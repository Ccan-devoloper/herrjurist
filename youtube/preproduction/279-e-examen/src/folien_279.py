"""Folge 279 · E-Examen Jura: Klausuren am Computer schreiben – Serienstandard Open Peeps (Katzenkönig).
Rahmen: fiktiver Prüfungssaal mit Laptops; Telse (Jurastudentin in Nordrhein-Westfalen) schreibt bald ihre Examensklausuren,
ihr Bruder Jost hat das zweite Examen in Bayern am Laptop geschrieben.
Szenen laut ../SZENENPLAN.md: A1 Prüfungssaal, A2 Einstieg, B Sachverhalt, C Rechtsgrundlage (Wortlautkarte § 5d Abs. 6
DRiG), D Länderbeispiele (§§ 10 I, 51 I JAG NRW und LJPA NRW; LJPA Bayern), E1 Was ändert sich (Gliederung, Umstellen,
Rechtschreibprüfung), E2 Zeit und Lesbarkeit, F Was bleibt, G Vorbereitung, H Ergebnis (Saal, Telse am Laptop),
I Klausurtipp (Lexi), J E-Examen in 5 Schritten, K Merksatz (Lexi).
Handlungsgeräusch: Telse tippt die ersten Sätze (H); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/redet/fig/ns/okz/neinz/requisit/
wortlaut/kasten/pm als eigene Kopie aus Folge 273 (gemeinsame Dateien unverändert); neu: tisch(), saal(), bildschirm(),
schirm_*(), landblock().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Laptops, Tastaturen und Programme ohne Marken oder Logos.
Normangaben nach gesetze-im-internet.de und recht.nrw.de, Länderangaben nach den Seiten der Landesjustizprüfungsämter
NRW (justiz.nrw) und Bayern (justiz.bayern.de), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_279/"

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
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
HELLBLAU = (226, 236, 252, 255)
HGELB = (253, 240, 196, 255)
HROT = (252, 214, 206, 255)
GRAU = (200, 200, 196, 255)
GRAU2 = (232, 232, 228, 255)
HOLZ = (214, 160, 110, 255)
HOLZ2 = (176, 122, 80, 255)
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


def zit(text, x, y, cue, size=28, **k):
    """Fundstellen-/Verweiszeile (grau, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_279/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180/201/237) ---------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def ticon(*a, **k):
    """Icon als Teil einer Tafelgrafik (darf in der Tafel stehen, rechts_frei() prüft nur Requisiten neben der Tafel)."""
    e = ficon(*a, **k)
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


# --- Figuren neben der Tafel ----------------------------------------------------------------------------------------------
X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Unterkante, Höhe neben der Tafel
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TE": "Telse", "TS": "Telse", "JO": "Jost"}
NFARBE = {"TE": LILA, "TS": LILA, "JO": TUERKIS}


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)];
    ein Eintrag (cue, None, None, None) beendet das vorige Requisit (z. B. vor einer Sprechblase)."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def allein(k, folge):
    return stehend(k, FX, folge)




