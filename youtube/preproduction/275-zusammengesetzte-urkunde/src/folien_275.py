"""Folge 275 · Zusammengesetzte Urkunde: Das vertauschte Preisschild § 267 – Serienstandard Open Peeps (Katzenkönig).
Fall: Im Baumarkt (fiktiv, ohne Marke) zieht Karlheinz das 29-€-Schild der billigen Bohrmaschine ab, reißt das 149-€-Schild
der teuren ab und klebt das billige fest darauf; an der Kasse tippt Frau Gundlach 29 € ein.
Szenen laut ../SZENENPLAN.md: A1 Werkzeugwand (Umkleben), A2 Kasse, B Sachverhalt, C Wortlautkarte § 267 Abs. 1 und
Urkundenbegriff (Verweis), D zusammengesetzte Urkunde (OLG Karlsruhe 1 Rv 3 Ss 691/18), E feste Verbindung, F Umkleben
(Verfälschen/Herstellen, Gegenansicht), G Gebrauchen, Vorsatz, Variante offener Karton, H Betrug (Wortlautkarte § 263
Abs. 1), I Konkurrenzen und Ergebnis, J Klausurtipp (Lexi, § 274), K Prüfschema, L Merksatz (Lexi).
Handlungsgeräusche: Schild abziehen, Schild abreißen (A1), Kassenschublade (A2); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/redet/fig/ns/okz/neinz/requisit/
wortlaut/kasten als eigene Kopie aus Folge 273 (gemeinsame Dateien unverändert); neu: bohrer_bild(), etikett_bild(),
lochwand(), theke_bild(), kasse_bild(), display(), schnipsel_bild().
Zahlen auf Tafeln, Pillen, Schildern und Blasen als Ziffern; Normtexte nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_275/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_275/" in n:
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
NAME = {"KH": "Karlheinz", "GU": "Frau Gundlach"}
NFARBE = {"KH": GELB, "GU": ROT}


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



# ===========================================================================================================================
# Folge 275: Baumarkt (Werkzeugwand, Kasse), Bohrmaschinen und Preisschilder programmatisch
# ===========================================================================================================================
BODEN_Y = 905
FHA = 500
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HELLLILA = (240, 236, 255, 255)
STAHL = (170, 176, 186, 255)
DUNKEL = (70, 74, 84, 255)


def boden(c):
    return hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], c, breite=7, farbe=INK))


def bohrer_bild(w, koerper, akku=False):
    """Bohrmaschine (Pistolenform, Bohrfutter links), programmatisch; Breite w."""
    h = int(w * 0.9)

    def zz(dr, s):
        S = lambda *p: [v * s for v in p]
        dr.line(S(2, 0.215 * h, 0.13 * w, 0.215 * h), fill=INK, width=int(7 * s))                 # Bohrer
        dr.rounded_rectangle(S(0.12 * w, 0.12 * h, 0.27 * w, 0.31 * h), 8 * s, fill=STAHL, outline=INK, width=4 * s)
        dr.polygon(S(0.55 * w, 0.34 * h, 0.80 * w, 0.34 * h, 0.74 * w, 0.80 * h, 0.52 * w, 0.80 * h), fill=koerper,
                   outline=INK, width=int(4 * s))                                                     # Griff
        dr.rounded_rectangle(S(0.25 * w, 0.04 * h, 0.97 * w, 0.40 * h), 22 * s, fill=koerper, outline=INK, width=5 * s)
        dr.rounded_rectangle(S(0.46 * w, 0.40 * h, 0.53 * w, 0.52 * h), 5 * s, fill=DUNKEL, outline=INK, width=3 * s)
        if akku:
            dr.rounded_rectangle(S(0.40 * w, 0.78 * h, 0.88 * w, 0.97 * h), 10 * s, fill=DUNKEL, outline=INK, width=4 * s)
        else:
            dr.line(S(0.63 * w, 0.80 * h, 0.63 * w, 0.97 * h), fill=INK, width=int(6 * s))       # Kabel
    return _flaeche(w, h, zz)


def etikett_bild(text, w=158, h=86, size=36):
    """Preisetikett des Marktes: Preis und Strichcode (Ziffern auf Tafeln/Schildern)."""
    def zz(dr, s):
        dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), 10 * s, fill=WEISS, outline=INK, width=4 * s)
        f = F("ExtraBold", size * s)
        tw = f.getlength(glyphen(text))
        dr.text(((w * s - tw) / 2, 8 * s), text, font=f, fill=INK)
        x = 22
        for i in range(19):
            b = 2 if i % 3 else 4
            dr.rectangle((x * s, (h - 26) * s, (x + b) * s, (h - 10) * s), fill=INK)
            x += b + 4
    assert F("ExtraBold", size).getlength(text) <= w - 16
    return _flaeche(w, h, zz)


def etikett(text, x, y, c, bis=None, anim="pop", name=None):
    return El(etikett_bild(text), x, y, c, anim, 0.0, bis, name=name or f"etikett:{text}")


def bohrer(x, y, w, koerper, c, akku=False, bis=None, anim="cut", name="bohrer"):
    return El(bohrer_bild(w, koerper, akku), x, y, c, anim, 0.0, bis, name=name)


def lochwand(c, x=110, y=220, w=900, h=640):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 12 * s, fill=(236, 226, 206, 255), outline=INK,
                             width=5 * s)
        for yy in range(40, h - 20, 46):
            for xx in range(40, w - 20, 46):
                dr.ellipse(((xx - 4) * s, (yy - 4) * s, (xx + 4) * s, (yy + 4) * s), fill=(186, 170, 140, 255))
    return hart(El(_flaeche(w, h, zz), x, y, c, "cut", 0.0, None, name="lochwand"))


def haken_wand(x, y, c):
    return hart(linienzug([(x, y), (x, y + 40), (x + 26, y + 40)], c, breite=7, farbe=INK))


def theke_bild(w=640, h=210):
    def zz(dr, s):
        dr.rectangle((3 * s, 18 * s, (w - 3) * s, (h - 1) * s), fill=HOLZ, outline=INK, width=5 * s)
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, 24 * s), fill=HOLZ2, outline=INK, width=5 * s)
        for k in range(1, 4):
            dr.line(((k * w / 4) * s, 40 * s, (k * w / 4) * s, (h - 20) * s), fill=HOLZ2, width=4 * s)
    return _flaeche(w, h, zz)


def kasse_bild(w=230, h=170):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 60 * s, (w - 3) * s, (h - 3) * s), 12 * s, fill=GRAU2, outline=INK, width=5 * s)
        dr.rounded_rectangle((20 * s, 3 * s, (w - 20) * s, 70 * s), 10 * s, fill=DUNKEL, outline=INK, width=5 * s)
        for r in range(2):
            for k in range(5):
                x0, y0 = 26 + k * 38, 92 + r * 32
                dr.rounded_rectangle((x0 * s, y0 * s, (x0 + 28) * s, (y0 + 22) * s), 4 * s, fill=WEISS, outline=INK,
                                     width=3 * s)
    return _flaeche(w, h, zz)


def display(text, x, y, c, bis=None):
    w, h = 190, 60
    def zz(dr, s):
        f = F("ExtraBold", 34 * s)
        tw = f.getlength(glyphen(text))
        dr.text(((w * s - tw) / 2, 6 * s), text, font=f, fill=(150, 240, 160, 255))
    return El(_flaeche(w, h, zz), x, y, c, "fade", 0.0, bis, name=f"display:{text}")


def schnipsel_bild():
    def zz(dr, s):
        dr.polygon([(4 * s, 30 * s), (40 * s, 8 * s), (62 * s, 34 * s), (30 * s, 52 * s)], fill=WEISS, outline=INK)
        dr.polygon([(70 * s, 40 * s), (104 * s, 26 * s), (118 * s, 50 * s), (84 * s, 60 * s)], fill=WEISS, outline=INK)
        dr.line([(4 * s, 30 * s), (40 * s, 8 * s), (62 * s, 34 * s), (30 * s, 52 * s), (4 * s, 30 * s)], fill=INK,
                width=4 * s)
        dr.line([(70 * s, 40 * s), (104 * s, 26 * s), (118 * s, 50 * s), (84 * s, 60 * s), (70 * s, 40 * s)], fill=INK,
                width=4 * s)
    return _flaeche(122, 64, zz)


# ===========================================================================================================================
# A1 Fall: Baumarkt, Werkzeugwand – zwei Bohrmaschinen, das Schild wird umgeklebt
# ===========================================================================================================================
BA = (210, 390, 300)                      # billige Maschine: x, y, Breite (Kabel)
BB = (590, 360, 380)                      # teure Maschine: x, y, Breite (Akku)
EA = (BA[0] + 145, BA[1] + 20)            # Etikett auf der billigen Maschine
EB = (BB[0] + 190, BB[1] + 28)            # Etikett auf der teuren Maschine
EH = (EA[0] + 60, BA[1] - 120)            # abgezogenes Etikett (in der Hand gedacht, über der Wand)
KHX = 1330
KH_A = ("KH_redet", KHX, BODEN_Y, FHA)
SCHILD = beim("zwei", "Preisschild")
ABZ = beim("abzieh", "zieht")
ABR = beim("abreiss", "reißt")
KLB = beim("kleb", "klebt")
ab_e = etikett("29 €", *EA, SCHILD, bis=ABZ)
ab_h = bewegt(etikett("29 €", *EH, ABZ, anim="cut", name="etikett:29 € abgezogen"), ABZ, (ABZ[0], ABZ[1] + 0.45),
              EA[0] - EH[0], EA[1] - EH[1])
ab_h.bis = KLB
ab_k = bewegt(etikett("29 €", *EB, KLB, anim="cut", name="etikett:29 € auf teurer Maschine"), KLB,
              (KLB[0], KLB[1] + 0.45), EH[0] - EB[0], EH[1] - EB[1])
folie([(NULL, "Fall · Baumarkt, Werkzeugabteilung"), ("billig", "Fall · zwei Preisschilder: 29 € und 149 €"),
       ("abzieh", "Fall · Karlheinz tauscht die Schilder"), ("ka1", "Fall · teure Maschine mit 29-€-Schild")], [
    boden(NULL), lochwand(NULL),
    bohrer(*BA[:2], BA[2], BLAU, NULL, name="bohrer:billig"),
    bohrer(*BB[:2], BB[2], GRUEN, NULL, akku=True, name="bohrer:teuer"),
    bis_(hart(pl("Baumarkt · Werkzeugabteilung", 70, 30, NULL, fill=GELB, size=38)), "ka1"),
    ab_e, etikett("149 €", *EB, SCHILD, bis=ABR),
    ring(EA[0] + 79, EA[1] + 43, 120, 72, "billig", farbe=ORANGE, breite=6, bis="teuer"),
    ring(EB[0] + 79, EB[1] + 43, 120, 72, "teuer", farbe=ORANGE, breite=6, bis="abzieh"),
    bis_(pl("billig", BA[0] + 90, BA[1] + 300, "billig", fill=HELLBLAU, size=30), "abzieh"),
    bis_(pl("teuer", BB[0] + 150, BB[1] + 370, "teuer", fill=HELLGRUEN, size=30), "abzieh"),
    szene(ab_h, "275abziehen*", 0.9, versatz=-0.28),
    szene(El(schnipsel_bild(), BB[0] + 230, BODEN_Y - 70, ABR, "pop", 0.0, None, name="schnipsel"), "275abreissen*", 1.0,
          versatz=-0.2),
    pl("abgerissen", BB[0] + 200, BODEN_Y - 140, ABR, fill=HROT, size=30),
    ab_k,
    pl("fest aufgeklebt", EB[0] - 30, EB[1] - 70, beim("kleb", "fest"), fill=HELLGRUEN, size=30),
    *fig("KH", KHX, BODEN_Y, FHA, [(beim("abzieh", "Karlheinz"), "eifrig"), ("kleb", "froh")], erst="pop", bis="ka1"),
    ns(NAME["KH"], KHX, BODEN_Y, beim("abzieh", "Karlheinz"), NFARBE["KH"], d=0.1),
    *redet("KH_redet", KHX, BODEN_Y, FHA, "ka1", "kasse"),
    blase("sprech", 640, 170, "ka1", 1240, 200, inhalt=["So, jetzt kostet", "die hier 29 €."], textsize=34, figur=KH_A,
          bis="kasse"),
])

# ===========================================================================================================================
# A2 Fall: an der Kasse
# ===========================================================================================================================
GUX = 470
KHK = 1560
TH = (680, BODEN_Y - 210)                 # Theke
KA = (720, TH[1] - 165)                   # Kasse auf der Theke
BK = (1000, TH[1] - 200, 260)             # teure Maschine auf der Theke
GU_K = ("GU_redet_r", GUX, BODEN_Y, FHA)
NIMMT = beim("zahlt", "nimmt")
mit_bk = bohrer(*BK[:2], BK[2], GRUEN, "kasse", akku=True, name="bohrer:teuer an der Kasse")
mit_bk.bis = NIMMT
mit_et = El(etikett_bild("29 €", w=120, h=66, size=28), BK[0] + 130, BK[1] + 14, "kasse", "cut", 0.0, NIMMT,
            name="etikett:29 € an der Kasse")
HX_, HY_ = KHK - 330, BODEN_Y - 420       # Maschine in der Hand von Karlheinz (vor ihm)
mit_h = bewegt(bohrer(HX_, HY_, BK[2], GRUEN, NIMMT, akku=True, name="bohrer:teuer mitgenommen"), NIMMT,
               (NIMMT[0], NIMMT[1] + 0.5), BK[0] - HX_, BK[1] - HY_)
mit_he = bewegt(El(etikett_bild("29 €", w=120, h=66, size=28), HX_ + 130, HY_ + 14, NIMMT, "cut", 0.0, None,
                   name="etikett:29 € mitgenommen"), NIMMT, (NIMMT[0], NIMMT[1] + 0.5), BK[0] - HX_, BK[1] - HY_)
folie([("kasse", "Fall · an der Kasse"), ("ga1", "Fall · 29 € statt 149 €"), ("zahlt", "Fall · bezahlt und mitgenommen"),
       ("frage", "Frage · Urkunde gefälscht?"), ("frage2", "Frage · Betrug an der Kasse?")], [
    boden("kasse"),
    bis_(hart(pl("Baumarkt · Kasse", 70, 30, "kasse", fill=GELB, size=38)), "ga1"),
    hart(El(theke_bild(), *TH, "kasse", "cut", 0.0, None, name="theke")),
    hart(El(kasse_bild(), *KA, "kasse", "cut", 0.0, None, name="kasse")),
    hart(mit_bk), hart(mit_et),
    display("29,00 €", KA[0] + 20, KA[1] + 4, beim("kasse", "Preis")),
    szene(ficon("tabler", "cash-banknote", 1250, TH[1] - 4, 110, beim("zahlt", "zahlt"), fuell=HELLGRUEN, bis=NIMMT),
          "275kasse*", 0.8, versatz=-0.1),
    pl("bezahlt: 29 €", 1010, TH[1] - 300, beim("zahlt", "zahlt"), fill=HELLGRUEN, size=30, bis=NIMMT),
    mit_h, mit_he,
    pl("Urkunde gefälscht?", 760, 170, "frage", fill=WEISS, size=36),
    pl("Schild selbst echt", 760, 250, beim("frage", "Preisschild"), fill=HELLGRUEN, size=32),
    pl("Betrug an der Kasse?", 760, 330, "frage2", fill=PINK, size=36),
    *fig("GU", GUX, BODEN_Y, FHA, [("kasse", "ruhig_r")], erst="cut", bis="ga1"),
    *redet("GU_redet_r", GUX, BODEN_Y, FHA, "ga1", "zahlt"),
    *fig("GU", GUX, BODEN_Y, FHA, [("zahlt", "froh_r")], erst="cut", bis="sv"),
    hart(ns(NAME["GU"], GUX, BODEN_Y, "kasse", NFARBE["GU"])),
    *fig("KH", KHK, BODEN_Y, FHA, [("kasse", "ruhig"), ("zahlt", "froh")], erst="cut", bis="sv"),
    hart(ns(NAME["KH"], KHK, BODEN_Y, "kasse", NFARBE["KH"])),
    blase("sprech", 520, 160, "ga1", 720, 190, inhalt=["29 €, bitte."], textsize=36, figur=GU_K, bis="zahlt"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_275(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt · das vertauschte Preisschild")], els)


sachverhalt_275("sv", [
    "In einem Baumarkt hängen zwei Bohrmaschinen. Auf jeder klebt ein Preisschild des Marktes: auf der einen 29 €, auf "
    "der anderen 149 €.",
    "Karlheinz zieht das Schild der billigen Maschine ab. Das Schild der teuren reißt er ab und klebt das 29-€-Schild "
    "fest darauf.",
    "An der Kasse tippt die Kassiererin, Frau Gundlach, den Preis vom Schild ein. Karlheinz zahlt 29 € und nimmt die "
    "teure Maschine mit.",
], "Strafbarkeit von Karlheinz nach §§ 267, 263 StGB?")

# ===========================================================================================================================
# C § 267 Abs. 1 StGB (Wortlautkarte) und Urkundenbegriff (Verweis)
# ===========================================================================================================================
W267 = ("„Wer zur Täuschung im Rechtsverkehr eine unechte Urkunde herstellt, eine echte Urkunde verfälscht oder eine "
        "unechte oder verfälschte Urkunde gebraucht, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe "
        "bestraft.“")
w267, w267_y = wortlaut(80, 180, 1100, W267, "§ 267 Abs. 1 StGB", "p267", marken=[
    ("Täuschung im Rechtsverkehr", beim("w267", "Täuschung")), ("unechte Urkunde herstellt", beim("w267", "herstellt")),
    ("echte Urkunde verfälscht", beim("w267", "verfälscht")), ("gebraucht", beim("w267", "gebraucht"))], size=32)
assert w267_y <= 470, w267_y
FUNK = [("Perpetuierung", "drei", 110, GELB), ("Beweis", beim("drei", "Beweis"), 450, HELLBLAU),
        ("Garantie", beim("drei", "Garantie"), 700, HELLGRUEN)]
folie([("p267", "§ 267 Abs. 1 StGB › Wortlaut"), ("begriff", "Urkunde › Begriff (Folge: gefälschte Entschuldigung)"),
       ("drei", "Urkunde › Perpetuierung, Beweis, Garantie")], rechts_frei([
    *tafel("p267", "Urkundenfälschung, § 267 Abs. 1"),
    *w267,
    pl("Urkundenbegriff: Folge „Die gefälschte Entschuldigung“", 110, w267_y + 20, "begriff", fill=HELLLILA, size=30),
    blk(110, w267_y + 100, 1040, 170, WEISS, "def", [("Urkunde = verkörperte Gedankenerklärung,", "Bold", 33, INK),
                                                     ("zum Beweis im Rechtsverkehr geeignet und bestimmt,", "Bold", 33, INK),
                                                     ("Aussteller erkennbar", "Bold", 33, INK)]),
    *[pl(t, x, w267_y + 300, c, fill=f, size=34) for t, c, x, f in FUNK],
    *requisit([("p267", ("fluent-emoji-flat", "balance-scale", 120, None), "§ 267 StGB", WEISS),
               ("begriff", ("tabler", "file-text", 100, WEISS), "Was ist eine Urkunde?", WEISS),
               ("drei", ("tabler", "list-check", 100, WEISS), "3 Funktionen", WEISS)]),
    *stehend("KH", X1, [("p267", "ruhig"), ("begriff", "denkt")]),
    *stehend("GU", X2, [("p267", "ruhig"), ("drei", "froh")]),
]))

# ===========================================================================================================================
# D Zusammengesetzte Urkunde: Erklärung + Bezugsobjekt, fest verbunden = neue Beweiseinheit
# ===========================================================================================================================
DB = (520, 200, 300)                      # Maschine in der Tafel
DE = (160, 230)                           # Etikett allein
ZE = (DB[0] + 145, DB[1] + 20)            # Etikett auf der Maschine (nach „fest verbunden“)
FV = beim("zus", "fest")
folie([("allein", "Zusammengesetzte Urkunde › Schild allein: wofür?"),
       ("zus", "Zusammengesetzte Urkunde › Erklärung + Bezugsobjekt, fest verbunden"),
       ("einheit", "Zusammengesetzte Urkunde › neue Beweiseinheit"), ("bz", "Zusammengesetzte Urkunde › Beweiszeichen"),
       ("olg", "Zusammengesetzte Urkunde › Preisschild auf Ware: OLG Karlsruhe"),
       ("aussage", "Zusammengesetzte Urkunde › Erklärung des Marktes"),
       ("aussteller", "Zusammengesetzte Urkunde › Aussteller: der Baumarkt")], rechts_frei([
    *tafel("allein", "Zusammengesetzte Urkunde"),
    bis_(etikett("29 €", *DE, "allein", name="etikett:allein"), FV),
    bis_(pl("wofür?", DE[0] - 20, DE[1] + 110, beim("allein", "Wofür"), fill=HROT, size=32), FV),
    bis_(ticon("tabler", "help", DE[0] + 230, DE[1] + 90, 80, beim("allein", "Wofür"), fuell=WEISS), FV),
    El(bohrer_bild(DB[2], GRUEN, True), DB[0], DB[1], beim("allein", "Ware"), "pop", 0.0, None, name="tafelbild:bohrer"),
    etikett("29 €", *ZE, FV, name="etikett:fest verbunden"),
    z("Erklärung + Bezugsobjekt, fest verbunden", 110, 470, "zus", "Bold", 34),
    ring(DB[0] + 150, DB[1] + 120, 175, 128, "einheit", farbe=ORANGE, breite=6),
    pl("neue Beweiseinheit", 880, 230, "einheit", fill=GELB, size=32),
    z("Beweiszeichen, z. B. Fahrzeug-Ident.-Nr. am Auto", 110, 530, "bz", "Bold", 32),
    ticon("tabler", "car", 1090, 590, 80, beim("bz", "Fahrzeugidentifikationsnummer"), fuell=HELLBLAU),
    z("aufgeklebte Preisschilder: ebenso", 110, 590, "olg", "Bold", 32),
    zit("OLG Karlsruhe, 13.3.2019 – 1 Rv 3 Ss 691/18 (Strichcode im Baumarkt)", 110, 638, beim("olg", "Strichcode")),
    blk(110, 690, 1040, 80, HGELB, "aussage", [("„Der Markt bietet diese Maschine für 29 € an.“", "ExtraBold", 34, INK)]),
    *okz("Aussteller: der Baumarkt, keine Unterschrift nötig", 800, "aussteller", "Bold", 32, x=170),
    *requisit([("allein", ("tabler", "tag", 100, WEISS), "Schild allein?", WEISS),
               ("zus", ("tabler", "link", 100, HELLGRUEN), "fest verbunden", HELLGRUEN),
               ("bz", ("tabler", "car", 110, HELLBLAU), "Beweiszeichen", WEISS),
               ("olg", ("tabler", "barcode", 100, WEISS), "OLG Karlsruhe", WEISS),
               ("aussteller", ("tabler", "building-store", 110, GELB), "Aussteller: Markt", WEISS)]),
    *stehend("KH", X1, [("allein", "denkt"), ("einheit", "ruhig"), ("aussage", "ernst")]),
    *stehend("GU", X2, [("allein", "ruhig"), ("aussteller", "froh")]),
]))

# ===========================================================================================================================
# E Wann fest verbunden?
# ===========================================================================================================================
MB = 180                                  # Mini-Maschinen-Breite (vor der Tat)
folie([("fest", "Feste Verbindung › auf Dauer, nicht untrennbar"), ("kleber", "Feste Verbindung › aufgeklebt (+)"),
       ("lose", "Feste Verbindung › lose angeheftet (−)"), ("steck", "Feste Verbindung › bloß aufgesteckt (−)"),
       ("vorher", "Feste Verbindung › vor der Tat: 2 echte Urkunden")], rechts_frei([
    *tafel("fest", "Wann fest verbunden?"),
    blk(110, 180, 1040, 80, HELLBLAU, "fest", [("auf Dauer angelegt, nicht untrennbar", "ExtraBold", 36, INK)]),
    *okz("mit Klebstoff aufgeklebtes Etikett", 300, "kleber", "Bold", 34, x=170),
    ticon("tabler", "sticker", 1080, 350, 70, "kleber", fuell=HELLGRUEN),
    *neinz("nur lose angeheftetes Schild", 380, "lose", "Bold", 34, x=170),
    ticon("tabler", "paperclip", 1080, 430, 70, "lose", fuell=WEISS),
    *neinz("Teil bloß aufgesteckt", 460, "steck", "Bold", 34, x=170),
    ticon("tabler", "plug-connected", 1080, 510, 70, "steck", fuell=WEISS),
    zit("OLG Karlsruhe, 1 Rv 3 Ss 691/18, Rn. 31, 36, 37", 110, 530, "steck"),
    z("Vor der Tat:", 110, 600, "vorher", "ExtraBold", 34),
    El(bohrer_bild(MB, BLAU), 150, 650, "vorher", "pop", 0.0, None, name="tafelbild:billig"),
    El(etikett_bild("29 €", w=110, h=60, size=26), 230, 650, "vorher", "pop", 0.0, None, name="etikett:mini 29"),
    El(bohrer_bild(MB, GRUEN, True), 420, 650, (("vorher", 0.15)), "pop", 0.0, None, name="tafelbild:teuer"),
    El(etikett_bild("149 €", w=110, h=60, size=26), 500, 650, ("vorher", 0.15), "pop", 0.0, None, name="etikett:mini 149"),
    pl("2 echte zusammengesetzte Urkunden", 640, 700, beim("vorher", "echte"), fill=HELLGRUEN, size=28),
    *requisit([("fest", ("tabler", "link", 100, WEISS), "fest verbunden?", WEISS),
               ("kleber", ("tabler", "sticker", 100, HELLGRUEN), "aufgeklebt", HELLGRUEN),
               ("lose", ("tabler", "paperclip", 100, WEISS), "lose", HROT),
               ("vorher", ("tabler", "circle-check", 100, HELLGRUEN), "2 Urkunden", WEISS)]),
    *stehend("KH", X1, [("fest", "ruhig"), ("lose", "denkt"), ("vorher", "ernst")]),
    *stehend("GU", X2, [("fest", "ruhig"), ("kleber", "froh")]),
]))

# ===========================================================================================================================
# F Umkleben: Verfälschen durch Austausch des Bezugsobjekts, zugleich Herstellen; Gegenansicht
# ===========================================================================================================================
UB = (720, 150, 230)
folie([("umk", "Umkleben · neue Einheit: 29-€-Schild + teure Maschine"),
       ("verf", "Umkleben › Rspr.: Verfälschen durch Austausch des Bezugsobjekts"),
       ("herst", "Umkleben › zugleich Herstellen einer unechten Urkunde"),
       ("gegen", "Umkleben › Gegenansicht: Austausch kein Verfälschen"),
       ("neufest", "Umkleben › neue Verbindung fest (+)")], rechts_frei([
    *tafel("umk", "Das Umkleben"),
    El(bohrer_bild(UB[2], GRUEN, True), UB[0], UB[1], "umk", "pop", 0.0, None, name="tafelbild:teuer"),
    El(etikett_bild("29 €", w=130, h=72, size=30), UB[0] + 100, UB[1] + 10, beim("neu", "billige"), "pop", 0.0, None, name="etikett:umgeklebt"),
    z("Anschein: Der Markt hat", 110, 200, beim("neu", "Einheit"), "Bold", 34),
    z("genau das erklärt.", 110, 250, beim("neu", "Einheit"), "Bold", 34),
    *neinz("hat er nicht", 320, beim("neu", "nicht"), "ExtraBold", 34, x=170),
    blk(110, 400, 1040, 130, HGELB, "verf", [("Rspr.: Verfälschen – Austausch", "ExtraBold", 36, INK),
                                             ("des Bezugsobjekts genügt", "ExtraBold", 36, INK)]),
    zit("OLG Karlsruhe, Rn. 36 (mit BGHSt 9, 235; 16, 94)", 110, 540, "verf"),
    z("zugleich: Herstellen einer unechten Urkunde", 110, 600, "herst", "Bold", 34),
    pl("tritt zurück", 880, 598, beim("herst", "Falllösungen"), fill=GRAU2, size=28),
    z("Gegenansicht: Austausch ist kein Verfälschen", 110, 700, "gegen", "Bold", 34, farbe=DROT),
    *okz("auch die neue Verbindung fest: aufgeklebt", 790, beim("neufest", "klebt"), "Bold", 34, x=170),
    *requisit([("umk", ("tabler", "replace", 100, WEISS), "umgeklebt", WEISS),
               ("verf", ("tabler", "pencil", 100, HGELB), "verfälscht", HGELB),
               ("herst", ("tabler", "file-x", 100, WEISS), "unecht", WEISS),
               ("gegen", ("fluent-emoji-flat", "balance-scale", 110, None), "Streit", WEISS),
               ("neufest", ("tabler", "sticker", 100, HELLGRUEN), "fest", HELLGRUEN)]),
    *stehend("KH", X1, [("umk", "froh"), ("neu", "ernst"), ("gegen", "denkt"), ("neufest", "sorge")]),
    *stehend("GU", X2, [("umk", "ruhig"), ("verf", "denkt"), ("neufest", "ernst")]),
]))

# ===========================================================================================================================
# G Gebrauchen, subjektiver Tatbestand, Variante offener Karton
# ===========================================================================================================================
folie([("gebr", "Tathandlung › Gebrauchen: Vorlage an der Kasse (+)"),
       ("subj", "Subjektiv › Vorsatz, zur Täuschung im Rechtsverkehr (+)"),
       ("karton", "Variante › teure Maschine im offenen Karton: § 267 (−)")], rechts_frei([
    *tafel("gebr", "Gebrauchen und Vorsatz"),
    *okz("Gebrauchen: Vorlage an der Kasse", 190, beim("gebr", "gebraucht"), "Bold", 34, x=170),
    *okz("Vorsatz", 260, beim("subj", "vorsätzlich"), "Bold", 34, x=170),
    *okz("zur Täuschung im Rechtsverkehr:", 330, beim("subj", "Kombination"), "Bold", 34, x=170),
    z("Kombination echt, nur 29 € verlangen", 170, 380, beim("subj", "neunundzwanzig"), "Regular", 32),
    karte(100, 470, 1060, 330, "karton", fill=HELLLILA, rund=18, schatten=6, rand=4),
    z("Variante: teure Maschine im offenen Karton", 140, 495, "karton", "ExtraBold", 34),
    ticon("tabler", "package", 230, 700, 150, beim("karton", "Karton"), fuell=GELB),
    El(etikett_bild("29 €", w=110, h=60, size=26), 175, 640, beim("karton", "Karton"), "pop", 0.0, None,
       name="etikett:karton"),
    z("Schild klebt nur am Karton", 380, 580, beim("karton", "klebt"), "Bold", 32),
    *neinz("mit dem Inhalt nicht fest verbunden", 640, beim("karton", "Inhalt"), "Bold", 32, x=425),
    z("§ 267 regelmäßig (−)", 380, 700, beim("karton", "regelmäßig"), "ExtraBold", 34, farbe=DROT),
    zit("OLG Karlsruhe, Rn. 37; OLG Köln, 4.7.1978 – 1 Ss 231/78", 140, 755, beim("karton", "regelmäßig")),
    *requisit([("gebr", ("ph", "cash-register", 110, WEISS), "an der Kasse", WEISS),
               ("subj", ("tabler", "brain", 100, LILA), "Vorsatz", WEISS),
               ("karton", ("tabler", "package", 110, GELB), "offener Karton", HELLLILA)]),
    *stehend("KH", X1, [("gebr", "ruhig"), ("subj", "froh"), ("karton", "denkt")]),
    *stehend("GU", X2, [("gebr", "ruhig"), ("subj", "denkt"), ("karton", "ruhig")]),
]))

# ===========================================================================================================================
# H Betrug an der Kasse: Wortlautkarte § 263 Abs. 1 StGB, Subsumtion
# ===========================================================================================================================
W263 = ("„Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen "
        "eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch Entstellung oder Unterdrückung "
        "wahrer Tatsachen einen Irrtum erregt oder unterhält, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit "
        "Geldstrafe bestraft.“")
w263, w263_y = wortlaut(80, 170, 1100, W263, "§ 263 Abs. 1 StGB", "p263", marken=[
    ("Vorspiegelung falscher", beim("w263", "Täuschung")), ("Irrtum erregt", beim("w263", "Irrtum")),
    ("beschädigt", beim("w263", "Schaden")), ("Absicht", beim("w263", "Bereicherungsabsicht"))], size=29)
assert w263_y <= 560, w263_y
PR = [("t1", "1. Täuschung: falscher Preis, schlüssig vorgespiegelt", beim("t1", "spiegelt")),
      ("t2", "2. Irrtum: 29 € seien der richtige Preis", beim("t2", "hält")),
      ("t3", "3. Verfügung: Herausgabe, kein Diebstahl", beim("t3", "Vermögensverfügung")),
      ("t4", "4. Schaden: teure Maschine zum Preis der billigen", beim("t4", "bekommt")),
      ("t5", "5. Vorsatz und Bereicherungsabsicht", beim("t5", "bereichern"))]
els_h = [*tafel("betrug", "Betrug an der Kasse, § 263"), *w263]
for i, (c, t, ok_c) in enumerate(PR):
    els_h += [z(t, 160, w263_y + 22 + i * 62, c, "Bold", 31), bis_(ok(115, w263_y + 42 + i * 62, ok_c, gr=20), None)]
assert w263_y + 22 + 4 * 62 + 45 <= 890
folie([("betrug", "Betrug · § 263 Abs. 1 StGB"), ("t1", "Betrug › Täuschung: falscher Preis (+)"),
       ("t2", "Betrug › Irrtum (+)"), ("t3", "Betrug › Vermögensverfügung, kein Diebstahl (+)"),
       ("t4", "Betrug › Vermögensschaden (+)"), ("t5", "Betrug › Vorsatz, Bereicherungsabsicht (+)")], rechts_frei([
    *els_h,
    *requisit([("betrug", ("ph", "cash-register", 110, WEISS), "Betrug?", WEISS),
               ("t1", ("tabler", "tag", 100, WEISS), "falscher Preis", HROT),
               ("t3", ("tabler", "hand-grab", 100, WEISS), "Herausgabe", WEISS),
               ("t4", ("tabler", "receipt-euro", 100, HROT), "Schaden", HROT),
               ("t5", ("tabler", "brain", 100, LILA), "Absicht", WEISS)]),
    *stehend("KH", X1, [("betrug", "ruhig"), ("t2", "froh"), ("t4", "ernst")]),
    *stehend("GU", X2, [("betrug", "ruhig"), ("t2", "froh"), ("t4", "staunt")]),
]))

# ===========================================================================================================================
# I Ergebnis und Konkurrenzen
# ===========================================================================================================================
folie([("erg", "Ergebnis › rechtswidrig, schuldhaft"), ("konk", "Konkurrenzen › Tateinheit"),
       ("erg2", "Ergebnis · §§ 267, 263, 52 StGB")], rechts_frei([
    *tafel("erg", "Konkurrenzen und Ergebnis"),
    *okz("rechtswidrig und schuldhaft", 190, beim("erg", "Rechtswidrig"), "Bold", 34, x=170),
    kasten(110, 290, 390, 130, HGELB, beim("konk", "Urkundenfälschung"), name="kasten:267"),
    z("Urkundenfälschung", 135, 305, beim("konk", "Urkundenfälschung"), "ExtraBold", 32, rechts=495),
    z("§ 267 Abs. 1", 135, 355, beim("konk", "Urkundenfälschung"), "Bold", 30, rechts=495),
    kasten(800, 290, 350, 130, HELLBLAU, beim("konk", "Betrug"), name="kasten:263"),
    z("Betrug", 825, 305, beim("konk", "Betrug"), "ExtraBold", 32, rechts=1140),
    z("§ 263 Abs. 1", 825, 355, beim("konk", "Betrug"), "Bold", 30, rechts=1140),
    pl("Tateinheit, § 52", 520, 330, beim("konk", "Tateinheit"), fill=GELB, size=28),
    z("Vorlegen an der Kasse = Gebrauchen + Täuschung", 110, 470, beim("konk", "Vorlegen"), "Bold", 34),
    blk(110, 580, 1040, 140, HELLGRUEN, "erg2", [("Karlheinz: Urkundenfälschung", "ExtraBold", 38, INK),
                                               ("in Tateinheit mit Betrug", "ExtraBold", 38, INK)]),
    zit("BGH 5 StR 38/23, Rn. 12; BGH 3 StR 156/08, Rn. 11", 110, 735, "erg2"),
    *requisit([("erg", ("tabler", "circle-check", 100, HELLGRUEN), "RW, Schuld", WEISS),
               ("konk", ("tabler", "link", 100, GELB), "Tateinheit", GELB),
               ("erg2", ("fluent-emoji-flat", "balance-scale", 110, None), "strafbar", WEISS)]),
    *stehend("KH", X1, [("erg", "ernst"), ("erg2", "sorge")]),
    *stehend("GU", X2, [("erg", "ruhig"), ("konk", "denkt"), ("erg2", "ernst")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: womit fest verbunden?", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Frag bei jedem Schild zuerst:", 200, 200, beim("tipp", "Frag"), "Bold", 34),
         z("womit ist es fest verbunden?", 200, 250, beim("tipp", "womit"), "ExtraBold", 36),
         El(etikett_bild("29 €"), 240, 340, beim("tipp", "Schild", 2), "pop", 0.0, None, name="etikett:tipp"),
         z("+", 440, 350, beim("tipp", "Ware"), "ExtraBold", 54),
         El(bohrer_bild(220, GRUEN, True), 500, 320, beim("tipp", "Ware"), "pop", 0.0, None, name="tafelbild:tipp"),
         pl("= Urkunde", 760, 370, beim("tipp", "Urkunde"), fill=HELLGRUEN, size=34),
         blk(110, 590, 1040, 140, HROT, "tipp2", [("abgerissenes teures Schild gesondert:", "Bold", 34, INK),
                                                  ("§ 274 Abs. 1 Nr. 1 StGB prüfen", "ExtraBold", 36, INK)]),
         zit("OLG Karlsruhe, Rn. 33: Abreißen vernichtet die Urkunde", 110, 745, beim("tipp2", "Urkundenunterdrückung")),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · womit ist das Schild fest verbunden?"), ("tipp2", "Klausurtipp › § 274 beim abgerissenen Schild")],
      els_k)

# ===========================================================================================================================
# K Prüfschema (Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Tatbestand", 0, BLAU, "ExtraBold"),
          ("k1a", "1.", "objektiv: a) zusammengesetzte Urkunde – Erklärung + Bezugsobjekt, fest verbunden", 1, None, "Bold"),
          ("k1b", "", "b) Tathandlung: Verfälschen durch Austausch (zugleich Herstellen), Gebrauchen", 1, None, "Bold"),
          ("k1c", "2.", "subjektiv: Vorsatz, zur Täuschung im Rechtsverkehr", 1, None, "Bold"),
          ("k2", "II./III.", "Rechtswidrigkeit, Schuld", 0, GRUEN, "ExtraBold"),
          ("k4", "IV.", "Konkurrenzen: Tateinheit mit Betrug, § 263", 0, GELB, "ExtraBold")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Urkundenfälschung am Preisschild"), 110, 90, "sch", 50)]
y = 220
for c, nr, text, tief, f, stil in REIHEN:
    if f:
        els_sch.append(pl(nr, 130, y - 6, c, fill=f, size=34))
        els_sch.append(z(text, 330, y, c, stil, 40, rechts=1820))
    else:
        if nr:
            els_sch.append(z(nr, 330, y, c, "ExtraBold", 36, rechts=1820))
        els_sch.append(z(text, 400, y, c, stil, 34, rechts=1820))
    y += 120
assert y <= 960, y
folie([("sch", "Prüfschema · Urkundenfälschung am Preisschild"), ("k1", "Prüfschema › I. Tatbestand"),
       ("k1a", "Prüfschema › I. 1. a) zusammengesetzte Urkunde"), ("k1b", "Prüfschema › I. 1. b) Tathandlung"),
       ("k1c", "Prüfschema › I. 2. subjektiv"), ("k2", "Prüfschema › II. Rechtswidrigkeit, III. Schuld"),
       ("k4", "Prüfschema › IV. Konkurrenzen")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein Preisschild allein ist ", 0), ("keine", "a"), (" Urkunde,", 0)],
                 [("erst ", 0), ("fest verbunden", "b"), (" mit der Ware.", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "keine"), "b": beim("merke", "fest")}),
    *markertext([[("Wer es fest auf eine andere Ware klebt,", 0)], [("fälscht eine ", 0), ("Urkunde", "c"), (",", 0)]],
                750, 480, 42, "m2", {"c": beim("m2", "Urkunde")}),
    *markertext([[("und wer damit an der Kasse bezahlt,", 0)], [("begeht zugleich einen ", 0), ("Betrug", "d"), (".", 0)]],
                750, 660, 42, "m3", {"d": beim("m3", "Betrug")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
