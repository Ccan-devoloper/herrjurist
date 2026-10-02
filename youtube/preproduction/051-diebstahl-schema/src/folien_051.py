"""Folge 051 · Diebstahl § 242 Schema: Wegnahme & Zueignungsabsicht – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Lesesaal (Fall), B Sachverhalt (Grundfall, drei Varianten), C Wortlaut § 242 I und
Aufbau, D fremde bewegliche Sache, E Wegnahme/Gewahrsam, F gelockerter Gewahrsam (Gegenfall Handy auf der Straße),
G Bruch und neuer Gewahrsam (Gewahrsamsenklave), H Vorsatz (Variante 1), I Zueignungsabsicht, J Gebrauchsanmaßung
(Variante 2), K Rechtswidrigkeit der Zueignung (Variante 3), L Ergebnis und § 248a, M Ausblick § 243,
N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche: nur Handlungsgeräusche – Stecker aus der Steckdose (szene_051stecker_1) und Reißverschluss des Rucksacks
(szene_051reissv_1), beide im Fall, wenn Matthias das Kabel sichtbar herauszieht und einsteckt."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_051/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobile Lesbarkeit: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def zitat(text, x, y, cue, size=26, **k):
    """BGH-Fundstelle unter einer Aussage (klein, grau, mindestens 26 px)."""
    return z(text, x, y, cue, "Bold", size, farbe=TEXT, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (zweizeilige Blöcke bleiben im Kasten)."""
    for t_, *_ in zeilen:
        glyphen(t_)
        assert F(_[0], _[1]).getlength(t_) <= w - 40, f"Block zu breit: {t_}"
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def umbruch(text, breite, size):
    f = F("Regular", size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter die Wortgruppe (sie muss in einer Zeile stehen)."""
    zeilen = umbruch(text, w - 60, size)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
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


def sachverhalt_klein(cue, absaetze, frage, size=34, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber Schrift passend zu Grundfall und drei Varianten."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 14
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


# --- Eigene Hilfsfunktion (wie Folge 029/035/042/047): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


# --- Figuren und Namensschilder ----------------------------------------------------------------------------------------
NAMEN = {"AN": ("Antje", GRUEN), "MA": ("Matthias", LILA)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
AX, MX = 1420, 1740                         # Antje links, Matthias rechts
PY = 420                                    # Pillen über den Köpfen


def name(p, cx, cue, unten=BR, size=28, d=0.0, bis=None, anim="cut"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def kabel(cx, unten, breite, cue, bis=None, anim="pop", fuell=WEISS):
    """Das Ladekabel als Stecker-Icon (tabler: plug)."""
    return ficon("tabler", "plug", cx, unten, breite, cue, fuell=fuell, bis=bis, anim=anim)


def paar(cue, an_folge, ma_folge, ax=AX, mx=MX):
    """Antje und Matthias rechts neben der Tafel, je mit Namensschild ab Folienbeginn."""
    return [*fig("AN", ax, BR, FR, an_folge, erst="cut"), name("AN", ax, cue),
            *fig("MA", mx, BR, FR, ma_folge, erst="cut"), name("MA", mx, cue)]


def steckdose(x, y, cue, bis=None):
    """Steckdose an der Tischfront (Karte mit zwei Löchern)."""
    els = [hart(karte(x, y, 58, 58, cue, fill=WEISS, rund=14, schatten=0, rand=4))]
    for dx in (18, 32):
        els.append(hart(karte(x + dx, y + 24, 9, 9, cue, fill=INK, rund=4, schatten=0, rand=0)))
    for e in els:
        e.bis = bis
    return els


# A Fall: Lesesaal der Unibibliothek -------------------------------------------------------------------------------------
BA = 900                                    # Boden im Lesesaal
SH = 560                                    # Standhöhe im Fall
ANX, MAX_, MAG = 530, 1530, 1060            # Antje am Tisch, Matthias am Nachbartisch, Matthias zwischen den Tischen
TA = (300, 650, 460, 250)                   # Tisch von Antje
TM = (1300, 650, 460, 250)                  # Nachbartisch
SD = (690, 700)                             # Steckdose an der Tischfront von Antje
KAB = [(628, 640), (668, 646), (700, 668), (712, 700), (719, 724)]   # Kabel vom Tisch in die Steckdose
MAb = ("MA_redet", MAX_, BA, SH)
ANb = ("AN_redet", ANX, BA, SH)
folie([(NULL, "Fall · Der Lesesaal"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(80, BA + 2), (1840, BA + 2)], NULL, breite=6, farbe=INK)),
    pl("Donnerstagnachmittag", 100, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Lesesaal · Unibibliothek", 100, 140, beim("fall", "Lesesaal"), fill=WEISS, size=30),
    # Antje am Tisch (Tischfront verdeckt die Beine)
    *fig("AN", ANX, BA, SH, [(beim("antje", "Antje"), "denkt")], bis="kaffee"),
    *fig("AN", ANX, BA, SH, [("zurueck", "ruhig")], bis="a1"),
    *redet("AN_redet", ANX, BA, SH, "a1", "frage"),
    *fig("AN", ANX, BA, SH, [("frage", "erschrickt"), ("frage2", "denkt")], erst="cut"),
    hart(karte(*TA, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    hart(ficon("tabler", "lamp", 345, TA[1], 80, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "books", 450, TA[1], 90, NULL, fuell=BLAU, anim="cut")),
    name("AN", ANX, beim("antje", "Antje"), unten=TA[1] + 70, anim="pop", bis="kaffee"),
    name("AN", ANX, "zurueck", unten=TA[1] + 70, anim="pop"),
    pl("lernt für die Klausur", ANX, 250, beim("antje", "lernt"), fill=WEISS, size=28, anker="m", bis="kaffee"),
    # Handy lädt am Kabel in der Steckdose
    *steckdose(*SD, NULL),
    ficon("tabler", "device-mobile-charging", 615, TA[1], 76, "kabel", fuell=GRUEN, bis="kaffee"),
    bis_(linienzug(KAB, "kabel", breite=7, farbe=INK), "steckt"),
    pl("Ladekabel · 15 €", 900, 600, beim("kabel", "Ladekabel"), fill=GELB, size=28, anker="m", bis="matthias"),
    kabel(600, TA[1], 48, "kaffee", bis="steckt"),
    # Antje kurz in der Cafeteria
    ficon("tabler", "coffee", 160, 330, 90, beim("kaffee", "Cafeteria"), fuell=GELB, bis="zurueck"),
    pl("kurz in der Cafeteria", 220, 262, beim("kaffee", "Cafeteria"), fill=WEISS, size=28, bis="zurueck"),
    pl("Kabel, Jacke und Bücher bleiben", 300, 420, beim("kaffee", "Kabel"), fill=WEISS, size=28, bis="steckt"),
    # Matthias am Nachbartisch
    *fig("MA", MAX_, BA, SH, [(beim("matthias", "Matthias"), "ruhig"), (beim("matthias", "Akku"), "listig")], bis="m1"),
    *redet("MA_redet", MAX_, BA, SH, "m1", "steckt"),
    hart(karte(*TM, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    hart(ficon("tabler", "lamp", 1715, TM[1], 80, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "book", 1400, TM[1], 80, NULL, fuell=WEISS, anim="cut")),
    ficon("tabler", "battery-1", 1590, TM[1], 80, beim("matthias", "Akku"), fuell=ROT),
    name("MA", MAX_, beim("matthias", "Matthias"), unten=TM[1] + 70, anim="pop", bis="steckt"),
    pl("Akku fast leer", 1530, 190, beim("matthias", "Akku"), fill=PINK, size=28, anker="m", bis="m1"),
    pl("eigenes Kabel zu Hause", 1530, 262, beim("matthias", "eigenes"), fill=WEISS, size=28, anker="m", bis="m1"),
    blase("sprech", 660, 210, "m1", 1060, 250, inhalt=["Das nehme ich mir", "einfach mit."], textsize=36,
          figur=MAb, bis="steckt"),
    # Matthias zieht das Kabel heraus und steckt es in den Rucksack (Stecker, Reißverschluss)
    *(lambda l: [szene(l[0], "051stecker*", 0.7, 0.15)] + l[1:])(
        fig("MA", MAG, BA, SH, [("steckt", "entschlossen"), ("heim", "entschlossen_r")], bis="zurueck")),
    name("MA", MAG, "steckt", unten=BA - 6, bis="zurueck"),
    szene(bis_(ficon("tabler", "backpack", 845, BA, 100, beim("steckt", "Rucksack"), fuell=BLAU), "zurueck"),
          "051reissv*", 0.8),
    bis_(kabel(845, BA - 108, 46, beim("steckt", "Rucksack")), "zurueck"),
    pl("in den Rucksack", 1060, 200, beim("steckt", "Rucksack"), fill=PINK, size=28, anker="m", bis="heim"),
    ficon("tabler", "home", 1060, 190, 80, "heim", fuell=GELB, bis="zurueck"),
    pl("will es behalten", 1060, 230, beim("heim", "behalten"), fill=PINK, size=28, anker="m", bis="zurueck"),
    pl("zehn Minuten später", 220, 262, "zurueck", fill=WEISS, size=28, bis="frage"),
    blase("sprech", 560, 200, "a1", 1000, 260, inhalt=["Wo ist denn mein", "Ladekabel?"], textsize=36,
          figur=ANb, bis="frage"),
    # Frage
    pl("Hat Matthias einen Diebstahl begangen?", 1150, 260, "frage", fill=PINK, size=36, anker="m"),
    pl("§ 242 Schritt für Schritt", 990, 350, beim("frage2", "Paragraf"), fill=WEISS, size=30, anker="m"),
    pl("drei Varianten", 1390, 350, beim("frage2", "drei"), fill=GELB, size=30, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Donnerstagnachmittag im Lesesaal der Unibibliothek: Antje lädt ihr Handy an einem weißen Ladekabel (Wert 15 Euro), "
    "das in der Steckdose an ihrem Tisch steckt. Sie geht kurz in die Cafeteria und nimmt das Handy mit; Kabel, Jacke "
    "und Bücher bleiben am Platz. Matthias vom Nachbartisch, dessen Akku fast leer ist, zieht das Kabel aus der "
    "Steckdose, steckt es in seinen Rucksack und nimmt es mit nach Hause, um es zu behalten.",
    "Variante 1: Matthias besitzt ein gleiches weißes Kabel und glaubt, er habe es am Morgen dort vergessen. Er hält "
    "das Kabel von Antje für seines.",
    "Variante 2: Matthias will das Kabel nur über Nacht benutzen und am nächsten Morgen an Antjes Platz zurücklegen.",
    "Variante 3: Antje hat Matthias genau dieses Kabel gestern verkauft. Er hat bezahlt, und sie hat zugesagt, es ihm "
    "heute zu übergeben.",
], "Hat sich Matthias nach § 242 StGB strafbar gemacht?")

# C Wortlaut § 242 I und Aufbau ---------------------------------------------------------------------------------------
T242 = ("„Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten "
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“")
wl242, y242 = wortlaut(90, 170, 1090, T242, "§ 242 Abs. 1 StGB", "p242", size=32,
                       marken=[("fremde bewegliche Sache", beim("p242w", "fremde")),
                               ("wegnimmt", beim("p242w", "wegnimmt")),
                               ("rechtswidrig zuzueignen", beim("p242w", "rechtswidrig"))])
folie([("p242", "§ 242 StGB › Wortlaut und Aufbau")], [
    *tafel("p242", "Diebstahl, § 242 StGB", h=y242 + 36 + 200 + 40 - 60),
    *wl242,
    blk(110, y242 + 36, 505, 200, GRUEN, beim("obj", "objektiven"), [("objektiver Tatbestand", "ExtraBold", 31, INK),
                                                                      ("fremde bewegliche", "Bold", 30, INK),
                                                                      ("Sache, Wegnahme", "Bold", 30, INK)]),
    blk(645, y242 + 36, 505, 200, BLAU, "subj", [("subjektiver Tatbestand", "ExtraBold", 31, INK),
                                                  ("Vorsatz, Absicht rechts-", "Bold", 30, INK),
                                                  ("widriger Zueignung", "Bold", 30, INK)]),
    *paar("p242", [("p242", "ruhig"), ("obj", "denkt")], [("p242", "ruhig"), ("subj", "denkt")]),
    kabel(1580, 330, 110, beim("p242w", "fremde"), fuell=WEISS),
])

# D Fremde bewegliche Sache ------------------------------------------------------------------------------------------
PO = "I. Tatbestand › 1. objektiv"
folie([("sache", f"{PO} › a) fremde bewegliche Sache")], [
    *tafel("sache", "Fremde bewegliche Sache", h=620),
    ok(135, 213, beim("sache2", "Sache"), gr=22), z("Sache: körperlicher Gegenstand, § 90 BGB", 175, 190, "sache2", size=34),
    ok(135, 293, beim("bewegl", "wegtragen"), gr=22), z("beweglich: Matthias kann es wegtragen", 175, 270, "bewegl", size=34),
    ok(135, 373, beim("fremd", "Antje"), gr=22), z("fremd: gehört nach bürgerlichem Recht Antje", 175, 350, "fremd", size=34),
    zitat("BGH, Beschl. v. 10.10.2018 – 4 StR 591/17, Rn. 6", 175, 405, beim("fremd", "Antje")),
    blk(110, 480, 1040, 80, GELB, beim("fremd", "nicht"), [("fremde bewegliche Sache (+)", "ExtraBold", 36, INK)]),
    *paar("sache", [("sache", "ruhig"), ("fremd", "froh")], [("sache", "ruhig"), ("bewegl", "listig")]),
    kabel(1580, 330, 120, "sache2", fuell=WEISS),
    pl("körperlicher Gegenstand", 1580, PY - 60, "sache2", fill=WEISS, size=28, anker="m", bis="fremd"),
    pl("gehört Antje", 1580, PY - 60, beim("fremd", "Antje"), fill=GRUEN, size=28, anker="m"),
])

# E Wegnahme und Gewahrsam -------------------------------------------------------------------------------------------
folie([("wegn", f"{PO} › b) Wegnahme"), ("gew", f"{PO} › b) Wegnahme › Gewahrsam")], [
    *tafel("wegn", "Wegnahme", h=640),
    z("Bruch fremden und Begründung neuen Gewahrsams", 110, 190, beim("wegn2", "Bruch"), "Bold", 34),
    zitat("BGH, Beschl. v. 3.3.2021 – 4 StR 338/20, Rn. 5", 110, 240, beim("wegn2", "Gewahrsams")),
    blk(110, 310, 1040, 72, GELB, "gew", [("Gewahrsam", "ExtraBold", 34, INK)]),
    z("vom Herrschaftswillen getragene", 110, 405, beim("gew", "Herrschaftswillen"), size=34),
    z("tatsächliche Sachherrschaft", 110, 452, beim("gew", "tatsächliche"), "Bold", 34),
    z("beurteilt nach den Anschauungen des täglichen Lebens", 110, 520, "verkehr", size=33),
    zitat("BGH 4 StR 338/20, Rn. 8", 110, 570, beim("verkehr", "täglichen")),
    *paar("wegn", [("wegn", "ruhig"), ("gew", "denkt")], [("wegn", "ruhig"), ("wegn2", "denkt"), ("verkehr", "listig")]),
    ficon("tabler", "hand-grab", 1580, 300, 100, beim("gew", "tatsächliche"), fuell=WEISS),
    kabel(1660, 330, 70, beim("gew", "tatsächliche"), fuell=WEISS),
])

# F Gelockerter Gewahrsam, Gegenfall Handy auf der Straße ------------------------------------------------------------
TF = (1290, 700, 380, 200)                  # Tisch von Antje (klein)
folie([("weg", f"{PO} › b) Wegnahme › gelockerter Gewahrsam")], [
    *tafel("weg", "Gelockerter Gewahrsam", h=800),
    z("Antje ist gar nicht da?", 110, 185, "weg", "Bold", 34),
    z("Gewahrsam besteht gelockert fort,", 110, 250, "locker", size=34),
    z("etwa: Landwirt lässt Geräte auf dem Feld", 110, 297, beim("locker", "Landwirt"), size=34),
    zitat("BGH, Beschl. v. 14.4.2020 – 5 StR 10/20, Rn. 7", 110, 347, beim("locker", "Feld")),
    ok(135, 433, beim("antjeok", "Gewahrsam"), gr=22),
    z("Antje: nur kurz weg, Platz besetzt", 175, 410, "antjeok", "Bold", 34),
    z("Gegenfall: Handy nachts auf der Straße verloren", 110, 510, "strasse", size=33),
    z("Besitzer fort, keine Einwirkung möglich", 110, 557, beim("strasse", "fort"), size=33),
    nein(135, 643, "fund", gr=20), z("kein Gewahrsam: nur Unterschlagung, § 246", 175, 620, "fund", "Bold", 34),
    zitat("BGH 5 StR 10/20, Rn. 5–8", 175, 670, beim("fund", "Unterschlagung")),
    # rechts: der leere Platz von Antje im Lesesaal
    hart(karte(*TF, "weg", fill=WEISS, rund=14, schatten=6, rand=5, anim="cut")),
    hart(ficon("tabler", "books", 1360, TF[1], 80, "weg", fuell=BLAU, anim="cut")),
    hart(kabel(1480, TF[1], 46, "weg")),
    hart(linienzug([(1500, 690), (1540, 700), (1572, 730), (1580, 760)], "weg", breite=6, farbe=INK)),
    *steckdose(1560, 755, "weg"),
    pl("Platz besetzt", 1480, 560, beim("antjeok", "Platz"), fill=GELB, size=28, anker="m"),
    *fig("AN", 1770, BR, FR, [("antjeok", "froh")], bis="strasse"),
    name("AN", 1770, "antjeok", bis="strasse"),
    ficon("tabler", "coffee", 1770, 440, 70, "antjeok", fuell=GELB, bis="strasse"),
    # Landwirt mit Gerät auf dem Feld
    ficon("tabler", "tractor", 1560, 330, 130, beim("locker", "Landwirt"), fuell=GRUEN, bis="strasse"),
    hart(bis_(linienzug([(1330, 332), (1800, 332)], beim("locker", "Feld"), breite=6, farbe=INK), "strasse")),
    # Gegenfall: Handy nachts auf der Straße
    ficon("tabler", "moon", 1820, 170, 70, "strasse", fuell=GELB),
    hart(linienzug([(1330, 452), (1860, 452)], "strasse", breite=6, farbe=INK)),
    ficon("tabler", "device-mobile", 1560, 450, 64, beim("strasse", "Handy"), fuell=WEISS),
    pl("verloren", 1560, 300, beim("strasse", "verloren"), fill=WEISS, size=28, anker="m"),
    pl("nur Unterschlagung", 1560, 220, "fund", fill=PINK, size=28, anker="m"),
])

# G Bruch und neuer Gewahrsam: Gewahrsamsenklave ---------------------------------------------------------------------
RX_ = 1500                                  # Rucksack
folie([("bruch", f"{PO} › b) Wegnahme › Bruch und neuer Gewahrsam")], [
    *tafel("bruch", "Bruch und neuer Gewahrsam", h=820),
    z("Gewahrsam ohne den Willen von Antje aufgehoben:", 110, 185, "bruch", size=33),
    ok(135, 263, beim("bruch", "Bruch"), gr=22), z("Bruch", 175, 240, beim("bruch", "Bruch"), "Bold", 34),
    z("neuer Gewahrsam: Kabel in den Rucksack gesteckt", 110, 320, "neu", "Bold", 33),
    pl("schon im Lesesaal", 110, 375, "lesesaal", fill=GELB, size=30),
    z("kleine, leicht bewegliche Sachen in der eigenen", 110, 455, "enklave", size=33),
    z("Tasche: auch im fremden Herrschaftsbereich", 110, 500, beim("enklave", "fremden"), size=33),
    blk(110, 560, 520, 72, GELB, beim("enklave", "Gewahrsamsenklave"), [("Gewahrsamsenklave", "ExtraBold", 34, INK)]),
    zitat("BGH 5 StR 593/18, Rn. 4 f. · BGH 2 StR 145/13, Rn. 3", 110, 650, beim("enklave", "Gewahrsamsenklave")),
    blk(110, 705, 1040, 80, GRUEN, "wegok", [("Wegnahme vollendet: obj. Tatbestand erfüllt", "ExtraBold", 33, INK)]),
    *fig("MA", MX, BR, FR, [("bruch", "entschlossen"), ("enklave", "listig"), ("wegok", "froh")], erst="cut"),
    name("MA", MX, "bruch"),
    ficon("tabler", "backpack", RX_, BR, 120, "bruch", fuell=BLAU),
    kabel(RX_, 520, 60, "bruch", bis=beim("neu", "Rucksack")),
    kabel(RX_, BR - 132, 52, beim("neu", "Rucksack")),
    ring(RX_, BR - 80, 105, 120, beim("enklave", "Gewahrsamsenklave")),
    ficon("tabler", "books", 1380, 300, 90, "bruch", fuell=WEISS),
    pl("Lesesaal", 1380, 330, "lesesaal", fill=WEISS, size=28, anker="m"),
])

# H Vorsatz (Variante 1) -----------------------------------------------------------------------------------------------
PS_ = "I. Tatbestand › 2. subjektiv"
MAd = ("MA_denkt", MX, BR, FR)
folie([("vors", f"{PS_} › a) Vorsatz"), ("v1", f"{PS_} › a) Vorsatz › Variante 1")], [
    *tafel("vors", "Vorsatz", h=640),
    z("Matthias weiß: Das Kabel gehört Antje,", 110, 190, "vors2", size=34),
    ok(135, 260, beim("vors2", "nehmen"), gr=22), z("und er will es nehmen", 175, 237, beim("vors2", "will"), size=34),
    z("Variante 1: gleiches Kabel, glaubt, er habe es", 110, 320, "v1", "Bold", 33),
    z("dort vergessen: hält es für sein eigenes", 150, 367, beim("v1", "hält"), "Bold", 33),
    z("kennt die Fremdheit nicht", 110, 440, "v1b", size=34),
    nein(135, 523, "v1ok", gr=20), z("§ 16 Abs. 1 StGB: ohne Vorsatz", 175, 500, "v1ok", "ExtraBold", 36),
    *paar("vors", [("vors", "ruhig"), ("v1", "denkt"), ("v1ok", "froh")],
          [("vors", "listig"), ("v1", "denkt"), ("v1b", "staunt"), ("v1ok", "froh")]),
    kabel(1580, 330, 90, "vors2", fuell=WEISS, bis="v1"),
    blase("denk", 420, 230, "v1", 1530, 230, figur=MAd, bis="v1ok"),
    kabel(1460, 290, 64, beim("v1", "gleiches"), fuell=WEISS, bis="v1ok"),
    kabel(1600, 290, 64, beim("v1", "gleiches"), fuell=WEISS, bis="v1ok"),
    pl("sein eigenes?", 1530, 330, beim("v1", "hält"), fill=GELB, size=28, anker="m", bis="v1ok"),
])

# I Zueignungsabsicht --------------------------------------------------------------------------------------------------
SL, SR2, SW = 110, 645, 505
folie([("zueig", f"{PS_} › b) Zueignungsabsicht")], [
    *tafel("zueig", "Zueignungsabsicht: zwei Teile", h=760),
    blk(SL, 180, SW, 70, BLAU, "aneig", [("Aneignung", "ExtraBold", 34, INK)]),
    z("Absicht: zielgerichtet wollen,", SL + 10, 270, beim("aneig", "zielgerichtet"), size=30, rechts=SL + SW),
    z("direkter Vorsatz 1. Grades", SL + 10, 312, beim("aneig", "direkter"), "Bold", 30, rechts=SL + SW),
    z("Kabel dem Vermögen einver-", SL + 10, 380, "aneig2", size=30, rechts=SL + SW),
    z("leiben, wie ein Eigentümer", SL + 10, 422, beim("aneig2", "wie"), size=30, rechts=SL + SW),
    z("darüber verfügen", SL + 10, 464, beim("aneig2", "Eigentümer"), size=30, rechts=SL + SW),
    zitat("BGH 3 StR 536/18, Rn. 16 f.", SL + 10, 515, beim("aneig2", "verfügen"), rechts=SL + SW),
    blk(SR2, 180, SW, 70, LILA, "enteig", [("Enteignung", "ExtraBold", 34, INK)]),
    z("bedingter Vorsatz genügt", SR2 + 10, 270, beim("enteig", "bedingter"), "Bold", 30, rechts=SR2 + SW),
    z("nimmt in Kauf: Antje", SR2 + 10, 338, beim("enteig", "nimmt"), size=30, rechts=SR2 + SW),
    z("verliert ihr Kabel auf Dauer", SR2 + 10, 380, beim("enteig", "Dauer"), size=30, rechts=SR2 + SW),
    zitat("BGH 3 StR 148/18, Rn. 7", SR2 + 10, 431, beim("enteig", "verliert"), rechts=SR2 + SW),
    ok(135, 643, "zueigok", gr=22),
    blk(175, 600, 975, 80, GRUEN, "zueigok", [("Grundfall: will es behalten – beides (+)", "ExtraBold", 33, INK)]),
    *paar("zueig", [("zueig", "ruhig"), ("enteig", "erschrickt"), ("zueigok", "denkt")],
          [("zueig", "ruhig"), ("aneig2", "froh"), ("enteig", "listig")]),
    ficon("tabler", "home", 1740, 330, 110, "aneig2", fuell=GELB),
    kabel(1740, 300, 44, "aneig2", fuell=WEISS),
    pl("auf Dauer weg", 1420, PY - 60, beim("enteig", "Dauer"), fill=PINK, size=28, anker="m"),
])

# J Gebrauchsanmaßung (Variante 2) -------------------------------------------------------------------------------------
MAe = ("MA_ehrlich", MX, BR, FR)
folie([("v2", f"{PS_} › b) Zueignungsabsicht › Variante 2")], [
    *tafel("v2", "Variante 2: Gebrauchsanmaßung", size=44, h=720),
    z("nur über Nacht benutzen", 110, 185, beim("v2", "nur"), "Bold", 34),
    z("fester Rückgabewille schon bei der Wegnahme:", 110, 270, "v2b", size=34),
    z("nur den Gebrauch angemaßt", 110, 317, beim("v2b", "maßt"), "Bold", 34),
    zitat("BGH, Beschl. v. 13.8.2025 – 4 StR 308/25, Rn. 6", 110, 367, beim("v2b", "Gebrauch")),
    nein(135, 453, "v2c", gr=20), z("kein Enteignungsvorsatz, keine Zueignungsabsicht", 175, 430, "v2c", size=33),
    blk(110, 520, 1040, 80, GELB, "v2ok", [("Gebrauchsanmaßung: kein Diebstahl", "ExtraBold", 36, INK)]),
    *fig("AN", AX, BR, FR, [("v2", "ruhig"), ("v2b", "froh")], erst="cut"), name("AN", AX, "v2"),
    *fig("MA", MX, BR, FR, [("v2", "ruhig")], bis="m2", erst="cut"),
    *redet("MA_ehrlich", MX, BR, FR, "m2", "v2b"),
    *fig("MA", MX, BR, FR, [("v2b", "froh")], erst="cut"),
    name("MA", MX, "v2"),
    ficon("tabler", "moon", 1580, 330, 90, beim("v2", "Nacht"), fuell=GELB, bis="m2"),
    kabel(1700, 330, 70, beim("v2", "benutzen"), fuell=WEISS, bis="m2"),
    blase("sprech", 520, 200, "m2", 1500, 240, inhalt=["Morgen früh lege", "ich es zurück."], textsize=36,
          figur=MAe, bis="v2b"),
    ficon("tabler", "moon", 1450, 330, 80, "v2b", fuell=GELB),
    pfeil_ink(1510, 290, 1640, 290, "v2b"),
    kabel(1700, 330, 64, "v2b", fuell=WEISS),
    pl("zurück an den Platz", 1580, PY - 60, beim("v2b", "zurückzugeben"), fill=GRUEN, size=28, anker="m"),
])

# K Rechtswidrigkeit der erstrebten Zueignung (Variante 3) -----------------------------------------------------------
folie([("rwz", f"{PS_} › b) Zueignungsabsicht › Rechtswidrigkeit der Zueignung"),
       ("v3", f"{PS_} › b) Zueignungsabsicht › Rechtswidrigkeit › Variante 3")], [
    *tafel("rwz", "Rechtswidrigkeit der Zueignung", size=44, h=820),
    z("erstrebte Zueignung muss rechtswidrig sein,", 110, 180, "rwz", size=33),
    z("der Vorsatz muss sich darauf erstrecken", 110, 225, "rwz2", size=33),
    zitat("BGH, Beschl. v. 28.10.2025 – 3 StR 458/25, Rn. 5 f.", 110, 272, beim("rwz2", "erstrecken")),
    z("rechtswidrig ohne fälligen, durchsetzbaren", 110, 335, "rwz3", "Bold", 33),
    z("Anspruch gerade auf diese Sache", 110, 380, beim("rwz3", "Anspruch"), "Bold", 33),
    z("Variante 3: Kabel gestern gekauft, bezahlt,", 110, 455, "v3", "Bold", 33),
    z("Übergabe für heute zugesagt", 150, 500, beim("v3", "zugesagt"), size=33),
    ok(135, 583, "v3b", gr=22), z("Anspruch aus Kaufvertrag, § 433 Abs. 1 BGB:", 175, 560, "v3b", size=33),
    z("fällig und einredefrei", 175, 605, beim("v3b", "fälligen"), "Bold", 33),
    nein(135, 693, "v3ok", gr=20),
    z("Zueignung nicht rechtswidrig: kein Diebstahl", 175, 670, "v3ok", "ExtraBold", 34),
    *paar("rwz", [("rwz", "ruhig"), ("v3", "froh_r"), ("v3ok", "denkt")],
          [("rwz", "ruhig"), ("v3", "froh"), ("v3b", "denkt"), ("v3ok", "froh")]),
    ficon("tabler", "receipt", 1480, 330, 90, beim("v3", "verkauft"), fuell=WEISS),
    ficon("tabler", "cash", 1660, 330, 100, beim("v3", "bezahlt"), fuell=GRUEN),
    pl("bezahlt", 1660, PY - 60, beim("v3", "bezahlt"), fill=GRUEN, size=28, anker="m"),
    pl("Anspruch auf dieses Kabel", 1580, 140, "v3b", fill=GELB, size=28, anker="m"),
])

# L Ergebnis und § 248a ------------------------------------------------------------------------------------------------
folie([("erg", "Grundfall › II. Rechtswidrigkeit, III. Schuld › Ergebnis"),
       ("p248a", "Grundfall › Strafantrag, § 248a StGB")], [
    *tafel("erg", "Ergebnis und Strafantrag", h=760),
    ok(135, 208, beim("erg", "keinen"), gr=22), z("Grundfall: kein Anspruch auf das Kabel", 175, 185, "erg", size=34),
    ok(135, 278, "rs", gr=22), z("Rechtswidrigkeit und Schuld liegen vor", 175, 255, "rs", size=34),
    blk(110, 325, 1040, 80, GRUEN, "erg2", [("Matthias: Diebstahl, § 242 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    z("Ladekabel für 15 €: geringwertig", 110, 450, "p248a", "Bold", 34),
    z("§ 248a: nur auf Antrag verfolgt", 110, 497, beim("p248a", "Paragraf"), size=34),
    zitat("BGH, Beschl. v. 9.7.2004 – 2 StR 176/04, Rn. 3", 110, 545, beim("p248a", "verfolgt")),
    z("außer: besonderes öffentliches Interesse", 110, 610, "oeff", size=34),
    *paar("erg", [("erg", "ruhig"), ("erg2", "froh"), ("p248a", "denkt")],
          [("erg", "ruhig"), ("erg2", "ertappt"), ("p248a", "sorge")]),
    ficon("tabler", "coin", 1580, 330, 90, "p248a", fuell=GELB),
    pl("15 €", 1580, PY - 60, "p248a", fill=WEISS, size=28, anker="m"),
    ficon("tabler", "signature", 1420, 220, 80, beim("p248a", "Antrag"), fuell=WEISS),
])

# M Ausblick § 243 -----------------------------------------------------------------------------------------------------
folie([("p243", "Ausblick › besonders schwerer Fall, § 243 StGB")], [
    *tafel("p243", "Ausblick: § 243 StGB", h=700),
    z("Regelbeispiele, z. B.:", 110, 185, "p243b", "Bold", 34),
    z("Einbrechen in ein Gebäude", 150, 235, beim("p243b", "Einbrechen"), size=34),
    z("gewerbsmäßiges Stehlen", 150, 285, beim("p243b", "gewerbsmäßiges"), size=34),
    blk(110, 350, 1040, 120, LILA, beim("p243b", "keine"), [("keine Tatbestandsmerkmale,", "ExtraBold", 34, INK),
                                                            ("sondern Strafzumessungsregeln", "ExtraBold", 34, INK)]),
    zitat("BGH, Urt. v. 7.8.2001 – 1 StR 470/00, Rn. 11", 110, 485, beim("p243b", "Strafzumessungsregeln")),
    nein(135, 583, "p243c", gr=20), z("geringwertige Sache: kein besonders schwerer", 175, 560, "p243c", "Bold", 33),
    z("Fall nach Nr. 1 bis 6, § 243 Abs. 2", 175, 605, beim("p243c", "Nummern"), "Bold", 33),
    *paar("p243", [("p243", "ruhig"), ("p243c", "froh")], [("p243", "ruhig"), ("p243b", "denkt")]),
    ficon("tabler", "building", 1500, 330, 100, beim("p243b", "Einbrechen"), fuell=WEISS),
    ficon("tabler", "briefcase", 1680, 330, 90, beim("p243b", "gewerbsmäßiges"), fuell=GELB),
])

# N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zueignung gehört in den subjektiven Tatbestand")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, beim("tipp", "Prüfe"), gr=26),
    z("Zueignung nie im objektiven Tatbestand prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("Sie muss nicht gelingen, nur beabsichtigt sein", 110, 290, "tipp2", size=34),
    zitat("BGH, Beschl. v. 10.10.2018 – 4 StR 591/17, Rn. 17", 110, 340, beim("tipp2", "beabsichtigen")),
    blk(110, 410, 1040, 120, GELB, "tipp3", [("Aneignung: Absicht", "ExtraBold", 34, INK),
                                              ("Enteignung: Vorsatz", "ExtraBold", 34, INK)]),
    z("Gebrauchsanmaßung? Wollte er die Sache", 110, 580, "tipp4", "Bold", 34),
    z("unverändert zurückgeben?", 110, 627, beim("tipp4", "unverändert"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m"),
    kabel(1790, 330, 80, "tipp4", fuell=WEISS),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 250
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Diebstahl, § 242 Abs. 1 StGB", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 180, "s_i", "ExtraBold", 38, rechts=1820),
    z("1. objektiv: fremde bewegliche Sache", K2, 236, "s1a", "Bold", 34, rechts=1820),
    z("Wegnahme: Bruch fremden und Begründung neuen Gewahrsams", K3, 286, "s1b", size=34, rechts=1820),
    z("2. subjektiv: Vorsatz", K2, 346, "s1c", "Bold", 34, rechts=1820),
    z("Absicht rechtswidriger Zueignung:", K3, 396, "s1d", size=34, rechts=1820),
    z("Aneignungsabsicht, Enteignungsvorsatz,", K3 + 40, 444, beim("s1d", "Aneignungsabsicht"), size=34, rechts=1820),
    z("Rechtswidrigkeit der Zueignung", K3 + 40, 492, beim("s1d", "Rechtswidrigkeit"), size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 560, "s_ii", "ExtraBold", 38, rechts=1820),
    z("III. Schuld", K1, 625, "s_iii", "ExtraBold", 38, rechts=1820),
    z("IV. Strafzumessung: besonders schwerer Fall, § 243", K1, 690, "s_iv", "ExtraBold", 38, rechts=1820),
    z("V. Strafantrag bei geringwertigen Sachen, § 248a", K1, 755, "s_v", "ExtraBold", 38, rechts=1820),
])

# P Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 140, "merke", 80, anker="m"),
    *markertext([[("Wegnahme", "a"), (": fremden Gewahrsam brechen", 0)], [("und neuen begründen; nur kurz weg", 0)],
                 [("und in der Nähe: gelockert.", 0)]], 750, 250, 38, "merke", {"a": beim("merke", "Wegnahme")}),
    *markertext([[("Zueignungsabsicht", "b"), (": Aneignung gewollt,", 0)], [("Enteignung in Kauf genommen.", 0)]],
                750, 480, 38, "m_2", {"b": beim("m_2", "Zueignungsabsicht")}),
    *markertext([[("Fester Rückgabewille", "c"), (" beim Nehmen:", 0)], [("kein Diebstahl.", 0)]], 750, 660, 38, "m_3",
                {"c": beim("m_3", "fest")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m"),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
