"""Folge 043 · Stellvertretung Schema: Wann bindet der Vertreter den Chef? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Wiebke kauft für die Werbeagentur von Herrn Gruber fünfzig Bürostühle bei Frau Engel), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Der Auftrag (Agentur), B Im Möbelhaus, C Die Rechnung und die Frage, D Sachverhalt,
E Anspruch, F Wortlaut § 164 I, G 1. eigene Willenserklärung, H 2. im fremden Namen, I 3. mit Vertretungsmacht
(Wortlaut § 167 I), J Rechtsfolge und § 166 I, K Gegenfall Überschreitung (Wortlaut § 177 I, Ausblick § 179),
L Gegenfall Rechtsscheinsvollmacht, M § 181, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Ladenglocke, rollender Bürostuhl, aufgerissener Umschlag; Freesound CC0).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/schild wie in Folge 041 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_043/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (236, 214, 178, 255)
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
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
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


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_043/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe, automatisch umbrochen.
    marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die Wortgruppe
    (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    breite = w - 56
    zeilen, cur = [], ""
    for wort in text.split():
        t = (cur + " " + wort).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = wort
    zeilen.append(cur)
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 020/025/028/032): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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




def nummern(x0, y, cue_liste, schritt=86, size=34, fill=GELB):
    """Runde Schrittnummern, jede zu ihrem Cue."""
    return [pl(str(i + 1), x0 + i * schritt, y, c, fill=fill, size=size, anker="m") for i, c in enumerate(cue_liste)]


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GR_F, WI_F, EN_F = BLAU, GRUEN, ROT         # Farben der Namensschilder (passend zur Kleidung)
K1, K2, K3 = 150, 210, 270
PA = "I. Kaufvertrag, § 164 I BGB"
MITTE = (X1 + X2) // 2


def stuhl(cx, cue, fuell, breite=150, unten=BODEN - 2, **k):
    """Bürostuhl (Phosphor office-chair, MIT), mit Palettenfarbe gefüllt."""
    return ficon("ph", "office-chair", cx, unten, breite, cue, fuell=fuell, **k)


def agentur(cue):
    """Büro der Werbeagentur: Boden, Schreibtisch mit Bildschirm, alter Bürostuhl."""
    return [hart(linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)),
            ficon("tabler", "desk", 500, BODEN - 4, 360, cue, fuell=GELB, anim="cut"),
            ficon("tabler", "device-desktop", 470, 645, 150, cue, fuell=WEISS, anim="cut"),
            stuhl(900, cue, GRAU, breite=160, anim="cut")]


# A Fall: der Auftrag in der Agentur ------------------------------------------------------------------------------------
GR_A, WI_A = 1200, 1620
GRa = ("GR_redet_r", GR_A, BODEN, FH)
folie([(NULL, "Fall · Der Auftrag")], [
    hart(pl("Werbeagentur Gruber", 70, 40, NULL, fill=GELB, size=44)),
    *agentur(NULL),
    *fig("GR", GR_A, BODEN, FH, [(NULL, "ruhig_r")], bis="g1", erst="cut"),
    *redet("GR_redet_r", GR_A, BODEN, FH, "g1", "laden"),
    hart(schild("Herr Gruber", GR_A, NULL, GR_F, unten=BODEN, d=0.0)),
    *fig("WI", WI_A, BODEN, FH, [(beim("auftrag", "Angestellte"), "ruhig"), (beim("g1", "Höchstens"), "denkt")]),
    schild("Wiebke, Angestellte", WI_A, beim("auftrag", "Angestellte"), WI_F, unten=BODEN, d=0.0),
    pl("neue Bürostühle", 900, 600, beim("auftrag", "Bürostühle"), fill=WEISS, size=28, anker="m", bis="g1"),
    pl("50 Bürostühle", 900, 540, beim("g1", "fünfzig"), fill=GRUEN, size=30, anker="m"),
    pl("höchstens 200 € das Stück", 900, 610, beim("g1", "Höchstens"), fill=GELB, size=28, anker="m"),
    blase("sprech", 780, 260, "g1", 1000, 220, inhalt=["Wiebke, kaufen Sie fünfzig Bürostühle", "für die Agentur.",
                                                     "Höchstens zweihundert Euro das Stück!"], textsize=32,
          figur=GRa, bis="laden"),
])

# B Fall: im Möbelhaus ----------------------------------------------------------------------------------------------------
WI_B, EN_B = 1300, 1700
WIb = ("WI_redet_r", WI_B, BODEN, FH)
ENb = ("EN_redet", EN_B, BODEN, FH)
T_TEST = T_(beim("probe", "testet"))
STUHL_T = stuhl(1090, "laden", GRUEN)
folie([("laden", "Fall · Im Möbelhaus")], [
    pl("Möbelhaus Engel", 70, 40, "laden", fill=GELB, size=44),
    linienzug([(60, BODEN), (1860, BODEN)], "laden", breite=7, farbe=INK),
    szene(ficon("tabler", "building-store", 200, BODEN - 2, 240, "laden", fuell=ROT), "043glocke*", 0.8),
    stuhl(470, "laden", BLAU), stuhl(680, "laden", LILA),
    szene(bewegt(STUHL_T, beim("probe", "testet"), ("probe", round(T_TEST - T_("probe") + 1.5, 3)), -200, 0),
          "043stuhl*", 1.0, round(T_TEST - T_("laden"), 3) - 0.2),
    pl("180 €", 1090, 600, beim("probe", "hundertachtzig"), fill=GRUEN, size=30, anker="m"),
    *fig("WI", WI_B, BODEN, FH, [("laden", "ruhig"), (beim("probe", "wählt"), "froh")], bis="w1"),
    *redet("WI_redet_r", WI_B, BODEN, FH, "w1", "e1"),
    peep_voll("WI_froh_r", WI_B, BODEN, FH, "e1", anim="cut"),
    schild("Wiebke", WI_B, "laden", WI_F, unten=BODEN),
    *fig("EN", EN_B, BODEN, FH, [(beim("laden", "Frau"), "ruhig")], bis="e1"),
    *redet("EN_redet", EN_B, BODEN, FH, "e1", "rechnung"),
    schild("Frau Engel, Möbelhaus", EN_B, beim("laden", "Frau"), EN_F, unten=BODEN, d=0.0),
    blase("sprech", 700, 220, "w1", 1250, 220, inhalt=["Ich kaufe für die Agentur Gruber", "fünfzig Stück von diesem Modell."],
          textsize=32, figur=WIb, bis="e1"),
    pl("50 Stück", 680, 560, beim("w1", "fünfzig"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 760, 220, "e1", 1300, 220, inhalt=["Sehr gern. Das macht neuntausend Euro,",
                                                     "die Rechnung geht an Herrn Gruber."], textsize=32,
          figur=ENb, bis="rechnung"),
    pl("9.000 €", 680, 480, beim("e1", "neuntausend"), fill=GELB, size=34, anker="m"),
])

# C Fall: die Rechnung, die Frage ----------------------------------------------------------------------------------------
GR_C, WI_C = 1200, 1640
GRc = ("GR_redet", GR_C, BODEN, FH)
folie([("rechnung", "Fall · Die Rechnung"), ("frage", "Fall · Die Frage")], [
    pl("Eine Woche später", 70, 40, "rechnung", fill=GELB, size=44, bis="frage"),
    *agentur("rechnung"),
    szene(ficon("tabler", "mail-opened", 620, 640, 90, beim("rechnung", "öffnet"), fuell=WEISS,
                bis=beim("rechnung", "Rechnung")), "043umschlag*", 0.8),
    ficon("ph", "invoice", 620, 640, 100, beim("rechnung", "Rechnung"), fuell=WEISS, bis="frage"),
    pl("Rechnung: 9.000 €", 620, 470, beim("rechnung", "Rechnung"), fill=GELB, size=30, anker="m", bis="frage"),
    *fig("GR", GR_C, BODEN, FH, [("rechnung", "ruhig"), (beim("rechnung", "Rechnung"), "schreck")], bis="g2"),
    *redet("GR_redet", GR_C, BODEN, FH, "g2", "frage"),
    peep_voll("GR_aerger", GR_C, BODEN, FH, "frage", anim="cut"),
    schild("Herr Gruber", GR_C, "rechnung", GR_F, unten=BODEN),
    blase("sprech", 900, 230, "g2", 820, 220, inhalt=["Ich habe mit Frau Engel nie ein Wort gewechselt.",
                                                    "Warum soll ich zahlen?"], textsize=32, figur=GRc, bis="frage"),
    pl("Bindet Wiebke ihren Chef?", 760, 140, beim("frage", "Bindet"), fill=PINK, size=44, anker="m"),
    pl("Stellvertretung in 3 Schritten", 760, 240, beim("frage", "Stellvertretung"), fill=GELB, size=36, anker="m"),
    *nummern(760 - 86, 335, [beim("frage", "drei")] * 3),
    *fig("WI", WI_C, BODEN, FH, [(beim("frage", "Wiebke"), "denkt")]),
    schild("Wiebke", WI_C, beim("frage", "Wiebke"), WI_F, unten=BODEN, d=0.0),
])

# D Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Gruber betreibt als Inhaber eine Werbeagentur. Er sagt zu seiner Angestellten Wiebke: „Kaufen Sie fünfzig "
    "Bürostühle für die Agentur. Höchstens 200 Euro das Stück!“ Wiebke testet im Möbelhaus von Frau Engel mehrere "
    "Modelle, wählt selbst einen Stuhl für 180 Euro und erklärt: „Ich kaufe für die Agentur Gruber fünfzig Stück von "
    "diesem Modell.“ Frau Engel ist einverstanden: 9.000 Euro, die Rechnung geht an Herrn Gruber.",
    "Herr Gruber will nicht zahlen. Er habe mit Frau Engel nie ein Wort gewechselt.",
], "Muss Herr Gruber die 9.000 Euro zahlen?")

# E Anspruch -------------------------------------------------------------------------------------------------------------
folie([("ansp", "Engel gegen Gruber · § 433 II BGB")], rechts_frei([
    *tafel("ansp", "Engel gegen Gruber: 9.000 €"),
    z("Anspruch: § 433 Abs. 2 BGB (Kaufpreis)", 110, 200, beim("ansp", "Paragraf"), "Bold", 38),
    z("nötig: Kaufvertrag mit Herrn Gruber", 110, 300, "vertrag", size=36),
    nein(140, 400, beim("vertrag", "Erklärt"), gr=20),
    z("erklärt hat aber nur Wiebke", 185, 380, beim("vertrag", "Erklärt"), "Bold", 36),
    ficon("tabler", "cash-banknote", MITTE, 390, 200, "ansp", fuell=GRUEN),
    pl("9.000 €", MITTE, 180, "ansp", fill=GELB, size=32, anker="m"),
    *fig("EN", X1, FB, FH, [("ansp", "ruhig")]),
    *fig("GR", X2, FB, FH, [("ansp", "ruhig"), (beim("vertrag", "Erklärt"), "denkt")], d=0.2),
    schild("Frau Engel", X1, "ansp", EN_F),
    schild("Herr Gruber", X2, "ansp", GR_F, d=0.3),
]))

# F Wortlaut § 164 I 1 ---------------------------------------------------------------------------------------------------
W164 = ("„Eine Willenserklärung, die jemand innerhalb der ihm zustehenden Vertretungsmacht im Namen des Vertretenen "
        "abgibt, wirkt unmittelbar für und gegen den Vertretenen.“")
w164_els, w164_y = wortlaut(80, 190, 1100, W164, "§ 164 Abs. 1 Satz 1 BGB", "p164", marken=[
    ("Willenserklärung", beim("p164", "Willenserklärung")),
    ("innerhalb der ihm", beim("p164", "innerhalb")), ("zustehenden Vertretungsmacht", beim("p164", "zustehenden")),
    ("im Namen des Vertretenen", beim("p164", "im")),
    ("wirkt unmittelbar für und gegen den Vertretenen", beim("p164", "wirkt"))], size=38)
folie([("p164", "§ 164 I BGB › Wortlaut")], rechts_frei([
    titel(glyphen("Der Wortlaut"), 110, 90, "p164", 50),
    *w164_els,
    blk(80, w164_y + 50, 1100, 100, GELB, "drei", [("Daraus: drei Prüfungspunkte", "ExtraBold", 38, INK)]),
    *nummern(630 - 86, w164_y + 210, [beim("drei", "drei")] * 3, schritt=86, fill=WEISS),
    ficon("tabler", "book", IX, IU, 140, "p164", fuell=GELB),
    *fig("WI", FX, FB, FR, [("p164", "ruhig"), (beim("p164", "wirkt"), "froh")]),
    schild("Wiebke", FX, "p164", WI_F),
]))

# G 1. eigene Willenserklärung -----------------------------------------------------------------------------------------------
P1 = f"{PA} › 1. eigene Willenserklärung"
folie([("s1", P1), ("bote", f"{P1} › Bote oder Vertreter?"), ("p165", f"{P1} › § 165 BGB")], rechts_frei([
    *tafel("s1", "1. eigene Willenserklärung"),
    z("Bote: überbringt nur eine fremde Erklärung", 110, 190, "bote", size=36),
    z("Vertreter: erklärt selbst", 110, 250, beim("bote", "Vertreter"), "Bold", 36),
    z("entscheidend: Auftreten nach außen", 110, 330, "aussen", size=36),
    zit("BGH, Urt. v. 25.9.2019 – IV ZR 99/18, Rn. 32", 150, 385, beim("aussen", "auftritt")),
    z("Wiebke wählt das Modell selbst aus", 110, 465, "s1ok", size=36),
    ok(140, 545, beim("s1ok", "Vertreterin"), gr=22),
    z("Vertreterin, keine Botin", 185, 525, beim("s1ok", "Vertreterin"), "Bold", 38),
    blk(110, 640, 1040, 150, GELB, "p165", [("§ 165 BGB: Auch eine 17-jährige Praktikantin", "Bold", 34, INK),
                                           ("könnte wirksam vertreten.", "ExtraBold", 36, INK)]),
    ficon("tabler", "mail", IX, IU, 130, "bote", fuell=WEISS, bis=beim("bote", "Vertreter")),
    ficon("tabler", "message", IX, IU, 130, beim("bote", "Vertreter"), fuell=GRUEN, bis="s1ok"),
    stuhl(IX, "s1ok", GRUEN, breite=140, unten=IU, bis="p165"),
    ficon("tabler", "school", IX, IU, 140, "p165", fuell=GELB),
    *fig("WI", FX, FB, FR, [("s1", "ruhig"), ("bote", "denkt"), ("s1ok", "froh"), ("p165", "strahlt")]),
    schild("Wiebke", FX, "s1", WI_F),
]))

# H 2. im fremden Namen ------------------------------------------------------------------------------------------------------
P2 = f"{PA} › 2. im fremden Namen"
folie([("s2", P2), ("umst", f"{P2} › Offenkundigkeit, § 164 I 2 BGB"), ("unt", f"{P2} › unternehmensbezogenes Geschäft"),
       ("angeht", f"{P2} › Geschäft für den, den es angeht"), ("p164b", f"{P2} › § 164 II BGB")], rechts_frei([
    *tafel("s2", "2. im fremden Namen"),
    z("Offenkundigkeitsprinzip", 110, 175, beim("s2", "Offenkundigkeitsprinzip"), "Bold", 34),
    ok(140, 250, beim("ausdr", "ausdrücklich"), gr=20),
    z("ausdrücklich: „für die Agentur Gruber“", 185, 230, beim("ausdr", "ausdrücklich"), size=34),
    z("§ 164 Abs. 1 Satz 2 BGB: Umstände genügen", 110, 300, "umst", size=34),
    z("unternehmensbezogenes Geschäft:", 110, 375, beim("unt", "unternehmensbezogene"), "Bold", 34),
    z("im Zweifel wird der Inhaber Vertragspartner", 150, 425, beim("unt", "unternehmensbezogene"), size=32),
    zit("BGH, Urt. v. 31.7.2012 – X ZR 154/11, Rn. 10", 150, 472, beim("unt", "Geschäft", ende=True)),
    z("Bargeschäft des täglichen Lebens: Offenlegung", 110, 535, "angeht", size=32),
    z("darf fehlen, wenn der Partner gleichgültig ist", 150, 582, beim("angeht", "gleichgültig"), size=32),
    z("= Geschäft für den, den es angeht", 150, 630, beim("angeht", "Geschäft"), "Bold", 32),
    zit("BGH, Urt. v. 16.10.2015 – V ZR 240/14, Rn. 10", 150, 677, beim("angeht", "angeht", ende=True)),
    blk(110, 735, 1040, 130, ROT, "p164b", [("§ 164 Abs. 2 BGB: Wille unerkennbar,", "Bold", 34, INK),
                                           ("dann ist Wiebke selbst gebunden", "ExtraBold", 36, INK)]),
    pl("„für die Agentur Gruber“", MITTE, 170, beim("ausdr", "ausdrücklich"), fill=WEISS, size=28, anker="m", bis="unt"),
    ficon("tabler", "building", MITTE, 390, 150, "unt", fuell=BLAU, bis="angeht"),
    pl("Inhaber: Herr Gruber", MITTE, 170, beim("unt", "Inhaber"), fill=BLAU, size=28, anker="m", bis="angeht"),
    ficon("tabler", "bread", MITTE, 390, 150, beim("angeht", "Bargeschäften"), fuell=GELB, bis="p164b"),
    *fig("WI", X1, FB, FH, [("s2", "ruhig_r"), (beim("ausdr", "ausdrücklich"), "froh_r"), ("p164b", "schreck")]),
    *fig("EN", X2, FB, FH, [("s2", "ruhig"), ("unt", "denkt"), ("angeht", "froh")], d=0.2),
    schild("Wiebke", X1, "s2", WI_F),
    schild("Frau Engel", X2, "s2", EN_F, d=0.3),
]))

# I 3. mit Vertretungsmacht (Wortlaut § 167 I) --------------------------------------------------------------------------------
P3 = f"{PA} › 3. mit Vertretungsmacht"
W167 = ("„Die Erteilung der Vollmacht erfolgt durch Erklärung gegenüber dem zu Bevollmächtigenden oder dem Dritten, "
        "dem gegenüber die Vertretung stattfinden soll.“")
w167_els, w167_y = wortlaut(80, 290, 1100, W167, "§ 167 Abs. 1 BGB", "p167", marken=[
    ("Bevollmächtigenden", beim("p167", "Vertreter")), ("oder dem Dritten", beim("p167", "Dritten"))], size=32)
folie([("s3", P3), ("p1662", f"{P3} › Vollmacht, §§ 166 II, 167 I BGB"), ("umfang", f"{P3} › Umfang der Vollmacht")],
      rechts_frei([
    *tafel("s3", "3. mit Vertretungsmacht"),
    z("Vollmacht = durch Rechtsgeschäft erteilte", 110, 175, "p1662", size=34),
    z("Vertretungsmacht, § 166 Abs. 2 BGB", 150, 225, beim("p1662", "Vollmacht"), "Bold", 34),
    *w167_els,
    ok(140, w167_y + 55, "innen", gr=20),
    z("Innenvollmacht an Wiebke, mündlich genügt", 185, w167_y + 35, "innen", "Bold", 34),
    z("Umfang: 50 Stühle, höchstens 200 € das Stück", 110, w167_y + 105, "umfang", size=34),
    ok(140, w167_y + 190, "s3ok", gr=20),
    z("180 € liegen darunter", 185, w167_y + 170, "s3ok", size=34),
    blk(110, w167_y + 235, 1040, 90, GRUEN, beim("s3ok", "Vollmacht"), [("Die Vollmacht deckt den Kauf.", "ExtraBold", 36, INK)]),
    ficon("tabler", "message", MITTE, 380, 120, "innen", fuell=WEISS),
    pl("höchstens 200 €", MITTE, 170, beim("umfang", "höchstens"), fill=GELB, size=28, anker="m"),
    pl("180 €", MITTE, 240, "s3ok", fill=GRUEN, size=28, anker="m"),
    *fig("GR", X1, FB, FH, [("s3", "ruhig_r"), ("innen", "froh_r")]),
    *fig("WI", X2, FB, FH, [("s3", "ruhig"), ("s3ok", "strahlt")], d=0.2),
    schild("Herr Gruber", X1, "s3", GR_F),
    schild("Wiebke", X2, "s3", WI_F, d=0.3),
]))

# J Rechtsfolge, Wissenszurechnung ---------------------------------------------------------------------------------------------
folie([("folge", "Rechtsfolge · § 164 I BGB"), ("p166", "Rechtsfolge › Wissenszurechnung, § 166 I BGB")], rechts_frei([
    *tafel("folge", "Rechtsfolge"),
    blk(110, 175, 1040, 90, GRUEN, "folge", [("wirkt unmittelbar für und gegen Herrn Gruber", "ExtraBold", 36, INK)]),
    ok(140, 330, "zahlt", gr=20), z("Herr Gruber ist Vertragspartner: 9.000 €", 185, 310, "zahlt", "Bold", 34),
    nein(140, 395, beim("zahlt", "Wiebke"), gr=20), z("Wiebke selbst ist nicht verpflichtet", 185, 375, beim("zahlt", "Wiebke"), size=34),
    z("§ 166 Abs. 1 BGB: Willensmängel und Wissen", 110, 470, "p166", "Bold", 34),
    z("es zählt die Person der Vertreterin", 150, 525, beim("p166", "Person"), size=34),
    z("Wiebke sieht beim Kauf Kratzer", 110, 610, "kratzer", size=34),
    nein(140, 690, beim("kratzer", "keine"), gr=20),
    z("Herr Gruber: keine Mängelrechte, § 442 BGB", 185, 670, beim("kratzer", "keine"), "Bold", 34),
    ficon("tabler", "cash-banknote", MITTE, 390, 170, "zahlt", fuell=GRUEN, bis="p166"),
    stuhl(MITTE, "kratzer", GRUEN, breite=140, unten=390),
    pl("Kratzer", MITTE, 170, beim("kratzer", "Kratzer"), fill=ROT, size=28, anker="m"),
    *fig("GR", X1, FB, FH, [("folge", "ruhig"), ("zahlt", "ernst"), (beim("kratzer", "keine"), "aerger")]),
    *fig("EN", X2, FB, FH, [("folge", "ruhig"), ("zahlt", "froh")], bis="p166", d=0.2),
    schild("Herr Gruber", X1, "folge", GR_F),
    schild("Frau Engel", X2, "folge", EN_F, d=0.3, bis="p166"),
    *fig("WI", X2, FB, FH, [("p166", "ruhig"), ("kratzer", "denkt")], erst="cut"),
    hart(schild("Wiebke", X2, "p166", WI_F, d=0.0)),
]))

# K Gegenfall 1: Überschreitung, § 177 I, Ausblick § 179 I ---------------------------------------------------------------------
W177 = ("„Schließt jemand ohne Vertretungsmacht im Namen eines anderen einen Vertrag, so hängt die Wirksamkeit des "
        "Vertrags für und gegen den Vertretenen von dessen Genehmigung ab.“")
w177_els, w177_y = wortlaut(80, 345, 1100, W177, "§ 177 Abs. 1 BGB", "p177", marken=[
    ("ohne Vertretungsmacht", beim("p177", "ohne")), ("von dessen Genehmigung ab", beim("p177", "Genehmigung"))], size=31)
GRk = ("GR_redet", X2, FB, FH)
folie([("ueber", "Gegenfall · Überschreitung der Vollmacht"), ("p177", "Gegenfall › § 177 I BGB"),
       ("p179", "Gegenfall › Ausblick: § 179 I BGB")], rechts_frei([
    *tafel("ueber", "Gegenfall: Überschreitung"),
    z("Designerstühle: 400 € das Stück", 110, 175, beim("ueber", "Designerstühle"), "Bold", 34),
    z("Frau Engel weiß von der Grenze nichts", 150, 225, beim("ueber", "Frau"), size=32),
    nein(140, 300, "ueber2", gr=20),
    z("überschreitet die Vollmacht: ohne Vertretungsmacht", 185, 280, "ueber2", "Bold", 32),
    *w177_els,
    z("= schwebend unwirksam", 110, w177_y + 20, "schwebend", "Bold", 34),
    nein(140, w177_y + 95, beim("g3", "genehmige"), gr=20),
    z("Herr Gruber genehmigt nicht", 185, w177_y + 75, beim("g3", "genehmige"), size=34),
    z("§ 179 Abs. 1 BGB: Wiebke haftet selbst,", 110, w177_y + 140, "p179", "Bold", 34),
    z("Wahl: Erfüllung oder Schadensersatz", 150, w177_y + 192, beim("p179", "Erfüllung"), size=34),
    ficon("ph", "armchair", X1, 400, 140, beim("ueber", "Designerstühle"), fuell=PINK, bis="g3"),
    pl("400 €", X1, 230, beim("ueber", "vierhundert"), fill=PINK, size=30, anker="m", bis="g3"),
    pl("20.000 €", X1, 300, beim("g3", "Zwanzigtausend"), fill=GELB, size=30, anker="m"),
    *fig("WI", X1, FB, FH, [("ueber", "verliebt_r"), ("ueber2", "sorge_r"), ("p179", "schreck_r")]),
    schild("Wiebke", X1, "ueber", WI_F),
    *fig("GR", X2, FB, FH, [(beim("ueber2", "Vollmacht"), "denkt")], bis="g3", d=0.0),
    *redet("GR_redet", X2, FB, FH, "g3", "p179"),
    peep_voll("GR_aerger", X2, FB, FH, "p179", anim="cut"),
    schild("Herr Gruber", X2, beim("ueber2", "Vollmacht"), GR_F, d=0.0),
    blase("sprech", 600, 200, "g3", 1550, 150, inhalt=["Zwanzigtausend Euro für Stühle?", "Das genehmige ich nicht!"],
          textsize=30, figur=GRk, bis="p179"),
]))

# L Gegenfall 2: Rechtsscheinsvollmacht ----------------------------------------------------------------------------------------
folie([("schein", "Gegenfall · ohne Vollmacht"), ("duld", "Gegenfall › Duldungsvollmacht"),
       ("anschein", "Gegenfall › Anscheinsvollmacht"), ("rs", "Gegenfall › Rechtsscheinsvollmacht")], rechts_frei([
    *tafel("schein", "Gegenfall: Rechtsschein"),
    nein(140, 195, beim("schein", "nie"), gr=20),
    z("keine Vollmacht von Herrn Gruber", 185, 175, beim("schein", "nie"), "Bold", 34),
    z("seit Monaten Käufe bei Frau Engel,", 150, 225, beim("schein", "Monaten"), size=32),
    z("Herr Gruber weiß das und zahlt jedes Mal", 150, 270, beim("schein", "weiß"), size=32),
    z("Duldungsvollmacht: lässt es willentlich geschehen,", 110, 340, "duld", "Bold", 32),
    z("Partner darf auf eine Vollmacht schließen", 150, 385, beim("duld", "darf"), size=32),
    z("Anscheinsvollmacht: kennt es nicht, hätte es aber", 110, 455, "anschein", "Bold", 32),
    z("erkennen und verhindern können; Partner vertraut", 150, 500, beim("anschein", "erkennen"), size=32),
    z("in der Regel: gewisse Dauer und Häufigkeit", 150, 545, beim("anschein", "Regel"), size=32),
    zit("BGH, Urt. v. 11.5.2011 – VIII ZR 289/09, Rn. 15, 16", 150, 592, beim("anschein", "Häufigkeit", ende=True)),
    blk(110, 640, 1040, 90, LILA, "rs", [("nicht ausdrücklich im Gesetz: Rechtsscheinsvollmacht", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 31.7.2012 – X ZR 154/11, Rn. 16 · Urt. v. 18.6.2025 – VIII ZR 219/23, Rn. 41", 110, 742,
        beim("rs", "Rechtsscheinsvollmacht", ende=True), size=24),
    ok(140, 812, "rsok", gr=20),
    z("hier: Bindung aus Duldungsvollmacht möglich", 185, 792, "rsok", "Bold", 34),
    ficon("tabler", "calendar-repeat", MITTE, 390, 140, beim("schein", "Monaten"), fuell=WEISS, bis="duld"),
    ficon("tabler", "eye-check", MITTE, 390, 140, "duld", fuell=GRUEN, bis="anschein"),
    ficon("tabler", "eye-off", MITTE, 390, 140, "anschein", fuell=GELB, bis="rs"),
    ficon("tabler", "scale", MITTE, 390, 150, "rs", fuell=LILA),
    *fig("GR", X1, FB, FH, [("schein", "ruhig_r"), ("anschein", "denkt_r"), ("rsok", "ernst_r")]),
    *fig("WI", X2, FB, FH, [("schein", "froh"), ("rsok", "strahlt")], d=0.2),
    schild("Herr Gruber", X1, "schein", GR_F),
    schild("Wiebke", X2, "schein", WI_F, d=0.3),
]))

# M § 181 in einem Satz -------------------------------------------------------------------------------------------------------
folie([("p181", "Ausblick · Insichgeschäft, § 181 BGB")], rechts_frei([
    *tafel("p181", "Insichgeschäft, § 181 BGB"),
    z("Wiebke verkauft der Agentur", 110, 200, beim("p181", "Verkauft"), size=36),
    z("im Namen von Herrn Gruber", 150, 255, beim("p181", "Namen"), size=36),
    z("ihre eigenen alten Stühle", 150, 310, beim("p181", "eigenen"), "Bold", 36),
    z("Insichgeschäft nur, wenn gestattet", 110, 420, beim("p181", "Insichgeschäft"), "Bold", 36),
    z("oder ausschließlich Erfüllung einer Verbindlichkeit", 150, 475, beim("p181", "ausschließlich"), size=34),
    stuhl(IX, beim("p181", "eigenen"), GRAU, breite=140, unten=IU),
    *fig("WI", FX, FB, FR, [("p181", "ruhig"), (beim("p181", "Insichgeschäft"), "denkt")]),
    schild("Wiebke", FX, "p181", WI_F),
]))

# N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · § 164 BGB ist keine Anspruchsgrundlage"), ("tipp3", "Klausurtipp · Reihenfolge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§ 164 BGB ist keine Anspruchsgrundlage.", 200, 200, beim("tipp", "Paragraf"), "Bold", 38),
    z("Prüfen beim Vertragsschluss,", 110, 300, "tipp2", size=36),
    z("also im Anspruch auf den Kaufpreis", 150, 355, beim("tipp2", "also"), size=36),
    z("Vertretungsmacht der Reihe nach:", 110, 460, "tipp3", "Bold", 36),
    z("1. echte Vollmacht", 150, 520, beim("tipp3", "echte"), size=36),
    z("2. Rechtsscheinsvollmacht", 150, 575, beim("tipp3", "Rechtsscheinsvollmacht"), size=36),
    z("3. Genehmigung", 150, 630, beim("tipp3", "Genehmigung"), size=36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    schild("Lexi", FX, "tipp", GELB),
])

# O Klausurschema ---------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Engel gegen Gruber, § 433 Abs. 2 BGB"), 110, 90, "sch", 46),
    z("I. Kaufvertrag Engel – Gruber", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("durch die Erklärung von Wiebke, § 164 Abs. 1 BGB", K2, 260, beim("k1", "durch"), size=36, rechts=1820),
    z("1. eigene Willenserklärung", K2, 340, "k11", size=36, rechts=1820),
    z("2. im fremden Namen", K2, 400, "k12", size=36, rechts=1820),
    z("3. mit Vertretungsmacht", K2, 460, "k13", size=36, rechts=1820),
    z("sonst: Genehmigung, § 177 BGB", K3, 520, beim("k13", "sonst"), size=34, farbe=TEXT, rechts=1820),
    *plusminus("II. Ergebnis: Herr Gruber muss zahlen", K1, 610, "k2", True, size=38, stil="Bold"),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Vertreter bindet den Chef, wenn er", 0)], [("eine ", 0), ("eigene Erklärung", "a"), (" im Namen", 0)],
                 [("des Chefs abgibt und ", 0), ("Vertretungsmacht", "b"), (" hat.", 0)]],
                750, 300, 46, "merke", {"a": beim("merke", "eigene"), "b": beim("merke", "Vertretungsmacht")}),
    *markertext([[("Fehlt die Vertretungsmacht,", 0)], [("entscheidet der Chef mit seiner", 0)], [("Genehmigung", "c"), (".", 0)]],
                750, 560, 46, "m2", {"c": beim("m2", "Genehmigung")}),
    *redet("LX_erklaert", 1680, 950, 690, "merke", lexi_bis_ende("merke")),
    schild("Lexi", 1680, "merke", GELB, unten=950),
])
