#!/usr/bin/env python3
"""Render the Willenserklärung pilot from locked voice takes and character art."""

import json
import math
import re
import subprocess
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"
WORK.mkdir(exist_ok=True)
ASSETS = ROOT / "assets"
SCRIPT = json.loads((ROOT / "script.json").read_text())
NARRATOR = ROOT / "audio"
CHARACTER = ROOT / "character-audio"
W, H, RATE = 1920, 1080, 48000
NAVY = (10, 24, 70)
BLUE = (45, 91, 227)
MINT = (164, 249, 220)
GOLD = (255, 207, 89)
WHITE = (250, 253, 255)
PINK = (255, 139, 145)
FONTS = ROOT.parent.parent / "fonts"


def font(size, bold=False):
    name = "SpaceGrotesk.ttf" if bold else "Inter.ttf"
    return ImageFont.truetype(str(FONTS / name), size)


def secs(p):
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(p)
    ]).decode().strip())


def pcm(p):
    return subprocess.check_output([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(p),
        "-ar", str(RATE), "-ac", "1", "-f", "s16le", "-acodec", "pcm_s16le", "-"
    ])


def make_audio():
    timeline, chunks = [], []
    samples = 0

    def silence(duration):
        nonlocal samples
        n = round(duration * RATE)
        chunks.append(b"\0\0" * n)
        samples += n

    def add_audio(segment, role, text, path):
        nonlocal samples
        raw = pcm(path)
        assert len(raw) % 2 == 0
        start = samples / RATE
        duration = len(raw) / (2 * RATE)
        chunks.append(raw)
        samples += len(raw) // 2
        timeline.append({"segment": segment, "role": role, "text": text,
                         "path": str(path), "start": start, "duration": duration})

    silence(.23)
    for i, segment in enumerate(SCRIPT["segments"]):
        for j, line in enumerate(segment["lines"]):
            role = line["role"]
            if role == "narrator":
                path = NARRATOR / f"{i + 1:02d}-{segment['id']}-{j + 1:02d}.mp3"
            elif segment["id"] == "hook" and role == "mara":
                path = CHARACTER / "mara_offer.mp3"
            elif segment["id"] == "hook" and role == "rex":
                path = CHARACTER / "rex_accept.mp3"
            elif segment["id"] == "vorbehalt" and role == "mara":
                path = CHARACTER / "mara_protest.mp3"
            else:
                raise ValueError(f"Missing actor take: {segment['id']} {role}")
            add_audio(segment["id"], role, line["text"], path)
            if role != "narrator":
                silence(.32 if role == "mara" else .48)
        if i != len(SCRIPT["segments"]) - 1:
            silence(.53 if segment["id"] in ("hook", "vorbehalt") else .43)
    speech_end = samples / RATE
    silence(7.8)
    with wave.open(str(WORK / "master.wav"), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(RATE)
        wav.writeframes(b"".join(chunks))
    (WORK / "timeline.json").write_text(json.dumps({"events": timeline,
        "speechEnd": speech_end, "duration": samples / RATE}, ensure_ascii=False, indent=2))
    return timeline, speech_end, samples / RATE


SCENE = {
    "offer": "scene-offer.jpg", "accept": "scene-accept.jpg",
    "reversal": "scene-reversal.jpg", "mara": "mara-close.jpg",
    "rex": "rex-close.jpg",
}


def measure(draw, s, f):
    return draw.textbbox((0, 0), s, font=f)[2]


def wrap(draw, text, f, width):
    result, line = [], ""
    for word in text.split():
        candidate = (line + " " + word).strip()
        if line and measure(draw, candidate, f) > width:
            result.append(line)
            line = word
        else:
            line = candidate
    if line:
        result.append(line)
    return result


def panel(img, box, fill=(8, 24, 67, 220), radius=32, outline=None):
    layer = Image.new("RGBA", img.size)
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=3 if outline else 1)
    return Image.alpha_composite(img, layer)


def put(draw, xy, text, f, fill=WHITE, anchor=None):
    draw.text(xy, text, font=f, fill=fill, anchor=anchor, stroke_width=0)


