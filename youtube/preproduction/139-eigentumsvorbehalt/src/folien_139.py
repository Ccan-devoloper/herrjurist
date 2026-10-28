"""Folge 139 · Eigentumsvorbehalt: Das Sofa ist da, gehört aber dem Möbelhaus – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Sonja kauft im Möbelhaus (Verkäufer Herr Schuster) ein Sofa für 2.400 €, 12 Raten zu je 200 €, mit
Eigentumsvorbehalt; Lieferung; nach 5 Raten (1.000 €) keine Zahlung mehr; Herr Schuster kündigt telefonisch die Abholung an.
Szenen laut ../SZENENPLAN.md: A1 Im Möbelhaus, A2 Das Sofa im Wohnzimmer, A3 Der Anruf / Frage, B Sachverhalt, C Aufbau,
D 1. Trennungsprinzip, E § 449 Abs. 1 (Wortlaut), F § 158 Abs. 1 (Wortlaut) mit Ratenleiste, G 2. Anwartschaftsrecht,
H 3. Herausgabe § 985 (Wortlaut) / § 986 Abs. 1, I § 449 Abs. 2 (Wortlaut), J Rücktritt, Teilzahlungsgeschäft,
Rückabwicklung, K Ergebnis (Wohnzimmer), L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Handlungsgeräusch: Telefonklingeln beim Anruf (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz/punkt als eigene Kopie aus Folge 116 (gemeinsame Dateien unverändert); neu: raumbild(), ratenleiste().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_139/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_139/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



def tisch(cx, unten, cue, w=420, h=250, fill=GELB):
    """Schreibtisch/Ladentheke in Seitenansicht (programmatisch: Platte, zwei Beine; Palettenfläche, Tuschekontur)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")


def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")


# --- Zeitstrahl nach Tagen (1.7. bis 30.9.2026) -----------------------------------------------------------------------------




BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
SO_N, SC_N = ROT, BLAU                      # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SO": "Sonja", "SC": "Herr Schuster"}
NFARBE = {"SO": SO_N, "SC": SC_N}
SOFA = BLAU                                 # Sofa durchgehend blau


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel SO/SC."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


def wohnzimmer(cue, sx, hart_=False, breite=520, x0=40, x1=1880, lampe=None, pflanze=True):
    """Sonjas Wohnzimmer: blaues Sofa (Tabler sofa), Stehlampe, Pflanze, Bild an der Wand."""
    lx = lampe if lampe is not None else sx - breite / 2 - 90
    els = [boden(cue, x0=x0, x1=x1), ficon("tabler", "sofa", sx, BODEN, breite, cue, fuell=SOFA),
           ficon("tabler", "lamp", lx, BODEN, 150, cue, fuell=GELB),
           ficon("tabler", "photo", sx, 470, 130, cue, fuell=WEISS)]
    if lampe is False:
        els.pop(2)
    if pflanze:
        els.insert(len(els) - 1, ficon("tabler", "plant-2", sx + breite / 2 + 70, BODEN, 120, cue, fuell=GRUEN))
    return [hart(e) for e in els] if hart_ else [e if i == 0 else hart(e) for i, e in enumerate(els)]


