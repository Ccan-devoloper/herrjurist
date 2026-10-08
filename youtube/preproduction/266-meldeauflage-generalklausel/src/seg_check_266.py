"""Gegenprobe einzelner Segmente nach einer Nachvertonung (Folge 266): whisper small und medium je Segment.
Aufruf: python3 seg_check_266.py 19 [weitere Segmentnummern]"""
import json, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
for m in ("small", "medium"):
    mod = WhisperModel(m, device="cpu", compute_type="int8", cpu_threads=2)
    for n in map(int, sys.argv[1:]):
        s = cj["segmente"][n - 1]
        y = resample_poly(x[int(s["start"] * sr):int(s["ende"] * sr)], 1, 3).astype(np.float32)
        t, _ = mod.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
        print(f"[{m}] Seg {n} Video {s['start'] + 8:.1f} s: {' '.join(z.text.strip() for z in t)}", flush=True)
