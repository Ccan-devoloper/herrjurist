"""Folge 245 · Leistungskondiktion § 812 I 1 Alt. 1 BGB – Prüfungsschema · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Frau Heidkamp hat Mila ihr gebrauchtes Klavier schriftlich für 2.400 € angeboten (vertippt, gemeint 4.200 €),
Mila nimmt an, zahlt beim Abholen bar, Frau Heidkamp zahlt die Scheine auf ihr Konto ein. Eine Woche später klingelt
Frau Heidkamp bei Mila und ficht an (§ 119 Abs. 1 Alt. 2, § 142 Abs. 1 BGB). Mila will ihr Geld zurück, Frau Heidkamp das
Klavier. Danach: § 812 Abs. 1 Satz 1 BGB (Wortlautkarte), 1. etwas erlangt, 2. durch Leistung, 3. ohne rechtlichen Grund,
4. kein Ausschluss (Wortlautkarten § 814, § 817 Satz 2), Rechtsfolge (Wortlautkarte § 818 Abs. 1, 2; Abs. 3 ein Satz),
Saldotheorie, Abgrenzung condictio ob rem, Ergebnis, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 229 (gemeinsame Dateien unverändert); neu: klavier(), fenster(), wohnzimmer(), handy(), stube().
Keine echte Instrumentenmarke: das Klavier ist aus Grundformen gezeichnet, ohne Schriftzug.
Handlungsgeräusche: Türklingel (A1) und Geldscheine (A2); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_245/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_245/" in n:
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
NAME = {"MI": "Mila", "HK": "Frau Heidkamp"}
NFARBE = {"MI": TUERKIS, "HK": LILA}


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


def tuer(x, cue, farbe=HOLZ, w=190, h=380):
    """Wohnungstür aus Grundformen (Rahmen, Blatt, Klinke) auf dem Boden."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
    dr.rounded_rectangle((o + 22 * s, o + 26 * s, o + (w - 22) * s, o + 160 * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + 22 * s, o + 190 * s, o + (w - 22) * s, o + (h - 26) * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + 18 * s, o + 176 * s, o + 52 * s, o + 188 * s), 4 * s, fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="tuer"))


_KL = {}


