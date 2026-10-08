"""Folge 265 · „Gekauft wie gesehen“: Hält der Gewährleistungsausschluss? · Serienstandard Open Peeps (Katzenkönig).
Fall: Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Nach Besichtigung und
Probefahrt: „Der Motor läuft einwandfrei.“ Handschriftlicher Vertrag: „Motor läuft einwandfrei.“ und „Gekauft wie gesehen,
keine Gewährleistung.“ 3 Wochen später ist der Motor hinüber; der Schaden war schon beim Kauf da; Herr Burmeister wusste
nichts. Danach: 1. Sachmangel § 434 (Wortlautkarte), Verweis Folge 059; 2. Ausschluss wirksam? (§ 476, Individualvereinbarung,
§ 309 Nr. 7); 3. Reichweite „gekauft wie gesehen“ (BGH VIII ZR 261/14, VIII ZR 136/04); § 444 (Wortlautkarte), Arglist (−),
Abgrenzung Folge 262, Garantie (−) (BGHZ 170, 86 Rn. 20, 25 f.; VIII ZR 161/23 Rn. 21); 4. vereinbarte Beschaffenheit geht vor
(BGHZ 170, 86 Rn. 30 f.; VIII ZR 161/23 Rn. 23, 38, 40); Ergebnis je Variante, Verweis Folge 063; Klausurtipp; Schema; Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/mitte/schild/
absatz_nb/requisit/stehend/paar/okw als eigene Kopie aus Folge 262 (gemeinsame Dateien unverändert); neu: auto(), haus(),
vertrag_karte().
Darstellung: keine echten Automarken (Tabler car, ohne Logo), kein Unfall; Haus Phosphor house, Werkstatt nur als Schild und
Werkzeug (Tabler tools). Keine Richterhämmer.
Handlungsgeräusche: Unterschrift, Schlüssel, Anlasser (Freesound CC0, ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_265/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_265/" in n:
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
NAME = {"CH": "Christel", "BU": "Herr Burmeister", "ME": "Mechanikerin"}
BLAU_P, LILA_P = (141, 179, 242, 255), (184, 169, 245, 255)
GRUEN_P, ROT_P = (143, 214, 148, 255), (240, 122, 106, 255)
NFARBE = {"CH": LILA_P, "BU": GRUEN_P, "ME": BLAU_P}


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


def sachverhalt_265(cue, absaetze, frage, size=34):
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






def auto(cx, unten, breite, cue, bis=None, anim="cut", d=0.0):
    """Der Kleinwagen: Tabler car (ohne Marke), Palettenfüllung Rot, Fenster weiß."""
    return ficon("tabler", "car", cx, unten, breite, cue, fuell=ROT_P, nebenfarbe=WEISS, bis=bis, anim=anim, d=d)


def haus(cx, unten, breite, cue, bis=None):
    """Wohnhaus von Herrn Burmeister (Phosphor house), Privatverkauf vor der Haustür."""
    return hart(ficon("ph", "house", cx, unten, breite, cue, fuell=HELL, nebenfarbe=BLAUHELL, bis=bis))


# ===========================================================================================================================
# A Fall: Privatverkauf vor dem Haus (fall … schluessel)
# ===========================================================================================================================
HX, CHX, CARX, BUX = 205, 560, 1030, 1500
VX, VY, VW, VH = 690, 50, 700, 380                 # Kaufvertrag (Karte über dem Auto)
folie([(NULL, "Fall · Christel sucht einen Kleinwagen"), ("hof", "Fall · Privatverkauf: Kleinwagen für 4.500 €"),
       ("probe", "Fall · Besichtigung und Probefahrt"), ("b1", "Fall · Herr Burmeister: „Der Motor läuft einwandfrei.“"),
       ("vertrag", "Fall · Handschriftlicher Kaufvertrag"), ("unterschr", "Fall · Unterschrieben, Schlüssel übergeben")], [
    boden(NULL), haus(HX, BODEN + 4, 300, NULL),
    # Christel (links, blickt nach rechts zum Auto und zu Herrn Burmeister)
    *fig("CH", CHX, BODEN, FH, [(NULL, "ruhig_r"), ("hof", "denkt_r"), ("probe", "staunt_r"), (beim("probe", "Alles"), "froh_r"),
                                ("b1", "ruhig_r"), ("vertrag", "denkt_r"), ("unterschr", "froh_r"),
                                ("schluessel", "strahlt_r")], erst="cut"),
    hart(ns(NAME["CH"], CHX, BODEN, NULL, NFARBE["CH"])),
    pl("sucht einen gebrauchten Kleinwagen", CHX, 335, beim("fall", "sucht"), fill=WEISS, size=30, anker="m", bis="hof"),
    # Herr Burmeister und sein Auto
    *fig("BU", BUX, BODEN, FH, [(beim("hof", "Burmeister"), "froh"), ("probe", "ruhig")], bis="b1", erst="pop"),
    *redet("BU_redet", BUX, BODEN, FH, "b1", "vertrag"),
    *fig("BU", BUX, BODEN, FH, [("vertrag", "ruhig"), ("unterschr", "froh")], erst="cut"),
    ns(NAME["BU"], BUX, BODEN, beim("hof", "Burmeister"), NFARBE["BU"], d=0.1),
    pl("privat", BUX, 330, beim("hof", "privat"), fill=GRUEN_P, size=30, anker="m", bis="b1"),
    auto(CARX, BODEN + 4, 420, beim("hof", "Auto"), anim="pop"),
    pl("Zu verkaufen: 4.500 €", CARX, 470, beim("hof", "viertausendfünfhundert"), fill=GELB, size=34, anker="m", bis="vertrag"),
    # Besichtigung und Probefahrt
    ficon("tabler", "eye", CHX - 150, 330, 76, beim("probe", "sieht"), fuell=WEISS, bis="b1"),
    pl("Besichtigung", CHX + 30, 255, beim("probe", "sieht"), fill=WEISS, size=30, anker="m", bis="b1"),
    ficon("tabler", "steering-wheel", CHX - 150, 230, 70, beim("probe", "Probefahrt"), fuell=WEISS, bis="b1"),
    pl("Probefahrt", CHX + 30, 175, beim("probe", "Probefahrt"), fill=WEISS, size=30, anker="m", bis="b1"),
    pl("alles in Ordnung", CHX + 30, 95, beim("probe", "Alles"), fill=HELLGRUEN, size=30, anker="m", bis="b1"),
    blase("sprech", 640, 190, "b1", 1080, 250, inhalt=["Der Motor läuft einwandfrei."], textsize=38,
          figur=("BU_redet", BUX, BODEN, FH), bis="vertrag"),
    ficon("tabler", "engine", CARX, 455, 96, beim("b1", "Motor"), fuell=HELLGRUEN, bis="vertrag"),
    # Kaufvertrag (handschriftlich, gemeinsam formuliert)
    feld(VX, VY, VW, VH, "vertrag", fill=WEISS, rand=5, rund=16, anim="pop", name="kaufvertrag"),
    mitte("Kaufvertrag", VX + VW / 2, VY + 22, "vertrag", "ExtraBold", 36),
    mitte("Kleinwagen, 4.500 €", VX + VW / 2, VY + 78, "vertrag", "Bold", 30),
    mitte("„Motor läuft einwandfrei.“", VX + VW / 2, VY + 135, beim("vertrag", "Motor"), "ExtraBold", 34),
    mitte("„Gekauft wie gesehen,", VX + VW / 2, VY + 195, beim("klausel", "Gekauft"), "ExtraBold", 34),
    mitte("keine Gewährleistung.“", VX + VW / 2, VY + 245, beim("klausel", "keine"), "ExtraBold", 34),
    szene(ficon("tabler", "signature", VX + 170, VY + VH - 16, 92, "unterschr", fuell=WEISS), "265unterschrift*", 0.8, 0.05),
    ficon("tabler", "signature", VX + VW - 170, VY + VH - 16, 92, beim("unterschr", "unterschreiben"), fuell=WEISS),
    szene(bewegt(ficon("tabler", "key", CHX + 150, 690, 80, "schluessel", fuell=GELB),
                 "schluessel", beim("schluessel", "Schlüssel", ende=True), (BUX - 170) - (CHX + 150), 0),
          "265schluessel*", 0.7, 0.0),
])

# ===========================================================================================================================
# B 3 Wochen später: in der Werkstatt (werk … m1)
# ===========================================================================================================================
CHB, CARB, MEX = 380, 930, 1520
folie([("werk", "Fall · 3 Wochen später: in der Werkstatt"), ("m1", "Fall · Mechanikerin: „Der Motor ist hinüber.“")], [
    boden("werk"),
    hart(pl("3 Wochen später", 70, 30, "werk", fill=GELB, size=30)),
    *schild("Kfz-Werkstatt", 1290, 40, "werk", size=38, fill=BLAUHELL),
    hart(ficon("ph", "toolbox", 1790, BODEN + 4, 140, "werk", fuell=GELB, nebenfarbe=WEISS)),
    auto(CARB, BODEN + 4, 420, "werk", anim="cut"),
    szene(ficon("tabler", "key", CARB - 130, 560, 70, beim("werk", "Werkstatt"), fuell=GELB, bis="m1"),
          "265anlasser*", 0.55, 0.0),
    ficon("tabler", "engine-off", CARB, 525, 110, beim("m1", "hinüber"), fuell=HELLROT),
    pl("Motorschaden", CARB, 340, beim("m1", "hinüber"), fill=HELLROT, size=32, anker="m"),
    pl("schon beim Kauf da", 620, 340, beim("m1", "Schaden"), fill=GELB, size=32, anker="m"),
    # Mechanikerin (rechts, blickt nach links zum Auto)
    *fig("ME", MEX, BODEN, FH, [("werk", "ruhig")], bis="m1", erst="pop"),
    *redet("ME_redet", MEX, BODEN, FH, "m1", "c1"),
    ns(NAME["ME"], MEX, BODEN, "werk", NFARBE["ME"], d=0.1),
    blase("sprech", 820, 210, "m1", 1000, 165, inhalt=["Der Motor ist hinüber. Und der", "Schaden war schon beim Kauf da."],
          textsize=32, figur=("ME_redet", MEX, BODEN, FH)),
    # Christel (links, blickt nach rechts)
    *fig("CH", CHB, BODEN, FH, [("werk", "denkt_r"), (beim("m1", "hinüber"), "staunt_r"), (beim("m1", "Schaden"), "sorge_r")],
         erst="pop"),
    ns(NAME["CH"], CHB, BODEN, "werk", NFARBE["CH"], d=0.1),
])

# ===========================================================================================================================
# C Zurück vor dem Haus: Herr Burmeister beruft sich auf den Ausschluss – die Frage (c1 … frage2)
# ===========================================================================================================================
CHC, BUC = 560, 1500
folie([("c1", "Fall · Christel: „Der Motor war von Anfang an kaputt!“"),
       ("b2", "Fall · Herr Burmeister: „gekauft wie gesehen, keine Gewährleistung“"),
       ("frage", "Die Frage · Hält der Ausschluss?"), ("frage2", "Die Frage · Mängelrechte trotzdem?")], [
    boden("c1"), haus(HX, BODEN + 4, 300, "c1"),
    *redet("CH_redet_r", CHC, BODEN, FH, "c1", "b2"),
    *fig("CH", CHC, BODEN, FH, [("b2", "aerger_r"), ("frage", "denkt_r")], erst="cut"),
    ns(NAME["CH"], CHC, BODEN, "c1", NFARBE["CH"], d=0.1),
    *fig("BU", BUC, BODEN, FH, [("c1", "staunt")], bis="b2", erst="pop"),
    *redet("BU_redet2", BUC, BODEN, FH, "b2", "frage"),
    *fig("BU", BUC, BODEN, FH, [("frage", "ernst")], erst="cut"),
    ns(NAME["BU"], BUC, BODEN, "c1", NFARBE["BU"], d=0.1),
    blase("sprech", 720, 210, "c1", 1010, 250, inhalt=["Herr Burmeister, der Motor", "war von Anfang an kaputt!"],
          textsize=34, figur=("CH_redet_r", CHC, BODEN, FH), bis="b2"),
    blase("sprech", 850, 270, "b2", 950, 225, inhalt=["Davon wusste ich nichts. Und", "es heißt: gekauft wie gesehen,",
                                                     "keine Gewährleistung."], textsize=34,
          figur=("BU_redet2", BUC, BODEN, FH), bis="frage"),
    pl("Hält dieser Ausschluss?", 300, 140, "frage", fill=PINK, size=36),
    pl("Oder kann Christel trotzdem ihre Mängelrechte geltend machen?", 300, 225, "frage2", fill=PINK, size=32),
])

# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
sachverhalt_265("sv", [
    "Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Nach Besichtigung und "
    "Probefahrt sagt Herr Burmeister: „Der Motor läuft einwandfrei.“ In den handschriftlichen Kaufvertrag, den beide "
    "gemeinsam formulieren, schreiben sie: „Motor läuft einwandfrei.“ Darunter steht: „Gekauft wie gesehen, keine "
    "Gewährleistung.“ Weitere Zusagen macht Herr Burmeister nicht.",
    "3 Wochen später ist der Motor hinüber. Die Mechanikerin stellt fest: Der Schaden war schon bei der Übergabe da; "
    "sehen konnte man ihn nicht. Herr Burmeister wusste davon nichts. Er beruft sich auf den Ausschluss.",
], "Kann Christel trotzdem ihre Mängelrechte geltend machen?", size=36)

# ===========================================================================================================================
# E 1. Sachmangel, § 434 BGB (Wortlautkarte)
# ===========================================================================================================================
PA = "A. Sachmangel"
w434, w434_y = wortlaut(80, 165, 1100, "„(1) Die Sache ist frei von Sachmängeln, wenn sie bei Gefahrübergang den subjektiven "
                                       "Anforderungen, den objektiven Anforderungen und den Montageanforderungen dieser "
                                       "Vorschrift entspricht. (2) Die Sache entspricht den subjektiven Anforderungen, wenn "
                                       "sie 1. die vereinbarte Beschaffenheit hat, … (3) … entspricht die Sache den "
                                       "objektiven Anforderungen, wenn sie 1. sich für die gewöhnliche Verwendung eignet, …“",
                        "§ 434 Abs. 1, Abs. 2 S. 1 Nr. 1, Abs. 3 S. 1 Nr. 1 BGB", "p434", size=30,
                        marken=[("Gefahrübergang", beim("p434", "Gefahrübergang")),
                                ("subjektiven", beim("p434", "subjektiven")), ("objektiven", beim("p434", "objektiven")),
                                ("vereinbarte", beim("subj", "vereinbarte")),
                                ("gewöhnliche", beim("objektiv", "gewöhnliche"))])
folie([("mangel", f"{PA}? · § 434 BGB"), ("subj", f"{PA} › subjektiv: vereinbarte Beschaffenheit"),
       ("objektiv", f"{PA} › objektiv: gewöhnliche Verwendung"), ("mangelok", f"{PA} (+)"),
       ("v059", f"{PA} › Folge „Wann ist eine Sache mangelhaft?“")], [
    *tafel("mangel", "1. Ist der Wagen mangelhaft?"),
    *w434,
    *okw("vereinbart: „Motor läuft einwandfrei.“", w434_y + 30, "motor", beim("motor", "Übergabe"), "Bold", 32, x=160),
    z("fehlt schon bei der Übergabe", 160, w434_y + 78, beim("motor", "Übergabe"), "Regular", 30),
    *okw("objektiv: nicht für die gewöhnliche Verwendung", w434_y + 135, "objektiv", beim("objektiv", "nicht"), "Bold", 32, x=160),
    *plusminus("Sachmangel", 110, w434_y + 200, beim("mangelok", "Sachmangel"), True, size=36, stil="ExtraBold"),
    pl("Folge „Wann ist eine Sache mangelhaft?“", 470, w434_y + 196, beim("v059", "Folge"), fill=LILAHELL, size=28),
    *requisit([("mangel", ("tabler", "car", 170, ROT_P), "Motor kaputt", HELLROT),
               ("subj", ("tabler", "contract", 120, WEISS), "„einwandfrei“", HELLGRUEN),
               ("objektiv", ("tabler", "engine-off", 130, HELLROT), "fährt nicht", HELLROT)]),
    *stehend("CH", FX, [("mangel", "denkt"), ("subj", "ruhig"), ("mangelok", "froh")]),
])
assert w434_y + 250 <= 895, w434_y

# ===========================================================================================================================
# F 2. Ausschluss wirksam?
# ===========================================================================================================================
PB = "B. Gewährleistungsausschluss"
folie([("aus", f"{PB} · 2. wirksam?"), ("priv", f"{PB} › Privatverkauf"),
       ("v476", f"{PB} › § 476 BGB: nur Verbrauchsgüterkauf"), ("indiv", f"{PB} › selbst formuliert: wirksam"),
       ("agb", f"{PB} › falls AGB: § 309 Nr. 7 BGB")], [
    *tafel("aus", "2. Ausschluss wirksam?"),
    z("Christel kauft privat, von einer Privatperson", 110, 185, "priv", "Bold", 34),
    *neinz("§ 476 BGB: nur beim Verbrauchsgüterkauf", 285, "v476", "Bold", 34, x=160, kreuz=beim("v476", "nur")),
    z("Unternehmer verkauft an Verbraucher", 160, 337, beim("v476", "also"), "Regular", 32),
    zit("§§ 474 Abs. 1, 476 Abs. 1 BGB", 160, 385, beim("v476", "Unternehmer")),
    *okz("selbst formuliert: keine AGB", 460, "indiv", "Bold", 34, x=160),
    *okw("Ausschluss grundsätzlich wirksam", 520, beim("indiv", "Er"), beim("indiv", "wirksam"), "ExtraBold", 34, x=160),
    zit("§ 305 Abs. 1 BGB", 160, 572, beim("indiv", "wirksam")),
    blk(110, 625, 1040, 150, HELLGRAU, "agb", [("Falls AGB: § 309 Nr. 7 BGB", "ExtraBold", 32, INK),
                                             ("kein Ausschluss der Haftung für Leben, Körper,", "Bold", 30, INK),
                                             ("Gesundheit und grobes Verschulden", "Bold", 30, INK)]),
    *requisit([("aus", ("tabler", "shield-off", 110, WEISS), "Ausschluss?", WEISS),
               ("priv", ("ph", "house", 130, HELL), "privat", GRUEN_P),
               ("v476", ("tabler", "user", 110, WEISS), "kein Unternehmer", HELLGRAU),
               ("indiv", ("tabler", "writing-sign", 110, WEISS), "handschriftlich", HELLGRUEN)], px=1560, pu=330, py=90),
    *paar("CH", [("aus", "denkt"), ("indiv", "sorge")], "BU", [("aus", "ruhig"), ("indiv", "froh")]),
])

# ===========================================================================================================================
# G 3. Reichweite: „gekauft wie gesehen“ + „keine Gewährleistung“
# ===========================================================================================================================
folie([("ausl", f"{PB} › 3. Reichweite"), ("gesehen", f"{PB} › „wie gesehen“: nur wahrnehmbare Mängel"),
       ("unsicht", f"{PB} › Motorschaden: nicht sichtbar"), ("keine", f"{PB} › dazu: „keine Gewährleistung“"),
       ("umfass", f"{PB} › umfassender Ausschluss"), ("zwerg", f"{PB} › Motorschaden grundsätzlich erfasst")], [
    *tafel("ausl", "3. Wie weit reicht der Ausschluss?", size=44),
    feld(110, 170, 1040, 270, "gesehen", fill=BLAUHELL, rand=5, rund=18, anim="pop", name="gesehen"),
    z("„Gekauft wie gesehen“ allein:", 140, 185, "gesehen", "ExtraBold", 34),
    z("in aller Regel nur Mängel, die bei der Besichtigung", 140, 238, beim("gesehen", "Regel"), "Bold", 30),
    z("wahrnehmbar sind, vor allem sichtbare", 140, 284, beim("gesehen", "wahrnehmen"), "Bold", 30),
    zit("BGH, Urt. v. 6.4.2016 – VIII ZR 261/14, Rn. 22", 140, 332, beim("gesehen", "sichtbare")),
    *neinz("Motorschaden: nicht zu sehen", 378, "unsicht", "Bold", 32, x=185, kreuz=beim("unsicht", "nicht")),
    feld(110, 465, 1040, 220, "keine", fill=GELB, rand=5, rund=18, anim="pop", name="keine"),
    z("dazu: „keine Gewährleistung“", 140, 480, "keine", "ExtraBold", 34),
    z("Verbindung = umfassender Ausschluss", 140, 533, beim("umfass", "Verbindung"), "Bold", 32),
    zit("BGH, Urt. v. 6.7.2005 – VIII ZR 136/04 (Leitsatz)", 140, 583, beim("umfass", "umfassenden")),
    zit("vgl. BGH, Urt. v. 6.4.2016 – VIII ZR 261/14, Rn. 24", 140, 625, beim("umfass", "umfassenden")),
    blk(110, 715, 1040, 110, HELLROT, "zwerg", [("erfasst grundsätzlich auch", "ExtraBold", 32, INK),
                                               ("den versteckten Motorschaden", "ExtraBold", 32, INK)]),
    *requisit([("gesehen", ("tabler", "eye", 120, WEISS), "nur Sichtbares", BLAUHELL),
               ("unsicht", ("tabler", "eye-off", 120, WEISS), "Motor: verborgen", HELLGRAU),
               ("keine", ("tabler", "shield-off", 120, WEISS), "keine Gewährleistung", GELB)]),
    *stehend("CH", FX, [("ausl", "denkt"), ("unsicht", "froh"), ("keine", "staunt"), ("zwerg", "sorge")]),
])

# ===========================================================================================================================
# H1 § 444 BGB (Wortlautkarte): Arglist (−), Abgrenzung Folge 262
# ===========================================================================================================================
w444, w444_y = wortlaut(80, 165, 1100, "„Auf eine Vereinbarung, durch welche die Rechte des Käufers wegen eines Mangels "
                                       "ausgeschlossen oder beschränkt werden, kann sich der Verkäufer nicht berufen, soweit "
                                       "er den Mangel arglistig verschwiegen oder eine Garantie für die Beschaffenheit der "
                                       "Sache übernommen hat.“", "§ 444 BGB", "p444", size=32,
                        marken=[("ausgeschlossen", beim("p444", "ausgeschlossen")), ("berufen", beim("p444", "berufen")),
                                ("arglistig", beim("p444", "arglistig")), ("Garantie", beim("p444", "Garantie"))])
folie([("p444", f"{PB} › Grenze: § 444 BGB"), ("arg", f"{PB} › § 444 BGB: Arglist (−)"),
       ("v262", f"{PB} › Händler und Anfechtung: Folge „Unfallwagen verschwiegen“")], [
    *tafel("p444", "Grenze: § 444 BGB"),
    *w444,
    *neinz("Arglist: Herr Burmeister wusste nichts vom Schaden", w444_y + 40, "arg", "Bold", 34, x=160,
           kreuz=beim("arg", "scheidet")),
    blk(110, w444_y + 125, 1040, 150, LILAHELL, "v262", [("Händler, Unfallschaden, Anfechtung:", "ExtraBold", 31, INK),
                                                        ("Folge „Unfallwagen verschwiegen“", "Bold", 31, INK),
                                                        ("hier: Privatverkauf und Ausschluss", "Bold", 30, INK)]),
    *requisit([("p444", ("tabler", "shield-off", 110, WEISS), "Grenzen?", WEISS),
               ("arg", ("tabler", "help", 110, WEISS), "nichts gewusst", HELLGRAU)], px=1560, pu=330, py=90),
    *paar("CH", [("p444", "denkt"), ("arg", "sorge")], "BU", [("p444", "ruhig"), ("arg", "ernst")]),
])
assert w444_y + 125 + 150 <= 895, w444_y

# ===========================================================================================================================
# H2 § 444 BGB: Garantie (−)
# ===========================================================================================================================
folie([("gar", f"{PB} › § 444 BGB: Garantie?"), ("privgar", f"{PB} › Garantie beim Privatverkauf: nur ausnahmsweise"),
       ("garnein", f"{PB} › Garantie (−): § 444 BGB hilft nicht")], [
    *tafel("gar", "Und eine Garantie?"),
    z("Garantie geht weiter als eine bloße Angabe:", 110, 185, "gar", "Bold", 34),
    z("Haftung sogar ohne Verschulden", 110, 240, beim("gar", "Verkäufer"), "ExtraBold", 34),
    zit("BGH, Urt. v. 29.11.2006 – VIII ZR 92/06, BGHZ 170, 86 Rn. 20", 110, 292, beim("gar", "Schadensersatz")),
    z("Privatverkauf: ohne ausdrückliche Abrede", 110, 370, "privgar", "Bold", 34),
    z("nur unter besonderen Umständen", 110, 422, beim("privgar", "nur"), "ExtraBold", 34),
    zit("BGHZ 170, 86 Rn. 25 f.; BGH, Urt. v. 10.4.2024 – VIII ZR 161/23, Rn. 21", 110, 474, beim("privgar", "Umständen")),
    *neinz("keine besonderen Umstände: keine Garantie", 555, "garnein", "Bold", 34, x=160, kreuz=beim("garnein", "nicht")),
    *plusminus("§ 444 BGB hilft Christel", 110, 650, beim("garnein", "Paragraf"), False, size=38, stil="ExtraBold"),
    *requisit([("gar", ("tabler", "certificate", 120, WEISS), "Garantie?", WEISS),
               ("privgar", ("ph", "house", 130, HELL), "privat", GRUEN_P),
               ("garnein", ("tabler", "x", 100, WEISS), "keine Garantie", HELLROT)]),
    *stehend("BU", FX, [("gar", "denkt"), ("privgar", "ruhig"), ("garnein", "froh")]),
])

# ===========================================================================================================================
# I 4. Die vereinbarte Beschaffenheit geht vor (BGHZ 170, 86)
# ===========================================================================================================================
folie([("vorrang", f"{PB} › vereinbarte Beschaffenheit geht vor"), ("bghz", f"{PB} › BGHZ 170, 86: Ausschluss gilt nicht dafür"),
       ("sinn", f"{PB} › sonst „ohne Sinn und Wert“"), ("heute", f"{PB} › ständige Rechtsprechung"),
       ("ergeb", f"{PB} › Haftung für den Motor (+)")], [
    *tafel("vorrang", "Die Beschaffenheit geht vor"),
    blk(110, 170, 500, 140, HELLGRUEN, beim("vorrang", "Motor"), [("„Motor läuft", "ExtraBold", 32, INK),
                                                                  ("einwandfrei.“", "ExtraBold", 32, INK)]),
    blk(650, 170, 500, 140, GELB, beim("vorrang", "Motor"), [("„Gekauft wie gesehen,", "Bold", 30, INK),
                                                             ("keine Gewährleistung.“", "Bold", 30, INK)]),
    z("Beschaffenheit vereinbart + pauschaler Ausschluss:", 110, 345, "bghz", "Bold", 32),
    z("Ausschluss gilt in der Regel nicht für das", 110, 395, beim("bghz", "gilt"), "ExtraBold", 32),
    z("Fehlen der vereinbarten Beschaffenheit", 110, 445, beim("bghz", "Fehlen"), "ExtraBold", 32),
    zit("BGH, Urt. v. 29.11.2006 – VIII ZR 92/06, BGHZ 170, 86 Rn. 30 f.", 110, 497, beim("bghz", "Fehlen")),
    z("sonst „ohne Sinn und Wert“ für den Käufer", 110, 555, "sinn", "Bold", 32),
    z("ständige Rechtsprechung, auch bei alten Autos", 110, 615, "heute", "Bold", 32),
    z("und bei Verschleißteilen", 110, 663, beim("heute", "bei", nr=2), "Bold", 32),
    zit("BGH, Urt. v. 10.4.2024 – VIII ZR 161/23, Rn. 23, 38, 40", 110, 713, beim("heute", "Teilen")),
    *okz("Ausschluss nur für andere Mängel", 760, "ergeb", "Bold", 32, x=160),
    *plusminus("Haftung für den Motor", 160, 812, beim("ergeb", "Für"), True, size=34, stil="ExtraBold"),
    *requisit([("vorrang", ("tabler", "contract", 120, WEISS), "Vertrag ganz lesen", WEISS),
               ("bghz", ("ph", "scales", 130, WEISS), "BGHZ 170, 86", BLAUHELL),
               ("ergeb", ("tabler", "engine", 130, HELLGRUEN), "Motor: Haftung", HELLGRUEN)], px=1560, pu=330, py=90),
    *paar("CH", [("vorrang", "denkt"), ("bghz", "staunt"), ("ergeb", "strahlt")],
          "BU", [("vorrang", "ruhig"), ("bghz", "sorge"), ("ergeb", "ernst")]),
])

# ===========================================================================================================================
# J Ergebnis je Variante
# ===========================================================================================================================
PC = "C. Ergebnis je Variante"
KX = 820                                        # Ergebnisspalte
folie([("var", f"{PC}"), ("va1", f"{PC} › ohne Satz zum Motor: Ausschluss greift"),
       ("va2", f"{PC} › nur „gekauft wie gesehen“: nicht erfasst"), ("va3", f"{PC} › Arglist oder Garantie: § 444 BGB"),
       ("va4", f"{PC} › unser Fall: Beschaffenheit vereinbart"), ("v063", f"{PC} › Folge „Die Käuferrechte auf einen Blick“")], [
    *tafel("var", "Ergebnis je Variante"),
    z("ohne „Motor läuft einwandfrei.“", 110, 180, "va1", "ExtraBold", 32),
    z("Ausschluss greift", 110, 228, beim("va1", "greift"), "Regular", 30),
    *plusminus("Mängelrechte", KX, 180, beim("va1", "keine"), False, size=32, stil="Bold"),
    z("nur „gekauft wie gesehen“", 110, 300, "va2", "ExtraBold", 32),
    z("unsichtbarer Motorschaden in der Regel nicht erfasst", 110, 348, beim("va2", "unsichtbare"), "Regular", 30),
    *plusminus("Mängelrechte", KX, 300, beim("va2", "erfasst"), True, size=32, stil="Bold"),
    z("Arglist oder Garantie", 110, 420, "va3", "ExtraBold", 32),
    z("kein Berufen auf den Ausschluss, § 444 BGB", 110, 468, beim("va3", "könnte"), "Regular", 30),
    *plusminus("Mängelrechte", KX, 420, beim("va3", "berufen"), True, size=32, stil="Bold"),
    feld(95, 530, 1070, 125, "va4", fill=HELLGRUEN, rand=5, rund=18, anim="pop", name="unserfall"),
    z("unser Fall: Beschaffenheit vereinbart", 125, 545, "va4", "ExtraBold", 32),
    z("die vereinbarte Beschaffenheit geht vor", 125, 595, beim("va4", "vereinbarte"), "Regular", 30),
    *plusminus("Mängelrechte", KX, 545, beim("va4", "Christel"), True, size=32, stil="Bold"),
    z("zuerst: Nacherfüllung, §§ 437 Nr. 1, 439 BGB", 110, 690, "v063", "Bold", 32),
    pl("Folge „§ 437 BGB: Die Käuferrechte auf einen Blick“", 110, 760, beim("v063", "Mehr"), fill=LILAHELL, size=28),
    *requisit([("var", ("tabler", "list-check", 120, WEISS), "Varianten", WEISS),
               ("va4", ("tabler", "engine", 130, HELLGRUEN), "unser Fall", HELLGRUEN),
               ("v063", ("tabler", "tools", 120, WEISS), "Nacherfüllung", GELB)]),
    *stehend("CH", FX, [("var", "denkt"), ("va1", "sorge"), ("va2", "ruhig"), ("va4", "strahlt")]),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Ausschluss in drei Schritten"), ("tipp2", "Klausurtipp · den ganzen Vertrag lesen"),
       ("tipp3", "Klausurtipp · Beschaffenheit vereinbart? Keine Garantie nötig")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Ausschluss in drei Schritten prüfen:", 200, 200, "tipp", "Bold", 34),
    z("1. wirksam?", 230, 255, beim("tipp", "Ist"), "ExtraBold", 34),
    z("2. Reichweite?", 480, 255, beim("tipp", "Wie"), "ExtraBold", 34),
    z("3. § 444 BGB?", 790, 255, beim("tipp", "Und"), "ExtraBold", 34),
    linienzug([(130, 335), (1130, 335)], "tipp2", breite=3),
    z("Den ganzen Vertrag lesen, nicht nur die Klausel", 200, 365, "tipp2", "ExtraBold", 34),
    zit("BGHZ 170, 86 Rn. 30", 200, 417, beim("tipp2", "Klausel")),
    z("Beschaffenheit vereinbart? Dann nimmt der", 200, 485, "tipp3", "Bold", 34),
    z("Ausschluss sie in der Regel aus", 200, 537, beim("tipp3", "Ausschluss"), "ExtraBold", 34),
    z("Eine Garantie braucht es dafür nicht", 200, 600, beim("tipp3", "Eine"), "Bold", 34),
    zit("BGH, Urt. v. 10.4.2024 – VIII ZR 161/23, Rn. 21, 23", 200, 660, beim("tipp3", "Eine")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kaufvertrag und Sachmangel bei Gefahrübergang, § 434 BGB", True),
          ("s2", 0, "II. Gewährleistungsausschluss", True),
          ("s2a", 1, "1. wirksam vereinbart; kein Verbrauchsgüterkauf, § 476 BGB", False),
          ("s2b", 1, "2. Reichweite: „gekauft wie gesehen, keine Gewährleistung“ = umfassend", False),
          ("s2c", 1, "3. § 444 BGB: Arglist (−), Garantie (−)", False),
          ("s2d", 1, "4. aber: nicht für die vereinbarte Beschaffenheit (BGHZ 170, 86)", False),
          ("s3", 0, "III. Ergebnis: Christel hat ihre Mängelrechte", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Christel gegen Herrn Burmeister"), 110, 90, "sch", 44),
           z("Mängelrechte aus § 437 BGB", 110, 158, beim("sch", "Mängelrechte"), "Bold", 36, rechts=1800)]
y = 260
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1820))
    y += {0: 95, 1: 80, 2: 80}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Sachmangel"),
       ("s2", "Prüfungsschema › II. Gewährleistungsausschluss"), ("s2b", "Prüfungsschema › II. 2. Reichweite"),
       ("s2c", "Prüfungsschema › II. 3. § 444 BGB"), ("s2d", "Prüfungsschema › II. 4. vereinbarte Beschaffenheit"), ("s3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("„Gekauft wie gesehen, keine", 0)], [("Gewährleistung“ schließt beim", 0)],
                 [("Privatkauf ", 0), ("viel aus.", "a")]],
                750, 270, 44, "merke", {"a": beim("merke", "viel")}),
    *markertext([[("Aber regelmäßig ", 0), ("nicht", "b"), (", was als", 0)],
                 [("Beschaffenheit vereinbart", "c"), (" ist,", 0)],
                 [("und ", 0), ("nie", "d"), (" bei Arglist oder Garantie.", 0)]],
                750, 520, 44, "merk2", {"b": beim("merk2", "nicht"), "c": beim("merk2", "Beschaffenheit"),
                                        "d": beim("merk2", "nie")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