# Each step changes the drawing or the highlighted legal point while a scene
# remains readable. Every state is a separately held cel: no pan or digital zoom.
STATES = {
    "hook": [
        ("offer", "Direkt an Rex", "Fahrrad · 80 €", 0.00),
        ("accept", "Gekauft!", "Rex antwortet sofort", 0.13),
        ("reversal", "Und Maras geheimes Nein?", "Was gilt rechtlich?", 0.27),
        ("mara", "Ein Satz kann binden.", "Vier Fragen lösen den Fall.", 0.64),
    ],
    "definition": [
        ("mara", "Willenserklärung", "Wille nach außen", 0.00),
        ("rex", "„Schönes Fahrrad“", "Beschreibung, noch kein Verkauf", .28),
        ("offer", "„Ich verkaufe dir ...“", "auf eine Rechtsfolge gerichtet", .55),
        ("mara", "Nicht die Unterschrift entscheidet", "sondern der rechtliche Erklärungswert", .82),
    ],
    "aussen": [
        ("offer", "Aus Rex' Sicht", "Wem? · Was? · Wofür?", .00),
        ("offer", "Rex · dieses Rad · 80 €", "Die wesentlichen Punkte sind klar.", .24),
        ("rex", "Objektiver Empfängerhorizont", "Wortlaut und Umstände", .48),
        ("mara", "§§ 133, 157 BGB", "Auslegung im Zusammenhang", .72),
        ("offer", "Direkte Ansprache", "Mehr als eine bloße Auslage", .88),
    ],
    "innen": [
        ("mara", "1 · Handlungswille", "Bewusst gehandelt?", .00),
        ("mara", "2 · Erklärungsbewusstsein", "Rechtliche Bedeutung erkannt?", .24),
        ("mara", "3 · Geschäftswille", "Gerade diesen Verkauf gewollt?", .47),
        ("reversal", "Mara wollte behalten", "Der Geschäftswille fehlt.", .68),
        ("mara", "Nicht automatisch unwirksam", "Jetzt kommt § 116 BGB ins Spiel.", .84),
    ],
    "vertrag": [
        ("offer", "Angebot", "Rex · Fahrrad · 80 €", .00),
        ("accept", "+ Annahme", "„Gekauft!“ ohne Änderung", .23),
        ("accept", "§§ 145, 147 BGB", "Anwesend: sofortige Antwort", .46),
        ("rex", "„Nur für 60 €“?", "§ 150 Abs. 2: neues Angebot", .66),
        ("accept", "Hier: 80 €", "Zwei passende Erklärungen", .84),
    ],
    "zugang": [
        ("offer", "Abgabe + Zugang", "Erklärung muss wirksam werden.", .00),
        ("diagram", "Unter Abwesenden", "§ 130 Abs. 1 BGB", .29),
        ("diagram", "Im Machtbereich", "gewöhnliche Kenntnisnahme möglich", .53),
        ("rex", "Lesen ist nicht nötig", "Rex' Briefkasten als Beispiel", .74),
        ("offer", "Hier: direktes Gespräch", "Beide hören die Erklärung.", .88),
    ],
    "vorbehalt": [
        ("reversal", "Mara will zurück", "Der Gedanke war geheim.", .00),
        ("mara", "§ 116 Satz 1 BGB", "Geheimer Vorbehalt macht nicht nichtig.", .19),
        ("rex", "Rex wusste nichts", "Er durfte dem Angebot vertrauen.", .49),
        ("mara", "§ 116 Satz 2 BGB", "Bei Kenntnis des Vorbehalts: nichtig", .73),
        ("reversal", "Der Fall ist entschieden", "Maras verborgenes Nein hilft nicht.", .89),
    ],
    "folge": [
        ("accept", "Kaufvertrag", "Mara + Rex · Fahrrad · 80 €", .00),
        ("mara", "Mara schuldet", "Übergabe + Eigentumsverschaffung", .27),
        ("rex", "Rex schuldet", "80 € Kaufpreis", .49),
        ("reversal", "§ 433 BGB", "Vertrag schafft zunächst Pflichten.", .70),
        ("offer", "Noch kein Eigentumswechsel", "Kaufvertrag ≠ Übereignung", .86),
    ],
    "schluss": [
        ("offer", "Zurück zum ersten Satz", "Maras konkretes Angebot", .00),
        ("accept", "Angebot + Annahme", "Rex sagt sofort Ja.", .31),
        ("reversal", "§ 116 BGB", "Ein geheimes Nein rettet Mara nicht.", .57),
        ("mara", "Die vier Fragen", "Äußeres · Inneres · Wirksamkeit · Folge", .70),
        ("offer", "Aus einem Satz wird ein Fall", "Sauber prüfen. Klar begründen.", .83),
    ],
}

