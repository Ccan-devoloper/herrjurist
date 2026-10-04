"""Folge 188 · Baugenehmigung Schema: Bauplanungs- und Bauordnungsrecht – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Herr Hasenkamp will auf seiner Wiese weit draußen vor dem Dorf (ringsum Felder, kein Bebauungsplan,
Flächennutzungsplan: Fläche für die Landwirtschaft) eine Betongarage mit 40 m² für zwei Oldtimer bauen; Frau Ortmann von der
Bauaufsichtsbehörde lehnt ab. Szenen laut ../SZENENPLAN.md: A1 Wiese, A2 Bauaufsichtsbehörde, B Sachverhalt, C Anspruch
(Wortlautkarten Art. 68 Abs. 1 S. 1 BayBO, § 74 Abs. 1 S. 1 BauO NRW 2018), D Länder-Overlay (Tabelle), E Kompetenz
(Wortlautkarten Art. 74 Abs. 1 Nr. 18, Art. 70 Abs. 1 GG), F1 I. Genehmigungsbedürftigkeit (Wortlautkarte Art. 55 Abs. 1
BayBO), F2 Ausnahmen und II. Bauantrag, G III. 1. Verfahren und Prüfprogramm, H III. 2. Bauplanungsrecht (Wortlautkarte
§ 29 Abs. 1 BauGB, Weiche), I § 35 (nur Ergebnis, Verweis 085), J1 III. 3. Bauordnungsrecht und Ergebnis, J2 zurück auf der
Wiese, K Prüfschema, L Klausurtipp (Lexi), M Merksatz (Lexi).
Handlungsgeräusch: Stempel „abgelehnt“ auf dem Bauantrag (A2); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 186 (gemeinsame Dateien unverändert); neu: landschaft(), garage(), stempel(), tabelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BauGB, GG), recht.nrw.de
(BauO NRW 2018, Fassung ab 01.09.2026) und der Lesefassung des Bayerischen Staatsministeriums für Wohnen, Bau und Verkehr
(Quelle BAYERN.RECHT, Fassung ab 01.01.2026; Änderungen 2026 per GVBl. geprüft), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_188/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_188/" in n:
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
NAME = {"HA": "Herr Hasenkamp", "OR": "Frau Ortmann"}
NFARBE = {"HA": BEIGE, "OR": ROSE}


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


def zwei(folge_l, folge_r, links="OR", rechts="HA"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)




import math

# --- eigene Szenenbausteine Folge 188 ----------------------------------------------------------------------------------------
HORIZONT = 640


def landschaft(c):
    """Feldflur vor dem Dorf (Grundform): Horizontlinie, drei Feldstreifen mit Furchen, Tuschekonturen."""
    def zz(dr, s):
        w, h = 1800, BODEN_Y - HORIZONT
        baender = [(0, 70, FELD1), (70, 160, FELD2), (160, h, FELD3)]
        for y0, y1, f in baender:
            dr.rectangle((0, y0 * s, w * s, y1 * s), fill=f)
            dr.line((0, y0 * s, w * s, y0 * s), fill=INK, width=4 * s)
        for k in range(14):                      # Furchen im mittleren und unteren Feld
            x = 40 + k * 130
            dr.line(((x) * s, 95 * s, (x + 60) * s, 95 * s), fill=(120, 160, 110, 255), width=3 * s)
            dr.line(((x + 40) * s, 205 * s, (x + 120) * s, 205 * s), fill=(110, 150, 100, 255), width=3 * s)
    return hart(El(_flaeche(1800, BODEN_Y - HORIZONT, zz), 60, HORIZONT, c, "cut", 0.0, None, name="landschaft"))


def garage(c, x0, unten, w=380, h=200, geplant=True, bis=None, anim="pop"):
    """Garage als Zeichnung: geplant = gestrichelte Kontur (noch nicht gebaut) mit angedeutetem Schwingtor."""
    def zz(dr, s):
        def strich(p0, p1):
            (xa, ya), (xb, yb) = p0, p1
            n = max(1, int(math.hypot(xb - xa, yb - ya) / 22))
            for i in range(n):
                if i % 2 == 0:
                    t0, t1 = i / n, (i + 1) / n
                    dr.line(((xa + (xb - xa) * t0) * s, (ya + (yb - ya) * t0) * s,
                             (xa + (xb - xa) * t1) * s, (ya + (yb - ya) * t1) * s), fill=INK, width=5 * s)
        if geplant:
            dr.rectangle((4 * s, 4 * s, (w - 4) * s, (h - 4) * s), fill=(255, 255, 255, 150))
            for p0, p1 in [((4, 4), (w - 4, 4)), ((w - 4, 4), (w - 4, h - 4)), ((4, h - 4), (4, 4))]:
                strich(p0, p1)
            for p0, p1 in [((40, 50), (w - 40, 50)), ((40, 50), (40, h - 4)), ((w - 40, 50), (w - 40, h - 4))]:
                strich(p0, p1)
    return El(_flaeche(w, h, zz), x0, unten - h, c, anim, 0.0, bis, name="garage")


def aushang(c, x0, y0, w, h):
    """Pinnwand an der Wand der Behörde (Grundform), darauf erscheinen Plan und Traktor."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(240, 222, 190, 255), outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="aushang"))


