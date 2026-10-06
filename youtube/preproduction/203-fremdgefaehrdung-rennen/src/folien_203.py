"""Folge 203 · Einverständliche Fremdgefährdung: Beifahrer beim Straßenrennen – Serienstandard Open Peeps (Katzenkönig).
Fall: Samstag, 1:10 Uhr. Hilmar (Anfang 50) fährt mit seinem jungen Kollegen Eike als Beifahrer auf einer Landstraße ein
Rennen gegen einen zweiten Wagen; beide nüchtern, beide kennen die Gefahr. Eike feuert an. Erlaubt 100 km/h, Hilmar fast
190 km/h; in einer Kurve verliert er die Kontrolle, der Wagen kommt von der Straße ab, Eike stirbt, Hilmar überlebt verletzt.
Szenen laut ../SZENENPLAN.md: A1 Parkplatz (Nacht), A2 Landstraße (Nacht, Rennen, Frage), B Sachverhalt, C echter Fall
(BGHSt 53, 55; nur Icons), D § 222 (Wortlaut), E1/E2 Zurechnung: Selbst- oder Fremdgefährdung, Tatherrschaft, F1 im Fall,
F2 Gegenansicht, G1 Einwilligung/§ 228 (Wortlaut), G2 Grenze konkrete Todesgefahr, G3 Ergebnis, H § 315d (Wortlaut,
Auszug), I Klausurtipp (Lexi, Prüfungsreihenfolge Schritt für Schritt), J Merksatz (Lexi).
Darstellung zurückhaltend: kein Aufprall, kein Blut, keine Verletzten im Bild, keine echten Automarken (Phosphor
car-profile), keine Raser-Verherrlichung; der Unfall nur über Kurvenschild, Warndreieck und Blaulicht. Personen fiktiv.
Nacht nur in den beiden Fallszenen (Hook: nächtliches Rennen), sonst Cremegrund.
Handlungsgeräusch: Motor (A2, die Wagen starten); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 198 (gemeinsame Dateien unverändert); neu: nachtfolie(), auto(), strasse().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (StGB), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_203/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_203/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
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




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in der Parkplatzszene
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (Fall verlangt die Nacht)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)
LINIE = (225, 228, 240, 255)                 # helle Linien auf dem Nachtgrund
NACHTGRAU = (78, 92, 150, 255)
FE = "fluent-emoji-high-contrast"
X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HI": "Hilmar", "EI": "Eike"}
NFARBE = {"HI": ORANGE, "EI": BLAU}


def nachtfolie(pfade, els):
    """Fallszene bei Nacht (Hook: nächtliches Rennen); Prüfung wie bausteine.folie."""
    bausteine.pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


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


def zwei(folge_hi, folge_ei):
    """Hilmar und Eike rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HI", X1, folge_hi), *stehend("EI", X2, folge_ei)]


def auto(c, cx, unten, breite, farbe, bis=None, spiegeln=False, anim="cut"):
    """Wagen ohne Marke: Phosphor car-profile (MIT), Palettenfüllung."""
    return ficon("ph", "car-profile", cx, unten, breite, c, fuell=farbe, spiegeln=spiegeln, bis=bis, anim=anim)


def strasse(c, oben=790, mitte=880, unten=990):
    """Landstraße in der Seitenansicht: ferner und naher Rand, gestrichelte Mittellinie (helle Linien auf Nachtgrund)."""
    els = [hart(linienzug([(40, oben), (1880, oben)], c, breite=6, farbe=LINIE)),
           hart(linienzug([(40, unten), (1880, unten)], c, breite=6, farbe=LINIE))]
    for x in range(60, 1860, 150):
        els.append(hart(linienzug([(x, mitte), (x + 80, mitte)], c, breite=6, farbe=LINIE)))
    return els


