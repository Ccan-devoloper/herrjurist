"""Folge 205 · Recht auf Vergessen: Muss dein Name aus dem Online-Archiv? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen (Nachbildung des Grundfalls von BVerfGE 152, 152): Gerhild zieht ein, ihr Nachbar Herr Dornbusch begrüßt
sie; abends findet sie mit einer neutralen Suchmaske (kein Logo) als 1. Treffer einen über 30 Jahre alten Artikel im
Onlinearchiv eines Nachrichtenmagazins (ohne Namen) über seinen Strafprozess; Herr Dornbusch verlangt beim Verlag
(Archivleiter Herr Stöver), nicht mehr unter seinem Namen zu berichten. Danach der echte Fall sachlich (nur Icons, keine
Tatdetails, keine realen Beteiligten), Prüfungsmaßstab (Abgrenzung Recht auf Vergessen II), Schutzbereich (Wortlautkarten
Art. 2 Abs. 1, Art. 1 Abs. 1 GG), Zeitdimension, Pressefreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 2 GG), mittelbare
Drittwirkung (Verweis Lüth), Abwägung, abgestufte Schutzmaßnahmen, Ergebnis, Lösung, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus
Folge 203 bzw. 160 (gemeinsame Dateien unverändert); neu: tuer(), archivregal(), suchmaske(), minisuche(), verlag().
Handlungsgeräusche: Karton abstellen (A1), Tippen (A2); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (GG), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_205/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_205/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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
NAME = {"DO": "Herr Dornbusch", "GE": "Gerhild", "ST": "Herr Stöver"}
NFARBE = {"DO": LILA, "GE": TUERKIS_, "ST": GELB}


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


def archivregal(cue, x0=60, w=420):
    """Archivregal an der Wand (Grundformen, Archivkästen in Palettenfarben mit weißem Etikett)."""
    y0, h = 150, BODEN - 150
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    farben = [BLAU, GRUEN, GELB, LILA, ROT, PINK]
    fach = (h - 30) // 4
    k = 0
    for f in range(4):
        yb = o + (25 + (f + 1) * fach) * s
        dr.rectangle((o, yb, o + w * s, yb + 12 * s), fill=HOLZ, outline=INK, width=4 * s)
        xx = o + 24 * s
        for _ in range(4):
            bw, bh = 82 * s, int(fach * 0.72) * s
            dr.rectangle((xx, yb - bh, xx + bw, yb), fill=farben[k % len(farben)], outline=INK, width=4 * s)
            dr.rectangle((xx + 18 * s, yb - bh + 22 * s, xx + bw - 18 * s, yb - bh + 46 * s), fill=WEISS, outline=INK, width=3 * s)
            xx += bw + 12 * s; k += 1
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0, y0, cue, "cut", 0.0, None, name="archivregal"))


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


# ===========================================================================================================================
# A1 Fall: Gerhild zieht ein, Herr Dornbusch begrüßt sie im Treppenhaus (fiktiv)
# ===========================================================================================================================
GEX, DOX = 560, 1350
folie([(NULL, "Fall · Gerhild zieht in eine neue Wohnung"), ("nachbar", "Fall · Nebenan: Herr Dornbusch")], [
    boden(NULL),
    tuer(170, NULL, farbe=HOLZ), tuer(1600, NULL, farbe=BLAU),
    hart(pl("Gerhild zieht in eine neue Wohnung", 70, 40, NULL, fill=TUERKIS_, size=32)),
    szene(ficon("tabler", "box", 860, BODEN, 230, beim("fall", "Wohnung"), fuell=HOLZ), "205karton*", 1.0, -0.05),
    *fig("GE", GEX, BODEN, FH, [(NULL, "ruhig_r"), ("d1", "froh_r")], erst="cut"),
    hart(ns(NAME["GE"], GEX, BODEN, NULL, TUERKIS_)),
    *fig("DO", DOX, BODEN, FH, [("nachbar", "ruhig")], bis="d1"),
    *redet("DO_redet", DOX, BODEN, FH, "d1", "google"),
    ns(NAME["DO"], DOX, BODEN, "nachbar", LILA, d=0.1),
    pl("Nebenan: Herr Dornbusch, ein freundlicher älterer Herr", 70, 104, "nachbar", fill=WEISS, size=30, bis="d1"),
    blase("sprech", 660, 250, "d1", 1170, 250, inhalt=["Willkommen in der Nachbarschaft!", "Wenn Sie etwas brauchen,",
                                                      "klingeln Sie einfach."],
          textsize=32, figur=("DO_redet", DOX, BODEN, FH)),
])

# ===========================================================================================================================
# A2 Fall: Am Abend sucht Gerhild nach dem Namen (neutrale Suchmaske, kein Logo, Magazin ohne Namen)
# ===========================================================================================================================
GE2 = 1600
WX, WY, WW, WH = 100, 110, 1180, 660


def suchmaske(cue):
    """Neutrales Browserfenster mit Suchfeld (kein Logo, keine Marke)."""
    els = [hart(feld(WX, WY, WW, WH, cue, fill=WEISS, rand=5, rund=22, name="fenster")),
           hart(linienzug([(WX + 4, WY + 64), (WX + WW - 4, WY + 64)], cue, breite=4, farbe=INK))]
    for i, f_ in enumerate((ROT, GELB, GRUEN)):
        els.append(hart(feld(WX + 26 + i * 40, WY + 20, 22, 22, cue, fill=f_, rand=3, rund=11, name="punkt")))
    els += [hart(feld(WX + 60, WY + 100, WW - 120, 84, cue, fill=WEISS, rand=4, rund=40, name="suchfeld")),
            hart(ficon("tabler", "search", WX + WW - 120, WY + 172, 58, cue, anim="cut"))]
    return els


folie([("google", "Fall · Am Abend: die Suche nach dem Namen"), ("treffer", "Fall · Der 1. Treffer: ein alter Artikel"),
       ("prozess", "Fall · Ein Bericht über seinen Strafprozess"), ("g1", "Fall · Gerhild ist überrascht")], [
    boden("google"),
    hart(mond(1830, 92, 34, "google")),
    pl("Am Abend", 1330, 40, "google", fill=LILA, size=30),
    *suchmaske("google"),
    szene(z("Dornbusch", WX + 100, WY + 118, beim("google", "Suchmaschine"), "Bold", 40, rechts=1180),
          "205tippen*", 0.8, -1.9),
    # erster Treffer (hervorgehoben), weitere Treffer nur als graue Platzhalter
    feld(WX + 60, WY + 220, WW - 120, 196, "treffer", fill=HELL, rand=5, rund=16, anim="pop", name="treffer1"),
    z("Onlinearchiv eines Nachrichtenmagazins", WX + 96, WY + 240, "treffer", size=28, farbe=TEXT, rechts=1240),
    z("Der Prozess gegen Herrn Dornbusch", WX + 96, WY + 282, "treffer", "ExtraBold", 38, rechts=1240),
    pl("1. Treffer", WX + WW - 250, WY + 236, "treffer", fill=GELB, size=30),
    pl("über 30 Jahre alt", WX + 96, WY + 346, beim("treffer", "dreißig"), fill=WEISS, size=28),
    feld(WX + 60, WY + 440, WW - 120, 56, "treffer", fill=HELLGRAU, rand=3, rund=14, anim="cut", name="treffer2"),
    feld(WX + 60, WY + 512, WW - 120, 56, "treffer", fill=HELLGRAU, rand=3, rund=14, anim="cut", name="treffer3"),
    pl("Strafprozess · Verurteilung wegen eines schweren Verbrechens", WX + 60, WY + 588, beim("prozess", "Strafprozess"),
       fill=HELLROT, size=30),
    *fig("GE", GE2, BODEN, FH, [("google", "ruhig"), ("treffer", "denkt"), (beim("prozess", "Verurteilung"), "staunt")],
         bis="g1", erst="cut"),
    *redet("GE_redet", GE2, BODEN, FH, "g1", "haft"),
    hart(ns(NAME["GE"], GE2, BODEN, "google", TUERKIS_)),
    blase("sprech", 470, 210, "g1", 1555, 260, inhalt=["Ausgerechnet mein", "netter Nachbar?"], textsize=34,
          figur=("GE_redet", GE2, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Fall: Herr Dornbusch beim Verlag; Archivleiter Herr Stöver (fiktiv). H kehrt hierher zurück.
# ===========================================================================================================================
STX, DOX3 = 700, 1420


def verlag(cue):
    return [boden(cue), archivregal(cue)]


folie([("haft", "Fall · Herr Dornbusch wendet sich an den Verlag"), ("s1", "Fall · Der Verlag: Archiv bleibt vollständig"),
       ("frage", "Die Frage · Muss sein Name aus dem Onlinearchiv?"),
       ("grund", "Die Frage · Recht auf Vergessen I, BVerfGE 152, 152")], [
    *verlag("haft"),
    pl("Strafe längst verbüßt", 560, 40, "haft", fill=HELLGRUEN, size=30, bis="frage"),
    pl("verlangt: nicht mehr unter Nennung seines Namens berichten", 560, 104, "klage", fill=WEISS, size=30, bis="frage"),
    *fig("ST", STX, BODEN, FH, [("haft", "ruhig_r"), ("klage", "denkt_r")], bis="s1", erst="cut"),
    *redet("ST_redet_r", STX, BODEN, FH, "s1", "frage"),
    *fig("ST", STX, BODEN, FH, [("frage", "ernst_r")], erst="cut"),
    hart(ns(NAME["ST"], STX, BODEN, "haft", GELB)),
    *fig("DO", DOX3, BODEN, FH, [("haft", "ernst"), ("klage", "sorge")], bis="d2", erst="cut"),
    *redet("DO_bittet", DOX3, BODEN, FH, "d2", "s1"),
    *fig("DO", DOX3, BODEN, FH, [("s1", "sorge"), ("frage", "muede")], erst="cut"),
    hart(ns(NAME["DO"], DOX3, BODEN, "haft", LILA)),
    blase("sprech", 560, 210, "d2", 1330, 290, inhalt=["Nehmen Sie wenigstens", "meinen Namen heraus."], textsize=34,
          figur=("DO_bittet", DOX3, BODEN, FH), bis="s1"),
    blase("sprech", 740, 230, "s1", 880, 290, inhalt=["Der Bericht war damals rechtmäßig.", "Unser Archiv bleibt vollständig."],
          textsize=32, figur=("ST_redet_r", STX, BODEN, FH), bis="frage"),
    pl("Muss sein Name aus dem Onlinearchiv?", 560, 40, "frage", fill=PINK, size=36),
    pl("nachgebildet: der Grundfall von Recht auf Vergessen I", 560, 116, "grund", fill=WEISS, size=30),
    pl("BVerfG, Beschl. v. 6.11.2019 · 1 BvR 16/13 · BVerfGE 152, 152", 560, 182, beim("grund", "Beschluss"), fill=GELB,
       size=30),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_205(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_205("sv", [
    "Gerhild zieht in eine neue Wohnung. Als sie den Namen ihres Nachbarn, Herrn Dornbusch, in eine Suchmaschine eingibt, "
    "erscheint als 1. Treffer ein über 30 Jahre alter Artikel aus dem kostenlos zugänglichen Onlinearchiv eines "
    "Nachrichtenmagazins. Er berichtet unter Nennung seines Namens über den Strafprozess und seine Verurteilung wegen "
    "eines schweren Verbrechens.",
    "Herr Dornbusch hat seine Strafe vollständig verbüßt und ist mit der Tat nicht wieder an die Öffentlichkeit getreten. "
    "Die Berichte waren bei ihrer Veröffentlichung rechtmäßig.",
    "Er verlangt vom Verlag, nicht mehr unter Nennung seines Namens über die Tat zu berichten. Der Verlag lehnt ab: Das Archiv "
    "bleibe vollständig. Landgericht und Oberlandesgericht geben der Unterlassungsklage statt, der Bundesgerichtshof "
    "weist sie ab. Herr Dornbusch erhebt Verfassungsbeschwerde gegen das Urteil.",
], "Verletzt das Urteil Herrn Dornbusch in Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG?")

# ===========================================================================================================================
# C1 Der echte Fall: das Verfahren (Rn. 1, 4–6, 37) – ohne Figuren, ohne Tatdetails, ohne reale Beteiligte
# ===========================================================================================================================
PF = "Der echte Fall"
folie([("weg", f"{PF} · Landgericht und Oberlandesgericht"), ("bgh", f"{PF} · Bundesgerichtshof weist ab"),
       ("vb", f"{PF} · Urteilsverfassungsbeschwerde")], [
    boden("weg"),
    pl("Recht auf Vergessen I · BVerfG, Beschl. v. 6.11.2019 · 1 BvR 16/13", 70, 40, "weg", fill=GELB, size=30),
    pl("Landgericht und Oberlandesgericht: Unterlassungsklage erfolgreich", 70, 118, beim("weg", "Landgericht"),
       fill=HELLGRUEN, size=30),
    pl("Bundesgerichtshof (13.11.2012 · VI ZR 330/11): Klage abgewiesen", 70, 188, "bgh", fill=HELLROT, size=30),
    pl("Verfassungsbeschwerde gegen das Zivilurteil", 70, 258, "vb", fill=WEISS, size=30),
    zit("BVerfGE 152, 152, Rn. 1, 4–6, 37", 80, 330, "vb"),
    ficon("tabler", "building", 230, BODEN, 150, beim("weg", "Landgericht"), fuell=HELLGRUEN),
    pl("LG (+)", 230, BODEN + 22, beim("weg", "Landgericht"), fill=HELLGRUEN, size=30, anker="m"),
    ficon("tabler", "building", 640, BODEN, 170, beim("weg", "Oberlandesgericht"), fuell=HELLGRUEN),
    pl("OLG (+)", 640, BODEN + 22, beim("weg", "Oberlandesgericht"), fill=HELLGRUEN, size=30, anker="m"),
    ficon("tabler", "building-bank", 1080, BODEN, 190, "bgh", fuell=HELLROT),
    pl("BGH (-)", 1080, BODEN + 22, "bgh", fill=HELLROT, size=30, anker="m"),
    ficon("tabler", "scale", 1560, BODEN, 200, "vb", fuell=GELB),
    pl("BVerfG", 1560, BODEN + 22, "vb", fill=GELB, size=30, anker="m"),
])


# ===========================================================================================================================
# C2 I. Prüfungsmaßstab: Grundgesetz oder Charta? (LS 1a; Rn. 11 f., 39, 41 f., 74; RvV II Rn. 33 f., 42, 50)
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


PI = "I. Prüfungsmaßstab"
folie([("mass", f"{PI} · Grundgesetz oder Charta?"), ("privileg", f"{PI} › Medienprivileg"),
       ("gg", f"{PI} › nicht vollständig vereinheitlicht: Grundgesetz"),
       ("rvv2", f"{PI} › Abgrenzung: Recht auf Vergessen II")], [
    *tafel("mass", "I. Prüfungsmaßstab"),
    z("Grundgesetz oder Grundrechte der Union?", 110, 180, "mass", "Bold", 36),
    blk(110, 245, 1040, 110, BLAUHELL, "privileg", [("Medienprivileg: Spielraum der Mitgliedstaaten", "ExtraBold", 32, INK),
                                                   ("Art. 85 DSGVO (früher Art. 9 DSRL 95/46/EG)", "Regular", 30, INK)]),
    zit("BVerfGE 152, 152, Rn. 11 f., 39, 74", 110, 365, "privileg"),
    *okz("nicht vollständig vereinheitlicht:", 420, "gg", "Bold", 34, x=160),
    z("primär Maßstab des Grundgesetzes", 160, 466, beim("gg", "Grundgesetz"), "Bold", 34),
    zit("Leitsatz 1a; Rn. 41 f., 74", 160, 514, beim("gg", "Grundgesetz")),
    blk(110, 575, 1040, 150, LILAHELL, "rvv2", [("Recht auf Vergessen II (BVerfGE 152, 216):", "ExtraBold", 32, INK),
                                               ("Suchmaschine, vollständig vereinheitlicht:", "Regular", 31, INK),
                                               ("Maßstab ist die Grundrechtecharta", "Regular", 31, INK)]),
    zit("1 BvR 276/17, Rn. 33 f., 42, 50", 110, 738, beim("rvv2", "Grundrechtecharta")),
    *requisit([("mass", ("tabler", "scale", 120, WEISS), "Maßstab?", PINK),
               ("privileg", ("tabler", "news", 110, BLAUHELL), "Medienprivileg", BLAUHELL),
               ("gg", ("tabler", "book-2", 110, ROT), "Grundgesetz", WEISS),
               ("rvv2", ("tabler", "world-search", 110, LILAHELL), "Suchmaschine: Charta", LILAHELL)]),
    *paar("DO", [("mass", "ernst"), ("gg", "ruhig")], "ST", [("mass", "ruhig"), ("rvv2", "denkt")]),
])

# ===========================================================================================================================
# D1 II. Schutzbereich: allgemeines Persönlichkeitsrecht (Wortlautkarten; Rn. 75, 79)
# ===========================================================================================================================
PII = "II. Schutzbereich"
w21, w21_y = wortlaut(80, 290, 1100, "„(1) Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit, …“",
                      "Art. 2 Abs. 1 GG (Auszug)", "a21",
                      marken=[("freie Entfaltung", beim("a21", "freie")), ("Persönlichkeit", beim("a21", "Persönlichkeit", 1))])
w11, w11_y = wortlaut(80, w21_y + 30, 1100, "„(1) Die Würde des Menschen ist unantastbar. …“", "Art. 1 Abs. 1 Satz 1 GG", "a11",
                      marken=[("Würde des Menschen", beim("a11", "Würde")), ("unantastbar", beim("a11", "unantastbar"))])
folie([("apr", f"{PII} · allgemeines Persönlichkeitsrecht"), ("a21", f"{PII} › Art. 2 Abs. 1 GG"),
       ("a11", f"{PII} › i. V. m. Art. 1 Abs. 1 GG")], [
    *tafel("apr", "II. Schutzbereich"),
    blk(110, 172, 1040, 90, PINK, "apr", [("allgemeines Persönlichkeitsrecht,", "ExtraBold", 33, INK),
                                       ("Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "ExtraBold", 31, INK)]),
    *w21, *w11,
    zit("BVerfGE 152, 152, Rn. 75, 79", 110, w11_y + 24, "a11"),
    *requisit([("apr", ("tabler", "fingerprint", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("a11", ("tabler", "shield-check", 110, WEISS), "Menschenwürde", WEISS)]),
    *stehend("DO", FX, [("apr", "ruhig"), ("a11", "ernst")]),
])

# ===========================================================================================================================
# D2 Schutz vor Berichten, Zeitdimension (LS 2a–c; Rn. 91 f., 105, 107, 109)
# ===========================================================================================================================
folie([("aeuss", f"{PII} › Schutz vor personenbezogenen Berichten"), ("zeit", f"{PII} › die Zeit zählt"),
       ("vergessen", f"{PII} › Möglichkeit des Vergessens"), ("neu", f"{PII} › Chance zum Neubeginn"),
       ("jederzeit", f"{PII} › Rechtfertigung zu jedem Zeitpunkt"), ("kein", f"{PII} › kein Recht, alles löschen zu lassen")], [
    *tafel("aeuss", "II. Schutzbereich: die Zeit zählt"),
    *neinz("nicht: informationelle Selbstbestimmung", 172, "aeuss", "Bold", 33, kreuz=beim("aeuss", "nicht")),
    *okz("sondern: Schutz vor Gefährdungen durch die", 222, beim("aeuss", "sondern"), "Bold", 33),
    z("Verbreitung personenbezogener Berichte", 185, 268, beim("aeuss", "Verbreitung"), "Bold", 33),
    zit("Leitsatz 2a; Rn. 91 f.", 185, 316, beim("aeuss", "Verbreitung")),
    blk(110, 370, 1040, 130, GELB, "vergessen", [("„Zur Zeitlichkeit der Freiheit gehört", "ExtraBold", 34, INK),
                                               ("die Möglichkeit des Vergessens.“", "ExtraBold", 34, INK)]),
    zit("Leitsatz 2b; Rn. 105", 110, 510, "vergessen"),
    *okz("Chance zum Neubeginn in Freiheit", 565, beim("neu", "Chance"), "Bold", 33),
    *okz("Verbreitung muss sich zu jedem Zeitpunkt", 625, "jederzeit", "Bold", 33),
    z("rechtfertigen lassen", 185, 671, beim("jederzeit", "rechtfertigen"), "Bold", 33),
    zit("Rn. 109", 520, 679, beim("jederzeit", "rechtfertigen")),
    *neinz("kein Recht, alles aus dem Internet löschen", 735, "kein", "Bold", 33, kreuz=beim("kein", "nicht")),
    z("zu lassen", 185, 781, "kein", "Bold", 33),
    zit("Leitsatz 2c; Rn. 107", 360, 789, "kein"),
    *requisit([("aeuss", ("tabler", "news", 110, WEISS), "Presseberichte", WEISS),
               ("zeit", ("tabler", "hourglass", 100, GELB), "die Zeit", GELB),
               ("neu", ("tabler", "sunrise", 120, GELB), "Neubeginn", HELLGRUEN),
               ("kein", ("tabler", "ban", 100, HELLROT), "nicht alles löschen", HELLROT)]),
    *stehend("DO", FX, [("aeuss", "ernst"), ("vergessen", "muede"), ("neu", "froh"), ("kein", "sorge")]),
])

# ===========================================================================================================================
# E1 III. Gegenrecht: Pressefreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 2 GG; Rn. 94, 112 f., 115)
# ===========================================================================================================================
PIII = "III. Gegenrecht"
w51, w51_y = wortlaut(80, 175, 1100, "„… Die Pressefreiheit und die Freiheit der Berichterstattung durch Rundfunk und "
                                     "Film werden gewährleistet. …“", "Art. 5 Abs. 1 Satz 2 GG", "a51",
                      marken=[("Pressefreiheit", beim("a51", "Pressefreiheit")), ("gewährleistet", beim("a51", "gewährleistet"))])
folie([("presse", f"{PIII} · der Verlag"), ("a51", f"{PIII} · Pressefreiheit, Art. 5 Abs. 1 Satz 2 GG"),
       ("archiv", f"{PIII} › auch das Onlinearchiv"), ("oeff", f"{PIII} › Archive für die Öffentlichkeit"),
       ("rechtm", f"{PIII} › ursprünglich rechtmäßig")], [
    *tafel("presse", "III. Gegenrecht: die Pressefreiheit"),
    *w51,
    *okz("Entscheidung, alte Berichte dauerhaft im Archiv", w51_y + 40, "archiv", "Bold", 33),
    z("zugänglich zu machen", 185, w51_y + 86, beim("archiv", "zugänglich"), "Bold", 33),
    zit("Rn. 94, 112", 545, w51_y + 94, beim("archiv", "zugänglich")),
    *okz("Archive: wichtig für die Öffentlichkeit,", w51_y + 150, "oeff", "Bold", 33),
    z("etwa für zeitgeschichtliche Recherchen", 185, w51_y + 196, beim("oeff", "zeitgeschichtliche"), "Bold", 33),
    zit("Rn. 113", 185, w51_y + 244, beim("oeff", "zeitgeschichtliche")),
    blk(110, w51_y + 300, 1040, 80, HELLGRUEN, "rechtm", [("ursprüngliche Berichterstattung: rechtmäßig", "ExtraBold", 33, INK)]),
    zit("Rn. 115", 110, w51_y + 392, "rechtm"),
    *requisit([("presse", ("tabler", "news", 110, GELB), "Verlag", GELB),
               ("archiv", ("tabler", "archive", 110, BLAUHELL), "Onlinearchiv", BLAUHELL),
               ("oeff", ("tabler", "history", 110, WEISS), "Zeitgeschichte", WEISS),
               ("rechtm", ("tabler", "circle-check", 110, HELLGRUEN), "damals rechtmäßig", HELLGRUEN)]),
    *stehend("ST", FX, [("presse", "ruhig"), ("archiv", "froh"), ("rechtm", "ernst")]),
])

# ===========================================================================================================================
# E2 Mittelbare Drittwirkung, Prüfpflichten (Rn. 76, 118 f.)
# ===========================================================================================================================
folie([("dritt", f"{PIII} › mittelbare Drittwirkung"), ("pruef", f"{PIII} › keine ständige Prüfpflicht"),
       ("beanst", f"{PIII} › Schutzpflichten nach Beanstandung")], [
    *tafel("dritt", "Zwischen Privaten: mittelbar"),
    *okz("Grundrechte wirken mittelbar,", 180, "dritt", "Bold", 34),
    z("über das Zivilrecht", 185, 226, beim("dritt", "über"), "Bold", 34),
    zit("Rn. 76; Ausstrahlung: Folge zum Lüth-Urteil", 185, 276, beim("dritt", "Lüth")),
    *neinz("keine Pflicht, das Archiv von sich aus", 360, "pruef", "Bold", 34, kreuz=beim("pruef", "nicht")),
    z("ständig zu überprüfen", 185, 406, beim("pruef", "ständig"), "Bold", 34),
    zit("Rn. 118", 185, 454, beim("pruef", "ständig")),
    *okz("Schutzpflichten erst, wenn sich", 540, "beanst", "Bold", 34),
    z("Betroffene an den Verlag wenden", 185, 586, beim("beanst", "Betroffene"), "Bold", 34),
    zit("Rn. 119", 185, 634, beim("beanst", "Betroffene")),
    *requisit([("dritt", ("tabler", "scale", 120, WEISS), "beide Seiten", WEISS),
               ("pruef", ("tabler", "list-search", 110, HELLROT), "keine Prüfpflicht", HELLROT),
               ("beanst", ("tabler", "mail", 110, GELB), "Beanstandung", GELB)]),
    *paar("DO", [("dritt", "ruhig"), ("beanst", "ernst")], "ST", [("dritt", "ruhig"), ("pruef", "froh"), ("beanst", "denkt")]),
])

# ===========================================================================================================================
# F1 IV. Abwägung: Zeitablauf, Breitenwirkung, Verhalten (Rn. 121–125, 146–150)
# ===========================================================================================================================
PIV = "IV. Abwägung"
folie([("abw", f"{PIV} · Persönlichkeitsrecht gegen Pressefreiheit"), ("zeitab", f"{PIV} › 1. Zeitablauf"),
       ("breite", f"{PIV} › 2. Breitenwirkung"), ("verhalten", f"{PIV} › 3. Verhalten des Betroffenen"),
       ("selbst", f"{PIV} › 3. wer selbst Aufmerksamkeit sucht")], [
    *tafel("abw", "IV. Abwägung"),
    z("1. Zeitablauf:", 110, 180, "zeitab", "ExtraBold", 34),
    z("Tat über 30 Jahre zurück, Strafe verbüßt", 160, 226, beim("zeitab", "Tat"), size=34),
    zit("Rn. 146", 160, 274, beim("zeitab", "Tat")),
    z("2. Breitenwirkung:", 110, 330, "breite", "ExtraBold", 34),
    z("Nachbarn und neue Bekannte suchen den Namen;", 160, 376, beim("breite", "Nachbarn"), size=34),
    z("der 1. Treffer prägt das Bild der Person", 160, 422, beim("breite", "Treffer"), size=34),
    zit("Rn. 147, 149", 160, 470, beim("breite", "Treffer")),
    z("3. Verhalten des Betroffenen:", 110, 526, "verhalten", "ExtraBold", 34),
    z("nicht wieder an die Öffentlichkeit getreten", 160, 572, beim("verhalten", "Er"), size=34),
    zit("Rn. 150", 160, 620, beim("verhalten", "Er")),
    blk(110, 668, 1040, 80, HELLROT, "selbst", [("wer selbst Aufmerksamkeit sucht: weniger Gewicht", "ExtraBold", 31, INK)]),
    zit("Rn. 123", 110, 760, "selbst"),
    *requisit([("abw", ("tabler", "scale", 120, WEISS), "Abwägung", GELB),
               ("zeitab", ("tabler", "hourglass", 100, GELB), "über 30 Jahre", GELB),
               ("breite", ("tabler", "world-search", 110, BLAUHELL), "Namenssuche", BLAUHELL),
               ("verhalten", ("tabler", "home", 110, HELLGRUEN), "zurückgezogen", HELLGRUEN),
               ("selbst", ("tabler", "speakerphone", 110, HELLROT), "Aufmerksamkeit?", HELLROT)]),
    *paar("GE", [("abw", "ruhig"), ("breite", "denkt"), ("verhalten", "ernst")],
          "DO", [("abw", "ernst"), ("zeitab", "muede"), ("breite", "sorge"), ("verhalten", "ruhig")]),
])


# ===========================================================================================================================
# F2 IV. 4. Abgestufte Schutzmaßnahmen (LS 2d; Rn. 128–141, 153); rechts zwei neutrale Mini-Suchmasken
# ===========================================================================================================================
def minisuche(y, suchtext, cue, ergebnis, ergebnis_cue, gut):
    """Kleine neutrale Suchmaske rechts der Tafel (kein Logo): Suchtext und Ergebnis."""
    x, w = 1270, 590
    els = [feld(x, y, w, 260, cue, fill=WEISS, rand=5, rund=20, anim="pop", name="minifenster"),
           feld(x + 26, y + 26, w - 52, 70, cue, fill=WEISS, rand=4, rund=34, anim="pop", name="minifeld"),
           z(suchtext, x + 56, y + 40, cue, "Bold", 32, rechts=x + w - 90),
           ficon("tabler", "search", x + w - 70, y + 86, 44, cue, anim="pop")]
    els += [feld(x + 26, y + 120, w - 52, 110, ergebnis_cue, fill=HELLGRUEN if gut else HELLROT, rand=4, rund=14,
                 anim="pop", name="minitreffer"),
            z(ergebnis[0], x + 56, y + 134, ergebnis_cue, "ExtraBold", 30, rechts=x + w - 40),
            z(ergebnis[1], x + 56, y + 176, ergebnis_cue, size=28, rechts=x + w - 40)]
    return els


folie([("stufen", f"{PIV} › 4. abgestufte Schutzmaßnahmen"), ("loesch", f"{PIV} › 4. keine Pflicht zur Löschung"),
       ("suche", f"{PIV} › 4. Auffindbarkeit über den Namen begrenzen"),
       ("sach", f"{PIV} › 4. sachbezogene Recherche bleibt möglich"), ("fach", f"{PIV} › 4. die Fachgerichte entscheiden")], [
    *tafel("stufen", "IV. 4. Abgestufter Schutz"),
    z("4. abgestufte Schutzmaßnahmen:", 110, 180, "stufen", "ExtraBold", 34),
    *neinz("Pflicht, alte Berichte endgültig zu löschen", 250, "loesch", "Bold", 33, kreuz=beim("loesch", "unvereinbar")),
    z("oder zu verändern: grundsätzlich unvereinbar", 185, 296, beim("loesch", "verändern"), "Bold", 33),
    zit("Rn. 130", 185, 344, beim("loesch", "verändern")),
    *okz("Auffindbarkeit über namensbezogene", 410, "suche", "Bold", 33),
    z("Suchabfragen begrenzen", 185, 456, beim("suche", "Suchabfragen"), "Bold", 33),
    zit("Leitsatz 2d; Rn. 133–135, 141", 185, 504, beim("suche", "Suchabfragen")),
    *okz("Recherche zu den damaligen Ereignissen:", 570, "sach", "Bold", 33),
    z("Bericht bleibt auffindbar, unverändert", 185, 616, beim("sach", "findet"), "Bold", 33),
    zit("Rn. 135", 185, 664, beim("sach", "findet")),
    blk(110, 715, 1040, 80, GELB, "fach", [("Was zumutbar ist, entscheiden die Fachgerichte", "ExtraBold", 32, INK)]),
    zit("Rn. 136, 141", 110, 805, "fach"),
    *requisit([("stufen", ("tabler", "stairs", 130, GELB), "abgestufter Schutz", GELB),
               ("loesch", ("tabler", "archive-off", 120, HELLROT), "nicht löschen", HELLROT)],
              bis=beim("suche", "namensbezogene")),
    *minisuche(130, "Dornbusch", beim("suche", "namensbezogene"), ("kein Treffer zum alten Artikel", "unter dem Namen begrenzt"),
               beim("suche", "nicht"), False),
    *minisuche(500, "Prozess von damals", "sach", ("Bericht im Archiv", "vollständig und unverändert"), beim("sach", "findet"), True),
])

# ===========================================================================================================================
# G Ergebnis im echten Fall (Tenor; Rn. 40, 143–153, 155, 157)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Zeitablauf zu gering gewichtet"), ("verl", "Ergebnis › Persönlichkeitsrecht verletzt"),
       ("zurueck", "Ergebnis › aufgehoben und zurückverwiesen")], [
    *tafel("erg", "Ergebnis im echten Fall"),
    *neinz("Bundesgerichtshof: Belastung durch den Zeitablauf", 180, "erg", "Bold", 33, kreuz=beim("erg", "nicht")),
    z("nicht hinreichend gewichtet", 185, 226, beim("erg", "nicht"), "Bold", 33),
    zit("Rn. 145–150", 185, 274, beim("erg", "nicht")),
    *neinz("keine Zwischenlösungen geprüft", 330, beim("erg", "keine"), "Bold", 33),
    zit("Rn. 153", 185, 378, beim("erg", "keine")),
    blk(110, 440, 1040, 110, HELLROT, "verl", [("Urteil verletzt das allgemeine", "ExtraBold", 33, INK),
                                            ("Persönlichkeitsrecht, Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "Regular", 30, INK)]),
    zit("Tenor; Rn. 40", 110, 562, "verl"),
    blk(110, 620, 1040, 80, GRUEN, "zurueck", [("aufgehoben und zurückverwiesen, einstimmig", "ExtraBold", 33, INK)]),
    zit("Tenor; Rn. 155, 157", 110, 712, "zurueck"),
    *requisit([("erg", ("tabler", "building-bank", 140, HELLROT), "Bundesgerichtshof", HELLROT),
               ("verl", ("tabler", "fingerprint", 120, PINK), "verletzt", PINK),
               ("zurueck", ("tabler", "arrow-back-up", 120, GRUEN), "zurück an den BGH", GRUEN)], pu=560, py=260),
])

# ===========================================================================================================================
# H Zurück zu Herrn Dornbusch (Schauplatz A3: die Geschichte kehrt zum Ausgangsfall zurück)
# ===========================================================================================================================
folie([("zur", "Zurück zu Herrn Dornbusch · die Lösung"), ("loes1", "Zurück zu Herrn Dornbusch › keine Löschung"),
       ("loes2", "Zurück zu Herrn Dornbusch › Schutz gegen die Namenssuche")], [
    *verlag("zur"),
    *fig("ST", STX, BODEN, FH, [("zur", "ruhig_r"), ("loes2", "denkt_r")], erst="cut"),
    hart(ns(NAME["ST"], STX, BODEN, "zur", GELB)),
    *fig("DO", DOX3, BODEN, FH, [("zur", "ernst"), (beim("loes2", "Schutzvorkehrungen"), "froh")], erst="cut"),
    hart(ns(NAME["DO"], DOX3, BODEN, "zur", LILA)),
    *neinz("Name aus dem Archiv löschen: nicht nötig", 60, "loes1", "Bold", 32, x=640, rechts=1880,
           kreuz=beim("loes1", "nicht")),
    *okz("Schutz gegen die Suche nach seinem Namen:", 120, "loes2", "Bold", 32, x=640, rechts=1880),
    z("zumutbare Schutzvorkehrungen kommen in Betracht", 640, 166, beim("loes2", "zumutbare"), "Bold", 32, rechts=1880),
    pl("welche: klären die Zivilgerichte", 595, 230, beim("loes2", "welche"), fill=GELB, size=30),
    ficon("tabler", "search-off", 1060, BODEN, 120, beim("loes2", "Suche"), fuell=WEISS),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst der Prüfungsmaßstab"), ("tipp2", "Klausurtipp · äußerungsrechtliches Persönlichkeitsrecht"),
       ("tipp3", "Klausurtipp · Zwischenlösungen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. zuerst den Prüfungsmaßstab klären:", 200, 200, "tipp", "Bold", 35),
    z("vollständig vereinheitlicht: Grundrechtecharta", 200, 252, beim("tipp", "Ist"), size=34),
    z("sonst: Grundgesetz", 200, 300, beim("tipp", "sonst"), size=34),
    linienzug([(130, 370), (1130, 370)], "tipp2", breite=3),
    *neinz("2. nicht: informationelle Selbstbestimmung", 400, "tipp2", "Bold", 34, x=200, kreuz=beim("tipp2", "nicht")),
    z("sondern: Persönlichkeitsrecht, äußerungsrechtlich", 200, 452, beim("tipp2", "sondern"), size=34),
    zit("Leitsatz 2a; Rn. 79, 91 f.", 200, 500, beim("tipp2", "sondern")),
    blk(130, 570, 1000, 120, GELB, "tipp3", [("3. Zwischenlösungen suchen", "ExtraBold", 34, INK),
                                          ("statt Alles oder Nichts", "ExtraBold", 34, INK)]),
    zit("Rn. 128–141, 153", 200, 702, "tipp3"),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Prüfungsmaßstab: Grundgesetz oder Charta", True),
          ("k2", 0, "II. Schutzbereich: allgemeines Persönlichkeitsrecht", True),
          ("k3", 0, "III. Gegenrecht: Meinungs- und Pressefreiheit,", True),
          (beim("k3", "mittelbar"), 1, "mittelbar über das Zivilrecht", False),
          ("k4", 0, "IV. Abwägung", True),
          (beim("k4", "Zeitablauf"), 1, "1. Zeitablauf   2. Breitenwirkung", False),
          (beim("k4", "Verhalten"), 1, "3. Verhalten des Betroffenen", False),
          (beim("k4", "abgestuften"), 1, "4. abgestufte Schutzmaßnahmen", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Begründetheit"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 96, 1: 84}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Prüfungsmaßstab"), ("k2", "Prüfschema › II. Schutzbereich"),
       ("k3", "Prüfschema › III. Gegenrecht"), ("k4", "Prüfschema › IV. Abwägung")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Zur Zeitlichkeit der Freiheit gehört", 0)],
                 [("die Möglichkeit des ", 0), ("Vergessens", "a"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "Vergessens")}),
    *markertext([[("Vergessen heißt aber ", 0), ("nicht löschen", "b"), (":", 0)],
                 [("Statt den Bericht zu ändern,", 0)], [("kann der Verlag die Auffindbarkeit", 0)],
                 [("über den Namen ", 0), ("begrenzen", "c"), (".", 0)]], 750, 480, 44, "m2",
                {"b": beim("m2", "löschen"), "c": beim("m2", "begrenzen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
