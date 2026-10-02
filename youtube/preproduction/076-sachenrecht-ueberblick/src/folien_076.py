"""Folge 076 · Sachenrecht Überblick: Eigentum an Sachen und Grundstücken – Serienstandard Open Peeps (Katzenkönig).
Ein durchgehender Beispielfall mit drei Stationen: Nina kauft ein Handy (Arne, Handy der Schwester), ein Auto
(Herr Kuhnert, Auto des Schwagers, keine Zulassungsbescheinigung Teil II) und ein Haus (Frau Lohse, unrichtiges Grundbuch).
Szenen laut ../SZENENPLAN.md: A1 Handy, A2 Auto, A3 Haus, A4 Frage, B Sachverhalt, C Grundsätze, D § 929 S. 1 (Wortlaut),
E Übergabeersatz, F § 932 (Wortlaut I 1 und II), G Rechtsschein des Besitzes, H § 935, I Auto, J § 873 I (Wortlaut) und
§ 925, K § 892, Widerspruch, Vormerkung, L Vergleichstabelle (progressiv), M Ergebnis, N Klausurtipp (Lexi),
O Klausurschema, P Merksatz (Lexi).
Zwei Handlungsgeräusche (Motorstart beim Losfahren, Unterschrift beim Notar; ../geraeusche_herkunft.json). Namensschild
jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als eigene Kopie
aus den Folgen 027 und 073 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_076/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (250, 205, 198, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_076/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073) ------------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
NI_F, AR_F, KU_F, LO_F = LILA, BLAU, WEISS, GELB     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


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


def paar(c0, l, lf, r, rf, ln, lfarbe, rn, rfarbe):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf), ns(ln, X1, FB, c0, lfarbe, d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(rn, X2, FB, c0, rfarbe, d=0.3)]


HANDY = ("tabler", "device-mobile", 90, WEISS)
AUTO = ("tabler", "car", 200, BLAU)
HAUS = ("ph", "house", 170, GELB)
BUCH = ("tabler", "book-2", 120, WEISS)

# A1 Fall: das Handy -----------------------------------------------------------------------------------------------------
NX, AX = 430, 1450
NH_R = hand("NI_ruhig_r", NX, BODEN, FH, +1)       # Ninas Hand (zu Arne hin)
AH_L = hand("AR_ruhig", AX, BODEN, FH, -1)         # Arnes Hand (zu Nina hin)
GIBT = (beim("zahlt", "gibt"), beim("zahlt", "Handy", ende=True))
ZAHLT = (beim("zahlt", "zahlt"), beim("zahlt", "und", ende=True))
folie([(NULL, "Fall · Drei Käufe"), ("handy", "Fall · Das Handy"), ("schwester", "Fall · Das Handy gehört der Schwester")], [
    hart(pl("Nina kauft drei Dinge", 70, 40, NULL, fill=GELB, size=44, bis="handy")),
    pl("Zuerst das Handy", 70, 40, "handy", fill=GELB, size=44),
    hart(boden(NULL)),
    ficon("tabler", "device-mobile", 760, 330, 90, beim("fall", "Handy"), fuell=WEISS, bis="handy"),
    ficon("tabler", "car", 960, 330, 170, beim("fall", "Auto"), fuell=BLAU, bis="handy"),
    ficon("ph", "house", 1170, 330, 150, beim("fall", "Haus"), fuell=GELB, bis="handy"),
    # Nina (links, blickt zu Arne)
    *fig("NI", NX, BODEN, FH, [(NULL, "ruhig_r"), (GIBT[1], "froh_r")], erst="cut"),
    hart(ns("Nina", NX, BODEN, NULL, NI_F)),
    # Arne (rechts, blickt zu Nina)
    *fig("AR", AX, BODEN, FH, [(beim("handy", "Arne"), "ruhig")], bis="ar1"),
    *redet("AR_redet", AX, BODEN, FH, "ar1", "zahlt"),
    *fig("AR", AX, BODEN, FH, [("zahlt", "froh"), ("schwester", "denkt")], erst="cut"),
    ns("Arne", AX, BODEN, beim("handy", "Arne"), AR_F),
    # das Handy: erst in Arnes Hand, dann bei Nina
    ficon("tabler", "device-mobile", AH_L[0] - 10, AH_L[1] + 20, 70, beim("handy", "Arne"), fuell=WEISS, bis=GIBT[0]),
    bewegt(ficon("tabler", "device-mobile", NH_R[0] + 10, NH_R[1] + 20, 70, GIBT[0], fuell=WEISS, anim="cut"),
           *GIBT, (AH_L[0] - 10) - (NH_R[0] + 10), 0),
    pl("150 €", 960, 560, beim("ar1", "hundertfünfzig"), fill=GRUEN, size=32, anker="m", bis="schwester"),
    # das Geld wandert zu Arne
    bewegt(ficon("tabler", "cash-banknote", AH_L[0] - 60, AH_L[1] - 40, 90, ZAHLT[0], fuell=GRUEN, anim="cut"),
           *ZAHLT, (NH_R[0] + 40) - (AH_L[0] - 60), 0),
    blase("sprech", 760, 210, "ar1", 1000, 220, inhalt=["Mein altes Handy. Für 150 €", "gehört es dir."], textsize=34,
          figur=("AR_redet", AX, BODEN, FH), bis="zahlt"),
    pl("Das Handy gehört der Schwester von Arne", 940, 140, "schwester", fill=PINK, size=34, anker="m"),
    pl("nur geliehen", 940, 240, beim("schwester", "geliehen"), fill=WEISS, size=32, anker="m"),
])

# A2 Fall: das Auto ------------------------------------------------------------------------------------------------------
NX2, KX, CX = 380, 1480, 930
NH2 = hand("NI_redet_r", NX2, BODEN, FH, +1)
KH = hand("KU_redet", KX, BODEN, FH, -1)
LOS = (beim("faehrt", "fährt"), beim("faehrt", "los", ende=True))
SCHL = (beim("ku1", "Schlüssel"), beim("ku1", "Schlüssel", ende=True))
ZAHLT2 = (beim("faehrt", "zahlt"), beim("faehrt", "und", ende=True))
folie([("auto", "Fall · Das Auto"), ("schwager", "Fall · Das Auto gehört dem Schwager")], [
    pl("Dann das Auto", 70, 40, "auto", fill=GELB, size=44),
    boden("auto"),
    ficon("tabler", "parking", 1780, 300, 80, beim("auto", "Parkplatz"), fuell=BLAU),
    pl("Parkplatz", 1640, 330, beim("auto", "Parkplatz"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "car", CX, BODEN, 400, "auto", fuell=BLAU, bis=LOS[0]),
    szene(bewegt(ficon("tabler", "car", 330, BODEN, 400, LOS[0], fuell=BLAU, anim="cut"), LOS[0], ("faehrt", T_("schwager") - T_("faehrt")),
                 CX - 330), "076motor*", 0.9, 0.0),
    pl("Gebrauchtwagen: 6.000 €", CX, 420, beim("auto", "sechstausend"), fill=GRUEN, size=32, anker="m", bis="ni1"),
    # Nina
    peep_voll("NI_ruhig_r", NX2, BODEN, FH, "auto", anim="pop", bis="ni1"),
    *redet("NI_redet_r", NX2, BODEN, FH, "ni1", "ku1"),
    peep_voll("NI_ruhig_r", NX2, BODEN, FH, "ku1", anim="cut", bis=LOS[0]),
    ns("Nina", NX2, BODEN, "auto", NI_F, bis=LOS[0]),
    # Herr Kuhnert
    peep_voll("KU_ruhig", KX, BODEN, FH, beim("auto", "Kuhnert"), anim="pop", bis="ku1"),
    *redet("KU_redet", KX, BODEN, FH, "ku1", "faehrt"),
    *fig("KU", KX, BODEN, FH, [("faehrt", "ruhig"), ("schwager", "denkt")], erst="cut"),
    ns("Herr Kuhnert", KX, BODEN, beim("auto", "Kuhnert"), KU_F),
    # Schlüssel und Geld wechseln die Hand
    ficon("tabler", "key", KH[0] - 10, KH[1] + 10, 70, beim("ku1", "Hier"), fuell=GELB, bis=SCHL[0]),
    bewegt(ficon("tabler", "key", NH2[0] + 10, NH2[1] + 10, 70, SCHL[0], fuell=GELB, anim="cut", bis=LOS[0]), *SCHL,
           (KH[0] - 10) - (NH2[0] + 10), 0),
    bewegt(ficon("tabler", "cash-banknote", KH[0] - 50, KH[1] - 40, 90, ZAHLT2[0], fuell=GRUEN, anim="cut"), *ZAHLT2,
           (NH2[0] + 40) - (KH[0] - 50), 0),
    blase("sprech", 640, 170, "ni1", 760, 220, inhalt=["Und wo ist die", "Zulassungsbescheinigung?"], textsize=34,
          figur=("NI_redet_r", NX2, BODEN, FH), bis="ku1"),
    blase("sprech", 760, 210, "ku1", 1100, 220, inhalt=["Die schicke ich Ihnen nächste", "Woche. Hier ist der Schlüssel."],
          textsize=34, figur=("KU_redet", KX, BODEN, FH), bis="faehrt"),
    pl("Das Auto gehört dem Schwager von Herrn Kuhnert", 960, 140, "schwager", fill=PINK, size=34, anker="m"),
    pl("nur geliehen", 960, 240, beim("schwager", "geliehen"), fill=WEISS, size=32, anker="m"),
])

# A3 Fall: das Haus ------------------------------------------------------------------------------------------------------
NX3, LX, MX = 760, 1520, 1140
folie([("haus", "Fall · Das Haus"), ("notar", "Fall · Beim Notar"), ("falsch", "Fall · Das Grundbuch ist falsch")], [
    pl("Zuletzt das Haus", 70, 40, "haus", fill=GELB, size=44),
    boden("haus"),
    ficon("ph", "house", 300, BODEN, 330, "haus", fuell=GELB),
    pl("kleines Haus", 300, 420, beim("haus", "kleines"), fill=WEISS, size=30, anker="m"),
    *fig("NI", NX3, BODEN, FH, [("haus", "ruhig_r")]),
    ns("Nina", NX3, BODEN, "haus", NI_F),
    *fig("LO", LX, BODEN, FH, [(beim("haus", "Lohse"), "ruhig")], bis="lo1"),
    *redet("LO_redet", LX, BODEN, FH, "lo1", "falsch"),
    peep_voll("LO_ruhig", LX, BODEN, FH, "falsch", anim="cut"),
    ns("Frau Lohse", LX, BODEN, beim("haus", "Lohse"), LO_F),
    # beim Notar: Kaufvertrag und Auflassung
    pl("Beim Notar", MX, 100, "notar", fill=WEISS, size=32, anker="m", bis="lo1"),
    szene(ficon("tabler", "writing-sign", MX, 320, 120, beim("notar", "Kaufvertrag"), fuell=WEISS, bis="lo1"), "076stift*", 0.8, 0.0),
    pl("Kaufvertrag", MX, 350, beim("notar", "Kaufvertrag"), fill=GELB, size=30, anker="m", bis="lo1"),
    pl("Auflassung", MX, 440, beim("notar", "Auflassung"), fill=GELB, size=30, anker="m", bis="lo1"),
    # das Grundbuch
    ficon("tabler", "book-2", MX, 520, 110, beim("lo1", "Grundbuch"), fuell=WEISS),
    pl("Grundbuch: Frau Lohse", MX, 540, beim("lo1", "Grundbuch"), fill=WEISS, size=30, anker="m"),
    nein(MX - 200, 572, beim("falsch", "falsch"), gr=22),
    pl("Das Haus gehört noch ihrem Bruder", MX - 50, 640, beim("falsch", "Bruder"), fill=PINK, size=30, anker="m"),
    pl("Nina weiß davon nichts", MX - 50, 730, beim("falsch", "Nina"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 700, 190, "lo1", 1150, 230, inhalt=["Ich stehe im Grundbuch.", "Das Haus gehört mir."], textsize=36,
          figur=("LO_redet", LX, BODEN, FH), bis="falsch"),
])

# A4 Fall: die Frage ------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Die Frage")], [
    pl("Die Frage", 70, 40, "frage", fill=GELB, size=44),
    boden("frage"),
    pl("Wird Nina trotzdem Eigentümerin?", 760, 170, "frage", fill=PINK, size=40, anker="m"),
    ficon("tabler", "device-mobile", 360, 640, 110, "frage", fuell=WEISS),
    ficon("tabler", "car", 760, 640, 300, "frage", fuell=BLAU, d=0.1),
    ficon("ph", "house", 1160, 640, 250, "frage", fuell=GELB, d=0.2),
    pl("Handy?", 360, 680, beim("frage2", "Handy"), fill=WEISS, size=32, anker="m"),
    pl("Auto?", 760, 680, beim("frage2", "Auto"), fill=WEISS, size=32, anker="m"),
    pl("Haus?", 1160, 680, beim("frage2", "Haus"), fill=WEISS, size=32, anker="m"),
    *fig("NI", 1620, BODEN, FH, [("frage", "denkt")]),
    ns("Nina", 1620, BODEN, "frage", NI_F),
])

# B Sachverhalt (eigene Fassung mit 34 px, damit drei Absätze auf die Karte passen) -------------------------------------
def sachverhalt_076(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 200, 85, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 200, y, 1520, cue, size=34, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 200, y + 4, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_076("sv", [
    "Nina kauft ihrem Bekannten Arne für 150 Euro sein altes Handy ab, und Arne übergibt es ihr. Das Handy gehört "
    "aber seiner Schwester, die es ihm nur geliehen hat.",
    "Auf einem Parkplatz kauft Nina von Herrn Kuhnert für 6.000 Euro einen Gebrauchtwagen. Auf ihre Frage nach der "
    "Zulassungsbescheinigung sagt er, er schicke sie nächste Woche. Nina zahlt und fährt los. Das Auto gehört dem "
    "Schwager von Herrn Kuhnert, der es ihm nur geliehen hat.",
    "Frau Lohse verkauft Nina ein kleines Haus. Beim Notar schließen beide den Kaufvertrag und erklären die Auflassung. "
    "Frau Lohse ist im Grundbuch als Eigentümerin eingetragen. Die Übertragung an sie war aber unwirksam, das Haus "
    "gehört noch ihrem Bruder. Nina weiß davon nichts; ein Widerspruch ist nicht eingetragen.",
], "Wird Nina Eigentümerin von Handy, Auto und Haus?")

# C Grundsätze -----------------------------------------------------------------------------------------------------------
folie([("grund", "Grundsätze des Sachenrechts"), ("publ", "Grundsätze › Publizität"), ("spez", "Grundsätze › Spezialität"),
       ("abstr", "Grundsätze › Abstraktion")], rechts_frei([
    *tafel("grund", "Drei Grundsätze des Sachenrechts"),
    z("1. Publizität: Eigentum soll erkennbar sein", 110, 200, "publ", "Bold", 36),
    z("bewegliche Sachen: am Besitz", 160, 260, beim("publ", "beweglichen"), size=34),
    z("Grundstücke: am Grundbuch", 160, 310, beim("publ", "Grundstücken"), size=34),
    z("2. Spezialität: stets eine bestimmte Sache", 110, 400, "spez", "Bold", 36),
    z("3. Abstraktion: Übereignung ist ein eigenes", 110, 490, "abstr", "Bold", 36),
    z("Geschäft, grundsätzlich unabhängig vom Kaufvertrag", 160, 550, beim("abstr", "grundsätzlich"), size=34),
    zit("Mehr dazu in eigenen Videos: Abstraktionsprinzip, Besitz und Eigentum", 110, 650, "mehr", size=28),
    *requisit([("grund", ("tabler", "scale", 130, WEISS), "Sachenrecht", WEISS),
               ("publ", ("tabler", "eye", 120, WEISS), "Publizität", GELB),
               ("spez", ("tabler", "hand-finger", 110, WEISS), "Spezialität", BLAU),
               ("abstr", ("tabler", "link-off", 120, WEISS), "Abstraktion", LILA)]),
    *fig("NI", FX, FB, FR, [("grund", "ruhig"), ("abstr", "denkt")]),
    ns("Nina", FX, FB, "grund", NI_F, d=0.1),
]))

# D § 929 Satz 1 (Wortlaut) -----------------------------------------------------------------------------------------------
W929 = ["„Zur Übertragung des Eigentums an einer beweglichen Sache ist",
        "erforderlich, dass der Eigentümer die Sache dem Erwerber übergibt",
        "und beide darüber einig sind, dass das Eigentum übergehen soll.“"]
w929, w929_y = wortlaut(80, 180, 1100, W929, "§ 929 Satz 1 BGB", "w929", marken=[
    (1, "der Eigentümer", beim("w929", "Eigentümer")), (1, "übergibt", beim("w929", "übergibt")),
    (2, "einig sind", beim("w929", "einig"))], size=32)
folie([("p929", "Bewegliche Sachen · § 929 S. 1 BGB"), ("einig", "§ 929 S. 1 BGB › Einigung"),
       ("ueberg", "§ 929 S. 1 BGB › Übergabe"), ("berecht", "§ 929 S. 1 BGB › Berechtigung")], rechts_frei([
    *tafel("p929", "Das Handy: § 929 Satz 1 BGB"),
    *w929,
    *okz("Einigung: Nina und Arne sind sich einig", w929_y + 50, "einig", "Bold"),
    *okz("Übergabe: Arne übergibt das Handy", w929_y + 120, "ueberg", "Bold"),
    z("übergeben muss der Eigentümer", 185, w929_y + 200, "berecht", size=34),
    *neinz("Berechtigung: Arne ist nicht berechtigt", w929_y + 260, beim("berecht", "Arne"), "Bold"),
    *requisit([("p929", HANDY, "§ 929 S. 1 BGB", GELB), (beim("berecht", "Arne"), HANDY, "nicht berechtigt", ROT)]),
    *paar("p929", "NI", [("p929", "ruhig"), ("berecht", "denkt")], "AR", [("p929", "ruhig"), ("berecht", "denkt")],
          "Nina", NI_F, "Arne", AR_F),
]))

# E Übergabeersatz -----------------------------------------------------------------------------------------------------------
folie([("surr", "Übergabeersatz"), ("s2", "Übergabeersatz › § 929 S. 2 BGB"), ("p930", "Übergabeersatz › § 930 BGB"),
       ("p931", "Übergabeersatz › § 931 BGB")], rechts_frei([
    *tafel("surr", "Wenn die Übergabe ersetzt wird"),
    z("§ 929 Satz 2 BGB: Erwerber hat die Sache schon", 110, 200, "s2", "Bold", 34),
    z("dann genügt die Einigung", 160, 255, beim("s2", "genügt"), size=34),
    z("§ 930 BGB: Veräußerer behält die Sache", 110, 350, "p930", "Bold", 34),
    z("dann genügt ein Besitzmittlungsverhältnis", 160, 405, beim("p930", "genügt"), size=34),
    z("§ 931 BGB: ein Dritter hat die Sache", 110, 500, "p931", "Bold", 34),
    z("dann genügt die Abtretung des", 160, 555, beim("p931", "genügt"), size=34),
    z("Herausgabeanspruchs", 160, 605, beim("p931", "Herausgabeanspruchs"), size=34),
    *requisit([("surr", ("tabler", "arrows-exchange", 130, WEISS), "Übergabeersatz", WEISS),
               ("s2", ("tabler", "hand-finger", 110, WEISS), "§ 929 S. 2 BGB", GELB),
               ("p930", ("tabler", "home", 120, GELB), "§ 930 BGB", BLAU),
               ("p931", ("tabler", "file-text", 110, WEISS), "§ 931 BGB", LILA)]),
    *fig("NI", FX, FB, FR, [("surr", "ruhig")]),
    ns("Nina", FX, FB, "surr", NI_F, d=0.1),
]))

# F § 932 (Wortlaut Abs. 1 Satz 1 und Abs. 2) -------------------------------------------------------------------------------
W932 = ["„(1) Durch eine nach § 929 erfolgte Veräußerung wird der Erwerber",
        "auch dann Eigentümer, wenn die Sache nicht dem Veräußerer gehört,",
        "es sei denn, dass er zu der Zeit, zu der er nach diesen Vorschriften",
        "das Eigentum erwerben würde, nicht in gutem Glauben ist. …",
        "(2) Der Erwerber ist nicht in gutem Glauben, wenn ihm bekannt oder",
        "infolge grober Fahrlässigkeit unbekannt ist, dass die Sache nicht",
        "dem Veräußerer gehört.“"]
w932, w932_y = wortlaut(80, 170, 1100, W932, "§ 932 Abs. 1 Satz 1, Abs. 2 BGB", "p932", marken=[
    (1, "auch dann Eigentümer", beim("w932", "auch")), (1, "nicht dem Veräußerer gehört", beim("w932", "nicht")),
    (3, "nicht in gutem Glauben", beim("w932", "gutem")), (4, "bekannt", beim("w932b", "Kenntnis")),
    (5, "infolge grober Fahrlässigkeit unbekannt", beim("w932b", "grobe"))], size=30)
folie([("p932", "Gutgläubiger Erwerb · § 932 Abs. 1 S. 1 BGB"), ("w932b", "Gutgläubiger Erwerb › guter Glaube, § 932 Abs. 2 BGB")],
      rechts_frei([
    *tafel("p932", "Hilft der gute Glaube?"),
    *w932,
    *requisit([("p932", ("tabler", "shield-check", 120, GRUEN), "guter Glaube?", GELB),
               ("w932b", ("tabler", "eye-off", 120, WEISS), "Kenntnis, grobe Fahrlässigkeit", ROT)]),
    *paar("p932", "NI", [("p932", "denkt")], "AR", [("p932", "ruhig")], "Nina", NI_F, "Arne", AR_F),
]))

# G Rechtsschein des Besitzes -------------------------------------------------------------------------------------------------
folie([("schein", "Gutgläubiger Erwerb › Rechtsschein des Besitzes"), ("nina1", "Gutgläubiger Erwerb › guter Glaube von Nina")],
      rechts_frei([
    *tafel("schein", "Das Handy: guter Glaube?"),
    z("Grundlage: der Rechtsschein des Besitzes", 110, 200, "schein", "Bold", 36),
    z("§ 1006 Abs. 1 BGB: Für den Besitzer wird vermutet,", 110, 270, beim("schein", "Für"), size=34),
    z("dass er Eigentümer ist", 160, 320, beim("schein", "Eigentümer"), size=34),
    zit("vgl. BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 160, 375, beim("schein", "Paragraf")),
    *okz("Arne hatte das Handy", 450, "nina1", size=34),
    *okz("Nina hatte keinen Grund zu zweifeln", 510, beim("nina1", "keinen"), size=34),
    blk(110, 600, 1040, 90, GRUEN, "nina2", [("Nina ist in gutem Glauben", "ExtraBold", 38, INK)]),
    *requisit([("schein", HANDY, "Besitz", BLAU), ("nina2", ("tabler", "shield-check", 120, GRUEN), "gutgläubig", GRUEN)]),
    *paar("schein", "NI", [("schein", "ruhig"), ("nina2", "froh")], "AR", [("schein", "ruhig")], "Nina", NI_F, "Arne", AR_F),
]))

# H § 935 ------------------------------------------------------------------------------------------------------------------
folie([("p935", "Ausschluss · § 935 BGB"), ("freiw", "§ 935 BGB › abhandengekommen?"), ("nina4", "Ergebnis · Handy")], rechts_frei([
    *tafel("p935", "Und wenn das Handy gestohlen wäre?"),
    z("§ 935 Abs. 1 BGB: kein gutgläubiger Erwerb,", 110, 200, beim("p935", "Nach"), "Bold", 34),
    z("wenn die Sache abhandengekommen ist", 160, 255, beim("p935", "abhandengekommen"), size=34),
    z("Ausnahme, § 935 Abs. 2 BGB: etwa Geld", 160, 320, "geld", size=32, farbe=TEXT),
    z("abhandengekommen = Besitz unfreiwillig verloren", 110, 410, "freiw", "Bold", 34),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 160, 465, beim("freiw", "unfreiwillig")),
    *okz("Die Schwester hat das Handy freiwillig verliehen", 530, beim("freiw", "Die"), size=34),
    blk(110, 630, 1040, 90, GRUEN, "nina4", [("Nina wird Eigentümerin des Handys", "ExtraBold", 38, INK)]),
    *requisit([("p935", ("tabler", "lock-open", 110, ROT), "gestohlen?", ROT),
               (beim("freiw", "Die"), HANDY, "freiwillig verliehen", GELB), ("nina4", HANDY, "gehört Nina", GRUEN)]),
    *paar("p935", "NI", [("p935", "denkt"), ("nina4", "zufrieden")], "AR", [("p935", "ruhig")], "Nina", NI_F, "Arne", AR_F),
]))

# I Auto ----------------------------------------------------------------------------------------------------------------------
folie([("auto2", "Das Auto · § 929 S. 1, § 932 BGB"), ("zb2", "Das Auto › guter Glaube beim Gebrauchtwagen"),
       ("grob", "Das Auto › grob fahrlässig, § 932 Abs. 2 BGB"), ("auto4", "Ergebnis · Auto")], rechts_frei([
    *tafel("auto2", "Das Auto: guter Glaube?"),
    *okz("Einigung und Übergabe", 185, "auto3", size=34),
    *neinz("Herr Kuhnert ist nicht Eigentümer", 240, beim("auto3", "aber"), size=34),
    *okz("nicht abhandengekommen: freiwillig verliehen", 295, "nabh", size=34),
    z("Gebrauchtwagen: Besitz allein reicht nicht", 110, 380, "zb2", "Bold", 34),
    z("regelmäßig mindestens: Zulassungsbescheinigung", 160, 435, "zb3", size=32),
    z("Teil II zeigen lassen, Berechtigung prüfen", 160, 480, beim("zb3", "Teil"), size=32),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 29;", 160, 530, beim("zb3", "Zulassungsbescheinigung")),
    zit("BGH, Urt. v. 1.3.2013 – V ZR 92/12, Rn. 13 f.", 160, 565, beim("zb3", "Zulassungsbescheinigung")),
    *neinz("Nina hat verzichtet: grob fahrlässig", 625, "grob", "Bold", 36),
    blk(110, 710, 1040, 90, HELLROT, "auto4", [("Nina wird nicht Eigentümerin", "ExtraBold", 38, INK)]),
    *requisit([("auto2", AUTO, "Gebrauchtwagen", BLAU),
               ("zb3", ("tabler", "file-certificate", 110, WEISS), "Zulassungsbescheinigung Teil II", WEISS),
               ("grob", ("tabler", "file-x", 110, ROT), "nicht geprüft", ROT), ("auto4", AUTO, "gehört dem Schwager", PINK)]),
    *paar("auto2", "NI", [("auto2", "ruhig"), ("grob", "sorge")], "KU", [("auto2", "ruhig"), ("zb3", "ernst")],
          "Nina", NI_F, "Herr Kuhnert", KU_F),
]))

# J Haus: § 873 Abs. 1 (Wortlaut), § 925 -----------------------------------------------------------------------------------------
W873 = ["„Zur Übertragung des Eigentums an einem Grundstück … ist die",
        "Einigung des Berechtigten und des anderen Teils über den Eintritt",
        "der Rechtsänderung und die Eintragung der Rechtsänderung in das",
        "Grundbuch erforderlich, soweit nicht das Gesetz ein anderes vorschreibt.“"]
w873, w873_y = wortlaut(80, 180, 1100, W873, "§ 873 Abs. 1 BGB", "w873", marken=[
    (1, "Einigung", beim("w873", "Einigung")), (1, "des Berechtigten", beim("w873", "Berechtigten")),
    (2, "die Eintragung der Rechtsänderung in das", beim("w873", "Eintragung")), (3, "Grundbuch", beim("w873", "Eintragung"))],
    size=30)
folie([("p873", "Grundstücke · § 873 Abs. 1 BGB"), ("p925", "Grundstücke › Auflassung, § 925 BGB"),
       ("eintr", "Grundstücke › Eintragung")], rechts_frei([
    *tafel("p873", "Das Haus: das Grundstück"),
    *w873,
    z("Einigung = Auflassung, § 925 Abs. 1 BGB", 110, w873_y + 50, "p925", "Bold", 34),
    z("bei gleichzeitiger Anwesenheit beider", 160, w873_y + 105, beim("p925", "bei"), size=34),
    z("vor einer zuständigen Stelle, etwa einem Notar", 160, w873_y + 155, beim("p925", "zuständigen"), size=34),
    blk(110, w873_y + 230, 1040, 90, BLAU, "eintr", [("Eigentum erst mit der Eintragung", "ExtraBold", 38, INK)]),
    *requisit([("p873", HAUS, "Haus = Grundstück", GELB), ("p925", ("tabler", "writing-sign", 120, WEISS), "Auflassung", GELB),
               ("eintr", BUCH, "Eintragung im Grundbuch", BLAU)]),
    *paar("p873", "NI", [("p873", "ruhig")], "LO", [("p873", "ruhig")], "Nina", NI_F, "Frau Lohse", LO_F),
]))

# K Haus: § 892, Widerspruch, Vormerkung ---------------------------------------------------------------------------------------
folie([("p892", "Grundstücke › öffentlicher Glaube, § 892 BGB"), ("kennt", "§ 892 BGB › nur Kenntnis schadet"),
       ("nina3", "Ergebnis · Haus"), ("wid", "§ 892 BGB › Widerspruch"), ("vorm", "Ausblick · Vormerkung, § 883 BGB")], rechts_frei([
    *tafel("p892", "Frau Lohse ist nicht berechtigt"),
    z("§ 892 Abs. 1 Satz 1 BGB: Für den Erwerber gilt", 110, 185, "w892", "Bold", 34),
    z("der Inhalt des Grundbuchs als richtig, es sei denn,", 160, 235, beim("w892", "Inhalt"), size=32),
    z("ein Widerspruch ist eingetragen oder", 160, 280, beim("w892", "Widerspruch"), size=32),
    z("ihm ist die Unrichtigkeit bekannt", 160, 325, beim("w892", "Unrichtigkeit"), size=32),
    z("Es schadet nur Kenntnis, nicht grobe Fahrlässigkeit", 110, 395, "kennt", "Bold", 34),
    *okz("Nina weiß nichts, und ein Widerspruch fehlt", 460, "nina3", size=34),
    blk(110, 530, 1040, 90, GRUEN, beim("nina3", "Mit"), [("Mit der Eintragung: Nina ist Eigentümerin", "ExtraBold", 36, INK)]),
    *neinz("Widerspruch vorher eingetragen: Erwerb gescheitert", 655, "wid", size=32),
    z("Vormerkung, § 883 BGB: schützt den Anspruch eines", 110, 735, "vorm", "Bold", 32),
    z("Käufers bis zur Eintragung gegen spätere Verfügungen", 160, 780, beim("vorm", "Käufers"), size=32),
    *requisit([("p892", BUCH, "öffentlicher Glaube", BLAU), ("kennt", ("tabler", "eye", 120, WEISS), "nur Kenntnis", ROT),
               (beim("nina3", "Mit"), HAUS, "gehört Nina", GRUEN), ("wid", ("tabler", "ban", 110, ROT), "Widerspruch", ROT),
               ("vorm", ("tabler", "bookmark", 100, GELB), "Vormerkung", GELB)]),
    *paar("p892", "NI", [("p892", "denkt"), (beim("nina3", "Mit"), "zufrieden")], "LO", [("p892", "ruhig"), ("kennt", "sorge")],
          "Nina", NI_F, "Frau Lohse", LO_F),
]))

# L Vergleichstabelle (progressiv, breite Karte) ---------------------------------------------------------------------------------
C0, C1, C2, CE = 110, 560, 1210, 1830
RY = [300, 430, 560, 700]
folie([("vgl", "Vergleich · bewegliche Sache und Grundstück")], [
    karte(60, 50, 1800, 900, "vgl"),
    titel(glyphen("Vergleich: bewegliche Sache und Grundstück"), 110, 80, "vgl", 44),
    z("bewegliche Sache", C1, 200, "vgl", "ExtraBold", 36, rechts=CE),
    z("Grundstück", C2, 200, "vgl", "ExtraBold", 36, rechts=CE),
    linienzug([(C0, 260), (CE, 260)], "vgl", breite=5),
    linienzug([(C1 - 30, 190), (C1 - 30, 830)], "vgl", breite=4),
    linienzug([(C2 - 30, 190), (C2 - 30, 830)], "vgl", breite=4),
    # 1. Übertragung
    z("Übertragung", C0, RY[0], "v1", "Bold", 34, rechts=C1 - 40),
    z("Einigung und Übergabe", C1, RY[0], "v1", size=32, rechts=C2 - 40),
    z("§ 929 Satz 1 BGB", C1, RY[0] + 45, "v1", size=28, farbe=TEXT, rechts=C2 - 40),
    z("Auflassung und Eintragung", C2, RY[0], beim("v1", "Grundstücke"), size=32, rechts=CE),
    z("§§ 873 Abs. 1, 925 BGB", C2, RY[0] + 45, beim("v1", "Grundstücke"), size=28, farbe=TEXT, rechts=CE),
    linienzug([(C0, RY[1] - 25), (CE, RY[1] - 25)], beim("v2", "Den"), breite=3),
    # 2. Rechtsschein
    z("Rechtsschein", C0, RY[1], "v2", "Bold", 34, rechts=C1 - 40),
    z("Besitz", C1, RY[1], beim("v2", "Besitz"), size=32, rechts=C2 - 40),
    z("§ 1006 BGB", C1, RY[1] + 45, beim("v2", "Besitz"), size=28, farbe=TEXT, rechts=C2 - 40),
    z("Grundbuch", C2, RY[1], beim("v2", "Grundbuch"), size=32, rechts=CE),
    z("§ 892 BGB", C2, RY[1] + 45, beim("v2", "Grundbuch"), size=28, farbe=TEXT, rechts=CE),
    linienzug([(C0, RY[2] - 25), (CE, RY[2] - 25)], "v3", breite=3),
    # 3. Was schadet
    z("Was schadet?", C0, RY[2], "v3", "Bold", 34, rechts=C1 - 40),
    z("Kenntnis und grobe Fahrlässigkeit", C1, RY[2], beim("v3", "Kenntnis"), size=32, rechts=C2 - 40),
    z("§ 932 Abs. 2 BGB", C1, RY[2] + 45, beim("v3", "Kenntnis"), size=28, farbe=TEXT, rechts=C2 - 40),
    z("nur Kenntnis", C2, RY[2], beim("v3", "beim"), size=32, rechts=CE),
    z("§ 892 Abs. 1 Satz 1 BGB", C2, RY[2] + 45, beim("v3", "beim"), size=28, farbe=TEXT, rechts=CE),
    linienzug([(C0, RY[3] - 25), (CE, RY[3] - 25)], "v4", breite=3),
    # 4. Abhandenkommen
    z("abhandengekommen", C0, RY[3], "v4", "Bold", 34, rechts=C1 - 40),
    z("kein gutgläubiger Erwerb", C1, RY[3], beim("v4", "Sperre"), size=32, rechts=C2 - 40),
    z("§ 935 Abs. 1 BGB", C1, RY[3] + 45, beim("v4", "Sperre"), size=28, farbe=TEXT, rechts=C2 - 40),
    z("keine solche Sperre", C2, RY[3], beim("v4", "nur"), size=32, rechts=CE),
])

# M Ergebnis ---------------------------------------------------------------------------------------------------------------
EX = (260, 760, 1260)
folie([("erg", "Ergebnis")], [
    pl("Ergebnis", 70, 40, "erg", fill=GELB, size=44),
    boden("erg"),
    ficon("tabler", "device-mobile", EX[0], 560, 110, "e1", fuell=WEISS),
    pl("Handy: gehört Nina", EX[0], 600, "e1", fill=GRUEN, size=30, anker="m"),
    ok(EX[0], 280, beim("e1", "gehört"), gr=34),
    ficon("tabler", "car", EX[1], 560, 290, "e2", fuell=BLAU),
    pl("Auto: bleibt beim Schwager", EX[1], 600, "e2", fill=HELLROT, size=30, anker="m"),
    nein(EX[1], 280, beim("e2", "bleibt"), gr=34),
    ficon("ph", "house", EX[2], 560, 240, "e3", fuell=GELB),
    pl("Haus: Nina mit Eintragung", EX[2], 600, "e3", fill=GRUEN, size=30, anker="m"),
    ok(EX[2], 280, beim("e3", "Eintragung"), gr=34),
    *fig("NI", 1680, BODEN, FH, [("erg", "ruhig"), ("e1", "froh"), ("e2", "sorge"), ("e3", "zufrieden")]),
    ns("Nina", 1680, BODEN, "erg", NI_F),
])

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Erwerb vom Nichtberechtigten"), ("tipp2", "Klausurtipp · Grundstück: nur Kenntnis")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Erwerb vom Nichtberechtigten:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("in dieser Reihenfolge", 200, 255, beim("tipp", "Reihenfolge"), size=34),
    z("1. § 929 BGB", 230, 320, beim("tipp", "neunhundertneunundzwanzig"), "Bold", 34),
    z("2. § 932 BGB", 230, 375, beim("tipp", "neunhundertzweiunddreißig"), "Bold", 34),
    z("3. § 935 BGB", 230, 430, beim("tipp", "neunhundertfünfunddreißig"), "Bold", 34),
    *neinz("Beim Grundstück nicht „grob fahrlässig“ schreiben", 540, "tipp2", "Bold", 34),
    z("Bei § 892 BGB zählt nur die Kenntnis.", 185, 600, beim("tipp2", "Bei"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k5", "Klausurschema › Grundstück")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Eigentumserwerb, §§ 929 ff. BGB"), 110, 90, "sch", 44),
    z("I. Einigung", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("II. Übergabe oder Übergabeersatz (§§ 929 S. 2, 930, 931 BGB)", K1, 270, "k2", "Bold", 38, rechts=1820),
    z("III. Berechtigung des Veräußerers", K1, 340, "k3", "Bold", 38, rechts=1820),
    z("IV. Fehlt sie: gutgläubiger Erwerb, §§ 932 ff. BGB", K1, 410, "k4", "Bold", 38, rechts=1820),
    z("ohne Abhandenkommen, § 935 BGB", K2, 470, "k4b", size=36, rechts=1820),
    blk(K1, 580, 1600, 150, BLAU, "k5", [("Grundstück: Auflassung (§ 925 BGB), Eintragung (§ 873 Abs. 1 BGB),", "Bold", 34, INK),
                                         ("Berechtigung oder öffentlicher Glaube des Grundbuchs (§ 892 BGB)", "Bold", 34, INK)]),
])

# P Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Bei beweglichen Sachen trägt ", 0), ("der Besitz", "a")],
                 [("den guten Glauben,", 0)], [("bei Grundstücken ", 0), ("das Grundbuch.", "b")]],
                750, 300, 42, "merke", {"a": beim("merke", "Besitz"), "b": beim("merke", "Grundbuch")}),
    *markertext([[("Beim Grundbuch schadet nur", 0)], [("Kenntnis", "c"), (" oder ein ", 0), ("Widerspruch.", "d")]],
                750, 580, 42, "m2", {"c": beim("m2", "Kenntnis"), "d": beim("m2", "Widerspruch")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
