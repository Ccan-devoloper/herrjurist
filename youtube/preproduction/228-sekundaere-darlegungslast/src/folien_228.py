"""Folge 228 · Sekundäre Darlegungslast § 138 ZPO: Wenn nur der Gegner es weiß – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Figuren fiktiv): Familie Mehnert – Herr und Frau Mehnert, Sohn (24) und Tochter (21) – nutzt einen
Internetanschluss (Anschlussinhaber Herr Mehnert). Eine Filmfirma verklagt ihn wegen eines über den Anschluss in einer
Tauschbörse angebotenen Spielfilms auf 1.000 € Schadensersatz; ihre Anwältin argumentiert mit der IP-Adresse.
Szenen laut ../SZENENPLAN.md: A1 Wohnzimmer, A2 Klage, B Sachverhalt, C Aufbau, D 1. Grundsatz, E § 138 Abs. 1, 2 ZPO
(Wortlaut), F § 138 Abs. 3 ZPO (Wortlaut), G Vermutung und Wissensgefälle, H Voraussetzungen, I Inhalt (BGH-Zitat
BearShare Rn. 18), J keine Umkehr der Beweislast, K Fall im Wohnzimmer, L Ergebnis, M Gegenfall, N Folge des Gegenfalls
(§ 138 Abs. 3, Loud), O Klausurtipp Relation (Lexi), P Klausurschema, Q Merksatz (Lexi).
Handlungsgeräusch: Brief wird geöffnet, wenn die Post der Filmfirma kommt (../geraeusche_herkunft.json).
Wohnzimmer (Boden, Sideboard, Sofa, Sitzkissen) programmatisch aus Grundformen; Router, WLAN, Laptop, Tablet, Brief, Film
usw. aus Tabler Icons. Namensschild jeder Figur, solange sie im Bild ist. Keine echten Filmtitel, Labels oder
Tauschbörsen-Logos.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 225 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut § 138 ZPO nach gesetze-im-internet.de, BGH-Zitat
nach dem amtlichen Volltext (bundesgerichtshof.de), Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_228/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_228/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]






def dicon(*a, **k):
    """Icon als Teil einer Tabelle innerhalb der Tafel (Zeilensymbol), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e



# --- eigene Szenenbausteine Folge 228 ----------------------------------------------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in der Fallszene
FHA = 470                                    # Figurenhöhe stehend in der Fallszene
SOH, TOH = 372, 352                          # sitzende Figuren (gleicher Maßstab wie stehend)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HELLBLAU = (226, 236, 252, 255)
HOLZ = (232, 206, 160, 255)
BRAUN = (170, 122, 82, 255)
SOFA = TUERKIS

