"""Folge 200 · Baugebiete BauNVO: Was darf ins Wohngebiet? (§ 30 BauGB) – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Ein qualifizierter Bebauungsplan (2022) setzt für eine neue Siedlung im Norden ein reines, im Süden ein
allgemeines Wohngebiet fest. Frau Möhring will im Norden eine Kita (2 Gruppen, 30 Plätze, Kinder aus der Siedlung) eröffnen,
Herr Tiemann im Süden ein kleines Tattoo-Studio (nur nach Termin, kein Lärm, Kundschaft aus der ganzen Stadt).
Szenen laut ../SZENENPLAN.md: A1 Siedlung Nord (Plan, Kita), A2 Süden (Ladenlokal), B Sachverhalt, C § 30 Abs. 1 BauGB
(Wortlautkarte), D Baugebiete § 1 Abs. 2 BauNVO (Tabelle), E Aufbau §§ 2–9, § 31 Abs. 1 BauGB (Wortlautkarte),
Gebietsverträglichkeit, F Kita § 3 BauNVO (Wortlautkarte), G Kinderlärm § 22 Abs. 1a BImSchG (Wortlautkarte), H Studio § 4
Abs. 1, 2 BauNVO (Wortlautkarte), I Ausnahme § 4 Abs. 3 Nr. 2 BauNVO (Wortlautkarte), § 246e BauGB, J § 15 Abs. 1 BauNVO
(Wortlautkarte), K Ergebnis (Siedlung), L Prüfschema, M Klausurtipp (Lexi), N Merksatz (Lexi).
Handlungsgeräusch: Ladenglocke, als Herr Tiemann in die Tür seines Ladenlokals tritt (A2); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist (Kinder unbenannt, ohne Schild). Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz/tabelle als eigene Kopie aus Folge 188 (gemeinsame Dateien unverändert); neu: bplan(),
zone(), laden(), kinder().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BauGB, BauNVO, BImSchG),
Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_200/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_200/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (232, 240, 238, 255)
WAND2 = (242, 232, 214, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))




def schreibtisch(c, x0, x1, h=170):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"MO": "Frau Möhring", "TI": "Herr Tiemann"}
NFARBE = {"MO": ROSE, "TI": BLAU}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
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


def zwei(folge_l, folge_r, links="MO", rechts="TI"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)




import math

def tabelle(x, y, spalten, zeilen, size=32, kopf_fill=GELB, zh=78):
    """Tabelle als einzelne Zeilenbilder: zeilen = [(cue, [zelle, …])]; die erste Zeile ist der Kopf (fett, farbig)."""
    els = []
    for zi, (cue, zellen) in enumerate(zeilen):
        w = sum(spalten)
        im = Image.new("RGBA", (w + 4, zh + 4))
        d = ImageDraw.Draw(im)
        xx = 2
        for si, (bw, txt) in enumerate(zip(spalten, zellen)):
            fill = kopf_fill if zi == 0 else (HELL if si == 0 else WEISS)
            d.rectangle((xx, 2, xx + bw, zh + 2), fill=fill, outline=INK, width=4)
            stil = "ExtraBold" if zi == 0 or si == 0 else "Bold"
            fnt = F(stil, size)
            assert fnt.getlength(glyphen(txt)) <= bw - 24, f"Tabellenzelle zu breit: {txt}"
            d.text((xx + 14, zh / 2 + 2), txt, font=fnt, fill=INK, anchor="lm")
            xx += bw
        els.append(El(im, x, y + zi * zh, cue, "rise", 0.0, None, name="tabelle:" + "|".join(zellen)))
    return els, y + len(zeilen) * zh



# --- eigene Szenenbausteine Folge 200 ----------------------------------------------------------------------------------------
HGELB = (253, 240, 196, 255)                 # Fläche reines Wohngebiet im Plan
HORANGE = (252, 216, 190, 255)               # Fläche allgemeines Wohngebiet im Plan
BX, BY, BW, BH = 70, 130, 540, 660           # Bebauungsplan-Tafel in den Fallszenen
ZR = (BY + 90, BY + 360)                     # Zone Nord (WR): oben/unten
ZA = (BY + 380, BY + BH - 20)                # Zone Süd (WA)


def bplan(c):
    """Der Bebauungsplan der Siedlung als Planblatt (Grundform): weißes Blatt, Tuschekontur, Kopfzeile."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (BW - 3) * s, (BH - 3) * s), 16 * s, fill=WEISS, outline=INK, width=5 * s)
        dr.line((3 * s, 78 * s, (BW - 3) * s, 78 * s), fill=INK, width=4 * s)
        dr.text((BW / 2 * s, 42 * s), glyphen("Bebauungsplan 2022"), font=F("ExtraBold", 34 * s), fill=INK, anchor="mm")
    return hart(El(_flaeche(BW, BH, zz), BX, BY, c, "cut", 0.0, None, name="bplan"))


