"""Vertonung der Reels mit ElevenLabs (Stimme Laura, eleven_v4) samt Wortzeiten.

Kosten: nur das Zeichenkontingent des ElevenLabs-Abos; Ergebnisse werden je Text zwischengespeichert, ein erneutes
Rendern desselben Textes kostet nichts. Der Proxy der Laufumgebung bzw. ELEVENLABS_API_KEY authentifiziert.
Die Gesamtlänge wird mit atempo (tonhöhenneutral) auf höchstens ZIEL_S gestrafft, höchstens um MAX_TEMPO.
"""
import base64, hashlib, json, os, re, subprocess, urllib.request, wave
import numpy as np
import imageio_ffmpeg
import opkern

VOICE = os.environ.get("OP_STIMME", "zKHQdbB8oaQ7roNTiDTK")      # Laura
MODEL = os.environ.get("OP_STIMM_MODELL", "eleven_v4")
SETT = {"stability": 0.42, "similarity_boost": 0.82, "style": 0.4, "use_speaker_boost": True, "speed": 1.2}
SR = 48000
ZIEL_S, MAX_TEMPO = opkern.MARKE["reelZielS"], 1.12
CACHE = os.path.join(opkern.RES, "cache", "tts")
os.makedirs(CACHE, exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()


def _tts(text, vor, nach):
    body = {"text": text, "model_id": MODEL, "language_code": "de", "voice_settings": SETT}
    if vor: body["previous_text"] = vor
    if nach: body["next_text"] = nach
    kopf = {"Content-Type": "application/json"}
    if os.environ.get("ELEVENLABS_API_KEY"): kopf["xi-api-key"] = os.environ["ELEVENLABS_API_KEY"]
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128",
                                 data=json.dumps(body).encode(), headers=kopf)
    return json.load(urllib.request.urlopen(req, timeout=180))


def _trocken(text):
    """Ohne API: Zeichenzeiten geschätzt (≈ 11,5 Zeichen/s wie Laura bei speed 1.2), nur zum Prüfen von Aufbau und Länge."""
    zeichen, st, en, t = list(text), [], [], 0.0
    for ch in zeichen:
        st.append(t); t += 1 / 11.5; en.append(t)
    return None, {"characters": zeichen, "character_start_times_seconds": st, "character_end_times_seconds": en}


def _segment(text, vor, nach):
    if os.environ.get("OP_TTS_TROCKEN"):
        return _trocken(text)
    key = hashlib.sha1(json.dumps([VOICE, MODEL, SETT, text, vor, nach]).encode()).hexdigest()[:16]
    js, mp3 = os.path.join(CACHE, key + ".json"), os.path.join(CACHE, key + ".mp3")
    if not os.path.exists(js):
        r = _tts(text, vor, nach)
        open(mp3, "wb").write(base64.b64decode(r["audio_base64"]))
        json.dump({"text": text, "al": r.get("alignment") or r.get("normalized_alignment")}, open(js, "w"), ensure_ascii=False)
    return mp3, json.load(open(js))["al"]


FR = SR // 100                                      # 10-ms-Rahmen


def _huelle(pcm):
    n = len(pcm) // FR
    x = pcm[:n * FR].astype(np.float32).reshape(n, FR)
    return np.sqrt((x ** 2).mean(axis=1))


def _grenzen(pcm, zeichen, st, en):
    """Schnittpunkte an echten Pausen. eleven_v4 spricht mit previous_text/next_text am Segmentanfang oft den Rest des
    vorigen und am Ende den Anfang des nächsten Satzes an – ein fester Schnitt an den Zeichenzeiten lässt diese
    Silbenfetzen stehen. Gesucht wird darum vom ersten bzw. letzten Buchstaben aus die nächste Stille (≥ 40 ms)."""
    if not len(pcm):
        return 0.0, en[-1] + 0.12
    h = _huelle(pcm); still = h < max(h.max() * 0.025, 60)
    bu = [i for i, c in enumerate(zeichen) if c.isalnum()] or [0, len(zeichen) - 1]
    f0, f1 = int(st[bu[0]] * 100), min(len(h) - 1, int(en[bu[-1]] * 100))
    a = f0
    while a > 0 and not still[max(0, a - 4):a].all(): a -= 1
    b = f1
    while b < len(h) - 4 and not still[b:b + 4].all(): b += 1
    return max(0.0, a / 100 - 0.03), min(len(pcm) / SR, b / 100 + 0.05)


