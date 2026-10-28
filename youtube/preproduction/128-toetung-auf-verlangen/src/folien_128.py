"""Folge 128 · Tötung auf Verlangen § 216 oder Suizidhilfe? Der Gisela-Fall – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Hedwig ist schwer krank und bittet ihren Mann Wilfried ausdrücklich, ihr beim Sterben zu helfen; er führt den
tödlichen Schritt selbst aus, sie kann danach nichts mehr ändern. Gegenvariante: Sie geht den letzten Schritt selbst.
ZURÜCKHALTUNG (Thema Suizid, wie 094): keine Methode, keine Mittel, Spritzen, Becher oder Fahrzeuge im Bild; als neutrales
Symbol für die Herrschaft über den letzten Schritt dient ein Schlüssel, für „danach nichts mehr zu ändern“ ein Schloss.
Hedwig erscheint nach ihrem Tod nicht mehr als Figur; die Beteiligten des Gisela-Falls und des Falls von 2022 erscheinen
nicht als Figuren (nur Gerichtsgebäude, Akten, Jahreszahlen).
Szenen laut ../SZENENPLAN.md: A1 Wohnzimmer (Bitte, letzter Schritt), A2 In derselben Nacht, A3 Anklage und Frage,
B Sachverhalt, C1 1. Ausgangspunkt, C2 Wortlautkarte § 216 Abs. 1, D 2. Abgrenzungskriterium, E Gisela-Fall,
F1 3. BGH 2022, F2 Recht auf selbstbestimmtes Sterben, G 4. Merkmale, H 5. Zweispalter und Ergebnis, I Klausurtipp (Lexi),
J Klausurschema, K Merksatz (Lexi), L Hilfsangebot (Telefonseelsorge).
Keine Geräusche (keine sichtbare Handlung, die ein Handlungsgeräusch tragen sollte; ruhiger Ton).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/spalte als eigene Kopie aus Folge 125 (gemeinsame
Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarte wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_128/"

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e)
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (246, 243, 255, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (Mindestgröße 26 px, mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    lh = int(max(g for _, _, g, _ in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=lh, rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_128/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil der Tafel (Diagramm), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 094/125) ----------------------------------------
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


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


FB, FR = 930, 480                           # Figur neben der Tafel: Unterkante, Höhe
FX = 1640                                   # eine Figur neben der Tafel
IX = 1380                                   # Requisit links neben der Figur (x ≥ 1250)
PY = 150                                    # Pillenhöhe über den Figuren
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HE_N, WF_N = GRUEN, BLAU                    # Farben der Namensschilder


def wilfried(c0, folge, bis=None):
    """Wilfried allein rechts neben der Tafel, blickt zur Tafel (nach links), Namensschild durchgehend."""
    return [*fig("WF", FX, FB, FR, folge, bis=bis), ns("Wilfried", FX, FB, c0, WF_N, d=0.1, bis=bis)]


def requisit(folge, x=IX + 120, y=PY, unten=380, bis_ende=None):
    """Wechselnde Pille (und Icon) über bzw. neben der Figur: folge = [(cue, (set, icon, breite, fuell) | None, text, farbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, IX, unten, br, c, fuell=fu, bis=b, anim="pop" if i == 0 else "cut"))
        if txt:
            els.append(pl(txt, x, y, c, fill=pf, size=30, anker="m", bis=b, anim="pop" if i == 0 else "cut"))
    return els


