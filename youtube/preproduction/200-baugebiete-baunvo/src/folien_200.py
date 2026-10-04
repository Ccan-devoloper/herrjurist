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
BX, BY, BW, BH = 70, 130, 560, 660           # Bebauungsplan-Tafel in den Fallszenen
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
        dr.text((20 * s, 58 * s), glyphen(zeile2), font=F("ExtraBold", 30 * s), fill=INK)
    assert F("ExtraBold", 30).getlength(zeile2) <= w - 40, zeile2
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
    hart(ficon("fluent-emoji-high-contrast", "houses", 1150, BODEN_Y, 260, NULL, fuell=WEISS, anim="cut", bis=beim("kita", "Einfamilienhaus"))),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 1700, BODEN_Y, 170, NULL, fuell=GRUEN, anim="cut", bis=beim("kita", "Frau"))),
    hart(zone(NULL, *ZR, (242, 242, 238, 255), "Norden", "", anim="cut")),
    hart(zone(NULL, *ZA, (242, 242, 238, 255), "Süden", "", anim="cut")),
    zone("wr", *ZR, HGELB, "Norden", "WR · reines Wohngebiet"),
    ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZR[1] - 18, 120, beim("wr", "reines"), fuell=WEISS),
    zone("wa", *ZA, HORANGE, "Süden", "WA · allgemeines Wohngebiet"),
    ficon("fluent-emoji-high-contrast", "houses", BX + 150, ZA[1] - 18, 120, beim("wa", "allgemeines"), fuell=WEISS),
    ficon("fluent-emoji-high-contrast", "teddy-bear", BX + 400, ZR[1] - 22, 90, beim("kita", "Kita"), fuell=GELB),
    ficon("ph", "house-line", KITA_X, BODEN_Y, 300, beim("kita", "Einfamilienhaus"), fuell=GELB),
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
    pl("Kita ins reine Wohngebiet?", 680, 130, "frage", fill=HGELB, size=36),
    ring(BX + 400, ZR[1] - 65, 75, 60, "frage", farbe=ORANGE, breite=7),
    pl("Studio ins allgemeine Wohngebiet?", 680, 215, "frage2", fill=HORANGE, size=36),
    ring(BX + 400, ZA[1] - 65, 75, 60, "frage2", farbe=ORANGE, breite=7),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_200(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_200("sv", [
    "Ein qualifizierter Bebauungsplan der Gemeinde aus dem Jahr 2022 setzt für eine neue Siedlung im Norden ein reines "
    "Wohngebiet und im Süden ein allgemeines Wohngebiet fest. Die Erschließung ist gesichert; die übrigen Festsetzungen "
    "halten beide Vorhaben ein.",
    "Frau Möhring will im Norden in einem Einfamilienhaus eine Kita mit 2 Gruppen und 30 Plätzen eröffnen. Alle Kinder "
    "kommen aus der Siedlung.",
    "Herr Tiemann mietet im Süden ein kleines Ladenlokal für sein Tattoo-Studio. Er arbeitet nur nach Termin, nach draußen "
    "dringt kein Lärm. Seine Kundschaft kommt aus der ganzen Stadt.",
], "Sind die Kita und das Studio nach der Art der baulichen Nutzung zulässig?")

# ===========================================================================================================================
# C § 30 Abs. 1 BauGB (Wortlaut)
# ===========================================================================================================================
PQ = "§ 30 Abs. 1 BauGB"
W30 = ("„(1) Im Geltungsbereich eines Bebauungsplans, der allein oder gemeinsam mit sonstigen baurechtlichen Vorschriften "
       "mindestens Festsetzungen über die Art und das Maß der baulichen Nutzung, die überbaubaren Grundstücksflächen und die "
       "örtlichen Verkehrsflächen enthält, ist ein Vorhaben zulässig, wenn es diesen Festsetzungen nicht widerspricht und "
       "die Erschließung gesichert ist.“")
w30, w30_y = wortlaut(80, 165, 1100, W30, "§ 30 Abs. 1 BauGB", "p30", marken=[
    ("nicht widerspricht", beim("p30w", "widerspricht")), ("Erschließung gesichert", beim("p30w", "Erschließung")),
    ("die Art und das Maß", beim("quali", "Art")), ("überbaubaren", beim("quali", "überbaubaren")),
    ("örtlichen Verkehrsflächen", beim("quali", "örtlichen"))], size=30)
folie([("p30", f"{PQ} · der Ausgangspunkt"), ("p30w", f"{PQ} › nicht widersprechen, Erschließung"),
       ("quali", f"{PQ} › qualifizierter Bebauungsplan"), ("hier", f"{PQ} › qualifiziert (+), Erschließung (+)"),
       ("art", f"{PQ} › offen: Art der baulichen Nutzung"), ("v188", f"{PQ} › Genehmigungspflicht: eigenes Video")], rechts_frei([
    *tafel("p30", "Ausgangspunkt: § 30 Abs. 1 BauGB"),
    *w30,
    *okz("qualifizierter Plan, Erschließung gesichert", w30_y + 25, "hier", "Bold", 32, x=160),
    blk(110, w30_y + 90, 1040, 76, GELB, "art", [("offen: die Art der baulichen Nutzung", "ExtraBold", 34, INK)]),
    zit("Genehmigungspflicht und Verfahren: Video „Baugenehmigung Schema“", 110, w30_y + 190, "v188", size=28),
    *requisit([("p30", ("tabler", "map", 100, WEISS), "Bebauungsplan", WEISS),
               ("hier", ("tabler", "circle-check", 100, HELLGRUEN), "qualifiziert", HELLGRUEN),
               ("art", ("tabler", "building-community", 110, GELB), "Art der Nutzung?", GELB)]),
    *zwei([("p30", "ruhig"), ("art", "denkt")], [("p30", "ruhig"), ("art", "skeptisch")]),
]))
assert w30_y + 230 <= 890, w30_y

# ===========================================================================================================================
# D Baugebiete: § 1 Abs. 2, 3 BauNVO (Tabelle)
# ===========================================================================================================================
PT = "Baugebiete"
tab, tab_y = tabelle(110, 235, [150, 470, 220], [
    ("p12", ["", "Baugebiet", "BauNVO"]),
    ("twr", ["WR", "reines Wohngebiet", "§ 3"]),
    ("twa", ["WA", "allgemeines Wohngebiet", "§ 4"]),
    ("tmi", ["MI", "Mischgebiet", "§ 6"]),
    ("tmu", ["MU", "urbanes Gebiet", "§ 6a"]),
    ("tge", ["GE", "Gewerbegebiet", "§ 8"]),
    ("tgi", ["GI", "Industriegebiet", "§ 9"])], zh=62)
folie([("bng", f"{PT} · die Baunutzungsverordnung"), ("p12", f"{PT} › § 1 Abs. 2 BauNVO: 12 Baugebiete"),
       ("twr", f"{PT} › reines Wohngebiet, § 3"), ("twa", f"{PT} › allgemeines Wohngebiet, § 4"),
       ("tmi", f"{PT} › Mischgebiet, § 6"), ("tmu", f"{PT} › urbanes Gebiet, § 6a"), ("tge", f"{PT} › Gewerbegebiet, § 8"),
       ("tgi", f"{PT} › Industriegebiet, § 9"), ("p13", f"{PT} › § 1 Abs. 3 S. 2 BauNVO: Teil des Plans")], rechts_frei([
    *tafel("bng", "Die Baugebiete der BauNVO"),
    z("§ 1 Abs. 2 BauNVO: 12 Baugebiete, z. B.", 110, 180, "p12", "Bold", 34),
    *tab,
    blk(110, tab_y + 20, 1040, 110, HELLGRUEN, "p13", [("Festsetzung im Plan: §§ 2 bis 14 BauNVO", "ExtraBold", 32, INK),
                                                     ("werden Bestandteil des Bebauungsplans", "ExtraBold", 32, INK)]),
    zit("§ 1 Abs. 3 S. 2 BauNVO", 110, tab_y + 140, "p13"),
    *requisit([("bng", ("tabler", "book", 100, WEISS), "BauNVO", WEISS),
               ("p12", ("tabler", "table", 100, WEISS), "12 Baugebiete", WEISS),
               ("p13", ("tabler", "map", 100, HELLGRUEN), "Teil des Plans", HELLGRUEN)]),
    *allein("TI", [("bng", "ruhig"), ("tmu", "skeptisch"), ("p13", "froh")]),
]))
assert tab_y + 180 <= 890, tab_y

# ===========================================================================================================================
# E Aufbau der §§ 2–9 BauNVO, § 31 Abs. 1 BauGB (Wortlaut), Gebietsverträglichkeit
# ===========================================================================================================================
PA = "Aufbau §§ 2–9 BauNVO"
W31 = ("„(1) Von den Festsetzungen des Bebauungsplans können solche Ausnahmen zugelassen werden, die in dem "
       "Bebauungsplan nach Art und Umfang ausdrücklich vorgesehen sind.“")
w31, w31_y = wortlaut(80, 425, 1100, W31, "§ 31 Abs. 1 BauGB", "p31", marken=[
    ("können", beim("p31", "können")), ("ausdrücklich vorgesehen", beim("p31", "ausdrücklich"))], size=30)
folie([("aufbau", f"{PA} · immer gleich gebaut"), ("abs1", f"{PA} › Abs. 1: Zweck"),
       ("abs2", f"{PA} › Abs. 2: allgemein zulässig"), ("abs3", f"{PA} › Abs. 3: ausnahmsweise"),
       ("p31", f"{PA} › Ausnahme, § 31 Abs. 1 BauGB"), ("erm", f"{PA} › Ermessen der Behörde"),
       ("gv", f"{PA} › ungeschrieben: Gebietsverträglichkeit")], rechts_frei([
    *tafel("aufbau", "Aufbau der §§ 2 bis 9 BauNVO"),
    blk(110, 175, 1040, 66, WEISS, "abs1", [("Abs. 1: Zweck des Gebiets", "ExtraBold", 32, INK)]),
    blk(110, 256, 1040, 66, GRUEN, "abs2", [("Abs. 2: allgemein zulässig", "ExtraBold", 32, INK)]),
    blk(110, 337, 1040, 66, GELB, "abs3", [("Abs. 3: ausnahmsweise zulassungsfähig", "ExtraBold", 32, INK)]),
    *w31,
    z("Entscheidung nach Ermessen der Behörde", 110, w31_y + 18, "erm", "Bold", 32),
    blk(110, w31_y + 75, 1040, 70, LILA, "gv", [("ungeschrieben: Gebietsverträglichkeit", "ExtraBold", 32, INK)]),
    zit("BVerwG, Beschl. v. 28.2.2008 – 4 B 60.07, Rn. 5, 11", 110, w31_y + 155, "gv"),
    *requisit([("aufbau", ("tabler", "list-numbers", 100, WEISS), "Abs. 1 · 2 · 3", WEISS),
               ("p31", ("tabler", "file-certificate", 100, GELB), "Ausnahme", GELB),
               ("erm", ("tabler", "scale", 100, WEISS), "Ermessen", WEISS),
               ("gv", ("tabler", "home-check", 100, LILA), "Gebietscharakter", LILA)]),
    *zwei([("aufbau", "ruhig"), ("abs3", "denkt"), ("gv", "froh")], [("aufbau", "skeptisch"), ("p31", "ruhig")]),
]))
assert w31_y + 190 <= 890, w31_y

# ===========================================================================================================================
# F Kita im reinen Wohngebiet: § 3 Abs. 1, 2 BauNVO (Wortlaut), Gegenfall große Kita
# ===========================================================================================================================
PK = "Kita im reinen Wohngebiet"
W3 = ("„(1) Reine Wohngebiete dienen dem Wohnen. (2) Zulässig sind 1. Wohngebäude, 2. Anlagen zur Kinderbetreuung, die den "
      "Bedürfnissen der Bewohner des Gebiets dienen.“")
w3, w3_y = wortlaut(80, 165, 1100, W3, "§ 3 Abs. 1, 2 BauNVO", "kita1", marken=[
    ("dienen dem Wohnen", beim("p3a", "Wohnen")), ("Anlagen zur Kinderbetreuung", beim("p3b", "Kinderbetreuung")),
    ("Bedürfnissen", beim("p3b", "Bedürfnissen")), ("Bewohner des Gebiets", beim("p3b", "Bewohner"))], size=30)
KX1, KX2, MOT = 1700, 1810, 1440             # Kinder und Frau Möhring neben der Tafel
folie([("kita1", f"{PK} · § 3 BauNVO"), ("p3a", f"{PK} › Abs. 1: dient dem Wohnen"),
       ("p3b", f"{PK} › Abs. 2 Nr. 2: Kinderbetreuung für die Bewohner"), ("sub3", f"{PK} › Kinder aus der Siedlung (+)"),
       ("gv3", f"{PK} › gebietsverträglich (+)"), ("gross", f"{PK} › Gegenfall: große Kita, Abs. 3 Nr. 2")], rechts_frei([
    *tafel("kita1", "Kita im reinen Wohngebiet: § 3 BauNVO"),
    *w3,
    *okz("Kinder aus der Siedlung: dient den Bewohnern", w3_y + 25, "sub3", "Bold", 32, x=160),
    *okz("2 Gruppen: stört den Gebietscharakter nicht", w3_y + 80, "gv3", "Bold", 32, x=160),
    blk(110, w3_y + 150, 1040, 120, HELLROT, "gross", [("Gegenfall: große Kita für die ganze Stadt", "ExtraBold", 32, INK),
                                                    ("nur ausnahmsweise: soziale Zwecke, Abs. 3 Nr. 2", "Bold", 32, INK)]),
    *requisit([("kita1", ("ph", "house-line", 110, GELB), "Kita", GELB),
               ("sub3", ("fluent-emoji-high-contrast", "teddy-bear", 90, GELB), "für die Siedlung", HELLGRUEN),
               ("gross", ("tabler", "building-community", 120, HELLROT), "Kita für die ganze Stadt?", HELLROT)]),
    *stehend("MO", MOT, [("kita1", "ruhig"), ("sub3", "froh"), ("gross", "denkt")]),
    *kinder(beim("sub3", "Kinder"), x1=KX1, x2=KX2),
]))
assert w3_y + 290 <= 890, w3_y

# ===========================================================================================================================
# G Kinderlärm: § 22 Abs. 1a BImSchG (Wortlaut), Ergebnis Kita
# ===========================================================================================================================
PL = "Kinderlärm"
W22 = ("„(1a) Geräuscheinwirkungen, die von Kindertageseinrichtungen, Kinderspielplätzen und ähnlichen Einrichtungen wie "
       "beispielsweise Ballspielplätzen durch Kinder hervorgerufen werden, sind im Regelfall keine schädliche "
       "Umwelteinwirkung. …“")
w22, w22_y = wortlaut(80, 165, 1100, W22, "§ 22 Abs. 1a S. 1 BImSchG", "p22", marken=[
    ("Kindertageseinrichtungen,", beim("p22", "Kindertageseinrichtungen")), ("im Regelfall keine", beim("p22", "Regelfall")),
    ("schädliche Umwelteinwirkung", beim("p22", "schädliche"))], size=30)
folie([("laerm", f"{PL} · ein Problem?"), ("p22", f"{PL} › § 22 Abs. 1a BImSchG: im Regelfall keine schädliche Umwelteinwirkung"),
       ("kerg", "Kita › allgemein zulässig (+)")], rechts_frei([
    *tafel("laerm", "Und der Kinderlärm?"),
    *w22,
    blk(110, w22_y + 40, 1040, 90, GRUEN, "kerg", [("Ergebnis: Die Kita ist allgemein zulässig.", "ExtraBold", 36, INK)]),
    bis_(ok(150, w22_y + 85, "kerg", gr=24), None),
    *requisit([("laerm", ("tabler", "volume", 100, WEISS), "Kinderlärm?", WEISS),
               ("p22", ("tabler", "volume", 100, HELLGRUEN), "im Regelfall hinzunehmen", HELLGRUEN),
               ("kerg", ("tabler", "circle-check", 100, HELLGRUEN), "Kita zulässig", HELLGRUEN)]),
    *stehend("MO", MOT, [("laerm", "sorge"), ("p22", "ruhig"), ("kerg", "stolz")]),
    *kinder("laerm", x1=KX1, x2=KX2),
]))
assert w22_y + 150 <= 890, w22_y

# ===========================================================================================================================
# H Tattoo-Studio im allgemeinen Wohngebiet: § 4 Abs. 1, 2 Nr. 2 BauNVO (Wortlaut), Gebietsversorgung
# ===========================================================================================================================
PS4 = "Studio im allgemeinen Wohngebiet"
W4 = ("„(1) Allgemeine Wohngebiete dienen vorwiegend dem Wohnen. (2) Zulässig sind … 2. die der Versorgung des Gebiets "
      "dienenden Läden, Schank- und Speisewirtschaften sowie nicht störenden Handwerksbetriebe, …“")
w4, w4_y = wortlaut(80, 165, 1100, W4, "§ 4 Abs. 1, 2 BauNVO", "stu1", marken=[
    ("vorwiegend dem Wohnen", beim("p4a", "vorwiegend")), ("der Versorgung des Gebiets", beim("p4b", "Versorgung")),
    ("nicht störenden Handwerksbetriebe", beim("p4b", "Handwerksbetriebe"))], size=30)
folie([("stu1", f"{PS4} · § 4 BauNVO"), ("p4a", f"{PS4} › Abs. 1: vorwiegend Wohnen"),
       ("p4b", f"{PS4} › Abs. 2 Nr. 2: gebietsversorgendes Handwerk?"), ("hw", f"{PS4} › Handwerk? kann offenbleiben"),
       ("vers", f"{PS4} › Versorgung des Gebiets: funktionale Zuordnung"), ("stadt", f"{PS4} › Kundschaft aus der ganzen Stadt"),
       ("nein2", f"{PS4} › Abs. 2 Nr. 2 (−)")], rechts_frei([
    *tafel("stu1", "Studio im allgemeinen Wohngebiet: § 4"),
    *w4,
    z("Handwerk? kann offenbleiben", 110, w4_y + 22, "hw", "Bold", 32),
    z("Versorgung des Gebiets = funktional dem Wohngebiet zuzuordnen", 110, w4_y + 77, "vers", "Bold", 30),
    zit("BVerwG, Urt. v. 20.3.2019 – 4 C 5.18, Rn. 16 (zur Gaststätte)", 110, w4_y + 122, "vers"),
    *neinz("Kundschaft aus der ganzen Stadt", w4_y + 175, "stadt", "Bold", 32, x=160),
    blk(110, w4_y + 240, 1040, 76, HELLROT, "nein2", [("§ 4 Abs. 2 Nr. 2 BauNVO (−)", "ExtraBold", 34, INK)]),
    *requisit([("stu1", ("tabler", "building-store", 110, BLAU), "Tattoo-Studio", BLAU),
               ("p4b", ("tabler", "tools", 100, WEISS), "Handwerk?", WEISS),
               ("stadt", ("tabler", "map-2", 100, HELLROT), "ganze Stadt", HELLROT)]),
    *allein("TI", [("stu1", "ruhig"), ("hw", "skeptisch"), ("nein2", "sorge")]),
]))
assert w4_y + 330 <= 890, w4_y

# ===========================================================================================================================
# I Ausnahme: § 4 Abs. 3 Nr. 2 BauNVO (Wortlaut), § 31 Abs. 1 BauGB, Regel-Ausnahme-Verhältnis, § 246e BauGB
# ===========================================================================================================================
PX3 = "Studio › Ausnahme"
W43 = "„(3) Ausnahmsweise können zugelassen werden … 2. sonstige nicht störende Gewerbebetriebe, …“"
w43, w43_y = wortlaut(80, 165, 1100, W43, "§ 4 Abs. 3 Nr. 2 BauNVO", "p4c", marken=[
    ("Ausnahmsweise", beim("p4c", "ausnahmsweise")), ("sonstige nicht", beim("p4c", "Sonstige")), ("störende Gewerbebetriebe", beim("p4c", "Gewerbebetriebe"))],
    size=30)
folie([("p4c", f"{PX3}: § 4 Abs. 3 Nr. 2 BauNVO"), ("ruhig", f"{PX3}: nicht störend (+)"),
       ("aus", f"{PX3} nach § 31 Abs. 1 BauGB möglich"), ("regel", f"{PX3}: Ermessen, Ausnahme bleibt Ausnahme"),
       ("turbo", f"{PX3}: § 246e BauGB hilft nicht")], rechts_frei([
    *tafel("p4c", "Bleibt die Ausnahme: § 4 Abs. 3"),
    *w43,
    *okz("klein, nur nach Termin, kein Lärm: nicht störend", w43_y + 25, "ruhig", "Bold", 32, x=160),
    blk(110, w43_y + 90, 1040, 76, GELB, "aus", [("Ausnahme nach § 31 Abs. 1 BauGB möglich", "ExtraBold", 34, INK)]),
    z("Ermessen: Die Ausnahme muss Ausnahme bleiben.", 110, w43_y + 195, "regel", "Bold", 32),
    zit("BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 17", 110, w43_y + 242, "regel"),
    *neinz("„Bau-Turbo“, § 246e BauGB: nur für den Wohnungsbau", w43_y + 305, "turbo", "Bold", 32, x=160),
    *requisit([("p4c", ("tabler", "building-store", 110, BLAU), "sonstiger Gewerbebetrieb", BLAU),
               ("ruhig", ("tabler", "calendar", 100, HELLGRUEN), "nur nach Termin", HELLGRUEN),
               ("aus", ("tabler", "file-certificate", 100, GELB), "Ausnahme", GELB),
               ("turbo", ("tabler", "home", 100, HELLROT), "nur Wohnungsbau", HELLROT)]),
    *allein("TI", [("p4c", "ruhig"), ("ruhig", "froh"), ("regel", "ernst"), ("turbo", "skeptisch")]),
]))
assert w43_y + 350 <= 890, w43_y

# ===========================================================================================================================
# J § 15 Abs. 1 BauNVO (Wortlaut): Einzelfall; Verweis Nachbarklage (Folge 113)
# ===========================================================================================================================
P15 = "§ 15 Abs. 1 BauNVO"
W15 = ("„(1) Die in den §§ 2 bis 14 aufgeführten baulichen und sonstigen Anlagen sind im Einzelfall unzulässig, wenn sie "
       "nach Anzahl, Lage, Umfang oder Zweckbestimmung der Eigenart des Baugebiets widersprechen. Sie sind auch unzulässig, "
       "wenn von ihnen Belästigungen oder Störungen ausgehen können, die nach der Eigenart des Baugebiets im Baugebiet "
       "selbst oder in dessen Umgebung unzumutbar sind, …“")
w15, w15_y = wortlaut(80, 165, 1100, W15, "§ 15 Abs. 1 BauNVO", "p15", marken=[
    ("im Einzelfall unzulässig,", beim("p15w", "Einzelfall")), ("Anzahl,", beim("p15w", "Anzahl")),
    ("unzumutbar", beim("p15w", "unzumutbar"))], size=30)
folie([("p15", f"{P15} · der Einzelfall"), ("p15w", f"{P15} › Eigenart, unzumutbare Störung"),
       ("h15", f"{P15} › Kita und Studio: nichts ersichtlich"), ("v113", f"{P15} › Nachbarn: Video „Nachbarklage“")], rechts_frei([
    *tafel("p15", "Zuletzt: § 15 Abs. 1 BauNVO"),
    *w15,
    *okz("Kita und Studio: nichts ersichtlich", w15_y + 25, "h15", "Bold", 32, x=160),
    zit("Gebietserhaltungsanspruch der Nachbarn: Video „Baurechtliche Nachbarklage“", 110, w15_y + 90, "v113", size=28),
    *requisit([("p15", ("tabler", "zoom-check", 100, WEISS), "Einzelfall", WEISS),
               ("v113", ("tabler", "users", 100, WEISS), "Nachbarn", WEISS)]),
    *zwei([("p15", "ruhig"), ("h15", "froh")], [("p15", "skeptisch"), ("h15", "froh")]),
]))
assert w15_y + 130 <= 890, w15_y

# ===========================================================================================================================
# K Ergebnis: zurück zur Siedlung, Herr Tiemann (Blase)
# ===========================================================================================================================
MO3, TI3 = 900, 1560
folie([("erg", "Ergebnis › Kita: allgemein zulässig"), ("erg2", "Ergebnis › Studio: nur als Ausnahme"),
       ("ti2", "Ergebnis › Herr Tiemann beantragt die Ausnahme")], [
    boden("erg"),
    *plan_grund("erg"),
    hart(pl("Ergebnis", 70, 30, "erg", fill=PINK, size=38)),
    ficon("fluent-emoji-high-contrast", "teddy-bear", BX + 400, ZR[1] - 22, 90, "erg", fuell=GELB),
    bis_(ok(BX + 470, ZR[0] + 120, beim("erg", "allgemein"), gr=26), None),
    pl("Kita: allgemein zulässig", 680, 120, beim("erg", "allgemein"), fill=HELLGRUEN, size=36),
    ficon("tabler", "building-store", BX + 400, ZA[1] - 22, 100, "erg2", fuell=BLAU),
    pl("Studio: nur als Ausnahme", 680, 200, beim("erg2", "Ausnahme"), fill=GELB, size=36),
    *fig("MO", MO3, BODEN_Y, FHA, [("erg", "stolz_r")], erst="pop"),
    ns(NAME["MO"], MO3, BODEN_Y, "erg", NFARBE["MO"], d=0.1),
    *fig("TI", TI3, BODEN_Y, FHA, [("erg", "ruhig"), ("erg2", "skeptisch")], erst="pop", bis="ti2"),
    *redet("TI_redet2", TI3, BODEN_Y, FHA, "ti2", "sch"),
    ns(NAME["TI"], TI3, BODEN_Y, "erg", NFARBE["TI"], d=0.1),
    blase("sprech", 640, 200, "ti2", 1510, 300, inhalt=["Dann beantrage ich", "die Ausnahme gleich mit."], textsize=34,
          figur=("TI_redet2", TI3, BODEN_Y, FHA), bis="sch"),
])

# ===========================================================================================================================
# L Prüfschema: Zulässigkeit nach § 30 Abs. 1 BauGB (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. qualifizierter Bebauungsplan (§ 30 Abs. 1 BauGB)"),
          ("s2", 0, "2. Art der baulichen Nutzung"),
          ("s2a", 1, "a) Baugebiet bestimmen (§ 1 Abs. 2, 3 BauNVO)"),
          ("s2b", 1, "b) Katalog: allgemein zulässig nach Abs. 2"),
          ("s2c", 1, "c) sonst Ausnahme (Abs. 3, § 31 Abs. 1 BauGB) oder Befreiung (§ 31 Abs. 2 BauGB)"),
          ("s2d", 1, "d) Gebietsverträglichkeit"),
          ("s2e", 1, "e) Einzelfall: § 15 Abs. 1 BauNVO"),
          ("s3", 0, "3. übrige Festsetzungen, z. B. Maß der baulichen Nutzung"),
          ("s4", 0, "4. gesicherte Erschließung")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Zulässigkeit nach § 30 Abs. 1 BauGB"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (40, 36)[ebene], rechts=1820))
    y += {0: 86, 1: 74}[ebene]
assert y <= 960, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › 1. qualifizierter Bebauungsplan"), ("s2", "Prüfschema › 2. Art der Nutzung"),
       ("s2a", "Prüfschema › 2. a) Baugebiet"), ("s2b", "Prüfschema › 2. b) Katalog Abs. 2"),
       ("s2c", "Prüfschema › 2. c) Ausnahme oder Befreiung"), ("s2d", "Prüfschema › 2. d) Gebietsverträglichkeit"),
       ("s2e", "Prüfschema › 2. e) § 15 BauNVO"), ("s3", "Prüfschema › 3. übrige Festsetzungen"),
       ("s4", "Prüfschema › 4. Erschließung")], els_sch)

