"""LexVerse-Thumbnails nach youtube/THUMBNAILS.md: Farbe je Rechtsgebiet, plakativer Text, Open-Peeps-Figuren rechts,
farbige Emoji-Motive (Fluent Emoji Flat, MIT). Zwei Vorlagen: "fall" (Hook + Szene) und "lern" (Thema + Karte + Figuren).
Jedes Bild wird beim Rendern geprüft: Text berührt keine Figur, Figuren sind seitlich nicht angeschnitten, freie Motive
überlappen nichts, gehaltene Gegenstände liegen vollständig im Bild.

    python3 thumbnail.py beispiele.json --out AUSGABE [--nur k1,k2] [--vorschau]

Voraussetzung: Emoji-Satz einmalig mit ./assets_holen.sh laden (oder LEXVERSE_EMOJI=…/icons.json setzen)."""
import argparse, hashlib, io, json, os, sys
import numpy as np
import cairosvg
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps
from scipy import ndimage

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HIER, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "youtube", "openpeeps-erweiterung", "figma-bibliothek"))
from lexpeeps import figur as peep          # noqa: E402
import lexi as LX                          # noqa: E402

SCHRIFT = os.environ.get("LEXVERSE_FONT", os.path.join(REPO, "fonts", "Nunito.ttf"))
EMOJI = os.environ.get("LEXVERSE_EMOJI", os.path.join(HIER, "assets", "fluent-emoji-flat", "icons.json"))
CACHE = os.environ.get("LEXVERSE_THUMB_CACHE", os.path.join(HIER, ".cache"))

W, H = 1280, 720
INK, WEISS, GELB = "#141414", "#FFFFFF", "#FFD23F"
GEBIET = {"Strafrecht": "#D7263D", "Zivilrecht": "#1B6FD1", "Öffentliches Recht": "#139A62", "2. Examen": "#6B3FD0",
          "Methodik": "#E08A00"}
KARTE = ("SCHEMA", "STREIT", "ABGRENZUNG", "FEHLER", "SCHRITTE", "DEFINITION", "ÜBERBLICK", "MUSTER", "TAKTIK", "SONDERFALL")
RAND = 18                      # Mindestabstand zum Bildrand
TEXT_X, TEXT_Y = 46, 42
FIG_LINKS = 650                # Figurenzone beginnt hier
KARTE_MIN = 380                # Lernvorlage: Mindesthöhe unter dem Text für die Karte
FIGUR_MIN = 660                # Mindesthöhe der ganzen Figur (sichtbar sind ~60 %)


class Fehler(Exception):
    pass


def font(size, gewicht=900):
    f = ImageFont.truetype(SCHRIFT, size); f.set_variation_by_axes([gewicht]); return f


_emo = None


def emoji_satz():
    global _emo
    if _emo is None:
        if not os.path.exists(EMOJI):
            raise Fehler(f"Emoji-Satz fehlt: {EMOJI} – zuerst youtube/thumbnails/assets_holen.sh ausführen")
        _emo = json.load(open(EMOJI))
    return _emo


def emoji(name, groesse, spiegeln=False, drehen=0):
    s = emoji_satz()
    if name not in s["icons"]:
        raise Fehler(f"Emoji '{name}' gibt es im Satz nicht")
    ic = s["icons"][name]; w = ic.get("width", s.get("width", 32)); h = ic.get("height", s.get("height", 32))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{ic["body"]}</svg>'
    im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=groesse, output_height=groesse))).convert("RGBA")
    if spiegeln: im = ImageOps.mirror(im)
    if drehen: im = im.rotate(drehen, expand=True, resample=Image.BICUBIC)
    return im.crop(im.getbbox())


def gruppe(teile, groesse):
    """Mehrere Emojis zu einem Motiv: teile = [(name, anteil, dx, dy, drehung)], Lage relativ zur Motivgröße."""
    leinwand = Image.new("RGBA", (int(groesse * 1.8), int(groesse * 1.8))); mx = my = int(groesse * 0.4)
    for name, anteil, dx, dy, dreh in teile:
        e = emoji(name, int(groesse * anteil), drehen=dreh)
        leinwand.alpha_composite(e, (int(mx + dx * groesse), int(my + dy * groesse)))
    return leinwand.crop(leinwand.getbbox())


