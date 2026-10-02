"""Folge 082 · § 80 V VwGO: Imbiss sofort geschlossen – was tun? Das Grundschema – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Imbissbude, Lebensmittelüberwachung der Stadt, Betriebsschließung mit Anordnung der sofortigen Vollziehung),
Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Imbiss (Kontrolle, Bescheid), B Verwaltungsgericht (Klage, Frage),
C Sachverhalt, D Grundsatz § 80 I 1 (Wortlaut), E Entfallen § 80 II 1 (Wortlaut Nr. 4), F Antrag § 80 V 1 (Wortlaut),
G A. Zulässigkeit I.–II., H III.–V., I B. I. formelle Rechtmäßigkeit der Anordnung, J II. Interessenabwägung,
K Erfolgsaussichten im Fall (Wortlaut Art. 138 II h VO (EU) 2017/625), L besonderes Vollzugsinteresse, M Beschluss
(Richterin), N Nachkontrolle (Imbiss), O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, wenn der Bescheid erscheint)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_082/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_082/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach der amtlichen Quelle, als Zitat mit Normangabe; feste Zeilen ergeben zusammen
    genau den Normtext. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    Wortgruppe (die Wortgruppe muss in einer Zeile stehen)."""
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


# --- Eigene Hilfsfunktion (wie Folge 069/064/061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HI_F, ST_F, RI_F = GELB, BLAU, LILA         # Farben der Namensschilder
ZU = "A. Zulässigkeit"
BG = "B. Begründetheit"
PV = "Prüfung § 80 V VwGO"


def imbiss(cx, cue, anim="pop", bis=None, breite=440):
    """Die Imbissbude von Herrn Hinrichs: Tabler „building-store“ (gelb), davor Pommes (Fluent HC „french-fries“) und
    Wurst (Tabler „sausage“) – in jeder Imbiss-Szene gleich."""
    return [ficon("tabler", "building-store", cx, BODEN, breite, cue, fuell=GELB, anim=anim, bis=bis),
            ficon(HC, "french-fries", cx - 95, BODEN - 120, 90, cue, fuell=GELB, anim=anim, bis=bis),
            ficon("tabler", "sausage", cx + 95, BODEN - 130, 90, cue, fuell=ROT, anim=anim, bis=bis)]