def stempel(text, cx, cy, cue, farbe=DROT, size=40, winkel=12):
    """Stempelabdruck (Rahmen und Text in Dunkelrot), leicht gedreht."""
    f = F("ExtraBold", size)
    tw = int(f.getlength(text)); w, h = tw + 50, int(size * 1.6)
    im = Image.new("RGBA", (w, h))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((3, 3, w - 4, h - 4), 10, fill=(255, 255, 255, 235), outline=farbe, width=6)
    d.text((w / 2, h / 2), glyphen(text), font=f, fill=farbe, anchor="mm")
    im = im.rotate(winkel, expand=True, resample=Image.BICUBIC)
    return El(im, cx - im.width / 2, cy - im.height / 2, cue, "pop", 0.0, None, name="stempel:" + text)


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


# ===========================================================================================================================
# A1 Fall: die Wiese weit draußen vor dem Dorf
# ===========================================================================================================================
HAX = 1450
GX0, GU = 640, 890                            # geplante Garage: linke Kante, Unterkante
folie([(NULL, "Fall · Die Wiese vor dem Dorf"), ("plan", "Fall · Die geplante Garage"), ("antrag", "Fall · Der Bauantrag"),
       ("ha1", "Fall · Herr Hasenkamp ist zuversichtlich")], [
    landschaft(NULL),
    boden(NULL),
    hart(ficon("fluent-emoji-high-contrast", "houses", 230, HORIZONT + 4, 210, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "building-church", 380, HORIZONT + 4, 90, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 1700, HORIZONT + 6, 120, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 470, HORIZONT + 6, 90, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "sun", 1720, 250, 120, NULL, fuell=GELB, anim="cut")),
    hart(pl("Wiese vor dem Dorf", 70, 30, NULL, fill=GRUEN, size=38)),
    pl("ringsum nur Felder", 70, 110, beim("fall", "Felder"), fill=WEISS, size=34),
    hart(pl("Dorf", 230, HORIZONT - 230, NULL, fill=WEISS, size=28, anker="m")),
    *fig("HA", HAX, BODEN_Y, FHA, [(NULL, "ruhig"), ("plan", "froh")], erst="cut", bis="ha1"),
    hart(ns(NAME["HA"], HAX, BODEN_Y, NULL, NFARBE["HA"])),
    garage(beim("plan", "Garage"), GX0, GU),
    ficon("tabler", "car", GX0 + 105, GU - 12, 130, beim("plan", "zwei"), fuell=ROT),
    ficon("tabler", "car", GX0 + 275, GU - 12, 130, beim("plan", "Oldtimer"), fuell=BLAU),
    pl("geplant: Garage · 40 m² · Beton", GX0 + 190, 545, beim("plan", "vierzig"), fill=GELB, size=32, anker="m"),
    ficon("tabler", "file-text", 1210, BODEN_Y, 90, "antrag", fuell=WEISS),
    pl("Bauantrag", 1210, 700, "antrag", fill=WEISS, size=30, anker="m"),
    *redet("HA_redet", HAX, BODEN_Y, FHA, "ha1", "amt"),
    blase("sprech", 860, 230, "ha1", 1000, 290, inhalt=["Die Garage erfüllt jeden Brandschutz", "und hält alle Abstände ein.",
                                                     "Was soll da schiefgehen?"], textsize=34,
          figur=("HA_redet", HAX, BODEN_Y, FHA), bis="amt"),
    *okz("Brandschutz", 190, beim("ha1", "Brandschutz"), "Bold", 34, x=120),
    *okz("Abstände", 250, beim("ha1", "Abstände"), "Bold", 34, x=120),
])

