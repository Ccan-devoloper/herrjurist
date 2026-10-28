"""Handlungsgeräusche Folge 174 aus Freesound CC0 (Vorschau-MP3 über die Freesound-API ohne Schlüssel, Abruf 04.10.2026):
zuerst zuschneiden, dann blenden (10 ms ein, 150 ms aus), 48 kHz mono 16 bit, Spitze auf −3 dBFS; Pegel im Mix setzt der Renderer.
Aufruf: python3 sfx_174.py <ordner mit 707864.mp3, 830195.mp3>   → ../../sfx3/szene_174hammer_1.wav, szene_174brief_1.wav"""
import subprocess, sys, wave, os
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
QUELLEN = {"szene_174hammer_1": ("707864", 0.12, 1.75), "szene_174brief_1": ("830195", 1.90, 3.30)}
for name, (fid, a, b) in QUELLEN.items():
    ziel = f"../../sfx3/{name}.wav"
    assert not os.path.exists(ziel) or "--neu" in sys.argv, f"existiert schon: {ziel}"
    x = np.frombuffer(subprocess.run([FF, "-v", "error", "-i", f"{sys.argv[1]}/{fid}.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                     capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    y = x[int(a * SR):int(b * SR)].copy()                      # 1. Zuschnitt
    ein, aus = int(0.010 * SR), int(0.150 * SR)                # 2. Blenden erst nach dem Zuschnitt
    y[:ein] *= np.linspace(0, 1, ein); y[-aus:] *= np.linspace(1, 0, aus)
    y = y / (np.abs(y).max() + 1e-9) * 10 ** (-3 / 20)
    with wave.open(ziel, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y * 32767).astype(np.int16).tobytes())
    print(name, round(len(y) / SR, 2), "s")
