"""Folge 149 · Halterhaftung § 7 StVG: Wer zahlt beim Parkplatzrempler? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Heidrun und Volkmar setzen auf dem Parkplatz eines Supermarkts gleichzeitig rückwärts aus gegenüberliegenden
Parklücken; die Hecks berühren sich (Kratzer an beiden Stoßstangen, niemand verletzt). Unstreitig rollten beide noch.
Heidrun verlangt von Volkmar 1.600 €.
Szenen laut ../SZENENPLAN.md: A Parkplatz, B Sachverhalt, C Aufbau, D Wortlautkarte § 7 Abs. 1, E § 7 im Fall, F § 7 Abs. 2,
G Wortlautkarte § 18 Abs. 1, H Wortlautkarten § 17 Abs. 1 und 2, I Abwägung (Säulen), J Parkplatzregeln (Wortlautkarte § 1
Abs. 2 StVO), K Anscheinsbeweis gegen den Rückwärtsfahrer, L Lösung und Gegenfall, M Klausurtipp (Lexi), N Prüfschema,
O Merksatz (Lexi).
DARSTELLUNG: kein Aufprallbild – die Autos rollen langsam Heck an Heck und stehen; danach zwei feine Kratzerstriche an den
Stoßstangen. Zwei Handlungsgeräusche (leises Kunststoff-Anstoßen, Autotür; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist (im Auto: Schild unter dem Auto). Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 124 (gemeinsame Dateien unverändert); neu: parkplatz(),
pschild(), kratzer(), saeulen().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_149/"

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
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
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
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_149/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/124) -----------------------------
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


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
ASPH = (206, 206, 202, 255)
P_O, P_U = 700, 905                          # Parkplatzfläche (Seitenansicht): Oberkante, Unterkante
FAHR = 858                                   # Unterkante der Autos
FBA, FHA = 905, 470                          # Figuren auf dem Parkplatz: Unterkante, Höhe
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def _hart_wenn(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def parkplatz(c):
    """Parkplatzfläche mit Kante und weißen Parkbuchtmarkierungen (für jede Folie neu erzeugt)."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (P_U - P_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (P_U - P_O) * s), fill=ASPH)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (P_U - P_O) * s - 3 * s, 1860 * s, (P_U - P_O) * s - 3 * s), fill=INK, width=6 * s)
    for x in (110, 580, 1310, 1780):                             # Buchtgrenzen links und rechts, Fahrgasse in der Mitte frei
        dr.polygon([((x - 10) * s, 170 * s), ((x + 10) * s, 170 * s), ((x + 26) * s, 196 * s), ((x + 6) * s, 196 * s)], fill=WEISS)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return _hart_wenn(c)(El(im, 30, P_O, c, "cut", 0.0, None, name="parkplatz"))


