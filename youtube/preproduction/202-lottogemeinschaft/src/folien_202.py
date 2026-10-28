"""Folge 202 · Tippgemeinschaft ohne Tippschein: Gefälligkeitsverhältnis und Haftung – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall nach BGH, Urt. v. 16.5.1974 – II ZR 12/73, NJW 1974, 1705: Gerold gibt für die Tipprunde (Erna, Ulf) jede Woche
ohne Entgelt den Lottoschein ab, vergisst ihn einmal; mit ihren Zahlen hätte die Runde 12.000 € gewonnen. Szenen laut ../SZENENPLAN.md.
DARSTELLUNG: neutraler „Lottoschein“ ohne Lotterie-Marke oder Logo (Schein aus Grundformen), kein Glücksspiel-Werbeton.
Zwei Handlungsgeräusche (Münzen beim Einsammeln, Tastatur, als Gerold am Samstag arbeitet; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 199 (gemeinsame Dateien unverändert); neu: tisch(), lottoschein(), kugeln().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_202/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_202/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe;
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




def pkt(text, y, cue, stil="Regular", size=34, x=185, **k):
    """Tafelzeile mit Aufzählungspunkt (Kriterium oder Argument, keine Bewertung)."""
    return [z("•", x - 38, y, cue, "ExtraBold", size), z(text, x, y, cue, stil, size, **k)]



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HI": "Gerold", "EN": "Erna", "UL": "Ulf"}
NFARBE = {"HI": GRUEN, "EN": GELB, "UL": BLAU}


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


def zwei(k1, folge1, k2, folge2):
    """Zwei Figuren neben der Tafel, beide blicken nach links zur Tafel."""
    return [*stehend(k1, X1, folge1), *stehend(k2, X2, folge2)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
HELLGRAU_ = (226, 226, 222, 255)
HOLZ_D = (190, 135, 90, 255)
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


def tisch(x0, x1, y, unten, c, fill=HOLZ):
    """Schreibtisch bzw. Küchenzeile in Seitenansicht: Platte und zwei Beine bzw. geschlossener Unterschrank."""
    w, h = x1 - x0, unten - y
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, 30), 8, fill=fill, outline=INK, width=5)
    for sx in (30, w - 60):
        dr.rectangle((sx, 28, sx + 30, h - 1), fill=HOLZ_D, outline=INK, width=5)
    return El(im, x0, y, c, "cut", 0.0, None, name="tisch")


def zeile_kueche(x0, x1, y, unten, c):
    """Küchenzeile: Arbeitsplatte mit Unterschrank und zwei Türen (Grundformen)."""
    w, h = x1 - x0, unten - y
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rectangle((10, 26, w - 11, h - 1), fill=(240, 236, 228, 255), outline=INK, width=5)
    dr.line((w // 2, 26, w // 2, h - 1), fill=INK, width=5)
    for gx in (w // 2 - 40, w // 2 + 26):
        dr.rounded_rectangle((gx, 70, gx + 14, 130), 6, fill=INK)
    dr.rounded_rectangle((0, 0, w - 1, 30), 8, fill=HOLZ, outline=INK, width=5)
    return El(im, x0, y, c, "cut", 0.0, None, name="kueche")


def lottoschein(x, y, w, c, d=0.0, bis=None):
    """Neutraler Lottoschein ohne Marke: weiße Karte mit vier Tippfeldern (Raster) und sechs markierten Feldern im ersten Tipp."""
    s = 2
    h = int(w * 1.25)
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), 12 * s, fill=WEISS, outline=INK, width=4 * s)
    dr.rectangle((4 * s, 18 * s, (w - 4) * s, 34 * s), fill=ROT)
    feld = (w - 36) // 2
    zelle = feld / 7
    markiert = {(0, 3), (1, 1), (2, 2), (3, 5), (4, 3), (5, 6)}
    for fi in range(4):
        fx = 12 + (fi % 2) * (feld + 12)
        fy = 46 + (fi // 2) * (feld + 12)
        for r in range(7):
            for k in range(7):
                x0_, y0_ = fx + k * zelle, fy + r * zelle
                q = (x0_ * s + 1, y0_ * s + 1, (x0_ + zelle) * s - 1, (y0_ + zelle) * s - 1)
                if fi == 0 and (r, k) in markiert:
                    dr.ellipse(q, fill=INK)
                else:
                    dr.rectangle(q, outline=(150, 150, 150, 255), width=s)
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x, y, c, "pop", d, bis, name="lottoschein")


def kugeln(cx, cy, zahlen, r, c, d=0.0, bis=None):
    """Gezogene Zahlen als Kugeln (Grundformen), Ziffern in Nunito."""
    s = 2
    n = len(zahlen)
    w = n * (2 * r + 14)
    im = Image.new("RGBA", (w * s, (2 * r + 8) * s))
    dr = ImageDraw.Draw(im)
    f = F("ExtraBold", int(r * 1.0 * s))
    for i, zl in enumerate(zahlen):
        x0_ = (i * (2 * r + 14) + 4) * s
        dr.ellipse((x0_, 4 * s, x0_ + 2 * r * s, (4 + 2 * r) * s), fill=GELB, outline=INK, width=4 * s)
        t = str(zl); b = f.getbbox(t)
        dr.text((x0_ + r * s - (b[2] + b[0]) / 2, (4 + r) * s - (b[3] + b[1]) / 2), t, font=f, fill=INK)
    im = im.resize((w, 2 * r + 8), Image.LANCZOS)
    return El(im, cx - w / 2, cy - r, c, "pop", d, bis, name="kugeln")


ZAHLEN = (4, 9, 17, 23, 31, 42)

# ===========================================================================================================================
# A1 Fall: die Tipprunde im Büro (Hook, Erna, Ulf, Gerold, Einsätze, Lottoschein, Annahmestelle, ohne Entgelt)
# ===========================================================================================================================
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
EX, UX, HX = 930, 1180, 1660                 # Erna, Ulf (blicken nach rechts), Gerold (blickt nach links)
folie([(NULL, "Fall · Die Tipprunde"), ("runde", "Fall · Erna und Ulf"), ("hilmar", "Fall · Gerold spielt mit"),
       ("geld", "Fall · Jede Woche 5 € pro Kopf"), ("schein", "Fall · Gerold gibt den Schein ab"),
       ("gratis", "Fall · ohne Entgelt")], [
    hart(boden_(G0, NULL)),
    hart(tisch(110, 560, 720, G0, NULL)),
    hart(ficon("tabler", "device-laptop", 270, 724, 170, NULL, fuell=HELLBLAU, anim="cut")),
    hart(ficon("tabler", "plant-2", 470, 724, 90, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "clock", 330, 420, 110, NULL, fuell=WEISS, anim="cut")),
    hart(bis_(lottoschein(700, 380, 220, NULL), beim("runde", "Erna"))),
    pl("Tipprunde: hätte gewonnen", 70, 30, beim("fall", "gewonnen"), fill=GELB, size=32),
    pl("Schein vergessen", 70, 100, beim("fall", "vergessen"), fill=HELLROT, size=32),
    *fig("EN", EX, G0, FHA, [(beim("runde", "Erna"), "ruhig_r"), ("geld", "froh_r")]),
    ns("Erna", EX, G0, beim("runde", "Erna"), GELB, d=0.1),
    *fig("UL", UX, G0, FHA, [(beim("runde", "Ulf"), "ruhig_r"), ("geld", "froh_r")]),
    ns("Ulf", UX, G0, beim("runde", "Ulf"), BLAU, d=0.1),
    pl("seit Jahren Lotto", 70, 170, beim("hilmar", "Seit"), fill=WEISS, size=32),
    *fig("HI", HX, G0, FHA, [(beim("hilmar", "Gerold"), "froh"), ("gratis", "ruhig")]),
    ns("Gerold", HX, G0, beim("hilmar", "Gerold"), GRUEN, d=0.1),
    szene(bewegt(ficon("tabler", "coin-euro", 1450, 820, 64, "geld", fuell=GELB), "geld", beim("geld", "Gerold"), -520, -80),
          "202muenzen*", 0.5, 0.0),
    bewegt(ficon("tabler", "coin-euro", 1500, 860, 64, "geld", fuell=GELB), "geld", beim("geld", "Gerold"), -320, -60),
    pl("je 5 € pro Woche", 760, 30, beim("geld", "fünf"), fill=GELB, size=32),
    lottoschein(1370, 400, 160, "schein"),
    pl("feste Zahlen", 1450, 330, beim("schein", "festen"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "building-store", 690, G0 + 4, 170, beim("schein", "Annahmestelle"), fuell=HELLBLAU),
    pl("Annahmestelle", 690, 640, beim("schein", "Annahmestelle"), fill=WEISS, size=28, anker="m"),
    pl("ohne Entgelt", 1690, 330, beim("gratis", "nichts"), fill=GRUEN, size=28, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: der vergessene Samstag (Gerold arbeitet lange, vergisst den Schein, Ziehung am Abend)
# ===========================================================================================================================
HX2 = 680
folie([("samstag", "Fall · Samstag: Gerold arbeitet lange"), ("vergisst", "Fall · Der Schein bleibt liegen"),
       ("ziehung", "Fall · Die Ziehung am Abend")], [
    boden_(G0, "samstag"),
    tisch(110, 560, 720, G0, "samstag"),
    szene(ficon("tabler", "device-laptop", 270, 724, 170, "samstag", fuell=HELLBLAU, anim="cut"), "202tastatur*", 0.45, 0.3),
    ficon("tabler", "plant-2", 470, 724, 90, "samstag", fuell=GRUEN, anim="cut"),
    ficon("tabler", "clock", 330, 420, 110, "samstag", fuell=WEISS, anim="cut"),
    pl("Samstag", 70, 30, beim("samstag", "Samstag"), fill=GELB, size=32),
    pl("lange arbeiten", 330, 470, beim("samstag", "lange"), fill=WEISS, size=28, anker="m"),
    *fig("HI", HX2, G0, FHA, [("samstag", "muede")], erst="cut"),
    ns("Gerold", HX2, G0, "samstag", GRUEN),
    lottoschein(1000, 480, 150, "vergisst"),
    pl("Schein vergessen", 1075, 410, beim("vergisst", "vergisst"), fill=HELLROT, size=28, anker="m"),
    ficon("tabler", "device-tv", 1560, 760, 380, "ziehung", fuell=WEISS),
    pl("Ziehung am Abend", 1560, 380, beim("ziehung", "gezogen"), fill=WEISS, size=30, anker="m"),
    kugeln(1560, 590, ZAHLEN, 30, beim("ziehung", "Zahlen")),
    pl("12.000 € Gewinn – ohne Schein", 1460, 800, beim("ziehung", "zwölftausend"), fill=GELB, size=30, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: Montag in der Teeküche (Erna, Gerold, Ulf reden; die Frage; Leitentscheidung)
# ===========================================================================================================================
EX3, UX3, HX3 = 880, 1140, 1640
folie([("montag", "Fall · Montag in der Teeküche"), ("e1", "Fall · Erna: 12.000 € gewonnen"),
       ("h1", "Fall · Gerold: Schein nicht abgegeben"), ("u1", "Fall · Ulf: je 4.000 €"), ("frage", "Fall · Die Frage"),
       ("bgh", "Fall · Der Lottogemeinschaft-Fall des BGH")], [
    boden_(G0, "montag", fill=(236, 230, 220, 255), h=100),
    zeile_kueche(80, 640, 700, G0, "montag"),
    ficon("tabler", "coffee", 200, 704, 110, "montag", fuell=WEISS, anim="cut"),
    ficon("tabler", "mug", 360, 704, 80, "montag", fuell=ROT, anim="cut"),
    ficon("tabler", "mug", 460, 704, 80, "montag", fuell=BLAU, anim="cut"),
    ficon("tabler", "clock", 560, 480, 100, "montag", fuell=WEISS, anim="cut"),
    pl("Montag", 70, 30, beim("montag", "Montag"), fill=GELB, size=32, bis="frage"),
    *fig("EN", EX3, G0, FHA, [("montag", "freut_r")], bis="e1", erst="cut"),
    *redet("EN_redet_r", EX3, G0, FHA, "e1", "h1"),
    *fig("EN", EX3, G0, FHA, [("h1", "staunt_r"), ("u1", "ernst_r"), ("frage", "denkt_r"), ("bgh", "ruhig_r")], erst="cut"),
    ns("Erna", EX3, G0, "montag", GELB),
    *fig("UL", UX3, G0, FHA, [("montag", "froh_r"), ("h1", "staunt_r")], bis="u1", erst="cut"),
    *redet("UL_redet_r", UX3, G0, FHA, "u1", "frage"),
    *fig("UL", UX3, G0, FHA, [("frage", "ernst_r"), ("bgh", "ruhig_r")], erst="cut"),
    ns("Ulf", UX3, G0, "montag", BLAU),
    *fig("HI", HX3, G0, FHA, [("montag", "sorge")], bis="h1", erst="cut"),
    *redet("HI_klagt", HX3, G0, FHA, "h1", "u1"),
    *fig("HI", HX3, G0, FHA, [("u1", "still"), ("bgh", "ruhig")], erst="cut"),
    ns("Gerold", HX3, G0, "montag", GRUEN),
    blase("sprech", 980, 220, "e1", 1180, 240, inhalt=["Gerold, mit unseren Zahlen", "hätten wir 12.000 € gewonnen!"],
          textsize=34, figur=("EN_redet_r", EX3, G0, FHA), bis="h1"),
    blase("sprech", 1060, 230, "h1", 1180, 240, inhalt=["Ich weiß. Ich habe den Schein diesmal", "nicht abgegeben. Es tut mir leid."],
          textsize=34, figur=("HI_klagt", HX3, G0, FHA), bis="u1"),
    blase("sprech", 900, 220, "u1", 1300, 240, inhalt=["Dann schuldest du Erna", "und mir je 4.000 €."],
          textsize=34, figur=("UL_redet_r", UX3, G0, FHA), bis="frage"),
    pl("Muss Gerold den entgangenen Gewinn ersetzen?", 70, 100, "frage", fill=PINK, size=32),
    pl("Oder nur eine Gefälligkeit?", 70, 170, "frage2", fill=PINK, size=32),
    pl("BGH, Urt. v. 16.5.1974 – II ZR 12/73", 70, 240, beim("bgh", "neunzehnhundert"), fill=GELB, size=32),
    zit("NJW 1974, 1705", 80, 308, beim("bgh", "neunzehnhundert")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_202(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_202("sv", [
    "Erna, Ulf und Gerold sind Kollegen und spielen seit Jahren als Tipprunde Lotto. Jede Woche zahlt jeder 5 € an Gerold. "
    "Gerold füllt den Lottoschein mit ihren festen Zahlen aus und gibt ihn in der Annahmestelle ab. Dafür bekommt er nichts.",
    "An einem Samstag muss Gerold lange arbeiten und vergisst den Schein. Am Abend wird gezogen: Mit ihren Zahlen hätte die "
    "Runde 12.000 € gewonnen.",
    "Am Montag sagt Gerold: „Ich habe den Schein diesmal nicht abgegeben.“ Ulf verlangt: „Dann schuldest du Erna und mir "
    "je 4.000 €.“",
], "Muss Gerold den entgangenen Gewinn ersetzen?")

# ===========================================================================================================================
# C Anspruch: §§ 280 Abs. 1, 241 Abs. 1 BGB – Schuldverhältnis? (Wortlautkarte § 241 Abs. 1 Satz 1)
# ===========================================================================================================================
W241 = umbruch("„Kraft des Schuldverhältnisses ist der Gläubiger berechtigt, von dem Schuldner eine Leistung zu fordern.“", 32, 1040)
_z41 = lambda wort: next(i for i, t in enumerate(W241) if wort in t)
w241, w241_y = wortlaut(80, 300, 1100, W241, "§ 241 Abs. 1 Satz 1 BGB", beim("p241", "Paragraf"),
                        marken=[(_z41("Schuldverhältnisses"), "Schuldverhältnisses", beim("p241", "Schuldverhältnisses")),
                                (_z41("Leistung"), "Leistung", beim("p241", "Leistung"))], size=32)
PC = "Anspruch: § 280 Abs. 1 BGB"
folie([("ansp", PC), ("pfl", f"{PC} › Pflicht aus einem Schuldverhältnis"),
       ("p241", f"{PC} › Schuldverhältnis, § 241 Abs. 1 BGB"), ("frage3", f"{PC} › Pflicht zum Einreichen?")], rechts_frei([
    *tafel("ansp", "Schadensersatz für Erna und Ulf?"),
    z("Erna und Ulf: Schadensersatz aus § 280 Abs. 1 BGB", 110, 180, "ansp", "Bold", 32),
    z("Voraussetzung: Gerold hat eine Pflicht aus", 110, 228, "pfl", "Bold", 32),
    z("einem Schuldverhältnis verletzt", 110, 272, beim("pfl", "einem"), "Bold", 32),
    *w241,
    blk(110, w241_y + 40, 1040, 90, PINK, "frage3", [("Schuldete Gerold das Einreichen des Scheins?", "ExtraBold", 33, INK)]),
    *requisit([("ansp", ("tabler", "coin-euro", 110, GELB), "je 4.000 €", GELB),
               ("pfl", ("tabler", "scale", 120, WEISS), "Pflicht verletzt?", WEISS),
               ("frage3", ("tabler", "ticket", 120, ROT), "Einreichen geschuldet?", PINK)]),
    *zwei("EN", [("ansp", "ernst"), ("p241", "ruhig"), ("frage3", "denkt")], "HI", [("ansp", "sorge"), ("frage3", "denkt")]),
]))
assert w241_y + 150 <= 930, w241_y

# ===========================================================================================================================
# D Rechtsbindungswille oder Gefälligkeit (Kriterien, BGH III ZR 346/14 Rn. 8)
# ===========================================================================================================================
PD = "Schuldverhältnis? › Rechtsbindungswille"
folie([("rbw", PD), ("gef", f"{PD} › bloßer Gefallen: keine Rechtspflicht"), ("obj", f"{PD} › objektiver Beobachter"),
       ("wirt", f"{PD} › wirtschaftliche Interessen, Verlass"), ("eigen", f"{PD} › eigenes Interesse des Helfers"),
       ("alltag", f"{PD} › Gefälligkeit des täglichen Lebens")], rechts_frei([
    *tafel("rbw", "Vertrag oder Gefälligkeit?"),
    z("Rechtsbindungswille – wie beim Angebot (§ 145 BGB)", 110, 180, "rbw", "Bold", 32),
    z("Nur ein Gefallen: keine Rechtspflicht", 110, 236, "gef", "Bold", 32),
    blk(110, 300, 1040, 130, HELLBLAU, "obj", [("Maßstab: objektiver Beobachter,", "Bold", 31, INK),
                                            ("Treu und Glauben, Verkehrssitte", "ExtraBold", 32, INK)]),
    z("Für eine Bindung spricht:", 110, 460, "wirt", "Bold", 32),
    *pkt("wesentliche wirtschaftliche Interessen des", 515, "wirt", "Regular", 31, x=160),
    z("anderen, er verlässt sich auf die Zusage", 160, 558, beim("wirt", "verlässt"), size=31),
    *pkt("eigenes rechtliches oder wirtschaftliches", 620, "eigen", "Regular", 31, x=160),
    z("Interesse des Helfers", 160, 663, beim("eigen", "Interesse"), size=31),
    blk(110, 725, 1040, 120, GELB, "alltag", [("Gefälligkeit des täglichen Lebens:", "Bold", 31, INK),
                                           ("in der Regel kein Bindungswille", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 23.7.2015 – III ZR 346/14, Rn. 8", 110, 855, "alltag"),
    *requisit([("rbw", ("tabler", "file-certificate", 110, WEISS), "Rechtsbindungswille?", WEISS),
               ("gef", ("tabler", "heart-handshake", 120, PINK), "Gefallen", PINK),
               ("obj", ("tabler", "eye", 120, HELLBLAU), "objektiver Beobachter", HELLBLAU),
               ("wirt", ("tabler", "coin-euro", 110, GELB), "wirtschaftliche Interessen", GELB),
               ("eigen", ("tabler", "briefcase", 120, HOLZ), "eigenes Interesse", WEISS),
               ("alltag", ("tabler", "coffee", 110, WEISS), "Alltag", GELB)]),
    *zwei("UL", [("rbw", "ruhig"), ("gef", "denkt"), ("alltag", "ruhig")], "HI", [("rbw", "ruhig"), ("wirt", "denkt"), ("alltag", "froh")]),
]))

# ===========================================================================================================================
# E1 Der Fall des BGH: Sachverhalt, § 762 BGB (Oberlandesgericht) und § 763 BGB
# ===========================================================================================================================
PE = "BGH, 16.5.1974 – II ZR 12/73"
folie([("urteil", f"{PE} › der Fall"), ("olg", f"{PE} › Oberlandesgericht: § 762 BGB"),
       ("neben", f"{PE} › Einreichen: Nebengeschäft"), ("p763", f"{PE} › staatlich genehmigt, § 763 BGB")], rechts_frei([
    *tafel("urteil", "Der Fall des BGH"),
    z("Mitspieler füllt die Scheine vor einer Ziehung", 110, 180, beim("urteil", "Mitspieler"), "Bold", 32),
    z("nicht wie verabredet aus", 110, 224, beim("urteil", "nicht"), "Bold", 32),
    z("Der Runde entgehen 10.550 DM", 110, 282, "dm", "Bold", 32),
    zit("BGH, Urt. v. 16.5.1974 – II ZR 12/73, NJW 1974, 1705", 110, 330, "dm"),
    blk(110, 385, 1040, 130, HELLBLAU, "olg", [("Oberlandesgericht: § 762 BGB –", "Bold", 31, INK),
                                            ("durch Spiel keine Verbindlichkeit", "ExtraBold", 32, INK)]),
    *neinz("BGH: Einreichen ist kein Spiel,", 555, "neben", "Bold", 32, x=160),
    z("sondern ein Nebengeschäft", 160, 600, beim("neben", "sondern"), "Bold", 32),
    blk(110, 665, 1040, 130, GRUEN, "p763", [("staatlich genehmigte Lotterie:", "Bold", 31, INK),
                                          ("verbindlich, § 763 Satz 1 BGB", "ExtraBold", 32, INK)]),
    ficon("tabler", "ticket", 1560, 360, 170, "urteil", fuell=ROT),
    pl("Scheine nicht ausgefüllt", 1560, 400, beim("urteil", "nicht"), fill=WEISS, size=28, anker="m"),
    pl("10.550 DM", 1560, 470, "dm", fill=GELB, size=30, anker="m"),
    ficon("tabler", "dice-5", 1440, 690, 110, "olg", fuell=LILA, bis="p763"),
    pl("Spiel?", 1440, 720, "olg", fill=LILA, size=28, anker="m", bis="p763"),
    ficon("tabler", "building-bank", 1690, 690, 120, "p763", fuell=HELLBLAU),
    pl("staatlich genehmigt", 1600, 720, "p763", fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "gavel", 1560, 900, 120, "neben", fuell=HOLZ),
]))

# ===========================================================================================================================
# E2 Der Fall des BGH: was bindet, was nicht (Leitsatz)
# ===========================================================================================================================
PE2 = "Lottogemeinschaft: was bindet?"
folie([("bind", PE2), ("verteil", f"{PE2} › Gewinn verteilen"), ("einsatz", f"{PE2} › Einsätze"),
       ("gbr", f"{PE2} › GbR? offengelassen"), ("kern", f"{PE2} › entscheidend"),
       ("lsatz", f"{PE2} › Einreichen: keine Verpflichtung")], rechts_frei([
    *tafel("bind", "Was bindet die Tipprunde?"),
    z("Rechtlich gebunden sind die Mitspieler:", 110, 180, "bind", "Bold", 32),
    *okz("Gewinn wie verabredet verteilen", 240, "verteil", "Regular", 32, x=160),
    *okz("versprochene Einsätze: können geschuldet sein", 300, "einsatz", "Regular", 32, x=160),
    z("Gesellschaft bürgerlichen Rechts? Vom BGH offengelassen", 110, 375, "gbr", "Bold", 30),
    zit("§ 705 BGB, heute in der Fassung seit 1.1.2024 (MoPeG)", 110, 420, "gbr"),
    z("Entscheidend war etwas anderes:", 110, 490, "kern", "Bold", 32),
    blk(110, 550, 1040, 200, GRUEN, "lsatz", [("Wer die Scheine ausfüllt und einreicht,", "Bold", 32, INK),
                                           ("übernimmt insoweit in der Regel keine", "ExtraBold", 33, INK),
                                           ("rechtsgeschäftliche Verpflichtung", "ExtraBold", 33, INK)]),
    zit("BGH, NJW 1974, 1705 (Leitsatz)", 110, 765, "lsatz"),
    *requisit([("bind", ("tabler", "users", 120, LILA), "Tipprunde", WEISS),
               ("verteil", ("tabler", "coin-euro", 110, GELB), "Gewinn verteilen", GRUEN),
               ("gbr", ("tabler", "question-mark", 90, None), "GbR: offen", WEISS),
               ("lsatz", ("tabler", "ticket", 120, ROT), "Einreichen: keine Pflicht", GRUEN)]),
    *zwei("EN", [("bind", "ruhig"), ("verteil", "froh"), ("lsatz", "staunt")], "HI", [("bind", "ruhig"), ("gbr", "denkt"), ("lsatz", "froh")]),
]))

# ===========================================================================================================================
# F1 Die Gründe: Interessenabwägung
# ===========================================================================================================================
PF = "Rechtsbindungswille › Gründe des BGH"
folie([("warum", PF), ("fehler", f"{PF} › Fehler passiert leicht"), ("hoch", f"{PF} › Schaden selten, aber hoch"),
       ("exist", f"{PF} › bis zur Existenzvernichtung"), ("unentg", f"{PF} › ohne Entgelt"),
       ("glueck", f"{PF} › Lottogewinn: Glücksfall"), ("gemein", f"{PF} › gemeinsames Spiel"),
       ("niemand", f"{PF} › niemand übernimmt dieses Risiko")], rechts_frei([
    *tafel("warum", "Warum keine Pflicht?"),
    z("Abwägung: die Interessen beider Seiten", 110, 180, beim("warum", "Der"), "Bold", 32),
    *pkt("Fehler passiert leicht: vergessen, keine Zeit,", 245, "fehler", "Regular", 31, x=160),
    z("falsche Zahlen angekreuzt", 160, 288, beim("fehler", "kreuzt"), size=31),
    *pkt("Schaden selten, aber außergewöhnlich hoch", 350, "hoch", "Regular", 31, x=160),
    z("bis zur Vernichtung der wirtschaftlichen Existenz", 160, 393, "exist", "Bold", 31),
    *pkt("und das für eine Aufgabe ohne Entgelt", 455, "unentg", "Regular", 31, x=160),
    *pkt("Lottogewinn: kein normaler Gewinn wie ein", 517, "glueck", "Regular", 31, x=160),
    z("Arbeitslohn, sondern ein Glücksfall", 160, 560, beim("glueck", "sondern"), size=31),
    *pkt("gemeinsames Spiel: Spannung und Chance teilen,", 622, "gemein", "Regular", 31, x=160),
    z("nicht ein Haftungsrisiko", 160, 665, beim("gemein", "nicht"), size=31),
    blk(110, 730, 1040, 110, PINK, "niemand", [("Niemand würde dieses Risiko übernehmen", "ExtraBold", 32, INK),
                                            ("oder einem Mitspieler zumuten", "Bold", 31, INK)]),
    zit("BGH, NJW 1974, 1705, 1706", 110, 852, "niemand"),
    *requisit([("warum", ("tabler", "scale", 120, WEISS), "Interessen abwägen", WEISS),
               ("fehler", ("tabler", "alarm", 110, ROT), "vergessen", HELLROT),
               ("hoch", ("tabler", "moneybag", 110, GELB), "Schaden: selten, aber hoch", GELB),
               ("exist", ("tabler", "home-off", 110, HELLROT), "Existenz in Gefahr", HELLROT),
               ("unentg", ("tabler", "heart-handshake", 120, PINK), "ohne Entgelt", GRUEN),
               ("glueck", ("tabler", "clover", 110, GRUEN), "Glücksfall", GRUEN),
               ("gemein", ("tabler", "users", 120, LILA), "gemeinsam spielen", LILA)]),
    *zwei("UL", [("warum", "ruhig"), ("hoch", "staunt"), ("glueck", "denkt"), ("niemand", "ernst")],
          "HI", [("warum", "ruhig"), ("fehler", "sorge"), ("exist", "schreck"), ("unentg", "ruhig"), ("niemand", "froh")]),
]))

# ===========================================================================================================================
# F2 Anders bei Entgelt; besondere Vereinbarung; Ergebnis für Gerold
# ===========================================================================================================================
PF2 = "Rechtsbindungswille › Ausnahmen"
folie([("anders", PF2 + " › Entgelt, geschäftliche Zwecke"), ("verein", PF2 + " › besondere Vereinbarung"),
       ("erg", "Ergebnis · keine Pflicht, keine Pflichtverletzung")], rechts_frei([
    *tafel("anders", "Anders, wenn …"),
    blk(110, 180, 1040, 170, LILA, "anders", [("… der Beauftragte ein Entgelt bekommt", "Bold", 32, INK),
                                           ("(wie eine Annahmestelle) oder", "Regular", 31, INK),
                                           ("geschäftliche Zwecke im Vordergrund stehen", "Bold", 32, INK)]),
    z("Sonst nötig: eine besondere Vereinbarung", 110, 390, "verein", "Bold", 32),
    zit("BGH, NJW 1974, 1705, 1706", 110, 438, "verein"),
    blk(110, 520, 1040, 170, GRUEN, "erg", [("Gerold:", "Bold", 32, INK), ("keine Pflicht zum Einreichen,", "ExtraBold", 33, INK),
                                         ("also keine Pflichtverletzung", "ExtraBold", 33, INK)]),
    *neinz("Anspruch aus § 280 Abs. 1 BGB", 730, beim("erg", "also"), "Bold", 32, x=160),
    *requisit([("anders", ("tabler", "building-store", 140, HELLBLAU), "Annahmestelle: Entgelt", LILA),
               ("verein", ("tabler", "file-certificate", 110, WEISS), "besondere Vereinbarung", WEISS),
               ("erg", ("tabler", "ticket-off", 120, WEISS), "keine Pflichtverletzung", GRUEN)]),
    *zwei("HI", [("anders", "ruhig"), ("erg", "froh")], "EN", [("anders", "denkt"), ("erg", "sorge")]),
]))

# ===========================================================================================================================
# G1 Deliktsrecht: § 823 Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W823 = umbruch("„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein "
               "sonstiges Recht eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden "
               "Schadens verpflichtet.“", 32, 1040)
_z23 = lambda wort: next(i for i, t in enumerate(W823) if wort in t)
w823, w823_y = wortlaut(80, 180, 1100, W823, "§ 823 Abs. 1 BGB", "w823",
                        marken=[(_z23(w), w, beim("w823", s)) for w, s in
                                (("Leben", "Leben"), ("Körper", "Körper"), ("Gesundheit", "Gesundheit"),
                                 ("Freiheit", "Freiheit"), ("Eigentum", "Eigentum"), ("sonstiges", "sonstige"))], size=32)
PG = "Delikt: § 823 Abs. 1 BGB"
folie([("delikt", "Deliktsrecht?"), ("w823", f"{PG} › geschützte Rechtsgüter"), ("verm", f"{PG} › Gewinnchance: kein Rechtsgut")], rechts_frei([
    *tafel("delikt", "Bleibt das Deliktsrecht?"),
    *w823,
    *neinz("entgangene Gewinnchance: kein geschütztes Rechtsgut", w823_y + 40, "verm", "Bold", 31, x=160),
    z("das Vermögen als solches ist nicht geschützt", 160, w823_y + 85, beim("verm", "denn"), size=31),
    zit("BGH, Urt. v. 5.4.2018 – III ZR 211/17, Rn. 19", 160, w823_y + 135, beim("verm", "denn")),
    *requisit([("w823", ("tabler", "shield-x", 110, WEISS), "Rechtsgüter", WEISS),
               ("verm", ("tabler", "clover", 110, GRUEN), "Gewinnchance: nicht geschützt", HELLROT)]),
    *zwei("UL", [("delikt", "denkt"), ("verm", "ernst")], "EN", [("delikt", "ruhig"), ("verm", "sorge")]),
]))
assert w823_y + 180 <= 930, w823_y

# ===========================================================================================================================
# G2 Abgrenzung: Haftungsmaßstab bei Gefälligkeiten (BGH VI ZR 467/15)
# ===========================================================================================================================
PG2 = "Abgrenzung: Haftung bei Gefälligkeiten"
folie([("garten", f"{PG2} › Rechtsgut verletzt"), ("fahrl", f"{PG2} › einfache Fahrlässigkeit, § 276 Abs. 2 BGB"),
       ("still", f"{PG2} › Haftungsbeschränkung nur ausnahmsweise")], rechts_frei([
    *tafel("garten", "Anders: ein Rechtsgut verletzt"),
    z("Gefälligkeit, bei der ein Rechtsgut verletzt wird:", 110, 180, "garten", "Bold", 32),
    z("Gießen des Nachbargartens, Wasserschaden", 110, 226, beim("garten", "Gießen"), size=32),
    blk(110, 300, 1040, 130, HELLBLAU, "fahrl", [("Haftung aus Delikt schon für einfache", "Bold", 31, INK),
                                              ("Fahrlässigkeit (§ 276 Abs. 2 BGB)", "ExtraBold", 32, INK)]),
    *pkt("stillschweigende Haftungsbeschränkung:", 480, "still", "Bold", 32, x=160),
    z("nur ausnahmsweise", 160, 525, beim("still", "nur"), "Bold", 32),
    zit("BGH, Urt. v. 26.4.2016 – VI ZR 467/15, Rn. 8, 10", 110, 590, beim("still", "nur")),
    ficon("tabler", "plant", 1430, 330, 120, beim("garten", "Nachbargartens"), fuell=GRUEN),
    ficon("tabler", "bucket-droplet", 1700, 330, 120, beim("garten", "Wasserschaden"), fuell=BLAU),
    pl("Wasserschaden", 1700, 360, beim("garten", "Wasserschaden"), fill=HELLBLAU, size=28, anker="m"),
    pl("Nachbargarten", 1430, 360, beim("garten", "Nachbargartens"), fill=GRUEN, size=28, anker="m"),
    *zwei("UL", [("garten", "ruhig"), ("fahrl", "ernst")], "EN", [("garten", "denkt"), ("still", "ruhig")]),
]))

# ===========================================================================================================================
# H Fall: zurück in der Teeküche
# ===========================================================================================================================
folie([("leer", "Fall · Erna und Ulf gehen leer aus"), ("e2", "Fall · Erna gibt ab jetzt den Schein ab")], [
    boden_(G0, "leer", fill=(236, 230, 220, 255), h=100),
    zeile_kueche(80, 640, 700, G0, "leer"),
    ficon("tabler", "coffee", 200, 704, 110, "leer", fuell=WEISS, anim="cut"),
    ficon("tabler", "mug", 360, 704, 80, "leer", fuell=ROT, anim="cut"),
    ficon("tabler", "mug", 460, 704, 80, "leer", fuell=BLAU, anim="cut"),
    ficon("tabler", "clock", 560, 480, 100, "leer", fuell=WEISS, anim="cut"),
    pl("leer ausgegangen", 70, 30, beim("leer", "leer"), fill=HELLROT, size=32),
    *fig("EN", EX3, G0, FHA, [("leer", "sorge_r")], bis="e2", erst="cut"),
    *redet("EN_froh_redet_r", EX3, G0, FHA, "e2", "tipp"),
    ns("Erna", EX3, G0, "leer", GELB),
    *fig("UL", UX3, G0, FHA, [("leer", "ernst_r"), ("e2", "froh_r")], erst="cut"),
    ns("Ulf", UX3, G0, "leer", BLAU),
    *fig("HI", HX3, G0, FHA, [("leer", "ruhig"), ("e2", "froh")], erst="cut"),
    ns("Gerold", HX3, G0, "leer", GRUEN),
    lottoschein(530, 563, 110, beim("e2", "Schein")),
    blase("sprech", 980, 220, "e2", 1250, 250, inhalt=["Dann spielen wir eben weiter. Aber", "den Schein gebe ab jetzt ich ab."],
          textsize=34, figur=("EN_froh_redet_r", EX3, G0, FHA)),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Rechtsbindungswille je Pflicht"), ("tp1", "Klausurtipp · die einzelne Pflicht"),
       ("tp2", "Klausurtipp · Gewinn verteilen: bindend"), ("tp3", "Klausurtipp · Schein einreichen: Gefälligkeit"),
       ("tp4", "Klausurtipp · Kriterien")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Rechtsbindungswille nicht pauschal", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("für die ganze Tipprunde prüfen,", 200, 250, beim("tipp", "ganze"), "Bold", 36),
    z("sondern für die einzelne Pflicht:", 200, 300, "tp1", "Bold", 36),
    *okz("Gewinn verteilen: rechtlich bindend", 385, "tp2", "Regular", 34, x=245),
    *neinz("Schein ausfüllen und einreichen:", 455, "tp3", "Regular", 34, x=245),
    z("in der Regel nur Gefälligkeit", 245, 503, beim("tp3", "in"), size=34),
    linienzug([(130, 590), (1130, 590)], "tp4", breite=3),
    z("Begründen mit den Kriterien:", 200, 620, "tp4", "Bold", 36),
    z("wirtschaftliche Bedeutung, Interessenlage,", 200, 676, beim("tp4", "wirtschaftliche"), size=33),
    z("Haftungsrisiko des Helfers", 200, 722, beim("tp4", "Haftungsrisiko"), size=33),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Anspruch aus § 280 Abs. 1 BGB", True),
          ("c2", 1, "1. Schuldverhältnis mit einer Pflicht zum Einreichen?", False),
          ("c3", 2, "Rechtsbindungswille (objektiver Beobachter): wirtschaftliche Bedeutung,", False),
          (beim("c3", "Interessenlage"), 2, "Interessenlage, Haftungsrisiko", False),
          ("c4", 2, "hier verneint: bloße Gefälligkeit", False),
          ("c5", 1, "2. kein Anspruch", False),
          ("c6", 0, "II. § 823 Abs. 1 BGB", True),
          ("c7", 1, "kein geschütztes Rechtsgut – das Vermögen als solches fehlt", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Lottogemeinschaft"), 110, 90, "sch", 46)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 260)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 88, 1: 76, 2: 66}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. § 280 Abs. 1 BGB"), ("c2", "Prüfschema › I. 1. Schuldverhältnis"),
       ("c3", "Prüfschema › I. 1. Rechtsbindungswille"), ("c4", "Prüfschema › I. 1. hier: Gefälligkeit"),
       ("c5", "Prüfschema › I. 2. kein Anspruch"), ("c6", "Prüfschema › II. § 823 Abs. 1 BGB"),
       ("c7", "Prüfschema › II. kein geschütztes Rechtsgut")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer für die Tipprunde ohne", 0)], [("Entgelt den Schein abgibt,", 0)],
                 [("tut in der Regel nur einen ", 0), ("Gefallen", "a"), (".", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Gefallen")}),
    *markertext([[("Für den entgangenen Gewinn", 0)], [("haftet er deshalb", 0)], [("grundsätzlich nicht", "b"), (".", 0)]],
                750, 600, 46, "mk2", {"b": beim("mk2", "grundsätzlich")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
