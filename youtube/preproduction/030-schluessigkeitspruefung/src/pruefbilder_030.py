"""Prüfbilder aus dem fertigen MP4 (Sichtprüfung Folge 030).
  python3 pruefbilder_030.py bildhalte MP4 VERSATZ      -> ../out/bh_mp4/NNN.jpg + ../out/bildhalte_mp4_K.png (je 30 Bildhalte)
  python3 pruefbilder_030.py lippen MP4 VERSATZ NAME T0 T1 X Y W H [X Y W H …]
                                                       -> ../out/lippen_NAME.png (0,1-s-Schritte, Ausschnitte nebeneinander)
VERSATZ = Beginn des Hauptfilms im MP4 (Hauptfilm-MP4: 0, Endschnitt: 8,0). Bildhalt-Zeitpunkt = Mitte des Halts."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
OUT = "../out"


def bild(mp4, t):
    r = subprocess.run([FF, "-v", "error", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True, check=True)
    import io
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


def bildhalte(mp4, vers):
    man = json.load(open("../bildhalt_manifest.json"))
    os.makedirs(f"{OUT}/bh_mp4", exist_ok=True)
    halte = [h for h in man["halte"] if h["eigenstaendig"]]
    tw, th, cols, je = 480, 270, 5, 30
    for k in range(0, len(halte), je):
        teil = halte[k:k + je]
        rows = (len(teil) + cols - 1) // cols
        sh = Image.new("RGB", (cols * tw, rows * (th + 22)), "white"); d = ImageDraw.Draw(sh)
        for i, h in enumerate(teil):
            t = (h["start"] + h["ende"]) / 2 + vers
            im = bild(mp4, t); im.save(f"{OUT}/bh_mp4/{h['nr']:03d}.jpg", quality=85)
            x, y = (i % cols) * tw, (i // cols) * (th + 22)
            sh.paste(im.resize((tw, th)), (x, y + 22))
            d.text((x + 4, y + 4), f"#{h['nr']}  {h['start']:.2f}–{h['ende']:.2f}s  {h['pruefpfad'][:48]}", fill="black")
        sh.save(f"{OUT}/bildhalte_mp4_{k // je + 1}.png")
    print(len(halte), "Bildhalte aus", mp4)


def lippen(mp4, vers, name, t0, t1, boxen):
    n = int(round((t1 - t0) / 0.1)) + 1
    spalten = 12
    bw = sum(b[2] for b in boxen) + 10 * (len(boxen) - 1)
    bh = max(b[3] for b in boxen)
    rows = (n + spalten - 1) // spalten
    sh = Image.new("RGB", (spalten * (bw + 8), rows * (bh + 20)), "white"); d = ImageDraw.Draw(sh)
    for i in range(n):
        t = t0 + i * 0.1
        im = bild(mp4, t + vers)
        x, y = (i % spalten) * (bw + 8), (i // spalten) * (bh + 20)
        xx = x
        for (bx, by, w, h) in boxen:
            sh.paste(im.crop((bx, by, bx + w, by + h)), (xx, y + 20)); xx += w + 10
        d.text((x + 2, y + 3), f"{t:.1f}", fill="black")
    sh.save(f"{OUT}/lippen_{name}.png")
    print("lippen", name, n, "Bilder")


if __name__ == "__main__":
    art, mp4, vers = sys.argv[1], sys.argv[2], float(sys.argv[3])
    if art == "bildhalte":
        bildhalte(mp4, vers)
    else:
        name, t0, t1 = sys.argv[4], float(sys.argv[5]), float(sys.argv[6])
        z = list(map(int, sys.argv[7:]))
        lippen(mp4, vers, name, t0, t1, [tuple(z[i:i + 4]) for i in range(0, len(z), 4)])
