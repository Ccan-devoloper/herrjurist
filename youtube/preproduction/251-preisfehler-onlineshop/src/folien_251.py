"""Folge 251 · Preisfehler Onlineshop: Muss der Händler liefern? (§ 119 BGB) · Serienstandard Open Peeps (Katzenkönig).
Beispielfall (angelehnt an BGH, Urt. v. 26.1.2005 – VIII ZR 79/04): Im Onlineshop von Frau Wetzel steht ein Fernseher für
49 € statt 499 €, weil die Software den eingegebenen Preis falsch übertragen hat. Herr Kübler bestellt am Montagabend, erhält
sofort eine automatische Eingangsbestätigung und am Dienstagmorgen die Mail „Ihr Auftrag wird jetzt von unserer
Versandabteilung bearbeitet.“ Am Dienstagmittag ficht Frau Wetzel telefonisch an. Danach: Anspruch § 433 Abs. 1 Satz 1,
I. Vertragsschluss (invitatio, Bestellung = Angebot, Wortlautkarte § 312i Abs. 1 Satz 1 Nr. 3, Wissenserklärung,
Annahme durch die 2. Mail), II. Anfechtung (Wortlautkarten § 119 Abs. 1 und § 120, BGH zum Datentransferfehler,
Fortwirken in der Annahme, Abgrenzung Kalkulationsirrtum, § 121, § 142 Abs. 1), Folge § 122 (Wortlautkarte),
Ergebnis, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 245 (gemeinsame Dateien unverändert); neu: tisch(), monitor(), mailkarte(), lager(), telefon(), okw().
Keine echten Shops oder Marken: Shopseite, Bildschirm und Mails aus Grundformen, ohne Namen oder Logo.
Handlungsgeräusch: Telefon (A2, Frau Wetzel ruft an); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_251/"

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
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (240, 236, 255, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_251/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205/229) ---------------------------------
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
NAME = {"KU": "Herr Kübler", "WE": "Frau Wetzel"}
NFARBE = {"KU": GRUEN, "WE": ROT}


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)



def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def fenster(x, y, w, h, cue):
    """Fenster mit Sprossen (Tageslicht)."""
    return [hart(feld(x, y, w, h, cue, fill=BLAUHELL, rand=5, rund=8, name="fenster")),
            hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")),
            hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2"))]


def tisch(x0, x1, cue, top=700):
    """Schreibtisch aus Grundformen: Platte und zwei Beine bis zum Boden."""
    return [hart(feld(x0, top, x1 - x0, 22, cue, fill=HOLZ, rand=4, rund=6, name="tischplatte")),
            hart(feld(x0 + 30, top + 22, 22, BODEN - top - 26, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="tischbein1")),
            hart(feld(x1 - 52, top + 22, 22, BODEN - top - 26, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="tischbein2"))]


def monitor(x0, y0, x1, y1, cue, top=700):
    """Bildschirm aus Grundformen (Rahmen, Anzeige, Fuß) auf dem Tisch; ohne Hersteller- oder Shopkennzeichen."""
    m = (x0 + x1) // 2
    return [hart(feld(x0, y0, x1 - x0, y1 - y0, cue, fill=INK, rand=4, rund=18, name="monitor")),
            hart(feld(x0 + 18, y0 + 18, x1 - x0 - 36, y1 - y0 - 36, cue, fill=WEISS, rand=2, rund=8, name="anzeige")),
            hart(feld(m - 40, y1, 80, top - y1 - 14, cue, fill=HELLGRAU, rand=4, rund=4, name="monitorhals")),
            hart(feld(m - 130, top - 16, 260, 16, cue, fill=HELLGRAU, rand=4, rund=6, name="monitorfuss"))]


def mailkarte(x, y, w, kopf, zeilen, cue, bis=None):
    """Automatische E-Mail im Posteingang: Umschlag, Kopfzeile, Text = gesprochener Inhalt (Ziffern statt Zahlwörtern)."""
    h = 70 + 38 * len(zeilen) + 14
    els = [bis_(feld(x, y, w, h, cue, fill=LILAHELL, rand=3, rund=14, anim="pop", name="mailkarte"), bis),
           bis_(ficon("tabler", "mail", x + 38, y + 56, 48, cue, fuell=WEISS), bis),
           bis_(z(kopf, x + 76, y + 16, cue, "ExtraBold", 26, rechts=x + w - 12), bis)]
    for i, t in enumerate(zeilen):
        els.append(bis_(z(t, x + 22, y + 68 + i * 38, cue, "Bold", 28, rechts=x + w - 14), bis))
    return els, y + h


# Zuhause bei Herrn Kübler (A1): Schreibtisch mit Bildschirm links, Fenster rechts, Herr Kübler davor
KUX = 1440
MON = (120, 90, 1080, 620)


def zuhause(cue):
    return [boden(cue), *fenster(1610, 140, 250, 220, cue), *tisch(90, 1110, cue), *monitor(*MON, cue)]


# ===========================================================================================================================
# A1 Fall: Herr Kübler bestellt den Fernseher für 49 € und bekommt zwei automatische E-Mails
# ===========================================================================================================================
mail1, m1y = mailkarte(605, 200, 435, "Automatische E-Mail", ["Vielen Dank, wir haben", "Ihre Bestellung erhalten."], "mail1")
mail2, m2y = mailkarte(605, m1y + 16, 435, "Zweite E-Mail", ["Ihr Auftrag wird jetzt von", "unserer Versandabteilung",
                                                              "bearbeitet."], "mail2")
assert m2y <= 598, m2y
folie([(NULL, "Fall · Bei Herrn Kübler zu Hause"), ("shop", "Fall · Fernseher für 49 € im Onlineshop"),
       ("bestellt", "Fall · Herr Kübler bestellt sofort"), ("mail1", "Fall · 1. Mail: Bestellung erhalten"),
       ("mail2", "Fall · 2. Mail: Auftrag wird bearbeitet")], [
    *zuhause(NULL),
    hart(pl("Bei Herrn Kübler zu Hause", 70, 22, NULL, fill=GELB, size=30)),
    hart(feld(140, 110, 920, 60, NULL, fill=BLAUHELL, rand=2, rund=8, name="kopfleiste")),
    hart(z("Onlineshop", 165, 118, NULL, "ExtraBold", 30, rechts=1040)),
    hart(linienzug([(585, 186), (585, 584)], NULL, breite=3, farbe=HELLGRAU)),
    ficon("tabler", "device-tv", 360, 380, 250, "shop", fuell=BLAUHELL),
    z("Fernseher", 175, 395, "shop", "Bold", 30, rechts=570),
    z("49 €", 175, 440, beim("shop", "neunundvierzig"), "ExtraBold", 56, farbe=DROT, rechts=570),
    pl("sonst 499 €", 360, 525, "sonst", fill=WEISS, size=28, anker="m"),
    bis_(ok(345, 470, "bestellt", gr=20), None), z("bestellt", 385, 452, "bestellt", "Bold", 32, rechts=570),
    pl("Montagabend", 500, 22, "bestellt", fill=WEISS, size=30, bis="mail2"),
    *mail1, *mail2,
    pl("Dienstagmorgen", 500, 22, "mail2", fill=WEISS, size=30),
    *fig("KU", KUX, BODEN, FH, [(NULL, "ruhig"), ("shop", "staunt"), ("bestellt", "strahlt"), ("mail1", "froh"),
                               ("mail2", "strahlt")], erst="cut"),
    hart(ns(NAME["KU"], KUX, BODEN, NULL, GRUEN)),
])


# ===========================================================================================================================
# A2 Im Lager von Frau Wetzel: 499 € eingegeben, 49 € im Shop – sie ruft an
# ===========================================================================================================================
WEX = 1380


def lager(cue):
    els = [boden(cue),
           hart(feld(90, 210, 18, BODEN - 214, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="regal1")),
           hart(feld(542, 210, 18, BODEN - 214, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="regal2"))]
    for i, y in enumerate((380, 600, 820)):
        els.append(hart(feld(90, y, 470, 18, cue, fill=HOLZ, rand=3, rund=4, name=f"brett{i}")))
        for j, x in enumerate((175, 325, 475)):
            els.append(ficon("tabler", "package", x, y, 120 if (i + j) % 2 else 105, cue, fuell=(232, 190, 140, 255), anim="cut"))
    return els + tisch(640, 1200, cue) + monitor(660, 230, 1180, 600, cue)


folie([("lager", "Fall · Dienstagmittag im Lager von Frau Wetzel"), ("fehler", "Fall · eingegeben 499 €, im Shop 49 €"),
       ("anruf", "Fall · Frau Wetzel ruft sofort an")], [
    *lager("lager"),
    hart(pl("Im Lager von Frau Wetzel", 70, 22, "lager", fill=GELB, size=30)),
    pl("Dienstagmittag", 520, 22, "lager", fill=WEISS, size=30),
    z("Bestellung: Fernseher", 700, 270, beim("lager", "Bestellung"), "Bold", 30, rechts=1150),
    z("eingegeben: 499 €", 700, 340, beim("fehler", "vierhundertneunundneunzig"), "ExtraBold", 36, rechts=1150),
    pfeil(800, 400, 800, 470, beim("fehler", "Software"), breite=8, kopf=24),
    ficon("tabler", "bug", 1060, 470, 80, beim("fehler", "Software"), fuell=HELLROT),
    z("im Shop: 49 €", 700, 490, beim("fehler", "Shop"), "ExtraBold", 36, farbe=DROT, rechts=1150),
    *fig("WE", WEX, BODEN, FH, [("lager", "tippt"), (beim("fehler", "Software"), "schreck"), ("anruf", "ernst")], erst="pop"),
    ficon("tabler", "keyboard", 900, 690, 150, "lager", fuell=WEISS, anim="cut"),
    ns(NAME["WE"], WEX, BODEN, "lager", ROT, d=0.1),
    szene(ficon("tabler", "device-mobile", WEX + 120, 560, 56, "anruf", fuell=WEISS), "251telefon*", 0.7, 0.1),
    pl("ruft sofort an", WEX, 330, beim("anruf", "ruft"), fill=WEISS, size=30, anker="m"),
])


# ===========================================================================================================================
# A3 Telefonat (geteiltes Bild): Frau Wetzel ficht an, Herr Kübler besteht auf Lieferung – die Frage
# ===========================================================================================================================
WT, KT = 520, 1440


def telefon(cue, oben=60):
    return [boden(cue), hart(linienzug([(960, oben), (960, BODEN)], cue, breite=6, farbe=INK)),
            ficon("tabler", "package", 180, BODEN, 130, cue, fuell=(232, 190, 140, 255), anim="cut"),
            ficon("tabler", "package", 330, BODEN, 110, cue, fuell=(232, 190, 140, 255), anim="cut"),
            *fenster(1630, 300, 230, 200, cue),
            ficon("tabler", "device-mobile", WT + 95, 540, 50, cue, fuell=WEISS, anim="cut"),
            ficon("tabler", "device-mobile", KT - 95, 540, 50, cue, fuell=WEISS, anim="cut")]


folie([("w1", "Fall · Frau Wetzel: „Ich fechte den Kauf an“"), ("k1", "Fall · Herr Kübler: „zwei Bestätigungen“"),
       ("frage", "Die Frage · Muss Frau Wetzel liefern?"), ("frage2", "Die Frage · Ist die 1. Mail eine Annahme?"),
       ("frage3", "Die Frage · Darf sie sich lösen?")], [
    *telefon("w1"),
    *redet("WE_redet_r", WT, BODEN, FH, "w1", "k1"),
    *fig("WE", WT, BODEN, FH, [("k1", "ernst_r"), ("frage", "ruhig_r")], erst="cut"),
    hart(ns(NAME["WE"], WT, BODEN, "w1", ROT)),
    *fig("KU", KT, BODEN, FH, [("w1", "sorge")], bis="k1", erst="cut"),
    *redet("KU_redet", KT, BODEN, FH, "k1", "frage"),
    *fig("KU", KT, BODEN, FH, [("frage", "denkt")], erst="cut"),
    hart(ns(NAME["KU"], KT, BODEN, "w1", GRUEN)),
    blase("sprech", 650, 230, "w1", 625, 210, inhalt=["Der Preis im Shop war ein", "Softwarefehler. Ich fechte den",
                                                    "Kauf an und liefere nicht."], textsize=31,
          figur=("WE_redet_r", WT, BODEN, FH), bis="frage"),
    blase("sprech", 650, 230, "k1", 1320, 210, inhalt=["Aber ich habe zwei", "Bestätigungen! Ich will den",
                                                     "Fernseher für 49 €."], textsize=31,
          figur=("KU_redet", KT, BODEN, FH), bis="frage"),
    pl("Muss Frau Wetzel liefern?", 70, 30, "frage", fill=PINK, size=34),
    pl("Ist schon die 1. Mail eine Annahme?", 70, 108, "frage2", fill=PINK, size=34),
    pl("Darf sie sich wegen des Fehlers vom Vertrag lösen?", 70, 186, "frage3", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_251(cue, absaetze, frage, size=35):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_251("sv", [
    "Im Onlineshop von Frau Wetzel kostet ein Fernseher plötzlich 49 € statt 499 €. Sie hatte 499 € in ihr System "
    "eingegeben; die Software hat den Preis unbemerkt falsch in den Shop übertragen.",
    "Am Montagabend bestellt Herr Kübler. Sofort kommt eine automatische E-Mail: „Vielen Dank, wir haben Ihre Bestellung "
    "erhalten.“ Am Dienstagmorgen folgt eine zweite: „Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.“",
    "Am Dienstagmittag bemerkt Frau Wetzel den Fehler, ruft Herrn Kübler sofort an und ficht den Kauf an. Er verlangt den "
    "Fernseher für 49 €.",
], "Muss Frau Wetzel liefern?")


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


def okw(text, y, cue, haken, stil="Bold", size=34, x=185, **k):
    """Tafelzeile zum Satzbeginn, Haken erst zur gesprochenen Bejahung (haken = Cue)."""
    return [ok(x - 45, y + 20, haken, gr=20), z(text, x, y, cue, stil, size, **k)]


# ===========================================================================================================================
# C Anspruch und Aufbau
# ===========================================================================================================================
PA = "Anspruch"
folie([("ansp", f"{PA} · § 433 Abs. 1 Satz 1 BGB: Lieferung"), ("aufbau", f"{PA} › Stufe 1: Kaufvertrag?"),
       ("aufbau2", f"{PA} › Stufe 2: Anfechtung?")], [
    *tafel("ansp", "Anspruch auf Lieferung"),
    z("Herr Kübler gegen Frau Wetzel", 110, 180, "ansp", "Bold", 36),
    z("Lieferung: Übergabe und Übereignung", 110, 245, beim("ansp", "Übergabe"), "Bold", 34),
    z("§ 433 Abs. 1 Satz 1 BGB", 110, 297, beim("ansp", "Paragraf"), "ExtraBold", 36),
    blk(110, 390, 1040, 100, GELB, beim("aufbau", "Ist"), [("Stufe 1: Ist ein Kaufvertrag zustande gekommen?", "ExtraBold", 32, INK)]),
    blk(110, 530, 1040, 100, HELLROT, "aufbau2", [("Stufe 2: Ist er durch Anfechtung weggefallen?", "ExtraBold", 32, INK)]),
    *requisit([("ansp", ("tabler", "device-tv", 150, BLAUHELL), "Fernseher", WEISS),
               ("aufbau", ("tabler", "list-check", 120, GELB), "zwei Stufen", GELB)], px=1560, pu=330, py=90),
    *paar("KU", [("ansp", "ruhig"), ("aufbau", "denkt")], "WE", [("ansp", "ruhig"), ("aufbau2", "ernst")]),
])

# ===========================================================================================================================
# D1 I. Vertragsschluss: Shopseite = invitatio, Bestellung = Angebot (VIII ZR 79/04 S. 5; X ZR 37/12 Rn. 14)
# ===========================================================================================================================
PI = "I. Vertragsschluss"
folie([("inv", f"{PI} · Shopseite: nur Einladung"), ("v014", f"{PI} › Folge „Angebot und Annahme“"),
       ("best", f"{PI} › Angebot: die Bestellung")], [
    *tafel("inv", "I. Vertragsschluss"),
    *neinz("Fernseher im Shop: noch kein Angebot", 180, "inv", "Bold", 36, kreuz=beim("inv", "kein")),
    z("nur Einladung, selbst eines abzugeben:", 185, 236, beim("inv", "Einladung"), "Bold", 34),
    z("invitatio ad offerendum", 185, 284, beim("inv", "Einladung"), "ExtraBold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, NJW 2005, 976;", 185, 336, beim("inv", "Einladung")),
    zit("BGH, Urt. v. 16.10.2012 – X ZR 37/12, Rn. 14", 185, 372, beim("inv", "Einladung")),
    blk(110, 440, 1040, 90, LILAHELL, "v014", [("mehr dazu: Folge „Angebot und Annahme“", "ExtraBold", 32, INK)]),
    *okz("Angebot: die Bestellung von Herrn Kübler", 590, beim("best", "Angebot"), "Bold", 34),
    *requisit([("inv", ("tabler", "browser", 130, WEISS), "Shopseite", WEISS),
               ("best", ("tabler", "shopping-cart", 130, GELB), "Bestellung", GELB)]),
    *stehend("KU", FX, [("inv", "ruhig"), ("best", "froh")]),
])

# ===========================================================================================================================
# D2 1. Mail: Eingangsbestätigung (Wortlautkarte § 312i Abs. 1 Satz 1 Nr. 3 BGB; X ZR 37/12 Rn. 19)
# ===========================================================================================================================
w312, w312_y = wortlaut(80, 170, 1100, "„(1) Bedient sich ein Unternehmer zum Zwecke des Abschlusses eines Vertrags über "
                                       "die Lieferung von Waren … (Vertrag im elektronischen Geschäftsverkehr), hat er dem "
                                       "Kunden … 3. den Zugang von dessen Bestellung unverzüglich auf elektronischem Wege zu "
                                       "bestätigen …“", "§ 312i Abs. 1 Satz 1 Nr. 3 BGB", "w312", size=31,
                        marken=[("Zugang von dessen", beim("w312", "Zugang")),
                                ("unverzüglich", beim("w312", "unverzüglich")),
                                ("elektronischem Wege", beim("w312", "elektronisch"))])
folie([("w312", f"{PI} › 1. Mail: Pflicht nach § 312i BGB"), ("wiss", f"{PI} › 1. Mail: nur Wissenserklärung"),
       ("ausl", f"{PI} › 1. Mail: Auslegung im Einzelfall"), ("erhalten", f"{PI} › 1. Mail: keine Annahme")], [
    *tafel("w312", "1. Mail: Eingangsbestätigung"),
    *w312,
    blk(110, w312_y + 20, 1040, 120, GELB, "wiss", [("in der Regel nur Wissenserklärung,", "ExtraBold", 32, INK),
                                                  ("keine Annahme", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 16.10.2012 – X ZR 37/12, Rn. 19", 110, w312_y + 152, beim("wiss", "Bundesgerichtshof")),
    z("Einzelfall: Auslegung aus Sicht des Empfängers", 110, w312_y + 200, "ausl", "Bold", 33),
    *neinz("„Wir haben Ihre Bestellung erhalten.“: nur Eingang", w312_y + 262, "erhalten", "Bold", 32,
           kreuz=beim("erhalten", "nur")),
    *requisit([("w312", ("tabler", "mail", 120, LILAHELL), "1. Mail", LILAHELL),
               ("wiss", ("tabler", "info-circle", 110, GELB), "Wissenserklärung", GELB),
               ("erhalten", ("tabler", "mail", 120, LILAHELL), "nur Eingang", WEISS)]),
    *stehend("KU", FX, [("w312", "ruhig"), ("wiss", "denkt"), ("erhalten", "ernst")]),
])
assert w312_y + 262 + 40 <= 895, w312_y

# ===========================================================================================================================
# D3 2. Mail: Annahme (VIII ZR 79/04 S. 5 f.; X ZR 37/12 Rn. 17, 19)
# ===========================================================================================================================
folie([("ann", f"{PI} › 2. Mail: kündigt Ausführung an"), ("konkl", f"{PI} › 2. Mail: Annahme"),
       ("auto", f"{PI} › automatisch, aber Erklärung von Frau Wetzel"), ("vertrag", f"{PI} › Kaufvertrag zu 49 €")], [
    *tafel("ann", "2. Mail: Annahme"),
    feld(110, 175, 1040, 130, "ann", fill=LILAHELL, rand=4, rund=16, anim="pop", name="mail2tafel"),
    ficon("tabler", "mail", 160, 262, 56, "ann", fuell=WEISS),
    z("„Ihr Auftrag wird jetzt von unserer", 215, 190, "ann", "Bold", 32),
    z("Versandabteilung bearbeitet.“", 215, 240, "ann", "Bold", 32),
    *okz("kündigt vorbehaltlose Ausführung an", 340, beim("ann", "vorbehaltlos"), "Bold", 34),
    *okz("= Annahme", 400, "konkl", "ExtraBold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 5 f.;", 185, 450, beim("konkl", "Bundesgerichtshof")),
    zit("BGH, Urt. v. 16.10.2012 – X ZR 37/12, Rn. 19", 185, 486, beim("konkl", "Bundesgerichtshof")),
    z("vom Computer verschickt:", 185, 550, "auto", "Bold", 34),
    *okw("trotzdem Erklärung von Frau Wetzel", 598, beim("auto", "Erklärung"), beim("auto", "Erklärung"), "Bold", 34),
    zit("BGH, Urt. v. 16.10.2012 – X ZR 37/12, Rn. 17", 185, 646, beim("auto", "Erklärung")),
    blk(110, 710, 1040, 90, HELLGRUEN, "vertrag", [("Kaufvertrag geschlossen: Fernseher für 49 €", "ExtraBold", 34, INK)]),
    *requisit([("ann", ("tabler", "mail-check", 120, LILAHELL), "2. Mail", LILAHELL),
               ("auto", ("tabler", "device-desktop", 130, WEISS), "automatisch", WEISS),
               ("vertrag", ("tabler", "file-text", 120, HELLGRUEN), "Kaufvertrag", HELLGRUEN)]),
    *stehend("KU", FX, [("ann", "ruhig"), ("konkl", "froh"), ("vertrag", "strahlt")]),
])

# ===========================================================================================================================
# E II. Anfechtung: § 119 Abs. 1 BGB (Wortlautkarte); Vertippen = Erklärungsirrtum (VIII ZR 79/04 S. 6 f.)
# ===========================================================================================================================
PII = "II. Anfechtung"
w119, w119_y = wortlaut(80, 170, 1100, "„(1) Wer bei der Abgabe einer Willenserklärung über deren Inhalt im Irrtum war oder "
                                       "eine Erklärung dieses Inhalts überhaupt nicht abgeben wollte, kann die Erklärung "
                                       "anfechten, wenn anzunehmen ist, dass er sie bei Kenntnis der Sachlage und bei "
                                       "verständiger Würdigung des Falles nicht abgegeben haben würde.“", "§ 119 Abs. 1 BGB",
                        "w119", size=31,
                        marken=[("anfechten", beim("w119", "anfechten")), ("über deren Inhalt", beim("w119", "Inhalt")),
                                ("überhaupt nicht abgeben", beim("w119", "überhaupt"))])
folie([("anf", f"{PII} · Anfechtungsgrund"), ("w119", f"{PII} › § 119 Abs. 1 BGB"),
       ("vertippt", f"{PII} › vertippt: Erklärungsirrtum"), ("hier", f"{PII} › hier: Fehler der Software")], [
    *tafel("anf", "II. Anfechtung: Anfechtungsgrund"),
    *w119,
    *okw("vertippt: Erklärungsirrtum, § 119 Abs. 1 Alt. 2 BGB", w119_y + 30, "vertippt",
         beim("vertippt", "Erklärungsirrtum"), "Bold", 34),
    zit("vgl. BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 7", 185, w119_y + 80, beim("vertippt", "Erklärungsirrtum")),
    *neinz("Frau Wetzel hat sich nicht vertippt:", w119_y + 145, "hier", "Bold", 34, kreuz=beim("hier", "nicht")),
    z("den Fehler machte die Software", 185, w119_y + 195, beim("hier", "Software"), "Bold", 34),
    *requisit([("anf", ("tabler", "help-circle", 110, WEISS), "Anfechtung?", WEISS),
               ("vertippt", ("tabler", "keyboard", 150, GELB), "vertippt", GELB),
               (beim("hier", "Software"), ("tabler", "bug", 110, HELLROT), "Software", HELLROT)]),
    *stehend("WE", FX, [("anf", "ruhig"), ("vertippt", "denkt"), ("hier", "sorge")]),
])
assert w119_y + 195 + 40 <= 895, w119_y

# ===========================================================================================================================
# F § 120 BGB (Wortlautkarte) und BGH VIII ZR 79/04 S. 7: Datentransferfehler = Erklärungsirrtum
# ===========================================================================================================================
w120, w120_y = wortlaut(80, 170, 1100, "„Eine Willenserklärung, welche durch die zur Übermittlung verwendete Person oder "
                                       "Einrichtung unrichtig übermittelt worden ist, kann unter der gleichen Voraussetzung "
                                       "angefochten werden wie nach § 119 eine irrtümlich abgegebene Willenserklärung.“",
                        "§ 120 BGB", "w120", size=31,
                        marken=[("Einrichtung", beim("w120", "Einrichtung")), ("unrichtig übermittelt", beim("w120", "unrichtig")),
                                ("angefochten", beim("w120", "anfechten"))])
folie([("w120", f"{PII} › Gedanke des § 120 BGB"), ("bgh", f"{PII} › BGH: kein Unterschied"),
       ("bereich", f"{PII} › auch im eigenen System: Erklärungsirrtum")], [
    *tafel("w120", "Fehler der Software: § 120 BGB"),
    *w120,
    blk(110, w120_y + 24, 1040, 120, GELB, beim("bgh", "Es"), [("BGH: kein Unterschied – selbst vertippt oder", "ExtraBold", 31, INK),
                                                             ("Software verfälscht das richtig Eingegebene", "ExtraBold", 31, INK)]),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 7", 110, w120_y + 158, beim("bgh", "Es")),
    *okw("auch im eigenen System: Erklärungsirrtum", w120_y + 225, "bereich", beim("bereich", "Erklärungsirrtum"), "Bold", 34),
    *requisit([("w120", ("tabler", "send", 110, WEISS), "Übermittlung", WEISS),
               ("bgh", ("tabler", "bug", 110, HELLROT), "Software", HELLROT),
               ("bereich", ("tabler", "device-desktop", 130, BLAUHELL), "eigenes System", BLAUHELL)]),
    *stehend("WE", FX, [("w120", "ruhig"), ("bgh", "denkt"), ("bereich", "froh")]),
])
assert w120_y + 225 + 40 <= 895, w120_y

# ===========================================================================================================================
# F2 Was wird angefochten? Fortwirken des Fehlers in der automatischen Annahme (VIII ZR 79/04 S. 6–8)
# ===========================================================================================================================
folie([("fort", f"{PII} › Shopseite war kein Angebot"), ("fort2", f"{PII} › angefochten: die Annahme"),
       ("kaus", f"{PII} › Kausalität")], [
    *tafel("fort", "Was wird angefochten?"),
    blk(110, 185, 430, 170, WEISS, "fort", [("Shopseite: 49 €", "ExtraBold", 32, INK), ("kein Angebot", "Bold", 30, INK)]),
    bis_(nein(330, 330, beim("fort", "kein"), gr=22), None),
    pfeil(560, 270, 700, 270, beim("fort2", "In"), breite=8, kopf=26),
    blk(720, 185, 430, 170, LILAHELL, "fort2", [("2. Mail: Annahme", "ExtraBold", 32, INK), ("angefochten", "Bold", 30, INK)]),
    z("Fehler wirkt fort: automatisch zu 49 € erklärt", 110, 400, beim("fort2", "In"), "Bold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 6–8", 110, 448, beim("fort2", "In")),
    *okz("Kausalität: bei Kenntnis nicht so angenommen", 520, "kaus", "Bold", 34),
    zit("§ 119 Abs. 1 BGB a. E.", 185, 568, "kaus"),
    *requisit([("fort", ("tabler", "browser", 120, WEISS), "Shopseite", WEISS),
               ("fort2", ("tabler", "mail-check", 120, LILAHELL), "Annahme", LILAHELL)], px=1560, pu=330, py=90),
    *paar("KU", [("fort", "ruhig"), ("kaus", "sorge")], "WE", [("fort", "denkt"), ("fort2", "ernst")]),
])

# ===========================================================================================================================
# G Abgrenzung Kalkulationsirrtum (VIII ZR 79/04 S. 8 f.)
# ===========================================================================================================================
folie([("kalk", "Abgrenzung · Kalkulationsirrtum"), ("kalk2", "Abgrenzung › grundsätzlich keine Anfechtung")], [
    *tafel("kalk", "Abgrenzung: Kalkulationsirrtum"),
    z("verrechnet schon bei der Berechnung des Preises", 110, 185, beim("kalk", "verrechnet"), "Bold", 34),
    blk(110, 250, 1040, 90, LILAHELL, beim("kalk", "Irrtum"), [("= Irrtum im Beweggrund", "ExtraBold", 34, INK)]),
    *neinz("grundsätzlich keine Anfechtung,", 390, "kalk2", "Bold", 34, kreuz=beim("kalk2", "nicht")),
    z("selbst wenn eine Software falsch gerechnet hat", 185, 438, beim("kalk2", "Software"), "Bold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 8 f.", 185, 490, beim("kalk2", "Software")),
    *requisit([("kalk", ("tabler", "calculator", 110, WEISS), "Berechnung", WEISS),
               ("kalk2", ("tabler", "ban", 110, HELLROT), "keine Anfechtung", HELLROT)]),
    *stehend("WE", FX, [("kalk", "denkt"), ("kalk2", "ernst")]),
])

# ===========================================================================================================================
# H Frist § 121, Erklärung gegenüber Herrn Kübler (§ 143), Folge § 142 Abs. 1
# ===========================================================================================================================
folie([("frist", f"{PII} › Frist: unverzüglich, § 121 BGB"), ("anruf2", f"{PII} › Erklärung gegenüber Herrn Kübler"),
       ("p142", f"{PII} › nichtig von Anfang an, § 142 Abs. 1 BGB")], [
    *tafel("frist", "Anfechtungsfrist und Folge"),
    z("§ 121 Abs. 1 BGB: unverzüglich,", 110, 185, beim("frist", "Paragraf"), "ExtraBold", 35),
    z("also ohne schuldhaftes Zögern, ab Kenntnis", 110, 237, beim("frist", "ohne"), "Bold", 34),
    *okz("am selben Mittag gegenüber Herrn Kübler", 320, "anruf2", "Bold", 34),
    zit("§ 143 Abs. 1, 2 BGB", 185, 368, "anruf2"),
    blk(110, 450, 1040, 120, HELLROT, "p142", [("§ 142 Abs. 1 BGB: Kaufvertrag", "ExtraBold", 33, INK),
                                             ("von Anfang an nichtig", "ExtraBold", 33, INK)]),
    *requisit([("frist", ("tabler", "clock", 110, GELB), "unverzüglich", GELB),
               ("anruf2", ("tabler", "device-mobile", 90, WEISS), "Anruf", WEISS),
               ("p142", ("tabler", "file-x", 120, HELLROT), "nichtig", HELLROT)]),
    *stehend("WE", FX, [("frist", "ruhig"), ("anruf2", "ernst"), ("p142", "froh")]),
])

# ===========================================================================================================================
# I Folge der Anfechtung: § 122 BGB (Wortlautkarte), Vertrauensschaden (VII ZR 122/14 Rn. 23: Begriff), Abs. 2
# ===========================================================================================================================
w122, w122_y = wortlaut(80, 170, 1100, "„(1) Ist eine Willenserklärung … auf Grund der §§ 119, 120 angefochten, so hat der "
                                       "Erklärende … den Schaden zu ersetzen, den der andere … dadurch erleidet, dass er auf "
                                       "die Gültigkeit der Erklärung vertraut, …“", "§ 122 Abs. 1 BGB", "w122", size=31,
                        marken=[("Schaden zu ersetzen", beim("w122", "Schaden")), ("Gültigkeit der Erklärung", beim("w122", "Gültigkeit"))])
folie([("w122", "Folge der Anfechtung · § 122 BGB"), ("vs", "Folge der Anfechtung › Vertrauensschaden"),
       ("erf", "Folge der Anfechtung › nicht das Erfüllungsinteresse"), ("abs2", "Folge der Anfechtung › § 122 Abs. 2 BGB")], [
    *tafel("w122", "Folge: Ersatz nach § 122 BGB"),
    *w122,
    *okz("Vertrauensschaden: etwa Kosten im Vertrauen auf den Kauf", w122_y + 26, "vs", "Bold", 31),
    zit("Begriff: BGH, Versäumnisurt. v. 18.5.2017 – VII ZR 122/14, Rn. 23", 185, w122_y + 72, "vs"),
    *neinz("nicht ersetzt: was er bei Erfüllung gehabt hätte,", w122_y + 128, "erf", "Bold", 31, kreuz=beim("erf", "Nicht")),
    z("also nicht der günstige Fernseher", 185, w122_y + 172, beim("erf", "günstige"), "Bold", 31),
    blk(110, w122_y + 236, 1040, 110, HELLGRAU, "abs2", [("§ 122 Abs. 2: kein Ersatz, wenn er den Fehler", "ExtraBold", 30, INK),
                                                       ("kannte oder kennen musste", "ExtraBold", 30, INK)]),
    *requisit([("w122", ("tabler", "coin-euro", 120, GELB), "Ersatz", GELB),
               ("erf", ("tabler", "device-tv", 140, HELLROT), "kein Fernseher", HELLROT),
               ("abs2", ("tabler", "eye", 110, WEISS), "kennen musste", WEISS)]),
    *stehend("KU", FX, [("w122", "ruhig"), ("erf", "sorge"), ("abs2", "denkt")]),
])
assert w122_y + 236 + 110 <= 895, w122_y

# ===========================================================================================================================
# J Ergebnis: zurück im Telefonat
# ===========================================================================================================================
folie([("erg", "Ergebnis · Frau Wetzel muss nicht liefern"), ("erg2", "Ergebnis › Vertrag mit der 2. Mail, wirksam angefochten")], [
    *telefon("erg", oben=250),
    *fig("WE", WT, BODEN, FH, [("erg", "ruhig_r"), (beim("erg", "nicht"), "froh_r")], erst="cut"),
    hart(ns(NAME["WE"], WT, BODEN, "erg", ROT)),
    *fig("KU", KT, BODEN, FH, [("erg", "ruhig"), (beim("erg", "nicht"), "sorge"), ("erg2", "ernst")], erst="cut"),
    hart(ns(NAME["KU"], KT, BODEN, "erg", GRUEN)),
    *neinz("kein Lieferanspruch: Frau Wetzel muss nicht liefern", 40, "erg", "Bold", 34, x=130, rechts=1880,
           kreuz=beim("erg", "nicht")),
    *okz("Vertrag erst mit der 2. Mail – den hat sie wirksam angefochten", 104, "erg2", "Bold", 34, x=130, rechts=1880),
    zit("§§ 119 Abs. 1, 121, 142 Abs. 1 BGB; BGH, Urt. v. 26.1.2005 – VIII ZR 79/04", 130, 160, beim("erg2", "angefochten"),
        rechts=1880),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Welche Erklärung ist die Annahme?"), ("tipp2", "Klausurtipp · Wirkt der Fehler dort fort?"),
       ("tipp3", "Klausurtipp · Erklären oder Kalkulieren")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Welche Erklärung ist die Annahme?", 200, 200, beim("tipp", "Welche"), "Bold", 35),
    z("2. Wirkt der Fehler in genau dieser", 200, 280, "tipp2", "Bold", 35),
    z("Erklärung fort?", 200, 330, beim("tipp2", "Erklärung"), "Bold", 35),
    linienzug([(130, 410), (1130, 410)], "tipp3", breite=3),
    *okw("Fehler beim Erklären oder Übermitteln:", 440, "tipp3", beim("tipp3", "berechtigt"), "Bold", 34, x=245),
    z("anfechtbar", 245, 488, beim("tipp3", "berechtigt"), "ExtraBold", 34),
    *neinz("Fehler beim Kalkulieren: grundsätzlich nicht", 560, beim("tipp3", "Kalkulieren"), "Bold", 34, x=245),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 7–9", 245, 610, beim("tipp3", "Kalkulieren")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kaufvertrag", True),
          ("s1a", 1, "Shop nur Einladung, Bestellung als Angebot", False),
          ("s1b", 1, "Annahme durch die 2. Mail, nicht schon durch die Eingangsbestätigung", False),
          ("s2", 0, "II. Nichtigkeit durch Anfechtung, § 142 Abs. 1 BGB", True),
          ("s2a", 1, "Erklärungsirrtum, § 119 Abs. 1 BGB – auch bei fehlerhafter Software", False),
          ("s2b", 1, "Erklärung gegenüber Herrn Kübler, unverzüglich (§§ 143, 121 BGB)", False),
          ("s3", 0, "III. Ergebnis: kein Lieferanspruch", True),
          (beim("s3", "aber"), 1, "aber Vertrauensschaden nach § 122 BGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Herr Kübler gegen Frau Wetzel auf Lieferung"), 110, 90, "sch", 44)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 86, 1: 76}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Kaufvertrag"), ("s2", "Prüfungsschema › II. Anfechtung"),
       ("s3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Eingangsbestätigung ist", 0)], [("in der Regel ", 0), ("noch keine Annahme", "a"), (".", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "noch")}),
    *markertext([[("Verfälscht die eigene Software den", 0)], [("Preis, darf der Händler ", 0), ("anfechten", "b"), (",", 0)],
                 [("schuldet aber grundsätzlich den", 0)], [("Vertrauensschaden", "c"), (".", 0)]],
                750, 470, 44, "merk2", {"b": beim("merk2", "anfechten"), "c": beim("merk2", "Vertrauensschaden")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
