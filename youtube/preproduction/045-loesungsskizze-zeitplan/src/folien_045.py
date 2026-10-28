"""Folge 045 · Lösungsskizze Klausur: Zeitplan für die 5-Stunden-Examensklausur – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Klausursaal 9 Uhr, B Klausursaal 12 Uhr und Frage, C Sachverhalt, D Bearbeitungszeit
(Wortlautkarte § 13 Abs. 1 S. 1 JAG NRW), E Zeitraster (Tortendiagramm, progressiv), F 1. Sachverhalt, G 2. Fallfrage,
H 3. Lösungsskizze, I 3. Gewichtung, J 4. Niederschrift / 5. Puffer, K Zeitnot (Jakob), L Klausurtipp (Lexi, Zeitleiste),
M Klausurschema (Zeitplan mit Zeitleiste), N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Aufgabenblatt landet auf dem Tisch (Szene A), Jakob schreibt los (Szene A)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import El
from PIL import ImageDraw
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_045/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 246, 233, 255)
GRAU = (215, 215, 220, 255)
HOLZ = (214, 160, 110, 255)
DAUER = bausteine._cj()["dauer"]

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


def pl(text, *a, rechts=None, **k):
    e = pille(glyphen(text), *a, **k)
    if rechts:
        assert e.x + e.sprite.width <= rechts, f"Pille zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, *_ in zeilen:
        glyphen(t)
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (recht.nrw.de) in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 22, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hart(e):
    e.anim = "cut"
    return e


# --- Eigene Hilfsfunktion (wie Folge 039): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------------
import wave as _wave
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


# --- Eigene Hilfsfunktion: Tortenstück für das Zeitraster (300 Minuten = Vollkreis, Start oben, im Uhrzeigersinn) -------
def torte(cx, cy, r, m0, m1, fill, cue, gesamt=300, rand=5, bis=None):
    s = 3
    R = r * s; pad = rand * s * 2
    im = Image.new("RGBA", (2 * R + 2 * pad, 2 * R + 2 * pad))
    dr = ImageDraw.Draw(im)
    a0, a1 = -90 + 360 * m0 / gesamt, -90 + 360 * m1 / gesamt
    dr.pieslice([pad, pad, pad + 2 * R, pad + 2 * R], a0, a1, fill=fill, outline=INK, width=rand * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - r - 2 * rand, cy - r - 2 * rand, cue, "pop", 0.0, bis, name="torte")


def torte_punkt(cx, cy, r, m, f=0.62, gesamt=300):
    """Punkt im Tortenstück bei Minute m (für Beschriftungen)."""
    a = math.radians(-90 + 360 * m / gesamt)
    return cx + r * f * math.cos(a), cy + r * f * math.sin(a)


import math
BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel
FARBEN_T = [GELB, BLAU, LILA, GRUEN, ROT]   # Sachverhalt, Fallfrage, Skizze, Niederschrift, Puffer
MINUTEN = [30, 10, 60, 180, 20]

# A/B Klausursaal --------------------------------------------------------------------------------------------------------
JOX, JAX, AUX, UHRX = 520, 1060, 1600, 790


def saal(cue, uhr):
    """Klausursaal: Boden, zwei Tische, Wanduhr (Grundbild ab cue)."""
    tisch_jo = ficon("tabler", "desk", JOX, BODEN - 2, 330, cue, fuell=HOLZ, anim="cut")
    tisch_ja = ficon("tabler", "desk", JAX, BODEN - 2, 330, cue, fuell=HOLZ, anim="cut")
    return ([linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
             pl("Im Klausursaal", 70, 40, cue, fill=GELB, size=40),
             ficon("tabler", uhr, UHRX, 210, 110, cue, fuell=WEISS)], tisch_jo, tisch_ja)


TOP = None
_els_a, TJO, TJA = saal("fall", "clock-hour-9")
TOP = TJO.y + 6                         # Tischplatte (Oberkante des Tisch-Icons)
AUa = ("AU_redet", AUX, BODEN, FH)
blatt_jo = szene(bewegt(ficon("tabler", "file-text", JOX - 60, TOP, 70, beim("aufgabe", "legt"), fuell=WEISS),
                        beim("aufgabe", "legt"), beim("aufgabe", "Aufgaben"), AUX - JOX + 60, -120), "045papier*", 1.0,
             versatz=round(bausteine._t(beim("aufgabe", "Aufgaben")) - bausteine._t(beim("aufgabe", "legt")) - 0.10, 3))
blatt_ja = bewegt(ficon("tabler", "file-text", JAX - 60, TOP, 70, beim("aufgabe", "legt"), fuell=WEISS),
                  beim("aufgabe", "legt"), beim("aufgabe", "Aufgaben"), AUX - JAX + 60, -120)
stift_ja = szene(ficon("tabler", "writing", JAX + 60, TOP, 80, "los", fuell=WEISS), "045stift*", 1.0, versatz=0.05)
folie([("fall", "Fall · Im Klausursaal, 9 Uhr")], [
    *_els_a,
    pl("9 Uhr", UHRX, 230, beim("fall", "Neun"), fill=WEISS, size=30, anker="m"),
    pl("Erster Examenstag: Zivilrecht", 70, 125, beim("fall", "Erster"), fill=WEISS, size=30),
    # Johanna
    peep_voll("JO_ruhig", JOX, BODEN, FH, "fall", bis="johanna"),
    peep_voll("JO_liest", JOX, BODEN, FH, "johanna", anim="cut"),
    # Jakob
    peep_voll("JA_ruhig", JAX, BODEN, FH, "fall", bis="jakob"),
    peep_voll("JA_cool", JAX, BODEN, FH, "jakob", anim="cut", bis="los"),
    peep_voll("JA_hektisch", JAX, BODEN, FH, "los", anim="cut"),
    # Aufsicht (blickt nach links zu den Tischen)
    peep_voll("AU_ruhig", AUX, BODEN, FH, "fall", bis="auf1"),
    *redet("AU_redet", AUX, BODEN, FH, "auf1", "jakob"),
    peep_voll("AU_ruhig", AUX, BODEN, FH, "jakob", anim="cut"),
    TJO, TJA,
    namensschild("Johanna", JOX, BODEN, "fall", BLAU),
    namensschild("Jakob", JAX, BODEN, "fall", GRUEN),
    namensschild("Aufsicht", AUX, BODEN, "fall", LILA),
    blatt_jo, blatt_ja,
    blase("sprech", 640, 210, "auf1", 1440, 210, inhalt=["Die Bearbeitungszeit beginnt jetzt.", "Sie haben fünf Stunden."],
          textsize=31, figur=AUa, bis="jakob"),
    pl("fünf Stunden", AUX, 330, beim("auf1", "fünf"), fill=GELB, size=30, anker="m", bis="jakob"),
    # Jakob blättert, schreibt los; Johanna liest und markiert
    pl("blättert kurz durch", JAX, 330, "jakob", fill=WEISS, size=28, anker="m", bis="los"),
    stift_ja,
    pl("schreibt sofort los", JAX, 330, "los", fill=ROT, size=28, anker="m", anim="cut"),
    pl("liest erst einmal", JOX, 330, "johanna", fill=WEISS, size=28, anker="m"),
    ficon("tabler", "highlight", JOX + 70, TOP, 70, "marker", fuell=GELB),
    pl("mit dem Textmarker", JOX + 40, TOP + 40, "marker", fill=GELB, size=28, anker="m"),
])

_els_b, TJOb, TJAb = saal("zwoelf", "clock-hour-12")
AUb = ("AU_redet", AUX, BODEN, FH)
JAb = ("JA_redet", JAX, BODEN, FH)
folie([("zwoelf", "Fall · 12 Uhr"), ("frage", "Fall · Die Frage")], [
    *_els_b,
    pl("12 Uhr", UHRX, 230, "zwoelf", fill=WEISS, size=30, anker="m"),
    peep_voll("JO_schreibt", JOX, BODEN, FH, "zwoelf", bis="frage"),
    peep_voll("JO_froh", JOX, BODEN, FH, "frage", anim="cut"),
    peep_voll("JA_hektisch", JAX, BODEN, FH, "zwoelf", bis="j1"),
    *redet("JA_redet", JAX, BODEN, FH, "j1", "seiten"),
    peep_voll("JA_hektisch", JAX, BODEN, FH, "seiten", anim="cut", bis="nochnicht"),
    peep_voll("JA_schreck", JAX, BODEN, FH, "nochnicht", anim="cut", bis="frage"),
    peep_voll("JA_muede", JAX, BODEN, FH, "frage", anim="cut"),
    peep_voll("AU_ruhig", AUX, BODEN, FH, "zwoelf", bis="auf2"),
    *redet("AU_redet", AUX, BODEN, FH, "auf2", "j1"),
    peep_voll("AU_ruhig", AUX, BODEN, FH, "j1", anim="cut"),
    TJOb, TJAb,
    namensschild("Johanna", JOX, BODEN, "zwoelf", BLAU),
    namensschild("Jakob", JAX, BODEN, "zwoelf", GRUEN),
    namensschild("Aufsicht", AUX, BODEN, "zwoelf", LILA),
    ficon("tabler", "writing", JAX + 60, TOP, 80, "zwoelf", fuell=WEISS),
    ficon("tabler", "highlight", JOX + 70, TOP, 70, "zwoelf", fuell=GELB),
    blase("sprech", 460, 180, "auf2", 1460, 220, inhalt=["Noch zwei Stunden."], textsize=36, figur=AUb, bis="j1"),
    blase("sprech", 640, 210, "j1", 1290, 210, inhalt=["Drei Stunden um, und ich", "bin erst bei der Hälfte!"],
          textsize=32, figur=JAb, bis="seiten"),
    ficon("tabler", "files", JAX - 70, TOP, 90, "seiten", fuell=WEISS),
    pl("viele Seiten", JAX, 330, beim("seiten", "Seiten"), fill=WEISS, size=28, anker="m", bis="nochnicht"),
    pl("Problem kommt erst noch", JAX, 330, "nochnicht", fill=ROT, size=28, anker="m", anim="cut", bis="frage"),
    pl("am Schwerpunkt", JOX, 330, beim("joh2", "Schwerpunkt"), fill=GELB, size=28, anker="m", bis="frage"),
    ficon("tabler", "list-check", JOX - 75, TOP, 70, "plan0", fuell=WEISS),
    pl("ihr Plan", JOX - 40, TOP + 40, "plan0", fill=WEISS, size=28, anker="m", bis="frage"),
    pl("Was hat Johanna anders gemacht?", 70, 125, "frage", fill=PINK, size=32),
    pl("Zeitplan und Lösungsskizze", 70, 205, beim("frage2", "Zeitplan"), fill=GELB, size=32),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Erster Examenstag, Klausur im Zivilrecht von 9 bis 14 Uhr. Die Aufsicht: „Die Bearbeitungszeit beginnt "
            "jetzt. Sie haben fünf Stunden.“ Jakob blättert kurz durch den Sachverhalt und schreibt sofort los. Johanna "
            "liest erst einmal, mit dem Textmarker in der Hand."),
    glyphen("Um 12 Uhr ist Jakob erst bei der Hälfte; das Problem des Falls kommt erst noch. Johanna schreibt nach "
            "ihrem Plan schon am Schwerpunkt."),
], "Wie teilst du die fünf Stunden ein?")

# D Bearbeitungszeit ------------------------------------------------------------------------------------------------------------
folie([("land", "Bearbeitungszeit › Landesrecht"), ("nrw", "Bearbeitungszeit › Beispiel: § 13 Abs. 1 JAG NRW"),
       ("regel", "Bearbeitungszeit › in der Regel fünf Stunden")], rechts_frei([
    *tafel("land", "Wie lange dauert die Klausur?"),
    z("Das regelt das Landesrecht:", 110, 190, beim("land", "regelt"), "Bold", 36),
    z("Ausbildungsgesetz oder Prüfungsordnung", 150, 245, beim("land", "Ausbildungsgesetz"), size=34),
    z("§ 5d Abs. 6 S. 1 DRiG", 150, 295, beim("land", "Ausbildungsgesetz"), size=26, farbe=TEXT),
    z("Beispiel Nordrhein-Westfalen:", 110, 370, beim("nrw", "Nordrhein"), "Bold", 34),
    *wortlaut(110, 425, 1040, 150, beim("nrw", "Nordrhein"), [
        [("„Für jede ", 0), ("Aufsichtsarbeit", "a"), (" in der staatlichen Pflichtfachprüfung", 0)],
        [("stehen dem Prüfling an je einem Tag ", 0), ("fünf Stunden", "b")],
        [("zur Verfügung.“", 0)],
    ], 30, {"a": beim("nrw", "Aufsichtsarbeit"), "b": beim("nrw", "fünf")}, "§ 13 Abs. 1 S. 1 JAG NRW"),
    fb(110, 660, 1040, 90, GELB, "regel", [("In der Regel: fünf Stunden", "ExtraBold", 36, INK)]),
    z("Was für dich gilt: eigene Prüfungsordnung prüfen", 110, 790, "eigen", "Bold", 34),
    peep_voll("JO_denkt", X1, BR, FR, "land", bis="eigen"),
    peep_voll("JO_froh", X1, BR, FR, "eigen", anim="cut"),
    peep_voll("AU_ruhig", X2, BR, FR, "land", d=0.2),
    namensschild("Johanna", X1, BR, "land", BLAU, d=0.2),
    namensschild("Aufsicht", X2, BR, "land", LILA, d=0.3),
    ficon("tabler", "map-pin", MB, 380, 80, "land", fuell=ROT, bis="nrw"),
    pl("Landesrecht", MB, 160, "land", fill=WEISS, size=30, anker="m", bis="nrw"),
    ficon("tabler", "book", MB, 380, 100, beim("nrw", "Nordrhein"), fuell=BLAU, anim="cut", bis="regel"),
    pl("Nordrhein-Westfalen", MB, 160, beim("nrw", "Nordrhein"), fill=WEISS, size=28, anker="m", anim="cut", bis="regel"),
    ficon("tabler", "hourglass", MB, 380, 90, "regel", fuell=GELB, anim="cut", bis="eigen"),
    pl("fünf Stunden", MB, 160, "regel", fill=GELB, size=30, anker="m", anim="cut", bis="eigen"),
    ficon("tabler", "book-2", MB, 380, 100, "eigen", fuell=GRUEN, anim="cut"),
    pl("deine Prüfungsordnung", MB, 160, "eigen", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# E Zeitraster (Tortendiagramm, Stück für Stück) ----------------------------------------------------------------------------
TCX, TCY, TR = 340, 520, 215
LX0 = 620
stuecke, legende = [], []
m = 0
TEXTE = [("30 Min.", "Lesen und markieren"), ("10 Min.", "Fallfrage"), ("60 Min.", "Lösungsskizze"),
         ("180 Min.", "Niederschrift"), ("20 Min.", "Puffer")]
for i, (mi, fa, (zahl, was), c) in enumerate(zip(MINUTEN, FARBEN_T, TEXTE, ["t1", "t2", "t3", "t4", "t5"])):
    stuecke.append(torte(TCX, TCY, TR, m, m + mi, fa, c))
    y = 250 + i * 60
    legende += [fb(LX0, y + 4, 36, 36, fa, c, [("", "Bold", 20, INK)], rund=8, rand=4),
                z(zahl, LX0 + 52, y, c, "ExtraBold", 30),
                z(was, LX0 + 190, y, c, size=30)]
    m += mi
p13 = torte_punkt(TCX, TCY, TR, 50, 0.6)
p23 = torte_punkt(TCX, TCY, TR, 200, 0.55)
folie([("raster", "Zeitplan › Empfehlung aus Erfahrung"), ("drittel", "Zeitplan › ein Drittel planen, zwei Drittel schreiben"),
       ("zweit", "Zeitplan › im zweiten Examen")], rechts_frei([
    *tafel("raster", "Zeitplan: fünf Stunden", size=46),
    pl("Empfehlung aus Erfahrung, keine Pflicht", 110, 175, beim("raster", "Empfehlung"), fill=PINK, size=26, rechts=1170),
    *stuecke, *legende,
    pl("ein Drittel", int(p13[0]), int(p13[1]) - 25, "drittel", fill=WEISS, size=28, anker="m"),
    pl("zwei Drittel", int(p23[0]), int(p23[1]) - 25, beim("drittel", "zwei"), fill=WEISS, size=28, anker="m"),
    z("ein Drittel planen,", LX0, 565, "drittel", "Bold", 30),
    z("zwei Drittel schreiben", LX0, 605, beim("drittel", "zwei"), "Bold", 30),
    z("(den Puffer eingeschlossen)", LX0, 648, beim("drittel", "Puffer"), size=28, farbe=TEXT),
    z("Das Verhältnis zählt,", LX0, 700, "verh", "Bold", 30),
    z("nicht die Minute.", LX0, 740, beim("verh", "nicht"), "Bold", 30),
    fb(110, 795, 1040, 85, LILAHELL, "zweit", [("2. Examen: meist eine Akte statt eines Sachverhalts, mehr Lesezeit", "Bold", 28, INK)]),
    peep_voll("JO_denkt", XS, BR, FR, "raster", bis="drittel"),
    peep_voll("JO_froh", XS, BR, FR, "drittel", anim="cut", bis="zweit"),
    peep_voll("JO_liest", XS, BR, FR, "zweit", anim="cut"),
    namensschild("Johanna", XS, BR, "raster", BLAU, d=0.2),
    ficon("tabler", "clock", XS, 380, 100, "raster", fuell=WEISS, bis="zweit"),
    ficon("tabler", "folders", XS, 380, 110, "zweit", fuell=GELB, anim="cut"),
    pl("Akte", XS, 160, "zweit", fill=WEISS, size=30, anker="m"),
]))

# F 1. Sachverhalt lesen und markieren -----------------------------------------------------------------------------------------
folie([("s1", "1. Sachverhalt lesen und markieren"), ("ansicht", "1. Sachverhalt › Rechtsansichten der Beteiligten")], rechts_frei([
    *tafel("s1", "1. Sachverhalt lesen und markieren", size=46),
    z("zweimal lesen", 110, 190, beim("s1", "zweimal"), "Bold", 38),
    z("das erste Mal ohne Stift", 150, 248, beim("s1", "ohne"), size=34),
    z("beim zweiten Lesen markieren:", 110, 330, "mark", "Bold", 36),
    pl("Personen", 150, 390, beim("mark", "Personen"), fill=GELB, size=32),
    pl("Daten", 380, 390, beim("mark", "Daten"), fill=BLAU, size=32),
    pl("Geldbeträge", 560, 390, beim("mark", "Geldbeträge"), fill=GRUEN, size=32),
    z("Rechtsansichten der Beteiligten", 110, 500, "ansicht", "Bold", 36),
    z("zeigen oft, wo die Probleme liegen", 150, 556, beim("ansicht", "zeigen"), size=34),
    fb(110, 660, 1040, 110, HELL, "angabe", [("Fast jede Angabe brauchst du in der Lösung.", "ExtraBold", 34, INK)]),
    peep_voll("JO_liest", XS, BR, FR, "s1", bis="ansicht"),
    peep_voll("JO_denkt", XS, BR, FR, "ansicht", anim="cut", bis="angabe"),
    peep_voll("JO_froh", XS, BR, FR, "angabe", anim="cut"),
    namensschild("Johanna", XS, BR, "s1", BLAU, d=0.2),
    ficon("tabler", "file-text", XS, 380, 90, "s1", fuell=WEISS, bis="mark"),
    pl("zweimal lesen", XS, 160, beim("s1", "zweimal"), fill=WEISS, size=30, anker="m", bis="mark"),
    ficon("tabler", "highlight", XS, 380, 90, "mark", fuell=GELB, anim="cut", bis="ansicht"),
    pl("markieren", XS, 160, "mark", fill=GELB, size=30, anker="m", anim="cut", bis="ansicht"),
    ficon("tabler", "message-2", XS, 380, 100, "ansicht", fuell=WEISS, anim="cut", bis="angabe"),
    pl("Rechtsansichten", XS, 160, "ansicht", fill=WEISS, size=30, anker="m", anim="cut", bis="angabe"),
    ficon("tabler", "list-check", XS, 380, 100, "angabe", fuell=WEISS, anim="cut"),
    pl("fast jede Angabe", XS, 160, "angabe", fill=HELL, size=30, anker="m", anim="cut"),
]))

# G 2. Fallfrage und Bearbeitervermerk -------------------------------------------------------------------------------------------
folie([("s2", "2. Fallfrage und Bearbeitervermerk"), ("aufbau", "2. Fallfrage › der Aufbau folgt der Frage")], rechts_frei([
    *tafel("s2", "2. Fallfrage und Bearbeitervermerk", size=46),
    z("Wer will was von wem?", 110, 200, "wer", "Bold", 40),
    z("Was sollst du ausdrücklich nicht prüfen?", 110, 290, "nicht", "Bold", 36),
    z("Der Aufbau folgt der Frage:", 110, 400, "aufbau", "Bold", 36),
    fb(110, 470, 300, 130, GELB, beim("aufbau", "Ansprüchen"), [("Ansprüche", "ExtraBold", 32, INK)]),
    fb(440, 470, 300, 130, ROTHELL, beim("aufbau", "Strafbarkeit"), [("Strafbarkeit", "ExtraBold", 32, INK)]),
    fb(770, 470, 380, 130, BLAU, beim("aufbau", "Erfolgsaussichten"),
       [("Erfolgsaussichten", "ExtraBold", 30, INK), ("einer Klage", "Bold", 28, INK)]),
    z("jeweils ein anderer Aufbau", 110, 650, beim("aufbau", "Klage"), size=34, farbe=TEXT),
    peep_voll("JO_liest", XS, BR, FR, "s2", bis="nicht"),
    peep_voll("JO_denkt", XS, BR, FR, "nicht", anim="cut", bis="aufbau"),
    peep_voll("JO_ruhig", XS, BR, FR, "aufbau", anim="cut"),
    namensschild("Johanna", XS, BR, "s2", BLAU, d=0.2),
    ficon("tabler", "file-description", XS, 380, 90, "s2", fuell=WEISS, bis="wer"),
    pl("Bearbeitervermerk", XS, 160, beim("s2", "Bearbeitervermerk"), fill=WEISS, size=30, anker="m", bis="wer"),
    ficon("tabler", "zoom-question", XS, 380, 100, "wer", fuell=GELB, anim="cut", bis="nicht"),
    pl("Wer will was?", XS, 160, "wer", fill=GELB, size=30, anker="m", anim="cut", bis="nicht"),
    ficon("tabler", "hand-stop", XS, 380, 100, "nicht", fuell=ROTHELL, anim="cut", bis="aufbau"),
    pl("nicht prüfen", XS, 160, "nicht", fill=ROTHELL, size=30, anker="m", anim="cut", bis="aufbau"),
    ficon("tabler", "list-numbers", XS, 380, 100, "aufbau", fuell=WEISS, anim="cut"),
    pl("Aufbau", XS, 160, "aufbau", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# H 3. Lösungsskizze: sammeln, Probleme, Schwerpunkt, Stichworte ------------------------------------------------------------
p_v = pl("aus Vertrag", 150, 255, beim("sammeln", "Vertrag"), fill=BLAU, size=30)
p_d = pl("aus Delikt", p_v.x + p_v.sprite.width + 30, 255, beim("sammeln", "Delikt"), fill=GELB, size=30)
p_b = pl("aus Bereicherung", p_d.x + p_d.sprite.width + 30, 255, beim("sammeln", "Bereicherung"), fill=GRUEN, size=30,
         rechts=1170)
DCX, DCY = p_d.x + p_d.sprite.width // 2, p_d.y + p_d.sprite.height // 2
p_s = pl("Schwerpunkt", DCX, 335, "schwer", fill=PINK, size=26, anker="m")
folie([("s3", "3. Lösungsskizze › Anspruchsgrundlagen sammeln"), ("probl", "3. Lösungsskizze › Probleme markieren"),
       ("schwer", "3. Lösungsskizze › Schwerpunkt setzen")], rechts_frei([
    *tafel("s3", "3. Lösungsskizze"),
    z("Anspruchsgrundlagen sammeln", 110, 190, "sammeln", "Bold", 38),
    p_v, p_d, p_b,
    z("Probleme markieren", 110, 410, "probl", "Bold", 38),
    ring(DCX, DCY, p_d.sprite.width // 2 + 22, p_d.sprite.height // 2 + 10, "probl", farbe=ORANGE, breite=6),
    p_s,
    z("Schwerpunkt: wo der Sachverhalt", 110, 490, "schwer", "Bold", 36),
    z("viele Einzelheiten liefert", 150, 545, beim("schwer", "viele"), "Bold", 36),
    fb(110, 650, 1040, 130, HELL, "stich", [("Stichworte, aber mit Ergebnis und Argument", "ExtraBold", 32, INK),
                                          ("beim Schreiben nicht neu nachdenken", "Bold", 30, INK)]),
    peep_voll("JO_denkt", XS, BR, FR, "s3", bis="sammeln"),
    peep_voll("JO_schreibt", XS, BR, FR, "sammeln", anim="cut", bis="schwer"),
    peep_voll("JO_denkt", XS, BR, FR, "schwer", anim="cut", bis="stich"),
    peep_voll("JO_froh", XS, BR, FR, "stich", anim="cut"),
    namensschild("Johanna", XS, BR, "s3", BLAU, d=0.2),
    ficon("tabler", "list", XS, 380, 100, "sammeln", fuell=WEISS, bis="probl"),
    pl("sammeln", XS, 160, "sammeln", fill=WEISS, size=30, anker="m", bis="probl"),
    ficon("tabler", "alert-triangle", XS, 380, 100, "probl", fuell=GELB, anim="cut", bis="schwer"),
    pl("Probleme", XS, 160, "probl", fill=GELB, size=30, anker="m", anim="cut", bis="schwer"),
    ficon("tabler", "star", XS, 380, 100, "schwer", fuell=PINK, anim="cut", bis="stich"),
    pl("Schwerpunkt", XS, 160, "schwer", fill=PINK, size=30, anker="m", anim="cut", bis="stich"),
    ficon("tabler", "notes", XS, 380, 100, "stich", fuell=WEISS, anim="cut"),
    pl("Stichworte", XS, 160, "stich", fill=HELL, size=30, anker="m", anim="cut"),
]))

# I 3. Lösungsskizze: Gewichtung, Urteilsstil, Skizze von Johanna ---------------------------------------------------------
folie([("gewicht", "3. Lösungsskizze › Gewichtung"), ("urteil", "3. Lösungsskizze › Unproblematisches im Urteilsstil"),
       ("jo3", "3. Lösungsskizze › die Skizze von Johanna")], rechts_frei([
    *tafel("gewicht", "3. Lösungsskizze: Gewichtung"),
    z("Jedem Punkt eine Zeit", 110, 190, "gewicht", "Bold", 38),
    z("Schwerpunkt: ausführlich", 150, 250, beim("gewicht", "Schwerpunkt"), size=34),
    z("Unproblematisches: Urteilsstil, ein Satz", 150, 305, "urteil", size=34),
    z("Johanna: drei Anspruchsgrundlagen", 110, 400, "jo3", "Bold", 36),
    fb(110, 460, 330, 100, GRAU, "jo3", [("1", "ExtraBold", 34, INK)], bis="jo4"),
    fb(460, 460, 330, 100, GRAU, beim("jo3", "drei"), [("2", "ExtraBold", 34, INK)], bis="jo4"),
    fb(810, 460, 330, 100, GRAU, beim("jo3", "Anspruchsgrundlagen"), [("3", "ExtraBold", 34, INK)], bis="jo4"),
    hart(fb(110, 460, 260, 100, GRUENHELL, "jo4", [("1: schnell erledigt", "Bold", 26, INK)])),
    hart(fb(880, 460, 260, 100, GRUENHELL, "jo4", [("3: schnell erledigt", "Bold", 26, INK)])),
    hart(fb(390, 460, 470, 100, GELB, beim("jo4", "eine"), [("2: trägt das Problem", "ExtraBold", 30, INK)])),
    pl("90 Minuten der Niederschrift", 390, 600, beim("jo5", "neunzig"), fill=PINK, size=30, rechts=1170),
    peep_voll("JO_denkt", XS, BR, FR, "gewicht", bis="jo3"),
    peep_voll("JO_schreibt", XS, BR, FR, "jo3", anim="cut", bis="jo5"),
    peep_voll("JO_froh", XS, BR, FR, "jo5", anim="cut"),
    namensschild("Johanna", XS, BR, "gewicht", BLAU, d=0.2),
    ficon("tabler", "clock", XS, 380, 100, "gewicht", fuell=WEISS, bis="urteil"),
    pl("eine Zeit je Punkt", XS, 160, "gewicht", fill=WEISS, size=28, anker="m", bis="urteil"),
    ficon("tabler", "gavel", XS, 380, 100, "urteil", fuell=HOLZ, anim="cut", bis="jo3"),
    pl("Urteilsstil", XS, 160, "urteil", fill=GRUENHELL, size=30, anker="m", anim="cut", bis="jo3"),
    ficon("tabler", "list-numbers", XS, 380, 100, "jo3", fuell=WEISS, anim="cut", bis="jo5"),
    pl("Skizze von Johanna", XS, 160, "jo3", fill=BLAU, size=28, anker="m", anim="cut", bis="jo5"),
    ficon("tabler", "hourglass", XS, 380, 90, "jo5", fuell=GELB, anim="cut"),
    pl("90 Minuten", XS, 160, "jo5", fill=PINK, size=30, anker="m", anim="cut"),
]))

# J 4. Niederschrift, 5. Puffer --------------------------------------------------------------------------------------------
folie([("s4", "4. Niederschrift"), ("s5", "5. Puffer")], rechts_frei([
    *tafel("s4", "4. Niederschrift · 5. Puffer"),
    z("4. Niederschrift", 110, 190, "s4", "Bold", 40),
    z("ausschreiben, was die Skizze vorgibt", 150, 250, beim("s4", "schreibst"), size=34),
    z("in ihrer Reihenfolge", 150, 305, beim("s4", "Reihenfolge"), size=34),
    z("5. Puffer", 110, 420, "s5", "Bold", 40),
    z("fängt Verzögerungen auf", 150, 480, "puffer", size=34),
    z("am Ende: Ergebnisse noch einmal lesen", 150, 535, beim("puffer", "Ende"), size=34),
    peep_voll("JO_schreibt", XS, BR, FR, "s4", bis="s5"),
    peep_voll("JO_ruhig", XS, BR, FR, "s5", anim="cut", bis=beim("puffer", "Ende")),
    peep_voll("JO_froh", XS, BR, FR, beim("puffer", "Ende"), anim="cut"),
    namensschild("Johanna", XS, BR, "s4", BLAU, d=0.2),
    ficon("tabler", "writing", XS, 380, 100, "s4", fuell=WEISS, bis="s5"),
    pl("Niederschrift", XS, 160, "s4", fill=GRUEN, size=30, anker="m", bis="s5"),
    ficon("tabler", "hourglass", XS, 380, 90, "s5", fuell=ROT, anim="cut", bis=beim("puffer", "Ende")),
    pl("Puffer", XS, 160, "s5", fill=ROT, size=30, anker="m", anim="cut", bis=beim("puffer", "Ende")),
    ficon("tabler", "eye", XS, 380, 100, beim("puffer", "Ende"), fuell=WEISS, anim="cut"),
    pl("noch einmal lesen", XS, 160, beim("puffer", "Ende"), fill=WEISS, size=30, anker="m", anim="cut"),
]))

# K Zeitnot (Jakob) ----------------------------------------------------------------------------------------------------------
JAk = ("JA_plan", XS, BR, FR)
folie([("fehler", "Zeitnot › Jakob ohne Skizze"), ("not1", "Zeitnot › Schwerpunkte zuerst"),
       ("not3", "Zeitnot › nie leer abgeben")], rechts_frei([
    *tafel("fehler", "Wenn die Zeit knapp wird"),
    z("Jakob: alles gleich ausführlich", 110, 190, beim("fehler", "Er"), "Bold", 36),
    z("ohne Skizze: wo liegt das Problem?", 150, 245, beim("fehler", "Ohne"), size=34),
    nein(1110, 210, beim("fehler", "ausführlich"), gr=20),
    z("1. zuerst die Schwerpunkte ausformulieren", 110, 340, "not1", "Bold", 36),
    z("2. den Rest knapp im Urteilsstil", 110, 400, "not2", "Bold", 36),
    z("3. die Gliederung bleibt vollständig", 110, 460, "glied", "Bold", 36),
    z("der Korrektor sieht: Du kennst den Aufbau.", 150, 515, beim("glied", "Korrektor"), size=32, farbe=TEXT),
    fb(110, 620, 1040, 130, ROTHELL, "not3", [("Nie leer abgeben:", "ExtraBold", 36, INK),
                                             ("jede Frage bekommt wenigstens ein Ergebnis", "Bold", 32, INK)]),
    peep_voll("JA_muede", XS, BR, FR, "fehler", bis="not1"),
    peep_voll("JA_ruhig", XS, BR, FR, "not1", anim="cut", bis="j2"),
    *redet("JA_plan", XS, BR, FR, "j2", "not3"),
    peep_voll("JA_hektisch", XS, BR, FR, "not3", anim="cut"),
    namensschild("Jakob", XS, BR, "fehler", GRUEN, d=0.2),
    ficon("tabler", "files", XS, 380, 100, "fehler", fuell=WEISS, bis="not"),
    pl("ohne Skizze", XS, 160, beim("fehler", "Ohne"), fill=ROTHELL, size=30, anker="m", bis="not"),
    ficon("tabler", "alarm", XS, 380, 100, "not", fuell=ROT, anim="cut", bis="j2"),
    pl("Zeit knapp", XS, 160, "not", fill=ROT, size=30, anker="m", anim="cut", bis="j2"),
    blase("sprech", 560, 200, "j2", 1560, 210, inhalt=["Also erst das Problem.", "Der Rest kommt kurz."], textsize=32,
          figur=JAk, bis="not3"),
    ficon("tabler", "writing", XS, 380, 100, "not3", fuell=WEISS, anim="cut"),
    pl("abgeben", XS, 160, "not3", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# L Klausurtipp (Lexi) mit Zeitleiste --------------------------------------------------------------------------------------
LXX = 1560
ZL0, ZL1, ZLY = 150, 1100, 430
px = lambda minute: ZL0 + (ZL1 - ZL0) * minute / 300
folie([("tipp", "Klausurtipp · Uhrzeiten an die Skizze")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Uhrzeiten an die Skizze, nicht nur Minuten", 200, 200, beim("tipp", "Schreib"), "Bold", 36),
    linienzug([(ZL0, ZLY), (ZL1, ZLY)], "tipp2", breite=8, farbe=INK),
    linienzug([(ZL0, ZLY - 22), (ZL0, ZLY + 22)], "tipp2", breite=6, farbe=INK),
    linienzug([(ZL1, ZLY - 22), (ZL1, ZLY + 22)], "tipp2", breite=6, farbe=INK),
    fb(int(px(0)), ZLY - 40, int(px(100) - px(0)), 30, LILA, beim("tipp2", "Skizze"), [("", "Bold", 20, INK)], rund=8, rand=4),
    linienzug([(px(100), ZLY - 30), (px(100), ZLY + 30)], beim("tipp2", "Skizze"), breite=7, farbe=DROT),
    fb(int(px(100)), ZLY - 40, int(px(280) - px(100)), 30, GRUEN, beim("tipp2", "Niederschrift"), [("", "Bold", 20, INK)],
       rund=8, rand=4),
    linienzug([(px(280), ZLY - 30), (px(280), ZLY + 30)], beim("tipp2", "Niederschrift"), breite=7, farbe=DROT),
    z("Skizze fertig: 10:40 Uhr", 200, 490, beim("tipp2", "zehn"), "Bold", 34),
    z("Niederschrift fertig: 13:40 Uhr", 200, 550, beim("tipp2", "dreizehn"), "Bold", 34),
    z("So merkst du sofort, wenn du", 200, 660, "tipp3", size=34),
    z("hinter deinem Plan liegst.", 200, 712, "tipp3", size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema: Zeitplan --------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
SL0, SLW, SLY = 160, 1600, 690
folie([("sch", "Klausurschema · Zeitplan")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Zeitplan für die Fünf-Stunden-Klausur"), 110, 90, "sch", 50),
    z("I. Sachverhalt lesen und markieren · etwa 30 Min.", K1, 200, "k1", "Bold", 36, rechts=1820),
    z("II. Fallfrage und Bearbeitervermerk · etwa 10 Min.", K1, 262, "k2", "Bold", 36, rechts=1820),
    z("III. Lösungsskizze · etwa 1 Std.", K1, 324, "k3", "Bold", 36, rechts=1820),
    z("Anspruchsgrundlagen · Probleme · Schwerpunkte", K2, 380, "k3a", size=32, farbe=TEXT, rechts=1820),
    z("IV. Niederschrift · etwa 3 Std.", K1, 442, "k4", "Bold", 36, rechts=1820),
    z("V. Puffer · etwa 20 Min.", K1, 504, "k5", "Bold", 36, rechts=1820),
    *[fb(int(SL0 + SLW * sum(MINUTEN[:i]) / 300), SLY, int(SLW * MINUTEN[i] / 300), 90, FARBEN_T[i], c,
         [(r_, "ExtraBold", 30 if i != 1 else 22, INK)], rund=10, rand=4)
      for i, (c, r_) in enumerate(zip(["k1", "k2", "k3", "k4", "k5"], ["I.", "II.", "III.", "IV.", "V."]))],
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Skizze verteilt", 0)], [("die ", 0), ("Zeit", "a"), (".", 0)]], 750, 320, 56, "merke",
                {"a": beim("merke", "Zeit")}),
    *markertext([[("Ausführlich nur am ", 0), ("Schwerpunkt", "b"), (",", 0)], [("abgegeben wird ", 0), ("immer", "c"), (".", 0)]],
                750, 590, 48, "m2", {"b": beim("m2", "Schwerpunkt"), "c": beim("m2", "immer")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
