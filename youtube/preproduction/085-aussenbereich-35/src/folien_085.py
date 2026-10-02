"""Folge 085 · Außenbereich § 35 BauGB: Warum dein Ferienhaus im Wald verboten ist – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Waldgrundstück, Bauantrag für ein Wochenendhaus, Ablehnung durch die Bauaufsichtsbehörde), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Wald (Grundstück, Plan), B Bauaufsichtsbehörde (Antrag, Ablehnung, Frage), C Sachverhalt,
D Zwei Ebenen + I. Vorhaben, E II. Bereich, F III. Privilegiert?, G IV. sonstiges Vorhaben (Wortlaut § 35 II),
H 1. öffentliche Belange (Wortlaut § 35 III 1, Nr. 1, 5), I Nr. 7 Splittersiedlung, J 2. § 35 IV, 3. Erschließung, Ergebnis,
K zurück im Wald (Waldrecht, Rechtsschutz), L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, wenn der Bauantrag erscheint)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_085/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_085/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 082/069/064/061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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
WI_F, DR_F = GRUEN, BLAU                    # Farben der Namensschilder
IV = "IV. Sonstiges Vorhaben"
OB = f"{IV} › 1. Öffentliche Belange"
DUNKELGRUEN = (70, 140, 85, 255)


def wald(cue, anim="pop", bis=None, xs=(150, 330, 510), xs2=(1300, 1480, 1680)):
    """Fichtenwald: Fluent HC „evergreen-tree“ (grün gefüllt) links und rechts – in jeder Waldszene gleich."""
    els = []
    for i, x in enumerate(list(xs) + list(xs2)):
        h = 300 if i % 2 == 0 else 250
        els.append(ficon(HC, "evergreen-tree", x, BODEN - 2, h, cue, fuell=GRUEN, anim=anim, bis=bis))
    return els


# A Fall: das Waldgrundstück ------------------------------------------------------------------------------------------------
WIX = 900
folie([(NULL, "Fall · Das Waldgrundstück")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Weit draußen vor dem Dorf", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *[hart(e) for e in wald(NULL, anim="cut")],
    *fig("WI", WIX, BODEN, FH, [(NULL, "ruhig"), (beim("plan", "Wochenendhaus"), "froh")], bis="wi1", erst="cut"),
    *redet("WI_redet", WIX, BODEN, FH, "wi1", "antrag"),
    hart(schild("Frau Wiesner", WIX, NULL, WI_F, unten=BODEN, d=0.0)),
    pl("Waldgrundstück gekauft", 560, 215, beim("fall", "Waldgrundstück"), fill=WEISS, size=32, anker="m", bis="wi1"),
    pl("mitten im Fichtenwald", 560, 285, beim("fall", "Fichtenwald"), fill=GRUEN, size=32, anker="m", bis="wi1"),
    blase("denk", 330, 270, beim("plan", "Wochenendhaus"), 1250, 230, figur=("WI_froh", WIX, BODEN, FH), bis="wi1"),
    ficon(HC, "hut", 1250, 280, 130, beim("plan", "Wochenendhaus"), fuell=GELB, d=0.2, bis="wi1"),
    pl("kleines Wochenendhaus", 1250, 400, beim("plan", "kleines"), fill=GELB, size=30, anker="m", bis="wi1"),
    blase("sprech", 820, 200, "wi1", 1240, 190, inhalt=["Hier baue ich mir mein Wochenendhaus.", "Nur ich, die Bäume und die Ruhe."],
          textsize=30, figur=("WI_redet", WIX, BODEN, FH)),
])

# B Fall: Bauantrag und Ablehnung -------------------------------------------------------------------------------------------
WIB, DRB = 820, 1500
WIb = ("WI_protest_r", WIB, BODEN, FH)
DRb = ("DR_redet", DRB, BODEN, FH)
LEHNT = beim("dr1", "lehne")
folie([("antrag", "Fall · Der Bauantrag"), ("dr1", "Fall · Die Ablehnung"), ("frage", "Fall · War die Ablehnung rechtmäßig?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "antrag", breite=7, farbe=INK),
    pl("Der Bauantrag", 70, 40, beim("antrag", "Bauantrag"), fill=GELB, size=40),
    ficon("tabler", "building", 330, BODEN - 2, 330, "antrag", fuell=WEISS),
    pl("Bauaufsichtsbehörde", 330, 450, beim("dreher", "Bauaufsichtsbehörde"), fill=WEISS, size=30, anker="m"),
    *fig("WI", WIB, BODEN, FH, [("antrag", "ruhig_r"), (LEHNT, "sorge_r")], bis="wi2"),
    *redet("WI_protest_r", WIB, BODEN, FH, "wi2", "frage"),
    *fig("WI", WIB, BODEN, FH, [("frage", "denkt_r")]),
    schild("Frau Wiesner", WIB, "antrag", WI_F, unten=BODEN),
    *fig("DR", DRB, BODEN, FH, [(beim("dreher", "Herr"), "ruhig")], bis="dr1"),
    *redet("DR_redet", DRB, BODEN, FH, "dr1", "wi2"),
    *fig("DR", DRB, BODEN, FH, [("wi2", "ruhig")]),
    schild("Herr Dreher, Bauaufsichtsbehörde", DRB, beim("dreher", "Herr"), DR_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", 1160, 690, 100, beim("antrag", "Bauantrag"), fuell=WEISS), "085papier*", 0.8, -0.35),
    pl("Bauantrag: Wochenendhaus", 1160, 720, beim("antrag", "Bauantrag"), fill=GELB, size=28, anker="m"),
    nein(1215, 610, LEHNT, gr=34),
    pl("kein Bebauungsplan", 1160, 330, beim("lage", "Bebauungsplan"), fill=WEISS, size=30, anker="m", bis="frage"),
    ficon("tabler", "map", 1160, 455, 80, beim("lage", "Flächennutzungsplan"), fuell=GRUEN, bis="frage"),
    pl("Flächennutzungsplan: Wald", 1160, 480, beim("lage", "Wald"), fill=GRUEN, size=30, anker="m", bis="frage"),
    blase("sprech", 780, 200, "dr1", 1150, 190, inhalt=["Frau Wiesner, ein Wochenendhaus mitten im", "Wald darf ich nicht genehmigen.",
                                                       "Ich lehne Ihren Antrag ab."], textsize=29, figur=DRb, bis="wi2"),
    blase("sprech", 700, 180, "wi2", 1150, 190, inhalt=["Aber es ist doch mein Grundstück!", "Und das Haus ist ganz klein."],
          textsize=30, figur=WIb, bis="frage"),
    pl("War die Ablehnung rechtmäßig?", 1160, 190, "frage", fill=PINK, size=44, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Wiesner kauft ein Waldgrundstück weit draußen vor dem Dorf, mitten im Fichtenwald. Dort will sie ein kleines "
    "Wochenendhaus bauen und stellt einen Bauantrag. Für die Fläche gilt kein Bebauungsplan; ringsum steht nur Wald. Der "
    "Flächennutzungsplan der Gemeinde stellt die Fläche als Wald dar. Das Waldstück ist in viele Parzellen geteilt. "
    "Herr Dreher von der Bauaufsichtsbehörde lehnt den Bauantrag ab.",
], "War die Ablehnung rechtmäßig?")

# D Zwei Ebenen, I. Vorhaben -----------------------------------------------------------------------------------------------
folie([("ebenen", "Grundlagen · Zwei Ebenen des Baurechts"), ("vorh", "I. Vorhaben, § 29 I BauGB")], rechts_frei([
    *tafel("ebenen", "Zwei Ebenen des Baurechts"),
    blk(110, 175, 1040, 132, GELB, beim("ebenen", "Bauplanungsrecht"),
        [("Bauplanungsrecht: Baugesetzbuch", "ExtraBold", 34, INK), ("Ist das Vorhaben an diesem Ort zulässig?", "Regular", 32, INK)]),
    blk(110, 325, 1040, 132, BLAU, beim("ordnung", "Bauordnungsrecht"),
        [("Bauordnungsrecht: Bauordnung deines Landes", "ExtraBold", 34, INK),
         ("Genehmigungsverfahren, Sicherheit des Baus", "Regular", 32, INK)]),
    z("I. Vorhaben, § 29 Abs. 1 BauGB", 110, 510, "vorh", "Bold", 36),
    z("Errichtung einer baulichen Anlage", 150, 565, beim("vorh", "Errichtung"), size=34),
    ok(1100, 590, beim("vorh", "Anlage"), gr=22),
    blk(110, 650, 1040, 80, GRUEN, "gelten", [("es gelten die §§ 30 bis 37 BauGB", "ExtraBold", 36, INK)]),
    ficon(HC, "hut", IX, IU, 150, "ebenen", fuell=GELB),
    pl("Wochenendhaus", IX, 190, beim("vorh", "Wochenendhaus"), fill=GELB, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("ebenen", "ruhig"), ("vorh", "denkt")]),
    schild("Frau Wiesner", FX, "ebenen", WI_F),
]))

# E II. Bereich ---------------------------------------------------------------------------------------------------------------
BE = "II. Bereich"
folie([("reihe", BE), ("p30", f"{BE} › § 30 BauGB: Bebauungsplan?"), ("p34", f"{BE} › § 34 BauGB: Innenbereich?"),
       ("p35", f"{BE} › Außenbereich, § 35 BauGB")], rechts_frei([
    *tafel("reihe", "II. Der Bereich"),
    z("immer in dieser Reihenfolge:", 110, 170, beim("reihe", "Reihenfolge"), size=32, farbe=TEXT),
    z("1. Gilt ein Bebauungsplan, § 30 BauGB?", 110, 240, "p30", "Bold", 36),
    z("hier nicht", 150, 295, beim("p30", "nicht"), size=34),
    nein(330, 318, beim("p30", "nicht"), gr=22),
    z("2. Im Zusammenhang bebauter Ortsteil,", 110, 380, "p34", "Bold", 36),
    z("also Innenbereich, § 34 BauGB?", 150, 435, beim("p34", "Innenbereich"), "Bold", 36),
    z("auch nicht: rundherum nur Wald", 150, 495, beim("p34", "Auch"), size=34),
    nein(680, 518, beim("p34", "Auch"), gr=22),
    blk(110, 580, 1040, 80, GRUEN, "p35", [("also Außenbereich: § 35 BauGB", "ExtraBold", 38, INK)]),
    zit("BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 11", 150, 680, beim("p35", "Außenbereich")),
    ficon(HC, "evergreen-tree", IX - 90, IU, 150, "reihe", fuell=GRUEN),
    ficon(HC, "evergreen-tree", IX + 90, IU, 120, "reihe", fuell=GRUEN),
    pl("rundherum nur Wald", IX, 190, beim("p34", "rundherum"), fill=GRUEN, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("reihe", "denkt")]),
    schild("Frau Wiesner", FX, "reihe", WI_F),
]))

# F III. Privilegiert? --------------------------------------------------------------------------------------------------------
PR = "III. Privilegiert, § 35 I BauGB?"
folie([("abs1", PR), ("nr4", f"{PR} › Nr. 4"), ("sonst", "III. Privilegiert? › nein: sonstiges Vorhaben")], rechts_frei([
    *tafel("abs1", "III. Privilegiert? § 35 Abs. 1 BauGB", size=42),
    z("Nr. 1: dient einem land- oder forstwirtschaftlichen Betrieb", 110, 165, "nr1", size=32),
    z("Nr. 5: Windenergie", 110, 215, beim("nr5", "Windenergie"), size=32),
    z("zulässig, wenn öffentliche Belange nicht entgegenstehen", 110, 280, beim("entg", "zulässig"), "Bold", 32),
    z("und die ausreichende Erschließung gesichert ist", 110, 325, beim("entg", "Erschließung"), "Bold", 32),
    zit("bevorrechtigt: BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 20", 150, 372, beim("entg", "bevorrechtigt")),
    z("Wochenendhaus: kein Betrieb, sondern Erholung", 110, 440, beim("kein1", "Wochenendhaus"), size=32),
    nein(1100, 462, beim("kein1", "erholen"), gr=22),
    z("Nr. 4: muss nicht im Außenbereich stehen", 110, 500, beim("nr4", "Ein"), size=32),
    zit("eigene Wochenendhausgebiete möglich, § 10 Abs. 1 BauNVO", 150, 548, beim("nr4", "Wochenendhausgebiete")),
    nein(1100, 522, beim("nr4", "Wochenendhausgebiete"), gr=22),
    blk(110, 620, 1040, 80, GELB, beim("sonst", "sonstiges"), [("also: sonstiges Vorhaben", "ExtraBold", 38, INK)]),
    ficon("tabler", "tractor", IX - 110, IU, 120, "nr1", fuell=GELB, bis="kein1"),
    ficon("tabler", "windmill", IX + 110, IU, 110, beim("nr5", "Windenergie"), fuell=WEISS, bis="kein1"),
    ficon(HC, "hut", IX, IU, 140, "kein1", fuell=GELB),
    pl("Erholung", IX, 190, beim("kein1", "erholen"), fill=GELB, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("abs1", "ruhig"), ("kein1", "denkt"), ("sonst", "sorge")]),
    schild("Frau Wiesner", FX, "abs1", WI_F),
]))

# G IV. Sonstiges Vorhaben: Wortlaut § 35 II ----------------------------------------------------------------------------------
W352 = ("„Sonstige Vorhaben können im Einzelfall zugelassen werden, wenn ihre Ausführung oder Benutzung öffentliche Belange "
        "nicht beeinträchtigt und die Erschließung gesichert ist.“")
Z352 = ["„Sonstige Vorhaben können im Einzelfall zugelassen werden,",
        "wenn ihre Ausführung oder Benutzung öffentliche Belange",
        "nicht beeinträchtigt und die Erschließung gesichert ist.“"]
w352, w352_y = wortlaut(80, 175, 1100, W352, "§ 35 Abs. 2 BauGB", "wl352", size=34, zeilen=Z352,
                        marken=[("nicht beeinträchtigt", beim("wl352", "beeinträchtigt")),
                                ("Erschließung gesichert", beim("wl352", "Erschließung"))])
folie([("wl352", f"{IV}, § 35 II BauGB")], rechts_frei([
    titel(glyphen("IV. Sonstiges Vorhaben"), 110, 75, "wl352", 50),
    *w352,
    z("strenger als bei Abs. 1:", 110, w352_y + 50, beim("streng", "strenger"), "Bold", 36),
    blk(110, w352_y + 115, 1040, 126, ROT, beim("streng", "scheitert"),
        [("Die Zulassung scheitert schon,", "ExtraBold", 36, INK), ("wenn ein Belang beeinträchtigt ist.", "ExtraBold", 36, INK)]),
    ficon(HC, "hut", IX, IU, 150, "wl352", fuell=GELB),
    pl("sonstiges Vorhaben", IX, 190, "wl352", fill=GELB, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("wl352", "sorge")]),
    schild("Frau Wiesner", FX, "wl352", WI_F),
]))

# H 1. Öffentliche Belange: Wortlaut § 35 III 1, Nr. 1 und 5 ------------------------------------------------------------------
W353 = ("„Eine Beeinträchtigung öffentlicher Belange liegt insbesondere vor, wenn das Vorhaben 1. den Darstellungen des "
        "Flächennutzungsplans widerspricht, … 5. … die natürliche Eigenart der Landschaft und ihren Erholungswert "
        "beeinträchtigt …, … 7. die Entstehung, Verfestigung oder Erweiterung einer Splittersiedlung befürchten lässt …“")
Z353 = ["„Eine Beeinträchtigung öffentlicher Belange liegt",
        "insbesondere vor, wenn das Vorhaben 1. den Darstellungen",
        "des Flächennutzungsplans widerspricht, … 5. … die",
        "natürliche Eigenart der Landschaft und ihren Erholungswert",
        "beeinträchtigt …, … 7. die Entstehung, Verfestigung oder",
        "Erweiterung einer Splittersiedlung befürchten lässt …“"]
w353, w353_y = wortlaut(80, 160, 1100, W353, "§ 35 Abs. 3 Satz 1 BauGB (Auszug)", "wl353", size=32, zeilen=Z353,
                        marken=[("insbesondere", beim("wl353", "Beispielen")),
                                ("des Flächennutzungsplans widerspricht,", beim("fnp", "widerspricht")),
                                ("natürliche Eigenart der Landschaft", beim("land", "natürliche"))])
folie([("wl353", f"{OB}, § 35 III 1 BauGB"), ("fnp", f"{OB} › Nr. 1 Flächennutzungsplan"),
       ("land", f"{OB} › Nr. 5 natürliche Eigenart der Landschaft")], rechts_frei([
    titel(glyphen("1. Öffentliche Belange"), 110, 70, "wl353", 46),
    *w353,
    z("Nr. 1: Der Plan stellt hier Wald dar,", 110, w353_y + 30, beim("fnp", "Plan"), "Bold", 32),
    z("kein Bauland für Wochenendhäuser", 150, w353_y + 77, beim("fnp", "Bauland"), size=32),
    z("Nr. 5: im forstlich genutzten Fichtenwald", 110, w353_y + 140, beim("land", "Fichtenwald"), "Bold", 32),
    z("ist ein Wochenendhaus ein Fremdkörper", 150, w353_y + 187, beim("land", "Fremdkörper"), size=32),
    ficon("tabler", "map", IX, IU, 120, "fnp", fuell=GRUEN, bis="land"),
    pl("Flächennutzungsplan: Wald", IX, 200, beim("fnp", "Wald"), fill=GRUEN, size=28, anker="m", bis="land"),
    ficon(HC, "evergreen-tree", IX - 90, IU, 150, "land", fuell=GRUEN),
    ficon(HC, "hut", IX + 80, IU, 90, "land", fuell=GELB),
    pl("Fremdkörper im Wald", IX, 200, beim("land", "Fremdkörper"), fill=ROT, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("wl353", "denkt"), ("land", "sorge")]),
    schild("Frau Wiesner", FX, "wl353", WI_F),
]))

# I Nr. 7 Splittersiedlung -----------------------------------------------------------------------------------------------------
folie([("split", f"{OB} › Nr. 7 Splittersiedlung"), ("beein", f"{OB}: beeinträchtigt")], rechts_frei([
    *tafel("split", "Nr. 7: Splittersiedlung"),
    z("„… die Entstehung, Verfestigung oder Erweiterung einer", 110, 185, "split", size=32),
    z("Splittersiedlung befürchten lässt …“", 110, 230, "split", size=32),
    zit("§ 35 Abs. 3 Satz 1 Nr. 7 BauGB", 700, 236, "split"),
    z("Splittersiedlung: bloße Anhäufung von Gebäuden,", 110, 305, beim("split", "bloßen"), "Bold", 32),
    z("kein Ortsteil", 150, 352, beim("split", "kein"), "Bold", 32),
    zit("BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 19", 150, 399, beim("split", "Ortsteil")),
    z("Waldstück in viele Parzellen geteilt", 110, 465, beim("vorbild", "Parzellen"), size=32),
    z("Nachbarn könnten sich auf ihr Haus berufen", 110, 512, beim("vorbild", "berufen"), size=32),
    z("so beginnt die Zersiedlung", 110, 559, beim("vorbild", "Zersiedlung"), "Bold", 32),
    zit("BVerwG, 4 C 10.11, Rn. 21 f. (Vorbildwirkung, Berufungsfall)", 150, 606, beim("vorbild", "Zersiedlung")),
    blk(110, 675, 1040, 80, ROT, "beein", [("öffentliche Belange beeinträchtigt", "ExtraBold", 38, INK)]),
    nein(1100, 715, beim("beein", "beeinträchtigt"), gr=26),
    ficon(HC, "hut", IX, IU, 120, "split", fuell=GELB),
    pl("ihr Haus", IX, 205, "split", fill=GELB, size=28, anker="m"),
    ficon(HC, "hut", IX - 200, IU, 90, beim("vorbild", "nebenan"), fuell=WEISS),
    ficon(HC, "hut", IX + 200, IU, 90, beim("vorbild", "nebenan"), fuell=WEISS),
    pl("Nachbarparzellen", IX, 120, beim("vorbild", "nebenan"), fill=WEISS, size=28, anker="m"),
    *fig("WI", FX, FB, FR, [("split", "denkt"), ("beein", "sorge")]),
    schild("Frau Wiesner", FX, "split", WI_F),
]))

# J 2. § 35 IV, 3. Erschließung, Ergebnis ----------------------------------------------------------------------------------------
folie([("abs4", f"{IV} › 2. Begünstigt, § 35 IV BauGB?"), ("erschl", f"{IV} › 3. Erschließung"),
       ("erg", "Ergebnis · Die Ablehnung war rechtmäßig")], rechts_frei([
    *tafel("abs4", "2. Begünstigt? § 35 Abs. 4 BauGB", size=44),
    z("nur bestimmte Vorhaben, z. B.:", 110, 170, beim("abs4", "begünstigt"), size=32),
    z("Umnutzung alter Hofgebäude, Satz 1 Nr. 1", 150, 220, beim("abs4", "Umnutzung"), size=32),
    z("Wiederaufbau eines abgebrannten Gebäudes, Nr. 3", 150, 267, beim("abs4", "Wiederaufbau"), size=32),
    z("neues Wochenendhaus: nein", 110, 330, beim("abs4", "neues"), "Bold", 34),
    nein(640, 352, beim("abs4", "gehört"), gr=22),
    z("3. Erschließung: kommt es nicht mehr an", 110, 420, "erschl", "Bold", 34),
    blk(110, 510, 1040, 126, GRUEN, "erg", [("Wochenendhaus unzulässig:", "ExtraBold", 38, INK),
                                            ("Die Ablehnung war rechtmäßig.", "ExtraBold", 38, INK)]),
    ok(1100, 600, beim("erg", "rechtmäßig"), gr=26),
    ficon("tabler", "file-text", IX, IU, 110, "abs4", fuell=WEISS),
    pl("Bauantrag", IX, 205, "abs4", fill=WEISS, size=28, anker="m", bis=beim("erg", "Ablehnung")),
    nein(IX + 50, IU - 70, beim("erg", "Ablehnung"), gr=26),
    pl("Ablehnung rechtmäßig", IX, 205, beim("erg", "Ablehnung"), fill=GRUEN, size=28, anker="m"),
    *fig("DR", FX, FB, FR, [("abs4", "denkt"), ("erg", "ruhig")]),
    schild("Herr Dreher, Bauaufsichtsbehörde", FX, "abs4", DR_F),
]))

# K Zurück im Wald: Waldrecht, Rechtsschutz -------------------------------------------------------------------------------------
WIK = 980
folie([("wald", "Ergebnis · Waldrecht"), ("klage", "Ergebnis · Rechtsschutz")], [
    linienzug([(60, BODEN), (1860, BODEN)], "wald", breite=7, farbe=INK),
    pl("Das Waldrecht", 70, 40, beim("wald", "Waldrecht"), fill=GELB, size=40),
    ficon("tabler", "sun", 1760, 190, 120, "wald", fuell=GELB),
    *wald("wald"),
    *fig("WI", WIK, BODEN, FH, [("wald", "sorge"), ("klage", "denkt")], bis="wi3"),
    *redet("WI_seufzt", WIK, BODEN, FH, "wi3", "tipp"),
    schild("Frau Wiesner", WIK, "wald", WI_F, unten=BODEN),
    ficon("tabler", "axe", 700, BODEN - 4, 90, beim("wald", "gerodet"), fuell=WEISS, bis="klage"),
    pl("Waldrecht: Roden nur mit Genehmigung", 980, 170, beim("wald", "Genehmigung"), fill=WEISS, size=32, anker="m", bis="wi3"),
    pl("§ 9 Abs. 1 Satz 1 BWaldG", 980, 235, beim("wald", "gerodet"), fill=WEISS, size=26, anker="m", bis="wi3"),
    ficon(HC, "classical-building", 700, BODEN - 4, 150, "klage", fuell=WEISS, bis="wi3"),
    pl("Verpflichtungsklage", 980, 315, beim("klage", "Verpflichtungsklage"), fill=BLAU, size=32, anker="m", bis="wi3"),
    pl("ohne Erfolg", 980, 385, beim("klage", "Erfolg"), fill=ROT, size=32, anker="m", bis="wi3"),
    blase("sprech", 780, 160, "wi3", 1000, 190, inhalt=["Dann bleibt mein Wald eben ein Wald."], textsize=32,
          figur=("WI_seufzt", WIK, BODEN, FH)),
])

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Erst der Bereich, dann die Gruppe")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfung in der Begründetheit:", 200, 200, beim("tipp", "Begründetheit"), "Bold", 34),
    z("Muss die Baugenehmigung erteilt werden?", 200, 255, beim("tipp", "Baugenehmigung"), size=34),
    z("zuerst den Bereich, dann die Gruppe", 200, 350, "tipp1", "Bold", 34),
    z("Katalog in § 35 Abs. 3 nicht abschließend:", 200, 445, "tipp2", "Bold", 34),
    z("„insbesondere“", 200, 500, beim("tipp2", "insbesondere"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 38, 76
zeilen_ = [("s1", "I. Vorhaben, § 29 Abs. 1 BauGB", "Bold", 0),
           ("s2", "II. Außenbereich: kein Bebauungsplan (§ 30), kein Innenbereich (§ 34)", "Bold", 0),
           ("s3", "III. Privilegiert nach § 35 Abs. 1?", "Bold", 0),
           ("s4", "IV. Wenn nicht: sonstiges Vorhaben, § 35 Abs. 2", "Bold", 0),
           ("s5", "1. öffentliche Belange, § 35 Abs. 3", "Regular", 1),
           ("s6", "2. Begünstigung, § 35 Abs. 4", "Regular", 1),
           ("s7", "3. Erschließung", "Regular", 1)]
els_t = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Klausurschema: Bauen im Außenbereich, § 35 BauGB"), 110, 85, "sch", 46)]
for i, (c, t, s, e) in enumerate(zeilen_):
    els_t.append(z(t, 140 + 60 * e, 200 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · § 35 BauGB")], els_t)

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Bei ", 0), ("privilegierten", "a"), (" Vorhaben fragst du,", 0)]], 750, 330, 42, beim("merke", "Bei"),
                {"a": beim("merke", "privilegierten")}),
    *markertext([[("ob öffentliche Belange ", 0), ("entgegenstehen.", "b")]], 750, 395, 42, beim("merke", "ob"),
                {"b": beim("merke", "entgegenstehen")}),
    *markertext([[("Ein Wochenendhaus ist ein ", 0), ("sonstiges Vorhaben:", "c")]], 750, 535, 42, "m2",
                {"c": beim("m2", "sonstiges")}),
    *markertext([[("Es scheitert schon, wenn es einen ", 0), ("einzigen", "d")]], 750, 600, 42, beim("m2", "Es"),
                {"d": beim("m2", "einzigen")}),
    *markertext([[("öffentlichen Belang ", 0), ("beeinträchtigt.", "e")]], 750, 665, 42, beim("m2", "öffentlichen"),
                {"e": beim("m2", "beeinträchtigt")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
