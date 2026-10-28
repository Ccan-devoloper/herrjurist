"""Folge 008 · Grundrechte Überblick: Freiheitsrechte, Gleichheitsrechte, Prüfung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Stadtpark, B Der Grund, C Der Kiosk, D Sachverhalt, E Grundrechtskatalog, F Welches
Grundrecht passt?, G Schutzbereich, H Eingriff, I Rechtfertigung (Schranke, Zweck, Eignung), J Erforderlichkeit,
Angemessenheit, K Art. 3 I: Ungleichbehandlung, L Art. 3 I: Rechtfertigung, M Ergebnis und Gegenfall, N Klausurtipp (Lexi),
O Klausurschema, P Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Handglocke, fahrender Verkaufswagen)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_008/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
BRAUN = (120, 92, 70, 255)
DAUER = bausteine._cj()["dauer"]
PA = "A. Berufsfreiheit, Art. 12 I GG"     # Prüfpfad Freiheitsrecht
PB = "B. Gleichheit, Art. 3 I GG"          # Prüfpfad Gleichheitsrecht


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def bis_(e, cue):
    """Endzeit für Elemente ohne bis-Parameter (Haken/Kreuz/Icons)."""
    e.bis = cue
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def eiswagen(cx, unten, breite, cue, bis=None, d=0.0, anim="pop", farbe=PINK, ware="ice-cream", warefarbe=GELB):
    """Verkaufswagen: Tabler 'truck' mit Ware (Tabler 'ice-cream' bzw. 'coffee') auf dem Dach."""
    return [ficon("tabler", "truck", cx, unten, breite, cue, fuell=farbe, d=d, bis=bis, anim=anim),
            ficon("tabler", ware, cx - breite * 0.12, unten - breite * 0.62, int(breite * 0.26), cue, fuell=warefarbe,
                  d=d, bis=bis, anim=anim)]


BODEN, FH = 880, 460
WIESE = (190, 230, 170, 255)

# A Fall: im Stadtpark -------------------------------------------------------------------------------------------------------
LX_, TX = 900, 1520                          # Lina (blickt nach rechts zu Tom), Tom (blickt nach links)
TO = ("TO_redet", TX, BODEN, FH)
folie([(("fall", -0.4), "Fall · Im Stadtpark")], [            # Prüfpfad ab dem ersten Bild nach dem Intro (0,0 s)
    pille("Der Eiswagen-Fall", 70, 40, ("fall", -0.4), fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], ("fall", -0.4), breite=7, farbe=INK),
    ficon("tabler", "trees", 1790, BODEN - 2, 200, ("fall", -0.4), fuell=GRUEN),
    ficon("tabler", "tree", 130, BODEN - 2, 150, ("fall", -0.4), fuell=GRUEN),
    pille("Stadtpark", 1790, BODEN + 22, "fall", fill=GRUEN, size=28, anker="m", d=0.2),
    *eiswagen(470, BODEN - 2, 420, "lina"),
    peep_voll("LI_froh_r", LX_, BODEN, FH, "lina", bis=beim("t1", "Verkaufswagen")),
    szene(ficon("tabler", "bell", LX_ + 120, BODEN - 175, 70, beim("lina", "verkauft"), fuell=GELB, bis="tom"), "008glocke*", 0.8),
    pille("Lina, Eisverkäuferin", LX_, BODEN + 22, "lina", fill=PINK, size=30, anker="m", d=0.2),
    ficon("tabler", "coins", 470, 300, 110, beim("lina", "Das"), fuell=GELB, bis="t1"),
    pille("ihr Lebensunterhalt", 470, 330, beim("lina", "Lebensunterhalt"), fill=GELB, size=32, anker="m", bis="t1"),
    # Tom vom Ordnungsamt
    peep_voll("TO_ruhig", TX, BODEN, FH, "tom", bis="t1"),
    pille("Tom, Ordnungsamt", TX, BODEN + 22, "tom", fill=BLAU, size=30, anker="m", d=0.2),
    *redet("TO_redet", TX, BODEN, FH, "t1", "grund"),
    ficon("tabler", "file-text", TX + 150, 600, 90, beim("t1", "Parksatzung"), fuell=WEISS),
    peep_voll("LI_schreck_r", LX_, BODEN, FH, beim("t1", "Verkaufswagen"), anim="cut"),
    blase("sprech", 760, 270, "t1", 1150, 220, inhalt=["Die Stadt hat eine neue Parksatzung.", "Ab Montag dürfen Verkaufswagen",
                                                      "nicht mehr in den Park fahren."], textsize=32, figur=TO),
    ficon("tabler", "truck-off", 470, 300, 120, beim("t1", "nicht"), fuell=ROT),
])

# B Fall: der Grund ------------------------------------------------------------------------------------------------------------
KX = 1580
KR = ("KR_redet", KX, BODEN, FH)
folie([("grund", "Fall · Der Grund")], [
    linienzug([(60, BODEN), (1860, BODEN)], "grund", breite=7, farbe=INK),
    fl_block(90, 800, 1120, 70, WIESE, "grund", [("Wiese", "Bold", 30, INK)], rand=4),
    ficon("tabler", "tree", 1260, BODEN - 2, 160, "grund", fuell=GRUEN, d=0.2),
    pille("letzter Sommer", 70, 40, "grund", fill=GELB, size=40),
    szene(bewegt(ficon("tabler", "truck", 860, 800, 380, beim("grund", "fuhren"), fuell=BLAU, anim="cut"),
                 beim("grund", "fuhren"), ("spuren", -0.3), -620), "008wagen*", 1.0),
    pille("kreuz und quer über Wege und Wiesen", 640, 290, beim("grund", "kreuz"), fill=WEISS, size=34, anker="m"),
    linienzug([(120, 845), (260, 830), (400, 848), (540, 832)], "spuren", breite=8, farbe=BRAUN),
    linienzug([(120, 862), (260, 847), (400, 865), (540, 849)], ("spuren", 0.15), breite=8, farbe=BRAUN),
    pille("tiefe Spuren im Rasen", 420, 375, beim("spuren", "Spuren"), fill=ORANGE, size=34, anker="m"),
    pille("Spaziergänger müssen ausweichen", 640, 455, beim("spuren", "Spaziergänger"), fill=LILA, size=32, anker="m"),
    # Frau Kranz, Spaziergängerin
    peep_voll("KR_ruhig", KX, BODEN, FH, "grund", d=0.3, bis="k1"),
    pille("Frau Kranz", KX, BODEN + 22, "grund", fill=LILA, size=30, anker="m", d=0.5),
    *redet("KR_redet", KX, BODEN, FH, "k1", "kiosk"),
    blase("sprech", 640, 210, "k1", 1300, 210, inhalt=["Endlich! Ständig musste ich", "den Wagen ausweichen."], textsize=34,
          figur=KR),
])

# C Fall: der Kiosk am Teich --------------------------------------------------------------------------------------------------
BX, LX2 = 820, 1560
BRx = ("BR_redet_r", BX, BODEN, FH)
LIx = ("LI_redet", LX2, BODEN, FH)
folie([("kiosk", "Fall · Der Kiosk"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "kiosk", breite=7, farbe=INK),
    ficon("tabler", "ripple", 170, BODEN - 10, 180, "kiosk", fuell=BLAU, d=0.2),
    pille("Teich", 170, BODEN + 22, "kiosk", fill=BLAU, size=28, anker="m", d=0.3),
    ficon("tabler", "building-store", 480, BODEN - 2, 330, "kiosk", fuell=TUERKIS),
    ficon("tabler", "ice-cream", 480, 668, 90, "kiosk", fuell=GELB, d=0.2),
    pille("Kiosk: Eis erlaubt", 480, 330, beim("kiosk", "darf"), fill=GRUEN, size=32, anker="m", bis="frage"),
    peep_voll("BR_ruhig_r", BX, BODEN, FH, "kiosk", d=0.2, bis="b1"),
    pille("Herr Brenner", BX, BODEN + 22, "kiosk", fill=TUERKIS, size=30, anker="m", d=0.3),
    *redet("BR_redet_r", BX, BODEN, FH, "b1", "l1"),
    peep_voll("BR_froh_r", BX, BODEN, FH, "l1", anim="cut"),
    blase("sprech", 560, 170, "b1", 1050, 220, inhalt=["Mein Kiosk fährt", "ja nirgendwohin."], textsize=36, figur=BRx, bis="l1"),
    # Lina kommt
    peep_voll("LI_aerger", LX2, BODEN, FH, ("kiosk", 0.3), bis="l1"),
    pille("Lina", LX2, BODEN + 22, ("kiosk", 0.3), fill=PINK, size=30, anker="m"),
    *redet("LI_redet", LX2, BODEN, FH, "l1", "frage"),
    peep_voll("LI_denkt", LX2, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 640, 230, "l1", 1230, 230, inhalt=["Das ist mein Beruf! Und der Kiosk", "verkauft dasselbe Eis wie ich!"],
          textsize=32, figur=LIx, bis="frage"),
    pille("Verletzt das Verbot Lina in ihren Grundrechten?", 960, 40, "frage", fill=PINK, size=36, anker="m"),
    pille("Freiheitsrecht?", 1100, 250, beim("frage", "Freiheitsrechte"), fill=BLAU, size=36, anker="m"),
    pille("Gleichheitsrecht?", 1100, 350, beim("frage", "Gleichheitsrechte"), fill=GELB, size=36, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Lina, eine Deutsche, verkauft seit Jahren im Sommer Eis aus ihrem Verkaufswagen im Stadtpark; davon lebt sie. Weil "
    "Verkaufswagen im letzten Sommer kreuz und quer über Wege und Wiesen fuhren, tiefe Spuren im Rasen hinterließen und "
    "Spaziergänger ausweichen mussten, erlässt die Stadt eine neue Parksatzung: Ab Montag dürfen Verkaufswagen nicht mehr "
    "in den Park fahren; der Verkauf aus Fahrzeugen im Park ist verboten. Der fest gebaute Kiosk am Teich darf weiter Eis "
    "verkaufen. Lina meint: „Das ist mein Beruf! Und der Kiosk verkauft dasselbe Eis wie ich!“",
    "Annahme: Die Satzung beruht auf einer wirksamen landesrechtlichen Grundlage und ist formell rechtmäßig.",
], "Verletzt das Verbot Lina in ihren Grundrechten?")

# E Grundrechtskatalog ------------------------------------------------------------------------------------------------------
FX, BR, FR = 1560, 930, 500
folie([("katalog", "Welches Grundrecht passt?"), ("frei", "Welches Grundrecht passt? › Freiheitsrechte"),
       ("gleich", "Welches Grundrecht passt? › Gleichheitsrechte"), ("bind", "Welches Grundrecht passt? › Bindung, Art. 1 III GG")], [
    *tafel("katalog", "Grundrechte, Art. 1–19 GG"),
    ficon("tabler", "pray", 160, 250, 70, beim("katalog", "Glauben"), fuell=LILA),
    z("Art. 4 Glaube", 215, 195, beim("katalog", "Glauben"), "Bold", 36),
    ficon("tabler", "message", 660, 250, 70, beim("katalog", "Meinung"), fuell=BLAU),
    z("Art. 5 Meinung", 715, 195, beim("katalog", "Meinung"), "Bold", 36),
    ficon("tabler", "users-group", 160, 345, 70, beim("katalog", "Versammlung"), fuell=ORANGE),
    z("Art. 8 Versammlung", 215, 290, beim("katalog", "Versammlung"), "Bold", 36),
    ficon("tabler", "briefcase", 660, 345, 70, beim("katalog", "Beruf"), fuell=GELB),
    z("Art. 12 Beruf", 715, 290, beim("katalog", "Beruf"), "Bold", 36),
    fl_block(110, 400, 1040, 130, BLAU, "frei", [("Freiheitsrechte", "ExtraBold", 40, INK),
                                               ("wehren staatliche Eingriffe ab", "Regular", 34, INK)]),
    fl_block(110, 560, 1040, 130, GELB, "gleich", [("Gleichheitsrechte", "ExtraBold", 40, INK),
                                                 ("vor allem Art. 3 GG", "Regular", 34, INK)]),
    z("Art. 1 III GG: Gesetzgebung, vollziehende Gewalt", 110, 730, "bind", "Bold", 34),
    z("und Rechtsprechung sind gebunden – auch die Stadt", 110, 780, beim("bind", "also"), size=34, farbe=TEXT),
    peep_voll("LI_denkt", FX, BR, FR, "katalog", bis="bind"),
    peep_voll("LI_ruhig", FX, BR, FR, "bind", anim="cut"),
    pille("Lina", FX, BR + 22, "katalog", fill=PINK, size=30, anker="m", d=0.2),
    ficon("tabler", "shield", FX, 330, 120, "frei", fuell=BLAU, bis="gleich"),
    ficon("tabler", "scale", FX, 330, 130, "gleich", fuell=GELB, bis="bind"),
    ficon("tabler", "building-bank", FX, 300, 140, beim("bind", "Gebunden"), fuell=GRAU),
    pille("Stadt", FX, 320, beim("bind", "Stadt"), fill=WEISS, size=30, anker="m"),
])

# F Welches Grundrecht passt? ------------------------------------------------------------------------------------------------
folie([("passt", "Welches Grundrecht passt? › Art. 12 I GG"), ("passt2", "Welches Grundrecht passt? › Art. 3 I GG")], [
    *tafel("passt", "Welches Grundrecht passt?"),
    ok(140, 230, beim("passt", "Artikel"), gr=24), z("Beruf: Art. 12 I GG", 185, 205, beim("passt", "Artikel"), "Bold", 40),
    z("spezieller als die allgemeine Handlungsfreiheit,", 225, 270, beim("passt", "spezieller"), size=34, farbe=TEXT),
    z("Art. 2 I GG", 225, 318, beim("passt", "spezieller"), size=34, farbe=TEXT),
    ok(140, 430, beim("passt2", "Kiosk"), gr=24), z("Kiosk anders behandelt: Art. 3 I GG", 185, 405, beim("passt2", "Kiosk"), "Bold", 40),
    fl_block(110, 560, 1040, 110, BLAU, beim("passt", "Artikel"), [("A. Freiheitsrecht: Art. 12 I GG", "ExtraBold", 38, INK)]),
    fl_block(110, 700, 1040, 110, GELB, beim("passt2", "Artikel"), [("B. Gleichheitsrecht: Art. 3 I GG", "ExtraBold", 38, INK)]),
    peep_voll("LI_denkt", FX, BR, FR, "passt", bis="passt2"),
    peep_voll("LI_aerger", FX, BR, FR, "passt2", anim="cut"),
    ficon("tabler", "briefcase", FX, 330, 120, beim("passt", "Beruf"), fuell=GELB, bis="passt2"),
    ficon("tabler", "building-store", FX - 90, 330, 130, beim("passt2", "Kiosk"), fuell=TUERKIS),
    ficon("tabler", "equal-not", FX + 80, 300, 90, beim("passt2", "anders"), fuell=ROT),
])

# G A. I. Schutzbereich --------------------------------------------------------------------------------------------------------
folie([("sb", f"{PA} › I. Schutzbereich"), ("sb_p", f"{PA} › I. Schutzbereich › persönlich"),
       ("sb_s", f"{PA} › I. Schutzbereich › sachlich")], [
    *tafel("sb", "A. I. Schutzbereich, Art. 12 I GG", size=46),
    z("1. persönlich: „Alle Deutschen“", 175, 195, "sb_p", "Bold", 38),
    ok(140, 280, beim("sb_p", "Lina"), gr=22), z("Lina ist Deutsche", 215, 255, beim("sb_p", "Lina"), size=34, farbe=TEXT),
    z("Ausländer: Art. 2 I GG", 215, 305, "ausl", size=34, farbe=TEXT),
    z("GmbH: über Art. 19 III GG", 215, 355, "gmbh", size=34, farbe=TEXT),
    z("2. sachlich: Beruf", 175, 450, "sb_s", "Bold", 38),
    z("jede auf Dauer angelegte Tätigkeit,", 215, 510, beim("sb_s", "jede"), size=34, farbe=TEXT),
    z("die der Schaffung und Aufrechterhaltung", 215, 558, beim("sb_s", "Schaffung"), size=34, farbe=TEXT),
    z("einer Lebensgrundlage dient", 215, 606, beim("sb_s", "Schaffung"), size=34, farbe=TEXT),
    ok(140, 690, beim("sb_s", "Lina"), gr=22), z("Lina lebt vom Eisverkauf", 215, 665, beim("sb_s", "Lina"), size=34, farbe=TEXT),
    fl_block(110, 760, 1040, 95, GRUEN, ("sb_s", 9.9), [("Schutzbereich eröffnet", "ExtraBold", 38, INK)]),
    peep_voll("LI_ruhig", FX, BR, FR, "sb", bis="sb_p"),
    peep_voll("LI_froh", FX, BR, FR, "sb_p", anim="cut"),
    ficon("tabler", "id", FX, 330, 120, beim("sb_p", "Deutsche"), fuell=GELB, bis="ausl"),
    pille("Deutsche", FX, 350, beim("sb_p", "Lina"), fill=GELB, size=32, anker="m", bis="ausl"),
    ficon("tabler", "world", FX, 330, 120, "ausl", fuell=BLAU, bis="gmbh"),
    pille("Art. 2 I GG", FX, 350, "ausl", fill=BLAU, size=32, anker="m", bis="gmbh"),
    ficon("tabler", "building-store", FX, 330, 130, "gmbh", fuell=TUERKIS, bis="sb_s"),
    pille("Lina-Eis GmbH", FX, 350, "gmbh", fill=TUERKIS, size=32, anker="m", bis="sb_s"),
    *eiswagen(FX, 330, 230, "sb_s"),
    ficon("tabler", "coins", FX + 160, 330, 80, beim("sb_s", "Lebensgrundlage"), fuell=GELB),
])

# H A. II. Eingriff ------------------------------------------------------------------------------------------------------------
folie([("ein", f"{PA} › II. Eingriff")], [
    *tafel("ein", "A. II. Eingriff"),
    z("Parksatzung: kein Verkauf aus dem Wagen", 175, 200, beim("ein", "Satzung"), "Bold", 36),
    z("im Park", 175, 250, beim("ein", "Satzung"), "Bold", 36),
    z("regelt, wo Lina ihren Beruf ausübt", 215, 330, beim("ein", "regelt"), size=34, farbe=TEXT),
    ok(140, 450, beim("ein", "Das"), gr=24), z("Eingriff (+)", 185, 425, beim("ein", "Das"), "ExtraBold", 40),
    peep_voll("LI_denkt", FX, BR, FR, "ein", bis=beim("ein", "verbietet")),
    peep_voll("LI_muede", FX, BR, FR, beim("ein", "verbietet"), anim="cut"),
    ficon("tabler", "file-text", FX - 110, 290, 120, beim("ein", "Satzung"), fuell=WEISS),
    ficon("tabler", "truck-off", FX + 90, 290, 120, beim("ein", "verbietet"), fuell=ROT),
    pille("Parksatzung", FX - 110, 305, beim("ein", "Satzung"), fill=WEISS, size=28, anker="m"),
])

# I A. III. Rechtfertigung: Schranke, Zweck, Eignung ------------------------------------------------------------------------
PR = f"{PA} › III. Rechtfertigung"
folie([("rf", PR), ("schranke", f"{PR} › 1. Schranke, Art. 12 I 2 GG"), ("vhm", f"{PR} › 2. Verhältnismäßigkeit"),
       ("zweck", f"{PR} › 2. Verhältnismäßigkeit › legitimer Zweck"), ("geeignet", f"{PR} › 2. Verhältnismäßigkeit › geeignet")], [
    *tafel("rf", "A. III. Rechtfertigung", size=46),
    z("1. Schranke: „durch Gesetz oder auf Grund", 175, 190, "schranke", "Bold", 36),
    z("eines Gesetzes“, Art. 12 I 2 GG", 215, 240, beim("schranke", "Gesetzes"), "Bold", 36),
    z("Satzung auf Grund von Landesrecht", 215, 300, "lr", size=34, farbe=TEXT),
    z("(unterstellt: Grundlage trägt, formell rechtmäßig)", 215, 346, beim("lr", "Dass"), size=30, farbe=TEXT),
    z("2. Schranken-Schranke: Verhältnismäßigkeit", 175, 430, "vhm", "Bold", 36),
    ok(180, 525, "zweck", gr=20), z("a) legitimer Zweck: Spaziergänger, Wiesen", 215, 500, "zweck", size=34),
    ok(180, 590, "geeignet", gr=20), z("b) geeignet: keine Spuren, weniger Gefahr", 215, 565, "geeignet", size=34),
    z("Möglichkeit der Zweckerreichung genügt", 255, 618, beim("geeignet", "Das"), size=30, farbe=TEXT),
    peep_voll("LI_denkt", FX, BR, FR, "rf", bis="zweck"),
    pille("Lina", FX, BR + 22, "rf", fill=PINK, size=30, anker="m", bis="zweck"),
    ficon("tabler", "building-bank", FX, 300, 130, "schranke", fuell=GRAU, bis="vhm"),
    pille("Landesrecht", FX, 330, "lr", fill=WEISS, size=30, anker="m", bis="vhm"),
    ficon("tabler", "scale", FX, 300, 130, "vhm", fuell=GELB, bis="zweck"),
    # Zweck: Spaziergängerin und Wiese
    peep_voll("KR_froh", 1380, BR, FR - 40, "zweck"),
    peep_voll("LI_ruhig", 1730, BR, FR - 40, "zweck", anim="cut"),
    ficon("tabler", "plant", 1555, BR - 4, 110, "zweck", fuell=GRUEN),
    ficon("tabler", "truck-off", 1555, 300, 120, "geeignet", fuell=ROT),
])

# J A. III. Erforderlichkeit, Angemessenheit, Ergebnis A ------------------------------------------------------------------------
folie([("erf", f"{PR} › 2. Verhältnismäßigkeit › erforderlich"), ("angem", f"{PR} › 2. Verhältnismäßigkeit › angemessen"),
       ("erg1", f"{PA} › nicht verletzt")], [
    *tafel("erf", "A. III. 2. Verhältnismäßigkeit", size=46),
    ok(140, 220, "erf", gr=22), z("c) erforderlich: kein milderes,", 185, 195, "erf", "Bold", 36),
    z("gleich wirksames Mittel", 225, 245, beim("erf", "gleich"), "Bold", 36),
    nein(250, 330, beim("erf", "Fahrverbot"), gr=20), z("nur Wiesen sperren: Wege nicht geschützt", 285, 307, beim("erf", "Fahrverbot"), size=32, farbe=TEXT),
    ok(140, 430, "angem", gr=22), z("d) angemessen", 185, 405, "angem", "Bold", 36),
    z("regelt nur das Wo, nicht das Ob", 225, 465, beim("angem", "Das"), size=34, farbe=TEXT),
    z("Beruf bleibt, nur nicht im Park", 225, 513, beim("angem", "Sie"), size=34, farbe=TEXT),
    z("Sicherheit vieler Spaziergänger überwiegt", 225, 561, beim("angem", "Dem"), size=34, farbe=TEXT),
    fl_block(110, 660, 1040, 150, GRUEN, "erg1", [("Eingriff gerechtfertigt", "ExtraBold", 42, INK),
                                                ("Art. 12 I GG nicht verletzt", "Regular", 36, INK)]),
    peep_voll("LI_denkt", FX, BR, FR - 60, "erf", bis=beim("erf", "Fahrverbot")),
    # erforderlich: Alternative „nur Wiese gesperrt“ – Weg bleibt gefährlich
    fl_block(1290, 700, 250, 60, WIESE, beim("erf", "Fahrverbot"), [("Wiese", "Bold", 28, INK)], rand=4, bis="angem"),
    ficon("tabler", "truck-off", 1415, 680, 110, beim("erf", "Fahrverbot"), fuell=ROT, bis="angem"),
    fl_block(1560, 700, 300, 60, GRAU, beim("erf", "Spaziergänger"), [("Weg", "Bold", 28, INK)], rand=4, bis="angem"),
    ficon("tabler", "truck", 1640, 698, 170, beim("erf", "Spaziergänger"), fuell=BLAU, bis="angem"),
    peep_voll("KR_ruhig", 1800, 698, 300, beim("erf", "Wegen"), bis="angem"),
    # angemessen: Waage
    ficon("tabler", "scale", FX, 330, 170, "angem", fuell=GELB),
    pille("Lina: ein Standort", 1400, 400, beim("angem", "Sie"), fill=PINK, size=28, anker="m"),
    pille("viele Spaziergänger", 1735, 400, beim("angem", "Dem"), fill=LILA, size=28, anker="m"),
    peep_voll("LI_muede", FX, BR, FR - 60, "angem"),
])

# K B. Art. 3 I: Ungleichbehandlung -------------------------------------------------------------------------------------------
L3, B3 = 1400, 1740
folie([("gl", PB), ("vgl", f"{PB} › I. Ungleichbehandlung")], [
    *tafel("gl", "B. Gleichheit, Art. 3 I GG"),
    z("statt Schutzbereich und Eingriff: zwei Schritte", 110, 195, beim("gl", "Hier"), size=34, farbe=TEXT),
    z("I. Ungleichbehandlung wesentlich Gleicher?", 110, 280, "vgl", "Bold", 38),
    z("Vergleichsgruppe: Eisverkauf im Park", 150, 345, beim("vgl", "Bilde"), size=34, farbe=TEXT),
    z("Lina und der Kiosk verkaufen beide Eis", 150, 393, beim("vgl", "Lina"), size=34, farbe=TEXT),
    ok(140, 495, "ungl", gr=24), z("Kiosk darf, Lina nicht: Ungleichbehandlung", 185, 470, "ungl", "Bold", 34),
    peep_voll("LI_denkt", L3, BR, FR - 40, "gl", bis="ungl"),
    peep_voll("LI_aerger", L3, BR, FR - 40, "ungl", anim="cut"),
    peep_voll("BR_ruhig", B3, BR, FR - 40, "gl", d=0.2, bis="ungl"),
    peep_voll("BR_froh", B3, BR, FR - 40, "ungl", anim="cut"),
    pille("Lina", L3, BR + 22, "gl", fill=PINK, size=30, anker="m"),
    pille("Kiosk", B3, BR + 22, "gl", fill=TUERKIS, size=30, anker="m"),
    pille("beide: Eis im Park", 1570, 150, beim("vgl", "Lina"), fill=GELB, size=32, anker="m"),
    ficon("tabler", "ice-cream", 1570, 330, 90, beim("vgl", "Eis"), fuell=GELB),
    kreuz_i(L3, 320, "ungl", gr=40), haken_i(B3, 320, "ungl", gr=36),
])

# L B. II. Rechtfertigung -------------------------------------------------------------------------------------------------------
P3 = f"{PB} › II. Rechtfertigung"
folie([("rf3", P3), ("mass", f"{P3} › Maßstab"), ("sachgrund", f"{P3} › Sachgrund"), ("erg2", f"{PB} › nicht verletzt")], [
    *tafel("rf3", "B. II. Rechtfertigung"),
    z("Sachgrund, angemessen zu Ziel und Ausmaß", 110, 195, beim("rf3", "Nötig"), "Bold", 36),
    z("der Ungleichbehandlung", 110, 245, beim("rf3", "Nötig"), "Bold", 36),
    z("Maßstab:", 110, 325, "mass", "Bold", 34),
    fl_block(110, 375, 330, 90, WEISS, beim("mass", "Willkürverbot"), [("Willkürverbot", "Bold", 32, INK)]),
    pfeil_ink(460, 420, 760, 420, beim("mass", "bis")),
    fl_block(780, 375, 370, 90, ORANGE, beim("mass", "strenger"), [("strenge VHM", "Bold", 32, INK)]),
    z("Berufsfreiheit berührt → strenger möglich", 110, 490, beim("mass", "Weil"), size=34, farbe=TEXT),
    ok(140, 590, "sachgrund", gr=22), z("Sachgrund: Kiosk steht fest, fährt weder", 185, 565, "sachgrund", "Bold", 34),
    z("über Wege noch über Wiesen", 225, 613, beim("sachgrund", "Er"), "Bold", 34),
    z("= genau das Ziel der Satzung", 225, 661, beim("sachgrund", "Genau"), size=34, farbe=TEXT),
    fl_block(110, 730, 1040, 110, GRUEN, "erg2", [("Ungleichbehandlung gerechtfertigt", "ExtraBold", 40, INK)]),
    ficon("tabler", "building-store", 1400, 560, 220, "rf3", fuell=TUERKIS),
    pille("Kiosk", 1400, 590, "rf3", fill=TUERKIS, size=30, anker="m"),
    ficon("tabler", "truck", 1730, 560, 240, "rf3", fuell=PINK),
    pille("Eiswagen", 1730, 590, "rf3", fill=PINK, size=30, anker="m"),
    ficon("tabler", "scale", 1565, 300, 140, "mass", fuell=GELB, bis="sachgrund"),
    pille("steht fest", 1400, 300, beim("sachgrund", "Der"), fill=GRUEN, size=32, anker="m"),
    pille("fährt", 1730, 300, beim("sachgrund", "Er"), fill=ORANGE, size=32, anker="m"),
    fl_block(1290, 700, 560, 70, WIESE, beim("sachgrund", "Wiesen"), [("Wege und Wiesen", "Bold", 28, INK)], rand=4),
])

# M Ergebnis und Gegenfall -------------------------------------------------------------------------------------------------------
folie([("ergebnis", "Ergebnis"), ("gegen", "Gegenfall · nur Eiswagen verboten")], [
    *tafel("ergebnis", "Ergebnis"),
    fl_block(110, 190, 1040, 150, GRUEN, ("ergebnis", 0.3), [("Keine Grundrechtsverletzung", "ExtraBold", 42, INK),
                                                           ("Art. 12 I GG (−) · Art. 3 I GG (−)", "Regular", 36, INK)]),
    z("Gegenfall: nur Eiswagen verboten,", 110, 410, "gegen", "ExtraBold", 38),
    z("Kaffeewagen fahren weiter", 150, 465, beim("gegen", "Kaffeewagen"), "Bold", 36),
    z("für Wege und Spaziergänger kein Unterschied", 150, 535, "gegen2", size=34, farbe=TEXT),
    nein(140, 640, beim("gegen2", "Findet"), gr=24), z("ohne anderen Sachgrund:", 185, 615, beim("gegen2", "Findet"), "Bold", 36),
    z("Art. 3 I GG verletzt", 185, 665, beim("gegen2", "ist"), "ExtraBold", 40),
    peep_voll("LI_muede", FX, BR, FR, "ergebnis", bis="gegen"),
    *eiswagen(1400, 600, 240, "gegen"),
    *eiswagen(1730, 600, 240, beim("gegen", "Kaffeewagen"), farbe=BLAU, ware="coffee", warefarbe=WEISS),
    bis_(kreuz_i(1400, 300, beim("gegen", "verbietet"), gr=44), None),
    bis_(haken_i(1730, 300, beim("gegen", "dürfen"), gr=40), None),
    ficon("tabler", "equal", 1565, 500, 80, "gegen2", fuell=GELB),
    fl_block(1290, 640, 560, 70, WIESE, "gegen2", [("dieselben Wege", "Bold", 28, INK)], rand=4),
])

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Prüfungsreihenfolge"), ("tipp2", "Klausurtipp · Art. 94 I Nr. 4a GG")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. speziellstes Freiheitsrecht", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("2. danach Art. 3 GG", 200, 252, beim("tipp", "danach"), "Bold", 36),
    z("Art. 2 I GG nur, wenn kein spezielleres passt", 215, 320, beim("tipp", "Artikel", 2), size=32, farbe=TEXT),
    ok(175, 445, "tipp2", gr=22), z("Rahmen oft: Verfassungsbeschwerde", 215, 420, "tipp2", "Bold", 34),
    z("heute Art. 94 I Nr. 4a GG", 215, 480, beim("tipp2", "Die"), "Bold", 34),
    z("§§ 13 Nr. 8a, 90 ff. BVerfGG", 215, 530, beim("tipp2", "Die"), size=32, farbe=TEXT),
    z("früher: Art. 93 I Nr. 4a GG", 215, 590, beim("tipp2", "Ältere"), size=32, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema -----------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Grundrechte prüfen", 110, 90, "sch", 54),
    z("A. Freiheitsrecht, z. B. Art. 12 I GG", K1, 190, "sA", "Bold", 38, rechts=1820),
    z("I. Schutzbereich: persönlich und sachlich", K2, 250, "sA1", size=36, farbe=TEXT, rechts=1820),
    z("II. Eingriff", K2, 302, "sA2", size=36, farbe=TEXT, rechts=1820),
    z("III. Verfassungsrechtliche Rechtfertigung", K2, 354, "sA3", size=36, farbe=TEXT, rechts=1820),
    z("1. Schranke (z. B. Gesetzesvorbehalt)", K3, 406, beim("sA3", "Schranke"), size=34, farbe=TEXT, rechts=1820),
    z("2. Schranken-Schranken, v. a. Verhältnismäßigkeit: legitimer Zweck, geeignet, erforderlich, angemessen",
      K3, 454, beim("sA3", "Schranken-Schranken"), size=32, farbe=TEXT, rechts=1820),
    z("B. Gleichheitsrecht, Art. 3 I GG", K1, 560, "sB", "Bold", 38, rechts=1820),
    z("I. Ungleichbehandlung wesentlich Gleicher (Vergleichsgruppen)", K2, 620, "sB1", size=36, farbe=TEXT, rechts=1820),
    z("II. Verfassungsrechtliche Rechtfertigung durch einen Sachgrund", K2, 672, "sB2", size=36, farbe=TEXT, rechts=1820),
    z("Maßstab: Willkürverbot bis strenge Verhältnismäßigkeit", K3, 724, beim("sB2", "Sachgrund"), size=32, farbe=TEXT, rechts=1820),
])

# P Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Freiheitsrechte fragen:", "a")], [("Darf der Staat so weit", 0)], [("eingreifen?", 0)]], 750, 310, 52, "merke",
                {"a": beim("merke", "Freiheitsrechte")}),
    *markertext([[("Gleichheitsrechte fragen:", "b")], [("Darf er ungleich behandeln?", 0)]], 750, 620, 48, "m2",
                {"b": beim("m2", "Gleichheitsrechte")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
