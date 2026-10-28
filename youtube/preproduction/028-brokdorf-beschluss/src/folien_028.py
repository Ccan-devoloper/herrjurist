"""Folge 028 · Brokdorf-Beschluss: Darf man eine Demo verbieten? (Art. 8 GG) – Serienstandard Open Peeps (Katzenkönig).
Echter Fall sachlich nacherzählt (BVerfGE 69, 315 – 1 BvR 233, 341/81, Beschl. v. 14.5.1985); Veranstalter, Richter und
Politiker treten nicht auf und werden nicht genannt. Neutral zur Kernkraft: das Kraftwerk erscheint nur als Gebäude-Icon.
Gewalt zurückhaltend: keine Gewaltbilder, Ausschreitungen nur als Textpille.
Szenen laut ../SZENENPLAN.md: A Die Wilstermarsch, B Das Verbot, C Der Weg durch die Instanzen / Die Frage, D Sachverhalt,
E Bedeutung, F Wortlaut Art. 8 I GG, G I. Schutzbereich, H Unfriedlichkeit Einzelner, I Ergebnis Schutzbereich / II. Eingriff,
J Wortlaut Art. 8 II GG, K Anmeldepflicht, L Wortlaut § 15 I VersG, M enge Auslegung, N Kooperation, O Anwendung im Fall,
P Ergebnis, Q Rechtslage heute, R Klausurtipp (Lexi), S Klausurschema, T Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Stempel auf der Allgemeinverfügung, Menschenmenge; Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_028/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
PAPIER = (250, 246, 232, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

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


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def in_tafel(e):
    """Piktogramm, das bewusst in der Tafel steht (zählt nicht als Requisit rechts)."""
    e.name = "tafelicon:" + (e.name or "")
    return e


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_028/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte (wie Folge 019/025): Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
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


# --- Eigene Hilfsfunktion (wie Folge 020/025): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
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


def schild(name, text, cx, cue, fill, d=0.2, bis=None, unten=None):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=28, anker="m", d=d, bis=bis)


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
P1 = "Fall"
A8 = "Art. 8 GG"
PR = f"{A8} › III. Rechtfertigung"
EL_TAG, BO_TAG = ("Elke, Anwohnerin", LILA), ("Herr Böhm, Versammlungsbehörde", WEISS)

# A Fall: die Wilstermarsch ---------------------------------------------------------------------------------------------
ELX = 1000
BAUX = 1420
folie([(NULL, f"{P1} · Die Wilstermarsch")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Wilstermarsch, Februar 1981", 70, 40, NULL, fill=GELB, size=44)),
    *[ficon("tabler", "trees", x, BODEN - 2, 120, NULL, fuell=GRUEN, anim="cut") for x in (130, 300)],
    ficon("tabler", "windmill", 470, BODEN - 2, 130, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "building-factory-2", BAUX + 120, BODEN - 2, 260, beim("bau", "Kernkraftwerks"), fuell=GRAU),
    ficon("tabler", "crane", BAUX - 170, BODEN - 2, 220, beim("bau", "Bau"), fuell=GELB),
    *[ficon("tabler", "fence", BAUX - 260 + 130 * i, BODEN - 2, 120, beim("bau", "weitergehen"), fuell=WEISS, d=0.08 * i)
      for i in range(5)],
    pl("Brokdorf: Bau eines Kernkraftwerks", BAUX, 560, beim("bau", "Brokdorf"), fill=WEISS, size=32, anker="m"),
    ficon("tabler", "speakerphone", 220, 330, 130, "aufruf", fuell=ORANGE),
    pl("Aufruf: Großdemonstration", 300, 200, "aufruf", fill=ORANGE, size=34),
    pl("am 28.2.1981", 300, 270, beim("aufruf", "achtundzwanzigsten"), fill=WEISS, size=32),
    pl("frühere Demos: teilweise unfriedlich", 70, 470, "frueher", fill=PINK, size=30),
    *fig("EL", ELX, BODEN, FH, [("elke", "ruhig_r")], bis="e1"),
    *redet("EL_redet_r", ELX, BODEN, FH, "e1", "boehm"),
    pl("Elke, Anwohnerin", ELX, BODEN + 22, beim("elke", "Elke"), fill=LILA, size=28, anker="m"),
    blase("sprech", 820, 200, "e1", 1230, 250, inhalt=["Ich will friedlich demonstrieren,", "so nah am Bauplatz wie möglich."],
          textsize=32, figur=("EL_redet_r", ELX, BODEN, FH), bis="boehm"),
])

# B Fall: das Verbot (Versammlungsbehörde) ---------------------------------------------------------------------------------
BOX = 1560
AK = (70, 150, 640, 640)                     # Allgemeinverfügung (x, y, w, h)
stempel = bewegt(ficon("tabler", "rubber-stamp", 560, 640, 100, "sofort", fuell=ROT),
                 "sofort", ("sofort", 0.45), 0, -160)
folie([("boehm", f"{P1} · Das Verbot")], [
    linienzug([(60, BODEN), (1860, BODEN)], "boehm", breite=7, farbe=INK),
    ficon("tabler", "table", 1210, BODEN - 2, 280, "boehm", fuell=ORANGE),
    ficon("tabler", "files", 1160, BODEN - 175, 90, "boehm", fuell=WEISS),
    ficon("tabler", "lamp", 1280, BODEN - 175, 100, "boehm", fuell=GELB),
    *fig("BO", BOX, BODEN, FH, [("boehm", "ruhig")], bis="b1"),
    *redet("BO_redet", BOX, BODEN, FH, "b1", "verbot"),
    peep_voll("BO_ernst", BOX, BODEN, FH, "verbot", anim="cut"),
    pl("Herr Böhm, Versammlungsbehörde", BOX, BODEN + 22, beim("boehm", "Böhm"), fill=WEISS, size=28, anker="m"),
    pl("Landrat des Kreises Steinburg", 70, 40, beim("boehm", "Landrat"), fill=GELB, size=36),
    bis_(ficon("tabler", "users-group", 380, 560, 220, "zahl", fuell=BLAU), "verbot"),
    bis_(pl("bis zu 50.000 Menschen erwartet", 380, 610, beim("zahl", "fünfzigtausend"), fill=BLAU, size=32, anker="m"), "verbot"),
    bis_(ficon("tabler", "news", 640, 420, 120, beim("b1", "Flugblättern"), fuell=WEISS), "verbot"),
    blase("sprech", 820, 240, "b1", 1000, 300, inhalt=["Angemeldet ist nichts. Und in", "Flugblättern heißen einige", "Gruppen Gewalt gut. Wir verbieten alles."],
          textsize=31, figur=("BO_redet", BOX, BODEN, FH), bis="verbot"),
    karte(*AK, "verbot", fill=PAPIER),
    titel(glyphen("Allgemeinverfügung"), 110, 185, "verbot", 44),
    z("vom 23.2.1981", 110, 245, beim("verbot", "dreiundzwanzigsten"), size=28, rechts=700),
    z("Verbot jeder Demonstration", 110, 300, beim("verbot", "jede"), "Bold", 32, rechts=700),
    z("gegen das Kraftwerk", 110, 345, beim("verbot", "Kraftwerk"), "Bold", 32, rechts=700),
    z("27.2. bis 1.3.1981", 110, 425, beim("gebiet", "drei"), size=32, rechts=700),
    z("rund 210 km² der Wilstermarsch", 110, 480, beim("gebiet", "zweihundertzehn"), size=32, rechts=700),
    z("sofort vollziehbar", 110, 560, "sofort", "Bold", 32, rechts=700),
    szene(stempel, "028stempel*", 1.0, versatz=0.45 - 0.20),
    zit("nach BVerfGE 69, 315 (321 f.) · Rn. 24–26", 110, 720, beim("sofort", "vollziehbar")),
])

# C Fall: der Weg durch die Instanzen / die Frage ---------------------------------------------------------------------------
MX, MY = 560, 520                            # Baustelle in der Karte
menge = [(250, 330), (870, 330), (230, 700), (890, 700)]
folie([("vg", f"{P1} · Der Weg durch die Instanzen"), ("frage", f"{P1} · Die Frage")], [
    karte(70, 120, 1000, 780, "vg", fill=(234, 244, 226, 255)),
    pl("Wilstermarsch", 95, 835, "vg", fill=WEISS, size=26),
    ficon("tabler", "building-factory-2", MX + 40, MY + 50, 120, "vg", fuell=GRAU),
    ficon("tabler", "fence", MX - 60, MY + 50, 80, "vg", fuell=WEISS),
    bis_(ring(MX, MY, 420, 300, "vg", farbe=DROT, breite=9), beim("vg", "beschränkt")),
    bis_(pl("Verbotsgebiet: rund 210 km²", MX + 120, 830, "vg", fill=ROT, size=28, anker="m"), beim("vg", "beschränkt")),
    bis_(ring(MX, MY, 170, 130, beim("vg", "beschränkt"), farbe=ORANGE, breite=9), beim("ovg", "ganze")),
    bis_(pl("nur Umgebung der Baustelle", MX + 120, 830, beim("vg", "Umgebung"), fill=ORANGE, size=28, anker="m"), beim("ovg", "ganze")),
    ring(MX, MY, 420, 300, beim("ovg", "ganze"), farbe=DROT, breite=9),
    pl("wieder das ganze Verbot", MX + 120, 830, beim("ovg", "ganze"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "building-bank", 1330, 280, 120, "vg", fuell=GRAU),
    pl("Verwaltungsgericht", 1330, 290, "vg", fill=WEISS, size=26, anker="m"),
    ficon("tabler", "building-bank", 1330, 520, 120, beim("ovg", "Oberverwaltungsgericht"), fuell=GRAU),
    pl("Oberverwaltungsgericht", 1330, 530, beim("ovg", "Oberverwaltungsgericht"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "moon-stars", 1180, 420, 70, beim("ovg", "Nacht"), fuell=GELB),
    *[szene(ficon("tabler", "users-group", x, y, 110, beim("demo", "demonstrieren"), fuell=BLAU, d=0.1 * i), "028menge*", 0.5, 0.0)
      if i == 0 else ficon("tabler", "users-group", x, y, 110, beim("demo", "demonstrieren"), fuell=BLAU, d=0.1 * i)
      for i, (x, y) in enumerate(menge)],
    pl("weit mehr als 50.000 Menschen", MX, 175, beim("demo", "weit"), fill=BLAU, size=30, anker="m"),
    pl("auch Ausschreitungen", MX, 230, beim("demo", "Ausschreitungen"), fill=PINK, size=26, anker="m"),
    ficon(HC, "classical-building", 1330, 790, 150, "vb", fuell=WEISS),
    pl("Verfassungsbeschwerden", 1330, 800, beim("vb", "Verfassungsbeschwerden"), fill=GELB, size=26, anker="m"),
    *fig("EL", 1730, FB, FR, [("vg", "ruhig"), ("ovg", "sorge"), ("frage", "denkt")]),
    schild("EL", "Elke", 1730, "vg", LILA),
    pl("Durfte der Staat diese Demonstration verbieten?", 640, 960, beim("frage", "Durfte"), fill=PINK, size=32, anker="m"),
])

# Fragepille zwei: über der Karte, eigener Bildhalt
FOLIEN[-1]["els"].append(pl("Und wann darf er das überhaupt?", 640, 50, beim("frage", "Und"), fill=PINK, size=32, anker="m"))

# D Sachverhalt ---------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Februar 1981: Bürgerinitiativen rufen bundesweit zu einer Großdemonstration gegen den Weiterbau des Kernkraftwerks "
    "Brokdorf (Schleswig-Holstein) am 28. Februar auf; frühere Demonstrationen dort verliefen teilweise unfriedlich. Die "
    "Demonstration ist nicht angemeldet. Die Behörde rechnet mit bis zu 50.000 Teilnehmern, darunter Gewaltbereiten. Am "
    "23. Februar verbietet der Landrat des Kreises Steinburg per Allgemeinverfügung jede Demonstration gegen das Kraftwerk "
    "vom 27. Februar bis 1. März auf rund 210 km² der Wilstermarsch, sofort vollziehbar. Das Verwaltungsgericht beschränkt "
    "das Verbot auf die Umgebung der Baustelle; das Oberverwaltungsgericht stellt es in der Nacht vor der Demonstration "
    "vollständig wieder her. Es folgen Verfassungsbeschwerden.",
    "(Nach BVerfGE 69, 315 – 1 BvR 233, 341/81, Beschluss vom 14. Mai 1985.)",
], "Verletzt das Verbot die Versammlungsfreiheit (Art. 8 GG)?")

# E Bedeutung der Versammlungsfreiheit -------------------------------------------------------------------------------------
folie([("demok", f"{A8} · Bedeutung für die Demokratie")], rechts_frei([
    *tafel("demok", "Warum die Versammlungsfreiheit zählt"),
    z("Bundesverfassungsgericht:", 110, 185, beim("demok", "Bundesverfassungsgericht"), size=32),
    z("unentbehrliches Funktionselement", 110, 235, beim("demok", "unentbehrlichen"), "Bold", 36),
    z("eines demokratischen Gemeinwesens", 110, 285, beim("demok", "demokratischen"), "Bold", 36),
    z("gerade auch für andersdenkende Minderheiten", 110, 365, beim("minder", "andersdenkenden"), size=34),
    z("ein Stück unmittelbarer Demokratie", 110, 445, beim("frueh", "Stück"), size=34),
    z("Teil eines politischen Frühwarnsystems", 110, 495, beim("frueh", "Frühwarnsystem"), size=34),
    z("Selbstbestimmung über", 110, 580, "selbst", "Bold", 34),
    z("Ort, Zeitpunkt, Art und Inhalt", 150, 630, beim("selbst", "Ort"), size=34),
    zit("BVerfGE 69, 315 · LS 1; (343, 347) · Rn. 61, 66", 110, 720, beim("selbst", "Inhalt")),
    ficon("tabler", "building-community", IX, IU, 150, "demok", fuell=BLAU, bis="minder"),
    ficon("tabler", "users-group", IX, IU, 150, "minder", fuell=LILA, bis="frueh"),
    ficon("tabler", "bell-ringing", IX, IU, 120, beim("frueh", "Frühwarnsystem"), fuell=GELB, bis="selbst"),
    ficon("tabler", "map-pin", IX, IU, 110, "selbst", fuell=ROT),
    *fig("EL", FX, FB, FR, [("demok", "ruhig"), ("selbst", "froh")]),
    schild("EL", "Elke", FX, "demok", LILA),
]))

# F Wortlaut Art. 8 I GG -----------------------------------------------------------------------------------------------------
W8 = ["„Alle Deutschen haben das Recht, sich ohne", "Anmeldung oder Erlaubnis friedlich und ohne", "Waffen zu versammeln.“"]
w8_els, _ = wortlaut(80, 220, 1100, W8, "Art. 8 Abs. 1 GG", "wl8", marken=[
    (0, "Alle Deutschen", beim("wl8", "Alle")), (1, "Anmeldung oder Erlaubnis", beim("wl8", "Anmeldung")),
    (1, "friedlich", beim("wl8", "friedlich")), (1, "ohne", beim("wl8", "ohne", nr=2)), (2, "Waffen", beim("wl8", "ohne", nr=2)),
    (2, "versammeln", beim("wl8", "versammeln"))], size=40)
folie([("wl8", f"{A8} › Wortlaut Art. 8 I GG")], rechts_frei([
    titel(glyphen("Der Wortlaut"), 110, 90, "wl8", 50),
    *w8_els,
    ficon("tabler", "book", IX, IU, 140, "wl8", fuell=GELB),
    *fig("EL", FX, FB, FR, [("wl8", "ruhig")]),
    schild("EL", "Elke", FX, "wl8", LILA),
]))

# G I. Schutzbereich --------------------------------------------------------------------------------------------------------
PS_ = f"{A8} › I. Schutzbereich"
folie([("sb", PS_), ("fried", f"{PS_} › friedlich und ohne Waffen")], rechts_frei([
    *tafel("sb", "I. Schutzbereich"),
    z("Versammlung: gemeinschaftliche, auf", 110, 195, beim("vers", "Geschützt"), "Bold", 36),
    z("Kommunikation angelegte Entfaltung", 110, 250, beim("vers", "Kommunikation"), "Bold", 36),
    z("auch die Demonstration", 150, 320, beim("vers", "Demonstration"), size=36),
    z("unfriedlich jedenfalls, wer", 110, 430, "fried", "Bold", 36),
    z("Gewalttätigkeiten gegen Personen", 150, 490, beim("fried", "Gewalttätigkeiten"), size=36),
    z("oder Sachen begeht", 150, 545, beim("fried", "Sachen"), size=36),
    zit("BVerfGE 69, 315 (342 f., 360) · Rn. 60, 90", 110, 640, beim("fried", "begeht")),
    ficon("tabler", "users-group", IX, IU, 150, "sb", fuell=GRUEN, bis="fried"),
    ficon("tabler", "hand-stop", IX, IU, 120, "fried", fuell=WEISS),
    *fig("EL", FX, FB, FR, [("sb", "ruhig"), ("fried", "ernst")]),
    schild("EL", "Elke", FX, "sb", LILA),
]))

# H Unfriedlichkeit Einzelner ------------------------------------------------------------------------------------------------
PU = f"{PS_} › Unfriedlichkeit Einzelner"
LEUTE = [(150 + 95 * i, 270) for i in range(10)]
ROTE = (3, 7)
folie([("einzel", PU)], rechts_frei([
    *tafel("einzel", "Und wenn nur einige gewalttätig werden?", size=42),
    *[in_tafel(ficon("tabler", "user", x, y, 70, "einzel", fuell=GRUEN, anim="cut",
            bis=beim("einzel", "gewalttätig") if i in ROTE else None)) for i, (x, y) in enumerate(LEUTE)],
    *[in_tafel(ficon("tabler", "user-x", LEUTE[i][0], LEUTE[i][1], 70, beim("einzel", "gewalttätig"), fuell=ROT)) for i in ROTE],
    ok(140, 350, beim("einzel", "Schutz"), gr=22),
    z("der Schutz bleibt für die friedlichen", 185, 330, beim("einzel", "Schutz"), "Bold", 34),
    z("Teilnehmer erhalten", 185, 380, beim("einzel", "Teilnehmer"), "Bold", 34),
    z("sonst: Einzelne könnten jede Demonstration", 110, 465, "umfunk", size=33),
    z("umfunktionieren und verbieten lassen", 150, 515, beim("umfunk", "umfunktionieren"), size=33),
    nein(140, 615, "kollek", gr=20),
    z("anders nur, wenn die Demonstration", 185, 595, "kollek", size=33),
    z("im Ganzen unfriedlich verlaufen soll", 185, 645, beim("kollek", "Ganzen"), size=33),
    z("oder Veranstalter und Anhang Gewalt", 185, 695, beim("kollek", "Veranstalter"), size=33),
    z("anstreben oder billigen", 185, 745, beim("kollek", "anstreben"), size=33),
    zit("BVerfGE 69, 315 (360 f.) · LS 4, Rn. 91 f.", 110, 815, beim("kollek", "billigen")),
    ficon("tabler", "shield-check", IX, IU, 130, beim("einzel", "Schutz"), fuell=GRUEN),
    *fig("EL", FX, FB, FR, [("einzel", "sorge"), (beim("einzel", "Schutz"), "froh")]),
    schild("EL", "Elke", FX, "einzel", LILA),
]))

# I Ergebnis Schutzbereich, II. Eingriff --------------------------------------------------------------------------------------
folie([("elke2", f"{PS_} › Ergebnis"), ("ein", f"{A8} › II. Eingriff")], rechts_frei([
    *tafel("elke2", "Und Elke?"),
    z("auch die Behörde ging davon aus:", 110, 195, "elke2", "Bold", 36),
    z("die meisten wollten friedlich demonstrieren", 150, 255, beim("elke2", "meisten"), size=34),
    *plusminus("Elke: geschützt", 110, 345, beim("elke2", "geschützt"), True, size=38, stil="Bold"),
    blk(110, 450, 1040, 90, BLAU, "ein", [("II. Eingriff: das Verbot", "ExtraBold", 38, INK)]),
    ok(1110, 495, beim("ein", "Eingriff"), gr=22),
    zit("BVerfGE 69, 315 (334, 365) · Rn. 43, 52, 99", 110, 590, beim("ein", "Eingriff")),
    ficon("tabler", "ban", IX, IU, 120, "ein", fuell=ROT),
    *fig("EL", FX, FB, FR, [("elke2", "froh"), ("ein", "ernst")]),
    schild("EL", "Elke", FX, "elke2", LILA),
]))

# J Wortlaut Art. 8 II GG und Grenzen -------------------------------------------------------------------------------------------
W82 = ["„Für Versammlungen unter freiem Himmel kann", "dieses Recht durch Gesetz oder auf Grund eines", "Gesetzes beschränkt werden.“"]
w82_els, w82_y = wortlaut(80, 200, 1100, W82, "Art. 8 Abs. 2 GG", "wl82", marken=[
    (0, "unter freiem Himmel", beim("wl82", "unter")), (1, "durch Gesetz", beim("wl82", "durch")),
    (1, "auf Grund eines", beim("wl82", "auf")), (2, "Gesetzes", beim("wl82", "auf")),
    (2, "beschränkt", beim("wl82", "beschränkt"))], size=38)
folie([("wl82", f"{PR} › Wortlaut Art. 8 II GG"), ("gleich", f"{PR} › Grenzen der Beschränkung")], rechts_frei([
    titel(glyphen("III. Rechtfertigung"), 110, 90, "wl82", 50),
    *w82_els,
    z("aber nur zum Schutz gleichwertiger", 110, w82_y + 50, "gleich", "Bold", 36),
    z("Rechtsgüter", 110, w82_y + 105, beim("gleich", "Rechtsgüter"), "Bold", 36),
    z("strikte Wahrung der Verhältnismäßigkeit", 110, w82_y + 185, beim("gleich", "strikter"), size=36),
    zit("BVerfGE 69, 315 (348 f.) · LS 2 b, Rn. 69", 110, w82_y + 270, beim("gleich", "Verhältnismäßigkeit")),
    ficon("tabler", "book", IX, IU, 140, "wl82", fuell=GELB, bis="gleich"),
    ficon("tabler", "scale", IX, IU, 160, "gleich", fuell=GELB),
    *fig("BO", FX, FB, FR, [("wl82", "ruhig")]),
    schild("BO", "Herr Böhm", FX, "wl82", WEISS),
]))

# K Anmeldepflicht -------------------------------------------------------------------------------------------------------------
folie([("anm", f"{PR} › Anmeldepflicht, § 14 VersG")], rechts_frei([
    *tafel("anm", "Und die fehlende Anmeldung?"),
    z("§ 14 VersG: Anmeldung unter freiem Himmel", 110, 195, beim("anm", "Paragraf"), "Bold", 34),
    z("verfassungsgemäß, solange die Pflicht", 110, 280, "ausn", size=34),
    z("nicht ausnahmslos gilt", 150, 330, beim("ausn", "nicht"), "Bold", 34),
    z("Spontanversammlung: aus aktuellem Anlass", 110, 420, "spontan", size=34),
    z("augenblicklich gebildet, keine Anmeldung", 150, 470, beim("spontan", "brauchen"), size=34),
    nein(140, 580, "auto", gr=20),
    z("nicht angemeldet: nicht automatisch Verbot", 185, 560, "auto", "Bold", 34),
    z("das Eingreifen wird nur leichter", 185, 615, beim("auto", "Eingreifen"), size=34),
    zit("BVerfGE 69, 315 (349–351) · LS 2 a, Rn. 72–74", 110, 700, beim("auto", "leichter")),
    ficon("tabler", "file-text", IX, IU, 110, "anm", fuell=WEISS, bis="spontan"),
    ficon("tabler", "bolt", IX, IU, 110, "spontan", fuell=GELB, bis="auto"),
    ficon("tabler", "ban", IX, IU, 110, "auto", fuell=WEISS),
    *fig("BO", FX, FB, FR, [("anm", "ruhig"), ("auto", "denkt")]),
    schild("BO", "Herr Böhm", FX, "anm", WEISS),
]))

# L Wortlaut § 15 I VersG ------------------------------------------------------------------------------------------------------
W15 = ["„Die zuständige Behörde kann die Versammlung oder den", "Aufzug verbieten oder von bestimmten Auflagen abhängig",
       "machen, wenn nach den zur Zeit des Erlasses der Verfügung", "erkennbaren Umständen die öffentliche Sicherheit oder",
       "Ordnung bei Durchführung der Versammlung oder des", "Aufzuges unmittelbar gefährdet ist.“"]
w15_els, _ = wortlaut(80, 200, 1100, W15, "§ 15 Abs. 1 VersG", "wl15", marken=[
    (1, "verbieten", beim("merk", "verbieten")), (1, "Auflagen", beim("merk", "Auflagen")),
    (3, "erkennbaren Umständen", beim("merk", "erkennbaren")), (3, "öffentliche Sicherheit oder", beim("merk", "öffentliche")),
    (4, "Ordnung", beim("merk", "Ordnung")), (5, "unmittelbar gefährdet", beim("merk", "unmittelbar"))], size=34)
folie([("wl15", f"{PR} › § 15 I VersG › Wortlaut")], rechts_frei([
    titel(glyphen("Grundlage: § 15 Abs. 1 VersG"), 110, 90, "wl15", 50),
    *w15_els,
    zit("Fassung wie 1981 (BVerfGE 69, 315 [318] · Rn. 10); gilt fort, soweit kein Landesgesetz", 110, 690, "wl15"),
    ficon("tabler", "book", IX, IU, 140, "wl15", fuell=GELB),
    *fig("BO", FX, FB, FR, [("wl15", "ernst")]),
    schild("BO", "Herr Böhm", FX, "wl15", WEISS),
]))

# M Enge Auslegung --------------------------------------------------------------------------------------------------------------
P15 = f"{PR} › § 15 I VersG"
folie([("eng", f"{P15} › enge Auslegung"), ("unmit", f"{P15} › unmittelbare Gefährdung"),
       ("ultima", f"{P15} › Verbot als ultima ratio")], rechts_frei([
    *tafel("eng", "Enge Auslegung"),
    z("1. Schutz elementarer Rechtsgüter", 110, 190, "elem", "Bold", 36),
    z("öffentliche Ordnung allein: im Allgemeinen nicht", 150, 245, beim("elem", "öffentliche"), size=32),
    z("2. unmittelbare Gefährdung", 110, 335, "unmit", "Bold", 36),
    z("Prognose aus Tatsachen", 150, 390, "prog", size=34),
    nein(170, 465, beim("prog", "bloßer"), gr=18),
    z("bloßer Verdacht reicht nicht", 210, 445, beim("prog", "bloßer"), size=34),
    z("3. Verbot als ultima ratio", 110, 535, "ultima", "Bold", 36),
    z("erst Auflagen ausschöpfen", 150, 590, beim("ultima", "Auflagen"), size=34),
    zit("BVerfGE 69, 315 (352–354) · LS 2 b, Rn. 78–80", 110, 680, beim("ultima", "ausgeschöpft")),
    ficon("tabler", "shield-check", IX, IU, 130, "elem", fuell=GRUEN, bis="unmit"),
    ficon("tabler", "alert-triangle", IX, IU, 120, "unmit", fuell=GELB, bis="prog"),
    ficon("tabler", "search", IX, IU, 120, "prog", fuell=WEISS, bis="ultima"),
    ficon("tabler", "stairs", IX, IU, 120, "ultima", fuell=ORANGE),
    *fig("EL", FX, FB, FR, [("eng", "ruhig"), ("prog", "froh")]),
    schild("EL", "Elke", FX, "eng", LILA),
]))

# N Kooperation (Gespräch am Tisch) -------------------------------------------------------------------------------------------
BX2, EX2 = 1000, 1560
BOb = ("BO_redet_r", BX2, BODEN, FH)
ELb = ("EL_redet", EX2, BODEN, FH)
KK = (70, 130, 640, 700)
folie([("koop", f"{PR} › Kooperation der Behörde")], [
    linienzug([(60, BODEN), (1860, BODEN)], "koop", breite=7, farbe=INK),
    ficon("tabler", "table", 1280, BODEN - 2, 280, "koop", fuell=ORANGE),
    ficon("tabler", "heart-handshake", 1280, BODEN - 175, 100, beim("koop", "Kooperation"), fuell=GRUEN),
    *fig("BO", BX2, BODEN, FH, [("koop", "ruhig_r")], bis="b2"),
    *redet("BO_redet_r", BX2, BODEN, FH, "b2", "e2"),
    *fig("BO", BX2, BODEN, FH, [("e2", "ruhig_r"), ("abm", "denkt_r")], erst="cut"),
    pl("Herr Böhm", BX2, BODEN + 22, "koop", fill=WEISS, size=28, anker="m"),
    *fig("EL", EX2, BODEN, FH, [("koop", "ruhig")], bis="e2", d=0.1),
    *redet("EL_redet", EX2, BODEN, FH, "e2", "abm"),
    peep_voll("EL_ruhig", EX2, BODEN, FH, "abm", anim="cut"),
    pl("Elke", EX2, BODEN + 22, "koop", fill=LILA, size=28, anker="m", d=0.1),
    karte(*KK, "koop", fill=PAPIER),
    titel(glyphen("Kooperation"), 110, 165, "koop", 46),
    z("versammlungsfreundlich verfahren", 110, 260, beim("koop", "versammlungsfreundlich"), size=30, rechts=690),
    z("zu Dialog und Kooperation bereit", 110, 310, beim("koop", "Dialog"), size=30, rechts=690),
    z("je mehr Kooperation der Veranstalter,", 110, 390, "schwelle", size=30, rechts=690),
    z("desto höher die Eingriffsschwelle", 110, 435, beim("schwelle", "höher"), "Bold", 30, rechts=690),
    z("Behörde kannte Zeit, Ort und", 110, 520, "abm", size=30, rechts=690),
    z("Trägergruppen", 110, 565, beim("abm", "Trägergruppen"), size=30, rechts=690),
    nein(130, 640, beim("abm", "Abmahnung"), gr=18),
    z("erwogene Abmahnung unterlassen", 170, 620, beim("abm", "Abmahnung"), "Bold", 30, rechts=690),
    zit("BVerfGE 69, 315 (355–359, 367) · LS 3, Rn. 83 f., 88, 103", 110, 735, beim("abm", "unterließ"), size=22),
    blase("sprech", 760, 210, "b2", 1120, 300, inhalt=["Mit wem hätten wir denn sprechen", "sollen? Es gab keinen Veranstalter."],
          textsize=32, figur=BOb, bis="e2"),
    blase("sprech", 700, 200, "e2", 1230, 320, inhalt=["Wer zur Demonstration aufgerufen", "hat, war doch bekannt."],
          textsize=32, figur=ELb, bis="abm"),
])

# O Anwendung im Fall ---------------------------------------------------------------------------------------------------------
folie([("subs", f"{PR} › Anwendung im Fall")], [
    karte(70, 120, 1000, 780, "subs", fill=(234, 244, 226, 255)),
    pl("Wilstermarsch", 95, 835, "subs", fill=WEISS, size=26),
    ficon("tabler", "building-factory-2", MX + 40, MY + 50, 120, "subs", fuell=GRAU),
    ficon("tabler", "fence", MX - 60, MY + 50, 80, "subs", fuell=WEISS),
    ring(MX, MY, 170, 130, beim("subs", "enge"), farbe=ORANGE, breite=9),
    haken_i(MX + 150, MY - 140, beim("subs", "vertretbar"), gr=26),
    pl("Umgebung der Baustelle: vertretbar", MX + 120, 830, beim("subs", "vertretbar"), fill=ORANGE, size=28, anker="m"),
    pl("Anhaltspunkte für Gewalt am Bauzaun", 1440, 180, beim("zaun", "erkennbare"), fill=WEISS, size=26, anker="m"),
    pl("Demonstranten: nichts zur Entschärfung beigetragen", 1300, 250, beim("zaun", "Demonstranten"), fill=WEISS, size=26, anker="m"),
    ring(MX, MY, 420, 300, "rest", farbe=DROT, breite=9),
    kreuz_i(MX + 390, MY - 300, beim("rest", "fehlten"), gr=26),
    pl("übrige Marsch: keine Anhaltspunkte", MX, 175, beim("rest", "fehlten"), fill=ROT, size=28, anker="m"),
    pl("Befürchtungen Dritter genügen nicht", 1300, 330, "angst", fill=PINK, size=26, anker="m"),
    pl("weit überwiegende Mehrheit: friedlich", 1300, 410, beim("mehr", "weit"), fill=GRUEN, size=26, anker="m"),
    zit("BVerfGE 69, 315 (365–368) · Rn. 99 f., 103", 90, 925, beim("mehr", "demonstrieren")),
    *fig("EL", 1730, FB, FR, [("subs", "ruhig"), ("rest", "froh")]),
    schild("EL", "Elke", 1730, "subs", LILA),
])

# P Ergebnis ---------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Beschluss vom 14.5.1985")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 90, GRUEN, "erg", [("Beschluss vom 14.5.1985", "ExtraBold", 38, INK)]),
    z("Verfassungsbeschwerden teilweise stattgegeben", 110, 320, beim("erg", "teilweise"), "Bold", 34),
    z("Ausschlag: ein Verfahrensfehler", 110, 410, "verf", "Bold", 34),
    z("OVG durfte nach damaligem Recht nicht", 150, 465, beim("verf", "damaligem"), size=32),
    z("zum Nachteil der Beschwerdeführer ändern", 150, 515, beim("verf", "Nachteil"), size=32),
    z("künftig: Verbote dieses Umfangs und mit", 110, 605, "kuenft", size=32),
    z("dieser Begründung schwerlich zu billigen", 150, 655, beim("kuenft", "Begründung"), "Bold", 32),
    zit("BVerfGE 69, 315 · 1 BvR 233, 341/81 · Tenor, Rn. 103–105 (§ 80 VI 2 VwGO a. F.)", 110, 740, beim("kuenft", "gebilligt")),
    ficon(HC, "classical-building", IX, IU, 180, "erg", fuell=WEISS),
    ficon("tabler", "gavel", IX + 170, IU, 100, beim("erg", "teilweise"), fuell=GELB),
    *fig("BO", FX, FB, FR, [("erg", "ernst"), ("kuenft", "denkt")]),
    schild("BO", "Herr Böhm", FX, "erg", WEISS),
]))

# Q Rechtslage heute --------------------------------------------------------------------------------------------------------
folie([("heute", "Rechtslage heute · Landesversammlungsgesetze")], rechts_frei([
    *tafel("heute", "Und heute?"),
    z("seit der Föderalismusreform 2006:", 110, 195, beim("heute", "Seit"), "Bold", 36),
    z("Versammlungsrecht ist Ländersache", 150, 255, beim("heute", "Ländersache"), size=36),
    z("Bayern: erstes eigenes Landesgesetz", 110, 345, "bayern", size=36),
    z("kein Landesgesetz: Versammlungsgesetz", 110, 435, "fort", size=36),
    z("des Bundes gilt fort", 150, 490, beim("fort", "Bundes"), "Bold", 36),
    z("Maßstäbe aus Art. 8 GG binden", 110, 580, "bind", size=36),
    z("jeden Gesetzgeber", 150, 635, beim("bind", "jeden"), "Bold", 36),
    zit("BVerfGE 122, 342 Rn. 2 · Art. 125a Abs. 1 GG · in deinem Land ggf. andere Norm", 110, 725, beim("bind", "Gesetzgeber")),
    ficon("tabler", "map", IX, IU, 140, "heute", fuell=GRUEN, bis="bind"),
    ficon("tabler", "scale", IX, IU, 150, "bind", fuell=GELB),
    *fig("EL", FX, FB, FR, [("heute", "ruhig")]),
    schild("EL", "Elke", FX, "heute", LILA),
]))

# R Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · erst das mildere Mittel")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("bei einem Verbot immer zuerst", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("das mildere Mittel prüfen", 200, 255, beim("tipp", "mildere"), "Bold", 36),
    z("reichen Auflagen oder ein räumlich", 200, 360, "tipp1", size=34),
    z("begrenztes Verbot:", 200, 410, beim("tipp1", "begrenztes"), size=34),
    z("Totalverbot unverhältnismäßig", 200, 470, beim("tipp1", "Totalverbot"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ----------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Versammlungsverbot, Art. 8 GG"), 110, 90, "sch", 48),
    z("I. Schutzbereich", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("1. Versammlung", K2, 250, "k1a", size=36, rechts=1820),
    z("2. friedlich und ohne Waffen: Unfriedlichkeit Einzelner schadet den übrigen nicht", K2, 305, "k1b", size=34, rechts=1820),
    z("II. Eingriff: Verbot oder Auflösung", K1, 385, "k2", "Bold", 38, rechts=1820),
    z("III. Rechtfertigung", K1, 465, "k3", "Bold", 38, rechts=1820),
    z("1. Schranke: Art. 8 II GG", K2, 525, "k3a", size=36, rechts=1820),
    z("2. § 15 I VersG: unmittelbare Gefährdung aus erkennbaren Umständen", K2, 585, "k3b", size=36, rechts=1820),
    z("3. Auflagen vor Verbot", K2, 645, "k3c", size=36, rechts=1820),
    z("fehlende Anmeldung allein genügt nicht", K3, 705, "k3d", size=34, rechts=1820),
    z("Kooperation der Behörde", K3, 760, "k3e", size=34, rechts=1820),
])

# T Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine Demonstration zu verbieten,", 0)], [("ist das ", 0), ("letzte Mittel.", "a")]],
                750, 310, 50, "merke", {"a": beim("merke", "letzte")}),
    *markertext([[("Unfriedliche Einzelne nehmen der", 0)], [("friedlichen Mehrheit", "b"), (" den Schutz", 0)],
                 [("von Art. 8 GG nicht.", 0)]], 750, 540, 46, "m2",
                {"b": beim("m2", "friedlichen")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
