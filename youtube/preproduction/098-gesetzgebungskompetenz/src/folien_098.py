"""Folge 098 · Gesetzgebungskompetenz: Bund oder Land? Art. 70 ff. GG – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Vorbild offengelegt: Berliner Mietendeckel, BVerfG 2 BvF 1/20): Ein Land beschließt eine Mietobergrenze von
9 €/m² für frei finanzierte Wohnungen; Vermieter Henke verlangt nach dem BGB die Zustimmung zur Erhöhung auf 10 €/m².
Szenen laut ../SZENENPLAN.md: A Landtag (Landesministerin stellt das Gesetz vor), B Wohnung von Frau Dahlke (Brief, Blasen,
Frage), C Sachverhalt, D Einordnung (formelle Verfassungsmäßigkeit), E 1. Grundsatz (Wortlaut Art. 70 I), F 2. ausschließliche
Gesetzgebung, G 3. a) Kompetenztitel, H Einwand Wohnungswesen und Art. 125a, I 3. b) Sperrwirkung (Wortlaut Art. 72 I),
J 3. c) Erforderlichkeitsklausel (Wortlaut Art. 72 II), K 3. d) Abweichungsrecht und 4. ungeschriebene Kompetenzen,
L Ergebnis (Frau Dahlke spricht), M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Ein Handlungsgeräusch: Frau Dahlke öffnet den Brief (Freesound CC0). Hilfsfunktionen wie Folgen 096/081 (eigene Kopie)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_098/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_098/" in n:
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



def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts (Kopie aus Folge 081)."""
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


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
X1, X2 = 1390, 1730                         # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
LM_F, DA_F, HE_F = LILA, BLAU, GRUEN        # Farben der Namensschilder
GK = "I. Gesetzgebungskompetenz"
MD = "BVerfG, Beschl. v. 25.3.2021 – 2 BvF 1/20"
AP = "BVerfG, Urt. v. 24.10.2002 – 2 BvF 1/01 (BVerfGE 106, 62)"


def boden(cue, hart_=False):
    e = linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


# A Fall: der Landtag beschließt die Mietobergrenze ----------------------------------------------------------------------------
LMX = 1300
LMa = ("LM_redet", LMX, BODEN, FH)
folie([(NULL, "Fall · Das neue Landesgesetz")], [
    boden(NULL, True),
    hart(pl("Landtag eines Landes", 70, 40, NULL, fill=LILA, size=40)),
    ficon("tabler", "building-bank", 330, BODEN - 2, 380, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "file-text", 650, 700, 100, beim("fall", "Gesetz"), fuell=WEISS),
    pl("neues Gesetz beschlossen", 650, 740, beim("fall", "beschlossen"), fill=GELB, size=30, anker="m"),
    ficon("tabler", "podium", 1080, BODEN - 2, 210, "lm", fuell=WEISS),
    *fig("LM", LMX, BODEN, FH, [("lm", "ruhig")], bis="lm1"),
    *redet("LM_redet", LMX, BODEN, FH, "lm1", "brief"),
    schild("Die Landesministerin", LMX, "lm", LM_F, unten=BODEN),
    blase("sprech", 820, 200, "lm1", 800, 210, inhalt=["Ab sofort darf die Miete für frei finanzierte",
                                                      "Wohnungen höchstens 9 € pro Quadratmeter",
                                                      "betragen."], textsize=30, figur=LMa),
])

