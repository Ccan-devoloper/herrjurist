"""Folge 027 · Besitz und Eigentum: Der Unterschied einfach erklärt (§§ 854 ff. BGB) – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Das geliehene Rad (WG/Keller), B Im Fahrradladen, C Der Dieb, D Sachverhalt,
E Eigentum (Wortlaut § 903 S. 1), F Besitz (Wortlaut § 854 I), G mittelbarer Besitz (Wortlaut § 868), H Eigen- und
Fremdbesitz (Wortlaut § 872), I Besitzdiener (Wortlaut § 855) und Erbenbesitz § 857, J verbotene Eigenmacht § 858,
K Selbsthilfe § 859 II, L Gegenfall: Anke holt ihr Rad, M § 861/§ 863, N Gegenprobe § 985/§ 986, O Ausblick §§ 929–931,
P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Schloss bricht auf,
Freilauf beim Wegschieben; Freesound CC0). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig wie in Folge 023 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_027/"


FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
HC = "fluent-emoji-high-contrast"
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return e.x + xs[i], e.y + int(h * 0.40) + ys[i]


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_027/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte (wie Folge 019): Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Eigene Hilfsfunktion (wie Folge 012/018): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause. redet_020() kürzt jedes Wortende auf
# das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende (siehe oben); Viseme aus der Schreibung geschätzt."""
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


def kaefig(x0, x1, y0, y1, cue, n=7):
    """Kellerabteil als Lattenverschlag: Rahmen (Karte) und senkrechte Latten (Bausteine karte/linienzug)."""
    rahmen = hart(karte(x0, y0, x1 - x0, y1 - y0, cue, fill=(240, 232, 216, 255), rund=6, schatten=0, rand=6))
    latten = [hart(linienzug([(x0 + (x1 - x0) * i / n, y0), (x0 + (x1 - x0) * i / n, y1)], cue, breite=6, farbe=INK))
              for i in range(1, n)]
    return [rahmen], latten


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2 = 150, 210
RAD = PINK                                  # Ankes Rad: Tabler „bike“, Rahmen rosa
JU_F, AN_F, KU_F, DI_F = BLAU, GRUEN, ORANGE, WEISS


def rad(cx, unten, breite, cue, **k):
    return ficon("tabler", "bike", cx, unten, breite, cue, fuell=RAD, **k)


# A Fall: das geliehene Rad (WG und Keller) -------------------------------------------------------------------------------
AN_A, JU_A, RAD_A = 300, 640, 950
KX0, KX1, KY0 = 1240, 1820, 500             # Kellerabteil
KM = (KX0 + KX1) // 2
r_k, l_k = kaefig(KX0, KX1, KY0, BODEN, NULL)
folie([(NULL, "Fall · Das geliehene Rad")], [
    hart(pl("In der WG", 70, 40, NULL, fill=GELB, size=48)),
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    *r_k,
    hart(pl("Kellerabteil", KM, 420, NULL, fill=WEISS, size=32, anker="m")),
    # das Rad: erst zwischen Anke und Jürgen, dann in den Keller
    hart(rad(RAD_A, BODEN, 300, NULL, bis=beim("j1", "schließe"))),
    bewegt(rad(KM, BODEN - 10, 300, beim("j1", "schließe"), anim="cut"),
           beim("j1", "schließe"), beim("j1", "Kellerabteil"), RAD_A - KM, 10),
    *l_k,
    ficon("tabler", "lock", KX0 + 45, 690, 60, beim("j1", "Kellerabteil"), fuell=GELB),
    ficon("tabler", "calendar", RAD_A, 520, 90, beim("leiht", "Juni"), fuell=WEISS, bis=beim("leiht", "September")),
    pl("Juni", RAD_A, 540, beim("leiht", "Juni"), fill=WEISS, size=30, anker="m", bis=beim("leiht", "September")),
    pl("geliehen bis Ende September", RAD_A, 360, beim("leiht", "September"), fill=GELB, size=32, anker="m", bis="a1"),
    # Anke
    *fig("AN", AN_A, BODEN, FH, [(NULL, "ruhig_r")], bis="a1", erst="cut"),
    *redet("AN_redet_r", AN_A, BODEN, FH, "a1", "j1"),
    peep_voll("AN_froh_r", AN_A, BODEN, FH, "j1", anim="cut"),
    hart(ns("Anke", AN_A, BODEN, NULL, AN_F)),
    # Jürgen
    *fig("JU", JU_A, BODEN, FH, [(NULL, "ruhig")], bis="j1", erst="cut"),
    *redet("JU_redet", JU_A, BODEN, FH, "j1", "laden"),
    hart(ns("Jürgen", JU_A, BODEN, NULL, JU_F)),
    blase("sprech", 690, 210, "a1", 560, 210, inhalt=["Bis September kannst du es haben.", "Aber pass gut darauf auf!"],
          textsize=32, figur=("AN_redet_r", AN_A, BODEN, FH), bis="j1"),
    blase("sprech", 600, 200, "j1", 900, 230, inhalt=["Versprochen. Ich schließe es", "in mein Kellerabteil."],
          textsize=32, figur=("JU_redet", JU_A, BODEN, FH), bis="laden"),
])

