"""Folge 099 · Schuldbeitritt, Schuldübernahme oder Bürgschaft? Die Abgrenzung – Serienstandard Open Peeps (Katzenkönig).
Fall: Jochen finanziert ein gebrauchtes Auto mit einem Bankkredit über 18.000 €; seine Freundin Katja schreibt der Bank
„Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro“ und unterschreibt; Jochen bleibt Kreditnehmer.
Szenen laut ../SZENENPLAN.md: A1 Autokredit, A2 Bank (Sicherheit, Erklärung), A3 ein Jahr später (Zahlungsverlangen, Frage),
B Sachverhalt, C Auslegung, D1 § 414 (Wortlaut) und § 415, D2 Folge, § 417, Entlassungswille, D3 Schuldbeitritt,
D4 § 765 Abs. 1 (Wortlaut), §§ 767, 768, 770, 771, D5 § 766 (Wortlaut), E1 Dreispalter, E2 Abgrenzung in 2 Schritten,
F Subsumtion, G Ergebnis (Bühne), H Klausurtipp (Lexi), I Klausurschema, J Merksatz (Lexi).
Zwei Handlungsgeräusche (Unterschrift, Brief; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild
ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als eigene Kopie aus Folge 089 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_099/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_099/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083) ------------------------------------
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
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"JO": "Jochen", "KA": "Katja", "ZO": "Frau Zöllner"}
NFARBE = {"JO": BLAU, "KA": GRUEN, "ZO": LILA}


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


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel EW/TA/SV."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]



def fl(name, cx, folge, bis=None, erst="cut", unten=BODEN, hoehe=FH, d=0.0):
    """Figur auf der Bühne: folge = [(cue, ansicht)] mit Ansichtsnamen ohne Präfix (z. B. 'ruhig_r')."""
    return fig(name, cx, unten, hoehe, folge, bis=bis, erst=erst, d=d)


def plus(cue, sek):
    c, o = cue if isinstance(cue, tuple) else (cue, 0.0)
    return (c, round(o + sek, 3))



# A1 Fall: der Autokredit -------------------------------------------------------------------------------------------------------
JX1, KX1 = 1180, 1640
folie([(NULL, "Fall · Der Autokredit")], [
    hart(pl("Jochen kauft ein gebrauchtes Auto", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "car", 640, BODEN + 22, 470, NULL, fuell=BLAU)),
    pl("für den Weg zur Arbeit", 640, 330, beim("fall", "Weg"), fill=WEISS, size=32, anker="m"),
    *fl("JO", JX1, [(NULL, "ruhig"), ("nur", "froh")]),
    hart(ns("Jochen", JX1, BODEN, NULL, NFARBE["JO"])),
    ficon("tabler", "building-bank", 250, 330, 150, "kredit", fuell=BLAU),
    pl("Kredit: 18.000 €", 250, 350, beim("kredit", "Kredit"), fill=GELB, size=32, anker="m"),
    pl("gehört Jochen, nur er fährt", 640, 405, "nur", fill=GRUEN, size=32, anker="m"),
    *fl("KA", KX1, [("katja", "ruhig")], erst="pop"),
    ns("Katja", KX1, BODEN, "katja", NFARBE["KA"], d=0.1),
    pl("Freundin: verdient gut", KX1, 200, beim("katja", "verdient"), fill=WEISS, size=30, anker="m"),
    pl("braucht kein Auto", KX1, 270, beim("katja", "braucht"), fill=WEISS, size=30, anker="m"),
])

# A2 Fall: die Bank will eine Sicherheit, Katja unterschreibt ---------------------------------------------------------------------
ZX2, JX2, KX2 = 430, 1150, 1600
KHX, KHY = hand("KA_ruhig", KX2, BODEN, FH, -1)
UNT = "unter"
folie([("bank", "Fall · Die Bank will eine Sicherheit"), ("zettel", "Fall · Katja unterschreibt")], [
    pl("Bei der Bank", 70, 30, "bank", fill=GELB, size=44),
    boden("bank"),
    ficon("tabler", "building-bank", 150, 420, 130, "bank", fuell=BLAU),
    ficon("tabler", "desk", 780, BODEN, 300, "bank", fuell=GELB),
    *fl("ZO", ZX2, [("bank", "ruhig_r")], bis="zo1", erst="pop"),
    *redet("ZO_redet_r", ZX2, BODEN, FH, "zo1", "jo1"),
    *fl("ZO", ZX2, [("jo1", "ruhig_r"), (beim("unter", "Bank"), "froh_r")]),
    ns("Frau Zöllner", ZX2, BODEN, "bank", NFARBE["ZO"], d=0.1),
    *fl("JO", JX2, [("bank", "ruhig")], bis="jo1", erst="pop", d=0.1),
    *redet("JO_redet_r", JX2, BODEN, FH, "jo1", "ka1"),
    *fl("JO", JX2, [("ka1", "froh_r"), ("zettel", "ruhig")]),
    ns("Jochen", JX2, BODEN, "bank", NFARBE["JO"], d=0.2),
    *fl("KA", KX2, [("bank", "ruhig")], bis="ka1", erst="pop", d=0.2),
    *redet("KA_redet", KX2, BODEN, FH, "ka1", "zettel"),
    *fl("KA", KX2, [("zettel", "ruhig"), (UNT, "froh")]),
    ns("Katja", KX2, BODEN, "bank", NFARBE["KA"], d=0.3),
    blase("sprech", 730, 240, "zo1", 660, 225, inhalt=["Wir brauchen noch eine Sicherheit.", "Sie bleiben natürlich",
                                                      "unser Kreditnehmer."], textsize=34,
          figur=("ZO_redet_r", ZX2, BODEN, FH), bis="jo1"),
    blase("sprech", 540, 190, "jo1", 1260, 215, inhalt=["Katja, kannst du für mich", "einspringen?"], textsize=34,
          figur=("JO_redet_r", JX2, BODEN, FH), bis="ka1"),
    blase("sprech", 460, 160, "ka1", 1480, 215, inhalt=["Klar, ich helfe dir."], textsize=34,
          figur=("KA_redet", KX2, BODEN, FH), bis="zettel"),
    karte(560, 85, 800, 280, "zettel", fill=WEISS, rund=10, schatten=6, rand=4),
    z("An die Bank:", 595, 105, "zettel", "Bold", 34, rechts=1340),
    z("Ich übernehme die Schulden von Jochen", 595, 160, beim("zettel", "Ich"), size=34, rechts=1340),
    z("aus dem Autokredit über 18.000 Euro.", 595, 210, beim("zettel", "aus"), size=34, rechts=1340),
    linienzug([(930, 335), (1320, 335)], UNT, breite=3),
    szene(z("Katja", 1010, 278, UNT, "ExtraBold", 40, rechts=1340), "099unterschrift*", 0.9, 0.0),
    ficon("tabler", "pencil", KHX - 30, KHY + 30, 70, "zettel", fuell=GELB),
    pl("Bank nimmt an", 180, 475, beim("unter", "Bank"), fill=GRUEN, size=30, anker="m"),
])

# A3 Fall: ein Jahr später – die Bank verlangt Zahlung, die Frage --------------------------------------------------------------
ZX3, KX3, JX3 = 430, 1080, 1660
folie([("spaet", "Fall · Ein Jahr später"), ("frage", "Fall · Die Frage")], [
    pl("Ein Jahr später: Jochen zahlt nicht mehr", 70, 30, "spaet", fill=GELB, size=44, bis="frage"),
    boden("spaet"),
    *fl("JO", JX3, [("spaet", "sorge")], erst="pop"),
    ns("Jochen", JX3, BODEN, "spaet", NFARBE["JO"], d=0.1),
    ficon("tabler", "calendar", JX3, 330, 110, "spaet", fuell=WEISS),
    pl("offen: 12.000 €", JX3, 160, beim("spaet", "Zwölftausend"), fill=ROT, size=32, anker="m"),
    ficon("tabler", "building-bank", 150, 420, 130, "brief", fuell=BLAU),
    *fl("ZO", ZX3, [("brief", "ruhig_r")], bis="zo2", erst="pop"),
    *redet("ZO_redet_r", ZX3, BODEN, FH, "zo2", "ka2"),
    *fl("ZO", ZX3, [("ka2", "denkt_r"), ("frage", "ruhig_r")]),
    ns("Frau Zöllner", ZX3, BODEN, "brief", NFARBE["ZO"], d=0.1),
    szene(ficon("tabler", "mail", 760, 600, 110, beim("brief", "wendet"), fuell=WEISS), "099brief*", 0.8, 0.0),
    *fl("KA", KX3, [("brief", "ruhig")], bis="ka2", erst="pop", d=0.1),
    *redet("KA_redet", KX3, BODEN, FH, "ka2", "frage"),
    *fl("KA", KX3, [("frage", "staunt")]),
    ns("Katja", KX3, BODEN, "brief", NFARBE["KA"], d=0.2),
    blase("sprech", 730, 210, "zo2", 660, 220, inhalt=["Sie haben die Schulden übernommen.", "Bitte zahlen Sie die 12.000 €."],
          textsize=34, figur=("ZO_redet_r", ZX3, BODEN, FH), bis="ka2"),
    blase("sprech", 730, 210, "ka2", 1060, 220, inhalt=["Ich wollte Jochen doch nur helfen,", "den Kredit zu bekommen!"],
          textsize=34, figur=("KA_redet", KX3, BODEN, FH), bis="frage"),
    pl("Was hat Katja da eigentlich unterschrieben?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("Schuldübernahme?", 500, 140, beim("frage2", "Schuldübernahme"), fill=WEISS, size=34, anker="m"),
    pl("Schuldbeitritt?", 900, 140, beim("frage2", "Schuldbeitritt"), fill=WEISS, size=34, anker="m"),
    pl("Bürgschaft?", 1280, 140, beim("frage2", "Bürgschaft"), fill=WEISS, size=34, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------------------
def sachverhalt_099(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_099("sv", [
    "Jochen kauft für den Weg zur Arbeit ein gebrauchtes Auto. Eine Bank finanziert es mit einem Kredit über 18.000 Euro. "
    "Das Auto gehört Jochen, nur er fährt es. Seine Freundin Katja verdient gut, braucht aber kein Auto.",
    "Frau Zöllner von der Bank verlangt eine weitere Sicherheit; Jochen soll Kreditnehmer bleiben. Katja schreibt mit der "
    "Hand an die Bank: „Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro.“ Sie unterschreibt, die "
    "Bank nimmt die Erklärung an.",
    "Ein Jahr später zahlt Jochen die Raten nicht mehr; 12.000 Euro sind offen. Die Bank verlangt sie von Katja.",
], "Was hat Katja unterschrieben, und muss sie zahlen?")

# C Auslegung, §§ 133, 157 -------------------------------------------------------------------------------------------------------
folie([("ausl", "Abgrenzung › Auslegung, §§ 133, 157 BGB")], rechts_frei([
    *tafel("ausl", "Was hat Katja erklärt?"),
    z("nicht allein das Wort „übernehmen“", 110, 190, "ausl", "Bold", 38),
    z("§§ 133, 157 BGB: der wirkliche Wille,", 110, 290, "ausl2", "Bold", 38),
    z("so wie die Bank ihn verstehen durfte", 160, 345, "ausl3", size=38),
    zit("BGH, Versäumnisurt. v. 3.9.2020 – III ZR 56/19, Rn. 19", 160, 405, "ausl3"),
    blk(110, 500, 1040, 120, GELB, "drei", [("3 Rechtsinstitute kommen in Betracht", "ExtraBold", 40, INK)]),
    *requisit([("ausl", ("tabler", "file-text", 100, WEISS), "„Ich übernehme …“", WEISS),
               ("ausl2", ("tabler", "search", 100, WEISS), "wirklicher Wille", WEISS),
               ("drei", ("tabler", "list-numbers", 100, WEISS), "3 Rechtsinstitute", GELB)]),
    *paar("ausl", "KA", [("ausl", "denkt"), ("drei", "ruhig")], "ZO", [("ausl", "ruhig"), ("ausl3", "denkt")]),
]))

# D1 1. befreiende Schuldübernahme: § 414 (Wortlaut), § 415 --------------------------------------------------------------------
W414 = ["„Eine Schuld kann von einem Dritten durch Vertrag mit dem Gläubiger",
        "in der Weise übernommen werden, dass der Dritte an die Stelle des",
        "bisherigen Schuldners tritt.“"]
w414, w414_y = wortlaut(80, 175, 1100, W414, "§ 414 BGB", "w414", marken=[
    (0, "durch Vertrag mit dem Gläubiger", beim("w414", "Vertrag")),
    (1, "an die Stelle des", beim("w414", "Stelle"))], size=32)
folie([("w414", "Abgrenzung › 1. Schuldübernahme, § 414 BGB"), ("p415", "1. Schuldübernahme › § 415 BGB")], rechts_frei([
    *tafel("w414", "1. Befreiende Schuldübernahme"),
    *w414,
    z("§ 415 BGB: Schuldner und Übernehmer vereinbaren,", 110, w414_y + 45, "p415", "Bold", 36),
    z("wirksam erst mit Genehmigung des Gläubigers", 160, w414_y + 100, beim("p415", "Genehmigung"), size=36),
    *requisit([("w414", ("tabler", "arrows-exchange", 110, WEISS), "an die Stelle", WEISS),
               ("p415", ("tabler", "circle-check", 100, GRUEN), "Genehmigung", GRUEN)]),
    *paar("w414", "JO", [("w414", "ruhig"), ("p415", "denkt")], "ZO", [("w414", "ruhig"), ("p415", "denkt")]),
]))

# D2 Folge, § 417, Entlassungswille (BGH VII ZR 13/11) --------------------------------------------------------------------------
folie([("frei", "1. Schuldübernahme › Folge, § 417 BGB"), ("streng", "1. Schuldübernahme › Entlassungswille")], rechts_frei([
    *tafel("frei", "1. Befreiende Schuldübernahme"),
    blk(110, 190, 1040, 110, GRUEN, "frei", [("Folge: Der Altschuldner wird frei", "ExtraBold", 40, INK)]),
    z("§ 417 BGB: Übernehmer kann Einwendungen", 110, 350, "p417", "Bold", 36),
    z("aus dem Verhältnis Gläubiger – Altschuldner", 160, 405, beim("p417", "Verhältnis"), size=36),
    z("erheben", 160, 460, beim("p417", "erheben"), size=36),
    z("Gläubiger verliert seinen Schuldner:", 110, 560, "streng", "Bold", 36),
    z("Wille, ihn zu entlassen, deutlich erkennbar", 160, 615, beim("streng", "Wille"), size=36),
    zit("BGH, Urt. v. 12.4.2012 – VII ZR 13/11, Rn. 7", 160, 675, beim("streng", "Bundesgerichtshof")),
    *requisit([("frei", ("tabler", "user-check", 100, GRUEN), "Altschuldner frei", GRUEN),
               ("p417", ("tabler", "shield", 100, WEISS), "Einwendungen", WEISS),
               ("streng", ("tabler", "user-x", 100, WEISS), "Entlassung?", WEISS)]),
    *paar("frei", "JO", [("frei", "froh"), ("streng", "ruhig")], "ZO", [("frei", "sorge"), ("streng", "denkt")]),
]))

# D3 2. Schuldbeitritt ----------------------------------------------------------------------------------------------------------
folie([("beit", "Abgrenzung › 2. Schuldbeitritt")], rechts_frei([
    *tafel("beit", "2. Schuldbeitritt"),
    z("auch: kumulative Schuldübernahme", 110, 190, beim("beit", "kumulative"), "Bold", 36),
    z("nicht allgemein geregelt, Vertrag nach", 110, 270, "beit2", "Bold", 36),
    z("§ 311 Abs. 1 BGB", 160, 325, beim("beit2", "dreihundertelf"), size=36),
    z("Beitretender und Altschuldner:", 110, 405, "ges", "Bold", 36),
    z("Gesamtschuldner, § 421 BGB", 160, 460, beim("ges", "Gesamtschuldner"), size=36),
    zit("BGH, Versäumnisurt. v. 3.9.2020 – III ZR 56/19, Rn. 18", 160, 515, beim("ges", "Gesamtschuldner")),
    z("nicht akzessorisch: eigene Wege", 110, 590, "nakz", "Bold", 36),
    zit("BGH, Urt. v. 12.11.2015 – I ZR 168/14, Rn. 40", 160, 645, beim("nakz", "eigene")),
    z("grundsätzlich formfrei", 110, 720, "formfr", "Bold", 36),
    zit("BGH, Urt. v. 12.5.2016 – IX ZR 208/15, Rn. 7", 160, 775, beim("formfr", "formfrei")),
    *requisit([("beit", ("tabler", "users", 110, WEISS), "Schuldbeitritt", WEISS),
               ("ges", ("tabler", "users-plus", 110, GELB), "Gesamtschuld", GELB),
               ("nakz", ("tabler", "link-off", 100, WEISS), "nicht akzessorisch", WEISS),
               ("formfr", ("tabler", "file-text", 100, GRUEN), "formfrei", GRUEN)]),
    *paar("beit", "JO", [("beit", "ruhig"), ("ges", "denkt")], "KA", [("beit", "ruhig"), ("ges", "sorge")]),
]))

# D4 3. Bürgschaft: § 765 Abs. 1 (Wortlaut), §§ 767, 768, 770, 771 ---------------------------------------------------------------
W765 = ["„(1) Durch den Bürgschaftsvertrag verpflichtet sich der Bürge gegenüber",
        "dem Gläubiger eines Dritten, für die Erfüllung der Verbindlichkeit des",
        "Dritten einzustehen.“"]
w765, w765_y = wortlaut(80, 175, 1100, W765, "§ 765 Abs. 1 BGB", "w765", marken=[
    (1, "Gläubiger eines Dritten", beim("w765", "Gläubiger", nr=1)),
    (2, "einzustehen", beim("w765", "einzustehen"))], size=32)
folie([("w765", "Abgrenzung › 3. Bürgschaft, § 765 Abs. 1 BGB"), ("akz", "3. Bürgschaft › Akzessorietät und Einreden")], rechts_frei([
    *tafel("w765", "3. Bürgschaft"),
    *w765,
    z("Einstehen für eine fremde Schuld", 110, w765_y + 35, "fremd", "Bold", 36),
    z("akzessorisch, § 767 BGB: Bestand der Hauptschuld", 110, w765_y + 105, "akz", "Bold", 36),
    z("§ 768 BGB: Einreden des Hauptschuldners", 110, w765_y + 175, "einr", "Bold", 36),
    z("§ 770 BGB: Anfechtbarkeit, Aufrechenbarkeit", 110, w765_y + 230, beim("einr", "siebenhundertsiebzig"), "Bold", 36),
    z("§ 771 BGB: Einrede der Vorausklage", 110, w765_y + 300, "p771", "Bold", 36),
    *requisit([("w765", ("tabler", "file-certificate", 100, WEISS), "Bürgschaft", WEISS),
               ("fremd", ("tabler", "user-plus", 110, WEISS), "fremde Schuld", WEISS),
               ("akz", ("tabler", "link", 100, GELB), "akzessorisch", GELB),
               ("einr", ("tabler", "shield", 100, GRUEN), "Einreden", GRUEN)]),
    *paar("w765", "KA", [("w765", "ruhig"), ("akz", "denkt"), ("einr", "froh")], "ZO", [("w765", "ruhig"), ("p771", "denkt")]),
]))

# D5 § 766 (Wortlaut) ------------------------------------------------------------------------------------------------------------
W766 = ["„Zur Gültigkeit des Bürgschaftsvertrags ist schriftliche Erteilung der",
        "Bürgschaftserklärung erforderlich. Die Erteilung der Bürgschafts-",
        "erklärung in elektronischer Form ist ausgeschlossen. …“"]
w766, w766_y = wortlaut(80, 175, 1100, W766, "§ 766 Satz 1 und 2 BGB", "w766", marken=[
    (0, "schriftliche Erteilung", beim("w766", "schriftliche")),
    (2, "in elektronischer Form ist ausgeschlossen", beim("w766b", "elektronischer"))], size=32)
folie([("w766", "3. Bürgschaft › Schriftform, § 766 BGB")], rechts_frei([
    *tafel("w766", "3. Bürgschaft: Form"),
    *w766,
    *okz("Bürgschaftserklärung: schriftlich", w766_y + 50, beim("w766", "erforderlich"), "Bold", 38, x=160),
    *neinz("elektronische Form ausgeschlossen", w766_y + 130, beim("w766b", "ausgeschlossen"), "Bold", 38, x=160),
    *requisit([(beim("w766", "schriftliche"), ("tabler", "signature", 110, WEISS), "schriftlich", GELB),
               ("w766b", ("tabler", "mail", 100, WEISS), "nicht elektronisch", WEISS)]),
    *paar("w766", "KA", [("w766", "ruhig"), ("w766b", "denkt")], "ZO", [("w766", "ruhig")]),
]))

# E1 Abgrenzung im Überblick (Dreispalter, progressiv) -------------------------------------------------------------------------
SP_X = [110, 450, 920, 1390]                # Zeilenkopf, Schuldübernahme, Schuldbeitritt, Bürgschaft
ZY = [170, 280, 390, 530, 640]              # Kopfzeile, Altschuldner, Haftung, akzessorisch, Form
STRICH = (21, 21, 21, 110)


def zelle(text, sp, zy, cue, stil="Regular", size=32, zeile2=None):
    els = [z(text, SP_X[sp], ZY[zy], cue, stil, size, rechts=(SP_X[sp + 1] - 20) if sp < 3 else 1830)]
    if zeile2:
        els.append(z(zeile2, SP_X[sp], ZY[zy] + 45, cue, stil, size, rechts=(SP_X[sp + 1] - 20) if sp < 3 else 1830))
    return els


folie([("tab", "Abgrenzung › Überblick")], [
    karte(60, 50, 1800, 820, "tab"),
    titel(glyphen("Abgrenzung im Überblick"), 110, 80, "tab", 46),
    *[linienzug([(x - 20, 160), (x - 20, 720)], "tab", breite=3, farbe=STRICH) for x in SP_X[1:]],
    *[linienzug([(100, y - 15), (1820, y - 15)], "tab", breite=3, farbe=STRICH) for y in ZY[1:]],
    *zelle("Schuldübernahme", 1, 0, beim("tab", "Schuldübernahme"), "ExtraBold", 34, zeile2="§§ 414, 415 BGB"),
    *zelle("Schuldbeitritt", 2, 0, beim("tab", "Beitritt"), "ExtraBold", 34, zeile2="§ 311 Abs. 1 BGB"),
    *zelle("Bürgschaft", 3, 0, beim("tab", "Bürgschaft"), "ExtraBold", 34, zeile2="§ 765 BGB"),
    *zelle("Altschuldner", 0, 1, beim("tab", "Altschuldner"), "Bold", 32),
    *zelle("wird frei", 1, 1, beim("tab", "frei"), "Bold", 32),
    *zelle("bleibt verpflichtet", 2, 1, beim("tab", "bleibt"), "Bold", 32),
    *zelle("bleibt verpflichtet", 3, 1, beim("tab", "bleibt"), "Bold", 32),
    *zelle("Haftung", 0, 2, "t2", "Bold", 32),
    *zelle("–", 1, 2, "t2", size=32),
    *zelle("eigene Schuld:", 2, 2, beim("t2", "schuldet"), size=32, zeile2="Gesamtschuld, § 421"),
    *zelle("Einstehen für", 3, 2, beim("t2", "wer"), size=32, zeile2="fremde Schuld"),
    *zelle("akzessorisch", 0, 3, "t3", "Bold", 32),
    *zelle("–", 1, 3, "t3", size=32),
    *zelle("ja, § 767", 3, 3, beim("t3", "Bürgschaft"), "Bold", 32),
    *zelle("nein", 2, 3, beim("t3", "akzessorisch"), "Bold", 32),
    *zelle("Form", 0, 4, "t4", "Bold", 32),
    *zelle("–", 1, 4, "t4", size=32),
    *zelle("grundsätzlich formfrei", 2, 4, beim("t4", "Schriftform"), size=32),
    *zelle("schriftlich, § 766", 3, 4, beim("t4", "Schriftform"), "Bold", 32),
])

# E2 Abgrenzung in 2 Schritten ----------------------------------------------------------------------------------------------------
folie([("k1q", "Abgrenzung › 1. Wird der Altschuldner frei?"), ("k2q", "Abgrenzung › 2. Eigene oder fremde Schuld?"),
       ("indiz", "Abgrenzung › Indiz: eigenes Interesse")], rechts_frei([
    *tafel("k1q", "Abgrenzung in 2 Schritten"),
    z("1. Soll der Altschuldner frei werden?", 110, 190, beim("k1q", "Soll"), "Bold", 36),
    z("nur dann: Schuldübernahme", 160, 245, beim("k1q", "Nur"), size=36),
    z("2. eigene Schuld: Schuldbeitritt", 110, 330, beim("k2q", "Beitritt"), "Bold", 36),
    z("nur Einstehen für fremde Schuld: Bürgschaft", 160, 385, beim("k2q", "Bürgschaft"), size=36),
    z("Indiz für Beitritt: eigenes wirtschaftliches", 110, 480, "indiz", "Bold", 36),
    z("oder rechtliches Interesse an der Tilgung", 160, 535, beim("indiz", "rechtliches"), size=36),
    zit("BGH, Versäumnisurt. v. 3.9.2020 – III ZR 56/19, Rn. 20", 160, 592, beim("indiz", "rechtliches")),
    z("im Zweifel: Bürgschaft (herrschende Meinung)", 110, 675, "zweif", "Bold", 36),
    z("damit die Schriftform nicht umgangen wird", 160, 730, beim("zweif", "damit"), size=36),
    *requisit([("k1q", ("tabler", "user-check", 100, WEISS), "Altschuldner frei?", WEISS),
               ("k2q", ("tabler", "users", 110, WEISS), "eigene Schuld?", WEISS),
               ("indiz", ("tabler", "briefcase", 100, GELB), "eigenes Interesse", GELB),
               ("zweif", ("tabler", "file-certificate", 100, WEISS), "im Zweifel Bürgschaft", WEISS)]),
    *paar("k1q", "JO", [("k1q", "ruhig"), ("indiz", "denkt")], "KA", [("k1q", "ruhig"), ("k2q", "denkt"), ("zweif", "ruhig")]),
]))

# F Subsumtion ----------------------------------------------------------------------------------------------------------------------
folie([("sub", "Subsumtion · Die Erklärung von Katja")], rechts_frei([
    *tafel("sub", "Im Fall: die Erklärung von Katja"),
    z("Bank wollte Jochen nicht entlassen", 160, 190, "s1", "Bold", 36),
    *neinz("keine Schuldübernahme", 245, beim("s1", "Schuldübernahme"), size=36, x=210),
    z("nur Jochen nutzt das Auto", 160, 330, "s2", "Bold", 36),
    *neinz("kein eigenes Interesse von Katja", 385, beim("s2", "eigenes"), size=36, x=210),
    z("nur Einstehen für eine fremde Schuld", 160, 470, "s3", "Bold", 36),
    *okz("Bürgschaft, trotz „übernehmen“", 525, beim("s3", "Bürgschaft"), "Bold", 36, x=210),
    z("Form, § 766 BGB: schriftlich erklärt,", 160, 610, "s4", "Bold", 36),
    *okz("eigenhändig unterschrieben", 665, beim("s4", "eigenhändig"), size=36, x=210),
    *requisit([("s1", ("tabler", "building-bank", 110, BLAU), "Jochen bleibt", WEISS),
               ("s2", ("tabler", "car", 130, BLAU), "nur Jochen", WEISS),
               ("s3", ("tabler", "file-certificate", 100, GELB), "Bürgschaft", GELB),
               ("s4", ("tabler", "signature", 110, WEISS), "unterschrieben", GRUEN)]),
    *paar("sub", "JO", [("sub", "ruhig"), ("s2", "denkt")], "KA", [("sub", "ruhig"), ("s1", "denkt"), ("s3", "sorge")]),
]))

# G Ergebnis (Bühne) ------------------------------------------------------------------------------------------------------------------
ZX9, JX9, KX9 = 420, 1000, 1600
folie([("erg", "Ergebnis · Katja haftet als Bürgin"), ("erg3", "Ergebnis › Einrede der Vorausklage, § 771 BGB")], [
    blk(80, 40, 1760, 100, GRUEN, "erg", [("Ergebnis: Katja haftet als Bürgin für 12.000 €", "ExtraBold", 42, INK)]),
    z("Haftung hängt an der Kreditschuld von Jochen, § 767 BGB", 110, 165, "erg2", "Bold", 34, rechts=1820),
    boden("erg"),
    ficon("tabler", "building-bank", 150, 420, 130, "erg", fuell=BLAU),
    *fl("ZO", ZX9, [("erg", "ruhig_r"), ("erg3", "denkt_r")], erst="pop"),
    ns("Frau Zöllner", ZX9, BODEN, "erg", NFARBE["ZO"], d=0.1),
    *fl("JO", JX9, [("erg", "sorge")], erst="pop", d=0.1),
    ns("Jochen", JX9, BODEN, "erg", NFARBE["JO"], d=0.2),
    *fl("KA", KX9, [("erg", "sorge"), ("erg3", "ruhig")], erst="pop", d=0.2),
    ns("Katja", KX9, BODEN, "erg", NFARBE["KA"], d=0.3),
    pl("Bürgin", KX9, 300, beim("erg", "Bürgin"), fill=GELB, size=32, anker="m"),
    pl("Kreditschuld", JX9, 230, "erg2", fill=WEISS, size=30, anker="m"),
    pl("Einrede der Vorausklage, § 771 BGB", KX9 - 120, 230, "erg3", fill=WEISS, size=30, anker="m"),
    pfeil(600, 560, 860, 560, beim("erg3", "vollstrecken"), breite=10, kopf=30),
    pl("zuerst bei Jochen vollstrecken", 700, 300, beim("erg3", "vollstrecken"), fill=GELB, size=28, anker="m"),
])

# H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Abgrenzung durch Auslegung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Rechtsnatur zuerst durch Auslegung", 200, 200, beim("tipp", "Bestimme"), "Bold", 38),
    z("2. Verbraucher tritt Kreditvertrag bei:", 200, 300, "tipp2", "Bold", 36),
    z("Verbraucherdarlehensrecht entsprechend,", 250, 355, beim("tipp2", "Verbraucherdarlehen"), size=36),
    z("etwa Widerrufsrecht", 250, 410, beim("tipp2", "Widerrufsrecht"), size=36),
    zit("BGH, Versäumnisurt. v. 21.9.2021 – XI ZR 650/20, Rn. 11", 250, 465, beim("tipp2", "Widerrufsrecht")),
    z("3. Nahestehende krass überfordert:", 200, 545, "tipp3", "Bold", 36),
    z("Sittenwidrigkeit vermutet, § 138 Abs. 1 BGB", 250, 600, beim("tipp3", "vermutet"), size=36),
    zit("BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9", 250, 655, beim("tipp3", "sittenwidrig")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# I Klausurschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Bürgschaftsvertrag"), ("k3", "Klausurschema › III. Hauptschuld"),
       ("k4", "Klausurschema › IV. Einreden"), ("k5", "Klausurschema › V. Ergebnis")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anspruch aus § 765 Abs. 1 BGB"), 110, 90, "sch", 46),
    z("I. Rechtsnatur der Erklärung: Auslegung, §§ 133, 157 BGB", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("1. Altschuldner frei?", K2, 262, "k1a", size=36, rechts=1820),
    z("2. eigene Schuld oder fremde Schuld?", K2, 317, "k1b", size=36, rechts=1820),
    z("II. Wirksamer Bürgschaftsvertrag", K1, 400, "k2", "Bold", 40, rechts=1820),
    z("Einigung, Schriftform (§ 766 BGB), keine Sittenwidrigkeit (§ 138 BGB)", K2, 462, "k2a", size=36, rechts=1820),
    z("III. Bestand der Hauptschuld, § 767 BGB", K1, 545, "k3", "Bold", 40, rechts=1820),
    z("IV. Einreden des Bürgen, §§ 768, 770, 771 BGB", K1, 630, "k4", "Bold", 40, rechts=1820),
    z("V. Ergebnis", K1, 715, "k5", "Bold", 40, rechts=1820),
])

# J Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wird der Altschuldner ", 0), ("frei", "a"), (",", 0)], [("ist es eine Schuldübernahme.", 0)]],
                750, 310, 42, "merke", {"a": beim("merke", "frei")}),
    *markertext([[("Bleibt er verpflichtet, entscheidet", 0)], [("der ", 0), ("Wille", "b"), (": Eigene Schuld heißt", 0)],
                 [("Beitritt", "c"), (", Einstehen für fremde", 0)], [("Schuld heißt ", 0), ("Bürgschaft", "d"), (".", 0)]],
                750, 480, 42, "m2", {"b": beim("m2", "Wille"), "c": beim("m2", "Beitritt"), "d": beim("m2", "Bürgschaft")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
