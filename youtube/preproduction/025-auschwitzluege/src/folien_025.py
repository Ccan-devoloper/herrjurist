"""Folge 025 · Auschwitzlüge: Warum sie nicht von der Meinungsfreiheit geschützt ist – Serienstandard Open Peeps (Katzenkönig).
Echter Fall sachlich nacherzählt (BVerfGE 90, 241 – 1 BvR 23/94, Beschl. v. 13.4.1994); Figuren fiktiv, Veranstalter, Redner,
Richter und Politiker treten nicht auf und werden nicht genannt. Würde und Zurückhaltung: keine leugnende Aussage im Wortlaut,
keine NS-Symbole, keine Lager- oder Opferbilder; ruhige Saal-, Behörden- und Tafelbilder.
Szenen laut ../SZENENPLAN.md: A Die Einladung (Saal), B Die Auflage (Versammlungsbehörde), C Der Weg nach Karlsruhe,
D Sachverhalt, E Maßstab, F Wortlaut Art. 5 I 1 GG, G Meinung, H Tatsachenbehauptung, I Tatsache und Wertung verbunden,
J Subsumtion, K Gegenbeispiel Kriegsschuld, L Hilfsweise/Eingriff, M Wortlaut Art. 5 II GG, N § 5 Nr. 4 VersG,
O Persönliche Ehre, P Abwägung, Q Ergebnis, R Wortlaut § 130 III StGB, S Wunsiedel-Ausnahme, T Klausurtipp (Lexi),
U Klausurschema, V Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Stempel, Umschlag; Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_025/"
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return e.x + xs[i], e.y + int(h * 0.40) + ys[i]


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_025/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte (wie Folge 019): Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Eigene Hilfsfunktion (wie Folge 012/018): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause. redet_020() kürzt jedes Wortende auf
# das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende (siehe oben); Viseme aus der Schreibung geschätzt."""
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




BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
P1 = "Fall"
PS_ = "Art. 5 I GG › I. Schutzbereich"
PR_ = "Art. 5 I GG › III. Rechtfertigung"

