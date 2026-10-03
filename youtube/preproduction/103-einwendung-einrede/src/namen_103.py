"""Namensprüfung Folge 103 (Vorgabe Kanalinhaber 01.10.2026: jeder Name klingt im ganzen Video gleich).
Jede Nennung eines Figurennamens (Wortzeiten aus ../cues.json) wird einzeln ausgeschnitten und
(1) mit der Spracherkennung im Satzzusammenhang abgeglichen (faster-whisper medium, Wortzeiten, asr.json),
(2) zusätzlich isoliert erkannt (Ausschnitt ±0,25 s, ohne Vorkontext, condition_on_previous_text=False),
(3) akustisch verglichen: MFCC (eigene Mel-Filterbank) + DTW-Abstand jeder Nennung zu allen übrigen Nennungen desselben
Namens; Ausreißer (> Median + 2,5 · MAD) werden markiert.
Zusätzlich: Gegenprobe der ganzen Sprachspur mit faster-whisper medium (Wortzeiten), gespeichert als <asr.json>.
Aufruf: python3 namen_103.py <asr.json> <ausgabe.json>   (asr.json wird erzeugt, falls nicht vorhanden)"""
import json, re, sys, wave
import numpy as np
from scipy.fft import dct
from scipy.signal import resample_poly

cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
NAMEN = ("Tilda", "Grünwald")


def mel_fb(n_fft=512, n_mel=26, sr=16000):
    hz = lambda m: 700 * (10 ** (m / 2595) - 1)
    mel = np.linspace(0, 2595 * np.log10(1 + sr / 2 / 700), n_mel + 2)
    bins = np.floor((n_fft + 1) * hz(mel) / sr).astype(int)
    fb = np.zeros((n_mel, n_fft // 2 + 1))
    for i in range(1, n_mel + 1):
        a, b, c = bins[i - 1], bins[i], bins[i + 1]
        fb[i - 1, a:b] = (np.arange(a, b) - a) / max(1, b - a)
        fb[i - 1, b:c] = (c - np.arange(b, c)) / max(1, c - b)
    return fb


FB = mel_fb()


def mfcc(y):
    y = resample_poly(y, 1, 3)
    fr = np.lib.stride_tricks.sliding_window_view(np.pad(y, (0, 400)), 400)[::160] * np.hamming(400)
    p = np.abs(np.fft.rfft(fr, 512)) ** 2
    m = dct(np.log(p @ FB.T + 1e-10), norm="ortho")[:, 1:13]
    return (m - m.mean(0)) / (m.std(0) + 1e-6)


def dtw(a, b):
    d = np.linalg.norm(a[:, None] - b[None], axis=2)
    D = np.full((len(a) + 1, len(b) + 1), np.inf); D[0, 0] = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i, j] = d[i - 1, j - 1] + min(D[i - 1, j], D[i, j - 1], D[i - 1, j - 1])
    return D[-1, -1] / (len(a) + len(b))


from faster_whisper import WhisperModel
modell = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=2)
import os
if not os.path.exists(sys.argv[1]):
    segs, _ = modell.transcribe("../stimme.wav", language="de", beam_size=5, word_timestamps=True)
    json.dump([(w.start, w.end, w.word) for s in segs for w in s.words], open(sys.argv[1], "w"), ensure_ascii=False)
asr = json.load(open(sys.argv[1]))
if isinstance(asr, dict):                       # Ausgabe von asr_103.py: {"woerter": [[a, b, wort], …]}
    asr = asr["woerter"]


def isoliert(a, b):
    y = x[max(0, int((a - 0.25) * sr)):int((b + 0.25) * sr)]
    y16 = resample_poly(y, 1, 3).astype(np.float32)
    segs, _ = modell.transcribe(y16, language="de", beam_size=5, condition_on_previous_text=False)
    return " ".join(s.text.strip() for s in segs)


nennungen = []
for si, s in enumerate(cj["segmente"]):
    for wd, (a, b) in zip(s["text"].split(), s["woerter"]):
        k = re.sub(r"[^\wäöüß]", "", wd)
        name = next((n for n in NAMEN if k == n or k == n + "s"), None)
        if not name:
            continue
        erkannt = " ".join(t for a2, b2, t in asr if a2 < b and b2 > a).strip()
        nennungen.append(dict(name=name, wort=k, segment=si + 1, sprecher=s["rolle"] or "Carla", t=round(a, 2),
                              video=round(a + 8.0, 1), dauer=round(b - a, 2), asr_satz=erkannt, asr_isoliert=isoliert(a, b),
                              m=mfcc(x[int(a * sr):int(b * sr)])))
for n in NAMEN:
    g = [e for e in nennungen if e["name"] == n and e["wort"] == n]
    for e in g:
        ds = [dtw(e["m"], f["m"]) for f in g if f is not e]
        e["dtw"] = round(float(np.median(ds)), 3) if ds else None
    werte = np.array([e["dtw"] for e in g if e["dtw"] is not None])
    if len(werte):
        med, mad = np.median(werte), np.median(np.abs(werte - np.median(werte))) + 1e-6
        for e in g:
            e["ausreisser"] = bool(e["dtw"] is not None and e["dtw"] > med + 2.5 * mad)
for e in nennungen:
    e.pop("m")
    e["asr_ok"] = e["wort"].lower()[:4] in re.sub(r"[^\wäöüß]", "", (e["asr_satz"] + e["asr_isoliert"]).lower())
json.dump(nennungen, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
for e in nennungen:
    print(e)
