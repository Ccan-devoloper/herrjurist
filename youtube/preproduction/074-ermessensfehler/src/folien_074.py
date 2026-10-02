"""Folge 074 · Ermessensfehler: Was darf das Gericht kontrollieren? (§ 114 VwGO) – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Café in der Altstadt, Tische auf dem Gehweg, Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut
../SZENENPLAN.md: A Altstadt (Antrag, Antwort der Stadt), B Verwaltungsgericht (Klage, Frage), C Sachverhalt, D Sondernutzung,
E gebunden oder Ermessen, F Rechtsfolgenseite, G Wortlaut § 40 VwVfG, H Wortlaut § 114 Satz 1 VwGO, I–K die drei
Ermessensfehler, L Reduzierung auf null, M Fall: Ermessensausfall, N Nachschieben (Wortlaut § 114 Satz 2), O Urteil
(Bescheidungsurteil), P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als Herr Hornung den Bescheid bringt). Eigene Hilfsfunktionen wie Folge 069."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_074/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_074/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 069/064/061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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
KA_F, HO_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
E1 = "1. Räumt die Norm Ermessen ein?"
E2 = "2. Ermessensfehler"


def tische(x0, cue, anim="pop", bis=None, breite=86, abstand=96):
    """Die 4 Tische vor dem Café: Phosphor „picnic-table“ (weiß gefüllt), nebeneinander auf dem Gehweg."""
    return [ficon("ph", "picnic-table", x0 + i * abstand, BODEN, breite, cue, fuell=WEISS, anim=anim, bis=bis) for i in range(4)]


# A Fall: das Café in der Altstadt, die Antwort der Stadt -------------------------------------------------------------------
CAX, KAX, HOX = 300, 1110, 1660
KAb = ("KA_redet_r", KAX, BODEN, FH)
HOb = ("HO_redet", HOX, BODEN, FH)
KOMMT = beim("hornung", "Herr")
folie([(NULL, "Fall · Das Café in der Altstadt"), ("hornung", "Fall · Die Antwort der Stadt")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Altstadt, Sommer", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "building-store", CAX, BODEN - 2, 400, NULL, fuell=GELB, anim="cut"),
    hart(pl("Café", CAX, 420, NULL, fill=WEISS, size=34, anker="m")),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *fig("KA", KAX, BODEN, FH, [(NULL, "ruhig_r"), ("antrag", "hofft_r"), (KOMMT, "ruhig_r"),
                               (beim("ho1", "nie"), "sorge_r")], bis="ka1", erst="cut"),
    *redet("KA_redet_r", KAX, BODEN, FH, "ka1", "klage"),
    hart(schild("Frau Kampmann, Café", KAX, NULL, KA_F, unten=BODEN, d=0.0)),
    ficon("tabler", "file-text", 820, 560, 80, "antrag", fuell=WEISS, bis="hornung"),
    pl("Antrag an die Stadt", 820, 600, beim("antrag", "Stadt"), fill=WEISS, size=30, anker="m", bis="hornung"),
    *tische(570, beim("antrag", "Tische")),
    pl("4 Tische auf dem Gehweg", 715, 700, beim("antrag", "Gehweg"), fill=GELB, size=30, anker="m"),
    *fig("HO", HOX, BODEN, FH, [(KOMMT, "ruhig")], bis="ho1"),
    *redet("HO_redet", HOX, BODEN, FH, "ho1", "ka1"),
    peep_voll("HO_ruhig", HOX, BODEN, FH, "ka1", anim="cut"),
    schild("Herr Hornung, Stadt", HOX, KOMMT, HO_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", HOX - 140, 700, 90, beim("hornung", "Antwort"), fuell=WEISS), "074brief*", 0.8, -0.25),
    nein(715, 640, beim("ho1", "abgelehnt"), gr=40),
    blase("sprech", 820, 230, "ho1", 1180, 215, inhalt=["Frau Kampmann, Tische auf dem Gehweg?",
                                                      "Das machen wir grundsätzlich nie.",
                                                      "Ihr Antrag ist abgelehnt."], textsize=30, figur=HOb, bis="ka1"),
    blase("sprech", 760, 200, "ka1", 900, 215, inhalt=["Nie? Sie haben sich meinen Gehweg", "doch gar nicht angesehen!"],
          textsize=30, figur=KAb, bis="klage"),
])

# B Die Klage und die Frage --------------------------------------------------------------------------------------------------
GERICHT = beim("klage", "Verwaltungsgericht")
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Was darf das Gericht kontrollieren?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 520, BODEN - 2, 420, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 960, 640, 100, beim("klage", "klagt"), fuell=WEISS),
    pl("Klage", 960, 660, beim("klage", "klagt"), fill=GRUEN, size=30, anker="m"),
    *fig("KA", 1160, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Frau Kampmann", 1160, "klage", KA_F, unten=BODEN),
    pl("Was darf das Gericht hier kontrollieren?", 1290, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Und hat die Klage Erfolg?", 1290, 240, "frage2", fill=WEISS, size=36, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Kampmann betreibt ein kleines Café in der Altstadt einer Stadt in Nordrhein-Westfalen. Sie beantragt bei der "
    "Stadt eine Sondernutzungserlaubnis: Von Mai bis September will sie 4 Tische auf den breiten Gehweg vor dem Café "
    "stellen. Herr Hornung von der Stadt übergibt den schriftlichen Bescheid. Die Stadt lehnt ab, einzige Begründung: "
    "„Das machen wir grundsätzlich nie.“ Frau Kampmann erhebt rechtzeitig Klage beim Verwaltungsgericht und verlangt die "
    "Erlaubnis. Im Prozess trägt die Stadt erstmals vor, Fußgänger bräuchten dort Platz.",
], "Hat die Klage Erfolg?")

# D Sondernutzung, § 18 StrWG NRW ------------------------------------------------------------------------------------------
folie([("norm", "Grundlage · Sondernutzung, § 18 StrWG NRW")], rechts_frei([
    *tafel("norm", "Sondernutzung, § 18 StrWG NRW"),
    z("Tische auf dem Gehweg: Nutzung über den", 110, 190, beim("norm", "Tische"), size=34),
    z("Gemeingebrauch hinaus", 110, 243, beim("norm", "Gemeingebrauch"), size=34),
    blk(110, 310, 1040, 76, BLAU, beim("norm", "Sondernutzung"), [("= Sondernutzung", "ExtraBold", 36, INK)]),
    z("braucht eine Erlaubnis", 110, 430, beim("norm2", "Erlaubnis"), "Bold", 36),
    zit("§ 18 Abs. 1 Satz 1 und 2 StrWG NRW", 150, 485, beim("norm2", "Paragraf")),
    z("Entscheidung der Stadt: nach Ermessen", 110, 560, beim("norm3", "Ermessen"), "Bold", 36),
    zit("OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 29, 58", 150, 615, beim("norm3", "Ermessen")),
    pl("In deinem Land: andere Nummer", 110, 690, "land", fill=PINK, size=32),
    ficon("tabler", "building-store", IX, IU, 150, "norm", fuell=GELB),
    pl("Café", IX, 180, "norm", fill=WEISS, size=28, anker="m"),
    *fig("KA", FX, FB, FR, [("norm", "denkt"), ("norm3", "ruhig")]),
    schild("Frau Kampmann", FX, "norm", KA_F),
]))

# E Gebunden oder Ermessen ---------------------------------------------------------------------------------------------------
folie([("geb", f"{E1} › gebunden oder Ermessen")], rechts_frei([
    *tafel("geb", "Gebunden oder Ermessen?"),
    z("„muss“ oder „ist zu“: gebunden", 110, 190, beim("muss", "muss"), "Bold", 36),
    z("Tatbestand erfüllt: Rechtsfolge zwingend", 150, 245, beim("muss", "Tatbestand"), size=34),
    z("„kann“: Ermessen", 110, 335, beim("kann", "kann"), "Bold", 36),
    z("„soll“: im Regelfall gebunden,", 110, 425, beim("soll", "Soll"), "Bold", 36),
    z("Ermessen nur im atypischen Fall", 150, 480, beim("soll", "atypischen"), size=34),
    zit("BVerwG, Beschl. v. 3.12.2009 – 9 B 79.09, Rn. 2", 150, 532, beim("soll", "Fall")),
    ficon("tabler", "scale", IX, IU, 140, "geb", fuell=WEISS),
    *fig("HO", FX, FB, FR, [("geb", "ruhig"), ("soll", "denkt")]),
    schild("Herr Hornung, Stadt", FX, "geb", HO_F),
]))

# F Rechtsfolgenseite, Entschließungs- und Auswahlermessen, Beurteilungsspielraum -------------------------------------------
folie([("rfs", f"{E1} › Rechtsfolgenseite")], rechts_frei([
    *tafel("rfs", "Ermessen: Rechtsfolgenseite"),
    blk(110, 190, 1040, 76, GELB, beim("ent", "Entschließungsermessen"), [("Entschließungsermessen: ob", "ExtraBold", 36, INK)]),
    blk(110, 290, 1040, 76, GRUEN, beim("aus", "Auswahlermessen"), [("Auswahlermessen: wie", "ExtraBold", 36, INK)]),
    z("Tatbestand: unbestimmte Rechtsbegriffe", 110, 420, beim("bsr", "Unbestimmte"), "Bold", 34),
    z("prüft das Gericht grundsätzlich voll", 150, 473, beim("bsr", "voll"), size=34),
    z("Beurteilungsspielraum: seltene Ausnahme", 150, 535, beim("bsr", "Beurteilungsspielraum"), size=34),
    zit("BVerwG, Beschl. v. 8.11.2016 – 3 B 11.16, Rn. 8", 150, 588, beim("bsr", "Ausnahme")),
    *tische(IX - 144, "rfs", breite=70),
    pl("ob?", IX - 60, 690, beim("ent", "ob"), fill=GELB, size=30, anker="m"),
    pl("wie?", IX + 60, 690, beim("aus", "wie"), fill=GRUEN, size=30, anker="m"),
    *fig("KA", FX, FB, FR, [("rfs", "denkt")]),
    schild("Frau Kampmann", FX, "rfs", KA_F),
]))