# A Fall: Kontrolle im Imbiss, der Bescheid ---------------------------------------------------------------------------------
BUX, HIX, STX = 450, 940, 1560
HIb = ("HI_redet_r", HIX, BODEN, FH)
STb = ("ST_redet", STX, BODEN, FH)
KOMMT = beim("steinke", "Frau")
TAG = beim("bescheid", "Am")
folie([(NULL, "Fall · Mittag an der Imbissbude"), ("steinke", "Fall · Die Kontrolle"), ("bescheid", "Fall · Der Bescheid")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(bis_(pl("Mittag an der Imbissbude", 70, 40, NULL, fill=GELB, size=40), "bescheid")),
    pl("Am nächsten Tag: der Bescheid", 70, 40, "bescheid", fill=GELB, size=40),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *[hart(e) for e in imbiss(BUX, NULL, anim="cut")],
    pl("Currywurst und Pommes", BUX, 200, beim("fall", "Currywurst"), fill=WEISS, size=30, anker="m"),
    *fig("HI", HIX, BODEN, FH, [(NULL, "ruhig_r"), (beim("kot", "Mäusekot"), "sorge_r"), (TAG, "aerger_r")], bis="hi1", erst="cut"),
    *redet("HI_redet_r", HIX, BODEN, FH, "hi1", "klage"),
    hart(schild("Herr Hinrichs, Imbiss", HIX, NULL, HI_F, unten=BODEN, d=0.0)),
    *fig("ST", STX, BODEN, FH, [(KOMMT, "ruhig")], bis="st1"),
    *redet("ST_redet", STX, BODEN, FH, "st1", "bescheid"),
    peep_voll("ST_ruhig", STX, BODEN, FH, "bescheid", anim="cut"),
    schild("Frau Steinke, Lebensmittelüberwachung", STX, KOMMT, ST_F, unten=BODEN, d=0.0),
    ficon("tabler", "clipboard-check", STX - 150, 640, 80, beim("steinke", "kontrolliert"), fuell=WEISS, bis="bescheid"),
    ficon(HC, "mouse", BUX - 150, BODEN - 4, 70, beim("kot", "Mäusekot"), fuell=WEISS),
    pl("Mäusekot auf der Arbeitsfläche", BUX, 265, beim("kot", "Mäusekot"), fill=ROT, size=30, anker="m"),
    pl("angenagte Brötchentüten", BUX, 330, beim("kot", "angenagte"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 760, 215, "st1", 1240, 170, inhalt=["Herr Hinrichs, das ist Mäusekot.", "Dazu dürfen Sie sich jetzt äußern.",
                                                      "Morgen bekommen Sie unseren Bescheid."], textsize=29, figur=STb, bis="bescheid"),
    szene(ficon("tabler", "file-text", STX - 150, 690, 90, beim("bescheid", "kommt"), fuell=WEISS), "082brief*", 0.8, -0.20),
    ficon("tabler", "lock", BUX, BODEN - 150, 110, beim("bescheid", "schließt"), fuell=WEISS),
    pl("Schließung, bis die Mäuse bekämpft sind", 1250, 150, beim("bescheid", "schließt"), fill=WEISS, size=30, anker="m", bis="hi1"),
    pl("sofortige Vollziehung angeordnet", 1250, 220, beim("bescheid", "sofortige"), fill=ROT, size=30, anker="m", bis="hi1"),
    pl("Grund: Gesundheit der Gäste", 1250, 290, beim("bescheid", "Gesundheit"), fill=WEISS, size=30, anker="m", bis="hi1"),
    blase("sprech", 820, 200, "hi1", 1300, 190, inhalt=["20 Jahre ohne Beanstandung! Ich klage", "dagegen, dann darf ich doch weiter öffnen."],
          textsize=29, figur=HIb, bis="klage"),
])

# B Die Klage und die Frage --------------------------------------------------------------------------------------------------
GERICHT = beim("klage", "Verwaltungsgericht")
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Darf er wieder öffnen?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Die Klage", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 560, BODEN - 2, 420, "klage", fuell=WEISS),
    pl("Verwaltungsgericht", 560, 330, GERICHT, fill=WEISS, size=34, anker="m"),
    ficon("tabler", "file-text", 1000, 640, 100, beim("klage", "Klage"), fuell=WEISS),
    pl("Klage", 1000, 660, beim("klage", "Klage"), fill=GRUEN, size=30, anker="m"),
    *fig("HI", 1200, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Herr Hinrichs", 1200, "klage", HI_F, unten=BODEN),
    pl("Darf er jetzt wieder öffnen?", 1250, 150, "frage", fill=PINK, size=44, anker="m"),
    pl("Und was kann er sofort tun?", 1250, 240, beim("frage", "Und"), fill=WEISS, size=36, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Hinrichs betreibt seit 20 Jahren eine Imbissbude. Bei einer Kontrolle findet Frau Steinke von der "
    "Lebensmittelüberwachung der Stadt Mäusekot auf der Arbeitsfläche und angenagte Brötchentüten; Herr Hinrichs kann sich "
    "dazu äußern. Am nächsten Tag erhält er den schriftlichen Bescheid: Die Stadt schließt den Imbiss, bis die Mäuse "
    "bekämpft sind und eine Nachkontrolle das bestätigt. Sie ordnet die sofortige Vollziehung an und begründet das "
    "schriftlich: Die Gesundheit der Gäste könne nicht bis zum Ende eines Prozesses warten. Herr Hinrichs erhebt Klage "
    "beim Verwaltungsgericht.",
], "Darf er jetzt wieder öffnen? Und was kann er sofort tun?")

# D Grundsatz § 80 I 1 -----------------------------------------------------------------------------------------------------------
W801 = "„Widerspruch und Anfechtungsklage haben aufschiebende Wirkung.“"
w801, w801_y = wortlaut(80, 175, 1100, W801, "§ 80 Abs. 1 Satz 1 VwGO", "wl801", size=38,
                        zeilen=["„Widerspruch und Anfechtungsklage haben", "aufschiebende Wirkung.“"],
                        marken=[("aufschiebende Wirkung", beim("wl801", "aufschiebende"))])
folie([("wl801", "Grundsatz · Aufschiebende Wirkung, § 80 I 1 VwGO")], rechts_frei([
    titel(glyphen("Der Grundsatz"), 110, 75, "wl801", 50),
    *w801,
    z("solange sie besteht: Die Behörde darf den", 110, w801_y + 45, beim("aw", "Solange"), "Bold", 36),
    z("Bescheid nicht vollziehen", 110, w801_y + 100, beim("aw", "vollziehen"), "Bold", 36),
    z("Herr Hinrichs hätte also recht, wenn es dabei bliebe", 110, w801_y + 200, beim("aw2", "Herr"), size=34),
    ficon("tabler", "hand-stop", IX, IU, 130, "wl801", fuell=GRUEN),
    pl("aufschiebende Wirkung", IX, 190, beim("wl801", "aufschiebende"), fill=GRUEN, size=28, anker="m"),
    *fig("HI", FX, FB, FR, [("wl801", "ruhig"), ("aw2", "froh")]),
    schild("Herr Hinrichs", FX, "wl801", HI_F),
]))

# E Entfallen § 80 II 1 ----------------------------------------------------------------------------------------------------------
W804 = ("„Die aufschiebende Wirkung entfällt nur … 4. in den Fällen, in denen die sofortige Vollziehung im öffentlichen "
        "Interesse oder im überwiegenden Interesse eines Beteiligten von der Behörde, die den Verwaltungsakt erlassen oder "
        "über den Widerspruch zu entscheiden hat, besonders angeordnet wird.“")
Z804 = ["„Die aufschiebende Wirkung entfällt nur … 4. in den Fällen,",
        "in denen die sofortige Vollziehung im öffentlichen Interesse",
        "oder im überwiegenden Interesse eines Beteiligten von der",
        "Behörde, die den Verwaltungsakt erlassen oder über den",
        "Widerspruch zu entscheiden hat, besonders angeordnet wird.“"]
w804, w804_y = wortlaut(80, 285, 1100, W804, "§ 80 Abs. 2 Satz 1 Nr. 4 VwGO (Auszug)", "nr4", size=32, zeilen=Z804,
                        marken=[("besonders angeordnet", beim("nr4", "besonders"))])
folie([("wl802", "Entfallen · § 80 II 1 VwGO"), ("nr4", "Entfallen · § 80 II 1 Nr. 4 VwGO")], rechts_frei([
    titel(glyphen("Wann die aufschiebende Wirkung entfällt"), 110, 75, "wl802", 42),
    z("Nr. 1 bis 3a: kraft Gesetzes, z. B. öffentliche Abgaben und Kosten", 110, 170, beim("nr13", "Nummern"), size=32),
    *w804,
    blk(110, w804_y + 30, 1040, 80, ROT, beim("hier", "Genau"), [("hier: Anordnung der Stadt", "ExtraBold", 38, INK)]),
    z("Die Klage hält die Schließung nicht auf.", 110, w804_y + 140, beim("hier", "Klage"), "Bold", 34),
    ficon("tabler", "hand-stop", IX, IU, 130, "wl802", fuell=GRUEN),
    nein(IX + 80, IU - 70, beim("hier", "Klage"), gr=34),
    *fig("HI", FX, FB, FR, [("wl802", "denkt"), (beim("hier", "Klage"), "sorge")]),
    schild("Herr Hinrichs", FX, "wl802", HI_F),
]))

# F Antrag § 80 V 1 -------------------------------------------------------------------------------------------------------------
W805 = ("„Auf Antrag kann das Gericht der Hauptsache die aufschiebende Wirkung in den Fällen des Absatzes 2 Satz 1 Nummer 1 "
        "bis 3a ganz oder teilweise anordnen, im Falle des Absatzes 2 Satz 1 Nummer 4 ganz oder teilweise wiederherstellen.“")
Z805 = ["„Auf Antrag kann das Gericht der Hauptsache die",
        "aufschiebende Wirkung in den Fällen des Absatzes 2 Satz 1",
        "Nummer 1 bis 3a ganz oder teilweise anordnen, im Falle des",
        "Absatzes 2 Satz 1 Nummer 4 ganz oder teilweise wiederherstellen.“"]
w805, w805_y = wortlaut(80, 175, 1100, W805, "§ 80 Abs. 5 Satz 1 VwGO", "wl805", size=32, zeilen=Z805,
                        marken=[("anordnen,", beim("wl805", "anordnen")), ("wiederherstellen.“", beim("wl805", "wiederherstellen"))])
folie([("wl805", "Rechtsschutz · Antrag nach § 80 V 1 VwGO")], rechts_frei([
    titel(glyphen("Der Antrag ans Gericht"), 110, 75, "wl805", 50),
    *w805,
    z("Nr. 1 bis 3a: Anordnung", 110, w805_y + 40, beim("wl805", "anordnen"), "Bold", 36),
    z("Nr. 4: Wiederherstellung", 110, w805_y + 100, beim("wl805", "wiederherstellen"), "Bold", 36),
    blk(110, w805_y + 180, 1040, 132, GRUEN, beim("antrag", "beantragt"),
        [("Antrag: die aufschiebende Wirkung", "ExtraBold", 36, INK), ("der Klage wiederherstellen", "ExtraBold", 36, INK)]),
    ficon(HC, "classical-building", IX, IU, 150, "wl805", fuell=WEISS),
    pl("Verwaltungsgericht", IX, 190, beim("antrag", "Verwaltungsgericht"), fill=WEISS, size=28, anker="m"),
    *fig("HI", FX, FB, FR, [("wl805", "denkt"), ("antrag", "ruhig")]),
    schild("Herr Hinrichs", FX, "wl805", HI_F),
]))

# G A. Zulässigkeit I.–II. ------------------------------------------------------------------------------------------------------
folie([("zul", f"{ZU} › I. Verwaltungsrechtsweg, § 40 I 1 VwGO"), ("statt", f"{ZU} › II. Statthaftigkeit")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("I. Verwaltungsrechtsweg, § 40 Abs. 1 Satz 1 VwGO", 110, 180, "rweg", "Bold", 36),
    z("Lebensmittelrecht ermächtigt allein Behörden:", 150, 240, beim("rweg", "Lebensmittelrecht"), size=34),
    z("öffentliches Recht", 150, 292, beim("rweg", "öffentliches"), size=34),
    ok(120, 315, beim("rweg", "öffentliches"), gr=18),
    z("II. Statthaftigkeit", 110, 385, "statt", "Bold", 36),
    z("Hauptsache: Anfechtungsklage, denn die Schließung", 150, 445, beim("statt", "Hauptsache"), size=34),
    z("ist ein belastender Verwaltungsakt", 150, 497, beim("statt", "belastender"), size=34),
    blk(110, 570, 1040, 80, BLAU, beim("statt2", "Paragraf"), [("also § 80 Abs. 5 VwGO", "ExtraBold", 36, INK)]),
    z("nicht die einstweilige Anordnung nach § 123 VwGO", 150, 675, beim("statt2", "einstweilige"), size=34),
    zit("§ 123 Abs. 5 VwGO", 150, 728, beim("statt2", "hundertdreiundzwanzig")),
    ficon(HC, "classical-building", IX, IU, 150, "zul", fuell=WEISS),
    *fig("HI", FX, FB, FR, [("zul", "ruhig"), ("statt2", "denkt")]),
    schild("Herr Hinrichs", FX, "zul", HI_F),
]))

