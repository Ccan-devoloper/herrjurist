import sys, json
sys.argv = ["render_kk.py", "--vorschau", "--out", "../out"]
src = open("render_kk.py").read().split("if nur_vorschau:")[0]
exec(src)
from PIL import Image
c = json.load(open("../cues.json"))["cues"]
punkte = [(n, float(dt)) for n, dt in (x.split(":") for x in sys.stdin.read().split())]
ims = []
for n, dt in punkte:
    im, _ = frame(c[n]["t"] + dt); ims.append(im.convert("RGB").resize((640, 360)))
s = Image.new("RGB", (1920, 360 * ((len(ims) + 2) // 3)))
for i, im in enumerate(ims): s.paste(im, ((i % 3) * 640, (i // 3) * 360))
s.save("../out/probe.png")
