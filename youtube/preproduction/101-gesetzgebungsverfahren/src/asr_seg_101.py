"""Gegenprobe einzelner Segmente mit faster-whisper (Modell als Argument). Aufruf: python3 asr_seg_101.py small 7 16 17"""
import json, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8", cpu_threads=2)
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
for nr in map(int, sys.argv[2:]):
    s = cj["segmente"][nr - 1]
    y = resample_poly(x[int(s["start"] * sr):int(s["ende"] * sr)], 1, 3).astype(np.float32)
    t, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
    print(nr, " ".join(z.text.strip() for z in t))
