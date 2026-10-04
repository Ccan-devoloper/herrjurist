"""Folge 199 · Tanken ohne Geld – der Tankstellenfall: Vertrag an der Zapfsäule? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall nach BGH, Urt. v. 4.5.2011 – VIII ZR 171/10: Armin tankt an Säule 4 für 80 €, an der Kasse liegt sein
Portemonnaie zu Hause; Pächterin Margarete. Szenen laut ../SZENENPLAN.md.
DARSTELLUNG: Tankstelle fiktiv, ohne Marke und Logo; Armin sympathisch (vergessen, kein Betrug); keine Anleitung zum Tankbetrug.
Zwei Handlungsgeräusche (Zapfen beim Tanken, Türglocke beim Betreten des Shops; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 196 (gemeinsame Dateien unverändert); neu: boden_(), dach(), theke(), regal().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_199/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_199/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149/196) ------------------------------------
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
NAME = {"AR": "Armin", "MA": "Margarete"}
NFARBE = {"AR": GELB, "MA": GRUEN}


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


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


def zwei(folge1, folge2):
    """Armin (links) und Margarete (rechts) neben der Tafel, beide blicken nach links zur Tafel."""
    return [*stehend("AR", X1, folge1), *stehend("MA", X2, folge2)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
HELLGRAU_ = (226, 226, 222, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    """Boden in Seitenansicht: Tuschelinie, optional Fläche darunter."""
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def dach(x0, x1, y, unten, c):
    """Tankstellendach (ohne Marke): flache Platte auf zwei Stützen (Grundformen)."""
    w, h = x1 - x0, unten - y
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    for sx in (60, w - 90):
        dr.rectangle((sx, 50, sx + 30, h - 2), fill=HELLGRAU_, outline=INK, width=5)
    dr.rounded_rectangle((0, 0, w - 1, 64), 14, fill=WEISS, outline=INK, width=5)
    dr.line((20, 44, w - 20, 44), fill=INK, width=3)
    return El(im, x0, y, c, "cut", 0.0, None, name="dach")


def theke(x0, x1, y, unten, c):
    """Kassentheke (Holz, Tuschekontur)."""
    im = Image.new("RGBA", (x1 - x0, unten - y))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, x1 - x0 - 1, unten - y - 1), fill=HOLZ, outline=INK, width=5)
    dr.rectangle((0, 0, x1 - x0 - 1, 26), fill=(190, 135, 90, 255), outline=INK, width=5)
    return El(im, x0, y, c, "cut", 0.0, None, name="theke")


def regal(x0, x1, y, unten, c, boeden=3):
    """Shop-Regal mit Böden (Grundformen); Waren als Icons darauf."""
    w, h = x1 - x0, unten - y
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, w - 1, h - 1), fill=(240, 236, 228, 255), outline=INK, width=5)
    for i in range(1, boeden + 1):
        yy = int(i * h / (boeden + 1))
        dr.line((0, yy, w, yy), fill=INK, width=5)
    return El(im, x0, y, c, "cut", 0.0, None, name="regal")


# ===========================================================================================================================
# A1 Fall: an der Zapfsäule (Hook, Armin tankt, geht zur Kasse, Portemonnaie vergessen)
# ===========================================================================================================================
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
AX = 1180                                    # Armin an der Säule
folie([(NULL, "Fall · Du tankst für 80 €"), ("armin", "Fall · Armin an Säule 4"), ("kasse", "Fall · Ab zur Kasse"),
       ("a1", "Fall · Armin: Portemonnaie vergessen")], [
    hart(boden_(G0, NULL)),
    hart(dach(120, 1080, 380, G0, NULL)),
    hart(ficon("tabler", "gas-station", 330, G0 + 4, 230, NULL, fuell=ROT, anim="cut")),
    hart(pl("4", 330, 560, NULL, fill=WEISS, size=34, anker="m")),
    hart(ficon("tabler", "car", 760, G0 + 4, 400, NULL, fuell=BLAU, anim="cut")),
    pl("80,00 €", 330, 470, beim("fall", "achtzig"), fill=GELB, size=36, anker="m"),
    ficon("tabler", "wallet-off", 760, 260, 120, beim("fall", "Portemonnaie"), fuell=HELLROT),
    pl("Portemonnaie: zu Hause", 760, 290, beim("fall", "Portemonnaie"), fill=HELLROT, size=30, anker="m"),
    pl("Samstagmorgen", 70, 30, beim("armin", "Samstagmorgen"), fill=GELB, size=32),
    *fig("AR", AX, G0, FHA, [(beim("armin", "Armin"), "froh"), ("kasse", "ruhig_r"), ("tasche", "sorge_r")], bis="a1"),
    ns("Armin", AX, G0, beim("armin", "Armin"), GELB, d=0.1),
    pl("Selbstbedienungstankstelle", 410, 30, beim("saeule", "Selbstbedienungstankstelle"), fill=WEISS, size=32),
    szene(ficon("tabler", "droplet", 520, 640, 70, beim("saeule", "tankt"), fuell=GELB), "199zapfen*", 0.5, 0.0),
    szene(ficon("tabler", "building-store", 1640, G0 + 4, 300, beim("kasse", "Shop"), fuell=HELLBLAU), "199klingel*", 0.45, 0.0),
    pl("Shop · Kasse", 1640, 540, beim("kasse", "Shop"), fill=WEISS, size=30, anker="m"),
    *redet("AR_klagt_r", AX, G0, FHA, "a1", "marg"),
    blase("sprech", 860, 230, "a1", 1500, 190, inhalt=["Oh nein! Mein Portemonnaie liegt", "noch zu Hause auf dem Küchentisch."],
          textsize=34, figur=("AR_klagt_r", AX, G0, FHA)),
])

# ===========================================================================================================================
# A2 Fall: im Shop an der Kasse – Margarete, Armins Frage, die Rechtsfrage
# ===========================================================================================================================
MX, AX2 = 860, 1500                          # Margarete hinter der Theke (blickt nach rechts), Armin (blickt nach links)
folie([("marg", "Fall · An der Kasse: Pächterin Margarete"), ("g1", "Fall · Margarete: 80 € an Säule 4"),
       ("a2", "Fall · Armin: schon gekauft?"), ("frage", "Fall · Die Frage"), ("bgh", "Fall · Der Tankstellenfall des BGH")], [
    boden_(G0, "marg", fill=(236, 230, 220, 255), h=100),
    regal(90, 470, 440, G0, "marg"),
    ficon("tabler", "candy", 170, 535, 80, "marg", fuell=PINK, anim="cut"),
    ficon("tabler", "candy", 280, 535, 80, "marg", fuell=GELB, anim="cut"),
    ficon("tabler", "candy", 390, 535, 80, "marg", fuell=GRUEN, anim="cut"),
    ficon("tabler", "bottle", 180, 650, 80, "marg", fuell=BLAU, anim="cut"),
    ficon("tabler", "bottle", 280, 650, 80, "marg", fuell=BLAU, anim="cut"),
    ficon("tabler", "bottle", 380, 650, 80, "marg", fuell=BLAU, anim="cut"),
    *fig("MA", MX, G0, FHA, [(beim("marg", "Margarete"), "ruhig_r")], bis="g1"),
    *redet("MA_redet_r", MX, G0, FHA, "g1", "a2"),
    *fig("MA", MX, G0, FHA, [("a2", "denkt_r"), ("frage", "ruhig_r")], erst="cut"),
    theke(600, 1120, 700, G0, "marg"),
    ficon("ph", "cash-register", 1010, 704, 130, "marg", fuell=WEISS, anim="cut"),
    ns("Margarete", MX, G0, beim("marg", "Margarete"), GRUEN, d=0.1),
    pl("Pächterin", 70, 30, beim("marg", "Pächterin"), fill=GRUEN, size=32),
    pl("Säule 4: 80,00 €", 1215, 560, beim("g1", "Säule"), fill=GELB, size=30, anker="m"),
    *fig("AR", AX2, G0, FHA, [("marg", "sorge")], bis="a2"),
    ns("Armin", AX2, G0, "marg", GELB),
    *redet("AR_redet", AX2, G0, FHA, "a2", "frage"),
    *fig("AR", AX2, G0, FHA, [("frage", "denkt"), ("bgh", "ruhig")], erst="cut"),
    blase("sprech", 900, 230, "g1", 900, 230, inhalt=["80 € an Säule 4. Das Benzin", "ist aber schon in Ihrem Tank."],
          textsize=34, figur=("MA_redet_r", MX, G0, FHA), bis="a2"),
    blase("sprech", 960, 230, "a2", 1200, 220, inhalt=["Heißt das, ich habe schon gekauft?", "Bezahlt wird doch erst hier an der Kasse."],
          textsize=34, figur=("AR_redet", AX2, G0, FHA), bis="frage"),
    pl("Kaufvertrag schon an der Zapfsäule oder erst an der Kasse?", 70, 100, "frage", fill=PINK, size=32),
    pl("Wem gehört das Benzin im Tank?", 70, 170, "frage2", fill=PINK, size=32),
    pl("BGH, Urt. v. 4.5.2011 – VIII ZR 171/10", 70, 240, beim("bgh2", "vierten"), fill=GELB, size=32),
    zit("NJW 2011, 2871", 80, 308, beim("bgh2", "vierten")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_199(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_199("sv", [
    "Samstagmorgen an einer Selbstbedienungstankstelle: Armin tankt an Säule 4 seinen Kombi voll, für 80 €. Dann geht er "
    "in den Shop zur Kasse und merkt, dass sein Portemonnaie zu Hause auf dem Küchentisch liegt. Er will bezahlen, kann "
    "es aber gerade nicht.",
    "Pächterin Margarete verkauft den Kraftstoff im eigenen Namen. Sie sagt: „80 € an Säule 4. Das Benzin ist aber schon "
    "in Ihrem Tank.“",
    "Armin fragt: „Heißt das, ich habe schon gekauft? Bezahlt wird doch erst hier an der Kasse.“",
], "Wann ist der Kaufvertrag geschlossen – und wem gehört das Benzin?")

# ===========================================================================================================================
# C Angebot und Annahme: zwei Deutungen (Wortlautkarte § 145 BGB)
# ===========================================================================================================================
W145 = umbruch("„Wer einem anderen die Schließung eines Vertrags anträgt, ist an den Antrag gebunden, es sei denn, dass er "
               "die Gebundenheit ausgeschlossen hat.“", 32, 1040)
_z45 = lambda wort: next(i for i, t in enumerate(W145) if wort in t)
w145, w145_y = wortlaut(80, 285, 1100, W145, "§ 145 BGB", beim("p145", "Paragraf"),
                        marken=[(_z45("anträgt"), "anträgt", beim("p145", "anträgt")),
                                (_z45("gebunden"), "gebunden", beim("p145", "gebunden"))], size=32)
PC = "Anspruch: § 433 Abs. 2 BGB › Kaufvertrag?"
folie([("ansp", "Anspruch: § 433 Abs. 2 BGB"), ("vert", PC), ("p145", f"{PC} › Angebot, § 145 BGB"),
       ("zwei", f"{PC} › zwei Deutungen"), ("d1", f"{PC} › 1. Säule = Angebot, Tanken = Annahme"),
       ("d2", f"{PC} › 2. Säule = Einladung, Angebot an der Kasse")], rechts_frei([
    *tafel("ansp", "Kaufvertrag: wann?"),
    z("Margarete verlangt 80 € aus § 433 Abs. 2 BGB", 110, 180, "ansp", "Bold", 32),
    z("Voraussetzung: Kaufvertrag = Angebot + Annahme", 110, 228, "vert", "Bold", 32),
    *w145,
    z("Zwei Deutungen kommen in Betracht:", 110, w145_y + 22, "zwei", "Bold", 32),
    blk(110, w145_y + 80, 505, 220, HELLBLAU, "d1", [("1. Zapfsäule:", "Bold", 30, INK), ("betriebsbereite Säule", "ExtraBold", 31, INK),
                                                  ("= Angebot,", "ExtraBold", 31, INK), ("Tanken = Annahme", "ExtraBold", 31, INK)]),
    blk(645, w145_y + 80, 505, 220, LILA, "d2", [("2. Kasse:", "Bold", 30, INK), ("Säule lädt nur ein,", "ExtraBold", 31, INK),
                                              ("Angebot erst an der", "ExtraBold", 31, INK), ("Kasse (Supermarkt)", "ExtraBold", 31, INK)]),
    *requisit([("ansp", ("tabler", "coin-euro", 110, GELB), "80 €", GELB),
               ("d1", ("tabler", "gas-station", 120, ROT), "Zapfsäule = Angebot?", HELLBLAU),
               ("d2", ("ph", "cash-register", 120, WEISS), "erst an der Kasse?", LILA)]),
    *zwei([("ansp", "ruhig"), ("d1", "denkt"), ("d2", "froh")], [("ansp", "ernst"), ("vert", "ruhig"), ("d1", "froh"), ("d2", "denkt")]),
]))
assert w145_y + 300 <= 930, w145_y

# ===========================================================================================================================
# D Der Fall des BGH: Landgericht und BGH
# ===========================================================================================================================
PD = "BGH, 4.5.2011 – VIII ZR 171/10"
folie([("urteil", f"{PD} › der Fall"), ("detek", f"{PD} › Detektivkosten"), ("lg", f"{PD} › Landgericht: §§ 145, 151 BGB"),
       ("bghja", f"{PD} › Kaufvertrag schon mit dem Tanken"), ("nkasse", f"{PD} › nicht erst an der Kasse")], rechts_frei([
    *tafel("urteil", "Der Fall des BGH"),
    z("Kunde tankt Diesel für 10,01 €", 110, 180, beim("urteil", "Kunde"), "Bold", 32),
    z("zahlt an der Kasse nur einen Schokoriegel", 110, 228, "riegel", "Bold", 32),
    z("und 2 Vignetten", 110, 272, beim("riegel", "zwei"), "Bold", 32),
    z("Betreiberin lässt ihn ermitteln, verlangt die Kosten", 110, 330, "detek", "Bold", 32),
    zit("BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 2, 3", 110, 376, "detek"),
    blk(110, 425, 1040, 130, HELLBLAU, "lg", [("Landgericht: betriebsbereite Zapfsäule = Angebot,", "Bold", 30, INK),
                                           ("Tanken = Annahme (§§ 145, 151 BGB)", "ExtraBold", 31, INK)]),
    zit("LG Traunstein, 7.7.2010 – 5 S 2956/09, wiedergegeben in BGH Rn. 8", 110, 565, "lg"),
    blk(110, 615, 1040, 130, GRUEN, "bghja", [("BGH bestätigt das Ergebnis:", "Bold", 30, INK),
                                           ("Kaufvertrag schon mit dem Tanken", "ExtraBold", 33, INK)]),
    zit("BGH, a. a. O., Rn. 11, 13 (Leitsatz 1)", 110, 755, "bghja"),
    *neinz("nicht erst an der Kasse (Rn. 14)", 800, "nkasse", "Bold", 32, x=160),
    ficon("tabler", "gas-station", 1560, 330, 170, "urteil", fuell=ROT),
    pl("Diesel: 10,01 €", 1560, 370, beim("urteil", "zehn"), fill=GELB, size=30, anker="m"),
    ficon("tabler", "candy", 1440, 560, 110, "riegel", fuell=PINK),
    pl("Schokoriegel + 2 Vignetten", 1560, 590, "riegel", fill=WEISS, size=28, anker="m", bis="detek"),
    ficon("ph", "detective", 1690, 560, 120, "detek", fuell=LILA),
    pl("Detektivbüro", 1560, 590, "detek", fill=LILA, size=28, anker="m"),
    ficon("tabler", "gavel", 1560, 840, 140, "bghja", fuell=HOLZ),
    pl("BGH: Vertrag an der Säule", 1560, 870, "bghja", fill=GRUEN, size=28, anker="m"),
]))

# ===========================================================================================================================
# E Die Gründe: Supermarkt und Tankstelle
# ===========================================================================================================================
PE = "Kaufvertrag beim Tanken › Gründe"
folie([("gr", PE), ("laden", f"{PE} › Supermarkt: zurücklegen möglich"), ("tank", f"{PE} › Benzin: praktisch unumkehrbar"),
       ("betr", f"{PE} › Betreiber: Besitz schon verschafft"), ("kunde", f"{PE} › redlicher Kunde: will behalten"),
       ("obj", f"{PE} › objektiver Beobachter"), ("armfalsch", "Ergebnis · Armin hat schon gekauft")], rechts_frei([
    *tafel("gr", "Warum schon an der Zapfsäule?"),
    blk(110, 180, 505, 190, HELLBLAU, "laden", [("Supermarkt:", "Bold", 30, INK), ("Ware zurück ins Regal;", "ExtraBold", 31, INK),
                                             ("Herausnehmen bindet nicht", "ExtraBold", 30, INK)]),
    blk(645, 180, 505, 190, GELB, "tank", [("Tankstelle:", "Bold", 30, INK), ("Benzin im Tank: praktisch", "ExtraBold", 30, INK),
                                        ("nicht zurückzugeben", "ExtraBold", 31, INK)]),
    zit("BGH, a. a. O., Rn. 15, 16 („praktisch unumkehrbarer Zustand“)", 110, 385, "tank"),
    *okz("Betreiber: hat den Besitz schon verschafft,", 445, "betr", "Bold", 31, x=160),
    z("ohne Vertrag dazu in der Regel nicht bereit", 160, 490, beim("betr", "ohne"), size=30),
    *okz("redlicher Kunde: will das Benzin behalten dürfen,", 555, "kunde", "Bold", 31, x=160),
    z("unabhängig davon, ob der Betreiber an der Kasse mitmacht", 160, 600, beim("kunde", "ohne"), size=29),
    blk(110, 665, 1040, 130, GRUEN, "obj", [("Objektiver Beobachter: Vertrag mit dem Einfüllen,", "Bold", 30, INK),
                                         ("keine weitere Erklärung an der Kasse nötig", "ExtraBold", 31, INK)]),
    zit("BGH, a. a. O., Rn. 16", 110, 805, "obj"),
    *requisit([("laden", ("tabler", "basket", 110, LILA), "Supermarkt", HELLBLAU),
               ("tank", ("tabler", "droplet", 90, GELB), "Benzin im Tank", GELB),
               ("betr", ("tabler", "gas-station", 120, ROT), "Besitz verschafft", WEISS),
               ("kunde", ("tabler", "car", 150, BLAU), "behalten dürfen", WEISS),
               ("armfalsch", ("tabler", "receipt-euro", 100, WEISS), "Armin hat schon gekauft", GRUEN)]),
    *zwei([("gr", "ruhig"), ("laden", "denkt"), ("kunde", "froh"), ("armfalsch", "staunt")],
          [("gr", "ruhig"), ("betr", "ernst"), ("obj", "froh")]),
]))

# ===========================================================================================================================
# F1 Eigentum: § 929 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W929 = umbruch("„Zur Übertragung des Eigentums an einer beweglichen Sache ist erforderlich, dass der Eigentümer die Sache dem "
               "Erwerber übergibt und beide darüber einig sind, dass das Eigentum übergehen soll.“", 32, 1040)
_z29 = lambda wort: next(i for i, t in enumerate(W929) if wort in t)
w929, w929_y = wortlaut(80, 265, 1100, W929, "§ 929 Satz 1 BGB", beim("abstr", "Paragraf"),
                        marken=[(_z29("übergibt"), "übergibt", beim("w929", "übergibt")),
                                (_z29("einig"), "einig", beim("w929", "einig"))], size=32)
PF = "Eigentum am Benzin: § 929 Satz 1 BGB"
folie([("eig", "Eigentum am Benzin?"), ("abstr", f"{PF}"), ("ueberg", f"{PF} › Übergabe (+)"),
       ("einig", f"{PF} › Einigung: schon beim Tanken?")], rechts_frei([
    *tafel("eig", "Wem gehört das Benzin?"),
    z("Kaufvertrag verpflichtet nur (§ 433 Abs. 1 BGB);", 110, 175, "abstr", "Bold", 31),
    z("Eigentum: eigene Übereignung", 110, 218, beim("abstr", "Übereignung"), "Bold", 31),
    *w929,
    *okz("Übergabe: mit dem Tanken", w929_y + 30, "ueberg", "Bold", 32, x=160),
    blk(110, w929_y + 100, 1040, 80, PINK, "einig", [("Einigung: schon beim Tanken?", "ExtraBold", 33, INK)]),
    *requisit([("eig", ("tabler", "droplet", 90, GELB), "Wem gehört das Benzin?", PINK),
               ("ueberg", ("tabler", "car", 150, BLAU), "Übergabe (+)", GRUEN),
               ("einig", ("tabler", "users", 110, LILA), "einig?", PINK)]),
    *zwei([("eig", "denkt"), ("ueberg", "ruhig"), ("einig", "denkt")], [("eig", "ruhig"), ("abstr", "ernst"), ("einig", "denkt")]),
]))
assert w929_y + 190 <= 930, w929_y

# ===========================================================================================================================
# F2 Eigentum: Meinungsstand
# ===========================================================================================================================
PM = "§ 929 Satz 1 › Einigung: Meinungsstand"
folie([("offen", f"{PM} › BGH: offen"), ("m1", f"{PM} › Ansicht 1: schon beim Einfüllen"),
       ("m2", f"{PM} › Ansicht 2: erst mit Bezahlung"), ("m3", f"{PM} › Eigentumsvorbehalt oder Bedingung"),
       ("misch", f"{PM} › Vermischung, § 948 BGB"), ("egal", "Eigentum › für die Zahlungspflicht egal")], rechts_frei([
    *tafel("offen", "Eigentum: Meinungsstand"),
    z("BGH: offen – „jedenfalls“ den Besitz verschafft", 110, 175, "offen", "Bold", 31),
    zit("BGH, a. a. O., Rn. 16", 110, 220, "offen"),
    blk(110, 270, 1040, 120, HELLBLAU, "m1", [("Ansicht 1: Eigentum schon", "Bold", 30, INK),
                                           ("mit dem Einfüllen", "ExtraBold", 32, INK)]),
    zit("OLG Düsseldorf, NStZ 1982, 249", 110, 398, "m1"),
    blk(110, 445, 1040, 120, LILA, "m2", [("Ansicht 2: Ware gegen Geld – Eigentum", "Bold", 30, INK),
                                       ("erst mit der Bezahlung", "ExtraBold", 32, INK)]),
    zit("OLG Hamm, NStZ 1983, 266; OLG Koblenz, Urt. v. 10.8.1998 – 2 Ss 206/98", 110, 573, "m2"),
    z("stillschweigender Eigentumsvorbehalt oder", 160, 620, "m3", size=30),
    z("Einigung unter der Bedingung der Zahlung", 160, 662, beim("m3", "Einigung"), size=30),
    z("Vermischung im Tank: ggf. Miteigentum (§§ 948, 947 BGB)", 110, 720, "misch", "Bold", 30),
    blk(110, 785, 1040, 80, GRUEN, "egal", [("Für die Zahlungspflicht: egal", "ExtraBold", 34, INK)]),
    *requisit([("offen", ("tabler", "gavel", 110, HOLZ), "BGH: offen", WEISS),
               ("m1", ("tabler", "droplet", 90, GELB), "schon beim Einfüllen?", HELLBLAU),
               ("m2", ("tabler", "coin-euro", 110, GELB), "Ware gegen Geld", LILA),
               ("egal", ("tabler", "receipt-euro", 100, WEISS), "80 € bleiben geschuldet", GRUEN)]),
    *zwei([("offen", "denkt"), ("m2", "ruhig"), ("egal", "muede")], [("offen", "ruhig"), ("m2", "froh"), ("egal", "ernst")]),
]))

# ===========================================================================================================================
# G Folge: Kaufpreis (Wortlautkarte § 433 Abs. 2 BGB), Fälligkeit, Verzug
# ===========================================================================================================================
W433 = umbruch("„Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu zahlen und die gekaufte Sache "
               "abzunehmen.“", 32, 1040)
_z33 = lambda wort: next(i for i, t in enumerate(W433) if wort in t)
w433, w433_y = wortlaut(80, 170, 1100, W433, "§ 433 Abs. 2 BGB", "w433",
                        marken=[(_z33("Kaufpreis"), "Kaufpreis", beim("w433", "Kaufpreis"))], size=32)
PG = "Folge: Kaufpreis, § 433 Abs. 2 BGB"
folie([("w433", PG), ("faell", f"{PG} › fällig sofort, § 271 Abs. 1 BGB"),
       ("verzug", f"{PG} › Wegfahren: Verzug ohne Mahnung"), ("kosten", f"{PG} › Detektivkosten")], rechts_frei([
    *tafel("w433", "Folge: Armin muss zahlen"),
    *w433,
    *okz("80 € fällig sofort (§ 271 Abs. 1 BGB)", w433_y + 30, "faell", "Bold", 32, x=160),
    zit("BGH, a. a. O., Rn. 17", 160, w433_y + 78, "faell"),
    blk(110, w433_y + 130, 1040, 130, PINK, "verzug", [("Wer wegfährt, ohne zu zahlen: Verzug", "Bold", 31, INK),
                                                    ("auch ohne Mahnung (§ 286 Abs. 2 Nr. 4 BGB)", "ExtraBold", 31, INK)]),
    zit("BGH, a. a. O., Leitsatz 2, Rn. 18–21", 110, w433_y + 270, "verzug"),
    *okz("BGH-Fall: Detektivkosten zu ersetzen", w433_y + 330, "kosten", "Bold", 32, x=160),
    zit("§§ 280 Abs. 1, 2, 286 BGB; BGH, a. a. O., Rn. 23–26", 160, w433_y + 378, "kosten"),
    *requisit([("w433", ("tabler", "coin-euro", 110, GELB), "Kaufpreis: 80 €", GELB),
               ("verzug", ("tabler", "car", 150, BLAU), "wegfahren = Verzug", PINK),
               ("kosten", ("ph", "detective", 120, LILA), "Detektivkosten", WEISS)]),
    *zwei([("w433", "ruhig"), ("verzug", "schreck"), ("kosten", "still")], [("w433", "ernst"), ("faell", "ruhig"), ("kosten", "ernst")]),
]))
assert w433_y + 420 <= 930, w433_y

# ===========================================================================================================================
# H1 Fall: Armin sagt Bescheid (zurück an der Kasse)
# ===========================================================================================================================
folie([("praxis", "Fall · Armin sagt Bescheid"), ("g2", "Fall · Margarete notiert Name und Adresse")], [
    boden_(G0, "praxis", fill=(236, 230, 220, 255), h=100),
    regal(90, 470, 440, G0, "praxis"),
    ficon("tabler", "candy", 170, 535, 80, "praxis", fuell=PINK, anim="cut"),
    ficon("tabler", "candy", 280, 535, 80, "praxis", fuell=GELB, anim="cut"),
    ficon("tabler", "candy", 390, 535, 80, "praxis", fuell=GRUEN, anim="cut"),
    ficon("tabler", "bottle", 180, 650, 80, "praxis", fuell=BLAU, anim="cut"),
    ficon("tabler", "bottle", 280, 650, 80, "praxis", fuell=BLAU, anim="cut"),
    ficon("tabler", "bottle", 380, 650, 80, "praxis", fuell=BLAU, anim="cut"),
    *fig("MA", MX, G0, FHA, [("praxis", "ruhig_r")], bis="g2"),
    *redet("MA_froh_redet_r", MX, G0, FHA, "g2", "keinrs"),
    theke(600, 1120, 700, G0, "praxis"),
    ficon("ph", "cash-register", 1010, 704, 130, "praxis", fuell=WEISS, anim="cut"),
    ficon("tabler", "notes", 760, 704, 100, beim("g2", "notiere"), fuell=WEISS),
    ns("Margarete", MX, G0, "praxis", GRUEN),
    *fig("AR", AX2, G0, FHA, [("praxis", "ernst"), ("g2", "froh")], bis="keinrs"),
    ns("Armin", AX2, G0, "praxis", GELB),
    pl("Armin sagt Bescheid", 70, 30, beim("praxis", "Bescheid"), fill=GELB, size=32),
    blase("sprech", 1000, 230, "g2", 960, 215, inhalt=["Kein Problem. Ich notiere Ihren Namen und Ihre", "Adresse, und Sie bringen das Geld heute noch vorbei."],
          textsize=32, figur=("MA_froh_redet_r", MX, G0, FHA)),
])

# ===========================================================================================================================
# H2 Praxis, Personalausweis, Strafrecht (ein Satz, Verweis Folge 022)
# ===========================================================================================================================
PH = "Praxis und Strafrecht"
folie([("keinrs", f"{PH} › Praxis, kein Rechtssatz"), ("ausw", f"{PH} › kein Personalausweis als Pfand"),
       ("straf", f"{PH} › Armin: nicht strafbar"), ("str2", f"{PH} › ohne Zahlungswillen: Betrug")], rechts_frei([
    *tafel("keinrs", "Praxis und Strafrecht"),
    z("Name und Adresse notieren, Pfand nehmen:", 110, 180, "keinrs", "Bold", 32),
    blk(110, 230, 1040, 80, GELB, beim("keinrs", "Praxis"), [("Praxis, kein Rechtssatz", "ExtraBold", 34, INK)]),
    *neinz("Personalausweis als Pfand: darf die Tankstelle", 360, "ausw", "Bold", 31, x=160),
    z("nicht verlangen (§ 1 Abs. 1 Satz 3 PAuswG)", 160, 405, beim("ausw", "nicht"), "Bold", 31),
    *okz("Armin: nicht strafbar – wollte zahlen,", 485, "straf", "Bold", 31, x=160),
    z("sagt offen Bescheid", 160, 530, beim("straf", "sagt"), "Bold", 31),
    blk(110, 600, 1040, 130, HELLROT, "str2", [("Schon beim Tanken nicht zahlungswillig:", "Bold", 30, INK),
                                            ("grundsätzlich (versuchter) Betrug", "ExtraBold", 32, INK)]),
    zit("BGH, Beschl. v. 10.1.2012 – 4 StR 632/11, Rn. 4, 5", 110, 740, "str2"),
    zit("mehr dazu: Video „Tankbetrug“", 110, 785, beim("str2", "mehr")),
    *requisit([("keinrs", ("tabler", "notes", 100, WEISS), "Praxis", GELB),
               ("ausw", ("tabler", "id-off", 110, HELLROT), "kein Ausweis als Pfand", HELLROT),
               ("straf", ("tabler", "user-check", 110, GRUEN), "nicht strafbar", GRUEN),
               ("str2", ("tabler", "gavel", 110, HOLZ), "Video „Tankbetrug“", WEISS)]),
    *zwei([("keinrs", "ruhig"), ("ausw", "denkt"), ("straf", "froh")], [("keinrs", "ruhig"), ("ausw", "ernst"), ("str2", "ernst")]),
]))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zwei Fragen trennen"), ("tp1", "Klausurtipp · Kaufvertrag: schon mit dem Tanken"),
       ("tp2", "Klausurtipp · Eigentum: gesondert, § 929 BGB"), ("tp3", "Klausurtipp · Abgrenzung Supermarkt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne zwei Fragen:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("1. Wann ist der Kaufvertrag geschlossen?", 200, 285, "tp1", "Bold", 34),
    z("SB-Tankstelle: schon mit dem Tanken", 240, 335, beim("tp1", "An"), size=33),
    z("2. Wann geht das Eigentum über?", 200, 420, "tp2", "Bold", 34),
    z("gesondert bei § 929 BGB prüfen – streitig", 240, 470, beim("tp2", "Das"), size=33),
    linienzug([(130, 555), (1130, 555)], "tp3", breite=3),
    z("Abgrenzung Supermarkt:", 200, 590, "tp3", "Bold", 36),
    z("Herausnehmen aus dem Regal bindet noch nicht", 200, 645, beim("tp3", "Herausnehmen"), size=33),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Anspruch auf den Kaufpreis, § 433 Abs. 2 BGB", True),
          ("c2", 1, "1. Kaufvertrag durch Angebot und Annahme", False),
          ("c3", 1, "2. Zeitpunkt: schon mit dem Tanken, nicht erst an der Kasse", False),
          ("c4", 1, "3. Fälligkeit: sofort (§ 271 Abs. 1 BGB)", False),
          ("c5", 0, "II. Eigentum am Benzin, § 929 Satz 1 BGB", True),
          ("c6", 1, "1. Übergabe: mit dem Tanken", False),
          ("c7", 1, "2. Einigung – streitig: schon beim Einfüllen oder erst mit der Bezahlung?", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Tankstellenfall"), 110, 90, "sch", 46)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 88, 1: 76}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. § 433 Abs. 2 BGB"), ("c2", "Prüfschema › I. 1. Kaufvertrag"),
       ("c3", "Prüfschema › I. 2. Zeitpunkt"), ("c4", "Prüfschema › I. 3. Fälligkeit"),
       ("c5", "Prüfschema › II. Eigentum, § 929 Satz 1 BGB"), ("c6", "Prüfschema › II. 1. Übergabe"),
       ("c7", "Prüfschema › II. 2. Einigung (streitig)")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("An der Selbstbedienungstankstelle", 0)], [("steht der Kaufvertrag schon", 0)],
                 [("mit dem ", 0), ("Tanken", "a"), (".", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Tanken")}),
    *markertext([[("Wer dann nicht zahlen kann,", 0)], [("schuldet den ", 0), ("Kaufpreis", "b"), (" trotzdem.", 0)]],
                750, 600, 46, "mk2", {"b": beim("mk2", "Kaufpreis")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
