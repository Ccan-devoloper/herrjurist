"""Folge 123 · Prüfungsschemata lernen – aber richtig: Verstehen statt pauken – Serienstandard Open Peeps (Katzenkönig).
Rahmen: Gunnar hat 80 Schemata auf Karteikarten gelernt (Karteikarten-Turm auf dem Schreibtisch) und scheitert im Tutorium
am Fall „Handy auf dem Gehweg“. Die Tutorin Marlene zeigt drei Werkzeuge. Szenen laut ../SZENENPLAN.md:
A1 Lerntisch mit Karteikarten-Turm, A2 Auswendig gelernt – am Fall gescheitert, B Sachverhalt, C1 Werkzeug 1: Landkarte
(Wortlautkarte § 242 Abs. 1 StGB), C2 Werkzeug 1 am Fall, D1 Werkzeug 2: Warum subjektiv?, D2 Zivilrecht: drei Stufen,
E1 Werkzeug 3: Wortlautkarte § 246 Abs. 1 StGB neben § 242, E2 Werkzeug 3 am Fall, F Lernen mit Fällen,
G Klausurtipp (Lexi), H Klausurschema § 246, I Merksatz (Lexi).
Ein Handlungsgeräusch (Marlene legt den Fall auf den Tisch; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 117 (gemeinsame Dateien unverändert); neu: turm() (Karteikarten-Turm aus Karten),
Vergleichstabelle § 242/§ 246, Treppe der drei Stufen.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_123/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_123/" in n:
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




BODEN, FH = 860, 480
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GU_N, MA_N = TUERKIS, LILA                  # Farben der Namensschilder
PX, PY, PU = 1560, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
HOLZ = (214, 160, 110, 255)
DUNKELGRUEN, DUNKELROT = (40, 150, 85, 255), (215, 60, 45, 255)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge, bis_ende=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=30, anker="m", bis=b))
    return els


def paar(c0, gf, mf, bis=None, gu_bis=None, ma_bis=None):
    """Tafelszene: Gunnar (links) und Marlene (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("GU", X1, FB, FR, gf, bis=gu_bis or bis), ns("Gunnar", X1, FB, c0, GU_N, d=0.1),
            *fig("MA", X2, FB, FR, mf, bis=ma_bis or bis, d=0.2), ns("Marlene", X2, FB, c0, MA_N, d=0.3)]


def turm(cx, unten, n, cue, d0=0.07, bis=None, anim="pop"):
    """Karteikarten-Turm: n flache Karten übereinander (aus Karten-Bausteinen, Palettenfarben)."""
    els, farben = [], [WEISS, GELB, BLAU, WEISS, GRUEN, LILA, WEISS, PINK]
    for i in range(n):
        w = 170 - (i % 3) * 8
        x = cx - w / 2 + ((i * 37) % 5 - 2) * 4
        e = karte(int(x), unten - (i + 1) * 30, w, 26, cue, fill=farben[i % len(farben)], rund=6, schatten=3, rand=3,
                  anim=anim, d=d0 * i)
        e.name = "karte:turm"
        els.append(bis_(e, bis))
    return els


def stufe_mini(x, y, aktiv, cue, bis=None):
    """Kleine Treppe (drei Stufen), aktive Stufe farbig."""
    els = []
    for i, f in enumerate((BLAU, GELB, GRUEN)):
        els.append(bis_(karte(x + i * 46, y - i * 22, 44, 22 + i * 22, cue, fill=f if i == aktiv else WEISS, rund=4,
                              schatten=2, rand=3), bis))
    return els


