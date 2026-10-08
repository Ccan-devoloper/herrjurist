"""Folge 258 · Anwaltsklausur Aufbau: Gutachten, Zweckmäßigkeit, Schriftsatz – Serienstandard Open Peeps (Katzenkönig).
Fall: Frau Steinhoff hat einem Gartenbaubetrieb 3.000 € für eine Terrasse angezahlt (fertig Ende April laut E-Mail);
passiert ist nichts. In der Kanzlei: Referendarin Isolde und Rechtsanwalt Hohlfeld.
Szenen laut ../SZENENPLAN.md: A Kanzlei (Fall, Hook, Frage), B Sachverhalt, C1 Perspektivwechsel, C2 § 43a Abs. 3 BRAO
(Wortlautkarte), C3 § 43a Abs. 4/5 BRAO (Wortlautkarten), D Aufbau, E I. Gutachten (Wortlautkarte § 323 Abs. 1 BGB),
F II. Zweckmäßigkeit statt zweitem Gutachten, G Zweckmäßigkeit am Fall (sechs Punkte), H Ergebnis in der Kanzlei,
I III. Praktischer Teil, J1–J3 Kurzblick (Wortlautkarten § 253 Abs. 2 ZPO, § 81 Abs. 1 S. 1 VwGO, § 137 Abs. 1 S. 1 StPO),
K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/stehend als eigene Kopie aus Folge 222
(gemeinsame Dateien unverändert); neu: person() (Mimikfolge mit Redefenstern), neben(), kanzlei(), regal(), sachverhalt_258().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_258/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_258/" in n:
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
NAME = {"IS": "Isolde", "ST": "Frau Steinhoff", "HO": "Herr Hohlfeld"}
NFARBE = {"IS": ROT, "ST": LILA, "HO": BLAU}


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






# --- eigene Szenenbausteine Folge 258 --------------------------------------------------------------------------------------
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


def sachverhalt_258(cue, absaetze, fragen):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    for f_ in fragen:
        els.append(pille(glyphen(f_), 210, y + 6, cue, fill=PINK, size=36)); y += 76
    assert y + 10 <= 950, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)


def regal(x, y, w, cue):
    """Wandregal (programmatisch: Brett in Holzfarbe mit Tuschekontur)."""
    return feld(x, y, w, 18, cue, fill=HOLZ, rand=4, rund=4, name="regal")


# ===========================================================================================================================
# Kanzlei: Besprechungszimmer (A und H)
# ===========================================================================================================================
STX, ISX, HOX = 420, 1330, 1650
TISCH_X = 870
STa = ("ST_redet_r", STX, BODEN, FH)
ISa = ("IS_redet", ISX, BODEN, FH)
HOa = ("HO_redet", HOX, BODEN, FH)
STfa = ("ST_redetfroh_r", STX, BODEN, FH)
HOfa = ("HO_redetfroh", HOX, BODEN, FH)


def kanzlei(c, hart_=True):
    """Raum: Fenster, Wandregal mit Büchern, Pflanze, Besprechungstisch."""
    els = [boden(c, hart_),
           ficon("tabler", "window", 250, 360, 190, c, fuell=BLAUHELL, anim="cut"),
           regal(560, 470, 300, c),
           ficon("tabler", "books", 650, 472, 120, c, fuell=GELB, anim="cut"),
           ficon("tabler", "books", 775, 472, 100, c, fuell=GRUEN, anim="cut"),
           ficon("tabler", "plant-2", 110, BODEN - 2, 110, c, fuell=GRUEN, anim="cut"),
           ficon("tabler", "desk", TISCH_X, BODEN - 2, 380, c, fuell=HOLZ, anim="cut")]
    return [hart(e) if hart_ else e for e in els]


KTOP = ficon("tabler", "desk", TISCH_X, BODEN - 2, 380, NULL).y + 8          # Tischplatte (wie Folge 222)

# A Fall --------------------------------------------------------------------------------------------------------------------
auszug = ficon("tabler", "receipt-euro", TISCH_X - 60, KTOP + 6, 80, beim("steinhoff", "Kontoauszug"), fuell=WEISS)
bewegt(auszug, beim("steinhoff", "Kontoauszug"), (beim("steinhoff", "Kontoauszug")[0],
                                                     beim("steinhoff", "Kontoauszug")[1] + 0.35), 0, -120)
szene(auszug, "258auszug_1", gain=1.0, versatz=0.23)     # Transient (0,12 s) am Aufsetzen nach 0,35 s Fallbewegung
RB_ = (1080, 60, 760, 290)                               # Rückblick-Karte „Im Garten“ oben rechts (während Frau Steinhoff spricht)
folie([(NULL, "Fall · In der Kanzlei"), ("st2", "Fall · Was soll ich jetzt tun?"), ("hook", "Einstieg · Die Frage")], [
    *kanzlei(NULL),
    hart(pl("In einer Anwaltskanzlei", 70, 30, NULL, fill=GELB, size=40)),
    *person("ST", STX, BODEN, FH, [(NULL, "ruhig_r"), ("st1", "!redet_r"), ("ho1", "sorge_r"), ("hook", "ruhig_r")]),
    hart(fall_ns("ST", STX, NULL)),
    *person("IS", ISX, BODEN, FH, [("isolde", "ruhig"), (beim("st1b", "Passiert"), "denkt"), ("ho1", "liest"),
                                   ("hook", "ruhig")], erst="pop"),
    fall_ns("IS", ISX, "isolde", d=0.1),
    *person("HO", HOX, BODEN, FH, [("hohlfeld", "ruhig"), ("ho1", "!redet"), ("hook", "denkt")], erst="pop"),
    fall_ns("HO", HOX, "hohlfeld", d=0.1),
    auszug,
    pl("Kontoauszug", TISCH_X - 60, KTOP - 150, beim("steinhoff", "Kontoauszug", ende=True), fill=WEISS, size=28,
       anker="m", bis="hook"),
    # Rückblick: der Garten ohne Terrasse
    bis_(karte(*RB_, "st1", fill=HELL, rund=18, schatten=6, rand=4), "st2"),
    pl("im Garten", RB_[0] + 30, RB_[1] + 20, "st1", fill=GRUEN, size=28, bis="st2"),
    ficon("tabler", "fence", 1230, 325, 170, "st1", fuell=HOLZ, bis="st2"),
    ficon("tabler", "plant-2", 1370, 325, 80, "st1", fuell=GRUEN, bis="st2"),
    pl("Terrasse: fertig Ende April", 1640, 120, beim("st1", "Ende"), fill=GELB, size=28, anker="m", bis="st2"),
    ficon("tabler", "calendar-x", 1540, 325, 80, beim("st1b", "Passiert"), fuell=WEISS, bis="st2"),
    pl("nichts passiert", 1715, 255, beim("st1b", "nichts"), fill=ROT, size=28, anker="m", bis="st2"),
    blase("sprech", 820, 230, "st1", 640, 200, inhalt=["Ich habe dem Gartenbaubetrieb", "3.000 € angezahlt. Ende April",
                                                       "sollte meine Terrasse fertig sein."], textsize=32, figur=STa,
          bis="st1b"),
    blase("sprech", 520, 150, "st1b", 560, 220, inhalt=["Passiert ist nichts."], textsize=34, figur=STa, bis="st2"),
    blase("sprech", 640, 190, "st2", 620, 210, inhalt=["Ich will mein Geld zurück.", "Was soll ich jetzt tun?"],
          textsize=36, figur=STa, bis="ho1"),
    blase("sprech", 860, 230, "ho1", 1250, 190, inhalt=["Sie schreiben das Gutachten, Isolde.",
                                                        "Und am Ende steht ein Vorschlag,", "was wir tun."], textsize=32,
          figur=HOa, bis="hook"),
    pl("Die Mandantin will nicht wissen, wer recht hat,", 960, 120, "hook", fill=WEISS, size=36, anker="m", bis="frage"),
    pl("sondern was sie jetzt konkret tun soll.", 960, 200, beim("hook", "sondern"), fill=GELB, size=36, anker="m",
       bis="frage"),
    pl("Genau das verlangt die Anwaltsklausur.", 960, 280, "hook2", fill=WEISS, size=32, anker="m", bis="frage"),
    pl("Wie baust du die Anwaltsklausur auf,", 960, 120, "frage", fill=PINK, size=38, anker="m"),
    pl("und was unterscheidet echte Zweckmäßigkeit von einem zweiten Gutachten?", 960, 205, "frage2", fill=PINK, size=34,
       anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_258("sv", [
    "Frau Steinhoff hat einem Gartenbaubetrieb für eine neue Terrasse 3.000 € angezahlt. Fertig sein sollte die Terrasse "
    "Ende April; das steht in einer E-Mail. Die Zahlung belegt ihr Kontoauszug. Passiert ist nichts. Eine Frist hat sie "
    "dem Betrieb noch nicht gesetzt.",
    "In der Kanzlei sagt sie: „Ich will mein Geld zurück. Was soll ich jetzt tun?“ Rechtsanwalt Hohlfeld zur "
    "Referendarin: „Sie schreiben das Gutachten, Isolde. Und am Ende steht ein Vorschlag, was wir tun.“",
], ["Wie baust du die Anwaltsklausur auf,", "und was ist echte Zweckmäßigkeit statt eines zweiten Gutachtens?"])

# ===========================================================================================================================
# C1 Perspektivwechsel: Richter oder Anwalt – parteiisch, aber nicht grenzenlos
# ===========================================================================================================================
X1s = ("ST_redet_r", X1, FB, FR)
X2s = ("IS_redet", X2, FB, FR)
folie([("pers", "Perspektivwechsel · Richter oder Anwalt"), ("partei", "Perspektivwechsel › parteiisch, aber gebunden")],
      rechts_frei([
    *tafel("pers", "Perspektivwechsel"),
    blk(110, 190, 500, 200, BLAUHELL, "richter", [("Als Richter:", "Bold", 30, INK), ("Wer hat recht?", "ExtraBold", 36, INK)],
        rund=18),
    blk(650, 190, 500, 200, HELL, "anwalt", [("Als Anwalt:", "Bold", 30, INK), ("Was nützt meiner", "ExtraBold", 34, INK),
                                            ("Mandantin?", "ExtraBold", 34, INK)], rund=18),
    pl("parteiisch", 110, 470, "partei", fill=GELB, size=34),
    pl("aber nicht grenzenlos", 360, 470, "grenze", fill=ROT, size=34),
    z("„Schreiben Sie ruhig, der Betrieb ist ein Betrüger.“", 110, 590, "st3", "Regular", 30),
    *okz("Wir bleiben sachlich.", 660, beim("is1", "sachlich"), "Bold", 32, x=160),
    *okz("Wir schreiben nur, was stimmt.", 720, beim("is1", "stimmt"), "Bold", 32, x=160),
    *neben("ST", X1, [("pers", "ruhig_r"), ("partei", "aerger_r"), ("st3", "!redet_r"), ("is1", "sorge_r")]),
    *neben("IS", X2, [("pers", "ruhig"), ("anwalt", "denkt"), ("is1", "!redet")], bis="w43"),
    blase("sprech", 560, 230, "st3", 1560, 190, inhalt=["Schreiben Sie ruhig,", "der Betrieb ist", "ein Betrüger."],
          textsize=32, figur=X1s, bis="is1"),
    blase("sprech", 560, 200, "is1", 1580, 190, inhalt=["Wir bleiben sachlich.", "Und wir schreiben nur,", "was stimmt."],
          textsize=32, figur=X2s),
]))

# ===========================================================================================================================
# C2 § 43a Abs. 3 BRAO: Sachlichkeit (Wortlautkarte)
# ===========================================================================================================================
W43_3 = ("„Der Rechtsanwalt darf sich bei seiner Berufsausübung nicht unsachlich verhalten. Unsachlich ist insbesondere ein "
         "Verhalten, bei dem es sich um die bewußte Verbreitung von Unwahrheiten oder solche herabsetzenden Äußerungen "
         "handelt, zu denen andere Beteiligte oder der Verfahrensverlauf keinen Anlaß gegeben haben.“")
w3, w3_y = wortlaut(110, 180, 1040, W43_3, "§ 43a Abs. 3 BRAO", "w43", marken=[
    ("unsachlich", beim("sach", "unsachlich")), ("Unwahrheiten", beim("unw", "Unwahrheiten")),
    ("herabsetzenden", beim("herab", "herabsetzen"))], size=30)
Y3 = w3_y + 30
folie([("w43", "§ 43a Abs. 3 BRAO › Sachlichkeit")], rechts_frei([
    *tafel("w43", "Parteiisch, aber sachlich"),
    *w3,
    *okz("nicht unsachlich verhalten", Y3, "sach", "Bold", 32),
    *okz("keine Unwahrheiten bewusst verbreiten", Y3 + 60, "unw", "Bold", 32),
    *okz("niemanden ohne Anlass herabsetzen", Y3 + 120, "herab", "Bold", 32),
    *neben("IS", FX, [("w43", "liest"), ("herab", "froh")], erst="cut"),
    *requisit([("w43", ("tabler", "scale", 120, WEISS), "Sachlichkeit", BLAU)]),
]))
assert Y3 + 120 + 50 <= 895, Y3

# ===========================================================================================================================
# C3 § 43a Abs. 4, 5 BRAO: widerstreitende Interessen, auch für Referendare (Wortlautkarten)
# ===========================================================================================================================
W43_4 = ("„Der Rechtsanwalt darf nicht tätig werden, wenn er einen anderen Mandanten in derselben Rechtssache bereits im "
         "widerstreitenden Interesse beraten oder vertreten hat.“")
W43_5 = ("„Absatz 4 Satz 1 gilt entsprechend für die Tätigkeit als Referendar im Vorbereitungsdienst im Rahmen der "
         "Ausbildung bei einem Rechtsanwalt.“")
w4, w4_y = wortlaut(110, 180, 1040, W43_4, "§ 43a Abs. 4 S. 1 BRAO", "abs4", marken=[
    ("derselben Rechtssache", beim("abs4", "derselben")), ("widerstreitenden", beim("abs4", "widerstreitenden")),
    ("nicht tätig werden", beim("abs4", "tätig"))], size=30)
w5, w5_y = wortlaut(110, w4_y + 40, 1040, W43_5, "§ 43a Abs. 5 S. 1 BRAO", "abs5", marken=[
    ("Referendar", beim("abs5", "Referendare"))], size=30)
folie([("abs4", "§ 43a Abs. 4 BRAO › widerstreitende Interessen"), ("abs5", "§ 43a Abs. 5 BRAO › auch für Referendare")],
      rechts_frei([
    *tafel("abs4", "Keine widerstreitenden Interessen"),
    *w4, *w5,
    pl("auch für Referendare in der Anwaltsstation", 110, w5_y + 30, beim("abs5", "Anwaltsstation"), fill=GELB, size=30),
    *neben("IS", FX, [("abs4", "denkt"), ("abs5", "liest"), (beim("abs5", "Anwaltsstation"), "froh")], erst="cut"),
    *requisit([("abs4", ("tabler", "users", 120, WEISS), "derselbe Fall", WEISS),
               ("abs5", ("tabler", "school", 120, WEISS), "Referendare", GELB)]),
]))
assert w5_y + 30 + 70 <= 895, w5_y

# ===========================================================================================================================
# D Aufbau: vorweg Mandantenbegehren, dann drei Stufen
# ===========================================================================================================================
STUFEN = [("stufe1", "I.", "Gutachten", "materielle und prozessuale Lage", BLAU),
          ("stufe2", "II.", "Zweckmäßigkeit", "Welcher Weg führt am besten zum Ziel?", GELB),
          ("stufe3", "III.", "Praktischer Teil", "was du tatsächlich entwirfst", GRUEN)]
els_st = []
for i, (c, r, t, u, farbe) in enumerate(STUFEN):
    y = 430 + i * 90
    x = 110 + i * 40
    els_st += [karte(x, y, 90, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
               zm(r, x + 45, y + 12, c, "ExtraBold", 34),
               z(t, x + 115, y + 12, c, "ExtraBold", 34),
               z(u, x + 115 + F("ExtraBold", 34).getlength(t) + 24, y + 16, beim(c, u.split()[0]), "Regular", 28)]
folie([("auf", "Aufbau · in der Regel drei Stufen"), ("begehr", "Aufbau › vorweg: das Mandantenbegehren"),
       ("stufe1", "Aufbau › I. Gutachten, II. Zweckmäßigkeit, III. Praktischer Teil"),
       ("bv", "Aufbau › der Bearbeitervermerk entscheidet")], rechts_frei([
    *tafel("auf", "Aufbau der Anwaltsklausur"),
    z("in der Regel 3 Stufen, davor 1 Frage", 110, 172, beim("auf", "Regel"), "Bold", 32),
    blk(110, 225, 1040, 80, HELLROT, "begehr", [("Vorweg: Was will die Mandantin erreichen?", "ExtraBold", 32, INK)]),
    z("Frau Steinhoff: Geld zurück,", 150, 320, "begehr2", "Bold", 30),
    z("keine Terrasse mehr von diesem Betrieb", 150, 362, beim("begehr2", "keine"), "Bold", 30),
    *els_st,
    z("Wie die Teile heißen und was entfällt:", 110, 725, "bv", "Bold", 32),
    z("der Bearbeitervermerk", 110, 770, beim("bv", "Bearbeitervermerk"), "ExtraBold", 32),
    pl("Bearbeitervermerk lesen: Folge 222", 650, 768, "f222", fill=GELB, size=28),
    *neben("ST", X1, [("auf", "ruhig"), ("begehr2", "sorge")]),
    *neben("IS", X2, [("auf", "ruhig"), ("begehr", "denkt"), ("stufe1", "schreibt"), ("f222", "froh")]),
    pl("Geld zurück", X1, PY, "begehr2", fill=HELLROT, size=30, anker="m"),
]))

# ===========================================================================================================================
# E I. Gutachten am Fall: § 346, § 323 BGB (Wortlautkarte), prozessual Amtsgericht
# ===========================================================================================================================
W323 = ("„Erbringt bei einem gegenseitigen Vertrag der Schuldner eine fällige Leistung nicht oder nicht vertragsgemäß, so "
        "kann der Gläubiger, wenn er dem Schuldner erfolglos eine angemessene Frist zur Leistung oder Nacherfüllung "
        "bestimmt hat, vom Vertrag zurücktreten.“")
w323, w323_y = wortlaut(110, 255, 1040, W323, "§ 323 Abs. 1 BGB", "w323", marken=[
    ("fällige Leistung", beim("w323", "fällige")), ("nicht", beim("w323", "nicht")), ("erfolglos", beim("fr", "erfolglos")),
    ("angemessene Frist", beim("fr", "angemessene"))], size=28)
GY = w323_y + 22
folie([("gut", "I. Gutachten › materiell: Rücktritt"), ("proz", "I. Gutachten › prozessual"),
       ("vorb", "I. Gutachten › bereitet die Maßnahme vor")], rechts_frei([
    *tafel("gut", "I. Gutachten bei Frau Steinhoff"),
    z("materiell: 3.000 € zurück nach einem Rücktritt", 110, 175, "mat", "Bold", 32),
    zit("§ 346 Abs. 1 BGB", 110, 215, beim("mat", "Paragraf")),
    *w323,
    *neinz("Eine Frist hat Frau Steinhoff noch nicht gesetzt.", GY, "noch", "Bold", 30, x=160),
    z("prozessual: Klage über 3.000 € beim Amtsgericht", 110, GY + 62, "proz", "Bold", 30),
    zit("§ 23 Nr. 1 GVG", 110, GY + 102, "proz"),
    blk(110, GY + 150, 1040, 80, HELL, beim("vorb", "bereitet"), [("Das Gutachten bereitet die Maßnahme vor.", "ExtraBold", 32, INK)]),
    *neben("IS", FX, [("gut", "liest"), ("noch", "denkt"), ("proz", "schreibt"), ("vorb", "froh")], erst="cut"),
    *requisit([("mat", ("tabler", "coin-euro", 110, GELB), "3.000 € zurück", GELB),
               ("w323", ("tabler", "hourglass", 100, WEISS), "Frist?", WEISS),
               ("proz", ("tabler", "building-bank", 120, WEISS), "Amtsgericht", BLAU)]),
]))
assert GY + 230 <= 895, GY

# ===========================================================================================================================
# F II. Zweckmäßigkeit: kein zweites Gutachten
# ===========================================================================================================================
folie([("zw", "II. Zweckmäßigkeit › kein zweites Gutachten"), ("echt", "II. Zweckmäßigkeit › sicher, schnell, kostengünstig")],
      rechts_frei([
    *tafel("zw", "II. Zweckmäßigkeit"),
    z("Hier lauert eine Falle:", 110, 175, beim("zw", "Hier"), "Bold", 32),
    feld(110, 240, 500, 330, "zw2", fill=HELLROT, anim="pop", name="spalte_falle"),
    zm("das zweite Gutachten", 360, 260, "zw2", "ExtraBold", 32),
    zm("Du prüfst noch einmal:", 360, 340, beim("zw2", "Du"), "Bold", 30),
    zm("Besteht der Anspruch?", 360, 390, beim("zw2", "Anspruch"), "Bold", 30),
    bis_(nein(360, 490, beim("zw2", "Anspruch", ende=True), gr=30), None),
    feld(650, 240, 500, 330, "echt", fill=HELLGRUEN, anim="pop", name="spalte_echt"),
    zm("echte Zweckmäßigkeit", 900, 260, "echt", "ExtraBold", 32),
    zm("Welcher Weg bringt das Geld", 900, 330, beim("echt", "Welcher"), "Bold", 30),
    zm("am sichersten,", 900, 380, beim("echt", "sichersten"), "Bold", 30),
    zm("schnellsten,", 900, 425, beim("echt", "schnellsten"), "Bold", 30),
    zm("kostengünstigsten zurück?", 900, 470, beim("echt", "kostengünstigsten"), "Bold", 30),
    ok(900, 535, beim("echt", "kostengünstigsten", ende=True), gr=26),
    blk(110, 620, 1040, 80, GELB, "vor", [("Widerspricht sich das: Sicherheit geht vor.", "ExtraBold", 34, INK)]),
    *neben("IS", FX, [("zw", "denkt"), ("echt", "schreibt"), ("vor", "froh")], erst="cut"),
    *requisit([("zw", ("tabler", "alert-triangle", 110, GELB), "Falle", ROT),
               ("echt", ("tabler", "route", 110, WEISS), "der beste Weg", GRUEN)]),
]))

# ===========================================================================================================================
# G II. Zweckmäßigkeit am Fall: sechs Punkte
# ===========================================================================================================================
REIHEN_Z = [("t1", "Zeit", BLAU, ["Klage sofort: am schnellsten"], None),
            ("t2", "Kosten", GELB, ["ohne Frist droht die Abweisung,", "dann trägt Frau Steinhoff die Kosten"], "§ 91 Abs. 1 ZPO"),
            ("t3", "Beweisbarkeit", GRUEN, ["Zahlung: Kontoauszug", "Termin Ende April: E-Mail"], None),
            ("t4", "Vergleich", LILA, ["vielleicht Zahlung auf ein klares", "Schreiben, notfalls in Raten"], None),
            ("t5", "Eilrechtsschutz", HELLROT, ["Arrest nur, wenn sonst die Vollstreckung", "vereitelt oder wesentlich erschwert würde"],
             "§ 917 Abs. 1 ZPO"),
            ("t6", "sicherster Weg", ORANGE, ["Frist setzen, schriftlich und nachweisbar,", "dann zurücktreten, notfalls klagen"],
             None)]
els_z = []
y = 170
for c, lab, farbe, zeilen, fund in REIHEN_Z:
    els_z.append(blk(110, y, 250, 84, farbe, c, [(lab, "ExtraBold", 28 if len(lab) > 10 else 30, INK)] +
                     ([(fund, "Regular", 26, INK)] if fund else []), rund=12, rand=4, anim="pop"))
    for i, t in enumerate(zeilen):
        cc = c if i == 0 else beim(c, t.split()[0].strip(","))
        els_z.append(z(t, 385, y + 4 + i * 40, cc, "Bold" if c != "t6" else "ExtraBold", 28))
    y += 100
els_z += [ok(1120, 400, beim("t3", "E-Mail", ende=True), gr=20), nein(1120, 600, beim("t5", "nichts"), gr=20),
          pl("Jeder Punkt: Fallbezug und Entscheidung", 110, 790, "t7", fill=PINK, size=30),
          pl("nicht: zweites Gutachten", 760, 790, beim("t7", "Unterschied"), fill=WEISS, size=28)]
folie([("t1", "II. Zweckmäßigkeit › Zeit"), ("t2", "II. Zweckmäßigkeit › Kosten, § 91 ZPO"),
       ("t3", "II. Zweckmäßigkeit › Beweisbarkeit"), ("t4", "II. Zweckmäßigkeit › Vergleich"),
       ("t5", "II. Zweckmäßigkeit › Eilrechtsschutz, § 917 ZPO"), ("t6", "II. Zweckmäßigkeit › der sicherste Weg"),
       ("t7", "II. Zweckmäßigkeit › Fallbezug statt zweitem Gutachten")], rechts_frei([
    *tafel("t1", "II. Zweckmäßigkeit bei Frau Steinhoff"),
    *els_z,
    *neben("IS", FX, [("t1", "denkt"), ("t3", "schreibt"), ("t5", "denkt"), ("t6", "froh")]),
    *requisit([("t1", ("tabler", "clock", 110, WEISS), "Zeit", BLAU),
               ("t2", ("tabler", "coin-euro", 110, GELB), "Kosten", GELB),
               ("t3", ("tabler", "receipt-euro", 90, WEISS), "Beweise", GRUEN),
               ("t4", ("ph", "handshake", 120, WEISS), "Vergleich", LILA),
               ("t5", ("tabler", "lock", 100, WEISS), "Arrest?", HELLROT),
               ("t6", ("tabler", "route", 110, WEISS), "sicherster Weg", ORANGE)]),
]))

# ===========================================================================================================================
# H Ergebnis in der Kanzlei (Rückkehr: Die Beratung aus A schließt dort)
# ===========================================================================================================================
folie([("is2", "Ergebnis · der Plan für Frau Steinhoff")], [
    *kanzlei("is2", hart_=False),
    pl("Zurück in der Kanzlei", 70, 30, "is2", fill=GELB, size=40),
    *person("ST", STX, BODEN, FH, [("is2", "ruhig_r"), ("st4", "!redetfroh_r"), ("ho2", "froh_r")], erst="pop"),
    fall_ns("ST", STX, "is2", d=0.1),
    *person("IS", ISX, BODEN, FH, [("is2", "!redet"), ("st4", "froh")], erst="pop"),
    fall_ns("IS", ISX, "is2", d=0.1),
    *person("HO", HOX, BODEN, FH, [("is2", "ruhig"), ("ho2", "!redetfroh")], bis="prak", erst="pop"),
    fall_ns("HO", HOX, "is2", d=0.1),
    ficon("tabler", "mail", TISCH_X, KTOP + 4, 90, beim("is2", "Frist"), fuell=WEISS),
    pl("Frist", TISCH_X, KTOP - 128, beim("is2", "Frist"), fill=GELB, size=28, anker="m"),
    blase("sprech", 900, 240, "is2", 860, 190, inhalt=["Wir setzen dem Betrieb jetzt schriftlich eine Frist.",
                                                       "Verstreicht sie, treten wir vom Vertrag zurück",
                                                       "und verlangen die 3.000 €."], textsize=30, figur=ISa, bis="st4"),
    blase("sprech", 440, 150, "st4", 560, 220, inhalt=["Endlich ein Plan."], textsize=36, figur=STfa, bis="ho2"),
    blase("sprech", 560, 170, "ho2", 1300, 200, inhalt=["Genau so.", "Das ist Zweckmäßigkeit."], textsize=34, figur=HOfa),
])

# ===========================================================================================================================
# I III. Praktischer Teil: je nach Bearbeitervermerk
# ===========================================================================================================================
PT = [("p1", "Schriftsatz", "an das Gericht", ("tabler", "file-text", 80, WEISS)),
      ("p2", "Schreiben", "an die Mandantin", ("tabler", "mail", 80, WEISS)),
      ("p3", "Vertragsentwurf", "", ("tabler", "file-pencil", 80, WEISS))]
els_p = []
for i, (c, t1, t2, ic) in enumerate(PT):
    x = 110 + i * 350
    els_p += [feld(x, 260, 330, 190, c, fill=BLAUHELL, anim="pop", name="block"),
              dicon(ic[0], ic[1], x + 165, 345, ic[2], c, fuell=ic[3]),
              zm(t1, x + 165, 360, c, "ExtraBold", 30)]
    if t2:
        els_p.append(zm(t2, x + 165, 400, c, "Regular", 26))
folie([("prak", "III. Praktischer Teil › je nach Bearbeitervermerk"), ("pf", "III. Praktischer Teil › bei Frau Steinhoff")],
      rechts_frei([
    *tafel("prak", "III. Praktischer Teil"),
    z("Was du entwirfst, steht im Bearbeitervermerk:", 110, 180, "je", "Bold", 32),
    *els_p,
    z("Bei Frau Steinhoff: 2 Schreiben", 110, 490, "pf", "ExtraBold", 32),
    blk(110, 550, 500, 100, HELL, "pf1", [("1. Fristsetzung", "ExtraBold", 30, INK), ("an den Betrieb", "Bold", 28, INK)]),
    blk(650, 550, 500, 100, HELL, "pf2", [("2. Brief an Frau Steinhoff", "ExtraBold", 30, INK),
                                         ("in verständlicher Sprache", "Bold", 28, INK)]),
    z("Hinweis im Brief: Innerhalb der Frist", 110, 690, "pf3", "Bold", 30),
    z("kann der Betrieb noch bauen.", 110, 735, beim("pf3", "noch"), "Bold", 30),
    *neben("IS", FX, [("prak", "ruhig"), ("pf", "schreibt"), ("pf3", "denkt")], erst="pop"),
    *requisit([("prak", ("tabler", "file-description", 100, WEISS), "Bearbeitervermerk", BLAU),
               ("pf1", ("tabler", "mail", 110, WEISS), "Frist", GELB),
               ("pf2", ("tabler", "mail-opened", 110, WEISS), "Brief", WEISS)]),
]))

# ===========================================================================================================================
# J1–J3 Kurzblick: Zivilrecht, Öffentliches Recht, Strafrecht (Wortlautkarten)
# ===========================================================================================================================
W253 = ("„Die Klageschrift muss enthalten: 1. die Bezeichnung der Parteien und des Gerichts; 2. die bestimmte Angabe des "
        "Gegenstandes und des Grundes des erhobenen Anspruchs, sowie einen bestimmten Antrag.“")
w253, w253_y = wortlaut(110, 330, 1040, W253, "§ 253 Abs. 2 ZPO", "zr", marken=[
    ("Parteien", beim("zr", "Parteien")), ("Gerichts", beim("zr", "Gericht")), ("Gegenstandes", beim("zr", "Gegenstand")),
    ("Grundes", beim("zr", "Grund")), ("bestimmten Antrag", beim("zr", "bestimmten"))], size=30)
folie([("drei", "Kurzblick · alle drei Rechtsgebiete"), ("zr", "Kurzblick › Zivilrecht: Klageschrift, § 253 ZPO")],
      rechts_frei([
    *tafel("drei", "Kurzblick: drei Rechtsgebiete"),
    z("Der Aufbau trägt in allen drei Rechtsgebieten.", 110, 175, "drei", "Bold", 32),
    z("Anders ist vor allem der praktische Teil.", 110, 222, beim("drei", "Anders"), "Bold", 32),
    pl("Zivilrecht: eine Klageschrift", 110, 270, "zr", fill=BLAU, size=30),
    *w253,
    *neben("IS", FX, [("drei", "ruhig"), ("zr", "liest")], erst="pop"),
    *requisit([("drei", ("tabler", "list-check", 110, WEISS), "3 Rechtsgebiete", WEISS),
               ("zr", ("tabler", "file-text", 100, WEISS), "Klageschrift", BLAU)]),
]))
assert w253_y <= 895

W81 = "„Die Klage ist bei dem Gericht schriftlich zu erheben.“"
w81, w81_y = wortlaut(110, 330, 1040, W81, "§ 81 Abs. 1 S. 1 VwGO", beim("oer", "Klage", nr=2), marken=[
    ("schriftlich", beim("oer", "schriftlich"))], size=32)
q1 = pl("Widerspruch", 150, 240, beim("oer", "Widerspruch"), fill=GELB, size=30)
q2 = pl("Klage", q1.x + q1.sprite.width + 20, 240, beim("oer", "Klage"), fill=GRUEN, size=30)
q3 = pl("Eilantrag", q2.x + q2.sprite.width + 20, 240, beim("oer", "Eilantrag"), fill=ROT, size=30)
folie([("oer", "Kurzblick › Öffentliches Recht: § 81 VwGO")], rechts_frei([
    *tafel("oer", "Öffentliches Recht"),
    z("gegen einen Bescheid, etwa:", 110, 175, "oer", "Bold", 32),
    q1, q2, q3,
    *w81,
    *neben("IS", FX, [("oer", "liest"), (beim("oer", "schriftlich"), "schreibt")], erst="pop"),
    *requisit([("oer", ("tabler", "building-bank", 120, WEISS), "Behörde", GRUEN)]),
]))

W137 = "„Der Beschuldigte kann sich in jeder Lage des Verfahrens des Beistandes eines Verteidigers bedienen.“"
w137, w137_y = wortlaut(110, 250, 1040, W137, "§ 137 Abs. 1 S. 1 StPO", beim("sr", "Beschuldigte"), marken=[
    ("in jeder Lage des Verfahrens", beim("sr", "jeder")), ("Verteidigers", beim("sr", "Verteidigers"))], size=32)
folie([("sr", "Kurzblick › Strafrecht: Verteidiger, § 137 StPO"), ("rev", "Kurzblick › Strafrecht: Revisionsklausur")],
      rechts_frei([
    *tafel("sr", "Strafrecht"),
    z("Du bist Verteidiger.", 110, 175, "sr", "ExtraBold", 34),
    *w137,
    blk(110, w137_y + 40, 1040, 100, HELL, "rev", [("Revisionsklausur: auch dort kann auf das", "Bold", 30, INK),
                                                  ("Gutachten die Zweckmäßigkeit folgen.", "Bold", 30, INK)]),
    pl("Die Sicht der Staatsanwaltschaft: Folge 39", 110, w137_y + 180, "f39", fill=GELB, size=28),
    *neben("IS", FX, [("sr", "liest"), ("rev", "denkt"), ("f39", "froh")], erst="pop"),
    *requisit([("sr", ("tabler", "briefcase", 110, GELB), "Verteidigung", ROT),
               ("rev", ("tabler", "file-search", 100, WEISS), "Revision", WEISS)]),
]))
assert w137_y + 250 <= 895, w137_y

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Zeit für den praktischen Teil")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Plane genug Zeit für den", 200, 200, beim("tipp", "Plane"), "Bold", 36),
    z("praktischen Teil ein.", 200, 255, beim("tipp", "praktischen"), "ExtraBold", 38),
    z("Fehlt er, fehlt ein großer Teil der Leistung.", 200, 330, beim("tipp", "Fehlt"), "Bold", 32),
    z("Der Schriftsatz widerspricht dem Gutachten nicht:", 200, 450, "tipp2", "Bold", 34),
    z("dieselben Gründe, dieselben Beweise", 200, 505, beim("tipp2", "dieselben"), "ExtraBold", 36),
    dicon("tabler", "hourglass", 400, 760, 130, beim("tipp", "Plane"), fuell=GELB),
    dicon("tabler", "equal", 800, 760, 130, beim("tipp2", "dieselben"), fuell=WEISS),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k0", "", "Vorweg: das Mandantenbegehren", HELLROT, 0),
          ("k1", "I.", "Gutachten", BLAU, 0),
          ("k1a", "", "materielle und prozessuale Lage", None, 1),
          ("k2", "II.", "Zweckmäßigkeit", GELB, 0),
          ("k2a", "", "sicher, schnell und kostengünstig, am Fall begründet", None, 1),
          ("k3", "III.", "Praktischer Teil", GRUEN, 0),
          ("k3a", "", "je nach Bearbeitervermerk: Schriftsatz, Mandantenschreiben", None, 1),
          (beim("k3a", "Vertragsentwurf"), "", "oder Vertragsentwurf", None, 2)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Anwaltsklausur"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0 and not r:
        els_sch += [karte(110, y, 900, 66, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(txt, 135, y + 9, c, "ExtraBold", 36, rechts=1820)]
        y += 92
    elif ebene == 0:
        els_sch += [karte(110, y, 110, 66, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 36).getlength(r) / 2, y + 9, c, "ExtraBold", 36, rechts=1820),
                    z(txt, 255, y + 9, c, "ExtraBold", 36, rechts=1820)]
        y += 92
    elif ebene == 1:
        els_sch.append(z(txt, 330, y, c, "Bold", 34, rechts=1820))
        els_sch.append(ok(290, y + 22, c, gr=18))
        y += 74
    else:
        els_sch.append(z(txt, 330, y - 22, c, "Bold", 34, rechts=1820))
        y += 52
assert y <= 960, y
folie([("sch", "Schema · Anwaltsklausur"), ("k0", "Schema › vorweg: Mandantenbegehren"), ("k1", "Schema › I. Gutachten"),
       ("k2", "Schema › II. Zweckmäßigkeit"), ("k3", "Schema › III. Praktischer Teil")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Das ", 0), ("Gutachten", "a"), (" sagt,", 0)], [("was ", 0), ("rechtlich", "b"), (" geht.", 0)]],
                750, 310, 52, "merke", {"a": beim("merke", "Gutachten"), "b": beim("merke", "rechtlich")}),
    *markertext([[("Die ", 0), ("Zweckmäßigkeit", "c"), (" sagt,", 0)], [("was die Mandantin ", 0), ("jetzt tun", "d"),
                                                                         (" soll.", 0)]],
                750, 560, 52, "m2", {"c": beim("m2", "Zweckmäßigkeit"), "d": beim("m2", "jetzt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
