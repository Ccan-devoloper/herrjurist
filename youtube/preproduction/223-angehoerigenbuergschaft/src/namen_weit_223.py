"""Ergänzung zu namen_223.py: Nennungen mit breiterem Fenster (±0,9 s) isoliert erkennen, je mit whisper small und medium,
weil das ±0,25-s-Fenster bei „Steffens“ in Folge 217 eine Halluzination lieferte. Aufruf: python3 namen_weit_223.py > ../out/namen_weit.log"""
import json, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
n = json.load(open("../out/namen.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
for mod in ("small", "medium"):
    m = WhisperModel(mod, device="cpu", compute_type="int8", cpu_threads=2)
    for e in n:
        y = resample_poly(x[max(0, int((e["t"] - 0.9) * sr)):int((e["t"] + e["dauer"] + 0.9) * sr)], 1, 3).astype(np.float32)
        s, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
        print(mod, e["name"], f"Video {e['video']} s", e["sprecher"], "->", " ".join(t.text.strip() for t in s), flush=True)