CUES = {
    "definition": [None, "Sagt sie nur", "Sagt sie zu Rex", "Der Unterschied"],
    "aussen": [None, "Mara spricht ihn", "Für Rex", "Bei der Auslegung", "Ein bloßes Fahrrad"],
    "innen": [None, "Erklärungsbewusstsein heißt", "Geschäftswille meint", "Hier hat Mara", "Entscheidend ist"],
    "vertrag": [None, "Genau das tut er", "Unter Anwesenden", "Würde er stattdessen", "Unser Rex bleibt"],
    "zugang": [None, "Bei einem Brief", "Dafür genügt", "Er muss den Brief", "In unserem Gespräch"],
    "vorbehalt": [None, "Jetzt die Auflösung", "Rex wusste", "Hätte er", "Für unseren Fall"],
    "folge": [None, "Nach Paragraf", "Rex schuldet", "Achte auf", "Das Eigentum"],
    "schluss": [None, "Er nahm", "Ihr geheimer", "Wenn du eine", "So wird"],
}


def draw_diagram(img, state):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((200, 400, 660, 680), radius=28, fill=(242, 250, 252), outline=NAVY, width=8)
    d.rectangle((340, 540, 520, 630), fill=(248, 230, 174), outline=NAVY, width=5)
    d.line((342, 542, 430, 592, 518, 542), fill=NAVY, width=4, joint="curve")
    d.rounded_rectangle((1290, 320, 1610, 750), radius=25, fill=(242, 250, 252), outline=NAVY, width=10)
    d.rounded_rectangle((1300, 490, 1600, 535), radius=8, fill=(8, 24, 67))
    d.rectangle((1300, 710, 1600, 750), fill=(248, 218, 143), outline=NAVY, width=5)
    # Arrow is a precise explanatory diagram, not an animation of a prop.
    d.line((710, 520, 1230, 520), fill=MINT, width=21)
    d.polygon([(1235, 520), (1180, 484), (1180, 556)], fill=MINT)
    put(d, (255, 710), "ABGABE", font(37, True), NAVY)
    put(d, (1304, 790), "ZUGANG", font(37, True), WHITE)


