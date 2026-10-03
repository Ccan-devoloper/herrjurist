"""Folge 088 · Rücksichtnahmegebot: Der Riesenbau neben deinem Einfamilienhaus – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Einfamilienhaus am Stadtrand, Baugenehmigung für einen achtgeschossigen Wohnblock nebenan, Klage der Nachbarin),
Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Garten (Haus, Wohnblock, Baugenehmigung, Schatten, Frage), B Sachverhalt,
C A. Zulässigkeit (Drittanfechtung, § 42 II, Schutznormtheorie, § 113 I 1), D B. drittschützende Normen im Überblick,
E Herkunft I (§ 35 III, Wortlaut § 34 I 1), F Herkunft II (Wortlaut § 15 I 2 BauNVO, § 31 II), G Maßstab (BVerwGE 52, 122),
H Schatten und Abstandsflächen, I erdrückende Wirkung, J zurück am Garten (Subsumtion, Ergebnis, Eilrechtsschutz),
K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, wenn die Baugenehmigung erscheint)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_088/"
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


def zk(text, x, y, cue, kcue, stil="Regular", size=34, **k):
    """Tafelzeile mit Bleistift-Kreuz direkt hinter dem Zeilenende (zur gesprochenen Verneinung)."""
    e = z(text, x, y, cue, stil, size, **k)
    return [e, nein(e.x + e.sprite.width + 28, y + size * 0.72, kcue, gr=22)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_088/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 085/082/069): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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


def schatten_flaeche(x0, x1, y0, y1, cue, bis=None, d=0.0):
    """Schatten des Wohnblocks als halbtransparente Fläche über dem Garten (Lichtwirkung, kein Requisit)."""
    im = Image.new("RGBA", (x1 - x0, y1 - y0))
    ImageDraw.Draw(im).polygon([(0, im.height), (im.width, 0), (im.width, im.height)], fill=(40, 40, 70, 55))
    return El(im, x0, y0, cue, "fade", d, bis, name="schatten")


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KO_F, RE_F = LILA, ROT                      # Farben der Namensschilder
ZU = "A. Zulässigkeit"
BG = "B. Begründetheit"
RG = "Rücksichtnahmegebot"
GH = 390                                    # Figurenhöhe in den Gartenszenen (der Wohnblock soll die Menschen überragen)
HAUSX, KOX, REX, BLX = 250, 650, 1090, 1560


def garten(cue, anim="pop", welk=None, bis=None):
    """Garten von Frau Kolbe: Haus (Tabler „home“), Zaun, Sonnenblume (welkt im Schatten), Tulpe – in jeder Gartenszene gleich."""
    els = [ficon("tabler", "home", HAUSX, BODEN - 2, 230, cue, fuell=GELB, anim=anim, bis=bis),
           ficon("tabler", "fence", 880, BODEN - 2, 110, cue, fuell=WEISS, anim=anim, bis=bis),
           ficon(HC, "tulip", 805, BODEN - 2, 70, cue, fuell=ROT, anim=anim, bis=bis)]
    if welk is None:
        els.append(ficon(HC, "sunflower", 470, BODEN - 2, 100, cue, fuell=GELB, anim=anim, bis=bis))
    else:
        els.append(ficon(HC, "sunflower", 470, BODEN - 2, 100, cue, fuell=GELB, anim=anim, bis=welk))
        els.append(ficon(HC, "wilted-flower", 470, BODEN - 2, 85, welk, fuell=ROT, anim="cut", bis=bis))
    return els


def block_(cue, anim="pop", bis=None):
    """Wohnblock: Tabler „building“ (blau gefüllt), 600 px hoch – überragt Haus und Menschen."""
    return ficon("tabler", "building", BLX, BODEN - 2, 600, cue, fuell=BLAU, anim=anim, bis=bis)


# A Fall: Haus, Wohnblock, Baugenehmigung -------------------------------------------------------------------------------------
KOa = ("KO_protest_r", KOX, BODEN, GH)
REa = ("RE_redet", REX, BODEN, GH)
folie([(NULL, "Fall · Das Haus am Stadtrand"), ("reimers", "Fall · Der Wohnblock nebenan"), ("genehm", "Fall · Die Baugenehmigung"),
       ("frage", "Fall · Kann sie die Genehmigung zu Fall bringen?")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *[hart(e) for e in garten(NULL, anim="cut", welk="schatten")],
    schatten_flaeche(330, 1262, 300, BODEN, "schatten"),
    *fig("KO", KOX, BODEN, GH, [(NULL, "ruhig_r"), ("re1", "sorge_r")], bis="ko1", erst="cut"),
    *redet("KO_protest_r", KOX, BODEN, GH, "ko1", "frage"),
    *fig("KO", KOX, BODEN, GH, [("frage", "denkt_r")]),
    hart(schild("Frau Kolbe", KOX, NULL, KO_F, unten=BODEN, d=0.0)),
    pl("seit 40 Jahren im Einfamilienhaus am Stadtrand", 70, 40, beim("fall", "vierzig"), fill=GELB, size=34, bis="re1"),
    pl("ringsum nur Einfamilienhäuser", 70, 205, "garten", fill=WEISS, size=30, bis="re1"),
    pl("kein Bebauungsplan", 70, 275, beim("garten", "Bebauungsplan"), fill=WEISS, size=30, bis="re1"),
    pl("Garten in der Sonne", 470, 600, beim("garten", "Garten"), fill=GELB, size=28, anker="m", bis="schatten"),
    *fig("RE", REX, BODEN, GH, [(beim("reimers", "Herr"), "ruhig")], bis="re1"),
    *redet("RE_redet", REX, BODEN, GH, "re1", "genehm"),
    *fig("RE", REX, BODEN, GH, [("genehm", "ruhig"), ("ko1", "denkt")]),
    schild("Herr Reimers, Bauherr", REX, beim("reimers", "Herr"), RE_F, unten=BODEN, d=0.0),
    blase("denk", 300, 230, beim("reimers", "Wohnblock"), 1300, 330, figur=("RE_ruhig", REX, BODEN, GH), bis="re1"),
    ficon("tabler", "building", 1300, 400, 120, beim("reimers", "Wohnblock"), fuell=BLAU, d=0.2, bis="re1"),
    blase("sprech", 820, 200, "re1", 820, 290, inhalt=["Hier entstehen 8 Geschosse mit 40 Wohnungen.",
                                                     "Die Abstandsflächen halte ich ein."], textsize=29, figur=REa, bis="genehm"),
    szene(ficon("tabler", "file-certificate", 900, 330, 90, beim("genehm", "Baugenehmigung"), fuell=WEISS, bis="ko1"),
          "088papier*", 0.8, -0.13),
    pl("Baugenehmigung erteilt", 900, 345, beim("genehm", "Baugenehmigung"), fill=GRUEN, size=28, anker="m", bis="ko1"),
    block_("masse"),
    pl("25 m hoch", BLX, 205, beim("masse", "fünfundzwanzig"), fill=BLAU, size=30, anker="m"),
    pl("50 m lang", BLX, 920, beim("masse", "fünfzig"), fill=BLAU, size=28, anker="m"),
    pl("14 m vor ihrem Haus", 900, 125, beim("masse", "vierzehn"), fill=WEISS, size=30, anker="m", bis="ko1"),
    pl("quer vor dem ganzen Garten", 900, 195, beim("masse", "quer"), fill=WEISS, size=30, anker="m", bis="ko1"),
    pl("Garten im Schatten", 470, 600, beim("schatten", "Schatten"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 660, 170, "ko1", 420, 330, inhalt=["Der Klotz nimmt mir ja die ganze Sonne!", "Dagegen klage ich."],
          textsize=29, figur=KOa, bis="frage"),
    pl("Kann sie die Baugenehmigung zu Fall bringen?", 830, 150, "frage", fill=PINK, size=38, anker="m"),
])

# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Kolbe wohnt seit 40 Jahren in ihrem eingeschossigen Einfamilienhaus am Stadtrand. Ringsum stehen nur ein- und "
    "zweigeschossige Einfamilienhäuser; einen Bebauungsplan gibt es nicht. Auf dem Nachbargrundstück südlich ihres Gartens "
    "will Herr Reimers einen Wohnblock mit 8 Geschossen und 40 Wohnungen bauen: 25 m hoch, 50 m lang, 14 m vor ihrem Haus, "
    "quer vor dem ganzen Garten. Die Abstandsflächen nach der Landesbauordnung hält der Bau ein. Die Bauaufsichtsbehörde "
    "erteilt die Baugenehmigung. Frau Kolbe erhebt Klage beim Verwaltungsgericht.",
], "Kann Frau Kolbe die Baugenehmigung zu Fall bringen?")

# C A. Zulässigkeit: Drittanfechtung, Klagebefugnis, Schutznormtheorie -------------------------------------------------------------
folie([("klage", f"{ZU} › Anfechtungsklage eines Dritten"), ("p42", f"{ZU} › Klagebefugnis, § 42 II VwGO"),
       ("schutz", f"{ZU} › Klagebefugnis › Schutznormtheorie"), ("objektiv", f"{BG} › Verletzung eigener Rechte, § 113 I 1 VwGO")],
      rechts_frei([
    *tafel("klage", "Die Klage der Nachbarin"),
    z("Genehmigung für einen anderen angegriffen:", 110, 170, beim("klage", "Genehmigung"), size=32),
    z("Anfechtungsklage eines Dritten", 150, 218, beim("klage", "Anfechtungsklage"), "Bold", 36),
    z("Klagebefugnis, § 42 Abs. 2 VwGO:", 110, 300, "p42", "Bold", 36),
    z("geltend machen, in eigenen Rechten verletzt zu sein", 150, 352, beim("p42", "geltend"), size=32),
    blk(110, 425, 1040, 132, GELB, "schutz",
        [("Schutznormtheorie: nur eine Norm, die", "ExtraBold", 34, INK),
         ("zumindest auch die Nachbarin schützt", "ExtraBold", 34, INK)]),
    z("= drittschützende Norm", 150, 572, beim("schutz", "drittschützende"), "Bold", 34),
    *zk("objektiv rechtswidrig: genügt nicht", 110, 650, "objektiv", beim("objektiv", "genügt"), "Bold", 34),
    z("„… rechtswidrig und der Kläger dadurch in seinen Rechten verletzt …“", 110, 712, beim("objektiv", "Paragraf"), size=28),
    zit("§ 113 Abs. 1 Satz 1 VwGO", 150, 760, beim("objektiv", "Paragraf")),
    ficon("tabler", "file-certificate", IX, IU, 110, "klage", fuell=WEISS),
    pl("Baugenehmigung", IX, 190, beim("klage", "Genehmigung"), fill=GRUEN, size=28, anker="m"),
    *fig("KO", FX, FB, FR, [("klage", "ruhig"), ("schutz", "denkt")]),
    schild("Frau Kolbe", FX, "klage", KO_F),
]))

# D B. Begründetheit: drittschützende Normen im Überblick --------------------------------------------------------------------------
DN = f"{BG} › Drittschützende Normen"
folie([("ueber", DN), ("abst", f"{DN} › Abstandsflächen"), ("gebiet", f"{DN} › Gebietserhaltungsanspruch"),
       ("mass", f"{DN} › Maß der baulichen Nutzung"), ("bleibt", f"{BG} › {RG}")], rechts_frei([
    *tafel("ueber", "Welche drittschützende Norm?"),
    z("1. Abstandsflächen der Landesbauordnung", 110, 175, "abst", "Bold", 34),
    *zk("schützen auch den Nachbarn, hier eingehalten", 150, 225, beim("abst", "schützen"), beim("abst", "eingehalten"), size=32),
    z("2. Gebietserhaltungsanspruch (Art der Nutzung)", 110, 300, "gebiet", "Bold", 34),
    *zk("Wohnblock ist Wohnen wie ihr Haus", 150, 350, beim("gebiet", "Wohnblock"), beim("gebiet", "Wohnen"), size=32),
    zit("BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8", 150, 398, beim("gebiet", "Gebietserhaltungsanspruch")),
    z("3. Maß der baulichen Nutzung: 8 Geschosse", 110, 470, "mass", "Bold", 34),
    *zk("schützt den Nachbarn in der Regel nicht", 150, 520, beim("mass", "schützt"), beim("mass", "Regel"), size=32),
    zit("BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 21; OVG NRW, 10 B 1713/08, Rn. 8", 150, 568, beim("mass", "schützt")),
    blk(110, 650, 1040, 80, GRUEN, "bleibt", [("Es bleibt: das Gebot der Rücksichtnahme", "ExtraBold", 36, INK)]),
    ficon("tabler", "building-community", IX, IU, 150, "ueber", fuell=BLAU),
    *fig("KO", FX, FB, FR, [("ueber", "denkt"), ("mass", "sorge"), ("bleibt", "ruhig")]),
    schild("Frau Kolbe", FX, "ueber", KO_F),
]))

# E Herkunft I: Außenbereich, Wortlaut § 34 I 1 -------------------------------------------------------------------------------------
W341 = ("„Innerhalb der im Zusammenhang bebauten Ortsteile ist ein Vorhaben zulässig, wenn es sich nach Art und Maß der "
        "baulichen Nutzung, der Bauweise und der Grundstücksfläche, die überbaut werden soll, in die Eigenart der näheren "
        "Umgebung einfügt und die Erschließung gesichert ist.“")
Z341 = ["„Innerhalb der im Zusammenhang bebauten Ortsteile ist ein",
        "Vorhaben zulässig, wenn es sich nach Art und Maß der baulichen",
        "Nutzung, der Bauweise und der Grundstücksfläche, die überbaut",
        "werden soll, in die Eigenart der näheren Umgebung einfügt",
        "und die Erschließung gesichert ist.“"]
w341, w341_y = wortlaut(80, 330, 1100, W341, "§ 34 Abs. 1 Satz 1 BauGB", "wl34", size=32, zeilen=Z341,
                        marken=[("in die Eigenart der näheren Umgebung einfügt", beim("wl34", "einfügen"))])
HK = f"{RG} › Herkunft"
folie([("herkunft", HK), ("aussen", f"{HK} › Außenbereich, § 35 III BauGB"), ("wl34", f"{HK} › Innenbereich, § 34 I 1 BauGB")],
      rechts_frei([
    titel(glyphen("Herkunft des Rücksichtnahmegebots"), 110, 75, "herkunft", 46),
    z("kein eigener Paragraf", 110, 150, beim("herkunft", "eigenen"), "Bold", 34),
    z("Außenbereich: unbenannter öffentlicher Belang, § 35 Abs. 3", 110, 210, "aussen", size=32),
    zit("BVerwG, Beschl. v. 11.12.2006 – 4 B 72.06, Rn. 8", 150, 258, beim("aussen", "unbenannter")),
    *w341,
    z("keine Rücksicht auf die Nachbarn: fügt sich nicht ein", 110, w341_y + 25, "einf", "Bold", 32),
    zit("BVerwG, 4 B 50.17, Rn. 4; 4 B 16.15, Rn. 8", 150, w341_y + 75,
        beim("einf", "fügt")),
    ficon(HC, "house", IX - 120, IU, 110, "herkunft", fuell=GELB),
    ficon(HC, "houses", IX + 90, IU, 150, "herkunft", fuell=GELB),
    pl("nähere Umgebung", IX, 190, beim("wl34", "Umgebung"), fill=GELB, size=28, anker="m"),
    *fig("KO", FX, FB, FR, [("herkunft", "denkt")]),
    schild("Frau Kolbe", FX, "herkunft", KO_F),
]))

# F Herkunft II: Wortlaut § 15 I 2 BauNVO, § 31 II BauGB -----------------------------------------------------------------------------
W152 = ("„Sie sind auch unzulässig, wenn von ihnen Belästigungen oder Störungen ausgehen können, die nach der Eigenart des "
        "Baugebiets im Baugebiet selbst oder in dessen Umgebung unzumutbar sind, oder wenn sie solchen Belästigungen oder "
        "Störungen ausgesetzt werden.“")
Z152 = ["„Sie sind auch unzulässig, wenn von ihnen Belästigungen oder",
        "Störungen ausgehen können, die nach der Eigenart des Baugebiets",
        "im Baugebiet selbst oder in dessen Umgebung unzumutbar sind,",
        "oder wenn sie solchen Belästigungen oder Störungen ausgesetzt",
        "werden.“"]
w152, w152_y = wortlaut(80, 170, 1100, W152, "§ 15 Abs. 1 Satz 2 BauNVO", "wl15", size=32, zeilen=Z152,
                        marken=[("unzumutbar", beim("wl15", "unzumutbar"))])
folie([("wl15", f"{HK} › Plangebiet, § 15 I 2 BauNVO"), ("befr", f"{HK} › Befreiung, § 31 II BauGB")], rechts_frei([
    titel(glyphen("Im Plangebiet: § 15 BauNVO"), 110, 75, "wl15", 46),
    *w152,
    zit("Ausprägung des Rücksichtnahmegebots: BVerwG, 4 C 8.11, Rn. 16", 110, w152_y + 18,
        beim("wl15", "Anlagen")),
    z("Befreiung vom Bebauungsplan, § 31 Abs. 2 BauGB:", 110, w152_y + 95, "befr", "Bold", 34),
    z("„… auch unter Würdigung nachbarlicher Interessen …“", 150, w152_y + 150, beim("befr", "Würdigung"), size=32),
    zit("BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 12", 150, w152_y + 200, beim("befr", "Würdigung")),
    ficon("tabler", "map", IX, IU, 120, "wl15", fuell=GRUEN),
    pl("Plangebiet", IX, 200, beim("wl15", "Plangebiet"), fill=GRUEN, size=28, anker="m"),
    *fig("KO", FX, FB, FR, [("wl15", "denkt")]),
    schild("Frau Kolbe", FX, "wl15", KO_F),
]))

# G Maßstab: Abwägung der Zumutbarkeit (BVerwGE 52, 122) ---------------------------------------------------------------------------
KO2X, RE2X = 1380, 1700
folie([("mst", f"{RG} › Maßstab"), ("zumut", f"{RG} › Maßstab: Abwägung der Zumutbarkeit")], rechts_frei([
    *tafel("mst", "Wann ist ein Vorhaben rücksichtslos?", size=44),
    z("Grundlegend: BVerwG, Urt. v. 25.2.1977 – IV C 22.75,", 110, 170, beim("mst", "Grundlegend"), "Bold", 32),
    z("BVerwGE 52, 122", 150, 215, beim("mst", "Grundlegend"), "Bold", 32),
    z("Je empfindlicher und schutzwürdiger der Nachbar,", 110, 295, "je1", size=34),
    z("desto mehr Rücksicht kann er verlangen.", 150, 345, beim("je1", "desto"), "Bold", 34),
    z("Je verständlicher die Interessen des Bauherrn,", 110, 425, "je2", size=34),
    z("desto weniger Rücksicht muss er nehmen.", 150, 475, beim("je2", "desto"), "Bold", 34),
    blk(110, 560, 1040, 126, GELB, "zumut", [("Abwägung: Was ist beiden nach", "ExtraBold", 36, INK),
                                             ("Lage der Dinge zuzumuten?", "ExtraBold", 36, INK)]),
    zit("BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 12 (zu BVerwGE 52, 122 <126>)", 150, 705, beim("zumut", "zuzumuten")),
    ficon(HC, "balance-scale", 1580, IU, 150, "mst", fuell=WEISS),
    *fig("KO", KO2X, FB, FR, [("mst", "denkt"), ("je1", "ruhig"), ("je2", "sorge")]),
    schild("Frau Kolbe", KO2X, "mst", KO_F),
    *fig("RE", RE2X, FB, FR, [("je2", "ruhig")]),
    schild("Herr Reimers, Bauherr", RE2X, "je2", RE_F),
]))

# H Schatten und Abstandsflächen ---------------------------------------------------------------------------------------------------
FA = f"{RG} › Im Fall"
folie([("schat", f"{FA} › Verschattung"), ("indiz", f"{FA} › Abstandsflächen als Indiz"), ("regel", f"{FA} › fügt sich nicht ein")],
      rechts_frei([
    *tafel("schat", "Im Fall: Schatten und Abstandsflächen", size=44),
    z("Verschattung: im bebauten Viertel", 110, 170, beim("schat", "bebauten"), "Bold", 34),
    *zk("in der Regel hinzunehmen", 150, 220, beim("schat", "hinnehmen"), beim("schat", "verschattet"), size=32),
    zit("OVG NRW, Urt. v. 17.3.2021 – 7 A 1791/19, Rn. 42", 150, 268, beim("schat", "hinnehmen")),
    z("Abstandsflächen eingehalten:", 110, 345, "indiz", "Bold", 34),
    z("starkes Indiz für Licht und Sonne", 150, 395, beim("indiz", "Indiz"), size=32),
    zit("BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9", 150, 443, beim("indiz", "Indiz")),
    z("Regel nur, wenn sich der Bau auch sonst einfügt", 110, 520, "regel", "Bold", 34),
    zit("BVerwG, Beschl. v. 27.3.2018 – 4 B 50.17, Rn. 4", 150, 568, beim("regel", "einfügt")),
    blk(110, 640, 1040, 126, ROT, beim("regel", "Acht"), [("8 Geschosse zwischen Einfamilienhäusern:", "ExtraBold", 34, INK),
                                                          ("fügt sich nicht ein", "ExtraBold", 34, INK)]),
    ficon("tabler", "home", IX - 120, IU, 110, "schat", fuell=GELB),
    ficon("tabler", "building", IX + 80, IU, 190, beim("schat", "Nachbargrundstück"), fuell=BLAU),
    ficon("tabler", "sun", IX - 120, 160, 80, "schat", fuell=GELB, bis=beim("schat", "verschattet")),
    pl("zeitweise Schatten", IX - 60, 140, beim("schat", "verschattet"), fill=WEISS, size=28, anker="m"),
    *fig("KO", FX, FB, FR, [("schat", "sorge"), ("regel", "denkt")]),
    schild("Frau Kolbe", FX, "schat", KO_F),
]))

# I Erdrückende Wirkung --------------------------------------------------------------------------------------------------------------
folie([("erdr", f"{FA} › erdrückende Wirkung?")], rechts_frei([
    *tafel("erdr", "Erdrückende Wirkung"),
    z("wegen seiner Ausmaße: nimmt dem Nachbar-", 110, 175, beim("erdr", "Ausmaße"), size=34),
    z("grundstück förmlich die Luft", 150, 225, beim("erdr", "Luft"), "Bold", 34),
    z("Gefühl des Eingemauertseins", 110, 295, beim("erdr", "Gefühl"), "Bold", 34),
    zit("OVG NRW, Urt. v. 17.3.2021 – 7 A 1791/19, Rn. 39", 150, 343, beim("erdr", "Gefühl")),
    z("oder: riegelt das Grundstück regelrecht ab", 110, 415, "riegel", "Bold", 34),
    zit("BVerwG, Beschl. v. 11.12.2006 – 4 B 72.06, Rn. 9", 150, 463, beim("riegel", "abriegelt")),
    z("gleiche Höhe: grundsätzlich nicht", 110, 540, "hoehe", size=34),
    zit("BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 10", 150, 588, beim("hoehe", "Betracht")),
    blk(110, 650, 1040, 80, ROT, beim("hoehe", "Hier"), [("hier: 8 Geschosse gegen 1", "ExtraBold", 38, INK)]),
    ficon("tabler", "home", IX - 140, IU, 90, "erdr", fuell=GELB),
    ficon("tabler", "building", IX + 70, IU, 230, "erdr", fuell=BLAU),
    pl("8 Geschosse", IX + 70, 120, beim("hoehe", "Hier"), fill=BLAU, size=28, anker="m"),
    pl("1 Geschoss", IX - 140, 250, beim("hoehe", "eines"), fill=GELB, size=26, anker="m"),
    *fig("KO", FX, FB, FR, [("erdr", "sorge")]),
    schild("Frau Kolbe", FX, "erdr", KO_F),
]))

# J Zurück am Garten: Subsumtion, Ergebnis, Eilrechtsschutz ---------------------------------------------------------------------------
KOj = ("KO_redet_r", KOX, BODEN, GH)
folie([("fall2", f"{FA} › erdrückende Wirkung"), ("rlos", f"{FA}: rücksichtslos"), ("erg", "Ergebnis · Die Klage ist begründet"),
       ("eil", "Ergebnis · Eilrechtsschutz")], [
    linienzug([(60, BODEN), (1860, BODEN)], "fall2", breite=7, farbe=INK),
    ficon("tabler", "sun", 1760, 190, 120, "fall2", fuell=GELB),
    *garten("fall2", welk="fall2"),
    schatten_flaeche(330, 1262, 300, BODEN, "fall2"),
    block_("fall2"),
    *fig("KO", KOX, BODEN, GH, [("fall2", "sorge_r"), ("erg", "froh_r")], bis="ko2"),
    *redet("KO_redet_r", KOX, BODEN, GH, "ko2", "tipp"),
    schild("Frau Kolbe", KOX, "fall2", KO_F, unten=BODEN),
    *fig("RE", REX, BODEN, GH, [("fall2", "ruhig"), ("rlos", "ernst"), ("erg", "denkt")]),
    schild("Herr Reimers, Bauherr", REX, "fall2", RE_F, unten=BODEN),
    pl("25 m hoch", BLX, 205, "fall2", fill=BLAU, size=30, anker="m"),
    pl("50 m lang", BLX, 920, beim("fall2", "fünfzig"), fill=BLAU, size=28, anker="m"),
    pl("14 m vor dem Haus", 900, 60, beim("fall2", "vierzehn"), fill=WEISS, size=30, anker="m", bis="erg"),
    pl("Grundstück vom Block beherrscht", 600, 130, beim("fall2", "beherrscht"), fill=WEISS, size=30, anker="m", bis="erg"),
    pl("neue Wohnungen: rechtfertigen das nicht", 600, 200, "wohn", fill=WEISS, size=30, anker="m", bis="erg"),
    pl("rücksichtslos", 600, 280, beim("rlos", "rücksichtslos"), fill=ROT, size=40, anker="m", bis="erg"),
    ficon(HC, "classical-building", 900, 420, 110, "erg", fuell=WEISS, bis="ko2"),
    pl("Klage begründet: Genehmigung aufgehoben", 900, 60, beim("erg", "Klage"), fill=GRUEN, size=30, anker="m", bis="ko2"),
    pl("§ 212a Abs. 1 BauGB: Klage hält den Bau nicht auf", 900, 125, beim("eil", "Paragraf"), fill=WEISS, size=28,
       anker="m", bis="ko2"),
    pl("Eilrechtsschutz: §§ 80a Abs. 3, 80 Abs. 5 VwGO", 900, 190, beim("eil", "Eilrechtsschutz"), fill=GELB, size=28,
       anker="m", bis="ko2"),
    pl("eigenes Video", 900, 435, beim("eil", "eigenes"), fill=GELB, size=26, anker="m", bis="ko2"),
    blase("sprech", 660, 150, "ko2", 420, 330, inhalt=["Dann muss Herr Reimers eben", "rücksichtsvoller planen."], textsize=30,
          figur=KOj),
])

# K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Klagebefugnis und Begründetheit trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne sauber:", 200, 200, beim("tipp", "Trenne"), "Bold", 34),
    z("Klagebefugnis: Verletzung des Rücksichtnahme-", 200, 280, "tipp1", "Bold", 34),
    z("gebots möglich", 240, 330, beim("tipp1", "möglich"), size=34),
    z("Begründetheit: Genehmigung rechtswidrig und", 200, 420, "tipp2", "Bold", 34),
    z("Nachbarin gerade dadurch in ihren Rechten verletzt", 240, 470, beim("tipp2", "Nachbarin"), size=34),
    z("Herkunft nennen: im Innenbereich das", 200, 560, "tipp3", "Bold", 34),
    z("Einfügen nach § 34 BauGB", 240, 610, beim("tipp3", "Einfügen"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Klausurschema ---------------------------------------------------------------------------------------------------------------------
SZ, LH = 36, 72
zeilen_ = [("s1", "A. Zulässigkeit", "Bold", 0),
           ("s2", "I. Anfechtungsklage gegen die Baugenehmigung", "Regular", 1),
           ("s3", "II. Klagebefugnis, § 42 Abs. 2 VwGO: drittschützende Norm möglich verletzt", "Regular", 1),
           ("s4", "B. Begründetheit, § 113 Abs. 1 Satz 1 VwGO", "Bold", 0),
           ("s5", "I. Verstoß gegen eine drittschützende Norm", "Regular", 1),
           ("s6", "1. Abstandsflächen, 2. Gebietserhaltungsanspruch", "Regular", 2),
           ("s7", "3. Rücksichtnahmegebot: Abwägung der Zumutbarkeit, erdrückende Wirkung", "Regular", 2),
           ("s8", "II. dadurch Verletzung eigener Rechte", "Regular", 1)]
els_t = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Klausurschema: Nachbarklage gegen die Baugenehmigung"), 110, 85, "sch", 46)]
for i, (c, t, s, e) in enumerate(zeilen_):
    els_t.append(z(t, 140 + 60 * e, 200 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · Nachbarklage, Rücksichtnahmegebot")], els_t)

# M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Als Nachbar kannst du nur", 0)]], 750, 330, 42, beim("merke", "Als"), {}),
    *markertext([[("drittschützende Normen", "a"), (" rügen.", 0)]], 750, 395, 42, beim("merke", "drittschützende"),
                {"a": beim("merke", "drittschützende")}),
    *markertext([[("Das ", 0), ("Rücksichtnahmegebot", "b"), (" schützt dich", 0)]], 750, 510, 42, "m2",
                {"b": beim("m2", "Rücksichtnahmegebot")}),
    *markertext([[("vor einem Bau, der dir ", 0), ("unzumutbar", "c"), (" ist,", 0)]], 750, 575, 42, beim("m2", "vor"),
                {"c": beim("m2", "unzumutbar")}),
    *markertext([[("etwa weil er dein Grundstück ", 0), ("erdrückt.", "d")]], 750, 640, 42, beim("m2", "etwa"),
                {"d": beim("m2", "erdrückt")}),
    *markertext([[("Schatten allein genügt ", 0), ("selten.", "e")]], 750, 735, 42, beim("m2", "Schatten"),
                {"e": beim("m2", "selten")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
