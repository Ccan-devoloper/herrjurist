"""Folge 023 · Anfechtung Schema §§ 119 ff. BGB: Die Prüfung in 5 Schritten – Serienstandard Open Peeps (Katzenkönig).
Frei erfundener Beispielfall (Ilse vertippt sich bei der Kalenderbestellung), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Die Bestellung (Buchladen), B Annahme und Anruf, C Sachverhalt, D Anspruch, E Wortlaut § 142 I, F 1. Anfechtungsgegenstand,
G 2. Anfechtungsgrund (Wortlaut § 119 I, Kausalität), H weitere Gründe (Wortlaut § 119 II, §§ 120, 123), I Gegenfall
Motiv-/Kalkulationsirrtum, J 3. Anfechtungserklärung, K 4. Frist, L 5. kein Ausschluss, M Rechtsfolge und § 122,
N Gegenfall Täuschung (Lieferwagen), O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Tippen am Laptop, Telefon klingelt; Freesound CC0).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig wie in Folge 020 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_023/"


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
        if n.startswith(("bild:", "ficon:")) or "/op_023/" in n:
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


def nummern(x0, y, cue_liste, schritt=86, size=34, fill=GELB):
    """Fünf runde Schrittnummern, jede zu ihrem Cue."""
    return [pl(str(i + 1), x0 + i * schritt, y, c, fill=fill, size=size, anker="m") for i, c in enumerate(cue_liste)]


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
PA = "II. Anfechtung, § 142 I"

# A Fall: die Bestellung im Buchladen ---------------------------------------------------------------------------------
IL_A = 990
LAP = (720, 640)                            # Laptop auf dem Ladentisch (Mitte, Unterkante)
LAGER = (1690, BODEN - 2)
ILa = ("IL_ruhig", IL_A, BODEN, FH)
folie([(NULL, "Fall · Die Bestellung")], [
    hart(pl("Montagabend", 70, 40, NULL, fill=GELB, size=48)),
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    # Buchladen: Regal mit Büchern, Ladentisch mit Laptop
    hart(linienzug([(90, 470), (430, 470)], NULL, breite=8, farbe=INK)),
    hart(linienzug([(90, 670), (430, 670)], NULL, breite=8, farbe=INK)),
    ficon("tabler", "books", 180, 468, 150, NULL, fuell=ROT, anim="cut"),
    ficon("tabler", "books", 340, 468, 150, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "books", 180, 668, 150, NULL, fuell=GRUEN, anim="cut"),
    ficon("tabler", "books", 340, 668, 150, NULL, fuell=GELB, anim="cut"),
    pl("Buchladen", 260, 760, NULL, fill=WEISS, size=32, anker="m", anim="cut"),
    ficon("tabler", "desk", 720, BODEN - 4, 340, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "device-laptop", LAP[0], LAP[1], 170, NULL, fuell=WEISS, anim="cut"),
    *fig("IL", IL_A, BODEN, FH, [(NULL, "ruhig"), (beim("null", "tippt"), "ernst")], erst="cut"),
    hart(pl("Ilse", IL_A, BODEN + 22, NULL, fill=LILA, size=30, anker="m")),
    ficon("tabler", "mail", LAP[0] + 150, LAP[1] - 100, 80, beim("bestell", "E-Mail"), fuell=GELB, bis=beim("null", "zwanzig")),
    ficon("tabler", "building-warehouse", LAGER[0], LAGER[1], 280, beim("bestell", "Großhändler"), fuell=BLAU),
    pl("Großhändler Winkler", LAGER[0], BODEN + 22, beim("bestell", "Winkler"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "calendar", 560, 500, 80, beim("bestell", "Kalender"), fuell=WEISS),
    pl("Kalender", 560, 520, beim("bestell", "Kalender"), fill=WEISS, size=26, anker="m"),
    blase("denk", 420, 220, beim("null", "zehn"), 1330, 250, inhalt=["zehn Kartons"], textsize=34,
          figur=ILa, bis=beim("null", "tippt")),
    szene(pl("100 Kartons", LAP[0], 370, beim("null", "tippt"), fill=ROT, size=34, anker="m"), "023tippen*", 0.8),
    pl("„0“ zu viel", LAP[0], 300, beim("null", "Null"), fill=WEISS, size=28, anker="m"),
    pl("je 20 €", LAP[0], 440, beim("null", "zwanzig"), fill=GELB, size=28, anker="m"),
    # die Bestellung geht ab: Mail fliegt zum Lager
    bewegt(ficon("tabler", "mail", LAGER[0], 470, 90, beim("null", "zwanzig"), fuell=GELB),
           beim("null", "zwanzig"), beim("null", "Euro", ende=True),
           LAP[0] + 150 - LAGER[0], LAP[1] - 100 - 470),
])

# B Fall: Annahme, Anruf, Streit -----------------------------------------------------------------------------------------
IL_B, WI_B = 420, 1430
ILb = ("IL_redet_r", IL_B, BODEN, FH)
WIb = ("WI_redet", WI_B, BODEN, FH)
folie([("annahme", "Fall · Die Annahme"), ("merkt", "Fall · Der Anruf"), ("frage", "Fall · Die Frage")], [
    pl("Dienstagmorgen", 70, 40, "annahme", fill=GELB, size=48, bis="frage"),
    linienzug([(60, BODEN), (1860, BODEN)], "annahme", breite=7, farbe=INK),
    ficon("tabler", "building-warehouse", 1730, BODEN - 2, 240, "annahme", fuell=BLAU),
    *fig("WI", WI_B, BODEN, FH, [("annahme", "froh")], bis="w1"),
    *redet("WI_redet", WI_B, BODEN, FH, "w1", "frage"),
    peep_voll("WI_aerger", WI_B, BODEN, FH, "frage", anim="cut"),
    pl("Herr Winkler", WI_B, BODEN + 22, "annahme", fill=BLAU, size=28, anker="m"),
    bewegt(ficon("tabler", "mail-check", IL_B + 200, 560, 90, beim("annahme", "nimmt"), fuell=GRUEN, bis="merkt"),
           beim("annahme", "nimmt"), beim("annahme", "E-Mail", ende=True), WI_B - 200 - IL_B - 200, 0),
    ficon("tabler", "truck-delivery", 1000, BODEN - 2, 220, beim("annahme", "Spedition"), fuell=GELB),
    pl("Spedition gebucht", 1000, 600, beim("annahme", "Spedition"), fill=GELB, size=28, anker="m", bis="i1"),
    *fig("IL", IL_B, BODEN, FH, [("annahme", "ruhig_r"), (beim("merkt", "erschrickt"), "schreck_r")], bis="i1"),
    *redet("IL_redet_r", IL_B, BODEN, FH, "i1", "w1"),
    peep_voll("IL_sorge_r", IL_B, BODEN, FH, "w1", anim="cut"),
    pl("Ilse", IL_B, BODEN + 22, "annahme", fill=LILA, size=30, anker="m"),
    ficon("tabler", "mail-opened", IL_B + 200, 560, 90, "merkt", fuell=GRUEN, bis=beim("merkt", "ruft")),
    pl("9 Uhr", IL_B + 200, 420, beim("merkt", "neun"), fill=WEISS, size=30, anker="m", bis=beim("merkt", "ruft")),
    ficon("tabler", "device-mobile", IL_B + 70, 500, 56, beim("merkt", "ruft"), fuell=WEISS),
    szene(ficon("tabler", "phone-call", WI_B - 190, 470, 80, beim("merkt", "ruft"), fuell=GRUEN, bis="w1"),
          "023telefon*", 0.6),
    blase("sprech", 860, 300, "i1", 860, 230, inhalt=["Herr Winkler, ich habe mich vertippt!",
                                                     "Ich wollte zehn Kartons, nicht hundert.",
                                                     "Diese Bestellung lasse ich so nicht gelten."], textsize=32,
          figur=ILb, bis="w1"),
    blase("sprech", 700, 250, "w1", 1060, 230, inhalt=["Bestellt ist bestellt.", "Sie schulden mir zweitausend Euro!"],
          textsize=34, figur=WIb, bis="frage"),
    pl("Muss Ilse zahlen?", 930, 130, beim("frage", "Muss"), fill=PINK, size=44, anker="m"),
    pl("Rettung: Anfechtung", 930, 230, beim("frage", "Anfechtung"), fill=GELB, size=38, anker="m"),
    *nummern(930 - 2 * 86, 330, [beim("frage", "fünf")] * 5),
])

# C Sachverhalt --------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Ilse führt einen kleinen Buchladen. Am Montagabend bestellt sie per E-Mail beim Großhändler Winkler Kalender. Sie "
    "will 10 Kartons, tippt aber versehentlich „100 Kartons“ zu je 20 Euro. Für Herrn Winkler ist der Tippfehler nicht "
    "erkennbar.",
    "Am Dienstagmorgen nimmt Herr Winkler die Bestellung per E-Mail an und bucht gleich eine Spedition für 80 Euro, die "
    "er nicht mehr stornieren kann. Ilse liest die Antwort um 9 Uhr und ruft sofort an: „Ich habe mich vertippt! Ich "
    "wollte zehn Kartons, nicht hundert. Diese Bestellung lasse ich so nicht gelten.“ Herr Winkler verlangt 2.000 Euro.",
    "(Frei erfundener Übungsfall.)",
], "Muss Ilse die 2.000 Euro zahlen?")

# D Anspruch -----------------------------------------------------------------------------------------------------------
folie([("ansp", "Winkler gegen Ilse · § 433 II BGB"), ("nichtig", "Winkler gegen Ilse › nichtig nach § 142 I BGB?")],
      rechts_frei([
    *tafel("ansp", "Winkler gegen Ilse: 2.000 €"),
    z("Anspruch: § 433 Abs. 2 BGB (Kaufpreis)", 110, 200, beim("ansp", "Paragraf"), "Bold", 38),
    ok(140, 310, beim("vertrag", "geschlossen"), gr=22),
    z("Kaufvertrag über 100 Kartons geschlossen", 185, 290, "vertrag", size=36),
    blk(110, 410, 1040, 150, GELB, "nichtig", [("aber: fällt weg, wenn Ilse", "Bold", 36, INK),
                                               ("wirksam anficht", "ExtraBold", 38, INK)]),
    z("Rechtsfolge: § 142 Abs. 1 BGB", 110, 620, beim("nichtig", "anficht"), "Bold", 36),
    ficon("tabler", "cash-banknote", (X1 + X2) // 2, 390, 200, "ansp", fuell=GRUEN),
    pl("2.000 €", (X1 + X2) // 2, 180, "ansp", fill=GELB, size=32, anker="m"),
    *fig("WI", X1, 930, 480, [("ansp", "ruhig")]),
    *fig("IL", X2, 930, 480, [("ansp", "ruhig"), ("nichtig", "denkt")], d=0.2),
    pl("Herr Winkler", X1, 952, "ansp", fill=BLAU, size=28, anker="m", d=0.2),
    pl("Ilse", X2, 952, "ansp", fill=LILA, size=30, anker="m", d=0.3),
]))

# E Wortlaut § 142 I BGB -----------------------------------------------------------------------------------------------
W142 = ["„Wird ein anfechtbares Rechtsgeschäft angefochten,", "so ist es als von Anfang an nichtig anzusehen.“"]
w142_els, w142_y = wortlaut(80, 200, 1100, W142, "§ 142 Abs. 1 BGB", "p142", marken=[
    (0, "anfechtbares Rechtsgeschäft", beim("p142", "anfechtbares")), (0, "angefochten", beim("p142", "angefochten")),
    (1, "von Anfang an nichtig", beim("p142", "von"))], size=40)
folie([("p142", "§ 142 I BGB › Wortlaut")], rechts_frei([
    titel(glyphen("Der Wortlaut"), 110, 90, "p142", 50),
    *w142_els,
    blk(80, w142_y + 60, 1100, 100, ROT, beim("p142", "nichtig"), [("= rückwirkend (ex tunc) unwirksam", "ExtraBold", 38, INK)]),
    ficon("tabler", "book", IX, IU, 140, "p142", fuell=GELB),
    *fig("IL", FX, FB, FR, [("p142", "ruhig"), (beim("p142", "nichtig"), "froh")]),
]))

# F 1. Anfechtungsgegenstand ---------------------------------------------------------------------------------------------
P1 = f"{PA} › 1. Anfechtungsgegenstand"
folie([("s1", P1), ("ausleg", f"{P1} › Auslegung, §§ 133, 157 BGB")], rechts_frei([
    *tafel("s1", "Schritt 1: Anfechtungsgegenstand"),
    z("eine Willenserklärung: die Bestellung", 110, 190, beim("s1", "Willenserklärung"), "Bold", 36),
    z("Zuerst auslegen, §§ 133, 157 BGB:", 110, 290, "ausleg", "Bold", 36),
    z("Wie musste Herr Winkler die Mail verstehen?", 150, 350, beim("ausleg", "Maßgeblich"), size=34),
    zit("BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 23", 150, 405, beim("ausleg", "musste", ende=True)),
    z("Tippfehler für ihn nicht erkennbar", 150, 480, "hundert", size=34),
    ok(140, 560, beim("hundert", "objektiv"), gr=22),
    z("objektiv erklärt: 100 Kartons", 185, 540, beim("hundert", "objektiv"), "Bold", 36),
    blk(110, 640, 1040, 100, GRUEN, "s1ok", [("Diese Erklärung will Ilse anfechten.", "ExtraBold", 36, INK)]),
    ficon("tabler", "mail", X1, 380, 110, "s1", fuell=GELB),
    pl("100 Kartons", X1, 160, beim("hundert", "hundert"), fill=ROT, size=28, anker="m"),
    *fig("WI", X1, 930, 480, [("s1", "ruhig"), ("ausleg", "denkt")]),
    *fig("IL", X2, 930, 480, [("s1", "ruhig"), ("s1ok", "ernst")], d=0.2),
    pl("Herr Winkler", X1, 952, "s1", fill=BLAU, size=28, anker="m", d=0.2),
    pl("Ilse", X2, 952, "s1", fill=LILA, size=30, anker="m", d=0.3),
]))

# G 2. Anfechtungsgrund: Wortlaut § 119 I, Kausalität ---------------------------------------------------------------------
P2 = f"{PA} › 2. Anfechtungsgrund"
W119 = ["„Wer bei der Abgabe einer Willenserklärung über deren", "Inhalt im Irrtum war oder eine Erklärung dieses Inhalts",
        "überhaupt nicht abgeben wollte, kann die Erklärung", "anfechten, wenn anzunehmen ist, dass er sie bei Kenntnis",
        "der Sachlage und bei verständiger Würdigung des Falles", "nicht abgegeben haben würde.“"]
w119_els, w119_y = wortlaut(80, 120, 1100, W119, "§ 119 Abs. 1 BGB", "p119", marken=[
    (0, "über deren", beim("inhalt", "Inhaltsirrtum")), (1, "Inhalt im Irrtum", beim("inhalt", "Inhaltsirrtum")),
    (1, "eine Erklärung dieses Inhalts", beim("erkl", "eine")), (2, "überhaupt nicht abgeben wollte", beim("erkl", "überhaupt")),
    (3, "bei Kenntnis", beim("kaus", "Kenntnis")), (4, "der Sachlage", beim("kaus", "Sachlage")),
    (4, "verständiger Würdigung", beim("kaus", "verständiger"))], size=32)
folie([("s2", f"{P2}, § 119 I BGB"), ("kaus", f"{P2} › Kausalität")], rechts_frei([
    titel(glyphen("Schritt 2: Anfechtungsgrund"), 110, 50, "s2", 46),
    *w119_els,
    z("Inhaltsirrtum: sagt, was er will, irrt über die Bedeutung", 110, w119_y + 30, "inhalt", size=32),
    z("Erklärungsirrtum: verspricht oder vertippt sich", 110, w119_y + 85, "erkl", "Bold", 32),
    ok(140, w119_y + 160, "ilse", gr=20),
    z("Ilse: 100 statt 10 getippt", 185, w119_y + 140, "ilse", "Bold", 32),
    z("Kausalität: so nicht bestellt", 110, w119_y + 215, "kaus", "Bold", 32),
    ok(140, w119_y + 290, beim("kaus2", "Weder"), gr=20),
    z("weder Ilse noch ein vernünftiger Dritter", 185, w119_y + 270, beim("kaus2", "Weder"), size=32),
    zit("BGH, Beschl. v. 10.6.2015 – IV ZB 39/14, Rn. 10", 185, w119_y + 325, beim("kaus2", "gewollt")),
    ficon("tabler", "device-laptop", IX, IU, 160, "s2", fuell=WEISS),
    pl("100 Kartons", IX, IU - 215, "ilse", fill=ROT, size=28, anker="m"),
    *fig("IL", FX, FB, FR, [("s2", "ruhig"), ("ilse", "sorge"), ("kaus2", "ernst")]),
]))

# H weitere Gründe: Wortlaut § 119 II, §§ 120, 123 ---------------------------------------------------------------------------
W1192 = ["„Als Irrtum über den Inhalt der Erklärung gilt auch der", "Irrtum über solche Eigenschaften der Person oder der Sache,",
         "die im Verkehr als wesentlich angesehen werden.“"]
w1192_els, w1192_y = wortlaut(80, 150, 1100, W1192, "§ 119 Abs. 2 BGB", "p119b", marken=[
    (1, "Eigenschaften", beim("p119b", "Eigenschaften")), (1, "der Person oder der Sache", beim("p119b", "Person")),
    (2, "im Verkehr als wesentlich", beim("p119b", "Verkehr"))], size=33)
folie([("weitere", f"{P2} › weitere Gründe"), ("p119b", f"{P2} › Eigenschaftsirrtum, § 119 II BGB"),
       ("p120", f"{P2} › Übermittlung, § 120 BGB"), ("p123", f"{P2} › Täuschung, Drohung, § 123 BGB")], rechts_frei([
    titel(glyphen("Weitere Anfechtungsgründe"), 110, 60, "weitere", 48),
    *w1192_els,
    z("§ 120 BGB: falsche Übermittlung, etwa durch einen Boten", 110, w1192_y + 50, "p120", "Bold", 34),
    z("§ 123 BGB: arglistige Täuschung", 110, w1192_y + 140, "p123", "Bold", 34),
    z("und widerrechtliche Drohung", 210, w1192_y + 195, beim("p123", "widerrechtliche"), "Bold", 34),
    ficon("tabler", "user-search", IX, IU, 140, "p119b", fuell=GELB, bis="p120"),
    ficon("tabler", "run", IX, IU, 140, "p120", fuell=BLAU, bis="p123"),
    ficon("tabler", "spy", IX, IU, 140, "p123", fuell=ROT),
    *fig("IL", FX, FB, FR, [("weitere", "ruhig"), ("p123", "denkt")]),
]))

# I Gegenfall: Motivirrtum, Kalkulationsirrtum -------------------------------------------------------------------------------
folie([("motiv", "Gegenfall · Motivirrtum"), ("kalk", "Gegenfall · Kalkulationsirrtum")], rechts_frei([
    *tafel("motiv", "Gegenfall: Motivirrtum"),
    z("Ilse bestellt bewusst 100 Kartons", 110, 185, beim("motiv", "bewusst"), "Bold", 36),
    z("Hoffnung: das Stadtfest", 150, 240, beim("motiv", "Stadtfest"), size=34),
    nein(160, 315, beim("motiv", "abgesagt"), gr=18), z("Fest abgesagt", 200, 295, beim("motiv", "abgesagt"), size=34),
    z("Irrtum nur im Beweggrund, nicht über die Erklärung", 110, 370, "motiv2", size=34),
    nein(140, 445, beim("motiv2", "berechtigt"), gr=20),
    z("Motivirrtum: keine Anfechtung", 185, 425, beim("motiv2", "Motivirrtum"), "Bold", 36),
    zit("BAG, Urt. v. 24.4.2014 – 8 AZR 429/12, Rn. 22 · BGH IV ZB 12/22, Rn. 15", 185, 480, beim("motiv2", "Anfechtung")),
    z("Kalkulationsirrtum (interner Rechenfehler):", 110, 560, "kalk", "Bold", 34),
    z("grundsätzlich gebunden", 150, 615, beim("kalk", "grundsätzlich"), size=34),
    z("treuwidrig (§ 242 BGB) kann sein: Bestehen auf dem", 150, 690, "treu", size=32),
    z("Vertrag trotz erkannten erheblichen Irrtums", 150, 740, beim("treu", "obwohl"), size=32),
    zit("BGH, Urt. v. 11.11.2014 – X ZR 32/14, Rn. 6, 9 (zu BGHZ 139, 177)", 150, 795, beim("treu", "erkannt")),
    ficon("tabler", "confetti", IX, IU, 140, beim("motiv", "Stadtfest"), fuell=GELB, bis=beim("motiv", "abgesagt")),
    ficon("tabler", "confetti-off", IX, IU, 140, beim("motiv", "abgesagt"), fuell=ROT, bis="kalk"),
    ficon("tabler", "calculator", IX, IU, 130, "kalk", fuell=WEISS),
    *fig("IL", FX, FB, FR, [("motiv", "strahlt"), (beim("motiv", "abgesagt"), "sorge"), ("kalk", "denkt")]),
]))

# J 3. Anfechtungserklärung ---------------------------------------------------------------------------------------------------
P3 = f"{PA} › 3. Anfechtungserklärung, § 143 BGB"
folie([("s3", P3)], rechts_frei([
    *tafel("s3", "Schritt 3: Anfechtungserklärung"),
    z("§ 143 Abs. 1 BGB: gegenüber dem Anfechtungsgegner", 110, 190, "s3", "Bold", 34),
    z("Vertrag: der andere Teil (§ 143 Abs. 2 BGB)", 150, 250, "gegner", size=34),
    ok(190, 330, beim("gegner", "Winkler"), gr=20), z("Herr Winkler", 235, 310, beim("gegner", "Winkler"), "Bold", 34),
    z("Wort „anfechten“ nicht nötig", 110, 400, "wort", "Bold", 34),
    z("unzweideutig: Vertrag soll wegen des Irrtums", 150, 460, beim("wort", "unzweideutig"), size=34),
    z("nicht gelten", 150, 512, beim("wort", "gelten"), size=34),
    zit("BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 29", 150, 570, beim("wort", "will")),
    blk(110, 640, 1040, 160, GRUEN, "s3ok", [("„Ich habe mich vertippt, ich lasse das", "Bold", 34, INK),
                                            ("so nicht gelten.“  Das reicht.", "ExtraBold", 36, INK)]),
    ficon("tabler", "device-mobile", X2 - 80, 550, 56, "s3", fuell=WEISS),
    ficon("tabler", "phone-call", X1, 380, 100, beim("gegner", "Winkler"), fuell=GRUEN),
    *fig("WI", X1, 930, 480, [("s3", "ruhig"), ("s3ok", "aerger")]),
    *fig("IL", X2, 930, 480, [("s3", "ernst")], d=0.2),
    pl("Herr Winkler", X1, 952, "s3", fill=BLAU, size=28, anker="m", d=0.2),
    pl("Ilse", X2, 952, "s3", fill=LILA, size=30, anker="m", d=0.3),
]))

# K 4. Anfechtungsfrist ---------------------------------------------------------------------------------------------------------
P4 = f"{PA} › 4. Anfechtungsfrist"
folie([("s4", f"{P4}, § 121 BGB"), ("p124", f"{P4} › Täuschung, Drohung, § 124 BGB"),
       ("zehn", f"{P4} › Höchstfrist, §§ 121 II, 124 III BGB")], rechts_frei([
    *tafel("s4", "Schritt 4: Anfechtungsfrist"),
    z("Irrtum, § 121 Abs. 1 BGB: unverzüglich", 110, 190, "p121", "Bold", 36),
    z("= ohne schuldhaftes Zögern", 150, 250, beim("p121", "ohne"), size=34),
    z("ab Kenntnis des Fehlers", 150, 302, beim("p121", "sobald"), size=34),
    pl("9:00 gelesen", 230, 400, "s4ok", fill=WEISS, size=28, anker="m"),
    pl("sofort: Anruf", 520, 400, beim("s4ok", "sofort"), fill=GRUEN, size=28, anker="m"),
    ok(700, 405, beim("s4ok", "rechtzeitig"), gr=22),
    z("rechtzeitig", 745, 385, beim("s4ok", "rechtzeitig"), "Bold", 34),
    z("Täuschung, Drohung: ein Jahr, § 124 Abs. 1 BGB", 110, 500, "p124", "Bold", 34),
    z("Höchstfrist: zehn Jahre nach Abgabe,", 110, 590, "zehn", "Bold", 34),
    z("§ 121 Abs. 2, § 124 Abs. 3 BGB", 150, 645, beim("zehn", "beiden"), size=34),
    ficon("tabler", "clock", IX, IU, 140, "s4", fuell=WEISS, bis="p124"),
    ficon("tabler", "calendar-event", IX, IU, 130, "p124", fuell=GELB),
    *fig("IL", FX, FB, FR, [("s4", "ruhig"), ("s4ok", "froh")]),
]))

# L 5. kein Ausschluss --------------------------------------------------------------------------------------------------------
P5 = f"{PA} › 5. kein Ausschluss, § 144 BGB"
folie([("s5", P5)], rechts_frei([
    *tafel("s5", "Schritt 5: kein Ausschluss"),
    z("§ 144 Abs. 1 BGB: Anfechtung ausgeschlossen,", 110, 190, "p144", "Bold", 34),
    z("wenn Ilse das Geschäft bestätigt", 150, 245, beim("p144", "wenn"), size=34),
    z("Bestätigung, z. B. in Kenntnis des Anfechtungsrechts:", 110, 330, "bsp", size=32),
    pl("„Schicken Sie ruhig die hundert.“", 150, 385, beim("bsp", "Schicken"), fill=GELB, size=32),
    zit("BGH, Urt. v. 4.12.2015 – V ZR 142/14, Rn. 8", 150, 470, beim("bsp", "Bestätigung")),
    ok(140, 560, "s5ok", gr=22), z("Das hat Ilse nicht getan.", 185, 540, "s5ok", "Bold", 36),
    blk(110, 630, 1040, 90, GRUEN, beim("s5ok", "getan", ende=True), [("Alle fünf Schritte erfüllt", "ExtraBold", 38, INK)]),
    ficon("tabler", "thumb-up", IX, IU, 120, beim("bsp", "Schicken"), fuell=GELB, bis="s5ok"),
    ficon("tabler", "x", IX, IU, 120, "s5ok", fuell=ROT),
    *fig("IL", FX, FB, FR, [("s5", "ruhig"), ("s5ok", "froh")]),
]))

# M Rechtsfolge, § 122 --------------------------------------------------------------------------------------------------------
folie([("folge", "Rechtsfolge · § 142 I BGB"), ("p122", "Rechtsfolge · Vertrauensschaden, § 122 BGB")], rechts_frei([
    *tafel("folge", "Rechtsfolge"),
    blk(110, 180, 1040, 90, ROT, "folge", [("Kaufvertrag von Anfang an nichtig", "ExtraBold", 38, INK)]),
    nein(140, 335, beim("folge", "keine"), gr=20), z("keine 2.000 € Kaufpreis", 185, 315, beim("folge", "keine"), size=34),
    z("§ 122 Abs. 1 BGB: Vertrauensschaden", 110, 410, "p122", "Bold", 36),
    z("Fehler nicht erkennbar (§ 122 Abs. 2 BGB)", 150, 465, beim("p122", "nicht"), size=32, farbe=TEXT),
    ok(140, 555, "spedi", gr=20), z("80 € Spedition, nicht stornierbar", 185, 535, "spedi", "Bold", 34),
    nein(140, 635, "gewinn", gr=20), z("Gewinn aus dem Geschäft", 185, 615, "gewinn", size=34),
    z("= Erfüllungsinteresse, nur die Obergrenze", 185, 670, beim("gewinn", "Erfüllungsinteresse"), size=34),
    ficon("tabler", "cash-banknote", X1, 380, 150, "folge", fuell=GRUEN, bis="p122"),
    ficon("tabler", "truck-delivery", X1, 380, 170, "spedi", fuell=GELB),
    pl("80 €", X1, 170, "spedi", fill=GELB, size=30, anker="m"),
    *fig("WI", X1, 930, 480, [("folge", "aerger"), ("spedi", "ruhig")]),
    *fig("IL", X2, 930, 480, [("folge", "froh"), ("p122", "ernst")], d=0.2),
    pl("Herr Winkler", X1, 952, "folge", fill=BLAU, size=28, anker="m", d=0.2),
    pl("Ilse", X2, 952, "folge", fill=LILA, size=30, anker="m", d=0.3),
]))

# N Gegenfall: arglistige Täuschung (Lieferwagen) ---------------------------------------------------------------------------
JOn = ("JO_redet_r", X1, 930, 480)
folie([("jg", "Gegenfall · arglistige Täuschung, § 123 I BGB"), ("t124", "Gegenfall › Frist, § 124 BGB"),
       ("t122", "Gegenfall › kein § 122 BGB")], rechts_frei([
    *tafel("jg", "Gegenfall: Täuschung"),
    z("Ilse kauft von Jörg einen gebrauchten Lieferwagen", 110, 185, beim("jg", "Ilse"), size=32),
    pl("„unfallfrei“", 150, 240, "j1", fill=GELB, size=30),
    z("Jörg weiß: schwerer Unfall", 110, 330, "unfall", "Bold", 34),
    z("Ilse erfährt es ein halbes Jahr später", 150, 385, beim("unfall", "Ilse"), size=32),
    ok(140, 470, "t123", gr=20), z("arglistige Täuschung, § 123 Abs. 1 BGB", 185, 450, "t123", "Bold", 34),
    z("bewusst falsche Tatsache vorgespiegelt", 185, 505, beim("t123", "spiegelt"), size=32),
    zit("BGH, Urt. v. 7.2.2018 – IV ZR 53/17, Rn. 28", 185, 555, beim("t123", "kauft")),
    ok(140, 640, "t124", gr=20), z("ein Jahr ab Entdeckung, § 124 BGB", 185, 620, "t124", "Bold", 34),
    nein(140, 725, "t122", gr=20), z("kein § 122 BGB: nur §§ 119, 120", 185, 705, "t122", "Bold", 34),
    ficon("tabler", "truck", (X1 + X2) // 2, 330, 200, beim("jg", "Lieferwagen"), fuell=WEISS, bis="j1"),
    ficon("tabler", "car-crash", (X1 + X2) // 2, 330, 180, "unfall", fuell=ROT, bis=beim("unfall", "Werkstatt")),
    ficon("tabler", "tools", (X1 + X2) // 2, 330, 150, beim("unfall", "Werkstatt"), fuell=GELB),
    pl("½ Jahr später", (X1 + X2) // 2, 130, beim("unfall", "halbes"), fill=WEISS, size=28, anker="m"),
    *fig("JO", X1, 930, 480, [(beim("jg", "Jörg"), "ruhig_r")], bis="j1"),
    *redet("JO_redet_r", X1, 930, 480, "j1", "unfall"),
    peep_voll("JO_ruhig_r", X1, 930, 480, "unfall", anim="cut", bis="t123"),
    peep_voll("JO_ertappt_r", X1, 930, 480, "t123", anim="cut"),
    pl("Jörg", X1, 952, beim("jg", "Jörg"), fill=GRUEN, size=30, anker="m"),
    *fig("IL", X2, 930, 480, [("jg", "froh"), ("unfall", "schreck"), ("t124", "ernst")], d=0.2),
    pl("Ilse", X2, 952, "jg", fill=LILA, size=30, anker="m", d=0.3),
    blase("sprech", 560, 200, "j1", 1500, 180, inhalt=["Der ist unfallfrei, versprochen!"], textsize=32,
          figur=JOn, bis="unfall"),
]))

# O Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · erst auslegen, dann anfechten"), ("tipp3", "Klausurtipp · Klausurkonvention")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Erst auslegen, dann anfechten.", 200, 200, beim("tipp", "Erst"), "Bold", 38),
    z("Übereinstimmend Gewolltes gilt,", 110, 300, "tipp2", size=34),
    z("auch wenn sich jemand verschrieben hat", 150, 355, beim("tipp2", "auch"), size=34),
    zit("BGH, Urt. v. 16.12.2021 – IX ZR 223/20, Rn. 19", 150, 410, beim("tipp2", "verschrieben")),
    z("Beide wussten: 10 Kartons gemeint?", 110, 480, beim("tipp2", "Wussten"), size=34),
    ok(140, 560, beim("tipp2", "nichts"), gr=20), z("nichts anzufechten", 185, 540, beim("tipp2", "nichts"), "Bold", 34),
    z("5 Schritte = Klausurkonvention,", 110, 640, "tipp3", "Bold", 36),
    z("kein Gesetzestext", 150, 695, beim("tipp3", "kein"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# P Klausurschema --------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Winkler gegen Ilse, § 433 Abs. 2 BGB"), 110, 90, "sch", 46),
    z("I. Kaufvertrag geschlossen", K1, 195, "k1", "Bold", 38, rechts=1820),
    z("II. nichtig nach § 142 Abs. 1 BGB?", K1, 265, "k2", "Bold", 38, rechts=1820),
    z("1. Anfechtungsgegenstand", K2, 335, "k21", size=36, rechts=1820),
    z("2. Anfechtungsgrund mit Kausalität", K2, 395, "k22", size=36, rechts=1820),
    z("3. Anfechtungserklärung gegenüber dem Gegner", K2, 455, "k23", size=36, rechts=1820),
    z("4. Anfechtungsfrist", K2, 515, "k24", size=36, rechts=1820),
    z("5. kein Ausschluss", K2, 575, "k25", size=36, rechts=1820),
    *plusminus("III. Ergebnis: kein Kaufpreis", K1, 655, "k3", False, size=38, stil="Bold"),
    z("aber Vertrauensschaden nach § 122 BGB", K2, 725, beim("k3", "aber"), size=36, rechts=1820),
])

# Q Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer wirksam anficht, vernichtet", 0)], [("das Geschäft ", 0), ("von Anfang an.", "a")]],
                750, 310, 48, "merke", {"a": beim("merke", "von")}),
    *markertext([[("Wer wegen eines Irrtums anficht,", 0)], [("ersetzt den ", 0), ("Vertrauensschaden", "b"), (",", 0)],
                 [("es sei denn, der andere kannte", 0)], [("den Fehler oder musste ihn kennen.", 0)]], 750, 520, 42, "m2",
                {"b": beim("m2", "Vertrauensschaden")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
