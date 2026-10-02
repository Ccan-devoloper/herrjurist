"""Folge 032 · Verhältnismäßigkeit prüfen: Die 4 Schritte im Öffentlichen Recht – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Spraydosen-Verbot per Allgemeinverfügung), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Graffiti in der Altstadt, B Im Farbengeschäft / Die Frage, C Sachverhalt, D Wortlaut Art. 20 III GG, E Herleitung,
F Prüfungsort, G Wortlaut § 40 VwVfG, H Wortlaut § 15 I, II BPolG, I 1. legitimer Zweck, J 2. Geeignetheit,
K 3. Erforderlichkeit, L 3. Erforderlichkeit: engeres Verbot / Ergebnis, M Variante (zurück im Laden), N 4. Angemessenheit
(Maßstab), O Abwägung, P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Ladenglocke, wenn Frau Dörr den Laden betritt; Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_032/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
PAPIER = (250, 246, 232, 255)
HOLZ = (236, 214, 178, 255)
HC = "fluent-emoji-high-contrast"
SF = "streamline-freehand"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_032/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte (wie Folge 019/025/028): Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        t = zeilen[zi]
        a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 020/025/028): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------
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


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=28, anker="m", d=d, bis=bis)


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
VH = "Verhältnismäßigkeit"
KU_F, FR_F, DO_F = ORANGE, GRUEN, BLAU     # Farben der Namensschilder


def laden(cue, ban_alle, ban_cue, anim="pop"):
    """Farbengeschäft (Szene B und M): Regal mit Farbsprühdosen (oben), Deo/Haarspray (Mitte), Lackeimern (unten), Tür.
    ban_alle=True: Verbotszeichen über dem ganzen Regal, sonst nur über der Reihe der Farbsprühdosen."""
    els = [
        linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
        karte(80, 300, 540, 560, cue, fill=HOLZ, rund=14, schatten=6, rand=5),
        linienzug([(90, 480), (610, 480)], cue, breite=6, farbe=INK),
        linienzug([(90, 670), (610, 670)], cue, breite=6, farbe=INK),
        *[ficon(SF, "color-spray", x, 470, 95, cue, fuell=f) for x, f in ((170, ROT), (300, BLAU), (430, GRUEN), (550, LILA))],
        *[ficon("tabler", "perfume", x, 660, 80, cue, fuell=f) for x, f in ((170, WEISS), (300, PINK), (430, WEISS), (550, GELB))],
        *[ficon("tabler", "bucket", x, 850, 110, cue, fuell=f) for x, f in ((210, ORANGE), (450, BLAU))],
        ficon("tabler", "door", 1800, BODEN - 2, 150, cue, fuell=HOLZ),
    ]
    if anim == "cut":
        for e in els:
            e.anim = "cut"
    if ban_alle:
        els.append(ficon("tabler", "ban", 350, 820, 420, ban_cue))
    else:
        els.append(ficon("tabler", "ban", 360, 490, 200, ban_cue))
    return els


# A Fall: Graffiti in der Altstadt --------------------------------------------------------------------------------------
KUX_A = 1620
folie([(NULL, "Fall · Graffiti in der Altstadt")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Montagmorgen in der Altstadt", 70, 40, NULL, fill=GELB, size=44)),
    ficon("tabler", "home", 190, BODEN - 2, 240, NULL, fuell=PINK, anim="cut"),
    ficon("ph", "wall", 560, BODEN - 2, 400, NULL, fuell=ORANGE, anim="cut"),
    ficon("ph", "scribble-loop", 500, BODEN - 120, 170, NULL, fuell=LILA, anim="cut"),
    ficon("ph", "scribble", 650, BODEN - 40, 130, NULL, anim="cut"),
    ficon("tabler", "sun", 1740, 200, 120, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "building-store", 1230, BODEN - 2, 330, NULL, fuell=BLAU, anim="cut"),
    pl("über Nacht besprüht", 560, 470, beim("fall", "besprüht"), fill=PINK, size=32, anker="m"),
    *fig("KU", KUX_A, BODEN, FH, [("kuehn", "ruhig"), (beim("kuehn", "Bei"), "froh")]),
    schild("Herr Kühn, Farbengeschäft", KUX_A, beim("kuehn", "Kühn"), KU_F, unten=BODEN, d=0.0),
    ficon("tabler", "bucket", 1110, 510, 90, beim("kuehn", "Lacke"), fuell=ORANGE),
    ficon("tabler", "brush", 1230, 510, 90, beim("kuehn", "Pinsel"), fuell=GELB),
    ficon(SF, "color-spray", 1350, 510, 90, beim("kuehn", "Spraydosen"), fuell=ROT),
])

# B Fall: im Farbengeschäft / die Frage ------------------------------------------------------------------------------------
KUX, FRX, DOX = 760, 1130, 1580
KUb = ("KU_redet_r", KUX, BODEN, FH)
FRb = ("FR_redet_r", FRX, BODEN, FH)
DOb = ("DO_redet", DOX, BODEN, FH)
KOMMT = beim("doerr", "kommt")
folie([("frauke", "Fall · Im Farbengeschäft"), ("frage", "Fall · Die Frage")], [
    pl("Im Farbengeschäft", 70, 40, "frauke", fill=GELB, size=40),
    *laden("frauke", True, beim("do1", "verkaufen")),
    # Herr Kühn
    *fig("KU", KUX, BODEN, FH, [("frauke", "ruhig_r")], bis="ku1"),
    *redet("KU_redet_r", KUX, BODEN, FH, "ku1", "fr1"),
    *fig("KU", KUX, BODEN, FH, [("fr1", "ruhig_r"), ("frage", "sorge_r")], erst="cut"),
    schild("Herr Kühn", KUX, "frauke", KU_F, unten=BODEN),
    # Frauke
    *fig("FR", FRX, BODEN, FH, [("frauke", "ruhig"), (KOMMT, "ruhig_r")], bis="fr1", d=0.15),
    *redet("FR_redet_r", FRX, BODEN, FH, "fr1", "frage"),
    *fig("FR", FRX, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    schild("Frauke, Wandmalerin", FRX, beim("frauke", "Frauke"), FR_F, unten=BODEN, d=0.0),
    bis_(ficon("tabler", "brush", FRX, 380, 90, beim("frauke", "Wandbilder"), fuell=GELB), "do1"),
    # Frau Dörr betritt den Laden (Ladenglocke)
    szene(peep_voll("DO_ruhig", DOX, BODEN, FH, KOMMT, anim="pop", bis="do1"), "032tuerglocke*", 1.0),
    *redet("DO_redet", DOX, BODEN, FH, "do1", "ku1"),
    *fig("DO", DOX, BODEN, FH, [("ku1", "ruhig"), ("frage", "denkt")], erst="cut"),
    schild("Frau Dörr, Ordnungsamt", DOX, beim("doerr", "Dörr"), DO_F, unten=BODEN, d=0.0),
    ficon("tabler", "file-text", 1360, 760, 80, beim("doerr", "Allgemeinverfügung"), fuell=WEISS),
    pl("Allgemeinverfügung", 1360, 965, beim("doerr", "Allgemeinverfügung"), fill=WEISS, size=26, anker="m"),
    pl("alle Spraydosen", 350, 230, beim("do1", "alle"), fill=ROT, size=32, anker="m"),
    bis_(pl("Deo", 170, 500, beim("ku1", "Deo"), fill=WEISS, size=24, anker="m"), "frage"),
    bis_(pl("Haarspray", 480, 500, beim("ku1", "Haarspray"), fill=WEISS, size=24, anker="m"), "frage"),
    blase("sprech", 820, 260, "do1", 1260, 200, inhalt=["Um die Graffiti zu stoppen, darf ab", "sofort niemand in der Stadt",
                                                      "Spraydosen verkaufen. Und zwar alle."], textsize=30, figur=DOb, bis="ku1"),
    blase("sprech", 460, 210, "ku1", 830, 200, inhalt=["Alle? Auch Deo", "und Haarspray?"], textsize=34, figur=KUb, bis="fr1"),
    blase("sprech", 760, 250, "fr1", 1200, 200, inhalt=["Ich male nur Wände, die ich", "bemalen darf. Dafür brauche",
                                                      "ich Sprühfarbe."], textsize=30, figur=FRb, bis="frage"),
    pl("Ist dieses Verbot verhältnismäßig?", 1180, 60, beim("frage", "Ist"), fill=PINK, size=36, anker="m"),
    pl("4 Schritte", 1180, 140, beim("frage", "vier"), fill=GELB, size=32, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "In der Altstadt werden über Nacht immer wieder Hauswände unerlaubt mit Graffiti besprüht. Das Ordnungsamt der Stadt "
    "erlässt deshalb eine Allgemeinverfügung: Ab sofort darf im Stadtgebiet niemand mehr Spraydosen verkaufen, und zwar "
    "alle, auch Deo und Haarspray. Herr Kühn betreibt ein Farbengeschäft. Frauke kauft dort Sprühfarbe für Wandbilder, "
    "die sie erlaubt malt. Gesprüht wird von Jugendlichen und Erwachsenen; viele Sprayer bestellen ihre Dosen ohnehin im "
    "Internet. Die meisten Kunden kaufen Sprühfarbe für erlaubte Zwecke.",
    "Bearbeitervermerk: Die Allgemeinverfügung stützt sich auf eine wirksame Ermächtigung zur Gefahrenabwehr, die Ermessen "
    "einräumt; ihre Voraussetzungen sind zu unterstellen. Zu prüfen ist nur die Verhältnismäßigkeit.",
], "Ist das Verbot verhältnismäßig?")

# D Herleitung: Wortlaut Art. 20 III GG -----------------------------------------------------------------------------------------
W20 = ["„Die Gesetzgebung ist an die verfassungsmäßige", "Ordnung, die vollziehende Gewalt und die",
       "Rechtsprechung sind an Gesetz und Recht", "gebunden.“"]
w20_els, w20_y = wortlaut(80, 200, 1100, W20, "Art. 20 Abs. 3 GG", "wl20", marken=[
    (0, "Gesetzgebung", beim("wl20", "Gesetzgebung")), (0, "verfassungsmäßige", beim("wl20", "verfassungsmäßige")),
    (1, "Ordnung", beim("wl20", "verfassungsmäßige")), (1, "vollziehende Gewalt", beim("wl20", "vollziehende")),
    (2, "Rechtsprechung", beim("wl20", "Rechtsprechung")), (2, "Gesetz und Recht", beim("wl20", "Gesetz", nr=2))], size=40)
folie([("herk", "Herleitung · Woher kommt der Grundsatz?"), ("wl20", "Herleitung › Wortlaut Art. 20 III GG")], rechts_frei([
    titel(glyphen("Woher kommt der Grundsatz?"), 110, 90, "herk", 50),
    *w20_els,
    nein(140, w20_y + 75, beim("nicht", "Verhältnismäßigkeit"), gr=22),
    z("Das Wort „Verhältnismäßigkeit“ steht da nicht.", 185, w20_y + 55, "nicht", "Bold", 36),
    ficon("tabler", "book", IX, IU, 140, "wl20", fuell=GELB),
    *fig("KU", FX, FB, FR, [("herk", "ruhig"), ("nicht", "denkt")]),
    schild("Herr Kühn", FX, "herk", KU_F),
]))

# E Herleitung durch das BVerfG -------------------------------------------------------------------------------------------------
folie([("rsp", "Herleitung › Rechtsstaatsprinzip und Grundrechte"), ("rang", "Herleitung › Verfassungsrang")], rechts_frei([
    *tafel("rsp", "Herleitung durch das BVerfG"),
    z("leitet den Grundsatz ab", 110, 185, beim("rsp", "leitet"), size=34, farbe=TEXT),
    z("aus dem Rechtsstaatsprinzip", 110, 240, beim("rsp", "Rechtsstaatsprinzip"), "Bold", 38),
    z("im Grunde schon aus dem Wesen der Grundrechte", 110, 300, beim("rsp", "Grunde"), size=34),
    z("Freiheit nur so weit beschränken, wie es zum", 110, 390, "wesen", size=34),
    z("Schutz öffentlicher Interessen unerlässlich ist", 110, 440, beim("wesen", "Schutz"), size=34),
    blk(110, 520, 1040, 90, GELB, "rang", [("Verfassungsrang", "ExtraBold", 38, INK)]),
    z("gilt auch beim Anwenden einfacher Gesetze", 110, 645, beim("rang", "gilt"), size=34),
    zit("BVerfGE 19, 342 (348 f.) · BVerfGE 65, 1 Rn. 149 · BVerfG, 2 BvR 2135/09, Rn. 8", 110, 730,
        beim("rang", "Gesetze")),
    ficon(HC, "classical-building", IX, IU, 160, "rsp", fuell=WEISS, bis="wesen"),
    ficon("tabler", "shield-check", IX, IU, 130, "wesen", fuell=GRUEN, bis="rang"),
    ficon("tabler", "book", IX, IU, 140, "rang", fuell=GELB),
    *fig("FR", FX, FB, FR, [("rsp", "ruhig")]),
    schild("Frauke", FX, "rsp", FR_F),
]))

# F Prüfungsort ----------------------------------------------------------------------------------------------------------------
folie([("ort", "Prüfungsort › Grundrechte: Schranken-Schranken"), ("art12", "Prüfungsort › Art. 12 I GG, Berufsausübung"),
       ("ermess", "Prüfungsort › Ermessen der Behörde")], rechts_frei([
    *tafel("ort", "Wo prüfst du ihn?"),
    z("1. Grundrechtsprüfung:", 110, 190, beim("ort", "Grundrechtsprüfung"), "Bold", 38),
    z("in den Schranken-Schranken", 150, 250, beim("ort", "Schranken"), size=36),
    z("hier: Berufsausübung von Herrn Kühn,", 150, 330, "art12", size=34),
    z("Art. 12 I GG", 150, 380, beim("art12", "Artikel"), "Bold", 34),
    z("2. Verwaltungsrecht:", 110, 480, "ermess", "Bold", 38),
    z("Grenze des Ermessens der Behörde", 150, 540, beim("ermess", "Ermessen"), size=36),
    ficon("tabler", "building-store", IX, IU, 160, "art12", fuell=BLAU, bis="ermess"),
    ficon("tabler", "file-text", IX, IU, 120, "ermess", fuell=WEISS),
    *fig("KU", FX, FB, FR, [("ort", "ruhig"), ("art12", "sorge")]),
    schild("Herr Kühn", FX, "ort", KU_F),
]))

# G Wortlaut § 40 VwVfG --------------------------------------------------------------------------------------------------------
W40 = ["„Ist die Behörde ermächtigt, nach ihrem Ermessen zu", "handeln, hat sie ihr Ermessen entsprechend dem",
       "Zweck der Ermächtigung auszuüben und die", "gesetzlichen Grenzen des Ermessens einzuhalten.“"]
w40_els, w40_y = wortlaut(80, 170, 1100, W40, "§ 40 VwVfG", "wl40", marken=[
    (0, "Ermessen", beim("wl40", "Ermessen")), (2, "Zweck der Ermächtigung", beim("wl40", "Zweck")),
    (3, "gesetzlichen Grenzen", beim("wl40", "gesetzlichen"))], size=38)
folie([("wl40", "Prüfungsort › Ermessen, § 40 VwVfG"), ("land", "Prüfungsort › Landesrecht und Verfassung")], rechts_frei([
    titel(glyphen("Ermessen: § 40 VwVfG"), 110, 80, "wl40", 50),
    *w40_els,
    z("Stadt: Verfahrensgesetz ihres Landes", 110, w40_y + 50, "land", size=36),
    z("Verhältnismäßigkeit gilt schon von Verfassungs wegen", 110, w40_y + 110, beim("land", "Grenze"), "Bold", 34),
    zit("Bund: § 40 VwVfG · Länder: eigenes VwVfG (in deinem Land ggf. andere Fundstelle)", 110, w40_y + 180,
        beim("land", "Landes")),
    ficon("tabler", "file-text", IX, IU, 120, "wl40", fuell=WEISS),
    *fig("DO", FX, FB, FR, [("wl40", "ruhig")]),
    schild("Frau Dörr", FX, "wl40", DO_F),
]))

# H Wortlaut § 15 I, II BPolG ----------------------------------------------------------------------------------------------------
W15 = ["„(1) Von mehreren möglichen und geeigneten Maßnahmen", "ist diejenige zu treffen, die den einzelnen und die",
       "Allgemeinheit voraussichtlich am wenigsten", "beeinträchtigt. (2) Eine Maßnahme darf nicht zu",
       "einem Nachteil führen, der zu dem erstrebten Erfolg", "erkennbar außer Verhältnis steht.“"]
w15_els, w15_y = wortlaut(80, 170, 1100, W15, "§ 15 Abs. 1 und 2 BPolG", "wl15", marken=[
    (0, "(1)", "abs1"), (3, "(2)", "abs2"), (2, "am wenigsten", beim("abs1", "wenigsten")), (3, "beeinträchtigt", beim("abs1", "beeinträchtigt")),
    (4, "Nachteil", beim("abs2", "Nachteil")), (5, "erkennbar außer Verhältnis", beim("abs2", "erkennbar"))], size=36)
folie([("wl15", "Prüfungsort › ausdrücklich geregelt: § 15 BPolG")], rechts_frei([
    titel(glyphen("Ausdrücklich geregelt: § 15 BPolG"), 110, 80, "wl15", 50),
    *w15_els,
    ficon("tabler", "book", IX, IU, 140, "wl15", fuell=BLAU),
    *fig("DO", FX, FB, FR, [("wl15", "ruhig"), ("abs2", "denkt")]),
    schild("Frau Dörr", FX, "wl15", DO_F),
]))

# I 1. legitimer Zweck ------------------------------------------------------------------------------------------------------------
ERST = beim("s1", "Erstens")
folie([(ERST, f"{VH} › 1. legitimer Zweck")], rechts_frei([
    karte(60, 60, 1140, 840, ERST),
    titel(glyphen("1. legitimer Zweck"), 110, 100, ERST, 46),
    z("Behörde: Zweck der Ermächtigung", 110, 190, "zweckb", "Bold", 36),
    z("hier: Abwehr von Gefahren", 150, 250, beim("zweckb", "Abwehr"), size=36),
    z("unerlaubt fremde Wände besprühen:", 110, 340, "graff", size=36),
    z("Sachbeschädigung, § 303 II StGB", 150, 400, beim("graff", "Sachbeschädigung"), "Bold", 36),
    blk(110, 490, 1040, 90, GRUEN, "legit", [("Hauswände schützen: legitimer Zweck", "ExtraBold", 36, INK)]),
    ok(1110, 535, beim("legit", "legitimer"), gr=22),
    zit("§ 40 VwVfG · § 303 Abs. 2 StGB · vgl. BVerfGE 159, 223 Rn. 169", 110, 620, beim("legit", "Zweck")),
    ficon("tabler", "shield-check", IX, IU, 130, "zweckb", fuell=GRUEN, bis="graff"),
    ficon("ph", "wall", IX, IU, 230, "graff", fuell=ORANGE),
    ficon("ph", "scribble-loop", IX - 30, IU - 30, 110, beim("graff", "besprüht"), fuell=LILA),
    *fig("KU", FX, FB, FR, [(ERST, "ruhig")]),
    schild("Herr Kühn", FX, ERST, KU_F),
]))

# J 2. Geeignetheit --------------------------------------------------------------------------------------------------------------
KU2 = ("KU_redet", FX, FB, FR)
folie([("s2", f"{VH} › 2. Geeignetheit")], rechts_frei([
    *tafel("s2", "2. Geeignetheit"),
    z("geeignet, wenn das Mittel den", 110, 190, beim("s2", "Geeignet"), "Bold", 36),
    z("Zweck fördern kann", 110, 245, beim("s2", "fördern"), "Bold", 36),
    z("die Möglichkeit genügt", 150, 310, beim("s2", "Möglichkeit"), size=34),
    z("viele bestellen online", 150, 400, "foerd", size=34),
    z("aber: ohne Dose um die Ecke vielleicht seltener", 150, 455, beim("foerd", "Aber"), size=34),
    z("muss den Zweck nicht vollständig erreichen", 150, 535, "geeig", size=34),
    blk(110, 590, 1040, 85, GRUEN, beim("geeig", "geeignet"), [("geeignet", "ExtraBold", 38, INK)]),
    ok(1110, 633, beim("geeig", "geeignet"), gr=22),
    nein(140, 735, "fehl1", gr=18),
    z("Fehler: Eignung verneinen, weil das Mittel", 185, 715, "fehl1", size=32),
    z("nicht perfekt wirkt", 185, 762, beim("fehl1", "perfekt"), size=32),
    zit("BVerfGE 159, 223 Rn. 185 f.", 110, 830, beim("fehl1", "wirkt")),
    ficon("tabler", "world-www", IX, IU, 130, "foerd", fuell=WEISS, bis=beim("foerd", "Aber")),
    ficon("tabler", "building-store", IX, IU, 150, beim("foerd", "Aber"), fuell=BLAU),
    *fig("KU", FX, FB, FR, [("s2", "ruhig")], bis="ku2"),
    *redet("KU_redet", FX, FB, FR, "ku2", "foerd"),
    *fig("KU", FX, FB, FR, [("foerd", "denkt"), ("geeig", "muede")], erst="cut"),
    schild("Herr Kühn", FX, "s2", KU_F),
    blase("sprech", 600, 300, "ku2", 1560, 200, inhalt=["Das bringt doch nichts.", "Die Sprayer bestellen",
                                                      "ihre Dosen einfach", "im Internet."], textsize=30, figur=KU2, bis="foerd"),
]))

# K 3. Erforderlichkeit --------------------------------------------------------------------------------------------------------
folie([("s3", f"{VH} › 3. Erforderlichkeit")], rechts_frei([
    *tafel("s3", "3. Erforderlichkeit"),
    z("kein milderes Mittel, das gleich wirksam ist", 110, 190, beim("s3", "kein"), "Bold", 36),
    z("beides zusammen: milder und gleich wirksam", 150, 255, beim("s3", "Beides"), size=34),
    z("Gleichwertigkeit muss eindeutig feststehen", 110, 345, "eind", size=34),
    z("Gesetzgeber: Einschätzungsspielraum", 110, 400, beim("eind", "Gesetzgeber"), size=34),
    zit("BVerfGE 159, 223 Rn. 203 f.", 110, 460, beim("eind", "Einschätzungsspielraum")),
    z("Verkaufsverbot nur an Jugendliche?", 110, 545, "jung", "Bold", 36),
    ok(150, 630, beim("jung", "milder"), gr=20),
    z("milder", 195, 610, beim("jung", "milder"), size=34),
    nein(150, 690, beim("jung", "nicht"), gr=18),
    z("nicht gleich wirksam: auch Erwachsene sprayen", 195, 670, beim("jung", "nicht"), size=34),
    ficon(SF, "color-spray", IX, IU, 130, "s3", fuell=ROT, bis="jung"),
    ficon("tabler", "mood-kid", IX, IU, 130, "jung", fuell=GELB),
    *fig("FR", FX, FB, FR, [("s3", "ruhig"), ("eind", "denkt")]),
    schild("Frauke", FX, "s3", FR_F),
]))

# L 3. Erforderlichkeit: engeres Verbot, Ergebnis ------------------------------------------------------------------------------
folie([("farbe", f"{VH} › 3. Erforderlichkeit › nur Farbsprühdosen?"),
       ("erg1", "Ergebnis: Verbot aller Spraydosen rechtswidrig")], rechts_frei([
    *tafel("farbe", "3. Erforderlichkeit: engeres Verbot"),
    z("Verbot nur für Farbsprühdosen?", 110, 190, "farbe", "Bold", 36),
    z("Deo und Haarspray: kein Graffiti", 150, 255, beim("farbe", "Mit"), size=34),
    ok(150, 345, beim("farbe", "genauso"), gr=20),
    z("wirkt genauso", 195, 325, beim("farbe", "genauso"), size=34),
    ok(150, 405, beim("farbe", "belastet"), gr=20),
    z("belastet weniger", 195, 385, beim("farbe", "belastet"), size=34),
    z("eindeutig: da hilft kein Spielraum", 110, 470, "kein", "Bold", 34),
    blk(110, 550, 1040, 90, ROT, "erg1", [("Verbot aller Spraydosen: nicht erforderlich", "ExtraBold", 34, INK)]),
    nein(1110, 595, beim("erg1", "nicht"), gr=22),
    z("Grenzen des Ermessens überschritten:", 110, 680, beim("erg1", "Stadt"), size=34),
    z("Allgemeinverfügung rechtswidrig", 110, 730, beim("erg1", "rechtswidrig"), "Bold", 36),
    ficon(SF, "color-spray", IX - 90, IU, 120, "farbe", fuell=ROT),
    ficon("tabler", "perfume", IX + 90, IU, 100, beim("farbe", "Deo"), fuell=WEISS),
    *fig("KU", FX, FB, FR, [("farbe", "ruhig"), ("erg1", "froh")]),
    schild("Herr Kühn", FX, "farbe", KU_F),
]))

# M Variante: zurück im Farbengeschäft -------------------------------------------------------------------------------------------
NACH = beim("var", "bessert")
folie([("var", "Gutachten · Prüfung beendet"), (beim("var", "Doch"), "Variante · nur Farbsprühdosen verboten")], [
    pl("Im Gutachten: Prüfung beendet", 70, 40, "var", fill=WEISS, size=36),
    *laden("var", False, beim("var", "verbietet")),
    *fig("KU", KUX, BODEN, FH, [("var", "ruhig_r"), ("var2", "denkt_r")]),
    schild("Herr Kühn", KUX, "var", KU_F, unten=BODEN),
    szene(peep_voll("DO_ruhig", DOX, BODEN, FH, NACH, anim="pop"), "032tuerglocke*", 1.0),
    schild("Frau Dörr, Ordnungsamt", DOX, NACH, DO_F, unten=BODEN),
    ficon("tabler", "file-text", 1360, 760, 80, NACH, fuell=WEISS),
    pl("neu: nur Farbsprühdosen verboten", 1180, 200, beim("var", "verbietet"), fill=ROT, size=32, anker="m"),
    pl("Zweck und Eignung bleiben", 1180, 280, "var2", fill=GRUEN, size=30, anker="m"),
    pl("kein gleich wirksames milderes Mittel", 1180, 350, beim("var2", "gleich"), fill=WEISS, size=30, anker="m"),
    pl("jetzt: 4. Schritt", 1180, 420, beim("var2", "vierte"), fill=GELB, size=30, anker="m"),
])

# N 4. Angemessenheit: Maßstab --------------------------------------------------------------------------------------------------
folie([("s4", "Variante › 4. Angemessenheit")], rechts_frei([
    *tafel("s4", "4. Angemessenheit"),
    z("Verhältnismäßigkeit im engeren Sinne", 110, 185, beim("s4", "Verhältnismäßigkeit"), size=34, farbe=TEXT),
    z("Zweck und zu erwartende Zweckerreichung", 110, 260, beim("s4", "Zweck"), "Bold", 36),
    z("nicht außer Verhältnis", 150, 320, beim("s4", "außer"), "Bold", 36),
    z("zur Schwere des Eingriffs", 150, 375, beim("s4", "Schwere"), "Bold", 36),
    z("je empfindlicher der Einzelne getroffen wird,", 110, 470, "je", size=34),
    z("desto gewichtiger das Gemeinwohlinteresse", 110, 525, beim("je", "desto"), "Bold", 34),
    zit("BVerfGE 159, 223 Rn. 216 f.", 110, 600, beim("je", "sein")),
    ficon(HC, "balance-scale", IX, IU, 190, "s4", fuell=GELB),
    *fig("FR", FX, FB, FR, [("s4", "ruhig"), ("je", "denkt")]),
    schild("Frauke", FX, "s4", FR_F),
]))

# O Abwägung -------------------------------------------------------------------------------------------------------------------
KUO, FRO = 1390, 1720
FRo = ("FR_redet", FRO, FB, FR)
folie([("last", "Variante › 4. Angemessenheit › Abwägung"), ("erg2", "Ergebnis Variante: eher unangemessen")], rechts_frei([
    *tafel("last", "Abwägung"),
    z("Last:", 110, 180, "last", "ExtraBold", 36),
    z("Herr Kühn: eine ganze Warengruppe weg", 150, 232, beim("last", "Herr"), size=32),
    z("Frauke: kein Arbeitsmaterial in der Stadt", 150, 282, beim("last", "Frauke"), size=32),
    z("trifft fast nur Menschen, die nichts falsch machen", 150, 332, "streu", size=32),
    z("Nutzen:", 110, 410, "nutzen", "ExtraBold", 36),
    z("Eigentum schützen: wiegt schwer", 150, 462, beim("nutzen", "Eigentum"), size=32),
    z("aber: Sprayer weichen leicht aus, Gewinn klein", 150, 512, beim("nutzen", "Aber"), size=32),
    blk(110, 580, 1040, 85, ROT, "erg2", [("spricht viel für: unangemessen", "ExtraBold", 36, INK)]),
    z("gut begründet: Gegenteil vertretbar", 110, 695, beim("erg2", "Gut"), size=32),
    z("gewichten statt behaupten", 110, 760, "abw", "Bold", 36),
    zit("vgl. BVerfGE 159, 223 Rn. 216", 110, 830, beim("abw", "behauptest")),
    *fig("KU", KUO, FB, FR, [("last", "ruhig"), (beim("last", "Herr"), "sorge")]),
    schild("Herr Kühn", KUO, "last", KU_F),
    *fig("FR", FRO, FB, FR, [("last", "ruhig"), (beim("last", "Frauke"), "sorge")], bis="fr2", d=0.1),
    *redet("FR_redet", FRO, FB, FR, "fr2", "nutzen"),
    *fig("FR", FRO, FB, FR, [("nutzen", "denkt")], erst="cut"),
    schild("Frauke", FRO, "last", FR_F, d=0.3),
    blase("sprech", 600, 270, "fr2", 1560, 200, inhalt=["Ich darf meine Wände doch", "bemalen. Warum darf ich",
                                                      "die Farbe nicht kaufen?"], textsize=30, figur=FRo, bis="nutzen"),
]))

# P Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Aufbau"), ("fehler", "Klausurtipp · typische Fehler")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("4 Schritte = Klausurkonvention,", 200, 200, beim("tipp", "vier"), "Bold", 36),
    z("das Gesetz schreibt den Aufbau nicht vor", 200, 255, beim("tipp", "das"), size=34),
    z("ausführlich nur, wo es streitig ist:", 200, 330, "ausf", size=34),
    z("meist Erforderlichkeit und Angemessenheit", 200, 380, beim("ausf", "meist"), "Bold", 34),
    z("Typische Fehler:", 110, 465, "fehler", "Bold", 36),
    nein(150, 550, "t1", gr=18), z("„steht im Wortlaut von Art. 20 III GG“", 200, 530, "t1", size=34),
    nein(150, 610, "t2", gr=18), z("milderes, aber weniger wirksames Mittel", 200, 590, "t2", size=34),
    nein(150, 670, "t3", gr=18), z("Angemessenheit: nur das Ergebnis", 200, 650, "t3", size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# Q Klausurschema -----------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Verhältnismäßigkeit"), 110, 90, "sch", 48),
    z("Verhältnismäßigkeit", K1, 190, "q0", "Bold", 40, rechts=1820),
    z("1. legitimer Zweck", K2, 270, "q1", "Bold", 38, rechts=1820),
    z("bei Behörden: Zweck der Ermächtigung", K3, 325, beim("q1", "Behörden"), size=34, rechts=1820),
    z("2. Geeignetheit", K2, 400, "q2", "Bold", 38, rechts=1820),
    z("Förderung genügt", K3, 455, beim("q2", "Förderung"), size=34, rechts=1820),
    z("3. Erforderlichkeit", K2, 530, "q3", "Bold", 38, rechts=1820),
    z("kein milderes, gleich wirksames Mittel", K3, 585, beim("q3", "kein"), size=34, rechts=1820),
    z("4. Angemessenheit", K2, 660, "q4", "Bold", 38, rechts=1820),
    z("Abwägung: Eingriffsschwere und Gewicht des Zwecks", K3, 715, beim("q4", "Abwägung"), size=34, rechts=1820),
])

# R Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein milderes Mittel zählt nur,", 0)], [("wenn es ", 0), ("genauso gut wirkt.", "a")]],
                750, 310, 50, "merke", {"a": beim("merke", "genauso")}),
    *markertext([[("Und angemessen ist ein Eingriff erst,", 0)], [("wenn sein ", 0), ("Nutzen die Last trägt.", "b")]],
                750, 540, 46, "m2", {"b": beim("m2", "Nutzen")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
