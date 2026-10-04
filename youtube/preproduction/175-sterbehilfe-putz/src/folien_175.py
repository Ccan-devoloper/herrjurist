"""Folge 175 · Sterbehilfe: aktiv, passiv, indirekt – Behandlungsabbruch (Fall Putz) – Serienstandard Open Peeps.
Fiktiver Rahmen: Strafrecht-Seminar mit Thilo (Student) und Professor Wedekind; danach der echte Fall sachlich nach
BGH, Urt. v. 25.6.2010 – 2 StR 454/09, BGHSt 55, 191 (nur mit Leitsatz/Rn.).
HÖCHSTE SENSIBILITÄT: Die Mutter, die Tochter, ihr Bruder und der Anwalt erscheinen NICHT als Figuren; die Handlung steht
nur als Text-Pille; kein Pflegebett, keine Sonde, kein Schlauch, keine Schere, kein Sterben im Bild. Im echten Fall nur
neutrale Icons (Gebäude, Kalender, Nachricht, Urkunde, Telefon, Dokument, Gericht, Waage, Richterhammer).
Keine Geräusche (keine sichtbare Handlung, die ein Handlungsgeräusch tragen sollte; ruhiger Ton).
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend/
paar/spricht_neben als eigene Kopie aus den Folgen 128/154 (gemeinsame Dateien unverändert).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_175/"

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
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (246, 243, 255, 255)
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
    lh = int(max(g for _, _, g, _ in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=lh, rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_175/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Norm- bzw. Leitsatztext wörtlich (gesetze-im-internet.de bzw. BGHSt-Leitsatz, Abruf 04.10.2026), als
    Zitat mit Fundstelle; marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 128/154) ----------------------------------------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
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


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (Kreuz zur gesprochenen Verneinung, ggf. eigener Cue)."""
    return [nein(x - 45, y + 20, kreuz or cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN = 860
FH = 440                                    # stehende Figur in der Seminarszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1600                                   # eine Figur neben der Tafel
PX, PY = 1575, 160                          # Pille über den Figuren
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
NAME = {"TH": "Thilo", "WD": "Prof. Wedekind"}
NFARBE = {"TH": LILA, "WD": GRUEN}


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def requisit(folge, px=PX, bis=None, pu=380, py=PY):
    """Wechselnde Pille (und Icon) rechts der Tafel: folge = [(cue, (set, icon, breite, fuell) | None, text, farbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b, anim="pop" if i == 0 else "cut"))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b, anim="pop" if i == 0 else "cut"))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(af, bf):
    """Tafelszene: Thilo und Professor Wedekind rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend("TH", X1, af), *stehend("WD", X2, bf)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def rednerpult(x, cue):
    """Rednerpult aus Grundformen (schräge Ablage, Säule, Fuß) auf dem Boden; x = linke Kante."""
    s = 2
    w, h = 170, 300
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.polygon([(o, o + 40 * s), (o + w * s, o), (o + w * s, o + 44 * s), (o, o + 70 * s)], fill=HOLZ, outline=INK, width=5 * s)
    dr.rectangle((o + 45 * s, o + 60 * s, o + (w - 45) * s, o + (h - 24) * s), fill=HOLZ, outline=INK, width=5 * s)
    dr.rounded_rectangle((o + 15 * s, o + (h - 26) * s, o + (w - 15) * s, o + h * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="pult"))


TAFEL_S = (60, 60, 600, 360)                # Whiteboard an der Wand (links oben)


def whiteboard(cue, fall=None, antwort=None):
    """Whiteboard des Seminars; ab 'fall' (Cue) steht dort der Fall Putz mit Fundstelle, ab 'antwort' die Antwort."""
    x, y, w, h = TAFEL_S
    els = [hart(karte(x, y, w, h, cue, fill=WEISS, rund=18, schatten=6, rand=4)),
           hart(z("Strafrecht-Seminar", x + 35, y + 18, cue, "ExtraBold", 36, rechts=x + w - 20)),
           hart(linienzug([(x, y + 78), (x + w, y + 78)], cue, breite=4))]
    if fall:
        c, an = fall
        neu = [z("Fall Putz", x + 35, y + 92, c, "ExtraBold", 42, rechts=x + w - 20),
               zit("BGH, Urt. v. 25.6.2010", x + 35, y + 152, c, rechts=x + w - 20),
               zit("2 StR 454/09 · BGHSt 55, 191", x + 35, y + 187, c, rechts=x + w - 20),
               ficon("tabler", "scale", x + w - 60, y + 70 + 75, 70, c, fuell=GELB)]
        els += [hart(e) for e in neu] if an == "cut" else neu
    if antwort:
        els += [z("entscheidend: Bezug zur Behandlung", x + 35, y + 240, antwort, "Bold", 30, rechts=x + w - 20),
                z("und Wille der Patientin", x + 35, y + 282, antwort, "Bold", 30, rechts=x + w - 20)]
    return els


THX, WDX = 760, 1500                        # Thilo links (blickt nach rechts), Wedekind rechts (blickt nach links)
PULT_X = 1680


def seminarraum(cue):
    return [boden(cue), rednerpult(PULT_X, cue),
            hart(ficon("tabler", "book-2", PULT_X + 92, BODEN - 300, 90, cue, fuell=BLAU, anim="cut")),
            hart(ficon("tabler", "plant-2", 230, BODEN, 120, cue, fuell=GRUEN, anim="cut"))]


# ===========================================================================================================================
# A1 Strafrecht-Seminar (fiktiv): der Hook als Text-Pillen, Frage und Antwort
# ===========================================================================================================================
HX = 1130                                   # Mitte der Hook-Pillen zwischen Whiteboard und Wedekind
folie([(NULL, "Fall · Im Strafrecht-Seminar"), ("wd1", "Die Frage · Ist das strafbar?"),
       ("klassiker", "Die Frage · Der Fall Putz")], [
    *seminarraum(NULL),
    *whiteboard(NULL, fall=(beim("klassiker", "Bundesgerichtshof"), "pop")),
    pl("echter Fall", HX, 110, beim("hook", "echten"), fill=GELB, size=30, anker="m", bis="wd1"),
    pl("Eine Frau liegt im Wachkoma, wird künstlich ernährt.", HX, 180, beim("hook", "Eine", 2), fill=WEISS, size=30,
       anker="m", bis="wd1"),
    pl("Früher hatte sie gesagt: Das will sie nicht.", HX, 250, "hook2", fill=WEISS, size=30, anker="m", bis="wd1"),
    pl("Auf Rat eines Anwalts durchtrennt die Tochter", HX, 320, "hook3", fill=ROTHELL, size=30, anker="m", bis="wd1"),
    pl("den Schlauch der Ernährungssonde.", HX, 385, beim("hook3", "Schlauch"), fill=ROTHELL, size=30, anker="m", bis="wd1"),
    # Thilo blickt zu Professor Wedekind (nach rechts)
    *fig("TH", THX, BODEN, FH, [(NULL, "ruhig_r"), ("hook3", "ernst_r"), ("wd1", "denkt_r")], bis="th1", erst="cut"),
    *redet("TH_redet_r", THX, BODEN, FH, "th1", "klassiker"),
    *fig("TH", THX, BODEN, FH, [("klassiker", "denkt_r")], erst="cut"),
    hart(ns("Thilo", THX, BODEN, NULL, LILA)),
    # Professor Wedekind blickt zu Thilo (nach links)
    *fig("WD", WDX, BODEN, FH, [(NULL, "ruhig"), ("hook3", "ernst")], bis="wd1", erst="cut"),
    *redet("WD_redet", WDX, BODEN, FH, "wd1", "th1"),
    *fig("WD", WDX, BODEN, FH, [("th1", "denkt"), ("klassiker", "ruhig")], erst="cut"),
    hart(ns("Prof. Wedekind", WDX, BODEN, NULL, GRUEN)),
    blase("sprech", 420, 160, "wd1", 1200, 250, inhalt=["Ist das strafbar?"], textsize=34,
          figur=("WD_redet", WDX, BODEN, FH), bis="th1"),
    blase("sprech", 640, 200, "th1", 1110, 260, inhalt=["Das ist doch aktive Sterbehilfe.", "Die ist immer strafbar."],
          textsize=32, figur=("TH_redet_r", THX, BODEN, FH), bis="klassiker"),
    pl("lange herrschende Meinung", HX, 150, beim("klassiker", "herrschende"), fill=WEISS, size=30, anker="m"),
    pl("BGH: anders entschieden", HX, 225, beim("klassiker", "anders"), fill=GELB, size=30, anker="m"),
])

# ===========================================================================================================================
# B 1. Die frühere Einteilung (Lehrbegriffe; BGHSt 55, 191 Rn. 27, 34)
# ===========================================================================================================================
P1 = "1. Frühere Einteilung (Lehre)"
folie([("begr", P1), ("aktiv", f"{P1} › aktive Sterbehilfe"), ("passiv", f"{P1} › passive Sterbehilfe"),
       ("indirekt", f"{P1} › indirekte Sterbehilfe"), ("grenze", f"{P1} › Grenze: Tun oder Unterlassen")], rechts_frei([
    *tafel("begr", "1. Die frühere Einteilung der Lehre"),
    blk(110, 180, 1040, 130, ROTHELL, "aktiv", [("aktiv: Jemand führt den Tod gezielt herbei.", "ExtraBold", 31, INK),
                                               ("stets verboten", "Bold", 31, INK)]),
    blk(110, 330, 1040, 130, GRUENHELL, "passiv", [("passiv: lebenserhaltende Maßnahmen unterlassen", "ExtraBold", 31, INK),
                                                  ("oder nicht fortgesetzt: unter Voraussetzungen erlaubt", "Bold", 31, INK)]),
    blk(110, 480, 1040, 130, BLAUHELL, "indirekt", [("indirekt: ärztlich gebotene Leidenslinderung,", "ExtraBold", 31, INK),
                                                   ("früherer Tod als mögliche Nebenfolge: ebenfalls erlaubt", "Bold", 31, INK)]),
    blk(110, 640, 1040, 90, GELB, "grenze", [("Die Grenze lief zwischen Tun und Unterlassen.", "ExtraBold", 32, INK)]),
    zit("Lehrbegriffe; so beschrieben in BGHSt 55, 191 Rn. 27, 34", 110, 750, beim("grenze", "Tun")),
    *paar([("begr", "ruhig"), ("grenze", "denkt")], [("begr", "ruhig"), ("aktiv", "ernst"), ("passiv", "ruhig")]),
    *requisit([("begr", None, "frühere Einteilung", WEISS), ("aktiv", None, "aktiv", ROTHELL), ("passiv", None, "passiv", GRUENHELL), ("indirekt", None, "indirekt", BLAUHELL),
               ("grenze", None, "Tun oder Unterlassen?", GELB)]),
]))

# ===========================================================================================================================
# C1 2. Der echte Fall: Wachkoma, der Wille der Mutter, die Betreuer (Rn. 3–7) – ohne Figuren, nur neutrale Icons
# ===========================================================================================================================
P2 = "2. Der echte Fall"
C1, C2, C3 = 340, 960, 1580
folie([("echt", f"{P2} · Fall Putz, BGHSt 55, 191"), ("koma", f"{P2} · Wachkoma"), ("wille", f"{P2} · Der Wille der Mutter"),
       ("betreuer", f"{P2} · Die Betreuer")], [
    boden("echt"),
    pl("Fall Putz · BGH, Urt. v. 25.6.2010 – 2 StR 454/09", 70, 30, "echt", fill=GELB, size=36),
    pl("nach dem Urteil", 1500, 62, beim("echt", "Urteil"), fill=WEISS, size=28, anker="m"),
    pl("die Mutter", C1, 135, beim("koma", "Mutter"), fill=BLAUHELL, size=28, anker="m"),
    # Spalte 1: Wachkoma im Altenheim
    pl("seit 2002", C1, 200, beim("koma", "zweitausendzwei"), fill=GELB, size=28, anker="m"),
    pl("nach einer Hirnblutung im Wachkoma", C1, 265, beim("koma", "Hirnblutung"), fill=WEISS, size=28, anker="m"),
    pl("in einem Altenheim", C1, 330, beim("koma", "Altenheim"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "building", C1, BODEN, 280, beim("koma", "Altenheim"), fuell=BLAUHELL),
    pl("künstlich ernährt", C1, 395, beim("koma", "künstlich"), fill=WEISS, size=28, anker="m"),
    pl("keine Besserung zu erwarten", C1, 460, beim("koma", "Besserung"), fill=ROTHELL, size=28, anker="m"),
    # Spalte 2: der früher geäußerte Wille
    pl("kurz vorher zur Tochter:", C2, 200, "wille", fill=WEISS, size=28, anker="m"),
    ficon("tabler", "message", C2, BODEN, 240, "wille", fuell=WEISS),
    pl("wenn sie sich nicht mehr äußern kann,", C2, 265, beim("wille", "Wenn"), fill=WEISS, size=28, anker="m"),
    pl("keine künstliche Ernährung", C2, 330, beim("wille", "keine"), fill=GELB, size=28, anker="m"),
    pl("nicht aufgeschrieben", C2, 410, beim("wille", "Aufgeschrieben"), fill=ROTHELL, size=28, anker="m"),
    # Spalte 3: Betreuer und Hausarzt
    pl("später:", C3, 200, "betreuer", fill=WEISS, size=28, anker="m"),
    pl("Tochter und Bruder werden Betreuer", C3, 265, beim("betreuer", "Betreuern"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "certificate", C3 - 120, BODEN, 200, beim("betreuer", "Betreuern"), fuell=GELB),
    pl("Hausarzt unterstützt sie", C3, 330, beim("betreuer", "Hausarzt"), fill=GRUENHELL, size=28, anker="m"),
    ficon("tabler", "stethoscope", C3 + 130, BODEN, 190, beim("betreuer", "Hausarzt"), fuell=WEISS),
])

# ===========================================================================================================================
# C2 2. Der echte Fall: Kompromiss, Anordnung, Rat des Anwalts, Krankenhaus (Rn. 7–8) – Handlung nur als Text-Pille
# ===========================================================================================================================
folie([("heim", f"{P2} · Die Ernährung wird eingestellt"), ("anord", f"{P2} · Die Anordnung"),
       ("rat", f"{P2} · Der Rat des Anwalts"), ("klinik", f"{P2} · Im Krankenhaus")], [
    boden("heim"),
    pl("Fall Putz · BGH, Urt. v. 25.6.2010 – 2 StR 454/09", 70, 30, "heim", fill=GELB, size=36),
    # Spalte 1: Kompromiss mit der Heimleitung
    pl("Kompromiss mit der Heimleitung", C1, 200, "heim", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "building", C1, BODEN, 230, "heim", fuell=BLAUHELL),
    pl("Tochter stellt die Ernährung ein", C1, 265, beim("heim", "stellte"), fill=GELB, size=30, anker="m"),
    # Spalte 2: Anordnung der Geschäftsleitung, Rat des Anwalts
    pl("am nächsten Tag:", C2, 200, "anord", fill=WEISS, size=30, anker="m"),
    pl("Geschäftsleitung: wieder aufnehmen", C2, 265, beim("anord", "Geschäftsleitung"), fill=ROTHELL, size=30, anker="m"),
    ficon("tabler", "file-alert", C2 - 110, BODEN, 150, beim("anord", "Geschäftsleitung"), fuell=WEISS),
    pl("Rat des Anwalts am Telefon:", C2, 345, "rat", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "phone", C2 + 110, BODEN, 140, "rat", fuell=WEISS),
    pl("den Schlauch der Sonde durchtrennen", C2, 410, beim("rat", "Schlauch"), fill=WEISS, size=30, anker="m"),
    pl("Die Tochter tut es,", C2, 490, beim("rat", "Tochter"), fill=GELB, size=30, anker="m"),
    pl("unterstützt von ihrem Bruder.", C2, 555, beim("rat", "unterstützt"), fill=GELB, size=30, anker="m"),
    # Spalte 3: Krankenhaus, natürlicher Tod
    pl("Das Personal bemerkt es.", C3, 200, "klinik", fill=WEISS, size=30, anker="m"),
    pl("im Krankenhaus wieder ernährt", C3, 265, beim("klinik", "Krankenhaus"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "building-hospital", C3, BODEN, 230, beim("klinik", "Krankenhaus"), fuell=WEISS),
    pl("gut 2 Wochen später:", C3, 345, beim("klinik", "gut"), fill=WEISS, size=30, anker="m"),
    pl("Sie stirbt eines natürlichen Todes.", C3, 410, beim("klinik", "starb"), fill=BLAUHELL, size=30, anker="m"),
])

# ===========================================================================================================================
# C3 Das Landgericht Fulda (Rn. 1, 9 f.) und die Frage
# ===========================================================================================================================
folie([("lg", f"{P2} · Landgericht Fulda"), ("frage", "Die Frage · Gerechtfertigt?")], rechts_frei([
    *tafel("lg", "Das Landgericht Fulda"),
    z("Anwalt: versuchter Totschlag", 110, 190, beim("lg", "Anwalt"), "Bold", 36),
    z("9 Monate Freiheitsstrafe auf Bewährung", 110, 245, beim("lg", "neun"), size=34),
    z("Tochter: Freispruch", 110, 335, "tochter", "Bold", 36),
    z("unvermeidbarer Erlaubnisirrtum nach dem Rechtsrat", 110, 390, beim("tochter", "unvermeidbaren"), size=34),
    zit("LG Fulda, Urt. v. 30.4.2009; nach BGH 2 StR 454/09 Rn. 1, 9 f.", 110, 455, beim("tochter", "Rechtsrat")),
    blk(110, 540, 1040, 100, PINK, "frage", [("War das Durchtrennen gerechtfertigt?", "ExtraBold", 36, INK)]),
    *requisit([("lg", ("fluent-emoji-flat", "classical-building", 280, None), "Landgericht Fulda", WEISS),
               ("frage", ("tabler", "scale", 220, WEISS), "gerechtfertigt?", PINK)], pu=700, py=220),
]))


# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
def sachverhalt_175(cue, absaetze, frage, quelle):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 85, cue, 52)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 12
    assert y + 120 <= 970, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    els.append(z(quelle, 210, y + 80, cue, size=26, farbe=TEXT, rechts=1760))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_175("sv", [
    "Eine Frau liegt seit 2002 nach einer Hirnblutung im Wachkoma in einem Altenheim und wird über eine Sonde künstlich "
    "ernährt; eine Besserung ist nicht zu erwarten. Kurz vorher hatte sie ihrer Tochter gesagt, wenn sie sich nicht mehr "
    "äußern könne, wolle sie keine künstliche Ernährung. Aufgeschrieben hatte sie das nicht. Später werden die Tochter und "
    "ihr Bruder zu Betreuern bestellt; der Hausarzt unterstützt sie.",
    "Nach einem Kompromiss mit der Heimleitung stellt die Tochter die Ernährung ein. Am nächsten Tag ordnet die "
    "Geschäftsleitung an, sie wieder aufzunehmen. Auf telefonischen Rat des Anwalts durchtrennt die Tochter, unterstützt "
    "von ihrem Bruder, den Schlauch der Sonde. Die Mutter wird im Krankenhaus wieder ernährt und stirbt gut 2 Wochen "
    "später eines natürlichen Todes.",
    "Das Landgericht Fulda verurteilt den Anwalt wegen versuchten Totschlags; die Tochter spricht es wegen eines "
    "unvermeidbaren Erlaubnisirrtums frei.",
], "War das Durchtrennen als Behandlungsabbruch gerechtfertigt?",
   "nach BGH, Urt. v. 25.6.2010 – 2 StR 454/09, BGHSt 55, 191 (Fall Putz), Rn. 1–10")

# ===========================================================================================================================
# E1 3. Der Kern: Rechtfertigung nur durch Einwilligung; alte Einteilung aufgegeben (Rn. 21 f., 26–28)
# ===========================================================================================================================
P3 = "3. Kern"
folie([("kern", f"{P3} › Rechtfertigung?"), ("einw", f"{P3} › Rechtfertigung durch Einwilligung"),
       ("alt", f"{P3} › alte Einteilung: aktives Tun"), ("aufg", f"{P3} › vom BGH aufgegeben")], rechts_frei([
    *tafel("kern", "3. Der Kern der Entscheidung"),
    z("Rechtfertigung nur durch den Willen", 110, 190, "einw", "Bold", 36),
    z("der Patientin: ihre Einwilligung", 110, 245, beim("einw", "Einwilligung"), "Bold", 36),
    zit("BGHSt 55, 191 Rn. 21", 110, 305, beim("einw", "Einwilligung")),
    *neinz("alte Einteilung: Durchtrennen ist aktives Tun,", 390, "alt", size=34, kreuz=beim("alt", "verboten")),
    z("also verboten", 185, 445, beim("alt", "verboten"), size=34),
    blk(110, 530, 1040, 100, GELB, "aufg", [("Daran hält der BGH nicht fest.", "ExtraBold", 36, INK)]),
    zit("BGHSt 55, 191 Rn. 22, 26–28", 110, 645, beim("aufg", "fest")),
    *stehend("WD", FX, [("kern", "ruhig"), ("alt", "ernst"), ("aufg", "ruhig")]),
    *requisit([("einw", None, "Einwilligung", GRUENHELL), ("alt", None, "aktives Tun?", ROTHELL),
               ("aufg", None, "hält nicht fest", GELB)], px=FX),
]))

# ===========================================================================================================================
# E2 Die Leitsätze 1 und 2 (wörtlich, BGHSt 55, 191) und der normative Oberbegriff (Rn. 30 f.)
# ===========================================================================================================================
LS1 = ["„Sterbehilfe durch Unterlassen, Begrenzen oder Beenden einer begonnenen",
       "medizinischen Behandlung (Behandlungsabbruch) ist gerechtfertigt, wenn",
       "dies dem tatsächlichen oder mutmaßlichen Patientenwillen entspricht",
       "(§ 1901a BGB) und dazu dient, einem ohne Behandlung zum Tode",
       "führenden Krankheitsprozess seinen Lauf zu lassen.“"]
ls1, ls1_y = wortlaut(100, 165, 1060, LS1, "BGHSt 55, 191, Leitsatz 1", "ls1", marken=[
    (0, "Unterlassen, Begrenzen oder Beenden", beim("ls1", "Unterlassen")),
    (1, "(Behandlungsabbruch)", beim("ls1", "Behandlungsabbruch")),
    (2, "tatsächlichen oder mutmaßlichen Patientenwillen", beim("ls1", "tatsächlichen")),
    (4, "seinen Lauf zu lassen", beim("lauf", "Lauf"))], size=29)
LS2 = ["„Ein Behandlungsabbruch kann sowohl durch Unterlassen als auch durch",
       "aktives Tun vorgenommen werden.“"]
ls2, ls2_y = wortlaut(100, ls1_y + 14, 1060, LS2, "BGHSt 55, 191, Leitsatz 2", "ls2", marken=[
    (1, "aktives Tun", beim("ls2", "aktives"))], size=29)
folie([("ls1", f"{P3} › Leitsatz 1: Behandlungsabbruch"), ("ls2", f"{P3} › Leitsatz 2: auch durch aktives Tun"),
       ("normativ", f"{P3} › normativ-wertender Oberbegriff")], rechts_frei([
    *tafel("ls1", "Die Leitsätze 1 und 2"),
    *ls1, *ls2,
    blk(100, ls2_y + 14, 1060, 110, GELB, "normativ", [("Einstellen oder Durchtrennen: entscheidet nicht", "ExtraBold", 30, INK),
                                                     ("normativ-wertender Oberbegriff (Rn. 30 f.)", "Bold", 30, INK)]),
    *stehend("TH", FX, [("ls1", "ruhig"), ("ls2", "denkt"), ("normativ", "ruhig")]),
    *requisit([("ls1", None, "Leitsatz 1", WEISS), ("ls2", None, "Leitsatz 2", WEISS),
               ("normativ", None, "entscheidet nicht", GELB)], px=FX),
]))

# ===========================================================================================================================
# E3 Voraussetzungen und Handelnde (Rn. 33 f., 39)
# ===========================================================================================================================
folie([("vor", f"{P3} › Voraussetzungen"), ("bezug", f"{P3} › Behandlungsbezug"), ("wer", f"{P3} › Wer handeln darf")],
      rechts_frei([
    *tafel("vor", "Voraussetzungen"),
    *okz("lebensbedrohliche Erkrankung", 190, beim("vor", "lebensbedrohlich"), "Bold", 34),
    *okz("Maßnahme medizinisch geeignet, das Leben", 260, beim("vor", "Maßnahme"), "Bold", 34),
    z("zu erhalten oder zu verlängern", 185, 312, beim("vor", "erhalten"), "Bold", 34),
    *okz("objektiv und subjektiv unmittelbar", 400, "bezug", "Bold", 34),
    z("auf die Behandlung bezogen", 185, 452, beim("bezug", "Behandlung"), "Bold", 34),
    *okz("Handelnde: Arzt, Betreuer, Bevollmächtigter", 540, "wer", "Bold", 34),
    z("und die Hilfspersonen, die sie hinzuziehen", 185, 592, beim("wer", "Hilfspersonen"), "Bold", 34),
    zit("BGHSt 55, 191 Rn. 33 f., 39", 110, 670, beim("wer", "hinzuziehen")),
    *stehend("WD", FX, [("vor", "ruhig"), ("wer", "ernst")]),
    *requisit([("vor", ("tabler", "stethoscope", 120, WEISS), "Voraussetzungen", WEISS),
               ("bezug", ("tabler", "stethoscope", 120, WEISS), "auf die Behandlung bezogen", GRUENHELL),
               ("wer", ("tabler", "certificate", 120, GELB), "wer handeln darf", WEISS)], px=FX, pu=330, py=140),
]))

# ===========================================================================================================================
# E4 Die Grenze: Leitsatz 3 (wörtlich), § 216 StGB, indirekte Sterbehilfe (Rn. 33 f., 37)
# ===========================================================================================================================
LS3 = ["„Gezielte Eingriffe in das Leben eines Menschen, die nicht in einem",
       "Zusammenhang mit dem Abbruch einer medizinischen Behandlung stehen,",
       "sind einer Rechtfertigung durch Einwilligung nicht zugänglich.“"]
ls3, ls3_y = wortlaut(100, 170, 1060, LS3, "BGHSt 55, 191, Leitsatz 3", "ls3", marken=[
    (0, "Gezielte Eingriffe", beim("ls3", "Gezielte")),
    (0, "nicht in einem", beim("ls3", "nicht")),
    (2, "nicht zugänglich", beim("ls3", "nicht", 2))], size=29)
folie([("ls3", f"{P3} › Leitsatz 3: die Grenze"), ("p216", f"{P3} › gezielte Eingriffe strafbar, § 216 StGB"),
       ("indir2", f"{P3} › indirekte Sterbehilfe erfasst")], rechts_frei([
    *tafel("ls3", "Die Grenze: Leitsatz 3"),
    *ls3,
    blk(100, ls3_y + 24, 1060, 130, ROTHELL, "p216", [("gezielte Eingriffe bleiben strafbar,", "ExtraBold", 32, INK),
                                                    ("auf Verlangen nach § 216 StGB", "ExtraBold", 32, INK)]),
    zit("BGHSt 55, 191 Rn. 33, 37; vgl. Folge 128", 110, ls3_y + 166, beim("p216", "Folge")),
    blk(100, ls3_y + 230, 1060, 90, GRUENHELL, "indir2", [("erfasst bleibt: indirekte Sterbehilfe", "ExtraBold", 32, INK)]),
    zit("BGHSt 55, 191 Rn. 34", 110, ls3_y + 332, beim("indir2", "indirekte")),
    *paar([("ls3", "ruhig"), ("p216", "ernst"), ("indir2", "ruhig")], [("ls3", "ernst"), ("indir2", "ruhig")]),
]))

# ===========================================================================================================================
# F1 4. Patientenwille: § 1827 BGB (früher § 1901a BGB) – Wortlautkarte Abs. 1 Satz 1
# ===========================================================================================================================
P4 = "4. Patientenwille"
W1827 = ["„(1) Hat ein einwilligungsfähiger Volljähriger für den Fall seiner",
         "Einwilligungsunfähigkeit schriftlich festgelegt, ob er in bestimmte, …",
         "Untersuchungen seines Gesundheitszustands, Heilbehandlungen oder",
         "ärztliche Eingriffe einwilligt oder sie untersagt (Patientenverfügung), …“"]
w1827, w1827_y = wortlaut(100, 300, 1060, W1827, "§ 1827 Abs. 1 Satz 1 BGB", "pv1", marken=[
    (1, "schriftlich festgelegt", beim("pv1", "schriftlich")),
    (3, "einwilligt oder sie untersagt", beim("pv1", "einwilligt")),
    (3, "(Patientenverfügung)", beim("pv1", "Patientenverfügung"))], size=29)
folie([("pv", f"{P4} › § 1827 BGB (früher § 1901a BGB)"), ("pv1", f"{P4} › Abs. 1: Patientenverfügung"),
       ("pv2", f"{P4} › Abs. 2: Behandlungswünsche, mutmaßlicher Wille")], rechts_frei([
    *tafel("pv", "4. Patientenwille: § 1827 BGB"),
    z("BGH 2010: § 1901a BGB a. F.", 110, 180, beim("pv", "stützte"), "Bold", 34),
    z("heute: § 1827 BGB", 110, 232, beim("pv", "heute"), "Bold", 34),
    *w1827,
    z("Abs. 2: sonst Behandlungswünsche oder", 110, w1827_y + 30, "pv2", "Bold", 34),
    z("mutmaßlicher Wille, etwa aus früheren Äußerungen", 110, w1827_y + 82, beim("pv2", "mutmaßliche"), "Bold", 34),
    *stehend("WD", FX, [("pv", "ruhig"), ("pv2", "denkt")]),
    *requisit([("pv", ("tabler", "book-2", 120, BLAU), "Betreuungsrecht", WEISS),
               (beim("pv", "heute"), ("tabler", "book-2", 120, BLAU), "§ 1827 BGB", WEISS),
               ("pv1", ("tabler", "file-text", 110, WEISS), "Patientenverfügung", GELB),
               ("pv2", ("tabler", "message", 120, WEISS), "mutmaßlicher Wille", WEISS)], px=FX, pu=330, py=140),
]))

# ===========================================================================================================================
# F2 § 1827 Abs. 3 BGB (Wortlaut), strenge Beweismaßstäbe, Wille im Fall festgestellt (Rn. 16 f., 24, 38)
# ===========================================================================================================================
W3 = ["„(3) Die Absätze 1 und 2 gelten unabhängig von Art und Stadium",
      "einer Erkrankung des Betreuten.“"]
w3, w3_y = wortlaut(100, 180, 1060, W3, "§ 1827 Abs. 3 BGB", "pv3", marken=[
    (0, "unabhängig von Art und Stadium", beim("pv3", "unabhängig"))], size=30)
folie([("pv3", f"{P4} › Abs. 3: unabhängig vom Stadium"), ("streng", f"{P4} › strenge Beweismaßstäbe"),
       ("hier", f"{P4} › Wille der Mutter festgestellt")], rechts_frei([
    *tafel("pv3", "§ 1827 Abs. 3 BGB und der Fall"),
    *w3,
    z("strenge Beweismaßstäbe für den Willen", 110, w3_y + 50, "streng", "Bold", 34),
    zit("BGHSt 55, 191 Rn. 38", 110, w3_y + 102, beim("streng", "Beweismaßstäbe")),
    *okz("hier: früher mündlich geäußerter Wille", w3_y + 180, "hier", "Bold", 34),
    z("der Mutter, zweifelsfrei festgestellt", 185, w3_y + 232, beim("hier", "zweifelsfrei"), "Bold", 34),
    zit("BGHSt 55, 191 Rn. 17", 185, w3_y + 290, beim("hier", "fest")),
    *stehend("TH", FX, [("pv3", "ruhig"), ("streng", "denkt"), ("hier", "ruhig")]),
    *requisit([("pv3", None, "unabhängig vom Stadium", WEISS), ("streng", None, "strenge Beweismaßstäbe", GELB),
               ("hier", None, "Wille festgestellt", GRUENHELL)], px=FX),
]))

# ===========================================================================================================================
# G 5. Ergebnis (Rn. 31, 41; Tenor)
# ===========================================================================================================================
P5 = "5. Ergebnis"
folie([("erg", f"{P5} › Wiederaufnahme verhindern"), ("erg2", f"{P5} › gerechtfertigter Behandlungsabbruch"),
       ("erg3", f"{P5} › Anwalt nicht rechtswidrig"), ("tenor", f"{P5} › Freispruch")], rechts_frei([
    *tafel("erg", "5. Ergebnis"),
    z("Durchtrennen: sollte verhindern, dass eine nicht mehr", 110, 190, beim("erg", "Durchtrennen"), "Bold", 33),
    z("gewollte Behandlung wieder aufgenommen wird", 110, 242, beim("erg", "gewollte"), "Bold", 33),
    *okz("gerechtfertigter Behandlungsabbruch", 330, "erg2", "Bold", 34),
    *okz("Anwalt als hinzugezogener Berater:", 410, "erg3", "Bold", 34),
    z("ebenso wenig rechtswidrig wie die Betreuer", 185, 462, beim("erg3", "ebenso"), "Bold", 34),
    zit("BGHSt 55, 191 Rn. 31, 41", 185, 520, beim("erg3", "selbst")),
    blk(110, 590, 1040, 140, GRUEN, "tenor", [("BGH: Urteil des Landgerichts aufgehoben,", "ExtraBold", 34, INK),
                                            ("der Anwalt wird freigesprochen", "ExtraBold", 34, INK)]),
    zit("Tenor, BGH, Urt. v. 25.6.2010 – 2 StR 454/09", 110, 745, beim("tenor", "frei")),
    *requisit([("erg", ("tabler", "scale", 230, WEISS), "Behandlungsabbruch?", WEISS),
               ("erg2", ("tabler", "scale", 230, WEISS), "gerechtfertigt", GRUENHELL),
               ("tenor", ("fluent-emoji-flat", "classical-building", 280, None), "Freispruch", GRUEN)], pu=700, py=220),
    pl("Bundesgerichtshof", PX, 760, "tenor", fill=WEISS, size=30, anker="m"),
]))

# ===========================================================================================================================
# H Zurück im Seminar
# ===========================================================================================================================
folie([("th2", "Zurück im Seminar · Die Frage"), ("wd2", "Zurück im Seminar · Die Antwort")], [
    *seminarraum("th2"),
    *whiteboard("th2", fall=("th2", "cut"), antwort=beim("wd2", "Entscheidend")),
    *fig("TH", THX, BODEN, FH, [("th2", "denkt_r")], bis="th2", erst="cut"),
    *redet("TH_redet_r", THX, BODEN, FH, "th2", "wd2"),
    *fig("TH", THX, BODEN, FH, [("wd2", "ruhig_r")], erst="cut"),
    hart(ns("Thilo", THX, BODEN, "th2", LILA)),
    *fig("WD", WDX, BODEN, FH, [("th2", "ruhig")], bis="wd2", erst="cut"),
    *redet("WD_redet", WDX, BODEN, FH, "wd2", "tipp"),
    hart(ns("Prof. Wedekind", WDX, BODEN, "th2", GRUEN)),
    blase("sprech", 660, 200, "th2", 1110, 270, inhalt=["Also kommt es nicht darauf an,", "ob man aktiv handelt?"],
          textsize=32, figur=("TH_redet_r", THX, BODEN, FH), bis="wd2"),
    blase("sprech", 700, 230, "wd2", 1160, 270, inhalt=["Nein. Entscheidend sind der", "Bezug zur Behandlung und", "der Wille der Patientin."],
          textsize=32, figur=("WD_redet", WDX, BODEN, FH)),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
LXX = 1600
folie([("tipp", "Klausurtipp · Tatbestand § 212 StGB"), ("tipp2", "Klausurtipp · Rechtfertigung: Behandlungsabbruch"),
       ("tipp3", "Klausurtipp · ohne Behandlungsbezug keine Rechtfertigung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Tatbestand: § 212 StGB,", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("hier versucht und durch aktives Tun", 200, 250, beim("tipp", "versucht"), size=34),
    z("Behandlungsabbruch erst in der Rechtswidrigkeit:", 200, 340, "tipp2", "Bold", 34),
    z("Rechtfertigung durch Einwilligung", 200, 390, beim("tipp2", "Rechtfertigung"), size=34),
    z("nach dem Patientenwillen", 200, 440, beim("tipp2", "Patientenwillen"), size=34),
    z("ohne Behandlungsbezug: keine Rechtfertigung", 200, 530, "tipp3", "Bold", 34),
    zit("BGHSt 55, 191 Leitsätze 1 und 3; Rn. 21 f.", 200, 590, beim("tipp3", "Rechtfertigung")),
    *redet("LX_warnt", LXX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", LXX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema (progressiv)
# ===========================================================================================================================
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("s1", f"{PS_} › 1. Tatbestand"), ("s2", f"{PS_} › 2. Rechtswidrigkeit"),
       ("s2a", f"{PS_} › 2. a) Erkrankung und Behandlung"), ("s2b", f"{PS_} › 2. b) Behandlungsbezug"),
       ("s2c", f"{PS_} › 2. c) Patientenwille"), ("s2d", f"{PS_} › 2. d) Handelnde"), ("s3", f"{PS_} › 3. Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Totschlag, § 212 StGB, beim Behandlungsabbruch", 110, 90, "sch", 44),
    z("1. Tatbestand", K1, 185, "s1", "Bold", 36, rechts=1820),
    z("a) Tötung eines anderen Menschen, durch Tun oder Unterlassen", K2, 243, beim("s1", "Tötung"), size=34, rechts=1820),
    z("b) Vorsatz", K2, 298, beim("s1", "Vorsatz"), size=34, rechts=1820),
    z("2. Rechtswidrigkeit: Rechtfertigung durch Behandlungsabbruch", K1, 375, "s2", "Bold", 36, rechts=1820),
    z("a) lebensbedrohliche Erkrankung und lebenserhaltende Behandlung", K2, 433, "s2a", size=34, rechts=1820),
    z("b) Unterlassen, Begrenzen oder Beenden dieser Behandlung,", K2, 488, "s2b", size=34, rechts=1820),
    z("mit unmittelbarem Behandlungsbezug", K2 + 32, 538, beim("s2b", "unmittelbarem"), size=34, rechts=1820),
    z("c) tatsächlicher oder mutmaßlicher Patientenwille, streng festgestellt", K2, 593, "s2c", size=34, rechts=1820),
    z("d) Handeln durch Arzt, Betreuer, Bevollmächtigten oder ihre Hilfspersonen", K2, 648, "s2d", size=34, rechts=1820),
    z("3. Schuld", K1, 725, "s3", "Bold", 36, rechts=1820),
    zit("Aufbau nach Klausurkonvention; Merkmale nach BGHSt 55, 191 Leitsätze 1–3, Rn. 33–39", K1, 800, "sch", rechts=1820),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nicht Tun oder Unterlassen entscheidet,", 0)],
                 [("sondern der ", 0), ("Bezug zur Behandlung", "a"), (".", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "Bezug")}),
    *markertext([[("Ein Behandlungsabbruch nach dem", 0)], [("Patientenwillen ist ", 0), ("gerechtfertigt", "b"), (",", 0)],
                 [("ein gezielter Eingriff ohne", 0)], [("Behandlungsbezug nicht.", 0)]], 750, 470, 40, "m2",
                {"b": beim("m2", "gerechtfertigt")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", "hilfe"),
    ns("Lexi", 1680, 960, "merke", GELB, d=0.2),
])

# ===========================================================================================================================
# L Hilfsangebot (ruhige Tafel, Nummern verifiziert auf telefonseelsorge.de, Abruf 04.10.2026)
# ===========================================================================================================================
folie([("hilfe", "Hilfsangebot")], [
    karte(160, 140, 1600, 760, "hilfe", fill=BLAUHELL),
    titel("Wenn dich das Thema belastet", 960, 200, "hilfe", 50, anker="m"),
    z("Die TelefonSeelsorge ist rund um die Uhr", 260, 320, beim("hilfe", "Die"), "Bold", 36, rechts=1700),
    z("und kostenlos für dich da.", 260, 375, beim("hilfe", "kostenlos"), "Bold", 36, rechts=1700),
    ficon("tabler", "phone-call", 1520, 470, 150, beim("hilfe", "Die"), fuell=GRUEN),
    z("0800 111 0 111", 260, 480, "nummern", "ExtraBold", 56, rechts=1700),
    z("0800 111 0 222", 260, 570, "nummern", "ExtraBold", 56, rechts=1700),
    z("telefonseelsorge.de", 260, 680, "nummern", size=32, farbe=TEXT, rechts=1700),
])