# ===========================================================================================================================
# A1 Fall: im Möbelhaus
# ===========================================================================================================================
SOX, SCX = 1060, 1560                       # Sonja (blickt nach rechts), Herr Schuster (blickt nach links)
MX = 470                                    # Ausstellungssofa
KL = beim("klausel", "Satz")
folie([(NULL, "Fall · Im Möbelhaus"), ("klausel", "Fall · Der Kaufvertrag")], [
    boden(NULL, hart_=True),
    hart(ficon("tabler", "sofa", MX, BODEN, 520, NULL, fuell=SOFA)),
    hart(ficon("tabler", "lamp", MX + 330, BODEN, 150, NULL, fuell=GELB)),
    ficon("tabler", "tag", MX, 520, 90, beim("fall", "Sofa"), fuell=GELB),
    pl("Sofa: 2.400 €", 70, 30, beim("fall", "Sofa"), fill=GELB, size=44),
    pl("12 Monatsraten zu je 200 €", 70, 120, beim("raten", "zwölf"), fill=WEISS, size=36),
    ficon("tabler", "calendar-dollar", 660, 210, 90, beim("raten", "zwölf"), fuell=WEISS),
    pl("Kaufvertrag", 70, 205, KL, fill=WEISS, size=36),
    ficon("tabler", "contract", 370, 290, 90, KL, fuell=WEISS),
    *fig("SO", SOX, BODEN, FH, [(NULL, "ruhig_r"), (beim("raten", "zwölf"), "laechelt_r"), ("sc1", "denkt_r")], erst="cut"),
    hart(ns("Sonja", SOX, BODEN, NULL, SO_N)),
    *fig("SC", SCX, BODEN, FH, [(beim("klausel", "Verkäufer"), "froh")], bis="sc1"),
    ns("Herr Schuster", SCX, BODEN, beim("klausel", "Verkäufer"), SC_N, d=0.1),
    *redet("SC_redet", SCX, BODEN, FH, "sc1", "liefer"),
    blase("sprech", 900, 200, "sc1", 1170, 200, inhalt=["Bis zur letzten Rate bleibt das Sofa", "Eigentum des Möbelhauses."],
          textsize=34, figur=("SC_redet", SCX, BODEN, FH), bis="liefer"),
])

# ===========================================================================================================================
# A2 Fall: das Sofa im Wohnzimmer
# ===========================================================================================================================
WX = 600                                    # Sofa im Wohnzimmer
SO2 = 1350                                  # Sonja rechts, blickt nach links zum Sofa
GEL = beim("liefer", "geliefert")
folie([("liefer", "Fall · Die Lieferung")], [
    *wohnzimmer("liefer", WX),
    ficon("tabler", "truck-delivery", 1650, 300, 170, GEL, fuell=WEISS, bis="so1"),
    pl("geliefert", 70, 30, GEL, fill=GRUEN, size=44),
    pl("Wohnzimmer", 70, 120, beim("liefer", "Wohnzimmer"), fill=WEISS, size=36),
    *fig("SO", SO2, BODEN, FH, [("liefer", "ruhig"), (beim("liefer", "steht"), "staunt")], bis="so1"),
    ns("Sonja", SO2, BODEN, "liefer", SO_N, d=0.1),
    *redet("SO_redet", SO2, BODEN, FH, "so1", "fuenf"),
    blase("sprech", 640, 170, "so1", 1300, 200, inhalt=["Endlich ein eigenes Sofa!"], textsize=38,
          figur=("SO_redet", SO2, BODEN, FH), bis="fuenf"),
])