def sticker(im, rand=10):
    """Weiße Aufkleberkontur um ein freigestelltes Bild."""
    pad = rand + 4
    g = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad)); g.paste(im, (pad, pad), im)
    a = g.getchannel("A").point(lambda v: 255 if v > 30 else 0)
    k = a.resize((max(1, a.width // 2), max(1, a.height // 2))).filter(ImageFilter.MaxFilter(2 * (rand // 2) + 1))
    a2 = k.resize(a.size).point(lambda v: 255 if v > 90 else 0).filter(ImageFilter.GaussianBlur(1))
    kontur = Image.new("RGBA", g.size, (255, 255, 255, 255)); kontur.putalpha(a2); kontur.alpha_composite(g)
    return kontur


def person(f):
    """Figur als freigestelltes PNG (zwischengespeichert). f: {"lexi": pose} oder {"pose", "kopf", "gesicht", ...}."""
    os.makedirs(CACHE, exist_ok=True)
    schluessel = {k: f.get(k) for k in ("lexi", "pose", "kopf", "gesicht", "bart", "brille", "farben", "spiegeln")}
    pfad = os.path.join(CACHE, hashlib.sha1(json.dumps(schluessel, sort_keys=True).encode()).hexdigest()[:16] + ".png")
    if not os.path.exists(pfad):
        if f.get("lexi"):
            if f["lexi"] not in LX.POSEN:
                raise Fehler(f"Lexi-Pose '{f['lexi']}' unbekannt (erlaubt: {', '.join(LX.POSEN)})")
            im = LX.lexi(f["lexi"], hoehe=1200, spiegeln=bool(f.get("spiegeln")))
        else:
            im = peep(f["pose"], f["kopf"], f["gesicht"], f.get("bart"), f.get("brille"), f.get("farben") or {},
                      hoehe=1200, spiegeln=bool(f.get("spiegeln")))
        im.save(pfad)
    im = Image.open(pfad).convert("RGBA"); return im.crop(im.getbbox())


def linien_verstaerken(im, px=2):
    """Tuschelinien der Figur um px verbreitern (bei 168 px Anzeigebreite sonst zu dünn)."""
    arr = np.asarray(im).copy()
    tinte = (arr[..., 3] > 120) & (arr[..., :3].max(axis=2) < 70)
    dicker = ndimage.binary_dilation(tinte, iterations=px) & (arr[..., 3] > 120)
    arr[dicker, :3] = (20, 20, 20)
    return Image.fromarray(arr)


class Bild:
    def __init__(self, gebiet):
        r, g, b = ImageColor.getrgb(GEBIET[gebiet])
        grund = Image.new("RGBA", (W, H), (r, g, b, 255))
        v = Image.new("L", (W, H), 0); ImageDraw.Draw(v).ellipse((-W * .2, -H * .4, W * 1.2, H * 1.4), fill=255)
        dunkel = Image.new("RGBA", (W, H), (int(r * .7), int(g * .7), int(b * .7), 255))
        self.im = Image.composite(grund, dunkel, v.filter(ImageFilter.GaussianBlur(160)))
        self.belegt = np.zeros((H, W), bool)          # Text- und Figurenflächen (für die Überlappungsprüfung)
        self.text_unten = TEXT_Y

    def setzen(self, sp, x, y, schatten=True, belegen=True):
        x, y = int(x), int(y)
        if schatten:
            s = Image.new("RGBA", (W, H)); m = Image.new("RGBA", sp.size, (0, 0, 0, 255))
            m.putalpha(sp.getchannel("A").point(lambda v: v * 80 // 255)); s.paste(m, (x + 10, y + 8), m)
            self.im.alpha_composite(s.filter(ImageFilter.GaussianBlur(12)))
        if x >= 0 and y >= 0: self.im.alpha_composite(sp, (x, y))
        else: self.im.paste(sp, (x, y), sp)
        if belegen:
            a = np.asarray(sp.getchannel("A")) > 40
            x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + sp.width), min(H, y + sp.height)
            self.belegt[y0:y1, x0:x1] |= a[y0 - y:y1 - y, x0 - x:x1 - x]

    def frei(self, sp, x, y, abstand=14):
        """Liegt sp an (x, y) vollständig im Bild und ohne Überlappung mit Text/Figuren (inkl. Abstand)?"""
        x, y = int(x), int(y)
        if x < RAND or y < RAND or x + sp.width > W - RAND or y + sp.height > H - RAND:
            return False
        a = np.asarray(sp.getchannel("A")) > 40
        b = self.belegt[y - abstand:y + sp.height + abstand, x - abstand:x + sp.width + abstand]
        a2 = np.pad(a, abstand)[:b.shape[0], :b.shape[1]]
        return not (a2 & b).any()


def hook(bild, zeilen, max_b, groesse=200, min_g=110):
    """Text oben links, weiß mit dunkler Kontur, Wörter mit * gelb. Schriftgröße passt sich der Breite an."""
    while groesse > min_g:
        f = font(groesse)
        if max(f.getlength(z.replace("*", "")) for z in zeilen) <= max_b: break
        groesse -= 6
    f = font(groesse); d = ImageDraw.Draw(bild.im)
    lage = Image.new("L", (W, H), 0); dl = ImageDraw.Draw(lage)
    y = TEXT_Y
    zeilen = [z[:-1] + "-" if z.endswith("~") else z for z in zeilen]      # Silbentrennung als Strich zeigen
    for z in zeilen:
        x = TEXT_X
        worte = z.split(" ")
        for i, w in enumerate(worte):
            gelb = w.startswith("*"); w = w.lstrip("*"); t = w + (" " if i < len(worte) - 1 else "")
            d.text((x + 7, y + 9), t, font=f, fill=(0, 0, 0, 120), stroke_width=15, stroke_fill=(0, 0, 0, 120))
            d.text((x, y), t, font=f, fill=GELB if gelb else WEISS, stroke_width=15, stroke_fill=INK)
            dl.text((x, y), t, font=f, fill=255, stroke_width=15, stroke_fill=255)
            dl.text((x + 7, y + 9), t, font=f, fill=255, stroke_width=15, stroke_fill=255)       # Schatten
            x += f.getlength(t)
        y += int(groesse * 0.96)
    m = np.asarray(lage) > 0
    if m[:, W - RAND:].any():
        raise Fehler(f"Text zu breit: {zeilen}")
    bild.belegt |= m
    bild.text_unten = int(np.nonzero(m.any(axis=1))[0].max()) + 12      # echte Unterkante inkl. Kontur und Schatten
    return groesse


class _Messbild:
    def __init__(self):
        self.im = Image.new("RGBA", (W, H)); self.belegt = np.zeros((H, W), bool); self.text_unten = TEXT_Y


def messen(zeilen, **kw):
    """(Unterkante, Schriftgröße) des Textes, ohne ins Bild zu zeichnen; (None, 0), wenn er nicht in die Breite passt."""
    m = _Messbild()
    try:
        g = hook(m, zeilen, **kw)
    except Fehler:
        return None, 0
    return m.text_unten, g


def verbinden(zeilen):
    """Zeilen zu einer Zeile. '~' am Zeilenende ist eine Silbentrennung ('ANFECHTUNGS~' + '*KLAGE' -> '*ANFECHTUNGSKLAGE'),
    '-' ein echter Bindestrich ('RASER-' + 'FALL' -> 'RASER-FALL'); sonst mit Leerzeichen."""
    teile = []
    for z in zeilen:
        if teile and teile[-1][-1:] in "-~":
            bind = "-" if teile[-1].endswith("-") else ""
            vorn = teile.pop()[:-1]; hinten = z.split(" ", 1)
            wort = vorn.lstrip("*") + bind + hinten[0].lstrip("*")
            if vorn.startswith("*") or hinten[0].startswith("*"): wort = "*" + wort
            teile.append(wort + (" " + hinten[1] if len(hinten) > 1 else ""))
        else:
            teile.append(z)
    return " ".join(teile)


def hand(im, seite):
    """Handpunkt einer Figur: äußerster Punkt im Band 30–60 % der Höhe auf der Seite 'links'/'rechts'."""
    a = np.asarray(im.getchannel("A")) > 40
    y0, y1 = int(a.shape[0] * .30), int(a.shape[0] * .60)
    best = None
    for yy in range(y0, y1):
        xs = np.nonzero(a[yy])[0]
        if not len(xs): continue
        x = xs.min() if seite == "links" else xs.max()
        if best is None or (x < best[0] if seite == "links" else x > best[0]): best = (x, yy)
    return best


def karte(kopf, zeilen=3, breite=420, farbe=INK):
    """Weiße Lernkarte: dunkle Kopfzeile mit großem Wort (Videoart), darunter abgehakte Prüfpunkte ohne Kleintext."""
    zh = 74; kh = 104; hoehe = kh + zeilen * zh + 30
    k = Image.new("RGBA", (breite, hoehe)); d = ImageDraw.Draw(k)
    d.rounded_rectangle((0, 0, breite - 1, hoehe - 1), radius=30, fill="#FFFFFF", outline=INK, width=6)
    d.rounded_rectangle((0, 0, breite - 1, kh), radius=30, fill=farbe); d.rectangle((0, kh - 30, breite - 1, kh), fill=farbe)
    d.line((0, kh, breite, kh), fill=INK, width=6)
    groesse = 78
    while font(groesse).getlength(kopf) > breite - 50: groesse -= 4
    f = font(groesse)
    tw = f.getlength(kopf); d.text(((breite - tw) / 2, kh / 2 - f.size * 0.62), kopf, font=f, fill="#FFFFFF")
    haken = emoji("check-mark-button", 54)
    laengen = [0.78, 0.62, 0.7, 0.5, 0.66]
    for i in range(zeilen):
        y = kh + 22 + i * zh
        k.alpha_composite(haken, (30, y))
        d.rounded_rectangle((104, y + 14, 104 + int((breite - 150) * laengen[i % 5]), y + 40), radius=13, fill="#CFD6E0")
    return k


def _motiv_teile(m):
    if "teile" in m: return [tuple(t) for t in m["teile"]]
    return [(m["emoji"], 1.0, 0, 0, m.get("drehung", 0))]


def szene(spec):
    """Rendert eine geprüfte Spezifikation (siehe pruefen) zu einem 1280×720-Bild."""
    k = spec["k"]; lay = spec.get("layout", {})
    bild = Bild(spec["gebiet"])
    requisiten = []
    if spec["typ"] == "lern":
        kt = karte(spec["karte"]).rotate(-4, expand=True, resample=Image.BICUBIC)
        requisiten.append(dict(img=kt, g=470, links=True))           # Karte so groß wie der Platz unter dem Text erlaubt
        if spec.get("motiv"):
            requisiten.append(dict(teile=_motiv_teile(spec["motiv"]), g=spec["motiv"].get("g", 300), optional=True))
    elif spec.get("motiv"):
        requisiten.append(dict(teile=_motiv_teile(spec["motiv"]), g=spec["motiv"].get("g", 420)))
    # 1) Figuren rechts (Oberkörper, unten angeschnitten), in die Zone fig_links..W-RAND eingepasst
    figs = [(f, person(f)) for f in spec["figuren"]]
    hoehe = lay.get("hoehe", 1000); ueber = lay.get("ueberlappung", 0.62)

    def skaliert(h):
        return [(f, sticker(linien_verstaerken(im.resize((int(im.width * h * f.get("gross", 1) / im.height), int(h * f.get("gross", 1))), Image.LANCZOS)), 10)) for f, im in figs]

    def aufstellen(sk, oben=0):
        x = W - RAND; p = []
        for f, im in sk:
            x -= im.width
            p.append((f, im, x, max(H - int(im.height * f.get("sichtbar", 0.6)), oben)))
            x += int(im.width * (1 - ueber))
        return p

    basis = lay.get("fig_links", FIG_LINKS)
    sichtbar = figs[0][0].get("sichtbar", 0.6)

    def links_bei(h):                                           # linke Kante der Figurengruppe bei Figurenhöhe h
        b = [im.width * h * f.get("gross", 1) / im.height + 28 for f, im in figs]
        return W - RAND - (b[0] + sum(x * ueber for x in b[1:]))

    def hoehe_fuer(fl):                                         # größte Höhe, bei der die Gruppe rechts von fl bleibt
        return hoehe if links_bei(hoehe) >= fl else hoehe * (W - RAND - fl) / (W - RAND - links_bei(hoehe))

    # 2) Text (darf keine Figur berühren). Reihenfolge: neben den Figuren (Figurenzone notfalls etwas schmaler), sonst
    #    einzeilig über die volle Breite, sonst mehrzeilig mit kleinerer Schrift; die Figuren stehen dann darunter.
    zeilen = spec["text"]
    einzeilig = [verbinden(zeilen)]
    text_b = max(font(100).getlength(z.replace("*", "")) for z in zeilen) + 15
    g_ein = messen(einzeilig, max_b=W - 2 * TEXT_X, groesse=170, min_g=105)[1]
    passt_einzeilig = font(g_ein).getlength(einzeilig[0].replace("*", "")) <= W - 2 * TEXT_X if g_ein else False

    def daneben_bei(fl):
        h = hoehe_fuer(fl)
        if h < FIGUR_MIN or text_b > links_bei(h) - TEXT_X - 30: return None
        unten, g = messen(zeilen, max_b=links_bei(h) - TEXT_X - 30, min_g=100)
        if not unten or (spec["typ"] == "lern" and H - unten < KARTE_MIN): return None
        return h, g
    # Reihenfolge: neben den Figuren oder einzeilig über die volle Breite – je nachdem, was Schrift und Figuren
    # zusammen größer macht (Schriftgröße × Figurenhöhe^1,5);
    # sonst neben den Figuren bei schmalerer Figurenzone; zuletzt mehrzeilig über die volle Breite mit kleinerer Schrift.
    # Steht der Text über die volle Breite, stehen die Figuren darunter.
    daneben = daneben_bei(basis)
    if daneben and passt_einzeilig:                            # Abwägung Schriftgröße gegen Figurengröße
        h_ein = min(hoehe_fuer(basis), (H - messen(einzeilig, max_b=W - 2 * TEXT_X, groesse=170, min_g=105)[0] - 14) / sichtbar - 28)
        if g_ein * h_ein ** 1.5 > daneben[1] * daneben[0] ** 1.5:
            daneben = None
    if not daneben and not passt_einzeilig:
        daneben = next((d for d in (daneben_bei(fl) for fl in range(basis + 25, 851, 25)) if d), None)
    if daneben:
        daneben = daneben[0]
        hook(bild, zeilen, max_b=links_bei(daneben) - TEXT_X - 30, min_g=100)
        plaetze = aufstellen(skaliert(daneben))
    else:
        if passt_einzeilig:
            hook(bild, einzeilig, max_b=W - 2 * TEXT_X, groesse=170, min_g=105)
        else:
            g = 150
            while g > 100:                                     # so groß wie möglich, solange die Figuren groß bleiben
                unten = messen(zeilen, max_b=W - 2 * TEXT_X, groesse=g, min_g=g)[0]
                if unten and (H - unten - 14) / sichtbar - 28 >= FIGUR_MIN: break
                g -= 6
            hook(bild, zeilen, max_b=W - 2 * TEXT_X, groesse=g, min_g=100)
        h = min(hoehe_fuer(basis), (H - bild.text_unten - 14) / sichtbar - 28)
        if h < FIGUR_MIN:
            raise Fehler(f"{k}: Figuren würden zu klein – Text kürzen (höchstens 2 kurze Zeilen)")
        plaetze = aufstellen(skaliert(int(h)), oben=bild.text_unten + 14)

    fig_links = min(p[2] for p in plaetze)
    textmaske = bild.belegt.copy()
    figmaske = np.zeros_like(textmaske)
    for f, im, x, y in plaetze:
        a = np.asarray(im.getchannel("A")) > 40
        x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + im.width), min(H, y + im.height)
        figmaske[y0:y1, x0:x1] |= a[y0 - y:y1 - y, x0 - x:x1 - x]
    if (textmaske & figmaske).any():
        raise Fehler(f"{k}: Text überschneidet eine Figur")
    if not all(x >= RAND and x + im.width <= W - RAND for f, im, x, y in plaetze):
        raise Fehler(f"{k}: Figur seitlich angeschnitten")
    # 3) Figuren zeichnen (hinterste zuerst) und gehaltene Gegenstände an der Hand
    gehalten = []
    for f, im, x, y in reversed(plaetze):
        bild.setzen(im, x, y)
        if f.get("haelt"):
            h = f["haelt"]; seite = h.get("hand", "links")
            hx, hy = hand(im, seite)
            e = sticker(emoji(h["emoji"], h.get("g", 160), spiegeln=h.get("spiegeln", False), drehen=h.get("drehung", 0)), 8)
            ex = x + hx - (e.width * 0.75 if seite == "links" else e.width * 0.25)
            ey = min(y + hy - e.height * 0.55, H - RAND - e.height)      # bleibt im Bild, auch wenn die Figur tief steht
            gehalten.append((e, ex, ey))
            m = Image.new("RGBA", (W, H)); m.alpha_composite(e, (int(ex), int(ey)))
            bild.belegt |= np.asarray(m.getchannel("A")) > 40
    # 4) freie Requisiten: größtmöglich im freien Raum links der Figuren und unter dem Text
    for r in requisiten:
        g = r["g"]
        while True:
            if "img" in r:                                          # fertiges Bild (Lernkarte), Höhe = g
                roh = r["img"].resize((int(r["img"].width * g / r["img"].height), g), Image.LANCZOS)
            else:
                roh = gruppe(r["teile"], g)
            e = sticker(roh, 10)
            kand = [(yy, xx) for xx in range(RAND, fig_links + 40 - e.width, 10)
                    for yy in range(max(RAND, bild.text_unten - 40), H - e.height - RAND, 10)]
            if r.get("links"):                                     # Lernkarte: fest am linken Rand, sonst kleiner
                kand = [t for t in kand if t[1] <= TEXT_X + 10]
                kand.sort(key=lambda t: -t[0])
            else:
                kand.sort(key=lambda t: (-t[0], t[1]))             # möglichst tief, dann links
            platz = next(((xx, yy) for yy, xx in kand if bild.frei(e, xx, yy)), None)
            if platz:
                bild.setzen(e, *platz); break
            if r.get("optional") and g <= 200:
                break                                           # optionales Motiv nur, wenn es groß wirken kann
            if g <= 120:
                raise Fehler(f"{k}: kein freier Platz für das Motiv")
            g -= 15
    # 5) gehaltene Gegenstände obenauf – vollständig im Bild
    for e, ex, ey in gehalten:
        if not (ex >= RAND and ey >= RAND and ex + e.width <= W - RAND and ey + e.height <= H - RAND):
            raise Fehler(f"{k}: gehaltener Gegenstand ragt aus dem Bild")
        bild.setzen(e, ex, ey)
    return bild.im.convert("RGB")


def pruefen(spec):
    """Regelprüfung nach THUMBNAILS.md. Liefert (fehler, hinweise); Fehler verhindern das Rendern."""
    fehler, hinweise = [], []
    k = spec.get("k", "?")
    if spec.get("typ") not in ("fall", "lern"): fehler.append(f"{k}: typ muss 'fall' oder 'lern' sein")
    if spec.get("gebiet") not in GEBIET: fehler.append(f"{k}: unbekanntes Gebiet {spec.get('gebiet')!r}")
    text = spec.get("text") or []
    if not 1 <= len(text) <= 3: fehler.append(f"{k}: 1–3 Textzeilen erlaubt")
    worte = verbinden(text).split()
    if not any(w.startswith("*") for w in worte): fehler.append(f"{k}: genau ein Wort mit * (gelb) markieren")
    if sum(w.startswith("*") for w in worte) > 1: hinweise.append(f"{k}: mehr als ein gelbes Wort")
    if len([w for w in worte if w not in ("§", "=", "VS.", "&")]) > 4: hinweise.append(f"{k}: mehr als 4 Wörter")
    for z in text:
        if len(z.replace("*", "")) > 16: hinweise.append(f"{k}: Zeile '{z}' länger als 16 Zeichen")
        if z.replace("*", "") != z.replace("*", "").upper(): hinweise.append(f"{k}: Zeile '{z}' nicht in Großbuchstaben")
    if spec.get("typ") == "lern" and spec.get("karte") not in KARTE:
        fehler.append(f"{k}: karte muss eine von {', '.join(KARTE)} sein")
    if not spec.get("figuren"): fehler.append(f"{k}: mindestens eine Figur")
    if len(spec.get("figuren") or []) > 3: hinweise.append(f"{k}: mehr als 3 Figuren wirken bei 168 px unruhig")
    namen = []
    for f in spec.get("figuren") or []:
        if not f.get("lexi") and not all(f.get(x) for x in ("pose", "kopf", "gesicht")):
            fehler.append(f"{k}: Figur braucht pose, kopf und gesicht (oder lexi)")
        if f.get("haelt"): namen.append(f["haelt"].get("emoji"))
    if spec.get("motiv"): namen += [t[0] for t in _motiv_teile(spec["motiv"])]
    icons = emoji_satz()["icons"]
    fehler += [f"{k}: Emoji '{n}' gibt es nicht" for n in namen if n not in icons]
    return fehler, hinweise


def varianten(spec):
    """Grundfassung plus A/B-Varianten ("varianten": {"B": {Felder, die sich ändern}}) für Test & Compare."""
    yield spec
    for name, aend in (spec.get("varianten") or {}).items():
        v = {**{a: b for a, b in spec.items() if a != "varianten"}, **aend}
        v["k"] = f"{spec['k']}_{name}"
        yield v


def vorschau(bilder, ziel):
    """Kontaktbogen in Originalgröße/2 und eine Handy-Feed-Ansicht (246×138 px, Zeitstempel unten rechts)."""
    tw, th, gap, cols = 600, 338, 18, 4
    rows = (len(bilder) + cols - 1) // cols
    bog = Image.new("RGB", (cols * (tw + gap) + gap, rows * (th + gap) + gap), "#FFFFFF")
    for i, (s, im) in enumerate(bilder):
        bog.paste(im.resize((tw, th), Image.LANCZOS), (gap + (i % cols) * (tw + gap), gap + (i // cols) * (th + gap)))
    bog.save(os.path.join(ziel, "uebersicht.png"))
    n = min(len(bilder), 10); spalten = 2; proz = (n + spalten - 1) // spalten
    mob = Image.new("RGB", (spalten * 560 + 40, proz * 160 + 30), "#FFFFFF"); d = ImageDraw.Draw(mob)
    ft, fs = font(19, 700), font(15, 500)
    for i, (s, im) in enumerate(bilder[:n]):
        x, y = 20 + (i // proz) * 560, 20 + (i % proz) * 160
        mob.paste(im.resize((246, 138), Image.LANCZOS), (x, y))
        d.rounded_rectangle((x + 196, y + 112, x + 240, y + 132), radius=4, fill="#000000"); d.text((x + 202, y + 114), "6:12", font=fs, fill="#FFFFFF")
        zl, cur = [], ""
        for w in s.get("titel", s["k"]).split():
            if ft.getlength(cur + " " + w) < 270: cur = (cur + " " + w).strip()
            else: zl.append(cur); cur = w
        zl.append(cur)
        for j, z in enumerate(zl[:3]): d.text((x + 258, y + 2 + j * 24), z, font=ft, fill=INK)
        d.text((x + 258, y + 78), "LexVerse", font=fs, fill="#606060")
    mob.save(os.path.join(ziel, "handy_feed.png"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("specs", help="JSON-Datei mit einer Liste von Thumbnail-Spezifikationen")
    ap.add_argument("--out", required=True, help="Ausgabeordner (nicht im Repository)")
    ap.add_argument("--nur", help="nur diese Folgen (k, kommagetrennt)")
    ap.add_argument("--vorschau", action="store_true", help="zusätzlich Kontaktbogen und Handy-Feed erzeugen")
    ap.add_argument("--ohne-varianten", action="store_true")
    a = ap.parse_args()
    specs = json.load(open(a.specs))
    if a.nur: specs = [s for s in specs if s["k"] in a.nur.split(",")]
    os.makedirs(a.out, exist_ok=True)
    bilder, kaputt = [], 0
    for grund in specs:
        for s in ([grund] if a.ohne_varianten else varianten(grund)):
            fehler, hinweise = pruefen(s)
            for h in hinweise: print("Hinweis:", h)
            try:
                if fehler: raise Fehler("; ".join(fehler))
                im = szene(s)
            except Fehler as e:
                print("FEHLER:", e); kaputt += 1; continue
            im.save(os.path.join(a.out, f"{s['k']}.jpg"), quality=92)
            bilder.append((s, im))
    if a.vorschau and bilder: vorschau(bilder, a.out)
    print(f"{len(bilder)} Thumbnails -> {a.out}" + (f", {kaputt} mit Fehlern" if kaputt else ""))
    sys.exit(1 if kaputt else 0)


if __name__ == "__main__":
    main()
