"""Folge 162 · Analogie Jura: Regelungslücke und vergleichbare Interessenlage – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Ilona wird von ihrem Nachbarn Bertold immer wieder vor anderen Nachbarn im Hof beleidigt (nur die Text-Pille
„beleidigende Äußerungen“, keine Beleidigungsworte) und klagt auf Unterlassung; vor Gericht beruft sich Bertold auf den
Wortlaut des § 1004 BGB. Danach Tafeln: Wortlautkarten § 1004 Abs. 1, § 823 Abs. 1 BGB, Art. 103 Abs. 2 GG, Zitatkarten
BGH IX ZR 91/24 Rn. 14 und I ZR 12/23 Rn. 16; drei Prüfschritte mit je eigener Farbe (Gelb, Lila, Grün). Szenen laut
../SZENENPLAN.md, Belege ../RECHTSSTAND.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/neinz2 als eigene Kopie aus Folge 160 (gemeinsame
Dateien unverändert); neu: haus, tuer, richtertisch, gerichtssaal, schritt_tafel, kachel. Zahlen auf Tafeln, Pillen und
Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_162/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_162/" in n:
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



GELBHELL = (255, 245, 210, 255)
LILAMITTEL = (236, 230, 255, 255)
SCHRITT = {1: (GELB, GELBHELL, "1. Regelungslücke"), 2: (LILA, LILAMITTEL, "2. planwidrig"),
           3: (GRUEN, HELLGRUEN, "3. vergleichbare Interessenlage")}      # eigene Farbe je Prüfschritt


def schritt_tafel(nr, cue, titel_):
    """Tafel eines Prüfschritts in seiner Farbe: helle Fläche, farbige Pille „Schritt n“ oben rechts."""
    farbe, hell, _ = SCHRITT[nr]
    return [*tafel(cue, titel_, fill=hell, frei=940), pl(f"Schritt {nr}", 1000, 96, cue, fill=farbe, size=30)]


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"IL": "Ilona", "BE": "Bertold", "RI": "Richterin"}
NFARBE = {"IL": PINK, "BE": ORANGE, "RI": WEISS}


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
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# --- Mehrfamilienhaus und Gerichtssaal aus Grundformen (Palettenflächen, Tuschekontur) ------------------------------------
HAUS_X, HAUS_W, HAUS_H = 90, 520, 600
TUER_X, TUER_W, TUER_H = HAUS_X + 200, 120, 200


def haus(cue):
    """Mehrfamilienhaus: Fassade, Dach, drei Etagen mit Fenstern, Haustür (geschlossen)."""
    w, h = HAUS_W, HAUS_H
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o + 40 * s, o + w * s, o + h * s), fill=(244, 228, 200, 255), outline=INK, width=5 * s)
    dr.polygon([(o - 2 * s, o + 42 * s), (o + 30 * s, o), (o + (w - 30) * s, o), (o + (w + 2) * s, o + 42 * s)],
               fill=ROT, outline=INK)
    dr.line([(o - 2 * s, o + 42 * s), (o + 30 * s, o), (o + (w - 30) * s, o), (o + (w + 2) * s, o + 42 * s)], fill=INK,
            width=5 * s)
    for r in range(3):
        for c_ in range(3):
            x0, y0 = o + (50 + c_ * 160) * s, o + (80 + r * 120) * s
            dr.rounded_rectangle((x0, y0, x0 + 100 * s, y0 + 76 * s), 6 * s, fill=BLAUHELL, outline=INK, width=4 * s)
            dr.line([(x0 + 50 * s, y0), (x0 + 50 * s, y0 + 76 * s)], fill=INK, width=3 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, HAUS_X - 6, BODEN - h - 6, cue, "cut", 0.0, None, name="haus"))


def tuer(cue, offen=False, bis=None):
    """Haustür: geschlossen (Holz mit Klinke) oder offen (dunkle Öffnung, Türblatt aufgeklappt)."""
    w, h = TUER_W, TUER_H
    im, dr, s = _flaeche(w + 40, h)
    o = 6 * s
    if offen:
        dr.rectangle((o, o, o + w * s, o + h * s), fill=(70, 62, 60, 255), outline=INK, width=5 * s)
        dr.polygon([(o + w * s, o), (o + (w + 36) * s, o + 18 * s), (o + (w + 36) * s, o + (h - 10) * s),
                    (o + w * s, o + h * s)], fill=HOLZ, outline=INK)
        dr.line([(o + w * s, o), (o + (w + 36) * s, o + 18 * s), (o + (w + 36) * s, o + (h - 10) * s), (o + w * s, o + h * s)],
                fill=INK, width=5 * s)
    else:
        dr.rectangle((o, o, o + w * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
        dr.ellipse((o + (w - 26) * s, o + 100 * s, o + (w - 12) * s, o + 114 * s), fill=INK)
    im = im.resize((w + 52, h + 12), Image.LANCZOS)
    return El(im, TUER_X - 6, BODEN - h - 6, cue, "cut", 0.0, bis, name="tuer")


RT_X, RT_W, RT_H = 700, 520, 250            # Richtertisch (Front), Oberkante BODEN - RT_H
RT_O = BODEN - RT_H


def richtertisch(cue):
    """Richtertisch als holzfarbene Front mit Platte; verdeckt die sitzende Richterin ab der Schulter."""
    w, h = RT_W, RT_H
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o + 22 * s, o + w * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    dr.rounded_rectangle((o - 4 * s, o, o + (w + 4) * s, o + 28 * s), 8 * s, fill=(190, 135, 90, 255), outline=INK, width=5 * s)
    for xx in (o + 40 * s, o + (w - 40) * s):
        dr.line([(xx, o + 60 * s), (xx, o + (h - 30) * s)], fill=INK, width=3 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, RT_X - 6, RT_O - 6, cue, "cut", 0.0, None, name="richtertisch"))


RIX, RIU, RIH = 960, RT_O + 165, 360        # Richterin sitzt hinter dem Tisch (Kopf und Schultern sichtbar)
GIX, GRX = 360, 1560                        # Ilona links, Bertold rechts im Gerichtssaal


def gerichtssaal(cue):
    return [boden(cue), richtertisch(cue), hart(pl("Gericht", 960, 40, cue, fill=WEISS, size=30, anker="m"))]


# ===========================================================================================================================
# A1 Fall: im Hof vor dem Mehrfamilienhaus. Bertold kommt aus der Haustür (blickt nach rechts zu Ilona), Ilona rechts
# (blickt nach links zu ihm). Keine Beleidigungsworte, nur die Text-Pille „beleidigende Äußerungen“.
# ===========================================================================================================================
BEX, ILX = 860, 1480
folie([(NULL, "Fall · Im Hof des Mehrfamilienhauses"), ("beleid", "Fall · Beleidigungen vor den Nachbarn"),
       ("il1", "Fall · Ilona will, dass es aufhört"), ("klage", "Fall · Klage auf Unterlassung")], [
    boden(NULL), haus(NULL),
    tuer(NULL, bis=beim("beleid", "Nachbar")),
    szene(tuer(beim("beleid", "Nachbar"), offen=True), "162tuer*", 0.8, -0.43),
    pl("Mehrfamilienhaus", HAUS_X + HAUS_W / 2, 200, NULL, fill=WEISS, size=30, anker="m"),
    # Ilona (blickt nach links zu Bertold)
    *fig("IL", ILX, BODEN, FH, [(NULL, "ruhig"), (beim("beleid", "beleidigt"), "sorge")], bis="il1", erst="cut"),
    *redet("IL_redet", ILX, BODEN, FH, "il1", "klage"),
    *fig("IL", ILX, BODEN, FH, [("klage", "denkt")], erst="cut"),
    hart(ns("Ilona", ILX, BODEN, NULL, PINK)),
    # Bertold kommt aus der Haustür (blickt nach rechts zu Ilona)
    *fig("BE", BEX, BODEN, FH, [(beim("beleid", "Nachbar"), "ruhig_r"), (beim("beleid", "beleidigt"), "verachtet_r"),
                               ("klage", "ernst_r")], erst="cut"),
    ns("Bertold", BEX, BODEN, beim("beleid", "Nachbar"), ORANGE, anim="cut"),
    pl("beleidigende Äußerungen", 1080, 300, beim("beleid", "beleidigt"), fill=HELLROT, size=32, anker="m", bis="il1"),
    hart(ficon("tabler", "message-x", 1080, 250, 90, beim("beleid", "beleidigt"), fuell=HELLROT, bis="il1", anim="cut")),
    pl("seit Wochen, immer wieder", 700, 40, beim("beleid", "seit"), fill=WEISS, size=30),
    pl("vor anderen Nachbarn im Hof", 700, 104, beim("beleid", "vor"), fill=WEISS, size=30),
    blase("sprech", 520, 190, "il1", 1300, 245, inhalt=["Bertold, ich will,", "dass das aufhört."], textsize=32,
          figur=("IL_redet", ILX, BODEN, FH), bis="klage"),
    pl("Klage auf Unterlassung", 1240, 200, "klage", fill=GELB, size=32, anker="m"),
    hart(ficon("tabler", "file-text", 1240, 160, 80, "klage", fuell=WEISS, anim="cut")),
])

# ===========================================================================================================================
# A2 Fall: im Gerichtssaal. Ilona links (blickt nach rechts), Bertold rechts (blickt nach links), Richterin sitzt hinter dem
# Richtertisch in der Mitte.
# ===========================================================================================================================
folie([("gericht", "Fall · Vor Gericht"), ("be1", "Fall · „§ 1004 schützt nur das Eigentum“"),
       ("frage", "Die Frage · Das Gesetz regelt den Fall nicht"),
       ("frage2", "Die Frage · Darf die Richterin trotzdem entscheiden?"), ("ri1", "Die Frage · eine Analogie?")], [
    *fig("RI", RIX, RIU, RIH, [("gericht", "ruhig_r"), ("frage", "denkt_r")], bis="ri1", erst="cut"),
    *redet("RI_redet_r", RIX, RIU, RIH, "ri1", "sv"),
    *gerichtssaal("gericht"),
    hart(ficon("tabler", "gavel", RIX + 170, RT_O + 4, 110, "gericht", fuell=HOLZ, anim="cut")),
    hart(ns("Richterin", RIX, BODEN - 40, "gericht", WEISS)),
    *fig("IL", GIX, BODEN, FH, [("gericht", "ruhig_r"), ("be1", "sorge_r"), ("frage2", "denkt_r"), ("ri1", "froh_r")],
         erst="cut"),
    hart(ns("Ilona", GIX, BODEN, "gericht", PINK)),
    *fig("BE", GRX, BODEN, FH, [("gericht", "ruhig")], bis="be1", erst="cut"),
    *redet("BE_redet", GRX, BODEN, FH, "be1", "frage"),
    *fig("BE", GRX, BODEN, FH, [("frage", "denkt"), ("ri1", "ernst")], erst="cut"),
    hart(ns("Bertold", GRX, BODEN, "gericht", ORANGE)),
    pl("Ilona klagt auf Unterlassung", 70, 40, "gericht", fill=GELB, size=30),
    blase("sprech", 560, 190, "be1", 1380, 250, inhalt=["§ 1004 schützt doch", "nur das Eigentum!"], textsize=32,
          figur=("BE_redet", GRX, BODEN, FH), bis="frage"),
    pl("Das Gesetz regelt diesen Fall nicht ausdrücklich.", 1320, 120, "frage", fill=WEISS, size=30, anker="m", bis="ri1"),
    pl("Darf die Richterin trotzdem entscheiden?", 1320, 190, "frage2", fill=PINK, size=32, anker="m", bis="ri1"),
    blase("sprech", 500, 180, "ri1", 1400, 230, inhalt=["Dann prüfen wir", "eine Analogie."], textsize=32,
          figur=("RI_redet_r", RIX, RIU, RIH), bis="sv"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_162(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_162("sv", [
    "Ilona wohnt in einem Mehrfamilienhaus. Ihr Nachbar Bertold beleidigt sie seit Wochen immer wieder, auch vor "
    "anderen Nachbarn im Hof. Einen sachlichen Anlass gibt es nicht.",
    "Ilona verlangt, dass er das künftig unterlässt, und klagt auf Unterlassung.",
    "Bertold hält dagegen: § 1004 BGB schütze nur das Eigentum, nicht die Ehre.",
], "Hat Ilona einen Anspruch darauf, dass Bertold weitere Beleidigungen unterlässt?")

# ===========================================================================================================================
# C1 Das Problem: Wortlautkarte § 1004 Abs. 1 BGB
# ===========================================================================================================================
PP = "Das Problem"
W1004 = ["„(1) Wird das Eigentum in anderer Weise als durch Entziehung",
         "oder Vorenthaltung des Besitzes beeinträchtigt, so kann der",
         "Eigentümer von dem Störer die Beseitigung der Beeinträchtigung",
         "verlangen. Sind weitere Beeinträchtigungen zu besorgen, so",
         "kann der Eigentümer auf Unterlassung klagen. …“"]
w1004, w1004_y = wortlaut(80, 175, 1100, W1004, "§ 1004 Abs. 1 BGB", "w1004", marken=[
    (3, "Sind weitere Beeinträchtigungen", beim("w1004", "Sind")), (4, "Eigentümer", beim("w1004", "Eigentümer")),
    (4, "Unterlassung", beim("w1004", "Unterlassung")), (0, "Eigentum", beim("nureig", "Eigentum"))], size=31)
folie([("w1004", f"{PP} · § 1004 Abs. 1 S. 2 BGB"), ("nureig", f"{PP} › Wortlaut: nur das Eigentum")], [
    *tafel("w1004", "Das Problem: der Wortlaut des § 1004"),
    *w1004,
    z("Wortlaut: nur das Eigentum", 160, w1004_y + 40, beim("nureig", "Eigentum"), "Bold", 34),
    *neinz("die Ehre ist kein Eigentum", w1004_y + 92, beim("nureig", "Ehre"), "Bold", 34, x=160),
    *requisit([("w1004", ("tabler", "home", 110, BLAUHELL), "Eigentum", BLAUHELL),
               (beim("nureig", "Ehre"), ("tabler", "user-shield", 110, PINK), "Ehre?", PINK)]),
    *paar("IL", [("w1004", "denkt"), (beim("nureig", "Ehre"), "sorge")], "BE", [("w1004", "ruhig"), ("nureig", "verachtet")]),
])

# ===========================================================================================================================
# C2 § 823 Abs. 1 BGB: schützt die Ehre, gibt aber nur Schadensersatz
# ===========================================================================================================================
W823 = ["„(1) Wer vorsätzlich oder fahrlässig das Leben, den Körper,",
        "die Gesundheit, die Freiheit, das Eigentum oder ein sonstiges",
        "Recht eines anderen widerrechtlich verletzt, ist dem anderen",
        "zum Ersatz des daraus entstehenden Schadens verpflichtet.“"]
w823, w823_y = wortlaut(80, 175, 1100, W823, "§ 823 Abs. 1 BGB", "p823", marken=[
    (1, "sonstiges", beim("p823", "allgemeine")), (3, "Ersatz des daraus entstehenden Schadens", beim("nurse", "Schadensersatz"))],
    size=31)
folie([("p823", f"{PP} › § 823 Abs. 1 BGB schützt die Ehre"), ("nurse", f"{PP} › § 823 Abs. 1 BGB: nur Schadensersatz"),
       ("kunft", f"{PP} › keine Unterlassung künftiger Beleidigungen")], [
    *tafel("p823", "Und § 823 Abs. 1 BGB?"),
    *w823,
    *okz("schützt auch das allgemeine Persönlichkeitsrecht,", w823_y + 34, beim("p823", "allgemeine"), "Bold", 33, x=160),
    z("also die Ehre", 160, w823_y + 78, beim("p823", "Ehre"), "Bold", 33),
    zit("BGH, Urt. v. 10.12.2024 – VI ZR 230/23, Rn. 14, 19", 400, w823_y + 86, beim("p823", "Ehre")),
    *neinz("Rechtsfolge: nur Schadensersatz für eine", w823_y + 148, "nurse", "Bold", 33, x=160),
    z("Verletzung, die schon geschehen ist", 160, w823_y + 192, beim("nurse", "Verletzung"), "Bold", 33),
    *neinz("keine Unterlassung künftiger Beleidigungen", w823_y + 254, "kunft", "Bold", 33, x=160),
    *requisit([("p823", ("tabler", "user-shield", 110, PINK), "Ehre", PINK),
               ("nurse", ("tabler", "coin-euro", 110, GELB), "nur Schadensersatz", GELB),
               ("kunft", ("tabler", "calendar-event", 110, WEISS), "und künftig?", WEISS)]),
    *paar("IL", [("p823", "ruhig"), ("kunft", "traurig")], "BE", [("p823", "denkt"), ("kunft", "verachtet")]),
])

# ===========================================================================================================================
# C3 Was ist eine Analogie? Norm auf einen Fall übertragen, den ihr Wortlaut nicht erfasst – erst nach der Auslegung
# ===========================================================================================================================
PA = "Analogie"
folie([("ana", f"{PA} · Norm auf einen ungeregelten Fall übertragen"), ("erst", f"{PA} › erst nach der Auslegung")], [
    *tafel("ana", "Was ist eine Analogie?"),
    z("Eine Norm wird auf einen Fall übertragen,", 110, 180, "ana", "Bold", 34),
    z("den ihr Wortlaut nicht erfasst.", 110, 226, beim("ana", "Wortlaut"), "Bold", 34),
    blk(110, 320, 400, 150, BLAUHELL, beim("ana", "Norm"), [("geregelt:", "Regular", 31, INK),
                                                         ("§ 1004 BGB", "ExtraBold", 34, INK),
                                                         ("Eigentum", "Regular", 31, INK)]),
    pfeil(530, 395, 720, 395, beim("ana", "übertragen"), breite=10, kopf=30),
    z("entsprechend", 548, 338, beim("ana", "übertragen"), "Bold", 28),
    blk(740, 320, 410, 150, PINK, beim("ana", "Fall"), [("ungeregelt:", "Regular", 31, INK),
                                                     ("Ehre", "ExtraBold", 34, INK),
                                                     ("Wortlaut erfasst sie nicht", "Regular", 28, INK)]),
    blk(110, 540, 1040, 84, GELBHELL, "erst", [("erst, wenn die Auslegung ausgeschöpft ist", "ExtraBold", 34, INK)]),
    *requisit([("ana", ("tabler", "arrows-right", 110, WEISS), "Analogie", GELB),
               ("erst", ("tabler", "book", 110, WEISS), "erst auslegen", GELBHELL)]),
    *paar("IL", [("ana", "denkt"), ("erst", "ruhig")], "BE", [("ana", "ruhig"), ("erst", "denkt")]),
])

# ===========================================================================================================================
# D1 Die BGH-Formel (Zitatkarte, BGH IX ZR 91/24, Rn. 14)
# ===========================================================================================================================
PV = "Voraussetzungen"
BGHF = ["„Die analoge Anwendung einer Vorschrift ist nur dann zulässig,",
        "wenn das Gesetz eine planwidrige Regelungslücke enthält und",
        "der zu beurteilende Sachverhalt in rechtlicher Hinsicht soweit",
        "mit dem Tatbestand, den der Gesetzgeber geregelt hat,",
        "vergleichbar ist, dass angenommen werden kann, der Gesetzgeber",
        "wäre bei einer Interessenabwägung, … zu dem gleichen",
        "Abwägungsergebnis gekommen.“"]
bghf, bghf_y = wortlaut(80, 175, 1100, BGHF, "BGH, Urt. v. 16.1.2025 – IX ZR 91/24, Rn. 14", "bgh", marken=[
    (1, "planwidrige Regelungslücke", beim("bgh", "planwidrige")), (4, "vergleichbar", beim("vgl", "vergleichbar")),
    (5, "gleichen", beim("abw", "gleichen")), (6, "Abwägungsergebnis", beim("abw", "Abwägungsergebnis"))], size=30)
folie([("bgh", f"{PV} · die BGH-Formel"), (beim("bgh", "planwidrige"), f"{PV} › planwidrige Regelungslücke"),
       ("vgl", f"{PV} › vergleichbarer Sachverhalt"), ("abw", f"{PV} › gleiches Abwägungsergebnis")], [
    *tafel("bgh", "Die Formel des Bundesgerichtshofs"),
    *bghf,
    zit("ebenso BGH, Urt. v. 24.2.2021 – VIII ZR 36/20, Rn. 38 („st. Rspr.“)", 110, bghf_y + 24, "abw"),
    *requisit([("bgh", ("tabler", "gavel", 120, HOLZ), "Bundesgerichtshof", WEISS),
               (beim("bgh", "planwidrige"), ("tabler", "puzzle", 110, GELB), "Lücke", GELB),
               ("vgl", ("tabler", "scale", 120, HELLGRUEN), "vergleichbar", HELLGRUEN)]),
    *stehend("IL", FX, [("bgh", "ruhig"), ("vgl", "denkt"), ("abw", "froh")]),
])

# ===========================================================================================================================
# D2 Drei Schritte, je eigene Farbe (Gelb, Lila, Grün)
# ===========================================================================================================================
folie([("drei", f"{PV} · drei Schritte"), ("s1", f"{PV} › 1. Regelungslücke"), ("s2", f"{PV} › 2. planwidrig"),
       ("s3", f"{PV} › 3. vergleichbare Interessenlage")], [
    *tafel("drei", "Analogie in drei Schritten"),
    blk(110, 190, 1040, 110, GELB, "s1", [("1. Regelungslücke", "ExtraBold", 40, INK)]),
    blk(110, 340, 1040, 110, LILA, "s2", [("2. Die Lücke ist planwidrig", "ExtraBold", 40, INK)]),
    blk(110, 490, 1040, 110, GRUEN, "s3", [("3. vergleichbare Interessenlage", "ExtraBold", 40, INK)]),
    *requisit([("drei", ("tabler", "list-numbers", 110, WEISS), "drei Schritte", WEISS),
               ("s1", ("tabler", "puzzle", 110, GELB), "Lücke", GELB),
               ("s2", ("tabler", "eye-off", 110, LILA), "übersehen?", LILA),
               ("s3", ("tabler", "scale", 120, GRUEN), "vergleichbar?", GRUEN)]),
    *paar("IL", [("drei", "ruhig"), ("s3", "froh")], "BE", [("drei", "denkt"), ("s2", "ruhig")]),
])

# ===========================================================================================================================
# E1 1. Regelungslücke (Gelb)
# ===========================================================================================================================
P1 = "1. Regelungslücke"
folie([("l1", f"{P1} · keine Norm erfasst den Fall"), ("l2", f"{P1} › bei Ilona"), ("l3", f"{P1} (+)")], [
    *schritt_tafel(1, "l1", "1. Regelungslücke"),
    z("Keine Norm erfasst den Fall,", 110, 185, "l1", "Bold", 36),
    z("auch nicht nach Auslegung.", 110, 233, beim("l1", "auch"), "Bold", 36),
    zit("vgl. BGH IX ZR 91/24, Rn. 10–13: erst direkte, dann analoge Anwendung", 110, 290, beim("l1", "auch")),
    z("Bei Ilona:", 110, 370, "l2", "ExtraBold", 34),
    *neinz("§ 1004 BGB erfasst nur das Eigentum", 425, beim("l2", "Paragraf"), "Bold", 34, x=160),
    *neinz("§ 823 Abs. 1 BGB gibt nur Schadensersatz", 480, beim("l2", "Paragraf", 2), "Bold", 34, x=160),
    blk(110, 570, 1040, 84, GELB, "l3", [("Regelungslücke (+)", "ExtraBold", 36, INK)]),
    *requisit([("l1", ("tabler", "puzzle", 110, GELB), "Lücke?", GELB),
               ("l3", ("tabler", "circle-check", 110, GELB), "Lücke (+)", GELB)]),
    *paar("IL", [("l1", "ruhig"), ("l2", "denkt"), ("l3", "froh")], "BE", [("l1", "denkt"), ("l3", "sorge")]),
])

# ===========================================================================================================================
# E2a 2. planwidrig (Lila): Fall übersehen, nicht bewusst ausgespart (IX ZR 91/24 Rn. 15; VIII ZR 36/20 Rn. 43 f.)
# ===========================================================================================================================
P2 = "2. planwidrig"
folie([("pw1", f"{P2} · Fall übersehen"), ("pw2", f"{P2} › bewusst ausgespart: keine Analogie"),
       ("pw3", f"{P2} › Entstehungsgeschichte und Zweck"), ("pw4", f"{P2} › Beispiel Kilometerleasing")], [
    *schritt_tafel(2, "pw1", "2. Die Lücke ist planwidrig"),
    z("Gesetzgeber unbeabsichtigt vom Regelungsplan", 110, 180, "pw1", "Bold", 34),
    z("abgewichen: Fall übersehen", 110, 226, beim("pw1", "übersehen"), "Bold", 34),
    zit("BGH, Urt. v. 16.1.2025 – IX ZR 91/24, Rn. 15", 110, 276, beim("pw1", "übersehen")),
    *neinz("bewusst ausgespart: keine Analogie", 330, "pw2", "Bold", 34),
    z("Prüfen: Entstehungsgeschichte und Zweck", 140, 410, "pw3", "Bold", 34),
    blk(110, 490, 1040, 130, LILAMITTEL, "pw4", [("Beispiel Leasing mit Kilometerabrechnung:", "ExtraBold", 32, INK),
                                               ("Gesetzgeber hat die Fälle bewusst beschränkt", "Regular", 32, INK)]),
    zit("BGH, Urt. v. 24.2.2021 – VIII ZR 36/20, Rn. 43 f. (§ 506 Abs. 2 BGB)", 110, 634, beim("pw4", "bewusst")),
    *requisit([("pw1", ("tabler", "eye-off", 110, LILA), "übersehen", LILA),
               ("pw2", ("tabler", "ban", 100, HELLROT), "bewusst: nein", HELLROT),
               ("pw3", ("tabler", "history", 110, LILAMITTEL), "Historie, Zweck", LILAMITTEL),
               ("pw4", ("tabler", "car", 120, WEISS), "Kilometerleasing", WEISS)]),
    *paar("IL", [("pw1", "denkt"), ("pw4", "ruhig")], "BE", [("pw1", "ruhig"), ("pw2", "denkt")]),
])

# ===========================================================================================================================
# E2b 2. planwidrig bei Ilona: Systematik §§ 12, 862, 1004 BGB
# ===========================================================================================================================
def kachel(x, cue, icon_, zeilen, fill):
    """Normkachel: Icon über einem Block mit drei Zeilen."""
    return [ficon("tabler", icon_, x + 120, 296, 60, cue, fuell=WEISS),
            blk(x, 310, 240, 190, fill, cue, [(t, st, 29, INK) for t, st in zeilen])]


folie([("pwf", f"{P2} › bei Ilona: Systematik"), ("sys", f"{P2} › Unterlassung in §§ 12, 862, 1004 BGB"),
       ("ehre", f"{P2} › Ehre schutzlos? nicht erkennbar"), (beim("ehre", "erkennbar"), f"{P2} (+)")], [
    *schritt_tafel(2, "pwf", "2. planwidrig: die Systematik"),
    z("Unterlassungsansprüche im BGB:", 110, 170, "sys", "Bold", 34),
    *kachel(110, beim("sys", "Namen"), "id", [("§ 12 BGB", "ExtraBold"), ("Name", "Bold"), ("Unterlassung", "Regular")],
            BLAUHELL),
    *kachel(375, beim("sys", "Besitz"), "key", [("§ 862 BGB", "ExtraBold"), ("Besitz", "Bold"), ("Unterlassung", "Regular")],
            BLAUHELL),
    *kachel(640, beim("sys", "Eigentum"), "home", [("§ 1004 BGB", "ExtraBold"), ("Eigentum", "Bold"),
                                                   ("Unterlassung", "Regular")], BLAUHELL),
    *kachel(905, "ehre", "user-shield", [("Ehre", "ExtraBold"), ("§ 823 schützt", "Bold"), ("Unterlassung?", "Regular")],
            PINK),
    z("schutzlos gewollt? nicht erkennbar", 110, 540, beim("ehre", "schutzlos"), "Bold", 34),
    blk(110, 610, 1040, 84, LILA, beim("ehre", "erkennbar"), [("planwidrige Lücke (+)", "ExtraBold", 36, INK)]),
    zit("Argument aus der Systematik (Wortlaut §§ 12, 862, 1004 BGB)", 110, 708, beim("ehre", "erkennbar")),
    *requisit([("pwf", ("tabler", "puzzle", 110, LILA), "Systematik", LILA),
               (beim("ehre", "erkennbar"), ("tabler", "circle-check", 110, LILA), "planwidrig (+)", LILA)]),
    *paar("IL", [("pwf", "ruhig"), ("ehre", "denkt"), (beim("ehre", "erkennbar"), "froh")],
          "BE", [("pwf", "denkt"), (beim("ehre", "erkennbar"), "sorge")]),
])

# ===========================================================================================================================
# E3 3. vergleichbare Interessenlage (Grün; VIII ZR 36/20 Rn. 41; Zitatkarte I ZR 12/23 Rn. 16)
# ===========================================================================================================================
P3 = "3. vergleichbare Interessenlage"
ZI = ["„Genauso, wie es dem Inhaber eines deliktsrechtlich geschützten",
      "Rechtsguts nicht zuzumuten ist, tatenlos eine",
      "Rechtsgutsverletzung hinzunehmen, …“"]
zi, zi_y = wortlaut(80, 300, 1100, ZI, "BGH, Urt. v. 2.5.2024 – I ZR 12/23, Rn. 16", "vi2", marken=[
    (1, "nicht zuzumuten", beim("vi2", "zuzumuten")), (1, "tatenlos", beim("vi2", "tatenlos"))], size=31)
folie([("vi1", f"{P3} · Wertung passt auf den neuen Fall"), ("vi2", f"{P3} › nicht tatenlos hinnehmen"),
       ("vi3", f"{P3} (+)")], [
    *schritt_tafel(3, "vi1", "3. vergleichbare Interessenlage"),
    z("Die Wertung der Norm passt auch", 110, 180, "vi1", "Bold", 34),
    z("auf den neuen Fall.", 110, 226, beim("vi1", "neuen"), "Bold", 34),
    zit("BGH, Urt. v. 24.2.2021 – VIII ZR 36/20, Rn. 41", 520, 234, beim("vi1", "neuen")),
    *zi,
    *okz("Ehre wie Eigentum: vergleichbar", zi_y + 34, "vi3", "Bold", 34, x=160),
    blk(110, zi_y + 104, 1040, 84, GRUEN, beim("vi3", "Eigentum"), [("vergleichbare Interessenlage (+)", "ExtraBold", 36, INK)]),
    *requisit([("vi1", ("tabler", "scale", 120, GRUEN), "Wertung", GRUEN),
               ("vi2", ("tabler", "hand-stop", 110, WEISS), "nicht tatenlos", WEISS),
               ("vi3", ("tabler", "circle-check", 110, GRUEN), "vergleichbar (+)", GRUEN)]),
    *paar("IL", [("vi1", "denkt"), ("vi2", "ruhig"), ("vi3", "strahlt")], "BE", [("vi1", "ruhig"), ("vi3", "sorge")]),
])

# ===========================================================================================================================
# F Rechtsprechung: quasinegatorischer Unterlassungsanspruch (V ZR 110/14 Rn. 20; VI ZR 230/23 Rn. 14; Verweis Folge 142)
# ===========================================================================================================================
PR = "Rechtsprechung"
folie([("rspr", f"{PR} · so sieht es der BGH"), ("qn", f"{PR} › § 1004 BGB für alle Rechtsgüter des § 823 BGB"),
       ("qn2", f"{PR} › quasinegatorischer Unterlassungsanspruch"), ("agl", f"{PR} › Anspruchsgrundlage"),
       ("f142", f"{PR} › beim Eigentum: Folge zu § 1004 BGB")], [
    *tafel("rspr", "Der quasinegatorische Anspruch"),
    *okz("§ 1004 BGB entsprechend für alle Rechtsgüter,", 180, "qn", "Bold", 34),
    z("die § 823 BGB schützt", 185, 226, beim("qn", "Rechtsgüter"), "Bold", 34),
    zit("BGH, Urt. v. 16.1.2015 – V ZR 110/14, Rn. 20", 185, 276, beim("qn", "Rechtsgüter")),
    blk(110, 330, 1040, 76, GELB, "qn2", [("quasinegatorischer Unterlassungsanspruch", "ExtraBold", 34, INK)]),
    z("Anspruchsgrundlage bei Ehrverletzungen:", 110, 450, "agl", "Bold", 34),
    blk(110, 505, 1040, 130, BLAUHELL, beim("agl", "Paragraf"), [("§ 1004 Abs. 1 S. 2 BGB analog i. V. m.", "ExtraBold", 33, INK),
                                                              ("§ 823 Abs. 1 BGB, Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "Bold", 31, INK)]),
    zit("BGH, Urt. v. 10.12.2024 – VI ZR 230/23, Rn. 14; Urt. v. 4.12.2018 – VI ZR 128/18, Rn. 5", 110, 648,
        beim("agl", "Paragraf")),
    z("beim Eigentum: Folge zu § 1004 BGB (Beseitigung)", 110, 720, "f142", "Bold", 32),
    *requisit([("rspr", ("tabler", "gavel", 120, HOLZ), "Rechtsprechung", WEISS),
               ("qn2", ("tabler", "hand-stop", 110, GELB), "Unterlassung", GELB),
               ("agl", ("tabler", "user-shield", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("f142", ("tabler", "home", 110, BLAUHELL), "§ 1004 BGB", BLAUHELL)]),
    *paar("IL", [("rspr", "ruhig"), ("agl", "froh")], "BE", [("rspr", "denkt"), ("qn2", "sorge")]),
])

# ===========================================================================================================================
# G Einzelanalogie und Gesamtanalogie (Rechtsanalogie; V ZR 56/12 Rn. 17)
# ===========================================================================================================================
PG = "Arten der Analogie"
folie([("einzel", f"{PG} · Einzelanalogie"), ("gesamt", f"{PG} › Gesamtanalogie (Rechtsanalogie)"),
       ("gbsp", f"{PG} › Beispiel: Leihe und Auftrag")], [
    *tafel("einzel", "Einzelanalogie und Gesamtanalogie"),
    blk(110, 180, 505, 200, BLAUHELL, "einzel", [("Einzelanalogie", "ExtraBold", 34, INK),
                                              ("eine einzelne Norm", "Regular", 31, INK),
                                              ("wird übertragen:", "Regular", 31, INK),
                                              ("§ 1004 BGB analog", "Bold", 31, INK)]),
    blk(645, 180, 505, 200, LILAMITTEL, "gesamt", [("Gesamtanalogie", "ExtraBold", 34, INK),
                                                ("(Rechtsanalogie): aus", "Regular", 31, INK),
                                                ("mehreren Normen ein", "Regular", 31, INK),
                                                ("gemeinsamer Grundgedanke", "Regular", 31, INK)]),
    z("Beispiel:", 110, 430, "gbsp", "ExtraBold", 34),
    blk(110, 485, 330, 110, WEISS, beim("gbsp", "Leihe"), [("§ 604 Abs. 3 BGB", "ExtraBold", 31, INK),
                                                         ("Leihe", "Regular", 31, INK)]),
    z("+", 456, 515, beim("gbsp", "Auftrag"), "ExtraBold", 44),
    blk(490, 485, 330, 110, WEISS, beim("gbsp", "Auftrag"), [("§ 671 Abs. 1 BGB", "ExtraBold", 31, INK),
                                                           ("Auftrag", "Regular", 31, INK)]),
    blk(110, 625, 1040, 84, GELB, beim("gbsp", "unentgeltliche"),
        [("unentgeltliche Versorgungsvereinbarung: jederzeit kündbar", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 8.2.2013 – V ZR 56/12, Rn. 17 („in Rechtsanalogie“)", 110, 722, beim("gbsp", "unentgeltliche")),
    *requisit([("einzel", ("tabler", "file-text", 110, BLAUHELL), "eine Norm", BLAUHELL),
               ("gesamt", ("tabler", "files", 110, LILAMITTEL), "mehrere Normen", LILAMITTEL),
               (beim("gbsp", "unentgeltliche"), ("tabler", "gift", 110, GELB), "unentgeltlich", GELB)]),
    *paar("IL", [("einzel", "ruhig"), ("gesamt", "denkt")], "BE", [("einzel", "denkt"), ("gbsp", "ruhig")]),
])

# ===========================================================================================================================
# H Gegenstücke: Umkehrschluss und teleologische Reduktion (BVerwG 6 C 17/09 Rn. 30; Verweis Folge 159)
# ===========================================================================================================================
PH = "Gegenstücke"
folie([("gegen", f"{PH} · aus der Folge zu den Auslegungsmethoden"), ("uk", f"{PH} › Umkehrschluss"),
       ("tr", f"{PH} › teleologische Reduktion")], [
    *tafel("gegen", "Zwei Gegenstücke zur Analogie"),
    zit("ausführlich: Folge zu den Auslegungsmethoden", 110, 170, beim("gegen", "Auslegungsmethoden")),
    blk(110, 225, 1040, 170, BLAUHELL, "uk", [("Umkehrschluss", "ExtraBold", 34, INK),
                                          ("Regelt das Gesetz einen Fall abschließend,", "Regular", 31, INK),
                                          ("gilt die Rechtsfolge für andere Fälle nicht.", "Regular", 31, INK)]),
    zit("argumentum e contrario", 820, 238, "uk"),
    blk(110, 440, 1040, 170, LILAMITTEL, "tr", [("teleologische Reduktion", "ExtraBold", 34, INK),
                                             ("Der Wortlaut erfasst einen Fall, den der", "Regular", 31, INK),
                                             ("Zweck der Norm nicht erfassen soll.", "Regular", 31, INK)]),
    zit("BVerwG, Urt. v. 27.10.2010 – 6 C 17/09, Rn. 30: „Gegenstück zur Analogie“", 110, 625, beim("tr", "Wortlaut")),
    *requisit([("gegen", ("tabler", "arrows-exchange", 110, WEISS), "Gegenstücke", WEISS),
               ("uk", ("tabler", "arrow-back-up", 110, BLAUHELL), "Umkehrschluss", BLAUHELL),
               ("tr", ("tabler", "scissors", 110, LILAMITTEL), "Reduktion", LILAMITTEL)]),
    *paar("IL", [("gegen", "ruhig"), ("tr", "denkt")], "BE", [("gegen", "denkt"), ("uk", "ruhig")]),
])

# ===========================================================================================================================
# I Grenzen: Wortlautkarte Art. 103 Abs. 2 GG (BVerfG 2 BvR 2500/09 Rn. 164 f.; Verweis Folge 148), Vorbehalt des Gesetzes
# ===========================================================================================================================
PI = "Grenzen"
W103 = ["„(2) Eine Tat kann nur bestraft werden, wenn die Strafbarkeit",
        "gesetzlich bestimmt war, bevor die Tat begangen wurde.“"]
w103, w103_y = wortlaut(80, 175, 1100, W103, "Art. 103 Abs. 2 GG", "a103", marken=[
    (1, "gesetzlich bestimmt", beim("a103", "gesetzlich"))], size=31)
folie([("grenz", f"{PI} · Grenzen der Analogie"), ("a103", f"{PI} › Strafrecht: Art. 103 Abs. 2 GG"),
       ("av", f"{PI} › Verbot strafbegründender Analogie"), ("oer", f"{PI} › Öffentliches Recht: Vorbehalt des Gesetzes")], [
    *tafel("grenz", "Grenzen der Analogie"),
    *w103,
    blk(110, w103_y + 26, 1040, 84, HELLROT, "av", [("Verbot strafbegründender Analogie", "ExtraBold", 34, INK)]),
    *neinz("nie zulasten des Täters", w103_y + 128, beim("av", "Zulasten"), "Bold", 34, x=160),
    zit("BVerfG, Beschl. v. 7.12.2011 – 2 BvR 2500/09, Rn. 164 f.; Folge zur Unfallflucht", 160, w103_y + 176,
        beim("av", "Unfallflucht")),
    linienzug([(110, w103_y + 230), (1150, w103_y + 230)], "oer", breite=3),
    z("Öffentliches Recht: Vorbehalt des Gesetzes", 110, w103_y + 255, "oer", "ExtraBold", 34),
    z("belastender Eingriff braucht eine gesetzliche", 160, w103_y + 308, beim("oer", "belastender"), "Bold", 33),
    z("Grundlage", 160, w103_y + 352, beim("oer", "Grundlage"), "Bold", 33),
    zit("vgl. Art. 20 Abs. 3 GG", 340, w103_y + 360, beim("oer", "Grundlage")),
    *neinz("Analogie ersetzt sie nicht einfach", w103_y + 414, "oer2", "Bold", 33, x=160),
    *requisit([("grenz", ("tabler", "barrier-block", 120, WEISS), "Grenzen", WEISS),
               ("a103", ("tabler", "book", 110, WEISS), "Art. 103 Abs. 2 GG", WEISS),
               ("av", ("tabler", "ban", 100, HELLROT), "Strafrecht: Verbot", HELLROT),
               ("oer", ("tabler", "building-bank", 110, BLAUHELL), "Öffentliches Recht", BLAUHELL)]),
    *paar("IL", [("grenz", "ruhig"), ("oer", "denkt")], "BE", [("grenz", "denkt"), ("av", "ruhig")]),
])

# ===========================================================================================================================
# J Lösung: zurück im Gerichtssaal (gleiche Bühne wie A2, weil die Geschichte zum Prozess zurückkehrt)
# ===========================================================================================================================
folie([("loes", "Lösung · zurück vor Gericht"), ("loes1", "Lösung › Analogie (+)"),
       ("abwg", "Lösung › Ehre verletzt, Meinungsfreiheit deckt es nicht"), ("wg", "Lösung › Wiederholungsgefahr vermutet"),
       ("ri2", "Lösung › Urteil: Unterlassung"), ("erg", "Ergebnis · Unterlassungsanspruch analog § 1004 BGB")], [
    *fig("RI", RIX, RIU, RIH, [("loes", "ruhig"), ("loes1", "denkt")], bis="ri2", erst="cut"),
    *redet("RI_redet", RIX, RIU, RIH, "ri2", "erg"),
    *fig("RI", RIX, RIU, RIH, [("erg", "froh")], erst="cut"),
    *gerichtssaal("loes"),
    hart(ficon("tabler", "gavel", RIX + 170, RT_O + 4, 110, "loes", fuell=HOLZ, anim="cut", bis="ri2")),
    szene(ficon("tabler", "gavel", RIX + 170, RT_O + 4, 130, "ri2", fuell=HOLZ, anim="pop"), "162hammer*", 1.0, -0.02),
    hart(ns("Richterin", RIX, BODEN - 40, "loes", WEISS)),
    *fig("IL", GIX, BODEN, FH, [("loes", "denkt_r"), ("loes1", "ruhig_r"), ("ri2", "froh_r"), ("erg", "strahlt_r")],
         erst="cut"),
    hart(ns("Ilona", GIX, BODEN, "loes", PINK)),
    *fig("BE", GRX, BODEN, FH, [("loes", "ruhig"), ("abwg", "sorge"), ("ri2", "ernst")], erst="cut"),
    hart(ns("Bertold", GRX, BODEN, "loes", ORANGE)),
    pl("Lücke (+) · planwidrig (+) · vergleichbar (+)", 70, 40, "loes1", fill=GRUEN, size=30, bis="ri2"),
    pl("Die Richterin darf die Lücke schließen.", 70, 104, beim("loes1", "darf"), fill=WEISS, size=30, bis="ri2"),
    pl("Ehre verletzt, von der Meinungsfreiheit nicht gedeckt", 1180, 260, beim("abwg", "Beleidigungen"), fill=HELLROT,
       size=28, anker="m", bis="ri2"),
    pl("Wiederholungsgefahr vermutet", 1180, 330, "wg", fill=GELB, size=28, anker="m", bis="ri2"),
    blase("sprech", 660, 200, "ri2", 600, 240, inhalt=["Der Beklagte muss die beleidigenden", "Äußerungen künftig unterlassen."],
          textsize=30, figur=("RI_redet", RIX, RIU, RIH), bis="erg"),
    pl("Unterlassungsanspruch analog § 1004 BGB", 960, 130, "erg", fill=GELB, size=34, anker="m"),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst Auslegung, dann Analogie"), ("tipp2", "Klausurtipp · nie nur „analog“"),
       ("tipp3", "Klausurtipp · Lücke – planwidrig – vergleichbar")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Analogie erst prüfen, wenn die", 200, 200, "tipp", "Bold", 36),
    z("Auslegung gescheitert ist", 200, 248, beim("tipp", "Auslegung"), "Bold", 36),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    *neinz("nie nur „analog“ schreiben", 365, "tipp2", "Bold", 36, x=200),
    blk(130, 460, 1000, 150, GELBHELL, "tipp3", [("begründen:", "ExtraBold", 34, INK),
                                              ("Lücke – planwidrig – vergleichbar", "ExtraBold", 36, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema (Farbpunkte der drei Schritte)
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. keine direkte Anwendung, auch nicht nach Auslegung", None),
          ("k2", 0, "II. Analogie", None),
          ("k2a", 1, "1. Regelungslücke", GELB),
          ("k2b", 1, "2. Planwidrigkeit", LILA),
          ("k2c", 1, "3. vergleichbare Interessenlage", GRUEN),
          ("k3", 0, "III. keine Grenze, etwa Analogieverbot (Art. 103 Abs. 2 GG)", None),
          ("k4", 0, "IV. Rechtsfolge: entsprechend anwenden", None)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel("Prüfschema: die Analogie", 110, 90, "sch", 46)]
y = 200
for c, ebene, text, farbe in REIHEN:
    x = (130, 230)[ebene]
    if farbe:
        im = Image.new("RGBA", (34, 34)); ImageDraw.Draw(im).ellipse((0, 0, 33, 33), fill=farbe, outline=INK, width=4)
        els_sch.append(El(im, x - 54, y + 12, c, "pop", 0.0, None, name="punkt"))
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Bold", 42 if ebene == 0 else 40, rechts=1800))
    y += {0: 104, 1: 92}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. keine direkte Anwendung"), ("k2", "Prüfschema › II. Analogie"),
       ("k2a", "Prüfschema › II. 1. Regelungslücke"), ("k2b", "Prüfschema › II. 2. Planwidrigkeit"),
       ("k2c", "Prüfschema › II. 3. vergleichbare Interessenlage"), ("k3", "Prüfschema › III. keine Grenze"),
       ("k4", "Prüfschema › IV. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Eine Analogie überträgt eine Norm", 0)], [("auf einen ", 0), ("ungeregelten Fall", "a"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "ungeregelten")}),
    *markertext([[("Sie trägt nur, wenn die Lücke", 0)], [("planwidrig", "b"), (" und die Interessenlage", 0)],
                 [("vergleichbar", "c"), (" ist.", 0)]], 750, 500, 44, "m2",
                {"b": beim("m2", "planwidrig"), "c": beim("m2", "vergleichbar")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
