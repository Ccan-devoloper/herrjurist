"""Folge 229 · Dein Foto in fremder Werbung: Die Eingriffskondiktion (§ 812 BGB) – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen (Nachbildung des Klassikers BGHZ 20, 345 – Paul Dahlke): An der Bushaltestelle hängt ein Werbeplakat der
fiktiven Limonadenfirma „Brauselust“ (keine echte Marke, kein echtes Logo) mit dem Bild des fiktiven Kai Möbius; eine
Kollegin erkennt ihn. Rückblick: Ein Fotograf der Firma fotografiert Kai im Stadtpark, ohne dass er es bemerkt. Im Büro
verlangt Kai von Marketingleiter Wendorf die übliche Lizenz von 3.000 €; Wendorf wendet ein, Kai hätte nie geworben. Die
reale Person des Klassikers wird nicht gezeigt, ihr Name steht nur als Fallbezeichnung auf der Fundstellen-Pille.
Danach: § 812 Abs. 1 Satz 1 BGB (Wortlautkarte), Vorrang der Leistungskondiktion (Verweis 073), 1. etwas erlangt (Nutzung),
2. auf Kosten (Zuweisungsgehalt; Wortlautkarte § 22 Satz 1 KUG), 3. ohne rechtlichen Grund, Rechtsfolge (Wortlautkarte
§ 818 Abs. 2 BGB, fiktive Lizenz), Einwand, Entreicherung, parallele Ansprüche, Ergebnis, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/tisch als eigene
Kopie aus Folge 226 (gemeinsame Dateien unverändert); neu: plakat(), haltestelle(), baum(), buero(), kopfbild().
Handlungsgeräusch: Kameraauslöser im Stadtpark (A2); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB, KUG), Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_229/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_229/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205) -------------------------------------
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


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KA": "Kai Möbius", "WE": "Marketingleiter Wendorf", "KO": "Kollegin", "FO": "Fotograf"}
NFARBE = {"KA": GRUEN, "WE": BLAU, "KO": PINK, "FO": GELB}


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def tuer(x, cue, farbe=HOLZ, w=190, h=360):
    """Wohnungstür aus Grundformen (Rahmen, Blatt, Klinke) auf dem Boden."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
    dr.rounded_rectangle((o + 22 * s, o + 26 * s, o + (w - 22) * s, o + 150 * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + 22 * s, o + 180 * s, o + (w - 22) * s, o + (h - 26) * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + (w - 52) * s, o + 168 * s, o + (w - 18) * s, o + 180 * s), 4 * s, fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="tuer"))


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)



