"""Folge 274 · Gebietserhaltungsanspruch: Flüchtlingsunterkunft im Gewerbegebiet? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Gewerbegebiet mit qualifiziertem Bebauungsplan; Frau Hollenberg (Eigentümerin, Schreinerei) klagt gegen die
Genehmigung der Nutzungsänderung des Bürogebäudes nebenan in eine Gemeinschaftsunterkunft für 300 Geflüchtete (Befreiung nach
§ 246 Abs. 10 BauGB, Herr Kerkhoff von der Bauaufsicht).
Szenen laut ../SZENENPLAN.md: A Gewerbegebiet (Fall), B Sachverhalt, C 1. Klagebefugnis/Gebietserhaltungsanspruch,
D Folgen des Anspruchs (ohne Beeinträchtigung, nur im selben Gebiet), E 2. § 8 BauNVO (Wortlautkarte), F Gebietsverträglichkeit/
Wohnähnlichkeit, G 3. § 246 Abs. 10 BauGB (Wortlautkarte), H Abs. 10 am Fall (BVerwG 4 B 39.17), I Grenzen: Abs. 13a
(Wortlautkarte), Abs. 17, J 4. Rücksichtnahme § 15 Abs. 1 S. 2 BauNVO (Wortlautkarte), K Ergebnis (zurück im Gewerbegebiet),
L Klausurtipp (Lexi), M Schema, N Merksatz (Lexi).
Darstellung: Geflüchtete erscheinen nicht als Figuren; die Unterkunft nur als Gebäude-Symbol (Tabler building).
Handlungsgeräusche: Kreissäge, als die Säge der Schreinerei erscheint; Papier, als die Genehmigung erscheint
(../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/tabelle als eigene Kopie aus Folge 200 (gemeinsame
Dateien unverändert); neu: gewerbegebiet(), ti(), grundstuecke(), zwei_gebiete().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BauGB, BauNVO), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_274/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_274/" in n:
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
NAME = {"HO": "Frau Hollenberg", "KE": "Herr Kerkhoff"}
NFARBE = {"HO": ORANGE, "KE": BLAU}


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


def zwei(folge_l, folge_r, links="HO", rechts="KE"):
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



# --- eigene Szenenbausteine Folge 274 ----------------------------------------------------------------------------------------
HOLZ2 = (233, 196, 150, 255)                 # Werkhalle der Schreinerei
BUEROGRAU = (232, 234, 238, 255)             # leeres Bürogebäude
FABX, HOX, LKWX, BUEX, KEX, LAGX = 270, 580, 820, 1110, 1480, 1745   # Fallszene: Positionen von links nach rechts


def ti(*a, **k):
    """Icon als Teil einer Tafelgrafik (Planausschnitt) – darf links in der Tafel stehen (nicht unter rechts_frei)."""
    e = ficon(*a, **k)
    e.name = "tafelgrafik:" + e.name
    return e


def gewerbegebiet(c, unterkunft=False, pille=True):
    """Grundbild der Fallszene: Boden, Werkhalle der Schreinerei, Bürogebäude/Unterkunft, Nachbarbetrieb (Lager)."""
    els = [boden(c),
           hart(ficon("tabler", "building-factory-2", FABX, BODEN_Y, 360, c, fuell=HOLZ2, anim="cut")),
           hart(ficon("tabler", "building-warehouse", LAGX, BODEN_Y, 210, c, fuell=HELLGRAU, anim="cut"))]
    if pille:
        els.append(hart(pl("Gewerbegebiet · Bebauungsplan", 70, 30, c, fill=BLAU, size=38)))
    if unterkunft:
        els += [hart(ficon("tabler", "building", BUEX, BODEN_Y, 300, c, fuell=HELLGRUEN, anim="cut")),
                hart(pl("Gemeinschaftsunterkunft", BUEX, 520, c, fill=HELLGRUEN, size=30, anker="m")),
                hart(pl("Schreinerei", FABX, 525, c, fill=HOLZ2, size=30, anker="m")),
                hart(ficon("tabler", "truck-delivery", LKWX, BODEN_Y, 200, c, fuell=GELB, anim="cut"))]
    return els


# ===========================================================================================================================
# A Fall: das Gewerbegebiet – Schreinerei, Bürogebäude, Unterkunft, Genehmigung, Sorge, Klage, Frage
# ===========================================================================================================================
BLASE_KE = dict(figur=("KE_redet", KEX, BODEN_Y, FHA))
folie([(NULL, "Fall · Das Gewerbegebiet am Stadtrand"), ("werk", "Fall · Die Schreinerei von Frau Hollenberg"),
       ("buero", "Fall · Das leere Bürogebäude nebenan"), ("heim", "Fall · Unterkunft für 300 Geflüchtete"),
       ("genehm", "Fall · Die Genehmigung"), ("ke1", "Fall · Befreiung wegen dringendem Bedarf"),
       ("ho1", "Fall · Frau Hollenberg fürchtet Auflagen"), ("klage", "Fall · Die Klage"),
       ("frage", "Fall · Kann der Betrieb die Unterkunft verhindern?")], [
    *gewerbegebiet(NULL),
    pl("Schreinerei", FABX, 525, beim("werk", "Schreinerei"), fill=HOLZ2, size=30, anker="m"),
    *fig("HO", HOX, BODEN_Y, FHA, [(beim("werk", "Frau"), "ruhig_r"), ("heim", "sorge_r"), ("genehm", "denkt_r")],
         erst="pop", bis="ho1"),
    ns(NAME["HO"], HOX, BODEN_Y, beim("werk", "Frau"), NFARBE["HO"], d=0.1),
    ficon("tabler", "clock", 140, 380, 80, beim("saege", "sechs"), fuell=WEISS),
    pl("ab 6 Uhr", 140, 395, beim("saege", "sechs"), fill=WEISS, size=28, anker="m"),
    szene(ficon("fluent-emoji-high-contrast", "carpentry-saw", 385, 465, 120, beim("saege", "Sägen"), fuell=GELB),
          "274saege*", 0.7, 0.0),
    ficon("tabler", "truck-delivery", LKWX, BODEN_Y, 200, beim("saege", "Lieferwagen"), fuell=GELB),
    ficon("tabler", "building", BUEX, BODEN_Y, 300, "buero", fuell=BUEROGRAU, bis="heim"),
    pl("leeres Bürogebäude", BUEX, 525, beim("buero", "leeres"), fill=WEISS, size=30, anker="m", bis="heim"),
    hart(ficon("tabler", "building", BUEX, BODEN_Y, 300, beim("heim", "Gemeinschaftsunterkunft"), fuell=HELLGRUEN, anim="cut")),
    pl("Gemeinschaftsunterkunft", BUEX, 525, beim("heim", "Gemeinschaftsunterkunft"), fill=HELLGRUEN, size=30, anker="m"),
    pl("300 Plätze", BUEX, 460, beim("heim", "dreihundert"), fill=WEISS, size=30, anker="m"),
    pl("vermietet an die Stadt", BUEX, 395, beim("heim", "Stadt"), fill=WEISS, size=28, anker="m", bis="ke1"),
    *fig("KE", KEX, BODEN_Y, FHA, [(beim("genehm", "Herr"), "ruhig")], erst="pop", bis="ke1"),
    ns(NAME["KE"], KEX, BODEN_Y, beim("genehm", "Herr"), NFARBE["KE"], d=0.1),
    szene(ficon("tabler", "file-certificate", KEX, 330, 110, beim("genehm", "genehmigt"), fuell=GELB, bis="ke1"),
          "274papier*", 0.8, -0.3),
    pl("Genehmigung: neue Nutzung", KEX, 190, beim("genehm", "genehmigt"), fill=GELB, size=28, anker="m", bis="ke1"),
    *redet("KE_redet", KEX, BODEN_Y, FHA, "ke1", "ho1"),
    blase("sprech", 1060, 270, "ke1", 1060, 235, inhalt=["Die Stadt braucht die Plätze dringend, und", "kein anderes Gebäude wird rechtzeitig frei.",
                                                       "Deshalb erteilen wir eine Befreiung."],
          textsize=32, bis="ho1", **BLASE_KE),
    *fig("KE", KEX, BODEN_Y, FHA, [("ho1", "ernst"), ("klage", "ruhig"), ("frage", "denkt")], erst="cut"),
    *redet("HO_redet_r", HOX, BODEN_Y, FHA, "ho1", "klage"),
    blase("sprech", 1060, 270, "ho1", 800, 235, inhalt=["Gegen die Menschen habe ich nichts. Aber", "wenn nebenan Schlafräume sind, bekomme ich",
                                                      "bald Auflagen für meine Maschinen."],
          textsize=32, figur=("HO_redet_r", HOX, BODEN_Y, FHA), bis="klage"),
    ficon("tabler", "bed", BUEX, 800, 110, beim("ho1", "Schlafräume"), fuell=WEISS),
    ring(385, 410, 95, 80, beim("ho1", "Maschinen"), farbe=ORANGE, breite=7, bis="klage"),
    *fig("HO", HOX, BODEN_Y, FHA, [("klage", "ernst_r")], erst="cut"),
    pl("Klage gegen die Genehmigung", 680, 120, beim("klage", "klagt"), fill=PINK, size=34),
    pl("Kann der Betrieb die Unterkunft verhindern?", 680, 195, "frage", fill=WEISS, size=32),
    pl("… auch ohne Nachweis, dass er gestört wird?", 680, 265, "frage2", fill=GELB, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_274(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_274("sv", [
    "Ein qualifizierter Bebauungsplan setzt am Stadtrand ein Gewerbegebiet fest; Ausnahmen nach § 8 Abs. 3 BauNVO schließt "
    "er nicht aus. Frau Hollenberg gehört dort ein Grundstück, auf dem sie eine Schreinerei betreibt (Sägen ab 6 Uhr, "
    "Lieferverkehr).",
    "Der Eigentümer des leeren Bürogebäudes nebenan will es zu einer Gemeinschaftsunterkunft für 300 Geflüchtete umbauen "
    "und an die Stadt vermieten; die Bewohner sollen dort mehrere Monate leben. Im Oktober 2026 genehmigt die "
    "Bauaufsichtsbehörde die Nutzungsänderung mit einer Befreiung nach § 246 Abs. 10 BauGB. Die Stadt hat dargelegt, "
    "dass sie die Plätze dringend braucht und kein anderes Gebäude rechtzeitig frei wird; ihr Einvernehmen liegt vor.",
    "Ein Lärmgutachten ergibt: An der Unterkunft hält die Schreinerei die Werte für ein Gewerbegebiet ein. Frau Hollenberg "
    "klagt gegen die Genehmigung.",
], "Hat die Klage von Frau Hollenberg Erfolg?")

# ===========================================================================================================================
# C 1. Klagebefugnis: Gebietserhaltungsanspruch, Schicksalsgemeinschaft (BVerwGE 94, 151)
# ===========================================================================================================================
PK = "1. Klagebefugnis"


def grundstuecke(c, y0, x0=130, links=None):
    """Drei Grundstücke im Gewerbegebiet als Planausschnitt (Schreinerei, Unterkunft, Lager)."""
    els = [hart(El(_flaeche(1000, 230, lambda dr, s: dr.rounded_rectangle((3 * s, 3 * s, 997 * s, 227 * s), 14 * s,
                                                                             fill=(236, 243, 252, 255), outline=INK, width=4 * s)),
                   x0, y0, c, "fade", 0.0, None, name="plan:GE"))]
    els.append(hart(z("GE · Gewerbegebiet", x0 + 20, y0 + 10, c, "Bold", 28, farbe=TEXT)))
    for i, (ic, fu, txt) in enumerate([("building-factory-2", HOLZ2, "Schreinerei"), ("building", HELLGRUEN, "Bürogebäude"),
                                      ("building-warehouse", HELLGRAU, "Lager")]):
        cx = x0 + 170 + i * 330
        els.append(hart(ti("tabler", ic, cx, y0 + 175, 110, c, fuell=fu, anim="cut")))
        els.append(hart(z(txt, cx - F("Bold", 26).getlength(txt) / 2, y0 + 182, c, "Bold", 26, farbe=TEXT)))
    return els


folie([("kb", f"{PK} · Norm, die auch sie schützt"), ("v113", f"{PK} › Prüfung: Video „Nachbarklage“"),
       ("gea", f"{PK} › Gebietserhaltungsanspruch"), ("tausch", f"{PK} › alle an die Art der Nutzung gebunden"),
       ("schick", f"{PK} › rechtliche Schicksalsgemeinschaft"), ("urt93", f"{PK} › BVerwGE 94, 151")], rechts_frei([
    *tafel("kb", "1. Die Klagebefugnis"),
    z("Sie braucht eine Norm, die auch sie schützt.", 110, 180, "kb", "Bold", 34),
    zit("§ 42 Abs. 2 VwGO · Prüfung im Einzelnen: Video „Baurechtliche Nachbarklage“", 110, 232, beim("v113", "Video")),
    blk(110, 290, 1040, 76, GELB, "gea", [("Gebietserhaltungsanspruch", "ExtraBold", 36, INK)]),
    *grundstuecke(beim("gea", "Gebietserhaltungsanspruch"), 390, x0=130),
    z("Jeder muss die festgesetzte Art der Nutzung hinnehmen –", 110, 640, "tausch", "Bold", 32),
    z("dafür müssen es alle anderen auch.", 110, 688, beim("tausch", "Dafür"), "Bold", 32),
    ti("tabler", "link", 465, 520, 70, beim("tausch", "Dafür"), fuell=WEISS),
    ti("tabler", "link", 795, 520, 70, beim("tausch", "Dafür"), fuell=WEISS),
    blk(110, 745, 1040, 70, LILA, "schick", [("rechtliche Schicksalsgemeinschaft", "ExtraBold", 34, INK)]),
    zit("BVerwG, Urt. v. 16.9.1993 – 4 C 28.91, BVerwGE 94, 151 (155 ff.)", 110, 822, "urt93"),
    zit("BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8", 110, 856, "urt93"),
    *requisit([("kb", ("tabler", "shield-check", 100, WEISS), "schützt die Norm auch sie?", WEISS),
               ("gea", ("tabler", "map", 100, BLAU), "Gewerbegebiet", BLAU),
               ("schick", ("tabler", "link", 100, LILA), "gemeinsam gebunden", LILA)]),
    *allein("HO", [("kb", "denkt"), ("gea", "ruhig"), ("schick", "froh")]),
]))

# ===========================================================================================================================
# D Gebietserhaltungsanspruch: Abwehr ohne Beeinträchtigung, nur im selben Baugebiet
# ===========================================================================================================================
PG = "1. Gebietserhaltungsanspruch"


def zwei_gebiete(c, y0, grenze_cue):
    """Planausschnitt: links das Gewerbegebiet (Schreinerei, Unterkunft), rechts ein Nachbargebiet (gekreuzt bei grenze)."""
    els = [hart(El(_flaeche(620, 210, lambda dr, s: dr.rounded_rectangle((3 * s, 3 * s, 617 * s, 207 * s), 14 * s,
                                                                            fill=(236, 243, 252, 255), outline=INK, width=4 * s)),
                   130, y0, c, "fade", 0.0, None, name="plan:GE2")),
           hart(z("GE · Gewerbegebiet", 150, y0 + 10, c, "Bold", 28, farbe=TEXT)),
           hart(ti("tabler", "building-factory-2", 290, y0 + 185, 110, c, fuell=HOLZ2, anim="cut")),
           hart(ti("tabler", "building", 560, y0 + 185, 110, c, fuell=HELLGRUEN, anim="cut"))]
    els += [El(_flaeche(360, 210, lambda dr, s: dr.rounded_rectangle((3 * s, 3 * s, 357 * s, 207 * s), 14 * s,
                                                                       fill=(246, 238, 226, 255), outline=INK, width=4 * s)),
               790, y0, grenze_cue, "pop", 0.0, None, name="plan:Nachbargebiet"),
            z("anderes Baugebiet", 810, y0 + 10, grenze_cue, "Bold", 28, farbe=TEXT),
            ti("tabler", "home", 970, y0 + 185, 100, grenze_cue, fuell=WEISS),
            nein(1080, y0 + 150, grenze_cue, gr=26)]
    return els


folie([("abwehr", f"{PG} › Abwehr gebietsfremder Nutzung"), ("unabh", f"{PG} › ohne tatsächliche Beeinträchtigung"),
       ("beweis", f"{PG} › kein Nachweis der Störung nötig"), ("grenze", f"{PG} › nur im selben Baugebiet")], rechts_frei([
    *tafel("abwehr", "Gebietserhaltungsanspruch: die Folgen"),
    *okz("Jeder Eigentümer kann gebietsfremde Nutzung abwehren,", 180, "abwehr", "Bold", 32, x=160),
    *okz("unabhängig von einer tatsächlichen Beeinträchtigung.", 240, "unabh", "Bold", 32, x=160),
    zit("BVerwG, Beschl. v. 27.8.2013 – 4 B 39.13, Rn. 3; Urt. v. 2.2.2012 – 4 C 14.10, Rn. 24", 160, 292, "unabh"),
    blk(110, 345, 1040, 76, HELLGRUEN, "beweis", [("Frau Hollenberg muss keine Störung beweisen.", "ExtraBold", 33, INK)]),
    *neinz("Aber: nur innerhalb desselben Baugebiets", 455, "grenze", "Bold", 32, x=160),
    zit("BVerwG, Beschl. v. 15.9.2020 – 4 B 46.19, Rn. 6", 160, 505, "grenze"),
    *zwei_gebiete("abwehr", 570, "grenze"),
    *requisit([("abwehr", ("tabler", "shield", 100, WEISS), "Abwehr", WEISS),
               ("beweis", ("tabler", "file-off", 100, HELLGRUEN), "kein Nachweis nötig", HELLGRUEN),
               ("grenze", ("tabler", "map", 100, BLAU), "nur im Baugebiet", BLAU)]),
    *allein("HO", [("abwehr", "ruhig"), ("beweis", "erleichtert"), ("grenze", "denkt")]),
]))

# ===========================================================================================================================
# E 2. § 8 BauNVO (Wortlaut Abs. 1, Abs. 3 Nr. 2): Anlage für soziale Zwecke?
# ===========================================================================================================================
P8 = "2. § 8 BauNVO"
W8 = ("„(1) Gewerbegebiete dienen vorwiegend der Unterbringung von nicht erheblich belästigenden Gewerbebetrieben. … "
      "(3) Ausnahmsweise können zugelassen werden … 2. Anlagen für kirchliche, kulturelle, soziale und gesundheitliche "
      "Zwecke, …“")
w8, w8_y = wortlaut(80, 165, 1100, W8, "§ 8 Abs. 1, Abs. 3 Nr. 2 BauNVO", "p8", marken=[
    ("vorwiegend", beim("p8a", "vorwiegend")), ("belästigenden Gewerbebetrieben.", beim("p8a", "belästigenden")),
    ("Ausnahmsweise", beim("p8b", "ausnahmsweise")), ("soziale", beim("p8b", "soziale"))], size=31)
folie([("p8", f"{P8} · Ist die Unterkunft gebietsfremd?"), ("p8a", f"{P8} › Abs. 1: Gewerbebetriebe"),
       ("p8b", f"{P8} › Abs. 3 Nr. 2: soziale Zwecke ausnahmsweise"),
       ("sozial", f"{P8} › Gemeinschaftsunterkunft: Anlage für soziale Zwecke?")], rechts_frei([
    *tafel("p8", "2. Gebietsfremd? § 8 BauNVO"),
    *w8,
    blk(110, w8_y + 35, 1040, 110, WEISS, "sozial", [("Gemeinschaftsunterkunft:", "ExtraBold", 33, INK),
                                                    ("als Anlage für soziale Zwecke denkbar", "Bold", 33, INK)]),
    zit("vgl. BT-Drs. 18/2752, S. 8, 12; BVerwG, Beschl. v. 27.2.2018 – 4 B 39.17, Rn. 10", 110, w8_y + 160, "sozial"),
    *requisit([("p8", ("tabler", "book", 100, WEISS), "BauNVO", WEISS),
               ("p8a", ("tabler", "building-factory-2", 110, HOLZ2), "Gewerbebetriebe", HOLZ2),
               ("sozial", ("tabler", "building", 100, HELLGRUEN), "soziale Zwecke?", HELLGRUEN)]),
    *zwei([("p8", "ruhig"), ("sozial", "denkt")], [("p8", "ruhig"), ("p8b", "denkt")]),
]))
assert w8_y + 200 <= 890, w8_y

# ===========================================================================================================================
# F Gebietsverträglichkeit: Wohnen im Gewerbegebiet? (4 C 14.10, 4 B 86.01, 4 B 39.17), § 31 Abs. 2 BauGB
# ===========================================================================================================================
PV = "2. Gebietsverträglichkeit"
folie([("gv", f"{PV} › auch die Ausnahme muss passen"), ("nwohn", f"{PV} › im Gewerbegebiet kein Wohnen"),
       ("pflege", f"{PV} › Pflegeheim: wohnähnlich, unzulässig"), ("monate", f"{PV} › Unterkunft: wohnähnlich"),
       ("rspr", f"{PV} › vielfach unzulässig, auch als Ausnahme"), ("b31", f"{PV} › § 31 Abs. 2 BauGB: Grundzüge der Planung"),
       ("gut", f"{PV} › gute Chancen für Frau Hollenberg")], rechts_frei([
    *tafel("gv", "Gebietsverträglichkeit: wohnähnlich?"),
    blk(110, 172, 1040, 70, LILA, "gv", [("Auch die Ausnahme muss zum Gebiet passen.", "ExtraBold", 33, INK)]),
    zit("BVerwG, Urt. v. 2.2.2012 – 4 C 14.10, Rn. 16 f.", 110, 252, "gv"),
    z("Im Gewerbegebiet soll nicht gewohnt werden.", 110, 300, "nwohn", "Bold", 33),
    z("Pflegeheim: wohnähnlich, typischerweise unzulässig", 110, 352, "pflege", "Regular", 32),
    zit("BVerwG, Beschl. v. 13.5.2002 – 4 B 86.01", 110, 398, "pflege"),
    z("Unterkunft: schlafen, essen, leben über Monate", 110, 446, "monate", "Regular", 32),
    z("also: wohnähnlich", 110, 494, beim("monate", "wohnähnlich"), "ExtraBold", 33),
    *neinz("vielfach unzulässig, auch als Ausnahme", 550, "rspr", "Bold", 32, x=160),
    zit("BT-Drs. 18/2752, S. 12; BVerwG, Beschl. v. 27.2.2018 – 4 B 39.17, Rn. 11, 16", 160, 600, "rspr"),
    *neinz("Befreiung, § 31 Abs. 2 BauGB: nur ohne Berührung", 652, "b31", "Bold", 32, x=160),
    z("der Grundzüge der Planung", 160, 698, beim("b31", "Grundzüge"), "Bold", 32),
    blk(110, 760, 1040, 76, HELLGRUEN, "gut", [("Zwischenstand: gute Chancen für Frau Hollenberg", "ExtraBold", 33, INK)]),
    *requisit([("gv", ("tabler", "building-factory-2", 110, HOLZ2), "Zweck des Gebiets", HOLZ2),
               ("nwohn", ("tabler", "home", 100, HELLROT), "kein Wohnen", HELLROT),
               ("monate", ("tabler", "bed", 100, WEISS), "wohnähnlich", WEISS),
               ("gut", ("tabler", "scale", 100, HELLGRUEN), "Zwischenstand", HELLGRUEN)]),
    *zwei([("gv", "denkt"), ("gut", "froh")], [("gv", "ernst"), ("gut", "denkt")]),
]))

# ===========================================================================================================================
# G 3. § 246 Abs. 10 BauGB (Wortlaut)
# ===========================================================================================================================
P246 = "3. § 246 Abs. 10 BauGB"
W10 = ("„(10) Bis zum Ablauf des 31. Dezember 2027 kann in Gewerbegebieten (§ 8 der Baunutzungsverordnung, auch in "
       "Verbindung mit § 34 Absatz 2) für Aufnahmeeinrichtungen, Gemeinschaftsunterkünfte oder sonstige Unterkünfte für "
       "Flüchtlinge oder Asylbegehrende von den Festsetzungen des Bebauungsplans befreit werden, wenn an dem Standort Anlagen "
       "für soziale Zwecke als Ausnahme zugelassen werden können oder allgemein zulässig sind und die Abweichung auch unter "
       "Würdigung nachbarlicher Interessen mit öffentlichen Belangen vereinbar ist. …“")
w10, w10_y = wortlaut(80, 225, 1100, W10, "§ 246 Abs. 10 S. 1 BauGB (Stand: zuletzt geändert 23.7.2026)", "p246", marken=[
    ("31. Dezember 2027", beim("w10", "Ende")), ("in Gewerbegebieten", beim("w10", "Gewerbegebieten")),
    ("befreit werden,", beim("w10", "befreit")), ("als Ausnahme", beim("w10b", "Ausnahme")),
    ("Würdigung nachbarlicher", beim("w10c", "Würdigung"))], size=30)
folie([("p246", f"{P246} · befristete Sonderregeln"), ("w10", f"{P246} › Befreiung im Gewerbegebiet bis 31.12.2027"),
       ("w10b", f"{P246} › Standort: soziale Anlagen als Ausnahme"),
       ("w10c", f"{P246} › Würdigung nachbarlicher Interessen")], rechts_frei([
    *tafel("p246", "3. Sonderregel: § 246 Abs. 10 BauGB"),
    z("befristete Sonderregeln für Flüchtlingsunterkünfte", 110, 172, beim("p246", "befristete"), "Bold", 32),
    *w10,
    *requisit([("p246", ("tabler", "book", 100, WEISS), "§ 246 BauGB", WEISS),
               ("w10", ("tabler", "calendar", 100, GELB), "bis 31.12.2027", GELB),
               ("w10c", ("tabler", "scale", 100, WEISS), "nachbarliche Interessen", WEISS)]),
    *zwei([("p246", "sorge"), ("w10c", "denkt")], [("p246", "ruhig"), ("w10", "froh")]),
]))
assert w10_y <= 880, w10_y

# ===========================================================================================================================
# H § 246 Abs. 10 am Fall: Standort, kein Gebietsbezug (4 B 39.17), Grundzüge der Planung
# ===========================================================================================================================
PF = "3. § 246 Abs. 10 am Fall"
folie([("stand", f"{PF} › Standort (+)"), ("zweck", f"{PF} › Zweck des Gewerbegebiets: egal"),
       ("bv18", f"{PF} › BVerwG 2018: Anspruch eingeschränkt"), ("gzp", f"{PF} › Grundzüge der Planung: egal")], rechts_frei([
    *tafel("stand", "§ 246 Abs. 10 BauGB am Fall"),
    *okz("Standort: soziale Anlagen als Ausnahme nicht ausgeschlossen", 180, "stand", "Bold", 31, x=160),
    zit("§ 1 Abs. 3 S. 2 BauNVO; vgl. BVerwG 4 B 39.17, Rn. 10", 160, 230, "stand"),
    *okz("muss nicht zum Zweck des Gewerbegebiets passen", 290, "zweck", "Bold", 32, x=160),
    blk(110, 355, 1040, 120, LILA, "bv18", [("BVerwG 2018, ähnlicher Fall:", "ExtraBold", 33, INK),
                                          ("Gebietserhaltungsanspruch eingeschränkt", "Bold", 33, INK)]),
    zit("BVerwG, Beschl. v. 27.2.2018 – 4 B 39.17, Rn. 1, 11, 13 (Bürogebäude im GE)", 110, 485, "bv18"),
    *okz("Grundzüge der Planung: anders als bei § 31 Abs. 2", 545, "gzp", "Bold", 32, x=160),
    z("ohne Bedeutung", 160, 593, beim("gzp", "nicht"), "Bold", 32),
    zit("BT-Drs. 18/2752, S. 12", 160, 643, "gzp"),
    *requisit([("stand", ("tabler", "map", 100, BLAU), "Ausnahme möglich", BLAU),
               ("bv18", ("tabler", "scale", 100, LILA), "BVerwG 2018", LILA),
               ("gzp", ("tabler", "file-certificate", 100, GELB), "Befreiung", GELB)]),
    *zwei([("stand", "sorge"), ("bv18", "ernst")], [("stand", "ruhig"), ("zweck", "froh")]),
]))

# ===========================================================================================================================
# I Grenzen: § 246 Abs. 13a (Wortlaut), Frist und Abs. 17
# ===========================================================================================================================
PI = "3. Grenzen der Sonderregel"
W13 = ("„(13a) Von den Absätzen 8 bis 13 darf nur Gebrauch gemacht werden, soweit dringend benötigte Unterkünfte im "
       "Gebiet der Gemeinde, in der sie entstehen sollen, nicht oder nicht rechtzeitig bereitgestellt werden können.“")
w13, w13_y = wortlaut(80, 165, 1100, W13, "§ 246 Abs. 13a BauGB", "dring", marken=[
    ("dringend benötigte", beim("dring", "dringend")), ("nicht rechtzeitig", beim("dring", "rechtzeitig"))], size=31)
folie([("dring", f"{PI} › Abs. 13a: dringender Bedarf"), ("frist", f"{PI} › Abs. 17: Frist für das Zulassungsverfahren")],
      rechts_frei([
    *tafel("dring", "Die Grenzen der Sonderregel"),
    *w13,
    *okz("Die Stadt hat den Bedarf dargelegt.", w13_y + 25, beim("dring", "dargelegt"), "Bold", 32, x=160),
    blk(110, w13_y + 95, 1040, 76, GELB, "frist", [("Frist 31.12.2027: nur für das Zulassungsverfahren", "ExtraBold", 32, INK)]),
    *okz("Die Genehmigung selbst wird nicht befristet.", w13_y + 195, beim("frist", "Genehmigung"), "Bold", 32, x=160),
    zit("§ 246 Abs. 17 BauGB; BVerwG, Beschl. v. 27.2.2018 – 4 B 39.17, Rn. 13", 160, w13_y + 245, beim("frist", "Genehmigung")),
    *requisit([("dring", ("tabler", "hourglass", 100, WEISS), "dringend benötigt", WEISS),
               ("frist", ("tabler", "calendar", 100, GELB), "bis 31.12.2027", GELB)]),
    *allein("KE", [("dring", "ruhig"), ("frist", "froh")]),
]))
assert w13_y + 290 <= 890, w13_y

# ===========================================================================================================================
# J 4. Rücksichtnahme: § 15 Abs. 1 S. 2 BauNVO (Wortlaut), heranrückende Nutzung, Lärmgutachten
# ===========================================================================================================================
PR = "4. Rücksichtnahme"
W15 = ("„Sie sind auch unzulässig, wenn von ihnen Belästigungen oder Störungen ausgehen können, die nach der Eigenart des "
       "Baugebiets im Baugebiet selbst oder in dessen Umgebung unzumutbar sind, oder wenn sie solchen Belästigungen oder "
       "Störungen ausgesetzt werden.“")
w15, w15_y = wortlaut(80, 280, 1100, W15, "§ 15 Abs. 1 S. 2 BauNVO", "p15", marken=[
    ("unzumutbar", beim("p15", "unzumutbaren")), ("ausgesetzt werden.", beim("p15", "ausgesetzt"))], size=30)
folie([("rueck", f"{PR} · Würdigung nachbarlicher Interessen"), ("p15", f"{PR} › § 15 Abs. 1 S. 2 BauNVO"),
       ("heran", f"{PR} › wer heranrückt, muss Lärm aushalten können"),
       ("gutacht", f"{PR} › Gutachten: Werte eingehalten")], rechts_frei([
    *tafel("rueck", "4. Die Rücksichtnahme"),
    z("Würdigung nachbarlicher Interessen = Rücksichtnahme", 110, 172, "rueck", "Bold", 32),
    zit("vgl. BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 12", 110, 220, "rueck"),
    *w15,
    z("Wer heranrückt, muss zulässigen Lärm aushalten können.", 110, w15_y + 22, "heran", "Bold", 32),
    zit("BVerwG, Urt. v. 29.11.2012 – 4 C 8.11, Rn. 16", 110, w15_y + 70, "heran"),
    *okz("Gutachten: Werte für ein Gewerbegebiet eingehalten", w15_y + 125, "gutacht", "Bold", 32, x=160),
    *okz("Die Schreinerei muss nichts ändern.", w15_y + 180, beim("gutacht", "nichts"), "Bold", 32, x=160),
    *requisit([("rueck", ("tabler", "scale", 100, WEISS), "Rücksichtnahme", WEISS),
               ("heran", ("tabler", "volume", 100, HOLZ2), "Betriebslärm", HOLZ2),
               ("gutacht", ("tabler", "clipboard-check", 100, HELLGRUEN), "Lärmgutachten", HELLGRUEN)]),
    *allein("HO", [("rueck", "ruhig"), ("heran", "ernst"), ("gutacht", "erleichtert")]),
]))
assert w15_y + 230 <= 890, w15_y

# ===========================================================================================================================
# K Ergebnis: zurück im Gewerbegebiet, Frau Hollenberg (Blase)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Befreiung rechtmäßig, Klage unbegründet"),
       ("erg2", "Ergebnis · Abs. 10 macht die Unterkunft hier möglich"),
       ("ho2", "Ergebnis · Die Schreinerei bleibt, wie sie ist")], [
    *gewerbegebiet("erg", unterkunft=True, pille=False),
    hart(pl("Ergebnis", 70, 30, "erg", fill=PINK, size=38)),
    bis_(ok(700, 148, beim("erg", "Befreiung"), gr=24), None),
    pl("Befreiung rechtmäßig", 740, 120, beim("erg", "Befreiung"), fill=HELLGRUEN, size=34),
    bis_(nein(700, 228, beim("erg", "unbegründet"), gr=22), None),
    pl("Klage unbegründet", 740, 200, beim("erg", "unbegründet"), fill=HELLROT, size=34),
    pl("§ 246 Abs. 10 BauGB macht die Unterkunft hier möglich", 700, 290, beim("erg2", "Absatz"), fill=WEISS, size=30),
    *fig("HO", HOX, BODEN_Y, FHA, [("erg", "ernst_r"), ("erg2", "ruhig_r")], erst="pop", bis="ho2"),
    ns(NAME["HO"], HOX, BODEN_Y, "erg", NFARBE["HO"], d=0.1),
    *redet("HO_redet2_r", HOX, BODEN_Y, FHA, "ho2", "tipp"),
    blase("sprech", 540, 250, "ho2", 300, 285, inhalt=["Dann bleibt meine", "Werkstatt, wie sie ist.", "Das war mir das Wichtigste."],
          textsize=32, figur=("HO_redet2_r", HOX, BODEN_Y, FHA), bis="tipp"),
    *fig("KE", KEX, BODEN_Y, FHA, [("erg", "ruhig"), ("ho2", "froh")], erst="pop"),
    ns(NAME["KE"], KEX, BODEN_Y, "erg", NFARBE["KE"], d=0.1),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi): zwei Stufen, Datum, nur städtebauliche Belange
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: in zwei Stufen prüfen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Art der Nutzung im Gewerbegebiet:", 200, 200, "tipp", "Bold", 34),
         blk(130, 280, 1020, 76, GRUEN, "k1", [("1. § 8 BauNVO: Ausnahme, Gebietsverträglichkeit", "ExtraBold", 32, INK)]),
         blk(130, 372, 1020, 76, GELB, "k2", [("2. § 246 Abs. 10 BauGB als Befreiung", "ExtraBold", 32, INK)]),
         z("Datum beachten: nach dem 31.12.2027 nach heutigem", 130, 480, "k3", "Bold", 32),
         z("Stand keine Befreiung mehr nach Abs. 10", 130, 526, beim("k3", "Absatz"), "Bold", 32),
         zit("§ 246 Abs. 10, 17 BauGB (Stand 8.10.2026)", 130, 574, beim("k3", "Absatz")),
         blk(130, 625, 1020, 76, BLAU, "k4", [("Nur städtebauliche Belange: Lärm, Verkehr", "ExtraBold", 32, INK)]),
         z("Eigenschaften der Bewohner: i. d. R. kein Gesichtspunkt", 130, 718, beim("k4", "Gefahren"), "Bold", 31),
         zit("BVerwG, Beschl. v. 6.12.2011 – 4 BN 20.11, Rn. 5, 7", 130, 765, beim("k4", "Gefahren")),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · in zwei Stufen prüfen"), ("k1", "Klausurtipp › 1. § 8 BauNVO"),
       ("k2", "Klausurtipp › 2. § 246 Abs. 10 BauGB"), ("k3", "Klausurtipp › Datum: 31.12.2027"),
       ("k4", "Klausurtipp › nur städtebauliche Belange")], els_k)

# ===========================================================================================================================
# M Schema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Klagebefugnis: Gebietserhaltungsanspruch (§ 42 Abs. 2 VwGO)"),
          ("s2", 0, "2. Begründetheit (§ 113 Abs. 1 S. 1 VwGO)"),
          ("s2a", 1, "a) § 8 BauNVO: wohnähnliche Unterkunft weder allgemein noch als Ausnahme zulässig"),
          ("s2b", 1, "b) aber Befreiung nach § 246 Abs. 10 BauGB: Standort und Rücksichtnahme"),
          ("s2c", 1, "c) Grenzen: Dringlichkeit (Abs. 13a) und Frist (31.12.2027, Abs. 17)"),
          ("s3", 0, "3. Ergebnis: keine Rechtsverletzung, Klage unbegründet")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Nachbarklage gegen die Unterkunft"), 110, 90, "sch", 46)]
y = 215
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (40, 35)[ebene], rechts=1820))
    y += {0: 100, 1: 86}[ebene]
assert y <= 960, y
folie([("sch", "Schema · Nachbarklage gegen die Unterkunft"), ("s1", "Schema › 1. Klagebefugnis"),
       ("s2", "Schema › 2. Begründetheit"), ("s2a", "Schema › 2. a) § 8 BauNVO"), ("s2b", "Schema › 2. b) § 246 Abs. 10 BauGB"),
       ("s2c", "Schema › 2. c) Dringlichkeit und Frist"), ("s3", "Schema › 3. Ergebnis")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im Baugebiet bilden die Eigentümer eine", 0)], [("Schicksalsgemeinschaft", "a"), (".", 0)]], 750, 280, 40,
                "merke", {"a": beim("merke", "Schicksalsgemeinschaft")}),
    *markertext([[("Jeder kann eine ", 0), ("gebietsfremde Nutzung", "b"), (" abwehren,", 0)],
                 [("auch ohne gestört zu sein.", 0)]], 750, 445, 40, "m2", {"b": beim("m2", "gebietsfremde")}),
    *markertext([[("Für Flüchtlingsunterkünfte öffnet ", 0), ("§ 246 Abs. 10", "c")],
                 [("das Gewerbegebiet aber, ", 0), ("befristet bis Ende 2027", "d"), (".", 0)]], 750, 620, 40, "m3",
                {"c": beim("m3", "Paragraf"), "d": beim("m3", "befristet")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
