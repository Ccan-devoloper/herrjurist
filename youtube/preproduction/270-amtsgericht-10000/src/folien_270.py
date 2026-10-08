"""Folge 270 · Amtsgericht Zuständigkeit 2026: Streitwert bis 10.000 Euro – Serienstandard Open Peeps (Katzenkönig).
Fall: Tischlermeister Herr Haberkorn hat bei einem Kunden eine Holztreppe eingebaut; die Rechnung über 9.200 € ist offen.
Seine Tochter Irmela ist Referendarin, Frau Bergfeld (Büro) erinnert an die Klage vom Dezember (7.000 €, Landgericht).
Szenen laut ../SZENENPLAN.md: A Tischlerei (Fall, Hook, Frage), B Sachverhalt, C1 § 23 Nr. 1 GVG (Wortlautkarte),
C2 § 71 Abs. 1 GVG (Wortlautkarte), C3 Reform 1.1.2026, D1 Rechenbeispiel (§§ 4, 5 ZPO), D2 § 78 Abs. 1 S. 1 ZPO
(Wortlautkarte, § 79 ZPO, Dialog), E1 Altverfahren § 44 S. 1 EGGVG (Wortlautkarte), E2 § 261 Abs. 3 Nr. 2 ZPO
(Wortlautkarte), E3 § 506 ZPO, F § 495a ZPO (Wortlautkarte), G Sonderzuständigkeiten § 23 Nr. 2, § 71 Abs. 2 GVG,
H Klausurtipp (Lexi), I Schema, J Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/person/neben als eigene Kopie aus
Folge 258 (gemeinsame Dateien unverändert); neu: werkstatt(), sachverhalt_270(), zeilen_block().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_270/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_270/" in n:
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
NAME = {"HA": "Herr Haberkorn", "IR": "Irmela", "BE": "Frau Bergfeld"}
NFARBE = {"HA": GRUEN, "IR": LILA, "BE": TUERKIS}


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


def sachverhalt_270(cue, absaetze, fragen):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    for f_ in fragen:
        els.append(pille(glyphen(f_), 210, y + 6, cue, fill=PINK, size=36)); y += 76
    assert y + 10 <= 950, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)



# --- eigene Szenenbausteine Folge 270 --------------------------------------------------------------------------------------
GRAUHELL = (226, 226, 230, 255)
GRUENHELL = (232, 247, 233, 255)


def zm(text, cx, y, cue, stil="Regular", size=30, **k):
    """Tafelzeile, mittig auf cx gesetzt."""
    return z(text, round(cx - F(stil, size).getlength(glyphen(text)) / 2), y, cue, stil, size, **k)


def werkbank(x, cue, breite=420):
    """Werkbank (programmatisch: Platte in Holzfarbe, zwei Beine, Tuschekontur)."""
    els = [feld(x - breite // 2, BODEN - 210, breite, 34, cue, fill=HOLZ, rand=5, rund=6, name="werkbank_platte"),
           feld(x - breite // 2 + 30, BODEN - 176, 26, 170, cue, fill=HOLZ, rand=4, rund=4, name="werkbank_bein"),
           feld(x + breite // 2 - 56, BODEN - 176, 26, 170, cue, fill=HOLZ, rand=4, rund=4, name="werkbank_bein")]
    return els


def bretter(x, unten, breite, n, cue):
    """Holzbretter, gestapelt (programmatisch, Holzfarbe mit Tuschekontur)."""
    return [feld(x + (i % 2) * 8, unten - 22 * (i + 1) - 4, breite, 18, cue, fill=HOLZ, rand=4, rund=4, name="brett")
            for i in range(n)]


WB_X = 870
WB_TOP = BODEN - 210


def werkstatt(c, hart_=True):
    """Tischlerei: Fenster, Werkzeugwand, Holzlager, Werkbank mit Brett und Werkzeug, Tür zum Büro."""
    els = [boden(c, hart_),
           ficon("tabler", "window", 250, 360, 190, c, fuell=BLAUHELL, anim="cut"),
           feld(560, 470, 280, 14, c, fill=HOLZ, rand=4, rund=4, name="brett_wand"),
           ficon("tabler", "tools", 640, 468, 90, c, fuell=GELB, anim="cut"),
           ficon("tabler", "ruler-measure", 760, 468, 80, c, fuell=WEISS, anim="cut"),
           *bretter(60, BODEN, 150, 3, c),
           *werkbank(WB_X, c),
           *bretter(WB_X + 20, WB_TOP + 4, 150, 2, c),
           ficon("tabler", "ruler-2", WB_X - 110, WB_TOP + 6, 90, c, fuell=WEISS, anim="cut")]
    return [hart(e) if hart_ else e for e in els]


# ===========================================================================================================================
# A Fall: in der Tischlerei
# ===========================================================================================================================
HAX, IRX, BEX = 400, 1340, 1680
HAa = ("HA_redet_r", HAX, BODEN, FH)
IRa = ("IR_redet", IRX, BODEN, FH)
BEa = ("BE_redet", BEX, BODEN, FH)
RB_ = (1080, 60, 760, 290)                   # Rückblick-Karte „beim Kunden“ oben rechts
rechnung = ficon("tabler", "receipt-euro", HAX + 75, BODEN - 170, 84, "rechnung", fuell=WEISS)
bewegt(rechnung, "rechnung", ("rechnung", 0.35), 0, 60)
szene(rechnung, "270rechnung_1", gain=1.0, versatz=0.35 - 0.29)   # Papiergeräusch: Transient (0,29 s) am Ende der Bewegung
folie([(NULL, "Fall · In der Tischlerei"), ("ha1", "Fall · Muss ich zum Landgericht?"), ("be1", "Fall · Die Klage vom Dezember"),
       ("hook", "Einstieg · Die Frage")], [
    *werkstatt(NULL),
    ficon("tabler", "door", 1820, BODEN - 2, 120, NULL, fuell=BLAUHELL, anim="cut"),
    hart(pl("In einer Tischlerei", 70, 30, NULL, fill=GELB, size=40)),
    *person("HA", HAX, BODEN, FH, [(NULL, "ruhig_r"), ("rechnung", "denkt_r"), ("ha1", "!redet_r"), ("ir1", "denkt_r"),
                                   (beim("ir1", "Amtsgericht"), "froh_r"), ("be1", "sorge_r"), ("hook", "ruhig_r")]),
    hart(fall_ns("HA", HAX, NULL)),
    pl("Tischlermeister", HAX, BODEN + 92, beim("rechnung", "Tischlermeister"), fill=WEISS, size=28, anker="m", bis="ha1"),
    rechnung,
    pl("Rechnung: 9.200 €", HAX + 240, BODEN - 360, "summe", fill=GELB, size=30, anker="m", bis="ha1"),
    # Rückblick: die eingebaute Holztreppe beim Kunden
    bis_(karte(*RB_, "treppe", fill=HELL, rund=18, schatten=6, rand=4), "ha1"),
    pl("Holztreppe", RB_[0] + 30, RB_[1] + 22, "treppe", fill=GELB, size=28, bis="ha1"),
    ficon("tabler", "stairs", 1260, 325, 150, beim("treppe", "Holztreppe"), fuell=HOLZ, bis="ha1"),
    ficon("tabler", "home", 1460, 325, 120, beim("treppe", "eingebaut"), fuell=WEISS, bis="ha1"),
    pl("beim Kunden eingebaut", 1640, 82, beim("treppe", "eingebaut"), fill=WEISS, size=28, anker="m", bis="ha1"),
    *person("IR", IRX, BODEN, FH, [("irmela", "ruhig"), ("ha1", "denkt"), ("ir1", "!redet"), ("be1", "liest"),
                                   ("hook", "ruhig")], erst="pop"),
    fall_ns("IR", IRX, "irmela", d=0.1),
    pl("Referendarin", IRX, BODEN + 92, beim("irmela", "Referendarin"), fill=WEISS, size=28, anker="m", bis="ha1"),
    *person("BE", BEX, BODEN, FH, [("bergfeld", "ruhig"), ("be1", "!redet"), ("hook", "denkt")], erst="pop"),
    fall_ns("BE", BEX, "bergfeld", d=0.1),
    pl("aus dem Büro", BEX, BODEN + 92, beim("bergfeld", "Büro"), fill=WEISS, size=28, anker="m", bis="hook"),
    blase("sprech", 900, 230, "ha1", 880, 200, inhalt=["Der Kunde zahlt einfach nicht.", "Muss ich damit zum Landgericht?",
                                                      "Dann brauche ich ja zwingend einen Anwalt."], textsize=32, figur=HAa,
          bis="ir1"),
    blase("sprech", 700, 230, "ir1", 940, 200, inhalt=["Nicht mehr, Papa.", "Seit 2026 geht das Amtsgericht",
                                                      "bis 10.000 €."], textsize=34, figur=IRa, bis="bergfeld"),
    blase("sprech", 660, 230, "be1", 1150, 200, inhalt=["Und unsere Klage vom Dezember", "über 7.000 €?",
                                                       "Die liegt beim Landgericht."], textsize=34, figur=BEa, bis="hook"),
    pl("10.000 € statt 5.000 €", 960, 120, "hook", fill=GELB, size=44, anker="m", bis="frage"),
    pl("die neue Wertgrenze", 960, 210, "hook2", fill=WEISS, size=36, anker="m", bis="frage"),
    pl("Wann ist das Amtsgericht jetzt zuständig?", 960, 100, "frage", fill=PINK, size=36, anker="m"),
    pl("Was gilt für Altverfahren?", 960, 180, "frage2", fill=PINK, size=36, anker="m"),
    pl("Und was haben die 1.000 € in § 495a ZPO damit zu tun?", 960, 260, "frage3", fill=PINK, size=34, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_270("sv", [
    "Tischlermeister Haberkorn hat bei einem Kunden eine Holztreppe eingebaut. Seine Rechnung über 9.200 € Werklohn ist "
    "offen. Er will klagen und fragt, ob er zum Landgericht und damit zwingend zu einem Anwalt muss.",
    "Frau Bergfeld aus dem Büro erinnert an eine ältere Klage der Tischlerei gegen einen anderen Kunden über 7.000 €: "
    "eingegangen beim Landgericht am 10.12.2025, zugestellt am 8.1.2026.",
], ["Welches Gericht ist für die 9.200 € zuständig, braucht er einen Anwalt?", "Und was gilt für die Klage vom Dezember?"])

# ===========================================================================================================================
# C1 § 23 Nr. 1 GVG (Wortlautkarte, aktuelle Fassung)
# ===========================================================================================================================
W23 = ("„Die Zuständigkeit der Amtsgerichte umfaßt in bürgerlichen Rechtsstreitigkeiten, soweit sie nicht ohne Rücksicht "
       "auf den Wert des Streitgegenstandes den Landgerichten zugewiesen sind: 1. Streitigkeiten über Ansprüche, deren "
       "Gegenstand an Geld oder Geldeswert die Summe von zehntausend Euro nicht übersteigt; …“")
w23, w23_y = wortlaut(110, 180, 1040, W23, "§ 23 Nr. 1 GVG (Fassung seit 1.1.2026)", "w23", marken=[
    ("Amtsgerichte", beim("w23b", "Amtsgericht")), ("Streitigkeiten über Ansprüche", beim("w23b", "Streitigkeiten")),
    ("Geldeswert", beim("w23b", "Geldeswert")), ("zehntausend Euro", beim("w23b", "zehntausend")),
    ("nicht übersteigt", beim("w23b", "übersteigt"))], size=30)
folie([("w23", "§ 23 Nr. 1 GVG › Wertgrenze 10.000 €"), ("bis", "§ 23 Nr. 1 GVG › 10.000 € gehören noch dazu")], rechts_frei([
    *tafel("w23", "Die Grundnorm: § 23 Nr. 1 GVG"),
    *w23,
    blk(110, w23_y + 30, 1040, 90, HELLGRUEN, "bis", [("Genau 10.000 € gehören noch zum Amtsgericht.", "ExtraBold", 34, INK)]),
    ok(1110, w23_y + 75, beim("bis", "Amtsgericht"), gr=22),
    *neben("IR", FX, [("w23", "liest"), ("bis", "froh")], erst="pop"),
    *requisit([("w23", ("tabler", "building-bank", 120, WEISS), "Amtsgericht", GRUEN),
               (beim("w23b", "zehntausend"), ("tabler", "coin-euro", 110, GELB), "bis 10.000 €", GELB)]),
]))
assert w23_y + 130 <= 895, w23_y

# ===========================================================================================================================
# C2 § 71 Abs. 1 GVG (Wortlautkarte)
# ===========================================================================================================================
W71 = ("„Vor die Zivilkammern, einschließlich der Kammern für Handelssachen, gehören alle bürgerlichen Rechtsstreitigkeiten, "
       "die nicht den Amtsgerichten zugewiesen sind.“")
w71, w71_y = wortlaut(110, 400, 1040, W71, "§ 71 Abs. 1 GVG", "w71b", marken=[
    ("Zivilkammern", beim("w71b", "Zivilkammern")), ("alle bürgerlichen Rechtsstreitigkeiten", beim("w71b", "alle")),
    ("nicht den Amtsgerichten zugewiesen", beim("w71b", "nicht"))], size=32)
folie([("w71", "§ 71 Abs. 1 GVG › sonst das Landgericht")], rechts_frei([
    *tafel("w71", "Der Rest: § 71 Abs. 1 GVG"),
    blk(110, 190, 500, 160, GRUENHELL, "w71", [("Amtsgericht", "ExtraBold", 34, INK), ("§ 23 Nr. 1 GVG:", "Bold", 28, INK),
                                               ("bis 10.000 €", "Bold", 28, INK)], rund=18),
    blk(650, 190, 500, 160, BLAUHELL, beim("w71", "Rest"), [("Landgericht", "ExtraBold", 34, INK),
                                                            ("§ 71 Abs. 1 GVG:", "Bold", 28, INK),
                                                            ("der Rest", "Bold", 28, INK)], rund=18),
    *w71,
    *neben("HA", FX, [("w71", "ruhig"), ("w71b", "denkt")], erst="pop"),
    *requisit([("w71", ("tabler", "building-bank", 120, WEISS), "Landgericht", BLAU)]),
]))
assert w71_y <= 895

# ===========================================================================================================================
# C3 Die Reform zum 1.1.2026 (Änderungsgesetz, BGBl. 2025 I Nr. 318)
# ===========================================================================================================================
folie([("reform", "Reform › bis 31.12.2025: 5.000 €"), ("gesetz", "Reform › Gesetz vom 8.12.2025"),
       ("kraft", "Reform › seit 1.1.2026: 10.000 €")], rechts_frei([
    *tafel("reform", "Die Reform zum 1.1.2026"),
    blk(110, 190, 470, 150, GRAUHELL, "reform", [("bis Ende 2025", "Bold", 30, INK), ("5.000 €", "ExtraBold", 44, INK)],
        rund=18),
    hart(pfeil(600, 265, 660, 265, beim("reform", "fünftausend", ende=True), breite=10, kopf=28)),
    blk(680, 190, 470, 150, GELB, "kraft", [("seit 1.1.2026", "Bold", 30, INK), ("10.000 €", "ExtraBold", 44, INK)],
        rund=18),
    z("Gesetz zur Änderung des Zuständigkeitsstreitwerts", 110, 400, "gesetz", "Bold", 32),
    z("der Amtsgerichte, zum Ausbau der Spezialisierung der", 110, 445, "gesetz", "Bold", 32),
    z("Justiz in Zivilsachen sowie zur Änderung weiterer", 110, 490, "gesetz", "Bold", 32),
    z("prozessualer Regelungen vom 8.12.2025", 110, 535, "gesetz", "Bold", 32),
    zit("BGBl. 2025 I Nr. 318, Art. 1 Nr. 1 (§ 23 Nr. 1 GVG)", 110, 590, "gesetz"),
    blk(110, 650, 1040, 80, HELL, "kraft", [("in Kraft seit 1.1.2026", "ExtraBold", 34, INK)]),
    zit("Art. 21 Abs. 2 des Gesetzes", 110, 745, "kraft"),
    *neben("HA", FX, [("reform", "ruhig"), ("kraft", "froh")], erst="pop"),
    *requisit([("reform", ("tabler", "calendar-event", 110, WEISS), "Stichtag", GELB)]),
]))

# ===========================================================================================================================
# D1 Rechenbeispiel: 9.200 € (§ 4 Abs. 1, § 5 ZPO)
# ===========================================================================================================================
folie([("rech", "Rechenbeispiel › 9.200 € Werklohn"), ("r2", "Rechenbeispiel › ohne Nebenforderungen, § 4 ZPO"),
       ("r3", "Rechenbeispiel › Amtsgericht"), ("r4", "Rechenbeispiel › mehrere Ansprüche, § 5 ZPO")], rechts_frei([
    *tafel("rech", "Rechenbeispiel: die Rechnung"),
    z("Werklohn für die Holztreppe: 9.200 €", 110, 180, "r1", "Bold", 34),
    *okz("9.200 € liegen unter 10.000 €", 240, beim("r1", "unter"), "Bold", 32, x=160),
    z("Zinsen und Kosten als Nebenforderungen: zählen nicht mit", 110, 310, "r2", "Bold", 30),
    zit("§ 4 Abs. 1 ZPO", 110, 352, beim("r2", "Paragraf")),
    blk(110, 400, 1040, 76, GRUENHELL, "r3", [("Also: Amtsgericht zuständig", "ExtraBold", 34, INK)]),
    linienzug([(110, 510), (1150, 510)], "r4", breite=4, farbe=TEXT),
    z("Vorsicht: Mehrere Ansprüche in einer Klage", 110, 535, "r4", "Bold", 32),
    z("werden zusammengerechnet.", 110, 580, beim("r4", "zusammengerechnet"), "Bold", 32),
    zit("§ 5 ZPO", 110, 625, beim("r4", "Paragraf")),
    z("9.200 € + 2. Rechnung über 1.000 € = 10.200 €", 110, 675, "r5", "Bold", 32),
    *neinz("über 10.000 €: Landgericht", 745, "r6", "ExtraBold", 34, x=160),
    *neben("HA", FX, [("rech", "ruhig"), ("r3", "froh"), ("r4", "sorge"), ("r6", "denkt")], erst="pop"),
    *requisit([("rech", ("tabler", "receipt-euro", 100, WEISS), "Rechnung: 9.200 €", GELB),
               ("r3", ("tabler", "building-bank", 120, WEISS), "Amtsgericht", GRUEN),
               ("r5", ("tabler", "receipt-euro", 100, HELLROT), "+ 1.000 €", ROT),
               ("r6", ("tabler", "building-bank", 120, WEISS), "Landgericht", BLAU)]),
]))

# ===========================================================================================================================
# D2 Anwaltszwang? § 78 Abs. 1 S. 1 ZPO (Wortlautkarte), § 79 ZPO; Dialog
# ===========================================================================================================================
W78 = "„Vor den Landgerichten und Oberlandesgerichten müssen sich die Parteien durch einen Rechtsanwalt vertreten lassen.“"
w78, w78_y = wortlaut(110, 180, 1040, W78, "§ 78 Abs. 1 S. 1 ZPO", "w78", marken=[
    ("Landgerichten", beim("w78b", "Landgerichten")), ("Oberlandesgerichten", beim("w78b", "Oberlandesgerichten")),
    ("Rechtsanwalt", beim("w78b", "Rechtsanwalt"))], size=32)
X1h = ("HA_redet_r", X1, FB, FR)
X2i = ("IR_redet", X2, FB, FR)
folie([("w78", "§ 78 Abs. 1 ZPO › Anwaltszwang?"), ("ag", "§ 78 Abs. 1 ZPO › nicht am Amtsgericht"),
       ("selbst", "§ 79 Abs. 1 ZPO › Partei führt den Prozess selbst")], rechts_frei([
    *tafel("w78", "Und der Anwalt?"),
    *w78,
    *neinz("am Amtsgericht: kein Anwaltszwang", w78_y + 30, "ag", "ExtraBold", 34, x=160),
    *okz("Herr Haberkorn darf den Prozess selbst führen", w78_y + 100, "selbst", "Bold", 32, x=160),
    zit("§ 79 Abs. 1 S. 1 ZPO", 160, w78_y + 145, beim("selbst", "Paragraf")),
    *okz("Ein Anwalt ist erlaubt, aber keine Pflicht.", w78_y + 200, beim("ir2", "Anwalt"), "Bold", 32, x=160),
    zit("§ 79 Abs. 2 S. 1 ZPO", 160, w78_y + 245, beim("ir2", "Anwalt")),
    *neben("HA", X1, [("w78", "sorge_r"), ("ag", "froh_r"), ("ha2", "!redetfroh_r"), ("ir2", "froh_r")]),
    *neben("IR", X2, [("w78", "liest"), ("ha2", "froh"), ("ir2", "!redet")], bis="alt"),
    blase("sprech", 560, 170, "ha2", 1460, 200, inhalt=["Dann führe ich", "den Prozess selbst."], textsize=32,
          figur=("HA_redetfroh_r", X1, FB, FR), bis="ir2"),
    blase("sprech", 600, 200, "ir2", 1600, 190, inhalt=["Kannst du.", "Ein Anwalt ist erlaubt,", "aber keine Pflicht."],
          textsize=32, figur=X2i),
]))
assert w78_y + 290 <= 895, w78_y

# ===========================================================================================================================
# E1 Altverfahren: § 44 S. 1 EGGVG (Wortlautkarte)
# ===========================================================================================================================
W44 = ("„§ 23 Nummer 1 des Gerichtsverfassungsgesetzes ist auf Verfahren, die vor dem 1. Januar 2026 anhängig geworden sind, "
       "in der bis einschließlich 31. Dezember 2025 geltenden Fassung anzuwenden. …“")
q1 = pl("Eingang beim Landgericht: 10.12.2025", 110, 180, "alt2", fill=GELB, size=30)
q2 = pl("Zustellung: Januar 2026", q1.x + q1.sprite.width + 20, 180, "alt3", fill=WEISS, size=30)
w44, w44_y = wortlaut(110, 270, 1040, W44, "§ 44 S. 1 EGGVG", "w44", marken=[
    ("vor dem 1. Januar 2026", beim("w44b", "vor")), ("anhängig geworden", beim("w44b", "anhängig")),
    ("geltenden Fassung", beim("w44b", "alten"))], size=30)
BEs = ("BE_redet", FX, FB, FR)
folie([("alt", "Altverfahren › die Klage vom Dezember"), ("w44", "Altverfahren › § 44 EGGVG"),
       ("anh", "Altverfahren › anhängig = eingegangen"), ("lg", "Altverfahren › alte Grenze: 5.000 €")], rechts_frei([
    *tafel("alt", "Altverfahren: die Klage vom Dezember"),
    q1, q2,
    *w44,
    blk(110, w44_y + 26, 1040, 80, HELL, "anh", [("anhängig = bei Gericht eingegangen", "ExtraBold", 34, INK)]),
    z("auf die Zustellung kommt es nicht an", 110, w44_y + 120, beim("anh", "Zustellung"), "Bold", 30),
    *okz("Klage vom Dezember: Grenze 5.000 €, also Landgericht", w44_y + 180, "lg", "Bold", 32, x=160,
         haken=beim("lg", "Landgericht")),
    *neben("BE", FX, [("alt", "ruhig"), ("w44", "denkt"), ("lg", "froh"), ("be2", "!redet")],
           bis="w261"),
    blase("sprech", 560, 170, "be2", 1500, 200, inhalt=["Dann bleibt es dort", "beim Anwalt."], textsize=34, figur=BEs),
    *requisit([("alt", ("tabler", "calendar-event", 110, WEISS), "Dezember 2025", WEISS)], bis="be2"),
]))
assert w44_y + 230 <= 895, w44_y

# ===========================================================================================================================
# E2 Perpetuatio fori: § 261 Abs. 3 Nr. 2 ZPO (Wortlautkarte)
# ===========================================================================================================================
W261 = ("„Die Rechtshängigkeit hat folgende Wirkungen: … 2. die Zuständigkeit des Prozessgerichts wird durch eine "
        "Veränderung der sie begründenden Umstände nicht berührt.“")
w261, w261_y = wortlaut(110, 180, 1040, W261, "§ 261 Abs. 3 Nr. 2 ZPO", "w261", marken=[
    ("Zuständigkeit", beim("w261b", "Zuständigkeit")), ("Prozessgerichts", beim("w261b", "Prozessgerichts")), ("Veränderung", beim("w261b", "Veränderung")),
    ("nicht berührt", beim("w261b", "berührt"))], size=30)
folie([("w261", "Altverfahren › § 261 Abs. 3 Nr. 2 ZPO"), ("pf", "Altverfahren › perpetuatio fori")], rechts_frei([
    *tafel("w261", "Und wenn sich später etwas ändert?"),
    *w261,
    pl("perpetuatio fori", 110, w261_y + 26, "pf", fill=GELB, size=34),
    z("Kunde zahlt im Prozess 3.000 €, der Streitwert sinkt:", 110, w261_y + 110, "pf2", "Bold", 30),
    *okz("das Landgericht bleibt zuständig", w261_y + 160, beim("pf2", "bleibt"), "ExtraBold", 32, x=160),
    blk(110, w261_y + 230, 1040, 80, HELL, "pf3", [("ab Rechtshängigkeit = Zustellung der Klage", "ExtraBold", 32, INK)]),
    zit("§ 253 Abs. 1, § 261 Abs. 1 ZPO", 110, w261_y + 325, beim("pf3", "Zustellung")),
    *neben("IR", FX, [("w261", "liest"), ("pf", "ruhig"), ("pf2", "denkt"), (beim("pf2", "bleibt"), "froh")], erst="pop"),
    *requisit([("pf2", ("tabler", "coin-euro", 110, GELB), "Teilzahlung: 3.000 €", GELB),
               (beim("pf2", "bleibt"), ("tabler", "building-bank", 120, WEISS), "Landgericht bleibt", BLAU)]),
]))
assert w261_y + 370 <= 895, w261_y

# ===========================================================================================================================
# E3 Ausnahme: Klageerweiterung am Amtsgericht, § 506 ZPO
# ===========================================================================================================================
folie([("w506", "Ausnahme › § 506 ZPO: Klageerweiterung")], rechts_frei([
    *tafel("w506", "Eine Ausnahme: § 506 ZPO"),
    blk(110, 190, 480, 170, GRUENHELL, "w506", [("Amtsgericht", "ExtraBold", 34, INK), ("Klage erweitert", "Bold", 30, INK),
                                                ("über 10.000 €", "Bold", 30, INK)], rund=18),
    hart(pfeil(610, 275, 680, 275, "w506b", breite=10, kopf=28)),
    blk(700, 190, 450, 170, BLAUHELL, "w506b", [("Landgericht", "ExtraBold", 34, INK), ("Verweisung", "Bold", 30, INK),
                                                ("auf Antrag", "Bold", 30, INK)], rund=18),
    zit("§ 506 Abs. 1 ZPO", 110, 390, beim("w506b", "Paragraf")),
    *neben("HA", FX, [("w506", "denkt"), ("w506b", "ruhig")], erst="pop"),
    *requisit([(beim("w506", "Erweitert"), ("tabler", "file-plus", 100, WEISS), "Klage erweitert", GRUEN),
               ("w506b", ("tabler", "arrows-exchange", 110, WEISS), "Verweisung", BLAU)]),
]))

# ===========================================================================================================================
# F Abgrenzung: § 495a ZPO (Wortlautkarte)
# ===========================================================================================================================
W495 = ("„Das Gericht kann sein Verfahren nach billigem Ermessen bestimmen, wenn der Streitwert 1 000 Euro nicht übersteigt. "
        "Auf Antrag muss mündlich verhandelt werden.“")
w495, w495_y = wortlaut(110, 180, 1040, W495, "§ 495a ZPO (Fassung seit 1.1.2026)", "w495", marken=[
    ("billigem Ermessen", beim("w495b", "billigem")), ("1 000 Euro", beim("w495b", "tausend")),
    ("mündlich verhandelt", beim("antrag", "mündlich"))], size=32)
Y5 = w495_y + 26
folie([("w495", "Abgrenzung › § 495a ZPO"), ("ver", "Abgrenzung › keine Zuständigkeitsnorm"),
       ("bsp", "Abgrenzung › 800 €: Amtsgericht, freieres Verfahren")], rechts_frei([
    *tafel("w495", "Nicht verwechseln: § 495a ZPO"),
    *w495,
    *okz("vereinfachtes Verfahren am Amtsgericht", Y5, beim("ver", "vereinfachtes"), "Bold", 32, x=160),
    *neinz("keine Zuständigkeitsnorm", Y5 + 55, beim("ver", "keine"), "ExtraBold", 32, x=160),
    z("Grenze seit 1.1.2026: 1.000 € statt 600 €", 110, Y5 + 125, "neu495", "Bold", 32),
    blk(110, Y5 + 185, 1040, 70, HELL, "bsp", [("Rechnung über 800 €: Amtsgericht wie bis 10.000 €", "Bold", 30, INK)]),
    *okz("das Gericht darf das Verfahren nur freier gestalten", Y5 + 275, "frei", "Bold", 30, x=160),
    *neben("BE", FX, [("w495", "ruhig"), ("ver", "denkt"), ("bsp", "froh")], erst="pop"),
    *requisit([("w495", ("tabler", "file-text", 100, WEISS), "§ 495a ZPO", WEISS),
               ("bsp", ("tabler", "receipt-euro", 100, WEISS), "Rechnung: 800 €", GELB)]),
]))
assert Y5 + 300 <= 895, Y5

# ===========================================================================================================================
# G Sonderzuständigkeiten: ohne Rücksicht auf den Wert (§ 23 Nr. 2, § 71 Abs. 2 GVG)
# ===========================================================================================================================
SO = [(None, "Amtsgericht, § 23 Nr. 2 GVG", GRUENHELL, "s23"),
      (beim("s23", "Wohnraummiete"), "a) Wohnraummiete", None, None),
      ("s23b", "c) Streit nach § 43 Abs. 2 WEG", None, None),
      ("s23c", "d) Wildschaden", None, None),
      (beim("s23d", "Nachbarstreitigkeiten"), "e) bestimmte Nachbarstreitigkeiten · neu 2026", None, None),
      (None, "Landgericht, § 71 Abs. 2 GVG", BLAUHELL, "s71"),
      (beim("s71", "Anordnungen"), "Nr. 5 Bauvertrag: Anordnungen des Bestellers", None, None),
      ("s71b", "Nr. 9 Heilbehandlungen · neu 2026", None, None),
      ("s71c", "Nr. 7 Veröffentlichungen in Presse und Internet · neu", None, None),
      ("s71d", "Nr. 8 Vergabe öffentlicher Aufträge · neu 2026", None, None)]
els_so, y = [], 175
for c, t, fill, kc in SO:
    if fill:
        els_so += [blk(110, y, 1040, 62, fill, kc, [(t, "ExtraBold", 32, INK)], rund=14, rand=4, anim="pop")]
        y += 76
    else:
        els_so.append(z(t, 150, y, c, "Bold", 30))
        y += 50
els_so.append(blk(110, y + 12, 1040, 70, HELL, "treppe2", [("Herr Haberkorn: nur Werklohn, der Wert entscheidet", "ExtraBold",
                                                          30, INK)]))
assert y + 90 <= 895, y
folie([("sonder", "Sonderzuständigkeiten › ohne Rücksicht auf den Wert"), ("s23", "Sonderzuständigkeiten › § 23 Nr. 2 GVG"),
       ("s71", "Sonderzuständigkeiten › § 71 Abs. 2 GVG"), ("treppe2", "Sonderzuständigkeiten › beim Werklohn zählt der Wert")],
      rechts_frei([
    *tafel("sonder", "Ohne Rücksicht auf den Wert"),
    *els_so,
    *neben("HA", FX, [("sonder", "ruhig"), ("s71", "denkt"), ("wert", "froh")], erst="pop"),
    *requisit([(beim("s23", "Wohnraummiete"), ("tabler", "home", 110, WEISS), "Wohnraummiete", GRUEN),
               ("s23c", ("tabler", "deer", 110, WEISS), "Wildschaden", GRUEN),
               (beim("s23d", "Nachbarstreitigkeiten"), ("tabler", "fence", 120, HOLZ), "Nachbarn", GRUEN),
               (beim("s71", "Anordnungen"), ("tabler", "home-cog", 110, WEISS), "Bauvertrag", BLAU),
               ("s71b", ("tabler", "stethoscope", 110, WEISS), "Heilbehandlung", BLAU),
               ("s71c", ("tabler", "news", 110, WEISS), "Presse", BLAU),
               ("s71d", ("tabler", "file-text", 100, WEISS), "Vergabe", BLAU),
               ("treppe2", ("tabler", "stairs", 120, HOLZ), "Werklohn", GELB)]),
]))

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · alte Skripte, Eingangsstempel")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Achtung: Alte Skripte nennen", 200, 200, beim("tipp", "Achtung"), "Bold", 36),
    z("noch 5.000 €.", 200, 255, beim("tipp", "fünftausend"), "ExtraBold", 38),
    z("Welche Hilfsmittel in welchem Stand zugelassen", 200, 340, "tipp2", "Bold", 32),
    z("sind: von Land zu Land verschieden", 200, 385, beim("tipp2", "Land"), "Bold", 32),
    z("Eingangsstempel der Klage prüfen:", 200, 470, beim("tipp3", "Eingangsstempel"), "Bold", 34),
    z("vor 2026 eingegangen: alte Grenze", 200, 525, beim("tipp3", "Ging"), "ExtraBold", 36),
    dicon("tabler", "books", 400, 800, 130, beim("tipp", "Skripte"), fuell=GELB),
    dicon("tabler", "calendar-event", 800, 800, 130, beim("tipp3", "Eingangsstempel"), fuell=WEISS),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Prüfschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Zuständigkeit ohne Rücksicht auf den Wert?", BLAU, 0),
          ("k1a", "", "etwa § 23 Nr. 2 oder § 71 Abs. 2 GVG", None, 1),
          ("k2", "II.", "Streitwert", GELB, 0),
          ("k2a", "", "ohne Nebenforderungen, mehrere Ansprüche zusammengerechnet", None, 1),
          ("k3", "III.", "Wann wurde die Klage anhängig?", GRUEN, 0),
          ("k3a", "", "vor 2026: 5.000 €, danach: 10.000 € (§ 44 EGGVG)", None, 1),
          ("k4", "IV.", "bis zur Grenze Amtsgericht zuständig, darüber Landgericht mit Anwaltszwang", LILA, 0),
          ("k5", "V.", "spätere Veränderungen nach Rechtshängigkeit: unberührt", HELLROT, 0),
          ("k5a", "", "außer bei einer Erweiterung nach § 506 ZPO", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: sachliche Zuständigkeit"), 110, 90, "sch", 46)]
y = 190
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 62, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 34).getlength(r) / 2, y + 8, c, "ExtraBold", 34, rechts=1820),
                    z(txt, 255, y + 8, c, "ExtraBold", 34, rechts=1820)]
        y += 84
    else:
        els_sch.append(z(txt, 330, y - 4, c, "Bold", 32, rechts=1820))
        els_sch.append(ok(290, y + 16, c, gr=18))
        y += 66
assert y <= 960, y
folie([("sch", "Schema · sachliche Zuständigkeit"), ("k1", "Schema › I. ohne Rücksicht auf den Wert"),
       ("k2", "Schema › II. Streitwert"), ("k3", "Schema › III. Zeitpunkt der Anhängigkeit"),
       ("k4", "Schema › IV. Amtsgericht oder Landgericht"), ("k5", "Schema › V. perpetuatio fori")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Amtsgericht ", "a"), ("bis ", 0), ("10.000 €", "b"), (",", 0)], [("ohne Anwaltszwang.", "c")]],
                750, 290, 50, "merke", {"a": beim("merke", "Amtsgericht"), "b": beim("merke", "zehntausend"),
                                        "c": beim("merke", "ohne")}),
    *markertext([[("Die ", 0), ("5.000 €", "d"), (" aus ", 0), ("alten Skripten", "e")],
                 [("gelten nur noch für Klagen, die", 0)], [("vor 2026 ", "f"), ("eingegangen sind.", 0)]],
                750, 500, 46, "m2", {"d": beim("m2", "fünftausend"), "e": beim("m2", "alten"),
                                     "f": beim("m2", "vor")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
