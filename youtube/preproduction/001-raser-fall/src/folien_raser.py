"""Folge 001 · Raser-Fall (nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, vereinfacht) – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Ampel (Nacht), B Kreuzung (Nacht), C Sachverhalt, D Vorsatz, E Mordmerkmale, F Max,
G Klausurtipp (Lexi), H Klausurschema, I Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Motor, Aufprall)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from PIL import ImageDraw

bausteine.FIGORDNER = "op_rf/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE, nacht=None)          # Nacht = Verlauf, erzeugt im Renderer
PFAD_FARBE = dict(bausteine.PFAD_FARBE, nacht=(255, 255, 255, 170))
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
NACHTHAUS = (78, 92, 150, 255)
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
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def ampel(cx, unten, breite, cue, licht, bis=None, d=0.0):
    """Tabler 'traffic-lights' mit leuchtender oberer (rot) oder unterer (grün) Lampe; Geometrie aus dem 24er-Raster
    (Körper x 6–18, y 1–23; Lampen bei y 7/12/17)."""
    e = ficon("tabler", "traffic-lights", cx, unten, breite, cue, fuell=(58, 58, 64, 255), d=d, bis=bis)
    im = e.sprite.copy(); w, h = im.size
    dr = ImageDraw.Draw(im)
    ly = {"rot": (7 - 1) / 22, "gruen": (17 - 1) / 22}[licht]
    farbe = {"rot": (240, 70, 55, 255), "gruen": (80, 210, 110, 255)}[licht]
    r = w * 1.45 / 12
    dr.ellipse((w / 2 - r, h * ly - r, w / 2 + r, h * ly + r), fill=farbe, outline=INK, width=max(2, int(w / 40)))
    e.sprite = im
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


BODEN, FH = 880, 430

# A Fall: das Rennen (Nacht, Tatzeit gegen 0:30 Uhr) ----------------------------------------------------------------------
JX, MXX, AX = 300, 1560, 1790          # Jonas, Max, Ampel
CJ, CM, CW = 760, 1200, 380            # Autos Jonas (rot) und Max (blau)
nachtfolie([("nacht", "Fall · Das Rennen")], [
    pille("Der Raser-Fall", 70, 40, "nacht", fill=GELB, size=48),
    ficon("tabler", "moon-stars", 1720, 230, 120, "nacht", fuell=GELB, d=0.3),
    ficon("tabler", "buildings", 520, BODEN - 4, 300, "nacht", fuell=NACHTHAUS, d=0.2),
    ficon("tabler", "building", 1000, BODEN - 4, 240, "nacht", fuell=NACHTHAUS, d=0.3),
    ficon("tabler", "buildings", 1420, BODEN - 4, 280, "nacht", fuell=NACHTHAUS, d=0.4),
    linienzug([(40, BODEN), (1880, BODEN)], "nacht", breite=7, farbe=LINIE),
    ampel(AX, BODEN - 2, 150, "ampel", "rot", bis="gruen"),
    ampel(AX, BODEN - 2, 150, "gruen", "gruen", bis="rennen"),
    # geparkte Autos an der Ampel
    ficon("tabler", "car", CJ, BODEN - 2, CW, "ampel", fuell=ROT, bis="rennen"),
    ficon("tabler", "car", CM, BODEN - 2, CW, "ampel", fuell=BLAU, d=0.2, bis="rennen"),
    # Jonas
    peep_voll("JO_cool_r", JX, BODEN, FH, "ampel", bis="j1"),
    *redet("JO_redet_r", JX, BODEN, FH, "j1", "m1"),
    peep_voll("JO_cool_r", JX, BODEN, FH, "m1", anim="cut", bis="gruen"),
    pille("Jonas", JX, BODEN + 22, "ampel", fill=ROT, size=30, anker="m", d=0.2, bis="gruen"),
    # Max
    peep_voll("MX_cool", MXX, BODEN, FH, "ampel", d=0.3, bis="m1"),
    *redet("MX_redet", MXX, BODEN, FH, "m1", "gruen"),
    pille("Max", MXX, BODEN + 22, "ampel", fill=BLAU, size=30, anker="m", d=0.5, bis="gruen"),
    blase("sprech", 600, 210, "j1", 700, 250, inhalt=["Bis zum Ende vom Boulevard.", "Wer zuerst da ist?"], textsize=32,
          figur=("JO_redet_r", JX, BODEN, FH), bis="m1"),
    blase("sprech", 380, 160, "m1", 1300, 300, inhalt=["Abgemacht!"], textsize=40, figur=("MX_redet", MXX, BODEN, FH), bis="gruen"),
    # Grün: beide sitzen im Auto, Vollgas
    szene(pille("Vollgas!", CJ, 560, beim("gruen", "Vollgas"), fill=ORANGE, size=34, anker="m", bis="rennen"), "motor*", 0.9),
    # Rennen über mehrere Kreuzungen
    ampel(170, BODEN - 2, 90, "rennen", "rot", d=0.1),
    ampel(1760, BODEN - 2, 90, "rennen", "rot", d=0.3),
    bewegt(ficon("tabler", "car", 1380, BODEN - 2, CW, "rennen", fuell=ROT, anim="cut"), ("rennen", 0.0), beim("rennen", "Rot", ende=True), -1150),
    bewegt(ficon("tabler", "car", 900, BODEN - 2, CW, "rennen", fuell=BLAU, anim="cut"), ("rennen", 0.0), beim("rennen", "Rot", ende=True), -950),
    pille("mehrere Kreuzungen, teils bei Rot", 960, 470, beim("rennen", "Rot"), fill=ROT, size=36, anker="m"),
])

# B Fall: die Kreuzung --------------------------------------------------------------------------------------------------
SX, KX = 1290, 960                     # Geländewagen, Kollisionspunkt
nachtfolie([("kreuzung", "Fall · Die Kreuzung"), ("frage", "Fall · Die Frage")], [
    ficon("tabler", "moon-stars", 1780, 200, 110, "kreuzung", fuell=GELB, d=0.2),
    linienzug([(40, BODEN), (1880, BODEN)], "kreuzung", breite=7, farbe=LINIE),
    ampel(110, BODEN - 2, 130, "kreuzung", "rot", d=0.2),
    pille("Rot", 110, 575, beim("kreuzung", "Rot"), fill=ROT, size=32, anker="m", bis="crash"),
    bewegt(ficon("tabler", "car", 820, BODEN - 2, 360, "kreuzung", fuell=ROT, anim="cut", bis="crash"),
           ("kreuzung", 0.2), beim("kreuzung", "Stundenkilometern", ende=True), -820),
    bewegt(ficon("tabler", "car", 420, BODEN - 2, 330, "kreuzung", fuell=BLAU, anim="cut"),
           ("kreuzung", 0.4), beim("kreuzung", "Stundenkilometern", ende=True), -620),
    pille("mehr als 160 km/h", 860, 420, beim("kreuzung", "hundertsechzig"), fill=ROT, size=36, anker="m", bis="crash"),
    # Geländewagen von rechts bei Grün
    ampel(1700, BODEN - 2, 90, "suv", "gruen", d=0.1, bis="crash"),
    bewegt(ficon("tabler", "car-suv", SX, BODEN - 2, 380, "suv", fuell=GRAU, spiegeln=True, anim="cut", bis="crash"),
           ("suv", 0.0), beim("suv", "Grün", ende=True), 450),
    pille("Grün", SX, 560, beim("suv", "Grün"), fill=GRUEN, size=32, anker="m", bis="crash"),
    # Zusammenstoß
    szene(ficon("tabler", "car-crash", KX, BODEN - 2, 400, beim("crash", "rammt"), fuell=ROT, anim="cut"), "aufprall*", 0.9),
    ficon("tabler", "car-suv", SX + 40, BODEN - 2, 380, beim("crash", "rammt"), fuell=GRAU, spiegeln=True, anim="cut"),
    pille("Fahrer (69) stirbt", SX + 40, 500, beim("tod", "Fahrer"), fill=WEISS, size=34, anker="m"),
    # Jonas nach dem Unfall
    *redet("JO_klagt", 1700, BODEN, FH, "j2", "frage"),
    peep_voll("JO_klagt", 1700, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 500, 210, "j2", 1330, 230, inhalt=["Ich wollte doch", "niemanden töten!"], textsize=36,
          figur=("JO_klagt", 1700, BODEN, FH), bis="frage"),
    pille("Mord? Und Max?", 960, 975, "frage", fill=PINK, size=38, anker="m"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Gegen 0:30 Uhr stehen Jonas und Max mit ihren Autos nebeneinander an einer roten Ampel in der Innenstadt und "
    "verabreden ein Rennen. Sie rasen über mehrere Kreuzungen, teils bei Rot.",
    "An der letzten Kreuzung fahren beide ungebremst bei Rot ein, Jonas mit mehr als 160 km/h. Er rammt einen "
    "Geländewagen, der bei Grün von rechts kommt. Dessen 69-jähriger Fahrer stirbt. Max trifft niemanden.",
    "(Nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, Berliner Ku’damm-Fall; vereinfacht, Namen geändert.)",
], "Wie haben sich Jonas und Max strafbar gemacht?")

# D Jonas: Vorsatz ---------------------------------------------------------------------------------------------------
FX, BR, FR = 1560, 930, 520
folie([("a", "A. Jonas › §§ 212, 211 StGB"), ("obj", "A. Jonas › I. 1. Objektiver Tatbestand"),
       ("vors", "A. Jonas › I. 2. Vorsatz")], [
    *tafel("a", "A. Strafbarkeit Jonas"),
    z("Mord, §§ 212, 211 StGB", 110, 200, beim("a", "Mord"), "Bold", 40),
    ok(135, 305, "obj", gr=24), z("I. 1. Objektiv: Tod, Kausalität", 175, 285, "obj", "Bold", 36),
    z("I. 2. Vorsatz?", 175, 375, "vors", "Bold", 36),
    nein(215, 465, beim("formen", "Absicht"), gr=22), z("Absicht", 250, 445, beim("formen", "Absicht"), size=36),
    nein(215, 535, beim("formen", "sicheres"), gr=22), z("sicheres Wissen", 250, 515, beim("formen", "sicheres"), size=36),
    z("→ bleibt: bedingter Vorsatz", 215, 595, beim("formen", "bleibt"), "Bold", 36),
    pille("das eigentliche Problem", 110, 700, beim("vors", "Problem"), fill=PINK, size=34),
    peep_voll("JO_cool", FX, BR, FR, "a", bis="vors"),
    peep_voll("JO_denkt", FX, BR, FR, "vors", anim="cut"),
    ficon("tabler", "car-crash", FX - 20, 330, 200, "obj", fuell=ROT, bis="vors"),
])

folie([("def", "A. Jonas › I. 2. Vorsatz › bedingter Vorsatz"), ("fahrl", "A. Jonas › I. 2. Vorsatz › Abgrenzung")], [
    *tafel("def", "Bedingter Vorsatz"),
    z("Wissen: Tod möglich, nicht ganz fernliegend", 110, 200, "def", "Bold", 36),
    z("Wollen: billigt oder findet sich ab", 110, 285, "def2", "Bold", 36),
    z("auch wenn gleichgültig oder unerwünscht", 150, 345, beim("def2", "mag"), size=34, farbe=TEXT),
    z("Bewusste Fahrlässigkeit:", 110, 470, "fahrl", "Bold", 38),
    z("vertraut ernsthaft, nicht nur vage,", 150, 535, beim("fahrl", "ernsthaft"), size=36),
    z("auf einen guten Ausgang", 150, 590, beim("fahrl", "vertraut"), size=36),
    pille("Abgrenzung: Gesamtschau aller Umstände", 110, 700, beim("fahrl", "gut"), fill=GELB, size=34),
    ficon("tabler", "brain", 1420, 330, 150, "def", fuell=PINK),
    ficon("tabler", "scale", 1700, 330, 150, "def2", fuell=GELB, bis="fahrl"),
    peep_voll("JO_denkt", FX, BR, FR, "def", bis="fahrl"),
    peep_voll("JO_cool", FX, BR, FR, "fahrl", anim="cut"),
    blase("denk", 400, 220, beim("fahrl", "vertraut"), 1560, 230, inhalt=["Wird schon", "gutgehen!"], textsize=38,
          figur=("JO_cool", FX, BR, FR)),
])

folie([("eigen", "A. Jonas › I. 2. Vorsatz › Eigengefahr"), ("bgh18", "A. Jonas › I. 2. Vorsatz › BGH 2018")], [
    *tafel("eigen", "Eigengefahr"),
    *plusminus("Jonas gefährdet auch sich selbst", 110, 200, beim("eigen", "Wer"), False, size=36, stil="Bold"),
    z("BGH, 1.3.2018 – 4 StR 399/17: aufgehoben", 110, 300, "bgh18", "Bold", 36),
    z("1. Vorsatz nötig, solange Unfall vermeidbar", 150, 370, "zeit", size=34),
    nein(175, 445, beim("zeit", "Ein"), gr=22), z("Entschluss erst in der Kreuzung: zu spät", 210, 425, beim("zeit", "Ein"), size=34),
    z("2. Eigengefahr im Einzelfall würdigen", 150, 520, "panzer", size=34),
    nein(175, 595, beim("panzer", "Dass"), gr=22), z("kein Erfahrungssatz „wie im Panzer“", 210, 575, beim("panzer", "Dass"), size=34),
    peep_voll("JO_schock", FX, BR, FR, "eigen", bis="bgh18"),
    peep_voll("JO_denkt", FX, BR, FR, "bgh18", anim="cut"),
    # Zeitstrahl: Bremsen möglich → Kreuzung
    linienzug([(1290, 260), (1830, 260)], "zeit", breite=6, farbe=INK),
    pille("noch bremsen", 1390, 200, ("zeit", 0.3), fill=GRUEN, size=28, anker="m"),
    pille("in der Kreuzung", 1720, 200, beim("zeit", "Ein"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "shield", 1830, 420, 90, beim("panzer", "Panzer"), fuell=GRUEN),
    kreuz_i(1830, 420, beim("panzer", "Erfahrungssatz"), gr=34),
])

folie([("bgh20", "A. Jonas › I. 2. Vorsatz › BGH 2020"), ("vors_erg", "A. Jonas › I. 2. Vorsatz (+)")], [
    *tafel("bgh20", "BGH, 18.6.2020 – 4 StR 482/19"),
    z("Eigengefahr kann abgestuft sein:", 110, 200, "abgestuft", "Bold", 38),
    ok(135, 290, beim("abgestuft", "Jonas"), gr=22), z("Aufprall auf Seite: nur leicht verletzt", 175, 270, beim("abgestuft", "Jonas"), size=34),
    nein(135, 360, "vertraut", gr=22), z("vertraut nur: kein Zusammenstoß mit Max", 175, 340, "vertraut", size=34),
    ok(135, 430, "egal", gr=22), z("diesen Unfall für den Sieg hingenommen", 175, 410, "egal", size=34),
    ok(135, 500, "bremsen", gr=22), z("weitergefahren, als Bremsen noch ging", 175, 480, "bremsen", size=34),
    fl_block(110, 600, 1040, 120, GRUEN, "vors_erg", [("Bedingter Tötungsvorsatz (+)", "ExtraBold", 42, INK)]),
    ficon("tabler", "car", 1390, 330, 200, beim("abgestuft", "Aufprall"), fuell=ROT),
    ficon("tabler", "car-suv", 1640, 330, 200, beim("abgestuft", "Aufprall"), fuell=GRAU, spiegeln=True, d=0.15),
    pille("leicht verletzt", 1390, 140, beim("abgestuft", "leicht"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "trophy", 1800, 300, 110, "egal", fuell=GELB),
    peep_voll("JO_cool", FX, BR, FR, "bgh20", bis="egal"),
    peep_voll("JO_stolz", FX, BR, FR, "egal", anim="cut", bis="vors_erg"),
    peep_voll("JO_muede", FX, BR, FR, "vors_erg", anim="cut"),
])

# E Jonas: Mordmerkmale, Ergebnis ---------------------------------------------------------------------------------------
folie([("mm", "A. Jonas › I. 3. Mordmerkmale"), ("mm_def", "A. Jonas › I. 3. Mordmerkmale › gemeingefährliches Mittel")], [
    *tafel("mm", "I. 3. Mordmerkmale"),
    z("Gemeingefährliches Mittel?", 110, 200, beim("mm", "gemeingefährliche"), "Bold", 40),
    z("kann mehrere Menschen gefährden,", 150, 275, "mm_def", size=36),
    z("Täter beherrscht die Gefahr nicht", 150, 330, beim("mm_def", "weil"), size=36),
    *plusminus("objektiv: liegt nahe", 150, 430, "mm_sub", True, size=36),
    *plusminus("subjektiv: nicht belegt", 150, 500, beim("mm_subj", "war"), False, size=36),
    pille("BGH: Merkmal verneint", 110, 610, beim("mm_subj", "verneinte"), fill=ROT, size=36),
    ficon("tabler", "car", 1520, 640, 300, "mm_def", fuell=ROT),
    ficon("tabler", "users", 1330, 380, 130, beim("mm_def", "mehrere"), fuell=BLAU),
    ficon("tabler", "users", 1540, 330, 130, beim("mm_def", "mehrere"), fuell=GRUEN, d=0.15),
    ficon("tabler", "users", 1750, 380, 130, beim("mm_def", "mehrere"), fuell=LILA, d=0.3),
    pille("erkannt und gebilligt?", 1540, 800, "mm_subj", fill=PINK, size=32, anker="m"),
])

folie([("heim", "A. Jonas › I. 3. Mordmerkmale › Heimtücke"), ("nb", "A. Jonas › I. 3. Mordmerkmale › niedrige Beweggründe")], [
    *tafel("heim", "Der Mord hält trotzdem"),
    ok(135, 225, beim("heim", "Heimtücke"), gr=24), z("Heimtücke", 175, 200, beim("heim", "Heimtücke"), "Bold", 40),
    z("Opfer verlässt sich auf sein Grün:", 215, 270, beim("heim", "Fahrer"), size=36),
    z("arg- und wehrlos", 215, 325, beim("heim", "arg"), "Bold", 36),
    z("Jonas erfasst das und nimmt es hin", 215, 385, "heim2", size=36),
    ok(135, 505, "nb", gr=24), z("Niedrige Beweggründe", 175, 480, "nb", "Bold", 40),
    z("Zufallsopfer für den Sieg im Rennen:", 215, 550, beim("nb", "Tod"), size=36),
    z("krasses Missverhältnis zum Anlass", 215, 605, beim("nb", "krassem"), "Bold", 36),
    ampel(1360, 520, 140, "heim", "gruen"),
    ficon("tabler", "car-suv", 1620, 520, 280, beim("heim", "Fahrer"), fuell=GRAU, spiegeln=True),
    pille("arg- und wehrlos", 1620, 600, beim("heim", "arg"), fill=GELB, size=32, anker="m", bis="nb"),
    ficon("tabler", "trophy", 1430, 820, 150, beim("nb", "Sieg"), fuell=GELB),
    pille("≠", 1590, 760, beim("nb", "krassem"), fill=WEISS, size=44, anker="m"),
    ficon("tabler", "heart", 1750, 820, 150, beim("nb", "Zufallsopfers"), fuell=ROT),
])

folie([("rws", "A. Jonas › II. Rechtswidrigkeit, III. Schuld"), ("a_erg", "A. Jonas › Ergebnis")], [
    *tafel("rws", "Ergebnis Jonas"),
    ok(135, 225, beim("rws", "Rechtswidrigkeit"), gr=24), z("II. Rechtswidrigkeit", 175, 200, beim("rws", "Rechtswidrigkeit"), "Bold", 38),
    ok(135, 300, beim("rws", "Schuld"), gr=24), z("III. Schuld", 175, 275, beim("rws", "Schuld"), "Bold", 38),
    fl_block(110, 400, 1040, 180, GRUEN, "a_erg", [("Jonas: Mord, §§ 212, 211 StGB", "ExtraBold", 42, INK),
                                                  ("in Tateinheit mit § 315c StGB", "Regular", 34, INK)]),
    pille("Straßenverkehrsgefährdung", 110, 640, beim("a_erg", "Gefährdung"), fill=GELB, size=34),
    peep_voll("JO_muede", FX, BR, FR, "rws"),
])

# F Gegenfall Max --------------------------------------------------------------------------------------------------
folie([("max", "B. Max"), ("mt", "B. Max › Mittäterschaft, § 25 II StGB"), ("max_erg", "B. Max › eigene Tat"),
       ("versuch", "B. Max › Ergebnis")], [
    *tafel("max", "B. Strafbarkeit Max"),
    z("hat den Geländewagen nicht berührt", 110, 200, beim("max", "Er"), "Bold", 36),
    z("Mord in Mittäterschaft, § 25 II StGB?", 110, 280, "mt", "Bold", 36),
    z("gemeinsamer Tatentschluss auch zur Tötung", 150, 340, beim("mt", "Dafür"), size=34, farbe=TEXT),
    nein(135, 430, "abrede", gr=22), z("Rennabrede genügt nicht → BGH hebt auf", 175, 410, "abrede", size=34),
    ok(135, 510, beim("max_erg", "Auch"), gr=22), z("eigener bedingter Tötungsvorsatz", 175, 490, beim("max_erg", "Auch"), size=34),
    z("dass Jonas traf und nicht er: Zufall", 215, 550, "zufall", size=34, farbe=TEXT),
    fl_block(110, 640, 1040, 160, GRUEN, "versuch", [("Max: versuchter Mord", "ExtraBold", 42, INK),
                                                    ("§§ 212, 211, 22, 23 I StGB", "Regular", 34, INK)]),
    ficon("tabler", "car", 1560, 330, 260, "max", fuell=BLAU),
    peep_voll("MX_cool", FX, BR, FR, "max", bis="abrede"),
    peep_voll("MX_denkt", FX, BR, FR, "abrede", anim="cut", bis="versuch"),
    peep_voll("MX_ernst", FX, BR, FR, "versuch", anim="cut"),
])

# G Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Vorsatz begründen"), ("tipp2", "Klausurtipp · § 315d StGB heute")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nie allein aus der Gefährlichkeit", 200, 200, beim("tipp", "Schließe"), "Bold", 36),
    z("auf Vorsatz schließen", 200, 250, beim("tipp", "Schließe"), "Bold", 36),
    ok(175, 345, "tipp1", gr=22), z("Wissen und Wollen mit Tatsachen belegen:", 215, 325, "tipp1", size=34),
    z("Motiv · Eigengefahr · Zeitpunkt", 255, 380, beim("tipp1", "Motiv"), "Bold", 34),
    ok(175, 470, "tipp1b", gr=22), z("jedes Mordmerkmal auch subjektiv", 215, 450, "tipp1b", size=34),
    z("Heute: § 315d StGB (seit 13.10.2017)", 200, 570, "tipp2", "Bold", 36),
    z("Abs. 5: Tod durch das Rennen, bis 10 Jahre", 215, 635, "tipp3", size=34),
    z("für den Tod genügt Fahrlässigkeit", 215, 690, beim("tipp3", "Für"), size=34),
    z("(auf den Fall von 2016 noch nicht anwendbar)", 215, 760, beim("tipp2", "seit"), size=30, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# H Klausurschema -------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 200, 260
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Raser-Fall", 110, 90, "sch", 54),
    z("A. Unfallfahrer: §§ 212, 211 StGB", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("I. Tatbestand", K2, 265, beim("k1", "Tatbestand"), "Bold", 36, rechts=1820),
    z("1. objektiv: Tod, Kausalität", K3, 320, beim("k1", "Erstens"), size=34, farbe=TEXT, rechts=1820),
    z("2. bedingter Tötungsvorsatz: Wissen, Wollen, Eigengefahr, Zeitpunkt", K3, 372, "k1b", size=34, farbe=TEXT, rechts=1820),
    z("3. Mordmerkmale, jeweils objektiv und subjektiv", K3, 424, "k1c", size=34, farbe=TEXT, rechts=1820),
    z("II. Rechtswidrigkeit", K2, 495, "k2", "Bold", 36, rechts=1820),
    z("III. Schuld", K2, 550, beim("k2", "Schuld"), "Bold", 36, rechts=1820),
    z("IV. Konkurrenzen", K2, 605, "k3", "Bold", 36, rechts=1820),
    z("B. Zweiter Raser", K1, 700, "k4", "Bold", 40, rechts=1820),
    z("Mittäterschaft, § 25 II StGB? Sonst eigene Tat, notfalls Versuch", K2, 765, beim("k4", "zuerst"), size=34, farbe=TEXT, rechts=1820),
])

# I Merksatz (Lexi) -----------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Raser sind nicht", 0)], [("automatisch ", 0), ("Mörder.", "a")]], 750, 320, 54, "merke",
                {"a": beim("merke", "Mörder")}),
    *markertext([[("Entscheidend: Tod anderer", 0)], [("billigend in Kauf genommen,", "b")], [("solange noch vermeidbar", "c")]],
                750, 560, 44, "m2", {"b": beim("m2", "billigend"), "c": beim("m2", "solange")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