# ===========================================================================================================================
# A1 Fall: Lerntisch mit Karteikarten-Turm, Marlene legt den Fall hin
# ===========================================================================================================================
GX, MX = 600, 1560                          # Gunnar (blickt nach rechts zum Tisch/zu Marlene), Marlene (blickt nach links)
TISCHX = 1050
tisch = ficon("tabler", "desk", TISCHX, BODEN - 2, 460, NULL, fuell=HOLZ)
TT = int(tisch.y) + 8                       # Tischplatte (Oberkante des Icons)
TURMX = TISCHX - 40
mh = hand("MA_ruhig", MX, BODEN, FH, -1)
BLATT_X, BLATT_U = TISCHX + 135, TT + 6
HIN = beim("tut", "legt")
LIEGT = ("tut", round(HIN[1] + 0.5, 3))
folie([(NULL, "Fall · Gunnar lernt"), ("turm", "Fall · 80 Schemata auf Karteikarten"), ("tut", "Fall · Im Tutorium"),
       ("g1", "Fall · Keine Karte für den Fall")], [
    hart(boden(NULL)),
    hart(tisch),
    hart(pl("Lernen für die Strafrechtsklausur", 70, 30, NULL, fill=GELB, size=40)),
    hart(ficon("tabler", "lamp", TISCHX - 185, TT + 4, 110, NULL, fuell=GELB)),
    *turm(TURMX, TT + 4, 3, NULL, anim="cut", d0=0.0),
    *turm(TURMX, TT + 4 - 90, 9, beim("turm", "Turm")),
    pl("80 Schemata", TURMX, TT - 450, beim("turm", "achtzig"), fill=WEISS, size=34, anker="m"),
    pl("alle auswendig", TURMX, TT - 375, beim("turm", "alle"), fill=GRUEN, size=30, anker="m"),
    # Marlene kommt ins Bild und legt den Fall auf den Tisch
    *fig("MA", MX, BODEN, FH, [("tut", "ruhig"), (LIEGT, "froh"), ("g1", "denkt")]),
    ns("Marlene", MX, BODEN, "tut", MA_N, d=0.2),
    bis_(ficon("tabler", "file-text", mh[0] - 30, mh[1] + 40, 90, "tut", fuell=WEISS, d=0.3), HIN),
    szene(bewegt(ficon("tabler", "file-text", BLATT_X, BLATT_U, 90, HIN, fuell=WEISS, anim="cut"),
                 HIN, LIEGT, (mh[0] - 30) - BLATT_X, (mh[1] + 40) - BLATT_U), "123blatt*", 0.8, versatz=0.5 - 0.18),
    pl("Fall", BLATT_X, TT - 150, LIEGT, fill=PINK, size=30, anker="m"),
    # Gunnar (links, blickt zum Tisch)
    *fig("GU", GX, BODEN, FH, [(NULL, "muede_r"), ("turm", "froh_r"), ("tut", "denkt_r"), (beim("tut", "Fall"), "sorge_r")],
         erst="cut", bis="g1"),
    hart(ns("Gunnar", GX, BODEN, NULL, GU_N)),
    *redet("GU_redet_r", GX, BODEN, FH, "g1", "hook"),
    blase("sprech", 740, 200, "g1", 560, 225, inhalt=["Diebstahl passt nicht. Und für", "alles andere habe ich keine Karte!"],
          textsize=34, figur=("GU_redet_r", GX, BODEN, FH), bis="hook"),
])

# ===========================================================================================================================
# A2 Auswendig gelernt – am Fall gescheitert
# ===========================================================================================================================
DREI = beim("m1", "drei")
folie([("hook", "Fall · Auswendig, und trotzdem gescheitert?"), ("hook2", "Fall · Vom Schema zurück zum Gesetz"),
       ("m1", "Fall · Drei Werkzeuge")], rechts_frei([
    *tafel("hook", "Auswendig gelernt, am Fall gescheitert?"),
    dicon("tabler", "cards", 170, 255, 80, beim("hook", "achtzig"), fuell=GELB),
    z("80 Schemata auswendig", 230, 190, beim("hook", "achtzig"), "Bold", 38),
    *neinz("trotzdem gescheitert am Fall", 285, beim("hook", "scheiterst"), "Bold", 38, x=230),
    z("Oft fehlt nicht der Fleiß,", 110, 390, "hook2", "Bold", 36),
    z("sondern der Weg vom Schema zurück zum Gesetz:", 110, 445, beim("hook2", "sondern"), "Bold", 36),
    blk(160, 530, 360, 100, BLAU, beim("hook2", "Schema"), [("Schema", "ExtraBold", 40, INK)], anim="pop"),
    pfeil(540, 580, 700, 580, beim("hook2", "zurück"), breite=10, kopf=30),
    blk(720, 530, 380, 100, GELB, beim("hook2", "Gesetz"), [("Gesetz", "ExtraBold", 40, INK)], anim="pop"),
    blk(110, 700, 1040, 110, GRUEN, DREI, [("3 Werkzeuge", "ExtraBold", 44, INK)]),
    *requisit([("hook", ("tabler", "cards", 110, GELB), "auswendig", WEISS)], bis_ende="m1"),
    *paar("hook", [("hook", "sorge"), ("hook2", "denkt"), (DREI, "froh")], [("hook", "ruhig"), ("hook2", "ernst")],
          ma_bis="m1"),
    *redet("MA_redet", X2, FB, FR, "m1", "sv"),
    blase("sprech", 660, 270, "m1", 1520, 210, inhalt=["Wirf deine Karten nicht weg.", "Aber lerne, woher jeder",
                                                      "Punkt kommt. Ich zeige dir", "3 Werkzeuge."],
          textsize=33, figur=("MA_redet", X2, FB, FR), bis="sv"),
]))


