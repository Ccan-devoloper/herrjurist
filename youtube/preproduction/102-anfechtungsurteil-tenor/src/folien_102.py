"""Folge 102 · Anfechtungsurteil Tenor: „in Gestalt des Widerspruchsbescheids“ – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Abwassergebühr einer Wäscherei, 2.400 € statt 1.500 €, Beispielland Nordrhein-Westfalen), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Wäscherei (Gebührenbescheid, Widerspruchsbescheid), B Verwaltungsgericht (Feststellung,
Frage), C Sachverhalt, D Vorfrage NRW (§ 110 II 1 Nr. 6, § 111 JustG NRW), E Gegenstand (Wortlaut § 79 I Nr. 1), F Umfang
(Wortlaut § 113 I 1, Teilbarkeit), G Tenor Hauptsache, H Klausurtipp § 113 II (Lexi), I Kosten (Wortlaut § 155 I 1, 5/8),
J Vorläufige Vollstreckbarkeit, K Berufung, L vollständiger Tenor, M Schema, N Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als Herr Zimmermann den Widerspruchsbescheid bringt). Hilfsfunktionen wie 093."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_102/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_102/" in n:
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
RE_F, ZI_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
TN = "Tenor"


def tenorbox(x, y, w, h, cue, bis=None):
    """Kasten für den Urteilstenor (hellgelb, schmale Kontur) mit kleinem Etikett „Tenor“."""
    return [bis_(karte(x, y, w, h, cue, fill=HELL, rund=16, schatten=6, rand=4), bis),
            pl("Tenor", x + 20, y - 48, cue, fill=GELB, size=26, bis=bis)]


def reihe(teile, x, y, gap=18):
    """Pillen nebeneinander (Breite aus dem Sprite): teile = [(text, cue, fill)]."""
    els = []
    for text, cue, fill in teile:
        e = pl(text, x, y, cue, fill=fill, size=30)
        els.append(e)
        x = e.x + e.sprite.width + gap
    assert x - gap <= 1170, "Pillenreihe zu breit"
    return els


# A Fall: die Wäscherei, der Gebührenbescheid, der Widerspruch ------------------------------------------------------------
HAX, REX, ZIX = 260, 1130, 1660
REb = ("RE_redet_r", REX, BODEN, FH)
ZIb = ("ZI_redet", ZIX, BODEN, FH)
KOMMT = beim("zimmer", "Herr")
folie([(NULL, "Fall · Der Gebührenbescheid"), ("zimmer", "Fall · Der Widerspruchsbescheid")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Wäscherei im eigenen Haus", 70, 40, NULL, fill=GELB, size=40)),
    ficon("ph", "house", HAX, BODEN - 2, 330, NULL, fuell=BLAU, anim="cut"),
    ficon("ph", "washing-machine", 500, BODEN - 2, 90, NULL, fuell=WEISS, anim="cut"),
    ficon("ph", "washing-machine", 610, BODEN - 2, 90, NULL, fuell=WEISS, anim="cut"),
    *fig("RE", REX, BODEN, FH, [(NULL, "ruhig_r"), (beim("bescheid", "zweitausendvierhundert"), "sorge_r"),
                               (beim("zaehler", "nur"), "denkt_r"), ("widerspr", "ruhig_r"), (KOMMT, "sorge_r"),
                               (beim("zi1", "zurückgewiesen"), "aerger_r")], bis="re1", erst="cut"),
    *redet("RE_redet_r", REX, BODEN, FH, "re1", "klage"),
    hart(schild("Frau Rehbein, Wäscherei", REX, NULL, RE_F, unten=BODEN, d=0.0)),
    ficon("tabler", "file-text", 840, 640, 90, beim("bescheid", "Gebührenbescheid"), fuell=WEISS),
    pl("Gebührenbescheid: 2.400 €", 840, 680, beim("bescheid", "zweitausendvierhundert"), fill=WEISS, size=30, anker="m"),
    pl("Satzung: 6 € je m³", 840, 745, beim("rechnung", "sechs"), fill=GELB, size=28, anker="m"),
    pl("Stadt: 400 m³ = 2.400 €", 840, 805, beim("rechnung", "vierhundert"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "gauge", 560, 520, 100, "zaehler", fuell=GELB),
    pl("Zähler: 250 m³", 560, 560, beim("zaehler", "zweihundertfünfzig"), fill=GRUEN, size=28, anker="m"),
    pl("Widerspruch", 840, 470, "widerspr", fill=GELB, size=30, anker="m"),
    nein(975, 490, beim("zi1", "zurückgewiesen"), gr=26),
    *fig("ZI", ZIX, BODEN, FH, [(KOMMT, "ruhig")], bis="zi1"),
    *redet("ZI_redet", ZIX, BODEN, FH, "zi1", "re1"),
    *fig("ZI", ZIX, BODEN, FH, [("re1", "denkt")], erst="cut"),
    schild("Herr Zimmermann, Stadt", ZIX, KOMMT, ZI_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", ZIX - 250, 700, 90, beim("zimmer", "Widerspruchsbescheid"), fuell=WEISS),
          "102brief*", 0.8, -0.44),
    pl("Widerspruchsbescheid", ZIX - 250, 745, beim("zimmer", "Widerspruchsbescheid"), fill=WEISS, size=26, anker="m"),
    blase("sprech", 900, 210, "zi1", 1260, 240, inhalt=["Frau Rehbein, wir bleiben bei 400 Kubikmetern.",
                                                       "Ihr Widerspruch wird zurückgewiesen."], textsize=30, figur=ZIb, bis="re1"),
    blase("sprech", 600, 210, "re1", 780, 240, inhalt=["Dann klage ich.", "Der ganze Bescheid muss weg!"], textsize=32,
          figur=REb, bis="klage"),
])

# B Gericht: Feststellung und Frage -------------------------------------------------------------------------------------------
REX2, RIX = 1190, 1670
RIb = ("RI_redet", RIX, BODEN, FH)
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Wie lautet der Tenor?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, beim("klage", "Verwaltungsgericht"), fill=GELB, size=40),
    ficon(HC, "classical-building", 330, BODEN - 2, 400, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 790, 640, 90, beim("klage", "klagt"), fuell=WEISS),
    pl("Klage: ganzen Bescheid aufheben", 790, 680, beim("klage", "Aufhebung"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "gauge", 790, 560, 90, "gericht", fuell=GELB, bis="hook"),
    pl("verbraucht: 250 m³", 790, 745, beim("ri1", "zweihundertfünfzig"), fill=GRUEN, size=28, anker="m"),
    pl("rechtmäßig: 1.500 €", 790, 805, beim("ri1", "tausendfünfhundert"), fill=GRUEN, size=28, anker="m"),
    *fig("RE", REX2, BODEN, FH, [("klage", "ruhig_r"), (beim("ri1", "Rechtmäßig"), "denkt_r"), ("frage", "ruhig_r")]),
    schild("Frau Rehbein", REX2, "klage", RE_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [("gericht", "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "hook"),
    peep_voll("RI_ruhig", RIX, BODEN, FH, "hook", anim="cut"),
    schild("der Richter", RIX, "gericht", RI_F, unten=BODEN),
    blase("sprech", 820, 200, "ri1", 1250, 250, inhalt=["Verbraucht wurden 250 Kubikmeter.",
                                                       "Rechtmäßig sind nur 1.500 Euro."], textsize=32, figur=RIb, bis="hook"),
    # Balken: 2.400 € = 1.500 € rechtmäßig + 900 € rechtswidrig
    karte(100, 150, 900, 76, beim("hook", "zweitausendvierhundert"), fill=WEISS, rund=12, schatten=5, rand=4),
    z("Bescheid: 2.400 €", 130, 168, beim("hook", "zweitausendvierhundert"), "Bold", 32),
    karte(100, 150, 562, 76, beim("hook", "neunhundert"), fill=GRUEN, rund=12, schatten=0, rand=4),
    z("1.500 € rechtmäßig", 130, 168, beim("hook", "neunhundert"), "Bold", 32),
    karte(662, 150, 338, 76, beim("hook", "neunhundert"), fill=ROT, rund=12, schatten=0, rand=4),
    z("900 € rechtswidrig", 690, 168, beim("hook", "rechtswidrig"), "Bold", 32),
    pl("Wie lautet der Tenor?", 1420, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Rolle des Widerspruchsbescheids?", 1420, 240, "frage2", fill=WEISS, size=34, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Rehbein betreibt eine Wäscherei im eigenen Haus in einer Stadt in Nordrhein-Westfalen. Mit Bescheid vom "
    "2. März 2026 setzt die Stadt die Abwassergebühr auf 2.400 € fest: Ihre Satzung verlangt 6 € je m³, die Stadt rechnet "
    "mit 400 m³. Frau Rehbein legt Widerspruch ein, der Zähler zeige nur 250 m³. Die Stadt weist den Widerspruch mit "
    "Bescheid vom 4. Mai 2026 zurück. Frau Rehbein klagt fristgerecht und beantragt, den ganzen Bescheid aufzuheben.",
    "Das Gericht stellt fest: Verbraucht wurden 250 m³; im Übrigen ist der Bescheid rechtmäßig. Die Kosten, die "
    "jede Seite vollstrecken kann, liegen unter 1.500 €.",
], "Wie lautet der Tenor des Urteils?")

# D Vorfrage: Warum ein Widerspruchsbescheid? (Beispiel NRW) -------------------------------------------------------------------
folie([("vv", "Vorfrage · Vorverfahren in NRW, § 110 JustG NRW")], rechts_frei([
    *tafel("vv", "Warum ein Widerspruchsbescheid?"),
    pl("Beispiel: Nordrhein-Westfalen", 110, 185, beim("nrw", "Nordrhein"), fill=PINK, size=32),
    z("Vorverfahren entfällt meist, § 110 Abs. 1 JustG NRW,", 110, 285, beim("nrw", "entfällt"), size=34),
    z("nicht aber bei Bescheiden nach dem", 110, 345, beim("nrw", "nicht"), "Bold", 34),
    z("Kommunalabgabengesetz", 150, 400, beim("nrw", "Kommunalabgabengesetz"), "Bold", 34),
    zit("§ 110 Abs. 2 Satz 1 Nr. 6 JustG NRW", 150, 452, beim("nrw", "Paragraf")),
    pl("In deinem Land: ggf. anders", 110, 520, "land", fill=PINK, size=30),
    z("Widerspruchsbehörde: die Stadt selbst", 110, 630, beim("wsb", "Stadt"), "Bold", 34),
    zit("§ 111 Satz 1 JustG NRW", 150, 682, beim("wsb", "selbst")),
    ficon("tabler", "rubber-stamp", IX, IU, 120, "vv", fuell=WEISS),
    pl("Widerspruchsbescheid", IX, 200, beim("vv", "Widerspruchsbescheid"), fill=WEISS, size=28, anker="m"),
    *fig("ZI", FX, FB, FR, [("vv", "ruhig"), ("wsb", "denkt")]),
    schild("Herr Zimmermann, Stadt", FX, "vv", ZI_F),
]))

# E Gegenstand: Wortlaut § 79 Abs. 1 Nr. 1 VwGO, Tenoranfang -----------------------------------------------------------------------
W79 = ("„Gegenstand der Anfechtungsklage ist 1. der ursprüngliche Verwaltungsakt in der Gestalt, die er durch den "
       "Widerspruchsbescheid gefunden hat, …“")
Z79 = ["„Gegenstand der Anfechtungsklage ist",
       "1. der ursprüngliche Verwaltungsakt in der Gestalt,",
       "die er durch den Widerspruchsbescheid gefunden hat, …“"]
w79, w79_y = wortlaut(80, 150, 1100, W79, "§ 79 Abs. 1 Nr. 1 VwGO", "wl79", size=34, zeilen=Z79,
                      marken=[("in der Gestalt,", beim("wl79", "Gestalt")),
                              ("Widerspruchsbescheid", beim("wl79", "Widerspruchsbescheid"))])
folie([("wl79", f"{TN} › Gegenstand, § 79 I Nr. 1 VwGO")], rechts_frei([
    titel(glyphen("Gegenstand der Klage"), 110, 60, "wl79", 44),
    *w79,
    z("angegriffen: der Gebührenbescheid, wie ihn", 110, w79_y + 22, beim("beide", "Gebührenbescheid"), "Bold", 34),
    z("der Widerspruchsbescheid bestätigt hat", 150, w79_y + 74, beim("beide", "Widerspruchsbescheid"), size=34),
    *tenorbox(90, w79_y + 160, 1090, 120, beim("t1", "Tenor")),
    z("Der Gebührenbescheid der Beklagten vom 2. März 2026", 120, w79_y + 178, beim("t1", "Gebührenbescheid"), size=32),
    z("in Gestalt des Widerspruchsbescheids vom 4. Mai 2026 …", 120, w79_y + 226, beim("t1", "Gestalt"), "Bold", 32),
    z("Beklagte: die Stadt, § 78 Abs. 1 Nr. 1 VwGO", 110, w79_y + 310, beim("bekl", "Beklagte"), size=32),
    z("Widerspruchsbescheid allein: nur bei erstmaliger oder", 110, w79_y + 370, beim("isol", "Widerspruchsbescheid"), size=32),
    z("zusätzlicher selbständiger Beschwer, § 79 I Nr. 2, II", 150, w79_y + 418, beim("isol", "zusätzlich"), size=32),
    ficon("tabler", "file-text", IX - 70, IU, 100, "wl79", fuell=WEISS),
    ficon("tabler", "file-text", IX + 70, IU, 100, beim("wl79", "Widerspruchsbescheid"), fuell=GELB),
    pl("Bescheid + Widerspruchsbescheid", IX, 190, beim("wl79", "Widerspruchsbescheid"), fill=WEISS, size=26, anker="m"),
    *fig("RE", FX, FB, FR, [("wl79", "denkt"), ("t1", "ruhig")]),
    schild("Frau Rehbein", FX, "wl79", RE_F),
]))

# F Umfang: Wortlaut § 113 Abs. 1 Satz 1 VwGO, Teilbarkeit -------------------------------------------------------------------------
W113 = ("„Soweit der Verwaltungsakt rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht "
        "den Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“")
Z113 = ["„Soweit der Verwaltungsakt rechtswidrig und der Kläger",
        "dadurch in seinen Rechten verletzt ist, hebt das Gericht",
        "den Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“"]
w113, w113_y = wortlaut(80, 150, 1100, W113, "§ 113 Abs. 1 Satz 1 VwGO", "wl113", size=32, zeilen=Z113,
                        marken=[("rechtswidrig", beim("wl113", "rechtswidrig")),
                                ("hebt das Gericht", beim("wl113", "hebt")),
                                ("„Soweit", beim("soweit", "soweit"))])
folie([("wl113", f"{TN} › Umfang: „soweit“, § 113 I 1 VwGO")], rechts_frei([
    titel(glyphen("Umfang der Aufhebung"), 110, 60, "wl113", 44),
    *w113,
    blk(110, w113_y + 24, 1040, 64, GELB, beim("soweit", "soweit"), [("Schlüsselwort: „soweit“", "ExtraBold", 36, INK)]),
    z("Teilaufhebung nur, wenn der Bescheid teilbar ist:", 110, w113_y + 118, beim("teil", "teilbar"), "Bold", 34),
    z("der Rest muss sinnvoll und rechtmäßig bestehen", 150, w113_y + 172, beim("teil", "Rest"), size=34),
    z("bleiben können", 150, w113_y + 222, beim("teil", "bleiben"), size=34),
    zit("BVerwG, Beschl. v. 10.10.2023 – 9 B 18.23, Rn. 7", 150, w113_y + 272, beim("teil", "können")),
    z("hier: eine Gebühr von 1.500 € kann für sich stehen", 110, w113_y + 330, beim("teil2", "Gebühr"), "Bold", 34),
    ok(1060, w113_y + 352, beim("teil2", "stehen"), gr=20),
    z("insoweit Rechtsverletzung der Adressatin", 110, w113_y + 392, beim("rv", "Adressatin"), size=34),
    zit("vgl. BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 150, w113_y + 442, beim("rv", "Rechten")),
    ficon(HC, "balance-scale", IX, IU, 150, "wl113", fuell=WEISS),
    pl("1.500 € bleiben", IX, 170, beim("teil2", "tausendfünfhundert"), fill=GRUEN, size=28, anker="m"),
    *fig("RI", FX, FB, FR, [("wl113", "ruhig")]),
    schild("der Richter", FX, "wl113", RI_F),
]))

# G Tenor: die Hauptsache -----------------------------------------------------------------------------------------------------------
folie([("t2", f"{TN} › Umfang: aufheben, soweit; im Übrigen abweisen")], rechts_frei([
    *tafel("t2", "Tenor: die Hauptsache"),
    *tenorbox(90, 200, 1090, 400, "t2"),
    z("Der Gebührenbescheid der Beklagten vom 2. März 2026", 120, 222, "t2", size=32),
    z("in Gestalt des Widerspruchsbescheids vom 4. Mai 2026", 120, 272, "t2", size=32),
    z("wird aufgehoben, soweit darin eine Gebühr von", 120, 322, beim("t2", "aufgehoben"), "Bold", 32),
    z("mehr als 1.500 € festgesetzt wird.", 120, 372, beim("t2", "mehr"), "Bold", 32),
    pl("Antrag: den ganzen Bescheid aufheben", 120, 440, beim("t3", "ganzen"), fill=WEISS, size=28),
    z("Im Übrigen wird die Klage abgewiesen.", 120, 520, beim("t3", "Im"), "Bold", 34),
    warnung_i(150, 690, "fehler", gr=26),
    z("typischer Klausurfehler: diesen Satz vergessen", 200, 668, beim("fehler", "Klausurfehler"), "Bold", 34),
    ficon("tabler", "file-text", IX, IU, 110, "t2", fuell=WEISS),
    pl("mehr als 1.500 €: aufgehoben", IX, 140, beim("t2", "mehr"), fill=ROT, size=28, anker="m"),
    pl("im Übrigen: abgewiesen", IX, 210, beim("t3", "abgewiesen"), fill=WEISS, size=28, anker="m"),
    *fig("RE", FX, FB, FR, [("t2", "ruhig"), (beim("t3", "abgewiesen"), "sorge")]),
    schild("Frau Rehbein", FX, "t2", RE_F),
]))

# H Klausurtipp (Lexi): § 113 Abs. 2 VwGO -----------------------------------------------------------------------------------------
W1132 = ("„Begehrt der Kläger die Änderung eines Verwaltungsakts, der einen Geldbetrag festsetzt …, kann das Gericht den "
         "Betrag in anderer Höhe festsetzen …“")
Z1132 = ["„Begehrt der Kläger die Änderung eines Verwaltungsakts,",
         "der einen Geldbetrag festsetzt …, kann das Gericht den",
         "Betrag in anderer Höhe festsetzen …“"]
w1132, w1132_y = wortlaut(100, 270, 1080, W1132, "§ 113 Abs. 2 Satz 1 VwGO (Auszug)", "wl1132", size=32, zeilen=Z1132,
                          marken=[("in anderer Höhe festsetzen", beim("wl1132", "anderer"))])
folie([("tipp", "Klausurtipp · Änderung nach § 113 II VwGO")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Schau auf den Antrag.", 200, 200, beim("tipp", "Antrag"), "Bold", 36),
    *w1132,
    z("Tenor dann etwa:", 130, w1132_y + 22, beim("tipp2", "Tenor"), "Bold", 32),
    z("Der Bescheid wird dahin geändert, dass die Gebühr", 130, w1132_y + 72, beim("tipp2", "Bescheid"), size=32),
    z("auf 1.500 € festgesetzt wird.", 130, w1132_y + 120, beim("tipp2", "auf"), size=32),
    zit("Formulierungsbeispiel (Klausurkonvention)", 130, w1132_y + 170, beim("tipp2", "festgesetzt")),
    blk(110, w1132_y + 225, 1040, 64, GRUEN, beim("tipp3", "beiden"), [("In beiden Fassungen: 1.500 €", "ExtraBold", 34, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "kosten"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# I Kosten: Wortlaut § 155 Abs. 1 Satz 1 VwGO, Quote ------------------------------------------------------------------------------
W155 = "„Wenn ein Beteiligter teils obsiegt, teils unterliegt, so sind die Kosten gegeneinander aufzuheben oder verhältnismäßig zu teilen.“"
Z155 = ["„Wenn ein Beteiligter teils obsiegt, teils unterliegt, so sind",
        "die Kosten gegeneinander aufzuheben oder verhältnismäßig",
        "zu teilen.“"]
w155, w155_y = wortlaut(80, 150, 1100, W155, "§ 155 Abs. 1 Satz 1 VwGO", "kosten", size=32, zeilen=Z155,
                        marken=[("verhältnismäßig", beim("kosten", "verhältnismäßig"))])
folie([("kosten", f"{TN} › Kosten, § 155 I 1 VwGO")], rechts_frei([
    titel(glyphen("Die Kosten"), 110, 60, "kosten", 44),
    *w155,
    *reihe([("Antrag: 2.400 €", beim("quote", "zweitausendvierhundert"), WEISS),
            ("gewonnen: 900 €", beim("quote", "gewinnt"), GRUEN),
            ("verloren: 1.500 €", beim("quote", "verliert"), ROT)], 110, w155_y + 30),
    blk(110, w155_y + 120, 1040, 76, GELB, beim("bruch", "Tausendfünfhundert"),
        [("1.500 € von 2.400 € = 5/8", "ExtraBold", 40, INK)]),
    *tenorbox(90, w155_y + 260, 1090, 120, beim("t4", "Kosten")),
    z("Die Kosten des Verfahrens tragen die Klägerin", 120, w155_y + 278, beim("t4", "Kosten"), size=32),
    *zz("zu 5/8", "und die Beklagte zu 3/8.", 120, w155_y + 326, beim("t4", "fünf"), beim("t4", "Beklagte"), size=32),
    ficon("tabler", "calculator", IX, IU, 110, "kosten", fuell=WEISS),
    pl("5/8 zu 3/8", IX, 210, beim("t4", "drei"), fill=GELB, size=28, anker="m"),
    *fig("RE", FX, FB, FR, [("kosten", "denkt"), (beim("quote", "verliert"), "sorge"), ("t4", "ruhig")]),
    schild("Frau Rehbein", FX, "kosten", RE_F),
]))

# J Vorläufige Vollstreckbarkeit ---------------------------------------------------------------------------------------------
folie([("vollstr", f"{TN} › Vorläufige Vollstreckbarkeit, § 167 VwGO")], rechts_frei([
    *tafel("vollstr", "Vorläufige Vollstreckbarkeit"),
    *zz("§ 167 Abs. 2 VwGO:", "Anfechtungsurteile nur wegen der Kosten", 110, 175, beim("vollstr", "Paragraf"),
        beim("vollstr", "Anfechtungsurteile"), size=32, rest_stil="Regular"),
    *zz("§ 167 Abs. 1 Satz 1 VwGO:", "ZPO entsprechend", 110, 228, beim("zpo", "Absatz"), beim("zpo", "Z"), size=32,
        rest_stil="Regular"),
    *zz("Kosten hier unter 1.500 €:", "§ 708 Nr. 11, § 711 ZPO", 110, 281, beim("zpo", "tausendfünfhundert"),
        beim("zpo", "Paragraf"), size=32, rest_stil="Regular"),
    *tenorbox(90, 370, 1090, 400, "t5"),
    z("Das Urteil ist wegen der Kosten vorläufig vollstreckbar.", 120, 390, beim("t5", "Das"), "Bold", 30),
    z("Der jeweilige Vollstreckungsschuldner darf die Vollstreckung", 120, 444, beim("t6", "jeweilige"), size=30),
    z("durch Sicherheitsleistung in Höhe von 110 % des vollstreckbaren", 120, 490, beim("t6", "durch"), size=30),
    z("Betrags abwenden, wenn nicht der jeweilige Vollstreckungsgläubiger", 120, 536, beim("t6", "Betrags"), size=30),
    z("vor der Vollstreckung Sicherheit in Höhe von 110 % des jeweils", 120, 582, beim("t6", "vor"), size=30),
    z("zu vollstreckenden Betrags leistet.", 120, 628, beim("t6", "vollstreckenden"), size=30),
    zit("Formel: vgl. OVG NRW, Urt. v. 3.12.2012 – 9 A 2646/11 (Tenor)", 120, 690, beim("t6", "leistet")),
    pl("„jeweils“: beide Seiten tragen Kosten", 110, 800, beim("jeweils", "beide"), fill=PINK, size=30),
    ficon("tabler", "coin", IX, IU, 110, "vollstr", fuell=GELB),
    pl("nur wegen der Kosten", IX, 210, beim("vollstr", "Kosten"), fill=WEISS, size=28, anker="m"),
    *fig("RI", FX, FB, FR, [("vollstr", "ruhig")]),
    schild("der Richter", FX, "vollstr", RI_F),
]))

# K Berufung ------------------------------------------------------------------------------------------------------------------
folie([("ber", f"{TN} › Berufung, § 124a I VwGO")], rechts_frei([
    *tafel("ber", "Und die Berufung?"),
    *zz("§ 124a Abs. 1 Satz 1 VwGO:", "Zulassung nur bei einem", 110, 190, beim("ber", "Paragraf"),
        beim("ber", "Zulassungsgrund"), size=34, rest_stil="Regular"),
    z("Zulassungsgrund nach § 124 Abs. 2 Nr. 3 oder 4 VwGO", 150, 245, beim("ber", "Paragraf", 2), size=34),
    blk(110, 340, 1040, 70, ROT, beim("ber2", "Nichtzulassung"), [("Nichtzulassung: Gericht nicht befugt", "ExtraBold", 36, INK)]),
    zit("§ 124a Abs. 1 Satz 3 VwGO", 150, 430, beim("ber2", "befugt")),
    ficon(HC, "balance-scale", IX, IU, 150, "ber", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("ber", "ruhig")]),
    schild("der Richter", FX, "ber", RI_F),
]))

# L Der vollständige Tenor (zum Mitschreiben, erscheint auf einmal) ----------------------------------------------------------------
els_v = [karte(110, 60, 1700, 900, "voll", fill=HELL), titel(glyphen("Der vollständige Tenor"), 170, 105, "voll", 56)]
y = 215
for absz, stil in (("Der Gebührenbescheid der Beklagten vom 2. März 2026 in Gestalt des Widerspruchsbescheids vom "
                    "4. Mai 2026 wird aufgehoben, soweit darin eine Gebühr von mehr als 1.500 € festgesetzt wird.", "Bold"),
                   ("Im Übrigen wird die Klage abgewiesen.", "Bold"),
                   ("Die Kosten des Verfahrens tragen die Klägerin zu 5/8 und die Beklagte zu 3/8.", "Regular"),
                   ("Das Urteil ist wegen der Kosten vorläufig vollstreckbar. Der jeweilige Vollstreckungsschuldner darf die "
                    "Vollstreckung durch Sicherheitsleistung in Höhe von 110 % des vollstreckbaren Betrags abwenden, wenn "
                    "nicht der jeweilige Vollstreckungsgläubiger vor der Vollstreckung Sicherheit in Höhe von 110 % des "
                    "jeweils zu vollstreckenden Betrags leistet.", "Regular")):
    e, y = absatz(glyphen(absz), 170, y, 1580, "voll", size=36, stil=stil)
    els_v += e; y += 26
assert y < 880, y
els_v.append(zit("Tenorformeln: Klausurkonvention nach dem Wortlaut der §§ 113, 155, 167 VwGO, §§ 708, 711 ZPO", 170, 885,
                 "voll", rechts=1790))
folie([("voll", "Ergebnis · Der vollständige Tenor")], els_v)

# M Schema: Tenor des Anfechtungsurteils -------------------------------------------------------------------------------------------
SZ, LH = 36, 86
els_s = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Schema: Tenor des Anfechtungsurteils"), 110, 85, "sch", 46)]
zeilen_s = [
    zz("1. Gegenstand:", "§ 79 Abs. 1 Nr. 1 VwGO", 110, 200, "s1", "s1", size=SZ, rest_stil="Regular", rechts=1820),
    [z("der Bescheid in Gestalt des Widerspruchsbescheids", 160, 200 + LH, "s1a", size=SZ, rechts=1820)],
    zz("2. Umfang:", "aufgehoben, soweit er rechtswidrig ist (§ 113 Abs. 1 Satz 1 VwGO)", 110, 200 + 2 * LH, "s1b",
       beim("s1b", "aufgehoben"), size=SZ, rest_stil="Regular", rechts=1820),
    [z("im Übrigen: Klageabweisung", 160, 200 + 3 * LH, "s1c", size=SZ, rechts=1820)],
    zz("3. Kosten:", "§ 154 Abs. 1 oder § 155 Abs. 1 Satz 1 VwGO", 110, 200 + 4 * LH, "s2", beim("s2", "Paragraf"), size=SZ,
       rest_stil="Regular", rechts=1820),
    zz("4. Vorläufige Vollstreckbarkeit:", "nur wegen der Kosten (§ 167 Abs. 2 VwGO)", 110, 200 + 5 * LH, "s3",
       beim("s3", "wegen"), size=SZ, rest_stil="Regular", rechts=1820),
    [z("ggf. Zulassung der Berufung (§ 124a Abs. 1 VwGO)", 110, 200 + 6 * LH, "s4", size=SZ, rechts=1820)],
]
for zl in zeilen_s:
    els_s += zl
folie([("sch", "Schema · Tenor des Anfechtungsurteils")], els_s)

# N Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Angegriffen wird der Bescheid ", 0), ("in Gestalt", "a")]], 750, 320, 46, "merke",
                {"a": beim("merke", "Gestalt")}),
    *markertext([[("des Widerspruchsbescheids.", 0)]], 750, 385, 46, beim("merke", "des"), {}),
    *markertext([[("Aufgehoben wird er nur, ", 0), ("soweit", "b")]], 750, 535, 46, "m2", {"b": beim("m2", "soweit")}),
    *markertext([[("er rechtswidrig ist und den Kläger", 0)]], 750, 600, 46, beim("m2", "rechtswidrig"), {}),
    *markertext([[("in seinen Rechten verletzt.", 0)]], 750, 665, 46, beim("m2", "in"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