# B Fall: der Brief des Vermieters ----------------------------------------------------------------------------------------------
DAX, HEX = 560, 1500
DAa = ("DA_redet_r", DAX, BODEN, FH)
HEa = ("HE_redet", HEX, BODEN, FH)
BH = hand("DA_liest_r", DAX, BODEN, FH, 1)
HERR = beim("brief", "Herrn")
folie([("brief", "Fall · Die Mieterhöhung"), ("frage", "Fall · Bund oder Land?")], [
    boden("brief"),
    pl("Eine Woche später: Wohnung von Frau Dahlke", 70, 40, "brief", fill=BLAU, size=36),
    ficon("tabler", "door", 210, BODEN - 2, 230, "brief", fuell=WEISS),
    *fig("DA", DAX, BODEN, FH, [("brief", "ruhig_r"), (beim("brief", "Post"), "liest_r"), ("erh", "sorge_r")], bis="da1"),
    *redet("DA_redet_r", DAX, BODEN, FH, "da1", "he1"),
    *fig("DA", DAX, BODEN, FH, [("he1", "denkt_r"), ("frage", "ruhig_r")], erst="cut"),
    schild("Frau Dahlke, Mieterin", DAX, "brief", DA_F, unten=BODEN, d=0.0),
    szene(ficon(HC, "envelope", BH[0] + 40, BH[1] + 30, 90, beim("brief", "Post"), fuell=WEISS), "098brief*", 0.8, 0.1),
    *fig("HE", HEX, BODEN, FH, [(HERR, "ruhig"), ("da1", "denkt")], bis="he1"),
    *redet("HE_redet", HEX, BODEN, FH, "he1", "frage"),
    *fig("HE", HEX, BODEN, FH, [("frage", "ruhig")], erst="cut"),
    schild("Herr Henke, Vermieter", HEX, HERR, HE_F, unten=BODEN),
    pl("bisher: 9 € pro Quadratmeter", 1030, 430, beim("bisher", "neun"), fill=WEISS, size=30, anker="m"),
    pl("BGB: Zustimmung zur Erhöhung auf 10 €", 1030, 505, beim("erh", "Erhöhung"), fill=GELB, size=30, anker="m"),
    pl("= ortsübliche Vergleichsmiete", 1030, 580, beim("erh", "ortsüblichen"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 620, 170, "da1", 760, 230, inhalt=["Mehr als 9 € verbietet doch", "das neue Landesgesetz!"],
          textsize=30, figur=DAa, bis="he1"),
    blase("sprech", 700, 200, "he1", 1180, 220, inhalt=["Die Miethöhe hat der Bund längst", "im BGB geregelt. Da hat das",
                                                       "Land nichts zu sagen."], textsize=30, figur=HEa, bis="frage"),
    blk(780, 175, 220, 76, GRUEN, beim("frage", "Durfte"), [("Bund?", "ExtraBold", 36, INK)]),
    blk(1060, 175, 220, 76, LILA, beim("frage", "Land"), [("Land?", "ExtraBold", 36, INK)]),
    pl("Vorbild: Berliner Mietendeckel, BVerfG 2021", 1030, 300, "vorbild", fill=PINK, size=30, anker="m"),
])

# C Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Der Landtag eines Landes beschließt ein Gesetz: Die Miete für frei finanzierte Wohnungen darf höchstens 9 € pro "
    "Quadratmeter betragen. Eine Woche später verlangt Herr Henke von seiner Mieterin Frau Dahlke, die bisher 9 € zahlt, "
    "nach dem BGB die Zustimmung zu einer Erhöhung auf 10 €, die ortsübliche Vergleichsmiete.",
    "Frau Dahlke: „Mehr als 9 € verbietet doch das neue Landesgesetz!“ Herr Henke: „Die Miethöhe hat der Bund längst im "
    "BGB geregelt. Da hat das Land nichts zu sagen.“",
], "Durfte das Land dieses Gesetz erlassen?")

# D Einordnung: formelle Verfassungsmäßigkeit ----------------------------------------------------------------------------------
FV = "Formelle Verfassungsmäßigkeit"
folie([("einord", f"{FV} des Landesgesetzes"), ("zust", f"{FV} › {GK}"), ("verw", f"{FV} › Exkurs: Weg nach Karlsruhe")],
      rechts_frei([
    *tafel("einord", "Wo gehört die Frage hin?"),
    z("formelle Verfassungsmäßigkeit des Landesgesetzes", 110, 185, beim("einord", "formelle"), "Bold", 34),
    blk(110, 260, 1040, 80, GELB, "zust", [("I. Zuständigkeit: Gesetzgebungskompetenz", "ExtraBold", 36, INK)]),
    z("II. Verfahren", 110, 370, beim("verf", "Verfahren"), "Bold", 36),
    z("III. Form", 110, 430, beim("verf", "Form"), "Bold", 36),
    pl("Wie kommt das Gesetz nach Karlsruhe?", 110, 545, "verw", fill=WEISS, size=30),
    z("z. B. abstrakte Normenkontrolle", 110, 620, beim("verw", "abstrakten"), size=34),
    zit("Art. 94 Abs. 1 Nr. 2 GG", 150, 668, beim("verw", "Normenkontrolle")),
    pl("Mehr dazu: Video Verfahrensarten des BVerfG", 110, 730, beim("verw", "Video"), fill=WEISS, size=30),
    ficon(HC, "classical-building", IX, IU, 150, "einord", fuell=WEISS),
    *fig("DA", FX, FB, FR, [("einord", "denkt"), ("verw", "ruhig")]),
    schild("Frau Dahlke", FX, "einord", DA_F),
]))

