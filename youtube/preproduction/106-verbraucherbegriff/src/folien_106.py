"""Folge 106 · Laptop für Kanzlei und Netflix: Der Verbraucherbegriff (§ 13 BGB) – Serienstandard Open Peeps (Katzenkönig).
Fall: Rechtsanwältin Ricarda (eigene Kanzlei) bestellt online bei Herrn Kortmann einen Laptop für 1.200 € (privates
Kundenkonto, Rechnung an die Wohnung, Lieferung an die Kanzlei); Nutzung 40 % Kanzlei, 60 % privat; Widerruf nach einer Woche.
Szenen laut ../SZENENPLAN.md: A1 Bestellung (Bildschirm), A2 Lieferung/Nutzung (Kanzlei und Wohnzimmer), A3 Widerruf und
Frage, B Sachverhalt, C Widerrufsrecht (§ 312g), D § 13 (Wortlaut), E § 14 Abs. 1 (Wortlaut, freier Beruf), F Dual Use
(Waage, Gegenfall), G EuGH Gruber, H Zweck und erkennbare Umstände, I Lampenfall und Ricarda (Zweispalter), J Ergebnis,
K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Zwei Handlungsgeräusche (Klick beim Bestellen, Paket in der Kanzlei; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene
Kopie aus Folge 086 (gemeinsame Dateien unverändert), neu: waage(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Im Bild kein Streaming-Logo, nur das neutrale Film-Icon (tabler:movie)."""
import sys, math
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_106/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_106/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/086) -------------------------------
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


