"""Folge 117 · Jura Klausur Fehler: Die 10 häufigsten und wie du sie vermeidest – Serienstandard Open Peeps (Katzenkönig).
Rahmen: Rückgabe einer Übungsklausur im Zivilrecht. Ronja bekommt ihre Arbeit von der Korrektorin Frau Brinkmann zurück;
die Randbemerkungen erscheinen als rote Pillen am Blatt. Übungsfall: Widerruf eines Online-Kaufs (Frau Kröger, Jacke 80 €).
Szenen laut ../SZENENPLAN.md: A1 Rückgabe (Stapel, Arbeit, Blatt mit roten Bemerkungen), A2 Wo gehen die Punkte verloren?,
B Sachverhalt der Übungsklausur, C–L Fehler 1–10 (je Tafel mit Ausschnitt aus Ronjas Klausur, Randbemerkung und
besserer Fassung; Ronja und Frau Brinkmann rechts), M Klausurtipp (Lexi), N Checkliste vor der Abgabe (Schema),
O Merksatz (Lexi).
Ein Handlungsgeräusch (Stapel Klausuren auf dem Tisch; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 114 (gemeinsame Dateien unverändert); neu: blatt() (Klausurausschnitt mit Randlinie und
Randbemerkung), besser(), Zeitstrahl der Frist.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarte wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_117/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_117/" in n:
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
RO_N, BR_N = TUERKIS, LILA                  # Farben der Namensschilder
PX, PY, PU = 1560, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"RO": "Ronja", "BR": "Frau Brinkmann"}
NFARBE = {"RO": RO_N, "BR": BR_N}
HOLZ = (214, 160, 110, 255)
GRAU = (150, 150, 158, 255)


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


def paar(c0, rf, bf, bis=None, ro_bis=None):
    """Tafelszene: Ronja (links) und Frau Brinkmann (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("RO", X1, FB, FR, rf, bis=ro_bis or bis), ns("Ronja", X1, FB, c0, RO_N, d=0.1),
            *fig("BR", X2, FB, FR, bf, bis=bis, d=0.2), ns("Frau Brinkmann", X2, FB, c0, BR_N, d=0.3)]


RAND_X = 820                                # Randlinie des Klausurblatts: rechts davon stehen die Randbemerkungen


def blatt(y, h, cue, zeilen, rand=None, label="Ronja schreibt:", bis=None):
    """Ausschnitt aus Ronjas Klausur: weißes Blatt mit roter Randlinie; zeilen = [(text, cue, stil, size)];
    rand = (text, cue): Randbemerkung der Korrektorin als rote Pille rechts der Randlinie."""
    els = [bis_(karte(110, y, 1040, h, cue, fill=WEISS, rund=14, schatten=6, rand=4), bis),
           bis_(z(label, 140, y + 14, cue, "Bold", 26, farbe=TEXT), bis),
           bis_(linienzug([(RAND_X, y + 12), (RAND_X, y + h - 12)], cue, breite=4, farbe=ROT), bis)]
    yy = y + 56
    for t, c, st, sz in zeilen:
        els.append(bis_(z(t, 140, yy, c, st, sz, rechts=RAND_X - 14), bis))
        yy += int(sz * 1.35)
    assert yy <= y + h, f"Blatt zu kurz: {zeilen[0][0]}"
    if rand:
        t, c = rand
        assert RAND_X + 14 + F("Bold", 28).getlength(t) + 68 <= 1170, f"Randbemerkung zu breit: {t}"
        els.append(bis_(pl(t, RAND_X + 14, y + 50, c, fill=ROT, size=28), bis))
    return els


def besser(y, h, cue, zeilen, bis=None, fill=HELLGRUEN, label="Besser:"):
    """Grüner Kasten mit der besseren Fassung; zeilen = [(text, cue, stil, size)]."""
    els = [bis_(karte(110, y, 1040, h, cue, fill=fill, rund=14, schatten=6, rand=4), bis),
           bis_(ok(150, y + 36, cue, gr=22), bis),
           bis_(z(label, 185, y + 14, cue, "ExtraBold", 32), bis)]
    yy = y + 64
    for t, c, st, sz in zeilen:
        els.append(bis_(z(t, 140, yy, c, st, sz), bis))
        yy += int(sz * 1.35)
    assert yy <= y + h + 4, f"Besser-Kasten zu kurz: {zeilen[0][0]}"
    return els


# ===========================================================================================================================
# A1 Fall: Rückgabe der Übungsklausur
# ===========================================================================================================================
RX, BX = 820, 1600                          # Ronja (blickt nach rechts zu Frau Brinkmann), Frau Brinkmann (blickt nach links)
TISCHX = 1200
tisch = ficon("tabler", "desk", TISCHX, BODEN - 2, 440, NULL, fuell=HOLZ)
TT = int(tisch.y) + 8                       # Tischplatte (Oberkante des Icons)
STAPEL_UNTEN = TT + 4
LANDET = ("korr", 0.4)
rh = hand("RO_ruhig_r", RX, BODEN, FH, +1)
bh = hand("BR_ruhig", BX, BODEN, FH, -1)
STX = TISCHX + 90
stapel = [bis_(ficon("tabler", "files", bh[0] - 50, bh[1] + 40, 110, NULL, fuell=WEISS, anim="cut"), "korr"),
          szene(bewegt(ficon("tabler", "files", STX, STAPEL_UNTEN, 110, "korr", fuell=WEISS, anim="cut"),
                       "korr", LANDET, (bh[0] - 50) - STX, (bh[1] + 40) - STAPEL_UNTEN), "117stapel*", 0.9,
                versatz=0.40 - 0.18)]
