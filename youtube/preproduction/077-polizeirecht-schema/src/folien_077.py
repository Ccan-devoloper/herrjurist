"""Folge 077 · Polizeirecht Schema: Standardmaßnahme vor Generalklausel – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Geburtstag im Park (Nacht),
B Die Polizei kommt (Nacht), C Der Platzverweis (Nacht), D Frage, E Sachverhalt, F Aufbau und Landesrecht, G Ermächtigungs-
grundlage: Reihenfolge und Versammlungsrecht, H Generalklausel (Wortlaut § 8 I PolG NRW), I Warum Standardmaßnahme zuerst,
J Platzverweis (Wortlaut § 34 I 1 PolG NRW), K formell, L Tatbestand: konkrete Gefahr, M Lärm (Wortlaut § 117 I OWiG,
§ 9 I LImschG NRW), N Adressat, O Rechtsfolge: Ermessen und Verhältnismäßigkeit, P zeitlich und räumlich begrenzt,
Q Ergebnis und Rechtsschutz, R Klausurtipp (Lexi), S Klausurschema, T Merksatz (Lexi).
Nacht nur in den Fallszenen A–C (der Fall spielt in der Nachtruhe, § 9 LImschG NRW). Geräusch nur bei sichtbarer Handlung:
Autotür, wenn der Streifenwagen erscheint (Szenen B und C)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_077/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE, nacht=None)                 # Nacht = Verlauf, erzeugt im Renderer
PFAD_FARBE = dict(bausteine.PFAD_FARBE, nacht=(255, 255, 255, 170))
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
ZARTGRUEN = (236, 248, 236, 255)
LINIE = (225, 228, 240, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_077/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


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


# --- Eigene Hilfsfunktion (wie Folge 064/061/052): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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


BODEN, FH, SH = 880, 460, 300               # Boden der Fallszenen, Höhe stehend / sitzend
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
SR_F, GO_F, KR_F, FR_F = GRUEN, BLAU, LILA, WEISS   # Farben der Namensschilder
FAX, SRX, FBX, BOXX = 360, 640, 900, 1090   # Freundin, Herr Schröder, Freund, Musikbox
KRX, HX, PX, GOX = 1500, 1760, 1530, 1290   # Frau Krämer, Haus, Streifenwagen, Frau Götz
K1, K2, K3 = 150, 210, 270


def park(cue, anim="pop"):
    """Stadtpark bei Nacht: Boden, Mond, Bäume, Haus von Frau Krämer am Parkrand (nur Bibliotheks-Icons)."""
    a = dict(anim=anim)
    return [hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=LINIE)),
            ficon("tabler", "moon-stars", 1835, 170, 90, cue, fuell=GELB, **a),
            ficon("tabler", "trees", 150, BODEN, 230, cue, fuell=GRUEN, **a),
            ficon("ph", "building-apartment", HX, BODEN, 230, cue, fuell=BLAU, nebenfarbe=GELB, **a)]


def gruppe(c_froh, c_sorge=None, bis=None, sr=True, erst="pop"):
    """Herr Schröder (steht) mit Freundin und Freund (sitzen im Gras), dazu Namensschilder."""
    fa = [(c_froh, "froh_r")] + ([(c_sorge, "sorge_r")] if c_sorge else [])
    fb = [(c_froh, "froh")] + ([(c_sorge, "sorge")] if c_sorge else [])
    els = [*fig("FA", FAX, BODEN, SH, fa, bis=bis, erst=erst), schild("Freundin", FAX, c_froh, FR_F, unten=BODEN, bis=bis),
           *fig("FB", FBX, BODEN, SH - 20, fb, bis=bis, erst=erst), schild("Freund", FBX, c_froh, FR_F, unten=BODEN, bis=bis)]
    if sr:
        els.append(schild("Herr Schröder", SRX, c_froh, SR_F, unten=BODEN, bis=bis))
    return els


def box(cue, laut=True, bis=None, anim="pop", noten_bis=None):
    els = [ficon("ph", "speaker-hifi", BOXX, BODEN, 170, cue, fuell=LILA, anim=anim, bis=bis)]
    if laut:
        els += [ficon("tabler", "music", BOXX - 20, BODEN - 200, 70, cue, fuell=GELB, anim=anim, bis=noten_bis),
                ficon("tabler", "music", BOXX + 60, BODEN - 260, 56, cue, fuell=GELB, anim=anim, bis=noten_bis)]
    return els


def streifenwagen(cue, bis=None, ton=True):
    e = ficon("ph", "police-car", PX, BODEN, 300, cue, fuell=WEISS, nebenfarbe=BLAU, bis=bis)
    return szene(e, "077tuer*", 0.8, 0.25) if ton else e


# A Fall: Geburtstag im Park (Nacht) ------------------------------------------------------------------------------------------
SRa = ("SR_redet_r", SRX, BODEN, FH)
KRb = ("KR_redet", KRX, BODEN, FH - 20)
nachtfolie([(NULL, "Fall · Geburtstag im Park")], [
    *park(NULL, anim="cut"),
    hart(pl("Samstagnacht in Nordrhein-Westfalen", 70, 40, NULL, fill=GELB, size=40)),
    pl("Stadtpark", 150, 590, NULL, fill=WEISS, size=30, anker="m", anim="cut"),
    *fig("SR", SRX, BODEN, FH, [("gruppe", "froh_r")]),
    *gruppe("gruppe"),
    pl("Geburtstag", SRX, 330, beim("gruppe", "Geburtstag"), fill=PINK, size=30, anker="m"),
    ficon(HC, "birthday-cake", SRX + 140, 385, 52, beim("gruppe", "Geburtstag"), fuell=WEISS),
    *box("box"),
    pl("laut", BOXX - 15, 480, beim("box", "laut"), fill=ROT, size=30, anker="m"),
    pl("die 3 singen mit", 640, 260, beim("box", "singen"), fill=WEISS, size=28, anker="m"),
    *fig("KR", KRX, BODEN, FH - 20, [("kraemer", "sorge")], bis="kr1"),
    *redet("KR_redet", KRX, BODEN, FH - 20, "kr1", "goetz"),
    schild("Frau Krämer, Anwohnerin", KRX, "kraemer", KR_F, unten=BODEN),
    ficon(HC, "mobile-phone", KRX - 200, 620, 60, beim("kraemer", "ruft"), fuell=WEISS),
    pl("ruft die Polizei", KRX - 200, 500, beim("kraemer", "ruft"), fill=BLAU, size=28, anker="m"),
    pl("Mitternacht", 1470, 40, beim("kraemer", "Mitternacht"), fill=GELB, size=34),
    pl("wohnt direkt am Park", HX - 70, 380, beim("kraemer", "wohnt"), fill=WEISS, size=26, anker="m"),
    blase("sprech", 640, 210, "kr1", 1250, 250, inhalt=["Ich kann nicht schlafen. Die Musik", "dröhnt bis in mein Schlafzimmer."],
          textsize=30, figur=KRb),
])

# B Fall: Die Polizei kommt (Nacht) ---------------------------------------------------------------------------------------------
GOb = ("GO_redet", GOX, BODEN, FH)
SRb = ("SR_redet_r", SRX, BODEN, FH)
nachtfolie([("goetz", "Fall · Die Polizei kommt")], [
    *park("goetz"),
    pl("1 Stunde später", 70, 40, beim("wieder", "Stunde"), fill=GELB, size=40),
    *fig("SR", SRX, BODEN, FH, [("goetz", "froh_r")], bis="sch1"),
    *redet("SR_redet_r", SRX, BODEN, FH, "sch1", "wieder"),
    *fig("SR", SRX, BODEN, FH, [("wieder", "froh_r")], erst="cut"),
    *gruppe("goetz"),
    *box("goetz", noten_bis="sch1"),
    pl("leiser", BOXX + 20, 600, beim("sch1", "machen"), fill=GRUEN, size=30, anker="m", bis="laut"),
    ficon("tabler", "music", BOXX - 20, BODEN - 200, 70, "laut", fuell=GELB),
    ficon("tabler", "music", BOXX + 60, BODEN - 260, 56, "laut", fuell=GELB),
    ficon("tabler", "music", BOXX + 10, BODEN - 330, 64, beim("laut", "voll"), fuell=GELB),
    pl("wieder voll aufgedreht", BOXX + 20, 460, beim("laut", "aufgedreht"), fill=ROT, size=30, anker="m"),
    streifenwagen("goetz", bis="wieder"),
    *fig("GO", GOX, BODEN, FH, [("goetz", "ruhig")], bis="go1"),
    *redet("GO_redet", GOX, BODEN, FH, "go1", "sch1"),
    *fig("GO", GOX, BODEN, FH, [("sch1", "ruhig")], erst="cut", bis="wieder"),
    schild("Frau Götz, Polizei", GOX, "goetz", GO_F, unten=BODEN, bis="wieder"),
    *fig("KR", KRX, BODEN, FH - 20, [("wieder", "muede")]),
    schild("Frau Krämer, Anwohnerin", KRX, "wieder", KR_F, unten=BODEN),
    ficon(HC, "mobile-phone", KRX - 200, 620, 60, beim("wieder", "ruft"), fuell=WEISS),
    pl("ruft wieder an", KRX - 200, 500, beim("wieder", "ruft"), fill=BLAU, size=28, anker="m"),
    blase("sprech", 660, 200, "go1", 1180, 240, inhalt=["Bitte machen Sie die Musik leiser.", "Die Nachbarn wollen schlafen."],
          textsize=30, figur=GOb, bis="sch1"),
    blase("sprech", 420, 160, "sch1", 760, 250, inhalt=["Klar, machen wir."], textsize=32, figur=SRb, bis="wieder"),
])

# C Fall: Der Platzverweis (Nacht) ----------------------------------------------------------------------------------------------
GOc = ("GO_ernst_redet", GOX, BODEN, FH)
SRc = ("SR_fragt_r", SRX, BODEN, FH)
nachtfolie([("zurueck", "Fall · Der Platzverweis")], [
    *park("zurueck"),
    pl("1 Stunde später", 70, 40, "zurueck", fill=GELB, size=40),
    *fig("SR", SRX, BODEN, FH, [("zurueck", "denkt_r")], bis="sch2"),
    *redet("SR_fragt_r", SRX, BODEN, FH, "sch2", "frage"),
    *gruppe("zurueck", beim("go2", "verlassen")),
    *box("zurueck"),
    streifenwagen("zurueck"),
    *fig("GO", GOX, BODEN, FH, [("zurueck", "ernst")], bis="go2"),
    *redet("GO_ernst_redet", GOX, BODEN, FH, "go2", "sch2"),
    *fig("GO", GOX, BODEN, FH, [("sch2", "ernst")], erst="cut"),
    schild("Frau Götz, Polizei", GOX, "zurueck", GO_F, unten=BODEN),
    pl("Platzverweis: bis 6 Uhr", PX + 30, 560, beim("go2", "sechs"), fill=ROT, size=30, anker="m"),
    blase("sprech", 700, 200, "go2", 1170, 240, inhalt=["Sie verlassen jetzt bitte alle", "den Park, bis morgen früh um 6."],
          textsize=30, figur=GOc, bis="sch2"),
    blase("sprech", 620, 200, "sch2", 760, 240, inhalt=["Wir sitzen doch nur auf der Wiese.", "Auf welcher Grundlage eigentlich?"],
          textsize=30, figur=SRc),
])

# D Frage -----------------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · War der Platzverweis rechtmäßig?")], rechts_frei([
    pl("Platzverweis im Stadtpark, bis 6 Uhr", 640, 420, "frage", fill=WEISS, size=36, anker="m"),
    pl("War der Platzverweis rechtmäßig?", 640, 560, beim("frage", "rechtmäßig"), fill=PINK, size=46, anker="m"),
    ficon("tabler", "trees", 1360, 400, 200, "frage", fuell=GRUEN),
    *fig("SR", 1420, FB, FR, [("frage", "denkt")]),
    schild("Herr Schröder", 1420, "frage", SR_F),
    *fig("GO", 1720, FB, FR, [("frage", "ernst")]),
    schild("Frau Götz", 1720, "frage", GO_F),
]))

# E Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Nordrhein-Westfalen, Samstagnacht: Herr Schröder feiert mit zwei Freunden im Stadtpark Geburtstag. Eine Musikbox läuft "
    "laut, die 3 singen mit. Gegen Mitternacht ruft Anwohnerin Frau Krämer die Polizei: Die Musik dröhnt bis in ihr "
    "Schlafzimmer. Frau Götz von der Polizei bittet die Gruppe, die Musik leiser zu machen. 1 Stunde später ist die Box wieder "
    "voll aufgedreht. Das Ordnungsamt ist nachts nicht erreichbar. Frau Götz verweist alle 3 bis 6 Uhr morgens aus dem Park. "
    "Herr Schröder fragt: „Auf welcher Grundlage eigentlich?“",
], "War der Platzverweis rechtmäßig?")

# F Aufbau und Landesrecht --------------------------------------------------------------------------------------------------------
folie([("aufbau", "Prüfung · Aufbau"), ("land", "Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen")], rechts_frei([
    *tafel("aufbau", "So prüfst du eine Polizeimaßnahme"),
    blk(110, 180, 1040, 72, BLAU, "a1", [("1. Ermächtigungsgrundlage", "ExtraBold", 36, INK)]),
    blk(110, 270, 1040, 72, GELB, "a2", [("2. formelle Rechtmäßigkeit", "ExtraBold", 36, INK)]),
    blk(110, 360, 1040, 72, GRUEN, beim("a3", "materielle"), [("3. materielle Rechtmäßigkeit", "ExtraBold", 36, INK)]),
    z("Polizeirecht ist Landesrecht", 110, 485, "land", "Bold", 36),
    z("Beispiel hier: Nordrhein-Westfalen", 150, 545, beim("land", "Nordrhein"), size=34),
    zit("PolG NRW (ab 13.12.2025), OBG NRW (ab 1.7.2026)", 150, 600, beim("land", "Beispiel")),
    z("andere Länder: ähnliche Regeln,", 110, 670, beim("land", "anderen"), size=34),
    z("oft unter anderer Nummer", 150, 725, beim("land", "Nummer"), size=34),
    ficon("ph", "police-car", IX, IU, 230, "aufbau", fuell=WEISS, nebenfarbe=BLAU),
    *fig("GO", FX, FB, FR, [("aufbau", "ruhig"), ("land", "denkt")]),
    schild("Frau Götz", FX, "aufbau", GO_F),
]))

# G Ermächtigungsgrundlage: Reihenfolge, Versammlungsrecht ----------------------------------------------------------------------
EGL = "1. Ermächtigungsgrundlage"
folie([("egl", f"{EGL} › Reihenfolge"), ("vers", f"{EGL} › Spezialgesetz? Versammlungsrecht")], rechts_frei([
    *tafel("egl", "1. Ermächtigungsgrundlage"),
    z("Platzverweis greift in Rechte ein:", 110, 175, beim("egl", "greift"), "Bold", 34),
    z("gesetzliche Grundlage nötig", 150, 222, beim("egl", "gesetzliche"), size=33),
    zit("§ 1 Abs. 5 Satz 1 PolG NRW", 150, 268, beim("egl", "Grundlage")),
    z("Reihenfolge:", 110, 315, "reihe", "Bold", 34),
    blk(150, 362, 1000, 60, ZITAT, "r1", [("1. Spezialgesetze", "ExtraBold", 34, INK)]),
    blk(210, 432, 940, 60, GELB, "r2", [("2. Standardmaßnahmen", "ExtraBold", 34, INK)]),
    blk(270, 502, 880, 60, BLAU, "r3", [("3. Generalklausel", "ExtraBold", 34, INK)]),
    z("Spezialgesetz hier? Versammlungsrecht", 110, 598, "vers", "Bold", 34),
    z("Versammlung: mindestens 3 Personen, überwiegend", 150, 648, beim("vers", "Versammlung", 2), size=32),
    z("zur Teilhabe an der öffentlichen Meinungsbildung", 150, 691, beim("vers", "Teilhabe"), size=32),
    zit("§ 2 Abs. 3 VersG NRW", 150, 736, beim("vers", "Meinungsbildung")),
    nein(150, 808, beim("vers", "nicht"), gr=20),
    z("Geburtstagsfeier: keine Versammlung", 195, 785, beim("vers", "Geburtstagsfeier"), "Bold", 34),
    ficon("tabler", "list-numbers", IX, IU, 130, "reihe", fuell=WEISS, bis="vers"),
    ficon(HC, "birthday-cake", IX, IU, 130, "vers", fuell=WEISS),
    *fig("SR", FX, FB, FR, [("egl", "denkt"), ("vers", "froh")]),
    schild("Herr Schröder", FX, "egl", SR_F),
]))

# H Generalklausel: Wortlaut § 8 Abs. 1 PolG NRW ------------------------------------------------------------------------------
W8 = ("„Die Polizei kann die notwendigen Maßnahmen treffen, um eine im einzelnen Falle bestehende, konkrete Gefahr für die "
      "öffentliche Sicherheit oder Ordnung (Gefahr) abzuwehren, soweit nicht die §§ 9 bis 46 die Befugnisse der Polizei "
      "besonders regeln.“")
Z8 = ["„Die Polizei kann die notwendigen Maßnahmen treffen, um eine im",
      "einzelnen Falle bestehende, konkrete Gefahr für die öffentliche",
      "Sicherheit oder Ordnung (Gefahr) abzuwehren, soweit nicht die",
      "§§ 9 bis 46 die Befugnisse der Polizei besonders regeln.“"]
w8, w8_y = wortlaut(70, 170, 1120, W8, "§ 8 Abs. 1 PolG NRW (Generalklausel)", "wl8", size=32, zeilen=Z8,
                    marken=[("notwendigen Maßnahmen", beim("wl8", "notwendigen")), ("konkrete Gefahr", beim("wl8", "konkrete")),
                            ("soweit nicht die", "soweit"),
                            ("§§ 9 bis 46 die Befugnisse der Polizei besonders regeln", beim("soweit", "Paragrafen"))])
folie([("wl8", f"{EGL} › Generalklausel, § 8 I PolG NRW")], rechts_frei([
    titel(glyphen("Die Generalklausel regelt den Vorrang selbst"), 100, 75, "wl8", 42),
    *w8,
    blk(110, w8_y + 40, 1040, 80, GELB, beim("soweit", "besonders"), [("Standardmaßnahme vor Generalklausel", "ExtraBold", 36, INK)]),
    zit("§§ 9 bis 46 PolG NRW: Standardmaßnahmen (z. B. § 34 Platzverweisung)", 150, w8_y + 140, beim("soweit", "regeln")),
    ficon("tabler", "list-numbers", IX, IU, 130, "wl8", fuell=WEISS),
    *fig("GO", FX, FB, FR, [("wl8", "ruhig"), ("soweit", "denkt")]),
    schild("Frau Götz", FX, "wl8", GO_F),
]))

# I Warum zuerst die Standardmaßnahme? ----------------------------------------------------------------------------------------
folie([("warum", f"{EGL} › Warum Standardmaßnahme zuerst?")], rechts_frei([
    *tafel("warum", "Warum zuerst die Standardmaßnahme?"),
    z("Standardmaßnahmen regeln typische Eingriffe", 110, 180, beim("warum", "Standardmaßnahmen"), "Bold", 34),
    z("in Grundrechte genauer:", 150, 233, beim("warum", "Grundrechte"), "Bold", 34),
    z("eigene Voraussetzungen und Grenzen", 150, 288, beim("warum", "Voraussetzungen"), size=34),
    z("klar bestimmt: was darf die Polizei, wo ist Schluss?", 150, 343, beim("warum", "bestimmt"), size=34),
    zit("vgl. VG Düsseldorf, Urt. v. 24.9.2025 – 18 K 4465/25, Rn. 174–178 (nicht rkr.)", 150, 393,
        beim("warum", "Schluss")),
    z("Generalklausel: für Lagen, die das Gesetz", 110, 455, "offen", "Bold", 34),
    z("nicht eigens regelt", 150, 508, beim("offen", "nicht"), "Bold", 34),
    ok(150, 593, beim("leiser", "Aufforderung"), gr=20),
    z("„Musik leiser!“: Generalklausel, § 8 Abs. 1", 195, 570, beim("leiser", "Aufforderung"), size=34),
    z("Box mitnehmen: wieder Standardmaßnahme,", 195, 650, "sicher", size=34),
    z("Sicherstellung, § 43 PolG NRW", 235, 703, beim("sicher", "Sicherstellung"), "Bold", 34),
    ficon("ph", "speaker-hifi", IX, IU, 110, "leiser", fuell=LILA),
    *fig("GO", FX, FB, FR, [("warum", "ruhig"), ("leiser", "denkt")]),
    schild("Frau Götz", FX, "warum", GO_F),
]))

# J Platzverweis: Wortlaut § 34 Abs. 1 Satz 1 PolG NRW ------------------------------------------------------------------------
W34 = ("„Die Polizei kann zur Abwehr einer Gefahr eine Person vorübergehend von einem Ort verweisen oder ihr vorübergehend "
       "das Betreten eines Ortes verbieten.“")
Z34 = ["„Die Polizei kann zur Abwehr einer Gefahr eine Person vorübergehend",
       "von einem Ort verweisen oder ihr vorübergehend das Betreten eines",
       "Ortes verbieten.“"]
w34, w34_y = wortlaut(70, 200, 1120, W34, "§ 34 Abs. 1 Satz 1 PolG NRW (Platzverweisung)", "wl34", size=32, zeilen=Z34,
                      marken=[("zur Abwehr einer Gefahr", beim("wl34", "Abwehr")), ("vorübergehend", beim("wl34", "vorübergehend")),
                              ("von einem Ort verweisen", beim("wl34", "Ort"))])
folie([("wl34", f"{EGL} › Platzverweis, § 34 I 1 PolG NRW")], rechts_frei([
    titel(glyphen("Die Standardmaßnahme: Platzverweisung"), 100, 80, "wl34", 44),
    *w34,
    ok(150, w34_y + 103, "egl34", gr=22),
    blk(200, w34_y + 60, 950, 84, GRUEN, "egl34", [("Ermächtigungsgrundlage: § 34 Abs. 1 Satz 1", "ExtraBold", 34, INK)]),
    ficon("tabler", "map-pin", IX, IU, 110, beim("wl34", "Ort"), fuell=ROT),
    *fig("GO", FX, FB, FR, [("wl34", "ernst")]),
    schild("Frau Götz", FX, "wl34", GO_F),
]))

# K Formelle Rechtmäßigkeit -----------------------------------------------------------------------------------------------------
FO = "2. formell"
folie([("formell", f"{FO} › Zuständigkeit"), ("anh", f"{FO} › Verfahren und Form")], rechts_frei([
    *tafel("formell", "2. Formelle Rechtmäßigkeit", fill=WEISS),
    z("Zuständigkeit:", 110, 180, "zust", "Bold", 34),
    z("Gefahrenabwehr auch Aufgabe des Ordnungsamts", 150, 233, beim("zust", "Ordnungsamt"), size=32),
    zit("§ 1 Abs. 1 OBG NRW", 150, 278, beim("zust", "zuständig")),
    z("seit 1.7.2026 eigene Vorschrift: § 24o OBG NRW", 150, 325, beim("zust", "Juli"), size=32),
    ok(150, 412, beim("eil", "Polizei"), gr=20),
    z("nachts nicht erreichbar: Polizei handelt", 195, 390, "eil", size=32),
    z("in eigener Zuständigkeit", 195, 435, beim("eil", "eigener"), size=32),
    zit("§ 1 Abs. 1 Satz 3 PolG NRW", 195, 480, beim("eil", "Zuständigkeit")),
    z("Verfahren:", 110, 545, "anh", "Bold", 34),
    ok(150, 620, beim("anh", "hier"), gr=20),
    z("Anhörung entbehrlich bei Gefahr im Verzug", 195, 598, beim("anh", "Gefahr"), size=32),
    zit("§ 28 Abs. 2 Nr. 1 VwVfG NRW", 195, 643, beim("anh", "entschieden")),
    z("Form:", 110, 708, "form", "Bold", 34),
    ok(150, 783, beim("form", "mündlich"), gr=20),
    z("mündlicher Platzverweis genügt", 195, 760, beim("form", "mündlich"), size=32),
    zit("§ 37 Abs. 2 Satz 1 VwVfG NRW", 195, 805, beim("form", "ergehen")),
    ficon("ph", "building-office", IX, IU, 140, "zust", fuell=WEISS, nebenfarbe=GELB, bis="eil"),
    ficon("tabler", "moon-stars", IX, IU, 120, "eil", fuell=GELB, bis="anh"),
    ficon("ph", "police-car", IX, IU, 220, "anh", fuell=WEISS, nebenfarbe=BLAU),
    *fig("GO", FX, FB, FR, [("formell", "ruhig"), ("eil", "ernst")]),
    schild("Frau Götz", FX, "formell", GO_F),
]))

# L Materiell: Tatbestand, konkrete Gefahr ------------------------------------------------------------------------------------
MA = "3. materiell › a) Tatbestand"
folie([("mat", f"{MA}: konkrete Gefahr")], rechts_frei([
    *tafel("mat", "3. Materiell: a) Tatbestand"),
    z("konkrete Gefahr für die öffentliche Sicherheit", 110, 180, "gefahr", "Bold", 34),
    z("öffentliche Sicherheit: u. a.", 150, 260, "def", size=34),
    z("Gesundheit des Einzelnen,", 190, 313, beim("def", "Gesundheit"), size=34),
    z("Unversehrtheit der Rechtsordnung", 190, 366, beim("def", "Unversehrtheit"), size=34),
    zit("OVG NRW, Urt. v. 2.7.2020 – 15 A 2100/18, Rn. 72", 190, 416, beim("def", "Rechtsordnung")),
    z("konkret: ohne Eingreifen in überschaubarer Zukunft", 150, 490, "konkret", size=34),
    z("ein Schaden hinreichend wahrscheinlich", 150, 543, beim("konkret", "Schaden"), size=34),
    zit("OVG NRW, Urt. v. 27.9.2021 – 5 A 2807/19, Rn. 67", 150, 593, beim("konkret", "wahrscheinlich")),
    ficon("tabler", "alert-triangle", IX, IU, 130, "mat", fuell=GELB),
    *fig("KR", FX, FB, FR - 20, [("mat", "muede"), ("def", "sorge")]),
    schild("Frau Krämer", FX, "mat", KR_F),
]))

# M Lärm: Wortlaut § 117 Abs. 1 OWiG und § 9 Abs. 1 LImschG NRW, Subsumtion ------------------------------------------------
W117 = ("„Ordnungswidrig handelt, wer ohne berechtigten Anlaß oder in einem unzulässigen oder nach den Umständen vermeidbaren "
        "Ausmaß Lärm erregt, der geeignet ist, die Allgemeinheit oder die Nachbarschaft erheblich zu belästigen oder die "
        "Gesundheit eines anderen zu schädigen.“")
Z117 = ["„Ordnungswidrig handelt, wer ohne berechtigten Anlaß oder in einem",
        "unzulässigen oder nach den Umständen vermeidbaren Ausmaß Lärm erregt,",
        "der geeignet ist, die Allgemeinheit oder die Nachbarschaft erheblich zu",
        "belästigen oder die Gesundheit eines anderen zu schädigen.“"]
w117, w117_y = wortlaut(70, 70, 1120, W117, "§ 117 Abs. 1 OWiG", "owi", size=29, zeilen=Z117,
                        marken=[("unzulässigen", beim("owi", "unzulässigem")),
                                ("vermeidbaren Ausmaß Lärm erregt", beim("owi", "vermeidbarem")),
                                ("Nachbarschaft erheblich zu", beim("owi", "Nachbarschaft")),
                                ("belästigen", beim("owi", "belästigen"))])
W9 = "„Von 22 bis 6 Uhr sind Betätigungen verboten, welche die Nachtruhe zu stören geeignet sind.“"
Z9 = ["„Von 22 bis 6 Uhr sind Betätigungen verboten, welche die Nachtruhe", "zu stören geeignet sind.“"]
w9, w9_y = wortlaut(70, w117_y + 22, 1120, W9, "§ 9 Abs. 1 LImschG NRW (Schutz der Nachtruhe)", "nacht", size=29, zeilen=Z9,
                    marken=[("Von 22 bis 6 Uhr", beim("nacht", "zweiundzwanzig")), ("Nachtruhe", beim("nacht", "Nachtruhe"))])
folie([("owi", f"{MA} › Lärm, § 117 OWiG, § 9 LImschG NRW")], rechts_frei([
    *w117, *w9,
    z("Musik dröhnt bis ins Schlafzimmer, trotz Bitte", 110, w9_y + 22, "subs", size=32),
    z("wieder laut: weitere Verstöße hinreichend wahrscheinlich", 110, w9_y + 67, beim("subs", "wieder"), size=32),
    ok(140, w9_y + 160, "gja", gr=22),
    blk(190, w9_y + 118, 960, 80, GRUEN, "gja", [("konkrete Gefahr liegt vor", "ExtraBold", 36, INK)]),
    ficon("ph", "speaker-hifi", IX, IU - 30, 120, "owi", fuell=LILA),
    ficon("tabler", "music", IX + 90, IU - 150, 60, "owi", fuell=GELB),
    ficon("tabler", "moon-stars", IX - 120, IU - 150, 80, "nacht", fuell=GELB),
    *fig("KR", FX, FB, FR - 20, [("owi", "sorge"), ("subs", "muede")]),
    schild("Frau Krämer", FX, "owi", KR_F),
]))

# N Adressat: Verhaltensstörer ------------------------------------------------------------------------------------------------
folie([("adr", "3. materiell › b) Adressat: Verhaltensstörer, § 4 I PolG NRW")], rechts_frei([
    *tafel("adr", "b) Richtiger Adressat"),
    z("„Verursacht eine Person eine Gefahr, so sind die", 110, 185, beim("adr", "Richtiger"), size=32),
    z("Maßnahmen gegen diese Person zu richten.“", 110, 230, beim("adr", "Richtiger"), size=32),
    zit("§ 4 Abs. 1 PolG NRW", 110, 278, beim("adr", "Richtiger")),
    blk(110, 330, 1040, 76, GELB, beim("adr", "Verhaltensstörer"), [("Verhaltensstörer", "ExtraBold", 36, INK)]),
    z("alle 3 feiern laut mit:", 110, 455, "alle", "Bold", 34),
    z("jeder trägt zum Lärm bei", 150, 510, beim("alle", "Jeder"), size=34),
    ok(150, 603, beim("alle", "alle", 2), gr=20),
    z("Platzverweis gegen alle 3", 195, 580, beim("alle", "alle", 2), "Bold", 34),
    *fig("FA", 1350, FB, 270, [("adr", "froh_r")]),
    schild("Freundin", 1350, "adr", FR_F),
    *fig("SR", 1580, FB, 420, [("adr", "denkt")]),
    schild("Herr Schröder", 1580, "adr", SR_F),
    *fig("FB", 1790, FB, 255, [("adr", "froh")]),
    schild("Freund", 1790, "adr", FR_F),
]))

# O Rechtsfolge: Ermessen, Verhältnismäßigkeit ---------------------------------------------------------------------------------
RF = "3. materiell › c) Rechtsfolge"
folie([("rf", f"{RF}: Ermessen, Verhältnismäßigkeit")], rechts_frei([
    *tafel("rf", "c) Rechtsfolge", fill=ZARTGRUEN),
    z("Ermessen, § 3 Abs. 1 PolG NRW", 110, 180, beim("rf", "Ermessen"), "Bold", 34),
    z("Verhältnismäßigkeit, § 2 PolG NRW", 110, 235, beim("rf", "verhältnismäßig"), "Bold", 34),
    ok(150, 333, beim("geeig", "geeignet"), gr=20),
    z("geeignet: Platzverweis beendet den Lärm", 195, 310, beim("geeig", "beendet"), size=33),
    ok(150, 418, beim("erf", "erforderlich"), gr=20),
    z("erforderlich: milderes Mittel schon versucht,", 195, 395, beim("erf", "erforderlich"), size=33),
    z("die Bitte, leiser zu sein, hat nicht gehalten", 195, 443, beim("erf", "Bitte"), size=33),
    ok(150, 528, beim("angem", "Stunden"), gr=20),
    z("angemessen: ein paar Stunden außerhalb des Parks", 195, 505, beim("angem", "Stunden"), size=33),
    z("wiegen weniger als die Nachtruhe der Nachbarn", 195, 553, beim("angem", "Nachtruhe"), size=33),
    zit("vgl. OVG NRW, Urt. v. 27.9.2021 – 5 A 2807/19, Rn. 83 f.", 195, 603, beim("angem", "Nachbarn")),
    ficon("tabler", "scale", IX, IU, 140, "rf", fuell=WEISS),
    *fig("GO", FX, FB, FR, [("rf", "ruhig"), ("erf", "denkt"), ("angem", "ernst")]),
    schild("Frau Götz", FX, "rf", GO_F),
]))

# P Zeitlich und räumlich begrenzt, Abgrenzung Aufenthaltsverbot -----------------------------------------------------------------
folie([("grenze", f"{RF} › zeitlich und räumlich begrenzt"), ("abgr", f"{RF} › Abgrenzung: Aufenthaltsverbot, § 34 II")],
      rechts_frei([
    *tafel("grenze", "Zeitlich und räumlich begrenzt", fill=ZARTGRUEN),
    z("vorübergehend: Dauer richtet sich nach der", 110, 180, "zeit", "Bold", 33),
    z("konkreten Gefahr", 150, 228, beim("zeit", "konkreten"), "Bold", 33),
    zit("OVG NRW, Beschl. v. 9.1.2023 – 5 B 14/23, Rn. 20", 150, 275, beim("zeit", "Gefahr")),
    ok(150, 348, beim("zeit", "Hier"), gr=20),
    z("hier: bis 6 Uhr, Ende der Nachtruhe", 195, 325, beim("zeit", "Hier"), size=33),
    z("Ort: überschaubar; ganzes Stadtgebiet reicht für", 110, 405, "raum", "Bold", 33),
    z("Abs. 1 nicht", 150, 453, beim("raum", "Stadtgebiet"), "Bold", 33),
    zit("OVG NRW, Urt. v. 27.9.2021 – 5 A 2807/19, Rn. 70 f., 77", 150, 500, beim("raum", "Oberverwaltungsgericht")),
    ok(150, 573, beim("raum", "Park"), gr=20),
    z("hier: der Stadtpark, ein bestimmter Ort", 195, 550, beim("raum", "Park"), size=33),
    z("Abgrenzung: Aufenthaltsverbot, § 34 Abs. 2", 110, 635, "abgr", "Bold", 33),
    z("Tatsachen lassen eine Straftat erwarten", 150, 685, beim("abgr", "Tatsachen"), size=32),
    z("höchstens 3 Monate", 150, 733, beim("abgr", "höchstens"), size=32),
    zit("§ 34 Abs. 2 Satz 1, 4 PolG NRW", 150, 780, beim("abgr", "Monate")),
    ficon("tabler", "clock-hour-6", IX, IU, 120, "zeit", fuell=WEISS, bis="raum"),
    ficon("tabler", "map-pin", IX, IU, 110, "raum", fuell=ROT, bis="abgr"),
    ficon("tabler", "calendar", IX, IU, 120, "abgr", fuell=WEISS),
    *fig("SR", FX, FB, FR, [("grenze", "denkt"), ("raum", "muede")]),
    schild("Herr Schröder", FX, "grenze", SR_F),
]))

# Q Ergebnis und Rechtsschutz -----------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis"), ("rs", "Ergebnis › Rechtsschutz")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 175, 1040, 84, GRUEN, beim("erg", "rechtmäßig"), [("Platzverweis rechtmäßig", "ExtraBold", 40, INK)]),
    z("Rechtsschutz:", 110, 320, "rs", "Bold", 34),
    z("am Morgen erledigt", 150, 375, beim("rs", "erledigt"), size=34),
    z("also: Fortsetzungsfeststellungsklage", 150, 430, beim("rs", "Fortsetzungsfeststellungsklage"), "Bold", 34),
    zit("§ 113 Abs. 1 Satz 4 VwGO analog; OVG NRW, 5 A 2807/19, Rn. 30, 56", 150, 482,
        beim("rs", "Fortsetzungsfeststellungsklage")),
    z("mehr dazu im Video zu den Klagearten", 150, 545, beim("rs", "Klagearten"), size=32),
    ficon("tabler", "gavel", IX, IU, 130, "rs", fuell=WEISS),
    *fig("SR", FX, FB, FR, [("erg", "muede"), ("rs", "denkt")]),
    schild("Herr Schröder", FX, "erg", SR_F),
]))

# R Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Generalklausel zuletzt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Fang nie mit der Generalklausel an.", 200, 200, beim("tipp", "Fang"), "Bold", 36),
    z("Erst prüfen: Spezialgesetz?", 200, 290, "tipp2", size=34),
    z("Standardmaßnahme?", 380, 345, beim("tipp2", "Standardmaßnahme"), size=34),
    z("Generalklausel nur, wenn keine passt", 200, 420, beim("tipp2", "Generalklausel"), "Bold", 34),
    z("Grenzen der Standardmaßnahme nicht über", 200, 510, "tipp3", size=34),
    z("die Generalklausel umgehen", 200, 563, beim("tipp3", "Generalklausel"), size=34),
    zit("§ 8 Abs. 1 PolG NRW: „soweit nicht … besonders regeln“", 200, 613, beim("tipp3", "umgehen")),
    zit("vgl. OVG NRW, Urt. v. 27.9.2021 – 5 A 2807/19, Rn. 82", 200, 655, beim("tipp3", "umgehen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema -----------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Rechtmäßigkeit einer polizeilichen Maßnahme"), 110, 90, "sch", 46),
    z("1. Ermächtigungsgrundlage: Spezialgesetz, dann Standardmaßnahme,", K1, 195, "q1", "Bold", 36, rechts=1820),
    z("zuletzt Generalklausel", K2, 250, beim("q1", "zuletzt"), size=SZ, rechts=1820),
    z("hier: § 34 Abs. 1 Satz 1 PolG NRW", K2, 300, beim("q1", "Hier"), size=SZ, rechts=1820),
    z("2. formell: Zuständigkeit, Verfahren, Form", K1, 380, "q2", "Bold", 36, rechts=1820),
    z("3. materiell:", K1, 455, "q3", "Bold", 36, rechts=1820),
    z("a) Tatbestand: konkrete Gefahr für die öffentliche Sicherheit", K2, 528, "q3a", size=SZ, rechts=1820),
    z("b) richtiger Adressat: Verhaltensstörer", K2, 598, "q3b", size=SZ, rechts=1820),
    z("c) Rechtsfolge: Ermessen und Verhältnismäßigkeit,", K2, 668, "q3c", size=SZ, rechts=1820),
    z("zeitlich und räumlich begrenzt", K3, 718, beim("q3c", "zeitlich"), size=SZ, rechts=1820),
])

# T Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst das ", 0), ("Spezialgesetz", "a"), (",", 0)]], 750, 320, 44, beim("merke", "Erst"),
                {"a": beim("merke", "Spezialgesetz")}),
    *markertext([[("dann die ", 0), ("Standardmaßnahme", "b"), (",", 0)]], 750, 378, 44, beim("merke", "dann"),
                {"b": beim("merke", "Standardmaßnahme")}),
    *markertext([[("zuletzt die ", 0), ("Generalklausel", "c"), (".", 0)]], 750, 436, 44, beim("merke", "zuletzt"),
                {"c": beim("merke", "Generalklausel")}),
    *markertext([[("Ein Platzverweis wehrt eine ", 0), ("konkrete Gefahr", "d"), (" ab,", 0)]], 750, 560, 44, "m2",
                {"d": beim("m2", "konkrete")}),
    *markertext([[("nur ", 0), ("vorübergehend", "e"), (" und nur für einen bestimmten Ort.", 0)]], 750, 618, 44,
                beim("m2", "nur"), {"e": beim("m2", "vorübergehend")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
