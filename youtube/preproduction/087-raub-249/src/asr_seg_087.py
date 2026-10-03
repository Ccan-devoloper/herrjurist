"""Spracherkennung segmentweise (faster-whisper, Modell als Argument) mit Wortzeiten, Ausgabe im Format von asr_087.py
(woerter absolut, segmente), damit namen_087.py darauf laufen kann. Segmentweise statt am Stück, weil der Lauf am Stück
unter hoher Last zweimal abgebrochen wurde (03.10.2026); jedes Segment wird zwischengespeichert (../out/asr_seg_<modell>/),
ein erneuter Aufruf setzt dort fort. Aufruf: python3 asr_seg_087.py medium <ausgabe.json>"""
import json, os, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel

m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8", cpu_threads=2)
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
woerter, je = [], []
zw = f"../out/asr_seg_{sys.argv[1]}"; os.makedirs(zw, exist_ok=True)
for s in cj["segmente"]:
    f = f"{zw}/{s['i'] + 1:02d}.json"
    if os.path.exists(f):
        e = json.load(open(f)); woerter += e["woerter"]; je.append(e["segment"]); continue
    y = resample_poly(x[int(s["start"] * sr):int(s["ende"] * sr)], 1, 3).astype(np.float32)
    t, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False, word_timestamps=True)
    t = list(t)
    ww = [[round(s["start"] + v.start, 2), round(s["start"] + v.end, 2), v.word.strip()] for z in t for v in z.words]
    seg = dict(nr=s["i"] + 1, rolle=s["rolle"], skript=s["text"], erkannt=" ".join(z.text.strip() for z in t))
    json.dump(dict(woerter=ww, segment=seg), open(f, "w"), ensure_ascii=False)
    woerter += ww; je.append(seg)
    print(s["i"] + 1, flush=True)
json.dump(dict(modell=sys.argv[1], woerter=woerter, segmente=je), open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(len(woerter), "Wörter")
