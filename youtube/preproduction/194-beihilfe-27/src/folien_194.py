"""Folge 194 · Beihilfe § 27 StGB: Schema – wie viel Hilfe macht strafbar? – Serienstandard Open Peeps (Katzenkönig).
Fall: Falko erzählt seiner Freundin Hedda am Freitagabend, dass er am Samstag in ein bewohntes Einfamilienhaus am
Stadtrand einbrechen will (welches, sagt er nicht); Hedda findet das falsch, gibt ihm aber den Autoschlüssel und will nichts
von der Beute. Samstag 22 Uhr: Falko fährt hin, bricht ein, nimmt Schmuck für 3.000 € und bringt ihn im Kofferraum weg.
Szenen laut ../SZENENPLAN.md: A1 vor der Haustür von Hedda, A2 das Haus am Stadtrand, A3 die Frage, B Sachverhalt,
C Wortlaut § 27 Abs. 1 und 2, D Prüfschema I. 1. a) (limitierte Akzessorietät, § 29), E1 b) Hilfeleisten, E2 Meinungsstand
(BGH-Förderungsformel – h. L. Kausalität), F 2. doppelter Gehilfenvorsatz, G Prüfschema komplett (II., III., Strafe),
H1–H4 Lösung, I1/I2 Sonderfälle, J Klausurtipp (Lexi), K Merksatz (Lexi).
Darstellung: Einbruch nur als Haus- und Schloss-Icon (zu → offen), keine Anleitung, kein Werkzeug; Personen fiktiv.
Handlungsgeräusche: Schlüssel (A1, Übergabe), Kofferraumklappe (A2); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 192 (gemeinsame Dateien unverändert); neu: fassade(), tuer(), stehend()/zwei() für FA/HE.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (StGB), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_194/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_194/" in n:
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
NAME = {"FA": "Falko", "HE": "Hedda"}
NFARBE = {"FA": GRUEN, "HE": ROT}
HOLZ = (214, 160, 110, 255)
HELLROT = (253, 232, 228, 255)
HELLGRAU = (226, 226, 222, 255)
ZITAT = (246, 246, 250, 255)
HELL = (255, 251, 230, 255)


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_he, folge_fa):
    """Hedda und Falko rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HE", X1, folge_he), *stehend("FA", X2, folge_fa)]


FE = "fluent-emoji-high-contrast"


def fassade(c, x0=80, x1=860, oben=380):
    """Hauswand von Hedda (Grundform), Tuschekontur."""
    w, h = x1 - x0, BODEN_Y - oben
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h + 2) * s), fill=WAND2, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h + 4, zz), x0, oben, c, "cut", 0.0, None, name="fassade"))