# ===========================================================================================================================
# B Sachverhalt (Fall aus dem Tutorium)
# ===========================================================================================================================
def sachverhalt_123(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Der Fall aus dem Tutorium", 210, 100, cue, 56)]
    y = 215
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=46, zeilenabstand=1.4)
        els += e; y += 34
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_123("sv", [
    "Spät am Abend findet ein Spaziergänger auf dem leeren Gehweg ein Handy. Die Eigentümerin hat es kurz vorher "
    "verloren, ist längst fort und weiß nicht, wo es liegt.",
    "Der Spaziergänger steckt das Handy ein, um es zu behalten. Zu Hause legt er seine eigene SIM-Karte ein und benutzt "
    "das Handy seitdem als seines.",
], "Hat sich der Spaziergänger strafbar gemacht?")

# ===========================================================================================================================
# C1 Werkzeug 1: das Schema als Landkarte des Gesetzes (§ 242 Abs. 1 StGB)
# ===========================================================================================================================
W242 = ["„Wer eine fremde bewegliche Sache einem anderen in der",
        "Absicht wegnimmt, die Sache sich oder einem Dritten",
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu",
        "fünf Jahren oder mit Geldstrafe bestraft.“"]
w242, w242_y = wortlaut(110, 240, 1040, W242, "§ 242 Abs. 1 StGB", "p242w", marken=[
    (0, "fremde bewegliche Sache", beim("obj", "fremde")),
    (1, "wegnimmt", beim("obj", "wegnimmt")),
    (0, "in der", beim("subj", "Absicht")),
    (1, "Absicht", beim("subj", "Absicht")),
    (2, "rechtswidrig zuzueignen", beim("subj", "rechtswidrig"))], size=30)
assert w242_y <= 510, w242_y
folie([("w1", "Werkzeug 1 · Das Schema als Landkarte"), ("p242", "Werkzeug 1 · Wortlaut § 242 Abs. 1 StGB"),
       ("obj", "Werkzeug 1 · § 242 › I. 1. objektiver Tatbestand"), ("subj", "Werkzeug 1 · § 242 › I. 2. subjektiver Tatbestand"),
       ("vors", "Werkzeug 1 · § 242 › aus dem Allgemeinen Teil")], rechts_frei([
    *tafel("w1", "Werkzeug 1: das Schema als Landkarte"),
    z("Jeder Prüfungspunkt kommt aus einem Wort.", 110, 180, beim("w1", "Jeder"), "Bold", 34),
    *w242,
    z("I. Tatbestand", 110, 530, "obj", "ExtraBold", 34),
    pl("1. objektiv: fremde bewegliche Sache", 110, 580, beim("obj", "fremde"), fill=GRUEN, size=30),
    pl("Wegnahme", 770, 580, beim("obj", "wegnimmt"), fill=GRUEN, size=30),
    pl("2. subjektiv: Absicht rechtswidriger Zueignung", 110, 650, beim("subj", "Absicht"), fill=GRUEN, size=30),
    z("aus dem Allgemeinen Teil:", 110, 735, beim("vors", "Allgemeinen"), "Bold", 32),
    pl("Vorsatz, § 15 StGB", 520, 725, beim("vors", "Vorsatz"), fill=BLAU, size=30),
    pl("II. Rechtswidrigkeit", 110, 800, beim("rws", "Rechtswidrigkeit"), fill=BLAU, size=30),
    pl("III. Schuld", 470, 800, beim("rws", "Schuld"), fill=BLAU, size=30),
    *requisit([("w1", ("tabler", "map-2", 110, GELB), "Landkarte", WEISS),
               ("p242", ("tabler", "book", 100, WEISS), "§ 242 StGB", WEISS),
               ("vors", ("tabler", "book", 100, BLAU), "Allgemeiner Teil", BLAU)]),
    *paar("w1", [("w1", "ruhig"), ("p242", "denkt"), ("obj", "ruhig"), ("vors", "froh")],
          [("w1", "froh"), ("p242", "ruhig")]),
]))

