"""Folge 011 · Deliktsaufbau Strafrecht: Tatbestand, Rechtswidrigkeit, Schuld – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Am Uferweg, B Dreißig Meter weiter, C Sachverhalt, D Warum drei Stufen?, E Das Gesetz trennt,
F I. objektiver Tatbestand (Handlung, Erfolg), G Kausalität und Zurechnung, H subjektiver Tatbestand, I § 16-Abwandlung,
J II. Rechtswidrigkeit, K III. Schuld, L Ergebnis, M Gegenfall (Szene), N Gegenfall (Prüfung), O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (fahrendes Rad, stürzendes Rad)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_011/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
FLUSS = (196, 222, 248, 255)
DAUER = bausteine._cj()["dauer"]
PA = "A. Nele, § 223 I StGB"
PT = f"{PA} › I. Tatbestand"

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())
_ERSATZ_OK = {"→"}


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen); nur „→“ kommt aus der Ersatzschrift."""
    fehl = {c for c in text if ord(c) not in _CMAP and c not in _ERSATZ_OK and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def liegend(el, winkel, cx, unten):
    """Requisit gekippt (umgefallenes Rad): Sprite gedreht, unten mittig auf (cx, unten)."""
    el.sprite = el.sprite.rotate(winkel, expand=True, resample=Image.BICUBIC)
    el.sprite = el.sprite.crop(el.sprite.getbbox())
    el.x, el.y = int(cx - el.sprite.width / 2), int(unten - el.sprite.height)
    return el


def uferweg(cue, baeume=((130, 150), (1790, 200))):
    """Uferweg: Flussband hinter dem Weg, Wegkante, Bäume."""
    els = [fl_block(60, 770, 1800, 92, FLUSS, cue, [], rand=4, anim="fade"),
           linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)]
    for i, (x, w) in enumerate(baeume):
        els.append(ficon("tabler", "trees" if i % 2 else "tree", x, BODEN - 2, w, cue, fuell=GRUEN, anim="fade"))
    return els


def wellen(cue, xs):
    return [ficon("tabler", "ripple", x, 840, 90, cue, fuell=BLAU, anim="fade") for x in xs]


BODEN, FH = 880, 440
RAD_H, BODEN_H = int(FH * 1.10), int(FH * 0.66)        # Kopfgröße angeglichen (Kopfbreite gemessen, figuren_011.py)
FX, BR, FR = 1560, 930, 500                           # Figur rechts neben der Tafel

# A Fall: am Uferweg ------------------------------------------------------------------------------------------------------
AX, NX, HX = 230, 860, 1340                           # Albrecht (Angler), Nele, Holger (Rad)
HOr = ("HO_rad_redet", HX, BODEN, RAD_H)
folie([(("fall", -0.4), "Fall · Am Uferweg")], [      # Prüfpfad und Grundbild ab 0,0 s
    *uferweg(("fall", -0.4), baeume=((130, 150),)),
    *wellen(("fall", -0.4), (1700,)),
    pl("Der Uferweg-Fall", 70, 40, ("fall", -0.4), fill=GELB, size=48),
    pl("Fluss", 1000, 785, ("fall", -0.4), fill=FLUSS, size=28, anker="m", anim="fade"),
    peep_voll("AL_ruhig_r", AX, BODEN, FH - 20, ("fall", -0.4), anim="cut"),
    linienzug([(275, 640), (470, 470)], ("fall", -0.4), breite=6, farbe=INK),          # Angelrute
    linienzug([(470, 470), (490, 800)], ("fall", -0.4), breite=2, farbe=INK),          # Schnur
    ficon("tabler", "fish-hook", 490, 835, 34, ("fall", -0.4), anim="fade"),
    pl("Herr Albrecht, Angler", AX + 60, BODEN + 22, ("fall", 0.2), fill=GRUEN, size=28, anker="m"),
    # Nele joggt
    peep_voll("NE_laeuft_r", NX, BODEN, FH, "nele", bis="t1"),
    pl("Nele, Mitte 50", NX, BODEN + 22, "nele", fill=ORANGE, size=30, anker="m", d=0.2),
    pl("joggt ihre Runde", NX, 280, beim("nele", "joggt"), fill=WEISS, size=30, anker="m", bis="holger"),
    # Holger rast heran
    szene(bewegt(peep_voll("HO_faehrt", HX, BODEN, RAD_H, "holger", anim="cut", bis="t1"), "holger", ("t1", -0.2), 250),
          "011rad*", 1.0),
    pl("viel zu schnell, zu knapp", 1340, 200, beim("holger", "viel"), fill=ROT, size=32, anker="m", bis="t1"),
    *redet("HO_rad_redet", HX, BODEN, RAD_H, "t1", "halt"),
    pl("Holger", HX, BODEN + 22, "holger", fill=BLAU, size=30, anker="m", d=0.3),
    blase("sprech", 380, 170, "t1", 1500, 250, inhalt=["Platz da!"], textsize=44, figur=HOr, bis="halt"),
    peep_voll("NE_schreck_r", NX, BODEN, FH, "t1", anim="cut", bis="sprung"),
    peep_voll("NE_schreck_r", NX - 170, BODEN, FH, "sprung", anim="cut"),
    pfeil_ink(NX - 20, 330, NX - 150, 330, "sprung"),
    pl("zur Seite", NX - 90, 250, "sprung", fill=WEISS, size=30, anker="m"),
])

