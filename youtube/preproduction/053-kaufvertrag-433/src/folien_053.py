"""Folge 053 · § 433 BGB: Die Pflichten aus dem Kaufvertrag – Prüfungsschema – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „gebrauchtes Fahrrad“): Inga kauft am Freitag im Vorgarten von Herrn Lüders (privat) dessen altes
Trekkingrad für 250 €, Abholung am Samstag. Am Samstag will sie das Rad mitnehmen und erst am Montag überweisen; Herr
Lüders verweigert die Herausgabe. Inga holt das Geld am Automaten, beide tauschen, Inga fährt davon.
Szenen laut ../SZENENPLAN.md: A1 Freitag (Anzeige, Vorgarten, Einigung), A2 Samstag (Streit, Tausch, Frage), B Sachverhalt,
C Wortlaut § 433 I, D Pflichten des Verkäufers, E Wortlaut § 433 II, F Trennungsprinzip, G drei Schritte, H I. entstanden,
I II. nicht erloschen (Wortlaut § 362 I), J III. durchsetzbar (Wortlaut § 320 I 1), K Zug um Zug, § 322, Abnahme,
L Erfüllung beim Tausch, M Ausblick Gefahrübergang, N Ausblick Verbrauchsgüterkauf, O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Geldscheine beim Bezahlen, Freilauf beim Davonfahren; Freesound CC0, Herkunft in
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns als eigene Kopie aus Folge 046 (gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_053/"

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
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_053/" in n:
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
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
IN_F, LU_F = GRUEN, BLAU                    # Farben der Namensschilder
RAD = PINK                                  # Ingas Rad (wie das Rad der Pose sitting/bike)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def rad(cx, unten, breite, cue, **k):
    """Ingas Rad: Phosphor „bicycle“ (MIT), beide Räder rosa."""
    return ficon("ph", "bicycle", cx, unten, breite, cue, fuell=RAD, nebenfarbe=RAD, **k)


def inga(cx, unten, hoehe, folge, **k):
    return fig("IN", cx, unten, hoehe, folge, **k)


def lue(cx, unten, hoehe, folge, **k):
    return fig("LU", cx, unten, hoehe, folge, **k)


def paar(c0, lue_folge, inga_folge):
    """Tafelszene: Herr Lüders links (X1), Inga rechts (X2), beide blicken zur Tafel."""
    return [*lue(X1, FB, FR, lue_folge), ns("Herr Lüders", X1, FB, c0, LU_F),
            *inga(X2, FB, FR, inga_folge, d=0.2), ns("Inga", X2, FB, c0, IN_F, d=0.2)]


# A1 Fall: Freitag – Anzeige, Vorgarten, Einigung ---------------------------------------------------------------------
LUX, INX = 560, 1500
HAUS = (230, BODEN - 2, 280)
PFLANZE = (400, BODEN - 2, 90)
RADX = 1000
BESUCH = "besuch"
folie([(NULL, "Fall · Die Anzeige"), (BESUCH, "Fall · Freitag im Vorgarten")], [
    hart(pl("Inga sucht ein gebrauchtes Fahrrad", 70, 40, NULL, fill=GRUEN, size=44, bis=BESUCH)),
    boden(NULL, True),
    *inga(INX, BODEN, FH, [(NULL, "ueberlegt"), ("anzeige", "froh")], bis="i1", erst="cut"),
    *redet("IN_redet", INX, BODEN, FH, "i1", "l1"),
    *inga(INX, BODEN, FH, [("l1", "froh")], bis="sams", erst="cut"),
    hart(ns("Inga, Käuferin", INX, BODEN, NULL, IN_F)),
    hart(ficon("tabler", "search", 900, 560, 200, NULL, fuell=WEISS, bis=beim("anzeige", "Internet"))),
    hart(rad(870, BODEN - 2, 280, NULL, bis=beim("anzeige", "Internet"))),
    hart(pl("gebraucht", 870, 600, NULL, fill=WEISS, size=30, anker="m", bis=beim("anzeige", "Internet"))),
    # die Anzeige im Internet
    bis_(karte(560, 200, 640, 420, beim("anzeige", "Internet"), fill=(226, 236, 252, 255)), BESUCH),
    ficon("tabler", "device-mobile", 640, 300, 60, beim("anzeige", "Internet"), fuell=WEISS, bis=BESUCH),
    pl("Anzeige im Internet", 700, 230, beim("anzeige", "Internet"), fill=WEISS, size=30, bis=BESUCH),
    rad(880, 540, 280, beim("anzeige", "Trekkingrad"), bis=BESUCH),
    pl("altes Trekkingrad", 880, 555, beim("anzeige", "Trekkingrad"), fill=WEISS, size=30, anker="m", bis=BESUCH),
    pl("250 €", 1110, 400, beim("anzeige", "zweihundertfünfzig"), fill=GELB, size=34, anker="m", bis=BESUCH),
    pl("Herr Lüders", 880, 295, beim("anzeige", "Herr"), fill=BLAU, size=30, anker="m", bis=BESUCH),
    # Freitag im Vorgarten
    pl("Freitag, im Vorgarten von Herrn Lüders", 70, 40, BESUCH, fill=GELB, size=44),
    ficon("tabler", "home", *HAUS, BESUCH, fuell=GELB),
    ficon("tabler", "plant", *PFLANZE, BESUCH, fuell=GRUEN),
    rad(RADX, BODEN - 2, 300, BESUCH),
    *lue(LUX, BODEN, FH, [(BESUCH, "ruhig_r")], bis="l1"),
    *redet("LU_redet_r", LUX, BODEN, FH, "l1", "sams"),
    ns("Herr Lüders, Verkäufer", LUX, BODEN, BESUCH, LU_F),
    blase("sprech", 660, 230, "i1", 1180, 230, inhalt=["Das Rad nehme ich,", "für zweihundertfünfzig Euro."], textsize=36,
          figur=("IN_redet", INX, BODEN, FH), bis="l1"),
    blase("sprech", 600, 230, "l1", 900, 230, inhalt=["Abgemacht!", "Holen Sie es morgen ab."], textsize=38,
          figur=("LU_redet_r", LUX, BODEN, FH), bis="sams"),
])

# A2 Fall: Samstag – Streit, Automat, Tausch, Frage -------------------------------------------------------------------
GELD0, GELD1 = (INX - 150, 700), (LUX + 170, 700)          # Geldscheine: Ingas Hand → Herr Lüders
KEY0, KEY1 = (LUX + 170, 620), (INX - 150, 620)            # Schlüssel: Herr Lüders → Inga
RAD1 = 1220                                                # Rad steht nach der Übergabe bei Inga
TZ = "tausch"
FAHR0, FAHR1 = 1300, 1600                                   # Inga fährt davon (nach rechts)
folie([("sams", "Fall · Samstag: das Rad gleich mitnehmen?"), (TZ, "Fall · Der Tausch"), ("frage", "Fall · Die Frage")], [
    pl("Samstag", 70, 40, "sams", fill=GELB, size=44),
    boden("sams"),
    ficon("tabler", "home", *HAUS, "sams", fuell=GELB),
    ficon("tabler", "plant", *PFLANZE, "sams", fuell=GRUEN),
    *lue(LUX, BODEN, FH, [("sams", "ruhig_r"), ("i2", "denkt_r")], bis="l2"),
    *redet("LU_streng_r", LUX, BODEN, FH, "l2", "automat"),
    *lue(LUX, BODEN, FH, [("automat", "ernst_r"), (TZ, "froh_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Herr Lüders", LUX, BODEN, "sams", LU_F),
    bis_(bewegt(rad(RAD1, BODEN - 2, 300, "sams"), beim(TZ, "Rad"), beim(TZ, "Rad", ende=True), RADX - RAD1, 0), "weg"),
    *inga(INX, BODEN, FH, [("sams", "froh")], bis="i2", erst="fade"),
    *redet("IN_redet", INX, BODEN, FH, "i2", "l2"),
    *inga(INX, BODEN, FH, [("l2", "sorge"), ("automat", "ruhig"), (TZ, "froh")], bis="weg", erst="cut"),
    ns("Inga", INX, BODEN, "sams", IN_F, bis="weg"),
    ficon("tabler", "device-mobile", INX - 135, 700, 56, "i2", fuell=WEISS, bis="l2"),
    blase("sprech", 600, 230, "i2", 1180, 230, inhalt=["Das Geld überweise ich", "Ihnen am Montag."], textsize=38,
          figur=("IN_redet", INX, BODEN, FH), bis="l2"),
    blase("sprech", 600, 230, "l2", 900, 230, inhalt=["Nein. Erst das Geld,", "dann das Rad."], textsize=40,
          figur=("LU_streng_r", LUX, BODEN, FH), bis="automat"),
    # Inga holt das Geld am Automaten an der Ecke
    ficon("tabler", "building-bank", 1760, 330, 150, "automat", fuell=WEISS, bis=TZ),
    pl("Automat an der Ecke", 1640, 350, beim("automat", "Automaten"), fill=WEISS, size=30, anker="m", bis=TZ),
    szene(bewegt(ficon("tabler", "cash-banknote", *GELD1, 110, beim("automat", "Geld"), fuell=GRUEN),
                 beim(TZ, "zahlt"), beim(TZ, "zahlt", ende=True), GELD0[0] - GELD1[0], 0), "053geld*", 0.6),
    pl("250 €", GELD1[0], 560, beim(TZ, "zahlt", ende=True), fill=GELB, size=30, anker="m"),
    bis_(bewegt(ficon("tabler", "key", *KEY1, 70, beim(TZ, "Schlüssel"), fuell=GELB),
                beim(TZ, "Schlüssel"), beim(TZ, "Schlüssel", ende=True), KEY0[0] - KEY1[0], 0), "weg"),
    # Inga fährt davon
    szene(bewegt(peep_voll("IN_rad_r", FAHR1, BODEN, 400, "weg", anim="cut"), "weg", beim("weg", "davon", ende=True),
                 FAHR0 - FAHR1, 0), "053freilauf*", 0.5),
    bewegt(ns("Inga", FAHR1, BODEN, "weg", IN_F, anim="cut"), "weg", beim("weg", "davon", ende=True), FAHR0 - FAHR1, 0),
    pl("Was durfte Inga von Herrn Lüders verlangen?", 1180, 140, "frage", fill=PINK, size=34, anker="m"),
    pl("Durfte er das Rad zurückhalten?", 1180, 230, "frage2", fill=PINK, size=34, anker="m"),
    pl("Was schuldet Inga ihm?", 1180, 320, beim("frage2", "Und"), fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Lüders bietet sein altes Trekkingrad privat im Internet für 250 Euro an. Am Freitag sieht Inga es sich bei ihm "
    "an und sagt: „Das Rad nehme ich, für 250 Euro.“ Herr Lüders antwortet: „Abgemacht! Holen Sie es morgen ab.“",
    "Am Samstag will Inga das Rad gleich mitnehmen und das Geld erst am Montag überweisen. Herr Lüders lehnt ab: „Erst "
    "das Geld, dann das Rad.“ Inga holt das Geld am Automaten an der Ecke und zahlt bar. Herr Lüders gibt ihr das Rad und "
    "den Schlüssel für das Schloss, Inga fährt damit nach Hause.",
], "Was durfte Inga verlangen, durfte Herr Lüders das Rad zurückhalten?")

# C Anspruchsgrundlage, Wortlaut § 433 Abs. 1 BGB ------------------------------------------------------------------------
W433_1 = ["„Durch den Kaufvertrag wird der Verkäufer einer Sache verpflichtet,",
          "dem Käufer die Sache zu übergeben und das Eigentum an der Sache",
          "zu verschaffen. Der Verkäufer hat dem Käufer die Sache frei von",
          "Sach- und Rechtsmängeln zu verschaffen.“"]
w1, w1_y = wortlaut(80, 290, 1100, W433_1, "§ 433 Abs. 1 BGB", "ansp", marken=[
    (1, "zu übergeben", beim("w1", "übergeben")),
    (1, "das Eigentum an der Sache", beim("w1", "Eigentum")),
    (2, "frei von", beim("w1b", "frei")), (3, "Sach- und Rechtsmängeln", beim("w1b", "frei"))], size=31)
folie([("ansp", "Inga gegen Herrn Lüders · § 433 Abs. 1 BGB"), ("w1", "§ 433 Abs. 1 BGB › Wortlaut")], rechts_frei([
    *tafel("ansp", "Inga gegen Herrn Lüders: das Rad"),
    z("Anspruchsgrundlage: § 433 Abs. 1 BGB", 110, 190, beim("ansp", "Anspruchsgrundlage"), "Bold", 36),
    *w1,
    z("Satz 1: übergeben und Eigentum verschaffen", 110, w1_y + 40, beim("w1", "übergeben"), size=32),
    z("Satz 2: frei von Sach- und Rechtsmängeln", 110, w1_y + 90, "w1b", size=32),
    rad(X1 + 150, 380, 220, "ansp", bis="w1b"),
    pl("das Rad", X1 + 150, 160, "ansp", fill=WEISS, size=28, anker="m", bis="w1b"),
    ficon("tabler", "shield-check", X1 + 150, 380, 120, "w1b", fuell=GRUEN),
    pl("ohne Mängel", X1 + 150, 160, "w1b", fill=GRUEN, size=28, anker="m"),
    *paar("ansp", [("ansp", "ruhig"), ("w1b", "ernst")], [("ansp", "ruhig"), ("w1", "denkt")]),
]))

# D Pflichten des Verkäufers ---------------------------------------------------------------------------------------------
folie([("vk", "§ 433 Abs. 1 BGB › Pflichten des Verkäufers"), ("vk3", "§ 433 Abs. 1 Satz 2 BGB › frei von Mängeln")],
      rechts_frei([
    *tafel("vk", "Der Verkäufer schuldet dreierlei"),
    z("1. Übergabe: Besitz,", 110, 200, "vk1", "Bold", 36),
    z("die tatsächliche Gewalt über das Rad", 150, 255, beim("vk1", "tatsächliche"), size=34),
    z("2. Übereignung: Inga wird Eigentümerin", 110, 340, "vk2", "Bold", 36),
    z("3. ein Rad ohne Mängel:", 110, 425, "vk3", "Bold", 36),
    z("kein Sachmangel, etwa kaputte Bremse,", 150, 485, "sm", size=34),
    z("§ 434 BGB", 150, 535, beim("sm", "Paragraf"), size=34),
    z("kein Rechtsmangel, § 435 BGB:", 150, 610, "rm", size=34),
    z("kein Dritter kann Rechte gegen Inga geltend machen", 150, 660, beim("rm", "Dritter"), size=32),
    bewegt(rad(X2 - 60, 380, 220, "vk", bis="vk2"), beim("vk1", "Besitz"), beim("vk1", "Gewalt", ende=True), X1 - X2 + 60, 0),
    ficon("tabler", "certificate", X2 - 60, 380, 130, "vk2", fuell=GELB, bis="vk3"),
    pl("Eigentümerin", X2 - 60, 160, "vk2", fill=GELB, size=28, anker="m", bis="vk3"),
    ficon("tabler", "tool", X2 - 60, 380, 120, "sm", fuell=WEISS, bis="rm"),
    pl("Bremse kaputt?", X2 - 60, 160, beim("sm", "kaputte"), fill=ROT, size=28, anker="m", bis="rm"),
    ficon("tabler", "users", X2 - 60, 380, 130, "rm", fuell=LILA),
    pl("Rechte Dritter?", X2 - 60, 160, beim("rm", "Dritter"), fill=LILA, size=28, anker="m"),
    *paar("vk", [("vk", "ruhig")], [("vk", "ruhig"), ("vk2", "froh"), ("sm", "sorge"), ("rm", "denkt")]),
]))

# E Wortlaut § 433 Abs. 2 BGB: Pflichten des Käufers --------------------------------------------------------------------
W433_2 = ["„Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten",
          "Kaufpreis zu zahlen und die gekaufte Sache abzunehmen.“"]
w2, w2_y = wortlaut(80, 190, 1100, W433_2, "§ 433 Abs. 2 BGB", "w2", marken=[
    (1, "Kaufpreis zu zahlen", beim("w2", "Kaufpreis")), (1, "die gekaufte Sache abzunehmen", beim("w2", "gekaufte"))],
    size=32)
folie([("w2", "§ 433 Abs. 2 BGB › Pflichten des Käufers")], rechts_frei([
    *tafel("w2", "Die Käuferin schuldet"),
    *w2,
    z("1. Kaufpreis: 250 €", 110, w2_y + 50, "kp", "Bold", 38),
    z("2. Abnahme: hier das Rad abholen", 110, w2_y + 130, "ab", "Bold", 38),
    ficon("tabler", "cash-banknote", X2 - 60, 380, 140, "kp", fuell=GRUEN),
    pl("250 €", X2 - 60, 160, "kp", fill=GELB, size=28, anker="m"),
    rad(X1 + 60, 380, 200, "ab"),
    pl("abholen", X1 + 60, 160, beim("ab", "abholen"), fill=WEISS, size=28, anker="m"),
    *paar("w2", [("w2", "ruhig"), ("kp", "froh")], [("w2", "denkt"), ("ab", "ruhig")]),
]))

# F Trennungsprinzip ------------------------------------------------------------------------------------------------------
folie([("trenn", "Trennungsprinzip · Verpflichtung und Übereignung")], rechts_frei([
    *tafel("trenn", "Wichtig: Der Kaufvertrag verpflichtet nur"),
    blk(110, 200, 500, 200, GELB, "trenn", [("Kaufvertrag", "ExtraBold", 40, INK), ("§ 433 BGB", "Bold", 32, INK),
                                            ("verpflichtet", "Regular", 32, INK)]),
    blk(650, 200, 500, 200, GRUEN, "p929", [("Übereignung", "ExtraBold", 40, INK), ("§ 929 Satz 1 BGB", "Bold", 32, INK),
                                            ("Einigung + Übergabe", "Regular", 32, INK)]),
    z("Erst die Übereignung macht Inga zur Eigentümerin.", 110, 450, beim("p929", "Eigentümerin"), size=34),
    blk(110, 540, 1040, 100, LILA, "tp", [("Trennungsprinzip", "ExtraBold", 42, INK)]),
    pl("Mehr dazu: Folge zum Abstraktionsprinzip", 110, 700, "f005", fill=WEISS, size=30),
    ficon("tabler", "file-certificate", X1, 380, 120, "trenn", fuell=GELB),
    ficon("tabler", "certificate", X2, 380, 120, "p929", fuell=GRUEN),
    *paar("trenn", [("trenn", "denkt"), ("tp", "ruhig")], [("trenn", "ueberlegt"), ("p929", "froh")]),
]))

# G Drei Schritte ---------------------------------------------------------------------------------------------------------
folie([("drei", "Aufbau · entstanden, nicht erloschen, durchsetzbar")], rechts_frei([
    *tafel("drei", "Jeden Anspruch in drei Schritten"),
    blk(110, 210, 1040, 140, GRUEN, "s1", [("I. entstanden", "ExtraBold", 46, INK)]),
    blk(110, 390, 1040, 140, GELB, "s2", [("II. nicht erloschen", "ExtraBold", 46, INK)]),
    blk(110, 570, 1040, 140, BLAU, "s3", [("III. durchsetzbar", "ExtraBold", 46, INK)]),
    ficon("tabler", "list-check", FX, 380, 130, "drei", fuell=WEISS),
    *paar("drei", [("drei", "ruhig")], [("drei", "denkt"), ("s3", "ruhig")]),
]))

# H I. entstanden ---------------------------------------------------------------------------------------------------------
folie([("ent", "I. Anspruch entstanden › Kaufvertrag")], rechts_frei([
    *tafel("ent", "I. Ist der Anspruch entstanden?"),
    z("Einigung am Freitag:", 110, 200, "kv", "Bold", 36),
    pl("das Rad", 150, 270, beim("kv", "Rad"), fill=BLAU, size=32),
    pl("Preis: 250 €", 400, 270, beim("kv", "Preis"), fill=GELB, size=32),
    ok(140, 420, "kv_ok", gr=22), z("wirksamer Kaufvertrag", 185, 400, "kv_ok", "Bold", 36),
    blk(110, 500, 1040, 100, GRUEN, beim("kv_ok", "der"), [("Anspruch entstanden", "ExtraBold", 40, INK)]),
    ficon("tabler", "calendar-event", X1 + 150, 380, 110, "ent", fuell=GELB),
    pl("Freitag", X1 + 150, 160, "ent", fill=GELB, size=28, anker="m"),
    *paar("ent", [("ent", "ruhig"), ("kv", "froh")], [("ent", "ruhig"), ("kv", "froh")]),
]))

# I II. nicht erloschen, Wortlaut § 362 Abs. 1 BGB --------------------------------------------------------------------------
W362 = ["„Das Schuldverhältnis erlischt, wenn die geschuldete Leistung",
        "an den Gläubiger bewirkt wird.“"]
w362, w362_y = wortlaut(80, 190, 1100, W362, "§ 362 Abs. 1 BGB", "p362", marken=[
    (0, "erlischt", beim("p362", "erlischt")), (1, "bewirkt wird", beim("p362", "bewirkt"))], size=33)
folie([("erl", "II. nicht erloschen › Erfüllung, § 362 Abs. 1 BGB")], rechts_frei([
    *tafel("erl", "II. Nicht erloschen?"),
    *w362,
    nein(140, w362_y + 80, "sa", gr=22),
    z("Samstagmorgen: Inga hat das Rad noch nicht", 185, w362_y + 60, "sa", "Bold", 34),
    ok(140, w362_y + 170, "erl_ok", gr=22), z("Der Anspruch besteht.", 185, w362_y + 150, "erl_ok", "Bold", 36),
    rad(X1 + 60, 380, 200, "erl"),
    pl("bei Herrn Lüders", X1 + 60, 160, "sa", fill=WEISS, size=28, anker="m"),
    *paar("erl", [("erl", "ruhig")], [("erl", "denkt"), ("sa", "sorge")]),
]))

# J III. durchsetzbar, Wortlaut § 320 Abs. 1 Satz 1 BGB ---------------------------------------------------------------------
W320 = ["„Wer aus einem gegenseitigen Vertrag verpflichtet ist, kann die ihm",
        "obliegende Leistung bis zur Bewirkung der Gegenleistung verweigern,",
        "es sei denn, dass er vorzuleisten verpflichtet ist.“"]
w320, w320_y = wortlaut(80, 250, 1100, W320, "§ 320 Abs. 1 Satz 1 BGB", "p320", marken=[
    (0, "gegenseitigen Vertrag", beim("p320", "gegenseitiger")),
    (1, "bis zur Bewirkung der Gegenleistung verweigern", beim("p320", "bis")),
    (2, "es sei denn, dass er vorzuleisten verpflichtet ist", "vor")], size=30)
folie([("dur", "III. durchsetzbar? › der Streit vom Samstag"), ("p320", "III. durchsetzbar › Einrede, § 320 Abs. 1 BGB")],
      rechts_frei([
    *tafel("dur", "III. Durchsetzbar?"),
    pl("der Streit vom Samstag", 110, 175, beim("dur", "Streit"), fill=PINK, size=30),
    *w320,
    nein(140, w320_y + 80, "kein", gr=22),
    z("Zahlung erst am Montag: nicht vereinbart", 185, w320_y + 60, "kein", "Bold", 34),
    ok(140, w320_y + 160, beim("kein", "Herr"), gr=22),
    z("Herr Lüders durfte das Rad zurückhalten.", 185, w320_y + 140, beim("kein", "Herr"), "Bold", 34),
    rad(X1 + 150, 380, 220, "dur"),
    ficon("tabler", "lock", X1 + 150, 230, 60, beim("kein", "zurückhalten"), fuell=GELB),
    pl("Montag?", X2, 160, beim("kein", "Montag"), fill=WEISS, size=28, anker="m"),
    *paar("dur", [("dur", "ernst"), ("kein", "froh")], [("dur", "sorge"), ("p320", "denkt")]),
]))

# K Zug um Zug, § 322; Abnahme ---------------------------------------------------------------------------------------------
folie([("zug", "III. durchsetzbar › Zug um Zug"), ("p322", "III. durchsetzbar › im Prozess, § 322 Abs. 1 BGB"),
       ("abn", "III. durchsetzbar › Abnahme keine Gegenleistung")], rechts_frei([
    *tafel("zug", "Zug um Zug"),
    z("Auch Inga musste nicht vorleisten.", 110, 190, "zug", "Bold", 36),
    blk(110, 260, 1040, 100, GELB, beim("zug", "Beide"), [("Beide leisten Zug um Zug.", "ExtraBold", 40, INK)]),
    z("Klage von Inga: Beruft er sich auf sein Recht,", 110, 410, "p322", "Bold", 34),
    z("nur Verurteilung Zug um Zug, § 322 Abs. 1 BGB", 150, 465, beim("p322", "Paragraf"), size=34),
    nein(140, 590, "abn", gr=22),
    z("Abnahme: im Allgemeinen keine Gegenleistung", 185, 570, "abn", "Bold", 34),
    z("für die Lieferung", 185, 622, beim("abn", "Lieferung"), "Bold", 34),
    zit("BGH, Urt. v. 26.10.2016 – VIII ZR 211/15, Rn. 29", 185, 685, beim("abn", "Bundesgerichtshof")),
    ficon("tabler", "cash-banknote", X2 + 20, 300, 110, "zug", fuell=GRUEN),
    ficon("tabler", "arrows-exchange", FX + 10, 300, 90, beim("zug", "Beide"), fuell=WEISS),
    rad(X1, 300, 150, "zug"),
    ficon("tabler", "scale", FX, 420, 90, "p322", fuell=WEISS),
    *paar("zug", [("zug", "ruhig"), ("p322", "denkt")], [("zug", "froh"), ("abn", "ruhig")]),
]))

# L Erfüllung beim Tausch ---------------------------------------------------------------------------------------------------
LX1, IX2 = 1365, 1720
folie([("erf", "Erfüllung · der Tausch am Samstag"), ("erl2", "Erfüllung · beide Ansprüche erloschen, § 362 Abs. 1 BGB")],
      rechts_frei([
    *tafel("erf", "Der Tausch am Samstag"),
    ok(140, 220, beim("ue", "übergibt"), gr=22), z("Übergabe von Rad und Schlüssel", 185, 200, beim("ue", "übergibt"), "Bold", 34),
    ok(140, 290, beim("ue", "einig"), gr=22), z("Einigung: Eigentum soll übergehen", 185, 270, beim("ue", "einig"), "Bold", 34),
    ok(140, 360, "geld", gr=22), z("Übereignung der Geldscheine an ihn", 185, 340, "geld", "Bold", 34),
    blk(110, 430, 1040, 140, GRUEN, "erl2", [("Beide Ansprüche erfüllt:", "Bold", 36, INK),
                                             ("erloschen, § 362 Abs. 1 BGB", "ExtraBold", 38, INK)]),
    ok(140, 640, "abg", gr=22), z("Abnahme: Inga fährt nach Hause", 185, 620, "abg", "Bold", 34),
    bis_(bewegt(rad(IX2 - 40, 330, 200, "erf"), beim("ue", "übergibt"), beim("ue", "Rad", ende=True), LX1 - IX2 + 40, 0), "abg"),
    bis_(bewegt(ficon("tabler", "key", IX2 - 40, 400, 60, "erf", fuell=GELB), beim("ue", "übergibt"),
                beim("ue", "Schlüssel", ende=True), LX1 - IX2 + 40, 0), "abg"),
    bewegt(ficon("tabler", "cash-banknote", LX1 + 40, 400, 100, "erf", fuell=GRUEN), "geld", beim("geld", "Geldscheine", ende=True),
           IX2 - LX1 - 80, 0),
    *lue(LX1, FB, FR, [("erf", "ruhig"), ("geld", "froh")]), ns("Herr Lüders", LX1, FB, "erf", LU_F),
    *inga(IX2, FB, FR, [("erf", "ruhig"), ("ue", "froh")], bis="abg", d=0.2), ns("Inga", IX2, FB, "erf", IN_F, d=0.2, bis="abg"),
    peep_voll("IN_rad", 1680, FB, 360, "abg", anim="cut"), ns("Inga", 1680, FB, "abg", IN_F, anim="cut"),
]))

# M Ausblick: Gefahrübergang und Gewährleistung -----------------------------------------------------------------------------
W434 = ["„Die Sache ist frei von Sachmängeln, wenn sie bei Gefahrübergang …“"]
w434, w434_y = wortlaut(80, 260, 1100, W434, "§ 434 Abs. 1 BGB", "p434", marken=[(0, "bei Gefahrübergang", beim("p434", "Gefahrübergang"))],
                        size=32)
folie([("gew", "Ausblick · Gewährleistung ab Gefahrübergang"), ("p446", "Ausblick · Gefahrübergang, § 446 Satz 1 BGB"),
       ("p437", "Ausblick · Mängelrechte, § 437 BGB")], rechts_frei([
    *tafel("gew", "Ausblick: Ab wann Gewährleistung?"),
    pl("Ab wann greift das Gewährleistungsrecht?", 110, 175, "gew", fill=PINK, size=30),
    *w434,
    z("§ 446 Satz 1 BGB: Gefahr geht mit der Übergabe über", 110, w434_y + 50, "p446", "Bold", 33),
    z("Bremse schon am Samstag kaputt?", 110, w434_y + 140, "p437", "Bold", 34),
    z("grundsätzlich Mängelrechte, § 437 BGB", 150, w434_y + 195, beim("p437", "grundsätzlich"), size=34),
    zit("Mangel bei Gefahrübergang: BGH, Urt. v. 10.11.2021 – VIII ZR 187/20, Rn. 78", 110, w434_y + 270,
        beim("p437", "Mängelrechte")),
    ficon("tabler", "calendar-event", X1 + 150, 380, 110, "p446", fuell=GELB, bis="p437"),
    pl("Übergabe: Samstag", X1 + 150, 160, beim("p446", "Übergabe"), fill=GELB, size=28, anker="m", bis="p437"),
    ficon("tabler", "tool", X1 + 150, 380, 120, "p437", fuell=WEISS),
    pl("Bremse kaputt?", X1 + 150, 160, beim("p437", "Bremse"), fill=ROT, size=28, anker="m"),
    *paar("gew", [("gew", "ruhig"), ("p437", "sorge")], [("gew", "denkt"), ("p437", "sorge")]),
]))

# N Ausblick: Verbrauchsgüterkauf -------------------------------------------------------------------------------------------
folie([("vgk", "Ausblick · Verbrauchsgüterkauf, § 474 Abs. 1 BGB"), ("p475", "Ausblick · Sonderregeln, § 475 Abs. 1 BGB")],
      rechts_frei([
    *tafel("vgk", "Ausblick: Verbrauchsgüterkauf"),
    z("§ 474 Abs. 1 BGB: Verbraucher kauft", 110, 200, beim("vgk", "Verbraucher"), "Bold", 36),
    z("von einem Unternehmer", 150, 255, beim("vgk", "Unternehmer"), size=34),
    z("Sonderregeln, z. B. § 475 Abs. 1 BGB:", 110, 350, "p475", "Bold", 36),
    z("keine Leistungszeit bestimmt: Übergabe", 150, 405, beim("p475", "Ist"), size=34),
    z("spätestens 30 Tage nach Vertragsschluss", 150, 455, beim("p475", "spätestens"), size=34),
    nein(140, 570, "priv", gr=22), z("Herr Lüders verkauft privat: gilt hier nicht", 185, 550, "priv", "Bold", 34),
    ficon("tabler", "building-store", X1 + 150, 380, 140, beim("vgk", "Unternehmer"), fuell=BLAU, bis="priv"),
    pl("Unternehmer", X1 + 150, 160, beim("vgk", "Unternehmer"), fill=BLAU, size=28, anker="m", bis="priv"),
    ficon("tabler", "home", X1 + 150, 380, 130, "priv", fuell=GELB),
    pl("privat", X1 + 150, 160, "priv", fill=GELB, size=28, anker="m"),
    *paar("vgk", [("vgk", "ruhig"), ("priv", "froh")], [("vgk", "denkt"), ("priv", "ruhig")]),
]))

# O Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · was wohin gehört")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Achte darauf, was wohin gehört.", 200, 200, beim("tipp", "Achte"), "Bold", 36),
    z("Kaufvertrag: bei I. entstanden", 150, 300, beim("tipp2", "Kaufvertrag"), size=36),
    z("Übereignung: erst bei II. erloschen", 150, 360, beim("tipp2", "Übereignung"), size=36),
    nein(140, 480, "tipp3", gr=22), z("„Mit dem Kaufvertrag ist Inga", 185, 460, "tipp3", size=34),
    z("Eigentümerin geworden.“", 185, 512, "tipp3", size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# P Klausurschema ----------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k4", "Klausurschema › Kaufpreis, § 433 Abs. 2 BGB")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Inga gegen Herrn Lüders, § 433 Abs. 1 S. 1 BGB"), 110, 90, "sch", 44),
    z("I. Anspruch entstanden", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("wirksamer Kaufvertrag", K2, 255, "k1a", size=34, rechts=1820),
    z("II. nicht erloschen", K1, 335, "k2", "Bold", 38, rechts=1820),
    z("vor allem keine Erfüllung, § 362 Abs. 1 BGB: Übergabe und Übereignung", K2, 390, "k2a", size=34, rechts=1820),
    z("III. durchsetzbar", K1, 470, "k3", "Bold", 38, rechts=1820),
    z("bei Einrede aus § 320 Abs. 1 BGB: nur Zug um Zug", K2, 525, "k3a", size=34, rechts=1820),
    blk(K1, 630, 1600, 90, BLAU, "k4", [("Kaufpreis aus § 433 Abs. 2 BGB: genauso prüfen", "ExtraBold", 36, INK)]),
])

# Q Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Kaufvertrag ", 0), ("verpflichtet beide Seiten,", "a")], [("im Zweifel Zug um Zug.", "b")]],
                750, 320, 44, "merke", {"a": beim("merke", "verpflichtet"), "b": beim("merke", "Zug")}),
    *markertext([[("Das Eigentum geht erst mit der", 0)], [("Übereignung", "c"), (" über,", 0)],
                 [("nicht schon mit dem Kaufvertrag.", 0)]],
                750, 530, 42, "m2", {"c": beim("m2", "Übereignung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