# H A. Zulässigkeit III.–V. -----------------------------------------------------------------------------------------------------
folie([("befugt", f"{ZU} › III. Antragsbefugnis, § 42 II VwGO analog"), ("gegner", f"{ZU} › IV. Antragsgegner, § 78 VwGO analog"),
       ("rsb", f"{ZU} › V. Rechtsschutzbedürfnis")], rechts_frei([
    *tafel("befugt", "A. Zulässigkeit"),
    z("III. Antragsbefugnis, § 42 Abs. 2 VwGO analog", 110, 170, "befugt", "Bold", 34),
    z("Adressat: möglicherweise in der Berufsfreiheit verletzt", 150, 222, beim("befugt", "Adressat"), size=30),
    zit("Art. 12 Abs. 1 GG", 150, 268, beim("befugt", "Berufsfreiheit")),
    z("IV. Antragsgegner, § 78 VwGO analog", 110, 325, "gegner", "Bold", 34),
    z("die Stadt als Rechtsträgerin, wenn dein Land", 150, 377, beim("gegner", "Stadt"), size=30),
    z("nichts anderes bestimmt", 150, 420, beim("gegner", "Land"), size=30),
    z("V. Rechtsschutzbedürfnis", 110, 482, "rsb", "Bold", 34),
    z("Rechtsbehelf eingelegt oder noch möglich", 150, 534, beim("rsb", "Rechtsbehelf"), size=30),
    z("Antrag schon vor der Klage zulässig, § 80 Abs. 5 Satz 2", 150, 577, beim("rsb", "Antrag"), size=30),
    ok(120, 641, "rsb2", gr=18),
    z("Herr Hinrichs hat geklagt.", 150, 620, "rsb2", size=30),
    z("Antrag bei der Behörde nur bei Abgaben und Kosten, § 80 Abs. 6", 150, 663, beim("abs6", "Einen"), size=30),
    blk(110, 735, 1040, 80, GRUEN, beim("zul2", "zulässig"), [("Der Antrag ist zulässig.", "ExtraBold", 38, INK)]),
    ok(1100, 775, beim("zul2", "zulässig"), gr=26),
    ficon("tabler", "building", IX, IU, 140, "gegner", fuell=WEISS),
    pl("Stadt", IX, 190, beim("gegner", "Stadt"), fill=GRUEN, size=30, anker="m"),
    *fig("HI", FX, FB, FR, [("befugt", "ruhig"), ("zul2", "froh")]),
    schild("Herr Hinrichs", FX, "befugt", HI_F),
]))

