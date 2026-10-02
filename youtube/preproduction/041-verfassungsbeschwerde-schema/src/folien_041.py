"""Folge 041 · Verfassungsbeschwerde Schema: Zulässigkeit und Begründetheit – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Bundesgesetz erlaubt die Untersagung der Bienenhaltung in Wohngebieten), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Garten am Stadtrand (Frau Wendt, Herr Hübner), B Durch alle Instanzen (Richterin Reuter), C Die Frage, D Sachverhalt,
E I. Zuständigkeit, F1 II. Beschwerdeberechtigung, F2 III. Prozessfähigkeit, G IV. Beschwerdegegenstand,
H V. Beschwerdebefugnis, I Gegenfall Herr Seifert, J VI. Rechtswegerschöpfung/Subsidiarität, K1/K2 VII. Form und Frist,
L1/L2 B. Begründetheit, M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Einwurf, wenn das Urteil im Briefkasten von Frau Wendt landet)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_041/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_041/" in n:
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


def wfragen(cue_wer, wer, cue_2, t2, cue_3, t3, y=180, labels=("Wer?", "Was?", "Gegen wen?")):
    """Drei Zeilen „Wer? / Was? / Gegen wen?“ in Sprechreihenfolge (Klausurkonvention)."""
    els = []
    for i, (c, lab, txt) in enumerate(((cue_wer, labels[0], wer), (cue_2, labels[1], t2), (cue_3, labels[2], t3))):
        yy = y + i * 52
        els.append(z(lab, 110, yy, c, "ExtraBold", 32))
        els.append(z(txt, 320, yy, c, size=32))
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WE_F, HU_F, RE_F, SE_F = GRUEN, BLAU, GRAU, ORANGE   # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270


def beute(x, cue, h=180):
    """Bienenbeute als Baustein: Kasten (Karte) mit Zargenlinie und Flugloch."""
    return [karte(x, BODEN - h, 130, h, cue, fill=HOLZ, rund=10, schatten=5, rand=5),
            linienzug([(x + 4, BODEN - h * 0.5), (x + 126, BODEN - h * 0.5)], cue, breite=5, farbe=INK),
            linienzug([(x + 45, BODEN - 22), (x + 85, BODEN - 22)], cue, breite=7, farbe=INK)]


# A Fall: Garten am Stadtrand, der Bescheid ------------------------------------------------------------------------------
WEX, HUX = 930, 1560
WEb = ("WE_redet_r", WEX, BODEN, FH)
HUb = ("HU_redet", HUX, BODEN, FH)
GES = beim("gesetz", "Bundesgesetz")
folie([(NULL, "Fall · Bienen im Garten"), ("huebner", "Fall · Der Bescheid")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Am Stadtrand", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "home", 220, BODEN - 2, 280, NULL, fuell=WEISS, anim="cut"),
    *[hart(e) for e in beute(430, NULL)], *[hart(e) for e in beute(600, NULL)],
    ficon(HC, "honeybee", 470, 640, 70, NULL, fuell=GELB, anim="cut"),
    ficon(HC, "honeybee", 640, 600, 60, NULL, fuell=GELB, anim="cut"),
    ficon(HC, "honeybee", 560, 540, 55, NULL, fuell=GELB, anim="cut"),
    ficon(HC, "sunflower", 790, BODEN - 2, 110, NULL, fuell=GELB, anim="cut"),
    *fig("WE", WEX, BODEN, FH, [(NULL, "ruhig_r"), ("gesetz", "sorge_r"), (beim("hu1", "Bescheid"), "denkt_r")], bis="we1", erst="cut"),
    *redet("WE_redet_r", WEX, BODEN, FH, "we1", "klage"),
    hart(schild("Frau Wendt, Hobbyimkerin", WEX, NULL, WE_F, unten=BODEN, d=0.0)),
    pl("2 Bienenvölker, seit 8 Jahren", 560, 330, beim("fall", "zwei"), fill=WEISS, size=30, anker="m", bis="gesetz"),
    ficon("tabler", "file-text", 640, 250, 110, GES, fuell=WEISS, bis="huebner"),
    pl("Neues Bundesgesetz", 640, 270, GES, fill=GELB, size=30, anker="m", bis="huebner"),
    pl("Bienenhaltung in Wohngebieten untersagen", 1240, 330, beim("gesetz", "untersagen"), fill=WEISS, size=30, anker="m",
       bis="huebner"),
    *fig("HU", HUX, BODEN, FH, [(beim("huebner", "Herr"), "ruhig")], bis="hu1"),
    *redet("HU_redet", HUX, BODEN, FH, "hu1", "we1"),
    peep_voll("HU_ruhig", HUX, BODEN, FH, "we1", anim="cut"),
    schild("Herr Hübner, Ordnungsamt", HUX, beim("huebner", "Herr"), HU_F, unten=BODEN),
    ficon("tabler", "file-text", 1425, 600, 90, beim("huebner", "Bescheid"), fuell=WEISS),
    pl("Bescheid", 1425, 440, beim("huebner", "Bescheid"), fill=ROT, size=28, anker="m"),
    blase("sprech", 760, 190, "hu1", 1400, 210, inhalt=["Ihre Bienen müssen bis Ende Mai weg.", "So steht es im Bescheid."],
          textsize=30, figur=HUb, bis="we1"),
    blase("sprech", 640, 190, "we1", 760, 210, inhalt=["Meine Bienen stören niemanden.", "Dagegen klage ich."],
          textsize=30, figur=WEb),
])

# B Fall: durch alle Instanzen -------------------------------------------------------------------------------------------
WBX, REX = 300, 1620
WBb = ("WE_redet_r", WBX, BODEN, FH)
REb = ("RE_redet", REX, BODEN, FH)
GX = (800, 1040, 1290)
folie([("klage", "Fall · Durch alle Instanzen"), ("zustell", "Fall · Das Urteil wird zugestellt")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Durch alle Instanzen", 70, 40, "klage", fill=GELB, size=40),
    *fig("WE", WBX, BODEN, FH, [("klage", "entschl_r"), (beim("klage", "Verwaltungsgericht"), "sorge_r"), ("zustell", "denkt_r")], bis="we2"),
    *redet("WE_redet_r", WBX, BODEN, FH, "we2", "frage"),
    schild("Frau Wendt", WBX, "klage", WE_F, unten=BODEN),
    ficon("tabler", "building-bank", GX[0], BODEN - 2, 160, beim("klage", "Verwaltungsgericht"), fuell=WEISS),
    pl("VG", GX[0], BODEN + 22, beim("klage", "Verwaltungsgericht"), fill=WEISS, size=28, anker="m"),
    nein(GX[0], 650, beim("klage", "Verwaltungsgericht"), gr=26, d=0.35),
    ficon("tabler", "building-bank", GX[1], BODEN - 2, 190, beim("ovg", "Oberverwaltungsgericht"), fuell=WEISS),
    pl("OVG", GX[1], BODEN + 22, beim("ovg", "Oberverwaltungsgericht"), fill=WEISS, size=28, anker="m"),
    nein(GX[1], 620, beim("ovg", "Oberverwaltungsgericht"), gr=26, d=0.35),
    ficon("tabler", "building-bank", GX[2], BODEN - 2, 220, beim("bverwg", "Bundesverwaltungsgericht"), fuell=GELB),
    pl("BVerwG", GX[2], BODEN + 22, beim("bverwg", "Bundesverwaltungsgericht"), fill=WEISS, size=28, anker="m"),
    nein(GX[2], 590, beim("re1", "zurückgewiesen"), gr=26),
    *fig("RE", REX, BODEN, FH, [(beim("reuter", "Richterin"), "ruhig")], bis="re1"),
    *redet("RE_redet", REX, BODEN, FH, "re1", "zustell"),
    peep_voll("RE_ruhig", REX, BODEN, FH, "zustell", anim="cut"),
    schild("Richterin Reuter, BVerwG", REX, beim("reuter", "Richterin"), RE_F, unten=BODEN),
    blase("sprech", 640, 190, "re1", 1330, 220, inhalt=["Die Revision der Klägerin", "wird zurückgewiesen."],
          textsize=32, figur=REb, bis="zustell"),
    ficon("tabler", "mailbox", 530, BODEN - 2, 130, "zustell", fuell=BLAU),
    szene(ficon("tabler", "mail", 530, 690, 90, beim("zustell", "zugestellt"), fuell=WEISS), "041einwurf*", 1.0, 0.0),
    pl("vollständiges Urteil", 530, 540, beim("zustell", "vollständige"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 660, 190, "we2", 760, 210, inhalt=["Das verletzt meine Freiheit.", "Jetzt gehe ich nach Karlsruhe."],
          textsize=30, figur=WBb),
    ficon(HC, "classical-building", 1040, 430, 130, beim("we2", "Karlsruhe"), fuell=WEISS),
    pl("Karlsruhe", 1040, 450, beim("we2", "Karlsruhe"), fill=PINK, size=28, anker="m"),
])

# C Die Frage --------------------------------------------------------------------------------------------------------------
WCX = 1380
folie([("frage", "Fall · Hat die Verfassungsbeschwerde Erfolg?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "frage", breite=7, farbe=INK),
    ficon(HC, "classical-building", 560, BODEN - 2, 360, "frage", fuell=WEISS, anim="cut"),
    pl("Bundesverfassungsgericht", 560, BODEN + 22, "frage", fill=WEISS, size=28, anker="m", anim="cut"),
    *fig("WE", WCX, BODEN, FH, [("frage", "entschl"), ("frage2", "ruhig")], erst="cut"),
    schild("Frau Wendt", WCX, "frage", WE_F, unten=BODEN, d=0.0),
    pl("Hat ihre Verfassungsbeschwerde Erfolg?", 960, 60, beim("frage", "Hat"), fill=PINK, size=40, anker="m"),
    pl("A. Zulässigkeit", 960, 200, beim("frage2", "Zulässigkeit"), fill=GELB, size=36, anker="m"),
    pl("B. Begründetheit", 960, 290, beim("frage2", "Begründetheit"), fill=GRUEN, size=36, anker="m"),
])

# D Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Ein neues Bundesgesetz erlaubt den Behörden, die Bienenhaltung in Wohngebieten zu untersagen. Frau Wendt (32) hält "
    "seit acht Jahren zwei Bienenvölker in ihrem Garten am Stadtrand. Herr Hübner vom Ordnungsamt untersagt ihr das per "
    "Bescheid: Die Bienen müssen bis Ende Mai weg. Frau Wendt klagt und verliert vor dem Verwaltungsgericht und dem "
    "Oberverwaltungsgericht; das Bundesverwaltungsgericht weist ihre Revision zurück. Das vollständige Urteil wird ihr "
    "zugestellt. Sie sieht sich in ihrer Freiheit verletzt und will nach Karlsruhe.",
    "Herr Seifert hält im Nachbarort Bienen und hat noch keinen Bescheid. Er will gleich gegen das Gesetz selbst vorgehen.",
], "Hat die Verfassungsbeschwerde von Frau Wendt Erfolg?")

# E I. Zuständigkeit -----------------------------------------------------------------------------------------------------------
W4A = ("„(1) Das Bundesverfassungsgericht entscheidet: … 4a. über Verfassungsbeschwerden, die von jedermann mit der "
       "Behauptung erhoben werden können, durch die öffentliche Gewalt in einem seiner Grundrechte oder in einem seiner in "
       "Artikel 20 Absatz 4, 33, 38, 101, 103 und 104 enthaltenen Rechte verletzt zu sein; …“")
w4a, w4a_y = wortlaut(80, 180, 1100, W4A, "Art. 94 Abs. 1 Nr. 4a GG", "zust", marken=[
    ("Verfassungsbeschwerden,", beim("zust", "Verfassungsbeschwerden")),
    ("Bundesverfassungsgericht entscheidet", beim("zust", "Bundesverfassungsgericht"))], size=30)
folie([("zust", "A. Zulässigkeit › I. Zuständigkeit, Art. 94 I Nr. 4a GG"),
       ("p13", "A. Zulässigkeit › I. Zuständigkeit, § 13 Nr. 8a BVerfGG")], rechts_frei([
    *tafel("zust", "I. Zuständigkeit"),
    *w4a,
    z("in Art. 94 GG seit 28.12.2024 (BGBl. 2024 I Nr. 439)", 110, w4a_y + 30, beim("art93", "seit"), "Bold", 34),
    z("vorher: Art. 93 I Nr. 4a GG a. F.", 150, w4a_y + 85, beim("art93", "vorher"), size=34, farbe=TEXT),
    z("dazu: § 13 Nr. 8a BVerfGG", 110, w4a_y + 160, beim("p13", "Paragraf"), "Bold", 36),
    ficon(HC, "classical-building", IX, IU, 200, "zust", fuell=WEISS),
    ficon("tabler", "calendar", IX + 170, IU, 90, beim("art93", "seit"), fuell=WEISS),
    *fig("WE", FX, FB, FR, [("zust", "ruhig")]),
    schild("Frau Wendt", FX, "zust", WE_F),
]))

# F1 II. Beschwerdeberechtigung --------------------------------------------------------------------------------------------------
W901 = ("„(1) Jedermann kann mit der Behauptung, durch die öffentliche Gewalt in einem seiner Grundrechte oder in einem "
        "seiner in Artikel 20 Abs. 4, Artikel 33, 38, 101, 103 und 104 des Grundgesetzes enthaltenen Rechte verletzt zu "
        "sein, die Verfassungsbeschwerde zum Bundesverfassungsgericht erheben.“")
w901, w901_y = wortlaut(80, 180, 1100, W901, "§ 90 Abs. 1 BVerfGG", "berecht", marken=[
    ("Jedermann", beim("berecht", "jedermann")), ("einem seiner Grundrechte", beim("traeger", "Grundrechts"))], size=30)
folie([("berecht", "A. Zulässigkeit › II. Beschwerdeberechtigung, § 90 I BVerfGG"),
       ("art193", "A. Zulässigkeit › II. Beschwerdeberechtigung › Art. 19 III GG")], rechts_frei([
    *tafel("berecht", "II. Beschwerdeberechtigung"),
    *w901,
    z("jedermann: wer Träger des gerügten Grundrechts sein kann", 110, w901_y + 30, beim("traeger", "Träger"), "Bold", 32),
    ok(140, w901_y + 108, beim("traeger", "Frau"), gr=22),
    z("Frau Wendt: als Mensch ohne Weiteres", 185, w901_y + 85, beim("traeger", "Frau"), size=32),
    z("juristische Personen: Art. 19 III GG,", 110, w901_y + 165, "art193", "Bold", 32),
    z("soweit das Grundrecht seinem Wesen nach auf sie passt", 150, w901_y + 215, beim("art193", "soweit"), size=32),
    zit("Art. 19 Abs. 3 GG; vgl. BVerfGE 142, 74 Rn. 59", 150, w901_y + 265, beim("art193", "passt")),
    ficon("tabler", "user", IX, IU, 130, "berecht", fuell=WEISS, bis="art193"),
    ficon("tabler", "building", IX, IU, 130, "art193", fuell=WEISS),
    *fig("WE", FX, FB, FR, [("berecht", "ruhig")]),
    schild("Frau Wendt", FX, "berecht", WE_F),
]))

# F2 III. Prozessfähigkeit -----------------------------------------------------------------------------------------------------
folie([("prozess", "A. Zulässigkeit › III. Prozessfähigkeit")], rechts_frei([
    *tafel("prozess", "III. Prozessfähigkeit"),
    z("Fähigkeit, Verfahrenshandlungen selbst vorzunehmen", 110, 190, beim("prozess", "Fähigkeit"), "Bold", 36),
    zit("BVerfG, Beschl. v. 8.8.2021 – 2 BvR 2000/20, Rn. 20", 150, 245, beim("prozess", "vorzunehmen")),
    ok(140, 345, beim("prozess", "volljährigen"), gr=22),
    z("Frau Wendt: volljährig, kein Problem", 185, 320, beim("prozess", "volljährigen"), size=34),
    ficon("tabler", "id", IX, IU, 150, beim("prozess", "volljährigen"), fuell=WEISS),
    pl("32 Jahre", IX, IU + 20, beim("prozess", "volljährigen"), fill=GELB, size=28, anker="m"),
    *fig("WE", FX, FB, FR, [("prozess", "ruhig")]),
    schild("Frau Wendt", FX, "prozess", WE_F),
]))

# G IV. Beschwerdegegenstand --------------------------------------------------------------------------------------------------
folie([("gegenst", "A. Zulässigkeit › IV. Beschwerdegegenstand")], rechts_frei([
    *tafel("gegenst", "IV. Beschwerdegegenstand"),
    z("Akt der öffentlichen Gewalt", 110, 190, beim("gegenst", "Akt"), "Bold", 38),
    pl("Gesetz", 150, 260, beim("gegenst", "Gesetz"), fill=WEISS, size=32),
    pl("Bescheid", 380, 260, beim("gegenst", "Bescheid"), fill=WEISS, size=32),
    pl("Urteil", 640, 260, beim("gegenst", "Urteil"), fill=WEISS, size=32),
    z("hier: das letzte Urteil (BVerwG)", 110, 380, beim("hier", "letzte"), "Bold", 36),
    z("dazu: die Urteile davor und der Bescheid", 150, 440, beim("hier", "dazu"), size=34),
    z("mittelbar: das Gesetz, auf dem alles beruht", 110, 530, "mittelbar", "Bold", 36),
    zit("vgl. BVerfGE 150, 244 Rn. 30; § 95 BVerfGG", 150, 590, beim("mittelbar", "beruht")),
    ficon("tabler", "building-bank", IX, IU, 150, beim("hier", "letzte"), fuell=GELB, bis="mittelbar"),
    ficon("tabler", "book", IX, IU, 130, "mittelbar", fuell=WEISS),
    *fig("WE", FX, FB, FR, [("gegenst", "ruhig"), ("hier", "entschl")]),
    schild("Frau Wendt", FX, "gegenst", WE_F),
]))

# H V. Beschwerdebefugnis ------------------------------------------------------------------------------------------------------
folie([("befugt", "A. Zulässigkeit › V. Beschwerdebefugnis"), ("art2", "A. Zulässigkeit › V. Beschwerdebefugnis › Art. 2 I GG"),
       ("sgu", "A. Zulässigkeit › V. Beschwerdebefugnis › selbst, gegenwärtig, unmittelbar")], rechts_frei([
    *tafel("befugt", "V. Beschwerdebefugnis"),
    z("Behauptung einer Grundrechtsverletzung", 110, 190, beim("befugt", "behaupten"), "Bold", 36),
    z("Verletzung muss möglich sein", 150, 245, beim("befugt", "möglich"), size=34),
    z("Hobby: allgemeine Handlungsfreiheit, Art. 2 I GG", 110, 325, beim("art2", "Hobby"), "Bold", 34),
    z("geschützt: jede Form menschlichen Handelns", 150, 380, beim("art2", "Geschützt"), size=34),
    zit("BVerfGE 159, 223 Rn. 112", 150, 432, beim("art2", "Handelns")),
    ok(140, 515, beim("moeglich", "möglich"), gr=22),
    z("Verletzung jedenfalls möglich", 185, 490, beim("moeglich", "möglich"), "Bold", 34),
    zit("vgl. BVerfGE 150, 244 Rn. 31", 185, 542, beim("moeglich", "möglich")),
    z("selbst, gegenwärtig und unmittelbar betroffen", 110, 620, beim("sgu", "selbst"), "Bold", 34),
    ok(140, 700, beim("adressat", "unproblematisch"), gr=22),
    z("Urteil richtet sich gegen sie, belastet sie jetzt", 185, 675, "adressat", size=34),
    zit("vgl. BVerfGE 142, 74 Rn. 63", 185, 727, beim("adressat", "unproblematisch")),
    ficon(HC, "honeybee", IX, IU, 140, beim("art2", "Hobby"), fuell=GELB),
    *fig("WE", FX, FB, FR, [("befugt", "denkt"), ("moeglich", "entschl")]),
    schild("Frau Wendt", FX, "befugt", WE_F),
]))

# I Gegenfall: Herr Seifert will direkt gegen das Gesetz -------------------------------------------------------------------------
SEb = ("SE_redet", FX, FB, FR)
folie([("seifert", "Gegenfall · Herr Seifert"), ("direkt", "Gegenfall · Gesetz direkt angreifen?"),
       ("unmitt", "Gegenfall · unmittelbar betroffen?")], rechts_frei([
    *tafel("seifert", "Gegenfall: Herr Seifert"),
    z("Bienen im Nachbarort, noch kein Bescheid", 110, 190, beim("seifert", "Er"), "Bold", 34),
    z("will gleich gegen das Gesetz nach Karlsruhe", 150, 245, "se1", size=34),
    z("Gesetz direkt: nur ausnahmsweise", 110, 330, "direkt", "Bold", 36),
    z("unmittelbar betroffen grundsätzlich nur, wenn", 110, 415, "unmitt", "Bold", 34),
    z("das Gesetz ohne weiteren Vollzugsakt wirkt", 150, 470, beim("unmitt", "ohne"), size=34),
    zit("BVerfGE 115, 118 Rn. 78; BVerfG-Merkblatt III.2.c", 150, 522, beim("unmitt", "wirkt")),
    z("hier nötig: erst ein Bescheid der Behörde", 110, 605, "vollzug", "Bold", 34),
    z("dagegen zunächst vor die Fachgerichte", 150, 660, beim("vollzug", "Gegen"), size=34),
    ficon("tabler", "file-text", IX, IU, 110, beim("vollzug", "Bescheid"), fuell=WEISS),
    *fig("SE", FX, FB, FR, [(beim("seifert", "Herrn"), "ruhig")], bis="se1"),
    *redet("SE_redet", FX, FB, FR, "se1", "direkt"),
    peep_voll("SE_denkt", FX, FB, FR, "direkt", anim="cut"),
    schild("Herr Seifert, Hobbyimker", FX, beim("seifert", "Herrn"), SE_F),
    blase("sprech", 640, 200, "se1", 1540, 240, inhalt=["Ich ziehe gleich gegen das", "Gesetz nach Karlsruhe."],
          textsize=30, figur=SEb, bis="direkt"),
]))

# J VI. Rechtswegerschöpfung und Subsidiarität ---------------------------------------------------------------------------------
W902 = ("„(2) Ist gegen die Verletzung der Rechtsweg zulässig, so kann die Verfassungsbeschwerde erst nach Erschöpfung "
        "des Rechtswegs erhoben werden. …“")
w902, w902_y = wortlaut(80, 180, 1100, W902, "§ 90 Abs. 2 Satz 1 BVerfGG", "rechtsweg", marken=[
    ("Rechtsweg zulässig", beim("rechtsweg", "Rechtsweg", nr=2)),
    ("Erschöpfung", beim("rechtsweg", "Erschöpfung"))], size=32)
folie([("rechtsweg", "A. Zulässigkeit › VI. Rechtswegerschöpfung, § 90 II 1 BVerfGG"),
       ("subsid", "A. Zulässigkeit › VI. Subsidiarität")], rechts_frei([
    *tafel("rechtsweg", "VI. Rechtsweg und Subsidiarität"),
    *w902,
    ok(140, w902_y + 55, beim("erschoepft", "Instanzen"), gr=22),
    z("Frau Wendt: VG, OVG, BVerwG, alle Instanzen", 185, w902_y + 30, beim("erschoepft", "Instanzen"), size=34),
    z("Subsidiarität: alle prozessualen Möglichkeiten", 110, w902_y + 120, "subsid", "Bold", 34),
    z("nutzen, um die Verletzung schon vor den", 150, w902_y + 175, beim("subsid", "Möglichkeiten"), size=34),
    z("Fachgerichten zu verhindern", 150, w902_y + 225, beim("subsid", "Möglichkeiten"), size=34),
    z("etwa: vollständiger Vortrag, geeignete Beweisanträge", 150, w902_y + 290, "vortrag", size=32),
    zit("BVerfGE 159, 223 Rn. 101; BVerfG-Merkblatt III.2.a", 150, w902_y + 345, beim("vortrag", "Beweisanträge")),
    ficon("tabler", "building-bank", IX - 120, IU, 90, beim("erschoepft", "Instanzen"), fuell=WEISS),
    ficon("tabler", "building-bank", IX, IU, 110, beim("erschoepft", "Instanzen"), fuell=WEISS),
    ficon("tabler", "building-bank", IX + 130, IU, 130, beim("erschoepft", "Instanzen"), fuell=GELB),
    *fig("WE", FX, FB, FR, [("rechtsweg", "ruhig"), ("subsid", "denkt")]),
    schild("Frau Wendt", FX, "rechtsweg", WE_F),
]))

# K1 VII. Form ------------------------------------------------------------------------------------------------------------------
folie([("form", "A. Zulässigkeit › VII. Form, §§ 23 I, 92 BVerfGG")], rechts_frei([
    *tafel("form", "VII. Form und Frist"),
    z("Form: schriftlich einreichen und begründen", 110, 190, beim("form", "schriftlich"), "Bold", 36),
    zit("§ 23 Abs. 1 BVerfGG", 150, 245, beim("form", "Paragraf")),
    z("Begründung: verletztes Recht und angegriffener Akt", 110, 330, beim("p92", "verletzte"), "Bold", 34),
    zit("§ 92 BVerfGG; vgl. BVerfGE 115, 118 Rn. 74", 150, 385, beim("p92", "Akt")),
    ficon("tabler", "file-pencil", IX, IU, 130, "form", fuell=WEISS),
    *fig("WE", FX, FB, FR, [("form", "ruhig")]),
    schild("Frau Wendt", FX, "form", WE_F),
]))

# K2 VII. Frist -------------------------------------------------------------------------------------------------------------------
W93 = ("„(1) Die Verfassungsbeschwerde ist binnen eines Monats zu erheben und zu begründen. … (3) Richtet sich die "
       "Verfassungsbeschwerde gegen ein Gesetz oder gegen einen sonstigen Hoheitsakt, gegen den ein Rechtsweg nicht "
       "offensteht, so kann die Verfassungsbeschwerde nur binnen eines Jahres seit dem Inkrafttreten des Gesetzes oder "
       "dem Erlaß des Hoheitsaktes erhoben werden.“")
w93, w93_y = wortlaut(80, 180, 1100, W93, "§ 93 Abs. 1 Satz 1, Abs. 3 BVerfGG", "frist", marken=[
    ("binnen eines Monats", beim("frist", "binnen")), ("zu erheben", beim("frist", "erheben")),
    ("gegen ein Gesetz", beim("jahr", "Gesetz")), ("binnen eines Jahres", beim("jahr", "Jahr")),
    ("Inkrafttreten", beim("jahr", "Inkrafttreten"))], size=30)
folie([("frist", "A. Zulässigkeit › VII. Frist, § 93 I BVerfGG"),
       ("jahr", "A. Zulässigkeit › VII. Frist gegen Gesetze, § 93 III BVerfGG"),
       ("zul", "A. Zulässigkeit › Ergebnis: zulässig")], rechts_frei([
    *tafel("frist", "VII. Form und Frist"),
    *w93,
    z("Beginn: Zustellung des vollständigen Urteils", 110, w93_y + 30, "beginn", "Bold", 34),
    zit("§ 93 Abs. 1 Satz 2 BVerfGG; § 116 Abs. 1 Satz 2 VwGO", 150, w93_y + 85, beim("beginn", "Urteils")),
    blk(110, w93_y + 145, 1040, 90, GRUEN, "zul", [("Form und Frist gewahrt: zulässig", "ExtraBold", 36, INK)]),
    ficon("tabler", "calendar", IX, IU, 140, "frist", fuell=WEISS),
    pl("1 Monat", IX, 190, beim("frist", "Monats"), fill=GELB, size=30, anker="m", bis=beim("jahr", "Jahr")),
    pl("Gesetz: 1 Jahr", IX, 190, beim("jahr", "Jahr"), fill=GELB, size=30, anker="m", bis="zul"),
    pl("zulässig", IX, 190, "zul", fill=GRUEN, size=30, anker="m"),
    *fig("WE", FX, FB, FR, [("frist", "denkt"), ("zul", "entschl")]),
    schild("Frau Wendt", FX, "frist", WE_F),
]))

# L1 B. Begründetheit: Prüfungsmaßstab ----------------------------------------------------------------------------------------
folie([("begr", "B. Begründetheit › Prüfungsmaßstab"), ("heck", "B. Begründetheit › spezifisches Verfassungsrecht")], rechts_frei([
    *tafel("begr", "B. Begründetheit"),
    z("begründet, wenn ein Grundrecht verletzt ist", 110, 190, beim("begr", "begründet"), "Bold", 36),
    z("Urteile: keine Nachprüfung in vollem Umfang", 110, 280, "voll", "Bold", 36),
    zit("BVerfG-Merkblatt I.", 150, 335, beim("voll", "Umfang")),
    z("nur: Verletzung spezifischen Verfassungsrechts", 110, 420, beim("heck", "spezifisches"), "Bold", 36),
    z("Grundrechte übersehen?", 150, 480, beim("heck2", "übersehen"), size=34),
    z("Gewicht der Grundrechte falsch eingeschätzt?", 150, 535, beim("heck2", "Gewicht"), size=34),
    zit("BVerfG, 1 BvR 98/21, Rn. 10, mit BVerfGE 18, 85 <92> („Hecksche Formel“)", 150, 590, beim("heck2", "eingeschätzt")),
    ficon(HC, "classical-building", IX, IU, 180, "begr", fuell=WEISS),
    *fig("WE", FX, FB, FR, [("begr", "ruhig"), ("heck", "denkt")]),
    schild("Frau Wendt", FX, "begr", WE_F),
]))

# L2 B. Begründetheit: verfassungswidriges Gesetz ---------------------------------------------------------------------------------
folie([("gesetzpr", "B. Begründetheit › verfassungswidriges Gesetz?")], rechts_frei([
    *tafel("gesetzpr", "B. Begründetheit: das Gesetz"),
    z("Urteil beruht auf verfassungswidrigem Gesetz?", 110, 190, beim("gesetzpr", "Beruht"), "Bold", 36),
    z("dann verletzt schon das ihr Grundrecht", 150, 245, beim("gesetzpr", "verletzt"), size=34),
    z("Gesetz prüfen:", 110, 330, beim("dreischritt", "prüfst"), "Bold", 36),
    pl("Schutzbereich", 150, 395, beim("dreischritt", "Schutzbereich"), fill=WEISS, size=32),
    pl("Eingriff", 450, 395, beim("dreischritt", "Eingriff"), fill=WEISS, size=32),
    pl("Rechtfertigung", 660, 395, beim("dreischritt", "Rechtfertigung"), fill=WEISS, size=32),
    blk(110, 510, 1040, 130, GELB, "nichtig", [("Erfolg: Urteil aufgehoben, Gesetz grundsätzlich nichtig", "ExtraBold", 32, INK),
                                            ("§ 95 Abs. 2, Abs. 3 Satz 2 BVerfGG; vgl. BVerfGE 150, 244 Rn. 34", "Regular", 26, INK)]),
    ficon("tabler", "book", IX, IU, 130, "gesetzpr", fuell=WEISS),
    *fig("WE", FX, FB, FR, [("gesetzpr", "denkt"), ("nichtig", "entschl")]),
    schild("Frau Wendt", FX, "gesetzpr", WE_F),
]))

# M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Nur Verfassungsrecht prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Urteilsverfassungsbeschwerde:", 200, 200, beim("tipp", "Urteilsverfassungsbeschwerde"), "Bold", 36),
    z("einfaches Recht nicht wie ein Fachgericht prüfen", 200, 255, beim("tipp", "Fachgericht"), size=34),
    z("Frag nur: Wo liegt der Verstoß", 200, 350, "tipp1", "Bold", 36),
    z("gegen Verfassungsrecht?", 200, 405, beim("tipp1", "Verstoß"), "Bold", 36),
    z("Unproblematisches nur kurz feststellen,", 200, 500, "tipp2", size=34),
    z("etwa die Prozessfähigkeit", 200, 555, beim("tipp2", "Prozessfähigkeit"), size=34, farbe=TEXT),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Verfassungsbeschwerde"), 110, 90, "sch", 48),
    z("A. Zulässigkeit", K1, 180, "sa", "Bold", 38, rechts=1820),
    z("I. Zuständigkeit: Art. 94 I Nr. 4a GG, § 13 Nr. 8a BVerfGG", K2, 240, "s1", size=SZ, rechts=1820),
    z("II. Beschwerdeberechtigung: jedermann, § 90 I BVerfGG", K2, 295, "s2", size=SZ, rechts=1820),
    z("III. Prozessfähigkeit", K2, 350, "s3", size=SZ, rechts=1820),
    z("IV. Beschwerdegegenstand: Akt der öffentlichen Gewalt", K2, 405, "s4", size=SZ, rechts=1820),
    z("V. Beschwerdebefugnis:", K2, 460, "s5", size=SZ, rechts=1820),
    z("möglicherweise verletzt; selbst, gegenwärtig, unmittelbar", K3, 510, beim("s5", "möglicherweise"), "Bold", SZ, rechts=1820),
    z("VI. Rechtswegerschöpfung und Subsidiarität, § 90 II BVerfGG", K2, 565, "s6", size=SZ, rechts=1820),
    z("VII. Form und Frist, §§ 23 I, 92, 93 BVerfGG", K2, 620, "s7", size=SZ, rechts=1820),
    z("B. Begründetheit", K1, 710, "sb", "Bold", 38, rechts=1820),
    z("Verletzung eines Grundrechts;", K2, 770, "sb1", size=SZ, rechts=1820),
    z("bei Urteilen nur spezifisches Verfassungsrecht", K2, 825, beim("sb1", "bei"), "Bold", SZ, rechts=1820),
])

# O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gegen ein Urteil:", 0)], [("erst durch alle Instanzen,", 0)],
                 [("dann binnen eines Monats", "a"), (" nach Karlsruhe.", 0)]],
                750, 310, 48, "merke", {"a": beim("merke", "binnen")}),
    *markertext([[("Dort zählt nur das", 0)], [("Verfassungsrecht.", "b")]],
                750, 600, 48, "m2", {"b": beim("m2", "Verfassungsrecht")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
