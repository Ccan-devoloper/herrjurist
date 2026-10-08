"""Folge 267 · Konkludente Täuschung beim Betrug: Lügen ohne falsches Wort – Serienstandard Open Peeps (Katzenkönig).
Fall 1: Freitagabend, Restaurant in der Altstadt (erfunden, ohne Namen und Marke). Baldur bestellt ein Drei-Gänge-Menü,
obwohl er kein Geld hat; Kellnerin Kaja serviert, Rechnung 48 €. Fall 2: Ortrud (Privatperson) hat eine Geburtstagsanzeige
aufgegeben und erhält von Herrn Weinert ein rechnungsähnliches Angebotsschreiben (89,60 €, „zahlbar binnen 10 Tagen“,
ausgefüllter Überweisungsträger, Angebotshinweis nur im Kleingedruckten). Szenen laut ../SZENENPLAN.md:
A1 Restaurant, A2 Ortrud und der Brief, A3 Herr Weinert im Büro, A4 Frage, B Sachverhalt, C § 263 Abs. 1 (Wortlautkarte),
D drei Wege und Maßstab, E1 Fall 1 Tafel, E2 Abgrenzung: Entschluss nach dem Essen (Restaurant, Baldur schleicht zur Tür),
F1 Fall 2: das Schreiben mit Rechnungsmerkmalen (BGHSt 47, 1), F2 planmäßig/direkter Vorsatz, F3 Kleingedrucktes,
F4 Kaufleute, Ergebnis, G Tun oder Unterlassen, H Klausurtipp (Lexi), I Schema, J Merksatz (Lexi).
Kein Richterhammer. Zwei Handlungsgeräusche (Teller, Brief im Kasten; ../geraeusche_herkunft.json). Namensschild jeder
Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/flurboden als
eigene Kopie aus Folge 264 (gemeinsame Dateien unverändert), geht() wie Folge 243. Zahlen auf Tafeln, Pillen und Blasen als
Ziffern. Wortlautkarte § 263 Abs. 1 wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026; amtliche Schreibung „daß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_267/"

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
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_267/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 249/252) -----------------------------------
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


def geht(e, s0, s1, dx, dy=0):
    """Bewegung (wie Folge 243): Element startet um (dx, dy) versetzt und kommt zwischen s0 und s1 an seiner Position an."""
    e.weg = (s0, s1, dx, dy)
    return e


BODEN_T = (214, 206, 192, 255)               # Steinboden (Büro)
BODEN_H = (222, 196, 160, 255)               # Holzboden (Restaurant, Wohnung)
F_O, F_U = 930, 1000                         # Bodenfläche (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def flurboden(cue, farbe, fugen=True):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=farbe)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    if fugen:
        for x in range(100, 1860, 220):
            dr.line(((x + 30) * s, 6 * s, (x - 10) * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


X1, X2 = 1400, 1745                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"BA": "Baldur", "KJ": "Kellnerin Kaja", "OD": "Ortrud", "WN": "Herr Weinert"}
NFARBE = {"BA": LILAHELL, "KJ": WEISS, "OD": BLAUHELL, "WN": HELLGRUEN}
for _a, _b in (("BA", "WN"), ("KJ", "OD"), ("BA", "KJ"), ("OD", "WN")):   # Schilder nebeneinander berühren sich nicht
    assert X1 + F("Bold", 30).getlength(NAME[_a]) / 2 + 30 + 12 < X2 - F("Bold", 30).getlength(NAME[_b]) / 2 - 30


def requisit(folge, px=PX, py=PY, pu=PU):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe[, bis])]."""
    els = []
    for i, eintrag in enumerate(folge):
        c, ic, txt, pf = eintrag[:4]
        b = eintrag[4] if len(eintrag) > 4 else (folge[i + 1][0] if i + 1 < len(folge) else None)
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def tisch(cx, c0, breite=420, y=735, bis=None):
    """Restauranttisch (Holzplatte, zwei Beine) vor der Figur."""
    x0 = cx - breite // 2
    return [bis_(hart(karte(x0, y, breite, 30, c0, fill=HOLZ, rund=8, schatten=4, rand=4, anim="cut")), bis),
            bis_(hart(linienzug([(x0 + 50, y + 32), (x0 + 50, F_O)], c0, breite=10)), bis),
            bis_(hart(linienzug([(x0 + breite - 50, y + 32), (x0 + breite - 50, F_O)], c0, breite=10)), bis)]


FENSTER, TUER = 1570, 1790                  # Restaurant: Fenster und Tür rechts


def restaurant(c0):
    """Restaurant in der Altstadt (erfunden, ohne Namen): Holzboden, Fenster, Tür, Pflanze."""
    return [hart(flurboden(c0, BODEN_H, fugen=False)),
            hart(ficon("tabler", "window", FENSTER, 410, 200, c0, fuell=BLAUHELL, anim="cut")),
            hart(ficon("tabler", "door", TUER, F_O + 8, 170, c0, fuell=HOLZ, anim="cut")),
            hart(ficon("tabler", "plant-2", 1080, F_O + 8, 130, c0, fuell=GRUEN, anim="cut"))]