# ===========================================================================================================================
# A3 Fall: Raten bleiben aus, der Anruf, Frage (geteilte Bühne: Möbelhaus links, Wohnzimmer rechts)
# ===========================================================================================================================
SCL, SOR, WR = 470, 1640, 1250              # Herr Schuster links (blickt nach rechts), Sonja rechts, Sofa rechts
RUF = beim("anruf", "ruft")
folie([("fuenf", "Fall · Die Raten"), ("anruf", "Fall · Der Anruf"), ("frage", "Fall · Die Frage")], [
    boden("fuenf", x0=40, x1=900), linienzug([(960, 300), (960, 1000)], "fuenf", breite=5, farbe=TEXT),
    *wohnzimmer("fuenf", WR, breite=400, x0=1020, x1=1880, lampe=False, pflanze=False),
    pl("5 Raten gezahlt: 1.000 €", 70, 30, beim("fuenf", "Fünf"), fill=GRUEN, size=40, bis="sc2"),
    pl("dann: keine Zahlung mehr", 70, 120, beim("stopp", "zahlt"), fill=ROT, size=36, bis="sc2"),
    ficon("tabler", "calendar-x", 720, 250, 100, beim("stopp", "zahlt"), fuell=WEISS, bis="sc2"),
    ficon("tabler", "coins", 450, 700, 150, beim("fuenf", "tausend"), fuell=GELB, bis=RUF),
    hart(ficon("tabler", "building-store", 170, BODEN, 200, "anruf", fuell=GELB)),
    szene(ficon("tabler", "phone-ringing", 730, 560, 110, RUF, fuell=WEISS), "139telefon*", 0.6, 0.0),
    ficon("tabler", "phone-call", 1450, 470, 90, RUF, fuell=WEISS),
    *fig("SC", SCL, BODEN, FH, [(RUF, "ernst_r")], bis="sc2"),
    ns("Herr Schuster", SCL, BODEN, RUF, SC_N, d=0.1),
    *redet("SC_streng_r", SCL, BODEN, FH, "sc2", "so2"),
    *fig("SC", SCL, BODEN, FH, [("so2", "ernst_r"), ("frage", "denkt_r")], erst="cut"),
    blase("sprech", 820, 210, "sc2", 560, 200, inhalt=["Das Sofa gehört noch uns.", "Wir holen es am Montag ab."], textsize=34,
          figur=("SC_streng_r", SCL, BODEN, FH), bis="so2"),
    *fig("SO", SOR, BODEN, FH, [("fuenf", "froh"), (beim("stopp", "zahlt"), "sorge"), ("sc2", "staunt")], bis="so2"),
    ns("Sonja", SOR, BODEN, "fuenf", SO_N, d=0.1),
    *redet("SO_empoert", SOR, BODEN, FH, "so2", "frage"),
    blase("sprech", 760, 200, "so2", 1400, 200, inhalt=["Aber ich habe das Sofa", "doch gekauft!"], textsize=36,
          figur=("SO_empoert", SOR, BODEN, FH), bis="frage"),
    *fig("SO", SOR, BODEN, FH, [("frage", "denkt"), ("frage2", "sorge")], erst="cut"),
    pl("Wer ist Eigentümer des Sofas?", 70, 30, "frage", fill=PINK, size=38),
    pl("Darf das Möbelhaus es einfach abholen?", 70, 120, "frage2", fill=WEISS, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_139(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_139("sv", [
    "Sonja kauft in einem Möbelhaus beim Verkäufer Herrn Schuster ein Sofa für 2.400 Euro, zahlbar in 12 Monatsraten zu "
    "je 200 Euro. Im Kaufvertrag steht: „Bis zur letzten Rate bleibt das Sofa Eigentum des Möbelhauses.“",
    "Das Sofa wird geliefert und steht in Sonjas Wohnzimmer. Sonja zahlt fünf Raten pünktlich, zusammen 1.000 Euro. "
    "Danach zahlt sie nicht mehr.",
    "Herr Schuster ruft an: Das Sofa gehöre noch dem Möbelhaus, man werde es am Montag abholen. Eine Frist zur Zahlung "
    "hat das Möbelhaus Sonja nicht gesetzt.",
], "Wer ist Eigentümer des Sofas – und darf das Möbelhaus es einfach abholen?")

# ===========================================================================================================================
# C Aufbau: drei Schritte
# ===========================================================================================================================
SCHRITTE = [("s1", "1.", "Konstruktion des Eigentumsvorbehalts", BLAU), ("s2", "2.", "Rechtsposition von Sonja", GELB),
            ("s3", "3.", "Herausgabe des Sofas?", GRUEN)]
folie([("plan", "Eigentumsvorbehalt › Aufbau")], rechts_frei([
    *tafel("plan", "Eigentumsvorbehalt: drei Schritte"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 220 + k * 150, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 240 + k * 150, c, "ExtraBold", 40),
        z(t, 280, 240 + k * 150, c, "Bold", 40))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "3 Schritte", WEISS),
               ("s1", ("tabler", "link", 100, WEISS), "Konstruktion", BLAU),
               ("s2", ("tabler", "key", 100, GELB), "Rechtsposition", GELB),
               ("s3", ("tabler", "sofa", 140, SOFA), "Herausgabe?", GRUEN)]),
    *paar("plan", "SO", [("plan", "ruhig"), ("s2", "laechelt")], "SC", [("plan", "ruhig"), ("s3", "denkt")]),
]))