# I B. I. formelle Rechtmäßigkeit der Anordnung ------------------------------------------------------------------------------------
FO = f"{BG} › I. formelle Rechtmäßigkeit der Anordnung"
folie([("begr", FO), ("anh", f"{FO} › Anhörung?")], rechts_frei([
    *tafel("begr", "B. I. Formelle Rechtmäßigkeit der Anordnung", size=40),
    z("1. Zuständigkeit: Behörde des Bescheids, hier die Stadt", 110, 165, beim("zust", "Zuständig"), "Bold", 32),
    zit("§ 80 Abs. 2 Satz 1 Nr. 4 VwGO", 150, 212, beim("zust", "Stadt")),
    z("2. Begründung, § 80 Abs. 3 Satz 1 VwGO:", 110, 268, beim("abs3", "Nach"), "Bold", 32),
    z("besonderes Interesse schriftlich, bezogen auf den Einzelfall", 150, 315, beim("abs3", "schriftlich"), size=30),
    zit("OVG NRW, Beschl. v. 12.7.2024 – 4 B 1116/23, Rn. 8", 150, 360, beim("abs3", "Einzelfall")),
    z("ob die Gründe inhaltlich tragen: hier noch egal", 150, 410, beim("inhalt", "Ob"), size=30),
    zit("OVG NRW, Beschl. v. 17.2.2025 – 7 B 34/25, Rn. 3", 150, 455, beim("inhalt", "Rolle")),
    z("fehlt sie: Anordnung formell rechtswidrig", 150, 505, beim("fehlt", "Fehlt"), size=30),
    zit("OVG NRW, 4 B 1116/23, Rn. 7", 150, 550, beim("fehlt", "rechtswidrig")),
    ok(120, 625, beim("gaeste", "genügt"), gr=18),
    z("Stadt: Gesundheit der Gäste in diesem Imbiss", 150, 602, beim("gaeste", "Gesundheit"), "Bold", 30),
    z("3. Anhörung vor der Anordnung? umstritten", 110, 680, beim("anh", "Ob"), "Bold", 32),
    z("Herr Hinrichs konnte sich ohnehin äußern", 150, 730, beim("anh", "Herr"), size=30),
    ok(120, 753, beim("anh", "äußern"), gr=18),
    ficon("tabler", "file-text", IX, IU, 120, "begr", fuell=WEISS),
    pl("sofortige Vollziehung", IX, 180, "begr", fill=ROT, size=28, anker="m"),
    *fig("ST", FX, FB, FR, [("begr", "ruhig"), ("anh", "denkt")]),
    schild("Frau Steinke, Lebensmittelüberwachung", FX, "begr", ST_F),
]))

