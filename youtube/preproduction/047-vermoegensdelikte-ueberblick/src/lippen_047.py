"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 047): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/047-Vermoegensdelikte-Ueberblick-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "klaus_k1": (15.0, 18.0, (940, 330, 1140, 500)),            # Klaus redet (Fall)
    "dagmar_bei_klaus": (15.0, 18.0, (1500, 330, 1700, 500)),   # Dagmar hört zu: Mund zu
    "klaus_k3": (158.0, 160.8, (1645, 480, 1845, 620)),         # Klaus droht (Variante 3)
    "dagmar_bei_k3": (158.0, 160.8, (1330, 480, 1530, 620)),
    "dagmar_d1": (187.5, 190.1, (1330, 480, 1530, 620)),        # Dagmar redet (Variante 4)
    "klaus_bei_d1": (187.5, 190.1, (1645, 480, 1845, 620)),
    "klaus_k2": (200.9, 202.7, (1645, 480, 1845, 620)),         # Klaus bittet (Variante 5)
    "lexi_tipp": (334.9, 338.6, (1450, 420, 1680, 580)),
    "lexi_merke": (392.3, 396.0, (1560, 280, 1800, 450)),
}
os.makedirs("../out/lip", exist_ok=True)
for name, (a, b, box) in F.items():
    n = int(round((b - a) * 10))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{a:.2f}", "-i", MP4, "-frames:v", str(n), "-vf",
                    f"fps=10,crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}", f"../out/lip/{name}_%03d.png"], check=True)
    bilder = [Image.open(f"../out/lip/{name}_{i:03d}.png") for i in range(1, n + 1) if os.path.exists(f"../out/lip/{name}_{i:03d}.png")]
    w, h = bilder[0].size; sc = min(1.0, 360 / w); w2, h2 = int(w * sc), int(h * sc); cols = 9
    s = Image.new("RGB", (cols * w2, ((len(bilder) + cols - 1) // cols) * (h2 + 18)), "white"); d = ImageDraw.Draw(s)
    for i, im in enumerate(bilder):
        x, y = (i % cols) * w2, (i // cols) * (h2 + 18)
        s.paste(im.resize((w2, h2)), (x, y)); d.text((x + 3, y + h2 + 2), f"{a + i * 0.1:.1f}s", fill=(0, 0, 0))
    s.save(f"../out/lip_{name}.png"); print(name, len(bilder))