# B Fall: dreißig Meter weiter --------------------------------------------------------------------------------------------
NB, HB, AB = 560, 1500, 210
NE_n1 = ("NE_redet_r", 1170, BODEN, FH)
AL_a1 = ("AL_redet_r", AB, BODEN, FH - 20)
folie([("halt", "Fall · Dreißig Meter weiter"), ("frage", "Fall · Die Frage")], [
    *uferweg("halt", baeume=()),
    *wellen("halt", (720, 1080)),
    pl("30 Meter weiter", 70, 40, "halt", fill=GELB, size=44),
    # Holger steht und trinkt
    ficon("ph", "bicycle", HB + 210, BODEN - 2, 250, "halt", fuell=WEISS, bis="sturz"),
    peep_voll("HO_steht", HB, BODEN, FH, "halt", bis=beim("halt", "trinkt")),
    peep_voll("HO_trinkt", HB, BODEN, FH, beim("halt", "trinkt"), anim="cut", bis="sturz"),
    ficon("tabler", "bottle", HB - 60, 560, 70, beim("halt", "trinkt"), fuell=BLAU, bis="sturz"),
    pl("steigt ab, trinkt in Ruhe", HB, 290, beim("halt", "steigt"), fill=WEISS, size=30, anker="m", bis="hin"),
    pl("Holger", HB, BODEN + 22, "halt", fill=BLAU, size=30, anker="m", d=0.2),
    # Albrecht am Ufer
    peep_voll("AL_schaut_r", AB, BODEN, FH - 20, "halt", d=0.2, bis="a1"),
    *redet("AL_redet_r", AB, BODEN, FH - 20, "a1", "frage"),
    peep_voll("AL_schaut_r", AB, BODEN, FH - 20, "frage", anim="cut"),
    pl("Herr Albrecht", AB, BODEN + 22, "halt", fill=GRUEN, size=28, anker="m", d=0.3),
    # Nele läuft hin und stößt
    peep_voll("NE_wut_r", NB, BODEN, FH, ("halt", 0.3), bis="hin"),
    bewegt(peep_voll("NE_wut_r", 1170, BODEN, FH, "hin", anim="cut", bis="n1"), "hin", beim("hin", "stößt"), NB - 1170),
    pl("Nele", NB, BODEN + 22, ("halt", 0.3), fill=ORANGE, size=30, anker="m", bis="hin"),
    pl("Nele", 1170, BODEN + 22, beim("hin", "stößt"), fill=ORANGE, size=30, anker="m"),
    pl("Stoß mit beiden Händen", 1330, 330, beim("hin", "stößt"), fill=ORANGE, size=30, anker="m", bis="sturz"),
    # Sturz
    szene(liegend(ficon("ph", "bicycle", 0, 0, 250, "sturz", fuell=WEISS, anim="cut"), 180, HB + 230, BODEN - 2),
          "011sturz*", 0.9, 0.15),
    peep_voll("HO_boden", HB, BODEN, BODEN_H, "sturz", anim="cut"),
    pl("Schürfwunde am Ellenbogen", HB, 450, beim("sturz", "Ellenbogen"), fill=ROT, size=30, anker="m", bis="frage"),
    ficon("tabler", "bandage", HB, 420, 70, beim("sturz", "schürft"), fuell=ROT, bis="frage"),
    *redet("NE_redet_r", 1170, BODEN, FH, "n1", "frage"),
    peep_voll("NE_ruhig_r", 1170, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 460, 170, "n1", 960, 250, inhalt=["Das war für eben!"], textsize=40, figur=NE_n1, bis="a1"),
    blase("sprech", 560, 170, "a1", 600, 250, inhalt=["Der stand doch längst!"], textsize=38, figur=AL_a1, bis="frage"),
    pl("Hat Nele sich strafbar gemacht?", 960, 130, "frage", fill=PINK, size=38, anker="m"),
    pl("I. Tatbestand", 520, 260, beim("lernst", "Tatbestand"), fill=GELB, size=34, anker="m"),
    pl("II. Rechtswidrigkeit", 960, 260, beim("lernst", "Rechtswidrigkeit"), fill=BLAU, size=34, anker="m"),
    pl("III. Schuld", 1400, 260, beim("lernst", "Schuld"), fill=LILA, size=34, anker="m"),
])

