"""Folge 110 · Schutznormtheorie: Klagen gegen die Genehmigung eines anderen – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Shisha-Bar mit Terrasse im Nachbarhaus, Gaststättenerlaubnis; Beispielland NRW), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Wohnstraße (Fall, Frage), B Sachverhalt, C 1. Ausgangspunkt § 42 II (Wortlautkarte),
D 2. Schutznormtheorie, E Frage 1: Welche Norm? (Wortlautkarte § 4 I 1 Nr. 3 GastG), F Frage 2: Auslegung (§ 3 I BImSchG,
§ 5 I Nr. 3 GastG), G Frage 3: geschützter Kreis, Gegenfall, H 3. typische Normen (Tabelle ja/nein), I 4. Grundrechte,
J Ergebnis (Verwaltungsgericht), K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Gläser, als die Bar mit Glas-Icon erscheint). Hilfsfunktionen wie 105 (dort wie 102)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_110/"
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


def zz(kopf, rest, x, y, c_kopf, c_rest, stil="Bold", size=34, rest_stil=None, **k):
    """Zeile in zwei Teilen: Gliederungspunkt zur Marke, Inhalt erst zum gesprochenen Wort (nie vor dem Wort)."""
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
        if n.startswith(("bild:", "ficon:")) or "/op_110/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 074/069): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
F2A, F2B, F2H = 1400, 1720, 420             # zwei Figuren neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BR_F, HO_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
KD = "Klagebefugnis Dritter"

# A Fall: Wohnstraße, Shisha-Bar mit Terrasse, Gaststättenerlaubnis ---------------------------------------------------------
HOX, BRX = 1250, 1690
HOb = ("HO_redet_r", HOX, BODEN, FH)
BRb = ("BR_redet", BRX, BODEN, FH)
folie([(NULL, "Fall · Die Shisha-Bar nebenan"), ("erl", "Fall · Die Gaststättenerlaubnis"),
       ("frage", "Fall · Darf sie die Erlaubnis anfechten?")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Wohnstraße", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "home", 245, BODEN - 2, 320, NULL, fuell=BLAU, anim="cut"),
    hart(pl("Haus von Frau Brüning", 245, 520, NULL, fill=WEISS, size=28, anker="m")),
    ficon("tabler", "window", 300, 490, 80, beim("bar", "Schlafzimmerfenster"), fuell=BLAU),
    pl("Schlafzimmerfenster", 300, 368, beim("bar", "Schlafzimmerfenster"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "building-store", 760, BODEN - 2, 330, beim("bar", "Nachbarhaus"), fuell=GELB),
    pl("Shisha-Bar von Frau Hoppe", 760, 505, beim("bar", "Shisha"), fill=WEISS, size=28, anker="m"),
    szene(ficon("tabler", "glass-cocktail", 480, 788, 56, beim("bar", "Terrasse"), fuell=PINK), "110glas*", 0.8, -0.1),
    ficon("tabler", "umbrella", 480, 730, 150, beim("bar", "Terrasse"), fuell=ROT),
    ficon("tabler", "table", 480, BODEN - 2, 110, beim("bar", "Terrasse"), fuell=WEISS),
    pl("Terrasse", 480, 925, beim("bar", "Terrasse"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "license", 760, 330, 80, beim("erl", "Gaststättenerlaubnis"), fuell=WEISS),
    pl("Gaststättenerlaubnis: Bar und Terrasse", 760, 365, beim("erl", "Gaststättenerlaubnis"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "moon", 480, 250, 80, beim("erl", "Mitternacht"), fuell=GELB),
    pl("bis 24 Uhr", 480, 285, beim("erl", "Mitternacht"), fill=GELB, size=28, anker="m"),
    *fig("HO", HOX, BODEN, FH, [(beim("bar", "Frau"), "ruhig_r")], bis="ho1"),
    *redet("HO_redet_r", HOX, BODEN, FH, "ho1", "br1"),
    *fig("HO", HOX, BODEN, FH, [("br1", "stolz_r")], erst="cut", bis="frage"),
    *fig("HO", HOX, BODEN, FH, [("frage", "ruhig_r")], erst="cut"),
    schild("Frau Hoppe, Betreiberin", HOX, beim("bar", "Frau"), HO_F, unten=BODEN, d=0.0),
    *fig("BR", BRX, BODEN, FH, [(NULL, "ruhig"), (beim("erl", "Mitternacht"), "sorge")], bis="br1", erst="cut"),
    *redet("BR_redet", BRX, BODEN, FH, "br1", "frage"),
    *fig("BR", BRX, BODEN, FH, [("frage", "denkt")], erst="cut"),
    hart(schild("Frau Brüning", BRX, NULL, BR_F, unten=BODEN, d=0.0)),
    blase("sprech", 880, 230, "ho1", 1290, 200, inhalt=["Bei uns sitzt man draußen bis Mitternacht.",
                                                       "Die Erlaubnis habe ich!"], textsize=32, figur=HOb, bis="br1"),
    blase("sprech", 820, 270, "br1", 1290, 210, inhalt=["Bis Mitternacht unter meinem Fenster?",
                                                       "Dann kann ich nicht mehr schlafen.",
                                                       "Ich klage gegen diese Erlaubnis."], textsize=32, figur=BRb, bis="frage"),
    pl("Erlaubnis nicht an Frau Brüning gerichtet", 1400, 150, beim("frage", "richtet"), fill=WEISS, size=32, anker="m"),
    pl("Darf sie die Genehmigung einer anderen anfechten?", 1250, 240, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Brüning wohnt in einem Haus in einer ruhigen Wohnstraße in Nordrhein-Westfalen. Im Nachbarhaus eröffnet Frau "
    "Hoppe eine Shisha-Bar, die auch Bier und Cocktails ausschenkt. Die Stadt erteilt Frau Hoppe die Gaststättenerlaubnis "
    "für die Gasträume und eine Terrasse mit 40 Plätzen, Betrieb bis 24 Uhr.",
    "Die Terrasse liegt direkt unter dem Schlafzimmerfenster von Frau Brüning. Sie befürchtet, nachts nicht mehr schlafen "
    "zu können, und erhebt fristgerecht Anfechtungsklage gegen die Gaststättenerlaubnis.",
], "Ist Frau Brüning klagebefugt?")

# C 1. Ausgangspunkt § 42 Abs. 2 VwGO -----------------------------------------------------------------------------------------------
W422 = ("„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage nur zulässig, wenn der Kläger geltend macht, durch den "
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen Rechten verletzt zu sein.“")
Z422 = ["„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage",
        "nur zulässig, wenn der Kläger geltend macht, durch den",
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung",
        "in seinen Rechten verletzt zu sein.“"]
w422, w422_y = wortlaut(80, 170, 1100, W422, "§ 42 Abs. 2 VwGO", beim("p42", "Paragraf"), size=32, zeilen=Z422,
                        marken=[("geltend macht", beim("p42", "geltend")),
                                ("in seinen Rechten verletzt", beim("p42", "Rechten"))])
folie([("p42", f"{KD} › 1. Ausgangspunkt, § 42 II VwGO"), ("adr", f"{KD} › 1. Frau Brüning ist nicht Adressatin")], rechts_frei([
    titel(glyphen("1. Ausgangspunkt"), 110, 60, "p42", 44),
    *w422,
    z("Adressatentheorie: hilft Frau Brüning nicht", 110, w422_y + 30, beim("adr", "Adressatentheorie"), "Bold", 34),
    nein(850, w422_y + 50, beim("adr", "nicht")),
    z("Adressatin der Erlaubnis ist Frau Hoppe,", 150, w422_y + 90, beim("adr", "Adressatin"), size=34),
    z("und die Erlaubnis begünstigt sie.", 150, w422_y + 140, beim("adr", "begünstigt"), size=34),
    pl("Grundlagen: Video zur Klagebefugnis", 110, w422_y + 215, beim("v105", "Video"), fill=WEISS, size=28),
    *fig("BR", F2A, FB, F2H, [("p42", "ruhig"), ("adr", "denkt")]),
    schild("Frau Brüning", F2A, "p42", BR_F),
    *fig("HO", F2B, FB, F2H, [("p42", "ruhig"), (beim("adr", "begünstigt"), "stolz")]),
    schild("Frau Hoppe", F2B, "p42", HO_F),
    ficon("tabler", "license", (F2A + F2B) // 2, 380, 110, beim("adr", "Adressatin"), fuell=GRUEN),
]))

# D 2. Schutznormtheorie ---------------------------------------------------------------------------------------------------------------
folie([("snt", f"{KD} › 2. Schutznormtheorie")], rechts_frei([
    *tafel("snt", "2. Schutznormtheorie"),
    z("Ein Dritter braucht eine Norm,", 110, 180, beim("snt", "Ein"), "Bold", 36),
    z("die zumindest auch ihn schützt.", 150, 235, beim("snt", "zumindest"), "Bold", 36),
    karte(110, 310, 1040, 230, beim("kreis", "Norm"), fill=GELB, rund=18, schatten=0, rand=5),
    z("Die Norm grenzt hinreichend deutlich ab:", 140, 328, beim("kreis", "Norm"), "ExtraBold", 34),
    z("· das geschützte private Interesse", 160, 382, beim("kreis", "geschützte"), size=32),
    z("· die Art seiner Verletzung", 160, 428, beim("kreis", "Art"), size=32),
    z("· den Kreis der geschützten Personen", 160, 474, beim("kreis", "Kreis"), size=32),
    zit("BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 40", 150, 560, beim("kreis", "abgrenzen")),
    z("Es genügt ein Personenkreis, der sich hinreichend", 110, 620, beim("allg", "Personenkreis"), size=34),
    z("von der Allgemeinheit unterscheidet.", 150, 670, beim("allg", "Allgemeinheit"), size=34),
    z("nur reflexartig mitbetroffen: kein eigenes Recht", 110, 745, beim("reflex", "reflexartig"), "Bold", 34),
    nein(990, 765, beim("reflex", "kein")),
    zit("BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 24", 150, 800, beim("reflex", "Recht")),
    ficon("tabler", "shield-check", IX, IU - 20, 130, "snt", fuell=GRUEN),
    pl("Schutznorm", IX, 190, beim("snt", "Norm"), fill=GRUEN, size=30, anker="m"),
    *fig("BR", FX, FB, FR, [("snt", "ruhig"), ("allg", "denkt")]),
    schild("Frau Brüning", FX, "snt", BR_F),
]))

# E Frage 1: Welche Norm? Wortlautkarte § 4 Abs. 1 Satz 1 Nr. 3 GastG ------------------------------------------------------------------
W4 = ("„Die Erlaubnis ist zu versagen, wenn … 3. der Gewerbebetrieb im Hinblick auf seine örtliche Lage oder auf die "
      "Verwendung der Räume dem öffentlichen Interesse widerspricht, insbesondere schädliche Umwelteinwirkungen im Sinne des "
      "Bundes-Immissionsschutzgesetzes oder sonst erhebliche Nachteile, Gefahren oder Belästigungen für die Allgemeinheit "
      "befürchten läßt, …“")
Z4 = ["„Die Erlaubnis ist zu versagen, wenn …",
      "3. der Gewerbebetrieb im Hinblick auf seine örtliche Lage oder",
      "auf die Verwendung der Räume dem öffentlichen Interesse",
      "widerspricht, insbesondere schädliche Umwelteinwirkungen im",
      "Sinne des Bundes-Immissionsschutzgesetzes oder sonst erhebliche",
      "Nachteile, Gefahren oder Belästigungen für die Allgemeinheit",
      "befürchten läßt, …“"]
w4, w4_y = wortlaut(80, 335, 1100, W4, "§ 4 Abs. 1 Satz 1 Nr. 3 GastG", beim("wl4", "Paragraf"), size=30, zeilen=Z4,
                    marken=[("örtliche Lage", beim("wl4", "örtliche")),
                            ("schädliche Umwelteinwirkungen", beim("wl4", "schädliche")),
                            ("befürchten läßt,", beim("wl4", "befürchten"))])
folie([("fa", f"{KD} › 2. Frage 1: Welche Norm?"), ("wl4", f"{KD} › 2. Frage 1: § 4 I 1 Nr. 3 GastG")], rechts_frei([
    titel(glyphen("Frage 1: Welche Norm?"), 110, 60, "fa", 44),
    z("Beispielland Nordrhein-Westfalen: Gaststättengesetz", 110, 145, beim("nrw", "Nordrhein"), "Bold", 32),
    z("des Bundes gilt fort", 150, 190, beim("nrw", "gilt"), "Bold", 32),
    z("andere Länder: eigene Gaststättengesetze", 110, 240, beim("nrw", "andere"), size=32),
    zit("Art. 125a Abs. 1 GG – in deinem Land ggf. andere Norm", 150, 285, beim("nrw", "Gesetze")),
    *w4,
    zit("Fallannahme: Ausschank auch von Bier und Cocktails, also erlaubnispflichtig (§ 2 GastG)", 110, w4_y + 20,
        beim("wl4", "befürchten"), rechts=1185),
    ficon("tabler", "building-store", IX, IU - 10, 150, "fa", fuell=GELB),
    pl("Shisha-Bar", IX, 200, "fa", fill=WEISS, size=30, anker="m"),
    *fig("BR", FX, FB, FR, [("fa", "denkt"), ("wl4", "ruhig")]),
    schild("Frau Brüning", FX, "fa", BR_F),
]))

# F Frage 2: Schützt sie auch Einzelne? Wortlaut, Systematik, Zweck --------------------------------------------------------------------
W3 = ("„… Immissionen, die nach Art, Ausmaß oder Dauer geeignet sind, Gefahren, erhebliche Nachteile oder erhebliche "
      "Belästigungen für die Allgemeinheit oder die Nachbarschaft herbeizuführen.“")
Z3 = ["„… Immissionen, die nach Art, Ausmaß oder Dauer geeignet sind,",
      "Gefahren, erhebliche Nachteile oder erhebliche Belästigungen",
      "für die Allgemeinheit oder die Nachbarschaft herbeizuführen.“"]
w3, w3_y = wortlaut(100, 255, 1080, W3, "§ 3 Abs. 1 BImSchG", beim("wort", "Schädliche"), size=30, zeilen=Z3,
                    marken=[("die Nachbarschaft", beim("wort", "Nachbarschaft"))])
folie([("fb", f"{KD} › 2. Frage 2: Schützt sie auch Einzelne?")], rechts_frei([
    titel(glyphen("Frage 2: Schützt sie auch Einzelne?"), 110, 60, "fb", 44),
    z("Auslegung: Wortlaut – Systematik – Zweck", 110, 145, beim("fb", "Auslegung"), "Bold", 34),
    z("Wortlaut: schädliche Umwelteinwirkungen", 110, 200, beim("wort", "Wortlaut"), "Bold", 32),
    *w3,
    z("Systematik: § 5 Abs. 1 Nr. 3 GastG – Auflagen zum Schutz", 110, w3_y + 22, beim("sys", "Systematik"), "Bold", 32),
    z("„für die Bewohner … der Nachbargrundstücke“", 150, w3_y + 68, beim("sys", "Bewohner"), size=32),
    z("Zweck: Konflikt zwischen Gaststätte und Wohnen lösen", 110, w3_y + 128, beim("zweck", "Zweck"), "Bold", 32),
    zit("OVG NRW, Beschl. v. 3.11.2015 – 4 B 652/15, Rn. 27, 32", 150, w3_y + 172, beim("zweck", "Wohnen")),
    karte(110, w3_y + 220, 1040, 70, beim("ja", "Insoweit"), fill=GRUEN, rund=18, schatten=0, rand=5),
    z("insoweit drittschützend", 140, w3_y + 232, beim("ja", "Insoweit"), "ExtraBold", 34),
    ok(590, w3_y + 252, beim("ja", "drittschützend")),
    zit("BVerwG, Urt. v. 12.12.2019 – 8 C 3.19, Rn. 39", 150, w3_y + 305, beim("ja", "Bundesverwaltungsgericht")),
    ficon("tabler", "home", IX, IU - 20, 130, beim("sys", "Bewohner"), fuell=BLAU),
    pl("Nachbarschaft", IX, 210, beim("wort", "Nachbarschaft"), fill=GELB, size=30, anker="m"),
    *fig("BR", FX, FB, FR, [("fb", "ruhig"), ("wort", "denkt"), (beim("ja", "drittschützend"), "froh")]),
    schild("Frau Brüning", FX, "fb", BR_F),
]))

# G Frage 3: Gehört Frau Brüning zum geschützten Kreis? Gegenfall ---------------------------------------------------------------------------
folie([("fc", f"{KD} › 2. Frage 3: Gehört Frau Brüning dazu?"), ("gegen", f"{KD} › 2. Frage 3: Gegenfall")], rechts_frei([
    *tafel("fc", "Frage 3: Geschützter Kreis?"),
    z("Nachbarschaft: wer im Einwirkungsbereich", 110, 180, beim("nachb", "Nachbarschaft"), "Bold", 36),
    z("des Betriebs wohnt", 150, 235, beim("nachb", "Betriebs"), "Bold", 36),
    zit("vgl. BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 43 (Lage des Grundstücks)", 150, 287, beim("nachb", "wohnt")),
    z("Frau Brüning: direkt über der Terrasse", 110, 345, beim("nachb", "Frau", 1), size=36),
    ok(790, 368, beim("nachb", "Terrasse")),
    z("Erhebliche Belästigung bis 24 Uhr?", 110, 430, beim("moegl", "Dass"), size=36),
    z("nicht offensichtlich ausgeschlossen", 150, 485, beim("moegl", "nicht"), "ExtraBold", 36),
    ok(860, 508, beim("moegl", "ausgeschlossen")),
    zit("Möglichkeit genügt: BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 13", 150, 540, beim("moegl", "ausgeschlossen")),
    karte(110, 610, 1040, 190, beim("gegen", "Anders"), fill=HELL, rund=18, schatten=0, rand=5),
    z("Gegenfall:", 140, 628, beim("gegen", "Anders"), "ExtraBold", 34),
    z("wohnt 3 Straßen weiter, hört vom Lärm nichts", 140, 680, beim("gegen", "drei"), size=34),
    z("und mag Shisha-Bars einfach nicht", 140, 730, beim("gegen", "Shisha"), size=34),
    nein(760, 750, beim("gegen", "mag")),
    ficon("tabler", "bed", IX - 70, IU - 20, 110, beim("nachb", "Terrasse"), fuell=WEISS, bis="gegen"),
    ficon("tabler", "moon", IX + 80, IU - 60, 80, beim("moegl", "Mitternacht"), fuell=GELB, bis="gegen"),
    ficon("tabler", "map-pin", IX, IU - 20, 100, beim("gegen", "drei"), fuell=ROT),
    pl("3 Straßen weiter", IX, 200, beim("gegen", "drei"), fill=WEISS, size=30, anker="m"),
    *fig("BR", FX, FB, FR, [("fc", "ruhig"), (beim("moegl", "belästigen"), "sorge"), ("gegen", "denkt")]),
    schild("Frau Brüning", FX, "fc", BR_F),
]))

# H 3. Typische Normen: drittschützend ja/nein (Tabelle, volle Breite wie Schema) ----------------------------------------------------------
els_t = [karte(60, 50, 1800, 900, "tab"), titel(glyphen("3. Typische Normen: drittschützend?"), 110, 85, "tab", 46),
         z("Norm", 110, 175, "tab", "ExtraBold", 30, farbe=TEXT, rechts=1820),
         z("drittschützend?", 1190, 175, "tab", "ExtraBold", 30, farbe=TEXT, rechts=1820),
         z("Beleg", 1440, 175, "tab", "ExtraBold", 30, farbe=TEXT, rechts=1820)]
ZEILEN_T = [  # (y, Text-cue, Haupttext, Untertext, Untertext-cue, ja, ja-cue, Belege)
    (225, beim("t1", "Schutz"), "Schutz vor schädlichen Umwelteinwirkungen im Gaststättenrecht",
     "§ 4 Abs. 1 Satz 1 Nr. 3 GastG", beim("t1", "Gaststättenrecht"), True, "t1",
     ["BVerwG 8 C 3.19, Rn. 39", "OVG NRW 4 B 652/15, Rn. 27"]),
    (325, beim("t2", "Schutzpflicht"), "Schutzpflicht für genehmigungsbedürftige Anlagen",
     "§ 5 Abs. 1 Nr. 1 BImSchG", beim("t2", "Paragraf"), True, beim("t2", "ebenso"),
     ["Wortlaut: „Nachbarschaft“"]),
    (425, beim("t3", "Abstandsflächen"), "Abstandsflächen der Landesbauordnung", None, None, True, beim("t3", "schützen"),
     ["BVerwG 4 B 52.15, Rn. 9"]),
    (510, beim("t4", "Art"), "Art der baulichen Nutzung: Gebietserhaltungsanspruch", None, None, True, "t4",
     ["BVerwG 4 C 6.20, Rn. 8"]),
    (675, beim("t5", "Vorsorgepflicht"), "Vorsorgepflicht", "§ 5 Abs. 1 Nr. 2 BImSchG – dient der Allgemeinheit",
     beim("t5", "dient"), False, "t5", ["BVerwG 7 B 2.08, Rn. 15"]),
    (775, beim("t6", "Festsetzungen"), "Festsetzungen zum Maß der baulichen Nutzung",
     "nur, wenn die Gemeinde als Plangeber das will", beim("t6", "nur"), False, beim("t6", "nur"),
     ["BVerwG 4 C 7.17, Rn. 14"]),
]
for y, c, txt, sub, csub, ja, cja, belege in ZEILEN_T:
    els_t.append(z(txt, 110, y, c, "Bold", 32, rechts=1170))
    if sub:
        els_t.append(z(sub, 130, y + 44, csub, size=28, farbe=TEXT, rechts=1170))
    cja = c if T_(cja) < T_(c) else cja        # ja/nein nie vor der gesprochenen Norm (Sprechreihenfolge)
    els_t.append(pl("ja" if ja else "nein", 1190, y - 4, cja, fill=GRUEN if ja else ROT, size=30))
    els_t.append(ok(1330, y + 22, cja) if ja else nein(1350, y + 22, cja))
    for i, b in enumerate(belege):
        els_t.append(zit(b, 1440, y + 4 + i * 40, cja, rechts=1820))
els_t.append(pl("Baurecht: Videos zum Rücksichtnahmegebot und zur Drittanfechtung", 110, 585, beim("bau", "Videos"),
                fill=WEISS, size=28))
folie([("tab", f"{KD} › 3. Typische Normen: drittschützend?")], els_t)

# I 4. Grundrechte nur hilfsweise --------------------------------------------------------------------------------------------------------------
folie([("grund", f"{KD} › 4. Grundrechte nur hilfsweise")], rechts_frei([
    *tafel("grund", "4. Grundrechte", h=520),
    z("Als Schutznorm nur hilfsweise:", 110, 190, beim("grund", "hilfsweise"), "Bold", 36),
    z("Zuerst entscheidet das einfache Gesetz,", 150, 260, beim("grund", "Zuerst"), size=36),
    z("wen es schützt.", 150, 315, beim("grund", "wen"), size=36),
    zit("vgl. BVerwG, Urt. v. 21.4.2009 – 4 C 3.08, Rn. 15", 150, 380, beim("grund", "schützt")),
    ficon("tabler", "book", IX - 120, IU - 20, 110, beim("grund", "Gesetz"), fuell=WEISS),
    pl("Gesetz", IX - 120, 200, beim("grund", "Gesetz"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "shield", IX + 120, IU - 20, 90, "grund", fuell=LILA),
    pl("Grundrechte", IX + 120, 200, "grund", fill=LILA, size=28, anker="m"),
    *fig("BR", FX, FB, FR, [("grund", "ruhig")]),
    schild("Frau Brüning", FX, "grund", BR_F),
]))

# J Ergebnis: Verwaltungsgericht --------------------------------------------------------------------------------------------------------------
RIX, BRX3, HOX3 = 760, 1330, 1690
RIb = ("RI_redet_r", RIX, BODEN, FH)
folie([("erg", "Ergebnis · Frau Brüning ist klagebefugt")], [
    linienzug([(60, BODEN), (1860, BODEN)], "erg", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "erg", fill=GELB, size=40),
    ficon(HC, "classical-building", 290, BODEN - 2, 340, "erg", fuell=WEISS),
    pl("Lärmschutz im Gaststättengesetz", 290, 410, beim("erg", "Lärmschutz"), fill=WEISS, size=26, anker="m"),
    pl("Frau Brüning: klagebefugt", 290, 470, beim("erg", "klagebefugt"), fill=GRUEN, size=28, anker="m"),
    ok(565, 470, beim("erg", "klagebefugt")),
    pl("Begründetheit: offen", 290, 530, beim("ri1", "Begründetheit"), fill=WEISS, size=28, anker="m"),
    *fig("RI", RIX, BODEN, FH, [("ri", "ruhig_r")], bis="ri1"),
    *redet("RI_redet_r", RIX, BODEN, FH, "ri1", "tipp"),
    schild("der Richter", RIX, "ri", RI_F, unten=BODEN),
    *fig("BR", BRX3, BODEN, FH, [("erg", "ruhig"), (beim("ri1", "Frau"), "froh")]),
    schild("Frau Brüning", BRX3, "erg", BR_F, unten=BODEN),
    *fig("HO", HOX3, BODEN, FH, [("erg", "ruhig"), (beim("ri1", "Ob"), "denkt")]),
    schild("Frau Hoppe", HOX3, "erg", HO_F, unten=BODEN),
    blase("sprech", 900, 270, "ri1", 1260, 200, inhalt=["Sie sind klagebefugt, Frau Brüning.",
                                                       "Ob die Terrasse wirklich zu laut ist,",
                                                       "prüfen wir in der Begründetheit."], textsize=32, figur=RIb),
])

# K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Schutznorm schon in der Klagebefugnis"), ("tipp2", "Klausurtipp · Begründetheit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Drittanfechtung: schon in der Klagebefugnis", 200, 180, beim("tipp", "Drittanfechtung"), "Bold", 34),
    z("die konkrete Schutznorm nennen", 200, 232, beim("tipp", "konkrete"), "Bold", 34),
    z("und kurz begründen, warum sie auch", 200, 300, beim("tipp", "begründest"), size=34),
    z("den Kläger schützt", 200, 350, beim("tipp", "Kläger"), size=34),
    karte(110, 500, 1040, 250, beim("tipp2", "Begründetheit"), fill=WEISS, rund=18, schatten=0, rand=5),
    z("Begründetheit: zählen nur Verstöße gegen", 140, 520, beim("tipp2", "Begründetheit"), "Bold", 34),
    z("drittschützende Normen", 140, 572, beim("tipp2", "drittschützende"), "Bold", 34),
    z("Fehler allein zulasten der Allgemeinheit:", 140, 640, beim("tipp2", "Fehler"), size=34),
    z("hilft dem Nachbarn nicht", 140, 690, beim("tipp2", "hilft"), "Bold", 34),
    nein(590, 710, beim("tipp2", "nicht")),
    zit("§ 113 Abs. 1 Satz 1 VwGO: „… dadurch in seinen Rechten verletzt …“", 140, 770, beim("tipp2", "Normen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Schema --------------------------------------------------------------------------------------------------------------------------
SZ, LH = 38, 92
els_s = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Schema: Klagebefugnis Dritter, § 42 Abs. 2 VwGO"), 110, 85, "sch", 46)]
zeilen_s = [
    zz("1. Ausgangspunkt:", "§ 42 Abs. 2 VwGO – der Dritte ist nicht Adressat", 110, 195, "s1", beim("s1", "Paragraf"),
       size=SZ, rest_stil="Regular", rechts=1820),
    [z("2. Schutznorm:", 110, 195 + LH, "s2", "Bold", SZ, rechts=1820)],
    [z("a) Welche Norm?", 170, 195 + 2 * LH, "s2a", "Bold", SZ, rechts=1820)],
    zz("b) Schützt sie auch Einzelne?", "Wortlaut, Systematik, Zweck", 170, 195 + 3 * LH, "s2b", beim("s2b", "Wortlaut"),
       size=SZ, rest_stil="Regular", rechts=1820),
    zz("c) Kläger im geschützten Kreis?", "Verletzung möglich?", 170, 195 + 4 * LH, "s2c", beim("s2c", "Verletzung"),
       size=SZ, rest_stil="Regular", rechts=1820),
    zz("3. Typische Schutznormen:", "Lärmschutz, Abstandsflächen, Gebietserhaltung – nicht: Vorsorge", 110, 195 + 5 * LH,
       "s3", beim("s3", "Lärmschutz"), size=SZ, rest_stil="Regular", rechts=1820),
    zz("4. Grundrechte:", "nur hilfsweise", 110, 195 + 6 * LH, "s4", beim("s4", "hilfsweise"), size=SZ, rest_stil="Regular",
       rechts=1820),
]
for zl in zeilen_s:
    els_s += zl
folie([("sch", "Schema · Klagebefugnis Dritter")], els_s)

# M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Genehmigung eines anderen greifst du", 0)]], 750, 320, 44, "merke", {}),
    *markertext([[("nur mit einer Norm an, die ", 0), ("auch dich schützt.", "a")]], 750, 385, 44, beim("merke", "nur"),
                {"a": beim("merke", "auch")}),
    *markertext([[("Die Nachbarin findet sie ", 0), ("im Lärmschutz.", "b")]], 750, 540, 44, "m2",
                {"b": beim("m2", "Lärmschutz")}),
    *markertext([[("Wer nur dagegen ist, findet keine.", 0)]], 750, 640, 44, beim("m2", "Wer"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
