"""Folge 038 · Körperverletzung § 223 StGB: Misshandlung & Gesundheitsschädigung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Wohngemeinschaft am Sonntagabend (Sofa, Fenster mit Mond, Lampe), B Sachverhalt,
C Wortlautkarte § 223 I, II, D körperliche Misshandlung (Grundfall Haare), E Bagatellgrenze (Ohrfeige/Stups),
F Gesundheitsschädigung (Abführmittel), G psychische Folgen, H ärztlicher Heileingriff (Hautarztpraxis),
I Versuch, J Ergebnis und Strafantrag, K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Gewalt zurückhaltend: kein Blut, keine Verletzungsbilder; Ohrfeige und Stups nur als Hand-Icon mit Pille.
Keine Geräusche (Freesound gesperrt, in sfx3 kein passendes Handlungsgeräusch)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_038/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
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


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
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


# --- Eigene Hilfsfunktion (wie Folge 029/035): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
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


# --- Figuren, Sitzmöbel, Namensschilder ------------------------------------------------------------------------------
NAMEN = {"KA": ("Katrin", BLAU), "KAL": ("Katrin", BLAU), "SI": ("Sigrid", LILA), "LI": ("Doktor Lindner", GRUEN)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
SITZ = 0.58                                 # Sitzende Figur (closed_legs-1) im Verhältnis zur Standhöhe


def name(p, cx, cue, unten=BR, size=28, d=0.2, bis=None, anim="pop"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def sofa(cx, unten, breite, cue, fuell=GRUEN, anim="cut"):
    """Sofa (Phosphor couch-thin); gibt (Element, Sitzhöhe) zurück. Die Sitzfläche liegt bei 57 % der Icon-Höhe."""
    e = ficon("ph", "couch-thin", cx, unten, breite, cue, fuell=fuell, anim=anim)
    return e, e.y + e.sprite.height * 0.57


def liege(cx, unten, breite, cue):
    """Behandlungsliege (Tabler bed-flat, Liegefläche weiß); gibt (Element, Oberkante der Liegefläche) zurück."""
    e = ficon("tabler", "bed-flat", cx, unten, breite, cue, fuell=WEISS, anim="cut")
    return e, e.y + e.sprite.height * 0.12


# A Fall: Wohngemeinschaft am Sonntagabend -----------------------------------------------------------------------------
BA = 900                                    # Boden im Wohnzimmer
SH = 560                                    # Sigrid stehend
KH = int(SH * SITZ)                         # Katrin sitzend
SOFA, SITZ_A = sofa(720, BA, 540, NULL)
KAX = 650
SIX0, SIX1 = 1330, 1110                     # Sigrid erst am Fenster, dann neben dem Sofa
KAb = ("KA_redet_r", KAX, SITZ_A, KH)
SIb = ("SI_redet", SIX1, BA, SH)
folie([(NULL, "Fall · Die Haare"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(80, BA + 2), (1840, BA + 2)], NULL, breite=6, farbe=INK)),
    hart(karte(1520, 150, 300, 280, NULL, fill=BLAU, rund=14, schatten=0, rand=5, anim="cut")),           # Fenster
    hart(linienzug([(1670, 150), (1670, 430)], NULL, breite=5, farbe=INK)),
    hart(ficon("tabler", "moon", 1750, 260, 90, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "lamp", 260, BA, 170, NULL, fuell=GELB, anim="cut")),
    SOFA,
    pl("Sonntagabend", 100, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Wohngemeinschaft", 100, 140, beim("fall", "Wohngemeinschaft"), fill=WEISS, size=30),
    # Katrin auf dem Sofa
    *fig("KAL", KAX, SITZ_A, KH, [(NULL, "schlaeft_r")], bis=beim("schnitt", "ab"), erst="cut"),   # schläft schon ab 0,0 s
    *fig("KA", KAX, SITZ_A, KH, [(beim("schnitt", "ab"), "schlaeft_r"), (beim("wach", "wacht"), "erschrickt_r")], erst="cut",
         bis="k1"),
    *redet("KA_redet_r", KAX, SITZ_A, KH, "k1", "s1"),
    *fig("KA", KAX, SITZ_A, KH, [("s1", "skeptisch_r"), ("frage", "denkt_r")], erst="cut"),
    name("KA", KAX, NULL, unten=BA - 6, d=0.0, anim="cut"),   # Namensschild ab dem ersten Bild
    ficon("tabler", "zzz", KAX + 60, SITZ_A - KH - 10, 70, beim("katrin", "eingeschlafen"), fuell=None, bis=beim("wach", "wacht")),
    pl("eingeschlafen", 520, 300, beim("katrin", "eingeschlafen"), fill=WEISS, size=28, anker="m", bis="sigrid"),
    # Sigrid: erst am Fenster (ärgert sich), dann mit der Schere neben dem Sofa
    *fig("SI", SIX0, BA, SH, [("sigrid", "ruhig"), (beim("sigrid", "ärgert"), "denkt")], bis="schere"),
    name("SI", SIX0, "sigrid", unten=BA - 6, bis="schere"),
    blase("denk", 400, 230, beim("sigrid", "Abfluss"), 1640, 560, inhalt=["Haare im", "Abfluss!"], textsize=34,
          figur=("SI_denkt", SIX0, BA, SH), bis="schere"),
    ficon("tabler", "bath", 1640, 760, 120, beim("sigrid", "Abfluss"), fuell=WEISS, bis="schere"),
    *fig("SI", SIX1, BA, SH, [("schere", "schleicht"), ("schnitt", "entschlossen"), (beim("wach", "wacht"), "ertappt")], bis="s1"),
    *redet("SI_redet", SIX1, BA, SH, "s1", "frage"),
    *fig("SI", SIX1, BA, SH, [("frage", "denkt")], erst="cut"),
    name("SI", SIX1, "schere", unten=BA - 6, d=0.0, anim="cut"),
    ficon("tabler", "scissors", SIX1 - 105, BA - SH * 0.47, 80, "schere", fuell=GRAU, bis=beim("wach", "wacht")),
    pl("Schere", SIX1 - 105, BA - SH * 0.47 + 30, "schere", fill=WEISS, size=26, anker="m", bis="schnitt"),
    pl("heimlich", 1110, 230, beim("schnitt", "heimlich"), fill=GELB, size=30, anker="m", bis=beim("wach", "wacht")),
    pl("Haare ab", 470, 300, beim("schnitt", "ab"), fill=PINK, size=32, anker="m", bis="k1"),
    blase("sprech", 560, 190, "k1", 780, 280, inhalt=["Meine Haare! Das ist", "Körperverletzung!"], textsize=34, figur=KAb,
          bis="s1"),
    blase("sprech", 560, 170, "s1", 1230, 250, inhalt=["Das hat doch gar", "nicht wehgetan."], textsize=36, figur=SIb,
          bis="frage"),
    # Frage
    pl("Wer hat recht?", 1600, 520, "frage", fill=PINK, size=34, anker="m"),
    pl("körperlich misshandelt?", 1600, 610, beim("frage2", "misshandelt"), fill=WEISS, size=30, anker="m"),
    pl("an der Gesundheit geschädigt?", 1600, 690, beim("frage2", "Gesundheit"), fill=WEISS, size=30, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Sonntagabend in einer Wohngemeinschaft: Katrin ist auf dem Sofa eingeschlafen. Ihre Mitbewohnerin Sigrid ärgert "
    "sich über Katrins lange Haare im Abfluss und schneidet sie ihr heimlich mit einer Schere ab. Katrin hat nichts gespürt.",
    "Variante 1: Katrin gibt Sigrid eine kräftige Ohrfeige; die Wange brennt und rötet sich. Gegenstück: Katrin stupst "
    "Sigrid nur leicht an die Schulter. Variante 2: Sigrid rührt heimlich ein Abführmittel in Katrins Tee; Katrin bekommt "
    "Durchfall und Bauchkrämpfe. Variante 3: Katrin schläft vor Aufregung zwei Nächte schlecht. Variante 4: Hautarzt "
    "Doktor Lindner klärt Katrin auf und entfernt mit ihrer Einwilligung fachgerecht ein verdächtiges Muttermal. "
    "Variante 5: Sigrid setzt die Schere an, doch Katrin wacht auf und hält ihre Haare fest.",
], "Wer hat sich nach § 223 StGB strafbar gemacht?")

# Gemeinsame Bühne rechts: kleines Sofa mit Katrin, daneben Sigrid ------------------------------------------------------
KR = int(FR * SITZ)


def wg_buehne(cue, ka_folge, si_folge, lang=False, kax=1430, six=1745, sofa_cue=None):
    """Kleines Sofa mit Katrin und Sigrid; beide blicken zur Tafel nach links (Suffix _r: Katrin wendet sich Sigrid zu)."""
    s_, sitz = sofa(kax + 30, BR, 330, sofa_cue or cue)
    p = "KAL" if lang else "KA"
    return [s_, *fig(p, kax, sitz, KR, ka_folge, erst="cut"), name(p, kax, cue, d=0.0, anim="cut"),
            *fig("SI", six, BR, FR, si_folge, erst="cut"), name("SI", six, cue, d=0.0, anim="cut")], sitz


# C Wortlaut § 223 -------------------------------------------------------------------------------------------------------
P223 = ["„(1) Wer eine andere Person körperlich mißhandelt oder an der Gesundheit",
        "schädigt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.",
        "(2) Der Versuch ist strafbar.“"]
wl223, y223 = wortlaut(90, 170, 1090, P223, "§ 223 StGB", "p223w", size=29,
                       marken=[(0, "andere Person", beim("p223w", "andere")),
                               (0, "körperlich mißhandelt", beim("p223w", "körperlich")),
                               (0, "an der Gesundheit", beim("p223w", "Gesundheit")),
                               (1, "schädigt", beim("p223w", "schädigt")),
                               (2, "Der Versuch ist strafbar.", beim("abs2", "Der"))])
buehne_c, _ = wg_buehne("p223", [("p223", "ruhig"), ("zwei", "denkt")], [("p223", "ruhig"), ("andere", "denkt")])
folie([("p223", "§ 223 StGB › Wortlaut und Varianten")], [
    *tafel("p223", "Körperverletzung, § 223 StGB"),
    *wl223,
    z("Opfer: eine andere Person", 110, y223 + 40, "andere", "Bold", 36),
    z("Selbstverletzung fällt nicht darunter", 150, y223 + 95, beim("andere", "wer"), size=34),
    z("zwei Varianten:", 110, y223 + 175, "zwei", "Bold", 36),
    fl_block(110, y223 + 235, 505, 70, GELB, "vm", [("1. körperliche Misshandlung", "ExtraBold", 31, INK)]),
    fl_block(645, y223 + 235, 505, 70, GRUEN, "vg", [("2. Gesundheitsschädigung", "ExtraBold", 31, INK)]),
    pl("eine genügt, oft beide", 110, y223 + 335, "eine", fill=WEISS, size=30),
    *buehne_c,
])

# D Körperliche Misshandlung: Grundfall --------------------------------------------------------------------------------
PT = "I. Tatbestand"
buehne_d, sitz_d = wg_buehne("mh", [("mh", "ruhig"), ("haare", "skeptisch"), ("mh_ok", "ruhig")],
                             [("mh", "ruhig"), ("schmerz", "denkt"), ("mh_ok", "ertappt")])
folie([("mh", f"{PT} › 1. körperliche Misshandlung › Grundfall: Haare ab")], [
    *tafel("mh", "1. Körperliche Misshandlung"),
    z("üble und unangemessene Behandlung,", 110, 185, beim("mhdef", "üble"), "Bold", 36),
    z("die das körperliche Wohlbefinden", 150, 240, beim("mhdef", "Wohlbefinden"), size=34),
    z("oder die körperliche Unversehrtheit", 150, 292, "unvers", size=34),
    z("nicht nur unerheblich beeinträchtigt", 150, 344, "nnu", "Bold", 34),
    z("BGH, Beschl. v. 13.12.2016 – 3 StR 354/16, Rn. 4", 110, 400, beim("nnu", "beeinträchtigt"), "Bold", 26, farbe=TEXT),
    pl("Schmerz ist nicht nötig", 110, 450, "schmerz", fill=GELB, size=32),
    z("Katrin: im Schlaf nichts gespürt", 110, 540, "haare", size=34),
    z("aber: Haare ab, Aussehen deutlich verändert", 110, 592, beim("haare", "Aber"), size=34),
    ok(135, 668, "unv_ok", gr=22), z("Unversehrtheit mehr als nur unerheblich beeinträchtigt", 175, 645, "unv_ok", "Bold", 32),
    z("BGH, Beschl. v. 17.4.2008 – 4 StR 634/07, Rn. 3: Haare abschneiden", 110, 705, "dread", "Bold", 26, farbe=TEXT),
    fl_block(110, 760, 1040, 80, GELB, "mh_ok", [("Sigrid hat Katrin körperlich misshandelt", "ExtraBold", 36, INK)]),
    ok(1110, 800, beim("mh_ok", "misshandelt"), gr=22),
    *buehne_d,
    ficon("tabler", "zzz", 1410, 440, 70, "haare", fuell=None, bis=beim("haare", "Aber")),
    pl("nichts gespürt", 1410, 290, "haare", fill=WEISS, size=26, anker="m", bis=beim("haare", "Aber")),
    ficon("tabler", "scissors", 1410, 440, 90, beim("haare", "Aber"), fuell=GRAU),
    pl("Haare ab", 1410, 290, beim("haare", "Haare"), fill=PINK, size=28, anker="m"),
    pl("Einwand zieht nicht", 1740, 380, "mh_ok", fill=GELB, size=26, anker="m"),
])

# E Bagatellgrenze: Ohrfeige und Stups ---------------------------------------------------------------------------------
buehne_e, sitz_e = wg_buehne("bag", [("bag", "ruhig"), ("v1", "wuetend_r"), ("stups", "ruhig_r")],
                             [("bag", "ruhig"), ("ohr", "aua"), ("stups", "ruhig"), ("stups_no", "denkt")])
folie([("bag", f"{PT} › 1. körperliche Misshandlung › Bagatellgrenze, Variante 1")], [
    *tafel("bag", "Wo liegt die Grenze?"),
    z("Nicht jeder vorsätzliche Schlag oder Stoß", 110, 185, "bag2", "Bold", 36),
    z("ist eine Körperverletzung.", 150, 240, beim("bag2", "Körperverletzung"), size=34),
    z("BGH, 3 StR 354/16, Rn. 4", 110, 296, beim("bag2", "betont"), "Bold", 26, farbe=TEXT),
    z("Variante 1: kräftige Ohrfeige", 110, 370, "v1", "Bold", 36),
    z("Wange brennt und rötet sich", 150, 425, "ohr", size=34),
    z("Wohlbefinden mehr als nur unerheblich beeinträchtigt", 150, 477, beim("ohr", "Wohlbefinden"), size=33),
    ok(135, 555, "ohr_ok", gr=22), z("Misshandlung", 175, 532, "ohr_ok", "Bold", 36),
    z("Gegenstück: nur ein leichter Stups an die Schulter", 110, 625, "stups", "Bold", 34),
    nein(135, 703, "stups_no", gr=20), z("unter der Schwelle", 175, 680, "stups_no", "Bold", 36),
    *buehne_e,
    ficon("tabler", "hand-stop", 1640, 585, 80, "v1", fuell=GELB, bis="stups"),
    pl("Ohrfeige", 1600, 380, "v1", fill=PINK, size=28, anker="m", bis="stups"),
    ficon("tabler", "hand-finger", 1660, 650, 70, "stups", fuell=GELB),
    pl("leichter Stups", 1600, 380, "stups", fill=WEISS, size=28, anker="m"),
])

# F Gesundheitsschädigung: Abführmittel --------------------------------------------------------------------------------
buehne_f, sitz_f = wg_buehne("gs", [("gs", "ruhig"), ("durch", "krank"), ("beide", "denkt")],
                             [("gs", "ruhig"), ("v2", "schleicht"), ("gs_ok", "ertappt")], lang=True)
folie([("gs", f"{PT} › 2. Gesundheitsschädigung › Variante 2: Abführmittel")], [
    *tafel("gs", "2. Gesundheitsschädigung"),
    z("jedes Hervorrufen oder Steigern eines Zustands,", 110, 185, beim("gsdef", "jedes"), "Bold", 35),
    z("der vom Normalzustand der körperlichen", 150, 240, beim("gsdef", "Normalzustand"), size=34),
    z("Funktionen nachteilig abweicht", 150, 292, beim("gsdef", "Funktionen"), size=34),
    z("auf welche Art: gleich", 150, 344, "art", size=34),
    z("BGH, Beschl. v. 18.7.2013 – 4 StR 168/13, Rn. 13", 110, 400, beim("art", "gleich"), "Bold", 26, farbe=TEXT),
    z("Variante 2: Abführmittel heimlich im Tee", 110, 470, "v2", "Bold", 36),
    z("Durchfall und Bauchkrämpfe", 150, 525, "durch", size=34),
    ok(135, 603, beim("gs_ok", "Gesundheitsschädigung"), gr=22), z("Gesundheitsschädigung", 175, 580, beim("gs_ok", "Gesundheitsschädigung"), "Bold", 36),
    ok(135, 663, "beide", gr=22), z("Krämpfe: zugleich Misshandlung", 175, 640, "beide", "Bold", 36),
    *buehne_f,
    ficon("tabler", "mug", 1410, 440, 80, "v2", fuell=WEISS),
    ficon("tabler", "pill", 1740, 440, 60, beim("v2", "Abführmittel"), fuell=PINK),
    pl("Abführmittel", 1740, 290, beim("v2", "Abführmittel"), fill=PINK, size=26, anker="m"),
    pl("Durchfall, Krämpfe", 1410, 290, "durch", fill=WEISS, size=26, anker="m"),
])

# G Psychische Folgen ---------------------------------------------------------------------------------------------------
buehne_g, sitz_g = wg_buehne("psy", [("psy", "ruhig"), ("v3", "muede"), ("v3_no", "denkt")],
                             [("psy", "ruhig"), ("rein", "denkt")])
folie([("psy", f"{PT} › 2. Gesundheitsschädigung › psychische Folgen, Variante 3")], [
    *tafel("psy", "Und psychische Folgen?"),
    z("Variante 3: zwei Nächte schlecht geschlafen", 110, 185, "v3", "Bold", 36),
    nein(135, 268, "rein", gr=20), z("rein psychische Empfindungen genügen nicht", 175, 245, "rein", size=34),
    nein(135, 320, "aufr", gr=20), z("auch keine bloße Aufregung oder Angst", 175, 297, "aufr", size=34),
    fl_block(110, 370, 1040, 120, GELB, "somat", [("erst ein pathologischer, körperlich", "ExtraBold", 34, INK),
                                                   ("objektivierbarer Zustand", "ExtraBold", 34, INK)]),
    z("etwa: Schlafverhalten dauerhaft geändert", 150, 520, "schlaf", size=34),
    z("BGH, 4 StR 168/13, Rn. 13 f.", 110, 578, beim("schlaf", "dauerhaft"), "Bold", 26, farbe=TEXT),
    nein(135, 668, "v3_no", gr=20), z("zwei unruhige Nächte: reicht nicht", 175, 645, "v3_no", "Bold", 36),
    *buehne_g,
    ficon("tabler", "moon", 1410, 440, 70, "v3", fuell=GELB),
    pl("zwei Nächte", 1410, 290, "v3", fill=WEISS, size=26, anker="m"),
    ficon("tabler", "brain", 1740, 440, 80, "rein", fuell=PINK),
    pl("nur psychisch", 1740, 290, "rein", fill=WEISS, size=26, anker="m", bis="somat"),
    pl("körperlich objektivierbar?", 1836, 200, "somat", fill=GELB, size=26, anker="r"),
])

# H Ärztlicher Heileingriff: Hautarztpraxis -----------------------------------------------------------------------------
LIX, KAX_H = 1745, 1440
LIEGE, LF = liege(KAX_H - 30, BR, 320, "arzt")
LIb = ("LI_redet", LIX, BR, FR)
KAHb = ("KA_einv_r", KAX_H, LF, KR)
folie([("arzt", "Variante 4 · Ärztlicher Heileingriff"), ("rspr", "Variante 4 · Heileingriff: Rechtsprechung und Lehre")], [
    *tafel("arzt", "Ärztlicher Heileingriff"),
    z("Variante 4: verdächtiges Muttermal", 110, 185, "v4", "Bold", 36),
    z("aufgeklärt über Ablauf und Risiken", 150, 240, beim("v4", "aufgeklärt"), size=34),
    pl("fachgerecht entfernt", 110, 295, "fach", fill=WEISS, size=30),
    fl_block(110, 370, 505, 64, BLAU, "rspr", [("Rechtsprechung", "ExtraBold", 32, INK)]),
    z("Tatbestand erfüllt", 130, 450, beim("rspr", "Tatbestand"), size=31, rechts=615),
    z("rechtmäßig grundsätzlich", 130, 495, "einw", size=31, rechts=615),
    z("nur mit Einwilligung", 130, 540, beim("einw", "Einwilligung"), "Bold", 31, rechts=615),
    z("nach Aufklärung", 130, 585, "aufkl", "Bold", 31, rechts=615),
    z("BGH, 4 StR 549/06, Rn. 22", 130, 632, beim("aufkl", "Aufklärung"), "Bold", 25, farbe=TEXT, rechts=615),
    fl_block(645, 370, 505, 64, LILA, "lehre", [("Teile der Lehre", "ExtraBold", 32, INK)]),
    z("angezeigt und", 665, 450, beim("lehre", "angezeigter"), size=31),
    z("kunstgerecht ausgeführt:", 665, 495, beim("lehre", "kunstgerecht"), size=31),
    z("schon keine", 665, 540, beim("lehre", "keine"), "Bold", 31),
    z("Körperverletzung", 665, 585, beim("lehre", "keine"), "Bold", 31),
    fl_block(110, 700, 1040, 80, GELB, "v4_erg", [("beide: Doktor Lindner nicht strafbar", "ExtraBold", 36, INK)]),
    ok(1110, 740, beim("v4_erg", "nicht"), gr=22),
    LIEGE,
    *fig("KA", KAX_H, LF, KR, [("arzt", "ruhig_r"), ("v4", "denkt_r")], bis="k2"),
    *redet("KA_einv_r", KAX_H, LF, KR, "k2", "fach"),
    *fig("KA", KAX_H, LF, KR, [("fach", "ruhig_r"), ("lehre", "denkt_r"), ("v4_erg", "einv_r")], erst="cut"),
    name("KA", KAX_H, "arzt", d=0.0),
    *fig("LI", LIX, BR, FR, [("arzt", "ruhig")], bis="l1"),
    *redet("LI_redet", LIX, BR, FR, "l1", "k2"),
    *fig("LI", LIX, BR, FR, [("k2", "froh"), ("rspr", "denkt"), ("v4_erg", "froh")], erst="cut"),
    name("LI", LIX, "arzt"),
    ficon("tabler", "stethoscope", 1560, 300, 80, "arzt", fuell=None),
    pl("Hautarztpraxis", 1560, 160, "arzt", fill=WEISS, size=28, anker="m", bis="l1"),
    blase("sprech", 560, 170, "l1", 1530, 220, inhalt=["Darf ich das Muttermal", "jetzt entfernen?"], textsize=33,
          figur=LIb, bis="k2"),
    blase("sprech", 520, 160, "k2", 1530, 220, inhalt=["Ja, ich bin", "einverstanden."], textsize=36, figur=KAHb,
          bis="fach"),
    pl("Einwilligung", 1560, 360, beim("einw", "Einwilligung"), fill=GELB, size=26, anker="m"),
])

# I Versuch -------------------------------------------------------------------------------------------------------------
buehne_i, sitz_i = wg_buehne("vers", [("vers", "schlaeft"), (beim("v5", "da"), "erschrickt")],
                             [("vers", "schleicht"), (beim("v5", "da"), "ertappt")], lang=True)
folie([("vers", "Variante 5 · Versuch, §§ 223 Abs. 2, 22 StGB")], [
    *tafel("vers", "Versuch, § 223 Abs. 2 StGB"),
    z("Variante 5: Schere angesetzt, Katrin wacht auf", 110, 185, "v5", "Bold", 36),
    z("und hält ihre Haare fest", 150, 240, beim("v5", "hält"), size=34),
    ok(135, 333, "tatent", gr=22), z("Tatentschluss: Haare abschneiden", 175, 310, "tatent", "Bold", 36),
    ok(135, 398, "ansetz", gr=22), z("nach ihrer Vorstellung unmittelbar angesetzt", 175, 375, "ansetz", "Bold", 34),
    z("§ 22 StGB", 175, 428, beim("ansetz", "unmittelbar"), "Bold", 26, farbe=TEXT),
    fl_block(110, 500, 1040, 80, GELB, "vers_ok", [("Versuch strafbar, § 223 Abs. 2", "ExtraBold", 38, INK)]),
    ok(1110, 540, beim("vers_ok", "Versuch"), gr=22),
    *buehne_i,
    ficon("tabler", "scissors", 1680, 745, 60, "v5", fuell=GRAU),
    pl("Schere angesetzt", 1700, 380, "v5", fill=WEISS, size=26, anker="m", bis=beim("v5", "da")),
    pl("Katrin wacht auf", 1420, 380, beim("v5", "da"), fill=PINK, size=26, anker="m"),
    ficon("tabler", "hand-grab", 1520, 610, 70, beim("v5", "hält"), fuell=GELB),
])

# J Ergebnis und Strafantrag -------------------------------------------------------------------------------------------
buehne_j, sitz_j = wg_buehne("erg", [("erg", "ruhig"), ("p230", "denkt"), ("frist", "skeptisch")],
                             [("erg", "ruhig"), ("erg2", "ertappt")])
folie([("erg", "Grundfall › II. Rechtswidrigkeit, III. Schuld"), ("erg2", "Grundfall › Ergebnis: § 223 Abs. 1 StGB"),
       ("p230", "Grundfall › Strafantrag, § 230 StGB")], [
    *tafel("erg", "Zurück zum Grundfall"),
    z("Rechtfertigung, Entschuldigung: nicht ersichtlich", 110, 185, "rw", size=36),
    fl_block(110, 255, 1040, 80, GELB, "erg2", [("Sigrid: strafbar wegen Körperverletzung", "ExtraBold", 36, INK)]),
    ok(1110, 295, beim("erg2", "strafbar"), gr=22),
    z("§ 230: nur auf Antrag", 110, 385, "p230", "Bold", 38),
    z("außer: besonderes öffentliches Interesse,", 150, 445, "oeff", size=34),
    z("bejaht von der Strafverfolgungsbehörde", 150, 497, beim("oeff", "bejaht"), size=34),
    z("Frist: drei Monate (§ 77b StGB)", 110, 580, "frist", "Bold", 36),
    z("ab Kenntnis von Tat und Täterin", 150, 635, "kennt", size=34),
    *buehne_j,
    ficon("tabler", "signature", 1410, 440, 90, beim("p230", "Antrag"), fuell=GELB),
    pl("Strafantrag", 1410, 290, beim("p230", "Antrag"), fill=GELB, size=26, anker="m"),
    ficon("tabler", "calendar-time", 1740, 440, 80, "frist", fuell=WEISS),
    pl("drei Monate", 1740, 290, "frist", fill=WEISS, size=26, anker="m"),
])

# K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Varianten trennen, § 224 nicht vorschnell")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("beide Varianten definieren", 200, 200, beim("tipp", "Definiere"), "Bold", 36),
    z("und getrennt subsumieren", 200, 252, beim("tipp", "subsumiere"), "Bold", 36),
    fl_block(110, 340, 1040, 64, BLAU, "tipp2", [("Schere: nicht vorschnell § 224", "ExtraBold", 34, INK)]),
    z("Gegenstand zum Haareabschneiden:", 150, 430, "tipp3", size=34),
    z("in der Regel kein gefährliches Werkzeug", 150, 482, beim("tipp3", "kein"), "Bold", 34),
    z("BGH, 4 StR 634/07, Rn. 4", 150, 540, beim("tipp3", "Werkzeug"), "Bold", 26, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.0),
    ficon("tabler", "scissors", 1800, 470, 80, "tipp2", fuell=GRAU),
])

# L Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 250
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Körperverletzung, § 223 StGB", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 190, "k_i", "ExtraBold", 40, rechts=1820),
    z("1. objektiv: andere Person", K2, 250, "k1a", "Bold", 36, rechts=1820),
    z("körperliche Misshandlung", K3, 305, "k1b", size=36, rechts=1820),
    z("oder Gesundheitsschädigung", K3, 355, "k1c", size=36, rechts=1820),
    z("Kausalität und objektive Zurechnung", K3, 405, "k1d", size=36, rechts=1820),
    z("2. subjektiv: Vorsatz", K2, 465, "k1e", "Bold", 36, rechts=1820),
    z("II. Rechtswidrigkeit (beim Arzt: Einwilligung)", K1, 545, "k_ii", "ExtraBold", 40, rechts=1820),
    z("III. Schuld", K1, 620, "k_iii", "ExtraBold", 40, rechts=1820),
    z("IV. Strafantrag, § 230", K1, 695, "k_iv", "ExtraBold", 40, rechts=1820),
    pl("Vollendung gescheitert: Versuch, § 223 Abs. 2", K1, 790, "k_v", fill=GELB, size=34),
])

# M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Misshandlung", "a"), (": kein Schmerz nötig,", 0)], [("aber mehr als nur unerheblich.", 0)]], 750, 300,
                44, "merke", {"a": beim("merke", "Misshandlung")}),
    *markertext([[("Gesundheitsschädigung", "b"), (":", 0)], [("nachteilig abweichender Zustand.", 0)]], 750, 470, 44, "m2",
                {"b": beim("m2", "Gesundheitsschädigung")}),
    *markertext([[("Psychische Folgen", "c"), (" nur, wenn", 0)], [("krankhaft und körperlich objektivierbar.", 0)]], 750,
                640, 44, "m3", {"c": beim("m3", "Psychische")}),
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