# J B. II. Interessenabwägung -----------------------------------------------------------------------------------------------------
IA = f"{BG} › II. Interessenabwägung"
folie([("abw", IA), ("fg1", f"{IA} › Erfolgsaussichten"), ("fg3", f"{IA} › Folgenabwägung")], rechts_frei([
    *tafel("abw", "B. II. Interessenabwägung"),
    z("eigene Abwägung des Gerichts:", 110, 170, beim("abw", "wägt"), "Bold", 34),
    z("Aussetzungsinteresse gegen Vollzugsinteresse", 150, 222, beim("abw", "Aussetzungsinteresse"), size=32),
    z("wesentlich: Erfolgsaussichten der Klage, summarisch", 110, 285, beim("eaus", "Erfolgsaussichten"), "Bold", 32),
    zit("BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8", 150, 333, beim("eaus", "summarisch")),
    blk(110, 385, 1040, 76, ROT, beim("fg1", "offensichtlich"),
        [("offensichtlich rechtswidrig: Aussetzungsinteresse", "ExtraBold", 32, INK)]),
    blk(110, 478, 1040, 126, GRUEN, beim("fg2", "offensichtlich"),
        [("offensichtlich rechtmäßig: bei Nr. 4 zusätzlich", "ExtraBold", 32, INK),
         ("besonderes Vollzugsinteresse", "ExtraBold", 32, INK)]),
    zit("OVG NRW, 4 B 1116/23, Rn. 43", 150, 612, beim("fg2", "Prozesses")),
    blk(110, 650, 1040, 76, GELB, beim("fg3", "offen"), [("offen: Folgenabwägung", "ExtraBold", 32, INK)]),
    zit("OVG NRW, Beschl. v. 16.1.2020 – 15 B 814/19, Rn. 9", 150, 738, beim("fg3", "Folgenabwägung")),
    ficon(HC, "balance-scale", IX, IU, 160, "abw", fuell=WEISS),
    pl("Aussetzung", IX - 110, 170, beim("abw", "Aussetzungsinteresse"), fill=PINK, size=28, anker="m"),
    pl("Vollzug", IX + 130, 170, beim("abw", "Vollzugsinteresse"), fill=BLAU, size=28, anker="m"),
    *fig("HI", FX, FB, FR, [("abw", "denkt")]),
    schild("Herr Hinrichs", FX, "abw", HI_F),
]))

