"""Endschnitt: vollständiges Standardintro (8 s) + Hauptfilm + vollständiges Standardoutro, alles 1920×1080/30 fps,
H.264 yuv420p, AAC 48 kHz Stereo. Intro, Hauptfilm und Outro werden per statischer Verstärkung (Intro/Outro mit Limiter) auf ≈ −16,5 LUFS gebracht,
an den Schnitten nur 15 ms Audio-Blende gegen Knackser, kein Bildeffekt.

    python3 schnitt.py --haupt HAUPTFILM.mp4 --out ZIEL.mp4 [--intro INTRO.mp4 --outro OUTRO.mp4]

Standard für Intro/Outro: youtube/preproduction/_quellen/ (lokaler Cache, nicht im Repository). Falls dort nichts liegt:
    rclone copy "lexverse:LexVerse Produktion/_Quellen" youtube/preproduction/_quellen --include "00-*.mp4"
"""
import argparse, json, os, subprocess
import imageio_ffmpeg

Q = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "preproduction", "_quellen")

FF = imageio_ffmpeg.get_ffmpeg_exe()


def dauer(pfad):
    r = subprocess.run([FF, "-i", pfad], capture_output=True, text=True).stderr
    h, m, s = r.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--intro", default=os.path.join(Q, "00-LexVerse-Standardintro-16x9-ORIGINAL.mp4"))
    ap.add_argument("--outro", default=os.path.join(Q, "00-Herrjurist-Standardoutro-16x9.mp4"))
    ap.add_argument("--haupt", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    teile = [a.intro, a.haupt, a.outro]
    flt = []
    for i, p in enumerate(teile):
        d = dauer(p)
        v = f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1[v{i}]"
        # Statische Pegel (gemessen 01.10.2026), Limiter bei −1,5 dBFS: Intro −17,4 LUFS/−0,5 dBFS, Outro −21,8/−3,0,
        # Hauptfilm −18,9/−3,9. Ziel ≈ −16,5 LUFS für alle Teile; einpassiges loudnorm verfehlt kurze Musik deutlich.
        lautheit = ["volume=1dB,alimiter=limit=0.84:level=disabled,", "volume=2.5dB,",
                    "volume=4.5dB,alimiter=limit=0.84:level=disabled,"][i]
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