# E 1. Grundsatz, Wortlaut Art. 70 I ------------------------------------------------------------------------------------------
W70 = "„Die Länder haben das Recht der Gesetzgebung, soweit dieses Grundgesetz nicht dem Bunde Gesetzgebungsbefugnisse verleiht.“"
Z70 = ["„Die Länder haben das Recht der Gesetzgebung, soweit",
       "dieses Grundgesetz nicht dem Bunde",
       "Gesetzgebungsbefugnisse verleiht.“"]
w70, w70_y = wortlaut(80, 160, 1100, W70, "Art. 70 Abs. 1 GG", "wl70", size=36, zeilen=Z70,
                      marken=[("Die Länder", beim("wl70", "Länder")),
                              ("nicht dem Bunde", beim("wl70", "nicht"))])
folie([("wl70", f"{GK} › 1. Grundsatz, Art. 70 I GG")], rechts_frei([
    titel(glyphen("1. Grundsatz: die Länder"), 110, 70, "wl70", 46),
    *w70,
    z("Du fragst: Gibt das Grundgesetz dem Bund diese Materie?", 110, w70_y + 40, beim("frage70", "fragst"), "Bold", 34),
    blk(110, w70_y + 150, 1040, 80, BLAU, "voll", [("keine Doppelzuständigkeit", "ExtraBold", 36, INK)]),
    z("jede Materie: entweder Bund oder Länder", 150, w70_y + 250, beim("voll", "Jede"), size=34),
    zit(f"{MD}, Rn. 81", 150, w70_y + 305, beim("voll", "entweder")),
    ficon(HC, "puzzle-piece", IX, IU, 140, "wl70", fuell=WEISS),
    *fig("HE", FX, FB, FR, [("wl70", "denkt"), ("voll", "ruhig")]),
    schild("Herr Henke", FX, "wl70", HE_F),
]))

# F 2. ausschließliche Gesetzgebung -----------------------------------------------------------------------------------------------
folie([("aus", f"{GK} › 2. ausschließliche Gesetzgebung, Art. 71, 73 GG")], rechts_frei([
    *tafel("aus", "2. Ausschließliche Gesetzgebung des Bundes", size=42),
    z("Art. 71, 73 GG", 110, 175, beim("aus", "Artikel"), "Bold", 34),
    z("z. B. auswärtige Angelegenheiten, Art. 73 Abs. 1 Nr. 1", 150, 245, beim("aus", "auswärtige"), size=32),
    z("z. B. Waffenrecht, Art. 73 Abs. 1 Nr. 12", 150, 300, beim("aus", "Waffenrecht"), size=32),
    blk(110, 385, 1040, 134, GELB, "aus2", [("Länder nur, wenn ein Bundesgesetz", "ExtraBold", 34, INK),
                                             ("sie ausdrücklich ermächtigt, Art. 71 GG", "ExtraBold", 34, INK)]),
    *neinz("Miete: nicht in Art. 73 GG", 195, 580, "aus3", "Bold", 36),
    ficon("tabler", "world", IX, IU, 130, beim("aus", "auswärtige"), fuell=BLAU),
    *fig("DA", FX, FB, FR, [("aus", "ruhig"), ("aus3", "denkt")]),
    schild("Frau Dahlke", FX, "aus", DA_F),
]))

