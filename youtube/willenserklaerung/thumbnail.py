#!/usr/bin/env python3
"""Create the matching 16:9 YouTube cover from the approved bicycle art."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

here = Path(__file__).resolve().parent
canvas = Image.open(here / "assets/scene-offer.jpg").convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).convert("RGBA")
layer = Image.new("RGBA", canvas.size)
d = ImageDraw.Draw(layer)
font = ImageFont.truetype(str(here.parent.parent / "fonts/SpaceGrotesk.ttf"), 51)
text = "WILLENSERKLÄRUNG"
box = d.textbbox((0, 0), text, font=font)
width = box[2] - box[0]
left = (1280 - width) // 2 - 30
d.rounded_rectangle((left, 18, left + width + 60, 102), radius=21, fill=(8, 24, 67, 239))
d.text(((1280 - width) // 2, 31), text, font=font, fill=(255, 255, 255, 255))
canvas = Image.alpha_composite(canvas, layer)
canvas.convert("RGB").save(here / "willenserklaerung-thumbnail.jpg", quality=94, subsampling=0)