# ===========================================================================================================================
# D 1. Trennungsprinzip
# ===========================================================================================================================
folie([("tr1", "1. Trennungsprinzip"), ("kv", "1. Trennungsprinzip › Kaufvertrag, § 433 BGB"),
       ("ueb", "1. Trennungsprinzip › Übereignung, § 929 S. 1 BGB")], rechts_frei([
    *tafel("tr1", "1. Trennungsprinzip"),
    z("zwei verschiedene Geschäfte", 110, 180, beim("tr1", "zwei"), "Bold", 36),
    karte(110, 250, 1040, 250, "kv", fill=HELLGRUEN, rund=18, schatten=5, rand=4),
    z("Kaufvertrag, § 433 BGB: unbedingt", 140, 270, "kv", "ExtraBold", 36),
    *okz("Möbelhaus: liefern und übereignen", 335, beim("kv", "liefern"), size=34, x=190),
    *okz("Sonja: zahlen", 395, beim("kv", "zahlen"), size=34, x=190),
    zit("§ 433 Abs. 1 Satz 1, Abs. 2 BGB", 190, 450, beim("kv", "zahlen")),
    karte(110, 530, 1040, 330, "ueb", fill=HELL, rund=18, schatten=5, rand=4),
    z("Übereignung, § 929 S. 1 BGB:", 140, 550, "ueb", "ExtraBold", 36),
    z("aufschiebend bedingt", 140, 600, beim("ueb", "aufschiebenden"), "ExtraBold", 36, farbe=(200, 60, 45, 255)),
    *okz("Einigung und Übergabe: mit der Lieferung", 670, beim("ueb2", "Einigung"), size=34, x=190),
    *neinz("Wirkung: noch nicht eingetreten", 730, beim("ueb2", "Wirkung"), size=34, x=190),
    zit("vgl. BGH, Urt. v. 8.5.2014 – IX ZR 128/12, Rn. 10", 190, 790, beim("ueb2", "Wirkung")),
    *requisit([("tr1", ("tabler", "link", 100, WEISS), "Trennungsprinzip", WEISS),
               (beim("tr1", "zwei"), ("tabler", "arrows-split-2", 100, WEISS), "zwei Geschäfte", WEISS),
               ("kv", ("tabler", "contract", 100, WEISS), "Kaufvertrag", GRUEN),
               ("ueb", ("tabler", "sofa", 140, SOFA), "Übereignung", WEISS),
               (beim("ueb", "aufschiebenden"), ("tabler", "lock", 100, GELB), "aufschiebend bedingt", GELB),
               (beim("ueb2", "Einigung"), ("tabler", "truck-delivery", 120, WEISS), "geliefert", WEISS)]),
    *paar("tr1", "SO", [("tr1", "ruhig"), ("kv", "laechelt"), ("ueb", "denkt")], "SC", [("tr1", "ruhig"), ("kv", "froh"),
                                                                                       ("ueb2", "ruhig")]),
]))

# ===========================================================================================================================
# E § 449 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W449 = ["„(1) Hat sich der Verkäufer einer beweglichen Sache das",
        "Eigentum bis zur Zahlung des Kaufpreises vorbehalten, so",
        "ist im Zweifel anzunehmen, dass das Eigentum unter der",
        "aufschiebenden Bedingung vollständiger Zahlung des",
        "Kaufpreises übertragen wird (Eigentumsvorbehalt).“"]
w449, w449_y = wortlaut(80, 190, 1100, W449, "§ 449 Abs. 1 BGB", beim("w449", "Paragraf"), marken=[
    (1, "Eigentum bis zur Zahlung des Kaufpreises vorbehalten", beim("w449", "Eigentum")),
    (2, "im Zweifel", beim("w449", "Zweifel")),
    (3, "aufschiebenden Bedingung vollständiger Zahlung", beim("w449", "aufschiebenden"))], size=33)
folie([("w449", "1. Konstruktion › § 449 Abs. 1 BGB")], rechts_frei([
    *tafel("w449", "Der Eigentumsvorbehalt"),
    *w449,
    blk(110, w449_y + 50, 1040, 80, GELB, beim("w449", "übertragen"), [("Übereignung unter aufschiebender Bedingung", "ExtraBold", 34, INK)]),
    *requisit([("w449", ("tabler", "contract", 100, WEISS), "§ 449 Abs. 1", WEISS),
               (beim("w449", "aufschiebenden"), ("tabler", "lock", 100, GELB), "vollständige Zahlung", GELB)]),
    *paar("w449", "SO", [("w449", "ruhig"), (beim("w449", "aufschiebenden"), "denkt")], "SC",
          [("w449", "ruhig"), (beim("w449", "vorbehalten"), "froh")]),
]))

