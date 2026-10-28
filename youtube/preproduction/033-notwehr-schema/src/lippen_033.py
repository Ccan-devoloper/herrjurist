"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 033): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/033-Notwehr-Schema-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "torsten_t1": (12.9, 14.4, (965, 430, 1165, 570)),            # Torsten redet
    "ulrike_bei_torsten": (12.9, 14.4, (670, 430, 870, 570)),     # Ulrike hört zu: Mund zu
    "ulrike_u1": (17.6, 20.6, (670, 430, 870, 570)),              # Ulrike redet
    "torsten_bei_ulrike": (17.6, 20.6, (965, 430, 1165, 570)),    # Torsten hört zu: Mund zu
    "kluge_kl1": (24.7, 26.6, (130, 430, 330, 570)),              # Herr Kluge redet
    "ulrike_bei_kluge": (24.7, 26.6, (670, 430, 870, 570)),       # Ulrike hört zu: Mund zu
    "lexi_tipp": (297.5, 301.5, (1440, 380, 1700, 560)),
    "lexi_merke": (347.3, 351.3, (1560, 250, 1820, 470)),
}
os.makedirs("../out/lip", exist_ok=True)
for name, (a, b, box) in F.items():
    n = int(round((b - a) * 10))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{a:.2f}", "-i", MP4, "-frames:v", str(n), "-vf",
                    f"fps=10,crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}", f"../out/lip/{name}_%03d.png"], check=True)
    bilder = [Image.open(f"../out/lip/{name}_{i:03d}.png") for i in range(1, n + 1) if os.path.exists(f"../out/lip/{name}_{i:03d}.png")]
    w, h = bilder[0].size; sc = min(1.0, 360 / w); w2, h2 = int(w * sc), int(h * sc); cols = 6
    s = Image.new("RGB", (cols * w2, ((len(bilder) + cols - 1) // cols) * (h2 + 18)), "white"); d = ImageDraw.Draw(s)
    for i, im in enumerate(bilder):
        x, y = (i % cols) * w2, (i // cols) * (h2 + 18)
        s.paste(im.resize((w2, h2)), (x, y)); d.text((x + 3, y + h2 + 2), f"{a + i * 0.1:.1f}s", fill=(0, 0, 0))
    s.save(f"../out/lip_{name}.png"); print(name, len(bilder))