# ===========================================================================================================================
# C2 Werkzeug 1 am Fall: § 242 StGB scheitert an der Wegnahme
# ===========================================================================================================================
GW_Y = 490
folie([("fall1", "Werkzeug 1 · am Fall: § 242 StGB"), ("wegn", "Werkzeug 1 · § 242 › b) Wegnahme"),
       ("kein", "Werkzeug 1 · § 242 › Ergebnis: kein Diebstahl")], rechts_frei([
    *tafel("fall1", "Werkzeug 1 am Fall: § 242 StGB"),
    *okz("a) fremde bewegliche Sache: das Handy", 180, beim("fall1", "Handy"), "Bold", 34, x=160),
    z("b) Wegnahme: fremden Gewahrsam brechen", 110, 255, "wegn", "Bold", 34),
    z("und neuen begründen", 165, 305, beim("wegn", "neuen"), "Bold", 34),
    zit("BGH 4 StR 338/20, Rn. 5", 560, 312, beim("wegn", "neuen")),
    linienzug([(160, GW_Y), (1100, GW_Y)], "gew", breite=6, farbe=INK),
    pl("Gehweg", 170, GW_Y + 16, "gew", fill=WEISS, size=28),
    dicon("tabler", "device-mobile", 520, GW_Y - 4, 80, "gew", fuell=BLAU),
    dicon("tabler", "moon", 1040, GW_Y - 70, 70, "gew", fuell=GELB),
    pl("Eigentümerin: fort, keine Einwirkung", 600, GW_Y + 16, beim("gew", "einwirken"), fill=ROT, size=28),
    *neinz("kein Gewahrsam mehr", 590, beim("gew", "keinen"), "Bold", 34, x=160),
    zit("BGH 5 StR 10/20, Rn. 6 f.", 560, 598, beim("gew", "keinen")),
    blk(110, 700, 1040, 80, ROT, "kein", [("Keine Wegnahme, also kein Diebstahl", "ExtraBold", 36, INK)]),
    *okz("Bis hierhin trägt das Schema.", 810, beim("kein", "Bis"), "Bold", 32, x=160),
    *requisit([("fall1", ("tabler", "device-mobile", 90, BLAU), "das Handy", WEISS),
               ("gew", ("tabler", "road", 100, WEISS), "Gehweg, Eigentümerin fort", WEISS),
               ("kein", ("tabler", "cards", 110, GELB), "Und jetzt?", PINK)]),
    *paar("fall1", [("fall1", "ruhig"), ("wegn", "denkt"), ("kein", "sorge")], [("fall1", "ruhig"), ("gew", "ernst")]),
]))