# ===========================================================================================================================
# F § 158 Abs. 1 (Wortlaut), Bedingung, Ratenleiste
# ===========================================================================================================================
W158 = ["„(1) Wird ein Rechtsgeschäft unter einer aufschiebenden",
        "Bedingung vorgenommen, so tritt die von der Bedingung",
        "abhängig gemachte Wirkung mit dem Eintritt der",
        "Bedingung ein.“"]
w158, w158_y = wortlaut(80, 180, 1100, W158, "§ 158 Abs. 1 BGB", beim("w158", "Paragraf"), marken=[
    (0, "aufschiebenden", beim("w158", "aufschiebenden")),
    (2, "mit dem Eintritt der", beim("w158", "Eintritt"))], size=33)
RY = w158_y + 120                                    # Ratenleiste: 12 Raten zu 200 €
RX0, RW = 120, 84


def ratenleiste(cue, gezahlt_cue):
    els = [z("12 Raten zu je 200 €", 110, RY - 62, cue, "Bold", 32)]
    for i in range(12):
        x = RX0 + i * RW
        els.append(karte(x, RY, RW - 10, 60, cue, fill=WEISS, rund=8, schatten=0, rand=4))
        if i < 5:
            els.append(karte(x, RY, RW - 10, 60, gezahlt_cue, fill=GRUEN, rund=8, schatten=0, rand=4))
    return els


folie([("w158", "1. Konstruktion › § 158 Abs. 1 BGB"), ("bed", "1. Konstruktion › Bedingung: vollständige Zahlung")],
      rechts_frei([
    *tafel("w158", "Die aufschiebende Bedingung"),
    *w158,
    *ratenleiste("bed", beim("bisher", "Gezahlt")),
    z("Bedingung: vollständige Zahlung, 2.400 €", 110, RY + 90, beim("bed", "vollständige"), "Bold", 34),
    *neinz("gezahlt: erst 1.000 €", RY + 150, beim("bisher", "Gezahlt"), "Bold", 34, x=160),
    blk(110, RY + 225, 1040, 80, HELLROT, "eig1", [("Eigentümer: noch das Möbelhaus", "ExtraBold", 36, INK)]),
    *requisit([("w158", ("tabler", "hourglass", 100, WEISS), "Bedingung", WEISS),
               ("bed", ("tabler", "coin-euro", 100, GELB), "2.400 €", GELB),
               (beim("bisher", "Gezahlt"), ("tabler", "coins", 100, GRUEN), "1.000 € gezahlt", GRUEN),
               ("eig1", ("tabler", "building-store", 120, GELB), "Eigentum: Möbelhaus", ROT)]),
    *paar("w158", "SO", [("w158", "ruhig"), ("bed", "denkt"), ("eig1", "sorge")], "SC",
          [("w158", "ruhig"), ("eig1", "froh")]),
]))

# ===========================================================================================================================
# G 2. Anwartschaftsrecht
# ===========================================================================================================================
folie([("anw", "2. Anwartschaftsrecht")], rechts_frei([
    *tafel("anw", "2. Anwartschaftsrecht"),
    *okz("Sonja hat ein Anwartschaftsrecht", 190, beim("anw", "Anwartschaftsrecht"), "Bold", 38, x=160),
    z("entsteht, wenn der andere Teil den Erwerb", 160, 280, "anw2", size=34),
    z("nicht mehr durch einseitige Erklärung", 160, 330, beim("anw2", "nicht"), size=34),
    z("zerstören kann", 160, 380, beim("anw2", "zerstören"), size=34),
    z("„ein dem Volleigentum wesensähnliches Recht“", 160, 460, "anw3", "Bold", 34),
    zit("BGH, Urt. v. 27.6.2025 – V ZR 143/24, Rn. 16", 160, 515, beim("anw3", "wesensähnliches")),
    linienzug([(110, 590), (1150, 590)], "anw4", breite=3),
    *okz("Rest gezahlt: Sonja wird Eigentümerin,", 620, beim("anw4", "wird"), "Bold", 36, x=160),
    z("ob das Möbelhaus will oder nicht", 160, 680, beim("anw4", "ob"), "Bold", 36),
    *requisit([("anw", ("tabler", "key", 100, GELB), "Anwartschaft", GELB),
               ("anw2", ("tabler", "shield-lock", 100, WEISS), "gesicherte Position", WEISS),
               (beim("anw4", "Eigentümerin"), ("tabler", "sofa", 140, SOFA), "Eigentum: Sonja", GRUEN)]),
    *paar("anw", "SO", [("anw", "laechelt"), ("anw4", "froh")], "SC", [("anw", "ruhig"), ("anw2", "denkt"),
                                                                      ("anw4", "ernst")]),
]))

