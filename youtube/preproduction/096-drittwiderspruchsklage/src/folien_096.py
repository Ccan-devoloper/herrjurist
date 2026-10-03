"""Folge 096 · Drittwiderspruchsklage § 771 ZPO: Wenn fremde Sachen gepfändet werden – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Ölgemälde der Großmutter, beim Enkel zur Aufbewahrung, gepfändet für seine Schulden), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Wohnung von Frau Wendland (Renovierung, Übergabe, Zettel), B Fahrradladen (Schulden, Urteil,
Auftrag), C Wohnung von Herrn Vollmer (Pfändung, Großmutter, Frage), D Sachverhalt, E Statthaftigkeit (Wortlaut § 771 I),
F Abgrenzung §§ 766, 805, G Zuständigkeit und Parteien, H Rechtsschutzbedürfnis, I Begründetheit: Eigentum, J Beweislast
(Wortlaut § 1006 I 1, III BGB), K Einwendungen, L Tenor, M Klausurtipp (Lexi), N Eilantrag (Wortlaut § 769 I),
O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Stift auf dem Zettel (A), Türklingel (C); Freesound CC0. Hilfsfunktionen wie Folge 093."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_096/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HOLZ = (214, 160, 110, 255)
HOLZHELL = (232, 190, 145, 255)
GOLD = (233, 190, 96, 255)
HIMMEL = (196, 222, 246, 255)
DUNKEL = (58, 58, 72, 255)
ROTHELL = (253, 232, 228, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf; Mindestschrift 26 px (mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def zz(kopf, rest, x, y, c_kopf, c_rest, stil="Bold", size=34, rest_stil=None, **k):
    """Zeile in zwei Teilen: erster Teil zur Marke, Rest erst zum gesprochenen Wort (nie vor dem Wort)."""
    a = z(kopf, x, y, c_kopf, stil, size, **k)
    dx = F(stil, size).getlength(kopf + " ")
    return [a, z(rest, x + dx, y, c_rest, rest_stil or stil, size, **k)]


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26, rechts=1170):
    """Fundstellenzeile (grau, klein, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, rechts=rechts)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_096/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe; feste
    Zeilen ergeben zusammen genau den Text. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen
    Textmarker hinter die Wortgruppe (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    assert " ".join(t.strip() for t in zeilen) == text, "feste Zeilen weichen vom Normtext ab"
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} steht nicht in einer Zeile: {zeilen}"
        t = zeilen[zi]; a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", 26, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 093/074): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
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


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


def gemaelde(cx, oben, w, cue, bis=None, anim="pop", d=0.0):
    """Das Ölgemälde: Goldrahmen (Tafelbaustein) mit Leinwand, darauf ein Leuchtturm am Meer (Tabler „building-lighthouse“,
    weiß gefüllt). Kein eigenes Gemälde-Icon in den Bibliotheken; Rahmen und Leinwand sind Kartenbausteine."""
    h = int(w * 0.8)
    els = [bis_(karte(int(cx - w / 2), oben, w, h, cue, fill=GOLD, rund=6, schatten=5, rand=5, anim=anim, d=d), bis),
           bis_(karte(int(cx - w * 0.38), int(oben + h * 0.12), int(w * 0.76), int(h * 0.76), cue, fill=HIMMEL, rund=4,
                      schatten=0, rand=3, anim=anim, d=d), bis),
           ficon("tabler", "building-lighthouse", cx, int(oben + h * 0.84), int(w * 0.36), cue, fuell=WEISS, anim=anim, d=d, bis=bis)]
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
X1, X2 = 1390, 1730                         # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WE_F, VO_F, GV_F, GE_F = BLAU, GRUEN, TUERKIS, GELB   # Farben der Namensschilder
ZA = "A. Zulässigkeit"
BE = "B. Begründetheit"

# A Fall: das Gemälde der Großmutter ---------------------------------------------------------------------------------------
WX, VX = 560, 1520
WEa = ("WE_redet_r", WX, BODEN, FH)
ENKEL = beim("bild", "Enkel")
folie([(NULL, "Fall · Das Gemälde der Großmutter"), ("zettel", "Fall · Der Zettel")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Wohnung von Frau Wendland", 70, 40, NULL, fill=BLAU, size=40)),
    ficon("tabler", "ladder", 200, BODEN - 2, 230, NULL, fuell=HOLZHELL, anim="cut"),
    ficon("tabler", "bucket", 330, BODEN - 2, 100, NULL, fuell=WEISS, anim="cut"),
    hart(pl("Renovierung", 200, 600, NULL, fill=WEISS, size=30, anker="m")),
    *fig("WE", WX, BODEN, FH, [(NULL, "ruhig_r"), ("bild", "froh_r")], bis="w1", erst="cut"),
    *redet("WE_redet_r", WX, BODEN, FH, "w1", "schuld"),
    hart(schild("Frau Wendland", WX, NULL, WE_F, unten=BODEN, d=0.0)),
    *gemaelde(1020, 430, 250, beim("bild", "Ölgemälde")),
    pl("Ölgemälde", 1020, 360, beim("bild", "Ölgemälde"), fill=GELB, size=32, anker="m"),
    pl("nur zur Aufbewahrung", 1020, 670, beim("bild", "aufbewahren"), fill=WEISS, size=30, anker="m"),
    *fig("VO", VX, BODEN, FH, [(ENKEL, "ruhig"), ("zettel", "froh"), ("w1", "ruhig")]),
    schild("Herr Vollmer, Student", VX, ENKEL, VO_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "note", 1020, 820, 80, "zettel", fuell=WEISS), "096stift*", 0.8, 0.1),
    pl("Zettel: Das Bild gehört Frau Wendland.", 1400, 290, beim("zettel", "Bild"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 700, 190, "w1", 540, 235, inhalt=["Pass gut darauf auf. Nach der",
                                                     "Renovierung hole ich es wieder ab."], textsize=30, figur=WEa, bis="schuld"),
])

