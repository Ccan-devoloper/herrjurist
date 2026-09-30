"""Vertont ein Skript (SEGMENTE mit [marke]) mit ElevenLabs v4 und legt jede Marke auf den Beginn des folgenden Wortes.

Aufruf im src-Ordner eines Videos:  python3 synth_el.py skript_xy
- Sprecher, Modell und Einstellungen wie im Repo-Erzähler (Moritz Wegner), Modell eleven_v4, Normalisierung aus.
- Sprechtext-Aufbereitung: § → Paragraf, Gesetzesabkürzungen mit Punkten (B.G.B.), Paragrafenzahlen stehen im Skript
  bereits als Wort in Hunderter-Form.
- Wortzeiten aus den Zeichen-Zeitmarken von ElevenLabs (/with-timestamps).
- Jedes Segment wird nach Textinhalt gecacht (../el_cache): unveränderter Text wird nie erneut bezahlt.
- Bricht ab, wenn das enthaltene Kontingent nicht reicht (keine automatische Mehrnutzung).
"""
import base64, hashlib, importlib, json, os, re, subprocess, sys, urllib.request, urllib.error
import numpy as np
import imageio_ffmpeg

API = "https://api.elevenlabs.io/v1/"
VOICE = "PhufIH7nYh2Up1uej6aY"
MODEL = "eleven_v4"
SETTINGS = {"stability": 0.42, "similarity_boost": 0.82, "style": 0.38, "use_speaker_boost": True, "speed": 1.08}
SR = 48000
ABK = ["VwVfG", "VwGO", "StGB", "StPO", "EStG", "BGB", "HGB", "ZPO", "AO", "GG", "UStG", "GmbHG", "AktG", "BVerfG", "BGH", "BFH", "BMF"]
MARKE = re.compile(r"\[(\w+)\]")


def sprechtext(t):
    t = t.replace("§§", "Paragrafen").replace("§", "Paragraf")
    for a in sorted(ABK, key=len, reverse=True):
        t = re.sub(rf"\b{a}\b", ".".join(a.upper()) + ".", t)
    return t


def anfrage(route, body=None):
    req = urllib.request.Request(API + route, data=None if body is None else json.dumps(body, ensure_ascii=False).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "Herrjurist-production/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=240))


def main(modul):
    SEGMENTE = importlib.import_module(modul).SEGMENTE
    cache = "../el_cache"; os.makedirs(cache, exist_ok=True)
    teile = []
    for roh, pause in SEGMENTE:
        stuecke = MARKE.split(roh)            # Text, Marke, Text, Marke, …
        text, marken = "", []
        for j, s in enumerate(stuecke):
            if j % 2:
                marken.append((s, len(text)))
            else:
                text += sprechtext(s)
        text = re.sub(r"\s+", " ", text)
        teile.append((text.strip(), marken, pause, len(text) - len(text.lstrip())))
    key = lambda t: hashlib.sha256(json.dumps([t, VOICE, MODEL, SETTINGS], ensure_ascii=False).encode()).hexdigest()[:20]
    neu = [t for t, *_ in teile if not os.path.exists(f"{cache}/{key(t)}.json")]
    bedarf = sum(len(t) for t in neu)
    sub = anfrage("user/subscription")
    rest = int(sub["character_limit"]) - int(sub["character_count"])
    print(f"neu zu sprechen: {len(neu)} Segmente, {bedarf} Zeichen; Kontingent frei: {rest}")
    if bedarf and rest < bedarf + 200:
        sys.exit("Kontingent reicht nicht – keine Vertonung (keine automatische Mehrnutzung).")
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    teile_audio, cues, segs, t = [np.zeros(int(0.4 * SR), np.int16)], {}, [], 0.4
    for i, (text, marken, pause, _) in enumerate(teile):
        k = key(text); js = f"{cache}/{k}.json"
        if not os.path.exists(js):
            vor = teile[i - 1][0] if i else None
            nach = teile[i + 1][0] if i + 1 < len(teile) else None
            body = {"text": text, "model_id": MODEL, "language_code": "de", "apply_text_normalization": "off",
                    "voice_settings": SETTINGS, "previous_text": vor, "next_text": nach}
            body = {a: b for a, b in body.items() if b is not None}
            try:
                r = anfrage(f"text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128", body)
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors="replace")
                if e.code == 400 and ("previous_text" in msg or "next_text" in msg):
                    body.pop("previous_text", None); body.pop("next_text", None)
                    r = anfrage(f"text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128", body)
                else:
                    sys.exit(f"HTTP {e.code}: {msg[:300]}")
            open(f"{cache}/{k}.mp3", "wb").write(base64.b64decode(r["audio_base64"]))
            json.dump({"text": text, "alignment": r.get("alignment") or r.get("normalized_alignment")}, open(js, "w"), ensure_ascii=False)
            print(f"  Segment {i + 1}/{len(teile)} gesprochen ({len(text)} Zeichen)")
        al = json.load(open(js))["alignment"]
        pcm = np.frombuffer(subprocess.run([ff, "-v", "error", "-i", f"{cache}/{k}.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                           capture_output=True, check=True).stdout, np.int16)
        chars, starts = al["characters"], al["character_start_times_seconds"]
        assert "".join(chars) == text, "Zeitmarken passen nicht zum Text"
        for name, pos in marken:
            # erstes Nicht-Leerzeichen ab der Markenposition (Text wurde links gestrippt)
            p = pos - teile[i][3]
            while p < len(chars) and chars[p] == " ":
                p += 1
            assert name not in cues, f"Marke doppelt: {name}"
            cues[name] = dict(t=round(t + max(0.0, starts[min(p, len(chars) - 1)] - 0.04), 3), seg=i,
                              wort=text[p:].split(" ")[0] if p < len(text) else "")
        d = len(pcm) / SR
        segs.append(dict(i=i, start=round(t, 3), ende=round(t + d, 3), text=text))
        teile_audio += [pcm, np.zeros(int(pause * SR), np.int16)]
        t += d + pause
    alles = np.concatenate(teile_audio)
    import wave
    with wave.open("../stimme.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(alles.tobytes())
    json.dump(dict(dauer=round(len(alles) / SR, 3), sr=SR, stimme=f"ElevenLabs {MODEL} {VOICE}", cues=cues, segmente=segs),
              open("../cues.json", "w"), ensure_ascii=False, indent=1)
    print(f"Dauer {len(alles) / SR:.2f}s, {len(cues)} Marken, sha256 {hashlib.sha256(alles.tobytes()).hexdigest()[:16]}")


if __name__ == "__main__":
    sys.path.insert(0, ".")
    main(sys.argv[1])
