"""Folge 225 · Staatshaftungsrecht Überblick: Welche Ansprüche hast du? – Serienstandard Open Peeps (Katzenkönig).
Übersicht mit drei Mini-Fällen (Beispielland Nordrhein-Westfalen), Figuren fiktiv: Herr Bergner wohnt über seinem
Fahrradladen; die Stadt baut die Straße um. (1) Ein Bagger des Bauhofs fährt gegen seinen Gartenzaun (Amtshaftung),
(2) sein Auto wird abgeschleppt, obwohl es außerhalb des Haltverbots stand (Primärebene: Anfechtung, Rückzahlung;
Sekundärebene: § 39 OBG NRW, Länder-Overlay NRW/BB/SN), (3) die Baustelle versperrt fünf Monate den Laden (keine Enteignung,
enteignender Eingriff, § 20 Abs. 6 StrWG NRW). Frau Wilmsen vom Tiefbauamt; ein Bauhof-Mitarbeiter (stumm).
Szenen laut ../SZENENPLAN.md: A Straße vor dem Fahrradladen, A2 drei Kacheln/Frage, B Sachverhalt, C zwei Ebenen,
D Amtshaftung (Wortlaut § 839 Abs. 1 Satz 1 BGB, Art. 34 Satz 1 GG), E Prüfschema Amtshaftung am Zaun, F Auto Primärebene,
G Auto Sekundärebene (Wortlaut § 39 Abs. 1 OBG NRW), H Länder-Overlay, I Laden: Enteignung? (Wortlaut Art. 14 Abs. 3 GG),
J Aufopferung: enteignungsgleicher/enteignender Eingriff, K Anliegerentschädigung (Wortlaut § 20 Abs. 6 StrWG NRW),
L Übersicht „Welcher Anspruch wann?“, M Rechtsweg (Wortlaut Art. 34 Satz 3 GG), N Klausurtipp (Lexi), O Merksatz (Lexi).
Handlungsgeräusche: Baggermotor, wenn der Bagger kommt; Holzbruch, wenn er gegen den Zaun fährt (../geraeusche_herkunft.json).
Straße, Haltverbotsschild, Haus und Zaun programmatisch (Grundformen, Palettenflächen, Tuschekontur); Bagger, Pylonen,
Auto, Fahrrad, Sperre usw. aus Icon-Bibliotheken (Tabler, Phosphor). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 213 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB, GG) und
recht.nrw.de (OBG NRW, StrWG NRW), Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_225/"

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e)
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
HELLGRAU = (226, 226, 222, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (Mindestgröße 26 px, mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    e = pille(glyphen(text), *a, **k)
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_225/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
_W = _wave.open("../stimme.wav"); _SR = _W.getframerate()
_X = np.frombuffer(_W.readframes(_W.getnframes()), np.int16).astype(np.float32) / 32768
_W.close()


def _hoerbares_ende(a, b, schwelle=-38.0):
    h = int(0.01 * _SR); seg = _X[int(a * _SR):int(b * _SR)]; n = len(seg) // h
    if n == 0:
        return b
    db = 20 * np.log10(np.sqrt((seg[: n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
    laut = np.nonzero(db > schwelle)[0]
    return min(b, a + (laut[-1] + 1) * 0.01) if len(laut) else min(b, a + 0.1)


def redet(basis, cx, unten, hoehe, cue, bis, **k):
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
    cj = bausteine._cj(); ta, tb = T_(cue), T_(bis)
    els = [peep_voll(basis, cx, unten, hoehe, cue, anim="cut", bis=bis, **k)]
    for s_ in cj["segmente"]:
        for w, (a, b) in zip(s_["text"].split(), s_["woerter"]):
            if a < ta - 0.01 or b > tb + 0.01:
                continue
            b = _hoerbares_ende(a, b)
            folge = bausteine.mundfolge(w)
            dauer = (b - a) * 0.88
            n = max(1, min(len(folge), int(dauer / 0.1)))
            folge = folge[:: max(1, len(folge) // n)][:n]
            for j, v in enumerate(folge):
                s0, s1 = a + dauer * j / n, a + dauer * (j + 1) / n
                els.append(peep_voll(f"{basis}_{v}", cx, unten, hoehe, (cue, round(s0 - ta, 3)), anim="cut",
                                     bis=(cue, round(s1 - ta, 3)), **k))
    return els


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]






def dicon(*a, **k):
    """Icon als Teil einer Tabelle innerhalb der Tafel (Zeilensymbol), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


# --- eigene Szenenbausteine Folge 225 ----------------------------------------------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in der Fallszene
FHA = 470                                    # Figurenhöhe in der Fallszene
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HC = "fluent-emoji-high-contrast"
ASPH = (150, 150, 158, 255)
WAND = (242, 232, 214, 255)
HOLZ = (232, 206, 160, 255)
BRAUN = (170, 122, 82, 255)

