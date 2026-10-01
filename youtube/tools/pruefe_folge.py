#!/usr/bin/env python3
"""Automatische Ton- und Technikprüfung einer Folge (Serienstandard Open Peeps). Ersetzt keine menschliche Hör-/Sichtprüfung.

    python3 pruefe_folge.py ORDNER [--mp4 ORDNER/out/NNN-Titel.mp4] [--asr]

ORDNER ist der Produktionsordner (enthält cues.json und stimme.wav). Prüft:
- Lautheit je Sprachsegment und Sprecher (ITU-R BS.1770); Ziel: alle Sprecher innerhalb ±1,5 LU
- Segmentkanten: Energie in den letzten 20 ms und kurze Restlaute nach Stille (abgeschnittene Satzenden)
- mit --asr: Spracherkennung (faster-whisper small) gegen den Skripttext, Abweichungen mit Zeitstempel
- mit --mp4: Streams (H.264/yuv420p/1920×1080/30 fps, AAC 48 kHz Stereo, keine Untertitelspur), vollständiger
  Fehler-Decode, Lautheit und Spitze für Intro (0–8 s), Hauptfilm und Outro
Ergebnis: ORDNER/pruefbericht.json und eine Zusammenfassung auf der Konsole; Exit-Code 1 bei hartem Fehler.
"""
import argparse, difflib, json, os, re, subprocess, sys, wave
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 48000


def lufs(x):
    import pyloudnorm as pyln
    if len(x) < 0.5 * SR:
        x = np.tile(x, int(0.5 * SR / max(1, len(x))) + 1)
    return float(pyln.Meter(SR).integrated_loudness(x))


