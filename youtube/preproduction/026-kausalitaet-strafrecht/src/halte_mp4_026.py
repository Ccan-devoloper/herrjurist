"""Bildhalt-Kontaktbögen aus dem finalen Hauptfilm-MP4 (Folge 026): je eigenständigem Bildhalt ein Frame am Keyframe-Zeitpunkt
des Manifests (vor einer Schiebeblende: Ende − 16 Frames, sonst Ende − 0,08 s). Ausgabe ../out/mp4halte/, ../out/bildhalte_mp4_N.png."""
import json, os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
sys.path.insert(0, ".")
FF = imageio_ffmpeg.get_ffmpeg_exe()
m = json.load(open("../bildhalt_manifest.json"))
nach = {h["nr"]: (m["halte"][i + 1]["folie"] if i + 1 < len(m["halte"]) else None) for i, h in enumerate(m["halte"])}
os.makedirs("../out/mp4halte", exist_ok=True)
mp4 = "../out/026-Kausalitaet-Strafrecht-Hauptfilm.mp4"
halte = [h for h in m["halte"] if h["eigenstaendig"]]
for h in halte:
    vor_wisch = nach[h["nr"]] not in (None, h["folie"])          # nächster Halt auf neuer Folie → Schiebeblende folgt
    t = h["ende"] - (16 / 30 if vor_wisch else 0.08)
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-vf", "scale=480:270",
                    f"../out/mp4halte/{h['nr']:03d}.jpg"], check=True)
per = 30
for b in range(0, len(halte), per):
    part = halte[b:b + per]
    s = Image.new("RGB", (5 * 480, ((len(part) + 4) // 5) * 290), "white"); d = ImageDraw.Draw(s)
    for i, h in enumerate(part):
        s.paste(Image.open(f"../out/mp4halte/{h['nr']:03d}.jpg"), ((i % 5) * 480, (i // 5) * 290))
        d.text(((i % 5) * 480 + 4, (i // 5) * 290 + 272), f"#{h['nr']} ab {h['start']:.2f}s", fill=(0, 0, 0))
    s.save(f"../out/bildhalte_mp4_{b // per + 1}.png")
print(len(halte), "Bildhalte aus dem MP4")
