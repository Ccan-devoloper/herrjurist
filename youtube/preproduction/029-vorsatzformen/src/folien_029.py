"""Folge 029 · Vorsatzformen: Absicht, direkter Vorsatz, Eventualvorsatz erklärt – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Die alte Mauer (Fall), B Sachverhalt, C Sachbeschädigung und § 15 (Wortlautkarten § 303 I,
§ 15), D Wissen und Wollen, E Variante 1 Absicht, F Variante 2 direkter Vorsatz, G Lehrbuchbeispiel Thomas-Fall (nur Icons,
keine Figuren, keine Explosion), H Variante 3 Eventualvorsatz, I Variante 4 bewusste Fahrlässigkeit, J Gesamtschau,
K Tatumstandsirrtum (Wortlautkarte § 16 I), L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Vorschlaghammer, Mauer stürzt auf den Zaun, Seil reißt – Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_029/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (222, 170, 118, 255)
STEIN = (214, 196, 178, 255)
SEIL = (150, 98, 52, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())
_ERSATZ_OK = {"→"}


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen); nur „→“ kommt aus der Ersatzschrift (nur über zeile())."""
    fehl = {c for c in text if ord(c) not in _CMAP and c not in _ERSATZ_OK and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert "→" not in text, "→ nur über zeile() (Ersatzschrift)"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def dreh(e, winkel):
    """Requisit kippen (Bibliotheks-Icon nur gedreht, nicht umgezeichnet); Fußpunkt unten mittig bleibt stehen."""
    cx, unten = e.x + e.sprite.width / 2, e.y + e.sprite.height
    e.sprite = e.sprite.rotate(winkel, resample=Image.BICUBIC, expand=True)
    e.sprite = e.sprite.crop(e.sprite.getbbox())
    e.x, e.y = int(round(cx - e.sprite.width / 2)), int(round(unten - e.sprite.height))
    e.name = (e.name or "") + f":dreh{winkel}"
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=31, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(zeile, wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
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


# --- Eigene Hilfsfunktion (wie Folge 022/026): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


BODEN, FH = 880, 430
FX, BR, FR = 1560, 930, 470                 # Figur rechts neben der Tafel
NAMEN = {"VO": ("Volker", BLAU), "HE": ("Heike", LILA)}


def name(p, cx, cue, unten=BODEN, size=28, d=0.2, bis=None, anim="pop", text=None):
    t, f = NAMEN[p]
    return pl(text or t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def mauer(cx, unten, breite, cue, anim="pop", bis=None, winkel=0):
    e = ficon("tabler", "wall", cx, unten, breite, cue, fuell=STEIN, nebenfarbe=STEIN, anim=anim, bis=bis)
    return dreh(e, winkel) if winkel else e


def zaun(cx, unten, breite, cue, anim="pop", bis=None, kaputt=False):
    return ficon("tabler", "fence-off" if kaputt else "fence", cx, unten, breite, cue, fuell=HOLZ, nebenfarbe=HOLZ,
                 anim=anim, bis=bis)


# A Fall: die alte Mauer ------------------------------------------------------------------------------------------------
HEX, VOX = 330, 1330                        # Heike links vor ihrem Zaun, Volker rechts in seinem Garten
ZX = (640, 790, 940)                        # Zaunfelder
MX = 1090                                   # Mauer
HEb = ("HE_redet_r", HEX, BODEN, FH)
HEr = ("HE_ruft_r", HEX, BODEN, FH)
VOb = ("VO_redet", VOX, BODEN, FH)
folie([(NULL, "Fall · Die alte Mauer"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=6, farbe=INK)),
    hart(pl("Samstagmorgen", 70, 40, NULL, fill=GELB, size=40, anim="cut")),
    hart(ficon("tabler", "sun", 1790, 200, 120, NULL, fuell=GELB, anim="cut")),
    hart(ficon("ph", "house", 1730, BODEN, 260, NULL, fuell=WEISS, nebenfarbe=BLAU, anim="cut")),
    hart(ficon("tabler", "tree", 1530, BODEN, 170, NULL, fuell=GRUEN, anim="cut")),
    hart(pl("Reihenhaussiedlung", 70, 120, NULL, fill=WEISS, size=30, anim="cut")),
    # Mauer: steht – kippt – liegt auf dem Zaun
    hart(mauer(MX, BODEN, 280, NULL, anim="cut", bis=beim("kippt", "kippt"))),
    hart(mauer(MX - 50, BODEN, 280, beim("kippt", "kippt"), anim="cut", bis=beim("kippt", "genau"), winkel=22)),
    *[hart(zaun(x, BODEN, 150, NULL, anim="cut", bis="bruch")) for x in ZX],
    hart(zaun(ZX[0], BODEN, 150, "bruch", anim="cut")),
    *[hart(zaun(x, BODEN, 150, "bruch", anim="cut", kaputt=True)) for x in ZX[1:]],
    szene(hart(mauer(860, BODEN, 280, beim("kippt", "genau"), anim="cut", winkel=78)), "029mauer*", 1.0, 0.0),
    pl("alte Mauer", MX, 560, beim("volker", "Mauer"), fill=WEISS, size=28, anker="m", bis=beim("kippt", "kippt")),
    pl("neuer Holzzaun", 790, 640, beim("heike", "Holzzaun"), fill=HOLZ, size=28, anker="m", bis=beim("kippt", "genau")),
    pl("drei Latten gebrochen", 830, 560, "bruch", fill=ROT, size=28, anker="m", bis="frage"),
    # Volker
    *fig("VO", VOX, BODEN, FH, [("volker", "ruhig")], bis="v1"),
    *redet("VO_redet", VOX, BODEN, FH, "v1", "hammer"),
    *fig("VO", VOX, BODEN, FH, [("hammer", "arbeit"), (beim("kippt", "genau"), "schreck"), ("frage", "denkt")], erst="cut"),
    name("VO", VOX, "volker", text="Volker, Anfang 60"),
    szene(ficon("tabler", "hammer", VOX - 110, 720, 90, beim("hammer", "schlägt"), fuell=GRAU, bis=beim("kippt", "genau")),
          "029hammer*", 1.0, 0.0),
    pl("untere Steine heraus", MX, 560, beim("hammer", "Steine"), fill=GELB, size=28, anker="m", bis=beim("kippt", "kippt")),
    # Heike
    *fig("HE", HEX, BODEN, FH, [("heike", "ruhig_r")], bis="h1"),
    *redet("HE_redet_r", HEX, BODEN, FH, "h1", "v1"),
    *fig("HE", HEX, BODEN, FH, [("v1", "skeptisch_r")], bis="h2", erst="cut"),
    *redet("HE_ruft_r", HEX, BODEN, FH, "h2", "frage"),
    *fig("HE", HEX, BODEN, FH, [("frage", "traurig_r")], erst="cut"),
    name("HE", HEX, "heike", text="Heike, Nachbarin"),
    blase("sprech", 600, 210, "h1", 560, 250, inhalt=["Pass bitte auf", "meinen Zaun auf!"], textsize=38, figur=HEb, bis="v1"),
    blase("sprech", 640, 170, "v1", 1300, 270, inhalt=["Die Mauer muss heute weg."], textsize=36, figur=VOb, bis="hammer"),
    blase("sprech", 480, 170, "h2", 520, 270, inhalt=["Mein neuer Zaun!"], textsize=40, figur=HEr, bis="frage"),
    # Frage
    pl("Hat Volker den Zaun vorsätzlich beschädigt?", 960, 200, "frage", fill=PINK, size=36, anker="m"),
    ficon("tabler", "brain", VOX, 360, 90, "frage2", fuell=PINK),
    pl("Was wusste er?", VOX - 150, 400, beim("frage2", "wusste"), fill=WEISS, size=28, anker="m"),
    pl("Was wollte er?", VOX + 170, 400, beim("frage2", "wollte"), fill=WEISS, size=28, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Volker (Anfang 60) schlägt die unteren Steine seiner alten Gartenmauer heraus. Die Mauer kippt auf den neuen "
    "Holzzaun seiner Nachbarin Heike, drei Latten brechen.",
    "Variante 1: Der Zaun ärgert Volker, die Mauer soll genau dorthin fallen. Variante 2: Die Mauer kann nur zum Zaun "
    "hin fallen, Volker weiß das sicher. Variante 3: Volker hält das für möglich, Abstützen ist ihm zu mühsam. "
    "Variante 4: Volker sichert die Mauer mit einem Seil und vertraut darauf; das Seil reißt.",
    "Gegenstück: Volker hält den Zaun nach einem alten Grenzplan für seinen eigenen.",
], "Hat Volker den Zaun vorsätzlich beschädigt?")

# C Sachbeschädigung, § 303 I und § 15 -----------------------------------------------------------------------------------
PA = "A. Sachbeschädigung, § 303 StGB"
P303 = ["„Wer rechtswidrig eine fremde Sache beschädigt oder zerstört, wird", "mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft.“"]
wl303, y303 = wortlaut(100, 180, 1060, P303, "§ 303 Abs. 1 StGB", beim("p303", "Sachbeschädigung"),
                       marken=[(0, "fremde Sache", beim("objektiv", "fremde")), (0, "beschädigt", beim("objektiv", "beschädigt"))])
P15 = ["„Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz", "fahrlässiges Handeln ausdrücklich mit Strafe bedroht.“"]
wl15, y15 = wortlaut(100, y303 + 120, 1060, P15, "§ 15 StGB", beim("p15", "Paragraf"),
                     marken=[(0, "vorsätzliches Handeln", beim("p15", "vorsätzliches")),
                             (1, "fahrlässiges Handeln ausdrücklich", beim("p15", "fahrlässiges"))])
folie([("p303", f"{PA} › objektiver Tatbestand"), ("p15", f"{PA} › subjektiver Tatbestand: Vorsatz, § 15 StGB")], [
    *tafel("p303", "Sachbeschädigung"),
    *wl303,
    ok(135, y303 + 47, "objektiv", gr=22), z("Objektiv: fremde Sache, beschädigt", 175, y303 + 24, "objektiv", "Bold", 36),
    *wl15,
    fl_block(110, y15 + 30, 1040, 100, GELB, "keinef", [("keine fahrlässige Sachbeschädigung", "ExtraBold", 38, INK)]),
    *fig("VO", 1780, BR, 430, [("p303", "denkt"), ("p15", "ertappt")]),
    name("VO", 1780, "p303", unten=BR),
    zaun(1460, 560, 220, beim("objektiv", "Zaun"), kaputt=True),
    pl("fremde Sache", 1460, 600, beim("objektiv", "fremde"), fill=HOLZ, size=28, anker="m"),
    pl("beschädigt", 1460, 670, beim("objektiv", "beschädigt"), fill=ROT, size=28, anker="m"),
    pl("Vorsatz?", 1460, 220, "p15", fill=PINK, size=34, anker="m"),
])

# D Wissen und Wollen ----------------------------------------------------------------------------------------------------
PV = "A. Sachbeschädigung › Vorsatz"


def balken(x, y, w, cue, voll, farbe, bis=None):
    """Pegel aus zwei Karten (leer/gefüllt) für die Stärke von Wissen bzw. Wollen."""
    return [bis_(karte(x, y, w, 44, cue, fill=WEISS, rund=14, schatten=0, rand=4), bis),
            bis_(karte(x, y, max(30, int(w * voll)), 44, cue, fill=farbe, rund=14, schatten=0, rand=4), bis)]


folie([("ww", f"{PV}: Wissen und Wollen")], [
    *tafel("ww", "Vorsatz"),
    z("Wissen und Wollen", 110, 200, beim("ww", "Wissen"), "ExtraBold", 44),
    z("der Tatbestandsverwirklichung", 110, 265, beim("ww", "Tatbestandsverwirklichung"), size=38),
    z("Wissen", 110, 395, beim("formen", "Wissen"), "Bold", 36),
    *balken(330, 390, 700, beim("formen", "Wissen"), 0.6, BLAU),
    z("Wollen", 110, 475, beim("formen", "Wollen"), "Bold", 36),
    *balken(330, 470, 700, beim("formen", "Wollen"), 0.85, GRUEN),
    pl("wie stark ausgeprägt?", 330, 545, beim("formen", "ausgeprägt"), fill=WEISS, size=30),
    fl_block(110, 650, 1040, 100, GELB, beim("formen", "drei"), [("drei Vorsatzformen", "ExtraBold", 40, INK)]),
    *fig("VO", FX, BR, FR, [("ww", "ruhig"), (beim("formen", "Spielen"), "froh")]),
    name("VO", FX, "ww", unten=BR),
    ficon("tabler", "brain", 1360, 330, 110, beim("ww", "Wissen"), fuell=BLAU),
    pl("Wissen", 1360, 360, beim("ww", "Wissen"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "target", 1780, 330, 110, beim("ww", "Wollen"), fuell=GRUEN),
    pl("Wollen", 1780, 360, beim("ww", "Wollen"), fill=GRUEN, size=28, anker="m"),
])

# Mini-Bühne rechts für die Varianten: Zaun – Mauer – Volker (blickt nach links zur Mauer) -----------------------------
ZV, MV, VV, BV, HV = 1330, 1480, 1790, 840, 430   # Zaun x, Mauer x, Volker x, Boden y, Volker Höhe


def buehne(cue, bis=None, mauer_winkel=0, kaputt=False):
    return [hart(linienzug([(1250, BV), (1880, BV)], cue, breite=5, farbe=INK)),
            zaun(ZV, BV, 140, cue, kaputt=kaputt, bis=bis),
            mauer(MV, BV, 170, cue, winkel=mauer_winkel, bis=bis)]


# E Variante 1: Absicht --------------------------------------------------------------------------------------------------
VOb1 = ("VO_grimmig", VV, BV, HV)
folie([("var1", f"{PV} › Variante 1"), ("abs", f"{PV} › Variante 1: Absicht (dolus directus 1. Grades)")], [
    *tafel("var1", "Variante 1: Der Zaun ärgert ihn"),
    z("Der Zaun ärgert Volker schon lange", 110, 190, "var1", size=36),
    z("„Genau dorthin soll die Mauer fallen.“", 110, 245, beim("v2", "Genau"), "Bold", 36),
    ok(135, 343, "abs", gr=22), z("Es kommt ihm gerade darauf an", 175, 320, "abs", "Bold", 38),
    fl_block(110, 400, 1040, 90, GELB, beim("abs", "Absicht"), [("Absicht = dolus directus 1. Grades", "ExtraBold", 38, INK)]),
    z("BGH, 2 StR 150/15, Rn. 17", 110, 510, beim("abs", "Absicht"), "Bold", 27, farbe=TEXT),
    z("Wissen: für möglich halten genügt", 110, 600, "abs2", size=36),
    *balken(110, 660, 500, beim("abs2", "möglich"), 0.4, BLAU),
    z("Entscheidend: das Wollen", 110, 740, beim("abs2", "Entscheidend"), "Bold", 36),
    *balken(110, 800, 500, beim("abs2", "Wollen"), 1.0, GRUEN),
    *buehne("var1"),
    *fig("VO", VV, BV, HV, [("var1", "arbeit")], bis="v2"),
    *redet("VO_grimmig", VV, BV, HV, "v2", "abs"),
    *fig("VO", VV, BV, HV, [("abs", "arbeit")], erst="cut"),
    name("VO", VV, "var1", unten=BV),
    ficon("tabler", "target", ZV, 600, 90, beim("v2", "dorthin"), fuell=ROT),
    blase("sprech", 560, 200, "v2", 1560, 250, inhalt=["Genau dorthin soll", "die Mauer fallen."], textsize=36, figur=VOb1, bis="abs"),
    pl("es kommt ihm darauf an", 1560, 230, "abs", fill=GRUEN, size=30, anker="m"),
])

# F Variante 2: direkter Vorsatz -----------------------------------------------------------------------------------------
VOb2 = ("VO_bedauert", VV, BV, HV)
folie([("var2", f"{PV} › Variante 2"), ("dir", f"{PV} › Variante 2: direkter Vorsatz (dolus directus 2. Grades)")], [
    *tafel("var2", "Variante 2: Die Mauer steht schief"),
    z("Volker hat nichts gegen den Zaun", 110, 190, "var2", size=36),
    z("Die Mauer kann nur zum Zaun hin fallen", 110, 245, beim("var2", "Aber"), size=36),
    ok(135, 323, "sicher", gr=22), z("Das weiß er sicher", 175, 300, "sicher", "Bold", 38),
    z("sieht die Beschädigung als sicher voraus", 110, 385, "dir", size=36),
    fl_block(110, 445, 1040, 90, LILA, beim("dir", "direkter"), [("direkter Vorsatz = dolus directus 2. Grades", "ExtraBold", 36, INK)]),
    z("BGH, 2 StR 150/15, Rn. 17", 110, 555, beim("dir", "direkter"), "Bold", 27, farbe=TEXT),
    z("Erfolg unerwünscht? Ändert nichts.", 110, 640, "dir2", "Bold", 36),
    z("BGH, 2 StR 150/15, Rn. 32", 110, 700, beim("dir2", "ändert"), "Bold", 27, farbe=TEXT),
    hart(linienzug([(1250, BV), (1880, BV)], "var2", breite=5, farbe=INK)),
    zaun(ZV, BV, 140, "var2"),
    mauer(MV - 10, BV, 170, beim("var2", "schief"), winkel=14),
    mauer(MV, BV, 170, "var2", bis=beim("var2", "schief")),
    pfeil_ink(MV - 60, 560, ZV + 40, 620, beim("var2", "nur")),
    pl("nur zum Zaun hin", 1480, 470, beim("var2", "nur"), fill=WEISS, size=28, anker="m"),
    *fig("VO", VV, BV, HV, [("var2", "ruhig")], bis="v3"),
    *redet("VO_bedauert", VV, BV, HV, "v3", "dir"),
    *fig("VO", VV, BV, HV, [("dir", "ertappt")], erst="cut"),
    name("VO", VV, "var2", unten=BV),
    pl("weiß es sicher", 1560, 330, "sicher", fill=LILA, size=30, anker="m", bis="v3"),
    blase("sprech", 600, 200, "v3", 1560, 250, inhalt=["Schade um den Zaun.", "Aber die Mauer muss weg."], textsize=34,
          figur=VOb2, bis="dir"),
    pl("sicher vorausgesehen", 1560, 250, "dir", fill=LILA, size=30, anker="m"),
])

# G Lehrbuchbeispiel: Thomas-Fall (keine Figur, keine Explosion, keine Opfer im Bild) -----------------------------------
PT = "Lehrbuchbeispiel · Thomas-Fall, Bremerhaven 1875"
folie([("thomas", PT), ("th_wiss", f"{PT} › direkter Vorsatz")], [
    *tafel("thomas", "Thomas-Fall, Bremerhaven 1875"),
    pl("klassisches Lehrbuchbeispiel", 110, 175, beim("thomas", "Lehrbuchbeispiel"), fill=GELB, size=32),
    z("hoch versichertes Fass", 110, 280, beim("fass", "hoch"), "Bold", 36),
    z("mit Sprengstoff und Uhrwerk", 110, 330, beim("fass", "Sprengstoff"), size=36),
    z("auf ein Auswandererschiff", 110, 380, beim("fass", "Auswandererschiff"), size=36),
    z("Plan: Explosion auf dem Ozean", 110, 460, "plan", "Bold", 36),
    z("Ziel: die Versicherungssumme", 110, 510, beim("plan", "Versicherungssumme"), size=36),
    z("Tod der Menschen an Bord: nicht sein Ziel", 110, 590, "th_ziel", size=36),
    z("(Lehrbuchdeutung)", 110, 640, beim("th_ziel", "Lehrbuchdeutung"), size=30, farbe=TEXT),
    ok(135, 723, "th_wiss", gr=22), z("Plan aufgegangen: sicher, und er wusste es", 175, 700, "th_wiss", "Bold", 36),
    fl_block(110, 775, 1040, 90, LILA, beim("th_wiss", "direkter"), [("direkter Vorsatz", "ExtraBold", 38, INK)]),
    ficon("tabler", "ship", 1560, 565, 300, "thomas", fuell=WEISS, nebenfarbe=BLAU),
    hart(linienzug([(1290, 600), (1380, 580), (1470, 600), (1560, 580), (1650, 600), (1740, 580), (1830, 600)], beim("plan", "Ozean"),
                   breite=8, farbe=BLAU)),
    pl("Ozean", 1560, 620, beim("plan", "Ozean"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "barrel", 1400, 860, 120, beim("fass", "Fass"), fuell=HOLZ),
    ficon("tabler", "clock", 1520, 860, 90, beim("fass", "Uhrwerk"), fuell=WEISS),
    ficon("tabler", "file-certificate", 1660, 860, 90, beim("fass", "versichertes"), fuell=WEISS),
    ficon("tabler", "coins", 1790, 860, 100, beim("plan", "Versicherungssumme"), fuell=GELB),
    pl("Versicherungssumme", 1720, 900, beim("plan", "Versicherungssumme"), fill=GELB, size=26, anker="m"),
    pl("Bremerhaven 1875", 1560, 100, "thomas", fill=WEISS, size=30, anker="m"),
    pl("sicher vorausgesehen", 1560, 180, "th_wiss", fill=LILA, size=30, anker="m"),
])

# H Variante 3: Eventualvorsatz -----------------------------------------------------------------------------------------
VOb3 = ("VO_egal", VV, BV, HV)
folie([("var3", f"{PV} › Variante 3"), ("ev", f"{PV} › Variante 3: Eventualvorsatz")], [
    *tafel("var3", "Variante 3: Abstützen? Zu mühsam."),
    z("Volker hält für möglich, dass die Mauer kippt", 110, 190, "var3", size=36),
    z("Abstützen ist ihm zu mühsam", 110, 245, beim("var3", "Abstützen"), size=36),
    fl_block(110, 320, 1040, 90, GRUEN, "ev", [("Eventualvorsatz", "ExtraBold", 40, INK)]),
    z("BGH: erkennt den Erfolg als möglich", 110, 440, "ev2", "Bold", 36),
    z("und nicht ganz fernliegend", 150, 492, beim("ev2", "nicht"), size=36),
    z("und billigt ihn oder findet sich mit ihm ab,", 110, 560, "ev3", "Bold", 36),
    z("mag er ihm auch unerwünscht sein", 150, 612, beim("ev3", "mag"), size=36),
    pl("ständige Rechtsprechung", 110, 690, "raser", fill=GELB, size=30),
    z("BGH, 4 StR 399/17, Rn. 18 (BGHSt 63, 88 – Berliner Raser)", 110, 780, beim("raser", "Berliner"), "Bold", 27, farbe=TEXT),
    z("BGH, 4 StR 558/11, Rn. 30 (BGHSt 57, 183)", 110, 820, beim("raser", "Berliner"), "Bold", 27, farbe=TEXT),
    *buehne("var3"),
    ficon("tabler", "help-circle", MV, 590, 70, beim("var3", "möglich"), fuell=GELB),
    *fig("VO", VV, BV, HV, [("var3", "denkt")], bis="v4"),
    *redet("VO_egal", VV, BV, HV, "v4", "ev"),
    *fig("VO", VV, BV, HV, [("ev", "egal")], erst="cut"),
    name("VO", VV, "var3", unten=BV),
    blase("sprech", 580, 200, "v4", 1560, 250, inhalt=["Wenn es den Zaun", "erwischt, dann eben."], textsize=36,
          figur=VOb3, bis="ev"),
    pl("möglich", 1440, 260, "ev2", fill=BLAU, size=30, anker="m"),
    pl("findet sich ab", 1680, 260, beim("ev3", "findet"), fill=GRUEN, size=30, anker="m"),
])

# I Variante 4: bewusste Fahrlässigkeit -------------------------------------------------------------------------------
BX4 = 1630                                   # Baum
VX4 = 1810
VOb4 = ("VO_zuversicht", VX4, BV, 400)
folie([("var4", f"{PV} › Variante 4"), ("fahrl", f"{PV} › Variante 4: bewusste Fahrlässigkeit")], [
    *tafel("var4", "Variante 4: das Seil"),
    z("Volker sieht dieselbe Gefahr", 110, 190, "var4", size=36),
    z("Seil an den Baum: Mauer soll zu ihm fallen", 110, 245, beim("var4", "Deshalb"), size=36),
    nein(135, 323, "reisst", gr=22), z("Das Seil reißt", 175, 300, "reisst", "Bold", 38),
    z("ernsthaft und nicht nur vage vertraut,", 110, 385, "fahrl", "Bold", 36),
    z("dass nichts passiert", 150, 437, beim("fahrl", "dass"), size=36),
    z("BGH, 4 StR 399/17, Rn. 18 (BGHSt 63, 88)", 110, 492, beim("fahrl", "dass"), "Bold", 27, farbe=TEXT),
    fl_block(110, 545, 1040, 90, WEISS, beim("fahrl", "bewusste"), [("bewusste Fahrlässigkeit", "ExtraBold", 40, INK)]),
    nein(135, 678, beim("fahrl", "kein"), gr=22), z("kein Vorsatz", 175, 655, beim("fahrl", "kein"), "Bold", 36),
    z("wegen Sachbeschädigung: nicht strafbar", 110, 735, "straflos", "Bold", 36),
    z("Schadensersatz: Zivilrecht, § 823 Abs. 1 BGB", 110, 800, beim("straflos", "Schadensersatz"), size=34, farbe=TEXT),
    hart(linienzug([(1250, BV), (1880, BV)], "var4", breite=5, farbe=INK)),
    zaun(ZV, BV, 140, "var4", bis=beim("reisst", "reißt")),
    hart(zaun(ZV, BV, 140, beim("reisst", "reißt"), kaputt=True)),
    mauer(MV, BV, 150, "var4", bis=beim("reisst", "reißt")),
    hart(mauer(ZV + 40, BV, 150, beim("reisst", "reißt"), winkel=70)),
    ficon("tabler", "tree", BX4, BV, 170, "var4", fuell=GRUEN),
    bis_(linienzug([(MV + 55, BV - 125), (BX4 - 6, BV - 45)], beim("var4", "Seil"), breite=10, farbe=SEIL), beim("reisst", "reißt")),
    szene(hart(linienzug([(BX4 - 62, BV - 18), (BX4 - 6, BV - 45)], beim("reisst", "reißt"), breite=10, farbe=SEIL)),
          "029seil*", 1.0, 0.0),
    pl("Seil", 1560, 610, beim("var4", "Seil"), fill=HOLZ, size=26, anker="m", bis=beim("reisst", "reißt")),
    pl("reißt", 1560, 610, beim("reisst", "reißt"), fill=ROT, size=26, anker="m"),
    *fig("VO", VX4, BV, 400, [("var4", "denkt")], bis="v5"),
    *redet("VO_zuversicht", VX4, BV, 400, "v5", "reisst"),
    *fig("VO", VX4, BV, 400, [("reisst", "schreck"), ("straflos", "ertappt")], erst="cut"),
    name("VO", VX4, "var4", unten=BV),
    blase("sprech", 560, 200, "v5", 1540, 250, inhalt=["Mit dem Seil kann", "nichts passieren."], textsize=36,
          figur=VOb4, bis="reisst"),
    pl("vertraut ernsthaft", 1560, 250, "fahrl", fill=WEISS, size=30, anker="m"),
])

# J Abgrenzung: Gesamtschau ---------------------------------------------------------------------------------------------
folie([("gesamt", f"{PV} › Abgrenzung: Gesamtschau")], [
    *tafel("gesamt", "Billigen oder vertrauen?"),
    z("Gesamtschau aller objektiven", 110, 190, beim("gesamt", "Gesamtschau"), "Bold", 38),
    z("und subjektiven Umstände", 110, 245, beim("gesamt", "subjektiven"), "Bold", 38),
    z("BGH, 4 StR 399/17, Rn. 20 (BGHSt 63, 88)", 110, 305, beim("gesamt", "Umstände"), "Bold", 27, farbe=TEXT),
    z("Indizien:", 110, 380, "indiz", "Bold", 36),
    z("Gefährlichkeit der Handlung (wesentlich)", 150, 435, beim("indiz", "Gefährlichkeit"), size=36),
    z("Motiv", 150, 487, beim("indiz", "Motiv"), size=36),
    z("konkrete Umstände", 150, 539, beim("indiz", "konkreten"), size=36),
    ok(135, 643, "seil", gr=22), z("Seil (Variante 4): für Vertrauen", 175, 620, "seil", "Bold", 36),
    nein(135, 713, beim("seil", "sein"), gr=22),
    z("„dann eben“ (Variante 3): dagegen", 175, 690, beim("seil", "sein"), "Bold", 36),
    ficon("tabler", "scale", 1500, 520, 260, "gesamt", fuell=GELB),
    pl("billigen", 1390, 560, beim("gesamt", "Billigen"), fill=GRUEN, size=28, anker="m"),
    pl("vertrauen", 1610, 560, beim("gesamt", "Vertrauen"), fill=BLAU, size=28, anker="m"),
    *fig("VO", 1800, BR, 430, [("gesamt", "denkt")]),
    name("VO", 1800, "gesamt", unten=BR),
    pl("Gefahr", 1500, 670, beim("indiz", "Gefährlichkeit"), fill=WEISS, size=26, anker="m"),
    pl("Motiv", 1500, 730, beim("indiz", "Motiv"), fill=WEISS, size=26, anker="m"),
])

# K Gegenstück: Tatumstandsirrtum, § 16 I -------------------------------------------------------------------------------
P16 = ["„Wer bei Begehung der Tat einen Umstand nicht kennt, der zum",
       "gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. Die",
       "Strafbarkeit wegen fahrlässiger Begehung bleibt unberührt.“"]
wl16, y16 = wortlaut(100, 270, 1060, P16, "§ 16 Abs. 1 StGB", "p16",
                     marken=[(0, "nicht kennt", beim("p16", "kennt")), (1, "handelt nicht vorsätzlich", beim("p16", "handelt")),
                             (2, "fahrlässiger Begehung", beim("p16b", "fahrlässige"))])
folie([("irrtum", f"{PA} › Gegenstück: Tatumstandsirrtum, § 16 Abs. 1 StGB")], [
    *tafel("irrtum", "Gegenstück: Tatumstandsirrtum"),
    z("Volker hält den Zaun für seinen eigenen", 110, 190, beim("irrtum", "Volker"), size=36),
    *wl16,
    nein(135, y16 + 53, "fremd", gr=22), z("Volker kennt nicht: die Sache ist fremd", 175, y16 + 30, "fremd", "Bold", 36),
    z("strafbar bliebe nur fahrlässige Begehung", 110, y16 + 110, "p16b", size=36),
    fl_block(110, y16 + 175, 1040, 90, GELB, beim("p16b", "und"), [("fahrlässige Sachbeschädigung: gibt es nicht", "ExtraBold", 36, INK)]),
    ficon("tabler", "map", 1400, 420, 150, beim("irrtum", "Grenzplan"), fuell=WEISS),
    pl("alter Grenzplan", 1400, 450, beim("irrtum", "Grenzplan"), fill=GELB, size=28, anker="m"),
    zaun(1400, 760, 180, "irrtum"),
    pl("fremd", 1400, 790, "fremd", fill=ROT, size=28, anker="m"),
    *fig("VO", 1760, BR, 430, [("irrtum", "denkt"), ("fremd", "ertappt")]),
    name("VO", 1760, "irrtum", unten=BR),
])

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Vorsatzform nur, wenn es darauf ankommt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Vorsatzform nur bestimmen, wenn es", 200, 200, beim("tipp", "Bestimme"), "Bold", 36),
    z("darauf ankommt", 200, 250, beim("tipp", "darauf"), "Bold", 36),
    z("meist genügt Eventualvorsatz", 240, 305, beim("tipp", "Meist"), size=34),
    z("Gesetz verlangt Absicht oder Wissentlichkeit?", 200, 390, "tipp2", "Bold", 36),
    z("z. B. § 226 Abs. 2 StGB: „absichtlich oder wissentlich“", 240, 445, beim("tipp2", "Paragraf"), size=33),
    z("dann reicht Eventualvorsatz nicht", 240, 497, beim("tipp2", "reicht"), size=34),
    z("BGH, 2 StR 150/15, Rn. 18", 240, 547, beim("tipp2", "reicht"), "Bold", 27, farbe=TEXT),
    z("Tötungsdelikte: „Hemmschwelle“ ist keine Begründung", 200, 625, "tipp3", "Bold", 34),
    z("BGH: nur Hinweis auf sorgfältige Gesamtwürdigung", 240, 680, beim("tipp3", "Für"), size=33),
    z("BGH, 4 StR 558/11, Rn. 42, 45 (BGHSt 57, 183)", 240, 730, beim("tipp3", "Für"), "Bold", 27, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema ------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 260
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Vorsatz im Tatbestand", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 190, "k1", "ExtraBold", 40, rechts=1820),
    z("1. Objektiver Tatbestand", K2, 255, beim("k1", "Erstens"), "Bold", 38, rechts=1820),
    z("2. Subjektiver Tatbestand: Vorsatz bei Begehung der Tat,", K2, 320, "k2", "Bold", 38, rechts=1820),
    z("bezogen auf alle objektiven Merkmale", K2 + 40, 375, beim("k2", "bezogen"), size=36, rechts=1820),
    z("a) Wissen und Wollen", K3, 440, "k2a", size=36, farbe=TEXT, rechts=1820),
    z("b) wo nötig Vorsatzform: Absicht, direkter Vorsatz, Eventualvorsatz", K3, 495, "k2b", size=36, farbe=TEXT, rechts=1820),
    z("c) Abgrenzung zur bewussten Fahrlässigkeit", K3, 550, "k2c", size=36, farbe=TEXT, rechts=1820),
    z("d) Tatumstandsirrtum, § 16 Abs. 1 StGB", K3, 605, "k2d", size=36, farbe=TEXT, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 690, "k3", "ExtraBold", 40, rechts=1820),
    z("III. Schuld", K1, 755, beim("k3", "Schuld"), "ExtraBold", 40, rechts=1820),
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Absicht", "a"), (": Es kommt dem Täter darauf an.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "Absicht")}),
    *markertext([[("Direkter Vorsatz", "b"), (": Er weiß es sicher.", 0)]], 750, 410, 44, "m2", {"b": beim("m2", "Direkter")}),
    *markertext([[("Eventualvorsatz", "c"), (": für möglich halten", 0)], [("und sich damit abfinden.", 0)]], 750, 530, 44, "m3",
                {"c": beim("m3", "Eventualvorsatz")}),
    *markertext([[("Wer ernsthaft vertraut: höchstens ", 0), ("fahrlässig.", "d")]], 750, 730, 44, "m4", {"d": beim("m4", "fahrlässig")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        assert "→" not in t_
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
