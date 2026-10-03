"""Folge 116 · Rücktritt § 323 BGB: Das Prüfungsschema mit Fristsetzung – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Leni (privat) bestellt am 1.7.2026 im Online-Shop von Ottmar eine Spielkonsole für 499 €, Vorkasse, Lieferung
bis 8.7.; keine Lieferung; 15.7. Frist „bis morgen“; Ottmar bittet um Geduld; 30.7. Rücktritt per E-Mail.
Szenen laut ../SZENENPLAN.md: A1 Bestellung, A2 Warten/Frist, A3 Lager von Ottmar, A4 Rücktritt/Frage, B Sachverhalt,
C Aufbau, D § 323 Abs. 1 (Wortlaut), E 1. gegenseitiger Vertrag, F 2. fällige, durchsetzbare Leistung, G 3. Frist
(Zeitstrahl), H 4. Entbehrlichkeit § 323 Abs. 2, I 5. kein Ausschluss § 323 Abs. 5, 6, J Klausurfehler Vertretenmüssen,
K II. § 349 (Wortlaut), L III. § 346 Abs. 1, M Abgrenzung § 326 Abs. 5 / § 437 Nr. 2, N Ergebnis, O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi).
Handlungsgeräusche: Tippen am Laptop (Bestellung, E-Mail mit Frist, Rücktritts-E-Mail), Karton im Lager
(../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz/tisch/punkt als eigene Kopie aus Folge 112 (gemeinsame Dateien unverändert); neu: wohnung(), Zeitstrahl Juli (tag()).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_116/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_116/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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



def tisch(cx, unten, cue, w=420, h=250, fill=GELB):
    """Schreibtisch/Ladentheke in Seitenansicht (programmatisch: Platte, zwei Beine; Palettenfläche, Tuschekontur)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")


def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")


