"""Folge 007 · Haustyrannen-Fall (frei nach BGH, Urt. v. 25.3.2003 – 1 StR 483/02 = BGHSt 48, 255) – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Haus, B Nacht, C Vormittag, D Sachverhalt, E Heimtücke, F Rechtswidrigkeit,
G § 35 I Gefahr, H nicht anders abwendbar, I § 35 II Irrtum, J Strafe/Ergebnis, K Klausurtipp (Lexi), L Klausurschema,
M Merksatz (Lexi). Sensibles Thema: keine Waffe, kein Blut, kein Opfer im Moment der Tat; Gewalt nur benannt (Pillen).
Geräusche nur bei sichtbarer Handlung (Haustür, Rollkoffer)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_007/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE, nacht=None)          # Nacht = Verlauf, erzeugt im Renderer
PFAD_FARBE = dict(bausteine.PFAD_FARBE, nacht=(255, 255, 255, 170))
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
NACHTWAND = (78, 92, 150, 255)
LINIE = (225, 228, 240, 255)
DAUER = bausteine._cj()["dauer"]


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


BODEN, FH = 880, 430
RAX, NAX = 470, 1430                   # Ralf links (blickt nach rechts), Nadine rechts (blickt nach links)

# A Fall: das Haus (Tag) --------------------------------------------------------------------------------------------------
RA = ("RA_redet_r", RAX, BODEN, FH)
folie([(("haus", -0.8), "Fall · Das Haus")], [            # Prüfpfad ab 0,0 s voll sichtbar
    pille("Der Haustyrannen-Fall", 70, 40, "haus", fill=GELB, size=48),
    linienzug([(40, BODEN), (1880, BODEN)], "haus", breite=7, farbe=INK),
    ficon("tabler", "sofa", 950, BODEN - 2, 300, "haus", fuell=BLAU, d=0.2),
    ficon("tabler", "lamp", 1185, BODEN - 2, 110, "haus", fuell=GELB, d=0.3),
    ficon("fluent-emoji-high-contrast", "girl", 1680, 690, 105, "haus", fuell=GELB, d=0.5),
    ficon("fluent-emoji-high-contrast", "girl", 1800, 700, 95, "haus", fuell=GELB, d=0.6),
    pille("zwei Töchter", 1740, 715, "haus", fill=GELB, size=28, anker="m", d=0.7),
    # Ralf
    peep_voll("RA_kalt_r", RAX, BODEN, FH, "haus", bis="jahre"),
    peep_voll("RA_wuetend_r", RAX, BODEN, FH, "jahre", anim="cut", bis="r1"),
    *redet("RA_redet_r", RAX, BODEN, FH, "r1", "angst"),
    peep_voll("RA_kalt_r", RAX, BODEN, FH, "angst", anim="cut"),
    pille("Ralf", RAX, BODEN + 22, "haus", fill=WEISS, size=30, anker="m", d=0.2),
    # Nadine
    peep_voll("NA_ruhig", NAX, BODEN, FH, "haus", d=0.3, bis="jahre"),
    peep_voll("NA_traurig", NAX, BODEN, FH, "jahre", anim="cut", bis="steigt"),
    peep_voll("NA_angst", NAX, BODEN, FH, "steigt", anim="cut", bis="angst"),
    peep_voll("NA_muede", NAX, BODEN, FH, "angst", anim="cut"),
    pille("Nadine", NAX, BODEN + 22, "haus", fill=LILA, size=30, anker="m", d=0.4),
    # Jahre der Gewalt, nur benannt
    ficon("tabler", "calendar", 950, 300, 120, beim("jahre", "fünfzehn"), fuell=ROT, bis="r1"),
    pille("seit 15 Jahren Misshandlungen", 950, 330, beim("jahre", "misshandelt"), fill=ROT, size=36, anker="m", bis="r1"),
    ficon("tabler", "trending-up", 950, 520, 110, "steigt", fuell=ROT, bis="r1"),
    pille("immer schlimmer", 950, 540, beim("steigt", "schlimmer"), fill=ORANGE, size=34, anker="m", bis="r1"),
    pille("auch die Töchter", 1740, 790, beim("steigt", "Töchter"), fill=ROT, size=26, anker="m", bis="r1"),
    # Drohung
    blase("sprech", 600, 200, "r1", 930, 260, inhalt=["Wenn du gehst, finde ich dich.", "Überall."], textsize=34,
          figur=RA, bis="angst"),
    pille("glaubt ihm", NAX, 300, beim("angst", "glaubt"), fill=LILA, size=32, anker="m"),
    pille("als äußerst gewalttätig bekannt", 900, 330, beim("angst", "äußerst"), fill=ROT, size=34, anker="m"),
])

# B Fall: die Nacht -------------------------------------------------------------------------------------------------------
DX = 330
nachtfolie([("nacht", "Fall · Die Nacht")], [
    ficon("tabler", "moon-stars", 1720, 230, 120, "nacht", fuell=GELB, d=0.2),
    linienzug([(40, BODEN), (1880, BODEN)], "nacht", breite=7, farbe=LINIE),
    szene(ficon("tabler", "door", DX, BODEN - 2, 260, "nacht", fuell=NACHTWAND), "007tuer*", 0.8),
    pille("gegen 3:30 Uhr", 960, 160, beim("nacht", "halb"), fill=GELB, size=36, anker="m"),
    ficon("tabler", "clock-hour-3", 960, 140, 90, beim("nacht", "halb"), fuell=WEISS),
    # Ralf kommt herein (steht neben der Tür), Nadine wach
    peep_voll("RA_kalt_r", 640, BODEN, FH, beim("nacht", "kommt"), bis="streit"),
    peep_voll("RA_wuetend_r", 640, BODEN, FH, "streit", anim="cut", bis="schlaf"),
    peep_voll("NA_muede", NAX, BODEN, FH, "nacht", d=0.3, bis="streit"),
    peep_voll("NA_angst", NAX, BODEN, FH, "streit", anim="cut", bis="schlaf"),
    peep_voll("NA_traurig", NAX, BODEN, FH, "schlaf", anim="cut"),
    pille("beschimpft und schlägt sie", 1040, 330, beim("streit", "beschimpft"), fill=ROT, size=36, anker="m", bis="schlaf"),
    # Ralf legt sich schlafen: nur das Bett, er selbst ist nicht zu sehen
    ficon("tabler", "bed", 900, BODEN - 2, 380, "schlaf", fuell=BLAU),
    ficon("tabler", "zzz", 1090, 630, 90, beim("schlaf", "schlafen"), fuell=WEISS),
    pille("Ralf schläft", 880, 510, beim("schlaf", "schlafen"), fill=WEISS, size=34, anker="m"),
    pille("Nadine bleibt wach", NAX, 300, beim("schlaf", "schlafen"), fill=LILA, size=30, anker="m", d=0.6),
])

# C Fall: der Vormittag ----------------------------------------------------------------------------------------------------
TX = 820                                # Schlafzimmertür
folie([("morgen", "Fall · Der Vormittag"), ("frage", "Fall · Die Frage")], [
    ficon("tabler", "sun", 1760, 220, 120, "morgen", fuell=GELB, d=0.2),
    linienzug([(40, BODEN), (1880, BODEN)], "morgen", breite=7, farbe=INK),
    pille("am Vormittag", 70, 40, "morgen", fill=GELB, size=40),
    ficon("tabler", "archive", 330, BODEN - 2, 170, "morgen", fuell=GRAU, d=0.2),
    pille("Revolver gefunden", 330, 560, beim("morgen", "Revolver"), fill=ROT, size=32, anker="m"),
    ficon("tabler", "hourglass", 1120, 420, 90, "ringen", fuell=GELB, bis="tat"),
    pille("ringt lange mit sich", 1120, 440, beim("ringen", "ringt"), fill=LILA, size=32, anker="m", bis="tat"),
    # Tat: nur die geschlossene Schlafzimmertür, kein Opfer, keine Waffe
    ficon("tabler", "door", TX, BODEN - 2, 250, "tat", fuell=BLAU),
    pille("Schlafzimmer", TX, 520, beim("tat", "Schlafzimmer"), fill=WEISS, size=30, anker="m"),
    pille("Ralf ist tot", TX, 430, beim("tat", "schlafenden"), fill=GRAU, size=36, anker="m"),
    peep_voll("NA_muede", NAX, BODEN, FH, "morgen", bis="ringen"),
    peep_voll("NA_ernst", NAX, BODEN, FH, "ringen", anim="cut", bis="tat"),
    peep_voll("NA_zu", NAX, BODEN, FH, "tat", anim="cut", bis="n1"),
    *redet("NA_redet", NAX, BODEN, FH, "n1", "frage"),
    peep_voll("NA_traurig", NAX, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 460, 170, "n1", 1180, 250, inhalt=["Ich sah keinen", "anderen Ausweg."], textsize=36,
          figur=("NA_redet", NAX, BODEN, FH), bis="frage"),
    pille("Mord? Oder entschuldigt?", 960, 975, "frage", fill=PINK, size=38, anker="m"),
])

# D Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Ralf misshandelt seine Frau Nadine seit rund 15 Jahren, zuletzt immer heftiger; inzwischen schlägt er auch die beiden "
    "Töchter. Für den Fall einer Trennung droht er, Nadine überall zu finden und den Töchtern etwas anzutun. Nadine nimmt "
    "das ernst; Ralf ist als äußerst gewalttätig bekannt. Hilfe bei Polizei oder Frauenhaus sucht sie nicht.",
    "Eines Nachts kommt Ralf gegen 3:30 Uhr heim, beschimpft und schlägt Nadine und legt sich schlafen. Am Vormittag "
    "findet sie seinen Revolver. Nach langem Ringen erschießt sie gegen Mittag den schlafenden Ralf. Sie sah keinen "
    "anderen Ausweg.",
    "(Frei nach BGH, Urt. v. 25.3.2003 – 1 StR 483/02 = BGHSt 48, 255; vereinfacht, Namen erfunden.)",
], "Wie hat sich Nadine strafbar gemacht?")

# E Tatbestand: Heimtücke ------------------------------------------------------------------------------------------------
FX, BR, FR = 1560, 930, 520
folie([("a", "A. Nadine › §§ 212, 211 StGB"), ("tb", "A. Nadine › I. 1. Tötung, Vorsatz"),
       ("heim", "A. Nadine › I. 2. Heimtücke")], [
    *tafel("a", "A. Strafbarkeit Nadine"),
    z("Mord, §§ 212, 211 StGB", 110, 200, beim("a", "Mord"), "Bold", 40),
    ok(135, 305, "tb", gr=24), z("I. 1. Tötung, Vorsatz", 175, 285, "tb", "Bold", 36),
    z("I. 2. Heimtücke?", 175, 375, "heim", "Bold", 36),
    z("in feindlicher Willensrichtung", 215, 445, beim("heim", "feindlicher"), size=34),
    z("Arg- und Wehrlosigkeit des Opfers", 215, 500, beim("heim", "Arg"), size=34),
    z("bewusst zur Tötung ausgenutzt", 215, 555, beim("heim", "bewusst"), size=34),
    pille("Mordmerkmal, § 211 II StGB", 110, 680, beim("heim", "Heimtücke"), fill=GELB, size=32),
    peep_voll("NA_ernst", FX, BR, FR, "a", bis="heim"),
    peep_voll("NA_traurig", FX, BR, FR, "heim", anim="cut"),
    ficon("tabler", "door", FX - 10, 380, 150, "tb", fuell=BLAU),
    pille("Ralf tot", FX - 10, 150, "tb", fill=GRAU, size=30, anker="m"),
])

folie([("schlaf2", "A. Nadine › I. 2. Heimtücke › Schlafender"), ("heim_erg", "A. Nadine › I. 2. Heimtücke (+)")], [
    *tafel("schlaf2", "Heimtücke am Schlafenden"),
    ok(135, 225, "schlaf2", gr=22), z("wehrlos: Ralf schläft", 175, 200, "schlaf2", "Bold", 36),
    ok(135, 300, beim("schlaf2", "Seine"), gr=22), z("arglos: Arglosigkeit mit in den Schlaf genommen", 175, 275,
                                                     beim("schlaf2", "Seine"), size=34),
    ok(135, 375, "nie", gr=22), z("rechnete nicht mit Angriff:", 175, 350, "nie", size=34),
    z("Nadine hatte sich nie gewehrt", 215, 400, beim("nie", "Nadine"), size=34, farbe=TEXT),
    ok(135, 475, "heim_erg", gr=22), z("bewusst ausgenutzt", 175, 450, "heim_erg", size=34),
    fl_block(110, 580, 1040, 110, GRUEN, beim("heim_erg", "Heimtücke"), [("Heimtücke (+)", "ExtraBold", 42, INK)]),
    ficon("tabler", "bed", FX, 310, 240, "schlaf2", fuell=BLAU),
    ficon("tabler", "zzz", FX + 120, 170, 70, "schlaf2", fuell=WEISS, d=0.2),
    pille("nie gewehrt", FX, 335, "nie", fill=LILA, size=28, anker="m"),
    peep_voll("NA_traurig", FX, BR, FR, "schlaf2", bis="heim_erg"),
    peep_voll("NA_zu", FX, BR, FR, "heim_erg", anim="cut"),
])

# F Rechtswidrigkeit: §§ 32, 34 ------------------------------------------------------------------------------------------
folie([("rw", "A. Nadine › II. Rechtswidrigkeit"), ("nw", "A. Nadine › II. 1. Notwehr, § 32 StGB")], [
    *tafel("rw", "II. Rechtswidrigkeit"),
    z("Rechtfertigung?", 110, 200, "rw", "Bold", 40),
    z("1. Notwehr, § 32 StGB", 110, 290, "nw", "Bold", 38),
    z("gegenwärtiger rechtswidriger Angriff?", 150, 360, beim("nw", "gegenwärtigen"), size=36),
    nein(175, 455, beim("nw", "Ralf"), gr=22), z("Ralf schläft: kein Angriff", 215, 435, beim("nw", "Ralf"), size=36),
    *plusminus("Notwehr", 110, 560, "nw_erg", False, size=40, stil="Bold"),
    ficon("tabler", "bed", FX, 310, 240, "rw", fuell=BLAU),
    ficon("tabler", "zzz", FX + 120, 170, 70, "rw", fuell=WEISS, d=0.2),
    pille("kein Angriff", FX, 335, beim("nw", "Angriff", nr=2), fill=ROT, size=30, anker="m"),
    peep_voll("NA_ernst", FX, BR, FR, "rw"),
])

folie([("ns", "A. Nadine › II. 2. Notstand, § 34 StGB"), ("rw_erg", "A. Nadine › II. Rechtswidrigkeit (+)")], [
    *tafel("ns", "2. Notstand, § 34 StGB"),
    z("geschütztes Interesse muss", 110, 200, "ns", "Bold", 38),
    z("wesentlich überwiegen", 110, 250, beim("ns", "wesentlich"), "Bold", 38),
    nein(135, 360, "ns2", gr=22), z("Gesundheit Nadine/Töchter überwiegt nicht", 175, 340, "ns2", size=34),
    z("Ralfs Leben", 215, 390, beim("ns2", "Leben"), size=34),
    nein(135, 470, "ns3", gr=22), z("auch bei akuter Lebensgefahr: nicht", 175, 450, "ns3", size=34),
    z("zu ihren Gunsten", 215, 500, beim("ns3", "Gunsten"), size=34, farbe=TEXT),
    fl_block(110, 580, 1040, 110, ROT, "rw_erg", [("Tat rechtswidrig", "ExtraBold", 42, INK)]),
    ficon("tabler", "scale", FX, 310, 200, "ns", fuell=GELB),
    pille("Gesundheit", FX - 140, 335, beim("ns2", "Gesundheit"), fill=LILA, size=28, anker="m"),
    pille("Leben", FX + 150, 335, beim("ns2", "Leben"), fill=ROT, size=28, anker="m"),
    peep_voll("NA_ernst", FX, BR, FR, "ns", bis="rw_erg"),
    peep_voll("NA_muede", FX, BR, FR, "rw_erg", anim="cut"),
])

# G Schuld: § 35 I, Gefahr -------------------------------------------------------------------------------------------------
folie([("schuld", "A. Nadine › III. Schuld, § 35 I StGB"), ("dauer", "A. Nadine › III. § 35 I › Dauergefahr"),
       ("jetzt", "A. Nadine › III. § 35 I › gegenwärtig"), ("ehe", "A. Nadine › III. § 35 I › Zumutbarkeit")], [
    *tafel("schuld", "III. Schuld: § 35 I StGB"),
    z("gegenwärtige Gefahr für Leben, Leib, Freiheit", 110, 200, "gefahr", "Bold", 36),
    z("kein Angriff nötig", 150, 255, beim("gefahr", "Angriff"), size=34, farbe=TEXT),
    ok(135, 350, "dauer", gr=22), z("Dauergefahr: Gewalt jederzeit möglich", 175, 330, "dauer", size=34),
    ok(135, 425, "jetzt", gr=22), z("gegenwärtig, obwohl Ralf schläft", 175, 405, "jetzt", size=34),
    z("früher nachts ohne Anlass geschlagen", 215, 460, beim("jetzt", "Er"), size=32, farbe=TEXT),
    z("nach dem Aufwachen neue Gewalt", 215, 510, beim("jetzt", "Aufwachen"), size=32, farbe=TEXT),
    ok(135, 600, "ehe", gr=22), z("Ausharren in der Ehe: Gefahr", 175, 580, "ehe", size=34),
    z("trotzdem nicht zumutbar (§ 35 I 2)", 215, 630, beim("ehe", "nicht"), size=34),
    ficon("tabler", "alert-triangle", FX, 310, 170, "gefahr", fuell=GELB, bis="jetzt"),
    ficon("tabler", "clock", FX, 310, 170, "jetzt", fuell=GELB, bis="ehe"),
    pille("jederzeit", FX, 335, beim("dauer", "jederzeit"), fill=ROT, size=30, anker="m", bis="ehe"),
    ficon("tabler", "home", FX, 310, 170, "ehe", fuell=LILA),
    pille("blieb bei ihm", FX, 335, "ehe", fill=LILA, size=30, anker="m"),
    peep_voll("NA_ernst", FX, BR, FR, "schuld", bis="dauer"),
    peep_voll("NA_angst", FX, BR, FR, "dauer", anim="cut", bis="ehe"),
    peep_voll("NA_traurig", FX, BR, FR, "ehe", anim="cut"),
])

# H Schuld: nicht anders abwendbar -----------------------------------------------------------------------------------------
GX, BX = 1380, 1700                     # Nadine mit Koffer (hypothetisch), Beraterin
folie([("anders", "A. Nadine › III. § 35 I › nicht anders abwendbar")], [
    *tafel("anders", "Nicht anders abwendbar?"),
    z("Tat = einzig geeignetes Mittel?", 110, 200, beim("anders", "die"), "Bold", 38),
    z("Andere Wege:", 110, 300, "hilfe", "Bold", 36),
    ficon("tabler", "home-shield", 175, 420, 70, beim("hilfe", "Frauenhaus"), fuell=GRUEN),
    z("mit den Töchtern ins Frauenhaus", 230, 365, beim("hilfe", "Frauenhaus"), size=36),
    ficon("fluent-emoji-high-contrast", "police-car", 175, 515, 74, beim("hilfe", "Polizei"), fuell=BLAU),
    z("die Polizei um Hilfe bitten", 230, 460, beim("hilfe", "Polizei"), size=36),
    pille("hypothetisch", 110, 600, "hilfe", fill=GELB, size=30),
    szene(peep_voll("NG_hoffnung_r", GX, BODEN, FH, "hilfe"), "007koffer*", 0.7, versatz=0.1),
    ficon("tabler", "luggage", GX + 125, BODEN - 2, 95, "hilfe", fuell=LILA),
    pille("Nadine", GX, BODEN + 22, "hilfe", fill=LILA, size=30, anker="m"),
    peep_voll("BE_freundlich", BX, BODEN, FH, "hilfe", d=0.3, bis="b1"),
    *redet("BE_redet", BX, BODEN, FH, "b1", "regel"),
    pille("Beraterin", BX, BODEN + 22, "hilfe", fill=GRUEN, size=30, anker="m", d=0.3),
    blase("sprech", 520, 190, "b1", 1500, 240, inhalt=["Sie und Ihre Töchter können", "noch heute zu uns kommen."],
          textsize=31, figur=("BE_redet", BX, BODEN, FH)),
    ficon("tabler", "home-shield", 1450, 640, 190, "anders", fuell=GRUEN, d=0.2, bis="hilfe"),
    ficon("fluent-emoji-high-contrast", "police-car", 1730, 640, 230, "anders", fuell=BLAU, d=0.3, bis="hilfe"),
])

folie([("regel", "A. Nadine › III. § 35 I › Hilfe Dritter geht vor"),
       ("versucht", "A. Nadine › III. § 35 I › nicht anders abwendbar (−)")], [
    *tafel("regel", "BGH: Hilfe Dritter geht vor"),
    z("Dauergefahr regelmäßig anders abwendbar:", 110, 200, "regel", "Bold", 36),
    z("Hilfe Dritter, v. a. staatlicher Stellen", 150, 255, beim("regel", "Hilfe"), size=34),
    z("Ausnahme: Wirksamkeit der Hilfe nach", 110, 345, "ausnahme", "Bold", 34),
    z("konkreten Umständen von vornherein zweifelhaft", 150, 395, beim("ausnahme", "Wirksamkeit"), size=34),
    nein(135, 495, "versucht", gr=22), z("Nadine: keine Hilfe gesucht", 175, 475, "versucht", size=34),
    z("Ausnahme? „eher fernliegend“, LG muss klären", 175, 545, "offen", size=32, farbe=TEXT),
    fl_block(110, 640, 1040, 110, ROT, beim("offen", "fernliegend"), [("§ 35 I in der Regel (−)", "ExtraBold", 40, INK)]),
    ficon("fluent-emoji-high-contrast", "classical-building", FX, 290, 170, "regel", fuell=WEISS),
    pille("BGHSt 48, 255", FX, 325, "regel", fill=WEISS, size=28, anker="m"),
    peep_voll("NA_ernst", FX, BR, FR, "regel", bis="versucht"),
    peep_voll("NA_traurig", FX, BR, FR, "versucht", anim="cut"),
])

# I Schuld: § 35 II Irrtum -------------------------------------------------------------------------------------------------
NI = ("NA_zu", FX, BR, FR)
folie([("irrtum", "A. Nadine › III. 2. Irrtum, § 35 II StGB"), ("pruef", "A. Nadine › III. 2. Irrtum › Vermeidbarkeit")], [
    *tafel("irrtum", "Irrtum, § 35 II StGB"),
    z("Nadine hält ihre Lage für ausweglos", 110, 200, "irrtum", "Bold", 36),
    z("unvermeidbar → ohne Strafe", 150, 280, "unverm", size=36),
    z("vermeidbar → Strafe, zwingend gemildert", 150, 340, "verm", size=36),
    z("Maßstab: Auswege gewissenhaft geprüft?", 110, 440, "pruef", "Bold", 36),
    z("bei Tötung: strenge Anforderungen", 150, 500, beim("pruef", "Bei"), size=34),
    z("lange Bedenkzeit, Rat möglich", 150, 570, "zeit", size=34),
    z("→ spricht für Vermeidbarkeit", 190, 620, beim("zeit", "spricht"), "Bold", 34),
    blase("denk", 330, 200, beim("irrtum", "ausweglos"), 1560, 210, inhalt=["ausweglos?"], textsize=40, figur=NI, bis="pruef"),
    ficon("tabler", "search", FX, 310, 150, "pruef", fuell=GELB, bis="zeit"),
    ficon("tabler", "hourglass", FX, 310, 150, "zeit", fuell=GELB),
    pille("lange Bedenkzeit", FX, 335, beim("zeit", "Bedenkzeit"), fill=GELB, size=28, anker="m"),
    peep_voll("NA_zu", FX, BR, FR, "irrtum", bis="pruef"),
    peep_voll("NA_ernst", FX, BR, FR, "pruef", anim="cut"),
])

# J Strafe und Ergebnis ----------------------------------------------------------------------------------------------------
folie([("folge", "A. Nadine › IV. Strafe"), ("vorrang", "A. Nadine › IV. Strafe › § 35 II 2 vor Rechtsfolgenlösung")], [
    *tafel("folge", "IV. Strafe"),
    z("Mord: lebenslang, § 211 I StGB", 110, 200, beim("folge", "Mord"), "Bold", 36),
    z("LG mildert: außergewöhnliche Umstände", 150, 270, beim("lg", "außergewöhnlicher"), size=34),
    z("9 Jahre, Rechtsfolgenlösung (§ 49 I Nr. 1 analog)", 150, 320, beim("lg", "neun"), size=30, farbe=TEXT),
    z("Großer Senat, BGHSt 30, 105", 150, 375, "gs", size=32, farbe=TEXT),
    ok(135, 470, "vorrang", gr=22), z("Vorrang: gesetzliche Milderung", 175, 450, "vorrang", "Bold", 34),
    z("§ 35 II 2, § 49 I StGB", 215, 500, beim("vorrang", "Paragraf"), size=34),
    z("Strafrahmen: 3 bis 15 Jahre", 175, 570, "rahmen", size=34),
    z("Misshandlungen zählen stärker mildernd", 175, 630, "gewicht", size=34),
    ficon("tabler", "gavel", FX, 310, 170, "folge", fuell=GELB),
    pille("lebenslang", FX, 335, beim("folge", "lebenslanger"), fill=ROT, size=30, anker="m", bis="lg"),
    pille("LG: 9 Jahre", FX, 335, beim("lg", "neun"), fill=GELB, size=30, anker="m", bis="rahmen"),
    pille("3 bis 15 Jahre", FX, 335, "rahmen", fill=GRUEN, size=30, anker="m"),
    peep_voll("NA_muede", FX, BR, FR, "folge", bis="gewicht"),
    peep_voll("NA_traurig", FX, BR, FR, "gewicht", anim="cut"),
])

folie([("erg", "A. Nadine › Ergebnis")], [
    *tafel("erg", "Ergebnis"),
    z("BGH hebt die Verurteilung auf", 110, 200, beim("erg", "hob"), "Bold", 38),
    z("Für die Klausur:", 110, 300, "erg2", "Bold", 36),
    ok(135, 385, beim("erg2", "Mord"), gr=22), z("Mord, Heimtücke", 175, 365, beim("erg2", "Mord"), size=36),
    nein(135, 455, beim("erg2", "gerechtfertigt"), gr=22), z("nicht gerechtfertigt", 175, 435, beim("erg2", "gerechtfertigt"), size=36),
    nein(135, 525, beim("erg2", "entschuldigt"), gr=22), z("in der Regel nicht entschuldigt", 175, 505, beim("erg2", "entschuldigt"), size=36),
    fl_block(110, 610, 1040, 140, GELB, "erg3", [("vermeidbarer Irrtum:", "ExtraBold", 38, INK),
                                               ("zwingend gemilderte Strafe", "Regular", 34, INK)]),
    ficon("fluent-emoji-high-contrast", "classical-building", FX, 290, 170, "erg", fuell=WEISS),
    pille("aufgehoben", FX, 325, beim("erg", "hob"), fill=GELB, size=30, anker="m"),
    peep_voll("NA_ernst", FX, BR, FR, "erg"),
])

# K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Angriff und Gefahr trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Angriff und Gefahr trennen", 200, 200, beim("tipp", "Trenne"), "Bold", 38),
    nein(175, 335, beim("tipp1", "Notwehr"), gr=22), z("§ 32: braucht einen Angriff", 215, 315, beim("tipp1", "Notwehr"), size=36),
    z("Schlafender greift nicht an", 255, 370, beim("tipp1", "Angriff"), size=34, farbe=TEXT),
    ok(175, 475, beim("tipp1", "Dauergefahr"), gr=22), z("Dauergefahr: beim Notstand", 215, 455, beim("tipp1", "Dauergefahr"), size=36),
    z("§§ 34, 35 StGB", 255, 510, beim("tipp1", "Notstand"), size=34, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Klausurschema ----------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 200, 260
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Haustyrannen-Fall", 110, 90, "sch", 54),
    z("A. Strafbarkeit: §§ 212, 211 StGB", K1, 190, "sch", "Bold", 40, rechts=1820),
    z("I. Tatbestand: Tötung, Vorsatz, Heimtücke", K2, 260, "k1", "Bold", 36, rechts=1820),
    z("II. Rechtswidrigkeit", K2, 330, "k2", "Bold", 36, rechts=1820),
    z("§ 32: kein gegenwärtiger Angriff · § 34: Abwägung scheitert", K3, 385, beim("k2", "Notwehr"), size=34, farbe=TEXT, rechts=1820),
    z("III. Schuld: § 35 I StGB", K2, 460, "k3", "Bold", 36, rechts=1820),
    z("Dauergefahr · Gegenwärtigkeit · andere Abwendbarkeit (Hilfe Dritter)", K3, 515, beim("k3", "Dauergefahr"), size=34,
      farbe=TEXT, rechts=1820),
    z("§ 35 II: Irrtum und Vermeidbarkeit", K3, 570, "k4", size=34, farbe=TEXT, rechts=1820),
    z("IV. Strafe", K2, 645, "k5", "Bold", 36, rechts=1820),
    z("§ 35 II 2, § 49 I StGB vor der Rechtsfolgenlösung", K3, 700, beim("k5", "Milderung"), size=34, farbe=TEXT, rechts=1820),
])

# M Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gegen den schlafenden", 0)], [("Haustyrannen: ", 0), ("keine Notwehr.", "a")]], 750, 320, 54, "merke",
                {"a": beim("merke", "keine")}),
    *markertext([[("Entschuldigt in der Regel nicht:", 0)], [("Hilfe von außen ", "b"), ("geht vor.", "c")]],
                750, 580, 48, "m2", {"b": beim("m2", "Hilfe"), "c": beim("m2", "geht")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