# A Fall: die Einladung (Saal) ----------------------------------------------------------------------------------------
STUEHLE = [(260 + 125 * i, BODEN - 2) for i in range(6)]
folie([(NULL, f"{P1} · Die Einladung")], [
    hart(pl("München, Frühjahr 1991", 70, 40, NULL, fill=GELB, size=44)),
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    *[ficon("tabler", "armchair", x, u, 110, NULL, fuell=LILA, anim="cut") for x, u in STUEHLE],
    ficon("tabler", "presentation", 1130, BODEN - 2, 190, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "door", 120 + 30, BODEN - 2, 150, NULL, fuell=ORANGE, anim="cut"),
    pl("Saal", 570, 680, beim("einl", "Saal"), fill=WEISS, size=34, anker="m"),
    pl("Parteiverband", 600, 230, beim("einl", "Parteiverband"), fill=BLAU, size=36, anker="m"),
    ficon("tabler", "mail-opened", 600, 470, 150, beim("einl", "lädt"), fuell=WEISS),
    pl("Einladung zur Versammlung", 600, 490, beim("einl", "lädt"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "building-bank", 1620, BODEN - 2, 260, beim("erwart", "Stadt"), fuell=GRAU),
    pl("Stadt München", 1620, BODEN + 22, beim("erwart", "Stadt"), fill=GRAU, size=30, anker="m"),
    pl("erwartet:", 1620, 300, beim("erwart", "erwartet"), fill=WEISS, size=32, anker="m"),
    pl("Leugnung der Judenverfolgung", 1450, 390, beim("erwart", "Judenverfolgung"), fill=ROT, size=32, anker="m"),
])

# B Fall: die Auflage (Versammlungsbehörde) -----------------------------------------------------------------------------
MOX, SVX = 1000, 1560
MOb = ("MO_redet_r", MOX, BODEN, FH)
SVb = ("SV_redet", SVX, BODEN, FH)
AK = (70, 130, 600, 640)                     # Auflagenkarte (x, y, w, h)
stempel = bewegt(ficon("tabler", "rubber-stamp", 560, 235, 100, beim("m1", "Auflage"), fuell=ROT),
                 beim("m1", "Auflage"), (beim("m1", "Auflage")[0], beim("m1", "Auflage")[1] + 0.45), 0, -160)
folie([("moeller", f"{P1} · Die Auflage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "moeller", breite=7, farbe=INK),
    ficon("tabler", "table", 1280, BODEN - 2, 280, "moeller", fuell=ORANGE),
    ficon("tabler", "files", 1230, BODEN - 175, 90, "moeller", fuell=WEISS),
    ficon("tabler", "lamp", 1350, BODEN - 175, 100, "moeller", fuell=GELB),
    *fig("MO", MOX, BODEN, FH, [("moeller", "ruhig_r")], bis="m1"),
    *redet("MO_redet_r", MOX, BODEN, FH, "m1", "auflage"),
    peep_voll("MO_ernst_r", MOX, BODEN, FH, "auflage", anim="cut", bis="s1"),
    peep_voll("MO_ruhig_r", MOX, BODEN, FH, "s1", anim="cut"),
    pl("Herr Möller, Versammlungsbehörde", MOX, BODEN + 22, beim("moeller", "Möller"), fill=BLAU, size=28, anker="m"),
    *fig("SV", SVX, BODEN, FH, [("moeller", "ruhig"), ("auflage", "denkt")], bis="s1", d=0.1),
    *redet("SV_redet", SVX, BODEN, FH, "s1", "klage"),
    pl("Svenja, Referendarin", SVX, BODEN + 22, beim("moeller", "Svenja"), fill=ORANGE, size=28, anker="m"),
    blase("sprech", 760, 270, "m1", 1060, 190, inhalt=["Wir erteilen eine Auflage.", "Auf der Versammlung darf die",
          "Judenverfolgung nicht geleugnet werden."], textsize=32, figur=MOb, bis="auflage"),
    karte(*AK, beim("m1", "Auflage"), fill=PAPIER),
    titel(glyphen("Auflage"), 110, 165, beim("m1", "Auflage"), 46),
    szene(stempel, "025stempel*", 1.0, versatz=0.45 - 0.11),
    z("Judenverfolgung nicht leugnen", 110, 270, beim("m1", "Judenverfolgung"), "Bold", 30, rechts=650),
    z("zu Beginn auf die Strafbarkeit", 110, 350, beim("auflage", "Beginn"), size=30, rechts=650),
    z("hinweisen", 110, 392, beim("auflage", "Strafbarkeit"), size=30, rechts=650),
    z("solche Beiträge sofort unterbinden", 110, 470, beim("auflage", "solche"), size=30, rechts=650),
    z("notfalls die Versammlung auflösen", 110, 550, beim("auflage", "notfalls"), size=30, rechts=650),
    zit("nach BVerfGE 90, 241 (242) · Rn. 4", 110, 690, beim("auflage", "auflösen")),
    blase("sprech", 790, 270, "s1", 1180, 190, inhalt=["Darf der Staat vorschreiben, was", "auf einer Versammlung gesagt wird?",
          "Es gibt doch die Meinungsfreiheit."], textsize=32, figur=SVb, bis="klage"),
])

# C Fall: der Weg nach Karlsruhe ----------------------------------------------------------------------------------------
INST = [(260, BODEN - 2), (500, BODEN - 82), (740, BODEN - 162)]
brief = bewegt(ficon("tabler", "file-text", 1330, 600, 100, "vb", fuell=WEISS), "vb", ("vb", 0.9), -480, -40)
folie([("klage", f"{P1} · Der Weg nach Karlsruhe"), ("frage", f"{P1} · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Die Versammlung findet statt.", 70, 40, "klage", fill=GELB, size=36),
    *[e for i, (x, u) in enumerate(INST) for e in (
        linienzug([(x - 110, u), (x + 110, u)], beim("klage", "klagt"), breite=7, farbe=INK),
        ficon("tabler", "building-bank", x, u - 4, 170, beim("klage", "klagt"), fuell=GRAU, d=0.15 * i),
        bis_(kreuz_i(x + 70, u - 190, beim("klage", "erfolglos"), gr=30, d=0.12 * i), None))],
    pl("drei Instanzen", 500, 330, beim("klage", "drei"), fill=WEISS, size=32, anker="m"),
    ficon(HC, "classical-building", 1330, BODEN - 2, 280, "vb", fuell=WEISS),
    pl("Bundesverfassungsgericht", 1330, BODEN + 22, "vb", fill=WEISS, size=28, anker="m"),
    szene(brief, "025brief*", 1.0, versatz=0.2),
    pl("Verfassungsbeschwerde", 1330, 450, beim("vb", "Verfassungsbeschwerde"), fill=GELB, size=32, anker="m"),
    *fig("SV", 1730, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    pl("Verletzt die Auflage die Meinungsfreiheit?", 760, 140, beim("frage", "Verletzt"), fill=PINK, size=36, anker="m"),
    pl("Ist die sogenannte Auschwitzlüge überhaupt eine Meinung?", 760, 230, beim("frage", "Und"), fill=PINK, size=36,
       anker="m"),
])

# D Sachverhalt ---------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frühjahr 1991: Ein Parteiverband lädt zu einer Versammlung in einem Saal in München ein. Nach der Einladung und dem "
    "angekündigten Redner erwartet die Stadt als Versammlungsbehörde, dass dort die Judenverfolgung im Dritten Reich "
    "geleugnet wird. Sie erteilt eine Auflage: Der Verband muss dafür sorgen, dass die Judenverfolgung auf der "
    "Versammlung nicht geleugnet oder bezweifelt wird, zu Beginn auf die Strafbarkeit hinweisen, solche Beiträge sofort "
    "unterbinden und notfalls die Versammlung unterbrechen oder auflösen (§ 5 Nr. 4 VersG). Die Versammlung findet statt. "
    "Die Klage des Verbands bleibt in drei Instanzen ohne Erfolg; er erhebt Verfassungsbeschwerde.",
    "(Nach BVerfGE 90, 241 – 1 BvR 23/94. Herr Möller und Svenja sind erfunden; Veranstalter und Redner werden nicht genannt.)",
], "Verletzt die Auflage die Meinungsfreiheit (Art. 5 I 1 GG)?")

# E Maßstab ---------------------------------------------------------------------------------------------------------------
folie([("mass", "Maßstab: Art. 5 I GG, nicht Art. 8 GG")], rechts_frei([
    *tafel("mass", "Maßstab"),
    ok(140, 215, beim("mass", "Meinungsfreiheit"), gr=22),
    z("vorrangig: Meinungsfreiheit, Art. 5 I GG", 185, 195, beim("mass", "Meinungsfreiheit"), "Bold", 36),
    nein(140, 300, beim("mass", "Versammlungsfreiheit"), gr=20),
    z("nicht: Versammlungsfreiheit, Art. 8 GG", 185, 280, beim("mass", "Versammlungsfreiheit"), size=36),
    z("denn die Auflage betrifft", 110, 400, "gegenst", size=36),
    z("bestimmte Äußerungen", 110, 455, beim("gegenst", "bestimmte"), "Bold", 36),
    zit("BVerfGE 90, 241 (246) · Rn. 25", 110, 540, beim("gegenst", "Äußerungen")),
    ficon("tabler", "users-group", IX, IU, 150, "mass", fuell=GRUEN, bis="gegenst"),
    ficon("tabler", "message-circle", IX, IU, 130, "gegenst", fuell=WEISS),
    *fig("SV", FX, FB, FR, [("mass", "ruhig")]),
    pl("Svenja", FX, FB + 22, "mass", fill=ORANGE, size=28, anker="m", d=0.2),
]))

# F Wortlaut Art. 5 I 1 GG --------------------------------------------------------------------------------------------------
W5 = ["„Jeder hat das Recht, seine Meinung in Wort,", "Schrift und Bild frei zu äußern und zu", "verbreiten …“"]
w5_els, w5_y = wortlaut(80, 220, 1100, W5, "Art. 5 Abs. 1 Satz 1 GG", "wl5", marken=[
    (0, "Jeder", beim("wl5", "Jeder")), (0, "seine Meinung", beim("wl5", "seine")), (0, "Wort,", beim("wl5", "Wort")),
    (1, "Schrift", beim("wl5", "Schrift")), (1, "Bild", beim("wl5", "Bild")), (1, "äußern", beim("wl5", "äußern")),
    (2, "verbreiten", beim("wl5", "verbreiten"))], size=40)
folie([("wl5", "Art. 5 I GG › Wortlaut")], rechts_frei([
    titel(glyphen("Der Wortlaut"), 110, 90, "wl5", 50),
    *w5_els,
    ficon("tabler", "book", IX, IU, 140, "wl5", fuell=GELB),
    *fig("SV", FX, FB, FR, [("wl5", "ruhig")]),
]))

# G I. Schutzbereich: Meinung ------------------------------------------------------------------------------------------------
folie([("sb", PS_), ("meinung", f"{PS_} › Meinung")], rechts_frei([
    *tafel("sb", "I. Schutzbereich"),
    z("Meinung: Stellungnahme und Dafürhalten", 110, 200, beim("meinung", "Stellungnahme"), "Bold", 38),
    z("nicht als wahr oder unwahr erweisbar", 150, 270, beim("meinung", "lassen"), size=36),
    z("geschützt, ob", 110, 380, "egal", "Bold", 36),
    *plusminus("begründet oder grundlos", 150, 445, beim("egal", "begründet"), True, size=36),
    *plusminus("wertvoll oder wertlos", 150, 505, beim("egal", "wertvoll"), True, size=36),
    zit("BVerfGE 90, 241 (247) · Rn. 26", 110, 590, beim("egal", "wertlos")),
    ficon("tabler", "message-circle", IX, IU, 140, "meinung", fuell=GELB),
    *fig("SV", FX, FB, FR, [("sb", "ruhig"), ("egal", "froh")]),
]))

# H I. Schutzbereich: Tatsachenbehauptung -------------------------------------------------------------------------------------
folie([("tats", f"{PS_} › Tatsachenbehauptung"), ("grenze", f"{PS_} › erwiesen unwahre Tatsachen")], rechts_frei([
    *tafel("tats", "Tatsachenbehauptung"),
    z("auf ihren Wahrheitsgehalt prüfbar", 110, 195, beim("tats", "lassen"), "Bold", 36),
    ok(140, 285, "vor", gr=22),
    z("geschützt, soweit Voraussetzung", 185, 265, "vor", size=34),
    z("für die Bildung von Meinungen", 185, 315, beim("vor", "Bildung"), size=34),
    blk(110, 400, 1040, 90, ROT, beim("grenze", "bewusst"), [("bewusst oder erwiesen unwahr: nicht geschützt", "ExtraBold", 34, INK)]),
    z("unrichtige Information: kein schützenswertes Gut", 110, 530, beim("grenze", "Unrichtige"), size=34),
    z("aber: Wahrheitspflicht nicht überspannen", 110, 620, "pflicht", "Bold", 34),
    zit("BVerfGE 90, 241 (247 f.) · Rn. 27 f.", 110, 700, beim("pflicht", "überspannen")),
    ficon("tabler", "search", IX, IU, 130, "tats", fuell=WEISS, bis="vor"),
    ficon("tabler", "bulb", IX, IU, 120, "vor", fuell=GELB, bis="grenze"),
    ficon("tabler", "ban", IX, IU, 120, beim("grenze", "bewusst"), fuell=ROT, bis="pflicht"),
    ficon("tabler", "scale", IX, IU, 150, "pflicht", fuell=GELB),
    *fig("MO", FX, FB, FR, [("tats", "ruhig"), ("grenze", "ernst")]),
    pl("Herr Möller", FX, FB + 22, "tats", fill=BLAU, size=28, anker="m", d=0.2),
]))

# I Tatsache und Wertung verbunden ---------------------------------------------------------------------------------------------
folie([("misch", f"{PS_} › Tatsache und Wertung verbunden")], rechts_frei([
    *tafel("misch", "Tatsache und Wertung"),
    pl("Tatsache", 160, 200, beim("misch", "Tatsache"), fill=BLAU, size=36),
    z("+", 470, 200, beim("misch", "Wertung"), "ExtraBold", 44),
    pl("Wertung", 560, 200, beim("misch", "Wertung"), fill=GELB, size=36),
    z("trennen nur, wenn der Sinn", 110, 340, "trenn", "Bold", 36),
    z("der Äußerung nicht verfälscht wird", 110, 395, beim("trenn", "nicht"), "Bold", 36),
    blk(110, 490, 1040, 90, GELB, "ganz", [("sonst: die ganze Äußerung als Meinung", "ExtraBold", 36, INK)]),
    zit("BVerfGE 90, 241 (248) · Rn. 29", 110, 640, beim("ganz", "Meinung")),
    ficon("tabler", "puzzle", IX, IU, 140, "misch", fuell=LILA),
    *fig("SV", FX, FB, FR, [("misch", "denkt")]),
]))

# J Subsumtion: Leugnung der Judenverfolgung ------------------------------------------------------------------------------------
folie([("subs", f"{PS_} › Leugnung der Judenverfolgung")], rechts_frei([
    *tafel("subs", "Und hier?"),
    z("Leugnung der Judenverfolgung:", 110, 195, beim("subs", "Wer"), "Bold", 36),
    z("eine Tatsachenbehauptung", 150, 250, beim("subs", "Tatsachenbehauptung"), size=36),
    z("erwiesen unwahr:", 110, 335, "belegt", "Bold", 36),
    z("– ungezählte Augenzeugenberichte und Dokumente", 150, 395, "b1", size=34),
    z("– Feststellungen der Gerichte", 150, 450, "b2", size=34),
    z("– Erkenntnisse der Geschichtswissenschaft", 150, 505, "b3", size=34),
    blk(110, 580, 1040, 90, ROT, "nicht", [("für sich genommen: nicht geschützt", "ExtraBold", 36, INK)]),
    nein(1110, 625, beim("nicht", "nicht", nr=1), gr=22),
    zit("BVerfGE 90, 241 (249 f.) · Rn. 34", 110, 715, beim("nicht", "nicht", nr=1)),
    ficon("tabler", "files", IX, IU, 130, "b1", fuell=WEISS, bis="b2"),
    ficon("tabler", "gavel", IX, IU, 130, "b2", fuell=GELB, bis="b3"),
    ficon("tabler", "books", IX, IU, 130, "b3", fuell=BLAU),
    *fig("SV", FX, FB, FR, [("subs", "ernst")]),
]))

# K Gegenbeispiel: Kriegsschuld --------------------------------------------------------------------------------------------------
folie([("schuld", f"{PS_} › Gegenbeispiel: Schuldfragen")], rechts_frei([
    *tafel("schuld", "Gegenbeispiel"),
    z("Schuld am Zweiten Weltkrieg?", 110, 195, beim("schuld", "Schuld"), "Bold", 38),
    z("Urteile über Schuld und Verantwortung:", 150, 270, beim("schuld", "Urteile"), size=34),
    z("komplexe Beurteilungen", 150, 325, beim("schuld", "komplexe"), "Bold", 36),
    z("ein Ereignis selbst leugnen:", 110, 430, "ereig", "Bold", 38),
    z("in aller Regel eine Tatsache", 150, 495, beim("ereig", "aller"), size=36),
    zit("BVerfGE 90, 241 (249 f.) · Rn. 34; vgl. BVerfGE 90, 1", 110, 580, beim("ereig", "Tatsache")),
    ficon("tabler", "scale", IX, IU, 150, "schuld", fuell=GELB, bis="ereig"),
    ficon("tabler", "calendar", IX, IU, 120, "ereig", fuell=WEISS),
    *fig("MO", FX, FB, FR, [("schuld", "denkt")]),
]))

# L Hilfsweise: Schutz im Zusammenhang, II. Eingriff --------------------------------------------------------------------------------
folie([("hilfs", f"{PS_} › hilfsweise: im Zusammenhang geschützt"), ("ein", "Art. 5 I GG › II. Eingriff")], rechts_frei([
    *tafel("hilfs", "Hilfsweise"),
    z("im Zusammenhang mit dem Versammlungsthema:", 110, 195, beim("hilfs", "Im"), "Bold", 34),
    z("Teil einer Meinung", 150, 255, beim("hilfs", "Teil"), size=36),
    ok(140, 340, beim("hilfs", "geschützt"), gr=22),
    z("dann geschützt", 185, 320, beim("hilfs", "geschützt"), "Bold", 36),
    blk(110, 420, 1040, 90, BLAU, "ein", [("II. Eingriff: die Auflage", "ExtraBold", 38, INK)]),
    ok(1110, 465, beim("ein", "Eingriff"), gr=22),
    zit("BVerfGE 90, 241 (250) · Rn. 35", 110, 560, beim("ein", "Eingriff")),
    ficon("tabler", "message-circle", IX, IU, 130, "hilfs", fuell=GELB, bis="ein"),
    ficon("tabler", "clipboard-text", IX, IU, 120, "ein", fuell=WEISS),
    *fig("SV", FX, FB, FR, [("hilfs", "denkt"), ("ein", "ruhig")]),
]))

# M Wortlaut Art. 5 II GG --------------------------------------------------------------------------------------------------------
W52 = ["„Diese Rechte finden ihre Schranken in den", "Vorschriften der allgemeinen Gesetze, den",
       "gesetzlichen Bestimmungen zum Schutze der", "Jugend und in dem Recht der persönlichen Ehre.“"]
w52_els, w52_y = wortlaut(80, 220, 1100, W52, "Art. 5 Abs. 2 GG", "wl52", marken=[
    (0, "Schranken", beim("wl52", "Schranken")), (1, "allgemeinen Gesetze", beim("wl52", "allgemeinen")),
    (2, "Schutze der", beim("wl52", "Schutze")), (3, "Jugend", beim("wl52", "Schutze")),
    (3, "Recht der persönlichen Ehre", beim("wl52", "Recht", nr=2))], size=38)
folie([("wl52", "Art. 5 I GG › III. Rechtfertigung › Wortlaut Art. 5 II GG")], rechts_frei([
    titel(glyphen("III. Rechtfertigung"), 110, 90, "wl52", 50),
    *w52_els,
    ficon("tabler", "book", IX, IU, 140, "wl52", fuell=GELB),
    *fig("MO", FX, FB, FR, [("wl52", "ruhig")]),
]))

# N Gesetzliche Grundlage: § 5 Nr. 4 VersG ------------------------------------------------------------------------------------------
folie([("grundl", f"{PR_} › Grundlage: § 5 Nr. 4 VersG")], rechts_frei([
    *tafel("grundl", "Gesetzliche Grundlage"),
    z("§ 5 Nr. 4 Versammlungsgesetz", 110, 190, beim("grundl", "Paragraf"), "Bold", 38),
    z("Versammlung in geschlossenen Räumen:", 110, 270, beim("vers", "Versammlung"), size=34),
    z("Verbot, wenn Äußerungen drohen, die als", 150, 325, beim("vers", "verboten"), size=34),
    z("Straftat von Amts wegen verfolgt werden", 150, 375, beim("vers", "Straftat"), size=34),
    z("Auflage = das mildere Mittel", 150, 440, beim("vers", "Auflage"), "Bold", 34),
    z("vorbeugend:", 110, 530, "streng", "Bold", 36),
    z("– strenge Gefahrenprognose", 150, 590, beim("streng", "strenge"), size=34),
    z("– zweifelsfreie Strafbarkeit", 150, 645, beim("streng", "zweifelsfreie"), size=34),
    zit("BVerfGE 90, 241 (250 f.) · Rn. 6, 37–39", 110, 720, beim("streng", "Strafbarkeit")),
    ficon("tabler", "armchair", IX, IU, 120, "vers", fuell=LILA, bis="streng"),
    ficon("tabler", "search", IX, IU, 120, "streng", fuell=WEISS),
    ficon("tabler", "file-certificate", IX, IU, 130, "grundl", fuell=WEISS, bis="vers"),
    *fig("MO", FX, FB, FR, [("grundl", "ernst")]),
]))

# O Recht der persönlichen Ehre: § 185 StGB -------------------------------------------------------------------------------------------
folie([("ehre", f"{PR_} › Schranke: persönliche Ehre, § 185 StGB")], rechts_frei([
    *tafel("ehre", "Recht der persönlichen Ehre"),
    z("§ 185 StGB: Beleidigung", 110, 190, beim("ehre", "Beleidigung"), "Bold", 38),
    z("in Deutschland lebende Juden:", 110, 280, beim("gruppe", "Deutschland"), size=34),
    z("beleidigungsfähige Gruppe", 150, 330, beim("gruppe", "beleidigungsfähige"), "Bold", 34),
    z("Leugnung ihres Verfolgungsschicksals", 110, 420, "wuerde", size=34),
    z("greift Achtungsanspruch und", 150, 470, beim("wuerde", "Achtungsanspruch"), size=34),
    z("Menschenwürde an", 150, 520, beim("wuerde", "Menschenwürde"), "Bold", 34),
    z("kein Strafantrag nötig (§ 194 I 2 StGB)", 110, 610, "antrag", size=34),
    zit("BVerfGE 90, 241 (251–253) · Rn. 40–46, 52", 110, 690, beim("antrag", "nicht")),
    ficon("tabler", "shield-check", IX, IU, 130, "ehre", fuell=GRUEN, bis="gruppe"),
    ficon("tabler", "users-group", IX, IU, 160, "gruppe", fuell=BLAU),
    *fig("SV", FX, FB, FR, [("ehre", "ernst")]),
]))

# P Abwägung ---------------------------------------------------------------------------------------------------------------------
folie([("abw", f"{PR_} › Abwägung")], rechts_frei([
    *tafel("abw", "Abwägung"),
    z("Tatsachenkern erwiesen unwahr", 110, 190, beim("leicht", "Tatsachenkern"), "Bold", 36),
    z("Eingriff wiegt nicht besonders schwer", 150, 250, beim("leicht", "wiegt"), size=34),
    blk(110, 320, 1040, 90, GRUEN, beim("leicht", "Persönlichkeitsschutz"), [("Persönlichkeitsschutz geht vor", "ExtraBold", 38, INK)]),
    z("Vermutung für die freie Rede bei Fragen,", 110, 460, "verm", size=34),
    z("die die Öffentlichkeit wesentlich berühren", 110, 510, beim("verm", "Öffentlichkeit"), size=34),
    nein(140, 615, beim("vnicht", "nicht"), gr=20),
    z("greift nicht bei kränkenden Äußerungen", 185, 595, beim("vnicht", "nicht"), size=34),
    z("auf erwiesen unwahrer Tatsachengrundlage", 185, 645, beim("vnicht", "erwiesen"), size=34),
    zit("BVerfGE 90, 241 (253 f.) · Rn. 48–50", 110, 720, beim("vnicht", "beruhen")),
    ficon("tabler", "scale", IX, IU, 170, "abw", fuell=GELB),
    *fig("MO", FX, FB, FR, [("abw", "ruhig"), ("verm", "denkt"), ("vnicht", "ernst")]),
]))

# Q Ergebnis ---------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Beschluss vom 13.4.1994")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 90, GRUEN, "erg", [("Beschluss vom 13.4.1994", "ExtraBold", 38, INK)]),
    z("Verfassungsbeschwerde verworfen:", 110, 330, beim("erg", "verwirft"), "Bold", 36),
    z("offensichtlich unbegründet", 150, 390, beim("erg", "offensichtlich"), size=36),
    z("Zulässigkeit offen gelassen", 110, 480, "offen", size=36),
    zit("BVerfGE 90, 241 · 1 BvR 23/94 · Tenor, Rn. 22", 110, 560, beim("offen", "offen", nr=1)),
    ficon(HC, "classical-building", IX, IU, 180, "erg", fuell=WEISS),
    ficon("tabler", "gavel", IX + 170, IU, 100, beim("erg", "verwirft"), fuell=GELB),
    *fig("SV", FX, FB, FR, [("erg", "ruhig")]),
]))

