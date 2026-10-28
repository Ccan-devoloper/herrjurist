"""Folge 195 · Kostenentscheidung ZPO: Kostenquote nach §§ 91, 92 – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Malermeister Herr Dressler streicht die Fassade am Haus von Frau Lindau und berechnet 10.000 € (auch für die
Garage); das Amtsgericht spricht 7.300 € zu (Auftrag für die Garage nicht bewiesen). Szenen laut ../SZENENPLAN.md:
A Am Haus von Frau Lindau, B Amtsgericht (Akte, Tenor der Richterin, Frage), C Sachverhalt, D Grundsatz § 91 Abs. 1 S. 1
(Wortlaut), E Teilunterliegen § 92 Abs. 1 S. 1 (Wortlaut), F Quote rechnen (Balken 27 % / 73 %), G Prozent oder Bruch und
Kostentenor, H Kostenaufhebung (Wortlaut § 92 Abs. 1 S. 2), I Ausnahme § 92 Abs. 2 (Wortlaut Nr. 1, Skala mit Faustregel),
J vier Sonderregeln (Wortlautkarten §§ 93, 91a, 269 Abs. 3 S. 2, 344), K Klausurtipp (Lexi, Wortlaut § 308 Abs. 2),
L Schema, M Merksatz (Lexi).
Handlungsgeräusch: Die Akte landet auf dem Richtertisch (B); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 192 (gemeinsame Dateien unverändert); neu: balken(), skala(), sachverhalt_195().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (ZPO), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_195/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_195/" in n:
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
FHA = 470                                    # Figurenhöhe in den Fallszenen
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
NAME = {"DR": "Herr Dressler", "LI": "Frau Lindau", "RI": "Richterin"}
NFARBE = {"DR": BLAU, "LI": ROT, "RI": LILA}


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


def zwei(folge_l, folge_r, links="DR", rechts="LI"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)







# --- eigene Szenenbausteine Folge 195 ----------------------------------------------------------------------------------------
DUNKEL = (58, 58, 72, 255)
GRAU = (205, 205, 210, 255)


def balken(x, y, w, h, teile, cue, rand=5):
    """Leerer Balken (Streitwert); teile = [(anteil 0..1 von links, breite 0..1, farbe, cue, text)] füllen sich zum Wort."""
    def rahmen(fill=None):
        im = Image.new("RGBA", (w + 2 * rand, h + 2 * rand))
        ImageDraw.Draw(im).rounded_rectangle((rand // 2, rand // 2, w + rand + rand // 2, h + rand + rand // 2), 14,
                                             fill=fill, outline=INK, width=rand)
        return im
    els = [El(rahmen(WEISS), x - rand, y - rand, cue, "fade", 0.0, None, name="balken")]
    for a, b, farbe, c, txt in teile:
        im = Image.new("RGBA", (int(w * b), h))
        ImageDraw.Draw(im).rectangle((0, 0, im.width, h), fill=farbe)
        dr = ImageDraw.Draw(im)
        if a > 0:
            dr.line((0, 0, 0, h), fill=INK, width=rand)
        f = F("ExtraBold", 30)
        assert f.getlength(glyphen(txt)) <= im.width - 16, f"Balkentext zu breit: {txt}"
        dr.text(((im.width - f.getlength(txt)) / 2, (h - 38) / 2), txt, font=f, fill=INK)
        els.append(El(im, x + int(w * a), y, c, "fade", 0.0, None, name="balkenteil:" + txt))
    els.append(El(rahmen(None), x - rand, y - rand, cue, "fade", 0.0, None, name="balkenrand"))
    return els


def skala(x, y, w, h, cue, gruen_bis, maximum, marke_cue, marke_wert, marke_text):
    """Skala 0 … maximum % mit grüner Zone bis gruen_bis (Faustregel) und rotem Zeiger bei marke_wert."""
    els = []
    im = Image.new("RGBA", (w + 10, h + 70))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((5, 5, w + 5, h + 5), 10, fill=WEISS, outline=INK, width=5)
    gw = int(w * gruen_bis / maximum)
    d.rounded_rectangle((5, 5, gw + 5, h + 5), 10, fill=GRUEN, outline=INK, width=5)
    f = F("Bold", 28)
    for v in range(0, maximum + 1, 10):
        xx = 5 + int(w * v / maximum)
        d.line((xx, h + 5, xx, h + 20), fill=INK, width=4)
        t = f"{v} %"
        tx = min(max(0, xx - f.getlength(t) / 2), w + 10 - f.getlength(t))
        d.text((tx, h + 24), t, font=f, fill=INK)
    els.append(El(im, x - 5, y - 5, cue, "fade", 0.0, None, name="skala"))
    zx = x + int(w * marke_wert / maximum)
    z_ = Image.new("RGBA", (40, h + 40))
    ImageDraw.Draw(z_).polygon([(0, 0), (40, 0), (20, 26)], fill=DROT)
    ImageDraw.Draw(z_).rectangle((16, 22, 24, h + 40), fill=DROT)
    els.append(El(z_, zx - 20, y - 28, marke_cue, "pop", 0.0, None, name="zeiger"))
    p = pl(marke_text, zx, y - 86, marke_cue, fill=HELLROT, size=28, anker="m")
    els.append(p)
    return els


# ===========================================================================================================================
# A Fall: am Haus von Frau Lindau
# ===========================================================================================================================
DRX, LIX = 1250, 1650
folie([(NULL, "Fall · Der Malermeister"), ("haus", "Fall · Fassade und Garage"), ("rechnung", "Fall · Rechnung: 10.000 €"),
       ("zahlt", "Fall · Frau Lindau zahlt nichts"), ("li1", "Fall · Frau Lindau bestreitet"),
       ("dr1", "Fall · Herr Dressler will klagen")], [
    boden(NULL),
    hart(ficon("tabler", "sun", 1760, 200, 110, NULL, fuell=GELB, anim="cut")),
    hart(ficon("ph", "house", 330, BODEN_Y + 2, 420, NULL, fuell=WEISS, nebenfarbe=BLAU, anim="cut")),
    hart(ficon("ph", "garage", 720, BODEN_Y + 2, 250, NULL, fuell=WEISS, nebenfarbe=GRAU, anim="cut")),
    hart(ficon("ph", "paint-bucket", 1010, BODEN_Y, 100, NULL, fuell=GELB, anim="cut")),
    *fig("DR", DRX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("rechnung", "froh_r"), ("zahlt", "sorge_r"), ("li1", "skeptisch_r")],
         erst="cut", bis="dr1"),
    *redet("DR_redet_r", DRX, BODEN_Y, FHA, "dr1", "klage"),
    hart(ns("Herr Dressler · Malermeister", DRX, BODEN_Y, NULL, NFARBE["DR"])),
    pl("Am Haus von Frau Lindau", 70, 40, beim("haus", "Haus"), fill=GRUEN, size=38),
    ficon("ph", "paint-roller", 330, 470, 110, beim("haus", "Fassade"), fuell=GELB),
    pl("Fassade", 330, 495, beim("haus", "Fassade"), fill=WEISS, size=30, anker="m"),
    pl("Garage?", 700, 590, beim("garage", "Garage"), fill=WEISS, size=30, anker="m"),
    *fig("LI", LIX, BODEN_Y, FHA, [(beim("haus", "Lindau"), "ruhig"), ("zahlt", "aerger")], bis="li1"),
    *redet("LI_redet", LIX, BODEN_Y, FHA, "li1", "dr1"),
    *fig("LI", LIX, BODEN_Y, FHA, [("dr1", "aerger")], erst="cut"),
    ns("Frau Lindau", LIX, BODEN_Y, beim("haus", "Lindau"), NFARBE["LI"]),
    ficon("tabler", "file-invoice", 960, 760, 110, "rechnung", fuell=WEISS),
    pl("Rechnung: 10.000 €", 960, 530, beim("rechnung", "zehntausend"), fill=GELB, size=30, anker="m"),
    pl("zahlt nichts", 960, 450, beim("zahlt", "zahlt"), fill=HELLROT, size=30, anker="m"),
    blase("sprech", 820, 230, "li1", 1180, 200, inhalt=["Die Fassade ist fleckig,", "und die Garage habe",
                                                      "ich nie bestellt!"], textsize=34,
          figur=("LI_redet", LIX, BODEN_Y, FHA), bis="dr1"),
    blase("sprech", 620, 190, "dr1", 820, 210, inhalt=["Dann sehen wir uns", "vor Gericht."], textsize=36,
          figur=("DR_redet_r", DRX, BODEN_Y, FHA), bis="klage"),
])

# ===========================================================================================================================
# B Fall: im Amtsgericht
# ===========================================================================================================================
RIX, RIU, RIH = 960, 640, 380
DRB, LIB = 330, 1590
akte = szene(bewegt(ficon("tabler", "file-text", 800, 562, 70, "klage", fuell=WEISS), "klage", ("klage", 0.35), 0, -70),
             "195akte*", 1.0, versatz=0.3)
folie([("klage", "Fall · Die Klage: 10.000 € Werklohn"), ("beweis", "Fall · Nach der Beweisaufnahme"),
       ("ri1", "Fall · Das Urteil in der Hauptsache"), ("frage", "Fall · 10.000 € verlangt, 7.300 € bekommen"),
       ("frage2", "Fall · Wer trägt die Kosten?")], [
    boden("klage"),
    hart(pl("Amtsgericht · Sitzungssaal", 70, 40, "klage", fill=GRAU, size=36)),
    *fig("RI", RIX, RIU, RIH, [("klage", "ruhig")], erst="cut", bis="ri1"),
    *redet("RI_redet", RIX, RIU, RIH, "ri1", "frage"),
    *fig("RI", RIX, RIU, RIH, [("frage", "denkt")], erst="cut"),
    hart(fl_block(740, 560, 440, 110, DUNKEL, "klage", [("Gericht", "Bold", 32, WEISS)], rand=5)),
    hart(pl("Richterin", RIX, 690, "klage", fill=LILA, size=28, anker="m")),
    akte,
    *fig("DR", DRB, BODEN_Y, FHA, [("klage", "ruhig_r"), ("beweis2", "sorge_r"), ("frage2", "denkt_r")], erst="cut"),
    hart(ns("Kläger: Herr Dressler", DRB, BODEN_Y, "klage", NFARBE["DR"])),
    *fig("LI", LIB, BODEN_Y, FHA, [("klage", "ruhig"), (beim("beweis", "Fassade"), "sorge"), ("beweis2", "froh"),
                                   ("ri1", "sorge"), ("frage2", "denkt")], erst="cut"),
    hart(ns("Beklagte: Frau Lindau", LIB, BODEN_Y, "klage", NFARBE["LI"])),
    pl("Klage: 10.000 € Werklohn", DRB, 300, beim("klage", "zehntausend"), fill=GELB, size=30, anker="m", bis="frage"),
    pl("Fassade: in Ordnung", LIB, 300, beim("beweis", "Fassade"), fill=GRUEN, size=30, anker="m", bis="frage"),
    pl("Garage: kein Auftrag bewiesen", DRB + 40, 380, beim("beweis2", "Auftrag"), fill=HELLROT, size=28, anker="m",
       bis="frage"),
    blase("sprech", 880, 210, "ri1", 1250, 125, inhalt=["Die Beklagte wird verurteilt, an den", "Kläger 7.300 € zu zahlen. Im Übrigen",
                                                       "wird die Klage abgewiesen."], textsize=32,
          figur=("RI_redet", RIX, RIU, RIH), bis="frage"),
    pl("verlangt: 10.000 €", 960, 40, "frage", fill=WEISS, size=34, anker="m"),
    pl("bekommen: 7.300 €", 960, 110, beim("frage", "siebentausend"), fill=GRUEN, size=34, anker="m"),
    pl("Wer trägt die Kosten des Rechtsstreits?", 960, 180, "frage2", fill=PINK, size=36, anker="m"),
])

# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_195(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_195("sv", [
    "Malermeister Herr Dressler streicht im April 2026 die Fassade am Haus von Frau Lindau. Nach seiner Darstellung hat sie "
    "auch den Anstrich ihrer Garage bestellt. Er stellt 10.000 Euro in Rechnung: 7.300 Euro für die Fassade, 2.700 Euro "
    "für die Garage.",
    "Frau Lindau zahlt nichts: Die Fassade sei fleckig, die Garage habe sie nie bestellt. Herr Dressler klagt vor dem "
    "Amtsgericht auf Zahlung von 10.000 Euro Werklohn; Zinsen verlangt er nicht.",
    "Nach der Beweisaufnahme steht fest: Die Fassade ist mangelfrei, der Werklohn dafür ist fällig. Einen Auftrag für die "
    "Garage kann Herr Dressler nicht beweisen. Das Gericht verurteilt Frau Lindau zur Zahlung von 7.300 Euro und weist "
    "die Klage im Übrigen ab.",
], "Wer trägt die Kosten des Rechtsstreits, und wie lautet der Kostentenor?")

# ===========================================================================================================================
# D Grundsatz: § 91 Abs. 1 S. 1 ZPO
# ===========================================================================================================================
PG = "Grundsatz"
W91 = ("„Die unterliegende Partei hat die Kosten des Rechtsstreits zu tragen, insbesondere die dem Gegner erwachsenen "
       "Kosten zu erstatten, soweit sie zur zweckentsprechenden Rechtsverfolgung oder Rechtsverteidigung notwendig waren. …“")
w91, w91_y = wortlaut(80, 165, 1100, W91, "§ 91 Abs. 1 S. 1 ZPO", "p91", marken=[
    ("unterliegende Partei", beim("p91", "unterliegende")), ("Kosten des Rechtsstreits", beim("p91", "Kosten")),
    ("dem Gegner erwachsenen", beim("umf", "Gegners")), ("notwendig waren.", beim("umf", "notwendigen"))], size=30)
folie([("p91", f"{PG} · § 91 Abs. 1 S. 1 ZPO"), ("unterl", f"{PG} › Unterliegensprinzip"),
       ("umf", f"{PG} › Gerichtskosten und notwendige Kosten des Gegners"), ("hier91", f"{PG} › hier: keiner hat ganz verloren")],
      rechts_frei([
    *tafel("p91", "Der Grundsatz: § 91 Abs. 1 S. 1 ZPO"),
    *w91,
    blk(110, w91_y + 26, 1040, 80, GELB, "unterl", [("Unterliegensprinzip: Wer verliert, zahlt.", "ExtraBold", 34, INK)]),
    z("Dazu gehören:", 110, w91_y + 135, "umf", "Bold", 32),
    *okz("die Gerichtskosten", w91_y + 185, beim("umf", "Gerichtskosten"), "Bold", 32, x=170),
    *okz("die notwendigen Kosten des Gegners, z. B. Anwalt", w91_y + 240, beim("umf", "notwendigen"), "Bold", 32, x=170),
    zit("Anwaltskosten: § 91 Abs. 2 S. 1 ZPO", 170, w91_y + 288, beim("umf", "Anwalt")),
    blk(110, w91_y + 345, 1040, 80, HELLROT, "hier91", [("Hier: Keiner hat ganz verloren.", "ExtraBold", 34, INK)]),
    *requisit([("p91", ("tabler", "scale", 100, WEISS), "Wer verliert?", WEISS),
               ("umf", ("tabler", "receipt-euro", 100, GELB), "Kosten", GELB),
               ("hier91", ("tabler", "chart-pie", 100, WEISS), "teils, teils", PINK)]),
    *zwei([("p91", "ruhig"), ("unterl", "froh"), ("hier91", "denkt")], [("p91", "denkt"), ("unterl", "sorge"), ("hier91", "ruhig")]),
]))
assert w91_y + 425 <= 890, w91_y

# ===========================================================================================================================
# E Teilunterliegen: § 92 Abs. 1 S. 1 ZPO
# ===========================================================================================================================
PT = "Teilunterliegen"
W92 = ("„Wenn jede Partei teils obsiegt, teils unterliegt, so sind die Kosten gegeneinander aufzuheben oder "
       "verhältnismäßig zu teilen. …“")
w92, w92_y = wortlaut(80, 175, 1100, W92, "§ 92 Abs. 1 S. 1 ZPO", "p92", marken=[
    ("teils obsiegt,", beim("p92", "teils")), ("teils unterliegt,", beim("p92", "teils", 2)),
    ("gegeneinander aufzuheben", beim("p92", "gegeneinander")), ("verhältnismäßig zu teilen.", beim("p92", "verhältnismäßig"))],
    size=34)
folie([("p92", f"{PT} · § 92 Abs. 1 S. 1 ZPO"), ("teilen", f"{PT} › Normalfall: Teilen nach Quote")], rechts_frei([
    *tafel("p92", "Teils gewonnen, teils verloren"),
    *w92,
    blk(110, w92_y + 40, 500, 130, GRUEN, "teilen", [("Normalfall:", "ExtraBold", 32, INK), ("Teilen nach Quote", "ExtraBold", 32, INK)]),
    blk(650, w92_y + 40, 500, 130, WEISS, beim("p92", "gegeneinander"), [("Alternative:", "Bold", 30, INK),
                                                                       ("Kostenaufhebung", "Bold", 30, INK)]),
    *requisit([("p92", ("tabler", "chart-pie", 100, WEISS), "teils, teils", WEISS),
               ("teilen", ("tabler", "calculator", 100, GRUEN), "Quote", GRUEN)]),
    *zwei([("p92", "denkt"), ("teilen", "ruhig")], [("p92", "ruhig"), ("teilen", "denkt")]),
]))
assert w92_y + 190 <= 890, w92_y

# ===========================================================================================================================
# F Die Quote rechnen
# ===========================================================================================================================
PQ = "Kostenquote"
BX, BY, BW, BH = 110, 245, 1040, 64
folie([("rech", f"{PQ} · rechnen"), ("r1", f"{PQ} › Streitwert: 10.000 €"), ("r2", f"{PQ} › Kläger verliert 2.700 €"),
       ("r3", f"{PQ} › 2.700 € : 10.000 € = 27 %"), ("r5", f"{PQ} › Beklagte verliert 7.300 €: 73 %"),
       ("basis", f"{PQ} › Unterliegen gemessen am Streitwert")], rechts_frei([
    *tafel("rech", "Die Kostenquote rechnen"),
    z("verlangt = Streitwert: 10.000 €", 110, 175, "r1", "Bold", 34),
    *balken(BX, BY, BW, BH, [(0.73, 0.27, ROT, beim("r2", "zweitausendsiebenhundert"), "2.700 €"),
                             (0.0, 0.73, GELB, beim("r5", "siebentausenddreihundert"), "7.300 €")], "r1"),
    z("Kläger verliert:", 110, 345, beim("r2", "zweitausendsiebenhundert"), "Bold", 32),
    z("2.700 € (Garage)", 110, 390, beim("r2", "zweitausendsiebenhundert"), "ExtraBold", 34),
    z("Beklagte verliert:", 650, 345, beim("r5", "siebentausenddreihundert"), "Bold", 32),
    z("7.300 € (Fassade)", 650, 390, beim("r5", "siebentausenddreihundert"), "ExtraBold", 34),
    z("2.700 € : 10.000 € = 27 %", 110, 470, "r3", "ExtraBold", 40),
    blk(110, 560, 500, 90, BLAU, "r4", [("Kläger: 27 %", "ExtraBold", 36, INK)]),
    blk(650, 560, 500, 90, GELB, beim("r5", "dreiundsiebzig"), [("Beklagte: 73 %", "ExtraBold", 36, INK)]),
    blk(110, 700, 1040, 90, HELL, "basis", [("Quote = Unterliegen : Streitwert", "ExtraBold", 36, INK)]),
    *requisit([("rech", ("tabler", "calculator", 100, WEISS), "Quote", WEISS),
               (beim("r2", "zweitausendsiebenhundert"), ("ph", "garage", 130, HELLROT), "Garage: verloren", HELLROT),
               ("r3", ("tabler", "percentage", 100, BLAU), "27 %", BLAU),
               ("dr2", None, None, None),
               ("r5", ("ph", "house", 130, GELB), "Fassade: verloren", GELB),
               ("basis", ("tabler", "chart-pie", 100, WEISS), "27 % zu 73 %", WEISS)]),
    *fig("DR", X1, FB, FR, [("rech", "ruhig"), (beim("r2", "zweitausendsiebenhundert"), "sorge"), ("r4", "skeptisch")], bis="dr2"),
    *redet("DR_fragt", X1, FB, FR, "dr2", "r5"),
    *fig("DR", X1, FB, FR, [("r5", "denkt"), ("basis", "ruhig")], erst="cut"),
    ns(NAME["DR"], X1, FB, "rech", NFARBE["DR"], d=0.1),
    *fig("LI", X2, FB, FR, [("rech", "ruhig"), ("r5", "sorge")]),
    ns(NAME["LI"], X2, FB, "rech", NFARBE["LI"], d=0.1),
    blase("sprech", 560, 200, "dr2", 1560, 220, inhalt=["Ich zahle mit, obwohl", "ich gewonnen habe?"], textsize=34,
          figur=("DR_fragt", X1, FB, FR), bis="r5"),
]))

# ===========================================================================================================================
# G Prozent oder Bruch, Kostentenor
# ===========================================================================================================================
PK = "Kostentenor"
folie([("bruch", f"{PK} · Prozent oder Bruch?"), ("bruch2", f"{PK} › hier: Prozent"), ("tenor", f"{PK} › Formulierung")],
      rechts_frei([
    *tafel("bruch", "Prozent oder Bruch?"),
    blk(110, 175, 500, 90, WEISS, beim("bruch", "Prozent"), [("Prozent", "ExtraBold", 34, INK)]),
    blk(650, 175, 500, 90, WEISS, beim("bruch", "Bruch"), [("Bruch", "ExtraBold", 34, INK)]),
    *okz("Bruch üblich bei glatten Anteilen: ¼ zu ¾", 295, beim("bruch", "glatten"), "Bold", 32, x=170),
    zit("z. B. OLG Hamm, Urt. v. 20.12.2007 – 24 U 53/06 (Tenor: ¼ und ¾)", 170, 345, beim("bruch", "glatten")),
    *neinz("27/100: schwer lesbar", 400, "bruch2", "Bold", 32, x=170),
    *okz("hier: Prozent", 455, beim("bruch2", "Prozent"), "ExtraBold", 32, x=170),
    pl("Kostentenor", 110, 535, "tenor", fill=GELB, size=30),
    blk(110, 600, 1040, 150, HELL, "tenor", [("„Von den Kosten des Rechtsstreits tragen", "ExtraBold", 34, INK),
                                             ("der Kläger 27 % und die Beklagte 73 %.“", "ExtraBold", 34, INK)]),
    zit("Tenor in Prozent z. B. OLG Hamm, Beschl. v. 19.10.2021 – 7 W 11/21", 110, 765, "tenor"),
    *requisit([("bruch", ("tabler", "percentage", 100, WEISS), "Prozent", WEISS),
               (beim("bruch", "Bruch"), ("tabler", "math-x-divide-y", 100, WEISS), "Bruch", WEISS),
               ("bruch2", ("tabler", "percentage", 100, BLAU), "27 % / 73 %", BLAU),
               ("tenor", ("tabler", "file-text", 100, GELB), "Tenor", GELB)]),
    *zwei([("bruch", "denkt"), ("tenor", "ruhig")], [("bruch", "ruhig"), ("tenor", "sorge")]),
]))

# ===========================================================================================================================
# H Kostenaufhebung: § 92 Abs. 1 S. 1 Alt. 1, S. 2 ZPO
# ===========================================================================================================================
PA = "Kostenaufhebung"
W922 = "„Sind die Kosten gegeneinander aufgehoben, so fallen die Gerichtskosten jeder Partei zur Hälfte zur Last.“"
w922, w922_y = wortlaut(80, 245, 1100, W922, "§ 92 Abs. 1 S. 2 ZPO", "aufh2", marken=[
    ("Gerichtskosten", beim("aufh2", "Gerichtskosten")), ("zur Hälfte", beim("aufh2", "Hälfte"))], size=34)
folie([("aufh", f"{PA} · § 92 Abs. 1 S. 1 Alt. 1 ZPO"), ("aufh2", f"{PA} › § 92 Abs. 1 S. 2 ZPO"),
       ("aufh3", f"{PA} › wenn beide etwa zur Hälfte gewinnen")], rechts_frei([
    *tafel("aufh", "Alternative: Kosten gegeneinander aufheben"),
    z("statt teilen: die Kosten gegeneinander aufheben", 110, 175, "aufh", "Bold", 32),
    *w922,
    *okz("eigene Anwaltskosten trägt jede Partei selbst", w922_y + 40, beim("aufh2", "Anwaltskosten"), "Bold", 32, x=170),
    blk(110, w922_y + 130, 1040, 90, GELB, "aufh3", [("passt vor allem bei etwa hälftigem Gewinn", "ExtraBold", 34, INK)]),
    zit("Wilke, ZJS 2014, 363 (366)", 110, w922_y + 235, "aufh3"),
    *requisit([("aufh", ("ph", "scales", 110, WEISS), "aufheben", WEISS),
               (beim("aufh2", "Hälfte"), ("tabler", "building-bank", 100, WEISS), "Gerichtskosten: ½ und ½", WEISS),
               ("aufh3", ("tabler", "chart-pie", 100, GELB), "etwa 50 zu 50", GELB)]),
    *zwei([("aufh", "ruhig"), ("aufh3", "denkt")], [("aufh", "ruhig")], links="RI", rechts="DR"),
]))
assert w922_y + 280 <= 890, w922_y

# ===========================================================================================================================
# I Ausnahme: § 92 Abs. 2 ZPO
# ===========================================================================================================================
PX2 = "Ausnahme"
W92II = ("„Das Gericht kann der einen Partei die gesamten Prozesskosten auferlegen, wenn 1. die Zuvielforderung der anderen "
         "Partei verhältnismäßig geringfügig war und keine oder nur geringfügig höhere Kosten veranlasst hat …“")
w92ii, w92ii_y = wortlaut(80, 215, 1100, W92II, "§ 92 Abs. 2 Nr. 1 ZPO", "nr1", marken=[
    ("gesamten Prozesskosten", beim("nr1", "gesamten")), ("verhältnismäßig geringfügig", beim("nr1", "verhältnismäßig")),
    ("keine oder nur geringfügig", beim("nr1", "keine"))], size=30)
folie([("p922", f"{PX2} · § 92 Abs. 2 ZPO"), ("nr1", f"{PX2} › Nr. 1: geringfügige Zuvielforderung"),
       ("beide", f"{PX2} › Nr. 1: beides muss vorliegen"), ("faust", f"{PX2} › Faustregel: bis etwa 10 %"),
       ("nicht", f"{PX2} › hier 27 %: nicht geringfügig"), ("nr2", f"{PX2} › Nr. 2: Ermessen, Sachverständige, Berechnung")],
      rechts_frei([
    *tafel("p922", "§ 92 Abs. 2 ZPO: alle Kosten auf eine Seite?"),
    z("Kann der Kläger die Kosten ganz loswerden?", 110, 165, "p922", "Bold", 32),
    *w92ii,
    pl("beides muss vorliegen", 110, w92ii_y + 14, "beide", fill=PINK, size=28),
    zit("AG Königs Wusterhausen, 13.4.2023 – 4 C 4468/22", 480, w92ii_y + 24, "beide"),
    *skala(130, w92ii_y + 150, 760, 44, beim("faust", "Faustregel"), 10, 30, beim("nicht", "Siebenundzwanzig"), 27, "hier: 27 %"),
    pl("Faustregel (Literatur): bis etwa 10 %", 110, w92ii_y + 80, beim("faust", "Faustregel"), fill=GRUEN, size=28, bis="nicht"),
    zit("Wilke, ZJS 2014, 363 (367) m. w. N.", 690, w92ii_y + 90, beim("faust", "Faustregel"), bis="nicht"),
    *neinz("27 %: Abs. 2 hilft Herrn Dressler nicht", w92ii_y + 265, beim("nicht", "Absatz"), "ExtraBold", 32, x=170),
    z("Nr. 2: Höhe hing ab von richterlichem Ermessen,", 110, w92ii_y + 330, "nr2", "Bold", 30),
    z("Sachverständigen oder gegenseitiger Berechnung", 150, w92ii_y + 372, "nr2", "Bold", 30),
    *requisit([("p922", ("ph", "scales", 110, WEISS), "alle Kosten?", WEISS),
               ("faust", ("tabler", "percentage-10", 100, GRUEN), "bis etwa 10 %", GRUEN),
               ("nicht", ("tabler", "percentage", 100, HELLROT), "27 %", HELLROT),
               ("nr2", ("tabler", "zoom-question", 100, WEISS), "Nr. 2", WEISS)]),
    *zwei([("p922", "skeptisch"), ("faust", "denkt"), ("nicht", "sorge")], [("p922", "ruhig"), ("nicht", "froh"), ("nr2", "ruhig")]),
]))
assert w92ii_y + 420 <= 900, w92ii_y

# ===========================================================================================================================
# J Vier Sonderregeln
# ===========================================================================================================================
PS_ = "Sonderregeln"
KARTEN = [
    ("p93", "§ 93 ZPO",
     "„Hat der Beklagte nicht durch sein Verhalten zur Erhebung der Klage Veranlassung gegeben, so fallen dem Kläger die "
     "Prozesskosten zur Last, wenn der Beklagte den Anspruch sofort anerkennt.“",
     [("nicht durch sein Verhalten", beim("p93", "keinen")), ("sofort anerkennt.", beim("p93", "sofort")),
      ("dem Kläger die", beim("p93", "trägt"))],
     "sofortiges Anerkenntnis: Der Kläger trägt die Kosten."),
    ("p91a", "§ 91a Abs. 1 S. 1 ZPO",
     "„Haben die Parteien … den Rechtsstreit in der Hauptsache für erledigt erklärt, so entscheidet das Gericht über die "
     "Kosten unter Berücksichtigung des bisherigen Sach- und Streitstandes nach billigem Ermessen durch Beschluss.“",
     [("für erledigt", beim("p91a", "erledigt")), ("billigem Ermessen", beim("p91a", "billigem"))],
     "Erledigung: Kosten nach billigem Ermessen"),
    ("p269", "§ 269 Abs. 3 S. 2 ZPO",
     "„Der Kläger ist verpflichtet, die Kosten des Rechtsstreits zu tragen, soweit nicht bereits rechtskräftig über sie "
     "erkannt ist oder sie dem Beklagten aus einem anderen Grund aufzuerlegen sind.“",
     [("Der Kläger ist verpflichtet,", beim("p269", "Kläger")), ("die Kosten des Rechtsstreits zu tragen,", beim("p269", "trägt"))],
     "Klagerücknahme: grundsätzlich zahlt der Kläger"),
    ("p344", "§ 344 ZPO",
     "„Ist das Versäumnisurteil in gesetzlicher Weise ergangen, so sind die durch die Versäumnis veranlassten Kosten, … "
     "der säumigen Partei auch dann aufzuerlegen, wenn infolge des Einspruchs eine abändernde Entscheidung erlassen wird.“",
     [("in gesetzlicher Weise", beim("p344", "gesetzlicher")), ("der säumigen Partei", beim("p344", "säumige")),
      ("abändernde Entscheidung", beim("p344", "gewinnt"))],
     "Säumnis: Die säumige Partei zahlt die Säumniskosten."),
]
# Kernsatz erst zum gesprochenen Schlüsselwort
KERN_CUE = {"p93": beim("p93", "trägt"), "p91a": beim("p91a", "billigem"), "p269": beim("p269", "trägt"),
            "p344": beim("p344", "säumige")}
els_j = [*tafel("sonder", "Vier Sonderregeln")]
PILLX = [110, 290, 520, 860]
for i, (c, norm, _, _, _) in enumerate(KARTEN):
    kurz = norm.replace(" ZPO", "").replace(" Abs. 1 S. 1", "")
    els_j.append(pl(kurz, PILLX[i], 172, "sonder", fill=WEISS, size=30, bis=c))
    els_j.append(hart(pl(kurz, PILLX[i], 172, c, fill=GELB, size=30)))
for i, (c, norm, text, marken, kern) in enumerate(KARTEN):
    nxt = KARTEN[i + 1][0] if i + 1 < len(KARTEN) else None
    w_, wy = wortlaut(80, 260, 1100, text, norm, c, marken=marken, size=30, bis=nxt)
    els_j += w_
    els_j.append(bis_(blk(110, wy + 30, 1040, 86, HELL, KERN_CUE[c], [(kern, "ExtraBold", 32, INK)]), nxt))
    assert wy + 120 <= 830, (c, wy)
els_j.append(pl("mehr dazu: Video zum Versäumnisurteil", 110, 830, "vu", fill=PINK, size=28))
els_j += requisit([("sonder", ("tabler", "list-check", 100, WEISS), "4 Sonderregeln", WEISS),
                   ("p93", ("ph", "handshake", 120, GELB), "Anerkenntnis", GELB),
                   ("p91a", ("tabler", "circle-check", 100, GRUEN), "Erledigung", GRUEN),
                   ("p269", ("tabler", "arrow-back-up", 100, WEISS), "Rücknahme", WEISS),
                   ("p344", ("ph", "chair", 110, BLAU), "Säumnis", BLAU)])
els_j += zwei([("sonder", "ruhig"), ("p91a", "denkt"), ("p344", "ruhig")], [("sonder", "denkt"), ("p93", "ruhig"), ("p269", "denkt")],
              links="RI", rechts="LI")
folie([("sonder", f"{PS_} · vier Fälle"), ("p93", f"{PS_} › § 93: sofortiges Anerkenntnis"),
       ("p91a", f"{PS_} › § 91a: Erledigung der Hauptsache"), ("p269", f"{PS_} › § 269 Abs. 3 S. 2: Klagerücknahme"),
       ("p344", f"{PS_} › § 344: Versäumniskosten")], rechts_frei(els_j))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
W308 = "„Über die Verpflichtung, die Prozesskosten zu tragen, hat das Gericht auch ohne Antrag zu erkennen.“"
w308, w308_y = wortlaut(130, 290, 1040, W308, "§ 308 Abs. 2 ZPO", "tipp2", marken=[("auch ohne Antrag", beim("tipp2", "ohne"))],
                        size=34)
folie([("tipp", "Klausurtipp · Kostentenor nie vergessen"), ("tipp2", "Klausurtipp › § 308 Abs. 2 ZPO"),
       ("tipp3", "Klausurtipp › danach: vorläufige Vollstreckbarkeit")], [
    *tafel("tipp", "Klausurtipp: der Kostentenor", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Vergiss den Kostentenor nie!", 200, 200, beim("tipp", "Vergiss"), "ExtraBold", 36),
    *w308,
    blk(130, w308_y + 40, 1020, 120, GELB, "tipp3", [("danach: vorläufige Vollstreckbarkeit", "ExtraBold", 32, INK),
                                                    ("§§ 708 ff. ZPO – ein eigenes Thema", "Bold", 30, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])
assert w308_y + 170 <= 890

# ===========================================================================================================================
# L Schema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", 0, "1. Grundsatz (§ 91 Abs. 1 S. 1 ZPO)"), (beim("k1", "Wer"), 1, "Wer verliert, trägt die Kosten."),
          ("k2", 0, "2. Teilunterliegen (§ 92 Abs. 1 S. 1 ZPO)"), (beim("k2", "Quote"), 1, "Quote = Unterliegen : Streitwert"),
          ("k3", 0, "3. Ausnahme (§ 92 Abs. 2 ZPO)"),
          ("k4", 0, "4. Sonderregeln (§§ 93, 91a, 269 Abs. 3 S. 2, 344 ZPO)"),
          ("k5", 0, "5. Kostentenor"), (beim("k5", "Kostentenor"), 1, "„Von den Kosten des Rechtsstreits tragen …“")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: die Kostenentscheidung"), 110, 90, "sch", 50)]
y = 210
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (40, 36)[ebene], rechts=1800, farbe=(INK, TEXT)[ebene]))
    y += {0: 80, 1: 92}[ebene]
assert y <= 960, y
folie([("sch", "Schema"), ("k1", "Schema › 1. Grundsatz"), ("k2", "Schema › 2. Teilunterliegen: Quote"),
       ("k3", "Schema › 3. Ausnahme, § 92 Abs. 2"), ("k4", "Schema › 4. Sonderregeln"), ("k5", "Schema › 5. Kostentenor")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Kosten folgen dem ", 0), ("Unterliegen", "a"), (".", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "Unterliegen")}),
    *markertext([[("Wer teils gewinnt und teils verliert,", 0)], [("zahlt nach ", 0), ("Quote", "b"), (":", 0)],
                 [("verlorener Betrag durch ", 0), ("Streitwert", "c"), (".", 0)]], 750, 450, 46, "m2",
                {"b": beim("m2", "Quote"), "c": beim("m2", "Streitwert")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