# G 3. a) Kompetenztitel ------------------------------------------------------------------------------------------------------------
KO = f"{GK} › 3. konkurrierende Gesetzgebung"
folie([("konk", f"{KO}, Art. 72, 74 GG"), ("ta", f"{KO} › a) Kompetenztitel"),
       ("nr1", f"{KO} › a) Kompetenztitel: Art. 74 I Nr. 1 GG")], rechts_frei([
    *tafel("konk", "3. Konkurrierende Gesetzgebung", size=44),
    z("Art. 72, 74 GG", 110, 170, beim("konk", "Artikel"), "Bold", 34),
    z("a) Kompetenztitel", 110, 240, "ta", "ExtraBold", 38),
    z("maßgeblich: was das Gesetz unmittelbar regelt,", 150, 305, beim("haupt", "unmittelbar"), size=32),
    z("Zweck und Wirkung, nicht die Bezeichnung", 150, 355, beim("haupt", "Zweck"), size=32),
    blk(150, 420, 1000, 76, BLAU, beim("haupt", "Hauptzweck"), [("entscheidend: der Hauptzweck", "ExtraBold", 34, INK)]),
    zit(f"{MD}, Rn. 104 f.", 150, 510, beim("haupt", "Hauptzweck", ende=True)),
    z("Mietobergrenze: Preis im Mietvertrag", 150, 590, beim("nr1", "Preis"), "Bold", 34),
    *okz("bürgerliches Recht, Art. 74 Abs. 1 Nr. 1 GG", 195, 660, beim("nr1", "bürgerliches"), "Bold", 34),
    zit(f"{MD}, Rn. 107 f.", 195, 715, beim("nr1", "Nummer")),
    ficon("tabler", "home-dollar", MB, 380, 130, "konk", fuell=GELB),
    pl("Mietobergrenze", MB, 180, beim("nr1", "Mietobergrenze"), fill=WEISS, size=30, anker="m"),
    *fig("DA", X1, FB, FR, [("konk", "ruhig"), ("nr1", "denkt")]),
    schild("Frau Dahlke", X1, "konk", DA_F),
    *fig("HE", X2, FB, FR, [("konk", "ruhig"), (beim("nr1", "bürgerliches"), "froh")], d=0.2),
    schild("Herr Henke", X2, "konk", HE_F, d=0.3),
]))

# H Einwand Wohnungswesen, Rechtsstand Art. 125a ----------------------------------------------------------------------------------
W125 = ("„Recht, das als Bundesrecht erlassen worden ist, aber wegen der Änderung des Artikels 74 Abs. 1 … nicht mehr als "
        "Bundesrecht erlassen werden könnte, gilt als Bundesrecht fort. Es kann durch Landesrecht ersetzt werden.“")
Z125 = ["„Recht, das als Bundesrecht erlassen worden ist, aber wegen der",
        "Änderung des Artikels 74 Abs. 1 … nicht mehr als Bundesrecht",
        "erlassen werden könnte, gilt als Bundesrecht fort.",
        "Es kann durch Landesrecht ersetzt werden.“"]
w125, w125_y = wortlaut(80, 470, 1100, W125, "Art. 125a Abs. 1 GG (Auszug)", "fort", size=30, zeilen=Z125,
                        marken=[("gilt als Bundesrecht fort.", beim("fort", "fort")),
                                ("durch Landesrecht ersetzt", beim("fort", "ersetzen"))])
folie([("wohn", f"{KO} › a) Einwand: Wohnungswesen"), ("fort", "Rechtsstand · Föderalismusreform 2006, Art. 125a I GG")],
      rechts_frei([
    *tafel("wohn", "Einwand des Landes: Wohnungswesen", size=42),
    z("Föderalismusreform 2006: Titel gestrichen,", 110, 175, beim("wohn", "Föderalismusreform"), "Bold", 32),
    z("seitdem Ländersache", 150, 225, beim("wohn", "Ländersache"), "Bold", 32),
    *neinz("Miethöhe auf dem freien Markt:", 195, 295, beim("wohn2", "Miethöhe"), "Bold", 32),
    z("schon vorher bürgerliches Recht", 195, 345, beim("wohn2", "bürgerlichen"), size=32),
    zit(f"{MD}, Rn. 178, 184 f.", 195, 395, beim("wohn2", "Bundesverfassungsgericht")),
    *w125,
    ficon("tabler", "building-bank", IX, IU, 140, "wohn", fuell=WEISS),
    pl("das Land", IX, 180, "wohn", fill=LILA, size=30, anker="m"),
    *fig("LM", FX, FB, FR, [("wohn", "entschlossen"), ("wohn2", "ruhig")]),
    schild("Die Landesministerin", FX, "wohn", LM_F),
]))

# I 3. b) Sperrwirkung, Wortlaut Art. 72 I ----------------------------------------------------------------------------------------
W72 = ("„Im Bereich der konkurrierenden Gesetzgebung haben die Länder die Befugnis zur Gesetzgebung, solange und soweit "
       "der Bund von seiner Gesetzgebungszuständigkeit nicht durch Gesetz Gebrauch gemacht hat.“")