# K Erfolgsaussichten im Fall (Wortlaut Art. 138 II h) ------------------------------------------------------------------------------
W138 = ("„sie ordnen an, dass das ganze Unternehmen oder ein Teil des Unternehmens des betreffenden Unternehmers oder seine "
        "Betriebe … für einen angemessenen Zeitraum isoliert oder geschlossen werden;“")
Z138 = ["„sie ordnen an, dass das ganze Unternehmen oder ein Teil des",
        "Unternehmens des betreffenden Unternehmers oder seine",
        "Betriebe … für einen angemessenen Zeitraum isoliert oder",
        "geschlossen werden;“"]
w138, w138_y = wortlaut(80, 230, 1100, W138, "Art. 138 Abs. 2 Buchst. h VO (EU) 2017/625 (Auszug)", "egl", size=32, zeilen=Z138,
                        marken=[("angemessenen Zeitraum", beim("egl", "angemessenen")), ("geschlossen werden;“", beim("egl", "schließen"))])
EA = f"{BG} › II. Interessenabwägung › Erfolgsaussichten im Fall"
folie([("egl", EA)], rechts_frei([
    titel(glyphen("Im Fall: die Erfolgsaussichten"), 110, 75, "egl", 46),
    z("Rechtsgrundlage: EU-Kontrollverordnung, bei festgestelltem Verstoß", 110, 165, beim("egl", "Rechtsgrundlage"), size=30),
    *w138,
    z("Verstoß: Hygieneregeln der EU", 110, w138_y + 25, beim("hyg", "Mäusekot"), "Bold", 32),
    z("Küche sauber halten, Schädlinge bekämpfen", 150, w138_y + 72, beim("hyg", "sauber"), size=30),
    zit("Art. 4 Abs. 2, Anhang II Kap. I Nr. 1, Kap. IX Nr. 4 VO (EG) Nr. 852/2004", 150, w138_y + 115, beim("hyg", "bekämpfen")),
    z("bloße Reinigung reicht nicht; Schließung nur bis zur Bekämpfung", 110, w138_y + 170, beim("verh", "Eine"), size=30),
    blk(110, w138_y + 230, 1040, 76, GRUEN, beim("offen", "offensichtlich"),
        [("offensichtlich rechtmäßig", "ExtraBold", 36, INK)]),
    ok(1100, w138_y + 268, beim("offen", "rechtmäßig"), gr=24),
    ficon(HC, "mouse", IX, IU, 120, "egl", fuell=WEISS),
    pl("Mäusekot in der Küche", IX, 180, beim("hyg", "Mäusekot"), fill=ROT, size=28, anker="m"),
    *fig("HI", FX, FB, FR, [("egl", "denkt"), ("offen", "sorge")]),
    schild("Herr Hinrichs", FX, "egl", HI_F),
]))