# C Sachverhalt -----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Sonntagmorgen am Uferweg: Der Radfahrer Holger rast viel zu schnell und zu knapp an der Joggerin Nele (Mitte 50) "
    "vorbei und ruft „Platz da!“. Nele springt zur Seite. Dreißig Meter weiter hält Holger an, steigt ab und trinkt in "
    "Ruhe. Nele läuft zu ihm und stößt ihn mit beiden Händen um; dass er sich dabei verletzt, nimmt sie in Kauf. Holger "
    "stürzt über sein Rad und schürft sich den Ellenbogen auf. Nele: „Das war für eben!“ Der Angler Herr Albrecht: "
    "„Der stand doch längst!“",
    "Annahme: Nele ist erwachsen, nüchtern und gesund.",
], "Hat Nele sich strafbar gemacht?")

# D Warum drei Stufen? ----------------------------------------------------------------------------------------------------
PW = "Warum drei Stufen?"
folie([("drei", PW), ("stb", f"{PW} › I. Tatbestand"), ("srw", f"{PW} › II. Rechtswidrigkeit"), ("ssch", f"{PW} › III. Schuld")], [
    *tafel("drei", "Warum drei Stufen?"),
    fl_block(110, 200, 1040, 170, GELB, "stb", [("I. Tatbestand", "ExtraBold", 42, INK),
                                               ("beschreibt, was das Gesetz verbietet", "Regular", 34, INK)]),
    fl_block(110, 400, 1040, 170, BLAU, "srw", [("II. Rechtswidrigkeit", "ExtraBold", 42, INK),
                                               ("Ist die Tat ausnahmsweise erlaubt?", "Regular", 34, INK)]),
    fl_block(110, 600, 1040, 170, LILA, "ssch", [("III. Schuld", "ExtraBold", 42, INK),
                                                ("Kann man sie dem Täter persönlich vorwerfen?", "Regular", 34, INK)]),
    peep_voll("NE_denkt", FX, BR, FR, "drei"),
    pl("Nele", FX, BR + 22, "drei", fill=ORANGE, size=30, anker="m", d=0.2),
    ficon("tabler", "book", FX, 330, 120, "stb", fuell=GELB, bis="srw"),
    ficon("tabler", "shield", FX, 330, 120, "srw", fuell=BLAU, bis="ssch"),
    ficon("tabler", "user-exclamation", FX, 330, 120, "ssch", fuell=LILA),
])

# E Das Gesetz trennt ----------------------------------------------------------------------------------------------------
folie([("gesetz", f"{PW} › Das Gesetz trennt"), ("g20", f"{PW} › Das Gesetz trennt › § 20 StGB"),
       ("g29", f"{PW} › Das Gesetz trennt › § 29 StGB")], [
    *tafel("gesetz", "Das Gesetz trennt selbst"),
    z("§ 32 I StGB: Wer in Notwehr handelt,", 110, 200, beim("gesetz", "Wer"), "Bold", 36),
    z("handelt „nicht rechtswidrig“", 150, 252, beim("gesetz", "nicht"), size=36, farbe=TEXT),
    z("§ 20 StGB: Wer schuldunfähig ist,", 110, 360, "g20", "Bold", 36),
    z("handelt „ohne Schuld“", 150, 412, beim("g20", "ohne"), size=36, farbe=TEXT),
    z("§ 29 StGB: Jeder Beteiligte wird", 110, 520, "g29", "Bold", 36),
    z("nach seiner eigenen Schuld bestraft", 150, 572, beim("g29", "nach"), size=36, farbe=TEXT),
    peep_voll("NE_ruhig", FX, BR, FR, "gesetz"),
    pl("Nele", FX, BR + 22, "gesetz", fill=ORANGE, size=30, anker="m", d=0.2),
    ficon("tabler", "shield", FX, 330, 120, beim("gesetz", "Notwehr"), fuell=BLAU, bis="g20"),
    pl("nicht rechtswidrig", FX, 350, beim("gesetz", "nicht"), fill=BLAU, size=30, anker="m", bis="g20"),
    ficon("tabler", "brain", FX, 330, 120, "g20", fuell=LILA, bis="g29"),
    pl("ohne Schuld", FX, 350, beim("g20", "ohne"), fill=LILA, size=30, anker="m", bis="g29"),
    ficon("tabler", "users-group", FX, 330, 130, "g29", fuell=ORANGE),
    pl("jeder nach eigener Schuld", FX, 350, beim("g29", "eigenen"), fill=ORANGE, size=28, anker="m"),
])