Z72 = ["„Im Bereich der konkurrierenden Gesetzgebung haben die",
       "Länder die Befugnis zur Gesetzgebung, solange und soweit",
       "der Bund von seiner Gesetzgebungszuständigkeit nicht durch",
       "Gesetz Gebrauch gemacht hat.“"]
w72, w72_y = wortlaut(80, 150, 1100, W72, "Art. 72 Abs. 1 GG", "wl72", size=32, zeilen=Z72,
                      marken=[("solange und soweit", beim("wl72", "solange")),
                              ("Gebrauch gemacht hat.“", beim("wl72", "Gebrauch"))])
folie([("wl72", f"{KO} › b) Sperrwirkung, Art. 72 I GG")], rechts_frei([
    titel(glyphen("b) Sperrwirkung"), 110, 65, "wl72", 46),
    *w72,
    z("Gebrauch gemacht = abschließend geregelt", 110, w72_y + 30, "ab", "Bold", 34),
    *okz("§§ 556 bis 561 BGB:", 195, w72_y + 100, beim("bgb", "Paragrafen"), "Bold", 34),
    z("Vergleichsmiete und Mietpreisbremse", 195, w72_y + 150, beim("bgb", "Vergleichsmiete"), size=34),
    zit(f"{MD}, Rn. 148, 160", 195, w72_y + 200, beim("bgb", "Mietpreisbremse")),
    blk(110, w72_y + 265, 1040, 80, ROTHELL, "egal", [("Land gesperrt, ob sein Gesetz", "ExtraBold", 34, INK)]),
    z("widerspricht, ergänzt oder nur wiederholt", 150, w72_y + 360, beim("egal", "widerspricht"), size=34),
    zit(f"{MD}, Rn. 89", 150, w72_y + 410, beim("egal", "wiederholt")),
    ficon("tabler", "lock", MB, 380, 110, "egal", fuell=GELB),
    pl("gesperrt", MB, 180, beim("egal", "gesperrt"), fill=ROT, size=30, anker="m"),
    *fig("LM", X1, FB, FR, [("wl72", "ruhig"), ("egal", "entschlossen")]),
    schild("Landesministerin", X1, "wl72", LM_F),
    *fig("HE", X2, FB, FR, [("wl72", "ruhig"), ("bgb", "froh")], d=0.2),
    schild("Herr Henke", X2, "wl72", HE_F, d=0.3),
]))

# J 3. c) Erforderlichkeitsklausel, Wortlaut Art. 72 II ------------------------------------------------------------------------------
W722 = ("„Auf den Gebieten des Artikels 74 Abs. 1 Nr. 4, 7, 11, 13, 15, 19a, 20, 22, 25 und 26 hat der Bund das "
        "Gesetzgebungsrecht, wenn und soweit die Herstellung gleichwertiger Lebensverhältnisse im Bundesgebiet oder die "
        "Wahrung der Rechts- oder Wirtschaftseinheit im gesamtstaatlichen Interesse eine bundesgesetzliche Regelung "
        "erforderlich macht.“")
Z722 = ["„Auf den Gebieten des Artikels 74 Abs. 1",
        "Nr. 4, 7, 11, 13, 15, 19a, 20, 22, 25 und 26 hat der Bund das",
        "Gesetzgebungsrecht, wenn und soweit die Herstellung",
        "gleichwertiger Lebensverhältnisse im Bundesgebiet oder die",
        "Wahrung der Rechts- oder Wirtschaftseinheit im",
        "gesamtstaatlichen Interesse eine bundesgesetzliche Regelung",
        "erforderlich macht.“"]
w722, w722_y = wortlaut(80, 135, 1100, W722, "Art. 72 Abs. 2 GG", "wl722", size=30, zeilen=Z722,
                        marken=[("Nr. 4, 7, 11, 13, 15, 19a, 20, 22, 25 und 26", beim("liste", "aufgezählten")),
                                ("erforderlich macht.“", beim("liste", "erforderlich")),
                                ("gleichwertiger Lebensverhältnisse", beim("liste", "gleichwertige")),
                                ("Rechts- oder Wirtschaftseinheit", beim("liste", "Rechts-"))])
