"""Folge 266 · Polizeiliche Generalklausel: Meldeauflage für Hooligans erlaubt? – Serienstandard Open Peeps (Katzenkönig).
Fall: Samstag, 15 Uhr, Polizeiwache in Nordrhein-Westfalen. Herr Schütte muss sich an den Samstagen der nächsten drei
Auswärtsspiele seines Vereins um 15 Uhr melden (Anpfiff 15:30 Uhr, 200 km entfernt). Polizistin Feddersen nimmt die Meldung
auf, Wachleiter Rabe nennt den Anlass. Keine echten Vereine, keine Vereinsfarben, kein Gewaltbild, keine Klischees.
Szenen laut ../SZENENPLAN.md: A Polizeiwache (Fall), B Sachverhalt, C Ermächtigungsgrundlage (Sperrwirkung), D Länder im
Vergleich (§ 16a NPOG, § 20 SächsPVDG, § 15a BbgPolG, NRW ohne Norm), E Wortlautkarte § 8 Abs. 1 PolG NRW, F Grundrechte
(Wortlautkarte Art. 11 GG, Zitiergebot § 7 PolG NRW), G Wesentlichkeit (Zitatkarte BVerwG 6 C 39.06 Rn. 33), H Abgrenzung
§ 10 PassG (Wortlautkarten § 10 Abs. 1 S. 2, § 7 Abs. 1 Nr. 1 PassG), I Gegenfall Auslandsspiel, J Tatbestand,
K Verhältnismäßigkeit und Ergebnis, L Klausurtipp (Lexi), M Schema, N Merksatz (Lexi).
Ein Handlungsgeräusch (Tür, wenn Herr Schütte die Wache betritt; ../geraeusche_herkunft.json). Namensschild jeder Figur,
solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus
Folge 257 (gemeinsame Dateien unverändert); neu: boden(), wache(), tresen(). Zahlen auf Tafeln, Pillen und Blasen als
Ziffern. Wortlautkarten wörtlich nach recht.nrw.de und gesetze-im-internet.de (Abruf 08.10.2026); Zitatkarte wörtlich nach
bverwg.de."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_266/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_266/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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




# --- eigene Szenenbausteine: Polizeiwache (Wand, Boden, Tür, Tresen), Grenzkontrolle (Palettenflächen, Tuschekontur) ------
BODEN = (214, 206, 192, 255)
WAND = (236, 240, 248, 255)
F_O, F_U = 930, 1000                         # Boden (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def boden(cue):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=BODEN)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    for x in range(150, 1860, 300):
        dr.line((x * s, 6 * s, x * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def wache(cue):
    """Innenraum der Polizeiwache: Wand, Tür links, Tresen in der Mitte (programmatisch, Palettenflächen)."""
    return [hart(karte(30, 240, 1860, F_O - 240 + 4, cue, fill=WAND, rund=6, schatten=0, rand=5, anim="cut")),
            hart(karte(110, 470, 230, F_O - 470 + 4, cue, fill=HOLZ, rund=8, schatten=0, rand=5, anim="cut")),
            hart(karte(300, 690, 22, 22, cue, fill=GELB, rund=11, schatten=0, rand=4, anim="cut"))]


def tresen(cue, x0=850, w=480):
    return [hart(karte(x0, 690, w, F_O - 690 + 16, cue, fill=HOLZ, rund=6, schatten=0, rand=5, anim="cut")),
            hart(karte(x0 - 20, 668, w + 40, 30, cue, fill=(190, 135, 88, 255), rund=6, schatten=0, rand=5, anim="cut"))]


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SC": "Herr Schütte", "FE": "Polizistin Feddersen", "RA": "Wachleiter Rabe"}
NFARBE = {"SC": GELB, "FE": BLAU, "RA": GRUEN}


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


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


K_UHR = ("tabler", "clock-hour-3", 100, WEISS)
K_STADION = ("tabler", "building-stadium", 120, GRUEN)
K_BRIEF = ("tabler", "file-text", 90, WEISS)

# ===========================================================================================================================
# A Fall: Samstag, 15 Uhr, Polizeiwache
# ===========================================================================================================================
SCX, FEX, RAX = 560, 1090, 1640              # Schütte (blickt nach rechts), Feddersen hinter dem Tresen, Rabe (blicken nach links)
SC_ERST = fig("SC", SCX, FU, FH, [("schuette", "skeptisch_r"), ("auflage", "sorge_r")], bis="sc1", erst="pop")
szene(SC_ERST[0], "266tuer*", 0.8, 0.0)
folie([(NULL, "Fall · Samstag, 15 Uhr, auf der Polizeiwache"), ("schuette", "Fall · Herr Schütte mit dem Schreiben"),
       ("auflage", "Fall · Die Meldeauflage"), ("anstoss", "Fall · Anpfiff 200 km entfernt"),
       ("fe1", "Fall · „Ihre Meldung ist notiert“"), ("sc1", "Fall · „Darf die Polizei das?“"),
       ("rabe", "Fall · Wachleiter Rabe"), ("ra1", "Fall · Verurteilungen und Verabredung"),
       ("gespraech", "Fall · Gefährderansprache im Sommer"), ("frage", "Fall · Die Frage")], [
    hart(boden(NULL)),
    *wache(NULL),
    hart(ficon("tabler", "clock-hour-3", 1790, 215, 105, NULL, fuell=WEISS, anim="cut")),
    hart(pl("Samstag, 15 Uhr: eine Polizeiwache in NRW", 70, 30, NULL, fill=GELB, size=38, bis="frage")),
    *fig("FE", FEX, FU, FH, [(NULL, "ruhig"), ("schuette", "denkt")], bis="fe1", erst="cut"),
    *redet("FE_redet", FEX, FU, FH, "fe1", "sc1"),
    *fig("FE", FEX, FU, FH, [("sc1", "ruhig"), ("ra1", "ernst"), ("frage", "denkt")], erst="cut"),
    *tresen(NULL),
    hart(ns("Polizistin Feddersen", FEX, FU, NULL, BLAU)),
    pl("Herr Schütte kommt mit einem Schreiben", 70, 100, "schuette", fill=WEISS, size=32, bis="auflage"),
    *SC_ERST,
    *redet("SC_redet_r", SCX, FU, FH, "sc1", "rabe"),
    *fig("SC", SCX, FU, FH, [("rabe", "skeptisch_r"), ("ra1", "still_r"), ("gespraech", "muede_r"), ("frage", "skeptisch_r")], erst="cut"),
    ns("Herr Schütte", SCX, FU, "schuette", GELB, d=0.1),
    ficon("tabler", "file-text", 930, 670, 72, beim("schuette", "Schreiben"), fuell=WEISS),
    pl("Meldeauflage: an 3 Auswärtsspielen je um 15 Uhr melden", 70, 100, "auflage", fill=WEISS, size=32, bis="frage"),
    pl("Anpfiff um 15:30 Uhr – 200 km entfernt", 70, 170, "anstoss", fill=WEISS, size=32, bis="sc1"),
    ficon("tabler", "building-stadium", 1640, 600, 170, "anstoss", fuell=GRUEN, bis="rabe"),
    *fig("RA", RAX, FU, FH, [("rabe", "ruhig")], bis="ra1", erst="pop"),
    *redet("RA_redet", RAX, FU, FH, "ra1", "gespraech"),
    *fig("RA", RAX, FU, FH, [("gespraech", "ernst"), ("frage", "denkt")], erst="cut"),
    ns("Wachleiter Rabe", RAX, FU, "rabe", GRUEN, d=0.1),
    pl("Gefährderansprache im Sommer: ohne Wirkung", 70, 170, "gespraech", fill=HELLROT, size=32, bis="frage"),
    ficon("tabler", "message-circle", 760, 430, 90, "gespraech", fuell=WEISS, bis="frage"),
    blase("sprech", 660, 190, "fe1", 1090, 290, inhalt=["Guten Tag, Herr Schütte.", "Ihre Meldung ist notiert."],
          textsize=34, figur=("FE_redet", FEX, FU, FH), bis="sc1"),
    blase("sprech", 720, 236, "sc1", 720, 290, inhalt=["Ich will doch nur Fußball sehen.", "Darf die Polizei mich einfach", "hierher bestellen?"],
          textsize=32, figur=("SC_redet_r", SCX, FU, FH), bis="rabe"),
    blase("sprech", 900, 240, "ra1", 1280, 290, inhalt=["Sie wurden 2-mal wegen Körperverletzung", "bei Auswärtsspielen verurteilt. Und Ihre Gruppe",
          "hat sich für heute zu einer Schlägerei verabredet."], textsize=32, figur=("RA_redet", RAX, FU, FH), bis="gespraech"),
    pl("Darf die Polizei Herrn Schütte zur Meldung verpflichten?", 70, 30, "frage", fill=PINK, size=36),
    pl("Worauf stützt sie die Meldeauflage, wenn das Polizeigesetz sie nicht nennt?", 70, 100, "frage2", fill=PINK, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_266(cue, absaetze, frage):
    els = [titel("Sachverhalt", 210, 165, cue, 60)]
    y = 270
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    els.insert(0, karte(140, 130, 1640, int(y + 6 + 80 - 130), cue, fill=HELL))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_266("sv", [
    "Nordrhein-Westfalen: Herr Schütte wurde 2-mal wegen Körperverletzung bei Auswärtsspielen seines Fußballvereins "
    "verurteilt. Im Sommer warnte ihn die Polizei in einer Gefährderansprache. Seine Gruppe hat sich für die nächsten "
    "Auswärtsspiele zu Schlägereien mit gegnerischen Fans verabredet.",
    "Nach Anhörung verpflichtet ihn die Polizei: An den Samstagen der nächsten 3 Auswärtsspiele muss er sich jeweils um "
    "15 Uhr auf seiner Polizeiwache melden; Anpfiff ist um 15:30 Uhr, 200 km entfernt. Bei Verhinderung darf er sich nach "
    "Absprache bei einer anderen Dienststelle melden.",
], "Ist die Meldeauflage rechtmäßig? Worauf kann die Polizei sie stützen?")

# ===========================================================================================================================
# C Ermächtigungsgrundlage: Sperrwirkung
# ===========================================================================================================================
PE = "1. Ermächtigungsgrundlage"
folie([("egl", f"{PE}"), (beim("egl", "Sperrwirkung"), f"{PE} · Sperrwirkung"), ("v077", f"{PE} · Aufbau: Folge 077"),
       ("spez", f"{PE} · eigene Befugnis für Meldeauflagen?")], rechts_frei([
    *tafel("egl", "1. Ermächtigungsgrundlage", h=700),
    z("Reihenfolge:", 110, 180, "egl", "ExtraBold", 34),
    blk(110, 235, 1040, 72, BLAU, beim("egl", "Spezielle"), [("1. spezielle Befugnis, Standardmaßnahme", "ExtraBold", 32, INK)]),
    blk(110, 325, 1040, 72, GELB, beim("egl", "Generalklausel"), [("2. erst dann: die Generalklausel", "ExtraBold", 32, INK)]),
    z("Sperrwirkung: Die speziellere Norm geht vor.", 110, 425, beim("egl", "Sperrwirkung"), "Bold", 32),
    z("Den Aufbau zeigt Folge 077.", 110, 485, "v077", size=30),
    z("Eigene Befugnis für Meldeauflagen?", 110, 565, "spez", "ExtraBold", 36),
    z("Das hängt vom Land ab.", 110, 622, beim("spez", "hängt"), size=32),
    *requisit([("egl", ("tabler", "book", 100, WEISS), "Ermächtigungsgrundlage", WEISS),
               ("v077", ("tabler", "list-details", 100, WEISS), "Folge 077", WEISS),
               ("spez", ("tabler", "map-2", 110, GRUEN), "Landesrecht", WEISS)]),
    *stehend("FE", X1, [("egl", "ruhig"), ("spez", "denkt")]),
    *stehend("SC", X2, [("egl", "skeptisch"), ("spez", "ruhig")]),
]))

# ===========================================================================================================================
# D Länder im Vergleich: eigene Meldeauflage?
# ===========================================================================================================================
SP0, SP1, SP2, SP3 = 120, 470, 830, 1560
ZL = [("tni", "Niedersachsen", "§ 16a NPOG", ["Gefahr – oder Tatsachen: Straftat,", "zumindest ihrer Art nach konkretisiert"], "3 Monate"),
      ("tsn", "Sachsen", "§ 20 SächsPVDG", ["Tatsachen: ihrer Art nach", "konkretisierte Straftat"], "1 Monat"),
      ("tbb", "Brandenburg", "§ 15a BbgPolG", ["Tatsachen: Straftat gegen Leib oder Leben,", "§§ 125, 125a StGB, § 27 Abs. 1 VersG"], "1 Monat")]
els_t = [karte(60, 50, 1800, 940, "tni"), titel(glyphen("Eigene Meldeauflage? Länder im Vergleich"), 110, 85, "tni", 46),
         z("Land", SP0, 170, "tni", "ExtraBold", 32, rechts=1820), z("Norm", SP1, 170, "tni", "ExtraBold", 32, rechts=1820),
         z("Voraussetzung", SP2, 170, beim("tvor", "Tatsachen"), "ExtraBold", 32, rechts=1820),
         z("Befristung", SP3, 170, "tdauer", "ExtraBold", 32, rechts=1820),
         linienzug([(110, 222), (1810, 222)], "tni", breite=5)]
y = 248
for c, land, norm, vor, dauer in ZL:
    els_t += [z(land, SP0, y, c, "Bold", 32, rechts=1820), z(norm, SP1, y, c, size=32, rechts=1820),
              z(vor[0], SP2, y, beim("tvor", "Tatsachen"), size=30, rechts=1540),
              z(vor[1], SP2, y + 40, beim("tvor", "Tatsachen"), size=30, rechts=1540),
              z(dauer, SP3, y, beim("tdauer", "Sachsen") if c != "tni" else beim("tdauer", "Niedersachsen"), "Bold", 32, rechts=1820),
              z("verlängerbar", SP3, y + 40, beim("tdauer", "Niedersachsen"), size=28, farbe=TEXT, rechts=1820)]
    y += 100
els_t += [pl("Dort ist die Generalklausel insoweit gesperrt (Sperrwirkung).", SP0, y - 2, "tsperr", fill=HELLROT, size=30)]
y += 80
els_t += [linienzug([(110, y - 14), (1810, y - 14)], "tnrw", breite=3),
          z("Nordrhein-Westfalen", SP0, y, "tnrw", "Bold", 32, rechts=1820),
          z("keine eigene Norm", SP1, y, "tnrw", "ExtraBold", 32, rechts=1820),
          z("also: Generalklausel, § 8 Abs. 1 PolG NRW", SP2, y, beim("tnrw", "Verwaltungsgericht"), size=30, rechts=1820),
          zit("VG Düsseldorf, Beschl. v. 20.6.2024 – 18 L 1554/24, Rn. 15", SP2, y + 44, beim("tnrw", "festgestellt"), rechts=1820)]
y += 120
els_t += [blk(110, y, 1700, 76, GELB, "tdein", [("In deinem Land kann das anders sein.", "ExtraBold", 34, INK)]),
          zit("Wortlaut geprüft am 8.10.2026: voris.wolterskluwer-online.de, revosax.sachsen.de, bravors.brandenburg.de, recht.nrw.de",
              110, y + 100, "tdein", rechts=1820)]
assert y + 140 <= 990, y
folie([("tni", "Länder › Niedersachsen: § 16a NPOG"), ("tsn", "Länder › Sachsen: § 20 SächsPVDG"),
       ("tbb", "Länder › Brandenburg: § 15a BbgPolG"), ("tsperr", "Länder › Sperrwirkung der eigenen Norm"),
       ("tvor", "Länder › Voraussetzungen"), ("tdauer", "Länder › Befristung"),
       ("tnrw", "Länder › Nordrhein-Westfalen: keine eigene Norm"), ("tdein", "Länder › dein Landesgesetz")], els_t)

# ===========================================================================================================================
# E Generalklausel: Wortlautkarte § 8 Abs. 1 PolG NRW
# ===========================================================================================================================
W8 = ["„(1) Die Polizei kann die notwendigen Maßnahmen treffen, um eine",
      "im einzelnen Falle bestehende, konkrete Gefahr für die öffentliche",
      "Sicherheit oder Ordnung (Gefahr) abzuwehren, soweit nicht die",
      "§§ 9 bis 46 die Befugnisse der Polizei besonders regeln.“"]
w8, w8_y = wortlaut(80, 250, 1100, W8, "§ 8 Abs. 1 PolG NRW (Beispiel Nordrhein-Westfalen)", "wl8", marken=[
    (0, "notwendigen Maßnahmen", beim("wl8", "notwendigen")), (1, "konkrete Gefahr", beim("wl8", "konkrete")),
    (2, "soweit nicht die", "soweit"), (3, "§§ 9 bis 46", beim("soweit", "Paragrafen"))], size=32)
folie([("wl8", "1. Ermächtigungsgrundlage › Generalklausel, § 8 Abs. 1 PolG NRW"),
       ("soweit", "1. Ermächtigungsgrundlage › „soweit nicht …“: Subsidiarität")], rechts_frei([
    *tafel("wl8", "Also: die Generalklausel", h=640),
    z("Nordrhein-Westfalen:", 110, 180, "wl8", "Bold", 32),
    *w8,
    *requisit([("wl8", ("tabler", "book", 100, WEISS), "§ 8 Abs. 1 PolG NRW", GELB),
               ("soweit", ("tabler", "list-details", 100, WEISS), "„soweit nicht …“", WEISS)]),
    *stehend("FE", X1, [("wl8", "ernst"), ("soweit", "ruhig")]),
    *stehend("SC", X2, [("wl8", "skeptisch"), ("soweit", "sorge")]),
]))

# ===========================================================================================================================
# F Trägt die Generalklausel? Art. 2 Abs. 1, Art. 11 GG, Zitiergebot
# ===========================================================================================================================
W11 = ["„(1) Alle Deutschen genießen Freizügigkeit im ganzen Bundesgebiet.",
       "(2) Dieses Recht darf nur durch Gesetz oder auf Grund eines Gesetzes",
       "und nur für die Fälle eingeschränkt werden, in denen es …",
       "um strafbaren Handlungen vorzubeugen, erforderlich ist.“"]
w11, w11_y = wortlaut(80, 410, 1100, W11, "Art. 11 GG", "art11", marken=[
    (0, "im ganzen Bundesgebiet", beim("art11", "überall")),
    (3, "um strafbaren Handlungen vorzubeugen", beim("art11", "strafbaren"))], size=30)
PT = "1. Ermächtigungsgrundlage › Trägt die Generalklausel?"
folie([("trag", f"{PT}"), ("grund", f"{PT} › Art. 2 Abs. 1 GG"), (beim("grund", "Freizügigkeit"), f"{PT} › Art. 11 GG"),
       ("art11", f"{PT} › Art. 11 Abs. 2 GG"), ("zitier", f"{PT} › Zitiergebot, § 7 PolG NRW")], rechts_frei([
    *tafel("trag", "Trägt die Generalklausel den Eingriff?", h=740, size=44),
    z("Eingriff in:", 110, 175, "grund", "ExtraBold", 34),
    pl("Art. 2 Abs. 1 GG", 110, 226, beim("grund", "allgemeine"), fill=BLAU, size=30),
    z("allgemeine Handlungsfreiheit", 450, 230, beim("grund", "allgemeine"), size=32),
    pl("Art. 11 Abs. 1 GG", 110, 292, beim("grund", "Freizügigkeit"), fill=GELB, size=30),
    z("Freizügigkeit – regelmäßig mitbetroffen", 450, 296, beim("grund", "Freizügigkeit"), size=32),
    zit("BVerwG, Urt. v. 25.7.2007 – 6 C 39.06, Rn. 36, 45", 110, 360, beim("grund", "elf")),
    *w11,
    *okz("§ 7 PolG NRW: Zitiergebot nennt die Freizügigkeit", w11_y + 24, "zitier", "Bold", 30, x=160),
    *requisit([("trag", ("tabler", "scale", 110, WEISS), "Eingriff?", WEISS),
               ("grund", ("tabler", "user-check", 100, BLAU), "Art. 2 Abs. 1 GG", BLAU),
               (beim("grund", "Freizügigkeit"), ("tabler", "map-pin", 100, GELB), "Art. 11 GG", GELB),
               ("art11", ("tabler", "map-pin", 100, GELB), "Straftaten vorbeugen", WEISS),
               ("zitier", ("tabler", "book", 100, WEISS), "§ 7 PolG NRW", WEISS)]),
    *stehend("SC", X1, [("trag", "skeptisch"), ("grund", "sorge"), ("zitier", "ruhig")]),
    *stehend("RA", X2, [("trag", "ruhig"), ("art11", "ernst")]),
]))

# ===========================================================================================================================
# G Braucht es eine eigene Befugnis? BVerwG 6 C 39.06 (Zitatkarte Rn. 33), Grenze Vorfeld (Rn. 34)
# ===========================================================================================================================
WB = ["„Polizeiliche Meldeauflagen der hier umstrittenen Art weisen",
      "demgegenüber keine Besonderheiten auf, die die Schaffung einer",
      "speziellen Ermächtigungsgrundlage geböten.“"]
wb, wb_y = wortlaut(80, 300, 1100, WB, "BVerwG, Urt. v. 25.7.2007 – 6 C 39.06, Rn. 33", "bvg2",
                    marken=[(1, "keine Besonderheiten", beim("bvg2", "hinreichend"))], size=30)
PW = "1. Ermächtigungsgrundlage › Wesentlichkeit"
folie([("wes", f"{PW} › Kritik"), ("bvg", f"{PW} › BVerwG: Generalklausel genügt"),
       ("bvg2", f"{PW} › hinreichend bestimmt"), ("bvg3", f"{PW} › keine Freiheitsentziehung"),
       ("vorfeld", f"{PW} › Grenze: Vorfeld")], rechts_frei([
    *tafel("wes", "Braucht es eine eigene Befugnis?", h=860),
    z("Kritik: Was häufig eingesetzt wird, braucht eine eigene Befugnis.", 160, 180, "wes", size=30),
    nein(115, 200, "bvg", gr=20),
    z("BVerwG: Die Generalklausel genügt.", 110, 235, "bvg", "ExtraBold", 34),
    *wb,
    *okz("durch jahrzehntelange Rechtsprechung hinreichend bestimmt", wb_y + 22, beim("bvg2", "jahrzehntelange"), size=30, x=160),
    *okz("nicht auf untypische Fälle beschränkt", wb_y + 72, beim("bvg2", "untypische"), size=30, x=160),
    *okz("an Intensität keine Freiheitsentziehung", wb_y + 122, "bvg3", size=30, x=160),
    blk(110, wb_y + 190, 1040, 112, HELLROT, "vorfeld", [("Grenze: Eingriffe im Vorfeld einer Gefahr brauchen", "ExtraBold", 30, INK),
                                                    ("eine spezielle Grundlage – hier: konkrete Gefahr nötig", "ExtraBold", 30, INK)]),
    zit("BVerwG, a. a. O., Rn. 34, 36", 110, wb_y + 312, beim("vorfeld", "konkrete")),
    *requisit([("wes", ("tabler", "message-2", 100, WEISS), "Kritik", WEISS),
               ("bvg", ("tabler", "building-bank", 110, BLAU), "BVerwG", WEISS),
               ("bvg3", ("tabler", "scale", 110, WEISS), "Intensität", WEISS),
               ("vorfeld", ("tabler", "alert-triangle", 100, HELLROT), "Grenze: Vorfeld", HELLROT)]),
    *stehend("RA", X1, [("wes", "denkt"), ("bvg", "fest"), ("vorfeld", "ernst")]),
    *stehend("SC", X2, [("wes", "froh"), ("bvg", "still"), ("vorfeld", "skeptisch")]),
]))
assert wb_y + 312 + 40 <= 920, wb_y

# ===========================================================================================================================
# H Abgrenzung: § 10 PassG (Wortlautkarten § 10 Abs. 1 Satz 2, § 7 Abs. 1 Nr. 1 PassG)
# ===========================================================================================================================
W10 = ["„… Sie können einem Deutschen die Ausreise in das Ausland",
       "untersagen, wenn Tatsachen die Annahme rechtfertigen, dass bei",
       "ihm die Voraussetzungen nach § 7 Absatz 1 vorliegen … “"]
w10, w10_y = wortlaut(80, 165, 1100, W10, "§ 10 Abs. 1 Satz 2 PassG", "wl10", marken=[
    (0, "Ausreise in das Ausland", beim("wl10", "Ausreise")), (1, "Tatsachen die Annahme rechtfertigen", beim("wl10", "Tatsachen")),
    (2, "§ 7 Absatz 1", beim("wl10", "Passversagung"))], size=30)
W7 = ["„1. die innere oder äußere Sicherheit oder sonstige erhebliche",
      "Belange der Bundesrepublik Deutschland gefährdet; …“"]
w7, w7_y = wortlaut(80, w10_y + 14, 1100, W7, "§ 7 Abs. 1 Nr. 1 PassG (Passversagung)", "p7", marken=[
    (0, "sonstige erhebliche", beim("p7", "erheblicher")), (1, "Belange", beim("p7", "Belange"))], size=30)
PP = "Abgrenzung › § 10 PassG"
folie([("pass", f"{PP}"), ("wl10", f"{PP} › Ausreiseuntersagung"), ("p7", f"{PP} › § 7 Abs. 1 Nr. 1: erhebliche Belange"),
       ("ansehen", f"{PP} › internationales Ansehen"), ("ausreise", f"{PP} › Ausreise: Art. 2 Abs. 1 GG"),
       ("neben", f"{PP} › nebeneinander anwendbar"), ("zweck", f"{PP} › Zweck entscheidet")], rechts_frei([
    karte(60, 60, 1140, 900, "pass"), titel(glyphen("Abgrenzung: § 10 PassG"), 110, 85, "pass", 44),
    *w10, *w7,
    z("Ansehen Deutschlands bei Gewalt von Fans im Ausland", 110, w7_y + 16, "ansehen", size=30),
    zit("BVerwG 6 C 39.06, Rn. 28; VG Köln, Urt. v. 12.2.2020 – 10 K 12258/17, Rn. 35", 110, w7_y + 54, beim("ansehen", "Ausland")),
    z("Ausreise: geschützt durch Art. 2 Abs. 1 GG", 110, w7_y + 96, "ausreise", size=30),
    zit("VG Köln, a. a. O., Rn. 27", 790, w7_y + 100, beim("ausreise", "eins"), rechts=1170),
    *okz("verschiedene Ziele – nebeneinander anwendbar", w7_y + 146, "neben", "Bold", 30, x=160),
    zit("BVerwG, a. a. O., Rn. 29", 870, w7_y + 151, beim("neben", "nebeneinander"), rechts=1170),
    blk(110, w7_y + 200, 1040, 112, GELB, "zweck", [("Nur Ausreise verhindern, um das Ansehen zu", "ExtraBold", 30, INK),
                                                ("schützen? Dann haben die Passvorschriften Vorrang.", "ExtraBold", 30, INK)]),
    zit("VG Gelsenkirchen, Beschl. v. 3.5.2023 – 17 L 615/23, Rn. 5, 7", 110, w7_y + 322, beim("zweck", "Vorrang")),
    *requisit([("pass", ("tabler", "id", 110, WEISS), "Passgesetz", WEISS),
               ("wl10", ("tabler", "plane-departure", 120, BLAU), "Ausreise untersagen", WEISS),
               ("ansehen", ("tabler", "world", 100, BLAU), "Ansehen", WEISS),
               ("neben", ("tabler", "arrows-left-right", 100, WEISS), "nebeneinander", WEISS),
               ("zweck", ("tabler", "shield", 100, GRUEN), "Zweck: Straftaten verhindern", GRUEN)]),
    *stehend("FE", X1, [("pass", "ruhig"), ("zweck", "ernst")]),
    *stehend("RA", X2, [("pass", "denkt"), ("neben", "ruhig")]),
]))
assert w7_y + 322 + 34 <= 960, w7_y

# ===========================================================================================================================
# I Gegenfall: Auswärtsspiel im Ausland (Grenzkontrolle)
# ===========================================================================================================================
GSX = 1380
folie([("ausl", "Gegenfall · Auswärtsspiel im Ausland"), ("ausl2", "Gegenfall · Meldeauflage daneben möglich"),
       ("inl", "Gegenfall · hier: Spiele im Inland")], [
    hart(boden("ausl")),
    hart(ficon("tabler", "plane-departure", 430, 640, 330, "ausl", fuell=BLAU, anim="cut")),
    hart(ficon("tabler", "barrier-block", 900, FU, 230, "ausl", fuell=HELLROT, anim="cut")),
    pl("Gegenfall: Der Verein spielt im Ausland", 70, 30, "ausl", fill=GELB, size=36),
    pl("Bundespolizei: Ausreise untersagt (§ 10 PassG)", 70, 100, beim("ausl", "Ausreise"), fill=WEISS, size=32),
    ficon("tabler", "hand-stop", 900, 640, 110, beim("ausl", "Ausreise"), fuell=WEISS, bis="inl"),
    pl("daneben möglich: die Meldeauflage", 70, 170, "ausl2", fill=WEISS, size=32),
    ficon("tabler", "file-text", 1120, 560, 90, "ausl2", fuell=WEISS),
    *fig("SC", GSX, FU, FH, [("ausl", "sorge"), ("ausl2", "skeptisch"), ("inl", "ruhig")], erst="pop"),
    ns("Herr Schütte", GSX, FU, "ausl", GELB, d=0.1),
    nein(440, 500, "inl", gr=44),
    pl("Hier: Spiele im Inland – das Passgesetz greift nicht", 70, 240, "inl", fill=HELLROT, size=32),
    ficon("tabler", "building-stadium", 1720, 640, 190, "inl", fuell=GRUEN),
])

# ===========================================================================================================================
# J 2. Tatbestand: konkrete Gefahr, Verhaltensstörer
# ===========================================================================================================================
PG = "2. Tatbestand: konkrete Gefahr"
folie([("tb", f"{PG}"), ("prog", f"{PG} › drohende Körperverletzungen"), ("tats", f"{PG} › Prognose auf Tatsachen"),
       ("indiz", f"{PG} › Fanszene und frühere Verfahren"), ("stoer", "2. Tatbestand › Verhaltensstörer"),
       ("gefja", f"{PG} (+)")], rechts_frei([
    *tafel("tb", "2. Tatbestand: konkrete Gefahr", h=860),
    z("Definition: Folge 257", 110, 175, beim("tb", "Definition"), "Bold", 32),
    *okz("drohen: Körperverletzungen bei der Schlägerei", 240, beim("prog", "drohen"), size=31, x=160),
    zit("Schutzgüter der öffentlichen Sicherheit: Folge 213", 160, 288, beim("prog", "Schutzgütern")),
    z("Prognose auf Tatsachen:", 110, 345, "tats", "ExtraBold", 32),
    *okz("2 einschlägige Verurteilungen", 400, beim("tats", "zwei"), size=31, x=160),
    *okz("Verabredung zur Schlägerei vor diesem Spiel", 450, beim("tats", "Verabredung"), size=31, x=160),
    z("Fanszene: kann mitzählen – frühere Verfahren", 110, 520, "indiz", size=30),
    z("aktuell und einzeln auswerten", 110, 560, beim("indiz", "aktuell"), "Bold", 30),
    zit("VG Minden, Urt. v. 14.5.2018 – 11 K 730/17, Rn. 32, 34", 110, 604, beim("indiz", "auswerten")),
    *okz("Herr Schütte: Verhaltensstörer", 660, "stoer", "Bold", 31, x=160),
    zit("vgl. § 4 Abs. 1 PolG NRW", 160, 706, beim("stoer", "Verhaltensstörer")),
    blk(110, 760, 1040, 76, GRUEN, "gefja", [("konkrete Gefahr (+)", "ExtraBold", 34, INK)]),
    *requisit([("tb", ("tabler", "alert-triangle", 100, WEISS), "konkrete Gefahr?", WEISS),
               ("prog", ("tabler", "first-aid-kit", 100, HELLROT), "Körperverletzungen", HELLROT),
               ("tats", ("tabler", "list-check", 100, WEISS), "Tatsachen", WEISS),
               ("indiz", ("tabler", "users-group", 110, WEISS), "Fanszene", WEISS),
               ("stoer", ("tabler", "user-exclamation", 100, WEISS), "Verhaltensstörer", WEISS),
               ("gefja", ("tabler", "shield", 100, GRUEN), "konkrete Gefahr (+)", GRUEN)]),
    *stehend("RA", X1, [("tb", "ruhig"), ("tats", "ernst"), ("gefja", "fest")]),
    *stehend("SC", X2, [("tb", "skeptisch"), ("tats", "still"), ("indiz", "sorge"), ("gefja", "still")]),
]))

# ===========================================================================================================================
# K 3. Ermessen und Verhältnismäßigkeit, Ergebnis
# ===========================================================================================================================
PV = "3. Verhältnismäßigkeit"
folie([("vh", "3. Ermessen und Verhältnismäßigkeit"), ("geeig", f"{PV} › geeignet"), ("mild", f"{PV} › erforderlich: Gefährderansprache?"),
       ("angem", f"{PV} › angemessen"), ("ort", f"{PV} › Meldung bei Verhinderung"), ("erg", "Ergebnis · Meldeauflage rechtmäßig")],
      rechts_frei([
    *tafel("vh", "3. Ermessen und Verhältnismäßigkeit", h=880, size=44),
    z("Ermessen, begrenzt durch die Verhältnismäßigkeit", 110, 170, "vh", "Bold", 32),
    zit("§§ 2, 3 PolG NRW", 110, 214, beim("vh", "Verhältnismäßigkeit")),
    *okz("geeignet: 15 Uhr auf der Wache – nicht im Stadion", 262, "geeig", "Bold", 31, x=160),
    *okz("erforderlich: milder wäre eine Gefährderansprache", 330, "mild", "Bold", 31, x=160),
    z("je nach Inhalt nicht einmal ein Grundrechtseingriff", 160, 376, beim("mild", "Inhalt"), size=29),
    zit("OVG NRW, Beschl. v. 22.8.2016 – 5 A 2532/14, Rn. 26", 160, 414, beim("mild", "Grundrechtseingriff")),
    z("aber: im Sommer ohne Wirkung", 160, 452, beim("mild", "Sommer"), "Bold", 30),
    *okz("angemessen: Leib und Gesundheit vieler Menschen", 520, "angem", "Bold", 31, x=160),
    z("nur an 3 Spieltagen", 160, 566, beim("angem", "drei"), size=30),
    zit("vgl. BVerwG 6 C 39.06, Rn. 43", 160, 606, beim("angem", "Spieltagen")),
    *okz("bei Verhinderung: Meldung nach Absprache woanders", 660, "ort", "Bold", 31, x=160),
    zit("vgl. BVerwG, a. a. O., Rn. 45; VG Minden 11 K 730/17, Rn. 42", 160, 706, beim("ort", "melden")),
    blk(110, 770, 1040, 80, GRUEN, "erg", [("Ergebnis: Die Meldeauflage ist rechtmäßig.", "ExtraBold", 34, INK)]),
    *requisit([("vh", ("tabler", "scale", 110, WEISS), "Verhältnismäßigkeit", WEISS),
               ("geeig", K_UHR, "15 Uhr: Wache", WEISS),
               ("mild", ("tabler", "message-circle", 100, WEISS), "Gefährderansprache", WEISS),
               ("angem", ("tabler", "heart", 100, ROT), "Leib und Gesundheit", HELLROT),
               ("ort", ("tabler", "map-pin", 100, GELB), "andere Dienststelle", WEISS),
               ("erg", ("tabler", "shield", 100, GRUEN), "rechtmäßig", GRUEN)]),
    *stehend("FE", X1, [("vh", "ruhig"), ("mild", "denkt"), ("erg", "froh")]),
    *stehend("SC", X2, [("vh", "skeptisch"), ("geeig", "muede"), ("ort", "ruhig"), ("erg", "still")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst das Landesgesetz"), ("tipp1", "Klausurtipp · Generalklausel begründen"),
       ("tipp2", "Klausurtipp · den Zweck benennen")], [
    *tafel("tipp", "Klausurtipp: Meldeauflage", fill=HELL, h=600, size=46),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Erst prüfen: eigene Meldeauflage", 200, 200, "tipp", "Bold", 34),
    z("im Landesgesetz?", 200, 248, beim("tipp", "Landesgesetz"), size=32),
    z("2. Nur wenn nicht: Generalklausel –", 200, 333, "tipp1", "Bold", 34),
    z("kurz begründen, warum sie trägt", 200, 381, beim("tipp1", "begründest"), size=32),
    z("3. Zweck benennen: Straftaten verhindern,", 200, 466, "tipp2", "Bold", 34),
    z("nicht bloß die Ausreise", 200, 514, beim("tipp2", "nicht"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Schema
# ===========================================================================================================================
REIHEN = [("s1", "1. Ermächtigungsgrundlage", "eigene Meldeauflage im Landesrecht? Sonst die Generalklausel"),
          ("s2", "2. Abgrenzung zum Passgesetz", "nach dem Zweck"),
          ("s3", "3. Formell", "Zuständigkeit und Anhörung"),
          ("s4", "4. Tatbestand", "konkrete Gefahr, auf Tatsachen gestützt; richtiger Adressat"),
          ("s5", "5. Ermessen und Verhältnismäßigkeit", "Gefährderansprache als milderes Mittel")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Meldeauflage"), 110, 85, "sch", 50),
           zit("z. B. § 8 Abs. 1 PolG NRW; eigene Normen: § 16a NPOG, § 20 SächsPVDG, § 15a BbgPolG", 110, 168, beim("sch", "Schema"), rechts=1820)]
y = 225
for c, kopf, unter in REIHEN:
    els_sch.append(z(kopf, 130, y, c, "ExtraBold", 38, rechts=1820))
    els_sch.append(z(unter, 180, y + 50, c, size=32, rechts=1820))
    y += 145
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › 1. Ermächtigungsgrundlage"), ("s2", "Schema › 2. Abgrenzung zum Passgesetz"),
       ("s3", "Schema › 3. formell"), ("s4", "Schema › 4. Tatbestand"), ("s5", "Schema › 5. Ermessen und Verhältnismäßigkeit")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst die ", 0), ("Spezialbefugnis", "a"), (",", 0)],
                 [("dann die ", 0), ("Generalklausel", "b"), (".", 0)]], 750, 300, 48, "merke",
                {"a": beim("merke", "Spezialbefugnis"), "b": beim("merke", "Generalklausel")}),
    *markertext([[("Sie trägt eine Meldeauflage,", 0)],
                 [("wenn ", 0), ("konkret", "c"), (" Straftaten drohen", 0)],
                 [("und die Auflage ", 0), ("verhältnismäßig", "d"), (" bleibt.", 0)]], 750, 520, 46, "m2",
                {"c": beim("m2", "konkret"), "d": beim("m2", "verhältnismäßig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