# ===========================================================================================================================
# A1 Fall: Wohnzimmer – die Bitte, der letzte Schritt
# ===========================================================================================================================
BODEN, GH = 880, 520
HEX, WFX = 600, 1320                        # Hedwig links (blickt nach rechts), Wilfried rechts (blickt nach links)
MX = (HEX + WFX) // 2
HEa = ("HE_redet_r", HEX, BODEN, GH)
TAT = beim("tat", "führt")
folie([(NULL, "Fall · Hedwig und Wilfried"), ("bitte", "Fall · Die Bitte"), ("tat", "Fall · Der letzte Schritt")], [
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Hedwig und Wilfried", 70, 30, NULL, fill=GELB, size=40)),
    ficon("tabler", "sofa", 250, BODEN, 300, NULL, fuell=LILA, anim="cut"),
    ficon("tabler", "lamp", 1760, BODEN, 150, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "window", MX, 470, 190, NULL, fuell=BLAUHELL, anim="cut"),
    ficon("tabler", "plant-2", 1560, BODEN, 110, NULL, fuell=GRUEN, anim="cut"),
    *fig("HE", HEX, BODEN, GH, [(NULL, "muede_r"), ("klar", "ernst_r")], erst="cut", bis="h1"),
    *redet("HE_redet_r", HEX, BODEN, GH, "h1", "tat"),
    *fig("HE", HEX, BODEN, GH, [("tat", "still_r")], erst="cut"),
    hart(ns("Hedwig", HEX, BODEN, NULL, HE_N)),
    *fig("WF", WFX, BODEN, GH, [(NULL, "ernst"), ("bitte", "sorge"), (TAT, "still")], erst="cut"),
    hart(ns("Wilfried", WFX, BODEN, NULL, WF_N)),
    pl("schwer krank", HEX, 290, beim("fall", "schwer"), fill=WEISS, size=30, anker="m", bis="h1"),
    pl("Schmerzen werden stärker", HEX, 220, beim("fall", "Schmerzen"), fill=ROTHELL, size=30, anker="m", bis="h1"),
    ficon("tabler", "calendar-event", MX, 690, 110, "bitte", fuell=WEISS, bis="tat"),
    pl("seit Monaten", MX, 720, beim("bitte", "Seit"), fill=WEISS, size=28, anker="m", bis="tat"),
    pl("bittet ihn ausdrücklich um Hilfe beim Sterben", 960, 120, beim("bitte", "ausdrücklich"), fill=WEISS, size=30,
       anker="m", bis="h1"),
    pl("lange und klar überlegt", 1150, 200, "klar", fill=GELB, size=30, anker="m", bis="h1"),
    blase("sprech", 640, 220, "h1", 1050, 190, inhalt=["Ich habe es mir gut überlegt.", "Bitte hilf mir."], textsize=34,
          figur=HEa, bis="tat"),
    ficon("tabler", "key", WFX + 170, 330, 90, TAT, fuell=GELB),
    pl("führt den tödlichen Schritt selbst aus", 1100, 120, TAT, fill=GELB, size=30, anker="m"),
    ficon("tabler", "lock", HEX - 170, 330, 80, "danach", fuell=WEISS),
    pl("danach nichts mehr zu ändern", 700, 195, beim("danach", "nichts"), fill=ROTHELL, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: In derselben Nacht (Hedwig nicht mehr im Bild)
# ===========================================================================================================================
folie([("stirbt", "Fall · In derselben Nacht")], [
    linienzug([(40, BODEN), (1880, BODEN)], "stirbt", breite=7, farbe=INK),
    ficon("tabler", "window", 760, 520, 260, "stirbt", fuell=BLAUHELL),
    ficon("tabler", "moon", 760, 455, 80, "stirbt", fuell=GELB),
    ficon("tabler", "candle", 760, BODEN, 110, "stirbt", fuell=WEISS),
    pl("in derselben Nacht", 70, 30, "stirbt", fill=GELB, size=40),
    pl("Hedwig stirbt.", 760, 600, beim("stirbt", "stirbt"), fill=WEISS, size=34, anker="m"),
    *fig("WF", 1400, BODEN, GH, [("stirbt", "still")]),
    ns("Wilfried", 1400, BODEN, "stirbt", WF_N, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: Die Anklage und die Frage
# ===========================================================================================================================
WFA = 1400
folie([("anklage", "Fall · Die Anklage"), ("frage", "Fall · Die Frage")], [
    linienzug([(40, BODEN), (1880, BODEN)], "anklage", breite=7, farbe=INK),
    ficon("fluent-emoji-flat", "classical-building", 380, BODEN, 360, "anklage"),
    pl("Staatsanwaltschaft", 380, 390, beim("anklage", "Staatsanwaltschaft"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "folder", 830, BODEN, 150, beim("anklage", "klagt"), fuell=GELB),
    pl("Anklage", 830, 640, beim("anklage", "klagt"), fill=WEISS, size=30, anker="m"),
    *fig("WF", WFA, BODEN, GH, [("anklage", "ernst")], bis="w1"),
    *redet("WF_redet", WFA, BODEN, GH, "w1", "frage"),
    *fig("WF", WFA, BODEN, GH, [("frage", "still")], erst="cut"),
    ns("Wilfried", WFA, BODEN, "anklage", WF_N, d=0.1),
    blase("sprech", 720, 190, "w1", 1060, 200, inhalt=["Ich habe nur getan,", "worum sie mich gebeten hat."], textsize=34,
          figur=("WF_redet", WFA, BODEN, GH), bis="frage"),
    pl("Tötung auf Verlangen, § 216 StGB?", 960, 140, "frage", fill=PINK, size=36, anker="m"),
    pl("letzten Schritt Hedwig überlassen: straflos?", 960, 225, "frage2", fill=PINK, size=36, anker="m"),
    ficon("tabler", "key", 1700, 380, 90, "frage2", fuell=GELB),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_128(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_128("sv", [
    "Hedwig ist schwer krank, ihre Schmerzen werden immer stärker. Seit Monaten bittet sie ihren Mann Wilfried "
    "ausdrücklich, ihr beim Sterben zu helfen; sie hat es sich lange und klar überlegt. Wilfried handelt nur, weil sie ihn "
    "darum bittet.",
    "Eines Abends gibt Wilfried nach und führt den tödlichen Schritt selbst aus. Hedwig kann danach nichts mehr ändern und "
    "stirbt in derselben Nacht. Die Staatsanwaltschaft klagt Wilfried an.",
    "Gegenvariante: Wilfried bereitet alles vor, den letzten Schritt geht Hedwig selbst.",
], "Tötung auf Verlangen, § 216 StGB, oder straflose Suizidhilfe?")

# ===========================================================================================================================
# C1 1. Ausgangspunkt: Selbsttötung straflos, Tötung eines anderen strafbar
# ===========================================================================================================================
P1 = "1. Ausgangspunkt"
folie([("aus", f"{P1} › Selbsttötung straflos"), ("p212", f"{P1} › Tötung eines anderen, § 212 StGB")], rechts_frei([
    *tafel("aus", P1),
    z("Selbsttötung: kein Tötungstatbestand", 110, 190, beim("aus", "Wer"), "Bold", 36),
    zit("BGHSt 63, 161 Rn. 18", 110, 245, beim("aus", "Tötungstatbestand")),
    z("auch die Hilfe dazu: straflos", 110, 315, "teiln", "Bold", 36),
    zit("vgl. Folge 094 (Sirius-Fall)", 110, 370, beim("teiln", "Folge")),
    z("Tötung eines anderen: § 212 StGB", 110, 460, "p212", "Bold", 36),
    z("strafbar, auch wenn das Opfer es will", 110, 515, beim("p212", "auch"), size=34),
    *wilfried("aus", [("aus", "ernst"), ("p212", "still")]),
    *requisit([(beim("aus", "Wer"), None, "Selbsttötung: straflos", WEISS), ("teiln", None, "vgl. Folge 094", GELB),
               ("p212", None, "§ 212 StGB", WEISS)], x=FX),
]))

# ===========================================================================================================================
# C2 Wortlautkarte § 216 Abs. 1 StGB
# ===========================================================================================================================
W216 = ["„(1) Ist jemand durch das ausdrückliche und ernstliche Verlangen",
        "des Getöteten zur Tötung bestimmt worden, so ist auf Freiheitsstrafe",
        "von sechs Monaten bis zu fünf Jahren zu erkennen.“"]
w216, w216_y = wortlaut(110, 175, 1040, W216, "§ 216 Abs. 1 StGB", "p216", marken=[
    (0, "ausdrückliche und ernstliche Verlangen", beim("p216", "ausdrückliche")),
    (1, "zur Tötung bestimmt", beim("p216", "bestimmt")),
    (2, "von sechs Monaten bis zu fünf Jahren", beim("strafe", "sechs"))], size=30)
folie([("p216", f"{P1} › § 216 Abs. 1 StGB"), ("priv", f"{P1} › Privilegierung des Totschlags")], rechts_frei([
    *tafel("p216", "§ 216 Abs. 1 StGB: Tötung auf Verlangen"),
    *w216,
    z("statt mindestens 5 Jahren (§ 212 Abs. 1 StGB)", 110, w216_y + 30, beim("strafe", "statt"), "Bold", 34),
    blk(110, w216_y + 110, 1040, 90, GELB, "priv", [("§ 216 StGB privilegiert den Totschlag", "ExtraBold", 34, INK)]),
    z("die Grenze zur straflosen Suizidhilfe entscheidet", 110, w216_y + 240, "grenze", "Bold", 34),
    *wilfried("p216", [("p216", "still"), ("grenze", "ernst")]),
    *requisit([("p216", ("tabler", "scale", 120, WEISS), "§ 216 StGB", GELB),
               ("strafe", ("tabler", "scale", 120, WEISS), "6 Monate bis 5 Jahre", WEISS),
               ("grenze", ("tabler", "arrows-split-2", 120, WEISS), "Täter oder Suizidhilfe?", PINK)], x=FX),
]))

# ===========================================================================================================================
# D 2. Abgrenzungskriterium: Wer beherrscht den letzten Akt?
# ===========================================================================================================================
P2 = "2. Abgrenzung"
folie([("krit", f"{P2} › Wer beherrscht den letzten Akt?"), ("f119", f"{P2} › Tatherrschaft, vgl. Folge 119")], rechts_frei([
    *tafel("krit", "2. Abgrenzungskriterium"),
    z("Wer beherrscht das zum Tod führende", 110, 190, beim("krit", "Entscheidend"), "Bold", 36),
    z("Geschehen zuletzt?", 110, 240, beim("krit", "Geschehen"), "Bold", 36),
    z("der letzte, unwiderrufliche Akt", 110, 310, "letzt", size=34),
    z("Tatherrschaft (vgl. Folge 119)", 110, 370, "f119", size=34),
    blk(110, 450, 1040, 140, ROTHELL, "hand", [("Sterbewilliger gibt sich in die Hand des anderen:", "ExtraBold", 31, INK),
                                               ("der andere hat die Tatherrschaft", "ExtraBold", 31, INK)]),
    blk(110, 620, 1040, 140, GRUENHELL, "selbst", [("freie Entscheidung bis zuletzt:", "ExtraBold", 31, INK),
                                                   ("er tötet sich selbst, mit fremder Hilfe", "ExtraBold", 31, INK)]),
    zit("BGHSt 63, 161 Rn. 18; BGH 6 StR 68/21 Rn. 14 (st. Rspr.)", 110, 785, beim("selbst", "Hilfe")),
    *wilfried("krit", [("krit", "ernst"), ("hand", "still")]),
    *requisit([(beim("krit", "zuletzt"), None, "zuletzt beherrscht?", WEISS), ("letzt", ("tabler", "key", 100, GELB), "letzter Akt", GELB),
               ("f119", ("tabler", "key", 100, GELB), "Tatherrschaft", WEISS),
               ("hand", ("tabler", "key", 100, GELB), "beim anderen", ROTHELL),
               ("selbst", ("tabler", "key", 100, GELB), "beim Sterbewilligen", GRUENHELL)], x=FX),
]))

# ===========================================================================================================================
# E Gisela-Fall, BGHSt 19, 135 (keine Figuren; keine Methode)
# ===========================================================================================================================
GX = 1580
folie([("gis", f"{P2} › Gisela-Fall, BGHSt 19, 135"), ("gis4", f"{P2} › Gisela-Fall: Tatherrschaft"),
       ("rg", f"{P2} › subjektive Sicht verworfen")], rechts_frei([
    *tafel("gis", "Der Gisela-Fall (1963)"),
    z("BGH, Urteil vom 14.8.1963 – 2 StR 181/63", 110, 180, beim("gis", "Bundesgerichtshof"), "Bold", 32),
    zit("BGHSt 19, 135, 139 f.", 110, 228, beim("gis", "Gisela-Fall")),
    z("gemeinsamer Plan: zusammen aus dem Leben scheiden", 110, 290, "gis2", size=32),
    z("nach dem Plan: er hat den letzten Schritt in der Hand", 110, 342, beim("gis2", "Nach"), size=32),
    z("sie starb, er überlebte", 110, 394, "gis3", size=32),
    z("zunächst freigesprochen", 110, 460, "gis4", size=32, farbe=TEXT),
    *okz("BGH: Freispruch aufgehoben, er hatte die Tatherrschaft", 512, beim("gis4", "hob"), "Bold", 32),
    z("anfangs noch Rettung möglich, aber sein Beitrag", 185, 570, "gis5", size=30),
    z("lief bis zuletzt weiter", 185, 612, beim("gis5", "denn"), size=30),
    *neinz("Reichsgericht: Tat als eigene gewollt? verworfen", 690, "rg", "Bold", 32),
    zit("Wiedergabe nach BGH 6 StR 68/21 Rn. 18 f. (BGHSt 19, 135, 138 ff.)", 110, 770, beim("rg", "verwarf")),
    ficon("fluent-emoji-flat", "classical-building", GX, 560, 260, "gis"),
    pl("Bundesgerichtshof", GX, 610, beim("gis", "Bundesgerichtshof"), fill=WEISS, size=30, anker="m"),
    pl("1963", GX, 680, beim("gis", "neunzehnhundertdreiundsechzig"), fill=GELB, size=34, anker="m"),
    pl("Gisela-Fall", GX, 150, beim("gis", "Gisela-Fall"), fill=GELB, size=34, anker="m", bis="gis4"),
    pl("Freispruch aufgehoben", GX, 150, beim("gis4", "hob"), fill=GRUEN, size=30, anker="m", anim="cut", bis="rg"),
    pl("Reichsgericht: verworfen", GX, 150, "rg", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "folder", GX, 870, 110, "gis2", fuell=WEISS),
]))

# ===========================================================================================================================
# F1 3. Neuere Rechtsprechung: BGH 2022 (keine Figuren; keine Methode)
# ===========================================================================================================================
P3 = "3. Neuere Rechtsprechung"
folie([("neu", f"{P3} › BGH, 6 StR 68/21 (2022)"), ("norm", f"{P3} › normative Betrachtung"),
       ("plan", f"{P3} › Gesamtplan"), ("frei", f"{P3} › straflose Suizidhilfe")], rechts_frei([
    *tafel("neu", "3. Neuere Rechtsprechung"),
    z("BGH, Beschluss vom 28.6.2022 – 6 StR 68/21", 110, 180, beim("neu", "Zweitausendzweiundzwanzig"), "Bold", 32),
    z("Ehefrau hilft ihrem schwerkranken Mann,", 110, 240, "neu2", size=32),
    z("auf seinen Wunsch, beim Sterben", 110, 284, beim("neu2", "auf"), size=32),
    z("Hauptteil: er selbst; ihr aktiver Beitrag: Absicherung", 110, 336, beim("neu2", "Den"), size=32),
    blk(110, 410, 1040, 140, GELB, "norm", [("normative Betrachtung: Ob jemand aktiv", "ExtraBold", 32, INK),
                                          ("handelt, entscheidet nicht allein.", "ExtraBold", 32, INK)]),
    *okz("Gesamtplan: ein Akt, über den allein er bestimmte", 580, "plan", "Bold", 31),
    *okz("danach: Er hätte noch Hilfe holen lassen können.", 640, "nach", "Bold", 31),
    blk(110, 710, 1040, 80, GRUENHELL, "frei", [("straflose Suizidhilfe: Freispruch", "ExtraBold", 32, INK)]),
    zit("6 StR 68/21 Rn. 13, 15–17", 110, 805, beim("frei", "B.G.H")),
    ficon("fluent-emoji-flat", "classical-building", GX, 560, 260, "neu"),
    pl("Bundesgerichtshof", GX, 610, beim("neu", "B.G.H"), fill=WEISS, size=30, anker="m"),
    pl("2022", GX, 680, beim("neu", "Zweitausendzweiundzwanzig"), fill=GELB, size=34, anker="m"),
    pl("6 StR 68/21", GX, 150, beim("neu", "Zweitausendzweiundzwanzig"), fill=WEISS, size=30, anker="m", bis="norm"),
    pl("normativ", GX, 150, "norm", fill=GELB, size=30, anker="m", anim="cut", bis="plan"),
    pl("Gesamtplan", GX, 150, "plan", fill=WEISS, size=30, anker="m", anim="cut", bis="frei"),
    pl("Freispruch", GX, 150, "frei", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "folder", GX, 870, 110, "neu2", fuell=WEISS),
]))

# ===========================================================================================================================
# F2 Recht auf selbstbestimmtes Sterben, Verfassungsfrage offen
# ===========================================================================================================================
folie([("bverfg", f"{P3} › Recht auf selbstbestimmtes Sterben"), ("offen", f"{P3} › § 216 einschränken? offen")], rechts_frei([
    *tafel("bverfg", "Recht auf selbstbestimmtes Sterben"),
    blk(110, 180, 1040, 140, BLAUHELL, beim("bverfg", "Deshalb"), [("BVerfG 2020: Verbot der geschäftsmäßigen", "ExtraBold", 32, INK),
                                                ("Suizidhilfe (§ 217 StGB) nichtig", "ExtraBold", 32, INK)]),
    zit("BVerfG, Urt. v. 26.2.2020 – 2 BvR 2347/15, Leitsatz 1, Rn. 337", 110, 335, beim("bverfg", "zweitausendzwanzig")),
    zit("vgl. Folge 094", 110, 375, beim("bverfg", "Folge")),
    z("offen: § 216 StGB einschränken, wenn jemand den", 110, 460, "offen", "Bold", 32),
    z("Schritt faktisch nicht selbst gehen kann?", 110, 508, beim("offen", "faktisch"), "Bold", 32),
    z("BGH: offengelassen, hält es für naheliegend", 110, 580, beim("offen", "ließ"), size=32),
    zit("6 StR 68/21 Rn. 21, 23", 110, 630, beim("offen", "naheliegend")),
    ficon("fluent-emoji-flat", "classical-building", GX, 560, 260, beim("bverfg", "Deshalb")),
    pl("Bundesverfassungsgericht", GX, 610, beim("bverfg", "Bundesverfassungsgericht"), fill=WEISS, size=30, anker="m"),
    pl("2020", GX, 680, beim("bverfg", "zweitausendzwanzig"), fill=GELB, size=34, anker="m"),
    pl("selbstbestimmtes Sterben", GX, 150, beim("bverfg", "selbstbestimmtes"), fill=BLAUHELL, size=30, anker="m", bis="offen"),
    pl("offen", GX, 150, "offen", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("tabler", "help-circle", GX, 870, 100, "offen", fuell=WEISS),
]))

# ===========================================================================================================================
# G 4. Merkmale des § 216 StGB
# ===========================================================================================================================
P4 = "4. Merkmale des § 216 StGB"
folie([("merk", P4), ("ausdr", f"{P4} › ausdrücklich"), ("ernst", f"{P4} › ernstlich"), ("best", f"{P4} › bestimmt")],
      rechts_frei([
    *tafel("merk", "4. Merkmale des § 216 StGB"),
    z("Tatherrschaft beim anderen: § 216 StGB prüfen", 110, 180, beim("merk", "Hat"), "Bold", 32),
    blk(110, 250, 1040, 140, LILAHELL, "ausdr", [("ausdrücklich: Das Opfer fordert den Tod eindeutig.", "ExtraBold", 30, INK),
                                               ("Eine bloße Zustimmung genügt nicht.", "ExtraBold", 30, INK)]),
    zit("BGHSt 63, 161 Rn. 19", 110, 400, beim("ausdr", "Zustimmung")),
    blk(110, 450, 1040, 180, BLAUHELL, "ernst", [("ernstlich: freie, fehlerfreie Willensbildung,", "ExtraBold", 30, INK),
                                               ("Bedeutung und Tragweite überblickt, innere", "ExtraBold", 30, INK),
                                               ("Festigkeit; Augenblicksstimmung allein genügt nicht", "ExtraBold", 30, INK)]),
    zit("BGH 3 StR 168/10 Rn. 12 f., 17", 110, 640, beim("ernst", "Augenblicksstimmung")),
    blk(110, 690, 1040, 90, GRUENHELL, "best", [("bestimmt: Das Verlangen ist handlungsleitend.", "ExtraBold", 30, INK)]),
    zit("BGHSt 63, 161 Rn. 19", 110, 790, beim("best", "handlungsleitend")),
    *wilfried("merk", [("merk", "ernst"), ("best", "still")]),
    *requisit([(beim("merk", "Paragraf"), None, "§ 216 StGB", GELB), ("ausdr", None, "ausdrücklich", LILAHELL),
               ("ernst", None, "ernstlich", BLAUHELL), ("best", None, "bestimmt", GRUENHELL)], x=FX),
]))

# ===========================================================================================================================
# H 5. Zweispalter (Täter des § 216 / strafloser Gehilfe) und Ergebnis
# ===========================================================================================================================
P5 = "5. Ergebnis"


def spalte(x, y, w, h, fill, kopf, cue, zeilen, size=29):
    """Eine Spalte des Zweispalters: Karte mit Kopf erscheint bei cue, die Zeilen folgen je zu ihrem gesprochenen Wort."""
    els = [karte(x, y, w, h, cue, fill=fill, rund=18, schatten=6, rand=4),
           z(kopf, x + 22, y + 14, cue, "ExtraBold", 32, rechts=x + w - 12)]
    yy = y + 64
    for text, c in zeilen:
        els.append(z(text, x + 22, yy, c, "Bold", size, rechts=x + w - 12)); yy += int(size * 1.36)
    assert yy <= y + h + 4, f"Spalte zu voll: {kopf} ({yy} > {y + h})"
    return els


ZY, ZH = 170, 230
folie([("zw", f"{P5} › Täter oder Gehilfe?"), ("erg", f"{P5} › Wilfried: Tatherrschaft"),
       ("erg3", f"{P5} › Wilfried: § 216 Abs. 1 StGB"), ("gegen", f"{P5} › Gegenvariante: straflos")], rechts_frei([
    *tafel("zw", "5. Ergebnis: Täter oder Gehilfe?", h=870),
    *spalte(90, ZY, 535, ZH, ROTHELL, "Täter des § 216 StGB", "zl", [
        ("führt den letzten Akt", beim("zl", "führt")), ("selbst aus", beim("zl", "selbst")),
        ("Opfer kann danach", beim("zl", "das")), ("nichts mehr ändern", beim("zl", "nichts"))]),
    *spalte(640, ZY, 535, ZH, GRUENHELL, "strafloser Gehilfe", "zr", [
        ("bereitet vor", beim("zr", "bereitet")), ("Opfer behält den letzten", beim("zr", "das")),
        ("Schritt und die freie", beim("zr", "Schritt")), ("Entscheidung bis zuletzt", beim("zr", "Entscheidung"))]),
    *okz("Wilfried: letzter Schritt selbst, Hedwig konnte danach", 425, beim("erg", "Er"), "Bold", 30, x=150),
    z("nichts mehr ändern: Tatherrschaft", 150, 467, beim("erg", "hatte"), "Bold", 30),
    *okz("Verlangen ausdrücklich und ernstlich, hat ihn bestimmt", 525, "erg2", "Bold", 30, x=150),
    blk(90, 590, 1085, 80, GRUEN, "erg3", [("Wilfried: Tötung auf Verlangen, § 216 Abs. 1 StGB", "ExtraBold", 32, INK)]),
    blk(90, 690, 1085, 80, BLAUHELL, "gegen", [("Gegenvariante: Hedwig geht den letzten Schritt selbst", "ExtraBold", 30, INK)]),
    blk(90, 790, 1085, 80, GRUENHELL, "gegen2", [("Sie tötet sich selbst: Wilfried als Gehilfe straflos", "ExtraBold", 30, INK)]),
    *wilfried("zw", [("zw", "ernst"), ("erg", "still"), ("gegen", "ernst")]),
    *requisit([("zw", ("tabler", "key", 100, GELB), None, WEISS),
               ("erg", ("tabler", "key", 100, GELB), "Wilfried", ROTHELL),
               ("erg3", ("tabler", "gavel", 110, (214, 160, 110, 255)), "§ 216 StGB", GRUEN),
               ("gegen", ("tabler", "key", 100, GELB), "Gegenvariante: Hedwig", GRUENHELL)], x=FX),
]))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
LXX = 1600
folie([("tipp", "Klausurtipp · zuerst die Tatherrschaft"), ("tipp3", "Klausurtipp · an das Unterlassen denken")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Grenze zuerst: Tatherrschaft am letzten Akt,", 200, 200, beim("tipp", "Zieh"), "Bold", 34),
    z("normativ nach dem Gesamtplan", 200, 250, beim("tipp", "normativ"), size=34),
    z("Erst wenn der andere herrscht:", 200, 340, "tipp2", "Bold", 34),
    z("die Merkmale des § 216 StGB prüfen", 200, 390, beim("tipp2", "prüfst"), size=34),
    z("Bei strafloser Suizidhilfe: Unterlassen?", 200, 480, "tipp3", "Bold", 34),
    z("freier Sterbewille: keine Rettungspflicht,", 200, 530, beim("tipp3", "Bei"), size=34),
    z("auch nicht für den Ehepartner", 200, 580, beim("tipp3", "Ehepartner"), size=34),
    zit("BGH 6 StR 68/21 Rn. 25, 29", 200, 640, beim("tipp3", "retten")),
    *redet("LX_warnt", LXX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", LXX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema (progressiv)
# ===========================================================================================================================
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("s1", f"{PS_} › 1. objektiver Tatbestand"), ("s1a", f"{PS_} › 1. b) Tatherrschaft"),
       ("s1b", f"{PS_} › 1. c) Verlangen"), ("s1c", f"{PS_} › 1. d) Bestimmtwerden"), ("s2", f"{PS_} › 2. subjektiver Tatbestand"),
       ("s3", f"{PS_} › 3. Rechtswidrigkeit"), ("s4", f"{PS_} › 4. Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Tötung auf Verlangen, § 216 Abs. 1 StGB", 110, 90, "sch", 46),
    z("1. Objektiver Tatbestand", K1, 190, "s1", "Bold", 36, rechts=1820),
    z("a) Tötung eines anderen Menschen", K2, 250, beim("s1", "Tötung"), size=34, rechts=1820),
    z("b) Tatherrschaft über den letzten Akt (sonst straflose Suizidhilfe)", K2, 310, "s1a", size=34, rechts=1820),
    z("c) ausdrückliches und ernstliches Verlangen", K2, 370, "s1b", size=34, rechts=1820),
    z("d) Bestimmtwerden durch das Verlangen", K2, 430, "s1c", size=34, rechts=1820),
    z("2. Subjektiver Tatbestand: Vorsatz, auch zum Verlangen", K1, 510, "s2", "Bold", 36, rechts=1820),
    z("3. Rechtswidrigkeit", K1, 580, "s3", "Bold", 36, rechts=1820),
    z("4. Schuld", K1, 650, "s4", "Bold", 36, rechts=1820),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer den letzten Akt ", 0), ("selbst ausführt", "a"), (",", 0)],
                 [("tötet, auf Verlangen nach § 216 StGB.", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "selbst")}),
    *markertext([[("Wer ihn dem frei entscheidenden", 0)], [("Sterbewilligen überlässt, leistet nur", 0)],
                 [("straflose Hilfe", "b"), (".", 0)]], 750, 500, 40, "m2", {"b": beim("m2", "straflose")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", "hilfe"),
    ns("Lexi", 1680, 960, "merke", GELB, d=0.2),
])

# ===========================================================================================================================
# L Hilfsangebot (ruhige Tafel, Nummern verifiziert auf telefonseelsorge.de, Abruf 03.10.2026)
# ===========================================================================================================================
folie([("hilfe", "Hilfsangebot")], [
    karte(160, 140, 1600, 760, "hilfe", fill=BLAUHELL),
    titel("Wenn dich das Thema selbst betrifft", 960, 200, "hilfe", 50, anker="m"),
    z("Die TelefonSeelsorge ist rund um die Uhr", 260, 320, beim("hilfe", "Die"), "Bold", 36, rechts=1700),
    z("und kostenlos für dich da.", 260, 375, beim("hilfe", "kostenlos"), "Bold", 36, rechts=1700),
    ficon("tabler", "phone-call", 1520, 470, 150, beim("hilfe", "Die"), fuell=GRUEN),
    z("0800 111 0 111", 260, 480, "nummern", "ExtraBold", 56, rechts=1700),
    z("0800 111 0 222", 260, 570, "nummern", "ExtraBold", 56, rechts=1700),
    z("telefonseelsorge.de", 260, 680, "nummern", size=32, farbe=TEXT, rechts=1700),
])
