"""Folge 049 · Rücknahme § 48 VwVfG: Muss das Café die Förderung zurückzahlen? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (kleines Café, Förderung des Landes, Rechenfehler der Förderstelle), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Café: Antrag und Förderbescheid, B Förderstelle zwei Jahre später, C Café: die Rücknahme, D Frage, E Sachverhalt,
F A. Rechtsgrundlage, G B. formell, H Wortlaut § 48 I 1 (rechtswidrig), I Wortlaut § 48 I 2 (begünstigend),
J Wortlaut § 48 II 1–2 (Vertrauensschutz), K Wortlaut § 48 II 3 (Ausschluss), L Abwägung und Ergebnis, M Gegenfall,
N Wortlaut § 48 IV 1 (Jahresfrist), O Ermessen, P Wortlaut § 49a I (Erstattung, Zinsen), Q Ausblick EU-Beihilfen,
R Klausurtipp (Lexi), S Klausurschema, T Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Papier beim Öffnen der beiden Bescheide (Szenen A, C), Umschlag auf dem Schreibtisch
bei der Anhörung (Szene B)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_049/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_049/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe. Automatisch umbrochen
    oder mit festen Zeilen (zeilen=[…], z. B. für Nummernlisten; die Zeilen ergeben zusammen genau den Normtext).
    marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die Wortgruppe
    (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    breite = w - 56
    if zeilen is None:
        zeilen, cur = [], ""
        for wort in text.split():
            t = (cur + " " + wort).strip()
            if f.getlength(t) <= breite:
                cur = t
            else:
                zeilen.append(cur); cur = wort
        zeilen.append(cur)
    else:
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 044/041/032): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------
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
HO_F, WA_F, EB_F = ROT, LILA, GRUEN         # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270


def cafe(cue, anim="pop"):
    """Café in der Altstadt: Ladenfront (Phosphor storefront), Theke (Karte) mit Tasse (Tabler coffee) und Croissant
    (Fluent Emoji High Contrast), Schild „Café“."""
    els = [ficon("ph", "storefront", 300, BODEN - 2, 380, cue, fuell=GELB, anim=anim),
           pl("Café", 300, BODEN + 22, cue, fill=WEISS, size=28, anker="m", anim=anim),
           karte(560, BODEN - 160, 300, 158, cue, fill=HOLZ, rund=10, schatten=0, rand=4),
           ficon("tabler", "coffee", 640, BODEN - 160, 110, cue, fuell=WEISS, anim=anim),
           ficon(HC, "croissant", 780, BODEN - 162, 110, cue, fuell=GELB, anim=anim)]
    if anim == "cut":
        els[2].anim = "cut"
    return els


# A Fall: das Café und der Förderbescheid ---------------------------------------------------------------------------------
HOX = 1080
HOb = ("HO_redfroh_r", HOX, BODEN, FH)
UMSATZ = beim("fall", "Umsatz")
folie([(NULL, "Fall · Das Café und die Förderung")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Ein kleines Café in der Altstadt", 70, 40, NULL, fill=GELB, size=40)),
    *cafe(NULL, anim="cut"),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    pl("Umsatz eingebrochen", 1560, 230, beim("fall", "eingebrochen"), fill=ROT, size=32, anker="m", bis="antrag"),
    # Frau Hofmann
    *fig("HO", HOX, BODEN, FH, [(NULL, "ruhig_r"), (beim("fall", "eingebrochen"), "sorge_r"), ("antrag", "entschl_r"),
                                (beim("bescheid", "bewilligt"), "froh_r")], bis="ho1", erst="cut"),
    *redet("HO_redfroh_r", HOX, BODEN, FH, "ho1", "verbraucht"),
    *fig("HO", HOX, BODEN, FH, [("verbraucht", "ruhig_r"), (beim("verbraucht", "ausgegeben"), "cute_r")], erst="cut"),
    hart(schild("Frau Hofmann, Café", HOX, NULL, HO_F, unten=BODEN, d=0.0)),
    # Antrag und Bescheid
    ficon("tabler", "file-text", 1400, 620, 130, beim("antrag", "beantragt"), fuell=WEISS, bis="verbraucht"),
    pl("Antrag", 1400, 650, beim("antrag", "beantragt"), fill=WEISS, size=28, anker="m", bis="verbraucht"),
    pl("Zahlen richtig", 1400, 715, beim("antrag", "richtig"), fill=GRUEN, size=28, anker="m", bis="verbraucht"),
    szene(ficon("tabler", "file-euro", 1700, 620, 150, beim("bescheid", "Bescheid"), fuell=GELB, bis=beim("verbraucht", "Miete")),
          "049brief*", 0.8, -0.70),
    pl("Förderbescheid", 1700, 650, beim("bescheid", "Bescheid"), fill=WEISS, size=28, anker="m", bis=beim("verbraucht", "Miete")),
    pl("20.000 €", 1700, 715, beim("bescheid", "zwanzigtausend"), fill=GELB, size=32, anker="m", bis=beim("verbraucht", "Miete")),
    blase("sprech", 700, 200, "ho1", 1180, 240, inhalt=["Zwanzigtausend Euro! Damit", "kommen wir durch den Winter."],
          textsize=32, figur=HOb, bis="verbraucht"),
    # Wofür das Geld ausgegeben wird
    ficon("tabler", "home", 1340, 600, 120, beim("verbraucht", "Miete"), fuell=WEISS),
    pl("Miete", 1340, 630, beim("verbraucht", "Miete"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "users", 1540, 600, 120, beim("verbraucht", "Löhne"), fuell=WEISS),
    pl("Löhne", 1540, 630, beim("verbraucht", "Löhne"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "truck", 1745, 600, 130, beim("verbraucht", "Lieferanten"), fuell=WEISS),
    pl("Lieferanten", 1745, 630, beim("verbraucht", "Lieferanten"), fill=WEISS, size=28, anker="m"),
    pl("Geld ausgegeben", 1540, 730, beim("verbraucht", "ausgegeben"), fill=ROT, size=32, anker="m"),
])

# B Fall: zwei Jahre später in der Förderstelle -----------------------------------------------------------------------------
EBX, WAX = 930, 1640
EBb = ("EB_redet_r", EBX, BODEN, FH)
WAb = ("WA_redet", WAX, BODEN, FH)
EB_DA = beim("ebert", "Prüferin")
_tisch = ficon("ph", "desk", 1290, BODEN - 2, 330, "amt", fuell=HOLZ)
TISCH = BODEN - 2 - _tisch.sprite.height
folie([("amt", "Fall · Zwei Jahre später: die Förderstelle"), ("anh", "Fall · Die Anhörung")], [
    linienzug([(60, BODEN), (1860, BODEN)], "amt", breite=7, farbe=INK),
    pl("Zwei Jahre später: die Förderstelle", 70, 40, "amt", fill=GELB, size=40),
    ficon(HC, "office-building", 250, BODEN - 2, 260, "amt", fuell=WEISS),
    pl("Förderstelle", 250, BODEN + 22, "amt", fill=WEISS, size=26, anker="m"),
    _tisch,
    ficon("tabler", "lamp", 1390, TISCH + 4, 80, "amt", fuell=GELB),
    ficon("tabler", "file-search", 1240, TISCH + 4, 90, beim("ebert", "Akte"), fuell=WEISS, bis=beim("eb1", "Rechenfehler")),
    ficon("tabler", "calculator", 1240, TISCH + 4, 90, beim("eb1", "Rechenfehler"), fuell=WEISS, bis="anh"),
    pl("15 %", 1240, TISCH - 230, beim("eb1", "fünfzehn"), fill=ROT, size=32, anker="m", bis="anh"),
    pl("gefördert erst ab 30 %", 1300, TISCH - 160, beim("eb1", "dreißig"), fill=WEISS, size=28, anker="m", bis="anh"),
    # Prüferin Ebert und Herr Wagner
    *fig("EB", EBX, BODEN, FH, [(EB_DA, "ruhig_r")], bis="eb1"),
    *redet("EB_redet_r", EBX, BODEN, FH, "eb1", "wa1"),
    *fig("EB", EBX, BODEN, FH, [("wa1", "ruhig_r"), ("anh", "denkt_r")], erst="cut"),
    schild("Frau Ebert, Prüferin", EBX, EB_DA, EB_F, unten=BODEN, d=0.0),
    *fig("WA", WAX, BODEN, FH, [("amt", "ruhig"), (beim("eb1", "fünfzehn"), "denkt")], bis="wa1"),
    *redet("WA_redet", WAX, BODEN, FH, "wa1", "anh"),
    *fig("WA", WAX, BODEN, FH, [("anh", "ruhig")], erst="cut"),
    schild("Herr Wagner, Förderstelle", WAX, "amt", WA_F, unten=BODEN),
    blase("sprech", 820, 250, "eb1", 760, 250, inhalt=["Herr Wagner, hier ist ein Rechenfehler.",
                                                      "Bei Frau Hofmann ist der Umsatz nur", "um fünfzehn Prozent gesunken.",
                                                      "Gefördert wird erst ab dreißig."], textsize=28, figur=EBb, bis="wa1"),
    blase("sprech", 720, 190, "wa1", 1270, 240, inhalt=["Dann hätte sie nichts bekommen", "dürfen. Wir fordern alles zurück."],
          textsize=30, figur=WAb, bis="anh"),
    # Anhörung
    pl("Anhörung, § 28 VwVfG", 960, 200, beim("anh", "Gelegenheit"), fill=GELB, size=34, anker="m"),
    szene(ficon("ph", "envelope", 1290, TISCH + 4, 120, beim("anh", "Gelegenheit"), fuell=WEISS), "049umschlag*", 0.7, -0.19),
    pl("Stellungnahme", 960, 290, beim("anh", "Stellungnahme"), fill=WEISS, size=30, anker="m"),
])

# C Fall: die Rücknahme im Café ---------------------------------------------------------------------------------------------
HCb = ("HO_redet_r", HOX, BODEN, FH)
folie([("rueck", "Fall · Die Rücknahme")], [
    linienzug([(60, BODEN), (1860, BODEN)], "rueck", breite=7, farbe=INK),
    pl("Einen Monat nach ihrer Antwort", 70, 40, "rueck", fill=GELB, size=40),
    *cafe("rueck"),
    *fig("HO", HOX, BODEN, FH, [("rueck", "denkt_r"), (beim("rueck", "zurück"), "sorge_r")], bis="ho2"),
    *redet("HO_redet_r", HOX, BODEN, FH, "ho2", "frage"),
    schild("Frau Hofmann", HOX, "rueck", HO_F, unten=BODEN),
    szene(ficon("tabler", "file-euro", 1560, 600, 160, beim("rueck", "nimmt"), fuell=ROT), "049brief*", 0.8, -0.70),
    pl("Rücknahme", 1560, 630, beim("rueck", "zurück"), fill=ROT, size=32, anker="m"),
    pl("20.000 € mit Zinsen", 1560, 700, beim("rueck", "zwanzigtausend"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 720, 190, "ho2", 1180, 250, inhalt=["Das Geld ist doch längst ausgegeben.", "Und der Fehler lag beim Amt!"],
          textsize=30, figur=HCb),
])

# D Die Frage -----------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Muss das Café zurückzahlen?")], [
    pl("Muss das Café die Förderung zurückzahlen?", 960, 70, beim("frage", "Muss"), fill=PINK, size=42, anker="m"),
    ficon("ph", "storefront", 420, 640, 300, "frage", fuell=GELB),
    pl("Café", 420, 660, "frage", fill=WEISS, size=28, anker="m"),
    ficon("tabler", "file-euro", 860, 640, 170, beim("frage", "Förderung"), fuell=GELB),
    pl("Förderung: 20.000 €", 860, 660, beim("frage", "Förderung"), fill=WEISS, size=28, anker="m"),
    pl("§ 48 VwVfG", 560, 820, beim("frage2", "achtundvierzig"), fill=GELB, size=36, anker="m"),
    pl("§ 49a VwVfG", 900, 820, beim("frage2", "neunundvierzig"), fill=GELB, size=36, anker="m"),
    *fig("HO", 1560, BODEN, FH, [("frage", "sorge"), ("frage2", "denkt")]),
    schild("Frau Hofmann", 1560, "frage", HO_F, unten=BODEN),
])

# E Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Hofmann führt ein kleines Café. Sie beantragt Geld aus einem Förderprogramm des Landes, das nur bei einem "
    "Umsatzrückgang von mindestens 30 Prozent fördert, und gibt ihre Zahlen richtig an. Die Förderstelle verrechnet sich und "
    "bewilligt durch endgültigen Bescheid 20.000 Euro; der Bescheid nennt nur den Betrag. Frau Hofmann bezahlt damit Miete, "
    "Löhne und Lieferanten. Zwei Jahre später bemerkt Prüferin Ebert: Der Umsatz ist nur um 15 Prozent gesunken. Herr Wagner "
    "hört Frau Hofmann an. Einen Monat nach ihrer Stellungnahme nimmt die Förderstelle den Bescheid zurück und verlangt "
    "20.000 Euro nebst Zinsen.",
    "Bearbeitervermerk: Die Förderstelle ist zuständig. Der Förderbescheid ist unanfechtbar.",
], "Muss Frau Hofmann die Förderung zurückzahlen?")

# F A. Rechtsgrundlage ----------------------------------------------------------------------------------------------------------
RU = "Rücknahme"
folie([("rgl", f"{RU} › A. Rechtsgrundlage"), ("widerruf", f"{RU} › A. Rechtsgrundlage › Abgrenzung: Widerruf, § 49"),
       ("land", f"{RU} › A. Rechtsgrundlage › Landesrecht")], rechts_frei([
    *tafel("rgl", "A. Rechtsgrundlage"),
    z("Förderbescheid: von Anfang an rechtswidrig", 110, 190, beim("rgl", "Förderbescheid"), "Bold", 36),
    ok(150, 268, "abgr", gr=20),
    z("also Rücknahme, § 48 VwVfG", 195, 245, "abgr", "Bold", 36),
    z("Widerruf, § 49 VwVfG: rechtmäßige Verwaltungsakte,", 110, 345, "widerruf", size=34),
    z("etwa bei zweckwidriger Verwendung", 150, 400, beim("widerruf", "zweckwidriger"), size=34),
    zit("§ 49 Abs. 3 Satz 1 Nr. 1 VwVfG", 150, 455, beim("widerruf", "Verwendung")),
    z("Land: eigenes Verfahrensgesetz,", 110, 545, "land", "Bold", 34),
    z("meist mit gleichem Wortlaut", 150, 600, beim("land", "gleichem"), size=34),
    zit("in deinem Land ggf. andere Fundstelle, z. B. Art. 48 BayVwVfG", 150, 655, beim("land", "Wortlaut")),
    ficon("tabler", "file-euro", IX, IU, 130, "rgl", fuell=GELB, bis="land"),
    ficon(HC, "classical-building", IX, IU, 170, "land", fuell=WEISS),
    *fig("HO", FX, FB, FR, [("rgl", "ruhig"), ("widerruf", "denkt"), ("land", "ruhig")]),
    schild("Frau Hofmann", FX, "rgl", HO_F),
]))

# G B. formell --------------------------------------------------------------------------------------------------------------------
folie([("formell", f"{RU} › B. formell: Zuständigkeit"), ("anh2", f"{RU} › B. formell: Anhörung, § 28 I VwVfG")], rechts_frei([
    *tafel("formell", "B. Formelle Rechtmäßigkeit"),
    ok(150, 213, beim("formell", "Zuständig"), gr=20),
    z("Zuständigkeit: die Förderstelle,", 195, 190, beim("formell", "Zuständig"), "Bold", 36),
    z("die auch bewilligt hat", 235, 245, beim("formell", "bewilligt"), size=34),
    z("Anhörung, § 28 I VwVfG:", 110, 345, "anh2", "Bold", 36),
    z("Die Rücknahme greift in ihre Rechte ein.", 150, 400, beim("anh2", "Rücknahme"), size=34),
    ok(150, 493, beim("anh2", "geschehen"), gr=20),
    z("Anhörung ist geschehen", 195, 470, beim("anh2", "geschehen"), "Bold", 34),
    ficon(HC, "office-building", IX, IU, 150, "formell", fuell=WEISS, bis="anh2"),
    ficon("ph", "envelope", IX, IU, 140, "anh2", fuell=WEISS),
    *fig("WA", FX, FB, FR, [("formell", "ruhig")]),
    schild("Herr Wagner", FX, "formell", WA_F),
]))

# H Wortlaut § 48 Abs. 1 Satz 1: rechtswidriger Verwaltungsakt -------------------------------------------------------------------
W4811 = ("„Ein rechtswidriger Verwaltungsakt kann, auch nachdem er unanfechtbar geworden ist, ganz oder teilweise mit Wirkung "
         "für die Zukunft oder für die Vergangenheit zurückgenommen werden.“")
w4811, w4811_y = wortlaut(80, 170, 1100, W4811, "§ 48 Abs. 1 Satz 1 VwVfG", "wl481", marken=[
    ("rechtswidriger Verwaltungsakt", beim("wl481", "rechtswidriger")), ("unanfechtbar", beim("wl481", "unanfechtbar")),
    ("für die Vergangenheit", beim("wl481", "Vergangenheit"))], size=36)
folie([("wl481", f"{RU} › C. materiell › 1. rechtswidriger Verwaltungsakt")], rechts_frei([
    titel(glyphen("Materiell: § 48 Abs. 1 Satz 1"), 110, 75, "wl481", 50),
    *w4811,
    ok(150, w4811_y + 73, beim("rw", "Rechtswidrig"), gr=20),
    z("rechtswidrig: 15 % Umsatzrückgang reichen nicht", 195, w4811_y + 50, beim("rw", "Rechtswidrig"), "Bold", 34),
    z("unanfechtbar: schadet nicht", 195, w4811_y + 120, beim("unanf", "schadet"), size=34),
    ficon("tabler", "file-euro", IX, IU, 130, "wl481", fuell=GELB, bis="rw"),
    ficon("tabler", "calculator", IX, IU, 130, "rw", fuell=WEISS),
    *fig("HO", FX, FB, FR, [("wl481", "ruhig"), ("rw", "denkt")]),
    schild("Frau Hofmann", FX, "wl481", HO_F),
]))

# I Wortlaut § 48 Abs. 1 Satz 2: begünstigend -------------------------------------------------------------------------------------
W4812 = ("„Ein Verwaltungsakt, der ein Recht oder einen rechtlich erheblichen Vorteil begründet oder bestätigt hat "
         "(begünstigender Verwaltungsakt), darf nur unter den Einschränkungen der Absätze 2 bis 4 zurückgenommen werden.“")
w4812, w4812_y = wortlaut(80, 170, 1100, W4812, "§ 48 Abs. 1 Satz 2 VwVfG", "beg", marken=[
    ("begünstigender Verwaltungsakt", beim("beg", "begünstigender")), ("Einschränkungen", beim("beg", "Einschränkungen")),
    ("Absätze 2 bis 4", beim("beg", "Absätze"))], size=36)
folie([("beg", f"{RU} › C. materiell › 2. begünstigender Verwaltungsakt, § 48 I 2")], rechts_frei([
    titel(glyphen("Schutz der Begünstigten: § 48 Abs. 1 Satz 2"), 110, 75, "beg", 46),
    *w4812,
    ok(150, w4812_y + 73, beim("beg2", "begünstigt"), gr=20),
    z("Der Förderbescheid begünstigt Frau Hofmann.", 195, w4812_y + 50, beim("beg2", "begünstigt"), "Bold", 34),
    ficon("tabler", "cash-banknote", IX, IU, 150, "beg", fuell=GRUEN),
    *fig("HO", FX, FB, FR, [("beg", "ruhig"), ("beg2", "froh")]),
    schild("Frau Hofmann", FX, "beg", HO_F),
]))

# J Wortlaut § 48 Abs. 2 Satz 1 und 2: Vertrauensschutz ------------------------------------------------------------------------------
W482 = ("„Ein rechtswidriger Verwaltungsakt, der eine einmalige oder laufende Geldleistung oder teilbare Sachleistung gewährt "
        "oder hierfür Voraussetzung ist, darf nicht zurückgenommen werden, soweit der Begünstigte auf den Bestand des "
        "Verwaltungsaktes vertraut hat und sein Vertrauen unter Abwägung mit dem öffentlichen Interesse an einer Rücknahme "
        "schutzwürdig ist. Das Vertrauen ist in der Regel schutzwürdig, wenn der Begünstigte gewährte Leistungen verbraucht "
        "oder eine Vermögensdisposition getroffen hat, die er nicht mehr oder nur unter unzumutbaren Nachteilen rückgängig "
        "machen kann.“")
w482, w482_y = wortlaut(80, 150, 1100, W482, "§ 48 Abs. 2 Satz 1 und 2 VwVfG", "wl482", marken=[
    ("Geldleistung", beim("wl482", "Geldleistungen")), ("darf nicht zurückgenommen werden,", beim("v1", "Rücknahme")),
    ("vertraut hat", beim("v1", "vertraut")), ("schutzwürdig", beim("v2", "schutzwürdig")),
    ("in der Regel", beim("v3", "Regel")), ("verbraucht", beim("v3", "verbraucht"))], size=29)
folie([("wl482", f"{RU} › C. materiell › 3. Vertrauensschutz, § 48 II")], rechts_frei([
    titel(glyphen("Geldleistung: Vertrauensschutz"), 110, 75, "wl482", 46),
    *w482,
    ok(150, w482_y + 68, beim("v4", "vertraut"), gr=20),
    z("Frau Hofmann hat vertraut,", 195, w482_y + 45, beim("v4", "vertraut"), "Bold", 34),
    z("das Geld ist verbraucht", 195, w482_y + 100, beim("v4", "verbraucht"), "Bold", 34),
    ficon("tabler", "cash-banknote", IX, IU, 150, "wl482", fuell=GRUEN),
    pl("verbraucht", IX, 190, beim("v4", "verbraucht"), fill=ROT, size=30, anker="m"),
    *fig("HO", FX, FB, FR, [("wl482", "ruhig"), ("v4", "cute")]),
    schild("Frau Hofmann", FX, "wl482", HO_F),
]))

# K Wortlaut § 48 Abs. 2 Satz 3: Ausschlussgründe ------------------------------------------------------------------------------------
W4823 = ("„Auf Vertrauen kann sich der Begünstigte nicht berufen, wenn er 1. den Verwaltungsakt durch arglistige Täuschung, "
         "Drohung oder Bestechung erwirkt hat; 2. den Verwaltungsakt durch Angaben erwirkt hat, die in wesentlicher Beziehung "
         "unrichtig oder unvollständig waren; 3. die Rechtswidrigkeit des Verwaltungsaktes kannte oder infolge grober "
         "Fahrlässigkeit nicht kannte.“")
Z4823 = ["„Auf Vertrauen kann sich der Begünstigte nicht berufen, wenn er",
         "1. den Verwaltungsakt durch arglistige Täuschung,", "    Drohung oder Bestechung erwirkt hat;",
         "2. den Verwaltungsakt durch Angaben erwirkt hat, die in", "    wesentlicher Beziehung unrichtig oder unvollständig waren;",
         "3. die Rechtswidrigkeit des Verwaltungsaktes kannte oder", "    infolge grober Fahrlässigkeit nicht kannte.“"]
w4823, w4823_y = wortlaut(80, 150, 1100, W4823, "§ 48 Abs. 2 Satz 3 VwVfG", "aus", marken=[
    ("Auf Vertrauen kann sich der Begünstigte nicht berufen,", beim("aus", "Kein")),
    ("arglistige Täuschung,", beim("aus1", "arglistige")), ("Drohung oder Bestechung", beim("aus1", "Drohung")),
    ("unrichtig oder unvollständig", beim("aus2", "unrichtige")),
    ("Rechtswidrigkeit des Verwaltungsaktes kannte", beim("aus3", "kannte")),
    ("infolge grober Fahrlässigkeit nicht kannte.", beim("aus3", "grob"))], size=30, zeilen=Z4823)
folie([("aus", f"{RU} › C. materiell › 3. Vertrauensschutz › Ausschluss, § 48 II 3")], rechts_frei([
    titel(glyphen("Kein Vertrauen: drei Fälle"), 110, 75, "aus", 46),
    *w4823,
    nein(150, w4823_y + 63, beim("aus1", "Nein"), gr=18),
    z("Nr. 1: keine Täuschung, Drohung, Bestechung", 195, w4823_y + 40, beim("aus1", "Nein"), size=32),
    nein(150, w4823_y + 118, beim("aus2", "Nein"), gr=18),
    z("Nr. 2: ihre Zahlen stimmten", 195, w4823_y + 95, beim("aus2", "Nein"), size=32),
    nein(150, w4823_y + 173, beim("aus3", "Rechenfehler"), gr=18),
    z("Nr. 3: Rechenfehler in der Akte,", 195, w4823_y + 150, beim("aus3", "Rechenfehler"), size=32),
    z("der Bescheid nennt nur den Betrag", 195, w4823_y + 200, beim("aus3", "Bescheid"), size=32),
    ficon("tabler", "file-euro", IX, IU, 130, "aus", fuell=GELB),
    *fig("HO", FX, FB, FR, [("aus", "denkt"), (beim("aus3", "Auch"), "entschl")]),
    schild("Frau Hofmann", FX, "aus", HO_F),
]))

# L Abwägung und Ergebnis ---------------------------------------------------------------------------------------------------------
folie([("abw", f"{RU} › C. materiell › 3. Vertrauensschutz › Abwägung"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("abw", "Abwägung und Ergebnis"),
    z("öffentliches Interesse: Steuergeld zurückholen,", 110, 190, beim("abw", "Steuergeld"), size=34),
    z("besteht bei jeder Rücknahme", 150, 245, beim("abw", "jeder"), size=34),
    ok(150, 343, beim("abw2", "Besondere"), gr=20),
    z("keine besonderen Umstände gegen den Regelfall", 195, 320, beim("abw2", "Besondere"), "Bold", 34),
    blk(110, 440, 1040, 85, GRUEN, beim("erg", "rechtswidrig"), [("Ergebnis: Rücknahme rechtswidrig", "ExtraBold", 38, INK)]),
    z("Ficht Frau Hofmann sie an:", 110, 575, "erg2", "Bold", 34),
    z("Das Café muss die Förderung nicht zurückzahlen.", 150, 630, beim("erg2", "muss"), size=34),
    ficon("ph", "scales", IX, IU, 170, "abw", fuell=WEISS, bis="erg"),
    ficon("tabler", "shield-check", IX, IU, 150, "erg", fuell=GRUEN),
    *fig("HO", FX, FB, FR, [("abw", "ruhig"), ("erg2", "froh")]),
    schild("Frau Hofmann", FX, "abw", HO_F),
]))

# M Gegenfall: falsche Angaben ---------------------------------------------------------------------------------------------------
GF = "Gegenfall"
folie([("gegen", f"{GF} › falsche Angaben, § 48 II 3 Nr. 2"), ("verg", f"{GF} › Rücknahme für die Vergangenheit, § 48 II 4")],
      rechts_frei([
    *tafel("gegen", "Gegenfall", fill=(255, 240, 236, 255)),
    z("Frau Hofmann gibt den Umsatzrückgang zu hoch an", 110, 190, beim("gegen", "Frau"), "Bold", 36),
    ok(150, 288, beim("gegen2", "greift"), gr=20),
    z("§ 48 II 3 Nr. 2 greift", 195, 265, beim("gegen2", "greift"), size=34),
    blk(110, 350, 1040, 85, ROT, beim("gegen2", "Vertrauen"), [("kein Vertrauensschutz", "ExtraBold", 38, INK)]),
    z("§ 48 II 4: in der Regel Rücknahme", 110, 490, "verg", "Bold", 36),
    z("mit Wirkung für die Vergangenheit", 150, 545, beim("verg", "Vergangenheit"), size=34),
    ficon("tabler", "calculator", IX, IU, 130, "gegen", fuell=WEISS),
    pl("zu hoch", IX, 190, beim("gegen", "hoch"), fill=ROT, size=30, anker="m"),
    *fig("HO", FX, FB, FR, [("gegen", "denkt"), ("gegen2", "sorge")]),
    schild("Frau Hofmann", FX, "gegen", HO_F),
]))

# N Wortlaut § 48 Abs. 4 Satz 1: Jahresfrist ---------------------------------------------------------------------------------------
W484 = ("„Erhält die Behörde von Tatsachen Kenntnis, welche die Rücknahme eines rechtswidrigen Verwaltungsaktes "
        "rechtfertigen, so ist die Rücknahme nur innerhalb eines Jahres seit dem Zeitpunkt der Kenntnisnahme zulässig.“")
w484, w484_y = wortlaut(80, 150, 1100, W484, "§ 48 Abs. 4 Satz 1 VwVfG", "wl484", marken=[
    ("Kenntnis,", beim("wl484", "Kenntnis")), ("innerhalb eines Jahres", beim("wl484", "innerhalb")),
    ("Kenntnisnahme", beim("wl484", "Kenntnisnahme"))], size=33)
folie([("wl484", f"{GF} › C. materiell › 4. Jahresfrist, § 48 IV")], rechts_frei([
    titel(glyphen("4. Jahresfrist"), 110, 75, "wl484", 50),
    *w484,
    nein(150, w484_y + 58, beim("frist1", "zwei"), gr=18),
    z("zwei Jahre seit dem Bescheid: keine Rolle", 195, w484_y + 35, beim("frist1", "zwei"), "Bold", 34),
    z("Beginn: Rechtswidrigkeit erkannt und alle", 110, w484_y + 110, beim("frist2", "beginnt"), size=34),
    z("erheblichen Tatsachen vollständig bekannt", 150, w484_y + 162, beim("frist2", "vollständig"), size=34),
    zit("BVerwG, Urt. v. 23.1.2019 – 10 C 5.17, Rn. 30 f. (stRspr seit BVerwGE 70, 356)", 150, w484_y + 215,
        beim("frist2", "kennt")),
    z("regelmäßig erst nach Anhörung und Stellungnahme", 110, w484_y + 270, "frist3", size=34),
    zit("BVerwG, 10 C 5.17, Rn. 31 f. (Entscheidungsfrist)", 150, w484_y + 323, beim("frist3", "Stellungnahme")),
    ok(150, w484_y + 403, beim("frist4", "gewahrt"), gr=20),
    z("hier gewahrt", 195, w484_y + 380, beim("frist4", "gewahrt"), "Bold", 34),
    ficon("tabler", "calendar", IX, IU, 140, "wl484", fuell=WEISS),
    pl("1 Jahr ab Kenntnis", IX, 180, beim("wl484", "Jahres"), fill=GELB, size=30, anker="m"),
    *fig("WA", FX, FB, FR, [("wl484", "ruhig"), ("frist2", "denkt")]),
    schild("Herr Wagner", FX, "wl484", WA_F),
]))

# O Ermessen -------------------------------------------------------------------------------------------------------------------------
folie([("erm", f"{GF} › C. materiell › 5. Ermessen, § 48 I 1")], rechts_frei([
    *tafel("erm", "5. Ermessen"),
    z("Behörde kann zurücknehmen, muss aber nicht", 110, 190, beim("erm", "Behörde"), "Bold", 36),
    zit("§ 48 Abs. 1 Satz 1 VwVfG („kann“)", 150, 245, beim("erm", "muss")),
    nein(150, 343, beim("erm2", "intendiertes"), gr=18),
    z("kein intendiertes Ermessen,", 195, 320, beim("erm2", "intendiertes"), "Bold", 34),
    z("auch nicht bei Fördergeld", 195, 375, beim("erm2", "Fördergeld"), size=34),
    zit("BVerwG, Urt. v. 16.6.2015 – 10 C 15.14, Rn. 29", 195, 430, beim("erm2", "Fördergeld")),
    nein(150, 523, beim("erm3", "formelhafter"), gr=18),
    z("formelhafter Hinweis auf Sparsamkeit reicht nicht", 195, 500, beim("erm3", "formelhafter"), size=34),
    z("abwägen: In wessen Sphäre lag der Fehler?", 110, 600, beim("erm3", "abwägen"), "Bold", 34),
    zit("BVerwG, 10 C 15.14, Rn. 19", 150, 655, beim("erm3", "Sphäre")),
    ficon("ph", "scales", IX, IU, 170, "erm", fuell=WEISS),
    *fig("WA", FX, FB, FR, [("erm", "ruhig"), ("erm3", "denkt")]),
    schild("Herr Wagner", FX, "erm", WA_F),
]))

# P Wortlaut § 49a Abs. 1: Erstattung und Zinsen -------------------------------------------------------------------------------------
W49a = ("„Soweit ein Verwaltungsakt mit Wirkung für die Vergangenheit zurückgenommen oder widerrufen worden oder infolge "
        "Eintritts einer auflösenden Bedingung unwirksam geworden ist, sind bereits erbrachte Leistungen zu erstatten. Die zu "
        "erstattende Leistung ist durch schriftlichen Verwaltungsakt festzusetzen.“")
w49a, w49a_y = wortlaut(80, 150, 1100, W49a, "§ 49a Abs. 1 VwVfG", "wl49a", marken=[
    ("für die Vergangenheit", beim("wl49a", "Vergangenheit")), ("zu erstatten.", beim("wl49a", "erstatten")),
    ("schriftlichen Verwaltungsakt", beim("fest", "schriftlichen"))], size=33)
folie([("wl49a", f"{GF} › Erstattung, § 49a I"), ("zins", f"{GF} › Zinsen, § 49a III")], rechts_frei([
    titel(glyphen("Erstattung, § 49a VwVfG"), 110, 75, "wl49a", 50),
    *w49a,
    z("Zinsen, § 49a Abs. 3 Satz 1:", 110, w49a_y + 45, "zins", "Bold", 34),
    z("fünf Prozentpunkte über dem Basiszinssatz", 150, w49a_y + 100, beim("zins", "fünf"), size=34),
    ficon("tabler", "file-euro", IX, IU, 140, "wl49a", fuell=ROT, bis="zins"),
    ficon("tabler", "percentage", IX, IU, 120, "zins", fuell=WEISS),
    *fig("HO", FX, FB, FR, [("wl49a", "sorge")]),
    schild("Frau Hofmann", FX, "wl49a", HO_F),
]))

# Q Ausblick: EU-Beihilfen -------------------------------------------------------------------------------------------------------
folie([("eu", "Ausblick · EU-Beihilfen")], rechts_frei([
    *tafel("eu", "Ausblick: EU-Beihilfen"),
    z("Kommission verlangt bestandskräftig die Rückforderung:", 110, 190, beim("eu", "Rückforderung"), "Bold", 34),
    z("Unionsrecht überlagert den Vertrauensschutz", 150, 250, beim("eu", "überlagert"), size=34),
    z("Rücknahme sogar nach Ablauf der Jahresfrist", 110, 350, beim("eu2", "sogar"), "Bold", 34),
    zit("EuGH, Urt. v. 20.3.1997 – C-24/95 (Alcan), Tenor 1; wiedergegeben in", 150, 410, beim("eu2", "Jahresfrist")),
    zit("BVerfG, Beschl. v. 17.2.2000 – 2 BvR 1210/98, Rn. 8", 150, 445, beim("eu2", "Jahresfrist")),
    ficon("tabler", "stars", IX, IU, 150, "eu", fuell=GELB),
    *fig("EB", FX, FB, FR, [("eu", "ruhig"), ("eu2", "denkt")]),
    schild("Frau Ebert", FX, "eu", EB_F),
]))

# R Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Rücknahme prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Rücknahme: meist in der Begründetheit", 200, 200, beim("tipp", "Rücknahme"), "Bold", 36),
    z("der Anfechtungsklage gegen den Rücknahmebescheid", 200, 255, beim("tipp", "Anfechtungsklage"), size=34),
    zit("§ 42 I, § 113 I 1 VwGO", 200, 310, beim("tipp", "Rücknahmebescheid")),
    z("Vertrauensschutz bei Absatz 2 prüfen,", 200, 390, "tipp1", "Bold", 34),
    z("nicht erst im Ermessen", 200, 445, beim("tipp1", "nicht"), size=34),
    z("Jahresfrist ab vollständiger Kenntnis,", 200, 540, "tipp2", "Bold", 34),
    z("nicht ab Erlass des Bescheids", 200, 595, beim("tipp2", "nicht"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ----------------------------------------------------------------------------------------------------------------------
SZ = 36
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Rücknahme"), 110, 90, "sch", 48),
    z("Rücknahme nach § 48 VwVfG", K1, 180, "q0", "Bold", 40, rechts=1820),
    z("A. Rechtsgrundlage: § 48, Abgrenzung zum Widerruf, § 49", K1, 255, "q1", size=SZ, rechts=1820),
    z("B. formell: Zuständigkeit, Anhörung § 28 I", K1, 320, "q2", size=SZ, rechts=1820),
    z("C. materiell:", K1, 385, "q3", size=SZ, rechts=1820),
    z("1. rechtswidriger Verwaltungsakt, § 48 I 1", K2, 445, beim("q3", "Eins"), size=SZ, rechts=1820),
    z("2. begünstigend, § 48 I 2", K2, 505, "q4", size=SZ, rechts=1820),
    z("3. bei Geldleistungen: Vertrauensschutz, § 48 II", K2, 565, "q5", size=SZ, rechts=1820),
    z("4. Jahresfrist, § 48 IV", K2, 625, "q6", size=SZ, rechts=1820),
    z("5. Ermessen, § 48 I 1", K2, 685, "q7", size=SZ, rechts=1820),
    z("Danach: Erstattung und Zinsen, § 49a I, III VwVfG", K1, 775, "q8", "Bold", 38, rechts=1820),
])

# T Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer auf einen rechtswidrigen", 0)], [("Förderbescheid vertraut und", 0)],
                 [("das Geld ", 0), ("verbraucht", "a"), (" hat,", 0)], [("ist in der Regel ", 0), ("geschützt.", "b")]],
                750, 300, 46, "merke", {"a": beim("merke", "verbraucht"), "b": beim("merke", "geschützt")}),
    *markertext([[("Wer wesentlich falsche Angaben", 0)], [("macht, ", 0), ("verliert diesen Schutz.", "c")]],
                750, 640, 46, "m2", {"c": beim("m2", "verliert")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
