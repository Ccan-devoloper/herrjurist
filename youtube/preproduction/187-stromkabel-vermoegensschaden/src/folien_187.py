"""Folge 187 · Bagger trifft Stromkabel: Reiner Vermögensschaden – kein Ersatz? – Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv, nach dem Plan-Hook): Fiete (Tiefbauunternehmer, fährt selbst den Bagger) reißt am Rand eines Gewerbegebiets ein
Stromkabel des Netzbetreibers auf; die Fahrradfabrik von Gotthard zwei Kilometer weiter steht einen Tag still (48.000 €),
nichts geht kaputt. Szenen laut ../SZENENPLAN.md: A1 Baustelle und Fabrik, A2 am Graben, B Sachverhalt, C Wortlautkarte
§ 823 Abs. 1 BGB, D Das Vermögen fehlt, E Prüfungsweg, F I. Eigentum, G Gegenfall Substanzschaden, H II. Gewerbebetrieb
(Begriff), I Betriebsbezogenheit im Fall, J § 823 Abs. 2 BGB, K Ergebnis, L Klausurtipp (Lexi), M Prüfschema, N Merksatz (Lexi).
DARSTELLUNG: Baustelle und Fabrik fiktiv, Stromkabel als Linie mit Blitz-Icons (Tabler), kein Unfall mit Personen; zwei
Handlungsgeräusche (Baggerschaufel, Maschinen laufen aus; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist (im Bagger: Schild unter dem Bagger). Hilfsfunktionen glyphen/z/pl/tafel/
blk/wortlaut/redet/fig/ns/okz/neinz/requisit als eigene Kopie aus Folge 158 (gemeinsame Dateien unverändert); neu: erdreich(),
kabel(), funken(), netzbild().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_187/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_187/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch für Wortlautkarten (Wortlaut bleibt unverändert)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur] if cur else zeilen


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        t = zeilen[zi]
        a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149) ------------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"FI": "Fiete", "GO": "Gotthard"}
NFARBE = {"FI": ORANGE, "GO": BLAU}


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_fi, folge_go):
    """Fiete und Gotthard rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("FI", X1, folge_fi), *stehend("GO", X2, folge_go)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
ERDE = (226, 196, 158, 255)
GRUBE = (176, 138, 98, 255)
KABEL = (70, 70, 74, 255)
G0, G1 = 640, 930                            # Erdoberfläche, Unterkante des Erdreichs
KY = 840                                     # Höhe des Kabels im Erdreich
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def _hart_wenn(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def erdreich(c):
    """Seitenansicht: Erdreich unter der Oberfläche (Grundform, Tuschekontur oben)."""
    im = Image.new("RGBA", (1860, G1 - G0))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860, G1 - G0), fill=ERDE)
    dr.line((0, 2, 1860, 2), fill=INK, width=6)
    for x in range(40, 1860, 140):                                           # Krümel im Erdreich
        dr.ellipse((x, 60 + (x * 7) % 90, x + 10, 68 + (x * 7) % 90), fill=GRUBE)
    return _hart_wenn(c)(El(im, 30, G0, c, "cut", 0.0, None, name="erdreich"))


def kabel(c, x0=30, x1=1890):
    """Stromkabel im Erdreich: dicke Linie mit Tuschekontur."""
    im = Image.new("RGBA", (x1 - x0, 30))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 3, x1 - x0 - 1, 26), 11, fill=KABEL, outline=INK, width=4)
    return _hart_wenn(c)(El(im, x0, KY - 15, c, "cut", 0.0, None, name="kabel"))


def grube(x0, x1, cue, bis=None):
    """Ausgehobener Graben bis zum Kabel."""
    im = Image.new("RGBA", (x1 - x0, KY - G0 + 20))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, x1 - x0, KY - G0 + 20), fill=GRUBE, outline=INK, width=4)
    return bis_(El(im, x0, G0 - 2, cue, "cut", 0.0, bis, name="grube"), bis)


def funken(cx, cy, cue, bis=None):
    """Aufgerissenes Kabel: Lücke im Kabel und kurze rote Risslinien (Grundform)."""
    im = Image.new("RGBA", (120, 90))
    dr = ImageDraw.Draw(im)
    dr.rectangle((44, 30, 76, 62), fill=GRUBE)
    for (a, b, c_, d_) in [(40, 46, 18, 20), (80, 46, 102, 20), (40, 46, 16, 70), (80, 46, 104, 72), (60, 30, 60, 4)]:
        dr.line((a, b, c_, d_), fill=DROT, width=6)
    return bis_(El(im, cx - 60, cy - 46, cue, "pop", 0.0, bis, name="funken"), bis)


