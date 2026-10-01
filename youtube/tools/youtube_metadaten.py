#!/usr/bin/env python3
"""YouTube-Metadaten für eine fertige LexVerse-Folge: Untertitel (SRT), Kapitelmarken und Beschreibung.

    python3 youtube_metadaten.py --cues ../preproduction/katzenkoenig-test/cues.json \
        --kapitel ../preproduction/katzenkoenig-test/kapitel.json \
        --folge "Der Katzenkönig-Fall: Täter hinter dem Täter" --versatz 8.0 --out /pfad/ausgabe

Eingaben:
- cues.json aus synth_el.py: je Segment der gesprochene Text, die Rolle und die Wortzeiten (ElevenLabs-Zeichenzeiten).
- kapitel.json aus dem Renderer: Zeitpunkte, an denen sich der Prüfpfad unten links ändert.
- der Themenplan (themenplanung/themenplan-780.csv) für Titel, Beschreibung, Tags, Playlists; --folge ist Arbeitstitel,
  YouTube-Titel oder Folgennummer.
- --versatz: Länge des vorangestellten Intros in Sekunden (Standardintro: 8,0 s).

Ausgaben in --out:
- untertitel.srt: zum Hochladen bei YouTube (nicht eingebrannt). Die Zeiten stammen aus der Sprachaufnahme, der Text
  steht in Schriftform („§ 17 StGB“ statt „Paragraf siebzehn“), Figurenrede mit Sprechernamen.
- kapitel.txt: Kapitelmarken nach YouTube-Regeln (erste bei 0:00, mindestens drei, jede mindestens 10 s).
- beschreibung.txt und metadaten.json: Titel, Beschreibung mit Kapiteln, Tags, Playlists, Thumbnail-Text.
"""
import argparse, csv, json, os, re

HIER = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HIER, "..", "themenplanung", "themenplan-780.csv")

# --- Zahlwörter -> Ziffern (für die Schriftform der Untertitel) ------------------------------------------------------
EINER = {"null": 0, "ein": 1, "eins": 1, "eine": 1, "zwei": 2, "drei": 3, "vier": 4, "fünf": 5, "sechs": 6, "sieben": 7,
         "acht": 8, "neun": 9}
BESONDERS = {"zehn": 10, "elf": 11, "zwölf": 12, "dreizehn": 13, "vierzehn": 14, "fünfzehn": 15, "sechzehn": 16,
             "siebzehn": 17, "achtzehn": 18, "neunzehn": 19}
ZEHNER = {"zwanzig": 20, "dreißig": 30, "vierzig": 40, "fünfzig": 50, "sechzig": 60, "siebzig": 70, "achtzig": 80,
          "neunzig": 90}
ORDINAL = {"erste": 1, "ersten": 1, "zweite": 2, "zweiten": 2, "dritte": 3, "dritten": 3, "vierte": 4, "vierten": 4}


def _unter_100(w):
    if w in EINER: return EINER[w]
    if w in BESONDERS: return BESONDERS[w]
    if w in ZEHNER: return ZEHNER[w]
    if "und" in w:
        e, z = w.split("und", 1)
        if e in EINER and z in ZEHNER:
            return EINER[e] + ZEHNER[z]
    return None


def zahlwort(w):
    """'fünfundzwanzig' -> 25, 'zweihundertelf' -> 211, 'hundertachtunddreißig' -> 138; sonst None."""
    w = w.lower()
    if not w or not w.isalpha():
        return None
    gesamt = 0
    if "tausend" in w:
        t, w = w.split("tausend", 1)
        v = 1 if t in ("", "ein") else _unter_100(t)
        if v is None: return None
        gesamt += v * 1000
    if "hundert" in w:
        h, w = w.split("hundert", 1)
        v = 1 if h in ("", "ein") else _unter_100(h)
        if v is None or (v > 9 and (gesamt or v < 11)): return None    # 'neunzehnhundertelf' = 1911 (Jahresform)
        gesamt += v * 100
    if w:
        v = _unter_100(w)
        if v is None: return None
        gesamt += v
    return gesamt