GIBT = beim("korr", "gibt")
GIBT_DA = ("korr", round(GIBT[1] + 0.9, 3))
SEITE = (90, 130, 520, 620)                 # großes Klausurblatt links: x, y, w, h
blatt_a = [karte(SEITE[0], SEITE[1], SEITE[2], SEITE[3], "rand", fill=WEISS, rund=12, schatten=8, rand=4),
           z("Übungsklausur Zivilrecht", SEITE[0] + 30, SEITE[1] + 22, "rand", "ExtraBold", 30, rechts=SEITE[0] + SEITE[2] - 20),
           z("Ronja", SEITE[0] + 30, SEITE[1] + 68, "rand", "Bold", 26, farbe=TEXT),
           linienzug([(SEITE[0] + 400, SEITE[1] + 110), (SEITE[0] + 400, SEITE[1] + SEITE[3] - 20)], "rand", breite=4, farbe=ROT)]
for i in range(9):                           # Schreibzeilen (grau)
    yy = SEITE[1] + 130 + i * 52
    blatt_a.append(linienzug([(SEITE[0] + 30, yy), (SEITE[0] + 370 - (i % 3) * 40, yy)], "rand", breite=5, farbe=GRAU))
for i, yy in enumerate([150, 255, 360, 460, 560]):   # rote Randbemerkungen (nur Fragezeichen; Inhalte folgen zum Wort)
    blatt_a.append(pl("?", SEITE[0] + 430, SEITE[1] + yy - 20, beim("rand", "rote"), fill=ROT, size=30, d=0.08 * i))
folie([(NULL, "Fall · Rückgabe der Übungsklausur"), ("r1", "Fall · Fünf Punkte")], [
    hart(boden(NULL)),
    hart(tisch),
    hart(pl("Rückgabe der Übungsklausur · Zivilrecht", 70, 30, NULL, fill=GELB, size=40)),
    *stapel,
    # Frau Brinkmann reicht Ronja die Arbeit über den Tisch
    bis_(ficon("tabler", "file-text", bh[0] - 40, bh[1] + 30, 80, GIBT, fuell=WEISS), GIBT),
    bewegt(bis_(ficon("tabler", "file-text", rh[0] + 40, rh[1] + 30, 80, GIBT, fuell=WEISS, anim="cut"), GIBT_DA),
           GIBT, GIBT_DA, (bh[0] - 40) - (rh[0] + 40), 0),
    ficon("tabler", "file-text", rh[0] + 40, rh[1] + 30, 80, GIBT_DA, fuell=WEISS, anim="cut"),
    *blatt_a,
    pl("5 Punkte", SEITE[0] + 30, SEITE[1] + SEITE[3] - 80, beim("r1", "Fünf"), fill=ROT, size=36),
    # Ronja (links, blickt zu Frau Brinkmann)
    *fig("RO", RX, BODEN, FH, [(NULL, "ruhig_r"), (GIBT_DA, "denkt_r")], erst="cut", bis="r1"),
    hart(ns("Ronja", RX, BODEN, NULL, RO_N)),
    *redet("RO_redet_r", RX, BODEN, FH, "r1", "hook"),
    blase("sprech", 720, 190, "r1", 1080, 235, inhalt=["5 Punkte? Dabei kannte ich", "das Widerrufsrecht genau!"],
          textsize=36, figur=("RO_redet_r", RX, BODEN, FH), bis="hook"),
    # Frau Brinkmann (rechts, blickt zu Ronja)
    *fig("BR", BX, BODEN, FH, [(NULL, "ruhig"), ("korr", "ernst"), (GIBT_DA, "froh")], erst="cut"),
    hart(ns("Frau Brinkmann", BX, BODEN, NULL, BR_N)),
])