ZITAT = (246, 246, 250, 255)
KORK = (214, 170, 120, 255)
WAND = (238, 232, 220, 255)


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
    """Wortlautkarte (wie Folge 201): Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit
    Normangabe; marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die erste noch nicht
    markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
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


def kasten(x, y, w, h, fill, c, rund=14, rand=4, anim="pop", bis=None, name="kasten"):
    """Leerer Tabellen-/Zellenkasten (Text kommt zeilenweise mit z())."""
    def zz(dr, s):
        dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return El(_flaeche(w, h, zz), x, y, c, anim, 0.0, bis, name=name)


def pm(text, x, y, cue, plus, size=32, stil="Bold", rechts=1170):
    """Zeile mit (+)/(−) in Dunkelgrün/Dunkelrot (Bewertung zur gesprochenen Chance bzw. zum Risiko)."""
    zei = "(+)" if plus else "(−)"
    a = z(zei, x, y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT))
    b = z(text, x + 70, y, cue, stil, size, rechts=rechts)
    return [a, b]



# --- Prüfungssaal: Boden, Tische mit Laptops und Büchern (programmatisch bzw. Tabler-Icons) --------------------------------
BODEN_Y = 905
FHA = 480
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
TEX, JOX = 380, 1610                         # Telse (links, blickt nach rechts), Jost (rechts, blickt nach links)
TISCH_Y = 650
TISCHE = [(640, 380), (1080, 380)]          # x, Breite
LAPTOP = [(800, 210), (1240, 210)]          # Laptop-Mitte, Breite (auf dem Tisch)


def boden(c):
    return hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], c, breite=7, farbe=INK))


def tisch(c, x0, w, name="tisch"):
    h = BODEN_Y - TISCH_Y
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, 30 * s), fill=HOLZ, outline=INK, width=5 * s)
        for lx in (26, w - 46):
            dr.rectangle((lx * s, 28 * s, (lx + 20) * s, (h - 1) * s), fill=HOLZ2, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, TISCH_Y, c, "cut", 0.0, None, name=name))


def saal(c, buecher=True):
    els = [boden(c)]
    for i, ((x0, w), (lx, lb)) in enumerate(zip(TISCHE, LAPTOP)):
        els.append(tisch(c, x0, w, name=f"tisch:{i}"))
        els.append(hart(ficon("tabler", "device-laptop", lx, TISCH_Y + 6, lb, c, fuell=HELLBLAU, anim="cut")))
        if buecher:
            els.append(hart(ficon("tabler", "books", x0 + w - 60, TISCH_Y + 6, 90, c, fuell=GELB, anim="cut")))
    return els


# --- Bildschirm-Skizze in der Tafel (keine echte Software, keine Marken) ---------------------------------------------------
SCH = (760, 200, 390, 260)                  # x, y, w, h des Bildschirms in der Tafel


def bildschirm(c, bis=None, x=SCH[0], y=SCH[1], w=SCH[2], h=SCH[3]):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 14 * s, fill=INK)
        dr.rectangle((16 * s, 16 * s, (w - 16) * s, (h - 16) * s), fill=WEISS)
    def fuss(dr, s):
        dr.polygon([(30 * s, 3 * s), ((w + 30) * s, 3 * s), ((w + 60) * s, 26 * s), (0, 26 * s)], fill=GRAU, outline=INK)
        dr.line([(30 * s, 3 * s), ((w + 30) * s, 3 * s), ((w + 60) * s, 26 * s), (0, 26 * s), (30 * s, 3 * s)], fill=INK, width=4 * s)
    return [bis_(kasten_bild(_flaeche(w, h, zz), x, y, c, "schirm"), bis),
            bis_(kasten_bild(_flaeche(w + 60, 30, fuss), x - 30, y + h - 4, c, "schirm:fuss"), bis)]


def kasten_bild(im, x, y, c, name, anim="pop"):
    return El(im, x, y, c, anim, 0.0, None, name=name)


def schirm_inhalt(art, c, bis=None):
    """Inhalt des Bildschirms je Zustand: 'gliederung', 'umstellen', 'rechtschreibung', 'ausdruck'."""
    x, y, w, h = SCH
    iw, ih = w - 32, h - 32
    def zz(dr, s):
        f = F("ExtraBold", 26 * s)
        def linie(xx, yy, ll, farbe=GRAU):
            dr.line((xx * s, yy * s, (xx + ll) * s, yy * s), fill=farbe, width=5 * s)
        if art == "gliederung":
            for i, (pre, ein, ll) in enumerate([("A.", 0, 240), ("I.", 34, 200), ("1.", 68, 180), ("2.", 68, 160)]):
                yy = 14 + i * 52
                dr.text(((14 + ein) * s, yy * s), pre, font=f, fill=INK)
                linie(58 + ein, yy + 16, ll - ein)
                linie(58 + ein, yy + 34, ll - ein - 40)
        elif art == "umstellen":
            for i in range(5):
                yy = 22 + i * 38
                if i == 1:
                    dr.rounded_rectangle((10 * s, (yy - 12) * s, (iw - 60) * s, (yy + 14) * s), 6 * s, fill=MARKER)
                linie(18, yy, iw - 90)
            dr.line(((iw - 40) * s, 36 * s, (iw - 40) * s, 170 * s), fill=INK, width=5 * s)
            dr.polygon([((iw - 54) * s, 160 * s), ((iw - 26) * s, 160 * s), ((iw - 40) * s, 184 * s)], fill=INK)
        elif art == "rechtschreibung":
            for i in range(4):
                linie(18, 26 + i * 44, iw - 60 - (i % 2) * 50)
            dr.text((18 * s, 168 * s), glyphen("Gutachten"), font=F("Bold", 28 * s), fill=INK)
            for k in range(14):
                xx = 18 + k * 10
                dr.line((xx * s, 206 * s, (xx + 5) * s, 212 * s), fill=DROT, width=3 * s)
                dr.line(((xx + 5) * s, 212 * s, (xx + 10) * s, 206 * s), fill=DROT, width=3 * s)
        elif art == "ausdruck":
            dr.rectangle((60 * s, 4 * s, (iw - 60) * s, (ih - 4) * s), fill=WEISS, outline=INK, width=3 * s)
            dr.rectangle(((iw - 140) * s, 4 * s, (iw - 60) * s, (ih - 4) * s), fill=HGELB, outline=INK, width=3 * s)
            for i in range(6):
                linie(76, 26 + i * 30, iw - 236)
    return bis_(El(_flaeche(iw, ih, zz), x + 16, y + 16, c, "cut", 0.0, None, name=f"schirm:{art}"), bis)


# ===========================================================================================================================
# A1 Fall: Prüfungssaal kurz vor dem Examen
# ===========================================================================================================================
TE_A = ("TE_redet_r", TEX, BODEN_Y, FHA)
JO_A = ("JO_redet", JOX, BODEN_Y, FHA)
folie([(NULL, "Fall · Prüfungssaal kurz vor dem Examen"), ("t1", "Fall · tippen oder mit der Hand schreiben?"),
       ("j1", "Fall · mehr als die Tastatur, das Wichtigste bleibt")], [
    *saal(NULL),
    bis_(hart(pl("Prüfungssaal kurz vor dem Examen", 70, 30, NULL, fill=GELB, size=38)), "t1"),
    ring(1020, TISCH_Y - 70, 470, 120, beim("lap", "Laptops"), farbe=ORANGE, breite=6, bis="tel"),
    pl("NRW · bald Examensklausuren", TEX, 330, beim("tel", "Examensklausuren"), fill=LILA, size=30, anker="m", bis="t1"),
    pl("2. Examen in Bayern: am Laptop", JOX - 60, 330, beim("jos", "zweites"), fill=TUERKIS, size=30, anker="m", bis="j1"),
    pl("Hand oder Laptop?", LAPTOP[0][0], 440, beim("t1", "Hand"), fill=HGELB, size=30, anker="m", bis="j1"),
    pl("das Wichtigste bleibt gleich", 1210, 440, beim("j1", "Wichtigste"), fill=HELLGRUEN, size=30, anker="m"),
    # Telse (links, blickt nach rechts)
    *fig("TE", TEX, BODEN_Y, FHA, [(NULL, "denkt_r"), ("tel", "froh_r")], erst="cut", bis="t1"),
    *redet("TE_redet_r", TEX, BODEN_Y, FHA, "t1", "j1"),
    *fig("TE", TEX, BODEN_Y, FHA, [("j1", "staunt_r")], erst="cut", bis="hook"),
    hart(ns(NAME["TE"], TEX, BODEN_Y, NULL, NFARBE["TE"])),
    # Jost (rechts, blickt nach links)
    *fig("JO", JOX, BODEN_Y, FHA, [(beim("jos", "Jost"), "froh"), ("t1", "ruhig")], erst="pop", bis="j1"),
    ns(NAME["JO"], JOX, BODEN_Y, beim("jos", "Jost"), NFARBE["JO"], d=0.1),
    *redet("JO_redet", JOX, BODEN_Y, FHA, "j1", "hook"),
    blase("sprech", 720, 190, "t1", 600, 190, inhalt=["Tippen oder mit der Hand schreiben?", "Was ändert sich da wirklich?"],
          textsize=32, figur=TE_A, bis="j1"),
    blase("sprech", 640, 190, "j1", 1380, 200, inhalt=["Mehr als die Tastatur. Aber", "das Wichtigste bleibt gleich."],
          textsize=32, figur=JO_A, bis="hook"),
])

# ===========================================================================================================================
# A2 Einstieg: Statt Stift jetzt Tastatur
# ===========================================================================================================================
folie([("hook", "Einstieg · statt Stift jetzt Tastatur"), ("hook2", "Einstieg › E-Examen: Klausuren am Computer"),
       ("wie", "Einstieg › geregelt? ändert sich? bleibt? vorbereiten?")], rechts_frei([
    *tafel("hook", "Statt Stift jetzt Tastatur?"),
    ticon("tabler", "pencil", 230, 330, 110, beim("hook", "Stift"), fuell=GELB),
    pfeil(320, 280, 420, 280, beim("hook", "Tastatur"), breite=8, kopf=26),
    ticon("tabler", "keyboard", 540, 330, 150, beim("hook", "Tastatur"), fuell=HELLBLAU),
    z("Statt Stift", 660, 230, beim("hook", "Stift"), "Bold", 36),
    z("jetzt Tastatur", 660, 280, beim("hook", "Tastatur"), "Bold", 36),
    blk(110, 380, 1040, 100, GELB, beim("hook2", "E-Examen"), [("E-Examen: Examensklausuren am Computer", "ExtraBold", 38, INK)]),
    z("1. Wo ist das geregelt?", 150, 530, beim("wie", "geregelt"), "Bold", 36),
    z("2. Was ändert sich?", 150, 600, beim("wie", "ändert"), "Bold", 36),
    z("3. Was bleibt?", 150, 670, beim("wie", "bleibt"), "Bold", 36),
    z("4. Wie bereitest du dich vor?", 150, 740, beim("wie", "vorbereitest"), "Bold", 36),
    *requisit([("hook", ("tabler", "pencil", 100, GELB), "Stift?", WEISS),
               (beim("hook", "Tastatur"), ("tabler", "keyboard", 130, HELLBLAU), "Tastatur", WEISS),
               ("hook2", ("tabler", "device-laptop", 140, HELLBLAU), "E-Examen", GELB),
               ("wie", ("tabler", "list-check", 100, WEISS), "4 Fragen", WEISS)]),
    *stehend("TE", X1, [("hook", "denkt"), ("hook2", "staunt"), ("wie", "ruhig")]),
    *stehend("JO", X2, [("hook", "ruhig"), ("hook2", "froh")]),
]))

# ===========================================================================================================================
# B Sachverhalt (Ausgangslage)
# ===========================================================================================================================
def sachverhalt_279(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt · Die Ausgangslage von Telse")], els)


sachverhalt_279("sv", [
    "Telse studiert Jura in Nordrhein-Westfalen. Bald schreibt sie die Aufsichtsarbeiten der staatlichen "
    "Pflichtfachprüfung.",
    "Bisher hat sie alle Klausuren mit der Hand geschrieben.",
    "Ihr Bruder Jost hat das 2. Examen in Bayern schon am Laptop geschrieben.",
], "Soll Telse am Laptop schreiben? Und was ändert sich dann für sie?")

# ===========================================================================================================================
# C Wo ist das E-Examen geregelt? Wortlaut § 5d Abs. 6 DRiG
# ===========================================================================================================================
W5D6 = ("„Das Nähere regelt das Landesrecht. Es kann auch bestimmen, dass in den staatlichen Prüfungen schriftliche "
        "Leistungen elektronisch erbracht werden dürfen.“")
w6, w6_y = wortlaut(80, 270, 1100, W5D6, "§ 5d Abs. 6 DRiG", "drig", marken=[
    ("Landesrecht", beim("wl1", "Landesrecht")), ("elektronisch", beim("wl2", "elektronisch")),
    ("dürfen", beim("wl2", "dürfen"))], size=34)
assert w6_y <= 640, w6_y
folie([("was", "Rechtsgrundlage · Wo ist das E-Examen geregelt?"), ("drig", "Rechtsgrundlage › § 5d Abs. 6 DRiG"),
       ("wl2", "Rechtsgrundlage › Land darf elektronische Klausuren zulassen"),
       ("land", "Rechtsgrundlage › ob und wie: dein Land")], rechts_frei([
    *tafel("was", "Wo ist das E-Examen geregelt?"),
    z("Grundlage: Deutsches Richtergesetz (DRiG)", 110, 190, "drig", "Bold", 34),
    *w6,
    blk(110, 600, 1040, 90, HGELB, "land", [("Ob und wie: Das entscheidet dein Land.", "ExtraBold", 36, INK)]),
    pl("2 Beispiele: NRW und Bayern", 110, 720, beim("land", "Beispiele"), fill=GELB, size=32),
    *requisit([("was", ("tabler", "help", 100, WEISS), "Wo geregelt?", WEISS),
               ("drig", ("tabler", "book", 100, WEISS), "DRiG", WEISS),
               ("wl2", ("tabler", "device-laptop", 140, HELLBLAU), "elektronisch erlaubt", HELLGRUEN),
               ("land", ("tabler", "map-pin", 100, GELB), "Landesrecht", GELB)]),
    *allein("TE", [("was", "ruhig"), ("wl1", "denkt"), ("wl2", "staunt"), ("land", "ruhig")]),
]))

# ===========================================================================================================================
# D Länderbeispiele: NRW (§§ 10 I, 51 I JAG NRW; LJPA NRW) und Bayern (LJPA Bayern)
# ===========================================================================================================================
LX0, LW, RW = 110, 270, 770


def landblock(c, y, h, land, fill, quelle, zeilen):
    """Länderzeile: Landkasten mit Fundstelle links, Regeln rechts zeilenweise in Sprechreihenfolge (zeilen=[(text, cue)])."""
    els = [kasten(LX0, y, LW, h, fill, c, name=f"land:{land}"),
           z(land, LX0 + 20, y + 20, c, "ExtraBold", 34, rechts=LX0 + LW - 10),
           kasten(LX0 + LW, y, RW, h, WEISS, c, name=f"regel:{land}")]
    for i, q in enumerate(quelle):
        els.append(zit(q, LX0 + 20, y + h - 44 - (len(quelle) - 1 - i) * 34, c, size=26, rechts=LX0 + LW - 6))
    for i, (t, cz) in enumerate(zeilen):
        els.append(z(t, LX0 + LW + 22, y + 18 + i * 46, cz or c, "Bold", 30, rechts=LX0 + LW + RW - 10))
    return els


folie([("nrw", "Länder › NRW: seit 1.1.2024 im 1. und 2. Examen"), ("nrw2", "Länder › NRW: Wahl zwischen Hand und Laptop"),
       ("nrw3", "Länder › NRW: Wechsel zur Hand vor Klausurbeginn"), ("by", "Länder › Bayern: 2. Examen 2024/2, 1. Examen 2026/2"),
       ("by2", "Länder › Bayern: freiwillig, Wahl vorab und bindend"), ("beide", "Länder › gestellter Laptop, kein eigener")],
      rechts_frei([
    *tafel("nrw", "E-Examen: 2 Beispiele"),
    *landblock("nrw", 180, 240, "NRW", HELLBLAU, ["§§ 10 I, 51 I", "JAG NRW"], [
        ("seit 1.1.2024: Prüfungsämter müssen", "nrw"), ("E-Klausur ermöglichen, 1. und 2. Examen", beim("nrw", "ersten")),
        ("Wahl: Hand oder Laptop", "nrw2"), ("Wechsel zur Hand: noch vor Klausurbeginn", "nrw3")]),
    *landblock("by", 445, 200, "Bayern", HGELB, ["LJPA Bayern", "(§ 5 III JAPO)"], [
        ("2. Examen: seit Termin 2024/2", "by"), ("1. Examen: seit Termin 2026/2", beim("by", "ersten")),
        ("freiwillig, Wahl vorab, grundsätzlich bindend", "by2")]),
    *okz("beide: gestellter Laptop im Saal, kein eigener", 690, "beide", "Bold", 34, x=170),
    zit("NRW: Seiten des Landesjustizprüfungsamts · Bayern: FAQ des Landesjustizprüfungsamts", 110, 760, "beide", size=26),
    *requisit([("nrw", ("tabler", "map-pin", 100, HELLBLAU), "Nordrhein-Westfalen", WEISS),
               ("nrw2", ("tabler", "arrows-exchange", 110, HELLGRUEN), "Hand oder Laptop", HELLGRUEN),
               ("by", ("tabler", "map-pin", 100, HGELB), "Bayern", WEISS),
               ("by2", ("tabler", "lock", 100, HGELB), "Wahl bindend", WEISS),
               ("beide", ("tabler", "device-laptop", 140, HELLBLAU), "gestellter Laptop", WEISS)]),
    *stehend("TE", X1, [("nrw", "denkt"), ("nrw2", "froh"), ("by", "ruhig")]),
    *stehend("JO", X2, [("nrw", "ruhig"), ("by", "froh"), ("by2", "ernst"), ("beide", "ruhig")]),
]))

# ===========================================================================================================================
# E1 Was ändert sich? Gliederung, Korrigieren und Umstellen, Rechtschreibprüfung (Jost: Korrektur gelesen)
# ===========================================================================================================================
JO_E = ("JO_redetfroh", X2, FB, FR)
folie([("aend", "Was ändert sich · beim Schreiben?"), ("gl", "Was ändert sich › 1. Gliederung"),
       ("um", "Was ändert sich › 2. Korrigieren und Umstellen"), ("rs", "Was ändert sich › Rechtschreibprüfung"),
       ("j2", "Was ändert sich › selbst Korrektur lesen")], rechts_frei([
    *tafel("aend", "Was ändert sich beim Schreiben?"),
    *bildschirm("aend"),
    schirm_inhalt("gliederung", "gl", bis="um"),
    schirm_inhalt("umstellen", "um", bis="rs"),
    schirm_inhalt("rechtschreibung", "rs"),
    z("1. Gliederung", 110, 190, "gl", "ExtraBold", 34, rechts=740),
    z("Absätze und Einzüge", 140, 240, beim("gl", "Absätzen"), "Bold", 30, rechts=740),
    zit("Bayern: keine automatische Gliederung", 140, 285, beim("gl", "automatische"), rechts=740),
    z("2. Korrigieren und Umstellen", 110, 360, "um", "ExtraBold", 34, rechts=740),
    z("löschen, einfügen, verschieben", 140, 410, beim("um", "löschst"), "Bold", 30, rechts=740),
    *okz("nichts durchgestrichen", 455, beim("um", "durchgestrichen"), "Bold", 30, x=185, rechts=740),
    z("Rechtschreibprüfung", 110, 545, "rs", "ExtraBold", 34, rechts=740),
    *okz("NRW: ein- und ausschaltbar", 595, beim("rs", "Nordrhein"), "Bold", 30, x=185, rechts=740),
    *neinz("Bayern: keine", 645, beim("rs", "Bayern"), "Bold", 30, x=185, rechts=740),
    pl("selbst Korrektur lesen", 110, 740, beim("j2", "Korrektur"), fill=HGELB, size=32),
    *requisit([("aend", ("tabler", "device-laptop", 140, HELLBLAU), "Was ändert sich?", WEISS),
               ("gl", ("tabler", "list-numbers", 100, WEISS), "Gliederung", WEISS),
               ("um", ("tabler", "arrows-move-vertical", 90, WEISS), "Umstellen", WEISS),
               ("rs", ("tabler", "text-spellcheck", 110, WEISS), "Rechtschreibung", WEISS),
               ("j2", None, None, None)]),
    *stehend("TE", X1, [("aend", "ruhig"), ("um", "staunt"), ("rs", "denkt"), ("j2", "ruhig")]),
    *fig("JO", X2, FB, FR, [("aend", "ruhig"), ("rs", "denkt")], bis="j2"),
    *redet("JO_redetfroh", X2, FB, FR, "j2", "zeit"),
    ns(NAME["JO"], X2, FB, "aend", NFARBE["JO"], d=0.1),
    blase("sprech", 600, 170, "j2", 1560, 250, inhalt=["Ich habe deshalb am Ende", "selbst Korrektur gelesen."],
          textsize=32, figur=JO_E, bis="zeit"),
]))

BL = (790, 470, 330, 330)                    # Ausdruck: x, y, w, h


def blatt(c, c_rand):
    """Ausdruck der Klausur (Skizze): Seite mit Schreibzeilen; der Korrekturrand erscheint beim Wort „Korrekturrand“."""
    x, y, w, h = BL
    def seite(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), fill=WEISS, outline=INK, width=4 * s)
        for i in range(8):
            dr.line((24 * s, (34 + i * 36) * s, (w - 130 - (i % 3) * 20) * s, (34 + i * 36) * s), fill=GRAU, width=5 * s)
    def rand(dr, s):
        dr.rectangle((3 * s, 3 * s, (96 - 3) * s, (h - 3) * s), fill=HGELB, outline=INK, width=4 * s)
    return [El(_flaeche(w, h, seite), x, y, c, "pop", 0.0, None, name="ausdruck"),
            El(_flaeche(96, h, rand), x + w - 96, y, c_rand, "pop", 0.0, None, name="ausdruck:korrekturrand"),
            z("Korrekturrand", x + w - 200, y + h + 10, c_rand, "Bold", 28, rechts=1170)]


# ===========================================================================================================================
# E2 Was ändert sich? Zeit und Lesbarkeit
# ===========================================================================================================================
folie([("zeit", "Was ändert sich › 3. Zeit"), ("zeit2", "Was ändert sich › Bayern: Hinweis, Abgabe per Klick"),
       ("zeit3", "Was ändert sich › NRW: automatisch gespeichert"), ("les", "Was ändert sich › 4. Lesbarkeit"),
       ("les2", "Was ändert sich › Bayern: Ausdruck mit Korrekturrand")], rechts_frei([
    *tafel("zeit", "Zeit und Lesbarkeit"),
    z("3. Zeit", 110, 190, "zeit", "ExtraBold", 34),
    *neinz("Bayern: keine Uhr in der Software", 240, beim("zeit", "Uhr"), "Bold", 30, x=185),
    z("Hinweis 15 Minuten vor Schluss", 185, 290, beim("zeit2", "Viertelstunde"), "Bold", 30),
    z("Abgabe selbst per Klick", 185, 340, beim("zeit2", "Klick"), "Bold", 30),
    *okz("NRW: bei Zeitablauf automatisch gespeichert", 390, beim("zeit3", "Zeitablauf"), "Bold", 30, x=185),
    z("4. Lesbarkeit", 110, 480, "les", "ExtraBold", 34),
    *okz("keine Handschrift mehr entziffern", 530, beim("les", "Handschrift"), "Bold", 30, x=185),
    z("Bayern: Prüfer erhalten Ausdruck", 185, 580, beim("les2", "ausgedruckt"), "Bold", 30, rechts=740),
    z("Korrekturrand: von der Software", 185, 630, beim("les2", "Korrekturrand"), "Bold", 30, rechts=740),
    *blatt(beim("les2", "ausgedruckt"), beim("les2", "Korrekturrand")),
    *requisit([("zeit", ("tabler", "clock-off", 100, WEISS), "keine Uhr", HROT),
               ("zeit2", ("tabler", "click", 100, WEISS), "selbst abgeben", WEISS),
               ("zeit3", ("tabler", "device-floppy", 100, HELLBLAU), "automatisch gespeichert", HELLGRUEN),
               ("les", ("tabler", "eye", 110, WEISS), "lesbar", WEISS),
               ("les2", ("tabler", "printer", 110, WEISS), "Ausdruck", WEISS)]),
    *stehend("TE", X1, [("zeit", "sorge"), ("zeit3", "ruhig"), ("les", "lacht")]),
    *stehend("JO", X2, [("zeit", "ernst"), ("zeit3", "ruhig"), ("les", "froh")]),
]))

# ===========================================================================================================================
# F Was bleibt gleich? Papier, Bücher, Gutachtenstil und Schwerpunkte
# ===========================================================================================================================
folie([("bleibt", "Was bleibt · gleich?"), ("pap", "Was bleibt › Aufgabentext auf Papier"),
       ("komm", "Was bleibt › Gesetzestexte als Bücher"), ("gut", "Was bleibt › Gutachtenstil, Argumente, Schwerpunkte"),
       ("mehr", "Was bleibt › mehr Text ist nicht besser")], rechts_frei([
    *tafel("bleibt", "Was bleibt gleich?"),
    *okz("Aufgabentext auf Papier", 190, beim("pap", "Aufgabentext"), "Bold", 34, x=170),
    *okz("Gesetzestexte als Bücher", 250, beim("komm", "Gesetzestexte"), "Bold", 34, x=170),
    z("2. Examen NRW: auch Kommentare", 170, 300, beim("komm", "Kommentare"), "Bold", 30),
    *neinz("nicht elektronisch", 370, beim("komm", "Elektronisch"), "Bold", 34, x=170),
    ticon("tabler", "file-text", 1000, 300, 100, beim("pap", "Aufgabentext"), fuell=WEISS),
    ticon("tabler", "books", 1090, 420, 120, beim("komm", "Gesetzestexte"), fuell=GELB),
    z("Es geht um dasselbe wie bisher:", 110, 470, "gut", "Bold", 34),
    pl("Gutachtenstil", 110, 535, beim("gut", "Gutachtenstil"), fill=BLAU, size=34),
    pl("Argumente", 440, 535, beim("gut", "Argumente"), fill=GRUEN, size=34),
    pl("Schwerpunkte", 700, 535, beim("gut", "Schwerpunkte"), fill=GELB, size=34),
    z("Tippen geht schneller, verführt zu langen Texten.", 110, 650, "mehr", "Bold", 32),
    blk(110, 710, 1040, 90, HROT, beim("mehr", "Mehr"), [("Mehr Text ist nicht automatisch besser.", "ExtraBold", 36, INK)]),
    *requisit([("bleibt", ("tabler", "shield-check", 100, HELLGRUEN), "bleibt gleich", HELLGRUEN),
               ("pap", ("tabler", "file-text", 100, WEISS), "Papier", WEISS),
               ("komm", ("tabler", "books", 120, GELB), "Bücher", WEISS),
               ("gut", ("tabler", "scale", 110, WEISS), "gleicher Maßstab", WEISS),
               ("mehr", ("tabler", "target", 100, HROT), "Schwerpunkte", WEISS)]),
    *stehend("TE", X1, [("bleibt", "ruhig"), ("pap", "froh"), ("gut", "denkt"), ("mehr", "staunt")]),
    *stehend("JO", X2, [("bleibt", "ruhig"), ("gut", "froh"), ("mehr", "ernst")]),
]))

# ===========================================================================================================================
# G Vorbereitung: Probeklausuren am Rechner, zehn Finger, Demoportale, Tastatur
# ===========================================================================================================================
DX, DW, DH = [110, 640], 510, 150


folie([("vorb", "Vorbereitung · Wie bereitest du dich vor?"), ("probe", "Vorbereitung › Probeklausuren am Rechner"),
       ("zehn", "Vorbereitung › Tippen mit 10 Fingern"), ("demo", "Vorbereitung › Demoportal der Länder"),
       ("tast", "Vorbereitung › Bayern: nur zugelassene Tastatur")], rechts_frei([
    *tafel("vorb", "So bereitest du dich vor"),
    ticon("tabler", "writing", 160, 250, 80, "probe", fuell=GELB),
    z("Probeklausuren am Rechner", 220, 185, "probe", "ExtraBold", 34),
    z("volle Länge, feste Zeit", 220, 232, beim("probe", "voller"), "Bold", 30),
    ticon("tabler", "keyboard", 160, 365, 90, "zehn", fuell=HELLBLAU),
    z("Tippen mit 10 Fingern", 220, 300, "zehn", "ExtraBold", 34),
    z("dein Blick bleibt beim Text", 220, 347, beim("zehn", "Blick"), "Bold", 30),
    z("Demoportal mit der Schreiboberfläche:", 110, 420, "demo", "ExtraBold", 34),
    kasten(DX[0], 475, DW, DH, HELLBLAU, "demo2", name="demo:NRW"),
    z("NRW", DX[0] + 20, 490, "demo2", "ExtraBold", 32),
    z("speichert zwischen; laut LJPA", DX[0] + 20, 532, beim("demo2", "speichert"), "Bold", 29, rechts=DX[0] + DW - 10),
    z("auch für lange Probeklausuren", DX[0] + 20, 572, beim("demo2", "Probeklausuren"), "Bold", 29, rechts=DX[0] + DW - 10),
    kasten(DX[1], 475, DW, DH, HGELB, "demo3", name="demo:Bayern"),
    z("Bayern", DX[1] + 20, 490, "demo3", "ExtraBold", 32),
    z("zeigt nur die Funktionen,", DX[1] + 20, 532, beim("demo3", "Funktionen"), "Bold", 29, rechts=DX[1] + DW - 10),
    z("speichert nicht", DX[1] + 20, 572, beim("demo3", "speichern"), "Bold", 29, rechts=DX[1] + DW - 10),
    blk(110, 680, 1040, 90, HGELB, "tast", [("Bayern: eigene Tastatur nur als zugelassenes Modell", "ExtraBold", 33, INK)]),
    *requisit([("vorb", ("tabler", "school", 110, WEISS), "Vorbereitung", WEISS),
               ("probe", ("tabler", "writing", 100, GELB), "Probeklausur am Rechner", WEISS),
               ("zehn", ("tabler", "keyboard", 130, HELLBLAU), "10 Finger", WEISS),
               ("demo", ("tabler", "device-laptop", 140, HELLBLAU), "Demoportal", WEISS),
               ("tast", ("tabler", "keyboard", 130, HGELB), "zugelassenes Modell", WEISS)]),
    *stehend("TE", X1, [("vorb", "denkt"), ("probe", "entschlossen"), ("demo", "ruhig"), ("demo2", "froh")]),
    *stehend("JO", X2, [("vorb", "ruhig"), ("zehn", "froh"), ("demo3", "denkt"), ("tast", "ruhig")]),
]))

# ===========================================================================================================================
# H Ergebnis: Prüfungssaal – Telse setzt sich an einen Laptop und tippt
# ===========================================================================================================================
SITZ_X, SITZ_H = 590, 340                    # Telse sitzend vor Tisch 1 (blickt nach rechts zum Laptop)
TS_H = ("TS_redet_r", SITZ_X, BODEN_Y, SITZ_H)
JO_H = ("JO_redetfroh", JOX, BODEN_Y, FHA)
SETZT = beim("erg", "setzt")
TIPPT = beim("erg", "tippt")


def hocker(c):
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, 157 * s, 24 * s), fill=GRAU, outline=INK, width=4 * s)
        dr.rectangle((70 * s, 22 * s, 90 * s, 130 * s), fill=GRAU2, outline=INK, width=4 * s)
        dr.rectangle((30 * s, 124 * s, 130 * s, 138 * s), fill=GRAU, outline=INK, width=4 * s)
    return El(_flaeche(160, 140, zz), SITZ_X - 110, BODEN_Y - 140, c, "cut", 0.0, None, name="hocker")


def text_auf_laptop(c, n):
    """Zeilen auf dem Laptopbildschirm (Skizze, nur Linien)."""
    lx, lb = LAPTOP[0]
    def zz(dr, s):
        for i in range(n):
            dr.line((4 * s, (6 + i * 14) * s, (96 - (i % 2) * 24) * s, (6 + i * 14) * s), fill=INK, width=4 * s)
    return El(_flaeche(100, 6 + n * 14, zz), lx - 50, TISCH_Y - 118, c, "cut", 0.0, None, name=f"laptoptext:{n}")


folie([("erg", "Ergebnis · Telse probiert den Laptop aus"), ("t2", "Ergebnis › Demoportal und Probeklausuren am Rechner"),
       ("j3", "Ergebnis › erst auf Papier gliedern, dann tippen")], [
    *saal("erg"),
    bis_(hart(pl("Prüfungssaal", 70, 30, "erg", fill=GELB, size=38)), "t2"),
    # Telse steht zuerst neben dem Tisch und setzt sich dann
    *fig("TE", TEX, BODEN_Y, FHA, [("erg", "froh_r")], erst="cut", bis=SETZT),
    bis_(hart(ns(NAME["TE"], TEX, BODEN_Y, "erg", NFARBE["TE"])), SETZT),
    hocker(SETZT),
    *fig("TS", SITZ_X, BODEN_Y - 110, SITZ_H, [(SETZT, "tippt_r")], erst="cut", bis="t2"),
    *redet("TS_redet_r", SITZ_X, BODEN_Y - 110, SITZ_H, "t2", "j3"),
    *fig("TS", SITZ_X, BODEN_Y - 110, SITZ_H, [("j3", "froh_r")], erst="cut", bis="tipp"),
    ns(NAME["TS"], SITZ_X - 30, BODEN_Y, SETZT, NFARBE["TS"]),
    szene(bis_(text_auf_laptop(TIPPT, 2), (TIPPT[0], round(TIPPT[1] + 0.8, 3))), "279tippen*", 1.3, versatz=0.0),
    text_auf_laptop((TIPPT[0], round(TIPPT[1] + 0.8, 3)), 4),
    pl("Demoportal + Probeklausuren am Rechner", 1220, 420, beim("t2", "Demoportal"), fill=HELLGRUEN, size=30, anker="m", bis="j3"),
    pl("erst auf Papier gliedern, dann tippen", 1200, 440, beim("j3", "gliedere"), fill=HGELB, size=30, anker="m"),
    *fig("JO", JOX, BODEN_Y, FHA, [("erg", "froh")], erst="cut", bis="j3"),
    *redet("JO_redetfroh", JOX, BODEN_Y, FHA, "j3", "tipp"),
    hart(ns(NAME["JO"], JOX, BODEN_Y, "erg", NFARBE["JO"])),
    blase("sprech", 820, 190, "t2", 700, 200, inhalt=["Ich schreibe am Laptop. Vorher übe ich im", "Demoportal und schreibe jede",
                                                     "Probeklausur am Rechner."], textsize=30, figur=TS_H, bis="j3"),
    blase("sprech", 640, 170, "j3", 1380, 200, inhalt=["Und gliedere zuerst auf dem", "Papier. Dann erst tippst du."],
          textsize=32, figur=JO_H, bis="tipp"),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi): erst skizzieren, dann tippen
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: erst skizzieren, dann tippen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Lösungsskizze zuerst auf dem Konzeptpapier", 200, 200, beim("tipp", "Lösungsskizze"), "Bold", 32),
         ticon("tabler", "clipboard-text", 260, 450, 120, beim("tipp", "Konzeptpapier"), fuell=WEISS),
         pl("Schwerpunkte markieren", 200, 262, beim("tipp", "markiere"), fill=GELB, size=30),
         pfeil(380, 400, 620, 400, "tipp2", breite=8, kopf=26),
         ticon("tabler", "device-laptop", 790, 470, 200, "tipp2", fuell=HELLBLAU),
         z("erst dann das Gutachten tippen", 660, 490, "tipp2", "Bold", 32),
         blk(110, 580, 1040, 130, HROT, "tipp3", [("Verschieben ist leicht, aber ein Umbau", "Bold", 32, INK),
                                                  ("mitten in der Klausur kostet Zeit", "ExtraBold", 34, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · erst Lösungsskizze auf Papier"), ("tipp2", "Klausurtipp › dann das Gutachten tippen"),
       ("tipp3", "Klausurtipp › Umbau kostet Zeit")], els_k)

# ===========================================================================================================================
# J Dein E-Examen in 5 Schritten (Schema, Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Regeln deines Landes prüfen: Wahl und Frist", BLAU),
          ("k2", "II.", "Demoportal ausprobieren", GRUEN),
          ("k3", "III.", "Probeklausuren am Rechner schreiben", HELLBLAU),
          ("k4", "IV.", "Lösungsskizze auf Papier, dann tippen", GELB),
          ("k5", "V.", "Zeit und Schwerpunkte im Blick behalten", HROT)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Dein E-Examen in 5 Schritten"), 110, 90, "sch", 50)]
y = 230
for c, nr, text, f in REIHEN:
    els_sch.append(pl(nr, 130, y - 6, c, fill=f, size=36))
    els_sch.append(z(text, 300, y, c, "ExtraBold", 40, rechts=1820))
    y += 135
assert y <= 960, y
folie([("sch", "E-Examen · 5 Schritte"), ("k1", "E-Examen › I. Regeln deines Landes prüfen"),
       ("k2", "E-Examen › II. Demoportal ausprobieren"), ("k3", "E-Examen › III. Probeklausuren am Rechner"),
       ("k4", "E-Examen › IV. erst Papier, dann tippen"), ("k5", "E-Examen › V. Zeit und Schwerpunkte")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im E-Examen ändert sich das ", 0), ("Werkzeug,", "a")], [("nicht der ", 0), ("Maßstab.", "b")]],
                750, 300, 44, "merke", {"a": beim("merke", "Werkzeug"), "b": beim("merke", "Maßstab")}),
    *markertext([[("Es zählen ", 0), ("Gutachtenstil", "c"), (" und ", 0), ("Schwerpunkte.", "e")]],
                750, 480, 42, "m2", {"c": beim("m2", "Gutachtenstil"), "e": beim("m2", "Schwerpunkte")}),
    *markertext([[("Ob und wie du am Laptop schreibst, regelt", 0)], [("dein Land, also frag dein ", 0), ("Prüfungsamt.", "d")]],
                750, 600, 40, "m3", {"d": beim("m3", "Prüfungsamt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
