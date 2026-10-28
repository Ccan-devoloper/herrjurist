"""Folge 214 · Schießen wegen ein paar Äpfeln? Notwehr bei Bagatellen – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Samstagnacht pflücken Jannes und Paulina (16) auf der Obstwiese von Herrn Gehrke (68) Äpfel für etwa 20 €;
Herr Gehrke droht, gibt einen Warnschuss ab und schießt den Fliehenden auf die Beine; Jannes wird am Bein getroffen.
Danach §§ 223, 224 StGB kurz (Verweis 042), § 32 StGB (Wortlautkarte; Schema verwiesen auf 033), Notwehrlage, Erforderlichkeit,
Gebotenheit (unerträgliches Missverhältnis), Grenzen (keine Kinder; Art. 2 Abs. 2 lit. a EMRK als Streitpunkt, Wortlautkarte),
Ergebnis und § 33 StGB (Wortlautkarte), Klausurtipp, Klausurschema und Merksatz mit Lexi.
DARSTELLUNG: keine Waffe im Bild, kein Schuss, keine Verletzten; Schuss und Treffer nur als Pillentext. Jugendliche als
sympathische Open-Peeps-Figuren. Nacht nur als Mond/Sterne auf dem Cremegrund.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar als
eigene Kopie aus Folge 211 (gemeinsame Dateien unverändert); neu: hh(), stehend() mit Körpergröße, nacht(), baum(), laeufer().
Handlungsgeräusche: Tür (Freesound CC0 256214), Laufen durchs Gras (Freesound CC0 411148); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Art. 2 EMRK nach der deutschen
Fassung des Europarats (die EMRK steht nicht auf gesetze-im-internet.de), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_214/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_214/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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
NAME = {"GE": "Herr Gehrke", "JA": "Jannes", "PA": "Paulina"}
NFARBE = {"GE": LILA, "JA": BLAU, "PA": PINK}
WAND = (246, 236, 220, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))

def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


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



# --- Folge 214: Größen, Szenenbausteine ---------------------------------------------------------------------------------
GROESSE = {"GE": 1.0, "JA": 0.94, "PA": 0.91}            # Jugendliche (16) etwas kleiner als Herr Gehrke (68)


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def nacht(cue):
    """Nacht als Zeichen auf dem Cremegrund (Tageslicht-Standard): Mond und Sterne, keine dunkle Bühne."""
    return [hart(mond(1790, 110, 46, cue)), hart(ficon("tabler", "stars", 1640, 175, 80, cue, fuell=GELB))]


def baum(x, cue, breite=300, aepfel=True):
    """Apfelbaum: Tabler-Baum (grün) mit roten Tabler-Äpfeln in der Krone."""
    els = [hart(ficon("tabler", "tree", x, BODEN, breite, cue, fuell=GRUEN))]
    if aepfel:
        h = breite * 1.0
        for dx, dy in ((-0.22, 0.62), (0.18, 0.70), (0.0, 0.50), (-0.05, 0.80), (0.24, 0.52)):
            els.append(hart(ficon("tabler", "apple", x + dx * breite, BODEN - h * dy + 30, 46, cue, fuell=ROT)))
    return els


# ===========================================================================================================================
# A1 Fall: Obstwiese bei Nacht – Äpfel pflücken, Licht, Herr Gehrke droht
# ===========================================================================================================================
HAUS = 250
GEX1 = 560
JAX1, PAX1 = 1250, 1480
folie([(NULL, "Fall · Samstagnacht auf der Obstwiese"), ("teens", "Fall · Jannes und Paulina pflücken Äpfel"),
       ("licht", "Fall · Im Haus geht das Licht an"), ("tuer", "Fall · Herr Gehrke tritt vor die Tür"),
       ("ge1", "Fall · Herr Gehrke droht"), ("ja1", "Fall · Weg hier!")], [
    boden(NULL), *nacht(NULL),
    hart(ficon("tabler", "home", HAUS, BODEN, 320, NULL, fuell=WAND, bis="licht")),
    hart(lichtschein(HAUS, BODEN - 170, 220, "licht")),
    hart(ficon("tabler", "home", HAUS, BODEN, 320, "licht", fuell=GELB)),
    hart(ficon("tabler", "fence", 790, BODEN, 230, NULL, fuell=WEISS)),
    *baum(1060, NULL), *baum(1720, NULL, 280),
    hart(pl("Samstagnacht im September, kurz vor Mitternacht", 70, 40, NULL, fill=BLAUHELL, size=30)),
    pl("Obstwiese von Herrn Gehrke (68)", 70, 104, "wiese", fill=HELLGRUEN, size=30, bis="licht"),
    pl("Jannes und Paulina, beide 16", 70, 168, "teens", fill=WEISS, size=30, bis="licht"),
    pl("Äpfel im Wert von etwa 20 €", 70, 232, beim("pflueck", "Äpfel"), fill=GELB, size=30, bis="licht"),
    ficon("tabler", "backpack", 1365, BODEN, 86, beim("pflueck", "Rucksack"), fuell=ORANGE),
    ficon("tabler", "apple", 1365, BODEN - 92, 44, beim("pflueck", "Äpfel"), fuell=ROT),
    # Jannes (blickt zum linken Baum, ab „licht“ zum Haus)
    *fig("JA", JAX1, BODEN, hh("JA", FH), [("teens", "froh"), ("licht", "denkt"), ("tuer", "angst")], bis="ja1"),
    *redet("JA_ruft", JAX1, BODEN, hh("JA", FH), "ja1", "flucht"),
    ns(NAME["JA"], JAX1, BODEN, "teens", NFARBE["JA"], d=0.1),
    # Paulina (blickt zum rechten Baum, spricht; ab „licht“ zum Haus)
    *fig("PA", PAX1, BODEN, hh("PA", FH), [("teens", "froh_r")], bis="pa1"),
    *redet("PA_redet_r", PAX1, BODEN, hh("PA", FH), "pa1", "licht"),
    *fig("PA", PAX1, BODEN, hh("PA", FH), [("licht", "ernst"), ("tuer", "angst")], erst="cut"),
    ns(NAME["PA"], PAX1, BODEN, "teens", NFARBE["PA"], d=0.1),
    blase("sprech", 640, 190, "pa1", 1500, 300, inhalt=["Die hier sind die besten", "im ganzen Dorf!"], textsize=32,
          figur=("PA_redet_r", PAX1, BODEN, hh("PA", FH)), bis="licht"),
    pl("Im Haus geht das Licht an.", 70, 104, "licht", fill=GELB, size=30, bis="ge1"),
    # Herr Gehrke tritt wütend vor die Tür (Handlungsgeräusch Tür)
    szene(fig("GE", GEX1, BODEN, FH, [("tuer", "wuetend_r")], bis="ge1")[0], "214tuer*", 0.7, -0.05),
    *redet("GE_ruft_r", GEX1, BODEN, FH, "ge1", "ja1"),
    *fig("GE", GEX1, BODEN, FH, [("ja1", "wuetend_r")], erst="cut"),
    ns(NAME["GE"], GEX1, BODEN, "tuer", NFARBE["GE"], d=0.1),
    blase("sprech", 720, 200, "ge1", 830, 270, inhalt=["Halt! Weg von meinen Bäumen,", "sonst schieße ich!"], textsize=32,
          figur=("GE_ruft_r", GEX1, BODEN, FH), bis="ja1"),
    blase("sprech", 480, 150, "ja1", 1250, 280, inhalt=["Schnell, weg hier!"], textsize=32,
          figur=("JA_ruft", JAX1, BODEN, hh("JA", FH))),
])

# ===========================================================================================================================
# A2 Fall: Die Flucht, der Warnschuss, der Schuss (nur erzählt: keine Waffe, kein Schuss, keine Verletzung im Bild)
# ===========================================================================================================================
GEX2 = 330
J0, J1, J2 = 1100, 1300, 1520         # Jannes: Start, nach „davon“, nach „weiter“
P0, P1, P2 = 1290, 1500, 1730
ZAUN2 = 560
L1 = ("flucht", 0.0), beim("flucht", "davon", ende=True)
L2 = ("weiter", 0.0), beim("weiter", "weiter", ende=True)


def laeufer(k, x0, x1, x2, folge1, folge2, sfx=False):
    """Figur läuft in zwei Etappen nach rechts (bewegt); Mimik wechselt nur nach Etappen."""
    h = hh(k, FH)
    e1 = peep_voll(f"{k}_{folge1}", x1, BODEN, h, "flucht", anim="cut", bis="weiter")
    if sfx:
        szene(e1, "214laufen*", 0.6, 0.05)
    els = [bewegt(e1, L1[0], L1[1], x0 - x1),
           bewegt(ns(NAME[k], x1, BODEN, "flucht", NFARBE[k], anim="cut", bis="weiter"), L1[0], L1[1], x0 - x1)]
    for i, (c, s) in enumerate(folge2):
        b = folge2[i + 1][0] if i + 1 < len(folge2) else None
        e = peep_voll(f"{k}_{s}", x2, BODEN, h, c, anim="cut", bis=b)
        if i == 0:
            e = bewegt(e, L2[0], L2[1], x1 - x2)
        els.append(e)
    els.append(bewegt(ns(NAME[k], x2, BODEN, "weiter", NFARBE[k], anim="cut"), L2[0], L2[1], x1 - x2))
    return els


folie([("flucht", "Fall · Die Flucht mit dem Rucksack"), ("warn", "Fall · Der Warnschuss in die Luft"),
       ("weiter", "Fall · Sie rennen weiter"), ("beine", "Fall · Der Schuss auf die Beine"),
       ("treffer", "Fall · Jannes ist am Bein getroffen")], [
    boden("flucht"), *nacht("flucht"),
    hart(ficon("tabler", "fence", ZAUN2, BODEN, 230, "flucht", fuell=WEISS)),
    *baum(900, "flucht", 260),
    *fig("GE", GEX2, BODEN, FH, [("flucht", "wuetend_r"), ("warn", "ernst_r"), ("treffer", "denkt_r")], erst="cut"),
    hart(ns(NAME["GE"], GEX2, BODEN, "flucht", NFARBE["GE"])),
    *laeufer("JA", J0, J1, J2, "angst_r", [("weiter", "angst_r"), ("treffer", "sorge_r")], sfx=True),
    *laeufer("PA", P0, P1, P2, "angst_r", [("weiter", "angst_r"), ("treffer", "sorge_r")]),
    pl("Die beiden rennen mit dem Rucksack davon.", 70, 40, "flucht", fill=WEISS, size=30),
    pl("Warnschuss in die Luft", 70, 104, "warn", fill=GELB, size=30),
    pl("Sie rennen weiter.", 70, 168, "weiter", fill=WEISS, size=30),
    pl("Er zielt auf ihre Beine und schießt.", 70, 232, "beine", fill=HELLROT, size=30),
    pl("Schrotkörner treffen Jannes am Bein.", 70, 296, "treffer", fill=HELLROT, size=30),
    ficon("tabler", "building-hospital", 700, 470, 100, beim("treffer", "Krankenhaus"), fuell=WEISS),
    pl("im Krankenhaus entfernt", 700, 500, beim("treffer", "Krankenhaus"), fill=WEISS, size=28, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: Später bei der Polizei
# ===========================================================================================================================
GEX3 = 1250
folie([("polizei", "Fall · Herr Gehrke bei der Polizei")], [
    boden("polizei"),
    hart(ficon("tabler", "building", 520, BODEN, 330, "polizei", fuell=WAND)),
    hart(pl("Polizei", 520, 560, "polizei", fill=BLAUHELL, size=30, anker="m")),
    hart(ficon("tabler", "sun", 1760, 220, 110, "polizei", fuell=GELB)),
    hart(pl("später, bei der Polizei", 70, 40, "polizei", fill=BLAUHELL, size=30)),
    *fig("GE", GEX3, BODEN, FH, [("polizei", "ernst")], bis="ge2", erst="cut"),
    *redet("GE_redet", GEX3, BODEN, FH, "ge2", "frage"),
    hart(ns(NAME["GE"], GEX3, BODEN, "polizei", NFARBE["GE"])),
    blase("sprech", 660, 200, "ge2", 1000, 270, inhalt=["Das waren meine Äpfel.", "Ich habe mich nur gewehrt."],
          textsize=32, figur=("GE_redet", GEX3, BODEN, FH)),
])

# ===========================================================================================================================
# A4 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Schießen wegen Äpfeln für 20 €?"), ("frage2", "Die Frage · Hat sich Herr Gehrke strafbar gemacht?")], [
    *tafel("frage", "Die Frage"),
    z("Darf man wegen Äpfeln für 20 €", 110, 190, "frage", "Bold", 40),
    z("auf Menschen schießen?", 110, 246, "frage", "Bold", 40),
    blk(110, 360, 1040, 90, GELB, "frage2", [("Hat Herr Gehrke sich strafbar gemacht?", "ExtraBold", 38, INK)]),
    *requisit([("frage", ("tabler", "apple", 100, ROT), "Äpfel für 20 €", GELB),
               ("frage2", ("tabler", "gavel", 110, WEISS), "strafbar?", WEISS)]),
    *paar("GE", [("frage", "denkt"), ("frage2", "ernst")], "JA", [("frage", "sorge")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_214(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_214("sv", [
    "Samstagnacht im September, kurz vor Mitternacht: Jannes und Paulina (beide 16) klettern über den Zaun der Obstwiese "
    "von Herrn Gehrke (68) und pflücken Äpfel im Wert von etwa 20 € in einen Rucksack. Dass die Äpfel nicht ihnen "
    "gehören, wissen sie.",
    "Wütend tritt Herr Gehrke mit seiner Schrotflinte vor die Tür und ruft: „Halt! Weg von meinen Bäumen, sonst schieße "
    "ich!“ Die beiden rennen mit dem Rucksack davon. Er gibt einen Warnschuss in die Luft ab; sie rennen weiter. Die "
    "Polizei käme zu spät, und hinterherlaufen kann er nicht.",
    "Da zielt Herr Gehrke auf ihre Beine und schießt. Schrotkörner treffen Jannes am Bein; im Krankenhaus werden sie "
    "entfernt. Töten wollte Herr Gehrke niemanden. Er schoss aus Ärger, Angst hatte er nicht.",
], "Hat Herr Gehrke sich strafbar gemacht?")

# ===========================================================================================================================
# C I. Tatbestand: §§ 223, 224 Abs. 1 Nr. 2 StGB (kurz; Verweis Folge 042)
# ===========================================================================================================================
PA_ = "A. Herr Gehrke, §§ 223, 224 StGB"
folie([("tb", f"{PA_} › I. Tatbestand › § 223 Abs. 1"), ("tb2", f"{PA_} › I. Tatbestand › § 224 Abs. 1 Nr. 2: Waffe"),
       ("vors", f"{PA_} › I. Tatbestand › Vorsatz"), ("v042", f"{PA_} › I. Tatbestand › siehe Folge 042"),
       ("rw", f"{PA_} › II. Rechtswidrigkeit: Notwehr?")], [
    *tafel("tb", "I. Tatbestand: §§ 223, 224 StGB"),
    *okz("§ 223 Abs. 1: Schrotkörner im Bein", 180, "tb", "Bold", 34),
    z("körperlich misshandelt, an der Gesundheit geschädigt", 185, 228, beim("tb", "Körperverletzung"), size=32),
    *okz("§ 224 Abs. 1 Nr. 2: mittels einer Waffe", 300, beim("tb2", "Waffe"), "Bold", 34),
    *okz("Vorsatz: Er wollte treffen.", 370, "vors", "Bold", 34),
    blk(110, 450, 1040, 80, BLAUHELL, "v042", [("Mehr dazu: Folge 042 · § 224 StGB", "ExtraBold", 33, INK)]),
    blk(110, 580, 1040, 130, GELB, "rw", [("II. Rechtswidrigkeit:", "ExtraBold", 34, INK),
                                       ("gerechtfertigt durch Notwehr, § 32 StGB?", "Regular", 33, INK)]),
    *requisit([("tb", ("tabler", "book", 110, WEISS), "§§ 223, 224 StGB", WEISS),
               ("rw", ("tabler", "shield-check", 110, GELB), "Notwehr?", GELB)]),
    *paar("GE", [("tb", "ernst"), ("rw", "denkt")], "JA", [("tb", "sorge")]),
])

# ===========================================================================================================================
# D § 32 StGB: Wortlautkarte (Abs. 2 und Abs. 1 vorgelesen); Verweis Folge 033
# ===========================================================================================================================
PN = "A. Herr Gehrke › II. Notwehr, § 32 StGB"
w32, w32_y = wortlaut(80, 180, 1100,
                      "„(1) Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht rechtswidrig. (2) Notwehr ist "
                      "die Verteidigung, die erforderlich ist, um einen gegenwärtigen rechtswidrigen Angriff von sich oder "
                      "einem anderen abzuwenden.“", "§ 32 StGB", "p32",
                      marken=[("Verteidigung", beim("p32", "Verteidigung")), ("erforderlich", beim("p32", "erforderlich")),
                              ("gegenwärtigen", beim("p32", "gegenwärtigen")),
                              ("rechtswidrigen", beim("p32", "rechtswidrigen")), ("Angriff", beim("p32", "Angriff")),
                              ("geboten", beim("abs1", "geboten"))], size=33)
folie([("p32", f"{PN} · Wortlaut"), ("abs1", f"{PN} › Abs. 1: nur die gebotene Tat"),
       ("v033", f"{PN} › Schema: siehe Folge 033")], [
    *tafel("p32", "§ 32 StGB: Notwehr"),
    *w32,
    blk(110, w32_y + 40, 1040, 80, BLAUHELL, "v033", [("Das ganze Schema: Folge 033 · Notwehr", "ExtraBold", 33, INK)]),
    blk(110, w32_y + 150, 1040, 80, GELB, beim("v033", "Grenze"), [("Hier geht es um die Grenze der Notwehr.", "ExtraBold", 33, INK)]),
    *requisit([("p32", ("tabler", "book", 110, WEISS), "§ 32 StGB", WEISS),
               ("abs1", ("tabler", "shield-check", 110, GELB), "geboten?", GELB)]),
    *stehend("GE", FX, [("p32", "ruhig"), ("abs1", "denkt")]),
])
assert w32_y + 250 <= 900, w32_y

# ===========================================================================================================================
# E 1. Notwehrlage (BGH 1 StR 126/21 Rn. 9)
# ===========================================================================================================================
PL = f"{PN} › 1. Notwehrlage"
folie([("lage", f"{PL}"), ("angr", f"{PL} › Angriff: Diebstahl"), ("sache", f"{PL} › auch Sachen verteidigungsfähig"),
       ("gegenw", f"{PL} › gegenwärtig: Flucht mit der Beute"), ("rechtsw", f"{PL} › rechtswidrig"),
       ("lage_ok", f"{PL} (+)")], [
    *tafel("lage", "1. Notwehrlage"),
    *okz("Angriff: Diebstahl der Äpfel, Eigentum", 180, "angr", "Bold", 34),
    z("Auch Sachen darf man verteidigen.", 185, 230, "sache", size=33),
    *okz("gegenwärtig: Flucht mit der Beute", 300, "gegenw", "Bold", 34),
    z("BGH: Notwehrlage, solange der Täter die Beute hat", 185, 350, "beute", size=32),
    zit("BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 9", 185, 396, "beute"),
    *okz("rechtswidrig: Diebstahl, § 242 StGB", 460, "rechtsw", "Bold", 34),
    blk(110, 540, 1040, 80, GRUEN, "lage_ok", [("Notwehrlage (+)", "ExtraBold", 36, INK)]),
    *requisit([("lage", ("tabler", "alert-triangle", 110, GELB), "Notwehrlage?", WEISS),
               ("angr", ("tabler", "apple", 100, ROT), "fremde Äpfel", WEISS),
               ("gegenw", ("tabler", "backpack", 100, ORANGE), "Beute im Rucksack", WEISS),
               ("lage_ok", ("tabler", "circle-check", 110, HELLGRUEN), "Notwehrlage (+)", HELLGRUEN)]),
    *paar("JA", [("lage", "ruhig"), ("angr", "ernst")], "PA", [("lage", "ruhig"), ("angr", "denkt")]),
])

# ===========================================================================================================================
# F 2. a) Erforderlichkeit (BGH 1 StR 126/21 Rn. 14; 2 StR 523/15 Rn. 11; 3 StR 199/15 Rn. 9)
# ===========================================================================================================================
PH = f"{PN} › 2. Notwehrhandlung"
folie([("erf", f"{PH} › a) erforderlich?"), ("ruf", f"{PH} › a) erforderlich: mildere Mittel?"),
       ("waffe", f"{PH} › a) erforderlich: Waffe erst androhen"), ("erf_ok", f"{PH} › a) erforderlich (+)"),
       ("noch", f"{PH} › a) erforderlich: noch keine Abwägung")], [
    *tafel("erf", "2. a) Erforderlichkeit"),
    z("mildestes Mittel, das den Angriff sofort und", 110, 180, "mild", "Bold", 34),
    z("endgültig beendet", 110, 226, "mild", "Bold", 34),
    zit("BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 14", 110, 274, "mild"),
    *neinz("Rufen und Drohen: ohne Erfolg", 330, "ruf", "Bold", 33, kreuz=beim("ruf", "schon")),
    *neinz("Warnschuss: ohne Wirkung", 385, "warn2", "Bold", 33, kreuz=beim("warn2", "ohne")),
    *neinz("Polizei: zu spät", 440, "pol2", "Bold", 33, kreuz=beim("pol2", "spät")),
    *neinz("Hinterherlaufen: mit 68 nicht möglich", 495, beim("pol2", "hinterherlaufen"), "Bold", 33,
           kreuz=beim("pol2", "nicht")),
    blk(110, 565, 1040, 130, GELB, "waffe", [("BGH: lebensgefährliche Waffe erst androhen", "ExtraBold", 32, INK),
                                          ("oder weniger gefährlich einsetzen (Beine)", "Regular", 32, INK)]),
    zit("BGH 2 StR 523/15, Rn. 11; BGH 3 StR 199/15, Rn. 9", 110, 704, "waffe"),
    *okz("Genau das getan: Schuss erforderlich (vertretbar)", 755, "erf_ok", "Bold", 33),
    zit("noch keine Abwägung von Äpfeln gegen Beine", 185, 808, "noch", size=30),
    *requisit([("erf", ("tabler", "shield-check", 110, WEISS), "erforderlich?", WEISS),
               ("ruf", ("tabler", "speakerphone", 110, GELB), "gerufen, gedroht", WEISS),
               ("warn2", ("tabler", "alert-triangle", 110, GELB), "Warnschuss", WEISS),
               ("pol2", ("tabler", "clock", 110, WEISS), "Polizei zu spät", WEISS),
               ("erf_ok", ("tabler", "circle-check", 110, HELLGRUEN), "erforderlich", HELLGRUEN)]),
    *stehend("GE", FX, [("erf", "ernst"), ("ruf", "denkt"), ("erf_ok", "ernst")]),
])

# ===========================================================================================================================
# G1 2. b) Gebotenheit: sozialethische Einschränkung, unerträgliches Missverhältnis (BGH 3 StR 450/10 Rn. 16)
# ===========================================================================================================================
wG, wG_y = wortlaut(80, 170, 1100, "„(1) Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht rechtswidrig. …“",
                    "§ 32 Abs. 1 StGB", "geb", marken=[("geboten", beim("geb", "Gebotenheit"))], size=32)
folie([("geb", f"{PH} › b) geboten?"), ("keine", f"{PH} › b) geboten: keine Güterabwägung"),
       ("sozial", f"{PH} › b) geboten: sozialethische Einschränkungen"),
       ("bgh", f"{PH} › b) geboten: unerträgliches Missverhältnis?")], [
    *tafel("geb", "2. b) Gebotenheit"),
    *wG,
    z("Grundsätzlich keine Abwägung der Rechtsgüter", 110, wG_y + 24, "keine", "Bold", 34),
    zit("BGH, Urt. v. 12.4.2016 – 2 StR 523/15, Rn. 21", 110, wG_y + 70, "keine"),
    z("Aber: sozialethische Einschränkungen", 110, wG_y + 120, "sozial", "Bold", 34),
    zit("BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 18", 110, wG_y + 166, "sozial"),
    blk(110, wG_y + 214, 1040, 80, GELB, "bgh", [("nicht geboten bei „unerträglichem Missverhältnis“", "ExtraBold", 32, INK)]),
    z("Abwehr gefährdet Leib oder Leben, der Angriff ist", 110, wG_y + 312, "bag", size=33),
    z("„evident bagatellhaft“", 110, wG_y + 356, beim("bag", "evident"), "Bold", 33),
    zit("BGH, Beschl. v. 1.3.2011 – 3 StR 450/10, Rn. 16", 110, wG_y + 404, "bag"),
    *requisit([("geb", ("tabler", "scale", 120, WEISS), "geboten?", WEISS),
               ("bgh", ("tabler", "alert-triangle", 110, GELB), "Missverhältnis?", GELB)]),
    *paar("GE", [("geb", "ernst"), ("bag", "sorge")], "JA", [("geb", "ruhig")]),
])
assert wG_y + 450 <= 900, wG_y

# ===========================================================================================================================
# G2 Im Fall: Äpfel für 20 € gegen Schrot auf Menschen → nicht geboten
# ===========================================================================================================================
folie([("hier", f"{PH} › b) geboten: im Fall"), ("nicht", f"{PH} › b) nicht geboten"),
       ("hinnehm", f"{PH} › b) nicht geboten: hinnehmen oder milder")], [
    *tafel("hier", "Im Fall: krasses Missverhältnis"),
    blk(110, 190, 500, 170, HELLGRUEN, "links", [("Äpfel", "ExtraBold", 38, INK), ("für 20 €", "ExtraBold", 38, INK)]),
    blk(650, 190, 500, 170, HELLROT, "rechts", [("Schrot auf Menschen", "ExtraBold", 33, INK),
                                             ("Gesundheit, sogar Leben", "Regular", 32, INK)]),
    *neinz("Die Verteidigung ist nicht geboten.", 420, "nicht", "ExtraBold", 36, kreuz=beim("nicht", "nicht")),
    zit("vgl. BGH 3 StR 450/10, Rn. 16; 3 StR 199/15, Rn. 11", 185, 472, "nicht"),
    z("Herr Gehrke hätte den Verlust hinnehmen oder", 110, 540, "hinnehm", size=33),
    z("weniger gefährliche Mittel wählen müssen:", 110, 586, "hinnehm", size=33),
    z("rufen, die Polizei verständigen", 110, 640, beim("hinnehm", "rufen"), "Bold", 34),
    zit("BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 18", 110, 690, "hinnehm"),
    *requisit([("hier", ("tabler", "scale", 120, WEISS), "Missverhältnis", WEISS),
               ("links", ("tabler", "apple", 100, ROT), "Äpfel: 20 €", HELLGRUEN),
               ("rechts", ("tabler", "alert-triangle", 110, HELLROT), "Leib und Leben", HELLROT),
               ("nicht", ("tabler", "shield-x", 110, HELLROT), "nicht geboten", HELLROT),
               ("hinnehm", ("tabler", "speakerphone", 110, WEISS), "rufen, Polizei", WEISS)]),
    *paar("GE", [("hier", "ernst"), ("nicht", "muede")], "JA", [("hier", "sorge"), ("hinnehm", "ruhig")]),
])

# ===========================================================================================================================
# G3 Keine Kinder; Art. 2 Abs. 2 lit. a EMRK als Streitpunkt (nur bei tödlicher Abwehr)
# ===========================================================================================================================
wE, wE_y = wortlaut(80, 470, 1100,
                    "„Eine Tötung wird nicht als Verletzung dieses Artikels betrachtet, wenn sie durch eine Gewaltanwendung "
                    "verursacht wird, die unbedingt erforderlich ist, um (a) jemanden gegen rechtswidrige Gewalt zu "
                    "verteidigen; …“", "Art. 2 Abs. 2 lit. a EMRK (deutsche Fassung des Europarats)", "emrk",
                    marken=[("Tötung", beim("emrk", "Tötung")), ("rechtswidrige", beim("emrk", "rechtswidrige"))], size=30)
folie([("kind", f"{PH} › b) geboten: keine Kinder"), ("kind2", f"{PH} › b) entscheidend: das Missverhältnis"),
       ("emrk", f"{PH} › b) Streitpunkt: Art. 2 EMRK bei Tötung"), ("emrk2", f"{PH} › b) Art. 2 EMRK: Private gebunden?")], [
    *tafel("kind", "Weitere Grenzen?"),
    *neinz("Kinder? Jannes und Paulina sind 16.", 180, "kind", "Bold", 34, kreuz=beim("kind", "keine")),
    zit("schuldunfähig nur unter 14 Jahren, § 19 StGB", 185, 228, "kind"),
    *neinz("Einschränkung gegenüber erkennbar Schuld-", 280, "kind2", "Bold", 33, kreuz=beim("kind2", "greift")),
    z("losen: greift nicht", 185, 326, "kind2", "Bold", 33),
    blk(110, 380, 1040, 70, GELB, beim("kind2", "Entscheidend"), [("Entscheidend: das Missverhältnis", "ExtraBold", 33, INK)]),
    *wE,
    z("Ob das auch zwischen Privaten gilt: umstritten", 110, wE_y + 18, "emrk2", "Bold", 33),
    *requisit([("kind", ("tabler", "calendar", 110, WEISS), "beide 16 Jahre", WEISS),
               ("emrk", ("tabler", "scale", 120, BLAUHELL), "EMRK", BLAUHELL)]),
    *paar("JA", [("kind", "ruhig")], "PA", [("kind", "ruhig"), ("emrk", "denkt")]),
])
assert wE_y + 70 <= 900, wE_y

# ===========================================================================================================================
# H Ergebnis Rechtswidrigkeit; § 33 StGB (Wortlautkarte; BGH 3 StR 199/15 Rn. 18 f.); strafbar
# ===========================================================================================================================
w33, w33_y = wortlaut(80, 250, 1100, "„Überschreitet der Täter die Grenzen der Notwehr aus Verwirrung, Furcht oder Schrecken, "
                                     "so wird er nicht bestraft.“", "§ 33 StGB", "p33",
                      marken=[("Verwirrung", beim("p33", "Verwirrung")), ("Furcht", beim("p33", "Furcht")),
                              ("Schrecken", beim("p33", "Schrecken"))], size=33)
PE = "A. Herr Gehrke"
folie([("erg", f"{PE} › II. Rechtswidrigkeit: nicht gerechtfertigt"), ("p33", f"{PE} › III. Schuld › § 33 StGB · Wortlaut"),
       ("aerger", f"{PE} › III. Schuld › § 33: aus Ärger, nicht aus Angst"), ("strafbar", f"{PE} › Ergebnis: strafbar"),
       ("dieb", f"{PE} › Ergebnis › Diebstahl: eigene Prüfung")], [
    *tafel("erg", "Ergebnis und § 33 StGB"),
    *neinz("§ 32 StGB: nicht gerechtfertigt", 180, "erg", "ExtraBold", 36, kreuz=beim("erg", "nicht")),
    *w33,
    *neinz("aus Ärger, nicht aus Angst: § 33 greift nicht", w33_y + 30, "aerger", "Bold", 33, kreuz=beim("aerger", "nicht")),
    zit("nur Verwirrung, Furcht, Schrecken: BGH, Urt. v. 27.10.2015 – 3 StR 199/15, Rn. 18", 185, w33_y + 78, "aerger"),
    blk(110, w33_y + 130, 1040, 130, HELLROT, "strafbar", [("strafbar: gefährliche Körperverletzung,", "ExtraBold", 33, INK),
                                                         ("§§ 223, 224 Abs. 1 Nr. 2 StGB", "ExtraBold", 33, INK)]),
    z("Diebstahl von Jannes und Paulina: eigene Prüfung", 110, w33_y + 290, "dieb", size=33),
    *requisit([("erg", ("tabler", "shield-x", 110, HELLROT), "nicht gerechtfertigt", HELLROT),
               ("aerger", ("tabler", "flame", 110, ORANGE), "Ärger", WEISS),
               ("strafbar", ("tabler", "gavel", 110, WEISS), "strafbar", HELLROT)]),
    *paar("GE", [("erg", "ernst"), ("aerger", "wuetend"), ("strafbar", "muede")], "PA", [("erg", "ruhig"), ("dieb", "sorge")]),
])
assert w33_y + 340 <= 900, w33_y

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Erforderlichkeit und Gebotenheit trennen"), ("t1", "Klausurtipp › a) Erforderlichkeit"),
       ("t2", "Klausurtipp › b) Gebotenheit"), ("t3", "Klausurtipp › Signal im Sachverhalt")], [
    *tafel("tipp", "Klausurtipp: sauber trennen", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("a) Erforderlichkeit", 200, 200, "t1", "ExtraBold", 36),
    z("mildestes gleich wirksames Mittel,", 240, 254, beim("t1", "mildesten"), size=34),
    z("ohne Abwägung", 240, 302, beim("t1", "ohne"), size=34),
    linienzug([(130, 370), (1130, 370)], "t2", breite=3),
    z("b) Gebotenheit", 200, 395, "t2", "ExtraBold", 36),
    z("Missverhältnis zwischen Beute und Abwehr", 240, 449, beim("t2", "Missverhältnis"), size=34),
    linienzug([(130, 520), (1130, 520)], "t3", breite=3),
    z("Signal im Sachverhalt:", 200, 545, "t3", "ExtraBold", 36),
    z("geringer Beutewert und", 240, 599, "t3", size=34),
    z("gefährliches Abwehrmittel", 240, 647, beim("t3", "gefährliches"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Gutachtenaufbau (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Gutachtenaufbau"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s2b", "Klausurschema › II. 2. b) nicht geboten"),
       ("s3", "Klausurschema › III. Schuld")], [
    *tafel("sch", "Klausurschema: Herr Gehrke"),
    *plusminus("I. Tatbestand, §§ 223, 224 Abs. 1 Nr. 2", 110, 190, "s1", True, size=36, stil="ExtraBold"),
    z("II. Rechtswidrigkeit: Notwehr, § 32 StGB", 110, 280, "s2", "ExtraBold", 36),
    *plusminus("1. Notwehrlage", 170, 340, beim("s2", "Notwehrlage"), True, size=34),
    *plusminus("2. a) erforderlich", 170, 396, beim("s2", "erforderlich"), True, size=34),
    *plusminus("b) geboten", 230, 452, "s2b", False, size=34),
    *plusminus("III. Schuld: § 33 StGB", 110, 540, "s3", False, size=36, stil="ExtraBold"),
    z("kein Notwehrexzess", 170, 596, beim("s3", "kein"), size=34),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Notwehr kennt grundsätzlich", 0)], [("keine Güterabwägung", "a"), (".", 0)]],
                750, 280, 44, "merke", {"a": beim("merke", "keine")}),
    *markertext([[("Wer aber für eine Kleinigkeit Leib oder", 0)], [("Leben eines Menschen gefährdet,", 0)],
                 [("handelt ", 0), ("nicht geboten", "b"), (".", 0)]],
                750, 430, 44, "m2", {"b": beim("m2", "nicht")}),
    *markertext([[("Für ein paar Äpfel darf man", 0)], [("nicht schießen", "c"), (".", 0)]],
                750, 670, 44, "m3", {"c": beim("m3", "nicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
