"""Folge 165 · Analogieverbot Strafrecht: Art. 103 II GG einfach erklärt – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Wieland bindet am öffentlichen Steg das Tretboot von Hartwin los, fährt eine Stunde über den See und bringt es
unbeschädigt zurück (ruhig, gewaltfrei). Tafeln: Wortlautkarten § 242 Abs. 1, § 248b Abs. 1/4, Art. 103 Abs. 2 GG, § 1 StGB,
§ 2 Abs. 1 StGB, § 240 Abs. 1 (Auszug), § 3 OWiG; Zitatkarten BVerfGE 126, 170 Rn. 73 und Rn. 80; vier Gewährleistungen
mit je eigener Farbe und gleicher Tafelstruktur (lex scripta Blau, lex certa Gelb, lex stricta Lila, lex praevia Grün).
Szenen laut ../SZENENPLAN.md, Belege ../RECHTSSTAND.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 162 (gemeinsame Dateien
unverändert); neu: see, steg, tretboot, boot_mit, gewaehr_tafel. Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Lateinische Begriffe sind in cues.json in der gesprochenen Form (zerta, präwia, pöna) – beim()-Anker nie darauf setzen."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_165/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_165/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


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


def neinz2(text, y, cue, kreuz, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Kreuz erst zur gesprochenen Verneinung (kreuz = Cue des Wortes „nicht“)."""
    return [nein(x - 45, y + 20, kreuz, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


GELBHELL = (255, 245, 210, 255)
LILAMITTEL = (236, 230, 255, 255)
BLAUMITTEL = (214, 228, 252, 255)
WASSER = (190, 220, 245, 255)
WELLE = (120, 165, 215, 255)
UFER = (214, 196, 150, 255)

# Vier Gewährleistungen: eigene Farbe je Ausprägung (Tafelfläche hell, Pille und Ergebnisblock kräftig)
GEW = {1: (BLAU, BLAUMITTEL, "lex scripta"), 2: (GELB, GELBHELL, "lex certa"), 3: (LILA, LILAMITTEL, "lex stricta"),
       4: (GRUEN, HELLGRUEN, "lex praevia")}

BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"WI": "Wieland", "HA": "Hartwin"}
NFARBE = {"WI": TUERKIS, "HA": ORANGE}


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


def paar(af, bf):
    """Tafelszene: Wieland und Hartwin rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend("WI", X1, af), *stehend("HA", X2, bf)]


# --- See, Steg und Tretboot aus Grundformen (Palettenflächen, Tuschekontur) ------------------------------------------------
SEE_X0, SEE_X1, SEE_O, SEE_U = 40, 1250, 835, 1000      # Wasserfläche (unten frei für den Prüfpfad)
STEG_X0, STEG_X1, STEG_O = 880, 1262, 815               # Steg: Deck von x0 bis zum Ufer, Oberkante
POLLER_X = 905


def see(cue):
    """Wasserfläche mit Wellenlinien und Uferböschung rechts."""
    w, h = SEE_X1 - SEE_X0, SEE_U - SEE_O
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 20 * s, fill=WASSER, outline=INK, width=5 * s)
    for r, y in enumerate((40, 85, 130)):
        for x in range(60 + (r % 2) * 90, w - 80, 180):
            pts = [(o + (x + k * 10) * s, o + (y + (6 if k % 2 else -6)) * s) for k in range(7)]
            dr.line(pts, fill=WELLE, width=4 * s, joint="curve")
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, SEE_X0 - 6, SEE_O - 6, cue, "cut", 0.0, None, name="see"))


def ufer(cue):
    """Ufer rechts: Böschung und Bodenlinie, auf der Hartwin steht."""
    w, h = 1880 - 1230, 1000 - BODEN
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.polygon([(o, o + h * s), (o + 40 * s, o), (o + w * s, o), (o + w * s, o + h * s)], fill=UFER)
    dr.line([(o, o + h * s), (o + 40 * s, o), (o + w * s, o)], fill=INK, width=6 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, 1230 - 6, BODEN - 6, cue, "cut", 0.0, None, name="ufer"))


def steg(cue):
    """Holzsteg vom Ufer in den See: Deck mit Planken, zwei Pfähle, Poller zum Festbinden."""
    w, h = STEG_X1 - STEG_X0 + 20, 1000 - STEG_O + 30
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    for px in (40, 200):
        dr.rectangle((o + px * s, o + 22 * s, o + (px + 26) * s, o + (h - 70) * s), fill=(150, 105, 70, 255), outline=INK,
                     width=4 * s)
    dr.rectangle((o, o, o + (w - 20) * s, o + 24 * s), fill=HOLZ, outline=INK, width=5 * s)
    for px in range(60, w - 20, 60):
        dr.line([(o + px * s, o + 4 * s), (o + px * s, o + 20 * s)], fill=INK, width=3 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, STEG_X0 - 6, STEG_O - 6, cue, "cut", 0.0, None, name="steg"))


def poller(cue):
    w, h = 26, 34
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 6 * s, fill=(150, 105, 70, 255), outline=INK, width=4 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, POLLER_X - 13 - 6, STEG_O - h - 6, cue, "cut", 0.0, None, name="poller"))


BOOT_W, BOOT_H = 330, 120                    # Rumpf
BOOT_X = 545                                 # festgemacht: Rumpf von BOOT_X bis BOOT_X + BOOT_W
BOOT_FAHRT = 140                             # draußen auf dem See
BOOT_O = 790                                 # Oberkante Rumpf


def _rumpf(spiegeln):
    w, h = BOOT_W, BOOT_H
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    pts = [(o, o + 10 * s), (o + w * s, o + 10 * s), (o + (w - 40) * s, o + (h - 10) * s), (o + 40 * s, o + (h - 10) * s)]
    dr.polygon(pts, fill=GELB)
    dr.line(pts + [pts[0]], fill=INK, width=5 * s)
    dr.rectangle((o + 20 * s, o + 34 * s, o + (w - 20) * s, o + 50 * s), fill=ROT)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if spiegeln else im


def _aufbau(spiegeln):
    """Sitzlehne und Radkasten (hinter der Figur)."""
    w, h = BOOT_W, 150
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.pieslice((o + (w - 150) * s, o + 40 * s, o + (w - 10) * s, o + 180 * s), 180, 360, fill=BLAU, outline=INK, width=5 * s)
    for a in range(200, 360, 40):
        import math as _m
        cx_, cy_ = o + (w - 80) * s, o + 110 * s
        dr.line([(cx_, cy_), (cx_ + 60 * s * _m.cos(_m.radians(a)), cy_ + 60 * s * _m.sin(_m.radians(a)))], fill=INK,
                width=3 * s)
    dr.rounded_rectangle((o + 96 * s, o + 92 * s, o + 196 * s, o + 150 * s), 12 * s, fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if spiegeln else im


def tretboot(x, cue, bis=None, spiegeln=False, weg=None, mit=None, anim="cut", oben=BOOT_O):
    """Tretboot (Rumpf Gelb mit roter Linie, Radkasten Blau, Sitzlehne) bei Rumpf-x = x; mit = Figur im Boot
    (Name der Ansicht), weg = (start, ende, dx) Bewegung über den See. Reihenfolge: Aufbau, Figur, Rumpf."""
    els = []
    a = El(_aufbau(spiegeln), x - 6, oben - 150 + 20 - 6, cue, anim, 0.0, bis, name="boot_aufbau")
    els.append(a)
    if mit:
        els.append(peep_voll(mit, x + BOOT_W / 2 - 10, oben + 100, 330, cue, anim=anim, bis=bis))
    els.append(El(_rumpf(spiegeln), x - 6, oben - 6, cue, anim, 0.0, bis, name="boot_rumpf"))
    if weg:
        for e in els:
            bewegt(e, weg[0], weg[1], weg[2])
    return els


def seil(cue, bis=None, lose=False):
    """Seil vom Bug zum Poller (festgebunden) oder lose im Wasser hängend."""
    bx, by = BOOT_X + BOOT_W - 12, BOOT_O + 22
    if lose:
        pts = [(POLLER_X, STEG_O - 26), (POLLER_X - 8, STEG_O + 10), (POLLER_X - 4, STEG_O + 40)]
    else:
        pts = [(bx, by), (bx + 10, by + 6), (POLLER_X - 8, STEG_O - 6), (POLLER_X, STEG_O - 26)]
    return bis_(linienzug(pts, cue, breite=7, farbe=(120, 80, 50, 255)), bis)


def seekulisse(cue):
    return [see(cue), ufer(cue), steg(cue), poller(cue),
            hart(ficon("tabler", "sunset", 1790, 230, 120, cue, fuell=GELB, anim="cut")),
            hart(ficon("tabler", "trees", 1790, BODEN + 4, 130, cue, fuell=GRUEN, anim="cut"))]


WIX, WIU = 1110, STEG_O                     # Wieland auf dem Steg
HAX = 1560                                  # Hartwin am Ufer

# ===========================================================================================================================
# A Fall: Sommerabend am See. Wieland steht auf dem Steg (blickt nach links zum Boot), bindet das Tretboot los, fährt über
# den See (Bewegung nach links), kommt zurück (Bewegung nach rechts) und bindet es wieder fest. Hartwin kommt am Ufer hinzu.
# ===========================================================================================================================
LOS = beim("nimmt", "bindet")
FAEHRT = beim("nimmt", "fährt")
BRINGT = beim("zurueck", "bringt")
FEST = beim("zurueck", "bindet")
DX = BOOT_X - BOOT_FAHRT
ANKUNFT = beim("zurueck", "zurück", ende=True)
RUECK = tretboot(BOOT_X, BRINGT, bis=FEST, mit="WB_ruhig_r", spiegeln=True, weg=(BRINGT, ANKUNFT, -DX))
szene(RUECK[-1], "165steg*", 0.8, round(T_(ANKUNFT) - T_(BRINGT) - 0.43, 3))   # Rumpf stößt beim Anlegen an den Steg
folie([(NULL, "Fall · Ein Sommerabend am See"), ("boot", "Fall · Das Tretboot von Hartwin"),
       ("nimmt", "Fall · Wieland fährt los, ohne zu fragen"), ("zurueck", "Fall · Wieland bringt das Boot zurück"),
       ("ha1", "Fall · „Das ist doch Diebstahl!“"), ("frage", "Die Frage · Passt ein Paragraf genau?"),
       ("frage2", "Die Frage · Pech für den Staat?")], [
    *seekulisse(NULL),
    hart(pl("Ein Sommerabend am See", 70, 40, NULL, fill=GELB, size=34, bis="ha1")),
    # Boot festgemacht ab 0,0 s bis „fährt“; Seil bis „bindet … los“
    *tretboot(BOOT_X, NULL, bis=FAEHRT),
    seil(NULL, bis=LOS), seil(LOS, bis=FAEHRT, lose=True),
    pl("Tretboot von Hartwin", 70, 108, "boot", fill=WEISS, size=32, bis="ha1"),
    pl("nur mit einem Seil festgebunden", 70, 172, beim("boot", "Seil"), fill=WEISS, size=32, bis="ha1"),
    ring(POLLER_X - 30, STEG_O - 4, 70, 42, beim("boot", "Seil"), bis=LOS),
    # Fahrt hinaus (nach links), Rückfahrt (nach rechts)
    *[szene(e, "165treten*", 0.7, 0.0) if i == 0 else e for i, e in
      enumerate(tretboot(BOOT_FAHRT, FAEHRT, bis=BRINGT, mit="WB_froh", weg=(FAEHRT, beim("nimmt", "See"), DX)))],
    pl("eine Stunde über den See, ohne zu fragen", 70, 236, beim("nimmt", "Stunde"), fill=PINK, size=32, bis="ha1"),
    *RUECK,
    *tretboot(BOOT_X, FEST), seil(FEST),
    pl("wieder festgebunden", 70, 300, FEST, fill=WEISS, size=32, bis="ha1"),
    pl("Kaputt ist nichts.", 70, 364, beim("zurueck", "Kaputt"), fill=GRUEN, size=32, bis="ha1"),
    # Wieland auf dem Steg: bis „fährt“ und ab „bindet … fest“
    *fig("WI", WIX, WIU, FH, [(NULL, "ruhig"), (LOS, "frech")], bis=FAEHRT, erst="cut"),
    bis_(hart(ns("Wieland", WIX, WIU, NULL, TUERKIS)), FAEHRT),
    *fig("WI", WIX, WIU, FH, [(FEST, "froh_r"), ("ha1", "sorge_r")], bis="wi1", erst="cut"),
    *redet("WI_redet_r", WIX, WIU, FH, "wi1", "frage"),
    *fig("WI", WIX, WIU, FH, [("frage", "frech_r")], erst="cut"),
    ns("Wieland", WIX, WIU, FEST, TUERKIS, anim="cut"),
    # Hartwin kommt am Ufer hinzu (blickt nach links zu Wieland)
    *redet("HA_redet", HAX, BODEN, FH + 20, "ha1", "wi1"),
    *fig("HA", HAX, BODEN, FH + 20, [("wi1", "ernst"), ("frage2", "denkt")], erst="cut"),
    ns("Hartwin", HAX, BODEN, "ha1", ORANGE, anim="cut"),
    blase("sprech", 600, 230, "ha1", 1420, 210, inhalt=["Das ist doch Diebstahl!", "Dafür gehört er bestraft!"], textsize=32,
          figur=("HA_redet", HAX, BODEN, FH + 20), bis="wi1"),
    blase("sprech", 520, 200, "wi1", 760, 250, inhalt=["Ich habe es doch", "zurückgebracht."], textsize=32,
          figur=("WI_redet_r", WIX, WIU, FH), bis="frage"),
    pl("Verwerflich – aber passt ein Paragraf genau?", 70, 40, "frage", fill=WEISS, size=34),
    pl("Pech für den Staat?", 70, 112, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_165(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_165("sv", [
    "Hartwin hat sein Tretboot am öffentlichen Steg eines Sees mit einem Seil festgebunden. Ohne zu fragen, bindet "
    "Wieland es los und fährt eine Stunde damit über den See. Er will es von Anfang an zurückbringen.",
    "Danach bindet er das Boot wieder am Steg fest. Beschädigt ist nichts.",
    "Hartwin meint: „Das ist doch Diebstahl! Dafür gehört er bestraft!“",
], "Hat Wieland sich strafbar gemacht?")

# ===========================================================================================================================
# C1 Diebstahl? Wortlautkarte § 242 Abs. 1 StGB; bloße Gebrauchsanmaßung (BGH 3 StR 484/14 Rn. 6)
# ===========================================================================================================================
PF = "Welcher Paragraf?"
W242 = ["„(1) Wer eine fremde bewegliche Sache einem anderen in der",
        "Absicht wegnimmt, die Sache sich oder einem Dritten",
        "rechtswidrig zuzueignen, wird … bestraft.“"]
w242, w242_y = wortlaut(80, 175, 1100, W242, "§ 242 Abs. 1 StGB (Auszug)", "dieb", marken=[
    (1, "Absicht", beim("dieb", "Absicht")), (2, "zuzueignen", beim("dieb", "zuzueignen"))], size=32)
folie([("dieb", f"{PF} · Diebstahl, § 242 StGB"), ("rueck", f"{PF} › nur benutzen und zurückbringen"),
       (beim("rueck", "kein"), f"{PF} › kein Diebstahl")], [
    *tafel("dieb", "Diebstahl?"),
    *w242,
    z("Wieland will das Boot nur benutzen", 110, w242_y + 40, "rueck", "Bold", 34),
    z("und zurückbringen: bloße Gebrauchsanmaßung", 110, w242_y + 86, beim("rueck", "maßt"), "Bold", 34),
    zit("BGH, Beschl. v. 17.12.2014 – 3 StR 484/14, Rn. 6", 110, w242_y + 140, beim("rueck", "maßt")),
    *neinz("kein Diebstahl", w242_y + 200, beim("rueck", "kein"), "ExtraBold", 36, x=160),
    *requisit([("dieb", ("tabler", "hand-grab", 110, WEISS), "Zueignung?", WEISS),
               ("rueck", ("tabler", "arrow-back-up", 110, GRUEN), "zurückbringen", GRUEN),
               (beim("rueck", "kein"), ("tabler", "ban", 100, HELLROT), "kein Diebstahl", HELLROT)]),
    *paar([("dieb", "ruhig"), (beim("rueck", "kein"), "froh")], [("dieb", "ernst"), (beim("rueck", "kein"), "sorge")]),
])

# ===========================================================================================================================
# C2 § 248b StGB (Wortlautkarte Abs. 1 und Abs. 4): nur Kraftfahrzeug oder Fahrrad
# ===========================================================================================================================
W248 = ["„(1) Wer ein Kraftfahrzeug oder ein Fahrrad gegen den Willen",
        "des Berechtigten in Gebrauch nimmt, wird … bestraft, …",
        "(4) Kraftfahrzeuge im Sinne dieser Vorschrift sind die",
        "Fahrzeuge, die durch Maschinenkraft bewegt werden, …“"]
w248, w248_y = wortlaut(80, 175, 1100, W248, "§ 248b Abs. 1 und 4 StGB (Auszug)", "p248", marken=[
    (0, "Kraftfahrzeug", beim("p248", "Kraftfahrzeugs")), (0, "Fahrrad", beim("p248", "Fahrrads")),
    (3, "Maschinenkraft", beim("kein", "Motor"))], size=31)
folie([("p248", f"{PF} · § 248b StGB: unbefugter Gebrauch"), ("kein", f"{PF} › Tretboot: kein Kraftfahrzeug"),
       (beim("kein", "Fahrrad"), f"{PF} › Tretboot: kein Fahrrad")], [
    *tafel("p248", "Unbefugter Gebrauch, § 248b StGB"),
    *w248,
    *neinz("kein Motor: kein Kraftfahrzeug", w248_y + 40, beim("kein", "Motor"), "Bold", 34, x=160),
    *neinz("kein Fahrrad, auch wenn man tritt", w248_y + 96, beim("kein", "Fahrrad"), "Bold", 34, x=160),
    *requisit([("p248", ("tabler", "car", 120, BLAU), "Kraftfahrzeug", BLAU),
               (beim("p248", "Fahrrads"), ("tabler", "bike", 120, GRUEN), "Fahrrad", GRUEN),
               ("kein", None, None, None)]),
    *rechts_frei(tretboot(PX - BOOT_W / 2, "kein", anim="pop", oben=300)),
    pl("Tretboot", PX, 100, "kein", fill=GELB, size=28, anker="m"),
    *paar([("p248", "denkt"), (beim("kein", "Fahrrad"), "froh")], [("p248", "ruhig"), ("kein", "sorge")]),
])

# ===========================================================================================================================
# D1 Art. 103 Abs. 2 GG und § 1 StGB (Wortlautkarten, vollständig vorgelesen bzw. „wortgleich“), nullum crimen …
# ===========================================================================================================================
PG = "Gesetzlichkeitsprinzip"
WT = ["„Eine Tat kann nur bestraft werden, wenn die Strafbarkeit",
      "gesetzlich bestimmt war, bevor die Tat begangen wurde.“"]
A103 = beim("a103", "Artikel")
w103, w103_y = wortlaut(80, 175, 1100, ["„(2) " + WT[0][1:], WT[1]], "Art. 103 Abs. 2 GG", A103, marken=[
    (1, "gesetzlich bestimmt", beim("a103", "gesetzlich")), (1, "bevor", beim("a103", "bevor"))], size=32)
w1, w1_y = wortlaut(80, w103_y + 20, 1100, WT, "§ 1 StGB – Keine Strafe ohne Gesetz", "p1", size=32)
folie([("a103", f"{PG} · Warum hilft das Gericht nicht nach?"), (A103, f"{PG} · Art. 103 Abs. 2 GG"),
       ("p1", f"{PG} › § 1 StGB: wortgleich"), ("latein", f"{PG} › nullum crimen, nulla poena sine lege")], [
    *tafel("a103", "Warum hilft das Gericht nicht nach?"),
    *w103, *w1,
    *okz("wortgleich", w1_y + 22, beim("p1", "wortgleich"), "Bold", 34, x=160),
    blk(110, w1_y + 90, 1040, 84, GELBHELL, "latein", [("nullum crimen, nulla poena sine lege", "ExtraBold", 36, INK)]),
    z("kein Verbrechen, keine Strafe ohne Gesetz", 140, w1_y + 192, beim("latein", "Kein"), "Bold", 34),
    *requisit([("a103", ("tabler", "help", 110, WEISS), "Gericht nachhelfen?", WEISS),
               (A103, ("tabler", "book", 110, WEISS), "Art. 103 Abs. 2 GG", WEISS),
               ("p1", ("tabler", "book-2", 110, GELB), "§ 1 StGB", GELB),
               ("latein", ("tabler", "scale", 120, GELBHELL), "sine lege", GELBHELL)]),
    *paar([("a103", "denkt"), ("latein", "ruhig")], [("a103", "ernst"), ("p1", "denkt")]),
])

# ===========================================================================================================================
# D2 Zwei Zwecke (BVerfGE 126, 170 Rn. 69 f.)
# ===========================================================================================================================
folie([("zweck", f"{PG} · zwei Zwecke"), ("z1", f"{PG} › Der Gesetzgeber entscheidet"),
       ("z2", f"{PG} › Vorhersehbarkeit")], [
    *tafel("zweck", "Zwei Zwecke"),
    zit("BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a., Rn. 69 f.", 110, 170, "zweck"),
    ficon("tabler", "building-bank", 190, 380, 120, "z1", fuell=BLAUHELL),
    blk(280, 240, 870, 150, BLAUHELL, "z1", [("1. Über Strafbarkeit entscheidet", "ExtraBold", 36, INK),
                                          ("der Gesetzgeber selbst.", "ExtraBold", 36, INK)]),
    ficon("tabler", "eye", 190, 600, 120, "z2", fuell=HELLGRUEN),
    blk(280, 460, 870, 150, HELLGRUEN, "z2", [("2. Jeder soll vorhersehen können,", "ExtraBold", 36, INK),
                                           ("was verboten ist.", "ExtraBold", 36, INK)]),
    *requisit([("zweck", ("tabler", "gavel", 120, HOLZ), "Bundesverfassungsgericht", WEISS),
               ("z1", ("tabler", "building-bank", 110, BLAUHELL), "Gesetzgeber", BLAUHELL),
               ("z2", ("tabler", "eye", 110, HELLGRUEN), "vorhersehbar", HELLGRUEN)]),
    *paar([("zweck", "ruhig"), ("z2", "denkt")], [("zweck", "denkt"), ("z1", "ruhig")]),
])

# ===========================================================================================================================
# E0 Vier Gewährleistungen (Überblick, deutsche Begriffe; Farben wie die vier Tafeln)
# ===========================================================================================================================
PV = "Vier Gewährleistungen"
folie([("vier", f"{PV} · Überblick"), ("va", f"{PV} › geschrieben"), ("vb", f"{PV} › bestimmt"),
       ("vc", f"{PV} › streng angewendet"), ("vd", f"{PV} › vor der Tat")], [
    *tafel("vier", "Vier Gewährleistungen"),
    zit("Art. 103 Abs. 2 GG, § 1 StGB", 110, 170, "vier"),
    blk(110, 230, 505, 150, BLAU, "va", [("1. geschrieben", "ExtraBold", 38, INK)]),
    blk(645, 230, 505, 150, GELB, "vb", [("2. bestimmt", "ExtraBold", 38, INK)]),
    blk(110, 420, 505, 150, LILA, "vc", [("3. streng angewendet", "ExtraBold", 38, INK)]),
    blk(645, 420, 505, 150, GRUEN, "vd", [("4. schon vor der Tat", "ExtraBold", 36, INK), ("gelten", "ExtraBold", 36, INK)]),
    *requisit([("vier", ("tabler", "list-numbers", 110, WEISS), "vier Gewährleistungen", WEISS)]),
    *paar([("vier", "ruhig"), ("vc", "denkt")], [("vier", "denkt"), ("vd", "ruhig")]),
])


# ===========================================================================================================================
# E1–E4 je eine Tafel in eigener Farbe, gleiche Struktur: Titel + Pille „Gewährleistung n“, Kernzeile (Begriff, Adressat),
# Inhalt, farbiger Block am Fall/Beispiel, Fundstelle
# ===========================================================================================================================
def gewaehr_tafel(nr, cue, titel_):
    farbe, hell, _ = GEW[nr]
    return [*tafel(cue, titel_, fill=hell, frei=880), pl(f"Gewährleistung {nr}", 930, 96, cue, fill=farbe, size=30)]


folie([("sa", "1. lex scripta · geschriebenes Gesetz"), ("sb", "1. lex scripta › kein Gewohnheitsrecht"),
       ("sc", "1. lex scripta › Anstand ist kein Straftatbestand")], [
    *gewaehr_tafel(1, "sa", "1. lex scripta"),
    z("Strafe braucht ein geschriebenes Gesetz.", 110, 190, beim("sa", "Strafe"), "ExtraBold", 36),
    *neinz("Gewohnheitsrecht begründet keine Strafbarkeit", 290, "sb", "Bold", 34),
    zit("BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a., Rn. 68, 77", 185, 345, "sb"),
    blk(110, 440, 1040, 130, BLAU, "sc", [("Fremde Boote nicht nehmen:", "ExtraBold", 34, INK),
                                       ("Regel des Anstands, kein Straftatbestand", "Bold", 34, INK)]),
    *requisit([("sa", ("tabler", "writing", 110, BLAU), "geschrieben", BLAU),
               ("sb", ("tabler", "ban", 100, HELLROT), "kein Gewohnheitsrecht", HELLROT),
               ("sc", ("tabler", "heart-handshake", 110, BLAUMITTEL), "Anstand", BLAUMITTEL)]),
    *paar([("sa", "ruhig"), ("sc", "froh")], [("sa", "denkt"), ("sc", "sorge")]),
])

folie([("ca", "2. lex certa · Bestimmtheitsgebot"), (beim("ca", "richtet"), "2. lex certa › richtet sich an den Gesetzgeber"),
       ("cb", "2. lex certa › am Wortlaut erkennbar"), ("cc", "2. lex certa › „Wer Unrecht tut …“ genügt nicht")], [
    *gewaehr_tafel(2, "ca", "2. lex certa"),
    z("Bestimmtheitsgebot", 110, 190, beim("ca", "Bestimmtheitsgebot"), "ExtraBold", 36),
    z("richtet sich an den Gesetzgeber", 520, 192, beim("ca", "richtet"), "Bold", 34),
    z("Strafbarkeit so genau beschreiben, dass man sie", 110, 280, "cb", "Bold", 34),
    z("im Regelfall schon am Wortlaut erkennt", 110, 326, beim("cb", "Regelfall"), "Bold", 34),
    zit("BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a., Rn. 71", 110, 380, beim("cb", "Regelfall")),
    blk(110, 440, 1040, 130, GELB, "cc", [("„Wer Unrecht tut, wird bestraft.“", "ExtraBold", 34, INK),
                                       ("zu unbestimmt: genügte dem nicht", "Bold", 34, INK)]),
    nein(1100, 505, beim("cc", "genügte"), gr=24),
    *requisit([("ca", ("tabler", "focus", 110, GELB), "bestimmt", GELB),
               (beim("ca", "richtet"), ("tabler", "building-bank", 110, GELBHELL), "Gesetzgeber", GELBHELL),
               ("cc", ("tabler", "help", 110, HELLROT), "zu vage", HELLROT)]),
    *paar([("ca", "denkt"), ("cc", "frech")], [("ca", "ruhig"), ("cc", "denkt")]),
])

folie([("sta", "3. lex stricta · Analogieverbot"), (beim("sta", "richtet"), "3. lex stricta › richtet sich an die Gerichte"),
       ("stb", "3. lex stricta › § 248b nicht auf Tretboote"), ("stc", "3. lex stricta › Verweis auf zwei Folgen")], [
    *gewaehr_tafel(3, "sta", "3. lex stricta"),
    z("Analogieverbot", 110, 190, beim("sta", "Analogieverbot"), "ExtraBold", 36),
    z("richtet sich an die Gerichte", 430, 192, beim("sta", "richtet"), "Bold", 34),
    *neinz2("§ 248b StGB nicht auf Tretboote erweitern", 290, "stb", beim("stb", "nicht"), "Bold", 34),
    blk(110, 440, 1040, 130, LILA, "stc", [("Einzelheiten: Folgen zur Analogie", "ExtraBold", 34, INK),
                                        ("und zur Unfallflucht", "Bold", 34, INK)]),
    *requisit([("sta", ("tabler", "ban", 100, LILA), "streng", LILA),
               (beim("sta", "richtet"), ("tabler", "gavel", 120, HOLZ), "Gerichte", WEISS),
               ("stc", ("tabler", "player-play", 110, LILAMITTEL), "zwei Folgen", LILAMITTEL)]),
    *paar([("sta", "ruhig"), ("stb", "froh")], [("sta", "denkt"), ("stb", "sorge")]),
])

W2 = ["„(1) Die Strafe und ihre Nebenfolgen bestimmen sich nach dem",
      "Gesetz, das zur Zeit der Tat gilt.“"]
w2, w2_y = wortlaut(80, 260, 1100, W2, "§ 2 Abs. 1 StGB", "pb", marken=[(1, "zur Zeit der Tat", beim("pb", "zur"))], size=32)
folie([("pa", "4. lex praevia · Rückwirkungsverbot"), ("pb", "4. lex praevia › § 2 Abs. 1 StGB"),
       ("pc", "4. lex praevia › neues Gesetz zu spät")], [
    *gewaehr_tafel(4, "pa", "4. lex praevia"),
    z("Rückwirkungsverbot", 110, 190, beim("pa", "Rückwirkungsverbot"), "ExtraBold", 36),
    *w2,
    blk(110, w2_y + 30, 1040, 130, GRUEN, "pc", [("neues Gesetz gegen fremde Bootsfahrten:", "ExtraBold", 34, INK),
                                              ("für Wieland zu spät", "Bold", 34, INK)]),
    *requisit([("pa", ("tabler", "history", 110, GRUEN), "vorher", GRUEN),
               ("pb", ("tabler", "calendar-time", 110, HELLGRUEN), "Tatzeit", HELLGRUEN),
               ("pc", ("tabler", "calendar-x", 110, WEISS), "zu spät", WEISS)]),
    *paar([("pa", "ruhig"), ("pc", "froh")], [("pa", "denkt"), ("pc", "muede")]),
])

# ===========================================================================================================================
# F1 Schwerpunkt Bestimmtheit: Untreue-Beschluss BVerfGE 126, 170 (Leitsatz 1, Rn. 73, 84, 89)
# ===========================================================================================================================
PB = "Bestimmtheit"
Z73 = ["„Es schließt die Verwendung wertausfüllungsbedürftiger",
       "Begriffe bis hin zu Generalklauseln im Strafrecht nicht",
       "von vornherein aus …“"]
DENN = beim("gk", "Denn")
z73, z73_y = wortlaut(80, 480, 1100, Z73, "BVerfGE 126, 170, Rn. 73", DENN, marken=[
    (1, "Generalklauseln", beim("gk", "Generalklauseln"))], size=31)
folie([("best", f"{PB} · Wie bestimmt muss ein Strafgesetz sein?"), ("unt", f"{PB} › Untreue-Beschluss 2010"),
       ("weit", f"{PB} › § 266 StGB: sehr weit gefasst"), ("gk", f"{PB} › noch vereinbar"),
       (DENN, f"{PB} › Generalklauseln nicht ausgeschlossen")], [
    *tafel("best", "Wie bestimmt muss es sein?"),
    z("Untreue-Beschluss", 110, 180, beim("unt", "Untreue-Beschluss"), "ExtraBold", 36),
    zit("BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a. (BVerfGE 126, 170)", 110, 232, beim("unt", "Untreue-Beschluss")),
    z("§ 266 StGB (Untreue): sehr weit gefasst", 110, 290, "weit", "Bold", 34),
    zit("Rn. 89", 790, 298, "weit"),
    *okz("mit dem Bestimmtheitsgebot noch vereinbar", 360, beim("gk", "vereinbar"), "Bold", 34, x=160),
    zit("Leitsatz 1, Rn. 84", 160, 410, beim("gk", "vereinbar")),
    *z73,
    *requisit([("best", ("tabler", "focus", 110, GELB), "Bestimmtheit", GELB),
               ("weit", ("tabler", "arrows-diagonal-minimize", 110, WEISS), "sehr weit", WEISS),
               ("gk", ("tabler", "circle-check", 110, GRUEN), "noch vereinbar", GRUEN)]),
    *paar([("best", "denkt"), ("gk", "ruhig")], [("best", "ruhig"), ("weit", "denkt")]),
])

# ===========================================================================================================================
# F2 Pflichten der Rechtsprechung: Präzisierungsgebot (Rn. 80, Zitatkarte), Verbot der Verschleifung (Rn. 78)
# ===========================================================================================================================
Z80 = ["„… ist die Rechtsprechung gehalten, verbleibende Unklarheiten",
       "über den Anwendungsbereich einer Norm durch Präzisierung",
       "und Konkretisierung im Wege der Auslegung nach Möglichkeit",
       "auszuräumen (Präzisierungsgebot).“"]
z80, z80_y = wortlaut(80, 175, 1100, Z80, "BVerfGE 126, 170, Rn. 80", "pg", marken=[
    (1, "Präzisierung", beim("pg", "Präzisierung")), (3, "Präzisierungsgebot", beim("pg", "Präzisierungsgebot"))], size=30)
folie([("pflicht", f"{PB} · Pflichten der Rechtsprechung"), ("pg", f"{PB} › Präzisierungsgebot"),
       ("versch", f"{PB} › kein Merkmal geht im anderen auf"), ("vs2", f"{PB} › Verbot der Verschleifung")], [
    *tafel("pflicht", "Pflichten der Rechtsprechung"),
    *z80,
    z("Kein Merkmal so weit auslegen,", 110, z80_y + 34, "versch", "Bold", 34),
    z("dass es in einem anderen aufgeht.", 110, z80_y + 80, beim("versch", "dass"), "Bold", 34),
    blk(110, z80_y + 150, 700, 84, HELLROT, "vs2", [("Verschleifung: verboten", "ExtraBold", 34, INK)]),
    zit("BVerfGE 126, 170, Rn. 78", 840, z80_y + 180, "vs2"),
    *requisit([("pflicht", ("tabler", "gavel", 120, HOLZ), "Rechtsprechung", WEISS),
               ("pg", ("tabler", "zoom-in", 110, GELB), "präzisieren", GELB),
               ("versch", ("tabler", "arrows-join", 110, HELLROT), "Verschleifung", HELLROT)]),
    *paar([("pflicht", "ruhig"), ("versch", "denkt")], [("pflicht", "denkt"), ("vs2", "ernst")]),
])

# ===========================================================================================================================
# F3 Daran scheiterte eine Verurteilung (Rn. 152, 154, 158)
# ===========================================================================================================================
NT_NACH = beim("nt2", "Vermögensnachteil")
NT_PFL = beim("nt2", "Pflichtwidrigkeit")
folie([("nachteil", f"{PB} · Daran scheiterte eine Verurteilung"), ("nt2", f"{PB} › Nachteil nicht eigenständig ermittelt"),
       (NT_PFL, f"{PB} › aus der Pflichtwidrigkeit gefolgert"), ("aufh", f"{PB} › Urteil aufgehoben")], [
    *tafel("nachteil", "Daran scheiterte eine Verurteilung"),
    z("Das Landgericht:", 110, 185, "nt2", "ExtraBold", 34),
    blk(700, 260, 450, 140, PINK, NT_NACH, [("Vermögensnachteil", "ExtraBold", 34, INK), ("§ 266 StGB", "Regular", 30, INK)]),
    *neinz("nicht eigenständig", 425, beim("nt2", "nicht"), "Bold", 34, x=750),
    z("ermittelt", 750, 471, beim("nt2", "ermittelt"), "Bold", 34),
    blk(110, 260, 450, 140, WEISS, NT_PFL, [("Pflichtwidrigkeit", "ExtraBold", 34, INK), ("§ 266 StGB", "Regular", 30, INK)]),
    pfeil(570, 330, 690, 330, beim("nt2", "gefolgert"), breite=10, kopf=28),
    z("gefolgert", 566, 284, beim("nt2", "gefolgert"), "Bold", 26),
    blk(110, 540, 1040, 84, GRUEN, "aufh", [("Das Bundesverfassungsgericht hob das Urteil auf.", "ExtraBold", 34, INK)]),
    zit("BVerfGE 126, 170, Rn. 152, 154, 158", 110, 640, "aufh"),
    *requisit([("nachteil", ("tabler", "coin-euro", 110, PINK), "Nachteil", PINK),
               ("aufh", ("tabler", "gavel", 120, HOLZ), "aufgehoben", GRUEN)]),
    *paar([("nachteil", "ruhig"), ("aufh", "froh")], [("nachteil", "denkt"), ("aufh", "ernst")]),
])

# ===========================================================================================================================
# F4 Sitzblockaden-Beschluss BVerfGE 92, 1 (DFR, Seitenzahlen): Gesetz bestimmt genug, vergeistigte Auslegung nicht
# ===========================================================================================================================
W240 = ["„(1) Wer einen Menschen rechtswidrig mit Gewalt oder durch",
        "Drohung mit einem empfindlichen Übel … nötigt, …“"]
w240, w240_y = wortlaut(80, 205, 1100, W240, "§ 240 Abs. 1 StGB (Auszug)", "sitz", marken=[
    (0, "Gewalt", beim("verg", "Gewaltbegriff"))], size=31)
VST_A = beim("vst", "Auslegung")
folie([("sitz", f"{PB} · Sitzblockaden-Beschluss 1995"), ("verg", f"{PB} › vergeistigter Gewaltbegriff"),
       ("unvor", f"{PB} › nicht mehr vorhersehbar"), ("vst", f"{PB} › Gesetz bestimmt genug"),
       (VST_A, f"{PB} › Auslegung verstößt gegen Art. 103 Abs. 2 GG")], [
    *tafel("sitz", "Sitzblockaden-Beschluss (1995)"),
    zit("BVerfG, Beschl. v. 10.1.1995 – 1 BvR 718/89 u. a. (BVerfGE 92, 1)", 110, 160, "sitz"),
    *w240,
    z("vergeistigt: bloße Anwesenheit auf der Straße", 110, w240_y + 26, beim("verg", "vergeistigt"), "Bold", 33),
    z("+ psychische Hemmung = Gewalt", 110, w240_y + 70, beim("verg", "psychisch"), "Bold", 33),
    zit("BVerfGE 92, 1 (15, 17)", 650, w240_y + 78, beim("verg", "psychisch")),
    *neinz("nicht mehr sicher vorhersehbar, was verboten ist", w240_y + 130, "unvor", "Bold", 33, x=160),
    zit("(18)", 1000, w240_y + 138, "unvor"),
    *okz("das Gesetz: bestimmt genug", w240_y + 200, "vst", "Bold", 33, x=160),
    zit("(13)", 620, w240_y + 208, "vst"),
    blk(110, w240_y + 262, 1040, 84, HELLROT, VST_A, [("die Auslegung: Verstoß gegen Art. 103 Abs. 2 GG", "ExtraBold", 33, INK)]),
    zit("BVerfGE 92, 1 (1, 14); mit 5 : 3 Stimmen (16)", 110, w240_y + 358, VST_A),
    *requisit([("sitz", ("tabler", "road", 110, WEISS), "Sitzblockade", WEISS),
               ("verg", ("tabler", "ghost", 110, LILAMITTEL), "vergeistigt", LILAMITTEL),
               ("unvor", ("tabler", "help", 110, HELLROT), "vorhersehbar?", HELLROT),
               (VST_A, ("tabler", "gavel", 120, HOLZ), "Verstoß", HELLROT)]),
    *paar([("sitz", "ruhig"), ("unvor", "denkt")], [("sitz", "denkt"), (VST_A, "ernst")]),
])

# ===========================================================================================================================
# G1 Nur zulasten: Analogie zugunsten nicht verboten (BGH 1 StR 118/20, Leitsatz, Rn. 19–21; § 306e StGB analog)
# ===========================================================================================================================
PZ = "Nur zulasten"
folie([("zug", f"{PZ} · Schutz vor Strafe"), ("zug2", f"{PZ} › Analogie zugunsten nicht verboten"),
       ("zbsp", f"{PZ} › Beispiel: tätige Reue, § 306e StGB analog")], [
    *tafel("zug", "Schutz vor Strafe"),
    z("Art. 103 Abs. 2 GG schützt vor Strafe.", 110, 180, "zug", "Bold", 34),
    *okz("Analogie zugunsten des Täters: nicht verboten", 260, "zug2", "Bold", 34, x=160),
    zit("BGH, Beschl. v. 27.5.2020 – 1 StR 118/20, Rn. 21", 160, 310, "zug2"),
    blk(110, 380, 1040, 176, HELLGRUEN, beim("zbsp", "tätige"), [("Beispiel: tätige Reue, § 306e StGB analog", "ExtraBold", 33, INK),
                                                             ("Täter beseitigt die Lebensgefahr freiwillig", "Regular", 32, INK),
                                                             ("auf andere Weise als durch Löschen", "Regular", 32, INK)]),
    zit("BGH, Beschl. v. 27.5.2020 – 1 StR 118/20, Leitsatz, Rn. 19 f.", 110, 570, beim("zbsp", "tätige")),
    *requisit([("zug", ("tabler", "shield-check", 110, WEISS), "Schutz vor Strafe", WEISS),
               ("zug2", ("tabler", "circle-check", 110, GRUEN), "zugunsten: erlaubt", GRUEN),
               ("zbsp", ("tabler", "lifebuoy", 110, HELLGRUEN), "tätige Reue", HELLGRUEN)]),
    *paar([("zug", "ruhig"), ("zug2", "froh")], [("zug", "denkt"), ("zbsp", "ruhig")]),
])

# ===========================================================================================================================
# G2 § 3 OWiG (Wortlautkarte)
# ===========================================================================================================================
W3 = ["„Eine Handlung kann als Ordnungswidrigkeit nur geahndet werden,",
      "wenn die Möglichkeit der Ahndung gesetzlich bestimmt war,",
      "bevor die Handlung begangen wurde.“"]
w3, w3_y = wortlaut(80, 175, 1100, W3, "§ 3 OWiG – Keine Ahndung ohne Gesetz", "owi2", marken=[
    (1, "gesetzlich bestimmt", beim("owi2", "gesetzlich")), (2, "bevor", beim("owi2", "bevor"))], size=31)
folie([("owi", f"{PZ} · auch für Ordnungswidrigkeiten"), ("owi2", f"{PZ} › § 3 OWiG")], [
    *tafel("owi", "Auch für Ordnungswidrigkeiten"),
    *w3,
    *requisit([("owi", ("tabler", "receipt", 110, WEISS), "Ordnungswidrigkeit", WEISS),
               ("owi2", ("tabler", "book", 110, GELB), "§ 3 OWiG", GELB)]),
    *paar([("owi", "ruhig"), ("owi2", "denkt")], [("owi", "denkt"), ("owi2", "ruhig")]),
])

# ===========================================================================================================================
# H Lösung: zurück am See (gleiche Bühne wie A, weil die Geschichte an den Steg zurückkehrt)
# ===========================================================================================================================
folie([("loes", "Lösung · zurück am See"), ("l1", "Lösung › Diebstahl scheidet aus"),
       (beim("l1", "Paragraf"), "Lösung › § 248b erfasst kein Tretboot"), ("l2", "Ergebnis · Wieland bleibt straflos"),
       ("ha2", "Ergebnis · „Einfach erlaubt?“"), ("pech", "Ergebnis · Pech für den Staat"),
       ("lg", "Ergebnis › Lücken schließt nur der Gesetzgeber")], [
    *seekulisse("loes"),
    *tretboot(BOOT_X, "loes"), seil("loes"),
    *fig("WI", WIX, WIU, FH, [("loes", "ruhig_r"), ("l2", "froh_r"), ("ha2", "denkt_r"), ("lg", "ruhig_r")], erst="cut"),
    hart(ns("Wieland", WIX, WIU, "loes", TUERKIS)),
    *fig("HA", HAX, BODEN, FH + 20, [("loes", "ernst"), ("l2", "sorge")], bis="ha2", erst="cut"),
    *redet("HA_fragt", HAX, BODEN, FH + 20, "ha2", "pech"),
    *fig("HA", HAX, BODEN, FH + 20, [("pech", "muede"), ("lg", "denkt")], erst="cut"),
    hart(ns("Hartwin", HAX, BODEN, "loes", ORANGE)),
    pl("Diebstahl scheidet aus", 70, 40, beim("l1", "Diebstahl"), fill=HELLROT, size=32, bis="ha2"),
    pl("§ 248b StGB erfasst kein Tretboot", 70, 104, beim("l1", "Paragraf"), fill=HELLROT, size=32, bis="ha2"),
    pl("Wieland bleibt straflos", 70, 168, "l2", fill=GRUEN, size=34, bis="ha2"),
    blase("sprech", 500, 200, "ha2", 1380, 220, inhalt=["Das ist also", "einfach erlaubt?"], textsize=32,
          figur=("HA_fragt", HAX, BODEN, FH + 20), bis="pech"),
    pl("Strafbar ist es jedenfalls nicht. Pech für den Staat.", 70, 40, "pech", fill=PINK, size=32),
    pl("Strafbarkeitslücken schließt nur der Gesetzgeber,", 70, 104, "lg", fill=WEISS, size=32),
    pl("und zwar nur für künftige Taten.", 70, 168, beim("lg", "und"), fill=WEISS, size=32),
    zit("BVerfGE 126, 170, Rn. 77; Art. 103 Abs. 2 GG", 80, 252, beim("lg", "und")),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi) – Formulierung als „üblich“ gekennzeichnet
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · auslegen bis zur Wortlautgrenze"), ("tipp2", "Klausurtipp · dann Schluss"),
       ("tipp3", "Klausurtipp · übliche Formulierung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Tatbestand auslegen,", 200, 200, beim("tipp", "Lege"), "Bold", 36),
    z("bis zur Grenze des Wortlauts", 200, 248, beim("tipp", "Grenze"), "Bold", 36),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    *neinz("passt der Fall dann nicht: Schluss", 365, "tipp2", "Bold", 36, x=200),
    z("keine Analogie zulasten des Täters", 200, 415, beim("tipp2", "keine"), "Bold", 36),
    blk(130, 500, 1000, 200, GELBHELL, "tipp3", [("üblich etwa:", "ExtraBold", 33, INK),
                                              ("„Eine Anwendung auf das Tretboot wäre", "Bold", 33, INK),
                                              ("eine nach Art. 103 Abs. 2 GG", "Bold", 33, INK),
                                              ("verbotene Analogie.“", "Bold", 33, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfraster (Farbpunkte der vier Gewährleistungen, Reihenfolge wie gesprochen)
# ===========================================================================================================================
REIHEN = [("k1", "1. Gibt es ein geschriebenes Gesetz?", "lex scripta", BLAU),
          ("k2", "2. Galt es schon zur Tatzeit?", "lex praevia", GRUEN),
          ("k3", "3. Ist es bestimmt genug?", "lex certa", GELB),
          ("k4", "4. Erfasst sein Wortlaut den Fall?", "lex stricta", LILA)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel("Prüfraster: Art. 103 Abs. 2 GG", 110, 90, "sch", 46)]
y = 210
for c, text, lat, farbe in REIHEN:
    im = Image.new("RGBA", (34, 34)); ImageDraw.Draw(im).ellipse((0, 0, 33, 33), fill=farbe, outline=INK, width=4)
    els_sch.append(El(im, 130, y + 12, c, "pop", 0.0, None, name="punkt"))
    els_sch.append(z(text, 190, y, c, "ExtraBold", 42, rechts=1800))
    els_sch.append(z(lat, 1100, y + 8, c, "Regular", 34, farbe=TEXT, rechts=1800))
    y += 110
els_sch.append(blk(130, y + 20, 1100, 90, GELBHELL, "k5", [("Nur wenn alles zutrifft, darf bestraft werden.", "ExtraBold", 38, INK)]))
assert y + 110 <= 970, y
folie([("sch", "Prüfraster"), ("k1", "Prüfraster › 1. geschriebenes Gesetz"), ("k2", "Prüfraster › 2. zur Tatzeit"),
       ("k3", "Prüfraster › 3. bestimmt genug"), ("k4", "Prüfraster › 4. Wortlaut erfasst den Fall"),
       ("k5", "Prüfraster › nur dann Strafe")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Keine Strafe ohne ", 0), ("geschriebenes", "a"), (",", 0)],
                 [("bestimmtes", "b"), (" und ", 0), ("vorher geltendes", "c"), (" Gesetz.", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "geschriebenes"), "b": beim("merke", "bestimmtes"),
                                       "c": beim("merke", "vorher")}),
    *markertext([[("Was der Wortlaut nicht erfasst,", 0)], [("bleibt ", 0), ("straflos", "d"), (".", 0)],
                 [("Lücken schließt nur der ", 0), ("Gesetzgeber", "e"), (".", 0)]], 750, 500, 44, "m2",
                {"d": beim("m2", "straflos"), "e": beim("m2", "Gesetzgeber")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
