"""Folge 148 · Unfallflucht § 142: Wie lange muss ich warten? Zettel reicht nicht – Serienstandard Open Peeps (Katzenkönig).
Fall: Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus, schrammt das geparkte Auto von Bernhard,
klemmt einen Zettel mit Name und Telefonnummer unter den Scheibenwischer und fährt sofort weiter; am Morgen findet Bernhard
Schramme und Zettel. Szenen laut ../SZENENPLAN.md: A1 Parkplatz bei Nacht (Nachtverlauf, weil der Fall nachts spielt und
niemand da ist), A2 derselbe Parkplatz am Morgen, B Sachverhalt, C Wortlautkarte § 142 Abs. 1, D I. 1. Unfall im
Straßenverkehr, E I. 2. Unfallbeteiligte (Wortlautkarte Abs. 5), F I. 3. Entfernen (Nr. 1, Nr. 2 Wartepflicht), G Zettel und
Vorsatz, H1 Wortlautkarte Abs. 2, H2 Wortlautkarte Abs. 3 S. 1, I Abs. 2 Nr. 2 und BVerfG (Gegenvariante), J Wortlautkarte
Abs. 4 (tätige Reue), K Ergebnis, L Klausurtipp (Lexi), M Prüfschema, N Merksatz (Lexi).
Kein Aufprallbild: Gerlindes Auto streift beim Ausparken das Auto von Bernhard (Bewegung als Folge kurzer Positionen),
danach nur eine Kratzlinie und ein Ring. Zwei Handlungsgeräusche (Kratzen, Wegfahren; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 140 (gemeinsame Dateien unverändert); neu: parkplatz(), auto(), fahrt(), schramme(), zettel(),
nachtfolie() (mit pruefe_im_bild). Zahlen auf Tafeln, Pillen und Blasen als Ziffern. Wortlautkarten wörtlich nach
gesetze-im-internet.de (Abruf 04.10.2026; Originalschreibung „daß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_148/"

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
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
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
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_148/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Stand: zuletzt geändert durch Art. 1 G v. 20.3.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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



# --- eigene Szenenbausteine: Parkplatz in Seitenansicht (Palettenflächen, Tuschekontur) -------------------------------------
BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (wie Folge 001)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)
ASPH_N = (78, 84, 108, 255)                  # Asphalt nachts
ASPH_T = (200, 200, 198, 255)                # Asphalt am Tag
LINIE = (236, 238, 246, 255)
KRATZ = (250, 250, 250, 255)                 # Kratzspur auf dem blauen Lack
P_O, P_U = 800, 1000                         # Parkplatzfläche (Oberkante, Unterkante)
U_BE, U_GL = 880, 948                        # Unterkante Auto Bernhard (hinten) / Gerlinde (vorn)
CW = 520                                     # Breite der Autos (Icon-Rahmen)
BX = 1000                                    # Auto von Bernhard (Mitte)
GX0, GX1, GX2, GX3 = 420, 1000, 1560, 1650   # Gerlinde: Parkbucht, neben Bernhard, hält, fährt weg


def parkplatz(cue, farbe):
    """Parkplatz in Seitenansicht: Asphaltfläche mit Tuschekante und Markierungsstrichen der Parkbuchten."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (P_U - P_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (P_U - P_O) * s), fill=farbe)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    for x in range(140, 1800, 420):          # Buchtenstriche (schräg, Draufsicht angedeutet)
        dr.line(((x + 40) * s, 18 * s, (x - 10) * s, 182 * s), fill=LINIE, width=8 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, P_O, cue, "cut", 0.0, None, name="parkplatz")


def auto(fuell, cx, unten, cue, bis=None, anim="cut", spiegeln=False):
    return ficon("tabler", "car", cx, unten, CW, cue, fuell=fuell, bis=bis, anim=anim, spiegeln=spiegeln)


def fahrt(fuell, von, nach, unten, start, dauer, n=12, bis=None):
    """Bewegung als Folge kurzer Positionen (harte Schnitte, Icon nicht umgezeichnet)."""
    c, t0 = start
    els = []
    for i in range(n + 1):
        p = i / n
        q = 3 * p * p - 2 * p ** 3
        a_ = (c, round(t0 + dauer * i / n, 3))
        b_ = (c, round(t0 + dauer * (i + 1) / n, 3)) if i < n else bis
        els.append(auto(fuell, von + (nach - von) * q, unten, a_, bis=b_))
    return els


_BE = auto(BLAU, BX, U_BE, "_")              # Geometrie des Autos von Bernhard (für Kratzspur und Zettel)
BE_X, BE_Y, BE_W, BE_H = _BE.x, _BE.y, _BE.sprite.width, _BE.sprite.height
SCH_Y = BE_Y + BE_H * 0.56                   # Höhe der Kratzspur an der Tür
SCH = [(BE_X + BE_W * f, SCH_Y + (8 if i % 2 else -8)) for i, f in enumerate([0.30, 0.36, 0.42, 0.48, 0.54, 0.60, 0.66])]
ZET = (BE_X + BE_W * 0.70, BE_Y + BE_H * 0.36)   # Zettel unter dem Scheibenwischer (Windschutzscheibe vorn rechts)