# B Fall: die Schulden beim Fahrradhändler --------------------------------------------------------------------------------------
GEX, VXb = 640, 1520
folie([("schuld", "Fall · Die Schulden"), ("titel", "Fall · Urteil und Vollstreckungsauftrag")], [
    linienzug([(60, BODEN), (1860, BODEN)], "schuld", breite=7, farbe=INK),
    pl("Fahrradladen Gebhardt", 70, 40, "schuld", fill=GELB, size=40),
    ficon("tabler", "bike", 180, BODEN - 2, 200, "schuld", fuell=WEISS),
    ficon("tabler", "bike", 420, BODEN - 2, 190, "schuld", fuell=WEISS),
    *fig("GE", GEX, BODEN, FH, [(beim("schuld", "Gebhardt"), "ruhig_r"), ("titel", "ernst_r")]),
    schild("Herr Gebhardt, Fahrradhändler", GEX, beim("schuld", "Gebhardt"), GE_F, unten=BODEN),
    *fig("VO", VXb, BODEN, FH, [("schuld", "sorge"), ("gv", "denkt")]),
    schild("Herr Vollmer", VXb, "schuld", VO_F, unten=BODEN),
    ficon("tabler", "cash-banknote", 1080, 560, 110, beim("schuld", "tausendachthundert"), fuell=GRUEN),
    pl("Schulden: 1.800 €", 1080, 600, beim("schuld", "tausendachthundert"), fill=WEISS, size=32, anker="m"),
    ficon("tabler", "file-certificate", 1080, 330, 100, beim("titel", "Urteil"), fuell=WEISS),
    pl("rechtskräftiges Urteil des Amtsgerichts", 1080, 150, beim("titel", "rechtskräftiges"), fill=BLAU, size=30, anker="m"),
    pl("Auftrag an die Gerichtsvollzieherin", 1080, 690, beim("gv", "beauftragt"), fill=PINK, size=30, anker="m"),
])

