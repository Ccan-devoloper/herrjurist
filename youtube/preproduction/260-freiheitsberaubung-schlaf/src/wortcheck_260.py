"""Gezielte Gegenprobe einzelner Wörter (Folge 260): schneidet jede Nennung (ElevenLabs-Wortzeiten aus ../cues.json) mit
±0,35 s Rand aus und lässt sie von whisper small und medium isoliert erkennen (ohne Vorkontext).
Aufruf: python3 wortcheck_260.py wort1 wort2 …   (Wortanfang, Groß-/Kleinschreibung egal)"""
import json, re, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
ziele = [a.lower() for a in sys.argv[1:]]
treffer = []
for si, s in enumerate(cj["segmente"]):
    for wd, (a, b) in zip(s["text"].split(), s["woerter"]):
        k = re.sub(r"[^\wäöüß]", "", wd).lower()
        if any(k.startswith(z) for z in ziele):
            treffer.append((si + 1, wd, a, b))
for m in ("small", "medium"):
    mod = WhisperModel(m, device="cpu", compute_type="int8", cpu_threads=2)
    for si, wd, a, b in treffer:
        y = resample_poly(x[max(0, int((a - 0.35) * sr)):int((b + 0.35) * sr)], 1, 3).astype(np.float32)
        t, _ = mod.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
        print(f"[{m}] Seg {si} {wd!r} Video {a + 8:.1f} s -> {' '.join(z.text.strip() for z in t)!r}", flush=True)
