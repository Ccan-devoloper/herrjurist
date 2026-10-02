"""Folge 034 · Schwarzarbeit: Kein Werklohn, keine Mängelrechte, kein Geld zurück? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Muster BGHZ 198, 141: gepflasterte Auffahrt, bar ohne Rechnung): Frau Ziegler (Bestellerin) und der Pflasterer
Herr Fuchs. Szenen laut ../SZENENPLAN.md: A Die Einfahrt (Angebot, Anzahlung, Pflaster, Streit, Frage), B Sachverhalt,
C Vorfrage (Wortlaut § 134 BGB, § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG), D Der Verstoß im Fall, E Gegenfall einseitiger Verstoß,
F1/F2 Ansprüche von Herrn Fuchs (Wortlaut § 817 Satz 2 BGB), G1 Mängelrechte, G2 Anzahlung, H Ergebnis,
I Rechtsprechungslinie, J Streitstand nachträgliche Abrede, K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Geldscheine bei der Anzahlung, Hammer beim Pflastern; Freesound CC0).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns wie in
Folge 031 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_034/"


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


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=44):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
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
        if n.startswith(("bild:", "ficon:")) or "/op_034/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folge 031) --------------------------------------------
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


def zi(cx, unten, hoehe, folge, **k):
    return fig("ZI", cx, unten, hoehe, folge, **k)


def fu(cx, unten, hoehe, folge, **k):
    return fig("FU", cx, unten, hoehe, folge, **k)


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
ZI_F, FU_F = LILA, BLAU                     # Farben der Namensschilder
STEIN = (196, 198, 206, 255)                # Pflasterstein (Grau)
SAND = (236, 214, 170, 255)                 # Sandbett
ERDE = (214, 186, 150, 255)                 # alte Einfahrt (Erde)


# --- Einfahrt im Querschnitt: Sandbett und eine Reihe Pflastersteine (Bausteine im karte-Stil) ---------------------------
EX0, EX1 = 640, 1300                         # Einfahrt zwischen den Figuren
SB, SW, SG = 52, 64, 8                       # Steinhöhe, Steinbreite, Fuge
ABSACKEN = {2: (16, -5), 3: (24, 4), 4: (12, -3), 7: (20, 6)}   # Stein-Nr.: (Absenkung px, Drehung °)


def einfahrt(cue, bis=None):
    """Bodenband unter der Oberfläche: Sandbett der Einfahrt."""
    return [bis_(karte(EX0, BODEN, EX1 - EX0, 110, cue, fill=SAND, rund=10, schatten=0, rand=5), bis)]


def steine(cue, uneben=False, bis=None):
    els = []
    n = (EX1 - EX0 - 16) // (SW + SG)
    for i in range(n):
        x = EX0 + 12 + i * (SW + SG)
        dy, rot = ABSACKEN.get(i, (0, 0)) if uneben else (0, 0)
        e = karte(x, BODEN + 6 + dy, SW, SB, cue, fill=STEIN, rund=8, schatten=0, rand=4, anim="cut")
        if rot:
            sp = e.sprite.rotate(rot, expand=True, resample=Image.BICUBIC)
            e = El(sp, e.x - (sp.width - e.sprite.width) / 2, e.y - (sp.height - e.sprite.height) / 2, cue, "cut", 0.0,
                   name="karte:stein")
        els.append(bis_(e, bis))
    return els


# A Fall: die Einfahrt -----------------------------------------------------------------------------------------------------------
ZI_A, FU_A = 470, 1500
ZI_R1 = ("ZI_redet_r", ZI_A, BODEN, FH)
ZI_R2 = ("ZI_fordert_r", ZI_A, BODEN, FH)
FU_R1 = ("FU_redet", FU_A, BODEN, FH)
FU_R2 = ("FU_fordert", FU_A, BODEN, FH)
GELD = (beim("anz", "zahlt"), beim("anz", "an", ende=True))
folie([(NULL, "Fall · Die Einfahrt"), ("f1", "Fall · Das Angebot"), ("anz", "Fall · Anzahlung und Pflaster"),
       ("z2", "Fall · Der Streit"), ("frage", "Fall · Die Frage")], [
    hart(pl("Die Einfahrt vor dem Haus", 70, 40, NULL, fill=GELB, size=40)),
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    hart(ficon("tabler", "home", 190, BODEN - 4, 280, NULL, fuell=GELB)),
    *[hart(e) for e in einfahrt(NULL)],
    hart(pl("Einfahrt", (EX0 + EX1) // 2, 990, NULL, fill=WEISS, size=28, anker="m", bis="pfl")),
    # Pflaster: erst eben, dann abgesackt
    *[szene(e, "034hammer*", 0.8) if i == 0 else e for i, e in enumerate(steine("pfl", bis="senkt"))],
    *steine("senkt", uneben=True),
    ficon("tabler", "hammer", EX1 - 40, BODEN - 4, 90, "pfl", fuell=GELB, bis="senkt"),
    pl("gepflastert", (EX0 + EX1) // 2, 990, "pfl", fill=GRUEN, size=28, anker="m", bis="senkt"),
    pl("Steine sacken ab: uneben", (EX0 + EX1) // 2, 990, "senkt", fill=ROT, size=28, anker="m"),
    # Angebot und Geld (Mitte, zwischen den Figuren)
    ficon("tabler", "receipt-off", 800, 540, 110, beim("f1", "Ohne"), fuell=WEISS),
    pl("ohne Rechnung", 800, 555, beim("f1", "Ohne"), fill=WEISS, size=28, anker="m"),
    pl("5.000 € bar", 1120, 640, beim("f1", "fünftausend"), fill=GELB, size=30, anker="m", bis="anz"),
    szene(bewegt(ficon("tabler", "cash-banknote", 1120, 700, 120, GELD[0], fuell=GRUEN, anim="cut"), *GELD, -460),
          "034geld*", 1.0),
    pl("2.000 € angezahlt", 1120, 720, GELD[1], fill=GRUEN, size=28, anker="m"),
    pl("3.000 € offen", 1120, 560, beim("f2", "dreitausend"), fill=ROT, size=28, anker="m"),
    # Frau Ziegler (links, blickt nach rechts zu Herrn Fuchs)
    *[hart(e) for e in zi(ZI_A, BODEN, FH, [(NULL, "ruhig_r")], bis="z1")],
    *redet("ZI_redet_r", ZI_A, BODEN, FH, "z1", "anz"),
    *zi(ZI_A, BODEN, FH, [("anz", "froh_r"), ("senkt", "schreck_r"), (beim("senkt", "die"), "sorge_r")], erst="cut", bis="z2"),
    *redet("ZI_fordert_r", ZI_A, BODEN, FH, "z2", "f2"),
    *zi(ZI_A, BODEN, FH, [("f2", "ernst_r"), ("frage3", "denkt_r")], erst="cut"),
    hart(ns("Frau Ziegler", ZI_A, BODEN, NULL, ZI_F)),
    blase("sprech", 760, 210, "z1", 860, 250, inhalt=["Gut, dann machen wir es", "ohne Rechnung."], textsize=36,
          figur=ZI_R1, bis="anz"),
    blase("sprech", 820, 210, "z2", 880, 250, inhalt=["Erst bessern Sie nach,", "vorher zahle ich nichts mehr!"],
          textsize=36, figur=ZI_R2, bis="f2"),
    # Herr Fuchs (rechts, blickt nach links zu Frau Ziegler)
    *fu(FU_A, BODEN, FH, [(beim("fuchs", "Fuchs"), "ruhig")], bis="f1"),
    *redet("FU_redet", FU_A, BODEN, FH, "f1", "z1"),
    *fu(FU_A, BODEN, FH, [("z1", "froh"), ("senkt", "ertappt")], erst="cut", bis="f2"),
    *redet("FU_fordert", FU_A, BODEN, FH, "f2", "frage"),
    *fu(FU_A, BODEN, FH, [("frage", "ernst"), ("frage2", "denkt")], erst="cut"),
    ns("Herr Fuchs, Pflasterer", FU_A, BODEN, beim("fuchs", "Fuchs"), FU_F),
    blase("sprech", 900, 230, "f1", 1080, 250, inhalt=["Mit Rechnung wird es teurer.", "Ohne Rechnung, bar auf die Hand:",
                                                       "fünftausend Euro."], textsize=34, figur=FU_R1, bis="z1"),
    blase("sprech", 800, 190, "f2", 1100, 250, inhalt=["Ich will meine restlichen", "dreitausend Euro!"], textsize=36,
          figur=FU_R2, bis="frage"),
    # Die Frage
    pl("Bekommt Herr Fuchs sein Geld?", 960, 130, "frage", fill=PINK, size=36, anker="m"),
    pl("Muss er nachbessern?", 960, 225, "frage2", fill=PINK, size=36, anker="m"),
    pl("Anzahlung zurück?", 960, 320, "frage3", fill=PINK, size=36, anker="m"),
])

# B Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Ziegler lässt die Einfahrt vor ihrem Haus von dem selbstständigen Pflasterer Herrn Fuchs neu pflastern. "
    "Herr Fuchs bietet an: mit Rechnung teurer, ohne Rechnung bar 5.000 Euro. Frau Ziegler ist einverstanden. Herr Fuchs "
    "soll keine Rechnung stellen und keine Umsatzsteuer abführen; Frau Ziegler spart so die Umsatzsteuer.",
    "Frau Ziegler zahlt 2.000 Euro bar an, Herr Fuchs pflastert die Einfahrt. Wenige Wochen später sacken mehrere Steine "
    "ab, die Einfahrt ist uneben. Frau Ziegler verlangt Nachbesserung und will vorher nichts mehr zahlen. Herr Fuchs "
    "verlangt die restlichen 3.000 Euro.",
], "Werklohn, Nachbesserung, Anzahlung zurück: Wer hat welche Ansprüche?")

# C Vorfrage: Ist der Werkvertrag wirksam? ---------------------------------------------------------------------------------------
W134 = ["„Ein Rechtsgeschäft, das gegen ein gesetzliches Verbot verstößt,",
        "ist nichtig, wenn sich nicht aus dem Gesetz ein anderes ergibt.“"]
w134, w134_y = wortlaut(80, 175, 1100, W134, "§ 134 BGB", "p134", marken=[
    (0, "gegen ein gesetzliches Verbot verstößt", beim("p134", "gegen")), (1, "ist nichtig", beim("p134", "nichtig"))])
W1 = ["„Schwarzarbeit leistet, wer Dienst- oder Werkleistungen erbringt",
      "oder ausführen lässt und dabei",
      "…",
      "2. als Steuerpflichtiger seine sich auf Grund der Dienst- oder",
      "Werkleistungen ergebenden steuerlichen Pflichten nicht erfüllt, …“"]
w1, w1_y = wortlaut(80, w134_y + 22, 1100, W1, "§ 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG", "sag", marken=[
    (0, "erbringt", beim("nr2", "erbringt")), (1, "ausführen lässt", beim("nr2", "ausführen")),
    (3, "als Steuerpflichtiger", beim("nr2b", "Steuerpflichtiger")),
    (4, "steuerlichen Pflichten nicht erfüllt", beim("nr2b", "steuerlichen"))], size=30)
folie([("vor", "Vorfrage · Ist der Werkvertrag wirksam?"), ("p134", "Vorfrage · § 134 BGB: gesetzliches Verbot"),
       ("sag", "Vorfrage · § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG")], rechts_frei([
    *tafel("vor", "Vorfrage: Ist der Werkvertrag wirksam?", size=42),
    *w134,
    *w1,
    blk(110, w1_y + 18, 1040, 88, GELB, "verbot", [("Verbot, solche Verträge zu schließen", "ExtraBold", 34, INK)]),
    zit("BGHZ 198, 141 Rn. 13", 820, w1_y + 112, "verbot"),
    ficon("tabler", "ban", (X1 + X2) // 2, 330, 110, "p134", fuell=WEISS, bis="sag"),
    pl("Verbot?", (X1 + X2) // 2, 350, "p134", fill=WEISS, size=26, anker="m", bis="sag"),
    ficon("tabler", "receipt-off", (X1 + X2) // 2, 330, 110, "sag", fuell=WEISS),
    pl("ohne Rechnung", (X1 + X2) // 2, 350, "sag", fill=WEISS, size=26, anker="m"),
    *zi(X1, FB, FR, [("vor", "denkt"), ("verbot", "sorge")]),
    ns("Frau Ziegler", X1, FB, "vor", ZI_F),
    *fu(X2, FB, FR, [("vor", "ruhig"), ("nr2b", "ertappt")], d=0.2),
    ns("Herr Fuchs", X2, FB, "vor", FU_F, d=0.2),
]))

# D Der Verstoß im Fall ------------------------------------------------------------------------------------------------------------
folie([("fu", "Nichtigkeit · Verstoß von Herrn Fuchs"), ("kennt", "Nichtigkeit · Kenntnis und bewusstes Ausnutzen"),
       ("nichtig", "Nichtigkeit · Ergebnis")], rechts_frei([
    *tafel("fu", "Verstoß gegen das Verbot?"),
    ok(140, 210, "fu", gr=20), z("Herr Fuchs: keine Rechnung, keine Umsatzsteuer", 185, 190, "fu", "Bold"),
    z("vorsätzlicher Verstoß", 225, 245, beim("fu", "vorsätzlich"), size=31),
    z("Frau Ziegler selbst Schwarzarbeit? kann offenbleiben", 185, 320, "zi", size=31),
    zit("BGHZ 198, 141 Rn. 22", 225, 370, "zi"),
    z("Nichtig jedenfalls, wenn der Besteller den Verstoß", 110, 440, "kennt", "Bold"),
    z("kennt und bewusst zum eigenen Vorteil ausnutzt", 150, 495, beim("kennt", "kennt"), "Bold"),
    zit("BGHZ 198, 141 Rn. 13, 23", 150, 550, beim("kennt", "kennt")),
    ok(140, 625, "spart", gr=20), z("Frau Ziegler spart die Umsatzsteuer", 185, 605, "spart", size=32),
    blk(110, 690, 1040, 140, ROT, "nichtig", [("Werkvertrag nichtig, und zwar insgesamt", "ExtraBold", 36, INK),
                                            ("§ 134 BGB i. V. m. § 1 Abs. 2 S. 1 Nr. 2 SchwarzArbG", "Regular", 30, INK)]),
    ficon("tabler", "receipt-off", X2, 300, 100, "fu", fuell=WEISS, bis="kennt"),
    ficon("tabler", "eye", X1, 300, 110, "kennt", fuell=WEISS, bis="spart"),
    pl("kennt den Verstoß", X1, 320, "kennt", fill=WEISS, size=26, anker="m", bis="spart"),
    ficon("tabler", "coins", X1, 300, 100, "spart", fuell=GELB),
    pl("spart die Steuer", X1, 320, "spart", fill=GELB, size=26, anker="m"),
    *zi(X1, FB, FR, [("fu", "ruhig"), ("kennt", "denkt"), ("spart", "sorge")]),
    ns("Frau Ziegler", X1, FB, "fu", ZI_F),
    *fu(X2, FB, FR, [("fu", "ertappt"), ("nichtig", "ernst")], d=0.2),
    ns("Herr Fuchs", X2, FB, "fu", FU_F, d=0.2),
]))

# E Gegenfall: einseitiger Verstoß ----------------------------------------------------------------------------------------------------
folie([("gegen", "Gegenfall · Frau Ziegler weiß von nichts"), ("gegen2", "Gegenfall · einseitiger Verstoß")], rechts_frei([
    *tafel("gegen", "Gegenfall"),
    z("Frau Ziegler weiß von nichts", 110, 190, beim("gegen", "nichts"), "Bold"),
    z("Herr Fuchs zahlt heimlich keine Steuern", 150, 245, beim("gegen", "heimlich"), size=32),
    ok(140, 360, "gegen2", gr=20), z("einseitiger Verstoß: Vertrag bleibt wirksam", 185, 340, "gegen2", "Bold"),
    zit("BGHZ 89, 369 (zur früheren Fassung); BGHZ 198, 141 Rn. 17", 185, 395, "gegen2"),
    ok(140, 480, "gegen3", gr=20), z("Mängelrechte bleiben, § 634 BGB", 185, 460, "gegen3", "Bold"),
    ficon("tabler", "eye-off", X1, 300, 110, beim("gegen", "nichts"), fuell=WEISS),
    pl("weiß von nichts", X1, 320, beim("gegen", "nichts"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "tool", X2, 300, 100, "gegen3", fuell=GRUEN),
    pl("Mängelrechte", X2, 320, "gegen3", fill=GRUEN, size=26, anker="m"),
    *zi(X1, FB, FR, [("gegen", "ruhig"), ("gegen3", "froh")]),
    ns("Frau Ziegler", X1, FB, "gegen", ZI_F),
    *fu(X2, FB, FR, [("gegen", "denkt")], d=0.2),
    ns("Herr Fuchs", X2, FB, "gegen", FU_F, d=0.2),
]))

# F1 Herr Fuchs: Werklohn, GoA, Wertersatz ----------------------------------------------------------------------------------------------
folie([("a", "A. Herr Fuchs gegen Frau Ziegler"), ("a1", "A. Herr Fuchs › I. Werklohn, § 631 Abs. 1 BGB"),
       ("a2", "A. Herr Fuchs › II. Geschäftsführung ohne Auftrag"), ("b", "A. Herr Fuchs › III. Wertersatz, §§ 812, 818 Abs. 2 BGB")],
      rechts_frei([
    *tafel("a", "A. Herr Fuchs gegen Frau Ziegler"),
    z("I. Werklohn, § 631 Abs. 1 BGB", 185, 190, "a1", "Bold"),
    nein(140, 265, beim("a1", "Ohne"), gr=20), z("kein wirksamer Vertrag", 185, 245, beim("a1", "Ohne"), size=32),
    z("II. Aufwendungsersatz, §§ 677, 683, 670 BGB", 185, 330, "a2", "Bold"),
    nein(140, 405, beim("a2", "Verbotene"), gr=20),
    z("verbotene Arbeit nicht für erforderlich halten", 185, 385, beim("a2", "Verbotene"), size=32),
    zit("BGHZ 201, 1 Rn. 14", 185, 435, beim("a2", "Verbotene")),
    z("III. Wertersatz, §§ 812 Abs. 1 S. 1 Alt. 1, 818 Abs. 2", 185, 510, "b", "Bold"),
    ok(140, 585, "b1", gr=20), z("Pflasterarbeiten durch Leistung erlangt,", 185, 565, "b1", size=32),
    z("ohne Rechtsgrund", 225, 615, beim("b1", "ohne"), size=32),
    ok(140, 700, "b2", gr=20), z("Herausgabe nicht möglich: Wertersatz", 185, 680, "b2", size=32),
    zit("BGHZ 201, 1 Rn. 16", 225, 730, "b2"),
    ficon("tabler", "file-invoice", X2, 300, 90, "a1", fuell=WEISS, bis="b"),
    pl("Werklohn?", X2, 320, "a1", fill=WEISS, size=26, anker="m", bis="b"),
    ficon("tabler", "scale", X2, 300, 110, "b", fuell=WEISS),
    pl("Wertersatz?", X2, 320, "b", fill=WEISS, size=26, anker="m"),
    *zi(X1, FB, FR, [("a", "ernst"), ("b1", "denkt")]),
    ns("Frau Ziegler", X1, FB, "a", ZI_F),
    *fu(X2, FB, FR, [("a", "ruhig"), (beim("a1", "Ohne"), "ertappt"), ("b2", "froh")], d=0.2),
    ns("Herr Fuchs", X2, FB, "a", FU_F, d=0.2),
]))

# F2 Herr Fuchs: Sperre des § 817 Satz 2 BGB ----------------------------------------------------------------------------------------------
W817 = ["„Die Rückforderung ist ausgeschlossen, wenn dem Leistenden",
        "gleichfalls ein solcher Verstoß zur Last fällt, …“"]
w817, w817_y = wortlaut(80, 175, 1100, W817, "§ 817 Satz 2 BGB", "p817", marken=[
    (0, "Die Rückforderung ist ausgeschlossen", beim("p817b", "Rückforderung")),
    (1, "gleichfalls ein solcher Verstoß", beim("p817b", "gleichfalls"))])
folie([("p817", "A. Herr Fuchs › III. Wertersatz › § 817 Satz 2 BGB"), ("werg", "A. Herr Fuchs › Ergebnis")], rechts_frei([
    *tafel("p817", "III. Wertersatz: Sperre des § 817 S. 2 BGB", size=42),
    *w817,
    ok(140, w817_y + 75, "p817c", gr=20), z("Herr Fuchs verstößt mit seiner Arbeit selbst", 185, w817_y + 55, "p817c", "Bold"),
    zit("BGHZ 201, 1 Rn. 19", 225, w817_y + 110, "p817c"),
    ok(140, w817_y + 190, "p817d", gr=20), z("Sperre gilt auch für § 812 BGB", 185, w817_y + 170, "p817d", "Bold"),
    zit("BGHZ 201, 1 Rn. 19, 30", 225, w817_y + 225, "p817d"),
    blk(110, w817_y + 290, 1040, 100, ROT, "werg", [("Ergebnis: kein Wertersatz", "ExtraBold", 38, INK)]),
    ficon("tabler", "lock", X2, 300, 90, "p817c", fuell=GELB),
    pl("gesperrt", X2, 320, "p817c", fill=GELB, size=26, anker="m"),
    *zi(X1, FB, FR, [("p817", "ernst")]),
    ns("Frau Ziegler", X1, FB, "p817", ZI_F),
    *fu(X2, FB, FR, [("p817", "denkt"), ("p817c", "ertappt"), ("werg", "muede")], d=0.2),
    ns("Herr Fuchs", X2, FB, "p817", FU_F, d=0.2),
]))

# G1 Frau Ziegler: Mängelrechte ----------------------------------------------------------------------------------------------------------
folie([("m", "B. Frau Ziegler gegen Herrn Fuchs"), ("m1", "B. Frau Ziegler › I. Mängelrechte, § 634 BGB")], rechts_frei([
    *tafel("m", "B. Frau Ziegler gegen Herrn Fuchs"),
    z("I. Mängelrechte, § 634 BGB", 185, 190, "m1", "Bold"),
    z("Nacherfüllung, Minderung, Schadensersatz", 225, 245, beim("m1", "Nacherfüllung"), size=32),
    z("setzen einen wirksamen Werkvertrag voraus", 225, 300, beim("m1", "setzen"), size=32),
    nein(140, 390, "m2", gr=20), z("kein wirksamer Vertrag", 185, 370, "m2", "Bold"),
    zit("BGHZ 198, 141 Rn. 27", 225, 425, "m2"),
    nein(140, 510, "m3", gr=20), z("Treu und Glauben, § 242 BGB:", 185, 490, "m3", "Bold"),
    z("allenfalls in ganz engen Grenzen", 225, 545, beim("m3", "allenfalls"), size=32),
    zit("BGHZ 198, 141 Rn. 30", 225, 595, beim("m3", "allenfalls")),
    ficon("tabler", "tool", FX, 300, 100, beim("m1", "Nacherfüllung"), fuell=GRUEN),
    pl("Nacherfüllung?", FX, 320, beim("m1", "Nacherfüllung"), fill=GRUEN, size=26, anker="m"),
    *zi(FX, FB, FR, [("m", "ruhig"), ("m2", "sorge"), ("m3", "muede")]),
    ns("Frau Ziegler", FX, FB, "m", ZI_F),
]))

# G2 Frau Ziegler: Rückzahlung der Anzahlung -----------------------------------------------------------------------------------------------
folie([("r", "B. Frau Ziegler › II. Rückzahlung, § 812 Abs. 1 S. 1 Alt. 1 BGB")], rechts_frei([
    *tafel("r", "B. Frau Ziegler: die Anzahlung"),
    z("II. Rückzahlung, § 812 Abs. 1 S. 1 Alt. 1 BGB", 185, 190, "r", "Bold"),
    ok(140, 265, "r1", gr=20), z("2.000 € ohne Rechtsgrund erlangt", 185, 245, "r1", size=32),
    z("Zahlung ohne Rechnung diente dem", 185, 330, "r2", size=32),
    z("verbotenen Geschäft", 185, 380, beim("r2", "verbotenen"), size=32),
    nein(140, 470, "r3", gr=20), z("§ 817 Satz 2 BGB sperrt die Rückforderung", 185, 450, "r3", "Bold"),
    zit("BGHZ 206, 69 Rn. 13–17", 225, 505, "r3"),
    ficon("tabler", "cash-banknote", X2, 300, 110, "r1", fuell=GRUEN),
    pl("2.000 €", X2, 320, "r1", fill=GRUEN, size=26, anker="m"),
    ficon("tabler", "lock", X1, 300, 90, "r3", fuell=GELB),
    pl("gesperrt", X1, 320, "r3", fill=GELB, size=26, anker="m"),
    *zi(X1, FB, FR, [("r", "denkt"), ("r3", "sorge")]),
    ns("Frau Ziegler", X1, FB, "r", ZI_F),
    *fu(X2, FB, FR, [("r", "ruhig")], d=0.2),
    ns("Herr Fuchs", X2, FB, "r", FU_F, d=0.2),
]))

# H Ergebnis -------------------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · kein Ausgleich")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    nein(140, 210, "e1", gr=20), z("Herr Fuchs: weder Werklohn noch Wertersatz", 185, 190, "e1", "Bold"),
    nein(140, 300, "e2", gr=20), z("Frau Ziegler: keine Mängelrechte,", 185, 280, "e2", "Bold"),
    z("keine Rückzahlung der Anzahlung", 185, 335, beim("e2", "bekommt"), "Bold"),
    z("kein Ausgleich zwischen beiden", 185, 425, "e3", size=32),
    zit("BGHZ 201, 1 Rn. 27; BGHZ 206, 69 Rn. 17", 185, 475, "e3"),
    blk(110, 560, 1040, 140, GELB, "e4", [("Wer bewusst gegen das Verbot verstößt,", "ExtraBold", 34, INK),
                                        ("soll schutzlos bleiben.", "ExtraBold", 34, INK)]),
    *zi(X1, FB, FR, [("erg", "ernst"), ("e2", "muede")]),
    ns("Frau Ziegler", X1, FB, "erg", ZI_F),
    *fu(X2, FB, FR, [("erg", "ernst"), ("e1", "muede")], d=0.2),
    ns("Herr Fuchs", X2, FB, "erg", FU_F, d=0.2),
]))

# I Rechtsprechungslinie -------------------------------------------------------------------------------------------------------------------
LY = [190, 290, 390, 510, 610]
folie([("linie", "Rechtsprechungslinie · BGH, VII. Zivilsenat")], rechts_frei([
    *tafel("linie", "Die Linie des Bundesgerichtshofs"),
    ok(140, LY[0] + 20, "l90", gr=20), z("1990 · BGHZ 111, 308: Wertersatz nach Treu und Glauben", 185, LY[0], "l90", size=32),
    nein(140, LY[1] + 20, "l13", gr=20), z("2013 · BGHZ 198, 141: keine Mängelrechte", 185, LY[1], "l13", size=32),
    nein(140, LY[2] + 20, "l14", gr=20), z("2014 · BGHZ 201, 1: kein Wertersatz mehr", 185, LY[2], "l14", size=32),
    z("Abschreckung ausgeblieben (Rn. 25)", 225, LY[2] + 50, beim("l14", "weil"), size=28, farbe=TEXT),
    nein(140, LY[3] + 20, "l15", gr=20), z("2015 · BGHZ 206, 69: keine Rückzahlung", 185, LY[3], "l15", size=32),
    z("2017 · BGHZ 214, 228: nichtig auch bei", 185, LY[4], "l17", size=32),
    z("nachträglicher Ohne-Rechnung-Abrede", 225, LY[4] + 50, beim("l17", "nachträglich"), size=32),
    zit("BGH, Az.: VII ZR 336/89 · VII ZR 6/13 · VII ZR 241/13 · VII ZR 216/14 · VII ZR 197/16", 110, 790, beim("l17", "nachträglich"), size=22),
    ficon("tabler", "gavel", FX, 560, 220, "linie", fuell=GELB),
    pl("1990", FX, 600, "l90", fill=WEISS, size=40, anker="m", bis="l13"),
    pl("2013", FX, 600, "l13", fill=WEISS, size=40, anker="m", bis="l14"),
    pl("2014", FX, 600, "l14", fill=WEISS, size=40, anker="m", bis="l15"),
    pl("2015", FX, 600, "l15", fill=WEISS, size=40, anker="m", bis="l17"),
    pl("2017", FX, 600, "l17", fill=WEISS, size=40, anker="m"),
]))

# J Streitstand: nachträgliche Abrede ----------------------------------------------------------------------------------------------------------
folie([("st", "Streitstand · nachträgliche Ohne-Rechnung-Abrede")], rechts_frei([
    *tafel("st", "Nachträgliche Abrede: was ist nichtig? (str.)", size=40),
    z("a. A. (Teil der Literatur):", 110, 190, "st", "Bold"),
    z("nur die Änderung nichtig,", 150, 245, beim("st", "nur"), size=32),
    z("der ursprüngliche Vertrag gilt weiter", 150, 295, beim("st", "ursprüngliche"), size=32),
    zit("z. B. Lorenz, NJW 2013, 3132, 3134; Nachweise in BGHZ 214, 228 Rn. 19", 150, 350, beim("st", "nur")),
    z("BGH: Erst die Verbindung mit der Werkleistung", 110, 440, "st2", "Bold"),
    z("macht die Abrede zur Schwarzarbeit", 150, 495, beim("st2", "macht"), size=32),
    blk(110, 580, 1040, 100, ROT, beim("st2", "also"), [("ganzer Vertrag nichtig", "ExtraBold", 38, INK)]),
    zit("BGHZ 214, 228 Rn. 19 (= VII ZR 197/16)", 150, 700, beim("st2", "also")),
    ficon("tabler", "scale", FX, 470, 220, "st", fuell=WEISS),
    ficon("tabler", "book", FX - 130, 800, 110, "st", fuell=BLAU),
    pl("a. A.", FX - 130, 820, "st", fill=BLAU, size=26, anker="m"),
    ficon("tabler", "book", FX + 130, 800, 110, "st2", fuell=GRUEN),
    pl("BGH", FX + 130, 820, "st2", fill=GRUEN, size=26, anker="m"),
]))

# K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Nichtigkeit genau prüfen"), ("tipp2", "Klausurtipp · Teilbeträge ohne Rechnung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nichtigkeit genau prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("Wer verstößt? Weiß die andere Seite davon?", 200, 260, beim("tipp", "Wer"), size=34),
    z("Teilbeträge ohne Rechnung:", 110, 380, "tipp2", "Bold", 36),
    z("trotzdem ganzer Vertrag nichtig,", 150, 440, beim("tipp2", "ist"), size=34),
    z("wenn dem Teil mit Rechnung keine bestimmten", 150, 495, "tipp3", size=34),
    z("Einzelleistungen zugeordnet sind", 150, 550, beim("tipp3", "Einzelleistungen"), size=34),
    zit("BGHZ 201, 1 Rn. 13; BGHZ 214, 228 Rn. 24", 150, 610, beim("tipp3", "Einzelleistungen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# L Klausurschema --------------------------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Schwarzarbeit"), 110, 90, "sch", 46),
    z("A. Ansprüche des Unternehmers", K1, 185, "s1", "Bold", 36, rechts=1820),
    z("I. Werklohn, § 631 Abs. 1 BGB", K2, 240, "s2", "Bold", 33, rechts=1820),
    z("Vertrag nichtig? § 134 BGB i. V. m. § 1 Abs. 2 S. 1 Nr. 2 SchwarzArbG", K3, 290, "s3", size=31, rechts=1820),
    z("1. Verbot greift (Ohne-Rechnung-Abrede)", K3 + 40, 335, beim("s3", "erstens"), size=31, rechts=1820),
    z("2. Unternehmer verstößt vorsätzlich", K3 + 40, 380, "s4", size=31, rechts=1820),
    z("3. Besteller kennt den Verstoß und nutzt ihn bewusst aus", K3 + 40, 425, "s5", size=31, rechts=1820),
    z("II. GoA, §§ 677, 683, 670 BGB: Aufwendungen nicht erforderlich", K2, 480, "s6", "Bold", 33, rechts=1820),
    z("III. Wertersatz, §§ 812 Abs. 1 S. 1 Alt. 1, 818 Abs. 2 BGB: gesperrt, § 817 S. 2 BGB", K2, 535, "s7", "Bold", 33,
      rechts=1820),
    z("B. Ansprüche des Bestellers", K1, 625, "s8", "Bold", 36, rechts=1820),
    z("I. Mängelrechte, § 634 BGB: kein wirksamer Vertrag", K2, 680, "s9", "Bold", 33, rechts=1820),
    z("II. Rückzahlung, § 812 Abs. 1 S. 1 Alt. 1 BGB: gesperrt, § 817 S. 2 BGB", K2, 735, "s10", "Bold", 33, rechts=1820),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Bei bewusster Schwarzarbeit", 0)], [("ist der Werkvertrag ", 0), ("nichtig.", "a")]], 750, 320, 52,
                "merke", {"a": beim("merke", "nichtig")}),
    *markertext([[("Und § 817 Satz 2 BGB sperrt", 0)], [("das Bereicherungsrecht ", 0), ("für beide Seiten.", "b")]],
                750, 560, 46, "mk2", {"b": beim("mk2", "für")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