BUCHSTABE = re.compile(r"^([a-zäöü])$")


def schriftform(text):
    """Gesprochene Normzitate und Abkürzungen in Schriftform bringen."""
    t = re.sub(r"\b((?:[A-ZÄÖÜ]\.){2,})", lambda m: m.group(1).replace(".", ""), text)       # B.G.H. -> BGH
    worte = t.split(" ")
    out, i = [], 0
    def zahl_ab(j):
        """Zahl ab Wort j (inkl. nachgestelltem Buchstaben 'a'), gibt (Text, neues j) oder (None, j)."""
        if j >= len(worte): return None, j
        roh = worte[j]; kern = roh.rstrip(",.;:!?)"); rest = roh[len(kern):]
        z = zahlwort(kern)
        if z is None:
            return None, j
        s = str(z); j += 1
        if not rest and j < len(worte) and BUCHSTABE.match(worte[j].rstrip(",.;:!?)")):       # 'zweihundertdreiundsechzig a'
            kern2 = worte[j].rstrip(",.;:!?)"); rest = worte[j][len(kern2):]; s += kern2; j += 1
        return s + rest, j
    while i < len(worte):
        w = worte[i]; wl = w.lower()
        if wl in ("paragraf", "paragraph", "paragrafen", "paragraphen"):
            z, j = zahl_ab(i + 1)
            if z:
                zeichen = "§§" if wl.startswith("paragrafen") or wl.startswith("paragraphen") else "§"
                teile = [z]
                while j < len(worte):
                    if j + 1 < len(worte) and worte[j] in ("und", "bis"):                     # 'Paragrafen zweihundertzwölf und …'
                        z2, j2 = zahl_ab(j + 1)
                        if not z2: break
                        teile += [worte[j], z2]; j = j2
                    elif teile[-1].endswith(","):                                              # 'Paragrafen dreihundertelf, zweihunderteinundvierzig …'
                        z2, j2 = zahl_ab(j)
                        if not z2: break
                        teile.append(z2); j = j2
                    else:
                        break
                out.append(f"{zeichen} " + " ".join(teile)); i = j; continue
        if wl in ("absatz", "satz", "nummer", "artikel"):
            z, j = zahl_ab(i + 1)
            if z:
                out.append({"absatz": "Abs.", "satz": "S.", "nummer": "Nr.", "artikel": "Art."}[wl] + " " + z); i = j; continue
        if wl in ORDINAL and i + 1 < len(worte) and worte[i + 1].lower().startswith("alternative"):
            rest = worte[i + 1][len("alternative"):]
            out.append(f"Alt. {ORDINAL[wl]}{rest}"); i += 2; continue
        kern = w.rstrip(",.;:!?)")
        if re.match(r"(?i)^(neunzehnhundert|zweitausend)", kern):                             # Jahreszahlen: 'zweitausendsiebzehn' -> 2017
            z = zahlwort(kern)
            if z is not None and 1900 <= z <= 2099:
                out.append(str(z) + w[len(kern):]); i += 1; continue
        out.append(w); i += 1
    return " ".join(out)


# --- Untertitel ------------------------------------------------------------------------------------------------------
KEIN_UMBRUCH_NACH = {"paragraf", "paragrafen", "paragraph", "paragraphen", "absatz", "satz", "nummer", "artikel",
                     "erste", "zweite", "dritte", "vierte", "und", "bis"}
MAX_ZEICHEN, MAX_DAUER, PAUSE = 84, 6.0, 0.6