def _blende(pcm, ms=8):
    """Kurze Ein-/Ausblendung gegen Knackser an den Schnittkanten."""
    n = min(len(pcm) // 2, SR * ms // 1000)
    if n <= 0: return pcm
    x = pcm.astype(np.float32); r = np.linspace(0, 1, n)
    x[:n] *= r; x[-n:] *= r[::-1]
    return x.astype(np.int16)


AUSSPRACHE = re.compile(r"§|\d|\b(?:Abs|Nr|Art|Alt|Var|bzw|ggf|vgl|usw|insb|S|z\. ?B|i\. ?V\. ?m|d\. ?h|u\. ?a)\.|\b\w*[A-ZÄÖÜ]\w*[A-ZÄÖÜ]\w*\b")
ERLAUBT = {"KG", "AG", "OHG", "GmbH", "GbR", "UG", "EU"}


def aussprache_pruefen(text):
    """Was die Stimme falsch oder buchstabiert sprechen würde: Paragrafenzeichen, Ziffern, Abkürzungen mit Punkt und
    Großbuchstaben-Kürzel (außer gängigen Rechtsformen). Im Sprechertext gehört alles ausgeschrieben."""
    return sorted({m.group(0) for m in AUSSPRACHE.finditer(text)} - ERLAUBT)


def vertonen(segmente, ziel_wav, pausen=None):
    """segmente: [(id, text)]. Schreibt ziel_wav und gibt {dauer, segmente:[{name, start, ende, woerter}]} zurück."""
    roh = []
    for i, (name, text) in enumerate(segmente):
        mp3, al = _segment(text, segmente[i - 1][1] if i else None, segmente[i + 1][1] if i + 1 < len(segmente) else None)
        roh.append((name, text, mp3, al))
    pausen = pausen or {}
    def laenge(tempo):
        t = 0.15
        for name, _, _, al in roh:
            st, en = al["character_start_times_seconds"], al["character_end_times_seconds"]
            t += (en[-1] + 0.1 - max(0, st[0] - 0.05)) / tempo + pausen.get(name, 0.25)
        return t
    tempo = 1.0
    while laenge(tempo) > ZIEL_S and tempo < MAX_TEMPO: tempo = round(tempo + 0.01, 2)
    teile, t, segs = [np.zeros(int(0.15 * SR), np.int16)], 0.15, []
    for name, text, mp3, al in roh:
        st = [x / tempo for x in al["character_start_times_seconds"]]
        en = [x / tempo for x in al["character_end_times_seconds"]]
        if mp3 is None:
            pcm = np.zeros(int((en[-1] + 0.2) * SR), np.int16)
        else:
            pcm = np.frombuffer(subprocess.run([FF, "-v", "error", "-i", mp3, "-af", f"atempo={tempo}", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                               capture_output=True, check=True).stdout, np.int16)
        a0, a1 = _grenzen(pcm, al["characters"], st, en)
        pcm = _blende(pcm[int(a0 * SR):int(a1 * SR)])
        woerter, cur, a, last = [], "", None, 0
        for ch, s, e in zip(al["characters"], st, en):
            if ch.isspace():
                if cur: woerter.append((cur, a - a0 + t, last - a0 + t)); cur = ""
                continue
            if not cur: a = s
            cur += ch; last = e
        if cur: woerter.append((cur, a - a0 + t, last - a0 + t))
        dauer = len(pcm) / SR
        segs.append(dict(name=name, text=text, start=round(t, 3), ende=round(t + dauer, 3), woerter=woerter))
        teile.append(pcm); t += dauer
        p = pausen.get(name, 0.25); teile.append(np.zeros(int(p * SR), np.int16)); t += p
    audio = np.concatenate(teile)
    audio = (audio.astype(np.float32) * (0.89 * 32767 / max(1, np.abs(audio).max()))).astype(np.int16) if np.abs(audio).max() else audio
    w = wave.open(ziel_wav, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(audio.tobytes()); w.close()
    return dict(dauer=round(t, 3), tempo=tempo, segmente=segs)