def draw_slide(segment, state_idx, spec):
    kind, title, sub, _ = spec
    if kind == "diagram":
        im = Image.new("RGBA", (W, H), BLUE + (255,))
        draw_diagram(im, state_idx)
        box = (525, 115, 1395, 315)
    else:
        base = Image.open(ASSETS / SCENE[kind]).convert("RGBA")
        im = base.resize((W, H), Image.Resampling.LANCZOS)
        if kind == "mara":
            box = (1050, 194, 1850, 565)
        elif kind == "rex":
            box = (70, 194, 865, 565)
        else:
            box = (615, 102, 1340, 338)

    # Recurring brand strip and progress line for wayfinding.
    im = panel(im, (48, 37, 383, 91), fill=(8, 24, 67, 228), radius=18)
    d = ImageDraw.Draw(im)
    put(d, (71, 50), "HERR JURIST  /  ZIVILRECHT", font(27, True))
    number = next(i for i, s in enumerate(SCRIPT["segments"]) if s["id"] == segment) + 1
    d.rounded_rectangle((1540, 43, 1853, 92), radius=16, fill=(8, 24, 67, 200))
    put(d, (1565, 54), f"KAPITEL {number:02d} / 09", font(25, True))
    d.rounded_rectangle((64, 1030, 1856, 1038), radius=4, fill=(7, 23, 64, 140))
    d.rounded_rectangle((64, 1030, 64 + int(1792 * (number - .25) / 9), 1038), radius=4, fill=MINT)

    im = panel(im, box, fill=(8, 24, 67, 222), radius=31)
    d = ImageDraw.Draw(im)
    bx0, by0, bx1, by1 = box
    tint = PINK if segment == "vorbehalt" and state_idx in (0, 3) else MINT
    d.rounded_rectangle((bx0 + 30, by0 + 28, bx0 + 112, by0 + 38), radius=5, fill=tint)
    ftitle = font(61 if len(title) <= 25 else 51, True)
    lines = wrap(d, title, ftitle, bx1 - bx0 - 70)
    y = by0 + 65
    for line in lines[:3]:
        put(d, (bx0 + 32, y), line, ftitle, WHITE)
        y += (68 if ftitle.size >= 60 else 60)
    fsub = font(31 if len(sub) > 41 else 36)
    for line in wrap(d, sub, fsub, bx1 - bx0 - 70)[:3]:
        put(d, (bx0 + 34, y + 9), line, fsub, tint)
        y += 48

    # Keep captions in a stable safe area; no illustrated text is masked.
    return im.convert("RGB")


def make_slides(timeline, speech_end, duration):
    groups = {}
    for event in timeline:
        groups.setdefault(event["segment"], []).append(event)
    events = []
    for segment in SCRIPT["segments"]:
        sid = segment["id"]
        section = groups[sid]
        first = section[0]["start"]
        end = section[-1]["start"] + section[-1]["duration"]
        if sid == "hook":
            # Precise first beats: offer, Rex's audible acceptance, Mara's turn.
            boundaries = [first, section[1]["start"], section[2]["start"],
                          section[2]["start"] + section[2]["duration"] * .64, end]
        else:
            spoken = next(e for e in section if e["role"] == "narrator")
            alignment = json.loads(Path(spoken["path"]).with_suffix(".json").read_text())["alignment"]
            transcript = "".join(alignment["characters"])
            boundaries = [first]
            for cue in CUES[sid][1:]:
                index = transcript.find(cue)
                if index < 0:
                    raise ValueError(f"Missing visual cue {sid}: {cue}")
                boundaries.append(spoken["start"] + alignment["character_start_times_seconds"][index])
            boundaries.append(end)
        for i, spec in enumerate(STATES[sid]):
            img = draw_slide(sid, i, spec)
            path = WORK / f"slide-{len(events):03d}.jpg"
            img.save(path, quality=92, subsampling=0)
            events.append({"file": path, "start": boundaries[i], "end": boundaries[i + 1],
                           "segment": sid, "state": i})
    endcard = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(endcard)
    put(d, (135, 105), "HERR JURIST", font(104, True), WHITE)
    put(d, (142, 235), "Der nächste Fall wartet schon.", font(51), MINT)
    d.rounded_rectangle((160, 445, 825, 820), radius=35, outline=(99, 147, 230), width=5)
    d.rounded_rectangle((1095, 445, 1760, 820), radius=35, outline=(99, 147, 230), width=5)
    put(d, (167, 880), "Weiterlernen", font(42, True), WHITE)
    put(d, (1280, 880), "Abonnieren", font(42, True), WHITE)
    endpath = WORK / f"slide-{len(events):03d}.jpg"
    endcard.save(endpath, quality=92, subsampling=0)
    events.append({"file": endpath, "start": speech_end, "end": duration,
                   "segment": "endcard", "state": 0})
    # Ensure gaps between chapters hold the preceding visual, and no empty frame.
    for i in range(len(events) - 1):
        if events[i]["end"] < events[i + 1]["start"]:
            events[i]["end"] = events[i + 1]["start"]
    events[0]["start"] = 0
    lines = []
    for item in events:
        lines.extend((f"file '{item['file']}'", f"duration {item['end'] - item['start']:.6f}"))
    lines.append(f"file '{events[-1]['file']}'")
    (WORK / "slides.txt").write_text("\n".join(lines) + "\n")
    (WORK / "slides.json").write_text(json.dumps([{**e, "file": str(e["file"])} for e in events], ensure_ascii=False, indent=2))
    return events


