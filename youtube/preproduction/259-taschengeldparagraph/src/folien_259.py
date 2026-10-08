"""Folge 259 · Taschengeldparagraph: Darf ein 16-Jähriger auf Raten kaufen? · Serienstandard Open Peeps (Katzenkönig).
Fall: Fridolin (16) kauft im (fiktiven) Radladen von Herrn Heinemann ein gebrauchtes E-Bike für 900 €, zahlt 300 € aus
gespartem Taschengeld (zur freien Verfügung) an, den Rest von 600 € in 6 Monatsraten zu je 100 € aus künftigem
Taschengeld; die Eltern fragt er nicht, das E-Bike nimmt er gleich mit. Abends die Mutter im Flur, am nächsten Tag ihr
Anruf: „Diesen Ratenkauf genehmigen wir nicht.“ Danach: Anspruch § 433 Abs. 2, I. Einigung, II. Wirksamkeit (§ 106;
Wortlautkarten § 107, § 108 Abs. 1, § 110; „bewirkt“ = vollständig erbracht, § 362 Abs. 1; Ratenkauf erst mit der letzten
Rate und keine Kreditgeschäfte – als herrschende Lehre gekennzeichnet; Genehmigung/Verweigerung, § 184, Aufforderung § 108
Abs. 2), Ergebnis mit Rückabwicklung (§ 812, Verweis Folge 245), Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/fenster als
eigene Kopie aus Folge 255 (gemeinsame Dateien unverändert); neu: mitte(), schild(), ebike(), leiste(), raten_x(), flur().
Keine echten Marken: Laden, E-Bike und Werkzeug aus Grundformen und Tabler-Icons, ohne Logo.
Handlungsgeräusche: Geldschein (Anzahlung), Freilauf (Fridolin fährt los), Telefon (Anruf der Mutter);
../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_259/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_259/" in n:
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
NAME = {"FR": "Fridolin", "HN": "Herr Heinemann", "MU": "Mutter"}
BLAU_P, LILA_P = (141, 179, 242, 255), (184, 169, 245, 255)
NFARBE = {"FR": (143, 214, 148, 255), "HN": BLAU_P, "MU": LILA_P}
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


def mitte(text, cx, y, cue, stil="Bold", size=34, **k):
    """Zentrierte Zeile (Felder, Schilder)."""
    return z(text, cx - F(stil, size).getlength(glyphen(text)) / 2, y, cue, stil, size, rechts=k.pop("rechts", 1880), **k)


def schild(text, x, y, cue, w=None, size=38, fill=GELB, bis=None):
    """Ladenschild (Grundform, fiktiver Laden, kein Logo)."""
    w = w or int(F("ExtraBold", size).getlength(glyphen(text))) + 60
    return [bis_(hart(feld(x, y, w, int(size * 1.9), cue, fill=fill, rand=5, rund=12, name="schild")), bis),
            bis_(hart(mitte(text, x + w / 2 + 6, y + size * 0.42, cue, "ExtraBold", size)), bis)]


def ebike(cx, unten, breite, cue, bis=None, anim="cut"):
    """E-Bike: Phosphor bicycle mit Akku-Symbol (Tabler battery-charging)."""
    return [ficon("ph", "bicycle", cx, unten, breite, cue, fuell=WEISS, bis=bis, anim=anim),
            ficon("tabler", "battery-charging", cx, unten - breite * 0.6, breite * 0.24, cue, fuell=GRUEN_P,
                  bis=bis, anim=anim)]


RW, RH, RG = 120, 84, 8                    # Ratenleiste: Feldbreite (je 100 €), Höhe, Abstand


def leiste(x, y, cue, raten_cue, bezahlt=1, bis=None, anz_w=200, gruen_ab=None, size=30):
    """Ratenleiste: Anzahlung 300 € (grün = bezahlt) und 6 Monatsraten zu je 100 € (weiß = offen).
    bezahlt = Anzahl grüner Raten; gruen_ab = [(nr, cue)] färbt Rate nr ab cue grün."""
    els = [feld(x, y, anz_w, RH, cue, fill=GRUEN_P, rand=4, rund=12, anim="pop", name="anz"),
           mitte("300 €", x + anz_w / 2 + 6, y + (RH - 36 * 1.3) / 2 + 10, cue, "ExtraBold", 36, bis=bis)]
    els[0].bis = bis
    umf = dict(gruen_ab or [])
    for i in range(6):
        rx = x + anz_w + RG + i * (RW + RG)
        if i + 1 in umf:
            els.append(feld(rx, y, RW, RH, raten_cue, fill=WEISS, rand=4, rund=12, anim="pop", bis=umf[i + 1],
                            name=f"rate{i + 1}"))
            els.append(feld(rx, y, RW, RH, umf[i + 1], fill=GRUEN_P, rand=4, rund=12, anim="cut", bis=bis, name=f"rate{i + 1}g"))
        else:
            els.append(feld(rx, y, RW, RH, raten_cue, fill=GRUEN_P if i < bezahlt - 1 else WEISS, rand=4, rund=12, anim="pop",
                            bis=bis, name=f"rate{i + 1}"))
        els.append(mitte("100 €", rx + RW / 2 + 6, y + (RH - size * 1.3) / 2 + 10, raten_cue, "Bold", size, bis=bis))
    return els, x + anz_w + RG + 6 * (RW + RG)


def raten_x(x, nr, anz_w=200):
    """Mitte der Rate nr (1–6) in der Leiste."""
    return x + anz_w + RG + (nr - 1) * (RW + RG) + RW / 2 + 6


# ===========================================================================================================================
# A Fall: im Radladen von Herrn Heinemann (fall … mit)
# ===========================================================================================================================
FRX, BIKX, HNX = 560, 1010, 1520            # Fridolin, E-Bike, Herr Heinemann
LX0, LY = 300, 150                          # Ratenleiste im Laden
LD = [*schild("Radladen Heinemann", 70, 40, NULL),
      hart(linienzug([(70, 560), (420, 560)], NULL, breite=6, farbe=INK)),            # Wandhalter
      ficon("ph", "bicycle", 245, 552, 300, NULL, fuell=WEISS, anim="cut"),
      ficon("ph", "bicycle", 245, BODEN + 6, 300, NULL, fuell=HELLGRAU, anim="cut"),
      ficon("tabler", "tool", 1820, 330, 100, NULL, fuell=WEISS, anim="cut")]
leiste_a, _lx1 = leiste(LX0, LY, "anz", beim("raten", "sechs"))
folie([(NULL, "Fall · Im Radladen"), ("h1", "Fall · Herr Heinemann: 300 € jetzt, Rest in Raten"),
       ("anz", "Fall · Anzahlung: 300 € aus Taschengeld"), ("raten", "Fall · Rest: 6 Monatsraten zu je 100 €"),
       ("frei", "Fall · Taschengeld zur freien Verfügung"), ("nicht", "Fall · Eltern nicht gefragt"),
       ("mit", "Fall · Fridolin nimmt das E-Bike mit")], [
    boden(NULL), *LD,
    # Fridolin (steht links, blickt nach rechts zum Rad und zu Herrn Heinemann)
    *fig("FR", FRX, BODEN, FH, [(NULL, "ruhig_r"), (beim("fall", "unbedingt"), "strahlt_r"), ("fridolin", "froh_r"),
                                ("laden", "staunt_r"),
                                ("angebot", "froh_r"), ("h1", "denkt_r"), ("anz", "froh_r"), ("frei", "ruhig_r"),
                                ("nicht", "sorge_r")], bis=beim("mit", "gibt"), erst="cut"),
    hart(bis_(ns(NAME["FR"], FRX, BODEN, NULL, NFARBE["FR"]), beim("mit", "gibt"))),
    pl("16 Jahre", FRX, 330, beim("fall", "sechzehn"), fill=WEISS, size=32, anker="m", bis="laden"),
    pl("Wunsch: ein E-Bike", FRX + 330, 250, beim("fall", "E-Bike"), fill=GELB, size=30, anker="m", bis="laden"),
    # Herr Heinemann und das E-Bike
    *ebike(BIKX, BODEN + 6, 380, beim("laden", "gebrauchtes"), bis=beim("mit", "gibt"), anim="pop"),
    pl("gebraucht", BIKX, 470, beim("laden", "gebrauchtes"), fill=WEISS, size=30, anker="m", bis="h1"),
    pl("900 €", BIKX, 390, beim("laden", "neunhundert"), fill=GELB, size=40, anker="m", bis="anz"),
    *fig("HN", HNX, BODEN, FH, [(beim("laden", "Herrn"), "ruhig"), ("angebot", "froh")], bis="h1", erst="pop"),
    *redet("HN_redet", HNX, BODEN, FH, "h1", "anz"),
    *fig("HN", HNX, BODEN, FH, [("anz", "froh"), ("nicht", "ruhig"), ("mit", "froh")], erst="cut"),
    ns(NAME["HN"], HNX, BODEN, beim("laden", "Herrn"), NFARBE["HN"], d=0.1),
    blase("sprech", 700, 230, "h1", 1180, 250, inhalt=["300 € jetzt, den Rest in", "6 Monatsraten zu je 100 €."],
          textsize=34, figur=("HN_redet", HNX, BODEN, FH), bis="anz"),
    # Anzahlung: der Geldschein wandert von Fridolin zu Herrn Heinemann
    szene(bewegt(ficon("tabler", "cash-banknote", FRX + 120, 700, 100, beim("anz", "zahlt"), fuell=GRUEN_P, bis="raten"),
                 beim("anz", "zahlt"), beim("anz", "dreihundert", ende=True), HNX - 150 - (FRX + 120), 0),
          "259geld*", 0.9, 0.0),
    pl("aus gespartem Taschengeld", FRX, 330, beim("anz", "Taschengeld"), fill=WEISS, size=28, anker="m", bis="raten"),
    *leiste_a,
    z("Anzahlung", LX0 + 30, LY + RH + 18, "anz", "Bold", 28),
    z("6 Monatsraten aus künftigem Taschengeld", LX0 + 250, LY + RH + 18, beim("raten", "künftigen"), "Bold", 28,
      rechts=1700),
    ficon("tabler", "pig-money", 850, 400, 100, "frei", fuell=HELLROT, bis="mit"),
    pl("Taschengeld: zur freien Verfügung", 920, 330, "frei", fill=HELLGRUEN, size=28, bis="mit"),
    ficon("tabler", "users", 850, 530, 90, "nicht", fuell=WEISS, bis="mit"),
    *[bis_(e, "mit") for e in neinz("Eltern nicht gefragt", 462, beim("nicht", "Gefragt"), "ExtraBold", 32, x=960,
                                    rechts=1400)],
    # Herr Heinemann gibt das E-Bike mit: Fridolin fährt los
    szene(peep_voll("FR_rad_r", 800, BODEN + 4, 420, beim("mit", "gibt"), anim="pop"), "259rad*", 0.8, 0.1),
    ns(NAME["FR"], 760, BODEN + 4, beim("mit", "gibt"), NFARBE["FR"], d=0.1),
    pl("E-Bike", 800, 330, beim("mit", "E-Bike"), fill=LILAHELL, size=30, anker="m"),
    ficon("tabler", "battery-charging", 905, 372, 64, beim("mit", "E-Bike"), fuell=GRUEN_P),
])

# ===========================================================================================================================
# B Am Abend im Flur: die Mutter
# ===========================================================================================================================
MUX, BIKB, FRB = 520, 1020, 1480


def flur(cue):
    return [boden(cue),
            hart(feld(1700, 300, 170, BODEN - 304, cue, fill=HOLZ, rand=5, rund=8, name="haustuer")),
            hart(feld(1720, 560, 20, 20, cue, fill=GELB, rand=3, rund=10, name="knauf")),
            ficon("tabler", "hanger", 130, 330, 110, cue, fuell=WEISS, anim="cut"),
            ficon("tabler", "lamp", 1000, 230, 120, cue, fuell=GELB, anim="cut")]


folie([("abend", "Fall · Am Abend im Flur"), ("m1", "Fall · Mutter: „Das hättest du mit uns besprechen müssen“")], [
    *flur("abend"),
    hart(pl("Am Abend", 70, 30, "abend", fill=GELB, size=30)),
    *ebike(BIKB, BODEN + 6, 360, "abend"),
    *fig("MU", MUX, BODEN, FH, [("abend", "ruhig_r"), (beim("abend", "E-Bike"), "staunt_r")], bis="m1", erst="pop"),
    *redet("MU_redet_r", MUX, BODEN, FH, "m1", "anruf"),
    hart(ns(NAME["MU"], MUX, BODEN, "abend", NFARBE["MU"])),
    *fig("FR", FRB, BODEN, FH, [("abend", "froh"), ("m1", "sorge")], erst="pop"),
    hart(ns(NAME["FR"], FRB, BODEN, "abend", NFARBE["FR"])),
    blase("sprech", 720, 230, "m1", 870, 250, inhalt=["Ein E-Bike auf Raten? Das", "hättest du mit uns", "besprechen müssen."],
          textsize=33, figur=("MU_redet_r", MUX, BODEN, FH)),
])

# ===========================================================================================================================
# C Am nächsten Tag: Anruf im Radladen – die Frage
# ===========================================================================================================================
TRENN = 960
MUC, FRC, HNC = 300, 700, 1560
folie([("anruf", "Fall · Am nächsten Tag: Anruf im Radladen"), ("m2", "Fall · Mutter: „Wir genehmigen nicht“"),
       ("frage", "Die Frage · Muss Fridolin 600 € zahlen?"), ("frage2", "Die Frage · Hilft der Taschengeldparagraf?")], [
    boden("anruf"),
    hart(linienzug([(TRENN, 300), (TRENN, BODEN)], "anruf", breite=6, farbe=INK)),
    hart(pl("Am nächsten Tag", 70, 30, "anruf", fill=GELB, size=30, bis="frage")),
    *schild("Radladen Heinemann", 1040, 30, "anruf", size=34, bis="frage"),
    ficon("ph", "bicycle", 1200, BODEN + 6, 280, "anruf", fuell=WEISS, anim="cut"),
    ficon("tabler", "phone", MUC + 150, 560, 70, beim("anruf", "ruft"), fuell=WEISS),
    szene(ficon("tabler", "phone-ringing", HNC - 190, 560, 80, beim("anruf", "Herrn"), fuell=GELB, bis="m2"), "259telefon*", 0.7, 0.05),
    ficon("tabler", "phone", HNC - 190, 560, 70, "m2", fuell=WEISS, anim="cut"),
    *fig("MU", MUC, BODEN, FH, [("anruf", "ernst_r")], bis="m2", erst="pop"),
    *redet("MU_redet_r", MUC, BODEN, FH, "m2", "frage"),
    *fig("MU", MUC, BODEN, FH, [("frage", "ernst_r")], erst="cut"),
    ns(NAME["MU"], MUC, BODEN, "anruf", NFARBE["MU"], d=0.1),
    *fig("FR", FRC, BODEN, FH, [("anruf", "sorge"), ("frage2", "denkt")], erst="pop"),
    ns(NAME["FR"], FRC, BODEN, "anruf", NFARBE["FR"], d=0.1),
    *fig("HN", HNC, BODEN, FH, [("anruf", "ruhig"), ("m2", "sorge"), ("frage", "denkt")], erst="pop"),
    ns(NAME["HN"], HNC, BODEN, "anruf", NFARBE["HN"], d=0.1),
    blase("sprech", 560, 190, "m2", 560, 300, inhalt=["Diesen Ratenkauf", "genehmigen wir nicht."], textsize=34,
          figur=("MU_redet_r", MUC, BODEN, FH), bis="frage"),
    pl("Muss Fridolin die restlichen 600 € zahlen?", 300, 140, "frage", fill=PINK, size=36),
    pl("Oder rettet ihn der Taschengeldparagraf?", 300, 225, "frage2", fill=PINK, size=36),
])

# ===========================================================================================================================
# D Sachverhalt
# ===========================================================================================================================
def sachverhalt_259(cue, absaetze, frage, size=34):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_259("sv", [
    "Der 16-jährige Fridolin kauft im Radladen von Herrn Heinemann ein gebrauchtes E-Bike für 900 €. Er zahlt 300 € "
    "sofort aus gespartem Taschengeld an, das ihm die Eltern zur freien Verfügung geben. Die übrigen 600 € soll er in "
    "6 Monatsraten zu je 100 € aus seinem künftigen Taschengeld zahlen. Die Eltern hat er nicht gefragt. Herr Heinemann "
    "gibt ihm das E-Bike gleich mit.",
    "Am nächsten Tag ruft die Mutter, auch für den Vater, bei Herrn Heinemann an: „Diesen Ratenkauf genehmigen wir "
    "nicht.“",
], "Muss Fridolin die restlichen 600 € zahlen?")


# ===========================================================================================================================
# Tafel-Helfer
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
# E Anspruch, I. Einigung, II. Wirksamkeit: § 106
# ===========================================================================================================================
folie([("ansp", "Anspruch · § 433 Abs. 2 BGB: restliche 600 €"), ("einig", "I. Einigung"),
       ("wirk", "II. Wirksamkeit · beschränkt geschäftsfähig, § 106 BGB"),
       ("v021", "II. Wirksamkeit › Grundschema: Folge „Minderjährige im Vertragsrecht“")], [
    *tafel("ansp", "Anspruch auf die Raten"),
    z("Herr Heinemann gegen Fridolin", 110, 180, "ansp", "Bold", 36),
    z("restliche 600 € Kaufpreis", 110, 240, beim("ansp", "sechshundert"), "Bold", 34),
    z("§ 433 Abs. 2 BGB", 110, 292, beim("ansp", "Paragraf"), "ExtraBold", 36),
    *okw("I. Einigung", 380, "einig", beim("einig", "Einig"), "ExtraBold", 36, x=160),
    z("II. Wirksamkeit?", 160, 460, "wirk", "ExtraBold", 36),
    z("Fridolin, 16: beschränkt geschäftsfähig", 185, 520, beim("wirk", "Fridolin"), "Bold", 34),
    zit("§ 106 BGB", 185, 570, beim("wirk", "Paragraf")),
    blk(110, 650, 1040, 150, LILAHELL, "v021", [("Grundschema: Folge", "ExtraBold", 31, INK),
                                               ("„Minderjährige im Vertragsrecht“", "ExtraBold", 31, INK),
                                               ("hier: der Ratenkauf", "Bold", 31, INK)]),
    *requisit([("ansp", ("tabler", "receipt", 120, WEISS), "600 € offen", GELB),
               ("einig", ("ph", "bicycle", 170, LILA_P), "Kaufvertrag", WEISS),
               ("wirk", ("tabler", "school", 120, WEISS), "16 Jahre", WEISS)], px=1560, pu=330, py=90),
    *paar("HN", [("ansp", "ruhig"), ("einig", "froh"), ("wirk", "denkt")], "FR", [("ansp", "sorge"), ("einig", "ruhig"),
                                                                              ("v021", "denkt")]),
])

# ===========================================================================================================================
# F § 107 BGB (Wortlautkarte): nicht lediglich rechtlich vorteilhaft, keine Einwilligung
# ===========================================================================================================================
PW = "II. Wirksamkeit"
w107, w107_y = wortlaut(80, 170, 1100, "„Der Minderjährige bedarf zu einer Willenserklärung, durch die er nicht lediglich "
                                       "einen rechtlichen Vorteil erlangt, der Einwilligung seines gesetzlichen Vertreters.“",
                        "§ 107 BGB", "p107", size=34,
                        marken=[("nicht lediglich", beim("p107", "nicht")), ("Einwilligung", beim("p107", "Einwilligung"))])
folie([("p107", f"{PW} › lediglich rechtlicher Vorteil? § 107 BGB"), ("pflicht", f"{PW} › Zahlungspflicht: rechtlicher Nachteil"),
       ("keine", f"{PW} › keine Einwilligung der Eltern")], [
    *tafel("p107", "Braucht Fridolin die Eltern?"),
    *w107,
    z("Ratenkauf: Pflicht, 900 € zu zahlen", 110, w107_y + 40, "pflicht", "Bold", 34),
    *plusminus("rechtlicher Nachteil", 110, w107_y + 100, beim("pflicht", "Nachteil"), False, size=34, stil="ExtraBold"),
    *neinz("Einwilligung der Eltern: keine", w107_y + 180, "keine", "Bold", 34, kreuz=beim("keine", "nicht")),
    *requisit([("p107", ("tabler", "users", 120, WEISS), "Eltern", WEISS),
               ("pflicht", ("tabler", "receipt", 110, WEISS), "Pflicht: 900 €", HELLROT),
               ("keine", ("tabler", "user-x", 110, WEISS), "nicht gefragt", PINK)]),
    *stehend("FR", FX, [("p107", "ruhig"), ("pflicht", "sorge"), ("keine", "ernst")]),
])
assert w107_y + 180 + 40 <= 895, w107_y

# ===========================================================================================================================
# G § 108 Abs. 1 BGB (Wortlautkarte): schwebend unwirksam
# ===========================================================================================================================
w108, w108_y = wortlaut(80, 170, 1100, "„(1) Schließt der Minderjährige einen Vertrag ohne die erforderliche Einwilligung des "
                                       "gesetzlichen Vertreters, so hängt die Wirksamkeit des Vertrags von der Genehmigung "
                                       "des Vertreters ab.“", "§ 108 Abs. 1 BGB", "p108", size=34,
                        marken=[("ohne die erforderliche", beim("p108", "ohne")), ("Genehmigung", beim("p108", "Genehmigung"))])
folie([("p108", f"{PW} › Genehmigung, § 108 Abs. 1 BGB"), ("schwebe", f"{PW} › schwebend unwirksam")], [
    *tafel("p108", "Ohne Einwilligung: Genehmigung"),
    *w108,
    blk(110, w108_y + 40, 1040, 100, GELB, "schwebe", [("bis dahin: schwebend unwirksam", "ExtraBold", 36, INK)]),
    *requisit([("p108", ("tabler", "file-text", 110, WEISS), "Genehmigung?", WEISS),
               ("schwebe", ("tabler", "hourglass", 110, GELB), "in der Schwebe", GELB)], px=1560, pu=330, py=90),
    *paar("MU", [("p108", "denkt"), ("schwebe", "ernst")], "FR", [("p108", "ruhig"), ("schwebe", "sorge")]),
])

# ===========================================================================================================================
# H § 110 BGB (Wortlautkarte): der Taschengeldparagraf
# ===========================================================================================================================
w110, w110_y = wortlaut(80, 245, 1100, "„Ein von dem Minderjährigen ohne Zustimmung des gesetzlichen Vertreters geschlossener "
                                       "Vertrag gilt als von Anfang an wirksam, wenn der Minderjährige die vertragsmäßige "
                                       "Leistung mit Mitteln bewirkt, die ihm zu diesem Zweck oder zu freier Verfügung … "
                                       "überlassen worden sind.“", "§ 110 BGB", "p110w", size=32,
                        marken=[("von Anfang an wirksam", beim("p110w", "Anfang")), ("bewirkt", beim("p110w", "bewirkt")),
                                ("zu freier Verfügung", beim("p110w", "freier"))])
PT = "§ 110 BGB"
folie([("p110", "Taschengeldparagraf · § 110 BGB"), ("p110w", f"{PT} › Leistung mit überlassenen Mitteln bewirkt?"),
       ("mittel", f"{PT} › Mittel: Taschengeld zur freien Verfügung")], [
    *tafel("p110", "Der Taschengeldparagraf"),
    z("Wirksam ohne Genehmigung?", 110, 175, "p110", "Bold", 34),
    *w110,
    *okw("Taschengeld: zur freien Verfügung", w110_y + 40, "mittel", beim("mittel", "passt"), "Bold", 34),
    *requisit([("p110", ("tabler", "pig-money", 130, HELLROT), "Taschengeld", HELLGRUEN),
               ("mittel", ("tabler", "pig-money", 130, HELLROT), "freie Verfügung", HELLGRUEN)]),
    *stehend("FR", FX, [("p110", "denkt"), ("mittel", "froh")]),
])
assert w110_y + 40 + 50 <= 895, w110_y

# ===========================================================================================================================
# I „bewirkt“ = vollständig erbracht (§ 362 Abs. 1); erst 300 von 900 €; nicht teilweise wirksam
# ===========================================================================================================================
LIX, LIY = 110, 440
leiste_i, _ = leiste(LIX, LIY, beim("anz2", "dreihundert"), beim("anz2", "neunhundert"))
folie([("bewirkt", f"{PT} › „bewirkt“"), ("erfuell", f"{PT} › bewirkt = vollständig erbracht"),
       ("anz2", f"{PT} › erst 300 von 900 € gezahlt"), ("teil", f"{PT} › Anzahlung: nicht teilweise wirksam")], [
    *tafel("bewirkt", "Was heißt „bewirkt“?"),
    z("„bewirkt“", 110, 180, "bewirkt", "ExtraBold", 40),
    z("= die Leistung vollständig erbracht", 110, 250, beim("erfuell", "vollständig"), "Bold", 34),
    zit("wie bei der Erfüllung, § 362 Abs. 1 BGB", 110, 302, beim("erfuell", "Erfüllung")),
    *leiste_i,
    z("bezahlt", LIX + 50, LIY + RH + 20, beim("anz2", "dreihundert"), "Bold", 28),
    z("offen: 600 €", LIX + 420, LIY + RH + 20, beim("anz2", "neunhundert"), "Bold", 28),
    pl("erst 300 von 900 €", 110, 360, beim("anz2", "dreihundert"), fill=HELLROT, size=32),
    *neinz("Anzahlung: nicht teilweise wirksam", 680, "teil", "Bold", 34, kreuz=beim("teil", "nicht")),
    *requisit([("bewirkt", ("tabler", "list-check", 120, WEISS), "bewirkt?", WEISS),
               ("anz2", ("tabler", "cash-banknote", 120, GRUEN_P), "300 € von 900 €", HELLROT)], px=1560, pu=330, py=90),
    *paar("HN", [("bewirkt", "ruhig"), ("anz2", "denkt")], "FR", [("bewirkt", "denkt"), ("anz2", "sorge"), ("teil", "ernst")]),
])

# ===========================================================================================================================
# K Ratenkauf: erst mit der letzten Rate (herrschende Lehre); Kreditgeschäfte nicht gedeckt
# ===========================================================================================================================
LKX, LKY = 110, 300
leiste_k, _ = leiste(LKX, LKY, "rate", "rate", gruen_ab=[(n, beim("letzte", "letzte")) for n in range(1, 7)])
folie([("rate", "Ratenkauf · herrschende Lehre"), ("letzte", "Ratenkauf › wirksam erst mit der letzten Rate"),
       ("kredit", "Ratenkauf › Pflicht, später zu zahlen: nicht gedeckt")], [
    *tafel("rate", "Ratenkauf und § 110 BGB"),
    z("nach herrschender Lehre:", 110, 180, beim("rate", "herrschender"), "Bold", 34),
    *leiste_k,
    z("letzte Rate", raten_x(LKX, 6) - F("Bold", 28).getlength("letzte Rate") / 2, LKY + RH + 20, beim("letzte", "letzte"), "Bold", 28),
    *okz("erst dann gilt der Vertrag als wirksam", 470, beim("letzte", "wirksam"), "Bold", 34),
    blk(110, 560, 1040, 110, HELLGRAU, "kredit", [("Pflicht, später zu zahlen:", "ExtraBold", 32, INK),
                                                ("vom Taschengeldparagrafen nicht gedeckt", "ExtraBold", 32, INK)]),
    *neinz("Kreditgeschäfte: ohne Eltern in der Schwebe", 720, beim("kredit", "Kreditgeschäfte"), "Bold", 34,
           kreuz=beim("kredit", "Kreditgeschäfte")),
    *requisit([("rate", ("tabler", "calendar-month", 120, WEISS), "6 Monate", WEISS),
               ("letzte", ("tabler", "check", 110, GRUEN_P), "alles bezahlt", HELLGRUEN),
               ("kredit", ("tabler", "credit-card", 120, WEISS), "Kredit", HELLROT)]),
    *stehend("FR", FX, [("rate", "ruhig"), ("letzte", "froh"), ("kredit", "ernst")]),
])

# ===========================================================================================================================
# L Genehmigung durch die Eltern; Aufforderung § 108 Abs. 2 (ein Satz)
# ===========================================================================================================================
PG = "Genehmigung"
folie([("eltern", f"{PG} · § 108 BGB: die Eltern entscheiden"), ("gen", f"{PG} › erteilt: von Anfang an wirksam, § 184 BGB"),
       ("verw", f"{PG} › verweigert: endgültig unwirksam"), ("auff", f"{PG} › Aufforderung, § 108 Abs. 2 BGB")], [
    *tafel("eltern", "Es kommt auf die Eltern an"),
    *okz("genehmigt: von Anfang an wirksam", 190, "gen", "Bold", 34, x=160),
    zit("§ 184 Abs. 1 BGB", 160, 240, beim("gen", "wirksam")),
    *neinz("verweigert: endgültig unwirksam", 310, "verw", "Bold", 34, x=160, kreuz=beim("verw", "endgültig")),
    feld(110, 410, 1040, 310, "auff", fill=BLAUHELL, rand=5, rund=18, anim="pop", name="aufforderung"),
    z("Aufforderung durch Herrn Heinemann:", 150, 435, "auff", "ExtraBold", 32),
    z("Erklärung nur noch ihm gegenüber", 150, 495, beim("auff", "ihm"), "Bold", 32),
    z("Genehmigung nur binnen 2 Wochen", 150, 552, beim("auff", "binnen"), "Bold", 32),
    z("nach Empfang", 150, 598, beim("auff", "Empfang"), "Bold", 32),
    z("Schweigen gilt als Verweigerung", 150, 655, beim("auff", "Schweigen"), "Bold", 32),
    zit("§ 108 Abs. 2 BGB", 110, 745, "auff"),
    *requisit([("eltern", ("tabler", "users", 120, WEISS), "Eltern", WEISS),
               ("gen", ("tabler", "check", 110, GRUEN_P), "genehmigt", HELLGRUEN),
               ("verw", ("tabler", "x", 110, WEISS), "verweigert", HELLROT),
               ("auff", ("tabler", "calendar-month", 120, WEISS), "2 Wochen", BLAUHELL)], px=1560, pu=330, py=90),
    *paar("MU", [("eltern", "ruhig"), ("gen", "froh"), ("verw", "ernst"), ("auff", "denkt")],
          "HN", [("eltern", "ruhig"), ("verw", "sorge"), ("auff", "denkt")]),
])

# ===========================================================================================================================
# M Ergebnis: zurück im Radladen; Rückabwicklung (§ 812, Verweis Folge 245)
# ===========================================================================================================================
FRM, BIKM, HNM = 520, 1000, 1520
folie([("erg", "Ergebnis · Genehmigung verweigert"), ("erg2", "Ergebnis › endgültig unwirksam: keine 600 €"),
       ("rueck", "Ergebnis › Rückabwicklung, § 812 BGB")], [
    boden("erg"),
    *schild("Radladen Heinemann", 1380, 300, "erg", size=30),
    *okz("Mutter lehnt für beide Eltern ab, gegenüber Herrn Heinemann", 40, "erg", "Bold", 32, x=130, rechts=1880),
    *neinz("Vertrag endgültig unwirksam", 100, "erg2", "Bold", 34, x=130, rechts=1880, kreuz=beim("erg2", "endgültig")),
    *neinz("Fridolin muss die 600 € nicht zahlen", 160, beim("erg2", "Fridolin"), "Bold", 34, x=130, rechts=1880),
    *ebike(BIKM, BODEN + 6, 340, "erg"),
    *fig("FR", FRM, BODEN, FH, [("erg", "ruhig_r"), ("erg2", "froh_r"), ("rueck", "ruhig_r")], erst="cut"),
    hart(ns(NAME["FR"], FRM, BODEN, "erg", NFARBE["FR"])),
    *fig("HN", HNM, BODEN, FH, [("erg", "ernst"), ("rueck", "ruhig")], erst="cut"),
    hart(ns(NAME["HN"], HNM, BODEN, "erg", NFARBE["HN"])),
    pfeil(BIKM + 200, 470, HNM - 170, 470, beim("rueck", "E-Bike"), breite=8, kopf=24),
    ficon("tabler", "cash-banknote", 760, 400, 100, beim("rueck", "Anzahlung"), fuell=GRUEN_P),
    pfeil(840, 360, FRM + 140, 360, beim("rueck", "Anzahlung"), breite=8, kopf=24),
    pl("§ 812 BGB", BIKM, 280, beim("rueck", "Paragraf"), fill=GELB, size=34, anker="m"),
    pl("Folge „Leistungskondiktion“", BIKM, 230 - 30, beim("rueck", "Mehr"), fill=LILAHELL, size=28, anker="m"),
])

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · § 110 nicht wegen der Anzahlung bejahen"), ("tipp2", "Klausurtipp · ganze Leistung bewirkt?"),
       ("tipp3", "Klausurtipp · Rate offen: weiter mit § 108 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§ 110 nicht schon wegen der Anzahlung bejahen", 200, 200, beim("tipp", "Bejahe"), "Bold", 34),
    z("Ganze vertragsmäßige Leistung bewirkt?", 200, 300, "tipp2", "Bold", 34),
    z("und zwar mit überlassenen Mitteln?", 200, 350, beim("tipp2", "überlassenen"), "Bold", 34),
    linienzug([(130, 430), (1130, 430)], "tipp3", breite=3),
    *neinz("eine Rate offen: nein", 470, "tipp3", "ExtraBold", 35, x=245, kreuz=beim("tipp3", "nein")),
    z("dann: Genehmigung nach § 108 BGB prüfen", 200, 550, beim("tipp3", "Dann"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Einigung", True),
          ("s2", 0, "II. Wirksamkeit", True),
          ("s2a", 1, "1. beschränkt geschäftsfähig, § 106 BGB", False),
          ("s2b", 1, "2. nicht lediglich rechtlich vorteilhaft, keine Einwilligung, § 107 BGB", False),
          ("s2c", 1, "3. § 110 BGB: Leistung vollständig bewirkt? Hier nein", False),
          ("s2d", 1, "4. Genehmigung, § 108 BGB: hier verweigert", False),
          ("s3", 0, "III. Ergebnis: kein Anspruch", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Herr Heinemann gegen Fridolin"), 110, 90, "sch", 44),
           z("auf die restlichen 600 €, § 433 Abs. 2 BGB", 110, 158, beim("sch", "restlichen"), "Bold", 36, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 92, 1: 80}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Einigung"), ("s2", "Prüfungsschema › II. Wirksamkeit"),
       ("s3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Taschengeldparagraf hilft erst,", 0)], [("wenn ", 0), ("alles", "a"), (" aus dem Taschengeld", 0)],
                 [("bezahlt ist.", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "alles")}),
    *markertext([[("Beim Ratenkauf also erst", 0)], [("mit der ", 0), ("letzten Rate", "b"), (".", 0)],
                 [("Bis dahin entscheiden die ", 0), ("Eltern", "c"), (".", 0)]],
                750, 540, 44, "merk2", {"b": beim("merk2", "letzten"), "c": beim("merk2", "Eltern")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