# ===========================================================================================================================
# A1 Fall: der Parkplatz am Stadtrand (Samstag, 1:10 Uhr, Nacht)
# ===========================================================================================================================
HIX, EIX, AUX, GEX = 400, 1300, 850, 1660
lat, lkopf = laterne(1060, BODEN_Y, 560, NULL)
lat = hart(lat)
nachtfolie([(NULL, "Fall · Samstag, 1:10 Uhr: ein Parkplatz am Stadtrand"), ("hilmar", "Fall · Hilmar und sein Wagen"),
            ("eike", "Fall · Eike fährt als Beifahrer mit"), ("gegner", "Fall · Ein Rennen gegen einen 2. Wagen"),
            ("wissen", "Fall · Beide kennen die Gefahr"), ("e1", "Fall · Eike feuert Hilmar an"),
            ("h1", "Fall · Hilmar: „Halt dich fest!“")], [
    hart(lichtkegel(lkopf[0], lkopf[1], 330, BODEN_Y, NULL)),
    lat,
    hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], NULL, breite=7, farbe=LINIE)),
    hart(mond(1770, 150, 46, NULL)),
    hart(ficon("tabler", "parking", 150, BODEN_Y, 110, NULL, fuell=BLAU, anim="cut")),
    hart(pl("Samstag, 1:10 Uhr", 70, 30, NULL, fill=LILA, size=38)),
    hart(pl("leerer Parkplatz am Stadtrand", 70, 100, NULL, fill=WEISS, size=30, bis="e1")),
    auto(NULL, AUX, BODEN_Y, 430, ROT),
    pl("Hilmar, Anfang 50: Wagen auf Tempo getrimmt", 70, 165, "hilmar", fill=ORANGE, size=30, bis="e1"),
    ficon("ph", "speedometer", AUX, 640, 90, beim("hilmar", "Tempo"), fuell=WEISS, bis="e1"),
    pl("Eike, junger Kollege: Beifahrer", 70, 230, "eike", fill=BLAU, size=30, bis="e1"),
    auto("gegner", GEX, BODEN_Y, 380, BLAU, spiegeln=True, anim="pop"),
    pl("Rennen gegen einen 2. Wagen", 70, 295, "gegner", fill=WEISS, size=30, bis="e1"),
    pl("beide nüchtern, kennen die Gefahr", 70, 360, "wissen", fill=GELB, size=30, bis="e1"),
    ficon(FE, "warning", 690, 420, 70, beim("wissen", "gefährlich"), fuell=GELB, bis="e1"),
    *fig("HI", HIX, BODEN_Y, FHA, [("hilmar", "ruhig_r"), ("eike", "entschl_r"), ("e1", "ruhig_r")], bis="h1"),
    ns(NAME["HI"], HIX, BODEN_Y, "hilmar", NFARBE["HI"], d=0.1),
    *redet("HI_redet_r", HIX, BODEN_Y, FHA, "h1", "start"),
    *fig("EI", EIX, BODEN_Y, FHA, [("eike", "froh"), ("wissen", "ruhig")], bis="e1"),
    *redet("EI_redet", EIX, BODEN_Y, FHA, "e1", "h1"),
    *fig("EI", EIX, BODEN_Y, FHA, [("h1", "begeistert")], erst="cut"),
    ns(NAME["EI"], EIX, BODEN_Y, "eike", NFARBE["EI"], d=0.1),
    blase("sprech", 700, 190, "e1", 1180, 240, inhalt=["Los, Hilmar, gib Gas!", "Den hängen wir ab!"], textsize=38,
          figur=("EI_redet", EIX, BODEN_Y, FHA), bis="h1"),
    blase("sprech", 440, 150, "h1", 560, 270, inhalt=["Halt dich fest!"], textsize=40,
          figur=("HI_redet_r", HIX, BODEN_Y, FHA)),
])

