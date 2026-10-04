"""Folge 161 · Abhandenkommen § 935 BGB: Gestohlen oder verliehen? – Serienstandard Open Peeps (Katzenkönig).
Zwei Parallelfälle mit gleicher Bildstruktur (links Hella, Mitte der Veräußerer, rechts Berta am Flohmarktstand):
Fall A: Hella leiht Knut ihre Kamera bis Montag; Knut verkauft sie auf dem Flohmarkt als seine für 300 € an Berta.
Fall B: Hella legt die Kamera im Park auf eine Bank; ein Dieb nimmt sie weg und verkauft sie dort ebenfalls für 300 € an Berta.
Szenen laut ../SZENENPLAN.md: A Fall A, B Fall B, C Frage (zwei Karten), D Sachverhalt, E Einordnung und Wortlautkarte
§ 935 Abs. 1 S. 1, F 1. Begriff (BGH-Zitatkarte), G Täuschung, H 2. mittelbarer Besitz (Wortlautkarte S. 2), I Knut
entscheidet, J 3. Besitzdiener (Wortlautkarte § 855), K Gedankenfall Fotoladen, L Probefahrt, M 4. Ausnahmen (Wortlautkarte
Abs. 2), N 5. Wertung (BGH-Zitatkarte), O 6. Lösung (zwei Karten), P Klausurtipp (Lexi), Q Prüfschema, R Merksatz (Lexi).
DARSTELLUNG: Der Dieb ist eine unauffällige Alltagsfigur (keine Kapuze, keine Maske, ruhige Mimik); die Wegnahme wird nur als
Wechsel der Kamera von der Bank zum Dieb gezeigt, keine Gewalt. Zwei Handlungsgeräusche (Geldscheine bei den Zahlungen;
../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist (wandert beim Gehen mit). Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/
redet/fig/ns/okz/neinz als eigene Kopie aus Folge 158 (gemeinsame Dateien unverändert); neu: kamera(), stand(), mini_fall(),
zweikarten().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_161/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_161/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch für Wortlautkarten (Wortlaut bleibt unverändert)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur] if cur else zeilen


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149) ------------------------------------
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



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HE": "Hella", "KN": "Knut", "BT": "Berta", "DI": "Dieb"}
HELLGRAU2 = (214, 218, 224, 255)
NFARBE = {"HE": LILA, "KN": ORANGE, "BT": GELB, "DI": HELLGRAU2}


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), bis_(ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1), bis)]


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


def zwei(a, folge_a, b, folge_b):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(a, X1, folge_a), *stehend(b, X2, folge_b)]


def kamera(cx, unten, cue, bis=None, breite=84, anim="pop"):
    """Die Kamera (Tabler „camera“, neutral, ohne Marke), Füllung Hellgrau."""
    return ficon("tabler", "camera", cx, unten, breite, cue, fuell=HELLGRAU2, bis=bis, anim=anim)


def geld(cx, unten, cue, bis=None):
    return ficon("tabler", "cash-banknote", cx, unten, 84, cue, fuell=GRUEN, bis=bis)


# ===========================================================================================================================
# A/B Fallszenen: gleiche Bildstruktur (links Hella, Mitte Veräußerer, rechts Berta am Flohmarktstand)
# ===========================================================================================================================
BODEN, FH = 880, 470
HX, MX0, MX1, BX = 330, 760, 1170, 1600       # Hella, Veräußerer (bei Hella / am Stand), Berta
HAND = BODEN - 205                           # Unterkante der Kamera in Handhöhe
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def stand(c, h=lambda e: e):
    """Flohmarktstand: Tisch aus Grundformen, darauf ein Korb (Phosphor „basket“), Markise als Tabler „building-store“."""
    return [h(ficon("tabler", "building-store", 1385, 520, 230, c, fuell=GELB, anim="cut")),
            h(karte(1300, 700, 170, 34, c, fill=HOLZ, rund=6, schatten=4, rand=4)),
            h(linienzug([(1318, 738), (1318, BODEN)], c, breite=7)), h(linienzug([(1452, 738), (1452, BODEN)], c, breite=7)),
            h(ficon("ph", "basket", 1385, 700, 90, c, fuell=WEISS, anim="cut")),
            h(pl("Flohmarkt", 1385, 240, c, fill=WEISS, size=28, anker="m", anim="cut"))]


# --- A Fall A: verliehen ---------------------------------------------------------------------------------------------------
_h = lambda e: hart(e)
KN_GEHT, KN_DA = "flohm", beim("flohm", "Flohmarkt")
folie([(NULL, "Fall A · verliehen"), ("knapp", "Fall A · Knut braucht Geld"), ("flohm", "Fall A · auf dem Flohmarkt"),
       ("berta", "Fall A · Zahlung und Übergabe")], [
    _h(boden(BODEN, NULL)),
    _h(ficon("tabler", "home", 140, BODEN, 200, NULL, fuell=LILA, anim="cut")),
    *stand(NULL, _h),
    _h(pl("Fall A: verliehen", 70, 30, NULL, fill=GRUEN, size=38)),
    # Hella vor ihrem Haus, blickt nach rechts zu Knut
    *fig("HE", HX, BODEN, FH, [(NULL, "ruhig_r")], bis="h1"),
    _h(ns("Hella", HX, BODEN, NULL, LILA)),
    pl("Hella besitzt eine Kamera", 70, 110, beim("hella", "Kamera"), fill=WEISS, size=34, bis="knapp"),
    bis_(kamera(HX + 120, HAND, beim("hella", "Kamera")), beim("leih", "leiht")),
    # Knut kommt dazu, blickt nach links zu Hella
    *fig("KN", MX0, BODEN, FH, [(beim("leih", "Knut"), "froh"), ("knapp", "sorge")], bis=KN_GEHT),
    bis_(ns("Knut", MX0, BODEN, beim("leih", "Knut"), ORANGE, d=0.1), KN_GEHT),
    bewegt(bis_(kamera(MX0 - 125, HAND, beim("leih", "leiht"), anim="cut"), KN_GEHT), beim("leih", "leiht"),
           beim("leih", "ihm"), HX + 120 - (MX0 - 125), 0),
    pl("Leihe bis Montag", 70, 190, beim("leih", "leiht"), fill=GRUEN, size=34, bis="knapp"),
    ficon("tabler", "calendar-event", 470, 252, 60, beim("leih", "Montag"), fuell=WEISS, bis="knapp"),
    *redet("HE_redet_r", HX, BODEN, FH, "h1", "knapp"),
    blase("sprech", 600, 210, "h1", 760, 300, inhalt=["Hier, bring sie mir", "am Montag zurück."], textsize=38,
          figur=("HE_redet_r", HX, BODEN, FH), bis="knapp"),
    *fig("HE", HX, BODEN, FH, [("knapp", "ruhig_r")], erst="cut"),
    pl("Knut braucht Geld", 70, 110, "knapp", fill=HELLROT, size=34, bis=KN_GEHT),
    ficon("tabler", "wallet", 485, 172, 60, beim("knapp", "Geld"), fuell=HELLROT, bis=KN_GEHT),
    # Knut geht mit der Kamera zum Stand, blickt nach rechts zu Berta
    bewegt(peep_voll("KN_ruhig_r", MX1, BODEN, FH, KN_GEHT, anim="cut", bis="k1"), KN_GEHT, KN_DA, MX0 - MX1, 0),
    bis_(bewegt(ns("Knut", MX1, BODEN, KN_GEHT, ORANGE, anim="cut"), KN_GEHT, KN_DA, MX0 - MX1, 0), None),
    bewegt(bis_(kamera(MX1 + 120, HAND, KN_GEHT, anim="cut"), beim("berta", "übergibt")), KN_GEHT, KN_DA, MX0 - MX1, 0),
    *fig("BT", BX, BODEN, FH, [(KN_DA, "ruhig")], bis="glaub"),
    ns("Berta", BX, BODEN, KN_DA, GELB, d=0.1),
    pl("gibt sie als seine eigene aus", 70, 110, beim("flohm", "gibt"), fill=HELLROT, size=34, bis="berta"),
    *redet("KN_redet_r", MX1, BODEN, FH, "k1", "berta"),
    blase("sprech", 640, 210, "k1", 1440, 250, inhalt=["Die Kamera gehört mir.", "Für 300 € ist sie deine."], textsize=38,
          figur=("KN_redet_r", MX1, BODEN, FH), bis="berta"),
    *fig("KN", MX1, BODEN, FH, [("berta", "ruhig_r")], erst="cut"),
    # Zahlung: Geldschein wandert von Berta zu Knut; Übergabe: Kamera wandert zu Berta
    szene(bewegt(geld(MX1 + 130, HAND - 70, "berta"), "berta", beim("berta", "Knut"), BX - 120 - (MX1 + 130), 0),
          "161geld*", 0.8, 0.1),
    bewegt(kamera(BX - 125, HAND, beim("berta", "übergibt"), anim="cut"), beim("berta", "übergibt"), beim("berta", "Kamera"),
           MX1 + 120 - (BX - 125), 0),
    pl("300 € bezahlt, Kamera übergeben", 70, 110, "berta", fill=WEISS, size=34),
    *fig("BT", BX, BODEN, FH, [("glaub", "froh")], erst="cut"),
    pl("Berta: kein Grund zu zweifeln", 70, 190, "glaub", fill=GELB, size=34),
])

# --- B Fall B: gestohlen ---------------------------------------------------------------------------------------------------
BANK_X = 600
DI_DA, DI_GEHT, DI_STAND = beim("dieb", "Dieb"), "verk", beim("verk", "demselben")
folie([("fallb", "Fall B · gestohlen"), ("dieb", "Fall B · der Dieb"), ("verk", "Fall B · auf dem Flohmarkt")], [
    boden(BODEN, "fallb"),
    ficon("ph", "tree", 140, BODEN, 220, "fallb", fuell=GRUEN, anim="cut"),
    bis_(bank(BANK_X - 120, BODEN, "fallb", breite=240), None),
    *stand("fallb", hart),
    hart(pl("Fall B: gestohlen", 70, 30, "fallb", fill=ROT, size=38)),
    *fig("HE", HX, BODEN, FH, [("fallb", "ruhig_r"), (DI_DA, "ruhig")], bis="glaub2", erst="cut"),
    hart(ns("Hella", HX, BODEN, "fallb", LILA)),
    pl("im Park: Kamera neben sich auf der Bank", 70, 110, "bank", fill=WEISS, size=34, bis="dieb"),
    bis_(kamera(BANK_X, BODEN - 118, beim("bank", "Bank")), beim("dieb", "nimmt")),
    # der Dieb: unauffällige Alltagsfigur, ruhige Mimik
    *fig("DI", BANK_X + 230, BODEN, FH, [(DI_DA, "ruhig")], bis=DI_GEHT),
    bis_(ns("Dieb", BANK_X + 230, BODEN, DI_DA, HELLGRAU2, d=0.1), DI_GEHT),
    bewegt(bis_(kamera(BANK_X + 110, HAND, beim("dieb", "nimmt"), anim="cut"), DI_GEHT), beim("dieb", "nimmt"),
           beim("dieb", "unbemerkt"), -110, 205 - 118),
    pl("ein Dieb nimmt sie unbemerkt weg", 70, 110, beim("dieb", "nimmt"), fill=HELLROT, size=34, bis="verk"),
    *fig("HE", HX, BODEN, FH, [("glaub2", "sorge_r")], erst="cut"),
    bewegt(peep_voll("DI_ruhig_r", MX1, BODEN, FH, DI_GEHT, anim="cut"), DI_GEHT, DI_STAND, BANK_X + 230 - MX1, 0),
    bewegt(ns("Dieb", MX1, BODEN, DI_GEHT, HELLGRAU2, anim="cut"), DI_GEHT, DI_STAND, BANK_X + 230 - MX1, 0),
    bewegt(bis_(kamera(MX1 + 115, HAND, DI_GEHT, anim="cut"), beim("verk", "wieder")), DI_GEHT, DI_STAND,
           BANK_X + 230 - MX1, 0),
    *fig("BT", BX, BODEN, FH, [(DI_STAND, "ruhig"), ("glaub2", "froh")]),
    ns("Berta", BX, BODEN, DI_STAND, GELB, d=0.1),
    pl("verkauft sie an Berta", 70, 110, "verk", fill=HELLROT, size=34),
    szene(bewegt(geld(MX1 + 130, HAND - 70, beim("verk", "wieder")), beim("verk", "wieder"), beim("verk", "Euro"),
                 BX - 120 - (MX1 + 130), 0), "161scheine*", 0.8, 0.1),
    bewegt(kamera(BX - 125, HAND, beim("verk", "wieder"), anim="cut"), beim("verk", "wieder"), beim("verk", "Euro"),
           MX1 + 115 - (BX - 125), 0),
    pl("wieder 300 €", 70, 190, beim("verk", "wieder"), fill=WEISS, size=34),
    pl("Berta: kein Grund zu zweifeln", 70, 270, "glaub2", fill=GELB, size=34),
])

# --- C Frage: zwei Karten mit gleicher Bildstruktur ------------------------------------------------------------------------
MH = 250                                     # Höhe der kleinen Figuren


def mini_fall(x0, cue, titel_, fill, mitte, mitte_txt, pfeil_txt):
    els = [karte(x0, 130, 860, 620, cue, fill=fill, rund=22, schatten=8, rand=5),
           z(titel_, x0 + 30, 150, cue, "ExtraBold", 40, rechts=x0 + 850)]
    for i, (k, name) in enumerate((("HE", "HE_ruhig_r"), (mitte, f"{mitte}_ruhig_r"), ("BT", "BT_froh"))):
        cx = x0 + 130 + i * 300
        els += [peep_voll(name, cx, 620, MH, cue, anim="cut"), ns(NAME[k], cx, 620, cue, NFARBE[k])]
    els += [pfeil(x0 + 200, 470, x0 + 360, 470, cue, breite=8, kopf=24), pfeil(x0 + 500, 470, x0 + 660, 470, cue, breite=8, kopf=24),
            kamera(x0 + 280, 455, cue, breite=60), kamera(x0 + 580, 455, cue, breite=60),
            z(pfeil_txt, x0 + 30, 220, cue, "Bold", 32, rechts=x0 + 850)]
    return els


folie([("frage", "Die Frage · Zweimal derselbe Kauf"), ("frage2", "Die Frage · Wird Berta Eigentümerin?")], [
    *mini_fall(60, "frage", "Fall A: verliehen", HELLGRUEN, "KN", "Knut", "Hella leiht, Knut verkauft"),
    *mini_fall(1000, "frage", "Fall B: gestohlen", HELLROT, "DI", "Dieb", "der Dieb nimmt und verkauft"),
    pl("zweimal derselbe gutgläubige Kauf", 960, 800, "frage", fill=WEISS, size=36, anker="m"),
    pl("Wird Berta jedes Mal Eigentümerin?", 960, 900, "frage2", fill=PINK, size=40, anker="m"),
])

# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
def sachverhalt_161(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_161("sv", [
    "Fall A: Hella leiht ihre Kamera ihrem Freund Knut bis Montag. Knut braucht Geld. Auf dem Flohmarkt gibt er die Kamera "
    "als seine eigene aus und verkauft sie für 300 € an Berta. Berta zahlt, Knut übergibt ihr die Kamera, beide sind sich "
    "über den Eigentumsübergang einig. Berta hat keinen Grund zu zweifeln.",
    "Fall B: Hella legt die Kamera im Park neben sich auf eine Bank. Ein Dieb nimmt sie unbemerkt weg und verkauft sie auf "
    "demselben Flohmarkt als seine eigene für 300 € an Berta, die auch diesmal keinen Grund zu zweifeln hat.",
    "Hella hat keinem der Verkäufe zugestimmt.",
], "Ist Berta jeweils Eigentümerin geworden?")

# ===========================================================================================================================
# E Einordnung: gutgläubiger Erwerb, Wortlautkarte § 935 Abs. 1 S. 1 BGB
# ===========================================================================================================================
W1 = umbruch("„Der Erwerb des Eigentums auf Grund der §§ 932 bis 934 tritt nicht ein, wenn die Sache dem Eigentümer "
             "gestohlen worden, verloren gegangen oder sonst abhanden gekommen war.“", 32, 1040)
_zi = lambda zl, wort: next(i for i, t in enumerate(zl) if wort in t)
w1, w1_y = wortlaut(80, 420, 1100, W1, "§ 935 Abs. 1 S. 1 BGB", "w1", marken=[
    (_zi(W1, "tritt nicht ein"), "tritt nicht ein", beim("w1", "tritt")),
    (_zi(W1, "gestohlen"), "gestohlen", beim("w1b", "gestohlen")),
    (_zi(W1, "verloren"), "verloren", beim("w1b", "verloren")),
    (_zi(W1, "abhanden"), "abhanden", beim("w1b", "abhanden"))], size=32)
folie([("nb", "Einordnung · Verkauf durch Nichtberechtigte"), ("p932", "Einordnung · gutgläubiger Erwerb, §§ 929 S. 1, 932 BGB"),
       ("gg", "Einordnung · Berta gutgläubig"), ("w1", "Die Weiche · § 935 Abs. 1 S. 1 BGB")], rechts_frei([
    *tafel("nb", "Die Weiche: § 935 BGB"),
    *neinz("Die Kamera gehört nicht dem Verkäufer", 180, beim("nb", "nicht"), "Bold", 34, x=160),
    z("Erwerb nur gutgläubig: §§ 929 S. 1, 932 BGB", 160, 245, "p932", "Bold", 34),
    z("Schema: Video „Gutgläubiger Erwerb“", 160, 298, beim("p932", "Schema"), "Bold", 30, farbe=TEXT),
    *okz("Berta ist in beiden Fällen gutgläubig", 350, "gg", "Bold", 34, x=160),
    *w1,
    *requisit([("nb", ("tabler", "camera", 110, HELLGRAU2), "nicht seine Kamera", HELLROT),
               ("p932", ("ph", "handshake", 110, GELB), "gutgläubiger Erwerb", WEISS),
               ("gg", ("tabler", "shield-check", 100, GRUEN), "gutgläubig", GRUEN),
               ("w1", ("tabler", "lock", 100, HELLROT), "Sperre: § 935", HELLROT)]),
    *zwei("HE", [("nb", "ernst"), ("w1", "skeptisch")], "BT", [("nb", "denkt"), ("gg", "froh"), ("w1", "sorge")]),
]))
assert w1_y <= 900, w1_y

# ===========================================================================================================================
# F 1. Begriff: unfreiwilliger Verlust des unmittelbaren Besitzes
# ===========================================================================================================================
P1 = "1. Abhandenkommen"
WD = umbruch("„Eine bewegliche Sache kommt ihrem Eigentümer abhanden, wenn dieser den unmittelbaren Besitz an ihr ohne "
             "seinen Willen verliert …“", 32, 1040)
wd, wd_y = wortlaut(80, 250, 1100, WD, "BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 11", "def", marken=[
    (_zi(WD, "unmittelbaren"), "unmittelbaren", beim("def", "unmittelbaren")),
    (_zi(WD, "ohne"), "ohne", beim("def", "ohne"))], size=32)
folie([("begr", f"{P1} › gestohlen, verloren: Beispiele"), ("def", f"{P1} › unfreiwilliger Verlust des unmittelbaren Besitzes"),
       ("grund", f"{P1} › Grund: kein Rechtsschein"), ("fb", f"{P1} › Fall B: abhandengekommen")], rechts_frei([
    *tafel("begr", "1. Was heißt abhandenkommen?"),
    z("gestohlen, verloren: nur Beispiele des Oberbegriffs", 110, 180, "begr", "Bold", 32),
    *wd,
    z("unfreiwilliger Besitzverlust entwertet den Besitz", 110, wd_y + 25, "grund", "Bold", 32),
    z("als Grundlage des gutgläubigen Erwerbs", 110, wd_y + 68, beim("grund", "Grundlage"), "Bold", 32),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 110, wd_y + 115, beim("grund", "Grundlage")),
    blk(110, wd_y + 175, 1040, 80, HELLROT, beim("fb", "Dieb"), [("Fall B: Dieb nimmt weg, abhandengekommen", "ExtraBold", 34, INK)]),
    *requisit([("begr", ("tabler", "camera-off", 110, HELLGRAU2), "abhanden?", WEISS),
               ("def", ("tabler", "hand-grab", 100, GELB), "ohne Willen", HELLROT),
               ("grund", ("tabler", "shield-off", 100, HELLGRAU2), "kein Rechtsschein", WEISS),
               ("fb", ("tabler", "camera", 110, HELLGRAU2), "Fall B", HELLROT)]),
    *zwei("HE", [("begr", "ruhig"), ("fb", "sorge")], "BT", [("begr", "denkt"), ("def", "ernst")]),
]))
assert wd_y + 255 <= 900, wd_y

# ===========================================================================================================================
# G Täuschung
# ===========================================================================================================================
folie([("taeu", f"{P1} › Täuschung: trotzdem freiwillig")], rechts_frei([
    *tafel("taeu", "Vorsicht bei Täuschung"),
    blk(110, 190, 1040, 150, HELLROT, beim("taeu2", "Wer"), [("Mit einer Lüge erschwindelt:", "Bold", 34, INK),
                                                          ("trotzdem freiwillig bekommen", "ExtraBold", 36, INK)]),
    *neinz("Besitzaufgabe nicht unfreiwillig, weil durch Täuschung bestimmt", 380, beim("taeu2", "freiwillig"), "Bold", 30,
           x=160),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 160, 425, beim("taeu2", "freiwillig")),
    *requisit([("taeu", ("tabler", "masks-theater", 110, LILA), "Täuschung", HELLROT),
               (beim("taeu2", "freiwillig"), ("tabler", "hand-grab", 100, GELB), "freiwillig", GRUEN)]),
    *zwei("HE", [("taeu", "skeptisch")], "BT", [("taeu", "ernst"), (beim("taeu2", "freiwillig"), "denkt")]),
]))

# ===========================================================================================================================
# H 2. mittelbarer Besitz: Wortlautkarte § 935 Abs. 1 S. 2 BGB
# ===========================================================================================================================
P2 = "2. mittelbarer Besitz"
W2 = umbruch("„Das Gleiche gilt, falls der Eigentümer nur mittelbarer Besitzer war, dann, wenn die Sache dem Besitzer "
             "abhanden gekommen war.“", 32, 1040)
w2, w2_y = wortlaut(80, 430, 1100, W2, "§ 935 Abs. 1 S. 2 BGB", "w2", marken=[
    (_zi(W2, "mittelbarer Besitzer"), "mittelbarer Besitzer", beim("w2", "mittelbarer")),
    (_zi(W2, "dem Besitzer"), "dem Besitzer", beim("w2", "Besitzer", nr=2))], size=32)
folie([("mb", f"{P2} › Fall A"), ("mb2", f"{P2} › Hella mittelbar, Knut unmittelbar"), ("w2", f"{P2} › § 935 Abs. 1 S. 2 BGB")],
      rechts_frei([
    *tafel("mb", "2. Fall A: mittelbarer Besitz"),
    blk(110, 180, 1040, 76, LILA, beim("mb2", "Verleiherin"), [("Hella (Verleiherin): mittelbare Besitzerin", "Bold", 32, INK)]),
    blk(110, 275, 1040, 76, ORANGE, beim("mb2", "Knut"), [("Knut (Entleiher): unmittelbarer Besitzer", "Bold", 32, INK)]),
    zit("§ 868 BGB; Entleiher als Besitzmittler: BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 26", 110, 370, beim("mb2", "Knut")),
    *w2,
    *requisit([("mb", ("tabler", "camera", 110, HELLGRAU2), "Fall A", GRUEN),
               ("mb2", ("tabler", "calendar-event", 100, WEISS), "Leihe", WEISS),
               ("w2", ("tabler", "book", 100, WEISS), "Satz 2", GELB)]),
    *zwei("HE", [("mb", "ruhig"), ("w2", "ernst")], "KN", [("mb", "ruhig"), ("w2", "denkt")]),
]))
assert w2_y <= 900, w2_y

# ===========================================================================================================================
# I Es kommt auf Knut an
# ===========================================================================================================================
folie([("knut", f"{P2} › Es kommt auf Knut an"), ("mbv", f"{P2} › Verlust des mittelbaren Besitzes reicht nicht"),
       ("umg", f"{P2} › Gegenprobe: Knut bestohlen")], rechts_frei([
    *tafel("knut", "Es kommt auf Knut an"),
    *okz("Knut hat die Kamera freiwillig an Berta übergeben", 185, beim("knut2", "freiwillig"), "Bold", 32, x=160),
    blk(110, 255, 1040, 76, GRUEN, beim("knut2", "übergeben"), [("kein Abhandenkommen", "ExtraBold", 36, INK)]),
    *neinz("Verlust des mittelbaren Besitzes reicht nicht", 375, beim("mbv", "reicht"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 13.12.2013 – V ZR 58/13, Rn. 16, 19", 160, 420, beim("mbv", "reicht")),
    linienzug([(130, 490), (1130, 490)], "umg", breite=3),
    z("Gegenprobe: Knut wird die Kamera gestohlen", 110, 515, beim("umg", "wenn"), "Bold", 32),
    blk(110, 575, 1040, 76, HELLROT, beim("umg", "Dann"), [("dann abhandengekommen nach Satz 2", "ExtraBold", 34, INK)]),
    *requisit([("knut", ("tabler", "hand-grab", 100, GELB), "Knut entscheidet", ORANGE),
               (beim("knut2", "übergeben"), ("tabler", "camera", 110, HELLGRAU2), "freiwillig", GRUEN),
               ("mbv", ("tabler", "link-off", 100, WEISS), "mittelbar: egal", WEISS),
               ("umg", ("tabler", "alert-triangle", 100, GELB), "Gegenprobe", HELLROT)]),
    *zwei("HE", [("knut", "skeptisch"), ("mbv", "sorge")], "KN", [("knut", "still"), ("umg", "sorge")]),
]))

# ===========================================================================================================================
# J 3. Besitzdiener: Wortlautkarte § 855 BGB
# ===========================================================================================================================
P3 = "3. Besitzdiener"
W855 = umbruch("„Übt jemand die tatsächliche Gewalt über eine Sache für einen anderen in dessen Haushalt oder "
               "Erwerbsgeschäft oder in einem ähnlichen Verhältnis aus, vermöge dessen er den sich auf die Sache beziehenden "
               "Weisungen des anderen Folge zu leisten hat, so ist nur der andere Besitzer.“", 32, 1040)
w855, w855_y = wortlaut(80, 250, 1100, W855, "§ 855 BGB", "w3", marken=[
    (_zi(W855, "Haushalt"), "Haushalt", beim("w3", "Haushalt")),
    (_zi(W855, "Erwerbsgeschäft"), "Erwerbsgeschäft", beim("w3", "Erwerbsgeschäft")),
    (_zi(W855, "Weisungen"), "Weisungen", beim("w3", "Weisungen")),
    (_zi(W855, "Besitzer."), "Besitzer", beim("w3", "nur"))], size=32)
folie([("bd", f"{P3} › die Falle"), ("w3", f"{P3} › § 855 BGB")], rechts_frei([
    *tafel("bd", "3. Die Falle: der Besitzdiener"),
    z("Grundlagen: Video „Besitz und Eigentum“", 110, 180, beim("bd", "bekannt"), "Bold", 30, farbe=TEXT),
    *w855,
    *requisit([("bd", ("tabler", "alert-triangle", 100, GELB), "Besitzdiener", WEISS),
               ("w3", ("tabler", "briefcase", 100, BLAU), "für einen anderen", WEISS)]),
    *zwei("HE", [("bd", "ruhig"), ("w3", "ernst")], "KN", [("bd", "denkt")]),
]))
assert w855_y <= 900, w855_y

# ===========================================================================================================================
# K Gedankenfall: Knut als Angestellter im Fotoladen
# ===========================================================================================================================
folie([("studio", f"{P3} › Gedankenfall Fotoladen"), ("bd2", f"{P3} › Hella unmittelbare Besitzerin"),
       ("bd3", f"{P3} › eigenmächtige Weggabe"), ("streit", f"{P3} › Einzelheiten streitig")], rechts_frei([
    *tafel("studio", "Gedankenfall: der Fotoladen"),
    z("Knut ist Angestellter im Fotoladen von Hella", 110, 180, beim("studio", "Angestellter"), "Bold", 32),
    z("und verkauft eine Kamera eigenmächtig", 110, 225, beim("studio", "eigenmächtig"), "Bold", 32),
    blk(110, 300, 1040, 76, LILA, beim("bd2", "Hella"), [("Hella bleibt unmittelbare Besitzerin", "Bold", 32, INK)]),
    blk(110, 395, 1040, 76, ORANGE, beim("bd2", "Knut"), [("Knut ist nur ihr Besitzdiener", "Bold", 32, INK)]),
    *okz("Weggabe ohne ihren Willen: kann abhandengekommen sein", 505, beim("bd3", "abhandengekommen"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 13.12.2013 – V ZR 58/13, Rn. 9", 160, 550, beim("bd3", "abhandengekommen")),
    blk(110, 615, 1040, 76, HELL, "streit", [("Die Einzelheiten sind streitig.", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 16", 110, 710, "streit"),
    *requisit([("studio", ("tabler", "building-store", 130, BLAU), "Fotoladen", WEISS),
               ("bd2", ("tabler", "briefcase", 100, BLAU), "Besitzdiener", ORANGE),
               ("bd3", ("tabler", "camera", 110, HELLGRAU2), "ohne ihren Willen", HELLROT),
               ("streit", ("ph", "scales", 110, GELB), "streitig", WEISS)]),
    *zwei("HE", [("studio", "ruhig"), ("bd3", "schreck")], "KN", [("studio", "denkt"), ("bd3", "still")]),
]))

# ===========================================================================================================================
# L Probefahrt (BGH V ZR 8/19)
# ===========================================================================================================================
folie([("probe", f"{P3} › Probefahrt: kein Besitzdiener"), ("probe3", f"{P3} › Probefahrt: kein Abhandenkommen")], rechts_frei([
    *tafel("probe", "Gegenbeispiel: die Probefahrt"),
    *neinz("unbegleitete Probefahrt: kein Besitzdiener", 185, beim("probe", "Besitzdiener"), "Bold", 34, x=160),
    z("gefälschte Papiere, 1 Stunde, nie zurück:", 160, 265, beim("probe2", "gefälschten"), "Bold", 32),
    z("trotzdem freiwillig bekommen", 160, 310, beim("probe2", "freiwillig"), "Bold", 32),
    blk(110, 385, 1040, 76, GRUEN, "probe3", [("kein Abhandenkommen", "ExtraBold", 36, INK)]),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Leitsätze 1 bis 3, Rn. 9, 21", 110, 480, "probe3"),
    *requisit([("probe", ("tabler", "car", 150, BLAU), "Probefahrt", WEISS),
               (beim("probe2", "gefälschten"), ("tabler", "file-text", 100, WEISS), "gefälschte Papiere", HELLROT),
               ("probe3", ("tabler", "hand-grab", 100, GELB), "freiwillig", GRUEN)]),
    *zwei("HE", [("probe", "ernst")], "KN", [("probe", "ruhig"), ("probe3", "denkt")]),
]))

# ===========================================================================================================================
# M 4. Ausnahmen: Wortlautkarte § 935 Abs. 2 BGB
# ===========================================================================================================================
P4 = "4. Ausnahmen, § 935 Abs. 2 BGB"
WA2 = umbruch("„Diese Vorschriften finden keine Anwendung auf Geld oder Inhaberpapiere sowie auf Sachen, die im Wege "
              "öffentlicher Versteigerung oder in einer Versteigerung nach § 979 Absatz 1a veräußert werden.“", 32, 1040)
wa2, wa2_y = wortlaut(80, 175, 1100, WA2, "§ 935 Abs. 2 BGB", "abs2", marken=[
    (_zi(WA2, "Geld"), "Geld", beim("geld", "Geld")),
    (_zi(WA2, "Inhaberpapiere"), "Inhaberpapiere", beim("geld", "Inhaberpapiere")),
    (_zi(WA2, "öffentlicher"), "öffentlicher", beim("verst", "öffentlichen")),
    (_zi(WA2, "§ 979 Absatz 1a"), "§ 979 Absatz 1a", beim("verst", "Fundsachen"))], size=32)
folie([("abs2", P4), ("verst", f"{P4} › Versteigerung"), ("abs2b", f"{P4} › Fall B: keine Ausnahme")], rechts_frei([
    *tafel("abs2", "4. Ausnahmen: § 935 Abs. 2 BGB"),
    *wa2,
    z("§ 979 Abs. 1a: Fundsachen-Versteigerung im Internet", 110, wa2_y + 20, beim("verst", "Internet"), "Bold", 30, farbe=TEXT),
    *neinz("Eine Kamera ist kein Geld", wa2_y + 90, beim("abs2b", "Kamera"), "Bold", 34, x=160),
    *neinz("Flohmarkt: keine öffentliche Versteigerung", wa2_y + 155, beim("abs2b", "Flohmarkt"), "Bold", 34, x=160),
    *requisit([("abs2", ("tabler", "book", 100, WEISS), "Abs. 2", GELB),
               ("geld", ("tabler", "coin-euro", 100, GELB), "Geld", WEISS),
               ("verst", ("tabler", "gavel", 100, HOLZ), "Versteigerung", WEISS),
               ("abs2b", ("tabler", "camera", 110, HELLGRAU2), "keine Ausnahme", HELLROT)]),
    *zwei("HE", [("abs2", "ruhig"), ("abs2b", "ernst")], "BT", [("abs2", "denkt"), ("abs2b", "sorge")]),
]))
assert wa2_y + 220 <= 900, wa2_y

# ===========================================================================================================================
# N 5. Wertung (BGH V ZR 92/25 Rn. 15), Veranlassungsprinzip (Lehrbegriff), Dauer der Sperre
# ===========================================================================================================================
P5 = "5. Wertung"
WW = umbruch("„… dass der Eigentümer, der eine Sache … freiwillig aus der Hand gibt, auch die Gefahr einer unrechtmäßigen "
             "Verfügung zu tragen hat, während der Eigentümer, dem die Sache ohne seinen Willen entzogen ist, "
             "schutzbedürftig bleibt …“", 30, 1040)
ww, ww_y = wortlaut(80, 170, 1100, WW, "BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 15", "wert2", marken=[
    (_zi(WW, "freiwillig"), "freiwillig", beim("wert2", "freiwillig")),
    (_zi(WW, "Gefahr"), "Gefahr", beim("wert2", "Gefahr")),
    (_zi(WW, "ohne seinen Willen"), "ohne seinen Willen", beim("wert3", "ohne")),
    (_zi(WW, "schutzbedürftig"), "schutzbedürftig", beim("wert3", "schutzbedürftig"))], size=30)
folie([("wert", f"{P5} › Warum der Unterschied?"), ("wert2", f"{P5} › Wer freiwillig weggibt, trägt die Gefahr"),
       ("veran", f"{P5} › Lehrbegriff: Veranlassungsprinzip"), ("dauer", f"{P5} › Sperre bleibt")], rechts_frei([
    *tafel("wert", "5. Warum dieser Unterschied?"),
    *ww,
    blk(110, ww_y + 25, 1040, 120, HELL, "veran", [("Lehrbegriff: Veranlassungsprinzip", "ExtraBold", 32, INK),
                                                ("Hella hat Knut ausgesucht, den Dieb nicht", "Bold", 32, INK)]),
    blk(110, ww_y + 170, 1040, 120, HELLROT, "dauer", [("abhandengekommen: grundsätzlich gesperrt,", "Bold", 32, INK),
                                                     ("auch für weitere Käufer, bis Hella Besitz hat", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 26.6.2026 – V ZR 92/25, Leitsatz, Rn. 13", 110, ww_y + 300, beim("dauer", "gesperrt")),
    *requisit([("wert", ("ph", "scales", 110, GELB), "Wertung", WEISS),
               ("wert2", ("tabler", "hand-grab", 100, GELB), "freiwillig: Risiko", GRUEN),
               ("wert3", ("tabler", "shield-check", 100, GRUEN), "unfreiwillig: Schutz", WEISS),
               ("veran", ("tabler", "user-check", 100, ORANGE), "selbst ausgesucht", WEISS),
               ("dauer", ("tabler", "lock", 100, HELLROT), "dauerhaft gesperrt", HELLROT)]),
    *zwei("HE", [("wert", "ruhig"), ("veran", "skeptisch"), ("dauer", "froh")], "BT", [("wert", "ernst"), ("dauer", "sorge")]),
]))
assert ww_y + 345 <= 900, ww_y

# ===========================================================================================================================
# O 6. Lösung beider Fälle (gleiche Struktur links/rechts)
# ===========================================================================================================================
LK, RK, KW = 110, 640, 510
folie([("loes", "Lösung · beide Fälle"), ("la", "Lösung › Fall A: Berta Eigentümerin"),
       ("lb", "Lösung › Fall B: Hella bleibt Eigentümerin")], rechts_frei([
    *tafel("loes", "6. Die Lösung"),
    karte(LK, 180, KW, 520, "la", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("Fall A: verliehen", LK + 25, 198, "la", "ExtraBold", 34, rechts=LK + KW - 10),
    *okz("kein Abhandenkommen", 262, beim("la", "kein"), "Bold", 30, x=LK + 70, gr=18, rechts=LK + KW - 10),
    z("Berta wird Eigentümerin,", LK + 25, 322, beim("la", "Berta"), size=30, rechts=LK + KW - 10),
    z("§§ 929 S. 1, 932 BGB", LK + 25, 364, beim("la", "Berta"), "Bold", 30, rechts=LK + KW - 10),
    *neinz("§ 985 gegen Berta", 430, beim("la2", "herausverlangen"), "Bold", 30, x=LK + 70, gr=18, rechts=LK + KW - 10),
    z("Hella hält sich an Knut", LK + 25, 495, beim("la2", "Knut"), size=30, rechts=LK + KW - 10),
    karte(RK, 180, KW, 520, "lb", fill=HELLROT, rund=18, schatten=6, rand=4),
    z("Fall B: gestohlen", RK + 25, 198, "lb", "ExtraBold", 34, rechts=RK + KW - 10),
    *neinz("abhandengekommen", 262, beim("lb", "abhandengekommen"), "Bold", 30, x=RK + 70, gr=18, rechts=RK + KW - 10),
    z("Berta wird nicht", RK + 25, 322, beim("lb", "Berta"), size=30, rechts=RK + KW - 10),
    z("Eigentümerin (§ 935 BGB)", RK + 25, 364, beim("lb", "Berta"), "Bold", 30, rechts=RK + KW - 10),
    *okz("§ 985 gegen Berta", 430, beim("lb2", "herausverlangen"), "Bold", 30, x=RK + 70, gr=18, rechts=RK + KW - 10),
    z("Hella bleibt Eigentümerin", RK + 25, 495, beim("lb2", "Hella"), size=30, rechts=RK + KW - 10),
    z("Video „Herausgabeanspruch“", 110, 740, beim("lb2", "mehr"), "Bold", 30, farbe=TEXT),
    *requisit([("loes", ("ph", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("la", ("tabler", "camera", 110, HELLGRAU2), "Fall A: Berta", GRUEN),
               ("lb", ("tabler", "camera", 110, HELLGRAU2), "Fall B: Hella", HELLROT)]),
    *zwei("HE", [("loes", "ruhig"), ("la", "sorge"), ("lb2", "froh")], "BT", [("loes", "ernst"), ("la", "froh"), ("lb", "sorge")]),
]))

# ===========================================================================================================================
# P Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · § 935 nach §§ 932 bis 934"), ("tp2", "Klausurtipp · Wer besaß unmittelbar?"),
       ("tp3", "Klausurtipp · Täuschung: an Freiwilligkeit denken")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§ 935 BGB immer erst nach §§ 932 bis 934 BGB", 200, 200, "tipp", "Bold", 34),
    z("prüfen: als letzte Hürde", 200, 255, beim("tipp", "letzte"), size=34),
    z("Wer hatte den unmittelbaren Besitz?", 200, 345, "tp2", "Bold", 34),
    z("Hat er ihn freiwillig aufgegeben?", 200, 400, beim("tp2", "freiwillig"), size=34),
    linienzug([(130, 480), (1130, 480)], "tp3", breite=3),
    z("Täuschung: an die Freiwilligkeit denken", 200, 510, "tp3", "Bold", 34),
    z("Betrug ist kein Diebstahl.", 200, 565, beim("tp3", "Betrug"), "ExtraBold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# Q Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Unmittelbarer Besitz: Wer hatte ihn?", True),
          ("c1", 1, "Eigentümer (auch durch Besitzdiener, § 855 BGB), § 935 Abs. 1 S. 1", False),
          (beim("c1", "oder"), 1, "oder sein Besitzmittler, § 935 Abs. 1 S. 2", False),
          ("c2", 0, "II. Unfreiwilliger Verlust", True),
          (beim("c2", "Eine"), 1, "Täuschung reicht nicht", False),
          ("c3", 0, "III. Keine Ausnahme nach § 935 Abs. 2 BGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: § 935 BGB"), 110, 90, "sch", 46),
           z("im gutgläubigen Erwerb nach §§ 932 bis 934 BGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 85, 1: 75}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Unmittelbarer Besitz"), ("c2", "Prüfschema › II. Unfreiwilliger Verlust"),
       ("c3", "Prüfschema › III. Keine Ausnahme")], els_sch)

# ===========================================================================================================================
# R Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Verliehen ist nicht", 0)], [("abhandengekommen", "a"), (".", 0)]], 750, 300, 48, "merke",
                {"a": beim("merke", "abhandengekommen")}),
    *markertext([[("Abhanden kommt eine Sache nur,", 0)], [("wenn der unmittelbare Besitz", 0)],
                 [("unfreiwillig", "b"), (" verloren geht.", 0)]], 750, 540, 44, "m2", {"b": beim("m2", "unfreiwillig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