def words_from_alignment(alignment):
    chars = alignment["characters"]
    begins = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]
    words, start, current = [], None, ""
    for c, a, b in zip(chars, begins, ends):
        if c.isspace():
            if current:
                words.append((current, start, last))
                current, start = "", None
        else:
            if start is None:
                start = a
            current += c
            last = b
    if current:
        words.append((current, start, last))
    return words


def legal_notation(words):
    """Keep a spoken legal citation intact and render its written form."""
    patterns = [
        (("paragrafen", "einhundertdreiunddreißig", "und", "einhundertsiebenundfünfzig"), "§§ 133, 157"),
        (("paragraf", "einhundertfünfzig", "absatz", "zwei"), "§ 150 Abs. 2"),
        (("paragraf", "einhundertdreißig", "absatz", "eins"), "§ 130 Abs. 1"),
        (("paragraf", "einhundertsechzehn"), "§ 116"),
        (("paragraf", "vierhundertdreiunddreißig"), "§ 433"),
    ]
    out, i = [], 0
    while i < len(words):
        found = False
        for pattern, replacement in patterns:
            candidate = tuple(re.sub(r"[^a-zäöüß]", "", w[0].lower()) for w in words[i:i + len(pattern)])
            if candidate == pattern:
                out.append((replacement, words[i][1], words[i + len(pattern) - 1][2]))
                i += len(pattern)
                found = True
                break
        if not found:
            out.append(words[i])
            i += 1
    return out


def groups_of_words(words):
    result, current = [], []
    for word in words:
        current.append(word)
        if len(current) >= 4 or (len(current) >= 2 and re.search(r"[,;.!?…:]$", word[0])):
            result.append(current)
            current = []
    if current:
        if result and len(current) == 1 and len(result[-1]) < 5:
            result[-1].extend(current)
        else:
            result.append(current)
    return result


def srt_time(t):
    ms = round(t * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def ass_time(t):
    return srt_time(t).replace(",", ".")[:-1]


def captions(timeline):
    cues = []
    for event in timeline:
        if event["role"] == "narrator":
            alignment = json.loads(Path(event["path"]).with_suffix(".json").read_text())["alignment"]
            for group in groups_of_words(legal_notation(words_from_alignment(alignment))):
                text = " ".join(w[0] for w in group)
                cues.append((event["start"] + group[0][1],
                             event["start"] + group[-1][2], text))
        else:
            chunks = [event["text"]]
            if len(event["text"].split()) > 6:
                w = event["text"].split()
                chunks = [" ".join(w[:5]), " ".join(w[5:])]
            for i, text in enumerate(chunks):
                cues.append((event["start"] + event["duration"] * i / len(chunks),
                             event["start"] + event["duration"] * (i + 1) / len(chunks), text))
    cues.sort()
    srt = []
    for i, (a, b, s) in enumerate(cues, 1):
        srt.append(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{s}\n")
    (ROOT / "willenserklaerung.de.srt").write_text("\n".join(srt))
    ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,Nimbus Sans,58,&H00FFFFFF,&H00FFFFFF,&H00201908,&H80000000,-1,0,0,0,100,100,0,0,1,4,1,2,120,120,78,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    for a, b, s in cues:
        safe = s.replace("{", "(").replace("}", ")").replace("\n", " ")
        ass += f"Dialogue: 0,{ass_time(a)},{ass_time(max(a + .12, b))},Caption,,0,0,0,,{safe}\n"
    (WORK / "captions.ass").write_text(ass)
    return len(cues)


def main():
    timeline, speech_end, duration = make_audio()
    slides = make_slides(timeline, speech_end, duration)
    cues = captions(timeline)
    print(json.dumps({"duration": duration, "speechEnd": speech_end,
                      "slides": len(slides), "captions": cues}, ensure_ascii=False))


if __name__ == "__main__":
    main()