def waage(cx, py, winkel, links, rechts, cue, bis=None, lf=WEISS, rf=WEISS):
    """Balkenwaage (gezeichnet aus Tuschelinien und zwei Schalen-Karten): Drehpunkt (cx, py); winkel > 0 = rechte Schale
    unten. links/rechts = Beschriftung der Schalen (Liste von Zeilen)."""
    s, W_, H_, SEIL = 2, 900, 360, 70
    im = Image.new("RGBA", (W_ * s, H_ * s)); dr = ImageDraw.Draw(im)
    ox, oy, L = 450, 50, 320
    a = math.radians(winkel)
    ex, ey = L * math.cos(a), L * math.sin(a)
    # Ständer und Fuß
    dr.line([(ox * s, oy * s), (ox * s, 320 * s)], fill=INK, width=9 * s)
    dr.rounded_rectangle(((ox - 120) * s, 312 * s, (ox + 120) * s, 344 * s), 12 * s, fill=INK)
    dr.rounded_rectangle(((ox - 114) * s, 318 * s, (ox + 114) * s, 338 * s), 8 * s, fill=GELB)
    # Balken
    dr.line([((ox - ex) * s, (oy - ey) * s), ((ox + ex) * s, (oy + ey) * s)], fill=INK, width=10 * s)
    f = F("Bold", 32)
    for sx, sy, txt, fl in ((ox - ex, oy - ey, links, lf), (ox + ex, oy + ey, rechts, rf)):
        dr.line([(sx * s, sy * s), ((sx - 105) * s, (sy + SEIL) * s)], fill=INK, width=4 * s)
        dr.line([(sx * s, sy * s), ((sx + 105) * s, (sy + SEIL) * s)], fill=INK, width=4 * s)
        x0, y0, x1, y1 = sx - 125, sy + SEIL, sx + 125, sy + SEIL + 40 + 40 * len(txt)
        dr.rounded_rectangle((x0 * s, y0 * s, x1 * s, y1 * s), 18 * s, fill=INK)
        dr.rounded_rectangle(((x0 + 5) * s, (y0 + 5) * s, (x1 - 5) * s, (y1 - 5) * s), 14 * s, fill=fl)
        for t in txt:
            glyphen(t)
            assert f.getlength(t) <= 230, f"Waagentext zu breit: {t}"
    dr.ellipse(((ox - 16) * s, (oy - 16) * s, (ox + 16) * s, (oy + 16) * s), fill=INK)
    dr.ellipse(((ox - 9) * s, (oy - 9) * s, (ox + 9) * s, (oy + 9) * s), fill=GELB)
    im = im.resize((W_, H_), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    for sx, sy, txt in ((ox - ex, oy - ey, links), (ox + ex, oy + ey, rechts)):
        y = sy + SEIL + 20
        for t in txt:
            b = f.getbbox(t)
            dr.text((sx - (b[2] - b[0]) / 2 - b[0], y - b[1] + 2), t, font=f, fill=INK)
            y += 40
    return El(im, cx - ox, py - oy, cue, "cut", 0.0, bis, name="waage:" + "/".join(links + rechts))


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
RI_N, KO_N = LILA, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"RI": "Ricarda", "KO": "Herr Kortmann"}
NFARBE = {"RI": RI_N, "KO": KO_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel RI/KO."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


# A1 Fall: die Bestellung (Bildschirm des Online-Shops) ------------------------------------------------------------------
MX = 1640                                            # Ricarda steht rechts und blickt zum Bildschirm
SX0, SY0, SW, SH = 80, 130, 1040, 560                # Bildschirm-Ausschnitt (Webseite)
BEST = beim("shop", "bestellt")
folie([(NULL, "Fall · Die Bestellung")], [
    hart(pl("Ricarda kauft einen Laptop", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "device-laptop", 760, 560, 300, NULL, fuell=BLAU, bis=BEST)),
    # Hook: Kanzlei und abends Filme (neutrales Film-Icon, kein Logo)
    ficon("tabler", "briefcase", 1440, 250, 110, beim("fall", "Kanzlei"), fuell=GELB),
    pl("Kanzlei", 1440, 262, beim("fall", "Kanzlei"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "movie", 1790, 250, 110, beim("fall", "abends"), fuell=LILA),
    pl("abends", 1790, 262, beim("fall", "abends"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "calendar-event", 1250, 520, 80, beim("shop", "Mai"), fuell=WEISS),
    pl("Mai", 1250, 530, beim("shop", "Mai"), fill=WEISS, size=30, anker="m"),
    # Bildschirm: der Online-Shop von Herrn Kortmann
    karte(SX0, SY0, SW, SH, BEST, fill=WEISS, rund=18, schatten=8),
    linienzug([(SX0 + 4, SY0 + 64), (SX0 + SW - 4, SY0 + 64)], BEST, breite=4),
    ficon("tabler", "device-laptop", SX0 + 830, SY0 + 330, 260, BEST, fuell=BLAU),
    szene(pl("Jetzt bestellen", SX0 + 40, SY0 + 450, BEST, fill=GRUEN, size=36), "106klick*", 0.6, 0.0),
    ficon("tabler", "pointer", SX0 + 330, SY0 + 540, 60, BEST, fuell=WEISS),
    z("Online-Shop Kortmann · Elektronik", SX0 + 30, SY0 + 12, beim("shop", "Herrn"), "Bold", 34, rechts=SX0 + SW - 16),
    z("Laptop · 1.200 €", SX0 + 40, SY0 + 100, beim("shop", "zwölfhundert"), "Bold", 40),
    ficon("tabler", "user", SX0 + 70, SY0 + 236, 50, "konto", fuell=LILA),
    z("Kundenkonto: privat", SX0 + 110, SY0 + 185, "konto", size=38),
    ficon("tabler", "home", SX0 + 70, SY0 + 326, 50, beim("konto", "Rechnung"), fuell=GELB),
    z("Rechnung an: Wohnung", SX0 + 110, SY0 + 275, beim("konto", "Rechnung"), size=38),
    # Ricarda (rechts, blickt zum Bildschirm nach links)
    *fig("RI", MX, BODEN, FH, [(NULL, "ruhig"), (BEST, "froh"), ("konto", "ruhig")], erst="cut"),
    hart(ns("Ricarda", MX, BODEN, NULL, RI_N)),
])

# A2 Fall: Lieferung in die Kanzlei, Nutzung in Kanzlei und Wohnzimmer -----------------------------------------------------
RX = 960
TISCH = ficon("tabler", "desk", 430, BODEN, 360, "_", fuell=GELB)
TY = int(TISCH.y + 0.12 * TISCH.sprite.height)       # Tischplatte
folie([("liefer", "Fall · Die Lieferung"), ("nutz", "Fall · Die Nutzung")], [
    pl("Lieferung an die Kanzlei", 70, 30, "liefer", fill=GELB, size=44, bis="nutz"),
    boden("liefer"),
    # Kanzlei links
    ficon("tabler", "desk", 430, BODEN, 360, "liefer", fuell=GELB),
    ficon("tabler", "briefcase", 160, BODEN, 120, "liefer", fuell=GELB),
    pl("Kanzlei", 430, 190, "liefer", fill=WEISS, size=34, anker="m"),
    szene(ficon("tabler", "package", 520, TY + 6, 130, beim("liefer", "Kanzlei"), fuell=GELB, bis="nutz"), "106paket*", 0.8, 0.0),
    ficon("tabler", "sun", 430, 400, 80, beim("liefer", "tagsüber"), fuell=GELB, bis="nutz"),
    pl("tagsüber dort", 430, 410, beim("liefer", "tagsüber"), fill=WEISS, size=30, anker="m", bis="nutz"),
    ficon("tabler", "device-laptop", 430, TY + 6, 170, "nutz", fuell=BLAU),
    pl("40 % Kanzlei", 430, 330, beim("nutz", "vierzig"), fill=GELB, size=40, anker="m"),
    # Wohnzimmer rechts (privat)
    ficon("tabler", "armchair", 1500, BODEN, 300, "privat", fuell=LILA),
    pl("60 % privat", 1560, 190, beim("privat", "sechzig"), fill=PINK, size=40, anker="m"),
    ficon("tabler", "movie", 1340, 440, 110, beim("privat", "Filme"), fuell=LILA),
    ficon("tabler", "photo", 1560, 440, 110, beim("privat", "Fotos"), fuell=GRUEN),
    ficon("tabler", "plane", 1780, 440, 110, beim("privat", "Urlaubsplanung"), fuell=BLAU),
    # Ricarda in der Mitte: erst zur Kanzlei (links), dann zum Wohnzimmer (rechts)
    *fig("RI", RX, BODEN, FH, [("liefer", "ruhig"), ("nutz", "denkt"), ("privat", "froh_r")], erst="cut"),
    ns("Ricarda", RX, BODEN, "liefer", RI_N),
])

# A3 Fall: der Widerruf per E-Mail, die Ablehnung, die Frage -------------------------------------------------------------------
AX, KX = 430, 1500
folie([("woche", "Fall · Der Widerruf"), ("frage", "Fall · Die Frage")], [
    pl("1 Woche nach der Lieferung", 70, 30, "woche", fill=GELB, size=44, bis="frage"),
    boden("woche"),
    ficon("tabler", "desk", 170, BODEN, 260, "woche", fuell=GELB),
    ficon("tabler", "device-laptop", 170, int(BODEN - 0.88 * 260 * 0.75) + 2, 130, "woche", fuell=BLAU),
    pl("Display gefällt nicht mehr", 70, 300, beim("woche", "Display"), fill=WEISS, size=30, bis="ri1"),
    ficon("tabler", "mail", 960, 560, 120, beim("woche", "E-Mail"), fuell=WEISS),
    pl("E-Mail", 960, 572, beim("woche", "E-Mail"), fill=WEISS, size=30, anker="m"),
    # Lager von Herrn Kortmann (rechts)
    ficon("tabler", "packages", 1790, BODEN, 190, beim("woche", "Herrn"), fuell=GELB),
    # Ricarda (links, blickt zu Herrn Kortmann)
    *fig("RI", AX, BODEN, FH, [("woche", "sorge_r")], bis="ri1", erst="cut"),
    ns("Ricarda", AX, BODEN, "woche", RI_N),
    *redet("RI_redet_r", AX, BODEN, FH, "ri1", "ko1"),
    *fig("RI", AX, BODEN, FH, [("ko1", "staunt_r")], bis="ri2", erst="cut"),
    *redet("RI_redet_r", AX, BODEN, FH, "ri2", "frage"),
    *fig("RI", AX, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    # Herr Kortmann (rechts, blickt zu Ricarda)
    *fig("KO", KX, BODEN, FH, [(beim("woche", "Herrn"), "ruhig")], bis="ko1"),
    ns("Herr Kortmann", KX, BODEN, beim("woche", "Herrn"), KO_N),
    *redet("KO_redet", KX, BODEN, FH, "ko1", "ri2"),
    *fig("KO", KX, BODEN, FH, [("ri2", "denkt"), ("frage", "ruhig")], erst="cut"),
    blase("sprech", 640, 170, "ri1", 760, 220, inhalt=["Ich widerrufe den Kaufvertrag."], textsize=36,
          figur=("RI_redet_r", AX, BODEN, FH), bis="ko1"),
    blase("sprech", 960, 250, "ko1", 1040, 225, inhalt=["Sie sind Anwältin, und geliefert wurde",
                                                      "an Ihre Kanzlei. Für Unternehmer",
                                                      "gibt es kein Widerrufsrecht."], textsize=34,
          figur=("KO_redet", KX, BODEN, FH), bis="ri2"),
    blase("sprech", 720, 190, "ri2", 800, 220, inhalt=["Ich nutze den Laptop aber", "überwiegend privat."], textsize=36,
          figur=("RI_redet_r", AX, BODEN, FH), bis="frage"),
    pl("Ist Ricarda Verbraucherin?", 960, 150, "frage", fill=PINK, size=42, anker="m"),
    pl("Daran hängt ihr Widerrufsrecht.", 960, 245, "frage2", fill=WEISS, size=34, anker="m"),
])


# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
def sachverhalt_106(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_106("sv", [
    "Rechtsanwältin Ricarda hat eine eigene Kanzlei. Im Mai 2026 bestellt sie online bei Herrn Kortmann, der einen "
    "Elektronikhandel im Internet betreibt, einen Laptop für 1.200 Euro: über ihr privates Kundenkonto, Rechnung an ihre "
    "Wohnung, Lieferung an die Kanzlei, weil sie tagsüber dort ist.",
    "Ricarda nutzt den Laptop zu 40 % für die Kanzlei und zu 60 % privat (Filme, Fotos, Urlaubsplanung).",
    "Eine Woche nach der Lieferung widerruft sie den Kaufvertrag per E-Mail. Herr Kortmann lehnt ab: Sie sei Anwältin, "
    "geliefert worden sei an die Kanzlei, und für Unternehmer gebe es kein Widerrufsrecht.",
], "Ist Ricarda Verbraucherin und kann sie widerrufen?")

# C Rechtsfolge: Widerrufsrecht, § 312g Abs. 1 BGB ------------------------------------------------------------------------------
folie([("wr", "Rechtsfolge · Widerrufsrecht, § 312g Abs. 1 BGB"), ("offen", "Rechtsfolge · hängt an § 13 BGB")], rechts_frei([
    *tafel("wr", "Woran es hängt: das Widerrufsrecht"),
    z("§ 312g Abs. 1 BGB: Widerrufsrecht des Verbrauchers", 110, 190, beim("w312", "Paragraf"), "Bold", 36),
    z("bei Fernabsatzverträgen (§ 312c BGB)", 160, 242, beim("w312", "Fernabsatz"), size=34),
    *okz("online bestellt: Fernabsatzvertrag", 320, "fern", "Bold", 34, x=160),
    *okz("Herr Kortmann handelt gewerblich: Unternehmer", 380, beim("fern", "gewerblich"), "Bold", 34, x=160),
    z("Frist: 14 Tage, frühestens ab Erhalt der Ware", 110, 465, "frist", "Bold", 36),
    zit("§ 355 Abs. 2, § 356 Abs. 2 Nr. 1 a, Abs. 3 BGB", 160, 517, beim("frist", "Erhalt")),
    *okz("nach 1 Woche: rechtzeitig", 580, beim("frist", "Nach"), "Bold", 34, x=160),
    blk(110, 680, 1040, 100, GELB, "offen", [("Offen: Ist Ricarda Verbraucherin?", "ExtraBold", 40, INK)]),
    *requisit([("wr", ("tabler", "arrow-back-up", 100, WEISS), "Widerruf?", WEISS),
               ("frist", ("tabler", "calendar-event", 100, WEISS), "14 Tage", WEISS),
               ("offen", ("tabler", "question-mark", 90, WEISS), "Verbraucherin?", GELB)]),
    *paar("wr", "RI", [("wr", "ruhig"), (beim("frist", "Nach"), "froh"), ("offen", "denkt")],
          "KO", [("wr", "ruhig"), ("fern", "denkt")]),
]))

# D § 13 BGB (Wortlaut) ----------------------------------------------------------------------------------------------------------
W13 = ["„Verbraucher ist jede natürliche Person, die ein Rechtsgeschäft zu",
       "Zwecken abschließt, die überwiegend weder ihrer gewerblichen noch",
       "ihrer selbständigen beruflichen Tätigkeit zugerechnet werden",
       "können.“"]
w13, w13_y = wortlaut(80, 165, 1100, W13, "§ 13 BGB", "w13", marken=[
    (0, "natürliche Person", beim("w13", "natürliche")), (0, "Rechtsgeschäft", beim("w13", "Rechtsgeschäft")),
    (1, "überwiegend", beim("w13", "überwiegend")), (1, "gewerblichen", beim("w13", "gewerblichen")),
    (2, "selbständigen beruflichen", beim("w13", "selbständigen"))], size=32)
folie([("w13", "Abgrenzung › Verbraucher, § 13 BGB")], rechts_frei([
    *tafel("w13", "§ 13 BGB: Verbraucher"),
    *w13,
    *okz("1. natürliche Person: Ricarda", w13_y + 40, "mp", "Bold", 36, x=160),
    *okz("2. Rechtsgeschäft: der Kauf", w13_y + 105, "mr", "Bold", 36, x=160),
    blk(110, w13_y + 190, 1040, 100, GELB, "mz", [("3. Entscheidend ist der Zweck", "ExtraBold", 40, INK)]),
    *requisit([("w13", ("tabler", "user", 100, WEISS), "Verbraucher?", WEISS),
               ("mp", ("tabler", "user-check", 100, GRUEN), "natürliche Person", GRUEN),
               ("mr", ("tabler", "receipt", 90, WEISS), "Kauf", WEISS),
               ("mz", ("tabler", "question-mark", 90, WEISS), "Zweck?", GELB)]),
    *paar("w13", "RI", [("w13", "ruhig"), ("mz", "denkt")], "KO", [("w13", "ruhig")]),
]))

# E § 14 Abs. 1 BGB (Wortlaut), Anwältin: freier Beruf, aber selbständig beruflich -------------------------------------------------
W14 = ["„Unternehmer ist eine natürliche oder juristische Person oder eine",
       "rechtsfähige Personengesellschaft, die bei Abschluss eines Rechts-",
       "geschäfts in Ausübung ihrer gewerblichen oder selbständigen",
       "beruflichen Tätigkeit handelt.“"]
w14, w14_y = wortlaut(80, 165, 1100, W14, "§ 14 Abs. 1 BGB", "w14", marken=[
    (2, "in Ausübung", beim("w14", "Ausübung")), (2, "gewerblichen", beim("w14", "gewerblichen")),
    (2, "selbständigen", beim("w14", "selbständigen"))], size=32)
folie([("w14", "Abgrenzung › Unternehmer, § 14 Abs. 1 BGB"), ("frei", "Unternehmer › Anwältin: freier Beruf")], rechts_frei([
    *tafel("w14", "§ 14 Abs. 1 BGB: Unternehmer"),
    *w14,
    *neinz("kein Gewerbe: Anwältin übt freien Beruf aus", w14_y + 40, "frei", "Bold", 34, x=160),
    zit("§ 2 Abs. 1, 2 BRAO", 160, w14_y + 92, beim("frei", "freien")),
    *okz("aber selbständig beruflich: eigene Kanzlei", w14_y + 150, "selb", "Bold", 34, x=160),
    blk(110, w14_y + 235, 1040, 150, GRUEN, "rolle", [("Nicht der Beruf entscheidet,", "ExtraBold", 38, INK),
                                                    ("sondern der Zweck des Geschäfts", "ExtraBold", 38, INK)]),
    *requisit([("w14", ("tabler", "building-store", 110, BLAU), "Unternehmer", WEISS),
               ("frei", ("tabler", "briefcase", 110, GELB), "freier Beruf", WEISS),
               ("selb", ("tabler", "id-badge", 90, WEISS), "selbständig", GRUEN),
               ("rolle", ("tabler", "question-mark", 90, WEISS), "Zweck?", GRUEN)]),
    *paar("w14", "RI", [("w14", "ruhig"), ("selb", "denkt"), ("rolle", "froh")], "KO", [("w14", "froh"), ("frei", "ruhig")]),
]))

# F Dual Use: überwiegender Zweck (Waage), Gegenfall -------------------------------------------------------------------------------
WX, WY = 630, 240
folie([("dual", "Abgrenzung › Dual Use: überwiegender Zweck"), ("gegen", "Dual Use › Gegenfall: 60 % Kanzlei")], rechts_frei([
    *tafel("dual", "Gemischte Nutzung: Dual Use"),
    waage(WX, WY, 0, ["Kanzlei"], ["privat"], "dual", bis="sub"),
    waage(WX, WY, 9, ["Kanzlei", "40 %"], ["privat", "60 %"], "sub", bis="gegen", rf=PINK),
    waage(WX, WY, -9, ["Kanzlei", "60 %"], ["privat", "40 %"], "gegen", lf=GELB),
    z("seit 13.6.2014 in § 13 BGB: „überwiegend“", 110, 545, "ueberw", "Bold", 36),
    zit("Gesetz v. 20.9.2013, BGBl. I S. 3642", 160, 597, beim("ueberw", "überwiegend")),
    z("doppelter Zweck: Es zählt der überwiegende Zweck", 110, 650, "begr", "Bold", 34),
    zit("BT-Drs. 17/13951, S. 61; Erwägungsgrund 17 RL 2011/83/EU", 160, 700, beim("begr", "doppeltem")),
    *okz("Ricarda: 60 % privat, der private Zweck überwiegt", 755, "sub", "Bold", 34, x=160),
    z("Gegenfall: 60 % Kanzlei, dann Unternehmerin", 110, 825, "gegen", "Bold", 34),
    *requisit([("dual", ("tabler", "scale", 110, WEISS), "Dual Use", WEISS),
               ("sub", ("tabler", "user-check", 100, GRUEN), "Verbraucherin", GRUEN),
               ("gegen", ("tabler", "briefcase", 110, GELB), "Unternehmerin", GELB)]),
    *paar("dual", "RI", [("dual", "ruhig"), ("sub", "froh"), ("gegen", "sorge")], "KO", [("dual", "ruhig"), ("sub", "sorge"),
                                                                                       ("gegen", "froh")]),
]))

# G strengere EuGH-Linie (Gruber) ------------------------------------------------------------------------------------------------------
folie([("gruber", "Dual Use › strengere EuGH-Linie (Gruber)"), ("nat", "Dual Use › § 13 BGB: das Überwiegen zählt")], rechts_frei([
    *tafel("gruber", "Strenger: EuGH im Zuständigkeitsrecht"),
    z("Urteil Gruber:", 110, 190, beim("gruber", "Urteil"), "Bold", 38),
    zit("EuGH, Urt. v. 20.1.2005 – C-464/01, Rn. 39, 41, 54", 160, 245, beim("gruber", "Urteil")),
    *neinz("Überwiegen des privaten Zwecks genügt nicht", 320, beim("gruber", "genügt"), "Bold", 36, x=160),
    z("beruflicher Zweck muss ganz untergeordnet sein", 160, 390, beim("gruber", "berufliche"), "Bold", 36),
    blk(110, 500, 1040, 100, GRUEN, "nat", [("§ 13 BGB: Es zählt das Überwiegen", "ExtraBold", 40, INK)]),
    *requisit([("gruber", ("tabler", "gavel", 110, WEISS), "EuGH: strenger", WEISS),
               ("nat", ("tabler", "scale", 110, WEISS), "§ 13 BGB: überwiegend", GRUEN)]),
    *paar("gruber", "RI", [("gruber", "sorge"), ("nat", "froh")], "KO", [("gruber", "denkt")]),
]))

# H Zweck und erkennbare Umstände (BGH) -------------------------------------------------------------------------------------------------
folie([("erk", "Abgrenzung › erkennbare Umstände")], rechts_frei([
    *tafel("erk", "Zweck und erkennbare Umstände"),
    z("Händler kennt den Zweck nicht?", 110, 190, "erk", "Bold", 38),
    z("maßgeblich: grundsätzlich der objektiv verfolgte Zweck", 110, 265, "obj", "Bold", 34),
    zit("BGH, Urt. v. 7.4.2021 – VIII ZR 191/19, Rn. 16", 160, 315, beim("obj", "Zweck")),
    z("natürliche Person: grundsätzlich Verbraucherhandeln", 110, 390, beim("zweif", "Handeln"), "Bold", 34),
    z("Zweifel gehen nicht zu ihren Lasten", 160, 442, beim("zweif", "Zweifel"), size=34),
    zit("BGH, Urt. v. 30.9.2009 – VIII ZR 7/09, Rn. 10 f.", 160, 494, beim("zweif", "Zweifel")),
    blk(110, 570, 1040, 150, GELB, "eind", [("Anders nur bei eindeutigen, für den", "ExtraBold", 36, INK),
                                          ("Vertragspartner erkennbaren Umständen", "ExtraBold", 36, INK)]),
    zit("BGH, Urt. v. 7.4.2021 – VIII ZR 49/19, Rn. 84", 160, 740, beim("eind", "hinweisen")),
    *requisit([("erk", ("tabler", "question-mark", 90, WEISS), "Zweck?", WEISS),
               ("zweif", ("tabler", "user-check", 100, GRUEN), "im Zweifel Verbraucher", GRUEN),
               ("eind", ("tabler", "eye", 110, WEISS), "erkennbar?", GELB)]),
    *paar("erk", "RI", [("erk", "ruhig"), ("zweif", "froh")], "KO", [("erk", "denkt"), ("eind", "ruhig")]),
]))

# I Lampenfall und Ricarda (Zweispalter) ---------------------------------------------------------------------------------------------------
LS, RS = 150, 690
folie([("lampe", "Erkennbare Umstände › Lampenfall, BGH VIII ZR 7/09"), ("hier", "Erkennbare Umstände › Ricarda")], rechts_frei([
    *tafel("lampe", "Lampenfall und Ricarda"),
    zit("BGH, Urt. v. 30.9.2009 – VIII ZR 7/09, Rn. 12", 110, 168, "lampe"),
    z("Lampenfall", LS - 40, 225, "lampe", "ExtraBold", 38),
    linienzug([(640, 230), (640, 600)], "lampe", breite=4),
    z("Rechtsanwältin", LS, 295, beim("lampe", "Rechtsanwältin"), size=34, rechts=625),
    z("Lampen für die Wohnung", LS, 350, beim("lampe", "Wohnung"), size=34, rechts=625),
    z("Lieferung an die Kanzlei", LS, 405, beim("lampe", "Kanzlei"), size=34, rechts=625),
    *okz("Verbraucherin", 490, "lampe2", "Bold", 36, x=LS + 40, rechts=625),
    z("Ricarda", RS - 40, 225, "hier", "ExtraBold", 38),
    z("Lieferadresse: Kanzlei", RS, 295, beim("hier", "Lieferadresse"), size=34),
    z("Kundenkonto: privat", RS, 350, beim("hier", "Kundenkonto"), size=34),
    z("Rechnung: Wohnung", RS, 405, beim("hier", "Rechnung"), size=34),
    *neinz("nicht eindeutig", 490, beim("hier", "nicht"), "Bold", 36, x=RS + 40),
    linienzug([(110, 620), (1150, 620)], "bew", breite=3),
    z("Beweislast für den privaten Zweck: Ricarda", 110, 650, "bew", "Bold", 36),
    zit("BGH, Urt. v. 30.9.2009 – VIII ZR 7/09, Rn. 11", 160, 705, beim("bew", "beweisen")),
    *requisit([("lampe", ("tabler", "lamp", 100, GELB), "Lampenfall", WEISS),
               ("lampe2", ("tabler", "user-check", 100, GRUEN), "Verbraucherin", GRUEN),
               ("hier", ("tabler", "truck-delivery", 120, WEISS), "nur Lieferadresse", WEISS),
               ("bew", ("tabler", "scale", 110, WEISS), "Beweislast", WEISS)]),
    *paar("lampe", "RI", [("lampe", "ruhig"), ("hier", "froh"), ("bew", "denkt")], "KO", [("lampe", "ruhig"), ("hier", "sorge")]),
]))

# J Ergebnis ---------------------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Ricarda ist Verbraucherin")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 150, GRUEN, "erg", [("Ricarda ist Verbraucherin,", "ExtraBold", 40, INK),
                                          ("ihr Widerruf ist wirksam", "ExtraBold", 40, INK)]),
    zit("§§ 13, 312g Abs. 1, 355 Abs. 1 BGB", 160, 360, beim("erg", "Widerruf")),
    z("Rückgewähr spätestens nach 14 Tagen:", 110, 440, "erg2", "Bold", 36),
    zit("§ 355 Abs. 3, § 357 Abs. 1 BGB", 160, 492, beim("erg2", "spätestens")),
    *okz("Ricarda: den Laptop", 560, beim("erg3", "Ricarda"), "Bold", 36, x=160),
    *okz("Herr Kortmann: die 1.200 €", 625, beim("erg3", "Herr"), "Bold", 36, x=160),
    *requisit([("erg", ("tabler", "user-check", 100, GRUEN), "Verbraucherin", GRUEN),
               (beim("erg3", "Ricarda"), ("tabler", "package", 110, GELB), "Laptop zurück", WEISS),
               (beim("erg3", "Herr"), ("tabler", "cash", 110, GRUEN), "1.200 € zurück", GRUEN)]),
    *paar("erg", "RI", [("erg", "froh")], "KO", [("erg", "sorge")]),
]))

