"""Gegenprobe der Namensnennungen Folge 279 mit faster-whisper small: jede Nennung isoliert (±0,25 s und ±0,6 s)."""
import json, re, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=1)
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
for s in cj["segmente"]:
    for wd, (a, b) in zip(s["text"].split(), s["woerter"]):
        k = re.sub(r"[^\wäöüß]", "", wd)
        if k not in ("Telse", "Jost"):
            continue
        out = []
        for r in (0.25, 0.6):
            y = resample_poly(x[max(0, int((a - r) * sr)):int((b + r) * sr)], 1, 3).astype(np.float32)
            t, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
            out.append(" ".join(z.text.strip() for z in t))
        print(f"{k} Video {a + 8:.1f} s ({b - a:.2f} s): ±0,25 s „{out[0]}“ · ±0,6 s „{out[1]}“")