folie([("wl722", f"{KO} › c) Erforderlichkeitsklausel, Art. 72 II GG")], rechts_frei([
    titel(glyphen("c) Erforderlichkeitsklausel"), 110, 60, "wl722", 44),
    *w722,
    z("nicht genug: bloß bundeseinheitliche Regeln", 110, w722_y + 22, beim("streng", "Bundeseinheitliche"), "Bold", 32),
    z("Lebensverhältnisse erheblich auseinanderentwickelt", 110, w722_y + 72, beim("streng2", "Gleichwertige"), "Bold", 32),
    zit(f"{AP}, Rn. 320 f.", 110, w722_y + 120, beim("streng2", "auseinanderentwickeln")),
    *neinz("Art. 74 Abs. 1 Nr. 1: nicht in der Liste", 195, w722_y + 180, "n1", "Bold", 34),
    z("hier entfällt die Prüfung", 195, w722_y + 232, beim("n1", "entfällt"), size=34),
    zit(f"{MD}, Rn. 86", 195, w722_y + 280, beim("n1", "Prüfung")),
    *fig("HE", FX, FB, FR, [("wl722", "denkt"), ("n1", "ruhig")]),
    schild("Herr Henke", FX, "wl722", HE_F),
    ficon("tabler", "list-check", IX, IU, 120, "liste", fuell=WEISS),
]))

# K 3. d) Abweichungsrecht, 4. ungeschriebene Kompetenzen ------------------------------------------------------------------------------
folie([("abw", f"{KO} › d) Abweichungsrecht, Art. 72 III GG"), ("unge", f"{GK} › 4. ungeschriebene Kompetenzen")],
      rechts_frei([
    *tafel("abw", "d) Abweichungsrecht, Art. 72 Abs. 3 GG", size=42),
    z("nur in einigen Gebieten, z. B.", 110, 175, beim("abw", "einigen"), size=34),
    z("Jagdwesen,", 150, 230, beim("abw", "Jagdwesen"), "Bold", 34),
    z("Naturschutz,", 350, 230, beim("abw", "Naturschutz"), "Bold", 34),
    z("Grundsteuer", 580, 230, beim("abw", "Grundsteuer"), "Bold", 34),
    z("Länder dürfen vom Bundesgesetz abweichen", 110, 295, beim("abw", "abweichen"), size=34),
    z("das spätere Gesetz geht vor, Art. 72 Abs. 3 Satz 3 GG", 110, 350, beim("abw", "spätere"), size=32),
    *neinz("Mietrecht: nicht im Katalog", 195, 425, "abw2", "Bold", 34),
    blk(110, 520, 1040, 76, BLAU, "unge", [("4. ungeschriebene Kompetenzen", "ExtraBold", 36, INK)]),
    z("Sachzusammenhang, Annex, Natur der Sache", 150, 615, beim("unge", "Sachzusammenhangs"), size=34),
    z("hier nicht nötig: Titel steht ausdrücklich im GG", 150, 670, beim("unge", "ausdrücklich"), "Bold", 32),
    ficon("tabler", "deer", MB, 380, 120, beim("abw", "Jagdwesen"), fuell=GELB, bis="unge"),
    ficon("tabler", "trees", MB, 380, 120, "unge", fuell=GRUEN, anim="cut"),
    *fig("DA", X1, FB, FR, [("abw", "ruhig"), ("abw2", "denkt")]),
    schild("Frau Dahlke", X1, "abw", DA_F),
    *fig("LM", X2, FB, FR, [("abw", "ruhig"), ("abw2", "entschlossen")], d=0.2),
    schild("Landesministerin", X2, "abw", LM_F, d=0.3),
]))

# L Ergebnis -----------------------------------------------------------------------------------------------------------------------------
DAe = ("DA_redetfroh", X1, FB, FR)
folie([("erg", "Ergebnis · Landesgesetz nichtig")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *neinz("Dem Land fehlt die Gesetzgebungskompetenz.", 195, 185, beim("erg", "fehlt"), "Bold", 34),
    blk(110, 270, 1040, 134, ROTHELL, beim("erg", "Landesgesetz"),
        [("Das Landesgesetz ist formell", "ExtraBold", 36, INK), ("verfassungswidrig und nichtig.", "ExtraBold", 36, INK)]),
    z("Vorbild: Berliner Mietendeckel insgesamt nichtig", 110, 440, beim("erg2", "Mietendeckel"), "Bold", 32),
    zit(f"{MD}, Rn. 78, 186", 110, 490, beim("erg2", "nichtig")),
    *okz("Mieterhöhung: allein nach dem BGB", 195, 570, beim("erg3", "Mieterhöhung"), "Bold", 34),
    *fig("DA", X1, FB, FR, [("erg", "ruhig"), ("erg3", "froh")], bis="da2"),
    *redet("DA_redetfroh", X1, FB, FR, "da2", "tipp"),
    schild("Frau Dahlke", X1, "erg", DA_F),
    *fig("HE", X2, FB, FR, [("erg", "ruhig"), ("erg2", "froh")], d=0.2),
    schild("Herr Henke", X2, "erg", HE_F, d=0.3),
    blase("sprech", 620, 170, "da2", 1560, 230, inhalt=["Dann prüfe ich die Mieterhöhung", "eben nach dem BGB."],
          textsize=28, figur=DAe),
]))