# ===========================================================================================================================
# A2 Fall: das Rennen auf der Landstraße (Nacht) und die Frage – kein Aufprall, keine Verletzten im Bild
# ===========================================================================================================================
RU, BU = 975, 870                            # Unterkante roter Wagen (naher Fahrstreifen), blauer Wagen (ferner)
KURVE = 1500
nachtfolie([("start", "Fall · Das Rennen auf der Landstraße"), ("tempo", "Fall · Erlaubt: 100 km/h – Hilmar: fast 190"),
            ("anfeuern", "Fall · Eike feuert Hilmar weiter an"), ("kurve", "Fall · In der Kurve: Kontrolle verloren"),
            ("ab", "Fall · Der Wagen kommt von der Straße ab"), ("stirbt", "Fall · Eike stirbt, Hilmar überlebt verletzt"),
            ("frage", "Fall · Fahrlässige Tötung durch Hilmar?"), ("frage2", "Fall · Oder: Selbstgefährdung von Eike?")], [
    hart(mond(1770, 150, 46, "start")),
    *strasse("start"),
    *[hart(ficon(FE, "evergreen-tree", x, 790, w, "start", fuell=GRUEN, anim="cut")) for x, w in
      ((180, 120), (420, 150), (700, 110), (1000, 140), (1250, 115), (1750, 135))],
    szene(bewegt(auto("start", 520, RU, 400, ROT, bis="tempo"), ("start", 0.0), beim("start", "nebeneinander", ende=True), -280),
          "203motor_1", 1.0, 0.0),
    bewegt(auto("start", 470, BU, 330, BLAU, bis="tempo"), ("start", 0.0), beim("start", "nebeneinander", ende=True), -265),
    pl("Start nebeneinander", 70, 30, beim("start", "starten"), fill=WEISS, size=34, bis="ab"),
    bewegt(auto("tempo", 940, RU, 400, ROT, bis="kurve"), ("tempo", 0.0), beim("tempo", "Hilmar"), -420),
    bewegt(auto("tempo", 980, BU, 330, BLAU, bis="kurve"), ("tempo", 0.0), beim("tempo", "Hilmar"), -510),
    pl("erlaubt: 100 km/h", 70, 110, "tempo", fill=WEISS, size=34),
    pl("Hilmar: fast 190 km/h", 400, 110, beim("tempo", "Hilmar"), fill=ROT, size=34),
    pl("Eike feuert ihn weiter an", 70, 190, "anfeuern", fill=BLAU, size=34, bis="stirbt"),
    hart(ficon("tabler", "road-sign", KURVE, 790, 120, "kurve", fuell=GELB, anim="cut")),
    bewegt(auto("kurve", 1300, RU, 400, ROT, bis="ab"), ("kurve", 0.0), beim("kurve", "verliert"), -360),
    bewegt(auto("kurve", 1720, BU, 330, BLAU, bis="ab"), ("kurve", 0.0), beim("kurve", "verliert"), -740),
    pl("Kurve: Hilmar verliert die Kontrolle", 70, 270, beim("kurve", "verliert"), fill=GELB, size=34),
    ficon(FE, "warning", 1300, RU, 150, "ab", fuell=GELB),
    pl("Wagen kommt von der Straße ab", 70, 350, "ab", fill=WEISS, size=34),
    ficon(FE, "police-car-light", 1080, RU, 110, "stirbt", fuell=ROT),
    pl("Eike stirbt an der Unfallstelle", 70, 430, "stirbt", fill=HELLGRAU, size=34),
    pl("Hilmar überlebt verletzt", 70, 510, beim("stirbt", "Hilmar"), fill=HELLGRAU, size=34),
    pl("Fahrlässige Tötung durch Hilmar?", 960, 30, "frage", fill=PINK, size=36),
    pl("Oder: Selbstgefährdung von Eike?", 960, 110, "frage2", fill=GELB, size=36),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_203(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_203("sv", [
    "Samstag, 1:10 Uhr: Hilmar (Anfang 50) hat seinen Wagen auf Tempo getrimmt. Mit seinem jungen Kollegen Eike als "
    "Beifahrer will er auf einer Landstraße gegen einen zweiten Wagen ein Rennen fahren. Beide sind nüchtern und wissen, "
    "wie gefährlich das ist.",
    "Eike: „Los, Hilmar, gib Gas! Den hängen wir ab!“ Hilmar: „Halt dich fest!“",
    "Die Wagen starten nebeneinander. Erlaubt sind 100 km/h, Hilmar fährt fast 190 km/h; Eike feuert ihn weiter an. In "
    "einer Kurve verliert Hilmar die Kontrolle, der Wagen kommt von der Straße ab. Eike stirbt noch an der Unfallstelle, "
    "Hilmar überlebt verletzt.",
], "Hat sich Hilmar wegen fahrlässiger Tötung strafbar gemacht?")

# ===========================================================================================================================
# C Der echte Fall: BGHSt 53, 55 (nur Icons, keine Figuren – reale Beteiligte werden nicht dargestellt)
# ===========================================================================================================================
PE = "Der echte Fall · BGHSt 53, 55"
folie([("bgh", f"{PE}"), ("bgh2", f"{PE} › Beschleunigungstests"), ("bgh3", f"{PE} › Überholen eines 3. Autos"),
       ("bgh4", f"{PE} › LG: § 315c – BGH: auch § 222")], rechts_frei([
    *tafel("bgh", "Der echte Fall: BGHSt 53, 55"),
    zit("BGH, Urt. v. 20.11.2008 – 4 StR 328/08", 110, 180, beim("bgh", "Urteil")),
    ficon(FE, "classical-building", PX, 380, 120, beim("bgh", "Urteil"), fuell=BLAU, bis="bgh2"),
    pl("BGH, 20.11.2008", PX, PY, beim("bgh", "Urteil"), fill=BLAU, size=28, anker="m", bis="bgh2"),
    z("2 Wagen: „Beschleunigungstests“ auf einer Bundesstraße", 110, 250, "bgh2", "Bold", 32),
    z("Beifahrer (der spätere Tote): Startzeichen, filmte", 110, 310, beim("bgh2", "Der"), "Bold", 32),
    z("gleichzeitiges Überholen eines 3. Autos:", 110, 380, "bgh3", "Bold", 32),
    z("Wagen kommt von der Fahrbahn ab", 110, 425, beim("bgh3", "kam"), "Bold", 32),
    zit("BGH 4 StR 328/08, Rn. 7–10", 110, 480, beim("bgh3", "kam")),
    *neinz("Landgericht: nur Gefährdung des Straßenverkehrs", 560, "bgh4", "Bold", 32, x=170),
    *okz("BGH: zusätzlich fahrlässige Tötung, § 222 StGB", 620, beim("bgh4", "Bundesgerichtshof"), "ExtraBold", 32, x=170),
    zit("Tenor; BGH 4 StR 328/08, Rn. 12", 170, 680, beim("bgh4", "Bundesgerichtshof")),
    auto("bgh2", PX, 640, 330, ROT, anim="pop"),
    auto("bgh2", PX, 840, 330, BLAU, anim="pop"),
    pl("Beschleunigungstests", PX, PY, "bgh2", fill=WEISS, size=28, anker="m", bis="bgh3"),
    ficon(FE, "video-camera", PX, 380, 100, beim("bgh2", "filmte"), fuell=WEISS, bis="bgh3"),
    ficon(FE, "warning", PX, 380, 110, "bgh3", fuell=GELB, bis="bgh4"),
    pl("Überholen", PX, PY, "bgh3", fill=GELB, size=28, anker="m", bis="bgh4"),
    ficon(FE, "balance-scale", PX, 380, 110, "bgh4", fuell=GELB),
    pl("§ 222 StGB (+)", PX, PY, beim("bgh4", "Bundesgerichtshof"), fill=GRUEN, size=28, anker="m"),
]))

# ===========================================================================================================================
# D Fahrlässige Tötung, § 222 StGB (Wortlaut), Tatbestand unproblematisch
# ===========================================================================================================================
PT = "A. Hilmar: § 222 StGB"
W222 = "„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“"
w222, w222_y = wortlaut(80, 175, 1100, W222, "§ 222 StGB", "p222", marken=[
    ("Fahrlässigkeit", beim("p222", "Fahrlässigkeit")), ("Tod eines Menschen verursacht", beim("p222", "Tod"))], size=32)
folie([("p222", f"{PT} › Wortlaut"), ("erfolg", f"{PT} › Erfolg und Kausalität"), ("pflicht", f"{PT} › Sorgfaltspflichtverletzung"),
       ("vorh", f"{PT} › Vorhersehbarkeit"), ("unpro", f"{PT} › bis hierhin unproblematisch")], rechts_frei([
    *tafel("p222", "Fahrlässige Tötung, § 222 StGB"),
    *w222,
    *okz("Erfolg: Eike ist tot", w222_y + 40, "erfolg", "Bold", 32, x=170),
    *okz("Kausalität: ohne das Rennen nicht gestorben", w222_y + 95, beim("erfolg", "ohne"), "Bold", 32, x=170),
    *okz("Sorgfaltspflicht verletzt: viel zu schnell", w222_y + 150, "pflicht", "Bold", 32, x=170),
    *okz("tödlicher Unfall vorhersehbar", w222_y + 205, "vorh", "Bold", 32, x=170),
    pl("bis hierhin unproblematisch", 110, w222_y + 280, "unpro", fill=GRUEN, size=32),
    *requisit([("p222", (FE, "balance-scale", 110, GELB), "§ 222 StGB", GELB),
               ("pflicht", ("ph", "speedometer", 110, ROT), "fast 190 km/h", ROT),
               ("unpro", (FE, "balance-scale", 110, GRUEN), "Tatbestand (+)", GRUEN)]),
    *stehend("HI", FX, [("p222", "ernst"), ("pflicht", "still"), ("unpro", "ernst")]),
]))
assert w222_y + 350 <= 900, w222_y

# ===========================================================================================================================
# E1 Zurechnung: Selbstgefährdung oder einverständliche Fremdgefährdung?
# ===========================================================================================================================
PZ = "A. Hilmar › Zurechnung"
folie([("problem", f"{PZ}: das Problem"), ("selbst", f"{PZ} › eigenverantwortliche Selbstgefährdung?"),
       ("v058", f"{PZ} › Selbstgefährdung: Heroinspritzen-Fall"), ("fremd", f"{PZ} › einverständliche Fremdgefährdung?")],
      rechts_frei([
    *tafel("problem", "Selbst- oder Fremdgefährdung?"),
    pl("Problem: die Zurechnung", 110, 180, beim("problem", "Zurechnung"), fill=GELB, size=32),
    blk(110, 260, 1040, 175, GRUEN, "selbst", [("eigenverantwortliche Selbstgefährdung:", "ExtraBold", 32, INK),
                                              ("nur veranlasst, ermöglicht oder gefördert", "Bold", 30, INK),
                                              ("Veranlasser: grundsätzlich nicht strafbar", "Bold", 30, INK)]),
    zit("BGH 4 StR 328/08, Rn. 21", 130, 450, beim("selbst", "grundsätzlich")),
    pl("kennst du: Folge zum Heroinspritzen-Fall", 110, 510, "v058", fill=WEISS, size=28),
    blk(110, 600, 1040, 130, HELLROT, "fremd", [("einverständliche Fremdgefährdung:", "ExtraBold", 32, INK),
                                               ("ein anderer gefährdet das Opfer, Opfer einverstanden", "Bold", 30, INK)]),
    *requisit([("problem", (FE, "white-question-mark", 80, WEISS), "zurechenbar?", WEISS),
               ("selbst", None, "selbst?", GRUEN),
               ("fremd", None, "fremd?", HELLROT)]),
    *zwei([("problem", "ernst"), ("fremd", "denkt")], [("problem", "ruhig"), ("selbst", "denkt"), ("fremd", "ernst")]),
]))

# ===========================================================================================================================
# E2 Abgrenzungskriterium: Tatherrschaft über die gefährdende Handlung
# ===========================================================================================================================
folie([("krit", f"{PZ} › Abgrenzung: Tatherrschaft"), ("auch", f"{PZ} › auch beim Fahrlässigkeitsdelikt"),
       ("unmittel", f"{PZ} › wer beherrscht das unmittelbare Geschehen?")], rechts_frei([
    *tafel("krit", "Abgrenzung: die Tatherrschaft"),
    blk(110, 180, 1040, 130, BLAU, beim("krit", "Der"), [("Tatherrschaft über die gefährdende Handlung", "ExtraBold", 32, INK),
                                                        ("wie bei Täterschaft und Teilnahme", "Bold", 30, INK)]),
    zit("BGH 4 StR 328/08, Rn. 22", 130, 325, beim("krit", "Täterschaft")),
    *okz("gilt auch beim Fahrlässigkeitsdelikt", 400, "auch", "Bold", 32, x=170),
    blk(110, 480, 1040, 130, GELB, "unmittel", [("besonders wichtig: Wer beherrscht das Geschehen,", "ExtraBold", 30, INK),
                                              ("das unmittelbar zum Erfolg führt?", "ExtraBold", 30, INK)]),
    zit("BGH 4 StR 328/08, Rn. 23", 130, 625, beim("unmittel", "unmittelbar")),
    *requisit([("krit", (FE, "crown", 110, GELB), "Tatherrschaft?", GELB),
               ("unmittel", ("ph", "steering-wheel", 110, WEISS), "unmittelbares Geschehen", WEISS)]),
    *zwei([("krit", "denkt"), ("unmittel", "ruhig")], [("krit", "ruhig"), ("auch", "denkt")]),
]))

# ===========================================================================================================================
# F1 Im Fall: Hilmar beherrscht das Geschehen – einverständliche Fremdgefährdung
# ===========================================================================================================================
PF = "A. Hilmar › Zurechnung › im Fall"
folie([("hier", f"{PF}: Hilmar am Steuer"), ("lenk", f"{PF}: Geschwindigkeit und Lenkung"),
       ("ausgesetzt", f"{PF}: Eike nur ausgesetzt"), ("anf", f"{PF}: Anfeuern untergeordnet"),
       ("fg", f"{PF}: einverständliche Fremdgefährdung (+)")], rechts_frei([
    *tafel("hier", "Im Fall: Wer beherrscht das Geschehen?", size=44),
    z("Hilmar sitzt am Steuer", 110, 180, "hier", "ExtraBold", 34),
    *okz("allein er bestimmt Geschwindigkeit und Lenkung", 245, "lenk", "Bold", 32, x=170),
    *neinz("Eike kann die Gefahr nicht selbst abwenden,", 310, "ausgesetzt", "Bold", 32, x=170),
    z("ist dem Fahrverhalten nur ausgesetzt", 170, 355, beim("ausgesetzt", "er"), "Bold", 32),
    z("Anfeuern: nur untergeordnete Bedeutung –", 170, 425, "anf", "Bold", 32),
    z("wie Startzeichen und Filmen im echten Fall", 170, 470, beim("anf", "wie"), "Bold", 32),
    zit("BGH 4 StR 328/08, Rn. 24", 170, 525, beim("anf", "wie")),
    blk(110, 600, 1040, 130, GRUEN, "fg", [("einverständliche Fremdgefährdung:", "ExtraBold", 32, INK),
                                          ("der Tod ist Hilmar zuzurechnen", "Bold", 30, INK)]),
    *requisit([("hier", ("ph", "steering-wheel", 110, WEISS), "am Steuer: Hilmar", ORANGE),
               ("lenk", (FE, "crown", 110, GELB), "Tatherrschaft: Hilmar", ORANGE),
               ("ausgesetzt", ("ph", "seat", 100, BLAU), "Eike: ausgesetzt", BLAU),
               ("fg", (FE, "balance-scale", 110, GRUEN), "zurechenbar (+)", GRUEN)]),
    *zwei([("hier", "entschl"), ("ausgesetzt", "ernst"), ("fg", "still")], [("hier", "ruhig"), ("ausgesetzt", "ernst"),
                                                                          ("anf", "denkt")]),
]))

# ===========================================================================================================================
# F2 Gegenansicht (ein Satz): Gleichstellung mit der Selbstgefährdung (etwa Roxin) – vom BGH abgelehnt
# ===========================================================================================================================
folie([("roxin", "A. Hilmar › Zurechnung › Gegenansicht: Gleichstellung?")], rechts_frei([
    *tafel("roxin", "Gegenansicht"),
    blk(110, 180, 1040, 130, LILA, beim("roxin", "Ein"), [("Teil der Lehre (etwa Roxin): manche Fremd-", "ExtraBold", 32, INK),
                                                         ("gefährdungen der Selbstgefährdung gleichstellen", "Bold", 30, INK)]),
    *neinz("BGH: hier nicht – es zählt die tatsächliche", 350, beim("roxin", "Bundesgerichtshof"), "Bold", 32, x=170),
    z("Situation beim Unfall, nicht, wer zufällig", 170, 395, beim("roxin", "Situation"), "Bold", 32),
    z("am Steuer saß", 170, 440, beim("roxin", "Situation"), "Bold", 32),
    zit("BGH 4 StR 328/08, Rn. 25 (mit Nachweisen zu Roxin)", 170, 495, beim("roxin", "zufällig")),
    *requisit([("roxin", (FE, "balance-scale", 110, LILA), "Gleichstellung?", LILA),
               (beim("roxin", "Bundesgerichtshof"), ("ph", "steering-wheel", 110, WEISS), "Situation beim Unfall", WEISS)]),
    *zwei([("roxin", "denkt")], [("roxin", "ruhig")]),
]))

# ===========================================================================================================================
# G1 Rechtswidrigkeit: Einwilligung? § 228 StGB (Wortlaut)
# ===========================================================================================================================
PW = "A. Hilmar › Rechtswidrigkeit: Einwilligung"
W228 = ("„Wer eine Körperverletzung mit Einwilligung der verletzten Person vornimmt, handelt nur dann rechtswidrig, wenn "
        "die Tat trotz der Einwilligung gegen die guten Sitten verstößt.“")
w228, w228_y = wortlaut(80, 330, 1100, W228, "§ 228 StGB", "p228", marken=[
    ("Einwilligung", beim("p228", "Einwilligung")), ("rechtswidrig", beim("p228", "rechtswidrig")),
    ("gegen die guten Sitten verstößt", beim("p228", "gegen"))], size=32)
folie([("einw", f"{PW}?"), ("p228", f"{PW} › Maßstab § 228 StGB")], rechts_frei([
    *tafel("einw", "Rechtswidrigkeit: Einwilligung?"),
    pl("Eike: mit dem Risiko einverstanden", 110, 180, beim("einw", "Eike"), fill=BLAU, size=32),
    pl("rechtfertigt das?", 110, 255, beim("einw", "Rechtfertigt"), fill=PINK, size=32),
    *w228,
    *requisit([("einw", (FE, "handshake", 110, BLAU), "einverstanden", BLAU),
               ("p228", (FE, "balance-scale", 110, GELB), "§ 228 StGB", GELB)]),
    *zwei([("einw", "ruhig"), ("p228", "denkt")], [("einw", "froh"), ("p228", "ruhig")]),
]))
assert w228_y <= 880, w228_y

# ===========================================================================================================================
# G2 Einwilligung bei § 222: rechtfertigend bis zur konkreten Todesgefahr; § 315c anders
# ===========================================================================================================================
PG = "A. Hilmar › Rechtswidrigkeit › Einwilligung bei § 222"
folie([("indiv", f"{PG}: Rechtsgüter des Einzelnen"), ("grenze", f"{PG} › Grenze: konkrete Todesgefahr"),
       ("v157", f"{PG} › Maßstab: Folge verabredete Schlägerei"), ("allg", f"{PG} › anders bei § 315c StGB")], rechts_frei([
    *tafel("indiv", "Einwilligung bei § 222 StGB?"),
    *okz("§ 222 schützt allein Rechtsgüter des Einzelnen", 185, beim("indiv", "Paragraf"), "Bold", 32, x=170),
    *okz("Einwilligung in das Risiko kann rechtfertigen", 240, beim("indiv", "Die"), "Bold", 32, x=170),
    zit("BGH 4 StR 328/08, Rn. 29", 170, 295, beim("indiv", "rechtfertigen")),
    blk(110, 360, 1040, 175, HELLROT, "grenze", [("Grenze: Sittenwidrigkeit", "ExtraBold", 32, INK),
                                                ("jedenfalls bei konkreter Todesgefahr,", "Bold", 30, INK),
                                                ("beurteilt aus der Sicht vor der Tat", "Bold", 30, INK)]),
    zit("BGH 4 StR 328/08, Rn. 28 f. (mit BGHSt 49, 166)", 130, 550, beim("grenze", "Sittenwidrig")),
    pl("mehr: Folge zur verabredeten Schlägerei", 110, 610, "v157", fill=WEISS, size=28),
    *neinz("§ 315c StGB schützt auch die Sicherheit des", 700, "allg", "Bold", 32, x=170),
    z("Verkehrs im Allgemeinen: Einwilligung hilft", 170, 745, beim("allg", "Er"), "Bold", 32),
    z("dort grundsätzlich nicht", 170, 790, beim("allg", "Dort"), "Bold", 32),
    *requisit([("indiv", (FE, "handshake", 110, BLAU), "Einwilligung", BLAU),
               ("grenze", (FE, "warning", 110, GELB), "konkrete Todesgefahr?", HELLROT),
               ("allg", (FE, "vertical-traffic-light", 70, GELB), "Sicherheit des Verkehrs", WEISS)]),
    *stehend("HI", FX, [("indiv", "denkt"), ("grenze", "ernst"), ("allg", "ruhig")]),
]))

# ===========================================================================================================================
# G3 Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · konkrete Todesgefahr"), ("erg2", "Ergebnis · Einwilligung rechtfertigt nicht; Schuld (+)"),
       ("erg3", "Ergebnis · Hilmar: § 222 StGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("fast 190 km/h in eine Kurve auf der Landstraße:", 110, 185, beim("erg", "Mit"), "Bold", 32),
    *okz("konkrete Todesgefahr für Eike", 245, beim("erg", "konkreter"), "ExtraBold", 32, x=170),
    *neinz("die Einwilligung rechtfertigt nicht", 310, "erg2", "Bold", 32, x=170),
    *okz("Schuld: Hilmar konnte die Gefahr erkennen", 375, beim("erg2", "Hilmar"), "Bold", 32, x=170),
    blk(110, 460, 1040, 130, GRUEN, "erg3", [("Hilmar: strafbar wegen fahrlässiger Tötung", "ExtraBold", 34, INK),
                                            ("§ 222 StGB", "Bold", 30, INK)]),
    *requisit([("erg", ("ph", "speedometer", 110, ROT), "fast 190 km/h", ROT),
               ("erg2", (FE, "handshake", 110, BLAU), "Einwilligung (−)", HELLROT),
               ("erg3", (FE, "balance-scale", 110, GRUEN), "§ 222 StGB (+)", GRUEN)]),
    *stehend("HI", FX, [("erg", "ernst"), ("erg3", "still")]),
]))

# ===========================================================================================================================
# H Heute: § 315d StGB (Wortlaut Auszug), seit 13.10.2017
# ===========================================================================================================================
PD = "Ausblick · § 315d StGB"
W315 = ("„(1) Wer im Straßenverkehr … 2. als Kraftfahrzeugführer an einem nicht erlaubten Kraftfahrzeugrennen teilnimmt … "
        "(5) Verursacht der Täter in den Fällen des Absatzes 2 durch die Tat den Tod … eines anderen Menschen …, so ist die "
        "Strafe Freiheitsstrafe von einem Jahr bis zu zehn Jahren …“")
w315, w315_y = wortlaut(80, 330, 1100, W315, "§ 315d Abs. 1 Nr. 2, Abs. 5 StGB (Auszug)", "p315d", marken=[
    ("Kraftfahrzeugrennen", beim("p315d", "Kraftfahrzeugrennen")), ("den Tod", beim("abs5", "Tod")),
    ("einem Jahr bis zu zehn Jahren", beim("abs5", "ein"))], size=30)
folie([("p315d", f"{PD}: verbotenes Kraftfahrzeugrennen"), ("abs5", f"{PD} › Abs. 5: Todesfolge")], rechts_frei([
    *tafel("p315d", "Heute: § 315d StGB"),
    pl("in Kraft seit 13.10.2017", 110, 180, beim("p315d", "Kraft"), fill=GELB, size=30),
    pl("im echten Fall noch nicht anwendbar", 110, 255, beim("p315d", "echten"), fill=WEISS, size=30),
    *w315,
    *requisit([("p315d", ("ph", "car-profile", 140, ROT), "verbotenes Rennen", ROT),
               ("abs5", (FE, "balance-scale", 110, GELB), "1 bis 10 Jahre", GELB)]),
    *stehend("HI", FX, [("p315d", "ernst"), ("abs5", "still")]),
]))
assert w315_y <= 900, w315_y

# ===========================================================================================================================
# I Klausurtipp mit Prüfungsreihenfolge (Lexi), Schritt für Schritt
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: die Prüfungsreihenfolge", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("I. Tatbestand", 200, 200, "k1", "ExtraBold", 34),
         z("Erfolg, Kausalität, Sorgfaltspflichtverletzung,", 230, 250, beim("k1", "Erfolg"), "Bold", 30),
         z("Vorhersehbarkeit", 230, 292, beim("k1", "Vorhersehbarkeit"), "Bold", 30),
         z("Zurechnung: Selbst- oder Fremdgefährdung?", 230, 350, "k2", "ExtraBold", 30),
         z("Wer beherrscht die gefährdende Handlung?", 230, 392, beim("k2", "Frag"), "Bold", 30),
         z("II. Rechtswidrigkeit", 200, 470, "k3", "ExtraBold", 34),
         z("Einwilligung, aber keine konkrete Todesgefahr", 230, 520, beim("k3", "Einwilligung"), "Bold", 30),
         z("III. Schuld", 200, 600, "k4", "ExtraBold", 34),
         pl("beim Rennen: § 315d StGB", 200, 690, "k5", fill=GELB, size=30),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · die Prüfungsreihenfolge"), ("k1", "Klausurtipp › I. Tatbestand"),
       ("k2", "Klausurtipp › I. Zurechnung: Selbst- oder Fremdgefährdung"), ("k3", "Klausurtipp › II. Rechtswidrigkeit"),
       ("k4", "Klausurtipp › III. Schuld"), ("k5", "Klausurtipp › beim Rennen: § 315d StGB")], els_k)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Beherrscht der andere die", 0)], [("gefährdende Handlung", "a"), (", ist es", 0)],
                 [("Fremdgefährdung", "b"), (", keine Selbstgefährdung.", 0)]], 750, 270, 42, "merke",
                {"a": beim("merke", "gefährdende"), "b": beim("merke", "Fremdgefährdung")}),
    *markertext([[("Dann hilft nur noch die Einwilligung,", 0)], [("und die endet bei ", 0), ("konkreter Todesgefahr", "c"),
                 (".", 0)]], 750, 560, 42, "mk2", {"c": beim("mk2", "konkreter")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
