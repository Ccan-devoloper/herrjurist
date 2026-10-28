"""Gegenprobe Folge 052: auffällige Stellen der Spracherkennung isoliert erkennen (faster-whisper medium, ohne Vorkontext).
Aufruf: python3 asr_052.py VON-BIS[,VON-BIS…]  (Hauptfilmzeit in Sekunden) -> Ausgabe auf der Konsole"""
import sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
m = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "medium", device="cpu", compute_type="int8", cpu_threads=2)
for sp in sys.argv[1].split(","):
    a, b = map(float, sp.split("-"))
    y = resample_poly(x[int(a * sr):int(b * sr)], 1, 3).astype(np.float32)
    segs, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
    print(f"{a + 8:.1f}–{b + 8:.1f} s (Video):", " ".join(s.text.strip() for s in segs))
