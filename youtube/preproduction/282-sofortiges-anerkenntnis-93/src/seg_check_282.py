"""Gezielte Spracherkennung einzelner Segmente (whisper small und medium) nach einer Nachvertonung.
Aufruf: python3 seg_check_282.py 4,27"""
import json, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
nr = [int(v) for v in sys.argv[1].split(",")]
for mod in ("small", "medium"):
    m = WhisperModel(mod, device="cpu", compute_type="int8", cpu_threads=2)
    for n in nr:
        s = cj["segmente"][n - 1]
        y = resample_poly(x[int(s["start"] * sr):int(s["ende"] * sr)], 1, 3).astype(np.float32)
        t, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
        print(mod, n, " ".join(z.text.strip() for z in t), flush=True)