# C Fall: die Pfändung in der Wohnung von Herrn Vollmer ----------------------------------------------------------------------------
VXc, GXc = 760, 1590
TX = 1160                                    # Wohnungstür (Rahmen links bei TX)
VOc = ("VO_redet_r", VXc, BODEN, FH)
GVc = ("GV_redet", GXc, BODEN, FH)
WEc = ("WE_redetstreng", GXc, BODEN, FH)
KOMMT_GV = beim("klingel", "klingelt")
KOMMT_WE = "oma"
folie([("klingel", "Fall · Die Pfändung"), ("oma", "Fall · Die Großmutter"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "klingel", breite=7, farbe=INK)),
    hart(pl("Wohnung von Herrn Vollmer", 70, 40, "klingel", fill=GRUEN, size=40)),
    *[hart(e) for e in gemaelde(330, 300, 250, "klingel")],
    ficon("tabler", "desk", 330, BODEN - 2, 300, "klingel", fuell=HOLZ, anim="cut"),
    ficon("tabler", "books", 330, 712, 90, "klingel", fuell=WEISS, anim="cut"),
    hart(karte(TX, 370, 250, BODEN - 370, "klingel", fill=HOLZ, rund=8, schatten=5)),
    hart(karte(TX + 20, 390, 210, BODEN - 390, "klingel", fill=HOLZHELL, rund=6, schatten=0, rand=4)),
    hart(karte(TX + 26, 610, 18, 50, "klingel", fill=DUNKEL, rund=6, schatten=0, rand=3)),
    szene(ficon("tabler", "bell-ringing", TX + 125, 360, 70, KOMMT_GV, fuell=GELB, bis="g1"), "096klingel*", 0.8, 0.0),
    *fig("VO", VXc, BODEN, FH, [("klingel", "ruhig_r"), ("g1", "schreck_r")], bis="v1", erst="cut"),
    *redet("VO_redet_r", VXc, BODEN, FH, "v1", "g2"),
    *fig("VO", VXc, BODEN, FH, [("g2", "sorge_r"), ("oma", "ruhig_r"), ("w2", "froh_r"), ("frage", "denkt_r")], erst="cut"),
    hart(schild("Herr Vollmer", VXc, "klingel", VO_F, unten=BODEN, d=0.0)),
    *fig("GV", GXc, BODEN, FH, [(KOMMT_GV, "ruhig")], bis="g1"),
    *redet("GV_redet", GXc, BODEN, FH, "g1", "v1"),
    peep_voll("GV_ruhig", GXc, BODEN, FH, "v1", anim="cut", bis="g2"),
    *redet("GV_redet", GXc, BODEN, FH, "g2", "versteig"),
    peep_voll("GV_ruhig", GXc, BODEN, FH, "versteig", anim="cut", bis="oma"),
    schild("Gerichtsvollzieherin", GXc, KOMMT_GV, GV_F, unten=BODEN, d=0.0, bis="oma"),
    pl("gepfändet", 330, 230, beim("g1", "pfände"), fill=ROT, size=32, anker="m"),
    blase("sprech", 740, 160, "g1", 1180, 235, inhalt=["Das Gemälde an der Wand pfände ich."], textsize=32, figur=GVc, bis="v1"),
    blase("sprech", 760, 190, "v1", 900, 235, inhalt=["Das gehört meiner Oma! Ich", "bewahre es nur für sie auf."],
          textsize=32, figur=VOc, bis="g2"),
    blase("sprech", 720, 190, "g2", 1190, 235, inhalt=["Es ist in Ihrer Wohnung.", "Wem es gehört, prüfe ich nicht."],
          textsize=32, figur=GVc, bis="versteig"),
    ficon("tabler", "calendar-event", 1000, 330, 90, beim("versteig", "Versteigerung"), fuell=WEISS, bis="w2"),
    pl("Versteigerung in 3 Wochen", 1000, 150, beim("versteig", "Versteigerung"), fill=PINK, size=30, anker="m", bis="w2"),
    *fig("WE", GXc, BODEN, FH, [(KOMMT_WE, "sorge")], bis="w2"),
    *redet("WE_redetstreng", GXc, BODEN, FH, "w2", "frage"),
    *fig("WE", GXc, BODEN, FH, [("frage", "entschlossen")], erst="cut"),
    schild("Frau Wendland", GXc, KOMMT_WE, WE_F, unten=BODEN, d=0.0),
    blase("sprech", 720, 190, "w2", 1190, 235, inhalt=["Das Bild gehört mir. Das", "lasse ich nicht versteigern!"],
          textsize=32, figur=WEc, bis="frage"),
    pl("Wie wehrt sich Frau Wendland?", 1180, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Und wie stoppt sie die Versteigerung rechtzeitig?", 1180, 240, "frage2", fill=WEISS, size=34, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Frau Wendland lässt ihre Wohnung renovieren. So lange gibt sie ihr Ölgemälde ihrem Enkel, dem Studenten "
            "Herrn Vollmer, nur zur Aufbewahrung. Auf einem Zettel, den beide unterschreiben, halten sie fest: Das Bild "
            "gehört Frau Wendland."),
    glyphen("Herr Vollmer schuldet dem Fahrradhändler Herrn Gebhardt 1.800 €. Aus einem rechtskräftigen Urteil des "
            "Amtsgerichts lässt Herr Gebhardt vollstrecken. Die Gerichtsvollzieherin pfändet das Gemälde in der Wohnung "
            "von Herrn Vollmer; die Versteigerung soll in 3 Wochen stattfinden."),
    glyphen("Frau Wendland schuldet Herrn Gebhardt nichts. Annahme: Der Zettel ist echt; das Gemälde ist mehr wert als 1.800 €."),
], "Wie wehrt sich Frau Wendland – und wie rechtzeitig?")

# E A. Zulässigkeit: 1. Statthaftigkeit, Wortlaut § 771 Abs. 1 ZPO ------------------------------------------------------------------
W771 = ("„Behauptet ein Dritter, dass ihm an dem Gegenstand der Zwangsvollstreckung ein die Veräußerung hinderndes Recht "
        "zustehe, so ist der Widerspruch gegen die Zwangsvollstreckung im Wege der Klage bei dem Gericht geltend zu machen, "
        "in dessen Bezirk die Zwangsvollstreckung erfolgt.“")
Z771 = ["„Behauptet ein Dritter, dass ihm an dem Gegenstand der",
        "Zwangsvollstreckung ein die Veräußerung hinderndes Recht",
        "zustehe, so ist der Widerspruch gegen die Zwangsvollstreckung",
        "im Wege der Klage bei dem Gericht geltend zu machen,",
        "in dessen Bezirk die Zwangsvollstreckung erfolgt.“"]
w771, w771_y = wortlaut(90, 225, 1080, W771, "§ 771 Abs. 1 ZPO", "wl771", size=32, zeilen=Z771,
                        marken=[("Dritter", beim("wl771", "Dritter")),
                                ("die Veräußerung hinderndes Recht", beim("wl771", "Veräußerung")),
                                ("im Wege der Klage", beim("wl771", "Klage")),
                                ("in dessen Bezirk", beim("wl771", "Bezirk"))])
