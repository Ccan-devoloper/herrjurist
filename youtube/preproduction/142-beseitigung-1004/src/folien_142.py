"""Folge 142 · Äste auf dem Garagendach: Beseitigungsanspruch aus § 1004 BGB – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Franziska (NRW) hat neben ihrem Haus eine Garage; der große Ahorn ihrer Nachbarin Rosemarie steht vier Meter von der
Grenze entfernt. Seit dem letzten Sommer ragen seine Äste über das Garagendach, im Herbst verstopft das Laub die Dachrinne.
Szenen laut ../SZENENPLAN.md: A1 Äste über der Garage (Grundstücke in Seitenansicht), A2 am Gartenzaun / Frage, B Sachverhalt,
C Wortlautkarte § 1004 Abs. 1 S. 1, § 903, vier Prüfungspunkte, D1 1. Eigentum / 2. Beeinträchtigung, D2 3. Störerin,
D3 Gegenfall Laub vom Baum selbst (Grenzabstand § 41 NachbG NRW, § 906 Abs. 2 S. 2 analog), E 4. keine Duldungspflicht
(§ 910 Abs. 2 statt § 906), F Verjährung und Zwischenergebnis, G Wortlautkarte § 910, H Verhältnis/Grenzen/Kosten,
I III. Unterlassung, J Ergebnis am Gartenzaun (Fristsetzung), K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Baum, Äste, Garage und Rinne stilisiert (Icons nur mit Palettenfarben gefüllt; Garage, Grenze und Ast als einfache
Tuscheformen wie die Straße in Folge 140). Keine Säge, kein Fällen im Bild; die Astschere erscheint nur als Icon.
Zwei Handlungsgeräusche (Laub fällt in die Rinne, Leiter wird angestellt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 140 (gemeinsame Dateien unverändert); neu: garage(), grenze(), ast(), laub().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_142/"

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
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_142/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        t = zeilen[zi]
        a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/140) ----------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=160, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=160, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
FR_N, RO_N = BLAU, GRUEN                    # Farben der Namensschilder (Hemd bzw. Hose)
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"FR": "Franziska", "RO": "Rosemarie"}
NFARBE = {"FR": FR_N, "RO": RO_N}
HOLZ = (214, 160, 110, 255)
DACH = (226, 222, 214, 255)


def boden(cue, hart_=False, x0=40, x1=1880):
    e = linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel FR/RO."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


# --- Szenenbausteine Fall (programmatisch, Palettenflächen, Tuschekontur) -------------------------------------------------
def garage(x0, x1, oben, cue, anim="pop", rinne=True):
    """Fertiggarage in Vorderansicht: gelbe Wand, Flachdach, Sektionaltor, Dachrinne als Halbrohr unter der Dachkante."""
    s = 2
    W_, H_ = (x1 - x0 + 60) * s, (BODEN - oben + 60) * s
    im = Image.new("RGBA", (W_, H_))
    d = ImageDraw.Draw(im)
    ox, oy = 30 * s, 30 * s                                   # Ursprung (x0, oben - 30) im Bild
    X = lambda x: (x - x0) * s + ox
    Y = lambda y: (y - oben) * s + oy
    d.rectangle((X(x0), Y(oben), X(x1), Y(BODEN)), fill=GELB, outline=INK, width=6 * s)
    tor = (x0 + (x1 - x0) * 0.16, oben + 70, x1 - (x1 - x0) * 0.16, BODEN)
    d.rectangle((X(tor[0]), Y(tor[1]), X(tor[2]), Y(tor[3])), fill=WEISS, outline=INK, width=5 * s)
    for k in range(1, 4):
        yy = tor[1] + (tor[3] - tor[1]) * k / 4
        d.line((X(tor[0]), Y(yy), X(tor[2]), Y(yy)), fill=INK, width=4 * s)
    d.rectangle((X(x0 - 20), Y(oben - 26), X(x1 + 20), Y(oben)), fill=DACH, outline=INK, width=6 * s)
    if rinne:
        d.rounded_rectangle((X(x0 - 14), Y(oben), X(x1 + 14), Y(oben + 24)), radius=12 * s, fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((W_ // s, H_ // s), Image.LANCZOS)
    return El(im, x0 - 30, oben - 30, cue, anim, 0.0, None, name="garage")


def grenze(x, y0, cue, anim="pop"):
    """Grundstücksgrenze als gestrichelte Tuschelinie."""
    im = Image.new("RGBA", (16, BODEN - y0))
    d = ImageDraw.Draw(im)
    for yy in range(0, BODEN - y0, 34):
        d.line((8, yy, 8, min(BODEN - y0, yy + 20)), fill=INK, width=6)
    return El(im, x - 8, y0, cue, anim, 0.0, None, name="grenze")


def ast(punkte, cue, d=0.0):
    """Ast als kräftige Tuschelinie (über die Grenze)."""
    e = linienzug(punkte, cue, breite=16, farbe=INK, d=d)
    return e


def blatt(cx, unten, breite, cue, fuell=ROT, **k):
    """Ahornblatt (Tabler leaf-maple), mit Palettenfarbe gefüllt."""
    return ficon("tabler", "leaf-maple", cx, unten, breite, cue, fuell=fuell, **k)


# A1 Fall: Äste über der Garage -------------------------------------------------------------------------------------------
GX0, GX1, GO = 940, 1440, 620                 # Garage: links, rechts, Wandoberkante (Dach 594–620, Rinne 620–644)
BX, BB = 520, 520                             # Ahorn: Stammmitte, Breite
GR = 860                                      # Grundstücksgrenze
FX1, RX1 = 1760, 140                          # Franziska rechts, Rosemarie links
AST = [(712, 515), (860, 530), (980, 547), (1080, 561), (1170, 574)]
folie([(NULL, "Fall · Äste über der Garage")], [
    hart(pl("Äste auf dem Garagendach", 70, 40, NULL, fill=GELB, size=44)),
    hart(pl("Nordrhein-Westfalen", 70, 130, NULL, fill=WEISS, size=30)),
    hart(boden(NULL)),
    hart(garage(GX0, GX1, GO, NULL)),
    hart(pl("Garage von Franziska", (GX0 + GX1) / 2, 760, NULL, fill=WEISS, size=30, anker="m")),
    *fig("FR", FX1, BODEN, FH, [(NULL, "ruhig"), ("leiter", "sorge")], erst="cut"),
    hart(ns("Franziska", FX1, BODEN, NULL, FR_N)),
    ficon("ph", "tree", BX, BODEN, BB, "ahorn", fuell=GRUEN),
    pl("Ahorn von Rosemarie", BX, 262, beim("ahorn", "Ahorn"), fill=GRUEN, size=30, anker="m"),
    *fig("RO", RX1, BODEN, FH, [("ahorn", "ruhig_r")], d=0.2),
    ns("Rosemarie", RX1, BODEN, "ahorn", RO_N, d=0.3),
    grenze(GR, 300, beim("ahorn", "Grenze")),
    ficon("tabler", "fence", GR, BODEN, 120, beim("ahorn", "Grenze"), fuell=HOLZ),
    linienzug([(BX, 912), (GR, 912)], beim("ahorn", "vier"), breite=4),
    pl("4 m", (BX + GR) / 2, 892, beim("ahorn", "vier"), fill=WEISS, size=28, anker="m"),
    ast(AST, "aeste"),
    *[blatt(x, y + 70, 80, "aeste", fuell=f, d=0.1 * i) for i, ((x, y), f) in enumerate(zip(AST[1:], (ROT, GELB, ROT, GELB)))],
    pl("Äste ragen über die Grenze", 1190, 330, beim("aeste", "ragen"), fill=WEISS, size=30, anker="m"),
    szene(ficon("ph", "leaf", 1030, 646, 56, "laub", fuell=GELB), "142laub*", 0.75, 0.0),
    *[ficon("ph", "leaf", x, 646, 56, "laub", fuell=f, d=0.15 * (i + 1)) for i, (x, f) in enumerate(((1150, ROT), (1270, GELB), (1380, ROT)))],
    pl("Laub verstopft die Dachrinne", 1190, 410, beim("laub", "verstopft"), fill=GELB, size=30, anker="m"),
    szene(ficon("ph", "ladder", 1545, BODEN, 230, "leiter", fuell=None), "142leiter*", 0.7, 0.05),
])

# A2 Fall: am Gartenzaun ----------------------------------------------------------------------------------------------------
RX2, FX2 = 640, 1290


def gartenzaun(cue, titel_, bis_titel=None):
    """Bühne am Gartenzaun: Ahorn links, Zaun in der Mitte, Garage rechts; Rosemarie links (blickt nach rechts),
    Franziska rechts (blickt nach links)."""
    return [pl(titel_, 70, 40, cue, fill=GELB, size=44, bis=bis_titel), boden(cue),
            ficon("ph", "tree", 270, BODEN, 430, cue, fuell=GRUEN),
            ficon("tabler", "fence", 890, BODEN, 140, cue, fuell=HOLZ), ficon("tabler", "fence", 1030, BODEN, 140, cue, fuell=HOLZ),
            garage(1520, 1850, 650, cue)]


folie([("fr1", "Fall · Am Gartenzaun"), ("frage", "Fall · Die Frage")], [
    *gartenzaun("fr1", "Am Gartenzaun", bis_titel="frage"),
    *[ficon("ph", "leaf", x, 660, 50, "fr1", fuell=f) for x, f in ((1580, ROT), (1680, GELB), (1790, ROT))],
    *redet("FR_bittet", FX2, BODEN, FH, "fr1", "ro1"),
    *fig("FR", FX2, BODEN, FH, [("ro1", "ruhig"), ("frage", "denkt")], erst="cut"),
    ns("Franziska", FX2, BODEN, "fr1", FR_N),
    *fig("RO", RX2, BODEN, FH, [("fr1", "ruhig_r")], bis="ro1", d=0.1),
    *redet("RO_meint_r", RX2, BODEN, FH, "ro1", "frage"),
    *fig("RO", RX2, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    ns("Rosemarie", RX2, BODEN, "fr1", RO_N, d=0.2),
    blase("sprech", 980, 200, "fr1", 1090, 225, inhalt=["Rosemarie, kannst du bitte die Äste", "über meiner Garage zurückschneiden?"],
          textsize=34, figur=("FR_bittet", FX2, BODEN, FH), bis="ro1"),
    blase("sprech", 860, 200, "ro1", 830, 225, inhalt=["Laub im Herbst ist ganz normal.", "Das ist hier überall so."],
          textsize=34, figur=("RO_meint_r", RX2, BODEN, FH), bis="frage"),
    pl("Kann Franziska den Rückschnitt verlangen?", 960, 40, "frage", fill=PINK, size=40, anker="m"),
    pl("Und darf sie notfalls selbst zur Astschere greifen?", 960, 130, "frage2", fill=WEISS, size=34, anker="m"),
    ficon("tabler", "scissors", 960, 420, 110, beim("frage2", "Astschere"), fuell=WEISS),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------------
def sachverhalt_142(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.34)
        els += e; y += 26
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_142("sv", [
    "Franziska wohnt in Nordrhein-Westfalen und hat neben ihrem Haus eine Garage. Im Garten ihrer Nachbarin Rosemarie "
    "steht ein großer Ahorn, 4 m von der Grenze entfernt.",
    "Seit dem letzten Sommer ragen seine Äste über die Grenze auf das Garagendach. Im Herbst fällt das Laub in die "
    "Dachrinne und verstopft sie; Franziska muss immer wieder auf die Leiter.",
    "Franziska bittet Rosemarie, die Äste zurückzuschneiden. Rosemarie lehnt ab: Laub im Herbst sei ganz normal, das sei "
    "hier überall so.",
], "Kann Franziska den Rückschnitt verlangen oder selbst schneiden?")

# C § 1004 Abs. 1 S. 1 (Wortlaut), § 903, vier Prüfungspunkte ------------------------------------------------------------------
W1004 = ["„Wird das Eigentum in anderer Weise als durch Entziehung oder",
         "Vorenthaltung des Besitzes beeinträchtigt, so kann der Eigentümer",
         "von dem Störer die Beseitigung der Beeinträchtigung verlangen.“"]
w1004, w1004_y = wortlaut(80, 180, 1100, W1004, "§ 1004 Abs. 1 Satz 1 BGB", "w1004", marken=[
    (0, "Eigentum", beim("w1004", "Eigentum")), (1, "beeinträchtigt", beim("w1004", "beeinträchtigt")),
    (2, "Störer", beim("w1004", "Störer")), (2, "Beseitigung", beim("w1004", "Beseitigung"))], size=34)
PUNKTE = [("v1", "1. Eigentum"), ("v2", "2. Beeinträchtigung"), ("v3", "3. Störer"),
          ("v4", "4. keine Duldungspflicht (§ 1004 Abs. 2 BGB)")]
folie([("p1004", "Anspruchsgrundlage · § 1004 Abs. 1 S. 1 BGB"), ("vier", "§ 1004 BGB › 4 Prüfungspunkte")], rechts_frei([
    *tafel("p1004", "Beseitigungsanspruch"),
    *w1004,
    z("§ 903 S. 1 BGB: andere von jeder Einwirkung ausschließen", 110, w1004_y + 30, "p903", "Bold", 32),
    z("4 Prüfungspunkte", 110, w1004_y + 105, "vier", "Bold", 38),
    *[z(t, 160, w1004_y + 165 + 58 * i, c, "Bold", 36) for i, (c, t) in enumerate(PUNKTE)],
    *requisit([("p1004", ("tabler", "leaf-maple", 110, ROT), "Beseitigung?", WEISS),
               ("p903", ("ph", "house", 110, WEISS), "§ 903 BGB", WEISS),
               ("vier", ("tabler", "list-check", 110, WEISS), "4 Prüfungspunkte", WEISS)]),
    *paar("p1004", "FR", [("p1004", "ruhig"), ("v1", "froh")], "RO", [("p1004", "ruhig"), ("v3", "denkt")]),
]))

# D1 1. Eigentum, 2. Beeinträchtigung --------------------------------------------------------------------------------------------
folie([("eig", "I. › 1. Eigentum"), ("beein", "I. › 2. Beeinträchtigung")], rechts_frei([
    *tafel("eig", "Eigentum und Beeinträchtigung"),
    z("1. Eigentum", 110, 190, "eig", "Bold", 38),
    *okz("Franziska ist Eigentümerin des Grundstücks", 250, beim("eig", "Eigentümerin")),
    z("2. Beeinträchtigung", 110, 345, "beein", "Bold", 38),
    z("nicht durch Entziehung des Besitzes", 160, 405, beim("beein", "nicht"), size=34),
    zit("dafür: § 985 BGB (Herausgabeanspruch)", 160, 458, beim("beein", "Paragraf"), size=28),
    z("fremde Äste über dem Garagendach,", 160, 525, "aeste2", size=34),
    z("ihr Laub verstopft die Rinne", 160, 577, beim("aeste2", "Laub"), size=34),
    *okz("Beeinträchtigung liegt vor", 655, "beein2", "Bold", 36),
    *requisit([("eig", ("ph", "garage", 130, GELB), "Eigentümerin", GRUEN),
               ("beein", ("tabler", "hand-stop", 100, WEISS), "nicht Entziehung", WEISS),
               ("aeste2", ("tabler", "leaf-maple", 110, ROT), "Äste und Laub", GELB),
               ("beein2", ("tabler", "droplet", 90, BLAU), "Beeinträchtigung", HELLROT)]),
    *paar("eig", "FR", [("eig", "ruhig"), (beim("eig", "Eigentümerin"), "froh"), ("aeste2", "sorge")],
          "RO", [("eig", "ruhig")]),
]))

# D2 3. Störerin --------------------------------------------------------------------------------------------------------------------
folie([("stoer", "I. › 3. Störer"), ("zust", "I. › 3. Störer › Zustandsstörerin"),
       ("natur", "I. › 3. Störer › Naturereignis")], rechts_frei([
    *tafel("stoer", "3. Ist Rosemarie Störerin?"),
    z("Handlungsstörer: verursacht durch Verhalten", 110, 190, "hand", "Bold", 34),
    *neinz("Das ist Rosemarie nicht", 245, beim("hand", "Das")),
    z("Zustandsstörer: Störung geht von der Sache aus", 110, 325, "zust", "Bold", 34),
    z("hier: von ihrem Baum", 160, 380, beim("zust", "denn"), size=34),
    z("Naturereignis: Eigentum am Baum allein genügt nicht", 110, 460, "natur", "Bold", 34),
    z("entscheidend: ordnungsgemäße Bewirtschaftung?", 160, 515, beim("natur", "Entscheidend"), size=34),
    zit("BGH, Urt. v. 20.9.2019 – V ZR 218/18, Rn. 8 f.", 160, 567, beim("natur", "Bundesgerichtshof")),
    *neinz("Äste über die Grenze wachsen lassen", 625, "grenze", "Bold", 34),
    zit("BGH, Urt. v. 14.6.2019 – V ZR 102/18, Rn. 9, 12", 160, 680, beim("grenze", "tut")),
    blk(110, 740, 1040, 96, GRUEN, "stoer2", [("Rosemarie ist Störerin", "ExtraBold", 40, INK)]),
    *requisit([("stoer", ("ph", "tree", 130, GRUEN), "Störerin?", WEISS),
               ("hand", ("tabler", "hand-stop", 100, WEISS), "Verhalten?", WEISS),
               ("zust", ("ph", "tree", 130, GRUEN), "ihr Baum", GRUEN),
               ("natur", ("ph", "wind", 120, WEISS), "Naturereignis", WEISS),
               ("grenze", ("tabler", "fence", 120, HOLZ), "über die Grenze", HELLROT),
               ("stoer2", ("tabler", "leaf-maple", 110, ROT), "Störerin", GRUEN)]),
    *paar("stoer", "FR", [("stoer", "ruhig"), ("stoer2", "froh")],
          "RO", [("stoer", "ruhig"), ("zust", "denkt"), ("grenze", "sorge")]),
]))

# D3 Gegenfall: Laub vom Baum selbst --------------------------------------------------------------------------------------------
folie([("gegen", "I. › 3. Störer › Gegenfall: Laub vom Baum"), ("ausgl", "Gegenfall › § 906 Abs. 2 S. 2 BGB analog")],
      rechts_frei([
    *tafel("gegen", "Gegenfall: Laub vom Baum selbst"),
    z("Laub, das der Wind herüberweht", 110, 190, "gegen", "Bold", 36),
    z("Grenzabstand des Nachbarrechtsgesetzes eingehalten?", 110, 270, "abstand", size=34),
    *okz("eingehalten: § 41 Abs. 1 NachbG NRW", 330, beim("abstand", "Paragraf"), "Bold", 34),
    zit("in deinem Land ggf. andere Nummer und andere Abstände", 160, 385, beim("abstand", "Paragraf"), size=28),
    *neinz("in aller Regel nicht verantwortlich", 450, beim("abstand", "verantwortlich"), "Bold", 34),
    zit("BGH, Urt. v. 20.9.2019 – V ZR 218/18, Leitsatz 1a, Rn. 13, 15", 160, 505, beim("abstand", "verantwortlich")),
    linienzug([(110, 575), (1150, 575)], "ausgl", breite=3),
    *neinz("kein Geldausgleich analog § 906 Abs. 2 S. 2 BGB", 605, "ausgl", "Bold", 34),
    zit("BGH, Urt. v. 20.9.2019 – V ZR 218/18, Leitsatz 2, Rn. 29 f.", 160, 660, beim("ausgl", "scheidet")),
    *requisit([("gegen", ("ph", "wind", 120, WEISS), "Laub vom Baum", GELB),
               ("abstand", ("tabler", "ruler-measure", 110, WEISS), "Grenzabstand", WEISS),
               ("ausgl", ("tabler", "coin-euro", 100, GELB), "Geldausgleich?", WEISS)]),
    *paar("gegen", "FR", [("gegen", "ruhig"), ("ausgl", "denkt")],
          "RO", [("gegen", "ruhig"), (beim("abstand", "verantwortlich"), "froh")]),
]))

# E 4. keine Duldungspflicht: § 910 Abs. 2 statt § 906 ----------------------------------------------------------------------------
folie([("duld", "I. › 4. keine Duldungspflicht, § 1004 Abs. 2 BGB"), ("nur910", "I. › 4. › Überhang: § 910 Abs. 2 BGB")],
      rechts_frei([
    *tafel("duld", "4. Keine Duldungspflicht"),
    z("§ 1004 Abs. 2 BGB: Muss Franziska dulden?", 110, 185, "duld", "Bold", 36),
    z("Rosemarie: „Laub im Herbst ist ganz normal.“", 160, 245, "orts", size=34),
    z("§ 906 BGB, ortsübliche Einwirkungen?", 160, 300, beim("orts", "Paragraf"), size=34),
    nein(115, 320, "nur910", gr=20),
    *okz("Überhang: allein § 910 Abs. 2 BGB", 365, "nur910", "Bold", 36),
    z("auch beim Laubfall; Ortsüblichkeit spielt keine Rolle", 160, 420, beim("nur910", "Ortsüblichkeit"), size=32),
    zit("BGH, Urt. v. 14.6.2019 – V ZR 102/18, Leitsatz, Rn. 8", 160, 470, beim("nur910", "auch")),
    z("Dulden nur, wenn die Benutzung nicht beeinträchtigt ist", 110, 530, "w910b", "Bold", 32),
    z("objektiv beurteilt; Beweislast: Baumeigentümerin", 160, 585, "obj", size=32),
    zit("BGH, Urt. v. 11.6.2021 – V ZR 234/19, Rn. 15", 160, 635, beim("obj", "beweisen")),
    *okz("verstopfte Dachrinne: Benutzung beeinträchtigt", 690, "rinne", "Bold", 32),
    *neinz("Grenzabstand hilft beim Überhang nicht", 760, "lnr", "Bold", 32),
    zit("vgl. BGH V ZR 218/18, Rn. 18 f.; V ZR 234/19, Rn. 9", 160, 812, beim("lnr", "Überhang")),
    *requisit([("duld", ("ph", "scales", 120, WEISS), "dulden?", WEISS),
               ("orts", ("tabler", "leaf-maple", 110, GELB), "ortsüblich?", WEISS),
               ("nur910", ("tabler", "fence", 120, HOLZ), "§ 910 Abs. 2 BGB", BLAU),
               ("rinne", ("tabler", "droplet", 90, BLAU), "Rinne verstopft", HELLROT),
               ("lnr", ("tabler", "ruler-measure", 110, WEISS), "Grenzabstand", WEISS)]),
    *paar("duld", "FR", [("duld", "ruhig"), ("rinne", "froh")],
          "RO", [("duld", "ruhig"), ("orts", "denkt"), ("nur910", "sorge")]),
]))

# F Verjährung und Zwischenergebnis -----------------------------------------------------------------------------------------------
folie([("verj", "I. › Verjährung, §§ 195, 199 BGB"), ("erg1", "I. › Zwischenergebnis")], rechts_frei([
    *tafel("verj", "Verjährung?"),
    z("Frist: 3 Jahre (§§ 195, 199 Abs. 1 BGB)", 110, 195, "verj", "Bold", 36),
    zit("BGH, Urt. v. 14.6.2019 – V ZR 102/18, Rn. 17; Urt. v. 22.2.2019 – V ZR 136/18, Rn. 12, 15", 110, 250,
        beim("verj", "drei")),
    *okz("Äste erst seit dem letzten Sommer: nicht verjährt", 320, beim("verj", "Äste"), "Bold", 34),
    blk(110, 430, 1040, 150, GRUEN, "erg1", [("Franziska kann verlangen,", "ExtraBold", 38, INK),
                                            ("dass Rosemarie den Überhang beseitigt", "ExtraBold", 38, INK)]),
    *requisit([("verj", ("tabler", "hourglass", 90, WEISS), "3 Jahre", WEISS),
               ("erg1", ("tabler", "scissors", 110, WEISS), "Überhang beseitigen", GRUEN)]),
    *paar("verj", "FR", [("verj", "ruhig"), ("erg1", "froh")], "RO", [("verj", "ruhig")]),
]))

# G II. Selbsthilferecht, Wortlaut § 910 --------------------------------------------------------------------------------------------
W910 = ["„(1) Der Eigentümer eines Grundstücks kann Wurzeln eines Baumes",
        "oder eines Strauches, die von einem Nachbargrundstück eingedrungen",
        "sind, abschneiden und behalten. Das Gleiche gilt von herüberragenden",
        "Zweigen, wenn der Eigentümer dem Besitzer des Nachbargrundstücks",
        "eine angemessene Frist zur Beseitigung bestimmt hat und die",
        "Beseitigung nicht innerhalb der Frist erfolgt.",
        "(2) Dem Eigentümer steht dieses Recht nicht zu, wenn die Wurzeln",
        "oder die Zweige die Benutzung des Grundstücks nicht beeinträchtigen.“"]
w910, w910_y = wortlaut(80, 180, 1100, W910, "§ 910 BGB", "w910", marken=[
    (2, "herüberragenden", beim("w910", "Herüberragende")), (2, "abschneiden und behalten", beim("w910", "abschneiden")),
    (4, "angemessene Frist", beim("w910", "angemessene")), (5, "nicht innerhalb der Frist", beim("w910", "nicht")),
    (7, "nicht beeinträchtigen", beim("w910c", "beeinträchtigen"))], size=30)
folie([("sh", "II. Selbsthilferecht · § 910 BGB")], rechts_frei([
    *tafel("sh", "II. Selbsthilferecht"),
    *w910,
    *requisit([("sh", ("tabler", "scissors", 110, WEISS), "Selbsthilfe", WEISS),
               (beim("w910", "angemessene"), ("tabler", "calendar-event", 100, WEISS), "angemessene Frist", GELB),
               ("w910c", ("tabler", "droplet", 90, BLAU), "Benutzung beeinträchtigt?", WEISS)]),
    *paar("sh", "FR", [("sh", "ruhig"), (beim("w910", "abschneiden"), "froh")],
          "RO", [("sh", "ruhig"), ("w910c", "denkt")]),
]))

# H Verhältnis zu § 1004, Grenzen, Kosten ---------------------------------------------------------------------------------------------
folie([("neben", "II. › Verhältnis zu § 1004 BGB"), ("schutz", "II. › Grenzen der Selbsthilfe"),
       ("kosten", "II. › Kosten der Selbsthilfe")], rechts_frei([
    *tafel("neben", "§ 910 BGB neben § 1004 BGB"),
    *okz("gleichrangig nebeneinander", 190, "neben", "Bold", 36),
    zit("BGH, Urt. v. 14.6.2019 – V ZR 102/18, Rn. 5", 160, 245, beim("neben", "nebeneinander")),
    z("Selbsthilferecht: kein Anspruch, verjährt nicht", 110, 305, "nverj", "Bold", 34),
    zit("BGH, Urt. v. 11.6.2021 – V ZR 234/19, Rn. 10", 160, 357, beim("nverj", "verjährt")),
    *neinz("nur die Zweige abschneiden, nicht den Baum fällen", 420, "nurzw", "Bold", 34),
    zit("BGH V ZR 234/19, Rn. 9", 160, 475, beim("nurzw", "nicht")),
    z("Grenze: öffentliches Naturschutzrecht,", 110, 540, "schutz", "Bold", 34),
    z("etwa eine Baumschutzsatzung der Gemeinde", 160, 595, beim("schutz", "Baumschutzsatzung"), size=34),
    zit("BGH V ZR 102/18, Rn. 14 f.; V ZR 234/19, Rn. 29", 160, 647, beim("schutz", "Baumschutzsatzung")),
    z("Schneidet Franziska selbst: erforderliche Kosten", 110, 710, "kosten", "Bold", 34),
    z("von Rosemarie, die zur Beseitigung verpflichtet war", 160, 765, beim("kosten", "Rosemarie"), size=34),
    zit("GoA oder Bereicherungsrecht; vgl. BGH, Urt. v. 23.3.2023 – V ZR 67/22, Rn. 10", 160, 817,
        beim("kosten", "verpflichtet")),
    *requisit([("neben", ("tabler", "arrows-exchange", 110, WEISS), "nebeneinander", GRUEN),
               ("nverj", ("tabler", "hourglass-off", 90, WEISS), "verjährt nicht", WEISS),
               ("nurzw", ("tabler", "scissors", 110, WEISS), "nur die Zweige", WEISS),
               ("schutz", ("ph", "tree", 130, GRUEN), "Baumschutzsatzung", WEISS),
               ("kosten", ("tabler", "coin-euro", 100, GELB), "Kosten", GELB)]),
    *paar("neben", "FR", [("neben", "ruhig"), ("nverj", "froh"), ("schutz", "denkt"), ("kosten", "froh")],
          "RO", [("neben", "ruhig"), ("kosten", "sorge")]),
]))

# I III. Unterlassungsanspruch -----------------------------------------------------------------------------------------------------
folie([("unt", "III. Unterlassungsanspruch · § 1004 Abs. 1 S. 2 BGB")], rechts_frei([
    *tafel("unt", "III. Unterlassungsanspruch"),
    z("Äste wachsen wieder hinüber?", 110, 195, "unt", "Bold", 38),
    z("§ 1004 Abs. 1 S. 2 BGB: weitere Beeinträchtigungen", 110, 275, "unt2", "Bold", 34),
    z("zu besorgen: Klage auf Unterlassung", 160, 330, beim("unt2", "Unterlassung"), size=34),
    *okz("Wiederholungsgefahr: nach einer Störung meist indiziert", 410, "wgef", size=32),
    zit("vgl. BGH, Urt. v. 11.6.2021 – V ZR 234/19, Rn. 6", 160, 465, beim("wgef", "indiziert")),
    *requisit([("unt", ("ph", "tree", 130, GRUEN), "wächst nach", WEISS),
               ("unt2", ("tabler", "hand-stop", 100, WEISS), "Unterlassung", WEISS),
               ("wgef", ("tabler", "repeat", 100, WEISS), "Wiederholungsgefahr", GELB)]),
    *paar("unt", "FR", [("unt", "denkt"), ("unt2", "ruhig")], "RO", [("unt", "ruhig")]),
]))

# J Ergebnis am Gartenzaun: Fristsetzung ---------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · § 1004 Abs. 1 S. 1 BGB"), ("frist", "Ergebnis › Fristsetzung, § 910 Abs. 1 S. 2 BGB")], [
    *gartenzaun("erg", "Ergebnis"),
    pl("Äste zurückschneiden: § 1004 BGB", 1110, 40, beim("erg", "Paragraf"), fill=GRUEN, size=36, anker="m", bis="fr2"),
    ficon("tabler", "calendar-event", 960, 600, 110, "frist", fuell=WEISS),
    pl("Frist", 960, 625, "frist", fill=GELB, size=30, anker="m", bis=beim("fr2", "vier")),
    pl("Frist: 4 Wochen", 960, 625, beim("fr2", "vier"), fill=GELB, size=30, anker="m", anim="cut"),
    *fig("FR", FX2, BODEN, FH, [("erg", "ruhig")], bis="fr2"),
    *redet("FR_bittet", FX2, BODEN, FH, "fr2", "ro2"),
    *fig("FR", FX2, BODEN, FH, [("ro2", "ruhig"), (beim("ro2", "kümmere"), "froh")], erst="cut"),
    ns("Franziska", FX2, BODEN, "erg", FR_N),
    *fig("RO", RX2, BODEN, FH, [("erg", "ruhig_r")], bis="ro2", d=0.1),
    *redet("RO_redet_r", RX2, BODEN, FH, "ro2", "schnitt"),
    *fig("RO", RX2, BODEN, FH, [("schnitt", "froh_r")], erst="cut"),
    ns("Rosemarie", RX2, BODEN, "erg", RO_N, d=0.2),
    blase("sprech", 900, 200, "fr2", 1080, 225, inhalt=["Bitte schneide die Äste in den", "nächsten 4 Wochen zurück."],
          textsize=34, figur=("FR_bittet", FX2, BODEN, FH), bis="ro2"),
    blase("sprech", 640, 200, "ro2", 820, 225, inhalt=["Gut, ich kümmere", "mich darum."],
          textsize=34, figur=("RO_redet_r", RX2, BODEN, FH), bis="schnitt"),
    ficon("tabler", "scissors", 960, 430, 110, "schnitt", fuell=WEISS),
    pl("Sonst: nach Fristablauf selbst abschneiden", 960, 130, beim("schnitt", "darf"), fill=WEISS, size=34, anker="m"),
    pl("§ 910 BGB", 960, 210, beim("schnitt", "Grenze"), fill=BLAU, size=30, anker="m"),
])

# K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Duldung beim Überhang")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Überhängende Äste: Duldungspflicht prüfen", 200, 200, beim("tipp", "überhängenden"), "Bold", 36),
    *neinz("nicht an § 906 BGB", 270, beim("tipp", "nicht"), size=34, x=245),
    *okz("sondern an § 910 Abs. 2 BGB", 330, beim("tipp", "sondern"), "Bold", 34, x=245),
    *neinz("mit Ortsüblichkeit argumentieren", 440, "tipp2", size=34, x=245),
    z("Damit verschenkst du Punkte", 245, 495, beim("tipp2", "verschenkt"), size=34),
    z("Beide Wege nennen: Anspruch und Selbsthilfe", 200, 590, "tipp3", "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# L Klausurschema --------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Selbsthilferecht"), ("k3", "Klausurschema › III. Unterlassung")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Äste über der Grenze"), 110, 90, "sch", 46),
    z("I. Beseitigungsanspruch, § 1004 Abs. 1 S. 1 BGB", K1, 195, "k1", "Bold", 40, rechts=1820),
    z("1. Eigentum", K2, 252, "k11", size=36, rechts=1820),
    z("2. Beeinträchtigung, nicht durch Besitzentziehung", K2, 302, "k12", size=36, rechts=1820),
    z("3. Störer: Handlungs- oder Zustandsstörer", K2, 352, "k13", size=36, rechts=1820),
    z("4. keine Duldungspflicht, § 1004 Abs. 2 BGB; beim Überhang § 910 Abs. 2 BGB", K2, 402, "k14", size=36, rechts=1820),
    z("II. Selbsthilferecht, § 910 BGB", K1, 480, "k2", "Bold", 40, rechts=1820),
    z("Frist erfolglos abgelaufen", K2, 537, "k2b", size=36, rechts=1820),
    z("Benutzung beeinträchtigt (§ 910 Abs. 2 BGB)", K2, 587, "k2c", size=36, rechts=1820),
    z("III. Unterlassungsanspruch, § 1004 Abs. 1 S. 2 BGB", K1, 665, "k3", "Bold", 40, rechts=1820),
    z("Wiederholungsgefahr", K2, 722, "k3b", size=36, rechts=1820),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Was über die Grenze wächst, muss der", 0)], [("Baumeigentümer auf Verlangen ", 0),
                 ("zurückschneiden.", "a")]], 750, 320, 44, "merke", {"a": beim("merke", "zurückschneiden")}),
    *markertext([[("Es sei denn, die Zweige beeinträchtigen", 0)], [("die Benutzung des Nachbargrundstücks ", 0),
                 ("nicht.", "b")]], 750, 590, 44, "m2", {"b": beim("m2", "nicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