# ===========================================================================================================================
# A2 Wo gehen die Punkte verloren?
# ===========================================================================================================================
folie([("hook", "Fall · Wo gehen die Punkte verloren?"), ("zehn", "Fall · Zehn Fehler")], rechts_frei([
    *tafel("hook", "Wo gehen die Punkte verloren?"),
    *neinz("nicht durch Nichtwissen", 190, beim("hook", "Nichtwissen"), "Bold", 38, x=160),
    z("sondern durch Fehler in", 110, 270, beim("hook", "sondern"), "Bold", 36),
    blk(110, 340, 330, 90, BLAU, beim("hook", "Aufbau"), [("Aufbau", "ExtraBold", 38, INK)], anim="pop"),
    blk(465, 340, 330, 90, GELB, beim("hook", "Stil"), [("Stil", "ExtraBold", 38, INK)], anim="pop"),
    blk(820, 340, 330, 90, GRUEN, beim("hook", "Schwerpunkt"), [("Schwerpunkt", "ExtraBold", 38, INK)], anim="pop"),
    z("Davor warnen immer wieder:", 110, 480, "warn", "Bold", 36),
    dicon("tabler", "building-bank", 200, 640, 100, beim("warn", "Prüfungsämter"), fuell=WEISS),
    z("Prüfungsämter", 270, 570, beim("warn", "Prüfungsämter"), "Bold", 34),
    dicon("tabler", "school", 670, 640, 100, beim("warn", "Universitäten"), fuell=WEISS),
    z("Universitäten", 740, 570, beim("warn", "Universitäten"), "Bold", 34),
    zit("in ihren Hinweisen", 270, 625, beim("warn", "Hinweisen")),
    blk(110, 720, 1040, 100, ROT, "zehn", [("10 Fehler in der Klausur von Ronja", "ExtraBold", 40, INK)]),
    *requisit([("hook", ("tabler", "target", 100, WEISS), "Wo bleiben die Punkte?", WEISS),
               ("warn", ("tabler", "alert-triangle", 100, GELB), "Hinweise", GELB)], bis_ende="r2"),
    *paar("hook", [("hook", "sorge"), ("warn", "denkt"), ("zehn", "ernst")], [("hook", "ruhig"), ("warn", "ernst")],
          ro_bis="r2"),
    *redet("RO_redet", X1, FB, FR, "r2", "sv"),
    blase("sprech", 620, 180, "r2", 1560, 200, inhalt=["Welche sind das, und wie", "vermeide ich sie?"],
          textsize=36, figur=("RO_redet", X1, FB, FR), bis="sv"),
]))


# ===========================================================================================================================
# B Sachverhalt der Übungsklausur
# ===========================================================================================================================
def sachverhalt_117(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt der Übungsklausur", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        st = "Regular"
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32, stil=st)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_117("sv", [
    "Frau Kröger kauft am 1. März im Onlineshop eines Modehändlers eine Jacke für 80 Euro und zahlt sofort. "
    "Am 6. März erhält sie die Jacke.",
    "Am 18. März schickt sie die Jacke zurück und schreibt dem Händler per E-Mail: „Ich widerrufe den Kauf.“ "
    "Einen Grund nennt sie nicht. Der Händler erhält die Jacke am 20. März, verweigert aber die Rückzahlung: "
    "Die Frist sei abgelaufen, und ohne Grund gebe es kein Geld zurück.",
    "Bearbeitervermerk: Frau Kröger ist Verbraucherin, der Händler Unternehmer. Gehen Sie davon aus, dass der "
    "Händler ordnungsgemäß über das Widerrufsrecht belehrt hat.",
], "Kann Frau Kröger vom Händler die 80 Euro zurückverlangen?")

# ===========================================================================================================================
# C Fehler 1: Sachverhalt und Bearbeitervermerk
# ===========================================================================================================================
folie([("f1", "1. Sachverhalt und Bearbeitervermerk"), ("f1d", "1. Sachverhalt und Bearbeitervermerk › besser")],
      rechts_frei([
    *tafel("f1", "1. Sachverhalt und Bearbeitervermerk"),
    *neinz("Sachverhalt und Vermerk nicht ausgewertet", 180, beim("f1", "nicht"), "Bold", 34, x=160),
    dicon("tabler", "calendar", 160, 322, 64, beim("f1a", "Kauf"), fuell=WEISS),
    pl("1. März: Kauf", 205, 260, beim("f1a", "Kauf"), fill=WEISS, size=32),
    dicon("tabler", "calendar", 640, 322, 64, beim("f1a", "Lieferung"), fuell=GELB),
    pl("6. März: Lieferung", 685, 260, beim("f1a", "Lieferung"), fill=GELB, size=32),
    bis_(z("Bearbeitervermerk: „… ordnungsgemäß belehrt.“", 110, 350, beim("f1b", "Vermerk"), "Bold", 32), "f1d"),
    *blatt(410, 200, beim("f1a", "Ronja"), [("Die Frist beginnt am 1. März (Kauf).", beim("f1a", "Ronja"), "Regular", 32),
                                           ("Belehrung? … (1 Seite)", beim("f1b", "prüft"), "Regular", 32)],
           rand=("Bearbeitervermerk?", beim("f1c", "Bearbeitervermerk")), bis="f1d"),
    *besser(410, 200, "f1d", [("Den Vermerk zuerst lesen.", "f1d", "Bold", 34),
                              ("Bei jeder Angabe: Wofür brauche ich sie?", beim("f1d", "frag"), "Regular", 32)]),
    blk(110, 650, 1040, 90, GELB, "f1e", [("2 Daten: oft eine Frist", "ExtraBold", 38, INK)]),
    *requisit([("f1", ("tabler", "file-search", 100, WEISS), "Sachverhalt", WEISS),
               ("f1b", ("tabler", "file-alert", 100, GELB), "Bearbeitervermerk", GELB),
               ("f1d", ("tabler", "eye", 100, WEISS), "erst lesen", WEISS)]),
    *paar("f1", [("f1", "ruhig"), ("f1a", "denkt"), (beim("f1c", "Bearbeitervermerk"), "ertappt"), ("f1d", "froh")],
          [("f1", "ruhig"), (beim("f1c", "Bearbeitervermerk"), "ernst"), ("f1d", "froh")]),
]))

