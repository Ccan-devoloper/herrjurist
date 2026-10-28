"""Folge 031 · Gemüseblatt-Fall: Vertrag mit Schutzwirkung für Dritte erklärt – Serienstandard Open Peeps (Katzenkönig).
Echter Fall (BGH, Urt. v. 28.1.1976 – VIII ZR 246/74 = BGHZ 66, 51), sachlich nacherzählt; Beteiligte nur als namenlose
Funktionsfiguren (Mutter, Tochter, Betreiber des Ladens). Szenen laut ../SZENENPLAN.md: A Im Selbstbedienungsladen,
B Die Klage, C Sachverhalt, D Warum Vertrag?, E Die Mutter (Wortlaut § 311 II, § 241 II), F Die Tochter selbst,
G Vertrag mit Schutzwirkung, H Vier Voraussetzungen, I Vor Vertragsschluss, J Streitstand, K/L Prüfung, M Heute,
N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi). Geräusch nur bei sichtbarer Handlung (Sturz; Freesound CC0).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns wie in
Folge 027 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_031/"


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
        if n.startswith(("bild:", "ficon:")) or "/op_031/" in n:
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


BODEN, FH = 880, 480
TOH = 430                                   # Tochter (14) etwas kleiner als die Erwachsenen
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FR_T = 430                                  # Tochter neben der Tafel
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
MU_F, TO_F, BE_F = LILA, GELB, BLAU         # Farben der Namensschilder
BLATT = (110, 190, 95, 255)                 # Gemüseblatt (Tabler „leaf“, grün gefüllt)
HOLZ = (232, 205, 160, 255)                 # Ladentheke/Kasse


def blatt(cx, unten, breite, cue, **k):
    """Gemüseblatt: Tabler-Icon „leaf“ (MIT), grün gefüllt, flach auf dem Boden (um 70° gedreht, nicht umgezeichnet)."""
    e = ficon("tabler", "leaf", cx, unten, breite, cue, fuell=BLATT, **k)
    sp = e.sprite.rotate(-70, expand=True, resample=Image.BICUBIC)
    return El(sp, cx - sp.width / 2, unten - sp.height, cue, e.anim, e.d, e.bis, name="ficon:leaf-liegend")


def mu(cx, unten, hoehe, folge, **k):
    return fig("MU", cx, unten, hoehe, folge, **k)


def to(cx, unten, hoehe, folge, **k):
    return fig("TO", cx, unten, hoehe, folge, **k)


def be(cx, unten, hoehe, folge, **k):
    return fig("BE", cx, unten, hoehe, folge, **k)


# A Fall: im Selbstbedienungsladen ------------------------------------------------------------------------------------------
RX0, RX1, RY0 = 60, 330, 380                # Regal
KA0, KA1, KAY = 760, 1060, 660              # Kasse (Theke)
PA0, PA1, PAY = 1560, 1860, 720             # Packablage
MU_A, TO_A0, TO_A1 = 650, 440, 1440         # Mutter an der Kasse; Tochter neben ihr, dann an der Packablage
BL_X = 1300                                 # Gemüseblatt am Boden vor der Packablage
TS_X, TSH = 1340, 300                       # Tochter am Boden (sitting/mid-1, gleicher Kopfmaßstab)
GEHT = (beim("pack", "geht"), beim("pack", "Packablage", ende=True))
STURZ = beim("rutscht", "stürzt")
MU_RED = ("MU_redet_r", MU_A, BODEN, FH)
folie([(NULL, "Fall · Im Selbstbedienungsladen")], [
    hart(pl("November 1963 · Selbstbedienungsladen", 70, 40, NULL, fill=GELB, size=44)),
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    # Regal mit Waren
    hart(karte(RX0, RY0, RX1 - RX0, BODEN - RY0, NULL, fill=(244, 236, 222, 255), rund=8, schatten=6, rand=5)),
    hart(linienzug([(RX0 + 6, 545), (RX1 - 6, 545)], NULL, breite=6, farbe=INK)),
    hart(linienzug([(RX0 + 6, 710), (RX1 - 6, 710)], NULL, breite=6, farbe=INK)),
    hart(ficon("tabler", "carrot", 130, 540, 80, NULL, fuell=ORANGE)),
    hart(ficon("tabler", "apple", 260, 540, 80, NULL, fuell=ROT)),
    hart(ficon("tabler", "leaf", 130, 705, 80, NULL, fuell=BLATT)),
    hart(ficon("tabler", "basket", 260, 705, 90, NULL, fuell=GELB)),
    hart(ficon("tabler", "shopping-bag", 195, BODEN - 8, 90, NULL, fuell=BLAU)),
    # Tochter geht hinter der Kasse herum zur Packablage (vor der Theke gezeichnet = hinter ihr)
    bewegt(peep_voll("TO_froh_r", TO_A1, BODEN, TOH, GEHT[0], anim="cut", bis=STURZ), *GEHT, TO_A0 - TO_A1),
    # Kasse und Packablage
    hart(karte(KA0, KAY, KA1 - KA0, BODEN - KAY, NULL, fill=HOLZ, rund=8, schatten=6, rand=5)),
    hart(ficon("tabler", "cash-register", (KA0 + KA1) // 2 + 40, KAY, 150, NULL, fuell=WEISS)),
    hart(karte(PA0, PAY, PA1 - PA0, BODEN - PAY, NULL, fill=(236, 236, 240, 255), rund=8, schatten=6, rand=5)),
    pl("Kasse", (KA0 + KA1) // 2, 950, beim("kasse", "Kasse"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "carrot", KA0 + 70, KAY, 70, beim("kasse", "Waren"), fuell=ORANGE),
    ficon("tabler", "apple", KA0 + 140, KAY, 60, beim("kasse", "Waren"), fuell=ROT, d=0.1),
    pl("Packablage", (PA0 + PA1) // 2, 620, beim("pack", "Packablage"), fill=WEISS, size=30, anker="m", bis="knie"),
    pl("Gemüseblatt", 1180, 960, beim("rutscht", "Gemüseblatt"), fill=GRUEN, size=28, anker="m"),
    # Mutter an der Kasse (blickt nach rechts zur Kasse und zur Tochter)
    *mu(MU_A, BODEN, FH, [(beim("mutter", "Mutter"), "ruhig_r"), (STURZ, "schreck_r")], bis="m1"),
    *redet("MU_redet_r", MU_A, BODEN, FH, "m1", "knie"),
    *mu(MU_A, BODEN, FH, [("knie", "sorge_r")], erst="cut"),
    ns("Mutter", MU_A, BODEN, beim("mutter", "Mutter"), MU_F),
    blase("sprech", 520, 200, "m1", 860, 230, inhalt=["Hast du dir wehgetan?"], textsize=36, figur=MU_RED, bis="knie"),
    # Tochter: neben der Mutter, geht zur Packablage, rutscht aus
    peep_voll("TO_froh_r", TO_A0, BODEN, TOH, beim("tochter", "Tochter"), bis=GEHT[0]),
    ns("Tochter, 14", TO_A0, BODEN, beim("tochter", "Tochter"), TO_F, bis=GEHT[0]),
    bewegt(ns("Tochter, 14", TO_A1, BODEN, GEHT[0], TO_F, anim="cut", bis=STURZ), *GEHT, TO_A0 - TO_A1),
    szene(peep_voll("TS_schreck", TS_X, BODEN, TSH, STURZ, anim="cut", bis="knie"), "031sturz*", 1.0, -0.2),
    peep_voll("TS_schmerz", TS_X, BODEN, TSH, "knie", anim="cut"),
    blatt(BL_X, BODEN + 4, 90, beim("rutscht", "Gemüseblatt")),
    ns("Tochter, 14", TS_X, BODEN, STURZ, TO_F, anim="cut"),
    ficon("tabler", "bandage", TS_X + 150, BODEN - 120, 70, beim("knie", "Knie"), fuell=WEISS),
    pl("am Knie verletzt", TS_X, 470, beim("knie", "Knie"), fill=ROT, size=30, anker="m"),
    pl("länger behandelt", TS_X, 395, beim("knie", "behandelt"), fill=WEISS, size=28, anker="m"),
])

# B Die Klage (1970) --------------------------------------------------------------------------------------------------------
TO_B, BE_B = 520, 1400
BE_RED = ("BE_redet", BE_B, BODEN, FH)
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Die Frage")], [
    pl("1970 · die Klage", 70, 40, "klage", fill=LILA, size=44),
    linienzug([(40, BODEN), (1880, BODEN)], "klage", breite=7, farbe=INK),
    ficon("tabler", "building-store", 1720, BODEN - 2, 230, "klage", fuell=GELB),
    *to(TO_B, BODEN, TOH, [("klage", "ernst_r"), ("frage", "denkt_r")]),
    ns("Tochter", TO_B, BODEN, "klage", TO_F),
    ficon("tabler", "file-text", TO_B + 230, 560, 100, beim("klage", "verklagt"), fuell=WEISS),
    pl("Klage auf Ersatz des Schadens", 960, 330, beim("klage", "Ersatz"), fill=GELB, size=32, anker="m", bis="b1"),
    *be(BE_B, BODEN, FH, [(beim("klage", "Betreiber"), "ruhig")], bis="b1"),
    *redet("BE_redet", BE_B, BODEN, FH, "b1", "frage"),
    *be(BE_B, BODEN, FH, [("frage", "abwehr")], erst="cut"),
    ns("Betreiber des Ladens", BE_B, BODEN, beim("klage", "Betreiber"), BE_F),
    blase("sprech", 640, 200, "b1", 960, 200, inhalt=["Die Ansprüche sind doch", "längst verjährt!"], textsize=36,
          figur=BE_RED, bis="frage"),
    ficon("tabler", "hourglass", 960, 470, 90, beim("b1", "verjährt"), fuell=GELB),
    pl("Vertraglicher Anspruch der Tochter?", 960, 140, "frage", fill=PINK, size=40, anker="m"),
    pl("wollte selbst nichts kaufen", 960, 240, beim("frage", "selbst"), fill=WEISS, size=32, anker="m"),
])

# C Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Im November 1963 begleitet eine 14-jährige Tochter ihre Mutter zum Einkauf in einen kleinen Selbstbedienungsladen. "
    "Die Mutter hat ihre Waren ausgesucht und steht noch an der Kasse. Die Tochter geht um die Kasse herum zur "
    "Packablage, um beim Einpacken zu helfen. Dort rutscht sie auf einem Gemüseblatt aus und verletzt sich am Knie; "
    "sie muss länger ärztlich behandelt werden.",
    "1970 verklagt die Tochter den Betreiber des Ladens auf Ersatz ihres Schadens. Er beruft sich unter anderem "
    "auf Verjährung.",
    "BGH, Urt. v. 28.1.1976 – VIII ZR 246/74, BGHZ 66, 51 (Gemüseblatt-Fall)",
], "Hat die Tochter einen vertraglichen Anspruch gegen den Betreiber?")

# D Warum ein vertraglicher Anspruch? ----------------------------------------------------------------------------------------
folie([("delikt", "Vorfrage · Delikt oder Vertrag?"), ("verj", "Vorfrage · Verjährung damals"),
       ("vorteil", "Vorfrage · Vorteile der vertraglichen Haftung")], rechts_frei([
    *tafel("delikt", "Warum ein vertraglicher Anspruch?", size=44),
    z("§ 823 Abs. 1 BGB: Verkehrssicherungspflicht", 110, 190, "delikt", "Bold", 34),
    nein(140, 280, "verj", gr=20),
    z("Delikt: kürzere Verjährung, § 852 BGB a. F.", 185, 260, "verj", size=34),
    ok(140, 350, "dreissig", gr=20),
    z("Verschulden bei Vertragsschluss: 30 Jahre", 185, 330, "dreissig", size=34),
    z("Weitere Vorteile (BGHZ 66, 51):", 110, 430, "vorteil", "Bold", 34),
    ok(140, 510, "v278", gr=20),
    z("Gehilfen: § 278 BGB statt § 831 BGB", 185, 490, "v278", size=34),
    z("keine Entlastung", 225, 540, beim("v278", "Entlastung"), size=32, farbe=TEXT),
    ok(140, 630, "vbew", gr=20),
    z("Beweislast für das Verschulden beim Betreiber", 185, 610, "vbew", size=34),
    zit("damals § 282 BGB a. F.; heute § 280 Abs. 1 Satz 2 BGB", 225, 660, beim("vbew", "Beweislast")),
    ficon("tabler", "hourglass", X2, 300, 90, "verj", fuell=GELB, bis="vorteil"),
    pl("verjährt?", X2, 320, "verj", fill=GELB, size=28, anker="m", bis="vorteil"),
    ficon("tabler", "link", X2, 300, 90, "v278", fuell=GELB, bis="vbew"),
    pl("§ 278 BGB", X2, 320, "v278", fill=GELB, size=28, anker="m", bis="vbew"),
    ficon("tabler", "scale", X2, 300, 100, "vbew", fuell=WEISS),
    pl("Beweislast", X2, 320, "vbew", fill=WEISS, size=28, anker="m"),
    *to(X1, FB, FR_T, [("delikt", "ernst")]),
    ns("Tochter", X1, FB, "delikt", TO_F),
    *be(X2, FB, FR, [("delikt", "ruhig"), ("dreissig", "ertappt"), ("v278", "denkt")], d=0.2),
    ns("Betreiber", X2, FB, "delikt", BE_F, d=0.2),
]))

# E Die Mutter: culpa in contrahendo – Wortlaut § 311 II und § 241 II ---------------------------------------------------------
W311 = ["„Ein Schuldverhältnis mit Pflichten nach § 241 Abs. 2 entsteht auch durch",
        "1. die Aufnahme von Vertragsverhandlungen,",
        "2. die Anbahnung eines Vertrags, bei welcher der eine Teil im Hinblick",
        "auf eine etwaige rechtsgeschäftliche Beziehung dem anderen Teil die",
        "Möglichkeit zur Einwirkung auf seine Rechte, Rechtsgüter und",
        "Interessen gewährt oder ihm diese anvertraut, oder",
        "3. ähnliche geschäftliche Kontakte.“"]
w311, w311_y = wortlaut(80, 175, 1100, W311, "§ 311 Abs. 2 BGB", "p311", marken=[
    (2, "Anbahnung eines Vertrags", beim("nr2", "Anbahnung")),
    (4, "Möglichkeit zur Einwirkung", beim("nr2", "Einwirkung")), (4, "Rechtsgüter", beim("nr2", "Rechtsgüter"))], size=30)
W241 = ["„Das Schuldverhältnis kann nach seinem Inhalt jeden Teil zur Rücksicht",
        "auf die Rechte, Rechtsgüter und Interessen des anderen Teils verpflichten.“"]
w241, w241_y = wortlaut(80, w311_y + 25, 1100, W241, "§ 241 Abs. 2 BGB", "p241", marken=[
    (0, "Rücksicht", beim("p241", "Rücksicht")), (1, "auf die Rechte, Rechtsgüter und Interessen", beim("p241", "Rechte"))],
    size=30)
folie([("mutter2", "Die Mutter · culpa in contrahendo"), ("p311", "Die Mutter · § 311 Abs. 2 Nr. 2 BGB: Anbahnung"),
       ("p241", "Die Mutter · Rücksichtspflichten, § 241 Abs. 2 BGB")], rechts_frei([
    *tafel("mutter2", "Die Mutter: culpa in contrahendo", size=44),
    *w311, *w241,
    ficon("tabler", "building-store", FX, 330, 170, "laden", fuell=GELB),
    pl("Laden für Kunden geöffnet", FX, 350, "laden", fill=GELB, size=28, anker="m"),
    pl("Mutter gestürzt? Ersatz", FX, 200, "mutter2", fill=WEISS, size=30, anker="m", bis="laden"),
    *mu(FX, FB, FR, [("mutter2", "ruhig"), ("p241", "froh")]),
    ns("Mutter", FX, FB, "mutter2", MU_F),
]))

# F Die Tochter selbst --------------------------------------------------------------------------------------------------------
folie([("kind", "Die Tochter · eigenes Schuldverhältnis?")], rechts_frei([
    *tafel("kind", "Und die Tochter?"),
    z("wollte selbst nichts kaufen, nur begleiten", 110, 190, "kind2", "Bold", 34),
    z("eigene culpa in contrahendo nur,", 110, 290, "kind3", "Bold", 34),
    z("wer den Laden zumindest als möglicher Kunde betritt", 150, 345, beim("kind3", "zumindest"), size=32),
    nein(140, 450, beim("kind4", "Schutz"), gr=20),
    z("nur Schutz vor dem Wetter", 185, 430, beim("kind4", "Schutz"), size=32),
    nein(140, 510, beim("kind4", "Durchgang"), gr=20),
    z("Laden als Durchgang", 185, 490, beim("kind4", "Durchgang"), size=32),
    zit("BGHZ 66, 51, Gründe IV.", 185, 545, beim("kind4", "Durchgang")),
    blk(110, 620, 1040, 100, ROT, "kind5", [("kein eigenes vorvertragliches Schuldverhältnis", "ExtraBold", 36, INK)]),
    ficon("tabler", "shopping-cart-off", FX, 330, 120, "kind2", fuell=WEISS, bis="kind4"),
    pl("nur begleitet", FX, 350, "kind2", fill=WEISS, size=28, anker="m", bis="kind4"),
    ficon("tabler", "umbrella", FX - 110, 330, 110, beim("kind4", "Schutz"), fuell=BLAU),
    ficon("tabler", "walk", FX + 110, 330, 100, beim("kind4", "Durchgang"), fuell=WEISS),
    *to(FX, FB, FR_T, [("kind", "ruhig"), ("kind3", "denkt"), ("kind5", "ernst")]),
    ns("Tochter", FX, FB, "kind", TO_F),
]))

# G Vertrag mit Schutzwirkung für Dritte ----------------------------------------------------------------------------------------
folie([("vsd", "Vertrag mit Schutzwirkung für Dritte")], rechts_frei([
    *tafel("vsd", "Vertrag mit Schutzwirkung für Dritte", size=44),
    z("Dritter im Schutzbereich eines fremden", 110, 190, "vsd2", "Bold", 34),
    z("Schuldverhältnisses", 150, 240, beim("vsd2", "Schuldverhältnisses"), "Bold", 34),
    nein(140, 340, "vsd3", gr=20), z("kein Anspruch auf die Leistung", 185, 320, "vsd3", size=34),
    ok(140, 410, beim("vsd3", "Schutz"), gr=20), z("aber Anspruch auf Schutz", 185, 390, beim("vsd3", "Schutz"), size=34),
    ok(140, 480, beim("vsd3", "Schadensersatz"), gr=20),
    z("Schadensersatz im eigenen Namen", 185, 460, beim("vsd3", "Schadensersatz"), size=34),
    zit("BGHZ 66, 51, Gründe V. 2.", 185, 515, beim("vsd3", "Schadensersatz")),
    blk(110, 600, 1040, 100, GELB, "vsd4", [("strenge Voraussetzungen", "ExtraBold", 38, INK)]),
    ficon("tabler", "building-store", X1, 300, 150, "vsd", fuell=GELB),
    pl("Betreiber", X1, 320, "vsd", fill=BLAU, size=26, anker="m"),
    ficon("tabler", "shield-check", X2, 300, 120, "vsd2", fuell=GRUEN),
    pl("Schutzbereich", X2, 320, "vsd2", fill=GRUEN, size=26, anker="m"),
    *mu(X1, FB, FR, [("vsd", "ruhig")]),
    ns("Mutter", X1, FB, "vsd", MU_F),
    *to(X2, FB, FR_T, [("vsd", "ruhig"), ("vsd3", "froh")], d=0.2),
    ns("Tochter", X2, FB, "vsd", TO_F, d=0.2),
]))

# H Die vier Voraussetzungen ------------------------------------------------------------------------------------------------------
VY = [180, 355, 530, 705]
folie([("ln", "Schutzwirkung › 1. Leistungsnähe"), ("gn", "Schutzwirkung › 2. Einbeziehungsinteresse (Gläubigernähe)"),
       ("ek", "Schutzwirkung › 3. Erkennbarkeit und Zumutbarkeit"), ("sb", "Schutzwirkung › 4. Schutzbedürfnis")], rechts_frei([
    karte(60, 60, 1140, 860, "ln"),
    z("1. Leistungsnähe", 110, VY[0], "ln", "Bold", 36),
    z("mit der Leistung in Berührung, gleiche Gefahren", 150, VY[0] + 50, beim("ln", "Dritte"), size=30, farbe=TEXT),
    ok(170, VY[0] + 125, "ln2", gr=18), z("mit der Mutter in der Kassenzone", 205, VY[0] + 105, "ln2", size=31),
    z("2. Einbeziehungsinteresse (Gläubigernähe)", 110, VY[1], "gn", "Bold", 36),
    ok(170, VY[1] + 75, "gn2", gr=18), z("Mutter verantwortlich für Wohl und Wehe", 205, VY[1] + 55, "gn2", size=31),
    z("3. Erkennbarkeit und Zumutbarkeit", 110, VY[2], "ek", "Bold", 36),
    ok(170, VY[2] + 75, "ek2", gr=18), z("Tochter gehört erkennbar dazu, zumutbar", 205, VY[2] + 55, "ek2", size=31),
    z("4. Schutzbedürfnis", 110, VY[3], "sb", "Bold", 36),
    ok(170, VY[3] + 75, "sb2", gr=18), z("kein eigener gleichwertiger vertraglicher Anspruch", 205, VY[3] + 55, "sb2", size=31),
    zit("Voraussetzungen: BGH, Urt. v. 5.7.2024 – V ZR 34/24, Rn. 14", 110, 855, "ln"),
    ficon("tabler", "cash-register", (X1 + X2) // 2, 330, 120, "ln2", fuell=WEISS, bis="gn2"),
    pl("Kassenzone", (X1 + X2) // 2, 350, "ln2", fill=WEISS, size=26, anker="m", bis="gn2"),
    ficon("tabler", "heart", (X1 + X2) // 2, 330, 110, "gn2", fuell=ROT, bis="ek2"),
    pl("Wohl und Wehe", (X1 + X2) // 2, 350, "gn2", fill=ROT, size=26, anker="m", bis="ek2"),
    ficon("tabler", "eye", (X1 + X2) // 2, 330, 120, "ek2", fuell=WEISS, bis="sb2"),
    pl("erkennbar", (X1 + X2) // 2, 350, "ek2", fill=WEISS, size=26, anker="m", bis="sb2"),
    ficon("tabler", "shield-check", (X1 + X2) // 2, 330, 110, "sb2", fuell=GRUEN),
    pl("schutzbedürftig", (X1 + X2) // 2, 350, "sb2", fill=GRUEN, size=26, anker="m"),
    *mu(X1, FB, FR, [("ln", "ruhig"), ("gn2", "froh")]),
    ns("Mutter", X1, FB, "ln", MU_F),
    *to(X2, FB, FR_T, [("ln", "ruhig"), ("sb2", "zufrieden")], d=0.2),
    ns("Tochter", X2, FB, "ln", TO_F, d=0.2),
]))

# I Schon vor dem Vertragsschluss ----------------------------------------------------------------------------------------------------
folie([("vor", "Schutzwirkung › schon vor dem Vertragsschluss")], rechts_frei([
    *tafel("vor", "Schon vor dem Kaufvertrag?"),
    z("Kauf noch nicht geschlossen", 110, 190, "vor", "Bold", 34),
    ok(140, 280, "vor2", gr=20), z("ohne Bedeutung: Schutzpflicht gilt vor", 185, 260, "vor2", size=34),
    z("wie nach dem Vertragsschluss", 185, 310, beim("vor2", "vor"), size=34),
    zit("BGHZ 66, 51, Gründe V. 4.", 185, 365, beim("vor2", "vor")),
    z("Gesetzesbegründung zu § 311 BGB:", 110, 450, "begr", "Bold", 34),
    z("„Salatblattfall des BGH“", 150, 505, beim("begr", "Salatblattfall"), size=34),
    zit("BT-Drs. 14/6040, S. 163", 150, 560, beim("begr", "Salatblattfall")),
    blk(110, 640, 1040, 140, GRUEN, "begr2", [("Schutzwirkung auch im", "ExtraBold", 36, INK),
                                            ("vorvertraglichen Schuldverhältnis", "ExtraBold", 36, INK)]),
    ficon("tabler", "cash-register", X1, 330, 130, "vor", fuell=WEISS),
    pl("noch an der Kasse", X1, 350, "vor", fill=WEISS, size=26, anker="m"),
    ficon("tabler", "book", X2, 330, 110, "begr", fuell=GRUEN),
    pl("§ 311 BGB", X2, 350, "begr", fill=GRUEN, size=26, anker="m"),
    *mu(X1, FB, FR, [("vor", "ruhig")]),
    ns("Mutter", X1, FB, "vor", MU_F),
    *to(X2, FB, FR_T, [("vor", "denkt"), ("vor2", "froh")], d=0.2),
    ns("Tochter", X2, FB, "vor", TO_F, d=0.2),
]))

# J Streitstand: Woraus folgt die Schutzwirkung? ---------------------------------------------------------------------------------------
folie([("streit", "Streitstand · Woraus folgt die Schutzwirkung?")], rechts_frei([
    *tafel("streit", "Woraus folgt die Schutzwirkung? (str.)", size=42),
    z("Rspr.: ergänzende Vertragsauslegung, § 157 BGB", 110, 190, "st1", "Bold", 34),
    zit("BGH, Urt. v. 5.7.2024 – V ZR 34/24, Rn. 13", 150, 245, beim("st1", "Vertragsauslegung")),
    z("a. A.: Gewohnheitsrecht, Rechtsfortbildung", 110, 315, "st2", "Bold", 34),
    z("BGHZ 66, 51: offen gelassen", 150, 370, beim("st2", "Bundesgerichtshof"), size=32, farbe=TEXT),
    z("zitiert oft: § 328 BGB analog", 110, 450, "st3", "Bold", 34),
    zit("z. B. BGH, Urt. v. 12.1.2011 – VIII ZR 346/09, Rn. 9", 150, 505, "st3"),
    z("§ 311 Abs. 3 Satz 1 BGB: Schuldverhältnis auch zu", 110, 585, "st4", "Bold", 34),
    z("Personen, die nicht Vertragspartei werden sollen", 150, 640, beim("st4", "Personen"), size=32),
    z("Weiterentwicklung offen (BT-Drs. 14/6040, S. 163)", 150, 700, "st5", size=32, farbe=TEXT),
    ficon("tabler", "scale", FX, 470, 220, "streit", fuell=WEISS),
    pl("umstritten", FX, 490, "streit", fill=PINK, size=32, anker="m"),
    ficon("tabler", "book", FX - 130, 800, 110, "st1", fuell=GRUEN),
    pl("§ 157", FX - 130, 820, "st1", fill=GRUEN, size=26, anker="m"),
    ficon("tabler", "book", FX + 130, 800, 110, "st3", fuell=BLAU),
    pl("§ 328 analog", FX + 130, 820, "st3", fill=BLAU, size=26, anker="m"),
]))

# K Prüfung: I. und II. --------------------------------------------------------------------------------------------------------------
folie([("a", "A. Tochter gegen Betreiber › §§ 280 I, 311 II, 241 II BGB mit Schutzwirkung"),
       ("p1", "A. Tochter gegen Betreiber › I. Schuldverhältnis mit Schutzwirkung"),
       ("p2", "A. Tochter gegen Betreiber › II. Pflichtverletzung")], rechts_frei([
    *tafel("a", "A. Tochter gegen Betreiber"),
    z("§§ 280 Abs. 1, 311 Abs. 2 Nr. 2, 241 Abs. 2 BGB", 110, 190, "a", "Bold", 34),
    z("mit Schutzwirkung für Dritte", 150, 240, "a", size=32),
    ok(140, 350, beim("p1", "Liegt"), gr=20),
    z("I. Schuldverhältnis mit Schutzwirkung", 185, 330, "p1", "Bold", 34),
    z("Mutter und Betreiber, Schutz für die Tochter", 225, 385, beim("p1", "Mutter"), size=31),
    z("II. Pflichtverletzung, § 241 Abs. 2 BGB", 185, 480, "p2", "Bold", 34),
    z("Boden verkehrssicher halten", 225, 535, beim("p2", "Betreiber"), size=31),
    ok(140, 610, "p2b", gr=20),
    z("Gemüseblatt am Boden: Gefahr aus seinem Bereich", 185, 590, "p2b", size=31),
    blatt((X1 + X2) // 2, 360, 120, "p2b"),
    pl("Gemüseblatt", (X1 + X2) // 2, 380, "p2b", fill=GRUEN, size=26, anker="m"),
    *to(X1, FB, FR_T, [("a", "ernst")]),
    ns("Tochter", X1, FB, "a", TO_F),
    *be(X2, FB, FR, [("a", "ruhig"), ("p2b", "ertappt")], d=0.2),
    ns("Betreiber", X2, FB, "a", BE_F, d=0.2),
]))

# L Prüfung: III., IV., Ergebnis ------------------------------------------------------------------------------------------------------
folie([("p3", "A. Tochter gegen Betreiber › III. Vertretenmüssen"),
       ("p4", "A. Tochter gegen Betreiber › IV. Schaden"), ("erg", "A. Tochter gegen Betreiber › Ergebnis")], rechts_frei([
    *tafel("p3", "A. Tochter gegen Betreiber"),
    z("III. Vertretenmüssen", 110, 190, "p3", "Bold", 34),
    z("vermutet, § 280 Abs. 1 Satz 2 BGB", 150, 245, beim("p3", "Es"), size=31),
    ok(140, 320, "p3b", gr=20), z("keine Entlastung: Sorgfalt nicht bewiesen", 185, 300, "p3b", size=31),
    z("Angestellte: § 278 BGB", 185, 355, "p3c", size=31, farbe=TEXT),
    z("IV. Schaden", 110, 440, "p4", "Bold", 34),
    ok(140, 515, beim("p4", "Aufwendungen"), gr=20), z("Aufwendungen", 185, 495, beim("p4", "Aufwendungen"), size=31),
    z("gekürzt: Mitverschulden 1/4, § 254 BGB", 185, 550, "p4b", size=31),
    blk(110, 640, 1040, 140, GRUEN, "erg", [("Ergebnis: BGH bestätigt den Anspruch,", "ExtraBold", 36, INK),
                                          ("nicht verjährt", "Regular", 34, INK)]),
    ficon("tabler", "link", (X1 + X2) // 2, 330, 90, "p3c", fuell=GELB),
    pl("§ 278", (X1 + X2) // 2, 350, "p3c", fill=GELB, size=26, anker="m"),
    *to(X1, FB, FR_T, [("p3", "ernst"), ("erg", "zufrieden")]),
    ns("Tochter", X1, FB, "p3", TO_F),
    *be(X2, FB, FR, [("p3", "ertappt"), ("erg", "ernst")], d=0.2),
    ns("Betreiber", X2, FB, "p3", BE_F, d=0.2),
]))

# M Und heute? -------------------------------------------------------------------------------------------------------------------------
folie([("heute", "Heute · was vom Vorteil bleibt")], rechts_frei([
    *tafel("heute", "Und heute?"),
    nein(140, 210, "h1", gr=20), z("Verjährungsvorteil weg:", 185, 190, "h1", "Bold", 34),
    z("beide Ansprüche regelmäßig 3 Jahre, § 195 BGB", 185, 245, beim("h1", "Beide"), size=32),
    ok(140, 345, "h2", gr=20), z("Schmerzensgeld, § 253 Abs. 2 BGB:", 185, 325, "h2", "Bold", 34),
    z("auch bei vertraglicher Haftung", 185, 380, beim("h2", "auch"), size=32),
    ok(140, 480, "h3", gr=20), z("bleibt: Gehilfen nach § 278 BGB", 185, 460, "h3", "Bold", 34),
    z("ohne Entlastung zugerechnet", 185, 515, beim("h3", "ohne"), size=32),
    ficon("tabler", "hourglass", X1, 330, 90, "h1", fuell=GELB),
    ficon("tabler", "coin-euro", (X1 + X2) // 2, 330, 90, "h2", fuell=GELB),
    ficon("tabler", "link", X2, 330, 90, "h3", fuell=GELB),
    *to((X1 + X2) // 2, FB, FR_T, [("heute", "ruhig"), ("h3", "zufrieden")]),
    ns("Tochter", (X1 + X2) // 2, FB, "heute", TO_F),
]))

# N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · erst das eigene Schuldverhältnis"), ("tipp2", "Klausurtipp · nicht § 328 BGB verwechseln")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst: Hat der Dritte selbst ein", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("Schuldverhältnis?", 200, 255, beim("tipp", "Schuldverhältnis"), "Bold", 36),
    z("Erst wenn nicht: Schutzwirkung", 200, 330, "tipp1", size=34),
    z("Nicht verwechseln mit § 328 BGB:", 110, 450, "tipp2", "Bold", 34),
    ok(140, 530, beim("tipp3", "Der"), gr=20), z("§ 328 BGB: Anspruch auf die Leistung", 185, 510, beim("tipp3", "Der"), size=32),
    ok(140, 600, beim("tipp3", "Schutzwirkung"), gr=20),
    z("Schutzwirkung: nur Anspruch auf Schutz", 185, 580, beim("tipp3", "Schutzwirkung"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# O Klausurschema --------------------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Vertrag mit Schutzwirkung für Dritte"), 110, 90, "sch", 46),
    z("Anspruch aus §§ 280 Abs. 1, 311 Abs. 2, 241 Abs. 2 BGB mit Schutzwirkung", K1, 190, "s1", "Bold", 36, rechts=1820),
    z("I. Schuldverhältnis mit Schutzwirkung", K1, 265, "s2", "Bold", 36, rechts=1820),
    z("1. Schuldverhältnis zwischen Gläubiger und Schuldner", K3, 320, beim("s2", "Erstens"), size=33, rechts=1820),
    z("2. Leistungsnähe", K3, 370, "s3", size=33, rechts=1820),
    z("3. Einbeziehungsinteresse (Gläubigernähe)", K3, 420, "s4", size=33, rechts=1820),
    z("4. Erkennbarkeit und Zumutbarkeit", K3, 470, "s5", size=33, rechts=1820),
    z("5. Schutzbedürfnis", K3, 520, "s6", size=33, rechts=1820),
    z("II. Pflichtverletzung (§ 241 Abs. 2 BGB)", K1, 595, "s7", "Bold", 36, rechts=1820),
    z("III. Vertretenmüssen (§ 280 Abs. 1 Satz 2, § 278 BGB)", K1, 665, "s8", "Bold", 36, rechts=1820),
    z("IV. Schaden, Mitverschulden (§ 254 BGB)", K1, 735, "s9", "Bold", 36, rechts=1820),
])

# P Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer nur begleitet,", 0)], [("bahnt keinen Vertrag an.", "a")]], 750, 320, 52, "merke",
                {"a": beim("merke", "bahnt")}),
    *markertext([[("Geschützt ist er trotzdem,", 0)], [("wenn er dem Kunden ", 0), ("so nahe steht,", "b")],
                 [("dass dessen Schutz ", 0), ("erkennbar auch ihm gilt.", "c")]],
                750, 540, 42, "m2", {"b": beim("m2", "so"), "c": beim("m2", "erkennbar")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
