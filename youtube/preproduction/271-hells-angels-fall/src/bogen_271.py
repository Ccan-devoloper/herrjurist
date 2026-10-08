"""Kontaktbögen der Bildhalt-Keyframes (Folge 271) aus dem Manifest-Lauf (../out/bildhalte/*.jpg) zur Sichtprüfung vor dem Vollrender."""
from PIL import Image, ImageDraw
import glob, json
man = json.load(open('../bildhalt_manifest.json'))
fs = sorted(glob.glob('../out/bildhalte/*.jpg'))
eig = [h for h in man['halte'] if h['eigenstaendig']]
for k in range(0, len(fs), 30):
    sh = Image.new('RGB', (5 * 480, 6 * 292), 'white'); d = ImageDraw.Draw(sh)
    for i, f in enumerate(fs[k:k + 30]):
        x, y = (i % 5) * 480, (i // 5) * 292
        sh.paste(Image.open(f), (x, y + 22)); h = eig[k + i]
        d.text((x + 4, y + 4), f"{k + i + 1:03d}  {h['start']:.1f}-{h['ende']:.1f}s", fill=(200, 0, 0))
    sh.save(f'../out/manifest_bogen_{k // 30 + 1}.png')
print(len(fs))
