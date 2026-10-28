"""Folge 057 · Klagearten VwGO: Welche Klage passt? Der komplette Überblick – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Bootsverleih am See), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Seeufer (Bescheid des Bauamts), B Internetseite (Bürgermeister), C Seeufer (Elektroboote), D Frage, E Sachverhalt,
F Klagebegehren § 88 / Rechtsweg § 40, G Wortlaut § 42 I, H Anfechtungsklage, I Verpflichtungsklage, J allgemeine
Leistungsklage, K Feststellungsklage § 43 I, L Subsidiarität § 43 II, M Ergebnis, N Abwandlung 1 Seefest, O Wortlaut
§ 113 I 4 (Fortsetzungsfeststellungsklage), P Abwandlung 2 Normenkontrolle, Q Klausurtipp (Lexi), R Klausurschema
(Entscheidungsbaum), S Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, wenn Frau Thiele den Bescheid überreicht)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_057/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_057/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 020/025/028/032/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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
BE_F, TH_F, HA_F, LI_F = GRUEN, BLAU, LILA, GELB   # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270
SK = "Statthafte Klageart"
WASSER = (141, 179, 242, 255)


def ufer(cue, anim="cut", boote=True, bis_boote=None):
    """Seeufer: Boden, Wasser mit Wellen, Holzsteg; optional zwei Tretboote (Fluent canoe) auf dem Wasser."""
    els = [linienzug([(640, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           karte(60, BODEN - 8, 600, 96, cue, fill=WASSER, rund=10, schatten=0, rand=4),
           ficon("tabler", "ripple", 200, BODEN + 70, 90, cue, anim=anim),
           ficon("tabler", "ripple", 470, BODEN + 70, 90, cue, anim=anim),
           karte(400, BODEN - 34, 330, 26, cue, fill=HOLZ, rund=4, schatten=0, rand=4),
           linienzug([(440, BODEN - 8), (440, BODEN + 40)], cue, breite=8, farbe=INK),
           linienzug([(620, BODEN - 8), (620, BODEN + 40)], cue, breite=8, farbe=INK)]
    for e in els:
        e.anim = "cut" if anim == "cut" else e.anim
    if boote:
        els += [ficon(HC, "canoe", 170, BODEN + 10, 170, cue, fuell=GELB, anim=anim, bis=bis_boote),
                ficon(HC, "canoe", 330, BODEN + 12, 150, cue, fuell=ROT, anim=anim, bis=bis_boote)]
    return els


def wortlaut_folie(cue, titeltext, text, quelle, marken, size=34, y=170):
    w, y_ende = wortlaut(80, y, 1100, glyphen(text), quelle, cue, marken=marken, size=size)
    return [titel(glyphen(titeltext), 110, 75, cue, 50), *w], y_ende


# A Fall: der Bootsverleih am See, Post vom Bauamt --------------------------------------------------------------------
BEX, THX = 860, 1560
BEb = ("BE_redet_r", BEX, BODEN, FH)
THb = ("TH_redet", THX, BODEN, FH)
KOMMT = beim("thiele", "Thiele")
BESCHEID = beim("thiele", "Bescheid")
folie([(NULL, "Fall · Der Bootsverleih am See"), ("thiele", "Fall · Post vom Bauamt")], [
    *ufer(NULL),
    hart(pl("Tretboote am See", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "tree", 1800, BODEN - 2, 150, NULL, fuell=GRUEN, anim="cut"),
    *fig("BE", BEX, BODEN, FH, [(NULL, "ruhig_r"), ("woche", "sorge_r")], bis="be1", erst="cut"),
    *redet("BE_redet_r", BEX, BODEN, FH, "be1", "netz"),
    hart(schild("Frau Behrens, Bootsverleih", BEX, NULL, BE_F, unten=BODEN, d=0.0)),
    pl("Diese Woche …", 70, 125, "woche", fill=WEISS, size=34),
    *fig("TH", THX, BODEN, FH, [(KOMMT, "ruhig")], bis="th1"),
    *redet("TH_redet", THX, BODEN, FH, "th1", "be1"),
    peep_voll("TH_ruhig", THX, BODEN, FH, "be1", anim="cut"),
    schild("Frau Thiele, Bauamt", THX, KOMMT, TH_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", 1400, 700, 90, BESCHEID, fuell=WEISS), "057brief*", 0.8, -0.10),
    nein(565, BODEN - 70, beim("th1", "Steg"), gr=30),
    pl("Steg", 565, BODEN - 140, beim("th1", "Steg"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "building-store", 1150, BODEN - 2, 150, beim("th1", "Kiosk"), fuell=WEISS),
    pl("Kiosk?", 1150, BODEN - 210, beim("th1", "Kiosk"), fill=WEISS, size=28, anker="m"),
    nein(1150, BODEN - 75, beim("th1", "genehmigen"), gr=30),
    blase("sprech", 820, 230, "th1", 1160, 215, inhalt=["Frau Behrens, Ihr Steg muss bis", "Monatsende weg. Und den Kiosk",
                                                      "genehmigen wir nicht."], textsize=30, figur=THb, bis="be1"),
    blase("sprech", 640, 190, "be1", 700, 225, inhalt=["Der Bescheid muss weg. Und die", "Genehmigung hole ich mir!"],
          textsize=30, figur=BEb, bis="netz"),
])

# B Fall: ein Satz auf der Internetseite ----------------------------------------------------------------------------------
HAX, BBX = 1620, 1060
HAb = ("HA_redet", HAX, BODEN, FH)
BBb = ("BE_redet_r", BBX, BODEN, FH)
HARMS = beim("netz", "Bürgermeister")
folie([("netz", "Fall · Ein Satz auf der Internetseite")], [
    linienzug([(60, BODEN), (1860, BODEN)], "netz", breite=7, farbe=INK),
    pl("Abends", 70, 40, "netz", fill=GELB, size=40),
    karte(110, 150, 780, 430, "netz", fill=WEISS, rund=18, schatten=8),
    karte(110, 150, 780, 70, "netz", fill=GELB, rund=18, schatten=0),
    z("Internetseite der Stadt", 150, 165, beim("netz", "Internetseite"), "Bold", 32, rechts=880),
    z("„Die Boote von Frau Behrens", 150, 330, beim("ha1", "Boote"), "ExtraBold", 36, rechts=880),
    z("sind nicht sicher.“", 150, 385, beim("ha1", "nicht"), "ExtraBold", 36, rechts=880),
    z("Bürgermeister Harms", 150, 470, beim("ha1", "sicher"), size=28, farbe=TEXT, rechts=880),
    *fig("HA", HAX, BODEN, FH, [(HARMS, "ruhig")], bis="ha1"),
    *redet("HA_redet", HAX, BODEN, FH, "ha1", "be2"),
    peep_voll("HA_ruhig", HAX, BODEN, FH, "be2", anim="cut"),
    schild("Bürgermeister Harms", HAX, HARMS, HA_F, unten=BODEN, d=0.0),
    blase("sprech", 640, 170, "ha1", 1270, 250, inhalt=["Die Boote von Frau Behrens", "sind nicht sicher."], textsize=32,
          figur=HAb, bis="be2"),
    *fig("BE", BBX, BODEN, FH, [("ha1", "sorge_r")], bis="be2"),
    *redet("BE_redet_r", BBX, BODEN, FH, "be2", "lindemann"),
    schild("Frau Behrens", BBX, "ha1", BE_F, unten=BODEN),
    blase("sprech", 560, 170, "be2", 1300, 230, inhalt=["Das ist falsch.", "Das soll er lassen!"], textsize=34, figur=BBb),
])

# C Fall: die Elektroboote ------------------------------------------------------------------------------------------------
LIX = 1560
LIb = ("LI_redet", LIX, BODEN, FH)
LIND = beim("lindemann", "Lindemann")
EBOOT = beim("li1", "Elektroboote")
folie([("lindemann", "Fall · Die neuen Elektroboote")], [
    *ufer("lindemann", anim="pop", bis_boote=EBOOT),
    ficon("tabler", "speedboat", 190, BODEN + 8, 170, EBOOT, fuell=BLAU),
    ficon("tabler", "speedboat", 370, BODEN + 10, 150, EBOOT, fuell=GRUEN),
    ficon("tabler", "bolt", 190, BODEN - 70, 60, EBOOT, fuell=GELB),
    ficon("tabler", "bolt", 370, BODEN - 60, 54, EBOOT, fuell=GELB),
    pl("Erlaubnis?", 290, BODEN - 210, beim("li1", "Erlaubnis"), fill=PINK, size=32, anker="m"),
    *fig("BE", BEX, BODEN, FH, [("lindemann", "ruhig_r"), (beim("li1", "Erlaubnis"), "denkt_r")], bis="be3"),
    *redet("BE_redet_r", BEX, BODEN, FH, "be3", "frage"),
    schild("Frau Behrens", BEX, "lindemann", BE_F, unten=BODEN),
    *fig("LI", LIX, BODEN, FH, [(LIND, "ruhig")], bis="li1"),
    *redet("LI_redet", LIX, BODEN, FH, "li1", "be3"),
    peep_voll("LI_ruhig", LIX, BODEN, FH, "be3", anim="cut"),
    schild("Herr Lindemann, Ordnungsamt", LIX, LIND, LI_F, unten=BODEN, d=0.0),
    blase("sprech", 700, 190, "li1", 1180, 230, inhalt=["Für Ihre neuen Elektroboote", "brauchen Sie eine Erlaubnis."],
          textsize=30, figur=LIb, bis="be3"),
    blase("sprech", 640, 190, "be3", 700, 225, inhalt=["Brauche ich nicht. Ich will", "wissen, woran ich bin."],
          textsize=30, figur=BEb),
])


# D Die Frage -------------------------------------------------------------------------------------------------------------
def reihe(cues, labels, y=560, anim="pop", label_cues=None):
    """Die vier Ziele des Falls nebeneinander: Steg-Bescheid, Kiosk, Internetseite, Elektroboote."""
    xs = (250, 640, 1030, 1420)
    label_cues = label_cues or cues
    els = [ficon("tabler", "file-text", xs[0], y, 150, cues[0], fuell=WEISS, anim=anim),
           ficon("tabler", "building-store", xs[1], y, 160, cues[1], fuell=WEISS, anim=anim),
           ficon("tabler", "browser", xs[2], y, 160, cues[2], fuell=GELB, anim=anim),
           ficon("tabler", "speedboat", xs[3], y, 190, cues[3], fuell=BLAU, anim=anim)]
    for x, t, c in zip(xs, labels, label_cues):
        els.append(pl(t, x, y + 40, c, fill=WEISS, size=30, anker="m", anim=anim))
    return els, xs


ZIELE = ("Bescheid aufheben", "Genehmigung erzwingen", "Äußerung stoppen", "Rechtslage klären")
reihe_d, RX = reihe((beim("frage", "Bescheid"), beim("frage", "Genehmigung"), beim("frage", "Äußerung"),
                     beim("frage", "Rechtslage")), ZIELE)
folie([("frage", "Fall · Vier Ziele, vier Klagen"), ("frage2", "Fall · Welche Klage passt wann?")], [
    *reihe_d,
    pl("Vier Ziele, vier Klagen", 840, 70, beim("frage", "Vier"), fill=PINK, size=42, anker="m"),
    pl("Welche passt wann?", 840, 790, "frage2", fill=GELB, size=36, anker="m"),
    pl("Verbot erledigt?", 620, 890, beim("frage3", "erledigt"), fill=WEISS, size=30, anker="m"),
    pl("Satzung?", 1060, 890, beim("frage3", "Satzung"), fill=WEISS, size=30, anker="m"),
    *fig("BE", 1730, BODEN, FH - 60, [("frage", "denkt"), ("frage2", "ruhig")]),
    schild("Frau Behrens", 1730, "frage", BE_F, unten=BODEN),
])

# E Sachverhalt -----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Behrens betreibt einen Bootsverleih am See. Frau Thiele vom Bauamt übergibt ihr einen Bescheid: Der Steg muss "
    "bis Monatsende beseitigt werden, und der beantragte Kiosk wird nicht genehmigt. Bürgermeister Harms schreibt auf der "
    "Internetseite der Stadt, ihre Boote seien nicht sicher. Herr Lindemann vom Ordnungsamt meint, für ihre neuen "
    "Elektroboote brauche sie eine Erlaubnis; sie hält das für falsch.",
    "Abwandlung 1: Herr Lindemann verbietet ihr, am Seefest-Wochenende Boote zu vermieten. Sie klagt, dann ist das "
    "Seefest vorbei.",
    "Abwandlung 2: Die Gemeinde beschließt einen Bebauungsplan: Am Ufer sind keine Kioske zulässig.",
], "Welche Klage ist jeweils statthaft?")

# F Ausgangspunkt: Klagebegehren, Rechtsweg ----------------------------------------------------------------------------------
W88 = "„Das Gericht darf über das Klagebegehren nicht hinausgehen, ist aber an die Fassung der Anträge nicht gebunden.“"
kopf88, y88 = wortlaut_folie("wl88", "Ausgangspunkt: das Klagebegehren", W88, "§ 88 VwGO", [
    ("Klagebegehren", beim("wl88", "Klagebegehren", nr=2)), ("nicht hinausgehen,", beim("wl88", "hinausgehen")),
    ("nicht gebunden.", beim("wl88", "gebunden"))], size=36)
folie([("wl88", f"{SK} › Klagebegehren, § 88 VwGO"), ("rweg", "Vorab › Verwaltungsrechtsweg, § 40 I VwGO")], rechts_frei([
    *kopf88,
    z("Es zählt, was sie wirklich erreichen will", 110, y88 + 40, "ziel", "Bold", 36),
    zit("BVerwG, Beschl. v. 12.5.2020 – 6 B 53.19, Rn. 3: wirkliches Rechtsschutzziel", 110, y88 + 95,
        beim("ziel", "erreichen")),
    z("Vorab: Verwaltungsrechtsweg, § 40 I VwGO", 110, y88 + 190, "rweg", "Bold", 36),
    z("öffentlich-rechtliche Streitigkeit", 150, y88 + 245, beim("rweg", "öffentlich-rechtliche"), size=34),
    z("nichtverfassungsrechtlicher Art", 150, y88 + 297, beim("rweg", "nichtverfassungsrechtlicher"), size=34),
    ok(150, y88 + 385, beim("rweg", "offen", nr=2), gr=20),
    z("hier: offen", 195, y88 + 362, beim("rweg", "offen", nr=2), "Bold", 34),
    ficon("tabler", "target", IX, IU, 130, "ziel", fuell=ROT, bis="rweg"),
    ficon(HC, "classical-building", IX, IU, 140, "rweg", fuell=WEISS),
    *fig("BE", FX, FB, FR, [("wl88", "ruhig"), ("ziel", "denkt")]),
    schild("Frau Behrens", FX, "wl88", BE_F),
]))

# G Wortlaut § 42 I ----------------------------------------------------------------------------------------------------------
W42 = ("„Durch Klage kann die Aufhebung eines Verwaltungsakts (Anfechtungsklage) sowie die Verurteilung zum Erlaß eines "
       "abgelehnten oder unterlassenen Verwaltungsakts (Verpflichtungsklage) begehrt werden.“")
kopf42, y42 = wortlaut_folie("wl42", "§ 42 Abs. 1 VwGO", W42, "§ 42 Abs. 1 VwGO", [
    ("Aufhebung", beim("wl42", "Aufhebung")), ("(Anfechtungsklage)", beim("wl42", "Anfechtungsklage")),
    ("Erlaß", beim("wl42", "Erlass")), ("abgelehnten", beim("wl42", "abgelehnten")),
    ("unterlassenen", beim("wl42", "unterlassenen")), ("(Verpflichtungsklage)", beim("wl42", "Verpflichtungsklage"))], size=38)
folie([("wl42", f"{SK} › § 42 I VwGO")], rechts_frei([
    *kopf42,
    pl("Aufhebung: Anfechtungsklage", 110, y42 + 50, beim("wl42", "Anfechtungsklage"), fill=GRUEN, size=32),
    pl("Erlass: Verpflichtungsklage", 110, y42 + 130, beim("wl42", "Verpflichtungsklage"), fill=BLAU, size=32),
    ficon("tabler", "file-text", IX, IU, 120, "wl42", fuell=WEISS),
    *fig("BE", FX, FB, FR, [("wl42", "ruhig")]),
    schild("Frau Behrens", FX, "wl42", BE_F),
]))

# H Anfechtungsklage: der Steg -------------------------------------------------------------------------------------------------
folie([("anf", f"{SK} › 1. Steg: Anfechtungsklage, § 42 I Alt. 1")], rechts_frei([
    *tafel("anf", "1. Der Steg"),
    z("Anordnung: ein Verwaltungsakt", 110, 190, beim("anf", "Anordnung"), "Bold", 36),
    z("Ziel: ihn loswerden", 110, 245, beim("anf", "loswerden"), size=34),
    blk(110, 320, 1040, 85, GRUEN, beim("anf2", "Anfechtungsklage"), [("Anfechtungsklage, § 42 I Alt. 1 VwGO", "ExtraBold", 36, INK)]),
    z("Erfolg: Das Gericht hebt den Bescheid selbst auf", 110, 455, beim("anf3", "Erfolg"), size=34),
    zit("§ 113 Abs. 1 Satz 1 VwGO", 150, 510, beim("anf3", "Paragraf")),
    z("deshalb: Gestaltungsklage", 110, 585, beim("anf3", "Gestaltungsklage"), "Bold", 36),
    zit("vgl. BVerwG, Urt. v. 28.1.2010 – 8 C 38.09, Rn. 56", 150, 640, beim("anf3", "Gestaltungsklage")),
    ficon("tabler", "file-text", IX, IU, 130, "anf", fuell=WEISS),
    pl("Steg muss weg", IX, 170, "anf", fill=WEISS, size=28, anker="m"),
    nein(IX, IU - 70, beim("anf3", "hebt"), gr=34),
    *fig("BE", FX, FB, FR, [("anf", "ruhig"), ("anf2", "denkt")]),
    schild("Frau Behrens", FX, "anf", BE_F),
]))

# I Verpflichtungsklage: der Kiosk ----------------------------------------------------------------------------------------------
folie([("vpf", f"{SK} › 2. Kiosk: Verpflichtungsklage, § 42 I Alt. 2"),
       ("untaet", f"{SK} › 2. Kiosk › Untätigkeitsklage, § 75 VwGO")], rechts_frei([
    *tafel("vpf", "2. Der Kiosk"),
    z("Ziel: einen Bescheid bekommen, die Genehmigung", 110, 190, beim("vpf", "einen"), "Bold", 34),
    blk(110, 260, 1040, 85, GRUEN, beim("vpf2", "Verpflichtungsklage"), [("Verpflichtungsklage, § 42 I Alt. 2 VwGO", "ExtraBold", 36, INK)]),
    z("nach Ablehnung: Versagungsgegenklage", 110, 375, beim("vpf2", "Versagungsgegenklage"), size=34),
    zit("BVerwG, Urt. v. 21.11.2006 – 1 C 10.06, Rn. 16", 150, 430, beim("vpf2", "genannt")),
    z("ohne zureichenden Grund nicht entschieden:", 110, 505, beim("untaet", "ohne"), size=34),
    z("Untätigkeitsklage, § 75 VwGO", 150, 560, beim("untaet", "Untätigkeitsklage"), "Bold", 36),
    z("in der Regel frühestens 3 Monate nach dem Antrag", 150, 615, beim("untaet", "frühestens"), size=34),
    z("Erfolg: Gericht verpflichtet die Behörde", 110, 710, beim("vpf3", "verpflichtet"), "Bold", 34),
    zit("§ 113 Abs. 5 VwGO (spruchreif: Erteilung, sonst neue Entscheidung)", 150, 765, beim("vpf3", "Paragraf")),
    ficon("tabler", "building-store", IX, IU, 140, "vpf", fuell=WEISS, bis="untaet"),
    ficon("tabler", "calendar", IX, IU, 130, "untaet", fuell=WEISS, bis="vpf3"),
    pl("3 Monate", IX, 190, beim("untaet", "frühestens"), fill=GELB, size=30, anker="m", bis="vpf3"),
    ficon("tabler", "gavel", IX, IU, 140, "vpf3", fuell=HOLZ),
    *fig("TH", FX, FB, FR, [("vpf", "ruhig")]),
    schild("Frau Thiele, Bauamt", FX, "vpf", TH_F),
]))

# J allgemeine Leistungsklage: der Satz im Internet -------------------------------------------------------------------------------
folie([("leist", f"{SK} › 3. Internetseite: allgemeine Leistungsklage")], rechts_frei([
    *tafel("leist", "3. Der Satz im Internet"),
    z("regelt nichts: kein Verwaltungsakt,", 110, 190, beim("leist", "regelt"), "Bold", 36),
    z("schlichtes Verwaltungshandeln", 150, 245, beim("leist", "schlichtes"), size=34),
    blk(110, 320, 1040, 85, GRUEN, beim("leist2", "allgemeine"), [("allgemeine Leistungsklage: Unterlassen", "ExtraBold", 36, INK)]),
    zit("BVerwG, Urt. v. 20.10.2016 – 2 A 2.14, Rn. 12; Urt. v. 27.2.2019 – 6 C 1.18, Rn. 14", 110, 420,
        beim("leist2", "Unterlassen")),
    z("nicht eigens geregelt, aber vorausgesetzt:", 110, 495, beim("leist3", "Eigens"), size=34),
    z("§ 43 Abs. 2 VwGO, § 111 VwGO", 150, 550, beim("leist3", "Paragraf"), "Bold", 34),
    z("Erfolg: rechtswidriger Eingriff in die Berufsfreiheit", 110, 645, beim("leist4", "rechtswidrig"), size=34),
    z("und Wiederholungsgefahr", 150, 700, beim("leist4", "Wiederholung"), "Bold", 34),
    zit("BVerwG, Urt. v. 20.11.2014 – 3 C 27.13, Rn. 11", 150, 755, beim("leist4", "droht")),
    ficon("tabler", "browser", IX, IU, 140, "leist", fuell=GELB),
    pl("„nicht sicher“", IX, 190, "leist", fill=WEISS, size=28, anker="m"),
    *fig("HA", FX, FB, FR, [("leist", "ruhig")]),
    schild("Bürgermeister Harms", FX, "leist", HA_F),
]))

# K Feststellungsklage § 43 I: die Elektroboote ------------------------------------------------------------------------------------
W43 = ("„Durch Klage kann die Feststellung des Bestehens oder Nichtbestehens eines Rechtsverhältnisses oder der Nichtigkeit "
       "eines Verwaltungsakts begehrt werden, wenn der Kläger ein berechtigtes Interesse an der baldigen Feststellung hat "
       "(Feststellungsklage).“")
kopf43, y43 = wortlaut_folie("wl43", "4. Die Elektroboote", W43, "§ 43 Abs. 1 VwGO", [
    ("Rechtsverhältnisses", beim("wl43", "Rechtsverhältnisses")), ("Nichtigkeit", beim("wl43", "Nichtigkeit")),
    ("berechtigtes", beim("wl43", "berechtigtes")), ("baldigen Feststellung", beim("wl43", "baldigen"))], size=32)
folie([("wl43", f"{SK} › 4. Elektroboote: Feststellungsklage, § 43 I")], rechts_frei([
    *kopf43,
    z("Rechtsverhältnis: rechtliche Beziehungen aus einem", 110, y43 + 30, beim("rv", "rechtliche"), "Bold", 34),
    z("konkreten Sachverhalt: muss, darf, braucht nicht", 150, y43 + 85, beim("rv", "muss"), size=34),
    zit("BVerwG, Urt. v. 20.11.2014 – 3 C 26.13, Rn. 12", 150, y43 + 140, beim("rv", "braucht")),
    z("Hier: Erlaubnis für die Elektroboote?", 110, y43 + 215, beim("rv2", "Braucht"), "Bold", 34),
    z("Stadt hat sich festgelegt, Boote sollen bald fahren", 150, y43 + 270, beim("rv2", "Stadt"), size=34),
    ficon("tabler", "speedboat", IX, IU, 200, "wl43", fuell=BLAU),
    pl("Erlaubnis?", IX, 200, beim("rv2", "Braucht"), fill=PINK, size=30, anker="m"),
    *fig("LI", FX, FB, FR, [("wl43", "ruhig"), ("rv2", "denkt")]),
    schild("Herr Lindemann", FX, "wl43", LI_F),
]))

# L Subsidiarität § 43 II 1 ---------------------------------------------------------------------------------------------------------
W432 = ("„Die Feststellung kann nicht begehrt werden, soweit der Kläger seine Rechte durch Gestaltungs- oder Leistungsklage "
        "verfolgen kann oder hätte verfolgen können.“")
kopf432, y432 = wortlaut_folie("wl432", "Aber: Absatz 2", W432, "§ 43 Abs. 2 Satz 1 VwGO", [
    ("Gestaltungs-", beim("wl432", "Gestaltungs-")), ("Leistungsklage", beim("wl432", "Leistungsklage")),
    ("hätte verfolgen können.", beim("wl432", "hätte"))], size=36)
folie([("wl432", f"{SK} › 4. Elektroboote › Subsidiarität, § 43 II")], rechts_frei([
    *kopf432,
    z("Bescheid verbietet die Boote: anfechten", 195, y432 + 52, beim("subs", "Bescheid"), "Bold", 34),
    ok(150, y432 + 175, beim("subs2", "Feststellungsklage"), gr=20),
    z("nur Streit, kein Bescheid: Feststellungsklage", 195, y432 + 152, beim("subs2", "Streit"), "Bold", 34),
    zit("BVerwG, 8 C 38.09, Rn. 56 (Subsidiarität); vgl. 3 C 26.13, Rn. 23", 195, y432 + 210,
        beim("subs2", "Feststellungsklage")),
    ficon("tabler", "file-text", IX, IU, 120, "subs", fuell=WEISS, bis="subs2"),
    ficon("tabler", "speedboat", IX, IU, 200, "subs2", fuell=BLAU),
    *fig("BE", FX, FB, FR, [("wl432", "ruhig"), ("subs2", "froh")]),
    schild("Frau Behrens", FX, "wl432", BE_F),
]))

# M Ergebnis Ausgangsfall ---------------------------------------------------------------------------------------------------------
reihe_m, _ = reihe(("erg",) * 4, ZIELE, anim="cut")
KL = ("Anfechtung", "Verpflichtung", "Leistung", "Feststellung")
els_m = [*reihe_m, pl("Vier Ziele, vier Klagen", 840, 70, "erg", fill=PINK, size=42, anker="m", anim="cut")]
for x, k, c in zip(RX, KL, ("e1", "e2", "e3", "e4")):
    els_m += [ok(x, 690, c, gr=30), pl(k, x, 760, c, fill=GRUEN, size=32, anker="m")]
folie([("erg", "Ergebnis Ausgangsfall")], [
    *els_m,
    *fig("BE", 1730, BODEN, FH - 60, [("erg", "ruhig"), ("e4", "froh")]),
    schild("Frau Behrens", 1730, "erg", BE_F, unten=BODEN),
])

# N Abwandlung 1: das Seefest -----------------------------------------------------------------------------------------------------
LNb = ("LI_redet", LIX, BODEN, FH)
SEEFEST = beim("seefest", "Seefest")
VORBEI = "vorbei"
folie([("seefest", "Abwandlung 1 · Das Seefest-Verbot")], [
    *ufer("seefest", anim="pop"),
    pl("Erste Abwandlung", 70, 40, "seefest", fill=GELB, size=40),
    ficon("tabler", "flag", 1010, BODEN - 2, 120, SEEFEST, fuell=ROT, bis=VORBEI),
    ficon("tabler", "flag", 1180, BODEN - 2, 110, SEEFEST, fuell=GELB, bis=VORBEI),
    ficon(HC, "confetti-ball", 1180, 560, 120, SEEFEST, fuell=PINK, bis=VORBEI),
    pl("Seefest", 1180, 600, SEEFEST, fill=PINK, size=32, anker="m", bis=VORBEI),
    *fig("BE", BEX, BODEN, FH, [("seefest", "ruhig_r"), ("li2", "sorge_r"), ("klagt", "denkt_r")]),
    schild("Frau Behrens", BEX, "seefest", BE_F, unten=BODEN),
    *fig("LI", LIX, BODEN, FH, [(beim("seefest", "Lindemann"), "ruhig")], bis="li2"),
    *redet("LI_redet", LIX, BODEN, FH, "li2", "klagt"),
    peep_voll("LI_ruhig", LIX, BODEN, FH, "klagt", anim="cut"),
    schild("Herr Lindemann", LIX, beim("seefest", "Lindemann"), LI_F, unten=BODEN, d=0.0),
    blase("sprech", 700, 170, "li2", 1160, 230, inhalt=["Am Seefest-Wochenende", "vermieten Sie keine Boote!"],
          textsize=32, figur=LNb, bis="klagt"),
    ficon("tabler", "gavel", 520, 560, 120, "klagt", fuell=HOLZ),
    pl("Frau Behrens klagt", 520, 600, "klagt", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "calendar-x", 1180, 560, 130, VORBEI, fuell=WEISS),
    pl("Seefest vorbei", 1180, 600, VORBEI, fill=WEISS, size=30, anker="m"),
    pl("Verbot erledigt", 1180, 665, beim(VORBEI, "erledigt"), fill=ROT, size=30, anker="m"),
])

# O Wortlaut § 113 I 4: Fortsetzungsfeststellungsklage -------------------------------------------------------------------------------
W113 = ("„Hat sich der Verwaltungsakt vorher durch Zurücknahme oder anders erledigt, so spricht das Gericht auf Antrag durch "
        "Urteil aus, daß der Verwaltungsakt rechtswidrig gewesen ist, wenn der Kläger ein berechtigtes Interesse an dieser "
        "Feststellung hat.“")
kopf113, y113 = wortlaut_folie("wl113", "§ 113 Abs. 1 Satz 4 VwGO", W113, "§ 113 Abs. 1 Satz 4 VwGO", [
    ("erledigt,", beim("wl113", "erledigt")), ("rechtswidrig", beim("wl113", "rechtswidrig")),
    ("berechtigtes", beim("wl113", "berechtigtes"))], size=34)
folie([("wl113", "Abwandlung 1 › Fortsetzungsfeststellungsklage, § 113 I 4")], rechts_frei([
    *kopf113,
    blk(110, y113 + 30, 1040, 85, GRUEN, beim("ffk", "Fortsetzungsfeststellungsklage"),
        [("Fortsetzungsfeststellungsklage", "ExtraBold", 38, INK)]),
    z("berechtigtes Interesse: Wiederholungsgefahr", 110, y113 + 150, beim("ffk2", "Wiederholungsgefahr"), "Bold", 34),
    z("Seefest jedes Jahr, dasselbe Verbot droht erneut", 150, y113 + 205, beim("ffk2", "Seefest"), size=34),
    zit("BVerwG, Urt. v. 26.4.2023 – 6 C 8.21, Rn. 20; Urt. v. 4.12.2014 – 4 C 33.13, Rn. 13", 150, y113 + 260,
        beim("ffk2", "droht")),
    ficon("tabler", "calendar-x", IX, IU, 130, "wl113", fuell=WEISS, bis="ffk2"),
    ficon("tabler", "flag", IX, IU, 120, "ffk2", fuell=ROT),
    pl("jedes Jahr", IX, 190, beim("ffk2", "jedes"), fill=GELB, size=30, anker="m"),
    *fig("BE", FX, FB, FR, [("wl113", "denkt"), ("ffk", "ruhig")]),
    schild("Frau Behrens", FX, "wl113", BE_F),
]))

# P Abwandlung 2: Bebauungsplan, Normenkontrolle --------------------------------------------------------------------------------------
folie([("bplan", "Abwandlung 2 · Bebauungsplan"), ("nk", "Abwandlung 2 › Normenkontrolle, § 47 VwGO")], rechts_frei([
    *tafel("bplan", "Zweite Abwandlung: Bebauungsplan"),
    z("Am Ufer sind keine Kioske zulässig", 110, 175, beim("bplan", "Ufer"), size=34),
    z("Bebauungsplan: Satzung nach dem BauGB", 110, 235, beim("nk", "Satzung"), "Bold", 34),
    zit("§ 10 Abs. 1 BauGB", 150, 287, beim("nk", "Satzung")),
    blk(110, 330, 1040, 80, GRUEN, beim("nk", "Normenkontrolle"), [("Normenkontrolle, § 47 Abs. 1 Nr. 1 VwGO", "ExtraBold", 34, INK)]),
    z("Antrag beim Oberverwaltungsgericht, keine Klage", 110, 435, "nk2", "Bold", 34),
    zit("in manchen Ländern: Verwaltungsgerichtshof (§ 184 VwGO)", 150, 487, beim("nk2", "Oberverwaltungsgericht")),
    z("antragsbefugt: mögliche Verletzung eigener Rechte", 110, 545, beim("nk3", "geltend"), size=34),
    z("Frist: 1 Jahr nach Bekanntmachung", 110, 597, beim("nk3", "Jahres"), size=34),
    zit("§ 47 Abs. 2 Satz 1 VwGO", 150, 649, beim("nk3", "Bekanntmachung")),
    z("andere Vorschriften unter dem Landesgesetz:", 110, 705, "nk4", size=34),
    z("nur, wenn das Landesrecht es vorsieht, Nr. 2", 150, 757, beim("nk4", "Landesrecht"), size=34),
    z("unwirksam: gilt für alle, § 47 Abs. 5 Satz 2", 110, 825, beim("nk5", "unwirksam"), "Bold", 34),
    ficon("ph", "map-trifold", IX, IU, 140, "bplan", fuell=GELB, bis="nk2"),
    ficon("tabler", "building-store", IX - 150, 260, 120, beim("bplan", "Kioske"), fuell=WEISS, bis="nk2"),
    bis_(nein(IX - 150, 200, beim("bplan", "Kioske"), gr=30), "nk2"),
    ficon(HC, "classical-building", IX, IU, 140, "nk2", fuell=WEISS, bis=beim("nk3", "Jahres")),
    pl("OVG", IX, 180, "nk2", fill=WEISS, size=30, anker="m", bis=beim("nk3", "Jahres")),
    ficon("tabler", "calendar", IX, IU, 130, beim("nk3", "Jahres"), fuell=WEISS, bis="nk5"),
    pl("1 Jahr", IX, 190, beim("nk3", "Jahres"), fill=GELB, size=30, anker="m", bis="nk5"),
    ficon("tabler", "users", IX, IU, 150, "nk5", fuell=WEISS),
    *fig("BE", FX, FB, FR, [("bplan", "sorge"), ("nk", "denkt")]),
    schild("Frau Behrens", FX, "bplan", BE_F),
]))

# Q Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Statthafte Klageart")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("statthafte Klageart: in der Zulässigkeit,", 200, 200, beim("tipp", "statthafte"), "Bold", 36),
    z("direkt nach dem Rechtsweg", 200, 255, beim("tipp", "direkt"), "Bold", 36),
    z("mit dem Begehren beginnen,", 200, 350, "tipp1", size=34),
    z("schiefen Antrag auslegen, § 88 VwGO", 200, 405, beim("tipp1", "schiefen"), size=34),
    z("erst ordnen, dann weiter prüfen:", 200, 500, "tipp2", size=34),
    z("Klagebefugnis, Vorverfahren und Frist", 200, 555, beim("tipp2", "Klagebefugnis"), "Bold", 34),
    z("hängen von der Klageart ab", 200, 610, beim("tipp2", "hängen"), "Bold", 34),
    zit("vgl. BVerwG, 8 C 38.09, Rn. 56; 6 C 1.18, Rn. 14 (keine Klagefrist)", 200, 665, beim("tipp2", "Klageart")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# R Klausurschema: der Entscheidungsbaum -------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema · Entscheidungsbaum")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Welche Klage passt?"), 110, 85, "sch", 46),
    z("Entscheidungsbaum: Klausurkonvention, keine Norm", 1050, 100, beim("sch", "Klausurkonvention"), size=28,
      farbe=TEXT, rechts=1820),
    z("1. Begehren, § 88 VwGO", K1, 175, "q0", "Bold", 38, rechts=1820),
    z("2. Verwaltungsakt?", K1, 245, "q1", "Bold", 38, rechts=1820),
    z("Aufhebung: Anfechtungsklage, § 42 I Alt. 1", K2, 305, "q2", size=SZ, rechts=1820),
    z("Erlass: Verpflichtungsklage, § 42 I Alt. 2", K2, 360, "q3", size=SZ, rechts=1820),
    z("schon erledigt: Fortsetzungsfeststellungsklage, § 113 I 4", K2, 415, "q4", size=SZ, rechts=1820),
    z("3. kein Verwaltungsakt:", K1, 490, "q5", "Bold", 38, rechts=1820),
    z("Tun oder Unterlassen: allgemeine Leistungsklage", K2, 550, "q6", size=SZ, rechts=1820),
    z("Klärung eines Rechtsverhältnisses: Feststellungsklage, § 43 (nachrangig)", K2, 605, "q7", size=SZ, rechts=1820),
    z("4. Bebauungsplan oder, je nach Land, andere Satzung:", K1, 680, "q8", "Bold", 38, rechts=1820),
    z("Normenkontrolle, § 47 VwGO", K2, 740, beim("q8", "Normenkontrolle"), size=SZ, rechts=1820),
])

# S Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst das ", 0), ("Ziel", "a"), (", dann die ", 0), ("Klage.", "b")]],
                750, 310, 50, "merke", {"a": beim("merke", "Ziel"), "b": beim("merke", "Klage")}),
    *markertext([[("Gibt es einen ", 0), ("Verwaltungsakt:", "c")], [("Anfechtung, Verpflichtung oder", 0)],
                 [("Fortsetzungsfeststellung.", 0)], [("Sonst: Leistung, Feststellung", 0)],
                 [("oder ", 0), ("Normenkontrolle.", "d")]],
                750, 440, 44, "m2", {"c": beim("m2", "Verwaltungsakt"), "d": beim("m2", "Normenkontrolle")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