# ===========================================================================================================================
# D Fehler 2: die falsche Frage
# ===========================================================================================================================
folie([("f2", "2. Die falsche Frage"), ("f2b", "2. Die falsche Frage › Wer will was von wem woraus?")], rechts_frei([
    *tafel("f2", "2. Die falsche Frage"),
    *blatt(180, 150, beim("f2", "Ronja"), [("Ist der Kaufvertrag wirksam? …", beim("f2", "Ronja"), "Regular", 34)],
           rand=("Frage?", beim("f2a", "Rand"))),
    pl("Gefragt: Bekommt Frau Kröger ihr Geld zurück?", 110, 360, beim("f2a", "Gefragt"), fill=PINK, size=32),
    z("Wer will was von wem woraus?", 110, 455, "f2b", "ExtraBold", 38),
    *besser(530, 330, beim("f2c", "Frau"), [
        ("Frau Kröger könnte gegen den Händler", beim("f2c", "Frau"), "Bold", 34),
        ("einen Anspruch auf Rückzahlung von 80 € haben,", beim("f2c", "Rückzahlung"), "Bold", 34),
        ("aus § 355 Abs. 3 Satz 1 BGB.", beim("f2c", "Paragraf"), "Bold", 34)], label="Besser, der Obersatz:"),
    *requisit([("f2", ("tabler", "file-text", 90, WEISS), "Wirksamkeit?", WEISS),
               (beim("f2a", "Gefragt"), ("tabler", "coin-euro", 100, GELB), "80 € zurück?", PINK),
               ("f2b", ("tabler", "message-question", 100, WEISS), "Wer, was, woraus?", WEISS)]),
    *paar("f2", [("f2", "ruhig"), (beim("f2a", "Rand"), "ertappt"), ("f2b", "denkt"), ("f2c", "froh")],
          [("f2", "ruhig"), (beim("f2a", "Rand"), "ernst"), ("f2c", "froh")]),
]))

# ===========================================================================================================================
# E Fehler 3: der Aufbau (zwei Beispiele aus anderen Klausuren)
# ===========================================================================================================================
LX0, RX0 = 110, 650                         # zwei Spalten
folie([("f3", "3. Der Aufbau"), ("f3a", "3. Der Aufbau › Zivilrecht: Vertrag vor Eigentum"),
       ("f3c", "3. Der Aufbau › Strafrecht: objektiv vor Vorsatz")], rechts_frei([
    *tafel("f3", "3. Der Aufbau"),
    *okz("Ronja: Aufbau richtig", 180, beim("f3", "Ronja"), "Bold", 34, x=160),
    zit("typisch: zwei Beispiele aus anderen Klausuren", 160, 235, beim("f3", "typisch")),
    karte(LX0, 300, 500, 560, "f3a", fill=HELL, rund=14, schatten=6, rand=4),
    z("Zivilrecht", LX0 + 25, 315, "f3a", "ExtraBold", 34, rechts=LX0 + 490),
    z("Vermieter will die", LX0 + 25, 370, "f3a", size=30, rechts=LX0 + 490),
    z("Wohnung zurück", LX0 + 25, 410, "f3a", size=30, rechts=LX0 + 490),
    blk(LX0 + 25, 470, 450, 80, BLAU, beim("f3a", "Vertrag"), [("1. Vertrag, § 546 Abs. 1", "Bold", 30, INK)], anim="pop"),
    blk(LX0 + 25, 570, 450, 80, GELB, beim("f3a", "Eigentum"), [("2. Eigentum, § 985", "Bold", 30, INK)], anim="pop"),
    z("Mietvertrag kann ein Recht", LX0 + 25, 675, "f3b", size=30, rechts=LX0 + 490),
    z("zum Besitz geben", LX0 + 25, 715, "f3b", size=30, rechts=LX0 + 490),
    zit("§ 986 Abs. 1 Satz 1 BGB", LX0 + 25, 765, beim("f3b", "Recht"), rechts=LX0 + 490),
    karte(RX0, 300, 500, 560, "f3c", fill=HELL, rund=14, schatten=6, rand=4),
    z("Strafrecht", RX0 + 25, 315, "f3c", "ExtraBold", 34, rechts=RX0 + 490),
    blk(RX0 + 25, 470, 450, 80, BLAU, beim("f3c", "objektive"), [("1. objektiver Tatbestand", "Bold", 30, INK)], anim="pop"),
    blk(RX0 + 25, 570, 450, 80, GELB, beim("f3c", "Vorsatz"), [("2. Vorsatz", "Bold", 30, INK)], anim="pop"),
    z("Vorsatz bezieht sich auf", RX0 + 25, 675, "f3d", size=30, rechts=RX0 + 490),
    z("die Tatumstände", RX0 + 25, 715, "f3d", size=30, rechts=RX0 + 490),
    zit("§ 16 Abs. 1 Satz 1 StGB", RX0 + 25, 765, beim("f3d", "Tatumstände"), rechts=RX0 + 490),
    *requisit([("f3", ("tabler", "list-numbers", 100, WEISS), "Reihenfolge", WEISS),
               ("f3a", ("tabler", "home", 100, GELB), "Vertrag vor Eigentum", BLAU),
               ("f3c", ("tabler", "scale", 100, WEISS), "objektiv vor Vorsatz", BLAU)]),
    *paar("f3", [("f3", "froh"), ("f3a", "denkt"), ("f3d", "ruhig")], [("f3", "froh"), ("f3a", "ruhig")]),
]))