# ===========================================================================================================================
# A1 Fall 1: Freitagabend im Restaurant
# ===========================================================================================================================
BAX, KJX, TX = 760, 1300, 760               # Baldur (hinter dem Tisch), Kaja, Tisch
P0 = "Fall 1"
folie([(NULL, f"{P0} · Freitagabend im Restaurant"), ("baldur", f"{P0} · Baldur am Tisch"), ("leer", f"{P0} · kein Geld, Konto leer"),
       ("kaja", f"{P0} · Kellnerin Kaja"), ("b1", f"{P0} · „Einmal das Drei-Gänge-Menü“"), ("essen", f"{P0} · Suppe, Hauptgang, Nachtisch"),
       ("rech", f"{P0} · Rechnung: 48 €"), ("b2", f"{P0} · „Ich kann nicht bezahlen“")], [
    *restaurant(NULL),
    hart(pl("Freitagabend: ein Restaurant in der Altstadt", 70, 30, NULL, fill=GELB, size=40)),
    *fig("BA", BAX, FU, FH, [(NULL, "ruhig_r"), ("leer", "denkt_r")], bis="b1", erst="cut"),
    *redet("BA_redet_r", BAX, FU, FH, "b1", "k1"),
    *fig("BA", BAX, FU, FH, [("k1", "froh_r"), (beim("essen", "isst"), "isst_r"), ("rech", "sorge_r")], bis="b2", erst="cut"),
    *redet("BA_redet2_r", BAX, FU, FH, "b2", "ortrud"),
    ns("Baldur", BAX, FU, NULL, LILAHELL),
    *tisch(TX, NULL),
    pl("Kein Geld dabei, Konto leer – und das weiß er", 70, 105, "leer", fill=WEISS, size=32),
    ficon("tabler", "wallet-off", 1000, 640, 120, "leer", fuell=WEISS, bis="b1"),
    *fig("KJ", KJX, FU, FH, [("kaja", "ruhig")], bis="k1", erst="pop"),
    *redet("KJ_redet", KJX, FU, FH, "k1", "essen"),
    *fig("KJ", KJX, FU, FH, [("essen", "froh"), ("rech", "ruhig"), ("b2", "staunt")], bis="ortrud", erst="cut"),
    ns("Kellnerin Kaja", KJX, FU, "kaja", WEISS, d=0.1),
    blase("sprech", 560, 170, "b1", 1040, 320, inhalt=["Einmal das", "Drei-Gänge-Menü, bitte."], textsize=34,
          figur=("BA_redet_r", BAX, FU, FH), bis="k1"),
    blase("sprech", 480, 150, "k1", 1130, 320, inhalt=["Sehr gern,", "kommt sofort."], textsize=34,
          figur=("KJ_redet", KJX, FU, FH), bis="essen"),
    szene(ficon("tabler", "soup", TX - 60, 738, 120, beim("essen", "Suppe"), fuell=GELB, bis=beim("essen", "Hauptgang")),
          "267teller*", 0.8, 0.0),
    ficon("fluent-emoji-flat", "spaghetti", TX - 60, 738, 120, beim("essen", "Hauptgang"), bis=beim("essen", "Nachtisch")),
    ficon("fluent-emoji-flat", "shortcake", TX - 60, 738, 100, beim("essen", "Nachtisch"), bis="rech"),
    pl("Suppe, Hauptgang, Nachtisch: Baldur isst alles auf", 70, 172, "essen", fill=WEISS, size=32),
    ficon("tabler", "receipt-euro", TX + 80, 738, 100, "rech", fuell=WEISS),
    pl("Rechnung: 48 €", 70, 239, "rech", fill=HELLROT, size=32),
    blase("sprech", 600, 170, "b2", 1060, 320, inhalt=["Tut mir leid, ich kann", "nicht bezahlen."], textsize=34,
          figur=("BA_redet2_r", BAX, FU, FH)),
])


# ===========================================================================================================================
# Brief von Herrn Weinert (eigenes Muster, erfunden): Registernummer, Betrag, Zahlungsfrist, Überweisungsträger,
# Angebotshinweis nur im Kleingedruckten
# ===========================================================================================================================
def brief(x, y, w, c, k, groesse=1.0, bis=None):
    """k = dict(reg, betrag, frist, ueber, klein) mit den Cues der Einzelteile. Gibt (els, geometrie) zurück."""
    g = groesse
    h = int(660 * g)
    els = [bis_(karte(x, y, w, h, c, fill=WEISS, rund=10, schatten=6, rand=4), bis)]
    geo = {}
    geo["reg"] = (x + 40, y + int(34 * g))
    els.append(z("Reg.-Nr. 26-0417-AZ", x + 40, y + int(34 * g), k["reg"], "Bold", int(34 * g), rechts=x + w - 16, bis=bis))
    els.append(z("Betrag: 89,60 €", x + 40, y + int(130 * g), k["betrag"], "ExtraBold", int(54 * g), rechts=x + w - 16, bis=bis))
    geo["betrag"] = (x + 40, y + int(130 * g))
    els.append(z("zahlbar binnen 10 Tagen", x + 40, y + int(225 * g), k["frist"], "ExtraBold", int(42 * g), rechts=x + w - 16, bis=bis))
    geo["frist"] = (x + 40, y + int(225 * g))
    uy = y + int(320 * g)
    els.append(bis_(karte(x + 30, uy, w - 60, int(150 * g), k["ueber"], fill=BLAUHELL, rund=8, schatten=0, rand=3), bis))
    els.append(z("Überweisung · 89,60 €", x + 56, uy + int(22 * g), k["ueber"], "Bold", max(26, int(32 * g)), rechts=x + w - 40, bis=bis))
    els.append(z("Verwendungszweck: 26-0417-AZ", x + 56, uy + int(80 * g), k["ueber"], size=max(26, int(30 * g)), rechts=x + w - 40, bis=bis))
    geo["ueber"] = (x + 30, uy, w - 60, int(150 * g))
    ky = y + h - int(110 * g)
    els.append(z("Dies ist ein Angebot für einen Eintrag", x + 40, ky, k["klein"], size=26, farbe=TEXT, rechts=x + w - 16, bis=bis))
    els.append(z("in einem Internetportal.", x + 40, ky + 36, k["klein"], size=26, farbe=TEXT, rechts=x + w - 16, bis=bis))
    geo["klein"] = (x + 40, ky)
    return els, geo