# F I. 1. objektiver Tatbestand: Handlung, Erfolg ------------------------------------------------------------------------
folie([("tb", f"{PT} › 1. objektiv"), ("handlung", f"{PT} › 1. objektiv › Tathandlung"),
       ("erfolg", f"{PT} › 1. objektiv › Erfolg")], [
    *tafel("tb", "A. Nele: Körperverletzung, § 223 I StGB", size=44),
    z("I. Tatbestand", 110, 190, beim("tb", "Römisch"), "ExtraBold", 38),
    z("1. objektiver Tatbestand", 150, 245, beim("tb", "objektiv"), "Bold", 36),
    ok(170, 330, "handlung", gr=20), z("a) Tathandlung: Nele stößt Holger", 205, 305, "handlung", size=34),
    z("b) Erfolg: körperliche Misshandlung =", 205, 375, "erfolg", "Bold", 34),
    z("jede üble, unangemessene Behandlung,", 245, 427, beim("erfolg", "jede"), size=32, farbe=TEXT),
    z("die das körperliche Wohlbefinden", 245, 472, beim("erfolg", "die"), size=32, farbe=TEXT),
    z("nicht nur unerheblich beeinträchtigt", 245, 517, beim("erfolg", "nicht"), size=32, farbe=TEXT),
    ok(210, 600, "wunde", gr=20), z("Sturz mit Schürfwunde (+)", 245, 575, "wunde", size=34),
    ok(210, 660, beim("wunde", "Gesundheitsschädigung"), gr=20),
    z("Wunde: auch Gesundheitsschädigung (+)", 245, 635, beim("wunde", "Gesundheitsschädigung"), size=34),
    z("(nachteilig vom Normalzustand abweichender Zustand)", 245, 690, beim("wunde", "Gesundheitsschädigung"),
      size=28, farbe=TEXT),
    peep_voll("HO_boden", FX, BR, int(FR * 0.66), "tb", bis="wunde"),
    peep_voll("HO_boden_muede", FX, BR, int(FR * 0.66), "wunde", anim="cut"),
    pl("Holger", FX, BR + 22, "tb", fill=BLAU, size=30, anker="m", d=0.2),
    ficon("tabler", "hand-stop", FX, 360, 110, beim("handlung", "stößt"), fuell=ORANGE, bis="erfolg"),
    pl("Stoß", FX, 390, beim("handlung", "stößt"), fill=ORANGE, size=30, anker="m", bis="erfolg"),
    ficon("tabler", "mood-sad", FX, 360, 110, beim("erfolg", "Wohlbefinden"), fuell=GELB, bis="wunde"),
    ficon("tabler", "bandage", FX, 360, 110, "wunde", fuell=ROT),
    pl("Schürfwunde", FX, 390, "wunde", fill=ROT, size=30, anker="m"),
])

# G Kausalität, objektive Zurechnung -------------------------------------------------------------------------------------
KX = 1570
folie([("kausal", f"{PT} › 1. objektiv › Kausalität"), ("zurech", f"{PT} › 1. objektiv › objektive Zurechnung")], [
    *tafel("kausal", "I. 1. objektiver Tatbestand", size=46),
    z("c) Kausalität:", 150, 200, "kausal", "Bold", 36),
    z("jede Bedingung, die nicht hinweggedacht", 190, 255, beim("kausal", "jede"), size=34, farbe=TEXT),
    z("werden kann, ohne dass der Erfolg entfiele", 190, 303, beim("kausal", "werden"), size=34, farbe=TEXT),
    ok(170, 385, beim("kausal", "Ohne"), gr=20), z("ohne Stoß kein Sturz", 205, 360, beim("kausal", "Ohne"), "Bold", 34),
    z("d) objektive Zurechnung (Lehre):", 150, 470, "zurech", "Bold", 36),
    z("Im Sturz verwirklicht sich die Gefahr,", 190, 525, beim("zurech", "Im"), size=34, farbe=TEXT),
    z("die Nele geschaffen hat", 190, 573, beim("zurech", "Gefahr"), size=34, farbe=TEXT),
    ok(170, 655, beim("zurech", "geschaffen"), gr=20),
    z("objektiver Tatbestand erfüllt", 205, 630, beim("zurech", "geschaffen"), "Bold", 34),
    # Kausalkette rechts
    ficon("tabler", "hand-stop", KX, 240, 100, "kausal", fuell=ORANGE),
    pl("Stoß", KX, 255, "kausal", fill=ORANGE, size=32, anker="m"),
    pfeil_ink(KX, 335, KX, 405, beim("kausal", "Ohne")),
    liegend(ficon("ph", "bicycle", 0, 0, 130, beim("kausal", "Sturz"), fuell=WEISS), 180, KX, 520),
    pl("Sturz", KX, 535, beim("kausal", "Sturz"), fill=BLAU, size=32, anker="m"),
    pfeil_ink(KX, 615, KX, 685, beim("kausal", "Sturz")),
    ficon("tabler", "bandage", KX, 800, 100, beim("kausal", "Sturz"), fuell=ROT),
    pl("Schürfwunde", KX, 815, beim("kausal", "Sturz"), fill=ROT, size=32, anker="m"),
    ring(KX, 520, 285, 400, beim("zurech", "verwirklicht"), farbe=DGRUEN, breite=6),
    pl("Gefahr verwirklicht", KX, 935, beim("zurech", "verwirklicht"), fill=GRUEN, size=30, anker="m"),
])