# ===========================================================================================================================
# H 3. Herausgabe: § 985 (Wortlaut), § 986 Abs. 1
# ===========================================================================================================================
W985 = ["„Der Eigentümer kann von dem Besitzer die Herausgabe",
        "der Sache verlangen.“"]
w985, w985_y = wortlaut(80, 180, 1100, W985, "§ 985 BGB", beim("w985", "Der"), marken=[
    (0, "Eigentümer", beim("w985", "Eigentümer")), (0, "Besitzer", beim("w985", "Besitzer")),
    (1, "der Sache verlangen", beim("w985", "Sache"))], size=34)
folie([("her", "3. Herausgabe › § 985 BGB"), ("h3", "3. Herausgabe › Recht zum Besitz, § 986 Abs. 1 BGB")], rechts_frei([
    *tafel("her", "3. Herausgabe"),
    *w985,
    *okz("Eigentümer: das Möbelhaus", w985_y + 40, "h1", "Bold", 36, x=160),
    *okz("Besitzerin: Sonja, das Sofa steht bei ihr", w985_y + 100, "h2", "Bold", 36, x=160),
    z("Recht zum Besitz? § 986 Abs. 1 BGB", 110, w985_y + 180, "h3", "Bold", 36),
    z("dem Eigentümer gegenüber zum Besitz berechtigt", 160, w985_y + 235, beim("h3", "Eigentümer"), size=34),
    *okz("aus dem Kaufvertrag, bis zum wirksamen Rücktritt", w985_y + 300, "h4", "Bold", 34, x=160),
    zit("vgl. BGH, Urt. v. 8.5.2014 – IX ZR 128/12, Rn. 11", 160, w985_y + 355, beim("h4", "Es")),
    *requisit([("her", ("tabler", "hand-grab", 100, WEISS), "Herausgabe?", WEISS),
               ("h1", ("tabler", "building-store", 120, GELB), "Eigentümer", GELB),
               ("h2", ("tabler", "sofa", 140, SOFA), "Besitz: Sonja", WEISS),
               ("h3", ("tabler", "shield-check", 100, GRUEN), "Recht zum Besitz?", WEISS),
               ("h4", ("tabler", "contract", 100, GRUEN), "aus dem Kaufvertrag", GRUEN)]),
    *paar("her", "SO", [("her", "ruhig"), ("h2", "denkt"), ("h4", "froh")], "SC", [("her", "froh"), ("h3", "denkt"),
                                                                                  ("h4", "sorge")]),
]))

# ===========================================================================================================================
# I § 449 Abs. 2 (Wortlaut)
# ===========================================================================================================================
W4492 = ["„(2) Auf Grund des Eigentumsvorbehalts kann der Verkäufer",
         "die Sache nur herausverlangen, wenn er vom Vertrag",
         "zurückgetreten ist.“"]
w4492, w4492_y = wortlaut(80, 180, 1100, W4492, "§ 449 Abs. 2 BGB", beim("w4492", "Paragraf"), marken=[
    (1, "nur herausverlangen", beim("w4492", "nur")), (1, "wenn er vom Vertrag", beim("w4492", "wenn")),
    (2, "zurückgetreten", beim("w4492", "zurückgetreten"))], size=34)
folie([("w4492", "3. Herausgabe › § 449 Abs. 2 BGB")], rechts_frei([
    *tafel("w4492", "3. Herausgabe: erst nach Rücktritt"),
    *w4492,
    blk(110, w4492_y + 60, 1040, 80, HELLROT, "nurev", [("Der Vorbehalt allein genügt nicht.", "ExtraBold", 36, INK)]),
    *requisit([("w4492", ("tabler", "arrow-back-up", 100, WEISS), "§ 449 Abs. 2", WEISS),
               ("nurev", ("tabler", "lock", 100, ROT), "Vorbehalt allein: nein", ROT)]),
    *paar("w4492", "SO", [("w4492", "ruhig"), ("nurev", "froh")], "SC", [("w4492", "ruhig"), ("nurev", "sorge")]),
]))