# ===========================================================================================================================
# F Fehler 4: die Norm genau zitieren
# ===========================================================================================================================
ABSX = [110 + i * 175 for i in range(6)]
FBEG = beim("f4a", "Absatz")
folie([("f4", "4. Die Norm ungenau zitiert"), ("f4a", "4. Die Norm › § 356 Abs. 2 Nr. 1 Buchst. a BGB")], rechts_frei([
    *tafel("f4", "4. Die Norm ungenau zitiert"),
    *blatt(180, 150, beim("f4", "Ronja"), [("Die Frist beginnt nach § 356 BGB …", beim("f4", "Paragraf"), "Regular", 34)],
           rand=("Norm?", beim("f4", "Rand"))),
    z("§ 356 BGB hat 6 Absätze:", 110, 365, "f4a", "Bold", 36),
    *[blk(ABSX[i], 430, 160, 80, WEISS, beim("f4a", "sechs"),
          [(f"Abs. {i + 1}", "Bold", 30, INK)], anim="pop", d=0.06 * i) for i in range(6)],
    blk(ABSX[1], 430, 160, 80, GELB, FBEG, [("Abs. 2", "ExtraBold", 30, INK)], anim="pop"),
    pl("Nr. 1", ABSX[1] + 10, 535, beim("f4a", "Nummer"), fill=GELB, size=30),
    pl("Buchst. a: Erhalt der Ware", ABSX[1] + 140, 535, beim("f4a", "Buchstabe"), fill=GELB, size=30),
    *besser(640, 220, "f4b", [("§ 356 Abs. 2 Nr. 1 Buchst. a BGB", "f4b", "ExtraBold", 36),
                              ("immer Absatz, Satz und Nummer nennen", beim("f4b", "Absatz"), "Regular", 32)]),
    *requisit([("f4", ("tabler", "book", 100, WEISS), "§ 356 BGB?", WEISS),
               ("f4a", ("tabler", "book", 100, GELB), "Abs. 2 Nr. 1 Buchst. a", GELB)]),
    *paar("f4", [("f4", "ruhig"), (beim("f4", "Rand"), "ertappt"), ("f4a", "denkt"), ("f4b", "froh")],
          [("f4", "ruhig"), (beim("f4", "Rand"), "ernst"), ("f4b", "froh")]),
]))

# ===========================================================================================================================
# G Fehler 5: Definition und Subsumtion (§ 312c Abs. 1 BGB als Wortlautkarte)
# ===========================================================================================================================
W312 = ["„Fernabsatzverträge sind Verträge, bei denen der Unternehmer …",
        "und der Verbraucher für die Vertragsverhandlungen und den",
        "Vertragsschluss ausschließlich Fernkommunikationsmittel",
        "verwenden, …“"]
w312, w312_y = wortlaut(110, 250, 1040, W312, "§ 312c Abs. 1 BGB", "f5a", marken=[
    (1, "für die Vertragsverhandlungen und den", beim("f5a", "für")),
    (2, "ausschließlich Fernkommunikationsmittel", beim("f5a", "ausschließlich"))], size=30)
assert w312_y <= 540, w312_y
folie([("f5", "5. Definition und Subsumtion"), ("f5a", "5. Definition › Fernabsatzvertrag, § 312c Abs. 1 BGB"),
       ("f5b", "5. Subsumtion › Fernabsatzvertrag")], rechts_frei([
    *tafel("f5", "5. Definition und Subsumtion"),
    *blatt(180, 130, beim("f5", "Ronja"), [("Es liegt ein Fernabsatzvertrag vor.", beim("f5", "Es"), "Regular", 34)],
           rand=("Definition?", beim("f5", "Rand")), bis="f5a"),
    bis_(pl("nur eine Behauptung", 140, 320, beim("f5", "Behauptung"), fill=ROT, size=30), "f5a"),
    z("Besser:", 150, 190, "f5a", "ExtraBold", 36),
    ok(122, 214, "f5a", gr=20),
    z("1. Definition", 300, 190, "f5a", "Bold", 36),
    *w312,
    z("2. Subsumtion: Frau Kröger hat allein über den", 110, 570, "f5b", "Bold", 34),
    z("Onlineshop bestellt.", 110, 620, beim("f5b", "Onlineshop"), "Bold", 34),
    blk(110, 700, 1040, 80, GRUEN, "f5c", [("3. Ergebnis: also ein Fernabsatzvertrag", "ExtraBold", 36, INK)]),
    *requisit([("f5", ("tabler", "zoom-question", 100, WEISS), "Fernabsatzvertrag?", WEISS),
               ("f5a", ("tabler", "book", 100, WEISS), "§ 312c Abs. 1 BGB", WEISS),
               ("f5b", ("tabler", "shirt", 100, BLAU), "im Onlineshop bestellt", WEISS)]),
    *paar("f5", [("f5", "ruhig"), (beim("f5", "Rand"), "ertappt"), ("f5a", "denkt"), ("f5c", "froh")],
          [("f5", "ruhig"), (beim("f5", "Rand"), "ernst"), ("f5c", "froh")]),
]))