def _zeit(t):
    t = max(0.0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"


def _zeilen(text, breite=42):
    if len(text) <= breite:
        return text
    worte = text.split(); best = None
    for k in range(1, len(worte)):
        a, b = " ".join(worte[:k]), " ".join(worte[k:])
        wert = max(len(a), len(b))
        if best is None or wert < best[0]:
            best = (wert, a + "\n" + b)
    return best[1]


def untertitel(cues, versatz, sprecher=True):
    bloecke = []
    for seg in cues["segmente"]:
        worte = seg["text"].split()
        assert len(worte) == len(seg["woerter"]), f"Segment {seg['i']}: Wörter und Zeiten passen nicht"
        akt = []
        def abschliessen():
            if not akt: return
            text = schriftform(" ".join(w for w, _ in akt))
            if sprecher and seg.get("rolle") and not any(b["seg"] == seg["i"] for b in bloecke):
                text = f"{seg['rolle']}: {text}"
            bloecke.append(dict(seg=seg["i"], a=akt[0][1][0], b=akt[-1][1][1], text=text))
            akt.clear()
        for k, (w, (a, b)) in enumerate(zip(worte, seg["woerter"])):
            if akt:
                laenge = len(" ".join(x for x, _ in akt)) + 1 + len(w)
                vorher = akt[-1][0].lower().rstrip(",.;:!?")
                pause = a - akt[-1][1][1]
                satzende = akt[-1][0][-1] in ".?!…:" and len(" ".join(x for x, _ in akt)) >= 20
                grenze = laenge > MAX_ZEICHEN or b - akt[0][1][0] > MAX_DAUER or pause > PAUSE or satzende
                if grenze and vorher not in KEIN_UMBRUCH_NACH:
                    abschliessen()
            akt.append((w, (a, b)))
        abschliessen()
    srt = []
    for n, bl in enumerate(bloecke):
        start = bl["a"] + versatz
        ende = bl["b"] + versatz + 0.3
        if n + 1 < len(bloecke):
            ende = min(ende, bloecke[n + 1]["a"] + versatz - 0.05)
        ende = max(ende, start + 1.0) if n + 1 == len(bloecke) else max(min(ende, bloecke[n + 1]["a"] + versatz - 0.05), start + 0.5)
        srt.append(f"{n + 1}\n{_zeit(start)} --> {_zeit(ende)}\n{_zeilen(bl['text'])}\n")
    return "\n".join(srt), len(bloecke)


# --- Kapitel ---------------------------------------------------------------------------------------------------------
def _mmss(t):
    t = int(round(t)); return f"{t // 60}:{t % 60:02d}" if t < 3600 else f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}"


def kapitel(liste, versatz, dauer, mindest=10.0):
    """liste: [{t, pfad}] in Sekunden ab Hauptfilmbeginn. Kapitel = oberste zwei Pfadebenen („A. Richard: Schuld“).
    YouTube verlangt je Kapitel mindestens 10 s: Zu kurze Kapitel werden mit dem Nachbarn desselben Prüfungsteils
    zusammengelegt („Rechtswidrigkeit und Schuld“), sonst dem vorigen Kapitel zugeschlagen."""
    roh = []
    for k in sorted(liste, key=lambda k: k["t"]):
        teile = [p.strip() for p in k["pfad"].replace("·", "›").split("›") if p.strip()]
        oben, unten = teile[0], (teile[1] if len(teile) > 1 else "")
        if roh and roh[-1]["oben"] == oben and roh[-1]["unten"] in ("", unten):
            roh[-1]["unten"] = unten                                   # 'A. Richard' -> 'A. Richard › Versuchter Mord'
            roh[-1]["teile"] = [unten] if unten else []
            continue
        roh.append(dict(t=k["t"] + versatz, oben=oben, unten=unten, teile=[unten] if unten else []))
    roh[0]["t"] = 0.0                                                  # erstes Kapitel bei 0:00 (umfasst das Intro)
    ende = dauer + versatz

    def aufzaehlung(teile):
        return teile[0] if len(teile) == 1 else ", ".join(teile[:-1]) + " und " + teile[-1]

    def name(k):
        return f"{k['oben']}: {aufzaehlung(k['teile'])}" if k["teile"] else k["oben"]

    while True:
        dauern = [(roh[i + 1]["t"] if i + 1 < len(roh) else ende) - roh[i]["t"] for i in range(len(roh))]
        kurz = [i for i in range(len(roh)) if dauern[i] < mindest]
        if not kurz or len(roh) <= 3:
            break
        i = kurz[0]
        nach = i + 1 if i + 1 < len(roh) and roh[i + 1]["oben"] == roh[i]["oben"] else None
        vor = i - 1 if i > 0 and roh[i - 1]["oben"] == roh[i]["oben"] else None
        if nach is not None:                                          # mit dem folgenden Teil desselben Abschnitts
            teile = roh[i]["teile"] + roh[nach]["teile"]
            roh[nach].update(t=roh[i]["t"], teile=teile if len(aufzaehlung(teile or [""])) <= 48 else roh[nach]["teile"]); del roh[i]
        elif vor is not None:
            teile = roh[vor]["teile"] + roh[i]["teile"]
            roh[vor]["teile"] = teile if len(aufzaehlung(teile or [""])) <= 48 else roh[vor]["teile"]; del roh[i]
        elif i == 0:
            roh[1]["t"] = 0.0; del roh[0]
        else:
            del roh[i]                                                # fremder Abschnitt: dem vorigen zuschlagen
    assert len(roh) >= 3, "YouTube verlangt mindestens drei Kapitel"
    return [(_mmss(k["t"]), name(k)[:70]) for k in roh]