folie([("zul", ZA), ("statt", f"{ZA} › 1. Statthaftigkeit"), ("wl771", f"{ZA} › 1. Statthaftigkeit, § 771 Abs. 1 ZPO")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("1. Statthaftigkeit", 110, 165, "statt", "Bold", 36),
    *w771,
    z("Frau Wendland: nicht Schuldnerin, sondern Dritte", 110, w771_y + 25, beim("dritt", "Frau"), "Bold", 34),
    z("behauptet ihr Eigentum am Gemälde", 150, w771_y + 80, beim("dritt", "behauptet"), size=34),
    blk(110, w771_y + 140, 1040, 70, GRUEN, beim("dritt", "Drittwiderspruchsklage"),
        [("Drittwiderspruchsklage statthaft", "ExtraBold", 36, INK)]),
    ok(1100, w771_y + 175, beim("dritt", "statthaft"), gr=22),
    *gemaelde(IX, 160, 190, "zul"),
    *fig("WE", FX, FB, FR, [("zul", "ruhig"), ("dritt", "entschlossen"), (beim("dritt", "statthaft"), "froh")]),
    schild("Frau Wendland", FX, "zul", WE_F),
]))

# F Abgrenzung: Erinnerung § 766, Klage auf vorzugsweise Befriedigung § 805 ---------------------------------------------------------
folie([("a766", f"{ZA} › 1. Statthaftigkeit › Abgrenzung")], rechts_frei([
    *tafel("a766", "Abgrenzung"),
    *zz("Erinnerung,", "§ 766 ZPO:", 110, 180, beim("a766", "Erinnerung"), beim("a766", "Paragraf"), size=36),
    z("nur Art und Weise der Vollstreckung", 150, 237, beim("a766", "Art"), size=34),
    z("hier: Gerichtsvollzieherin hat richtig gehandelt", 110, 320, beim("gew", "richtig"), "Bold", 34),
    ok(980, 342, beim("gew", "richtig"), gr=20),
    z("Sie prüft grundsätzlich nur den Gewahrsam", 150, 375, beim("gew", "prüft"), size=34),
    z("des Schuldners, nicht das Eigentum.", 150, 428, beim("gew", "Schuldners"), size=34),
    zit("§ 808 Abs. 1 ZPO; BGH, Urt. v. 5.7.2007 – III ZR 143/06, Rn. 9", 150, 480, beim("gew", "Eigentum")),
    z("ohne Besitz, nur Pfand- oder Vorzugsrecht:", 110, 560, beim("a805", "ohne"), "Bold", 34),
    *zz("§ 805 ZPO:", "Klage auf vorzugsweise Befriedigung", 150, 615, beim("a805", "Paragraf"),
        beim("a805", "vorzugsweise"), "Regular", 34),
    pl("Video: Rechtsbehelfe in der Zwangsvollstreckung", 110, 700, beim("verw", "Video"), fill=LILA, size=30),
    ficon("tabler", "list-check", IX, IU, 110, "a766", fuell=WEISS, bis="gew"),
    pl("§ 766: Art und Weise", IX, 200, beim("a766", "Art"), fill=BLAU, size=28, anker="m", bis="gew"),
    ficon("tabler", "home", IX, IU, 120, "gew", fuell=WEISS, anim="cut", bis="a805"),
    pl("Gewahrsam", IX, 200, beim("gew", "Gewahrsam"), fill=WEISS, size=28, anker="m", anim="cut", bis="a805"),
    ficon("tabler", "coin", IX, IU, 100, "a805", fuell=GELB, anim="cut"),
    pl("§ 805: Erlös", IX, 200, beim("a805", "Erlös"), fill=GELB, size=28, anker="m", anim="cut"),
    *fig("GV", FX, FB, FR, [("a766", "ruhig"), ("gew", "denkt"), ("a805", "ruhig")]),
    schild("Gerichtsvollzieherin", FX, "a766", GV_F),
]))

