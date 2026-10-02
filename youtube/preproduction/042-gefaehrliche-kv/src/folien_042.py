"""Folge 042 · Gefährliche Körperverletzung Schema: § 224 StGB mit allen 5 Varianten – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Dorffest (Festzelt, Biertisch, Sonne), B Sachverhalt, C Wortlautkarte § 224 I, II,
D Aufbau, E1 Grundfall: § 223 und Nr. 2 (gefährliches Werkzeug), E2 Nr. 2: der Schuh am Fuß, F Nr. 1 (Variante 1),
G Nr. 3 (Variante 2), H Nr. 4 (Variante 3), I Nr. 5 (Variante 4), J Vorsatz, K Versuch (Variante 5), L Ergebnis,
M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Gewalt zurückhaltend: kein Blut, keine Verletzungsbilder, kein Würgen oder Schlagen im Bild; Tritt, Schlag und Würgen nur
als Pille bzw. neutrales Symbol (Stiefel, Glas, Hand). Keine Geräusche (Freesound gesperrt, in sfx3 nichts Passendes)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_042/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
DUNKEL = (74, 74, 94, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def zitat(text, x, y, cue, **k):
    """BGH-Fundstelle unter einer Definition (klein, grau)."""
    return z(text, x, y, cue, "Bold", 26, farbe=TEXT, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (zweizeilige Blöcke bleiben im Kasten)."""
    for t_, *_ in zeilen:
        glyphen(t_)
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def gekippt(e, winkel):
    """Requisit (Icon) um 'winkel' Grad gedreht, unten auf derselben Linie (nicht umgezeichnet)."""
    unten = e.y + e.sprite.height
    cx = e.x + e.sprite.width / 2
    e.sprite = e.sprite.rotate(winkel, expand=True, resample=Image.BICUBIC)
    e.sprite = e.sprite.crop(e.sprite.getbbox())
    e.x, e.y = int(cx - e.sprite.width / 2), int(unten - e.sprite.height)
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


