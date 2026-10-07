"""Folge 226 · Erfundenes Interview: Allgemeines Persönlichkeitsrecht im Zivilrecht – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen (Nachbildung des Klassikers BGHZ 128, 1): Am Kiosk liegt das fiktive Wochenmagazin „Funkelblatt“ (kein echter
Verlag, kein echtes Logo) mit einem erfundenen Exklusiv-Interview der fiktiven Schauspielerin Juliane Hellberg; eine Leserin
greift zu; in der Redaktion weiß Chefredakteur Kettler, dass das Interview erfunden ist; in der Kanzlei verlangt Anwalt
Dr. Ruhnau Unterlassung, Widerruf und Geldentschädigung. Die reale Person des echten Falls wird nicht gezeigt, ihr Name steht
nur als Fallbezeichnung auf der Fundstellen-Pille. Danach: § 823 Abs. 1 BGB (Wortlautkarte), sonstiges Recht (Wortlautkarten
Art. 2 Abs. 1, Art. 1 Abs. 1 GG), Rahmenrecht, Eingriff (Unterschieben nicht getaner Äußerungen), Abwägung mit der
Pressefreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 2 GG), Verschulden, Rechtsfolgen (Unterlassung, Widerruf, Geldentschädigung,
Höhe), Ergebnis, Klausurtipp, Schema, Merksatz. Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/tuer/feld als eigene Kopie aus Folge 205 (gemeinsame
Dateien unverändert); neu: regal(), tisch(), kopfbild(), heft(), platzhalter(), kiosk(), kanzlei().
Handlungsgeräusche: Tippen (A2), Anklopfen (A3); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB, GG), Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_226/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_226/" in n:
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
NAME = {"JU": "Juliane Hellberg", "KE": "Chefredakteur Kettler", "RU": "Anwalt Dr. Ruhnau", "LE": "Leserin"}
NFARBE = {"JU": PINK, "KE": BLAU, "RU": GRUEN, "LE": GELB}


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



def regal(cue, x0=60, w=420):
    """Bücherregal der Kanzlei (Grundformen, Buchrücken in Palettenfarben)."""
    y0, h = 150, BODEN - 150
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    farben = [BLAU, GRUEN, GELB, LILA, ROT, PINK, WEISS]
    fach = (h - 30) // 4
    k = 0
    for f in range(4):
        yb = o + (25 + (f + 1) * fach) * s
        dr.rectangle((o, yb, o + w * s, yb + 12 * s), fill=HOLZ, outline=INK, width=4 * s)
        xx = o + 22 * s
        for j in range(9):
            bw, bh = (30 + (j * 7) % 14) * s, int(fach * (0.62 + 0.08 * ((j + f) % 3))) * s
            if xx + bw > o + (w - 18) * s:
                break
            dr.rectangle((xx, yb - bh, xx + bw, yb), fill=farben[k % len(farben)], outline=INK, width=3 * s)
            xx += bw + 6 * s; k += 1
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0, y0, cue, "cut", 0.0, None, name="regal"))


def tisch(x, w, cue, h=200, farbe=HOLZ):
    """Schreibtisch/Theke aus Grundformen auf dem Boden."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 34 * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
    dr.rectangle((o + 24 * s, o + 34 * s, o + 54 * s, o + h * s), fill=farbe, outline=INK, width=5 * s)
    dr.rectangle((o + (w - 54) * s, o + 34 * s, o + (w - 24) * s, o + h * s), fill=farbe, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="tisch"))


_JU_KOPF = {}


def kopfbild(name="JU_froh", breite=150):
    """Brustbild der (fiktiven) Schauspielerin für das Titelblatt: Ausschnitt der Open-Peeps-Figur, nicht umgezeichnet."""
    if (name, breite) not in _JU_KOPF:
        im = Image.open(FIG + "op_226/" + name + ".png").convert("RGBA")
        bb = im.getbbox(); im = im.crop(bb)
        im = im.crop((0, 0, im.width, int(im.height * 0.36)))
        _JU_KOPF[(name, breite)] = im.resize((breite, int(im.height * breite / im.width)), Image.LANCZOS)
    return _JU_KOPF[(name, breite)]


def heft(x, y, w, h, cue, zeilen_cue=None, mini=False, bis=None, anim="cut"):
    """Titelblatt des fiktiven Magazins „Funkelblatt“ (kein echter Verlag, kein echtes Logo)."""
    els = [El(_feld(w, h, fill=GELB, rand=5, rund=10), x, y, cue, anim, 0.0, bis, name="heft"),
           El(_feld(w - 24, 70 if not mini else 50, fill=ROT, rand=4, rund=6), x + 12, y + 12, cue, anim, 0.0, bis,
              name="heftkopf")]
    gr = 40 if not mini else 30
    while F("ExtraBold", gr).getlength("FUNKELBLATT") > w - 56:
        gr -= 2
    els.append(bis_(z("FUNKELBLATT", x + 26, y + (28 if not mini else 22), cue, "ExtraBold", gr,
                      farbe=WEISS, rechts=x + w - 10), bis))
    if mini:
        return els
    zc = zeilen_cue or cue
    k = kopfbild("JU_froh", 150)
    els.append(El(k, x + w - k.width - 18, y + h - k.height - 6, zc, "pop", 0.0, bis, name="bild:titelbild"))
    els += [bis_(z("EXKLUSIV!", x + 22, y + 100, zc, "ExtraBold", 38, rechts=x + w - 10), bis),
            bis_(z("Juliane Hellberg", x + 22, y + 146, zc, "Bold", 30, rechts=x + w - 10), bis),
            bis_(z("spricht über", x + 22, y + 186, zc, "Bold", 30, rechts=x + w - 10), bis),
            bis_(z("ihre Trennung", x + 22, y + 226, zc, "Bold", 30, rechts=x + w - 10), bis)]
    return els


