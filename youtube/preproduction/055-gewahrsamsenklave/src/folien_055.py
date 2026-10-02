"""Folge 055 · Ladendiebstahl: Wann ist die Ware weg? Gewahrsamsenklave erklärt – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Supermarkt (Fall), B Sachverhalt (Grundfall, drei Varianten), C Wortlaut § 242,
D Sache und Wegnahme, E Gewahrsamsenklave, F Beobachtung und Ergebnis, G Variante 1 (zurück ins Regal, § 24),
H Variante 2 (Kiste im Einkaufswagen), I Variante 3 (Versteck unter der Zeitung), J Folgen (Rücktritt, § 252),
K Strafantrag und Festnahme (§ 248a, § 127 StPO), L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Geräusche: nur Handlungsgeräusche – Lippenstift in die Jackentasche (szene_055tasche_1) und Kiste Wein in den
Einkaufswagen (szene_055kiste_1)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_055/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobile Lesbarkeit: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def zitat(text, x, y, cue, size=26, **k):
    """BGH-Fundstelle unter einer Aussage (klein, grau, mindestens 26 px)."""
    return z(text, x, y, cue, "Bold", size, farbe=TEXT, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (zweizeilige Blöcke bleiben im Kasten)."""
    for t_, *_ in zeilen:
        glyphen(t_)
        assert F(_[0], _[1]).getlength(t_) <= w - 40, f"Block zu breit: {t_}"
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def umbruch(text, breite, size):
    f = F("Regular", size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter die Wortgruppe (sie muss in einer Zeile stehen)."""
    zeilen = umbruch(text, w - 60, size)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
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


def sachverhalt_klein(cue, absaetze, frage, size=34, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber Schrift passend zu Grundfall und drei Varianten."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 14
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


# --- Eigene Hilfsfunktion (wie Folge 029/035/042/047): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----
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
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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



# --- Figuren und Namensschilder ----------------------------------------------------------------------------------------
NAMEN = {"MO": ("Monika", LILA), "RA": ("Rainer", GRUEN)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
MX, RX = 1420, 1740                         # Monika links, Rainer rechts
PY = 420                                    # Pillen über den Köpfen


def name(p, cx, cue, unten=BR, size=28, d=0.0, bis=None, anim="cut"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def lippenstift(cx, unten, breite, cue, bis=None, anim="pop"):
    """Lippenstift (Fluent Emoji High Contrast: lipstick, MIT)."""
    return ficon("fluent-emoji-high-contrast", "lipstick", cx, unten, breite, cue, fuell=ROT, bis=bis, anim=anim)


def kiste(cx, unten, breite, cue, bis=None, anim="pop"):
    """Kiste Wein: Karton (tabler box) mit zwei Flaschenhälsen (tabler bottle)."""
    els = [ficon("tabler", "bottle", cx - breite * 0.18, unten - breite * 0.55, breite * 0.42, cue, fuell=GRUEN, bis=bis, anim=anim),
           ficon("tabler", "bottle", cx + breite * 0.16, unten - breite * 0.55, breite * 0.42, cue, fuell=GRUEN, bis=bis, anim=anim),
           ficon("tabler", "box", cx, unten, breite, cue, fuell=ORANGE, bis=bis, anim=anim)]
    return els


def paar(cue, mo_folge, ra_folge, mx=MX, rx=RX):
    """Monika und Rainer rechts neben der Tafel, je mit Namensschild ab Folienbeginn."""
    return [*fig("MO", mx, BR, FR, mo_folge, erst="cut"), name("MO", mx, cue),
            *fig("RA", rx, BR, FR, ra_folge, erst="cut"), name("RA", rx, cue)]


def tasche_ring(cx, unten, hoehe, cue, bis=None):
    """Ring um die Jackentasche von Monika (Grundansicht blickt nach links)."""
    return ring(round(cx + 0.045 * hoehe), round(unten - 0.555 * hoehe), round(0.075 * hoehe), round(0.06 * hoehe), cue, bis=bis)


# A Fall: Supermarkt ----------------------------------------------------------------------------------------------------
BA = 900                                    # Boden im Laden
SH = 560                                    # Standhöhe im Fall
MOA, MOB, RAA = 720, 1060, 1420             # Monika am Regal, Monika auf dem Weg zur Kasse, Rainer
RG = (140, 380, 380, 520)                   # Kosmetikregal
KS = (1580, 700, 280, 200)                  # Kassentresen
NULL = ("fall", -0.4)
MOb = ("MO_redet", MOA, BA, SH)
RAb = ("RA_redet", RAA, BA, SH)
folie([(NULL, "Fall · Der Supermarkt"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(80, BA + 2), (1840, BA + 2)], NULL, breite=6, farbe=INK)),
    pl("Samstagvormittag", 100, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Supermarkt", 100, 140, beim("fall", "Supermarkt"), fill=WEISS, size=30),
    # Kosmetikregal mit drei Böden
    hart(karte(*RG, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    *[hart(linienzug([(RG[0] + 8, y), (RG[0] + RG[2] - 8, y)], NULL, breite=5, farbe=INK)) for y in (540, 700)],
    pl("Kosmetik", RG[0] + RG[2] / 2, RG[1] + 18, NULL, fill=PINK, size=28, anker="m", anim="cut"),
    *[hart(lippenstift(x, 532, 34, NULL, anim="cut")) for x in (200, 260, 320, 380)],
    lippenstift(440, 532, 34, NULL, anim="cut", bis="lippen"),
    *[hart(ficon("tabler", "perfume", x, 692, 56, NULL, fuell=LILA, anim="cut")) for x in (210, 330, 450)],
    *[hart(ficon("tabler", "spray", x, 880, 56, NULL, fuell=GRUEN, anim="cut")) for x in (210, 330, 450)],
    # Kasse rechts
    hart(karte(*KS, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    hart(ficon("tabler", "barcode", KS[0] + 140, KS[1] - 4, 70, NULL, fuell=WEISS, anim="cut")),
    pl("Kasse", KS[0] + 140, KS[1] + 70, NULL, fill=GELB, size=28, anker="m", anim="cut"),
    # Monika am Regal
    *fig("MO", MOA, BA, SH, [(beim("monika", "Monika"), "ruhig"), ("lippen", "denkt"), ("umsehen", "listig_r"),
                             (beim("umsehen", "um"), "listig"), ("tasche", "listig")], bis="mo1"),
    *redet("MO_redet", MOA, BA, SH, "mo1", "rainer"),
    *fig("MO", MOA, BA, SH, [("rainer", "froh")], bis="kasse", erst="cut"),
    *fig("MO", MOB, BA, SH, [("kasse", "ruhig_r"), ("ra1", "erschrickt_r"), ("frage", "erschrickt_r")], erst="cut"),
    name("MO", MOA, beim("monika", "Monika"), unten=BA - 6, anim="pop", bis="kasse"),
    name("MO", MOB, "kasse", unten=BA - 6),
    lippenstift(MOA - 98, 655, 52, "lippen", bis="tasche"),
    pl("Lippenstift · 9 €", MOA - 120, 270, beim("lippen", "Lippenstift"), fill=GELB, size=28, anker="m", bis="mo1"),
    pl("schaut sich um", MOA + 200, 270, "umsehen", fill=WEISS, size=28, anker="m", bis="tasche"),
    szene(tasche_ring(MOA, BA, SH, "tasche", bis="kasse"), "055tasche*", 0.8, 0.1),
    pl("in die Jackentasche", MOA + 220, 270, "tasche", fill=PINK, size=28, anker="m", bis="mo1"),
    pl("will nicht zahlen", MOA + 220, 200, beim("tasche", "Bezahlen"), fill=WEISS, size=28, anker="m", bis="mo1"),
    blase("sprech", 560, 200, "mo1", 1120, 220, inhalt=["Den behalte ich", "einfach."], textsize=36,
          figur=MOb, bis="rainer"),
    # Rainer beobachtet über den Deckenspiegel
    *fig("RA", RAA, BA, SH, [("rainer", "beobachtet"), ("spiegel", "wach"), ("kasse", "beobachtet")], bis="ra1"),
    *redet("RA_redet", RAA, BA, SH, "ra1", "frage"),
    *fig("RA", RAA, BA, SH, [("frage", "ruhig")], erst="cut"),
    name("RA", RAA, "rainer", unten=BA - 6, anim="pop"),
    pl("Ladendetektiv", RAA, 270, beim("spiegel", "Ladendetektiv"), fill=GRUEN, size=28, anker="m", bis="anspr"),
    ficon("fluent-emoji-high-contrast", "mirror", 960, 250, 110, "spiegel", fuell=BLAU, bis="ra1"),
    pl("Spiegel an der Decke", 960, 64, beim("spiegel", "Spiegel"), fill=WEISS, size=28, anker="m", bis="ra1"),
    ficon("tabler", "eye", 1120, 210, 70, beim("spiegel", "beobachtet"), fuell=WEISS, bis="ra1"),
    pl("Richtung Kasse", 1720, 560, "kasse", fill=WEISS, size=28, anker="m", bis="anspr"),
    pl("noch vor der Kasse", 1720, 560, beim("anspr", "Kasse"), fill=PINK, size=28, anker="m"),
    blase("sprech", 720, 250, "ra1", 1000, 200, inhalt=["Entschuldigung, ich bin der", "Ladendetektiv. Kommen", "Sie bitte kurz mit."],
          textsize=32, figur=RAb, bis="frage"),
    # Frage
    pl("Diebstahl schon vollendet?", 960, 190, "frage", fill=PINK, size=36, anker="m"),
    pl("noch im Laden · alles gesehen", 1000, 265, "frage2", fill=WEISS, size=28, anker="m"),
    pl("Grundfall und drei Varianten", 1630, 120, "frage3", fill=GELB, size=28, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Samstagvormittag im Supermarkt: Monika nimmt am Kosmetikregal einen Lippenstift für 9 Euro, schaut sich um und "
    "steckt ihn in ihre Jackentasche. Bezahlen will sie ihn nicht. Ladendetektiv Rainer beobachtet alles über einen "
    "Spiegel an der Decke. Noch bevor Monika die Kasse erreicht, spricht er sie ruhig an.",
    "Variante 1: Bevor Rainer sie anspricht, legt Monika den Lippenstift von sich aus zurück ins Regal.",
    "Variante 2: Monika stellt eine schwere Kiste Wein offen in den Einkaufswagen, um sie ohne Bezahlung "
    "hinauszuschieben. Rainer spricht sie vor der Kasse an.",
    "Variante 3: Monika versteckt den Lippenstift im Einkaufswagen unter einer Zeitung und legt an der Kasse nur die "
    "übrigen Waren aufs Band.",
], "Hat Monika einen vollendeten Diebstahl begangen?")

# C Wortlaut § 242 -----------------------------------------------------------------------------------------------------
T242 = ("„Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten "
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“")
wl242, y242 = wortlaut(90, 170, 1090, T242, "§ 242 Abs. 1 StGB", "p242", size=32,
                       marken=[("wegnimmt", beim("p242w", "wegnimmt"))])
wl2, y2 = wortlaut(90, y242 + 24, 1090, "„Der Versuch ist strafbar.“", "§ 242 Abs. 2 StGB", "abs2", size=32)
folie([("p242", "§ 242 StGB › Wortlaut")], [
    *tafel("p242", "Diebstahl, § 242 StGB", h=y2 + 30 + 90 + 40 - 60),
    *wl242, *wl2,
    blk(110, y2 + 30, 1040, 90, GELB, "kern", [("vollendet oder versucht? Das entscheidet die Wegnahme", "ExtraBold", 31, INK)]),
    *paar("p242", [("p242", "ruhig"), ("abs2", "denkt")], [("p242", "ruhig"), ("kern", "beobachtet")]),
    lippenstift(1580, 380, 80, beim("p242w", "wegnimmt")),
])

# D Sache, Wegnahme, Gewahrsam des Supermarkts -------------------------------------------------------------------------
PO = "Grundfall › I. Tatbestand › 1. objektiv"
folie([("sache", f"{PO} › a) fremde bewegliche Sache"), ("wegn", f"{PO} › b) Wegnahme")], [
    *tafel("sache", "Sache und Wegnahme", h=650),
    ok(135, 213, beim("sache", "Supermarkt"), gr=22), z("fremde bewegliche Sache: gehört dem Supermarkt", 175, 190, "sache", size=34),
    z("Wegnahme: Bruch fremden und", 110, 290, "wegn", "Bold", 34),
    z("Begründung neuen Gewahrsams", 110, 337, beim("wegn", "Bruch"), "Bold", 34),
    zitat("BGH, Urt. v. 6.3.2019 – 5 StR 593/18, Rn. 3", 110, 387, beim("wegn", "Gewahrsams")),
    blk(110, 460, 1040, 80, GELB, "gewahr", [("Gewahrsam zunächst: der Supermarkt", "ExtraBold", 34, INK)]),
    z("das Regal steht in seinem Laden", 110, 565, beim("gewahr", "Regal"), size=34),
    *paar("sache", [("sache", "ruhig"), ("gewahr", "denkt")], [("sache", "ruhig"), ("wegn", "beobachtet")]),
    ficon("tabler", "building-store", 1580, 330, 130, beim("gewahr", "Supermarkt"), fuell=GELB),
    lippenstift(1580, 140 + 40, 40, "sache"),
    pl("gehört dem Supermarkt", 1580, 80 + 120, beim("sache", "gehört"), fill=WEISS, size=28, anker="m", bis="gewahr"),
])

# E Gewahrsamsenklave ------------------------------------------------------------------------------------------------
LX0, LY0, LW, LH = 1270, 120, 590, 860      # Laden als großer Gewahrsamsbereich
EMX = 1620
folie([("enkl", f"{PO} › b) Wegnahme › Gewahrsamsenklave")], [
    *tafel("enkl", "Gewahrsamsenklave", h=840),
    z("kleine, leicht bewegliche Sachen:", 110, 185, "klein", "Bold", 34),
    z("Einstecken in die Kleidung genügt", 110, 232, beim("klein", "Einstecken"), size=34),
    z("Tasche der Kleidung: Sachherrschaft beim Träger,", 110, 305, "tasche2", size=33),
    z("auch noch im Laden", 110, 350, "mitten", "Bold", 33),
    zitat("BGH 5 StR 593/18, Rn. 4 f. · BGH 3 StR 556/09, Rn. 11 f.", 110, 400, beim("mitten", "Laden")),
    blk(110, 470, 1040, 120, GELB, beim("enkl2", "Gewahrsamsenklave"), [("Gewahrsamsenklave: eigene Sphäre", "ExtraBold", 34, INK),
                                                                         ("mitten im fremden Bereich", "Bold", 32, INK)]),
    z("so schon BGHSt 16, 271 (1961), bis heute", 110, 625, "seit", size=33),
    blk(110, 700, 1040, 80, GRUEN, "vollendet", [("Wegnahme mit dem Einstecken vollendet", "ExtraBold", 34, INK)]),
    # rechts: der Laden als Gewahrsamsbereich, darin die Jackentasche als Enklave
    karte(LX0, LY0, LW, LH, "enkl", fill=(232, 240, 253, 255), rund=22, schatten=6, rand=4),
    pl("Laden: Gewahrsam Supermarkt", LX0 + LW / 2, LY0 + 20, "enkl", fill=BLAU, size=28, anker="m"),
    *fig("MO", EMX, 940, 600, [("enkl", "ruhig"), ("tasche2", "listig"), ("vollendet", "erschrickt")], erst="cut"),
    name("MO", EMX - 190, "enkl", unten=900),
    lippenstift(EMX - 200, 520, 46, "klein", bis="tasche2"),
    ring(round(EMX + 0.045 * 600), round(940 - 0.555 * 600), round(0.075 * 600), round(0.06 * 600), "tasche2"),
    pl("Enklave: Monika", EMX + 30, 230, beim("enkl2", "Gewahrsamsenklave"), fill=ORANGE, size=28, anker="m"),
])

# F Beobachtung und Ergebnis ---------------------------------------------------------------------------------------------
folie([("beob", f"{PO} › b) Wegnahme › Beobachtung"), ("subj", "Grundfall › I. 2. subjektiv, II., III. › Ergebnis")], [
    *tafel("beob", "Beobachtet: trotzdem vollendet", h=840),
    z("Der Detektiv hat alles gesehen?", 110, 185, "beob", "Bold", 34),
    nein(135, 263, "heiml", gr=20), z("Diebstahl ist keine heimliche Tat", 175, 240, beim("heiml", "Diebstahl"), "ExtraBold", 34),
    zitat("BGH, Urt. v. 18.2.2010 – 3 StR 556/09, Rn. 12", 175, 290, beim("heiml", "heimliche")),
    z("Beobachtung: nur die Chance, die Sache", 110, 350, "chance", size=33),
    z("zurückzuholen", 110, 395, beim("chance", "zurückzuholen"), size=33),
    z("kein gesicherter Gewahrsam nötig", 110, 450, "gesich", "Bold", 33),
    ok(135, 538, beim("subj", "Vorsatz"), gr=22), z("Vorsatz, Zueignungsabsicht: will behalten", 175, 515, beim("subj", "Vorsatz"), size=33),
    ok(135, 608, "erg", gr=22), z("Rechtswidrigkeit und Schuld", 175, 585, "erg", size=33),
    blk(110, 680, 1040, 80, GRUEN, "erg2", [("Monika: vollendeter Diebstahl, § 242 Abs. 1", "ExtraBold", 34, INK)]),
    *paar("beob", [("beob", "listig"), ("heiml", "erschrickt"), ("subj", "denkt"), ("erg2", "muede")],
          [("beob", "beobachtet"), ("chance", "ruhig")]),
    ficon("fluent-emoji-high-contrast", "mirror", 1580, 250, 100, "beob", fuell=BLAU),
    ficon("tabler", "eye", 1720, 220, 70, "beob", fuell=WEISS),
    tasche_ring(MX, BR, FR, beim("subj", "Lippenstift")),
    pl("Lippenstift zurückholen", 1580, 300, "chance", fill=WEISS, size=28, anker="m", bis="subj"),
])

# G Variante 1: zurück ins Regal ------------------------------------------------------------------------------------------
RG1 = (1300, 520, 300, 380)
folie([("v1", "Variante 1 › zurück ins Regal"), ("v1b", "Variante 1 › Rücktritt, § 24 StGB?")], [
    *tafel("v1", "Variante 1: zurück ins Regal", h=720),
    z("legt den Lippenstift von sich aus zurück", 110, 185, "v1", "Bold", 34),
    z("Rücktritt nach § 24 StGB?", 110, 260, "v1b", size=34),
    z("§ 24 Abs. 1: befreit nur von der Strafe", 110, 330, "v1c", size=34),
    z("„wegen Versuchs“", 150, 377, beim("v1c", "Versuchs"), "Bold", 34),
    nein(135, 463, "v1d", gr=20), z("Tat schon vollendet: kein Rücktritt", 175, 440, "v1d", "ExtraBold", 34),
    z("Zurücklegen: nur noch bei der Strafe, § 46 Abs. 2", 110, 530, "v1e", size=33),
    z("(Verhalten nach der Tat)", 110, 575, beim("v1e", "Strafe"), size=30, farbe=TEXT),
    hart(karte(*RG1, "v1", fill=WEISS, rund=14, schatten=6, rand=5, anim="cut")),
    hart(linienzug([(RG1[0] + 8, 680), (RG1[0] + RG1[2] - 8, 680)], "v1", breite=5, farbe=INK)),
    *[hart(lippenstift(x, 672, 34, "v1", anim="cut")) for x in (1350, 1410, 1470)],
    lippenstift(1530, 672, 34, beim("v1", "zurück")),
    ficon("tabler", "arrow-back-up", 1450, 505, 64, beim("v1", "zurück"), fuell=None),
    *fig("MO", 1740, BR, FR, [("v1", "reuig"), ("v1d", "erschrickt"), ("v1e", "denkt")], erst="cut"),
    name("MO", 1740, "v1"),
    pl("schlechtes Gewissen", 1650, 400, beim("v1", "schlechtes"), fill=WEISS, size=28, anker="m", bis="v1d"),
    pl("zu spät: vollendet", 1650, 400, "v1d", fill=PINK, size=28, anker="m"),
])

# H Variante 2: schwere Kiste offen im Einkaufswagen --------------------------------------------------------------------
WX = 1545                                   # Einkaufswagen
folie([("v2", "Variante 2 › Kiste im Einkaufswagen"), ("v2f", "Variante 2 › versuchter Diebstahl, §§ 242 Abs. 2, 22 StGB"),
       ("v2g", "Variante 2 › Rücktritt, § 24 StGB")], [
    *tafel("v2", "Variante 2: Kiste im Einkaufswagen", size=44, h=840),
    z("schwere Kiste Wein offen im Einkaufswagen", 110, 180, "v2", "Bold", 33),
    z("Rainer spricht sie vor der Kasse an", 110, 225, "v2b", size=33),
    z("umfangreiche, schwere Sachen:", 110, 290, "v2c", size=33),
    z("entscheidender Unterschied", 110, 335, beim("v2c", "entscheidenden"), "Bold", 33),
    zitat("BGH 5 StR 593/18, Rn. 4", 110, 383, beim("v2c", "Unterschied")),
    z("Abtransport schwierig, offen im Wagen des Ladens", 110, 435, "v2d", size=33),
    nein(135, 513, "v2e", gr=20), z("keine Gewahrsamsenklave", 175, 490, "v2e", "Bold", 34),
    zitat("BGH, Beschl. v. 18.6.2013 – 2 StR 145/13, Rn. 3", 175, 540, beim("v2e", "Gewahrsamsenklave")),
    blk(110, 600, 1040, 80, LILA, "v2f", [("Gewahrsam noch beim Supermarkt: Versuch", "ExtraBold", 34, INK)]),
    z("freiwillig zurückgestellt: straflos, § 24 Abs. 1", 110, 715, beim("v2g", "Hätte"), "Bold", 33),
    *fig("RA", 1335, BR, FR, [("v2b", "ruhig_r"), ("v2d", "beobachtet_r")], erst="pop"),
    name("RA", 1335, "v2b"),
    *fig("MO", 1770, BR, FR, [("v2", "listig"), ("v2b", "erschrickt"), ("v2f", "denkt"), ("v2g", "reuig")], erst="cut"),
    name("MO", 1770, "v2"),
    ficon("tabler", "shopping-cart", WX, BR, 230, "v2", fuell=WEISS),
    *[szene(e, "055kiste*", 0.8, 0.05) if i == 2 else e for i, e in enumerate(kiste(WX + 20, BR - 120, 110, beim("v2", "Kiste")))],
    pl("schwer", WX + 10, 440, beim("v2c", "schweren"), fill=WEISS, size=28, anker="m", bis="v2d"),
    pl("Wagen des Ladens", WX + 10, 440, "v2d", fill=BLAU, size=28, anker="m", bis="v2f"),
    pl("noch Gewahrsam des Ladens", 1560, 120, "v2f", fill=LILA, size=28, anker="m"),
])

# I Variante 3: versteckt unter der Zeitung -----------------------------------------------------------------------------
folie([("v3", "Variante 3 › Versteck im Einkaufswagen"), ("v3c", "Variante 3 › Betrug? Diebstahl?")], [
    *tafel("v3", "Variante 3: unter der Zeitung", h=840),
    z("Lippenstift im Wagen unter einer Zeitung", 110, 180, "v3", "Bold", 33),
    z("an der Kasse nur die übrigen Waren aufs Band", 110, 225, "v3b", size=33),
    nein(135, 313, "v3c", gr=20), z("Betrug? Nein.", 175, 290, "v3c", "ExtraBold", 34),
    z("Kassiererin verfügt nur über die Waren,", 110, 360, "v3d", size=33),
    z("die sie sieht und abrechnet", 110, 405, beim("v3d", "sieht"), size=33),
    zitat("BGH, Beschl. v. 26.7.1995 – 4 StR 234/95, Rn. 12 (BGHSt 41, 198)", 110, 455, beim("v3d", "abrechnet")),
    blk(110, 520, 1040, 80, GELB, "v3e", [("Es bleibt Diebstahl, kein Betrug", "ExtraBold", 34, INK)]),
    z("vollendet oder versucht?", 110, 630, "v3f", "Bold", 33),
    z("Umstände des Einzelfalls", 110, 675, beim("v3f", "Umständen"), size=33),
    zitat("BGH 4 StR 234/95, Rn. 18", 110, 722, beim("v3f", "Einzelfalls")),
    hart(karte(1465, 700, 185, 230, "v3", fill=WEISS, rund=12, schatten=6, rand=5, anim="cut")),
    pl("Kasse", 1557, 790, "v3", fill=GELB, size=28, anker="m", anim="cut"),
    ficon("tabler", "bottle", 1505, 700, 44, "v3b", fuell=GRUEN),
    ficon("tabler", "barcode", 1600, 700, 54, "v3b", fuell=WEISS),
    pl("aufs Band: übrige Waren", 1450, 590, "v3b", fill=WEISS, size=28, anker="m", bis="v3d"),
    pl("sieht nur das Band", 1450, 590, "v3d", fill=PINK, size=28, anker="m"),
    ficon("tabler", "shopping-cart", 1335, BR, 200, "v3", fuell=WEISS),
    lippenstift(1345, BR - 108, 36, "v3", bis=beim("v3", "Zeitung")),
    ficon("ph", "newspaper", 1345, BR - 100, 96, beim("v3", "Zeitung"), fuell=WEISS),
    *fig("MO", 1760, BR, FR, [("v3", "listig"), ("v3c", "ruhig"), ("v3e", "erschrickt"), ("v3f", "denkt")], erst="cut"),
    name("MO", 1760, "v3"),
])

# J Folgen: Rücktritt und Ausblick § 252 ---------------------------------------------------------------------------------
folie([("folgen", "Folgen › Rücktritt, § 24 StGB"), ("p252", "Ausblick › räuberischer Diebstahl, § 252 StGB")], [
    *tafel("folgen", "Warum die Grenze zählt", h=760),
    z("1. Rücktritt, § 24: nur bis zur Vollendung", 110, 185, "f1", "Bold", 34),
    z("2. Ausblick: räuberischer Diebstahl, § 252", 110, 270, "p252", "Bold", 34),
    z("setzt einen vollendeten Diebstahl voraus", 150, 320, "p252b", size=33),
    zitat("BGH 4 StR 234/95, Rn. 15", 150, 368, beim("p252b", "voraus")),
    ok(175, 453, beim("p252b", "Würde"), gr=22),
    z("Gewalt nach dem Einstecken: § 252 in Betracht", 215, 430, beim("p252b", "Würde"), size=33),
    nein(175, 523, "p252c", gr=20),
    z("bloßer Versuch (Kiste): § 252 scheidet aus", 215, 500, "p252c", size=33),
    # rechts: vollendet (Jackentasche) gegen Versuch (Kiste im Wagen)
    *fig("MO", 1420, BR, FR, [("folgen", "denkt"), ("p252", "ruhig")], erst="cut"), name("MO", 1420, "folgen"),
    tasche_ring(1420, BR, FR, "f1"),
    pl("vollendet", 1420, 400, "f1", fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "shopping-cart", 1730, BR, 200, "f1", fuell=WEISS),
    *kiste(1740, BR - 104, 96, "f1"),
    pl("Versuch", 1730, 560, "f1", fill=LILA, size=28, anker="m"),
])

# K Strafantrag und Festnahme -------------------------------------------------------------------------------------------
T127 = ("„Wird jemand auf frischer Tat betroffen oder verfolgt, so ist, wenn er der Flucht verdächtig ist oder seine "
        "Identität nicht sofort festgestellt werden kann, jedermann befugt, ihn auch ohne richterliche Anordnung "
        "vorläufig festzunehmen.“")
wl127, y127 = wortlaut(90, 455, 1090, T127, "§ 127 Abs. 1 Satz 1 StPO", "p127", size=30,
                       marken=[("frischer Tat betroffen", beim("p127", "frischer")),
                               ("Flucht verdächtig", beim("p127b", "fluchtverdächtig")),
                               ("nicht sofort festgestellt", beim("p127b", "nicht"))])
folie([("p248a", "Grundfall › Strafantrag, § 248a StGB"), ("p127", "Ausblick › vorläufige Festnahme, § 127 StPO")], [
    *tafel("p248a", "Strafantrag und Festnahme", h=y127 + 40 - 60),
    z("Lippenstift für 9 €: geringwertig", 110, 180, "p248a", "Bold", 34),
    z("§ 248a: nur auf Antrag verfolgt", 110, 227, beim("p248a", "Paragraf"), size=34),
    zitat("BGH, Beschl. v. 9.7.2004 – 2 StR 176/04, Rn. 3", 110, 275, beim("p248a", "verfolgt")),
    z("außer: besonderes öffentliches Interesse", 110, 335, "oeff", size=34),
    *wl127,
    *paar("p248a", [("p248a", "ruhig"), ("p127", "erschrickt"), ("p127b", "denkt")],
          [("p248a", "ruhig"), ("p127", "beobachtet")]),
    lippenstift(1580, 330, 50, "p248a"),
    pl("9 €", 1580, PY - 60, "p248a", fill=GELB, size=28, anker="m"),
    pl("auf frischer Tat", 1580, 200, beim("p127", "frischer"), fill=PINK, size=28, anker="m"),
])

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Vollendung an der Wegnahme prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, beim("tipp", "Schreibe"), gr=26),
    z("Nie: „beobachtet, also nur Versuch“", 200, 200, beim("tipp", "Schreibe"), "Bold", 34),
    z("Vollendung an der Wegnahme prüfen:", 110, 290, "tipp2", size=34),
    z("Wie groß ist die Sache, wo steckt sie?", 110, 337, beim("tipp2", "Wie"), "Bold", 34),
    blk(110, 410, 1040, 80, GELB, "tipp3", [("Kleines in Kleidung oder Tasche: Enklave", "ExtraBold", 34, INK)]),
    blk(110, 515, 1040, 80, LILA, "tipp4", [("Großes offen im Einkaufswagen: noch keine Enklave", "ExtraBold", 31, INK)]),
    z("dann Versuch und Rücktritt prüfen", 110, 625, beim("tipp4", "Dann"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m"),
    lippenstift(1790, 360, 90, "tipp3"),
])

# M Klausurschema ------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 250
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Diebstahl, § 242 StGB", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 180, "s_i", "ExtraBold", 38, rechts=1820),
    z("1. objektiv: fremde bewegliche Sache", K2, 236, "s1a", "Bold", 34, rechts=1820),
    z("Wegnahme: Bruch fremden und Begründung neuen Gewahrsams", K3, 286, "s1b", size=34, rechts=1820),
    z("kleine Sachen in Kleidung oder Tasche: Gewahrsamsenklave,", K3 + 40, 334, "s1c", size=34, rechts=1820),
    z("Beobachtung unerheblich", K3 + 40, 382, beim("s1c", "Beobachtung"), size=34, rechts=1820),
    z("2. subjektiv: Vorsatz, Absicht rechtswidriger Zueignung", K2, 442, "s1d", "Bold", 34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 510, "s_ii", "ExtraBold", 38, rechts=1820),
    z("III. Schuld", K1, 575, "s_iii", "ExtraBold", 38, rechts=1820),
    z("IV. Strafantrag bei geringwertigen Sachen, § 248a", K1, 640, "s_iv", "ExtraBold", 38, rechts=1820),
    blk(K1, 720, 1660, 120, LILA, "s_v", [("Fehlt die Vollendung: Versuch, § 242 Abs. 2", "ExtraBold", 36, INK),
                                         ("mit Rücktritt nach § 24", "Bold", 34, INK)]),
])

# N Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 140, "merke", 80, anker="m"),
    *markertext([[("Kleine Sache", "a"), (" in Kleidung oder Tasche:", 0)], [("in der Regel schon weggenommen,", 0)],
                 [("mitten im Laden, vor dem Detektiv.", 0)]], 750, 250, 38, "merke", {"a": beim("merke", "kleine")}),
    *markertext([[("Große Ware", "b"), (" offen im Wagen:", 0)], [("keine solche Enklave.", 0)]],
                750, 480, 38, "m_2", {"b": beim("m_2", "Große")}),
    *markertext([[("Rücktritt", "c"), (" nur, solange die Tat", 0)], [("nicht vollendet ist.", 0)]], 750, 660, 38, "m_3",
                {"c": beim("m_3", "zurücktreten")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m"),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
