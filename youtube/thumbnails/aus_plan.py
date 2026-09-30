"""Thumbnail-Spezifikationen für alle Folgen des Themenplans.

Je Folge steht in youtube/themenplanung/thumbs_*.json eine kurze, abstrakte Angabe (Text A/B, Vorlage, Rollen mit Mimik,
Gegenstand, Motiv). Dieses Skript macht daraus vollständige Spezifikationen für thumbnail.py: Frisur, Hautton, Kleidung,
Pose und Bart werden aus Folgennummer und Rolle abgeleitet (reproduzierbar, abwechslungsreich, normale Hauttöne).

    python3 aus_plan.py --json alle.json                       # nur Spezifikationen schreiben
    python3 aus_plan.py --render AUSGABE [--nr 1-40] [--gebiet Strafrecht] [--ohne-varianten]

Abstraktes Format (eine Folge):
    {"nr": 1, "typ": "fall", "text": ["MORD MIT", "DEM *AUTO?"], "b": ["*RASER-", "FALL"],
     "figuren": [{"rolle": "Zeugin", "person": "w", "mimik": "aengstlich"},
                 {"rolle": "Raser", "person": "m", "mimik": "frech", "haelt": "car-key"}],
     "motiv": ["racing-car", "collision"]}
    Lernvideos zusätzlich "karte": "SCHEMA" usw.; Lexi als Figur: {"lexi": "erklaert"}."""
import argparse, csv, glob, hashlib, json, os, sys

HIER = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HIER, "..", "themenplanung")
sys.path.insert(0, HIER)
import thumbnail as T          # noqa: E402

MIMIK = {"wuetend": "Rage", "sehr_wuetend": "Very Angry", "fies": "Angry with Fang", "aengstlich": "Concerned Fear",
         "erschrocken": "Fear", "besorgt": "Concerned", "frech": "Cheeky", "ernst": "Serious", "entschlossen": "Driven",
         "froh": "Smile Big", "lacht": "Smile LOL", "erklaert": "Explaining", "skeptisch": "Suspicious",
         "staunend": "Awe", "hektisch": "Hectic", "muede": "Tired", "ruhig": "Calm", "verachtend": "Contempt",
         "verliebt": "Loving Grin 1", "stolz": "Smile", "traurig": "Solemn"}
LEXI = {"erklaert": "erklaert_auf", "warnt": "warnt_auf", "freut": "freut", "skeptisch": "skeptisch",
        "nachdenklich": "nachdenklich", "ruhig": "ruhig"}
KOPF = {"w": ["Long", "Long Curly", "Bun", "Medium Straight", "Long Bangs", "Bangs", "Bangs 2", "Buns", "Long Afro",
              "Medium Bangs", "Medium Bangs 2", "Medium 1", "Medium 2", "Cornrows 2", "Hijab"],
        "m": ["Short 1", "Short 2", "Short 3", "Short 4", "Short 5", "Pomp", "Shaved 1", "Shaved 2", "Twists",
              "Flat Top", "Afro", "Dreads 1", "Short 4_2", "No Hair 1", "Turban"],
        "w_alt": ["Gray Bun", "Gray Medium"], "m_alt": ["Gray Short", "No Hair 2", "No Hair 3"]}
BART = ["Full", "Goatee 1", "Moustache 1", "Chin", None, None, None]
HAUT = ["#F1C6A5", "#E9BE98", "#D9A07A", "#C58E64", "#B07552", "#8D5A3B"]
OBERTEIL = ["#9BD88A", "#7FB2F0", "#F28C6B", "#F9D56E", "#B784D1", "#F6A5C0", "#9FD8E5", "#FFCF77"]
DUNKEL = "#3D3D58"


def _zahl(*teile):
    return int(hashlib.md5("|".join(map(str, teile)).encode()).hexdigest(), 16)


