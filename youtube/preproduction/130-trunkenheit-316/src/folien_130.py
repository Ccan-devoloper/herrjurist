"""Folge 130 · Trunkenheit im Verkehr § 316: 0,3 – 0,5 – 1,1 – 1,6 Promille – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Verkehrskontrolle am Ortsausgang; eine Polizistin hält Heinrich (0,8 ‰, fährt schnurgerade, keine
Ausfallerscheinungen) und Siegfried (1,2 ‰, fährt unauffällig, hält sich für fit) an. Niemand wird gefährdet.
Szenen laut ../SZENENPLAN.md: A1 Kontrolle Heinrich, A2 Kontrolle Siegfried, B Sachverhalt, C Wortlautkarte § 316 Abs. 1,
D absolute Fahruntüchtigkeit (1,1 ‰, Radfahrer 1,6 ‰), E relative Fahruntüchtigkeit (etwa ab 0,3 ‰), F Wortlautkarte
§ 24a Abs. 1 StVG (0,5 ‰), G Vorsatz/Fahrlässigkeit, H Abgrenzung § 315c, I Ergebnis, J Klausurtipp (Lexi),
K Prüfschema, L Merksatz (Lexi). Promille-Skala als Thermometer (skala()) rechts neben der Tafel in D–G, wächst Wert für Wert.
DARSTELLUNG: kein Alkoholkonsum im Bild, nur ein neutrales Glas-Icon bei „alkoholischer Getränke“; nüchterner Ton.
Zwei Handlungsgeräusche (Ankunft der beiden Autos an der Kontrollstelle; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 124 (gemeinsame Dateien unverändert); neu: kontrollstelle(), ortsschild(), skala().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_130/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_130/" in n:
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



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
ASPH = (200, 200, 198, 255)
GRAS = (205, 234, 196, 255)
STR_O, STR_U = 700, 850                      # Fahrbahn (Seitenansicht): Oberkante, Unterkante
FAHR = 836                                   # Unterkante der Autos und der Figuren auf der Fahrbahn
FH = 440                                     # Figur auf der Fahrbahn


def kontrollstelle(cue):
    """Landstraße am Ortsausgang in Seitenansicht: Asphalt mit Randlinie (durchgezogen) und Bankett, kein Mittelstreifen."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (1000 - STR_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (STR_U - STR_O) * s), fill=ASPH)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (STR_U - STR_O) * s, 1860 * s, (STR_U - STR_O) * s), fill=INK, width=6 * s)
    dr.rectangle((0, 18 * s, 1860 * s, 26 * s), fill=WEISS)          # durchgezogene Randlinie
    dr.rectangle((0, (STR_U - STR_O + 3) * s, 1860 * s, (1000 - STR_O) * s), fill=GRAS)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    e = El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")
    return e