# --- Zeitstrahl nach Tagen (1.7. bis 30.9.2026) -----------------------------------------------------------------------------


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
LE_N, OT_N = GRUEN, BLAU                    # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"LE": "Leni", "OT": "Ottmar"}
NFARBE = {"LE": LE_N, "OT": OT_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel LE/OT."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


def wohnung(cue, hart_=False):
    """Lenis Wohnzimmer: Schreibtisch mit Laptop, Sessel (programmatischer Tisch, Tabler-Icons)."""
    els = [boden(cue), tisch(TIX, BODEN, cue), ficon("tabler", "device-laptop", TIX - 20, BODEN - 256, 200, cue, fuell=WEISS),
           ficon("tabler", "armchair", 330, BODEN, 260, cue, fuell=LILA)]
    return [hart(e) for e in els] if hart_ else [e if i == 0 else hart(e) for i, e in enumerate(els)]


# ===========================================================================================================================
# A1 Fall: Leni bestellt online, 1. Juli 2026
# ===========================================================================================================================
TIX = 980                                   # Schreibtisch mit Laptop
LEX = 1480                                  # Leni rechts, blickt nach links zum Laptop
BEST = beim("fall", "bestellt")
folie([(NULL, "Fall · Die Bestellung")], [
    *wohnung(NULL, hart_=True),
    pl("1. Juli 2026", 70, 30, beim("fall", "ersten"), fill=GELB, size=44),
    szene(ficon("tabler", "shopping-cart", TIX - 20, 440, 100, BEST, fuell=WEISS), "116tippen*", 0.6, 0.0),
    pl("Online-Shop", TIX - 20, 300, beim("fall", "Online-Shop"), fill=WEISS, size=32, anker="m"),
    pl("Spielkonsole: 499 €", 70, 120, beim("fall", "Spielkonsole"), fill=GELB, size=36),
    ficon("tabler", "device-gamepad-2", 545, 180, 100, beim("fall", "Spielkonsole"), fuell=LILA),
    pl("Vorkasse: sofort bezahlt", 70, 205, beim("vork", "Vorkasse"), fill=GRUEN, size=36),
    ficon("tabler", "credit-card", 600, 265, 90, beim("vork", "Vorkasse"), fuell=WEISS),
    pl("Lieferung bis 8. Juli", 70, 290, beim("ltermin", "Lieferung"), fill=WEISS, size=36),
    ficon("tabler", "truck-delivery", 520, 352, 100, beim("ltermin", "Lieferung"), fuell=WEISS),
    *fig("LE", LEX, BODEN, FH, [(NULL, "ruhig"), (BEST, "froh")], bis="le1", erst="cut"),
    hart(ns("Leni", LEX, BODEN, NULL, LE_N)),
    *redet("LE_redet", LEX, BODEN, FH, "le1", "warten"),
    blase("sprech", 500, 170, "le1", 1230, 200, inhalt=["Bezahlt. In einer", "Woche ist sie da."], textsize=36,
          figur=("LE_redet", LEX, BODEN, FH), bis="warten"),
])

# ===========================================================================================================================
# A2 Fall: kein Paket, Frist per E-Mail
# ===========================================================================================================================
MAILT = beim("mail", "E-Mail")
folie([("warten", "Fall · Das Warten"), ("mail", "Fall · Die Frist")], [
    *wohnung("warten"),
    pl("8. Juli 2026", 70, 30, beim("warten", "achte"), fill=GELB, size=44, bis=beim("mail", "fünfzehnten")),
    pl("kein Paket", 70, 120, beim("warten", "kein"), fill=ROT, size=36),
    ficon("tabler", "package-off", 330, 520, 130, beim("warten", "kein"), fuell=WEISS, bis="mail"),
    pl("15. Juli 2026", 70, 30, beim("mail", "fünfzehnten"), fill=GELB, size=44),
    szene(ficon("tabler", "mail", TIX - 20, 440, 100, MAILT, fuell=WEISS), "116tippen*", 0.6, 0.0),
    pl("E-Mail an den Shop", TIX - 20, 300, MAILT, fill=WEISS, size=32, anker="m"),
    pl("Frist: bis morgen", 70, 205, beim("le2", "morgen"), fill=GELB, size=36),
    *fig("LE", LEX, BODEN, FH, [("warten", "ruhig"), (beim("warten", "kein"), "sorge"), (MAILT, "denkt")], bis="le2"),
    ns("Leni", LEX, BODEN, "warten", LE_N, d=0.1),
    *redet("LE_bestimmt", LEX, BODEN, FH, "le2", "ott"),
    blase("sprech", 520, 170, "le2", 1230, 200, inhalt=["Liefern Sie die Konsole", "bitte bis morgen."], textsize=36,
          figur=("LE_bestimmt", LEX, BODEN, FH), bis="ott"),
])

# ===========================================================================================================================
# A3 Fall: im Lager von Ottmar
# ===========================================================================================================================
OTX = 1450
LEER = beim("lager", "leer")
folie([("ott", "Fall · Im Lager von Ottmar")], [
    boden("ott"),
    ficon("tabler", "building-warehouse", 420, BODEN, 330, "ott", fuell=GELB),
    pl("Online-Shop von Ottmar", 70, 30, beim("ott", "gehört"), fill=WEISS, size=40),
    szene(ficon("tabler", "package", 830, BODEN, 150, LEER, fuell=WEISS), "116karton*", 0.7, 0.0),
    pl("Regal leer", 70, 120, LEER, fill=ROT, size=36),
    *fig("OT", OTX, BODEN, FH, [("ott", "ruhig"), (LEER, "sorge")], bis="ot1"),
    ns("Ottmar", OTX, BODEN, "ott", OT_N, d=0.1),
    *redet("OT_redet", OTX, BODEN, FH, "ot1", "still"),
    blase("sprech", 700, 260, "ot1", 1000, 220, inhalt=["Mein Lieferant hat mich", "im Stich gelassen. Die Konsole",
                                                        "kommt bald, bitte haben Sie", "noch etwas Geduld."],
          textsize=32, figur=("OT_redet", OTX, BODEN, FH), bis="still"),
])

# ===========================================================================================================================
# A4 Fall: Rücktritt per E-Mail, Frage
# ===========================================================================================================================
SCHREIBT = beim("ruecktr", "schreibt")
folie([("still", "Fall · Der Rücktritt"), ("frage", "Fall · Die Frage")], [
    *wohnung("still"),
    pl("Zwei Wochen später", 70, 30, "still", fill=GELB, size=44, bis=beim("ruecktr", "dreißigsten")),
    pl("30. Juli 2026", 70, 30, beim("ruecktr", "dreißigsten"), fill=GELB, size=44),
    pl("immer noch nichts da", 70, 120, beim("still", "nichts"), fill=ROT, size=36, bis="frage"),
    ficon("tabler", "package-off", 330, 520, 130, beim("still", "nichts"), fuell=WEISS),
    szene(ficon("tabler", "mail", TIX - 20, 440, 100, SCHREIBT, fuell=WEISS), "116tippen*", 0.6, 0.0),
    pl("Rücktritt", TIX - 20, 300, beim("le3", "trete"), fill=ROT, size=32, anker="m"),
    pl("499 € zurück", TIX - 20, 210, beim("le3", "vierhundertneunundneunzig"), fill=GELB, size=32, anker="m", bis="frage"),
    pl("Kann Leni wirksam zurücktreten?", 70, 120, "frage", fill=PINK, size=36),
    pl("War ihre Frist bis morgen nicht viel zu kurz?", 70, 205, "frage2", fill=WEISS, size=34),
    *fig("LE", LEX, BODEN, FH, [("still", "muede"), (SCHREIBT, "denkt")], bis="le3"),
    ns("Leni", LEX, BODEN, "still", LE_N, d=0.1),
    *redet("LE_bestimmt", LEX, BODEN, FH, "le3", "frage"),
    blase("sprech", 700, 220, "le3", 1240, 200, inhalt=["Ich trete vom Kaufvertrag zurück.", "Bitte überweisen Sie mir",
                                                        "die 499 € zurück."], textsize=32,
          figur=("LE_bestimmt", LEX, BODEN, FH), bis="frage"),
    *fig("LE", LEX, BODEN, FH, [("frage", "denkt"), ("frage2", "sorge")], erst="cut"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_116(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_116("sv", [
    "Leni bestellt am 1. Juli 2026 für sich privat im Online-Shop von Ottmar, der den Shop gewerblich betreibt, eine "
    "Spielkonsole für 499 Euro. Sie zahlt sofort per Vorkasse. Versprochen ist die Lieferung bis zum 8. Juli.",
    "Bis zum 8. Juli kommt kein Paket. Am 15. Juli schreibt Leni per E-Mail: „Liefern Sie die Konsole bitte bis "
    "morgen.“ Ottmar antwortet, sein Lieferant habe ihn im Stich gelassen; die Konsole komme bald, Leni möge noch etwas "
    "Geduld haben.",
    "Am 30. Juli ist immer noch nichts geliefert. Leni erklärt Ottmar per E-Mail den Rücktritt vom Kaufvertrag und "
    "verlangt die 499 Euro zurück.",
], "Kann Leni wirksam zurücktreten – und war ihre Frist „bis morgen“ zu kurz?")

# ===========================================================================================================================
# C Aufbau: drei Ebenen
# ===========================================================================================================================
EBENEN = [("p1", "I.", "Rücktrittsrecht, § 323 BGB", BLAU), ("p2", "II.", "Rücktrittserklärung", GELB),
          ("p3", "III.", "Rechtsfolge", GRUEN)]
folie([("plan", "Rücktritt, § 323 BGB › Aufbau")], rechts_frei([
    *tafel("plan", "Rücktritt: drei Ebenen"),
    *[e for k, (c, r, t, fa) in enumerate(EBENEN) for e in (
        karte(130, 220 + k * 150, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 240 + k * 150, c, "ExtraBold", 40),
        z(t, 280, 240 + k * 150, c, "Bold", 40))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "3 Ebenen", WEISS),
               ("p1", ("tabler", "scale", 100, WEISS), "Rücktrittsrecht", BLAU),
               ("p2", ("tabler", "mail", 100, WEISS), "Erklärung", GELB),
               ("p3", ("tabler", "arrow-back-up", 100, WEISS), "Rechtsfolge", GRUEN)]),
    *paar("plan", "LE", [("plan", "ruhig"), ("p3", "froh")], "OT", [("plan", "ruhig"), ("p2", "sorge")]),
]))

# ===========================================================================================================================
# D I. Rücktrittsrecht, § 323 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W323 = ["„(1) Erbringt bei einem gegenseitigen Vertrag der Schuldner",
        "eine fällige Leistung nicht oder nicht vertragsgemäß, so kann",
        "der Gläubiger, wenn er dem Schuldner erfolglos eine",
        "angemessene Frist zur Leistung oder Nacherfüllung bestimmt",
        "hat, vom Vertrag zurücktreten.“"]
w323, w323_y = wortlaut(80, 180, 1100, W323, "§ 323 Abs. 1 BGB", beim("w1", "Paragraf"), marken=[
    (0, "gegenseitigen Vertrag", beim("w1", "gegenseitigen")), (1, "eine fällige Leistung nicht", beim("w1", "fällige")),
    (2, "erfolglos", beim("w1", "erfolglos")), (3, "angemessene Frist zur Leistung", beim("w1", "angemessene")),
    (4, "vom Vertrag zurücktreten", beim("w1", "zurücktreten"))], size=33)
folie([("w1", "I. Rücktrittsrecht › § 323 Abs. 1 BGB")], rechts_frei([
    *tafel("w1", "I. Rücktrittsrecht"),
    *w323,
    blk(110, w323_y + 50, 1040, 80, BLAU, beim("w1", "zurücktreten"), [("Rücktrittsrecht nach erfolgloser Frist", "ExtraBold", 36, INK)]),
    *requisit([("w1", ("tabler", "scale", 100, WEISS), "§ 323 Abs. 1", WEISS),
               (beim("w1", "angemessene"), ("tabler", "hourglass", 100, GELB), "Frist", GELB)]),
    *paar("w1", "LE", [("w1", "ruhig"), (beim("w1", "zurücktreten"), "froh")], "OT", [("w1", "ruhig"), (beim("w1", "angemessene"), "denkt")]),
]))

# ===========================================================================================================================
# E I. 1. Gegenseitiger Vertrag
# ===========================================================================================================================
folie([("g1", "I. 1. Gegenseitiger Vertrag")], rechts_frei([
    *tafel("g1", "1. Gegenseitiger Vertrag"),
    *okz("Kaufvertrag: gegenseitiger Vertrag", 200, beim("g2", "Kaufvertrag"), "Bold", 38, x=160),
    z("Ottmar schuldet die Konsole,", 160, 290, beim("g2", "Ottmar"), size=36),
    z("Leni den Kaufpreis: 499 €", 160, 345, beim("g2", "Leni"), size=36),
    zit("§ 433 Abs. 1, 2 BGB", 160, 405, beim("g2", "Paragraf")),
    *requisit([("g1", ("tabler", "arrows-exchange", 110, WEISS), "gegenseitig", WEISS),
               (beim("g2", "Ottmar"), ("tabler", "device-gamepad-2", 110, LILA), "Konsole", LILA),
               (beim("g2", "Leni"), ("tabler", "coin-euro", 100, GELB), "Kaufpreis 499 €", GELB)]),
    *paar("g1", "LE", [("g1", "ruhig"), (beim("g2", "Leni"), "froh")], "OT", [("g1", "ruhig"), (beim("g2", "Ottmar"), "sorge")]),
]))

# ===========================================================================================================================
# F I. 2. Fällige, durchsetzbare Leistung nicht erbracht
# ===========================================================================================================================
folie([("f1", "I. 2. Fällige Leistung nicht erbracht"), ("f3", "I. 2. Fällige Leistung › ohne Termin"),
       ("f4", "I. 2. Fällige Leistung › durchsetzbar")], rechts_frei([
    *tafel("f1", "2. Fällige Leistung nicht erbracht", size=44),
    *okz("vereinbart: Lieferung bis 8.7.2026", 190, beim("f2", "Vereinbart"), "Bold", 36, x=160),
    *okz("dann fällig, die Lieferung bleibt aus", 250, beim("f2", "Spätestens"), "Bold", 36, x=160),
    zit("§ 271 Abs. 2 BGB", 160, 302, beim("f2", "fällig")),
    z("ohne Termin: sofort fällig, § 271 Abs. 1 BGB", 160, 365, "f3", size=34),
    z("Verbrauchsgüterkauf: nur unverzüglich,", 160, 420, beim("f3", "Verbrauchsgüterkauf"), size=34),
    z("§ 475 Abs. 1 BGB", 160, 468, beim("f3", "Paragraf", 2), size=34),
    *okz("durchsetzbar: Leni hat bezahlt, keine Einrede", 545, beim("f4", "durchsetzbar"), "Bold", 36, x=160),
    zit("BGH, Urt. v. 14.2.2020 – V ZR 11/18, Rn. 38", 160, 600, beim("f4", "Einrede")),
    blk(110, 670, 1040, 90, LILA, "f103", [("Mehr dazu: Video „Einwendung und Einrede“", "ExtraBold", 34, INK)]),
    *requisit([("f1", ("tabler", "package-off", 100, WEISS), "nicht geliefert", ROT),
               ("f2", ("tabler", "calendar-event", 100, WEISS), "fällig: 8.7.2026", WEISS),
               ("f3", ("tabler", "clock", 100, WEISS), "ohne Termin", WEISS),
               ("f4", ("tabler", "hand-stop", 100, WEISS), "keine Einrede", GRUEN)]),
    *paar("f1", "LE", [("f1", "ruhig"), ("f2", "sorge"), ("f4", "froh")], "OT", [("f1", "ruhig"), ("f2", "denkt")]),
]))

# ===========================================================================================================================
# G I. 3. Angemessene Frist, erfolglos abgelaufen (Zeitstrahl Juli 2026)
# ===========================================================================================================================
ZY = 520
JX0, JX1 = 150, 1130


def tag(d):
    """x-Position eines Julitags auf dem Zeitstrahl (1.–31.7.2026)."""
    return JX0 + (d - 1) / 30 * (JX1 - JX0)


folie([("fr1", "I. 3. Frist › angemessen, erfolglos"), ("fr3", "I. 3. Frist › zu kurz"),
       ("fr6", "I. 3. Frist › abgelaufen")], rechts_frei([
    *tafel("fr1", "3. Angemessene Frist"),
    z("zur Leistung bestimmt, erfolglos abgelaufen", 110, 180, beim("fr1", "angemessene"), "Bold", 36),
    linienzug([(JX0 - 10, ZY), (JX1 + 10, ZY)], "fr1", breite=5),
    *[linienzug([(tag(d), ZY - 12), (tag(d), ZY + 12)], "fr1", breite=4) for d in (1, 8, 15, 22, 29)],
    z("Juli 2026", 150, ZY + 22, "fr1", "Bold", 28, farbe=TEXT),
    punkt(tag(15), ZY, beim("fr2", "fünfzehnten"), farbe=ROT),
    dicon("tabler", "mail", tag(15), ZY - 20, 50, beim("fr2", "fünfzehnten"), fuell=WEISS),
    pl("15.7.: Frist bis morgen", tag(15), 250, beim("fr2", "Frist"), fill=WEISS, size=28, anker="m"),
    linienzug([(tag(15), ZY), (tag(16), ZY)], "fr3", breite=9, farbe=ROT),
    pl("zu kurz", tag(15), 330, beim("fr3", "kurz"), fill=ROT, size=28, anker="m"),
    blk(int(tag(16)), ZY + 22, int(tag(27) - tag(16)), 50, GRUEN, beim("fr4", "angemessene"),
        [("angemessene Frist läuft", "ExtraBold", 28, INK)], anim="fade"),
    z("Zu kurze Frist setzt eine angemessene in Gang", 150, ZY + 100, beim("fr4", "setzt"), "Bold", 34),
    zit("BGH, Urt. v. 14.10.2020 – VIII ZR 318/19, Rn. 28", 150, ZY + 148, beim("fr4", "Gang")),
    z("außer: Es kommt gerade auf die Kürze an", 150, ZY + 195, beim("fr5", "Gläubiger"), size=34),
    zit("BGH, Urt. v. 26.8.2020 – VIII ZR 351/19, Rn. 28, 43", 150, ZY + 243, beim("fr5", "Kürze")),
    linienzug([(tag(15), ZY - 70), (tag(30), ZY - 70)], "fr6", breite=4),
    linienzug([(tag(15), ZY - 82), (tag(15), ZY - 58)], "fr6", breite=4),
    linienzug([(tag(30), ZY - 82), (tag(30), ZY - 58)], "fr6", breite=4),
    pl("Leni wartet 2 Wochen", (tag(15) + tag(30)) / 2 + 60, 380, "fr6", fill=GELB, size=28, anker="m"),
    dicon("fluent-emoji-high-contrast", "cross-mark", tag(30), ZY + 22, 44, "fr7"),
    *okz("Frist erfolglos abgelaufen", ZY + 295, beim("fr7", "erfolglos"), "Bold", 36, x=160),
    *requisit([("fr1", ("tabler", "hourglass", 100, WEISS), "Frist", WEISS),
               ("fr3", ("tabler", "hourglass-high", 100, ROT), "bis morgen: zu kurz", ROT),
               ("fr4", ("tabler", "hourglass", 100, GRUEN), "angemessene Frist", GRUEN),
               ("fr6", ("tabler", "truck-delivery", 100, WEISS), "2 Wochen: genügt", WEISS),
               ("fr7", ("tabler", "package-off", 100, WEISS), "nichts geliefert", ROT)]),
    *paar("fr1", "LE", [("fr1", "ruhig"), ("fr3", "sorge"), ("fr4", "froh")], "OT",
          [("fr1", "ruhig"), ("fr3", "froh"), ("fr4", "sorge"), ("fr7", "denkt")]),
]))

# ===========================================================================================================================
# H I. 4. Entbehrlichkeit, § 323 Abs. 2
# ===========================================================================================================================
folie([("e1", "I. 4. Entbehrlichkeit › § 323 Abs. 2 BGB"), ("e5", "I. 4. Entbehrlichkeit › der Fall")], rechts_frei([
    *tafel("e1", "4. Frist entbehrlich?"),
    z("§ 323 Abs. 2 BGB", 110, 180, beim("e1", "Paragraf"), "Bold", 36),
    z("Nr. 1: ernsthafte und endgültige Verweigerung", 150, 245, "e2", "Bold", 34),
    zit("strenge Anforderungen: BGH, Urt. v. 1.7.2015 – VIII ZR 226/14, Rn. 33", 150, 293, beim("e2", "strenge")),
    *neinz("Ottmar bittet nur um Geduld", 340, "e2f", size=34, x=195),
    z("Nr. 2: Termin für den Gläubiger wesentlich", 150, 420, "e3", "Bold", 34),
    z("etwa vor Vertragsschluss mitgeteilt", 195, 470, beim("e3", "etwa"), size=34),
    *neinz("bloßer Liefertermin genügt nicht", 520, "e3f", size=34, x=195),
    z("Nr. 3: besondere Umstände, nur bei", 150, 600, "e4", "Bold", 34),
    z("nicht vertragsgemäßer Leistung", 195, 650, beim("e4", "nicht"), "Bold", 34),
    *neinz("hier bleibt die Lieferung aus", 700, beim("e4", "Lieferung"), size=34, x=195),
    blk(110, 775, 1040, 80, LILA, "e5", [("Frist nötig, und Leni hat sie gesetzt", "ExtraBold", 36, INK)]),
    *requisit([("e1", ("tabler", "hourglass", 100, WEISS), "entbehrlich?", WEISS),
               ("e2", ("tabler", "hand-stop", 100, WEISS), "Verweigerung?", WEISS),
               ("e3", ("tabler", "calendar-event", 100, WEISS), "Termingeschäft?", WEISS),
               ("e4", ("tabler", "alert-triangle", 100, WEISS), "besondere Umstände?", WEISS),
               ("e5", ("tabler", "hourglass", 100, GELB), "Frist nötig", GELB)]),
    *paar("e1", "LE", [("e1", "ruhig"), ("e2", "denkt"), ("e5", "froh")], "OT",
          [("e1", "ruhig"), ("e2f", "froh"), ("e5", "sorge")]),
]))

# ===========================================================================================================================
# I I. 5. Kein Ausschluss, § 323 Abs. 5, 6
# ===========================================================================================================================
folie([("a1", "I. 5. Kein Ausschluss › § 323 Abs. 5, 6 BGB")], rechts_frei([
    *tafel("a1", "5. Kein Ausschluss"),
    z("Abs. 5 Satz 1: nach einer Teilleistung", 110, 190, "a2", "Bold", 34),
    z("vom ganzen Vertrag nur ohne Interesse an ihr", 150, 240, beim("a2", "ganzen"), size=34),
    z("Abs. 5 Satz 2: Schlechtleistung, unerhebliche", 110, 310, "a2b", "Bold", 34),
    z("Pflichtverletzung schließt den Rücktritt aus", 150, 360, beim("a2b", "Pflichtverletzung"), size=34),
    z("Abs. 6: Gläubiger allein oder weit", 110, 430, "a3", "Bold", 34),
    z("überwiegend verantwortlich", 150, 480, beim("a3", "überwiegend"), size=34),
    linienzug([(110, 555), (1150, 555)], "a4", breite=3),
    *neinz("Ottmar hat gar nichts geliefert", 580, beim("a4", "Ottmar"), "Bold", 36, x=160),
    *neinz("Leni trifft keine Verantwortung", 645, beim("a4", "Leni"), "Bold", 36, x=160),
    blk(110, 735, 1040, 80, GRUEN, beim("a4", "Verantwortung"), [("kein Ausschluss", "ExtraBold", 38, INK)]),
    *requisit([("a1", ("tabler", "ban", 100, WEISS), "Ausschluss?", WEISS),
               ("a2", ("tabler", "package", 100, WEISS), "Teilleistung?", WEISS),
               ("a3", ("tabler", "user-exclamation", 100, WEISS), "Gläubiger verantwortlich?", WEISS),
               ("a4", ("tabler", "check", 100, GRUEN), "kein Ausschluss", GRUEN)]),
    *paar("a1", "LE", [("a1", "ruhig"), ("a3", "denkt"), ("a4", "froh")], "OT", [("a1", "ruhig"), ("a4", "sorge")]),
]))

# ===========================================================================================================================
# J Typischer Klausurfehler: kein Vertretenmüssen, kein Verzug
# ===========================================================================================================================
folie([("vm1", "I. Rücktrittsrecht › kein Vertretenmüssen")], rechts_frei([
    *tafel("vm1", "Typischer Klausurfehler"),
    blk(110, 180, 1040, 80, HELLROT, "vm1", [("Vertretenmüssen prüfen", "ExtraBold", 38, INK)]),
    *neinz("§ 323 BGB verlangt es nicht", 300, "vm2", "Bold", 36, x=160),
    zit("BT-Drucks. 14/6040, S. 93, 184", 160, 355, beim("vm2", "nicht")),
    z("Vertretenmüssen gehört zum Schadensersatz", 160, 415, "vm3", size=34),
    z("statt der Leistung: §§ 281, 280 Abs. 1 BGB", 160, 465, beim("vm3", "statt"), size=34),
    *neinz("auch kein Verzug nötig", 540, "vm4", "Bold", 36, x=160),
    blk(110, 610, 1040, 80, LILA, beim("vm4", "den"), [("Mehr dazu: Video „Schuldnerverzug“", "ExtraBold", 34, INK)]),
    *okz("Wer schuld ist, spielt keine Rolle", 730, beim("vm5", "spielt"), "Bold", 36, x=160),
    *requisit([("vm1", ("tabler", "alert-triangle", 100, ROT), "Klausurfehler", ROT),
               ("vm3", ("tabler", "scale", 100, WEISS), "nur Schadensersatz", WEISS),
               ("vm5", ("tabler", "truck-delivery", 100, WEISS), "Lieferant egal", WEISS)]),
    *paar("vm1", "LE", [("vm1", "ruhig"), ("vm5", "froh")], "OT", [("vm1", "ruhig"), ("vm2", "staunt"), ("vm5", "sorge")]),
]))

# ===========================================================================================================================
# K II. Rücktrittserklärung, § 349 (Wortlaut)
# ===========================================================================================================================
W349 = ["„Der Rücktritt erfolgt durch Erklärung gegenüber",
        "dem anderen Teil.“"]
w349, w349_y = wortlaut(80, 180, 1100, W349, "§ 349 BGB", beim("r1", "Paragraf"), marken=[
    (0, "durch Erklärung", beim("r1", "Erklärung")), (1, "dem anderen Teil", beim("r1", "anderen"))], size=36)
folie([("r1", "II. Rücktrittserklärung › § 349 BGB"), ("r2", "II. Rücktrittserklärung › der Fall")], rechts_frei([
    *tafel("r1", "II. Rücktrittserklärung"),
    *w349,
    *okz("E-Mail von Leni an Ottmar, 30.7.2026", w349_y + 60, beim("r2", "E-Mail"), "Bold", 36, x=160),
    blk(110, w349_y + 150, 1040, 80, GELB, beim("r2", "genügt"), [("Erklärung wirksam", "ExtraBold", 38, INK)]),
    *requisit([("r1", ("tabler", "mail", 100, WEISS), "Erklärung", WEISS),
               ("r2", ("tabler", "mail", 100, GELB), "E-Mail vom 30.7.", GELB)]),
    *paar("r1", "LE", [("r1", "ruhig"), ("r2", "froh")], "OT", [("r1", "ruhig"), ("r2", "sorge")]),
]))

# ===========================================================================================================================
# L III. Rechtsfolge, § 346 Abs. 1
# ===========================================================================================================================
folie([("rf1", "III. Rechtsfolge › § 346 Abs. 1 BGB")], rechts_frei([
    *tafel("rf1", "III. Rechtsfolge"),
    z("§ 346 Abs. 1 BGB:", 110, 190, beim("rf1", "Paragraf"), "Bold", 36),
    z("empfangene Leistungen zurückgewähren", 110, 245, beim("rf1", "empfangenen"), "Bold", 36),
    *okz("Ottmar: 499 € zurückzahlen", 340, beim("rf2", "zurückzahlen"), "Bold", 38, x=160),
    *okz("Leni: hat nichts erhalten, gibt nichts zurück", 420, beim("rf3", "muss"), "Bold", 36, x=160),
    *requisit([("rf1", ("tabler", "arrow-back-up", 100, WEISS), "Rückgewähr", WEISS),
               ("rf2", ("tabler", "coin-euro", 100, GELB), "499 € zurück", GELB),
               ("rf3", ("tabler", "package-off", 100, WEISS), "nichts zurückzugeben", WEISS)]),
    *paar("rf1", "LE", [("rf1", "ruhig"), ("rf2", "froh")], "OT", [("rf1", "ruhig"), ("rf2", "sorge")]),
]))

# ===========================================================================================================================
# M Abgrenzung: § 326 Abs. 5, § 437 Nr. 2
# ===========================================================================================================================
folie([("ab1", "Abgrenzung › Unmöglichkeit, § 326 Abs. 5 BGB"), ("ab2", "Abgrenzung › Mangel, § 437 Nr. 2 BGB")],
      rechts_frei([
    *tafel("ab1", "Abgrenzung"),
    z("Leistung unmöglich: § 326 Abs. 5 BGB", 110, 190, beim("ab1", "Paragraf"), "Bold", 36),
    z("etwa: bestimmte gebrauchte Konsole verbrannt", 150, 245, beim("ab1", "etwa"), size=34),
    *okz("Rücktritt nach § 323 BGB, ohne Fristsetzung", 305, "ab1b", "Bold", 34, x=195),
    linienzug([(110, 400), (1150, 400)], "ab2", breite=3),
    z("mangelhafte Konsole: § 437 Nr. 2 BGB", 110, 430, beim("ab2", "mangelhaften"), "Bold", 36),
    *okz("§ 323 BGB mit Frist zur Nacherfüllung", 490, beim("ab2", "Frist"), "Bold", 34, x=195),
    *requisit([("ab1", ("tabler", "device-gamepad-2", 110, LILA), "unmöglich?", WEISS),
               (beim("ab1", "etwa"), ("tabler", "flame", 100, ROT), "verbrannt", ROT),
               ("ab2", ("tabler", "tool", 100, WEISS), "mangelhaft", WEISS)]),
    *paar("ab1", "LE", [("ab1", "ruhig"), ("ab2", "denkt")], "OT", [("ab1", "ruhig"), (beim("ab1", "etwa"), "staunt"),
                                                                    ("ab2", "denkt")]),
]))

# ===========================================================================================================================
# N Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Leni ist wirksam zurückgetreten", 200, beim("erg", "Leni"), "Bold", 38, x=160),
    *okz("Ottmar muss die 499 € zurückzahlen", 280, beim("erg2", "zurückzahlen"), "Bold", 38, x=160),
    zit("§§ 323 Abs. 1, 349, 346 Abs. 1 BGB", 160, 340, beim("erg2", "zurückzahlen")),
    *requisit([("erg", ("tabler", "scale", 100, GRUEN), "wirksam", GRUEN),
               ("erg2", ("tabler", "coin-euro", 100, GELB), "499 € zurück", GELB)]),
    *paar("erg", "LE", [("erg", "froh")], "OT", [("erg", "sorge")]),
]))