X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
IX, IU = 1560, 380                          # Requisit über den Figuren
NAME = {"BE": "Herr Bergner", "WI": "Frau Wilmsen", "BH": "Bauhof-Mitarbeiter"}
NFARBE = {"BE": BLAU, "WI": ROT, "BH": ORANGE}


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def stehend(k, x, folge, unten=930, hoehe=480, bis=None, erst="pop"):
    return [*fig(k, x, unten, hoehe, folge, bis=bis, erst=erst), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def zwei(links, folge_l, rechts, folge_r):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell))]."""
    els = []
    for i, (c, (s_, n_, br, fu)) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        els.append(ficon(s_, n_, IX, IU, br, c, fuell=fu, bis=b))
    return els


# --- Fallszene: Straße mit Fahrradladen (Seitenansicht, Grundformen + Icons) --------------------------------------------------
def strasse(c):
    """Fahrbahn als Band unter der Bodenlinie, Bodenlinie in Tusche."""
    w, h = 1800, 56
    def zz(dr, s):
        dr.rectangle((0, 0, w * s - 1, h * s - 1), fill=ASPH, outline=INK, width=4 * s)
        for x in range(60, w, 220):
            dr.rectangle((x * s, 24 * s, (x + 90) * s, 32 * s), fill=WEISS)
    return hart(El(_flaeche(w, h, zz), 60, BODEN_Y, c, "cut", 0.0, None, name="strasse"))


def haltverbot(c):
    """Haltverbotsschild (Zeichen 283 als Grundform: blaue Scheibe, roter Rand, rotes Kreuz) an einem Pfosten."""
    w, h = 130, 380
    def zz(dr, s):
        dr.rectangle((60 * s, 110 * s, 70 * s, (h - 1) * s), fill=(120, 120, 128, 255), outline=INK, width=3 * s)
        dr.ellipse((4 * s, 4 * s, 126 * s, 126 * s), fill=ROT, outline=INK, width=4 * s)
        dr.ellipse((20 * s, 20 * s, 110 * s, 110 * s), fill=BLAU, outline=INK, width=3 * s)
        for a, b in (((32, 32), (98, 98)), ((98, 32), (32, 98))):
            dr.line((a[0] * s, a[1] * s, b[0] * s, b[1] * s), fill=ROT, width=12 * s)
    return hart(El(_flaeche(w, h, zz), 95, BODEN_Y - h, c, "cut", 0.0, None, name="haltverbot"))


HX0, HX1, HTOP = 1370, 1860, 470            # Haus: links, rechts, Wandoberkante


def haus(c):
    """Haus mit Fahrradladen im Erdgeschoss (Wand, Dach, Schaufenster, Tür, Fenster oben)."""
    w, h = HX1 - HX0, BODEN_Y - (HTOP - 120)
    def zz(dr, s):
        top = 120
        dr.rectangle((6 * s, top * s, (w - 6) * s, (h - 1) * s), fill=WAND, outline=INK, width=5 * s)
        dr.polygon([(0, (top + 4) * s), (w * s // 2, 6 * s), (w * s, (top + 4) * s)], fill=ROT)
        dr.line([(0, (top + 4) * s), (w * s // 2, 6 * s), (w * s - 1, (top + 4) * s), (0, (top + 4) * s)], fill=INK,
                width=6 * s, joint="curve")
        for x0 in (70, 300):
            dr.rectangle((x0 * s, (top + 50) * s, (x0 + 110) * s, (top + 150) * s), fill=BLAU, outline=INK, width=5 * s)
        dr.rectangle((40 * s, (top + 250) * s, 300 * s, (top + 400) * s), fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.rectangle((350 * s, (top + 240) * s, 450 * s, (h - 1) * s), fill=GELB, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), HX0, HTOP - 120, c, "cut", 0.0, None, name="haus"))


ZX0, ZX1, ZH = 1110, 1345, 125               # Gartenzaun links neben dem Haus


def zaun(c, kaputt=False, bis=None):
    """Gartenzaun aus Latten (Grundformen); kaputt: zwei Latten umgeknickt, eine liegt am Boden."""
    w, h = ZX1 - ZX0, ZH + 20
    def zz(dr, s):
        n = 8
        st = w / n
        for i in range(n):
            x = 6 + i * st
            if kaputt and i in (1, 2):
                continue
            dr.rounded_rectangle((x * s, 10 * s, (x + st * 0.62) * s, (h - 2) * s), 6 * s, fill=HOLZ, outline=INK, width=4 * s)
        if kaputt:
            dr.polygon([(int((6 + 1 * st) * s), (h - 2) * s), (int((6 + 1.6 * st) * s), (h - 2) * s),
                        (int((6 + 0.6 * st) * s), int(h * 0.45) * s), (int((6 + 0.1 * st) * s), int(h * 0.55) * s)],
                       fill=HOLZ, outline=INK)
            dr.line([(int((6 + 1 * st) * s), (h - 2) * s), (int((6 + 0.1 * st) * s), int(h * 0.55) * s),
                     (int((6 + 0.6 * st) * s), int(h * 0.45) * s), (int((6 + 1.6 * st) * s), (h - 2) * s)], fill=INK, width=4 * s)
            dr.rounded_rectangle((int((6 + 2 * st) * s), (h - 22) * s, int((6 + 4.6 * st) * s), (h - 4) * s), 6 * s, fill=HOLZ,
                                 outline=INK, width=4 * s)
        for yy in (40, 95):
            x_a, x_b = (6, w - 4)
            if kaputt:
                dr.rectangle((x_a * s, yy * s, int((6 + 1 * st) * s), (yy + 10) * s), fill=HOLZ, outline=INK, width=3 * s)
                dr.rectangle((int((6 + 3 * st) * s), yy * s, x_b * s, (yy + 10) * s), fill=HOLZ, outline=INK, width=3 * s)
            else:
                dr.rectangle((x_a * s, yy * s, x_b * s, (yy + 10) * s), fill=HOLZ, outline=INK, width=3 * s)
    return El(_flaeche(w, h, zz), ZX0, BODEN_Y - h, c, "cut", 0.0, bis, name="zaun_kaputt" if kaputt else "zaun")


# ===========================================================================================================================
# A Fall: Straße vor dem Fahrradladen
# ===========================================================================================================================
BEX, WIX, BHX, BAGX0, BAGX1, AUTOX = 1745, 1460, 630, 870, 990, 360
BE_A = ("BE_redet", BEX, BODEN_Y, FHA)
WI_A = ("WI_redet_r", WIX, BODEN_Y, FHA)
GEGEN = beim("zaun", "gegen")
WIK = beim("wi1", "Die")
folie([(NULL, "Fall · Die Straße vor dem Fahrradladen"), ("umbau", "Fall · Die Stadt baut die Straße um"),
       ("zaun", "Fall · Der Zaun"), ("auto", "Fall · Das Auto"), ("laden", "Fall · Der Laden"),
       ("be1", "Fall · Herr Bergner beschwert sich")], [
    strasse(NULL), haltverbot(NULL), hart(haus(NULL)),
    hart(ficon("ph", "bicycle", 1540, HTOP + 390, 180, NULL, fuell=None, anim="cut")),
    hart(pl("Fahrräder", 1605, HTOP - 32, NULL, fill=GELB, size=28, anker="m")),
    zaun(NULL, bis=GEGEN), szene(zaun(GEGEN, kaputt=True), "225zaun*", 1.0, 0.0),
    hart(ficon("tabler", "car", AUTOX, BODEN_Y + 4, 260, NULL, fuell=BLAU, nebenfarbe=WEISS, bis="auto", anim="cut")),
    # Pillen oben links (gesprochener Gedanke)
    pl("Herr Bergner wohnt über seinem Fahrradladen", 70, 30, beim("fall", "wohnt"), fill=GELB, size=32, bis="be1"),
    pl("Die Stadt baut die Straße um", 70, 105, "umbau", fill=WEISS, size=32, bis="be1"),
    pl("Bagger des Bauhofs fährt gegen den Zaun", 70, 180, GEGEN, fill=ROT, size=32, bis="be1"),
    pl("Auto abgeschleppt – stand außerhalb des Haltverbots", 70, 255, "auto", fill=BLAU, size=32, bis="be1"),
    pl("Baustelle versperrt 5 Monate den Weg in den Laden", 70, 330, beim("laden", "versperrt"), fill=ORANGE, size=32,
       bis="be1"),
    pl("außerhalb", AUTOX, BODEN_Y - 150, beim("auto", "außerhalb"), fill=WEISS, size=28, anker="m", bis="be1"),
    # Baustelle: Pylonen, Bagger, Bauhof-Mitarbeiter
    ficon("tabler", "traffic-cone", 520, BODEN_Y + 2, 70, "umbau", fuell=ORANGE),
    ficon("tabler", "traffic-cone", 1065, BODEN_Y + 2, 70, "umbau", fuell=ORANGE),
    szene(ficon("tabler", "backhoe", BAGX0, BODEN_Y + 2, 300, "umbau", fuell=GELB, bis=GEGEN), "225bagger*", 1.0, 0.0),
    hart(ficon("tabler", "backhoe", BAGX1, BODEN_Y + 2, 300, GEGEN, fuell=GELB, anim="cut")),
    *fig("BH", BHX, BODEN_Y, FHA, [("umbau", "ruhig_r"), (GEGEN, "erschrocken_r"), ("auto", "sorge_r")]),
    ns(NAME["BH"], BHX, BODEN_Y, "umbau", NFARBE["BH"], d=0.1),
    # Baustellensperre vor der Ladentür
    ficon("tabler", "barrier-block", 1830, BODEN_Y + 2, 110, beim("laden", "versperrt"), fuell=ORANGE),
    # Herr Bergner vor seinem Haus (blickt nach links zur Baustelle)
    *fig("BE", BEX, BODEN_Y, FHA, [(NULL, "ruhig"), (GEGEN, "staunt"), ("auto", "sorge"), ("laden", "ernst")],
         bis="be1", erst="cut"),
    hart(ns(NAME["BE"], BEX, BODEN_Y, NULL, NFARBE["BE"])),
    *redet("BE_redet", BEX, BODEN_Y, FHA, "be1", "wi1"),
    *fig("BE", BEX, BODEN_Y, FHA, [("wi1", "denkt")], erst="cut"),
    blase("sprech", 640, 240, "be1", 1290, 210, inhalt=["Mein Zaun ist kaputt, mein", "Auto war weg, und in meinen",
                                                        "Laden kommt kein Kunde mehr!"], textsize=32, figur=BE_A, bis="wi1"),
    # Frau Wilmsen vom Tiefbauamt kommt dazu (blickt nach rechts zu Herrn Bergner)
    *redet("WI_redet_r", WIX, BODEN_Y, FHA, "wi1", "frage"),
    ns(NAME["WI"], WIX, BODEN_Y, "wi1", NFARBE["WI"], d=0.1),
    blase("sprech", 600, 220, "wi1", 1130, 210, inhalt=["Die Straße muss gemacht", "werden, Herr Bergner.",
                                                        "Das trifft alle hier."], textsize=32, figur=WI_A),
])


# ===========================================================================================================================
# A2 Die Frage: drei Kacheln
# ===========================================================================================================================
def kachel(x, cue, kopf, zeilen, icon, fuell, farbe):
    els = [karte(x, 150, 540, 500, cue, fill=WEISS), karte(x, 150, 540, 90, cue, fill=farbe, rund=26, schatten=0),
           z(kopf, x + 270 - F("ExtraBold", 40).getlength(kopf) / 2, 168, cue, "ExtraBold", 40, rechts=x + 530),
           ficon(*icon, x + 270, 470, 200, cue, fuell=fuell)]
    for i, t in enumerate(zeilen):
        els.append(z(t, x + 270 - F("Bold", 32).getlength(t) / 2, 505 + i * 48, cue, "Bold", 32, rechts=x + 530))
    return els


folie([("frage", "Fall · Die Frage")], [
    *kachel(100, "frage", "1 · Zaun", ["Bagger des Bauhofs", "beschädigt ihn"], ("tabler", "fence", ), HOLZ, ROT),
    *kachel(690, "frage", "2 · Auto", ["abgeschleppt, obwohl", "außerhalb des Haltverbots"],
            ("tabler", "car"), BLAU, BLAU),
    *kachel(1280, "frage", "3 · Laden", ["5 Monate versperrt,", "keine Kunden"], ("ph", "storefront"), GELB,
            ORANGE),
    pl("Welche Ansprüche hat Herr Bergner gegen die Stadt?", 960, 760, "frage", fill=PINK, size=44, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_225(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 85, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_225("sv", [
    "Herr Bergner wohnt in einer Stadt in Nordrhein-Westfalen über seinem kleinen Fahrradladen. Die Stadt baut die Straße "
    "davor um. Ein Mitarbeiter des städtischen Bauhofs fährt beim Rangieren mit dem Bagger unachtsam gegen Herrn Bergners "
    "Gartenzaun. Die Reparatur kostet 1.200 €; Ersatz von anderer Seite gibt es nicht.",
    "Herrn Bergners Auto steht in einer Seitenstraße, außerhalb einer Haltverbotszone. Die Stadt lässt es trotzdem "
    "abschleppen und setzt die Kosten von 250 € durch Bescheid fest. Herr Bergner zahlt, um sein Auto zurückzubekommen; "
    "für das Taxi zum Abschlepphof zahlt er 30 €.",
    "Die Baustelle versperrt 5 Monate lang den Zugang zu seinem Laden; einen Behelfsweg gibt es nicht. Die Kunden bleiben "
    "aus, der Laden steht vor dem Aus. Frau Wilmsen vom Tiefbauamt der Stadt meint, das treffe alle Anlieger.",
], "Welche Ansprüche hat Herr Bergner gegen die Stadt?")

# ===========================================================================================================================
# C Zwei Ebenen
# ===========================================================================================================================
folie([("ebenen", "Überblick · Zwei Ebenen"), ("primaer", "Überblick › Primärebene"), ("sekundaer", "Überblick › Sekundärebene")],
      rechts_frei([
    *tafel("ebenen", "Zwei Ebenen"),
    blk(110, 200, 1040, 200, BLAU, "primaer", [("Primärebene", "ExtraBold", 42, INK),
                                                ("Abwehr der Maßnahme selbst", "Bold", 36, INK)]),
    blk(110, 450, 1040, 200, GELB, "sekundaer", [("Sekundärebene", "ExtraBold", 42, INK),
                                                  ("Geld: Schadensersatz oder Entschädigung", "Bold", 36, INK)]),
    zit("Begriffe z. B. BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 27", 110, 700, "sekundaer"),
    *requisit([("primaer", ("tabler", "shield-check", 110, BLAU)), ("sekundaer", ("tabler", "cash-banknote", 130, GRUEN))]),
    *zwei("WI", [("ebenen", "ruhig"), ("sekundaer", "denkt")], "BE", [("ebenen", "ruhig"), ("primaer", "ernst"),
                                                                     ("sekundaer", "denkt")]),
]))

# ===========================================================================================================================
# D Amtshaftung: Wortlaut § 839 Abs. 1 Satz 1 BGB, Art. 34 Satz 1 GG
# ===========================================================================================================================
W839 = ("„(1) Verletzt ein Beamter vorsätzlich oder fahrlässig die ihm einem Dritten gegenüber obliegende Amtspflicht, so hat "
        "er dem Dritten den daraus entstehenden Schaden zu ersetzen. …“")
W34 = ("„Verletzt jemand in Ausübung eines ihm anvertrauten öffentlichen Amtes die ihm einem Dritten gegenüber obliegende "
       "Amtspflicht, so trifft die Verantwortlichkeit grundsätzlich den Staat oder die Körperschaft, in deren Dienst er steht. …“")
w839, w839_y = wortlaut(80, 170, 1100, W839, "§ 839 Abs. 1 Satz 1 BGB", beim("w839", "Paragraf"), marken=[
    ("Beamter", beim("w839", "Beamter")), ("Dritten", beim("w839", "Dritten")),
    ("Amtspflicht", beim("w839", "Amtspflicht")), ("Schaden zu ersetzen", beim("w839", "Schaden"))], size=30)
w34, w34_y = wortlaut(80, w839_y + 24, 1100, W34, "Art. 34 Satz 1 GG", "w34", marken=[
    ("Verantwortlichkeit", beim("w34", "Verantwortlichkeit")), ("Staat", beim("w34", "Staat")),
    ("Körperschaft", beim("w34", "Körperschaft"))], size=30)
assert w34_y <= 890, w34_y
folie([("ah", "Amtshaftung · § 839 BGB"), ("w34", "Amtshaftung › Art. 34 Satz 1 GG")], rechts_frei([
    *tafel("ah", "Der Zaun: Amtshaftung", size=44),
    *w839, *w34,
    *requisit([("ah", ("tabler", "fence", 140, HOLZ)), ("w34", ("tabler", "building-bank", 120, WEISS))]),
    *allein("BE", [("ah", "ernst"), ("w34", "denkt")]),
]))

# ===========================================================================================================================
# E Amtshaftung: Prüfschema am Fall Zaun
# ===========================================================================================================================
def nr(n, y, cue, farbe=BLAU):
    return [karte(110, y + 2, 50, 50, cue, fill=farbe, rund=12, schatten=3, rand=4),
            z(n, 135 - F("ExtraBold", 32).getlength(n) / 2, y + 4, cue, "ExtraBold", 32)]


els_e = [*tafel("s1", "Amtshaftung: Prüfschema", size=44),
         *nr("1", 170, "s1"), z("Beamter im haftungsrechtlichen Sinn", 180, 170, "s1", "Bold", 33),
         z("auch Angestellte, sogar private Helfer", 210, 218, "s1b", size=30),
         zit("BGH, Urt. v. 18.2.2014 – VI ZR 383/12, Rn. 5–7", 210, 258, beim("s1b", "Abschleppunternehmer")),
         *okz("Bauhof; Straßenbau hoheitlich, § 9a Abs. 1 StrWG NRW", 296, "s1c", size=30, x=250),
         *nr("2", 352, "s2"), z("Amtspflichtverletzung", 180, 352, "s2", "Bold", 33),
         *okz("fremdes Eigentum nicht beschädigen", 398, beim("s2", "Amtsträger"), size=30, x=250),
         zit("BGH, Urt. v. 4.7.2013 – III ZR 250/12, Rn. 13", 250, 440, beim("s2", "Amtsträger")),
         *nr("3", 482, "s3"), z("Drittbezogenheit", 180, 482, "s3", "Bold", 33),
         *okz("schützt gerade den Eigentümer", 482, beim("s3", "Pflicht"), size=30, x=520),
         *nr("4", 542, "s4"), z("Verschulden", 180, 542, "s4", "Bold", 33),
         *okz("nicht aufgepasst: fahrlässig", 542, beim("s4", "Fahrer"), size=30, x=520),
         *nr("5", 602, "s5"), z("Schaden", 180, 602, "s5", "Bold", 33),
         *okz("1.200 € Reparatur", 602, beim("s5", "zwölfhundert"), size=30, x=520),
         *nr("6", 662, "s6"), z("kein Ausschluss", 180, 662, "s6", "Bold", 33),
         z("§ 839 Abs. 1 Satz 2: kein anderer Ersatz", 250, 708, beim("s6", "Bei"), size=30),
         z("§ 839 Abs. 3: Rechtsmittel versäumt", 250, 752, "s6b", size=30),
         *okz("beides greift nicht", 796, "s6c", size=30, x=250),
         blk(110, 845, 1040, 70, GRUEN, "s7", [("Die Stadt ersetzt den Zaun (Art. 34 Satz 1 GG)", "ExtraBold", 32, INK)]),
         *requisit([("s1", ("tabler", "backhoe", 160, GELB)), ("s2", ("tabler", "fence", 140, HOLZ)),
                    ("s4", ("tabler", "alert-triangle", 110, GELB)), ("s5", ("tabler", "receipt-euro", 110, WEISS)),
                    ("s6", ("tabler", "scale", 120, WEISS)), ("s7", ("tabler", "cash-banknote", 130, GRUEN))]),
         *zwei("BH", [("s1", "ruhig"), ("s4", "sorge")], "BE", [("s1", "ruhig"), ("s3", "denkt"), ("s7", "froh")])]
folie([("s1", "Amtshaftung › 1. Beamter im haftungsrechtlichen Sinn"), ("s2", "Amtshaftung › 2. Amtspflichtverletzung"),
       ("s3", "Amtshaftung › 3. Drittbezogenheit"), ("s4", "Amtshaftung › 4. Verschulden"), ("s5", "Amtshaftung › 5. Schaden"),
       ("s6", "Amtshaftung › 6. kein Ausschluss"), ("s7", "Amtshaftung › Ergebnis: Zaun")], rechts_frei(els_e))

# ===========================================================================================================================
# F Das Auto: Primärebene
# ===========================================================================================================================
folie([("ab", "Das Auto · rechtswidrig abgeschleppt"), ("anf", "Das Auto › Primärebene: Anfechtung"),
       ("rueck", "Das Auto › Primärebene: Geld zurück"), ("fba", "Das Auto › Folgenbeseitigung")], rechts_frei([
    *tafel("ab", "Das Auto: Primärebene"),
    *neinz("außerhalb des Haltverbots: rechtswidrig", 190, beim("ab", "Abschleppen"), "Bold", 34),
    z("Kosten nur für rechtmäßiges Abschleppen", 140, 262, "konnex", size=34),
    zit("BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 11", 140, 310, beim("konnex", "Abschleppen")),
    *okz("Anfechtung des Kostenbescheids (250 €)", 370, beim("anf", "ficht"), "Bold", 34),
    *okz("Rückzahlung im selben Urteil", 450, beim("rueck", "Das"), "Bold", 34),
    zit("§ 113 Abs. 1 Satz 2 VwGO; vgl. BVerwG 3 C 25.16:", 185, 498, beim("rueck", "zurückzahlt")),
    zit("Bescheid aufgehoben, Zahlung angeordnet", 185, 534, beim("rueck", "zurückzahlt")),
    blk(110, 600, 1040, 90, LILA, "fba", [("Folgenbeseitigung: Video „Folgenbeseitigungsanspruch“", "ExtraBold", 32, INK)]),
    zit("BVerwG, Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14", 110, 712, "fba"),
    *requisit([("ab", ("tabler", "car", 160, BLAU)), ("anf", ("tabler", "file-invoice", 110, WEISS)),
               ("rueck", ("tabler", "cash-banknote", 130, GRUEN)), ("fba", ("tabler", "restore", 110, LILA))]),
    *allein("BE", [("ab", "ernst"), ("anf", "denkt"), ("rueck", "froh")]),
]))

# ===========================================================================================================================
# G Sekundärebene: Wortlaut § 39 Abs. 1 OBG NRW
# ===========================================================================================================================
W39 = ("„(1) Ein Schaden, den jemand durch Maßnahmen der Ordnungsbehörden erleidet, ist zu ersetzen, wenn er … b) durch "
       "rechtswidrige Maßnahmen, gleichgültig, ob die Ordnungsbehörden ein Verschulden trifft oder nicht, entstanden ist.“")
w39, w39_y = wortlaut(80, 250, 1100, W39, "§ 39 Abs. 1 OBG NRW (Auszug)", "w39", marken=[
    ("Schaden", beim("w39", "Schäden")), ("rechtswidrige Maßnahmen", beim("w39", "rechtswidrige")),
    ("gleichgültig", beim("w39", "gleichgültig")), ("Verschulden", beim("w39", "Verschulden"))], size=30)
folie([("taxi", "Das Auto › Sekundärebene: Taxi"), ("w39", "Das Auto › § 39 Abs. 1 OBG NRW")], rechts_frei([
    *tafel("taxi", "Das Auto: Sekundärebene"),
    z("30 € Taxi zum Abschlepphof", 110, 180, beim("taxi", "dreißig"), "Bold", 36),
    *w39,
    *okz("nur Vermögensschäden, also auch das Taxi", w39_y + 40, "vermoegen", "Bold", 34),
    zit("§ 40 Abs. 1 Satz 1 OBG NRW; verschuldensunabhängig:", 185, w39_y + 90, "vermoegen"),
    zit("BGH, Urt. v. 19.1.2006 – III ZR 82/05, Rn. 9", 185, w39_y + 126, "vermoegen"),
    pl("Beispiel Nordrhein-Westfalen", 1120, 182, "w39", fill=GELB, size=28, anker="r"),
    *requisit([("taxi", ("ph", "taxi", 160, GELB)), ("w39", ("tabler", "scale", 120, WEISS)),
               ("vermoegen", ("ph", "taxi", 160, GELB))]),
    *allein("BE", [("taxi", "denkt"), ("vermoegen", "froh")]),
]))
assert w39_y + 170 <= 940, w39_y

# ===========================================================================================================================
# H Länder-Overlay: Entschädigung bei rechtswidrigen Maßnahmen (nur am Landesportal geprüfte Normen)
# ===========================================================================================================================
CL, CN = 110, 470
TY = 250
ZEILEN = [("tnrw", "Nordrhein-Westfalen", ["§ 39 Abs. 1 Buchst. b OBG NRW", "Polizei: § 67 PolG NRW"], ["neununddreißig", "siebenundsechzig"]),
          ("tbb", "Brandenburg", ["§ 38 Abs. 1 Buchst. b OBG"], ["achtunddreißig"]),
          ("tsn", "Sachsen", ["§ 41 Abs. 1 Nr. 2 SächsPBG"], ["einundvierzig"])]
els_t = [*tafel("tab", "Länder-Overlay: Entschädigung", size=42),
         z("bei rechtswidrigen Maßnahmen, ohne Verschulden", 110, 165, "tab", "Bold", 30, farbe=TEXT),
         z("Land", CL, TY - 50, "tab", "Bold", 28, farbe=TEXT), z("Vorschrift", CN, TY - 50, "tab", "Bold", 28, farbe=TEXT),
         linienzug([(110, TY - 8), (1160, TY - 8)], "tab", breite=3)]
y = TY + 10
for c, land, normen, worte in ZEILEN:
    els_t.append(z(land, CL, y, c, "Bold", 30))
    for k, (nm, w) in enumerate(zip(normen, worte)):
        els_t.append(z(nm, CN, y + k * 48, beim(c, w) if k else c, size=30))
    y += 48 * len(normen) + 40
    els_t.append(linienzug([(110, y - 22), (1160, y - 22)], c, breite=2, farbe=(200, 200, 205, 255)))
els_t += [z("dein Land: Polizei- oder Ordnungsgesetz", 110, y + 10, "teigen", "Bold", 32),
          zit("geprüft an recht.nrw.de, bravors.brandenburg.de, revosax.sachsen.de (Abruf 7.10.2026)", 110, y + 62,
              beim("teigen", "Polizei")),
          ficon("tabler", "map-2", IX, IU, 140, "tab", fuell=WEISS),
          *allein("WI", [("tab", "ruhig"), ("tsn", "denkt"), ("teigen", "froh")])]
assert y + 100 <= 940, y
folie([("tab", "Länder-Overlay · Entschädigung"), ("tnrw", "Länder-Overlay › Nordrhein-Westfalen"),
       ("tbb", "Länder-Overlay › Brandenburg"), ("tsn", "Länder-Overlay › Sachsen"),
       ("teigen", "Länder-Overlay › dein Landesgesetz")], rechts_frei(els_t))

# ===========================================================================================================================
# I Der Laden: Enteignung? Wortlaut Art. 14 Abs. 3 Satz 1, 2 GG
# ===========================================================================================================================
W14 = ("„(3) Eine Enteignung ist nur zum Wohle der Allgemeinheit zulässig. Sie darf nur durch Gesetz oder auf Grund eines "
       "Gesetzes erfolgen, das Art und Ausmaß der Entschädigung regelt. …“")
w14, w14_y = wortlaut(80, 170, 1100, W14, "Art. 14 Abs. 3 Satz 1, 2 GG", beim("w14", "Artikel"), marken=[
    ("Wohle der Allgemeinheit", beim("w14", "Wohle")), ("durch Gesetz", beim("w14", "Gesetz")),
    ("Ausmaß der Entschädigung", beim("w14", "Ausmaß"))], size=30)
folie([("la", "Der Laden · Enteignung?"), ("entzug", "Der Laden › Begriff der Enteignung"),
       ("nichts", "Der Laden › keine Enteignung")], rechts_frei([
    *tafel("la", "Der Laden: eine Enteignung?", size=44),
    *w14,
    blk(110, w14_y + 40, 1040, 90, BLAU, "entzug", [("Enteignung: Der Staat entzieht konkretes Eigentum", "ExtraBold", 33, INK)]),
    zit("BVerfG, Beschl. v. 15.7.1981 – 1 BvL 77/78 (Naßauskiesung),", 110, w14_y + 150, beim("entzug", "Staat")),
    zit("BVerfGE 58, 300 (330 f.), DFR-Rn. 145 f.", 110, w14_y + 186, beim("entzug", "Staat")),
    *neinz("Herrn Bergner wird nichts entzogen", w14_y + 250, "nichts", "Bold", 34),
    *requisit([("la", ("ph", "storefront", 150, GELB)), ("entzug", ("tabler", "building-bank", 120, WEISS)),
               ("nichts", ("ph", "storefront", 150, GELB))]),
    *zwei("WI", [("la", "ruhig"), ("nichts", "ernst")], "BE", [("la", "sorge"), ("entzug", "denkt")]),
]))
assert w14_y + 300 <= 890, w14_y

# ===========================================================================================================================
# J Aufopferungsgedanke: enteignungsgleicher und enteignender Eingriff
# ===========================================================================================================================
folie([("auf", "Der Laden › Aufopferungsgedanke"), ("egl", "Der Laden › enteignungsgleicher Eingriff"),
       ("ee", "Der Laden › enteignender Eingriff")], rechts_frei([
    *tafel("auf", "Aufopferung: zwei Ansprüche", size=44),
    z("Sonderopfer für das Gemeinwohl: Entschädigung", 110, 175, beim("auf", "Wer"), "Bold", 34),
    z("gewohnheitsrechtlich, § 75 Einl. Pr. ALR (1794)", 110, 228, "alr", size=32),
    zit("BGH, Urt. v. 7.9.2017 – III ZR 71/17, Rn. 16", 110, 272, beim("alr", "preußische")),
    blk(110, 330, 1040, 150, ROT, "egl", [("enteignungsgleicher Eingriff", "ExtraBold", 38, INK),
                                          ("rechtswidrig, unmittelbar, ohne Verschulden", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 15.12.2016 – III ZR 387/14, Rn. 20 f.", 110, 492, beim("egl", "Verschulden")),
    blk(110, 545, 1040, 150, GRUEN, "ee", [("enteignender Eingriff", "ExtraBold", 38, INK),
                                           ("rechtmäßig, untypische Nebenfolge, unzumutbar", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 17.3.2022 – III ZR 79/21, Rn. 56; Urt. v. 14.3.2013 – III ZR 253/12, Rn. 8", 110, 707,
        beim("ee", "Zumutbare")),
    *okz("Straßenumbau rechtmäßig: enteignender Eingriff", 770, "bau", "Bold", 34),
    *requisit([("auf", ("ph", "hand-heart", 130, ROT)), ("egl", ("tabler", "alert-triangle", 110, ROT)),
               ("ee", ("tabler", "barrier-block", 140, ORANGE))]),
    *zwei("WI", [("auf", "ruhig"), ("bau", "denkt")], "BE", [("auf", "denkt"), ("ee", "ernst")]),
]))

# ===========================================================================================================================
# K Anliegerentschädigung: Wortlaut § 20 Abs. 6 Satz 1 StrWG NRW
# ===========================================================================================================================
W20 = ("„(6) Werden durch Straßenarbeiten Zufahrten oder Zugänge für längere Zeit unterbrochen oder wird ihre Benutzung "
       "erheblich erschwert, ohne daß von Behelfsmaßnahmen eine wesentliche Entlastung ausgeht, und wird dadurch die "
       "wirtschaftliche Existenz eines anliegenden Betriebes gefährdet, so kann dessen Inhaber eine Entschädigung in Höhe des "
       "Betrages beanspruchen, der erforderlich ist, um das Fortbestehen des Betriebes bei Anspannung der eigenen Kräfte und "
       "unter Berücksichtigung der gegebenen Anpassungsmöglichkeiten zu sichern. …“")
w20, w20_y = wortlaut(80, 230, 1100, W20, "§ 20 Abs. 6 Satz 1 StrWG NRW", beim("w20", "Paragraf"), marken=[
    ("für längere Zeit", beim("m1", "längere")), ("unterbrochen", beim("m1", "unterbrochen")), ("erheblich erschwert", beim("m1", "erheblich")),
    ("Behelfsmaßnahmen", "m2"), ("wirtschaftliche Existenz", beim("m3", "wirtschaftliche")),
    ("Fortbestehen des Betriebes", beim("hoehe", "Fortbestehen"))], size=28)
folie([("anl", "Der Laden › Anlieger"), ("w20", "Der Laden › § 20 Abs. 6 StrWG NRW"), ("hoehe", "Der Laden › Höhe"),
       ("lerg", "Der Laden › Ergebnis")], rechts_frei([
    *tafel("anl", "Der Laden: Anliegerentschädigung", size=42),
    z("normale Baustellen: hinnehmen", 110, 170, beim("anl", "Normale"), "Bold", 32),
    *w20,
    z("nicht der ganze entgangene Gewinn", 110, w20_y + 22, beim("hoehe", "nicht"), "Bold", 32),
    *okz("5 Monate ohne Behelfsweg, Laden vor dem Aus: Entschädigung", w20_y + 82, beim("lerg", "Herr"), "Bold", 32),
    *requisit([("anl", ("tabler", "barrier-block", 140, ORANGE)), ("m1", ("tabler", "hourglass", 100, GELB)),
               ("m3", ("ph", "storefront", 150, GELB)), ("hoehe", ("tabler", "cash-banknote", 130, GRUEN))]),
    *allein("BE", [("anl", "sorge"), ("m3", "ernst"), (beim("lerg", "Herr"), "froh")]),
]))
assert w20_y + 130 <= 890, w20_y

# ===========================================================================================================================
# L Übersicht: Welcher Anspruch wann? (Aufbau Zeile für Zeile)
# ===========================================================================================================================
REIHEN = [("u1", "rechtswidriger Zustand dauert an", "Folgenbeseitigung", ("tabler", "restore", LILA)),
          ("u2", "rechtswidrig und schuldhaft", "Amtshaftung: Schadensersatz", ("tabler", "fence", HOLZ)),
          ("u3", "rechtswidrig, auch ohne Verschulden", "enteignungsgleicher Eingriff, Landesrecht", ("ph", "taxi", GELB)),
          ("u4", "rechtmäßig, aber ein Sonderopfer", "enteignender Eingriff, Sonderregel", ("ph", "storefront", GELB)),
          ("u5", "Opfer an Leben oder Gesundheit", "Aufopferungsanspruch", ("tabler", "first-aid-kit", ROT))]
els_u = [karte(60, 50, 1800, 940, "ueb"), titel(glyphen("Welcher Anspruch wann?"), 110, 90, "ueb", 52),
         z("Situation", 200, 200, "ueb", "Bold", 30, rechts=1820, farbe=TEXT),
         z("Anspruch", 1000, 200, "ueb", "Bold", 30, rechts=1820, farbe=TEXT),
         linienzug([(110, 248), (1810, 248)], "ueb", breite=3)]
y = 275
for c, sit, ans, (s_, n_, fu) in REIHEN:
    els_u += [dicon(s_, n_, 145, y + 72, 70, c, fuell=fu),
              z(sit, 200, y + 14, c, "Bold", 36, rechts=980),
              z(ans, 1000, y + 14, c, "ExtraBold", 36, rechts=1820)]
    y += 125
    els_u.append(linienzug([(110, y - 20), (1810, y - 20)], c, breite=2, farbe=(200, 200, 205, 255)))
els_u.append(zit("Belege: § 839 BGB, Art. 34 GG; § 39 OBG NRW; § 20 Abs. 6 StrWG NRW; BGH III ZR 387/14, III ZR 79/21, "
                 "III ZR 71/17", 110, y + 10, "u5", rechts=1820))
assert y + 50 <= 970, y
folie([("ueb", "Übersicht · Welcher Anspruch wann?"), ("u1", "Übersicht › Folgenbeseitigung"), ("u2", "Übersicht › Amtshaftung"),
       ("u3", "Übersicht › enteignungsgleicher Eingriff, Landesrecht"), ("u4", "Übersicht › enteignender Eingriff"),
       ("u5", "Übersicht › Aufopferung")], els_u)

# ===========================================================================================================================
# M Rechtsweg: Wortlaut Art. 34 Satz 3 GG, § 40 Abs. 2 VwGO
# ===========================================================================================================================
W34_3 = "„Für den Anspruch auf Schadensersatz und für den Rückgriff darf der ordentliche Rechtsweg nicht ausgeschlossen werden.“"
w343, w343_y = wortlaut(80, 170, 1100, W34_3, "Art. 34 Satz 3 GG", beim("rw34", "Artikel"), marken=[
    ("ordentliche Rechtsweg", beim("rw34", "ordentliche"))], size=30)
folie([("rw", "Rechtsweg"), ("rw34", "Rechtsweg › Art. 34 Satz 3 GG"), ("rw40", "Rechtsweg › § 40 Abs. 2 VwGO"),
       ("rwvg", "Rechtsweg › Verwaltungsgericht")], rechts_frei([
    *tafel("rw", "Rechtsweg"),
    *w343,
    *okz("Aufopferung (vermögensrechtlich): ordentliche Gerichte", w343_y + 40, beim("rw40", "vermögensrechtliche"), "Bold", 32),
    zit("§ 40 Abs. 2 Satz 1 VwGO; Landesrecht z. B. § 43 Abs. 1 OBG NRW", 185, w343_y + 88, beim("rw40", "Paragraf")),
    *okz("Kostenbescheid, Folgenbeseitigung: Verwaltungsgericht", w343_y + 150, "rwvg", "Bold", 32),
    zit("§ 40 Abs. 1 VwGO; BVerwG, Urt. v. 27.2.2019 – 6 C 1.18, Rn. 14 (Leistungsklage)", 185, w343_y + 198, "rwvg"),
    *requisit([("rw", ("tabler", "gavel", 120, WEISS)), ("rwvg", ("tabler", "building-bank", 120, WEISS))]),
    *zwei("WI", [("rw", "ruhig"), ("rwvg", "denkt")], "BE", [("rw", "denkt"), ("rw34", "ernst")]),
]))
assert w343_y + 240 <= 940, w343_y

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst die Primärebene"), ("t2", "Klausurtipp › kein Wahlrecht"),
       ("t3", "Klausurtipp › Ansprüche nebeneinander")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe zuerst die Primärebene", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("Wer sich nicht wehrt, riskiert das Geld:", 200, 290, "t1", size=34),
    z("§ 839 Abs. 3 BGB", 200, 340, beim("t1", "Paragraf"), "Bold", 34),
    z("rechtswidrige Enteignung: kein Wahlrecht,", 200, 430, "t2", size=34),
    z("erst anfechten", 200, 480, beim("t2", "erst"), "Bold", 34),
    zit("BVerfGE 58, 300 (324), DFR-Rn. 121", 200, 530, beim("t2", "erst")),
    z("Amtshaftung und Entschädigung", 200, 610, "t3", size=34),
    z("nebeneinander prüfen", 200, 660, beim("t3", "nebeneinander"), "Bold", 34),
    zit("vgl. § 40 Abs. 5 OBG NRW", 200, 710, beim("t3", "nebeneinander")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst ", 0), ("abwehren", "a"), (", dann Geld.", 0)]], 750, 300, 48, "merke", {"a": beim("merke", "abwehren")}),
    *markertext([[("Mit Verschulden zahlt der Staat", 0)], [("Schadensersatz", "b"), (", ohne Verschulden", 0)],
                 [("Entschädigung", "c"), (", wenn ein Gesetz oder", 0)], [("ein Sonderopfer sie trägt.", 0)]],
                750, 450, 42, "mk2", {"b": beim("mk2", "Schadensersatz"), "c": beim("mk2", "Entschädigung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