def ortsschild(cx, boden_, cue):
    """Ortsausgangsschild als Grundform: gelbe Tafel, zwei dunkle Schriftbalken (ohne realen Ortsnamen), roter
    Schrägstrich, grauer Pfosten."""
    s = 2
    w, h, hp = 170, 110, 80
    im = Image.new("RGBA", ((w + 12) * s, (h + hp + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle(((w / 2 - 2) * s, h * s, (w / 2 + 14) * s, (h + hp + 6) * s), 4 * s, fill=(150, 150, 150, 255),
                         outline=INK, width=3 * s)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 10 * s, fill=GELB, outline=INK, width=5 * s)
    dr.rounded_rectangle((34 * s, 30 * s, (w - 22) * s, 48 * s), 6 * s, fill=(70, 70, 70, 255))
    dr.rounded_rectangle((50 * s, 66 * s, (w - 38) * s, 82 * s), 6 * s, fill=(70, 70, 70, 255))
    dr.line((22 * s, (h - 4) * s, (w - 10) * s, 18 * s), fill=DROT, width=13 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, boden_ - im.height, cue, "cut", 0.0, None, name="ortsschild")


def kulisse(c):
    """Kulisse der Kontrollstelle: Straße, Bäume, Ortsausgangsschild (für jede Folie neu erzeugt)."""
    h = (lambda e: hart(e)) if c == NULL else (lambda e: e)
    return [h(kontrollstelle(c)),
            h(ficon("tabler", "trees", 450, STR_O + 4, 190, c, fuell=GRUEN, anim="cut")),
            h(ficon("tabler", "trees", 660, STR_O + 4, 160, c, fuell=GRUEN, anim="cut")),
            h(ortsschild(150, STR_O + 4, c))]


def polizei(c, d=0.0):
    """Streifenwagen (Fluent Emoji) und zwei Leitkegel (Tabler) rechts an der Kontrollstelle."""
    return [ficon("fluent-emoji-flat", "police-car", 1700, FAHR, 300, c, d=d),
            ficon("tabler", "cone", 1470, FAHR - 4, 62, c, fuell=ROT, d=d + 0.1),
            ficon("tabler", "cone", 1530, FAHR - 4, 62, c, fuell=ROT, d=d + 0.15)]


# --- Promille-Skala als Thermometer (rechts neben der Tafel) ------------------------------------------------------------
SKX, SKW = 1300, 46                          # Röhre: linke Kante, Breite
SK_O, SK_U, SK_MAX = 170, 880, 1.8           # y bei 1,8 ‰ und bei 0 ‰
SKL = SKX + SKW + 24                         # Beschriftung


def sky(p):
    return SK_U - p * (SK_U - SK_O) / SK_MAX


def _roehre():
    s = 2
    w, h = SKW + 60, SK_U - SK_O + 110
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    cx = w / 2
    dr.ellipse(((cx - 40) * s, (h - 84) * s, (cx + 40) * s, (h - 4) * s), fill=WEISS, outline=INK, width=5 * s)
    dr.rounded_rectangle(((cx - SKW / 2) * s, 4 * s, (cx + SKW / 2) * s, (h - 60) * s), int(SKW / 2) * s, fill=WEISS,
                         outline=INK, width=5 * s)
    dr.rectangle(((cx - SKW / 2 + 5) * s, (h - 90) * s, (cx + SKW / 2 - 5) * s, (h - 50) * s), fill=WEISS)
    im = im.resize((w, h), Image.LANCZOS)
    return im, SKX + SKW / 2 - w / 2, SK_O - 4


def _zone(p0, p1, farbe):
    im = Image.new("RGBA", (SKW - 14, int(sky(p0) - sky(p1))))
    ImageDraw.Draw(im).rectangle((0, 0, im.width, im.height), fill=farbe)
    return im, SKX + 7, sky(p1)


SCHWELLEN = {"03": (0.3, "0,3 ‰ relativ", None), "05": (0.5, "0,5 ‰ § 24a StVG", None),
             "11": (1.1, "1,1 ‰ absolut (Kfz)", (1.1, 1.72, ROT)), "16": (1.6, "1,6 ‰ Radfahrer", None)}
PERSON = {"SI": (1.2, "Siegfried: 1,2 ‰", GELB), "HE": (0.8, "Heinrich: 0,8 ‰", BLAU)}


def skala(start, cues):
    """Thermometer mit den Schwellen und Personenmarken; start = Folienstart (Röhre), cues = {schlüssel: cue}.
    Schwellen: 03, 05, 11, 16 (Zone über 1,1 ‰ rot, 0,3–1,1 ‰ gelb, sobald 03 erscheint); Personen: SI, HE."""
    im, x, y = _roehre()
    els = [El(im, x, y, start, "fade", 0.0, None, name="skala")]
    els.append(z("Blutalkohol", SKX - 30, 112, start, "Bold", 28, rechts=1640))
    els.append(z("0 ‰", SKL, sky(0) - 18, start, "Regular", 26, farbe=TEXT, rechts=1640))
    for k, c in cues.items():
        if k in SCHWELLEN:
            p, txt, zone = SCHWELLEN[k]
            if zone:
                zi, zx, zy = _zone(zone[0], zone[1], zone[2]); els.append(El(zi, zx, zy, c, "fade", 0.0, None, name="zone" + k))
            if k == "03":
                zi, zx, zy = _zone(0.3, 1.1, GELB); els.append(El(zi, zx, zy, c, "fade", 0.0, None, name="zone03"))
            els.append(linienzug([(SKX - 6, sky(p)), (SKX + SKW + 14, sky(p))], c, breite=5))
            els.append(z(txt, SKL, sky(p) - 17, c, "Bold", 28, rechts=1660))
        elif k in PERSON:
            p, txt, f = PERSON[k]
            r = 15
            dot = Image.new("RGBA", (2 * r + 6, 2 * r + 6))
            ImageDraw.Draw(dot).ellipse((3, 3, 2 * r + 3, 2 * r + 3), fill=f, outline=INK, width=4)
            els.append(El(dot, SKX + SKW / 2 - r - 3, sky(p) - r - 3, c, "pop", 0.0, None, name="punkt" + k))
            els.append(z(txt, SKL, sky(p) - 17, c, "ExtraBold", 28, farbe=INK, rechts=1660))
    return els


BODEN = 860
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
SFX_, SFB, SFR = 1775, 930, 430             # Figur neben dem Thermometer
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HE": "Heinrich", "SI": "Siegfried", "PO": "Polizistin"}
NFARBE = {"HE": BLAU, "SI": GELB, "PO": LILA}


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


# ===========================================================================================================================
# A1 Fall: Kontrolle Heinrich
# ===========================================================================================================================
CW = 360                                     # Autobreite
CA, CS = 360, 760                            # Auto: Startposition (steht ab 0,0 s im Bild), Halt an der Kontrollstelle
HEX, POX = 1060, 1320                        # Heinrich neben seinem Auto (blickt nach rechts), Polizistin (blickt nach links)
FAHRT = ("hein", 0.0)
HALT = beim("hein", "schnurgerade")
folie([(NULL, "Fall · Am Ortsausgang"), ("kontr", "Fall · Die Verkehrskontrolle"), ("p1", "Fall · Heinrich wird kontrolliert"),
       ("blut1", "Fall · Heinrich: 0,8 ‰")], [
    *kulisse(NULL),
    hart(pl("Ein Freitagnachmittag am Ortsausgang", 70, 30, NULL, fill=GELB, size=40)),
    pl("Verkehrskontrolle", 70, 120, "kontr", fill=WEISS, size=36),
    *polizei("kontr"),
    *fig("PO", POX, FAHR, FH, [("kontr", "ruhig")], bis="p1", erst="pop", d=0.2),
    *redet("PO_redet", POX, FAHR, FH, "p1", "test"),
    peep_voll("PO_ernst", POX, FAHR, FH, "test", anim="cut"),
    ns("Polizistin", POX, FAHR, "kontr", LILA, d=0.3),
    blase("sprech", 660, 220, "p1", 1230, 250, inhalt=["Allgemeine Verkehrskontrolle.", "Bitte einmal kräftig pusten."],
          textsize=34, figur=("PO_redet", POX, FAHR, FH), bis="test"),
    # Heinrichs Auto: steht ab 0,0 s, fährt schnurgerade heran und hält an der Kontrollstelle
    hart(ficon("tabler", "car", CA, FAHR, CW, NULL, fuell=BLAU, anim="cut", bis=FAHRT)),
    szene(bewegt(ficon("tabler", "car", CS, FAHR, CW, FAHRT, fuell=BLAU, anim="cut"), FAHRT, HALT, CA - CS, 0),
          "130anfahrt*", 0.8, 0.0),
    linienzug([(70, FAHR - 30), (CS - CW / 2 - 20, FAHR - 30)], HALT, breite=6, farbe=DGRUEN),
    pl("fährt schnurgerade, kein Fahrfehler", 70, 200, HALT, fill=HELLGRUEN, size=34),
    # Heinrich steigt aus (blickt nach rechts zur Polizistin), Atemtest, Blutprobe, redet
    *fig("HE", HEX, FAHR, FH, [("p1", "ruhig_r"), ("test", "staunt_r")], bis="h1", erst="pop"),
    *redet("HE_redet_r", HEX, FAHR, FH, "h1", "sieg"),
    ns("Heinrich", HEX, FAHR, "p1", BLAU, d=0.1),
    pl("Atemtest schlägt an", 70, 280, "test", fill=WEISS, size=34),
    ficon("tabler", "test-pipe", 520, 440, 70, "blut1", fuell=WEISS),
    pl("Blutprobe: 0,8 ‰", 70, 360, "blut1", fill=HELLROT, size=36),
    blase("sprech", 560, 210, "h1", 760, 520, inhalt=["Aber ich bin doch", "ganz normal gefahren!"], textsize=36,
          figur=("HE_redet_r", HEX, FAHR, FH), bis="sieg"),
])

# ===========================================================================================================================
# A2 Fall: Kontrolle Siegfried
# ===========================================================================================================================
SIX = 1060
FAHRT2 = ("sieg", 0.0)
HALT2 = beim("sieg", "Siegfried")
folie([("sieg", "Fall · Siegfried wird kontrolliert"), ("blut2", "Fall · Siegfried: 1,2 ‰"), ("niemand", "Fall · Niemand gefährdet"),
       ("frage", "Fall · Die Frage")], [
    *kulisse("sieg"),
    pl("Kurz darauf", 70, 30, "sieg", fill=GELB, size=40),
    *polizei("sieg"),
    peep_voll("PO_ruhig", POX, FAHR, FH, "sieg", anim="cut"),
    ns("Polizistin", POX, FAHR, "sieg", LILA, anim="cut"),
    szene(bewegt(ficon("tabler", "car", CS, FAHR, CW, FAHRT2, fuell=GELB, anim="cut"), FAHRT2, HALT2, CA - CS, 0),
          "130halt*", 0.8, 0.0),
    linienzug([(70, FAHR - 30), (CS - CW / 2 - 20, FAHR - 30)], beim("sieg", "unauffällig"), breite=6, farbe=DGRUEN),
    pl("fährt völlig unauffällig", 70, 120, beim("sieg", "unauffällig"), fill=HELLGRUEN, size=34),
    *fig("SI", SIX, FAHR, FH, [("blut2", "ruhig_r")], bis="s1", erst="pop"),
    *redet("SI_redet_r", SIX, FAHR, FH, "s1", "niemand"),
    *fig("SI", SIX, FAHR, FH, [("niemand", "froh_r")], erst="cut"),
    ns("Siegfried", SIX, FAHR, "blut2", GELB, d=0.1),
    ficon("tabler", "test-pipe", 470, 262, 56, "blut2", fuell=WEISS),
    pl("Blutprobe: 1,2 ‰", 70, 200, "blut2", fill=HELLROT, size=36),
    blase("sprech", 500, 170, "s1", 780, 520, inhalt=["Ich fühle mich topfit."], textsize=36,
          figur=("SI_redet_r", SIX, FAHR, FH), bis="niemand"),
    pl("niemand gefährdet oder verletzt", 70, 280, "niemand", fill=GRUEN, size=34),
    pl("Beide strafbar?", 70, 360, "frage", fill=PINK, size=36),
    pl("Oder einer nur ordnungswidrig?", 70, 440, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_130(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_130("sv", [
    "An einem Freitagnachmittag kontrolliert eine Polizistin am Ortsausgang den Verkehr. Heinrich fährt mit seinem Auto "
    "heran, schnurgerade und ohne jeden Fahrfehler; auch sonst zeigt er keine Auffälligkeiten. Der Atemtest schlägt an. "
    "Die Blutprobe ergibt eine Blutalkoholkonzentration von 0,8 ‰.",
    "Kurz darauf hält die Polizistin Siegfried an. Auch er ist völlig unauffällig gefahren. Seine Blutprobe ergibt 1,2 ‰. "
    "Siegfried hält sich für fahrtüchtig: „Ich fühle mich topfit.“",
    "Gefährdet oder verletzt wurde niemand.",
], "Wie haben sich Heinrich und Siegfried strafbar gemacht? Ordnungswidrigkeiten?")

# ===========================================================================================================================
# C Wortlautkarte § 316 Abs. 1 StGB, Führen im Verkehr, Kern, keine Promillezahl im Gesetz
# ===========================================================================================================================
P316 = "§ 316 StGB"
W316 = ["„Wer im Verkehr (§§ 315 bis 315e) ein Fahrzeug führt,",
        "obwohl er infolge des Genusses alkoholischer Getränke",
        "oder anderer berauschender Mittel nicht in der Lage ist,",
        "das Fahrzeug sicher zu führen, wird mit Freiheitsstrafe",
        "bis zu einem Jahr oder mit Geldstrafe bestraft, wenn die",
        "Tat nicht in § 315a oder § 315c mit Strafe bedroht ist.“"]
w316, w316_y = wortlaut(80, 165, 1100, W316, "§ 316 Abs. 1 StGB", "p316", marken=[
    (0, "im Verkehr", beim("p316", "Verkehr")), (0, "ein Fahrzeug führt", beim("p316", "Fahrzeug")),
    (1, "alkoholischer Getränke", beim("p316", "alkoholischer")), (2, "nicht in der Lage ist", "p316b"),
    (3, "sicher zu führen", beim("p316b", "sicher"))], size=32)
folie([("p316", f"{P316} › Wortlaut Abs. 1"), ("fuehr", f"{P316} › Führen eines Fahrzeugs im Verkehr"),
       ("kern", f"{P316} › Fahruntüchtigkeit infolge Alkohols"), ("zahl", f"{P316} › Grenzwerte: Beweisregeln")],
      rechts_frei([
    *tafel("p316", "Die Norm: § 316 Abs. 1 StGB"),
    *w316,
    *okz("Führen eines Fahrzeugs im Verkehr: beide (+)", w316_y + 26, beim("fuehr", "Auto"), "Bold", 32, x=160),
    z("Kern: Fahruntüchtigkeit infolge Alkohols", 110, w316_y + 96, beim("kern", "Fahruntüchtigkeit"), "Bold", 34),
    z("Keine Promillezahl im Gesetz:", 110, w316_y + 166, "zahl", "Bold", 32),
    z("Grenzwerte der Rechtsprechung sind Beweisregeln", 110, w316_y + 214, beim("zahl", "Grenzwerte"), size=32),
    zit("BGH, Urt. v. 9.4.2015 – 4 StR 401/14 (BGHSt 60, 227), Rn. 7", 110, w316_y + 264, beim("zahl", "Beweisregeln")),
    *requisit([("p316", ("tabler", "book", 100, WEISS), "§ 316 Abs. 1 StGB", GELB),
               (beim("p316", "alkoholischer"), ("tabler", "glass", 90, WEISS), "alkoholische Getränke", WEISS),
               ("fuehr", ("tabler", "car", 150, BLAU), "Führen im Verkehr", WEISS),
               ("kern", ("tabler", "help-circle", 100, WEISS), "fahruntüchtig?", PINK),
               ("zahl", ("tabler", "gavel", 100, HOLZ), "Grenzwerte: Rechtsprechung", GELB)]),
    *stehend("HE", X1, [("p316", "ruhig"), ("kern", "denkt")]),
    *stehend("SI", X2, [("p316", "ruhig"), ("kern", "froh")]),
]))

# ===========================================================================================================================
# D 1. Absolute Fahruntüchtigkeit: 1,1 ‰ (Kraftfahrer), Radfahrer 1,6 ‰
# ===========================================================================================================================
PA = "1. Absolute Fahruntüchtigkeit"
folie([("abs", f"{P316} › {PA}"), ("abs11", f"{P316} › {PA} › ab 1,1 ‰"), ("unwid", f"{P316} › {PA} › unwiderleglich"),
       ("sieg_abs", f"{P316} › {PA} › Siegfried: 1,2 ‰"), ("rad", f"{P316} › {PA} › Radfahrer: 1,6 ‰")], rechts_frei([
    *tafel("abs", "1. Absolute Fahruntüchtigkeit"),
    z("ab 1,1 ‰ BAK: jeder Kraftfahrer fahruntüchtig", 110, 180, "abs11", "Bold", 34),
    zit("BGHSt 37, 89 (Beschl. v. 28.6.1990 – 4 StR 297/90)", 110, 230, "bgh"),
    z("Grundwert 1,0 ‰ + Sicherheitszuschlag 0,1 ‰", 110, 280, "zuschl", size=32),
    zit("BGH, Beschl. v. 20.7.1999 – 4 StR 106/99 (BGHSt 45, 140), Rn. 12, 15 f.", 110, 328, beim("zuschl", "Sicherheitszuschlag")),
    *okz("unwiderleglich: kein Gegenbeweis,", 390, "unwid", "Bold", 34, x=160),
    z("auch nicht durch schnurgerades Fahren", 160, 440, beim("unwid", "schnurgerades"), size=32),
    zit("BGH, Beschl. v. 13.4.2023 – 4 StR 439/22, Rn. 4, 6", 160, 488, beim("unwid", "schnurgerades")),
    blk(110, 540, 1040, 80, GELB, "sieg_abs", [("Siegfried, 1,2 ‰: absolut fahruntüchtig", "ExtraBold", 36, INK)]),
    linienzug([(130, 655), (1130, 655)], "rad", breite=3),
    z("Radfahrer: höherer Grenzwert", 110, 680, "rad", "Bold", 34),
    z("OLG: überwiegend 1,6 ‰", 110, 730, "rad16", size=32),
    zit("OLG Karlsruhe, Beschl. v. 14.7.2020 – 2 Rv 35 Ss 175/20", 110, 778, "rad16"),
    zit("BGH, Beschl. v. 21.6.2017 – 4 StR 386/16, Rn. 2: kein Anlass zur Prüfung", 110, 816, "radbgh"),
    *skala("abs", {"11": "abs11", "SI": "sieg_abs", "16": "rad16"}),
    ficon("tabler", "bike", 1560, sky(1.6) + 36 + 70, 90, "rad", fuell=GELB),
    *stehend("SI", SFX_, [("abs", "ruhig"), ("unwid", "froh"), ("sieg_abs", "sorge"), ("rad", "ruhig")], SFB, SFR),
], x0=1260))

# ===========================================================================================================================
# E 2. Relative Fahruntüchtigkeit (etwa ab 0,3 ‰, nur mit alkoholbedingten Ausfallerscheinungen)
# ===========================================================================================================================
PR = "2. Relative Fahruntüchtigkeit"
folie([("rel", f"{P316} › {PR}"), ("aus", f"{P316} › {PR} › Ausfallerscheinungen"),
       ("hein_rel", f"{P316} › {PR} › Heinrich: 0,8 ‰"), ("hein_neg", f"{P316} › {PR} › Heinrich (−)")], rechts_frei([
    *tafel("rel", "2. Relative Fahruntüchtigkeit"),
    z("unter 1,1 ‰, etwa ab 0,3 ‰ möglich", 110, 180, "rel03", "Bold", 34),
    zit("OLG Hamm, Urt. v. 25.8.2010 – I-20 U 74/10, Rn. 28", 110, 230, beim("rel03", "null")),
    *okz("plus alkoholbedingte Ausfallerscheinungen:", 290, "aus", "Bold", 34, x=160),
    z("Schlangenlinien, typischer Fahrfehler", 160, 340, beim("aus", "Schlangenlinien"), size=32),
    *neinz("Fehler, der auch nüchtern passiert wäre: genügt nicht", 410, "kaus", "Bold", 32, x=160),
    zit("BGH, Beschl. v. 2.3.2021 – 4 StR 366/20, Rn. 9; 4 StR 526/24, Rn. 5, 7", 160, 460, beim("kaus", "genügt")),
    blk(110, 520, 1040, 80, BLAU, "hein_rel", [("Heinrich, 0,8 ‰: schnurgerade, keine Ausfälle", "ExtraBold", 34, INK)]),
    *neinz("relative Fahruntüchtigkeit nicht belegt: § 316 (−)", 650, "hein_neg", "Bold", 34, x=160),
    *skala("rel", {"11": "rel", "16": "rel", "03": "rel03", "HE": "hein_rel"}),
    *stehend("HE", SFX_, [("rel", "ruhig"), ("aus", "denkt"), ("hein_rel", "ruhig"), ("hein_neg", "staunt")], SFB, SFR),
], x0=1260))

# ===========================================================================================================================
# F 3. Wortlautkarte § 24a Abs. 1 StVG (0,5 ‰), § 24a Abs. 1a, § 24c StVG
# ===========================================================================================================================
PO_ = "3. Ordnungswidrigkeit, § 24a StVG"
W24 = ["„Ordnungswidrig handelt, wer vorsätzlich oder fahrlässig",
       "im Straßenverkehr ein Kraftfahrzeug führt, obwohl er",
       "0,25 mg/l oder mehr Alkohol in der Atemluft oder 0,5 Promille",
       "oder mehr Alkohol im Blut oder eine Alkoholmenge im Körper",
       "hat, die zu einer solchen Atem- oder Blutalkoholkonzentration",
       "führt.“"]
w24, w24_y = wortlaut(80, 230, 1100, W24, "§ 24a Abs. 1 StVG", "p24a", marken=[
    (0, "Ordnungswidrig handelt", beim("p24a", "Ordnungswidrig")), (1, "ein Kraftfahrzeug führt", beim("p24a", "Kraftfahrzeug")),
    (2, "0,25 mg/l oder mehr Alkohol in der Atemluft", "atem"), (2, "0,5 Promille", "p24b")], size=30)
folie([("owi", f"{PO_}"), ("p24a", f"{PO_} › Wortlaut Abs. 1"), ("ohne", f"{PO_} › ohne Ausfallerscheinungen"),
       ("hein_owi", f"{PO_} › Heinrich: 0,8 ‰ (+)"), ("thc", "§ 24a Abs. 1a, § 24c StVG")], rechts_frei([
    *tafel("owi", "3. Ordnungswidrigkeit: § 24a StVG"),
    z("Folgenlos für Heinrich? Nein:", 110, 172, "owi", "Bold", 34),
    *w24,
    *okz("ohne Ausfallerscheinungen", w24_y + 22, "ohne", "Bold", 32, x=160),
    z("Geldbuße, in der Regel Fahrverbot (§§ 24a Abs. 3, 25 Abs. 1 S. 2 StVG)", 160, w24_y + 70, "fv", size=28),
    blk(110, w24_y + 120, 1040, 76, GRUEN, "hein_owi", [("Heinrich, 0,8 ‰: ordnungswidrig", "ExtraBold", 34, INK)]),
    z("Cannabis: eigener THC-Grenzwert, § 24a Abs. 1a StVG", 110, w24_y + 220, "thc", size=30),
    z("Probezeit oder unter 21: kein Kfz unter Alkoholwirkung, § 24c", 110, w24_y + 266, "anf", size=30),
    *skala("owi", {"11": "owi", "16": "owi", "03": "owi", "HE": "owi", "05": "p24b"}),
    *stehend("HE", SFX_, [("owi", "ruhig"), ("ohne", "sorge"), ("hein_owi", "still")], SFB, SFR),
], x0=1260))

# ===========================================================================================================================
# G 4. Vorsatz oder Fahrlässigkeit (Siegfried)
# ===========================================================================================================================
PV = "4. Vorsatz oder Fahrlässigkeit"
folie([("vors", f"{P316} › {PV}"), ("grenz", f"{P316} › {PV} › Grenzwert kein Vorsatzgegenstand"),
       ("fahrl", f"{P316} › {PV} › Siegfried: fahrlässig, Abs. 2")], rechts_frei([
    *tafel("vors", "4. Vorsatz oder Fahrlässigkeit?"),
    z("Vorsatz: Fahruntüchtigkeit kennen oder mit ihr", 110, 190, "vors2", "Bold", 34),
    z("rechnen und sich damit abfinden", 110, 238, beim("vors2", "rechnet"), "Bold", 34),
    zit("BGH, Urt. v. 9.4.2015 – 4 StR 401/14 (BGHSt 60, 227), Rn. 7", 110, 290, beim("vors2", "abfindet")),
    *okz("den Grenzwert selbst muss er nicht kennen", 350, "grenz", "Bold", 32, x=160),
    blk(110, 430, 1040, 120, LILA, "fahrl", [("Siegfried hält sich für fahrtüchtig,", "ExtraBold", 34, INK),
                                            ("hätte es aber erkennen können", "ExtraBold", 34, INK)]),
    *okz("fahrlässig: § 316 Abs. 2 StGB", 590, beim("fahrl", "fahrlässig"), "Bold", 34, x=160),
    *skala("vors", {"11": "vors", "16": "vors", "03": "vors", "05": "vors", "SI": "vors"}),
    *stehend("SI", SFX_, [("vors", "ruhig"), ("fahrl", "sorge")], SFB, SFR),
], x0=1260))

# ===========================================================================================================================
# H 5. Abgrenzung § 315c Abs. 1 Nr. 1 a StGB
# ===========================================================================================================================
PG = "5. Abgrenzung: § 315c StGB"
folie([("p315c", f"{PG}"), ("beinahe", f"{PG} › konkrete Gefahr: Beinahe-Unfall"), ("keine", f"{PG} › hier (−)"),
       ("subs", f"{PG} › § 316 bleibt anwendbar")], rechts_frei([
    *tafel("p315c", "5. Abgrenzung: § 315c StGB"),
    z("§ 315c Abs. 1 Nr. 1 a StGB verlangt zusätzlich:", 110, 180, "p315c", "Bold", 34),
    z("konkrete Gefahr für Leib oder Leben eines anderen", 160, 235, beim("p315c", "konkrete"), size=32),
    z("oder für fremde Sachen von bedeutendem Wert", 160, 280, beim("p315c", "fremde"), size=32),
    z("also: ein Beinahe-Unfall", 160, 345, "beinahe", "Bold", 34),
    zit("BGH, Beschl. v. 13.3.2025 – 4 StR 391/24, Rn. 4", 160, 395, "beinahe"),
    *neinz("hier niemand gefährdet: § 315c (−)", 465, "keine", "Bold", 34, x=160),
    z("§ 316 bleibt anwendbar; bei konkreter Gefahr", 110, 545, "subs", size=32),
    z("träte er zurück (§ 316 Abs. 1 a. E.)", 110, 592, beim("subs", "träte"), size=32),
    *requisit([("p315c", ("tabler", "alert-triangle", 100, GELB), "konkrete Gefahr?", WEISS),
               ("beinahe", ("tabler", "alert-triangle", 100, ROT), "Beinahe-Unfall", HELLROT),
               ("keine", ("tabler", "shield-check", 100, GRUEN), "niemand gefährdet", GRUEN),
               ("subs", ("tabler", "book", 100, WEISS), "§ 316 bleibt", GELB)]),
    *stehend("HE", X1, [("p315c", "ruhig")]),
    *stehend("SI", X2, [("p315c", "ruhig"), ("keine", "froh")]),
]))

# ===========================================================================================================================
# I Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Siegfried: § 316 Abs. 1, 2 StGB"), ("owig", "Ergebnis · § 21 Abs. 1 OWiG"),
       ("fe", "Ergebnis · § 69 Abs. 2 Nr. 2 StGB"), ("erg2", "Ergebnis · Heinrich: § 24a Abs. 1 StVG")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Siegfried ist strafbar wegen", 110, 185, "erg", "Bold", 36),
    blk(110, 250, 1040, 80, GELB, beim("erg", "fahrlässiger"), [("fahrlässiger Trunkenheit im Verkehr, § 316 StGB", "ExtraBold", 34, INK)]),
    z("§ 24a StVG tritt zurück: § 21 Abs. 1 OWiG", 110, 365, "owig", "Bold", 32),
    z("Fahrerlaubnis in der Regel entzogen: § 69 Abs. 2 Nr. 2 StGB", 110, 425, "fe", "Bold", 32),
    linienzug([(130, 500), (1130, 500)], "erg2", breite=3),
    z("Heinrich:", 110, 530, "erg2", "Bold", 36),
    blk(110, 590, 1040, 80, GRUEN, beim("erg2", "ordnungswidrig"), [("nur ordnungswidrig, § 24a Abs. 1 StVG", "ExtraBold", 34, INK)]),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", GRUEN), ("fe", ("tabler", "id", 100, WEISS), "Fahrerlaubnis", WEISS)]),
    *stehend("HE", X1, [("erg", "ruhig"), ("erg2", "still")]),
    *stehend("SI", X2, [("erg", "muede")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Grenzwert = Beweisregel"), ("tipp2", "Klausurtipp · unter 1,1 ‰: Ausfallerscheinungen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Grenzwert: kein Tatbestandsmerkmal,", 200, 200, beim("tipp", "Grenzwert"), "Bold", 36),
    z("sondern eine Beweisregel", 200, 250, beim("tipp", "sondern"), size=34),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    z("Unter 1,1 ‰ immer prüfen:", 200, 360, "tipp2", "Bold", 36),
    z("Ausfallerscheinungen festgestellt?", 200, 420, beim("tipp2", "Ausfallerscheinungen"), size=34),
    z("Beruhen sie gerade auf dem Alkohol?", 200, 475, beim("tipp2", "gerade"), size=34),
    zit("vgl. BGH, Beschl. v. 26.2.2025 – 4 StR 526/24, Rn. 7", 200, 535, beim("tipp2", "gerade")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Tatbestand", True),
          (beim("k1", "Objektiv"), 1, "1. Objektiv: Führen eines Fahrzeugs im Verkehr", False),
          ("k1b", 1, "Fahruntüchtigkeit infolge Alkohols:", True),
          ("k1c", 2, "absolut: ab 1,1 ‰, bei Radfahrern 1,6 ‰", False),
          ("k1d", 2, "relativ: mit alkoholbedingten Ausfallerscheinungen", False),
          ("k1e", 1, "2. Subjektiv: Vorsatz, sonst Fahrlässigkeit (§ 316 Abs. 2 StGB)", False),
          ("k2", 0, "II. Rechtswidrigkeit  ·  III. Schuld", True),
          ("k3", 0, "Konkurrenzen: Vorrang von § 315c StGB", True),
          ("k4", 0, "Ohne Straftat: ab 0,5 ‰ § 24a StVG", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Trunkenheit im Verkehr"), 110, 90, "sch", 46),
           z("§ 316 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "k1b":
        els_sch.append(karte(180, y - 16, 1640, 212, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 35, rechts=1800))
    y += {0: 90, 1: 76, 2: 70}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Tatbestand"), ("k1b", "Prüfschema › I. Fahruntüchtigkeit"),
       ("k1e", "Prüfschema › I. 2. Vorsatz/Fahrlässigkeit"), ("k2", "Prüfschema › II. und III."),
       ("k3", "Prüfschema › Konkurrenzen"), ("k4", "Prüfschema › § 24a StVG")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ab 1,1 ‰ hilft auch", 0)], [("schnurgerades Fahren nicht", "a"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "schnurgerades")}),
    *markertext([[("Darunter braucht die Straftat", 0)], [("Ausfallerscheinungen", "b"), (",", 0)],
                 [("die Ordnungswidrigkeit nur 0,5 ‰", 0), (".", 0)]], 750, 540, 44, "m2", {"b": beim("m2", "Ausfallerscheinungen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
