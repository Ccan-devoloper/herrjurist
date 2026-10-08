"""Folge 262 · Unfallwagen verschwiegen: Arglistige Täuschung oder Mängelrechte? · Serienstandard Open Peeps (Katzenkönig).
Fall: Angelika, selbständige Hebamme, kauft für ihre Hausbesuche beim (fiktiven) Gebrauchtwagenhändler Herrn Hecker einen
Kombi für 8.000 € unter Ausschluss jeder Gewährleistung. Herr Hecker hatte den Wagen als Unfallwagen angekauft und den
schweren Frontschaden in seiner eigenen Werkstatt reparieren lassen; er schweigt, Angelika fragt nicht. Drei Monate später
entdeckt der Prüfer bei der Hauptuntersuchung den reparierten Unfallschaden; eine Woche danach ficht Angelika schriftlich an.
Danach: zwei Wege; § 123 Abs. 1 (Wortlautkarte), Täuschung durch Unterlassen (Aufklärungspflicht, Gebrauchtwagen,
Bagatellschaden), Irrtum und Kausalität, Arglist; § 124 Abs. 1, 2 (Wortlautkarte), § 143; § 142 Abs. 1 (Wortlautkarte),
§ 812, Verweis Folge 023; Verhältnis zu den Mängelrechten (keine Sperre bei Arglist; § 119 Abs. 2 h. M.); § 14, § 476,
§ 444 (Wortlautkarte); Vergleich Anfechtung/Rücktritt (§§ 346, 325, 326 Abs. 5; Verweis Folgen 063, 236); Klausurtipp
(BGH VIII ZR 37/24); Schema; Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/mitte/schild/
absatz_nb/requisit/stehend/paar/okw als eigene Kopie aus Folge 259 (gemeinsame Dateien unverändert); neu: kombi(),
werkstatt(), Hebebühne aus Grundformen.
Darstellung: keine echten Automarken (Tabler car, ohne Logo), kein Unfall im Bild – der Schaden erscheint nur als
Werkstatt-Symbol (Phosphor garage/wrench) und als Lupe des Prüfers. Keine Richterhämmer.
Handlungsgeräusche: Unterschrift, Hebebühne, Brief (Freesound CC0, ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_262/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_262/" in n:
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
NAME = {"AN": "Angelika", "HK": "Herr Hecker", "PR": "Prüfer"}
BLAU_P, LILA_P = (141, 179, 242, 255), (184, 169, 245, 255)
GRUEN_P, ROT_P = (143, 214, 148, 255), (240, 122, 106, 255)
NFARBE = {"AN": ROT_P, "HK": BLAU_P, "PR": GRUEN_P}


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


def mitte(text, cx, y, cue, stil="Bold", size=34, **k):
    """Zentrierte Zeile (Felder, Schilder)."""
    return z(text, cx - F(stil, size).getlength(glyphen(text)) / 2, y, cue, stil, size, rechts=k.pop("rechts", 1880), **k)


def schild(text, x, y, cue, w=None, size=38, fill=GELB, bis=None):
    """Ladenschild (Grundform, fiktiver Laden, kein Logo)."""
    w = w or int(F("ExtraBold", size).getlength(glyphen(text))) + 60
    return [bis_(hart(feld(x, y, w, int(size * 1.9), cue, fill=fill, rand=5, rund=12, name="schild")), bis),
            bis_(hart(mitte(text, x + w / 2 + 6, y + size * 0.42, cue, "ExtraBold", size)), bis)]


def absatz_nb(text, x, y, breite, cue, size=38, stil="Regular", zeilenabstand=1.35, farbe=INK):
    """Wie bausteine.absatz, aber Umbruch nur an normalen Leerzeichen (geschütztes Leerzeichen hält „900 €“ zusammen)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split(" "):
        t = (cur + " " + w).strip(" ")
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    if cur:
        zeilen.append(cur)
    els = [OT(z_, x, y + i * size * zeilenabstand, cue, stil, size, farbe=farbe, anim="fade") for i, z_ in enumerate(zeilen)]
    return els, y + len(zeilen) * size * zeilenabstand