# ===========================================================================================================================
# A2 Fall 2: Ortrud und der Brief im Kasten
# ===========================================================================================================================
ODX, MBX = 1480, 230
BRX, BRY, BRW = 420, 250, 640
br_a, geo_a = brief(BRX, BRY, BRW, "rmerk", dict(reg="rmerk", betrag=beim("rmerk", "Betrag"),
                                               frist=beim("rmerk", "fett"), ueber="ueber", klein="klein"))
P2 = "Fall 2"
folie([("ortrud", f"{P2} · Ortrud gibt eine Anzeige auf"), ("brief", f"{P2} · ein Brief im Kasten"),
       ("rmerk", f"{P2} · Registernummer, Betrag, Zahlungsfrist"), ("ueber", f"{P2} · ausgefüllter Überweisungsträger"),
       ("o1", f"{P2} · „Die Rechnung für meine Anzeige“"), ("klein", f"{P2} · das Kleingedruckte")], [
    hart(flurboden("ortrud", BODEN_H, fugen=False)),
    pl("Ortrud: Anzeige in der Tageszeitung", 70, 30, "ortrud", fill=GELB, size=40),
    pl("zum 80. Geburtstag ihrer Schwester", 70, 105, beim("ortrud", "Geburtstag"), fill=WEISS, size=32),
    ficon("fluent-emoji-flat", "newspaper", 640, 720, 260, "ortrud", bis="rmerk"),
    ficon("fluent-emoji-flat", "birthday-cake", 920, 720, 170, beim("ortrud", "Geburtstag"), bis="rmerk"),
    ficon("fluent-emoji-flat", "closed-mailbox-with-raised-flag", MBX, F_O + 8, 230, "brief", anim="cut"),
    szene(ficon("fluent-emoji-flat", "envelope", MBX, 650, 130, "brief", bis="rmerk"), "267brief*", 0.8, 0.0),
    pl("3 Tage später: ein Brief im Kasten", 70, 172, "brief", fill=WEISS, size=32),
    *br_a,
    ring(geo_a["reg"][0] + 170, geo_a["reg"][1] + 22, 205, 40, beim("rmerk", "Registernummer"), bis=beim("rmerk", "Betrag")),
    ring(geo_a["frist"][0] + 250, geo_a["frist"][1] + 26, 285, 46, beim("rmerk", "fett"), bis="ueber"),
    *fig("OD", ODX, FU, FH, [("ortrud", "ruhig"), ("rmerk", "liest")], bis="o1", erst="pop"),
    *redet("OD_redet", ODX, FU, FH, "o1", "klein"),
    *fig("OD", ODX, FU, FH, [("klein", "froh")], bis="weinert", erst="cut"),
    ns("Ortrud", ODX, FU, "ortrud", BLAUHELL, d=0.1),
    blase("sprech", 640, 170, "o1", 1370, 280, inhalt=["Ach, die Rechnung für meine", "Anzeige. Die zahle ich gleich."],
          textsize=31, figur=("OD_redet", ODX, FU, FH), bis="klein"),
    ficon("fluent-emoji-flat", "magnifying-glass-tilted-left", BRX + BRW + 80, geo_a["klein"][1] + 90, 120, "klein"),
    blk(1090, 100, 790, 120, WEISS, beim("klein", "Dies"), [("„Dies ist ein Angebot für einen Eintrag", "Bold", 28, INK),
                                                           ("in einem Internetportal.“", "Bold", 28, INK)]),
])

# ===========================================================================================================================
# A3 Fall 2: Herr Weinert im Büro
# ===========================================================================================================================
WNX, DSX = 1250, 560
folie([("weinert", f"{P2} · Absender: Herr Weinert"), ("w1", f"{P2} · „Kein falsches Wort“")], [
    hart(flurboden("weinert", BODEN_T)),
    pl("Absender des Schreibens: Herr Weinert", 70, 30, "weinert", fill=GELB, size=40),
    pl("setzt darauf: Kaum jemand liest das Kleingedruckte", 70, 105, beim("weinert", "setzt"), fill=WEISS, size=32),
    hart(karte(DSX - 260, 735, 520, 30, "weinert", fill=HOLZ, rund=8, schatten=4, rand=4, anim="cut")),
    hart(linienzug([(DSX - 210, 767), (DSX - 210, F_O)], "weinert", breite=10)),
    hart(linienzug([(DSX + 210, 767), (DSX + 210, F_O)], "weinert", breite=10)),
    ficon("tabler", "device-laptop", DSX - 110, 738, 190, "weinert", fuell=WEISS, anim="cut"),
    ficon("tabler", "mail", DSX + 120, 738, 110, "weinert", fuell=WEISS, anim="cut"),
    ficon("tabler", "mail", DSX + 140, 690, 110, "weinert", fuell=WEISS, anim="cut"),
    ficon("tabler", "mail", DSX + 125, 642, 110, beim("weinert", "setzt"), fuell=WEISS),
    *fig("WN", WNX, FU, FH, [("weinert", "ruhig")], bis="w1", erst="pop"),
    *redet("WN_redet", WNX, FU, FH, "w1", "frage"),
    ns("Herr Weinert", WNX, FU, "weinert", HELLGRUEN, d=0.1),
    blase("sprech", 820, 170, "w1", 860, 300, inhalt=["Im Kleingedruckten steht doch alles.", "Ich habe kein falsches Wort geschrieben."],
          textsize=30, figur=("WN_redet", WNX, FU, FH)),
])