# R Rechtslage heute: Wortlaut § 130 III StGB ----------------------------------------------------------------------------------------
W130 = ["„Mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe", "wird bestraft, wer eine unter der Herrschaft des",
        "Nationalsozialismus begangene Handlung der in § 6 Abs. 1", "des Völkerstrafgesetzbuches bezeichneten Art in einer",
        "Weise, die geeignet ist, den öffentlichen Frieden zu", "stören, öffentlich oder in einer Versammlung billigt,",
        "leugnet oder verharmlost.“"]
w130_els, w130_y = wortlaut(80, 190, 1100, W130, "§ 130 Abs. 3 StGB (Völkermord: § 6 Abs. 1 VStGB)", "heute", marken=[
    (2, "§ 6 Abs. 1", beim("wl130", "Völkermord")), (1, "Herrschaft des", beim("wl130", "Herrschaft")),
    (2, "Nationalsozialismus", beim("wl130", "Herrschaft")),
    (5, "öffentlich", beim("wl130", "öffentlich")), (5, "Versammlung", beim("wl130", "Versammlung")),
    (5, "billigt,", beim("wl130", "billigt")), (6, "leugnet", beim("wl130", "leugnet")),
    (6, "verharmlost", beim("wl130", "verharmlost")), (4, "geeignet ist, den öffentlichen Frieden zu", beim("wl130", "geeignet"))],
    size=33)