# H I. 2. subjektiver Tatbestand: § 15, Vorsatz ---------------------------------------------------------------------------
NE_v = ("NE_denkt", FX, BR, FR)
folie([("subj", f"{PT} › 2. subjektiv, § 15 StGB"), ("vorsatz", f"{PT} › 2. subjektiv › Vorsatz")], [
    *tafel("subj", "I. 2. subjektiver Tatbestand", size=46),
    z("§ 15 StGB: Strafbar ist nur vorsätzliches", 110, 200, beim("subj", "Strafbar"), "Bold", 36),
    z("Handeln, wenn nicht das Gesetz fahrlässiges", 110, 250, beim("subj", "Handeln"), "Bold", 36),
    z("Handeln ausdrücklich mit Strafe bedroht", 110, 300, beim("subj", "ausdrücklich"), "Bold", 36),
    z("Vorsatz, vereinfacht: Wissen und Wollen", 110, 420, "vorsatz", "ExtraBold", 38),
    ok(170, 505, beim("vorsatz", "Nele"), gr=20), z("Nele wollte Holger umstoßen", 205, 480, beim("vorsatz", "Nele"), size=34),
    ok(170, 565, beim("vorsatz", "nahm"), gr=20), z("und nahm in Kauf, dass er sich verletzt", 205, 540, beim("vorsatz", "nahm"), size=34),
    peep_voll("NE_ruhig", FX, BR, FR, "subj", bis="vorsatz"),
    pl("Nele", FX, BR + 22, "subj", fill=ORANGE, size=30, anker="m", d=0.2),
    ficon("tabler", "book", FX, 330, 120, "subj", fuell=GELB, bis="vorsatz"),
    pl("§ 15", FX, 350, "subj", fill=GELB, size=30, anker="m", bis="vorsatz"),
    peep_voll("NE_denkt", FX, BR, FR, "vorsatz", anim="cut"),
    blase("denk", 380, 240, beim("vorsatz", "Nele"), 1580, 210, inhalt=["umstoßen!"], textsize=40, figur=NE_v),
])

# I § 16-Abwandlung, Ergebnis Tatbestand ----------------------------------------------------------------------------------
folie([("p16", f"{PT} › 2. subjektiv › Tatumstandsirrtum, § 16 StGB"), ("tb_erg", f"{PT} › erfüllt")], [
    *tafel("p16", "Abwandlung: Irrtum über Tatumstände", size=44),
    z("Arm beim Dehnen nach hinten geschwungen,", 110, 200, beim("p16", "Dehnen"), size=34),
    z("weiß nicht, dass dort jemand steht", 110, 250, beim("p16", "weiß"), size=34),
    z("§ 16 I StGB: Wer einen Tatumstand nicht", 110, 340, "p16b", "Bold", 36),
    z("kennt, handelt nicht vorsätzlich", 110, 390, beim("p16b", "handelt"), "Bold", 36),
    z("dann allenfalls fahrlässige Körperverletzung,", 110, 480, "p229", size=34, farbe=TEXT),
    z("§ 229 StGB", 110, 528, beim("p229", "Paragraf"), size=34, farbe=TEXT),
    fl_block(110, 640, 1040, 150, GRUEN, "tb_erg", [("Bei Nele: Tatbestand erfüllt", "ExtraBold", 40, INK),
                                                  ("sie kannte alle Tatumstände", "Regular", 34, INK)]),
    peep_voll("NE_ruhig", 1420, BR, FR, "p16", bis="tb_erg"),
    pl("Nele", 1420, BR + 22, "p16", fill=ORANGE, size=30, anker="m", bis="tb_erg"),
    pl("dehnt sich", 1420, 330, beim("p16", "Dehnen"), fill=WEISS, size=30, anker="m", bis="tb_erg"),
    peep_voll("AL_ruhig", 1760, BR, FR - 30, beim("p16", "dort"), bis="tb_erg"),
    pl("jemand", 1760, BR + 22, beim("p16", "dort"), fill=GRUEN, size=28, anker="m", bis="tb_erg"),
    pfeil_ink(1520, 640, 1640, 640, beim("p16", "Arm")),
    pl("weiß sie nicht", 1600, 250, beim("p16", "weiß"), fill=GELB, size=30, anker="m", bis="tb_erg"),
    peep_voll("NE_wut", FX, BR, FR, "tb_erg", anim="cut"),
    pl("Nele, im Fall", FX, BR + 22, "tb_erg", fill=ORANGE, size=30, anker="m"),
])