# G Zuständigkeit und Parteien ---------------------------------------------------------------------------------------------------
folie([("zust", f"{ZA} › 2. Zuständigkeit"), ("p802", f"{ZA} › 2. Zuständigkeit, § 802 ZPO"),
       ("sachl", f"{ZA} › 2. Zuständigkeit › sachlich: Streitwert"), ("bekl", f"{ZA} › Parteien, § 771 Abs. 2 ZPO")],
      rechts_frei([
    *tafel("zust", "2. Zuständigkeit"),
    z("örtlich: Gericht, in dessen Bezirk vollstreckt wird", 110, 170, beim("zust", "Örtlich"), "Bold", 34),
    z("ausschließlich, § 802 ZPO", 150, 222, beim("p802", "ausschließlich"), size=34),
    z("sachlich: nach dem Streitwert", 110, 290, beim("sachl", "Sachlich"), "Bold", 34),
    *zz("§ 6 ZPO:", "Betrag der Forderung, hier 1.800 €", 150, 342, beim("sachl", "Paragraf"), beim("sachl", "Betrag"),
        "Regular", 34),
    zit("BGH, Beschl. v. 7.2.2008 – IX ZR 69/05, Rn. 2", 150, 392, beim("sachl", "Forderung")),
    z("Sache weniger wert: ihr Wert (§ 6 Satz 2 ZPO)", 150, 432, beim("sachl", "weniger"), size=34),
    blk(110, 495, 1040, 70, BLAU, beim("ag", "Amtsgericht"), [("Amtsgericht am Wohnort von Herrn Vollmer", "ExtraBold", 34, INK)]),
    zit("bis 10.000 €: § 23 Nr. 1, § 71 Abs. 1 GVG", 150, 575, beim("ag", "Amtsgericht")),
    *zz("Beklagter:", "der Gläubiger, Herr Gebhardt", 110, 640, "bekl", beim("bekl", "Gläubiger"), "Bold", 34),
    z("auch gegen den Schuldner: Streitgenossen,", 150, 695, beim("bekl", "Klagt"), size=34),
    z("§ 771 Abs. 2 ZPO", 150, 745, beim("bekl", "Streitgenossen"), size=34),
    ficon("tabler", "map-pin", MB, 380, 100, "zust", fuell=PINK, bis="sachl"),
    pl("Ort der Vollstreckung", MB, 180, beim("zust", "Örtlich"), fill=WEISS, size=28, anker="m", bis="sachl"),
    ficon("tabler", "cash-banknote", MB, 380, 110, "sachl", fuell=GRUEN, anim="cut", bis="ag"),
    pl("Streitwert: 1.800 €", MB, 180, beim("sachl", "tausendachthundert"), fill=GRUEN, size=28, anker="m", anim="cut", bis="ag"),
    ficon("tabler", "building-bank", MB, 380, 120, "ag", fuell=BLAU, anim="cut"),
    pl("Amtsgericht", MB, 180, "ag", fill=BLAU, size=28, anker="m", anim="cut"),
    *fig("WE", X1, FB, FR, [("zust", "ruhig"), ("ag", "froh")]),
    schild("Frau Wendland", X1, "zust", WE_F),
    *fig("GE", X2, FB, FR, [("zust", "ruhig"), ("bekl", "ernst")], d=0.2),
    schild("Herr Gebhardt", X2, "zust", GE_F, d=0.3),
]))

# H Rechtsschutzbedürfnis ----------------------------------------------------------------------------------------------------------
ZB1, ZB2, ZJ = 230, 1010, 600                # Zeitstrahl: Beginn (Pfändung), Ende (Verwertung), jetzt
folie([("rsb", f"{ZA} › 3. Rechtsschutzbedürfnis"), ("rsb3", f"{ZA} › Ergebnis: zulässig")], rechts_frei([
    *tafel("rsb", "3. Rechtsschutzbedürfnis"),
    z("besteht ab Beginn der Vollstreckung", 110, 180, beim("rsb", "sobald"), "Bold", 34),
    z("und solange sie andauert", 150, 232, beim("rsb", "solange"), size=34),
    z("entfällt, wenn sie durch Verwertung beendet ist", 110, 300, beim("rsb2", "Verwertung"), size=34),
    hart(linienzug([(150, 440), (1130, 440)], beim("rsb", "sobald"), breite=6, farbe=INK)),
    hart(linienzug([(ZB1, 420), (ZB1, 460)], beim("rsb", "sobald"), breite=8, farbe=DGRUEN)),
    z("Beginn: Pfändung", 150, 475, beim("rsb", "sobald"), "Bold", 28),
    hart(linienzug([(ZB2, 420), (ZB2, 460)], beim("rsb2", "Verwertung"), breite=8, farbe=DROT)),
    z("Ende: Verwertung", 880, 475, beim("rsb2", "Verwertung"), "Bold", 28),
    karte(ZJ - 16, 424, 32, 32, beim("rsb3", "Bild"), fill=PINK, rund=16, schatten=3, rand=4, anim="pop"),
    z("jetzt: gepfändet, noch nicht versteigert", 330, 540, beim("rsb3", "gepfändet"), "Bold", 32),
    ok(1000, 560, beim("rsb3", "versteigert"), gr=20),
    blk(110, 640, 1040, 76, GRUEN, beim("rsb3", "zulässig"), [("Die Klage ist zulässig.", "ExtraBold", 38, INK)]),
    ok(1090, 678, beim("rsb3", "zulässig"), gr=24),
    ficon("tabler", "hourglass", IX, IU, 100, "rsb", fuell=GELB),
    pl("Versteigerung in 3 Wochen", IX, 200, beim("rsb3", "Bild"), fill=PINK, size=28, anker="m"),
    *fig("WE", FX, FB, FR, [("rsb", "denkt"), (beim("rsb3", "zulässig"), "froh")]),
    schild("Frau Wendland", FX, "rsb", WE_F),
]))

