"""Folge 223 · Mittellose Ehefrau bürgt: Ist die Angehörigenbürgschaft sittenwidrig? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Tischlermeister Gero braucht für seine Werkstatt einen Firmenkredit über 200.000 € (Zinsen 1.000 € im Monat);
Herr Wittkamp von der Bank verlangt die Bürgschaft seiner Frau Anneke (kein eigenes Einkommen, kein Vermögen). Drei Jahre
später sind 180.000 € offen, die Bank verlangt sie von Anneke.
Szenen laut ../SZENENPLAN.md: A1 Werkstatt, A2 Bank (Bürgschaft verlangt, Bitte, Urkunde), A3 drei Jahre später (Frage),
B Sachverhalt, C Anspruch § 765 Abs. 1 (Wortlaut), Einigung, Form, Hauptschuld, D1/D2 Bürgschaftsbeschluss BVerfGE 89, 214
(Art. 2 Abs. 1 GG als Wortlautkarte), E1/E2 § 138 Abs. 1 (Wortlaut) und BGH-Kriterien, F Subsumtion, G Ergebnis (Bühne),
H Gegenfall, I Klausurtipp (Lexi), J Klausurschema, K Merksatz (Lexi).
DARSTELLUNG: keine echte Bank, kein Logo; Anneke sachlich und selbstbestimmt, Gero ohne Klischee, die Bank sachlich; die
Beschwerdeführerinnen des Bürgschaftsbeschlusses werden nicht als Figuren gezeigt.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/stehend/paar/tisch als eigene Kopie
aus Folge 220 (gemeinsame Dateien unverändert). Zwei Handlungsgeräusche (Unterschrift, Brief; ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut BGB/GG nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_223/"

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
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_223/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/220) ---------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"AN": "Anneke", "GE": "Gero", "WI": "Herr Wittkamp"}
NFARBE = {"AN": TUERKIS_, "GE": GELB, "WI": BLAU}
FE = "fluent-emoji-high-contrast"


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def tisch(x0, x1, cue, oben=690, bis=None, fill=HOLZ):
    """Tisch vor bzw. neben den Figuren: Platte und zwei Beine."""
    return [feld(x0, oben, x1 - x0, 34, cue, fill=fill, rand=5, rund=6, bis=bis, name="tischplatte"),
            feld(x0 + 30, oben + 34, 26, BODEN - oben - 34, cue, fill=fill, rand=4, rund=3, bis=bis, name="tischbein"),
            feld(x1 - 56, oben + 34, 26, BODEN - oben - 34, cue, fill=fill, rand=4, rund=3, bis=bis, name="tischbein2")]


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


# ===========================================================================================================================
# A1 Fall: die Werkstatt (Gero, Firmenkredit, Zinsen)
# ===========================================================================================================================
GX1 = 1180
folie([(NULL, "Fall · Die Werkstatt von Gero")], [
    hart(pl("Gero ist Tischlermeister", 70, 30, NULL, fill=GELB, size=44)),
    boden(NULL),
    *[hart(e) for e in tisch(160, 860, NULL, oben=700)],
    hart(ficon(FE, "carpentry-saw", 330, 700, 210, NULL, fuell=WEISS)),
    hart(ficon(FE, "wood", 640, 700, 230, NULL, fuell=HOLZ)),
    hart(ficon(FE, "toolbox", 760, BODEN, 150, NULL, fuell=ROT)),
    *fig("GE", GX1, BODEN, FH, [(NULL, "froh"), ("kredit", "ruhig"), ("zins", "sorge")], erst="cut"),
    hart(fall_ns("GE", GX1, NULL)),
    ficon("tabler", "building-bank", 1620, 300, 150, "kredit", fuell=BLAU),
    pl("Firmenkredit: 200.000 €", 1620, 405, beim("kredit", "Firmenkredit"), fill=GELB, size=32, anker="m"),
    pl("für neue Maschinen", 1620, 330, beim("kredit", "Maschinen"), fill=WEISS, size=30, anker="m"),
    pl("Zinsen: 1.000 € im Monat", 1620, 480, beim("zins", "Zinsen"), fill=ROT, size=32, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: bei der Bank – Bürgschaft verlangt, Bitte, Urkunde
# ===========================================================================================================================
WX2, GX2, AX2 = 430, 1110, 1610
AHX, AHY = hand("AN_ruhig", AX2, BODEN, FH, -1)
UNT = beim("urk", "Euro")
folie([("bank", "Fall · Bei der Bank"), ("anneke", "Fall · Die Bank will die Bürgschaft von Anneke"),
       ("urk", "Fall · Anneke unterschreibt")], [
    pl("Bei der Bank", 70, 30, "bank", fill=GELB, size=44),
    boden("bank"),
    ficon("tabler", "building-bank", 180, 420, 120, "bank", fuell=BLAU),
    *fig("WI", WX2, BODEN, FH, [("bank", "ruhig_r")], bis="wi1", erst="pop"),
    *redet("WI_redet_r", WX2, BODEN, FH, "wi1", "anneke"),
    *fig("WI", WX2, BODEN, FH, [("anneke", "ruhig_r"), (beim("nimmt", "nimmt"), "froh_r")], erst="cut"),
    feld(200, 660, 470, 200, "bank", fill=BLAU, rand=5, rund=12, name="schreibtisch"),
    ns("Herr Wittkamp", WX2, BODEN, "bank", NFARBE["WI"], d=0.1),
    *fig("GE", GX2, BODEN, FH, [("bank", "ruhig")], bis="ge1", erst="pop", d=0.1),
    *redet("GE_redet_r", GX2, BODEN, FH, "ge1", "an1"),
    *fig("GE", GX2, BODEN, FH, [("an1", "ruhig_r"), ("urk", "ruhig")], erst="cut"),
    ns("Gero", GX2, BODEN, "bank", NFARBE["GE"], d=0.2),
    *fig("AN", AX2, BODEN, FH, [("anneke", "ruhig"), ("mittel", "denkt")], bis="an1", erst="pop"),
    *redet("AN_redet", AX2, BODEN, FH, "an1", "urk"),
    *fig("AN", AX2, BODEN, FH, [("urk", "ruhig"), (beim("nimmt", "nimmt"), "sorge")], erst="cut"),
    ns("Anneke", AX2, BODEN, "anneke", NFARBE["AN"], d=0.1),
    ficon(FE, "ring", AX2, 395, 70, beim("anneke", "verheiratet"), fuell=GELB, bis="ge1"),
    pl("seit 8 Jahren verheiratet", AX2, 120, beim("anneke", "verheiratet"), fill=WEISS, size=30, anker="m", bis="ge1"),
    pl("kein eigenes Einkommen", AX2, 175, beim("mittel", "Einkommen"), fill=ROT, size=30, anker="m", bis="ge1"),
    pl("kein Vermögen", AX2, 230, beim("mittel", "Vermögen"), fill=ROT, size=30, anker="m", bis="ge1"),
    blase("sprech", 700, 210, "wi1", 860, 220, inhalt=["Den Kredit gibt es nur, wenn Ihre", "Frau eine Bürgschaft übernimmt."],
          textsize=34, figur=("WI_redet_r", WX2, BODEN, FH), bis="anneke"),
    blase("sprech", 720, 200, "ge1", 1440, 165, inhalt=["Anneke, ohne deine Bürgschaft", "bekomme ich den Kredit nicht."],
          textsize=34, figur=("GE_redet_r", GX2, BODEN, FH), bis="an1"),
    blase("sprech", 720, 200, "an1", 1250, 165, inhalt=["Wenn es für die Werkstatt sein", "muss, unterschreibe ich."],
          textsize=34, figur=("AN_redet", AX2, BODEN, FH), bis="urk"),
    karte(470, 70, 820, 290, beim("urk", "Urkunde"), fill=WEISS, rund=10, schatten=6, rand=4),
    z("Bürgschaft", 505, 88, beim("urk", "Urkunde"), "ExtraBold", 36, rechts=1270),
    z("Ich bürge für den Firmenkredit von", 505, 145, beim("urk", "Ich"), size=34, rechts=1270),
    z("Gero über 200.000 Euro.", 505, 195, beim("urk", "Gero"), size=34, rechts=1270),
    linienzug([(840, 335), (1240, 335)], UNT, breite=3),
    szene(z("Anneke", 905, 276, UNT, "ExtraBold", 40, rechts=1270), "223unterschrift*", 0.9, 0.0),
    ficon("tabler", "ballpen", AHX - 30, AHY + 30, 70, beim("urk", "eigenhändig"), fuell=GELB),
    pl("Bank nimmt an", WX2, 735, beim("nimmt", "nimmt"), fill=GRUEN, size=30, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: drei Jahre später – die Bank verlangt Zahlung, die Frage
# ===========================================================================================================================
WX3, AX3, GX3 = 430, 1080, 1660
folie([("spaet", "Fall · Drei Jahre später"), ("frage", "Fall · Die Frage")], [
    pl("Drei Jahre später: keine Aufträge mehr", 70, 30, "spaet", fill=GELB, size=44, bis="frage"),
    boden("spaet"),
    *fig("GE", GX3, BODEN, FH, [("spaet", "sorge"), ("frage", "muede")], erst="pop"),
    ns("Gero", GX3, BODEN, "spaet", NFARBE["GE"], d=0.1),
    ficon("tabler", "calendar", GX3, 360, 100, "spaet", fuell=WEISS),
    pl("Raten bleiben aus", GX3, 115, beim("spaet", "Raten"), fill=WEISS, size=30, anker="m"),
    pl("Bank kündigt", GX3, 175, beim("kuend", "kündigt"), fill=WEISS, size=30, anker="m"),
    pl("offen: 180.000 €", GX3, 240, beim("kuend", "hundertachtzigtausend"), fill=ROT, size=32, anker="m"),
    ficon("tabler", "building-bank", 150, 420, 120, "brief", fuell=BLAU),
    *fig("WI", WX3, BODEN, FH, [("brief", "ruhig_r")], bis="wi2", erst="pop"),
    *redet("WI_redet_r", WX3, BODEN, FH, "wi2", "an2"),
    *fig("WI", WX3, BODEN, FH, [("an2", "ernst_r"), ("frage", "ruhig_r")], erst="cut"),
    ns("Herr Wittkamp", WX3, BODEN, "brief", NFARBE["WI"], d=0.1),
    szene(ficon("tabler", "mail", 760, 600, 110, beim("brief", "wendet"), fuell=WEISS), "223brief*", 0.8, 0.0),
    *fig("AN", AX3, BODEN, FH, [("brief", "ruhig")], bis="an2", erst="pop", d=0.1),
    *redet("AN_redet", AX3, BODEN, FH, "an2", "frage"),
    *fig("AN", AX3, BODEN, FH, [("frage", "sorge")], erst="cut"),
    ns("Anneke", AX3, BODEN, "brief", NFARBE["AN"], d=0.2),
    blase("sprech", 720, 210, "wi2", 680, 220, inhalt=["Sie haben gebürgt. Bitte zahlen", "Sie die 180.000 €."],
          textsize=34, figur=("WI_redet_r", WX3, BODEN, FH), bis="an2"),
    blase("sprech", 680, 200, "an2", 900, 215, inhalt=["Davon kann ich nicht einmal", "die Zinsen bezahlen."],
          textsize=34, figur=("AN_redet", AX3, BODEN, FH), bis="frage"),
    pl("Muss Anneke zahlen?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("Oder ist ihre Bürgschaft sittenwidrig und nichtig?", 900, 125, "frage2", fill=WEISS, size=34, anker="m"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_223(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_223("sv", [
    "Tischlermeister Gero braucht für neue Maschinen seiner Werkstatt einen Firmenkredit über 200.000 Euro; die Zinsen "
    "betragen 1.000 Euro im Monat. Herr Wittkamp von der Bank verlangt, dass seine Ehefrau Anneke bürgt.",
    "Anneke ist seit acht Jahren mit Gero verheiratet. Sie hat kein eigenes Einkommen und kein Vermögen; daran wird sich "
    "absehbar nichts ändern. Die Werkstatt gehört Gero allein. Anneke unterschreibt eigenhändig die Urkunde: „Ich bürge "
    "für den Firmenkredit von Gero über 200.000 Euro.“ Herr Wittkamp nimmt die Erklärung an.",
    "Drei Jahre später bleiben die Aufträge aus. Die Bank kündigt den Kredit wirksam, 180.000 Euro sind offen. Sie "
    "verlangt das Geld von Anneke. Umstände, die eine Ausnutzung durch die Bank ausschließen, sind nicht ersichtlich.",
], "Muss Anneke zahlen?")

# ===========================================================================================================================
# C Anspruch aus § 765 Abs. 1 (Wortlaut), Einigung, Form § 766 S. 1, Hauptschuld
# ===========================================================================================================================
W765 = ("„(1) Durch den Bürgschaftsvertrag verpflichtet sich der Bürge gegenüber dem Gläubiger eines Dritten, für die "
        "Erfüllung der Verbindlichkeit des Dritten einzustehen.“")
w765, w765_y = wortlaut(80, 240, 1100, W765, "§ 765 Abs. 1 BGB", "w765", marken=[
    ("Gläubiger eines Dritten", beim("w765", "Gläubiger")), ("einzustehen", beim("w765", "einzustehen"))], size=32)
folie([("agl", "Anspruch · Bank gegen Anneke, § 765 Abs. 1 BGB"), ("einig", "I. Entstanden › Bürgschaftsvertrag und Form"),
       ("problem", "I. Entstanden › Nichtigkeit, § 138 Abs. 1 BGB?")], rechts_frei([
    *tafel("agl", "Bank gegen Anneke: 180.000 €"),
    z("Anspruch aus § 765 Abs. 1 BGB", 110, 175, beim("agl", "Anspruch"), "Bold", 38),
    *w765,
    *okz("Einigung: Anneke und die Bank", w765_y + 25, "einig", size=34, x=160),
    *okz("Form, § 766 S. 1 BGB: schriftlich erteilt,", w765_y + 85, beim("form", "Form"), size=34, x=160),
    z("eigenhändig unterschrieben (§ 126 Abs. 1 BGB)", 160, w765_y + 135, beim("form", "eigenhändig"), size=34),
    *okz("Hauptschuld: Darlehen an Gero", w765_y + 195, "haupt", size=34, x=160),
    blk(110, w765_y + 265, 1050, 80, HELLROT, "problem", [("Problem: nichtig nach § 138 Abs. 1 BGB?", "ExtraBold", 36, INK)]),
    *requisit([("agl", ("tabler", "building-bank", 120, BLAU), "Anspruch der Bank", WEISS),
               ("w765", ("tabler", "file-certificate", 110, WEISS), "einstehen", GELB),
               ("form", ("tabler", "signature", 110, WEISS), "schriftlich", GELB),
               ("problem", ("tabler", "scale", 120, WEISS), "nichtig?", PINK)]),
    *paar("WI", [("agl", "ruhig")], "AN", [("agl", "sorge"), ("einig", "ruhig"), ("problem", "denkt")]),
]))

# ===========================================================================================================================
# D1 Bürgschaftsbeschluss, BVerfGE 89, 214: der Fall der Tochter, Art. 2 Abs. 1 GG (Wortlaut), Privatautonomie
# ===========================================================================================================================
WA2 = ("„(1) Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit, soweit er nicht die Rechte anderer "
       "verletzt und nicht gegen die verfassungsmäßige Ordnung oder das Sittengesetz verstößt.“")
wa2, wa2_y = wortlaut(80, 420, 1100, WA2, "Art. 2 Abs. 1 GG", "art2", marken=[
    ("freie Entfaltung seiner Persönlichkeit", beim("art2", "freie"))], size=30)
folie([("bverfg", "Bürgschaftsbeschluss · BVerfGE 89, 214"), ("art2", "Bürgschaftsbeschluss › Privatautonomie, Art. 2 Abs. 1 GG")],
      rechts_frei([
    *tafel("bverfg", "Bürgschaftsbeschluss"),
    blk(110, 165, 1050, 100, GELB, "bverfg", [("BVerfG, Beschl. v. 19.10.1993 · BVerfGE 89, 214", "ExtraBold", 32, INK),
                                            ("1 BvR 567/89, 1 BvR 1044/89", "Bold", 30, INK)]),
    z("Tochter, 21, ohne Berufsausbildung, bürgt für die", 110, 290, beim("tochter", "Tochter"), "Bold", 34),
    z("Geschäftskredite des Vaters: bis 100.000 DM", 160, 340, beim("tochter", "Geschäftskredite"), size=34),
    zit("BVerfGE 89, 214 (218)", 160, 388, beim("tochter", "hunderttausend")),
    *wa2,
    z("schützt die Privatautonomie:", 110, wa2_y + 25, "privat", "Bold", 34),
    z("„Selbstbestimmung des Einzelnen im Rechtsleben“", 160, wa2_y + 75, beim("privat", "Selbstbestimmung"), size=34),
    zit("BVerfGE 89, 214 (231)", 160, wa2_y + 122, beim("privat", "Rechtsleben")),
    z("starkes Übergewicht einer Seite: Fremdbestimmung", 110, wa2_y + 170, "fremd", "Bold", 34),
    zit("BVerfGE 89, 214 (232)", 160, wa2_y + 217, beim("fremd", "fremdbestimmt")),
    *requisit([("bverfg", ("tabler", "building-bank", 120, BLAUHELL), "Bundesverfassungsgericht", BLAUHELL),
               ("tochter", ("tabler", "briefcase", 110, WEISS), "Geschäftskredite des Vaters", WEISS),
               ("art2", ("tabler", "user-check", 110, GRUEN), "freie Entfaltung", GRUEN),
               (beim("privat", "Selbstbestimmung"), ("tabler", "user-check", 110, GRUEN), "Selbstbestimmung", GRUEN),
               ("fremd", ("tabler", "scale", 120, ROT), "Übergewicht", ROT)]),
    *paar("AN", [("bverfg", "ruhig"), ("fremd", "denkt")], "GE", [("bverfg", "ruhig"), ("fremd", "sorge")]),
]))

# ===========================================================================================================================
# D2 Pflicht der Zivilgerichte: Korrektur über die Generalklauseln (BVerfGE 89, 214, 229 f., 234)
# ===========================================================================================================================
folie([("korr", "Bürgschaftsbeschluss › Inhaltskontrolle durch die Zivilgerichte"),
       ("gk", "Bürgschaftsbeschluss › Generalklauseln, §§ 138, 242 BGB")], rechts_frei([
    *tafel("korr", "Pflicht der Zivilgerichte"),
    z("1. Vertrag für eine Seite ungewöhnlich belastend", 110, 190, beim("korr", "ungewöhnlich"), "Bold", 36),
    z("2. Folge strukturell ungleicher Verhandlungsstärke", 110, 255, beim("korr", "strukturell"), "Bold", 36),
    z("dann: Zivilgerichte müssen korrigierend eingreifen", 110, 330, beim("korr", "Zivilgerichte"), size=36),
    zit("BVerfGE 89, 214 (234)", 160, 382, beim("korr", "eingreifen")),
    blk(110, 440, 1050, 90, GELB, "gk", [("über die Generalklauseln: § 138 BGB, § 242 BGB", "ExtraBold", 36, INK)]),
    zit("BVerfGE 89, 214 (229 f.)", 160, 545, beim("gk", "zweihundertzweiundvierzig")),
    *neinz("„Vertrag ist Vertrag“ reicht dann nicht", 620, "vvv", "Bold", 38, x=160, kreuz=beim("vvv", "reicht")),
    *requisit([("korr", ("tabler", "gavel", 110, WEISS), "Zivilgericht", WEISS),
               ("gk", ("tabler", "books", 110, GELB), "§§ 138, 242 BGB", GELB),
               ("vvv", ("tabler", "file-certificate", 110, WEISS), "Vertrag ist Vertrag?", PINK)]),
    *paar("AN", [("korr", "ruhig")], "GE", [("korr", "ruhig"), ("vvv", "froh")]),
]))

# ===========================================================================================================================
# E1 § 138 Abs. 1 (Wortlaut) und die Kriterien des BGH
# ===========================================================================================================================
W138 = "„(1) Ein Rechtsgeschäft, das gegen die guten Sitten verstößt, ist nichtig.“"
w138, w138_y = wortlaut(80, 170, 1100, W138, "§ 138 Abs. 1 BGB", "w138", marken=[
    ("guten Sitten", beim("w138", "guten")), ("nichtig", beim("w138", "nichtig"))], size=34)
folie([("w138", "I. Entstanden › Nichtigkeit, § 138 Abs. 1 BGB"),
       ("krass", "§ 138 Abs. 1 BGB › 1. krasse finanzielle Überforderung"),
       ("nahe", "§ 138 Abs. 1 BGB › 2. besondere persönliche Nähe")], rechts_frei([
    *tafel("w138", "Sittenwidrigkeit"),
    *w138,
    z("Kriterien des BGH bei nahen Angehörigen:", 110, w138_y + 30, "bgh", "Bold", 36),
    z("1. krasse finanzielle Überforderung:", 110, w138_y + 105, "krass", "Bold", 36),
    z("voraussichtlich nicht einmal die laufenden Zinsen", 160, w138_y + 160, beim("krass", "laufenden"), size=34),
    z("aus dem pfändbaren Einkommen und Vermögen", 160, w138_y + 210, beim("krass", "pfändbaren"), size=34),
    z("dauerhaft tragbar", 160, w138_y + 260, beim("krass", "dauerhaft"), size=34),
    zit("BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9", 160, w138_y + 310, beim("krass", "tragen")),
    z("2. persönlich besonders nahe, etwa Ehegatte", 110, w138_y + 375, "nahe", "Bold", 36),
    zit("BGH, Urt. v. 15.11.2016 – XI ZR 32/16, Rn. 20", 160, w138_y + 427, beim("nahe", "Ehegatte")),
    *requisit([("w138", ("tabler", "scale", 120, WEISS), "gute Sitten", WEISS),
               ("krass", ("tabler", "coin-euro", 110, GELB), "nicht einmal die Zinsen", ROT),
               ("nahe", ("tabler", "heart-handshake", 120, PINK), "Ehegatte", PINK)]),
    *paar("AN", [("w138", "ruhig"), ("krass", "denkt"), ("nahe", "ruhig")], "GE", [("w138", "ruhig"), ("nahe", "froh")]),
]))

# ===========================================================================================================================
# E2 Vermutung und Widerlegung (XI ZR 82/11 Rn. 9; XI ZR 32/16 Rn. 20)
# ===========================================================================================================================
folie([("verm", "§ 138 Abs. 1 BGB › 3. Vermutung"), ("widerl", "§ 138 Abs. 1 BGB › Widerlegung durch die Bank")], rechts_frei([
    *tafel("verm", "Folge: eine Vermutung"),
    z("Vermutet wird:", 110, 185, "verm", "Bold", 38),
    z("Bürgschaft allein aus emotionaler Verbundenheit", 160, 245, beim("verm", "emotionaler"), size=36),
    z("und die Bank hat das in sittlich anstößiger", 160, 300, beim("verm", "Bank"), size=36),
    z("Weise ausgenutzt", 160, 355, beim("verm", "ausgenutzt"), size=36),
    zit("BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9", 160, 410, beim("verm", "ausgenutzt")),
    z("Die Bank kann die Vermutung widerlegen,", 110, 500, "widerl", "Bold", 38),
    z("muss dafür aber vortragen und beweisen", 160, 560, beim("widerl", "vortragen"), size=36),
    zit("BGH, Urt. v. 15.11.2016 – XI ZR 32/16, Rn. 20", 160, 615, beim("widerl", "beweisen")),
    *requisit([("verm", ("tabler", "heart", 110, PINK), "emotionale Verbundenheit", PINK),
               ("widerl", ("tabler", "building-bank", 120, BLAU), "Bank muss beweisen", BLAU)]),
    *paar("WI", [("verm", "ernst"), ("widerl", "ruhig")], "AN", [("verm", "sorge"), ("widerl", "denkt")]),
]))

# ===========================================================================================================================
# F Subsumtion (XI ZR 32/16 Rn. 29 f.)
# ===========================================================================================================================
folie([("sub", "§ 138 Abs. 1 BGB › im Fall"), ("ehe", "§ 138 Abs. 1 BGB › im Fall: Nähe und Eigeninteresse")], rechts_frei([
    *tafel("sub", "Im Fall: Anneke"),
    z("Einkommen 0 €, Vermögen 0 €: pfändbar ist nichts", 110, 185, "kein", "Bold", 36),
    z("Zinsen 1.000 € im Monat: nicht tragbar", 110, 245, beim("zins2", "Zinsen"), size=36),
    *okz("krass überfordert", 310, beim("zins2", "krass"), "Bold", 36, x=160),
    *okz("Ehefrau: persönlich besonders nahe", 390, "ehe", "Bold", 36, x=160),
    *neinz("kein eigenes Interesse: Werkstatt gehört Gero", 470, "eigen", "Bold", 36, x=160),
    z("Familie profitiert: nur mittelbarer Vorteil", 160, 535, beim("mittelb", "mittelbarer"), size=36),
    zit("BGH, Urt. v. 15.11.2016 – XI ZR 32/16, Rn. 29 f.", 160, 588, beim("mittelb", "Vorteil")),
    *neinz("Vermutung nicht widerlegt", 660, "nichts", "Bold", 36, x=160),
    *requisit([("sub", ("tabler", "wallet", 110, WEISS), "Anneke: 0 €", WEISS),
               ("zins2", ("tabler", "coin-euro", 110, GELB), "Zinsen: 1.000 € im Monat", ROT),
               ("ehe", (FE, "ring", 90, GELB), "Ehefrau", PINK),
               ("eigen", (FE, "toolbox", 120, ROT), "Werkstatt: nur Gero", WEISS)]),
    *paar("AN", [("sub", "denkt"), ("zins2", "sorge"), ("nichts", "ruhig")], "GE", [("sub", "sorge"), ("eigen", "ruhig")]),
]))

# ===========================================================================================================================
# G Ergebnis (Bühne)
# ===========================================================================================================================
WX9, AX9, GX9 = 470, 1120, 1660
folie([("erg", "Ergebnis · Bürgschaft nichtig, § 138 Abs. 1 BGB")], [
    blk(80, 40, 1760, 100, GRUEN, "erg", [("Ergebnis: Bürgschaft sittenwidrig, nach § 138 Abs. 1 BGB nichtig", "ExtraBold", 40, INK)]),
    boden("erg"),
    ficon("tabler", "building-bank", 170, 420, 130, "erg", fuell=BLAU),
    *fig("WI", WX9, BODEN, FH, [("erg", "ernst_r")], erst="pop"),
    ns("Herr Wittkamp", WX9, BODEN, "erg", NFARBE["WI"], d=0.1),
    *fig("AN", AX9, BODEN, FH, [("erg", "ruhig"), ("erg2", "froh")], erst="pop", d=0.1),
    ns("Anneke", AX9, BODEN, "erg", NFARBE["AN"], d=0.2),
    *fig("GE", GX9, BODEN, FH, [("erg", "ruhig"), ("erg2", "froh")], erst="pop", d=0.2),
    ns("Gero", GX9, BODEN, "erg", NFARBE["GE"], d=0.3),
    ficon("tabler", "file-off", 800, 560, 140, beim("erg", "nichtig"), fuell=WEISS),
    pl("Bürgschaft nichtig", 760, 360, beim("erg", "nichtig"), fill=WEISS, size=32, anker="m"),
    pl("Anneke muss nichts zahlen", AX9, 230, "erg2", fill=GELB, size=34, anker="m"),
])

# ===========================================================================================================================
# H Gegenfall: eigenes Interesse (XI ZR 32/16 Rn. 29 f.; BVerfGE 89, 214, 235 f.)
# ===========================================================================================================================
folie([("gegen", "Gegenfall · eigenes Interesse am Kredit"), ("bf2", "Gegenfall › Bürgschaftsbeschluss, zweite Beschwerde")],
      rechts_frei([
    *tafel("gegen", "Gegenfall: eigenes Interesse"),
    z("Eigenes Interesse am Kredit, etwa: Das finanzierte", 110, 185, "gegen", "Bold", 34),
    z("Objekt gehört der bürgenden Person zur Hälfte", 160, 237, beim("gegen", "Hälfte"), size=34),
    *okz("Vermutung widerlegt", 305, beim("gegen", "widerlegt"), "Bold", 36, x=160),
    zit("BGH, Urt. v. 15.11.2016 – XI ZR 32/16, Rn. 29 f.", 160, 360, beim("gegen", "widerlegt")),
    z("Bürgschaftsbeschluss: Ehefrau ohne Einkommen", 110, 440, beim("bf2", "Ehefrau"), "Bold", 34),
    *neinz("Verfassungsbeschwerde ohne Erfolg", 500, beim("bf2", "Verfassungsbeschwerde"), "Bold", 34, x=160),
    z("Konsumkredit ihres Mannes in üblicher Höhe", 160, 560, beim("bf2", "Konsumkredit"), size=34),
    z("eigenes Interesse durfte angenommen werden", 160, 615, beim("bf2", "annehmen"), size=34),
    zit("BVerfGE 89, 214 (235 f.)", 160, 668, beim("bf2", "interessiert")),
    *requisit([("gegen", ("tabler", "home", 120, GELB), "gehört ihr zur Hälfte", GELB),
               (beim("bf2", "Konsumkredit"), ("tabler", "shopping-cart", 110, WEISS), "Konsumkredit", WEISS)]),
    *paar("AN", [("gegen", "denkt"), ("bf2", "ruhig")], "GE", [("gegen", "ruhig")]),
]))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · § 138 BGB beim Entstehen prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Sittenwidrigkeit beim Bürgschaftsvertrag,", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("also beim Entstehen des Anspruchs", 250, 255, beim("tipp", "Entstehen"), size=36),
    z("2. Prognose bei Abgabe der Erklärung,", 200, 345, "tipp2", "Bold", 36),
    z("nicht erst die spätere Pleite", 250, 400, beim("tipp2", "nicht"), size=36),
    zit("BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9", 250, 455, beim("tipp2", "Pleite")),
    z("3. Überforderung am Sachverhalt nachrechnen,", 200, 540, "tipp3", "Bold", 36),
    z("die Ausnutzung wird vermutet", 250, 595, beim("tipp3", "Ausnutzung"), size=36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema (progressiv)
# ===========================================================================================================================
K1, K2, K3 = 150, 230, 310
folie([("sch", "Klausurschema"), ("k1b", "Klausurschema › I. 2. keine Nichtigkeit, § 138 Abs. 1 BGB"),
       ("k2", "Klausurschema › II. nicht erloschen"), ("k3", "Klausurschema › III. durchsetzbar")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anspruch aus § 765 Abs. 1 BGB"), 110, 90, "sch", 46),
    z("I. Anspruch entstanden", K1, 185, "k1", "Bold", 40, rechts=1820),
    z("1. Bürgschaftsvertrag und Form (§§ 765 Abs. 1, 766 S. 1 BGB)", K2, 245, "k1a", size=34, rechts=1820),
    z("2. keine Nichtigkeit nach § 138 Abs. 1 BGB", K2, 300, "k1b", size=34, rechts=1820),
    z("a) krasse finanzielle Überforderung", K3, 352, "k1c", size=34, rechts=1820),
    z("b) besondere persönliche Nähe", K3, 404, beim("k1d", "besondere"), size=34, rechts=1820),
    z("c) Vermutung nicht widerlegt", K3, 456, beim("k1e", "Vermutung"), size=34, rechts=1820),
    z("3. Bestehen der Hauptschuld", K2, 511, "k1f", size=34, rechts=1820),
    z("II. Anspruch nicht erloschen", K1, 590, "k2", "Bold", 40, rechts=1820),
    z("III. Anspruch durchsetzbar", K1, 670, "k3", "Bold", 40, rechts=1820),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 175, "merke", 84, anker="m"),
    *markertext([[("Kann eine ", 0), ("nahestehende Person", "a"), (" nicht", 0)],
                 [("einmal die ", 0), ("Zinsen", "b"), (" tragen,", 0)]],
                750, 310, 44, "merke", {"a": beim("merke", "nahestehende"), "b": beim("merke", "Zinsen")}),
    *markertext([[("ist ihre Bürgschaft in der Regel", 0)], [("sittenwidrig", "c"), (",", 0)]],
                750, 450, 44, "m2", {"c": beim("m2", "sittenwidrig")}),
    *markertext([[("es sei denn, die Bank ", 0), ("widerlegt", "d")], [("die Vermutung.", 0)]],
                750, 600, 44, "m3", {"d": beim("m3", "widerlegt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