def schramme(cue, bis=None):
    """Kratzspur: helle Zickzacklinie mit Tuschekante (gut sichtbar auf dem blauen Lack)."""
    a = bis_(linienzug(SCH, cue, breite=12, farbe=INK), bis)
    b = bis_(linienzug(SCH, cue, breite=6, farbe=KRATZ), bis)
    a.sprite.alpha_composite(b.sprite, (b.x - a.x, b.y - a.y))
    return a


def zettel(cue, bis=None, anim="pop"):
    return ficon("tabler", "note", ZET[0], ZET[1] + 30, 64, cue, fuell=WEISS, bis=bis, anim=anim)


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


BODEN = 860
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"GL": "Gerlinde", "BE": "Bernhard"}
NFARBE = {"GL": ROT, "BE": BLAU}
FH = 420                                    # Figurenhöhe in den Fallszenen


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


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


P = "§ 142 StGB"

# ===========================================================================================================================
# A1 Fall: kurz vor Mitternacht auf dem Parkplatz (Nacht: der Fall spielt nachts, niemand ist da)
# ===========================================================================================================================
GLX = 1265                                  # Gerlinde steigt aus, steht zwischen den Autos und blickt nach links zur Tür
AUS = beim("aus", "parkt")
KR = beim("kratz", "schrammt")
lat, (lkx, lky) = laterne(560, P_O + 40, 420, NULL)
WEGF = fahrt(ROT, GX2, GX3, U_GL, beim("weg", "fährt"), 0.6, n=6, bis=beim("weg", "weiter"))   # Auto ist bei „weiter“ weg
WEGF[0] = szene(WEGF[0], "148wegfahrt*", 0.8, 0.0)        # Wegfahren: Geräusch setzt mit der sichtbaren Bewegung ein
nachtfolie([(NULL, "Fall · Nachts auf dem Parkplatz"), ("aus", "Fall · Gerlinde parkt aus"),
            ("kratz", "Fall · Die Schramme"), ("leer", "Fall · Niemand zu sehen"), ("zettel", "Fall · Der Zettel"),
            ("weg", "Fall · Gerlinde fährt weiter")], [
    hart(lichtkegel(lkx, lky, 230, P_O + 120, NULL)),
    hart(parkplatz(NULL, ASPH_N)),
    hart(lat),
    hart(mond(1780, 120, 46, NULL)),
    hart(ficon("tabler", "parking", 120, P_O - 10, 110, NULL, fuell=BLAU, anim="cut")),
    hart(pl("Kurz vor Mitternacht: öffentlicher Parkplatz", 70, 30, NULL, fill=GELB, size=40)),
    # Auto von Bernhard steht ab 0,0 s (hinten); Kratzspur ab „schrammt“, Ring bei „An der Tür“
    hart(auto(BLAU, BX, U_BE, NULL)),
    szene(schramme(KR), "148kratzer*", 0.9, 0.0),
    pl("schrammt das Auto von Bernhard", 70, 115, KR, fill=BLAU, size=32),
    ring(int((SCH[0][0] + SCH[-1][0]) / 2), int(SCH_Y), 170, 50, "schaden", bis="g1"),
    pl("lange Schramme an der Tür", 70, 190, "schaden", fill=WEISS, size=32),
    pl("weit und breit niemand", 70, 265, "leer", fill=WEISS, size=32),
    zettel("zettel", anim="pop"),
    pl("Zettel: Name und Telefonnummer", 70, 340, beim("zettel", "klemmt"), fill=WEISS, size=32),
    pl("fährt sofort weiter", 70, 415, "weg", fill=HELLROT, size=32),
    # Gerlinde: Auto in der Parkbucht ab 0,0 s, parkt bei „parkt aus“ aus, streift Bernhards Auto, hält rechts
    hart(auto(ROT, GX0, U_GL, NULL, bis=AUS)),
    *fahrt(ROT, GX0, GX1, U_GL, AUS, 1.2, n=12, bis=KR),
    *fahrt(ROT, GX1, GX2, U_GL, KR, 1.0, n=10, bis="weg"),
    *WEGF,
    # Gerlinde steigt aus (bei „Weit und breit“), sieht die Schramme, redet, steigt bei „und fährt“ wieder ein
    *fig("GL", GLX, U_GL + 12, FH, [("leer", "schreck")], bis="g1", erst="pop"),
    *redet("GL_redet", GLX, U_GL + 12, FH, "g1", "zettel"),
    *fig("GL", GLX, U_GL + 12, FH, [("zettel", "still")], bis="weg", erst="cut"),
    bis_(ns("Gerlinde", GLX, U_GL + 12, "leer", ROT, d=0.2), "weg"),
    blase("sprech", 700, 230, "g1", 1340, 300, inhalt=["Ist doch nur ein Kratzer.", "Ich lasse einen Zettel da."],
          textsize=36, figur=("GL_redet", GLX, U_GL + 12, FH), bis="zettel"),
])

