"""Folge 281 · Mietminderung § 536 BGB: Schimmel, Baulärm, kalte Heizung · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Friedemann mietet von Frau Teuber eine Altbauwohnung für 850 € warm (700 € kalt + 150 € Nebenkosten).
Schimmel hinter dem Schrank an der Außenwand (nur als dezentes Symbol: wenige graugrüne Flecken), Anzeige erst im Januar;
Neubau auf dem Nachbargrundstück (Bagger und Presslufthammer im Fenster); im Januar eine Woche kalte Heizung, sofort
gemeldet. Frau Teuber sieht sich alles an (sachlich, fair). Danach: § 536 Abs. 1 (Wortlautkarte S. 1–3), kraft Gesetzes,
Mangel, Unerheblichkeit, Bruttomiete; drei Beispiele (Schimmel/Beweislast, Baulärm nach Bolzplatz/Baustelle, Heizung);
§ 536c und § 536b (Wortlautkarten); Praxisrisiko (§ 543, Vorbehalt, § 320); Ergebnis, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/
stehend/paar/okw als eigene Kopie aus Folge 278 (gemeinsame Dateien unverändert); neu: zimmer(), schimmel(), heizkoerper().
Handlungsgeräusch: Bagger im Fenster (A, Wort „baut“), szene_281bagger_1 (Kopie von Freesound CC0 118974);
../geraeusche_herkunft.json. Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de
(BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_281/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_281/" in n:
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
NAME = {"FR": "Friedemann", "TB": "Frau Teuber"}
BLAU_P, LILA_P, ROT_P = (141, 179, 242, 255), (184, 169, 245, 255), (240, 122, 106, 255)
GRUEN_P0 = (143, 214, 148, 255)
NFARBE = {"FR": BLAU_P, "TB": (249, 166, 108, 255)}
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
# Schauplatz: Schlafzimmer der Altbauwohnung (A, H) – programmatisch: Schrank, Fenster mit Blick auf die Baustelle,
# Heizkörper unter dem Fenster; Schimmel nur als dezentes Symbol (wenige graugrüne Flecken neben dem Schrank)
# ===========================================================================================================================
FRX, TBX = 1180, 1620                        # Friedemann und Frau Teuber im Zimmer
FE_X, FE_Y, FE_W, FE_H = 560, 230, 440, 300  # Fenster
SCHIMMEL = (128, 146, 118, 255)


def schrank(cue):
    els = [hart(feld(110, 320, 270, BODEN - 324, cue, fill=HOLZ, rand=5, rund=10, name="schrank")),
           hart(feld(244, 336, 4, BODEN - 360, cue, fill=INK, rand=1, rund=2, name="schranktuer")),
           hart(feld(222, 560, 12, 40, cue, fill=DUNKELHOLZ, rand=2, rund=5, name="griff1")),
           hart(feld(258, 560, 12, 40, cue, fill=DUNKELHOLZ, rand=2, rund=5, name="griff2"))]
    return els


def schimmel(cue, bis=None):
    """Dezentes Symbol: sieben kleine graugrüne Flecken an der Außenwand, halb hinter dem Schrank."""
    im = Image.new("RGBA", (180, 170))
    dr = ImageDraw.Draw(im)
    for x, y, r in [(30, 40, 16), (58, 28, 10), (52, 70, 13), (86, 52, 9), (24, 104, 11), (70, 112, 8), (104, 86, 6)]:
        dr.ellipse((x - r, y - r, x + r, y + r), fill=SCHIMMEL)
    return bis_(El(im, 352, 360, cue, "fade", 0.0, None, name="schimmel"), bis)


def heizkoerper(cue):
    els = [hart(feld(640, 610, 280, 150, cue, fill=WEISS, rand=5, rund=12, name="heizkoerper"))]
    for i in range(6):
        els.append(hart(feld(668 + i * 40, 630, 14, 110, cue, fill=HELLGRAU, rand=2, rund=6, name=f"rippe{i}")))
    els.append(hart(feld(906, 760, 10, 100, cue, fill=HELLGRAU, rand=2, rund=4, name="rohr")))
    return els


def zimmer(cue, draussen=(), schimmel_cue=None, schimmel_bis=None):
    """Zimmer: Boden, Schimmel (unter dem Schrank gezeichnet), Schrank, Fenster mit Blick nach draußen, Heizkörper."""
    fe = fenster(FE_X, FE_Y, FE_W, FE_H, cue)
    els = [boden(cue)]
    if schimmel_cue:
        els.append(schimmel(schimmel_cue, schimmel_bis))
    els += schrank(cue) + [fe[0]] + list(draussen) + fe[1:] + heizkoerper(cue)
    return els


def kran(cue, bis=None):
    return ficon("tabler", "crane", FE_X + 330, FE_Y + FE_H - 14, 150, cue, fuell=GELB, anim="pop", bis=bis)


def bagger(cue, bis=None):
    return ficon("tabler", "backhoe", FE_X + 90, FE_Y + FE_H - 14, 130, cue, fuell=GELB, anim="pop", bis=bis)


# ===========================================================================================================================
# A Fall: Schimmel, Baulärm, kalte Heizung; Frau Teuber sieht sich alles an – die Frage
# ===========================================================================================================================
TOP1, TOP2 = 1450, 120                         # Pillen oben rechts (über dem Kopf von Friedemann frei)
folie([(NULL, "Fall · Die Altbauwohnung"), ("fried", "Fall · Friedemann, 850 € warm"),
       ("schim", "Fall · Schimmel an der Außenwand"), ("bau", "Fall · Baustelle nebenan"),
       ("kalt", "Fall · Heizung eine Woche kalt"), ("teub", "Fall · Frau Teuber sieht sich alles an"),
       ("t1", "Fall · Frau Teuber: „vom Lüften“"), ("f1", "Fall · Friedemann: „nur noch die halbe Miete“"),
       ("frage", "Die Frage · Ist seine Miete gemindert?"), ("frage2", "Die Frage · Muss Friedemann etwas erklären?"),
       ("frage3", "Die Frage · Was riskiert er?")], [
    *zimmer(NULL, draussen=[kran(beim("bau", "baut")), szene(bagger(beim("bau", "baut")), "281bagger*", 0.7, 0.0),
                            bis_(ficon("tabler", "hammer-drill", FE_X + 172, FE_Y + FE_H - 14, 60, beim("bau", "Presslufthammer"),
                                       fuell=WEISS, anim="pop"), "teub")],
            schimmel_cue=beim("schim", "Schimmel")),
    pl("Darfst du weniger Miete überweisen?", TOP1, TOP2, beim("fall", "Darfst"), fill=PINK, size=32, anker="m", bis="fried"),
    pl("Altbauwohnung: 850 € warm", TOP1, TOP2, beim("fried", "Altbauwohnung"), fill=WEISS, size=32, anker="m", bis="schim"),
    pl("November: Schimmel an der Außenwand", TOP1, TOP2, beim("schim", "Schimmel"), fill=WEISS, size=30, anker="m", bis="bau"),
    pl("Bescheid erst im Januar", TOP1, TOP2 + 76, beim("schim", "Januar"), fill=HELLROT, size=30, anker="m", bis="bau"),
    pl("Dezember: Neubau nebenan", TOP1, TOP2, beim("bau", "baut"), fill=GELB, size=30, anker="m", bis="kalt"),
    pl("tagsüber Presslufthammer", TOP1, TOP2 + 76, beim("bau", "Presslufthammer"), fill=GELB, size=30, anker="m", bis="kalt"),
    pl("Januar: Heizung 1 Woche kalt", TOP1, TOP2, beim("kalt", "Heizung"), fill=BLAUHELL, size=30, anker="m", bis="teub"),
    pl("am selben Tag gemeldet", TOP1, TOP2 + 76, beim("kalt", "meldet"), fill=HELLGRUEN, size=30, anker="m", bis="teub"),
    bis_(ficon("tabler", "snowflake", 990, 740, 80, beim("kalt", "Heizung"), fuell=BLAUHELL, anim="pop"), "teub"),
    bis_(ficon("tabler", "phone", 1720, 258, 50, beim("kalt", "meldet"), fuell=WEISS, anim="pop"), "teub"),
    *fig("FR", FRX, BODEN, FH, [("fried", "ruhig"), (beim("schim", "Schimmel"), "sorge"), (beim("bau", "Presslufthammer"), "muede"),
                               (beim("kalt", "Heizung"), "schreck"), (beim("kalt", "meldet"), "ernst")], bis="teub", erst="pop"),
    *fig("FR", FRX, BODEN, FH, [("teub", "ruhig_r"), ("t1", "denkt_r")], bis="f1", erst="cut"),
    *redet("FR_redet_r", FRX, BODEN, FH, "f1", "frage"),
    *fig("FR", FRX, BODEN, FH, [("frage", "ernst_r")], erst="cut"),
    ns(NAME["FR"], FRX, BODEN, "fried", NFARBE["FR"], d=0.1),
    *fig("TB", TBX, BODEN, FH, [("teub", "ruhig")], bis="t1", erst="pop"),
    *redet("TB_redet", TBX, BODEN, FH, "t1", "f1"),
    *fig("TB", TBX, BODEN, FH, [("f1", "staunt"), ("frage", "denkt")], erst="cut"),
    ns(NAME["TB"], TBX, BODEN, "teub", NFARBE["TB"], d=0.1),
    pl("Vermieterin", TBX, BODEN + 80, beim("teub", "Vermieterin"), fill=WEISS, size=26, anker="m"),
    blase("sprech", 660, 200, "t1", 1500, 230, inhalt=["Der Schimmel kommt vom Lüften.", "Und für die Baustelle",
                                                     "nebenan kann ich nichts."],
          textsize=31, figur=("TB_redet", TBX, BODEN, FH), bis="f1"),
    blase("sprech", 640, 170, "f1", 1300, 230, inhalt=["Dann überweise ich ab Februar", "nur noch die halbe Miete."],
          textsize=31, figur=("FR_redet_r", FRX, BODEN, FH), bis="frage"),
    pl("Ist seine Miete gemindert?", 980, 30, "frage", fill=PINK, size=34),
    pl("Muss Friedemann etwas erklären?", 980, 108, "frage2", fill=PINK, size=34),
    pl("Was riskiert er, wenn er zu viel abzieht?", 980, 186, "frage3", fill=PINK, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_281(cue, absaetze, frage, size=43):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_281("sv", [
    "Friedemann mietet von Frau Teuber eine Altbauwohnung für 850 € warm: 700 € Kaltmiete und 150 € Vorauszahlung auf "
    "die Nebenkosten. Im November entdeckt er hinter dem Schrank im Schlafzimmer Schimmel an der Außenwand. Frau Teuber "
    "sagt er erst im Januar Bescheid.",
    "Seit Dezember baut der Nachbar ein neues Haus; tagsüber dröhnt der Presslufthammer. Im Januar bleibt die Heizung eine "
    "Woche lang kalt. Das meldet Friedemann noch am selben Tag.",
    "Frau Teuber meint, der Schimmel komme vom Lüften, und für die Baustelle könne sie nichts. Friedemann will ab Februar "
    "nur noch die halbe Miete überweisen.",
], "Ist die Miete gemindert, und was riskiert Friedemann?")


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
# C1 § 536 Abs. 1 BGB (Wortlautkarte Satz 1–3)
# ===========================================================================================================================
PM = "Minderung"
w536, w536_y = wortlaut(80, 170, 1100, "„Hat die Mietsache zur Zeit der Überlassung an den Mieter einen Mangel, der ihre Tauglichkeit "
                                       "zum vertragsgemäßen Gebrauch aufhebt, oder entsteht während der Mietzeit ein solcher "
                                       "Mangel, so ist der Mieter für die Zeit, in der die Tauglichkeit aufgehoben ist, von der "
                                       "Entrichtung der Miete befreit. Für die Zeit, während der die Tauglichkeit gemindert ist, "
                                       "hat er nur eine angemessen herabgesetzte Miete zu entrichten. Eine unerhebliche "
                                       "Minderung der Tauglichkeit bleibt außer Betracht.“",
                        "§ 536 Abs. 1 BGB", "w536", size=32,
                        marken=[("aufhebt", beim("w536", "aufhebt")), ("befreit", beim("w536", "befreit")),
                                ("gemindert", beim("w536s2", "gemindert")), ("angemessen", beim("w536s2", "angemessen")),
                                ("unerhebliche", beim("w536s3", "unerhebliche"))])
folie([("w536", f"{PM} · § 536 Abs. 1 BGB: Tauglichkeit aufgehoben"), ("w536s2", f"{PM} › Tauglichkeit gemindert"),
       ("w536s3", f"{PM} › unerhebliche Minderung zählt nicht")], [
    *tafel("w536", "Mietminderung, § 536 Abs. 1"),
    *w536,
    *requisit([("w536", ("tabler", "home", 120, WEISS), "von der Miete befreit", WEISS),
               ("w536s2", ("tabler", "coins", 120, GELB), "angemessen herabgesetzt", GELB),
               ("w536s3", ("tabler", "tool", 100, WEISS), "unerheblich", WEISS)]),
    *stehend("FR", FX, [("w536", "ruhig"), ("w536s2", "denkt"), ("w536s3", "ernst")]),
])
assert w536_y <= 895, w536_y

# ===========================================================================================================================
# C2 kraft Gesetzes (Vergleich § 441 Abs. 1), Mangel, Unerheblichkeit, Bruttomiete
# ===========================================================================================================================
folie([("kraft", f"{PM} › kraft Gesetzes, ohne Erklärung"), ("mangel", f"{PM} › Mangel: Ist weicht vom Soll ab"),
       ("unerh", f"{PM} › unerheblich, § 536 Abs. 1 Satz 3 BGB"), ("brutto", f"{PM} › Bemessung: Bruttomiete")], [
    *tafel("kraft", "Minderung kraft Gesetzes"),
    *okw("kraft Gesetzes: Friedemann muss nichts erklären", 172, "kraft", beim("kraft", "Gesetzes"), "Bold", 33),
    zit("anders beim Kauf: Minderung durch Erklärung, § 441 Abs. 1 BGB", 185, 222, beim("kraft", "anders")),
    blk(110, 280, 1040, 120, BLAUHELL, "mangel", [("Mangel: tatsächlicher Zustand weicht zum Nachteil", "ExtraBold", 31, INK),
                                                 ("des Mieters vom vertraglich vorausgesetzten ab", "ExtraBold", 31, INK)]),
    zit("BGH, Urt. v. 5.12.2018 – VIII ZR 271/17, Rn. 21; Urt. v. 29.4.2020 – VIII ZR 31/18, Rn. 24", 110, 412,
        beim("mangel", "Nachteil")),
    *neinz("unerheblich: leicht erkennbar, schnell und mit", 470, "unerh", "Bold", 32, kreuz=beim("unerh", "Unerheblich")),
    z("geringen Kosten behoben – zählt nicht", 185, 514, beim("unerh", "geringen"), "Bold", 32),
    zit("BGH, Urt. v. 6.4.2005 – XII ZR 225/03, Gründe II. 1.", 185, 562, beim("unerh", "geringen")),
    blk(110, 620, 1040, 90, GELB, "brutto", [("Bemessung: Bruttomiete, also samt Nebenkosten", "ExtraBold", 32, INK)]),
    z("bei Friedemann: 700 € + 150 € = 850 €", 140, 770, beim("brutto", "Friedemann"), "Bold", 32),
    zit("BGH, Urt. v. 6.4.2005 – XII ZR 225/03, Leitsatz", 140, 724, beim("brutto", "Bundesgerichtshof")),
    *requisit([("kraft", ("tabler", "writing-sign", 110, WEISS), "keine Erklärung", WEISS),
               ("mangel", ("tabler", "home-exclamation", 120, WEISS), "Ist und Soll", BLAUHELL),
               ("unerh", ("tabler", "tool", 100, WEISS), "unerheblich?", WEISS),
               ("brutto", ("tabler", "coins", 120, GELB), "850 € warm", GELB)]),
    *stehend("TB", FX, [("kraft", "ruhig"), ("mangel", "denkt"), ("brutto", "ernst")]),
])

# ===========================================================================================================================
# D1 Beispiel 1: Schimmel – Ursache, Beweislast nach Verantwortungsbereichen, Baustandard (VIII ZR 271/17)
# ===========================================================================================================================
PB = "Drei Probleme"
folie([("drei", f"{PB} · Schimmel, Baulärm, kalte Heizung"), ("s1", f"{PB} › 1. Schimmel: Baumangel?"),
       ("s1b", f"{PB} › 1. Schimmel: Lüften und Heizen"), ("bew", f"{PB} › 1. Schimmel: Beweislast"),
       ("alt", f"{PB} › 1. Schimmel: Altbau, Lüften im Einzelfall")], [
    *tafel("drei", "1. Schimmel"),
    z("Schimmel – Baulärm – kalte Heizung", 110, 166, "drei", "Regular", 30, farbe=TEXT),
    *okw("Mangel, wenn Baumangel – etwa feuchte Wand", 222, "s1", beim("s1", "Mangel"), "Bold", 33),
    *neinz("zu wenig gelüftet und geheizt: kein Mangel", 282, "s1b", "Bold", 33, kreuz=beim("s1b", "nicht")),
    zit("BGH, Urt. v. 11.7.2012 – VIII ZR 138/11, Rn. 16", 185, 332, beim("s1b", "nicht")),
    hart(feld(110, 384, 1040, 170, beim("bew", "beweisen"), fill=BLAUHELL, rand=5, rund=18, name="beweislast")),
    z("Beweislast nach Verantwortungsbereichen", 140, 398, beim("bew", "beweisen"), "ExtraBold", 31, rechts=1130),
    z("1. Vermieterin: Ursache nicht aus ihrem Bereich", 140, 446, beim("bew", "Verantwortungsbereich"), "Bold", 31, rechts=1130),
    z("2. dann Mieter: Schimmel nicht zu vertreten", 140, 494, "bew2", "Bold", 31, rechts=1130),
    zit("BGH, Urt. v. 1.3.2000 – XII ZR 272/97, Gründe II. 2. a); VIII ZR 31/18, Rn. 74, 79", 110, 566,
        beim("bew", "beweisen")),
    *neinz("Wärmebrücken nach Bauvorschriften der Bauzeit:", 624, "alt", "Bold", 32, kreuz=beim("alt", "kein")),
    z("kein Mangel", 185, 668, beim("alt", "kein"), "Bold", 32),
    z("zumutbares Lüften: Einzelfall", 185, 724, beim("alt", "welches"), "Bold", 32),
    zit("BGH, Urt. v. 5.12.2018 – VIII ZR 271/17, Leitsätze 1 und 2", 185, 772, beim("alt", "welches")),
    *requisit([("s1", ("tabler", "droplet", 80, BLAUHELL), "feuchte Wand", BLAUHELL),
               ("s1b", ("tabler", "temperature", 70, WEISS), "lüften und heizen", WEISS),
               ("bew", ("ph", "scales", 130, WEISS), "Beweislast", BLAUHELL),
               ("alt", ("tabler", "home", 120, WEISS), "Altbau", WEISS)]),
    *paar("FR", [("drei", "ruhig"), ("s1b", "denkt"), ("bew2", "sorge"), ("alt", "ernst")],
          "TB", [("drei", "ruhig"), ("bew", "denkt"), ("alt", "ruhig")]),
])

# ===========================================================================================================================
# D2 Beispiel 2: Baulärm vom Nachbargrundstück (VIII ZR 197/14 Bolzplatz; VIII ZR 31/18 Baustelle)
# ===========================================================================================================================
folie([("s2", f"{PB} › 2. Baulärm: grundsätzlich kein Mangel"), ("bolz", f"{PB} › 2. Baulärm: Bolzplatz und Baustelle"),
       ("s2b", f"{PB} › 2. Baulärm: Darlegung des Mieters"), ("s2c", f"{PB} › 2. Baulärm: Beweis der Vermieterin")], [
    *tafel("s2", "2. Baulärm von nebenan"),
    *neinz("grundsätzlich kein Mangel, wenn auch die Vermieterin", 172, "s2", "Bold", 32, kreuz=beim("s2", "kein")),
    z("ihn ohne Abwehr- oder Entschädigungsmöglichkeit", 185, 216, beim("s2", "ohne"), "Bold", 32),
    z("hinnehmen muss", 185, 260, beim("s2", "hinnehmen"), "Bold", 32),
    zit("vgl. § 906 BGB", 185, 308, beim("s2", "hinnehmen")),
    blk(110, 360, 510, 46 + 3 * 38, HELLGRUEN, beim("bolz", "Bolzplatz"),
        [("Bolzplatz", "ExtraBold", 30, INK), ("BGH, Urt. v. 29.4.2015", "Bold", 28, INK), ("VIII ZR 197/14, Leitsatz 3", "Bold", 28, INK)]),
    blk(640, 360, 510, 46 + 3 * 38, GELB, beim("bolz", "Baustelle"),
        [("Baustelle", "ExtraBold", 30, INK), ("BGH, Urt. v. 29.4.2020", "Bold", 28, INK), ("VIII ZR 31/18, Leitsatz 1", "Bold", 28, INK)]),
    z("Mieter: wesentliche Beeinträchtigung darlegen", 110, 560, "s2b", "Bold", 32),
    z("Vermieterin: keine Ansprüche gegen den Nachbarn?", 110, 616, "s2c", "Bold", 32),
    z("Tatsachen aus ihrem Bereich beweisen", 110, 660, beim("s2c", "Tatsachen"), "Bold", 32),
    zit("BGH, Urt. v. 29.4.2020 – VIII ZR 31/18, Leitsätze 3 und 5", 110, 714, "s2b"),
    *requisit([("s2", ("tabler", "crane", 130, GELB), "Neubau nebenan", WEISS),
               (beim("bolz", "Bolzplatz"), ("ph", "soccer-ball", 110, WEISS), "Bolzplatz", HELLGRUEN),
               (beim("bolz", "Baustelle"), ("tabler", "backhoe", 140, GELB), "Baustelle", GELB),
               ("s2b", ("tabler", "volume", 100, WEISS), "wesentlich?", WEISS),
               ("s2c", ("ph", "scales", 130, WEISS), "Beweis: Vermieterin", WEISS)]),
    *stehend("TB", FX, [("s2", "ruhig"), ("bolz", "denkt"), ("s2c", "ernst")]),
])

# ===========================================================================================================================
# D3 Beispiel 3: kalte Heizung (XII ZR 225/03: Heizung gehört zur Vermieterleistung); Höhe im Einzelfall
# ===========================================================================================================================
folie([("s3", f"{PB} › 3. kalte Heizung: Wärme geschuldet"), ("s3b", f"{PB} › 3. kalte Heizung: Tauglichkeit gemindert"),
       ("s3c", f"{PB} › 3. kalte Heizung: Höhe im Einzelfall")], [
    *tafel("s3", "3. Kalte Heizung"),
    *okw("auch die Wärme schuldet die Vermieterin", 172, "s3", beim("s3", "Wärme"), "Bold", 36),
    zit("BGH, Urt. v. 6.4.2005 – XII ZR 225/03, Gründe II. 2. b) bb): „… Heizung“", 185, 224, beim("s3", "Wärme")),
    *okw("Ausfall im Januar: Tauglichkeit für diese Zeit gemindert", 290, "s3b", beim("s3b", "gemindert"), "Bold", 32),
    zit("§ 536 Abs. 1 Satz 2 BGB", 185, 340, beim("s3b", "gemindert")),
    blk(110, 410, 1040, 46 + 2 * 40, GELB, "s3c", [("Um wie viel? Einzelfall,", "ExtraBold", 32, INK),
                                                  ("etwa Dauer und Außentemperatur", "Bold", 30, INK)]),
    *requisit([("s3", ("ph", "thermometer-cold", 80, WEISS), "Wärme", WEISS),
               ("s3b", ("tabler", "snowflake", 110, BLAUHELL), "Januar: kalt", BLAUHELL),
               ("s3c", ("tabler", "calendar", 110, WEISS), "Dauer?", GELB)]),
    *stehend("FR", FX, [("s3", "muede"), ("s3b", "schreck"), ("s3c", "denkt")]),
])

# ===========================================================================================================================
# E § 536c BGB (Wortlautkarten Abs. 1 Satz 1 und Abs. 2 Satz 2 Nr. 1): Anzeige
# ===========================================================================================================================
PA = "Anzeige"
w1, w1_y = wortlaut(80, 160, 1100, "„Zeigt sich im Laufe der Mietzeit ein Mangel der Mietsache …, so hat der Mieter dies dem "
                                   "Vermieter unverzüglich anzuzeigen.“", "§ 536c Abs. 1 Satz 1 BGB", "w536c", size=31,
                    marken=[("Mangel", beim("w536c", "Mangel")), ("unverzüglich", beim("w536c", "unverzüglich"))])
w2, w2_y = wortlaut(80, w1_y + 16, 1100, "„Soweit der Vermieter infolge der Unterlassung der Anzeige nicht Abhilfe schaffen "
                                         "konnte, ist der Mieter nicht berechtigt, 1. die in § 536 bestimmten Rechte geltend "
                                         "zu machen, …“", "§ 536c Abs. 2 Satz 2 Nr. 1 BGB", "w536c2", size=31,
                    marken=[("Abhilfe", beim("w536c2", "Abhilfe")), ("geltend", beim("w536c2", "geltend"))])
folie([("w536c", f"{PA} · § 536c Abs. 1 BGB: unverzüglich anzeigen"), ("w536c2", f"{PA} › Folge, § 536c Abs. 2 Satz 2 Nr. 1 BGB"),
       ("anz", f"{PA} › Schimmel: November bis Januar"), ("anz2", f"{PA} › Heizung: sofort gemeldet")], [
    *tafel("w536c", "Anzeige des Mangels, § 536c"),
    *w1, *w2,
    z("Schimmel: von November bis Januar unbekannt", 110, w2_y + 18, "anz", "Bold", 31),
    *neinz("konnte sie deshalb nicht abhelfen: insoweit keine Minderung", w2_y + 64, beim("anz", "Konnte"), "Bold", 30,
           kreuz=beim("anz", "scheidet")),
    *okz("Heizung: sofort gemeldet – keine Sperre", w2_y + 118, "anz2", "Bold", 31),
    *requisit([("w536c", ("tabler", "phone", 90, WEISS), "unverzüglich melden", WEISS),
               ("anz", ("tabler", "calendar-x", 110, WEISS), "November bis Januar", HELLROT),
               ("anz2", ("tabler", "phone-check", 90, HELLGRUEN), "sofort gemeldet", HELLGRUEN)]),
    *stehend("FR", FX, [("w536c", "ruhig"), ("anz", "sorge"), ("anz2", "erleichtert")]),
])
assert w2_y + 118 + 50 <= 895, w2_y

# ===========================================================================================================================
# F § 536b BGB (Wortlautkarte Satz 1): Kenntnis bei Vertragsschluss
# ===========================================================================================================================
PK = "Kenntnis"
w3, w3_y = wortlaut(80, 170, 1100, "„Kennt der Mieter bei Vertragsschluss den Mangel der Mietsache, so stehen ihm die Rechte "
                                   "aus den §§ 536 und 536a nicht zu.“", "§ 536b Satz 1 BGB", "w536b", size=34,
                    marken=[("Kennt", beim("w536b", "Kennt")), ("bei Vertragsschluss", beim("w536b", "Vertragsschluss")),
                            ("nicht zu", beim("w536b", "nicht"))])
folie([("w536b", f"{PK} · § 536b Satz 1 BGB: bei Vertragsschluss"), ("kennt", f"{PK} › bei der Besichtigung gesehen?")], [
    *tafel("w536b", "Kenntnis, § 536b"),
    *w3,
    *neinz("bei der Besichtigung gesehen und trotzdem", w3_y + 40, "kennt", "Bold", 36, kreuz=beim("kennt", "nicht")),
    z("unterschrieben: keine Minderung", 185, w3_y + 92, beim("kennt", "unterschrieben"), "Bold", 36),
    *requisit([("w536b", ("tabler", "signature", 120, WEISS), "Vertragsschluss", WEISS),
               ("kennt", ("tabler", "eye", 110, WEISS), "Besichtigung", WEISS)]),
    *stehend("TB", FX, [("w536b", "ruhig"), ("kennt", "denkt")]),
])
assert w3_y + 140 <= 895, w3_y

# ===========================================================================================================================
# G Praxisrisiko: zu hohe Minderung → Verzug, § 543; Irrtum (VIII ZR 138/11); Vorbehalt; § 320 (VIII ZR 19/14)
# ===========================================================================================================================
PR = "Risiko"
folie([("risk", f"{PR} · Die halbe Miete"), ("verz", f"{PR} › Verzug, fristlose Kündigung, § 543 BGB"),
       ("irrt", f"{PR} › Irrtum über die Ursache"), ("vorb", f"{PR} › Zahlung unter Vorbehalt"),
       ("p320", f"{PR} › Zurückbehaltung, § 320 BGB")], [
    *tafel("risk", "Risiko: die halbe Miete"),
    *neinz("zu viel gemindert: Verzug mit dem Rest", 172, "verz", "Bold", 33, kreuz=beim("verz", "Verzug")),
    z("Rückstand etwa 2 Monatsmieten: fristlose Kündigung", 185, 226, beim("verz", "Erreicht"), "Bold", 32),
    zit("§ 543 Abs. 2 Satz 1 Nr. 3 BGB", 185, 274, beim("verz", "Paragraf")),
    *neinz("Irrtum über die Ursache: entschuldigt nicht, wenn erkennbar", 330, "irrt", "Bold", 31, kreuz=beim("irrt", "nicht")),
    zit("BGH, Urt. v. 11.7.2012 – VIII ZR 138/11, Leitsatz", 185, 378, beim("irrt", "Bundesgerichtshof")),
    blk(110, 432, 1040, 46 + 2 * 40, HELLGRUEN, "vorb", [("Sicherer: volle Miete unter Vorbehalt zahlen,", "ExtraBold", 31, INK),
                                                        ("Mehrbetrag zurückfordern", "Bold", 30, INK)]),
    zit("VIII ZR 138/11, Rn. 20: Vorbehalt schließt § 814 BGB aus", 110, 572, beim("vorb", "Vorbehalt")),
    z("§ 320 BGB: Teil zurückbehalten, Druck für die Reparatur", 110, 632, "p320", "Bold", 31),
    z("aber nur zeitlich und der Höhe nach begrenzt", 110, 678, beim("p320", "zeitlich"), "Bold", 31),
    zit("BGH, Versäumnisurt. v. 17.6.2015 – VIII ZR 19/14, Leitsatz 3", 110, 726, beim("p320", "zeitlich")),
    *requisit([("risk", ("tabler", "cash-banknote", 130, GRUEN_P), "halbe Miete?", HELLROT),
               (beim("verz", "fristlos"), ("tabler", "file-x", 100, WEISS), "fristlos kündigen", HELLROT),
               ("irrt", ("tabler", "alert-triangle", 110, GELB), "Irrtum", GELB),
               ("vorb", ("tabler", "receipt", 110, WEISS), "unter Vorbehalt", HELLGRUEN),
               ("p320", ("ph", "hand-coins", 120, WEISS), "zurückbehalten", WEISS)]),
    *paar("FR", [("risk", "sorge"), ("irrt", "denkt"), ("vorb", "erleichtert")],
          "TB", [("risk", "ernst"), ("vorb", "ruhig"), ("p320", "denkt")]),
])

# ===========================================================================================================================
# H Ergebnis: zurück im Zimmer
# ===========================================================================================================================
folie([("erg", "Ergebnis · kalte Woche: gemindert"), ("erg2", "Ergebnis › Schimmel: Ursache und Anzeige"),
       ("erg3", "Ergebnis › Baulärm: nur mit Anspruch gegen den Nachbarn")], [
    *zimmer("erg", draussen=[kran("erg"), bagger("erg")], schimmel_cue="erg"),
    *fig("FR", FRX, BODEN, FH, [("erg", "erleichtert_r"), ("erg2", "denkt_r"), ("erg3", "ernst_r")], erst="cut"),
    hart(ns(NAME["FR"], FRX, BODEN, "erg", NFARBE["FR"])),
    *fig("TB", TBX, BODEN, FH, [("erg", "ruhig"), ("erg2", "denkt"), ("erg3", "ernst")], erst="cut"),
    hart(ns(NAME["TB"], TBX, BODEN, "erg", NFARBE["TB"])),
    *okz("kalte Woche: Miete kraft Gesetzes gemindert", 30, "erg", "Bold", 33, x=150, rechts=1880),
    *okz("Schimmel: Ursache entscheidet; vor der Anzeige ggf. ausgeschlossen", 90, "erg2", "Bold", 32, x=150, rechts=1880),
    *okz("Baulärm: nur bei Abwehr- oder Entschädigungsanspruch der Vermieterin", 150, "erg3", "Bold", 32, x=150, rechts=1880),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · keine eigene Anspruchsgrundlage"), ("tipp2", "Klausurtipp · im Anspruch auf Miete prüfen"),
       ("tipp3", "Klausurtipp · zu viel gezahlt: Bereicherungsrecht")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Minderung: keine eigene Anspruchsgrundlage", 200, 200, beim("tipp", "Minderung"), "Bold", 34),
    z("prüfen im Anspruch auf Miete, § 535 Abs. 2 BGB", 200, 286, "tipp2", "Bold", 34),
    *okz("geschuldet: nur die geminderte Miete", 342, beim("tipp2", "Geschuldet"), "Bold", 34, x=245),
    linienzug([(130, 420), (1130, 420)], "tipp3", breite=3),
    z("voll gezahlt? Mehrbetrag zurückverlangen:", 200, 450, "tipp3", "ExtraBold", 34),
    z("§ 812 Abs. 1 Satz 1 Alt. 1 BGB", 245, 512, beim("tipp3", "Bereicherungsrecht"), "Bold", 34),
    zit("vgl. § 556b Abs. 2 BGB: „… wegen zu viel gezahlter Miete“", 245, 566,
        beim("tipp3", "Bereicherungsrecht")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Anspruch entstanden, § 535 Abs. 2 BGB", True),
          ("k2", 0, "II. Minderung kraft Gesetzes, § 536 BGB", True),
          ("k2a", 1, "1. Mangel: nachteilige Abweichung von Ist und Soll", False),
          ("k2b", 1, "2. nicht unerheblich, § 536 Abs. 1 Satz 3", False),
          ("k2c", 1, "3. keine Kenntnis bei Vertragsschluss, § 536b", False),
          ("k2d", 1, "4. keine Sperre wegen unterlassener Anzeige, § 536c Abs. 2", False),
          ("k2e", 1, "5. Umfang: angemessen, von der Bruttomiete", False),
          ("k3", 0, "III. Ergebnis: geschuldet ist nur die geminderte Miete", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Vermieterin gegen Mieter auf Miete"), 110, 90, "sch", 44)]
y = 196
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 36, rechts=1800))
    y += {0: 104, 1: 84}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("k1", "Prüfungsschema › I. Anspruch entstanden"),
       ("k2", "Prüfungsschema › II. Minderung, § 536 BGB"), ("k3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Miete mindert sich ", 0), ("von selbst", "a"), (",", 0)],
                 [("sobald ein nicht unerheblicher", 0)], [("Mangel da ist.", 0)]],
                750, 265, 44, "merke", {"a": beim("merke", "selbst")}),
    *markertext([[("Zeig ihn aber ", 0), ("sofort", "b"), (" an, und zahle", 0)],
                 [("im Zweifel unter ", 0), ("Vorbehalt", "c"), (",", 0)], [("statt einfach weniger zu überweisen.", 0)]],
                750, 530, 44, "merk2", {"b": beim("merk2", "sofort"), "c": beim("merk2", "Vorbehalt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