# J II. Rechtswidrigkeit -----------------------------------------------------------------------------------------------
PR = f"{PA} › II. Rechtswidrigkeit"
folie([("rw", PR), ("nw", f"{PR} › Notwehr, § 32 StGB"), ("vorbei", f"{PR} › Notwehr › gegenwärtiger Angriff?"),
       ("rw_erg", f"{PA} › II. rechtswidrig")], [
    *tafel("rw", "II. Rechtswidrigkeit"),
    z("Tatbestand deutet auf Rechtswidrigkeit hin", 110, 195, "indiz", "Bold", 34),
    z("(Lehre: Indizwirkung)", 150, 243, beim("indiz", "Tatbestand"), size=30, farbe=TEXT),
    z("entfällt nur bei einem Rechtfertigungsgrund", 110, 305, "rfg", size=34),
    z("Notwehr, § 32 StGB:", 110, 390, "nw", "ExtraBold", 38),
    z("gegenwärtiger rechtswidriger Angriff?", 150, 445, beim("nw", "Sie"), "Bold", 34),
    z("Fahrweise gefährlich, aber vorbei:", 150, 520, "vorbei", size=34, farbe=TEXT),
    z("Holger steht längst und trinkt", 150, 568, beim("vorbei", "steht"), size=34, farbe=TEXT),
    nein(165, 645, beim("vorbei", "Ein"), gr=20), z("kein Angriff mehr: Notwehr (−)", 205, 620, beim("vorbei", "Ein"), "Bold", 34),
    fl_block(110, 700, 1040, 120, ROT, "rw_erg", [("Nele handelte rechtswidrig", "ExtraBold", 40, INK)]),
    # rechts: Zeitleiste und Holger
    pl("Raserei", 1300, 170, beim("vorbei", "Fahrweise"), fill=ORANGE, size=30),
    pfeil_ink(1475, 205, 1615, 205, beim("vorbei", "Aber")),
    pl("Stoß", 1640, 170, beim("vorbei", "Aber"), fill=ORANGE, size=30),
    pl("vorbei", 1320, 250, beim("vorbei", "Aber"), fill=WEISS, size=28),
    peep_voll("NE_ruhig_r", 1400, BR, FR - 40, "rw", bis="vorbei"),
    peep_voll("HO_steht", 1730, BR, FR - 40, "rw", bis="vorbei"),
    peep_voll("HO_trinkt", 1730, BR, FR - 40, "vorbei", anim="cut"),
    ficon("tabler", "bottle", 1670, 650, 60, "vorbei", fuell=BLAU),
    peep_voll("NE_denkt_r", 1400, BR, FR - 40, "vorbei", anim="cut", bis="rw_erg"),
    peep_voll("NE_ertappt_r", 1400, BR, FR - 40, "rw_erg", anim="cut"),
    pl("Nele", 1400, BR + 22, "rw", fill=ORANGE, size=28, anker="m"),
    pl("Holger", 1730, BR + 22, "rw", fill=BLAU, size=28, anker="m"),
])

# K III. Schuld --------------------------------------------------------------------------------------------------------------
PS_ = f"{PA} › III. Schuld"
folie([("schuld", PS_), ("faehig", f"{PS_} › Schuldfähigkeit, §§ 19, 20 StGB"), ("entsch", f"{PS_} › Entschuldigungsgründe"),
       ("p17", f"{PS_} › Unrechtsbewusstsein, § 17 StGB"), ("schuld_erg", f"{PA} › III. schuldhaft")], [
    *tafel("schuld", "III. Schuld"),
    z("1. Schuldfähigkeit", 110, 195, "faehig", "ExtraBold", 36),
    z("§ 19: noch nicht vierzehn", 150, 248, beim("faehig", "wer"), size=34, farbe=TEXT),
    z("§ 20: etwa krankhafte seelische Störung,", 150, 298, "p20", size=34, farbe=TEXT),
    z("unfähig, Unrecht einzusehen oder danach", 150, 346, beim("p20", "unfähig"), size=34, farbe=TEXT),
    z("zu handeln", 150, 394, beim("p20", "unfähig"), size=34, farbe=TEXT),
    ok(165, 470, "klar", gr=20), z("Nele: erwachsen, klarer Verstand", 205, 445, "klar", "Bold", 34),
    z("2. Entschuldigungsgrund, z. B. § 35: liegt nicht vor", 110, 530, "entsch", "Bold", 32),
    z("3. Verbotsirrtum, § 17: spricht nichts dafür", 110, 595, "p17", "Bold", 32),
    fl_block(110, 690, 1040, 120, LILA, "schuld_erg", [("Nele handelte schuldhaft", "ExtraBold", 40, INK)]),
    peep_voll("NE_denkt", FX, BR, FR, "schuld", bis="klar"),
    pl("Nele", FX, BR + 22, "schuld", fill=ORANGE, size=30, anker="m", d=0.2),
    ficon("tabler", "mood-kid", FX, 330, 110, beim("faehig", "wer"), fuell=GELB, bis="p20"),
    pl("unter 14", FX, 350, beim("faehig", "vierzehn"), fill=GELB, size=30, anker="m", bis="p20"),
    ficon("tabler", "brain", FX, 330, 110, "p20", fuell=LILA, bis="klar"),
    pl("Einsicht, Steuerung", FX, 350, beim("p20", "unfähig"), fill=LILA, size=28, anker="m", bis="klar"),
    peep_voll("NE_ruhig", FX, BR, FR, "klar", anim="cut", bis="schuld_erg"),
    pl("erwachsen", FX, 300, "klar", fill=WEISS, size=30, anker="m", bis="schuld_erg"),
    peep_voll("NE_ertappt", FX, BR, FR, "schuld_erg", anim="cut"),
])