# ===========================================================================================================================
# H Fehler 6: Gutachtenstil am falschen Ort
# ===========================================================================================================================
folie([("f6", "6. Gutachtenstil am falschen Ort"), ("f6c", "6. Gutachtenstil › richtig: umgekehrt")], rechts_frei([
    *tafel("f6", "6. Gutachtenstil am falschen Ort"),
    *blatt(180, 230, "f6a", [("Ein Kaufvertrag könnte geschlossen sein.", "f6a", "Regular", 30),
                             ("Dazu müsste ein Angebot vorliegen …", beim("f6a", "Angebot"), "Regular", 30),
                             ("… Annahme … Also liegt ein Kaufvertrag vor.", beim("f6a", "Annahme"), "Regular", 30)],
           label="Ronja schreibt (klarer Punkt):"),
    pl("klar", RAND_X + 14, 230, beim("f6a", "klar"), fill=GELB, size=30),
    *blatt(435, 150, "f6b", [("Die Frist ist abgelaufen, denn sie beginnt", beim("f6b", "Die"), "Regular", 30),
                             ("mit dem Kauf.", beim("f6b", "Kauf"), "Regular", 30)],
           rand=("Ergebnis vorweg?", beim("f6b", "Rand")), label="Ronja schreibt (das Problem):"),
    *besser(615, 250, "f6c", [("Klares: in einem Satz feststellen", "f6c", "Bold", 34),
                              ("Problem: Gutachtenstil,", "f6d", "Bold", 34),
                              ("das Ergebnis kommt zum Schluss", beim("f6d", "Ergebnis"), "Bold", 34)],
           label="Richtig ist es umgekehrt:"),
    *requisit([("f6", ("tabler", "writing", 100, WEISS), "Gutachten oder Urteil?", WEISS),
               (beim("f6b", "Rand"), ("tabler", "alert-triangle", 100, ROT), "Ergebnis vorweg?", ROT),
               ("f6c", ("tabler", "writing", 100, GRUEN), "umgekehrt", GRUEN)]),
    *paar("f6", [("f6", "ruhig"), ("f6a", "denkt"), (beim("f6b", "Rand"), "ertappt"), ("f6c", "froh")],
          [("f6", "ruhig"), (beim("f6b", "Rand"), "ernst"), ("f6c", "froh")]),
]))

# ===========================================================================================================================
# I Fehler 7: der Schwerpunkt (mit Fristrechnung am Zeitstrahl)
# ===========================================================================================================================
T0, T1, TY = 170, 1090, 480                 # Zeitstrahl 1. bis 20. März
tag = lambda d: T0 + (d - 1) / 19 * (T1 - T0)
F7S = beim("f7a", "Frist")
strahl = [linienzug([(T0 - 20, TY), (T1 + 20, TY)], F7S, breite=5)]
for d_ in range(1, 21):
    strahl.append(linienzug([(tag(d_), TY - (12 if d_ in (1, 6, 18, 20) else 7)), (tag(d_), TY + (12 if d_ in (1, 6, 18, 20) else 7))],
                            F7S, breite=3 if d_ not in (1, 6, 18, 20) else 5))
for d_, txt, c in [(1, "1.", F7S), (6, "6.", beim("f7a", "sechsten")), (18, "18.", beim("f7b", "achtzehnten")),
                   (20, "20.", beim("f7b", "zwanzigsten"))]:
    strahl.append(z(txt, tag(d_) - F("Bold", 28).getlength(txt) / 2, TY + 22, c, "Bold", 28, farbe=TEXT))
FRIST = beim("f7a", "beginnt")
folie([("f7", "7. Der Schwerpunkt verfehlt"), ("f7a", "7. Schwerpunkt › die Frist, § 356 Abs. 2 Nr. 1 Buchst. a BGB")],
      rechts_frei([
    *tafel("f7", "7. Der Schwerpunkt verfehlt"),
    z("Ronja:", 110, 185, beim("f7", "Eine"), "Bold", 32),
    blk(250, 180, 760, 56, WEISS, beim("f7", "Eine"), [("Kaufvertrag: 1 Seite", "Bold", 28, INK)], anim="pop", rand=4),
    blk(250, 250, 160, 56, WEISS, beim("f7", "zwei"), [("Frist", "Bold", 28, INK)], anim="pop", rand=4),
    z("2 Zeilen", 425, 255, beim("f7", "Zeilen"), "Bold", 30, farbe=TEXT),
    pl("Schwerpunkt?", 840, 245, beim("f7", "Rand"), fill=ROT, size=30),
    z("14 Tage, Beginn mit Erhalt der Ware", 110, 320, beim("f7a", "Frist"), "Bold", 34),
    zit("§ 355 Abs. 2 Satz 1, § 356 Abs. 2 Nr. 1 Buchst. a BGB", 110, 368, beim("f7a", "beginnt")),
    *strahl,
    blk(int(tag(6)), TY - 58, int(tag(20) - tag(6)), 44, GELB, FRIST, [("14 Tage", "ExtraBold", 28, INK)], anim="pop"),
    pl("Kauf", tag(1) - 40, TY + 70, F7S, fill=WEISS, size=28),
    pl("Erhalt", tag(6) - 50, TY + 70, beim("f7a", "erhält"), fill=GELB, size=28),
    pl("Widerruf abgesandt", tag(18) - 280, TY + 70, beim("f7b", "Widerruf"), fill=GRUEN, size=28),
    *okz("Fristende 20. März", 630, beim("f7b", "endet"), "Bold", 34, x=160),
    zit("§ 187 Abs. 1, § 188 Abs. 1 BGB", 600, 638, beim("f7b", "zwanzigsten")),
    *okz("Absendung am 18. März: rechtzeitig", 690, beim("f7b", "rechtzeitig"), "Bold", 34, x=160),
    zit("§ 355 Abs. 1 Satz 5 BGB", 160, 740, beim("f7b", "rechtzeitig")),
    *okz("kein Grund nötig", 795, "f7c", "Bold", 34, x=160),
    zit("§ 355 Abs. 1 Satz 4 BGB", 450, 803, beim("f7c", "Grund")),
    *requisit([("f7", ("tabler", "target", 100, WEISS), "Wo ist das Problem?", WEISS),
               ("f7a", ("tabler", "calendar-due", 100, GELB), "die Frist", GELB),
               ("f7c", ("tabler", "mail", 100, WEISS), "ohne Grund", WEISS)]),
    *paar("f7", [("f7", "ruhig"), (beim("f7", "Rand"), "ertappt"), ("f7a", "denkt"), ("f7b", "froh")],
          [("f7", "ruhig"), (beim("f7", "Rand"), "ernst"), ("f7b", "froh")]),
]))

