"""Folge 232 · Kündigung wegen 1,30 Euro? Der Fall Emmely (§ 626 BGB) – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen nach BAG, Urt. v. 10.6.2010 – 2 AZR 541/09: Kassiererin Doris (seit fast 31 Jahren), Kollegin Merle findet zwei
Pfandbons, Filialleiter Bartels gibt sie Doris zur Aufbewahrung im Kassenbüro; zehn Tage später löst Doris bei einem privaten
Einkauf zwei nicht abgezeichnete Pfandbons ein (1,30 €); fristlose, hilfsweise ordentliche Kündigung.
Szenen laut ../SZENENPLAN.md: A Kasse (Fund), B Kassenbüro (Ablage), C Kasse zehn Tage später (Einkauf, Kündigung, Frage),
D Sachverhalt, E § 626 Abs. 1 (Wortlautkarte, zwei Stufen), F Stufe 1 abstrakt, G Stufe 1 im Fall, H Stufe 2, I Abmahnung
(§ 314 Abs. 2 S. 1 als Wortlautkarte), J Abwägung im Fall, K Vorrat an Vertrauen, L Prozessverhalten, M Ergebnis,
N § 626 Abs. 2 und § 1 Abs. 2 S. 1 KSchG (Wortlautkarten), O Klausurtipp (Lexi), P Prüfschema, Q Merksatz (Lexi).
Zwei Handlungsgeräusche (Schritte, als Herr Bartels an die Kasse kommt; Kassenscanner, als die Bons über die Kasse gehen;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Die reale Klägerin wird nicht dargestellt;
„Emmely“ steht nur als Fallbezeichnung auf der Tafel. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/umbruch/redet/fig/ns/
okz/neinz/requisit/hand als eigene Kopie aus den Folgen 152 und 231 (gemeinsame Dateien unverändert); neu: theke(), regal(),
buero(), bons(), plus(), vorrat().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_232/"

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
THEKE = (205, 214, 222, 255)
BAND = (70, 74, 84, 255)
WAND = (246, 236, 220, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_232/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 152/231) -------------------------------------
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


def plus(text, y, cue, x=150, size=33, stil="Regular"):
    """Tafelzeile mit grünem (+) dahinter: Umstand, der in der Abwägung für Doris spricht."""
    e = plusminus(glyphen(text), x, y, cue, True, size=size, stil=stil)
    assert e[1].x + e[1].sprite.width <= 1170, f"Zeile zu breit: {text}"
    return e


def hand(name, cx, unten, hoehe, links=True):
    """Position der Hand (äußerster deckender Punkt im Band 45–62 % der Höhe) einer Figur."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h_ = a.shape[0]
    band = a[int(h_ * 0.45):int(h_ * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if links else xs.argmax()
    return e.x + xs[i], e.y + int(h_ * 0.45) + ys[i]


# --- Größen und Positionen --------------------------------------------------------------------------------------------------
BODEN_Y = 905                                # Boden im Supermarkt = Unterkante der Figuren
FHA = 480                                    # Figurenhöhe in den Fallszenen
THEKE_Y = 690                                # Oberkante der Kassentheke
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"DO": "Doris", "ME": "Merle", "BT": "Herr Bartels"}
NFARBE = {"DO": TUERKIS, "ME": ROT, "BT": BLAU}


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


def zwei(folge_do, folge_bt):
    """Doris und Herr Bartels rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("DO", X1, folge_do), *stehend("BT", X2, folge_bt)]


def allein(k, folge):
    return stehend(k, FX, folge)


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def theke(c, x0, x1):
    """Kassentheke (Grundform) mit Kassenband und Kasse (Tabler cash-register); verdeckt die Beine der Person dahinter."""
    s = 2
    w, h = x1 - x0, BODEN_Y - THEKE_Y
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 22 * s, (w + 3) * s, (h + 3) * s), 10 * s, fill=THEKE, outline=INK, width=5 * s)
    dr.rounded_rectangle((3 * s, 3 * s, (w + 3) * s, 28 * s), 8 * s, fill=BAND, outline=INK, width=5 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return [El(im, x0 - 3, THEKE_Y - 3, c, "cut", 0.0, None, name="theke"),
            ficon("tabler", "cash-register", x1 - 90, THEKE_Y + 2, 130, c, fuell=WEISS, anim="cut")]


def regal(c, x0, x1, y0=600):
    """Niedriges Warenregal (Grundform) mit Waren aus Tabler (gefüllt mit Palettenfarben)."""
    s = 2
    w, h = x1 - x0, BODEN_Y - y0
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((3 * s, 3 * s, (w + 3) * s, (h + 3) * s), fill=WEISS, outline=INK, width=5 * s)
    for yb in (h // 2, h - 6):
        dr.line((3 * s, yb * s, (w + 3) * s, yb * s), fill=INK, width=5 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    els = [El(im, x0 - 3, y0 - 3, c, "cut", 0.0, None, name="regal")]
    ware = [("bottle", BLAU), ("milk", WEISS), ("apple", ROT), ("bread", HOLZ), ("cheese", GELB), ("carrot", ORANGE)]
    n = 3
    for r, yb in enumerate((y0 + h // 2, BODEN_Y - 6)):
        for i in range(n):
            ic, fu = ware[r * n + i]
            els.append(ficon("tabler", ic, x0 + (i + 0.5) * w / n, yb - 4, 62, c, fuell=fu, anim="cut"))
    return els


def bons(cx, unten, cue, bis=None, anim="pop", breite=54):
    """Die zwei Pfandbons (Tabler receipt, weiß)."""
    return [ficon("tabler", "receipt", cx, unten, breite, cue, fuell=WEISS, bis=bis, anim=anim),
            ficon("tabler", "receipt", cx + breite * 0.8, unten, breite, cue, fuell=WEISS, bis=bis, anim=anim)]


# ===========================================================================================================================
# A Fall: an der Kasse – Merle findet zwei Pfandbons, Herr Bartels gibt sie Doris
# ===========================================================================================================================
TX0, TX1 = 200, 860                          # Kassentheke
DX_, MX_, BX_ = 540, 1060, 1560              # Doris (hinter der Theke, blickt nach rechts), Merle, Herr Bartels
S_LOS, S_DA = beim("chef", "Filialleiter"), beim("chef", "Bartels", ende=True)
FUND = beim("fund", "zwei")
WEITER = beim("chef", "weiter")
folie([(NULL, "Fall · Im Supermarkt"), ("fund", "Fall · Zwei Pfandbons"), ("chef", "Fall · Der Filialleiter")], [
    *regal(NULL, 1200, 1380),
    hart(linienzug([(40, BODEN_Y), (1880, BODEN_Y)], NULL, breite=7, farbe=INK)),
    hart(pl("Supermarkt mitten in der Stadt", 70, 30, NULL, fill=GELB, size=38)),
    # Doris hinter der Kasse (Theke verdeckt die Beine)
    *fig("DO", DX_, BODEN_Y, FHA, [(NULL, "froh_r"), (FUND, "staunt_r"), ("me1", "ruhig_r"), ("ba1", "ruhig_r")], erst="cut",
         bis="ablage"),
    *theke(NULL, TX0, TX1),
    hart(ns("Doris", DX_, BODEN_Y, NULL, TUERKIS)),
    pl("Doris: Kassiererin seit fast 31 Jahren", 70, 110, beim("doris", "seit"), fill=TUERKIS, size=34, bis="fund"),
    pl("ohne jede Beanstandung", 70, 190, beim("doris", "Beanstandung"), fill=WEISS, size=34, bis="fund"),
    # Merle findet die Bons im Kassenbereich
    *fig("ME", MX_, BODEN_Y, FHA, [(beim("fund", "Kollegin"), "staunt"), ("me1", "staunt")], bis="me1"),
    ns("Merle", MX_, BODEN_Y, beim("fund", "Kollegin"), ROT, d=0.1, bis="ablage"),
    *bons(905, BODEN_Y - 4, FUND, bis=WEITER),
    pl("2 Pfandbons: 0,48 € und 0,82 €", 70, 110, FUND, fill=WEISS, size=34, bis="ablage"),
    *redet("ME_redet", MX_, BODEN_Y, FHA, "me1", "chef"),
    blase("sprech", 600, 190, "me1", 1150, 250, inhalt=["Die hat wohl jemand", "liegen lassen!"], textsize=38,
          figur=("ME_redet", MX_, BODEN_Y, FHA), bis="chef"),
    *fig("ME", MX_, BODEN_Y, FHA, [("chef", "froh"), ("ba1", "ruhig")], erst="cut", bis="ablage"),
    # Herr Bartels kommt von rechts (Schritte) und gibt die Bons an Doris weiter
    szene(bewegt(peep_voll("BT_ruhig", BX_, BODEN_Y, FHA, "chef", anim="pop", bis="ba1"), S_LOS, S_DA, 140, 0),
          "232schritte*", 1.0, 0.0),
    bewegt(ns("Herr Bartels", BX_, BODEN_Y, "chef", BLAU, d=0.1, bis="ablage"), S_LOS, S_DA, 140, 0),
    pl("Filialleiter: Herr Bartels", 70, 190, beim("chef", "Filialleiter"), fill=BLAU, size=34, bis="ablage"),
    *bons(560, THEKE_Y, WEITER, bis="ablage"),
    *redet("BT_redet", BX_, BODEN_Y, FHA, "ba1", "ablage"),
    blase("sprech", 700, 200, "ba1", 1440, 240, inhalt=["Bewahren Sie die im Kassenbüro auf,", "falls sich noch jemand meldet."],
          textsize=32, figur=("BT_redet", BX_, BODEN_Y, FHA), bis="ablage"),
])

# ===========================================================================================================================
# B Kassenbüro: Doris legt die Bons auf die Ablage
# ===========================================================================================================================
OX = 1080                                    # Doris im Kassenbüro (blickt nach links zur Ablage)
hx, hy = hand("DO_ruhig", OX, BODEN_Y, FHA)
AB_X, AB_Y = 520, 560                        # Ablage (Brett) im Kassenbüro
AB_LOS, AB_DA = beim("ablage", "legt"), beim("ablage", "Ablage", ende=True)
bon_lauf = [bewegt(e, AB_LOS, AB_DA, round(hx - (AB_X + 20)), round(hy - AB_Y)) for e in bons(AB_X, AB_Y, "ablage", anim="cut")]


def buero(c):
    """Kassenbüro (Grundform): Wandfläche, Tür, Brett als Ablage mit Ordnern."""
    s = 2
    im = Image.new("RGBA", (1780 * s, 560 * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 3 * s, 1777 * s, 557 * s), 16 * s, fill=WAND, outline=INK, width=5 * s)
    dr.rounded_rectangle((1440 * s, 120 * s, 1640 * s, 557 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)   # Tür
    dr.ellipse((1600 * s, 330 * s, 1620 * s, 350 * s), fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    brett = Image.new("RGBA", (520, 26))
    ImageDraw.Draw(brett).rounded_rectangle((0, 0, 519, 25), 6, fill=HOLZ, outline=INK, width=4)
    return [El(im, 70, BODEN_Y - 557, c, "cut", 0.0, None, name="buero"),
            El(brett, AB_X - 200, AB_Y, c, "cut", 0.0, None, name="ablage"),
            ficon("tabler", "folder", AB_X - 120, AB_Y + 2, 90, c, fuell=GELB, anim="cut"),
            ficon("tabler", "archive", AB_X + 200, AB_Y + 2, 90, c, fuell=WEISS, anim="cut")]


folie([("ablage", "Fall · Im Kassenbüro")], [
    *buero("ablage"),
    hart(linienzug([(40, BODEN_Y), (1880, BODEN_Y)], "ablage", breite=7, farbe=INK)),
    hart(pl("Kassenbüro", 70, 30, "ablage", fill=GELB, size=38)),
    *fig("DO", OX, BODEN_Y, FHA, [("ablage", "ruhig"), (AB_DA, "froh")], erst="cut"),
    hart(ns("Doris", OX, BODEN_Y, "ablage", TUERKIS)),
    *bon_lauf,
    pl("Ablage im Kassenbüro", 70, 110, beim("ablage", "Ablage"), fill=WEISS, size=34),
])

# ===========================================================================================================================
# C Zehn Tage später: privater Einkauf an der Kasse, Kündigung, Frage
# ===========================================================================================================================
TX1C = 760
MX2, DX2, BX2 = 430, 990, 1400               # Merle hinter der Kasse (blickt nach rechts), Doris als Kundin, Herr Bartels
hx2, hy2 = hand("DO_ruhig", DX2, BODEN_Y, FHA)
EIN_LOS, EIN_DA = beim("einl", "reicht"), beim("einl", "Pfandbons", ende=True)
bons_kasse = [bewegt(e, EIN_LOS, EIN_DA, round(hx2 - 490), round(hy2 - THEKE_Y)) for e in bons(490, THEKE_Y, EIN_LOS, anim="cut",
                                                                                           bis="kuend")]
szene(bons_kasse[0], "232scanner*", 0.8, round(T_(EIN_DA) - T_(EIN_LOS), 3))   # Piepen, wenn die Bons an der Kasse ankommen
folie([("zehn", "Fall · Zehn Tage später"), ("einl", "Fall · Zwei Pfandbons an der Kasse"), ("kuend", "Fall · Die Kündigung"),
       ("frage", "Fall · Die Frage"), ("echt", "Fall · Der echte Fall: BAG 2010")], [
    hart(linienzug([(40, BODEN_Y), (1880, BODEN_Y)], "zehn", breite=7, farbe=INK)),
    *regal("zehn", 1620, 1840),
    pl("10 Tage später", 70, 30, "zehn", fill=GELB, size=38),
    ficon("tabler", "calendar-event", 420, 96, 66, "zehn", fuell=WEISS),
    pl("privater Einkauf, außerhalb der Arbeitszeit", 70, 110, beim("zehn", "außerhalb"), fill=TUERKIS, size=32, bis="kuend"),
    # Merle an der Kasse, Doris als Kundin mit Korb
    *fig("ME", MX2, BODEN_Y, FHA, [("zehn", "froh_r"), ("kuend", "sorge_r"), ("frage", "ernst_r")], erst="cut"),
    *theke("zehn", TX0, TX1C),
    ficon("tabler", "basket", 360, THEKE_Y + 2, 96, "zehn", fuell=GELB, anim="cut"),
    hart(ns("Merle", MX2, BODEN_Y, "zehn", ROT)),
    *fig("DO", DX2, BODEN_Y, FHA, [("zehn", "froh"), ("kuend", "schreck"), ("ba2", "sorge"), ("frage", "still")], erst="cut"),
    hart(ns("Doris", DX2, BODEN_Y, "zehn", TUERKIS)),
    *bons_kasse,
    pl("2 Pfandbons, nicht abgezeichnet", 70, 190, beim("einl", "abgezeichnet"), fill=WEISS, size=32, bis="kuend"),
    pl("Einkauf: 1,30 € billiger", 70, 270, "summe", fill=GELB, size=32, bis="kuend"),
    # Herr Bartels steht direkt daneben
    *fig("BT", BX2, BODEN_Y, FHA, [("dabei", "ruhig"), ("kuend", "ernst")], bis="ba2"),
    ns("Herr Bartels", BX2, BODEN_Y, "dabei", BLAU, d=0.1),
    pl("Herr Bartels steht direkt daneben", 70, 350, beim("dabei", "steht"), fill=BLAU, size=32, bis="kuend"),
    # Kündigung
    pl("Verdacht: die Bons aus dem Kassenbüro", 70, 110, beim("kuend", "verdächtigt"), fill=HELLROT, size=32, bis="frage"),
    pl("Kündigung: fristlos, hilfsweise ordentlich", 70, 190, beim("kuend", "fristlos"), fill=HELLROT, size=32, bis="frage"),
    ficon("tabler", "file-text", 900, 268, 80, beim("kuend", "fristlos"), fuell=WEISS, bis="frage"),
    *redet("BT_redet", BX2, BODEN_Y, FHA, "ba2", "frage"),
    blase("sprech", 640, 170, "ba2", 1300, 250, inhalt=["Das Vertrauen ist", "unwiederbringlich zerstört."], textsize=36,
          figur=("BT_redet", BX2, BODEN_Y, FHA), bis="frage"),
    *fig("BT", BX2, BODEN_Y, FHA, [("frage", "still")], erst="cut"),
    # Frage und echter Fall
    pl("Nach fast 31 Jahren fristlos wegen 1,30 €?", 70, 110, "frage", fill=PINK, size=34),
    karte(70, 200, 900, 150, "echt", fill=WEISS, rund=18, schatten=6, rand=4),
    z("Fall „Emmely“", 100, 222, "echt", "ExtraBold", 38, rechts=950),
    z("BAG, Urt. v. 10.6.2010 – 2 AZR 541/09", 100, 284, "echt", "Bold", 32, rechts=950),
])


# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
def sachverhalt_232(cue, absaetze, frage, quelle):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 12
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=32))
    els.append(z(quelle, 210, y + 84, cue, size=26, farbe=TEXT, rechts=1760))
    assert y + 84 + 40 <= 975, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)


sachverhalt_232("sv", [
    "Doris arbeitet seit fast 31 Jahren als Kassiererin in einem Supermarkt, bisher ohne Beanstandung. Ihre Kollegin Merle "
    "findet im Kassenbereich zwei Pfandbons über 0,48 € und 0,82 €. Filialleiter Bartels gibt sie Doris: Sie soll sie im "
    "Kassenbüro aufbewahren, falls sich noch jemand meldet. Doris legt sie dort auf eine Ablage.",
    "Zehn Tage später kauft Doris außerhalb ihrer Arbeitszeit privat ein und reicht bei Merle an der Kasse zwei nicht "
    "abgezeichnete Pfandbons. Ihr Einkauf wird 1,30 € billiger; Herr Bartels steht daneben.",
    "Der Arbeitgeber verdächtigt sie, die Bons aus dem Kassenbüro eingelöst zu haben, und kündigt fristlos, hilfsweise "
    "ordentlich. Doris bestreitet ein bewusstes Fehlverhalten und ändert ihre Erklärungen im Prozess mehrmals.",
], "Ist die fristlose Kündigung wirksam?", "Nach BAG, Urt. v. 10.6.2010 – 2 AZR 541/09 (Fall „Emmely“)")

# ===========================================================================================================================
# E Wortlautkarte § 626 Abs. 1 BGB: wichtiger Grund, zwei Stufen
# ===========================================================================================================================
PA = "§ 626 Abs. 1 BGB"
W626 = ("„Das Dienstverhältnis kann von jedem Vertragsteil aus wichtigem Grund ohne Einhaltung einer Kündigungsfrist "
        "gekündigt werden, wenn Tatsachen vorliegen, auf Grund derer dem Kündigenden unter Berücksichtigung aller Umstände "
        "des Einzelfalles und unter Abwägung der Interessen beider Vertragsteile die Fortsetzung des Dienstverhältnisses "
        "bis zum Ablauf der Kündigungsfrist oder bis zu der vereinbarten Beendigung des Dienstverhältnisses nicht "
        "zugemutet werden kann.“")
w626, w626_y = wortlaut(80, 160, 1100, W626, "§ 626 Abs. 1 BGB", "p626", marken=[
    ("Dienstverhältnis", beim("wg", "Dienstverhältnis")), ("wichtigem Grund", beim("wg", "wichtigem")),
    ("Umstände", beim("umst", "Umstände")), ("Abwägung", beim("umst", "Abwägung")),
    ("zugemutet", beim("zumut", "zugemutet"))], size=30)
folie([("p626", f"{PA} › wichtiger Grund"), ("stufen", f"{PA} › zwei Stufen"),
       ("absolut", f"{PA} › keine absoluten Kündigungsgründe")], rechts_frei([
    *tafel("p626", "Fristlos: § 626 Abs. 1 BGB"),
    *w626,
    blk(110, w626_y + 22, 1040, 76, GELB, "stufe1", [("1. Stufe: an sich als wichtiger Grund geeignet?", "ExtraBold", 32, INK)]),
    blk(110, w626_y + 112, 1040, 76, BLAU, "stufe2", [("2. Stufe: Abwägung – trotzdem zumutbar?", "ExtraBold", 32, INK)]),
    z("Keine absoluten Kündigungsgründe", 110, w626_y + 206, "absolut", "Bold", 32),
    zit("BAG, Urt. v. 10.6.2010 – 2 AZR 541/09, Rn. 16", 110, w626_y + 252, "absolut"),
    *requisit([("p626", ("tabler", "book", 100, WEISS), "§ 626 BGB", GELB),
               ("stufen", ("tabler", "stack-2", 100, BLAU), "2 Stufen", BLAU),
               ("absolut", ("tabler", "scale", 110, WEISS), "Einzelfall", WEISS)]),
    *zwei([("p626", "ruhig"), ("stufen", "sorge"), ("absolut", "ruhig")], [("p626", "ruhig"), ("stufen", "skeptisch")]),
]))
assert w626_y + 290 <= 900, w626_y

# ===========================================================================================================================
# F Stufe 1: an sich geeignet (abstrakt)
# ===========================================================================================================================
P1 = "Stufe 1 › an sich geeignet"
folie([("s1", P1), ("verm", f"{P1} › Vermögen des Arbeitgebers"), ("gering", f"{P1} › auch bei geringem Wert"),
       ("grenze", f"{P1} › keine Wertgrenze"), ("prog", f"{P1} › Prognoseprinzip")], rechts_frei([
    *tafel("s1", "1. Stufe: an sich geeignet?"),
    z("Vorsätzlich gegen das Vermögen des Arbeitgebers", 110, 180, "verm", "Bold", 34),
    zit("rechtswidrige und vorsätzliche Handlungen, Rn. 26", 110, 228, "verm"),
    *okz("auch bei geringem Wert oder ohne Schaden", 290, "gering", "Bold", 34, x=160),
    zit("Rn. 25 f.; Leitsatz 1", 160, 338, "gering"),
    *neinz("Keine Wertgrenze", 400, "grenze", "Bold", 34, x=160, kreuz=beim("grenze", "lehnt")),
    z("Vertrauen erschüttert, egal wie hoch der Schaden", 160, 452, "vertr", size=32),
    zit("Rn. 27", 160, 498, "vertr"),
    blk(110, 560, 1040, 80, LILA, beim("prog", "Prognoseprinzip"), [("Keine Strafe: Prognoseprinzip", "ExtraBold", 36, INK)]),
    z("Ist künftig noch eine störungsfreie", 110, 668, beim("prog", "Ist", nr=2), size=34),
    z("Vertragserfüllung zu erwarten?", 110, 716, beim("prog", "Ist", nr=2), size=34),
    zit("Rn. 28", 110, 764, beim("prog", "Ist", nr=2)),
    *requisit([("s1", ("tabler", "receipt", 90, WEISS), "1,30 €", GELB),
               ("grenze", ("tabler", "coin-euro", 100, GELB), "keine Wertgrenze", HELLROT),
               (beim("prog", "Prognoseprinzip"), ("tabler", "crystal-ball", 100, LILA), "Prognose", LILA)]),
    *allein("DO", [("s1", "sorge"), ("grenze", "ernst"), ("prog", "ruhig")]),
]))

# ===========================================================================================================================
# G Stufe 1 im Fall
# ===========================================================================================================================
P1F = "Stufe 1 › im Fall"
folie([("fest", f"{P1F} › Feststellung des LAG"), ("vort", f"{P1F} › Pflichtverletzung"),
       ("ansich", f"{P1F} › wichtiger Grund an sich (+)")], rechts_frei([
    *tafel("fest", "1. Stufe im Fall"),
    z("LAG: Doris hat die Bons aus dem Kassenbüro eingelöst.", 110, 180, "fest", "Bold", 32),
    zit("Rn. 20", 110, 226, "fest"),
    z("Doris bestreitet ein bewusstes Fehlverhalten.", 110, 282, "bestr", size=32),
    z("BAG an die Feststellung gebunden", 110, 334, "bind", "Bold", 32),
    zit("§ 559 Abs. 2 ZPO; Rn. 21", 110, 380, "bind"),
    *okz("Vorteil verschafft, der ihr nicht zustand", 440, "vort", "Bold", 33, x=160),
    *okz("klare Anweisung des Filialleiters missachtet", 498, "weis", "Bold", 33, x=160),
    *okz("Kernbereich ihrer Arbeit als Kassiererin", 556, "kern", "Bold", 33, x=160),
    zit("Rn. 31, 42", 160, 604, "kern"),
    blk(110, 670, 1040, 80, HELLGRUEN, "ansich", [("Wichtiger Grund an sich (+)", "ExtraBold", 36, INK)]),
    *requisit([("fest", ("tabler", "gavel", 100, HOLZ), "Landesarbeitsgericht", WEISS),
               ("vort", ("tabler", "receipt", 90, WEISS), "1,30 € Vorteil", GELB),
               ("weis", ("tabler", "alert-triangle", 100, GELB), "Anweisung missachtet", HELLROT),
               ("kern", ("tabler", "cash-register", 120, WEISS), "Kassiererin", TUERKIS),
               ("ansich", ("tabler", "file-check", 100, HELLGRUEN), "an sich (+)", HELLGRUEN)]),
    *zwei([("fest", "ruhig"), ("bestr", "ernst"), ("vort", "still"), ("ansich", "sorge")],
          [("fest", "ruhig"), ("weis", "ernst"), ("ansich", "skeptisch")]),
]))

# ===========================================================================================================================
# H Stufe 2: Interessenabwägung, mildere Mittel
# ===========================================================================================================================
P2 = "Stufe 2 › Interessenabwägung"


def mittel(x, cue, icon, fuell, zeilen):
    els = [karte(x, 600, 500, 120, cue, fill=HELL, rund=18, schatten=6, rand=4),
           ficon("tabler", icon, x + 70, 700, 76, cue, fuell=fuell)]
    y0 = 660 - 22 * len(zeilen)
    for i, t in enumerate(zeilen):
        els.append(z(t, x + 130, y0 + i * 44, cue, "ExtraBold", 34, rechts=x + 490))
    return els


folie([("abw", P2), ("dauer", f"{P2} › Dauer, störungsfreier Verlauf"), ("mild", f"{P2} › mildere Mittel")], rechts_frei([
    *tafel("abw", "2. Stufe: Interessenabwägung"),
    z("Zu berücksichtigen sind etwa:", 110, 180, "krit", "Bold", 34),
    z("• Gewicht der Pflichtverletzung", 130, 236, beim("krit", "Gewicht"), size=33),
    z("• Grad des Verschuldens", 130, 284, beim("krit", "Grad"), size=33),
    z("• Wiederholungsgefahr", 130, 332, beim("krit", "Wiederholungsgefahr"), size=33),
    z("• Dauer und störungsfreier Verlauf", 130, 380, "dauer", size=33),
    zit("Rn. 34", 130, 428, "dauer"),
    blk(110, 484, 1040, 80, HELLROT, "mild", [("Fristlos nur, wenn mildere Mittel unzumutbar sind", "ExtraBold", 33, INK)]),
    *requisit([("abw", ("tabler", "scale", 110, WEISS), "Abwägung", WEISS),
               ("mild", ("tabler", "hand-stop", 100, GELB), "milderes Mittel?", HELLROT)]),
    *zwei([("abw", "ruhig"), ("dauer", "froh"), ("mild", "ruhig")], [("abw", "ruhig"), ("mild", "skeptisch")]),
]) + mittel(110, beim("abm", "Abmahnung"), "file-alert", GELB, ["Abmahnung"])
  + mittel(650, beim("abm", "ordentliche"), "calendar-time", WEISS, ["ordentliche", "Kündigung"]))

# ===========================================================================================================================
# I Die Abmahnung: Verhältnismäßigkeit, § 314 Abs. 2 S. 1 BGB (Wortlautkarte), Ausnahmen
# ===========================================================================================================================
PAB = "Stufe 2 › Abmahnung"
W314 = ("„Besteht der wichtige Grund in der Verletzung einer Pflicht aus dem Vertrag, ist die Kündigung erst nach "
        "erfolglosem Ablauf einer zur Abhilfe bestimmten Frist oder nach erfolgloser Abmahnung zulässig. …“")
w314, w314_y = wortlaut(80, 262, 1100, W314, "§ 314 Abs. 2 S. 1 BGB", "p314",
                        marken=[("nach erfolgloser Abmahnung", beim("p314", "bestätigt"))], size=30)
folie([("verh", f"{PAB} › Verhältnismäßigkeit"), ("p314", f"{PAB} › § 314 Abs. 2 BGB"),
       ("entb", f"{PAB} › entbehrlich nur ausnahmsweise"), ("vb", f"{PAB} › auch bei Vermögensdelikten")], rechts_frei([
    *tafel("verh", "Die Abmahnung"),
    z("Grundsatz der Verhältnismäßigkeit", 110, 180, "verh", "Bold", 34),
    zit("Rn. 35", 110, 226, "verh"),
    *w314,
    zit("BAG: „gesetzgeberische Bestätigung“, Rn. 37", 110, w314_y + 10, beim("p314", "bestätigt")),
    z("Entbehrlich nur, wenn", 110, w314_y + 62, "entb", "Bold", 33),
    z("• Besserung auch nach Abmahnung nicht zu erwarten", 130, w314_y + 110, beim("entb", "Besserung"), size=31),
    z("• oder Hinnahme offensichtlich ausgeschlossen", 130, w314_y + 156, "schwer", size=31),
    zit("Rn. 37", 130, w314_y + 200, "schwer"),
    blk(110, w314_y + 246, 1040, 76, GELB, "vb", [("Auch bei Vermögensdelikten (Rn. 38)", "ExtraBold", 33, INK)]),
    *requisit([("verh", ("tabler", "scale", 110, WEISS), "verhältnismäßig?", WEISS),
               ("p314", ("tabler", "book", 100, WEISS), "§ 314 Abs. 2 BGB", GELB),
               ("entb", ("tabler", "file-alert", 100, GELB), "Abmahnung nötig", GELB),
               ("vb", ("tabler", "coin-euro", 100, GELB), "auch Vermögensdelikte", WEISS)]),
    *allein("BT", [("verh", "ruhig"), ("p314", "skeptisch"), ("vb", "still")]),
]))
assert w314_y + 322 <= 900, w314_y

# ===========================================================================================================================
# J Abwägung im Fall: offen statt heimlich, fast 31 Jahre
# ===========================================================================================================================
PF = "Stufe 2 › Abwägung im Fall"
folie([("fall2", PF), ("offen", f"{PF} › offen statt heimlich"), ("jahre", f"{PF} › fast 31 Jahre")], rechts_frei([
    *tafel("fall2", "Abwägung im Fall"),
    *plus("offen eingelöst, vor den Augen des Vorgesetzten", 190, "offen"),
    *plus("nicht auf Heimlichkeit angelegt", 250, "heiml"),
    *plus("sich eines schweren Unrechts nicht bewusst", 310, "unr"),
    zit("Rn. 45", 150, 360, "unr"),
    *plus("fast 31 Jahre ohne vergleichbare Pflichtverletzung", 430, "jahre", stil="Bold"),
    zit("Rn. 46–48", 150, 480, "jahre"),
    *requisit([("fall2", ("tabler", "scale", 110, WEISS), "Abwägung", WEISS),
               ("offen", ("tabler", "eye", 100, WEISS), "offen", WEISS),
               ("jahre", ("tabler", "calendar", 100, WEISS), "fast 31 Jahre", TUERKIS)]),
    *allein("DO", [("fall2", "ruhig"), ("offen", "still"), ("jahre", "froh")]),
]))

# ===========================================================================================================================
# K Vorrat an Vertrauen (31 Felder), objektiver Maßstab, geringer Nachteil
# ===========================================================================================================================
VX, VY, VW, VH, VG = 110, 300, 30, 70, 3.3   # Vorratsbalken: links, oben, Feldbreite, Höhe, Abstand


def vorrat(cue, n=31):
    """Vorrat an Vertrauen als Balken aus 31 Feldern (je ein Jahr, das letzte nur angefangen)."""
    s = 2
    im = Image.new("RGBA", (int((n * (VW + VG) + 10) * s), (VH + 10) * s))
    dr = ImageDraw.Draw(im)
    for i in range(n):
        x0 = (i * (VW + VG) + 3) * s
        dr.rounded_rectangle((x0, 3 * s, x0 + VW * s, (VH + 3) * s), 6 * s, fill=GRUEN, outline=INK, width=3 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, VX - 3, VY - 3, cue, "fade", 0.0, None, name="vorrat")


def angezehrt(cue, i=30):
    im = Image.new("RGBA", (VW + 6, VH + 6))
    ImageDraw.Draw(im).rounded_rectangle((3, 3, VW + 2, VH + 2), 6, fill=ROT[:3] + (255,), outline=INK, width=3)
    return El(im, VX - 3 + i * (VW + VG), VY - 3, cue, "pop", 0.0, None, name="angezehrt")


assert VX + 31 * (VW + VG) <= 1170
PV = "Stufe 2 › Vorrat an Vertrauen"
folie([("vorrat", PV), ("aufg", f"{PV} › nicht vollständig aufgezehrt"), ("obj", f"{PV} › objektiver Maßstab"),
       ("schad", "Stufe 2 › geringer Nachteil")], rechts_frei([
    *tafel("vorrat", "Vorrat an Vertrauen"),
    z("„erarbeiteter Vorrat an Vertrauen“", 110, 190, "vorrat", "Bold", 36),
    zit("Rn. 47", 760, 200, "vorrat"),
    vorrat("vorrat"),
    z("fast 31 Jahre", 110, VY + VH + 14, "vorrat", size=28, farbe=TEXT),
    angezehrt(beim("aufg", "ersten")),
    z("1. Vorfall", VX + 30 * (VW + VG) + VW - 122, VY + VH + 14, beim("aufg", "ersten"), "Bold", 28, farbe=DROT),
    z("Je länger ungestört, desto eher wird er durch einen", 110, 450, "aufg", size=32),
    z("ersten Vorfall nicht vollständig aufgezehrt.", 110, 496, "aufg", size=32),
    z("Maßstab: objektiv, nicht das Gefühl des Arbeitgebers", 110, 570, "obj", "Bold", 32),
    zit("Rn. 47, 50", 110, 616, "obj"),
    *plus("geringer Nachteil: nach 10 Tagen keine Nachfrage", 680, "schad", x=110, size=32),
    zit("Rn. 50", 110, 730, "schad"),
    *requisit([("vorrat", ("tabler", "heart-handshake", 110, GRUEN), "Vertrauen", HELLGRUEN),
               ("obj", ("tabler", "scale", 110, WEISS), "objektiv", WEISS),
               ("schad", ("tabler", "receipt", 90, WEISS), "1,30 €", GELB)]),
    *zwei([("vorrat", "froh"), ("aufg", "ruhig"), ("schad", "froh")], [("vorrat", "ruhig"), ("obj", "skeptisch"), ("schad", "still")]),
]))

# ===========================================================================================================================
# L Prozessverhalten
# ===========================================================================================================================
PP = "Stufe 2 › Prozessverhalten"
folie([("proz", PP), ("zug", f"{PP} › Zeitpunkt des Zugangs"), ("rueck", f"{PP} › keine Rückschlüsse")], rechts_frei([
    *tafel("proz", "Und das Prozessverhalten?"),
    z("Erklärungen im Prozess mehrmals geändert", 110, 180, "proz", "Bold", 34),
    z("Das zählt nicht gegen sie.", 110, 260, "zug", "ExtraBold", 34),
    z("Maßgeblich: Zeitpunkt des Zugangs der Kündigung", 110, 330, beim("zug", "Maßgeblich"), size=33),
    zit("Rn. 52", 110, 378, beim("zug", "Maßgeblich")),
    z("Keine Rückschlüsse auf künftige Zuverlässigkeit", 110, 440, "rueck", size=33),
    zit("Rn. 54, 56", 110, 488, "rueck"),
    *requisit([("proz", ("tabler", "message-2", 100, WEISS), "im Prozess", WEISS),
               ("zug", ("tabler", "mail", 100, WEISS), "Zugang", GELB),
               ("rueck", ("tabler", "user-check", 100, HELLGRUEN), "zuverlässig?", HELLGRUEN)]),
    *zwei([("proz", "sorge"), ("zug", "ruhig")], [("proz", "skeptisch"), ("rueck", "still")]),
]))

# ===========================================================================================================================
# M Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis"), ("unw", "Ergebnis › fristlose Kündigung unwirksam"), ("ausr", "Ergebnis › Abmahnung hätte gereicht")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    *neinz("Die fristlose Kündigung ist unwirksam.", 200, "unw", "ExtraBold", 36, x=160, kreuz=beim("unw", "unwirksam")),
    blk(110, 300, 1040, 90, HELLGRUEN, "ausr", [("Eine Abmahnung hätte ausgereicht.", "ExtraBold", 38, INK)]),
    zit("BAG, Urt. v. 10.6.2010 – 2 AZR 541/09, Rn. 14, 32", 110, 412, "ausr"),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Bundesarbeitsgericht", WEISS),
               ("ausr", ("tabler", "file-alert", 100, GELB), "Abmahnung", GELB)]),
    *zwei([("erg", "ruhig"), ("unw", "froh")], [("erg", "ruhig"), ("unw", "still")]),
]))

# ===========================================================================================================================
# N Noch zwei Punkte: § 626 Abs. 2 BGB, hilfsweise ordentliche Kündigung § 1 Abs. 2 S. 1 KSchG (Wortlautkarten)
# ===========================================================================================================================
W6262 = ("„Die Kündigung kann nur innerhalb von zwei Wochen erfolgen. Die Frist beginnt mit dem Zeitpunkt, in dem der "
         "Kündigungsberechtigte von den für die Kündigung maßgebenden Tatsachen Kenntnis erlangt.“")
w2, w2_y = wortlaut(80, 160, 1100, W6262, "§ 626 Abs. 2 S. 1, 2 BGB", "p2",
                    marken=[("zwei Wochen", beim("p2", "zwei", nr=3)), ("Kenntnis", beim("kennt", "Kenntnis"))], size=30)
W12 = ("„Sozial ungerechtfertigt ist die Kündigung, wenn sie nicht durch Gründe, die … in dem Verhalten des Arbeitnehmers "
       "liegen, … bedingt ist.“")
wk, wk_y = wortlaut(80, w2_y + 72, 1100, W12, "§ 1 Abs. 2 S. 1 KSchG", "kschg",
                    marken=[("Sozial ungerechtfertigt", beim("kschg", "sozial"))], size=30)
folie([("p2", "Noch zwei Punkte › § 626 Abs. 2 BGB: 2 Wochen"), ("ord", "Noch zwei Punkte › hilfsweise ordentliche Kündigung"),
       ("kschg", "Noch zwei Punkte › § 1 Abs. 2 S. 1 KSchG"), ("v152", "Noch zwei Punkte › Video „Kündigungsschutz“")],
      rechts_frei([
    *tafel("p2", "Noch zwei Punkte"),
    *w2,
    z("Hilfsweise ordentliche Kündigung?", 110, w2_y + 18, "ord", "Bold", 34),
    *wk,
    z("sozial ungerechtfertigt: Abmahnung hätte genügt", 110, wk_y + 20, beim("kschg", "weil"), "Bold", 32),
    zit("BAG, Urt. v. 10.6.2010 – 2 AZR 541/09, Rn. 58", 110, wk_y + 66, beim("kschg", "weil")),
    z("Anwendbarkeit des KSchG: Video „Kündigungsschutz“", 110, wk_y + 122, "v152", "Bold", 30, farbe=TEXT),
    *requisit([("p2", ("tabler", "hourglass", 90, GELB), "2 Wochen", GELB),
               ("ord", ("tabler", "calendar-time", 100, WEISS), "ordentlich?", WEISS),
               ("kschg", ("tabler", "book", 100, WEISS), "§ 1 KSchG", BLAU)]),
    *zwei([("p2", "ruhig"), ("kschg", "froh")], [("p2", "ruhig"), ("ord", "skeptisch"), ("kschg", "still")]),
]))
assert wk_y + 160 <= 900, wk_y

# ===========================================================================================================================
# O Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Bagatellfall"), ("t2", "Klausurtipp · geringer Wert: Interessenabwägung"),
       ("t3", "Klausurtipp · Abmahnung prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bagatellfall nicht schon", 200, 200, "t1", "ExtraBold", 38),
    z("auf der 1. Stufe aussortieren", 200, 256, "t1", "ExtraBold", 38),
    linienzug([(130, 336), (1130, 336)], "t2", breite=3),
    z("Der geringe Wert gehört", 200, 362, "t2", "Bold", 36),
    z("in die Interessenabwägung.", 200, 414, "t2", "Bold", 36),
    linienzug([(130, 494), (1130, 494)], "t3", breite=3),
    z("Dort immer prüfen:", 200, 520, "t3", "Bold", 36),
    z("Hätte eine Abmahnung genügt?", 200, 572, beim("t3", "Abmahnung"), "ExtraBold", 38),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# P Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Kündigungserklärung", True),
          ("k1", 1, "schriftlich, § 623 BGB", False),
          ("k2", 0, "II. Klagefrist: 3 Wochen", True),
          ("k2", 1, "§ 13 Abs. 1 S. 2, § 4 S. 1 KSchG", False),
          ("k3", 0, "III. Wichtiger Grund, § 626 Abs. 1 BGB", True),
          ("k3a", 1, "1. an sich geeignet", False),
          ("k3b", 1, "2. Interessenabwägung mit milderen Mitteln", False),
          ("k4", 0, "IV. Zwei-Wochen-Frist, § 626 Abs. 2 BGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: fristlose Kündigung"), 110, 90, "sch", 46),
           z("§ 626 BGB; § 623 BGB; §§ 4, 13 KSchG", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 78, 1: 70}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Kündigungserklärung"), ("k2", "Prüfschema › II. Klagefrist"),
       ("k3", "Prüfschema › III. Wichtiger Grund"), ("k4", "Prüfschema › IV. Zwei-Wochen-Frist")], els_sch)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Auch ein ", 0), ("Bagatelldelikt", "a"), (" gegen den", 0)], [("Arbeitgeber kann an sich", 0)],
                 [("ein wichtiger Grund sein.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "Bagatelldelikt")}),
    *markertext([[("Doch vor der Kündigung steht", 0)], [("in der Regel die ", 0), ("Abmahnung", "b"), (",", 0)],
                 [("gerade nach vielen Jahren", 0)], [("ohne Beanstandung.", 0)]], 750, 540, 44, "m2",
                {"b": beim("m2", "Abmahnung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
