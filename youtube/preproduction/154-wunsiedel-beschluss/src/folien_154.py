"""Folge 154 · Wunsiedel-Beschluss: Darf ein Gesetz eine Meinung verbieten? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen: Grundrechte-Seminar mit Swantje (Studentin) und Professor Ahlborn; danach der echte Fall sachlich:
BVerfG, Beschl. v. 4.11.2009 – 1 BvR 2150/08, BVerfGE 124, 300 (nur mit Rn.). HÖCHSTE SENSIBILITÄT: keine Figur für
Rudolf Heß, den Veranstalter oder Teilnehmer; keine Darstellung der Veranstaltung, keine Symbole, Fahnen, Uniformen,
Fackeln, Parolen oder Zitate von Teilnehmern; im echten Fall nur neutrale Icons (Ort, Kalender, Behörde, Gesetzbuch,
Gericht, Waage). Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
tisch/requisit/stehend/paar/spricht_neben als eigene Kopie aus Folge 146 (gemeinsame Dateien unverändert).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_154/"

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
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_154/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz2(text, y, cue, kreuz, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Kreuz erst zur gesprochenen Verneinung (kreuz = Cue des Wortes „nicht“)."""
    return [nein(x - 45, y + 20, kreuz, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s






def tisch(x, breite, cue):
    """Schreibtisch aus Grundformen (Holzplatte, zwei Beine) auf dem Boden."""
    im, dr, s = _flaeche(breite, 210)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xx in (o + 30 * s, o + (breite - 52) * s):
        dr.rectangle((xx, o + 34 * s, xx + 22 * s, o + 210 * s), fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((breite + 12, 222), Image.LANCZOS)
    return hart(El(im, x, BODEN - 216, cue, "cut", 0.0, None, name="tisch"))


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SW": "Swantje", "AH": "Prof. Ahlborn"}
NFARBE = {"SW": BLAU, "AH": GRUEN}


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def spricht_neben(k, x, cue, bis, davor, danach, zeilen, size=32, cy=250, w=600, h=200, cx=None):
    """Figur neben der Tafel spricht (Grundbild bis cue, Rede cue→bis, danach Folge); Blase über den Figuren."""
    els = [*fig(k, x, FB, FR, davor, bis=cue)] if davor else []
    els += redet(f"{k}_redet", x, FB, FR, cue, bis)
    els += fig(k, x, FB, FR, danach, erst="cut")
    els.append(blase("sprech", w, h, cue, cx or 1560, cy, inhalt=zeilen, textsize=size, figur=(f"{k}_redet", x, FB, FR),
                     bis=bis))
    return rechts_frei(els)



# ===========================================================================================================================
# A1 Fall: das Grundrechte-Seminar (fiktiv) – Swantje links (blickt nach rechts), Professor Ahlborn rechts (nach links)
# ===========================================================================================================================
SWX, AHX = 720, 1560
TAFEL_S = (60, 60, 560, 330)                # Seminartafel an der Wand (Karte links oben)
TISCH_X, TISCH_B = 880, 420
TISCH_O = BODEN - 216 + 8                   # Oberkante der Tischplatte


def seminartafel(cue, wunsiedel=None):
    """Seminartafel mit Überschrift; ab 'wunsiedel' (Cue) steht dort der Wunsiedel-Beschluss mit Fundstelle."""
    x, y, w, h = TAFEL_S
    els = [hart(karte(x, y, w, h, cue, fill=WEISS, rund=18, schatten=6, rand=4)),
           hart(z("Grundrechte-Seminar", x + 35, y + 18, cue, "ExtraBold", 36, rechts=x + w - 20)),
           hart(linienzug([(x, y + 78), (x + w, y + 78)], cue, breite=4))]
    if wunsiedel:
        c, an = wunsiedel
        els += [z("Wunsiedel-Beschluss", x + 35, y + 92, c, "ExtraBold", 40, rechts=x + w - 20),
                zit("BVerfG, Beschl. v. 4.11.2009", x + 35, y + 152, c, rechts=x + w - 20),
                zit("1 BvR 2150/08 · BVerfGE 124, 300", x + 35, y + 187, c, rechts=x + w - 20),
                ficon("tabler", "scale", x + w - 55, y + 70, 60, c, fuell=GELB)]
        if an == "cut":
            els = [hart(e) for e in els]
    return els


def buch_auf_tisch(cue):
    return hart(ficon("tabler", "book-2", TISCH_X + 210, TISCH_O, 120, cue, fuell=ROT, anim="cut"))


folie([(NULL, "Fall · Das Grundrechte-Seminar"), ("ah1", "Die Frage · Darf ein Gesetz eine Meinung verbieten?"),
       ("klassiker", "Die Frage · Der Wunsiedel-Beschluss")], [
    boden(NULL),
    tisch(TISCH_X, TISCH_B, NULL),
    *seminartafel(NULL, ("klassiker", "pop")),
    # Professor Ahlborn legt das Gesetzbuch auf den Tisch (Buch gleitet von seiner Seite auf die Platte)
    szene(bewegt(ficon("tabler", "book-2", TISCH_X + 210, TISCH_O, 120, "buch", fuell=ROT, anim="cut"),
                 ("buch", 0.25), ("buch", 0.85), 230, -30), "154buch*", 0.9, 0.70),
    # Swantje blickt zu Professor Ahlborn (nach rechts)
    *fig("SW", SWX, BODEN, FH, [(NULL, "ruhig_r"), ("ah1", "denkt_r")], bis="sw1", erst="cut"),
    *redet("SW_redet_r", SWX, BODEN, FH, "sw1", "klassiker"),
    *fig("SW", SWX, BODEN, FH, [("klassiker", "froh_r")], erst="cut"),
    hart(ns("Swantje", SWX, BODEN, NULL, BLAU)),
    # Professor Ahlborn blickt zu Swantje (nach links)
    *fig("AH", AHX, BODEN, FH, [(NULL, "ruhig")], bis="ah1", erst="cut"),
    *redet("AH_redet", AHX, BODEN, FH, "ah1", "sw1"),
    *fig("AH", AHX, BODEN, FH, [("sw1", "denkt"), ("klassiker", "froh")], erst="cut"),
    hart(ns("Prof. Ahlborn", AHX, BODEN, NULL, GRUEN)),
    blase("sprech", 620, 200, "ah1", 1290, 270, inhalt=["Darf ein Gesetz eine bestimmte", "Meinung verbieten?"],
          textsize=31, figur=("AH_redet", AHX, BODEN, FH), bis="sw1"),
    blase("sprech", 680, 200, "sw1", 1150, 280, inhalt=["Eigentlich nicht. Ein Gesetz muss",
                                                     "doch für alle Meinungen gleich gelten."], textsize=30,
          figur=("SW_redet_r", SWX, BODEN, FH), bis="klassiker"),
])

# ===========================================================================================================================
# B1 Der echte Fall: Wunsiedel 2005 (Rn. 1, 7 f., 10, 19) – ohne Figuren, nur neutrale Icons
# ===========================================================================================================================
folie([("stadt", "Der echte Fall · Wunsiedel"), ("anm", "Der echte Fall · Die Anmeldung"),
       ("verbot", "Der echte Fall · Das Verbot")], [
    boden("stadt"),
    pl("Wunsiedel", 70, 40, "stadt", fill=GELB, size=34),
    pl("Hier liegt das Grab von Rudolf Heß, einem führenden Nationalsozialisten", 70, 118, beim("stadt", "Grab"),
       fill=WEISS, size=30),
    pl("Ein Veranstalter meldet jährlich eine Gedenkveranstaltung an", 70, 188, "anm", fill=WEISS, size=30),
    pl("auch für den 20.8.2005", 70, 258, beim("anm", "zwanzigsten"), fill=HELL, size=30),
    pl("Landratsamt: Verbot nach dem Versammlungsgesetz (§ 15 Abs. 1 VersG)", 70, 328, "verbot", fill=HELLROT, size=30),
    pl("Begründung: Es drohe eine Straftat nach § 130 Abs. 4 StGB", 70, 398, "grund", fill=WEISS, size=30),
    zit("BVerfGE 124, 300, Rn. 1, 7 f., 10", 80, 470, "grund"),
    ficon("tabler", "map-pin", 300, BODEN, 150, "stadt", fuell=ROT),
    ficon("tabler", "calendar-event", 740, BODEN, 170, "anm", fuell=WEISS),
    ficon("tabler", "building", 1180, BODEN, 170, "verbot", fuell=BLAUHELL),
    ficon("tabler", "ban", 1330, BODEN - 150, 90, beim("verbot", "verbietet"), fuell=HELLROT),
    ficon("tabler", "book-2", 1640, BODEN, 160, "grund", fuell=ROT),
])

# ===========================================================================================================================
# B2 Der Weg durch die Instanzen, Verfassungsbeschwerde, Frage (Rn. 8 f., 23 f.)
# ===========================================================================================================================
folie([("klage", "Der echte Fall · Drei Instanzen"), ("vb", "Der echte Fall · Verfassungsbeschwerde"),
       ("frage", "Der echte Fall · Die Frage")], [
    *tafel("klage", "Der Weg durch die Instanzen"),
    *neinz("Verwaltungsgericht, 9.5.2006", 185, beim("klage", "drei"), "Bold", 34, x=160),
    *neinz("Verwaltungsgerichtshof, 26.3.2007", 245, beim("klage", "Instanzen"), "Bold", 34, x=160),
    *neinz("Bundesverwaltungsgericht, 25.6.2008", 305, beim("klage", "Bundesverwaltungsgericht"), "Bold", 34, x=160),
    zit("Klage und Rechtsmittel erfolglos · BVerfGE 124, 300, Rn. 8 f.", 160, 360, beim("klage", "Bundesverwaltungsgericht")),
    blk(110, 420, 1040, 80, GELB, "vb", [("Verfassungsbeschwerde", "ExtraBold", 36, INK)]),
    z("§ 130 Abs. 4 StGB sei kein allgemeines Gesetz,", 110, 530, "vbgrund", "Bold", 34),
    z("er richte sich gegen eine politische Richtung", 110, 578, beim("vbgrund", "gegen"), size=34),
    zit("Rn. 23 f.", 110, 628, beim("vbgrund", "gegen")),
    pl("Darf der Gesetzgeber eine Meinung gezielt verbieten?", 110, 700, "frage", fill=PINK, size=34),
    *requisit([("klage", ("tabler", "gavel", 170, HOLZ), "drei Instanzen", WEISS),
               ("vb", ("tabler", "building-bank", 180, WEISS), "Verfassungsbeschwerde", GELB),
               ("frage", ("tabler", "message", 160, PINK), "gezieltes Verbot?", PINK)], pu=640, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_154(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_154("sv", [
    "In der Stadt Wunsiedel liegt das Grab von Rudolf Heß. Ein Veranstalter meldet dort für jedes Jahr bis 2010 eine "
    "Gedenkveranstaltung für Heß unter freiem Himmel an, auch für den 20. August 2005.",
    "Mit Bescheid vom 29. Juni 2005 verbietet das Landratsamt die Veranstaltung und jede Ersatzveranstaltung "
    "(§ 15 Abs. 1 VersG): Es drohe eine Straftat nach § 130 Abs. 4 StGB, der seit dem 1. April 2005 gilt. Eilanträge "
    "bleiben erfolglos. Die Klage scheitert vor dem Verwaltungsgericht (9.5.2006), dem Bayerischen "
    "Verwaltungsgerichtshof (26.3.2007) und dem Bundesverwaltungsgericht (25.6.2008).",
    "Der Veranstalter erhebt Verfassungsbeschwerde: § 130 Abs. 4 StGB sei kein allgemeines Gesetz, weil er sich gegen "
    "eine bestimmte politische Richtung wende.",
], "Ist § 130 Abs. 4 StGB mit Art. 5 Abs. 1 und 2 GG vereinbar?")

# ===========================================================================================================================
# D I. Schutzbereich (Wortlautkarte Art. 5 Abs. 1 Satz 1 GG; Rn. 45, 49 f.)
# ===========================================================================================================================
PI = "I. Schutzbereich"
W5 = ["„(1) Jeder hat das Recht, seine Meinung in Wort, Schrift und",
      "Bild frei zu äußern und zu verbreiten …“"]
w5, w5_y = wortlaut(80, 175, 1100, W5, "Art. 5 Abs. 1 Satz 1 GG (Auszug)", "a5", marken=[
    (1, "äußern", beim("a5", "äußern")), (1, "verbreiten", beim("a5", "verbreiten"))], size=32)
folie([("a5", f"{PI} · Art. 5 Abs. 1 Satz 1 GG"), ("wert", f"{PI} › jede Meinung"),
       ("ns", f"{PI} › auch nationalsozialistisches Gedankengut"), ("art8", f"{PI} › Art. 8 GG im Maßstab des Art. 5 GG")], [
    *tafel("a5", "I. Schutzbereich: die Meinungsfreiheit"),
    *w5,
    *okz("geschützt, ob wertvoll oder wertlos,", w5_y + 25, "wert", "Bold", 34, x=160),
    z("gefährlich oder harmlos", 160, w5_y + 71, beim("wert", "gefährlich"), "Bold", 34),
    zit("BVerfGE 124, 300, Rn. 49", 160, w5_y + 117, beim("wert", "gefährlich")),
    *okz("selbst die Verbreitung nationalsozialistischen", w5_y + 165, "ns", "Bold", 34, x=160),
    z("Gedankenguts: nicht von vornherein ausgenommen", 160, w5_y + 211, beim("ns", "vornherein"), size=34),
    zit("Rn. 50", 160, w5_y + 257, beim("ns", "vornherein")),
    blk(110, w5_y + 300, 1040, 110, BLAUHELL, "art8", [("Verbot wegen des Inhalts: Art. 8 GG", "ExtraBold", 34, INK),
                                                     ("richtet sich hier nach Art. 5 GG", "ExtraBold", 34, INK)]),
    zit("Rn. 45", 110, w5_y + 420, "art8"),
    pl("mehr dazu: Folge zum Brokdorf-Beschluss (Art. 8 GG)", 110, w5_y + 460, "brok", fill=HELL, size=30),
    *requisit([("a5", ("tabler", "message", 100, WEISS), "Meinungsfreiheit", GELB),
               ("wert", ("tabler", "scale", 100, WEISS), "jede Meinung", WEISS),
               ("ns", ("tabler", "shield-check", 100, BLAUHELL), "Schutzbereich (+)", BLAUHELL),
               ("art8", ("tabler", "book", 100, BLAUHELL), "Art. 8 GG", BLAUHELL),
               ("brok", ("tabler", "link", 100, HELL), "Brokdorf-Beschluss", HELL)]),
    *stehend("SW", FX, [("a5", "ruhig"), ("ns", "denkt"), ("art8", "ruhig")]),
])

# ===========================================================================================================================
# E II. Eingriff (Wortlautkarte § 130 Abs. 4 StGB; Rn. 3, 51)
# ===========================================================================================================================
PII = "II. Eingriff"
W130 = ["„(4) Mit Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe",
        "wird bestraft, wer öffentlich oder in einer Versammlung den",
        "öffentlichen Frieden in einer die Würde der Opfer verletzenden",
        "Weise dadurch stört, dass er die nationalsozialistische Gewalt-",
        "und Willkürherrschaft billigt, verherrlicht oder rechtfertigt.“"]
w130, w130_y = wortlaut(80, 175, 1100, W130, "§ 130 Abs. 4 StGB", "p130", marken=[
    (1, "öffentlich oder in einer Versammlung", beim("p130", "öffentlich")),
    (2, "öffentlichen Frieden", beim("p130", "öffentlichen")), (2, "Würde der Opfer", beim("p130", "Würde")),
    (3, "stört", beim("p130", "stört")), (4, "billigt, verherrlicht oder rechtfertigt", beim("p130", "billigt"))], size=31)
folie([("p130", f"{PII} · § 130 Abs. 4 StGB"), ("eingriff", f"{PII} › knüpft am Meinungsinhalt an (+)")], [
    *tafel("p130", "II. Eingriff: § 130 Abs. 4 StGB"),
    *w130,
    *okz("knüpft an den Inhalt einer Meinung an:", w130_y + 35, "eingriff", "Bold", 34, x=160),
    *plusminus("Eingriff in die Meinungsfreiheit", 160, w130_y + 83, beim("eingriff", "greift"), True, size=34, stil="Bold"),
    zit("BVerfGE 124, 300, Rn. 51; Wortlaut Rn. 3", 160, w130_y + 133, beim("eingriff", "greift")),
    *requisit([("p130", ("tabler", "book-2", 100, ROT), "§ 130 Abs. 4 StGB", WEISS),
               ("eingriff", ("tabler", "alert-triangle", 100, HELLROT), "Eingriff (+)", HELLROT)]),
    *stehend("AH", FX, [("p130", "ruhig"), ("eingriff", "ernst")]),
])

# ===========================================================================================================================
# F III. Rechtfertigung: allgemeine Gesetze (Wortlautkarte Art. 5 Abs. 2 GG; Rn. 54–58; BVerfGE 7, 198 <209 f.>)
# ===========================================================================================================================
PIII = "III. Rechtfertigung"
W52 = ["„(2) Diese Rechte finden ihre Schranken in den Vorschriften",
       "der allgemeinen Gesetze …“"]
w52, w52_y = wortlaut(80, 175, 1100, W52, "Art. 5 Abs. 2 GG (Auszug)", "a52", marken=[
    (0, "Schranken", beim("a52", "Schranken")), (1, "allgemeinen Gesetze", beim("a52", "allgemeinen"))], size=32)
folie([("a52", f"{PIII} · Art. 5 Abs. 2 GG"), ("sonder", f"{PIII} › Sonderrechtslehre"),
       ("abwl", f"{PIII} › Abwägungslehre"), ("kombi", f"{PIII} › Kombination durch das BVerfG"),
       ("blind", f"{PIII} › meinungsneutral")], [
    *tafel("a52", "III. Rechtfertigung: allgemeine Gesetze"),
    *w52,
    pl("Wann ist ein Gesetz allgemein?", 110, w52_y + 22, "wann", fill=PINK, size=34),
    blk(110, w52_y + 105, 505, 150, BLAUHELL, "sonder", [("Sonderrechtslehre", "ExtraBold", 32, INK),
                                                       ("nicht gegen eine Meinung", "Regular", 30, INK),
                                                       ("als solche gerichtet", "Regular", 30, INK)]),
    blk(645, w52_y + 105, 505, 150, LILAHELL, "abwl", [("Abwägungslehre", "ExtraBold", 32, INK),
                                                     ("Rechtsgut mit Vorrang", "Regular", 30, INK),
                                                     ("vor der Meinungsfreiheit", "Regular", 30, INK)]),
    ok(568, w52_y + 125, beim("kombi", "nicht"), gr=22),                    # Element der Sonderrechtslehre
    ok(1103, w52_y + 125, beim("kombi", "Vorrang"), gr=22),                 # Element der Abwägungslehre
    blk(110, w52_y + 280, 1040, 80, HELLGRUEN, "kombi", [("BVerfG verbindet beides, schon im Lüth-Urteil", "ExtraBold", 32, INK)]),
    zit("BVerfGE 7, 198 <209 f.>; BVerfGE 124, 300, Rn. 54", 110, w52_y + 370, "kombi"),
    pl("meinungsneutral: blind gegenüber denen, auf die es angewendet wird", 110, w52_y + 415, "blind", fill=GELB, size=28),
    zit("Rn. 58", 110, w52_y + 480, "blind"),
    *requisit([("a52", ("tabler", "book", 100, WEISS), "Art. 5 Abs. 2 GG", GELB),
               ("sonder", ("tabler", "ban", 90, BLAUHELL), "Sonderrecht?", BLAUHELL),
               ("abwl", ("tabler", "scale", 100, LILAHELL), "Vorrang?", LILAHELL),
               ("kombi", ("tabler", "circle-check", 90, HELLGRUEN), "beides", HELLGRUEN),
               ("blind", ("tabler", "eye-off", 100, GELB), "meinungsneutral", GELB)]),
    *paar("SW", [("a52", "ruhig"), ("sonder", "denkt"), ("blind", "froh")],
          "AH", [("a52", "ruhig"), ("kombi", "froh"), (beim("kombi", "Vorrang"), "ernst")]),
])

# ===========================================================================================================================
# G § 130 Abs. 4 StGB ist kein allgemeines Gesetz (Rn. 10, 61–63)
# ===========================================================================================================================
folie([("bverwg", f"{PIII} › § 130 Abs. 4 StGB allgemein?"), ("nur", f"{PIII} › nur eine Haltung zum Nationalsozialismus"),
       ("sonderr", f"{PIII} › Sonderrecht"), ("ehre", f"{PIII} › auch kein Ehrschutz")], [
    *tafel("bverwg", "Ist § 130 Abs. 4 StGB allgemein?"),
    z("Bundesverwaltungsgericht: ja, allgemeines Gesetz", 110, 175, "bverwg", "Bold", 34),
    zit("BVerfGE 124, 300, Rn. 10", 110, 223, "bverwg"),
    blk(110, 268, 1040, 72, HELLROT, "nein", [("Bundesverfassungsgericht: nein", "ExtraBold", 34, INK)]),
    *okz("schützt den öffentlichen Frieden, auch sonst geschützt", 360, "frieden", size=33),
    *neinz("aber nur Äußerungen mit einer bestimmten", 420, "nur", "Bold", 33),
    z("Haltung zum Nationalsozialismus", 185, 465, beim("nur", "Haltung"), "Bold", 33),
    z("nicht: Gutheißung anderer totalitärer Regime", 185, 510, beim("nur", "nicht"), size=33),
    *neinz("Antwort auf Versammlungen von Rechtsradikalen,", 570, "antwort", "Bold", 33),
    z("gerade auch in Wunsiedel", 185, 615, beim("antwort", "gerade"), size=33),
    blk(110, 665, 1040, 72, ROT, "sonderr", [("Sonderrecht, kein allgemeines Gesetz", "ExtraBold", 34, INK)]),
    zit("Rn. 61", 110, 745, "sonderr"),
    *neinz2("auch nicht: Schranke der persönlichen Ehre", 790, "ehre", beim("ehre", "nicht"), size=33),
    zit("Rn. 62 f.", 900, 798, "ehre"),
    *requisit([("bverwg", ("tabler", "gavel", 110, HOLZ), "BVerwG: allgemein", WEISS),
               ("nein", ("tabler", "building-bank", 110, WEISS), "BVerfG: nein", HELLROT),
               ("sonderr", ("tabler", "ban", 90, HELLROT), "Sonderrecht", HELLROT)]),
    *paar("SW", [("bverwg", "ruhig"), ("nein", "denkt"), ("sonderr", "sorge")],
          "AH", [("bverwg", "ernst"), ("frieden", "ruhig"), ("sonderr", "ernst")]),
])

# ===========================================================================================================================
# H1 Die Wunsiedel-Ausnahme (Leitsatz 1, Rn. 52, 64–66)
# ===========================================================================================================================
LS1 = ["„… ist Art. 5 Abs. 1 und 2 GG für Bestimmungen, die der",
       "propagandistischen Gutheißung der nationalsozialistischen",
       "Gewalt- und Willkürherrschaft Grenzen setzen, eine Ausnahme",
       "vom Verbot des Sonderrechts für meinungsbezogene Gesetze",
       "immanent.“"]
ls1, ls1_y = wortlaut(80, 265, 1100, LS1, "BVerfGE 124, 300, Leitsatz 1 (Rn. 64)", "zitat", marken=[
    (1, "propagandistischen Gutheißung", beim("zitat", "propagandistischen")),
    (2, "Ausnahme", beim("zitat", "Ausnahme")), (4, "immanent", beim("zitat", "immanent"))], size=31)
folie([("sw2", f"{PIII} › Sonderrecht verfassungswidrig?"), ("ah2", f"{PIII} › die Wunsiedel-Ausnahme"),
       ("unrecht", f"{PIII} › Grund der Ausnahme")], [
    *tafel("sw2", "Ist Sonderrecht verfassungswidrig?"),
    blk(110, 172, 1040, 72, GELB, beim("ah2", "Ausnahme"), [("Nein: Das Gericht erkennt eine Ausnahme an.", "ExtraBold", 34, INK)]),
    *ls1,
    z("Grund: einzigartiges Unrecht und Schrecken", 110, ls1_y + 25, "unrecht", "Bold", 34),
    z("Grundgesetz: geradezu ein Gegenentwurf dazu", 110, ls1_y + 73, "gegen", "Bold", 34),
    z("Gutheißung: Angriff auf die Identität des", 110, ls1_y + 121, "identi", "Bold", 34),
    z("Gemeinwesens, mit friedensbedrohendem Potenzial", 110, ls1_y + 167, beim("identi", "Gemeinwesens"), size=33),
    zit("Rn. 52, 65 f.", 110, ls1_y + 215, beim("identi", "Gemeinwesens")),
    *spricht_neben("SW", X1, "sw2", "ah2", [], [("ah2", "denkt"), ("identi", "ruhig")],
                   ["Dann wäre das Verbot", "doch verfassungswidrig?"], size=32),
    ns("Swantje", X1, FB, "sw2", BLAU, d=0.1),
    *spricht_neben("AH", X2, "ah2", "zitat", [("sw2", "ruhig")], [("zitat", "ernst")],
                   ["Nein. Das Gericht erkennt", "eine Ausnahme an."], size=32),
    ns("Prof. Ahlborn", X2, FB, "sw2", GRUEN, d=0.1),
])

# ===========================================================================================================================
# H2 Grenzen der Ausnahme (Leitsatz 2, Rn. 66–68)
# ===========================================================================================================================
folie([("ah3", f"{PIII} › Grenzen der Ausnahme"), ("geist", f"{PIII} › kein Verbot wegen geistiger Wirkung"),
       ("vhm", f"{PIII} › auch Sonderrecht verhältnismäßig")], [
    *tafel("ah3", "Grenzen der Ausnahme"),
    *neinz("nicht übertragbar auf andere Meinungen", 185, beim("ah3", "andere"), "Bold", 34),
    zit("BVerfGE 124, 300, Rn. 66", 185, 233, beim("ah3", "andere")),
    *neinz2("kein Verbot von rechtsradikalem oder", 300, "geist", beim("geist", "nicht"), "Bold", 34),
    z("nationalsozialistischem Gedankengut", 185, 346, beim("geist", "nationalsozialistisches"), "Bold", 34),
    z("allein wegen seiner geistigen Wirkung", 185, 392, beim("geist", "geistigen"), size=34),
    zit("Leitsatz 2; Rn. 67", 185, 440, beim("geist", "geistigen")),
    *okz("auch Sonderrecht muss verhältnismäßig sein", 505, "vhm", "Bold", 34),
    zit("Rn. 68", 185, 553, "vhm"),
    *spricht_neben("AH", FX, "ah3", "geist", [], [("geist", "ernst"), ("vhm", "ruhig")],
                   ["Aber Vorsicht: Für andere", "Meinungen gilt diese", "Ausnahme nicht."], size=32, h=230),
    ns("Prof. Ahlborn", FX, FB, "ah3", GRUEN, d=0.1),
    *requisit([("geist", ("tabler", "message", 100, WEISS), "geistige Wirkung", WEISS),
               ("vhm", ("tabler", "scale", 100, GELB), "verhältnismäßig", GELB)]),
])

# ===========================================================================================================================
# I1 Verhältnismäßigkeit: der öffentliche Friede (Rn. 69–85)
# ===========================================================================================================================
PV = f"{PIII} › Verhältnismäßigkeit"
folie([("zweck", f"{PV}: öffentlicher Friede"), ("kein", f"{PV} › nicht: Schutz vor Beunruhigung"),
       ("friedl", f"{PV} › Friedlichkeit"), ("gea", f"{PV} › geeignet, erforderlich, angemessen")], [
    *tafel("zweck", "Verhältnismäßigkeit: öffentlicher Friede"),
    z("legitimer Zweck: öffentlicher Friede, eng verstanden", 110, 175, "zweck", "Bold", 34),
    zit("BVerfGE 124, 300, Rn. 70, 76", 110, 223, "zweck"),
    *neinz("nicht: Schutz vor beunruhigenden Meinungen", 285, "kein", "Bold", 34),
    z("oder vor einer „Vergiftung des geistigen Klimas“", 185, 331, beim("kein", "Vergiftung"), size=33),
    zit("Rn. 77", 185, 379, beim("kein", "Vergiftung")),
    *okz("sondern: Friedlichkeit, Schutz vor Äußerungen,", 440, "friedl", "Bold", 34),
    z("die auf Aggression oder Rechtsbruch angelegt sind", 185, 486, beim("friedl", "Aggression"), size=33),
    zit("Rn. 78", 185, 534, beim("friedl", "Aggression")),
    pl("geeignet", 110, 595, beim("gea", "geeignet"), fill=HELLGRUEN, size=32),
    pl("erforderlich", 320, 595, beim("gea", "erforderlich"), fill=HELLGRUEN, size=32),
    pl("angemessen", 585, 595, beim("gea", "angemessen"), fill=HELLGRUEN, size=32),
    zit("Rn. 80–85", 110, 670, beim("gea", "angemessen")),
    *requisit([("zweck", ("tabler", "scale", 100, WEISS), "öffentlicher Friede", WEISS),
               ("kein", ("tabler", "ban", 90, HELLROT), "nicht: Beunruhigung", HELLROT),
               ("friedl", ("tabler", "shield-check", 100, HELLGRUEN), "Friedlichkeit", HELLGRUEN)]),
    *paar("SW", [("zweck", "ruhig"), ("kein", "denkt"), ("friedl", "froh")],
          "AH", [("zweck", "ruhig"), ("gea", "froh")]),
])

# ===========================================================================================================================
# I2 Vermutete Friedensstörung, untypische Fälle, Wechselwirkung (Rn. 95, 97 f., 103)
# ===========================================================================================================================
folie([("verm", f"{PV} › Störung vermutet"), ("atyp", f"{PV} › untypische Fälle"),
       ("ww", f"{PIII} › Auslegung: Wechselwirkung")], [
    *tafel("verm", "Störung des öffentlichen Friedens"),
    blk(110, 175, 1040, 120, GELB, "verm", [("Bei einer Billigung kann die Störung", "ExtraBold", 34, INK),
                                          ("grundsätzlich vermutet werden", "ExtraBold", 34, INK)]),
    zit("BVerfGE 124, 300, Rn. 95, 103", 110, 308, "verm"),
    *neinz("außer in untypischen Fällen,", 370, "atyp", "Bold", 34),
    z("etwa bei kleinen geschlossenen Versammlungen", 185, 416, beim("atyp", "kleinen"), size=34),
    zit("Rn. 103", 185, 464, beim("atyp", "kleinen")),
    blk(110, 530, 1040, 120, PINK, "ww", [("Wechselwirkung: Auslegung im Licht", "ExtraBold", 34, INK),
                                        ("der Meinungsfreiheit", "ExtraBold", 34, INK)]),
    zit("Rn. 97 f.; zur Wechselwirkung: Folge zum Lüth-Urteil", 110, 663, "ww"),
    *requisit([("verm", ("tabler", "scale", 100, GELB), "Vermutung", GELB),
               ("atyp", ("tabler", "search", 100, WEISS), "untypischer Fall", WEISS),
               ("ww", ("tabler", "arrows-exchange", 100, PINK), "Wechselwirkung", PINK)]),
    *stehend("SW", FX, [("verm", "denkt"), ("ww", "froh")]),
])

# ===========================================================================================================================
# J Anwendung im Fall, Ergebnis (Rn. 47, 101, 105–110; Entscheidungsformel)
# ===========================================================================================================================
PA = "Anwendung im Fall"
folie([("anw", f"{PA} · Billigung durch eine Ehrung?"), ("person", f"{PA} › nicht: Lob nur der Person"),
       ("vertretbar", f"{PA} › Würdigung vertretbar"), ("erg", "Ergebnis · Verfassungsbeschwerde zurückgewiesen")], [
    *tafel("anw", "Im Fall: Billigung durch eine Ehrung?"),
    *okz("Ehrung einer Person kann Billigung sein,", 180, "symbol", "Bold", 34),
    z("wenn sie als Symbolfigur für die national-", 185, 226, beim("symbol", "Symbolfigur"), size=34),
    z("sozialistische Herrschaft als solche steht", 185, 272, beim("symbol", "Symbolfigur"), size=34),
    zit("BVerfGE 124, 300, Rn. 101, 107", 185, 320, beim("symbol", "Symbolfigur")),
    *neinz2("ein Lob, das nur der Person gilt: reicht nicht", 385, "person", beim("person", "nicht"), "Bold", 34),
    zit("Rn. 107", 185, 433, "person"),
    *okz("BVerwG durfte annehmen: Billigung der", 495, "vertretbar", "Bold", 34),
    z("nationalsozialistischen Herrschaft im Ganzen", 185, 541, beim("vertretbar", "Ganzen"), size=34),
    zit("Rn. 108", 185, 589, beim("vertretbar", "Ganzen")),
    blk(110, 645, 1040, 80, GRUEN, "erg", [("Die Verfassungsbeschwerde wird zurückgewiesen.", "ExtraBold", 34, INK)]),
    zit("BVerfGE 124, 300 (Entscheidungsformel); Rn. 47, 105", 110, 740, "erg"),
    *requisit([("anw", ("tabler", "search", 100, WEISS), "im Fall", WEISS),
               ("vertretbar", ("tabler", "scale", 100, WEISS), "vertretbar", WEISS),
               ("erg", ("tabler", "gavel", 110, HOLZ), "zurückgewiesen", GRUEN)]),
    *paar("SW", [("anw", "denkt"), ("erg", "ruhig")], "AH", [("anw", "ruhig"), ("vertretbar", "ernst")]),
])

# ===========================================================================================================================
# K Zurück im Seminar (gleicher Schauplatz wie A1: die Geschichte kehrt zur Ausgangsfrage zurück)
# ===========================================================================================================================
x_, y_, w_, h_ = TAFEL_S
folie([("sw3", "Zurück im Seminar · Die Frage"), ("ah4", "Zurück im Seminar · Die Antwort")], [
    boden("sw3"),
    tisch(TISCH_X, TISCH_B, "sw3"),
    *seminartafel("sw3", ("sw3", "cut")),
    z("Nur in der Ausnahme.", x_ + 35, y_ + 225, beim("ah4", "Nur"), "Bold", 30, rechts=x_ + w_ - 100),
    z("Sonst: meinungsneutral.", x_ + 35, y_ + 265, beim("ah4", "meinungsneutral"), "Bold", 30, rechts=x_ + w_ - 100),
    buch_auf_tisch("sw3"),
    *redet("SW_redet_r", SWX, BODEN, FH, "sw3", "ah4"),
    *fig("SW", SWX, BODEN, FH, [("ah4", "denkt_r"), (beim("ah4", "meinungsneutral"), "froh_r")], erst="cut"),
    hart(ns("Swantje", SWX, BODEN, "sw3", BLAU)),
    *fig("AH", AHX, BODEN, FH, [("sw3", "ruhig")], bis="ah4", erst="cut"),
    *redet("AH_redet", AHX, BODEN, FH, "ah4", "tipp"),
    hart(ns("Prof. Ahlborn", AHX, BODEN, "sw3", GRUEN)),
    blase("sprech", 680, 200, "sw3", 1150, 280, inhalt=["Also darf ein Gesetz eine", "bestimmte Meinung verbieten?"],
          textsize=31, figur=("SW_redet_r", SWX, BODEN, FH), bis="ah4"),
    blase("sprech", 620, 200, "ah4", 1290, 270, inhalt=["Nur in dieser einen Ausnahme.", "Sonst muss es",
                                                     "meinungsneutral sein."], textsize=31,
          figur=("AH_redet", AHX, BODEN, FH), bis="tipp"),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi) – Prüfungsreihenfolge bei Art. 5 Abs. 2 GG (Rn. 61, 64, 66)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst: allgemeines Gesetz?"), ("tipp2", "Klausurtipp · sonst Sonderrecht"),
       ("tipp3", "Klausurtipp · Ausnahme nicht übertragen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Art. 5 Abs. 2 GG: zuerst prüfen,", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("ob das Gesetz allgemein ist", 200, 250, beim("tipp", "allgemein"), "Bold", 36),
    *neinz("wenn nicht: Sonderrecht, grundsätzlich unzulässig", 330, "tipp2", size=34, x=200),
    linienzug([(130, 410), (1130, 410)], "tipp3", breite=3),
    *neinz2("Wunsiedel-Ausnahme nicht auf andere", 440, "tipp3", beim("tipp3", "nicht"), "Bold", 34, x=200),
    z("Meinungen übertragen", 200, 488, beim("tipp3", "andere"), "Bold", 34),
    zit("BVerfGE 124, 300, Rn. 61, 64, 66", 200, 538, beim("tipp3", "andere")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich, Art. 5 Abs. 1 Satz 1 GG", True),
          (beim("k1", "verfassungsfeindliche"), 1, "auch verfassungsfeindliche Meinungen", False),
          ("k2", 0, "II. Eingriff", True),
          ("k3", 0, "III. Rechtfertigung", True),
          ("k3a", 1, "1. allgemeines Gesetz, also meinungsneutral?", False),
          ("k4", 1, "2. wenn nein: Sonderrecht, zulässig nur in der Wunsiedel-Ausnahme", False),
          ("k5", 1, "3. Verhältnismäßigkeit, enger Begriff des öffentlichen Friedens", False),
          ("k6", 1, "4. Auslegung im Licht der Meinungsfreiheit", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Meinungsfreiheit, Art. 5 GG"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 88, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k3a", "Prüfschema › III. 1. allgemeines Gesetz?"),
       ("k4", "Prüfschema › III. 2. Sonderrecht, Wunsiedel-Ausnahme"), ("k5", "Prüfschema › III. 3. Verhältnismäßigkeit"),
       ("k6", "Prüfschema › III. 4. Auslegung")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein Gesetz, das sich gegen eine bestimmte", 0)], [("Meinung richtet, ist ", 0),
                 ("kein allgemeines Gesetz", "a"), (".", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "kein")}),
    *markertext([[("Erlaubt ist solches Sonderrecht ", 0), ("nur", "b"), (" gegen die", 0)],
                 [("Gutheißung der nationalsozialistischen", 0)], [("Gewalt- und Willkürherrschaft,", 0)],
                 [("und auch dann nur verhältnismäßig.", 0)]], 750, 480, 42, "m2",
                {"b": beim("m2", "nur")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