def figur(nr, i, r, belegt):
    """Abstrakte Rolle -> Open-Peeps-Figur. belegt verhindert gleiche Frisur/Haut/Farbe in einem Thumbnail."""
    if r.get("lexi"):
        return {"lexi": LEXI[r["lexi"]], "spiegeln": not r.get("zur_person")}
    if r.get("mimik") not in MIMIK:
        raise T.Fehler(f"Folge {nr}: Mimik '{r.get('mimik')}' unbekannt (erlaubt: {', '.join(MIMIK)})")
    person = r.get("person", "m" if _zahl(nr, i, "p") % 2 else "w")
    liste = KOPF[person + ("_alt" if r.get("alt") else "")]

    def waehle(werte, art):
        frei = [w for w in werte if w not in belegt] or werte
        w = frei[_zahl(nr, i, art, r.get("rolle")) % len(frei)]; belegt.add(w); return w
    kopf, haut, farbe = waehle(liste, "k"), waehle(HAUT, "h"), waehle(OBERTEIL, "o")
    bart = BART[_zahl(nr, i, "b") % len(BART)] if person == "m" and not r.get("alt") else None
    anzug = r.get("kleidung") == "anzug"
    mimik = r["mimik"]
    if r.get("haelt"):
        pose = "standing/robot_dance-1"                       # ausgestreckter Arm für den Gegenstand
    elif r.get("kleidung") == "arzt":
        pose = "standing/doctor-nurse-01"
    elif anzug:
        pose = ["standing/blazer-1", "standing/blazer-3"][_zahl(nr, i, "a") % 2]
    elif mimik in ("aengstlich", "erschrocken", "besorgt", "staunend", "traurig", "muede"):
        pose = "standing/easing-1"
    elif mimik in ("wuetend", "sehr_wuetend", "ernst", "skeptisch", "entschlossen", "verachtend", "stolz"):
        pose = ["standing/crossed_arms-1", "standing/shirt-1"][_zahl(nr, i, "a") % 2]
    else:
        pose = ["standing/shirt-1", "standing/blazer-3", "standing/easing-1"][_zahl(nr, i, "a") % 3]
    farben = {"Skin": haut, "Top": DUNKEL if anzug else farbe}
    if pose.startswith("standing/blazer"):
        farben["Jacket"] = DUNKEL if anzug else farbe
        farben["Pants"] = DUNKEL
        if not anzug: farben["Top"] = "#FFFFFF"
    f = {"pose": pose, "kopf": kopf, "gesicht": MIMIK[mimik], "farben": farben, "spiegeln": not r.get("zur_person")}
    if bart: f["bart"] = bart
    if r.get("brille"): f["brille"] = "Glasses"
    if r.get("haelt"):
        h = r["haelt"] if isinstance(r["haelt"], dict) else {"emoji": r["haelt"]}
        f["haelt"] = {"emoji": h["emoji"], "g": h.get("g", 170), "drehung": h.get("drehung", 0),
                      "hand": "rechts" if r.get("zur_person") else "links"}
        if h.get("spiegeln"): f["haelt"]["spiegeln"] = True
    return f


def motiv(m, typ):
    if not m: return None
    if isinstance(m, dict): return m
    namen = [m] if isinstance(m, str) else m
    if len(namen) == 1: return {"emoji": namen[0]}
    return {"teile": [[namen[0], 1.0, 0, 0, 0], [namen[1], 0.5, 0.72, -0.1, 0]]}


def plan():
    zeilen = csv.DictReader(open(os.path.join(PLAN, "themenplan-780.csv"), encoding="utf-8-sig"), delimiter=";")
    return {int(z["Nr."]): z for z in zeilen}


def angaben(muster=None):
    a = {}
    for p in sorted(glob.glob(muster or os.path.join(PLAN, "thumbs_*.json"))):
        for e in json.load(open(p)):
            if e["nr"] in a: raise T.Fehler(f"Folge {e['nr']} doppelt ({p})")
            a[e["nr"]] = e
    return a