def tuer(c, x0=560, w=170, h=330):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h + 2) * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.ellipse(((w - 40) * s, (h // 2) * s, (w - 24) * s, (h // 2 + 16) * s), fill=INK)
    return hart(El(_flaeche(w, h + 4, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="tuer"))


# ===========================================================================================================================
# A1 Fall: Freitagabend vor der Haustür von Hedda
# ===========================================================================================================================
HEX, FAX = 1010, 1450
TUER_SCHL = beim("he1", "Schlüssel")
folie([(NULL, "Fall · Freitagabend bei Hedda"), ("plan", "Fall · Falko erzählt seinen Plan"),
       ("familie", "Fall · Ein bewohntes Einfamilienhaus"), ("welches", "Fall · Welches Haus? Sagt er nicht"),
       ("fa1", "Fall · Falko bittet um das Auto"), ("he1", "Fall · Hedda gibt den Schlüssel"),
       ("nichts", "Fall · Hedda will nichts von der Beute")], [
    fassade(NULL),
    tuer(NULL),
    fenster(NULL, 150, 470, 260, 230),
    boden(NULL),
    hart(ficon(FE, "crescent-moon", 1790, 190, 90, NULL, fuell=GELB, anim="cut")),
    hart(pl("Freitagabend", 70, 30, NULL, fill=LILA, size=38)),
    hart(ficon(FE, "automobile", 1735, BODEN_Y, 250, NULL, fuell=ROT, anim="cut")),
    pl("Samstag: Einbruch in ein Einfamilienhaus", 70, 110, "plan", fill=WEISS, size=32),
    ficon(FE, "house", 930, 175, 80, "plan", fuell=GELB, bis="fa1"),
    pl("dort wohnt eine Familie – abends nicht zu Hause", 70, 185, "familie", fill=WEISS, size=30),
    pl("Welches Haus? Sagt er nicht.", 70, 255, "welches", fill=PINK, size=30),
    pl("Auto von Hedda", 1735, 625, beim("fa1", "Auto"), fill=WEISS, size=26, anker="m"),
    *fig("HE", HEX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("plan", "denkt_r"), ("familie", "sorge_r")], erst="cut", bis="fa1"),
    *fig("HE", HEX, BODEN_Y, FHA, [("fa1", "sorge_r")], erst="cut", bis="he1"),
    *redet("HE_redet_r", HEX, BODEN_Y, FHA, "he1", "nichts"),
    *fig("HE", HEX, BODEN_Y, FHA, [("nichts", "ernst_r")], erst="cut"),
    hart(ns(NAME["HE"], HEX, BODEN_Y, NULL, NFARBE["HE"])),
    *fig("FA", FAX, BODEN_Y, FHA, [(NULL, "ruhig"), ("plan", "entschlossen"), ("welches", "denkt")], erst="cut", bis="fa1"),
    *redet("FA_redet", FAX, BODEN_Y, FHA, "fa1", "he1"),
    *fig("FA", FAX, BODEN_Y, FHA, [("he1", "ruhig")], erst="cut"),
    hart(ns(NAME["FA"], FAX, BODEN_Y, NULL, NFARBE["FA"])),
    blase("sprech", 940, 230, "fa1", 1270, 200, inhalt=["Leihst du mir dein Auto? Mit dem Bus", "komme ich da nicht hin, und die",
                                                      "Beute muss ja auch weg."], textsize=34,
          figur=("FA_redet", FAX, BODEN_Y, FHA), bis="he1"),
    blase("sprech", 860, 230, "he1", 1230, 200, inhalt=["Ich finde das falsch. Aber gut,", "hier ist der Schlüssel.",
                                                      "Bring ihn mir Sonntag zurück."], textsize=34,
          figur=("HE_redet_r", HEX, BODEN_Y, FHA), bis="nichts"),
    szene(bewegt(ficon(FE, "key", 1330, 690, 70, TUER_SCHL, fuell=GELB, anim="cut"), TUER_SCHL,
                 (TUER_SCHL[0], TUER_SCHL[1] + 0.9), -230, 0), "194schluessel_1", 1.0, 0.0),
    pl("von der Beute: nichts", HEX, 360, "nichts", fill=HELLGRAU, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: Samstag, 22 Uhr – das Haus am Stadtrand
# ===========================================================================================================================
AUTO_X = 1060
FA2X = 1450
KOFFER0 = ("koffer", 0.3)
KOFFER1 = ("koffer", 1.4)
KOFFER2 = ("koffer", 1.6)                  # Schmuck verschwindet hinten im Auto (Kofferraum)
folie([("sa", "Fall · Samstag, 22 Uhr: das Haus am Stadtrand"), ("einbruch", "Fall · Falko bricht ein"),
       ("beute", "Fall · Schmuck für 3.000 €"), ("koffer", "Fall · Die Beute im Kofferraum")], [
    boden("sa"),
    hart(ficon(FE, "house-with-garden", 430, BODEN_Y, 560, "sa", fuell=GELB, anim="cut")),
    hart(ficon(FE, "crescent-moon", 1790, 190, 90, "sa", fuell=GELB, anim="cut")),
    hart(pl("Samstag, 22 Uhr · Stadtrand", 70, 30, "sa", fill=LILA, size=38)),
    hart(ficon(FE, "ten-oclock", 830, 130, 80, "sa", fuell=WEISS, anim="cut")),
    pl("bewohnt: Familie nicht zu Hause", 70, 110, "sa", fill=WEISS, size=30, d=0.3),
    bewegt(ficon(FE, "automobile", AUTO_X, BODEN_Y, 300, "sa", fuell=ROT, anim="cut"), "sa", ("sa", 2.2), 640, 0),
    pl("Auto von Hedda", AUTO_X, 630, beim("sa", "Auto"), fill=WEISS, size=26, anker="m", bis=KOFFER0),
    ficon(FE, "locked", 780, 560, 90, "sa", fuell=GELB, bis="einbruch", anim="cut"),
    ficon(FE, "unlocked", 780, 560, 90, "einbruch", fuell=GELB, anim="cut"),
    pl("Einbruch", 780, 390, "einbruch", fill=HELLROT, size=32, anker="m"),
    ficon(FE, "gem-stone", 740, 880, 70, "beute", fuell=BLAU, bis=KOFFER0),
    ficon(FE, "ring", 810, 880, 60, "beute", fuell=GELB, bis=KOFFER0),
    pl("Schmuck: 3.000 €", 1000, 200, "beute", fill=GELB, size=34),
    szene(bewegt(ficon(FE, "gem-stone", AUTO_X + 95, 800, 70, KOFFER0, fuell=BLAU, anim="cut", bis=KOFFER2), KOFFER0, KOFFER1,
                 -415, 80), "194kofferraum_1", 1.0, 1.15),
    bewegt(ficon(FE, "ring", AUTO_X + 105, 800, 60, KOFFER0, fuell=GELB, anim="cut", bis=KOFFER2), KOFFER0, KOFFER1, -355, 80),
    pl("im Kofferraum weg", 1000, 280, beim("koffer", "Kofferraum"), fill=WEISS, size=32),
    *fig("FA", FA2X, BODEN_Y, FHA, [(beim("sa", "Falko"), "entschlossen"), ("einbruch", "ernst"), ("koffer", "entschlossen")]),
    ns(NAME["FA"], FA2X, BODEN_Y, beim("sa", "Falko"), NFARBE["FA"], d=0.1),
])

# ===========================================================================================================================
# A3 Fall: die Frage
# ===========================================================================================================================
FA3X, HE3X = 620, 1350
folie([("frage", "Fall · Falko: Täter. Und Hedda?"), ("frage2", "Fall · Wie viel Hilfe macht strafbar?")], [
    boden("frage"),
    hart(ficon(FE, "automobile", 985, BODEN_Y, 260, "frage", fuell=ROT, anim="cut")),
    hart(ficon(FE, "key", 985, 640, 70, "frage", fuell=GELB, anim="cut")),
    *fig("FA", FA3X, BODEN_Y, FHA, [("frage", "ruhig_r")], erst="cut"),
    hart(ns(NAME["FA"], FA3X, BODEN_Y, "frage", NFARBE["FA"])),
    *fig("HE", HE3X, BODEN_Y, FHA, [("frage", "ruhig"), (beim("frage", "Hedda"), "sorge")], erst="cut"),
    hart(ns(NAME["HE"], HE3X, BODEN_Y, "frage", NFARBE["HE"])),
    *okz("Falko: Täter", 70, beim("frage", "Täter"), "ExtraBold", 38, x=440),
    pl("Und Hedda?", 1160, 70, beim("frage", "Hedda"), fill=PINK, size=38),
    pl("nur ein Auto verliehen", 1080, 160, "frage2", fill=WEISS, size=32),
    pl("Wie viel Hilfe macht strafbar?", 520, 260, beim("frage2", "Wie"), fill=GELB, size=40),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_194(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_194("sv", [
    "Am Freitagabend erzählt Falko seiner Freundin Hedda offen, dass er am Samstag in ein Einfamilienhaus am Stadtrand "
    "einbrechen will. Dort wohnt eine Familie, die an dem Abend nicht zu Hause ist. Welches Haus genau, sagt er nicht.",
    "Falko: „Leihst du mir dein Auto? Mit dem Bus komme ich da nicht hin, und die Beute muss ja auch weg.“ Hedda: „Ich finde "
    "das falsch. Aber gut, hier ist der Schlüssel. Bring ihn mir Sonntag zurück.“ Von der Beute will Hedda nichts.",
    "Am Samstag um 22 Uhr fährt Falko mit dem Auto von Hedda zu dem Haus, bricht ein und nimmt Schmuck für 3.000 € mit. Die "
    "Beute bringt er im Kofferraum weg.",
], "Hat sich Hedda strafbar gemacht?")

# ===========================================================================================================================
# C Wortlaut § 27 Abs. 1 und 2 StGB
# ===========================================================================================================================
PW = "Beihilfe, § 27 StGB"
W1 = ("„(1) Als Gehilfe wird bestraft, wer vorsätzlich einem anderen zu dessen vorsätzlich begangener rechtswidriger Tat "
      "Hilfe geleistet hat.“")
w1, w1_y = wortlaut(80, 175, 1100, W1, "§ 27 Abs. 1 StGB", "p27", marken=[
    ("Gehilfe", beim("p27w", "Gehilfe")), ("vorsätzlich", beim("p27w", "vorsätzlich")),
    ("rechtswidriger Tat", beim("p27w", "rechtswidriger")), ("Hilfe geleistet", beim("p27w", "Hilfe"))], size=34)
W2 = ("„(2) Die Strafe für den Gehilfen richtet sich nach der Strafdrohung für den Täter. Sie ist nach § 49 Abs. 1 zu "
      "mildern.“")
w2, w2_y = wortlaut(80, w1_y + 34, 1100, W2, "§ 27 Abs. 2 StGB", "p27a2", marken=[
    ("Strafdrohung", beim("p27a2", "Strafdrohung")), ("für den Täter.", beim("p27a2", "Täter")), ("mildern.", beim("p27s2", "mildern"))], size=34)
folie([("p27", f"{PW} › Wortlaut Abs. 1"), ("p27a2", f"{PW} › Wortlaut Abs. 2: Strafe"),
       ("p27s2", f"{PW} › zwingende Milderung, § 49 Abs. 1")], rechts_frei([
    *tafel("p27", "Beihilfe, § 27 StGB"),
    *w1, *w2,
    *requisit([("p27", (FE, "balance-scale", 110, GELB), "§ 27 StGB", GELB),
               ("p27a2", (FE, "balance-scale", 110, GELB), "Strafe wie Täter …", WEISS),
               ("p27s2", (FE, "balance-scale", 110, GELB), "… aber gemildert", GRUEN)]),
    *zwei([("p27", "denkt"), ("p27a2", "sorge")], [("p27", "ruhig"), ("p27s2", "ernst")]),
]))
assert w2_y <= 890, w2_y

# ===========================================================================================================================
# D Prüfschema I. 1. a): vorsätzliche rechtswidrige Haupttat, limitierte Akzessorietät (§ 29)
# ===========================================================================================================================
PS1 = "Prüfschema › I. Tatbestand"
W29 = "„Jeder Beteiligte wird ohne Rücksicht auf die Schuld des anderen nach seiner Schuld bestraft.“"
w29, w29_y = wortlaut(330, 485, 1430, W29, "§ 29 StGB", "p29", marken=[
    ("ohne Rücksicht auf die Schuld des anderen", beim("p29", "Rücksicht")), ("nach seiner Schuld", beim("p29", "seiner"))],
    size=34)
folie([("sch", "Prüfschema · Beihilfe, § 27 StGB"), ("s_i", PS1), ("s1", f"{PS1} › 1. objektiv"),
       ("s1a", f"{PS1} › 1. a) Haupttat"), ("akz", f"{PS1} › 1. a) Schuld des Haupttäters nicht nötig"),
       ("p29", f"{PS1} › 1. a) § 29 StGB"), ("lim", f"{PS1} › 1. a) limitierte Akzessorietät")], [
    karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Beihilfe, § 27 StGB"), 110, 90, "sch", 46),
    z("I. Tatbestand", 130, 200, "s_i", "ExtraBold", 40, rechts=1800),
    z("1. objektiver Tatbestand", 200, 280, "s1", "Bold", 36, rechts=1800),
    z("a) vorsätzliche, rechtswidrige Haupttat eines anderen", 270, 350, "s1a", "Bold", 36, rechts=1800),
    *neinz("schuldhaft? nicht nötig", 420, "akz", "Bold", 34, x=345, rechts=1800),
    *w29,
    pl("= limitierte Akzessorietät", 330, w29_y + 30, "lim", fill=GELB, size=36),
])
assert w29_y + 110 <= 960, w29_y

# ===========================================================================================================================
# E1 Prüfschema I. 1. b): Hilfeleisten – physisch, psychisch, Zeitpunkt
# ===========================================================================================================================
PH = "Prüfschema › I. 1. b) Hilfeleisten"
folie([("s1b", PH), ("phys", f"{PH} › physisch"), ("psych", f"{PH} › psychisch"), ("zeit", f"{PH} › schon in der Vorbereitung")],
      rechts_frei([
    *tafel("s1b", "I. 1. b) Hilfeleisten"),
    blk(110, 190, 1040, 120, GELB, "phys", [("physisch", "ExtraBold", 34, INK), ("z. B. ein Tatmittel wie ein Auto", "Bold", 30, INK)]),
    blk(110, 350, 1040, 120, BLAU, "psych", [("psychisch", "ExtraBold", 34, INK),
                                             ("Rat oder Bestärken des Tatentschlusses", "Bold", 30, INK)]),
    *okz("schon im Vorbereitungsstadium möglich", 530, "zeit", "Bold", 34, x=170),
    zit("BGH, Beschl. v. 21.4.2020 – 4 StR 287/19, Rn. 15", 170, 585, "zeit"),
    zit("BGH, Beschl. v. 20.9.2016 – 3 StR 49/16, Rn. 18 (psychische Beihilfe)", 170, 625, "zeit"),
    *requisit([("s1b", (FE, "handshake", 110, GELB), "Hilfe", GELB),
               ("phys", (FE, "automobile", 170, ROT), "physisch", GELB),
               ("psych", (FE, "light-bulb", 90, GELB), "psychisch", BLAU),
               ("zeit", (FE, "spiral-calendar", 100, WEISS), "Vorbereitung", WEISS)]),
    *zwei([("s1b", "ruhig"), ("phys", "denkt"), ("zeit", "ernst")], [("s1b", "ruhig"), ("psych", "denkt")]),
]))

# ===========================================================================================================================
# E2 Meinungsstand: Förderungsformel (BGH) – Kausalität (h. L.)
# ===========================================================================================================================
PM = "Prüfschema › I. 1. b) Wie stark muss die Hilfe wirken?"
folie([("streit", PM), ("bgh1", f"{PM} › BGH: Förderungsformel"), ("bgh2", f"{PM} › BGH: Kausalität nicht nötig"),
       ("lehre", f"{PM} › h. L.: Kausalität"), ("arg", f"{PM} › Argument der h. L."), ("meist", f"{PM} › meist gleiches Ergebnis")],
      rechts_frei([
    *tafel("streit", "Wie stark muss die Hilfe wirken?"),
    blk(110, 180, 1040, 76, BLAU, "bgh1", [("Rspr. (BGH): Förderungsformel", "ExtraBold", 34, INK)]),
    *okz("Tat gefördert oder erleichtert", 275, beim("bgh1", "fördert"), "Bold", 32, x=170),
    *neinz("ursächlich für den Erfolg? nicht nötig", 325, "bgh2", "Bold", 32, x=170),
    zit("BGH 4 StR 287/19, Rn. 15 · 3 StR 322/19, Rn. 8 · BGHSt 46, 107 (HRRS-Rn. 6)", 170, 375, "bgh2"),
    blk(110, 440, 1040, 76, LILA, "lehre", [("h. L.: Hilfe muss im Erfolg wirken (Kausalität)", "ExtraBold", 32, INK)]),
    z("Tat in konkreter Gestalt ermöglicht,", 170, 535, "lehre2", "Bold", 32),
    z("erleichtert oder abgesichert", 170, 580, beim("lehre2", "erleichtert"), "Bold", 32),
    z("Argument: sonst wird straflose versuchte Beihilfe", 170, 645, "arg", "Regular", 30),
    z("zur vollendeten", 170, 688, beim("arg", "vollendete"), "Regular", 30),
    zit("Lehre: nach Hefendehl, Vorlesung StGB AT, Uni Freiburg, KK 822 f.", 170, 735, beim("arg", "vollendete")),
    pl("meist gleiches Ergebnis", 110, 790, "meist", fill=GRUEN, size=34),
    *requisit([("streit", (FE, "balance-scale", 110, WEISS), "Streit", PINK),
               ("bgh1", (FE, "classical-building", 110, BLAU), "BGH", BLAU),
               ("lehre", (FE, "link", 100, LILA), "Kausalität", LILA),
               ("meist", (FE, "handshake", 110, GRUEN), "meist gleich", GRUEN)]),
    *zwei([("streit", "denkt"), ("bgh1", "liest"), ("meist", "ruhig")], [("streit", "denkt"), ("lehre", "ernst"), ("meist", "ruhig")]),
]))

# ===========================================================================================================================
# F Prüfschema I. 2.: doppelter Gehilfenvorsatz
# ===========================================================================================================================
PV = "Prüfschema › I. 2. doppelter Gehilfenvorsatz"
folie([("s2", PV), ("v1", f"{PV} › Vorsatz 1: Haupttat"), ("v1b", f"{PV} › wesentliche Merkmale"),
       ("v1c", f"{PV} › keine Einzelheiten"), ("v2", f"{PV} › Vorsatz 2: eigene Hilfe")], rechts_frei([
    *tafel("s2", "I. 2. doppelter Gehilfenvorsatz"),
    blk(110, 180, 1040, 76, GELB, "v1", [("Vorsatz 1: die Haupttat", "ExtraBold", 34, INK)]),
    *okz("in ihren wesentlichen Merkmalen:", 275, "v1b", "Bold", 32, x=170),
    z("Unrechtsgehalt und Angriffsrichtung", 170, 320, beim("v1b", "Unrechtsgehalt"), "ExtraBold", 32),
    *neinz("Einzelheiten der Tat: nicht nötig", 380, "v1c", "Bold", 32, x=170),
    zit("BGH, Urt. v. 31.10.2019 – 3 StR 322/19, Rn. 10", 170, 430, "v1c"),
    zit("BGH, Beschl. v. 7.2.2017 – 3 StR 430/16, Rn. 11", 170, 468, "v1c"),
    blk(110, 540, 1040, 76, GRUEN, "v2", [("Vorsatz 2: die eigene Hilfe", "ExtraBold", 34, INK)]),
    *okz("weiß: Hilfe kann die Tat fördern", 635, beim("v2", "Er"), "Bold", 32, x=170),
    *requisit([("s2", (FE, "brain", 110, PINK), "2 × Vorsatz", PINK),
               ("v1", (FE, "house", 110, GELB), "Haupttat", GELB),
               ("v1c", (FE, "white-question-mark", 80, WEISS), "Einzelheiten: nicht nötig", WEISS),
               ("v2", (FE, "handshake", 110, GRUEN), "eigene Hilfe", GRUEN)]),
    *zwei([("s2", "ruhig"), ("v1b", "denkt"), ("v2", "liest")], [("s2", "ruhig"), ("v1c", "denkt"), ("v2", "ernst")]),
]))

# ===========================================================================================================================
# G Prüfschema komplett: II. Rechtswidrigkeit, III. Schuld, Strafe
# ===========================================================================================================================
REIHEN_A = [(0, "I. Tatbestand"), (1, "1. objektiv: a) vorsätzliche, rechtswidrige Haupttat (limitierte Akzessorietät)"),
            (2, "b) Hilfeleisten: physisch oder psychisch (BGH: Förderung genügt; h. L.: Kausalität)"),
            (1, "2. subjektiv: doppelter Gehilfenvorsatz (Haupttat in wesentlichen Merkmalen; eigene Hilfe)")]
els_g = [karte(60, 50, 1800, 940, "s_ii"), titel(glyphen("Prüfschema: Beihilfe, § 27 StGB"), 110, 90, "s_ii", 46)]
y = 200
for ebene, text in REIHEN_A:
    x = (130, 200, 300)[ebene]
    els_g.append(z(text, x, y, "s_ii", ("ExtraBold", "Bold", "Bold")[ebene], (40, 32, 32)[ebene], rechts=1820,
                   farbe=(INK, TEXT, TEXT)[ebene]))
    y += 80
els_g += [z("II. Rechtswidrigkeit", 130, y + 10, beim("s_ii", "Rechtswidrigkeit"), "ExtraBold", 40, rechts=1820),
          z("III. Schuld", 130, y + 100, beim("s_iii", "Schuld"), "ExtraBold", 40, rechts=1820),
          blk(130, y + 200, 1660, 80, GELB, "strafe", [("Strafe: § 27 Abs. 2 StGB – Milderung nach § 49 Abs. 1 zwingend",
                                                        "ExtraBold", 36, INK)])]
assert y + 290 <= 960, y
folie([("s_ii", "Prüfschema › II. Rechtswidrigkeit"), ("s_iii", "Prüfschema › III. Schuld"),
       ("strafe", "Prüfschema › Strafe: § 27 Abs. 2 StGB")], els_g)

# ===========================================================================================================================
# H1 Lösung: Haupttat von Falko, keine Mittäterschaft von Hedda
# ===========================================================================================================================
PL = "Lösung › Hedda"
folie([("loes", "Lösung · Der Fall"), ("h1", f"{PL} › 1. a) Haupttat von Falko"),
       ("h2", f"{PL} › 1. a) schwerer Wohnungseinbruchdiebstahl"), ("h2b", f"{PL} › 1. a) dauerhaft genutzte Privatwohnung"),
       ("h3", f"{PL} › 1. a) vorsätzlich und rechtswidrig"), ("mitt", f"{PL} › zuerst: Mittäterin? nein")], rechts_frei([
    *tafel("loes", "Lösung: Hat sich Hedda strafbar gemacht?"),
    z("a) Haupttat von Falko", 110, 180, "h1", "ExtraBold", 34),
    *okz("bricht in ein bewohntes Haus ein und stiehlt", 235, beim("h1", "bricht"), "Bold", 32, x=170),
    blk(110, 300, 1040, 120, GELB, "h2", [("schwerer Wohnungseinbruchdiebstahl", "ExtraBold", 34, INK),
                                         ("§§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4 StGB", "Bold", 30, INK)]),
    *okz("dauerhaft genutzte Privatwohnung", 445, "h2b", "Bold", 32, x=170),
    zit("BGH, Urt. v. 24.6.2020 – 5 StR 671/19, Rn. 10, 13, 37", 170, 492, "h2b"),
    *okz("vorsätzlich und rechtswidrig", 545, "h3", "Bold", 32, x=170),
    *neinz("Hedda Mittäterin? kein Beuteinteresse,", 630, "mitt", "Bold", 32, x=170),
    z("kein Einfluss auf Ob und Wie der Tat", 170, 675, beim("mitt", "Einfluss"), "Bold", 32),
    pl("mehr: Folge zur Mittäterschaft", 170, 740, beim("mitt", "Mehr"), fill=WEISS, size=28),
    *requisit([("loes", (FE, "house", 110, GELB), "Lösung", WEISS),
               ("h1", (FE, "unlocked", 90, GELB), "Einbruch", HELLROT),
               ("h2b", (FE, "house-with-garden", 150, GELB), "bewohnt", GELB),
               ("mitt", (FE, "gem-stone", 90, BLAU), "Beute? nein", HELLGRAU)]),
    *zwei([("loes", "ruhig"), ("h1", "liest"), ("mitt", "ernst")], [("loes", "ruhig"), ("h1", "still"), ("h3", "ernst")]),
]))

# ===========================================================================================================================
# H2 Lösung: Hilfeleisten
# ===========================================================================================================================
folie([("hl", f"{PL} › 1. b) Hilfeleisten: das Auto"), ("hl2", f"{PL} › 1. b) BGH: erleichtert"),
       ("hl3", f"{PL} › 1. b) h. L.: im Erfolg ausgewirkt"), ("hl4", f"{PL} › 1. b) Streitentscheid entbehrlich")], rechts_frei([
    *tafel("hl", "Lösung: b) Hilfeleisten"),
    z("Auto: Fahrt zum Haus und Abtransport der Beute", 110, 185, "hl", "ExtraBold", 32),
    *okz("BGH: erleichtert die Tat – genügt", 270, "hl2", "Bold", 34, x=170),
    *okz("h. L.: hat sich im Erfolg ausgewirkt", 345, "hl3", "Bold", 34, x=170),
    z("(Tat lief genau so mit dem Auto ab)", 170, 395, beim("hl3", "Tat"), "Regular", 30, farbe=TEXT),
    blk(110, 470, 1040, 120, GRUEN, "hl4", [("beide Ansichten: Hilfeleisten (+)", "ExtraBold", 34, INK),
                                           ("Streitentscheid entbehrlich", "Bold", 30, INK)]),
    *requisit([("hl", (FE, "automobile", 190, ROT), "Fahrt und Abtransport", WEISS),
               ("hl2", (FE, "classical-building", 110, BLAU), "BGH (+)", BLAU),
               ("hl3", (FE, "link", 100, LILA), "h. L. (+)", LILA),
               ("hl4", (FE, "handshake", 110, GRUEN), "gleiches Ergebnis", GRUEN)]),
    *zwei([("hl", "ernst"), ("hl3", "liest")], [("hl", "still"), ("hl4", "ernst")]),
]))

# ===========================================================================================================================
# H3 Lösung: Vorsatz, Rechtswidrigkeit, Schuld
# ===========================================================================================================================
folie([("vs", f"{PL} › 2. Vorsatz: Haupttat"), ("vs2", f"{PL} › 2. welches Haus: nur eine Einzelheit"),
       ("vs3", f"{PL} › 2. Vorsatz: eigene Hilfe"), ("vs4", f"{PL} › 2. Missbilligung unerheblich"),
       ("rws", f"{PL} › II. Rechtswidrigkeit, III. Schuld")], rechts_frei([
    *tafel("vs", "Lösung: 2. Vorsatz von Hedda"),
    *okz("kennt: Einbruch in ein bewohntes Haus, Diebstahl", 185, "vs", "Bold", 32, x=170),
    *okz("welches Haus? nur eine Einzelheit", 250, "vs2", "Bold", 32, x=170),
    *okz("weiß: ihr Auto hilft dabei", 315, "vs3", "Bold", 32, x=170),
    *okz("findet die Tat falsch: ändert nichts", 380, "vs4", "Bold", 32, x=170),
    zit("BGH, Urt. v. 1.8.2000 – 5 StR 624/99, BGHSt 46, 107 (HRRS-Rn. 6)", 170, 428, "vs4"),
    *okz("II. Rechtswidrigkeit (+)  III. Schuld (+)", 500, "rws", "ExtraBold", 32, x=170),
    *requisit([("vs", (FE, "house", 110, GELB), "Haupttat bekannt", GELB),
               ("vs2", (FE, "white-question-mark", 80, WEISS), "welches Haus?", WEISS),
               ("vs3", (FE, "key", 90, GELB), "ihr Auto hilft", WEISS),
               ("vs4", (FE, "thinking-face", 100, GELB), "Missbilligung: unerheblich", WEISS),
               ("rws", (FE, "balance-scale", 110, WEISS), "II. und III. (+)", GRUEN)]),
    *zwei([("vs", "liest"), ("vs4", "sorge"), ("rws", "ernst")], [("vs", "still"), ("vs3", "ernst")]),
]))

# ===========================================================================================================================
# H4 Ergebnis und Strafrahmen
# ===========================================================================================================================
folie([("erg", "Ergebnis · Hedda: Beihilfe"), ("rahmen", "Ergebnis · Strafrahmen gemildert, § 49 Abs. 1")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 160, GRUEN, "erg", [("Hedda: Beihilfe zum schweren", "ExtraBold", 36, INK),
                                           ("Wohnungseinbruchdiebstahl", "ExtraBold", 36, INK),
                                           ("§§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4, 27 StGB", "Bold", 30, INK)]),
    z("Strafrahmen:", 110, 390, "rahmen", "ExtraBold", 34),
    z("Täter (§ 244 Abs. 4): 1 bis 10 Jahre", 170, 450, beim("rahmen", "statt"), "Bold", 34),
    blk(110, 520, 1040, 120, GELB, beim("rahmen", "drei"), [("Gehilfin: 3 Monate bis 7 Jahre 6 Monate", "ExtraBold", 34, INK),
                                                          ("§ 27 Abs. 2 S. 2, § 49 Abs. 1 Nr. 2, 3 StGB", "Bold", 30, INK)]),
    *requisit([("erg", (FE, "balance-scale", 110, GRUEN), "Beihilfe", GRUEN),
               ("rahmen", (FE, "balance-scale", 110, GELB), "gemildert", GELB)]),
    *zwei([("erg", "ernst")], [("erg", "still")]),
]))

# ===========================================================================================================================
# I1 Sonderfall: sukzessive Beihilfe
# ===========================================================================================================================
PS2 = "Sonderfälle"
folie([("sf", f"{PS2} · in Kürze"), ("sukz", f"{PS2} › 1. sukzessive Beihilfe"), ("sukz2", f"{PS2} › 1. Teile der Lehre")],
      rechts_frei([
    *tafel("sf", "Drei Sonderfälle"),
    blk(110, 180, 1040, 76, WEISS, "sukz", [("1. sukzessive Beihilfe", "ExtraBold", 34, INK)]),
    *okz("BGH: auch nach Vollendung bis zur Beendigung,", 275, beim("sukz", "Nach"), "Bold", 32, x=170),
    z("z. B. beim Abtransport der Beute", 170, 320, beim("sukz", "etwa"), "Bold", 32),
    zit("BGH 4 StR 287/19, Rn. 15 · 3 StR 49/16, Rn. 18", 170, 370, beim("sukz", "etwa")),
    z("Teile der Lehre: nur bis zur Vollendung", 170, 440, "sukz2", "Bold", 32),
    zit("nach Hefendehl, Vorlesung StGB AT, Uni Freiburg, KK 831 f.", 170, 488, "sukz2"),
    *requisit([("sf", (FE, "white-question-mark", 80, WEISS), "3 Sonderfälle", WEISS),
               ("sukz", (FE, "package", 110, HOLZ), "Abtransport", WEISS),
               ("sukz2", (FE, "stopwatch", 100, WEISS), "bis wann?", PINK)]),
    *zwei([("sf", "ruhig"), ("sukz", "denkt")], [("sf", "ruhig"), ("sukz2", "denkt")]),
]))

# ===========================================================================================================================
# I2 Sonderfälle: neutrale Handlungen (Taxifahrt), Unterlassen
# ===========================================================================================================================
folie([("taxi", f"{PS2} › 2. neutrale Handlungen: die Taxifahrt"), ("taxi2", f"{PS2} › 2. sicheres Wissen: Beihilfe"),
       ("taxi3", f"{PS2} › 2. nur für möglich gehalten"), ("taxi4", f"{PS2} › 2. erkennbar tatgeneigter Täter"),
       ("unterl", f"{PS2} › 3. Beihilfe durch Unterlassen")], rechts_frei([
    *tafel("taxi", "Drei Sonderfälle"),
    blk(110, 180, 1040, 76, WEISS, "taxi", [("2. neutrale Handlungen: die Taxifahrt", "ExtraBold", 34, INK)]),
    *okz("Fahrer weiß sicher vom Einbruch: Beihilfe", 275, "taxi2", "Bold", 32, x=170),
    *neinz("hält es nur für möglich: regelmäßig nicht", 335, "taxi3", "Bold", 32, x=170),
    z("außer: Förderung eines erkennbar tatgeneigten", 170, 395, "taxi4", "Bold", 32),
    z("Täters „angelegen sein lassen“", 170, 440, beim("taxi4", "erkennbar"), "Bold", 32),
    zit("BGHSt 46, 107 (HRRS-Rn. 14) · BGH 5 StR 468/12, Rn. 26", 170, 490, "taxi4"),
    blk(110, 570, 1040, 120, WEISS, "unterl", [("3. Beihilfe durch Unterlassen", "ExtraBold", 34, INK),
                                              ("nur mit Garantenstellung, § 13 StGB", "Bold", 30, INK)]),
    *requisit([("taxi", (FE, "taxi", 170, GELB), "Taxifahrt", GELB),
               ("taxi2", (FE, "house", 110, GELB), "weiß: Einbruch", HELLROT),
               ("taxi3", (FE, "white-question-mark", 80, WEISS), "nur möglich", WEISS),
               ("unterl", (FE, "shield", 100, BLAU), "Garant?", BLAU)]),
    *zwei([("taxi", "ruhig"), ("taxi3", "denkt"), ("unterl", "liest")], [("taxi", "ruhig"), ("taxi2", "ernst"), ("unterl", "denkt")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Täterschaft vor Teilnahme", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("erst den Täter, dann den Teilnehmer prüfen", 200, 200, "tipp", "Bold", 32),
         blk(130, 300, 1020, 120, GELB, "tipp2", [("Ist der Beteiligte selbst Täter?", "ExtraBold", 32, INK),
                                                  ("Erst wenn nicht: Beihilfe", "ExtraBold", 32, INK)]),
         blk(130, 460, 1020, 160, HELLROT, "tipp3", [("Obersatz mit genauer Haupttat:", "ExtraBold", 32, INK),
                                                     ("Beihilfe zum schweren Wohnungs-", "Bold", 30, INK),
                                                     ("einbruchdiebstahl, nicht bloß zum Diebstahl", "Bold", 30, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · erst Täter, dann Teilnehmer"), ("tipp2", "Klausurtipp › Täterschaft zuerst"),
       ("tipp3", "Klausurtipp › Haupttat genau benennen")], els_k)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Hilfe leistet, wer eine fremde vorsätzliche,", 0)],
                 [("rechtswidrige Tat ", 0), ("fördert", "a"), (".", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "fördert")}),
    *markertext([[("Strafbar wird das mit ", 0), ("doppeltem Vorsatz", "b"), (":", 0)]], 750, 470, 42, "mk2",
                {"b": beim("mk2", "doppeltem")}),
    *markertext([[("Der Gehilfe kennt die Haupttat in ihren", 0)], [("wesentlichen Merkmalen", "c"), (" und weiß,", 0)],
                 [("dass er ", 0), ("hilft", "d"), (".", 0)]], 750, 580, 42, "mk3",
                {"c": beim("mk3", "wesentlichen"), "d": beim("mk3", "hilft")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