def zone(c, oben, unten, fill, zeile1, zeile2, anim="pop", bis=None):
    """Baugebietsfläche im Plan mit Himmelsrichtung und Gebietsbezeichnung."""
    w, h = BW - 40, unten - oben
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 12 * s, fill=fill, outline=INK, width=4 * s)
        dr.text((20 * s, 18 * s), glyphen(zeile1), font=F("Bold", 28 * s), fill=TEXT)
        dr.text((20 * s, 58 * s), glyphen(zeile2), font=F("ExtraBold", 32 * s), fill=INK)
    assert F("ExtraBold", 32).getlength(zeile2) <= w - 40, zeile2
    return El(_flaeche(w, h, zz), BX + 20, oben, c, anim, 0.0, bis, name="zone:" + zeile2)


def plan_grund(c):
    """Planblatt mit beiden Gebieten und den Häusern der Siedlung (für die Rückkehr in Szene K)."""
    return [bplan(c), hart(zone(c, *ZR, HGELB, "Norden", "WR · reines Wohngebiet", anim="cut")),
            hart(zone(c, *ZA, HORANGE, "Süden", "WA · allgemeines Wohngebiet", anim="cut")),
            hart(ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZR[1] - 18, 120, c, fuell=WEISS, anim="cut")),
            hart(ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZA[1] - 18, 120, c, fuell=WEISS, anim="cut"))]


KITA_X, LADEN_X = 900, 900                   # Kita-Haus bzw. Ladenlokal in den Fallszenen
KIND = 0.58                                  # Kinder (um 5): Anteil der Erwachsenenhöhe
KH = int(FHA * KIND)


def kinder(cue, bis=None, x1=1190, x2=1305):
    """Zwei Kinder aus der Siedlung (Open Peeps, kleiner skaliert; sprechen nicht, ohne Namen)."""
    return [peep_voll("KA_froh", x1, BODEN_Y, KH, cue, anim="pop", bis=bis),
            peep_voll("KB_froh", x2, BODEN_Y, KH - 12, cue, anim="pop", d=0.15, bis=bis)]


