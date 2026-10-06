"""Folge 207 · Gesamtsaldierung: Der Vermögensschaden beim Betrug § 263 erklärt – Serienstandard Open Peeps (Katzenkönig).
Fall: Samstagvormittag, Garagenverkauf. Alwin (um 45) verkauft Gundula (um 60) einen „Designer-Sessel“ für 300 € als Original,
obwohl er weiß, dass es ein Nachbau ist (300 € hält er für den richtigen Preis). Gundula zahlt bar. Die Gutachterin Ulla schätzt
den Sessel: gut gemachter Nachbau, genau 300 € wert. Gegenfall: nur 120 € wert → Schaden 180 €.
Szenen laut ../SZENENPLAN.md: A1 Garagenverkauf, A2 Leseecke mit Gutachten, B Sachverhalt, C1 § 263 Abs. 1 (Wortlautkarte),
C2 Vermögensbegriff, D Gesamtsaldierung, E Waage 300 € − 300 € = 0 €, F kein Schaden trotz Täuschung, G1 individueller
Schadenseinschlag, G2 Eingehungs- und Gefährdungsschaden, H Gegenfall (Waage geneigt, 180 €), I Versuch § 263 Abs. 2,
J Klausurtipp (Lexi), K Prüfschema, L Merksatz (Lexi). Keine echten Marken, keine Klischees; Personen fiktiv.
Handlungsgeräusche: Geldscheine beim Bezahlen (A1), Sessel wird abgestellt (A2); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 203 (gemeinsame Dateien unverändert); neu: waage(), gleichung().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (StGB), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_207/"

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
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if getattr(e, "in_tafel", False):            # bewusst auf der Tafel (Waage, Vermögensgegenstände)
            continue
        if n.startswith(("bild:", "ficon:")) or "/op_207/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]





# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
FE = "fluent-emoji-high-contrast"
X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"GU": "Gundula", "AL": "Alwin", "UL": "Ulla"}
NFARBE = {"GU": LILA, "AL": GRUEN, "UL": TUERKIS}
SESSEL = ROT                                # Farbe des Sessels in allen Szenen gleich
PS_ = "§ 263 Abs. 1 StGB › Vermögensschaden"


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


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


def zwei(folge_gu, folge_al):
    """Gundula und Alwin rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("GU", X1, folge_gu), *stehend("AL", X2, folge_al)]


def auf_tafel(e):
    """Requisit, das bewusst Teil der Tafel ist (Waage, Vermögensgegenstände); rechts_frei() lässt es zu."""
    e.in_tafel = True
    return e


def sessel(c, cx, unten=BODEN_Y, breite=280, bis=None, anim="pop"):
    """Der „Designer-Sessel“ ohne Marke: Tabler armchair (MIT), Palettenfüllung."""
    return ficon("tabler", "armchair", cx, unten, breite, c, fuell=SESSEL, bis=bis, anim=anim)


def geld(c, cx, unten, breite=150, bis=None, anim="pop"):
    return ficon(FE, "euro-banknote", cx, unten, breite, c, fuell=GRUEN, bis=bis, anim=anim)


def waage(cx, oben, cue, neig=0, bis=None, links=None, rechts=None):
    """Balkenwaage aus Tuschelinien: Säule, Fuß, Balken, Schalen. neig > 0 senkt die linke Schale (schwerere Seite).
    links/rechts = (cue, Element-Fabrik(cx, unten)) legt einen Gegenstand in die Schale. Gibt (Elemente, (lx, ly), (rx, ry))."""
    halb, haenge, fuss = 300, 170, oben + 330
    ly, ry = oben + neig, oben - neig
    lx, rx = cx - halb, cx + halb
    els = [hart(linienzug([(cx, oben - 18), (cx, fuss)], cue, breite=12)),
           hart(linienzug([(cx - 130, fuss), (cx + 130, fuss)], cue, breite=14)),
           hart(linienzug([(lx, ly), (rx, ry)], cue, breite=12))]
    schalen = []
    for x, y in ((lx, ly), (rx, ry)):
        sy = y + haenge
        els += [hart(linienzug([(x, y), (x - 115, sy)], cue, breite=5)), hart(linienzug([(x, y), (x + 115, sy)], cue, breite=5)),
                hart(linienzug([(x - 125, sy), (x - 85, sy + 26), (x, sy + 36), (x + 85, sy + 26), (x + 125, sy)], cue, breite=8)),
                hart(linienzug([(x - 125, sy), (x + 125, sy)], cue, breite=6))]
        schalen.append((x, sy + 2))
    for e in els:
        e.bis = bis
    return els, schalen[0], schalen[1]