def haufen(cx, cue):
    """Ausgehobene Erde neben dem Graben."""
    im = Image.new("RGBA", (200, 70))
    ImageDraw.Draw(im).pieslice((0, 0, 200, 140), 180, 360, fill=GRUBE, outline=INK, width=4)
    return El(im, cx - 100, G0 - 68, cue, "pop", 0.0, None, name="haufen")


# ===========================================================================================================================
# A1 Fall: Baustelle und Fabrik
# ===========================================================================================================================
BAG_X, BAG_W = 330, 360                      # Bagger (Tabler „backhoe“)
GR0, GR1 = 505, 600                          # Graben
FAB_X = 1430                                 # Fabrik (Tabler „building-factory-2“)
FX_A, GX_A = 850, 1770                       # Fiete neben dem Bagger, Gotthard vor seiner Fabrik
FHA = 400                                    # Figurenhöhe in der Fallszene
F_REIN = beim("fiete", "Graben")
BLITZE = [1050, 1300, 1600, 1830]
folie([(NULL, "Fall · Baustelle am Gewerbegebiet"), ("treffer", "Fall · Das Stromkabel"), ("fabrik", "Fall · Die Fahrradfabrik"),
       ("dunkel", "Fall · Stromausfall")], [
    erdreich(NULL), kabel(NULL),
    hart(ficon("tabler", "backhoe", BAG_X, G0 + 4, BAG_W, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "traffic-cone", 90, G0 + 4, 70, NULL, fuell=ORANGE, anim="cut")),
    hart(ficon("tabler", "traffic-cone", 740, G0 + 4, 70, NULL, fuell=ORANGE, anim="cut")),
    hart(pl("Baustelle am Rand eines Gewerbegebiets", 70, 30, NULL, fill=GELB, size=34)),
    *[hart(bis_(ficon("tabler", "bolt", x, KY - 22, 56, NULL, fuell=GELB, anim="cut"), "dunkel")) for x in BLITZE],
    # Fiete neben seinem Bagger, dann steigt er ein (Namensschild unter dem Bagger)
    *fig("FI", FX_A, G0, FHA, [(beim("fiete", "Fiete"), "ruhig")], bis=F_REIN),
    bis_(ns("Fiete", FX_A, G0, beim("fiete", "Fiete"), ORANGE, d=0.1), F_REIN),
    pl("Fiete: kleines Tiefbauunternehmen", 70, 100, beim("fiete", "Fiete"), fill=WEISS, size=32, bis="fabrik"),
    szene(grube(GR0, GR1, F_REIN), "187bagger*", 0.7, 0.0),
    haufen(GR1 + 70, F_REIN),
    ns("Fiete", BAG_X, G0, F_REIN, ORANGE),
    pl("hebt mit dem Bagger einen Graben aus", 70, 170, beim("fiete", "hebt"), fill=WEISS, size=32, bis="fabrik"),
    pl("Leitungspläne nicht angesehen", 70, 240, "plan", fill=HELLROT, size=32, bis="fabrik"),
    funken((GR0 + GR1) / 2, KY, "treffer"),
    pl("Stromkabel aufgerissen", (GR0 + GR1) / 2, G1 - 50, beim("treffer", "Stromkabel"), fill=HELLROT, size=30, anker="m"),
    pl("Kabel des Netzbetreibers, versorgt das Gewerbegebiet", 70, 310, beim("netz", "Netzbetreiber"), fill=WEISS, size=32,
       bis="fabrik"),
    # die Fahrradfabrik zwei Kilometer weiter
    bis_(ficon("tabler", "building-factory-2", FAB_X, G0 + 4, 420, "fabrik", fuell=BLAU), "dunkel"),
    ficon("tabler", "building-factory-2", FAB_X, G0 + 4, 420, "dunkel", fuell=HELLGRAU, anim="cut"),
    ficon("tabler", "bike", FAB_X - 40, G0 - 300, 120, beim("fabrik", "Fahrradfabrik"), fuell=WEISS),
    pfeil(800, 420, 1180, 420, beim("fabrik", "Kilometer"), breite=8, kopf=26),
    pl("2 km", 990, 340, beim("fabrik", "Kilometer"), fill=GELB, size=34, anker="m"),
    *fig("GO", GX_A, G0, FHA, [(beim("fabrik", "Gotthard"), "ruhig"), ("dunkel", "schreck"), ("still", "sorge"),
                                ("heil", "skeptisch")]),
    ns("Gotthard", GX_A, G0, beim("fabrik", "Gotthard"), BLAU, d=0.1),
    pl("Fahrradfabrik von Gotthard", 70, 100, "fabrik", fill=BLAU, size=32, bis="dunkel"),
    *[ficon("tabler", "bolt-off", x, KY - 22, 56, "dunkel", fuell=HELLGRAU, anim="cut") for x in BLITZE],
    szene(pl("Strom fällt aus", 70, 100, "dunkel", fill=HELLROT, size=32), "187maschine*", 0.7, 0.0),
    ficon("tabler", "clock-pause", 70 + 40, 260 + 64, 64, "still", fuell=WEISS),
    pl("Fertigung steht 1 Tag still", 160, 254, "still", fill=GELB, size=32),
    pl("nichts kaputt: Maschinen laufen am nächsten Morgen wieder", 70, 170, "heil", fill=HELLGRUEN, size=30),
    ficon("tabler", "settings", FAB_X + 130, G0 - 300, 90, beim("heil", "Maschinen"), fuell=GRUEN),
])