# ===========================================================================================================================
# O Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Frist in drei Schritten"), ("tipp2", "Klausurtipp · zu kurze Frist")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Frist in drei Schritten prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("1. gesetzt?", 240, 265, beim("tipp", "gesetzt"), size=36),
    z("2. angemessen?", 240, 320, beim("tipp", "angemessen"), size=36),
    z("3. erfolglos abgelaufen?", 240, 375, beim("tipp", "erfolglos"), size=36),
    linienzug([(130, 455), (1130, 455)], "tipp2", breite=3),
    z("Frist zu kurz?", 200, 485, "tipp2", "Bold", 36),
    z("Mit der angemessenen Frist weiterrechnen,", 200, 545, beim("tipp2", "rechne"), size=34),
    z("statt den Rücktritt abzulehnen.", 200, 595, beim("tipp2", "statt"), "Bold", 34),
    zit("BGH, Urt. v. 14.10.2020 – VIII ZR 318/19, Rn. 28", 200, 650, beim("tipp2", "abzulehnen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# P Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Rücktrittsrecht", "§ 323 Abs. 1 BGB", BLAU, 0),
          ("k11", "1.", "gegenseitiger Vertrag", "", None, 1),
          ("k12", "2.", "fällige, durchsetzbare Leistung nicht erbracht", "", None, 1),
          ("k13", "3.", "angemessene Frist erfolglos abgelaufen", "", None, 1),
          ("k14", "4.", "oder: Frist entbehrlich", "§ 323 Abs. 2", None, 1),
          ("k15", "5.", "kein Ausschluss", "§ 323 Abs. 5, 6", None, 1),
          ("k2", "II.", "Rücktrittserklärung", "§ 349 BGB", GELB, 0),
          ("k3", "III.", "Rückgewähr", "§ 346 Abs. 1 BGB", GRUEN, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Rücktritt, § 323 BGB"), 110, 90, "sch", 50)]
y = 200
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 92
    else:
        els_sch += [z(r, 270, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 330, y + 4, c, "Bold", 36, rechts=1820)]
        hh = 76
    if norm:
        els_sch.append(zit(norm, 1300, y + (18 if ebene == 0 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Rücktrittsrecht"), ("k2", "Klausurschema › II. Erklärung"),
       ("k3", "Klausurschema › III. Rückgewähr")], els_sch)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Rücktritt fragt nicht,", 0)], [("wer schuld ist.", "a")]],
                750, 290, 44, "merke", {"a": beim("merke", "wer")}),
    *markertext([[("Er braucht eine fällige", 0)], [("Leistung, die ausbleibt,", "b")]],
                750, 480, 42, "mk2", {"b": beim("mk2", "Leistung")}),
    *markertext([[("und eine Frist, die erfolglos abläuft,", "c")], [("oder einen Grund, warum sie entbehrlich ist.", 0)]],
                750, 670, 40, "mk3", {"c": beim("mk3", "Frist")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
