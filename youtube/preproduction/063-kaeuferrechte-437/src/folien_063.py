"""Folge 063 · § 437 BGB: Die Käuferrechte auf einen Blick – Schema – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „Der neue Kühlschrank kühlt nicht“): Manfred (Verbraucher) kauft im Elektrogeschäft von Frau Kemper
(Unternehmerin) einen Kühlschrank für 600 €; sie liefert ihn in seine Küche, er kühlt nicht. Manfred verlangt am Telefon
einen neuen (Frist 2 Wochen), Frau Kemper sagt zu und vergisst den Auftrag; Manfred kauft woanders für 700 €.
Szenen laut ../SZENENPLAN.md: A1 Elektrogeschäft, A2 Küche und Telefonat, A3 Ersatzkauf, B Sachverhalt, C § 437 (Wortlaut),
D I. Voraussetzungen, E1 II. Nacherfüllung (Wortlaut § 439 I), E2 § 439 II–IV, F1 III. Frist als Brücke, F2 Entbehrlichkeit
und § 475d, G1 IV. Rücktritt, G2 Minderung, H1 V. Schadensersatz (Normen), H2 Schadensersatz am Fall, I Ergebnis und
Verjährung, J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Keine Geräusche (siehe ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen
glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 059 (gemeinsame Dateien unverändert). Zahlen auf
Tafeln, Pillen und Blasen als Ziffern, im Sprechtext als Wörter."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_063/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    # wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (fl_block nimmt 64 px an)
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
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (Befund Folge 063)


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_063/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Eigene Hilfsfunktion (wie Folge 031/037): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
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




BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel: Frau Kemper links, Manfred rechts
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
MA_F, KM_F = BLAU, GRUEN                    # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
KUEHL = (236, 244, 252, 255)                # Füllung Kühlschrank (Tabler „fridge“)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def kuehlschrank(cx, unten, breite, cue, fuell=KUEHL, name="fridge", **k):
    """Kühlschrank: Tabler „fridge“ bzw. „fridge-off“ (MIT)."""
    return ficon("tabler", name, cx, unten, breite, cue, fuell=fuell, **k)


def manfred(cx, unten, hoehe, folge, **k):
    return fig("MA", cx, unten, hoehe, folge, **k)


def kemper(cx, unten, hoehe, folge, **k):
    return fig("KM", cx, unten, hoehe, folge, **k)


def paar(c0, km_folge, ma_folge):
    """Tafelszene: Frau Kemper links (X1), Manfred rechts (X2), beide blicken zur Tafel."""
    return [*kemper(X1, FB, FR, km_folge), ns("Frau Kemper", X1, FB, c0, KM_F),
            *manfred(X2, FB, FR, ma_folge, d=0.2), ns("Manfred", X2, FB, c0, MA_F, d=0.2)]


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


FRIDGE = ("tabler", "fridge", 120, KUEHL)
FRIDGE_OFF = ("tabler", "fridge-off", 120, ROT)

# A1 Fall: Kauf im Elektrogeschäft ---------------------------------------------------------------------------------------
KMX, MAX = 520, 1500
folie([(NULL, "Fall · Kauf im Elektrogeschäft")], [
    hart(pl("Im Elektrogeschäft von Frau Kemper", 70, 40, NULL, fill=GELB, size=44)),
    boden(NULL, True),
    hart(ficon("tabler", "building-store", 250, 400, 190, NULL, fuell=GELB)),
    hart(kuehlschrank(960, BODEN, 230, NULL)),
    *kemper(KMX, BODEN, FH, [(NULL, "froh_r")], erst="cut"),
    hart(ns("Frau Kemper, Händlerin", KMX, BODEN, NULL, KM_F)),
    *manfred(MAX, BODEN, FH, [(NULL, "ruhig"), (beim("fall", "Kühlschrank"), "zufrieden")], erst="cut"),
    hart(ns("Manfred, Käufer", MAX, BODEN, NULL, MA_F)),
    pl("neu", 960, 590, beim("fall", "neuen"), fill=GRUEN, size=32, anker="m"),
    ficon("tabler", "cash-banknote", 960, 480, 150, beim("fall", "sechshundert"), fuell=GRUEN),
    pl("600 €", 960, 330, beim("fall", "sechshundert"), fill=GELB, size=36, anker="m"),
])

# A2 Fall: Küche – Lieferung, kühlt nicht, Telefonat, Frist vergeht ------------------------------------------------------
KX = 900                                                         # Kühlschrank in der Küche
INSET = (70, 150, 520, 700)                                      # Telefon-Ausschnitt: Frau Kemper im Geschäft
IKX, IKU, IKH = 330, 800, 400                                    # Frau Kemper im Ausschnitt
folie([("liefer", "Fall · Lieferung in die Küche"), ("warm", "Fall · Der Kühlschrank kühlt nicht"),
       ("ma1", "Fall · Nacherfüllung verlangt, Frist 2 Wochen"), ("verg", "Fall · Die Frist läuft ab")], [
    bis_(pl("Am nächsten Tag: Lieferung in die Küche", 70, 40, "liefer", fill=GELB, size=44), "warm"),
    bis_(pl("Am Abend", 70, 40, "warm", fill=LILA, size=44), "verg"),
    pl("2 Wochen später", 70, 40, beim("verg", "zwei"), fill=LILA, size=44),
    boden("liefer"),
    karte(1060, 600, 210, 280, "liefer", fill=(222, 214, 200, 255), rund=10, schatten=4),     # Küchenzeile
    karte(1080, 640, 170, 14, "liefer", fill=WEISS, rund=6, schatten=0, rand=3),
    bewegt(kuehlschrank(KX, BODEN, 260, "liefer"), "liefer", beim("liefer", "Küche", ende=True), -380, 0),
    *kemper(380, BODEN, FH, [("liefer", "froh_r")], bis="warm", erst="fade"),
    bis_(ns("Frau Kemper", 380, BODEN, "liefer", KM_F), "warm"),
    ficon("tabler", "temperature-plus", KX, 520, 90, beim("warm", "warm"), fuell=ROT),
    pl("innen warm", KX, 400, beim("warm", "warm"), fill=ROT, size=30, anker="m"),
    pl("Kompressor defekt", KX, 920, beim("warm", "Kompressor"), fill=ROT, size=30, anker="m"),
    *manfred(1560, BODEN, FH, [("liefer", "froh"), ("warm", "sorge")], bis="ma1", erst="fade"),
    *redet("MA_redet", 1560, BODEN, FH, "ma1", "ke1"),
    *manfred(1560, BODEN, FH, [("ke1", "zufrieden"), ("verg", "denkt")], bis="neu", erst="cut"),
    ns("Manfred", 1560, BODEN, "liefer", MA_F),
    ficon("tabler", "device-mobile", 1400, 640, 60, "ma1", fuell=WEISS),
    blase("sprech", 700, 250, "ma1", 1320, 220, inhalt=["Der Kühlschrank kühlt nicht!", "Bringen Sie mir bitte innerhalb",
                                                       "von 2 Wochen einen neuen."],
          textsize=34, figur=("MA_redet", 1560, BODEN, FH), bis="ke1"),
    # Telefon: Frau Kemper in ihrem Geschäft (Ausschnitt links)
    karte(*INSET, "ma1", fill=(255, 252, 240, 255), rund=22, schatten=6),
    ficon("tabler", "building-store", 150, 830, 90, "ma1", fuell=GELB),
    ficon("tabler", "device-mobile", 470, 640, 60, "ma1", fuell=WEISS),
    *kemper(IKX, IKU, IKH, [("ma1", "ruhig_r")], bis="ke1", erst="pop"),
    *redet("KM_redet_r", IKX, IKU, IKH, "ke1", "verg"),
    *kemper(IKX, IKU, IKH, [("verg", "ruhig_r")], erst="cut"),
    ns("Frau Kemper", IKX, IKU, "ma1", KM_F),
    blase("sprech", 430, 200, "ke1", 360, 260, inhalt=["Ja, ich kümmere", "mich darum."], textsize=34,
          figur=("KM_redet_r", IKX, IKU, IKH), bis="verg"),
    pl("Auftrag vergessen", 305, 335, "verg", fill=ROT, size=30, anker="m"),
    ficon("tabler", "calendar-time", 1300, 560, 110, beim("verg", "zwei"), fuell=WEISS),
    pl("Frist abgelaufen", 1300, 410, beim("verg", "vergehen"), fill=ROT, size=30, anker="m"),
])

# A3 Fall: Ersatzkauf und Frage -------------------------------------------------------------------------------------------
folie([("neu", "Fall · Ersatzkauf in einem anderen Geschäft"), ("frage", "Fall · Die Frage")], [
    pl("In einem anderen Geschäft", 70, 40, "neu", fill=GELB, size=44),
    boden("neu"),
    ficon("tabler", "building-store", 250, 400, 190, "neu", fuell=GRUEN),
    kuehlschrank(560, BODEN, 200, "neu", fuell=ROT, name="fridge-off"),
    pl("600 € zurück?", 560, 470, beim("ma2", "Geld"), fill=WEISS, size=30, anker="m"),
    kuehlschrank(1000, BODEN, 230, beim("neu", "gleichen"), fuell=GRUEN),
    pl("700 €", 1000, 470, beim("neu", "siebenhundert"), fill=GELB, size=36, anker="m"),
    pl("100 € mehr", 1000, 560 - 160, beim("ma2", "hundert"), fill=ROT, size=32, anker="m"),
    *manfred(1560, BODEN, FH, [("neu", "denkt")], bis="ma2", erst="cut"),
    *redet("MA_aerger", 1560, BODEN, FH, "ma2", "frage"),
    *manfred(1560, BODEN, FH, [("frage", "denkt")], erst="cut"),
    ns("Manfred", 1560, BODEN, "neu", MA_F),
    blase("sprech", 640, 210, "ma2", 1300, 200, inhalt=["Ich will mein Geld zurück", "und die 100 € mehr!"], textsize=36,
          figur=("MA_aerger", 1560, BODEN, FH), bis="frage"),
    pl("Was kann Manfred verlangen?", 960, 150, "frage", fill=PINK, size=36, anker="m"),
    pl("Und in welcher Reihenfolge?", 960, 240, "frage2", fill=PINK, size=36, anker="m"),
])

# B Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Manfred kauft im Elektrogeschäft von Frau Kemper einen neuen Kühlschrank für 600 Euro. Am nächsten Tag liefert sie "
    "ihn in seine Küche. Am Abend ist er innen noch warm: Der Kompressor ist von Anfang an defekt.",
    "Manfred ruft an: „Der Kühlschrank kühlt nicht! Bringen Sie mir bitte innerhalb von 2 Wochen einen neuen.“ Frau Kemper "
    "sagt: „Ja, ich kümmere mich darum.“ Doch sie vergisst den Auftrag, und die 2 Wochen vergehen. Manfred kauft "
    "woanders einen gleichen Kühlschrank für 700 Euro. Er will sein Geld zurück und die 100 Euro mehr.",
], "Was kann Manfred verlangen, und in welcher Reihenfolge?")

# C § 437 BGB (Wortlaut) ---------------------------------------------------------------------------------------------------
W437 = ["„Ist die Sache mangelhaft, kann der Käufer, wenn die Voraussetzungen",
        "der folgenden Vorschriften vorliegen und soweit nicht ein anderes",
        "bestimmt ist,",
        "1. nach § 439 Nacherfüllung verlangen,",
        "2. nach den §§ 440, 323 und 326 Abs. 5 von dem Vertrag zurücktreten",
        "oder nach § 441 den Kaufpreis mindern und",
        "3. nach den §§ 440, 280, 281, 283 und 311a Schadensersatz oder",
        "nach § 284 Ersatz vergeblicher Aufwendungen verlangen.“"]
w437, w437_y = wortlaut(80, 170, 1100, W437, "§ 437 BGB", beim("norm", "Paragraf"), marken=[
    (0, "Ist die Sache mangelhaft", "w1"),
    (3, "Nacherfüllung", beim("w1", "Nacherfüllung")),
    (4, "zurücktreten", beim("w2", "zurücktreten")),
    (5, "den Kaufpreis mindern", beim("w2", "mindern")),
    (6, "Schadensersatz", beim("w3", "Schadensersatz")),
    (7, "Ersatz vergeblicher Aufwendungen", beim("w3", "Ersatz")),
    (0, "wenn die Voraussetzungen", "verw"), (1, "der folgenden Vorschriften vorliegen", "verw")], size=30)
folie([("norm", "Käuferrechte · § 437 BGB › Wortlaut"), ("verw", "Käuferrechte · § 437 BGB › Verweis auf die Einzelvorschriften")],
      rechts_frei([
    *tafel("norm", "Die Käuferrechte: § 437 BGB"),
    *w437,
    blk(110, w437_y + 25, 300, 100, BLAU, beim("w1", "erstens"), [("1. Nacherfüllung", "ExtraBold", 32, INK)]),
    blk(430, w437_y + 25, 400, 100, GELB, beim("w2", "zweitens"), [("2. Rücktritt, Minderung", "ExtraBold", 32, INK)]),
    blk(850, w437_y + 25, 320, 100, GRUEN, beim("w3", "drittens"), [("3. Schadensersatz", "ExtraBold", 32, INK)]),
    z("Jede Nummer verweist: Voraussetzungen dort prüfen", 110, w437_y + 150, "verw", "Bold", 34),
    *requisit([("norm", FRIDGE, "der Kühlschrank", WEISS), ("verw", ("tabler", "list-check", 120, WEISS), "Verweis", GELB)]),
    *paar("norm", [("norm", "ruhig"), ("w2", "sorge"), ("verw", "denkt")], [("norm", "denkt"), ("w2", "zufrieden"),
                                                                            ("verw", "denkt")]),
]))

# D I. Gemeinsame Voraussetzungen ------------------------------------------------------------------------------------------
folie([("vor", "I. Voraussetzungen › Kaufvertrag, Sachmangel, kein Ausschluss"),
       ("vsub", "I. Voraussetzungen › Sachmangel bei Gefahrübergang, § 434 Abs. 3 Satz 1 Nr. 1 BGB"),
       ("vok", "I. Voraussetzungen › kein Ausschluss")], rechts_frei([
    *tafel("vor", "I. Gemeinsame Voraussetzungen"),
    z("1. wirksamer Kaufvertrag, § 433 BGB", 160, 190, "v1", "Bold", 34),
    z("2. Sachmangel bei Gefahrübergang, §§ 434, 446 BGB", 160, 250, "v2", "Bold", 34),
    z("3. kein Ausschluss der Mängelrechte", 160, 310, "v3", "Bold", 34),
    z("Kühlschrank kühlt nicht: nicht geeignet für die", 160, 410, "vsub", size=32),
    z("gewöhnliche Verwendung, § 434 Abs. 3 Satz 1 Nr. 1 BGB", 160, 455, beim("vsub", "gewöhnliche"), size=32),
    z("Kompressor schon bei der Übergabe defekt", 160, 520, "vgef", size=32),
    ok(125, 270, "vgef", gr=20),
    pl("Mangel im Detail: Folge zu § 434 BGB", 110, 610, "v059", fill=WEISS, size=30),
    z("Ausschluss: keiner", 160, 720, "vok", size=32),
    ok(125, 330, "vok", gr=20),
    *requisit([("vor", FRIDGE, "der Kühlschrank", WEISS), ("vsub", FRIDGE_OFF, "kühlt nicht", ROT),
               ("v059", ("tabler", "device-tv", 120, WEISS), "Folge zu § 434", GELB), ("vok", ("tabler", "shield-check", 120, GRUEN), "kein Ausschluss", GRUEN)]),
    *paar("vor", [("vor", "ruhig"), ("vsub", "sorge"), ("vok", "ernst")], [("vor", "denkt"), ("vsub", "sorge"),
                                                                          ("vok", "denkt")]),
]))

# E1 II. Nacherfüllung, Wortlaut § 439 Abs. 1 ----------------------------------------------------------------------------
W439 = ["„Der Käufer kann als Nacherfüllung nach seiner Wahl die Beseitigung",
        "des Mangels oder die Lieferung einer mangelfreien Sache verlangen.“"]
w439, w439_y = wortlaut(80, 290, 1100, W439, "§ 439 Abs. 1 BGB", "w439", marken=[
    (0, "nach seiner Wahl", beim("w439", "Wahl")), (0, "Beseitigung", beim("w439", "Beseitigung")),
    (1, "des Mangels", beim("w439", "Beseitigung")), (1, "Lieferung einer mangelfreien Sache", beim("w439", "Lieferung"))],
    size=30)
folie([("ne", "II. Nacherfüllung › Vorrang, §§ 437 Nr. 1, 439 BGB"), ("w439", "II. Nacherfüllung › Wahlrecht, § 439 Abs. 1 BGB")],
      rechts_frei([
    *tafel("ne", "II. Nacherfüllung, § 439 BGB"),
    z("An erster Stelle: Der Verkäufer bekommt", 110, 180, beim("ne", "Sie"), "Bold", 34),
    z("eine zweite Chance.", 110, 228, beim("ne", "zweite"), "Bold", 34),
    *w439,
    blk(110, w439_y + 40, 1040, 100, GRUEN, "wahl", [("Manfred wählt: einen neuen Kühlschrank", "ExtraBold", 36, INK)]),
    *requisit([("ne", FRIDGE, "Nacherfüllung", BLAU), (beim("ne", "zweite"), ("tabler", "refresh", 120, WEISS), "zweite Chance", GELB),
               (beim("w439", "Beseitigung"), ("tabler", "tools", 120, WEISS), "Beseitigung", WEISS),
               (beim("w439", "Lieferung"), FRIDGE, "Lieferung", WEISS),
               ("wahl", ("tabler", "fridge", 120, GRUEN), "neuer Kühlschrank", GRUEN)]),
    *paar("ne", [("ne", "ruhig"), ("w439", "denkt")], [("ne", "denkt"), ("wahl", "zufrieden")]),
]))

# E2 § 439 Abs. 2–4 --------------------------------------------------------------------------------------------------------
folie([("kost", "II. Nacherfüllung › Kosten, § 439 Abs. 2 BGB"), ("einbau", "II. Nacherfüllung › Aus- und Einbau, § 439 Abs. 3 BGB"),
       ("verw4", "II. Nacherfüllung › Verweigerung, § 439 Abs. 4 BGB")], rechts_frei([
    *tafel("kost", "Nacherfüllung: Kosten und Grenzen"),
    z("Abs. 2: Die Kosten trägt der Verkäufer,", 110, 190, "kost", "Bold", 34),
    z("etwa Transport, Wege, Arbeit und Material", 150, 245, beim("kost", "Transport"), size=34),
    z("Abs. 3: bestimmungsgemäß eingebaut?", 110, 340, "einbau", "Bold", 34),
    z("Dann auch Ausbau und Einbau", 150, 395, beim("einbau", "Ausbau"), size=34),
    z("Abs. 4: Verweigerung der gewählten Art,", 110, 490, "verw4", "Bold", 34),
    z("wenn nur mit unverhältnismäßigen Kosten möglich", 150, 545, beim("verw4", "unverhältnismäßigen"), size=34),
    blk(110, 630, 1040, 100, GELB, "andere", [("Dann: Anspruch nur auf die andere Art", "ExtraBold", 36, INK)]),
    *requisit([("kost", ("tabler", "truck-delivery", 150, WEISS), "Verkäufer zahlt", GRUEN),
               ("einbau", ("tabler", "hammer", 120, WEISS), "Ausbau und Einbau", WEISS),
               ("verw4", ("tabler", "calculator", 110, WEISS), "unverhältnismäßig?", ROT),
               ("andere", ("tabler", "arrows-exchange", 130, WEISS), "andere Art", GELB)]),
    *paar("kost", [("kost", "ruhig"), ("verw4", "denkt")], [("kost", "zufrieden"), ("verw4", "denkt")]),
]))

# F1 III. Frist zur Nacherfüllung als Brücke ------------------------------------------------------------------------------
folie([("brue", "III. Frist zur Nacherfüllung › Brücke zu den weiteren Rechten"),
       ("fsub", "III. Frist zur Nacherfüllung › Manfred: 2 Wochen")], rechts_frei([
    *tafel("brue", "III. Frist zur Nacherfüllung"),
    blk(110, 180, 1040, 100, GELB, beim("brue", "Brücke"), [("Brücke zu den weiteren Rechten", "ExtraBold", 36, INK)]),
    z("Rücktritt, Minderung, Schadensersatz statt der Leistung:", 110, 320, beim("brue", "Rücktritt"), "Bold", 32),
    z("grundsätzlich erst nach erfolgloser angemessener Frist", 110, 370, beim("brue", "angemessene"), size=32),
    zit("§§ 323 Abs. 1, 441 Abs. 1, 281 Abs. 1 BGB", 110, 420, beim("brue", "angemessene")),
    blk(110, 480, 1040, 90, LILA, "bgh1", [("So sichert das Gesetz den Vorrang der Nacherfüllung", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 26.8.2020 – VIII ZR 351/19, Rn. 47 f.", 110, 585, "bgh1"),
    ok(140, 680, "fsub", gr=22),
    z("Manfred: 2 Wochen gesetzt, ungenutzt abgelaufen", 185, 660, "fsub", "Bold", 34),
    *requisit([("brue", ("tabler", "hourglass", 110, WEISS), "Frist", GELB),
               ("fsub", ("tabler", "calendar-time", 120, WEISS), "2 Wochen", ROT)]),
    *paar("brue", [("brue", "ruhig"), ("fsub", "sorge")], [("brue", "denkt"), ("fsub", "zufrieden")]),
]))

# F2 Entbehrlichkeit, § 475d ---------------------------------------------------------------------------------------------
folie([("entb", "III. Frist zur Nacherfüllung › entbehrlich, §§ 323 Abs. 2, 440, 326 Abs. 5 BGB"),
       ("p475d", "III. Frist zur Nacherfüllung › Verbrauchsgüterkauf, § 475d BGB")], rechts_frei([
    *tafel("entb", "Frist entbehrlich, etwa"),
    z("1. ernsthafte und endgültige Verweigerung", 110, 190, "entb", "Bold", 34),
    zit("§ 323 Abs. 2 Nr. 1, § 281 Abs. 2 BGB", 150, 240, "entb"),
    z("2. Nacherfüllung fehlgeschlagen, § 440 BGB:", 110, 300, "fehl", "Bold", 34),
    z("Nachbesserung in der Regel nach 2. erfolglosem Versuch", 150, 352, beim("fehl", "Nachbesserung"), size=32),
    z("3. Nacherfüllung unmöglich", 110, 440, "unm", "Bold", 34),
    zit("§ 326 Abs. 5, §§ 283, 311a Abs. 2 BGB", 150, 490, "unm"),
    blk(110, 560, 1040, 90, GELB, "p475d", [("Verbrauchsgüterkauf, § 475d BGB:", "ExtraBold", 34, INK)]),
    z("Mitteilung des Mangels und angemessene Zeit", 150, 675, beim("p475d", "Mitteilung"), size=32),
    z("verstrichen: genügt", 150, 722, beim("p475d", "verstreichen"), size=32),
    pl("Unternehmerin", X1, 230, beim("p475d", "Unternehmer"), fill=GRUEN, size=28, anker="m"),
    pl("Verbraucher", X2, 300, beim("p475d", "Verbrauchsgüterkauf"), fill=BLAU, size=28, anker="m"),
    *requisit([("entb", ("tabler", "hand-stop", 120, WEISS), "Verweigerung", ROT),
               (beim("fehl", "zweiten"), ("tabler", "tools", 120, WEISS), "2 Versuche", ROT),
               ("unm", FRIDGE_OFF, "unmöglich", ROT), ("p475d", None, None, None)]),
    *paar("entb", [("entb", "ruhig"), ("unm", "denkt"), ("p475d", "ernst")], [("entb", "denkt"), ("p475d", "zufrieden")]),
]))

# G1 IV. Rücktritt -----------------------------------------------------------------------------------------------------------
folie([("rt", "IV. Rücktritt › §§ 437 Nr. 2, 440, 323 BGB"), ("erh", "IV. Rücktritt › Erheblichkeit, § 323 Abs. 5 Satz 2 BGB"),
       ("rfolge", "IV. Rücktritt › Rückgewähr, § 346 Abs. 1 BGB")], rechts_frei([
    *tafel("rt", "IV. Rücktritt"),
    z("§ 437 Nr. 2 mit § 323 BGB", 110, 180, beim("rt", "Paragraf"), "Bold", 34),
    z("bei unmöglicher Nacherfüllung: § 326 Abs. 5 BGB", 110, 235, "rt2", size=32),
    z("Ausgeschlossen bei unerheblicher Pflichtverletzung,", 110, 320, "erh", "Bold", 32),
    z("§ 323 Abs. 5 Satz 2 BGB", 110, 365, beim("erh", "unerheblich"), "Bold", 32),
    z("Behebbarer Mangel: Beseitigung über 5 % des", 110, 435, "bgh2", size=32),
    z("Kaufpreises – in der Regel erheblich", 110, 480, beim("bgh2", "fünf"), size=32),
    zit("BGH, Urt. v. 28.5.2014 – VIII ZR 94/13, Leitsatz 2, Rn. 12", 110, 528, beim("bgh2", "fünf")),
    ok(140, 610, "rsub", gr=22), z("Kühlschrank kühlt gar nicht: erheblich", 185, 590, "rsub", "Bold", 34),
    blk(110, 670, 1040, 100, GRUEN, "rfolge", [("600 € zurück, Zug um Zug gegen den Kühlschrank", "ExtraBold", 32, INK)]),
    zit("Rücktrittserklärung § 349, Rückgewähr §§ 346 Abs. 1, 348 BGB", 110, 785, "rfolge"),
    *requisit([("rt", FRIDGE_OFF, "Rücktritt", GELB), (beim("bgh2", "fünf"), ("tabler", "percentage", 110, WEISS), "5 %", GELB),
               ("rsub", FRIDGE_OFF, "kühlt gar nicht", ROT),
               ("rfolge", ("tabler", "cash-banknote", 150, GRUEN), "600 € zurück", GRUEN)]),
    *paar("rt", [("rt", "ruhig"), ("rsub", "sorge")], [("rt", "denkt"), ("rfolge", "froh")]),
]))

# G2 Minderung, § 441 --------------------------------------------------------------------------------------------------------
folie([("mi", "IV. Minderung › § 441 BGB"), ("mre", "IV. Minderung › Berechnung, § 441 Abs. 3 BGB")], rechts_frei([
    *tafel("mi", "IV. Oder: Minderung, § 441 BGB"),
    z("Statt zurückzutreten: Kaufpreis mindern", 110, 180, "mi", "Bold", 34),
    z("auch bei unerheblichem Mangel, § 441 Abs. 1 Satz 2", 110, 235, "mi2", size=32),
    z("Abwandlung: nur das Gefrierfach ist defekt", 110, 320, "mbsp", "Bold", 34),
    z("Im Verhältnis, Werte bei Vertragsschluss:", 110, 405, "mre", "Bold", 32),
    z("ohne Mangel 800 €, mit Mangel 600 €", 150, 455, beim("mre", "achthundert"), size=32),
    pl("ein Viertel weniger", 150, 515, beim("mre", "Viertel"), fill=ROT, size=30),
    blk(110, 600, 1040, 110, GELB, beim("mre2", "von"), [("600 € × 600 € : 800 € = 450 €", "ExtraBold", 40, INK)]),
    *requisit([("mi", ("tabler", "receipt", 110, WEISS), "Preis mindern", GELB),
               ("mbsp", ("tabler", "snowflake-off", 120, WEISS), "Gefrierfach defekt", ROT),
               ("mre", ("tabler", "calculator", 110, WEISS), "im Verhältnis", GELB),
               (beim("mre2", "vierhundertfünfzig"), ("tabler", "coins", 120, GELB), "450 €", GELB)]),
    *paar("mi", [("mi", "ruhig"), ("mre2", "denkt")], [("mi", "denkt"), ("mbsp", "zufrieden"), ("mre", "denkt")]),
]))

# H1 V. Schadensersatz: Normen -------------------------------------------------------------------------------------------
folie([("se", "V. Schadensersatz › § 437 Nr. 3 BGB"), ("se1", "V. Schadensersatz › §§ 280 Abs. 1, 3, 281 BGB"),
       ("se2", "V. Schadensersatz › §§ 283, 311a Abs. 2 BGB")], rechts_frei([
    *tafel("se", "V. Schadensersatz, § 437 Nr. 3 BGB"),
    z("Behebbarer Mangel:", 110, 200, "se1", "Bold", 34),
    z("§§ 280 Abs. 1, 3, 281 BGB – wieder mit Frist", 150, 255, beim("se1", "Paragraf"), size=34),
    z("Nacherfüllung unmöglich:", 110, 350, "se2", "Bold", 34),
    z("§ 283 BGB", 150, 405, beim("se2", "Paragraf"), size=34),
    z("schon bei Vertragsschluss unmöglich:", 110, 500, "se3", "Bold", 34),
    z("§ 311a Abs. 2 BGB", 150, 555, beim("se3", "Paragraf"), size=34),
    *requisit([("se", ("tabler", "scale", 130, WEISS), "Schadensersatz", GELB),
               (beim("se1", "Frist"), ("tabler", "hourglass", 110, WEISS), "mit Frist", GELB),
               ("se2", FRIDGE_OFF, "unmöglich", ROT)]),
    *paar("se", [("se", "ruhig"), ("se2", "denkt")], [("se", "denkt"), ("se1", "zufrieden"), ("se2", "denkt")]),
]))

# H2 Schadensersatz am Fall ---------------------------------------------------------------------------------------------
folie([("vm", "V. Schadensersatz › Vertretenmüssen, § 280 Abs. 1 Satz 2 BGB"),
       ("dk", "V. Schadensersatz › Mehrkosten statt der Leistung, § 281 BGB"),
       ("p325", "V. Schadensersatz › neben dem Rücktritt, § 325 BGB"),
       ("p284", "V. Schadensersatz › Aufwendungsersatz, § 284 BGB")], rechts_frei([
    *tafel("vm", "V. Schadensersatz: der Fall"),
    z("Vertretenmüssen vermutet, § 280 Abs. 1 Satz 2 BGB", 110, 180, "vm", "Bold", 34),
    nein(140, 260, beim("vmsub", "entlasten"), gr=20),
    z("Frau Kemper: zugesagt und vergessen", 185, 240, "vmsub", size=32),
    z("keine Entlastung", 185, 285, beim("vmsub", "entlasten"), size=32),
    zit("Bezugspunkt Nacherfüllung: BGH, Urt. v. 17.10.2012 – VIII ZR 226/11, Rn. 12", 110, 335, beim("vmsub", "entlasten")),
    z("Mehrkosten Ersatzkauf: 700 € – 600 € = 100 €", 110, 400, "dk", "Bold", 34),
    blk(110, 455, 1040, 90, GRUEN, beim("dk", "Schadensersatz"), [("100 € als Schadensersatz statt der Leistung", "ExtraBold", 34, INK)]),
    zit("Deckungskauf: BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, Leitsatz, Rn. 13", 110, 560, beim("dk", "Schadensersatz")),
    z("Rücktritt schließt Schadensersatz nicht aus, § 325 BGB", 110, 620, "p325", "Bold", 32),
    z("Anstelle des Schadensersatzes statt der Leistung:", 110, 700, "p284", size=32),
    z("Ersatz vergeblicher Aufwendungen, § 284 BGB", 110, 745, beim("p284", "Paragraf"), "Bold", 32),
    *requisit([("vm", ("tabler", "scale", 130, WEISS), "vermutet", GELB),
               ("vmsub", ("tabler", "calendar-x", 120, WEISS), "vergessen", ROT),
               ("dk", ("tabler", "cash-banknote", 150, GRUEN), "+100 €", GRUEN),
               ("p325", ("tabler", "arrows-exchange", 130, WEISS), "Rücktritt + Schadensersatz", GELB),
               ("p284", ("tabler", "receipt", 110, WEISS), "Aufwendungen", WEISS)]),
    *paar("vm", [("vm", "ruhig"), ("vmsub", "sorge"), ("p284", "denkt")], [("vm", "denkt"), ("dk", "zufrieden"),
                                                                          ("p284", "denkt")]),
]))

# I Ergebnis, Verjährung ------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Rücktritt und Schadensersatz"), ("p438", "Ausblick · Verjährung, § 438 BGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 100, GRUEN, beim("erg", "zurücktreten"), [("Rücktritt: 600 € zurück", "ExtraBold", 40, INK)]),
    blk(110, 320, 1040, 100, GRUEN, "erg2", [("dazu 100 € Schadensersatz", "ExtraBold", 40, INK)]),
    z("Verjährung: Nacherfüllung und Schadensersatz", 110, 490, "p438", "Bold", 34),
    z("in der Regel 2 Jahre ab Ablieferung", 150, 545, beim("p438", "zwei"), size=34),
    zit("§ 438 Abs. 1 Nr. 3, Abs. 2 BGB", 150, 600, beim("p438", "Paragraf")),
    *requisit([("erg", ("tabler", "cash-banknote", 150, GRUEN), "600 € zurück", GRUEN),
               ("erg2", ("tabler", "cash-banknote", 150, GRUEN), "+ 100 €", GRUEN),
               ("p438", ("tabler", "calendar-time", 120, WEISS), "2 Jahre", GELB)]),
    *paar("erg", [("erg", "sorge"), ("p438", "ernst")], [("erg", "froh"), ("p438", "denkt")]),
]))

# J Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Reihenfolge der Prüfung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe in dieser Reihenfolge:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("1. Voraussetzungen des § 437 BGB", 150, 300, beim("tipp", "Voraussetzungen"), size=36),
    z("2. das konkrete Recht mit voller Normkette", 150, 370, "tipp1", size=36),
    z("3. bei Rücktritt, Minderung und Schadensersatz", 150, 440, "tipp2", size=36),
    z("statt der Leistung: zuerst die Frist", 185, 495, beim("tipp2", "statt"), size=36),
    z("zur Nacherfüllung", 185, 550, beim("tipp2", "Frist"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k4", "Klausurschema › Rücktritt, Minderung, Schadensersatz")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Käuferrechte, § 437 BGB"), 110, 90, "sch", 44),
    z("I. Voraussetzungen", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("Kaufvertrag, Sachmangel bei Gefahrübergang, kein Ausschluss", K2, 242, beim("k1", "Kaufvertrag"), size=32, rechts=1820),
    z("II. Nacherfüllung, §§ 437 Nr. 1, 439 BGB", K1, 315, "k2", "Bold", 38, rechts=1820),
    z("nach Wahl des Käufers", K2, 367, beim("k2", "Wahl"), size=32, rechts=1820),
    z("III. Frist zur Nacherfüllung", K1, 440, "k3", "Bold", 38, rechts=1820),
    z("erfolglos oder entbehrlich (§§ 323 Abs. 2, 440, 326 Abs. 5, 475d BGB)", K2, 492, beim("k3", "erfolglos"), size=32,
      rechts=1820),
    z("IV. Rücktritt, §§ 437 Nr. 2, 323 BGB: bei erheblichem Mangel", K1, 565, "k4", "Bold", 38, rechts=1820),
    z("oder Minderung, § 441 BGB", K2, 617, beim("k4", "Minderung"), size=32, rechts=1820),
    z("V. Schadensersatz, §§ 437 Nr. 3, 280, 281, 283, 311a BGB", K1, 690, "k5", "Bold", 38, rechts=1820),
    z("Vertretenmüssen vermutet", K2, 742, beim("k5", "vermutetem"), size=32, rechts=1820),
    z("oder Ersatz vergeblicher Aufwendungen, § 284 BGB", K2, 794, beim("k5", "Ersatz"), size=32, rechts=1820),
])

# L Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst bekommt der Verkäufer", 0)], [("seine ", 0), ("zweite Chance", "a"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "zweite")}),
    *markertext([[("Wer zurücktreten, mindern oder", 0)], [("Schadensersatz statt der Leistung will,", 0)],
                 [("braucht grundsätzlich eine", 0)], [("erfolglose Frist", "b"), (" zur Nacherfüllung.", 0)]],
                750, 480, 40, "m2", {"b": beim("m2", "erfolglose")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
