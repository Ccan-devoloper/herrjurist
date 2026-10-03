"""Gegenprobe Folge 090: einzelne Stellen der Sprachspur (Hauptfilmzeit, Fenster) isoliert mit whisper small und medium
erkennen (ohne Vorkontext). Aufruf: python3 isoliert_090.py <ausgabe.json> t0:t1 [t0:t1 …]"""
import json, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel

w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
fenster = [tuple(map(float, a.split(":"))) for a in sys.argv[2:]]
erg = []
for modell in ("small", "medium"):
    m = WhisperModel(modell, device="cpu", compute_type="int8", cpu_threads=2)
    for a, b in fenster:
        y = resample_poly(x[int(a * sr):int(b * sr)], 1, 3).astype(np.float32)
        segs, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
        erg.append(dict(modell=modell, von=a, bis=b, video=round(a + 8.0, 1), text=" ".join(s.text.strip() for s in segs)))
        print(erg[-1])
json.dump(erg, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
