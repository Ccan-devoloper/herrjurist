"""Folge 282 · Sofortiges Anerkenntnis § 93 ZPO: Verlieren ohne Kosten – Serienstandard Open Peeps (Katzenkönig).
Fall: Die Gartenbau Fink GmbH (Herr Fink) verklagt Frau Mehlhorn ohne Mahnung auf 1.280 € Werklohn; Frau Mehlhorn will einfach
zahlen und geht zu Rechtsanwalt Rosenbaum.
Szenen laut ../SZENENPLAN.md: A1 Gartenbau und Garten (Fall), A2 Kanzlei (Hook, Fragen), B Sachverhalt, C Zahlen oder
anerkennen?, D § 307 ZPO (Wortlautkarte), E § 93 ZPO (Wortlautkarte), E1 keine Veranlassung, E2 sofort (schriftliches
Vorverfahren), F1 Tenor, F2 Teilanerkenntnis, G zwei typische Fehler, H Klausurtipp (Lexi), I Schema, J Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/person/neben/zm als eigene Kopie aus
Folge 270 (gemeinsame Dateien unverändert); neu: garten(), kanzlei(), hecke(), sachverhalt_282().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
from PIL import ImageFilter

bausteine.FIGORDNER = "op_282/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_282/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel, nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/217/219/222) ---------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, haken=None, **k):
    """Tafelzeile mit Bleistift-Haken davor; haken = Cue der gesprochenen Bejahung (sonst mit der Zeile)."""
    return [bis_(ok(x - 45, y + 20, haken or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


# --- Besetzung und Maße ----------------------------------------------------------------------------------------------------
BODEN, FH = 860, 480                        # Fallszenen: Bodenlinie, Figurenhöhe
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 150, 370                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"ME": "Frau Mehlhorn", "RO": "Herr Rosenbaum", "FI": "Herr Fink"}
NFARBE = {"ME": ROT, "RO": BLAU, "FI": GRUEN}


def boden(cue, hart_=True):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


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


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)






# --- eigene Szenenbausteine (aus Folge 270) --------------------------------------------------------------------------------------
GRAUHELL = (226, 226, 230, 255)


def zm(text, cx, y, cue, stil="Regular", size=30, **k):
    """Tafelzeile, mittig auf cx gesetzt."""
    return z(text, round(cx - F(stil, size).getlength(glyphen(text)) / 2), y, cue, stil, size, **k)


def person(k, x, unten, hoehe, folge, bis=None, erst="cut", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)]; suffix mit '!' = Figur spricht von cue bis zum
    nächsten Eintrag (Mundzustände aus den Wortgrenzen, redet())."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if s.startswith("!"):
            assert b is not None, "Redefenster braucht ein Ende"
            els += redet(f"{k}_{s[1:]}", x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(f"{k}_{s}", x, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0,
                                 bis=b))
    return els


def neben(k, x, folge, bis=None, erst="pop"):
    """Figur neben der Tafel (blickt nach links zur Tafel bzw. _r nach rechts), mit Namensschild ab dem ersten Bild."""
    els = [*person(k, x, FB, FR, folge, bis=bis, erst=erst), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def sachverhalt_282(cue, absaetze, fragen):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    for f_ in fragen:
        els.append(pille(glyphen(f_), 210, y + 6, cue, fill=PINK, size=36)); y += 76
    assert y + 10 <= 950, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)



# --- eigene Szenenbausteine Folge 282 --------------------------------------------------------------------------------------
GRUENHELL = (232, 247, 233, 255)
GRAUHELL = (226, 226, 230, 255)
HECKE = (110, 170, 105, 255)
HECKE_D = (86, 140, 84, 255)
ERDE = (150, 110, 80, 255)
PAPIER = (255, 253, 245, 255)


def _hecke_bild(breite, hoehe, n):
    """Geschnittene Hecke: gerade Kante unten, flach gewölbte Blattbögen oben, Tuschekontur (programmatisch, 2-fach gerendert)."""
    k = 2; W_, H_ = (breite + 12) * k, (hoehe + 12) * k
    maske = Image.new("L", (W_, H_), 0); md = ImageDraw.Draw(maske)
    o = 6 * k; bw = breite * k / n
    md.rounded_rectangle((o, o + 30 * k, o + breite * k, o + hoehe * k), 14 * k, fill=255)
    for i in range(n):
        md.ellipse((o + i * bw - 4 * k, o, o + (i + 1) * bw + 4 * k, o + 64 * k), fill=255)
    rand = maske.filter(ImageFilter.MaxFilter(5 * 2 + 1))
    im = Image.new("RGBA", (W_, H_), (0, 0, 0, 0))
    im.paste(Image.new("RGBA", (W_, H_), INK), (0, 0), rand)
    im.paste(Image.new("RGBA", (W_, H_), HECKE), (0, 0), maske)
    d = ImageDraw.Draw(im)
    for i in range(n):                                       # Blattstriche
        cx = o + (i + 0.5) * bw
        for dy in (70, 130):
            d.arc((cx - 22 * k, o + dy * k, cx + 22 * k, o + (dy + 30) * k), 200, 340, fill=HECKE_D, width=4 * k)
    return im.resize((breite + 12, hoehe + 12), Image.LANCZOS)


def hecke(x, unten, breite, hoehe, cue, n=4):
    """Frisch geschnittene Hecke (programmatisch)."""
    return [El(_hecke_bild(breite, hoehe, n), x - 6, unten - hoehe - 6, cue, "cut", 0.0, None, name="hecke")]


def beet(x, unten, cue):
    """Beet: Erdstreifen mit drei Blumen (Tabler flower)."""
    return [feld(x, unten - 34, 260, 34, cue, fill=ERDE, rand=4, rund=10, name="beet"),
            *[ficon("tabler", "flower", x + 45 + i * 85, unten - 30, 70, cue, fuell=f, anim="pop")
              for i, f in enumerate((ROT, GELB, LILA))]]


# ===========================================================================================================================
# A1 Fall: Gartenbau Fink und der Garten von Frau Mehlhorn
# ===========================================================================================================================
FIX, MEX = 560, 1390
FIa = ("FI_redet_r", FIX, BODEN, FH)
MEa = ("ME_redet", MEX, BODEN, FH)
SCHILD = (90, 330, 300, 130)
rechnung = ficon("tabler", "receipt-euro", MEX - 115, BODEN - 250, 84, "rechnung", fuell=WEISS, bis="frist")
bewegt(rechnung, "rechnung", ("rechnung", 1.0), -(MEX - 115 - (FIX + 100)), 0)
brief = ficon("tabler", "mail", 1800, BODEN - 112, 70, beim("klage", "Klage"), fuell=GELB)
szene(brief, "282briefkasten_1", gain=0.8, versatz=-0.25)   # Briefkastenklappe: Transient (0,32 s) kurz nach dem Erscheinen
folie([(NULL, "Fall · Gartenbau Fink"), ("fi1", "Fall · Keine Zahlung? Dann zum Amtsgericht"),
       ("post", "Fall · Klage ohne Mahnung")], [
    boden(NULL),
    hart(feld(*SCHILD, NULL, fill=GRUENHELL, rand=5, rund=16, name="schild")),
    hart(z("Gartenbau", SCHILD[0] + 30, SCHILD[1] + 14, NULL, "ExtraBold", 40, rechts=SCHILD[0] + SCHILD[2])),
    hart(z("Fink", SCHILD[0] + 30, SCHILD[1] + 64, NULL, "ExtraBold", 40, rechts=SCHILD[0] + SCHILD[2])),
    hart(feld(SCHILD[0] + SCHILD[2] // 2 - 8, SCHILD[1] + SCHILD[3] + 10, 16, BODEN - SCHILD[1] - SCHILD[3] - 12, NULL,
              fill=HOLZ, rand=3, rund=4, name="pfosten")),
    hart(ficon("tabler", "garden-cart", 300, BODEN - 2, 150, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "plant", 820, BODEN - 2, 90, NULL, fuell=GRUEN, anim="cut")),
    hart(linienzug([(960, 400), (960, BODEN)], NULL, breite=4, farbe=TEXT)),
    hart(pl("Ein Gartenbaubetrieb", 70, 30, NULL, fill=GELB, size=40)),
    *person("FI", FIX, BODEN, FH, [(NULL, "ruhig_r"), ("frist", "eilig_r"), ("fi1", "!redet_r"), ("post", "eilig_r"),
                                   ("me1", "denkt_r")]),
    hart(fall_ns("FI", FIX, NULL)),
    pl("Gartenbau Fink GmbH", FIX, BODEN + 92, beim("fink", "Fink"), fill=WEISS, size=28, anker="m", bis="fi1"),
    # Garten von Frau Mehlhorn (rechts)
    *[hart(e) for e in hecke(990, BODEN, 240, 210, beim("fink", "Mehlhorn"))],
    ficon("tabler", "scissors", 1110, BODEN - 222, 70, beim("fink", "Hecke"), fuell=WEISS, bis="rechnung"),
    *beet(1500, BODEN, beim("fink", "Beet")),
    hart(ficon("tabler", "mailbox", 1800, BODEN - 2, 120, beim("fink", "Mehlhorn"), fuell=BLAUHELL, anim="cut")),
    *person("ME", MEX, BODEN, FH, [(beim("fink", "Mehlhorn"), "ruhig"), ("klage", "sorge"), ("me1", "!redet")],
           bis="kanzlei", erst="pop"),
    fall_ns("ME", MEX, beim("fink", "Mehlhorn"), d=0.1),
    pl("Hecke geschnitten, Beet angelegt", 1440, 250, beim("fink", "Beet"), fill=WEISS, size=28, anker="m", bis="rechnung"),
    rechnung,
    pl("Rechnung: 1.280 €", 1440, 250, beim("rechnung", "tausendzweihundertachtzig"), fill=GELB, size=32, anker="m",
       bis="frist"),
    ficon("tabler", "calendar-time", 1440, 340, 96, "frist", fuell=WEISS, bis="fi1"),
    pl("2 Wochen später: kein Geld", 1440, 100, "frist", fill=GELB, size=32, anker="m", bis="fi1"),
    blase("sprech", 640, 190, "fi1", 600, 240, inhalt=["Keine Zahlung?", "Dann gleich zum Amtsgericht."], textsize=34,
          figur=FIa, bis="post"),
    ficon("tabler", "building-bank", 820, 500, 100, beim("fi1", "Amtsgericht"), fuell=WEISS, bis="post"),
    pl("ohne Mahnung", 1140, 100, "post", fill=WEISS, size=32, anker="m", bis="me1"),
    pl("ohne Anruf", 1560, 100, beim("post", "Anruf"), fill=WEISS, size=32, anker="m", bis="me1"),
    ficon("tabler", "bell-off", 1140, 280, 90, "post", fuell=WEISS, bis="me1"),
    ficon("tabler", "phone-off", 1560, 280, 90, beim("post", "Anruf"), fuell=WEISS, bis="me1"),
    brief,
    pl("Klage vom Amtsgericht", 1690, 610, beim("klage", "Klage"), fill=GELB, size=30, anker="m", bis="me1"),
    blase("sprech", 700, 250, "me1", 1380, 200, inhalt=["Eine Klage?", "Mich hat niemand gemahnt.",
                                                       "Ich zahle die Rechnung doch einfach."], textsize=32, figur=MEa,
          bis="kanzlei"),
])

# ===========================================================================================================================
# A2 Kanzlei: Rechtsanwalt Rosenbaum, Hook und Fragen
# ===========================================================================================================================
ROX, ME2X = 640, 1380
ROa = ("RO_redet_r", ROX, BODEN, FH)
folie([("kanzlei", "Fall · In der Kanzlei"), ("hook", "Einstieg · Die Frage")], [
    boden("kanzlei"),
    hart(ficon("tabler", "window", 250, 420, 180, "kanzlei", fuell=BLAUHELL, anim="cut")),
    hart(feld(1560, 470, 300, 14, "kanzlei", fill=HOLZ, rand=4, rund=4, name="regal")),
    hart(ficon("tabler", "books", 1640, 468, 100, "kanzlei", fuell=GELB, anim="cut")),
    hart(ficon("tabler", "scale", 1780, 468, 90, "kanzlei", fuell=WEISS, anim="cut")),
    hart(feld(860, BODEN - 200, 300, 30, "kanzlei", fill=HOLZ, rand=5, rund=6, name="tisch")),
    hart(feld(880, BODEN - 170, 24, 166, "kanzlei", fill=HOLZ, rand=4, rund=4, name="tischbein")),
    hart(feld(1116, BODEN - 170, 24, 166, "kanzlei", fill=HOLZ, rand=4, rund=4, name="tischbein")),
    hart(ficon("tabler", "mail", 1010, BODEN - 228, 80, "kanzlei", fuell=GELB, anim="cut")),
    hart(pl("In der Kanzlei", 70, 30, "kanzlei", fill=GELB, size=40)),
    *person("RO", ROX, BODEN, FH, [("kanzlei", "ruhig_r"), ("ro1", "!redet_r"), ("hook", "denkt_r")], erst="pop"),
    fall_ns("RO", ROX, "kanzlei", d=0.1),
    pl("Rechtsanwalt", ROX, BODEN + 92, beim("kanzlei", "Rechtsanwalt"), fill=WEISS, size=28, anker="m", bis="hook"),
    *person("ME", ME2X, BODEN, FH, [("kanzlei", "sorge"), ("ro1", "denkt"), ("hook", "ruhig")], erst="cut"),
    hart(fall_ns("ME", ME2X, "kanzlei")),
    pl("Beklagte", ME2X, BODEN + 92, "kanzlei", fill=WEISS, size=28, anker="m", bis="hook"),
    blase("sprech", 640, 210, "ro1", 760, 200, inhalt=["Langsam. Erst klären wir,", "wer die Kosten trägt."],
          textsize=34, figur=ROa, bis="hook"),
    pl("Prozess verlieren, keine Kosten tragen?", 960, 110, "hook", fill=GELB, size=40, anker="m", bis="frage"),
    pl("Wann ist ein Anerkenntnis sofort?", 960, 90, "frage", fill=PINK, size=36, anker="m"),
    pl("Wann gab die Beklagte keine Veranlassung zur Klage?", 960, 170, "frage2", fill=PINK, size=36, anker="m"),
    pl("Und wie sieht der Tenor aus?", 960, 250, "frage3", fill=PINK, size=36, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_282("sv", [
    "Herr Fink, Inhaber der Gartenbau Fink GmbH, hat bei Frau Mehlhorn die Hecke geschnitten und ein Beet angelegt. Die "
    "Rechnung über 1.280 € ging ihr Anfang September zu, ohne Zahlungsfrist und ohne Hinweis auf Verzugsfolgen. Zwei "
    "Wochen später reicht die GmbH ohne Mahnung und ohne Anruf Klage beim Amtsgericht ein.",
    "Das Gericht ordnet das schriftliche Vorverfahren an. Frau Mehlhorn will die Rechnung einfach bezahlen und geht zu "
    "Rechtsanwalt Rosenbaum.",
], ["Zahlen oder anerkennen: Wer trägt die Kosten?", "Wie lautet der Tenor?"])

# ===========================================================================================================================
# C Problem: zahlen oder anerkennen?
# ===========================================================================================================================
folie([("zahl", "Problem › zahlen oder anerkennen?"), ("zahl2", "Problem › Zahlung: Erledigung, § 91a ZPO"),
       ("direkt", "Problem › direkter: das Anerkenntnis")], rechts_frei([
    *tafel("zahl", "Zahlen oder anerkennen?"),
    blk(110, 190, 1040, 80, GRAUHELL, "zahl", [("Erste Idee: einfach zahlen", "ExtraBold", 36, INK)]),
    z("Nach der Zustellung: Erledigung des Rechtsstreits", 110, 310, "zahl2", "Bold", 32),
    z("Kosten: § 91a ZPO, nach billigem Ermessen", 110, 370, "zahl3", "Bold", 32),
    zit("§ 91a Abs. 1 S. 1 ZPO", 110, 420, beim("zahl3", "Paragraf")),
    blk(110, 500, 1040, 90, GELB, "direkt", [("Direkter: das Anerkenntnis", "ExtraBold", 38, INK)]),
    *neben("ME", FX, [("zahl", "ruhig"), ("zahl3", "denkt"), ("direkt", "froh")], erst="pop"),
    *requisit([("zahl", ("tabler", "coins", 110, GELB), "zahlen", GELB),
               ("direkt", ("tabler", "file-check", 100, WEISS), "anerkennen", GRUEN)]),
]))

# ===========================================================================================================================
# D § 307 ZPO (Wortlautkarte)
# ===========================================================================================================================
W307 = ("„Erkennt eine Partei den gegen sie geltend gemachten Anspruch ganz oder zum Teil an, so ist sie dem Anerkenntnis "
        "gemäß zu verurteilen. Einer mündlichen Verhandlung bedarf es insoweit nicht.“")
w307, w307_y = wortlaut(110, 180, 1040, W307, "§ 307 ZPO", "w307", marken=[
    ("Erkennt", beim("w307b", "Erkennt")), ("ganz oder zum Teil", beim("w307b", "ganz")),
    ("Anerkenntnis", beim("w307b", "Anerkenntnis")), ("verurteilen", beim("w307b", "verurteilen")),
    ("mündlichen Verhandlung", beim("ohne", "mündlichen"))], size=32)
folie([("w307", "§ 307 ZPO › Anerkenntnisurteil"), ("k91", "§ 91 ZPO › Grundsatz: Wer unterliegt, trägt die Kosten"),
       ("ausn", "§ 91 ZPO › Ausnahme?")], rechts_frei([
    *tafel("w307", "Das Anerkenntnis: § 307 ZPO"),
    *w307,
    *okz("Frau Mehlhorn verliert: Anerkenntnisurteil", w307_y + 30, "verl", "Bold", 32, x=160,
         haken=beim("verl", "Anerkenntnisurteil")),
    z("§ 91: Die unterliegende Partei trägt die Kosten.", 110, w307_y + 110, "k91", "Bold", 32),
    zit("§ 91 Abs. 1 S. 1 ZPO", 110, w307_y + 158, beim("k91", "Paragraf")),
    pl("Doch: eine Ausnahme", 110, w307_y + 220, "ausn", fill=GELB, size=34),
    *neben("ME", FX, [("w307", "ruhig"), ("verl", "sorge"), ("ausn", "denkt")], erst="pop"),
    *requisit([("w307", ("tabler", "file-check", 100, WEISS), "Anerkenntnis", GRUEN),
               ("k91", ("tabler", "coins", 110, HELLROT), "Kosten?", ROT)]),
]))
assert w307_y + 290 <= 895, w307_y

# ===========================================================================================================================
# E § 93 ZPO (Wortlautkarte)
# ===========================================================================================================================
W93 = ("„Hat der Beklagte nicht durch sein Verhalten zur Erhebung der Klage Veranlassung gegeben, so fallen dem Kläger die "
       "Prozesskosten zur Last, wenn der Beklagte den Anspruch sofort anerkennt.“")
w93, w93_y = wortlaut(110, 180, 1040, W93, "§ 93 ZPO", "w93", marken=[
    ("nicht durch sein Verhalten", beim("w93b", "nicht")), ("Veranlassung", beim("w93b", "Veranlassung")),
    ("dem Kläger", beim("w93b", "Kläger")), ("Prozesskosten zur Last", beim("w93b", "Prozesskosten")),
    ("sofort", beim("w93b", "sofort"))], size=32)
folie([("w93", "§ 93 ZPO › Kosten bei sofortigem Anerkenntnis"), ("zwei", "§ 93 ZPO › zwei Voraussetzungen")], rechts_frei([
    *tafel("w93", "Die Ausnahme: § 93 ZPO"),
    *w93,
    blk(110, w93_y + 40, 500, 110, GRUENHELL, beim("zwei", "keine"), [("1.", "ExtraBold", 34, INK),
                                                                       ("keine Veranlassung", "ExtraBold", 34, INK)]),
    blk(650, w93_y + 40, 500, 110, BLAUHELL, beim("zwei", "sofort"), [("2.", "ExtraBold", 34, INK),
                                                                       ("sofort anerkannt", "ExtraBold", 34, INK)]),
    *neben("RO", FX, [("w93", "ruhig"), ("zwei", "froh")], erst="pop"),
    *requisit([("w93", ("tabler", "scale", 110, WEISS), "§ 93 ZPO", WEISS),
               (beim("w93b", "Kläger"), ("tabler", "scale", 110, BLAUHELL), "Kosten: Kläger", BLAU)]),
]))
assert w93_y + 160 <= 895, w93_y

# ===========================================================================================================================
# E1 Erstens: keine Veranlassung zur Klage
# ===========================================================================================================================
MEs = ("ME_redetfest", FX, FB, FR)
folie([("ver", "§ 93 ZPO › 1. keine Veranlassung"), ("ver3", "§ 93 ZPO › 1. Veranlassung: der Fall"),
       ("verzug", "§ 93 ZPO › 1. kein Verzug, § 286 BGB"), ("keine", "§ 93 ZPO › 1. keine Veranlassung gegeben")],
      rechts_frei([
    *tafel("ver", "1. Keine Veranlassung zur Klage"),
    blk(110, 180, 1040, 112, HELL, "ver1", [("Verhalten vor dem Prozess lässt den Kläger annehmen,", "Bold", 30, INK),
                                            ("er komme ohne Gericht nicht zu seinem Recht", "Bold", 30, INK)]),
    zit("BGH, Beschl. v. 30.5.2006 – VI ZB 64/05, Rn. 10", 110, 302, beim("ver1", "Recht")),
    z("typisch: fällige Leistung trotz Aufforderung nicht erbracht", 110, 355, "ver2", "Bold", 30),
    zit("BGH, Beschl. v. 22.10.2015 – V ZB 93/13, Rn. 19", 110, 397, beim("ver2", "Aufforderung")),
    z("Im Fall:", 110, 460, "ver3", "ExtraBold", 32),
    *okz("Rechnung", 460, beim("ver3", "Rechnung"), "Bold", 32, x=330),
    *neinz("Mahnung", 460, beim("ver3", "Mahnung"), "Bold", 32, x=600),
    *neinz("Anruf", 460, beim("ver3", "Anruf"), "Bold", 32, x=860),
    *neinz("kein Verzug: keine Mahnung, 30 Tage nicht um", 530, "verzug", "Bold", 32, x=160,
           kreuz=beim("verzug", "Verzug")),
    zit("§ 286 Abs. 1, 3 BGB", 160, 575, beim("verzug", "dreißig")),
    blk(110, 640, 1040, 84, GRUENHELL, "keine", [("Also: keine Veranlassung", "ExtraBold", 36, INK)]),
    ok(1100, 682, beim("keine", "Veranlassung"), gr=22),
    *neben("ME", FX, [("ver", "ruhig"), ("ver3", "denkt"), ("keine", "froh"), ("me2", "!redetfest")], bis="sof"),
    blase("sprech", 520, 150, "me2", 1520, 240, inhalt=["Ich hätte sofort gezahlt."], textsize=34, figur=MEs),
    *requisit([("ver3", ("tabler", "receipt-euro", 100, WEISS), "Rechnung", WEISS),
               (beim("ver3", "Mahnung"), ("tabler", "bell-off", 100, WEISS), "keine Mahnung", WEISS)], bis="me2"),
]))

# ===========================================================================================================================
# E2 Zweitens: sofort (schriftliches Vorverfahren)
# ===========================================================================================================================
X1r = ("RO_redet_r", X1, FB, FR)
folie([("sof", "§ 93 ZPO › 2. sofort"), ("sof3", "§ 93 ZPO › 2. sofort = in der Klageerwiderungsfrist"),
       ("vert", "§ 93 ZPO › 2. Verteidigungsanzeige ohne Abweisungsantrag"), ("erg", "Ergebnis › Kosten: Klägerin")],
      rechts_frei([
    *tafel("sof", "2. Sofort anerkannt"),
    pl("schriftliches Vorverfahren", 110, 172, "sof2", fill=WEISS, size=30),
    blk(110, 240, 470, 120, BLAUHELL, "fr1", [("2 Wochen", "ExtraBold", 34, INK), ("Verteidigungsanzeige", "Bold", 30, INK)]),
    hart(pfeil(590, 300, 640, 300, "fr2", breite=8, kopf=24)),
    blk(650, 240, 500, 120, GELB, "fr2", [("mind. 2 weitere Wochen", "ExtraBold", 34, INK),
                                          ("Klageerwiderung", "Bold", 30, INK)]),
    zit("§ 276 Abs. 1 S. 1, 2 ZPO", 110, 372, beim("fr1", "zwei")),
    blk(110, 420, 1040, 80, HELL, "sof3", [("sofort = innerhalb der Klageerwiderungsfrist", "ExtraBold", 34, INK)]),
    *okz("Verteidigungsanzeige schadet nicht,", 525, beim("vert", "schadet"), "Bold", 32, x=160),
    z("solange ohne Abweisungsantrag und ohne Bestreiten", 160, 570, beim("vert", "solange"), "Bold", 30),
    zit("BGH, Beschl. v. 30.5.2006 – VI ZB 64/05, Rn. 22; v. 21.3.2019 – IX ZB 54/18, Rn. 7", 110, 618, "bgh"),
    blk(110, 680, 1040, 80, GRUENHELL, "erg", [("Ergebnis: Frau Mehlhorn wird verurteilt,", "ExtraBold", 32, INK)]),
    blk(110, 775, 1040, 80, BLAUHELL, "erg2", [("aber die Kosten trägt die Gartenbaufirma.", "ExtraBold", 32, INK)]),
    *neben("RO", X1, [("sof", "ruhig_r"), ("sof3", "ernst_r"), ("ro2", "!redet_r"), ("erg", "froh_r")]),
    *neben("ME", X2, [("sof", "ruhig"), ("ro2", "denkt"), ("erg", "froh")]),
    blase("sprech", 640, 230, "ro2", 1540, 210, inhalt=["Wir zeigen nur die Verteidigung an", "und erkennen in der",
                                                       "Klageerwiderung an."], textsize=30, figur=X1r, bis="erg"),
]))

# ===========================================================================================================================
# F1 Muster: Tenor des Anerkenntnisurteils
# ===========================================================================================================================
UR = (110, 175, 1040, 560)
folie([("ten", "Muster › Tenor des Anerkenntnisurteils"), ("ten2", "Muster › Kosten: § 93 ZPO"),
       ("ten3", "Muster › vorläufig vollstreckbar, § 708 Nr. 1 ZPO")], rechts_frei([
    *tafel("ten", "Muster: der Tenor"),
    feld(*UR, "ten", fill=PAPIER, rand=4, rund=12, name="urteil"),
    zm("Anerkenntnisurteil", 630, 200, "ten0", "ExtraBold", 42),
    zit("§ 313b Abs. 1 S. 2 ZPO", 630 - 140, 255, "ten0"),
    z("1. Die Beklagte wird verurteilt, an die Klägerin", 150, 320, "ten1", "Bold", 32),
    z("1.280 € zu zahlen.", 190, 365, beim("ten1", "tausendzweihundertachtzig"), "Bold", 32),
    z("2. Die Klägerin trägt die Kosten des Rechtsstreits.", 150, 440, "ten2", "Bold", 32),
    zit("§ 93 ZPO", 190, 485, "ten2"),
    z("3. Das Urteil ist vorläufig vollstreckbar.", 150, 560, "ten3", "Bold", 32),
    zit("§ 708 Nr. 1 ZPO", 190, 605, "ten4"),
    pl("ohne Sicherheitsleistung", 110, 770, "ten4", fill=GELB, size=32),
    *neben("RO", FX, [("ten", "ruhig"), ("ten2", "froh"), ("ten3", "ruhig")], erst="pop"),
    *requisit([("ten", ("tabler", "file-certificate", 100, WEISS), "Urteil", WEISS),
               ("ten2", ("tabler", "scale", 110, BLAUHELL), "Kosten: Klägerin", BLAU),
               ("ten4", ("tabler", "file-check", 100, WEISS), "§ 708 Nr. 1", GELB)]),
]))

# ===========================================================================================================================
# F2 Abwandlung: Teilanerkenntnis
# ===========================================================================================================================
folie([("teil", "Abwandlung › Teilanerkenntnis"), ("teil3", "Abwandlung › Teil-Anerkenntnisurteil"),
       ("teil5", "Abwandlung › Kosten im Schlussurteil")], rechts_frei([
    *tafel("teil", "Abwandlung: Teilanerkenntnis"),
    blk(650, 180, 500, 110, HELLROT, "teil", [("300 € Rasenmähen", "ExtraBold", 32, INK), ("nie gemäht", "Bold", 30, INK)]),
    blk(110, 180, 500, 110, GRUENHELL, "teil2", [("980 €", "ExtraBold", 34, INK), ("anerkannt", "Bold", 30, INK)]),
    *okz("Teil-Anerkenntnisurteil über 980 €", 330, "teil3", "Bold", 32, x=160),
    zit("§§ 301, 307 ZPO", 160, 375, beim("teil3", "Teil")),
    z("über 300 € wird gestritten", 160, 420, "teil4", "Bold", 32),
    blk(110, 490, 1040, 80, HELL, "teil5", [("Kosten: dem Schlussurteil vorbehalten", "ExtraBold", 34, INK)]),
    z("Schlussurteil: einheitliche Kostenentscheidung", 110, 600, "teil6", "Bold", 32),
    z("980 €: § 93 ZPO", 160, 655, "teil7", "Bold", 32),
    z("300 €: nach dem Ergebnis des Streits", 160, 705, "teil8", "Bold", 32),
    zit("BGH, Beschl. v. 19.10.2000 – I ZR 176/00", 110, 765, "teil6"),
    *neben("ME", FX, [("teil", "denkt"), ("teil2", "ruhig"), ("teil5", "denkt"), ("teil7", "froh")], erst="pop"),
    *requisit([("teil", ("tabler", "lawn-mower", 120, HELLROT), "nie gemäht", ROT),
               ("teil2", ("tabler", "file-check", 100, WEISS), "980 € anerkannt", GRUEN),
               ("teil5", ("tabler", "hourglass", 100, WEISS), "Schlussurteil", GELB)]),
]))

# ===========================================================================================================================
# G Zwei typische Fehler
# ===========================================================================================================================
folie([("fehl", "Typische Fehler"), ("f1", "Typische Fehler › 1. Abweisungsantrag angekündigt"),
       ("f2", "Typische Fehler › 2. Sicherheitsleistung im Tenor")], rechts_frei([
    *tafel("fehl", "Zwei typische Fehler"),
    *neinz("1. In der Verteidigungsanzeige Klageabweisung", 190, "f1", "Bold", 32, x=160),
    z("ankündigen, erst später anerkennen", 160, 235, beim("f1", "erst"), "Bold", 32),
    z("regelmäßig nicht mehr sofort: Kosten trägt die Beklagte", 160, 295, "f1b", "Bold", 30),
    zit("BGH, Beschl. v. 21.3.2019 – IX ZB 54/18, Rn. 8", 160, 340, beim("f1b", "Kosten")),
    linienzug([(110, 410), (1150, 410)], "f2", breite=4, farbe=TEXT),
    *neinz("2. Anerkenntnisurteil mit Sicherheitsleistung", 440, "f2", "Bold", 32, x=160),
    z("oder Abwendungsbefugnis", 160, 485, beim("f2", "Abwendungsbefugnis"), "Bold", 32),
    blk(110, 560, 1040, 80, HELL, "f2b", [("§ 711 ZPO gilt nur für § 708 Nr. 4 bis 11", "ExtraBold", 34, INK)]),
    *neben("RO", FX, [("fehl", "ernst"), ("f1b", "denkt"), ("f2", "ernst"), ("f2b", "ruhig")], erst="pop"),
    *requisit([("f1", ("tabler", "file-x", 100, HELLROT), "zu spät", ROT),
               ("f2", ("tabler", "coins", 110, HELLROT), "keine Sicherheit", ROT)]),
]))

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Anwaltsklausur: § 93 prüfen")], [
    *tafel("tipp", "Klausurtipp: Anwaltsklausur", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Forderung berechtigt?", 200, 200, "tipp2", "Bold", 36),
    z("Vor jeder Verteidigung § 93 prüfen.", 200, 255, beim("tipp2", "vor"), "ExtraBold", 36),
    blk(150, 340, 1000, 80, ZITAT, "tipp3", [("„Die Beklagte erkennt den Klageanspruch an.“", "ExtraBold", 34, INK)]),
    z("+ Antrag: Kosten der Klägerin auferlegen", 200, 460, "tipp4", "Bold", 34),
    z("+ warum keine Veranlassung zur Klage", 200, 520, "tipp5", "Bold", 34),
    dicon("tabler", "file-text", 450, 800, 120, "tipp3", fuell=WEISS),
    dicon("tabler", "scale", 800, 800, 130, "tipp4", fuell=GELB),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Prüfschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Anerkenntnis, ganz oder zum Teil (§ 307 ZPO)", BLAU, 0),
          ("k2", "II.", "keine Veranlassung zur Klage", GELB, 0),
          ("k2a", "", "Verhalten vor dem Prozess", None, 1),
          ("k3", "III.", "sofort", GRUEN, 0),
          ("k3a", "", "schriftliches Vorverfahren: innerhalb der Klageerwiderungsfrist, ohne Abweisungsantrag", None, 1),
          ("k4", "IV.", "Tenor", LILA, 0),
          ("k4a", "", "Kosten beim Kläger, vorläufig vollstreckbar nach § 708 Nr. 1 ZPO", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: sofortiges Anerkenntnis, § 93 ZPO"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 62, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 34).getlength(r) / 2, y + 8, c, "ExtraBold", 34, rechts=1820),
                    z(txt, 255, y + 8, c, "ExtraBold", 34, rechts=1820)]
        y += 90
    else:
        els_sch.append(z(txt, 330, y - 4, c, "Bold", 30, rechts=1820))
        els_sch.append(ok(290, y + 16, c, gr=18))
        y += 76
assert y <= 960, y
folie([("sch", "Schema · sofortiges Anerkenntnis"), ("k1", "Schema › I. Anerkenntnis"),
       ("k2", "Schema › II. keine Veranlassung"), ("k3", "Schema › III. sofort"), ("k4", "Schema › IV. Tenor")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer ", 0), ("ohne Anlass", "a"), (" verklagt wird", 0)], [("und ", 0), ("sofort anerkennt", "b"), (",", 0)],
                 [("verliert den Prozess,", "c")]],
                750, 300, 50, "merke", {"a": beim("merke", "ohne"), "b": beim("merke", "sofort"),
                                        "c": beim("merke", "verliert")}),
    *markertext([[("aber die ", 0), ("Kosten", "d"), (" trägt der ", 0), ("Kläger.", "e")]],
                750, 560, 50, "m2", {"d": beim("m2", "Kosten"), "e": beim("m2", "Kläger")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