# ===========================================================================================================================
# D1 Werkzeug 2: Warum steht der Punkt hier? (Zueignungsabsicht im subjektiven Tatbestand)
# ===========================================================================================================================
ZS_Y = 560
folie([("w2", "Werkzeug 2 · Warum steht der Punkt hier?"), ("w2a", "Werkzeug 2 · Warum ist die Zueignung subjektiv?"),
       ("w2b", "Werkzeug 2 · Vollendet mit der Wegnahme")], rechts_frei([
    *tafel("w2", "Werkzeug 2: Warum steht der Punkt hier?"),
    pl("Warum ist die Zueignung subjektiv?", 110, 175, beim("w2a", "Warum"), fill=PINK, size=34),
    z("Weil das Gesetz nur die Absicht verlangt:", 110, 270, beim("w2a", "Weil"), "Bold", 34),
    z("„… in der Absicht wegnimmt, die Sache sich … zuzueignen“", 110, 325, beim("w2a", "Absicht"), size=30),
    zit("§ 242 Abs. 1 StGB", 110, 372, beim("w2a", "Absicht")),
    linienzug([(160, ZS_Y), (1110, ZS_Y)], "w2b", breite=6, farbe=INK),
    linienzug([(330, ZS_Y - 16), (330, ZS_Y + 16)], beim("w2b", "Weck"), breite=6),
    pl("Wegnahme", 250, ZS_Y - 90, beim("w2b", "Weck"), fill=GELB, size=30),
    *okz("Diebstahl vollendet", ZS_Y + 30, beim("w2b", "vollendet"), "Bold", 32, x=230),
    linienzug([(860, ZS_Y - 16), (860, ZS_Y + 16)], beim("w2b", "behält"), breite=6),
    pl("behält er sie?", 760, ZS_Y - 90, beim("w2b", "behält"), fill=WEISS, size=30),
    z("für den Tatbestand egal", 720, ZS_Y + 34, beim("w2b", "egal"), "Bold", 32),
    zit("BGH 4 StR 591/17, Rn. 17", 110, 700, beim("w2b", "Bundesgerichtshof")),
    *requisit([("w2", ("tabler", "help", 100, GELB), "Warum?", GELB),
               ("w2b", ("tabler", "device-mobile", 90, BLAU), "behalten egal", WEISS)]),
    *paar("w2", [("w2", "ruhig"), ("w2a", "denkt"), (beim("w2b", "egal"), "froh")],
          [("w2", "froh"), ("w2a", "ruhig")]),
]))

# ===========================================================================================================================
# D2 Zivilrecht: entstanden – untergegangen – durchsetzbar (Verweis Folge 103)
# ===========================================================================================================================
TR = [(beim("w2c", "entstanden"), "1. entstanden", BLAU), (beim("w2c", "untergegangen"), "2. untergegangen", GELB),
      (beim("w2c", "durchsetzbar"), "3. durchsetzbar", GRUEN)]
folie([("w2c", "Werkzeug 2 · Zivilrecht: drei Stufen"), ("w2d", "Werkzeug 2 · Warum diese Reihenfolge?")], rechts_frei([
    *tafel("w2c", "Im Zivilrecht genauso: drei Stufen"),
    *[blk(110 + i * 345, 330 - i * 60, 330, 90 + i * 60, f, c, [(t, "ExtraBold", 32, INK)], anim="pop")
      for i, (c, t, f) in enumerate(TR)],
    z("Erlöschen kann nur, was entstanden ist.", 110, 470, beim("w2d", "Erlöschen"), "Bold", 34),
    zit("§ 362 Abs. 1 BGB: „Das Schuldverhältnis erlischt, …“", 110, 520, beim("w2d", "Erlöschen")),
    z("Verjährung: Der Anspruch bleibt bestehen,", 110, 585, beim("w2e", "Verjährung"), "Bold", 34),
    z("nur Recht, die Leistung zu verweigern: zuletzt", 110, 635, beim("w2e", "Recht"), "Bold", 34),
    zit("§ 214 Abs. 1 BGB", 110, 685, beim("w2e", "Recht")),
    pl("mehr in Folge 103", 800, 680, beim("w2e", "Folge"), fill=LILA, size=30),
    blk(110, 750, 1040, 80, GELB, "w2f", [("Grund kennen statt Reihenfolge pauken", "ExtraBold", 36, INK)]),
    *requisit([("w2c", ("tabler", "stairs-up", 110, WEISS), "drei Stufen", WEISS),
               ("w2e", ("tabler", "hourglass", 100, GELB), "Verjährung", GELB),
               ("w2f", ("tabler", "bulb", 100, GELB), "verstanden", GRUEN)]),
    *paar("w2c", [("w2c", "denkt"), ("w2d", "ruhig"), ("w2f", "froh")], [("w2c", "ruhig"), ("w2f", "froh")]),
]))

# ===========================================================================================================================
# E1 Werkzeug 3: das Schema aus dem Wortlaut bauen (§ 246 Abs. 1 StGB neben § 242)
# ===========================================================================================================================
W246 = ["„Wer eine fremde bewegliche Sache sich oder einem Dritten",
        "rechtswidrig zueignet, wird mit Freiheitsstrafe bis zu drei",
        "Jahren oder mit Geldstrafe bestraft, wenn die Tat nicht in",
        "anderen Vorschriften mit schwererer Strafe bedroht ist.“"]