# ===========================================================================================================================
# M Klausurtipp (Lexi): die Reihenfolge bei der Art der Nutzung
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: immer dieselbe Reihenfolge", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Art der Nutzung prüfen:", 200, 200, "tipp", "Bold", 34),
         blk(130, 290, 1020, 76, WEISS, "k1", [("1. Gebiet bestimmen", "ExtraBold", 34, INK)]),
         blk(130, 386, 1020, 76, GRUEN, "k2", [("2. Katalog in Abs. 2", "ExtraBold", 34, INK)]),
         blk(130, 482, 1020, 76, GELB, "k3", [("3. Ausnahme oder Befreiung, § 31 BauGB", "ExtraBold", 34, INK)]),
         blk(130, 578, 1020, 76, BLAU, "k4", [("4. zuletzt § 15 BauNVO", "ExtraBold", 34, INK)]),
         z("Ältere Pläne: Welche BauNVO-Fassung gilt?", 130, 690, "k5", "Bold", 32),
         zit("Überleitungsvorschriften §§ 25 ff. BauNVO, z. B. § 25d, § 25e", 130, 740, "k5"),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · immer dieselbe Reihenfolge"), ("k1", "Klausurtipp › 1. Gebiet"), ("k2", "Klausurtipp › 2. Katalog"),
       ("k3", "Klausurtipp › 3. Ausnahme oder Befreiung"), ("k4", "Klausurtipp › 4. § 15 BauNVO"),
       ("k5", "Klausurtipp › Fassung der BauNVO")], els_k)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der ", 0), ("Bebauungsplan", "a"), (" wählt das Gebiet,", 0)]], 750, 290, 40, "merke",
                {"a": beim("merke", "Bebauungsplan")}),
    *markertext([[("die ", 0), ("BauNVO", "b"), (" liefert den Katalog.", 0)]], 750, 380, 40, "m2", {"b": beim("m2", "Baunutzungsverordnung")}),
    *markertext([[("Was dort nicht allgemein zulässig ist,", 0)],
                 [("braucht eine ", 0), ("Ausnahme oder Befreiung", "c"), (".", 0)]], 750, 500, 40, "m3",
                {"c": beim("m3", "Ausnahme")}),
    *markertext([[("Und ", 0), ("§ 15", "d"), (" prüft am Ende", 0)],
                 [("den Einzelfall.", 0)]], 750, 680, 40, "m4", {"d": beim("m4", "Paragraf")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
