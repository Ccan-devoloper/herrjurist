"""Vertont ein Skript (SEGMENTE mit [marke]) mit ElevenLabs v4 und legt jede Marke auf den Beginn des folgenden Wortes.

Aufruf im src-Ordner eines Videos:  python3 synth_el.py skript_xy [carla|moritz]  (Standard: carla)
- Segmente: (text, pause) für den Erzähler oder (text, pause, rolle) für Figurenrede; STIMMEN = {rolle: voice_id} im Skript.
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
ERZAEHLER = {"moritz": "PhufIH7nYh2Up1uej6aY", "carla": "rKiu7lQ4c5P3az3745s3"}
VOICE = ERZAEHLER["moritz"]
MODEL = "eleven_v4"
SETTINGS = {"stability": 0.42, "similarity_boost": 0.82, "style": 0.38, "use_speaker_boost": True, "speed": 1.08}
ROLLE_SETTINGS = {"stability": 0.35, "similarity_boost": 0.8, "style": 0.55, "use_speaker_boost": True, "speed": 1.05}
SR = 48000
ABK = ["VwVfG", "VwGO", "StGB", "StPO", "EStG", "BGB", "HGB", "ZPO", "AO", "GG", "UStG", "GmbHG", "AktG", "BVerfG", "BGH", "BFH", "BMF"]
MARKE = re.compile(r"\[(\w+)\]")


def sprechtext(t):
    t = t.replace("§§", "Paragrafen").replace("§", "Paragraf")
    for a in sorted(ABK, key=len, reverse=True):
        t = re.sub(rf"\b{a}\b", ".".join(a.upper()) + ".", t)
    return t


def entstoeren(pcm, sr=SR):
    """Bereinigt ein Segment ohne Längenänderung (Cue-Zeiten bleiben gültig, Cache bleibt nutzbar):
    - Restlaut am Segmentende: eine kurze laute Insel (≤ 0,2 s) nach ≥ 0,2 s Stille ist ein Artefakt
      (Stimme setzt neu an und wird abgeschnitten, hörbar als „Abbrechen“) und wird stummgeschaltet.
    - 8 ms Ein- und 15 ms Ausblendung gegen Knacken an den Segmentkanten.
    Gibt (pcm, Liste der bereinigten Restlaute in Sekunden) zurück."""
    x = pcm.astype(np.float32)
    h = int(0.01 * sr); n = len(x) // h
    if n < 3:
        return pcm, []
    db = 20 * np.log10(np.sqrt((x[: n * h].reshape(n, h) ** 2).mean(1)) / 32768 + 1e-9)
    laut = np.nonzero(db > -45)[0]
    entfernt = []
    if len(laut):
        inseln = np.split(laut, np.nonzero(np.diff(laut) > 1)[0] + 1)
        while len(inseln) > 1:
            letzte, davor = inseln[-1], inseln[-2]
            if (letzte[0] - davor[-1]) / 100 >= 0.2 and (letzte[-1] - letzte[0] + 1) / 100 <= 0.2:
                a0 = letzte[0] * h
                x[a0:] = 0.0
                entfernt.append(round(a0 / sr, 3))
                inseln = inseln[:-1]
            else:
                break
    ein, aus = int(0.008 * sr), int(0.015 * sr)
    x[:ein] *= np.linspace(0, 1, ein)
    x[-aus:] *= np.linspace(1, 0, aus)
    return np.clip(x, -32768, 32767).astype(np.int16), entfernt


ZIEL_LUFS = -19.0          # gemeinsame Lautheit aller Stimmen (Erzählerin und Figuren), Endmischung hebt auf ≈ −16 LUFS
KREDIT_PRO_ZEICHEN = 0.15  # gemessen Folge 001: 533 Credits / 4.420 Zeichen ≈ 0,12 (eleven_v4); 0,15 als Sicherheitsmarge


def angleichen(pcm, sr=SR, ziel=ZIEL_LUFS):
    """Bringt ein Segment auf ziel LUFS (ITU-R BS.1770, pyloudnorm), Verstärkung auf ±10 dB begrenzt,
    Spitze höchstens −1 dBFS. Kurze Segmente werden für die Messung wiederholt. Gibt (pcm, Messwert, Gain) zurück."""
    import pyloudnorm as pyln
    x = pcm.astype(np.float64) / 32768
    mess = x if len(x) >= 0.5 * sr else np.tile(x, int(0.5 * sr / max(1, len(x))) + 1)
    l = pyln.Meter(sr).integrated_loudness(mess)
    if not np.isfinite(l):
        return pcm, None, 0.0
    g = float(np.clip(ziel - l, -10, 10))
    spitze = np.abs(x).max() * 10 ** (g / 20)
    if spitze > 0.89:
        g -= 20 * np.log10(spitze / 0.89)
    y = x * 10 ** (g / 20)
    return np.clip(y * 32768, -32768, 32767).astype(np.int16), round(l, 1), round(g, 1)


def anfrage(route, body=None):
    req = urllib.request.Request(API + route, data=None if body is None else json.dumps(body, ensure_ascii=False).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "Herrjurist-production/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=240))


def main(modul, erzaehler="carla"):
    m = importlib.import_module(modul)
    SEGMENTE, STIMMEN = m.SEGMENTE, getattr(m, "STIMMEN", {})
    bes = os.path.join(os.path.dirname(os.path.abspath(__file__)), "besetzung.json")
    ens = json.load(open(bes))["ensemble"] if os.path.exists(bes) else {}
    vid_von = lambda s: ens[s]["id"] if s in ens else s          # Ensemble-Name oder direkte Voice-ID
    stimme_von = lambda rolle: (vid_von(STIMMEN[rolle]), ROLLE_SETTINGS) if rolle else (ERZAEHLER[erzaehler], SETTINGS)
    cache = "../el_cache"; os.makedirs(cache, exist_ok=True)
    teile = []
    for seg in SEGMENTE:
        roh, pause, rolle = (seg + (None,))[:3]
        stuecke = MARKE.split(roh)            # Text, Marke, Text, Marke, …
        text, marken = "", []
        for j, s in enumerate(stuecke):
            if j % 2:
                marken.append((s, len(text)))
            else:
                text += sprechtext(s)
        text = re.sub(r"\s+", " ", text)
        teile.append((text.strip(), marken, pause, len(text) - len(text.lstrip()), rolle))
    key = lambda t, r: hashlib.sha256(json.dumps([t, *stimme_von(r), MODEL], ensure_ascii=False).encode()).hexdigest()[:20]
    neu = [t for t, _, _, _, r in teile if not os.path.exists(f"{cache}/{key(t, r)}.json")]
    bedarf = sum(len(t) for t in neu)
    sub = anfrage("user/subscription")
    rest = int(sub["character_limit"]) - int(sub["character_count"])   # ElevenLabs zählt hier Credits, nicht Zeichen
    schaetzung = int(bedarf * KREDIT_PRO_ZEICHEN) + 1
    print(f"neu zu sprechen: {len(neu)} Segmente, {bedarf} Zeichen ≈ {schaetzung} Credits; Kontingent frei: {rest} Credits")
    if bedarf and rest < schaetzung + 200:
        sys.exit("Kontingent reicht nicht – keine Vertonung (keine automatische Mehrnutzung).")
    rest_vorher = rest
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    teile_audio, cues, segs, t = [np.zeros(int(0.4 * SR), np.int16)], {}, [], 0.4
    for i, (text, marken, pause, _, rolle) in enumerate(teile):
        vid, sett = stimme_von(rolle)
        k = key(text, rolle); js = f"{cache}/{k}.json"
        if not os.path.exists(js):
            vor = teile[i - 1][0] if i else None
            nach = teile[i + 1][0] if i + 1 < len(teile) else None
            body = {"text": text, "model_id": MODEL, "language_code": "de", "apply_text_normalization": "off",
                    "voice_settings": sett, "previous_text": vor, "next_text": nach}
            body = {a: b for a, b in body.items() if b is not None}
            try:
                r = anfrage(f"text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128", body)
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors="replace")
                if e.code == 400 and ("previous_text" in msg or "next_text" in msg):
                    body.pop("previous_text", None); body.pop("next_text", None)
                    r = anfrage(f"text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128", body)
                else:
                    sys.exit(f"HTTP {e.code}: {msg[:300]}")
            open(f"{cache}/{k}.mp3", "wb").write(base64.b64decode(r["audio_base64"]))
            json.dump({"text": text, "alignment": r.get("alignment") or r.get("normalized_alignment")}, open(js, "w"), ensure_ascii=False)
            print(f"  Segment {i + 1}/{len(teile)} gesprochen ({len(text)} Zeichen)")
        al = json.load(open(js))["alignment"]
        pcm = np.frombuffer(subprocess.run([ff, "-v", "error", "-i", f"{cache}/{k}.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                           capture_output=True, check=True).stdout, np.int16)
        pcm, l_vor, g = angleichen(pcm)
        pcm, rest = entstoeren(pcm)
        if l_vor is not None and abs(g) >= 1.5:
            print(f"  Segment {i + 1} ({rolle or 'Erzählerin'}): {l_vor} LUFS → {ZIEL_LUFS} LUFS ({g:+.1f} dB)")
        if rest:
            print(f"  Segment {i + 1}: Restlaut am Ende stummgeschaltet (bei {', '.join(f'{r:.2f}' for r in rest)} s im Segment)")
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
        ends = al["character_end_times_seconds"]
        woerter, w0 = [], None           # (Start, Ende) je Wort, absolut – für Mundbewegungen
        for j, ch in enumerate(chars + [" "]):
            if ch != " " and w0 is None: w0 = j
            if ch == " " and w0 is not None:
                woerter.append((round(t + starts[w0], 3), round(t + ends[j - 1], 3))); w0 = None
        segs.append(dict(i=i, start=round(t, 3), ende=round(t + d, 3), text=text, rolle=rolle, woerter=woerter))
        teile_audio += [pcm, np.zeros(int(pause * SR), np.int16)]
        t += d + pause
    alles = np.concatenate(teile_audio)
    import wave
    with wave.open("../stimme.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(alles.tobytes())
    json.dump(dict(dauer=round(len(alles) / SR, 3), sr=SR, stimme=f"ElevenLabs {MODEL}, Erzähler {erzaehler}", cues=cues, segmente=segs),
              open("../cues.json", "w"), ensure_ascii=False, indent=1)
    if neu:
        nach = anfrage("user/subscription")
        verbraucht = rest_vorher - (int(nach["character_limit"]) - int(nach["character_count"]))
        print(f"Credits verbraucht: {verbraucht} für {bedarf} Zeichen ({verbraucht / max(1, bedarf):.3f} je Zeichen)")
    print(f"Dauer {len(alles) / SR:.2f}s, {len(cues)} Marken, sha256 {hashlib.sha256(alles.tobytes()).hexdigest()[:16]}")


if __name__ == "__main__":
    sys.path.insert(0, ".")
    # Sperre: Vertonungen laufen nie gleichzeitig (Kontingentprüfung und Verbrauch bleiben eindeutig)
    import fcntl
    sperre = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".vertonung.lock"), "w")
    fcntl.flock(sperre, fcntl.LOCK_EX)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "carla")
