"""Folge 093 · Verpflichtungsklage Schema: Spruchreife und Bescheidungsurteil – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Café an einer Gemeindestraße, 6 Tische auf dem Gehweg, Beispielland Nordrhein-Westfalen), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Straße mit Café (Antrag, Bescheid), B Verwaltungsgericht (Klage, Frage), C Sachverhalt,
D Aufbau/Rechtsweg, E Statthaftigkeit (Wortlaut § 42 I Alt. 2), F Klagebefugnis, G Vorverfahren/Frist, H Klagegegner,
I Begründetheit (Wortlaut § 113 V), J Anspruch/Zeitpunkt, K Anspruchsprüfung, L Ermessensfehler (falscher Sachverhalt),
M Spruchreife, N Im Fall, O Tenorformeln, P Urteil, Q Klausurtipp (Lexi), R Klausurschema, S Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als Frau Siebert den Bescheid bringt). Hilfsfunktionen wie Folge 074."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_093/"
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


def zz(kopf, rest, x, y, c_kopf, c_rest, stil="Bold", size=34, rest_stil=None, **k):
    """Zeile in zwei Teilen: Gliederungspunkt zur Marke, Inhalt erst zum gesprochenen Wort (nie vor dem Wort)."""
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
        if n.startswith(("bild:", "ficon:")) or "/op_093/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 074/069): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
FE_F, SI_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
ZA = "A. Zulässigkeit"
BE = "B. Begründetheit"


def tische(x0, cue, anim="pop", bis=None, breite=70, abstand=76, unten=BODEN, geplant=False, n=6):
    """Die 6 Tische vor dem Café: Phosphor „picnic-table“ (weiß gefüllt), nebeneinander auf dem Gehweg.
    geplant=True: halbtransparent – die Tische sind nur beantragt, noch nicht aufgestellt."""
    els = [ficon("ph", "picnic-table", x0 + i * abstand, unten, breite, cue, fuell=WEISS, anim=anim, bis=bis) for i in range(n)]
    if geplant:
        for e in els:
            sp = e.sprite.copy()
            sp.putalpha(sp.getchannel("A").point(lambda v: int(v * 0.4)))
            e.sprite = sp
    return els


# A Fall: das Café an der Straße, der Bescheid der Stadt -------------------------------------------------------------------
CAX, FEX, SIX = 290, 1130, 1680
FEb = ("FE_redet_r", FEX, BODEN, FH)
SIb = ("SI_redet", SIX, BODEN, FH)
KOMMT = beim("siebert", "Frau")
folie([(NULL, "Fall · Das Café an der Straße"), ("siebert", "Fall · Der Bescheid der Stadt")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("An der Hauptstraße, Sommer", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "building-store", CAX, BODEN - 2, 380, NULL, fuell=GRUEN, anim="cut"),
    hart(pl("Café", CAX, 440, NULL, fill=WEISS, size=34, anker="m")),
    ficon("tabler", "coffee", CAX, 400, 70, NULL, fuell=WEISS, anim="cut"),
    *fig("FE", FEX, BODEN, FH, [(NULL, "ruhig_r"), ("antrag", "hofft_r"), (KOMMT, "ruhig_r"),
                                (beim("si1", "schmal"), "sorge_r")], bis="fe1", erst="cut"),
    *redet("FE_redet_r", FEX, BODEN, FH, "fe1", "klage"),
    hart(schild("Herr Feldmann, Café", FEX, NULL, FE_F, unten=BODEN, d=0.0)),
    ficon("tabler", "file-text", 720, 600, 80, "antrag", fuell=WEISS, bis="siebert"),
    pl("Antrag an die Stadt", 720, 640, beim("antrag", "Stadt"), fill=WEISS, size=30, anker="m", bis="siebert"),
    *tische(530, beim("antrag", "Tische"), geplant=True),
    pl("6 Tische auf dem Gehweg", 720, 720, beim("antrag", "Gehweg"), fill=GELB, size=30, anker="m", bis="fe1"),
    *fig("SI", SIX, BODEN, FH, [(KOMMT, "ruhig")], bis="si1"),
    *redet("SI_redet", SIX, BODEN, FH, "si1", "fe1"),
    *fig("SI", SIX, BODEN, FH, [("fe1", "ruhig"), (beim("fe1", "drei"), "denkt")], erst="cut"),
    schild("Frau Siebert, Stadt", SIX, KOMMT, SI_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", SIX - 150, 690, 90, beim("siebert", "Bescheid"), fuell=WEISS), "093brief*", 0.8, -0.24),
    nein(720, 845, beim("si1", "ab"), gr=40),
    blase("sprech", 1060, 270, "si1", 1000, 245, inhalt=["Herr Feldmann, Ihr Gehweg ist zu schmal.",
                                                       "Mit den Tischen müssten Fußgänger",
                                                       "auf die Fahrbahn ausweichen.",
                                                       "Das ist zu gefährlich, wir lehnen ab."], textsize=30, figur=SIb, bis="fe1"),
    blase("sprech", 820, 210, "fe1", 760, 215, inhalt=["Zu schmal? Der Gehweg ist 5 Meter breit.",
                                                      "Da bleiben 3 Meter frei!"], textsize=30, figur=FEb, bis="klage"),
    ficon("tabler", "ruler-measure", 600, 560, 90, beim("fe1", "fünf"), fuell=GELB),
    pl("Gehweg: 5 m breit", 830, 520, beim("fe1", "fünf"), fill=WEISS, size=30, anker="m"),
    pl("3 m bleiben frei", 830, 600, beim("fe1", "drei"), fill=GRUEN, size=30, anker="m"),
])

# B Die Klage und die Frage --------------------------------------------------------------------------------------------------
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Erlaubnis oder neue Entscheidung?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "klage", fill=GELB, size=40),
    pl("3 Wochen später", 70, 120, beim("klage", "Drei"), fill=WEISS, size=30),
    ficon(HC, "classical-building", 520, BODEN - 2, 420, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 960, 640, 100, beim("klage", "klagt"), fuell=WEISS),
    pl("Klage auf die Erlaubnis", 960, 660, beim("klage", "verlangt"), fill=GRUEN, size=30, anker="m"),
    *fig("FE", 1220, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt"), ("frage2", "hofft")]),
    schild("Herr Feldmann", 1220, "klage", FE_F, unten=BODEN),
    pl("Hat die Klage Erfolg?", 1340, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Erlaubnis oder nur neue Entscheidung?", 1300, 240, "frage2", fill=WEISS, size=36, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Feldmann führt ein Café an einer Gemeindestraße in einer Stadt in Nordrhein-Westfalen. Er beantragt bei der "
    "Stadt eine Sondernutzungserlaubnis: Von Mai bis September will er 6 Tische auf den Gehweg vor dem Café stellen. "
    "Frau Siebert von der Stadt übergibt den Bescheid mit Rechtsbehelfsbelehrung: Die Stadt lehnt ab, der Gehweg sei zu "
    "schmal, Fußgänger müssten auf die Fahrbahn ausweichen. Tatsächlich ist der Gehweg 5 m breit; mit den Tischen bleiben "
    "3 m frei. 3 Wochen nach der Übergabe klagt Herr Feldmann beim Verwaltungsgericht und verlangt die Erlaubnis.",
], "Hat die Klage Erfolg – Erlaubnis oder neue Entscheidung?")

# D Aufbau und Rechtsweg -------------------------------------------------------------------------------------------------------
folie([("aufbau", "Aufbau · A. Zulässigkeit, B. Begründetheit"), ("rweg", f"{ZA} › I. Verwaltungsrechtsweg, § 40 VwGO")],
      rechts_frei([
    *tafel("aufbau", "Verpflichtungsklage: Aufbau"),
    blk(110, 180, 1040, 70, GELB, "aufbau2", [("A. Zulässigkeit", "ExtraBold", 36, INK)]),
    blk(110, 270, 1040, 70, GRUEN, beim("aufbau2", "Begründetheit"), [("B. Begründetheit", "ExtraBold", 36, INK)]),
    pl("Beispiel: Nordrhein-Westfalen", 110, 375, beim("verweis1", "Nordrhein"), fill=PINK, size=32),
    *zz("I. Verwaltungsrechtsweg,", "§ 40 Abs. 1 Satz 1 VwGO", 110, 480, "rweg", beim("rweg", "Paragraf")),
    z("Sondernutzung: Straßen- und Wegegesetz", 150, 540, beim("rweg", "Sondernutzung"), size=34),
    z("= öffentliches Recht", 150, 595, beim("rweg", "öffentliches"), size=34),
    ok(510, 615, beim("rweg", "Recht"), gr=22),
    ficon("tabler", "building-store", IX, IU, 150, "aufbau", fuell=GRUEN),
    pl("Café", IX, 190, "aufbau", fill=WEISS, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("aufbau", "denkt"), ("rweg", "ruhig")]),
    schild("Herr Feldmann", FX, "aufbau", FE_F),
]))

# E Statthaftigkeit, Wortlaut § 42 Abs. 1 Alt. 2 VwGO ---------------------------------------------------------------------------
W42 = "„Durch Klage kann … die Verurteilung zum Erlaß eines abgelehnten oder unterlassenen Verwaltungsakts (Verpflichtungsklage) begehrt werden.“"
Z42 = ["„Durch Klage kann … die Verurteilung zum Erlaß eines",
       "abgelehnten oder unterlassenen Verwaltungsakts",
       "(Verpflichtungsklage) begehrt werden.“"]
w42, w42_y = wortlaut(80, 160, 1100, W42, "§ 42 Abs. 1 Alt. 2 VwGO (Auszug)", "wl42", size=34, zeilen=Z42,
                      marken=[("abgelehnten", beim("wl42", "abgelehnten")),
                              ("(Verpflichtungsklage)", beim("wl42", "Verpflichtungsklage"))])
folie([("wl42", f"{ZA} › II. Statthaftigkeit, § 42 I Alt. 2 VwGO")], rechts_frei([
    titel(glyphen("Statthafte Klageart"), 110, 70, "wl42", 44),
    *w42,
    z("Erlaubnis = Verwaltungsakt, abgelehnt", 110, w42_y + 30, beim("va", "Erlaubnis"), "Bold", 34),
    blk(110, w42_y + 95, 1040, 70, BLAU, beim("vgk", "Versagungsgegenklage"), [("Versagungsgegenklage", "ExtraBold", 36, INK)]),
    z("umfasst die Aufhebung des Ablehnungsbescheids", 150, w42_y + 180, beim("vgk", "umfasst"), size=34),
    zit("BVerwG, Urt. v. 21.11.2006 – 1 C 10.06, Rn. 16", 150, w42_y + 232, beim("vgk", "Ablehnungsbescheids")),
    z("nicht in angemessener Frist entschieden:", 110, w42_y + 300, beim("untaet", "angemessener"), size=34),
    z("Untätigkeitsklage, § 75 VwGO", 150, w42_y + 355, beim("untaet", "Untätigkeitsklage"), "Bold", 34),
    ficon("tabler", "file-text", IX, IU, 110, "wl42", fuell=WEISS),
    pl("Bescheid", IX, 200, "wl42", fill=WEISS, size=28, anker="m"),
    bis_(nein(IX + 70, IU - 40, beim("va", "abgelehnt"), gr=30), "untaet"),
    ficon("tabler", "hourglass", IX + 130, IU - 10, 70, beim("untaet", "angemessener"), fuell=GELB),
    *fig("SI", FX, FB, FR, [("wl42", "ruhig"), ("untaet", "denkt")]),
    schild("Frau Siebert, Stadt", FX, "wl42", SI_F),
]))

# F Klagebefugnis, § 42 Abs. 2 VwGO ---------------------------------------------------------------------------------------------
folie([("kb", f"{ZA} › III. Klagebefugnis, § 42 II VwGO")], rechts_frei([
    *tafel("kb", "Klagebefugnis, § 42 Abs. 2 VwGO"),
    z("möglich: Anspruch auf den Verwaltungsakt", 110, 190, beim("kb", "möglich"), "Bold", 36),
    zit("vgl. BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9", 150, 245, beim("kb", "Verwaltungsakt")),
    z("bei Ermessen: möglicher Anspruch", 110, 330, beim("kb2", "Ermessen"), "Bold", 36),
    z("auf eine fehlerfreie Entscheidung", 150, 385, beim("kb2", "fehlerfreie"), size=34),
    zit("vgl. OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 62", 150, 437, beim("kb2", "Entscheidung")),
    z("hier: aus dem Straßen- und Wegegesetz", 110, 520, beim("kb3", "Straßen"), size=34),
    blk(110, 590, 1040, 70, GRUEN, beim("kb3", "klagebefugt"), [("Herr Feldmann ist klagebefugt.", "ExtraBold", 36, INK)]),
    ok(1100, 625, beim("kb3", "klagebefugt"), gr=22),
    ficon("tabler", "file-text", IX, IU, 110, "kb", fuell=WEISS),
    pl("Anspruch?", IX, 200, beim("kb", "Anspruch"), fill=GELB, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("kb", "denkt"), ("kb3", "hofft")]),
    schild("Herr Feldmann", FX, "kb", FE_F),
]))

# G Vorverfahren und Klagefrist ---------------------------------------------------------------------------------------------------
folie([("vv", f"{ZA} › IV. Vorverfahren, § 68 II VwGO"), ("frist", f"{ZA} › V. Klagefrist, § 74 II VwGO")], rechts_frei([
    *tafel("vv", "Vorverfahren und Klagefrist"),
    *zz("IV. Vorverfahren,", "§ 68 Abs. 2 VwGO:", 110, 190, "vv", beim("vv", "Paragraf"), size=36),
    z("grundsätzlich Widerspruch", 150, 245, beim("vv", "Widerspruch"), size=34),
    z("NRW: entfällt, § 110 Abs. 1 Satz 2 JustG NRW,", 150, 300, beim("nrw", "entfällt"), size=34),
    z("auch hier", 150, 353, beim("nrw", "auch"), size=34),
    pl("In deinem Land: ggf. anders", 150, 410, "land", fill=PINK, size=30),
    *zz("V. Klagefrist,", "§ 74 Abs. 2 VwGO:", 110, 510, "frist", beim("frist", "Paragraf"), size=36),
    z("1 Monat ab Bekanntgabe der Ablehnung", 150, 565, beim("frist", "Monat"), size=34),
    z("Klage nach 3 Wochen: rechtzeitig", 150, 620, beim("frist2", "drei"), size=34),
    ok(720, 640, beim("frist2", "rechtzeitig"), gr=22),
    ficon("tabler", "mail", IX, IU, 120, "vv", fuell=WEISS, bis="frist"),
    pl("Widerspruch?", IX, 210, beim("vv", "Widerspruch"), fill=WEISS, size=28, anker="m", bis="frist"),
    bis_(nein(IX + 80, IU - 40, beim("nrw", "entfällt"), gr=30), "frist"),
    ficon("tabler", "calendar", IX, IU, 120, "frist", fuell=WEISS),
    pl("1 Monat", IX, 210, beim("frist", "Monat"), fill=GELB, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("vv", "ruhig"), ("frist2", "froh")]),
    schild("Herr Feldmann", FX, "vv", FE_F),
]))

# H Klagegegner, Ergebnis Zulässigkeit ----------------------------------------------------------------------------------------------
folie([("kg", f"{ZA} › VI. Klagegegner, § 78 VwGO"), ("zul", f"{ZA} › Ergebnis: zulässig")], rechts_frei([
    *tafel("kg", "Klagegegner, § 78 Abs. 1 Nr. 1 VwGO"),
    z("die Körperschaft, deren Behörde", 110, 190, beim("kg", "Körperschaft"), "Bold", 36),
    z("den Antrag abgelehnt hat", 110, 245, beim("kg", "Antrag"), "Bold", 36),
    blk(110, 320, 1040, 70, BLAU, beim("kg", "Stadt"), [("hier: die Stadt", "ExtraBold", 36, INK)]),
    blk(110, 470, 1040, 76, GRUEN, "zul", [("Die Klage ist zulässig.", "ExtraBold", 38, INK)]),
    ok(1090, 508, beim("zul", "zulässig"), gr=24),
    ficon("tabler", "building", IX, IU, 130, "kg", fuell=WEISS),
    pl("Stadt", IX, 200, beim("kg", "Stadt"), fill=BLAU, size=28, anker="m"),
    *fig("SI", FX, FB, FR, [("kg", "ruhig"), ("zul", "denkt")]),
    schild("Frau Siebert, Stadt", FX, "kg", SI_F),
]))

# I Begründetheit, Wortlaut § 113 Abs. 5 VwGO ------------------------------------------------------------------------------------
W113 = ("„Soweit die Ablehnung oder Unterlassung des Verwaltungsakts rechtswidrig und der Kläger dadurch in seinen Rechten "
        "verletzt ist, spricht das Gericht die Verpflichtung der Verwaltungsbehörde aus, die beantragte Amtshandlung "
        "vorzunehmen, wenn die Sache spruchreif ist. Andernfalls spricht es die Verpflichtung aus, den Kläger unter "
        "Beachtung der Rechtsauffassung des Gerichts zu bescheiden.“")
Z113 = ["„Soweit die Ablehnung oder Unterlassung des Verwaltungsakts",
        "rechtswidrig und der Kläger dadurch in seinen Rechten",
        "verletzt ist, spricht das Gericht die Verpflichtung der",
        "Verwaltungsbehörde aus, die beantragte Amtshandlung",
        "vorzunehmen, wenn die Sache spruchreif ist. Andernfalls",
        "spricht es die Verpflichtung aus, den Kläger unter",
        "Beachtung der Rechtsauffassung des Gerichts zu bescheiden.“"]
w113, w113_y = wortlaut(80, 160, 1100, W113, "§ 113 Abs. 5 VwGO", "wl113", size=33, zeilen=Z113,
                        marken=[("rechtswidrig", beim("wl113", "rechtswidrig")),
                                ("in seinen Rechten", beim("wl113", "Rechten")),
                                ("wenn die Sache spruchreif ist.", beim("wl113", "spruchreif")),
                                ("zu bescheiden.“", beim("satz2", "bescheiden"))])
folie([("wl113", f"{BE} › § 113 V VwGO")], rechts_frei([
    titel(glyphen("B. Begründetheit"), 110, 70, "wl113", 44),
    *w113,
    pl("Satz 1: Verpflichtung zur Amtshandlung", 110, w113_y + 30, beim("wl113", "spruchreif"), fill=GRUEN, size=30),
    pl("Satz 2: Verpflichtung zur Bescheidung", 110, w113_y + 105, beim("satz2", "bescheiden"), fill=GELB, size=30),
    ficon(HC, "balance-scale", IX, IU, 150, "wl113", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("wl113", "ruhig")]),
    schild("die Richterin", FX, "wl113", RI_F),
]))

# J Anspruch, maßgeblicher Zeitpunkt ---------------------------------------------------------------------------------------------
folie([("anspr", f"{BE} › Anspruch auf die Erlaubnis?"), ("zeit", f"{BE} › maßgeblicher Zeitpunkt")], rechts_frei([
    *tafel("anspr", "Vom Anspruch her prüfen"),
    blk(110, 180, 1040, 70, GELB, beim("anspr", "Anspruch", 2), [("Anspruch auf die Erlaubnis?", "ExtraBold", 36, INK)]),
    z("maßgeblich in der Regel: Sach- und Rechtslage", 110, 320, beim("zeit", "Maßgeblich"), "Bold", 34),
    z("der letzten mündlichen Verhandlung", 150, 375, beim("zeit", "letzten"), size=34),
    zit("BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 18", 150, 427, beim("zeit", "Verhandlung")),
    z("materielles Recht kann Abweichendes bestimmen", 110, 505, beim("zeit2", "materielle"), size=34),
    ficon("tabler", "file-text", IX, IU, 110, "anspr", fuell=WEISS, bis="zeit"),
    pl("Erlaubnis?", IX, 200, beim("anspr", "Erlaubnis"), fill=GELB, size=28, anker="m", bis="zeit"),
    ficon("tabler", "clock", IX, IU, 120, "zeit", fuell=WEISS),
    pl("letzte Verhandlung", IX, 210, beim("zeit", "letzten"), fill=WEISS, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("anspr", "hofft"), ("zeit", "denkt")]),
    schild("Herr Feldmann", FX, "anspr", FE_F),
]))

# K Anspruchsprüfung: Grundlage, formell, materiell, Rechtsfolge --------------------------------------------------------------------
folie([("agl", f"{BE} › I. Anspruchsgrundlage, § 18 StrWG NRW"), ("form", f"{BE} › II. formelle Voraussetzungen"),
       ("mat", f"{BE} › III. materielle Voraussetzungen"), ("rf", f"{BE} › IV. Rechtsfolge: gebunden oder Ermessen?")],
      rechts_frei([
    *tafel("agl", "Anspruch auf die Erlaubnis"),
    *zz("I. Anspruchsgrundlage:", "§ 18 Abs. 1 StrWG NRW", 110, 180, "agl", beim("agl", "Paragraf")),
    zit("OVG NRW, Urt. v. 7.4.2017 – 11 A 2068/14, Rn. 49", 150, 232, beim("agl", "Sondernutzungserlaubnis")),
    *zz("II. formell:", "Antrag bei der zuständigen Stadt", 110, 300, "form", beim("form", "Antrag")),
    ok(860, 320, beim("form", "gestellt"), gr=20),
    *zz("III. materiell:", "6 Tische auf dem Gehweg,", 110, 395, "mat", beim("mat", "Sechs")),
    z("über den Gemeingebrauch hinaus: Sondernutzung", 150, 450, beim("mat", "Gemeingebrauch"), size=34),
    ok(1120, 470, beim("mat", "Sondernutzung"), gr=20),
    *zz("IV. Rechtsfolge:", "gebunden oder Ermessen?", 110, 545, "rf", beim("rf", "gebunden")),
    blk(150, 610, 1000, 70, GELB, beim("rf", "Ermessen", 2), [("Ermessen der Stadt", "ExtraBold", 36, INK)]),
    zit("OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 29, 58", 150, 700, beim("rf", "Ermessen", 2)),
    *tische(IX - 160, "agl", breite=52, abstand=64, unten=IU),
    pl("6 Tische", IX, 230, beim("mat", "Sechs"), fill=GELB, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("agl", "ruhig"), ("rf", "denkt")]),
    schild("Herr Feldmann", FX, "agl", FE_F),
]))

# L Ermessensfehler: falscher Sachverhalt ---------------------------------------------------------------------------------------
folie([("fehler", f"{BE} › IV. Rechtsfolge › Ermessensfehler?"), ("rw", f"{BE} › Ablehnung rechtswidrig, Rechtsverletzung")],
      rechts_frei([
    *tafel("fehler", "Ermessen auf falscher Grundlage"),
    z("nur Anspruch auf fehlerfreie Entscheidung", 110, 180, beim("fehler", "Anspruch"), "Bold", 34),
    zit("OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 58–62", 150, 232, beim("fehler", "Entscheidung")),
    z("Stadt: abgewogen, aber auf falscher Grundlage", 110, 300, beim("fehler2", "abgewogen"), size=34),
    z("Gericht: Gehweg 5 m breit, 3 m bleiben frei", 110, 360, beim("messen", "Gehweg"), size=34),
    blk(110, 430, 1040, 70, ROT, beim("fehler3", "falschen"), [("falscher Sachverhalt: Ermessensfehler", "ExtraBold", 36, INK)]),
    zit("OVG NRW, Urt. v. 7.4.2017 – 11 A 2068/14, Rn. 57, 90", 150, 520, beim("fehler3", "fehlerhaft")),
    z("Ablehnung rechtswidrig,", 110, 595, beim("rw", "rechtswidrig"), "Bold", 36),
    z("Anspruch auf fehlerfreie Entscheidung verletzt", 150, 650, beim("rw", "verletzt"), size=34),
    ficon("tabler", "ruler-measure", IX, IU - 40, 120, beim("messen", "Gehweg"), fuell=GELB),
    pl("5 m breit", IX, 190, beim("messen", "fünf"), fill=WEISS, size=28, anker="m"),
    pl("3 m frei", IX, 300, beim("messen", "drei"), fill=GRUEN, size=28, anker="m"),
    *fig("RI", FX, FB, FR, [("fehler", "ruhig")]),
    schild("die Richterin", FX, "fehler", RI_F),
]))

# M Spruchreife --------------------------------------------------------------------------------------------------------------------
folie([("spruch", f"{BE} › V. Spruchreife")], rechts_frei([
    *tafel("spruch", "Spruchreife"),
    z("Gericht macht die Sache grundsätzlich selbst", 110, 175, beim("spruch", "Gericht"), "Bold", 34),
    z("spruchreif, klärt den Sachverhalt auf", 150, 228, beim("spruch", "Sachverhalt"), size=34),
    zit("BVerwG, Urt. v. 11.7.2018 – 1 C 18.17, Rn. 28", 150, 280, beim("spruch", "aufklären")),
    z("spruchreif, wenn feststeht, welche Entscheidung", 110, 345, beim("spruch2", "feststeht"), "Bold", 34),
    z("die Behörde treffen muss: gebunden oder", 150, 398, beim("spruch2", "gebundenen"), size=34),
    z("Ermessen auf null reduziert", 150, 451, beim("spruch2", "null"), size=34),
    zit("BVerwG, Beschl. v. 23.1.2014 – 1 B 16.13, Rn. 4", 150, 503, beim("spruch2", "reduziert")),
    blk(110, 560, 1040, 68, GRUEN, beim("vu", "Verpflichtungsurteil"), [("dann: Verpflichtungsurteil, Satz 1", "ExtraBold", 34, INK)]),
    z("Das Ermessen selbst übt das Gericht nicht aus.", 110, 655, beim("grenze", "Ermessen"), "Bold", 34),
    zit("vgl. BVerwG, Urt. v. 11.7.2018 – 1 C 18.17, Rn. 36", 150, 707, beim("grenze", "aus")),
    blk(110, 765, 1040, 68, GELB, beim("bu", "Bescheidungsurteil"), [("sonst: Bescheidungsurteil, Satz 2", "ExtraBold", 34, INK)]),
    ficon(HC, "balance-scale", IX, IU, 150, "spruch", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("spruch", "ruhig")]),
    schild("die Richterin", FX, "spruch", RI_F),
]))

# N Im Fall: nicht spruchreif -------------------------------------------------------------------------------------------------------
folie([("fall2", f"{BE} › V. Spruchreife › im Fall"), ("erg", "Ergebnis · Bescheidungsurteil")], rechts_frei([
    *tafel("fall2", "Der Fall: spruchreif?"),
    z("Raum für andere Gründe mit Bezug zur Straße:", 110, 185, beim("fall2", "Raum"), "Bold", 34),
    z("Stadtbild, Lärm für die Anwohner", 150, 240, beim("fall2", "Stadtbild"), size=34),
    zit("OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 67", 150, 292, beim("fall2", "Anwohner")),
    z("Ermessen nicht auf null reduziert", 110, 370, beim("null", "nicht"), "Bold", 36),
    nein(720, 392, beim("null", "reduziert"), gr=22),
    z("Sache nicht spruchreif", 110, 435, beim("nsr", "nicht"), "Bold", 36),
    nein(520, 457, beim("nsr", "spruchreif"), gr=22),
    blk(110, 530, 1040, 76, GELB, beim("erg", "Bescheidungsurteil"), [("Bescheidungsurteil, § 113 Abs. 5 Satz 2 VwGO", "ExtraBold", 34, INK)]),
    ficon("tabler", "building", IX - 90, IU, 110, beim("fall2", "Stadtbild"), fuell=WEISS),
    pl("Stadtbild", IX - 90, 220, beim("fall2", "Stadtbild"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "volume", IX + 100, IU, 100, beim("fall2", "Lärm"), fuell=WEISS),
    pl("Lärm", IX + 100, 220, beim("fall2", "Lärm"), fill=WEISS, size=28, anker="m"),
    *fig("FE", FX, FB, FR, [("fall2", "denkt"), ("null", "sorge"), ("erg", "ruhig")]),
    schild("Herr Feldmann", FX, "fall2", FE_F),
]))

# O Tenorformeln (Klausurkonvention) -------------------------------------------------------------------------------------------------
folie([("tenor", "Tenor · Verpflichtung oder Bescheidung")], rechts_frei([
    *tafel("tenor", "Tenor: zwei Formeln"),
    blk(110, 170, 1040, 60, GRUEN, beim("tv", "Verpflichtungsurteil"), [("Verpflichtungsurteil", "ExtraBold", 32, INK)]),
    z("Die Beklagte wird unter Aufhebung des Bescheids", 130, 245, beim("tv", "Beklagte"), size=32),
    z("verpflichtet, dem Kläger die beantragte Erlaubnis", 130, 293, beim("tv", "verpflichtet"), size=32),
    z("zu erteilen.", 130, 341, beim("tv", "erteilen"), size=32),
    blk(110, 405, 1040, 60, GELB, beim("tb", "Bescheidungsurteil"), [("Bescheidungsurteil", "ExtraBold", 32, INK)]),
    z("Die Beklagte wird unter Aufhebung des Bescheids", 130, 480, beim("tb", "Beklagte"), size=32),
    z("verpflichtet, über den Antrag des Klägers unter", 130, 528, beim("tb", "verpflichtet"), size=32),
    z("Beachtung der Rechtsauffassung des Gerichts", 130, 576, beim("tb", "Beachtung"), size=32),
    z("erneut zu entscheiden.", 130, 624, beim("tb", "erneut"), size=32),
    z("Erlaubnis verlangt? Dann zusätzlich:", 130, 700, beim("tim", "Erlaubnis"), size=32),
    z("Im Übrigen wird die Klage abgewiesen.", 130, 750, beim("tim", "Im"), "Bold", 34),
    ficon(HC, "balance-scale", IX, IU, 150, "tenor", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("tenor", "ruhig")]),
    schild("die Richterin", FX, "tenor", RI_F),
]))

# P Das Urteil ------------------------------------------------------------------------------------------------------------------------
RIX, FEX2 = 1420, 600
RIb = ("RI_redet", RIX, BODEN, FH)
FEb2 = ("FE_redetfroh_r", FEX2, BODEN, FH)
folie([("urteil", "Ergebnis · Das Urteil")], [
    linienzug([(60, BODEN), (1860, BODEN)], "urteil", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "urteil", fill=GELB, size=40),
    ficon(HC, "balance-scale", 1010, 700, 150, "urteil", fuell=WEISS),
    *fig("FE", FEX2, BODEN, FH, [("urteil", "ruhig_r"), (beim("ri1", "Im"), "denkt_r")], bis="fe2"),
    *redet("FE_redetfroh_r", FEX2, BODEN, FH, "fe2", "tipp"),
    schild("Herr Feldmann", FEX2, "urteil", FE_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [("urteil", "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "fe2"),
    peep_voll("RI_ruhig", RIX, BODEN, FH, "fe2", anim="cut"),
    schild("die Richterin", RIX, "urteil", RI_F, unten=BODEN),
    blase("sprech", 1000, 230, "ri1", 960, 215, inhalt=["Die Stadt muss über den Antrag neu entscheiden,",
                                                      "unter Beachtung der Rechtsauffassung des Gerichts.",
                                                      "Im Übrigen wird die Klage abgewiesen."], textsize=30, figur=RIb, bis="fe2"),
    blase("sprech", 760, 170, "fe2", 700, 230, inhalt=["Immerhin. Diesmal mit den richtigen Zahlen."], textsize=30,
          figur=FEb2, bis="tipp"),
])

# Q Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Antrag, Spruchreife und Tenor")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Den Antrag genau ansehen.", 200, 200, beim("tipp", "Antrag"), "Bold", 36),
    z("Behörde hat Ermessen: Ein Ermessensfehler führt", 200, 300, beim("tipp1", "Ermessen"), size=34),
    z("meist nur zum Bescheidungsurteil.", 200, 355, beim("tipp1", "Bescheidungsurteil"), "Bold", 34),
    z("Am Ende immer: Spruchreife prüfen,", 200, 455, beim("tipp2", "Spruchreife"), "Bold", 36),
    z("den Tenor passend formulieren.", 200, 510, beim("tipp2", "Tenor"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# R Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 36, 80
els_t = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Klausurschema: Verpflichtungsklage"), 110, 85, "sch", 46)]
links = [("sa", "A. Zulässigkeit", "ExtraBold"),
         ("s1", "I. Verwaltungsrechtsweg, § 40 VwGO", "Regular"),
         ("s2", "II. Statthaftigkeit, § 42 I Alt. 2 VwGO", "Regular"),
         ("s3", "III. Klagebefugnis, § 42 II VwGO", "Regular"),
         ("s4", "IV. Vorverfahren, § 68 II VwGO", "Regular"),
         ("s5", "V. Klagefrist, § 74 II VwGO", "Regular"),
         ("s6", "VI. Klagegegner, § 78 VwGO", "Regular")]
rechts = [("sb", "B. Begründetheit, § 113 V VwGO", "ExtraBold"),
          ("sz", "maßgeblicher Zeitpunkt", "Regular"),
          ("s7", "I. Anspruchsgrundlage", "Regular"),
          ("s8", "II. formelle Voraussetzungen", "Regular"),
          ("s9", "III. materielle Voraussetzungen", "Regular"),
          ("s10", "IV. Rechtsfolge: gebunden oder Ermessen", "Regular"),
          (beim("s11", "Spruchreife"), "V. Spruchreife: Verpflichtung", "Regular"),
          (beim("s11", "Bescheidung"), "oder Bescheidung", "Regular")]
for i, (c, t, s) in enumerate(links):
    els_t.append(z(t, 110 + (0 if i == 0 else 30), 200 + i * LH, c, s, SZ + (4 if i == 0 else 0), rechts=950))
for i, (c, t, s) in enumerate(rechts):
    els_t.append(z(t, 990 + (0 if i == 0 else 30) + (40 if i == 7 else 0), 200 + i * LH - (LH - 52 if i == 7 else 0), c, s, SZ + (4 if i == 0 else 0),
                   rechts=1820))
folie([("sch", "Klausurschema · Verpflichtungsklage")], els_t)

# S Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Spruchreif ist die Sache, ", 0), ("wenn feststeht,", "a")]], 750, 320, 46, "merke",
                {"a": beim("merke", "feststeht")}),
    *markertext([[("was die Behörde tun muss.", 0)]], 750, 385, 46, beim("merke", "was"), {}),
    *markertext([[("Dann verpflichtet das Gericht ", 0), ("zum Erlass,", "b")]], 750, 535, 46, "m2",
                {"b": beim("m2", "Erlass")}),
    *markertext([[("sonst nur ", 0), ("zur neuen Entscheidung.", "c")]], 750, 600, 46, beim("m2", "sonst"),
                {"c": beim("m2", "neuen")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
