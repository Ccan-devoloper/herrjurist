"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 047): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/047-Vermoegensdelikte-Ueberblick-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "florian_f1": (16.8, 19.5, (1320, 450, 1520, 600)),          # Florian redet
    "britta_bei_florian": (16.8, 19.5, (1635, 450, 1835, 600)),  # Britta hört zu: Mund zu
    "britta_b1": (19.5, 21.8, (1635, 450, 1835, 600)),           # Britta redet
    "florian_bei_britta": (19.5, 21.8, (1320, 450, 1520, 600)),  # Florian hört zu: Mund zu
    "florian_f2": (123.4, 126.1, (1600, 430, 1800, 580)),
    "lexi_tipp": (359.8, 363.5, (1450, 400, 1680, 560)),
    "lexi_merke": (401.2, 404.9, (1560, 260, 1800, 430)),
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