def platzhalter(x, y, w, h, cue, fill=BLAUHELL):
    """Weitere Hefte im Regal (ohne Titel, ohne Logo)."""
    els = [hart(feld(x, y, w, h, cue, fill=fill, rand=4, rund=8, name="heft2"))]
    for i in range(3):
        els.append(hart(feld(x + 16, y + 20 + i * 44, w - 32, 22, cue, fill=WEISS, rand=3, rund=6, name="balken")))
    return els


# ===========================================================================================================================
# A1 Fall: Am Kiosk liegt das neue „Funkelblatt“ (fiktiv) – Leserin, dann Juliane Hellberg
# ===========================================================================================================================
LEX, JUX1 = 1230, 1680
KX, KW = 90, 880                          # Kiosk


def kiosk(cue):
    els = [boden(cue)]
    # Markise (rot/weiß gestreift) und Rückwand
    els.append(hart(feld(KX, 110, KW, 70, cue, fill=ROT, rand=5, rund=10, name="markise")))
    for i in range(1, 8, 2):
        els.append(hart(feld(KX + i * KW // 8, 110, KW // 8, 70, cue, fill=WEISS, rand=4, rund=2, name="streifen")))
    els.append(hart(feld(KX + 20, 180, KW - 40, 420, cue, fill=HELLGRAU, rand=5, rund=4, name="rueckwand")))
    els.append(tisch(KX, KW, cue, h=BODEN - 600))
    return els


folie([(NULL, "Fall · Am Kiosk: das neue Funkelblatt"), ("titel", "Fall · Exklusiv auf dem Titel"),
       ("l1", "Fall · Eine Leserin greift zu"), ("nie", "Fall · Juliane Hellberg hat nie gesprochen")], [
    *kiosk(NULL),
    *platzhalter(KX + 50, 250, 190, 300, NULL, fill=BLAUHELL),
    *platzhalter(KX + KW - 240, 250, 190, 300, NULL, fill=HELLGRUEN),
    *heft(KX + 270, 200, 340, 380, NULL, zeilen_cue="titel"),
    hart(pl("Am Kiosk: das neue Funkelblatt", 70, 30, NULL, fill=GELB, size=32)),
    pl("4 Seiten Interview", KX + 300, 620, "seiten", fill=WEISS, size=32),
    *fig("LE", LEX, BODEN, FH, [(NULL, "ruhig"), ("titel", "staunt")], bis="l1", erst="cut"),
    *redet("LE_redet", LEX, BODEN, FH, "l1", "nie"),
    *fig("LE", LEX, BODEN, FH, [("nie", "froh")], erst="cut"),
    hart(ns(NAME["LE"], LEX, BODEN, NULL, GELB)),
    blase("sprech", 640, 210, "l1", 1430, 250, inhalt=["Ein Exklusiv-Interview mit", "Juliane Hellberg!",
                                                      "Das nehme ich mit."], textsize=32,
          figur=("LE_redet", LEX, BODEN, FH), bis="nie"),
    *fig("JU", JUX1, BODEN, FH, [("nie", "ernst"), ("erfunden", "sorge")]),
    ns(NAME["JU"], JUX1, BODEN, "nie", PINK, d=0.1),
    pl("Juliane Hellberg hat nie mit dem Magazin gesprochen", 1060, 30, "nie", fill=WEISS, size=28),
    pl("Jedes Wort ist erfunden.", 1060, 96, "erfunden", fill=HELLROT, size=32),
    pl("erfunden", KX + 290, 500, "erfunden", fill=HELLROT, size=32),
])

# ===========================================================================================================================
# A2 Fall: In der Redaktion (Chefredakteur Kettler, fiktiv; sachlich, keine Karikatur)
# ===========================================================================================================================
KEX = 1450
folie([("redakt", "Fall · In der Redaktion"), ("auflage", "Fall · Auflage: 400.000 Exemplare"),
       ("ke1", "Fall · Der Chefredakteur")], [
    boden("redakt"),
    tisch(160, 640, "redakt", h=230),
    hart(feld(320, 380, 330, 210, "redakt", fill=INK, rand=4, rund=14, name="monitor")),
    hart(feld(338, 398, 294, 174, "redakt", fill=WEISS, rand=3, rund=6, name="bildschirm")),
    hart(feld(458, 590, 54, 24, "redakt", fill=INK, rand=3, rund=2, name="fuss")),
    hart(feld(415, 610, 140, 14, "redakt", fill=INK, rand=3, rund=6, name="sockel")),
    hart(pl("In der Redaktion weiß man das", 70, 30, "redakt", fill=GELB, size=32)),
    *heft(860, 120, 330, 410, "redakt", anim="cut"),
    pl("Auflage: 400.000 Exemplare", 860, 560, "auflage", fill=WEISS, size=30),
    szene(z("Das Interview …", 360, 420, beim("ke1", "Interview"), "Bold", 28, rechts=625), "226tippen*", 0.8, -1.2),
    *fig("KE", KEX, BODEN, FH, [("redakt", "ruhig"), ("auflage", "froh")], bis="ke1", erst="cut"),
    *redet("KE_redet", KEX, BODEN, FH, "ke1", "kanzlei"),
    hart(ns(NAME["KE"], KEX, BODEN, "redakt", BLAU)),
    blase("sprech", 690, 250, "ke1", 1470, 250, inhalt=["Mit ihrem Namen auf dem Titel", "verkaufen wir mehr Hefte.",
                                                       "Das Interview schreiben wir", "eben selbst."], textsize=32,
          figur=("KE_redet", KEX, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Fall: In der Kanzlei (Anwalt Dr. Ruhnau, fiktiv); Frage und echter Fall als Pillen. G kehrt hierher zurück.
# ===========================================================================================================================
JUX3, RUX = 760, 1460


def kanzlei(cue):
    return [boden(cue), regal(cue), tuer(1660, cue, farbe=HOLZ)]


folie([("kanzlei", "Fall · In der Kanzlei"), ("r1", "Fall · Die Forderungen"),
       ("frage", "Die Frage · Unterlassung, Widerruf, Geldentschädigung?"),
       ("bgh", "Die Frage · BGHZ 128, 1 (Caroline von Monaco)")], [
    *kanzlei("kanzlei"),
    hart(pl("In der Kanzlei", 560, 30, "kanzlei", fill=GELB, size=32, bis="frage")),
    szene(peep_voll("JU_ernst_r", JUX3, BODEN, FH, "kanzlei", anim="pop", bis="j1"), "226klopfen*", 0.8, -0.6),
    *redet("JU_redet_r", JUX3, BODEN, FH, "j1", "r1"),
    *fig("JU", JUX3, BODEN, FH, [("r1", "denkt_r"), ("frage", "ernst_r")], erst="cut"),
    ns(NAME["JU"], JUX3, BODEN, "kanzlei", PINK),
    *fig("RU", RUX, BODEN, FH, [("kanzlei", "ruhig"), ("j1", "ernst")], bis="r1", erst="cut"),
    *redet("RU_redet", RUX, BODEN, FH, "r1", "frage"),
    *fig("RU", RUX, BODEN, FH, [("frage", "denkt")], erst="cut"),
    hart(ns(NAME["RU"], RUX, BODEN, "kanzlei", GRUEN)),
    blase("sprech", 560, 120, "j1", 900, 280, inhalt=["Ich habe nie mit diesem", "Magazin gesprochen!"], textsize=34,
          figur=("JU_redet_r", JUX3, BODEN, FH), bis="r1"),
    blase("sprech", 880, 190, "r1", 1040, 270, inhalt=["Dann verlangen wir Unterlassung, Widerruf",
                                                      "und eine Geldentschädigung."], textsize=32,
          figur=("RU_redet", RUX, BODEN, FH), bis="frage"),
    pl("Zu Recht? Und wonach richtet sich die Höhe?", 560, 30, "frage", fill=PINK, size=34),
    pl("nachgebildet: ein erfundenes Interview mit einer Prinzessin", 560, 104, "klassiker", fill=WEISS, size=30),
    pl("BGH, Urt. v. 15.11.1994 · VI ZR 56/94 · BGHZ 128, 1 (Caroline von Monaco)", 560, 170, beim("bgh", "Bundesgerichtshof"),
       fill=GELB, size=28),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_226(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=37, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_226("sv", [
    "Das Wochenmagazin „Funkelblatt“ (Auflage 400.000) titelt: „Exklusiv! Juliane Hellberg spricht über ihre Trennung.“ "
    "Im Heft folgen 4 Seiten Interview mit der Schauspielerin über ihr Privatleben.",
    "Juliane Hellberg hat nie mit dem Magazin gesprochen; jedes Wort ist erfunden. Chefredakteur Kettler wusste das: Ihr "
    "Name auf dem Titel sollte mehr Hefte verkaufen.",
    "Frau Hellberg verlangt Unterlassung, Widerruf und eine Geldentschädigung.",
], "Zu Recht? Und wonach richtet sich die Höhe der Geldentschädigung?")


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
# C1 I. Anspruchsgrundlage: § 823 Abs. 1 BGB (Wortlautkarte, vollständig vorgelesen)
# ===========================================================================================================================
PI = "I. Anspruchsgrundlage"
w823, w823_y = wortlaut(80, 250, 1100, "„(1) Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die "
                                       "Freiheit, das Eigentum oder ein sonstiges Recht eines anderen widerrechtlich "
                                       "verletzt, ist dem anderen zum Ersatz des daraus entstehenden Schadens verpflichtet.“",
                        "§ 823 Abs. 1 BGB", "w823",
                        marken=[("sonstiges Recht", beim("w823", "sonstiges")), ("widerrechtlich", beim("w823", "widerrechtlich")),
                                ("Ersatz", beim("w823", "Ersatz"))])
folie([("norm", f"{PI} · § 823 Abs. 1 BGB"), ("w823", f"{PI} › Wortlaut"), ("schema", f"{PI} › Grundschema")], [
    *tafel("norm", "I. Anspruchsgrundlage"),
    z("§ 823 Abs. 1 BGB", 110, 180, "norm", "ExtraBold", 40),
    *w823,
    zit("Grundschema: unsere Folge zu § 823 Abs. 1 BGB", 110, w823_y + 30, "schema", size=28),
    *requisit([("norm", ("tabler", "scale", 120, WEISS), "§ 823 Abs. 1", GELB),
               ("schema", ("tabler", "books", 120, BLAUHELL), "Grundschema", BLAUHELL)]),
    *stehend("JU", FX, [("norm", "ruhig"), ("w823", "denkt")]),
])

# ===========================================================================================================================
# C2 Sonstiges Recht: allgemeines Persönlichkeitsrecht (Wortlautkarten Art. 2 Abs. 1, Art. 1 Abs. 1 GG)
# ===========================================================================================================================
w21, w21_y = wortlaut(80, 420, 1100, "„(1) Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit, …“",
                      "Art. 2 Abs. 1 GG (Auszug)", "a21",
                      marken=[("freie Entfaltung", beim("a21", "freie")), ("Persönlichkeit", beim("a21", "Persönlichkeit", 1))])
w11, w11_y = wortlaut(80, w21_y + 24, 1100, "„(1) Die Würde des Menschen ist unantastbar. …“", "Art. 1 Abs. 1 Satz 1 GG", "a11",
                      marken=[("Würde des Menschen", beim("a11", "Würde")), ("unantastbar", beim("a11", "unantastbar"))])
folie([("sonst", f"{PI} › sonstiges Recht"), ("bghz13", f"{PI} › sonstiges Recht seit 1954"),
       ("wurzel", f"{PI} › Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG")], [
    *tafel("sonst", "Sonstiges Recht"),
    blk(110, 172, 1040, 80, PINK, "sonst", [("allgemeines Persönlichkeitsrecht: nicht im Gesetzestext", "ExtraBold", 31, INK)]),
    *okz("1954 vom BGH als sonstiges Recht anerkannt", 272, "bghz13", "Bold", 33),
    zit("BGHZ 13, 334; BVerfGE 34, 269 <271, 281>", 185, 318, beim("bghz13", "sonstiges")),
    z("wurzelt im Grundgesetz:", 110, 366, "wurzel", "Bold", 33),
    *w21, *w11,
    *requisit([("sonst", ("tabler", "fingerprint", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("bghz13", ("tabler", "gavel", 110, WEISS), "BGH, 1954", WEISS),
               ("wurzel", ("tabler", "shield-check", 110, GELB), "Grundgesetz", GELB)]),
    *stehend("JU", FX, [("sonst", "ruhig"), ("a11", "ernst")]),
])

# ===========================================================================================================================
# C3 Rahmenrecht: Rechtswidrigkeit erst nach Abwägung (VI ZR 211/12 Rn. 22)
# ===========================================================================================================================
folie([("rahmen", f"{PI} › ein Rahmenrecht"), ("abw", f"{PI} › Reichweite durch Abwägung")], [
    *tafel("rahmen", "Ein Rahmenrecht"),
    z("anders als Körper oder Eigentum:", 110, 190, "rahmen", "Bold", 36),
    blk(110, 250, 1040, 90, GELB, beim("rahmen", "Rahmenrecht"), [("ein Rahmenrecht", "ExtraBold", 40, INK)]),
    *neinz("Reichweite steht nicht von vornherein fest", 400, "abw", "Bold", 34, kreuz=beim("abw", "nicht")),
    *okz("rechtswidrig? erst die Abwägung mit den", 470, beim("abw", "Ob"), "Bold", 34),
    z("Belangen der anderen Seite entscheidet", 185, 516, beim("abw", "Belangen"), "Bold", 34),
    zit("BGH, Urt. v. 17.12.2013 – VI ZR 211/12, Rn. 22", 185, 572, beim("abw", "Belangen")),
    *requisit([("rahmen", ("tabler", "fingerprint", 110, PINK), "Rahmenrecht", PINK),
               ("abw", ("tabler", "scale", 130, WEISS), "Abwägung", GELB)], px=1560, pu=330, py=90),
    *paar("JU", [("rahmen", "ruhig"), ("abw", "denkt")], "KE", [("abw", "ruhig")]),
])

# ===========================================================================================================================
# D II. Eingriff: Unterschieben nicht getaner Äußerungen (BVerfGE 54, 148 LS 1, <155>; 34, 269 <282 f.>)
# ===========================================================================================================================
PII = "II. Eingriff"
folie([("mund", f"{PII} · Was schützt das Persönlichkeitsrecht?"), ("eppler", f"{PII} › Worte in den Mund gelegt"),
       ("selbst", f"{PII} › Selbstbestimmung über das eigene Wort"), ("privat", f"{PII} › Privatleben"),
       ("eingriff", f"{PII} › Eingriff (+)")], [
    *tafel("mund", "II. Eingriff"),
    z("Was schützt das Persönlichkeitsrecht hier?", 110, 180, "mund", "Bold", 36),
    blk(110, 240, 1040, 130, GELB, "eppler", [("Schutz davor, dass jemandem Äußerungen", "ExtraBold", 33, INK),
                                            ("in den Mund gelegt werden, die er nicht getan hat", "ExtraBold", 33, INK)]),
    zit("BVerfGE 54, 148 (Eppler), Leitsatz 1, <155>", 110, 382, beim("eppler", "Äußerungen")),
    *okz("selbst entscheiden, ob und wie man mit eigenen", 450, "selbst", "Bold", 33),
    z("Worten an die Öffentlichkeit tritt", 185, 496, beim("selbst", "Worten"), "Bold", 33),
    zit("BVerfGE 54, 148 <155>", 185, 544, beim("selbst", "Worten")),
    *okz("erfundenes Interview betrifft ihr Privatleben", 610, "privat", "Bold", 33),
    zit("BVerfGE 34, 269 <282 f.> (Soraya: erfundenes Interview)", 185, 656, "privat"),
    blk(110, 720, 1040, 80, HELLGRUEN, "eingriff", [("Eingriff in das Persönlichkeitsrecht: (+)", "ExtraBold", 34, INK)]),
    *requisit([("mund", ("tabler", "fingerprint", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("eppler", ("tabler", "message-off", 120, HELLROT), "nie gesagt", HELLROT),
               ("selbst", ("tabler", "microphone", 110, WEISS), "das eigene Wort", WEISS),
               ("privat", ("tabler", "lock", 110, LILAHELL), "Privatleben", LILAHELL),
               ("eingriff", ("tabler", "circle-check", 110, HELLGRUEN), "Eingriff (+)", HELLGRUEN)]),
    *stehend("JU", FX, [("mund", "ruhig"), ("eppler", "ernst"), ("privat", "sorge"), ("eingriff", "ernst")]),
])

# ===========================================================================================================================
# E1 III. Rechtswidrigkeit: Pressefreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 2 GG; BVerfGE 34, 269 <283 f.>; 54, 208 LS 2)
# ===========================================================================================================================
PIII = "III. Rechtswidrigkeit"
w52, w52_y = wortlaut(80, 240, 1100, "„… Die Pressefreiheit und die Freiheit der Berichterstattung durch Rundfunk und "
                                     "Film werden gewährleistet. …“", "Art. 5 Abs. 1 Satz 2 GG", "a52",
                      marken=[("Pressefreiheit", beim("a52", "Pressefreiheit")), ("gewährleistet", beim("a52", "gewährleistet"))])
folie([("presse", f"{PIII} · die Gegenseite: das Magazin"), ("a52", f"{PIII} › Pressefreiheit, Art. 5 Abs. 1 Satz 2 GG"),
       ("unterh", f"{PIII} › auch Unterhaltungspresse"), ("nichts", f"{PIII} › erfundenes Interview: kein Beitrag"),
       ("zitat", f"{PIII} › unrichtiges Zitat nicht geschützt")], [
    *tafel("presse", "III. Abwägung: Pressefreiheit"),
    z("Gegenseite: das Magazin", 110, 180, "presse", "Bold", 36),
    *w52,
    *okz("gilt auch für die Unterhaltungspresse", w52_y + 36, "unterh", "Bold", 33),
    zit("BVerfGE 34, 269 <283>", 830, w52_y + 44, "unterh"),
    *neinz("erfundenes Interview: kann zu einer wirklichen", w52_y + 110, "nichts", "Bold", 33,
           kreuz=beim("nichts", "nichts")),
    z("Meinungsbildung nichts beitragen", 185, w52_y + 156, beim("nichts", "Meinungsbildung"), "Bold", 33),
    zit("BVerfGE 34, 269 <283 f.> (Soraya)", 185, w52_y + 204, beim("nichts", "Meinungsbildung")),
    *neinz("unrichtiges Zitat: von der Meinungsfreiheit", w52_y + 270, "zitat", "Bold", 33, kreuz=beim("zitat", "nicht")),
    z("nicht geschützt", 185, w52_y + 316, beim("zitat", "nicht"), "Bold", 33),
    zit("BVerfGE 54, 208 (Böll), Leitsatz 2", 470, w52_y + 324, beim("zitat", "nicht")),
    *requisit([("presse", ("tabler", "news", 120, GELB), "Magazin", GELB),
               ("nichts", ("tabler", "message-off", 120, HELLROT), "erfunden", HELLROT),
               ("zitat", ("tabler", "quote-off", 110, HELLROT), "falsches Zitat", HELLROT)]),
    *stehend("KE", FX, [("presse", "ruhig"), ("nichts", "denkt"), ("zitat", "ernst")]),
])

# ===========================================================================================================================
# E2 Ergebnis der Abwägung; Verschulden: Vorsatz (BVerfGE 34, 269 <284>)
# ===========================================================================================================================
folie([("vorrang", f"{PIII} › Persönlichkeitsrecht überwiegt"), ("vors", "Verschulden · Vorsatz")], [
    *tafel("vorrang", "Abwägung und Verschulden"),
    blk(110, 180, 1040, 90, HELLGRUEN, beim("vorrang", "Persönlichkeitsrecht"),
        [("Das Persönlichkeitsrecht überwiegt", "ExtraBold", 36, INK)]),
    *okz("der Eingriff ist rechtswidrig", 310, beim("vorrang", "rechtswidrig"), "Bold", 34),
    zit("BVerfGE 34, 269 <284>: Schutz der Privatsphäre „unbedingt“ vorrangig", 185, 360, beim("vorrang", "rechtswidrig")),
    z("Verschulden:", 110, 450, "vors", "ExtraBold", 36),
    *okz("Interview bewusst erfunden: Vorsatz", 510, beim("vors", "bewusst"), "Bold", 34),
    *requisit([("vorrang", ("tabler", "scale", 140, HELLGRUEN), "Persönlichkeitsrecht", HELLGRUEN),
               ("vors", ("tabler", "writing", 120, HELLROT), "bewusst erfunden", HELLROT)], px=1560, pu=330, py=90),
    *paar("JU", [("vorrang", "froh")], "KE", [("vorrang", "denkt"), ("vors", "ernst")]),
])

# ===========================================================================================================================
# F1 IV. Rechtsfolgen: 1. Unterlassung, 2. Widerruf (VI ZR 314/10 Rn. 8; BVerfGE 97, 125 LS 1, <148 ff.>)
# ===========================================================================================================================
PIV = "IV. Rechtsfolgen"
folie([("folgen", f"{PIV} · Welche Ansprüche?"), ("unterl", f"{PIV} › 1. Unterlassung"), ("widerruf", f"{PIV} › 2. Widerruf")], [
    *tafel("folgen", "IV. Rechtsfolgen"),
    z("Welche Ansprüche hat Frau Hellberg?", 110, 180, "folgen", "Bold", 36),
    z("1. Unterlassung", 110, 250, "unterl", "ExtraBold", 36),
    z("§ 1004 Abs. 1 Satz 2 BGB analog", 160, 300, beim("unterl", "tausendvier"), size=33),
    z("i. V. m. § 823 Abs. 1 BGB", 160, 344, beim("unterl", "achthundertdreiundzwanzig"), size=33),
    *okz("das Interview nicht weiter verbreiten", 400, beim("unterl", "Magazin"), "Bold", 33),
    zit("BGH, Urt. v. 11.12.2012 – VI ZR 314/10, Rn. 8", 185, 448, beim("unterl", "Magazin")),
    z("2. Widerruf", 110, 520, "widerruf", "ExtraBold", 36),
    *okz("öffentlich klarstellen: Interview hat nie", 580, beim("widerruf", "öffentlich"), "Bold", 33),
    z("stattgefunden", 185, 626, beim("widerruf", "stattgefunden"), "Bold", 33),
    *okz("notfalls auf der Titelseite", 690, beim("widerruf", "notfalls"), "Bold", 33),
    zit("BVerfGE 97, 125, Leitsatz 1, <148 ff.>", 185, 738, beim("widerruf", "notfalls")),
    *rechts_frei([ficon("tabler", "hand-stop", 1420, 520, 150, "unterl", fuell=HELLROT, bis="widerruf"),
                  pl("Unterlassung", 1420, 560, "unterl", fill=HELLROT, size=28, anker="m", bis="widerruf")]),
    *rechts_frei(heft(1280, 230, 300, 300, "widerruf", mini=True, anim="pop")),
    pl("Richtigstellung:", 1300, 320, beim("widerruf", "klarstellen"), fill=WEISS, size=26),
    z("Das Interview hat", 1300, 380, beim("widerruf", "klarstellen"), "Bold", 26, rechts=1575),
    z("nie stattgefunden.", 1300, 416, beim("widerruf", "klarstellen"), "Bold", 26, rechts=1575),
    pl("Titelseite", 1430, 560, beim("widerruf", "Titelseite"), fill=GELB, size=28, anker="m"),
    *stehend("RU", 1735, [("folgen", "ruhig"), ("unterl", "ernst"), ("widerruf", "froh")]),
])

# ===========================================================================================================================
# F2 IV. 3. Geldentschädigung: Voraussetzungen, Abgrenzung § 253 Abs. 2 (VI ZR 211/12 Rn. 38, 40, 43 f.)
# ===========================================================================================================================
folie([("geld", f"{PIV} › 3. Geldentschädigung"), ("vor2", f"{PIV} › 3. Voraussetzungen"),
       ("schwer", f"{PIV} › 3. hier: schwerwiegend"), ("reicht", f"{PIV} › 3. Widerruf reicht nicht"),
       ("p253", f"{PIV} › 3. kein Schmerzensgeld, § 253 Abs. 2 BGB"), ("schutz", f"{PIV} › 3. Schutzauftrag Art. 1, 2 GG")], [
    *tafel("geld", "3. Geldentschädigung"),
    z("Voraussetzungen:", 110, 175, "vor2", "ExtraBold", 34),
    *okz("schwerwiegender Eingriff, der nicht in anderer", 225, beim("vor2", "schwerwiegenden"), "Bold", 32),
    z("Weise befriedigend aufgefangen werden kann", 185, 268, beim("vor2", "nicht"), "Bold", 32),
    zit("BGH VI ZR 211/12, Rn. 38; BVerfGE 34, 269 <286>", 185, 314, beim("vor2", "nicht")),
    z("Hier: erfundenes Interview über das Privatleben,", 110, 372, "schwer", size=32),
    z("groß auf dem Titel, mit Vorsatz", 110, 414, beim("schwer", "groß"), size=32),
    *okz("ein Widerruf allein gleicht das nicht aus", 474, "reicht", "Bold", 32),
    zit("Rn. 43 f. (mit BGHZ 128, 1, 13 f.)", 185, 518, "reicht"),
    *neinz("kein Schmerzensgeld nach § 253 Abs. 2 BGB:", 582, "p253", "Bold", 32, kreuz=beim("p253", "kein")),
    z("dort fehlt das Persönlichkeitsrecht", 185, 625, beim("p253", "dort"), "Bold", 32),
    blk(110, 690, 1040, 110, GELB, "schutz", [("Grundlage: Schutzauftrag aus", "ExtraBold", 32, INK),
                                            ("Art. 1 und Art. 2 Abs. 1 GG", "ExtraBold", 32, INK)]),
    zit("BGH VI ZR 211/12, Rn. 40; BVerfGE 34, 269 <292>", 110, 812, "schutz"),
    *requisit([("geld", ("tabler", "coin-euro", 120, GELB), "Geldentschädigung", GELB),
               ("schwer", ("tabler", "alert-triangle", 120, HELLROT), "schwerwiegend", HELLROT),
               ("p253", ("tabler", "ban", 110, HELLROT), "nicht § 253 Abs. 2", HELLROT),
               ("schutz", ("tabler", "shield-check", 110, GELB), "Art. 1, 2 GG", GELB)]),
    *stehend("JU", FX, [("geld", "ernst"), ("schwer", "sorge"), ("schutz", "ruhig")]),
])

# ===========================================================================================================================
# F3 Höhe: Genugtuung, Prävention, Gewinnerzielung (BGHZ 128, 1, 15 f. nach VI ZR 332/94, VI ZR 211/12 Rn. 38, 49;
# BVerfG 1 BvR 1127/96 Rn. 9)
# ===========================================================================================================================
folie([("hoehe", f"{PIV} › 3. Höhe"), ("genug", f"{PIV} › 3. Genugtuung und Prävention"),
       ("kommerz", f"{PIV} › 3. Zwangskommerzialisierung"), ("gewinn", f"{PIV} › 3. Gewinn als Bemessungsfaktor"),
       ("hemm", f"{PIV} › 3. echter Hemmungseffekt"), ("grenze", f"{PIV} › 3. Grenzen")], [
    *tafel("hoehe", "3. Höhe der Geldentschädigung"),
    *okz("im Vordergrund: Genugtuung", 175, beim("genug", "Vordergrund"), "Bold", 32),
    *okz("außerdem: Prävention", 225, beim("genug", "Prävention"), "Bold", 32),
    zit("BGH VI ZR 332/94 (im Anschluss an BGHZ 128, 1); VI ZR 255/03", 185, 271, beim("genug", "Prävention")),
    blk(110, 315, 1040, 100, WEISS, "kommerz", [("Persönlichkeit vorsätzlich als Mittel", "ExtraBold", 31, INK),
                                              ("zur Auflagensteigerung eingesetzt:", "ExtraBold", 31, INK)]),
    blk(110, 425, 1040, 70, HELLROT, beim("kommerz", "rücksichtslose"),
        [("„rücksichtslose Zwangskommerzialisierung“", "ExtraBold", 31, INK)]),
    zit("BGH VI ZR 211/12, Rn. 49 (mit BGHZ 128, 1, 15 f.)", 110, 503, beim("kommerz", "rücksichtslose")),
    *okz("Erzielung von Gewinnen: Bemessungsfaktor", 555, "gewinn", "Bold", 32),
    *okz("„echter Hemmungseffekt“", 607, "hemm", "Bold", 32),
    zit("BGH VI ZR 332/94; BVerfG, Beschl. v. 8.3.2000 – 1 BvR 1127/96, Rn. 9", 185, 652, "hemm"),
    *neinz("aber keine Gewinnabschöpfung", 712, "grenze", "Bold", 32, kreuz=beim("grenze", "nicht")),
    *neinz("Pressefreiheit nicht unverhältnismäßig einschränken", 764, beim("grenze", "Höhe"), "Bold", 32),
    zit("BGH VI ZR 211/12, Rn. 38 (mit BGHZ 128, 1, 16)", 185, 810, beim("grenze", "Höhe")),
    *requisit([("hoehe", ("tabler", "coin-euro", 120, GELB), "Höhe?", PINK),
               ("genug", ("tabler", "heart-broken", 110, PINK), "Genugtuung", PINK),
               ("kommerz", ("tabler", "chart-line", 120, HELLROT), "mehr Auflage", HELLROT),
               ("gewinn", ("tabler", "coins", 120, GELB), "Gewinn", GELB),
               ("hemm", ("tabler", "hand-stop", 120, HELLROT), "Hemmungseffekt", HELLROT),
               ("grenze", ("tabler", "scale", 130, WEISS), "Grenzen", WEISS)]),
    *stehend("KE", FX, [("hoehe", "ruhig"), ("kommerz", "denkt"), ("hemm", "ernst")]),
])

# ===========================================================================================================================
# G Ergebnis: zurück in die Kanzlei (Schauplatz A3)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Unterlassung und Widerruf"), ("erg2", "Ergebnis › Geldentschädigung"),
       ("echt", "Ergebnis › BGHZ 128, 1: Gewinn als Bemessungsfaktor")], [
    *kanzlei("erg"),
    *fig("JU", JUX3, BODEN, FH, [("erg", "ruhig_r"), (beim("erg2", "Geldentschädigung"), "froh_r")], erst="cut"),
    hart(ns(NAME["JU"], JUX3, BODEN, "erg", PINK)),
    *fig("RU", RUX, BODEN, FH, [("erg", "ruhig"), ("erg2", "froh")], erst="cut"),
    hart(ns(NAME["RU"], RUX, BODEN, "erg", GRUEN)),
    *okz("Unterlassung und Widerruf: (+)", 40, beim("erg", "Unterlassung"), "Bold", 32, x=600, rechts=1880),
    *okz("Geldentschädigung: (+), bei der Höhe zählt", 100, "erg2", "Bold", 32, x=600, rechts=1880),
    z("auch der angestrebte Gewinn", 600, 146, beim("erg2", "angestrebten"), "Bold", 32, rechts=1880),
    pl("BGHZ 128, 1: Gewinnerzielung als Bemessungsfaktor", 555, 210, "echt", fill=GELB, size=30),
    ficon("tabler", "coin-euro", 1110, BODEN, 130, beim("erg2", "Geldentschädigung"), fuell=GELB),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Ansprüche getrennt prüfen"), ("tipp2", "Klausurtipp · Rechtswidrigkeit durch Abwägung"),
       ("tipp3", "Klausurtipp · nicht § 253 Abs. 2 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Unterlassung, Widerruf und", 200, 200, "tipp", "Bold", 35),
    z("Geldentschädigung getrennt prüfen", 200, 250, beim("tipp", "Geldentschädigung"), "Bold", 35),
    z("jeder Anspruch: eigene Voraussetzungen", 200, 304, beim("tipp", "jeder"), size=34),
    linienzug([(130, 372), (1130, 372)], "tipp2", breite=3),
    *neinz("2. Rechtswidrigkeit nicht indiziert:", 400, "tipp2", "Bold", 34, x=200, kreuz=beim("tipp2", "nicht")),
    z("begründen mit der Abwägung", 200, 452, beim("tipp2", "begründest"), size=34),
    blk(130, 530, 1000, 170, GELB, "tipp3", [("3. Geldentschädigung: nicht § 253 Abs. 2,", "ExtraBold", 33, INK),
                                          ("sondern § 823 Abs. 1 BGB i. V. m.", "ExtraBold", 33, INK),
                                          ("Art. 1 Abs. 1, Art. 2 Abs. 1 GG", "ExtraBold", 33, INK)]),
    zit("BGH VI ZR 211/12, Rn. 22, 40", 200, 712, "tipp3"),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Eingriff in das allgemeine Persönlichkeitsrecht", True),
          (beim("s1", "sonstiges"), 1, "als sonstiges Recht, § 823 Abs. 1 BGB", False),
          ("s2", 0, "2. Rechtswidrigkeit nach Abwägung", True),
          ("s3", 0, "3. Verschulden", True),
          ("s4", 0, "4. schwerwiegende Verletzung,", True),
          ("s4b", 1, "nicht anders befriedigend aufzufangen", False),
          ("s5", 0, "5. Höhe: Genugtuung, Prävention,", True),
          (beim("s5", "angestrebtem"), 1, "angestrebter Gewinn", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Geldentschädigung"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 92, 1: 84}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › 1. Eingriff"), ("s2", "Prüfschema › 2. Rechtswidrigkeit"),
       ("s3", "Prüfschema › 3. Verschulden"), ("s4", "Prüfschema › 4. schwerwiegend"), ("s5", "Prüfschema › 5. Höhe")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer einem Menschen Worte", 0)], [("in den Mund legt", "a"), (", verletzt", 0)],
                 [("sein Persönlichkeitsrecht.", 0)]], 750, 270, 44, "merke",
                {"a": beim("merke", "Mund")}),
    *markertext([[("Und wer damit vorsätzlich Auflage macht,", 0)], [("muss mit einer ", 0), ("Geldentschädigung", "b")],
                 [("rechnen, die auch den", 0)], [("angestrebten Gewinn", "c"), (" berücksichtigt.", 0)]],
                750, 500, 44, "m2", {"b": beim("m2", "Geldentschädigung"), "c": beim("m2", "angestrebten")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