def _klavier_bild(w, h):
    """Aufrechtes Klavier aus Grundformen (Gehäuse, Deckel, Notenpult, Tastatur, Füße), ohne Marke und Schriftzug."""
    if (w, h) in _KL:
        return _KL[(w, h)]
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s; S = lambda v: o + int(v * s)
    lw = max(2, int(w / 92)) * s
    dr.rounded_rectangle((S(0), S(0), S(w), S(h * 0.07)), 6 * s, fill=DUNKELHOLZ, outline=INK, width=lw)        # Deckel
    dr.rounded_rectangle((S(w * 0.03), S(h * 0.06), S(w * 0.97), S(h * 0.93)), 8 * s, fill=HOLZ, outline=INK, width=lw)  # Korpus
    dr.rounded_rectangle((S(w * 0.10), S(h * 0.14), S(w * 0.90), S(h * 0.42)), 6 * s, fill=(232, 190, 140, 255), outline=INK,
                         width=max(1, lw // 2))                                                              # Füllung oben
    dr.rounded_rectangle((S(w * 0.30), S(h * 0.38), S(w * 0.70), S(h * 0.47)), 4 * s, fill=DUNKELHOLZ, outline=INK,
                         width=max(1, lw // 2))                                                              # Notenpult
    ky0, ky1 = h * 0.50, h * 0.62
    dr.rectangle((S(w * 0.0), S(h * 0.47), S(w), S(ky0)), fill=DUNKELHOLZ, outline=INK, width=lw)            # Tastenklappe
    dr.rectangle((S(w * 0.02), S(ky0), S(w * 0.98), S(ky1)), fill=WEISS, outline=INK, width=lw)               # Tastatur
    n = 22
    for i in range(1, n):
        xx = w * 0.02 + (w * 0.96) * i / n
        dr.line((S(xx), S(ky0), S(xx), S(ky1)), fill=INK, width=max(1, lw // 2))
    for i in range(n):
        if i % 7 in (2, 6):
            continue
        xx = w * 0.02 + (w * 0.96) * (i + 1) / n
        dr.rectangle((S(xx - w * 0.012), S(ky0), S(xx + w * 0.012), S(ky0 + (ky1 - ky0) * 0.6)), fill=INK)
    dr.rectangle((S(w * 0.0), S(ky1), S(w), S(h * 0.66)), fill=DUNKELHOLZ, outline=INK, width=lw)             # Leiste
    dr.rounded_rectangle((S(w * 0.10), S(h * 0.70), S(w * 0.90), S(h * 0.88)), 6 * s, fill=(232, 190, 140, 255), outline=INK,
                         width=max(1, lw // 2))                                                              # Füllung unten
    for fx in (0.06, 0.88):
        dr.rounded_rectangle((S(w * fx), S(h * 0.92), S(w * fx + w * 0.06), S(h)), 3 * s, fill=DUNKELHOLZ, outline=INK, width=lw)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    _KL[(w, h)] = im
    return im


def klavier(x, w, cue, h=None, unten=BODEN, anim="cut", bis=None):
    h = h or int(w * 0.92)
    return El(_klavier_bild(w, h), x, unten - h - 6, cue, anim, 0.0, bis, name="klavier")


def fenster(x, y, w, h, cue):
    """Fenster mit Sprossen (Tageslicht)."""
    return [hart(feld(x, y, w, h, cue, fill=BLAUHELL, rand=5, rund=8, name="fenster")),
            hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")),
            hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2"))]


# Wohnzimmer bei Mila (A1, A3, Ergebnis): Fenster, Sessel, Klavier links, Tür rechts
MIX, HKX = 1180, 1600                       # Mila, Frau Heidkamp in der Fallszene
KLX, KLW = 470, 470                         # Klavier


def wohnzimmer(cue, fy=250):
    return [boden(cue), *fenster(110, fy, 280, 240, cue),
            ficon("tabler", "armchair", 250, BODEN, 230, cue, fuell=LILA, anim="cut"),
            hart(klavier(KLX, KLW, cue)), tuer(1690, cue)]


# ===========================================================================================================================
# A1 Fall: Mila im Wohnzimmer mit dem Klavier – Frau Heidkamp klingelt und ficht an
# ===========================================================================================================================
folie([(NULL, "Fall · Bei Mila im Wohnzimmer"), ("klingel", "Fall · Frau Heidkamp klingelt"),
       ("h1", "Fall · „Vertippt: 4.200 € statt 2.400 €“"), ("m1", "Fall · Mila hat schon bezahlt")], [
    *wohnzimmer(NULL),
    hart(pl("Bei Mila im Wohnzimmer", 70, 30, NULL, fill=GELB, size=32)),
    pl("seit einer Woche", KLX + KLW // 2, 300, "klavier", fill=WEISS, size=30, anker="m", bis="h1"),
    *fig("MI", MIX, BODEN, FH, [(NULL, "froh"), ("klingel", "staunt_r"), ("h1", "sorge_r")], bis="m1", erst="cut"),
    *redet("MI_sorgt_r", MIX, BODEN, FH, "m1", "rueck"),
    hart(ns(NAME["MI"], MIX, BODEN, NULL, TUERKIS)),
    szene(ficon("tabler", "bell-ringing", 1785, 420, 76, "klingel", fuell=GELB, bis="h1"), "245klingel*", 0.8, 0.0),
    *fig("HK", HKX, BODEN, FH, [("klingel", "ruhig")], bis="h1", erst="pop"),
    *redet("HK_redet", HKX, BODEN, FH, "h1", "m1"),
    *fig("HK", HKX, BODEN, FH, [("m1", "sorge")], erst="cut"),
    ns(NAME["HK"], HKX, BODEN, "klingel", LILA, d=0.1),
    blase("sprech", 720, 250, "h1", 1290, 210, inhalt=["Ich habe mich in meinem Angebot", "vertippt: Das Klavier sollte 4.200 €",
                                                     "kosten, nicht 2.400. Ich fechte", "den Kauf an."], textsize=30,
          figur=("HK_redet", HKX, BODEN, FH), bis="m1"),
    blase("sprech", 560, 160, "m1", 1080, 250, inhalt=["Aber ich habe doch", "schon bezahlt!"], textsize=34,
          figur=("MI_sorgt_r", MIX, BODEN, FH)),
])


# ===========================================================================================================================
# A2 Rückblick: bei Frau Heidkamp – das Angebot per Nachricht, Zusage, Barzahlung, Einzahlung
# ===========================================================================================================================
HKX2, MIX2 = 760, 1660


def handy(x, y, cue, bis=None):
    """Smartphone mit der Nachricht von Frau Heidkamp (Rahmen aus Grundformen, Text = gesprochener Inhalt)."""
    w, h = 430, 470
    els = [bis_(feld(x, y, w, h, cue, fill=INK, rand=4, rund=40, anim="pop", name="handy"), bis),
           bis_(feld(x + 18, y + 40, w - 36, h - 80, cue, fill=WEISS, rand=2, rund=16, anim="pop", name="display"), bis),
           bis_(z("Frau Heidkamp", x + 44, y + 60, cue, "ExtraBold", 28, rechts=x + w - 20), bis),
           bis_(feld(x + 36, y + 110, w - 84, 150, cue, fill=LILAHELL, rand=3, rund=18, anim="pop", name="nachricht"), bis)]
    for i, t in enumerate(["Sie können das", "Klavier für 2.400 €", "haben."]):
        els.append(bis_(z(t, x + 56, y + 132 + i * 40, cue, "Bold", 30, rechts=x + w - 60), bis))
    return els


def stube(cue):
    """Wohnstube bei Frau Heidkamp (Rückblick): Klavier links, Bild an der Wand, Stehlampe."""
    return [boden(cue), hart(klavier(120, 430, cue)),
            ficon("tabler", "photo", 300, 330, 220, cue, fuell=GELB, anim="cut"),
            ficon("tabler", "plant-2", 470, BODEN - 402, 90, cue, fuell=GRUEN, anim="cut")]


folie([("rueck", "Rückblick · Zwei Wochen vorher bei Frau Heidkamp"), ("angebot", "Rückblick · Das Angebot: 2.400 €"),
       ("zusage", "Rückblick · Mila sagt sofort zu"), ("bar", "Rückblick · Mila zahlt bar"),
       ("konto", "Rückblick · Die Scheine kommen aufs Konto")], [
    *stube("rueck"),
    hart(pl("Zwei Wochen vorher", 70, 30, "rueck", fill=GELB, size=32)),
    *fig("HK", HKX2, BODEN, FH, [("rueck", "tippt_r"), ("zusage", "froh_r"), ("konto", "ruhig_r")], erst="pop"),
    ns(NAME["HK"], HKX2, BODEN, "rueck", LILA, d=0.1),
    ficon("tabler", "device-mobile", HKX2 + 70, 660, 50, "rueck", fuell=WEISS, bis="zusage"),     # Handy in der Hand
    *handy(1230, 110, "angebot", bis="bar"),
    *okz("Mila sagt sofort zu", 600, "zusage", "Bold", 32, x=1310, rechts=1880, bis="bar"),
    *fig("MI", MIX2, BODEN, FH, [("bar", "froh")], erst="pop"),
    ns(NAME["MI"], MIX2, BODEN, "bar", TUERKIS, d=0.1),
    szene(ficon("tabler", "cash-banknote", 1210, 640, 150, beim("bar", "bar"), fuell=GRUEN, bis="konto"), "245scheine*", 0.8, 0.05),
    pl("2.400 € bar", 1210, 420, beim("bar", "bar"), fill=GRUEN, size=32, anker="m", bis="konto"),
    ficon("tabler", "cash-banknote", 1010, 330, 120, "konto", fuell=GRUEN),
    pfeil(1085, 300, 1260, 300, beim("konto", "Konto"), breite=8, kopf=26),
    ficon("tabler", "building-bank", 1350, 370, 150, beim("konto", "Konto"), fuell=BLAUHELL),
    pl("auf ihr Konto eingezahlt", 1180, 420, beim("konto", "Konto"), fill=BLAUHELL, size=30, anker="m"),
])


# ===========================================================================================================================
# A3 Zurück im Wohnzimmer: Geld zurück? Klavier zurück! – die Frage
# ===========================================================================================================================
folie([("mi2", "Fall · Mila will ihr Geld zurück"), ("h2", "Fall · Frau Heidkamp will ihr Klavier"),
       ("frage", "Die Frage · Geld zurück trotz nichtigem Kauf?"), ("frage2", "Die Frage · Und das Klavier?")], [
    *wohnzimmer("mi2", fy=290),
    hart(pl("Bei Mila im Wohnzimmer", 70, 30, "mi2", fill=GELB, size=32, bis="frage")),
    *redet("MI_redet_r", MIX, BODEN, FH, "mi2", "h2"),
    *fig("MI", MIX, BODEN, FH, [("h2", "denkt_r"), ("frage", "ernst_r")], erst="cut"),
    hart(ns(NAME["MI"], MIX, BODEN, "mi2", TUERKIS)),
    *fig("HK", HKX, BODEN, FH, [("mi2", "ernst")], bis="h2", erst="cut"),
    *redet("HK_fest", HKX, BODEN, FH, "h2", "frage"),
    *fig("HK", HKX, BODEN, FH, [("frage", "ruhig")], erst="cut"),
    hart(ns(NAME["HK"], HKX, BODEN, "mi2", LILA)),
    blase("sprech", 560, 190, "mi2", 1080, 240, inhalt=["Dann will ich meine", "2.400 € zurück."], textsize=34,
          figur=("MI_redet_r", MIX, BODEN, FH), bis="h2"),
    blase("sprech", 600, 230, "h2", 1310, 230, inhalt=["Die bekommen Sie. Aber nur,", "wenn ich mein Klavier",
                                                     "wiederbekomme."], textsize=32,
          figur=("HK_fest", HKX, BODEN, FH), bis="frage"),
    pl("Der Kaufvertrag ist nichtig, aber Mila hat schon bezahlt.", 70, 30, "frage", fill=WEISS, size=30),
    pl("Kann sie ihr Geld zurückverlangen?", 70, 104, beim("frage", "Kann"), fill=PINK, size=34),
    pl("Und muss sie dafür das Klavier hergeben?", 70, 184, "frage2", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_245(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=37, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_245("sv", [
    "Frau Heidkamp schreibt Mila: „Sie können das Klavier für 2.400 € haben.“ Gemeint hatte sie 4.200 €; sie hat sich "
    "vertippt. Mila sagt sofort zu.",
    "Beim Abholen zahlt Mila 2.400 € bar. Frau Heidkamp zahlt die Scheine noch am selben Tag auf ihr Konto ein. Von dem "
    "Tippfehler weiß Mila nichts.",
    "Eine Woche später bemerkt Frau Heidkamp den Fehler und ficht ihre Erklärung sofort gegenüber Mila an. Mila verlangt "
    "ihre 2.400 € zurück; Frau Heidkamp will dafür ihr Klavier wiederhaben.",
], "Kann Mila ihr Geld zurückverlangen, und muss sie dafür das Klavier hergeben?")


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
# C I. Anspruchsgrundlage: § 812 Abs. 1 Satz 1 BGB (Wortlautkarte), Schema
# ===========================================================================================================================
PI = "I. Anspruchsgrundlage"
w812, w812_y = wortlaut(80, 320, 1100, "„(1) Wer durch die Leistung eines anderen oder in sonstiger Weise auf dessen Kosten "
                                       "etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe verpflichtet. …“",
                        "§ 812 Abs. 1 Satz 1 BGB", "w812",
                        marken=[("durch die Leistung eines anderen", beim("w812", "Leistung")), ("etwas", beim("w812", "etwas")),
                                ("ohne rechtlichen Grund", beim("w812", "rechtlichen")), ("erlangt", beim("w812", "erlangt"))])
SCHEMA4 = [("1. etwas erlangt", beim("schema", "etwas")), ("2. durch Leistung", beim("schema", "Leistung")),
           ("3. ohne rechtlichen Grund", beim("schema", "rechtlichen")), ("4. kein Ausschluss", beim("schema", "Ausschluss"))]
folie([("norm", f"{PI} · § 812 Abs. 1 Satz 1 Alt. 1 BGB"), ("w812", f"{PI} › Wortlaut"),
       ("schema", f"{PI} › Schema: vier Prüfungspunkte")], [
    *tafel("norm", "I. Anspruchsgrundlage"),
    z("§ 812 Abs. 1 Satz 1 Alt. 1 BGB: Leistungskondiktion", 110, 180, "norm", "ExtraBold", 36),
    z("genauer: condictio indebiti", 110, 232, beim("norm", "condictio"), "Bold", 32),
    *w812,
    feld(110, w812_y + 26, 1040, 170, "schema", fill=GELB, rand=5, rund=18, anim="rise", name="schemablock"),
    z("Schema:", 140, w812_y + 40, "schema", "ExtraBold", 32),
    *[z(t, 150 + (i % 2) * 500, w812_y + 88 + (i // 2) * 50, c, "ExtraBold", 32) for i, (t, c) in enumerate(SCHEMA4)],
    zit("BGH, Urt. v. 20.1.2026 – XI ZR 131/24, Rn. 36", 110, 274, beim("norm", "condictio")),
    *requisit([("norm", ("tabler", "scale", 120, WEISS), "§ 812 BGB", GELB),
               ("schema", ("tabler", "list-check", 120, GELB), "Schema", GELB)], px=1560, pu=330, py=90),
    *paar("MI", [("norm", "ruhig"), ("w812", "denkt")], "HK", [("norm", "ruhig"), ("schema", "denkt")]),
])

# ===========================================================================================================================
# D 1. Etwas erlangt (V ZR 119/11 Rn. 17; IX ZR 164/14 Rn. 8)
# ===========================================================================================================================
PII = "II. Voraussetzungen"
folie([("erl", f"{PII} › 1. etwas erlangt"), ("vorteil", f"{PII} › 1. jeder vermögenswerte Vorteil"),
       ("scheine", f"{PII} › 1. Eigentum und Besitz an den Scheinen"), ("ueber", f"{PII} › 1. Übereignung nicht angefochten"),
       ("gutschr", f"{PII} › 1. bei Überweisung: die Gutschrift")], [
    *tafel("erl", "1. Etwas erlangt"),
    z("Was hat Frau Heidkamp erlangt?", 110, 190, "erl", "Bold", 36),
    *okz("jeder vermögenswerte Vorteil", 260, "vorteil", "Bold", 34),
    zit("BGH, Urt. v. 2.12.2011 – V ZR 119/11, Rn. 17", 185, 308, "vorteil"),
    *okz("hier: Eigentum und Besitz an den Scheinen", 370, "scheine", "Bold", 34),
    zit("Übereignung nach § 929 Satz 1 BGB", 185, 418, "scheine"),
    blk(110, 480, 1040, 120, HELLGRUEN, "ueber", [("angefochten: nur der Kaufvertrag,", "ExtraBold", 32, INK),
                                                ("nicht die Übereignung des Geldes", "ExtraBold", 32, INK)]),
    blk(110, 630, 1040, 120, BLAUHELL, "gutschr", [("bei Überweisung: die Gutschrift,", "ExtraBold", 32, INK),
                                                 ("also ein Anspruch gegen die Bank", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8", 110, 768, "gutschr"),
    *requisit([("erl", ("tabler", "help-circle", 110, WEISS), "erlangt?", WEISS),
               ("scheine", ("tabler", "cash-banknote", 140, GRUEN), "Scheine", GRUEN),
               ("gutschr", ("tabler", "building-bank", 130, BLAUHELL), "Gutschrift", BLAUHELL)]),
    *stehend("HK", FX, [("erl", "ruhig"), ("scheine", "denkt"), ("ueber", "ernst")]),
])

# ===========================================================================================================================
# E 2. Durch Leistung (III ZR 291/11 Rn. 24; VIII ZR 39/17 Rn. 17)
# ===========================================================================================================================
folie([("leist", f"{PII} › 2. durch Leistung"), ("def", f"{PII} › 2. Leistungsbegriff"),
       ("bewusst", f"{PII} › 2. bewusst"), ("zweck", f"{PII} › 2. zweckgerichtet: Kaufpreisschuld"),
       ("horiz", f"{PII} › 2. Sicht des Empfängers")], [
    *tafel("leist", "2. Durch Leistung"),
    blk(110, 180, 1040, 120, GELB, "def", [("Leistung = bewusste und zweckgerichtete", "ExtraBold", 33, INK),
                                         ("Mehrung fremden Vermögens", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 21.6.2012 – III ZR 291/11, Rn. 24;", 110, 316, beim("def", "Bundesgerichtshof")),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17", 110, 352, beim("def", "Bundesgerichtshof")),
    *okz("bewusst: Mila übergibt das Geld", 420, "bewusst", "Bold", 34),
    *okz("zweckgerichtet: Erfüllung der Kaufpreisschuld,", 480, "zweck", "Bold", 34),
    z("§ 433 Abs. 2 BGB", 185, 528, beim("zweck", "Paragraf"), "Bold", 34),
    blk(110, 600, 1040, 120, BLAUHELL, "horiz", [("Vorstellungen gehen auseinander:", "ExtraBold", 32, INK),
                                               ("Sicht eines vernünftigen Empfängers", "ExtraBold", 32, INK)]),
    *okz("hier: Zweck eindeutig", 750, beim("horiz", "Hier"), "Bold", 34),
    *requisit([("leist", ("tabler", "cash-banknote-move", 140, GRUEN), "Leistung?", WEISS),
               ("zweck", ("tabler", "target-arrow", 120, GELB), "Zweck", GELB),
               ("horiz", ("tabler", "eye", 120, BLAUHELL), "Empfängersicht", BLAUHELL)]),
    *stehend("MI", FX, [("leist", "ruhig"), ("bewusst", "ernst"), ("horiz", "denkt")]),
])

# ===========================================================================================================================
# F 3. Ohne rechtlichen Grund (§§ 119, 121, 142, 143 BGB; V ZR 55/13 Rn. 19; VIII ZR 37/24 Rn. 41 f.)
# ===========================================================================================================================
folie([("org", f"{PII} › 3. ohne rechtlichen Grund"), ("kv", f"{PII} › 3. Rechtsgrund: Kaufvertrag?"),
       ("irrt", f"{PII} › 3. Erklärungsirrtum, § 119 Abs. 1 BGB"), ("anf", f"{PII} › 3. unverzüglich angefochten"),
       ("p142", f"{PII} › 3. nichtig von Anfang an, § 142 Abs. 1 BGB"), ("alt1", f"{PII} › 3. Satz 1, 1. Alternative")], [
    *tafel("org", "3. Ohne rechtlichen Grund"),
    z("Rechtsgrund wäre: der Kaufvertrag", 110, 180, "kv", "Bold", 36),
    z("Erklärung dieses Inhalts nicht gewollt:", 185, 250, "irrt", "Bold", 34),
    z("vertippt, 2.400 € statt 4.200 €", 185, 298, beim("irrt", "vertippt"), "Bold", 34),
    *okz("Erklärungsirrtum, § 119 Abs. 1 Alt. 2 BGB", 360, beim("irrt", "Erklärungsirrtum"), "Bold", 34),
    *okz("unverzüglich angefochten, §§ 121, 143 BGB", 420, "anf", "Bold", 34),
    blk(110, 490, 1040, 120, HELLROT, "p142", [("§ 142 Abs. 1 BGB: Kaufvertrag als von", "ExtraBold", 33, INK),
                                             ("Anfang an nichtig anzusehen", "ExtraBold", 33, INK)]),
    blk(110, 640, 1040, 80, HELLGRUEN, "alt1", [("Rückwirkung: Satz 1, 1. Alternative", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 27.6.2014 – V ZR 55/13, Rn. 19;", 110, 736, beim("alt1", "Bundesgerichtshof")),
    zit("BGH, Urt. v. 11.2.2026 – VIII ZR 37/24, Rn. 41 f.", 110, 772, beim("alt1", "Bundesgerichtshof")),
    *requisit([("org", ("tabler", "file-text", 120, WEISS), "Kaufvertrag", WEISS),
               ("irrt", ("tabler", "keyboard", 140, GELB), "vertippt", GELB),
               ("p142", ("tabler", "file-x", 120, HELLROT), "nichtig", HELLROT)]),
    *stehend("HK", FX, [("org", "ruhig"), ("irrt", "sorge"), ("anf", "ernst"), ("alt1", "ruhig")]),
])

# ===========================================================================================================================
# G1 4. Kein Ausschluss: § 814 BGB (Wortlautkarte; XI ZR 170/13 Rn. 109)
# ===========================================================================================================================
w814, w814_y = wortlaut(80, 180, 1100, "„Das zum Zwecke der Erfüllung einer Verbindlichkeit Geleistete kann nicht "
                                       "zurückgefordert werden, wenn der Leistende gewusst hat, dass er zur Leistung nicht "
                                       "verpflichtet war, …“", "§ 814 BGB", "w814",
                        marken=[("gewusst hat", beim("w814", "gewusst")), ("nicht verpflichtet", beim("w814", "verpflichtet"))])
folie([("aus", f"{PII} › 4. kein Ausschluss"), ("w814", f"{PII} › 4. § 814 BGB: Kenntnis der Nichtschuld"),
       ("k814", f"{PII} › 4. § 814 BGB: Mila wusste nichts")], [
    *tafel("aus", "4. Kein Ausschluss"),
    *w814,
    z("nötig: positive Kenntnis der Rechtslage", 110, w814_y + 30, "k814", "Bold", 34),
    zit("BGH, Urt. v. 13.5.2014 – XI ZR 170/13, Rn. 109", 110, w814_y + 78, "k814"),
    *neinz("Mila wusste beim Zahlen nichts vom Irrtum", w814_y + 140, beim("k814", "Mila"), "Bold", 34,
           kreuz=beim("k814", "nichts")),
    z("sie ging davon aus, den Kaufpreis zu schulden", 185, w814_y + 188, beim("k814", "ging"), "Bold", 34),
    *requisit([("aus", ("tabler", "ban", 110, HELLROT), "Ausschluss?", WEISS),
               ("k814", ("tabler", "help-circle", 110, BLAUHELL), "Kenntnis?", BLAUHELL)]),
    *stehend("MI", FX, [("aus", "ruhig"), ("w814", "denkt"), ("k814", "ernst")]),
])

# ===========================================================================================================================
# G2 4. Kein Ausschluss: § 817 Satz 2 BGB (Wortlautkarte); Voraussetzungen (+)
# ===========================================================================================================================
w817, w817_y = wortlaut(80, 180, 1100, "„Die Rückforderung ist ausgeschlossen, wenn dem Leistenden gleichfalls ein solcher "
                                       "Verstoß zur Last fällt, …“", "§ 817 Satz 2 BGB", "w817",
                        marken=[("Rückforderung ist ausgeschlossen", beim("w817", "Rückforderung")),
                                ("dem Leistenden", beim("w817", "Leistenden")), ("Verstoß", beim("w817", "Verstoß"))])
folie([("w817", f"{PII} › 4. § 817 Satz 2 BGB"), ("k817", f"{PII} › 4. kein Gesetzes- oder Sittenverstoß"),
       ("tbm", f"{PII} › Voraussetzungen (+)")], [
    *tafel("w817", "4. Kein Ausschluss"),
    *w817,
    z("Verstoß gegen ein gesetzliches Verbot oder die", 110, w817_y + 30, beim("w817", "gesetzliches"), "Bold", 34),
    z("guten Sitten", 110, w817_y + 78, beim("w817", "guten"), "Bold", 34),
    *neinz("Klavierkauf: weder verboten noch sittenwidrig", w817_y + 150, "k817", "Bold", 34, kreuz=beim("k817", "weder")),
    blk(110, w817_y + 230, 1040, 170, HELLGRUEN, "tbm", [("1. etwas erlangt: (+)    2. durch Leistung: (+)", "ExtraBold", 32, INK),
                                                       ("3. ohne rechtlichen Grund: (+)", "ExtraBold", 32, INK),
                                                       ("4. kein Ausschluss: (+)", "ExtraBold", 32, INK)]),
    *requisit([("w817", ("tabler", "ban", 110, HELLROT), "§ 817 Satz 2", WEISS),
               ("tbm", ("tabler", "circle-check", 110, HELLGRUEN), "Voraussetzungen (+)", HELLGRUEN)]),
    *stehend("MI", FX, [("w817", "ruhig"), ("k817", "froh")]),
])

# ===========================================================================================================================
# H Rechtsfolge: § 818 Abs. 1, 2 BGB (Wortlautkarte); Abs. 3 (XI ZR 158/24 Rn. 18)
# ===========================================================================================================================
PIII = "III. Rechtsfolge"
w818, w818_y = wortlaut(80, 225, 1100, "„(1) Die Verpflichtung zur Herausgabe erstreckt sich auf die gezogenen Nutzungen … "
                                       "(2) Ist die Herausgabe wegen der Beschaffenheit des Erlangten nicht möglich oder ist "
                                       "der Empfänger aus einem anderen Grunde zur Herausgabe außerstande, so hat er den Wert "
                                       "zu ersetzen.“", "§ 818 Abs. 1, 2 BGB", "w818a", size=31,
                        marken=[("Nutzungen", beim("w818a", "Nutzungen")), ("außerstande", beim("w818b", "außerstande")),
                                ("Wert", beim("w818b", "Wert"))])
folie([("rf", f"{PIII} · Herausgabe"), ("w818a", f"{PIII} › § 818 Abs. 1 BGB: auch Nutzungen"),
       ("weg", f"{PIII} › Scheine nicht mehr da"), ("w818b", f"{PIII} › § 818 Abs. 2 BGB: Wertersatz"),
       ("wert", f"{PIII} › 2.400 €"), ("entr", f"{PIII} › keine Entreicherung, § 818 Abs. 3 BGB")], [
    *tafel("rf", "III. Rechtsfolge: § 818 BGB"),
    z("Herausgabe des Erlangten", 110, 168, "hg", "Bold", 36),
    *w818,
    *neinz("Scheine: nicht mehr da, bei der Bank eingezahlt", w818_y + 20, "weg", "Bold", 33, kreuz=beim("weg", "nicht")),
    blk(110, w818_y + 72, 500, 70, GELB, "wert", [("Wertersatz: 2.400 €", "ExtraBold", 34, INK)]),
    *okz("keine Entreicherung, § 818 Abs. 3 BGB:", w818_y + 160, "entr", "Bold", 33),
    z("der Betrag steckt noch in ihrem Vermögen", 185, w818_y + 204, beim("entr", "Betrag"), "Bold", 33),
    zit("BGH, Urt. v. 21.7.2026 – XI ZR 158/24, Rn. 18", 185, w818_y + 248, beim("entr", "Betrag")),
    *requisit([("rf", ("tabler", "arrow-back-up", 110, WEISS), "herausgeben", WEISS),
               ("weg", ("tabler", "building-bank", 130, BLAUHELL), "eingezahlt", BLAUHELL),
               ("wert", ("tabler", "coin-euro", 130, GELB), "2.400 €", GELB)]),
    *stehend("HK", FX, [("rf", "ruhig"), ("weg", "denkt"), ("wert", "ernst")]),
])
assert w818_y + 248 + 34 <= 895, w818_y

# ===========================================================================================================================
# I Saldotheorie: beide Seiten haben geleistet (V ZR 52/12 Rn. 28; VIII ZR 37/24 Rn. 41)
# ===========================================================================================================================
PIV = "IV. Saldotheorie"
folie([("gegen", f"{PIV} · auch Mila hat etwas erlangt"), ("saldo", f"{PIV} › Ansprüche nicht isoliert"),
       (beim("saldo", "Zug"), f"{PIV} › Zug um Zug: Geld gegen Klavier")], [
    *tafel("gegen", "IV. Beide haben geleistet"),
    *okz("auch Mila hat erlangt: das Klavier,", 180, "gegen", "Bold", 34),
    z("durch Leistung von Frau Heidkamp,", 185, 228, beim("gegen", "Leistung"), "Bold", 34),
    z("ohne rechtlichen Grund", 185, 276, beim("gegen", "rechtlichen"), "Bold", 34),
    blk(110, 350, 1040, 80, GELB, "saldo", [("Saldotheorie: Ansprüche nicht isoliert", "ExtraBold", 34, INK)]),
    hart(klavier(250, 170, beim("saldo", "Geld"), h=150, unten=620)),
    ficon("tabler", "arrows-exchange", 600, 600, 150, beim("saldo", "Geld"), fuell=WEISS),
    ficon("tabler", "cash-banknote", 900, 600, 170, beim("saldo", "Geld"), fuell=GRUEN),
    pl("Klavier", 335, 632, beim("saldo", "Geld"), fill=WEISS, size=28, anker="m"),
    pl("2.400 €", 900, 632, beim("saldo", "Geld"), fill=GRUEN, size=28, anker="m"),
    blk(110, 710, 1040, 120, HELLGRUEN, beim("saldo", "Zug"), [("Geld nur Zug um Zug gegen Rückgabe", "ExtraBold", 33, INK),
                                                            ("und Rückübereignung des Klaviers", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 27.9.2013 – V ZR 52/12, Rn. 28; BGH VIII ZR 37/24, Rn. 41", 110, 846, beim("saldo", "Zug")),
    *requisit([("gegen", ("tabler", "piano", 130, WEISS), "Klavier", WEISS),
               ("saldo", ("tabler", "scale", 120, GELB), "Saldotheorie", GELB)], px=1560, pu=330, py=90),
    *paar("MI", [("gegen", "denkt"), (beim("saldo", "Zug"), "ernst")], "HK", [("gegen", "ruhig"), (beim("saldo", "Zug"), "froh")]),
])

# ===========================================================================================================================
# J Abgrenzung: condictio ob rem (XII ZR 190/08 Rn. 31 f.)
# ===========================================================================================================================
folie([("orem", "Abgrenzung · condictio ob rem, § 812 Abs. 1 Satz 2 Alt. 2 BGB"), ("orem2", "Abgrenzung › hier nicht")], [
    *tafel("orem", "Abgrenzung: condictio ob rem"),
    z("§ 812 Abs. 1 Satz 2 Alt. 2 BGB", 110, 185, "orem", "ExtraBold", 36),
    blk(110, 260, 1040, 120, LILAHELL, beim("orem", "Einigung"), [("Einigung über einen bezweckten Erfolg,", "ExtraBold", 33, INK),
                                                              ("den man nicht einfordern kann", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 6.7.2011 – XII ZR 190/08, Rn. 31 f.", 110, 396, beim("orem", "Einigung")),
    *neinz("hier nicht: Mila zahlte auf eine Kaufpreisschuld", 470, "orem2", "Bold", 34),
    *requisit([("orem", ("tabler", "target", 120, LILAHELL), "bezweckter Erfolg?", LILAHELL),
               ("orem2", ("tabler", "file-text", 120, WEISS), "Kaufpreisschuld", WEISS)]),
    *stehend("MI", FX, [("orem", "ruhig"), ("orem2", "ernst")]),
])

# ===========================================================================================================================
# K Ergebnis: zurück im Wohnzimmer
# ===========================================================================================================================
folie([("erg", "Ergebnis · 2.400 € für Mila"), ("erg2", "Ergebnis › Zug um Zug gegen das Klavier")], [
    *wohnzimmer("erg", fy=300),
    *fig("MI", MIX, BODEN, FH, [("erg", "ruhig_r"), (beim("erg", "zweitausendvierhundert"), "froh_r")], erst="cut"),
    hart(ns(NAME["MI"], MIX, BODEN, "erg", TUERKIS)),
    *fig("HK", HKX, BODEN, FH, [("erg", "ruhig"), ("erg2", "froh")], erst="cut"),
    hart(ns(NAME["HK"], HKX, BODEN, "erg", LILA)),
    *okz("2.400 € an Mila, § 812 Abs. 1 Satz 1 Alt. 1 BGB", 40, beim("erg", "zweitausendvierhundert"), "Bold", 32, x=130,
         rechts=1880),
    *okz("Zug um Zug gegen Rückgabe und Rückübereignung", 100, "erg2", "Bold", 32, x=130, rechts=1880),
    z("des Klaviers", 130, 146, beim("erg2", "Rückübereignung"), "Bold", 32, rechts=1880),
    ficon("tabler", "cash-banknote", 1390, 300, 130, beim("erg", "zweitausendvierhundert"), fuell=GRUEN),
    ficon("tabler", "arrows-exchange", 1390, 420, 100, "erg2", fuell=WEISS),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi; VIII ZR 39/17 Rn. 16 f.)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst die Leistungskondiktion"), ("tipp2", "Klausurtipp · Leistende über den Zweck bestimmen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Rückabwicklung einer Leistung: immer", 200, 200, "tipp", "Bold", 35),
    z("zuerst die Leistungskondiktion prüfen", 200, 250, beim("tipp", "zuerst"), "Bold", 35),
    *okz("Vorrang vor der Nichtleistungskondiktion", 312, beim("tipp", "Vorrang"), size=34, x=245),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 16", 245, 360, beim("tipp", "Vorrang")),
    linienzug([(130, 420), (1130, 420)], "tipp2", breite=3),
    z("2. Leistenden und Empfänger über den", 200, 450, "tipp2", "Bold", 35),
    z("Zweck der Zuwendung bestimmen", 200, 500, beim("tipp2", "Zweck"), "Bold", 35),
    blk(130, 580, 1000, 100, GELB, beim("tipp2", "abweichenden"),
        [("abweichende Vorstellungen: Sicht des Empfängers", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17", 200, 698, beim("tipp2", "abweichenden")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. etwas erlangt", True),
          (beim("s1", "Eigentum"), 1, "hier: Eigentum und Besitz an den Scheinen", False),
          ("s2", 0, "2. durch Leistung", True),
          (beim("s2", "bewusst"), 1, "bewusst und zweckgerichtet", False),
          ("s3", 0, "3. ohne rechtlichen Grund", True),
          (beim("s3", "Anfechtung"), 1, "hier: Anfechtung, § 142 Abs. 1 BGB", False),
          ("s4", 0, "4. kein Ausschluss nach § 814 oder § 817 Satz 2 BGB", True),
          ("s5", 0, "5. Rechtsfolge: § 818 BGB", True),
          (beim("s5", "Herausgabe"), 1, "Herausgabe oder Wertersatz", False),
          (beim("s5", "beiderseitigen"), 1, "bei beiderseitigen Leistungen: Saldotheorie", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Leistungskondiktion, § 812 Abs. 1 Satz 1 Alt. 1 BGB"), 110, 90, "sch", 44)]
y = 190
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 80, 1: 72}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › 1. etwas erlangt"), ("s2", "Prüfungsschema › 2. durch Leistung"),
       ("s3", "Prüfungsschema › 3. ohne rechtlichen Grund"), ("s4", "Prüfungsschema › 4. kein Ausschluss"),
       ("s5", "Prüfungsschema › 5. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer durch Leistung etwas", 0)], [("ohne rechtlichen Grund", "a"), (" erlangt,", 0)],
                 [("muss es ", 0), ("herausgeben", "b"), (".", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "rechtlichen"), "b": beim("merke", "herausgeben")}),
    *markertext([[("Ist ein Kauf gescheitert, gibt jede Seite", 0)], [("zurück, was sie bekommen hat,", 0)],
                 [("grundsätzlich ", 0), ("Zug um Zug", "c"), (".", 0)]],
                750, 560, 44, "merk2", {"c": beim("merk2", "Zug")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