def gleichung(text, cx, y, cue, size=54, farbe=INK, **k):
    """Rechnung in Ziffern, mittig unter der Waage."""
    f = F("ExtraBold", size)
    return z(text, cx - f.getlength(glyphen(text)) / 2, y, cue, "ExtraBold", size, farbe=farbe, **k)


# ===========================================================================================================================
# A1 Fall: Garagenverkauf (Samstagvormittag)
# ===========================================================================================================================
ALX, SEX, GUX = 720, 1040, 1500
folie([(NULL, "Fall · Samstagvormittag: ein Garagenverkauf"), ("gundula", "Fall · Gundula sucht einen Sessel"),
       ("alwin", "Fall · Alwin: „Designer-Sessel“ für 300 €"), ("nachbau", "Fall · In Wahrheit ein Nachbau"),
       ("preis", "Fall · Alwin hält 300 € für den richtigen Preis"), ("g1", "Fall · Gundula: „Ist das wirklich ein Original?“"),
       ("a1", "Fall · Alwin: „Ja, ein echtes Designerstück.“"), ("zahlt", "Fall · Gundula zahlt 300 € bar"),
       ("mit", "Fall · Gundula nimmt den Sessel mit")], [
    hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], NULL, breite=7)),
    hart(ficon("ph", "garage", 300, BODEN_Y, 470, NULL, fuell=HELLGRAU, anim="cut")),
    hart(pl("Samstagvormittag", 70, 30, NULL, fill=LILA, size=38)),
    hart(pl("Garagenverkauf", 70, 100, NULL, fill=WEISS, size=32)),
    pl("Gundula sucht einen bequemen Sessel", 1060, 30, "gundula", fill=LILA, size=30, bis="g1"),
    pl("für ihre Leseecke", 1060, 95, beim("gundula", "Leseecke"), fill=WEISS, size=30, bis="g1"),
    *fig("GU", GUX, BODEN_Y, FHA, [("gundula", "ruhig")], bis="g1"),
    *redet("GU_redet", GUX, BODEN_Y, FHA, "g1", "a1"),
    *fig("GU", GUX, BODEN_Y, FHA, [("a1", "froh"), ("mit", "froh_r")], erst="cut"),
    ns(NAME["GU"], GUX, BODEN_Y, "gundula", NFARBE["GU"], d=0.1),
    *fig("AL", ALX, BODEN_Y, FHA, [("alwin", "ruhig_r"), ("nachbau", "denkt_r"), ("preis", "ruhig_r")], bis="a1"),
    *redet("AL_redet_r", ALX, BODEN_Y, FHA, "a1", "zahlt"),
    *fig("AL", ALX, BODEN_Y, FHA, [("zahlt", "froh_r")], erst="cut"),
    ns(NAME["AL"], ALX, BODEN_Y, "alwin", NFARBE["AL"], d=0.1),
    sessel("alwin", SEX, bis="mit"),
    pl("„Designer-Sessel“", SEX, 545, beim("alwin", "Designer"), fill=WEISS, size=30, anker="m", bis="zahlt"),
    pl("300 €", SEX, 610, beim("alwin", "dreihundert"), fill=GELB, size=36, anker="m", bis="zahlt"),
    blase("denk", 470, 190, "nachbau", 800, 330, inhalt=["kein Original –", "ein Nachbau"], textsize=36,
          figur=("AL_denkt_r", ALX, BODEN_Y, FHA), bis="g1"),
    pl("Alwin hält 300 € für den richtigen Preis", 70, 170, "preis", fill=GRUEN, size=30, bis="zahlt"),
    blase("sprech", 560, 210, "g1", 1480, 240, inhalt=["Ist das wirklich", "ein Original?"], textsize=40,
          figur=("GU_redet", GUX, BODEN_Y, FHA), bis="a1"),
    blase("sprech", 520, 210, "a1", 840, 300, inhalt=["Ja, ein echtes", "Designerstück."], textsize=40,
          figur=("AL_redet_r", ALX, BODEN_Y, FHA), bis="zahlt"),
    szene(bewegt(geld("zahlt", 880, 600, bis="leseecke"), ("zahlt", 0.0), beim("zahlt", "Euro", ende=True), 520),
          "207geld_1", 1.0, 0.0),
    pl("Gundula zahlt 300 € bar", 1060, 30, "zahlt", fill=GELB, size=30),
    pl("und nimmt den Sessel mit", 1060, 95, "mit", fill=WEISS, size=30),
    sessel("mit", 1745, breite=240, anim="cut"),
])

