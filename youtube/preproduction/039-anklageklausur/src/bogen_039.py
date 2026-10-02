"""Kontaktbogen aus Einzelbildern (Sichtprüfung): python3 bogen_039.py ZIEL.png BILD1.png BILD2.png … (3 Spalten)."""
import sys
from PIL import Image, ImageDraw
ziel, bilder = sys.argv[1], sys.argv[2:]
tw, th, cols = 640, 360, 3
rows = (len(bilder) + cols - 1) // cols
sh = Image.new("RGB", (cols * tw, rows * (th + 24)), "white"); d = ImageDraw.Draw(sh)
for i, b in enumerate(bilder):
    x, y = (i % cols) * tw, (i // cols) * (th + 24)
    sh.paste(Image.open(b).convert("RGB").resize((tw, th)), (x, y + 24)); d.text((x + 6, y + 6), b.split("/")[-1], fill="black")
sh.save(ziel)