def sachverhalt_262(cue, absaetze, frage, size=34):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz_nb(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


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





def kombi(cx, unten, breite, cue, bis=None, anim="cut", d=0.0):
    """Der Kombi: Tabler car (ohne Marke), Palettenfüllung Gelb, Fenster weiß."""
    return ficon("tabler", "car", cx, unten, breite, cue, fuell=GELB, nebenfarbe=WEISS, bis=bis, anim=anim, d=d)


def werkstatt(cx, unten, breite, cue, bis=None, anim="cut"):
    """Werkstatt-Symbol (Phosphor garage) – der Unfallschaden erscheint nie als Unfall, nur als Werkstatt."""
    return ficon("ph", "garage", cx, unten, breite, cue, fuell=HELLGRAU, nebenfarbe=WEISS, bis=bis, anim=anim)


# ===========================================================================================================================
# A Fall: beim Gebrauchtwagenhändler (fall … unterschr)
# ===========================================================================================================================
ANX, CARX, HKX, GX = 430, 950, 1480, 1775
folie([(NULL, "Fall · Beim Gebrauchtwagenhändler"), ("vorher", "Fall · Vorher: Unfallschaden in eigener Werkstatt repariert"),
       ("h1", "Fall · Herr Hecker: „ohne jede Gewährleistung“"), ("kauf", "Fall · Keine Frage, kein Hinweis"),
       ("unterschr", "Fall · Kaufvertrag unterschrieben")], [
    boden(NULL), *schild("Autohandel Hecker", 70, 40, NULL),
    werkstatt(GX, BODEN + 4, 190, NULL),
    ficon("tabler", "car", 175, BODEN + 4, 230, NULL, fuell=BLAU_P, nebenfarbe=WEISS, anim="cut"),   # weiterer Gebrauchtwagen
    hart(pl("Werkstatt", GX, 610, NULL, fill=WEISS, size=26, anker="m")),
    # Angelika (links, blickt nach rechts zum Kombi und zu Herrn Hecker)
    *fig("AN", ANX, BODEN, FH, [(NULL, "ruhig_r"), (beim("fall", "Hausbesuche"), "froh_r"), ("hof", "staunt_r"),
                                (beim("hof", "achttausend"), "froh_r"), ("vorher", "ruhig_r"), ("h1", "denkt_r"),
                                ("kauf", "ruhig_r"), ("unterschr", "froh_r")], erst="cut"),
    hart(ns(NAME["AN"], ANX, BODEN, NULL, NFARBE["AN"])),
    pl("selbständige Hebamme", ANX, 330, beim("fall", "Hebamme"), fill=WEISS, size=30, anker="m", bis="vorher"),
    ficon("tabler", "home", ANX - 120, 300, 70, beim("fall", "Hausbesuche"), fuell=GELB, bis="vorher"),
    pl("Hausbesuche", ANX + 40, 250, beim("fall", "Hausbesuche"), fill=GELB, size=30, anker="m", bis="vorher"),
    # Herr Hecker und der Kombi
    *fig("HK", HKX, BODEN, FH, [(beim("hof", "Herrn"), "froh"), ("vorher", "denkt")], bis="h1", erst="pop"),
    *redet("HK_redet", HKX, BODEN, FH, "h1", "kauf"),
    *fig("HK", HKX, BODEN, FH, [("kauf", "ruhig"), ("unterschr", "froh")], erst="cut"),
    ns(NAME["HK"], HKX, BODEN, beim("hof", "Herrn"), NFARBE["HK"], d=0.1),
    kombi(CARX, BODEN + 4, 440, beim("hof", "Kombi"), anim="pop"),
    pl("Kombi", CARX, 470, beim("hof", "Kombi"), fill=WEISS, size=32, anker="m", bis=beim("hof", "achttausend")),
    pl("Kombi: 8.000 €", CARX, 470, beim("hof", "achttausend"), fill=GELB, size=36, anker="m", anim="cut"),
    # Rückblick: Unfallwagen angekauft, Frontschaden in der eigenen Werkstatt repariert
    feld(560, 90, 800, 250, "vorher", fill=BLAUHELL, rand=5, rund=18, anim="pop", bis="h1", name="rueckblick"),
    z("Was Angelika nicht weiß:", 600, 115, "vorher", "ExtraBold", 32, rechts=1340, bis="h1"),
    z("Herr Hecker kaufte den Wagen als Unfallwagen an", 600, 180, beim("vorher", "Unfallwagen"), "Bold", 28,
      rechts=1340, bis="h1"),
    z("und ließ den Frontschaden in seiner eigenen", 600, 228, beim("vorher", "Frontschaden"), "Bold", 28, rechts=1340,
      bis="h1"),
    z("Werkstatt reparieren", 600, 276, beim("vorher", "Werkstatt"), "Bold", 28, rechts=1340, bis="h1"),
    ficon("ph", "wrench", GX, 560, 80, beim("vorher", "Werkstatt"), fuell=GELB, bis="kauf"),
    blase("sprech", 760, 220, "h1", 1000, 250, inhalt=["8.000 €, aber ohne", "jede Gewährleistung."], textsize=36,
          figur=("HK_redet", HKX, BODEN, FH), bis="kauf"),
    # keine Frage, kein Hinweis
    pl("fragt nicht nach Unfällen", ANX, 300, beim("kauf", "fragt"), fill=HELLROT, size=28, anker="m"),
    ficon("tabler", "message-off", HKX, 395, 86, beim("kauf", "sagt"), fuell=WEISS),
    pl("sagt nichts", HKX, 240, beim("kauf", "sagt"), fill=HELLROT, size=28, anker="m"),
    # Unterschrift
    szene(ficon("tabler", "contract", CARX, 400, 110, "unterschr", fuell=WEISS), "262unterschrift*", 0.7, 0.05),
    pl("Gewährleistung ausgeschlossen", CARX, 200, beim("unterschr", "unterschreibt"), fill=GELB, size=28, anker="m"),
])

# ===========================================================================================================================
# B Drei Monate später: Hauptuntersuchung (hu … a1)
# ===========================================================================================================================
ANB, CARB, PRX = 360, 960, 1530
PLAT = 650                                  # Oberkante der Hebebühne (gehoben)
HUB = 130                                   # Hubhöhe
H0, H1 = beim("hu", "Hauptuntersuchung"), (beim("hu", "Hauptuntersuchung")[0], beim("hu", "Hauptuntersuchung")[1] + 1.8)
folie([("hu", "Fall · Drei Monate später: Hauptuntersuchung"), ("p1", "Fall · Prüfer: „Unfallschaden repariert“"),
       ("a1", "Fall · Angelika: „Ich will mein Geld zurück“")], [
    boden("hu"),
    hart(pl("3 Monate später", 70, 30, "hu", fill=GELB, size=30)),
    pl("Hauptuntersuchung", 70, 100, H0, fill=WEISS, size=30),
    # Hebebühne (Grundformen): zwei Säulen, Plattform hebt den Kombi
    hart(feld(CARB - 300, 420, 34, BODEN - 424, "hu", fill=HELLGRAU, rand=4, rund=6, name="saeule1")),
    hart(feld(CARB + 266, 420, 34, BODEN - 424, "hu", fill=HELLGRAU, rand=4, rund=6, name="saeule2")),
    szene(bewegt(hart(feld(CARB - 262, PLAT, 524, 24, "hu", fill=HELLGRAU, rand=4, rund=6, name="plattform")),
                 H0, H1, 0, HUB), "262hebebuehne*", 0.6, 0.0),
    bewegt(kombi(CARB, PLAT + 4, 420, "hu"), H0, H1, 0, HUB),
    # Prüfer (rechts, blickt nach links zum Kombi und zeigt darauf)
    *fig("PR", PRX, BODEN, FH, [("hu", "ruhig")], bis="p1", erst="pop"),
    *redet("PR_redet", PRX, BODEN, FH, "p1", "a1"),
    *fig("PR", PRX, BODEN, FH, [("a1", "ernst")], erst="cut"),
    ns(NAME["PR"], PRX, BODEN, "hu", NFARBE["PR"], d=0.1),
    blase("sprech", 700, 250, "p1", 1180, 250, inhalt=["Hier wurde ein schwerer", "Unfallschaden repariert."],
          textsize=34, figur=("PR_redet", PRX, BODEN, FH), bis="a1"),
    ficon("tabler", "zoom-exclamation", CARB + 110, PLAT - 70, 96, beim("p1", "Unfallschaden"), fuell=WEISS),
    ficon("ph", "wrench", CARB - 70, PLAT - 70, 80, beim("p1", "repariert"), fuell=WEISS),
    # Angelika (links, blickt nach rechts)
    *fig("AN", ANB, BODEN, FH, [("hu", "ruhig_r"), (beim("p1", "Unfallschaden"), "staunt_r")], bis="a1", erst="pop"),
    *redet("AN_redet_r", ANB, BODEN, FH, "a1", "brief"),
    ns(NAME["AN"], ANB, BODEN, "hu", NFARBE["AN"], d=0.1),
    blase("sprech", 780, 260, "a1", 760, 220, inhalt=["Davon hat mir Herr Hecker", "kein Wort gesagt! Ich will",
                                                      "mein Geld zurück."], textsize=34,
          figur=("AN_redet_r", ANB, BODEN, FH)),
])

# ===========================================================================================================================
# C Eine Woche später: die Anfechtung – die Frage (brief … frage2)
# ===========================================================================================================================
ANC, HKC = 380, 1560
MX = HKC - 230                              # Zielort des Briefs
folie([("brief", "Fall · Eine Woche später: Anfechtung"), ("frage", "Die Frage · Anfechtung trotz Mängelrechten?"),
       ("frage2", "Die Frage · Hilft der Gewährleistungsausschluss?")], [
    boden("brief"),
    hart(pl("1 Woche später", 70, 30, "brief", fill=GELB, size=30, bis="frage")),
    *schild("Autohandel Hecker", 1320, 290, "brief", size=38),
    *fig("AN", ANC, BODEN, FH, [("brief", "ernst_r"), ("frage", "denkt_r")], erst="pop"),
    ns(NAME["AN"], ANC, BODEN, "brief", NFARBE["AN"], d=0.1),
    *fig("HK", HKC, BODEN, FH, [("brief", "ruhig"), (beim("brief", "schriftlich"), "sorge"), ("frage2", "denkt")], erst="pop"),
    ns(NAME["HK"], HKC, BODEN, "brief", NFARBE["HK"], d=0.1),
    szene(bewegt(ficon("tabler", "mail", MX, 700, 120, beim("brief", "ficht"), fuell=WEISS),
                 beim("brief", "ficht"), beim("brief", "schriftlich", ende=True), (ANC + 190) - MX, 0),
          "262brief*", 0.8, 0.0),
    pl("Anfechtung", MX, 520, beim("brief", "schriftlich"), fill=WEISS, size=32, anker="m"),
    pl("Darf sie anfechten, obwohl sie auch Mängelrechte hat?", 300, 140, "frage", fill=PINK, size=34),
    pl("Hilft Herrn Hecker der Ausschluss der Gewährleistung?", 300, 225, "frage2", fill=PINK, size=34),
])

# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
sachverhalt_262("sv", [
    "Angelika, selbständige Hebamme, kauft für ihre Hausbesuche beim Gebrauchtwagenhändler Herrn Hecker einen Kombi "
    "für 8.000 €. Im Vertrag ist jede Gewährleistung ausgeschlossen. Herr Hecker hatte den Wagen als Unfallwagen "
    "angekauft und den schweren Frontschaden in seiner eigenen Werkstatt reparieren lassen. Er sagt dazu nichts. "
    "Angelika fragt nicht nach und hält den Wagen für unfallfrei; hätte sie vom Unfall gewusst, hätte sie ihn nicht "
    "gekauft. Das ist Herrn Hecker klar.",
    "Drei Monate später entdeckt der Prüfer bei der Hauptuntersuchung den reparierten Unfallschaden. Eine Woche danach "
    "erklärt Angelika gegenüber Herrn Hecker schriftlich die Anfechtung und verlangt die 8.000 € zurück.",
], "Kann Angelika die 8.000 € zurückverlangen?", size=36)

# ===========================================================================================================================
# E Zwei Wege
# ===========================================================================================================================
PA = "A. Anfechtung"
folie([("ansp", "Angelika gegen Herrn Hecker · 8.000 € zurück"), ("weg1", "Zwei Wege › 1. Anfechtung"),
       ("weg2", "Zwei Wege › 2. Rücktritt wegen eines Mangels")], [
    *tafel("ansp", "Zwei Wege zum Geld"),
    z("Angelika will ihr Geld zurück: 8.000 €", 110, 185, "ansp", "Bold", 36),
    blk(110, 270, 1040, 150, BLAUHELL, "weg1", [("Weg 1: Anfechtung", "ExtraBold", 38, INK),
                                               ("Rückgabe nach Bereicherungsrecht", "Bold", 30, INK)]),
    zit("§§ 123, 142 Abs. 1, 812 BGB", 130, 432, "weg1"),
    blk(110, 500, 1040, 150, HELLGRUEN, "weg2", [("Weg 2: Rücktritt", "ExtraBold", 38, INK),
                                                ("wegen eines Mangels", "Bold", 30, INK)]),
    zit("§§ 437 Nr. 2, 346 BGB", 130, 662, "weg2"),
    *requisit([("ansp", ("tabler", "receipt-refund", 110, WEISS), "8.000 € zurück?", GELB)], px=1560, pu=330, py=90),
    *paar("AN", [("ansp", "ruhig"), ("weg1", "denkt")], "HK", [("ansp", "sorge"), ("weg2", "ernst")]),
])

# ===========================================================================================================================
# F § 123 Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
w123, w123_y = wortlaut(80, 180, 1100, "„(1) Wer zur Abgabe einer Willenserklärung durch arglistige Täuschung oder widerrechtlich "
                                       "durch Drohung bestimmt worden ist, kann die Erklärung anfechten.“", "§ 123 Abs. 1 BGB",
                        "p123", size=34, marken=[("arglistige", beim("p123", "arglistige")), ("Täuschung", beim("p123", "Täuschung")),
                                                 ("anfechten", beim("p123", "anfechten"))])
folie([("p123", f"{PA} · § 123 Abs. 1 BGB"), ("pruef", f"{PA} › Prüfung: Täuschung, Irrtum, Kausalität, Arglist")], [
    *tafel("p123", "Arglistige Täuschung"),
    *w123,
    z("1. Täuschung", 130, w123_y + 40, beim("pruef", "Täuschung"), "ExtraBold", 36),
    z("2. Irrtum und Kausalität", 130, w123_y + 100, beim("pruef", "Irrtum"), "ExtraBold", 36),
    z("3. Arglist", 130, w123_y + 160, beim("pruef", "Arglist"), "ExtraBold", 36),
    *requisit([("p123", ("tabler", "file-text", 110, WEISS), "Anfechtung", WEISS)]),
    *stehend("AN", FX, [("p123", "denkt"), ("pruef", "ernst")]),
])
assert w123_y + 160 + 50 <= 895, w123_y

# ===========================================================================================================================
# G 1. Täuschung: Schweigen nur bei Aufklärungspflicht
# ===========================================================================================================================
PT = f"{PA} › 1. Täuschung"
folie([("luege", f"{PT}: Schweigen statt Lüge"), ("pflicht", f"{PT} › Schweigen nur bei Aufklärungspflicht"),
       ("erwart", f"{PT} › Aufklärungspflicht: redlicherweise erwartet")], [
    *tafel("luege", "1. Täuschung durch Schweigen?"),
    z("Herr Hecker hat nicht gelogen,", 110, 185, "luege", "Bold", 36),
    z("sondern geschwiegen", 110, 240, beim("luege", "geschwiegen"), "Bold", 36),
    z("Schweigen täuscht nur bei Aufklärungspflicht", 110, 330, "pflicht", "ExtraBold", 36),
    feld(110, 410, 1040, 300, "erwart", fill=HELL, rand=5, rund=18, anim="pop", name="pflichtfeld"),
    z("Aufklären muss man, auch ungefragt, über", 145, 445, "erwart", "Bold", 32),
    z("Tatsachen, deren Mitteilung der andere", 145, 497, beim("erwart", "Tatsachen"), "Bold", 32),
    z("redlicherweise erwarten darf, weil sie für", 145, 549, beim("erwart", "redlicherweise"), "Bold", 32),
    z("seine Entscheidung offensichtlich", 145, 601, beim("erwart", "seine"), "Bold", 32),
    z("ausschlaggebend sind", 145, 653, beim("erwart", "ausschlaggebend"), "Bold", 32),
    zit("BGH, Urt. v. 11.8.2010 – XII ZR 123/09, Rn. 19 f.", 110, 740, beim("erwart", "ausschlaggebend")),
    *requisit([("luege", ("tabler", "message-off", 110, WEISS), "schweigt", HELLROT),
               ("erwart", ("tabler", "help", 110, WEISS), "redlich erwartet?", GELB)], px=1560, pu=330, py=90),
    *paar("AN", [("luege", "denkt"), ("erwart", "ernst")], "HK", [("luege", "sorge"), ("pflicht", "ernst")]),
])

# ===========================================================================================================================
# H Aufklärungspflicht beim Gebrauchtwagen
# ===========================================================================================================================
folie([("gw", f"{PT} › Unfallschaden: aufklärungspflichtig"), ("bagatell", f"{PT} › Ausnahme: Bagatellschaden"),
       ("kennt", f"{PT} › Herr Hecker kannte den Schaden"), ("unterl", f"{PT} › Täuschung durch Unterlassen (+)")], [
    *tafel("gw", "Aufklärungspflicht beim Gebrauchtwagen", size=42),
    *okw("bekannter Unfallschaden: aufklärungspflichtig", 185, "gw", beim("gw", "aufklärungspflichtig"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 19.6.2013 – VIII ZR 183/12, Rn. 17–19", 160, 238, beim("gw", "Bundesgerichtshof")),
    *neinz("ausgenommen: Bagatellschaden, etwa kleiner Lackschaden", 310, "bagatell", "Bold", 32, x=160,
           kreuz=beim("bagatell", "Bagatellschäden")),
    zit("BGH, Urt. v. 19.12.2012 – VIII ZR 117/12, Rn. 9, 14", 160, 362, beim("bagatell", "Lackschaden")),
    *okz("Herr Hecker kannte den Frontschaden", 435, "kennt", "Bold", 34, x=160),
    z("aus seiner eigenen Werkstatt", 160, 485, beim("kennt", "eigenen"), "Bold", 34),
    blk(110, 580, 1040, 110, GELB, "unterl", [("Schweigen = Täuschung durch Unterlassen", "ExtraBold", 36, INK)]),
    *plusminus("Täuschung", 110, 720, beim("unterl", "Täuschung"), True, size=36, stil="ExtraBold"),
    *requisit([("gw", ("tabler", "car", 170, GELB), "Unfallschaden bekannt?", WEISS),
               ("bagatell", ("tabler", "brush", 110, WEISS), "kleiner Lackschaden", HELLGRAU),
               ("kennt", ("ph", "garage", 150, HELLGRAU), "eigene Werkstatt", BLAUHELL)], px=1560, pu=330, py=90),
    *stehend("HK", FX, [("gw", "ruhig"), ("kennt", "ertappt"), ("unterl", "sorge")]),
])

# ===========================================================================================================================
# I 2. Irrtum und Kausalität
# ===========================================================================================================================
folie([("irrtum", f"{PA} › 2. Irrtum: Kombi „unfallfrei“"), ("kaus", f"{PA} › 2. Kausalität: sonst nicht gekauft")], [
    *tafel("irrtum", "2. Irrtum und Kausalität"),
    *okw("Irrtum: Angelika hält den Kombi für unfallfrei", 200, "irrtum", beim("irrtum", "unfallfrei"), "Bold", 34, x=160),
    *okw("Kausalität: Mit dem Wissen um den Unfall", 320, "kaus", beim("kaus", "ursächlich"), "Bold", 34, x=160),
    z("hätte sie den Wagen nicht gekauft", 160, 372, beim("kaus", "hätte"), "Bold", 34),
    zit("vgl. BGH, Urt. v. 15.4.2015 – VIII ZR 80/14, Rn. 15", 160, 430, beim("kaus", "hätte")),
    *requisit([("irrtum", ("tabler", "car", 170, GELB), "unfallfrei?", WEISS),
               ("kaus", ("tabler", "contract", 120, WEISS), "sonst kein Kauf", HELLROT)]),
    *stehend("AN", FX, [("irrtum", "froh"), ("kaus", "sorge")]),
])

# ===========================================================================================================================
# J 3. Arglist
# ===========================================================================================================================
folie([("arg", f"{PA} › 3. Arglist"), ("arg2", f"{PA} › 3. Arglist: Kenntnis und Billigung"),
       ("argok", f"{PA} › 3. Arglist (+)")], [
    *tafel("arg", "3. Arglist"),
    z("Arglistig verschweigt einen Mangel, wer ihn", 110, 185, beim("arg", "Arglistig"), "Bold", 34),
    z("mindestens für möglich hält", 110, 237, beim("arg", "mindestens"), "ExtraBold", 34),
    z("und damit rechnet und billigend in Kauf nimmt,", 110, 289, "arg2", "Bold", 34),
    z("dass der andere ihn nicht kennt", 110, 341, beim("arg2", "dass"), "ExtraBold", 34),
    z("und bei Kenntnis nicht oder nicht so gekauft hätte", 110, 393, beim("arg2", "Kenntnis"), "ExtraBold", 34),
    zit("BGH, Urt. v. 15.4.2015 – VIII ZR 80/14, Rn. 16", 110, 450, beim("arg2", "Kenntnis")),
    *okz("Herr Hecker kannte den Schaden", 540, beim("argok", "kannte"), "Bold", 34, x=160),
    *okz("und wusste: sonst kein Kauf", 600, beim("argok", "wusste"), "Bold", 34, x=160),
    *plusminus("Arglist", 110, 690, beim("argok", "Arglist"), True, size=40, stil="ExtraBold"),
    *requisit([("arg", ("tabler", "eye", 110, WEISS), "Wissen", WEISS),
               ("argok", ("ph", "garage", 150, HELLGRAU), "Schaden bekannt", HELLROT)]),
    *stehend("HK", FX, [("arg", "ruhig"), ("arg2", "denkt"), ("argok", "ertappt")]),
])

# ===========================================================================================================================
# K Frist § 124 BGB (Wortlautkarte), Erklärung § 143 BGB
# ===========================================================================================================================
w124, w124_y = wortlaut(80, 170, 1100, "„(1) Die Anfechtung einer nach § 123 anfechtbaren Willenserklärung kann nur binnen "
                                       "Jahresfrist erfolgen. (2) Die Frist beginnt im Falle der arglistigen Täuschung mit "
                                       "dem Zeitpunkt, in welchem der Anfechtungsberechtigte die Täuschung entdeckt, …“",
                        "§ 124 Abs. 1, 2 BGB", "p124", size=32,
                        marken=[("binnen", beim("p124a", "binnen")), ("Jahresfrist", beim("p124a", "Jahresfrist")),
                                ("entdeckt", beim("p124b", "entdeckt"))])
folie([("p124", f"{PA} › Frist, § 124 BGB"), ("p124a", f"{PA} › Frist: ein Jahr"),
       ("p124b", f"{PA} › Frist: ab Entdeckung der Täuschung"), ("frist", f"{PA} › Erklärung, § 143 BGB: rechtzeitig")], [
    *tafel("p124", "Frist und Erklärung"),
    *w124,
    z("Hauptuntersuchung: Täuschung entdeckt", 110, w124_y + 40, beim("frist", "Entdeckung"), "Bold", 34),
    z("1 Woche später: Anfechtung gegenüber Herrn Hecker", 110, w124_y + 95, beim("frist", "gegenüber"), "Bold", 34),
    zit("§ 143 Abs. 1, 2 BGB", 110, w124_y + 147, beim("frist", "Paragraf")),
    *okz("rechtzeitig", w124_y + 200, beim("frist", "rechtzeitig"), "ExtraBold", 36, x=160),
    *requisit([("p124a", ("tabler", "calendar-event", 120, WEISS), "1 Jahr", GELB),
               ("frist", ("tabler", "mail", 120, WEISS), "nach 1 Woche", HELLGRUEN)]),
    *stehend("AN", FX, [("p124", "ruhig"), ("frist", "froh")]),
])
assert w124_y + 200 + 50 <= 895, w124_y

# ===========================================================================================================================
# L Rechtsfolge § 142 Abs. 1 BGB (Wortlautkarte), Rückgabe § 812 BGB, Verweis Folge 023
# ===========================================================================================================================
w142, w142_y = wortlaut(80, 170, 1100, "„(1) Wird ein anfechtbares Rechtsgeschäft angefochten, so ist es als von Anfang an "
                                       "nichtig anzusehen.“", "§ 142 Abs. 1 BGB", "p142", size=34,
                        marken=[("Anfang", beim("p142", "Anfang")), ("nichtig", beim("p142", "nichtig"))])
folie([("p142", f"{PA} › Rechtsfolge, § 142 Abs. 1 BGB"), ("p812", f"{PA} › Rückgabe, § 812 BGB"),
       ("v023", f"{PA} › Grundschema: Folge „Anfechtung in fünf Schritten“")], [
    *tafel("p142", "Die Folge der Anfechtung"),
    *w142,
    z("Rückgabe nach § 812 Abs. 1 S. 1 Alt. 1 BGB:", 110, w142_y + 40, "p812", "Bold", 34),
    z("8.000 € an Angelika", 160, w142_y + 100, beim("p812", "Angelika"), "Bold", 34),
    z("Kombi an Herrn Hecker", 160, w142_y + 152, beim("p812", "Hecker"), "Bold", 34),
    blk(110, w142_y + 230, 1040, 110, LILAHELL, "v023", [("Grundschema: Folge", "ExtraBold", 31, INK),
                                                        ("„Anfechtung in fünf Schritten“", "ExtraBold", 31, INK)]),
    *requisit([("p142", ("tabler", "file-x", 110, WEISS), "Vertrag nichtig", HELLROT),
               ("p812", ("tabler", "arrows-exchange", 120, WEISS), "8.000 € gegen Kombi", GELB)], px=1560, pu=330, py=90),
    *paar("AN", [("p142", "ruhig"), ("p812", "froh")], "HK", [("p142", "sorge"), ("p812", "ernst")]),
])
assert w142_y + 230 + 110 <= 895, w142_y

# ===========================================================================================================================
# M Verhältnis zu den Mängelrechten: keine Sperre bei Arglist; anders § 119 Abs. 2 (h. M.)
# ===========================================================================================================================
PB = "B. Anfechtung und Mängelrechte"
folie([("konk", f"{PB} · Anfechtung trotz Mangel?"), ("mangel", f"{PB} › Unfallwagen: Sachmangel"),
       ("sperre", f"{PB} › Arglist: keine Sperre durch §§ 437 ff. BGB"),
       ("p119", f"{PB} › anders: § 119 Abs. 2 BGB (h. M.)")], [
    *tafel("konk", "Anfechtung trotz Mängelrechten?"),
    z("Der Kombi ist auch mangelhaft:", 110, 180, "mangel", "Bold", 34),
    z("Unfallwagen: nicht die übliche Beschaffenheit", 110, 232, beim("mangel", "Unfallwagen"), "Bold", 34),
    zit("§ 434 Abs. 3 S. 1 Nr. 2 BGB", 110, 282, beim("mangel", "übliche")),
    z("Die Reparatur ändert daran nichts", 110, 330, "rep", "Bold", 34),
    zit("BGH, Urt. v. 19.12.2012 – VIII ZR 117/12, Rn. 14", 110, 380, "rep"),
    *okw("Arglist: Mängelrechte sperren die Anfechtung nicht", 450, "sperre", beim("sperre", "nicht"), "ExtraBold", 33, x=160),
    z("BGH prüft beide Wege nebeneinander", 160, 505, "bgh", "Bold", 34),
    zit("BGH, Urt. v. 15.4.2015 – VIII ZR 80/14, Rn. 13, 17", 160, 555, "bgh"),
    blk(110, 620, 1040, 150, HELLGRAU, "p119", [("anders: Eigenschaftsirrtum, § 119 Abs. 2", "ExtraBold", 32, INK),
                                              ("ab Gefahrübergang verdrängt", "Bold", 32, INK),
                                              ("(herrschende Meinung)", "Bold", 30, INK)]),
    *requisit([("mangel", ("tabler", "car", 170, GELB), "Unfallwagen", HELLROT),
               ("rep", ("ph", "wrench", 110, WEISS), "repariert", WEISS),
               ("sperre", ("ph", "scales", 130, WEISS), "beide Wege", HELLGRUEN),
               ("p119", ("tabler", "help", 110, WEISS), "§ 119 Abs. 2?", HELLGRAU)]),
    *stehend("AN", FX, [("konk", "denkt"), ("sperre", "froh"), ("p119", "ruhig")]),
])

# ===========================================================================================================================
# N1 Gewährleistungsausschluss: Unternehmerin; § 476 beim Verbraucher (ein Satz)
# ===========================================================================================================================
PC = "C. Gewährleistungsausschluss"
folie([("aus", f"{PC} · Hilft der Ausschluss?"), ("unter", f"{PC} › Angelika: Unternehmerin, § 14 BGB"),
       ("v476", f"{PC} › Verbraucher: § 476 Abs. 1 BGB")], [
    *tafel("aus", "Hilft der Ausschluss?"),
    z("Angelika kauft beruflich, als Unternehmerin", 110, 190, "unter", "Bold", 34),
    zit("§ 14 Abs. 1 BGB", 110, 242, beim("unter", "Unternehmerin")),
    *okw("Ausschluss grundsätzlich möglich", 310, beim("unter", "Da"), beim("unter", "möglich"), "Bold", 34, x=160),
    *neinz("gegenüber einem Verbraucher: nicht möglich", 420, "v476", "Bold", 34, x=160, kreuz=beim("v476", "nicht")),
    zit("§ 476 Abs. 1 S. 1 BGB", 160, 472, beim("v476", "Paragraf")),
    *requisit([("aus", ("tabler", "shield-off", 110, WEISS), "Ausschluss?", WEISS),
               ("unter", ("tabler", "briefcase", 120, WEISS), "beruflich", BLAUHELL),
               ("v476", ("tabler", "user", 110, WEISS), "Verbraucher?", HELLGRAU)], px=1560, pu=330, py=90),
    *paar("AN", [("aus", "denkt"), ("unter", "ruhig")], "HK", [("aus", "froh"), ("v476", "denkt")]),
])

# ===========================================================================================================================
# N2 § 444 BGB (Wortlautkarte); Anfechtung vom Ausschluss nicht erfasst
# ===========================================================================================================================
w444, w444_y = wortlaut(80, 170, 1100, "„Auf eine Vereinbarung, durch welche die Rechte des Käufers wegen eines Mangels "
                                       "ausgeschlossen oder beschränkt werden, kann sich der Verkäufer nicht berufen, soweit "
                                       "er den Mangel arglistig verschwiegen oder eine Garantie für die Beschaffenheit der "
                                       "Sache übernommen hat.“", "§ 444 BGB", "p444", size=32,
                        marken=[("ausgeschlossen", beim("p444", "ausgeschlossen")), ("berufen", beim("p444", "berufen")),
                                ("arglistig", beim("p444", "arglistig")), ("verschwiegen", beim("p444", "verschwiegen"))])
folie([("p444", f"{PC} › § 444 BGB"), ("p444ok", f"{PC} › arglistig verschwiegen: kein Berufen"),
       ("anfaus", f"{PC} › Anfechtung: vom Ausschluss nicht erfasst")], [
    *tafel("p444", "Kein Schutz bei Arglist"),
    *w444,
    *okz("Herr Hecker hat den Mangel arglistig verschwiegen", w444_y + 40, "p444ok", "Bold", 34, x=160),
    blk(110, w444_y + 120, 1040, 110, HELLGRUEN, "anfaus", [("Anfechtung: vom Ausschluss nicht erfasst", "ExtraBold", 32, INK),
                                                           ("er betrifft nur die Mängelrechte", "Bold", 32, INK)]),
    *requisit([("p444", ("tabler", "shield-off", 110, WEISS), "Ausschluss?", WEISS),
               ("p444ok", ("tabler", "x", 100, WEISS), "kein Berufen", HELLROT)], px=1560, pu=330, py=90),
    *paar("AN", [("p444", "ruhig"), ("p444ok", "froh")], "HK", [("p444", "denkt"), ("p444ok", "sorge")]),
])
assert w444_y + 120 + 110 <= 895, w444_y

# ===========================================================================================================================
# O Was ist günstiger? Anfechtung oder Rücktritt (Verweis Folgen 063, 236)
# ===========================================================================================================================
PD = "D. Anfechtung oder Rücktritt?"
folie([("vgl", f"{PD} · Was ist günstiger?"), ("vgl1", f"{PD} › Anfechtung: Vertrag rückwirkend weg"),
       ("vgl2", f"{PD} › Rücktritt: Vertrag bleibt Grundlage"), ("frist2", f"{PD} › Rücktritt ohne Frist"),
       ("vgl3", f"{PD} › Praxis: Anfechtung, hilfsweise Rücktritt"),
       ("v063", f"{PD} › Folgen „Käuferrechte“ und „Schadensersatz im Kaufrecht“")], [
    *tafel("vgl", "Was ist günstiger?"),
    feld(110, 170, 1040, 130, "vgl1", fill=HELLROT, rand=5, rund=18, anim="pop", name="anf"),
    z("Anfechtung: Vertrag rückwirkend weg", 140, 182, "vgl1", "ExtraBold", 34),
    z("und mit ihm die vertraglichen Mängelrechte", 140, 236, beim("vgl1", "und"), "Bold", 32),
    feld(110, 320, 1040, 180, "vgl2", fill=HELLGRUEN, rand=5, rund=18, anim="pop", name="ruecktritt"),
    z("Rücktritt: Vertrag bleibt Grundlage", 140, 332, "vgl2", "ExtraBold", 34),
    z("Rückabwicklung, § 346 BGB", 140, 386, beim("vgl2", "Rückabgewickelt"), "Bold", 32),
    z("Schadensersatz daneben, § 325 BGB", 140, 436, beim("vgl2", "Schadensersatz"), "Bold", 32),
    *okz("Frist zur Nacherfüllung: in der Regel entbehrlich", 525, "frist2", "Bold", 32, x=160),
    zit("Unfallwagen bleibt Unfallwagen; §§ 437 Nr. 2, 326 Abs. 5 BGB", 160, 575, beim("frist2", "Aus")),
    pl("Praxis: Anfechtung, hilfsweise Rücktritt", 110, 625, beim("vgl3", "beides"), fill=PINK, size=32),
    blk(110, 720, 1040, 110, LILAHELL, "v063", [("Folgen „Käuferrechte § 437 BGB“ und", "ExtraBold", 30, INK),
                                               ("„Schadensersatz im Kaufrecht“", "ExtraBold", 30, INK)]),
    *requisit([("vgl", ("ph", "scales", 140, WEISS), "Was ist besser?", GELB),
               ("vgl1", ("tabler", "file-x", 110, WEISS), "Vertrag weg", HELLROT),
               ("vgl2", ("tabler", "receipt-refund", 110, WEISS), "Rücktritt", HELLGRUEN),
               ("vgl3", ("tabler", "mail", 120, WEISS), "beides erklären", PINK)]),
    *stehend("AN", FX, [("vgl", "denkt"), ("vgl2", "ruhig"), ("vgl3", "froh")]),
])

# ===========================================================================================================================
# P Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Aufklärungspflicht begründen"), ("tipp2", "Klausurtipp · Erklärung des Käufers auslegen"),
       ("tipp3", "Klausurtipp · Anfechtung zugleich Rücktritt?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Täuschung durch Unterlassen:", 200, 200, "tipp", "Bold", 34),
    z("Knackpunkt ist die Aufklärungspflicht", 200, 252, beim("tipp", "Knackpunkt"), "ExtraBold", 34),
    z("am Fall begründen", 200, 304, beim("tipp", "Begründe"), "Bold", 34),
    linienzug([(130, 380), (1130, 380)], "tipp2", breite=3),
    z("Erklärung des Käufers genau lesen", 200, 410, "tipp2", "ExtraBold", 34),
    z("Eine Anfechtung kann zugleich als Rücktritt", 200, 480, "tipp3", "Bold", 34),
    z("auszulegen sein, wenn der Käufer den Vertrag", 200, 532, beim("tipp3", "auszulegen"), "Bold", 34),
    z("auf jeden Fall rückabgewickelt haben will", 200, 584, beim("tipp3", "auf"), "Bold", 34),
    zit("BGH, Urt. v. 11.2.2026 – VIII ZR 37/24, Leitsatz 1, Rn. 37", 200, 650, beim("tipp3", "Bundesgerichtshof")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# Q Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Anfechtung und Rückgabe", True),
          ("s1a", 1, "1. arglistige Täuschung, § 123 Abs. 1 BGB:", False),
          (beim("s1a", "Täuschung", nr=2), 2, "Täuschung (bei Schweigen: Aufklärungspflicht), Irrtum, Kausalität, Arglist", False),
          ("s1b", 1, "2. Anfechtungserklärung, Jahresfrist ab Entdeckung, §§ 143, 124 BGB", False),
          ("s1c", 1, "3. nichtig von Anfang an, § 142 Abs. 1 BGB; Rückgabe, § 812 BGB", False),
          ("s2", 0, "II. alternativ: Rücktritt, §§ 437 Nr. 2, 346 BGB", True),
          (beim("s2", "Unfallwagen"), 2, "Unfallwagen mangelhaft; Ausschluss scheitert an § 444 BGB", False),
          ("s3", 0, "III. Ergebnis: Angelika bekommt ihr Geld zurück", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Angelika gegen Herrn Hecker"), 110, 90, "sch", 44),
           z("auf Rückzahlung der 8.000 €", 110, 158, beim("sch", "achttausend"), "Bold", 36, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1820))
    y += {0: 92, 1: 70, 2: 80}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Anfechtung und Rückgabe"),
       ("s2", "Prüfungsschema › II. alternativ: Rücktritt"), ("s3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# R Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer einen bekannten ", 0), ("Unfallschaden", "a")], [("verschweigt, täuscht ", 0), ("arglistig.", "b")]],
                750, 270, 44, "merke", {"a": beim("merke", "Unfallschaden"), "b": beim("merke", "arglistig")}),
    *markertext([[("Der Käufer kann ", 0), ("anfechten", "c"), (" oder", 0)],
                 [("seine ", 0), ("Mängelrechte", "d"), (" nutzen, und auf den", 0)],
                 [("Gewährleistungsausschluss kann sich", 0)], [("der Händler ", 0), ("nicht berufen.", "e")]],
                750, 450, 44, "merk2", {"c": beim("merk2", "anfechten"), "d": beim("merk2", "Mängelrechte"),
                                        "e": beim("merk2", "berufen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