# ===========================================================================================================================
# A2 Fall: bei der Bauaufsichtsbehörde – Frau Ortmann lehnt ab (Stempel)
# ===========================================================================================================================
ORX, HA2 = 640, 1360
folie([("amt", "Fall · Bei der Bauaufsichtsbehörde"), ("kbpl", "Fall · kein Bebauungsplan"),
       ("fnp", "Fall · Flächennutzungsplan: Landwirtschaft"), ("or1", "Fall · Die Ablehnung"),
       ("frage", "Fall · Anspruch auf die Baugenehmigung?"), ("frage2", "Fall · zwei Ebenen")], [
    boden("amt"),
    fenster("amt", 1520, 300, w=260, h=220),
    schreibtisch("amt", 780, 1140, h=160),
    hart(pl("Bauaufsichtsbehörde", 70, 30, "amt", fill=BLAU, size=38)),
    ficon("tabler", "file-text", 960, BODEN_Y - 160, 100, beim("amt", "Antrag"), fuell=WEISS),
    pl("Bauantrag Hasenkamp", 960, 568, beim("amt", "Antrag"), fill=WEISS, size=28, anker="m"),
    *fig("OR", ORX, BODEN_Y, FHA, [("amt", "denkt_r"), ("fnp", "ernst_r")], erst="pop", bis="or1"),
    *redet("OR_redet_r", ORX, BODEN_Y, FHA, "or1", "frage"),
    *fig("OR", ORX, BODEN_Y, FHA, [("frage", "ruhig_r")], erst="cut"),
    ns(NAME["OR"], ORX, BODEN_Y, "amt", NFARBE["OR"], d=0.1),
    *fig("HA", HA2, BODEN_Y, FHA, [("amt", "stolz"), ("or1", "sorge"), ("frage", "skeptisch")], erst="pop"),
    ns(NAME["HA"], HA2, BODEN_Y, "amt", NFARBE["HA"], d=0.1),
    *neinz("kein Bebauungsplan", 115, "kbpl", "Bold", 34, x=120, bis="or1"),
    aushang("amt", 790, 385, 340, 150),
    ficon("tabler", "map", 880, 515, 100, "fnp", fuell=GRUEN),
    ficon("fluent-emoji-high-contrast", "tractor", 1040, 515, 100, beim("fnp", "Landwirtschaft"), fuell=GELB),
    pl("Flächennutzungsplan: Fläche für die Landwirtschaft", 70, 185, "fnp", fill=GRUEN, size=32, bis="or1"),
    blase("sprech", 820, 230, "or1", 1110, 245, inhalt=["Ihre Garage mag sicher sein.", "Aber sie steht im Außenbereich.",
                                                     "Ich lehne den Antrag ab."], textsize=34,
          figur=("OR_redet_r", ORX, BODEN_Y, FHA), bis="frage"),
    szene(stempel("ABGELEHNT", 960, 690, beim("or1", "lehne"), size=30), "188stempel*", 1.0, 0.0),
    pl("Anspruch auf die Baugenehmigung?", 70, 115, "frage", fill=PINK, size=36),
    pl("Ebene 1: Bauplanungsrecht", 70, 195, beim("frage2", "Bauplanungsrecht"), fill=GRUEN, size=34),
    pl("Ebene 2: Bauordnungsrecht", 70, 275, beim("frage2", "Bauordnungsrecht"), fill=BLAU, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_188(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_188("sv", [
    "Herr Hasenkamp besitzt eine Wiese weit draußen vor dem Dorf; ringsum liegen nur Felder. Dort will er eine Garage "
    "aus Beton mit 40 m² für seine zwei Oldtimer bauen. Sie hält die Abstandsflächen ein und erfüllt die Anforderungen an "
    "den Brandschutz. Er stellt einen ordnungsgemäßen Bauantrag.",
    "Für die Wiese gilt kein Bebauungsplan. Der Flächennutzungsplan der Gemeinde stellt sie als Fläche für die "
    "Landwirtschaft dar. Herr Hasenkamp betreibt keine Landwirtschaft.",
    "Frau Ortmann von der Bauaufsichtsbehörde lehnt den Bauantrag ab: Die Garage stehe im Außenbereich.",
], "Hat Herr Hasenkamp einen Anspruch auf die Baugenehmigung?")

# ===========================================================================================================================
# C Anspruchsgrundlage: Art. 68 Abs. 1 S. 1 BayBO, § 74 Abs. 1 S. 1 BauO NRW 2018 (Wortlaut)
# ===========================================================================================================================
PA = "Anspruch"
W68 = ("„Die Baugenehmigung ist zu erteilen, wenn dem Bauvorhaben keine öffentlich-rechtlichen Vorschriften "
       "entgegenstehen, die im bauaufsichtlichen Genehmigungsverfahren zu prüfen sind; …“")
w68, w68_y = wortlaut(80, 165, 1100, W68, "Art. 68 Abs. 1 S. 1 BayBO", "by68", marken=[
    ("ist zu erteilen", beim("by68", "erteilen")), ("entgegenstehen", beim("by68", "entgegenstehen")),
    ("zu prüfen sind", beim("by68", "prüfen"))], size=30)
W74 = "„Die Baugenehmigung ist zu erteilen, wenn dem Vorhaben keine öffentlich-rechtlichen Vorschriften entgegenstehen.“"
w74, w74_y = wortlaut(80, w68_y + 22, 1100, W74, "§ 74 Abs. 1 S. 1 BauO NRW 2018", "nrw74", marken=[
    ("entgegenstehen.", beim("nrw74", "ohne"))], size=30)
folie([("anspr", f"{PA} · Landesbauordnung (Beispiele: Bayern, NRW)"), ("by68", f"{PA} › Art. 68 Abs. 1 S. 1 BayBO"),
       ("nrw74", f"{PA} › § 74 Abs. 1 S. 1 BauO NRW 2018"), ("gebunden", f"{PA} › gebundene Entscheidung"),
       ("anspr2", f"{PA} › wenn nichts entgegensteht")], rechts_frei([
    *tafel("anspr", "Anspruch auf die Baugenehmigung"),
    *w68, *w74,
    blk(110, w74_y + 25, 1040, 76, GELB, "gebunden", [("„ist zu erteilen“ = gebundene Entscheidung", "ExtraBold", 32, INK)]),
    *okz("nichts steht entgegen: Anspruch", w74_y + 130, "anspr2", "ExtraBold", 34, x=160),
    *requisit([("anspr", ("tabler", "file-certificate", 100, WEISS), "Baugenehmigung?", WEISS),
               ("by68", ("tabler", "map-pin", 90, BLAU), "Bayern", BLAU),
               ("nrw74", ("tabler", "map-pin", 90, GRUEN), "Nordrhein-Westfalen", GRUEN),
               ("gebunden", ("tabler", "scale", 100, GELB), "gebunden", GELB),
               ("anspr2", ("tabler", "circle-check", 100, HELLGRUEN), "Anspruch", HELLGRUEN)]),
    *allein("HA", [("anspr", "ruhig"), ("anspr2", "froh")]),
]))
assert w74_y + 175 <= 890, w74_y

# ===========================================================================================================================
# D Länder-Overlay: Tabelle Bayern / Nordrhein-Westfalen
# ===========================================================================================================================
PT = "Länder-Overlay"
tab, tab_y = tabelle(110, 190, [400, 320, 320], [
    ("tab", ["", "BayBO", "BauO NRW 2018"]),
    ("tab1", ["Genehmigungspflicht", "Art. 55 Abs. 1", "§ 60 Abs. 1"]),
    ("tab2", ["vereinfachtes Verfahren", "Art. 59", "§ 64"]),
    ("tab3", ["Anspruch", "Art. 68 Abs. 1 S. 1", "§ 74 Abs. 1 S. 1"])])
folie([("tab", f"{PT} · gleiche Struktur, andere Nummern"), ("tab1", f"{PT} › Genehmigungspflicht"),
       ("tab2", f"{PT} › vereinfachtes Verfahren"), ("tab3", f"{PT} › Anspruch"),
       ("eigen", f"{PT} › andere Länder: eigene LBO prüfen")], rechts_frei([
    *tafel("tab", "Länder-Overlay: Bayern und NRW"),
    *tab,
    pl("Andere Länder: ähnlich – Nummern in deiner LBO nachschlagen", 110, tab_y + 50, "eigen", fill=PINK, size=30),
    *requisit([("tab", ("tabler", "table", 100, WEISS), "2 Beispielländer", WEISS),
               ("eigen", ("tabler", "map-2", 100, HELLGRUEN), "deine LBO", HELLGRUEN)]),
    *allein("OR", [("tab", "ruhig"), ("eigen", "froh")]),
]))
assert tab_y + 200 <= 890

# ===========================================================================================================================
# E Kompetenz: Art. 74 Abs. 1 Nr. 18 GG, Art. 70 Abs. 1 GG (Wortlaut)
# ===========================================================================================================================
PK = "Kompetenz"
W7418 = ("„(1) Die konkurrierende Gesetzgebung erstreckt sich auf folgende Gebiete: … 18. den städtebaulichen "
         "Grundstücksverkehr, das Bodenrecht (ohne das Recht der Erschließungsbeiträge) …“")
wg1, wg1_y = wortlaut(80, 165, 1100, W7418, "Art. 74 Abs. 1 Nr. 18 GG", "gg74", marken=[
    ("konkurrierende Gesetzgebung", beim("gg74", "konkurrierende")), ("das Bodenrecht", beim("gg74", "Bodenrecht"))], size=30)
W70 = "„(1) Die Länder haben das Recht der Gesetzgebung, soweit dieses Grundgesetz nicht dem Bunde Gesetzgebungsbefugnisse verleiht.“"
wg2, wg2_y = wortlaut(80, wg1_y + 120, 1100, W70, "Art. 70 Abs. 1 GG", "gg70", marken=[
    ("Die Länder", beim("gg70", "Ländern"))], size=30)
folie([("komp", f"{PK} · Warum zwei Ebenen?"), ("gg74", f"{PK} › Bund: Bodenrecht, Art. 74 Abs. 1 Nr. 18 GG"),
       ("bodenr", f"{PK} › Bauplanungsrecht: BauGB"), ("gg70", f"{PK} › Länder: Art. 70 Abs. 1 GG"),
       ("ordn", f"{PK} › Bauordnungsrecht: Landesbauordnungen")], rechts_frei([
    *tafel("komp", "Wer regelt was?"),
    *wg1,
    blk(110, wg1_y + 18, 1040, 80, GRUEN, "bodenr", [("Bund: Bauplanungsrecht (BauGB) – Darf hier gebaut werden?", "ExtraBold", 30, INK)]),
    *wg2,
    blk(110, wg2_y + 18, 1040, 80, BLAU, "ordn", [("Länder: Bauordnungsrecht – Gefahrenabwehr, Verfahren", "ExtraBold", 30, INK)]),
    *requisit([("komp", ("tabler", "scale", 100, WEISS), "Gesetzgebungskompetenz", WEISS),
               ("gg74", ("tabler", "building-bank", 100, GRUEN), "Bund", GRUEN),
               ("gg70", ("tabler", "map-2", 100, BLAU), "Länder", BLAU)]),
    *zwei([("komp", "ruhig"), ("ordn", "froh")], [("komp", "skeptisch"), ("bodenr", "ruhig")]),
]))
assert wg2_y + 110 <= 890, wg2_y

# ===========================================================================================================================
# F1 I. Genehmigungsbedürftigkeit: Art. 55 Abs. 1 BayBO (Wortlaut), § 60 Abs. 1 BauO NRW 2018
# ===========================================================================================================================
PG = "I. Genehmigungsbedürftigkeit"
W55 = ("„(1) Die Errichtung, Änderung und Nutzungsänderung von Anlagen bedürfen der Baugenehmigung, soweit in Art. 56 bis "
       "58, 72 und 73 nichts anderes bestimmt ist.“")
w55, w55_y = wortlaut(80, 165, 1100, W55, "Art. 55 Abs. 1 BayBO", "by55", marken=[
    ("Errichtung", beim("by55", "Errichtung")), ("der Baugenehmigung,", beim("by55", "Baugenehmigung")),
    ("nichts anderes", beim("by55", "Ausnahme")), ("bestimmt ist", beim("by55", "Ausnahme"))], size=30)
W60 = ("„(1) Die Errichtung, Änderung, Nutzungsänderung und Beseitigung von Anlagen bedürfen der Baugenehmigung, soweit in "
       "den §§ 61 bis 63, 78 und 79 nichts anderes bestimmt ist.“")
w60, w60_y = wortlaut(80, w55_y + 22, 1100, W60, "§ 60 Abs. 1 BauO NRW 2018", "nrw60", marken=[
    ("Beseitigung", beim("nrw60", "Beseitigung"))], size=30)
folie([("gb", f"{PG} · Braucht die Garage eine Genehmigung?"), ("by55", f"{PG} › Art. 55 Abs. 1 BayBO"),
       ("nrw60", f"{PG} › § 60 Abs. 1 BauO NRW 2018")], rechts_frei([
    *tafel("gb", "I. Genehmigungsbedürftigkeit"),
    *w55, *w60,
    *requisit([("gb", ("tabler", "file-text", 100, WEISS), "Genehmigung nötig?", WEISS),
               ("by55", ("tabler", "map-pin", 90, BLAU), "Bayern", BLAU),
               ("nrw60", ("tabler", "map-pin", 90, GRUEN), "NRW: auch Beseitigung", GRUEN)]),
    *allein("HA", [("gb", "skeptisch"), ("by55", "ruhig")]),
]))
assert w60_y <= 890

# ===========================================================================================================================
# F2 Ausnahmen (verfahrensfrei, Freistellung) und II. Bauantrag
# ===========================================================================================================================
folie([("frei", f"{PG} › verfahrensfrei? Garagen bis 50 m²"), ("ausser", f"{PG} › nicht im Außenbereich"),
       ("freist", f"{PG} › Freistellung? kein Bebauungsplan"), ("pflicht", f"{PG} › genehmigungspflichtig (+)"),
       ("ba", "II. Bauantrag › ordnungsgemäß (unterstellt)")], rechts_frei([
    *tafel("frei", "Ausnahmen? Nicht für diese Garage"),
    z("verfahrensfrei: kleine Garagen bis 50 m²", 110, 190, "frei", "Bold", 34),
    z("(weitere Maße je Land)", 110, 240, beim("frei", "Maßgaben"), size=30),
    *neinz("… aber nicht im Außenbereich", 295, "ausser", "ExtraBold", 34, x=160),
    zit("Art. 57 Abs. 1 Nr. 1 Buchst. b BayBO · § 62 Abs. 1 S. 1 Nr. 1 Buchst. b BauO NRW 2018", 110, 350, "frei"),
    *neinz("Freistellung: nur mit qualifiziertem oder", 420, "freist", "Bold", 32, x=160),
    z("vorhabenbezogenem Bebauungsplan – fehlt", 160, 466, "freist", "Bold", 32),
    zit("Art. 58 Abs. 1 S. 1 Nr. 1 BayBO · § 63 Abs. 2 S. 1 Nr. 1 BauO NRW 2018", 110, 518, "freist"),
    blk(110, 575, 1040, 76, HELLROT, "pflicht", [("Die Garage ist genehmigungspflichtig.", "ExtraBold", 34, INK)]),
    *okz("II. Bauantrag ordnungsgemäß (unterstellt)", 690, "ba", "ExtraBold", 34, x=160),
    zit("Art. 64 BayBO · § 70 BauO NRW 2018", 160, 742, "ba"),
    *requisit([("frei", ("tabler", "car-garage", 110, WEISS), "Garage: 40 m²", WEISS),
               ("ausser", ("fluent-emoji-high-contrast", "sheaf-of-rice", 90, GELB), "Außenbereich", HELLROT),
               ("freist", ("tabler", "map", 100, WEISS), "kein Bebauungsplan", WEISS),
               ("pflicht", ("tabler", "file-certificate", 100, HELLROT), "Genehmigung nötig", HELLROT),
               ("ba", ("tabler", "file-text", 100, HELLGRUEN), "Bauantrag gestellt", HELLGRUEN)]),
    *allein("HA", [("frei", "froh"), ("ausser", "sorge"), ("ba", "ruhig")]),
]))

# ===========================================================================================================================
# G III. 1. Verfahrensart und Prüfprogramm: Art. 59 BayBO, § 64 BauO NRW 2018; Brandschutz
# ===========================================================================================================================
PV = "III. 1. Verfahrensart"
folie([("gf", "III. Genehmigungsfähigkeit"), ("verf", f"{PV} · Welches Verfahren?"), ("sonder", f"{PV} › kein Sonderbau"),
       ("verein", f"{PV} › vereinfachtes Verfahren"), ("prog", f"{PV} › Prüfprogramm"),
       ("p1", f"{PV} › Prüfprogramm: §§ 29–38 BauGB"), ("p2", f"{PV} › Prüfprogramm: Abstandsflächen, örtliche Bauvorschriften"),
       ("p3", f"{PV} › Prüfprogramm: beantragte Abweichungen"), ("p4", f"{PV} › Prüfprogramm: andere Vorschriften"),
       ("brand", f"{PV} › Brandschutz: grundsätzlich nicht geprüft"), ("trotz", f"{PV} › Brandschutz: trotzdem einzuhalten")],
      rechts_frei([
    *tafel("gf", "III. Genehmigungsfähigkeit"),
    z("1. Verfahrensart und Prüfprogramm", 110, 172, "verf", "ExtraBold", 34),
    *neinz("Sonderbau? nein", 225, "sonder", "Bold", 32, x=160),
    blk(110, 277, 1040, 70, GELB, "verein", [("vereinfachtes Baugenehmigungsverfahren", "ExtraBold", 32, INK)]),
    zit("Art. 59 S. 1 BayBO · § 64 Abs. 1 S. 1 BauO NRW 2018", 110, 355, "verein"),
    z("Prüfprogramm:", 110, 405, "prog", "ExtraBold", 32),
    *okz("Bauplanungsrecht, §§ 29–38 BauGB", 450, "p1", "Bold", 32, x=160),
    *okz("Abstandsflächen, örtliche Bauvorschriften", 497, "p2", "Bold", 32, x=160),
    zit("NRW zusätzlich §§ 4, 48, 49 BauO NRW 2018", 160, 542, "p2"),
    *okz("beantragte Abweichungen", 585, "p3", "Bold", 32, x=160),
    *okz("bestimmte andere öffentlich-rechtliche Vorschriften", 632, "p4", "Bold", 32, x=160),
    *neinz("Brandschutz: grundsätzlich nicht geprüft", 695, "brand", "ExtraBold", 32, x=160),
    zit("Art. 62b Abs. 2 S. 2 BayBO · § 64 Abs. 1 S. 2 BauO NRW 2018", 160, 741, "brand"),
    z("… aber trotzdem einzuhalten", 160, 790, "trotz", "ExtraBold", 32),
    zit("Art. 55 Abs. 2 BayBO · § 60 Abs. 2 BauO NRW 2018", 160, 836, "trotz"),
    *requisit([("gf", ("tabler", "list-check", 100, WEISS), "Genehmigungsfähigkeit", WEISS),
               ("verein", ("tabler", "file-text", 100, GELB), "vereinfachtes Verfahren", GELB),
               ("prog", ("tabler", "list-check", 100, HELLGRUEN), "Prüfprogramm", HELLGRUEN),
               ("brand", ("fluent-emoji-high-contrast", "fire-extinguisher", 80, ROT), "Brandschutz: nicht geprüft", HELLROT),
               ("trotz", ("fluent-emoji-high-contrast", "fire-extinguisher", 80, ROT), "aber einzuhalten", GELB)]),
    *zwei([("gf", "ruhig"), ("prog", "ernst"), ("trotz", "froh")], [("gf", "ruhig"), ("brand", "stolz"), ("trotz", "skeptisch")]),
]))

# ===========================================================================================================================
# H III. 2. Bauplanungsrecht: § 29 Abs. 1 BauGB (Wortlaut), Weiche §§ 30, 34, 35
# ===========================================================================================================================
PB = "III. 2. Bauplanungsrecht"
W29 = ("„(1) Für Vorhaben, die die Errichtung, Änderung oder Nutzungsänderung von baulichen Anlagen zum Inhalt haben, … "
       "gelten die §§ 30 bis 37.“")
w29, w29_y = wortlaut(80, 165, 1100, W29, "§ 29 Abs. 1 BauGB", "p29", marken=[
    ("Errichtung", beim("p29", "Errichtung")), ("baulichen Anlagen", beim("p29", "baulichen")),
    ("§§ 30 bis 37", beim("p29", "Paragrafen"))], size=30)
WY = w29_y + 120
folie([("bpl", f"{PB} · das Herzstück"), ("p29", f"{PB} › § 29 Abs. 1 BauGB: Vorhaben"), ("vorh", f"{PB} › Garage = Vorhaben (+)"),
       ("weiche", f"{PB} › Welcher Bereich?"), ("w30", f"{PB} › § 30 BauGB: Bebauungsplan? nein"),
       ("w34", f"{PB} › § 34 BauGB: Innenbereich? nein"), ("w35", f"{PB} › Außenbereich, § 35 BauGB")], rechts_frei([
    *tafel("bpl", "III. 2. Bauplanungsrecht"),
    *w29,
    *okz("Garage = bauliche Anlage, ihr Bau = Vorhaben", w29_y + 30, "vorh", "Bold", 32, x=160),
    z("Die Weiche:", 110, WY, "weiche", "ExtraBold", 34),
    *neinz("§ 30: Gilt ein Bebauungsplan? nein", WY + 55, "w30", "Bold", 32, x=160),
    *neinz("§ 34: im Zusammenhang bebauter Ortsteil? nein", WY + 105, "w34", "Bold", 32, x=160),
    blk(110, WY + 165, 1040, 76, GRUEN, "w35", [("Außenbereich, § 35 BauGB", "ExtraBold", 34, INK)]),
    zit("BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 11", 110, WY + 255, "w35"),
    *requisit([("bpl", ("tabler", "map", 100, GRUEN), "Darf hier gebaut werden?", GRUEN),
               ("vorh", ("tabler", "car-garage", 110, WEISS), "Vorhaben", WEISS),
               ("w30", ("tabler", "map", 100, HELLROT), "kein Bebauungsplan", HELLROT),
               ("w34", ("fluent-emoji-high-contrast", "houses", 120, WEISS), "kein Ortsteil", HELLROT),
               ("w35", ("fluent-emoji-high-contrast", "sheaf-of-rice", 90, GELB), "Außenbereich", GRUEN)]),
    *zwei([("bpl", "ruhig"), ("w35", "ernst")], [("bpl", "ruhig"), ("w34", "sorge")]),
]))
assert WY + 300 <= 890, WY

# ===========================================================================================================================
# I § 35 BauGB: sonstiges Vorhaben, öffentliche Belange (nur Ergebnis, Verweis Folge 085)
# ===========================================================================================================================
P35 = "III. 2. › § 35 BauGB"
folie([("l35", f"{P35}: privilegiert? nein"), ("sonst", f"{P35}: sonstiges Vorhaben, Abs. 2"),
       ("belang", f"{P35}: öffentliche Belange beeinträchtigt, Abs. 3"), ("verw85", f"{P35}: Einzelheiten im Video „Außenbereich“"),
       ("unzul", f"{PB} › unzulässig (−)")], rechts_frei([
    *tafel("l35", "Außenbereich: § 35 BauGB"),
    *neinz("privilegiert (Abs. 1)? nein – kein landwirtschaftlicher Betrieb", 185, "l35", "Bold", 30, x=160),
    blk(110, 245, 1040, 76, GELB, "sonst", [("sonstiges Vorhaben, § 35 Abs. 2 BauGB", "ExtraBold", 34, INK)]),
    z("öffentliche Belange beeinträchtigt (Abs. 3 S. 1):", 110, 355, "belang", "Bold", 32),
    *neinz("Nr. 1: widerspricht dem Flächennutzungsplan", 405, beim("belang", "widerspricht"), "Regular", 32, x=160),
    *neinz("Nr. 5: natürliche Eigenart der Landschaft", 455, beim("belang", "natürliche"), "Regular", 32, x=160),
    zit("Einzelheiten im Video „Außenbereich § 35 BauGB“", 110, 515, "verw85", size=28),
    blk(110, 580, 1040, 76, HELLROT, "unzul", [("bauplanungsrechtlich unzulässig", "ExtraBold", 34, INK)]),
    *requisit([("l35", ("fluent-emoji-high-contrast", "tractor", 110, GELB), "kein Betrieb", HELLROT),
               ("sonst", ("tabler", "car-garage", 110, WEISS), "sonstiges Vorhaben", GELB),
               ("belang", ("fluent-emoji-high-contrast", "deciduous-tree", 100, GRUEN), "öffentliche Belange", GRUEN),
               ("unzul", ("tabler", "ban", 100, HELLROT), "unzulässig", HELLROT)]),
    *zwei([("l35", "ernst"), ("unzul", "ruhig")], [("l35", "sorge"), ("unzul", "muede")]),
]))

# ===========================================================================================================================
# J1 III. 3. Bauordnungsrecht und Ergebnis
# ===========================================================================================================================
PO = "III. 3. Bauordnungsrecht"
folie([("bo", f"{PO}"), ("abst", f"{PO} › Abstandsflächen eingehalten (+)"), ("hilft", f"{PO} › hilft nicht"),
       ("steht", "Ergebnis › § 35 BauGB steht entgegen"), ("erg", "Ergebnis › kein Anspruch, Ablehnung rechtmäßig")], rechts_frei([
    *tafel("bo", "III. 3. Bauordnungsrecht und Ergebnis"),
    *okz("Abstandsflächen eingehalten", 190, "abst", "Bold", 34, x=160),
    zit("Art. 6 BayBO · § 6 BauO NRW 2018 (Fallannahme)", 160, 240, "abst"),
    z("Das hilft aber nicht:", 110, 310, "hilft", "ExtraBold", 34),
    blk(110, 370, 1040, 120, HELLROT, "steht", [("§ 35 BauGB steht entgegen –", "ExtraBold", 34, INK),
                                                ("eine Vorschrift im Prüfprogramm", "ExtraBold", 34, INK)]),
    *neinz("kein Anspruch auf die Baugenehmigung", 535, "erg", "ExtraBold", 34, x=160),
    *okz("Ablehnung rechtmäßig", 590, beim("erg", "Ablehnung"), "ExtraBold", 34, x=160),
    *requisit([("bo", ("tabler", "ruler-measure", 100, WEISS), "Abstände", WEISS),
               ("steht", ("tabler", "ban", 100, HELLROT), "§ 35 steht entgegen", HELLROT),
               ("erg", ("tabler", "file-x", 100, HELLROT), "abgelehnt – zu Recht", HELLROT)]),
    *zwei([("bo", "ruhig"), ("erg", "ernst")], [("bo", "stolz"), ("hilft", "skeptisch"), ("erg", "sorge")]),
]))

# ===========================================================================================================================
# J2 zurück auf der Wiese: Herr Hasenkamp (Blase)
# ===========================================================================================================================
HA3 = 1450
folie([("ha2", "Ergebnis · Herr Hasenkamp auf seiner Wiese")], [
    landschaft("ha2"),
    boden("ha2"),
    hart(ficon("fluent-emoji-high-contrast", "houses", 230, HORIZONT + 4, 210, "ha2", fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "building-church", 380, HORIZONT + 4, 90, "ha2", fuell=WEISS, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 1700, HORIZONT + 6, 120, "ha2", fuell=GRUEN, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 470, HORIZONT + 6, 90, "ha2", fuell=GRUEN, anim="cut")),
    hart(pl("Wiese vor dem Dorf", 70, 30, "ha2", fill=GRUEN, size=38)),
    hart(garage("ha2", GX0, GU, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "sheaf-of-rice", GX0 + 190, GU - 20, 110, "ha2", fuell=GELB, anim="cut")),
    hart(pl("Außenbereich: keine Garage", GX0 + 190, 545, "ha2", fill=HELLROT, size=32, anker="m")),
    *redet("HA_redet2", HA3, BODEN_Y, FHA, "ha2", "sch"),
    hart(ns(NAME["HA"], HA3, BODEN_Y, "ha2", NFARBE["HA"])),
    blase("sprech", 820, 200, "ha2", 1000, 290, inhalt=["Dann hilft mir der beste Brandschutz", "nichts, wenn der Ort nicht passt."],
          textsize=34, figur=("HA_redet2", HA3, BODEN_Y, FHA), bis="sch"),
])

# ===========================================================================================================================
# K Prüfschema: Anspruch auf Baugenehmigung (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s0", 2, "Anspruchsgrundlage: Landesbauordnung (z. B. Art. 68 BayBO, § 74 BauO NRW 2018)"),
          ("s1", 0, "I. Genehmigungsbedürftigkeit: keine Verfahrensfreiheit, keine Freistellung"),
          ("s2", 0, "II. ordnungsgemäßer Bauantrag"),
          ("s3", 0, "III. Genehmigungsfähigkeit"),
          ("s3a", 1, "1. Verfahrensart und Prüfprogramm (Art. 59 BayBO, § 64 BauO NRW 2018)"),
          ("s3b", 1, "2. Bauplanungsrecht, §§ 29–38 BauGB (Weiche §§ 30, 34, 35)"),
          ("s3c", 1, "3. Bauordnungsrecht, soweit geprüft (z. B. Abstandsflächen)"),
          ("s3d", 1, "4. andere öffentlich-rechtliche Vorschriften im Prüfprogramm"),
          ("s4", 0, "IV. Ergebnis: Anspruch (+) oder (−)")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Anspruch auf Baugenehmigung"), 110, 90, "sch", 46)]
y = 190
for c, ebene, text in REIHEN:
    x = (130, 200, 130)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular", "Bold")[ebene], (40, 36, 36)[ebene], rechts=1800,
                     farbe=(INK, INK, TEXT)[ebene]))
    y += {0: 84, 1: 70, 2: 84}[ebene]
assert y <= 960, y
folie([("sch", "Prüfschema"), ("s0", "Prüfschema › Anspruchsgrundlage"), ("s1", "Prüfschema › I. Genehmigungsbedürftigkeit"),
       ("s2", "Prüfschema › II. Bauantrag"), ("s3", "Prüfschema › III. Genehmigungsfähigkeit"),
       ("s3a", "Prüfschema › III. 1. Verfahrensart"), ("s3b", "Prüfschema › III. 2. Bauplanungsrecht"),
       ("s3c", "Prüfschema › III. 3. Bauordnungsrecht"), ("s3d", "Prüfschema › III. 4. andere Vorschriften"),
       ("s4", "Prüfschema › IV. Ergebnis")], els_sch)

# ===========================================================================================================================
# L Klausurtipp (Lexi): erst die Verfahrensart, dann das Prüfprogramm
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: zuerst die Verfahrensart", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Verfahrensart bestimmen", 200, 200, "tipp", "Bold", 34),
         blk(130, 300, 1020, 90, GELB, "k1", [("daraus: Prüfprogramm – was prüft die Behörde?", "ExtraBold", 34, INK)]),
         blk(130, 420, 1020, 90, GRUEN, "k2", [("Bauplanungsrecht: in jedem Baugenehmigungsverfahren", "ExtraBold", 32, INK)]),
         blk(130, 540, 1020, 90, BLAU, "k3", [("Klage: Verpflichtungsklage, § 42 Abs. 1 VwGO", "ExtraBold", 34, INK)]),
         zit("Aufbau: Video „Zulässigkeit und Begründetheit“", 130, 650, beim("k3", "Aufbau"), size=28),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · zuerst die Verfahrensart"), ("k1", "Klausurtipp › Prüfprogramm"),
       ("k2", "Klausurtipp › Bauplanungsrecht immer"), ("k3", "Klausurtipp › Verpflichtungsklage")], els_k)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Das ", 0), ("Bauplanungsrecht", "a"), (" fragt, ob an", 0)],
                 [("diesem Ort gebaut werden darf,", 0)]], 750, 270, 40, "merke", {"a": beim("merke", "Bauplanungsrecht")}),
    *markertext([[("das ", 0), ("Bauordnungsrecht", "b"), (" vor allem,", 0)],
                 [("wie sicher gebaut wird.", 0)]], 750, 400, 40, "m2", {"b": beim("m2", "Bauordnungsrecht")}),
    *markertext([[("Die Baugenehmigung gibt es nur, wenn", 0)],
                 [("keine ", 0), ("zu prüfende Vorschrift", "c"), (" entgegensteht.", 0)]], 750, 540, 40, "m3",
                {"c": beim("m3", "prüfende")}),
    *markertext([[("Der ", 0), ("falsche Ort", "d"), (" genügt schon", 0)],
                 [("für die Ablehnung.", 0)]], 750, 690, 40, "m4", {"d": beim("m4", "falsche")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