# ===========================================================================================================================
# J Fehler 8: der Meinungsstreit
# ===========================================================================================================================
folie([("f8", "8. Der Meinungsstreit"), ("f8a", "8. Meinungsstreit › Ändert er das Ergebnis?")], rechts_frei([
    *tafel("f8", "8. Der Meinungsstreit"),
    *blatt(180, 230, beim("f8", "Bei"), [("Ansicht 1: …", beim("f8", "zwei"), "Regular", 32),
                            ("Ansicht 2: …", beim("f8", "Ansichten"), "Regular", 32),
                            ("Das ist umstritten.", beim("f8", "umstritten"), "Bold", 32)],
           rand=("Ihre Lösung?", beim("f8", "Rand")), label="Ronja schreibt (Nebenfrage):"),
    blk(110, 440, 1040, 80, GELB, "f8a", [("Ändert der Streit das Ergebnis?", "ExtraBold", 36, INK)]),
    blk(110, 560, 500, 150, WEISS, "f8b", [("gleiches Ergebnis:", "Bold", 30, INK), ("Streit kann", "ExtraBold", 32, INK),
                                          ("dahinstehen", "ExtraBold", 32, INK)]),
    blk(650, 560, 500, 150, GRUEN, "f8c", [("verschiedene Ergebnisse:", "Bold", 30, INK), ("entscheiden,", "ExtraBold", 32, INK),
                                          ("mit Argument", "ExtraBold", 32, INK)]),
    *neinz("nicht nur der Hinweis auf die „herrschende Meinung“", 745, beim("f8c", "nicht"), "Bold", 32, x=160),
    linienzug([(360, 522), (360, 556)], "f8b", breite=5),
    linienzug([(900, 522), (900, 556)], "f8c", breite=5),
    *requisit([("f8", ("tabler", "arrows-split", 100, WEISS), "zwei Ansichten", WEISS),
               ("f8a", ("tabler", "scale", 100, GELB), "Ergebnis anders?", GELB),
               ("f8c", ("tabler", "gavel", 100, HOLZ), "entscheiden", GRUEN)]),
    *paar("f8", [("f8", "ruhig"), (beim("f8", "Rand"), "ertappt"), ("f8a", "denkt"), ("f8c", "froh")],
          [("f8", "ruhig"), (beim("f8", "Rand"), "ernst"), ("f8b", "ruhig"), ("f8c", "froh")]),
]))

# ===========================================================================================================================
# K Fehler 9: die Zeit
# ===========================================================================================================================
folie([("f9", "9. Die Zeit"), ("f9a", "9. Die Zeit › Zeitplan"), ("f9b", "9. Die Zeit › wenn es knapp wird")], rechts_frei([
    *tafel("f9", "9. Die Zeit"),
    *blatt(180, 250, beim("f9", "Für"), [("I. Widerrufsrecht …", beim("f9", "Für"), "Regular", 32), ("II. Frist …", beim("f9", "Für"), "Regular", 32),
                            ("III. Rückzahlung", beim("f9", "Rückzahlung"), "Bold", 32)],
           rand=("Rückzahlung?", beim("f9", "Rand")), label="Ronjas Gliederung:"),
    pl("fehlt ganz", 470, 330, beim("f9", "fehlt"), fill=ROT, size=30),
    *besser(470, 200, "f9a", [("Zeitplan mit Uhrzeiten an der Skizze", "f9a", "Bold", 34),
                              ("wie in Folge 045", beim("f9a", "Folge"), "Regular", 32)]),
    blk(110, 700, 1040, 140, GELB, "f9b", [("Wird es knapp: Gliederung zu Ende,", "Bold", 34, INK),
                                          ("den Rest kurz im Urteilsstil", "Bold", 34, INK)]),
    *requisit([("f9", ("tabler", "hourglass", 100, WEISS), "keine Minute mehr", ROT),
               ("f9a", ("tabler", "clock-hour-4", 100, WEISS), "Uhrzeiten", WEISS),
               ("f9b", ("tabler", "list-check", 100, GELB), "Gliederung zu Ende", GELB)]),
    *paar("f9", [("f9", "sorge"), (beim("f9", "Rand"), "ertappt"), ("f9a", "denkt"), ("f9b", "ruhig")],
          [("f9", "ruhig"), (beim("f9", "Rand"), "ernst"), ("f9a", "froh")]),
]))