def tisch(x, w, cue, h=200, farbe=HOLZ):
    """Schreibtisch/Theke aus Grundformen auf dem Boden."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 34 * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
    dr.rectangle((o + 24 * s, o + 34 * s, o + 54 * s, o + h * s), fill=farbe, outline=INK, width=5 * s)
    dr.rectangle((o + (w - 54) * s, o + 34 * s, o + (w - 24) * s, o + h * s), fill=farbe, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="tisch"))



def baum(x, cue, h=300):
    """Parkbaum aus Grundformen (Stamm, runde Krone)."""
    return [hart(feld(x - 18, BODEN - h, 36, h - 6, cue, fill=HOLZ, rand=4, rund=6, name="stamm")),
            hart(feld(x - 135, BODEN - h - 230, 270, 260, cue, fill=GRUEN, rand=5, rund=125, name="krone"))]


_KOPF = {}


def kopfbild(name="KA_froh", breite=150):
    """Brustbild von Kai für das Plakat: Ausschnitt der Open-Peeps-Figur, nicht umgezeichnet."""
    if (name, breite) not in _KOPF:
        im = Image.open(FIG + "op_229/" + name + ".png").convert("RGBA")
        im = im.crop(im.getbbox())
        im = im.crop((0, 0, im.width, int(im.height * 0.42)))
        _KOPF[(name, breite)] = im.resize((breite, int(im.height * breite / im.width)), Image.LANCZOS)
    return _KOPF[(name, breite)]


def plakat(x, y, w, h, cue, bild_cue=None, bis=None, anim="cut", mini=False):
    """Werbeplakat der fiktiven Limonadenfirma „Brauselust“ (keine echte Marke, kein Logo): Rahmen, Name, Kai, Flasche,
    Slogan. bild_cue: ab wann Kai und die Flasche auf dem Plakat zu sehen sind."""
    els = [El(_feld(w, h, fill=WEISS, rand=6 if not mini else 4, rund=8), x, y, cue, anim, 0.0, bis, name="plakatrahmen"),
           El(_feld(w - 28, h - 28, fill=GELB, rand=3, rund=6), x + 14, y + 14, cue, anim, 0.0, bis, name="plakatgrund")]
    gr = 54 if not mini else 22
    while F("ExtraBold", gr).getlength("BRAUSELUST") > w - 70:
        gr -= 2
    if not mini:
        els.append(bis_(z("BRAUSELUST", x + 34, y + 34, cue, "ExtraBold", gr, farbe=INK, rechts=x + w - 10), bis))
    bc = bild_cue or cue
    k = kopfbild("KA_froh_r", int(w * (0.50 if not mini else 0.62)))
    ky = y + (int(h * 0.19) if not mini else 20)
    kx = x + int(w * 0.18)
    els.append(El(k, kx, ky, bc, "pop" if bild_cue else anim, 0.0, bis, name="bild:plakatkai"))
    # die Flasche steht auf Kais offener Hand (Hand bei ≈ 37 % der Figurenhöhe, rechter Rand)
    els.append(ficon("tabler", "bottle", kx + int(k.width * 0.90), ky + int(k.height * 0.37 / 0.42) + 4,
                     int(k.width * 0.22), bc, fuell=HELLGRUEN, bis=bis, anim="pop" if bild_cue else anim))
    if not mini:
        sg = max(28, gr - 22)
        if F("Bold", sg).getlength("so schmeckt der Sommer") <= w - 60:
            els.append(bis_(z("so schmeckt der Sommer", x + 34, y + h - 84, cue, "Bold", sg, rechts=x + w - 10), bis))
        else:
            els += [bis_(z("so schmeckt", x + 34, y + h - 120, cue, "Bold", sg, rechts=x + w - 10), bis),
                    bis_(z("der Sommer", x + 34, y + h - 82, cue, "Bold", sg, rechts=x + w - 10), bis)]
    return els


# ===========================================================================================================================
# A1 Fall: An der Bushaltestelle hängt das neue Brauselust-Plakat – Kollegin erkennt Kai
# ===========================================================================================================================
KOX, KAX = 1290, 1650
HX0, HW = 90, 880                           # Wartehäuschen


def haltestelle(cue, plakat_cue, bild_cue):
    els = [boden(cue),
           hart(feld(HX0, 110, HW, 46, cue, fill=HELLGRAU, rand=5, rund=10, name="dach")),
           hart(feld(HX0 + 14, 156, 26, BODEN - 162, cue, fill=HELLGRAU, rand=4, rund=4, name="pfosten1")),
           hart(feld(HX0 + HW - 40, 156, 26, BODEN - 162, cue, fill=HELLGRAU, rand=4, rund=4, name="pfosten2")),
           hart(feld(HX0 + 60, 680, HW - 120, 26, cue, fill=HOLZ, rand=4, rund=6, name="bank")),
           hart(feld(1060, 450, 16, BODEN - 456, cue, fill=INK, rand=2, rund=4, name="mast")),
           hart(feld(1023, 365, 90, 90, cue, fill=GELB, rand=5, rund=45, name="schild")),
           hart(z("H", 1049, 372, cue, "ExtraBold", 54, farbe=(40, 150, 85, 255), rechts=1120))]
    els += plakat(HX0 + 130, 180, 500, 470, plakat_cue, bild_cue=bild_cue, anim="pop")
    return els


folie([(NULL, "Fall · An der Bushaltestelle"), ("plakat", "Fall · Ein neues Werbeplakat: Brauselust"),
       ("gesicht", "Fall · Auf dem Plakat: Kai"), ("k1", "Fall · Gefragt hat ihn niemand")], [
    *haltestelle(NULL, "plakat", "gesicht"),
    hart(pl("An der Bushaltestelle", 70, 30, NULL, fill=GELB, size=32)),
    *fig("KO", KOX, BODEN, FH, [(NULL, "ruhig"), ("gesicht", "staunt")], bis="k1", erst="cut"),
    *redet("KO_redet", KOX, BODEN, FH, "k1", "ka1"),
    *fig("KO", KOX, BODEN, FH, [("ka1", "froh")], erst="cut"),
    hart(ns(NAME["KO"], KOX, BODEN, NULL, PINK)),
    *fig("KA", KAX, BODEN, FH, [(NULL, "ruhig"), ("gesicht", "staunt")], bis="ka1", erst="cut"),
    *redet("KA_redet", KAX, BODEN, FH, "ka1", "park"),
    hart(ns(NAME["KA"], KAX, BODEN, NULL, GRUEN)),
    blase("sprech", 600, 200, "k1", 1290, 250, inhalt=["Kai, guck mal! Das bist", "ja du, auf dem Plakat!"], textsize=32,
          figur=("KO_redet", KOX, BODEN, FH), bis="ka1"),
    blase("sprech", 560, 200, "ka1", 1500, 250, inhalt=["Das bin ja ich.", "Gefragt hat mich niemand!"], textsize=32,
          figur=("KA_redet", KAX, BODEN, FH)),
])

# ===========================================================================================================================
# A2 Rückblick: Im Stadtpark fotografiert ein Fotograf der Firma Kai, ohne dass er es bemerkt
# ===========================================================================================================================
FOX, KAX2 = 640, 1430
folie([("park", "Fall · Im Sommer im Stadtpark"), ("knips", "Fall · Ein Fotograf der Firma"),
       ("plakate", "Fall · 120 Plakate in der ganzen Stadt")], [
    boden("park"),
    *baum(230, "park"), *baum(1060, "park", h=290), *baum(1760, "park", h=280),
    hart(pl("Im Sommer im Stadtpark", 70, 30, "park", fill=GELB, size=32)),
    *fig("KA", KAX2, BODEN, FH, [("park", "trinkt_r"), ("plakate", "ruhig_r")], erst="cut"),
    ficon("tabler", "bottle", KAX2 + 80, BODEN - 268, 52, "park", fuell=HELLGRUEN, anim="cut", bis="plakate"),   # auf der offenen Hand
    hart(ns(NAME["KA"], KAX2, BODEN, "park", GRUEN)),
    *fig("FO", FOX, BODEN, FH, [("knips", "ruhig_r")], erst="pop"),
    ns(NAME["FO"], FOX, BODEN, "knips", GELB, d=0.1),
    ficon("tabler", "camera", FOX + 105, 560, 84, "knips", fuell=WEISS),
    szene(ficon("tabler", "sparkles", FOX + 190, 520, 70, beim("knips", "fotografiert"), fuell=GELB), "229kamera*", 0.35, -0.03),
    pl("ohne dass er es bemerkte", 70, 100, beim("knips", "ohne"), fill=WEISS, size=30),
    *[El(_feld(150, 190, fill=WEISS, rand=4, rund=6), 980 + i * 170, 40, "plakate", "pop", 0.04 * i, None, name="miniplakat")
      for i in range(5)],
    *[El(kopfbild("KA_froh_r", 100), 1005 + i * 170, 60, "plakate", "pop", 0.04 * i, None, name="bild:minikai") for i in range(5)],
    pl("120 Plakate in der ganzen Stadt", 1405, 250, "plakate", fill=GELB, size=30, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: Im Büro der Firma (Marketingleiter Wendorf, sachlich); Frage und Klassiker als Pillen
# ===========================================================================================================================
KAX3, WEX = 760, 1400


def buero(cue):
    return [boden(cue), *plakat(80, 170, 330, 400, cue, mini=False), tisch(1530, 350, cue, h=210),
            ficon("tabler", "bottle", 1705, BODEN - 214, 70, cue, fuell=HELLGRUEN, anim="cut")]


folie([("buero", "Fall · Im Büro der Firma Brauselust"), ("ka2", "Fall · Kai verlangt die übliche Lizenz"),
       ("w1", "Fall · Der Einwand des Marketingleiters"), ("frage", "Die Frage · Muss die Firma zahlen?"),
       ("bgh", "Die Frage · BGHZ 20, 345 (Paul Dahlke)")], [
    *buero("buero"),
    hart(pl("Im Büro der Firma Brauselust", 470, 30, "buero", fill=GELB, size=32, bis="frage")),
    peep_voll("KA_ernst_r", KAX3, BODEN, FH, "buero", anim="pop", bis="ka2"),
    *redet("KA_redet_r", KAX3, BODEN, FH, "ka2", "w1"),
    *fig("KA", KAX3, BODEN, FH, [("w1", "denkt_r"), ("frage", "ernst_r"), ("klassiker", "ruhig_r")], erst="cut"),
    ns(NAME["KA"], KAX3, BODEN, "buero", GRUEN),
    *fig("WE", WEX, BODEN, FH, [("buero", "ruhig"), ("ka2", "ernst")], bis="w1", erst="cut"),
    *redet("WE_redet", WEX, BODEN, FH, "w1", "frage"),
    *fig("WE", WEX, BODEN, FH, [("frage", "denkt"), ("klassiker", "ruhig")], erst="cut"),
    hart(ns(NAME["WE"], WEX, BODEN, "buero", BLAU)),
    blase("sprech", 620, 230, "ka2", 900, 250, inhalt=["Sie werben mit meinem Gesicht.", "Dafür will ich die übliche",
                                                      "Lizenz: 3.000 €."], textsize=32,
          figur=("KA_redet_r", KAX3, BODEN, FH), bis="w1"),
    blase("sprech", 640, 230, "w1", 1260, 250, inhalt=["Sie hätten doch nie für", "Limonade geworben. Also haben",
                                                      "Sie auch nichts verloren."], textsize=32,
          figur=("WE_redet", WEX, BODEN, FH), bis="frage"),
    pl("Muss die Firma zahlen, und wie viel?", 470, 30, "frage", fill=PINK, size=34),
    pl("übliche Lizenz für ein solches Werbefoto: 3.000 €", 470, 104, "lizenz", fill=WEISS, size=30),
    pl("BGH, Urt. v. 8.5.1956 · I ZR 62/54 · BGHZ 20, 345 (Paul Dahlke)", 470, 170, beim("bgh", "Bundesgerichtshof"),
       fill=GELB, size=28),
    pl("Klassiker: Werbung mit dem Bild eines Schauspielers, ohne Einwilligung", 470, 232, beim("bgh", "Werbung"),
       fill=WEISS, size=28),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_229(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=37, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_229("sv", [
    "Ein Fotograf der Limonadenfirma „Brauselust“ fotografiert Kai Möbius im Stadtpark, ohne dass Kai es bemerkt. Ohne "
    "seine Einwilligung wirbt die Firma mit dem Bild: 120 Plakate zeigen Kai lachend mit einer Flasche Brauselust.",
    "Marketingleiter Wendorf wusste, dass für die Werbung eine Einwilligung nötig war und Kai nie gefragt wurde. Für ein "
    "solches Werbefoto zahlt man üblicherweise 3.000 €.",
    "Kai verlangt 3.000 €. Wendorf meint, Kai hätte ohnehin nie für Limonade geworben und deshalb nichts verloren.",
], "Muss die Firma zahlen, und wie viel?")


# ===========================================================================================================================
# Tafel-Helfer
# ===========================================================================================================================
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


# ===========================================================================================================================
# C1 I. Anspruchsgrundlage: § 812 Abs. 1 Satz 1 BGB (Wortlautkarte, vollständig vorgelesen)
# ===========================================================================================================================
PI = "I. Anspruchsgrundlage"
w812, w812_y = wortlaut(80, 250, 1100, "„(1) Wer durch die Leistung eines anderen oder in sonstiger Weise auf dessen Kosten "
                                       "etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe verpflichtet. …“",
                        "§ 812 Abs. 1 Satz 1 BGB", "w812",
                        marken=[("in sonstiger Weise", beim("w812", "sonstiger")), ("dessen Kosten", beim("w812", "Kosten")),
                                ("ohne rechtlichen Grund", beim("w812", "rechtlichen")), ("erlangt", beim("w812", "erlangt"))])
folie([("norm", f"{PI} · § 812 Abs. 1 Satz 1 BGB"), ("w812", f"{PI} › Wortlaut"),
       ("alt2", f"{PI} › 2. Alternative: Eingriffskondiktion")], [
    *tafel("norm", "I. Anspruchsgrundlage"),
    z("§ 812 Abs. 1 Satz 1 BGB", 110, 180, "norm", "ExtraBold", 40),
    *w812,
    blk(110, w812_y + 30, 1040, 130, GELB, "alt2", [("2. Alternative: Bereicherung in sonstiger Weise", "ExtraBold", 33, INK),
                                                  ("= Eingriffskondiktion", "ExtraBold", 33, INK)]),
    *requisit([("norm", ("tabler", "scale", 120, WEISS), "§ 812 BGB", GELB),
               ("alt2", ("tabler", "photo", 120, GELB), "Eingriff", HELLROT)]),
    *stehend("KA", FX, [("norm", "ruhig"), ("w812", "denkt")]),
])

# ===========================================================================================================================
# C2 Vorrang der Leistungskondiktion (I ZR 187/10 Rn. 46; Verweis Folge 073)
# ===========================================================================================================================
folie([("vorr", f"{PI} › Vorrang: Hat Kai geleistet?"), ("nein", f"{PI} › keine Leistung"),
       ("verweis", f"{PI} › Vorrang der Leistungskondiktion: Folge Überblick")], [
    *tafel("vorr", "Vorrang der Leistungskondiktion"),
    z("Vorher fragen: Hat Kai etwas geleistet?", 110, 190, "vorr", "Bold", 36),
    *neinz("Nein: Kai hat der Firma nichts zugewendet", 270, "nein", "Bold", 34, kreuz=beim("nein", "Nein")),
    *okz("die Firma hat sich sein Bild genommen", 340, beim("nein", "Bild"), "Bold", 34),
    zit("BGH, Urt. v. 18.1.2012 – I ZR 187/10, Rn. 46 (Vorrang der Leistungskondiktion)", 185, 392, beim("nein", "Bild")),
    blk(110, 480, 1040, 130, BLAUHELL, "verweis", [("Warum die Leistungskondiktion Vorrang hat:", "ExtraBold", 32, INK),
                                                 ("unsere Folge „Bereicherungsrecht im Überblick“", "ExtraBold", 32, INK)]),
    *requisit([("vorr", ("tabler", "gift-off", 120, HELLROT), "keine Leistung?", WEISS),
               ("verweis", ("tabler", "books", 120, BLAUHELL), "Überblick", BLAUHELL)], px=1560, pu=330, py=90),
    *paar("WE", [("vorr", "ruhig"), ("nein", "denkt")], "KA", [("vorr", "ruhig"), ("nein", "ernst")]),
])

# ===========================================================================================================================
# D 1. Etwas erlangt: die Nutzung des Bildnisses (VI ZR 123/11 Rn. 24; I ZR 120/19 Rn. 58)
# ===========================================================================================================================
PII = "II. Voraussetzungen"
folie([("erl", f"{PII} › 1. etwas erlangt"), ("nutz", f"{PII} › 1. die Nutzung des Bildnisses"),
       ("bgh1", f"{PII} › 1. BGH: Nutzung ist Bereicherungsgegenstand")], [
    *tafel("erl", "1. Etwas erlangt"),
    z("Was hat die Firma erlangt?", 110, 190, "erl", "Bold", 36),
    *neinz("nicht das Foto als Gegenstand", 280, "nutz", "Bold", 34, kreuz=beim("nutz", "Nicht")),
    *okz("sondern: die Nutzung von Kais Bildnis", 350, beim("nutz", "sondern"), "Bold", 34),
    z("für die eigene Werbung", 185, 398, beim("nutz", "Werbung"), "Bold", 34),
    blk(110, 490, 1040, 130, HELLGRUEN, "bgh1", [("BGH: Bereicherungsgegenstand ist", "ExtraBold", 34, INK),
                                               ("die Nutzung des Bildnisses", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 20.3.2012 – VI ZR 123/11, Rn. 24", 110, 638, "bgh1"),
    zit("BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 58", 110, 676, "bgh1"),
    *requisit([("erl", ("tabler", "help-circle", 110, WEISS), "erlangt?", WEISS),
               ("nutz", ("tabler", "ad-2", 120, GELB), "Nutzung für Werbung", GELB)]),
    *stehend("KA", FX, [("erl", "ruhig"), ("nutz", "denkt"), ("bgh1", "ernst")]),
])

# ===========================================================================================================================
# E1 2. Auf Kosten: Lehre vom Zuweisungsgehalt (IX ZR 204/11 Rn. 15; I ZR 187/10 Rn. 40)
# ===========================================================================================================================
folie([("kosten", f"{PII} › 2. auf Kosten"), ("zuw", f"{PII} › 2. Lehre vom Zuweisungsgehalt")], [
    *tafel("kosten", "2. Auf Kosten von Kai"),
    z("Lehre vom Zuweisungsgehalt:", 110, 200, "zuw", "ExtraBold", 38),
    blk(110, 270, 1040, 180, GELB, "def", [("Verletzung einer Rechtsposition, die dem", "ExtraBold", 33, INK),
                                         ("Berechtigten zur ausschließlichen Verfügung", "ExtraBold", 33, INK),
                                         ("und Verwertung zugewiesen ist", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 16.5.2013 – IX ZR 204/11, Rn. 15", 110, 468, "def"),
    zit("BGH, Urt. v. 18.1.2012 – I ZR 187/10, BGHZ 192, 204, Rn. 40", 110, 506, "def"),
    *requisit([("kosten", ("tabler", "user-square", 120, WEISS), "auf wessen Kosten?", WEISS),
               ("def", ("tabler", "key", 120, GELB), "nur für Kai", GELB)]),
    *stehend("KA", FX, [("kosten", "ruhig"), ("def", "denkt")]),
])

# ===========================================================================================================================
# E2 Recht am eigenen Bild (Wortlautkarte § 22 Satz 1 KUG; I ZR 234/10 Rn. 15; I ZR 120/19 Rn. 26)
# ===========================================================================================================================
w22, w22_y = wortlaut(80, 250, 1100, "„Bildnisse dürfen nur mit Einwilligung des Abgebildeten verbreitet oder öffentlich "
                                     "zur Schau gestellt werden. …“", "§ 22 Satz 1 KUG", "w22",
                      marken=[("nur mit Einwilligung", beim("w22", "Einwilligung")), ("verbreitet", beim("w22", "verbreitet"))])
folie([("kug", f"{PII} › 2. Recht am eigenen Bild"), ("w22", f"{PII} › 2. § 22 Satz 1 KUG"),
       ("werb", f"{PII} › 2. Kai entscheidet über Werbung"), ("eing", f"{PII} › 2. Eingriff in den Zuweisungsgehalt")], [
    *tafel("kug", "Recht am eigenen Bild"),
    z("Welche Rechtsposition?", 110, 180, "kug", "Bold", 36),
    *w22,
    *okz("über Werbung mit seinem Bild entscheidet Kai", w22_y + 30, "werb", "Bold", 33),
    *okz("vermögensrechtlicher Bestandteil des", w22_y + 90, "verm", "Bold", 33),
    z("Persönlichkeitsrechts", 185, w22_y + 136, beim("verm", "Persönlichkeitsrechts"), "Bold", 33),
    zit("BGH, Urt. v. 31.5.2012 – I ZR 234/10, Rn. 15", 185, w22_y + 186, beim("verm", "Persönlichkeitsrechts")),
    blk(110, w22_y + 240, 1040, 110, HELLROT, "eing", [("unbefugte Werbung mit fremdem Bildnis:", "ExtraBold", 32, INK),
                                                     ("Eingriff in den Zuweisungsgehalt", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 26", 110, w22_y + 362, "eing"),
    *requisit([("kug", ("tabler", "user-square", 120, GELB), "Recht am eigenen Bild", GELB),
               ("werb", ("tabler", "ad-2", 120, WEISS), "Werbung?", WEISS),
               ("eing", ("tabler", "ban", 110, HELLROT), "Eingriff", HELLROT)], px=1560, pu=330, py=90),
    *paar("WE", [("kug", "ruhig"), ("eing", "sorge")], "KA", [("kug", "ruhig"), ("werb", "ernst")]),
])

# ===========================================================================================================================
# F 3. Ohne rechtlichen Grund (I ZR 120/19 Rn. 36, 38)
# ===========================================================================================================================
folie([("org", f"{PII} › 3. ohne rechtlichen Grund"), ("einw", f"{PII} › 3. keine Einwilligung"),
       ("p23", f"{PII} › 3. keine Ausnahme nach § 23 KUG"), ("tbm", f"{PII} › Voraussetzungen (+)")], [
    *tafel("org", "3. Ohne rechtlichen Grund"),
    *neinz("Einwilligung: nie erteilt", 200, "einw", "Bold", 35, kreuz=beim("einw", "nie")),
    zit("§ 22 Satz 1 KUG; BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 36", 185, 250, "einw"),
    *neinz("Ausnahme Zeitgeschichte, § 23 Abs. 1 Nr. 1 KUG:", 330, "p23", "Bold", 33, kreuz=beim("p23", "nicht")),
    z("nicht für den, der ein Bild allein für", 185, 378, beim("p23", "nicht"), "Bold", 33),
    z("seine Werbung verwertet", 185, 424, beim("p23", "Werbung"), "Bold", 33),
    zit("BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 38", 185, 474, beim("p23", "Werbung")),
    blk(110, 560, 1040, 220, HELLGRUEN, "tbm", [("1. etwas erlangt: (+)", "ExtraBold", 32, INK),
                                              ("2. in sonstiger Weise auf Kosten: (+)", "ExtraBold", 32, INK),
                                              ("3. ohne rechtlichen Grund: (+)", "ExtraBold", 32, INK)]),
    *requisit([("org", ("tabler", "file-certificate", 120, WEISS), "Rechtsgrund?", WEISS),
               ("einw", ("tabler", "signature", 120, HELLROT), "keine Einwilligung", HELLROT),
               ("tbm", ("tabler", "circle-check", 110, HELLGRUEN), "Voraussetzungen (+)", HELLGRUEN)]),
    *stehend("WE", FX, [("org", "ruhig"), ("einw", "ernst"), ("p23", "sorge")]),
])

# ===========================================================================================================================
# G1 Rechtsfolge: § 818 Abs. 2 BGB (Wortlautkarte), fiktive Lizenz (I ZR 120/19 Rn. 58 f.; I ZR 41/24 Rn. 126)
# ===========================================================================================================================
PIII = "III. Rechtsfolge"
w818, w818_y = wortlaut(80, 240, 1100, "„(2) Ist die Herausgabe wegen der Beschaffenheit des Erlangten nicht möglich oder "
                                       "ist der Empfänger aus einem anderen Grunde zur Herausgabe außerstande, so hat er den "
                                       "Wert zu ersetzen.“", "§ 818 Abs. 2 BGB", "w818",
                        marken=[("Beschaffenheit des Erlangten", beim("w818", "Beschaffenheit")), ("Wert zu ersetzen", beim("w818", "Wert"))])
folie([("rf", f"{PIII} · Herausgabe?"), ("w818", f"{PIII} › § 818 Abs. 2 BGB: Wertersatz"),
       ("lizw", f"{PIII} › Wert = übliche Lizenzgebühr"), ("hier", f"{PIII} › hier: 3.000 €")], [
    *tafel("rf", "III. Rechtsfolge: Wertersatz"),
    *neinz("Nutzung kann nicht herausgegeben werden", 175, "unm", "Bold", 34, kreuz=beim("unm", "nicht")),
    *w818,
    *okz("Wert = übliche Lizenzgebühr („fiktive Lizenz“):", w818_y + 30, "lizw", "Bold", 33),
    z("was vernünftige Vertragspartner vereinbart hätten", 185, w818_y + 76, beim("lizw", "vernünftige"), "Bold", 33),
    zit("I ZR 120/19, Rn. 58 f.; I ZR 41/24, Rn. 126 mit BGHZ 20, 345 (Paul Dahlke)", 185, w818_y + 126,
        beim("lizw", "vernünftige")),
    blk(110, w818_y + 190, 1040, 90, GELB, "hier", [("Hier: 3.000 €", "ExtraBold", 40, INK)]),
    *requisit([("rf", ("tabler", "package", 120, WEISS), "herausgeben?", WEISS),
               ("w818", ("tabler", "scale", 120, WEISS), "Wertersatz", GELB),
               ("hier", ("tabler", "coin-euro", 130, GELB), "3.000 €", GELB)]),
    *stehend("KA", FX, [("rf", "ruhig"), ("lizw", "denkt"), ("hier", "froh")]),
])

# ===========================================================================================================================
# G2 Einwand Wendorf (VI ZR 123/11 Rn. 24; I ZR 120/19 Rn. 58; I ZR 41/24 Rn. 124)
# ===========================================================================================================================
folie([("einwand", f"{PIII} › Einwand: „nie für Limonade geworben“"), ("egal", f"{PIII} › Einwand unerheblich"),
       ("fing", f"{PIII} › keine fingierte Zustimmung"), ("wert", f"{PIII} › Verletzer muss sich festhalten lassen")], [
    *tafel("einwand", "Der Einwand des Marketingleiters"),
    pl("„Sie hätten doch nie für Limonade geworben.“", 110, 175, "einwand", fill=BLAUHELL, size=32),
    *neinz("ob Kai geworben hätte: unerheblich", 270, "egal", "Bold", 35, kreuz=beim("egal", "unerheblich")),
    zit("BGH, Urt. v. 23.4.2026 – I ZR 41/24, Rn. 124", 185, 320, beim("egal", "unerheblich")),
    *okz("keine unterstellte Zustimmung, sondern Ausgleich", 390, "fing", "Bold", 33),
    z("für den Eingriff in Kais alleinige Befugnis", 185, 436, beim("fing", "Eingriff"), "Bold", 33),
    blk(110, 520, 1040, 120, GELB, "wert", [("Wer ein fremdes Bild für Werbung nutzt,", "ExtraBold", 32, INK),
                                          ("misst ihm einen wirtschaftlichen Wert bei.", "ExtraBold", 32, INK)]),
    blk(110, 652, 1040, 70, HELLGRUEN, beim("wert", "Daran"), [("Daran muss er sich festhalten lassen.", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 20.3.2012 – VI ZR 123/11, Rn. 24; BGH I ZR 120/19, Rn. 58", 110, 740, beim("wert", "Daran")),
    *requisit([("einwand", ("tabler", "message-circle-question", 110, BLAUHELL), "Einwand", BLAUHELL),
               ("egal", ("tabler", "x", 110, HELLROT), "unerheblich", HELLROT),
               ("wert", ("tabler", "coin-euro", 120, GELB), "Wert", GELB)], px=1560, pu=330, py=90),
    *paar("WE", [("einwand", "denkt"), ("egal", "sorge")], "KA", [("einwand", "ruhig"), ("egal", "froh")]),
])

# ===========================================================================================================================
# G3 Entreicherung? (§§ 818 Abs. 3, 819 Abs. 1, 818 Abs. 4 BGB; XII ZR 102/09 Rn. 55)
# ===========================================================================================================================
folie([("entr", f"{PIII} › Entreicherung, § 818 Abs. 3 BGB?"), ("kennt", f"{PIII} › verschärfte Haftung, § 819 Abs. 1 BGB")], [
    *tafel("entr", "Entreicherung?"),
    z("Entreicherung nach § 818 Abs. 3 BGB?", 110, 180, "entr", "Bold", 36),
    *neinz("Berufung darauf: nicht möglich", 240, beim("entr", "nicht"), "Bold", 35),
    *okz("die Firma wusste: keine Einwilligung", 300, "kennt", "Bold", 35),
    blk(110, 370, 1040, 130, GELB, beim("kennt", "verschärft"), [("Kenntnis: verschärfte Haftung", "ExtraBold", 34, INK),
                                                              ("§ 819 Abs. 1 i. V. m. § 818 Abs. 4 BGB", "ExtraBold", 34, INK)]),
    zit("§ 818 Abs. 4 BGB: Haftung nach den allgemeinen Vorschriften; BGH, Urt. v. 11.8.2010", 110, 518, beim("kennt", "verschärft")),
    zit("– XII ZR 102/09, Rn. 55 (kein Wegfall der Bereicherung mehr)", 110, 556, beim("kennt", "verschärft")),
    *requisit([("entr", ("tabler", "receipt-euro", 120, WEISS), "entreichert?", WEISS),
               ("kennt", ("tabler", "alert-triangle", 120, HELLROT), "Kenntnis", HELLROT)]),
    *stehend("WE", FX, [("entr", "denkt"), ("kennt", "sorge")]),
])

# ===========================================================================================================================
# H Parallele Ansprüche (I ZR 120/19 Rn. 26, 70; I ZR 234/10 Rn. 42; VI ZR 250/19 Rn. 8; I ZR 41/24 Rn. 126)
# ===========================================================================================================================
PIV = "IV. Daneben"
folie([("par", f"{PIV} · weitere Ansprüche"), ("p823", f"{PIV} › Schadensersatz, § 823 BGB"),
       ("versch", f"{PIV} › nur mit Verschulden"), ("unt", f"{PIV} › Unterlassung, § 1004 Abs. 1 Satz 2 BGB analog")], [
    *tafel("par", "IV. Daneben: weitere Ansprüche"),
    z("Schadensersatz:", 110, 180, "p823", "ExtraBold", 36),
    *okz("§ 823 Abs. 1 BGB: Persönlichkeitsrecht", 240, beim("p823", "achthundertdreiundzwanzig"), "Bold", 34),
    *okz("§ 823 Abs. 2 BGB i. V. m. § 22 KUG", 300, beim("p823", "Absatz", 2), "Bold", 34),
    blk(110, 380, 1040, 120, HELLROT, "versch", [("nur mit Verschulden –", "ExtraBold", 34, INK),
                                               ("die Eingriffskondiktion braucht keins", "ExtraBold", 34, INK)]),
    zit("BGH I ZR 120/19, Rn. 26, 70; BGH I ZR 234/10, Rn. 42", 110, 514, "versch"),
    z("Unterlassung:", 110, 590, "unt", "ExtraBold", 36),
    *okz("entsprechend § 1004 Abs. 1 Satz 2 BGB:", 650, beim("unt", "tausendvier"), "Bold", 34),
    z("keine Werbung mehr mit Kais Bild", 185, 696, beim("unt", "Werbung"), "Bold", 34),
    zit("BGH, Urt. v. 7.7.2020 – VI ZR 250/19, Rn. 8; BGH I ZR 41/24, Rn. 126", 185, 746, beim("unt", "Werbung")),
    *requisit([("par", ("tabler", "list-check", 120, WEISS), "weitere Ansprüche", WEISS),
               ("p823", ("tabler", "coin-euro", 120, GELB), "Schadensersatz", GELB),
               ("versch", ("tabler", "alert-triangle", 120, HELLROT), "Verschulden?", HELLROT),
               ("unt", ("tabler", "hand-stop", 130, HELLROT), "Unterlassung", HELLROT)]),
    *stehend("KA", FX, [("par", "ruhig"), ("versch", "denkt"), ("unt", "ernst")]),
])

# ===========================================================================================================================
# I Ergebnis: zurück an die Bushaltestelle (Schauplatz A1)
# ===========================================================================================================================
folie([("erg", "Ergebnis · 3.000 € Wertersatz"), ("erg2", "Ergebnis › keine Werbung mehr mit Kais Bild")], [
    *haltestelle("erg", "erg", "erg"),
    *fig("KO", KOX, BODEN, FH, [("erg", "ruhig"), (beim("erg", "dreitausend"), "froh")], erst="cut"),
    hart(ns(NAME["KO"], KOX, BODEN, "erg", PINK)),
    *fig("KA", KAX, BODEN, FH, [("erg", "ruhig"), (beim("erg", "dreitausend"), "froh")], erst="cut"),
    hart(ns(NAME["KA"], KAX, BODEN, "erg", GRUEN)),
    *okz("3.000 € Wertersatz, §§ 812 Abs. 1 Satz 1 Alt. 2,", 30, beim("erg", "dreitausend"), "Bold", 32, x=1060, rechts=1880),
    z("818 Abs. 2 BGB", 1060, 76, beim("erg", "achthundertachtzehn"), "Bold", 32, rechts=1880),
    *okz("keine Werbung mehr mit seinem Bild", 140, "erg2", "Bold", 32, x=1060, rechts=1880),
    ficon("tabler", "coin-euro", 1330, 330, 110, beim("erg", "dreitausend"), fuell=GELB),
    ficon("tabler", "hand-stop", 1480, 330, 110, "erg2", fuell=HELLROT),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Eingriffskondiktion ohne Verschulden"), ("tipp2", "Klausurtipp · auf Kosten: Zuweisungsgehalt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Eingriffskondiktion auch prüfen, wenn der", 200, 200, "tipp", "Bold", 35),
    z("Schadensersatz am Verschulden scheitert", 200, 250, beim("tipp", "Schadensersatz"), "Bold", 35),
    *okz("§ 812 braucht kein Verschulden", 312, beim("tipp", "braucht"), size=34, x=245),
    linienzug([(130, 390), (1130, 390)], "tipp2", breite=3),
    z("2. „auf dessen Kosten“: mit dem", 200, 420, "tipp2", "Bold", 35),
    z("Zuweisungsgehalt begründen", 200, 470, beim("tipp2", "Zuweisungsgehalt"), "Bold", 35),
    blk(130, 550, 1000, 100, GELB, beim("tipp2", "Vermögensverlust"),
        [("kein Vermögensverlust des Abgebildeten nötig", "ExtraBold", 33, INK)]),
    zit("BGH VI ZR 123/11, Rn. 24; BGH I ZR 41/24, Rn. 124; IX ZR 204/11, Rn. 15", 200, 668, beim("tipp2", "Vermögensverlust")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. etwas erlangt", True),
          (beim("s1", "Nutzung"), 1, "hier: Nutzung des Bildnisses", False),
          ("s2", 0, "2. in sonstiger Weise (keine Leistung)", True),
          ("s3", 0, "3. auf Kosten des Anspruchstellers:", True),
          (beim("s3", "Eingriff"), 1, "Eingriff in den Zuweisungsgehalt (Recht am eigenen Bild)", False),
          ("s4", 0, "4. ohne rechtlichen Grund (keine Einwilligung)", True),
          ("s5", 0, "5. Rechtsfolge: § 818 Abs. 2 BGB", True),
          (beim("s5", "Wertersatz"), 1, "Wertersatz in Höhe der üblichen Lizenzgebühr", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Eingriffskondiktion, § 812 Abs. 1 Satz 1 Alt. 2 BGB"), 110, 90, "sch", 46, )]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 92, 1: 84}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › 1. etwas erlangt"), ("s2", "Prüfschema › 2. in sonstiger Weise"),
       ("s3", "Prüfschema › 3. auf Kosten"), ("s4", "Prüfschema › 4. ohne rechtlichen Grund"),
       ("s5", "Prüfschema › 5. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer mit einem fremden Bild wirbt,", 0)], [("greift in dessen ", 0), ("Zuweisungsgehalt", "a"), (" ein.", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "Zuweisungsgehalt")}),
    *markertext([[("Er schuldet die ", 0), ("übliche Lizenzgebühr", "b"), (",", 0)], [("auch ohne Verschulden", "c"), (" und auch,", 0)],
                 [("wenn der Abgebildete", 0)], [("nie zugestimmt hätte.", 0)]],
                750, 470, 44, "m2", {"b": beim("m2", "übliche"), "c": beim("m2", "ohne")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
