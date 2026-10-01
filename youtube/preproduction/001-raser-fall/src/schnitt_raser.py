"""Endschnitt: vollständiges Standardintro (8 s) + Hauptfilm + vollständiges Standardoutro, alles 1920×1080/30 fps,
H.264 yuv420p, AAC 48 kHz Stereo. Intro und Outro werden auf die Lautheit des Hauptfilms gebracht (EBU R128, −16 LUFS),
an den Schnitten nur 15 ms Audio-Blende gegen Knackser, kein Bildeffekt.

    python3 schnitt_raser.py --intro INTRO.mp4 --outro OUTRO.mp4 --haupt ../out/001-Raser-Fall-Hauptfilm.mp4 --out ZIEL.mp4
"""
import argparse, json, subprocess
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def dauer(pfad):
    r = subprocess.run([FF, "-i", pfad], capture_output=True, text=True).stderr
    h, m, s = r.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--intro", required=True); ap.add_argument("--outro", required=True)
    ap.add_argument("--haupt", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    teile = [a.intro, a.haupt, a.outro]
    flt = []
    for i, p in enumerate(teile):
        d = dauer(p)
        v = f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1[v{i}]"
        lautheit = "volume=2.5dB," if i == 1 else "loudnorm=I=-16:TP=-1.5:LRA=11,"   # Hauptfilm −18,9 → ≈ −16,4 LUFS, TP ≈ −1,4 dBTP
        au = (f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,{lautheit}"
              f"afade=t=in:d=0.015,afade=t=out:st={max(0, d - 0.015):.3f}:d=0.015,aresample=48000[a{i}]")
        flt += [v, au]
    flt.append("[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]")
    cmd = [FF, "-y", "-loglevel", "error"]
    for p in teile:
        cmd += ["-i", p]
    cmd += ["-filter_complex", ";".join(flt), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            "-movflags", "+faststart", "-sn", a.out]
    subprocess.run(cmd, check=True)
    print(json.dumps({"intro": round(dauer(a.intro), 3), "haupt": round(dauer(a.haupt), 3), "outro": round(dauer(a.outro), 3),
                      "gesamt": round(dauer(a.out), 3), "hauptfilm_ab": round(dauer(a.intro), 3)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
