"""Folge 114 · Straferwartung Zuständigkeit: Strafrichter, Schöffengericht, LG – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Herr Hartung (34, zweimal wegen Betrugs vorbestraft) nimmt von Februar bis Juli 2026 in Erlenstadt (erfunden)
als angeblicher Terrassenbauer zwölf Anzahlungen (zusammen 40.000 €, darunter 3.500 € von Herrn Grote) und lebt davon.
Im September 2026 bestimmt Staatsanwältin Eggert das zuständige Gericht.
Szenen laut ../SZENENPLAN.md: A1 Garten (Anzahlung), A2 Garten (gebaut wird nie, elf weitere Kunden), A3 Staatsanwaltschaft
(Akte, Frage), B Sachverhalt, C Zwei Fragen, D Die Treppe (§ 25 Nr. 2 und § 24 Abs. 1 Satz 1 Nr. 2 GVG im Wortlaut, § 28,
§ 24 Abs. 2, § 74 Abs. 1, Nr. 3, Sonderzuweisungen), G1 Vergehen und Strafrahmen, G2 Regelbeispiel gewerbsmäßig/großes
Ausmaß, H Vorstrafen und Gesamtstrafe, I Prognose und Ergebnis (Jahresachse), J II. Örtlich, K III. Anklage, L Klausurtipp
(Lexi), M Klausurschema (Treppe), N Merksatz (Lexi).
Zwei Handlungsgeräusche (Geldscheine bei der Anzahlung, Akte auf dem Schreibtisch; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 112 (gemeinsame Dateien unverändert); neu: Treppe aus Blöcken, Jahresachse.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_114/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_114/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]





BODEN, FH = 860, 480
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GR_N, HA_N, EG_N = ORANGE, TUERKIS, LILA    # Farben der Namensschilder
PX, PY, PU = 1560, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"GR": "Herr Grote", "HA": "Herr Hartung", "EG": "Staatsanwältin Eggert"}
KURZ = {"GR": "Herr Grote", "HA": "Herr Hartung", "EG": "StA Eggert"}
NFARBE = {"GR": GR_N, "HA": HA_N, "EG": EG_N}
HOLZ = (214, 160, 110, 255)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf), ns(KURZ[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(KURZ[r], X2, FB, c0, NFARBE[r], d=0.3)]


def allein(c0, p, folge):
    return [*fig(p, FX, FB, FR, folge), ns(NAME[p], FX, FB, c0, NFARBE[p], d=0.1)]


# ===========================================================================================================================
# A1 Fall: im Garten von Herrn Grote, März 2026
# ===========================================================================================================================
GRX, HAX = 950, 1530                        # Grote (blickt nach rechts zu Hartung), Hartung (blickt nach links zu Grote)
HAUSX = 260
ZAHLT = beim("anz", "zahlt")
ZAHLT_DA = ("anz", round(ZAHLT[1] + 0.8, 3))
gh = hand("GR_ruhig_r", GRX, BODEN, FH, +1)
hh = hand("HA_ruhig", HAX, BODEN, FH, -1)
folie([(NULL, "Fall · Im Garten von Herrn Grote"), ("anz", "Fall · Die Anzahlung")], [
    hart(boden(NULL)),
    hart(ficon("tabler", "home", HAUSX, BODEN, 300, NULL, fuell=GELB)),
    hart(ficon("tabler", "fence", 560, BODEN, 200, NULL, fuell=WEISS)),
    hart(ficon("tabler", "plant-2", 700, BODEN, 110, NULL, fuell=GRUEN)),
    hart(pl("Erlenstadt, März 2026", 70, 30, NULL, fill=GELB, size=44)),
    pl("Wunsch: eine neue Terrasse", 70, 120, beim("grote", "Terrasse"), fill=WEISS, size=36),
    pl("selbstständiger Handwerker", HAX, 120, beim("hart", "selbstständiger"), fill=WEISS, size=32, anker="m", bis="h1"),
    ficon("tabler", "tools", 1790, BODEN, 110, beim("hart", "Handwerker"), fuell=None),
    pl("Anzahlung: 3.500 €", 70, 210, beim("anz", "dreitausendfünfhundert"), fill=GELB, size=40),
    # Geldscheine wandern von Grote zu Hartung
    bis_(ficon("tabler", "cash-banknote", gh[0] + 30, gh[1] + 20, 110, "anz", fuell=GRUEN), ZAHLT),
    szene(bewegt(bis_(ficon("tabler", "cash-banknote", hh[0] - 30, hh[1] + 20, 110, ZAHLT, fuell=GRUEN, anim="cut"),
                      ZAHLT_DA), ZAHLT, ZAHLT_DA, (gh[0] + 30) - (hh[0] - 30), 0), "114geld*", 0.8, 0.0),
    ficon("tabler", "cash-banknote", hh[0] - 30, hh[1] + 20, 110, ZAHLT_DA, fuell=GRUEN, anim="cut"),
    # Grote (links, blickt zu Hartung)
    *fig("GR", GRX, BODEN, FH, [(NULL, "ruhig_r"), (beim("grote", "Terrasse"), "froh_r"), ("anz", "ruhig_r"),
                                ("h1", "froh_r")], erst="cut"),
    hart(ns("Herr Grote", GRX, BODEN, NULL, GR_N)),
    # Hartung (rechts, blickt zu Grote), kommt bei „Herr Hartung“ ins Bild
    *fig("HA", HAX, BODEN, FH, [("hart", "ruhig"), (ZAHLT_DA, "cool")], bis="h1"),
    ns("Herr Hartung", HAX, BODEN, "hart", HA_N, d=0.1),
    *redet("HA_redet", HAX, BODEN, FH, "h1", "nie"),
    blase("sprech", 760, 220, "h1", 1180, 200, inhalt=["Nächste Woche fangen wir an.", "Das Material ist schon bestellt."],
          textsize=36, figur=("HA_redet", HAX, BODEN, FH), bis="nie"),
])

# ===========================================================================================================================
# A2 Fall: derselbe Garten, Monate später
# ===========================================================================================================================
GRX2 = 1500
TEL = beim("g1", "Telefon")
folie([("nie", "Fall · Gebaut wird nie"), ("elf", "Fall · Elf weitere Kunden")], [
    boden("nie"),
    ficon("tabler", "home", HAUSX, BODEN, 300, "nie", fuell=GELB),
    ficon("tabler", "fence", 560, BODEN, 200, "nie", fuell=WEISS),
    ficon("tabler", "plant-2", 700, BODEN, 110, "nie", fuell=GRUEN),
    pl("Gebaut wird nie.", 70, 30, "nie", fill=ROT, size=44, bis=beim("elf", "elf")),
    ficon("tabler", "phone-off", 1180, 600, 100, TEL, fuell=WEISS, bis="elf"),
    pl("Telefon abgeschaltet", 1180, 620, TEL, fill=WEISS, size=30, anker="m", bis="elf"),
    blase("sprech", 800, 230, "g1", 860, 190, inhalt=["Seit April warte ich. Niemand kommt,", "und sein Telefon ist abgeschaltet."],
          textsize=36, figur=("GR_redet", GRX2, BODEN, FH), bis="elf"),
    # elf weitere Kunden: elf Häuser in Erlenstadt
    pl("11 weitere Kunden in Erlenstadt", 70, 30, beim("elf", "elf"), fill=GELB, size=44),
    *[ficon("tabler", "home", 110 + i * 92, 260, 80, beim("elf", "Kunden"), fuell=GELB, d=0.05 * i) for i in range(11)],
    pl("Februar bis Juli 2026", 70, 300, beim("elf", "Februar"), fill=WEISS, size=36),
    *fig("GR", GRX2, BODEN, FH, [("nie", "sorge")], bis="g1"),
    ns("Herr Grote", GRX2, BODEN, "nie", GR_N, d=0.1),
    *redet("GR_redet", GRX2, BODEN, FH, "g1", "elf"),
    *fig("GR", GRX2, BODEN, FH, [("elf", "muede")], erst="cut"),
])

# ===========================================================================================================================
# A3 Fall: bei der Staatsanwaltschaft, September 2026
# ===========================================================================================================================
EGX = 1500
TISCHX = 560
akte = szene(bewegt(ficon("tabler", "folders", TISCHX, 511, 190, "akte", fuell=GELB), "akte", ("akte", 0.35), 0, -260),
             "114akte*", 1.0, versatz=0.30)
folie([("akte", "Fall · Bei der Staatsanwaltschaft"), ("frage", "Fall · Die Frage")], [
    boden("akte"),
    pl("September 2026: bei der Staatsanwaltschaft", 70, 30, "akte", fill=GELB, size=40),
    ficon("tabler", "desk", TISCHX, BODEN - 2, 560, "akte", fuell=HOLZ),
    akte,
    pl("12 Anzahlungen", 70, 120, beim("zwoelf", "Zwölf"), fill=WEISS, size=36),
    pl("zusammen 40.000 €", 420, 120, beim("zwoelf", "vierzigtausend"), fill=GELB, size=36),
    pl("Material nie bestellt – er lebte vom Geld", 70, 205, beim("lebte", "Material"), fill=WEISS, size=34),
    pl("2 Vorstrafen wegen Betrugs", 70, 290, beim("vor", "zweimal"), fill=ROT, size=36),
    *fig("EG", EGX, BODEN, FH, [(beim("akte", "Staatsanwältin"), "ruhig"), (beim("lebte", "Material"), "denkt"), ("vor", "ernst")],
        bis="e_1"),
    ns("Staatsanwältin Eggert", EGX, BODEN, beim("akte", "Staatsanwältin"), EG_N),
    *redet("EG_redet", EGX, BODEN, FH, "e_1", "frage"),
    blase("sprech", 700, 220, "e_1", 1250, 200, inhalt=["12 Betrugstaten. Zu welchem", "Gericht klage ich an?"],
          textsize=36, figur=("EG_redet", EGX, BODEN, FH), bis="frage"),
    pl("Strafrichter, Schöffengericht oder Landgericht?", 880, 120, "frage", fill=PINK, size=34),
    pl("Welches Gericht ist örtlich zuständig?", 880, 205, "frage2", fill=WEISS, size=34),
    *fig("EG", EGX, BODEN, FH, [("frage", "denkt")], erst="cut"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_114(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_114("sv", [
    "Herr Hartung (34) bietet in Erlenstadt als selbstständiger Handwerker den Bau von Terrassen an. Von Februar bis "
    "Juli 2026 nimmt er von 12 Kunden in Erlenstadt Anzahlungen zwischen 2.000 und 5.000 Euro, zusammen 40.000 Euro, "
    "darunter 3.500 Euro von Herrn Grote. Bauen wollte er nie, Material bestellte er nicht. Er hatte kein anderes "
    "Einkommen und lebte von dem Geld.",
    "Herr Hartung wohnt in Erlenstadt. Er ist zweimal wegen Betrugs vorbestraft (2019 Geldstrafe, 2022 zehn Monate "
    "Freiheitsstrafe mit Bewährung, Bewährungszeit 2025 abgelaufen).",
    "Im September 2026 liegt die Akte bei Staatsanwältin Eggert. Die Taten sind nachweisbar. Bearbeitervermerk: "
    "Bestimmen Sie das zuständige Gericht.",
], "Zu welchem Gericht erhebt die Staatsanwältin Anklage?")

# ===========================================================================================================================
# C Zwei Fragen
# ===========================================================================================================================
folie([("plan", "Zuständigkeit › zwei Fragen"), ("plan3", "Zuständigkeit › die Straferwartung")], rechts_frei([
    *tafel("plan", "Welches Gericht?"),
    karte(150, 200, 90, 76, "plan1", fill=BLAU, rund=14, schatten=5, rand=4),
    z("I.", 195 - F("ExtraBold", 38).getlength("I.") / 2, 212, "plan1", "ExtraBold", 38),
    z("sachliche Zuständigkeit", 270, 205, "plan1", "Bold", 40),
    zit("Gerichtsverfassungsgesetz (GVG), § 1 StPO", 270, 262, beim("plan1", "Gerichtsverfassungsgesetz")),
    karte(150, 340, 90, 76, "plan2", fill=GRUEN, rund=14, schatten=5, rand=4),
    z("II.", 195 - F("ExtraBold", 38).getlength("II.") / 2, 352, "plan2", "ExtraBold", 38),
    z("örtliche Zuständigkeit", 270, 345, "plan2", "Bold", 40),
    zit("§§ 7 ff. StPO", 270, 402, beim("plan2", "Paragrafen")),
    blk(110, 500, 1040, 110, GELB, "plan3", [("Sachlich entscheidet vor allem", "Bold", 34, INK),
                                             ("eine Prognose: die Straferwartung", "ExtraBold", 38, INK)]),
    *requisit([("plan", ("tabler", "gavel", 110, HOLZ), "Welches Gericht?", WEISS),
               ("plan2", ("tabler", "map-pin", 90, ROT), "Welcher Ort?", WEISS),
               ("plan3", ("tabler", "hourglass", 90, GELB), "Straferwartung", GELB)]),
    *paar("plan", "HA", [("plan", "ruhig"), ("plan3", "denkt")], "EG", [("plan", "ruhig"), ("plan1", "denkt"),
                                                                       ("plan3", "ernst")]),
]))

# ===========================================================================================================================
# D Die Treppe: Strafrichter, Schöffengericht, Landgericht, Sonderzuweisungen (Wortlautkarten § 25 Nr. 2, § 24 Abs. 1 Nr. 2)
# ===========================================================================================================================
STUFEN = [("Strafrichter", "bis 2 Jahre", BLAU, beim("st1a", "Strafrichter")),
          ("Schöffengericht", "bis 4 Jahre", GRUEN, "st2"),
          ("Landgericht", "über 4 Jahre", GELB, "st3"),
          ("OLG", "Staatsschutz", LILA, "st4b")]
treppe = []
for k, (n, u, farbe, c) in enumerate(STUFEN):
    top = 790 - k * 80
    treppe.append(blk(110 + k * 262, top, 255, 880 - top, farbe, c, [(n, "ExtraBold", 28, INK), (u, "Bold", 28, INK)],
                      anim="pop"))

W25 = ["„Der Richter beim Amtsgericht entscheidet als Strafrichter",
       "bei Vergehen, … 2. wenn eine höhere Strafe als Freiheitsstrafe",
       "von zwei Jahren nicht zu erwarten ist.“"]
w25, w25_y = wortlaut(80, 170, 1100, W25, "§ 25 Nr. 2 GVG", beim("st1a", "Paragraf"), marken=[
    (1, "bei Vergehen", beim("st1a", "Vergehen")), (1, "eine höhere Strafe als Freiheitsstrafe", beim("st1a", "höhere")),
    (2, "nicht zu erwarten", beim("st1a", "erwarten"))], size=32, bis="st2")
W24 = ["„(1) In Strafsachen sind die Amtsgerichte zuständig, wenn nicht …",
       "2. im Einzelfall eine höhere Strafe als vier Jahre Freiheitsstrafe",
       "oder die Unterbringung des Beschuldigten in einem psychiatrischen",
       "Krankenhaus, allein oder neben einer Strafe, oder in der",
       "Sicherungsverwahrung (§§ 66 bis 66b des Strafgesetzbuches) zu",
       "erwarten ist …“"]
w24, w24_y = wortlaut(80, 165, 1100, W24, "§ 24 Abs. 1 Satz 1 Nr. 2 GVG", beim("st3a", "Nach"), marken=[
    (0, "die Amtsgerichte zuständig, wenn nicht", beim("st3a", "Amtsgericht")),
    (1, "höhere Strafe als vier Jahre Freiheitsstrafe", beim("st3a", "höhere")),
    (2, "Unterbringung", beim("st3b", "Unterbringung")), (4, "Sicherungsverwahrung", beim("st3b", "Sicherungsverwahrung"))],
    size=30, bis="st3c")
assert w24_y <= 540, w24_y
folie([("st1", "I. Sachlich › die Treppe"), ("st1a", "I. Sachlich › Strafrichter, § 25 Nr. 2 GVG"),
       ("st2", "I. Sachlich › Schöffengericht, § 28 GVG"), ("st2a", "I. Sachlich › Strafbann, § 24 Abs. 2 GVG"),
       ("st3a", "I. Sachlich › Landgericht, § 24 Abs. 1 Satz 1 Nr. 2 GVG"),
       ("st3d", "I. Sachlich › Landgericht, § 24 Abs. 1 Satz 1 Nr. 3 GVG"), ("st4", "I. Sachlich › Sonderzuweisungen")],
      rechts_frei([
    *tafel("st1", "I. Sachlich: die Treppe"),
    *treppe,
    *w25,
    # Schöffengericht und Strafbann
    bis_(z("Schöffengericht: die übrigen Sachen des Amtsgerichts", 110, 190, "st2", "Bold", 36), "st3"),
    bis_(zit("§ 28 GVG", 110, 245, beim("st2", "Paragraf")), "st3"),
    bis_(z("Strafbann: höchstens 4 Jahre Freiheitsstrafe", 110, 310, "st2a", "Bold", 36), "st3"),
    bis_(zit("§ 24 Abs. 2 GVG", 110, 365, beim("st2a", "Paragraf")), "st3"),
    *w24,
    bis_(z("Dann: Strafkammer des Landgerichts", 110, 190, "st3c", "Bold", 36), "st4"),
    bis_(zit("§ 74 Abs. 1 GVG", 110, 245, beim("st3c", "Paragraf")), "st4"),
    bis_(z("Nr. 3: Anklage beim Landgericht wegen", 110, 310, "st3d", "Bold", 34), "st4"),
    bis_(z("besonderer Schutzbedürftigkeit, Umfang, Bedeutung", 110, 360, beim("st3d", "besonderer"), size=34), "st4"),
    z("Vorrang: Sonderzuweisungen", 110, 190, "st4", "Bold", 36),
    z("Schwurgericht, z. B. Mord", 150, 255, "st4a", "Bold", 34),
    zit("§ 74 Abs. 2 GVG", 150, 305, beim("st4a", "Schwurgericht")),
    z("OLG: Staatsschutzsachen, z. B. Hochverrat", 150, 370, "st4b", "Bold", 34),
    zit("§ 120 GVG", 150, 420, beim("st4b", "Paragraf")),
    *requisit([("st1", ("tabler", "stairs-up", 110, WEISS), "4 Stufen", WEISS),
               (beim("st1a", "Strafrichter"), ("tabler", "gavel", 110, HOLZ), "Strafrichter", BLAU),
               ("st2", ("tabler", "gavel", 110, GRUEN), "Schöffengericht", GRUEN),
               ("st3", ("tabler", "building-bank", 110, GELB), "Landgericht", GELB),
               ("st4", ("tabler", "building-fortress", 110, LILA), "Sonderzuweisungen", LILA)]),
    *paar("st1", "HA", [("st1", "ruhig"), ("st2a", "denkt"), ("st3a", "ernst")],
          "EG", [("st1", "ruhig"), ("st2", "denkt"), ("st4", "ruhig")]),
]))

# ===========================================================================================================================
# G1 Straferwartung: Vergehen und Strafrahmen
# ===========================================================================================================================
folie([("e1", "I. Sachlich › Straferwartung"), ("e2", "Straferwartung › Vergehen, § 12 StGB"),
       ("e3", "Straferwartung › Strafrahmen, § 263 StGB")], rechts_frei([
    *tafel("e1", "Die Straferwartung bilden"),
    z("1. Vergehen?", 110, 190, "e2", "ExtraBold", 38),
    *okz("Betrug ist ein Vergehen", 255, beim("e2", "Vergehen"), "Bold", 36, x=160),
    zit("§ 12 Abs. 2 StGB", 160, 310, beim("e2", "Paragraf")),
    *okz("auch im besonders schweren Fall", 365, "e2a", "Bold", 36, x=160),
    zit("§ 12 Abs. 3 StGB: Schärfungen bleiben außer Betracht", 160, 420, beim("e2a", "Solche")),
    z("2. Strafrahmen", 110, 500, "e3", "ExtraBold", 38),
    z("§ 263 Abs. 1 StGB: Freiheitsstrafe bis 5 Jahre", 160, 565, beim("e3", "Freiheitsstrafe"), "Bold", 36),
    z("oder Geldstrafe", 160, 615, beim("e3", "Geldstrafe"), size=34),
    blk(110, 690, 1040, 100, GELB, "e4", [("besonders schwerer Fall, § 263 Abs. 3:", "Bold", 34, INK),
                                          ("6 Monate bis 10 Jahre", "ExtraBold", 38, INK)]),
    *requisit([("e1", ("tabler", "hourglass", 90, GELB), "Straferwartung", GELB),
               ("e2", ("tabler", "scale", 100, WEISS), "Vergehen", WEISS),
               ("e3", ("tabler", "file-text", 90, WEISS), "§ 263 StGB", WEISS),
               ("e4", ("tabler", "file-text", 90, GELB), "6 Monate bis 10 Jahre", GELB)]),
    *paar("e1", "HA", [("e1", "ruhig"), ("e4", "schreck")], "EG", [("e1", "ruhig"), ("e2", "denkt"), ("e4", "ernst")]),
]))

# ===========================================================================================================================
# G2 Regelbeispiel gewerbsmäßig, großes Ausmaß
# ===========================================================================================================================
folie([("e5", "Straferwartung › Regelbeispiel: gewerbsmäßig"), ("e8", "Straferwartung › großes Ausmaß?")], rechts_frei([
    *tafel("e5", "Regelbeispiel: gewerbsmäßig"),
    z("§ 263 Abs. 3 Satz 2 Nr. 1 StGB", 110, 185, "e5", "Bold", 36),
    z("Gewerbsmäßig handelt, wer sich durch wiederholte", 110, 250, "e6", size=34),
    z("Taten eine nicht nur vorübergehende Einnahmequelle", 110, 298, beim("e6", "wiederholte"), size=34),
    z("von einigem Umfang und einiger Dauer verschaffen will.", 110, 346, beim("e6", "Einnahmequelle"), size=34),
    zit("BGH, Beschl. v. 14.4.2026 – 3 StR 556/25, Rn. 5", 110, 400, beim("e6", "Einnahmequelle")),
    *okz("Hartung lebte von den Anzahlungen", 470, beim("e7", "lebte"), "Bold", 36, x=160),
    blk(110, 545, 1040, 80, GRUEN, beim("e7", "Regelbeispiel"), [("Regelbeispiel erfüllt", "ExtraBold", 38, INK)]),
    *neinz("Nr. 2, großes Ausmaß: je Tat, grundsätzlich 50.000 €", 670, "e8", "Bold", 34, x=160),
    z("hier je Tat höchstens 5.000 €", 160, 722, beim("e8", "einzeln"), size=34),
    zit("vgl. BGH, Urt. v. 24.6.2026 – 1 StR 247/25, Rn. 14", 160, 775, beim("e8", "fünfzigtausend")),
    *requisit([("e5", ("tabler", "cash-banknote", 110, GRUEN), "Einnahmequelle?", WEISS),
               ("e7", ("tabler", "cash-banknote", 110, GRUEN), "lebte vom Geld", GRUEN),
               ("e8", ("tabler", "x", 90, WEISS), "kein großes Ausmaß", ROT)]),
    *paar("e5", "HA", [("e5", "ruhig"), ("e7", "schreck"), ("e8", "denkt")], "EG", [("e5", "ruhig"), ("e7", "ernst")]),
]))

# ===========================================================================================================================
# H Vorstrafen und Gesamtstrafe, §§ 46, 53, 54 StGB
# ===========================================================================================================================
QX = 160
folie([("e9", "Straferwartung › Vorstrafen, § 46 Abs. 2 StGB"), ("e10", "Straferwartung › Gesamtstrafe, §§ 53, 54 StGB")],
      rechts_frei([
    *tafel("e9", "Vorstrafen und Gesamtstrafe"),
    *okz("2 Vorstrafen: strafschärfend", 190, "e9", "Bold", 36, x=160),
    zit("§ 46 Abs. 2 StGB: „das Vorleben des Täters“", 160, 245, beim("e9", "Vorleben")),
    z("12 Taten: 12 Einzelstrafen", 110, 320, "e10", "Bold", 36),
    *[karte(QX + i * 82, 382, 62, 52, beim("e10", "Einzelstrafen"), fill=BLAU, rund=10, schatten=4, rand=4) for i in range(12)],
    z("daraus eine Gesamtstrafe, § 53 StGB", 110, 465, beim("e10", "Gesamtstrafe"), "Bold", 36),
    z("§ 54 StGB: die höchste Einzelstrafe wird erhöht,", 110, 540, "e11", "Bold", 36),
    z("die Summe darf nicht erreicht werden", 110, 592, beim("e11", "Summe"), "Bold", 36),
    blk(110, 680, 1040, 90, GELB, "e11a", [("Asperationsprinzip", "ExtraBold", 40, INK)]),
    *requisit([("e9", ("tabler", "file-text", 90, ROT), "2 Vorstrafen", ROT),
               ("e10", ("tabler", "stack-2", 100, BLAU), "12 Einzelstrafen", BLAU),
               ("e11", ("tabler", "sum", 90, WEISS), "Summe nicht erreichen", WEISS)]),
    *paar("e9", "HA", [("e9", "schreck"), ("e10", "denkt")], "EG", [("e9", "ernst"), ("e11", "denkt")]),
]))

# ===========================================================================================================================
# I Prognose und Ergebnis der sachlichen Zuständigkeit
# ===========================================================================================================================
AX0, AX1, AY = 150, 1040, 420
jahr = lambda j: AX0 + j / 5 * (AX1 - AX0)
achse = [linienzug([(AX0 - 10, AY), (AX1 + 10, AY)], "e12", breite=5)]
for j in range(6):
    achse.append(linienzug([(jahr(j), AY - 12), (jahr(j), AY + 12)], "e12", breite=4))
    t_ = f"{j}" if j < 5 else "5 Jahre"
    achse.append(z(t_, jahr(j) - F("Bold", 28).getlength(str(j)) / 2, AY + 20, "e12", "Bold", 28, farbe=TEXT))
GES = beim("e12", "Gesamtstrafe")
folie([("e12", "Straferwartung › Prognose der Staatsanwältin"), ("f1", "I. Sachlich › Ergebnis"),
       ("f5", "I. Sachlich › Amtsgericht – Schöffengericht")], rechts_frei([
    *tafel("e12", "Prognose der Staatsanwältin"),
    pl("Einzelstrafen: je um 1 Jahr", 110, 180, beim("e12", "Einzelstrafen"), fill=BLAU, size=32),
    z("ihre Einschätzung im Einzelfall, keine feste Regel", 110, 262, "e13", size=30, farbe=TEXT),
    *achse,
    blk(int(jahr(2.5)), AY - 78, int(jahr(3.5) - jahr(2.5)), 62, LILA, GES, [("2,5–3,5 J.", "ExtraBold", 30, INK)],
        anim="pop"),
    linienzug([(jahr(2), AY - 110), (jahr(2), AY + 50)], "f2", breite=6, farbe=DROT),
    z("Grenze Strafrichter", jahr(2) - F("Bold", 28).getlength("Grenze Strafrichter") / 2, AY + 60, "f2", "Bold", 28),
    linienzug([(jahr(4), AY - 110), (jahr(4), AY + 50)], "f3", breite=6, farbe=DROT),
    z("Strafbann AG", jahr(4) - F("Bold", 28).getlength("Strafbann AG") / 2, AY + 60, "f3", "Bold", 28),
    *neinz("über 2 Jahre: nicht der Strafrichter", 540, beim("f2", "Über"), "Bold", 34, x=160),
    *neinz("nicht über 4 Jahre: kein Landgericht nach Nr. 2", 600, beim("f3", "Nicht"), "Bold", 34, x=160),
    *neinz("besonderer Umfang, besondere Bedeutung: nicht ersichtlich", 660, beim("f4", "nichts"), "Bold", 34, x=160),
    blk(110, 735, 1040, 90, GRUEN, "f5", [("Sachlich: Amtsgericht – Schöffengericht", "ExtraBold", 38, INK)]),
    *requisit([("e12", ("tabler", "hourglass", 90, WEISS), "Prognose", WEISS),
               (GES, ("tabler", "hourglass", 90, LILA), "2,5–3,5 Jahre", LILA),
               ("f1", ("tabler", "stairs-up", 110, WEISS), "Welche Stufe?", WEISS),
               ("f5", ("tabler", "gavel", 110, GRUEN), "Schöffengericht", GRUEN)]),
    *paar("e12", "HA", [("e12", "schreck"), ("f5", "denkt")], "EG", [("e12", "denkt"), ("f5", "froh")]),
]))

# ===========================================================================================================================
# J II. Örtliche Zuständigkeit, §§ 7, 8, 3, 13 StPO
# ===========================================================================================================================
BZ = (110, 640, 1040, 230)
folie([("o1", "II. Örtlich › §§ 7 ff. StPO"), ("o2", "II. Örtlich › Tatort, § 7 Abs. 1 StPO"),
       ("o3", "II. Örtlich › Wohnsitz, § 8 Abs. 1 StPO"), ("o4", "II. Örtlich › Zusammenhang, §§ 3, 13 StPO")],
      rechts_frei([
    *tafel("o1", "II. Örtliche Zuständigkeit"),
    z("Tatort, § 7 Abs. 1 StPO", 110, 185, beim("o2", "Tatort"), "Bold", 36),
    *okz("alle 12 Taten in Erlenstadt", 238, beim("o2", "Alle"), size=34, x=160),
    z("Wohnsitz bei Klageerhebung, § 8 Abs. 1 StPO", 110, 305, beim("o3", "Wohnsitz"), "Bold", 36),
    *okz("Herr Hartung wohnt in Erlenstadt", 358, beim("o3", "Auch"), size=34, x=160),
    z("Tatorte in verschiedenen Bezirken? Zusammenhang:", 110, 430, "o4", "Bold", 34),
    z("jedes Gericht, das für eine der Taten zuständig wäre", 110, 480, beim("o4", "ist"), size=34),
    zit("§§ 3, 13 Abs. 1 StPO", 110, 530, beim("o4", "Paragrafen")),
    karte(BZ[0], BZ[1], BZ[2], BZ[3], beim("o2", "Alle"), fill=HELLGRUEN, rund=30, schatten=6, rand=4),
    pl("Bezirk Erlenstadt", BZ[0] + 30, BZ[1] + 20, beim("o2", "Alle"), fill=WEISS, size=30),
    *[dicon("tabler", "map-pin", 180 + (i % 6) * 120 + (i // 6) * 60, 790 + (i // 6) * 70, 50, beim("o2", "zwölf"),
            fuell=ROT) for i in range(12)],
    dicon("tabler", "home", 1060, 840, 110, beim("o3", "Wohnsitz"), fuell=GELB),
    *requisit([("o1", ("tabler", "map-pin", 90, ROT), "Welcher Ort?", WEISS),
               ("o2", ("tabler", "map-pins", 100, ROT), "Tatort", WEISS),
               ("o3", ("tabler", "home", 100, GELB), "Wohnsitz", WEISS),
               ("o4", ("tabler", "map-2", 100, WEISS), "Zusammenhang", WEISS)]),
    *paar("o1", "HA", [("o1", "ruhig"), ("o3", "denkt")], "EG", [("o1", "ruhig"), ("o2", "denkt"), ("o4", "ernst")]),
]))

# ===========================================================================================================================
# K III. Die Anklage
# ===========================================================================================================================
folie([("an1", "III. Anklage › Gericht, § 200 Abs. 1 Satz 2 StPO"), ("an3", "III. Anklage › Klausurkonvention")],
      rechts_frei([
    *tafel("an1", "III. Gericht in der Anklage"),
    z("Die Anklageschrift nennt das Gericht", 110, 190, "an1", "Bold", 36),
    zit("§ 200 Abs. 1 Satz 2 StPO", 110, 245, beim("an1", "Paragraf")),
    z("… samt Spruchkörper", 110, 310, "an2", "Bold", 36),
    zit("Nr. 110 Abs. 3 RiStBV", 110, 365, beim("an2", "Richtlinien")),
    karte(160, 440, 940, 230, "e_2", fill=WEISS, rund=12, schatten=6, rand=4),
    z("Anklageschrift", 200, 465, "e_2", "ExtraBold", 36),
    z("Anklage zum Amtsgericht – Schöffengericht –", 200, 535, beim("e_2", "Amtsgericht"), "Bold", 36, rechts=1080),
    z("Erlenstadt", 200, 590, beim("e_2", "Erlenstadt"), "Bold", 36, rechts=1080),
    blk(110, 720, 1040, 80, LILA, "an3", [("Genaue Formel: Klausurkonvention", "ExtraBold", 36, INK)]),
    *fig("EG", FX, FB, FR, [("an1", "ruhig"), ("an2", "denkt")], bis="e_2"),
    ns("Staatsanwältin Eggert", FX, FB, "an1", EG_N, d=0.1),
    *redet("EG_redet", FX, FB, FR, "e_2", "an3"),
    blase("sprech", 600, 260, "e_2", 1560, 230, inhalt=["Anklage zum Amtsgericht –", "Schöffengericht –", "Erlenstadt."],
          textsize=36, figur=("EG_redet", FX, FB, FR), bis="an3"),
    *fig("EG", FX, FB, FR, [("an3", "froh")], erst="cut"),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Straferwartung begründen"), ("tipp3", "Klausurtipp · bewegliche Zuständigkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Straferwartung konkret begründen:", 200, 200, beim("tipp", "Begründe"), "Bold", 36),
    z("Strafrahmen, Vorstrafen, Gesamtstrafe", 200, 255, beim("tipp", "Strafrahmen"), size=34),
    z("Eine Zahl ohne Begründung überzeugt nicht.", 200, 315, "tipp2", "Bold", 34),
    linienzug([(130, 390), (1130, 390)], "tipp3", breite=3),
    z("Nr. 3: die bewegliche Zuständigkeit", 200, 420, "tipp3", "Bold", 36),
    zit("vgl. BVerfG, Beschl. v. 1.3.2011 – 2 BvR 1/11, Rn. 13", 200, 472, beim("tipp3", "bewegliche")),
    z("Gründe in den Akten festhalten", 200, 530, beim("tipp3", "hält"), size=34),
    zit("Nr. 113 Abs. 2 RiStBV", 200, 580, beim("tipp3", "Akten")),
    z("Das Gericht prüft sie bei der Eröffnung.", 200, 640, "tipp4", "Bold", 34),
    zit("§ 209 StPO; BGH, Beschl. v. 6.10.2016 – 2 StR 330/16, Rn. 11", 200, 692, beim("tipp4", "Eröffnung")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (Treppe)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Sachlich", "GVG, § 1 StPO", BLAU, 0),
          ("k11", "1.", "Sonderzuweisungen", "§ 24 Abs. 1 Satz 1 Nr. 1 GVG", None, 1),
          ("k12", "2.", "Straferwartung: Strafrahmen, Vorstrafen, Gesamtstrafe", "§§ 263, 46, 53, 54 StGB", None, 1),
          ("k13", "3.", "die Stufe", "§§ 25, 28, 24, 74 GVG", None, 2),
          ("k14", "4.", "besondere Bedeutung, Umfang, Schutzbedürftigkeit", "§ 24 Abs. 1 Satz 1 Nr. 3 GVG", None, 1),
          ("k2", "II.", "Örtlich: Tatort, Wohnsitz, Zusammenhang", "§§ 7, 8, 3, 13 StPO", GRUEN, 0),
          ("k3", "III.", "Das Gericht in der Anklage", "§ 200 Abs. 1 Satz 2 StPO", GELB, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Zuständigkeit"), 110, 90, "sch", 50)]
y = 190
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 100, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 160 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 245, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 92
    else:
        els_sch += [z(r, 260, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 320, y + 4, c, "Bold", 36, rechts=1820)]
        hh = 72
    if ebene == 2:                                      # kleine Treppe: drei Stufen, nacheinander zum Wort
        for k, (n, u, fa, w_) in enumerate([("Strafrichter", "bis 2 Jahre", BLAU, "Strafrichter"),
                                            ("Schöffengericht", "bis 4 Jahre", GRUEN, "Schöffengericht"),
                                            ("Landgericht", "darüber", GELB, "Landgericht")]):
            top = y + 95 - k * 40
            els_sch.append(blk(520 + k * 300, top, 290, y + 175 - top, fa, beim("k13", w_), [(n, "ExtraBold", 28, INK),
                                                                                         (u, "Bold", 26, INK)], anim="pop"))
        hh = 182
    if norm:
        ende_ = (245 + F("ExtraBold", 40).getlength(kopf)) if ebene == 0 else (320 + F("Bold", 36).getlength(kopf))
        els_sch.append(zit(norm, max(1260, int(ende_) + 40) if ebene != 2 else int(ende_) + 40, y + (18 if ebene == 0 else 12), c, size=28, rechts=1830))
    y += hh
assert y <= 975, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Sachlich"), ("k2", "Klausurschema › II. Örtlich"),
       ("k3", "Klausurschema › III. Anklage")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Straferwartung", 0)], [("bestimmt die Stufe.", "a")]],
                750, 290, 44, "merke", {"a": beim("merke", "bestimmt")}),
    *markertext([[("Bei Vergehen bis 2 Jahre der Strafrichter,", 0)],
                 [("bis 4 Jahre das ", 0), ("Schöffengericht", "b"), (",", 0)], [("darüber das Landgericht.", 0)]],
                750, 450, 38, "mk2", {"b": beim("mk2", "Schöffengericht")}),
    *markertext([[("Und jede Prognose", 0)], [("braucht eine Begründung.", "c")]], 750, 700, 42, "mk3",
                {"c": beim("mk3", "Begründung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