# I B. Begründetheit: die Veräußerung hinderndes Recht ------------------------------------------------------------------------------
folie([("begr", BE), ("recht", f"{BE} › 1. die Veräußerung hinderndes Recht: Eigentum")], rechts_frei([
    *tafel("begr", "B. Begründetheit"),
    z("1. ein die Veräußerung hinderndes Recht", 110, 180, "recht", "Bold", 36),
    z("Standardfall: das Eigentum", 150, 237, beim("recht", "Standardfall"), size=34),
    z("Die Vollstreckung greift auf Vermögen einer Dritten über,", 110, 320, beim("eig", "greift"), size=34),
    z("das nicht für die Forderung haftet.", 150, 373, beim("eig", "haftet"), size=34),
    zit("vgl. BGH, Urt. v. 14.9.2018 – V ZR 267/17, Rn. 6", 150, 425, beim("eig", "haftet")),
    z("Verwahrung (§ 688 BGB): Herr Vollmer besitzt nur,", 110, 505, beim("verwahr", "Verwahrung"), "Bold", 34),
    z("Eigentümerin bleibt Frau Wendland", 150, 560, beim("verwahr", "Eigentümerin"), "Bold", 34),
    ok(760, 582, beim("verwahr", "Großmutter"), gr=20),
    *gemaelde(MB, 170, 200, "begr"),
    pl("Eigentum: Frau Wendland", MB, 360, beim("recht", "Eigentum"), fill=BLAU, size=28, anker="m"),
    *fig("WE", X1, FB, FR, [("begr", "ruhig"), ("recht", "entschlossen"), (beim("verwahr", "Großmutter"), "froh")]),
    schild("Frau Wendland", X1, "begr", WE_F),
    *fig("VO", X2, FB, FR, [("begr", "ruhig"), ("verwahr", "froh")], d=0.2),
    schild("Herr Vollmer", X2, "begr", VO_F, d=0.3),
]))

# J Beweislast: Eigentumsvermutung § 1006 BGB ------------------------------------------------------------------------------------
W1006 = "„Zugunsten des Besitzers einer beweglichen Sache wird vermutet, dass er Eigentümer der Sache sei.“"
Z1006 = ["„Zugunsten des Besitzers einer beweglichen Sache",
         "wird vermutet, dass er Eigentümer der Sache sei.“"]
W1006c = "„Im Falle eines mittelbaren Besitzes gilt die Vermutung für den mittelbaren Besitzer.“"
Z1006c = ["„Im Falle eines mittelbaren Besitzes gilt die Vermutung",
          "für den mittelbaren Besitzer.“"]
w1006, w1006_y = wortlaut(90, 230, 1080, W1006, "§ 1006 Abs. 1 Satz 1 BGB", beim("bw2", "Zugunsten"), size=32, zeilen=Z1006,
                          marken=[("Besitzers", beim("bw2", "Besitzers")), ("Eigentümer", beim("bw2", "Eigentümer"))])
w1006c, w1006c_y = wortlaut(90, w1006_y + 194, 1080, W1006c, "§ 1006 Abs. 3 BGB", beim("p1006", "Absatz"), size=32,
                            zeilen=Z1006c, marken=[("für den mittelbaren Besitzer.“", beim("p1006", "für"))])
folie([("beweis", f"{BE} › 1. Beweislast"), ("bw2", f"{BE} › 1. Beweislast › Eigentumsvermutung, § 1006 BGB"),
       ("zettel2", f"{BE} › 1. Eigentum steht fest")], rechts_frei([
    *tafel("beweis", "Beweislast"),
    z("Die Klägerin muss ihr Recht beweisen.", 110, 170, beim("beweis", "Klägerin"), "Bold", 34),
    *w1006,
    pl("Besitzer hier: der Enkel", 110, w1006_y + 12, beim("bw2", "Enkel"), fill=GRUEN, size=28),
    z("Frau Wendland muss zeigen: Er verwahrt nur für sie.", 110, w1006_y + 79, beim("bw3", "zeigen"), "Bold", 32),
    *w1006c,
    z("Frau Wendland: mittelbare Besitzerin (§ 868 BGB)", 110, w1006_y + 139, beim("p1006", "mittelbare"), size=32),
    blk(110, w1006c_y + 14, 1040, 66, GRUEN, beim("zettel2", "Eigentum"), [("Zettel belegt die Verwahrung: Eigentum steht fest", "ExtraBold", 32, INK)]),
    ficon("tabler", "scale", MB, 380, 110, "beweis", fuell=WEISS, bis="zettel2"),
    pl("Wer muss beweisen?", MB, 180, "beweis", fill=PINK, size=28, anker="m", bis="zettel2"),
    ficon("tabler", "note", MB, 380, 100, "zettel2", fuell=WEISS, anim="cut"),
    pl("Zettel", MB, 180, beim("zettel2", "Zettel"), fill=WEISS, size=28, anker="m", anim="cut"),
    *fig("WE", X1, FB, FR, [("beweis", "sorge"), ("bw3", "denkt"), ("p1006", "ruhig"), (beim("zettel2", "Eigentum"), "strahlt")]),
    schild("Frau Wendland", X1, "beweis", WE_F),
    *fig("GE", X2, FB, FR, [("beweis", "ruhig"), ("bw2", "denkt"), (beim("zettel2", "Eigentum"), "ernst")], d=0.2),
    schild("Herr Gebhardt", X2, "beweis", GE_F, d=0.3),
]))