# L Ergebnis, Strafantrag ---------------------------------------------------------------------------------------------------
folie([("ergebnis", "Ergebnis"), ("antrag", "Ergebnis › Strafantrag, § 230 StGB")], [
    *tafel("ergebnis", "Ergebnis"),
    fl_block(110, 200, 1040, 150, GRUEN, ("ergebnis", 0.3), [("Nele ist strafbar wegen", "ExtraBold", 40, INK),
                                                           ("Körperverletzung, § 223 I StGB", "Regular", 36, INK)]),
    z("§ 230 I StGB: Verfolgung grundsätzlich", 110, 430, "antrag", "Bold", 36),
    z("nur auf Antrag", 110, 480, beim("antrag", "nur"), "Bold", 36),
    z("(außer bei besonderem öffentlichen Interesse)", 110, 540, beim("antrag", "Antrag"), size=30, farbe=TEXT),
    peep_voll("NE_ertappt_r", 1400, BR, FR - 40, "ergebnis"),
    peep_voll("HO_steht", 1730, BR, FR - 40, "ergebnis"),
    pl("Nele", 1400, BR + 22, "ergebnis", fill=ORANGE, size=28, anker="m"),
    pl("Holger", 1730, BR + 22, "ergebnis", fill=BLAU, size=28, anker="m"),
    ficon("tabler", "file-text", 1730, 330, 100, beim("antrag", "Antrag"), fuell=WEISS),
    pl("Strafantrag?", 1730, 350, beim("antrag", "Antrag"), fill=GELB, size=30, anker="m"),
])

# M Gegenfall: Szene ---------------------------------------------------------------------------------------------------------
NG, HG = 760, 1150
folie([("gegen", "Gegenfall · Holger will Nele anfahren")], [
    *uferweg("gegen", baeume=((130, 150),)),
    *wellen("gegen", (420, 1500)),
    pl("Gegenfall", 70, 40, "gegen", fill=GELB, size=48),
    peep_voll("NE_laeuft_r", NG, BODEN, FH, "gegen", bis=beim("gegen", "absichtlich")),
    peep_voll("NE_angst_r", NG, BODEN, FH, beim("gegen", "absichtlich"), anim="cut"),
    pl("Nele", NG, BODEN + 22, "gegen", fill=ORANGE, size=30, anker="m"),
    szene(bewegt(peep_voll("HO_rad_wut", HG, BODEN, RAD_H, beim("gegen", "Holger"), anim="cut", bis=beim("gegen", "stößt")),
                 beim("gegen", "Holger"), beim("gegen", "Sie"), 400), "011rad*", 1.0),
    pl("absichtlich auf Nele zu", 1250, 200, beim("gegen", "absichtlich"), fill=ROT, size=32, anker="m",
       bis=beim("gegen", "stößt")),
    pl("Holger", HG, BODEN + 22, beim("gegen", "Holger"), fill=BLAU, size=30, anker="m"),
    szene(liegend(ficon("ph", "bicycle", 0, 0, 250, beim("gegen", "stößt"), fuell=WEISS, anim="cut"), 180, HG + 220, BODEN - 2),
          "011sturz*", 0.7, 0.15),
    peep_voll("HO_boden", HG, BODEN, BODEN_H, beim("gegen", "stößt"), anim="cut"),
    pl("Stoß vom Rad", 960, 330, beim("gegen", "stößt"), fill=ORANGE, size=30, anker="m"),
])

