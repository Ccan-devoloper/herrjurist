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
    dr.rounded_rectangle((o + 150 * s, o + 30 * s, o + 175 * s, o + 150 * s), 8 * s, fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if spiegeln else im


def tretboot(x, cue, bis=None, spiegeln=False, weg=None, mit=None, anim="cut", oben=BOOT_O):
    """Tretboot (Rumpf Gelb mit roter Linie, Radkasten Blau, Sitzlehne) bei Rumpf-x = x; mit = Figur im Boot
    (Name der Ansicht), weg = (start, ende, dx) Bewegung über den See. Reihenfolge: Aufbau, Figur, Rumpf."""
    els = []
    a = El(_aufbau(spiegeln), x - 6, oben - 150 + 20 - 6, cue, anim, 0.0, bis, name="boot_aufbau")
    els.append(a)
    if mit:
        els.append(peep_voll(mit, x + BOOT_W / 2, oben + 70, 330, cue, anim=anim, bis=bis))
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