X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
IX, IU = 1560, 380                          # Requisit über den Figuren
NAME = {"HM": "Herr Mehnert", "FM": "Frau Mehnert", "SO": "Sohn", "TO": "Tochter", "AW": "Anwältin der Filmfirma"}
NFARBE = {"HM": BLAU, "FM": GRUEN, "SO": GELB, "TO": LILA, "AW": ROT}


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def stehend(k, x, folge, unten=930, hoehe=480, bis=None, erst="pop"):
    return [*fig(k, x, unten, hoehe, folge, bis=bis, erst=erst), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def zwei(links, folge_l, rechts, folge_r):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


def requisit(folge, x=IX, u=IU):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell))]."""
    els = []
    for i, (c, (s_, n_, br, fu)) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        els.append(ficon(s_, n_, x, u, br, c, fuell=fu, bis=b))
    return els


def nr(n, y, cue, farbe=BLAU, x=110):
    return [karte(x, y + 2, 50, 50, cue, fill=farbe, rund=12, schatten=3, rand=4),
            z(n, x + 25 - F("ExtraBold", 32).getlength(n) / 2, y + 4, cue, "ExtraBold", 32)]


# --- Wohnzimmer der Familie Mehnert (Seitenansicht, Grundformen + Icons) ----------------------------------------------------
SBX0, SBX1, SBTOP = 70, 300, 760             # Sideboard mit Router
SOX0, SOX1, SITZ = 360, 860, 778             # Sofa: links, rechts, Sitzfläche
KX0, KX1 = 905, 1185                         # Sitzkissen der Tochter
SOX, TOX, FMX, HMX = 640, 1045, 1400, 1700   # Figuren im Wohnzimmer


def boden_linie(c):
    return hart(El(_flaeche(1800, 8, lambda dr, s: dr.rectangle((0, 0, 1800 * s, 8 * s), fill=INK)), 60, BODEN_Y - 2, c,
                   "cut", 0.0, None, name="boden"))


def sideboard(c):
    w, h = SBX1 - SBX0, BODEN_Y - SBTOP
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 14) * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.line(((w // 2) * s, 12 * s, (w // 2) * s, (h - 22) * s), fill=INK, width=4 * s)
        for x in (24, w - 34):
            dr.rectangle((x * s, (h - 16) * s, (x + 10) * s, (h - 1) * s), fill=INK)
    return hart(El(_flaeche(w, h, zz), SBX0, SBTOP, c, "cut", 0.0, None, name="sideboard"))


def sofa(c):
    """Sofa (Rückenlehne, Sitzfläche, Armlehnen, Füße) als Pastellfläche mit Tuschekontur."""
    w, h = SOX1 - SOX0, BODEN_Y - 620
    sitz = SITZ - 620
    def zz(dr, s):
        dr.rounded_rectangle((40 * s, 6 * s, (w - 40) * s, (sitz + 20) * s), 28 * s, fill=SOFA, outline=INK, width=5 * s)
        dr.rounded_rectangle((20 * s, sitz * s, (w - 20) * s, (h - 26) * s), 18 * s, fill=SOFA, outline=INK, width=5 * s)
        for x0 in (4, w - 64):
            dr.rounded_rectangle((x0 * s, (sitz - 60) * s, (x0 + 60) * s, (h - 26) * s), 22 * s, fill=SOFA, outline=INK,
                                 width=5 * s)
        for x in (50, w - 62):
            dr.rectangle((x * s, (h - 28) * s, (x + 12) * s, (h - 1) * s), fill=INK)
    return hart(El(_flaeche(w, h, zz), SOX0, 620, c, "cut", 0.0, None, name="sofa"))


def kissen(c):
    w, h = KX1 - KX0, 46
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 20 * s, fill=ORANGE, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), KX0, BODEN_Y - h + 12, c, "cut", 0.0, None, name="kissen"))


def wohnzimmer(c):
    """Statischer Raum: Boden, Sideboard mit Router, Sofa, Sitzkissen."""
    return [boden_linie(c), sideboard(c), hart(ficon("tabler", "router", 185, SBTOP + 4, 150, c, fuell=WEISS, anim="cut")),
            sofa(c), kissen(c)]


def familie(c, folgen, bis=None, erst="cut"):
    """Alle vier im Wohnzimmer; folgen = {Kürzel: [(cue, suffix)]}. Sohn und Tochter blicken nach rechts zu den Eltern,
    Frau Mehnert nach rechts zu ihrem Mann, Herr Mehnert nach links zur Familie."""
    pos = {"SO": (SOX, SOH), "TO": (TOX, TOH), "FM": (FMX, FHA), "HM": (HMX, FHA)}
    els = []
    for k, f in folgen.items():
        x, h = pos[k]
        els += fig(k, x, BODEN_Y, h, f, bis=bis, erst=erst)
        els.append(hart(ns(NAME[k], x, BODEN_Y, f[0][0], NFARBE[k], bis=bis)) if erst == "cut" else
                   ns(NAME[k], x, BODEN_Y, f[0][0], NFARBE[k], d=0.1, bis=bis))
    return els


def pills(folge, x=70, y0=34, dy=74, size=32, bis=None):
    """Pillen oben links, je eine Zeile pro gesprochenem Gedanken: folge = [(cue, text, farbe)]."""
    return [pl(t, x, y0 + i * dy, c, fill=f, size=size, bis=bis) for i, (c, t, f) in enumerate(folge)]


# ===========================================================================================================================
# A1 Fall: das Wohnzimmer der Familie Mehnert
# ===========================================================================================================================
HM_A = ("HM_redet", HMX, BODEN_Y, FHA)
FM_A = ("FM_redet_r", FMX, BODEN_Y, FHA)
SURF = beim("haus", "surfen")
folie([(NULL, "Fall · 4 Menschen, 1 Router"), ("haus", "Fall · Familie Mehnert"), ("brief", "Fall · Post von einer Filmfirma"),
       ("vorwurf", "Fall · Der Vorwurf"), ("me1", "Fall · Herr Mehnert"), ("fm1", "Fall · Frau Mehnert")], [
    *wohnzimmer(NULL),
    ficon("tabler", "wifi", 185, SBTOP - 150, 110, beim("fall", "Router"), fuell=None),
    ficon("tabler", "device-laptop", 455, SITZ + 2, 120, SURF, fuell=WEISS),
    ficon("tabler", "device-tablet", 1232, BODEN_Y + 4, 78, SURF, fuell=WEISS),
    *pills([(NULL, "4 Menschen, 1 Router", GELB), (SURF, "alle surfen über denselben Anschluss", WEISS),
            ("brief", "Post von einer Filmfirma", BLAU), (beim("vorwurf", "Spielfilm"), "Spielfilm in einer Tauschbörse angeboten", ROT),
            (beim("vorwurf", "zwölften"), "am 12. Mai um 21:47 Uhr", ORANGE)], bis="klage"),
    szene(ficon("tabler", "mail-opened", 1565, 650, 110, "brief", fuell=WEISS), "228brief*", 1.0, -0.40),
    ficon("tabler", "movie", 905, 300, 100, beim("vorwurf", "Spielfilm"), fuell=LILA),
    *familie(NULL, {"SO": [(NULL, "ruhig_r"), (beim("haus", "Sohn"), "froh_r"), (beim("vorwurf", "Spielfilm"), "staunt_r")],
                    "TO": [(NULL, "ruhig_r"), (beim("haus", "Tochter"), "froh_r"), (beim("vorwurf", "Spielfilm"), "staunt_r")]}),
    *fig("FM", FMX, BODEN_Y, FHA, [(NULL, "ruhig_r"), (beim("haus", "Frau"), "froh_r"), ("brief", "denkt_r"),
                                   (beim("vorwurf", "Spielfilm"), "sorge_r")], bis="fm1", erst="cut"),
    hart(ns(NAME["FM"], FMX, BODEN_Y, NULL, NFARBE["FM"])),
    *redet("FM_redet_r", FMX, BODEN_Y, FHA, "fm1", "klage"),
    *fig("HM", HMX, BODEN_Y, FHA, [(NULL, "ruhig"), (beim("haus", "Herr"), "froh"), ("brief", "staunt"),
                                   (beim("vorwurf", "Spielfilm"), "schreck")], bis="me1", erst="cut"),
    hart(ns(NAME["HM"], HMX, BODEN_Y, NULL, NFARBE["HM"])),
    *redet("HM_redet", HMX, BODEN_Y, FHA, "me1", "fm1"),
    *fig("HM", HMX, BODEN_Y, FHA, [("fm1", "sorge")], erst="cut"),
    blase("sprech", 690, 210, "me1", 1330, 230, inhalt=["Ich war das nicht! Ich habe", "noch nie einen Film getauscht."],
          textsize=32, figur=HM_A, bis="fm1"),
    blase("sprech", 600, 200, "fm1", 1430, 240, inhalt=["Aber bei uns hängen", "4 Leute am selben Router."],
          textsize=32, figur=FM_A),
])

# ===========================================================================================================================
# A2 Fall: die Klage
# ===========================================================================================================================
AWX, HMX2 = 560, 1420
AW_A = ("AW_redet_r", AWX, BODEN_Y, FHA)
folie([("klage", "Fall · Die Klage"), ("aw1", "Fall · Das Argument der Anwältin"), ("frage", "Fall · Die Frage")], [
    boden_linie("klage"),
    ficon("tabler", "file-text", 990, 760, 150, "klage", fuell=WEISS),
    pl("Klage: 1.000 € Schadensersatz", 990, 786, beim("klage", "tausend"), fill=GELB, size=32, anker="m"),
    pl("IP-Adresse: Anschluss von Herrn Mehnert", 990, 852, beim("aw1", "IP"), fill=WEISS, size=28, anker="m"),
    *fig("AW", AWX, BODEN_Y, FHA, [("klage", "ruhig_r"), ("anw", "froh_r")], bis="aw1"),
    ns(NAME["AW"], AWX, BODEN_Y, "klage", NFARBE["AW"], d=0.1),
    *redet("AW_redet_r", AWX, BODEN_Y, FHA, "aw1", "frage"),
    *fig("AW", AWX, BODEN_Y, FHA, [("frage", "denkt_r")], erst="cut"),
    blase("sprech", 620, 230, "aw1", 830, 250, inhalt=["Die IP-Adresse gehört zu", "Ihrem Anschluss.", "Also waren Sie es."],
          textsize=32, figur=AW_A, bis="frage"),
    *fig("HM", HMX2, BODEN_Y, FHA, [("klage", "sorge"), ("aw1", "ernst"), ("frage", "denkt"), ("frage2", "ruhig")]),
    ns(NAME["HM"], HMX2, BODEN_Y, "klage", NFARBE["HM"], d=0.1),
    ficon("tabler", "home-question", 1740, 700, 190, beim("frage", "weiß"), fuell=GELB),
    pl("Wer wann im Internet war, weiß nur die Familie", 960, 70, beim("frage", "weiß"), fill=WEISS, size=34, anker="m"),
    pl("Was muss Herr Mehnert vortragen – und wer muss was beweisen?", 960, 160, "frage2", fill=PINK, size=38, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_228(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 85, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_228("sv", [
    "Herr und Frau Mehnert leben mit ihrem 24-jährigen Sohn und ihrer 21-jährigen Tochter zusammen. Alle vier nutzen mit "
    "eigenen Geräten denselben Internetanschluss; das WLAN ist mit einem Passwort geschützt, das alle kennen. "
    "Anschlussinhaber ist Herr Mehnert.",
    "Eine Filmfirma, Inhaberin der ausschließlichen Nutzungsrechte an einem Spielfilm, lässt ermitteln: Am 12. Mai 2026 um "
    "21:47 Uhr wurde der Film über diesen Anschluss in einer Tauschbörse zum Herunterladen angeboten. Sie verklagt Herrn "
    "Mehnert auf 1.000 € Schadensersatz.",
    "Herr Mehnert bestreitet, den Film angeboten zu haben. Er hat alle im Haushalt gefragt; niemand hat etwas eingeräumt. "
    "An dem Abend waren alle vier zu Hause.",
], "Was muss Herr Mehnert vortragen – und wer muss was beweisen?")

# ===========================================================================================================================
# C Aufbau: fünf Schritte
# ===========================================================================================================================
SCHRITTE = [("p1", "Der Grundsatz"), ("p2", "§ 138 ZPO"), ("p3", "Die sekundäre Darlegungslast"),
            ("p4", "Der Fall mit Gegenfall"), ("p5", "Die Relation")]
els_c = [*tafel("plan", "In 5 Schritten")]
for i, (c, t) in enumerate(SCHRITTE):
    y = 200 + i * 120
    els_c += [*nr(str(i + 1), y, c), z(t, 190, y, c, "Bold", 40)]
els_c += [*requisit([("p1", ("tabler", "scale", 120, WEISS)), ("p2", ("tabler", "book", 120, GELB)),
                     ("p3", ("tabler", "home-question", 140, GELB)), ("p4", ("tabler", "users", 130, GRUEN)),
                     ("p5", ("tabler", "list-numbers", 120, WEISS))]),
          *zwei("AW", [("plan", "ruhig")], "HM", [("plan", "ruhig"), ("p3", "denkt"), ("p5", "ruhig")])]
folie([("plan", "Aufbau · 5 Schritte")], rechts_frei(els_c))

# ===========================================================================================================================
# D 1. Grundsatz
# ===========================================================================================================================
folie([("g1", "1. Grundsatz · § 97 Abs. 2 UrhG"), ("g2", "1. Grundsatz › Darlegungs- und Beweislast"),
       ("g3", "1. Grundsatz › anspruchsbegründende Tatsache")], rechts_frei([
    *tafel("g1", "1. Der Grundsatz"),
    z("Anspruch: Schadensersatz, § 97 Abs. 2 UrhG", 110, 185, beim("g1", "Paragraf"), "Bold", 36),
    blk(110, 260, 1040, 160, BLAU, "g2", [("Die Filmfirma trägt die", "ExtraBold", 38, INK),
                                          ("Darlegungs- und Beweislast für die Täterschaft", "Bold", 34, INK)]),
    zit("BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), Rn. 14", 110, 436, beim("g2", "Bundesgerichtshof")),
    *okz("Täterschaft: anspruchsbegründende Tatsache", 520, "g3", "Bold", 36),
    pl("mehr: Video „Beweislast ZPO“", 110, 610, beim("g3", "Mehr"), fill=GELB, size=30),
    *requisit([("g1", ("tabler", "movie", 130, LILA)), ("g2", ("tabler", "scale", 130, WEISS))]),
    *zwei("AW", [("g1", "ruhig"), ("g2", "froh")], "HM", [("g1", "ernst"), ("g3", "denkt")]),
]))

# ===========================================================================================================================
# E 2. § 138 Abs. 1, 2 ZPO (Wortlaut)
# ===========================================================================================================================
W1 = "„(1) Die Parteien haben ihre Erklärungen über tatsächliche Umstände vollständig und der Wahrheit gemäß abzugeben."
W2 = "(2) Jede Partei hat sich über die von dem Gegner behaupteten Tatsachen zu erklären. …“"
w1, w1_y = wortlaut(80, 180, 1100, W1, "§ 138 Abs. 1 ZPO", "w1", marken=[
    ("vollständig", beim("w1", "vollständig")), ("der Wahrheit gemäß", beim("w1", "Wahrheit"))], size=34)
w2, w2_y = wortlaut(80, w1_y + 30, 1100, W2, "§ 138 Abs. 2 ZPO", "w2", marken=[
    ("Jede Partei", beim("w2", "Jede")), ("zu erklären", beim("w2", "erklären"))], size=34)
assert w2_y <= 900, w2_y
folie([("e1", "2. § 138 ZPO"), ("w1", "2. § 138 Abs. 1 ZPO › Wahrheitspflicht"),
       ("w2", "2. § 138 Abs. 2 ZPO › Erklärungspflicht")], rechts_frei([
    *tafel("e1", "2. § 138 ZPO: Erklärungspflicht"),
    *w1, *w2,
    *requisit([("e1", ("tabler", "book", 120, GELB)), ("w2", ("tabler", "messages", 120, WEISS))]),
    *zwei("AW", [("e1", "ruhig")], "HM", [("e1", "ruhig"), ("w2", "denkt")]),
]))

# ===========================================================================================================================
# F 2. § 138 Abs. 3 ZPO (Wortlaut)
# ===========================================================================================================================
W3 = ("„(3) Tatsachen, die nicht ausdrücklich bestritten werden, sind als zugestanden anzusehen, wenn nicht die Absicht, sie "
      "bestreiten zu wollen, aus den übrigen Erklärungen der Partei hervorgeht.“")
w3, w3_y = wortlaut(80, 180, 1100, W3, "§ 138 Abs. 3 ZPO", "w3", marken=[
    ("nicht ausdrücklich bestritten", beim("w3", "ausdrücklich")), ("zugestanden anzusehen", beim("w3", "zugestanden"))],
    size=34)
folie([("w3", "2. § 138 Abs. 3 ZPO › Geständnisfiktion"), ("w4", "2. § 138 Abs. 3 ZPO › ausdrückliches Bestreiten")],
      rechts_frei([
    *tafel("w3", "Die Folge: § 138 Abs. 3 ZPO"),
    *w3,
    *okz("Herr Mehnert bestreitet ausdrücklich: „Ich war es nicht.“", w3_y + 50, "w4", "Bold", 34),
    pl("Reicht das?", 110, w3_y + 140, "w5", fill=PINK, size=40),
    *requisit([("w3", ("tabler", "file-certificate", 120, WEISS)), ("w4", ("tabler", "hand-stop", 120, GELB)),
               ("w5", ("tabler", "question-mark", 110, PINK))]),
    *zwei("AW", [("w3", "ruhig"), ("w5", "denkt")], "HM", [("w3", "ruhig"), ("w4", "ernst"), ("w5", "sorge")]),
]))
assert w3_y + 220 <= 900, w3_y

# ===========================================================================================================================
# G 3. Vermutung und Wissensgefälle
# ===========================================================================================================================
folie([("v1", "3. Sekundäre Darlegungslast"), ("v2", "3. › tatsächliche Vermutung"),
       ("v3", "3. › nur die Familie weiß es")], rechts_frei([
    *tafel("v1", "3. Sekundäre Darlegungslast", size=44),
    z("Niemand sonst konnte den Anschluss nutzen?", 110, 180, "v2", "Bold", 34),
    z("Dann: tatsächliche Vermutung, der Anschlussinhaber ist Täter", 110, 232, beim("v2", "Vermutung"), size=30),
    zit("BGH, Urt. v. 6.10.2016 – I ZR 154/15 (Afterlife), Rn. 14; BearShare, Rn. 15", 110, 280, beim("v2", "Vermutung")),
    blk(110, 360, 500, 230, GRUEN, "v3", [("Familie Mehnert", "ExtraBold", 36, INK), ("weiß, wer den Anschluss", "Bold", 30, INK),
                                          ("nutzen konnte", "Bold", 30, INK)]),
    blk(650, 360, 500, 230, ROT, beim("v3", "Filmfirma"), [("Filmfirma", "ExtraBold", 36, INK),
                                                          ("sieht nur die", "Bold", 30, INK), ("IP-Adresse", "Bold", 30, INK)]),
    dicon("tabler", "home", 360, 700, 90, "v3", fuell=GELB),
    dicon("tabler", "world-www", 900, 700, 90, beim("v3", "Filmfirma"), fuell=BLAU),
    zit("vgl. Afterlife, Rn. 20: „Interna des Anschlussinhabers“", 110, 730, beim("v3", "Filmfirma")),
    *requisit([("v2", ("tabler", "router", 140, WEISS)), ("v3", ("tabler", "home-question", 150, GELB))]),
    *zwei("AW", [("v1", "ruhig"), (beim("v3", "Filmfirma"), "denkt")], "HM", [("v1", "ruhig"), ("v3", "froh")]),
]))

# ===========================================================================================================================
# H 3. Wann gilt die sekundäre Darlegungslast?
# ===========================================================================================================================
folie([("v4", "3. › Voraussetzungen"), ("v5", "3. › sekundäre Darlegungslast des Gegners")], rechts_frei([
    *tafel("v4", "Wann trifft sie den Gegner?", size=44),
    *okz("darlegungsbelastete Partei: keine nähere Kenntnis", 185, beim("v4", "darlegungsbelastete"), "Bold", 32),
    *okz("sie kann selbst nichts aufklären", 255, beim("v4", "aufklären"), "Bold", 32),
    *okz("Gegner: nähere Angaben möglich und zumutbar", 325, beim("v4", "Gegner"), "Bold", 32),
    zit("BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), Rn. 17", 185, 378, beim("v4", "zumutbar")),
    blk(110, 450, 1040, 150, GELB, "v5", [("Dann in der Regel:", "Bold", 32, INK),
                                          ("sekundäre Darlegungslast des Gegners", "ExtraBold", 38, INK)]),
    *requisit([("v4", ("tabler", "eye-off", 120, WEISS)), ("v5", ("tabler", "message-circle-question", 120, GELB))]),
    *zwei("AW", [("v4", "ruhig"), ("v5", "froh")], "HM", [("v4", "denkt"), ("v5", "ernst")]),
]))

# ===========================================================================================================================
# I 3. Inhalt: Vortrag und Nachforschung (BGH-Zitat)
# ===========================================================================================================================
ZQ = ("„… dass er vorträgt, ob andere Personen und gegebenenfalls welche anderen Personen selbständigen Zugang zu seinem "
      "Internetanschluss hatten und als Täter der Rechtsverletzung in Betracht kommen.“")
zq, zq_y = wortlaut(80, 165, 1100, ZQ, "BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), Rn. 18", beim("i2", "Ob"), marken=[
    ("andere Personen", beim("i2", "andere")), ("selbständigen Zugang", beim("i2", "selbständigen")),
    ("als Täter", beim("i2", "Täter"))], size=30)
folie([("i1", "3. › Was muss er vortragen?"), ("i3", "3. › Nachforschung im Rahmen des Zumutbaren"),
       ("i4", "3. › Grenzen der Nachforschung")], rechts_frei([
    *tafel("i1", "Was muss er vortragen?"),
    *zq,
    *okz("nachforschen, soweit zumutbar, und Ergebnis mitteilen", zq_y + 30, "i3", "Bold", 32),
    zit("BGH, Urt. v. 6.10.2016 – I ZR 154/15 (Afterlife), Rn. 15", 185, zq_y + 76, beim("i3", "mitteilen")),
    *neinz("nicht nötig: den Computer der Ehefrau untersuchen", zq_y + 140, beim("i4", "Computer"), "Bold", 32),
    *neinz("nicht nötig: ihre Internetnutzung dokumentieren", zq_y + 205, beim("i4", "dokumentieren"), "Bold", 32),
    zit("Afterlife, Leitsatz b, Rn. 26: in der Regel unzumutbar", 185, zq_y + 255, beim("i4", "dokumentieren")),
    *requisit([("i1", ("tabler", "message-circle-question", 120, GELB)), (beim("i2", "Ob"), ("tabler", "users", 130, GRUEN)),
               ("i3", ("tabler", "search", 120, WEISS)), ("i4", ("tabler", "device-laptop", 150, WEISS))]),
    *zwei("FM", [("i1", "ruhig"), (beim("i4", "Computer"), "froh")], "HM", [("i1", "denkt"), ("i3", "ernst"), ("i4", "ruhig")]),
]))
assert zq_y + 300 <= 900, zq_y

# ===========================================================================================================================
# J 3. Keine Umkehr der Beweislast
# ===========================================================================================================================
folie([("u1", "3. › keine Umkehr der Beweislast"), ("u2", "3. › Grenze: § 138 Abs. 1, 2 ZPO")], rechts_frei([
    *tafel("u1", "Keine Umkehr der Beweislast"),
    blk(110, 180, 1040, 110, GRUEN, beim("u1", "kehrt"), [("Die Beweislast bleibt bei der Filmfirma", "ExtraBold", 36, INK)]),
    z("Grenze: Wahrheits- und Erklärungspflicht, § 138 Abs. 1, 2 ZPO", 110, 345, beim("u2", "Wahrheits"), "Bold", 32),
    *neinz("keine Pflicht, der Filmfirma alles zu liefern,", 425, beim("u2", "nicht"), "Bold", 32),
    z("was sie für ihren Prozesserfolg braucht", 185, 475, beim("u2", "nicht"), size=32),
    zit("BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), Rn. 18", 110, 545, beim("u2", "Prozesserfolg")),
    *requisit([("u1", ("tabler", "scale", 140, WEISS)), ("u2", ("tabler", "book", 120, GELB))]),
    *zwei("AW", [("u1", "ernst"), ("u2", "denkt")], "HM", [("u1", "froh"), ("u2", "ruhig")]),
]))

# ===========================================================================================================================
# K 4. Der Fall: Herr Mehnert trägt vor (zurück im Wohnzimmer)
# ===========================================================================================================================
HM_K = ("HM_redet", HMX, BODEN_Y, FHA)
GERAET = beim("me2", "Geräte")
folie([("f1", "4. Der Fall · Herr Mehnert hat alle gefragt"), ("me2", "4. Der Fall › Vortrag von Herrn Mehnert"),
       ("f2", "4. Der Fall › niemand hat etwas zugegeben")], [
    *wohnzimmer("f1"),
    ficon("tabler", "device-laptop", 455, SITZ + 2, 120, GERAET, fuell=WEISS),
    ficon("tabler", "device-tablet", 1232, BODEN_Y + 4, 78, GERAET, fuell=WEISS),
    ficon("tabler", "key", 185, SBTOP - 130, 90, beim("me2", "WLAN"), fuell=GELB),
    *pills([("f1", "Herr Mehnert hat alle gefragt", GELB), (beim("me2", "WLAN"), "alle kennen das WLAN-Passwort", WEISS),
            (beim("me2", "Abend"), "12. Mai, 21:47 Uhr: alle zu Hause", ORANGE), ("f2", "Zugegeben hat es niemand", ROT)]),
    *familie("f1", {"SO": [("f1", "ruhig_r"), (beim("me2", "Sohn"), "froh_r"), ("f2", "ruhig_r")],
                    "TO": [("f1", "ruhig_r"), (beim("me2", "Tochter"), "froh_r"), ("f2", "ruhig_r")],
                    "FM": [("f1", "ruhig_r"), (beim("me2", "Frau"), "froh_r"), ("f2", "ruhig_r")]}, erst="pop"),
    *fig("HM", HMX, BODEN_Y, FHA, [("f1", "ruhig")], bis="me2"),
    ns(NAME["HM"], HMX, BODEN_Y, "f1", NFARBE["HM"], d=0.1),
    *redet("HM_redet", HMX, BODEN_Y, FHA, "me2", "f2"),
    *fig("HM", HMX, BODEN_Y, FHA, [("f2", "ernst")], erst="cut"),
    blase("sprech", 760, 290, "me2", 1300, 250, inhalt=["Meine Frau, mein Sohn und meine", "Tochter haben eigene Geräte",
                                                        "und kennen das WLAN-Passwort.", "An dem Abend waren alle zu Hause."],
          textsize=30, figur=HM_K, bis="f2"),
])

# ===========================================================================================================================
# L 4. Der Fall: Ergebnis
# ===========================================================================================================================
folie([("f3", "4. Der Fall › sekundäre Darlegungslast erfüllt"), ("f4", "4. Der Fall › Beweislast bei der Filmfirma"),
       ("f5", "4. Der Fall › Ergebnis")], rechts_frei([
    *tafel("f3", "4. Der Fall"),
    *okz("sekundäre Darlegungslast erfüllt", 185, beim("f3", "sekundären"), "Bold", 36),
    *neinz("keine Vermutung gegen Herrn Mehnert", 255, beim("f3", "Vermutung"), "Bold", 34),
    zit("BearShare, Rn. 15, 19; Afterlife, Rn. 15, 26", 185, 305, beim("f3", "Vermutung")),
    blk(110, 380, 1040, 170, BLAU, "f4", [("Die Filmfirma muss darlegen und beweisen:", "Bold", 34, INK),
                                          ("gerade Herr Mehnert hat den Film angeboten", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), Rn. 20", 110, 566, beim("f4", "angeboten")),
    blk(110, 640, 1040, 90, GRUEN, "f5", [("Kein Beweis: Klage abgewiesen", "ExtraBold", 38, INK)]),
    *requisit([("f3", ("tabler", "circle-check", 120, GRUEN)), ("f4", ("tabler", "scale", 140, WEISS)),
               ("f5", ("tabler", "file-x", 120, WEISS))]),
    *zwei("AW", [("f3", "ernst"), ("f4", "ruhig"), ("f5", "denkt")], "HM", [("f3", "ruhig"), ("f5", "froh")]),
]))

# ===========================================================================================================================
# M 4. Der Gegenfall: pauschales Bestreiten
# ===========================================================================================================================
HM_M = ("HM_redet", FX, FB, FR)
folie([("gf", "4. Der Gegenfall"), ("gf2", "4. Der Gegenfall › pauschales Bestreiten"),
       ("gf3", "4. Der Gegenfall › nachvollziehbarer Vortrag")], rechts_frei([
    *tafel("gf", "4. Der Gegenfall"),
    z("Herr Mehnert sagt nur:", 110, 180, "gf", "Bold", 34),
    z("„Theoretisch könnte es jeder bei uns gewesen sein.“", 110, 232, "me3", size=32),
    *neinz("pauschal, bloß theoretische Möglichkeit: genügt nicht", 315, beim("gf2", "Das"), "Bold", 32),
    zit("Afterlife, Rn. 15; Loud, Rn. 15", 185, 362, beim("gf2", "Bundesgerichtshof")),
    z("Nötig ist nachvollziehbarer Vortrag: Wer hatte", 110, 440, "gf3", "Bold", 32),
    z("Gelegenheit nach …", 110, 486, "gf3", "Bold", 32),
    z("· Nutzerverhalten", 150, 545, beim("gf3", "Nutzerverhalten"), size=32),
    z("· Kenntnissen und Fähigkeiten", 150, 595, beim("gf3", "Kenntnissen"), size=32),
    z("· zur Tatzeit", 150, 645, beim("gf3", "Tatzeit"), size=32),
    zit("BGH, Urt. v. 30.3.2017 – I ZR 19/16 (Loud), Rn. 15", 110, 712, beim("gf3", "Tatzeit")),
    *fig("HM", FX, FB, FR, [("gf", "ruhig")], bis="me3"),
    *redet("HM_redet", FX, FB, FR, "me3", "gf2"),
    *fig("HM", FX, FB, FR, [("gf2", "sorge"), ("gf3", "denkt")], erst="cut"),
    ns(NAME["HM"], FX, FB, "gf", NFARBE["HM"], d=0.1),
    blase("sprech", 590, 200, "me3", 1560, 200, inhalt=["Theoretisch könnte es", "jeder bei uns gewesen sein."],
          textsize=32, figur=HM_M, bis="gf2"),
    *requisit([("gf2", ("tabler", "question-mark", 110, PINK)), ("gf3", ("tabler", "clock", 120, WEISS))]),
]))

# ===========================================================================================================================
# N 4. Der Gegenfall: die Folge
# ===========================================================================================================================
folie([("gf4", "4. Der Gegenfall › § 138 Abs. 3 ZPO"), ("gf5", "4. Der Gegenfall › Haftung als Täter"),
       ("loud", "4. Der Gegenfall › Name nennen")], rechts_frei([
    *tafel("gf4", "Gegenfall: die Folge"),
    *neinz("einfaches Bestreiten unwirksam", 185, beim("gf4", "einfaches"), "Bold", 36),
    z("§ 138 Abs. 3 ZPO: Behauptung gilt als zugestanden", 185, 245, beim("gf4", "Paragraf"), "Bold", 32),
    zit("BGH, Urt. v. 30.3.2017 – I ZR 19/16 (Loud), Rn. 27", 185, 295, beim("gf4", "zugestanden")),
    blk(110, 365, 1040, 100, ROT, "gf5", [("Vermutung greift: Haftung als Täter", "ExtraBold", 36, INK)]),
    zit("Loud, Rn. 29", 110, 478, beim("gf5", "haftet")),
    blk(110, 545, 1040, 160, GELB, "loud", [("Weiß er, wer es war, etwa ein volljähriges Kind?", "Bold", 32, INK),
                                            ("Name nennen, sonst haftet er selbst", "ExtraBold", 36, INK)]),
    zit("BGH, Urt. v. 30.3.2017 – I ZR 19/16 (Loud), Leitsatz, Rn. 26", 110, 720, beim("loud", "Namen")),
    *requisit([("gf4", ("tabler", "file-certificate", 120, WEISS)), ("gf5", ("tabler", "gavel", 120, WEISS)),
               ("loud", ("tabler", "id", 130, GELB))]),
    *zwei("AW", [("gf4", "ruhig"), ("gf5", "froh"), ("loud", "ruhig")], "HM", [("gf4", "sorge"), ("gf5", "schreck"),
                                                                             ("loud", "denkt")]),
]))

# ===========================================================================================================================
# O Klausurtipp (Lexi): Relation
# ===========================================================================================================================
def station(x, y, w, text, cue, fill):
    return [karte(x, y, w, 80, cue, fill=fill, rund=16, schatten=4, rand=4),
            z(text, x + w / 2 - F("Bold", 28).getlength(text) / 2, y + 20, cue, "Bold", 28, rechts=x + w)]


DST = beim("tipp", "Darlegungsstation")
BST = beim("tipp", "Beklagtenstation")
folie([("tipp", "Klausurtipp · Relation"), ("t1", "Klausurtipp › Erheblichkeit des Bestreitens"),
       ("t3", "Klausurtipp › Beweisstation")], [
    *tafel("tipp", "Klausurtipp: Relation", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("sekundäre Darlegungslast: Darlegungsstation,", 200, 200, beim("tipp", "sekundäre"), "Bold", 32),
    z("und zwar die Beklagtenstation", 200, 248, BST, "Bold", 32),
    z("Darlegungsstation", 200, 312, DST, "Bold", 28, farbe=TEXT),
    linienzug([(200, 352), (800, 352)], DST, breite=3, farbe=TEXT),
    *station(200, 368, 290, "Klägerstation", DST, WEISS),
    *station(510, 368, 290, "Beklagtenstation", DST, WEISS),
    bis_(karte(510, 368, 290, 80, BST, fill=GELB, rund=16, schatten=4, rand=4), None),
    z("Beklagtenstation", 655 - F("Bold", 28).getlength("Beklagtenstation") / 2, 388, BST, "Bold", 28, rechts=800),
    *station(840, 368, 290, "Beweisstation", beim("t2", "Beweisstation"), WEISS),
    z("Ist das Bestreiten erheblich?", 200, 485, "t1", "Bold", 34),
    *neinz("pauschal: unbeachtlich, Täterschaft zugestanden", 560, beim("t2", "Pauschales"), size=32, x=245),
    z("keine Beweisstation nötig", 245, 608, beim("t2", "Beweisstation"), size=32),
    *okz("genug vorgetragen: Täterschaft streitig", 690, "t3", size=32, x=245),
    z("Beweisstation: Beweislast beim Kläger", 245, 738, beim("t3", "Beweisstation"), "Bold", 32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# P Klausurschema (breit, Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", [("Wer trägt die Darlegungslast? Grundsätzlich der Anspruchsteller", "k1")]),
          ("k2", "II.", [("Fehlt ihm der Einblick, und kann der Gegner zumutbar mehr sagen?", "k2"),
                         ("Dann: sekundäre Darlegungslast des Gegners", beim("k2", "Dann"))]),
          ("k3", "III.", [("Hat der Gegner konkret vorgetragen, auch nach zumutbarer Nachforschung?", "k3")]),
          ("k4", "IV.", [("ja: Der Anspruchsteller beweist.", beim("k4", "Wenn")),
                         ("nein: Seine Behauptung gilt als zugestanden.", beim("k4", "Wenn", nr=2))])]
els_s = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: sekundäre Darlegungslast"), 110, 90, "sch", 50)]
y = 210
for c, num, zeilen in REIHEN:
    els_s.append(z(num, 120, y, c, "ExtraBold", 38, rechts=1820))
    for j, (t, cc) in enumerate(zeilen):
        els_s.append(z(t, 230, y + j * 56, cc, "Bold" if j == 0 else "Regular", 36, rechts=1820))
    y += 56 * len(zeilen) + 52
els_s.append(zit("Belege: § 138 ZPO; BGH I ZR 169/12 (BearShare), Rn. 14–20; I ZR 154/15 (Afterlife), Rn. 15; "
                 "I ZR 19/16 (Loud), Rn. 15, 27", 120, y + 10, beim("k4", "zugestanden"), rechts=1820))
assert y + 60 <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Darlegungslast"), ("k2", "Klausurschema › II. sekundäre Darlegungslast"),
       ("k3", "Klausurschema › III. konkreter Vortrag"), ("k4", "Klausurschema › IV. Ergebnis")], els_s)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer mehr weiß, ", 0), ("muss mehr sagen", "a"), (".", 0)]], 750, 300, 50, "merke",
                {"a": beim("merke", "muss")}),
    *markertext([[("Die sekundäre Darlegungslast", 0)], [("verlangt ", 0), ("Vortrag", "b"), (", keinen Beweis.", 0)],
                 [("Die ", 0), ("Beweislast bleibt", "c"), (", wo sie war.", 0)]],
                750, 460, 46, "mk2", {"b": beim("mk2", "Vortrag"), "c": beim("mk2", "Beweislast")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