# L besonderes Vollzugsinteresse -------------------------------------------------------------------------------------------------
folie([("eilig", f"{BG} › II. Interessenabwägung › besonderes Vollzugsinteresse")], rechts_frei([
    *tafel("eilig", "Besonderes Vollzugsinteresse"),
    z("jeden Tag essen Gäste aus dieser Küche", 110, 200, beim("eilig", "Jeden"), "Bold", 36),
    z("ihr Schutz kann nicht bis zum Ende des Prozesses warten", 110, 270, beim("eilig", "Ihr"), size=32),
    blk(110, 360, 1040, 80, GRUEN, beim("eilig", "warten"), [("Vollzugsinteresse überwiegt", "ExtraBold", 38, INK)]),
    ficon("tabler", "users", IX, IU, 140, "eilig", fuell=WEISS),
    pl("Gäste", IX, 190, beim("eilig", "Gäste"), fill=WEISS, size=28, anker="m"),
    *fig("ST", FX, FB, FR, [("eilig", "ruhig")]),
    schild("Frau Steinke, Lebensmittelüberwachung", FX, "eilig", ST_F),
]))

# M Der Beschluss --------------------------------------------------------------------------------------------------------------------
RIX, HIX2 = 1320, 620
RIb = ("RI_redet", RIX, BODEN, FH)
folie([("urteil", "Ergebnis · Der Beschluss")], [
    linienzug([(60, BODEN), (1860, BODEN)], "urteil", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "urteil", fill=GELB, size=40),
    ficon(HC, "balance-scale", 960, 700, 150, "urteil", fuell=WEISS),
    *fig("HI", HIX2, BODEN, FH, [("urteil", "denkt_r"), (beim("ri1", "abgelehnt"), "muede_r")]),
    schild("Herr Hinrichs", HIX2, "urteil", HI_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [(beim("urteil", "Verwaltungsgericht"), "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "ende"),
    schild("die Richterin", RIX, beim("urteil", "Verwaltungsgericht"), RI_F, unten=BODEN, d=0.0),
    blase("sprech", 700, 200, "ri1", 1240, 200, inhalt=["Der Antrag ist zulässig, aber", "unbegründet. Er wird abgelehnt."],
          textsize=30, figur=RIb),
    pl("zulässig, aber unbegründet", 960, 740, beim("ri1", "unbegründet"), fill=ROT, size=30, anker="m"),
])

# N Nachkontrolle: zurück am Imbiss -------------------------------------------------------------------------------------------------
folie([("ende", "Ergebnis · Die Nachkontrolle")], [
    linienzug([(60, BODEN), (1860, BODEN)], "ende", breite=7, farbe=INK),
    pl("Nach der Schädlingsbekämpfung", 70, 40, "ende", fill=GELB, size=40),
    *imbiss(BUX, "ende"),
    ficon("tabler", "lock", BUX, BODEN - 150, 110, "ende", fuell=WEISS, bis=beim("ende", "Nachkontrolle")),
    pl("Mäuse bekämpft", BUX, 300, beim("ende", "bekämpfen"), fill=GRUEN, size=30, anker="m"),
    *fig("HI", HIX, BODEN, FH, [("ende", "ruhig_r"), (beim("ende", "öffnen"), "froh_r")]),
    schild("Herr Hinrichs, Imbiss", HIX, "ende", HI_F, unten=BODEN),
    *fig("ST", STX, BODEN, FH, [(beim("ende", "Nachkontrolle"), "ruhig")]),
    schild("Frau Steinke, Lebensmittelüberwachung", STX, beim("ende", "Nachkontrolle"), ST_F, unten=BODEN),
    ficon("tabler", "clipboard-check", STX - 150, 640, 80, beim("ende", "Nachkontrolle"), fuell=WEISS),
    ok(STX - 150, 560, beim("ende", "öffnen"), gr=30),
    pl("wieder geöffnet", 1250, 200, beim("ende", "öffnen"), fill=GRUEN, size=34, anker="m"),
])

# O Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Anordnung oder Wiederherstellung?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("zuerst: Warum entfällt die aufschiebende Wirkung?", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("Behörde hat angeordnet: Wiederherstellung", 200, 290, beim("tipp1", "Wiederherstellung"), size=34),
    z("sonst: Anordnung", 200, 345, beim("tipp1", "Anordnung"), size=34),
    z("Vorsicht im Lebensmittelrecht: § 39 Abs. 7 LFGB", 200, 440, beim("tipp2", "Vorsicht"), "Bold", 34),
    z("bestimmte Anordnungen schon kraft Gesetzes", 200, 495, beim("tipp2", "bestimmte"), size=34),
    z("ohne aufschiebende Wirkung", 200, 550, beim("tipp2", "keine"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# P Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 34, 64
LX0, RX0 = 110, 1000
links = [("s1", "I. Verwaltungsrechtsweg, § 40 I 1"), ("s2", "II. Statthaftigkeit: § 80 V, nicht § 123"),
         ("s3", "III. Antragsbefugnis, § 42 II analog"), ("s4", "IV. Antragsgegner, § 78 analog"),
         ("s5", "V. Rechtsschutzbedürfnis")]
rechts_ = [("s6", "I. formelle Rechtmäßigkeit der", "Bold"), ("s6", "Anordnung, § 80 III 1", "Bold"),
           ("s7", "II. Interessenabwägung:", "Bold"), ("s8", "1. Erfolgsaussichten", "Regular"),
           ("s9", "2. besonderes Vollzugsinteresse", "Regular"), ("s10", "3. Folgenabwägung", "Regular")]
els_t = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: § 80 V VwGO"), 110, 85, "sch", 46),
         z("A. Zulässigkeit", LX0, 190, "sa", "ExtraBold", 38, rechts=980),
         z("B. Begründetheit", RX0, 190, "sb", "ExtraBold", 38, rechts=1820)]
for i, (c, t) in enumerate(links):
    els_t.append(z(t, LX0 + 30, 265 + i * LH, c, size=SZ, rechts=980))
for i, (c, t, s) in enumerate(rechts_):
    els_t.append(z(t, RX0 + (30 if s == "Bold" else 70) + (40 if t.startswith("Anordnung") else 0), 265 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · § 80 V VwGO")], els_t)

# Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Behörde hat die sofortige Vollziehung ", 0), ("angeordnet:", "a")]], 750, 320, 42, "merke",
                {"a": beim("merke", "angeordnet")}),
    *markertext([[("Gericht ", 0), ("stellt", "b"), (" die aufschiebende Wirkung ", 0), ("wieder her,", "c")]], 750, 385, 42,
                beim("merke", "stellt"), {"b": beim("merke", "stellt"), "c": beim("merke", "wieder")}),
    *markertext([[("sonst ", 0), ("ordnet", "d"), (" es sie an.", 0)]], 750, 450, 42, beim("merke", "sonst"),
                {"d": beim("merke", "ordnet")}),
    *markertext([[("Entscheidend: die ", 0), ("Interessenabwägung,", "e")]], 750, 590, 42, "m2",
                {"e": beim("m2", "Interessenabwägung")}),
    *markertext([[("vor allem nach den ", 0), ("Erfolgsaussichten", "f")]], 750, 655, 42, beim("m2", "vor"),
                {"f": beim("m2", "Erfolgsaussichten")}),
    *markertext([[("in der Hauptsache.", 0)]], 750, 720, 42, beim("m2", "Hauptsache"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