# K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Kanzleiadresse allein reicht nicht")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Kanzleiadresse: nicht täuschen lassen", 200, 200, beim("tipp", "Lass"), "Bold", 38),
    z("Lieferung an die Kanzlei oder Zahlung vom", 200, 265, beim("tipp", "Eine"), size=34),
    z("Geschäftskonto allein: kein Unternehmer", 200, 317, beim("tipp", "Geschäftskonto"), "Bold", 34),
    zit("BGH, Urt. v. 30.9.2009 – VIII ZR 7/09, Rn. 12;", 200, 375, beim("tipp", "Unternehmer")),
    zit("BGH, Urt. v. 7.4.2021 – VIII ZR 191/19, Rn. 21", 200, 412, beim("tipp", "Unternehmer")),
    z("1. objektiver Zweck", 200, 490, beim("tipp2", "objektiven"), "Bold", 36),
    z("2. eindeutige Umstände dagegen?", 200, 550, beim("tipp2", "eindeutige"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# L Klausurschema ---------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k3", "Klausurschema › III. Zweck"), ("k4", "Klausurschema › IV. erkennbare Umstände"),
       ("k5", "Klausurschema › sonst Unternehmer, § 14 BGB")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Verbraucher, § 13 BGB"), 110, 90, "sch", 46),
    z("I. natürliche Person", K1, 190, "k1", "Bold", 40, rechts=1820),
    z("II. Rechtsgeschäft", K1, 260, "k2", "Bold", 40, rechts=1820),
    z("III. Zweck", K1, 330, "k3", "Bold", 40, rechts=1820),
    z("gemischte Nutzung: überwiegender Zweck", K2, 382, beim("k3", "gemischter"), size=36, rechts=1820),
    z("IV. keine eindeutigen Umstände für berufliches Handeln", K1, 450, "k4", "Bold", 40, rechts=1820),
    z("im Zweifel Verbraucher", K2, 502, beim("k4", "Zweifel"), size=36, rechts=1820),
    linienzug([(110, 580), (1810, 580)], "k5", breite=3),
    z("Scheitert die Verbrauchereigenschaft: Unternehmer nach § 14 BGB prüfen", K1, 610, "k5", "Bold", 38, rechts=1820),
])

# M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Es zählt der ", 0), ("überwiegende Zweck", "a")], [("des Geschäfts, nicht der Beruf.", 0)]],
                750, 320, 46, "merke", {"a": beim("merke", "überwiegende")}),
    *markertext([[("Und im Zweifel handelt eine", 0)], [("natürliche Person als ", 0), ("Verbraucher.", "c")]],
                750, 560, 46, "mz2", {"c": beim("mz2", "Verbraucher")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
