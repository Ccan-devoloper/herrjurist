"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 029): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/029-Vorsatzformen-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "heike_volker": (12.3, 17.4, (220, 430, 1440, 600)),        # Heike redet, dann Volker; der jeweils andere hat den Mund zu
    "heike_ruft": (26.7, 28.9, (220, 430, 1440, 600)),
    "volker_v1": (92.1, 95.0, (1690, 390, 1890, 540)),
    "volker_v2": (120.2, 123.7, (1690, 390, 1890, 540)),
    "volker_v3": (174.4, 177.4, (1690, 390, 1890, 540)),
    "volker_v4": (206.1, 208.9, (1710, 420, 1900, 560)),
    "lexi_tipp": (273.2, 276.9, (1440, 300, 1700, 520)),
    "lexi_merke": (335.1, 338.8, (1560, 250, 1820, 470)),
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
