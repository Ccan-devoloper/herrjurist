"""Folge 070 · Explodierende Flasche: Produzentenhaftung nach § 823 I BGB – Serienstandard Open Peeps (Katzenkönig).
Erfundener Ausgangsfall (Plan-Hook): Bettina will zu Hause eine Mehrweg-Mineralwasserflasche öffnen, die Flasche
explodiert, ein Splitter trifft ihr Auge (keine Wunde, nur abstrakte Augenklappe). Gutachten: feiner Haarriss. Herr Kroll
betreibt den Mineralbrunnen (Hersteller). Echte Fälle: Hühnerpest (BGHZ 51, 91), Limonadenflasche (BGHZ 104, 323),
Mineralwasserflasche II (BGHZ 129, 353) – ohne Figuren, nur Symbole.
Szenen laut ../SZENENPLAN.md: A1 Küche, A2 Mineralbrunnen und Frage, B Sachverhalt, C § 823 I (Wortlaut) und Beweisnot,
D Herstellerpflichten, E1 Hühnerpest (Fall), E2 Hühnerpest (Beweisregel), F1 Befundsicherung, F2 Mineralwasserflasche II,
G Ausreißer, H1/H2 Lösung, I § 1 ProdHaftG (Wortlaut), J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Ein Handlungsgeräusch (berstende Flasche, siehe ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im
Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 067 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern, im Sprechtext als Wörter."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_070/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_070/" in n:
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





BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel: Bettina links, Herr Kroll rechts
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BE_F, KR_F = BLAU, GRUEN                    # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def boden(cue, hart_=False, x0=40, x1=1880):
    e = linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def bettina(cx, unten, hoehe, folge, **k):
    return fig("BE", cx, unten, hoehe, folge, **k)


def kroll(cx, unten, hoehe, folge, **k):
    return fig("KR", cx, unten, hoehe, folge, **k)


def paar(c0, be_folge, kr_folge):
    """Tafelszene: Bettina links (X1), Herr Kroll rechts (X2), beide blicken zur Tafel."""
    return [*bettina(X1, FB, FR, be_folge), ns("Bettina", X1, FB, c0, BE_F),
            *kroll(X2, FB, FR, kr_folge, d=0.2), ns("Herr Kroll", X2, FB, c0, KR_F, d=0.2)]


def nur_kroll(c0, folge):
    return [*kroll(FX, FB, FR, folge), ns("Herr Kroll", FX, FB, c0, KR_F)]


def nur_bettina(c0, folge):
    return [*bettina(FX, FB, FR, folge), ns("Bettina", FX, FB, c0, BE_F)]


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


SCALE = ("tabler", "scale", 130, WEISS)
FLASCHE = ("tabler", "bottle", 70, GRUEN)
FABRIK = ("tabler", "building-factory-2", 150, WEISS)

# A1 Fall: in der Küche ------------------------------------------------------------------------------------------------
BX = 1300                                    # Bettina (blickt nach links zum Tisch, ihre Hand bei x ≈ 1190, y ≈ 562)
HX, HY = 1186, 598                           # Flasche in ihrer Hand: Mitte, Unterkante
folie([(NULL, "Fall · In der Küche"), ("knall", "Fall · Die Flasche explodiert"), ("riss", "Fall · Das Gutachten")], [
    hart(pl("Ein Kasten Mineralwasser", 70, 40, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    # Kasten mit Mehrwegflaschen am Boden, Tisch
    *[hart(ficon("tabler", "bottle", 595 + i * 65, 775, 76, NULL, fuell=GRUEN)) for i in range(3)],
    hart(karte(545, 760, 220, 100, NULL, fill=GELB, rund=10, schatten=4, rand=5)),
    hart(karte(720, 636, 430, 26, NULL, fill=WEISS, rund=8, schatten=4, rand=5)),
    hart(linienzug([(770, 662), (770, BODEN)], NULL, breite=7, farbe=INK)),
    hart(linienzug([(1100, 662), (1100, BODEN)], NULL, breite=7, farbe=INK)),
    ficon("tabler", "shopping-cart", 300, 500, 130, beim("fall", "Supermarkt"), fuell=WEISS),
    pl("im Supermarkt gekauft", 300, 560, beim("fall", "Supermarkt"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "recycle", 300, 700, 90, beim("fall", "Mehrwegflaschen"), fuell=GRUEN),
    pl("Mehrwegflaschen aus Glas", 300, 740, beim("fall", "Mehrwegflaschen"), fill=GRUEN, size=30, anker="m"),
    *bettina(BX, BODEN, FH, [(NULL, "ruhig"), ("oeffnen", "froh"), ("knall", "schreck"), ("auge", "sorge")],
             bis="b1", erst="cut"),
    *redet("BE_redet", BX, BODEN, FH, "b1", "riss"),
    *bettina(BX, BODEN, FH, [("riss", "denkt")], erst="cut"),
    hart(ns("Bettina", BX, BODEN, NULL, BE_F)),
    ficon("tabler", "bottle", HX, HY, 64, "oeffnen", fuell=GRUEN, anim="cut", bis="knall"),
    pl("will die Flasche öffnen", 960, 470, "oeffnen", fill=WEISS, size=30, anker="m", bis="knall"),
    szene(ficon("fluent-emoji-high-contrast", "collision", HX - 10, HY + 10, 130, "knall", anim="cut", bis="auge"),
          "070flasche*", 0.8, -0.06),
    ficon("tabler", "bottle-off", 1185, BODEN, 80, "auge", fuell=GRUEN, anim="cut"),
    pl("explodiert", 1000, 470, "knall", fill=ROT, size=34, anker="m", bis="riss"),
    pl("Splitter am Auge", 1540, 300, "auge", fill=ORANGE, size=30, anker="m", bis="b1"),
    ficon("tabler", "first-aid-kit", 1640, 520, 90, beim("auge", "ärztlich"), fuell=WEISS, bis="b1"),
    blase("sprech", 640, 220, "b1", 800, 230, inhalt=["Mein Auge! Die Flasche", "ist einfach geplatzt!"], textsize=36,
          figur=("BE_redet", BX, BODEN, FH), bis="riss"),
    ficon("tabler", "microscope", 960, 600, 110, "riss", fuell=WEISS),
    pl("Gutachten: feiner Haarriss im Glas", 940, 420, beim("riss", "Haarriss"), fill=GELB, size=32, anker="m"),
])

# A2 Fall: der Mineralbrunnen, Forderung und Frage -------------------------------------------------------------------------
KX, BX2 = 1000, 1580                         # Herr Kroll (blickt nach rechts zu Bettina), Bettina (blickt nach links)
folie([("kroll", "Fall · Der Hersteller"), ("ford", "Fall · Die Forderung"), ("frage", "Fall · Die Frage")], [
    pl("Der Mineralbrunnen von Herrn Kroll", 70, 40, "kroll", fill=GELB, size=44),
    boden("kroll"),
    ficon("tabler", "building-factory-2", 250, BODEN, 300, "kroll", fuell=WEISS),
    linienzug([(430, 760), (860, 760)], "kroll", breite=7, farbe=INK),
    *[ficon("tabler", "bottle", 470 + i * 90, 756, 44, "kroll", fuell=GRUEN) for i in range(5)],
    ficon("tabler", "eye", 650, 640, 80, "kr1", fuell=WEISS, bis="ford"),
    pl("Sichtkontrolle am Band", 650, 495, "kr1", fill=WEISS, size=28, anker="m", bis="ford"),
    *kroll(KX, BODEN, FH, [("kroll", "ruhig_r")], bis="kr1"),
    *redet("KR_redet_r", KX, BODEN, FH, "kr1", "ford"),
    *kroll(KX, BODEN, FH, [("ford", "denkt_r"), ("frage2", "sorge_r")], erst="cut"),
    ns("Herr Kroll, Hersteller", KX, BODEN, "kroll", KR_F),
    *bettina(BX2, BODEN, FH, [("kroll", "ernst"), ("ford", "ruhig2"), ("frage2", "denkt")], d=0.2),
    ns("Bettina", BX2, BODEN, "kroll", BE_F, d=0.2),
    blase("sprech", 790, 190, "kr1", 690, 245, inhalt=["Unsere Leute schauen sich jede Flasche an.",
                                                        "Vielleicht ist sie bei Ihnen heruntergefallen!"],
          textsize=30, figur=("KR_redet_r", KX, BODEN, FH), bis="ford"),
    ficon("tabler", "first-aid-kit", 1260, 220, 80, beim("ford", "Behandlungskosten"), fuell=WEISS),
    pl("Behandlungskosten", 1320, 160, beim("ford", "Behandlungskosten"), fill=WEISS, size=32),
    ficon("tabler", "coins", 1260, 320, 80, beim("ford", "Schmerzensgeld"), fuell=GELB),
    pl("Schmerzensgeld", 1320, 260, beim("ford", "Schmerzensgeld"), fill=WEISS, size=32),
    ficon("tabler", "shopping-cart", 160, 260, 90, "frage", fuell=WEISS),
    pl("Vertrag nur mit dem Supermarkt", 230, 190, "frage", fill=WEISS, size=32),
    pl("Haftet der Hersteller trotzdem?", 90, 300, "frage2", fill=PINK, size=34),
    pl("Wie beweist sie, was im Betrieb passiert ist?", 90, 390, beim("frage2", "Und"), fill=PINK, size=34),
])

# B Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Bettina kauft im Supermarkt einen Kasten Mineralwasser in Mehrwegflaschen aus Glas. Zu Hause will sie eine Flasche "
    "öffnen, da explodiert die Flasche. Ein Splitter trifft Bettina am Auge; sie muss ärztlich behandelt werden. Ein "
    "Gutachter findet an der Bruchstelle einen feinen Haarriss im Glas.",
    "Abgefüllt hat das Wasser der Mineralbrunnen von Herrn Kroll. Dort sehen Mitarbeiter die Flaschen am Band nur "
    "flüchtig an. Herr Kroll sagt: „Unsere Leute schauen sich jede Flasche an. Vielleicht ist sie bei Ihnen "
    "heruntergefallen!“ Bettina verlangt von ihm die Behandlungskosten und ein Schmerzensgeld.",
], "Haftet Herr Kroll, obwohl Bettina nur mit dem Supermarkt einen Vertrag hat?")

# C § 823 Abs. 1 BGB (Wortlaut) und Beweisnot ------------------------------------------------------------------------------
W823 = ["„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die",
        "Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht",
        "eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz",
        "des daraus entstehenden Schadens verpflichtet.“"]
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 1 BGB", "norm", marken=[
    (0, "vorsätzlich oder fahrlässig", beim("w823", "vorsätzlich")),
    (0, "den Körper", beim("w823", "Körper")), (1, "Gesundheit", beim("w823", "Gesundheit")),
    (2, "widerrechtlich verletzt", beim("w823", "widerrechtlich")),
    (2, "zum Ersatz", beim("w823", "Schaden")), (3, "des daraus entstehenden Schadens", beim("w823", "Schaden"))],
    size=32)
folie([("norm", "Anspruchsgrundlage · § 823 Abs. 1 BGB › Wortlaut"), ("bew", "Beweislast · Grundsatz: Anspruchsteller beweist"),
       ("bew2", "Beweislast · Problem: Blick in den Betrieb")], rechts_frei([
    *tafel("norm", "Ohne Vertrag: § 823 Abs. 1 BGB"),
    *w823,
    blk(110, w823_y + 40, 1040, 100, BLAU, "bew", [("Anspruchsteller beweist alle Tatsachen,", "ExtraBold", 32, INK),
                                                   ("auch das Verschulden", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91 (Gründe III. 3. bb)", 110, w823_y + 155, beim("bew", "Verschulden")),
    blk(110, w823_y + 215, 1040, 100, ROT, "bew2", [("Problem: Den Betrieb des Herstellers", "ExtraBold", 32, INK),
                                                     ("kann Bettina nicht einsehen", "ExtraBold", 32, INK)]),
    *requisit([("norm", SCALE, "§ 823 Abs. 1 BGB", GELB), ("bew", SCALE, "Grundsatz", BLAU),
               ("bew2", ("tabler", "eye-off", 120, WEISS), "Betrieb nicht einsehbar", ROT)]),
    *paar("norm", [("norm", "ruhig2"), ("bew", "denkt"), ("bew2", "sorge")], [("norm", "ruhig"), ("bew2", "froh")]),
]))

# D Herstellerpflichten -------------------------------------------------------------------------------------------------------
folie([("vsp", "Herstellerpflichten · Verkehrssicherungspflichten"), ("p1", "Herstellerpflichten › 1. Konstruktion"),
       ("p2", "Herstellerpflichten › 2. Fabrikation"), ("p3", "Herstellerpflichten › 3. Instruktion"),
       ("p4", "Herstellerpflichten › 4. Produktbeobachtung"), ("pfall", "Herstellerpflichten › Haarriss: Fabrikationsfehler")],
      rechts_frei([
    *tafel("vsp", "Verkehrssicherungspflichten des Herstellers", size=42),
    z("Gefahrenquelle: notwendige und zumutbare Vorkehrungen", 110, 170, beim("vsp", "notwendigen"), size=32),
    zit("BGH, Urt. v. 21.3.2023 – VI ZR 1369/20, Rn. 18 f.", 110, 215, beim("vsp", "notwendigen")),
    z("1. Konstruktion: Planung mit gebotenem Sicherheitsstandard", 110, 275, "p1", "Bold", 32),
    zit("BGH, Urt. v. 16.6.2009 – VI ZR 107/08, BGHZ 181, 253, Rn. 15", 150, 320, "p1"),
    z("2. Fabrikation: kein Stück weicht vom sicheren Plan ab", 110, 380, "p2", "Bold", 32),
    z("3. Instruktion: Warnung vor Gefahren bei Gebrauch", 110, 465, "p3", "Bold", 32),
    z("und naheliegendem Fehlgebrauch", 150, 510, beim("p3", "naheliegenden"), size=32),
    zit("BGH, Urt. v. 16.6.2009 – VI ZR 107/08, BGHZ 181, 253, Rn. 23", 150, 555, beim("p3", "naheliegenden")),
    z("4. Produktbeobachtung: auch nach dem Inverkehrbringen", 110, 615, "p4", "Bold", 32),
    zit("BGH, Urt. v. 16.12.2008 – VI ZR 170/07, Rn. 10", 150, 660, beim("p4", "beobachten")),
    blk(110, 720, 1040, 90, GELB, "pfall", [("Haarriss in einer Flasche: Fabrikationsfehler", "ExtraBold", 32, INK)]),
    zit("vgl. BGH, Urt. v. 9.5.1995 – VI ZR 158/94, BGHZ 129, 353 (Gründe II. 1. b) aa)", 110, 822, "pfall"),
    ok(85, 400, "pfall", gr=18),
    *requisit([("vsp", FABRIK, "Gefahrenquelle", WEISS), ("p1", ("tabler", "ruler-2", 120, WEISS), "Konstruktion", WEISS),
               ("p2", FABRIK, "Fabrikation", WEISS), ("p3", ("tabler", "file-alert", 110, WEISS), "Instruktion", WEISS),
               ("p4", ("tabler", "zoom-check", 120, WEISS), "Produktbeobachtung", WEISS),
               ("pfall", FLASCHE, "Haarriss", GELB)]),
    *nur_kroll("vsp", [("vsp", "ruhig"), ("p2", "denkt"), ("pfall", "sorge")]),
]))

# E1 Hühnerpest-Fall (echt, ohne Figuren) ----------------------------------------------------------------------------------
folie([("huhn", "Hühnerpest-Fall · BGH 1968"), ("h1", "Hühnerpest-Fall · Sachverhalt"), ("h4", "Hühnerpest-Fall · kein Vertrag")], [
    pl("Der Hühnerpest-Fall", 70, 40, "huhn", fill=GELB, size=44),
    zit("BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91", 75, 120, "huhn", size=28),
    boden("huhn"),
    ficon("tabler", "building-factory-2", 330, BODEN, 300, "huhn", fuell=WEISS),
    pl("Impfstoffwerk", 330, BODEN + 22, "huhn", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "vaccine-bottle", 880, BODEN, 120, "h1", fuell=GRUEN),
    ficon("fluent-emoji-high-contrast", "syringe", 1010, BODEN - 40, 120, "h1"),
    pl("Tierarzt impft", 940, BODEN + 22, "h1", fill=WEISS, size=30, anker="m"),
    *[ficon("fluent-emoji-high-contrast", "chicken", 1380 + (i % 3) * 150, BODEN - (i // 3) * 140, 120, beim("h1", "Hühnerfarm"))
      for i in range(6)],
    pl("Hühnerfarm", 1530, BODEN + 22, beim("h1", "Hühnerfarm"), fill=GELB, size=30, anker="m"),
    pl("Hühnerpest bricht aus", 1530, 330, "h2", fill=ROT, size=32, anker="m"),
    pl("mehr als 4.000 Hühner verendet", 1530, 410, beim("h2", "viertausend"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "virus", 880, 640, 100, "h3", fuell=ROT),
    pl("bakteriell verunreinigt", 880, 450, "h3", fill=ROT, size=30, anker="m"),
    pl("wahrscheinlich beim Abfüllen", 880, 520, beim("h3", "wahrscheinlich"), fill=WEISS, size=28, anker="m"),
    linienzug([(470, 300), (1380, 300)], "h4", breite=6, farbe=INK),
    nein(925, 300, "h4", gr=26),
    pl("kein Vertrag mit dem Werk", 925, 200, "h4", fill=WEISS, size=30, anker="m"),
    pl("nur Deliktsrecht", 330, 470, beim("h4", "Deliktsrecht"), fill=GELB, size=32, anker="m"),
])

# E2 Hühnerpest: die Beweisregel -------------------------------------------------------------------------------------------
folie([("regel", "Hühnerpest-Fall › Geschädigte beweist den Produktfehler"),
       ("umkehr", "Hühnerpest-Fall › Beweislastumkehr beim Verschulden"), ("huhn2", "Hühnerpest-Fall › keine Entlastung")],
      rechts_frei([
    *tafel("regel", "Hühnerpest: die Beweisregel"),
    blk(110, 180, 1040, 150, BLAU, "regel", [("Geschädigte beweist: Produktfehler", "ExtraBold", 32, INK),
                                            ("verursacht den Schaden, aus dem Organisations-", "ExtraBold", 30, INK),
                                            ("und Gefahrenbereich des Herstellers", "ExtraBold", 30, INK)]),
    blk(110, 360, 1040, 90, GELB, "umkehr", [("Dann beweist der Hersteller: kein Verschulden", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91 (Gründe III., III. 3. bb)", 110, 462, "umkehr"),
    z("Grund: Er ist näher daran, überblickt die Produktion", 110, 520, "grund", "Bold", 32),
    z("Werk: Abfüllen von Hand, bessere Sicherungen fehlten", 150, 610, beim("huhn2", "Es"), size=32),
    nein(125, 630, beim("huhn2", "Es"), gr=18),
    z("nicht entlastet: Haftung dem Grunde nach", 150, 670, "huhn3", "Bold", 32),
    zit("BGHZ 51, 91 (Gründe III. 4.)", 150, 720, "huhn3"),
    *requisit([("regel", ("tabler", "zoom-check", 120, WEISS), "Produktfehler", BLAU),
               ("umkehr", SCALE, "Beweislastumkehr", GELB), ("grund", FABRIK, "näher daran", WEISS),
               ("huhn2", ("tabler", "vaccine-bottle", 110, GRUEN), "nicht entlastet", ROT)]),
    *paar("regel", [("regel", "denkt"), ("umkehr", "ok"), ("huhn3", "ruhig2")], [("regel", "ruhig"), ("umkehr", "sorge")]),
]))

# F1 Befundsicherung (Limonadenflasche) ----------------------------------------------------------------------------------------
folie([("mehr", "Befundsicherung · Wann entstand der Riss?"), ("limo", "Befundsicherung · Limonadenflasche 1988"),
       ("bumk", "Befundsicherung › Beweislastumkehr")], rechts_frei([
    *tafel("mehr", "Mehrwegflaschen: Befundsicherung"),
    z("Ein Haarriss kann auch später entstehen, etwa zu Hause", 110, 180, beim("mehr", "Ein"), size=32),
    pl("Fehler schon beim Verlassen des Betriebs?", 110, 240, "wann", fill=PINK, size=32),
    z("Befundsicherungspflicht", 110, 345, "limo", "Bold", 36),
    zit("BGH, Urt. v. 7.6.1988 – VI ZR 91/87, BGHZ 104, 323 (Limonadenflasche)", 110, 395, "limo"),
    z("Flaschen wieder befüllt: Zustand prüfen,", 150, 450, "befund", size=32),
    z("den Befund sichern", 150, 495, beim("befund", "Befund"), size=32),
    blk(110, 570, 1040, 90, GELB, "bumk", [("Pflicht verletzt: Beweislast kann sich umkehren", "ExtraBold", 32, INK)]),
    z("Hersteller beweist: Fehler nicht in seinem Bereich", 110, 690, beim("bumk", "Dann"), "Bold", 32),
    zit("BGHZ 129, 353 (Leitsatz 2, Gründe II. 2. a) mit BGHZ 104, 323, 330", 110, 740, beim("bumk", "Dann")),
    *requisit([("mehr", ("tabler", "home", 120, WEISS), "zu Hause entstanden?", WEISS),
               ("limo", ("tabler", "recycle", 120, GRUEN), "Mehrwegflaschen", GRUEN),
               ("befund", ("tabler", "clipboard-check", 110, WEISS), "Befund sichern", WEISS),
               ("bumk", SCALE, "Beweislastumkehr", GELB)]),
    *paar("mehr", [("mehr", "denkt"), ("bumk", "ok")], [("mehr", "froh"), ("wann", "denkt"), ("bumk", "sorge")]),
]))

# F2 Mineralwasserflasche II (echt, ohne Figur des Kindes) --------------------------------------------------------------------
folie([("mw", "Mineralwasserflasche II · 1995"), ("mw2", "Mineralwasserflasche II › Kontrolle jeder Flasche"),
       ("mw3", "Mineralwasserflasche II › Sichtkontrolle reicht kaum")], rechts_frei([
    *tafel("mw", "Mineralwasserflasche II"),
    zit("BGH, Urt. v. 9.5.1995 – VI ZR 158/94, BGHZ 129, 353", 110, 165, "mw", size=28),
    z("Mehrwegflasche explodiert in der Hand", 110, 230, beim("mw", "explodierte"), "Bold", 32),
    z("eines 9-jährigen Mädchens", 150, 275, beim("mw", "neunjährigen"), size=32),
    z("Splitter treffen ihr Auge", 150, 320, beim("mw", "Splitter"), size=32),
    z("Verlangt: Kontrollverfahren, das den Zustand", 110, 420, "mw2", "Bold", 32),
    z("jeder Flasche ermittelt", 150, 465, beim("mw2", "jeder"), "Bold", 32),
    ok(125, 485, beim("mw2", "jeder"), gr=18),
    z("Sichtkontrolle bei rund 4 Flaschen pro Sekunde:", 110, 565, "mw3", "Bold", 32),
    z("dafür kaum geeignet", 150, 610, beim("mw3", "kaum"), size=32),
    nein(125, 630, beim("mw3", "kaum"), gr=18),
    zit("BGHZ 129, 353 (Sachverhalt; Gründe II. 2. b) cc)", 110, 665, beim("mw3", "kaum")),
    *requisit([("mw", ("tabler", "bottle-off", 100, GRUEN), "Mehrwegflasche explodiert", ROT),
               ("mw2", ("tabler", "checklist", 110, WEISS), "jede Flasche", WEISS),
               ("mw3", ("tabler", "eye", 120, WEISS), "4 pro Sekunde", ROT)]),
    *nur_kroll("mw", [("mw", "ernst"), ("mw2", "denkt"), ("mw3", "ertappt")]),
]))

# G Ausreißer und Entlastung ---------------------------------------------------------------------------------------------------
folie([("aus", "Ausreißer und Entlastung")], rechts_frei([
    *tafel("aus", "Ausreißer und Entlastung"),
    pl("Alles Zumutbare getan?", 110, 180, "aus", fill=PINK, size=34),
    z("Ausreißer: trotz aller zumutbaren Vorkehrungen", 110, 290, "aus2", "Bold", 32),
    z("nicht zu vermeiden", 150, 335, beim("aus2", "nicht"), "Bold", 32),
    zit("BGHZ 51, 91 (Gründe III. 3. bb); BGHZ 129, 353 (Gründe I., II. 1. b) bb)", 110, 385, beim("aus2", "nicht")),
    blk(110, 450, 1040, 100, GRUEN, "aus3", [("Hersteller beweist das: kein Verschulden,", "ExtraBold", 32, INK),
                                            ("keine Haftung aus § 823 BGB", "ExtraBold", 32, INK)]),
    zit("vgl. BGHZ 129, 353 (Gründe III.)", 110, 565, beim("aus3", "Paragraf")),
    *requisit([("aus", ("tabler", "shield-check", 120, WEISS), "alles Zumutbare?", WEISS),
               ("aus2", FLASCHE, "Ausreißer", GELB), ("aus3", SCALE, "entlastet", GRUEN)]),
    *paar("aus", [("aus", "denkt"), ("aus3", "sorge")], [("aus", "denkt"), ("aus3", "froh")]),
]))

# H1 Lösung: Tatbestand und Befundsicherung -----------------------------------------------------------------------------------
folie([("loes", "Lösung · Bettina gegen Herrn Kroll, § 823 Abs. 1 BGB"), ("l1", "Lösung › 1. Rechtsgutsverletzung"),
       ("l2", "Lösung › 2. Produktfehler und Kausalität"), ("l3", "Lösung › 3. Befundsicherung verletzt")], rechts_frei([
    *tafel("loes", "Lösung: § 823 Abs. 1 BGB"),
    z("1. Rechtsgutsverletzung", 110, 180, "l1", "Bold", 34),
    z("Auge verletzt: Körper und Gesundheit", 150, 235, beim("l1", "Auge"), size=32),
    ok(125, 255, beim("l1", "Gesundheit"), gr=18),
    z("2. Produktfehler und Kausalität", 110, 320, "l2", "Bold", 34),
    z("Haarriss: Fabrikationsfehler, verursacht die Explosion", 150, 375, beim("l2", "Haarriss"), size=32),
    z("Beleg: das Gutachten", 150, 420, beim("l2", "belegt"), size=32),
    ok(125, 440, beim("l2", "belegt"), gr=18),
    z("3. Fehler aus dem Bereich des Herstellers?", 110, 505, "l3", "Bold", 34),
    z("nur flüchtige Sichtkontrolle am Band:", 150, 560, beim("l3", "flüchtig"), size=32),
    z("Befundsicherungspflicht verletzt", 150, 605, beim("l3", "Befundsicherungspflicht"), size=32),
    blk(110, 670, 1040, 90, GELB, beim("l3", "Deshalb"), [("Herr Kroll beweist: Riss entstand erst später", "ExtraBold", 32, INK)]),
    *requisit([("loes", ("tabler", "gavel", 120, WEISS), "Lösung", WEISS), ("l1", ("tabler", "eye", 120, WEISS), "Körper, Gesundheit", ORANGE),
               ("l2", ("tabler", "microscope", 110, WEISS), "Gutachten", WEISS),
               ("l3", ("tabler", "clipboard-check", 110, WEISS), "Befund nicht gesichert", ROT),
               (beim("l3", "Deshalb"), SCALE, "Beweislast bei Herrn Kroll", GELB)]),
    *paar("loes", [("loes", "ruhig2"), ("l2", "denkt"), (beim("l3", "Deshalb"), "ok")],
          [("loes", "ruhig"), ("l3", "ertappt")]),
]))

# H2 Lösung: Verschulden und Ergebnis ---------------------------------------------------------------------------------------------
folie([("l4", "Lösung › 4. Verschulden: Beweislastumkehr"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("l4", "Lösung: Verschulden und Ergebnis"),
    z("4. Verschulden", 110, 180, "l4", "Bold", 34),
    z("Hühnerpest-Regel: Herr Kroll müsste sich entlasten", 150, 235, beim("l4", "Hühnerpest"), size=32),
    z("Entlastung gelingt nicht", 150, 280, beim("l4", "gelingt"), size=32),
    nein(125, 300, beim("l4", "gelingt"), gr=18),
    blk(110, 370, 1040, 100, GRUEN, "erg", [("Herr Kroll haftet", "ExtraBold", 34, INK),
                                           ("nach § 823 Abs. 1 BGB", "ExtraBold", 32, INK)]),
    z("Behandlungskosten", 150, 520, beim("erg2", "Behandlungskosten"), size=34),
    ok(125, 540, beim("erg2", "Behandlungskosten"), gr=18),
    z("Schmerzensgeld, § 253 Abs. 2 BGB", 150, 580, beim("erg2", "Schmerzensgeld"), size=34),
    ok(125, 600, beim("erg2", "Schmerzensgeld"), gr=18),
    *requisit([("l4", SCALE, "Hühnerpest-Regel", GELB), ("erg", ("tabler", "gavel", 120, WEISS), "Herr Kroll haftet", GRUEN),
               (beim("erg2", "Behandlungskosten"), ("tabler", "first-aid-kit", 110, WEISS), "Behandlungskosten", WEISS),
               (beim("erg2", "Schmerzensgeld"), ("tabler", "coins", 120, GELB), "Schmerzensgeld", GELB)]),
    *paar("l4", [("l4", "denkt"), ("erg", "ok")], [("l4", "sorge"), ("erg", "ernst")]),
]))

# I Abgrenzung: § 1 ProdHaftG (Wortlaut) -----------------------------------------------------------------------------------------
W1 = ["„Wird durch den Fehler eines Produkts jemand getötet, sein Körper",
      "oder seine Gesundheit verletzt oder eine Sache beschädigt, so ist der",
      "Hersteller des Produkts verpflichtet, dem Geschädigten den daraus",
      "entstehenden Schaden zu ersetzen. …“"]
w1, w1_y = wortlaut(80, 165, 1100, W1, "§ 1 Abs. 1 Satz 1 ProdHaftG", "w1", marken=[
    (0, "Fehler eines Produkts", beim("w1", "Fehler")), (1, "Gesundheit verletzt", beim("w1", "verletzt")),
    (2, "Hersteller", beim("w1", "Hersteller"))], size=30)
folie([("phg", "Abgrenzung · § 1 ProdHaftG"), ("ohne", "Abgrenzung › ohne Verschulden, auch für Ausreißer"),
       ("sach", "Abgrenzung › Sachschäden: 500 € selbst"), ("beide", "Abgrenzung › beide Ansprüche nebeneinander"),
       ("eu", "Abgrenzung › Reform: Richtlinie (EU) 2024/2853")], rechts_frei([
    *tafel("phg", "Daneben: Produkthaftungsgesetz"),
    *w1,
    z("ohne Verschulden, auch für Ausreißer", 110, w1_y + 30, "ohne", "Bold", 32),
    zit("BGHZ 129, 353 (Leitsatz 1; Gründe II. 1. b) bb)", 110, w1_y + 75, beim("ohne", "Ausreißer")),
    z("Sachschaden: 500 € selbst tragen, § 11 ProdHaftG", 110, w1_y + 125, "sach", "Bold", 32),
    z("nur andere, privat genutzte Sachen, § 1 Abs. 1 Satz 2", 150, w1_y + 170, beim("sach", "geschützt"), size=30),
    z("§ 15 Abs. 2 ProdHaftG: § 823 BGB bleibt daneben", 110, w1_y + 230, "beide", "Bold", 32),
    blk(110, w1_y + 290, 1040, 90, LILA, "eu", [("Richtlinie (EU) 2024/2853: Umsetzung bis 9.12.2026", "ExtraBold", 30, INK)]),
    *requisit([("phg", ("tabler", "book", 120, WEISS), "ProdHaftG", WEISS), ("ohne", FLASCHE, "auch Ausreißer", GELB),
               ("sach", ("tabler", "coins", 120, GELB), "500 € selbst", WEISS),
               ("beide", SCALE, "nebeneinander", GRUEN), ("eu", ("tabler", "refresh", 120, WEISS), "Reform läuft", LILA)]),
    *nur_bettina("phg", [("phg", "ruhig2"), ("ohne", "ok"), ("sach", "denkt"), ("eu", "ruhig2")]),
]))

# J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · getrennt prüfen, Verschulden bleibt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Getrennt prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("§ 1 ProdHaftG", 185, 270, beim("tipp", "eins"), size=34),
    z("§ 823 Abs. 1 BGB", 185, 320, beim("tipp", "achthundertdreiundzwanzig"), size=34),
    z("Nie: „Produzentenhaftung ohne Verschulden“", 150, 420, "tipp1", "Bold", 34),
    nein(125, 440, beim("tipp1", "ohne"), gr=18),
    z("Nur die Beweislast kehrt sich um", 150, 510, "tipp2", "Bold", 34),
    z("entlastet sich der Hersteller, haftet er nicht", 185, 560, beim("tipp2", "entlastet"), size=34),
    zit("vgl. BGHZ 51, 91 (Gründe II. 1. a), III. 3. bb)", 185, 610, beim("tipp2", "entlastet")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › Rechtswidrigkeit, Verschulden, Schaden")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Produzentenhaftung, § 823 Abs. 1 BGB"), 110, 90, "sch", 44),
    z("I. Tatbestand", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("Rechtsgutsverletzung, Verletzung einer Herstellerpflicht durch einen Produktfehler, Kausalität", K2, 255,
      beim("k1", "Rechtsgutsverletzung"), size=30, rechts=1820),
    z("Beweis: Fehler beweist der Geschädigte, bei Mehrwegflaschen hilft die Befundsicherung", K2, 305,
      "k1b", size=30, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 390, "k2", "Bold", 38, rechts=1820),
    z("III. Verschulden", K1, 475, "k3", "Bold", 38, rechts=1820),
    z("mit Beweislastumkehr zulasten des Herstellers", K2, 530, beim("k3", "Beweislastumkehr"), size=30, rechts=1820),
    z("IV. Schaden und Rechtsfolge", K1, 615, "k4", "Bold", 38, rechts=1820),
    z("mit Schmerzensgeld, § 253 Abs. 2 BGB", K2, 670, beim("k4", "Schmerzensgeld"), size=30, rechts=1820),
])

# L Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Den ", 0), ("Produktfehler", "a"), (" und seine Folgen", 0)],
                 [("beweist der Geschädigte.", 0)]],
                750, 320, 42, "merke", {"a": beim("merke", "Produktfehler")}),
    *markertext([[("Dass ihn ", 0), ("kein Verschulden", "b"), (" trifft,", 0)],
                 [("muss der Hersteller beweisen.", 0)]],
                750, 560, 42, "m2", {"b": beim("m2", "kein")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