# --- Themenplan ------------------------------------------------------------------------------------------------------
def planzeile(folge, pfad=PLAN):
    with open(pfad, encoding="utf-8-sig") as f:
        zeilen = list(csv.DictReader(f, delimiter=";"))
    for z in zeilen:
        if folge in (z["Nr."], z["Arbeitstitel"], z["YouTube-Titel"]):
            return z
    raise SystemExit(f"Folge {folge!r} steht nicht im Themenplan {pfad}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cues", required=True); ap.add_argument("--kapitel", required=True)
    ap.add_argument("--folge", required=True); ap.add_argument("--versatz", type=float, default=8.0)
    ap.add_argument("--out", required=True); ap.add_argument("--plan", default=PLAN)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    cues = json.load(open(a.cues)); kap_roh = json.load(open(a.kapitel))
    srt, n = untertitel(cues, a.versatz)
    open(os.path.join(a.out, "untertitel.srt"), "w", encoding="utf-8").write(srt)
    kap = kapitel(kap_roh, a.versatz, cues["dauer"])
    kap_text = "\n".join(f"{t} {name}" for t, name in kap)
    open(os.path.join(a.out, "kapitel.txt"), "w", encoding="utf-8").write(kap_text + "\n")
    z = planzeile(a.folge, a.plan)
    tags = [t.strip() for t in re.split(r"\s\|\s", z["Tags"]) if t.strip()]
    tags = [z["Suchbegriff"]] + [t for t in tags if t.lower() != z["Suchbegriff"].lower()]
    while len(",".join(tags)) > 480:                                  # YouTube-Grenze: 500 Zeichen
        tags.pop()
    hashtags = " ".join("#" + re.sub(r"[^\wäöüÄÖÜß]", "", w) for w in (z["Suchbegriff"], z["Gebiet"], "Jura")[:3])
    teile = [z["Beschreibung (Anfang)"], "", "Kapitel:", kap_text, ""]
    if z["Normen"]: teile.append(f"Normen: {z['Normen']}")
    if z["Leitentscheidung"]: teile.append(f"Leitentscheidung: {z['Leitentscheidung']}")
    teile += ["", "Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: Tag der Veröffentlichung.", "", hashtags]
    beschreibung = "\n".join(teile)
    assert len(beschreibung) <= 5000
    open(os.path.join(a.out, "beschreibung.txt"), "w", encoding="utf-8").write(beschreibung + "\n")
    meta = dict(titel=z["YouTube-Titel"], beschreibung=beschreibung, tags=tags,
                playlists=[p.strip() for p in z["Playlists"].split("|") if p.strip()],
                thumbnail_text=z["Thumbnail-Text"], sprache="de", kategorie="Bildung", nr=z["Nr."], kapitel=kap)
    json.dump(meta, open(os.path.join(a.out, "metadaten.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{n} Untertitel, {len(kap)} Kapitel, {len(tags)} Tags -> {a.out}")


if __name__ == "__main__":
    main()
