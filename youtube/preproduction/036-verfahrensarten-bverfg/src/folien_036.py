"""Folge 036 · Verfahrensarten BVerfG: Welches Verfahren wann? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Bundesgesetz verbietet privates Silvesterfeuerwerk), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Das neue Gesetz, B Feuerwerksladen (Frau Pfeiffer), C Bundestag (Fraktion Pohl), D Land Süd (Hagedorn),
E Amtsgericht (Richter Glaser), F Die Frage, G Sachverhalt, H Zuständigkeit Art. 94 GG, I1/I2 Verfassungsbeschwerde,
J1/J2 Organstreit, K1/K2 abstrakte Normenkontrolle, L1/L2 konkrete Normenkontrolle, M1/M2 Bund-Länder-Streit,
N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Feuerzeug, wenn der Kunde zündet; Stempel, wenn Richter Glaser vorlegt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_036/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_036/" in n:
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
PF_F, PO_F, HA_F, GL_F = PINK, BLAU, LILA, GRAU   # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270

# A Fall: das neue Gesetz ---------------------------------------------------------------------------------------------------
folie([(NULL, "Fall · Das neue Gesetz")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Ein neues Bundesgesetz", 70, 40, NULL, fill=GELB, size=44)),
    ficon("tabler", "building-bank", 330, BODEN - 2, 320, NULL, fuell=GELB, anim="cut"),
    hart(pl("Bundestag", 330, BODEN + 22, NULL, fill=WEISS, size=30, anker="m")),
    ficon("tabler", "file-text", 720, 640, 150, beim("fall", "Gesetz"), fuell=WEISS),
    pl("Gesetz", 720, 660, beim("fall", "Gesetz"), fill=WEISS, size=30, anker="m"),
    ficon(HC, "fireworks", 1180, 600, 230, "verbot", fuell=GELB),
    ficon("tabler", "rocket", 1460, 600, 170, beim("verbot", "Silvesterfeuerwerk"), fuell=ROT),
    ficon(HC, "firecracker", 1700, 600, 150, beim("verbot", "Silvesterfeuerwerk"), fuell=ROT, d=0.1),
    ficon("tabler", "ban", 1440, 660, 560, beim("verbot", "verboten")),
    pl("Verkauf", 1260, 700, beim("verbot", "Verkauf"), fill=WEISS, size=32, anker="m"),
    pl("Abbrennen", 1620, 700, beim("verbot", "Abbrennen"), fill=WEISS, size=32, anker="m"),
    ficon("tabler", "receipt-euro", 720, BODEN - 2, 120, "bussgeld", fuell=GELB),
    pl("Bußgeld", 720, 900, beim("bussgeld", "Bußgeld"), fill=ROT, size=30, anker="m"),
    ficon(HC, "classical-building", 1000, 300, 150, beim("viele", "Karlsruhe"), fuell=WEISS),
    pl("nach Karlsruhe", 1000, 310, beim("viele", "Karlsruhe"), fill=PINK, size=30, anker="m"),
])

# B Fall: Frau Pfeiffer im Feuerwerksladen --------------------------------------------------------------------------------
PFX = 1180
PFb = ("PF_redet", PFX, BODEN, FH)
folie([("pfeiffer", "Fall · Frau Pfeiffer, Feuerwerksladen")], [
    linienzug([(60, BODEN), (1860, BODEN)], "pfeiffer", breite=7, farbe=INK),
    pl("Im Feuerwerksladen", 70, 40, "pfeiffer", fill=GELB, size=40),
    karte(80, 300, 600, 560, "pfeiffer", fill=HOLZ, rund=14, schatten=6, rand=5),
    linienzug([(90, 560), (670, 560)], "pfeiffer", breite=6, farbe=INK),
    ficon(HC, "fireworks", 210, 550, 140, "pfeiffer", fuell=GELB),
    ficon("tabler", "rocket", 380, 550, 120, "pfeiffer", fuell=ROT),
    ficon(HC, "firecracker", 550, 550, 110, "pfeiffer", fuell=ROT),
    ficon("tabler", "rocket", 210, 845, 120, "pfeiffer", fuell=BLAU),
    ficon("tabler", "sparkle", 380, 845, 110, "pfeiffer", fuell=GELB),
    ficon(HC, "fireworks", 550, 845, 140, "pfeiffer", fuell=PINK),
    ficon("tabler", "building-store", 1720, BODEN - 2, 220, "pfeiffer", fuell=BLAU),
    *fig("PF", PFX, BODEN, FH, [("pfeiffer", "ruhig")], bis="pf1"),
    *redet("PF_redet", PFX, BODEN, FH, "pf1", "pohl"),
    schild("Frau Pfeiffer, Ladeninhaberin", PFX, "pfeiffer", PF_F, unten=BODEN),
    ficon("tabler", "ban", 380, 840, 480, beim("pf1", "nimmt")),
    blase("sprech", 760, 230, "pf1", 1180, 190, inhalt=["Das Gesetz nimmt mir mein Geschäft.",
                                                      "Dagegen wehre ich mich in Karlsruhe."], textsize=32, figur=PFb),
])

# C Fall: Bundestag, Fraktion Pohl fragt -------------------------------------------------------------------------------------
POX = 880
POb = ("PO_redet_r", POX, BODEN, FH)
folie([("pohl", "Fall · Fraktion fragt die Bundesregierung")], [
    linienzug([(60, BODEN), (1860, BODEN)], "pohl", breite=7, farbe=INK),
    pl("Im Bundestag", 70, 40, "pohl", fill=GELB, size=40),
    ficon("tabler", "building-bank", 330, BODEN - 2, 300, "pohl", fuell=GELB),
    pl("Bundestag", 330, BODEN + 22, "pohl", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "building-bank", 1600, BODEN - 2, 300, beim("pohl", "auf"), fuell=BLAU),
    pl("Bundesregierung", 1600, BODEN + 22, beim("pohl", "auf"), fill=WEISS, size=30, anker="m"),
    *fig("PO", POX, BODEN, FH, [(beim("pohl", "Pohl"), "ruhig_r"), ("schweigt", "denkt_r")], bis="po1"),
    *redet("PO_redet_r", POX, BODEN, FH, "po1", "hagedorn"),
    schild("Herr Pohl, Fraktionschef", POX, beim("pohl", "Pohl"), PO_F, unten=BODEN),
    ficon("tabler", "message-question", 1250, 500, 130, beim("pohl", "Gutachten"), fuell=WEISS),
    pl("Gutachten zum Verbot?", 1250, 520, beim("pohl", "Gutachten"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "ban", 1600, 470, 150, beim("schweigt", "verweigert")),
    pl("Antwort verweigert", 1600, 300, beim("schweigt", "verweigert"), fill=ROT, size=30, anker="m"),
    blase("sprech", 720, 210, "po1", 760, 190, inhalt=["Die Regierung muss uns Auskunft geben.",
                                                     "Das klären wir in Karlsruhe."], textsize=30, figur=POb),
])

# D Fall: Land Süd, Ministerpräsidentin Hagedorn -----------------------------------------------------------------------------
HAX = 1300
HAb = ("HA_redet", HAX, BODEN, FH)
folie([("hagedorn", "Fall · Landesregierung Süd")], [
    linienzug([(60, BODEN), (1860, BODEN)], "hagedorn", breite=7, farbe=INK),
    pl("Land Süd", 70, 40, "hagedorn", fill=GELB, size=40),
    ficon("tabler", "map", 450, BODEN - 2, 360, beim("hagedorn", "Land"), fuell=GRUEN),
    pl("Land Süd", 450, BODEN + 22, beim("hagedorn", "Land"), fill=WEISS, size=30, anker="m"),
    *fig("HA", HAX, BODEN, FH, [("hagedorn", "ruhig")], bis="ha1"),
    *redet("HA_redet", HAX, BODEN, FH, "ha1", "kunde"),
    schild("Ministerpräsidentin Hagedorn", HAX, "hagedorn", HA_F, unten=BODEN),
    ficon(HC, "classical-building", 1700, 560, 160, beim("ha1", "Karlsruhe"), fuell=WEISS),
    pl("Karlsruhe", 1700, 580, beim("ha1", "Karlsruhe"), fill=PINK, size=30, anker="m"),
    blase("sprech", 760, 210, "ha1", 920, 200, inhalt=["Dieses Gesetz ist verfassungswidrig.",
                                                     "Wir lassen es in Karlsruhe prüfen."], textsize=30, figur=HAb),
])

# E Fall: Kunde, Bußgeld, Amtsgericht ------------------------------------------------------------------------------------------
GLX = 1560
GLb = ("GL_redet", GLX, BODEN, FH)
VOR = beim("gl1", "vor")
folie([("kunde", "Fall · Bußgeld und Einspruch"), ("glaser", "Fall · Am Amtsgericht")], [
    linienzug([(60, BODEN), (1860, BODEN)], "kunde", breite=7, farbe=INK),
    pl("Ein Kunde zündet trotzdem", 70, 40, "kunde", fill=GELB, size=40),
    ficon("tabler", "rocket", 260, 640, 170, beim("kunde", "Raketen"), fuell=ROT),
    szene(ficon("tabler", "lighter", 390, 720, 70, beim("kunde", "zündet"), fuell=ROT), "036feuerzeug*", 1.0, -0.05),
    ficon("tabler", "receipt-euro", 610, 640, 130, beim("kunde", "Bußgeld"), fuell=GELB),
    pl("Bußgeld", 610, 660, beim("kunde", "Bußgeld"), fill=ROT, size=30, anker="m"),
    ficon("tabler", "file-text", 860, 640, 130, beim("kunde", "Einspruch"), fuell=WEISS),
    pl("Einspruch", 860, 660, beim("kunde", "Einspruch"), fill=WEISS, size=30, anker="m"),
    pl("Amtsgericht", 1180, 630, beim("glaser", "Amtsgericht"), fill=GRAU, size=30, anker="m"),
    ficon("tabler", "gavel", 1180, BODEN - 2, 170, beim("glaser", "Amtsgericht"), fuell=HOLZ),
    *fig("GL", GLX, BODEN, FH, [(beim("glaser", "Richter"), "ruhig")], bis="gl1"),
    *redet("GL_redet", GLX, BODEN, FH, "gl1", "frage"),
    schild("Richter Glaser", GLX, beim("glaser", "Richter"), GL_F, unten=BODEN),
    szene(ficon("tabler", "rubber-stamp", 860, 470, 110, VOR, fuell=ROT), "036stempel*", 1.0, 0.1),
    pl("Vorlage an das BVerfG", 860, 790, VOR, fill=PINK, size=30, anker="m"),
    blase("sprech", 820, 210, "gl1", 1100, 260, inhalt=["Ich halte das Gesetz für verfassungswidrig.",
                                                      "Deshalb lege ich es dem", "Bundesverfassungsgericht vor."],
          textsize=30, figur=GLb),
])

# F Fall: die Frage – alle vier ------------------------------------------------------------------------------------------------
QH = 400
QX = (300, 730, 1180, 1620)
folie([("frage", "Fall · Welches Verfahren passt wann?"), ("regel", "Fall · Wer will was gegen wen?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "frage", breite=7, farbe=INK),
    peep_voll("PF_entschl_r", QX[0], BODEN, QH, "frage", anim="cut"),
    peep_voll("PO_entschl_r", QX[1], BODEN, QH, "frage", anim="cut"),
    peep_voll("HA_entschl", QX[2], BODEN, QH, "frage", anim="cut"),
    peep_voll("GL_denkt", QX[3], BODEN, QH, "frage", anim="cut"),
    schild("Frau Pfeiffer", QX[0], "frage", PF_F, unten=BODEN, d=0.0, size=26),
    schild("Herr Pohl", QX[1], "frage", PO_F, unten=BODEN, d=0.0, size=26),
    schild("Ministerpräsidentin Hagedorn", QX[2], "frage", HA_F, unten=BODEN, d=0.0, size=24),
    schild("Richter Glaser", QX[3], "frage", GL_F, unten=BODEN, d=0.0, size=26),
    pl("Bürgerin", QX[0], 400, beim("frage", "Bürgerin"), fill=WEISS, size=28, anker="m"),
    pl("Fraktion", QX[1], 400, beim("frage", "Fraktion"), fill=WEISS, size=28, anker="m"),
    pl("Landesregierung", QX[2], 400, beim("frage", "Landesregierung"), fill=WEISS, size=28, anker="m"),
    pl("Amtsgericht", QX[3], 400, beim("frage", "Amtsgericht"), fill=WEISS, size=28, anker="m"),
    pl("Welches Verfahren passt wann?", 960, 60, beim("frage", "Welches"), fill=PINK, size=40, anker="m"),
    pl("Wer will was gegen wen?", 960, 180, beim("regel", "Wer"), fill=GELB, size=40, anker="m"),
])

# G Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Ein neues Bundesgesetz verbietet privates Silvesterfeuerwerk, den Verkauf und das Abbrennen; Verstöße kosten ein "
    "Bußgeld. Frau Pfeiffer verkauft in ihrem Laden seit Jahren Feuerwerk und will sich in Karlsruhe gegen das Gesetz "
    "wehren. Die Fraktion von Herrn Pohl fragt im Bundestag, auf welches Gutachten sich das Verbot stützt; die "
    "Bundesregierung verweigert die Antwort. Die Landesregierung Süd hält das Gesetz für verfassungswidrig und will es "
    "prüfen lassen; bis dahin setzt das Land Süd es nicht um, die Bundesregierung rügt das.",
    "Ein Kunde zündet trotzdem Raketen, soll ein Bußgeld zahlen und legt Einspruch ein. Richter Glaser am Amtsgericht hält "
    "das Gesetz für verfassungswidrig und für seine Entscheidung erheblich.",
], "Wer kann mit welchem Verfahren nach Karlsruhe?")

# H Zuständigkeit: Art. 94 GG n. F. ---------------------------------------------------------------------------------------------
folie([("art94", "Zuständigkeit › Art. 94 GG (seit 28.12.2024)"), ("art93", "Zuständigkeit › früher Art. 93 GG"),
       ("p13", "Zuständigkeit › BVerfGG, Katalog § 13")], rechts_frei([
    *tafel("art94", "Zuständigkeiten des BVerfG"),
    z("Art. 94 GG: Zuständigkeiten", 110, 190, beim("art94", "Zuständigkeiten"), "Bold", 38),
    z("seit 28.12.2024 (BGBl. 2024 I Nr. 439)", 150, 250, beim("art94", "achtundzwanzigsten"), size=34),
    z("vorher: Art. 93 GG a. F.", 110, 350, "art93", "Bold", 38),
    z("Art. 93 GG heute: Stellung und Organisation", 150, 410, beim("art93", "Stellung"), size=34),
    z("Verfahren: Bundesverfassungsgerichtsgesetz", 110, 510, "p13", "Bold", 36),
    z("Katalog: § 13 BVerfGG", 150, 570, beim("p13", "Katalog"), size=34),
    ficon(HC, "classical-building", IX, 520, 300, "art94", fuell=WEISS),
    pl("Bundesverfassungsgericht", IX, 540, "art94", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "calendar", IX, 860, 150, beim("art94", "achtundzwanzigsten"), fuell=WEISS),
    pl("28.12.2024", IX, 880, beim("art94", "achtundzwanzigsten"), fill=GELB, size=30, anker="m"),
]))

# I1 Verfassungsbeschwerde: Wer will was gegen wen? ---------------------------------------------------------------------------
W4A = ("„(1) Das Bundesverfassungsgericht entscheidet: … 4a. über Verfassungsbeschwerden, die von jedermann mit der "
       "Behauptung erhoben werden können, durch die öffentliche Gewalt in einem seiner Grundrechte … verletzt zu sein;“")
w4a, w4a_y = wortlaut(80, 350, 1100, W4A, "Art. 94 Abs. 1 Nr. 4a GG", "vb", marken=[
    ("jedermann", beim("vb", "Jedermann")), ("Grundrechte", beim("vb", "Grundrechte")),
    ("öffentliche Gewalt", beim("vbgegen", "öffentliche"))])
folie([("vb", "1. Frau Pfeiffer › Wer will was gegen wen?"), ("wl4a", "1. Verfassungsbeschwerde, Art. 94 I Nr. 4a GG")],
      rechts_frei([
    *tafel("vb", "1. Frau Pfeiffer"),
    *wfragen(beim("vb", "Jedermann"), "jedermann", beim("vb", "Was"), "eigene Grundrechte: Berufsfreiheit",
             "vbgegen", "öffentliche Gewalt: das Gesetz"),
    *w4a,
    blk(110, w4a_y + 30, 1040, 90, GRUEN, "wl4a", [("Verfassungsbeschwerde, Art. 94 I Nr. 4a GG", "ExtraBold", 36, INK)]),
    ficon("tabler", "building-store", IX, IU, 150, "vb", fuell=BLAU, bis="vbgegen"),
    ficon("tabler", "file-text", IX, IU, 120, "vbgegen", fuell=WEISS),
    *fig("PF", FX, FB, FR, [("vb", "ruhig"), ("vbgegen", "entschl")]),
    schild("Frau Pfeiffer", FX, "vb", PF_F),
]))

# I2 Verfassungsbeschwerde: Stichworte ---------------------------------------------------------------------------------------
folie([("vbbef", "1. Verfassungsbeschwerde › Beschwerdebefugnis"), ("vbfrist", "1. Verfassungsbeschwerde › Frist, § 93 BVerfGG")],
      rechts_frei([
    *tafel("vbbef", "Verfassungsbeschwerde: Stichworte"),
    z("Beschwerdebefugnis gegen ein Gesetz:", 110, 190, beim("vbbef", "Beschwerdebefugnis"), "Bold", 36),
    z("selbst, gegenwärtig und unmittelbar betroffen", 150, 250, beim("vbbef", "selbst"), size=34),
    zit("BVerfGE 115, 118 Rn. 78; §§ 13 Nr. 8a, 90 ff. BVerfGG", 150, 305, beim("vbbef", "betroffen")),
    z("Frist gegen ein Gesetz: ein Jahr ab Inkrafttreten", 110, 400, "vbfrist", "Bold", 36),
    zit("§ 93 Abs. 3 BVerfGG", 150, 455, beim("vbfrist", "Inkrafttreten")),
    z("gegen ein Urteil: ein Monat, § 93 Abs. 1 BVerfGG", 110, 540, beim("vbfrist", "Urteil"), "Bold", 36),
    z("vorher in der Regel Rechtsweg erschöpfen", 150, 600, beim("vbfrist", "vorher"), size=34),
    zit("§ 90 Abs. 2 BVerfGG", 150, 655, beim("vbfrist", "erschöpfen")),
    ficon("tabler", "calendar", IX, IU, 140, "vbfrist", fuell=WEISS),
    pl("1 Jahr", IX, 330, beim("vbfrist", "Jahr"), fill=GELB, size=30, anker="m", bis=beim("vbfrist", "Monat")),
    pl("1 Monat", IX, 330, beim("vbfrist", "Monat"), fill=GELB, size=30, anker="m"),
    *fig("PF", FX, FB, FR, [("vbbef", "denkt")]),
    schild("Frau Pfeiffer", FX, "vbbef", PF_F),
]))

# J1 Organstreit: Wer will was gegen wen? -------------------------------------------------------------------------------------
W1 = ("„(1) Das Bundesverfassungsgericht entscheidet: 1. über die Auslegung dieses Grundgesetzes aus Anlass von "
      "Streitigkeiten über den Umfang der Rechte und Pflichten eines obersten Bundesorgans oder anderer Beteiligter, die "
      "durch dieses Grundgesetz oder in der Geschäftsordnung eines obersten Bundesorgans mit eigenen Rechten ausgestattet "
      "sind; …“")
w1, w1_y = wortlaut(80, 350, 1100, W1, "Art. 94 Abs. 1 Nr. 1 GG", "os", marken=[
    ("anderer Beteiligter", beim("os", "Fraktion")), ("obersten Bundesorgans", beim("os", "Bundesregierung")),
    ("Rechte und Pflichten", beim("os", "eigene"))], size=30)
folie([("os", "2. Fraktion Pohl › Wer will was gegen wen?"), ("wl1", "2. Organstreit, Art. 94 I Nr. 1 GG")], rechts_frei([
    *tafel("os", "2. Herr Pohl und seine Fraktion"),
    *wfragen(beim("os", "Fraktion"), "seine Fraktion", beim("os", "Bundesregierung"), "die Bundesregierung",
             beim("os", "eigene"), "eigene Rechte: Frage- und Informationsrecht", labels=("Wer?", "Gegen wen?", "Was?")),
    *w1,
    blk(110, w1_y + 25, 1040, 90, GRUEN, "wl1", [("Organstreit, Art. 94 I Nr. 1 GG", "ExtraBold", 36, INK)]),
    zit("Frage- und Informationsrecht: Art. 38 I 2, 20 II 2 GG; BVerfG, 2 BvE 2/11, Rn. 168 f.", 110, w1_y + 135, "wl1"),
    ficon("tabler", "building-bank", IX, IU, 170, beim("os", "Bundesregierung"), fuell=BLAU, bis=beim("os", "Frage")),
    ficon("tabler", "message-question", IX, IU, 140, beim("os", "Frage"), fuell=WEISS),
    *fig("PO", FX, FB, FR, [("os", "ruhig"), (beim("os", "eigene"), "entschl")]),
    schild("Herr Pohl", FX, "os", PO_F),
]))

# J2 Organstreit: Stichworte --------------------------------------------------------------------------------------------------
folie([("osbet", "2. Organstreit › Beteiligte, § 63 BVerfGG"), ("osfrist", "2. Organstreit › Frist, § 64 III BVerfGG"),
       ("osfest", "2. Organstreit › nur Feststellung, § 67 BVerfGG")], rechts_frei([
    *tafel("osbet", "Organstreit: Stichworte"),
    z("Antragsberechtigt: Fraktion als Teil des Bundestages", 110, 190, beim("osbet", "Antragsberechtigt"), "Bold", 34),
    z("Antragsgegnerin: Bundesregierung", 150, 250, beim("osbet", "Antragsgegnerin"), size=34),
    zit("§ 63 BVerfGG; BVerfG, 2 BvE 2/11, Rn. 163 f.", 150, 305, beim("osbet", "Bundesregierung")),
    z("Frist: sechs Monate, § 64 Abs. 3 BVerfGG", 110, 400, "osfrist", "Bold", 36),
    blk(110, 500, 1040, 110, GELB, "osfest", [("Erfolg: das Gericht stellt nur fest", "ExtraBold", 36, INK),
                                            ("§ 67 BVerfGG; keine Verpflichtung (BVerfG, 2 BvE 2/11, Rn. 174 f.)", "Regular", 26, INK)]),
    ficon("tabler", "users", IX, IU, 170, "osbet", fuell=BLAU, bis="osfrist"),
    ficon("tabler", "calendar", IX, IU, 140, "osfrist", fuell=WEISS, bis="osfest"),
    pl("6 Monate", IX, 330, beim("osfrist", "sechs"), fill=GELB, size=30, anker="m", bis="osfest"),
    ficon(HC, "classical-building", IX, IU, 180, "osfest", fuell=WEISS),
    *fig("PO", FX, FB, FR, [("osbet", "ruhig"), ("osfest", "denkt")]),
    schild("Herr Pohl", FX, "osbet", PO_F),
]))

# K1 abstrakte Normenkontrolle: Wer will was gegen wen? ------------------------------------------------------------------------
W2 = ("„(1) Das Bundesverfassungsgericht entscheidet: … 2. bei Meinungsverschiedenheiten oder Zweifeln über die förmliche "
      "und sachliche Vereinbarkeit von Bundesrecht oder Landesrecht mit diesem Grundgesetz … auf Antrag der "
      "Bundesregierung, einer Landesregierung oder eines Viertels der Mitglieder des Bundestages;“")
w2, w2_y = wortlaut(80, 350, 1100, W2, "Art. 94 Abs. 1 Nr. 2 GG", "ank", marken=[
    ("einer Landesregierung", beim("ank", "Landesregierung")), ("Vereinbarkeit von Bundesrecht", beim("ank", "prüfen")),
    ("Bundesregierung,", beim("ankber", "Bundesregierung")),
    ("Viertels", beim("ankber", "Viertel")), ("Mitglieder des Bundestages", beim("ankber", "Viertel"))], size=30)
folie([("ank", "3. Landesregierung Süd › Wer will was gegen wen?"), ("wl2", "3. Abstrakte Normenkontrolle, Art. 94 I Nr. 2 GG"),
       ("ankber", "3. Abstrakte Normenkontrolle › Antragsberechtigung")], rechts_frei([
    *tafel("ank", "3. Ministerpräsidentin Hagedorn", size=42),
    *wfragen(beim("ank", "Landesregierung"), "die Landesregierung", beim("ank", "prüfen"), "nur das Gesetz prüfen lassen",
             beim("ank", "ohne"), "ohne Gegner"),
    *w2,
    blk(110, w2_y + 25, 1040, 90, GRUEN, "wl2", [("abstrakte Normenkontrolle, Art. 94 I Nr. 2 GG", "ExtraBold", 34, INK)]),
    ficon("tabler", "map", IX, IU, 180, "ank", fuell=GRUEN, bis="wl2"),
    ficon("tabler", "scale", IX, IU, 180, "wl2", fuell=GELB),
    *fig("HA", FX, FB, FR, [("ank", "ruhig"), (beim("ank", "Gesetz"), "entschl")]),
    schild("Ministerpräsidentin Hagedorn", FX, "ank", HA_F, size=24),
]))

# K2 abstrakte Normenkontrolle: objektives Verfahren -------------------------------------------------------------------------
folie([("ankobj", "3. Abstrakte Normenkontrolle › keine eigenen Rechte, keine Frist")], rechts_frei([
    *tafel("ankobj", "Abstrakte Normenkontrolle: Stichworte"),
    ok(140, 215, beim("ankobj", "Eigene"), gr=22),
    z("keine eigenen Rechte nötig", 185, 190, beim("ankobj", "Eigene"), "Bold", 34),
    ok(140, 295, beim("ankobj", "Frist"), gr=22),
    z("keine Frist", 185, 270, beim("ankobj", "Frist"), "Bold", 34),
    zit("§§ 13 Nr. 6, 76 ff. BVerfGG; BVerfGE 150, 1 Rn. 137 f.", 110, 360, beim("ankobj", "Frist")),
    ficon("tabler", "hourglass-off", IX, IU, 140, beim("ankobj", "Frist"), fuell=WEISS),
    *fig("HA", FX, FB, FR, [("ankobj", "denkt")]),
    schild("Ministerpräsidentin Hagedorn", FX, "ankobj", HA_F, size=24),
]))

# L1 konkrete Normenkontrolle: Art. 100 I GG (vorgelesen) ---------------------------------------------------------------------
W100 = ("„Hält ein Gericht ein Gesetz, auf dessen Gültigkeit es bei der Entscheidung ankommt, für verfassungswidrig, so "
        "ist das Verfahren auszusetzen und … die Entscheidung des Bundesverfassungsgerichtes einzuholen. …“")
w100, w100_y = wortlaut(80, 330, 1100, W100, "Art. 100 Abs. 1 Satz 1 GG", "wl100", marken=[
    ("Gericht", beim("wl100", "Gericht")), ("auf dessen Gültigkeit", beim("wl100", "auf")),
    ("für verfassungswidrig,", beim("wl100", "verfassungswidrig")), ("auszusetzen", beim("wl100", "auszusetzen")),
    ("Bundesverfassungsgerichtes einzuholen", beim("wl100", "Bundesverfassungsgerichtes"))], size=34)
folie([("knk", "4. Richter Glaser › Wer will was gegen wen?"), ("wl100", "4. Konkrete Normenkontrolle, Art. 100 I GG")],
      rechts_frei([
    *tafel("knk", "4. Richter Glaser"),
    z("Wer?", 110, 180, beim("knk", "kein"), "ExtraBold", 32),
    z("kein Bürger, kein Organ: ein Gericht", 320, 180, beim("knk", "kein"), size=32),
    z("Wortlaut:", 110, 260, "wl100", "ExtraBold", 32),
    *w100,
    blk(110, w100_y + 25, 1040, 90, GRUEN, beim("wl100", "einzuholen"),
        [("konkrete Normenkontrolle, Art. 100 I GG", "ExtraBold", 36, INK)]),
    ficon("tabler", "gavel", IX, IU, 170, "knk", fuell=HOLZ),
    *fig("GL", FX, FB, FR, [("knk", "ruhig")]),
    schild("Richter Glaser", FX, "knk", GL_F),
]))

# L2 konkrete Normenkontrolle: Stichworte ------------------------------------------------------------------------------------
folie([("knkmon", "4. Konkrete Normenkontrolle › Verwerfungsmonopol"), ("knkueb", "4. Konkrete Normenkontrolle › Überzeugung"),
       ("knkerh", "4. Konkrete Normenkontrolle › Entscheidungserheblichkeit"),
       ("knkpart", "4. Konkrete Normenkontrolle › keine Vorlage auf Antrag")], rechts_frei([
    *tafel("knkmon", "Konkrete Normenkontrolle: Stichworte"),
    z("Parlamentsgesetz verwerfen: nur das BVerfG", 110, 190, "knkmon", "Bold", 36),
    zit("Verwerfungsmonopol, Art. 100 Abs. 1 GG; §§ 13 Nr. 11, 80 ff. BVerfGG", 150, 245, beim("knkmon", "verwerfen")),
    z("Überzeugung von der Verfassungswidrigkeit", 110, 330, "knkueb", "Bold", 36),
    z("Zweifel reichen nicht", 150, 390, beim("knkueb", "Zweifel"), size=34),
    z("Entscheidungserheblichkeit", 110, 480, "knkerh", "Bold", 36),
    z("es kommt für seine Entscheidung auf das Gesetz an", 150, 540, beim("knkerh", "Entscheidung"), size=34),
    zit("§ 80 Abs. 2 BVerfGG; BVerfGE 138, 136 Rn. 92 f.", 150, 595, beim("knkerh", "Gesetz")),
    nein(140, 685, "knkpart", gr=20),
    z("der Kunde kann die Vorlage nicht erzwingen", 185, 665, "knkpart", "Bold", 34),
    zit("§ 80 Abs. 3 BVerfGG", 185, 720, beim("knkpart", "erzwingen")),
    ficon(HC, "classical-building", IX, IU, 180, "knkmon", fuell=WEISS, bis="knkpart"),
    ficon("tabler", "file-text", IX, IU, 120, "knkpart", fuell=WEISS),
    *fig("GL", FX, FB, FR, [("knkmon", "ernst"), ("knkueb", "denkt"), ("knkerh", "ruhig")]),
    schild("Richter Glaser", FX, "knkmon", GL_F),
]))

# M1 Bund-Länder-Streit: Wer will was gegen wen? -------------------------------------------------------------------------------
W3 = ("„(1) Das Bundesverfassungsgericht entscheidet: … 3. bei Meinungsverschiedenheiten über Rechte und Pflichten des "
      "Bundes und der Länder, insbesondere bei der Ausführung von Bundesrecht durch die Länder und bei der Ausübung der "
      "Bundesaufsicht; …“")
w3, w3_y = wortlaut(80, 350, 1100, W3, "Art. 94 Abs. 1 Nr. 3 GG", "bls", marken=[
    ("Bundesaufsicht", beim("bls", "rügt")), ("Rechte und Pflichten", beim("blsstreit", "Pflichten")),
    ("Ausführung von Bundesrecht", beim("blsstreit", "Ausführung"))], size=32)
BRX, HAM = 1380, 1690
folie([("bls", "5. Bundesregierung › Wer will was gegen wen?"), ("wl3", "5. Bund-Länder-Streit, Art. 94 I Nr. 3 GG")],
      rechts_frei([
    *tafel("bls", "5. Die Bundesregierung"),
    *wfragen(beim("bls", "Bundesregierung"), "die Bundesregierung", beim("bls", "Land"), "das Land Süd",
             beim("blsstreit", "Pflichten"), "Pflichten bei der Ausführung von Bundesrecht",
             labels=("Wer?", "Gegen wen?", "Was?")),
    *w3,
    blk(110, w3_y + 25, 1040, 90, GRUEN, "wl3", [("Bund-Länder-Streit, Art. 94 I Nr. 3 GG", "ExtraBold", 36, INK)]),
    ficon("tabler", "building-bank", BRX, 560, 200, beim("bls", "Bundesregierung"), fuell=BLAU),
    pl("Bundesregierung", BRX, 580, beim("bls", "Bundesregierung"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "arrows-exchange", BRX, 360, 120, "blsstreit", fuell=WEISS),
    *fig("HA", HAM, FB, FR, [(beim("bls", "Land"), "sorge"), ("wl3", "denkt")]),
    schild("Ministerpräsidentin Hagedorn", HAM, beim("bls", "Land"), HA_F, size=22),
]))

# M2 Bund-Länder-Streit: Stichworte -----------------------------------------------------------------------------------------
folie([("blsbet", "5. Bund-Länder-Streit › Beteiligte, § 68 BVerfGG"),
       ("blsbr", "5. Bund-Länder-Streit › zuerst der Bundesrat, Art. 84 IV GG")], rechts_frei([
    *tafel("blsbet", "Bund-Länder-Streit: Stichworte"),
    z("nur Bundesregierung und Landesregierung", 110, 190, "blsbet", "Bold", 36),
    zit("§ 68 BVerfGG", 150, 245, beim("blsbet", "Landesregierung")),
    z("Land führt Bundesgesetz als eigene Angelegenheit aus:", 110, 330, "blsbr", "Bold", 34),
    z("zuerst entscheidet der Bundesrat", 150, 390, beim("blsbr", "zuerst"), size=34),
    z("gegen seinen Beschluss: binnen eines Monats", 150, 445, beim("blsbr", "Gegen"), size=34),
    zit("Art. 83, 84 Abs. 3 und 4 GG; § 70 BVerfGG", 150, 500, beim("blsbr", "Monats")),
    ficon("tabler", "building-bank", BRX, 560, 200, "blsbet", fuell=BLAU),
    pl("Bundesregierung", BRX, 580, "blsbet", fill=WEISS, size=26, anker="m", bis=beim("blsbr", "Bundesrat")),
    pl("Bundesrat", BRX, 580, beim("blsbr", "Bundesrat"), fill=LILA, size=26, anker="m"),
    ficon("tabler", "calendar", BRX, 360, 110, beim("blsbr", "Monats"), fuell=WEISS),
    pl("1 Monat", BRX, 230, beim("blsbr", "Monats"), fill=GELB, size=26, anker="m"),
    *fig("HA", HAM, FB, FR, [("blsbet", "denkt")]),
    schild("Ministerpräsidentin Hagedorn", HAM, "blsbet", HA_F, size=22),
]))

# N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Erst die Verfahrensart"), ("tipp2", "Klausurtipp · Art. 94 statt Art. 93")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst die Verfahrensart bestimmen,", 200, 200, beim("tipp", "Bestimme"), "Bold", 36),
    z("erst dann die Zulässigkeit prüfen", 200, 255, beim("tipp", "erst"), size=34),
    z("„Wer will was gegen wen?“", 200, 350, "tipp1", "Bold", 36),
    z("Klausurkonvention, keine Norm", 200, 405, beim("tipp1", "Klausurkonvention"), size=34),
    z("Zuständigkeit: Art. 94 GG zitieren", 200, 500, "tipp2", "Bold", 36),
    z("ältere Urteile und Bücher: Art. 93 GG a. F.", 200, 555, beim("tipp2", "Ältere"), size=34, farbe=TEXT),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema ----------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Welches Verfahren?"), 110, 90, "sch", 48),
    z("A. Nur die Gültigkeit einer Norm?", K1, 180, "sa", "Bold", 38, rechts=1820),
    z("I. Gericht überzeugt, Gesetz verfassungswidrig:", K2, 240, "sa1", size=SZ, rechts=1820),
    z("konkrete Normenkontrolle, Art. 100 I GG", K3, 290, beim("sa1", "konkrete"), "Bold", SZ, rechts=1820),
    z("II. Regierung oder ein Viertel des Bundestages:", K2, 350, "sa2", size=SZ, rechts=1820),
    z("abstrakte Normenkontrolle, Art. 94 I Nr. 2 GG", K3, 400, beim("sa2", "abstrakte"), "Bold", SZ, rechts=1820),
    z("B. Eigene Rechte: wer gegen wen?", K1, 490, "sb", "Bold", 38, rechts=1820),
    z("I. Jedermann gegen die öffentliche Gewalt:", K2, 550, "sb1", size=SZ, rechts=1820),
    z("Verfassungsbeschwerde, Art. 94 I Nr. 4a GG", K3, 600, beim("sb1", "Verfassungsbeschwerde"), "Bold", SZ, rechts=1820),
    z("II. Organ gegen Organ:", K2, 660, "sb2", size=SZ, rechts=1820),
    z("Organstreit, Art. 94 I Nr. 1 GG", K3, 710, beim("sb2", "Organstreit"), "Bold", SZ, rechts=1820),
    z("III. Bund gegen Land oder umgekehrt:", K2, 770, "sb3", size=SZ, rechts=1820),
    z("Bund-Länder-Streit, Art. 94 I Nr. 3 GG", K3, 820, beim("sb3", "Bund-Länder-Streit"), "Bold", SZ, rechts=1820),
])

# P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nur die Gültigkeit eines Gesetzes?", 0)], [("Der Weg führt zur ", 0), ("Normenkontrolle.", "a")]],
                750, 320, 50, "merke", {"a": beim("merke", "Normenkontrolle")}),
    *markertext([[("Eigene Rechte?", 0)], [("Dann entscheidet,", 0)], [("wer gegen wen ", "b"), ("streitet.", 0)]],
                750, 540, 50, "m2", {"b": beim("m2", "wer")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
