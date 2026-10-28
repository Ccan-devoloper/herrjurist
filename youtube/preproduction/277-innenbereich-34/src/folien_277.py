"""Folge 277 · § 34 BauGB: Wann fügt sich ein Neubau ein? Innenbereich erklärt – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Einfamilienhausstraße am Stadtrand ohne Bebauungsplan; Herr Kronberg (Investor) will statt eines alten Hauses
einen Wohnblock mit 6 Geschossen und 24 Wohnungen bauen; Frau Morgenstern wohnt nebenan. Der Gemeinderat verweigert die
Zustimmung nach § 34 Abs. 3b, § 36a BauGB.
Szenen laut ../SZENENPLAN.md: A Straße (Fall), B Sachverhalt, C 1. Anwendbarkeit (§ 30, § 34/§ 35, Ortsteil,
Bebauungszusammenhang), D 2. § 34 Abs. 1 (Wortlautkarte), E nähere Umgebung und Rahmen (Straßenansicht), F Art: § 34 Abs. 2
(Wortlautkarte), G Maß: Rahmenüberschreitung, Spannungen (Geschossdiagramm), H Bauweise, Grundstücksfläche, Erschließung,
I 3. Rücksichtnahme, J 4. § 34 Abs. 3b (Wortlautkarte), K Zustimmung § 36a (Wortlautkarte), L Ergebnis (zurück in der
Straße), M Klausurtipp (Lexi), N Schema, O Merksatz (Lexi).
Handlungsgeräusche: Bagger, als der Bagger zum Abriss erscheint; Papier, als der Bauantrag erscheint
(../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 274 (dort aus 200;
gemeinsame Dateien unverändert); neu: strasse(), haus(), geschosse(), ansicht().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BauGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_277/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_277/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180/200) -------------------------------------
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
NAME = {"KR": "Herr Kronberg", "MO": "Frau Morgenstern"}
NFARBE = {"KR": BLAU, "MO": GRUEN}


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


def zwei(folge_l, folge_r, links="KR", rechts="MO"):
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



# --- eigene Szenenbausteine Folge 277 ----------------------------------------------------------------------------------------
HAUSFARBEN = [(246, 232, 170, 255), (242, 214, 196, 255), (214, 232, 250, 255), (226, 240, 214, 255)]
ALTGRAU = (214, 214, 210, 255)
BLOCKF = (253, 226, 160, 255)
NEUF = (205, 232, 190, 255)
FHA = 440                                      # Figurenhöhe in der Fallszene
H1X, BLX, MOHX, BAUMX, KRX, MOX, H4X = 175, 480, 800, 975, 1185, 1475, 1720   # Fallszene von links nach rechts
GH = 34                                        # Geschosshöhe in den Diagrammen


def ti(*a, **k):
    """Icon als Teil einer Tafelgrafik – darf links in der Tafel stehen (nicht unter rechts_frei)."""
    e = ficon(*a, **k)
    e.name = "tafelgrafik:" + e.name
    return e


def _strich(dr, p0, p1, s, w=4, lang=14, luecke=10):
    """gestrichelte Linie (Skalierung s)."""
    (x0, y0), (x1, y1) = p0, p1
    d = math.hypot(x1 - x0, y1 - y0); n = max(1, int(d / (lang + luecke)))
    for i in range(n + 1):
        a = i * (lang + luecke) / d; b = min(1.0, (i * (lang + luecke) + lang) / d)
        if a >= 1:
            break
        dr.line(((x0 + (x1 - x0) * a) * s, (y0 + (y1 - y0) * a) * s, (x0 + (x1 - x0) * b) * s, (y0 + (y1 - y0) * b) * s),
                fill=INK, width=w * s)


def bau(cx, unten, gesch, breite, fill, cue, dach=True, gestrichelt=False, anim="pop", bis=None, d=0.0, gh=None):
    """Gebäude als Geschossdiagramm (Tafelgrafik): gesch Geschosse à GH px, Fenster je Geschoss, Satteldach oder Flachdach;
    gestrichelt = nur gedachter Umriss (Vorbildwirkung)."""
    GH = gh or globals()["GH"]
    dachh = int(breite * 0.34) if dach else 10
    w, h = breite + 8, gesch * GH + dachh + 8

    def zz(dr, s):
        x0, x1, yb, yt = 4, breite + 4, h - 4, h - 4 - gesch * GH
        if gestrichelt:
            for p, q in [((x0, yb), (x0, yt)), ((x1, yb), (x1, yt)), ((x0, yt), (x1, yt))]:
                _strich(dr, p, q, s, w=(4 if GH < 50 else 6))
            return
        dr.rectangle((x0 * s, yt * s, x1 * s, yb * s), fill=fill, outline=INK, width=(4 if GH < 50 else 7) * s)
        if dach:
            dr.polygon([(x0 * s - 6 * s, yt * s), ((x0 + x1) / 2 * s, (yt - dachh + 6) * s), (x1 * s + 6 * s, yt * s)],
                       fill=(240, 122, 106, 255), outline=INK)
            dr.line([(x0 * s - 6 * s, yt * s), ((x0 + x1) / 2 * s, (yt - dachh + 6) * s), (x1 * s + 6 * s, yt * s)], fill=INK,
                    width=4 * s)
        else:
            dr.rectangle((x0 * s - 4 * s, (yt - (8 if GH < 50 else 12)) * s, x1 * s + 4 * s, yt * s), fill=INK)
        nf = max(1, int(breite / 40))
        for g in range(gesch):
            fg = 16 if GH < 50 else 28
            y0 = yb - (g + 1) * GH + (GH - fg) / 2
            for k in range(nf):
                fx = x0 + (breite / nf) * (k + 0.5) - fg / 2
                dr.rectangle((fx * s, y0 * s, (fx + fg) * s, (y0 + fg) * s), fill=(214, 232, 250, 255), outline=INK,
                             width=(3 if GH < 50 else 4) * s)

    im = _flaeche(w + 12, h + 4, lambda dr, s: zz(dr, s))
    return El(im, cx - (w + 12) / 2, unten - (h + 4), cue, anim, d, bis, name=f"tafelgrafik:bau{gesch}")


def gestrichelt_linie(x0, y, x1, cue, bis=None, d=0.0):
    im = _flaeche(int(x1 - x0) + 8, 12, lambda dr, s: _strich(dr, (4, 6), (x1 - x0 + 4, 6), s, w=4))
    return El(im, x0 - 4, y - 6, cue, "fade", d, bis, name="tafelgrafik:linie")


def strasse(c, altes_haus=True):
    """Grundbild der Fallszene: Boden, Einfamilienhäuser mit Gärten (Tabler home-2, trees, fence)."""
    els = [boden(c),
           hart(ficon("tabler", "home-2", H1X, BODEN_Y, 220, c, fuell=HAUSFARBEN[0], anim="cut")),
           hart(ficon("tabler", "fence", 330, BODEN_Y, 80, c, fuell=WEISS, anim="cut")),
           hart(ficon("tabler", "fence", 645, BODEN_Y, 80, c, fuell=WEISS, anim="cut")),
           hart(ficon("tabler", "home-2", MOHX, BODEN_Y, 220, c, fuell=HAUSFARBEN[1], anim="cut")),
           hart(ficon("tabler", "trees", BAUMX, BODEN_Y, 150, c, fuell=GRUEN, anim="cut")),
           hart(ficon("tabler", "home-2", H4X, BODEN_Y, 220, c, fuell=HAUSFARBEN[2], anim="cut"))]
    return els


# ===========================================================================================================================
# A Fall: die Einfamilienhausstraße – Grundstückskauf, Abriss, Wohnblock, zwei Stimmen, Bauantrag, Fragen
# ===========================================================================================================================
folie([(NULL, "Fall · Eine Straße mit Einfamilienhäusern"), ("ohnebp", "Fall · Kein Bebauungsplan"),
       ("kauf", "Fall · Herr Kronberg kauft ein Grundstück"), ("block", "Fall · Ein Wohnblock mit 6 Geschossen"),
       ("kr1", "Fall · Herr Kronberg: Wohnungen für 24 Familien"), ("nebenan", "Fall · Frau Morgenstern wohnt nebenan"),
       ("mo1", "Fall · Passt das in diese Straße?"), ("antrag", "Fall · Der Bauantrag"),
       ("frage", "Fall · Fügt sich der Wohnblock ein?")], [
    *strasse(NULL),
    hart(pl("Einfamilienhäuser mit Gärten · 1 bis 2 Geschosse", 70, 30, NULL, fill=BLAU, size=34)),
    pl("kein Bebauungsplan", 70, 105, beim("ohnebp", "Bebauungsplan"), fill=PINK, size=32),
    hart(ficon("tabler", "home-2", BLX, BODEN_Y, 220, NULL, fuell=ALTGRAU, anim="cut", bis="block")),
    pl("gekauft: Herr Kronberg", BLX, 610, beim("kauf", "gekauft"), fill=BLAU, size=28, anker="m", bis="block"),
    szene(ficon("tabler", "bulldozer", BLX + 40, BODEN_Y + 2, 190, beim("kauf", "abreißen"), fuell=GELB, bis=beim("block", "Wohnblock")),
          "277bagger*", 0.8, 0.0),
    bau(BLX, BODEN_Y, 6, 230, BLOCKF, beim("block", "Wohnblock"), dach=False, gh=60),
    pl("6 Geschosse · 24 Wohnungen", BLX, 455, beim("block", "sechs"), fill=GELB, size=30, anker="m"),
    *fig("KR", KRX, BODEN_Y, FHA, [(beim("kauf", "Herr"), "ruhig"), ("block", "froh")], erst="pop", bis="kr1"),
    ns(NAME["KR"], KRX, BODEN_Y, beim("kauf", "Herr"), NFARBE["KR"], d=0.1),
    *redet("KR_redet", KRX, BODEN_Y, FHA, "kr1", "nebenan"),
    blase("sprech", 900, 210, "kr1", 1130, 300, inhalt=["Die Stadt braucht Wohnungen. Hier können", "24 Familien ein Zuhause finden."],
          textsize=32, bis="nebenan", figur=("KR_redet", KRX, BODEN_Y, FHA)),
    *fig("KR", KRX, BODEN_Y, FHA, [("nebenan", "ruhig"), ("mo1", "denkt"), ("antrag", "ruhig"), ("frage", "denkt")], erst="cut"),
    *fig("MO", MOX, BODEN_Y, FHA, [(beim("nebenan", "Frau"), "ruhig")], erst="pop", bis="mo1"),
    ns(NAME["MO"], MOX, BODEN_Y, beim("nebenan", "Frau"), NFARBE["MO"], d=0.1),
    pl("Haus Morgenstern", MOHX, 610, beim("nebenan", "nebenan"), fill=GRUEN, size=28, anker="m"),
    *redet("MO_redet", MOX, BODEN_Y, FHA, "mo1", "antrag"),
    blase("sprech", 920, 250, "mo1", 1240, 290, inhalt=["Gegen neue Nachbarn habe ich nichts. Aber", "6 Stockwerke direkt neben unseren Gärten?",
                                                     "Passt das in diese Straße?"],
          textsize=32, bis="antrag", figur=("MO_redet", MOX, BODEN_Y, FHA)),
    ring(BLX, 712, 170, 200, beim("mo1", "Stockwerke"), farbe=ORANGE, breite=7, bis="antrag"),
    *fig("MO", MOX, BODEN_Y, FHA, [("antrag", "ernst"), ("frage2", "denkt")], erst="cut"),
    szene(ficon("tabler", "file-certificate", KRX, 440, 96, beim("antrag", "beantragt"), fuell=GELB), "277papier*", 0.8, -0.2),
    pl("Bauantrag", KRX, 300, beim("antrag", "beantragt"), fill=GELB, size=28, anker="m"),
    pl("Fügt sich der Wohnblock in die Straße ein?", 820, 120, "frage", fill=WEISS, size=32),
    pl("… und wenn nicht: Kann die Gemeinde den Weg frei machen?", 820, 195, "frage2", fill=GELB, size=30),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_277(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_277("sv", [
    "In einer Straße am Stadtrand stehen nur Einfamilienhäuser mit Gärten, ein- oder zweigeschossig und mit Abstand zu den "
    "Grenzen; Läden oder Betriebe gibt es nicht. Einen Bebauungsplan gibt es nicht.",
    "Herr Kronberg kauft dort ein Grundstück. Er will das alte Haus abreißen und einen Wohnblock mit 6 Geschossen und "
    "24 Wohnungen bauen. Der Block hält Abstand zu den Grenzen und bleibt in der Bautiefe der Nachbarhäuser; die "
    "Erschließung ist gesichert. Frau Morgenstern wohnt nebenan.",
    "Herr Kronberg beantragt die Baugenehmigung, notfalls mit einer Abweichung nach § 34 Abs. 3b BauGB. 2 Monate nach "
    "dem Ersuchen der Bauaufsichtsbehörde verweigert der Gemeinderat die Zustimmung: 6 Geschosse passen nicht zu seinen "
    "Vorstellungen für die Straße.",
], "Ist der Wohnblock bauplanungsrechtlich zulässig?")

# ===========================================================================================================================
# C 1. Anwendbarkeit: § 30 Abs. 1, Innen- oder Außenbereich, Ortsteil und Bebauungszusammenhang (4 C 5.14 Rn. 11)
# ===========================================================================================================================
PA = "1. Anwendbarkeit"
folie([("anw", f"{PA} · Welche Vorschrift gilt?"), ("b30", f"{PA} › § 30 Abs. 1: kein qualifizierter Bebauungsplan"),
       ("abgr", f"{PA} › § 34 oder § 35 BauGB?"), ("ortst", f"{PA} › Ortsteil"),
       ("zus", f"{PA} › Bebauungszusammenhang"), ("strasse", f"{PA} › § 34 BauGB anwendbar")], rechts_frei([
    *tafel("anw", "1. Welche Vorschrift gilt?"),
    z("Qualifizierter Bebauungsplan (§ 30 Abs. 1 BauGB)?", 160, 180, "b30", "Bold", 33),
    bis_(nein(115, 200, beim("b30", "fehlt"), gr=22), None),
    z("fehlt", 1000, 180, beim("b30", "fehlt"), "ExtraBold", 33, farbe=DROT),
    blk(110, 245, 1040, 76, GELB, "abgr", [("§ 34 Innenbereich oder § 35 Außenbereich?", "ExtraBold", 34, INK)]),
    z("Ortsteil:", 110, 350, "ortst", "ExtraBold", 33),
    z("Bebauungskomplex mit gewissem Gewicht,", 290, 350, beim("ortst", "Bebauungskomplex"), "Regular", 32),
    z("Ausdruck einer organischen Siedlungsstruktur", 290, 398, beim("ortst", "organischen"), "Regular", 32),
    z("im Zusammenhang bebaut:", 110, 468, "zus", "ExtraBold", 33),
    z("trotz Baulücken Eindruck der Geschlossenheit", 110, 516, beim("zus", "Baulücken"), "Regular", 32),
    z("und Zusammengehörigkeit", 110, 564, beim("zus", "Zusammengehörigkeit"), "Regular", 32),
    zit("BVerwG, Urt. v. 30.6.2015 – 4 C 5.14, Rn. 11 (mit BVerwGE 31, 20 <21 f.>)", 110, 616, beim("zus", "Zusammengehörigkeit")),
    *okz("Die Straße erfüllt beides, das Grundstück liegt mittendrin.", 680, "strasse", "Bold", 32, x=160),
    blk(110, 750, 1040, 76, GRUEN, beim("strasse", "Paragraf"), [("§ 34 BauGB ist anwendbar.", "ExtraBold", 34, INK)]),
    *requisit([("anw", ("tabler", "book", 100, WEISS), "BauGB", WEISS),
               ("abgr", ("tabler", "map-2", 100, BLAU), "Innen oder außen?", BLAU),
               ("ortst", ("tabler", "buildings", 100, GELB), "Ortsteil", GELB),
               ("zus", ("tabler", "home-2", 100, HAUSFARBEN[1]), "Zusammenhang", WEISS),
               ("strasse", ("tabler", "map-pin", 100, GRUEN), "Innenbereich", GRUEN)]),
    *allein("KR", [("anw", "denkt"), ("ortst", "ruhig"), ("strasse", "froh")]),
]))

# ===========================================================================================================================
# D 2. Einfügen: § 34 Abs. 1 S. 1 BauGB (Wortlaut), die vier Merkmale
# ===========================================================================================================================
PE = "2. Einfügen"
W34 = ("„(1) Innerhalb der im Zusammenhang bebauten Ortsteile ist ein Vorhaben zulässig, wenn es sich nach Art und Maß der "
       "baulichen Nutzung, der Bauweise und der Grundstücksfläche, die überbaut werden soll, in die Eigenart der näheren "
       "Umgebung einfügt und die Erschließung gesichert ist. …“")
w34, w34_y = wortlaut(80, 165, 1100, W34, "§ 34 Abs. 1 S. 1 BauGB", "p34", marken=[
    ("Art", beim("w34", "Art")), ("Maß", beim("w34", "Maß")), ("Bauweise", beim("w34", "Bauweise")),
    ("Grundstücksfläche,", beim("w34", "Grundstücksfläche")), ("näheren", beim("w34", "näheren")),
    ("einfügt", beim("w34", "einfügt")), ("Erschließung gesichert", beim("w34b", "Erschließung"))], size=31)
MERKMALE = [("Art", "Art"), ("Maß", "Maß"), ("Bauweise", "Bauweise"), ("Grundstücksfläche", "Grundstücksfläche")]
KX = [(110, 200), (320, 200), (530, 290), (830, 320)]   # Merkmalskacheln (x, Breite)
kach = []
for (bx, bw), (txt, wort) in zip(KX, MERKMALE):
    kach.append(blk(bx, w34_y + 40, bw, 70, GELB, beim("w34", wort), [(txt, "ExtraBold", 30, INK)]))
folie([("p34", f"{PE} · § 34 Abs. 1 BauGB"), ("w34", f"{PE} › Art, Maß, Bauweise, Grundstücksfläche"),
       ("w34b", f"{PE} › Erschließung gesichert")], rechts_frei([
    *tafel("p34", "2. Das Einfügen: § 34 Abs. 1 BauGB"),
    *w34, *kach,
    blk(110, w34_y + 135, 1040, 70, WEISS, beim("w34", "näheren"), [("Maßstab: die Eigenart der näheren Umgebung", "ExtraBold", 32, INK)]),
    *requisit([("p34", ("tabler", "book", 100, WEISS), "§ 34 BauGB", WEISS),
               ("w34b", ("tabler", "road", 100, HELLGRAU), "Erschließung", HELLGRAU)]),
    *zwei([("p34", "ruhig"), ("w34b", "denkt")], [("p34", "ruhig"), ("w34", "denkt")]),
]))
assert w34_y + 215 <= 890, w34_y

# ===========================================================================================================================
# E nähere Umgebung und Rahmen (4 C 7.15 Rn. 9, 10, 13, 17; BVerwGE 55, 369)
# ===========================================================================================================================
def ansicht(c, y_unten, x0=150):
    """Straßenansicht als Tafelgrafik: Einfamilienhäuser (1–2 Geschosse) und das Baugrundstück (gestrichelt)."""
    els = [hart(El(_flaeche(1000, 8, lambda dr, s: dr.rectangle((0, 0, 1000 * s, 8 * s), fill=INK)), 130, y_unten, c,
                   "cut", 0.0, None, name="tafelgrafik:boden"))]
    for i, g in enumerate([1, 2, 2, None, 2, 1, 2]):
        cx = x0 + 60 + i * 140
        if g is None:
            els.append(hart(bau(cx, y_unten, 2, 100, WEISS, c, gestrichelt=True, anim="cut")))
        else:
            els.append(hart(bau(cx, y_unten, g, 100, HAUSFARBEN[i % 4], c, anim="cut")))
    return els


PU_ = "2. Nähere Umgebung"
GX = 150 + 60 + 3 * 140                       # Baugrundstück in der Straßenansicht
folie([("naeh", f"{PU_} › so weit sich das Vorhaben auswirkt"), ("gesond", f"{PU_} › je Merkmal gesondert"),
       ("rahmen", f"{PU_} › Rahmen: was tatsächlich vorhanden ist"), ("inn", f"{PU_} › im Rahmen: fügt sich in der Regel ein")],
      rechts_frei([
    *tafel("naeh", "Die nähere Umgebung und der Rahmen"),
    z("reicht so weit, wie sich das Vorhaben auswirken kann", 110, 175, "naeh", "Bold", 32),
    z("und wie die Umgebung das Grundstück prägt", 110, 221, beim("naeh", "prägt"), "Bold", 32),
    zit("BVerwG, Urt. v. 8.12.2016 – 4 C 7.15, Rn. 9 (mit BVerwGE 55, 369 <380>)", 110, 268, beim("naeh", "prägt")),
    *ansicht("naeh", 520),
    pl("Baugrundstück", GX, 335, "naeh", fill=WEISS, size=26, anker="m"),
    ring(GX, 450, 330, 105, beim("naeh", "prägt"), farbe=ORANGE, breite=6),
    z("für jedes Merkmal gesondert bestimmt", 110, 575, "gesond", "Bold", 32),
    blk(110, 640, 1040, 76, LILA, "rahmen", [("Rahmen: was dort tatsächlich vorhanden ist", "ExtraBold", 33, INK)]),
    zit("4 C 7.15, Rn. 10, 13", 110, 726, "rahmen"),
    *okz("Im Rahmen: fügt sich in der Regel ein.", 775, "inn", "Bold", 32, x=160),
    zit("4 C 7.15, Rn. 17 (mit BVerwGE 55, 369 <386>)", 160, 823, "inn"),
    *requisit([("naeh", ("tabler", "zoom-in", 100, WEISS), "nähere Umgebung", WEISS),
               ("rahmen", ("tabler", "ruler-measure", 110, LILA), "Rahmen", LILA)]),
    *allein("MO", [("naeh", "ruhig"), ("rahmen", "denkt"), ("inn", "ruhig")]),
]))

# ===========================================================================================================================
# F Art: § 34 Abs. 2 BauGB (Wortlaut), faktisches reines Wohngebiet (§ 3 BauNVO)
# ===========================================================================================================================
PR2 = "2. a) Art der Nutzung"
W2 = ("„(2) Entspricht die Eigenart der näheren Umgebung einem der Baugebiete, die in der auf Grund des § 9a erlassenen "
      "Verordnung bezeichnet sind, beurteilt sich die Zulässigkeit des Vorhabens nach seiner Art allein danach, ob es nach "
      "der Verordnung in dem Baugebiet allgemein zulässig wäre; …“")
w2, w2_y = wortlaut(80, 165, 1100, W2, "§ 34 Abs. 2 Hs. 1 BauGB", "p2", marken=[
    ("Baugebiete,", beim("w2", "Baugebiet")), ("nach seiner Art allein", beim("w2", "Art")),
    ("allgemein zulässig", beim("w2", "allgemein"))], size=31)
folie([("p2", f"{PR2} · § 34 Abs. 2 BauGB"), ("w2", f"{PR2} › faktisches Baugebiet"),
       ("fakt", f"{PR2} › reines Wohngebiet (§ 3 BauNVO)"), ("wohn", f"{PR2} › Wohngebäude allgemein zulässig")], rechts_frei([
    *tafel("p2", "Die Art der Nutzung: § 34 Abs. 2 BauGB"),
    *w2,
    *okz("Die Straße entspricht einem reinen Wohngebiet (§ 3 BauNVO).", w2_y + 30, "fakt", "Bold", 31, x=160),
    *okz("Wohngebäude: allgemein zulässig (§ 3 Abs. 2 Nr. 1 BauNVO)", w2_y + 90, "wohn", "Bold", 31, x=160),
    blk(110, w2_y + 160, 1040, 76, GRUEN, beim("wohn", "Seiner"), [("Art: Der Block fügt sich ein.", "ExtraBold", 34, INK)]),
    zit("Die Baugebiete im Einzelnen: Video „Baugebiete der BauNVO“", 110, w2_y + 250, "v200"),
    *requisit([("p2", ("tabler", "book", 100, WEISS), "BauNVO", WEISS),
               ("fakt", ("tabler", "home-2", 100, HAUSFARBEN[0]), "reines Wohngebiet", HAUSFARBEN[0]),
               ("wohn", ("tabler", "building", 90, BLOCKF), "Wohngebäude", GELB)]),
    *zwei([("p2", "ruhig"), ("wohn", "froh")], [("p2", "ruhig"), ("fakt", "denkt")]),
]))
assert w2_y + 290 <= 890, w2_y

# ===========================================================================================================================
# G Maß: Rahmenüberschreitung, bodenrechtliche Spannungen, Vorbildwirkung (4 C 7.15 Rn. 17, Leitsatz 2)
# ===========================================================================================================================
PM = "2. b) Maß der baulichen Nutzung"
DB = 545                                         # Grundlinie des Geschossdiagramms
DX = [210, 340, 470, 640, 810, 940, 1070]        # Häuser links/rechts, Baugrundstück in der Mitte
folie([("mass", f"{PM} · Anders beim Maß"), ("mfak", f"{PM} › Grundfläche, Geschosszahl, Höhe"),
       ("ref", f"{PM} › kein Vorbild für 6 Geschosse"), ("ueber", f"{PM} › Rahmen gesprengt"),
       ("ausn", f"{PM} › Ausnahme: keine bodenrechtlichen Spannungen"), ("spann", f"{PM} › Vorbildwirkung: Spannungen"),
       ("neinm", f"{PM} › fügt sich nicht ein")], rechts_frei([
    *tafel("mass", "Das Maß der baulichen Nutzung"),
    z("Was man von außen sieht: Grundfläche, Geschosszahl, Höhe", 110, 172, "mfak", "Bold", 31),
    zit("wertende Gesamtbetrachtung · BVerwG 4 C 7.15, Leitsatz 2, Rn. 17", 110, 218, beim("mfak", "Gesamtbetrachtung")),
    hart(El(_flaeche(1000, 8, lambda dr, s: dr.rectangle((0, 0, 1000 * s, 8 * s), fill=INK)), 130, DB, "mass", "cut", 0.0,
            None, name="tafelgrafik:boden")),
    *[hart(bau(x, DB, g, 100, HAUSFARBEN[i % 4], "mass", anim="cut")) for i, (x, g) in
      enumerate(zip(DX[:3] + DX[4:], [2, 1, 2, 2, 1, 2]))],
    gestrichelt_linie(140, DB - 2 * GH - 4, 1120, beim("ref", "zwei")),
    z("gestrichelt: Rahmen der Umgebung, höchstens 2 Geschosse", 140, DB + 14, beim("ref", "zwei"), "Bold", 26, farbe=TEXT),
    bau(DX[3], DB, 6, 150, BLOCKF, beim("ref", "sechs"), dach=False),
    pl("6 Geschosse: kein Vorbild", 160, 270, beim("ref", "sechs"), fill=GELB, size=28),
    bis_(nein(DX[3] + 110, DB - 6 * GH - 10, "ueber", gr=24), None),
    *[bau(x, DB, 6, 100, WEISS, beim("spann", "berufen"), dach=False, gestrichelt=True) for x in (DX[2], DX[4])],
    blk(110, 600, 1040, 112, LILA, "ausn", [("Ausnahme: keine bodenrechtlich beachtlichen", "ExtraBold", 31, INK),
                                          ("Spannungen, auch nicht durch Vorbildwirkung", "ExtraBold", 31, INK)]),
    zit("4 C 7.15, Rn. 17 (mit BVerwGE 55, 369 <386>; 4 C 13.93)", 110, 720, "ausn"),
    z("Nachbarn könnten nachziehen: neues Gesicht der Straße", 110, 765, beim("spann", "berufen"), "Bold", 31),
    *neinz("Nach dem Maß fügt sich der Block nicht ein.", 820, "neinm", "ExtraBold", 32, x=160),
    *requisit([("mass", ("tabler", "ruler-measure", 110, WEISS), "Maß", WEISS),
               ("spann", ("tabler", "buildings", 100, GELB), "Vorbildwirkung", GELB)]),
    *zwei([("mass", "ruhig"), ("ueber", "denkt"), ("neinm", "ernst")], [("mass", "denkt"), ("neinm", "ruhig")]),
]))

# ===========================================================================================================================
# H Bauweise, Grundstücksfläche, Erschließung
# ===========================================================================================================================
PB = "2. c) Bauweise, Grundstücksfläche"
STAND = [("Art", 1, "w"), ("Maß", 0, "w"), ("Bauweise", 1, "bauw"), ("Grundstücksfläche", 1, "bauw")]
folie([("bauw", f"{PB} › kein Problem"), ("ersch", "2. d) Erschließung › gesichert")], rechts_frei([
    *tafel("bauw", "Bauweise, Grundstücksfläche, Erschließung"),
    *okz("Bauweise: Der Block hält Abstand zu den Grenzen.", 185, beim("bauw", "Abstand"), "Bold", 32, x=160),
    *okz("Grundstücksfläche: in der Bautiefe der Nachbarhäuser", 255, beim("bauw", "Bautiefe"), "Bold", 32, x=160),
    *okz("Erschließung über die Straße: gesichert", 325, beim("ersch", "Erschließung"), "Bold", 32, x=160),
    z("Zwischenstand:", 110, 430, "bauw", "ExtraBold", 33),
    *[blk(KX[i][0], 490, KX[i][1], 70, (GRUEN if ok_ else ROT), "bauw" if t_ in ("Art", "Maß") else beim("bauw", t_),
          [(t_, "ExtraBold", 30, INK)]) for i, (t_, ok_, _) in enumerate(STAND)],
    *[(ok if o_ else nein)(KX[i][0] + KX[i][1] - 22, 488, "bauw" if t_ in ("Art", "Maß") else beim("bauw", t_), gr=20)
      for i, (t_, o_, _) in enumerate(STAND)],
    zit("§ 34 Abs. 1 S. 1 BauGB; § 22 Abs. 2 BauNVO (offene Bauweise) als Orientierung", 110, 590, beim("bauw", "Abstand")),
    *requisit([("bauw", ("tabler", "ruler-measure", 110, WEISS), "Abstand, Bautiefe", WEISS),
               ("ersch", ("tabler", "road", 100, HELLGRAU), "Erschließung", HELLGRAU)]),
    *allein("KR", [("bauw", "ruhig"), ("ersch", "froh")]),
]))

# ===========================================================================================================================
# I 3. Rücksichtnahme als Teil des Einfügens (4 C 7.15 Rn. 17; Verweis Folge 274)
# ===========================================================================================================================
PRU = "3. Rücksichtnahme"
folie([("rueck", f"{PRU} · Teil des Einfügens"), ("v274", f"{PRU} › Nachbarschutz: Video „Gebietserhaltungsanspruch“")],
      rechts_frei([
    *tafel("rueck", "3. Die Rücksichtnahme"),
    blk(110, 172, 1040, 70, GELB, beim("rueck", "Teil"), [("Teil des Einfügens", "ExtraBold", 34, INK)]),
    z("Auch ein Vorhaben im Rahmen fügt sich nicht ein,", 110, 270, beim("rueck", "Auch"), "Bold", 32),
    z("wenn es die gebotene Rücksicht auf die Nachbarn", 110, 316, beim("rueck", "gebotene"), "Bold", 32),
    z("fehlen lässt.", 110, 362, beim("rueck", "gebotene"), "Bold", 32),
    zit("BVerwG, Urt. v. 8.12.2016 – 4 C 7.15, Rn. 17 (mit BVerwGE 55, 369 <386>)", 110, 414, beim("rueck", "gebotene")),
    hart(El(_flaeche(700, 8, lambda dr, s: dr.rectangle((0, 0, 700 * s, 8 * s), fill=INK)), 250, 760, beim("rueck", "Nachbarn"),
            "cut", 0.0, None, name="tafelgrafik:boden")),
    bau(400, 760, 2, 130, HAUSFARBEN[1], beim("rueck", "Nachbarn")),
    bau(700, 760, 6, 150, BLOCKF, beim("rueck", "Nachbarn"), dach=False),
    ti("tabler", "sun", 900, 560, 80, beim("rueck", "Nachbarn"), fuell=GELB),
    pl("Nachbarhaus", 400, 780, beim("rueck", "Nachbarn"), fill=WEISS, size=26, anker="m"),
    zit("Wie Nachbarn ihre Rechte durchsetzen: Video „Gebietserhaltungsanspruch“", 110, 840, "v274"),
    *requisit([("rueck", ("tabler", "scale", 100, WEISS), "Rücksichtnahme", WEISS),
               ("v274", ("tabler", "shield", 100, GRUEN), "Nachbarschutz", GRUEN)]),
    *allein("MO", [("rueck", "sorge"), ("v274", "ruhig")]),
]))

# ===========================================================================================================================
# J 4. § 34 Abs. 3b BauGB (Wortlaut; G v. 27.10.2025, BGBl. 2025 I Nr. 257, in Kraft 30.10.2025), unbefristet, § 246e
# ===========================================================================================================================
P3B = "4. § 34 Abs. 3b BauGB"
W3B = ("„(3b) Mit Zustimmung der Gemeinde kann im Einzelfall oder in mehreren vergleichbaren Fällen vom Erfordernis des "
       "Einfügens in die nähere Umgebung abgewichen werden, wenn das Vorhaben der Errichtung eines Wohngebäudes dient und "
       "auch unter Würdigung nachbarlicher Interessen mit den öffentlichen Belangen vereinbar ist.“")
w3b, w3b_y = wortlaut(80, 262, 1100, W3B, "§ 34 Abs. 3b BauGB", "p3b", marken=[
    ("Zustimmung der Gemeinde", beim("w3b", "Zustimmung")), ("vergleichbaren Fällen", beim("w3b", "vergleichbaren")),
    ("abgewichen", beim("w3b", "abgewichen")), ("Wohngebäudes", beim("w3b", "Wohngebäudes")),
    ("Würdigung nachbarlicher", beim("w3bb", "Würdigung"))], size=30)
folie([("p3b", f"{P3B} · neu seit 30.10.2025"), ("w3b", f"{P3B} › Abweichung mit Zustimmung der Gemeinde"),
       ("w3bb", f"{P3B} › Würdigung nachbarlicher Interessen"), ("begr", f"{P3B} › etwa das Maß muss sich nicht einfügen"),
       ("befr", f"{P3B} › unbefristet, anders als § 246e")], rechts_frei([
    *tafel("p3b", "4. Abweichung: § 34 Abs. 3b BauGB"),
    z("neu seit 30.10.2025", 110, 172, beim("p3b", "dreißigsten"), "ExtraBold", 33),
    zit("Art. 1 Nr. 5 c, Art. 2 G v. 27.10.2025, BGBl. 2025 I Nr. 257", 110, 218,
        beim("p3b", "dreißigsten")),
    *w3b,
    z("Begründung: etwa das Maß muss sich nicht mehr einfügen.", 110, w3b_y + 22, "begr", "Bold", 31),
    zit("BT-Drs. 21/781 (neu), S. 23", 110, w3b_y + 68, "begr"),
    *okz("unbefristet – anders als § 246e BauGB (bis 31.12.2030)", w3b_y + 118, "befr", "Bold", 31, x=160),
    *requisit([("p3b", ("tabler", "calendar", 100, GELB), "seit 30.10.2025", GELB),
               ("w3b", ("tabler", "home-2", 100, BLOCKF), "Wohngebäude", GELB),
               ("befr", ("tabler", "hourglass", 100, WEISS), "ohne Frist", WEISS)]),
    *zwei([("p3b", "ruhig"), ("w3b", "zuversicht"), ("befr", "ruhig")], [("p3b", "ruhig"), ("w3bb", "denkt")]),
]))
assert w3b_y + 170 <= 890, w3b_y

# ===========================================================================================================================
# K Zustimmung der Gemeinde: § 36a Abs. 1 S. 2, 4 BauGB (Wortlaut), Gemeinderat verweigert
# ===========================================================================================================================
P36 = "4. Zustimmung, § 36a BauGB"
W36 = ("„Die Gemeinde erteilt die Zustimmung, wenn das Vorhaben mit ihren Vorstellungen von der städtebaulichen Entwicklung "
       "und Ordnung vereinbar ist. … Die Zustimmung der Gemeinde gilt als erteilt, wenn sie nicht binnen drei Monaten nach "
       "Eingang des Ersuchens der Genehmigungsbehörde verweigert wird; …“")
w36, w36_y = wortlaut(80, 165, 1100, W36, "§ 36a Abs. 1 S. 2, 4 BauGB", "zust", marken=[
    ("Vorstellungen", beim("zust", "Vorstellungen")), ("städtebaulichen Entwicklung", beim("zust", "städtebaulichen")),
    ("gilt als erteilt,", beim("drei", "gilt")), ("drei Monaten", beim("drei", "drei"))], size=31)
folie([("zust", f"{P36} › Vorstellungen der Gemeinde"), ("drei", f"{P36} › gilt nach 3 Monaten als erteilt"),
       ("rat", f"{P36} › Gemeinderat verweigert")], rechts_frei([
    *tafel("zust", "Die Zustimmung der Gemeinde"),
    *w36,
    *neinz("Gemeinderat nach 2 Monaten: Zustimmung verweigert", w36_y + 35, beim("rat", "lehnt"), "ExtraBold", 32, x=160),
    z("6 Geschosse passen nicht zu seinen Vorstellungen.", 160, w36_y + 90, beim("rat", "Sechs"), "Bold", 31),
    blk(110, w36_y + 160, 1040, 76, PINK, beim("rat", "Sechs"), [("keine Zustimmung, keine Abweichung", "ExtraBold", 33, INK)]),
    *requisit([("zust", ("tabler", "writing-sign", 100, WEISS), "Zustimmung", WEISS),
               ("drei", ("tabler", "clock", 100, GELB), "3 Monate", GELB),
               ("rat", ("tabler", "file-x", 100, HELLROT), "verweigert", HELLROT)]),
    *allein("KR", [("zust", "ruhig"), ("drei", "denkt"), ("rat", "ernst")]),
]))
assert w36_y + 250 <= 890, w36_y

# ===========================================================================================================================
# L Ergebnis: zurück in der Straße; Herr Kronberg plant neu, Frau Morgenstern (Blasen)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Maß: fügt sich nicht ein, keine Abweichung"), ("erg2", "Ergebnis · Baugenehmigung abzulehnen"),
       ("kr2", "Ergebnis · Herr Kronberg plant neu"), ("mo2", "Ergebnis · Frau Morgenstern")], [
    *strasse("erg"),
    hart(pl("Ergebnis", 70, 30, "erg", fill=PINK, size=38)),
    bau(BLX, BODEN_Y, 6, 230, WEISS, "erg", dach=False, gestrichelt=True, bis=beim("kr2", "zwei"), gh=60),
    pl("geplant: 6 Geschosse", BLX, 455, "erg", fill=WEISS, size=28, anker="m", bis=beim("kr2", "zwei")),
    bis_(nein(95, 145, beim("erg", "Maß"), gr=22), None),
    pl("Maß: fügt sich nicht ein", 125, 115, beim("erg", "Maß"), fill=HELLROT, size=30),
    bis_(nein(95, 215, beim("erg", "Zustimmung"), gr=22), None),
    pl("ohne Zustimmung keine Abweichung", 125, 185, beim("erg", "Zustimmung"), fill=HELLROT, size=30),
    pl("Baugenehmigung: abzulehnen", 125, 255, beim("erg2", "Baugenehmigung"), fill=PINK, size=32),
    ficon("tabler", "home-2", BLX, BODEN_Y, 230, beim("kr2", "zwei"), fuell=NEUF),
    pl("neu geplant: 2 Geschosse", BLX, 610, beim("kr2", "zwei"), fill=GRUEN, size=28, anker="m"),
    *fig("KR", KRX, BODEN_Y, FHA, [("erg", "ernst"), ("erg2", "ruhig")], erst="pop", bis="kr2"),
    ns(NAME["KR"], KRX, BODEN_Y, "erg", NFARBE["KR"], d=0.1),
    *redet("KR_redet2", KRX, BODEN_Y, FHA, "kr2", "mo2"),
    blase("sprech", 700, 210, "kr2", 1100, 300, inhalt=["Dann plane ich neu, mit 2 Geschossen", "wie die Nachbarhäuser."],
          textsize=32, bis="mo2", figur=("KR_redet2", KRX, BODEN_Y, FHA)),
    *fig("KR", KRX, BODEN_Y, FHA, [("mo2", "froh")], erst="cut"),
    *fig("MO", MOX, BODEN_Y, FHA, [("erg", "ruhig"), ("kr2", "froh")], erst="pop", bis="mo2"),
    ns(NAME["MO"], MOX, BODEN_Y, "erg", NFARBE["MO"], d=0.1),
    *redet("MO_redet2", MOX, BODEN_Y, FHA, "mo2", "tipp"),
    blase("sprech", 560, 170, "mo2", 1500, 290, inhalt=["Damit kann ich gut leben."], textsize=34, bis="tipp",
          figur=("MO_redet2", MOX, BODEN_Y, FHA)),
])

# ===========================================================================================================================
# M Klausurtipp (Lexi): Maßstäbe trennen, Spannungen, § 34 Abs. 3b erst danach, kein Anspruch auf Zustimmung
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Maßstäbe trennen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Wer prüft was?", 200, 200, "tipp", "Bold", 34),
         blk(130, 280, 1020, 76, GRUEN, "k1", [("Art im faktischen Baugebiet: § 34 Abs. 2, BauNVO", "ExtraBold", 31, INK)]),
         blk(130, 372, 1020, 76, GELB, "k2", [("Maß, Bauweise, Grundstücksfläche: § 34 Abs. 1", "ExtraBold", 31, INK)]),
         z("Rahmen gesprengt? Bodenrechtliche Spannungen prüfen,", 130, 480, "k3", "Bold", 31),
         z("vor allem die Vorbildwirkung", 130, 526, beim("k3", "Vorbildwirkung"), "Bold", 31),
         blk(130, 600, 1020, 76, BLAU, "k4", [("§ 34 Abs. 3b erst, wenn das Einfügen scheitert", "ExtraBold", 31, INK)]),
         z("Auf die Zustimmung: grundsätzlich kein Anspruch", 130, 700, beim("k4", "Anspruch"), "Bold", 31),
         zit("BT-Drs. 21/781 (neu), S. 24; § 36a Abs. 1, 3 BauGB", 130, 748, beim("k4", "Anspruch")),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Maßstäbe trennen"), ("k1", "Klausurtipp › Art: § 34 Abs. 2"),
       ("k2", "Klausurtipp › Maß, Bauweise, Fläche: § 34 Abs. 1"), ("k3", "Klausurtipp › Spannungen, Vorbildwirkung"),
       ("k4", "Klausurtipp › § 34 Abs. 3b erst danach")], els_k)

# ===========================================================================================================================
# N Schema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Anwendbarkeit: kein qualifizierter Bebauungsplan (§ 30 Abs. 1)"),
          (beim("s1", "im"), 1, "im Zusammenhang bebauter Ortsteil (Abgrenzung zu § 35)"),
          ("s2", 0, "2. Einfügen in die Eigenart der näheren Umgebung (§ 34 Abs. 1)"),
          ("s2a", 1, "a) Art: im faktischen Baugebiet nach § 34 Abs. 2 und BauNVO"),
          ("s2b", 1, "b) Maß, Bauweise, Grundstücksfläche: im Rahmen oder ohne Spannungen"),
          ("s2c", 1, "c) Rücksichtnahme"),
          ("s3", 0, "3. Erschließung gesichert"),
          ("s4", 0, "4. Notfalls Abweichung nach § 34 Abs. 3b: Zustimmung der Gemeinde"),
          ("s5", 0, "5. Ergebnis")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Bauen im Innenbereich, § 34 BauGB"), 110, 90, "sch", 46)]
y = 215
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (38, 34)[ebene], rechts=1820))
    y += {0: 84, 1: 70}[ebene]
assert y <= 960, y
folie([("sch", "Schema · Bauen im Innenbereich"), ("s1", "Schema › 1. Anwendbarkeit"), ("s2", "Schema › 2. Einfügen"),
       ("s2a", "Schema › 2. a) Art"), ("s2b", "Schema › 2. b) Maß, Bauweise, Grundstücksfläche"),
       ("s2c", "Schema › 2. c) Rücksichtnahme"), ("s3", "Schema › 3. Erschließung"), ("s4", "Schema › 4. § 34 Abs. 3b"),
       ("s5", "Schema › 5. Ergebnis")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im Innenbereich ersetzt die ", 0), ("vorhandene Bebauung", "a")], [("den Bebauungsplan.", 0)]],
                750, 280, 40, "merke", {"a": beim("merke", "vorhandene")}),
    *markertext([[("Wer ihren ", 0), ("Rahmen", "b"), (" sprengt, fügt sich nur ein,", 0)],
                 [("wenn keine ", 0), ("bodenrechtlichen Spannungen", "c"), (" entstehen.", 0)]], 750, 445, 40, "m2",
                {"b": beim("m2", "Rahmen"), "c": beim("m2", "bodenrechtlichen")}),
    *markertext([[("Für Wohngebäude öffnet ", 0), ("§ 34 Abs. 3b", "d"), (" einen zweiten Weg,", 0)],
                 [("aber nur mit ", 0), ("Zustimmung der Gemeinde", "e"), (".", 0)]], 750, 620, 40, "m3",
                {"d": beim("m3", "Absatz"), "e": beim("m3", "Zustimmung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