# ===========================================================================================================================
# J Rücktritt, Teilzahlungsgeschäft, Rückabwicklung
# ===========================================================================================================================
folie([("rt1", "Rücktritt › § 323 Abs. 1 BGB"), ("tz", "Rücktritt › Teilzahlungsgeschäft?"),
       ("rg", "Rückabwicklung › §§ 346 ff. BGB")], rechts_frei([
    *tafel("rt1", "Rücktritt und Rückabwicklung"),
    z("Rücktrittsrecht: § 323 Abs. 1 BGB", 110, 180, beim("rt1", "Rücktrittsrecht"), "Bold", 36),
    z("erfolglos angemessene Frist zur Zahlung", 150, 235, beim("rt1", "erfolglos"), size=34),
    blk(110, 295, 1040, 70, LILA, beim("rt1", "Mehr"), [("Mehr dazu: Video „Rücktritt“", "ExtraBold", 32, INK)]),
    linienzug([(110, 395), (1150, 395)], "tz", breite=3),
    z("entgeltliches Teilzahlungsgeschäft? offen", 110, 415, "tz", "Bold", 36),
    z("dann: Rücktritt wegen Zahlungsverzugs nur", 150, 470, beim("tz", "dann"), size=34),
    z("unter strengeren Voraussetzungen, § 508 BGB", 150, 520, beim("tz", "strengeren"), size=34),
    linienzug([(110, 595), (1150, 595)], "rg", breite=3),
    z("nach wirksamem Rücktritt: §§ 346 ff. BGB", 110, 615, "rg", "Bold", 36),
    z("Sonja: Sofa zurück, Wertersatz für die Nutzung", 150, 670, beim("rg", "Sonja"), size=34),
    z("Möbelhaus: 1.000 € zurück", 150, 725, beim("rg", "Möbelhaus"), size=34),
    zit("§ 346 Abs. 1, Abs. 2 Satz 1 Nr. 1 BGB", 150, 780, beim("rg", "Wertersatz")),
    *requisit([("rt1", ("tabler", "arrow-back-up", 100, WEISS), "Rücktrittsrecht", WEISS),
               (beim("rt1", "Frist"), ("tabler", "hourglass", 100, WEISS), "Frist zur Zahlung", WEISS),
               ("tz", ("tabler", "calendar-dollar", 100, WEISS), "Teilzahlung?", WEISS),
               ("rg", ("tabler", "arrows-exchange", 110, WEISS), "Rückabwicklung", WEISS),
               (beim("rg", "Sofa"), ("tabler", "sofa", 140, SOFA), "Sofa zurück", WEISS),
               (beim("rg", "Möbelhaus"), ("tabler", "coins", 100, GELB), "1.000 € zurück", GELB)]),
    *paar("rt1", "SO", [("rt1", "ruhig"), ("tz", "denkt"), ("rg", "sorge")], "SC", [("rt1", "ruhig"), ("tz", "denkt"),
                                                                                   ("rg", "ruhig")]),
]))

