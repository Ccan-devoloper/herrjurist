"""Folge 276 · Invitatio ad offerendum: Ist der Preis im Schaufenster ein Angebot? · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Edelgard sieht am Samstagvormittag im Schaufenster eines kleinen Modegeschäfts (fiktiv, Schild nur „Mode“, keine
Marke) eine Wolljacke mit Preisschild 20 €; gemeint waren 200 €. Im Laden verlangt sie von Herrn Böckmann (Inhaber) die Jacke
für 20 €; er lehnt ab. Danach: Anspruch § 433 Abs. 1 Satz 1, Wortlautkarte § 145 (Rechtsbindungswille, invitatio),
Wortlautkarten §§ 133, 157 (verständiger Empfänger), Schaufenster/Katalog/Prospekt = invitatio (h. M., Gründe BGH 1 StR 146/17
Rn. 21), Angebot der Kundin und Ablehnung (§ 146), Abgrenzung Selbstbedienungsladen (Streit), SB-Tankstelle, Warenautomat,
Onlineshop (Folge 251), Sofort kaufen (Folge 255), Ergebnis mit Preisangabenrecht, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 255 (gemeinsame Dateien unverändert); neu: ladenfront(), preisschild(), laden().
Handlungsgeräusch: Ladenglocke (A2, Edelgard betritt den Laden); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_276/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_276/" in n:
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
NAME = {"ED": "Edelgard", "BO": "Herr Böckmann"}
BLAU_P, LILA_P, ROT_P = (141, 179, 242, 255), (184, 169, 245, 255), (240, 122, 106, 255)
NFARBE = {"ED": ROT_P, "BO": BLAU_P}
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
# Schauplätze: Ladenfront mit Schaufenster (A1) und Verkaufsraum (A2, H) – programmatisch, ohne Namen oder Marke
# ===========================================================================================================================
FASSADE = (253, 240, 214, 255)
JACKE = (184, 169, 245, 255)                 # Wolljacke im Schaufenster (Lila), Edelgard trägt Rot


def ladenfront(cue):
    return [boden(cue),
            hart(feld(70, 120, 1020, BODEN - 124, cue, fill=FASSADE, rand=5, rund=6, name="fassade")),
            hart(feld(170, 140, 560, 84, cue, fill=GELB, rand=4, rund=12, name="ladenschild")),
            hart(z("Mode", 450 - F("ExtraBold", 50).getlength("Mode") / 2, 150, cue, "ExtraBold", 50)),
            hart(feld(130, 260, 640, 520, cue, fill=BLAUHELL, rand=6, rund=8, name="schaufenster")),
            hart(feld(130, 770, 640, 22, cue, fill=HELLGRAU, rand=4, rund=4, name="fensterbank")),
            hart(feld(850, 300, 190, BODEN - 304, cue, fill=HOLZ, rand=5, rund=10, name="ladentuer")),
            hart(feld(1000, 580, 20, 20, cue, fill=GELB, rand=3, rund=10, name="tuerknauf")),
            hart(linienzug([(330, 270), (330, 330)], cue, breite=4, farbe=INK)),
            ficon("tabler", "hanger", 330, 410, 150, cue, fuell=None, anim="cut"),
            ficon("tabler", "jacket", 330, 720, 290, cue, fuell=JACKE, anim="cut")]


def preisschild(cue, text_cue, bis=None):
    """Preisschild neben der Jacke; der Preis erscheint erst zum gesprochenen Wort."""
    return [bis_(hart(feld(520, 600, 200, 96, cue, fill=WEISS, rand=4, rund=12, name="preisschild")), bis),
            bis_(z("20 €", 620 - F("ExtraBold", 52).getlength("20 €") / 2, 610, text_cue, "ExtraBold", 52, rechts=760), bis)]


def laden(cue):
    """Verkaufsraum: Kleiderstange mit Jacken links, Ladentheke mit Kasse, Ladentür rechts."""
    els = [boden(cue),
           hart(feld(70, 330, 520, 16, cue, fill=HELLGRAU, rand=4, rund=6, name="kleiderstange")),
           hart(feld(90, 346, 14, BODEN - 350, cue, fill=HELLGRAU, rand=3, rund=4, name="staender1")),
           hart(feld(556, 346, 14, BODEN - 350, cue, fill=HELLGRAU, rand=3, rund=4, name="staender2"))]
    for i, f_ in enumerate(((143, 214, 148, 255), JACKE, (141, 179, 242, 255), (249, 213, 110, 255))):
        els.append(ficon("tabler", "jacket", 175 + i * 110, 560, 120, cue, fuell=f_, anim="cut"))
    els += [hart(feld(610, 640, 360, BODEN - 644, cue, fill=HOLZ, rand=5, rund=10, name="theke")),
            ficon("ph", "cash-register", 790, 640, 170, cue, fuell=WEISS, anim="cut"),
            hart(feld(1700, 330, 170, BODEN - 334, cue, fill=HOLZ, rand=5, rund=10, name="tuer_innen")),
            hart(feld(1720, 580, 18, 18, cue, fill=GELB, rand=3, rund=9, name="knauf_innen"))]
    return els


# ===========================================================================================================================
# A1 Vor dem Schaufenster: Jacke für 20 € statt 200 €
# ===========================================================================================================================
EDX = 1420
folie([(NULL, "Fall · Vor dem Schaufenster"), ("edel", "Fall · Edelgard vor dem Modegeschäft"),
       ("schild", "Fall · Preisschild: 20 €"), ("null", "Fall · gemeint waren 200 €")], [
    *ladenfront(NULL),
    *preisschild(NULL, beim("fall", "zwanzig")),
    pl("statt 200 €?", 620, 520, beim("fall", "zweihundert"), fill=HELLROT, size=32, anker="m", bis="edel"),
    pl("Samstagvormittag", 1160, 40, beim("edel", "Samstagvormittag"), fill=GELB, size=30),
    pl("Wolljacke", 330, 720, beim("schild", "Wolljacke"), fill=WEISS, size=28, anker="m"),
    pl("Preisschild: 20 €", 1420, 200, "schild", fill=WEISS, size=32, anker="m", bis="null"),
    pl("gemeint: 200 €", 1420, 200, beim("null", "Gemeint"), fill=HELLROT, size=32, anker="m"),
    pl("eine Null fehlt", 1420, 270, beim("null", "Null"), fill=HELLROT, size=30, anker="m"),
    *fig("ED", EDX, BODEN, FH, [("edel", "ruhig"), (beim("schild", "zwanzig"), "staunt"), ("null", "strahlt")], erst="pop"),
    ns(NAME["ED"], EDX, BODEN, "edel", ROT_P, d=0.1),
])

# ===========================================================================================================================
# A2 Im Laden: Edelgard verlangt die Jacke für 20 €; Herr Böckmann lehnt ab – die Frage
# ===========================================================================================================================
BOX, EDL = 1080, 1440
folie([("laden", "Fall · Im Laden bei Herrn Böckmann"), ("e1", "Fall · Edelgard: „für 20 €“"),
       ("b1", "Fall · Herr Böckmann: „Die Jacke kostet 200 €“"), ("e2", "Fall · Edelgard: „Das ist Ihr Angebot“"),
       ("frage", "Die Frage · Muss er für 20 € verkaufen?"), ("frage2", "Die Frage · Preisschild schon ein Angebot?"),
       ("frage3", "Die Frage · oder nur eine Einladung?")], [
    *laden("laden"),
    hart(pl("Im Laden", 70, 30, "laden", fill=GELB, size=30, bis="frage")),
    szene(ficon("tabler", "bell", 1785, 320, 60, beim("laden", "hinein"), fuell=GELB), "276glocke*", 0.8, 0.05),
    *fig("BO", BOX, BODEN, FH, [("laden", "ruhig_r"), (beim("laden", "Inhaber"), "froh_r")], bis="b1", erst="cut"),
    *redet("BO_redet_r", BOX, BODEN, FH, "b1", "e2"),
    *fig("BO", BOX, BODEN, FH, [("e2", "sorge_r"), ("frage", "ernst_r")], erst="cut"),
    hart(ns(NAME["BO"], BOX, BODEN, "laden", BLAU_P)),
    *fig("ED", EDL, BODEN, FH, [(beim("laden", "hinein"), "froh")], bis="e1", erst="pop"),
    *redet("ED_redet", EDL, BODEN, FH, "e1", "b1"),
    *fig("ED", EDL, BODEN, FH, [("b1", "staunt")], bis="e2", erst="cut"),
    *redet("ED_beharrt", EDL, BODEN, FH, "e2", "frage"),
    *fig("ED", EDL, BODEN, FH, [("frage", "ernst")], erst="cut"),
    ns(NAME["ED"], EDL, BODEN, beim("laden", "hinein"), ROT_P, d=0.1),
    blase("sprech", 600, 210, "e1", 1250, 200, inhalt=["Ich nehme die Jacke aus dem", "Schaufenster, für 20 €."],
          textsize=31, figur=("ED_redet", EDL, BODEN, FH), bis="b1"),
    blase("sprech", 640, 210, "b1", 1000, 200, inhalt=["Das tut mir leid, auf dem Schild", "fehlt eine Null. Die Jacke",
                                                    "kostet 200 €."],
          textsize=31, figur=("BO_redet_r", BOX, BODEN, FH), bis="e2"),
    blase("sprech", 600, 210, "e2", 1250, 200, inhalt=["Im Schaufenster steht 20.", "Das ist Ihr Angebot,",
                                                     "und ich nehme es an."],
          textsize=31, figur=("ED_beharrt", EDL, BODEN, FH), bis="frage"),
    pl("Muss Herr Böckmann ihr die Jacke für 20 € verkaufen?", 70, 30, "frage", fill=PINK, size=34),
    pl("War das Preisschild schon ein Angebot?", 70, 108, "frage2", fill=PINK, size=34),
    pl("Oder nur eine Einladung, selbst eines zu machen?", 70, 186, "frage3", fill=PINK, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_276(cue, absaetze, frage, size=38):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_276("sv", [
    "Edelgard sieht am Samstagvormittag im Schaufenster eines kleinen Modegeschäfts eine Wolljacke. Auf dem Preisschild "
    "stehen 20 €. Gemeint waren 200 €; beim Beschriften ist eine Null verloren gegangen.",
    "Im Laden sagt sie zu Herrn Böckmann, dem Inhaber: „Ich nehme die Jacke aus dem Schaufenster, für 20 €.“",
    "Herr Böckmann lehnt ab: Auf dem Schild fehle eine Null, die Jacke koste 200 €. Edelgard meint, das Preisschild im "
    "Schaufenster sei sein Angebot, und sie nehme es an.",
], "Hat Edelgard Anspruch auf die Jacke für 20 €?")


# ===========================================================================================================================
# Tafel-Helfer (wie Folge 255)
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
# C Anspruch: § 433 Abs. 1 Satz 1, Kaufvertrag = Angebot und Annahme; Frage: Wer hat angeboten?
# ===========================================================================================================================
PA = "Anspruch"
folie([("ansp", f"{PA} · § 433 Abs. 1 Satz 1 BGB: Jacke für 20 €?"), ("ansp2", f"{PA} › Kaufvertrag: Angebot und Annahme"),
       ("v014", f"{PA} › Folge „Angebot und Annahme“"), ("kern", f"{PA} › Wer hat das Angebot gemacht?")], [
    *tafel("ansp", "Anspruch auf die Jacke"),
    z("Edelgard gegen Herrn Böckmann", 110, 180, "ansp", "Bold", 36),
    z("Übergabe und Übereignung der Jacke für 20 €", 110, 245, beim("ansp", "Übergabe"), "Bold", 34),
    z("§ 433 Abs. 1 Satz 1 BGB", 110, 297, beim("ansp", "Paragraf"), "ExtraBold", 36),
    blk(110, 380, 1040, 100, GELB, "ansp2", [("Voraussetzung: Kaufvertrag aus Angebot und Annahme", "ExtraBold", 31, INK)]),
    blk(110, 520, 1040, 90, LILAHELL, "v014", [("mehr dazu: Folge „Angebot und Annahme“", "ExtraBold", 32, INK)]),
    blk(110, 650, 1040, 100, HELLROT, beim("kern", "Wer"), [("Hier: Wer hat überhaupt das Angebot gemacht?", "ExtraBold", 32, INK)]),
    *requisit([("ansp", ("tabler", "jacket", 150, JACKE), "Jacke: 20 €?", WEISS),
               ("ansp2", ("tabler", "file-text", 120, WEISS), "Kaufvertrag?", GELB),
               ("kern", ("tabler", "help-circle", 120, HELLROT), "Wer bietet an?", HELLROT)], px=1560, pu=330, py=90),
    *paar("ED", [("ansp", "ruhig"), ("ansp2", "denkt")], "BO", [("ansp", "ruhig"), ("kern", "denkt")]),
])

# ===========================================================================================================================
# D1 § 145 BGB (Wortlautkarte); Rechtsbindungswille; invitatio ad offerendum (BGH III ZR 220/25 Rn. 13)
# ===========================================================================================================================
PI = "I. Angebot"
w145, w145_y = wortlaut(80, 170, 1100, "„Wer einem anderen die Schließung eines Vertrags anträgt, ist an den Antrag gebunden, "
                                       "es sei denn, dass er die Gebundenheit ausgeschlossen hat.“", "§ 145 BGB", "w145",
                        size=34, marken=[("anträgt", beim("w145", "anträgt")), ("gebunden", beim("w145", "gebunden"))])
folie([("w145", f"{PI} · Antrag und Bindung, § 145 BGB"), ("rbw", f"{PI} › Rechtsbindungswille"),
       ("inv", f"{PI} › fehlt er: invitatio ad offerendum")], [
    *tafel("w145", "Was ist ein Angebot?"),
    *w145,
    *okw("Angebot: Erklärung, mit der man sich binden will", w145_y + 30, "rbw", beim("rbw", "binden"), "Bold", 34),
    z("entscheidend: der Rechtsbindungswille", 185, w145_y + 82, beim("rbw", "Rechtsbindungswille"), "ExtraBold", 34),
    blk(110, w145_y + 160, 1040, 120, GELB, "inv", [("fehlt er: Aufforderung, selbst ein Angebot", "ExtraBold", 32, INK),
                                                   ("abzugeben – invitatio ad offerendum", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 21.5.2026 – III ZR 220/25, Rn. 13", 110, w145_y + 292, beim("inv", "Bundesgerichtshof")),
    *requisit([("w145", ("tabler", "lock", 110, GELB), "gebunden", GELB),
               ("rbw", ("tabler", "hand-stop", 110, WEISS), "Bindungswille", WEISS),
               ("inv", ("tabler", "mail-opened", 120, LILAHELL), "nur Einladung", LILAHELL)]),
    *stehend("BO", FX, [("w145", "ruhig"), ("rbw", "denkt"), ("inv", "froh")]),
])
assert w145_y + 292 + 40 <= 895, w145_y

# ===========================================================================================================================
# D2 Auslegung §§ 133, 157 BGB (Wortlautkarten); verständiger Empfänger (VIII ZR 79/04 S. 6)
# ===========================================================================================================================
w133, w133_y = wortlaut(80, 160, 1100, "„Bei der Auslegung einer Willenserklärung ist der wirkliche Wille zu erforschen und "
                                       "nicht an dem buchstäblichen Sinne des Ausdrucks zu haften.“", "§ 133 BGB", "w133",
                        size=32, marken=[("wirkliche Wille", beim("w133", "wirkliche"))])
w157, w157_y = wortlaut(80, w133_y + 18, 1100, "„Verträge sind so auszulegen, wie Treu und Glauben mit Rücksicht auf die "
                                              "Verkehrssitte es erfordern.“", "§ 157 BGB", "w157",
                        size=32, marken=[("Treu und Glauben", beim("w157", "Treu")), ("Verkehrssitte", beim("w157", "Verkehrssitte"))])
folie([("w133", f"{PI} › Auslegung, § 133 BGB"), ("w157", f"{PI} › Auslegung, § 157 BGB"),
       ("horiz", f"{PI} › Sicht eines verständigen Passanten")], [
    *tafel("w133", "Bindungswille? Auslegung"),
    *w133, *w157,
    *okw("Maßstab: verständiger Empfänger", w157_y + 26, "horiz", beim("horiz", "verständiger"), "Bold", 34),
    z("hier: ein verständiger Passant vor dem Schaufenster", 185, w157_y + 78, beim("horiz", "Passant"), "Bold", 32),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 6 (§§ 133, 157 BGB)", 185, w157_y + 128, beim("horiz", "verständiger")),
    *requisit([("w133", ("tabler", "search", 110, WEISS), "Auslegung", WEISS),
               ("horiz", ("tabler", "eye", 120, BLAUHELL), "Sicht des Passanten", BLAUHELL)]),
    *stehend("ED", FX, [("w133", "ruhig"), ("w157", "denkt"), ("horiz", "ernst")]),
])
assert w157_y + 128 + 40 <= 895, w157_y

# ===========================================================================================================================
# E Schaufenster = invitatio (h. M.); Gründe (BGH 1 StR 146/17 Rn. 21); Werbung (III ZR 220/25 Rn. 13, III ZR 62/11 Rn. 11)
# ===========================================================================================================================
folie([("schauf", f"{PI} › Schaufenster: nur Einladung"), ("gruende", f"{PI} › Grund 1: Kann er liefern?"),
       ("bonit", f"{PI} › Grund 2: Kann der Kunde zahlen?"), ("mehr", f"{PI} › Grund 3: Wie viele Kunden kommen?"),
       ("katalog", f"{PI} › ebenso Katalog und Prospekt")], [
    *tafel("schauf", "Schaufenster: nur eine Einladung"),
    *neinz("Ware im Schaufenster: kein Angebot", 172, "schauf", "Bold", 34, kreuz=beim("schauf", "kein")),
    *okw("nur Einladung (herrschende Meinung)", 226, beim("schauf", "sondern"), beim("schauf", "Einladung"), "Bold", 34),
    z("Gründe für Angebote an die Allgemeinheit:", 110, 298, "gruende", "ExtraBold", 34),
    zit("BGH, Urt. v. 25.10.2017 – 1 StR 146/17, Rn. 21", 110, 346, beim("gruende", "Bundesgerichtshof")),
    z("1. Kann er überhaupt liefern? (Vorrat)", 150, 400, beim("gruende", "liefern"), "Bold", 34),
    z("2. Kann der Kunde zahlen? (Bonität)", 150, 455, beim("bonit", "zahlen"), "Bold", 34),
    z("3. Wie viele Kunden kommen?", 150, 510, "mehr", "Bold", 34),
    blk(110, 570, 1040, 100, HELLROT, beim("mehr", "Wäre"), [("Schild als Angebot: 10 Kunden, 10-mal gebunden", "ExtraBold", 31, INK)]),
    blk(110, 700, 1040, 80, LILAHELL, "katalog", [("ebenso: Katalog und Prospekt", "ExtraBold", 32, INK)]),
    zit("Werbeschreiben: BGH III ZR 220/25, Rn. 13; Anzeige: BGH III ZR 62/11, Rn. 11", 110, 796,
        beim("katalog", "Werbeschreiben")),
    *requisit([("schauf", ("tabler", "building-store", 130, FASSADE), "Schaufenster", WEISS),
               ("gruende", ("tabler", "package", 120, HOLZ), "Vorrat?", WEISS),
               ("bonit", ("tabler", "coin-euro", 110, GELB), "zahlungsfähig?", GELB),
               ("mehr", ("tabler", "users", 130, WEISS), "10 Kunden?", HELLROT),
               ("katalog", ("tabler", "book", 120, LILAHELL), "Katalog, Prospekt", LILAHELL)]),
    *stehend("BO", FX, [("schauf", "ruhig"), ("gruende", "denkt"), ("mehr", "sorge"), ("katalog", "ruhig")]),
])

# ===========================================================================================================================
# F Angebot der Kundin; Ablehnung; Erlöschen § 146 BGB
# ===========================================================================================================================
folie([("edang", f"{PI} › Angebot: Edelgard im Laden"), ("frei", "II. Annahme? › Herr Böckmann lehnt ab, § 146 BGB"),
       ("leer", "II. Annahme? › „Ich nehme Ihr Angebot an“ geht ins Leere")], [
    *tafel("edang", "Wer hat das Angebot gemacht?"),
    *okw("Angebot: Edelgard im Laden", 175, "edang", beim("edang", "Edelgard"), "Bold", 34),
    z("„Ich nehme die Jacke für 20 €.“", 185, 227, beim("edang", "Ich"), "Bold", 34),
    z("Annahme? Das entscheidet Herr Böckmann.", 110, 320, "frei", "ExtraBold", 34),
    *neinz("Er lehnt ab: ihr Angebot erlischt", 382, beim("frei", "Er"), "Bold", 34, kreuz=beim("frei", "lehnt")),
    zit("§ 146 BGB", 185, 430, beim("frei", "Paragraf")),
    blk(110, 510, 1040, 120, HELLGRAU, "leer", [("„Ich nehme Ihr Angebot an“ geht ins Leere:", "ExtraBold", 31, INK),
                                               ("Es gab keins.", "ExtraBold", 31, INK)]),
    *requisit([("edang", ("tabler", "message", 110, ROT_P), "Angebot: Edelgard", WEISS),
               ("frei", ("tabler", "hand-stop", 110, BLAUHELL), "abgelehnt", HELLROT),
               ("leer", ("tabler", "circle-off", 110, WEISS), "kein Angebot des Händlers", WEISS)], px=1560, pu=330, py=90),
    *paar("ED", [("edang", "froh"), ("frei", "sorge"), ("leer", "still")], "BO", [("edang", "ruhig"), ("frei", "ernst")]),
])

# ===========================================================================================================================
# G1 Abgrenzung: Selbstbedienungsladen (Streit) und SB-Tankstelle (BGH VIII ZR 171/10 Rn. 13–16)
# ===========================================================================================================================
PG = "Abgrenzung"
folie([("abgr", f"{PG} · in der Klausur sauber trennen"), ("sb", f"{PG} › Selbstbedienungsladen: Regal bindet nicht"),
       ("sb1", f"{PG} › Selbstbedienung: Ansicht 1"), ("sb2", f"{PG} › Selbstbedienung: Ansicht 2"),
       ("tank", f"{PG} › Tankstelle: Kauf schon beim Tanken")], [
    *tafel("abgr", "Abgrenzung: Selbstbedienung"),
    z("Selbstbedienungsladen", 110, 172, "sb", "ExtraBold", 36),
    *neinz("Herausnehmen aus dem Regal bindet noch nicht", 232, "sb", "Bold", 33, kreuz=beim("sb", "bindet")),
    zit("BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 15", 185, 278, beim("sb", "Bundesgerichtshof")),
    z("Wie der Vertrag an der Kasse entsteht: umstritten", 110, 334, "sb1", "Bold", 33),
    blk(110, 392, 510, 150, BLAUHELL, beim("sb1", "Nach"), [("Ansicht 1:", "ExtraBold", 30, INK),
                                                            ("Regal = Angebot,", "Bold", 30, INK),
                                                            ("Annahme: Vorlegen an Kasse", "Bold", 30, INK)]),
    blk(640, 392, 510, 150, LILAHELL, "sb2", [("Ansicht 2:", "ExtraBold", 30, INK), ("Regal = Einladung,", "Bold", 30, INK),
                                             ("Angebot an der Kasse", "Bold", 30, INK)]),
    blk(110, 590, 1040, 140, GELB, "tank", [("Selbstbedienungstankstelle:", "ExtraBold", 32, INK),
                                           ("Kauf schon beim Tanken – Einfüllen", "Bold", 31, INK),
                                           ("praktisch nicht rückgängig zu machen", "Bold", 31, INK)]),
    zit("BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 13, 16", 110, 744, beim("tank", "Bundesgerichtshof")),
    *requisit([("abgr", ("tabler", "arrows-split", 110, WEISS), "Abgrenzung", WEISS),
               ("sb", ("tabler", "shopping-cart", 130, WEISS), "Regal", WEISS),
               ("sb1", ("ph", "cash-register", 130, WEISS), "Kasse", BLAUHELL),
               ("tank", ("tabler", "gas-station", 120, GELB), "Tankstelle", GELB)]),
    *stehend("ED", FX, [("abgr", "ruhig"), ("sb", "denkt"), ("sb2", "ernst"), ("tank", "staunt")]),
])

# ===========================================================================================================================
# G2 Abgrenzung: Warenautomat (überwiegende Ansicht), Onlineshop (Folge 251), Sofort kaufen (Folge 255)
# ===========================================================================================================================
folie([("auto", f"{PG} › Warenautomat: Angebot an jeden"), ("shop", f"{PG} › Onlineshop: nur Einladung"),
       ("platt", f"{PG} › Sofort kaufen: Angebot des Verkäufers")], [
    *tafel("auto", "Abgrenzung: Automat und online"),
    *okw("Warenautomat: Angebot an jeden", 172, "auto", beim("auto", "Angebot"), "Bold", 34),
    z("überwiegende Ansicht; solange Ware da ist", 185, 222, beim("auto", "überwiegende"), "Regular", 32),
    z("und der Automat funktioniert", 185, 266, beim("auto", "solange"), "Regular", 32),
    *neinz("Onlineshop: nur Einladung", 340, "shop", "Bold", 34, kreuz=beim("shop", "Einladung")),
    z("Angebot = deine Bestellung", 185, 390, beim("shop", "Angebot"), "Regular", 32),
    zit("BGH VIII ZR 79/04, S. 5; X ZR 37/12, Rn. 14", 185, 436, beim("shop", "Bestellung")),
    blk(185, 478, 965, 76, LILAHELL, beim("shop", "wie"), [("Folge „Preisfehler im Onlineshop“", "ExtraBold", 30, INK)]),
    *okw("Sofort kaufen: Angebot des Verkäufers", 600, "platt", beim("platt", "bietet"), "Bold", 34),
    z("zu einem festen Preis", 185, 650, beim("platt", "festen"), "Regular", 32),
    zit("BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 12", 185, 696, beim("platt", "festen")),
    blk(185, 738, 965, 76, LILAHELL, beim("platt", "das"), [("Folge „Sofort kaufen“", "ExtraBold", 30, INK)]),
    *requisit([("auto", ("tabler", "coins", 120, GELB), "Automat", GELB),
               ("shop", ("tabler", "shopping-cart", 130, WEISS), "Onlineshop", WEISS),
               ("platt", ("tabler", "hand-click", 120, WEISS), "Sofort kaufen", GELB)]),
    *stehend("BO", FX, [("auto", "ruhig"), ("shop", "denkt"), ("platt", "froh")]),
])

# ===========================================================================================================================
# H Ergebnis: zurück im Laden; Preisangabenrecht in einem Satz (§ 10 Abs. 1, § 20 Nr. 1 PAngV)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Preisschild: kein Angebot"), ("erg2", "Ergebnis › kein Anspruch auf die Jacke für 20 €"),
       ("pangv", "Ergebnis › Preisangabenrecht: kein Kaufvertrag")], [
    *laden("erg"),
    *fig("BO", BOX, BODEN, FH, [("erg", "ruhig_r"), ("pangv", "denkt_r")], erst="cut"),
    hart(ns(NAME["BO"], BOX, BODEN, "erg", BLAU_P)),
    *fig("ED", EDL, BODEN, FH, [("erg", "ernst"), ("erg2", "still"), ("pangv", "denkt")], erst="cut"),
    hart(ns(NAME["ED"], EDL, BODEN, "erg", ROT_P)),
    *neinz("Preisschild im Schaufenster: kein Angebot", 30, "erg", "Bold", 34, x=130, rechts=1880, kreuz=beim("erg", "kein")),
    *neinz("Herr Böckmann musste nicht annehmen", 88, "erg2", "Bold", 34, x=130, rechts=1880),
    *neinz("kein Anspruch auf die Jacke für 20 €", 146, beim("erg2", "Ohne"), "Bold", 34, x=130, rechts=1880),
    zit("§ 433 Abs. 1 Satz 1 BGB; §§ 145, 146 BGB", 130, 196, beim("erg2", "Ohne"), rechts=1880),
    blk(1000, 236, 880, 80, HELLGRAU, "pangv", [("falsches Preisschild: ggf. Verstoß gegen die PAngV", "Bold", 28, INK)]),
    z("aber kein Kaufvertrag zu 20 €", 1030, 368, beim("pangv", "einen"), "ExtraBold", 30, rechts=1880),
    zit("§ 10 Abs. 1, § 20 Nr. 1 PAngV", 1030, 326, beim("pangv", "Preisangabenverordnung"), rechts=1880),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · nicht sofort zur Anfechtung"), ("tipp2", "Klausurtipp · zuerst: Wer hat angeboten?"),
       ("tipp3", "Klausurtipp · invitatio sauber begründen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("falscher Preis: nicht sofort zur Anfechtung", 200, 200, beim("tipp", "Spring"), "Bold", 35),
    z("zuerst prüfen: Wer hat das Angebot gemacht?", 200, 290, "tipp2", "Bold", 34),
    z("nur Einladung: Der Händler hat nichts erklärt,", 200, 345, beim("tipp2", "War"), "Regular", 33),
    z("was er anfechten müsste", 200, 393, beim("tipp2", "anfechten"), "Regular", 33),
    linienzug([(130, 468), (1130, 468)], "tipp3", breite=3),
    z("Einladung begründen:", 200, 498, "tipp3", "ExtraBold", 35),
    *okz("fehlender Rechtsbindungswille", 568, beim("tipp3", "fehlenden"), "Bold", 34, x=245),
    *neinz("nicht bloß das Wort „Schaufenster“", 628, beim("tipp3", "nicht"), "Bold", 34, x=245),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kaufvertrag", True),
          ("s1a", 1, "Angebot durch das Schaufenster? Nein: nur invitatio ad offerendum,", False),
          (beim("s1a", "denn"), 2, "denn es fehlt der Rechtsbindungswille", False),
          ("s1b", 2, "Auslegung nach §§ 133, 157 BGB", False),
          ("s1c", 1, "Angebot erst durch Edelgard im Laden", False),
          ("s1d", 1, "keine Annahme: Herr Böckmann lehnt ab", False),
          ("s2", 0, "II. Ergebnis: kein Anspruch", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Edelgard gegen Herrn Böckmann"), 110, 90, "sch", 44),
           z("auf Übergabe und Übereignung der Jacke", 110, 158, beim("sch", "Übergabe"), "Bold", 36, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 100, 1: 84, 2: 76}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Kaufvertrag"), ("s1c", "Prüfungsschema › I. Angebot der Kundin"),
       ("s2", "Prüfungsschema › II. Ergebnis")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ware im Schaufenster, im Katalog", 0)], [("oder im Prospekt ist in der Regel", 0)],
                 [("kein Angebot", "a"), (", sondern eine ", 0), ("Einladung", "b"), (",", 0)], [("eines abzugeben.", 0)]],
                750, 265, 44, "merke", {"a": beim("merke", "kein"), "b": beim("merke", "Einladung")}),
    *markertext([[("Das Angebot macht der ", 0), ("Kunde", "c"), (",", 0)], [("und ob er es annimmt,", 0)],
                 [("entscheidet der ", 0), ("Händler", "d"), (".", 0)]],
                750, 580, 44, "merk2", {"c": beim("merk2", "Kunde"), "d": beim("merk2", "Händler")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