folie([("heute", "Rechtslage heute › § 130 III StGB")], rechts_frei([
    titel(glyphen("Heute: § 130 Abs. 3 StGB"), 110, 90, "heute", 50),
    *w130_els,
    ficon("tabler", "book", IX, IU, 140, "heute", fuell=GELB),
    *fig("SV", FX, FB, FR, [("heute", "ruhig")]),
]))

# S Wunsiedel-Ausnahme -----------------------------------------------------------------------------------------------------------
PH = "Rechtslage heute › § 130 III StGB"
folie([("sonder", f"{PH} › kein allgemeines Gesetz"), ("wuns", f"{PH} › Wunsiedel-Ausnahme"),
       ("frieden", f"{PH} › Gefahr für den öffentlichen Frieden")], rechts_frei([
    *tafel("sonder", "Kein allgemeines Gesetz"),
    nein(140, 210, beim("sonder", "allgemeines"), gr=20),
    z("§ 130 III StGB: kein allgemeines Gesetz", 185, 190, beim("sonder", "allgemeines"), "Bold", 34),
    z("erfasst nur Äußerungen zum Nationalsozialismus", 185, 240, beim("sonder", "erfasst"), size=32),
    blk(110, 310, 1040, 80, BLAU, beim("wuns", "Wunsiedel"), [("Wunsiedel-Ausnahme", "ExtraBold", 36, INK)]),
    z("zunächst für § 130 IV StGB (BVerfGE 124, 300)", 150, 415, beim("wuns", "zunächst"), size=32),
    z("2018 auch für § 130 III StGB (Kammer)", 150, 465, "kammer", size=32),
    nein(140, 560, beim("geist", "allein"), gr=20),
    z("kein Verbot allein wegen geistiger Wirkung", 185, 540, beim("geist", "allein"), size=32),
    ok(140, 625, beim("frieden", "öffentlichen"), gr=20),
    z("nötig: Gefährdung des öffentlichen Friedens", 185, 605, beim("frieden", "öffentlichen"), size=32),
    z("bei Leugnung in der Regel indiziert", 185, 660, beim("frieden", "Leugnung"), "Bold", 32),
    zit("BVerfGE 124, 300 LS 1, 2, Rn. 61, 64 · BVerfG (K), 1 BvR 2083/15 Rn. 21", 110, 735, beim("frieden", "indiziert")),
    zit("BVerfG (K), 1 BvR 673/18 Rn. 23 f., 31, 33", 110, 775, beim("frieden", "indiziert")),
    ficon("tabler", "file-text", IX, IU, 120, "sonder", fuell=WEISS, bis="wuns"),
    ficon(HC, "classical-building", IX, IU, 170, "wuns", fuell=WEISS, bis="frieden"),
    ficon("tabler", "shield-check", IX, IU, 130, "frieden", fuell=GRUEN),
    *fig("MO", FX, FB, FR, [("sonder", "ruhig"), ("geist", "ernst")]),
]))