# ===========================================================================================================================
# A2 Fall: am Graben
# ===========================================================================================================================
FX_B, GX_B = 900, 1330
folie([("g1", "Fall · Gotthard verlangt Ersatz"), ("frage", "Fall · Die Frage"), ("klass", "Fall · Ein Klassiker")], [
    erdreich("g1"), kabel("g1"),
    ficon("tabler", "backhoe", BAG_X, G0 + 4, BAG_W, "g1", fuell=GELB, anim="cut"),
    grube(GR0, GR1, "g1"), haufen(GR1 + 70, "g1"), funken((GR0 + GR1) / 2, KY, "g1"),
    ficon("tabler", "building-factory-2", 1700, G0 + 4, 300, "g1", fuell=HELLGRAU, anim="cut"),
    *fig("FI", FX_B, G0, FHA, [("g1", "ernst_r")], bis="f1", erst="cut"),
    ns("Fiete", FX_B, G0, "g1", ORANGE),
    *redet("GO_redet", GX_B, G0, FHA, "g1", "f1"),
    blase("sprech", 720, 175, "g1", 1160, 112, inhalt=["Ein Tag Stillstand kostet mich", "48.000 €. Das zahlen Sie!"], textsize=36,
          figur=("GO_redet", GX_B, G0, FHA), bis="f1"),
    ns("Gotthard", GX_B, G0, "g1", BLAU),
    pl("Produktionsausfall: 48.000 €", 70, 868, beim("g1", "achtundvierzigtausend"), fill=GELB, size=32),
    *redet("FI_redet_r", FX_B, G0, FHA, "f1", "frage"),
    blase("sprech", 640, 175, "f1", 860, 112, inhalt=["Ich habe ein Kabel getroffen,", "nicht Ihre Fabrik!"], textsize=36,
          figur=("FI_redet_r", FX_B, G0, FHA), bis="frage"),
    *fig("GO", GX_B, G0, FHA, [("f1", "wut"), ("frage", "skeptisch"), ("klass", "ernst")], erst="cut"),
    *fig("FI", FX_B, G0, FHA, [("frage", "sorge_r"), ("klass", "denkt_r")], erst="cut"),
    pl("Muss Fiete den Produktionsausfall ersetzen?", 70, 100, "frage", fill=PINK, size=32),
    pl("Klassiker: der Stromkabel-Fall", 70, 170, beim("klass", "Klassiker"), fill=GELB, size=32),
    zit("BGH, Urt. v. 9.12.1958 – VI ZR 199/57, BGHZ 29, 65", 80, 236, beim("klass", "Stromkabel")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_187(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_187("sv", [
    "Fiete führt ein kleines Tiefbauunternehmen. Am Rand eines Gewerbegebiets hebt er mit seinem Bagger einen Graben aus. "
    "In die Leitungspläne hat er vorher nicht geschaut. Die Schaufel reißt ein Stromkabel auf, das dem örtlichen "
    "Netzbetreiber gehört und das ganze Gewerbegebiet versorgt.",
    "Zwei Kilometer weiter liegt die Fahrradfabrik von Gotthard. Dort fällt der Strom aus; die Fertigung steht einen ganzen "
    "Tag still. Kaputt geht dabei nichts, am nächsten Morgen laufen die Maschinen wieder.",
    "Gotthard sagt zu Fiete: „Ein Tag Stillstand kostet mich 48.000 €. Das zahlen Sie!“ Fiete antwortet: „Ich habe ein "
    "Kabel getroffen, nicht Ihre Fabrik!“",
], "Kann Gotthard von Fiete die 48.000 € aus § 823 BGB verlangen?")

# ===========================================================================================================================
# C Wortlautkarte § 823 Abs. 1 BGB
# ===========================================================================================================================
W823 = umbruch("„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein "
               "sonstiges Recht eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden "
               "Schadens verpflichtet.“", 34, 1040)
_zi = lambda wort: next(i for i, t in enumerate(W823) if wort in t)
RG = [("Leben", "Leben"), ("Körper", "Körper"), ("Gesundheit", "Gesundheit"), ("Freiheit", "Freiheit"), ("Eigentum", "Eigentum"),
      ("sonstiges Recht", "sonstiges")]
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 1 BGB", "norm",
                        marken=[(_zi(t), t, beim("w1", w)) for t, w in RG], size=34)
PN = "Die Norm: § 823 Abs. 1 BGB"
folie([("norm", PN), ("w1", f"{PN} › geschützte Rechtsgüter"), ("schema", f"{PN} › hier: Rechtsgutsverletzung")], rechts_frei([
    *tafel("norm", "Die Norm: § 823 Abs. 1 BGB"),
    *w823,
    z("ganzes Prüfschema: Video „Deliktsrecht“", 110, w823_y + 40, beim("schema", "Prüfschema"), "Bold", 30, farbe=TEXT),
    blk(110, w823_y + 100, 1040, 80, GELB, beim("schema", "hier"), [("hier: das erste Merkmal, die Rechtsgutsverletzung",
                                                                   "ExtraBold", 32, INK)]),
    *requisit([("norm", ("tabler", "book", 100, WEISS), "§ 823 Abs. 1 BGB", GELB),
               ("schema", ("tabler", "list-check", 100, WEISS), "Rechtsgutsverletzung", GELB)]),
    *zwei([("norm", "ruhig"), ("schema", "denkt")], [("norm", "skeptisch"), ("w1", "ernst")]),
]))

# ===========================================================================================================================
# D Das Vermögen fehlt
# ===========================================================================================================================
PV = "Das Vermögen fehlt"
folie([("liste", "Die Norm › bestimmte Rechtsgüter"), ("fehlt", f"{PV} › Vermögen als solches nicht geschützt"),
       ("grund", f"{PV} › Entscheidung des Gesetzgebers"), ("ufer", f"{PV} › keine uferlose Haftung"),
       ("ausn", f"{PV} › Ausnahme: § 826 BGB")], rechts_frei([
    *tafel("liste", "Warum fehlt das Vermögen?"),
    blk(110, 175, 1040, 130, HELLGRUEN, "liste", [("geschützt: Leben, Körper, Gesundheit,", "Bold", 32, INK),
                                                ("Freiheit, Eigentum, sonstige Rechte", "Bold", 32, INK)]),
    *neinz("das Vermögen als solches", 340, "fehlt", "ExtraBold", 34, x=160),
    zit("BGH, Urt. v. 5.4.2018 – III ZR 211/17, Rn. 19", 160, 392, "fehlt"),
    z("Gesetzgeber: keine allgemeine deliktische", 110, 455, beim("grund", "Gesetzgeber"), "Bold", 32),
    z("Haftung für Vermögensschäden", 110, 500, beim("grund", "Gesetzgeber"), "Bold", 32),
    zit("BGH, Urt. v. 13.12.2011 – XI ZR 51/10, Rn. 26", 110, 548, beim("grund", "Gesetzgeber")),
    blk(110, 605, 1040, 80, GELB, "ufer", [("sonst uferlose Haftung: 1 Kabel trifft viele Betriebe", "ExtraBold", 30, INK)]),
    z("Ausnahme: § 826 BGB, vorsätzliche", 110, 720, "ausn", "Bold", 32),
    z("sittenwidrige Schädigung", 110, 765, beim("ausn", "vorsätzlicher"), "Bold", 32),
    *requisit([("liste", ("tabler", "list-check", 100, WEISS), "Rechtsgüter", HELLGRUEN),
               ("fehlt", ("tabler", "wallet", 100, GELB), "Vermögen: nein", HELLROT),
               ("grund", ("tabler", "scale", 100, WEISS), "keine allgemeine Haftung", WEISS),
               ("ufer", ("tabler", "users-group", 110, BLAU), "viele Betriebe", WEISS),
               ("ausn", ("tabler", "alert-triangle", 100, GELB), "§ 826 BGB", WEISS)]),
    *zwei([("liste", "ruhig"), ("ufer", "froh")], [("liste", "ernst"), ("fehlt", "sorge"), ("ausn", "skeptisch")]),
]))

# ===========================================================================================================================
# E Prüfungsweg
# ===========================================================================================================================
folie([("pruef", "Prüfung · geschütztes Recht der Fabrik?"), ("p1", "Prüfung › I. Eigentum"), ("p2", "Prüfung › II. Gewerbebetrieb")],
      rechts_frei([
    *tafel("pruef", "Ist ein Recht der Fabrik verletzt?"),
    blk(110, 200, 1040, 110, GELB, "p1", [("I. Eigentum", "ExtraBold", 40, INK)]),
    blk(110, 350, 1040, 110, BLAU, "p2", [("II. Recht am Gewerbebetrieb", "ExtraBold", 40, INK)]),
    *requisit([("pruef", ("tabler", "building-factory-2", 160, BLAU), "Fahrradfabrik", WEISS),
               ("p1", ("tabler", "settings", 100, GELB), "Eigentum", GELB),
               ("p2", ("tabler", "building-factory-2", 160, BLAU), "Gewerbebetrieb", BLAU)]),
    *zwei([("pruef", "ernst")], [("pruef", "skeptisch"), ("p2", "ernst")]),
]))

# ===========================================================================================================================
# F I. Eigentum
# ===========================================================================================================================
PE = "I. Eigentum"
folie([("eig", PE), ("kabel", f"{PE} › am Kabel: Netzbetreiber"), ("masch", f"{PE} › Maschinen der Fabrik"),
       ("bgh1", f"{PE} › Fertigung nur unterbrochen"), ("nutz", f"{PE} › Nutzung: Einwirkung auf die Sache?"),
       ("eigerg", f"{PE} › nicht verletzt")], rechts_frei([
    *tafel("eig", "I. Das Eigentum"),
    *okz("Kabel beschädigt: Eigentum des Netzbetreibers", 180, beim("kabel", "Kabel"), "Bold", 32, x=160),
    z("Ersatz verlangen kann er, Gotthard nicht", 160, 232, "netzan", size=30),
    zit("BGH, Urt. v. 8.5.2018 – VI ZR 295/17, Rn. 10", 160, 276, "netzan"),
    z("Maschinen der Fabrik: unversehrt", 110, 335, beim("masch", "Sie"), "Bold", 32),
    *neinz("nur Fertigung unterbrochen: keine Eigentumsverletzung", 395, beim("bgh1", "keine"), "Bold", 30, x=160),
    zit("BGH, Urt. v. 13.4.2023 – III ZR 215/21, Rn. 44", 160, 445, beim("bgh1", "keine")),
    *neinz("Nutzung: nur bei unmittelbarer Einwirkung auf die Sache", 505, beim("nutz", "unmittelbare"), "Bold", 30, x=160),
    zit("BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 18", 160, 555, beim("nutz", "unmittelbare")),
    z("Der Bagger hat die Maschinen nie berührt.", 160, 610, "nutz2", size=30),
    blk(110, 680, 1040, 80, ROT, "eigerg", [("Eigentum der Fabrik: nicht verletzt", "ExtraBold", 34, INK)]),
    *requisit([("eig", ("tabler", "settings", 100, GELB), "Eigentum", GELB),
               ("kabel", ("tabler", "plug-off", 100, HELLGRAU), "Kabel: Netzbetreiber", WEISS),
               ("masch", ("tabler", "settings", 100, GRUEN), "unversehrt", HELLGRUEN),
               ("bgh1", ("tabler", "clock-pause", 100, WEISS), "Fertigung unterbrochen", HELLROT),
               ("nutz2", ("tabler", "backhoe", 190, GELB), "nie berührt", WEISS),
               ("eigerg", ("tabler", "settings", 100, GRUEN), "nicht verletzt", HELLROT)]),
    *zwei([("eig", "ernst"), ("netzan", "froh"), ("eigerg", "ruhig")],
          [("eig", "skeptisch"), ("netzan", "wut"), ("bgh1", "sorge"), ("eigerg", "muede")]),
]))

# ===========================================================================================================================
# G Gegenfall: Substanzschaden
# ===========================================================================================================================
PG = "Gegenfall · Substanzschaden"
folie([("gegen", PG), ("gg1", f"{PG} › Asphaltmischwerk"), ("gg2", f"{PG} › Eigentum (+), Folgeschäden"),
       ("gg3", f"{PG} › Ware verdirbt")], rechts_frei([
    *tafel("gegen", "Gegenfall: Sachen beschädigt"),
    blk(110, 180, 1040, 80, HELL, "gegen", [("Stromausfall beschädigt Sachen der Fabrik?", "ExtraBold", 32, INK)]),
    z("Asphaltmischwerk: Ausfall nach Kabelschaden", 110, 300, "gg1", "Bold", 32),
    z("beschädigte die Anlagensteuerung", 110, 345, beim("gg1", "Anlagensteuerung"), "Bold", 32),
    zit("BGH, Urt. v. 13.4.2023 – III ZR 215/21, Rn. 7, 41", 110, 392, beim("gg1", "Anlagensteuerung")),
    *okz("Eigentum verletzt", 455, beim("gg2", "Eigentum"), "Bold", 32, x=160),
    *okz("ersetzt auch: Folgeschäden des Stillstands", 515, beim("gg2", "Folgeschäden"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 13.4.2023 – III ZR 215/21, Rn. 44", 160, 565, beim("gg2", "Folgeschäden")),
    *okz("ebenso: Sachen gehen unter, z. B. Ware verdirbt", 630, beim("gg3", "Sachen"), "Bold", 32, x=160),
    *requisit([("gegen", ("tabler", "bolt-off", 100, HELLGRAU), "Stromausfall", WEISS),
               ("gg1", ("tabler", "cpu", 100, HELLROT), "Anlagensteuerung beschädigt", HELLROT),
               ("gg2", ("tabler", "receipt-euro", 100, WEISS), "Folgeschäden", HELLGRUEN),
               ("gg3", ("tabler", "package-off", 100, HELLROT), "Ware verdorben", HELLROT)]),
    *zwei([("gegen", "denkt"), ("gg2", "sorge")], [("gegen", "skeptisch"), ("gg2", "ernst")]),
]))

# ===========================================================================================================================
# H II. Gewerbebetrieb: Begriff, Auffangtatbestand, Betriebsbezogenheit
# ===========================================================================================================================
PW = "II. Gewerbebetrieb"
folie([("gew", PW), ("sonst", f"{PW} › sonstiges Recht"), ("auff", f"{PW} › Auffangtatbestand"),
       ("bez", f"{PW} › betriebsbezogener Eingriff")], rechts_frei([
    *tafel("gew", "II. Recht am Gewerbebetrieb"),
    z("Recht am eingerichteten und ausgeübten", 110, 180, "gew", "Bold", 32),
    z("Gewerbebetrieb", 110, 225, "gew", "Bold", 32),
    *okz("sonstiges Recht im Sinne von § 823 Abs. 1 BGB", 290, beim("sonst", "sonstiges"), "Bold", 30, x=160),
    zit("BGH, Urt. v. 6.2.2014 – I ZR 75/13, Rn. 12", 160, 340, beim("sonst", "sonstiges")),
    blk(110, 395, 1040, 130, HELL, "auff", [("Auffangtatbestand: schließt nur Schutzlücken,", "Bold", 30, INK),
                                          ("kein Schutz, wo das Gesetz ihn verwehrt", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 3.6.2020 – XIII ZR 22/19, Rn. 22", 110, 540, beim("auff", "Schutzlücken")),
    blk(110, 600, 1040, 130, GELB, "bez", [("betriebsbezogen: unmittelbar gegen den", "ExtraBold", 32, INK),
                                         ("Betrieb als solchen gerichtet", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 20", 110, 745, beim("bez", "betriebsbezogen")),
    *requisit([("gew", ("tabler", "building-factory-2", 160, BLAU), "Gewerbebetrieb", BLAU),
               ("sonst", ("tabler", "book", 100, WEISS), "sonstiges Recht", WEISS),
               ("auff", ("tabler", "shield-check", 100, GRUEN), "nur Auffangtatbestand", WEISS),
               ("bez", ("tabler", "target", 100, WEISS), "betriebsbezogen?", GELB)]),
    *zwei([("gew", "ruhig"), ("auff", "denkt")], [("gew", "ernst"), ("bez", "skeptisch")]),
]))


# ===========================================================================================================================
# I Betriebsbezogenheit im Fall: das Kabel versorgt das ganze Gewerbegebiet
# ===========================================================================================================================
def netzbild(y, cue):
    """Kabel mit vier Abnehmern im Gewerbegebiet; alle ohne Strom (Tabler-Icons, programmatische Leitung)."""
    els = [linienzug([(150, y + 150), (1120, y + 150)], cue, breite=12, farbe=KABEL)]
    for i, (x, ic, br, f_) in enumerate([(300, "building-store", 150, ROT), (530, "building-factory-2", 210, BLAU),
                                         (770, "building-warehouse", 160, LILA), (990, "building", 120, GRUEN)]):
        els.append(linienzug([(x, y + 150), (x, y + 112)], cue, breite=8, farbe=KABEL))
        els.append(ficon("tabler", ic, x, y + 112, br, cue, fuell=f_))
    els.append(ficon("tabler", "backhoe", 170, y + 100, 120, cue, fuell=GELB))
    return els


PB = "II. Gewerbebetrieb › im Fall"
NY = 255
folie([("subs", PB), ("zuf", f"{PB} › rein zufällig getroffen"), ("bgh2", "II. Gewerbebetrieb › Stromkabel-Fall: nicht betriebsbezogen")],
      [*tafel("subs", "Im Fall: betriebsbezogen?"),
    *netzbild(NY, "subs"),          # Schaubild in der Tafel (bewusst links)
    *[ficon("tabler", "bolt-off", x + 34, NY + 146, 36, beim("zuf", "Ausfall"), fuell=HELLGRAU) for x in (300, 530, 770, 990)],
    *rechts_frei([
    pl("2 km", 370, NY + 175, beim("subs", "zwei"), fill=GELB, size=28),
    pl("ganzes Gewerbegebiet am Kabel", 520, NY + 175, beim("subs", "Gewerbegebiet"), fill=WEISS, size=28),
    z("Ausfall traf die Fabrik rein zufällig,", 110, NY + 260, beim("zuf", "zufällig"), "Bold", 32),
    z("wie jeden anderen Abnehmer", 110, NY + 305, beim("zuf", "jeden"), "Bold", 32),
    zit("BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 20", 110, NY + 352, beim("zuf", "jeden")),
    *neinz("kein betriebsbezogener Eingriff", NY + 420, beim("bgh2", "kein"), "ExtraBold", 34, x=160),
    zit("Stromkabel-Fall: BGH, Urt. v. 9.12.1958 – VI ZR 199/57, BGHZ 29, 65", 160, NY + 475, beim("bgh2", "kein")),
    blk(110, NY + 540, 1040, 80, ROT, beim("bgh2", "kein"), [("Gewerbebetrieb: nicht verletzt", "ExtraBold", 34, INK)]),
    *requisit([("subs", ("tabler", "plug-off", 100, HELLGRAU), "ganzes Gewerbegebiet", WEISS),
               ("zuf", ("tabler", "users-group", 110, BLAU), "wie jeder Abnehmer", WEISS),
               ("bgh2", ("tabler", "gavel", 100, HOLZ), "BGHZ 29, 65", WEISS)]),
    *zwei([("subs", "ernst"), ("bgh2", "froh")], [("subs", "skeptisch"), ("zuf", "sorge"), ("bgh2", "muede")]),
])])
assert NY + 620 <= 900

# ===========================================================================================================================
# J § 823 Abs. 2 BGB (ein Satz, Verweis Folge 158)
# ===========================================================================================================================
folie([("abs2", "§ 823 Abs. 2 BGB · Schutzgesetz?")], rechts_frei([
    *tafel("abs2", "Und § 823 Abs. 2 BGB?"),
    z("nur, wenn Fiete ein Schutzgesetz verletzt hätte,", 110, 190, beim("abs2", "Fiete"), "Bold", 32),
    z("das gerade auch das Vermögen der Fabrik schützt", 110, 235, beim("abs2", "Vermögen"), "Bold", 32),
    zit("BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 10 f.", 110, 285, beim("abs2", "Vermögen")),
    *neinz("hier nicht ersichtlich", 350, beim("abs2", "ersichtlich"), "ExtraBold", 34, x=160),
    z("mehr: Video „Schutzgesetz“", 110, 420, beim("abs2", "mehr"), "Bold", 30, farbe=TEXT),
    *requisit([("abs2", ("tabler", "book", 100, WEISS), "Schutzgesetz?", GELB)]),
    *zwei([("abs2", "denkt")], [("abs2", "skeptisch")]),
]))

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Gotthard gegen Fiete"), ("erg2", "Ergebnis › Netzbetreiber gegen Fiete"),
       ("erg3", "Ergebnis › anders bei Substanzschaden"), ("vertrag", "Ergebnis › gegen den Netzbetreiber: eigene Frage")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 130, ROT, "erg", [("Gotthard gegen Fiete aus § 823 BGB:", "ExtraBold", 34, INK),
                                        ("kein Ersatz der 48.000 €", "ExtraBold", 34, INK)]),
    *okz("Fiete haftet dem Netzbetreiber für das Kabel", 360, beim("erg2", "Netzbetreiber"), "Bold", 32, x=160),
    z("anders bei beschädigten Maschinen", 160, 430, "erg3", "Bold", 32),
    z("oder verdorbener Ware", 160, 475, beim("erg3", "Ware"), "Bold", 32),
    z("Ansprüche gegen den Netzbetreiber: eigene Frage", 110, 560, "vertrag", "Bold", 30, farbe=TEXT),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", WEISS),
               ("erg2", ("tabler", "plug-off", 100, HELLGRAU), "Kabel", WEISS),
               ("erg3", ("tabler", "package-off", 100, HELLROT), "beschädigte Sachen", HELLGRUEN),
               ("vertrag", ("tabler", "building", 100, GRUEN), "Netzbetreiber", WEISS)]),
    *zwei([("erg", "froh"), ("erg3", "ernst")], [("erg", "wut"), ("erg2", "muede"), ("vertrag", "still")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst die Rechtsgüter"), ("tp2", "Klausurtipp · Gewerbebetrieb nur subsidiär"),
       ("tp3", "Klausurtipp · Betriebsbezogenheit entscheidet")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst die genannten Rechtsgüter,", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("vor allem das Eigentum", 200, 260, beim("tipp", "Eigentum"), size=34),
    z("Dann erst der Gewerbebetrieb:", 200, 345, "tp2", "Bold", 36),
    z("nur Auffangtatbestand", 200, 405, beim("tp2", "Auffangtatbestand"), size=34),
    linienzug([(130, 485), (1130, 485)], "tp3", breite=3),
    z("Dort entscheidet die Betriebsbezogenheit,", 200, 515, beim("tp3", "Betriebsbezogenheit"), "Bold", 36),
    z("nicht die Höhe des Schadens", 200, 575, beim("tp3", "Höhe"), size=34),
    zit("BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 14, 20", 200, 625, beim("tp3", "Höhe")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Eigentum", True),
          ("c1", 1, "Substanzschaden oder Nutzungsbeeinträchtigung durch Einwirkung auf die Sache", False),
          ("c2", 0, "II. Recht am Gewerbebetrieb (subsidiär)", True),
          ("c2", 1, "nur bei betriebsbezogenem Eingriff", False),
          ("c3", 0, "III. Reines Vermögen: andere Grundlagen", True),
          ("c3", 1, "vor allem § 823 Abs. 2 BGB mit Schutzgesetz und § 826 BGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Rechtsgutsverletzung beim Stromausfall"), 110, 90, "sch", 46),
           z("§ 823 Abs. 1 BGB, erstes Merkmal; übriges Schema: Video „Deliktsrecht“", 110, 160, "sch", "Bold", 32, farbe=TEXT,
             rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 80, 1: 100}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Eigentum"), ("c2", "Prüfschema › II. Gewerbebetrieb"),
       ("c3", "Prüfschema › III. reines Vermögen")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer nur Geld verliert, ohne dass", 0)], [("ein ", 0), ("geschütztes Recht", "a"), (" verletzt ist,", 0)],
                 [("bekommt aus § 823 Abs. 1 BGB nichts.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "geschütztes")}),
    *markertext([[("Der Gewerbebetrieb ist nur bei einem", 0)], [("betriebsbezogenen", "b"), (" Eingriff verletzt.", 0)]],
                750, 600, 44, "m2", {"b": beim("m2", "betriebsbezogenen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