# ===========================================================================================================================
# K Ergebnis (zurück im Wohnzimmer)
# ===========================================================================================================================
EX = 1450                                    # Sonja neben dem Sofa, blickt nach links zur Tafel
folie([("erg", "Ergebnis"), ("erg5", "Ergebnis › nach wirksamem Rücktritt")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Eigentümer: noch das Möbelhaus", 190, "erg1", "Bold", 36, x=160),
    *neinz("keine Frist: kein wirksamer Rücktritt", 255, "erg2", "Bold", 36, x=160),
    *okz("Sonja darf das Sofa vorerst behalten", 320, beim("erg3", "Sonja"), "Bold", 36, x=160),
    *neinz("kein Abholen gegen ihren Willen", 385, beim("erg3", "Möbelhaus"), "Bold", 36, x=160),
    *okz("Möbelhaus: fällige Raten, § 433 Abs. 2 BGB", 450, "erg4", "Bold", 36, x=160),
    blk(110, 535, 1040, 120, HELL, "erg5", [("erst nach wirksamem Rücktritt:", "ExtraBold", 34, INK),
                                            ("Herausgabe, §§ 985, 346 Abs. 1 BGB", "ExtraBold", 34, INK)]),
    zit("vgl. BGH, Beschl. v. 24.1.2019 – IX ZR 110/17, Rn. 65", 110, 675, beim("erg5", "Paragraf")),
    boden("erg", x0=1240, x1=1880),
    hart(ficon("tabler", "sofa", 1700, BODEN, 300, "erg", fuell=SOFA)),
    *fig("SO", EX, BODEN, 440, [("erg", "ruhig"), ("erg3", "froh"), ("erg5", "denkt")]),
    ns("Sonja", EX, BODEN, "erg", SO_N, d=0.1),
    pl("Sofa bleibt vorerst bei Sonja", 1560, 200, "erg3", fill=GRUEN, size=28, anker="m", bis="erg5"),
    pl("erst nach Rücktritt: zurück", 1560, 200, "erg5", fill=GELB, size=28, anker="m"),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · letzte Rate"), ("tipp3", "Klausurtipp · Begriffe")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Mit der letzten Rate geht das Eigentum", 200, 200, beim("tipp", "letzten"), "Bold", 36),
    z("automatisch über.", 200, 255, beim("tipp", "automatisch"), "Bold", 36),
    z("keine neue Einigung, keine Erklärung:", 200, 335, "tipp2", size=34),
    z("Die Bedingung tritt ein, § 158 Abs. 1 BGB.", 200, 390, beim("tipp2", "Bedingung"), size=34),
    linienzug([(130, 470), (1130, 470)], "tipp3", breite=3),
    z("2 Begriffe für später:", 200, 500, "tipp3", "Bold", 36),
    z("verlängerter Eigentumsvorbehalt", 240, 560, beim("tipp3", "verlängerten"), size=34),
    z("erweiterter Eigentumsvorbehalt", 240, 615, beim("tipp3", "erweiterten"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Eigentum des Verkäufers", "", BLAU, 0),
          ("k11", "1.", "Übereignung aufschiebend bedingt", "§§ 929 S. 1, 158 Abs. 1, 449 Abs. 1 BGB", None, 1),
          ("k12", "2.", "Bedingung nicht eingetreten: Käufer hat nur das Anwartschaftsrecht", "", None, 1),
          ("k2", "II.", "Besitz des Käufers", "", GELB, 0),
          ("k3", "III.", "kein Recht zum Besitz", "§ 986 Abs. 1 BGB", GRUEN, 0),
          ("k31", "1.", "Recht zum Besitz aus dem Kaufvertrag", "", None, 1),
          ("k32", "2.", "endet erst mit wirksamem Rücktritt", "§§ 449 Abs. 2, 323 BGB", None, 1),
          ("k4", "", "daneben: Rückgewähr", "§ 346 Abs. 1 BGB", None, 2)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Herausgabe beim Eigentumsvorbehalt"), 110, 90, "sch", 46),
           zit("Herausgabeanspruch des Vorbehaltsverkäufers, § 985 BGB", 110, 150, "sch", size=30)]
y = 215
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 92
    elif ebene == 1:
        els_sch += [z(r, 270, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 330, y + 4, c, "Bold", 36, rechts=1820)]
        hh = 76
    else:
        y += 14
        els_sch += [linienzug([(110, y - 8), (1810, y - 8)], c, breite=3), z(kopf, 130, y + 10, c, "ExtraBold", 38, rechts=1820)]
        hh = 92
    if norm:
        els_sch.append(zit(norm, 1260, y + (18 if ebene != 1 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Eigentum"), ("k2", "Klausurschema › II. Besitz"),
       ("k3", "Klausurschema › III. kein Recht zum Besitz"), ("k4", "Klausurschema › Rückgewähr")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Kauf ist unbedingt,", "a")], [("nur die Übereignung ist bedingt.", "b")]],
                750, 290, 42, "merke", {"a": beim("merke", "Kauf"), "b": beim("merke", "Übereignung")}),
    *markertext([[("Das Eigentum geht erst mit", 0)], [("der letzten Rate über.", "c")]],
                750, 480, 42, "mk2", {"c": beim("mk2", "letzten")}),
    *markertext([[("Zurückholen erst", 0)], [("nach dem Rücktritt.", "d")]],
                750, 670, 42, "mk3", {"d": beim("mk3", "Rücktritt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