# K Einwendungen des Beklagten, Ergebnis --------------------------------------------------------------------------------------------
folie([("einw", f"{BE} › 2. keine Einwendungen des Beklagten"), ("keine", f"{BE} › Ergebnis: begründet")], rechts_frei([
    *tafel("einw", "2. Einwendungen des Beklagten?"),
    z("keine Einwendungen von Herrn Gebhardt", 110, 180, "einw", "Bold", 36),
    z("etwa: Das Vermögen der Dritten haftet selbst", 150, 250, beim("einw", "Vermögen"), size=34),
    z("für die Forderung.", 150, 303, beim("einw", "Forderung"), size=34),
    zit("vgl. BGH, Urt. v. 14.9.2018 – V ZR 267/17, Rn. 6", 150, 355, beim("einw", "Forderung")),
    z("Frau Wendland schuldet ihm nichts.", 110, 440, beim("keine", "Frau"), "Bold", 34),
    blk(110, 520, 1040, 76, GRUEN, beim("keine", "begründet"), [("Die Klage ist begründet.", "ExtraBold", 38, INK)]),
    ok(1090, 558, beim("keine", "begründet"), gr=24),
    ficon("tabler", "file-certificate", MB, 380, 100, "einw", fuell=WEISS),
    pl("Einwendungen?", MB, 180, "einw", fill=PINK, size=28, anker="m", bis=beim("keine", "nichts")),
    pl("keine", MB, 180, beim("keine", "nichts"), fill=GRUEN, size=28, anker="m", anim="cut"),
    *fig("WE", X1, FB, FR, [("einw", "ruhig"), (beim("keine", "begründet"), "strahlt")]),
    schild("Frau Wendland", X1, "einw", WE_F),
    *fig("GE", X2, FB, FR, [("einw", "denkt"), ("keine", "ernst")], d=0.2),
    schild("Herr Gebhardt", X2, "einw", GE_F, d=0.3),
]))

# L Tenor (Klausurkonvention) -------------------------------------------------------------------------------------------------------
folie([("tenor", "Tenor (Klausurkonvention)")], rechts_frei([
    *tafel("tenor", "Tenor (Klausurkonvention)"),
    blk(110, 200, 1040, 240, GRUEN, beim("tenor", "Die"),
        [("Die Zwangsvollstreckung aus dem Urteil", "Bold", 36, INK),
         ("des Amtsgerichts in das Ölgemälde", "Bold", 36, INK),
         ("wird für unzulässig erklärt.", "ExtraBold", 38, INK)]),
    zit("vgl. § 775 Nr. 1 ZPO; BGH, Urt. v. 11.1.2007 – IX ZR 181/05, Rn. 2", 110, 470, beim("tenor", "unzulässig")),
    ficon(HC, "balance-scale", MB, 380, 140, "tenor", fuell=WEISS),
    pl("unzulässig", MB, 180, beim("tenor", "unzulässig"), fill=GRUEN, size=30, anker="m"),
    *fig("WE", X1, FB, FR, [("tenor", "froh"), (beim("tenor", "unzulässig"), "strahlt")]),
    schild("Frau Wendland", X1, "tenor", WE_F),
    *fig("GE", X2, FB, FR, [("tenor", "ernst")], d=0.2),
    schild("Herr Gebhardt", X2, "tenor", GE_F, d=0.3),
]))