# B Fall: im Fahrradladen ----------------------------------------------------------------------------------------------------
JU_B, KU_B = 1430, 1730
SF = (500, 420, 420, 300)                   # Schaufenster (x, y, w, h)
SF_U = SF[1] + SF[3] - 18
WEG = (beim("ku1", "Räder"), beim("ku1", "Schaufenster", ende=True))
folie([("laden", "Fall · Im Fahrradladen")], [
    pl("Fahrradladen Kunze", 70, 40, "laden", fill=ORANGE, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "laden", breite=7, farbe=INK),
    ficon("tabler", "building-store", 250, BODEN - 2, 300, "laden", fuell=GELB),
    karte(*SF, "laden", fill=(226, 236, 252, 255), rund=10, schatten=6),
    pl("Schaufenster", SF[0] + SF[2] // 2, SF[1] - 70, beim("ku1", "Schaufenster"), fill=WEISS, size=30, anker="m"),
    # zwei Räder des Ladens, Jürgen stellt sie ins Schaufenster
    ficon("tabler", "bike", 1000, BODEN, 200, "laden", fuell=BLAU, bis=WEG[0]),
    ficon("tabler", "bike", 1220, BODEN, 200, "laden", fuell=ROT, d=0.15, bis=WEG[0]),
    bewegt(ficon("tabler", "bike", SF[0] + 110, SF_U, 200, WEG[0], fuell=BLAU, anim="cut"), *WEG, 1000 - SF[0] - 110, BODEN - SF_U),
    bewegt(ficon("tabler", "bike", SF[0] + 310, SF_U, 200, WEG[0], fuell=ROT, anim="cut"), *WEG, 1220 - SF[0] - 310, BODEN - SF_U),
    *fig("KU", KU_B, BODEN, FH, [(beim("laden", "Frau"), "ruhig")], bis="ku1"),
    *redet("KU_redet", KU_B, BODEN, FH, "ku1", "dieb"),
    ns("Frau Kunze", KU_B, BODEN, beim("laden", "Frau"), KU_F),
    *fig("JU", JU_B, BODEN, FH, [(beim("laden", "Jürgen"), "ruhig_r"), (WEG[0], "froh_r")], bis="dieb"),
    ns("Jürgen", JU_B, BODEN, beim("laden", "Jürgen"), JU_F),
    blase("sprech", 700, 200, "ku1", 1300, 220, inhalt=["Jürgen, stell bitte die neuen", "Räder ins Schaufenster."],
          textsize=32, figur=("KU_redet", KU_B, BODEN, FH)),
])

# C Fall: der Dieb -----------------------------------------------------------------------------------------------------------
CX0, CX1 = 90, 530
CM = (CX0 + CX1) // 2
DI0, DI1 = 760, 1260                        # Unbekannter: am Keller, dann mit dem Rad weg
RAD1, RAD2 = 1520, 960                      # Rad beim Unbekannten, dann bei Jürgen
JU_C = 700
SCHIEBT = (beim("dieb", "schiebt"), beim("dieb", "davon", ende=True))
NIMMT = (beim("zurueck", "nimmt"), beim("zurueck", "ab", ende=True))
r_c, l_c = kaefig(CX0, CX1, KY0, BODEN, "dieb")
folie([("dieb", "Fall · Der Dieb"), ("frage", "Fall · Die Frage")], [
    pl("Am Abend", 70, 40, "dieb", fill=LILA, size=48),
    ficon("tabler", "moon", 380, 120, 80, "dieb", fuell=GELB),
    linienzug([(60, BODEN), (1860, BODEN)], "dieb", breite=7, farbe=INK),
    *r_c,
    rad(CM, BODEN - 10, 300, "dieb", bis=SCHIEBT[0]),
    bewegt(rad(RAD1, BODEN, 300, SCHIEBT[0], anim="cut", bis=NIMMT[0]), *SCHIEBT, CM - RAD1, -10),
    bewegt(rad(RAD2, BODEN, 300, NIMMT[0], anim="cut"), *NIMMT, RAD1 - RAD2),
    *l_c,
    ficon("tabler", "lock", CX1 - 45, 690, 60, "dieb", fuell=GELB, bis=beim("dieb", "bricht")),
    szene(ficon("tabler", "lock-open", CX1 - 45, 690, 60, beim("dieb", "bricht"), fuell=ROT, anim="cut"), "027schloss*", 0.8),
    # der Unbekannte
    peep_voll("DI_geht", DI0, BODEN, FH, beim("dieb", "Unbekannter"), anim="fade", bis=SCHIEBT[0]),
    ns("Unbekannter", DI0, BODEN, beim("dieb", "Unbekannter"), DI_F, bis=SCHIEBT[0]),
    szene(bewegt(peep_voll("DI_geht_r", DI1, BODEN, FH, SCHIEBT[0], anim="cut", bis=NIMMT[0]), *SCHIEBT, DI0 - DI1),
          "027freilauf*", 0.7, 0.05),
    bewegt(ns("Unbekannter", DI1, BODEN, SCHIEBT[0], DI_F, anim="cut"), *SCHIEBT, DI0 - DI1),
    peep_voll("DI_ertappt", DI1, BODEN, FH, NIMMT[0], anim="cut"),
    # Jürgen
    bewegt(peep_voll("JU_ruft_r", JU_C, BODEN, FH, beim("hinter", "Jürgen"), anim="fade", bis="j2"),
           beim("hinter", "rennt"), beim("hinter", "hinterher", ende=True), -120),
    bewegt(ns("Jürgen", JU_C, BODEN, beim("hinter", "Jürgen"), JU_F, anim="fade"),
           beim("hinter", "rennt"), beim("hinter", "hinterher", ende=True), -120),
    *redet("JU_ruft_r", JU_C, BODEN, FH, "j2", "zurueck"),
    *fig("JU", JU_C, BODEN, FH, [("zurueck", "ernst_r"), (NIMMT[1], "froh_r")], erst="cut"),
    blase("sprech", 520, 170, "j2", 900, 250, inhalt=["Halt! Das Rad bleibt hier!"], textsize=36,
          figur=("JU_ruft_r", JU_C, BODEN, FH), bis="zurueck"),
    pl("an der nächsten Ecke", 1250, 330, beim("zurueck", "Ecke"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("Wem gehört das Rad? Wer besitzt es?", 1060, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Durfte Jürgen es sich zurückholen?", 1060, 250, beim("frage", "durfte"), fill=PINK, size=36, anker="m"),
])

# D Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Anke leiht ihrem Mitbewohner Jürgen im Juni ihr Fahrrad, bis Ende September. Jürgen schließt es in sein "
    "Kellerabteil. Tagsüber jobbt er im Fahrradladen von Frau Kunze und stellt dort auf ihre Anweisung die neuen Räder "
    "des Ladens ins Schaufenster.",
    "An einem Abend bricht ein Unbekannter das Kellerabteil auf und schiebt das Rad davon. Jürgen sieht ihn, rennt "
    "sofort hinterher und nimmt dem Mann das Rad an der nächsten Ecke wieder ab.",
], "Wem gehört das Rad, wer besitzt es – und durfte Jürgen es sich zurückholen?")

# E Eigentum, § 903 S. 1 ------------------------------------------------------------------------------------------------------
W903 = ["„Der Eigentümer einer Sache kann, soweit nicht das Gesetz oder", "Rechte Dritter entgegenstehen, mit der Sache nach Belieben",
        "verfahren und andere von jeder Einwirkung ausschließen.“"]
w903, w903_y = wortlaut(80, 300, 1100, W903, "§ 903 Satz 1 BGB", "p903", marken=[
    (0, "soweit nicht das Gesetz oder", beim("p903", "soweit")), (1, "Rechte Dritter entgegenstehen", beim("p903", "soweit")),
    (1, "nach Belieben", beim("p903", "Belieben")), (2, "verfahren", beim("p903", "Belieben")),
    (2, "von jeder Einwirkung ausschließen", beim("p903", "Einwirkung"))], size=34)
folie([("eig", "Eigentum, § 903 BGB")], rechts_frei([
    *tafel("eig", "Eigentum"),
    z("Eigentum: die rechtliche Herrschaft über eine Sache", 110, 200, beim("eig", "Eigentum"), "Bold", 36),
    *w903,
    blk(110, w903_y + 70, 1040, 100, GRUEN, "anke", [("Eigentümerin: Anke, die ganze Zeit", "ExtraBold", 38, INK)]),
    ficon("tabler", "certificate", FX, 400, 150, "eig", fuell=GELB),
    *fig("AN", FX, FB, FR, [("eig", "ruhig"), ("anke", "zufrieden")]),
    ns("Anke", FX, FB, "eig", AN_F),
]))

# F Besitz, § 854 I -----------------------------------------------------------------------------------------------------------
W854 = ["„Der Besitz einer Sache wird durch die Erlangung der", "tatsächlichen Gewalt über die Sache erworben.“"]
w854, w854_y = wortlaut(80, 270, 1100, W854, "§ 854 Abs. 1 BGB", "p854", marken=[
    (0, "Erlangung der", beim("p854", "Erlangung")), (1, "tatsächlichen Gewalt", beim("p854", "Erlangung"))], size=38)
folie([("besitz", "Besitz, § 854 I BGB"), ("jb", "Besitz › Jürgen: unmittelbarer Besitz")], rechts_frei([
    *tafel("besitz", "Besitz"),
    z("Besitz: die tatsächliche Herrschaft", 110, 190, beim("besitz", "Besitz"), "Bold", 36),
    *w854,
    z("+ Besitzwille (nach h. M.)", 110, w854_y + 40, "wille", "Bold", 34),
    z("maßgeblich: die Verkehrsanschauung", 110, w854_y + 100, "verkehr", size=34),
    zit("BGH, Urt. v. 17.3.2017 – V ZR 70/16, Rn. 10", 150, w854_y + 155, beim("verkehr", "Bundesgerichtshof")),
    ok(140, w854_y + 240, "jb", gr=22),
    z("Jürgen: Rad im abgeschlossenen Kellerabteil", 185, w854_y + 220, "jb", size=34),
    blk(110, w854_y + 300, 1040, 90, BLAU, beim("jb", "unmittelbarer"), [("Jürgen ist unmittelbarer Besitzer", "ExtraBold", 38, INK)]),
    rad(FX, 380, 220, "besitz"),
    ficon("tabler", "lock", FX + 150, 380, 60, beim("jb", "abgeschlossenen"), fuell=GELB),
    *fig("JU", FX, FB, FR, [("besitz", "ruhig"), ("jb", "froh")]),
    ns("Jürgen", FX, FB, "besitz", JU_F),
]))

# G mittelbarer Besitz, § 868 ---------------------------------------------------------------------------------------------------
W868 = ["„Besitzt jemand eine Sache als Nießbraucher, Pfandgläubiger,", "Pächter, Mieter, Verwahrer oder in einem ähnlichen Verhältnis,",
        "vermöge dessen er einem anderen gegenüber auf Zeit zum Besitz", "berechtigt oder verpflichtet ist, so ist auch der andere",
        "Besitzer (mittelbarer Besitz).“"]
w868, w868_y = wortlaut(80, 180, 1100, W868, "§ 868 BGB", "p868", marken=[
    (1, "Mieter, Verwahrer", beim("p868", "Mieter")), (1, "in einem ähnlichen Verhältnis", beim("p868", "ähnlichen")),
    (2, "auf Zeit zum Besitz", beim("zeit", "Zeit")), (3, "berechtigt", beim("zeit", "berechtigt")),
    (3, "so ist auch der andere", beim("zeit", "auch")), (4, "Besitzer", beim("zeit", "auch"))], size=32)
folie([("mittel", "Mittelbarer Besitz, § 868 BGB"), ("leihe", "Mittelbarer Besitz › Leihe als Besitzmittlungsverhältnis")],
      rechts_frei([
    *tafel("mittel", "Mittelbarer Besitz", size=46),
    *w868,
    z("Leihe bis September = Besitzmittlungsverhältnis", 110, w868_y + 30, "leihe", "Bold", 34),
    z("danach Rückgabe (§ 604 Abs. 1 BGB), von Jürgen anerkannt", 150, w868_y + 85, beim("leihe", "Danach"), size=31),
    zit("BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 20, 24", 150, w868_y + 135, beim("leihe", "erkennt")),
    blk(110, w868_y + 190, 1040, 90, GRUEN, "mb", [("Anke ist mittelbare Besitzerin", "ExtraBold", 38, INK)]),
    rad((X1 + X2) // 2, 380, 220, "mittel"),
    pl("bis September", (X1 + X2) // 2, 150, "leihe", fill=GELB, size=28, anker="m"),
    *fig("AN", X1, FB, FR, [("mittel", "denkt"), ("mb", "zufrieden")]),
    *fig("JU", X2, FB, FR, [("mittel", "ruhig")], d=0.2),
    ns("Anke", X1, FB, "mittel", AN_F, d=0.2),
    ns("Jürgen", X2, FB, "mittel", JU_F, d=0.3),
]))

# H Eigen- und Fremdbesitz, § 872 ---------------------------------------------------------------------------------------------
W872 = ["„Wer eine Sache als ihm gehörend besitzt, ist Eigenbesitzer.“"]
w872, w872_y = wortlaut(80, 200, 1100, W872, "§ 872 BGB", "p872", marken=[
    (0, "als ihm gehörend", beim("p872", "gehörend"))], size=38)
folie([("p872", "Eigen- und Fremdbesitz, § 872 BGB")], rechts_frei([
    *tafel("p872", "Eigen- und Fremdbesitz"),
    *w872,
    ok(140, w872_y + 90, beim("p872", "Eigenbesitzerin"), gr=22),
    z("Anke: Eigenbesitzerin", 185, w872_y + 70, beim("p872", "Eigenbesitzerin"), "Bold", 38),
    ok(140, w872_y + 180, beim("fremd", "Fremdbesitzer"), gr=22),
    z("Jürgen: Fremdbesitzer", 185, w872_y + 160, "fremd", "Bold", 38),
    z("besitzt das Rad als fremde Sache", 225, w872_y + 220, beim("fremd", "fremde"), size=34),
    rad((X1 + X2) // 2, 380, 220, "p872"),
    *fig("AN", X1, FB, FR, [("p872", "zufrieden")]),
    *fig("JU", X2, FB, FR, [("p872", "ruhig"), ("fremd", "denkt")], d=0.2),
    ns("Anke", X1, FB, "p872", AN_F, d=0.2),
    ns("Jürgen", X2, FB, "p872", JU_F, d=0.3),
]))

# I Besitzdiener, § 855; Erbenbesitz, § 857 --------------------------------------------------------------------------------------
W855 = ["„Übt jemand die tatsächliche Gewalt über eine Sache für einen", "anderen in dessen Haushalt oder Erwerbsgeschäft oder in einem",
        "ähnlichen Verhältnis aus, vermöge dessen er den sich auf die", "Sache beziehenden Weisungen des anderen Folge zu leisten hat,",
        "so ist nur der andere Besitzer.“"]
w855, w855_y = wortlaut(80, 160, 1100, W855, "§ 855 BGB", "p855", marken=[
    (0, "tatsächliche Gewalt", beim("p855", "tatsächliche")), (0, "für einen", beim("p855", "für")),
    (1, "anderen", beim("p855", "für")), (1, "Erwerbsgeschäft", beim("p855", "Erwerbsgeschäft")),
    (3, "Weisungen des anderen Folge zu leisten", beim("p855", "Weisungen")), (4, "so ist nur der andere Besitzer", beim("p855", "nur"))],
    size=32)
folie([("diener", "Besitzdiener, § 855 BGB"), ("p857", "Sonderfall · Erbenbesitz, § 857 BGB")], rechts_frei([
    *tafel("diener", "Besitzdiener"),
    *w855,
    ok(140, w855_y + 50, beim("kunze", "Besitzdiener"), gr=20),
    z("Jürgen im Laden: nur Besitzdiener", 185, w855_y + 30, "kunze", "Bold", 34),
    z("Besitzerin: Frau Kunze", 225, w855_y + 80, beim("kunze", "Besitzerin"), size=32),
    zit("BGH, Urt. v. 30.1.2015 – V ZR 63/13, Rn. 19 (Arbeitnehmer)", 225, w855_y + 130, beim("bgh855", "Arbeitnehmer")),
    nein(140, w855_y + 205, "kontrast", gr=20),
    z("Anke und Jürgen: kein Weisungsverhältnis", 185, w855_y + 185, "kontrast", size=32),
    blk(110, w855_y + 250, 1040, 80, LILA, "p857", [("Sonderfall: Erbenbesitz, § 857 BGB", "ExtraBold", 34, INK)]),
    ficon("tabler", "bike", X1 - 60, 380, 150, "diener", fuell=BLAU, bis="kontrast"),
    ficon("tabler", "bike", X1 + 100, 380, 150, "diener", fuell=ROT, bis="kontrast"),
    rad(X2, 380, 200, "kontrast"),
    *fig("KU", X1, FB, FR, [("diener", "ruhig"), ("kunze", "froh")]),
    *fig("JU", X2, FB, FR, [("diener", "ruhig"), ("kontrast", "froh")], d=0.2),
    ns("Frau Kunze", X1, FB, "diener", KU_F, d=0.2),
    ns("Jürgen", X2, FB, "diener", JU_F, d=0.3),
]))

# J verbotene Eigenmacht, § 858 ---------------------------------------------------------------------------------------------------
folie([("eigenm", "Verbotene Eigenmacht, § 858 BGB"), ("fehler", "Verbotene Eigenmacht › fehlerhafter Besitz, § 858 II BGB")],
      rechts_frei([
    *tafel("eigenm", "Der Dieb"),
    z("§ 858 Abs. 1 BGB: Besitz ohne Willen entzogen", 110, 190, "p858", "Bold", 34),
    ok(140, 270, beim("p858", "verbotene"), gr=20), z("verbotene Eigenmacht", 185, 250, beim("p858", "verbotene"), "Bold", 36),
    z("nur gegen den unmittelbaren Besitzer: Jürgen", 110, 340, "unm", size=34),
    zit("BGH, Urt. v. 17.3.2017 – V ZR 70/16, Rn. 9", 150, 395, beim("unm", "unmittelbaren")),
    z("Unbekannter: Besitz, aber fehlerhaft (§ 858 Abs. 2 BGB)", 110, 480, "fehler", size=34),
    nein(140, 560, beim("fehler", "Eigentum"), gr=20), z("kein Eigentum", 185, 540, beim("fehler", "Eigentum"), "Bold", 36),
    rad(X1, 380, 200, "eigenm"),
    *fig("DI", X1, FB, FR, [("eigenm", "geht"), ("fehler", "ertappt")]),
    *fig("JU", X2, FB, FR, [("eigenm", "aerger"), ("unm", "ernst")], d=0.2),
    ns("Unbekannter", X1, FB, "eigenm", DI_F, d=0.2),
    ns("Jürgen", X2, FB, "eigenm", JU_F, d=0.3),
]))

# K Selbsthilfe, § 859 II ---------------------------------------------------------------------------------------------------------
folie([("p859", "Selbsthilfe, § 859 II BGB"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("p859", "Durfte Jürgen das?"),
    z("§ 859 Abs. 2 BGB: Der Besitzer darf dem verfolgten", 110, 190, beim("p859", "Paragraf"), "Bold", 34),
    z("Täter die weggenommene Sache wieder abnehmen.", 110, 240, beim("p859", "Täter"), "Bold", 34),
    ok(140, 340, "frisch", gr=20), z("Jürgen folgt ihm auf frischer Tat", 185, 320, "frisch", size=34),
    blk(110, 430, 1040, 150, GRUEN, "erg", [("Anke bleibt Eigentümerin.", "ExtraBold", 36, INK),
                                            ("Jürgen durfte seinen Besitz zurückholen.", "Bold", 34, INK)]),
    rad(X2, 380, 200, "p859"),
    *fig("DI", X1, FB, FR, [("p859", "ertappt")]),
    *fig("JU", X2, FB, FR, [("p859", "ruhig"), ("frisch", "froh")], d=0.2),
    ns("Unbekannter", X1, FB, "p859", DI_F, d=0.2),
    ns("Jürgen", X2, FB, "p859", JU_F, d=0.3),
]))

# L Gegenfall: Anke holt ihr Rad -------------------------------------------------------------------------------------------------
HX, JU_L, RAD_L, GX = 220, 520, 760, 1730
AN_L0, AN_L1 = 1000, 1180                   # Anke kommt, dann mit dem Rad an der Garage der Eltern
RAD_G = 1470
BRINGT = (beim("nimmt", "bringt"), beim("nimmt", "Eltern", ende=True))
folie([("gegen", "Gegenfall · Anke holt ihr Rad")], [
    pl("Im Juli", 70, 40, "gegen", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "gegen", breite=7, farbe=INK),
    ficon("ph", "house", HX, BODEN - 2, 300, "gegen", fuell=GELB),
    ficon("ph", "garage", GX, BODEN - 2, 240, beim("nimmt", "Garage"), fuell=BLAU),
    pl("Garage der Eltern", GX, 420, beim("nimmt", "Garage"), fill=WEISS, size=28, anker="m"),
    rad(RAD_L, BODEN, 280, "gegen", bis=BRINGT[0]),
    bewegt(rad(RAD_G, BODEN, 280, BRINGT[0], anim="cut"), *BRINGT, RAD_L - RAD_G),
    pl("ohne zu fragen", RAD_L, 420, beim("nimmt", "ohne"), fill=PINK, size=30, anker="m", bis=BRINGT[0]),
    # Jürgen stellt das Rad ab und geht kurz ins Haus, dann kommt er zurück
    peep_voll("JU_ruhig_r", JU_L, BODEN, FH, "gegen", bis=beim("nimmt", "abstellt", ende=True)),
    ns("Jürgen", JU_L, BODEN, "gegen", JU_F, bis=beim("nimmt", "abstellt", ende=True)),
    peep_voll("JU_schreck_r", JU_L, BODEN, FH, "j3", anim="fade", bis="j3"),
    *redet("JU_ruft_r", JU_L, BODEN, FH, "j3", "a2"),
    peep_voll("JU_aerger_r", JU_L, BODEN, FH, "a2", anim="cut"),
    ns("Jürgen", JU_L, BODEN, "j3", JU_F),
    # Anke
    peep_voll("AN_geht", AN_L0, BODEN, FH, beim("nimmt", "nimmt"), anim="fade", bis=BRINGT[0]),
    ns("Anke", AN_L0, BODEN, beim("nimmt", "nimmt"), AN_F, bis=BRINGT[0]),
    bewegt(peep_voll("AN_geht_r", AN_L1, BODEN, FH, BRINGT[0], anim="cut", bis="j3"), *BRINGT, AN_L0 - AN_L1),
    bewegt(ns("Anke", AN_L1, BODEN, BRINGT[0], AN_F, anim="cut"), *BRINGT, AN_L0 - AN_L1),
    peep_voll("AN_denkt", AN_L1, BODEN, FH, "j3", anim="cut", bis="a2"),
    *redet("AN_trotzig", AN_L1, BODEN, FH, "a2", "p861"),
    blase("sprech", 700, 200, "j3", 860, 230, inhalt=["Das Rad ist bis September geliehen!", "Ich will es zurück."],
          textsize=32, figur=("JU_ruft_r", JU_L, BODEN, FH), bis="a2"),
    blase("sprech", 460, 160, "a2", 1150, 250, inhalt=["Es ist aber mein Rad!"], textsize=36,
          figur=("AN_trotzig", AN_L1, BODEN, FH)),
])

# M Gegenfall: § 861, § 863 ----------------------------------------------------------------------------------------------------------
folie([("p861", "Gegenfall › verbotene Eigenmacht, § 858 I BGB"), ("anspr", "Gegenfall › § 861 I BGB"),
       ("p863", "Gegenfall › Einwendungen, § 863 BGB")], rechts_frei([
    *tafel("p861", "Gegenfall: Jürgen gegen Anke"),
    ok(140, 210, beim("p861", "verbotene"), gr=20), z("Anke: verbotene Eigenmacht", 185, 190, beim("p861", "verbotene"), "Bold", 36),
    z("Besitz ohne Jürgens Willen entzogen,", 185, 245, beim("p861", "entzogen"), size=32),
    z("kein Gesetz erlaubt es", 185, 290, beim("p861", "kein"), size=32),
    z("§ 861 Abs. 1 BGB: Wiedereinräumung des Besitzes", 110, 370, "anspr", "Bold", 34),
    nein(140, 470, "p863", gr=20), z("Eigentum von Anke? Hilft nicht.", 185, 450, "p863", "Bold", 34),
    z("§ 863 BGB: Recht zum Besitz nur für die Frage,", 185, 505, beim("p863", "Recht"), size=32),
    z("ob verbotene Eigenmacht vorliegt", 185, 550, beim("p863", "verbotene"), size=32),
    blk(110, 630, 1040, 100, GELB, "posses", [("possessorisch: schützt allein den Besitz", "ExtraBold", 36, INK)]),
    *fig("AN", X1, FB, FR, [("p861", "aerger"), ("p863", "denkt")]),
    *fig("JU", X2, FB, FR, [("p861", "ernst"), ("anspr", "froh")], d=0.2),
    ns("Anke", X1, FB, "p861", AN_F, d=0.2),
    ns("Jürgen", X2, FB, "p861", JU_F, d=0.3),
]))

# N Gegenprobe: § 985, § 986 ------------------------------------------------------------------------------------------------------------
folie([("p985", "Gegenprobe · § 985 BGB?"), ("p986", "Gegenprobe › Recht zum Besitz, § 986 BGB")], rechts_frei([
    *tafel("p985", "Gegenprobe: Anke gegen Jürgen"),
    z("§ 985 BGB: Herausgabe an die Eigentümerin?", 110, 190, beim("p985", "Paragraf"), "Bold", 34),
    nein(140, 270, beim("p985", "Nein"), gr=20), z("Nein.", 185, 250, beim("p985", "Nein"), "Bold", 36),
    z("petitorisch: schützt das Eigentum", 110, 330, beim("p985", "petitorische"), size=34),
    z("aber: Recht zum Besitz aus der Leihe", 110, 410, "p986", "Bold", 34),
    z("bis September, § 986 Abs. 1 BGB", 150, 465, beim("p986", "September"), size=34),
    ficon("tabler", "certificate", X1, 380, 120, "p985", fuell=GELB),
    rad(X2, 380, 200, "p986"),
    *fig("AN", X1, FB, FR, [("p985", "denkt"), ("p986", "aerger")]),
    *fig("JU", X2, FB, FR, [("p985", "ruhig"), ("p986", "froh")], d=0.2),
    ns("Anke", X1, FB, "p985", AN_F, d=0.2),
    ns("Jürgen", X2, FB, "p985", JU_F, d=0.3),
]))

# O Ausblick: Übereignung ------------------------------------------------------------------------------------------------------------------
folie([("ausblick", "Ausblick · Übereignung"), ("p929", "Ausblick › Übergabe, § 929 S. 1 BGB"),
       ("p930", "Ausblick › Besitzkonstitut, § 930 BGB"), ("p931", "Ausblick › Abtretung, § 931 BGB")], rechts_frei([
    *tafel("ausblick", "Ausblick: Besitz und Übereignung"),
    z("Der Besitz entscheidet auch bei der Übereignung.", 110, 190, beim("ausblick", "Besitz"), "Bold", 34),
    z("§ 929 S. 1 BGB: Übergabe, also ein Besitzwechsel", 110, 290, "p929", size=34),
    z("§ 930 BGB: Veräußerer behält die Sache,", 110, 370, "p930", size=34),
    z("Erwerber bekommt mittelbaren Besitz", 150, 420, beim("p930", "Erwerber"), size=34),
    z("§ 931 BGB: Abtretung des Herausgabeanspruchs", 110, 500, "p931", size=34),
    z("Anke übereignet, während Jürgen das Rad hat", 150, 550, beim("p931", "Anke"), size=32, farbe=TEXT),
    ficon("tabler", "arrows-exchange", (X1 + X2) // 2, 380, 140, "p929", fuell=WEISS, bis="p930"),
    ficon("tabler", "home", (X1 + X2) // 2, 380, 130, "p930", fuell=GELB, bis="p931"),
    ficon("tabler", "writing-sign", (X1 + X2) // 2, 380, 130, "p931", fuell=WEISS),
    *fig("AN", X1, FB, FR, [("ausblick", "ruhig"), ("p931", "zufrieden")]),
    *fig("JU", X2, FB, FR, [("ausblick", "ruhig")], d=0.2),
    ns("Anke", X1, FB, "ausblick", AN_F, d=0.2),
    ns("Jürgen", X2, FB, "ausblick", JU_F, d=0.3),
]))

# P Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Besitz je Person"), ("tipp2", "Klausurtipp · § 861 ohne Eigentum")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Besitz für jede Person einzeln bestimmen:", 200, 200, beim("tipp", "Bestimme"), "Bold", 36),
    z("unmittelbar oder mittelbar", 200, 260, beim("tipp", "unmittelbar"), size=34),
    z("Besitzdiener", 200, 310, beim("tipp", "Besitzdiener"), size=34),
    z("Eigen- oder Fremdbesitz", 200, 360, beim("tipp", "Eigen-"), size=34),
    z("Bei § 861 BGB nicht prüfen, wem die Sache gehört.", 110, 470, "tipp2", "Bold", 34),
    nein(140, 560, beim("tipp2", "Der"), gr=20),
    z("„Anke ist doch Eigentümerin“ gehört dort nicht hin.", 185, 540, beim("tipp2", "Der"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# Q Klausurschema --------------------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Jürgen gegen Anke, § 861 Abs. 1 BGB"), 110, 90, "sch", 46),
    *plusminus("I. Jürgen war Besitzer", K1, 200, "k1", True, size=38, stil="Bold"),
    *plusminus("II. Besitz durch verbotene Eigenmacht entzogen (§ 858 Abs. 1 BGB)", K1, 275, "k2", True, size=38, stil="Bold"),
    *plusminus("III. Anke besitzt Jürgen gegenüber fehlerhaft (§ 858 Abs. 2 BGB)", K1, 350, "k3", True, size=38, stil="Bold"),
    z("IV. kein Ausschluss (§ 861 Abs. 2 BGB),", K1, 425, "k4", "Bold", 38, rechts=1820),
    z("kein Erlöschen (§ 864 BGB)", K2, 480, beim("k4", "Erlöschen"), size=36, rechts=1820),
    z("V. Einwendungen nur nach § 863 BGB", K1, 555, "k5", "Bold", 38, rechts=1820),
        blk(K1, 700, 1500, 100, GRUEN, "k6", [("Ergebnis: Anke muss Jürgen den Besitz wieder einräumen.", "ExtraBold", 38, INK)]),
])

# R Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eigentum ist das ", 0), ("rechtliche", "a"), (" Haben,", 0)],
                 [("Besitz das ", 0), ("tatsächliche.", "b")]], 750, 320, 50, "merke",
                {"a": beim("merke", "rechtliche"), "b": beim("merke", "tatsächliche")}),
    *markertext([[("Der Besitz wird für sich geschützt,", 0)], [("sogar ", 0), ("gegen die Eigentümerin.", "c")]],
                750, 560, 46, "m2", {"c": beim("m2", "gegen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
