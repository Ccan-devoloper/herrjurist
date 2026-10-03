"""Folge 090 · Drittanfechtung Baugenehmigung: Eilrechtsschutz nach §§ 80a, 80 V VwGO – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Nachbarin, Rohbau mit 4 Geschossen, Abstandsflächen verletzt), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Baustelle (Rohbau wächst, Blasen Dorn/Weber, Klage), B Kanzlei (Falk), C Sachverhalt, D Problem § 80 I 1 / § 212a I BauGB
(Wortlaut), E Antrag § 80a III (Wortlaut), F A. Zulässigkeit I.–II., G III. Rechtsschutzbedürfnis, § 80 VI, Beiladung,
H B. Interessenabwägung im Dreieck, I Prüfungsmaßstab drittschützende Normen, J Abstandsflächen (Skizze), K Tenor,
L Baustelle: Baustopp und Sicherungsmaßnahmen, M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Mauern am Rohbau)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_090/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_090/" in n:
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




def rechteck(x, y, w, h, fill, cue, bis=None, rand=4, rund=6, anim="pop", d=0.0, name="rechteck"):
    """Fläche einer Skizze (Tafelbaustein, kein Requisit): Palettenfarbe mit Tuschekontur."""
    im = Image.new("RGBA", (int(w) + 2, int(h) + 2))
    ImageDraw.Draw(im).rounded_rectangle((1, 1, int(w), int(h)), rund, fill=fill, outline=INK, width=rand)
    return El(im, x, y, cue, anim, d, bis, name=name)


def skizze(e):
    """Icon als Teil der Tafelskizze (darf in der Tafel stehen; rechts_frei() prüft nur freie Requisiten)."""
    e.name = "skizze:" + e.name.split(":", 1)[1]
    return e


def strichlinie(x, y0, y1, cue, bis=None, breite=5, strich=22, luecke=14):
    """Senkrechte gestrichelte Linie (Grundstücksgrenze)."""
    im = Image.new("RGBA", (breite + 2, int(y1 - y0) + 2))
    dr = ImageDraw.Draw(im); y = 0
    while y < y1 - y0:
        dr.line([(1 + breite / 2, y), (1 + breite / 2, min(y + strich, y1 - y0))], fill=INK, width=breite); y += strich + luecke
    return El(im, x - breite / 2, y0, cue, "fade", 0.0, bis, name="grenze")


def schatten_flaeche(x0, x1, y0, y1, cue, bis=None):
    """Schatten des Rohbaus über dem Haus von Frau Dorn (Lichtwirkung, kein Requisit)."""
    im = Image.new("RGBA", (x1 - x0, y1 - y0))
    ImageDraw.Draw(im).polygon([(0, im.height), (im.width, 0), (im.width, im.height)], fill=(40, 40, 70, 60))
    return El(im, x0, y0, cue, "fade", 0.0, bis, name="schatten")


BODEN, FH = 880, 430
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
DO_F, WE_F, FA_F = GRUEN, ORANGE, BLAU      # Farben der Namensschilder
ZU = "A. Zulässigkeit"
BG = "B. Begründetheit"
HAUSX, DOX, GRX, ROX, WEX = 290, 640, 820, 1090, 1600
WALL = 150                                  # Breite eines Mauerstücks (Tabler „wall“), 2 Spalten je Geschoss


def haus(cue, anim="pop", bis=None):
    """Haus mit Garten von Frau Dorn: Fluent HC „house-with-garden“ (gelb) – in jeder Baustellenszene gleich."""
    return ficon(HC, "house-with-garden", HAUSX, BODEN - 2, 330, cue, fuell=GELB, anim=anim, bis=bis)


def geschoss(n, cue, anim="pop", d=0.0, bis=None):
    """n-tes Geschoss (1 = Erdgeschoss) des Rohbaus aus zwei Mauerstücken (Tabler „wall“, rot gefüllt)."""
    unten = BODEN - 2 - (n - 1) * WALL
    return [ficon("tabler", "wall", ROX - WALL / 2 + 2, unten, WALL, cue, fuell=ROT, anim=anim, d=d, bis=bis),
            ficon("tabler", "wall", ROX + WALL / 2 - 2, unten, WALL, cue, fuell=ROT, anim=anim, d=d, bis=bis)]


# A Fall: Haus, Rohbau, Blasen, Klage ----------------------------------------------------------------------------------------------
DOa = ("DO_redet_r", DOX, BODEN, FH)
WEa = ("WE_redet", WEX, BODEN, FH)
folie([(NULL, "Fall · Das Haus mit Garten"), ("bau", "Fall · Der Rohbau nebenan"), ("licht", "Fall · Kein Tageslicht mehr"),
       ("do1", "Fall · Zu nah an der Grenze?"), ("klage", "Fall · Die Klage"), ("weiter", "Fall · Es wird weiter gebaut")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    ficon("tabler", "sun", 1480, 175, 120, NULL, fuell=GELB, anim="cut"),
    hart(haus(NULL, anim="cut")),
    hart(bis_(pl("Frau Dorn: kleines Haus mit Garten", 70, 40, NULL, fill=GELB, size=36), "bau")),
    *fig("DO", DOX, BODEN, FH, [(NULL, "ruhig_r"), (beim("licht", "Tageslicht"), "sorge_r")], bis="do1", erst="cut"),
    *redet("DO_redet_r", DOX, BODEN, FH, "do1", "we1"),
    *fig("DO", DOX, BODEN, FH, [("we1", "aerger_r"), ("klage", "denkt_r")], bis="kanzlei"),
    hart(schild("Frau Dorn, Nachbarin", DOX, NULL, DO_F, unten=BODEN, d=0.0)),
    # Rohbau wächst: drei Geschosse stehen, das vierte ist geplant und wird ab „weiter“ gemauert
    *geschoss(1, beim("bau", "Rohbau")), *geschoss(2, beim("bau", "Rohbau"), d=0.25), *geschoss(3, beim("bau", "Rohbau"), d=0.5),
    pl("Rohbau nebenan", 70, 40, beim("bau", "Rohbau"), fill=GELB, size=36, bis="klage"),
    rechteck(ROX - WALL + 2, BODEN - 2 - 4 * WALL, 2 * WALL - 4, WALL, (255, 255, 255, 120), beim("bau", "Vier"), bis="weiter",
             name="geplant"),
    pl("geplant: 4 Geschosse", ROX, BODEN - 4 * WALL - 70, beim("bau", "Vier"), fill=WEISS, size=30, anker="m", bis="weiter"),
    schatten_flaeche(110, ROX - WALL, BODEN - 3 * WALL - 20, BODEN, beim("licht", "Schon"), bis="kanzlei"),
    pl("fast das ganze Tageslicht weg", HAUSX, 470, beim("licht", "Tageslicht"), fill=WEISS, size=30, anker="m", bis="klage"),
    strichlinie(GRX, BODEN - 330, BODEN, beim("do1", "Grenze")),
    pl("Grenze", GRX, BODEN - 385, beim("do1", "Grenze"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 700, 160, "do1", 520, 255, inhalt=["Das steht doch viel zu nah", "an meiner Grenze!"], textsize=30,
          figur=DOa, bis="we1"),
    *fig("WE", WEX, BODEN, FH, [(beim("bau", "Herrn"), "ruhig")], bis="we1"),
    *redet("WE_redet", WEX, BODEN, FH, "we1", "klage"),
    *fig("WE", WEX, BODEN, FH, [("klage", "ruhig")], bis="kanzlei"),
    schild("Herr Weber, Bauherr", WEX, beim("bau", "Herrn"), WE_F, unten=BODEN, d=0.0),
    ficon("tabler", "file-certificate", WEX - 175, 640, 80, beim("we1", "Baugenehmigung"), fuell=WEISS, bis="kanzlei"),
    blase("sprech", 640, 160, "we1", 1560, 320, inhalt=["Ich habe eine Baugenehmigung", "der Stadt. Ich baue weiter."],
          textsize=30, figur=WEa, bis="klage"),
    ficon(HC, "classical-building", 760, 420, 120, beim("klage", "Verwaltungsgericht"), fuell=WEISS, bis="kanzlei"),
    pl("Klage beim Verwaltungsgericht", 70, 120, beim("klage", "Klage"), fill=GRUEN, size=32, bis="kanzlei"),
    pl("NRW: ohne Widerspruch", 70, 195, beim("klage", "Nordrhein-Westfalen"), fill=WEISS, size=30, bis="kanzlei"),
    pl("in deinem Land ggf. Widerspruch", 70, 260, beim("klage", "deinem"), fill=WEISS, size=30, bis="kanzlei"),
    *geschoss(4, beim("weiter", "gemauert"), anim="cut"),
    szene(ficon("tabler", "trowel", ROX + WALL + 60, BODEN - 3 * WALL - 10, 90, beim("weiter", "gemauert"), fuell=GELB,
                bis="kanzlei"), "090mauer*", 0.7, 0.0),
    pl("Es wird weiter gemauert.", ROX, 150, beim("weiter", "gemauert"), fill=ROT, size=30, anker="m", bis="kanzlei"),
])

# B Kanzlei ---------------------------------------------------------------------------------------------------------------------
DOK, FAK = 620, 1300
FAb = ("FA_redet", FAK, BODEN, FH)
folie([("kanzlei", "Fall · In der Kanzlei"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "kanzlei", breite=7, farbe=INK),
    pl("In der Kanzlei", 70, 40, "kanzlei", fill=GELB, size=36),
    ficon("tabler", "desk", 960, BODEN - 2, 300, "kanzlei", fuell=GELB),
    ficon("tabler", "briefcase", 1560, BODEN - 2, 110, "kanzlei", fuell=BLAU),
    ficon("tabler", "file-certificate", 900, BODEN - 175, 70, "kanzlei", fuell=WEISS),
    *fig("DO", DOK, BODEN, FH, [("kanzlei", "sorge_r"), ("frage", "denkt_r")]),
    schild("Frau Dorn", DOK, "kanzlei", DO_F, unten=BODEN),
    *fig("FA", FAK, BODEN, FH, [(beim("kanzlei", "Rechtsanwalt"), "ruhig")], bis="fa1"),
    *redet("FA_redet", FAK, BODEN, FH, "fa1", "frage"),
    *fig("FA", FAK, BODEN, FH, [("frage", "denkt")]),
    schild("Rechtsanwalt Falk", FAK, beim("kanzlei", "Rechtsanwalt"), FA_F, unten=BODEN, d=0.0),
    blase("sprech", 720, 160, "fa1", 1180, 260, inhalt=["Ihre Klage allein stoppt den Bau nicht.", "Wir brauchen einen Eilantrag."],
          textsize=30, figur=FAb, bis="frage"),
    pl("Warum hält die Klage den Bau nicht auf?", 960, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Wie prüfst du den Eilantrag in der Anwaltsklausur?", 960, 240, beim("frage", "Und"), fill=WEISS, size=34, anker="m"),
])

# C Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Dorn wohnt in einem kleinen Haus mit Garten. Ringsum stehen zweigeschossige Häuser; einen Bebauungsplan gibt "
    "es nicht. Die Stadt erteilt Herrn Weber die Baugenehmigung für ein Mehrfamilienhaus mit 4 Geschossen auf dem "
    "Nachbargrundstück. Die Hauswand zu Frau Dorn ist 12,5 m hoch und steht 3 m vor ihrer Grenze; eine Abweichung von "
    "den Abstandsflächen hat die Stadt nicht zugelassen.",
    "Herr Weber baut sofort. Frau Dorn erhebt Klage beim Verwaltungsgericht (in NRW ohne Widerspruch). Herr Weber baut "
    "weiter; Frau Dorn geht zu Rechtsanwalt Falk.",
], "Warum hält die Klage den Bau nicht auf? Wie prüfst du den Eilantrag?")

# D Problem: § 80 I 1, § 212a I BauGB ------------------------------------------------------------------------------------------------
W212 = ("„Widerspruch und Anfechtungsklage eines Dritten gegen die bauaufsichtliche Zulassung eines Vorhabens haben "
        "keine aufschiebende Wirkung.“")
w212, w212_y = wortlaut(80, 250, 1100, W212, "§ 212a Abs. 1 BauGB", "wl212", size=36,
                        zeilen=["„Widerspruch und Anfechtungsklage eines Dritten", "gegen die bauaufsichtliche Zulassung eines",
                                "Vorhabens haben keine aufschiebende Wirkung.“"],
                        marken=[("eines Dritten", beim("wl212", "eines")), ("keine aufschiebende Wirkung.“", beim("wl212", "keine"))])
folie([("grund", "Problem · Aufschiebende Wirkung, § 80 I 1 VwGO"), ("wl212", "Problem · § 212a I BauGB"),
       ("nr3", "Problem · § 80 II 1 Nr. 3 VwGO")], rechts_frei([
    titel(glyphen("Warum die Klage nicht stoppt"), 110, 75, "grund", 48),
    z("Grundsatz: Widerspruch und Anfechtungsklage haben", 110, 165, "grund", size=32),
    z("aufschiebende Wirkung, § 80 Abs. 1 Satz 1 VwGO", 110, 208, beim("grund", "aufschiebende"), size=32),
    *w212,
    z("= Fall des § 80 Abs. 2 Satz 1 Nr. 3 VwGO:", 110, w212_y + 35, "nr3", "Bold", 34),
    z("Ein Bundesgesetz schließt die Wirkung aus.", 150, w212_y + 90, beim("nr3", "Bundesgesetz"), size=32),
    blk(110, w212_y + 165, 1040, 80, ROT, "darf", [("Herr Weber darf vorerst weiterbauen.", "ExtraBold", 36, INK)]),
    ficon("tabler", "hand-stop", IX, IU, 130, "grund", fuell=GRUEN, bis=beim("wl212", "keine")),
    pl("aufschiebende Wirkung", IX, 190, beim("grund", "aufschiebende"), fill=GRUEN, size=28, anker="m", bis=beim("wl212", "keine")),
    ficon("tabler", "wall", IX, IU, 140, beim("wl212", "keine"), fuell=ROT, anim="cut"),
    pl("Bau läuft weiter", IX, 190, beim("wl212", "keine"), fill=ROT, size=28, anker="m", anim="cut"),
    *fig("DO", FX, FB, FR, [("grund", "denkt"), (beim("wl212", "keine"), "sorge")], bis="darf"),
    *fig("WE", FX, FB, FR, [("darf", "ruhig")]),
    schild("Frau Dorn", FX, "grund", DO_F, bis="darf"),
    schild("Herr Weber, Bauherr", FX, "darf", WE_F, d=0.0),
]))

# E Antrag § 80a III ---------------------------------------------------------------------------------------------------------------
W80A = ("„Das Gericht kann auf Antrag Maßnahmen nach den Absätzen 1 und 2 ändern oder aufheben oder solche Maßnahmen "
        "treffen. § 80 Abs. 5 bis 8 gilt entsprechend.“")
w80a, w80a_y = wortlaut(80, 175, 1100, W80A, "§ 80a Abs. 3 VwGO", "wl80a", size=36,
                        zeilen=["„Das Gericht kann auf Antrag Maßnahmen nach den", "Absätzen 1 und 2 ändern oder aufheben oder",
                                "solche Maßnahmen treffen. § 80 Abs. 5 bis 8 gilt", "entsprechend.“"],
                        marken=[("auf Antrag", beim("wl80a", "auf")), ("§ 80 Abs. 5 bis 8 gilt", beim("wl80a", "Paragraf"))])
folie([("wl80a", "Antrag · § 80a III VwGO"), ("antrag", "Antrag · § 80a III 2 i. V. m. § 80 V 1 Alt. 1 VwGO")], rechts_frei([
    titel(glyphen("Der Eilantrag"), 110, 75, "wl80a", 50),
    *w80a,
    z("Antrag nach § 80a Abs. 3 Satz 2 i. V. m.", 110, w80a_y + 40, "antrag", "Bold", 34),
    z("§ 80 Abs. 5 Satz 1 Alt. 1 VwGO:", 110, w80a_y + 90, beim("antrag", "Paragraf"), "Bold", 34),
    blk(110, w80a_y + 160, 1040, 80, GRUEN, beim("antrag", "anzuordnen"),
        [("aufschiebende Wirkung der Klage anordnen", "ExtraBold", 36, INK)]),
    z("anordnen, nicht wiederherstellen:", 110, w80a_y + 275, "anord", "Bold", 32),
    z("Wirkung entfällt kraft Gesetzes, nicht durch die Behörde", 150, w80a_y + 322, beim("anord", "Wirkung"), size=30),
    ficon(HC, "classical-building", IX, IU, 150, "wl80a", fuell=WEISS),
    pl("Verwaltungsgericht", IX, 190, beim("wl80a", "Gericht"), fill=WEISS, size=28, anker="m"),
    *fig("FA", FX, FB, FR, [("wl80a", "denkt"), ("antrag", "ruhig")]),
    schild("Rechtsanwalt Falk", FX, "wl80a", FA_F),
]))

# F A. Zulässigkeit I.–II. ---------------------------------------------------------------------------------------------------------
folie([("zul", f"{ZU} › I. Statthaftigkeit"), ("befugt", f"{ZU} › II. Antragsbefugnis, § 42 II VwGO analog")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("I. Statthaftigkeit", 110, 180, "statt", "Bold", 36),
    z("Hauptsache: Anfechtung eines Verwaltungsakts,", 150, 238, beim("statt", "Hauptsache"), size=32),
    z("der Herrn Weber begünstigt und sie belastet", 150, 285, beim("statt", "begünstigt"), size=32),
    blk(110, 345, 1040, 76, BLAU, beim("statt", "Deshalb"), [("also § 80a VwGO, nicht § 123 VwGO", "ExtraBold", 34, INK)]),
    zit("§ 123 Abs. 5 VwGO", 150, 430, beim("statt", "hundertdreiundzwanzig")),
    z("II. Antragsbefugnis, § 42 Abs. 2 VwGO analog", 110, 495, "befugt", "Bold", 36),
    z("geltend machen: Verletzung einer Norm,", 150, 553, beim("befugt", "geltend"), size=32),
    z("die gerade sie als Nachbarin schützt", 150, 600, beim("befugt", "gerade"), size=32),
    z("hier: Abstandsflächen der Landesbauordnung", 150, 660, "abst", "Bold", 32),
    ok(120, 683, "abst", gr=18),
    pl("Video: Rücksichtnahmegebot", 150, 735, beim("abst", "Welche"), fill=GELB, size=28),
    ficon("tabler", "file-certificate", IX, IU, 120, "zul", fuell=WEISS),
    pl("Baugenehmigung", IX, 190, beim("statt", "Verwaltungsakt"), fill=WEISS, size=28, anker="m"),
    *fig("DO", FX, FB, FR, [("zul", "ruhig"), ("befugt", "denkt")]),
    schild("Frau Dorn, Antragstellerin", FX, "zul", DO_F),
]))

# G A. III. Rechtsschutzbedürfnis, § 80 VI, Beiladung ------------------------------------------------------------------------------
DX2, WX2, FH2 = 1360, 1720, 400
folie([("rsb", f"{ZU} › III. Rechtsschutzbedürfnis"), ("abs6", f"{ZU} › III. Rechtsschutzbedürfnis › § 80 VI VwGO?"),
       ("beil", "Beteiligte › Beiladung des Bauherrn, § 65 II VwGO")], rechts_frei([
    *tafel("rsb", "A. Zulässigkeit"),
    z("III. Rechtsschutzbedürfnis", 110, 170, "rsb", "Bold", 36),
    z("Klage erhoben", 150, 228, beim("rsb", "Klage"), size=32),
    ok(120, 251, beim("rsb", "erhoben"), gr=18),
    z("Beschluss nützt ihr: noch wird gebaut", 150, 280, beim("rsb2", "Beschluss"), size=32),
    ok(120, 303, beim("rsb2", "gebaut"), gr=18),
    z("vorher Antrag bei der Behörde? Nach dem Wortlaut nein:", 150, 345, "abs6", "Bold", 30),
    z("§ 80a Abs. 3 Satz 2 verweist auch auf § 80 Abs. 6,", 150, 392, beim("abs6", "verweist"), size=30),
    z("der gilt nur bei öffentlichen Abgaben und Kosten", 150, 437, beim("abs6", "Abgaben"), size=30),
    zit("§ 80 Abs. 6 Satz 1 i. V. m. Abs. 2 Satz 1 Nr. 1 VwGO", 150, 482, beim("abs6", "Kosten")),
    z("Beiladung des Bauherrn, § 65 Abs. 2 VwGO:", 110, 560, "beil", "Bold", 34),
    z("notwendig, die Entscheidung kann ihm gegenüber", 150, 615, beim("beil", "Paragraf"), size=32),
    z("nur einheitlich ergehen", 150, 662, beim("beil", "einheitlich"), size=32),
    *fig("DO", DX2, FB, FH2, [("rsb", "ruhig"), ("abs6", "denkt")]),
    schild("Frau Dorn", DX2, "rsb", DO_F),
    *fig("WE", WX2, FB, FH2, [(beim("beil", "Herrn"), "denkt")]),
    schild("Herr Weber, Beigeladener", WX2 - 30, beim("beil", "Herrn"), WE_F, d=0.0, size=26),
    ficon("tabler", "user-plus", WX2, 430, 110, beim("beil", "lädt"), fuell=ORANGE),
]))

# H B. Begründetheit: Interessenabwägung im Dreieck -----------------------------------------------------------------------------
IA = f"{BG} › Interessenabwägung"
folie([("begr", IA), ("wert", f"{IA} › Wertung des § 212a I BauGB"), ("eaus", f"{IA} › Erfolgsaussichten, summarisch"),
       ("offen", f"{IA} › Folgenabwägung")], rechts_frei([
    *tafel("begr", "B. Begründetheit"),
    z("eigene Abwägung des Gerichts, im Dreieck:", 110, 170, beim("begr", "Gericht"), "Bold", 34),
    z("Aussetzungsinteresse von Frau Dorn", 150, 225, beim("pole", "Aussetzungsinteresse"), size=32),
    z("gegen Vollzugsinteresse von Herrn Weber", 150, 272, beim("pole", "Vollzugsinteresse"), size=32),
    blk(110, 335, 1040, 160, GELB, "wert", [("Wertung des § 212a Abs. 1 BauGB:", "ExtraBold", 32, INK),
                                            ("Genehmigung grundsätzlich vollziehbar", "ExtraBold", 32, INK)]),
    zit("OVG NRW, Beschl. v. 29.12.2025 – 7 B 359/25, Rn. 12", 150, 508, beim("wert", "Prozesses")),
    z("wesentlich: Erfolgsaussichten der Klage, summarisch", 110, 565, "eaus", "Bold", 32),
    zit("BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8", 150, 612, beim("eaus", "summarisch")),
    z("offen: Folgenabwägung, die Wertung wiegt schwer", 110, 672, "offen", "Bold", 32),
    zit("OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 90", 150, 720, beim("offen", "Wertung")),
    ficon(HC, "balance-scale", IX, 360, 160, "begr", fuell=WEISS),
    pl("Aussetzung", 1395, 150, beim("pole", "Aussetzungsinteresse"), fill=GRUEN, size=28, anker="m"),
    pl("Vollzug", 1725, 150, beim("pole", "Vollzugsinteresse"), fill=ORANGE, size=28, anker="m"),
    pl("§ 212a BauGB", IX, 420, "wert", fill=GELB, size=28, anker="m"),
    *fig("DO", DX2, FB, FH2, [("begr", "denkt")]),
    schild("Frau Dorn", DX2, "begr", DO_F),
    *fig("WE", WX2, FB, FH2, [("begr", "ruhig")]),
    schild("Herr Weber", WX2, "begr", WE_F),
]))

# I Prüfungsmaßstab: nur drittschützende Normen --------------------------------------------------------------------------------------
folie([("nurdritt", f"{BG} › Maßstab: nur drittschützende Normen"), ("mass", f"{BG} › Maß der baulichen Nutzung?")], rechts_frei([
    *tafel("nurdritt", "Was das Gericht prüft"),
    z("nicht: Ist die Genehmigung irgendwie rechtswidrig?", 110, 180, "nurdritt", "Bold", 34),
    nein(1110, 205, beim("nurdritt", "rechtswidrig"), gr=24),
    z("sondern: Verstößt sie gegen Normen,", 110, 255, "nur2", "Bold", 34),
    z("die gerade Frau Dorn schützen?", 110, 305, beim("nur2", "gerade"), "Bold", 34),
    ok(1000, 330, beim("nur2", "schützen"), gr=24),
    zit("OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 3", 150, 360, beim("nur2", "schützen")),
    z("Maß der baulichen Nutzung: 4 Geschosse", 110, 440, "mass", "Bold", 32),
    z("in zweigeschossiger Umgebung? kann offenbleiben", 150, 487, beim("mass", "zweigeschossige"), size=30),
    z("hilft nur, wenn zugleich das Rücksichtnahmegebot", 150, 545, beim("mass", "Darauf"), size=30),
    z("verletzt ist", 150, 590, beim("mass", "Rücksichtnahmegebot"), size=30),
    zit("OVG NRW, Beschl. v. 14.1.2021 – 10 B 1891/20, Rn. 5", 150, 640, beim("mass", "verletzt")),
    ficon("tabler", "scale", IX, IU, 140, "nurdritt", fuell=WEISS),
    pl("nur ihre Rechte", IX, 190, beim("nur2", "gerade"), fill=GRUEN, size=28, anker="m"),
    *fig("DO", FX, FB, FR, [("nurdritt", "ruhig"), ("mass", "denkt")]),
    schild("Frau Dorn", FX, "nurdritt", DO_F),
]))

# J Abstandsflächen: Skizze ---------------------------------------------------------------------------------------------------------
AF = f"{BG} › Erfolgsaussichten › Abstandsflächen"
M = 24                                       # Maßstab der Skizze: 1 m = 24 px
SB, GX = 740, 660                            # Boden der Skizze, Grenze
WAND = GX - 3 * M                            # Hauswand 3 m vor der Grenze
folie([("abf", AF), ("nrw", f"{AF} › Beispiel NRW"), ("fall2", f"{AF} › im Fall"), ("rw", f"{AF} › Ergebnis")], rechts_frei([
    *tafel("abf", "Die Abstandsflächen", h=860),
    z("schützen auch den Nachbarn, gerade bei Sonne", 110, 160, "schutz", "Bold", 32),
    zit("BVerwG, 4 B 52.15, Rn. 9; OVG NRW, 10 B 603/20, Rn. 16", 150, 205, beim("schutz", "Sonne")),
    z("z. B. NRW: auf dem eigenen Grundstück,", 110, 255, "nrw", size=32),
    z("Tiefe 0,4 H, mindestens 3 m", 110, 298, beim("nrw", "Tiefe"), "Bold", 32),
    zit("§ 6 Abs. 2 Satz 1, Abs. 5 Satz 1 BauO NRW 2018", 150, 340, beim("nrw", "Tiefe")),
    zit("in deinem Land ggf. andere Regel", 150, 376, beim("nrw", "deinem")),
    # Skizze im Schnitt: Wand von Herrn Weber links, Grenze, Haus von Frau Dorn rechts
    hart(linienzug([(110, SB), (1150, SB)], "fall2", breite=5, farbe=INK)),
    rechteck(WAND - 230, SB - int(12.5 * M), 230, int(12.5 * M), BLAU, beim("fall2", "Hauswand"), anim="cut", name="wand"),
    pl("H = 12,5 m", WAND - 115, SB - int(12.5 * M) + 25, beim("fall2", "zwölfeinhalb"), fill=WEISS, size=28, anker="m"),
    strichlinie(GX, SB - 240, SB, beim("fall2", "Hauswand")),
    pl("Grenze", GX + 70, SB - 240, beim("fall2", "Hauswand"), fill=WEISS, size=26, anker="m"),
    skizze(ficon(HC, "house-with-garden", 1050, SB - 2, 170, beim("fall2", "Hauswand"), fuell=GELB, anim="cut")),
    rechteck(WAND, SB - 15, 5 * M, 28, GRUEN, beim("fall2", "fünf"), name="abstandsflaeche"),
    pl("nötig: 5 m", IX, 130, beim("fall2", "fünf"), fill=GRUEN, size=28, anker="m"),
    pl("steht nur 3 m vor der Grenze", IX, 200, beim("fall2", "drei"), fill=WEISS, size=26, anker="m"),
    rechteck(GX, SB - 15, 2 * M, 28, ROT, beim("verst", "Zwei"), anim="cut", name="auf_ihrem_grundstueck"),
    pl("2 m auf ihrem Grundstück", IX, 270, beim("verst", "Zwei"), fill=ROT, size=28, anker="m"),
    pl("keine Abweichung zugelassen", IX, 340, beim("verst", "Abweichung"), fill=WEISS, size=26, anker="m"),
    blk(110, 770, 1040, 76, GRUEN, beim("rw", "offensichtlich"), [("offensichtlich in ihren Rechten verletzt", "ExtraBold", 32, INK)]),
    ok(1100, 808, beim("rw", "Rechten"), gr=24),
    z("Rücksichtnahmegebot: kann offenbleiben", 150, 862, "rueck", size=28),
    *fig("DO", FX, FB, FR, [("abf", "denkt"), ("verst", "aerger"), ("rw", "froh")]),
    schild("Frau Dorn", FX, "abf", DO_F),
]))

# K Ergebnis und Tenor ---------------------------------------------------------------------------------------------------------------
folie([("ergeb", "Ergebnis · Aussetzungsinteresse überwiegt"), ("tenor", "Ergebnis · Tenor (Klausurkonvention)")], rechts_frei([
    *tafel("ergeb", "Das Ergebnis"),
    z("Aussetzungsinteresse von Frau Dorn überwiegt,", 110, 175, beim("ergeb", "Aussetzungsinteresse"), "Bold", 34),
    z("trotz § 212a Abs. 1 BauGB", 150, 225, beim("ergeb", "trotz"), size=32),
    zit("OVG NRW, Beschl. v. 16.6.2020 – 10 B 603/20, Rn. 16", 150, 272, beim("ergeb", "zweihundertzwölf")),
    z("Tenor (Klausurkonvention):", 110, 345, "tenor", "Bold", 34),
    blk(110, 400, 1040, 310, GRUEN, beim("tenor", "Die"),
        [("„Die aufschiebende Wirkung der Klage", "ExtraBold", 34, INK), ("der Antragstellerin gegen die dem", "ExtraBold", 34, INK),
         ("Beigeladenen erteilte Baugenehmigung", "ExtraBold", 34, INK), ("wird angeordnet.“", "ExtraBold", 34, INK)]),
    z("dazu Kosten und Streitwert", 150, 735, beim("tenor", "Kosten"), size=32),
    zit("Tenorform wie OVG NRW, 10 B 603/20", 150, 782, beim("tenor", "Streitwert")),
    ficon(HC, "classical-building", IX, IU, 150, "ergeb", fuell=WEISS),
    pl("Beschluss", IX, 190, "tenor", fill=GRUEN, size=28, anker="m"),
    *fig("DO", FX, FB, FR, [("ergeb", "froh")]),
    schild("Frau Dorn", FX, "ergeb", DO_F),
]))

# L Baustelle: Baustopp, Sicherungsmaßnahmen --------------------------------------------------------------------------------------
WEb = ("WE_redet", WEX, BODEN, FH)
folie([("stopp", "Ergebnis · Die Baustelle ruht"), ("sich", "Ergebnis · Sicherungsmaßnahmen, § 80a III 1, I Nr. 2 VwGO")], [
    linienzug([(60, BODEN), (1860, BODEN)], "stopp", breite=7, farbe=INK),
    ficon("tabler", "sun", 1480, 175, 120, "stopp", fuell=GELB),
    haus("stopp"),
    *[e for n in (1, 2, 3, 4) for e in geschoss(n, "stopp")],
    ficon("tabler", "barrier-block", ROX + 260, BODEN - 2, 150, beim("stopp", "nicht"), fuell=ROT),
    pl("Genehmigung darf nicht ausgenutzt werden", 70, 40, beim("stopp", "nicht"), fill=GELB, size=32),
    pl("baut er trotzdem weiter:", 70, 120, "sich", fill=WEISS, size=30),
    pl("Sicherungsmaßnahmen, § 80a Abs. 3 Satz 1, Abs. 1 Nr. 2 VwGO", 70, 190, beim("sich", "Sicherungsmaßnahmen"), fill=ORANGE, size=30),
    pl("etwa Stilllegung der Baustelle", 70, 260, beim("sich", "Stilllegung"), fill=ROT, size=30),
    *fig("DO", DOX, BODEN, FH, [("stopp", "froh_r")]),
    schild("Frau Dorn, Nachbarin", DOX, "stopp", DO_F, unten=BODEN),
    *fig("WE", WEX, BODEN, FH, [("stopp", "denkt"), ("sich", "muede")], bis="we2"),
    *redet("WE_redet", WEX, BODEN, FH, "we2", "tipp"),
    schild("Herr Weber, Bauherr", WEX, "stopp", WE_F, unten=BODEN),
    blase("sprech", 590, 140, "we2", 1540, 300, inhalt=["Dann muss ich wohl umplanen."], textsize=30, figur=WEb),
])

# M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Rechtswidrig ist nicht genug"), ("tipp2", "Klausurtipp · Prüfprogramm der Genehmigung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("nie: „rechtswidrig, also Antrag begründet“", 200, 200, beim("tipp", "Schreib"), "Bold", 34),
    nein(1110, 222, beim("tipp", "Erfolg"), gr=22),
    z("immer: Verletzt sie eine Norm, die gerade", 200, 290, "tipp1", size=34),
    z("die Antragstellerin schützt?", 200, 342, beim("tipp1", "gerade"), size=34),
    z("Bauordnungsrecht: Prüft die Behörde die Norm", 200, 440, "tipp2", "Bold", 34),
    z("im Genehmigungsverfahren deines Landes überhaupt?", 200, 492, beim("tipp2", "Genehmigungsverfahren"), size=32),
    z("NRW: Abstandsflächen gehören dazu", 200, 560, beim("tipp2", "Nordrhein-Westfalen"), size=34),
    zit("§ 64 Abs. 1 Satz 1 Nr. 1 Buchst. b BauO NRW 2018", 200, 610, beim("tipp2", "Abstandsflächen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 32, 60
LX0, RX0 = 110, 960
links = [("s1", "I. Statthaftigkeit: § 80a III 2,", "Regular"), ("s1", "§ 80 V 1 Alt. 1 (Anordnung)", "Regular"),
         ("s2", "II. Antragsbefugnis: drittschützende", "Regular"), ("s2", "Norm, § 42 II analog", "Regular"),
         ("s3", "III. Rechtsschutzbedürfnis:", "Regular"), ("s3", "Rechtsbehelf erhoben", "Regular"),
         ("s4", "Beiladung des Bauherrn, § 65 II", "Bold")]
rechts_ = [("s5", "I. Interessenabwägung im Dreieck,", "Regular"), ("s5", "Wertung des § 212a I BauGB", "Regular"),
           ("s6", "II. summarisch: nur", "Regular"), ("s6", "drittschützende Normen", "Regular"),
           ("s7", "III. hier: Abstandsflächen", "Regular"), ("s8", "C. Tenor: Anordnung", "ExtraBold")]
els_t = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: Eilantrag der Nachbarin"), 110, 85, "sch", 44),
         z("A. Zulässigkeit", LX0, 190, "sa", "ExtraBold", 38, rechts=940),
         z("B. Begründetheit", RX0, 190, "sb", "ExtraBold", 38, rechts=1820)]
for i, (c, t, st) in enumerate(links):
    einzug = 30 if t.startswith(("I", "B")) else 70
    els_t.append(z(t, LX0 + einzug, 262 + i * LH + (20 if c == "s4" else 0), c, st, SZ, rechts=940))
for i, (c, t, st) in enumerate(rechts_):
    einzug = 0 if c == "s8" else (30 if t.startswith(("I", "II", "III")) else 70)
    els_t.append(z(t, RX0 + einzug, 262 + i * LH + (40 if c == "s8" else 0), c, st, SZ if c != "s8" else 38, rechts=1820))
folie([("sch", "Klausurschema · Eilantrag nach §§ 80a III, 80 V VwGO")], els_t)

# O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gegen eine ", 0), ("Baugenehmigung", "a"), (" hat der", 0)]], 750, 320, 42, "merke",
                {"a": beim("merke", "Baugenehmigung")}),
    *markertext([[("Rechtsbehelf des Nachbarn ", 0), ("keine", "b")]], 750, 385, 42, beim("merke", "Rechtsbehelf"),
                {"b": beim("merke", "keine")}),
    *markertext([[("aufschiebende Wirkung.", 0)]], 750, 450, 42, beim("merke", "aufschiebende"), {}),
    *markertext([[("Das Gericht ", 0), ("ordnet", "c"), (" sie auf Antrag an, wenn", 0)]], 750, 580, 40, "m2",
                {"c": beim("m2", "ordnet")}),
    *markertext([[("die Genehmigung voraussichtlich eine Norm", 0)]], 750, 642, 40, beim("m2", "Genehmigung"), {}),
    *markertext([[("verletzt, die ", 0), ("gerade den Nachbarn", "d"), (" schützt.", 0)]], 750, 704, 40, beim("m2", "verletzt"),
                {"d": beim("m2", "gerade")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