# N Gegenfall: Prüfung ------------------------------------------------------------------------------------------------------
PG = "Gegenfall › II. Rechtswidrigkeit › Notwehr, § 32 StGB"
SX = 1575
folie([("gegen2", PG), ("gegen3", "Gegenfall › gerechtfertigt"), ("ende", "Gegenfall › Prüfung endet bei II.")], [
    *tafel("gegen2", "Gegenfall: Notwehr, § 32 StGB", size=46),
    ok(165, 225, "gegen2", gr=20), z("Angriff gegenwärtig und rechtswidrig", 205, 200, "gegen2", "Bold", 34),
    ok(165, 290, beim("gegen2", "Der"), gr=20), z("Stoß wehrt sofort ab", 205, 265, beim("gegen2", "Der"), "Bold", 34),
    z("kein milderes, ebenso sicheres Mittel", 205, 315, beim("gegen2", "milderes"), size=32, farbe=TEXT),
    ok(165, 390, beim("gegen2", "Ausweichen"), gr=20),
    z("Ausweichen muss sie nicht", 205, 365, beim("gegen2", "Ausweichen"), "Bold", 34),
    ok(165, 450, beim("gegen2", "will"), gr=20), z("will sich schützen", 205, 425, beim("gegen2", "will"), "Bold", 34),
    z("Tatbestand bleibt erfüllt", 110, 530, "gegen3", size=34, farbe=TEXT),
    fl_block(110, 590, 1040, 110, GRUEN, beim("gegen3", "gerechtfertigt"), [("durch Notwehr gerechtfertigt", "ExtraBold", 40, INK)]),
    z("Die Prüfung endet schon bei II.", 110, 750, "ende", "ExtraBold", 38),
    # rechts: Stufenleiter
    pl("I. Tatbestand", SX, 160, "gegen3", fill=GELB, size=32, anker="m"),
    haken_i(SX + 175, 192, beim("gegen3", "erfüllt"), gr=26),
    pl("II. Rechtswidrigkeit", SX, 250, "gegen3", fill=BLAU, size=32, anker="m"),
    kreuz_i(SX + 225, 282, beim("gegen3", "gerechtfertigt"), gr=26),
    pl("III. Schuld", SX, 340, beim("ende", "endet"), fill=GRAU, size=32, anker="m"),
    pl("nicht mehr geprüft", SX, 420, beim("ende", "Rechtswidrigkeit"), fill=WEISS, size=28, anker="m"),
    peep_voll("NE_angst", SX, BR, FR - 60, "gegen2", bis="gegen3"),
    peep_voll("NE_froh", SX, BR, FR - 60, "gegen3", anim="cut"),
    pl("Nele", SX, BR + 22, "gegen2", fill=ORANGE, size=30, anker="m"),
])

# O Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Schwerpunkt setzen"), ("tipp2", "Klausurtipp · Unproblematisches kurz")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Ausführlich nur, wo der Fall", 200, 200, beim("tipp", "Schreib"), "Bold", 36),
    z("ein Problem hat", 200, 252, beim("tipp", "Problem"), "Bold", 36),
    z("hier: Gegenwärtigkeit des Angriffs", 215, 320, beim("tipp", "hier"), size=34, farbe=TEXT),
    z("Sachverhalt gibt zur Schuld nichts her?", 200, 430, "tipp2", "Bold", 36),
    z("Ein Satz genügt:", 215, 490, beim("tipp2", "genügt"), size=34, farbe=TEXT),
    z("„Nele handelte schuldhaft.“", 215, 550, beim("tipp2", "Nele"), "Bold", 36),
    *redet("LX_warnt", 1560, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", 1560, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# P Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: vorsätzliches vollendetes Begehungsdelikt", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 200, "k1", "ExtraBold", 40, rechts=1820),
    z("1. objektiv: Tathandlung, Erfolg, Kausalität, objektive Zurechnung", K2, 262, "k1a", size=36, farbe=TEXT, rechts=1820),
    z("2. subjektiv: Vorsatz (§§ 15, 16 StGB)", K2, 316, "k1b", size=36, farbe=TEXT, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 410, "k2", "ExtraBold", 40, rechts=1820),
    z("Rechtfertigungsgründe, z. B. Notwehr (§ 32 StGB)", K2, 472, beim("k2", "Rechtfertigungsgründe"), size=36, farbe=TEXT,
      rechts=1820),
    z("III. Schuld", K1, 566, "k3", "ExtraBold", 40, rechts=1820),
    z("Schuldfähigkeit (§§ 19, 20), Entschuldigungsgründe (z. B. § 35),", K2, 628, beim("k3", "Schuldfähigkeit"), size=36,
      farbe=TEXT, rechts=1820),
    z("Unrechtsbewusstsein (§ 17 StGB)", K2, 682, beim("k3", "Unrechtsbewusstsein"), size=36, farbe=TEXT, rechts=1820),
    z("Danach ggf.: Strafantrag (z. B. § 230 StGB)", K1, 780, "k4", "Bold", 36, rechts=1820),
])

# Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Tatbestand:", "a"), (" Passt die Tat unter das Gesetz?", 0)]], 750, 320, 44, "merke",
                {"a": beim("merke", "Tatbestand")}),
    *markertext([[("Rechtswidrigkeit:", "b"), (" Ausnahmsweise erlaubt?", 0)]], 750, 430, 44, "m2",
                {"b": beim("m2", "Rechtswidrigkeit")}),
    *markertext([[("Schuld:", "c"), (" Dem Täter vorwerfbar?", 0)]], 750, 540, 44, "m3", {"c": beim("m3", "Schuld")}),
    *markertext([[("Scheitert eine Stufe,", "d")], [("endet die Prüfung.", 0)]], 750, 680, 46, "m4",
                {"d": beim("m4", "Scheitert")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
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
