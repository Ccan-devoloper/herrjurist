"""Folge 268 · Reparatur oder neues Gerät? Nacherfüllung § 439 BGB · Serienstandard Open Peeps (Katzenkönig).
Fall: Undine kauft im August 2026 im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. 3 Wochen später schaltet
es sich immer wieder von selbst aus. Herr Stelzer repariert auf ihren Wunsch zweimal (Akku, Software), ohne Erfolg; er
bietet eine dritte Reparatur an, Undine will ein neues Handy (neu 450 €, Reparatur 60 € für ihn).
Danach: Ausgangslage (Verbrauchsgüterkauf, Mangel, § 477; Verweis Folge 063); 1. Wahlrecht § 439 Abs. 1 (Wortlautkarte;
BGH VIII ZR 66/17 LS 3a, Rn. 42 f., 47 f.); 2. Ort (§ 269; BGH VIII ZR 220/10 Rn. 29, 33; VIII ZR 278/16 Rn. 21);
3. § 439 Abs. 4 (Wortlautkarte; V ZR 275/12 Rn. 39; VIII ZR 66/17 LS 4c, Rn. 76; Verweis Folge 219); 4. § 440 S. 2
(Wortlautkarte); Verbraucher § 475d Abs. 1 Nr. 2 (Wortlautkarte; BT-Drs. 19/27424, S. 37), § 475 Abs. 4; Ergebnis;
Klausurtipp; Schema; Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/mitte/schild/
absatz_nb/requisit/stehend/paar/okw als eigene Kopie aus Folge 265 (gemeinsame Dateien unverändert); neu: theke(), regal(),
handy(), zaehler().
Darstellung: keine echten Handymarken (Tabler device-mobile ohne Logo), fiktiver Laden „Handyladen Stelzer“. Keine
Richterhämmer (Rechtsprechung als Waage).
Handlungsgeräusche: Kartenterminal, Schraubendreher (Freesound CC0, ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_268/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_268/" in n:
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
NAME = {"UN": "Undine", "ST": "Herr Stelzer"}
BLAU_P, LILA_P = (141, 179, 242, 255), (184, 169, 245, 255)
GRUEN_P, ROT_P = (143, 214, 148, 255), (240, 122, 106, 255)
NFARBE = {"UN": BLAU_P, "ST": LILA_P}


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


def sachverhalt_268(cue, absaetze, frage, size=34):
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






# --- eigene Szenenbausteine Folge 268 ----------------------------------------------------------------------------------------
def handy(cx, unten, breite, cue, fuell=None, bis=None, anim="pop", aus=False, d=0.0):
    """Das Smartphone: Tabler device-mobile (ohne Marke), ausgeschaltet: device-mobile-off."""
    return ficon("tabler", "device-mobile-off" if aus else "device-mobile", cx, unten, breite, cue,
                 fuell=fuell or (HELLGRAU if aus else BLAUHELL), bis=bis, anim=anim, d=d)


TX, TY, TW = 760, 640, 480                      # Theke im Handyladen (Oberkante TY, Unterkante BODEN)


def theke(cue):
    return [hart(feld(TX + 20, TY + 26, TW - 40, BODEN - TY - 26, cue, fill=HOLZ, rand=5, rund=10, name="theke")),
            hart(feld(TX, TY, TW, 32, cue, fill=DUNKELHOLZ, rand=5, rund=8, name="thekenplatte"))]


def regal(cue):
    """Wandregal hinter dem Verkäufer mit Ausstellungsgeräten (ohne Marken)."""
    els = []
    for y in (150, 270):
        els.append(hart(feld(1430, y, 440, 22, cue, fill=DUNKELHOLZ, rand=4, rund=6, name="regal")))
        for i, f in enumerate((BLAUHELL, LILAHELL, HELLGRUEN, GELB)):
            els.append(hart(ficon("tabler", "device-mobile", 1480 + i * 110, y + 4, 52, cue, fuell=f, anim="cut")))
    return els


def laden(cue):
    return [boden(cue), *schild("Handyladen Stelzer", 70, 40, cue, size=38, fill=BLAUHELL), *regal(cue), *theke(cue)]


UNX, STX = 470, 1540                            # Fallszene im Laden: Undine links (blickt nach rechts), Herr Stelzer rechts

# ===========================================================================================================================
# A Fall: Kauf im Handyladen (fall, kauf)
# ===========================================================================================================================
folie([(NULL, "Fall · Undine kauft ein neues Smartphone"), ("kauf", "Fall · bezahlt und mitgenommen")], [
    *laden(NULL),
    *fig("UN", UNX, BODEN, FH, [(NULL, "ruhig_r"), (beim("fall", "Smartphone"), "staunt_r"), ("kauf", "froh_r"),
                                (beim("kauf", "nimmt"), "strahlt_r")], erst="cut"),
    hart(ns(NAME["UN"], UNX, BODEN, NULL, NFARBE["UN"])),
    *fig("ST", STX, BODEN, FH, [(beim("fall", "Stelzer"), "froh"), ("kauf", "ruhig")], erst="pop"),
    ns(NAME["ST"], STX, BODEN, beim("fall", "Stelzer"), NFARBE["ST"], d=0.1),
    handy(900, TY + 4, 64, beim("fall", "Smartphone"), bis=beim("kauf", "nimmt")),
    pl("neues Smartphone", 900, 395, beim("fall", "Smartphone"), fill=WEISS, size=32, anker="m", bis="kauf"),
    pl("600 €", 900, 480, beim("fall", "sechshundert"), fill=GELB, size=36, anker="m", bis=beim("kauf", "nimmt")),
    szene(ficon("tabler", "credit-card", 1110, TY + 4, 92, beim("kauf", "bezahlt"), fuell=GELB, bis=beim("kauf", "nimmt")),
          "268kasse*", 0.7, 0.15),
    pl("bezahlt", 1110, 480, beim("kauf", "bezahlt"), fill=HELLGRUEN, size=32, anker="m", bis=beim("kauf", "nimmt")),
    bewegt(handy(UNX + 150, 650, 64, beim("kauf", "nimmt"), anim="cut"),
           beim("kauf", "nimmt"), beim("kauf", "mit", ende=True), 900 - (UNX + 150), TY + 4 - 650),
])

# ===========================================================================================================================
# B 3 Wochen später zu Hause: das Handy geht aus (aus1, zurueck)
# ===========================================================================================================================
UNB = 1180
folie([("aus1", "Fall · 3 Wochen später: Das Handy geht immer wieder aus"), ("zurueck", "Fall · zurück in den Laden")], [
    boden("aus1"),
    hart(pl("3 Wochen später", 70, 30, "aus1", fill=GELB, size=30)),
    *fenster(150, 150, 300, 230, "aus1"),
    hart(ficon("ph", "couch", 420, BODEN + 4, 380, "aus1", fuell=LILAHELL, nebenfarbe=LILAHELL)),
    hart(ficon("tabler", "lamp", 760, BODEN + 4, 120, "aus1", fuell=GELB)),
    hart(feld(UNB - 310, 700, 160, BODEN - 700, "aus1", fill=HOLZ, rand=5, rund=8, name="beistelltisch")),
    handy(UNB - 230, 700, 90, "aus1", anim="cut", bis=beim("aus1", "aus", nr=1)),
    handy(UNB - 230, 700, 90, beim("aus1", "aus", nr=1), aus=True, anim="cut", bis="zurueck"),
    pl("geht immer wieder von selbst aus", 800, 330, beim("aus1", "immer"), fill=HELLROT, size=32, anker="m",
       bis="zurueck"),
    *fig("UN", UNB, BODEN, FH, [("aus1", "ruhig"), (beim("aus1", "aus", nr=1), "staunt"), ("zurueck", "aerger_r")], erst="cut"),
    ns(NAME["UN"], UNB, BODEN, "aus1", NFARBE["UN"]),
    ficon("ph", "storefront", UNB + 330, 640, 170, "zurueck", fuell=BLAUHELL),
    pl("zurück in den Laden", UNB + 330, 400, beim("zurueck", "zurück"), fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# C Zurück im Laden: zwei Reparaturen, dann der Streit an der Theke und die Frage (u1 … frage2)
# ===========================================================================================================================
ZX, ZY = 70, 150                                # Reparaturzähler oben links unter dem Ladenschild


def zaehler_zeile(nr, text, y, cue, kreuz):
    return [pl(f"{nr}. Reparatur: {text}", ZX, y, cue, fill=WEISS, size=28),
            nein(ZX + F("Bold", 28).getlength(f"{nr}. Reparatur: {text}") + 110, y + 26, kreuz, gr=20)]


folie([("u1", "Fall · Undine: „Bitte reparieren Sie es.“"), ("rep1", "Fall · 1. Reparatur: Akku getauscht"),
       ("wieder1", "Fall · 1 Woche später: wieder aus"), ("rep2", "Fall · 2. Reparatur: Software neu aufgespielt"),
       ("wieder2", "Fall · wieder aus"), ("s1", "Fall · Herr Stelzer: „ein drittes Mal“"),
       ("u2", "Fall · Undine: „endlich ein neues Handy“"), ("s2", "Fall · Herr Stelzer: neu 450 €, Reparatur 60 €"),
       ("frage", "Die Frage · Reparatur oder neues Handy?"), ("frage2", "Die Frage · gleich zurücktreten?")], [
    *laden("u1"),
    # Undine (links, blickt nach rechts)
    *redet("UN_redet_r", UNX, BODEN, FH, "u1", "rep1"),
    *fig("UN", UNX, BODEN, FH, [("rep1", "ruhig_r"), ("wieder1", "sorge_r"), ("rep2", "denkt_r"), ("wieder2", "aerger_r"),
                                ("s1", "muede_r")], bis="u2", erst="cut"),
    *redet("UN_redet2_r", UNX, BODEN, FH, "u2", "s2"),
    *fig("UN", UNX, BODEN, FH, [("s2", "denkt_r"), ("frage", "ernst_r")], erst="cut"),
    ns(NAME["UN"], UNX, BODEN, "u1", NFARBE["UN"]),
    # Herr Stelzer (rechts, blickt nach links)
    *fig("ST", STX, BODEN, FH, [("u1", "ruhig"), ("rep1", "froh"), ("wieder1", "staunt"), ("rep2", "denkt"),
                                ("wieder2", "sorge")], bis="s1", erst="cut"),
    *redet("ST_redet", STX, BODEN, FH, "s1", "u2"),
    *fig("ST", STX, BODEN, FH, [("u2", "staunt")], bis="s2", erst="cut"),
    *redet("ST_redet2", STX, BODEN, FH, "s2", "frage"),
    *fig("ST", STX, BODEN, FH, [("frage", "ernst")], erst="cut"),
    ns(NAME["ST"], STX, BODEN, "u1", NFARBE["ST"]),
    # Handy auf der Theke
    handy(900, TY + 4, 64, "u1", aus=True, anim="cut", bis="rep1"),
    blase("sprech", 700, 220, "u1", 870, 300, inhalt=["Mein Handy geht ständig aus.", "Bitte reparieren Sie es."],
          textsize=34, figur=("UN_redet_r", UNX, BODEN, FH), bis="rep1"),
    # 1. Reparatur: Akku
    szene(ficon("tabler", "battery-2", 900, TY + 4, 90, "rep1", fuell=HELLGRUEN, bis="wieder1"), "268schrauben*", 0.6, 0.1),
    ficon("tabler", "tools", 1080, TY + 4, 90, "rep1", fuell=WEISS, bis="frage"),
    *zaehler_zeile(1, "Akku getauscht", ZY, "rep1", beim("wieder1", "wieder")),
    handy(900, TY + 4, 64, "wieder1", aus=True, anim="cut", bis="rep2"),
    pl("1 Woche später: wieder aus", 960, 470, beim("wieder1", "Woche"), fill=HELLROT, size=30, anker="m", bis="rep2"),
    # 2. Reparatur: Software
    ficon("tabler", "device-mobile-cog", 900, TY + 4, 80, "rep2", fuell=BLAUHELL, bis="wieder2"),
    *zaehler_zeile(2, "Software neu", ZY + 85, "rep2", beim("wieder2", "wieder")),
    handy(900, TY + 4, 64, "wieder2", aus=True, anim="cut"),
    pl("wieder aus", 960, 470, beim("wieder2", "wieder"), fill=HELLROT, size=30, anker="m", bis="s1"),
    # Streit
    blase("sprech", 640, 190, "s1", 1060, 300, inhalt=["Ich repariere es gern", "ein drittes Mal."], textsize=36,
          figur=("ST_redet", STX, BODEN, FH), bis="u2"),
    blase("sprech", 700, 220, "u2", 870, 300, inhalt=["Nein. Ich will jetzt", "endlich ein neues Handy."], textsize=36,
          figur=("UN_redet2_r", UNX, BODEN, FH), bis="s2"),
    blase("sprech", 720, 220, "s2", 1040, 300, inhalt=["Ein neues kostet mich 450 €.", "Eine Reparatur nur 60."],
          textsize=34, figur=("ST_redet2", STX, BODEN, FH), bis="frage"),
    pl("Wer entscheidet: Reparatur oder neues Handy?", 560, 300, "frage", fill=PINK, size=32),
    pl("Und gleich zurücktreten, ohne weitere Frist?", 560, 385, "frage2", fill=PINK, size=32),
])

# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
sachverhalt_268("sv", [
    "Undine kauft im August 2026 für sich privat im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. "
    "3 Wochen später schaltet es sich immer wieder von selbst aus. Undine bringt es in den Laden und bittet um eine "
    "Reparatur. Herr Stelzer tauscht den Akku; eine Woche später geht das Handy wieder aus. Bei der zweiten Reparatur "
    "spielt er die Software neu auf; wieder schaltet es sich ab. Die Ursache hat er nicht gefunden.",
    "Herr Stelzer bietet eine dritte Reparatur an. Undine will jetzt ein neues Handy. Ein neues kostet Herrn Stelzer "
    "450 €, eine Reparatur 60 €. Mangelfrei ist das Handy 600 € wert.",
], "Muss Herr Stelzer ein neues Handy liefern? Kann Undine gleich zurücktreten?", size=36)

# ===========================================================================================================================
# E Ausgangslage (lage … v063)
# ===========================================================================================================================
PL = "Ausgangslage"
folie([("lage", f"{PL} · Verbrauchsgüterkauf"), ("mang", f"{PL} › Sachmangel"),
       ("vermut", f"{PL} › Vermutung, § 477 Abs. 1 BGB"), ("v063", f"{PL} › Folge „Die Käuferrechte auf einen Blick“")], [
    *tafel("lage", "Ausgangslage"),
    z("Undine: Verbraucherin, § 13 BGB", 110, 180, "lage", "Bold", 34),
    z("Herr Stelzer: Unternehmer, § 14 BGB", 110, 235, beim("lage", "Unternehmer"), "Bold", 34),
    *okw("Verbrauchsgüterkauf, § 474 Abs. 1 BGB", 300, beim("lage", "Verbrauchsgüterkauf"), beim("lage", "Verbrauchsgüterkauf"),
         "ExtraBold", 34, x=160),
    *okw("Handy schaltet sich ständig aus: Sachmangel", 400, "mang", beim("mang", "mangelhaft"), "Bold", 34, x=160),
    zit("§ 434 Abs. 1, Abs. 3 S. 1 Nr. 1 BGB: gewöhnliche Verwendung", 160, 452, beim("mang", "mangelhaft")),
    z("Fehler im 1. Jahr nach der Übergabe:", 110, 530, "vermut", "Bold", 34),
    z("vermutet: schon bei Übergabe mangelhaft", 110, 582, beim("vermut", "vermutet"), "ExtraBold", 34),
    zit("§ 477 Abs. 1 S. 1 BGB", 110, 634, beim("vermut", "vermutet")),
    pl("Folge „§ 437 BGB: Die Käuferrechte auf einen Blick“", 110, 720, beim("v063", "Folge"), fill=LILAHELL, size=28),
    *requisit([("lage", ("ph", "storefront", 150, BLAUHELL), "Laden an Privatkundin", WEISS),
               ("mang", ("tabler", "device-mobile-off", 110, HELLGRAU), "geht ständig aus", HELLROT),
               ("vermut", ("tabler", "calendar", 110, WEISS), "1 Jahr", GELB)], px=1560, pu=330, py=90),
    *paar("UN", [("lage", "ruhig"), ("mang", "sorge"), ("vermut", "froh")], "ST", [("lage", "ruhig"), ("mang", "ernst")]),
])

# ===========================================================================================================================
# F 1. Wahlrecht, § 439 Abs. 1 BGB (Wortlautkarte) (p439 … neu)
# ===========================================================================================================================
PA = "A. Nacherfüllung"
w439, w439_y = wortlaut(80, 165, 1100, "„Der Käufer kann als Nacherfüllung nach seiner Wahl die Beseitigung des Mangels "
                                       "oder die Lieferung einer mangelfreien Sache verlangen.“", "§ 439 Abs. 1 BGB", "p439",
                        size=34, marken=[("Wahl", beim("p439", "Wahl")), ("Beseitigung", beim("p439", "Beseitigung")),
                                         ("Lieferung", beim("p439", "Lieferung"))])
folie([("p439", f"{PA} › 1. Wahlrecht, § 439 Abs. 1 BGB"), ("wahl", f"{PA} › 1. Die Wahl hat der Käufer"),
       ("erst", f"{PA} › 1. zuerst: Reparatur gewählt"), ("bind", f"{PA} › 1. an die Wahl gebunden? grundsätzlich nein"),
       ("treu", f"{PA} › 1. Grenze: Treu und Glauben"), ("fehl", f"{PA} › 1. Wechsel zur Lieferung erlaubt"),
       ("neu", f"{PA} › 1. neues Handy (+)")], [
    *tafel("p439", "1. Wahlrecht des Käufers"),
    *w439,
    *okz("Die Wahl hat der Käufer, nicht der Verkäufer", w439_y + 30, "wahl", "Bold", 34, x=160),
    z("Undine wählte zuerst: Reparatur", 110, w439_y + 100, "erst", "Bold", 34),
    *neinz("gebunden? grundsätzlich nicht", w439_y + 160, "bind", "ExtraBold", 34, x=160, kreuz=beim("bind", "grundsätzlich")),
    zit("BGH, Urt. v. 24.10.2018 – VIII ZR 66/17, Leitsatz 3a, Rn. 42 f.", 160, w439_y + 212, beim("bind", "Bundesgerichtshof")),
    z("Grenze: Treu und Glauben, § 242 BGB", 160, w439_y + 270, "treu", "Bold", 32),
    z("nicht fachgerecht beseitigt: Wechsel erlaubt", 160, w439_y + 325, beim("fehl", "nicht"), "Bold", 32),
    zit("VIII ZR 66/17, Rn. 47 f.", 160, w439_y + 377, beim("fehl", "wechseln")),
    *plusminus("Anspruch auf ein neues Handy", 110, w439_y + 430, beim("neu", "neues"), True, size=36, stil="ExtraBold"),
    *requisit([("p439", ("tabler", "arrows-exchange", 120, WEISS), "Reparatur oder neu?", WEISS),
               ("erst", ("tabler", "tools", 110, WEISS), "zuerst: Reparatur", GELB),
               ("fehl", ("tabler", "device-mobile-off", 100, HELLGRAU), "2-mal gescheitert", HELLROT),
               ("neu", ("tabler", "device-mobile-check", 100, HELLGRUEN), "jetzt: neues Handy", HELLGRUEN)]),
    *stehend("UN", FX, [("p439", "denkt"), ("wahl", "froh"), ("erst", "ruhig"), ("bind", "sorge"), ("fehl", "denkt"),
                        ("neu", "strahlt")]),
])
assert w439_y + 480 <= 895, w439_y

# ===========================================================================================================================
# G 2. Ort der Nacherfüllung (ort … kost)
# ===========================================================================================================================
folie([("ort", f"{PA} › 2. Ort der Nacherfüllung"), ("ort1", f"{PA} › 2. Ort: § 269 Abs. 1 BGB"),
       ("ort2", f"{PA} › 2. Kauf im Laden: beim Verkäufer"), ("ort3", f"{PA} › 2. Handy in den Laden bringen"),
       ("kost", f"{PA} › 2. Kosten: Verkäufer, § 439 Abs. 2 BGB")], [
    *tafel("ort", "2. Wo wird nacherfüllt?"),
    z("allgemeine Regel: § 269 Abs. 1 BGB", 110, 185, "ort1", "ExtraBold", 34),
    z("keine eigene Regel im Kaufrecht", 110, 240, beim("ort1", "allgemeine"), "Regular", 32),
    zit("BGH, Urt. v. 13.4.2011 – VIII ZR 220/10, Leitsatz 1, Rn. 29", 110, 290, beim("ort1", "Regel")),
    feld(110, 345, 1040, 200, "ort2", fill=BLAUHELL, rand=5, rund=18, anim="pop", name="ortfeld"),
    z("Geschäft des täglichen Lebens, Kauf im Laden:", 140, 362, beim("ort2", "Geschäften"), "Bold", 32),
    z("Ort regelmäßig beim Verkäufer", 140, 414, beim("ort2", "regelmäßig"), "ExtraBold", 34),
    zit("VIII ZR 220/10, Rn. 33; bestätigt: BGH, Urt. v. 19.7.2017 – VIII ZR 278/16, Rn. 21", 140, 470,
        beim("ort2", "Verkäufer")),
    *okz("Undine bringt das Handy in den Laden", 590, "ort3", "Bold", 34, x=160),
    z("Kosten trägt Herr Stelzer, § 439 Abs. 2 BGB", 160, 665, "kost", "ExtraBold", 34),
    z("Transport-, Wege-, Arbeits- und Materialkosten", 160, 718, beim("kost", "Paragraf"), "Regular", 30),
    *requisit([("ort", ("tabler", "map-pin", 100, PINK), "wo?", WEISS),
               ("ort2", ("ph", "storefront", 150, BLAUHELL), "Laden", BLAUHELL),
               ("kost", ("tabler", "coin-euro", 110, GELB), "Verkäufer zahlt", GELB)], px=1560, pu=330, py=90),
    *paar("UN", [("ort", "denkt"), ("ort3", "ruhig")], "ST", [("ort", "ruhig"), ("ort2", "froh"), ("kost", "ernst")]),
])

# ===========================================================================================================================
# H 3. Verweigerung, § 439 Abs. 4 BGB (Wortlautkarte) (p4 … abs)
# ===========================================================================================================================
w4, w4_y = wortlaut(80, 160, 1100, "„Der Verkäufer kann die vom Käufer gewählte Art der Nacherfüllung unbeschadet des § 275 "
                                   "Abs. 2 und 3 verweigern, wenn sie nur mit unverhältnismäßigen Kosten möglich ist. Dabei "
                                   "sind insbesondere der Wert der Sache in mangelfreiem Zustand, die Bedeutung des Mangels "
                                   "und die Frage zu berücksichtigen, ob auf die andere Art der Nacherfüllung ohne "
                                   "erhebliche Nachteile für den Käufer zurückgegriffen werden könnte. …“",
                    "§ 439 Abs. 4 S. 1, 2 BGB", "p4w", size=29,
                    marken=[("verweigern", beim("p4w", "verweigern")), ("unverhältnismäßigen", beim("p4w", "unverhältnismäßigen")),
                            ("Wert", beim("krit", "Wert")), ("Bedeutung", beim("krit", "Bedeutung")),
                            ("Nachteile", beim("krit", "Nachteile"))])
folie([("p4", f"{PA} › 3. Verweigerung, § 439 Abs. 4 BGB"), ("krit", f"{PA} › 3. Abwägung: Wert, Bedeutung, Nachteile"),
       ("rel", f"{PA} › 3. relative Unverhältnismäßigkeit"), ("abs", f"{PA} › 3. absolute Unverhältnismäßigkeit")], [
    *tafel("p4", "3. Darf Herr Stelzer verweigern?", size=44),
    *w4,
    feld(95, w4_y + 25, 515, 215, "rel", fill=HELLGRUEN, rand=5, rund=18, anim="pop", name="relativ"),
    z("relativ:", 120, w4_y + 40, "rel", "ExtraBold", 32, rechts=600),
    z("im Vergleich zur", 120, w4_y + 88, beim("rel", "Vergleich"), "Bold", 30, rechts=600),
    z("anderen Art zu teuer", 120, w4_y + 132, beim("rel", "teuer"), "Bold", 30, rechts=600),
    z("dann bleibt die andere Art", 120, w4_y + 180, beim("rel", "Dann"), "ExtraBold", 30, rechts=600),
    feld(640, w4_y + 25, 515, 215, "abs", fill=HELLROT, rand=5, rund=18, anim="pop", name="absolut"),
    z("absolut:", 665, w4_y + 40, "abs", "ExtraBold", 32, rechts=1145),
    z("schon für sich", 665, w4_y + 88, beim("abs", "schon"), "Bold", 30, rechts=1145),
    z("allein zu teuer", 665, w4_y + 132, beim("abs", "allein"), "Bold", 30, rechts=1145),
    zit("BGH, Urt. v. 4.4.2014 – V ZR 275/12, Rn. 39", 110, w4_y + 262, beim("abs", "teuer")),
    *requisit([("p4", ("tabler", "hand-stop", 110, WEISS), "verweigern?", WEISS),
               ("krit", ("ph", "scales", 130, WEISS), "abwägen", BLAUHELL)], px=1560, pu=330, py=90),
    *paar("UN", [("p4", "sorge"), ("krit", "denkt"), ("abs", "ernst")], "ST", [("p4", "denkt"), ("rel", "froh"), ("abs", "ruhig")]),
])
assert w4_y + 300 <= 900, w4_y

# ===========================================================================================================================
# I 3. Subsumtion: relativ und absolut (rsub … v219)
# ===========================================================================================================================
folie([("rsub", f"{PA} › 3. relativ: 450 € gegen 60 €"), ("bgh2", f"{PA} › 3. kein Verweis ohne nachhaltige Reparatur"),
       ("zwei", f"{PA} › 3. zwei Reparaturen gescheitert"), ("asub", f"{PA} › 3. absolut: 450 € bei Wert 600 €"),
       ("verw", f"{PA} › 3. Verweigerung (−)"), ("v219", f"{PA} › 3. Folge „Aus- und Einbaukosten § 439 III BGB“")], [
    *tafel("rsub", "3. Verweigerung im Fall"),
    z("relativ: neues Handy 450 € gegen Reparatur 60 €", 110, 180, "rsub", "Bold", 32),
    blk(110, 240, 1040, 200, BLAUHELL, "bgh2", [("Kein Verweis auf die Reparatur, wenn sie", "Bold", 31, INK),
                                               ("den Mangel nicht vollständig, nachhaltig", "ExtraBold", 31, INK),
                                               ("und fachgerecht beseitigt", "ExtraBold", 31, INK)]),
    zit("BGH, Urt. v. 24.10.2018 – VIII ZR 66/17, Leitsatz 4c, Rn. 76", 110, 452, beim("bgh2", "nachhaltig")),
    *neinz("2 Reparaturen gescheitert: kein 3. Versuch", 530, "zwei", "Bold", 34, x=160, kreuz=beim("zwei", "gescheitert")),
    z("absolut: 450 € bei Wert 600 €: nicht unverhältnismäßig", 110, 605, "asub", "Bold", 32),
    *plusminus("Verweigerung", 110, 670, beim("verw", "verweigern"), False, size=38, stil="ExtraBold"),
    pl("eingebaut? Folge „Aus- und Einbaukosten § 439 III BGB“", 110, 760, beim("v219", "eingebauten"), fill=LILAHELL,
       size=28),
    *requisit([("rsub", ("tabler", "calculator", 110, WEISS), "450 € : 60 €", GELB),
               ("zwei", ("tabler", "tools", 110, WEISS), "2-mal gescheitert", HELLROT),
               ("asub", ("tabler", "device-mobile", 90, BLAUHELL), "Wert 600 €", WEISS),
               ("verw", ("tabler", "device-mobile-check", 100, HELLGRUEN), "neues Handy", HELLGRUEN)]),
    *stehend("ST", FX, [("rsub", "froh"), ("bgh2", "staunt"), ("zwei", "sorge"), ("asub", "denkt"), ("verw", "ernst")]),
])

# ===========================================================================================================================
# J 4. Gleich zurücktreten? § 440 BGB (Wortlautkarte S. 2) (ruek … regel)
# ===========================================================================================================================
PB = "B. Rücktritt oder Minderung"
w440, w440_y = wortlaut(80, 370, 1100, "„Eine Nachbesserung gilt nach dem erfolglosen zweiten Versuch als fehlgeschlagen, "
                                       "wenn sich nicht insbesondere aus der Art der Sache oder des Mangels oder den "
                                       "sonstigen Umständen etwas anderes ergibt.“", "§ 440 S. 2 BGB", "p440s2", size=32,
                        marken=[("zweiten", beim("p440s2", "zweiten")), ("fehlgeschlagen", beim("p440s2", "fehlgeschlagen")),
                                ("anderes", beim("p440s2", "anderes"))])
folie([("ruek", f"{PB} · ohne weitere Frist?"), ("frist", f"{PB} › grundsätzlich: Frist zur Nacherfüllung"),
       ("p440", f"{PB} › § 440 S. 1 BGB: Fehlschlagen"), ("p440s2", f"{PB} › § 440 S. 2 BGB: nach dem 2. Versuch"),
       ("regel", f"{PB} › Regel, keine feste Grenze")], [
    *tafel("ruek", "4. Gleich zurücktreten oder mindern?", size=44),
    z("grundsätzlich: erfolglose Frist zur Nacherfüllung", 110, 180, "frist", "Bold", 32),
    zit("§ 323 Abs. 1, § 441 Abs. 1 S. 1 BGB", 110, 230, beim("frist", "Frist")),
    *okz("§ 440 S. 1 BGB: entbehrlich u. a. bei Fehlschlagen", 290, "p440", "Bold", 32, x=160),
    *w440,
    blk(110, w440_y + 25, 1040, 90, GELB, "regel", [("2 Versuche: eine Regel, keine feste Grenze", "ExtraBold", 32, INK)]),
    *requisit([("ruek", ("tabler", "arrow-back-up", 110, WEISS), "Geld zurück?", WEISS),
               ("frist", ("tabler", "hourglass", 100, GELB), "Frist", GELB),
               ("p440s2", ("tabler", "tools", 110, WEISS), "2 Versuche", HELLROT)], px=1560, pu=330, py=90),
    *paar("UN", [("ruek", "denkt"), ("p440", "froh"), ("regel", "denkt")], "ST", [("ruek", "sorge"), ("frist", "ruhig"),
                                                                                    ("p440s2", "sorge")]),
])
assert w440_y + 125 <= 895, w440_y

# ===========================================================================================================================
# K Beim Verbraucher: § 475d Abs. 1 Nr. 2 BGB (Wortlautkarte), § 475 Abs. 4 BGB (vgk … info)
# ===========================================================================================================================
w475d, w475d_y = wortlaut(80, 280, 1100, "„… bedarf es der in § 323 Absatz 1 bestimmten Fristsetzung zur Nacherfüllung "
                                         "abweichend von § 323 Absatz 2 und § 440 nicht, wenn … 2. sich trotz der vom "
                                         "Unternehmer versuchten Nacherfüllung ein Mangel zeigt, …“",
                          "§ 475d Abs. 1 Nr. 2 BGB", "p475d", size=30,
                          marken=[("trotz", beim("p475d", "trotz")), ("zeigt", beim("p475d", "zeigt"))])
folie([("vgk", f"{PB} › Verbraucher: § 475d statt § 440 BGB"), ("p475d", f"{PB} › § 475d Abs. 1 Nr. 2 BGB"),
       ("anz", f"{PB} › keine feste Zahl an Versuchen"), ("usub", f"{PB} › kein 3. Versuch nötig"),
       ("info", f"{PB} › Information vor der Nacherfüllung, § 475 Abs. 4 BGB")], [
    *tafel("vgk", "Beim Verbraucher: § 475d BGB"),
    z("Rücktritt: § 475d BGB statt § 440 BGB", 110, 185, beim("vgk", "Für"), "ExtraBold", 34),
    *w475d,
    z("keine feste Zahl an Versuchen: Einzelfall", 110, w475d_y + 22, "anz", "Bold", 32),
    zit("BT-Drs. 19/27424, S. 37 (Begründung)", 110, w475d_y + 72, beim("anz", "Einzelfall")),
    *okz("2 Reparaturen gescheitert: kein 3. Versuch nötig", w475d_y + 125, "usub", "Bold", 32, x=160),
    feld(95, w475d_y + 190, 1070, 165, "info", fill=HELLGRAU, rand=5, rund=18, anim="pop", name="info"),
    z("Käufe ab 31.7.2026: vor der Nacherfüllung informieren", 120, w475d_y + 205, beim("info", "Käufen"), "ExtraBold", 30),
    z("über das Wahlrecht und + 12 Monate Verjährung", 120, w475d_y + 253, beim("info", "Wahlrecht"), "Bold", 30),
    zit("bei Reparatur · § 475 Abs. 4, § 475e Abs. 5 BGB; Art. 229 § 72 EGBGB", 120, w475d_y + 302, beim("info", "Reparatur")),
    *requisit([("vgk", ("tabler", "user", 110, WEISS), "Verbraucherin", BLAUHELL),
               ("anz", ("ph", "scales", 130, WEISS), "Einzelfall", WEISS),
               ("info", ("tabler", "info-circle", 110, WEISS), "Pflicht zur Information", HELLGRAU)]),
    *stehend("UN", FX, [("vgk", "denkt"), ("p475d", "staunt"), ("usub", "froh"), ("info", "ruhig")]),
])
assert w475d_y + 360 <= 900, w475d_y

# ===========================================================================================================================
# L Ergebnis (erg … erg3)
# ===========================================================================================================================
PC = "C. Ergebnis"
folie([("erg", f"{PC} · neues Handy (+)"), ("erg2", f"{PC} › oder Rücktritt ohne weitere Frist"),
       ("erg3", f"{PC} › oder Minderung")], [
    *tafel("erg", "Ergebnis"),
    *plusminus("Undine: Anspruch auf ein neues Handy", 110, 190, beim("erg", "Undine"), True, size=36, stil="ExtraBold"),
    zit("§§ 437 Nr. 1, 439 Abs. 1 Alt. 2 BGB", 110, 245, beim("erg", "neues")),
    z("oder: Rücktritt ohne weitere Frist", 110, 330, "erg2", "ExtraBold", 34),
    *okz("Mangel erheblich, § 323 Abs. 5 S. 2 BGB", 400, beim("erg2", "Mangel"), "Bold", 32, x=160),
    z("Handy zurück gegen den Kaufpreis, Zug um Zug", 160, 465, beim("erg2", "Dann"), "Bold", 32),
    zit("§§ 437 Nr. 2, 323 Abs. 1, 475d Abs. 1 Nr. 2, 346, 348 BGB", 160, 515, beim("erg2", "Zug")),
    z("oder: Minderung des Kaufpreises", 110, 600, "erg3", "ExtraBold", 34),
    zit("§§ 437 Nr. 2, 441 BGB", 110, 652, beim("erg3", "mindert")),
    *requisit([("erg", ("tabler", "device-mobile-check", 100, HELLGRUEN), "neues Handy", HELLGRUEN),
               ("erg2", ("tabler", "arrow-back-up", 110, WEISS), "Rücktritt", WEISS),
               ("erg3", ("tabler", "discount", 110, GELB), "Minderung", GELB)], px=1560, pu=330, py=90),
    *paar("UN", [("erg", "strahlt"), ("erg2", "froh"), ("erg3", "denkt")], "ST", [("erg", "sorge"), ("erg2", "ernst")]),
])

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zwei Ebenen trennen"), ("tipp2", "Klausurtipp · Rücktritt und Minderung: Frist entbehrlich?"),
       ("tipp3", "Klausurtipp · Verbrauchsgüterkauf: § 475d BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zwei Ebenen trennen:", 200, 200, "tipp", "Bold", 34),
    z("1. Anspruch auf Nacherfüllung", 200, 270, beim("tipp", "Erst"), "ExtraBold", 34),
    z("Wahlrecht · Ort · Einrede aus Abs. 4", 240, 325, beim("tipp", "Wahlrecht"), "Bold", 32),
    z("Einrede: Der Verkäufer muss sie erheben", 240, 378, beim("tipp", "erheben", ende=False), "Regular", 30),
    zit("BGH, Urt. v. 24.10.2018 – VIII ZR 66/17, Rn. 57", 240, 425, beim("tipp", "erheben")),
    linienzug([(130, 485), (1130, 485)], "tipp2", breite=3),
    z("2. Rücktritt und Minderung", 200, 515, "tipp2", "ExtraBold", 34),
    z("Ist die Frist entbehrlich?", 240, 570, beim("tipp2", "Ist"), "Bold", 32),
    z("Verbrauchsgüterkauf: § 475d BGB", 240, 640, "tipp3", "ExtraBold", 34),
    z("sonst: §§ 323 Abs. 2, 440 BGB", 240, 695, beim("tipp3", "Paragraf"), "Regular", 30),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Prüfungsschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Kaufvertrag und Sachmangel bei Gefahrübergang (§ 477 BGB)", True),
          ("k2", 0, "II. Wahl der Lieferung, § 439 Abs. 1 BGB; Wechsel erlaubt", True),
          ("k3", 0, "III. Nacherfüllungsverlangen am richtigen Ort: im Laden, § 269 BGB", True),
          ("k4", 0, "IV. keine Verweigerung, § 439 Abs. 4 BGB", True),
          ("k5", 0, "V. Ergebnis: Anspruch auf ein neues Handy", True),
          ("k6", 1, "Alternativ: Rücktritt ohne weitere Frist, § 475d Abs. 1 Nr. 2 BGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Undine gegen Herrn Stelzer"), 110, 90, "sch", 44),
           z("Lieferung eines neuen Handys, §§ 437 Nr. 1, 439 Abs. 1 BGB", 110, 158, beim("sch", "Lieferung"), "Bold", 36,
             rechts=1800)]
y = 270
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Bold", 40 if ebene == 0 else 36, rechts=1820))
    y += 105
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("k1", "Prüfungsschema › I. Sachmangel"), ("k2", "Prüfungsschema › II. Wahl der Lieferung"),
       ("k3", "Prüfungsschema › III. Ort"), ("k4", "Prüfungsschema › IV. keine Verweigerung"),
       ("k5", "Prüfungsschema › V. Ergebnis"), ("k6", "Prüfungsschema › alternativ: Rücktritt")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei der Nacherfüllung ", 0), ("wählt der Käufer.", "a")],
                 [("Der Verkäufer kann nur ausnahmsweise", 0)],
                 [("verweigern, vor allem bei", 0)], [("unverhältnismäßigen Kosten.", "b")]],
                750, 260, 42, "merke", {"a": beim("merke", "wählt"), "b": beim("merke", "unverhältnismäßigen")}),
    *markertext([[("Nach ", 0), ("zwei", "c"), (" gescheiterten Versuchen gilt die", 0)],
                 [("Nachbesserung in der Regel als", 0)], [("fehlgeschlagen,", 0)],
                 [("beim Verbraucher entscheidet der ", 0), ("Einzelfall.", "d")]],
                750, 550, 42, "merk2", {"c": beim("merk2", "zwei"), "d": beim("merk2", "Einzelfall")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
