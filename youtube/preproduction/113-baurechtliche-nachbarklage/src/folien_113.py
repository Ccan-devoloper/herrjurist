"""Folge 113 · Baurechtliche Nachbarklage: Welche Vorschriften schützen dich? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Wohngebiet in Nordrhein-Westfalen, Baugenehmigung für den Anbau von Herrn Pütz, Klage der Nachbarin Frau Mahnke),
Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Wohnstraße mit zwei Häusern (Bebauungsplan, Anbau, Genehmigung, drei Rügen),
B Sachverhalt, C 1. Zulässigkeit kurz, D 2. Begründetheit mit Wortlautkarte § 113 I 1 VwGO, E 3. Ampel-Tabelle
drittschützender Normen, F 4. Rügen 1 und 2 (Geschossflächenzahl, Flachdach), G Rüge 3 mit Wortlautkarte § 6 BauO NRW,
H zurück an der Grenze (Abstandsfläche, Rechtsverletzung, Ergebnis, Eilrechtsschutz), I Klausurtipp (Lexi), J Schema,
K Merksatz (Lexi). Geräusch nur bei sichtbarer Handlung (Papier, wenn die Baugenehmigung erscheint)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_113/"
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


def zh(text, x, y, cue, hcue, stil="Regular", size=34, **k):
    """Tafelzeile mit Bleistift-Haken direkt hinter dem Zeilenende (zur gesprochenen Bejahung)."""
    e = z(text, x, y, cue, stil, size, **k)
    return [e, ok(e.x + e.sprite.width + 30, y + size * 0.70, hcue, gr=24)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_113/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 088/085): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------------
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


def strichlinie(x, y0, y1, cue, bis=None, breite=5, strich=22, luecke=14, anim="fade"):
    """Senkrechte gestrichelte Linie (Grundstücksgrenze)."""
    im = Image.new("RGBA", (breite + 2, int(y1 - y0) + 2))
    dr = ImageDraw.Draw(im); y = 0
    while y < y1 - y0:
        dr.line([(1 + breite / 2, y), (1 + breite / 2, min(y + strich, y1 - y0))], fill=INK, width=breite); y += strich + luecke
    return El(im, x - breite / 2, y0, cue, anim, 0.0, bis, name="grenze")


def masspfeil(x0, x1, y, cue, bis=None, anim="fade"):
    """Waagerechte Maßlinie mit Endstrichen (Abstand des Anbaus zur Grenze)."""
    s = 3; w, h = int(x1 - x0) + 8, 40
    im = Image.new("RGBA", (w * s, h * s)); dr = ImageDraw.Draw(im)
    dr.line([(4 * s, h / 2 * s), ((w - 4) * s, h / 2 * s)], fill=INK, width=5 * s)
    for xx in (4, w - 4):
        dr.line([(xx * s, 6 * s), (xx * s, (h - 6) * s)], fill=INK, width=5 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x0 - 4, y - h / 2, cue, anim, 0.0, bis, name="masslinie")


def flaeche(x0, x1, y0, y1, farbe, cue, bis=None, d=0.0, anim="fade", name="abstandsflaeche"):
    """Abstandsfläche als halbtransparenter Streifen vor der Wand (Tafelgrafik, kein Requisit)."""
    im = Image.new("RGBA", (int(x1 - x0), int(y1 - y0)))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 6, fill=farbe[:3] + (150,), outline=INK, width=3)
    return El(im, x0, y0, cue, anim, d, bis, name=name)


FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
MA_F, PU_F = ROT, GRUEN                     # Farben der Namensschilder (wie Pullover bzw. Hemd)
MA_S, PU_S = "Frau Mahnke", "Herr Pütz, Bauherr"

# Wohnstraße (Szene A und H): Haus Mahnke links, Grenze, Anbau und Haus Pütz rechts ---------------------------------------------
BODEN, GH = 860, 380
HMX, GRX, ANX, HPX = 230, 815, 1085, 1390   # Haus Mahnke, Grenze, Anbau (Mitte), Haus Pütz
AN_W = 280                                  # Breite des Anbaus (Tabler „wall“, flach gedeckt)
AN_L = ANX - AN_W / 2                        # linke Wand des Anbaus (zur Grenze), 130 px = 1,50 m
M15 = AN_L - GRX                             # 1,50 m in Pixeln
MAX, PUX = 470, 1745                         # Frau Mahnke, Herr Pütz


def strasse(cue, anim="pop", mit_anbau=True, anbau_cue=None, bis=None):
    els = [hart(linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)) if anim == "cut"
           else linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           ficon("ph", "house-line", HMX, BODEN + 4, 330, cue, fuell=GELB, anim=anim, bis=bis),
           strichlinie(GRX, 600, BODEN + 40, cue, bis=bis, anim="cut" if anim == "cut" else "fade"),
           ficon("ph", "house-line", HPX, BODEN + 4, 330, cue, fuell=BLAU, anim=anim, bis=bis)]
    if mit_anbau:
        els.append(ficon("tabler", "wall", ANX, BODEN, AN_W, anbau_cue or cue, fuell=ROT,
                         anim="pop" if anbau_cue else anim, bis=bis))
    return els


# A Fall: Wohnstraße, Bebauungsplan, Anbau, Baugenehmigung, drei Rügen -----------------------------------------------------------
MAa = ("MA_protest_r", MAX, BODEN, GH)
PUa = ("PU_redet", PUX, BODEN, GH)
folie([(NULL, "Fall · Der Anbau nebenan"), ("genehm", "Fall · Die Baugenehmigung"),
       ("frage", "Fall · Drei Verstöße – welcher hilft ihr?")], [
    *strasse(NULL, anim="cut", anbau_cue="anbau"),
    *fig("MA", MAX, BODEN, GH, [(NULL, "ruhig_r"), ("anbau", "sorge_r")], bis="ma1", erst="cut"),
    *redet("MA_protest_r", MAX, BODEN, GH, "ma1", "frage"),
    *fig("MA", MAX, BODEN, GH, [("frage", "denkt_r")]),
    hart(schild(MA_S, MAX, NULL, MA_F, unten=BODEN, d=0.0)),
    pl("Wohngebiet in Nordrhein-Westfalen", 70, 40, beim("fall", "Wohngebiet"), fill=WEISS, size=30, bis="ma1"),
    pl("Bebauungsplan: Geschossflächenzahl 0,4", 70, 110, beim("plan", "Geschossflächenzahl"), fill=GELB, size=30, bis="ma1"),
    pl("Gestaltungssatzung: Satteldächer", 70, 180, beim("plan", "Gestaltungssatzung"), fill=GELB, size=30, bis="ma1"),
    pl("Grenze", GRX, 548, beim("pu1", "Grenze"), fill=WEISS, size=26, anker="m"),
    *fig("PU", PUX, BODEN, GH, [(beim("puetz", "Herr"), "ruhig")], bis="pu1"),
    *redet("PU_redet", PUX, BODEN, GH, "pu1", "genehm"),
    *fig("PU", PUX, BODEN, GH, [("genehm", "ruhig"), ("ma1", "ernst"), ("frage", "denkt")]),
    schild(PU_S, PUX, beim("puetz", "Herr"), PU_F, unten=BODEN, d=0.0),
    blase("denk", 300, 230, beim("puetz", "vergrößern"), 1450, 300, figur=("PU_ruhig", PUX, BODEN, GH), bis="pu1"),
    ficon("tabler", "home-plus", 1450, 365, 110, beim("puetz", "vergrößern"), fuell=BLAU, d=0.2, bis="pu1"),
    blase("sprech", 900, 200, "pu1", 1300, 260, inhalt=["Ich baue an: 2 Geschosse mit Flachdach,",
                                                     "bis kurz vor die Grenze."], textsize=29, figur=PUa, bis="genehm"),
    szene(ficon("tabler", "file-certificate", 1640, 330, 90, beim("genehm", "Baugenehmigung"), fuell=WEISS, bis="ma1"),
          "113papier*", 0.8, -0.24),
    pl("Baugenehmigung erteilt", 1640, 345, beim("genehm", "Baugenehmigung"), fill=GRUEN, size=28, anker="m", bis="ma1"),
    pl("Wand 6 m hoch", ANX, 510, beim("anbau", "sechs"), fill=ROT, size=28, anker="m", bis="frage"),
    masspfeil(GRX, AN_L, BODEN - 40, beim("anbau", "eineinhalb")),
    pl("1,50 m", (GRX + AN_L) / 2, BODEN - 118, beim("anbau", "eineinhalb"), fill=WEISS, size=26, anker="m", pad=(10, 8), bis="ma1"),
    pl("Geschossflächenzahl jetzt 0,55", HPX, 440, beim("gfz", "Geschossflächenzahl"), fill=GELB, size=28, anker="m",
       bis="ma1"),
    blase("sprech", 900, 200, "ma1", 640, 220, inhalt=["Viel zu groß, ein Flachdach, und dann noch",
                                                     "direkt an meiner Grenze! Dagegen klage ich."], textsize=29,
          figur=MAa, bis="frage"),
    pl("1 Geschossflächenzahl", HPX, 440, beim("frage", "Drei"), fill=GELB, size=28, anker="m"),
    pl("2 Flachdach", ANX, 510, beim("frage", "Drei"), fill=ROT, size=28, anker="m"),
    pl("3 Abstand zur Grenze", GRX + 30, 430, beim("frage", "Drei"), fill=WEISS, size=28, anker="m"),
    pl("3 Verstöße: Mit welchem gewinnt sie ihre Klage?", 960, 110, "frage2", fill=PINK, size=36, anker="m"),
])

# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Mahnke und Herr Pütz wohnen nebeneinander in Einfamilienhäusern in einem allgemeinen Wohngebiet in "
    "Nordrhein-Westfalen. Der Bebauungsplan setzt eine Geschossflächenzahl von 0,4 fest; eine Gestaltungssatzung der Stadt "
    "schreibt Satteldächer vor.",
    "Die Bauaufsichtsbehörde erteilt Herrn Pütz die Baugenehmigung für einen zweigeschossigen Anbau mit Flachdach. Die "
    "Wand zum Grundstück von Frau Mahnke wird 6 m hoch und steht 1,50 m vor der Grenze. Die Geschossflächenzahl steigt auf "
    "0,55. Eine Befreiung oder Abweichung hat Herr Pütz weder beantragt noch erhalten. Frau Mahnke erhebt Klage beim "
    "Verwaltungsgericht.",
], "Mit welchem Verstoß gewinnt Frau Mahnke ihre Klage?")

# C 1. Zulässigkeit kurz --------------------------------------------------------------------------------------------------------
ZU = "1. Zulässigkeit"
folie([("zul", f"{ZU} › Anfechtungsklage"), ("kb", f"{ZU} › Klagebefugnis, § 42 II VwGO")], rechts_frei([
    *tafel("zul", "1. Zulässigkeit, kurz"),
    z("Anfechtungsklage gegen die Genehmigung", 110, 175, beim("zul", "Anfechtungsklage"), "Bold", 36),
    z("des Nachbarn", 150, 225, beim("zul", "Nachbarn"), size=34),
    z("in Nordrhein-Westfalen ohne Widerspruchsverfahren", 110, 300, beim("zul", "Nordrhein"), size=32),
    zit("§ 110 Abs. 1 Satz 1, Abs. 3 Satz 2 Nr. 8 JustG NRW", 150, 348, beim("zul", "Widerspruchsverfahren")),
    z("Klagebefugnis, § 42 Abs. 2 VwGO:", 110, 425, "kb", "Bold", 36),
    z("Verletzung einer Norm geltend gemacht,", 150, 477, beim("kb", "Verletzung"), size=34),
    z("die auch sie schützt", 150, 525, beim("kb", "auch"), size=34),
    *zh("hier: die Abstandsflächen", 150, 595, beim("kb", "Abstandsflächen"), beim("kb", "Abstandsflächen"), "Bold", 34),
    blk(110, 680, 1040, 80, GELB, "v110", [("Videos: Klagebefugnis und Schutznormtheorie", "ExtraBold", 34, INK)]),
    ficon("tabler", "file-certificate", IX, IU, 110, "zul", fuell=WEISS),
    pl("Genehmigung des Nachbarn", IX, 190, beim("zul", "Genehmigung"), fill=GRUEN, size=28, anker="m"),
    *fig("MA", FX, FB, FR, [("zul", "ruhig"), ("kb", "denkt")]),
    schild(MA_S, FX, "zul", MA_F),
]))

# D 2. Begründetheit: Wortlautkarte § 113 I 1 VwGO ---------------------------------------------------------------------------------
W113 = ("„Soweit der Verwaltungsakt rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht "
        "den Verwaltungsakt … auf.“")
Z113 = ["„Soweit der Verwaltungsakt rechtswidrig und der Kläger",
        "dadurch in seinen Rechten verletzt ist, hebt das Gericht den",
        "Verwaltungsakt … auf.“"]
w113, w113_y = wortlaut(80, 160, 1100, W113, "§ 113 Abs. 1 Satz 1 VwGO", "p113", size=34, zeilen=Z113,
                        marken=[("rechtswidrig", beim("p113", "rechtswidrig")),
                                ("dadurch in seinen Rechten verletzt", beim("p113", "dadurch"))])
BG = "2. Begründetheit"
folie([("p113", f"{BG}, § 113 I 1 VwGO"), ("zwei", f"{BG} › rechtswidrig und dadurch verletzt"),
       ("faden", f"{BG} › objektiv rechtswidrig ist nicht gleich verletzt")], rechts_frei([
    titel(glyphen("2. Begründetheit"), 110, 75, "p113", 46),
    *w113,
    z("1. Die Genehmigung ist rechtswidrig,", 110, w113_y + 30, beim("zwei", "Genehmigung"), "Bold", 34),
    z("2. und sie verletzt gerade die Klägerin.", 110, w113_y + 82, beim("zwei", "verletzt"), "Bold", 34),
    blk(110, w113_y + 160, 1040, 126, ROT, "faden", [("Objektive Rechtswidrigkeit ist", "ExtraBold", 36, INK),
                                                    ("nicht gleich Rechtsverletzung!", "ExtraBold", 36, INK)]),
    z("Nur wenn die verletzte Norm auch den Nachbarn schützt", 110, w113_y + 305, beim("faden", "Verstoß"), size=32),
    zit("OVG NRW, Urt. v. 6.11.2024 – 7 A 75/23, Rn. 32", 150, w113_y + 352, beim("faden", "Verstoß")),
    ficon("tabler", "scale", IX, IU, 140, "p113", fuell=WEISS),
    *fig("MA", FX, FB, FR, [("p113", "denkt"), ("faden", "ernst")]),
    schild(MA_S, FX, "p113", MA_F),
]))

# E 3. Ampel-Tabelle: Welche Bauvorschriften schützen dich? -----------------------------------------------------------------------
DS = "3. Drittschützende Normen"
AY = [170, 305, 440, 575, 710]                # Zeilenanfänge
AMP = 805                                      # linker Rand der Ampel-Pillen


def ampel(i, cue, norm, text, fill, haken, sub, sub_cue, quelle, q_cue):
    y = AY[i]
    els = [z(norm, 110, y, cue, "Bold", 32, rechts=AMP - 20),
           pl(text, AMP, y - 8, beim(cue, haken[0]), fill=fill, size=28)]
    p = els[-1]
    els.append((ok if haken[1] else nein)(p.x + p.sprite.width + 30, y + 16, beim(cue, haken[0]), gr=22))
    els.append(z(sub, 150, y + 46, sub_cue, size=30, rechts=AMP - 20))
    if quelle:
        els.append(zit(quelle, 150, y + 88, q_cue, rechts=AMP + 330))
    return els


folie([("tab", DS), ("t1", f"{DS} › Abstandsflächen"), ("t2", f"{DS} › Gebietserhaltungsanspruch"),
       ("t3", f"{DS} › Rücksichtnahmegebot"), ("t4", f"{DS} › Maß der baulichen Nutzung: nein"),
       ("t5", f"{DS} › Gestaltungsvorschriften: nein")], rechts_frei([
    *tafel("tab", "Welche Bauvorschriften schützen dich?", size=44),
    *ampel(0, "t1", "1. Abstandsflächen (Landesbauordnung)", "schützt mich", GRUEN, ("Abstandsflächen", 1),
           "Licht, Luft und Sozialabstand", beim("t1", "Licht"),
           "OVG NRW, Urt. v. 22.1.2025 – 7 A 1367/22, Rn. 53, 80", beim("t1", "Nachbarn")),
    *ampel(1, "t2", "2. Art der Nutzung: Gebietserhaltung", "schützt mich", GRUEN, ("Gebietserhaltungsanspruch", 1),
           "auch ohne konkrete Beeinträchtigung", beim("t2", "konkrete"),
           "BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8", beim("t2", "konkrete")),
    *ampel(2, "t3", "3. Rücksichtnahmegebot", "vor Unzumutbarem", GELB, ("Unzumutbarem", 1),
           "§ 15 I 2 BauNVO, §§ 34 I, 35 III BauGB", beim("t3", "fünfzehn"),
           None, None),
    pl("eigenes Video", AMP, AY[2] + 50, beim("t3", "eigenes"), fill=GELB, size=26),
    *ampel(3, "t4", "4. Maß der baulichen Nutzung", "schützt mich nicht", ROT, ("schützt", 0),
           "nur, wenn die Gemeinde das will", beim("t4", "nur"),
           "BVerwG, 4 C 7.17, Rn. 14, 21; OVG NRW, 10 B 645/23, Rn. 48", beim("t4", "Plangeber")),
    *ampel(4, "t5", "5. Gestaltungsvorschriften", "schützt mich nicht", ROT, ("schützen", 0),
           "sie dienen dem Ortsbild", beim("t5", "Ortsbild"),
           "OVG NRW, Urt. v. 6.11.2024 – 7 A 75/23, Rn. 41", beim("t5", "Ortsbild")),
    ficon("tabler", "traffic-lights", IX, IU, 120, "tab", fuell=GELB),
    *fig("MA", FX, FB, FR, [("tab", "denkt"), ("t1", "froh"), ("t4", "sorge")]),
    schild(MA_S, FX, "tab", MA_F),
]))

# F 4. Die Rügen am Fall: Geschossflächenzahl, Flachdach ---------------------------------------------------------------------------
RG = "4. Die Rügen am Fall"
folie([("r1", f"{RG} › 1. Geschossflächenzahl"), ("r2", f"{RG} › 2. Flachdach")], rechts_frei([
    *tafel("r1", "Die Rügen von Frau Mahnke"),
    z("1. Geschossflächenzahl 0,55 statt 0,4", 110, 170, "r1", "Bold", 34),
    *zh("objektiv rechtswidrig, § 30 Abs. 1 BauGB", 150, 222, beim("r1a", "widerspricht"), beim("r1a", "objektiv"), size=32),
    *zk("kein Schutzwille der Gemeinde: keine Rechtsverletzung", 150, 272, beim("r1b", "Schutzwillen"),
        beim("r1b", "nicht", nr=2), size=30),
    z("Befreiung, § 31 Abs. 2: nur Würdigung nachbarlicher", 150, 330, "befr", size=30),
    z("Interessen rügbar", 190, 372, beim("befr", "nachbarlichen"), size=30),
    zit("BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 12", 190, 414, beim("befr", "nachbarlichen")),
    z("2. Flachdach statt Satteldach", 110, 500, "r2", "Bold", 34),
    *zh("verstößt gegen die Gestaltungssatzung", 150, 552, beim("r2", "verstößt"), beim("r2", "Gestaltungssatzung"),
        size=32),
    *zk("schützt das Ortsbild, nicht Frau Mahnke", 150, 602, "r2a", beim("r2a", "nicht"), size=32),
    blk(110, 690, 1040, 80, GELB, beim("r2a", "nicht"), [("2 Verstöße, aber keine Rechtsverletzung", "ExtraBold", 34, INK)]),
    ficon("tabler", "home-plus", IX - 110, IU, 110, "r1", fuell=BLAU),
    ficon("tabler", "wall", IX + 100, IU, 130, "r2", fuell=ROT),
    pl("Bebauungsplan", IX - 110, 210, beim("r1a", "Bebauungsplan"), fill=GELB, size=26, anker="m"),
    pl("Flachdach", IX + 100, 210, "r2", fill=ROT, size=26, anker="m"),
    *fig("MA", FX, FB, FR, [("r1", "denkt"), ("r1b", "sorge"), ("r2", "denkt"), ("r2a", "sorge")]),
    schild(MA_S, FX, "r1", MA_F),
]))

# G Rüge 3: Abstandsfläche, Wortlautkarte § 6 BauO NRW 2018 (Auszug) ---------------------------------------------------------------
W6 = ("„(2) Abstandsflächen müssen auf dem Grundstück selbst liegen. … (4) Die Tiefe der Abstandsfläche bemisst sich nach "
      "der Wandhöhe; … Das sich ergebende Maß ist H. (5) Die Tiefe der Abstandsflächen beträgt 0,4 H, mindestens 3 m. …“")
Z6 = ["„(2) Abstandsflächen müssen auf dem Grundstück selbst liegen. …",
      "(4) Die Tiefe der Abstandsfläche bemisst sich nach der Wandhöhe;",
      "… Das sich ergebende Maß ist H.",
      "(5) Die Tiefe der Abstandsflächen beträgt 0,4 H, mindestens 3 m. …“"]
w6, w6_y = wortlaut(80, 160, 1100, W6, "§ 6 Abs. 2 Satz 1, Abs. 4, Abs. 5 Satz 1 BauO NRW 2018", "wl6", size=31, zeilen=Z6,
                    marken=[("auf dem Grundstück selbst", beim("wl6", "Grundstück")),
                            ("nach der Wandhöhe", beim("wl6", "Wandhöhe")),
                            ("0,4 H, mindestens 3 m", beim("wl6", "mindestens"))])
folie([("r3", f"{RG} › 3. Abstandsfläche"), ("wl6", f"{RG} › 3. Abstandsfläche, § 6 BauO NRW 2018")], rechts_frei([
    titel(glyphen("3. Abstandsfläche, Beispiel Nordrhein-Westfalen"), 110, 75, "r3", 44),
    *w6,
    z("Wand des Anbaus: 6 m hoch", 110, w6_y + 30, "rech", "Bold", 34),
    z("0,4 · 6 m = 2,40 m", 150, w6_y + 82, beim("rech", "Null"), size=34),
    blk(110, w6_y + 150, 1040, 80, GELB, beim("rech", "Mindestmaß"), [("also gilt das Mindestmaß: 3 m", "ExtraBold", 36, INK)]),
    ficon("tabler", "ruler-measure", IX, IU, 140, "r3", fuell=GELB),
    pl("H = Wandhöhe", IX, 200, beim("wl6", "Wandhöhe"), fill=WEISS, size=28, anker="m"),
    *fig("MA", FX, FB, FR, [("r3", "denkt")]),
    schild(MA_S, FX, "r3", MA_F),
]))

# H Zurück an der Grenze: Abstandsfläche, Rechtsverletzung, Ergebnis, Eilrechtsschutz ------------------------------------------------
PUj = ("PU_neu", PUX, BODEN, GH)
folie([("luecke", f"{RG} › 3. Abstandsfläche: 1,50 m statt 3 m"), ("verl", f"{RG} › 3. Abstandsfläche: Rechtsverletzung"),
       ("erg", "Ergebnis · Klage begründet, nur wegen der Abstandsfläche"), ("eil", "Ergebnis · Eilrechtsschutz")], [
    *strasse("luecke"),
    *fig("MA", MAX, BODEN, GH, [("luecke", "sorge_r"), ("erg", "froh_r")]),
    schild(MA_S, MAX, "luecke", MA_F, unten=BODEN),
    *fig("PU", PUX, BODEN, GH, [("luecke", "ruhig"), ("verl", "ernst"), ("erg", "muede")], bis="pu2"),
    *redet("PU_neu", PUX, BODEN, GH, "pu2", "tipp"),
    schild(PU_S, PUX, "luecke", PU_F, unten=BODEN),
    masspfeil(GRX, AN_L, BODEN - 40, "luecke"),
    pl("1,50 m", (GRX + AN_L) / 2, BODEN - 118, beim("luecke", "eineinhalb"), fill=WEISS, size=26, anker="m", pad=(10, 8), bis="erg"),
    flaeche(GRX, AN_L, BODEN + 6, BODEN + 40, GELB, beim("luecke", "Eineinhalb")),
    flaeche(AN_L - 2 * M15, GRX, BODEN + 6, BODEN + 40, ROT, beim("luecke", "Grundstück"), name="auf_ihrem_grund"),
    pl("Abstandsfläche 3 m: 1,50 m auf ihrem Grundstück", 720, 950 - 2, beim("luecke", "Grundstück"), fill=ROT, size=28,
       anker="m", bis="erg"),
    pl("keine Abweichung zugelassen", 960, 60, "abw", fill=WEISS, size=30, anker="m", bis="erg"),
    pl("Norm schützt auch Frau Mahnke: Rechtsverletzung", 960, 130, beim("verl", "Weil"), fill=GRUEN, size=30, anker="m",
       bis="erg"),
    pl("keine konkrete Beeinträchtigung nötig", 960, 200, beim("verl", "konkrete"), fill=WEISS, size=28, anker="m", bis="erg"),
    bis_(zit("OVG NRW, Urt. v. 22.1.2025 – 7 A 1367/22, Rn. 53, 57", 640, 262, beim("verl", "konkrete"), rechts=1500), "erg"),
    pl("in deinem Land ggf. andere Regel", 960, 330, "land", fill=GELB, size=28, anker="m", bis="erg"),
    ficon(HC, "classical-building", 960, 420, 110, "erg", fuell=WEISS, bis="pu2"),
    pl("Klage begründet: nur wegen der Abstandsfläche", 960, 60, beim("erg", "Klage"), fill=GRUEN, size=30, anker="m",
       bis="pu2"),
    pl("Gericht hebt die Baugenehmigung auf", 960, 130, beim("erg", "Gericht"), fill=WEISS, size=30, anker="m", bis="pu2"),
    pl("Eilrechtsschutz: eigenes Video zur Drittanfechtung", 960, 200, "eil", fill=GELB, size=28, anker="m", bis="pu2"),
    blase("sprech", 820, 200, "pu2", 1290, 250, inhalt=["Dann plane ich den Anbau eben neu,", "mit 3 Metern Abstand."],
          textsize=30, figur=PUj),
])

# I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Drittschutz bei jedem Verstoß prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    *zk("nicht alle Fehler der Reihe nach prüfen", 200, 200, beim("tipp", "nicht"), beim("tipp", "durch"), "Bold", 34),
    z("bei jedem Verstoß sofort fragen:", 200, 300, "tipp1", "Bold", 34),
    z("Schützt die verletzte Norm auch den Kläger?", 240, 352, beim("tipp1", "Schützt"), size=34),
    z("gehört die Norm zum Prüfprogramm", 200, 450, "tipp2", "Bold", 34),
    z("der Genehmigung?", 240, 502, beim("tipp2", "Genehmigung"), size=34),
    z("Nordrhein-Westfalen: Abstandsflächen gehören dazu", 240, 580, beim("tipp2", "Nordrhein"), size=32),
    zit("§ 64 Abs. 1 Satz 1 Nr. 1 Buchst. b BauO NRW 2018", 240, 628, beim("tipp2", "Abstandsflächen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# J Schema ----------------------------------------------------------------------------------------------------------------------------
SZ, LH = 36, 74
zeilen_ = [("s1", "1. Zulässigkeit", "Bold", 0),
           ("s1a", "a) Anfechtungsklage gegen die Baugenehmigung", "Regular", 1),
           ("s1b", "b) Klagebefugnis: drittschützende Norm, die verletzt sein kann", "Regular", 1),
           ("s2", "2. Begründetheit, § 113 Abs. 1 Satz 1 VwGO", "Bold", 0),
           ("s2a", "a) Die Genehmigung ist rechtswidrig,", "Regular", 1),
           ("s2b", "b) und zwar wegen eines Verstoßes gegen eine drittschützende Norm:", "Regular", 1),
           ("s2c", "Abstandsflächen, Gebietserhaltung, Rücksichtnahme – nicht Maß, Gestaltung", "Regular", 2),
           ("s3", "3. Die Klägerin ist dadurch in ihren Rechten verletzt.", "Bold", 0)]
els_t = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Schema: Baurechtliche Nachbarklage"), 110, 85, "sch", 46)]
for i, (c, t, s, e) in enumerate(zeilen_):
    els_t.append(z(t, 140 + 60 * e, 200 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Schema · Baurechtliche Nachbarklage")], els_t)

# K Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nicht jeder Baurechtsverstoß", 0)]], 750, 340, 44, beim("merke", "Nicht"), {}),
    *markertext([[("deines Nachbarn ", 0), ("verletzt dein Recht.", "a")]], 750, 410, 44, beim("merke", "deines"),
                {"a": beim("merke", "verletzt")}),
    *markertext([[("Du gewinnst nur mit einer Norm,", 0)]], 750, 540, 44, "m2", {}),
    *markertext([[("die ", 0), ("auch dich schützt,", "b")]], 750, 610, 44, beim("m2", "die"), {"b": beim("m2", "auch")}),
    *markertext([[("etwa mit der ", 0), ("Abstandsfläche.", "c")]], 750, 700, 44, beim("m2", "etwa"),
                {"c": beim("m2", "Abstandsfläche")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