# M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · den Eilantrag nicht vergessen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Die Klage allein hält die Versteigerung", 200, 200, beim("tipp", "Klage"), "Bold", 36),
    z("nicht auf.", 200, 255, beim("tipp", "nicht"), "Bold", 36),
    z("Zugleich beantragen: einstweilige Einstellung", 200, 355, beim("tipp2", "Beantrage"), size=34),
    z("§ 771 Abs. 3 ZPO verweist auf §§ 769, 770 ZPO", 200, 420, beim("tipp2", "verweist"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "wl769"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Eilantrag: einstweilige Einstellung, Wortlaut § 769 Abs. 1 ZPO -----------------------------------------------------------------
W769 = ("„Das Prozessgericht kann auf Antrag anordnen, dass bis zum Erlass des Urteils … die Zwangsvollstreckung gegen "
        "oder ohne Sicherheitsleistung eingestellt … werde … Die tatsächlichen Behauptungen, die den Antrag begründen, "
        "sind glaubhaft zu machen.“")
Z769 = ["„Das Prozessgericht kann auf Antrag anordnen, dass bis zum",
        "Erlass des Urteils … die Zwangsvollstreckung gegen oder ohne",
        "Sicherheitsleistung eingestellt … werde … Die tatsächlichen",
        "Behauptungen, die den Antrag begründen, sind glaubhaft zu machen.“"]
w769, w769_y = wortlaut(90, 165, 1080, W769, "§ 769 Abs. 1 Satz 1, 3 ZPO (Auszug), über § 771 Abs. 3 ZPO", "wl769", size=30,
                        zeilen=Z769,
                        marken=[("auf Antrag", beim("wl769", "Antrag")),
                                ("gegen oder ohne", beim("wl769", "gegen")),
                                ("glaubhaft zu machen.“", beim("glaub", "glaubhaft"))])
PE = "Eilantrag"
folie([("wl769", f"{PE} › einstweilige Einstellung, § 769 ZPO"), ("glaub", f"{PE} › Glaubhaftmachung"),
       ("vorlage", f"{PE} › Vorlage, § 775 Nr. 2 ZPO"), ("p770", f"{PE} › Entscheidung im Urteil, § 770 ZPO")], rechts_frei([
    titel(glyphen("Eilantrag: einstweilige Einstellung"), 110, 75, "wl769", 44),
    *w769,
    *zz("glaubhaft machen:", "Zettel und eidesstattliche Versicherung", 110, w769_y + 25, beim("glaub", "Tatsachen"),
        beim("glaub", "Zettel"), "Bold", 32, rest_stil="Regular"),
    zit("§ 294 Abs. 1 ZPO", 150, w769_y + 72, beim("glaub", "eidesstattlichen")),
    *zz("Beschluss der Gerichtsvollzieherin vorlegen:", "Sie stellt ein,", 110, w769_y + 125, beim("vorlage", "Beschluss"),
        beim("vorlage", "stellt"), "Bold", 32, rest_stil="Regular"),
    z("§ 775 Nr. 2 ZPO", 150, w769_y + 175, beim("vorlage", "Paragraf"), size=32),
    *zz("Im Urteil:", "bestätigen, ändern oder aufheben,", 110, w769_y + 240, beim("p770", "Urteil"), beim("p770", "bestätigen"),
        "Bold", 32, rest_stil="Regular"),
    z("§ 770 ZPO", 150, w769_y + 290, beim("p770", "Paragraf"), size=32),
    ficon("tabler", "hand-stop", MB, 380, 100, "wl769", fuell=GELB, bis="vorlage"),
    pl("Versteigerung stoppen", MB, 180, "wl769", fill=GELB, size=28, anker="m", bis="vorlage"),
    ficon("tabler", "file-text", MB, 380, 90, "vorlage", fuell=WEISS, anim="cut", bis="p770"),
    pl("Beschluss vorlegen", MB, 180, beim("vorlage", "Beschluss"), fill=BLAU, size=28, anker="m", anim="cut", bis="p770"),
    ficon(HC, "balance-scale", MB, 380, 120, "p770", fuell=WEISS, anim="cut"),
    pl("§ 770", MB, 180, beim("p770", "Paragraf"), fill=WEISS, size=28, anker="m", anim="cut"),
    *fig("WE", X1, FB, FR, [("wl769", "entschlossen"), ("glaub", "ruhig"), (beim("vorlage", "stellt"), "froh")]),
    schild("Frau Wendland", X1, "wl769", WE_F),
    *fig("GV", X2, FB, FR, [("wl769", "ruhig"), ("vorlage", "denkt"), (beim("vorlage", "stellt"), "ruhig")], d=0.2),
    schild("Gerichtsvollzieherin", X2 - 20, "wl769", GV_F, d=0.3),
]))

# O Klausurschema ----------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("sA", "Klausurschema › A. Zulässigkeit"), ("sB", "Klausurschema › B. Begründetheit"),
       ("sC", "Klausurschema › Eilantrag")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Drittwiderspruchsklage, § 771 ZPO"), 110, 85, "sch", 46),
    z("A. Zulässigkeit", K1, 180, "sA", "ExtraBold", 38, rechts=1820),
    z("1. Statthaftigkeit: Dritter behauptet ein die Veräußerung hinderndes Recht", K2, 245, "s1", "Bold", 34, rechts=1820),
    *zz("2. Zuständigkeit: Ort der Vollstreckung, ausschließlich (§ 802);", "sachlich: Streitwert", K2, 310, "s2",
        beim("s2", "sachlich"), "Bold", 34, rechts=1820),
    z("3. Rechtsschutzbedürfnis: solange die Vollstreckung andauert", K2, 375, "s3", "Bold", 34, rechts=1820),
    z("B. Begründetheit", K1, 470, "sB", "ExtraBold", 38, rechts=1820),
    z("1. ein die Veräußerung hinderndes Recht, meist Eigentum (Beweislast, § 1006 BGB)", K2, 535, "sb1", "Bold", 34, rechts=1820),
    z("2. keine Einwendungen des Beklagten", K2, 600, "sb2", "Bold", 34, rechts=1820),
    blk(K1, 690, 1600, 90, GELB, "sC", [("Daneben: Antrag auf einstweilige Einstellung, §§ 771 Abs. 3, 769 ZPO", "Bold", 34, INK)]),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gepfändet wird, was der", 0)], [("Schuldner im ", 0), ("Gewahrsam", "a"), (" hat.", 0)]], 750, 310, 46,
                "merke", {"a": beim("merke", "Gewahrsam")}),
    *markertext([[("Gehört es einem Dritten:", 0)], [("Drittwiderspruchsklage", "b"), (".", 0)]], 750, 540, 46, "m2",
                {"b": beim("m2", "Drittwiderspruchsklage")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