# ===========================================================================================================================
# L Fehler 10: das Ergebnis
# ===========================================================================================================================
folie([("f10", "10. Das Ergebnis widerspricht der Prüfung"), ("f10a", "10. Das Ergebnis › folgt aus der Prüfung")],
      rechts_frei([
    *tafel("f10", "10. Ergebnis widerspricht der Prüfung"),
    *blatt(180, 230, beim("f10", "Oben"), [("oben: Frist abgelaufen.", beim("f10", "Oben"), "Bold", 32),
                             ("…", beim("f10", "Unten"), "Regular", 32),
                             ("Ergebnis: Frau Kröger kann die 80 €", beim("f10", "schnell"), "Bold", 32),
                             ("zurückverlangen.", beim("f10", "schnell"), "Bold", 32)],
           rand=("Widerspruch?", beim("f10", "Rand")), label="Ronja schreibt:"),
    z("Das Ergebnis folgt aus der Prüfung darüber.", 110, 445, "f10a", "Bold", 34),
    *okz("richtig gerechnet: Widerruf rechtzeitig", 505, beim("f10a", "Richtig"), "Bold", 34, x=160),
    *besser(580, 220, "f10b", [("Frau Kröger kann vom Händler die", "f10b", "ExtraBold", 34),
                               ("Rückzahlung der 80 € verlangen.", beim("f10b", "Rückzahlung"), "ExtraBold", 34)],
            label="Ergebnis:"),
    *requisit([("f10", ("tabler", "alert-triangle", 100, ROT), "oben anders als unten", ROT),
               ("f10a", ("tabler", "coin-euro", 100, GELB), "80 € zurück", GRUEN)], bis_ende="r3"),
    *paar("f10", [("f10", "ruhig"), (beim("f10", "Rand"), "ertappt"), ("f10a", "denkt"), ("f10b", "froh")],
          [("f10", "ruhig"), (beim("f10", "Rand"), "ernst"), ("f10b", "froh")], ro_bis="r3"),
    *redet("RO_redet", X1, FB, FR, "r3", "tipp"),
    blase("sprech", 620, 180, "r3", 1560, 200, inhalt=["Das nehme ich mir für", "die nächste Klausur vor."],
          textsize=36, figur=("RO_redet", X1, FB, FR), bis="tipp"),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Frage und Ergebnis hintereinander lesen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Vor der Abgabe direkt hintereinander lesen:", 200, 200, beim("tipp", "Lies"), "Bold", 36),
    pl("die Fallfrage", 200, 270, beim("tipp", "Fallfrage"), fill=PINK, size=34),
    pl("dein Ergebnis", 540, 270, beim("tipp", "Ergebnis"), fill=GRUEN, size=34),
    *okz("Passt die Antwort zur Frage?", 380, "tipp2", "Bold", 36, x=200),
    *okz("Trägt die Prüfung darüber genau dieses Ergebnis?", 460, "tipp3", "Bold", 36, x=200),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Checkliste vor der Abgabe (Klausurschema)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Vor dem Schreiben: Bearbeitervermerk, Sachverhalt, Fallfrage", BLAU, 0),
          ("k2", "II.", "Die Gliederung: der richtige Aufbau", GRUEN, 0),
          ("k3", "III.", "Beim Schreiben:", GELB, 0),
          ("k31", "1.", "genaue Normen (Absatz, Satz, Nummer)", None, 1),
          ("k32", "2.", "Definition mit Subsumtion", None, 1),
          ("k33", "3.", "Gutachtenstil nur am Problem", None, 1),
          ("k34", "4.", "dort der Schwerpunkt", None, 1),
          ("k35", "5.", "Streit nur, wenn er das Ergebnis ändert", None, 1),
          ("k4", "IV.", "Am Ende: die Zeit im Blick", LILA, 0),
          ("k41", "", "und ein Ergebnis, das die Frage beantwortet", None, 2)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Checkliste vor der Abgabe"), 110, 90, "sch", 50)]
y = 185
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(txt, 255, y + 10, c, "ExtraBold", 38, rechts=1820)]
        y += 88
    else:
        if r:
            els_sch.append(z(r, 270, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(z(txt, 330 if ebene == 1 else 255, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(ok(230 if ebene == 1 else 215, y + 24, c, gr=18))
        y += 64
assert y <= 975, y
folie([("sch", "Checkliste vor der Abgabe"), ("k1", "Checkliste › I. Vor dem Schreiben"), ("k2", "Checkliste › II. Gliederung"),
       ("k3", "Checkliste › III. Beim Schreiben"), ("k4", "Checkliste › IV. Am Ende")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Punkte holst du ", 0), ("am Problem.", "a")]], 750, 300, 46, "merke", {"a": beim("merke", "am")}),
    *markertext([[("Lies genau, zitiere genau,", 0)], [("und schreib ausführlich nur dort,", 0)],
                 [("wo der Fall es verlangt.", "b")]], 750, 430, 40, "m2", {"b": beim("m2", "Fall")}),
    *markertext([[("Am Ende beantwortest du ", 0), ("die Frage.", "c")]], 750, 720, 42, "m3",
                {"c": beim("m3", "Frage")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
