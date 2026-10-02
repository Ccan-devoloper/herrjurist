"""Folge 081 · Zulässigkeit und Begründetheit: Aufbau im Öffentlichen Recht – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Übungsfall): Tabea teilt ihr Auto mit zwei Mitbewohnern; nach einem Geschwindigkeitsverstoß ordnet die Stadt
ein Fahrtenbuch an (§ 31a StVZO). Mitbewohner Lennart vermischt Zulässigkeit und Begründetheit. Szenen laut ../SZENENPLAN.md:
A Straße vor dem WG-Haus (Rückblende Blitzer), B Hausflur mit Briefkasten (Bescheid, Blasen), C Sachverhalt, D Obersatz,
E fehlende Zulässigkeit, F Bausteine I.–II., G Bausteine III.–V., H Klagebefugnis (Wortlaut § 42 II), I Fehler 2 (Lennart),
J Begründetheit (Wortlaut § 113 I 1), K Rechtswidrigkeit (§ 31a StVZO), L Argument von Tabea, Rechtsverletzung, Ergebnis,
M andere Verfahren (Verfassungsbeschwerde, § 80 V VwGO), N Gewichtung, O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/schild als eigene Kopie aus Folge 069 (gemeinsame Dateien
unverändert). Zwei Handlungsgeräusche (Auto fährt am Blitzer vorbei, Briefkastenklappe; ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_081/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HC = "fluent-emoji-high-contrast"
HELLROT = (250, 205, 198, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_081/" in n:
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


# --- Eigene Hilfsfunktion (Kopie aus Folge 069): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts (Kopie aus Folge 080)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, x, y, cue, stil="Regular", size=34, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 22, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, x, y, cue, stil="Regular", size=34, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 22, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN, FH = 860, 480
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
X1, X2 = 1420, 1730                         # zwei Figuren neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
TA_F, LE_F = LILA, GRUEN                    # Farben der Namensschilder
ZU = "A. Zulässigkeit"
BG = "B. Begründetheit"


def boden(cue, hart_=False):
    e = linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


# A Fall: Straße vor dem WG-Haus, Rückblende Blitzer --------------------------------------------------------------------------
HAUSX, TAX, AUTOX = 260, 640, 1010
folie([(NULL, "Fall · Das geteilte Auto"), ("blitz", "Fall · Vor 3 Monaten: geblitzt"), ("bogen", "Fall · Der Anhörungsbogen")], [
    boden(NULL, True),
    hart(pl("Die Studentin Tabea", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "building", HAUSX, BODEN - 2, 300, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "sun", 900, 200, 110, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "car", AUTOX, BODEN - 2, 360, NULL, fuell=GELB, anim="cut"),
    *fig("TA", TAX, BODEN, FH, [(NULL, "ruhig_r"), ("bogen", "denkt_r"), ("fahrer", "sorge_r")], erst="cut"),
    hart(schild("Tabea, Studentin", TAX, NULL, TA_F, unten=BODEN, d=0.0)),
    ficon("tabler", "key", AUTOX - 120, 560, 70, beim("fall", "teilt"), fuell=GELB),
    pl("Auto geteilt mit 2 Mitbewohnern", AUTOX + 60, 600, beim("fall", "Mitbewohnern"), fill=WEISS, size=30, anker="m"),
    # Rückblende-Panel oben rechts: Auto fährt am Blitzer vorbei
    karte(1180, 90, 680, 330, "blitz", fill=(246, 246, 250, 255)),
    pl("Vor 3 Monaten", 1210, 60, "blitz", fill=GELB, size=30),
    linienzug([(1210, 360), (1830, 360)], "blitz", breite=5, farbe=INK),
    linienzug([(1760, 360), (1760, 230)], "blitz", breite=6, farbe=INK),
    ficon("tabler", "camera", 1760, 240, 90, "blitz", fuell=WEISS),
    szene(bewegt(ficon("tabler", "car", 1560, 358, 170, "blitz", fuell=GELB, anim="cut"), "blitz",
                 beim("blitz", "geblitzt"), -320), "081auto*", 0.7, -0.15),
    ficon("tabler", "bolt", 1680, 200, 60, beim("blitz", "geblitzt"), fuell=GELB),
    pl("25 km/h zu schnell", 1440, 130, beim("blitz", "fünfundzwanzig"), fill=ROT, size=30, anker="m"),
    ficon(HC, "envelope", TAX + 230, 470, 90, "bogen", fuell=WEISS),
    pl("Anhörungsbogen: liegen gelassen", TAX + 230, 300, beim("bogen", "liegen"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "zoom-question", 1520, 560, 90, "fahrer", fuell=WEISS),
    pl("Fahrer: unbekannt", 1520, 600, beim("fahrer", "gefahren"), fill=ROT, size=30, anker="m"),
])

# B Hausflur: der Bescheid ------------------------------------------------------------------------------------------------------
TAX2, LEX = 760, 1440
TAb = ("TA_redet_r", TAX2, BODEN, FH)
TFb = ("TA_fragt_r", TAX2, BODEN, FH)
LEb = ("LE_redet", LEX, BODEN, FH)
BH = hand("TA_liest_r", TAX2, BODEN, FH, 1)
folie([("bescheid", "Fall · Der Bescheid"), ("frage", "Fall · Zwei Fragen vermischt")], [
    boden("bescheid"),
    pl("Heute, im Hausflur", 70, 40, "bescheid", fill=GELB, size=40),
    szene(ficon("tabler", "mailbox", 300, 620, 200, beim("bescheid", "Bescheid"), fuell=BLAU), "081briefkasten*", 0.8, -0.25),
    linienzug([(300, 615), (300, BODEN)], "bescheid", breite=8, farbe=INK),
    *fig("TA", TAX2, BODEN, FH, [("bescheid", "liest_r")], bis="ta1"),
    *redet("TA_redet_r", TAX2, BODEN, FH, "ta1", "le1"),
    *fig("TA", TAX2, BODEN, FH, [("le1", "aerger_r")], bis="ta2", erst="cut"),
    *redet("TA_fragt_r", TAX2, BODEN, FH, "ta2", "frage"),
    *fig("TA", TAX2, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    schild("Tabea", TAX2, "bescheid", TA_F, unten=BODEN, d=0.0),
    ficon("tabler", "file-text", BH[0] + 30, BH[1] + 40, 80, beim("bescheid", "Bescheid"), fuell=WEISS),
    ficon("tabler", "notebook", 1080, 720, 90, beim("ta1", "Fahrtenbuch"), fuell=GELB, bis="frage"),
    pl("Bescheid: Fahrtenbuch, ein halbes Jahr", 1080, 760, beim("ta1", "Fahrtenbuch"), fill=WEISS, size=28, anker="m", bis="frage"),
    *fig("LE", LEX, BODEN, FH, [("bescheid", "ruhig")], bis="le1"),
    *redet("LE_redet", LEX, BODEN, FH, "le1", "ta2"),
    *fig("LE", LEX, BODEN, FH, [("ta2", "ruhig"), ("frage", "denkt")], erst="cut"),
    schild("Lennart, Mitbewohner", LEX, "bescheid", LE_F, unten=BODEN, d=0.0),
    blase("sprech", 760, 200, "ta1", 640, 190, inhalt=["Ich soll ein halbes Jahr ein", "Fahrtenbuch führen? Ich bin doch",
                                                      "gar nicht gefahren!"], textsize=30, figur=TAb, bis="le1"),
    blase("sprech", 720, 170, "le1", 1300, 190, inhalt=["Dann ist der Bescheid rechtswidrig.", "Deine Klage ist also zulässig."],
          textsize=30, figur=LEb, bis="ta2"),
    blase("sprech", 560, 130, "ta2", 640, 210, inhalt=["Und hat meine Klage Erfolg?"], textsize=32, figur=TFb, bis="frage"),
    pl("Lennart vermischt 2 Fragen", 1100, 150, beim("frage", "vermischt"), fill=PINK, size=40, anker="m"),
    blk(700, 250, 380, 76, BLAU, beim("frage2", "Zulässigkeit"), [("Zulässigkeit", "ExtraBold", 36, INK)]),
    blk(1120, 250, 380, 76, GRUEN, beim("frage2", "Begründetheit"), [("Begründetheit", "ExtraBold", 36, INK)]),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Tabea teilt ihr kleines Auto mit 2 Mitbewohnern. Vor 3 Monaten wurde jemand damit geblitzt, 25 km/h zu schnell. "
    "Den Anhörungsbogen hat Tabea liegen lassen; wer gefahren ist, hat die Stadt nicht herausgefunden.",
    "Heute erhält Tabea einen Bescheid der Stadt: Sie muss für ihr Auto ein halbes Jahr lang ein Fahrtenbuch führen. "
    "Tabea: „Ich bin doch gar nicht gefahren!“ Ihr Mitbewohner Lennart meint: „Dann ist der Bescheid rechtswidrig. "
    "Deine Klage ist also zulässig.“",
], "Hat die Klage Erfolg?")

# D Obersatz: zwei Fragen -----------------------------------------------------------------------------------------------------
folie([("ober", "Obersatz · Zulässigkeit und Begründetheit")], rechts_frei([
    *tafel("ober", "Der Obersatz"),
    blk(110, 190, 1040, 90, HELL, beim("ober", "Klage"), [("„Die Klage hat Erfolg, soweit sie", "Bold", 36, INK)], rand=4),
    blk(110, 270, 1040, 90, HELL, beim("ober", "zulässig"), [("zulässig und begründet ist.“", "Bold", 36, INK)], rand=4),
    pl("Klausurkonvention, kein Gesetzestext", 110, 385, beim("konv", "Klausurkonvention"), fill=PINK, size=30),
    blk(110, 480, 1040, 76, BLAU, beim("zul", "Zulässigkeit"), [("A. Zulässigkeit", "ExtraBold", 36, INK)]),
    z("Darf das Gericht in der Sache entscheiden?", 150, 572, beim("zul", "Darf"), "Bold", 34),
    z("= Sachentscheidungsvoraussetzungen", 150, 625, beim("sev", "Sachentscheidungsvoraussetzungen"), size=34),
    blk(110, 700, 1040, 76, GRUEN, beim("begr", "Begründetheit"), [("B. Begründetheit", "ExtraBold", 36, INK)]),
    z("Hat die Klägerin in der Sache recht?", 150, 792, beim("begr", "Hat"), "Bold", 34),
    ficon(HC, "classical-building", IX, IU, 150, "ober", fuell=WEISS),
    *fig("TA", FX, FB, FR, [("ober", "denkt"), ("begr", "ruhig")]),
    schild("Tabea", FX, "ober", TA_F),
]))

# E Fehlt die Zulässigkeit --------------------------------------------------------------------------------------------------------
folie([("unz", f"{ZU} › fehlt sie: keine Sachentscheidung"), ("p109", f"{ZU} › Zwischenurteil, § 109 VwGO")], rechts_frei([
    *tafel("unz", "Fehlt eine Zulässigkeitsvoraussetzung"),
    z("keine Entscheidung in der Sache", 110, 190, beim("unz", "entscheidet"), "Bold", 36),
    *okz("meist: Abweisung als unzulässig", 195, 280, beim("unz2", "unzulässig"), size=34),
    *okz("falscher Rechtsweg: Verweisung an das", 195, 360, beim("unz2", "verweist"), size=34),
    z("zuständige Gericht", 195, 413, beim("unz2", "zuständige"), size=34),
    zit("§ 17a Abs. 2 Satz 1 GVG i. V. m. § 173 Satz 1 VwGO", 195, 466, beim("unz2", "Gericht")),
    blk(110, 560, 1040, 80, GELB, beim("p109", "Zwischenurteil"), [("vorab: Zwischenurteil über die Zulässigkeit", "ExtraBold", 34, INK)]),
    zit("§ 109 VwGO", 150, 655, beim("p109", "Paragraf")),
    ficon(HC, "classical-building", IX, IU, 150, "unz", fuell=WEISS),
    *fig("TA", FX, FB, FR, [("unz", "denkt")]),
    schild("Tabea", FX, "unz", TA_F),
]))

# F Bausteine der Zulässigkeit I.–II. --------------------------------------------------------------------------------------------
folie([("bau", f"{ZU} · die Bausteine"), ("b1", f"{ZU} › I. Rechtsweg, § 40 I 1 VwGO"),
       ("b2", f"{ZU} › II. statthafte Klageart")], rechts_frei([
    *tafel("bau", "A. Zulässigkeit: die Bausteine"),
    z("I. Rechtsweg: Verwaltungsrechtsweg, § 40 Abs. 1 Satz 1 VwGO", 110, 190, "b1", "Bold", 32),
    z("öffentlich-rechtliche Streitigkeit", 150, 245, beim("b1", "öffentlich-rechtliche"), size=34),
    z("nichtverfassungsrechtlicher Art", 150, 298, beim("b1", "nichtverfassungsrechtlicher"), size=34),
    *okz("Fahrtenbuchauflage: Behörde, Straßenverkehrsrecht", 195, 365, beim("b1a", "Behörde"), size=32),
    z("II. statthafte Klageart", 110, 470, "b2", "Bold", 36),
    z("nach dem Begehren, vgl. § 88 VwGO", 150, 525, beim("b2", "Begehren"), size=34),
    z("Bescheid = Verwaltungsakt, § 35 Satz 1 VwVfG", 150, 595, beim("b2a", "Bescheid"), size=34),
    blk(150, 660, 1000, 80, GRUEN, beim("b2a", "Anfechtungsklage"),
        [("loswerden: Anfechtungsklage, § 42 Abs. 1 Alt. 1 VwGO", "ExtraBold", 32, INK)]),
    ficon("tabler", "notebook", IX, IU, 120, "bau", fuell=GELB),
    pl("Fahrtenbuchauflage", IX, 180, beim("b1a", "Fahrtenbuchauflage"), fill=WEISS, size=28, anker="m"),
    *fig("TA", FX, FB, FR, [("bau", "ruhig"), ("b2a", "aerger")]),
    schild("Tabea", FX, "bau", TA_F),
]))

# G Bausteine III.–V. ---------------------------------------------------------------------------------------------------------
folie([("b3", f"{ZU} › III. besondere Voraussetzungen der Klageart"), ("b4", f"{ZU} › IV. Beteiligte"),
       ("b5", f"{ZU} › V. Rechtsschutzbedürfnis")], rechts_frei([
    *tafel("b3", "A. Zulässigkeit: die Bausteine"),
    z("III. besondere Voraussetzungen der Klageart", 110, 190, "b3", "Bold", 36),
    z("Klagebefugnis, § 42 Abs. 2 VwGO", 150, 245, beim("b3", "Klagebefugnis"), size=34),
    z("Vorverfahren, wenn nötig, §§ 68 ff. VwGO", 150, 298, beim("b3", "Vorverfahren"), size=34),
    z("Klagefrist, § 74 VwGO", 150, 351, beim("b3", "Klagefrist"), size=34),
    z("IV. Beteiligte", 110, 430, "b4", "Bold", 36),
    z("richtiger Klagegegner, § 78 VwGO", 150, 485, beim("b4", "Klagegegner"), size=34),
    z("Beteiligten- und Prozessfähigkeit, §§ 61, 62 VwGO", 150, 538, beim("b4", "Beteiligten-"), size=34),
    z("V. Rechtsschutzbedürfnis", 110, 617, "b5", "Bold", 36),
    pl("Im Einzelnen: Video zur Anfechtungsklage", 110, 720, beim("b6", "Video"), fill=WEISS, size=30),
    ficon("tabler", "list-check", IX, IU, 130, "b3", fuell=WEISS),
    *fig("TA", FX, FB, FR, [("b3", "ruhig")]),
    schild("Tabea", FX, "b3", TA_F),
]))

# H III. Klagebefugnis, Wortlaut § 42 II, Fehler 1 ---------------------------------------------------------------------------------
W422 = ("„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage nur zulässig, wenn der Kläger geltend macht, durch den "
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen Rechten verletzt zu sein.“")
Z422 = ["„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage",
        "nur zulässig, wenn der Kläger geltend macht, durch den",
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung",
        "in seinen Rechten verletzt zu sein.“"]
w422, w422_y = wortlaut(80, 150, 1100, W422, "§ 42 Abs. 2 VwGO", "wl42", size=34, zeilen=Z422,
                        marken=[("geltend macht", beim("wl42", "geltend")),
                                ("in seinen Rechten verletzt", beim("wl42", "verletzt"))])
folie([("wl42", f"{ZU} › III. Klagebefugnis, § 42 II VwGO"), ("f1", "Typische Fehler › volle Rechtsverletzung geprüft")],
      rechts_frei([
    titel(glyphen("III. Klagebefugnis"), 110, 65, "wl42", 46),
    *w422,
    z("Verletzung muss möglich sein", 110, w422_y + 25, beim("mt", "möglich"), "Bold", 34),
    z("ob sie wirklich vorliegt: noch nicht hier", 150, w422_y + 78, beim("mt", "wirklich"), size=32),
    zit("BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9", 150, w422_y + 126, beim("mt", "Frage")),
    *okz("Adressatin eines belastenden Bescheids:", 195, w422_y + 185, beim("adr", "Adressatin"), "Bold", 34),
    z("allgemeine Handlungsfreiheit, Art. 2 Abs. 1 GG", 195, w422_y + 238, beim("adr", "allgemeinen"), size=32),
    zit("BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 195, w422_y + 286, beim("adr", "Handlungsfreiheit")),
    blk(110, w422_y + 345, 1040, 76, HELLROT, beim("f1", "Typischer"),
        [("Fehler 1: hier schon die ganze Rechtsverletzung prüfen", "ExtraBold", 32, INK)]),
    nein(1120, w422_y + 340, beim("f1", "Rechtsverletzung"), gr=26),
    ficon("tabler", "file-text", IX, IU, 120, "wl42", fuell=WEISS),
    pl("an Tabea", IX, 180, beim("adr", "Adressatin"), fill=WEISS, size=28, anker="m"),
    *fig("TA", FX, FB, FR, [("wl42", "denkt"), ("adr", "ruhig")]),
    schild("Tabea", FX, "wl42", TA_F),
]))

# I Fehler 2: Lennart, Ergebnis der Zulässigkeit ---------------------------------------------------------------------------------
LEb2 = ("LE_einsicht", X1, FB, FR)
folie([("f2", "Typische Fehler › Begründetheit in der Zulässigkeit"), ("zulerg", f"{ZU} › Ergebnis: zulässig")], rechts_frei([
    *tafel("f2", "Fehler 2: Begründetheit in der Zulässigkeit", size=40),
    z("Lennart:", 110, 180, beim("f2", "Lennart"), "Bold", 34),
    blk(110, 235, 1040, 80, HELLROT, beim("f2", "begründet"), [("„Der Bescheid ist rechtswidrig,", "Bold", 34, INK)], rand=4),
    blk(110, 310, 1040, 80, HELLROT, beim("f2", "rechtswidrig"), [("deine Klage ist also zulässig.“", "Bold", 34, INK)], rand=4),
    nein(1110, 300, beim("f2", "rechtswidrig"), gr=30),
    z("rechtswidrig oder nicht: eine Frage der Begründetheit", 110, 430, beim("f2a", "Frage"), "Bold", 32),
    blk(110, 600, 1040, 90, GRUEN, beim("zulerg", "zulässig"), [("Ergebnis: Die Klage ist zulässig.", "ExtraBold", 38, INK)]),
    z("Annahme: auch die übrigen Voraussetzungen liegen vor", 110, 530, beim("zulerg", "übrigen"), size=30),
    ok(1100, 645, beim("zulerg", "zulässig"), gr=28),
    *fig("LE", X1, FB, FR, [("f2", "denkt")], bis="le2"),
    *redet("LE_einsicht", X1, FB, FR, "le2", "zulerg"),
    *fig("LE", X1, FB, FR, [("zulerg", "ruhig")], erst="cut"),
    schild("Lennart", X1, "f2", LE_F),
    *fig("TA", X2, FB, FR, [("f2", "ruhig")]),
    schild("Tabea", X2, "f2", TA_F),
    blase("sprech", 640, 210, "le2", 1560, 150, inhalt=["Stimmt. Erst die Zulässigkeit, und", "ob der Bescheid rechtswidrig ist,",
                                                       "kommt in die Begründetheit."], textsize=28, figur=LEb2, bis="zulerg"),
]))

# J B. Begründetheit, Wortlaut § 113 I 1 ------------------------------------------------------------------------------------------
W113 = ("„Soweit der Verwaltungsakt rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht den "
        "Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“")
Z113 = ["„Soweit der Verwaltungsakt rechtswidrig und der Kläger",
        "dadurch in seinen Rechten verletzt ist, hebt das Gericht",
        "den Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“"]
w113, w113_y = wortlaut(80, 175, 1100, W113, "§ 113 Abs. 1 Satz 1 VwGO", "wl113", size=32, zeilen=Z113,
                        marken=[("rechtswidrig", beim("wl113", "rechtswidrig")),
                                ("in seinen Rechten verletzt", beim("wl113", "verletzt")),
                                ("hebt das Gericht", beim("wl113", "hebt"))])
folie([("wl113", f"{BG}, § 113 I 1 VwGO")], rechts_frei([
    titel(glyphen("B. Begründetheit (Anfechtungsklage)"), 110, 75, "wl113", 46),
    *w113,
    blk(110, w113_y + 45, 1040, 80, BLAU, beim("zwei", "Rechtswidrigkeit"), [("I. Rechtswidrigkeit", "ExtraBold", 36, INK)]),
    blk(110, w113_y + 150, 1040, 80, GRUEN, beim("zwei", "Rechtsverletzung"), [("II. Rechtsverletzung", "ExtraBold", 36, INK)]),
    ficon(HC, "classical-building", IX, IU, 150, "wl113", fuell=WEISS),
    *fig("TA", FX, FB, FR, [("wl113", "denkt")]),
    schild("Tabea", FX, "wl113", TA_F),
]))

# K I. Rechtswidrigkeit, § 31a StVZO ------------------------------------------------------------------------------------------------
W31 = "„… wenn die Feststellung eines Fahrzeugführers nach einer Zuwiderhandlung gegen Verkehrsvorschriften nicht möglich war.“"
Z31 = ["„… wenn die Feststellung eines Fahrzeugführers nach einer",
       "Zuwiderhandlung gegen Verkehrsvorschriften nicht möglich war.“"]
w31, w31_y = wortlaut(80, 470, 1100, W31, "§ 31a Abs. 1 Satz 1 StVZO (Auszug)", "tb", size=32, zeilen=Z31,
                      marken=[("Feststellung eines Fahrzeugführers", beim("tb", "Feststellung")),
                              ("nicht möglich war.“", beim("tb", "möglich"))])
folie([("rw", f"{BG} › I. Rechtswidrigkeit"), ("egl", f"{BG} › I. 1. Ermächtigungsgrundlage, § 31a StVZO"),
       ("tb", f"{BG} › I. 3. materielle Rechtmäßigkeit › Tatbestand")], rechts_frei([
    *tafel("rw", "I. Rechtswidrigkeit"),
    z("1. Ermächtigungsgrundlage", 150, 180, beim("rw", "Ermächtigungsgrundlage"), "Bold", 34),
    z("2. formelle Rechtmäßigkeit", 150, 233, beim("rw", "formelle"), "Bold", 34),
    z("3. materielle Rechtmäßigkeit", 150, 286, beim("rw", "materielle"), "Bold", 34),
    z("hier: § 31a Abs. 1 Satz 1 StVZO, Fahrtenbuch", 110, 370, beim("egl", "Paragraf"), size=34),
    z("Behörde kann gegenüber dem Halter anordnen,", 110, 420, beim("tb", "Halter"), size=30),
    *w31,
    ficon("tabler", "notebook", IX, IU, 120, "rw", fuell=GELB),
    pl("§ 31a StVZO", IX, 180, beim("egl", "Paragraf"), fill=GELB, size=30, anker="m"),
    *fig("TA", FX, FB, FR, [("rw", "ruhig"), ("tb", "denkt")]),
    schild("Tabea", FX, "rw", TA_F),
]))

# L Das Argument von Tabea, Rechtsverletzung, Ergebnis ---------------------------------------------------------------------------
folie([("arg", f"{BG} › I. 3. materielle Rechtmäßigkeit › Feststellung des Fahrers"), ("rv", f"{BG} › II. Rechtsverletzung"),
       ("erg", "Ergebnis · Hat die Klage Erfolg?")], rechts_frei([
    *tafel("arg", "Erst hier: das Argument von Tabea", size=42),
    blk(110, 180, 1040, 76, HELL, "arg", [("„Ich bin doch gar nicht gefahren!“", "Bold", 34, INK)], rand=4),
    *neinz("nicht: Ist sie selbst gefahren?", 195, 290, beim("arg2", "selbst"), size=34),
    *okz("sondern: Konnte der Fahrer festgestellt werden?", 195, 345, beim("arg2", "Fahrer"), "Bold", 34),
    z("II. Rechtsverletzung: als Adressatin regelmäßig (+)", 110, 440, beim("rv", "Adressatin"), "Bold", 32),
    zit("BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 150, 490, beim("rv", "Rechten")),
    *okz("A. Zulässigkeit: zulässig", 195, 575, beim("erg", "Zulässig"), "Bold", 34),
    blk(110, 650, 1040, 120, BLAU, beim("erg2", "Begründetheit"),
        [("Den Erfolg entscheidet die Begründetheit:", "ExtraBold", 32, INK),
         ("War der Fahrer festzustellen?", "ExtraBold", 32, INK)]),
    ficon("tabler", "zoom-question", IX, IU, 120, "arg", fuell=WEISS),
    *fig("TA", X2, FB, FR, [("arg", "aerger"), ("arg2", "denkt"), ("erg", "ruhig")]),
    schild("Tabea", X2, "arg", TA_F),
    *fig("LE", X1, FB, FR, [("arg", "ruhig"), ("erg2", "denkt")]),
    schild("Lennart", X1, "arg", LE_F),
]))

# M Gleicher Aufbau in anderen Verfahren -----------------------------------------------------------------------------------------
folie([("ueb", "Übertragung · gleicher Grundaufbau"), ("vb", "Übertragung › Verfassungsbeschwerde, Art. 94 I Nr. 4a GG"),
       ("eil", "Übertragung › Eilverfahren, § 80 V VwGO")], rechts_frei([
    *tafel("ueb", "Gleicher Grundaufbau in anderen Verfahren", size=40),
    z("Verfassungsbeschwerde", 110, 175, "vb", "ExtraBold", 36),
    z("A. Zulässigkeit: Art. 94 Abs. 1 Nr. 4a GG, §§ 90 ff. BVerfGG", 150, 230, beim("vb", "Zulässigkeit"), size=30),
    z("z. B. Beschwerdebefugnis, Rechtswegerschöpfung,", 150, 278, beim("vb2", "Beschwerdebefugnis"), size=30),
    z("Frist (§ 90 Abs. 1, 2; § 93 BVerfGG)", 150, 324, beim("vb2", "Frist"), size=30),
    z("B. Begründetheit: tatsächlich in einem Grundrecht", 150, 380, beim("vb3", "Begründet"), "Bold", 30),
    z("oder grundrechtsgleichen Recht verletzt", 150, 426, beim("vb3", "grundrechtsgleichen"), "Bold", 30),
    zit("vgl. § 95 Abs. 1 Satz 1 BVerfGG", 150, 474, beim("vb3", "verletzt")),
    z("Eilverfahren, § 80 Abs. 5 VwGO", 110, 545, "eil", "ExtraBold", 36),
    z("A. Zulässigkeit und B. Begründetheit des Antrags", 150, 600, beim("eil", "Zulässigkeit"), size=30),
    z("Begründetheit: Interessenabwägung, vor allem nach", 150, 655, beim("eil2", "Interessen"), "Bold", 30),
    z("den Erfolgsaussichten in der Hauptsache", 150, 701, beim("eil2", "Erfolgsaussichten"), "Bold", 30),
    zit("BVerwG, Beschl. v. 11.11.2020 – 7 VR 5.20, Rn. 8", 150, 749, beim("eil2", "Hauptsache")),
    ficon(HC, "classical-building", IX, IU, 140, "vb", fuell=WEISS, bis="eil"),
    pl("Verfassungsbeschwerde", IX, 190, beim("vb", "Verfassungsbeschwerde"), fill=WEISS, size=28, anker="m", bis="eil"),
    ficon("tabler", "hourglass", IX, IU, 120, "eil", fuell=GELB),
    pl("Eilverfahren", IX, 190, beim("eil", "Eilverfahren"), fill=WEISS, size=28, anker="m"),
    *fig("LE", FX, FB, FR, [("ueb", "ruhig"), ("eil", "denkt")]),
    schild("Lennart", FX, "ueb", LE_F),
]))

# N Gewichtung --------------------------------------------------------------------------------------------------------------------
folie([("gew", "Gewichtung · Urteilsstil und Gutachtenstil")], rechts_frei([
    *tafel("gew", "Wie ausführlich?"),
    z("unproblematisch: knapp im Urteilsstil", 110, 200, beim("gew1", "Urteilsstil"), "Bold", 36),
    z("etwa der Rechtsweg", 150, 255, beim("gew1", "Rechtsweg"), size=34),
    z("das Problem: im Gutachtenstil", 110, 355, beim("gew2", "Gutachtenstil"), "Bold", 36),
    z("hier: die Feststellung des Fahrers", 150, 410, beim("gew2", "Feststellung"), size=34),
    pl("Mehr dazu: Video Gutachtenstil", 110, 520, beim("gew3", "Video"), fill=WEISS, size=30),
    ficon("tabler", "writing", IX, IU, 130, "gew", fuell=WEISS),
    *fig("TA", FX, FB, FR, [("gew", "ruhig"), ("gew2", "denkt")]),
    schild("Tabea", FX, "gew", TA_F),
]))

# O Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Wohin gehört der Gedanke?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Wohin gehört der Gedanke?", 200, 200, beim("tipp", "wohin"), "Bold", 38),
    z("Darf das Gericht entscheiden?", 200, 320, beim("tipp1", "Gericht"), size=36),
    blk(200, 375, 760, 76, BLAU, beim("tipp1", "Zulässigkeit"), [("Zulässigkeit", "ExtraBold", 36, INK)]),
    z("Hat die Behörde richtig gehandelt?", 200, 510, beim("tipp2", "Behörde"), size=36),
    blk(200, 565, 760, 76, GRUEN, beim("tipp2", "Begründetheit"), [("Begründetheit", "ExtraBold", 36, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# P Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 32, 60
LX0, RX0 = 110, 1000
links = [("s1", "I. Rechtsweg, § 40 I 1 VwGO"), ("s2", "II. statthafte Klageart"),
         ("s3", "III. besondere Voraussetzungen"), ("s3", "der Klageart (z. B. § 42 II, §§ 68 ff., § 74)"),
         ("s4", "IV. Beteiligte (§§ 61, 62, 78)"), ("s5", "V. Rechtsschutzbedürfnis")]
rechts_ = [("s6", "I. Rechtswidrigkeit:", "Bold"), ("s6", "1. Ermächtigungsgrundlage", "Regular"),
           ("s6", "2. formelle Rechtmäßigkeit", "Regular"), ("s6", "3. materielle Rechtmäßigkeit", "Regular"),
           ("s7", "II. Rechtsverletzung", "Bold")]
els_t = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: Zulässigkeit und Begründetheit"), 110, 85, "sch", 46),
         blk(110, 160, 1700, 70, HELL, "s0", [("Obersatz: „Die Klage hat Erfolg, soweit sie zulässig und begründet ist.“", "Bold", 32, INK)], rand=4),
         z("A. Zulässigkeit", LX0, 265, "sa", "ExtraBold", 38, rechts=980),
         z("B. Begründetheit (§ 113 I 1 VwGO)", RX0, 265, "sb", "ExtraBold", 38, rechts=1820),
         z("C. Ergebnis", LX0, 790, "sc", "ExtraBold", 38, rechts=980)]
for i, (c, t) in enumerate(links):
    eingerueckt = t.startswith("der Klageart")
    els_t.append(z(t, LX0 + (70 if eingerueckt else 30), 335 + i * LH, c, size=SZ if not eingerueckt else 28, rechts=980))
for i, (c, t, s) in enumerate(rechts_):
    cue = c if i in (0, 4) else beim("s6", {1: "Ermächtigungsgrundlage", 2: "formeller", 3: "materieller"}[i])
    els_t.append(z(t, RX0 + (30 if s == "Bold" else 70), 335 + i * LH, cue, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · Zulässigkeit und Begründetheit")], els_t)

# Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die ", 0), ("Zulässigkeit", "a"), (" fragt,", 0)]], 750, 310, 46, "merke", {"a": beim("merke", "Zulässigkeit")}),
    *markertext([[("ob das Gericht entscheiden darf,", 0)]], 750, 375, 46, beim("merke", "ob"), {}),
    *markertext([[("die ", 0), ("Begründetheit,", "b")]], 750, 440, 46, beim("merke", "die", 2), {"b": beim("merke", "Begründetheit")}),
    *markertext([[("wer in der Sache recht hat.", 0)]], 750, 505, 46, beim("merke", "wer"), {}),
    *markertext([[("Was die Sache betrifft,", 0)]], 750, 640, 46, "m2", {}),
    *markertext([[("gehört erst in die ", 0), ("Begründetheit.", "c")]], 750, 705, 46, beim("m2", "gehört"),
                {"c": beim("m2", "Begründetheit")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
