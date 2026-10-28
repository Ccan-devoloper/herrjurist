"""Folge 020 · Grundrechtsprüfung Schema: Schutzbereich, Eingriff, Rechtfertigung – Serienstandard Open Peeps (Katzenkönig).
Frei erfundener Beispielfall (Skateverbot in der Fußgängerzone), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Fußgängerzone am Morgen, B Mittags (Beinahe-Zusammenstoß), C Das Verbot / Die Frage, D Sachverhalt, E Vorfragen,
F Wortlaut Art. 2 I GG, G I. Schutzbereich, H II. Eingriff (klassisch), I II. Eingriff (modern, Osho), J III. 1. Schranke,
K 2. Schranken-Schranken formell, L Zitiergebot (Wortlaut Art. 19 I GG), M Bestimmtheit, N Verhältnismäßigkeit,
O Angemessenheit, P Wesensgehalt (Wortlaut Art. 19 II GG) und Ergebnis, Q Gegenfall, R Klausurtipp (Lexi),
S Klausurschema, T Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (rollende Skateboards, Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_020/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_020/" in n:
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


def schild(cx, oben, cue, text="8–20 Uhr", breite=220, mit_pfosten=True, boden=None, bis=None):
    """Verbotsschild: Pfosten + weiße Tafel mit durchgestrichenem Skateboard (Tabler) und Uhrzeit."""
    els = []
    if mit_pfosten:
        els.append(bis_(linienzug([(cx, oben + 200), (cx, boden or BODEN)], cue, breite=10, farbe=INK), bis))
    els.append(bis_(karte(cx - breite // 2, oben, breite, 210, cue, fill=WEISS, rund=14, schatten=6, rand=5), bis))
    els.append(ficon("tabler", "skateboard-off", cx, oben + 140, 120, cue, fuell=ROT, bis=bis))
    t = z(text, 0, 0, cue, "ExtraBold", 32, rechts=engine.W)
    t.x, t.y, t.bis = cx - t.sprite.width / 2, oben + 145, bis
    els.append(t)
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270

# A Fall: Fußgängerzone am Morgen -------------------------------------------------------------------------------------
GA_X, GA_DX = 1350, 380
ROLL0, ROLL1 = ("fall", 0.6), "gudrun"
gu_a = bewegt(peep_voll("GU_froh", GA_X, BODEN - 34, FH, NULL, anim="cut"), ROLL0, ROLL1, GA_DX)
brett_a = bewegt(ficon("tabler", "skateboard", GA_X, BODEN - 2, 250, NULL, fuell=GELB, anim="cut"), ROLL0, ROLL1, GA_DX)
folie([(NULL, "Fall · In der Fußgängerzone")], [
    hart(pl("Montagmorgen", 70, 40, NULL, fill=GELB, size=48)),
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    ficon("tabler", "building-store", 260, BODEN - 2, 300, NULL, fuell=PINK, anim="cut"),
    ficon("tabler", "building-store", 640, BODEN - 2, 260, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "lamp", 900, BODEN - 2, 120, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "tree", 1060, BODEN - 2, 200, NULL, fuell=GRUEN, anim="cut"),
    ficon("tabler", "sun", 1740, 200, 120, NULL, fuell=GELB, anim="cut"),
    pl("Fußgängerzone", 450, 470, beim("fall", "Fußgängerzone"), fill=WEISS, size=34, anker="m"),
    gu_a, szene(brett_a, "020skateboard*", 1.0, versatz=T_(ROLL0)),
    pl("Gudrun, 60", GA_X, BODEN + 22, beim("gudrun", "Gudrun"), fill=ORANGE, size=30, anker="m"),
    pl("mit dem Skateboard", GA_X, 280, beim("gudrun", "Skateboard"), fill=GELB, size=32, anker="m"),
    ficon("tabler", "briefcase", 1700, 470, 110, beim("gudrun", "Arbeit"), fuell=ORANGE),
    pl("zur Arbeit", 1700, 490, beim("gudrun", "Arbeit"), fill=WEISS, size=30, anker="m"),
])

# B Fall: mittags, beinahe ein Zusammenstoß --------------------------------------------------------------------------
KR_X = 1350
KRb = ("KR_redet", KR_X, BODEN, FH)
skater1 = bewegt(ficon("tabler", "skateboarding", 900, BODEN - 2, 170, beim("mittag", "rollen"), fuell=ORANGE, spiegeln=True,
                       bis="krueger"), beim("mittag", "rollen"), beim("mittag", "vorbei", ende=True), 800)
skater2 = bewegt(ficon("tabler", "skateboarding", 1000, BODEN - 2, 170, beim("krueger", "kann"), fuell=BLAU, spiegeln=True),
                 beim("krueger", "kann"), beim("krueger", "ausweichen", ende=True), 800)
folie([("mittag", "Fall · Mittags in der Fußgängerzone")], [
    pl("Mittags: voll", 70, 40, "mittag", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "mittag", breite=7, farbe=INK),
    ficon("tabler", "building-store", 260, BODEN - 2, 300, "mittag", fuell=PINK),
    *[ficon("tabler", "walk", x, BODEN - 2, 120, beim("mittag", "voll"), fuell=f, d=0.12 * i)
      for i, (x, f) in enumerate(((470, GRUEN), (600, LILA), (730, BLAU)))],
    szene(skater1, "020vorbei*", 1.0),
    pl("knapp vorbei", 900, 560, beim("mittag", "knapp"), fill=ROT, size=32, anker="m", bis="krueger"),
    *fig("KR", KR_X, BODEN, FH, [("krueger", "ruhig_r"), (beim("krueger", "gerade"), "schreck_r")], bis="k1"),
    *redet("KR_redet", KR_X, BODEN, FH, "k1", "stadt"),
    pl("Frau Krüger", KR_X, BODEN + 22, beim("krueger", "Krüger"), fill=LILA, size=30, anker="m"),
    szene(skater2, "020vorbei*", 1.0),
    blase("sprech", 640, 200, "k1", 860, 250, inhalt=["Das war knapp! Hier gehen", "doch Kinder und alte Leute!"],
          textsize=34, figur=KRb),
])

# C Fall: das Verbot / die Frage ----------------------------------------------------------------------------------------
SX, BRX, GUX = 700, 1000, 1500
BRc = ("BR_redet_r", BRX, BODEN, FH)
GUc = ("GU_redet", GUX, BODEN, FH)
folie([("stadt", "Fall · Das Verbot"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "stadt", breite=7, farbe=INK),
    ficon("tabler", "building-bank", 240, BODEN - 2, 260, beim("stadt", "Stadt"), fuell=GRAU),
    pl("Stadt", 240, BODEN + 22, beim("stadt", "Stadt"), fill=GRAU, size=30, anker="m"),
    ficon("tabler", "file-text", 240, 520, 110, beim("stadt", "Verordnung"), fuell=WEISS),
    pl("Verordnung", 240, 540, beim("stadt", "Verordnung"), fill=WEISS, size=30, anker="m"),
    *schild(SX, 270, beim("brueckner", "Schild")),
    pl("Bußgeld", SX, 500, beim("b1", "Bußgeld"), fill=ROT, size=30, anker="m"),
    *fig("BR", BRX, BODEN, FH, [("brueckner", "ruhig_r")], bis="b1"),
    *redet("BR_redet_r", BRX, BODEN, FH, "b1", "g1"),
    peep_voll("BR_ruhig_r", BRX, BODEN, FH, "g1", anim="cut"),
    pl("Herr Brückner, Ordnungsamt", BRX, BODEN + 22, beim("brueckner", "Brückner"), fill=BLAU, size=28, anker="m"),
    *fig("GU", GUX, BODEN, FH, [("stadt", "ruhig"), ("b1", "schreck")], bis="g1"),
    *redet("GU_redet", GUX, BODEN, FH, "g1", "frage"),
    peep_voll("GU_denkt", GUX, BODEN, FH, "frage", anim="cut"),
    ficon("tabler", "skateboard", 1730, BODEN - 2, 170, "stadt", fuell=GELB),
    pl("Gudrun", GUX, BODEN + 22, "stadt", fill=ORANGE, size=30, anker="m", d=0.2),
    blase("sprech", 720, 230, "b1", 1270, 215, inhalt=["Ab sofort ist Skateboardfahren hier", "von 8 bis 20 Uhr verboten.",
                                                       "Wer es trotzdem tut, zahlt ein Bußgeld."], textsize=31, figur=BRc, bis="g1"),
    blase("sprech", 680, 190, "g1", 1220, 230, inhalt=["Skaten ist doch kein Verbrechen!", "Das ist meine Freiheit!"],
          textsize=33, figur=GUc, bis="frage"),
    pl("Verletzt das Verbot Gudrun in ihren Grundrechten?", 1060, 50, beim("frage", "Verletzt"), fill=PINK, size=38, anker="m"),
    pl("Schutzbereich", 760, 150, beim("frage", "Schutzbereich"), fill=GELB, size=32, anker="m"),
    pl("Eingriff", 1060, 150, beim("frage", "Eingriff"), fill=GELB, size=32, anker="m"),
    pl("Rechtfertigung", 1360, 150, beim("frage", "Rechtfertigung"), fill=GELB, size=32, anker="m"),
])

# D Sachverhalt --------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Gudrun (60) fährt jeden Morgen mit ihrem Skateboard durch die Fußgängerzone ihrer Stadt zur Arbeit. Mittags ist "
    "die Fußgängerzone voll; immer wieder rollen Skater knapp an Fußgängern vorbei, Frau Krüger kann gerade noch "
    "ausweichen. Die Stadt erlässt daraufhin eine Verordnung: In der Fußgängerzone ist Skateboardfahren von 8 bis 20 Uhr "
    "verboten, Verstöße kosten ein Bußgeld. Herr Brückner vom Ordnungsamt hängt das Schild auf. Gudrun meint: „Skaten "
    "ist doch kein Verbrechen! Das ist meine Freiheit!“",
    "Annahmen: Die Verordnung beruht auf einer wirksamen landesrechtlichen Grundlage und ist formell rechtmäßig. Gudrun "
    "skatet nicht beruflich und will nicht demonstrieren. (Fall und Personen sind erfunden.)",
], "Verletzt das Verbot Gudrun in ihren Grundrechten?")

# E Vorfragen ----------------------------------------------------------------------------------------------------------
folie([("bind", "Vorfrage › Grundrechtsbindung, Art. 1 III GG"), ("welches", "Vorfrage › Welches Grundrecht passt?"),
       ("auffang", "Vorfrage › Art. 2 I GG, allgemeine Handlungsfreiheit")], rechts_frei([
    *tafel("bind", "Vorfragen"),
    z("Die Stadt ist an die Grundrechte gebunden", 110, 190, "bind", "Bold", 36),
    ok(140, 285, beim("bind", "Absatz"), gr=22),
    z("auch die vollziehende Gewalt, Art. 1 III GG", 185, 265, beim("bind", "vollziehende"), size=34),
    z("Welches Grundrecht passt?", 110, 360, "welches", "Bold", 36),
    nein(140, 450, beim("welches", "beruflich"), gr=20),
    z("skatet nicht beruflich (Art. 12 GG)", 185, 430, beim("welches", "beruflich"), size=34),
    nein(140, 515, beim("welches", "demonstrieren"), gr=20),
    z("will nicht demonstrieren (Art. 8 GG)", 185, 495, beim("welches", "demonstrieren"), size=34),
    blk(110, 580, 1040, 90, GELB, beim("auffang", "Artikel"), [("Art. 2 I GG: allgemeine Handlungsfreiheit", "ExtraBold", 36, INK)]),
    z("greift, wo kein spezielleres Grundrecht schützt", 110, 700, beim("auffang", "greift"), size=34),
    zit("BVerfGE 128, 226 Rn. 47 (Fraport) · BVerfGE 6, 32 (37) (Elfes)", 110, 790, beim("auffang", "schützt")),
    ficon("tabler", "building-bank", IX, IU, 150, "bind", fuell=GRAU, bis="welches"),
    ficon(HC, "skateboard", IX, IU, 150, "welches", fuell=GELB),
    *fig("GU", FX, FB, FR, [("bind", "ruhig"), ("welches", "denkt")]),
]))

# F Wortlaut Art. 2 I GG ------------------------------------------------------------------------------------------------
W2 = ["„Jeder hat das Recht auf die freie Entfaltung", "seiner Persönlichkeit, soweit er nicht die Rechte",
      "anderer verletzt und nicht gegen die", "verfassungsmäßige Ordnung oder das Sittengesetz", "verstößt.“"]
w2_els, w2_y = wortlaut(80, 190, 1100, W2, "Art. 2 Abs. 1 GG", "wortlaut", marken=[
    (0, "Jeder", beim("wortlaut", "Jeder")), (0, "freie Entfaltung", beim("wortlaut", "freie")),
    (1, "seiner Persönlichkeit", beim("wortlaut", "seiner")), (1, "Rechte", beim("wortlaut", "Rechte")),
    (2, "anderer", beim("wortlaut", "Rechte")), (3, "verfassungsmäßige Ordnung", beim("wortlaut", "verfassungsmäßige")),
    (3, "Sittengesetz", beim("wortlaut", "Sittengesetz"))], size=38)
folie([("wortlaut", "Art. 2 I GG › Wortlaut")], rechts_frei([
    titel(glyphen("Der Wortlaut"), 110, 90, "wortlaut", 50),
    *w2_els,
    *fig("GU", FX, FB, FR, [("wortlaut", "ruhig")]),
    ficon("tabler", "book", IX, IU, 140, "wortlaut", fuell=GELB),
]))

# G I. Schutzbereich ------------------------------------------------------------------------------------------------------
PS_ = "Art. 2 I GG › I. Schutzbereich"
folie([("sb", PS_), ("sb_p", f"{PS_} › persönlich"), ("sb_s", f"{PS_} › sachlich")], rechts_frei([
    *tafel("sb", "I. Schutzbereich"),
    z("persönlich: jeder", 110, 190, "sb_p", "Bold", 38),
    ok(140, 280, beim("sb_p", "Gudrun"), gr=22),
    z("also auch Gudrun", 185, 260, beim("sb_p", "Gudrun"), size=36),
    z("sachlich: jede Form menschlichen Handelns", 110, 350, "sb_s", "Bold", 38),
    z("ganz gleich, welches Gewicht sie für die", 150, 415, beim("sb_s", "ganz"), size=34),
    z("Persönlichkeit hat", 150, 465, beim("sb_s", "Persönlichkeit"), size=34),
    zit("BVerfGE 159, 223 Rn. 112 · BVerfGE 80, 137 (152)", 150, 525, beim("sb_s", "hat", ende=True)),
    z("sogar das Reiten im Walde", 110, 585, "reiten", "Bold", 36),
    zit("BVerfGE 80, 137 (154)", 600, 595, beim("reiten", "Walde")),
    ok(140, 680, beim("skaten", "Skaten"), gr=22),
    z("also auch Skaten", 185, 660, beim("skaten", "Skaten"), "Bold", 36),
    blk(110, 735, 1040, 90, GRUEN, beim("skaten", "Schutzbereich"), [("Schutzbereich eröffnet", "ExtraBold", 38, INK)]),
    ficon("tabler", "user", IX, IU, 120, "sb_p", fuell=ORANGE, bis="sb_s"),
    ficon("tabler", "walk", IX, IU, 120, "sb_s", fuell=BLAU, bis="reiten"),
    ficon("tabler", "horse", IX, IU, 180, "reiten", fuell=ORANGE, bis="skaten"),
    ficon(HC, "skateboard", IX, IU, 160, "skaten", fuell=GELB),
    *fig("GU", FX, FB, FR, [("sb", "ruhig"), ("skaten", "froh")]),
]))

# H II. Eingriff: klassisch -----------------------------------------------------------------------------------------------
PE_ = "Art. 2 I GG › II. Eingriff"
folie([("ein", PE_), ("klass", f"{PE_} › klassischer Eingriff")], rechts_frei([
    *tafel("ein", "II. Eingriff"),
    z("klassischer Eingriff:", 110, 190, "klass", "Bold", 38),
    z("– rechtsförmig", 150, 260, beim("klass", "rechtsförmig"), size=36),
    z("– unmittelbar", 150, 320, beim("klass", "unmittelbar"), size=36),
    z("– gezielt (final)", 150, 380, beim("klass", "gezielt"), size=36),
    z("– notfalls mit Zwang durchsetzbar", 150, 440, beim("klass", "notfalls"), size=36),
    z("= Gebot oder Verbot (imperativ)", 150, 510, beim("klass", "Gebot"), "Bold", 36),
    zit("BVerfGE 105, 279 (Osho) Rn. 68", 150, 575, beim("klass", "Verbot")),
    ok(140, 680, beim("verbot", "alle"), gr=22),
    z("Verbot mit Bußgeld: alle vier Merkmale", 185, 660, "verbot", "Bold", 36),
    *schild(IX, IU - 240, "ein", mit_pfosten=False),
    pl("Bußgeld", IX, IU - 10, beim("verbot", "Bußgeld"), fill=ROT, size=30, anker="m"),
    *fig("GU", FX, FB, FR, [("ein", "muede")]),
]))

# I II. Eingriff: modern (Osho) -------------------------------------------------------------------------------------------
folie([("modern", f"{PE_} › weiterer Schutz"), ("faktisch", f"{PE_} › moderner Eingriffsbegriff"), ("hier", f"{PE_} › hier: klassischer Eingriff (+)")], rechts_frei([
    *tafel("modern", "II. Eingriff: weiterer Schutz"),
    z("Der Schutz reicht weiter.", 110, 190, "modern", "Bold", 36),
    z("Osho-Beschluss (BVerfGE 105, 279):", 110, 265, "osho", "Bold", 36),
    z("Äußerungen der Bundesregierung", 150, 325, beim("osho", "Äußerungen"), size=34),
    z("über eine religiöse Bewegung", 150, 375, beim("osho", "religiöse"), size=34),
    z("an Art. 4 GG gemessen,", 150, 435, beim("osho", "Artikel"), size=34),
    z("obwohl sie nichts verboten", 150, 485, beim("osho", "obwohl"), size=34),
    blk(110, 555, 1040, 90, BLAU, "faktisch", [("auch faktische und mittelbare Beeinträchtigungen", "ExtraBold", 34, INK)]),
    z("= moderner Eingriffsbegriff", 150, 665, beim("faktisch", "moderne"), "Bold", 34),
    zit("Rn. 68–70, 77", 680, 675, beim("faktisch", "Eingriffsbegriff")),
    ok(140, 765, beim("hier", "klassische"), gr=22),
    z("hier nicht nötig: klassischer Eingriff liegt vor", 185, 745, "hier", size=34),
    ficon("tabler", "building-bank", IX - 90, IU, 130, "osho", fuell=GRAU, bis="hier"),
    ficon("tabler", "speakerphone", IX + 90, IU - 20, 110, beim("osho", "Äußerungen"), fuell=GELB, bis="hier"),
    *schild(IX, IU - 240, "hier", mit_pfosten=False),
    *fig("GU", FX, FB, FR, [("modern", "denkt"), ("hier", "ernst")]),
]))

# J III. 1. Schranke --------------------------------------------------------------------------------------------------------
PR_ = "Art. 2 I GG › III. Rechtfertigung"
folie([("rf", PR_), ("schranke", f"{PR_} › 1. Schranke"),
       (beim("schranke", "Vorbehalt"), f"{PR_} › 1. Schranke: verfassungsmäßige Ordnung")], rechts_frei([
    *tafel("rf", "III. Rechtfertigung"),
    z("1. Schranke", 110, 190, "schranke", "Bold", 38),
    z("Vorbehalt der verfassungsmäßigen Ordnung", 150, 255, beim("schranke", "Vorbehalt"), size=36),
    z("= jede Rechtsnorm, die formell und", 150, 340, "elfes", size=36),
    z("materiell verfassungsgemäß ist", 150, 395, beim("elfes", "materiell"), size=36),
    zit("BVerfGE 6, 32 (38) (Elfes) · BVerfGE 80, 137 (153)", 150, 460, beim("elfes", "ist", ende=True)),
    blk(110, 530, 1040, 90, GELB, "leicht", [("Schranke leicht erreicht", "ExtraBold", 38, INK)]),
    z("Entscheidend: Ist die Verordnung selbst", 110, 670, beim("leicht", "Entscheidend"), "Bold", 36),
    z("verfassungsgemäß?", 110, 725, beim("leicht", "verfassungsgemäß"), "Bold", 36),
    ficon("tabler", "book", IX, IU, 140, "elfes", fuell=BLAU, bis=beim("leicht", "Entscheidend")),
    ficon("tabler", "file-text", IX, IU, 120, beim("leicht", "Entscheidend"), fuell=WEISS),
    *fig("BR", FX, FB, FR, [("rf", "ruhig")]),
    pl("Herr Brückner", FX, FB + 22, "rf", fill=BLAU, size=28, anker="m", d=0.2),
]))

# K 2. Schranken-Schranken: formell -----------------------------------------------------------------------------------------
PSS = f"{PR_} › 2. Schranken-Schranken"
folie([("ss", PSS), ("formell", f"{PSS} › formell")], rechts_frei([
    *tafel("ss", "2. Schranken-Schranken"),
    z("Ist die Verordnung selbst verfassungsgemäß?", 110, 190, "ss", size=34, farbe=TEXT),
    z("a) formell:", 110, 270, "formell", "Bold", 38),
    z("– Zuständigkeit", 150, 340, beim("formell", "Zuständigkeit"), size=36),
    z("– Verfahren", 150, 400, beim("formell", "Verfahren"), size=36),
    z("– Form", 150, 460, beim("formell", "Form", nr=2), size=36),
    ok(140, 565, beim("formell", "unterstellen"), gr=22),
    z("wirksames Landesgesetz als Grundlage,", 185, 545, beim("formell", "wirksamen"), size=34),
    z("formell in Ordnung: unterstellt", 185, 600, beim("formell", "unterstellen"), "Bold", 34),
    ficon("tabler", "file-certificate", IX, IU, 140, "formell", fuell=WEISS),
    *fig("BR", FX, FB, FR, [("ss", "ruhig")]),
]))

# L Zitiergebot (Wortlaut Art. 19 I GG) ----------------------------------------------------------------------------------------
W19 = ["„Soweit nach diesem Grundgesetz ein Grundrecht", "durch Gesetz oder auf Grund eines Gesetzes",
       "eingeschränkt werden kann, muß das Gesetz", "allgemein und nicht nur für den Einzelfall gelten.",
       "Außerdem muß das Gesetz das Grundrecht unter", "Angabe des Artikels nennen.“"]
w19_els, w19_y = wortlaut(80, 150, 1100, W19, "Art. 19 Abs. 1 GG", "zitier", marken=[
    (4, "das Grundrecht unter", beim("zitier", "Grundrecht")), (5, "Angabe des Artikels nennen", beim("zitier", "Angabe")),
    (1, "durch Gesetz oder auf Grund eines Gesetzes", beim("nur", "durch"))], size=34)
PZ = f"{PSS} › formell › Zitiergebot, Art. 19 I 2 GG"
folie([("zitier", PZ), ("nicht", f"{PSS} › Zitiergebot: nicht bei Art. 2 I GG")], rechts_frei([
    titel(glyphen("Zitiergebot"), 110, 60, "zitier", 50),
    *w19_els,
    ok(140, w19_y + 55, beim("nur", "Fernmeldegeheimnis"), gr=22),
    z("gilt z. B. für das Fernmeldegeheimnis (Art. 10 II 1 GG)", 185, w19_y + 35, beim("nur", "Fernmeldegeheimnis"), size=33),
    nein(140, w19_y + 120, beim("nicht", "nicht"), gr=20),
    z("nicht für die allgemeine Handlungsfreiheit", 185, w19_y + 100, "nicht", "Bold", 34),
    zit("BVerfGE 113, 348 Rn. 84, 86 · BVerfGE 10, 89 (99)", 185, w19_y + 165, beim("nicht", "nicht")),
    ficon("tabler", "phone", IX, IU, 110, beim("nur", "Fernmeldegeheimnis"), fuell=BLAU, bis="nicht"),
    ficon(HC, "skateboard", IX, IU, 150, "nicht", fuell=GELB),
    *fig("GU", FX, FB, FR, [("zitier", "denkt"), ("nicht", "ernst")]),
]))

# M Bestimmtheit -------------------------------------------------------------------------------------------------------------
SB_X, GB_X = 1400, 1720
folie([("best", f"{PSS} › materiell › Bestimmtheit")], rechts_frei([
    *tafel("best", "b) materiell: Bestimmtheit"),
    z("Betroffene müssen die Rechtslage erkennen", 110, 190, "best", size=36),
    z("und ihr Verhalten danach ausrichten können", 110, 245, beim("best", "Verhalten"), size=36),
    zit("BVerfGE 134, 141 Rn. 126", 110, 310, beim("best", "können")),
    ok(140, 410, beim("klar", "Skateboard"), gr=20), z("Skateboard", 185, 390, beim("klar", "Skateboard"), "Bold", 36),
    ok(140, 470, beim("klar", "Fußgängerzone"), gr=20), z("Fußgängerzone", 185, 450, beim("klar", "Fußgängerzone"), "Bold", 36),
    ok(140, 530, beim("klar", "acht"), gr=20), z("8 bis 20 Uhr", 185, 510, beim("klar", "acht"), "Bold", 36),
    blk(110, 600, 1040, 90, GRUEN, beim("klar", "klar", nr=1), [("Das ist klar.", "ExtraBold", 38, INK)]),
    *schild(SB_X, 330, "best", boden=FB),
    *fig("GU", GB_X, FB, FR, [("best", "ernst")]),
]))

# N Verhältnismäßigkeit --------------------------------------------------------------------------------------------------------
PV = f"{PSS} › materiell › Verhältnismäßigkeit"
folie([("vhm", PV), ("zweck", f"{PV} › legitimer Zweck"), ("geeignet", f"{PV} › geeignet"), ("erf", f"{PV} › erforderlich")],
      rechts_frei([
    *tafel("vhm", "Verhältnismäßigkeit"),
    ok(140, 210, beim("zweck", "legitim"), gr=20),
    z("1. legitimer Zweck: Gesundheit der Fußgänger", 185, 190, beim("zweck", "Fußgänger"), size=34),
    ok(140, 275, beim("geeignet", "weniger"), gr=20),
    z("2. geeignet: Zweck kann gefördert werden", 185, 255, "geeignet", size=34),
    z("Möglichkeit genügt: weniger Zusammenstöße", 185, 305, beim("geeignet", "Möglichkeit"), size=34),
    zit("BVerfGE 159, 223 Rn. 169, 185", 185, 360, beim("geeignet", "Zusammenstöße")),
    z("3. erforderlich: kein milderes, gleich", 185, 420, "erf", size=34),
    z("wirksames Mittel", 185, 470, beim("erf", "wirksames"), size=34),
    nein(200, 560, beim("schritt", "kontrollieren"), gr=18),
    z("Schritttempo? kaum kontrollierbar", 240, 540, "schritt", size=34),
    z("gleich wirksam muss eindeutig feststehen", 240, 595, beim("schritt", "eindeutig"), size=34),
    zit("BVerfGE 159, 223 Rn. 203", 240, 650, beim("schritt", "feststehen")),
    ok(140, 725, beim("tag", "tagsüber"), gr=20),
    z("Verbot gilt nur tagsüber, wenn es voll ist", 185, 705, beim("tag", "tagsüber"), "Bold", 34),
    ficon("tabler", "first-aid-kit", IX, IU, 130, "zweck", fuell=ROT, bis="erf"),
    ficon("tabler", "gauge", IX, IU, 130, "schritt", fuell=GELB, bis="tag"),
    ficon("tabler", "clock", IX, IU, 130, "tag", fuell=WEISS),
    *fig("KR", FX, FB, FR, [("vhm", "ruhig"), ("geeignet", "froh")]),
    pl("Frau Krüger", FX, FB + 22, "vhm", fill=LILA, size=28, anker="m", d=0.2),
]))

# O Angemessenheit ------------------------------------------------------------------------------------------------------------
GO_X, KO_X = 1420, 1750
hx, hy = hand("GU_muede", GO_X, FB, FR, -1)
folie([("angem", f"{PV} › angemessen")], rechts_frei([
    *tafel("angem", "4. angemessen"),
    z("Zweck nicht außer Verhältnis", 110, 190, "angem", "Bold", 36),
    z("zur Schwere des Eingriffs", 110, 245, beim("angem", "Schwere"), "Bold", 36),
    zit("BVerfGE 159, 223 Rn. 216", 110, 305, beim("angem", "Eingriffs")),
    z("Gudrun: tagsüber absteigen, Brett tragen", 150, 380, "last", size=34),
    z("abends und überall sonst: fahren", 150, 435, beim("last", "Abends"), size=34),
    ficon("tabler", "scale", 1585, 400, 200, beim("schutz", "Dem"), fuell=GELB),
    z("gegenüber: Gesundheit vieler Fußgänger", 150, 520, beim("schutz", "Gesundheit"), size=34),
    ok(140, 640, beim("schutz", "angemessen"), gr=22),
    blk(185, 600, 600, 85, GRUEN, beim("schutz", "angemessen"), [("angemessen", "ExtraBold", 38, INK)]),
    *fig("GU", GO_X, FB, FR, [("angem", "ruhig"), ("last", "muede")]),
    ficon(HC, "skateboard", max(1350, hx - 10), hy + 60, 120, "last", fuell=GELB),
    *fig("KR", KO_X, FB, FR, [("schutz", "ruhig")]),
]))

# P Wesensgehalt (Wortlaut Art. 19 II GG), Ergebnis -----------------------------------------------------------------------------
W192 = ["„In keinem Falle darf ein Grundrecht in seinem", "Wesensgehalt angetastet werden.“"]
w192_els, w192_y = wortlaut(80, 150, 1100, W192, "Art. 19 Abs. 2 GG", "wesen",
                            marken=[(1, "Wesensgehalt", beim("wesen", "Wesensgehalt"))], size=38)
folie([("wesen", f"{PSS} › materiell › Wesensgehalt, Art. 19 II GG"), ("erg", "Ergebnis: Art. 2 I GG nicht verletzt")], rechts_frei([
    titel(glyphen("Wesensgehalt"), 110, 60, "wesen", 50),
    *w192_els,
    ok(140, w192_y + 70, beim("wesen2", "unberührt"), gr=22),
    z("nur Fußgängerzone, nur tagsüber:", 185, w192_y + 50, "wesen2", size=36),
    z("Wesensgehalt unberührt", 185, w192_y + 105, beim("wesen2", "unberührt"), "Bold", 36),
    blk(80, w192_y + 200, 1100, 160, GRUEN, "erg", [("Ergebnis: Eingriff gerechtfertigt", "ExtraBold", 38, INK), ("", "Regular", 18, INK)]),
    z("Gudrun nicht in Art. 2 I GG verletzt", 120, w192_y + 290, beim("erg", "Gudrun"), "Bold", 36),
    *fig("GU", FX, FB, FR, [("wesen", "ruhig"), ("erg", "sorge")]),
]))

# Q Gegenfall --------------------------------------------------------------------------------------------------------------------
folie([("gegen", "Gegenfall · Verbot rund um die Uhr"), ("gegen3", "Gegenfall › erforderlich?")], rechts_frei([
    *tafel("gegen", "Gegenfall"),
    z("Verbot rund um die Uhr", 110, 190, "gegen", "Bold", 38),
    z("auch nachts, wenn die Fußgängerzone leer ist", 110, 255, beim("gegen", "nachts"), size=34),
    z("Geht es nur um die Fußgänger?", 110, 350, "gegen2", "Bold", 36),
    ok(140, 435, beim("gegen2", "milder"), gr=20),
    z("Verbot am Tag: gleich wirksam und milder", 185, 415, beim("gegen2", "Verbot"), size=34),
    blk(110, 520, 1040, 90, ROT, "gegen3", [("spricht viel für: nicht erforderlich", "ExtraBold", 36, INK)]),
    nein(1110, 565, beim("gegen3", "nicht"), gr=22),
    zit("vgl. BVerfGE 159, 223 Rn. 169, 203", 110, 640, beim("gegen3", "erforderlich")),
    *schild(1400, 330, "gegen", text="0–24 Uhr", boden=FB),
    ficon("tabler", "moon", 1400, 260, 90, beim("gegen", "nachts"), fuell=GELB),
    *fig("GU", 1720, FB, FR, [("gegen", "sorge"), ("gegen3", "froh")]),
]))

# R Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Aufbau"), ("fehler", "Klausurtipp · typische Aufbaufehler")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Dreischritt = Klausurkonvention,", 200, 200, beim("tipp", "Dreischritt"), "Bold", 36),
    z("kein Gesetzestext", 200, 255, beim("tipp", "kein"), "Bold", 36),
    z("trotzdem einhalten", 200, 320, beim("tipp", "Halte"), size=34),
    z("Typische Fehler:", 110, 410, "fehler", "Bold", 36),
    nein(150, 495, "f1", gr=18), z("Verhältnismäßigkeit vor der Schranke", 200, 475, "f1", size=34),
    nein(150, 555, "f2", gr=18), z("Zitiergebot bei jedem Grundrecht", 200, 535, "f2", size=34),
    nein(150, 615, "f3", gr=18), z("Art. 2 I GG vor spezielleren Grundrechten", 200, 595, "f3", size=34),
    z("Was eindeutig ist, prüfst du kurz.", 110, 700, "kurz", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ------------------------------------------------------------------------------------------------------------
fR = F("Regular", 34)
VX = K3 + int(fR.getlength("Verhältnismäßigkeit: "))
vx = [VX]
for t in ("legitimer Zweck, ", "Eignung, ", "Erforderlichkeit, "):
    vx.append(vx[-1] + int(fR.getlength(t)))
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Freiheitsrecht"), 110, 90, "sch", 48),
    z("I. Schutzbereich: persönlich und sachlich", K1, 195, "s1", "Bold", 38, rechts=1820),
    z("II. Eingriff", K1, 265, "s2", "Bold", 38, rechts=1820),
    z("III. Verfassungsrechtliche Rechtfertigung", K1, 335, "s3", "Bold", 38, rechts=1820),
    z("1. Schranke", K2, 405, "s31", size=36, rechts=1820),
    z("2. Schranken-Schranken", K2, 470, "s32", size=36, rechts=1820),
    z("a) formell, mit Zitiergebot, wo es gilt", K3, 535, "s32f", size=34, rechts=1820),
    z("b) materiell: Bestimmtheit", K3, 600, "s32m", size=34, rechts=1820),
    z("Verhältnismäßigkeit:", K3, 665, "s32v", size=34, rechts=1820),
    z("legitimer Zweck,", vx[0], 665, beim("s32v", "legitimem"), size=34, rechts=1820),
    z("Eignung,", vx[1], 665, beim("s32v", "Eignung"), size=34, rechts=1820),
    z("Erforderlichkeit,", vx[2], 665, beim("s32v", "Erforderlichkeit"), size=34, rechts=1820),
    z("Angemessenheit", vx[3], 665, beim("s32v", "Angemessenheit"), size=34, rechts=1820),
    z("Wesensgehalt, Art. 19 II GG", K3, 730, "s32w", size=34, rechts=1820),
])

# T Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Schutzbereich und Eingriff", 0)], [("sind oft ", 0), ("schnell bejaht.", "a")]],
                750, 310, 50, "merke", {"a": beim("merke", "schnell")}),
    *markertext([[("Die eigentliche Arbeit steckt in den", 0)], [("Schranken-Schranken", "b"), (",", 0)],
                 [("vor allem in der ", 0), ("Verhältnismäßigkeit.", "c")]], 750, 540, 46, "m2",
                {"b": beim("m2", "Schranken"), "c": beim("m2", "Verhältnismäßigkeit")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