w246, w246_y = wortlaut(110, 235, 1040, W246, "§ 246 Abs. 1 StGB", "p246w", marken=[
    (0, "fremde bewegliche Sache", beim("t1", "Fremde")),
    (1, "zueignet", beim("t3", "zueignet"))], size=30)
assert w246_y <= 505, w246_y
C1X, C2X, RY = 130, 650, [590, 655, 720, 785]
folie([("w3", "Werkzeug 3 · Schema aus dem Wortlaut"), ("p246", "Werkzeug 3 · Wortlaut § 246 Abs. 1 StGB"),
       ("neben", "Werkzeug 3 · § 246 neben § 242"), ("t4", "Werkzeug 3 · Zueignung wird objektiv")], rechts_frei([
    *tafel("w3", "Werkzeug 3: Schema aus dem Wortlaut"),
    z("Nie gelernt? Dann baust du das Schema aus dem Wortlaut.", 110, 180, beim("w3", "Ein"), "Bold", 32),
    *w246,
    karte(110, 515, 1040, 350, "neben", fill=HELL, rund=14, schatten=6, rand=4),
    z("§ 242 Diebstahl", C1X, 530, "neben", "ExtraBold", 32),
    z("§ 246 Unterschlagung", C2X, 530, "neben", "ExtraBold", 32),
    linienzug([(630, 530), (630, 850)], "neben", breite=4, farbe=TEXT),
    z("fremde bewegliche Sache", C1X, RY[0], beim("t1", "Fremde"), size=30),
    *okz("fremde bewegliche Sache", RY[0], beim("t1", "kennst"), size=30, x=C2X + 45, gr=18),
    z("wegnimmt", C1X, RY[1], beim("t2", "Wegnimmt"), size=30),
    *neinz("fehlt: kein Gewahrsamsbruch", RY[1], beim("t2", "fehlt"), size=30, x=C2X + 45, gr=18),
    z("in der Absicht … zuzueignen", C1X, RY[2], beim("t3", "Absicht"), size=30),
    z("zueignet", C2X + 45, RY[2], beim("t3", "zueignet"), "Bold", 30),
    pl("subjektiv", C1X, RY[3] - 6, beim("t4", "wandert"), fill=WEISS, size=28),
    pfeil(400, RY[3] + 20, C2X + 30, RY[3] + 20, beim("t4", "wandert"), breite=8, kopf=24),
    pl("objektiv", C2X + 45, RY[3] - 6, beim("t4", "objektiven"), fill=GRUEN, size=28),
    *requisit([("w3", ("tabler", "tools", 100, WEISS), "selbst bauen", WEISS),
               ("p246", ("tabler", "book", 100, WEISS), "§ 246 StGB", WEISS),
               ("neben", ("tabler", "arrows-exchange", 100, GELB), "neben § 242", GELB)]),
    *paar("w3", [("w3", "sorge"), ("p246", "denkt"), ("t1", "ruhig"), ("t4", "froh")],
          [("w3", "froh"), ("p246", "ruhig")]),
]))

