"""Folge 052 · Anscheinsgefahr: Hilfeschrei aus dem Fernseher – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Mietshaus, Sonntagabend kurz vor elf; Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut
../SZENENPLAN.md: A Mietshaus (Frau Jäger hört Schreie, Anruf), B Hausflur (Polizist Ahrens, Schlüsseldienst), C Wohnzimmer
(Herr Böttcher vor dem Krimi), D Wochen später (Kostenbescheid, kaputtes Schloss), E Frage, F Sachverhalt, G Landesrecht
und zwei Ebenen, H Ermächtigungsgrundlage mit Wortlaut § 41 I 1 Nr. 4 PolG NRW, I Wortlaut Art. 13 VII GG und formell,
J Gefahrbegriff mit Wortlaut § 8 I PolG NRW, K Anscheinsgefahr, L Abgrenzung Putativgefahr/Gefahrenverdacht,
M Verhältnismäßigkeit, Vollzug, Ergebnis der ersten Ebene, N Kosten (ex post), O Subsumtion Kosten, P Entschädigung mit
Wortlaut § 39 I OBG NRW, Q Gegenfall OLG Köln (Zeitschaltuhr), R Klausurtipp (Lexi), S Klausurschema, T Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Klingel und Klopfen an der Wohnungstür, Schloss beim Öffnen durch den
Schlüsseldienst (Szene B)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_052/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HOLZ = (236, 214, 178, 255)
WAND = (226, 218, 205, 255)
ZARTROT = (255, 240, 236, 255)
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


def zit(text, x, y, cue, size=26, rechts=1170):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, rechts=rechts)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_052/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach der amtlichen Quelle, als Zitat mit Normangabe. Automatisch umbrochen
    oder mit festen Zeilen (zeilen=[…]; die Zeilen ergeben zusammen genau den Normtext).
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


# --- Eigene Hilfsfunktion (wie Folge 049/044/041/032): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------
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
JA_F, AH_F, BO_F = LILA, BLAU, GELB         # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270

# A Fall: Sonntagabend im Mietshaus ------------------------------------------------------------------------------------------
JAX = 720
JAb = ("JA_redet_r", JAX, BODEN, FH)
STILL = beim("schrei2", "still")
WIEDER = beim("schrei2", "wieder")
folie([(NULL, "Fall · Sonntagabend im Mietshaus")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Sonntagabend, kurz vor elf", 70, 40, NULL, fill=GELB, size=40)),
    # Wohnung von Frau Jäger (links), Wand, Wohnung nebenan (rechts)
    hart(karte(1060, 140, 70, BODEN - 140, NULL, fill=WAND, rund=8, schatten=0, rand=4)),
    ficon("tabler", "window", 260, 560, 210, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "moon-stars", 260, 470, 90, NULL, fuell=GELB, anim="cut"),
    ficon("ph", "lamp", 420, BODEN - 2, 150, NULL, fuell=GELB, anim="cut"),
    *fig("JA", JAX, BODEN, FH, [(NULL, "ruhig_r"), (beim("schrei", "Schreie"), "sorge_r"), (STILL, "denkt_r"),
                                (WIEDER, "sorge_r")], bis="ja1", erst="cut"),
    *redet("JA_redet_r", JAX, BODEN, FH, "ja1", "polizei"),
    hart(schild("Frau Jäger, Nachbarin", JAX, NULL, JA_F, unten=BODEN, d=0.0)),
    ficon("tabler", "ear", 960, 470, 80, beim("schrei", "hört"), fuell=WEISS),
    ficon("ph", "speaker-high", 1290, 520, 120, beim("schrei", "Schreie"), fuell=ROT, bis=STILL),
    pl("Schreie", 1290, 560, beim("schrei", "Schreie"), fill=ROT, size=30, anker="m", bis=STILL),
    pl("Wohnung von Herrn Böttcher", 1500, 180, beim("schrei2", "Böttcher"), fill=WEISS, size=30, anker="m"),
    pl("„Hilfe!“", 1560, 330, beim("schrei2", "Hilfe"), fill=ROT, size=36, anker="m", bis=STILL),
    pl("still", 1560, 330, STILL, fill=WEISS, size=32, anker="m", bis=WIEDER),
    ficon("ph", "speaker-high", 1290, 520, 120, WIEDER, fuell=ROT),
    pl("wieder Schreie", 1290, 560, WIEDER, fill=ROT, size=30, anker="m"),
    pl("„Hilfe!“", 1560, 330, WIEDER, fill=ROT, size=36, anker="m"),
    ficon("tabler", "device-mobile", 860, 520, 60, "ja1", fuell=WEISS),
    blase("sprech", 780, 210, "ja1", 640, 245, inhalt=["Polizei? Bei meinem Nachbarn schreit", "eine Frau um Hilfe! Er wohnt allein.",
                                                      "Bitte kommen Sie schnell!"], textsize=29, figur=JAb),
])

# B Fall: Die Polizei an der Tür ------------------------------------------------------------------------------------------
TX, AHX = 700, 1400
AHb = ("AH_redet", AHX, BODEN, FH)
_tuer = ficon("tabler", "door", TX, BODEN - 2, 300, "polizei", fuell=WEISS, bis=beim("tuer", "auf"))
TUER_OBEN = BODEN - 2 - _tuer.sprite.height
KLI, KLO, RUF = beim("klingel", "klingelt"), beim("klingel", "klopft"), beim("klingel", "ruft")
NIEMAND, WEITER = beim("klingel", "Niemand"), beim("klingel", "schreit")
folie([("polizei", "Fall · Die Polizei an der Tür")], [
    linienzug([(60, BODEN), (1860, BODEN)], "polizei", breite=7, farbe=INK),
    pl("Wenige Minuten später: im Hausflur", 70, 40, "polizei", fill=GELB, size=40),
    ficon("tabler", "stairs", 220, BODEN - 2, 220, "polizei", fuell=WEISS),
    _tuer,
    pl("Böttcher", TX, TUER_OBEN + 70, "polizei", fill=GELB, size=26, anker="m", bis=beim("tuer", "auf")),
    ficon("ph", "door-open", TX, BODEN - 2, 300, beim("tuer", "auf"), fuell=WEISS),
    # Ahrens kommt von rechts
    peep_voll("AH_ruhig", AHX, BODEN, FH, beim("polizei", "Ahrens"), anim="pop", bis=RUF),
    *fig("AH", AHX, BODEN, FH, [(RUF, "entschl")], bis="ah1", erst="cut"),
    *redet("AH_redet", AHX, BODEN, FH, "ah1", "tuer"),
    *fig("AH", AHX, BODEN, FH, [("tuer", "ruhig")], bis="drin", erst="cut"),
    schild("Polizist Ahrens", AHX, beim("polizei", "Ahrens"), AH_F, unten=BODEN, d=0.0),
    # klingeln, klopfen, rufen – niemand öffnet – es schreit weiter
    szene(ficon("tabler", "bell-ringing", 960, 470, 80, KLI, fuell=GELB, bis="tuer"), "052klingel*", 0.8, 0.0),
    pl("klingelt", 1090, 420, KLI, fill=WEISS, size=28, anker="m", bis="tuer"),
    szene(ficon("ph", "hand-fist", 960, 570, 80, KLO, fuell=WEISS, bis="tuer"), "052klopfen*", 0.9, -0.15),
    pl("klopft", 1090, 520, KLO, fill=WEISS, size=28, anker="m", bis="tuer"),
    pl("ruft", 1090, 610, RUF, fill=WEISS, size=28, anker="m", bis="tuer"),
    pl("niemand öffnet", TX, TUER_OBEN - 60, NIEMAND, fill=WEISS, size=28, anker="m", bis="tuer"),
    ficon("ph", "speaker-high", 470, 600, 100, WEITER, fuell=ROT),
    pl("„Hilfe!“", 470, 400, WEITER, fill=ROT, size=34, anker="m"),
    blase("sprech", 760, 210, "ah1", 1330, 220, inhalt=["Wir können nicht warten. Da drin ist", "vielleicht jemand in Lebensgefahr."],
          textsize=30, figur=AHb, bis="tuer"),
    # Schlüsseldienst öffnet das Schloss (nur angedeutet)
    szene(ficon("ph", "toolbox", 1000, BODEN - 2, 150, beim("tuer", "Schlüsseldienst"), fuell=GELB), "052schloss*", 0.8, 0.0),
    pl("Schlüsseldienst", 1000, BODEN + 22, beim("tuer", "Schlüsseldienst"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "lock-x", 1000, 600, 90, beim("tuer", "Schloss"), fuell=ROT),
])

# C Fall: In der Wohnung ----------------------------------------------------------------------------------------------------
BSX, AH2 = 860, 1560
BSb = ("BS_redet_r", BSX, BODEN, 330)
folie([("drin", "Fall · In der Wohnung")], [
    linienzug([(60, BODEN), (1860, BODEN)], "drin", breite=7, farbe=INK),
    pl("Drinnen: Herr Böttcher allein vor dem Fernseher", 70, 40, "drin", fill=GELB, size=38),
    karte(220, BODEN - 140, 300, 138, "drin", fill=HOLZ, rund=10, schatten=0, rand=4),
    ficon("ph", "television", 370, BODEN - 140, 280, "drin", fuell=BLAU),
    ficon(HC, "clapper-board", 340, BODEN - 190, 80, beim("drin", "Krimi"), fuell=WEISS),
    pl("Krimi", 370, BODEN - 520, beim("drin", "Krimi"), fill=WEISS, size=30, anker="m"),
    ficon("ph", "speaker-high", 600, BODEN - 330, 100, beim("drin", "voller"), fuell=ROT),
    pl("volle Lautstärke", 600, BODEN - 520, beim("drin", "voller"), fill=ROT, size=28, anker="m"),
    ficon("ph", "armchair", BSX, BODEN - 2, 380, "drin", fuell=LILA),
    *fig("BS", BSX, BODEN - 70, 330, [("drin", "ruhig")], bis="bo1"),
    *redet("BS_redet_r", BSX, BODEN - 70, 330, "bo1", "bescheid"),
    schild("Herr Böttcher", BSX, "drin", BO_F, unten=BODEN),
    *fig("AH", AH2, BODEN, FH, [("drin", "ruhig"), ("bo1", "denkt")]),
    schild("Polizist Ahrens", AH2, "drin", AH_F, unten=BODEN),
    blase("sprech", 700, 210, "bo1", 1180, 300, inhalt=["Was ist denn hier los? Ich", "schaue doch nur meinen Krimi!"],
          textsize=32, figur=("BS_redet_r", BSX, BODEN - 70, 330)),
])

# D Fall: Wochen später ------------------------------------------------------------------------------------------------------
BOX = 1240
BOb = ("BO_redet", BOX, BODEN, FH)
KAPUTT = beim("schloss", "kaputt")
folie([("bescheid", "Fall · Wochen später")], [
    linienzug([(60, BODEN), (1860, BODEN)], "bescheid", breite=7, farbe=INK),
    pl("Wochen später", 70, 40, "bescheid", fill=GELB, size=40),
    karte(220, BODEN - 140, 300, 138, "bescheid", fill=HOLZ, rund=10, schatten=0, rand=4),
    ficon("ph", "television", 370, BODEN - 140, 280, "bescheid", fuell=WEISS),
    ficon("tabler", "file-euro", 720, 560, 150, beim("bescheid", "Polizeipräsidium"), fuell=GELB),
    pl("Polizeipräsidium", 720, 590, beim("bescheid", "Polizeipräsidium"), fill=WEISS, size=28, anker="m"),
    pl("250 € für den Schlüsseldienst", 720, 660, beim("bescheid", "zweihundertfünfzig"), fill=GELB, size=30, anker="m"),
    ficon("tabler", "lock-x", 1620, 560, 130, beim("schloss", "Schloss"), fuell=ROT),
    pl("Schloss kaputt", 1620, 590, KAPUTT, fill=ROT, size=28, anker="m"),
    *fig("BO", BOX, BODEN, FH, [("bescheid", "ruhig"), (beim("bescheid", "zweihundertfünfzig"), "staunt"), (KAPUTT, "sorge")],
         bis="bo2"),
    *redet("BO_redet", BOX, BODEN, FH, "bo2", "frage"),
    schild("Herr Böttcher", BOX, "bescheid", BO_F, unten=BODEN),
    blase("sprech", 640, 190, "bo2", 900, 260, inhalt=["Ich soll zahlen? Ich habe", "doch nur ferngesehen!"], textsize=32, figur=BOb),
])

# E Die Frage -----------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Durfte die Polizei hinein? Wer zahlt?")], [
    pl("Durfte die Polizei in die Wohnung?", 640, 90, beim("frage", "Durfte"), fill=PINK, size=42, anker="m"),
    ficon("ph", "door-open", 420, 560, 220, beim("frage", "Wohnung"), fuell=WEISS),
    ficon(HC, "clapper-board", 760, 520, 150, beim("frage", "Krimi"), fuell=WEISS),
    pl("obwohl nur ein Krimi lief", 640, 600, beim("frage", "obwohl"), fill=WEISS, size=32, anker="m"),
    pl("Wer trägt am Ende die Kosten?", 640, 740, beim("frage2", "Kosten"), fill=GELB, size=42, anker="m"),
    *fig("BO", FX, FB, FR, [("frage", "denkt")]),
    schild("Herr Böttcher", FX, "frage", BO_F),
])

# F Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Sonntagabend, kurz vor 23 Uhr, Nordrhein-Westfalen: Frau Jäger hört durch die Wand aus der Nachbarwohnung, wie eine Frau "
    "um Hilfe schreit. Dort lebt Herr Böttcher allein. Sie ruft die Polizei. Polizist Ahrens klingelt, klopft und ruft; "
    "niemand öffnet, hinter der Tür schreit es weiter. Ein Schlüsseldienst bricht im Auftrag der Polizei das Schloss auf. "
    "Drinnen sitzt Herr Böttcher vor dem Fernseher: Ein Krimi läuft so laut, dass er Klingel und Rufe nicht gehört hat. "
    "Wochen später verlangt das Polizeipräsidium 250 Euro für den Schlüsseldienst. Das Schloss ist kaputt.",
], "War das Betreten rechtmäßig? Wer trägt Kosten und Schaden?")

# G Landesrecht und zwei Ebenen ----------------------------------------------------------------------------------------------
folie([("land", "Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen"), ("ebenen", "Prüfung · zwei Ebenen")], rechts_frei([
    *tafel("land", "Polizeirecht ist Landesrecht"),
    z("Beispiel hier: Nordrhein-Westfalen", 110, 190, beim("land", "Nordrhein"), "Bold", 36),
    zit("PolG NRW (Fassung ab 13.12.2025), OBG NRW (ab 1.7.2026)", 150, 245, beim("land", "Beispiel")),
    z("andere Länder: eigene, ähnliche Regeln,", 110, 310, beim("land", "anderen"), size=34),
    z("oft unter anderer Nummer", 150, 365, beim("land", "Nummer"), size=34),
    z("Zwei Ebenen:", 110, 455, "ebenen", "Bold", 36),
    blk(110, 520, 1040, 85, BLAU, "prim", [("1. Ebene: War das Betreten rechtmäßig?", "ExtraBold", 36, INK)]),
    blk(110, 640, 1040, 85, GELB, "sek", [("2. Ebene: Wer zahlt am Ende?", "ExtraBold", 36, INK)]),
    ficon("tabler", "map", IX, IU, 150, "land", fuell=GRUEN, bis="prim"),
    ficon("ph", "door-open", IX, IU, 150, "prim", fuell=WEISS, bis="sek"),
    ficon("tabler", "file-euro", IX, IU, 140, "sek", fuell=GELB),
    *fig("AH", FX, FB, FR, [("land", "ruhig")]),
    schild("Polizist Ahrens", FX, "land", AH_F),
]))

# H 1. Ermächtigungsgrundlage: Wortlaut § 41 PolG NRW --------------------------------------------------------------------------
E1 = "1. Ebene: Betreten"
W41 = ("„Die Polizei kann eine Wohnung ohne Einwilligung des Inhabers betreten und durchsuchen, wenn … 4. das zur Abwehr "
       "einer gegenwärtigen Gefahr für Leib, Leben oder Freiheit einer Person oder für Sachen von bedeutendem Wert "
       "erforderlich ist.“")
Z41 = ["„Die Polizei kann eine Wohnung ohne Einwilligung des Inhabers",
       "betreten und durchsuchen, wenn …",
       "4. das zur Abwehr einer gegenwärtigen Gefahr für",
       "Leib, Leben oder Freiheit einer Person oder für Sachen",
       "von bedeutendem Wert erforderlich ist.“"]
w41, w41_y = wortlaut(80, 330, 1100, W41, "§ 41 Abs. 1 Satz 1 Nr. 4 PolG NRW", "wl41", marken=[
    ("ohne Einwilligung des Inhabers", beim("wl41", "ohne")), ("betreten", beim("wl41", "betreten")),
    ("gegenwärtigen Gefahr", beim("wl41", "gegenwärtigen")), ("Leib, Leben oder Freiheit einer Person", beim("wl41", "Leib")),
    ("erforderlich ist.", beim("wl41", "erforderlich"))], size=32, zeilen=Z41)
folie([("egl", f"{E1} › 1. Ermächtigungsgrundlage"), ("wl41", f"{E1} › 1. Ermächtigungsgrundlage, § 41 I 1 Nr. 4 PolG NRW"),
       ("nacht", f"{E1} › 1. Ermächtigungsgrundlage › Nachtzeit, § 41 II PolG NRW")], rechts_frei([
    titel(glyphen("1. Ermächtigungsgrundlage"), 110, 75, "egl", 50),
    nein(150, 188, beim("egl", "nicht"), gr=18),
    z("nicht die Generalklausel, § 8 I PolG NRW,", 195, 165, beim("egl", "nicht"), size=34),
    ok(150, 248, beim("egl", "Standardbefugnis"), gr=20),
    z("sondern die Standardbefugnis, § 41 PolG NRW", 195, 225, beim("egl", "Standardbefugnis"), "Bold", 34),
    zit("§ 8 Abs. 1 PolG NRW: „soweit nicht die §§ 9 bis 46 … besonders regeln“", 195, 280,
        beim("egl", "einundvierzig")),
    *w41,
    ok(150, w41_y + 63, beim("nacht", "nachts"), gr=20),
    z("§ 41 Abs. 2: auch nachts zulässig (Fälle Nr. 3 und 4)", 195, w41_y + 40, beim("nacht", "nachts"), "Bold", 32),
    ficon("ph", "door-open", IX, IU, 150, "egl", fuell=WEISS, bis="nacht"),
    ficon("tabler", "moon-stars", IX, IU, 130, "nacht", fuell=GELB),
    *fig("AH", FX, FB, FR, [("egl", "ruhig")]),
    schild("Polizist Ahrens", FX, "egl", AH_F),
]))

# I Art. 13 VII GG und formell ----------------------------------------------------------------------------------------------------
W137 = ("„Eingriffe und Beschränkungen dürfen im übrigen nur zur Abwehr einer gemeinen Gefahr oder einer Lebensgefahr für "
        "einzelne Personen, auf Grund eines Gesetzes auch zur Verhütung dringender Gefahren für die öffentliche Sicherheit "
        "und Ordnung … vorgenommen werden.“")
Z137 = ["„Eingriffe und Beschränkungen dürfen im übrigen nur zur",
        "Abwehr einer gemeinen Gefahr oder einer Lebensgefahr für",
        "einzelne Personen, auf Grund eines Gesetzes auch zur Verhütung",
        "dringender Gefahren für die öffentliche Sicherheit und Ordnung …",
        "vorgenommen werden.“"]
w137, w137_y = wortlaut(80, 260, 1100, W137, "Art. 13 Abs. 7 GG (Auslassung: Beispiele „insbesondere …“)", "wl13", marken=[
    ("Lebensgefahr", beim("wl13", "Lebensgefahr")), ("auf Grund eines Gesetzes", beim("wl13", "Grund")),
    ("dringender Gefahren", beim("wl13", "dringender"))], size=31, zeilen=Z137)
folie([("art13", f"{E1} › 1. Ermächtigungsgrundlage › Art. 13 VII GG"),
       ("formell", f"{E1} › 2. formell: Zuständigkeit, § 1 I PolG NRW")], rechts_frei([
    titel(glyphen("Art. 13 GG: Unverletzlichkeit der Wohnung"), 110, 75, "art13", 46),
    z("Das Betreten greift in Art. 13 Abs. 1 GG ein.", 110, 175, beim("art13", "greift"), "Bold", 34),
    *w137,
    ok(150, w137_y + 73, beim("formell", "zuständig"), gr=20),
    z("2. formell: Polizei zuständig für die Gefahrenabwehr,", 195, w137_y + 50, "formell", "Bold", 33),
    z("§ 1 Abs. 1 Satz 1 PolG NRW", 195, w137_y + 105, beim("formell", "Paragraf"), size=32),
    ficon("tabler", "home", IX, IU, 140, "art13", fuell=WEISS, bis="formell"),
    ficon(HC, "police-car-light", IX, IU, 130, "formell", fuell=BLAU),
    *fig("BO", FX, FB, FR, [("art13", "ruhig"), ("formell", "denkt")]),
    schild("Herr Böttcher", FX, "art13", BO_F),
]))

# J 3. materiell: Gefahr, Wortlaut § 8 I PolG NRW ---------------------------------------------------------------------------------
W8 = ("„Die Polizei kann die notwendigen Maßnahmen treffen, um eine im einzelnen Falle bestehende, konkrete Gefahr für die "
      "öffentliche Sicherheit oder Ordnung (Gefahr) abzuwehren, …“")
Z8 = ["„Die Polizei kann die notwendigen Maßnahmen treffen, um eine",
      "im einzelnen Falle bestehende, konkrete Gefahr für die",
      "öffentliche Sicherheit oder Ordnung (Gefahr) abzuwehren, …“"]
w8, w8_y = wortlaut(80, 150, 1100, W8, "§ 8 Abs. 1 PolG NRW (Legaldefinition „Gefahr“)", "wl8", marken=[
    ("im einzelnen Falle bestehende, konkrete Gefahr", beim("wl8", "einzelnen")),
    ("öffentliche Sicherheit oder Ordnung", beim("wl8", "öffentliche"))], size=32, zeilen=Z8)
folie([("gefahr", f"{E1} › 3. materiell: Gefahr, § 8 I PolG NRW"),
       ("gegenw", f"{E1} › 3. materiell: gegenwärtige Gefahr, § 41 I 1 Nr. 4")], rechts_frei([
    titel(glyphen("3. Materiell: die Gefahr"), 110, 75, "gefahr", 50),
    *w8,
    z("konkrete Gefahr: in absehbarer Zeit droht ein Schaden", 110, w8_y + 30, "wahrsch", "Bold", 33),
    z("mit hinreichender Wahrscheinlichkeit", 150, w8_y + 80, beim("wahrsch", "hinreichender"), size=33),
    z("je größer der Schaden, desto geringer die Anforderungen", 150, w8_y + 130, beim("wahrsch", "Je"), size=33),
    z("an die Wahrscheinlichkeit", 150, w8_y + 180, beim("wahrsch", "Anforderungen"), size=33),
    zit("OVG NRW, Urt. v. 5.7.2013 – 5 A 607/11, Rn. 153", 150, w8_y + 228, beim("wahrsch", "Wahrscheinlichkeit", nr=2)),
    z("gegenwärtig: Schädigung hat begonnen oder steht mit an", 110, w8_y + 290, "gegenw", "Bold", 33),
    z("Sicherheit grenzender Wahrscheinlichkeit unmittelbar bevor", 150, w8_y + 340, beim("gegenw", "Sicherheit"), size=33),
    zit("OVG NRW, Urt. v. 2.3.2021 – 5 A 942/19, Rn. 42", 150, w8_y + 388, beim("gegenw", "unmittelbar")),
    ficon(HC, "police-car-light", IX, IU, 130, "gefahr", fuell=BLAU),
    *fig("AH", FX, FB, FR, [("gefahr", "ruhig"), ("gegenw", "entschl")]),
    schild("Polizist Ahrens", FX, "gefahr", AH_F),
]))

# K Anscheinsgefahr -----------------------------------------------------------------------------------------------------------------
folie([("problem", f"{E1} › 3. materiell › keine Gefahr?"), ("exante", f"{E1} › 3. materiell › Anscheinsgefahr, ex ante")],
      rechts_frei([
    *tafel("problem", "Gar keine Gefahr, nur ein Krimi?"),
    pl("ex ante: im Moment des Einschreitens", 110, 175, beim("exante", "Entscheidend"), fill=GELB, size=32),
    z("Anscheinsgefahr: Objektive Tatsachen deuten für einen", 110, 270, "anschein", "Bold", 33),
    z("verständigen, besonnenen Beamten auf eine Gefahr hin", 150, 322, beim("anschein", "verständigen"), size=33),
    blk(110, 385, 1040, 75, GRUEN, beim("anschein", "echte"), [("Anscheinsgefahr = echte Gefahr", "ExtraBold", 34, INK)]),
    zit("OVG NRW, 7 A 1717/01, Rn. 99; OVG NRW, 15 A 3186/17, Rn. 109", 110, 475,
        beim("anschein", "echte")),
    ok(150, 568, beim("subs", "Hilfeschreie"), gr=18),
    z("Hilfeschreie einer Frau", 195, 545, beim("subs", "Hilfeschreie"), size=33),
    ok(150, 623, beim("subs", "allein"), gr=18),
    z("bei einem Mann, der allein wohnt", 195, 600, beim("subs", "allein"), size=33),
    ok(150, 678, beim("subs", "niemand"), gr=18),
    z("niemand öffnet", 195, 655, beim("subs", "niemand"), size=33),
    blk(110, 735, 1040, 75, GRUEN, beim("subs", "Lebensgefahr"), [("Ahrens durfte Lebensgefahr annehmen", "ExtraBold", 34, INK)]),
    ficon("ph", "eye", IX, IU, 140, "exante", fuell=WEISS),
    *fig("AH", FX, FB, FR, [("problem", "denkt"), ("subs", "entschl")]),
    schild("Polizist Ahrens", FX, "problem", AH_F),
]))

# L Abgrenzung: Putativgefahr und Gefahrenverdacht ------------------------------------------------------------------------------
folie([("schein", f"{E1} › 3. materiell › Abgrenzung: Putativgefahr"),
       ("verdacht", f"{E1} › 3. materiell › Abgrenzung: Gefahrenverdacht")], rechts_frei([
    *tafel("schein", "Abgrenzung", fill=ZARTROT),
    z("Putativgefahr (Scheingefahr):", 110, 180, beim("schein", "Putativgefahr"), "Bold", 36),
    z("Gefahr angenommen, ohne hinreichende Anhaltspunkte", 150, 235, beim("schein", "nimmt"), size=33),
    zit("VG Münster, Urt. v. 11.12.2006 – 1 K 3539/04, Rn. 27", 150, 285, beim("schein", "Anhaltspunkte")),
    z("klar Filmmusik und Werbung hörbar:", 150, 340, beim("schein2", "Filmmusik"), size=33),
    nein(190, 418, beim("schein2", "rechtswidrig"), gr=18),
    z("Gefahr nur eingebildet, Hineingehen rechtswidrig", 235, 395, beim("schein2", "eingebildet"), "Bold", 33),
    z("Gefahrenverdacht:", 110, 500, "verdacht", "Bold", 36),
    z("Gefahr möglich, aber die Polizei ist nicht sicher", 150, 555, beim("verdacht", "möglich"), size=33),
    z("Maßnahmen, die zur Aufklärung nötig sind", 150, 610, beim("verdacht", "Maßnahmen"), size=33),
    zit("OVG NRW, Urt. v. 7.8.2018 – 5 A 294/16, Rn. 37", 150, 660, beim("verdacht", "Aufklärung")),
    ficon("ph", "music-notes", 1450, 420, 110, beim("schein2", "Filmmusik"), fuell=GELB, bis="verdacht"),
    ficon("tabler", "ad", 1680, 420, 110, beim("schein2", "Werbung"), fuell=WEISS, bis="verdacht"),
    ficon("ph", "question", IX, IU, 140, "verdacht", fuell=GELB),
    *fig("AH", FX, FB, FR, [("schein", "denkt")]),
    schild("Polizist Ahrens", FX, "schein", AH_F),
]))

# M Verhältnismäßigkeit, Vollzug, Ergebnis der ersten Ebene ------------------------------------------------------------------------
folie([("verh", f"{E1} › Verhältnismäßigkeit, § 2 PolG NRW"),
       ("vollzug", f"{E1} › Vollzug: Ersatzvornahme, §§ 50 II, 52 PolG NRW"), ("erg1", "Ergebnis der ersten Ebene")],
      rechts_frei([
    *tafel("verh", "Verhältnismäßigkeit und Vollzug"),
    ok(150, 213, beim("verh", "geklingelt"), gr=20),
    z("erst geklingelt, geklopft und gerufen", 195, 190, beim("verh", "geklingelt"), "Bold", 34),
    zit("§ 2 PolG NRW (Grundsatz der Verhältnismäßigkeit)", 195, 245, beim("verh", "gerufen")),
    z("Schloss öffnen lassen: Ersatzvornahme", 110, 330, "vollzug", "Bold", 34),
    z("im sofortigen Vollzug, §§ 50 Abs. 2, 52 PolG NRW", 150, 385, beim("vollzug", "sofortigen"), size=33),
    zit("vgl. VG Köln, Gerichtsbescheid v. 11.2.2016 – 20 K 6403/14, Rn. 48–50", 150, 435, beim("vollzug", "fünfzig")),
    blk(110, 520, 1040, 85, GRUEN, beim("erg1", "rechtmäßig"), [("Ergebnis 1. Ebene: Betreten rechtmäßig", "ExtraBold", 38, INK)]),
    ficon("ph", "toolbox", IX, IU, 150, "vollzug", fuell=GELB, bis="erg1"),
    ficon("tabler", "shield-check", IX, IU, 140, "erg1", fuell=GRUEN),
    *fig("AH", FX, FB, FR, [("verh", "ruhig"), ("erg1", "froh")]),
    schild("Polizist Ahrens", FX, "verh", AH_F),
]))

# N 2. Ebene: Kosten -------------------------------------------------------------------------------------------------------------
E2 = "2. Ebene"
folie([("ebene2", f"{E2} · Kosten › Maßstab ex post"), ("kosten", f"{E2} · Kosten, § 52 I PolG NRW"),
       ("zurech", f"{E2} · Kosten › Anscheinsstörer")], rechts_frei([
    *tafel("ebene2", "2. Ebene: Kosten"),
    pl("ex post: wie es wirklich war", 110, 175, beim("expost", "wirklich"), fill=GELB, size=32),
    zit("OVG NRW, Beschl. v. 14.6.2000 – 5 A 95/00, Rn. 19, 21", 110, 255, beim("expost", "post")),
    z("Ersatzvornahme nach § 52 Abs. 1 PolG NRW:", 110, 320, "kosten", "Bold", 34),
    z("„auf Kosten der betroffenen Person“", 150, 375, beim("kosten", "Kosten"), size=34),
    z("Anscheinsstörer zahlt nur, wenn er die Umstände", 110, 465, "zurech", "Bold", 34),
    z("des Anscheins selbst zu verantworten hat", 150, 520, beim("zurech", "verantworten"), size=34),
    zit("OVG NRW, Beschl. v. 14.6.2000 – 5 A 95/00, Rn. 15, 23", 150, 570, beim("zurech", "verantworten")),
    ficon("tabler", "file-euro", IX, IU, 140, "ebene2", fuell=GELB),
    *fig("BO", FX, FB, FR, [("ebene2", "ruhig"), ("zurech", "denkt")]),
    schild("Herr Böttcher", FX, "ebene2", BO_F),
]))

# O 2. Ebene: Kosten – Herr Böttcher ---------------------------------------------------------------------------------------------
folie([("bo_subs", f"{E2} · Kosten › Herr Böttcher")], rechts_frei([
    *tafel("bo_subs", "Hat Herr Böttcher den Anschein zu verantworten?", size=40),
    z("Krimi so laut gestellt, dass", 110, 190, beim("bo_subs", "Krimi"), "Bold", 34),
    z("die Nachbarin Hilfeschreie hörte", 150, 245, beim("bo_subs", "Nachbarin"), size=34),
    z("und er selbst weder Klingel noch Polizei", 150, 300, beim("bo_subs", "weder"), size=34),
    ok(150, 393, beim("zahlt", "Verantwortungsbereich"), gr=20),
    z("liegt in seinem Verantwortungsbereich", 195, 370, beim("zahlt", "Verantwortungsbereich"), "Bold", 34),
    blk(110, 470, 1040, 85, GELB, beim("zahlt", "zahlen"), [("Vieles spricht dafür: Er zahlt die 250 €", "ExtraBold", 36, INK)]),
    ficon("ph", "television", 1420, 330, 150, "bo_subs", fuell=BLAU),
    ficon("ph", "speaker-high", 1640, 300, 90, beim("bo_subs", "laut"), fuell=ROT),
    *fig("BO", FX, FB, FR, [("bo_subs", "denkt"), ("zahlt", "muede")]),
    schild("Herr Böttcher", FX, "bo_subs", BO_F),
]))

# P 2. Ebene: Entschädigung, Wortlaut § 39 I OBG NRW --------------------------------------------------------------------------
W39 = ("„Ein Schaden, den jemand durch Maßnahmen der Ordnungsbehörden erleidet, ist zu ersetzen, wenn er a) infolge einer "
       "Inanspruchnahme nach § 19 oder b) durch rechtswidrige Maßnahmen, gleichgültig, ob die Ordnungsbehörden ein "
       "Verschulden trifft oder nicht, entstanden ist.“")
Z39 = ["„Ein Schaden, den jemand durch Maßnahmen der Ordnungsbehörden",
       "erleidet, ist zu ersetzen, wenn er",
       "a) infolge einer Inanspruchnahme nach § 19 oder",
       "b) durch rechtswidrige Maßnahmen, gleichgültig, ob die",
       "Ordnungsbehörden ein Verschulden trifft oder nicht,",
       "entstanden ist.“"]
w39, w39_y = wortlaut(80, 215, 1100, W39, "§ 39 Abs. 1 OBG NRW, über § 67 PolG NRW", beim("wl39", "Danach"), marken=[
    ("ist zu ersetzen,", beim("wl39", "ersetzen")), ("infolge einer Inanspruchnahme nach § 19", beim("wl39", "Inanspruchnahme")),
    ("durch rechtswidrige Maßnahmen,", beim("wl39", "rechtswidrige"))], size=29, zeilen=Z39)
folie([("entsch", f"{E2} · Entschädigung, § 67 PolG NRW, § 39 I OBG NRW"),
       ("analog", f"{E2} · Entschädigung › Anscheinsstörer wie Nichtstörer")], rechts_frei([
    titel(glyphen("Und das kaputte Schloss?"), 110, 75, "entsch", 50),
    z("§ 67 PolG NRW: §§ 39 bis 43 OBG NRW entsprechend", 110, 160, beim("wl39", "siebenundsechzig"), "Bold", 32),
    *w39,
    zit("§ 19 OBG NRW: Inanspruchnahme nicht verantwortlicher Personen (Nichtstörer)", 110, w39_y + 8,
        beim("wl39", "Nichtstörer")),
    nein(150, w39_y + 78, beim("rechtm", "Rechtswidrig"), gr=18),
    z("b) rechtswidrig war hier nichts", 195, w39_y + 55, beim("rechtm", "Rechtswidrig"), size=32),
    z("a) analog: Anscheinsstörer ohne Verantwortung", 110, w39_y + 115, "analog", "Bold", 32),
    z("wird wie ein Nichtstörer entschädigt", 150, w39_y + 165, beim("analog", "Nichtstörer"), size=32),
    zit("OVG NRW, 5 A 95/00, Rn. 15; OLG Köln, Urt. v. 26.1.1995 – 7 U 146/94, Rn. 20", 150, w39_y + 210,
        beim("analog", "entschädigt")),
    nein(150, w39_y + 283, beim("bo_ent", "verantworten"), gr=18),
    z("Herr Böttcher: zu verantworten, geht leer aus", 195, w39_y + 260, beim("bo_ent", "verantworten"), "Bold", 32),
    ficon("tabler", "lock-x", IX, IU, 130, "entsch", fuell=ROT),
    *fig("BO", FX, FB, FR, [("entsch", "sorge"), (beim("bo_ent", "leer"), "muede")]),
    schild("Herr Böttcher", FX, "entsch", BO_F),
]))

# Q Gegenfall: OLG Köln, Zeitschaltuhr ---------------------------------------------------------------------------------------
GF = "Gegenfall · OLG Köln"
folie([("gegen", f"{GF}: Zeitschaltuhr"), ("olg", f"{GF} › Entschädigung, § 39 I a OBG NRW"),
       ("mitv", f"{GF} › Mitverschulden, § 40 IV OBG NRW")], rechts_frei([
    *tafel("gegen", "Gegenfall: ein echter Fall", fill=ZARTROT),
    zit("OLG Köln, Urt. v. 26.1.1995 – 7 U 146/94, NRWE Rn. 5, 13–24, 30–40", 110, 165, beim("gegen", "Oberlandesgerichts")),
    z("Familie im Urlaub, eine Zeitschaltuhr", 110, 220, beim("gegen", "Familie"), size=34),
    z("schaltet abends den Fernseher ein", 150, 275, beim("gegen", "abends"), size=34),
    z("Nachbarn vermuten einen Einbrecher,", 110, 345, "gegen2", size=34),
    z("die Polizei bricht die Tür auf", 150, 400, beim("gegen2", "bricht"), size=34),
    ok(150, 493, beim("olg", "Entschädigung"), gr=20),
    z("Entschädigung zugesprochen", 195, 470, beim("olg", "Entschädigung"), "Bold", 34),
    z("Zeitschaltuhr: nur mittelbare Ursache", 195, 525, beim("olg", "mittelbare"), size=34),
    z("Mitverschulden: hätte die Nachbarn einweihen müssen", 110, 610, "mitv", "Bold", 33),
    blk(110, 680, 1040, 85, ROT, beim("mitv", "Drittel"), [("nur ein Drittel, § 40 Abs. 4 OBG NRW", "ExtraBold", 36, INK)]),
    ficon("ph", "suitcase-rolling", 1380, 330, 120, beim("gegen", "Urlaub"), fuell=GELB),
    ficon("ph", "timer", 1580, 330, 120, beim("gegen", "Zeitschaltuhr"), fuell=WEISS),
    ficon("ph", "television", 1770, 330, 140, beim("gegen", "Fernseher"), fuell=BLAU),
    ficon("tabler", "door", 1450, 760, 170, "gegen2", fuell=WEISS, bis=beim("gegen2", "bricht")),
    ficon("ph", "door-open", 1450, 760, 170, beim("gegen2", "bricht"), fuell=WEISS),
    ficon(HC, "balance-scale", 1700, 760, 170, "olg", fuell=GELB),
]))

# R Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Ebenen trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne die Ebenen:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("Rechtmäßigkeit ex ante,", 200, 270, "tipp1", size=34),
    z("Kosten und Entschädigung ex post", 200, 325, beim("tipp1", "Kosten"), size=34),
    z("Standardbefugnis vor Generalklausel", 200, 420, "tipp2", "Bold", 34),
    zit("§ 8 Abs. 1 PolG NRW: „soweit nicht die §§ 9 bis 46 … besonders regeln“", 200, 475, beim("tipp2", "Generalklausel")),
    z("Entschädigung: ordentliche Gerichte,", 200, 560, "tipp3", "Bold", 34),
    z("§ 43 Abs. 1 OBG NRW (über § 67 PolG NRW)", 200, 615, beim("tipp3", "Paragraf"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ------------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anscheinsgefahr"), 110, 90, "sch", 48),
    z("A. Primärebene (ex ante): Rechtmäßigkeit des Betretens", K1, 185, "q1", "Bold", 38, rechts=1820),
    z("1. Ermächtigungsgrundlage: § 41 Abs. 1 Satz 1 Nr. 4 PolG NRW (vor § 8 I)", K2, 255, "q2", size=SZ, rechts=1820),
    z("2. formell: Zuständigkeit, § 1 Abs. 1 PolG NRW", K2, 315, "q3", size=SZ, rechts=1820),
    z("3. materiell: gegenwärtige Gefahr für Leib oder Leben", K2, 375, "q4", size=SZ, rechts=1820),
    z("Anscheinsgefahr genügt, Putativgefahr nicht", K3, 430, beim("q4", "Anscheinsgefahr"), size=SZ, rechts=1820),
    z("dann: Ermessen und Verhältnismäßigkeit, §§ 2, 3 PolG NRW", K3, 485, "q5", size=SZ, rechts=1820),
    z("B. Sekundärebene (ex post)", K1, 575, "q6", "Bold", 38, rechts=1820),
    z("Kosten, § 52 Abs. 1 PolG NRW: nur bei zu verantwortendem Anschein", K2, 640, beim("q6", "Kosten"), size=SZ, rechts=1820),
    z("Entschädigung wie ein Nichtstörer, § 67 PolG NRW i. V. m. § 39 Abs. 1 a OBG NRW", K2, 700, "q7", size=SZ,
      rechts=1820),
    z("gemindert bei Mitverschulden, § 40 Abs. 4 OBG NRW", K3, 755, beim("q7", "gemindert"), size=SZ, rechts=1820),
])

# T Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Über die Maßnahme entscheidet", 0)], [("der ", 0), ("Anschein", "a"), (",", 0)],
                 [("über die Kosten die ", 0), ("Wirklichkeit", "b"), (".", 0)]],
                750, 300, 46, "merke", {"a": beim("merke", "Anschein"), "b": beim("merke", "Wirklichkeit")}),
    *markertext([[("Wer den Anschein nicht zu verantworten", 0)], [("hat, zahlt nicht und wird wie ein", 0)],
                 [("Nichtstörer ", 0), ("entschädigt", "c"), (".", 0)]],
                750, 580, 46, "m2", {"c": beim("m2", "entschädigt")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
