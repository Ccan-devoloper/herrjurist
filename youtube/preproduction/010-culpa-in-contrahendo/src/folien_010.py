"""Folge 010 · Haftung ohne Vertrag? Culpa in contrahendo und der Linoleumrollen-Fall – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Teppichabteilung, B Forderung, C Sachverhalt, D Vorfrage Delikt,
E Linoleumrollen-Fall 1911, F Reichsgericht/Kodifikation, G I. Schuldverhältnis, H II. Pflichtverletzung,
I III. Vertretenmüssen, J IV. Schaden/Ergebnis, K Gegenfrage Tochter, L Fallgruppen, M Klausurtipp (Lexi),
N Klausurschema, O Merksatz (Lexi). Fiktiver Fall, Namen erfunden; der historische Fall ohne Figuren (nur Requisiten).
Geräusch nur bei sichtbarer Handlung (umkippende Rollen)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import El

bausteine.FIGORDNER = "op_010/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = bausteine.BG_FARBE
PFAD_FARBE = bausteine.PFAD_FARBE
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
BRAUN = (205, 160, 110, 255)           # Teppichrollen
DAUER = bausteine._cj()["dauer"]


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


def rolle(cx, unten, hoehe, cue, liegend=False, d=0.0, bis=None, anim="pop"):
    """Teppichrolle: Tabler-Icon 'cylinder' (MIT), braun gefüllt; liegend = um 90° gedreht (umgekippt)."""
    e = ficon("tabler", "cylinder", cx, unten, int(hoehe * 0.8), cue, fuell=BRAUN, d=d, bis=bis, anim=anim)
    if liegend:
        sp = e.sprite.rotate(90, expand=True, resample=Image.BICUBIC)
        e = El(sp, cx - sp.width / 2, unten - sp.height, cue, anim, d, bis, name="ficon:cylinder-liegend")
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


BODEN, FH = 880, 430
FX, BR, FR = 1560, 930, 520            # eine Figur rechts neben der Tafel
JX, KX = 1400, 1720                     # zwei Figuren rechts neben der Tafel (Jannik, Kessler)
F2 = 470                                # Figurenhöhe bei zwei Figuren

# A Fall: in der Teppichabteilung --------------------------------------------------------------------------------------
HSH = 303                               # kniende Ansicht im selben Maßstab (Kopfbreite gemessen)
JAX, HAX = 520, 1520                    # Jannik links (blickt nach rechts), Frau Hartmann rechts (blickt nach links)
HA = ("HA_redet", HAX, BODEN, FH)
JA = ("JA_redet_r", JAX, BODEN, FH)
folie([(("laden", -0.38), "Fall · In der Teppichabteilung")], [            # Prüfpfad ab 0,0 s voll sichtbar
    pille("Einrichtungshaus · Bodenbeläge", 70, 40, "laden", fill=GELB, size=44),
    linienzug([(40, BODEN), (1880, BODEN)], "laden", breite=7, farbe=INK),
    ficon("tabler", "sofa", 170, BODEN - 2, 200, "laden", fuell=BLAU, d=0.2),
    ficon("tabler", "lamp", 330, BODEN - 2, 90, "laden", fuell=GELB, d=0.3),
    # Rollenlager neben Jannik: drei stehende Rollen, zwei davon werden beiseitegestellt und kippen
    rolle(740, BODEN - 2, 280, "laden", d=0.4),
    rolle(880, BODEN - 2, 280, "laden", d=0.5, bis="rollen"),
    rolle(1020, BODEN - 2, 280, "laden", d=0.6, bis="rollen"),
    rolle(1110, BODEN - 2, 280, "rollen", anim="cut", bis="kippen"),
    rolle(1260, BODEN - 2, 280, "rollen", anim="cut", bis="kippen"),
    pille("ungesichert beiseite", 1200, 420, beim("rollen", "ohne"), fill=ORANGE, size=32, anker="m", bis="kippen"),
    szene(rolle(1180, BODEN - 2, 300, "kippen", liegend=True, anim="cut"), "010rollen*", 1.0),
    rolle(1250, BODEN - 70, 300, "kippen", liegend=True, anim="cut"),
    pille("zu Boden gerissen", 1230, 560, beim("kippen", "reißen"), fill=ROT, size=32, anker="m", bis="fordert"),
    # Muster
    ficon("tabler", "color-swatch", 1220, 520, 110, "muster", fuell=LILA, bis="rollen"),
    pille("Muster", 1220, 540, beim("muster", "Muster"), fill=LILA, size=30, anker="m", bis="rollen"),
    # Jannik
    peep_voll("JA_freundlich_r", JAX, BODEN, FH, "laden", d=0.3, bis="kippen"),
    peep_voll("JA_schreck_r", JAX, BODEN, FH, "kippen", anim="cut", bis="j1"),
    *redet("JA_redet_r", JAX, BODEN, FH, "j1", "arm"),
    peep_voll("JA_muede_r", JAX, BODEN, FH, "arm", anim="cut"),
    pille("Verkäufer Jannik", JAX, BODEN + 22, beim("muster", "Verkäufer"), fill=GRUEN, size=30, anker="m"),
    # Frau Hartmann
    peep_voll("HA_ruhig", HAX, BODEN, FH, "kundin", bis="h1"),
    *redet("HA_redet", HAX, BODEN, FH, "h1", "rollen"),
    peep_voll("HA_freut", HAX, BODEN, FH, "rollen", anim="cut", bis="kippen"),
    peep_voll("HS_angst", HAX, BODEN, HSH, "kippen", anim="cut", bis="arm"),       # am Boden (kniend)
    peep_voll("HS_schmerz", HAX, BODEN, HSH, "arm", anim="cut"),
    pille("Frau Hartmann", HAX, BODEN + 22, "kundin", fill=LILA, size=30, anker="m"),
    blase("sprech", 560, 200, "h1", 1180, 230, inhalt=["Den hier nehme ich. Können", "Sie mir die Rolle zeigen?"],
          textsize=31, figur=HA, bis="rollen"),
    blase("sprech", 480, 170, "j1", 820, 250, inhalt=["Oh nein! Haben Sie", "sich verletzt?"], textsize=34,
          figur=JA, bis="arm"),
    # Folgen
    ficon("tabler", "bandage", HAX, 330, 100, "arm", fuell=WEISS),
    pille("Handgelenk gebrochen", HAX, 350, beim("arm", "Handgelenk"), fill=ROT, size=30, anker="m"),
    ficon("tabler", "shopping-cart-off", 1000, 300, 110, "nichts", fuell=WEISS),
    pille("kein Kauf", 1000, 320, beim("nichts", "nichts"), fill=GRAU, size=32, anker="m"),
])

# B Fall: die Forderung --------------------------------------------------------------------------------------------------
KEX, HBX = 470, 1430
KE = ("KE_redet_r", KEX, BODEN, FH)
folie([("fordert", "Fall · Forderung"), ("frage", "Fall · Rechtsfrage")], [
    linienzug([(40, BODEN), (1880, BODEN)], "fordert", breite=7, farbe=INK),
    pille("Inhaber Kessler", KEX, BODEN + 22, beim("fordert", "Inhaber"), fill=BLAU, size=30, anker="m"),
    peep_voll("KE_ruhig_r", KEX, BODEN, FH, beim("fordert", "Inhaber"), bis="k1"),
    *redet("KE_redet_r", KEX, BODEN, FH, "k1", "frage"),
    peep_voll("KE_abwehr_r", KEX, BODEN, FH, "frage", anim="cut"),
    peep_voll("HA_fordert", HBX, BODEN, FH, "fordert", bis="k1"),
    peep_voll("HA_ernst", HBX, BODEN, FH, "k1", anim="cut"),
    pille("Frau Hartmann", HBX, BODEN + 22, "fordert", fill=LILA, size=30, anker="m"),
    ficon("tabler", "bandage", HBX + 150, 600, 80, "fordert", fuell=WEISS),
    ficon("tabler", "coin-euro", 960, 420, 110, beim("fordert", "Heilungskosten"), fuell=GELB, bis="k1"),
    pille("Heilungskosten", 960, 440, beim("fordert", "Heilungskosten"), fill=GELB, size=32, anker="m", bis="k1"),
    pille("Schmerzensgeld", 960, 520, beim("fordert", "Schmerzensgeld"), fill=PINK, size=32, anker="m", bis="k1"),
    blase("sprech", 620, 250, "k1", 900, 240, inhalt=["Einen Vertrag hatten wir nie.", "Und Jannik habe ich sorgfältig",
                                                     "ausgewählt und angeleitet."], textsize=30, figur=KE, bis="frage"),
    ficon("tabler", "file-off", 960, 560, 100, beim("k1", "Vertrag"), fuell=WEISS, bis="frage"),
    ficon("tabler", "user-check", 960, 690, 100, beim("k1", "sorgfältig"), fuell=GRUEN, bis="frage"),
    pille("Haftung ohne Vertrag?", 960, 975, "frage", fill=PINK, size=40, anker="m"),
    ficon("tabler", "file-off", 960, 560, 130, "frage", fuell=WEISS),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Hartmann möchte im Einrichtungshaus des Einzelkaufmanns Kessler einen Teppichboden kaufen und wählt bei "
    "Verkäufer Jannik ein Muster aus. Um ihr die Rolle zu zeigen, stellt Jannik zwei schwere Teppichrollen beiseite, "
    "ohne sie zu sichern. Die Rollen kippen um und reißen Frau Hartmann zu Boden; ihr Handgelenk ist gebrochen. "
    "Ein Kauf kommt nicht zustande.",
    "Sie verlangt von Kessler Ersatz der Heilungskosten und Schmerzensgeld. Kessler meint, ohne Vertrag hafte er "
    "nicht; Jannik habe er sorgfältig ausgewählt und angeleitet.",
    "(Fall erfunden, nachgebildet RG, Urt. v. 7.12.1911 – VI 240/11 = RGZ 78, 239, Linoleumrollen-Fall.)",
], "Kann Frau Hartmann von Kessler Schadensersatz verlangen?")

# D Vorfrage: Delikt -----------------------------------------------------------------------------------------------------
folie([("delikt", "Vorfrage · Delikt"), ("p823", "Vorfrage · Delikt › § 823 I BGB: Jannik"),
       ("p831", "Vorfrage · Delikt › § 831 BGB: Kessler"), ("exkul", "Vorfrage · Delikt › § 831 I 2: Entlastung")], [
    *tafel("delikt", "Reicht das Deliktsrecht?"),
    ok(135, 225, "p823", gr=22), z("§ 823 I BGB: Jannik haftet", 175, 200, "p823", "Bold", 36),
    z("fahrlässig ihren Körper verletzt", 215, 255, beim("p823", "fahrlässig"), size=34, farbe=TEXT),
    z("§ 831 I 1 BGB: Kessler haftet für", 175, 345, "p831", "Bold", 36),
    z("seinen Verrichtungsgehilfen", 215, 400, beim("p831", "Verrichtungsgehilfen"), size=34),
    nein(135, 505, "exkul", gr=22), z("§ 831 I 2: Entlastung möglich", 175, 485, "exkul", "Bold", 36),
    z("sorgfältig ausgewählt und angeleitet", 215, 540, beim("exkul", "sorgfältig"), size=34, farbe=TEXT),
    fl_block(110, 640, 1040, 110, ROT, "luecke", [("Frau Hartmann bliebe nur Jannik", "ExtraBold", 40, INK)]),
    peep_voll("JA_ernst", JX, BODEN, F2, "delikt", bis="luecke"),
    peep_voll("JA_muede", JX, BODEN, F2, "luecke", anim="cut"),
    pille("Jannik", JX, BODEN + 22, "delikt", fill=GRUEN, size=30, anker="m"),
    peep_voll("KE_ruhig", KX, BODEN, F2, "delikt", d=0.2, bis="exkul"),
    peep_voll("KE_abwehr", KX, BODEN, F2, "exkul", anim="cut"),
    pille("Kessler", KX, BODEN + 22, "delikt", fill=BLAU, size=30, anker="m", d=0.2),
    pille("§ 823 I", JX, 260, "p823", fill=GELB, size=30, anker="m"),
    pille("§ 831", KX, 260, "p831", fill=GELB, size=30, anker="m", bis="exkul"),
    ficon("tabler", "user-check", KX, 250, 90, "exkul", fuell=GRUEN),
    pille("Entlastung", KX, 270, beim("exkul", "entlasten"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "wallet-off", JX, 190, 70, "luecke", fuell=WEISS),
])

# E Der Linoleumrollen-Fall (RG 1911): ohne Figuren, nur Requisiten ------------------------------------------------------
folie([("rg", "Leitentscheidung · Linoleumrollen-Fall (RGZ 78, 239)")], [
    pille("Der Linoleumrollen-Fall · Reichsgericht 1911", 70, 40, "rg", fill=GELB, size=44),
    linienzug([(40, BODEN), (1880, BODEN)], "rg", breite=7, farbe=INK),
    ficon("fluent-emoji-high-contrast", "department-store", 360, BODEN - 2, 360, "rg", fuell=WEISS, d=0.2),
    pille("Warenhaus", 360, BODEN + 22, beim("rg", "Warenhaus"), fill=WEISS, size=30, anker="m"),
    rolle(860, BODEN - 2, 300, "rg", d=0.4, bis=beim("rg", "fallen")),
    rolle(960, BODEN - 2, 300, "rg", d=0.5, bis=beim("rg", "fallen")),
    szene(rolle(1000, BODEN - 2, 300, beim("rg", "fallen"), liegend=True, anim="cut"), "010rollen*", 0.8),
    rolle(1060, BODEN - 70, 300, beim("rg", "fallen"), liegend=True, anim="cut"),
    pille("zwei Linoleumrollen", 1030, 560, beim("rg", "Linoleumrollen"), fill=ORANGE, size=32, anker="m"),
    ficon("fluent-emoji-high-contrast", "woman", 1480, BODEN - 2, 160, beim("rg", "Kundin"), fuell=LILA),
    ficon("fluent-emoji-high-contrast", "child", 1640, BODEN - 2, 110, beim("rg", "Kind"), fuell=GELB),
    pille("Kundin und Kind", 1560, BODEN + 22, beim("rg", "Kundin"), fill=LILA, size=30, anker="m"),
    ficon("tabler", "shopping-cart-off", 1560, 400, 110, "rg2", fuell=WEISS),
    pille("kein Kauf", 1560, 420, "rg2", fill=GRAU, size=32, anker="m"),
])

# F Reichsgericht und Kodifikation ---------------------------------------------------------------------------------------
folie([("rg3", "Leitentscheidung · Linoleumrollen-Fall (RGZ 78, 239) › vertragsähnlich"),
       ("rg6", "Leitentscheidung · Linoleumrollen-Fall (RGZ 78, 239) › § 278 statt § 831 BGB"), ("kodif", "Heute · § 311 II BGB (seit 2002)")], [
    *tafel("rg3", "Reichsgericht, RGZ 78, 239"),
    z("Bitte um Vorlegen + Vorlegen der Ware", 110, 200, "rg3", "Bold", 36),
    z("→ bereitet einen Kauf vor", 150, 255, beim("rg3", "bereiten"), size=34),
    z("vertragsähnliches Rechtsverhältnis", 110, 330, "rg4", "Bold", 36),
    z("Pflicht: Sorgfalt für Gesundheit und Eigentum", 150, 385, "rg5", size=32),
    z("Angestellter erfüllt diese Pflicht: § 278 BGB", 110, 460, "rg6", "Bold", 34),
    z("sonst Verweis an den meist mittellosen", 150, 515, "mittellos", size=32, farbe=TEXT),
    z("Angestellten (nur § 831 BGB)", 150, 560, beim("mittellos", "Angestellten"), size=32, farbe=TEXT),
    fl_block(110, 635, 1040, 95, GELB, "cic", [("Klassiker der culpa in contrahendo", "ExtraBold", 38, INK)]),
    fl_block(110, 750, 1040, 95, GRUEN, "kodif", [("seit 2002 im Gesetz: § 311 II BGB", "ExtraBold", 38, INK)]),
    ficon("fluent-emoji-high-contrast", "classical-building", FX, 330, 220, "rg3", fuell=WEISS),
    pille("Reichsgericht 1911", FX, 350, "rg3", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "first-aid-kit", FX - 120, 600, 120, "rg5", fuell=ROT, bis="kodif"),
    pille("Gesundheit", FX - 120, 620, "rg5", fill=ROT, size=28, anker="m", bis="kodif"),
    ficon("tabler", "sofa", FX + 120, 600, 140, beim("rg5", "Eigentum"), fuell=BLAU, bis="kodif"),
    pille("Eigentum", FX + 120, 620, beim("rg5", "Eigentum"), fill=BLAU, size=28, anker="m", bis="kodif"),
    ficon("tabler", "link", FX, 840, 110, "rg6", fuell=GELB, bis="kodif"),
    pille("§ 278 BGB", FX, 860, "rg6", fill=GELB, size=30, anker="m", bis="kodif"),
    ficon("tabler", "book", FX, 760, 160, "kodif", fuell=GRUEN),
    pille("§ 311 II BGB", FX, 780, "kodif", fill=GRUEN, size=32, anker="m"),
])

# G I. Schuldverhältnis ------------------------------------------------------------------------------------------------------
folie([("a", "A. Hartmann gegen Kessler › §§ 280 I, 311 II, 241 II BGB"),
       ("sch1", "A. Hartmann gegen Kessler › I. Schuldverhältnis"),
       ("anb", "A. Hartmann gegen Kessler › I. Schuldverhältnis › § 311 II Nr. 2: Anbahnung")], [
    *tafel("a", "A. Hartmann gegen Kessler"),
    z("§§ 280 I, 311 II, 241 II BGB", 110, 195, beim("a", "culpa"), "Bold", 38),
    z("I. Schuldverhältnis", 110, 280, "sch1", "Bold", 38),
    nein(135, 360, beim("sch1", "Kaufvertrag"), gr=22), z("Kaufvertrag", 175, 340, beim("sch1", "Kaufvertrag"), size=36),
    z("§ 311 II BGB genügt schon:", 150, 420, "nr", "Bold", 36),
    z("Nr. 1 Vertragsverhandlungen", 190, 475, beim("nr", "Vertragsverhandlungen"), size=34),
    z("Nr. 2 Anbahnung eines Vertrags", 190, 525, beim("nr", "Anbahnung"), size=34),
    z("Nr. 3 ähnliche geschäftliche Kontakte", 190, 575, beim("nr", "ähnliche"), size=34),
    ok(160, 545, "anb", gr=20),
    z("kommt, um zu kaufen", 190, 645, beim("anb", "Frau"), "Bold", 34),
    z("→ Einwirkung auf ihre Gesundheit möglich", 190, 695, beim("anb", "Möglichkeit"), size=34),
    pille("Gesetzesbegründung: „Linoleumrollenfall“", 110, 770, "begr", fill=GELB, size=30),
    peep_voll("HA_ernst", FX, BR, FR, "a", bis="anb"),
    peep_voll("HA_ruhig", FX, BR, FR, "anb", anim="cut"),
    ficon("tabler", "file-off", FX, 320, 120, beim("sch1", "Kaufvertrag"), fuell=WEISS, bis="anb"),
    ficon("tabler", "shopping-cart", FX, 320, 130, beim("anb", "Frau"), fuell=GELB),
    pille("kommt, um zu kaufen", FX, 340, beim("anb", "Frau"), fill=GELB, size=28, anker="m"),
])

# H II. Pflichtverletzung --------------------------------------------------------------------------------------------------
folie([("pfl", "A. Hartmann gegen Kessler › II. Pflichtverletzung, § 241 II")], [
    *tafel("pfl", "II. Pflichtverletzung"),
    z("§ 241 II BGB: Rücksicht auf die", 110, 200, beim("pfl", "Paragraf"), "Bold", 36),
    z("Rechtsgüter des anderen Teils", 150, 255, beim("pfl", "Rechtsgüter"), size=34),
    ok(135, 355, "pfl2", gr=22), z("schwere Rollen ungesichert abgestellt", 175, 335, "pfl2", size=34),
    z("Pflicht trifft Kessler", 175, 425, "pfl3", "Bold", 34),
    z("verletzt durch Jannik", 215, 480, beim("pfl3", "Jannik"), size=34),
    fl_block(110, 580, 1040, 110, GRUEN, beim("pfl3", "verletzt"), [("Pflichtverletzung (+)", "ExtraBold", 42, INK)]),
    rolle(JX, 300, 260, "pfl2", liegend=True),
    pille("ungesichert", JX, 320, "pfl2", fill=ORANGE, size=28, anker="m"),
    peep_voll("JA_ernst", JX, BODEN, F2, "pfl", bis="pfl3"),
    peep_voll("JA_muede", JX, BODEN, F2, "pfl3", anim="cut"),
    pille("Jannik", JX, BODEN + 22, "pfl", fill=GRUEN, size=30, anker="m"),
    peep_voll("KE_ruhig", KX, BODEN, F2, "pfl", d=0.2, bis="pfl3"),
    peep_voll("KE_ertappt", KX, BODEN, F2, "pfl3", anim="cut"),
    pille("Kessler", KX, BODEN + 22, "pfl", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Pflicht", KX, 350, "pfl3", fill=GELB, size=28, anker="m"),
])

# I III. Vertretenmüssen ---------------------------------------------------------------------------------------------------
folie([("vm", "A. Hartmann gegen Kessler › III. Vertretenmüssen"),
       ("p278", "A. Hartmann gegen Kessler › III. Vertretenmüssen › § 278 BGB: Erfüllungsgehilfe")], [
    *tafel("vm", "III. Vertretenmüssen"),
    z("§ 280 I 2 BGB: wird vermutet", 110, 200, beim("vm", "Es"), "Bold", 36),
    z("§ 278 BGB: Verschulden des", 110, 285, "p278", "Bold", 36),
    z("Erfüllungsgehilfen wie eigenes", 150, 340, beim("p278", "Erfüllungsgehilfe"), size=34),
    ok(135, 435, "fahrl", gr=22), z("Jannik fahrlässig, § 276 II BGB", 175, 415, "fahrl", "Bold", 34),
    z("Rollen abstützen oder schräg", 215, 470, beim("fahrl", "abstützen"), size=32, farbe=TEXT),
    z("an die Wand lehnen", 215, 515, beim("fahrl", "schräg"), size=32, farbe=TEXT),
    nein(135, 610, "keine", gr=22), z("keine Entlastung wie bei § 831 BGB", 175, 590, "keine", "Bold", 34),
    fl_block(110, 690, 1040, 110, GRUEN, beim("keine", "nicht"), [("Vertretenmüssen (+)", "ExtraBold", 42, INK)]),
    peep_voll("JA_ernst", JX, BODEN, F2, "vm", bis="fahrl"),
    peep_voll("JA_muede", JX, BODEN, F2, "fahrl", anim="cut"),
    pille("Jannik", JX, BODEN + 22, "vm", fill=GRUEN, size=30, anker="m"),
    peep_voll("KE_denkt", KX, BODEN, F2, "vm", d=0.2, bis="keine"),
    peep_voll("KE_ertappt", KX, BODEN, F2, "keine", anim="cut"),
    pille("Kessler", KX, BODEN + 22, "vm", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Erfüllungsgehilfe", JX, 245, beim("p278", "Erfüllungsgehilfe"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "link", (JX + KX) // 2, 420, 90, "p278", fuell=GELB),
    pille("§ 278", (JX + KX) // 2, 440, "p278", fill=GELB, size=28, anker="m"),
    ficon("tabler", "hand-stop", KX, 280, 90, "keine", fuell=ROT),
    pille("keine Entlastung", KX, 300, "keine", fill=ROT, size=26, anker="m"),
])

# J IV. Schaden und Ergebnis -----------------------------------------------------------------------------------------------
folie([("schaden", "A. Hartmann gegen Kessler › IV. Schaden"),
       ("smg", "A. Hartmann gegen Kessler › IV. Schaden › Schmerzensgeld, § 253 II"), ("erg", "A. Hartmann gegen Kessler › Ergebnis")], [
    *tafel("schaden", "IV. Schaden"),
    ok(135, 225, beim("schaden", "Heilungskosten"), gr=22),
    z("Heilungskosten", 175, 200, beim("schaden", "Heilungskosten"), "Bold", 38),
    z("Körper verletzt:", 175, 280, beim("smg", "Körper"), size=34, farbe=TEXT),
    ok(135, 360, beim("smg", "Paragraf"), gr=22), z("Schmerzensgeld, § 253 II BGB", 175, 335, beim("smg", "Paragraf"), "Bold", 38),
    fl_block(110, 450, 1040, 150, GRUEN, "erg", [("Ergebnis: Kessler haftet,", "ExtraBold", 42, INK),
                                               ("obwohl es nie einen Vertrag gab", "Regular", 36, INK)]),
    peep_voll("HA_schmerz", FX, BR, FR, "schaden", bis="erg"),
    peep_voll("HA_zufrieden", FX, BR, FR, "erg", anim="cut"),
    ficon("tabler", "bandage", FX + 150, 560, 80, "schaden", fuell=WEISS),
    ficon("tabler", "first-aid-kit", FX - 150, 320, 110, beim("schaden", "Heilungskosten"), fuell=ROT),
    pille("Heilungskosten", FX - 150, 340, beim("schaden", "Heilungskosten"), fill=ROT, size=26, anker="m"),
    ficon("tabler", "coin-euro", FX + 160, 320, 110, beim("smg", "Schmerzensgeld"), fuell=GELB),
    pille("Schmerzensgeld", FX + 160, 340, beim("smg", "Schmerzensgeld"), fill=GELB, size=26, anker="m"),
])

# K Gegenfrage: die Tochter ------------------------------------------------------------------------------------------------
folie([("kind", "Gegenfrage · Die Tochter (Schutz Dritter)")], [
    *tafel("kind", "Und die Tochter?"),
    pille("hypothetisch", 110, 190, "kind", fill=GELB, size=30),
    z("Dritte, die einer Partei nahestehen:", 110, 300, "kind2", "Bold", 36),
    z("Grundsätze des Vertrags mit Schutzwirkung", 150, 355, beim("kind2", "Grundsätzen"), size=34),
    z("zugunsten Dritter", 150, 405, beim("kind2", "zugunsten"), size=34),
    ok(135, 505, "kind3", gr=22), z("auch schon vor Vertragsschluss", 175, 485, "kind3", "Bold", 34),
    z("BT-Drs. 14/6040, S. 163", 215, 540, beim("kind3", "Gesetzesbegründung"), size=30, farbe=TEXT),
    peep_voll("HA_ernst", 1460, BODEN, FH, "kind"),
    pille("Frau Hartmann", 1460, BODEN + 22, "kind", fill=LILA, size=30, anker="m"),
    ficon("fluent-emoji-high-contrast", "girl", 1720, BODEN - 2, 170, beim("kind", "Tochter"), fuell=GELB),
    pille("Tochter", 1720, BODEN + 22, beim("kind", "Tochter"), fill=GELB, size=30, anker="m"),
    pille("auch getroffen?", 1720, 640, beim("kind", "getroffen"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "shield-check", 1600, 330, 130, "kind2", fuell=GRUEN),
    pille("Schutzbereich", 1600, 350, "kind2", fill=GRUEN, size=28, anker="m"),
])

# L Fallgruppen -----------------------------------------------------------------------------------------------------------
GY = [205, 330, 455, 600]
folie([("gruppen", "Fallgruppen · culpa in contrahendo › Schutzpflichten"),
       (beim("g2", "Aufklärungspflichten"), "Fallgruppen · culpa in contrahendo › Aufklärungspflichten"),
       (beim("g3", "Abbruch"), "Fallgruppen · culpa in contrahendo › Abbruch der Verhandlungen"),
       (beim("g4", "Haftung"), "Fallgruppen · culpa in contrahendo › Haftung Dritter, § 311 III BGB")], [
    *tafel("gruppen", "Fallgruppen"),
    ficon("tabler", "shield-check", 140, GY[0] + 50, 60, beim("gruppen", "verletzte"), fuell=GRUEN),
    z("Schutzpflichten verletzt", 190, GY[0], beim("gruppen", "verletzte"), "Bold", 36),
    pille("unser Fall", 690, GY[0] - 12, beim("gruppen", "verletzte"), fill=GELB, size=28),
    ficon("tabler", "info-circle", 140, GY[1] + 50, 60, beim("g2", "Aufklärungspflichten"), fuell=BLAU),
    z("Aufklärungspflicht verletzt", 190, GY[1], beim("g2", "Aufklärungspflichten"), "Bold", 36),
    z("→ nachteiliger Vertrag", 230, GY[1] + 52, beim("g2", "nachteiligen"), size=32, farbe=TEXT),
    ficon("tabler", "door-exit", 140, GY[2] + 50, 60, "g3", fuell=ORANGE),
    z("Abbruch ohne triftigen Grund", 190, GY[2], beim("g3", "Abbruch"), "Bold", 36),
    z("wenn der Vertrag schon als sicher galt", 230, GY[2] + 52, beim("g3", "wenn"), size=32, farbe=TEXT),
    z("(BGH, 13.10.2017 – V ZR 11/17)", 230, GY[2] + 97, beim("g3", "wenn"), size=28, farbe=TEXT),
    ficon("tabler", "user-shield", 140, GY[3] + 50, 60, beim("g4", "Haftung"), fuell=LILA),
    z("Dritte, § 311 III BGB:", 190, GY[3], beim("g4", "Haftung"), "Bold", 36),
    z("besonderes Vertrauen in Anspruch genommen", 230, GY[3] + 52, beim("g4", "besonderes"), size=32, farbe=TEXT),
    rolle(FX, 420, 300, beim("gruppen", "Rolle"), liegend=True, bis=beim("g2", "Aufklärungspflichten")),
    pille("Schutzpflicht", FX, 440, beim("gruppen", "Schutzpflichten"), fill=GRUEN, size=32, anker="m", bis=beim("g2", "Aufklärungspflichten")),
    ficon("tabler", "info-circle", FX, 420, 200, beim("g2", "Aufklärungspflichten"), fuell=BLAU, bis=beim("g3", "Abbruch")),
    pille("Aufklärung", FX, 440, beim("g2", "Aufklärungspflichten"), fill=BLAU, size=32, anker="m", bis=beim("g3", "Abbruch")),
    ficon("tabler", "door-exit", FX, 420, 200, beim("g3", "Abbruch"), fuell=ORANGE, bis=beim("g4", "Haftung")),
    pille("Abbruch", FX, 440, beim("g3", "Abbruch"), fill=ORANGE, size=32, anker="m", bis=beim("g4", "Haftung")),
    ficon("tabler", "user-shield", FX, 420, 200, beim("g4", "Haftung"), fuell=LILA),
    pille("Vertrauen", FX, 440, beim("g4", "Vertrauen"), fill=LILA, size=32, anker="m"),
])

# M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · culpa in contrahendo vor dem Delikt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("culpa in contrahendo vor dem Delikt", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("als vertragsähnlichen Anspruch", 240, 255, beim("tipp", "vertragsähnlichen"), size=34, farbe=TEXT),
    ok(175, 365, beim("tipp1", "Erfüllungsgehilfen"), gr=22),
    z("Erfüllungsgehilfe, § 278:", 215, 345, beim("tipp1", "Erfüllungsgehilfen"), "Bold", 36),
    z("keine Entlastung", 255, 400, beim("tipp1", "keine"), size=34, farbe=TEXT),
    nein(175, 495, beim("tipp1", "Verrichtungsgehilfen"), gr=22),
    z("Verrichtungsgehilfe, § 831:", 215, 475, beim("tipp1", "Verrichtungsgehilfen"), "Bold", 36),
    z("Entlastung möglich", 255, 530, beim("tipp1", "schon"), size=34, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ----------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 200, 260
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: culpa in contrahendo", 110, 90, "sch", 54),
    z("A. Anspruch aus §§ 280 I, 311 II, 241 II BGB", K1, 190, "s1", "Bold", 40, rechts=1820),
    z("I. Vorvertragliches Schuldverhältnis, § 311 II (Nr. 1–3)", K2, 265, "s2", "Bold", 36, rechts=1820),
    z("II. Pflichtverletzung: Rücksichtspflicht, § 241 II", K2, 335, "s3", "Bold", 36, rechts=1820),
    z("III. Vertretenmüssen: vermutet, § 280 I 2", K2, 405, "s4", "Bold", 36, rechts=1820),
    z("Gehilfe: § 278 BGB, keine Entlastung", K3, 460, beim("s4", "Paragraf"), size=34, farbe=TEXT, rechts=1820),
    z("IV. Schaden, auch Schmerzensgeld (§ 253 II)", K2, 535, "s5", "Bold", 36, rechts=1820),
    z("B. Danach Delikt", K1, 625, "s6", "Bold", 40, rechts=1820),
    z("§ 831 BGB gegen den Inhaber: Entlastung möglich", K2, 690, beim("s6", "Paragraf"), size=34, rechts=1820),
    z("§ 823 I BGB gegen den Angestellten", K2, 745, "s7", size=34, rechts=1820),
])

# O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer einen Vertrag anbahnt,", 0)], [("schuldet schon ", 0), ("Rücksicht.", "a")]], 750, 320, 54, "merke",
                {"a": beim("merke", "Rücksicht")}),
    *markertext([[("Für Gehilfen haftet er wie für sich:", 0)], [("ohne Entlastung.", "b")]],
                750, 580, 48, "m2", {"b": beim("m2", "ohne")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