# T Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Tatsache oder Meinung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Tatsache oder Meinung?", 200, 200, beim("tipp", "Ob"), "Bold", 36),
    z("am Gesamtkontext der Äußerung", 200, 255, beim("tipp", "Gesamtkontext"), size=34),
    z("Schutzbereich nur für die erwiesen", 200, 350, "tipp1", "Bold", 36),
    z("unwahre Tatsache selbst verneinen", 200, 405, beim("tipp1", "unwahre"), "Bold", 36),
    z("nicht sauber trennbar:", 200, 500, "tipp2", size=34),
    z("weiter die Rechtfertigung prüfen", 200, 555, beim("tipp2", "prüfst"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# U Klausurschema ----------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Meinungsfreiheit, Art. 5 I 1 GG"), 110, 90, "sch", 48),
    z("I. Schutzbereich", K1, 195, "k1", "Bold", 38, rechts=1820),
    z("1. Meinung oder Tatsachenbehauptung (Gesamtkontext)", K2, 260, "k1a", size=36, rechts=1820),
    z("2. erwiesen unwahre Tatsache: nicht geschützt", K2, 320, "k1b", size=36, rechts=1820),
    z("3. untrennbar mit Wertung verbunden: insgesamt Meinung", K2, 380, "k1c", size=36, rechts=1820),
    z("II. Eingriff", K1, 460, "k2", "Bold", 38, rechts=1820),
    z("III. Rechtfertigung", K1, 540, "k3", "Bold", 38, rechts=1820),
    z("1. Schranke aus Art. 5 II GG", K2, 605, "k3a", size=36, rechts=1820),
    z("bei § 130 III StGB: Wunsiedel-Ausnahme", K3, 665, "k3b", size=34, rechts=1820),
    z("2. Abwägung im Einzelfall", K2, 735, "k3c", size=36, rechts=1820),
])

# V Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Meinungen schützt Art. 5 GG,", 0)], [("ob ", 0), ("wertvoll oder wertlos.", "a")]],
                750, 310, 50, "merke", {"a": beim("merke", "wertvoll")}),
    *markertext([[("Die ", 0), ("erwiesen unwahre", "b"), (" Tatsachenbehauptung", 0)],
                 [("selbst, wie die Leugnung des", 0)], [("Holocaust, schützt er nicht.", "c")]], 750, 540, 46, "m2",
                {"b": beim("m2", "erwiesen"), "c": beim("m2", "schützt")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