# ===========================================================================================================================
# E2 Werkzeug 3 am Fall: § 246 StGB
# ===========================================================================================================================
folie([("t5", "Werkzeug 3 · am Fall: § 246 StGB"), ("t6", "Werkzeug 3 · § 246 › Zueignung"),
       ("t7", "Werkzeug 3 · § 246 › rechtswidrig"), ("t8", "Werkzeug 3 · § 246 › Vorsatz, Rechtswidrigkeit, Schuld"),
       ("t9", "Werkzeug 3 · § 246 › keine schwerere Vorschrift"), ("erg", "Werkzeug 3 · Ergebnis: Unterschlagung")],
      rechts_frei([
    *tafel("t5", "Werkzeug 3 am Fall: § 246 StGB"),
    z("Wie viel Zueignung? Die Strafsenate des BGH", 110, 180, beim("t5", "Strafsenate"), "Bold", 32),
    z("sehen es unterschiedlich.", 110, 225, beim("t5", "unterschiedlich"), "Bold", 32),
    zit("BGH 6 StR 191/23, Rn. 5, 10; BGH 4 StR 442/23, Rn. 11", 110, 272, beim("t5", "unterschiedlich")),
    *okz("nach jeder Ansicht: benutzt das Handy als seines", 330, beim("t6", "benutzt"), "Bold", 32, x=160),
    z("und schließt die Eigentümerin aus", 160, 378, beim("t6", "schließt"), "Bold", 32),
    *okz("rechtswidrig: kein Anspruch auf das Handy", 445, "t7", "Bold", 32, x=160),
    *okz("Vorsatz, Rechtswidrigkeit und Schuld", 515, "t8", "Bold", 32, x=160),
    *okz("keine schwerere Vorschrift greift", 585, "t9", "Bold", 32, x=160),
    blk(110, 670, 1040, 90, GRUEN, "erg", [("Ergebnis: Unterschlagung, § 246 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    *requisit([("t5", ("tabler", "scale", 100, WEISS), "BGH uneins", WEISS),
               ("t6", ("tabler", "device-mobile", 90, BLAU), "als seines benutzt", WEISS),
               ("erg", ("tabler", "book", 100, GRUEN), "§ 246 StGB", GRUEN)], bis_ende="g2"),
    *paar("t5", [("t5", "denkt"), ("t6", "ruhig"), ("erg", "froh")], [("t5", "ruhig"), ("erg", "froh")], gu_bis="g2"),
    *redet("GU_redetfroh", X1, FB, FR, "g2", "m2"),
    blase("sprech", 600, 190, "g2", 1560, 190, inhalt=["Das Schema stand ja", "schon im Gesetz!"],
          textsize=36, figur=("GU_redetfroh", X1, FB, FR), bis="m2"),
]))

# ===========================================================================================================================
# F Lernen mit Fällen statt Listen
# ===========================================================================================================================
folie([("m2", "Lernen · mit Fällen statt Listen"), ("l1", "Lernen · 1. Schema aus dem Kopf"),
       ("l2", "Lernen · 2. Vergleichen, Fehler notieren"), ("l3", "Lernen · 3. Wiederholen nach ein paar Tagen"),
       ("l4", "Lernen · Was die Lernforschung sagt")], rechts_frei([
    *tafel("m2", "Mit Fällen statt Listen"),
    dicon("tabler", "brain", 175, 270, 80, "l1", fuell=BLAU),
    blk(240, 180, 910, 100, BLAU, "l1", [("1. Kurzer Fall: Schema aus dem Kopf,", "Bold", 32, INK),
                                         ("ohne Karte", "Bold", 32, INK)]),
    dicon("tabler", "list-check", 175, 400, 80, "l2", fuell=GELB),
    blk(240, 310, 910, 100, GELB, "l2", [("2. Mit dem Gesetz vergleichen,", "Bold", 32, INK),
                                         ("jeden Fehler notieren", "Bold", 32, INK)]),
    dicon("tabler", "calendar-repeat", 175, 530, 80, "l3", fuell=GRUEN),
    blk(240, 440, 910, 100, GRUEN, "l3", [("3. Ein paar Tage später: derselbe Fall,", "Bold", 32, INK),
                                          ("danach ein neuer", "Bold", 32, INK)]),
    z("Lernforschung: Abrufen aus dem Gedächtnis", 110, 590, beim("l4", "Lernforschung"), "Bold", 32),
    z("und verteiltes Wiederholen halten länger", 110, 635, beim("l4", "verteilt"), "Bold", 32),
    *neinz("als bloßes Wiederlesen oder Pauken an einem Abend", 690, beim("l4", "bloßes"), "Bold", 30, x=160),
    zit("Weinstein, Madan & Sumeracki, Cognitive Research 3 (2018), Art. 2", 110, 745, beim("l4", "Lernforschung")),
    *requisit([("l1", ("tabler", "notebook", 100, WEISS), "aus dem Kopf", WEISS),
               ("l2", ("tabler", "book", 100, GELB), "mit dem Gesetz", GELB),
               ("l3", ("tabler", "calendar-repeat", 100, GRUEN), "ein paar Tage später", GRUEN),
               ("l4", ("tabler", "school", 100, WEISS), "Lernforschung", WEISS)], bis_ende="g3"),
    *fig("GU", X1, FB, FR, [("m2", "ruhig"), ("l1", "denkt"), ("l3", "ruhig"), ("l4", "froh")], bis="g3", d=0.0),
    ns("Gunnar", X1, FB, "m2", GU_N, d=0.1),
    *fig("MA", X2, FB, FR, [("l1", "froh")], erst="cut"),
    ns("Marlene", X2, FB, "m2", MA_N, d=0.3),
    *redet("MA_redet", X2, FB, FR, "m2", "l1"),
    blase("sprech", 600, 190, "m2", 1500, 190, inhalt=["Und so lernst du damit:", "mit Fällen statt Listen."],
          textsize=36, figur=("MA_redet", X2, FB, FR), bis="l1"),
    *redet("GU_redetfroh", X1, FB, FR, "g3", "tipp"),
    blase("sprech", 620, 190, "g3", 1560, 190, inhalt=["Also Karten behalten, aber", "mit Fällen abfragen."],
          textsize=36, figur=("GU_redetfroh", X1, FB, FR), bis="tipp"),
]))

# ===========================================================================================================================
# G Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Kein Schema? Die Norm Wort für Wort lesen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Passt kein gelerntes Schema:", 200, 200, "tipp", "Bold", 38),
    *okz("die Norm Wort für Wort lesen", 290, beim("tipp", "lies"), "Bold", 36, x=200),
    *okz("aus jedem Merkmal einen Prüfungspunkt machen", 370, "tipp2", "Bold", 36, x=200),
    *okz("die Norm im Obersatz genau zitieren", 450, beim("tipp3", "zitiere"), "Bold", 36, x=200),
    blk(160, 560, 990, 90, GELB, beim("tipp3", "So"), [("So zeigst du: Du denkst vom Gesetz aus.", "ExtraBold", 36, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Klausurschema: Unterschlagung, § 246 Abs. 1 StGB (aus dem Wortlaut gebaut)
# ===========================================================================================================================
REIHEN = [("s1", "I.", "Tatbestand", BLAU, 0),
          ("s1a", "1.", "objektiv", None, 1),
          ("s1a1", "a)", "fremde bewegliche Sache", None, 2),
          ("s1a2", "b)", "Zueignung (sich oder einem Dritten)", None, 2),
          ("s1a3", "c)", "Rechtswidrigkeit der Zueignung", None, 2),
          ("s1b", "2.", "subjektiv: Vorsatz", None, 1),
          ("s2", "II.", "Rechtswidrigkeit", GRUEN, 0),
          ("s3", "III.", "Schuld", GELB, 0),
          ("s4", "", "Klausel: nur, wenn keine schwerere Vorschrift greift", LILA, 3)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Unterschlagung, § 246 Abs. 1 StGB"), 110, 90, "sch", 50)]
y = 190
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(txt, 255, y + 10, c, "ExtraBold", 38, rechts=1820)]
        y += 88
    elif ebene == 3:
        els_sch.append(blk(110, y + 10, 1300, 80, farbe, c, [(txt, "ExtraBold", 36, INK)]))
        y += 100
    else:
        xr = 270 if ebene == 1 else 350
        els_sch.append(z(r, xr, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(z(txt, xr + 60, y + 2, c, "Bold", 36, rechts=1820))
        y += 64
assert y <= 975, y
folie([("sch", "Klausurschema · § 246 StGB"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s1a", "Klausurschema › I. 1. objektiv"), ("s1b", "Klausurschema › I. 2. subjektiv"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s3", "Klausurschema › III. Schuld"),
       ("s4", "Klausurschema › Subsidiarität")], els_sch)

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein Schema ist kein Gedicht zum Aufsagen,", 0)], [("sondern eine ", 0), ("Landkarte des Gesetzes.", "a")]],
                750, 310, 44, "merke", {"a": beim("merke", "Landkarte")}),
    *markertext([[("Wer weiß, woher jeder Punkt kommt,", 0)], [("findet auch durch ", 0), ("einen neuen Fall.", "b")]],
                750, 560, 44, "mm2", {"b": beim("mm2", "neuen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
