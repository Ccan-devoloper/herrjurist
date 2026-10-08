"""Handlungsgeräusche Folge 274 aus Freesound CC0 (Vorschau-MP3 der API, Abruf 08.10.2026): zuschneiden, erst danach
blenden, Spitze normalisieren, 48 kHz mono nach ../../sfx3/szene_274<name>_1.wav (eigene Dateinamen, nichts überschrieben).
Aufruf: python3 sfx_274.py <ordner mit raw_<id>.wav>"""
import os, sys, wave
import numpy as np

QUELLE = sys.argv[1]
ZIEL = "../../sfx3/"
# name: (Freesound-ID, Schnitt von, bis [s], Einblendung, Ausblendung [s])
JOBS = {"274saege": (390713, 0.6, 3.2, 0.15, 0.6), "274papier": (429298, 1.15, 2.05, 0.01, 0.15)}
for name, (fid, a, b, ein, aus) in JOBS.items():
    w = wave.open(f"{QUELLE}/raw_{fid}.wav"); sr = w.getframerate(); assert sr == 48000
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    x = x[int(a * sr):int(b * sr)].copy()
    ne, na = int(ein * sr), int(aus * sr)
    x[:ne] *= np.linspace(0, 1, ne); x[-na:] *= np.linspace(1, 0, na)
    x = x / (np.abs(x).max() + 1e-9) * 0.9
    p = f"{ZIEL}szene_{name}_1.wav"
    assert not os.path.exists(p), f"{p} existiert schon"
    with wave.open(p, "wb") as o:
        o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes((x * 32767).astype(np.int16).tobytes())
    print(p, round(len(x) / sr, 3), "s")