def pschild(cx, boden_, c):
    """Parkschild: Pfosten (Grundform) mit dem Tabler-Icon „parking“ (Blau)."""
    s = 2
    hp = 300
    im = Image.new("RGBA", (24 * s, hp * s))
    ImageDraw.Draw(im).rounded_rectangle((2 * s, 0, 18 * s, hp * s - 1), 4 * s, fill=(150, 150, 150, 255), outline=INK, width=3 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    h = _hart_wenn(c)
    pfosten = h(El(im, cx - 10, boden_ - hp, c, "cut", 0.0, None, name="pfosten"))
    return [pfosten, h(ficon("tabler", "parking", cx, boden_ - hp + 20, 120, c, fuell=BLAU, anim="cut"))]


def kulisse(c):
    """Supermarkt (Tabler „building-store“, ohne Namen), Einkaufswagen, Parkschild, Parkplatzfläche."""
    h = _hart_wenn(c)
    return [parkplatz(c),
            h(ficon("tabler", "building-store", 175, P_O + 6, 250, c, fuell=TUERKIS, anim="cut")),
            h(ficon("tabler", "shopping-cart", 1665, P_O + 2, 110, c, fuell=None, anim="cut")),
            *pschild(1830, FAHR, c)]


def kratzer(cx, cy, cue, bis=None):
    """Feiner Kratzer an der Stoßstange: kurzer Zickzackstrich (Grundform, Dunkelrot)."""
    pts = [(cx - 22, cy), (cx - 11, cy - 7), (cx, cy + 2), (cx + 11, cy - 6), (cx + 22, cy + 1)]
    e = linienzug(pts, cue, breite=5, farbe=DROT)
    e.bis = bis
    return e


def stehend(k, x, folge, unten=930, hoehe=480):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HD": "Heidrun", "VO": "Volkmar"}
NFARBE = {"HD": GELB, "VO": BLAU}           # wie die Autos


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_hd, folge_vo):
    """Heidrun und Volkmar rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HD", X1, folge_hd), *stehend("VO", X2, folge_vo)]


# ===========================================================================================================================
# A Fall: der Supermarktparkplatz
# ===========================================================================================================================
CW = 380                                     # Autobreite (Renderbreite des Icons)
CWB = ficon("tabler", "car", 0, 0, CW, "_", fuell=GELB).sprite.width     # tatsächliche Breite nach dem Zuschnitt
HX0, HXK = 440, round(960 - CWB / 2)         # Heidruns Auto (blickt nach links): geparkt, beim Kontakt (Heck an Heck)
VX0, VXK = 1480, round(960 + CWB / 2)        # Volkmars Auto (blickt nach rechts): geparkt, beim Kontakt
HFX, VFX = 410, 1500                         # Figuren nach dem Aussteigen
H_LOS = beim("heid", "setzt")
V_LOS = beim("volk", "setzt")
AUS = "schaden"
folie([(NULL, "Fall · Auf dem Supermarktparkplatz"), ("heid", "Fall · Beide setzen zurück"),
       ("kontakt", "Fall · Die Hecks berühren sich"), ("h1", "Fall · Keiner will schuld sein"), ("rep", "Fall · Die Frage")], [
    *kulisse(NULL),
    hart(pl("Samstagvormittag: Parkplatz eines Supermarkts", 70, 30, NULL, fill=GELB, size=38)),
    # die Autos: stehen zunächst in ihren Buchten, rollen dann langsam rückwärts aufeinander zu
    hart(bewegt(ficon("tabler", "car", HXK, FAHR, CW, NULL, fuell=GELB, spiegeln=True, anim="cut"), H_LOS, "kontakt", HX0 - HXK, 0)),
    bewegt(ficon("tabler", "car", VXK, FAHR, CW, NULL, fuell=BLAU, anim="cut"), V_LOS, "kontakt", VX0 - VXK, 0),
    bis_(bewegt(ns("Heidrun", HXK, FAHR, beim("heid", "Heidrun"), GELB), H_LOS, "kontakt", HX0 - HXK, 0), AUS),
    bis_(bewegt(ns("Volkmar", VXK, FAHR, beim("volk", "Volkmar"), BLAU), V_LOS, "kontakt", VX0 - VXK, 0), AUS),
    pl("Heidrun setzt rückwärts aus", 70, 110, H_LOS, fill=WEISS, size=34, bis="kontakt"),
    pfeil(520, 560, 700, 560, H_LOS, breite=10, kopf=30, bis="kontakt"),
    pl("Volkmar setzt gegenüber zurück", 70, 190, V_LOS, fill=WEISS, size=34, bis="kontakt"),
    pfeil(1400, 560, 1220, 560, V_LOS, breite=10, kopf=30, bis="kontakt"),
    pl("langsam aufeinander zu", 70, 270, beim("roll", "Langsam"), fill=WEISS, size=34, bis="kontakt"),
    szene(pl("Die Hecks berühren sich.", 70, 110, "kontakt", fill=HELLROT, size=34, bis="h1"), "149rempler*", 0.7, 0.0),
    pl("Verletzt: niemand", 70, 190, AUS, fill=GRUEN, size=34, bis="h1"),
    pl("Kratzer an beiden Stoßstangen", 70, 270, beim("schaden", "Stoßstangen"), fill=WEISS, size=34, bis="h1"),
    kratzer(960 - 48, FAHR - 100, beim("schaden", "Kratzer")),
    kratzer(960 + 48, FAHR - 100, beim("schaden", "Kratzer")),
    # beide steigen aus (Autotür), Heidrun blickt nach rechts zu Volkmar, Volkmar nach links zu ihr
    szene(peep_voll("HD_schreck_r", HFX, FBA, FHA, AUS, anim="pop", bis="h1"), "149tuer*", 0.6, 0.0),
    ns("Heidrun", HFX, FBA, AUS, GELB, d=0.1),
    *fig("VO", VFX, FBA, FHA, [(AUS, "ruhig"), ("h1", "schreck")], bis="v1"),
    ns("Volkmar", VFX, FBA, AUS, BLAU, d=0.1),
    *redet("HD_redet_r", HFX, FBA, FHA, "h1", "v1"),
    blase("sprech", 560, 210, "h1", 610, 240, inhalt=["Sie sind mir hinten", "reingefahren!"], textsize=38,
          figur=("HD_redet_r", HFX, FBA, FHA), bis="v1"),
    *fig("HD", HFX, FBA, FHA, [("v1", "skeptisch_r"), ("keiner", "ernst_r"), ("rep", "sorge_r")], erst="cut"),
    *redet("VO_redet", VFX, FBA, FHA, "v1", "keiner"),
    blase("sprech", 640, 220, "v1", 1300, 240, inhalt=["Ich? Sie haben doch auch", "nicht nach hinten geschaut!"],
          textsize=36, figur=("VO_redet", VFX, FBA, FHA), bis="keiner"),
    *fig("VO", VFX, FBA, FHA, [("keiner", "denkt"), ("frage", "ernst")], erst="cut"),
    pl("Keiner will schuld sein.", 70, 110, "keiner", fill=WEISS, size=34, bis="frage"),
    pl("Unstreitig: Beide rollten noch.", 70, 190, beim("beide", "Beide"), fill=WEISS, size=34, bis="frage"),
    pl("Reparatur Heidrun: 1.600 €", 70, 270, beim("rep", "Reparaturkosten"), fill=GELB, size=34, bis="frage"),
    ficon("tabler", "receipt-euro", 640, 328, 64, beim("rep", "tausendsechshundert"), fuell=WEISS, bis="frage"),
    pl("Reparatur Heidrun: 1.600 €", 70, 110, "frage", fill=GELB, size=34),
    ficon("tabler", "receipt-euro", 640, 168, 64, "frage", fuell=WEISS),
    pl("Haftung, ohne Verschulden beweisen zu müssen?", 70, 190, "frage", fill=PINK, size=34),
    pl("Wie teilt man, wenn beide beteiligt sind?", 70, 270, "frage2", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_149(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_149("sv", [
    "An einem Samstagvormittag setzen Heidrun und Volkmar auf dem Parkplatz eines Supermarkts gleichzeitig rückwärts aus "
    "zwei gegenüberliegenden Parklücken. Der Parkplatz ist öffentlich zugänglich; Schilder oder Markierungen zur Vorfahrt "
    "gibt es nicht. Beide fahren ihr eigenes Auto. Langsam rollen sie aufeinander zu, bis sich die Hecks berühren. "
    "Verletzt ist niemand; beide Stoßstangen haben Kratzer.",
    "Heidrun ruft: „Sie sind mir hinten reingefahren!“ Volkmar entgegnet: „Ich? Sie haben doch auch nicht nach hinten "
    "geschaut!“ Unstreitig ist nur, dass beide Autos noch rollten, als sie sich berührten. Mehr lässt sich nicht aufklären.",
    "Heidrun verlangt von Volkmar und seinem Haftpflichtversicherer die Reparaturkosten für ihr Auto, 1.600 €.",
], "Kann Heidrun Ersatz verlangen, und in welcher Höhe?")

# ===========================================================================================================================
# C Aufbau: drei Schritte im StVG
# ===========================================================================================================================
folie([("aufbau", "Aufbau · drei Schritte im StVG"), ("w7", "Aufbau › § 7 StVG: Halter"), ("w18", "Aufbau › § 18 StVG: Fahrer"),
       ("w17", "Aufbau › § 17 StVG: Verteilung")], rechts_frei([
    *tafel("aufbau", "Der Aufbau"),
    z("Prüfung im StVG in drei Schritten:", 110, 185, "aufbau", "Bold", 36),
    blk(110, 260, 1040, 80, GELB, "w7", [("1. § 7 StVG: Haftung des Halters", "ExtraBold", 36, INK)]),
    blk(110, 370, 1040, 80, BLAU, "w18", [("2. § 18 StVG: Haftung des Fahrers", "ExtraBold", 36, INK)]),
    blk(110, 480, 1040, 80, GRUEN, "w17", [("3. § 17 StVG: Verteilung bei zwei Autos", "ExtraBold", 36, INK)]),
    *requisit([("aufbau", ("tabler", "book", 100, WEISS), "StVG", GELB),
               ("w7", ("tabler", "car", 150, BLAU), "Halter", GELB),
               ("w18", ("tabler", "steering-wheel", 100, WEISS), "Fahrer", BLAU),
               ("w17", ("tabler", "scale", 100, WEISS), "Verteilung", GRUEN)]),
    *zwei([("aufbau", "ernst")], [("aufbau", "ruhig"), ("w7", "denkt")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 7 Abs. 1 StVG, Gefährdungshaftung
# ===========================================================================================================================
PA = "I. Halterhaftung, § 7 Abs. 1 StVG"
W7 = ["„Wird bei dem Betrieb eines Kraftfahrzeugs ein Mensch",
      "getötet, der Körper oder die Gesundheit eines Menschen",
      "verletzt oder eine Sache beschädigt, so ist der Halter",
      "verpflichtet, dem Verletzten den daraus entstehenden",
      "Schaden zu ersetzen.“"]
w7, w7_y = wortlaut(80, 170, 1100, W7, "§ 7 Abs. 1 StVG", "p7", marken=[
    (0, "bei dem Betrieb eines Kraftfahrzeugs", beim("p7", "Betrieb")), (2, "eine Sache beschädigt", beim("p7", "Sache")),
    (2, "Halter", beim("p7", "Halter")), (4, "Schaden zu ersetzen", beim("p7", "Schaden"))], size=34)
folie([("p7", f"{PA} › Wortlaut"), ("gef", f"{PA} › Gefährdungshaftung")], rechts_frei([
    *tafel("p7", "Die Norm: § 7 Abs. 1 StVG"),
    *w7,
    z("Von Verschulden steht da nichts:", 110, w7_y + 30, "gef", "Bold", 34),
    blk(110, w7_y + 85, 1040, 80, LILA, beim("gef", "Gefährdungshaftung"), [("Gefährdungshaftung", "ExtraBold", 38, INK)]),
    zit("BGH, Urt. v. 11.6.2013 – VI ZR 150/12, Rn. 17", 110, w7_y + 178, beim("gef", "Gefährdungshaftung")),
    z("Preis dafür, dass der Halter erlaubterweise", 110, w7_y + 235, "preis", "Bold", 34),
    z("eine Gefahrenquelle eröffnet", 110, w7_y + 283, beim("preis", "Gefahrenquelle"), "Bold", 34),
    zit("BGH, Urt. v. 24.3.2015 – VI ZR 265/14, Rn. 5", 110, w7_y + 338, beim("preis", "Gefahrenquelle")),
    *requisit([("p7", ("tabler", "book", 100, WEISS), "§ 7 Abs. 1 StVG", GELB),
               ("gef", ("tabler", "alert-triangle", 100, GELB), "ohne Verschulden", LILA),
               ("preis", ("tabler", "car", 150, BLAU), "Gefahrenquelle Auto", WEISS)]),
    *zwei([("p7", "ruhig")], [("p7", "ernst"), ("gef", "sorge")]),
]))

# ===========================================================================================================================
# E § 7 Abs. 1 im Fall
# ===========================================================================================================================
folie([("halter", f"{PA} › Halter"), ("betr", f"{PA} › bei dem Betrieb"), ("rg", f"{PA} › Rechtsgutverletzung"),
       ("kaus", f"{PA} › haftungsbegründende Kausalität")], rechts_frei([
    *tafel("halter", "§ 7 Abs. 1 StVG im Fall"),
    *okz("1. Halter: Volkmar, sein eigenes Auto", 180, beim("halter", "Halter"), "Bold", 34, x=160),
    *okz("2. bei dem Betrieb: weit auszulegen", 260, beim("betr", "weit"), "Bold", 34, x=160),
    z("Gefahren des Autos haben sich im Schaden ausgewirkt", 160, 312, beim("betr", "genügt"), size=32),
    zit("BGH, Urt. v. 24.3.2015 – VI ZR 265/14, Rn. 5", 160, 358, beim("betr", "genügt")),
    z("rückwärts ausparken: in Betrieb", 160, 400, "betr2", "Bold", 32),
    *okz("3. Rechtsgutverletzung: Auto beschädigt (Sache)", 480, "rg", "Bold", 34, x=160),
    z("4. Beschädigung beruht auf diesem Betrieb", 160, 560, "kaus", "Bold", 34),
    *okz("haftungsbegründende Kausalität", 612, beim("kaus", "haftungsbegründende"), "Regular", 32, x=160),
    *requisit([("halter", ("tabler", "car", 150, BLAU), "Halter: Volkmar", BLAU),
               ("betr", ("tabler", "car", 150, BLAU), "in Betrieb", WEISS),
               ("rg", ("tabler", "tool", 100, WEISS), "Sache beschädigt", HELLROT),
               ("kaus", ("tabler", "link", 100, WEISS), "Kausalität", WEISS)]),
    *zwei([("halter", "ruhig"), ("rg", "sorge")], [("halter", "ernst"), ("betr2", "still")]),
]))

# ===========================================================================================================================
# F § 7 Abs. 2 StVG: höhere Gewalt
# ===========================================================================================================================
W72 = ["„Die Ersatzpflicht ist ausgeschlossen, wenn der Unfall",
       "durch höhere Gewalt verursacht wird.“"]
w72, w72_y = wortlaut(80, 170, 1100, W72, "§ 7 Abs. 2 StVG", "p72", marken=[
    (1, "höhere Gewalt", beim("p72", "höhere"))], size=34)
folie([("p72", f"{PA} › Ausschluss: höhere Gewalt, § 7 Abs. 2"), ("p7erg", f"{PA} › Volkmar haftet (+)")], rechts_frei([
    *tafel("p72", "Ausschluss: § 7 Abs. 2 StVG"),
    *w72,
    *neinz("Rempler beim Ausparken: keine höhere Gewalt", w72_y + 40, beim("hg", "Rempler"), "Bold", 34, x=160),
    zit("vgl. BGH, Urt. v. 15.12.2015 – VI ZR 6/15, Rn. 9", 160, w72_y + 92, beim("hg", "Rempler")),
    blk(110, w72_y + 160, 1040, 120, GRUEN, "p7erg", [("Volkmar haftet als Halter,", "ExtraBold", 38, INK),
                                                      ("ganz ohne Verschulden", "ExtraBold", 38, INK)]),
    *requisit([("p72", ("tabler", "cloud-storm", 110, BLAU), "höhere Gewalt?", WEISS),
               ("hg", ("tabler", "car", 150, BLAU), "Rempler beim Ausparken", WEISS),
               ("p7erg", ("tabler", "shield-check", 100, GRUEN), "§ 7 StVG (+)", GRUEN)]),
    *zwei([("p72", "skeptisch"), ("p7erg", "froh")], [("p72", "denkt"), ("p7erg", "muede")]),
]))

# ===========================================================================================================================
# G Wortlautkarte § 18 Abs. 1 StVG: Fahrerhaftung, vermutetes Verschulden
# ===========================================================================================================================
PB = "II. Fahrerhaftung, § 18 Abs. 1 StVG"
W18 = ["„In den Fällen des § 7 Abs. 1 ist auch der Führer des",
       "Kraftfahrzeugs zum Ersatz des Schadens nach den",
       "Vorschriften der §§ 8 bis 15 verpflichtet. Die Ersatzpflicht",
       "ist ausgeschlossen, wenn der Schaden nicht durch ein",
       "Verschulden des Führers verursacht ist.“"]
w18, w18_y = wortlaut(80, 170, 1100, W18, "§ 18 Abs. 1 StVG", "p18a", marken=[
    (0, "auch der Führer", beim("p18a", "auch")), (3, "ist ausgeschlossen", beim("p18b", "ausgeschlossen")),
    (4, "Verschulden des Führers", beim("p18b", "Verschulden"))], size=32)
folie([("p18", PB), ("p18b", f"{PB} › S. 2: Entlastung"), ("verm", f"{PB} › vermutetes Verschulden"),
       ("p18c", f"{PB} › Entlastung? Offen")], rechts_frei([
    *tafel("p18", "II. Der Fahrer: § 18 StVG"),
    *w18,
    z("vermutetes Verschulden:", 110, w18_y + 30, "verm", "Bold", 34),
    z("Der Fahrer muss beweisen, dass ihn kein", 110, w18_y + 80, beim("verm", "Fahrer"), size=32),
    z("Verschulden trifft.", 110, w18_y + 122, beim("verm", "Fahrer"), size=32),
    zit("BGH, Urt. v. 11.6.2013 – VI ZR 150/12, Rn. 13, 18", 110, w18_y + 172, beim("verm", "Fahrer")),
    z("Abgrenzung zum Anscheinsbeweis: Video dazu", 110, w18_y + 218, beim("verm", "Abgrenzung"), "Bold", 30, farbe=TEXT),
    blk(110, w18_y + 280, 1040, 80, PINK, "p18c", [("Kann Volkmar sich entlasten?", "ExtraBold", 36, INK)]),
    *requisit([("p18", ("tabler", "steering-wheel", 100, WEISS), "Volkmar am Steuer", BLAU),
               ("p18b", ("tabler", "shield", 100, BLAU), "Entlastung", WEISS),
               ("verm", ("tabler", "scale", 100, WEISS), "Beweis: Fahrer", GELB),
               ("p18c", ("tabler", "parking", 100, BLAU), "Parkplatz?", PINK)]),
    *zwei([("p18", "ruhig")], [("p18", "ernst"), ("verm", "sorge"), ("p18c", "denkt")]),
]))

# ===========================================================================================================================
# H Wortlautkarten § 17 Abs. 1 und 2 StVG
# ===========================================================================================================================
PC = "III. Haftungsverteilung, § 17 StVG"
W171 = ["„Wird ein Schaden durch mehrere Kraftfahrzeuge verursacht",
        "und sind die beteiligten Fahrzeughalter einem Dritten kraft",
        "Gesetzes zum Ersatz des Schadens verpflichtet, so hängt im",
        "Verhältnis der Fahrzeughalter zueinander die Verpflichtung",
        "zum Ersatz sowie der Umfang des zu leistenden Ersatzes von",
        "den Umständen, insbesondere davon ab, inwieweit der Schaden",
        "vorwiegend von dem einen oder dem anderen Teil verursacht",
        "worden ist.“"]
w171, w171_y = wortlaut(80, 165, 1100, W171, "§ 17 Abs. 1 StVG", "p17a", marken=[
    (3, "Verhältnis der Fahrzeughalter zueinander", beim("p17a", "Verhältnis")), (5, "den Umständen", beim("p17a", "Umständen")),
    (6, "vorwiegend", beim("p17a", "vorwiegend"))], size=30)
W172 = ["„Wenn der Schaden einem der beteiligten Fahrzeughalter",
        "entstanden ist, gilt Absatz 1 auch für die Haftung der",
        "Fahrzeughalter untereinander.“"]
w172, w172_y = wortlaut(80, w171_y + 20, 1100, W172, "§ 17 Abs. 2 StVG", "p17b", marken=[
    (0, "einem der beteiligten Fahrzeughalter", beim("p17b", "einer"))], size=30)
assert w172_y <= 895, w172_y
folie([("p17", PC), ("p17a", f"{PC} › Abs. 1: wer vorwiegend verursacht hat"), ("p17b", f"{PC} › Abs. 2: Halter untereinander")],
      rechts_frei([
    *tafel("p17", "III. Die Verteilung: § 17 StVG"),
    z("Zwei Autos haben den Schaden verursacht.", 110, 175, "p17", "Bold", 34, bis="p17a"),
    *w171, *w172,
    *requisit([("p17", ("tabler", "car", 150, BLAU), "zwei Autos", WEISS),
               ("p17a", ("tabler", "scale", 100, WEISS), "Verursachung", GELB),
               ("p17b", ("tabler", "car", 150, GELB), "Heidrun: Halterin", GELB)]),
    *zwei([("p17", "ernst"), ("p17b", "skeptisch")], [("p17", "ruhig")]),
]))


# ===========================================================================================================================
# I Abwägung: Betriebsgefahr als Sockel, Verschulden, § 17 Abs. 3, § 9 StVG / § 254 BGB
# ===========================================================================================================================
LXS, RXS, SW_ = 160, 660, 440                # Säulen: links Heidrun, rechts Volkmar


def saeulen(cue_name, cue_bg, cue_v, text_v, fill_v, y0=180):
    """Zwei Säulen: Namensschild, Sockel „Betriebsgefahr“, darauf das (bewiesene) Verschulden."""
    els = [pl("Heidrun", LXS + SW_ / 2, y0, cue_name, fill=GELB, size=30, anker="m"),
           pl("Volkmar", RXS + SW_ / 2, y0, cue_name, fill=BLAU, size=30, anker="m")]
    for x in (LXS, RXS):
        els.append(blk(x, y0 + 170, SW_, 95, HELLGRAU, cue_bg, [("Betriebsgefahr", "ExtraBold", 34, INK)]))
    if cue_v:
        for x in (LXS, RXS):
            els.append(blk(x, y0 + 65, SW_, 95, fill_v, cue_v, [(text_v, "ExtraBold", 32, INK)]))
    return els


folie([("sockel", f"{PC} › Sockel: Betriebsgefahr"), ("versch", f"{PC} › Verschulden"), ("bew", f"{PC} › nur Bewiesenes"),
       ("p173", f"{PC} › Abs. 3: unabwendbares Ereignis"), ("p254", "Mitverschulden · § 9 StVG, § 254 BGB")], rechts_frei([
    *tafel("sockel", "Die Abwägung nach § 17 StVG"),
    *saeulen("sockel", "sockel", "versch", "Verschulden?", HELLROT),
    z("nur was unstreitig, zugestanden oder bewiesen ist", 110, 470, "bew", "Bold", 32),
    zit("BGH, Urt. v. 11.10.2016 – VI ZR 66/16, Rn. 7, 12", 110, 515, "bew"),
    z("Abs. 3: frei nur bei unabwendbarem Ereignis:", 110, 580, "p173", "Bold", 32),
    z("verhalten wie ein Idealfahrer", 110, 625, beim("p173", "Idealfahrer"), size=32),
    zit("BGH, Urt. v. 3.12.2024 – VI ZR 18/24, Rn. 15", 110, 670, beim("p173", "Idealfahrer")),
    z("Mitverschulden des Verletzten: § 9 StVG mit § 254 BGB", 110, 735, "p254", "Bold", 32),
    z("unter Haltern: derselbe Maßstab in § 17 StVG", 110, 780, beim("p254", "unter"), size=32),
    *requisit([("sockel", ("tabler", "car", 150, BLAU), "Betriebsgefahr", HELLGRAU),
               ("versch", ("tabler", "alert-triangle", 100, GELB), "Verschulden", HELLROT),
               ("bew", ("tabler", "file-check", 100, WEISS), "nur Bewiesenes", WEISS),
               ("p173", ("tabler", "star", 100, GELB), "Idealfahrer", WEISS),
               ("p254", ("tabler", "book", 100, WEISS), "§ 254 BGB", WEISS)]),
    *zwei([("sockel", "ruhig"), ("p173", "skeptisch")], [("sockel", "ernst"), ("versch", "sorge"), ("p254", "ruhig")]),
]))

# ===========================================================================================================================
# J Parkplatzregeln: StVO, kein „rechts vor links“, § 1 Abs. 2 StVO, sofort anhalten können
# ===========================================================================================================================
W12 = ["„Wer am Verkehr teilnimmt hat sich so zu verhalten, dass kein",
       "Anderer geschädigt, gefährdet oder mehr, als nach den Umständen",
       "unvermeidbar, behindert oder belästigt wird.“"]
w12, w12_y = wortlaut(80, 470, 1100, W12, "§ 1 Abs. 2 StVO", "p12", marken=[
    (0, "so zu verhalten", beim("p12", "verhalten")), (1, "geschädigt", beim("p12", "geschädigt"))], size=30)
folie([("park", "Parkplatz · Welche Regeln gelten?"), ("stvo", "Parkplatz › StVO anwendbar"),
       ("rvl", "Parkplatz › kein „rechts vor links“"), ("p12", "Parkplatz › § 1 Abs. 2 StVO: Rücksicht"),
       ("anh", "Parkplatz › rückwärts: sofort anhalten können")], rechts_frei([
    *tafel("park", "Regeln auf dem Parkplatz"),
    *okz("StVO gilt: Parkplatz öffentlich zugänglich", 180, beim("stvo", "gilt"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 22.11.2022 – VI ZR 344/21, Rn. 12", 160, 228, beim("stvo", "gilt")),
    z("Fahrgassen: meist kein eindeutiger Straßencharakter", 160, 285, "rvl", "Bold", 32),
    *neinz("„rechts vor links“: gilt nicht, auch nicht mittelbar", 340, beim("rvl", "rechts"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 22.11.2022 – VI ZR 344/21, Rn. 15, 17 f.", 160, 390, beim("rvl", "rechts")),
    *w12,
    blk(110, w12_y + 22, 1040, 80, GELB, "anh", [("Rückwärts: notfalls sofort anhalten können", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 26.1.2016 – VI ZR 179/15, Rn. 11", 110, w12_y + 112, beim("anh", "sofort")),
    *requisit([("park", ("tabler", "parking", 100, BLAU), "Parkplatz", WEISS),
               ("stvo", ("tabler", "book", 100, WEISS), "StVO", GELB),
               ("rvl", ("tabler", "road-off", 100, WEISS), "keine Vorfahrtsregel", HELLROT),
               ("p12", ("tabler", "heart-handshake", 100, ROT), "Rücksicht", WEISS),
               ("anh", ("tabler", "hand-stop", 100, GELB), "sofort anhalten", GELB)]),
    *zwei([("park", "ruhig"), ("rvl", "skeptisch"), ("anh", "ernst")], [("park", "denkt"), ("p12", "ruhig")]),
]))

# ===========================================================================================================================
# K Anscheinsbeweis gegen den Rückwärtsfahrer
# ===========================================================================================================================
LK, RK, KW = 110, 640, 510
folie([("ansch", "Parkplatz › Anscheinsbeweis gegen den Rückwärtsfahrer"), ("ans1", "Parkplatz › rollte noch: Anschein (+)"),
       ("ans2", "Parkplatz › stand schon: kein Anschein"), ("ans4", "Parkplatz › Betriebsgefahr zählt trotzdem")], rechts_frei([
    *tafel("ansch", "Anschein gegen den Rückwärtsfahrer?"),
    karte(LK, 180, KW, 300, "ans1", fill=HELLROT, rund=18, schatten=6, rand=4),
    z("rollte noch", LK + 25, 198, "ans1", "ExtraBold", 34, rechts=LK + KW - 10),
    z("im Moment der Kollision", LK + 25, 250, beim("ans1", "Moment"), size=30, rechts=LK + KW - 10),
    z("erster Anschein:", LK + 25, 320, beim("ans1", "Anschein"), "Bold", 30, rechts=LK + KW - 10),
    z("Sorgfaltspflicht verletzt", LK + 25, 362, beim("ans1", "Sorgfaltspflicht"), "Bold", 30, rechts=LK + KW - 10),
    ok(LK + KW - 50, 430, beim("ans1", "Sorgfaltspflicht"), gr=20),
    karte(RK, 180, KW, 300, "ans2", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("stand schon", RK + 25, 198, "ans2", "ExtraBold", 34, rechts=RK + KW - 10),
    z("oder nicht auszuschließen", RK + 25, 250, beim("ans2", "lässt"), size=30, rechts=RK + KW - 10),
    z("kein Anschein", RK + 25, 320, beim("ans2", "spricht"), "Bold", 30, rechts=RK + KW - 10),
    z("gegen ihn", RK + 25, 362, beim("ans2", "spricht"), "Bold", 30, rechts=RK + KW - 10),
    nein(RK + KW - 50, 430, beim("ans2", "kein"), gr=20),
    zit("BGH, Urt. v. 15.12.2015 – VI ZR 6/15, Rn. 15;", 110, 510, "ans3"),
    zit("Urt. v. 26.1.2016 – VI ZR 179/15, Rn. 11;", 110, 548, "ans3"),
    zit("Urt. v. 11.10.2016 – VI ZR 66/16, Rn. 9 f.", 110, 586, "ans3"),
    blk(110, 650, 1040, 80, GELB, "ans4", [("Seine Betriebsgefahr zählt trotzdem.", "ExtraBold", 36, INK)]),
    zit("BGH, Urt. v. 11.10.2016 – VI ZR 66/16, Rn. 12", 110, 742, "ans4"),
    *requisit([("ansch", ("tabler", "bulb", 100, GELB), "Anscheinsbeweis?", WEISS),
               ("ans1", ("tabler", "car", 150, HELLROT), "rollte noch", HELLROT),
               ("ans2", ("tabler", "car", 150, HELLGRUEN), "stand schon", HELLGRUEN),
               ("ans3", ("tabler", "gavel", 100, HOLZ), "BGH 2015 und 2016", WEISS),
               ("ans4", ("tabler", "car", 150, BLAU), "Betriebsgefahr", HELLGRAU)]),
    *zwei([("ansch", "ruhig"), ("ans1", "skeptisch")], [("ansch", "denkt"), ("ans2", "ruhig"), ("ans4", "ernst")]),
]))

# ===========================================================================================================================
# L Lösung und Gegenfall
# ===========================================================================================================================
folie([("loes", "Lösung · Heidrun gegen Volkmar"), ("l1", "Lösung › Anschein gegen beide"),
       ("l2", "Lösung › § 18 StVG: keine Entlastung"), ("l3", "Lösung › Abwägung nach § 17 StVG"),
       ("l5", "Lösung › 800 € für Heidrun"), ("l6", "Gegenfall · Volkmar stand schon")], rechts_frei([
    *tafel("loes", "Lösung: Heidrun gegen Volkmar"),
    *saeulen("loes", "loes", "l1", "Verstoß (Anschein)", HELLROT),
    *okz("§ 18: Volkmar kann sich nicht entlasten", 470, beim("l2", "entlasten"), "Bold", 32, x=160),
    *okz("unabwendbar für keinen, § 17 Abs. 3", 520, beim("l2", "unabwendbar"), "Bold", 32, x=160),
    pl("=", 630, 300, "l3", fill=WEISS, size=44, anker="m"),
    z("gleiche Betriebsgefahr, gleich schwere Verstöße", 160, 575, beim("l3", "gleiche"), size=32),
    blk(110, 625, 500, 80, GELB, "l4", [("je zur Hälfte", "ExtraBold", 36, INK)]),
    blk(640, 625, 510, 80, GRUEN, "l5", [("800 € an Heidrun", "ExtraBold", 36, INK)]),
    z("Gegenfall: Volkmar stand schon: kein Anschein gegen ihn;", 110, 730, "l6", "Bold", 30),
    z("Heidrun trägt den größeren Teil, seine Betriebsgefahr zählt mit", 110, 772, beim("l6", "Dann"), size=30),
    *requisit([("loes", ("tabler", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("l1", ("tabler", "bulb", 100, GELB), "Anschein gegen beide", HELLROT),
               ("l3", ("tabler", "scale", 100, WEISS), "Abwägung", WEISS),
               ("l5", ("tabler", "coin-euro", 100, GELB), "800 €", GRUEN),
               ("l6", ("tabler", "car", 150, HELLGRUEN), "Gegenfall", WEISS)]),
    *zwei([("loes", "ernst"), ("l5", "still"), ("l6", "skeptisch")], [("loes", "ernst"), ("l2", "sorge"), ("l5", "muede")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Reihenfolge § 7, § 18, § 17 StVG"), ("tp4", "Klausurtipp · Direktanspruch, § 115 VVG"),
       ("tp5", "Klausurtipp · daneben § 823 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Halte die Reihenfolge ein:", 200, 200, beim("tipp", "Halte"), "Bold", 36),
    z("1. § 7 StVG gegen den Halter", 200, 262, "tp1", size=34),
    z("2. § 18 StVG gegen den Fahrer", 200, 317, "tp2", size=34),
    z("3. Verteilung nach § 17 StVG", 200, 372, "tp3", size=34),
    linienzug([(130, 445), (1130, 445)], "tp4", breite=3),
    z("Versicherer nicht vergessen:", 200, 475, "tp4", "Bold", 36),
    z("Anspruch auch gegen den Versicherer", 200, 535, beim("tp4", "kann"), size=34),
    zit("§ 115 Abs. 1 S. 1 Nr. 1 VVG (Pflichtversicherung)", 200, 588, beim("tp4", "kann")),
    z("daneben: § 823 BGB, Video „Deliktsrecht“", 200, 660, "tp5", "Bold", 32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. § 7 Abs. 1 StVG: Haftung des Halters", True),
          ("s1a", 1, "Halter, Betrieb eines Kraftfahrzeugs, Rechtsgutverletzung, Kausalität", False),
          ("s1b", 1, "kein Ausschluss durch höhere Gewalt, § 7 Abs. 2 StVG", False),
          ("s2", 0, "II. § 18 Abs. 1 StVG: Haftung des Fahrers", True),
          ("s2", 1, "haftet, wenn er sich nicht entlastet (S. 2)", False),
          ("s3", 0, "III. § 17 StVG: Abwägung der Verursachungsbeiträge", True),
          ("s3a", 1, "Betriebsgefahr und bewiesenes Verschulden", False),
          ("s3b", 1, "frei nur bei unabwendbarem Ereignis, § 17 Abs. 3 StVG", False),
          ("s4", 0, "IV. Direktanspruch gegen den Versicherer, § 115 VVG", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Ansprüche nach dem StVG"), 110, 90, "sch", 46),
           z("§§ 7, 17, 18 StVG; § 115 Abs. 1 VVG", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 78, 1: 70}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. § 7 StVG"), ("s1b", "Prüfschema › I. höhere Gewalt"),
       ("s2", "Prüfschema › II. § 18 StVG"), ("s3", "Prüfschema › III. § 17 StVG"),
       ("s3b", "Prüfschema › III. unabwendbares Ereignis"), ("s4", "Prüfschema › IV. Direktanspruch")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Halter haftet für die", 0)], [("Betriebsgefahr seines Autos,", 0)],
                 [("auch ohne Verschulden", "a"), (".", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "auch")}),
    *markertext([[("Verursachen zwei Autos den Schaden,", 0)], [("entscheidet die ", 0), ("Abwägung", "b"), (",", 0)],
                 [("wer welchen Anteil trägt.", 0)]], 750, 580, 44, "m2", {"b": beim("m2", "Abwägung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