# ===========================================================================================================================
# A2 Fall: Leseecke und Gutachten
# ===========================================================================================================================
LSX, GU2, ULX = 470, 1000, 1560
folie([("leseecke", "Fall · Der Sessel in der Leseecke"), ("gutachten", "Fall · Die Gutachterin Ulla schätzt den Sessel"),
       ("u1", "Fall · Ulla: „Er ist genau 300 € wert.“"), ("frage", "Fall · Getäuscht – aber geschädigt?"),
       ("frage2", "Fall · Die Antwort: die Gesamtsaldierung")], [
    hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], "leseecke", breite=7)),
    hart(ficon("ph", "lamp", 170, BODEN_Y, 190, "leseecke", fuell=GELB, anim="cut")),
    hart(linienzug([(640, 640), (900, 640)], "leseecke", breite=10)),
    hart(ficon(FE, "books", 770, 636, 150, "leseecke", fuell=BLAU, anim="cut")),
    hart(ficon(FE, "potted-plant", 770, BODEN_Y, 120, "leseecke", fuell=GRUEN, anim="cut")),
    szene(sessel("leseecke", LSX, breite=300), "207sessel_1", 1.0, 0.0),
    hart(pl("Zu Hause: die Leseecke", 70, 30, "leseecke", fill=LILA, size=38)),
    pl("Gutachterin Ulla schätzt den Sessel", 70, 105, "gutachten", fill=TUERKIS, size=30),
    ficon(FE, "magnifying-glass-tilted-left", LSX + 40, 610, 110, beim("gutachten", "schätzen"), fuell=WEISS, bis="frage"),
    pl("Wert: 300 €", LSX, 405, beim("u1", "dreihundert"), fill=GRUEN, size=34, anker="m"),
    *fig("GU", GU2, BODEN_Y, FHA, [("leseecke", "froh_r"), ("gutachten", "ruhig_r"), (beim("u1", "Nachbau"), "sorge_r"),
                                   (beim("u1", "dreihundert"), "denkt_r"), ("frage", "ernst_r")]),
    ns(NAME["GU"], GU2, BODEN_Y, "leseecke", NFARBE["GU"], d=0.1),
    *fig("UL", ULX, BODEN_Y, FHA, [("gutachten", "ruhig")], bis="u1"),
    *redet("UL_redet", ULX, BODEN_Y, FHA, "u1", "frage"),
    *fig("UL", ULX, BODEN_Y, FHA, [("frage", "ruhig")], erst="cut"),
    ns(NAME["UL"], ULX, BODEN_Y, "gutachten", NFARBE["UL"], d=0.1),
    blase("sprech", 740, 230, "u1", 1440, 250, inhalt=["Ein Nachbau, aber gut gemacht.", "Er ist genau 300 € wert."],
          textsize=34, figur=("UL_redet", ULX, BODEN_Y, FHA), bis="frage"),
    pl("Gundula wurde getäuscht.", 70, 180, "frage", fill=PINK, size=32),
    pl("Aber ist ihr Vermögen beschädigt?", 70, 255, beim("frage", "Aber"), fill=GELB, size=32),
    pl("Antwort: die Gesamtsaldierung", 1080, 180, "frage2", fill=WEISS, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_207(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_207("sv", [
    "Samstagvormittag, Garagenverkauf: Gundula (um 60) sucht einen bequemen Sessel für ihre Leseecke. Alwin bietet vor "
    "seiner Garage einen „Designer-Sessel“ für 300 € an. Er weiß, dass es kein Original ist, sondern ein Nachbau; 300 € "
    "hält er aber für den richtigen Preis.",
    "Gundula: „Ist das wirklich ein Original?“ Alwin: „Ja, ein echtes Designerstück.“ Gundula zahlt 300 € bar und nimmt "
    "den Sessel mit.",
    "Später schätzt die Gutachterin Ulla den Sessel: ein gut gemachter Nachbau, genau 300 € wert.",
], "Hat sich Alwin wegen Betrugs nach § 263 StGB strafbar gemacht?")

# ===========================================================================================================================
# C1 § 263 Abs. 1 StGB (Wortlaut): das Merkmal „Vermögen beschädigt“; Täuschung, Irrtum, Verfügung liegen vor
# ===========================================================================================================================
P263 = "§ 263 Abs. 1 StGB"
W263 = ("„Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen "
        "eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch Entstellung oder Unterdrückung "
        "wahrer Tatsachen einen Irrtum erregt oder unterhält, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit "
        "Geldstrafe bestraft.“")
w263, w263_y = wortlaut(80, 170, 1100, W263, "§ 263 Abs. 1 StGB", "p263", marken=[
    ("Vermögen eines anderen", beim("beschaedigt", "Vermögen")), ("beschädigt", beim("beschaedigt", "beschädigt"))], size=28)
folie([("p263", f"{P263} › Wortlaut"), ("beschaedigt", f"{P263} › Merkmal: Vermögen beschädigt"),
       ("kette", f"{P263} › Täuschung, Irrtum, Verfügung (+)"), ("v065", f"{P263} › Prüfung: Folge zum Betrugsschema")],
      rechts_frei([
    *tafel("p263", "Betrug, § 263 Abs. 1 StGB"),
    *w263,
    z("Täuschung, Irrtum, Vermögensverfügung:", 110, w263_y + 30, "kette", "ExtraBold", 32),
    *okz("Täuschung: Alwin lügt über das „Original“", w263_y + 85, beim("kette2", "Alwin"), "Bold", 30, x=170),
    *okz("Irrtum: Gundula glaubt ihm", w263_y + 135, beim("kette2", "Gundula"), "Bold", 30, x=170),
    *okz("Vermögensverfügung: Gundula zahlt", w263_y + 185, beim("kette2", "zahlt"), "Bold", 30, x=170),
    pl("Prüfung im Einzelnen: Folge zum Betrugsschema", 110, w263_y + 255, "v065", fill=WEISS, size=28),
    *requisit([("p263", (FE, "balance-scale", 110, GELB), "§ 263 StGB", GELB),
               ("kette", (FE, "white-question-mark", 80, WEISS), "Original?", WEISS),
               (beim("kette2", "zahlt"), (FE, "euro-banknote", 130, GRUEN), "300 € gezahlt", GRUEN)]),
    *zwei([("p263", "ruhig"), ("kette", "denkt"), (beim("kette2", "zahlt"), "ernst")],
          [("p263", "ruhig"), ("kette", "ernst")]),
]))
assert w263_y + 320 <= 900, w263_y

# ===========================================================================================================================
# C2 Heute nur der Schaden; Vermögensbegriff (Rechtsprechung) in einem Satz
# ===========================================================================================================================
folie([("heute", f"{PS_}: Ist das Vermögen beschädigt?"), ("vbegr", f"{PS_} › Vermögen: geldwerte Güter")], rechts_frei([
    *tafel("heute", "Heute: der Vermögensschaden"),
    pl("nur noch offen: Ist das Vermögen beschädigt?", 110, 185, "heute", fill=GELB, size=32),
    blk(110, 290, 1040, 175, BLAU, "vbegr", [("Vermögen (Rechtsprechung):", "ExtraBold", 32, INK),
                                            ("Summe der geldwerten Güter einer Person,", "Bold", 30, INK),
                                            ("wirtschaftlich betrachtet", "Bold", 30, INK)]),
    zit("BGH 2 StR 335/15 Rn. 4, 6; BVerfG 2 BvR 2559/08 Rn. 85, 102", 130, 480, beim("vbegr", "Summe")),
    auf_tafel(geld(beim("vbegr", "geldwerten"), 260, 720, breite=150)),
    auf_tafel(sessel(beim("vbegr", "geldwerten"), 500, 720, breite=170)),
    auf_tafel(ficon(FE, "house", 730, 720, 140, beim("vbegr", "geldwerten"), fuell=GELB)),
    auf_tafel(ficon("tabler", "credit-card", 960, 720, 150, beim("vbegr", "geldwerten"), fuell=BLAU)),
    *requisit([("heute", ("ph", "wallet", 110, GELB), "Vermögen beschädigt?", GELB),
               ("vbegr", (FE, "money-bag", 110, GELB), "geldwerte Güter", BLAU)]),
    *stehend("GU", FX, [("heute", "denkt"), ("vbegr", "ruhig")]),
]))

# ===========================================================================================================================
# D Gesamtsaldierung: vorher – nachher, Gegenleistung gleicht aus, verbleibende Minderung
# ===========================================================================================================================
folie([("saldo", f"{PS_} › Gesamtsaldierung"), ("vorher", f"{PS_} › vorher: unmittelbar vor der Verfügung"),
       ("nachher", f"{PS_} › nachher: unmittelbar danach"), ("komp", f"{PS_} › Gegenleistung gleicht aus"),
       ("minder", f"{PS_} › Schaden = verbleibende Minderung")], rechts_frei([
    *tafel("saldo", "Die Gesamtsaldierung"),
    pl("Schaden ermitteln: Gesamtsaldierung", 110, 180, beim("saldo", "Gesamtsaldierung"), fill=GELB, size=32),
    blk(110, 270, 490, 175, HELLGRAU, "vorher", [("vorher:", "ExtraBold", 32, INK), ("Vermögen unmittelbar", "Bold", 30, INK),
                                               ("vor der Verfügung", "Bold", 30, INK)]),
    pfeil(615, 357, 655, 357, "nachher", breite=8, kopf=22),
    blk(660, 270, 490, 175, HELLGRAU, "nachher", [("nachher:", "ExtraBold", 32, INK), ("Vermögen unmittelbar", "Bold", 30, INK),
                                                 ("nach der Verfügung", "Bold", 30, INK)]),
    *okz("was durch die Verfügung zugleich hereinkommt,", 490, "komp", "Bold", 30, x=170),
    z("gleicht den Abfluss aus: vor allem die Gegenleistung", 170, 535, beim("komp", "Gegenleistung"), "Bold", 30),
    blk(110, 620, 1040, 130, HELLROT, "minder", [("Schaden nur, wenn unterm Strich", "ExtraBold", 32, INK),
                                                ("eine Minderung bleibt", "Bold", 30, INK)]),
    zit("BGH 1 StR 13/18 Rn. 8; BGH 2 StR 77/22 Rn. 8; BGH 2 StR 283/25 Rn. 10", 130, 765, beim("minder", "Minderung")),
    *requisit([("saldo", (FE, "balance-scale", 120, GELB), "Gesamtsaldierung", GELB),
               ("vorher", (FE, "euro-banknote", 130, GRUEN), "vorher", HELLGRAU),
               ("nachher", ("tabler", "armchair", 130, SESSEL), "nachher", HELLGRAU),
               (beim("komp", "Gegenleistung"), ("tabler", "armchair", 130, SESSEL), "Gegenleistung", GRUEN),
               ("minder", ("tabler", "calculator", 100, WEISS), "Minderung?", HELLROT)]),
    *stehend("GU", FX, [("saldo", "denkt"), ("komp", "ruhig"), ("minder", "ernst")]),
]))

# ===========================================================================================================================
# E Im Fall: die Waage – 300 € − 300 € = 0 €
# ===========================================================================================================================
WX, WO = 620, 330                            # Waage: Mitte, Höhe des Balkens
els_w, (lx, ly), (rx, ry) = waage(WX, WO, "rech")
folie([("rech", f"{PS_} › im Fall: die Waage"), ("rech1", f"{PS_} › vorher: 300 € Geld"),
       ("rech2", f"{PS_} › nachher: Sessel, 300 € wert"), ("rech3", f"{PS_} › 300 € − 300 € = 0 €"),
       ("null", f"{PS_} (−)")], rechts_frei([
    *tafel("rech", "Im Fall: die Waage"),
    *els_w,
    auf_tafel(geld("rech1", lx, ly, breite=170)),
    pl("vorher: 300 € Geld", lx, ly + 70, "rech1", fill=GRUEN, size=30, anker="m"),
    auf_tafel(sessel("rech2", rx, ry, breite=170)),
    pl("nachher: Sessel, 300 € wert", rx - 30, ry + 70, "rech2", fill=WEISS, size=30, anker="m"),
    gleichung("300 € − 300 € = 0 €", WX, 690, "rech3"),
    *neinz("ein Schaden bleibt nicht", 790, "null", "ExtraBold", 34, x=330),
    *requisit([("rech", (FE, "balance-scale", 120, GELB), "Waage im Gleichgewicht", GELB),
               ("rech3", ("tabler", "calculator", 100, WEISS), "300 € − 300 €", WEISS),
               ("null", ("tabler", "calculator", 100, WEISS), "Schaden: 0 €", HELLROT)]),
    *stehend("GU", FX, [("rech", "ruhig"), ("rech2", "froh"), ("null", "denkt")]),
]))

# ===========================================================================================================================
# F Kein Schaden trotz Täuschung: BGHSt 16, 321 (Melkmaschine); BGH 2 StR 283/25 (Nachbau statt Original)
# ===========================================================================================================================
PK = f"{PS_} › kein Schaden trotz Täuschung"
folie([("folge", f"{PK}"), ("dispo", f"{PK} › § 263 schützt das Vermögen"), ("melk", f"{PK} › Melkmaschinen-Fall"),
       ("nb", f"{PK} › Nachbau statt Original"), ("kein", "Ergebnis · kein vollendeter Betrug von Alwin")], rechts_frei([
    *tafel("folge", "Kein Schaden trotz Täuschung"),
    z("Gundula wurde belogen – und doch fehlt der Schaden", 110, 180, "folge", "ExtraBold", 32),
    blk(110, 245, 1040, 130, BLAU, "dispo", [("§ 263 schützt das Vermögen, nicht die", "ExtraBold", 32, INK),
                                            ("Freiheit, ohne Täuschung zu entscheiden", "Bold", 30, INK)]),
    z("BGH, Melkmaschinen-Fall: Wer wegen einer Täuschung", 110, 410, beim("melk", "Bundesgerichtshof"), "Bold", 30),
    z("verfügt, ist nicht schon deshalb geschädigt", 110, 455, beim("melk", "Wer"), "Bold", 30),
    zit("BGHSt 16, 321 (Beschl. v. 16.8.1961 – 4 StR 166/61)", 110, 505, beim("melk", "geschädigt")),
    blk(110, 570, 1040, 175, GELB, "nb", [("Nachbau statt Original:", "ExtraBold", 32, INK),
                                         ("Schaden regelmäßig nur, wenn die Sache", "Bold", 30, INK),
                                         ("objektiv den Preis nicht wert ist", "Bold", 30, INK)]),
    zit("BGH 2 StR 283/25 Rn. 10, 13", 130, 760, beim("nb", "objektiv")),
    *neinz("vollendeter Betrug von Alwin", 820, "kein", "ExtraBold", 32, x=170),
    *requisit([("folge", (FE, "white-question-mark", 80, WEISS), "belogen, doch der Schaden fehlt", WEISS),
               ("dispo", (FE, "balance-scale", 120, BLAU), "Vermögensdelikt", BLAU),
               ("melk", (FE, "cow-face", 110, WEISS), "Melkmaschinen-Fall", WEISS),
               ("nb", ("tabler", "armchair", 130, SESSEL), "Nachbau: 300 € wert", GELB),
               ("kein", (FE, "balance-scale", 120, HELLROT), "Betrug (−)", HELLROT)]),
    *zwei([("folge", "sorge"), ("dispo", "ruhig"), ("kein", "denkt")], [("folge", "ruhig"), ("melk", "denkt"), ("kein", "ernst")]),
]))

# ===========================================================================================================================
# G1 Korrektur: individueller Schadenseinschlag (BGHSt 16, 321, Leitsatz a–c; BGH 3 StR 171/17)
# ===========================================================================================================================
PI = f"{PS_} › Korrektur: individueller Schadenseinschlag"
folie([("indiv", f"{PI}"), ("i1", f"{PI} › a) Zweck verfehlt"), ("i2", f"{PI} › b) Folgemaßnahmen"),
       ("i3", f"{PI} › c) Mittel der Lebensführung"), ("i4", f"{PI} › im Fall (−)")], rechts_frei([
    *tafel("indiv", "Individueller Schadenseinschlag"),
    pl("1. Korrektur", 110, 180, beim("indiv", "Erstens"), fill=WEISS, size=30),
    pl("auch bei gleichem Wert ein Schaden, wenn …", 355, 180, beim("indiv", "Auch"), fill=GELB, size=30),
    z("a) die Sache nicht zum vertraglich vorausgesetzten", 110, 260, "i1", "Bold", 30),
    z("Zweck und nicht anders zumutbar verwendbar ist", 150, 302, beim("i1", "auch"), "Bold", 30),
    z("b) die Verpflichtung zu vermögensschädigenden", 110, 365, "i2", "Bold", 30),
    z("Maßnahmen zwingt, etwa zu einem teuren Kredit", 150, 407, beim("i2", "Maßnahmen"), "Bold", 30),
    z("c) die Mittel für eine angemessene Lebensführung fehlen", 110, 470, "i3", "Bold", 30),
    zit("BGHSt 16, 321 (Leitsatz a–c); BGH 3 StR 171/17", 110, 525, beim("i3", "fehlen")),
    blk(110, 600, 1040, 175, HELLGRUEN, "i4", [("Hier nicht:", "ExtraBold", 32, INK),
                                              ("Gundula liest im Sessel, hat bar gezahlt", "Bold", 30, INK),
                                              ("und kommt weiter gut zurecht", "Bold", 30, INK)]),
    *neinz("individueller Schadenseinschlag", 805, beim("i4", "kommt"), "ExtraBold", 32, x=170),
    *requisit([("indiv", (FE, "white-question-mark", 80, WEISS), "trotz gleichem Wert?", GELB),
               ("i1", ("tabler", "armchair", 130, SESSEL), "Zweck verfehlt?", WEISS),
               ("i2", ("tabler", "credit-card", 130, BLAU), "teurer Kredit?", WEISS),
               ("i3", ("ph", "wallet", 110, GELB), "Mittel fehlen?", WEISS),
               ("i4", (FE, "books", 120, BLAU), "Gundula liest darin", HELLGRUEN)]),
    *stehend("GU", FX, [("indiv", "denkt"), ("i1", "ruhig"), ("i4", "froh")]),
]))

# ===========================================================================================================================
# G2 Korrekturen: Eingehungsschaden (BGH 1 StR 13/18 Rn. 9), Gefährdungsschaden (BVerfG 2 BvR 2500/09 Rn. 174–176)
# ===========================================================================================================================
folie([("eing", f"{PS_} › Eingehungsschaden"), ("gef", f"{PS_} › Gefährdungsschaden"),
       ("gef2", f"{PS_} › Gefährdungsschaden beziffern")], rechts_frei([
    *tafel("eing", "Weitere Korrekturen"),
    blk(110, 180, 1040, 175, BLAU, "eing", [("2. Eingehungsschaden:", "ExtraBold", 32, INK),
                                           ("schon beim Vertragsschluss, wenn der Anspruch", "Bold", 30, INK),
                                           ("weniger wert ist als die eigene Verpflichtung", "Bold", 30, INK)]),
    zit("BGH 1 StR 13/18 Rn. 9", 130, 370, beim("eing", "Eingehungsschaden")),
    blk(110, 440, 1040, 175, LILA, "gef", [("3. Gefährdungsschaden:", "ExtraBold", 32, INK),
                                          ("konkrete Gefahr eines künftigen Verlusts", "Bold", 30, INK),
                                          ("mindert das Vermögen schon gegenwärtig", "Bold", 30, INK)]),
    zit("BVerfG 2 BvR 2500/09 Rn. 174 f.; 2 BvR 2559/08 Rn. 136 f.", 130, 630, beim("gef", "mindern")),
    *okz("auch er muss der Höhe nach beziffert werden", 700, "gef2", "Bold", 32, x=170),
    zit("BVerfG 2 BvR 2500/09 Rn. 176; 2 BvR 2559/08 Rn. 150", 170, 760, beim("gef2", "beziffert")),
    *requisit([("eing", (FE, "handshake", 120, GELB), "Vertragsschluss", BLAU),
               ("gef", (FE, "warning", 110, GELB), "konkrete Gefahr", LILA),
               ("gef2", ("tabler", "calculator", 100, WEISS), "beziffern", WEISS)]),
    *zwei([("eing", "ruhig"), ("gef", "denkt")], [("eing", "ruhig"), ("gef2", "ernst")]),
]))

# ===========================================================================================================================
# H Gegenfall: nur 120 € wert → Schaden 180 €
# ===========================================================================================================================
els_g0, _, _ = waage(WX, 330, "gegen", bis="grech")       # Waage leer im Gleichgewicht, bis die Werte kommen
els_g, (glx, gly), (grx, gry) = waage(WX, 355, "grech", neig=40)
PG = "Gegenfall › Sessel nur 120 € wert"
folie([("gegen", "Gegenfall › anderes Gutachten"), ("u2", "Gegenfall › Ulla: „nur 120 € wert“"),
       ("grech", f"{PG}: 300 € hingegeben"), ("grech2", f"{PG}: Schaden 180 €"),
       ("gerg", f"{PG}: mit Vorsatz und Bereicherungsabsicht Tatbestand (+)")], rechts_frei([
    *tafel("gegen", "Gegenfall: nur 120 € wert"),
    pl("Angenommen: ein anderes Gutachten", 110, 180, beim("gegen", "Angenommen"), fill=LILA, size=30),
    pl("Wert: nur 120 €", 110, 255, beim("u2", "hundertzwanzig"), fill=ROT, size=30),
    *els_g0,
    *els_g,
    auf_tafel(geld("grech", glx, gly, breite=170)),
    pl("gegeben: 300 €", glx, gly + 70, "grech", fill=GRUEN, size=30, anker="m"),
    auf_tafel(sessel(beim("grech", "erhält"), grx, gry, breite=150)),
    pl("erhalten: 120 €", grx, gry + 70, beim("grech", "erhält"), fill=WEISS, size=30, anker="m"),
    gleichung("300 € − 120 € = 180 €", WX, 735, "grech2"),
    *okz("mit Vorsatz und Bereicherungsabsicht: Betrugstatbestand (+)", 825, "gerg", "Bold", 30, x=170),
    *fig("UL", FX, FB, FR, [("gegen", "ruhig")], bis="u2"),
    *redet("UL_redet", FX, FB, FR, "u2", "grech"),
    *fig("UL", FX, FB, FR, [("grech", "ruhig"), ("grech2", "ernst")], erst="cut"),
    ns(NAME["UL"], FX, FB, "gegen", NFARBE["UL"], d=0.1),
    blase("sprech", 560, 200, "u2", 1560, 210, inhalt=["Dieser Nachbau ist", "nur 120 € wert."], textsize=38,
          figur=("UL_redet", FX, FB, FR), bis="grech"),
    pl("Schaden: 180 €", PX, PY, "grech2", fill=HELLROT, size=30, anker="m"),
]))

# ===========================================================================================================================
# I Versuch, § 263 Abs. 2 StGB: scheidet im Ausgangsfall aus (keine Vorstellung von einem Schaden, § 22 StGB)
# ===========================================================================================================================
wv, wv_y = wortlaut(80, 175, 1100, "„Der Versuch ist strafbar.“", "§ 263 Abs. 2 StGB", "versuch",
                   marken=[("Versuch", beim("versuch", "Versuch"))], size=32)
folie([("versuch", "Versuch, § 263 Abs. 2 StGB › im Ausgangsfall (−)")], rechts_frei([
    *tafel("versuch", "Versuch, § 263 Abs. 2 StGB"),
    *wv,
    *neinz("Versuch scheidet im Ausgangsfall aus:", wv_y + 50, beim("versuch", "scheidet"), "ExtraBold", 32, x=170),
    z("Alwin hält 300 € für den richtigen Preis", 170, wv_y + 105, beim("versuch", "Alwin"), "Bold", 32),
    z("einen Schaden stellt er sich gar nicht vor", 170, wv_y + 160, beim("versuch", "Schaden"), "Bold", 32),
    zit("§ 22 StGB: „nach seiner Vorstellung von der Tat“", 170, wv_y + 220, beim("versuch", "Schaden")),
    *stehend("AL", FX, [("versuch", "ruhig"), (beim("versuch", "Alwin"), "denkt")]),
    blase("denk", 440, 170, beim("versuch", "Alwin"), 1500, 230, inhalt=["300 € sind der", "richtige Preis"], textsize=34,
          figur=("AL_denkt", FX, FB, FR)),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi): Schaden immer beziffern
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Schaden beziffern", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Beziffere den Schaden immer.", 200, 200, "tipp", "ExtraBold", 34),
         z("Rechnung hinschreiben: Leistung − Gegenleistung,", 230, 275, "tipp2", "Bold", 30),
         z("in Euro", 230, 317, beim("tipp2", "Euro"), "Bold", 30),
         z("das verlangt das BVerfG von den Strafgerichten,", 230, 395, "tipp3", "Bold", 30),
         z("außer in einfach gelagerten Fällen", 230, 437, beim("tipp3", "außer"), "Bold", 30),
         zit("BVerfG 2 BvR 2500/09 Rn. 176; 2 BvR 2559/08 Rn. 112", 230, 490, beim("tipp3", "außer")),
         pl("Urteil ohne Wert: unsere Folge zur Sachrüge", 200, 565, "v204", fill=WEISS, size=28),
         blk(200, 665, 940, 130, GELB, "tipp4", [("nichts übrig:", "ExtraBold", 32, INK),
                                                ("kein Schaden, kein vollendeter Betrug", "Bold", 30, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Schaden immer beziffern"), ("tipp2", "Klausurtipp › Leistung − Gegenleistung, in Euro"),
       ("tipp3", "Klausurtipp › Bezifferung: BVerfG"), ("v204", "Klausurtipp › Urteil ohne Wert: Folge zur Sachrüge"),
       ("tipp4", "Klausurtipp › nichts übrig: kein Schaden")], els_k)

# ===========================================================================================================================
# K Prüfschema Vermögensschaden (breite Karte), Punkt für Punkt
# ===========================================================================================================================
PSCH = "Prüfschema Vermögensschaden"
folie([("sch", PSCH), ("s1", f"{PSCH} › 1. Vermögen vor der Verfügung"), ("s2", f"{PSCH} › 2. Vermögen danach, samt Gegenleistung"),
       ("s3", f"{PSCH} › 3. Differenz in Euro"), ("s4", f"{PSCH} › 4. Korrekturen")], [
    karte(60, 60, 1800, 840, "sch"),
    titel("Prüfschema: Vermögensschaden, § 263 Abs. 1 StGB", 110, 100, "sch", 46),
    z("1. Vermögenswert unmittelbar vor der Verfügung", 130, 220, "s1", "ExtraBold", 36, rechts=1820),
    z("2. Vermögenswert unmittelbar danach, samt Gegenleistung", 130, 320, "s2", "ExtraBold", 36, rechts=1820),
    z("3. Differenz, in Euro beziffert", 130, 420, "s3", "ExtraBold", 36, rechts=1820),
    z("4. Korrekturen prüfen:", 130, 520, "s4", "ExtraBold", 36, rechts=1820),
    z("a) individueller Schadenseinschlag", 190, 590, beim("s4", "individuellen"), "Bold", 34, rechts=1820),
    z("b) Eingehungsschaden", 190, 650, beim("s4", "Eingehungs"), "Bold", 34, rechts=1820),
    z("c) Gefährdungsschaden", 190, 710, beim("s4", "Gefährdungsschaden"), "Bold", 34, rechts=1820),
    ficon(FE, "balance-scale", 1600, 470, 200, "sch", fuell=GELB),
    ficon("tabler", "calculator", 1600, 760, 150, "s3", fuell=WEISS),
])

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Täuschung allein ist ", 0), ("kein Schaden", "a"), (".", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "kein")}),
    *markertext([[("Entscheidend ist der Vergleich", 0)], [("vor und nach", "b"), (" der Verfügung,", 0)],
                 [("und am Ende steht eine ", 0), ("Zahl in Euro", "c"), (".", 0)]], 750, 460, 44, "mk2",
                {"b": beim("mk2", "vor"), "c": beim("mk2", "Zahl")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