# ===========================================================================================================================
# A2 Fall: am nächsten Morgen (derselbe Parkplatz bei Tag – die Geschichte kehrt an den Unfallort zurück)
# ===========================================================================================================================
BEX = 1500                                  # Bernhard steht rechts neben seinem Auto und blickt nach links zur Tür
folie([("morgen", "Fall · Am nächsten Morgen"), ("frage", "Fall · Die Frage")], [
    parkplatz("morgen", ASPH_T),
    ficon("tabler", "parking", 120, P_O - 10, 110, "morgen", fuell=BLAU, anim="cut"),
    ficon("tabler", "sun", 1100, 190, 120, "morgen", fuell=GELB, anim="cut"),
    ficon("tabler", "trees", 420, P_O + 4, 200, "morgen", fuell=GRUEN, anim="cut"),
    auto(BLAU, BX, U_BE, "morgen"),
    schramme("morgen"),
    zettel("morgen", anim="cut"),
    pl("Am nächsten Morgen", 70, 30, "morgen", fill=GELB, size=40),
    ring(int((SCH[0][0] + SCH[-1][0]) / 2), int(SCH_Y), 170, 50, beim("morgen", "Schramme"), bis="frage"),
    ring(int(ZET[0]), int(ZET[1]), 60, 52, beim("morgen", "Zettel"), bis="frage"),
    pl("Bernhard findet Schramme und Zettel", 70, 115, beim("morgen", "findet"), fill=BLAU, size=32),
    *fig("BE", BEX, U_GL + 12, FH, [("morgen", "denkt")], bis="b1", erst="pop"),
    *redet("BE_redet", BEX, U_GL + 12, FH, "b1", "frage"),
    *fig("BE", BEX, U_GL + 12, FH, [("frage", "sorge")], erst="cut"),
    ns("Bernhard", BEX, U_GL + 12, "morgen", BLAU, d=0.2),
    blase("sprech", 660, 230, "b1", 1500, 300, inhalt=["Ein Zettel? Und wenn", "der weggeweht wäre?"], textsize=36,
          figur=("BE_redet", BEX, U_GL + 12, FH), bis="frage"),
    pl("§ 142 StGB: unerlaubtes Entfernen?", 70, 200, "frage", fill=PINK, size=36),
    pl("Wie lange hätte sie warten müssen?", 70, 285, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_148(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_148("sv", [
    "Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus. Dabei schrammt sie das geparkte Auto von "
    "Bernhard; an der Tür bleibt eine lange Schramme, die Reparatur kostet rund 400 €. Gerlinde bemerkt das sofort. "
    "Weit und breit ist niemand zu sehen.",
    "Sie schreibt ihren Namen und ihre Telefonnummer auf einen Zettel, klemmt ihn unter den Scheibenwischer und fährt "
    "sofort weiter.",
    "Am nächsten Morgen findet Bernhard die Schramme und den Zettel.",
], "Strafbarkeit von Gerlinde nach § 142 StGB? Wie lange hätte sie warten müssen?")

# ===========================================================================================================================
# C Wortlautkarte § 142 Abs. 1
# ===========================================================================================================================
W1 = ["„(1) Ein Unfallbeteiligter, der sich nach einem Unfall",
      "im Straßenverkehr vom Unfallort entfernt, bevor er",
      "1. zugunsten der anderen Unfallbeteiligten und der Geschädigten",
      "die Feststellung seiner Person, seines Fahrzeugs und der Art",
      "seiner Beteiligung durch seine Anwesenheit und durch die",
      "Angabe, daß er an dem Unfall beteiligt ist, ermöglicht hat oder",
      "2. eine nach den Umständen angemessene Zeit gewartet hat,",
      "ohne daß jemand bereit war, die Feststellungen zu treffen,",
      "wird mit Freiheitsstrafe bis zu drei Jahren oder mit",
      "Geldstrafe bestraft.“"]
w1, w1_y = wortlaut(80, 160, 1100, W1, "§ 142 Abs. 1 StGB", "p142", marken=[
    (0, "Unfallbeteiligter", beim("p142", "Unfallbeteiligten")), (1, "im Straßenverkehr", beim("p142", "Straßenverkehr")),
    (1, "vom Unfallort entfernt", beim("p142", "Unfallort")), (4, "durch seine Anwesenheit", beim("nr1", "Anwesenheit")),
    (6, "angemessene Zeit gewartet", beim("nr2", "angemessene"))], size=30)
folie([("p142", f"{P} › Wortlaut Abs. 1"), ("nr1", f"{P} › Abs. 1 Nr. 1: Anwesenheit"),
       ("nr2", f"{P} › Abs. 1 Nr. 2: Wartepflicht")], rechts_frei([
    *tafel("p142", "§ 142 Abs. 1 StGB: Unfallflucht", h=w1_y + 60 - 60),
    *w1,
    *requisit([("p142", ("tabler", "book", 100, WEISS), "§ 142 Abs. 1 StGB", GELB),
               ("nr1", ("tabler", "user", 100, WEISS), "Nr. 1: anwesend sein", WEISS),
               ("nr2", ("tabler", "hourglass", 100, GELB), "Nr. 2: warten", WEISS)]),
    *stehend("GL", X1, [("p142", "ruhig"), ("nr2", "denkt")]),
    *stehend("BE", X2, [("p142", "ernst")]),
]))

# ===========================================================================================================================
# D I. 1. Unfall im Straßenverkehr
# ===========================================================================================================================
PU1 = "I. 1. Unfall im Straßenverkehr"
folie([("unfall", f"{P} › {PU1}"), ("park", f"{P} › {PU1} › Parkplatz"),
       ("baga", f"{P} › {PU1} › nicht völlig belanglos"), ("schr", f"{P} › {PU1} (+)")], rechts_frei([
    *tafel("unfall", "1. Unfall im Straßenverkehr", h=700),
    z("schädigendes Ereignis, das mit dem Straßenverkehr", 110, 180, "unfall", "Bold", 32),
    z("und seinen Gefahren zusammenhängt", 110, 228, beim("unfall", "Gefahren"), "Bold", 32),
    zit("BGH, Urt. v. 15.11.2001 – 4 StR 233/01, Rn. 7 (BGHSt 47, 158)", 110, 276, beim("unfall", "zusammenhängt")),
    *okz("allgemein zugänglicher Parkplatz: gehört dazu", 340, "park", size=32, x=160),
    zit("OLG Naumburg, Beschl. v. 6.5.2024 – 1 ORs 38/24", 160, 388, beim("park", "gehört")),
    linienzug([(130, 450), (1130, 450)], "baga", breite=3),
    z("ausgenommen: völlig belangloser Schaden", 110, 470, "baga", "Bold", 32),
    z("= üblicherweise wird kein Ersatz verlangt", 110, 518, beim("baga", "also"), size=32),
    zit("OLG Naumburg, Beschl. v. 6.5.2024 – 1 ORs 38/24 (Schramme und Delle)", 110, 566, beim("baga", "Ersatz")),
    blk(110, 625, 1040, 80, GRUEN, "schr", [("Schramme für 400 €: nicht belanglos (+)", "ExtraBold", 34, INK)]),
    *requisit([("unfall", ("tabler", "car", 150, ROT), "Unfall?", WEISS),
               ("park", ("tabler", "parking", 100, BLAU), "Parkplatz", WEISS),
               ("baga", ("tabler", "coin", 100, GELB), "belanglos?", WEISS),
               ("schr", ("tabler", "currency-euro", 100, GELB), "400 €", GRUEN)]),
    *stehend("BE", FX, [("unfall", "ruhig"), ("schr", "ernst")]),
]))

# ===========================================================================================================================
# E I. 2. Unfallbeteiligte: Wortlautkarte Abs. 5
# ===========================================================================================================================
W5 = ["„(5) Unfallbeteiligter ist jeder, dessen Verhalten nach den",
      "Umständen zur Verursachung des Unfalls beigetragen haben",
      "kann.“"]
w5, w5_y = wortlaut(80, 200, 1100, W5, "§ 142 Abs. 5 StGB", "abs5", marken=[
    (0, "jeder", beim("abs5", "jeder")), (1, "zur Verursachung des Unfalls beigetragen haben", beim("abs5", "Verursachung"))],
    size=32)
folie([("abs5", f"{P} › I. 2. Unfallbeteiligte, Abs. 5"), ("ger5", f"{P} › I. 2. Gerlinde: Unfallbeteiligte (+)")],
      rechts_frei([
    *tafel("abs5", "2. Unfallbeteiligte", h=w5_y + 140 - 60),
    *w5,
    *okz("Gerlinde hat beim Ausparken selbst geschrammt: (+)", w5_y + 40, "ger5", "Bold", 32, x=160),
    *requisit([("abs5", ("tabler", "book", 100, WEISS), "§ 142 Abs. 5", GELB),
               ("ger5", ("tabler", "car", 150, ROT), "Unfallbeteiligte (+)", GRUEN)]),
    *stehend("GL", FX, [("abs5", "ruhig"), ("ger5", "sorge")]),
]))

# ===========================================================================================================================
# F I. 3. Entfernen: Nr. 1 Anwesenheit, Nr. 2 Wartepflicht
# ===========================================================================================================================
PE = "I. 3. Entfernen"
folie([("entf", f"{P} › {PE}"), ("anw", f"{P} › {PE} › Nr. 1: Anwesenheit"), ("niem", f"{P} › {PE} › Nr. 1: niemand da"),
       ("warte", f"{P} › {PE} › Nr. 2: Wartepflicht"), ("fakt", f"{P} › {PE} › Nr. 2: angemessene Zeit"),
       ("null", f"{P} › {PE} › Gerlinde: nicht gewartet")], rechts_frei([
    *tafel("entf", "3. Entfernen vom Unfallort"),
    z("Nr. 1: Anwesenheit und Angabe der Beteiligung", 110, 175, "anw", "Bold", 32),
    z("gegenüber feststellungsbereiten Personen", 110, 223, beim("anw", "jemandem"), size=32),
    *neinz("nachts: niemand da", 280, "niem", size=32, x=160),
    linienzug([(130, 342), (1130, 342)], "warte", breite=3),
    z("Nr. 2: eine angemessene Zeit warten", 110, 360, "warte", "Bold", 32),
    z("feste Minutenzahl: steht nicht im Gesetz", 110, 408, "minuten", size=32),
    z("Umstände: Uhrzeit, Verkehr, Auffälligkeit, Schadenshöhe", 110, 456, "fakt", size=32),
    blk(110, 520, 1040, 120, GELB, "olg", [("OLG Dresden: selbst bei kleinem Schaden auf", "ExtraBold", 32, INK),
                                           ("wenig befahrener Straße mindestens 10 Minuten", "ExtraBold", 32, INK)]),
    zit("OLG Dresden, Urt. v. 17.4.2018 – 6 U 1480/17 (Zivilsenat, zu § 142 StGB)", 110, 656, beim("olg", "mindestens")),
    *neinz("Gerlinde: gar nicht gewartet", 715, "null", "Bold", 34, x=160),
    *requisit([("entf", ("tabler", "car", 150, ROT), "Entfernen", WEISS),
               ("anw", ("tabler", "user", 100, WEISS), "Nr. 1: anwesend", WEISS),
               ("niem", ("tabler", "moon", 100, GELB), "niemand da", HELLROT),
               ("warte", ("tabler", "hourglass", 100, GELB), "Nr. 2: warten", WEISS),
               ("minuten", ("tabler", "clock", 100, WEISS), "keine feste Minutenzahl", WEISS),
               ("fakt", ("tabler", "clock", 100, WEISS), "nach den Umständen", WEISS),
               ("olg", ("tabler", "clock", 100, WEISS), "mindestens 10 Minuten", GELB),
               ("null", ("tabler", "hourglass", 100, GELB), "gar nicht gewartet", HELLROT)]),
    *stehend("GL", FX, [("entf", "ruhig"), ("niem", "denkt"), ("null", "sorge")]),
]))

# ===========================================================================================================================
# G Warum der Zettel nicht reicht
# ===========================================================================================================================
PZ = "I. 3. Entfernen › Zettel?"
folie([("zett", f"{P} › {PZ}"), ("zugun", f"{P} › {PZ} › nur zwei Wege"), ("ersatz", f"{P} › {PZ} › kein Ersatz"),
       ("vors", f"{P} › I. 4. Vorsatz (+)")], rechts_frei([
    *tafel("zett", "Und der Zettel?", h=740),
    z("nur zwei Wege, „zugunsten der anderen", 110, 175, "zugun", "Bold", 32),
    z("Unfallbeteiligten und der Geschädigten“:", 110, 223, beim("zugun", "Unfallbeteiligten"), "Bold", 32),
    z("1. anwesend sein und Feststellungen ermöglichen", 160, 280, beim("zugun", "Anwesenheit"), size=32),
    z("2. angemessen warten", 160, 328, beim("zugun", "warten"), size=32),
    *neinz("Zettel als Ersatz: im Gesetz nicht vorgesehen", 400, "ersatz", "Bold", 32, x=160),
    z("nach dem Wegfahren prüft niemand mehr:", 110, 470, "person", size=32),
    z("Person, Fahrzeug, Art der Beteiligung", 110, 518, beim("person", "wer"), "Bold", 32),
    zit("§ 142 Abs. 1 Nr. 1 StGB", 110, 566, beim("person", "beteiligt")),
    blk(110, 625, 1040, 120, LILA, "vors", [("4. Vorsatz (+): Gerlinde wusste von der", "ExtraBold", 32, INK),
                                            ("Schramme – der Zettel zeigt es sogar", "ExtraBold", 32, INK)]),
    *requisit([("zett", ("tabler", "note", 100, WEISS), "Zettel?", WEISS),
               ("zugun", ("tabler", "users", 110, WEISS), "Feststellungen", WEISS),
               ("ersatz", ("tabler", "note-off", 100, WEISS), "kein Ersatz", HELLROT),
               ("person", ("tabler", "id", 100, WEISS), "Person, Fahrzeug, Beteiligung", WEISS),
               ("vors", ("tabler", "note", 100, WEISS), "Vorsatz (+)", LILA)]),
    *stehend("BE", FX, [("zett", "denkt"), ("ersatz", "ernst"), ("vors", "still")]),
]))

# ===========================================================================================================================
# H1 Abs. 2 Nr. 1 (Wortlautkarte Abs. 2)
# ===========================================================================================================================
W2 = ["„(2) Nach Absatz 1 wird auch ein Unfallbeteiligter bestraft,",
      "der sich 1. nach Ablauf der Wartefrist (Absatz 1 Nr. 2) oder",
      "2. berechtigt oder entschuldigt vom Unfallort entfernt hat und",
      "die Feststellungen nicht unverzüglich nachträglich ermöglicht.“"]
w2, w2_y = wortlaut(80, 160, 1100, W2, "§ 142 Abs. 2 StGB", "abs2", marken=[
    (1, "1. nach Ablauf der Wartefrist", beim("abs2", "Nach")),
    (3, "nicht unverzüglich nachträglich ermöglicht", beim("abs2", "unverzüglich"))], size=30)
folie([("abs2", f"{P} › Abs. 2 Nr. 1: nach der Wartefrist")], rechts_frei([
    *tafel("abs2", "Abs. 2: nach dem Warten", h=w2_y + 170 - 60),
    *w2,
    z("auch nach dem Warten nicht einfach frei:", 110, w2_y + 40, beim("abs2", "nicht"), "Bold", 32),
    z("Feststellungen unverzüglich nachträglich ermöglichen", 110, w2_y + 88, beim("abs2", "ermöglichen"), size=32),
    *requisit([("abs2", ("tabler", "hourglass", 100, GELB), "Wartefrist abgelaufen", WEISS),
               (beim("abs2", "unverzüglich"), ("tabler", "phone-call", 100, WEISS), "unverzüglich melden", GELB)]),
    *stehend("GL", FX, [("abs2", "ruhig")]),
]))

# ===========================================================================================================================
# H2 Abs. 3 S. 1 (Wortlautkarte): wie nachträglich ermöglichen
# ===========================================================================================================================
W3 = ["„(3) Der Verpflichtung, die Feststellungen nachträglich zu",
      "ermöglichen, genügt der Unfallbeteiligte, wenn er den Berechtigten",
      "(Absatz 1 Nr. 1) oder einer nahe gelegenen Polizeidienststelle",
      "mitteilt, daß er an dem Unfall beteiligt gewesen ist, und wenn er",
      "seine Anschrift, seinen Aufenthalt sowie das Kennzeichen und den",
      "Standort seines Fahrzeugs angibt und dieses zu unverzüglichen",
      "Feststellungen für eine ihm zumutbare Zeit zur Verfügung hält. …“"]
w3, w3_y = wortlaut(80, 160, 1100, W3, "§ 142 Abs. 3 S. 1 StGB", "abs3", marken=[
    (1, "den Berechtigten", beim("abs3", "Berechtigten")), (2, "nahe gelegenen Polizeidienststelle", beim("abs3", "Polizeidienststelle")),
    (4, "Anschrift", beim("abs3b", "Anschrift")), (4, "Aufenthalt", beim("abs3b", "Aufenthalt")),
    (4, "Kennzeichen", beim("abs3b", "Kennzeichen")), (5, "Standort", beim("abs3b", "Standort")),
    (6, "zur Verfügung hält", "abs3c")], size=30)
folie([("abs3", f"{P} › Abs. 3: nachträglich ermöglichen"), ("spaet", f"{P} › Abs. 3: Meldung nach dem Warten"),
       ("nurtel", f"{P} › Abs. 3: Zettel nur Name, Telefon")], rechts_frei([
    *tafel("abs3", "Abs. 3: die nachträgliche Meldung", h=w3_y + 170 - 60),
    *w3,
    *okz("Meldung kommt nach dem Warten, nicht statt des Wartens", w3_y + 30, "spaet", "Bold", 30, x=160),
    *neinz("Zettel: nur Name und Telefonnummer", w3_y + 95, "nurtel", size=32, x=160),
    *requisit([("abs3", ("tabler", "phone-call", 100, WEISS), "Berechtigter oder Polizei", WEISS),
               ("abs3b", ("tabler", "id", 100, WEISS), "Anschrift, Kennzeichen …", WEISS),
               ("abs3c", ("tabler", "car", 150, ROT), "Fahrzeug bereithalten", WEISS),
               ("spaet", ("tabler", "hourglass", 100, GELB), "erst warten, dann melden", GELB),
               ("nurtel", ("tabler", "note", 100, WEISS), "Name, Telefon", HELLROT)]),
    *stehend("GL", FX, [("abs3", "ruhig"), ("nurtel", "sorge")]),
]))

# ===========================================================================================================================
# I Abs. 2 Nr. 2: unvorsätzliches Entfernen (BVerfG), Gegenvariante
# ===========================================================================================================================
w2b, w2b_y = wortlaut(80, 160, 1100, W2, "§ 142 Abs. 2 StGB", "abs22", marken=[
    (2, "2. berechtigt oder entschuldigt", beim("abs22", "berechtigt"))], size=30)
PB = "Abs. 2 Nr. 2: berechtigt oder entschuldigt"
folie([("abs22", f"{P} › {PB}"), ("bverfg", f"{P} › {PB} › unbemerkter Unfall"),
       ("analog", f"{P} › {PB} › Analogieverbot, Art. 103 Abs. 2 GG"), ("gegen", f"{P} › Gegenvariante: nicht bemerkt")],
      rechts_frei([
    *tafel("abs22", "Abs. 2 Nr. 2: erst später bemerkt?", h=w2b_y + 400 - 60),
    *w2b,
    *neinz("Unfall nicht bemerkt, erst später erfahren: nicht erfasst", w2b_y + 30, "bverfg", "Bold", 30, x=160),
    zit("BVerfG, Beschl. v. 19.3.2007 – 2 BvR 2273/06, Rn. 18, 20", 160, w2b_y + 78, beim("bverfg", "Bundesverfassungsgericht")),
    z("unvorsätzlich ist nicht „berechtigt oder entschuldigt“", 110, w2b_y + 140, "analog", size=32),
    z("sonst verbotene Analogie, Art. 103 Abs. 2 GG", 110, w2b_y + 188, beim("analog", "verbotene"), "Bold", 32),
    zit("ebenso BGH, Beschl. v. 15.11.2010 – 4 StR 413/10, Rn. 5", 110, w2b_y + 236, beim("analog", "Grundgesetz")),
    blk(110, w2b_y + 290, 1040, 80, LILA, "gegen", [("Gegenvariante: nicht bemerkt – nicht strafbar", "ExtraBold", 32, INK)]),
    *requisit([("abs22", ("tabler", "book", 100, WEISS), "Abs. 2 Nr. 2", GELB),
               ("bverfg", ("tabler", "eye-off", 100, WEISS), "nicht bemerkt", WEISS),
               ("analog", ("tabler", "scale", 110, WEISS), "Art. 103 Abs. 2 GG", WEISS),
               ("gegen", ("tabler", "eye-off", 100, WEISS), "§ 142 (−)", LILA)]),
    *stehend("GL", FX, [("abs22", "ruhig"), ("bverfg", "denkt")]),
]))

# ===========================================================================================================================
# J Tätige Reue, Abs. 4 (Wortlautkarte)
# ===========================================================================================================================
W4 = ["„(4) Das Gericht mildert in den Fällen der Absätze 1 und 2",
      "die Strafe (§ 49 Abs. 1) oder kann von Strafe nach diesen",
      "Vorschriften absehen, wenn der Unfallbeteiligte innerhalb von",
      "vierundzwanzig Stunden nach einem Unfall außerhalb des",
      "fließenden Verkehrs, der ausschließlich nicht bedeutenden",
      "Sachschaden zur Folge hat, freiwillig die Feststellungen",
      "nachträglich ermöglicht (Absatz 3).“"]
w4, w4_y = wortlaut(80, 160, 1100, W4, "§ 142 Abs. 4 StGB", "abs4", marken=[
    (3, "außerhalb des", beim("a4a", "außerhalb")), (4, "fließenden Verkehrs", beim("a4a", "außerhalb")),
    (4, "ausschließlich nicht bedeutenden", beim("a4b", "ausschließlich")), (5, "Sachschaden", beim("a4b", "Sachschaden")),
    (2, "innerhalb von", beim("a4c", "innerhalb")), (3, "vierundzwanzig Stunden", beim("a4c", "innerhalb")),
    (5, "freiwillig", beim("a4c", "freiwillig")),
    (0, "mildert", beim("a4d", "mildert")), (1, "kann von Strafe", beim("a4d", "absehen")),
    (2, "Vorschriften absehen", beim("a4d", "absehen"))], size=30)
PR = "Abs. 4: tätige Reue"
folie([("abs4", f"{P} › {PR}"), ("a4a", f"{P} › {PR} › außerhalb des fließenden Verkehrs"),
       ("a4b", f"{P} › {PR} › nicht bedeutender Sachschaden"), ("a4c", f"{P} › {PR} › binnen 24 Stunden, freiwillig"),
       ("a4d", f"{P} › {PR} › Milderung oder Absehen"), ("parkunf", f"{P} › {PR} › Parkunfall"),
       ("vier", f"{P} › {PR} › 400 €: nicht bedeutend")], rechts_frei([
    *tafel("abs4", "Abs. 4: tätige Reue", h=w4_y + 220 - 60),
    *w4,
    *okz("Parkunfall: außerhalb des fließenden Verkehrs", w4_y + 30, "parkunf", size=32, x=160),
    zit("BT-Drucks. 13/8587: Stellungnahme des Bundesrates Nr. 6 und Gegenäußerung", 160, w4_y + 78,
        beim("parkunf", "Parkunfälle")),
    *okz("400 € für eine Schramme: kein bedeutender Schaden", w4_y + 140, "vier", size=32, x=160),
    *requisit([("abs4", ("tabler", "heart-handshake", 110, WEISS), "tätige Reue", GELB),
               ("a4a", ("tabler", "parking", 100, BLAU), "nicht im fließenden Verkehr", WEISS),
               ("a4b", ("tabler", "coin", 100, GELB), "nicht bedeutender Sachschaden", WEISS),
               ("a4c", ("tabler", "clock-24", 100, WEISS), "binnen 24 Stunden", GELB),
               ("a4d", ("tabler", "scale", 110, WEISS), "mildern oder absehen", GRUEN),
               ("parkunf", ("tabler", "parking", 100, BLAU), "Parkunfall (+)", GRUEN)]),
    *stehend("GL", FX, [("abs4", "ruhig"), ("a4d", "denkt"), ("vier", "still")]),
]))

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("rws", "II. Rechtswidrigkeit · III. Schuld"), ("erg", "Ergebnis · § 142 Abs. 1 Nr. 2 StGB"),
       ("erg2", "Ergebnis · Ausblick: Meldung binnen 24 Stunden, Abs. 4")], rechts_frei([
    *tafel("rws", "Ergebnis", h=720),
    *okz("II. Rechtswidrigkeit, III. Schuld: liegen vor", 175, "rws", "Bold", 32, x=160),
    z("Gerlinde ist strafbar nach", 110, 260, "erg", "Bold", 36),
    blk(110, 320, 1040, 80, GELB, beim("erg", "Paragraf"), [("§ 142 Abs. 1 Nr. 2 StGB", "ExtraBold", 38, INK)]),
    z("Ausblick: Meldet sie sich binnen 24 Stunden selbst", 110, 450, "erg2", "Bold", 32),
    z("bei Bernhard oder der Polizei mit den Angaben", 110, 498, beim("erg2", "Bernhard"), size=32),
    z("nach Abs. 3:", 110, 546, beim("erg2", "Angaben"), size=32),
    blk(110, 605, 1040, 80, LILA, beim("erg2", "greift"), [("dann greift § 142 Abs. 4 StGB", "ExtraBold", 34, INK)]),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "strafbar", GELB),
               ("erg2", ("tabler", "phone-call", 100, WEISS), "binnen 24 Stunden melden", LILA)]),
    *stehend("GL", X1, [("rws", "ruhig"), ("erg", "muede"), ("erg2", "denkt")]),
    *stehend("BE", X2, [("rws", "ruhig"), ("erg", "still")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Abs. 1: Nr. 1 vor Nr. 2"), ("tipp2", "Klausurtipp · Abs. 2 nur bei erlaubtem Entfernen"),
       ("tipp3", "Klausurtipp · Vorsatz"), ("tipp4", "Klausurtipp · Abs. 4 bei der Strafe")], [
    *tafel("tipp", "Klausurtipp", fill=HELL, h=560),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. zuerst Abs. 1: Nr. 1 vor Nr. 2", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("2. Abs. 2 nur bei erlaubtem Entfernen:", 200, 275, "tipp2", "Bold", 34),
    z("nach der Wartefrist oder berechtigt/entschuldigt", 200, 325, beim("tipp2", "nach"), size=32),
    z("3. Vorsatz: Unfall und Schaden für möglich halten", 200, 400, "tipp3", "Bold", 34),
    zit("§§ 15, 16 Abs. 1 S. 1 StGB", 200, 450, beim("tipp3", "möglich")),
    z("4. Abs. 4 erst am Ende, bei der Strafe", 200, 515, "tipp4", "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Tatbestand", True),
          (beim("s1", "Unfall"), 1, "1. Unfall im Straßenverkehr", False),
          (beim("s1", "Unfallbeteiligter"), 1, "2. Unfallbeteiligter, Abs. 5", False),
          ("s1b", 1, "3. Entfernen, bevor Abs. 1 Nr. 1 oder Nr. 2 erfüllt ist", False),
          ("s1c", 2, "oder Abs. 2: erlaubt entfernt, nicht unverzüglich nachträglich ermöglicht", False),
          ("s1d", 1, "4. Vorsatz", False),
          ("s2", 0, "II. Rechtswidrigkeit  ·  III. Schuld", True),
          ("s3", 0, "IV. Tätige Reue, Abs. 4", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Unerlaubtes Entfernen vom Unfallort"), 110, 90, "sch", 46),
           z("§ 142 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "s1b":
        els_sch.append(karte(180, y - 16, 1640, 160, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 96, 1: 80, 2: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s1b", "Prüfschema › I. 3. Entfernen"),
       ("s1c", "Prüfschema › I. 3. oder Abs. 2"), ("s1d", "Prüfschema › I. 4. Vorsatz"),
       ("s2", "Prüfschema › II. und III."), ("s3", "Prüfschema › IV. Tätige Reue")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer nach einem Unfall niemanden antrifft,", 0)],
                 [("muss ", 0), ("warten", "a"), (", so lange die Umstände es verlangen.", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "warten")}),
    *markertext([[("Ein ", 0), ("Zettel", "b"), (" ersetzt das Warten nicht.", 0)]], 750, 470, 44, "m2",
                {"b": beim("m2", "Zettel")}),
    *markertext([[("Wer trotzdem wegfährt, kann sich bei", 0)], [("kleinen Parkschäden nur noch über ", 0),
                 ("Abs. 4", "c"), (" helfen.", 0)]], 750, 600, 44, "m3", {"c": beim("m3", "Absatz")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