# ===========================================================================================================================
# A4 Die Frage
# ===========================================================================================================================
FQ1, FQ2 = 620, 1320
folie([("frage", "Fall · Die Frage")], [
    hart(flurboden("frage", BODEN_H, fugen=False)),
    pl("Baldur hat nicht gelogen", 70, 30, "frage", fill=WEISS, size=38),
    pl("Weinert auch nicht", 70, 102, beim("frage", "Weinert"), fill=WEISS, size=38),
    pl("Haben beide trotzdem getäuscht?", 70, 174, "frage2", fill=PINK, size=40),
    *fig("BA", FQ1, FU, FH, [("frage", "ruhig_r"), ("frage2", "denkt_r")], erst="cut"),
    ns("Baldur", FQ1, FU, "frage", LILAHELL),
    *tisch(FQ1 + 40, "frage", breite=360),
    ficon("tabler", "receipt-euro", FQ1 + 120, 738, 90, "frage", fuell=WEISS, anim="cut"),
    *fig("WN", FQ2, FU, FH, [("frage", "ruhig"), ("frage2", "denkt")], erst="cut"),
    ns("Herr Weinert", FQ2, FU, "frage", HELLGRUEN),
    ficon("tabler", "file-invoice", FQ2 + 300, F_O + 8, 150, "frage", fuell=WEISS, anim="cut"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_267(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 85, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_267("sv", [
    "Freitagabend bestellt Baldur in einem Restaurant ein Drei-Gänge-Menü. Er hat kein Geld dabei, sein Konto ist leer, "
    "und er weiß, dass er nicht zahlen kann. Kellnerin Kaja serviert. Nach dem Nachtisch bringt sie die Rechnung über 48 €; "
    "Baldur kann nicht bezahlen.",
    "Ortrud hat in der Tageszeitung eine Anzeige zum 80. Geburtstag ihrer Schwester aufgegeben. Drei Tage später erhält sie "
    "ein Schreiben von Herrn Weinert: oben eine Registernummer, in der Mitte ein Betrag von 89,60 €, fett gedruckt "
    "„zahlbar binnen 10 Tagen“, dazu ein ausgefüllter Überweisungsträger. Nur ganz unten steht klein gedruckt, dass es "
    "sich um ein Angebot für einen Eintrag in einem Internetportal handelt.",
    "Weinert setzt planmäßig darauf, dass die Empfänger das Schreiben für eine Rechnung halten. Ortrud hält es für die "
    "Rechnung der Zeitung und überweist 89,60 €. Der Eintrag ist für sie wertlos.",
], "Haben Baldur und Weinert getäuscht (§ 263 Abs. 1 StGB)?")

# ===========================================================================================================================
# C § 263 Abs. 1 StGB: Wortlaut, Täuschung über Tatsachen
# ===========================================================================================================================
W263 = ["„(1) Wer in der Absicht, sich oder einem Dritten einen",
        "rechtswidrigen Vermögensvorteil zu verschaffen, das",
        "Vermögen eines anderen dadurch beschädigt, daß er durch",
        "Vorspiegelung falscher oder durch Entstellung oder",
        "Unterdrückung wahrer Tatsachen einen Irrtum erregt oder",
        "unterhält, …“"]
w263, w263_y = wortlaut(80, 175, 1100, W263, "§ 263 Abs. 1 StGB", "p263", marken=[
    (3, "Vorspiegelung falscher", beim("tats", "spiegelt")), (3, "Entstellung", beim("tats", "entstellt")),
    (4, "Unterdrückung wahrer", beim("tats", "unterdrückt")), (4, "Tatsachen", beim("tats", "wahre"))], size=32)
PC = "§ 263 Abs. 1 StGB"
folie([("p263", f"{PC} › Wortlaut"), ("tats", f"{PC} › Täuschung über Tatsachen"), ("verw", f"{PC} › hier nur: die Täuschung")], rechts_frei([
    *tafel("p263", "Betrug: am Anfang die Täuschung", h=860, size=46),
    *w263,
    blk(110, w263_y + 30, 1040, 130, BLAUHELL, "verw", [("Irrtum, Vermögensverfügung, Schaden:", "ExtraBold", 33, INK),
                                                        ("siehe Betrugsschema", "Regular", 33, INK)]),
    pl("hier: nur die Täuschung", 110, w263_y + 190, beim("verw", "hier"), fill=GELB, size=34),
    *requisit([("p263", ("tabler", "book", 110, WEISS), "§ 263 StGB", GELB),
               ("tats", ("tabler", "question-mark", 90, None), "Täuschung", WEISS),
               ("verw", ("tabler", "list", 100, WEISS), "Betrugsschema", WEISS)]),
    *stehend("BA", X1, [("p263", "ruhig"), ("tats", "denkt"), ("verw", "ruhig")]),
    *stehend("WN", X2, [("p263", "ruhig"), ("tats", "ernst")]),
]))

# ===========================================================================================================================
# D Drei Wege der Täuschung und der Maßstab
# ===========================================================================================================================
PD = "Täuschung"
folie([("drei", f"{PD} › drei Wege"), ("ausdr", f"{PD} › 1. ausdrücklich"), ("konkl", f"{PD} › 2. konkludent"),
       ("unterl", f"{PD} › 3. durch Unterlassen"), ("mass", f"{PD} › Maßstab: Verkehrsanschauung")], rechts_frei([
    *tafel("drei", "Drei Wege der Täuschung", h=860, size=46),
    z("1. ausdrücklich: bewusst unwahre Behauptung", 110, 180, "ausdr", "Bold", 34),
    z("2. konkludent: Verhalten mit stillschweigender", 110, 250, "konkl", "Bold", 34),
    z("Erklärung nach der Verkehrsanschauung", 150, 296, beim("konkl", "Verkehrsanschauung"), size=34),
    z("3. Unterlassen: Irrtum nicht aufgeklärt,", 110, 366, "unterl", "Bold", 34),
    z("obwohl eine Pflicht dazu besteht", 150, 412, beim("unterl", "verpflichtet"), size=34),
    blk(110, 492, 1040, 130, GELB, "mass", [("Maßstab: Was erklärt das Verhalten", "ExtraBold", 34, INK),
                                           ("nach der Verkehrsanschauung mit?", "ExtraBold", 34, INK)]),
    pl("konkrete Situation", 110, 650, beim("mass2", "Situation"), fill=WEISS, size=30),
    pl("Geschäftstyp", 470, 650, beim("mass2", "Geschäftstyp"), fill=WEISS, size=30),
    pl("Erwartungen der Beteiligten", 110, 722, beim("mass2", "Erwartungen"), fill=WEISS, size=30),
    zit("BGH 5 StR 181/06, Rn. 20–22; BGHSt 47, 1, 3", 110, 800, beim("mass2", "Beteiligten")),
    *requisit([("drei", ("tabler", "list-numbers", 100, WEISS), "3 Wege", GELB),
               ("ausdr", ("tabler", "message", 100, WEISS), "ausdrücklich", WEISS),
               ("konkl", ("tabler", "eye", 100, WEISS), "konkludent", WEISS),
               ("unterl", ("tabler", "eye-off", 100, WEISS), "Unterlassen", WEISS),
               ("mass", ("tabler", "scale", 110, WEISS), "Verkehrsanschauung", GELB)]),
    *stehend("KJ", X1, [("drei", "ruhig"), ("konkl", "staunt"), ("mass", "ruhig")]),
    *stehend("OD", X2, [("drei", "ruhig"), ("unterl", "liest"), ("mass2", "froh")]),
]))

# ===========================================================================================================================
# E1 Fall 1: die Bestellung
# ===========================================================================================================================
PE = "Fall 1 · Restaurant"
folie([("f1", f"{PE} › Täuschung?"), ("f1a", f"{PE} › ausdrücklich: nichts Falsches"),
       ("f1b", f"{PE} › Bestellung erklärt: kann und will zahlen"), ("f1c", f"{PE} › ähnlich: Tanken, Hotel"),
       ("f1d", f"{PE} › Erklärung falsch"), ("f1e", f"{PE} › konkludente Täuschung (+)"),
       ("f1f", f"{PE} › Irrtum, Verfügung, Schaden"), ("f1g", f"{PE} › Ergebnis: Betrug")], rechts_frei([
    *tafel("f1", "Fall 1: die Bestellung", h=860, size=46),
    *neinz("ausdrücklich: nichts Falsches gesagt", 175, "f1a", "Bold", 34, x=160),
    blk(110, 240, 1040, 130, BLAUHELL, "f1b", [("Bestellung erklärt schlüssig:", "ExtraBold", 34, INK),
                                               ("„Ich kann und will nach dem Essen bezahlen.“", "Regular", 32, INK)]),
    z("ähnlich: BGH zum Tanken und zu Hotelgästen", 110, 396, "f1c", size=32),
    zit("BGH 4 StR 632/11, Rn. 4; 4 StR 141/17, Rn. 6", 110, 442, beim("f1c", "Tanken")),
    z("Wirklichkeit: Baldur kann nicht zahlen – falsch", 110, 506, "f1d", "Bold", 32),
    *okz("konkludente Täuschung", 566, "f1e", "ExtraBold", 36, x=160),
    z("Kaja glaubt ihm und serviert:", 110, 640, "f1f", size=32),
    z("Irrtum, Verfügung, Schaden", 110, 684, beim("f1f", "Irrtum"), "Bold", 32),
    blk(110, 752, 1040, 86, HELLGRUEN, "f1g", [("Ergebnis: Betrug, § 263 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    *requisit([("f1", ("tabler", "tools-kitchen-2", 100, None), "Bestellung", GELB),
               ("f1b", ("tabler", "message", 100, WEISS), "„kann und will zahlen“", WEISS),
               ("f1c", ("tabler", "gas-station", 100, WEISS), "Tanken", WEISS, beim("f1c", "Hotelgästen")),
               (beim("f1c", "Hotelgästen"), ("tabler", "bed", 110, WEISS), "Hotelgäste", WEISS),
               ("f1d", ("tabler", "wallet-off", 100, WEISS), "kann nicht zahlen", HELLROT),
               ("f1f", ("tabler", "soup", 110, GELB), "Kaja serviert", WEISS),
               ("f1g", ("tabler", "circle-check", 100, GRUEN), "Betrug", GRUEN)]),
    *stehend("BA", X1, [("f1", "ruhig"), ("f1a", "froh"), ("f1d", "ernst"), ("f1g", "still")]),
    *stehend("KJ", X2, [("f1", "ruhig"), ("f1f", "froh"), ("f1g", "sorge")]),
]))

# ===========================================================================================================================
# E2 Abgrenzung: Entschluss erst nach dem Essen, Baldur schleicht zur Tür
# ===========================================================================================================================
KJ2 = 330
TS = beim("zech", "davonschleicht")
ZIELX = 1600
folie([("zech", "Fall 1 · Abwandlung › Entschluss erst nach dem Essen"), ("zech2", "Fall 1 · Abwandlung › Bestellung war wahr"),
       ("zech3", "Fall 1 · Abwandlung › Betrug (-)")], [
    *restaurant("zech"),
    pl("Abwandlung: Entschluss erst nach dem Essen", 70, 30, "zech", fill=GELB, size=40),
    pl("Bei der Bestellung: Erklärung noch wahr", 70, 105, "zech2", fill=WEISS, size=32),
    pl("heimliches Weggehen erklärt niemandem etwas", 70, 172, beim("zech2", "heimliche"), fill=WEISS, size=32),
    nein(110, 272, "zech3", gr=24),
    pl("Betrug scheidet aus", 150, 239, "zech3", fill=HELLROT, size=32),
    *fig("KJ", KJ2, FU, FH, [("zech", "ruhig")], erst="cut"),
    ns("Kellnerin Kaja", KJ2, FU, "zech", WEISS),
    peep_voll("BA_denkt_r", BAX, FU, FH, "zech", anim="cut", bis=TS),
    geht(peep_voll("BA_denkt_r", ZIELX, FU, FH, TS, anim="cut", bis="zech3"), TS, (TS[0], TS[1] + 1.8), BAX - ZIELX),
    peep_voll("BA_still_r", ZIELX, FU, FH, "zech3", anim="cut"),
    ns("Baldur", BAX, FU, "zech", LILAHELL, bis=TS),
    geht(ns("Baldur", ZIELX, FU, TS, LILAHELL), TS, (TS[0], TS[1] + 1.8), BAX - ZIELX),
    *tisch(TX, "zech"),
    ficon("fluent-emoji-flat", "fork-and-knife-with-plate", TX - 60, 738, 110, "zech", anim="cut"),
])

# ===========================================================================================================================
# F1 Fall 2: das Schreiben (BGHSt 47, 1): Rechnungsmerkmale prägen den Gesamteindruck
# ===========================================================================================================================
B2X, B2Y, B2W = 110, 250, 900
br_f, geo_f = brief(B2X, B2Y, B2W, "f2", dict(reg="f2", betrag="f2", frist="f2", ueber="f2", klein="f2"), groesse=1.0)
PF2 = "Fall 2 · Schreiben"
folie([("f2", f"{PF2} › Täuschung?"), ("f2a", f"{PF2} › jeder Satz wahr"), ("f2b", f"{PF2} › wahres Schreiben kann täuschen"),
       ("bgh", f"{PF2} › BGHSt 47, 1"), ("rm", f"{PF2} › Rechnungsmerkmale prägen den Gesamteindruck"),
       ("zpfl", f"{PF2} › erklärt schlüssig: Zahlungspflicht"), ("hint", f"{PF2} › Hinweis tritt zurück")], [
    pl("Fall 2: das Schreiben von Herrn Weinert", 70, 30, "f2", fill=GELB, size=40),
    pl("BGH, Urt. v. 26.4.2001 – 4 StR 439/00 (BGHSt 47, 1)", 70, 105, "bgh", fill=WEISS, size=30),
    pl("Angebotsschreiben wie Rechnungen", 70, 168, beim("bgh", "Angebotsschreiben"), fill=WEISS, size=30),
    *br_f,
    ring(geo_f["reg"][0] + 170, geo_f["reg"][1] + 22, 205, 40, beim("rm", "Registernummer")),
    ring(geo_f["betrag"][0] + 210, geo_f["betrag"][1] + 34, 245, 52, beim("rm", "Betrag")),
    ring(geo_f["frist"][0] + 250, geo_f["frist"][1] + 26, 285, 46, beim("rm", "Zahlungsfrist")),
    ring(geo_f["ueber"][0] + geo_f["ueber"][2] // 2, geo_f["ueber"][1] + geo_f["ueber"][3] // 2, geo_f["ueber"][2] // 2 + 20,
         geo_f["ueber"][3] // 2 + 18, beim("rm", "Überweisungsträger")),
    zit("BGHSt 47, 1, 3 f.", B2X + B2W - 250, B2Y + 660 + 16, "zpfl"),
    *requisit([("f2", ("tabler", "file-invoice", 100, WEISS), "Schreiben", WEISS),
               ("f2a", ("tabler", "circle-check", 100, GRUEN), "jeder Satz wahr", GRUEN),
               ("f2b", ("tabler", "question-mark", 90, None), "kann trotzdem täuschen", HELLROT),
               ("bgh", ("tabler", "building-bank", 120, BLAU), "Bundesgerichtshof", WEISS),
               ("rm", ("tabler", "receipt-euro", 100, WEISS), "Gesamteindruck", WEISS),
               ("zpfl", ("tabler", "message", 100, WEISS), "„Du musst zahlen!“", PINK),
               ("hint", ("fluent-emoji-flat", "magnifying-glass-tilted-left", 100, None), "Hinweis tritt zurück", WEISS)]),
    *stehend("OD", X1, [("f2", "ruhig"), ("rm", "liest"), ("zpfl", "staunt")]),
    *stehend("WN", X2, [("f2", "ruhig"), ("f2b", "denkt"), ("bgh", "ernst")]),
])

# ===========================================================================================================================
# F2 Wann täuscht ein wahres Schreiben? Planmäßig, Zweck, direkter Vorsatz
# ===========================================================================================================================
PF3 = "Fall 2 · wahres Schreiben"
folie([("plan", f"{PF3} › planmäßig eingesetzt"), ("zweck", f"{PF3} › Irrtum ist Zweck"), ("dv", f"{PF3} › direkter Vorsatz")], rechts_frei([
    *tafel("plan", "Wann täuscht ein wahres Schreiben?", h=620, size=44),
    *okz("Wirkung planmäßig eingesetzt", 180, "plan", "Bold", 34, x=160),
    *okz("Irrtum: nicht bloße Folge, sondern Zweck", 254, "zweck", "Bold", 34, x=160),
    zit("BGHSt 47, 1, 5", 160, 304, beim("zweck", "Zweck")),
    blk(110, 370, 1040, 130, GELB, "dv", [("direkter Vorsatz nötig –", "ExtraBold", 34, INK),
                                         ("bedingter Vorsatz genügt nicht", "ExtraBold", 34, INK)]),
    zit("BGHSt 47, 1, 5 f.", 110, 516, beim("dv", "bedingter")),
    *requisit([("plan", ("tabler", "target", 100, WEISS), "planmäßig", WEISS),
               ("zweck", ("tabler", "target", 100, ROT), "Zweck: Irrtum", HELLROT),
               ("dv", ("tabler", "bulb", 100, GELB), "direkter Vorsatz", GELB)]),
    *stehend("OD", X1, [("plan", "sorge"), ("dv", "ernst")]),
    *stehend("WN", X2, [("plan", "denkt"), ("zweck", "ernst")]),
]))

# ===========================================================================================================================
# F3 Und das Kleingedruckte?
# ===========================================================================================================================
PF4 = "Fall 2 · Kleingedrucktes"
folie([("klein2", f"{PF4} › erkennbar?"), ("klein3", f"{PF4} › beseitigt die Täuschung nicht"),
       ("sorg", f"{PF4} › kein Schutz vor jeder Sorglosigkeit"), ("sorg2", f"{PF4} › gezielt aufs Überlesen gesetzt")], rechts_frei([
    *tafel("klein2", "Und das Kleingedruckte?", h=720, size=46),
    z("Angebot bei genauem Hinsehen erkennbar?", 110, 180, "klein3", "Bold", 34),
    *okz("beseitigt die Täuschung nicht", 246, beim("klein3", "beseitigt"), "ExtraBold", 34, x=160),
    zit("BGHSt 47, 1, 6", 160, 296, beim("klein3", "Täuschung")),
    z("Zwar: kein Schutz vor jeder Sorglosigkeit", 110, 366, "sorg", size=34),
    zit("BGHSt 47, 1, 4", 110, 414, beim("sorg", "Sorglosigkeit")),
    blk(110, 478, 1040, 130, HELLGRUEN, "sorg2", [("Aber: Wer gezielt aufs Überlesen setzt,", "ExtraBold", 33, INK),
                                                  ("täuscht trotzdem.", "ExtraBold", 33, INK)]),
    zit("ebenso BGH 2 StR 616/12, Rn. 21 (Abofalle)", 110, 626, beim("sorg2", "täuscht")),
    *requisit([("klein2", ("fluent-emoji-flat", "magnifying-glass-tilted-left", 110, None), "Kleingedrucktes", WEISS),
               ("klein3", ("tabler", "eye", 100, WEISS), "erkennbar", WEISS),
               ("sorg", ("tabler", "shield-check", 100, WEISS), "Sorglosigkeit?", WEISS),
               ("sorg2", ("tabler", "eye-off", 100, WEISS), "Hinweis wird überlesen", HELLROT)]),
    *stehend("OD", X1, [("klein2", "liest"), ("klein3", "staunt"), ("sorg2", "ernst")]),
    *stehend("WN", X2, [("klein2", "ruhig"), ("klein3", "denkt"), ("sorg2", "still")]),
]))

# ===========================================================================================================================
# F4 Kaufleute, Ergebnis Fall 2
# ===========================================================================================================================
PF5 = "Fall 2 · Ergebnis"
folie([("kauf", f"{PF5} › Kaufleute? Ortrud: Privatperson"), ("f2e", f"{PF5} › Irrtum, Zahlung, Schaden"),
       ("f2f", f"{PF5} › Weinert: Betrug")], rechts_frei([
    *tafel("kauf", "Fall 2: das Ergebnis", h=660, size=46),
    z("geschäftserfahrene Kaufleute: früher zurückhaltender", 110, 180, "kauf", size=32),
    zit("BGH, Beschl. v. 27.2.1979 – 5 StR 805/78; dazu BGHSt 47, 1, 7", 110, 226, beim("kauf", "zurückhaltender")),
    *okz("Ortrud: Privatperson", 292, beim("kauf", "Privatperson"), "Bold", 34, x=160),
    z("Sie zahlt im Irrtum; der Eintrag ist für sie wertlos", 110, 376, "f2e", size=32),
    zit("Schaden: BGHSt 47, 1, 8", 110, 422, beim("f2e", "wertlos")),
    blk(110, 492, 1040, 86, HELLGRUEN, "f2f", [("Ergebnis: Betrug, § 263 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    *requisit([("kauf", ("tabler", "building-store", 110, WEISS), "Kaufleute?", WEISS),
               (beim("kauf", "Privatperson"), ("tabler", "users", 100, WEISS), "Privatperson", GRUEN),
               ("f2e", ("tabler", "receipt-euro", 100, WEISS), "zahlt im Irrtum", HELLROT),
               ("f2f", ("tabler", "circle-check", 100, GRUEN), "Betrug", GRUEN)]),
    *stehend("OD", X1, [("kauf", "ruhig"), ("f2e", "sorge")]),
    *stehend("WN", X2, [("kauf", "ruhig"), ("f2f", "still")]),
]))

# ===========================================================================================================================
# G Tun oder Unterlassen?
# ===========================================================================================================================
PG = "Abgrenzung"
folie([("tun", f"{PG} › Tun oder Unterlassen?"), ("tun2", f"{PG} › aktives Tun: Verhalten erklärt"),
       ("unt", f"{PG} › Unterlassen: Irrtum nicht aufgeklärt"), ("gar", f"{PG} › Garantenpflicht, § 13 Abs. 1 StGB")], rechts_frei([
    *tafel("tun", "Tun oder Unterlassen?", h=700, size=46),
    blk(110, 190, 1040, 130, HELLGRUEN, "tun2", [("aktives Tun: Baldur und Weinert erklären", "ExtraBold", 33, INK),
                                                 ("durch ihr Verhalten etwas", "Regular", 33, INK)]),
    blk(110, 356, 1040, 130, LILAHELL, "unt", [("Unterlassen: nichts erklärt, fremden", "ExtraBold", 33, INK),
                                              ("Irrtum nur nicht aufgeklärt", "Regular", 33, INK)]),
    z("nur mit Garantenpflicht zur Aufklärung, § 13 Abs. 1 StGB", 110, 522, "gar", "Bold", 32),
    zit("BGH, Beschl. v. 9.9.2025 – 5 StR 244/25, Rn. 9 f.", 110, 572, beim("gar", "Paragraf")),
    *requisit([("tun", ("tabler", "scale", 110, WEISS), "Tun oder Unterlassen?", GELB),
               ("tun2", ("tabler", "message", 100, WEISS), "aktiv erklärt", GRUEN),
               ("unt", ("tabler", "eye-off", 100, WEISS), "nicht aufgeklärt", LILAHELL),
               ("gar", ("tabler", "shield-check", 100, WEISS), "Garantenpflicht", WEISS)]),
    *stehend("BA", X1, [("tun", "ruhig"), ("unt", "denkt")]),
    *stehend("WN", X2, [("tun", "ruhig"), ("gar", "ernst")]),
]))

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · drei Schritte"), ("tipp1", "Klausurtipp · 1. ausdrückliche Lüge?"),
       ("tipp2", "Klausurtipp · 2. Erklärungswert"), ("tipp3", "Klausurtipp · 3. Unterlassen"),
       ("tipp4", "Klausurtipp · Zeitpunkt")], [
    *tafel("tipp", "Klausurtipp: drei Schritte", fill=HELL, h=740, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Gibt es eine ausdrückliche Lüge?", 200, 205, "tipp1", "Bold", 34),
    z("2. Was erklärt das Verhalten nach der", 200, 295, "tipp2", "Bold", 34),
    z("Verkehrsanschauung mit – und stimmt das?", 200, 345, beim("tipp2", "Verkehrsanschauung"), size=34),
    z("3. Erst danach: Unterlassen", 200, 435, "tipp3", "Bold", 34),
    z("mit Garantenpflicht", 200, 485, beim("tipp3", "Unterlassen"), size=34),
    z("Zeitpunkt: getäuscht wird bei der Bestellung,", 200, 585, "tipp4", "Bold", 34),
    z("nicht beim Weggehen", 200, 635, beim("tipp4", "nicht"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Schema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. ausdrückliche Erklärung"),
          ("s2", 0, "2. konkludente Erklärung"),
          ("s2a", 1, "a) Erklärungswert nach der Verkehrsanschauung"),
          ("s2b", 1, "b) Vergleich mit der Wirklichkeit"),
          ("s2c", 1, "c) wahre Erklärung: planmäßiger Gesamteindruck, direkter Vorsatz"),
          ("s3", 0, "3. Unterlassen: nur mit Garantenpflicht (§ 13 Abs. 1 StGB)")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Täuschung, § 263 Abs. 1 StGB"), 110, 90, "sch", 46)]
y = 225
for c, ebene, text in REIHEN:
    els_sch.append(z(text, 130 + 70 * ebene, y, c, "ExtraBold" if ebene == 0 else "Bold", 40 if ebene == 0 else 36, rechts=1820))
    y += 112 if ebene == 0 else 96
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › 1. ausdrücklich"), ("s2", "Schema › 2. konkludent"),
       ("s2a", "Schema › 2. a) Erklärungswert"), ("s2b", "Schema › 2. b) Vergleich mit der Wirklichkeit"),
       ("s2c", "Schema › 2. c) wahre Erklärung"), ("s3", "Schema › 3. Unterlassen")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer im Restaurant ", 0), ("bestellt", "a"), (", erklärt,", 0)],
                 [("dass er ", 0), ("zahlen kann und will", "b"), (".", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "bestellt"), "b": beim("merke", "zahlen")}),
    *markertext([[("Wer ", 0), ("planmäßig", "c"), (" eine Rechnung", 0)],
                 [("vortäuscht, täuscht auch", 0)],
                 [("mit ", 0), ("lauter wahren Sätzen", "d"), (".", 0)]], 750, 520, 46, "m2",
                {"c": beim("m2", "planmäßig"), "d": beim("m2", "lauter")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
