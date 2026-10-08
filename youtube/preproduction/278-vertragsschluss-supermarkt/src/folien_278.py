"""Folge 278 · Vertragsschluss Supermarkt: Wann kaufst du die Milch? · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Erhard nimmt am Dienstagabend im Supermarkt (fiktiv, Schild nur „Milch“, keine Marke) eine kalte Glasflasche
Milch mit einer Hand aus dem Kühlregal, den Blick auf dem Handy; die Flasche rutscht und zerbricht (nur als Symbol), niemand
wird verletzt. Frau Kesting (Filialleiterin) verlangt 1,49 €. Danach: Anspruch § 433 Abs. 2 (Wortlautkarte), Streit um den
Vertragsschluss im Selbstbedienungsladen nach BGHZ 66, 51, Gründe V. 1 (zwei Ansichten nebeneinander, Argumente, § 9 JuSchG),
Folge für die Flasche (nach beiden Ansichten erst an der Kasse; VIII ZR 171/10 Rn. 14 f.), § 311 Abs. 2 Nr. 2, § 241 Abs. 2,
§ 280 Abs. 1 (Wortlautkarten), § 823 Abs. 1 mit Beweislast, Gegenrichtung Gemüseblatt-Fall, Ergebnis, Klausurtipp, Schema,
Merksatz. Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als
eigene Kopie aus Folge 276 (gemeinsame Dateien unverändert); neu: kuehlregal(), scherben(), flasche_kipp().
Handlungsgeräusch: zerbrechende Glasflasche (A, Wort „zerbricht“); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_278/"

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
LILAHELL = (240, 236, 255, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_278/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205/229) ---------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"EH": "Erhard", "KE": "Frau Kesting"}
BLAU_P, LILA_P, ROT_P = (141, 179, 242, 255), (184, 169, 245, 255), (240, 122, 106, 255)
GRUEN_P0 = (143, 214, 148, 255)
NFARBE = {"EH": GRUEN_P0, "KE": LILA_P}
GRUEN_P = (143, 214, 148, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def fenster(x, y, w, h, cue, fill=None, bis=None):
    """Fenster mit Sprossen (Tageslicht; abends dunkleres Blau)."""
    return [bis_(hart(feld(x, y, w, h, cue, fill=fill or BLAUHELL, rand=5, rund=8, name="fenster")), bis),
            bis_(hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")), bis),
            bis_(hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2")), bis)]




# ===========================================================================================================================
# Schauplatz: Gang im Supermarkt mit Kühlregal (A, H) – programmatisch, ohne Namen oder Marke
# ===========================================================================================================================
MILCH = WEISS                                # Milchflaschen weiß gefüllt
EHX, KEX = 1040, 1560                        # Erhard und Frau Kesting im Gang
SCHX = EHX - 150                             # Scherben am Boden zwischen Regal und Erhard
REGAL_Y = 300


def kuehlregal(cue):
    """Kühlregal links: Glasfront mit drei Böden und Milchflaschen (Tabler 'bottle'), Schild „Milch“."""
    els = [boden(cue),
           hart(feld(70, REGAL_Y, 690, BODEN - REGAL_Y - 4, cue, fill=HELLGRAU, rand=5, rund=10, name="kuehlregal")),
           hart(feld(96, REGAL_Y + 26, 638, BODEN - REGAL_Y - 56, cue, fill=BLAUHELL, rand=4, rund=8, name="glasfront")),
           hart(feld(300, REGAL_Y - 70, 260, 70, cue, fill=GELB, rand=4, rund=12, name="schild")),
           hart(z("Milch", 430 - F("ExtraBold", 44).getlength("Milch") / 2, REGAL_Y - 64, cue, "ExtraBold", 44))]
    for k, yb in enumerate((REGAL_Y + 175, REGAL_Y + 335, REGAL_Y + 495)):
        els.append(hart(feld(96, yb, 638, 14, cue, fill=WEISS, rand=3, rund=4, name=f"boden{k}")))
        for i in range(7 if k else 6):          # oberster Boden: eine Lücke (dort stand Erhards Flasche)
            els.append(ficon("tabler", "bottle", 160 + i * 88, yb, 60, cue, fuell=MILCH, anim="cut"))
    return els


def scherben(cue, bis=None):
    """Zerbrochene Flasche nur als Symbol: Kollisionszeichen (Fluent Emoji High Contrast) und Milchpfütze; niemand verletzt."""
    return [bis_(El(_feld(150, 26, WEISS, 4, 13), SCHX - 81, BODEN - 22, cue, "pop", 0.0, None, name="pfuetze"), bis),
            bis_(ficon("fluent-emoji-high-contrast", "collision", SCHX - 10, BODEN - 18, 70, cue, fuell=GELB, anim="pop"), bis)]


def flasche_kipp(cx, unten, winkel, cue, bis):
    """Fallende Flasche: Tabler-Icon gedreht (nicht umgezeichnet)."""
    e = ficon("tabler", "bottle", cx, unten, 64, cue, fuell=MILCH, anim="cut", bis=bis)
    sp = e.sprite.rotate(winkel, expand=True, resample=Image.BICUBIC)
    e.x, e.y = cx - sp.width / 2, unten - sp.height
    e.sprite = sp
    e.name = "ficon:bottle_kipp"
    return e


# ===========================================================================================================================
# A Im Gang: Glasflasche rutscht aus der Hand; Frau Kesting verlangt 1,49 € – die Frage
# ===========================================================================================================================
HAND_L = (EHX - 50, BODEN - 196)            # äußere Hand zum Regal hin (Grundansicht blickt nach links), aus der Sichtprüfung
HAND_V = (EHX - 2, BODEN - 196)             # vordere Faust vor dem Gürtel: Handy

folie([(NULL, "Fall · Im Supermarkt"), ("erh", "Fall · Erhard am Kühlregal"),
       ("griff", "Fall · eine Hand, Blick aufs Handy"), ("rutsch", "Fall · Die Flasche rutscht"),
       ("knall", "Fall · zerbrochen, niemand verletzt"), ("kest", "Fall · Frau Kesting kommt dazu"),
       ("k1", "Fall · Frau Kesting: „1,49 €“"), ("e1", "Fall · Erhard: „noch gar nicht gekauft“"),
       ("frage", "Die Frage · Muss Erhard zahlen?"), ("frage2", "Die Frage · Wann ist der Kaufvertrag geschlossen?"),
       ("frage3", "Die Frage · Wer trägt das Risiko im Gang?")], [
    *kuehlregal(NULL),
    pl("Musst du sie bezahlen?", 1380, 200, beim("fall", "Musst"), fill=PINK, size=32, anker="m", bis="erh"),
    pl("Dienstagabend", 1880 - F("Bold", 30).getlength("Dienstagabend") - 40, 40, beim("erh", "Dienstagabend"),
       fill=GELB, size=30, bis="kest"),
    *fig("EH", EHX, BODEN, FH, [("erh", "ruhig"), ("griff", "denkt"), (beim("rutsch", "rutscht"), "schreck"),
                               (beim("knall", "Verletzt"), "sorge")], bis="kest", erst="pop"),
    *fig("EH", EHX, BODEN, FH, [("kest", "staunt_r")], bis="e1", erst="cut"),
    *redet("EH_redet_r", EHX, BODEN, FH, "e1", "frage"),
    *fig("EH", EHX, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    ns(NAME["EH"], EHX, BODEN, "erh", NFARBE["EH"], d=0.1),
    # Flasche in der Hand, Handy in der anderen; dann rutscht sie, zerbricht (nur Symbol)
    bis_(ficon("tabler", "bottle", *HAND_L, 64, "griff", fuell=MILCH, anim="pop"), beim("rutsch", "rutscht")),
    bis_(ficon("tabler", "device-mobile", *HAND_V, 44, beim("griff", "Blick"), fuell=BLAUHELL, anim="pop"),
         beim("rutsch", "rutscht")),
    pl("Glasflasche Milch", 1380, 200, beim("griff", "Flasche"), fill=WEISS, size=30, anker="m", bis="rutsch"),
    pl("eine Hand, Blick aufs Handy", 1380, 270, beim("griff", "Blick"), fill=WEISS, size=30, anker="m", bis="rutsch"),
    flasche_kipp(HAND_L[0] - 20, BODEN - 160, 25, beim("rutsch", "rutscht"), beim("rutsch", "Finger")),
    flasche_kipp(HAND_L[0] - 50, BODEN - 50, 70, beim("rutsch", "Finger"), beim("knall", "zerbricht")),
    pl("beschlagen: rutscht", 1380, 200, beim("rutsch", "beschlagene"), fill=BLAUHELL, size=30, anker="m", bis="knall"),
    szene(scherben(beim("knall", "zerbricht"))[1], "278glas*", 0.9, 0.0),
    scherben(beim("knall", "zerbricht"))[0],
    pl("zerbrochen", 1380, 200, beim("knall", "zerbricht"), fill=HELLROT, size=30, anker="m", bis="kest"),
    pl("niemand verletzt", 1380, 270, beim("knall", "Verletzt"), fill=HELLGRUEN, size=30, anker="m", bis="kest"),
    # Frau Kesting kommt dazu
    *fig("KE", KEX, BODEN, FH, [("kest", "ernst")], bis="k1", erst="pop"),
    *redet("KE_redet", KEX, BODEN, FH, "k1", "e1"),
    *fig("KE", KEX, BODEN, FH, [("e1", "denkt"), ("frage", "ernst")], erst="cut"),
    ns(NAME["KE"], KEX, BODEN, "kest", NFARBE["KE"], d=0.1),
    pl("Filialleiterin", KEX, BODEN + 80, beim("kest", "Filialleiterin"), fill=WEISS, size=26, anker="m"),
    blase("sprech", 640, 190, "k1", 1300, 210, inhalt=["Die Flasche müssen Sie", "bezahlen, 1,49 €."],
          textsize=31, figur=("KE_redet", KEX, BODEN, FH), bis="e1"),
    blase("sprech", 700, 220, "e1", 1180, 200, inhalt=["Wieso? Gekauft habe ich sie doch", "noch gar nicht. An der Kasse",
                                                     "war ich noch nicht."],
          textsize=31, figur=("EH_redet_r", EHX, BODEN, FH), bis="frage"),
    pl("Muss Erhard die Milch bezahlen?", 800, 30, "frage", fill=PINK, size=34),
    pl("Wann kommt der Kaufvertrag zustande?", 800, 108, "frage2", fill=PINK, size=34),
    pl("Wer trägt das Risiko im Gang?", 800, 186, "frage3", fill=PINK, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_278(cue, absaetze, frage, size=44):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_278("sv", [
    "Erhard nimmt am Dienstagabend im Supermarkt eine kalte Glasflasche Milch aus dem Kühlregal. Er hält sie mit einer "
    "Hand und schaut dabei auf die Einkaufsliste in seinem Handy. Die beschlagene Flasche rutscht ihm durch die Finger "
    "und zerbricht auf dem Boden. Verletzt wird niemand.",
    "Frau Kesting, die Filialleiterin, verlangt für den Markt 1,49 €. Erhard meint, er habe die Milch noch gar nicht "
    "gekauft; an der Kasse sei er noch nicht gewesen.",
], "Kann der Markt von Erhard Geld verlangen?")


# ===========================================================================================================================
# Tafel-Helfer (wie Folge 276)
# ===========================================================================================================================
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


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def okw(text, y, cue, haken, stil="Bold", size=34, x=185, **k):
    """Tafelzeile zum Satzbeginn, Haken erst zur gesprochenen Bejahung (haken = Cue)."""
    return [ok(x - 45, y + 20, haken, gr=20), z(text, x, y, cue, stil, size, **k)]


# ===========================================================================================================================
# C Anspruch: § 433 Abs. 2 (Wortlautkarte); Kaufvertrag; Anknüpfung an Folge 276; Streit im Selbstbedienungsladen
# ===========================================================================================================================
PA = "Anspruch"
w433, w433_y = wortlaut(80, 230, 1100, "„Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu zahlen und "
                                       "die gekaufte Sache abzunehmen.“", "§ 433 Abs. 2 BGB", "w433", size=34,
                        marken=[("Kaufpreis zu zahlen", beim("w433", "Kaufpreis"))])
folie([("ansp", f"{PA} · Markt gegen Erhard: Kaufpreis?"), ("w433", f"{PA} › Kaufpreis, § 433 Abs. 2 BGB"),
       ("ansp2", f"{PA} › Kaufvertrag: Angebot und Annahme"), ("v276", f"{PA} › Schaufenster: nur Einladung"),
       ("kern", f"{PA} › Selbstbedienungsladen: umstritten")], [
    *tafel("ansp", "Anspruch auf den Kaufpreis"),
    z("Markt gegen Erhard: 1,49 € für die Milch", 110, 168, "ansp", "Bold", 36),
    *w433,
    blk(110, w433_y + 30, 1040, 90, GELB, "ansp2", [("Voraussetzung: Kaufvertrag aus Angebot und Annahme", "ExtraBold", 30, INK)]),
    zit("§§ 145 ff. BGB", 110, w433_y + 132, beim("ansp2", "Paragrafen")),
    blk(110, w433_y + 186, 1040, 90, LILAHELL, "v276", [("Schaufenster: nur Einladung – Folge „Invitatio“", "ExtraBold", 30, INK)]),
    blk(110, w433_y + 306, 1040, 90, HELLROT, beim("kern", "umstritten"),
        [("Selbstbedienungsladen: umstritten", "ExtraBold", 32, INK)]),
    *requisit([("ansp", ("tabler", "bottle", 90, MILCH), "Milch: 1,49 €", WEISS),
               ("ansp2", ("tabler", "file-text", 110, WEISS), "Kaufvertrag?", GELB),
               ("v276", ("tabler", "building-store", 120, WEISS), "Schaufenster", LILAHELL),
               ("kern", ("tabler", "shopping-cart", 120, WEISS), "Supermarkt?", HELLROT)], px=1560, pu=330, py=90),
    *paar("EH", [("ansp", "ruhig"), ("kern", "denkt")], "KE", [("ansp", "ruhig"), ("ansp2", "denkt")]),
])
assert w433_y + 306 + 100 <= 895, w433_y

# ===========================================================================================================================
# D Streitstand: zwei Ansichten (BGHZ 66, 51, Gründe V. 1), Argumente je ein Satz; § 9 Abs. 1 Nr. 2 JuSchG
# ===========================================================================================================================
PS_ = "Streit"
folie([("streit", f"{PS_} · Wann ist im Supermarkt gekauft?"), ("an1", f"{PS_} › Ansicht 1: Regal = Angebot"),
       ("arg1", f"{PS_} › Ansicht 1: Argument"), ("an2", f"{PS_} › Ansicht 2: Regal = Einladung"),
       ("annahme", f"{PS_} › Ansicht 2: Annahme durch Registrieren"), ("arg2", f"{PS_} › Ansicht 2: Argument"),
       ("jusch", f"{PS_} › Ansicht 2: Jugendschutz, § 9 JuSchG")], [
    *tafel("streit", "Streit: Wann ist gekauft?"),
    zit("beide Ansichten: BGH, Urt. v. 28.1.1976 – VIII ZR 246/74,", 110, 166, beim("streit", "beschrieben")),
    zit("BGHZ 66, 51 (Gemüseblatt-Fall), Gründe V. 1", 110, 202, beim("streit", "beschrieben")),
    hart(feld(110, 252, 510, 192, "an1", fill=BLAUHELL, rand=5, rund=18, name="ansicht1")),
    z("Ansicht 1", 140, 266, "an1", "ExtraBold", 30, rechts=600),
    z("Regal = Angebot an jeden", 140, 312, beim("an1", "Regal"), "Bold", 28, rechts=600),
    z("Annahme: Vorlegen", 140, 352, beim("an1", "Du"), "Bold", 28, rechts=600),
    z("an der Kasse", 140, 390, beim("an1", "Kasse"), "Bold", 28, rechts=600),
    hart(feld(640, 252, 510, 192, "an2", fill=LILAHELL, rand=5, rund=18, name="ansicht2")),
    z("Ansicht 2 (überwiegend)", 670, 266, "an2", "ExtraBold", 30, rechts=1130),
    z("Regal = nur Einladung", 670, 312, beim("an2", "Regal"), "Bold", 28, rechts=1130),
    z("Angebot: Vorlegen an der Kasse", 670, 352, beim("an2", "Das"), "Bold", 28, rechts=1130),
    z("Annahme: Registrieren", 670, 390, "annahme", "Bold", 28, rechts=1130),
    z("Dafür:", 130, 470, "arg1", "ExtraBold", 30, farbe=DGRUEN, rechts=600),
    z("Wer Ware mit Preis ins", 130, 512, beim("arg1", "Wer"), "Regular", 28, rechts=600),
    z("Regal stellt, will an jeden", 130, 550, beim("arg1", "Wer"), "Regular", 28, rechts=600),
    z("verkaufen.", 130, 588, beim("arg1", "Wer"), "Regular", 28, rechts=600),
    z("Dafür:", 660, 470, "arg2", "ExtraBold", 30, farbe=DGRUEN, rechts=1130),
    z("Der Markt will an der Kasse", 660, 512, beim("arg2", "Der"), "Regular", 28, rechts=1130),
    z("noch prüfen, etwa beim", 660, 550, beim("arg2", "Der"), "Regular", 28, rechts=1130),
    z("Jugendschutz.", 660, 588, beim("arg2", "Jugendschutz"), "Regular", 28, rechts=1130),
    blk(640, 640, 510, 46 + 2 * 38, GELB, "jusch", [("Schnaps nicht an", "Bold", 28, INK), ("Jugendliche", "Bold", 28, INK)]),
    zit("§ 9 Abs. 1 Nr. 2 JuSchG", 660, 776, beim("jusch", "Paragraf")),
    *requisit([("streit", ("fluent-emoji-high-contrast", "leafy-green", 120, GRUEN_P), "Gemüseblatt-Fall", HELLGRUEN),
               ("an1", ("tabler", "shopping-cart", 130, WEISS), "Regal: Angebot?", BLAUHELL),
               (beim("an1", "Kasse"), ("ph", "cash-register", 130, WEISS), "Annahme: Kasse", BLAUHELL),
               ("an2", ("tabler", "mail-opened", 120, LILAHELL), "nur Einladung", LILAHELL),
               ("annahme", ("ph", "barcode", 130, WEISS), "scannen", LILAHELL),
               ("arg2", ("ph", "beer-bottle", 110, GELB), "Jugendschutz", GELB)]),
    *stehend("KE", FX, [("streit", "ruhig"), ("an1", "denkt"), ("arg1", "froh"), ("an2", "ernst"), ("arg2", "denkt")]),
])

# ===========================================================================================================================
# E Folge für die Flasche: nach beiden Ansichten erst an der Kasse (VIII ZR 171/10 Rn. 14 f.) → kein Kaufpreis
# ===========================================================================================================================
PF = "Die Flasche"
folie([("beide", f"{PF} · Streit kann offenbleiben"), ("regal", f"{PF} › Herausnehmen bindet nicht"),
       ("kein433", f"{PF} › kein Vertrag, kein Kaufpreis"), ("aber", f"{PF} › aber: Haftung?")], [
    *tafel("beide", "Folge für die Flasche"),
    z("Streit kann offenbleiben:", 110, 172, "beide", "ExtraBold", 34),
    *okw("nach beiden Ansichten: Vertrag erst an der Kasse", 228, beim("beide", "Nach"), beim("beide", "Kasse"), "Bold", 33),
    *neinz("Herausnehmen aus dem Regal bindet noch nicht", 300, "regal", "Bold", 33, kreuz=beim("regal", "bindet")),
    zit("BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 14 f.", 185, 348, beim("regal", "Bundesgerichtshof")),
    *neinz("im Gang: noch kein Kaufvertrag", 420, "kein433", "Bold", 34, kreuz=beim("kein433", "keinen")),
    *neinz("kein Anspruch auf den Kaufpreis, § 433 Abs. 2 BGB", 476, beim("kein433", "damit"), "Bold", 33,
           kreuz=beim("kein433", "keinen", nr=2)),
    blk(110, 580, 1040, 100, HELLROT, "aber", [("Aber: Haftung für die Scherben?", "ExtraBold", 34, INK)]),
    *requisit([("beide", ("ph", "cash-register", 130, WEISS), "erst an der Kasse", WEISS),
               ("regal", ("tabler", "shopping-cart", 130, WEISS), "Regal: noch frei", WEISS),
               ("kein433", ("tabler", "bottle", 90, MILCH), "kein Kaufpreis", HELLGRUEN),
               ("aber", ("fluent-emoji-high-contrast", "collision", 120, GELB), "Scherben", HELLROT)]),
    *stehend("EH", FX, [("beide", "denkt"), ("kein433", "erleichtert"), ("aber", "sorge")]),
])

# ===========================================================================================================================
# F1 § 311 Abs. 2 Nr. 2 BGB (Wortlautkarte, Auszug): Schuldverhältnis durch Anbahnung
# ===========================================================================================================================
PC = "II. culpa in contrahendo"
w311, w311_y = wortlaut(80, 170, 1100, "„Ein Schuldverhältnis mit Pflichten nach § 241 Abs. 2 entsteht auch durch … 2. die "
                                       "Anbahnung eines Vertrags, bei welcher der eine Teil im Hinblick auf eine etwaige "
                                       "rechtsgeschäftliche Beziehung dem anderen Teil die Möglichkeit zur Einwirkung auf "
                                       "seine Rechte, Rechtsgüter und Interessen gewährt oder ihm diese anvertraut, …“",
                        "§ 311 Abs. 2 Nr. 2 BGB", "w311", size=32,
                        marken=[("Anbahnung", beim("w311", "Anbahnung")), ("Einwirkung", beim("w311", "Einwirkung"))])
folie([("w311", f"{PC} · Schuldverhältnis, § 311 Abs. 2 BGB"), ("anb", f"{PC} › Anbahnung: Ware in der Hand des Kunden")], [
    *tafel("w311", "Schuldverhältnis ohne Vertrag?"),
    *w311,
    *okw("Der Markt lässt Erhard die Ware selbst in die Hand nehmen.", w311_y + 34, "anb", beim("anb", "Genau"), "Bold", 31),
    *requisit([("w311", ("tabler", "building-store", 130, WEISS), "Anbahnung", WEISS),
               ("anb", ("tabler", "bottle", 90, MILCH), "Ware in der Hand", WEISS)]),
    *stehend("EH", FX, [("w311", "ruhig"), ("anb", "denkt")]),
])
assert w311_y + 34 + 50 <= 895, w311_y

# ===========================================================================================================================
# F2 § 241 Abs. 2 BGB (Wortlautkarte): Rücksicht – auch der Kunde; Verweis Folge 010
# ===========================================================================================================================
w241, w241_y = wortlaut(80, 170, 1100, "„Das Schuldverhältnis kann nach seinem Inhalt jeden Teil zur Rücksicht auf die "
                                       "Rechte, Rechtsgüter und Interessen des anderen Teils verpflichten.“",
                        "§ 241 Abs. 2 BGB", "w241", size=34,
                        marken=[("jeden Teil", beim("w241", "jeden")), ("Rücksicht", beim("w241", "Rücksicht"))])
folie([("w241", f"{PC} › Rücksichtspflicht, § 241 Abs. 2 BGB"), ("pfl", f"{PC} › auch der Kunde"),
       ("v010", f"{PC} › Folge „Culpa in contrahendo“")], [
    *tafel("w241", "Rücksicht – für jeden Teil"),
    *w241,
    *okw("auch der Kunde: sorgfältig mit fremder Ware", w241_y + 40, "pfl", beim("pfl", "Also"), "Bold", 34),
    z("die Milch gehört noch dem Markt", 185, w241_y + 96, beim("pfl", "fremder"), "Regular", 32),
    blk(110, w241_y + 180, 1040, 90, LILAHELL, "v010", [("mehr dazu: Folge „Culpa in contrahendo“", "ExtraBold", 32, INK)]),
    *requisit([("w241", ("tabler", "hand-stop", 110, WEISS), "Rücksicht", WEISS),
               ("pfl", ("tabler", "bottle", 90, MILCH), "fremde Ware", WEISS),
               ("v010", ("tabler", "book", 120, LILAHELL), "Grundlagen", LILAHELL)]),
    *stehend("KE", FX, [("w241", "ruhig"), ("pfl", "froh")]),
])
assert w241_y + 180 + 100 <= 895, w241_y

# ===========================================================================================================================
# F3 § 280 Abs. 1 BGB (Wortlautkarte): Pflichtverletzung, vermutetes Vertretenmüssen, Fahrlässigkeit (§ 276 Abs. 2)
# ===========================================================================================================================
w280, w280_y = wortlaut(80, 170, 1100, "„Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so kann der Gläubiger "
                                       "Ersatz des hierdurch entstehenden Schadens verlangen. Dies gilt nicht, wenn der "
                                       "Schuldner die Pflichtverletzung nicht zu vertreten hat.“",
                        "§ 280 Abs. 1 BGB", "w280", size=32,
                        marken=[("Pflicht", beim("w280", "Pflicht")), ("nicht zu", beim("vm", "nicht", nr=2))])
folie([("w280", f"{PC} › Anspruchsgrundlage, § 280 Abs. 1 BGB"), ("vm", f"{PC} › Vertretenmüssen vermutet"),
       ("fahr", f"{PC} › fahrlässig, § 276 Abs. 2 BGB"), ("anders", f"{PC} › angerempelt? Beweis: Erhard")], [
    *tafel("w280", "Schadensersatz, § 280 Abs. 1"),
    *w280,
    *okw("Vertretenmüssen vermutet: Erhard muss sich entlasten", w280_y + 30, beim("vm", "Vertretenmüssen"),
         beim("vm", "vermutet"), "Bold", 32),
    *okw("fahrlässig: nasse Flasche, eine Hand, Blick aufs Handy", w280_y + 96, "fahr", beim("fahr", "fahrlässig"),
         "Bold", 32),
    zit("§ 276 Abs. 2 BGB: im Verkehr erforderliche Sorgfalt außer Acht gelassen", 185, w280_y + 144, beim("fahr", "fahrlässig")),
    blk(110, w280_y + 200, 1040, 120, HELLGRAU, "anders", [("angerempelt? Dann kann das Verschulden fehlen –", "Bold", 30, INK),
                                                          ("das müsste Erhard aber beweisen.", "Bold", 30, INK)]),
    *requisit([("w280", ("tabler", "receipt", 110, WEISS), "Schadensersatz", WEISS),
               ("vm", ("ph", "scales", 130, WEISS), "Beweis: Erhard", HELLROT),
               ("fahr", ("tabler", "device-mobile", 80, BLAUHELL), "Blick aufs Handy", BLAUHELL),
               ("anders", ("tabler", "users", 130, WEISS), "angerempelt?", WEISS)]),
    *stehend("EH", FX, [("w280", "ernst"), ("vm", "sorge"), ("fahr", "still"), ("anders", "denkt")]),
])
assert w280_y + 200 + 130 <= 895, w280_y

# ===========================================================================================================================
# F4 § 823 Abs. 1 BGB daneben; Beweislast im Vergleich (BGHZ 66, 51, Gründe IV.)
# ===========================================================================================================================
PD = "III. Delikt"
folie([("d823", f"{PD} · § 823 Abs. 1 BGB: Eigentum verletzt"), ("beweis", f"{PD} › Beweisvorteil der culpa in contrahendo")], [
    *tafel("d823", "Daneben: Delikt"),
    *okw("§ 823 Abs. 1 BGB: fahrlässig fremdes Eigentum verletzt", 172, "d823", beim("d823", "Eigentum"), "Bold", 32),
    blk(110, 250, 510, 46 + 3 * 40, HELLGRUEN, beim("d823", "Dort"),
        [("culpa in contrahendo", "ExtraBold", 30, INK), ("Verschulden vermutet:", "Bold", 28, INK),
         ("Erhard entlastet sich", "Bold", 28, INK)]),
    blk(640, 250, 510, 46 + 3 * 40, HELLROT, beim("d823", "Dort"),
        [("Delikt, § 823 Abs. 1", "ExtraBold", 30, INK), ("Verschulden beweist", "Bold", 28, INK),
         ("der Markt", "Bold", 28, INK)]),
    blk(110, 470, 1040, 120, GELB, "beweis", [("Beweisvorteil schon im Gemüseblatt-Fall", "ExtraBold", 31, INK),
                                             ("(damals: Beweislastumkehr nach § 282 BGB a. F.)", "Bold", 28, INK)]),
    zit("BGH, Urt. v. 28.1.1976 – VIII ZR 246/74, BGHZ 66, 51, Gründe IV.", 110, 604, beim("beweis", "Bundesgerichtshof")),
    *requisit([("d823", ("tabler", "bottle", 90, MILCH), "Eigentum des Marktes", WEISS),
               ("beweis", ("ph", "scales", 130, WEISS), "Beweislast", GELB)]),
    *stehend("KE", FX, [("d823", "ernst"), ("beweis", "denkt")]),
])

# ===========================================================================================================================
# G Gegenrichtung: Schutzpflicht des Ladens (BGHZ 66, 51, Gründe V. 1, V. 4); Verweis Folge 031
# ===========================================================================================================================
PG = "Gegenrichtung"
folie([("gegen", f"{PG} · Rücksicht gilt auch für den Laden"), ("gb", f"{PG} › Gemüseblatt-Fall"),
       ("mutter", f"{PG} › Laden haftet schon vor dem Kauf"), ("v031", f"{PG} › Folge „Gemüseblatt-Fall“")], [
    *tafel("gegen", "Umgekehrt: Pflicht des Ladens"),
    z("Die Rücksichtspflicht gilt auch umgekehrt.", 110, 172, "gegen", "ExtraBold", 34),
    z("Gemüseblatt-Fall: Mädchen rutscht in der", 110, 250, "gb", "Bold", 33),
    z("Kassenzone auf einem Gemüseblatt aus", 110, 298, beim("gb", "Kassenzone"), "Bold", 33),
    *okw("wäre die Mutter gestürzt: Laden haftet aus c. i. c.", 380, "mutter", beim("mutter", "gehaftet"), "Bold", 32),
    z("obwohl der Kaufvertrag noch nicht geschlossen war", 185, 432, beim("mutter", "obwohl"), "Regular", 32),
    zit("BGH, Urt. v. 28.1.1976 – VIII ZR 246/74, BGHZ 66, 51, Gründe V. 1, V. 4", 110, 486, beim("mutter", "obwohl")),
    blk(110, 560, 1040, 90, LILAHELL, "v031", [("Schutz des Kindes: Folge „Gemüseblatt-Fall“", "ExtraBold", 32, INK)]),
    *requisit([("gegen", ("tabler", "arrows-exchange", 120, WEISS), "in beide Richtungen", WEISS),
               ("gb", ("fluent-emoji-high-contrast", "leafy-green", 120, GRUEN_P), "Gemüseblatt", HELLGRUEN),
               ("mutter", ("tabler", "building-store", 130, WEISS), "Laden haftet", HELLROT),
               ("v031", ("tabler", "book", 120, LILAHELL), "Schutz des Kindes", LILAHELL)]),
    *stehend("KE", FX, [("gegen", "ruhig"), ("gb", "sorge"), ("mutter", "ernst")]),
])

# ===========================================================================================================================
# H Ergebnis: zurück im Gang
# ===========================================================================================================================
folie([("erg", "Ergebnis · kein Kaufpreis"), ("erg2", "Ergebnis › Schadensersatz: c. i. c. und Delikt"),
       ("erg3", "Ergebnis › nicht als Käufer, sondern als Schädiger")], [
    *kuehlregal("erg"),
    *scherben("erg"),
    *fig("EH", EHX, BODEN, FH, [("erg", "erleichtert_r"), ("erg2", "ernst_r"), ("erg3", "still_r")], erst="cut"),
    hart(ns(NAME["EH"], EHX, BODEN, "erg", NFARBE["EH"])),
    *fig("KE", KEX, BODEN, FH, [("erg", "ruhig"), ("erg2", "froh")], erst="cut"),
    hart(ns(NAME["KE"], KEX, BODEN, "erg", NFARBE["KE"])),
    *neinz("kein Kaufpreis: kein Kaufvertrag", 30, "erg", "Bold", 34, x=850, rechts=1880, kreuz=beim("erg", "nicht")),
    *okz("Schadensersatz für die Flasche: c. i. c. und Delikt", 88, "erg2", "Bold", 32, x=850, rechts=1880),
    zit("§§ 280 Abs. 1, 241 Abs. 2, 311 Abs. 2 BGB; § 823 Abs. 1 BGB", 850, 140, beim("erg2", "culpa"), rechts=1880),
    blk(800, 190, 1080, 80, GELB, "erg3", [("nicht als Käufer, sondern als Schädiger", "ExtraBold", 34, INK)]),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Streit nur entscheiden, wenn nötig"), ("tipp2", "Klausurtipp · gleiches Ergebnis: offenlassen"),
       ("tipp3", "Klausurtipp · weiter prüfen: c. i. c. und Delikt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Streit nur entscheiden, wenn es darauf ankommt", 200, 200, beim("tipp", "Entscheide"), "Bold", 34),
    z("gleiches Ergebnis: kurz darstellen, offenlassen", 200, 290, "tipp2", "Bold", 34),
    zit("wie BGHZ 66, 51, Gründe V. 1", 200, 340, beim("tipp2", "Bundesgerichtshof")),
    linienzug([(130, 418), (1130, 418)], "tipp3", breite=3),
    z("Kaufpreis gescheitert? Weiter prüfen:", 200, 448, "tipp3", "ExtraBold", 35),
    *okz("culpa in contrahendo", 518, beim("tipp3", "culpa"), "Bold", 34, x=245),
    *okz("Delikt", 578, beim("tipp3", "Delikt"), "Bold", 34, x=245),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kaufpreis, § 433 Abs. 2 BGB", True),
          ("s1a", 1, "Vertragsschluss im Selbstbedienungsladen: umstritten", False),
          ("s1b", 1, "nach beiden Ansichten erst an der Kasse", False),
          ("s1c", 1, "hier: kein Vertrag, kein Kaufpreis", False),
          ("s2", 0, "II. Schadensersatz aus c. i. c., §§ 280 Abs. 1, 241 Abs. 2, 311 Abs. 2 BGB", True),
          ("s2a", 1, "1. Schuldverhältnis durch Anbahnung", False),
          ("s2b", 1, "2. Pflichtverletzung", False),
          ("s2c", 1, "3. vermutetes Vertretenmüssen, § 280 Abs. 1 Satz 2", False),
          ("s2d", 1, "4. Schaden", False),
          ("s3", 0, "III. Delikt, § 823 Abs. 1 BGB: Markt beweist das Verschulden", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Markt gegen Erhard"), 110, 90, "sch", 44)]
y = 190
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 36 if ebene == 0 else 34, rechts=1800))
    y += {0: 86, 1: 70}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Kaufpreis"), ("s2", "Prüfungsschema › II. culpa in contrahendo"),
       ("s3", "Prüfungsschema › III. Delikt")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im Supermarkt kaufst du", 0)], [("erst an der ", 0), ("Kasse", "a"), (".", 0)]],
                750, 265, 44, "merke", {"a": beim("merke", "Kasse")}),
    *markertext([[("Bis dahin schuldest du keinen", 0)], [("Kaufpreis", "b"), (", aber Rücksicht auf die", 0)],
                 [("Ware, und für verschuldete Schäden", 0)], [("haftest du schon im ", 0), ("Gang", "c"), (".", 0)]],
                750, 470, 44, "merk2", {"b": beim("merk2", "Kaufpreis"), "c": beim("merk2", "Gang")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