# M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Erst die Kompetenz, nicht Art. 31 GG")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nicht vorschnell: Art. 31 GG", 200, 200, beim("tipp", "vorschnell"), "Bold", 38),
    z("„Bundesrecht bricht Landesrecht“", 200, 260, beim("tipp", "Bundesrecht"), size=34),
    blk(200, 345, 900, 76, BLAU, "tipp1", [("Zuerst die Kompetenz prüfen", "ExtraBold", 36, INK)]),
    z("fehlt sie: Landesgesetz schon deshalb nichtig", 200, 450, beim("tipp1", "Fehlt"), size=34),
    z("so das BVerfG, obwohl sich die Antragsteller", 200, 540, beim("tipp2", "So"), size=32),
    z("auch auf Art. 31 GG berufen hatten", 200, 590, beim("tipp2", "Antragsteller"), size=32),
    zit(f"{MD}, Rn. 27, 78, 87", 200, 645, beim("tipp2", "berufen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema -------------------------------------------------------------------------------------------------------------------------
SZ, LH = 32, 62
K1, K2 = 150, 230
schema = [("s1", K1, "1. Grundsatz: Länder, Art. 70 Abs. 1 GG", "Bold"),
          ("s2", K1, "2. ausschließliche Gesetzgebung des Bundes, Art. 71, 73 GG", "Bold"),
          ("s3", K1, "3. konkurrierende Gesetzgebung, Art. 72, 74 GG", "Bold"),
          ("s3a", K2, "a) Kompetenztitel aus Art. 74 GG", "Regular"),
          ("s3b", K2, "b) Sperrwirkung, Art. 72 Abs. 1 GG", "Regular"),
          ("s3c", K2, "c) Erforderlichkeit, Art. 72 Abs. 2 GG: nur bei den genannten Nummern", "Regular"),
          ("s3d", K2, "d) Abweichungsrecht, Art. 72 Abs. 3 GG", "Regular"),
          ("s4", K1, "4. ungeschriebene Kompetenzen", "Bold"),
          ("s5", K1, "5. Ergebnis", "Bold")]
els_s = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: Gesetzgebungskompetenz"), 110, 85, "sch", 46),
         z("I. Gesetzgebungskompetenz (formelle Verfassungsmäßigkeit)", 110, 175, "sch", "ExtraBold", 36, rechts=1820)]
for i, (c, x, t, s) in enumerate(schema):
    els_s.append(z(t, x, 245 + i * LH, c, s, SZ, rechts=1820))
els_s.append(blk(110, 245 + len(schema) * LH + 20, 1700, 76, HELL, "s6", [("danach: II. Verfahren, III. Form", "Bold", 34, INK)]))
folie([("sch", "Klausurschema · Gesetzgebungskompetenz")], els_s)

# O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gesetzgebung ist ", 0), ("Ländersache,", "a")]], 750, 310, 46, "merke", {"a": beim("merke", "Ländersache")}),
    *markertext([[("soweit das Grundgesetz", 0)]], 750, 375, 46, beim("merke", "soweit"), {}),
    *markertext([[("sie nicht dem ", 0), ("Bund", "b"), (" gibt.", 0)]], 750, 440, 46, beim("merke", "sie"),
                {"b": beim("merke", "Bund")}),
    *markertext([[("Im konkurrierenden Bereich sperrt", 0)]], 750, 575, 46, "m2", {}),
    *markertext([[("ein ", 0), ("abschließendes Bundesgesetz", "c")]], 750, 640, 46, beim("m2", "ein"),
                {"c": beim("m2", "abschließendes")}),
    *markertext([[("die Länder.", 0)]], 750, 705, 46, beim("m2", "Länder"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