# ===========================================================================================================================
# A1 Fall: die neue Siedlung – der Bebauungsplan, die Kita im Norden
# ===========================================================================================================================
MOX = 1560
folie([(NULL, "Fall · Die neue Siedlung"), ("wr", "Fall · Norden: reines Wohngebiet"),
       ("wa", "Fall · Süden: allgemeines Wohngebiet"), ("kita", "Fall · Die Kita von Frau Möhring"),
       ("mo1", "Fall · 2 Gruppen, Kinder aus der Siedlung")], [
    boden(NULL),
    bplan(NULL),
    hart(pl("Neue Siedlung", 70, 30, NULL, fill=GRUEN, size=38)),
    hart(ficon("fluent-emoji-high-contrast", "houses", 1150, BODEN_Y, 260, NULL, fuell=WEISS, anim="cut", bis="kita")),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 1700, BODEN_Y, 170, NULL, fuell=GRUEN, anim="cut", bis="kita")),
    zone("wr", *ZR, HGELB, "Norden", "WR · reines Wohngebiet"),
    ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZR[1] - 18, 120, beim("wr", "reines"), fuell=WEISS),
    zone("wa", *ZA, HORANGE, "Süden", "WA · allgemeines Wohngebiet"),
    ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZA[1] - 18, 120, beim("wa", "allgemeines"), fuell=WEISS),
    ficon("fluent-emoji-high-contrast", "teddy-bear", BX + 400, ZR[1] - 22, 90, beim("kita", "Kita"), fuell=GELB),
    ficon("ph", "house-line", KITA_X, BODEN_Y, 300, "kita", fuell=GELB),
    pl("Kita", KITA_X, 540, beim("kita", "Kita"), fill=WEISS, size=34, anker="m"),
    ficon("fluent-emoji-high-contrast", "playground-slide", 1080, BODEN_Y, 120, beim("kita", "Kita"), fuell=ROT),
    *fig("MO", MOX, BODEN_Y, FHA, [(beim("kita", "Frau"), "froh")], erst="pop", bis="mo1"),
    ns(NAME["MO"], MOX, BODEN_Y, beim("kita", "Frau"), NFARBE["MO"], d=0.1),
    *redet("MO_redet", MOX, BODEN_Y, FHA, "mo1", "studio"),
    blase("sprech", 900, 260, "mo1", 1170, 240, inhalt=["2 Gruppen, 30 Plätze, und alle Kinder", "kommen hier aus der Siedlung."],
          textsize=34, figur=("MO_redet", MOX, BODEN_Y, FHA), bis="studio"),
    pl("2 Gruppen · 30 Plätze", KITA_X, 460, beim("mo1", "dreißig"), fill=GELB, size=30, anker="m"),
    *kinder(beim("mo1", "Kinder")),
    pl("Kinder aus der Siedlung", 1250, 560, beim("mo1", "Siedlung"), fill=WEISS, size=28, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: das Ladenlokal im Süden – Herr Tiemann (Ladenglocke) und die Fragen
# ===========================================================================================================================
TIX = 1560
folie([("studio", "Fall · Süden: das Ladenlokal von Herrn Tiemann"), ("ti1", "Fall · Herr Tiemann erklärt sein Studio"),
       ("frage", "Fall · Kita ins reine Wohngebiet?"), ("frage2", "Fall · Studio ins allgemeine Wohngebiet?")], [
    boden("studio"),
    *plan_grund("studio"),
    hart(ficon("fluent-emoji-high-contrast", "teddy-bear", BX + 400, ZR[1] - 22, 90, "studio", fuell=GELB, anim="cut")),
    ficon("tabler", "building-store", BX + 400, ZA[1] - 22, 100, beim("studio", "Ladenlokal"), fuell=BLAU),
    hart(pl("Süden: allgemeines Wohngebiet", 70, 30, "studio", fill=ORANGE, size=38)),
    ficon("tabler", "building-store", LADEN_X, BODEN_Y, 330, beim("studio", "Ladenlokal"), fuell=BLAU),
    pl("Tattoo-Studio", LADEN_X, 520, beim("studio", "Tattoo"), fill=WEISS, size=34, anker="m"),
    szene(fig("TI", TIX, BODEN_Y, FHA, [(beim("studio", "Herr"), "froh")], erst="pop", bis="ti1")[0], "200tuerglocke*", 1.0, 0.0),
    ns(NAME["TI"], TIX, BODEN_Y, beim("studio", "Herr"), NFARBE["TI"], d=0.1),
    *redet("TI_redet", TIX, BODEN_Y, FHA, "ti1", "frage"),
    blase("sprech", 960, 300, "ti1", 1150, 230, inhalt=["Ich arbeite nur nach Termin, und", "nach draußen dringt kein Lärm.",
                                                     "Meine Kundschaft kommt aus der ganzen Stadt."],
          textsize=32, figur=("TI_redet", TIX, BODEN_Y, FHA), bis="frage"),
    ficon("tabler", "calendar", 1150, BODEN_Y, 90, beim("ti1", "Termin"), fuell=WEISS),
    ficon("tabler", "volume-off", 1260, BODEN_Y, 80, beim("ti1", "Lärm"), fuell=WEISS),
    ficon("tabler", "map-2", 1370, BODEN_Y, 80, beim("ti1", "Stadt"), fuell=GRUEN),
    *fig("TI", TIX, BODEN_Y, FHA, [("frage", "skeptisch")], erst="cut"),
    pl("Kita ins reine Wohngebiet?", 660, 130, "frage", fill=HGELB, size=36),
    ring(BX + 400, ZR[1] - 65, 75, 60, "frage", farbe=ORANGE, breite=7),
    pl("Studio ins allgemeine Wohngebiet?", 660, 215, "frage2", fill=HORANGE, size=36),
    ring(BX + 400, ZA[1] - 65, 75, 60, "frage2", farbe=ORANGE, breite=7),
])