def sachverhalt_klein(cue, absaetze, frage, size=33, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber mit kleinerer Schrift (längerer Sachverhalt mit fünf Varianten)."""
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 200
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.3)
        els += e; y += 16
    els.append(pl(frage, 210, min(y + 8, 870), cue, fill=PINK, size=36))
    assert y + 8 <= 870, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


# --- Eigene Hilfsfunktion (wie Folge 029/035/038): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------
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


# --- Figuren und Namensschilder ----------------------------------------------------------------------------------------
NAMEN = {"RE": ("Reinhard", GRUEN), "TO": ("Tobias", BLAU), "TOS": ("Tobias", BLAU), "AN": ("Anja", LILA)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
SITZ = 0.68                                 # Tobias am Boden (hands_back-1) im Verhältnis zur Standhöhe


def name(p, cx, cue, unten=BR, size=28, d=0.2, bis=None, anim="pop"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def stiefel(cx, unten, breite, cue, bis=None, anim="pop"):
    return ficon("ph", "boot-thin", cx, unten, breite, cue, fuell=DUNKEL, bis=bis, anim=anim)


# A Fall: Dorffest -------------------------------------------------------------------------------------------------------
BA = 900                                    # Boden auf der Festwiese
SH = 560                                    # Standhöhe im Fall
TOX, TOX1, TISCHX, REX0, REX1 = 840, 720, 1270, 1640, 990
TISCH = ficon("tabler", "picnic-table", TISCHX, BA, 300, NULL, fuell=WEISS, anim="cut")
TOPF = TISCH.y + 4                          # Tischplatte (oberer Rand des Icons)
GLAS_STEHT = ficon("ph", "beer-stein-thin", TISCHX + 40, TOPF + 6, 70, NULL, fuell=GELB, anim="cut",
                   bis=beim("glas", "um"))
GLAS_KIPPT = gekippt(ficon("ph", "beer-stein-thin", TISCHX + 40, TOPF + 8, 70, beim("glas", "um"), fuell=GELB, anim="cut"), -60)
TOb = ("TOS_redet_r", TOX1, BA, int(SH * SITZ))
REb = ("RE_redet", REX0, BA, SH)
folie([(NULL, "Fall · Das Dorffest"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(80, BA + 2), (1840, BA + 2)], NULL, breite=6, farbe=INK)),
    hart(ficon("tabler", "tent", 370, BA, 340, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "sun", 1790, 210, 110, NULL, fuell=GELB, anim="cut")),
    TISCH, GLAS_STEHT, GLAS_KIPPT,
    pl("Samstagnachmittag", 100, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Dorffest", 100, 140, beim("fall", "Dorffest"), fill=WEISS, size=30),
    # Tobias: tanzt, dann am Boden
    *fig("TO", TOX, BA, SH, [(NULL, "froh_r")], bis="stoss", erst="cut"),
    ficon("tabler", "music", TOX - 150, 420, 80, beim("tobias", "tanzt"), fuell=None, bis="stoss"),
    pl("tanzt", TOX - 150, 450, beim("tobias", "tanzt"), fill=WEISS, size=28, anker="m", bis="stoss"),
    pl("aus Versehen", TISCHX + 40, TOPF - 120, beim("glas", "Versehen"), fill=WEISS, size=28, anker="m", bis="stoss"),
    *fig("TOS", TOX1, BA, int(SH * SITZ), [("stoss", "erschrickt_r"), ("beule", "redet_r")], erst="cut", bis="t1"),
    *redet("TOS_redet_r", TOX1, BA, int(SH * SITZ), "t1", "frage"),
    *fig("TOS", TOX1, BA, int(SH * SITZ), [("frage", "ruhig_r")], erst="cut"),
    name("TO", TOX, NULL, unten=BA - 6, d=0.0, anim="cut", bis="stoss"),       # Namensschild ab dem ersten Bild
    name("TOS", TOX1, "stoss", unten=BA - 6, d=0.0, anim="cut"),
    # Reinhard: am Tisch, dann bei Tobias
    *fig("RE", REX0, BA, SH, [(beim("glas", "Reinhard"), "ruhig"), ("reinhard", "wuetend")], bis="r1"),
    *redet("RE_redet", REX0, BA, SH, "r1", "stoss"),
    name("RE", REX0, beim("glas", "Reinhard"), unten=BA - 6, bis="stoss"),
    pl("außer sich", REX0, 280, beim("reinhard", "außer"), fill=PINK, size=30, anker="m", bis="r1"),
    blase("sprech", 520, 170, "r1", 1500, 260, inhalt=["Das wirst du", "bereuen!"], textsize=38, figur=REb, bis="stoss"),
    *fig("RE", REX1, BA, SH, [("stoss", "wuetend"), ("tritt", "entschlossen"), ("t1", "veraechtlich"), ("frage", "denkt")],
         erst="cut"),
    name("RE", REX1, "stoss", unten=BA - 6, d=0.0, anim="cut"),
    pl("zu Boden gestoßen", TOX1, 300, beim("stoss", "Boden"), fill=WEISS, size=28, anker="m", bis="tritt"),
    stiefel(TOX1 + 165, 610, 90, beim("tritt", "Arbeitsstiefel"), bis="t1"),
    pl("schwerer Arbeitsstiefel", TOX1, 330, beim("tritt", "Arbeitsstiefel"), fill=WEISS, size=28, anker="m", bis="beule"),
    pl("Tritt gegen den Kopf", TOX1 - 50, 410, beim("tritt", "Kopf"), fill=PINK, size=30, anker="m", bis="t1"),
    pl("dicke Beule", TOX1 - 50, 330, "beule", fill=GELB, size=30, anker="m", bis="t1"),
    blase("sprech", 600, 190, "t1", 560, 330, inhalt=["Mit dem Stiefel? Das", "ist doch gefährlich!"], textsize=34,
          figur=TOb, bis="frage"),
    # Frage
    pl("Gefährlich im Sinne des Gesetzes?", 1520, 330, "frage", fill=PINK, size=34, anker="m"),
    pl("Wann wird die Körperverletzung gefährlich?", 1520, 420, beim("frage2", "Wann"), fill=WEISS, size=30, anker="m"),
    pl("Wie prüfst du das?", 1520, 500, beim("frage2", "prüfst"), fill=WEISS, size=30, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Samstagnachmittag auf dem Dorffest: Tobias tanzt vor dem Festzelt und stößt dabei aus Versehen das Bierglas von "
    "Reinhard (Mitte 50) um. Reinhard stößt Tobias zu Boden und tritt ihm mit seinem schweren Arbeitsstiefel gegen den "
    "Kopf. Tobias bekommt eine dicke Beule.",
    "Variante 1: Reinhard mischt Tobias heimlich eine hohe Dosis eines starken Schlafmittels ins Glas; Tobias bricht "
    "zusammen und muss im Krankenhaus behandelt werden. Variante 2: Reinhard geht lächelnd auf Tobias zu, reicht ihm die "
    "Hand („Komm, vertragen wir uns wieder.“) und schlägt dann unvermittelt zu. Gegenstück: Reinhard greift Tobias nur "
    "überraschend von hinten an. Variante 3: Reinhards Tochter Anja stellt sich Tobias in den Weg, damit er nicht "
    "ausweichen kann, während Reinhard zuschlägt; selbst schlägt sie nicht. Variante 4: Reinhard drückt Tobias kräftig "
    "und lange den Hals zu; in Lebensgefahr gerät Tobias nicht. Variante 5: Reinhard holt mit dem Stiefel zum Tritt gegen "
    "Tobias’ Kopf aus, doch Tobias rollt sich weg.",
], "Wie hat sich Reinhard strafbar gemacht?")

# Gemeinsame Bühne rechts: Reinhard und Tobias -------------------------------------------------------------------------
KR = int(FR * SITZ)


def buehne(cue, re_folge, to_folge, sitzt=False, rex=1430, tox=1745):
    """Reinhard und Tobias rechts neben der Tafel; Grundansicht blickt zur Tafel nach links. sitzt = Tobias am Boden."""
    p, h = ("TOS", KR) if sitzt else ("TO", FR)
    return [*fig("RE", rex, BR, FR, re_folge, erst="cut"), name("RE", rex, cue, d=0.0, anim="cut"),
            *fig(p, tox, BR, h, to_folge, erst="cut"), name(p, tox, cue, d=0.0, anim="cut")]


# C Wortlaut § 224 -------------------------------------------------------------------------------------------------------
P224 = ["„(1) Wer die Körperverletzung",
        "1. durch Beibringung von Gift oder anderen gesundheitsschädlichen Stoffen,",
        "2. mittels einer Waffe oder eines anderen gefährlichen Werkzeugs,",
        "3. mittels eines hinterlistigen Überfalls,",
        "4. mit einem anderen Beteiligten gemeinschaftlich oder",
        "5. mittels einer das Leben gefährdenden Behandlung",
        "begeht, wird mit Freiheitsstrafe von sechs Monaten bis zu zehn Jahren,",
        "in minder schweren Fällen mit Freiheitsstrafe von drei Monaten bis zu",
        "fünf Jahren bestraft.",
        "(2) Der Versuch ist strafbar.“"]
wl224, y224 = wortlaut(90, 170, 1090, P224, "§ 224 StGB", "p224", size=28,
                       marken=[(0, "Körperverletzung", beim("p224w", "Körperverletzung")),
                               (1, "Gift oder anderen gesundheitsschädlichen Stoffen", "n1"),
                               (2, "Waffe oder eines anderen gefährlichen Werkzeugs", "n2"),
                               (3, "hinterlistigen Überfalls", "n3"),
                               (4, "mit einem anderen Beteiligten gemeinschaftlich", "n4"),
                               (5, "das Leben gefährdenden Behandlung", "n5"),
                               (6, "sechs Monaten bis zu zehn Jahren", beim("straf", "sechs")),
                               (9, "Der Versuch ist strafbar.", beim("abs2", "Versuch"))])
NRX = [1320, 1445, 1570, 1695, 1820]
NRI = [("tabler", "pill", PINK), ("ph", "boot-thin", DUNKEL), ("ph", "handshake-thin", GELB), ("tabler", "users", BLAU),
       ("tabler", "heartbeat", ROT)]
folie([("p224", "§ 224 StGB › Wortlaut: fünf Begehungsweisen")], [
    *tafel("p224", "Gefährliche Körperverletzung, § 224 StGB"),
    *wl224,
    pl("fünf Begehungsweisen", 110, y224 + 30, beim("p224w", "fünf"), fill=GELB, size=32),
    *[ficon(s_, n_, x_, 360, 90, f"n{i + 1}", fuell=c_) for i, ((s_, n_, c_), x_) in enumerate(zip(NRI, NRX))],
    *buehne("p224", [("p224", "ruhig"), ("n2", "denkt")], [("p224", "ruhig"), ("n5", "denkt")]),
])

# D Aufbau ---------------------------------------------------------------------------------------------------------------
folie([("aufbau", "§ 224 StGB › Aufbau: Grundtatbestand und Qualifikation")], [
    *tafel("aufbau", "Aufbau der Prüfung"),
    pl("§ 224 = Qualifikation", 110, 200, beim("aufbau", "Qualifikation"), fill=GELB, size=36),
    blk(110, 320, 1040, 90, BLAU, "grund", [("1. Grundtatbestand: § 223 StGB", "ExtraBold", 38, INK)]),
    blk(110, 470, 1040, 90, GELB, "dann", [("2. mindestens eine Nummer des § 224 Abs. 1", "ExtraBold", 36, INK)]),
    ficon("tabler", "arrow-down", 630, 462, 50, "dann", fuell=None),
    *buehne("aufbau", [("aufbau", "denkt"), ("dann", "ruhig")], [("aufbau", "ruhig"), ("grund", "denkt")]),
])

# E1 Grundfall: § 223 und Nr. 2 ----------------------------------------------------------------------------------------
PG = "Grundfall › I. 1. objektiv"
folie([("gf", f"{PG} › a) Körperverletzung, § 223 StGB"),
       ("nr2", f"{PG} › b) Qualifikation: Nr. 2 gefährliches Werkzeug")], [
    *tafel("gf", "Grundfall: Tritt mit dem Arbeitsstiefel"),
    z("Tritt gegen den Kopf: körperliche Misshandlung", 110, 185, "gf223", size=34),
    z("Beule: Gesundheitsschädigung", 110, 237, beim("gf223", "Beule"), size=34),
    ok(135, 313, "gf_ok", gr=22), z("§ 223 StGB", 175, 290, "gf_ok", "Bold", 36),
    blk(110, 370, 1040, 70, GELB, "nr2", [("Nr. 2: gefährliches Werkzeug", "ExtraBold", 34, INK)]),
    z("jeder bewegliche Gegenstand, der nach seiner", 110, 470, "wdef", "Bold", 34),
    z("objektiven Beschaffenheit", 150, 522, beim("wdef", "objektiven"), size=34),
    z("und der Art seiner Benutzung im konkreten Einzelfall", 150, 574, "wart", size=34),
    z("geeignet ist, erhebliche Körperverletzungen herbeizuführen", 150, 626, "werh", "Bold", 32),
    zitat("BGH, Beschl. v. 28.6.2018 – 1 StR 171/18, Rn. 6", 110, 686, beim("werh", "herbeizuführen")),
    *buehne("gf", [("gf", "ruhig"), ("nr2", "denkt")], [("gf", "redet"), ("gf_ok", "ruhig")], sitzt=True),
    stiefel(1590, 820, 80, "gf"),
    pl("Beule", 1745, 560, beim("gf223", "Beule"), fill=GELB, size=26, anker="m"),
    pl("beweglicher Gegenstand", 1600, 200, beim("wdef", "bewegliche"), fill=WEISS, size=26, anker="m"),
])

# E2 Nr. 2: der Schuh am Fuß ---------------------------------------------------------------------------------------------
folie([("schuh", f"{PG} › b) Nr. 2: der Schuh am Fuß")], [
    *tafel("schuh", "Und der Schuh am Fuß?"),
    z("Es kommt auf den Einzelfall an:", 110, 185, "schuh2", "Bold", 36),
    z("· Beschaffenheit des Schuhs", 150, 240, beim("schuh2", "Beschaffenheit"), size=34),
    z("· Heftigkeit des Tritts", 150, 292, "heftig", size=34),
    z("· getroffener Körperteil", 150, 344, "teil", size=34),
    blk(110, 410, 1040, 120, BLAU, "kopf", [("Straßenschuh üblicher Beschaffenheit, Tritt", "ExtraBold", 33, INK),
                                                 ("gegen den Kopf: regelmäßig gefährliches Werkzeug", "ExtraBold", 33, INK)]),
    zitat("BGH, Urt. v. 25.1.2023 – 6 StR 298/22, Rn. 4", 110, 548, beim("kopf", "Kopf")),
    z("Reinhard: sogar ein schwerer Arbeitsstiefel", 110, 610, "stiefel", size=34),
    ok(135, 688, "nr2_ok", gr=22), z("Nr. 2 erfüllt", 175, 665, "nr2_ok", "Bold", 38),
    pl("Lebensgefahr? gesondert bei Nr. 5", 110, 745, "nr5gf", fill=WEISS, size=30),
    *buehne("schuh", [("schuh", "ruhig"), ("stiefel", "veraechtlich"), ("nr2_ok", "ertappt")],
            [("schuh", "ruhig"), ("kopf", "redet")], sitzt=True),
    stiefel(1590, 820, 80, "schuh"),
    ficon("ph", "sneaker-thin", 1590, 330, 90, beim("schuh2", "Beschaffenheit"), fuell=WEISS, bis="stiefel"),
    pl("Schuh?", 1590, 200, beim("schuh2", "Beschaffenheit"), fill=WEISS, size=26, anker="m", bis="stiefel"),
    stiefel(1590, 330, 110, "stiefel"),
    pl("Arbeitsstiefel", 1590, 200, "stiefel", fill=GELB, size=26, anker="m"),
    pl("gegen den Kopf", 1745, 440, beim("kopf", "Kopf"), fill=PINK, size=26, anker="m"),
])

# F Nr. 1: Gift oder gesundheitsschädliche Stoffe ----------------------------------------------------------------------
folie([("nr1", "Variante 1 › Nr. 1: Gift oder gesundheitsschädliche Stoffe")], [
    *tafel("nr1", "Nr. 1: Gift, gesundheitsschädliche Stoffe"),
    z("Variante 1: hohe Dosis Schlafmittel im Glas", 110, 185, "nr1", "Bold", 36),
    z("Tobias bricht zusammen, Behandlung im Krankenhaus", 150, 240, "zus", size=33),
    blk(110, 310, 1040, 120, GELB, "stoff", [("Stoff nach Art und konkretem Einsatz zur", "ExtraBold", 33, INK),
                                                  ("erheblichen Gesundheitsschädigung geeignet", "ExtraBold", 33, INK)]),
    zitat("BGH, Urt. v. 16.3.2006 – 4 StR 536/05 (BGHSt 51, 18), Rn. 17", 110, 448, beim("stoff", "geeignet")),
    z("auch Stoffe des täglichen Bedarfs,", 110, 510, "alltag", size=34),
    z("etwa Kochsalz in großer Menge", 150, 562, beim("alltag", "Kochsalz"), size=34),
    ok(135, 643, "nr1_ok", gr=22), z("hohe Dosis Schlafmittel: Nr. 1", 175, 620, "nr1_ok", "Bold", 38),
    *fig("RE", 1430, BR, FR, [("nr1", "listig"), ("nr1_ok", "ertappt")], erst="cut"), name("RE", 1430, "nr1", d=0.0, anim="cut"),
    *fig("TO", 1745, BR, FR, [("nr1", "ruhig")], bis="zus", erst="cut"), name("TO", 1745, "nr1", d=0.0, anim="cut", bis="zus"),
    *fig("TOS", 1745, BR, KR, [("zus", "schlaeft")], erst="cut"), name("TOS", 1745, "zus", d=0.0, anim="cut"),
    ficon("tabler", "glass-full", 1590, 820, 70, "nr1", fuell=GELB),
    ficon("tabler", "pills", 1500, 330, 90, beim("nr1", "Schlafmittels"), fuell=WEISS),
    pl("Schlafmittel", 1500, 200, beim("nr1", "Schlafmittels"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "ambulance", 1750, 330, 110, "zus", fuell=WEISS),
    pl("Krankenhaus", 1740, 200, beim("zus", "Krankenhaus"), fill=WEISS, size=26, anker="m"),
])

# G Nr. 3: hinterlistiger Überfall -------------------------------------------------------------------------------------
GRX, GTX = 1430, 1760
REg = ("RE_laechelt_r", GRX, BR, FR)
folie([("nr3", "Variante 2 › Nr. 3: hinterlistiger Überfall")], [
    *tafel("nr3", "Nr. 3: hinterlistiger Überfall"),
    z("Variante 2: lächelnd die Hand gereicht,", 110, 185, "nr3", "Bold", 36),
    z("dann unvermittelt zugeschlagen", 150, 240, "schlag", size=34),
    z("planmäßig in einer auf Verdeckung der wahren", 110, 310, "hdef", "Bold", 34),
    z("Absicht berechneten Weise,", 150, 362, beim("hdef", "Absicht"), "Bold", 34),
    z("um dem Opfer die Abwehr zu erschweren", 150, 414, "hzweck", size=34),
    zitat("BGH, Beschl. v. 15.12.2020 – 3 StR 386/20, Rn. 4", 110, 472, beim("hzweck", "erschweren")),
    z("typisch: vorgetäuschte Friedfertigkeit", 110, 530, "fried", size=34),
    ok(135, 611, "nr3_ok", gr=22), z("Reinhard: Nr. 3", 175, 588, "nr3_ok", "Bold", 38),
    z("Gegenstück: nur überraschend von hinten", 110, 670, "hinten", "Bold", 34),
    nein(135, 748, "hinten_no", gr=20), z("bloßes Überraschungsmoment genügt nicht", 175, 725, "hinten_no", size=34),
    zitat("BGH, Beschl. v. 2.5.2012 – 3 StR 146/12, Rn. 3", 175, 780, beim("hinten_no", "Überraschungsmoments")),
    *fig("RE", GRX, BR, FR, [("nr3", "laechelt_r")], bis="r2", erst="cut"),
    *redet("RE_laechelt_r", GRX, BR, FR, "r2", "schlag"),
    *fig("RE", GRX, BR, FR, [("schlag", "entschlossen_r"), ("hdef", "listig_r"), ("hinten", "ruhig")], erst="cut"),
    name("RE", GRX, "nr3", d=0.0, anim="cut"),
    *fig("TO", GTX, BR, FR, [("nr3", "froh"), ("schlag", "erschrickt"), ("hdef", "aua"), ("hinten", "ruhig")], erst="cut"),
    name("TO", GTX, "nr3", d=0.0, anim="cut"),
    ficon("ph", "handshake-thin", 1595, 640, 100, beim("nr3", "Hand"), fuell=GELB, bis="schlag"),
    blase("sprech", 560, 180, "r2", 1560, 260, inhalt=["Komm, vertragen", "wir uns wieder."], textsize=36, figur=REg,
          bis="schlag"),
    pl("schlägt unvermittelt zu", 1595, 330, "schlag", fill=PINK, size=26, anker="m", bis="hinten"),
    pl("vorgetäuschte Friedfertigkeit", 1595, 400, "fried", fill=GELB, size=26, anker="m", bis="hinten"),
    pl("nur von hinten?", 1595, 330, "hinten", fill=WEISS, size=26, anker="m"),
])

# H Nr. 4: gemeinschaftlich ---------------------------------------------------------------------------------------------
HRX, HTX, HAX = 1370, 1600, 1810
ANb = ("AN_redet", HAX, BR, FR)
folie([("nr4", "Variante 3 › Nr. 4: mit einem anderen Beteiligten gemeinschaftlich")], [
    *tafel("nr4", "Nr. 4: gemeinschaftlich"),
    z("Variante 3: Anja versperrt Tobias den Weg", 110, 185, "nr4", "Bold", 36),
    z("Reinhard schlägt zu, Tobias kann nicht ausweichen", 150, 240, "zuschl", size=33),
    z("Anja schlägt selbst nicht", 150, 292, "selbst", size=33),
    blk(110, 355, 1040, 70, GELB, "geh", [("auch ein Gehilfe ist „anderer Beteiligter“", "ExtraBold", 33, INK)]),
    z("jedenfalls, wenn der anwesende Gehilfe den Angriff", 110, 450, "vstk", size=33),
    z("bewusst verstärkt und die Lage des Opfers verschlechtert", 110, 500, beim("vstk", "verstärkt"), size=33),
    z("etwa: schlechter ausweichen oder fliehen", 150, 555, "flucht", "Bold", 34),
    zitat("BGH, Urt. v. 3.9.2002 – 5 StR 210/02 (BGHSt 47, 383), Rn. 10 f.", 110, 612, beim("flucht", "fliehen")),
    ok(135, 693, "nr4_ok", gr=22), z("Reinhard und Anja: Nr. 4", 175, 670, "nr4_ok", "Bold", 38),
    *fig("RE", HRX, BR, FR, [("nr4", "ruhig_r"), ("zuschl", "entschlossen_r"), ("geh", "ruhig")], erst="cut"),
    name("RE", HRX, "nr4", d=0.0, anim="cut"),
    *fig("TO", HTX, BR, FR, [("nr4", "skeptisch"), ("zuschl", "erschrickt"), ("geh", "aua")], erst="cut"),
    name("TO", HTX, "nr4", d=0.0, anim="cut"),
    *fig("AN", HAX, BR, FR, [("nr4", "streng")], bis="a1"),
    *redet("AN_redet", HAX, BR, FR, "a1", "zuschl"),
    *fig("AN", HAX, BR, FR, [("zuschl", "streng"), ("geh", "denkt")], erst="cut"),
    name("AN", HAX, beim("nr4", "Anja")),
    blase("sprech", 520, 180, "a1", 1640, 250, inhalt=["Hier kommst du", "nicht vorbei!"], textsize=36, figur=ANb, bis="zuschl"),
    pl("versperrt den Weg", 1700, 400, beim("nr4", "Weg"), fill=WEISS, size=26, anker="m", bis="a1"),
    pl("kein Ausweg", 1600, 360, "zuschl", fill=PINK, size=26, anker="m"),
    pl("Gehilfin", 1810, 420, "geh", fill=LILA, size=26, anker="m"),
])

# I Nr. 5: das Leben gefährdende Behandlung ----------------------------------------------------------------------------
folie([("nr5", "Variante 4 › Nr. 5: das Leben gefährdende Behandlung")], [
    *tafel("nr5", "Nr. 5: lebensgefährdende Behandlung"),
    z("Variante 4: Hals kräftig und lange zugedrückt", 110, 185, "nr5", "Bold", 36),
    z("keine tatsächliche Lebensgefahr", 150, 240, "keine", size=34),
    z("muss auch nicht eintreten", 150, 292, "ldef", size=34),
    blk(110, 355, 1040, 120, GELB, "abstr", [("genügt: Behandlung abstrakt geeignet,", "ExtraBold", 34, INK),
                                                  ("das Leben zu gefährden", "ExtraBold", 34, INK)]),
    zitat("BGH, Urt. v. 8.12.2016 – 1 StR 344/16, Rn. 12", 110, 492, beim("abstr", "gefährden")),
    z("Würgen: Dauer und Stärke entscheiden", 110, 550, "dauer", "Bold", 34),
    nein(135, 628, "griff", gr=20), z("nicht jeder Griff an den Hals", 175, 605, "griff", size=34),
    zitat("BGH, Beschl. v. 18.1.2022 – 2 StR 206/21, Rn. 4", 175, 660, beim("griff", "Hals")),
    ok(135, 738, "nr5_ok", gr=22), z("kräftig und lange: Nr. 5", 175, 715, "nr5_ok", "Bold", 38),
    *buehne("nr5", [("nr5", "wuetend"), ("ldef", "denkt"), ("nr5_ok", "ertappt")],
            [("nr5", "aua"), ("keine", "ruhig"), ("dauer", "denkt")]),
    ficon("tabler", "heartbeat", 1590, 330, 100, "nr5", fuell=None),
    pl("drückt den Hals zu", 1590, 200, "nr5", fill=PINK, size=26, anker="m", bis="keine"),
    pl("keine Lebensgefahr", 1590, 200, "keine", fill=WEISS, size=26, anker="m", bis="abstr"),
    pl("abstrakt geeignet", 1590, 200, "abstr", fill=GELB, size=26, anker="m"),
])

# J Vorsatz -------------------------------------------------------------------------------------------------------------
folie([("vz", "Grundfall › I. 2. subjektiv: Vorsatz")], [
    *tafel("vz", "Subjektiver Tatbestand: Vorsatz"),
    ok(135, 208, "vz1", gr=22), z("bezüglich der Körperverletzung", 175, 185, "vz1", "Bold", 36),
    ok(135, 268, "vz2", gr=22), z("und der Qualifikation", 175, 245, "vz2", "Bold", 36),
    blk(110, 320, 1040, 120, GELB, "umst", [("genügt: Kenntnis der Umstände, aus denen", "ExtraBold", 33, INK),
                                                 ("sich die Gefährlichkeit ergibt", "ExtraBold", 33, INK)]),
    zitat("BGH, 3 StR 386/20, Rn. 12; BGH, 4 StR 551/12, Rn. 24 (Nr. 5)", 110, 458, beim("umst", "ergibt")),
    z("Grundfall: schwerer Stiefel, Tritt gegen den Kopf", 110, 520, "stief", size=34),
    nein(135, 598, "bezw", gr=20), z("Gefährlichkeit bezwecken: nicht nötig", 175, 575, "bezw", size=34),
    *buehne("vz", [("vz", "denkt"), ("stief", "entschlossen")], [("vz", "ruhig"), ("stief", "redet")], sitzt=True),
    stiefel(1590, 820, 80, "vz"),
    blase("denk", 360, 200, "stief", 1560, 260, inhalt=["Stiefel,", "Kopf"], textsize=36, figur=("RE_entschlossen", 1430, BR, FR)),
])

# K Versuch -------------------------------------------------------------------------------------------------------------
folie([("vers", "Variante 5 › Versuch, §§ 224 Abs. 2, 22 StGB")], [
    *tafel("vers", "Versuch, § 224 Abs. 2 StGB"),
    z("Variante 5: Tritt gegen den Kopf ausgeholt,", 110, 185, "vers", "Bold", 36),
    z("Tobias rollt sich weg", 150, 240, "weg", size=34),
    ok(135, 333, "tatent", gr=22), z("Tatentschluss: Tritt mit dem Stiefel gegen den Kopf", 175, 310, "tatent", "Bold", 33),
    ok(135, 398, "ansetz", gr=22), z("nach seiner Vorstellung unmittelbar angesetzt", 175, 375, "ansetz", "Bold", 34),
    zitat("§ 22 StGB", 175, 428, beim("ansetz", "unmittelbar")),
    blk(110, 500, 1040, 80, GELB, "vers_ok", [("versuchte gefährliche KV strafbar, § 224 Abs. 2", "ExtraBold", 34, INK)]),
    ok(1110, 540, beim("vers_ok", "strafbar"), gr=22),
    *fig("RE", 1430, BR, FR, [("vers", "entschlossen_r"), ("weg", "ertappt_r"), ("vers_ok", "denkt")], erst="cut"),
    name("RE", 1430, "vers", d=0.0, anim="cut"),
    *fig("TOS", 1660, BR, KR, [("vers", "erschrickt")], bis="weg", erst="cut"),
    name("TOS", 1660, "vers", d=0.0, anim="cut", bis="weg"),
    *fig("TOS", 1790, BR, KR, [("weg", "staunt")], erst="cut"),
    name("TOS", 1790, "weg", d=0.0, anim="cut"),
    stiefel(1560, 700, 80, beim("vers", "Stiefel")),
    pl("ausgeholt", 1560, 330, beim("vers", "aus"), fill=PINK, size=26, anker="m", bis="weg"),
    pl("weggerollt", 1760, 330, "weg", fill=WEISS, size=26, anker="m"),
])

# L Ergebnis -----------------------------------------------------------------------------------------------------------
folie([("erg", "Grundfall › II. Rechtswidrigkeit, III. Schuld"), ("erg2", "Grundfall › Ergebnis: §§ 223, 224 Abs. 1 Nr. 2 StGB"),
       ("antrag", "Grundfall › kein Strafantrag nötig, § 230 StGB")], [
    *tafel("erg", "Zurück zum Grundfall"),
    z("Rechtfertigung, Entschuldigung: fehlen", 110, 185, "rw", size=36),
    blk(110, 255, 1040, 120, GELB, "erg2", [("Reinhard: strafbar wegen gefährlicher", "ExtraBold", 36, INK),
                                                 ("Körperverletzung, §§ 223, 224 Abs. 1 Nr. 2", "ExtraBold", 36, INK)]),
    ok(1110, 315, beim("erg2", "strafbar"), gr=22),
    z("Strafantrag: nicht nötig", 110, 425, "antrag", "Bold", 38),
    z("§ 230 nennt nur die einfache (§ 223)", 150, 485, beim("antrag", "Paragraf"), size=34),
    z("und die fahrlässige Körperverletzung (§ 229)", 150, 537, beim("antrag", "fahrlässige"), size=34),
    *buehne("erg", [("erg", "ruhig"), ("erg2", "ertappt")], [("erg", "ruhig"), ("antrag", "staunt")], sitzt=True),
    ficon("tabler", "scale", 1530, 330, 100, "erg2", fuell=GELB),
    pl("strafbar", 1530, 200, beim("erg2", "strafbar"), fill=GELB, size=26, anker="m"),
    ficon("tabler", "signature", 1790, 330, 80, "antrag", fuell=WEISS),
    pl("kein Antrag nötig", 1740, 200, "antrag", fill=WEISS, size=26, anker="m"),
])

# M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · §§ 223, 224 zusammen prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§§ 223, 224 zusammen prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("erst Grundtatbestand, dann die Nummern", 200, 252, beim("tipp", "erst"), "Bold", 36),
    blk(110, 340, 1040, 64, BLAU, "tipp2", [("jede naheliegende Nummer ansprechen", "ExtraBold", 34, INK)]),
    z("oft sind es mehrere", 150, 430, beim("tipp2", "oft"), size=34),
    z("Schuh konkret begründen:", 150, 510, "tipp3", "Bold", 34),
    z("welcher Schuh, wie heftig, welcher Körperteil", 150, 562, beim("tipp3", "welcher"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.0),
    stiefel(1800, 470, 80, "tipp3"),
])

# N Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2, K3, K4 = 130, 190, 250, 310
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Gefährliche Körperverletzung, §§ 223, 224 StGB", 110, 90, "sch", 46),
    z("I. Tatbestand", K1, 180, "k_i", "ExtraBold", 40, rechts=1820),
    z("1. objektiv", K2, 238, "k1", "Bold", 36, rechts=1820),
    z("a) Körperverletzung, § 223", K3, 290, "k1a", size=35, rechts=1820),
    z("b) Qualifikation, § 224 Abs. 1:", K3, 342, "k1b", size=35, rechts=1820),
    z("Nr. 1 Gift oder gesundheitsschädliche Stoffe", K4, 394, "kq1", size=33, rechts=1820),
    z("Nr. 2 gefährliches Werkzeug", K4, 440, "kq2", size=33, rechts=1820),
    z("Nr. 3 hinterlistiger Überfall", K4, 486, "kq3", size=33, rechts=1820),
    z("Nr. 4 gemeinschaftliche Begehung", K4, 532, "kq4", size=33, rechts=1820),
    z("Nr. 5 lebensgefährdende Behandlung", K4, 578, "kq5", size=33, rechts=1820),
    z("2. subjektiv: Vorsatz, auch bezüglich der Qualifikation", K2, 638, "k2", "Bold", 36, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 712, "k_ii", "ExtraBold", 40, rechts=1820),
    z("III. Schuld", K1, 776, "k_iii", "ExtraBold", 40, rechts=1820),
    pl("Vollendung gescheitert: Versuch, § 224 Abs. 2", K1, 852, "k_v", fill=GELB, size=32),
])

# O Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("§ 224", "a"), (" baut auf der", 0)], [("Körperverletzung auf.", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "Paragraf")}),
    *markertext([[("Jede Nummer", "b"), (" beschreibt eine Begehungsweise,", 0)], [("die die Tat abstrakt gefährlicher macht.", 0)]],
                750, 470, 42, "m2", {"b": beim("m2", "Nummern")}),
    *markertext([[("Der ", 0), ("Vorsatz", "c"), (" muss die gefährlichen", 0)], [("Umstände umfassen.", 0)]], 750, 640, 44, "m3",
                {"c": beim("m3", "Vorsatz")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.0),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