def ton(ordner):
    cj = json.load(open(os.path.join(ordner, "cues.json")))
    w = wave.open(os.path.join(ordner, "stimme.wav"))
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64) / 32768
    seg, kanten, je = [], [], {}
    for s in cj["segmente"]:
        a, b = int(s["start"] * SR), int(s["ende"] * SR)
        l = round(lufs(x[a:b]), 1)
        wer = s["rolle"] or "Erzählerin"
        je.setdefault(wer, []).append(l)
        seg.append(dict(nr=s["i"] + 1, sprecher=wer, lufs=l))
        h = int(0.01 * SR); t = x[a:b]; n = len(t) // h
        db = 20 * np.log10(np.sqrt((t[: n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
        ende = 20 * np.log10(np.sqrt(np.mean(t[-int(0.02 * SR):] ** 2)) + 1e-9)
        laut = np.nonzero(db > -45)[0]
        rest = False
        if len(laut):
            inseln = np.split(laut, np.nonzero(np.diff(laut) > 1)[0] + 1)
            if len(inseln) > 1 and (inseln[-1][0] - inseln[-2][-1]) / 100 >= 0.2 and len(inseln[-1]) <= 20:
                rest = True
        if ende > -40 or rest:
            kanten.append(dict(nr=s["i"] + 1, ende_db=round(float(ende), 1), restlaut=rest, zeit=round(s["ende"], 2)))
    mittel = {k: round(float(np.mean(v)), 1) for k, v in je.items()}
    spanne = round(max(mittel.values()) - min(mittel.values()), 1)
    return dict(segmente=seg, mittel_je_sprecher=mittel, spanne_lu=spanne, kanten=kanten)


def asr(ordner):
    from faster_whisper import WhisperModel
    cj = json.load(open(os.path.join(ordner, "cues.json")))
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(os.path.join(ordner, "stimme.wav"), language="de", beam_size=5, word_timestamps=True)
    hyp = [(w.word, w.start) for s in segs for w in s.words]
    ref = [(w, a) for s in cj["segmente"] for w, (a, b) in zip(s["text"].split(), s["woerter"])]
    norm = lambda t: re.sub(r"[^a-zäöüß0-9]", "", t.lower())
    r, h = [norm(w) for w, _ in ref], [norm(w) for w, _ in hyp]
    sm = difflib.SequenceMatcher(a=r, b=h, autojunk=False)
    zahl = re.compile(r"^\d+$")
    abw = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == "equal":
            continue
        gehoert = " ".join(w for w, _ in hyp[b0:b1]).strip()
        if gehoert and all(zahl.match(norm(w)) or norm(w) in ("paragraf", "paragrafen") for w, _ in hyp[b0:b1]):
            continue                                   # nur Zahlschreibweise (Skript: Zahlwort, Erkennung: Ziffern)
        t = ref[a0][1] if a0 < len(ref) else ref[-1][1]
        abw.append(dict(zeit=round(t, 2), skript=" ".join(w for w, _ in ref[a0:a1]), gehoert=gehoert))
    return dict(uebereinstimmung=round(sm.ratio(), 3), abweichungen=abw)


def mp4(pfad, intro=8.0):
    pr = subprocess.run([FF, "-hide_banner", "-i", pfad], capture_output=True, text=True).stderr
    dauer = pr.split("Duration: ")[1].split(",")[0]
    h, mi, se = dauer.split(":"); dauer = int(h) * 3600 + int(mi) * 60 + float(se)
    video = [l for l in pr.splitlines() if "Video:" in l]
    audio = [l for l in pr.splitlines() if "Audio:" in l]
    untertitel = [l for l in pr.splitlines() if "Subtitle:" in l]
    dec = subprocess.run([FF, "-hide_banner", "-v", "error", "-xerror", "-i", pfad, "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"],
                         capture_output=True, text=True)

    def laut(ss, t):
        r = subprocess.run([FF, "-hide_banner", "-ss", str(ss), "-t", str(t), "-i", pfad, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r); p = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)
        return dict(lufs=float(i[-1]) if i else None, spitze=float(p[-1]) if p else None)

    outro = 15.08
    teile = dict(intro=laut(0, intro), hauptfilm=laut(intro, dauer - intro - outro), outro=laut(dauer - outro, outro),
                 gesamt=laut(0, dauer))
    ok = (len(video) == 1 and "h264" in video[0] and "yuv420p" in video[0] and "1920x1080" in video[0] and " 30 fps" in video[0]
          and len(audio) == 1 and "aac" in audio[0] and "48000 Hz" in audio[0] and "stereo" in audio[0] and not untertitel
          and dec.returncode == 0 and not dec.stderr.strip())
    return dict(datei=os.path.basename(pfad), dauer=round(dauer, 2), video=video[0].strip() if video else None,
                audio=audio[0].strip() if audio else None, untertitelspur=bool(untertitel), decode_fehlerfrei=dec.returncode == 0
                and not dec.stderr.strip(), lautheit=teile, technik_ok=ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ordner"); ap.add_argument("--mp4"); ap.add_argument("--asr", action="store_true")
    a = ap.parse_args()
    bericht = dict(ton=ton(a.ordner))
    if a.asr:
        bericht["asr"] = asr(a.ordner)
    if a.mp4:
        bericht["mp4"] = mp4(a.mp4)
    json.dump(bericht, open(os.path.join(a.ordner, "pruefbericht.json"), "w"), ensure_ascii=False, indent=1)
    t = bericht["ton"]
    print("Lautheit je Sprecher:", t["mittel_je_sprecher"], "Spanne", t["spanne_lu"], "LU", "OK" if t["spanne_lu"] <= 1.5 else "ZU GROSS")
    print("Segmentkanten auffällig:", t["kanten"] or "keine")
    if a.asr:
        print("Spracherkennung:", bericht["asr"]["uebereinstimmung"], "Abweichungen (ohne Zahlschreibweise):")
        for d in bericht["asr"]["abweichungen"]:
            print(f"  {d['zeit']:7.2f}s  Skript: {d['skript']!r}  gehört: {d['gehoert']!r}")
    if a.mp4:
        m = bericht["mp4"]
        print("MP4:", m["dauer"], "s, Technik", "OK" if m["technik_ok"] else "FEHLER", "| Lautheit:",
              {k: v["lufs"] for k, v in m["lautheit"].items()}, "| Spitze gesamt:", m["lautheit"]["gesamt"]["spitze"])
    hart = t["spanne_lu"] > 1.5 or any(k["restlaut"] for k in t["kanten"]) or (a.mp4 and not bericht["mp4"]["technik_ok"])
    sys.exit(1 if hart else 0)


if __name__ == "__main__":
    main()