def spezifikation(e, z):
    nr = e["nr"]; belegt = set()
    s = {"k": f"{nr:03d}", "typ": e["typ"], "gebiet": z["Gebiet"], "titel": z["YouTube-Titel"], "text": e["text"],
         "figuren": [figur(nr, i, r, belegt) for i, r in enumerate(e["figuren"])]}
    if e["typ"] == "lern": s["karte"] = e.get("karte")
    m = motiv(e.get("motiv"), e["typ"])
    if m: s["motiv"] = m
    if e.get("layout"): s["layout"] = e["layout"]
    if e.get("b"): s["varianten"] = {"B": {"text": e["b"]}}
    return s


def bereich(text):
    nrs = set()
    for t in text.split(","):
        a, _, b = t.partition("-"); nrs.update(range(int(a), int(b or a) + 1))
    return nrs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", help="vollständige Spezifikationen hierhin schreiben")
    ap.add_argument("--render", help="Thumbnails in diesen Ordner rendern (nicht ins Repository)")
    ap.add_argument("--nr", help="nur diese Folgen, z. B. 1-40,55")
    ap.add_argument("--gebiet")
    ap.add_argument("--angaben", help="andere Angabedateien (Glob), Standard: themenplanung/thumbs_*.json")
    ap.add_argument("--ohne-varianten", action="store_true")
    a = ap.parse_args()
    p, ang = plan(), angaben(a.angaben)
    fehlend = sorted(set(p) - set(ang))
    nrs = sorted(ang)
    if a.nr: nrs = [n for n in nrs if n in bereich(a.nr)]
    if a.gebiet: nrs = [n for n in nrs if p[n]["Gebiet"] == a.gebiet]
    specs, kaputt = [], []
    for n in nrs:
        try:
            specs.append(spezifikation(ang[n], p[n]))
        except (T.Fehler, KeyError) as ex:
            kaputt.append(f"{n}: {ex}")
    if a.json:
        json.dump(specs, open(a.json, "w"), ensure_ascii=False, indent=1)
    if a.render:
        os.makedirs(a.render, exist_ok=True)
        bilder = []
        for grund in specs:
            for s in ([grund] if a.ohne_varianten else T.varianten(grund)):
                fehler, hinweise = T.pruefen(s)
                for h in hinweise: print("Hinweis:", h)
                try:
                    if fehler: raise T.Fehler("; ".join(fehler))
                    im = T.szene(s)
                except T.Fehler as ex:
                    kaputt.append(str(ex)); continue
                im.save(os.path.join(a.render, f"{s['k']}.jpg"), quality=92); bilder.append((s, im))
        for i in range(0, len(bilder), 12):                      # Kontaktbögen zu je 12 Bildern mit Nummer
            teil = bilder[i:i + 12]
            bog = T.Image.new("RGB", (4 * 618 + 18, 3 * 386 + 18), "#FFFFFF"); d = T.ImageDraw.Draw(bog)
            for j, (s, im) in enumerate(teil):
                x, y = 18 + (j % 4) * 618, 18 + (j // 4) * 386
                bog.paste(im.resize((600, 338), T.Image.LANCZOS), (x, y))
                d.text((x, y + 340), f"{s['k']}  {s['titel'][:60]}", font=T.font(22, 700), fill=T.INK)
            bog.save(os.path.join(a.render, f"bogen_{i // 12 + 1:03d}.png"))
        print(f"{len(bilder)} Thumbnails -> {a.render}")
    for k in kaputt: print("FEHLER:", k)
    if fehlend and not (a.nr or a.gebiet): print(f"ohne Angabe: {len(fehlend)} Folgen")
    print(f"{len(specs)} Spezifikationen, {len(kaputt)} Fehler")
    sys.exit(1 if kaputt else 0)


if __name__ == "__main__":
    main()
