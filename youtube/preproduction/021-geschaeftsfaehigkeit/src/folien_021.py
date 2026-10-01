"""Folge 021 · Geschäftsfähigkeit Schema §§ 104 ff. BGB: Minderjährige im Vertrag – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Im Handyladen, B Am Abend zu Hause / Ritters Brief, C Sachverhalt,
D Anspruch und I. Einigung, E II. 1./2. Geschäftsunfähigkeit und beschränkte Geschäftsfähigkeit (Altersleiste),
F II. 3. lediglich rechtlicher Vorteil (Wortlautkarte § 107), G II. 4. Einwilligung, H II. 5. Taschengeld (Wortlautkarte
§ 110, Ratenleiste), I Gegenfall Kopfhörer, J II. 6. Genehmigung (§ 108 I, § 184), K Aufforderung (Wortlautkarte
§ 108 II, Zwei-Wochen-Leiste), L Widerruf (§ 109, § 131 II), M III. Ergebnis und Ausblick §§ 112, 113, N Klausurtipp
(Lexi), O Klausurschema, P Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Anzahlung auf der Theke, Umschlag
von Ritters Brief öffnet sich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_021/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (205, 205, 210, 255)
THEKE = (226, 236, 252, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def block(x, y, w, h, fill, cue, text, size=38, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(text), "ExtraBold", size, INK)], **k)


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de) in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 22, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def bis_(el, bis):
    el.bis = bis
    return el


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2

# A Fall: im Handyladen -------------------------------------------------------------------------------------------------
FX, RX = 380, 1560                      # Frieda links (blickt nach rechts), Ritter rechts hinter der Theke
TX0, TX1, TY = 780, 1300, 640           # Ladentheke
folie([(NULL, "Fall · Im Handyladen")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Handyladen Ritter", (TX0 + TX1) / 2, 60, NULL, fill=BLAU, size=40, anker="m"),
    karte(TX0, TY, TX1 - TX0, BODEN - TY, NULL, fill=THEKE, rund=14, schatten=6),
    peep_voll("FR_ruhig_r", FX, BODEN, FH, NULL, bis="f1"),
    namensschild("Frieda", FX, BODEN, NULL, GRUEN),
    pl("15 Jahre", FX, 300, beim("fall", "fünfzehn"), fill=GELB, size=32, anker="m", bis="f1"),
    peep_voll("RI_ruhig", RX, BODEN, FH, beim("laden", "Herrn"), anim="fade", bis="r1"),
    namensschild("Herr Ritter", RX, BODEN, beim("laden", "Herrn"), BLAU),
    # das Smartphone in der Auslage
    ficon("tabler", "device-mobile", 1040, TY - 4, 90, beim("laden", "Smartphone"), fuell=WEISS, bis="r1"),
    pl("600 €", 1170, 380, beim("laden", "sechshundert"), fill=GELB, size=40, anker="m", bis="anz"),
    pl("sonst 800 €", 1170, 300, beim("laden", "achthundert"), fill=WEISS, size=30, anker="m", bis="anz"),
    *redet("FR_redet_r", FX, BODEN, FH, "f1", "anz"),
    blase("sprech", 640, 180, "f1", 720, 280, inhalt=["Sechshundert statt achthundert?", "Das nehme ich!"], textsize=32,
          figur=("FR_redet_r", FX, BODEN, FH), bis="anz"),
    peep_voll("FR_froh_r", FX, BODEN, FH, "anz", anim="cut", bis="weiss"),
    # Anzahlung: der Geldschein wandert auf die Theke
    szene(bewegt(ficon("tabler", "cash-banknote", 900, TY - 4, 110, beim("anz", "zahlt"), fuell=GRUEN),
                 beim("anz", "zahlt"), beim("anz", "sofort", ende=True), FX + 110 - 900, -120),
          "021muenzen*", 0.9, round(bausteine._t(beim("anz", "sofort", ende=True)) - bausteine._t(beim("anz", "zahlt")) - 0.03, 3)),
    pl("100 € Anzahlung", 900, 470, beim("anz", "sofort", ende=True), fill=GRUEN, size=30, anker="m", bis="r1"),
    pl("aus Taschengeld", 900, 400, beim("anz", "Taschengeld"), fill=WEISS, size=28, anker="m", bis="r1"),
    pl("Rest: 5 Monatsraten", 1180, 300, beim("raten", "fünf"), fill=ORANGE, size=30, anker="m", bis="r1"),
    peep_voll("FR_ruhig_r", FX, BODEN, FH, "weiss", anim="cut", bis="r1"),
    pl("Ritter weiß: Frieda ist 15", RX, 300, beim("weiss", "weiß"), fill=GELB, size=28, anker="m", bis="r1"),
    pl("Eltern wissen nichts", FX, 300, beim("weiss", "Eltern"), fill=PINK, size=30, anker="m", bis="r1"),
    *redet("RI_redet", RX, BODEN, FH, "r1", "abend"),
    blase("sprech", 600, 170, "r1", 1100, 270, inhalt=["Abgemacht. Viel Spaß", "mit dem Handy!"], textsize=34,
          figur=("RI_redet", RX, BODEN, FH)),
    peep_voll("FR_froh_r", FX, BODEN, FH, "r1", anim="cut"),
    # Ritter gibt Frieda das Handy
    bewegt(ficon("tabler", "device-mobile", FX + 120, 640, 70, beim("r1", "Viel"), fuell=WEISS),
           beim("r1", "Viel"), beim("r1", "Handy", ende=True), 1040 - (FX + 120), TY - 4 - 640),
])

# B Fall: am Abend zu Hause, Ritters Brief ------------------------------------------------------------------------------
MX, FX, RX = 480, 960, 1640             # Mutter (blickt nach rechts), Frieda (blickt nach links), Ritter im Laden
TRENN = 1280
folie([("abend", "Fall · Am Abend zu Hause"), ("brief", "Fall · Ritters Brief"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "abend", breite=7, farbe=INK),
    pl("Am Abend", 70, 40, "abend", fill=GELB, size=44),
    ficon("tabler", "lamp", 150, BODEN - 4, 150, "abend", fuell=GELB),
    ficon("tabler", "sofa", 720, BODEN - 4, 260, "abend", fuell=LILA),
    peep_voll("MU_ruhig_r", MX, BODEN, FH, "abend", bis="mu1"),
    namensschild("Friedas Mutter", MX, BODEN, "abend", ROT),
    peep_voll("FR_froh", FX, BODEN, FH, "abend", bis="mu1"),
    namensschild("Frieda", FX, BODEN, "abend", GRUEN),
    ficon("tabler", "device-mobile", FX - 110, 650, 60, "abend", fuell=WEISS),
    pl("das neue Handy", FX - 250, 520, beim("abend", "neue"), fill=WEISS, size=28, anker="m", bis="mu1"),
    *redet("MU_redet_r", MX, BODEN, FH, "mu1", "brief"),
    blase("sprech", 620, 170, "mu1", 760, 190, inhalt=["Sechshundert Euro?", "Das genehmigen wir nicht!"], textsize=34,
          figur=("MU_redet_r", MX, BODEN, FH), bis="brief"),
    peep_voll("FR_sorge", FX, BODEN, FH, "mu1", anim="cut", bis="frage"),
    peep_voll("MU_ernst_r", MX, BODEN, FH, "brief", anim="cut", bis="schweigen"),
    # rechts: Ritter im Laden schreibt den Eltern
    linienzug([(TRENN, 230), (TRENN, BODEN)], beim("brief", "Ritter"), breite=5, farbe=GRAU),
    pl("im Laden", RX, 60, beim("brief", "Ritter"), fill=BLAU, size=30, anker="m"),
    pl("erfährt davon nichts", RX, 300, beim("brief", "Ritter"), fill=PINK, size=28, anker="m", bis=beim("brief", "schreibt")),
    peep_voll("RI_ernst", RX, BODEN, FH, beim("brief", "Ritter"), anim="fade", bis="frage"),
    namensschild("Herr Ritter", RX, BODEN, beim("brief", "Ritter"), BLAU),
    ficon("tabler", "pencil", RX - 170, 640, 80, beim("brief", "schreibt"), fuell=WEISS, bis="frage"),
    bewegt(ficon("tabler", "mail", MX + 200, 560, 90, beim("brief", "schreibt"), fuell=GELB,
                 bis=beim("brief", "Eltern", ende=True)),
           beim("brief", "schreibt"), beim("brief", "Eltern", ende=True), RX - 170 - (MX + 200), 0),
    szene(ficon("tabler", "mail-opened", MX + 200, 560, 90, beim("brief", "Eltern", ende=True), fuell=GELB, anim="cut"),
          "021umschlag*", 0.9, -0.08),
    pl("Aufforderung an die Eltern", MX + 280, 240, beim("brief", "fordert"), fill=GELB, size=28, anker="m", bis="frage"),
    pl("Genehmigen Sie den Kauf?", MX + 280, 310, beim("brief", "genehmigen"), fill=WEISS, size=28, anker="m",
       bis="frage"),
    peep_voll("MU_denkt_r", MX, BODEN, FH, "schweigen", anim="cut"),
    ficon("tabler", "message-off", MX - 200, 330, 80, "schweigen", fuell=WEISS),
    pl("keine Antwort", MX - 200, 200, beim("schweigen", "antworten"), fill=WEISS, size=30, anker="m"),
    peep_voll("FR_ueberlegt", FX, BODEN, FH, "frage", anim="cut"),
    peep_voll("RI_denkt", RX, BODEN, FH, "frage", anim="cut"),
    pl("Muss Frieda die restlichen 500 € zahlen?", 960, 140, "frage", fill=PINK, size=40, anker="m"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Die 15-jährige Frieda kauft im Handyladen von Herrn Ritter ein Smartphone für 600 Euro, das sonst 800 Euro "
    "kostet. 100 Euro zahlt sie sofort aus gespartem Taschengeld, das ihr die Eltern zur freien Verfügung geben; den "
    "Rest soll sie in fünf Monatsraten zahlen. Ritter weiß, dass Frieda 15 ist. Er übergibt und übereignet ihr das "
    "Handy sofort, ohne Eigentumsvorbehalt. Die Eltern wissen nichts von dem Kauf; Frieda behauptet auch nichts anderes.",
    "Am Abend sagt die Mutter, auch für den Vater, zu Frieda: „Das genehmigen wir nicht!“ Ritter erfährt davon nichts. "
    "Er fordert die Eltern per Brief auf, zu erklären, ob sie den Kauf genehmigen. Sie antworten nicht; zwei Wochen "
    "nach Empfang des Briefes ist nichts geschehen.",
    "(Frei erfundener Übungsfall.)",
], "Muss Frieda die restlichen 500 Euro zahlen?")

# D Anspruch und I. Einigung ----------------------------------------------------------------------------------------------
folie([("ansp", "Ritter gegen Frieda · § 433 Abs. 2 BGB"), ("einig", "I. Einigung · Angebot und Annahme"),
       ("wirk", "II. Wirksamkeit · Friedas Geschäftsfähigkeit")], rechts_frei([
    *tafel("ansp", "Ritter gegen Frieda: 500 €"),
    z("restlicher Kaufpreis", 110, 200, beim("ansp", "restlichen"), "Bold", 40),
    z("Anspruch: § 433 Abs. 2 BGB", 150, 260, beim("ansp", "Paragraf"), size=34),
    z("I. Einigung", 110, 350, "einig", "Bold", 38),
    ok(135, 430, beim("einig", "liegen"), gr=22), z("Angebot und Annahme liegen vor", 175, 410, beim("einig", "Angebot"), size=34),
    z("II. Wirksamkeit?", 110, 510, "wirk", "Bold", 38),
    block(110, 590, 1040, 110, GELB, beim("wirk", "Geschäftsfähigkeit"), "Friedas Geschäftsfähigkeit", size=40),
    ficon("tabler", "cash-banknote", MB, 380, 150, "ansp", fuell=GRUEN, bis="einig"),
    ficon("tabler", "file-text", MB, 380, 110, "einig", fuell=WEISS, anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "ansp", bis="wirk"),
    peep_voll("RI_denkt", X1, BR, FR, "wirk", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "ansp", d=0.2, bis="wirk"),
    peep_voll("FR_denkt", X2, BR, FR, "wirk", anim="cut"),
    namensschild("Ritter", X1, BR, "ansp", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "ansp", GRUEN, d=0.3),
]))

# E II. 1./2. Geschäftsunfähigkeit, beschränkte Geschäftsfähigkeit --------------------------------------------------------
AX0, AX7, AX18 = 110, 330, 1150         # Altersleiste: 0 Jahre, 7 Jahre, 18 Jahre
AY = 560
def alter_x(j):
    return AX7 + (AX18 - AX7) * (j - 7) / 11


folie([("p104", "II. Wirksamkeit › 1. geschäftsunfähig? §§ 104, 105 BGB"),
       ("p106", "II. Wirksamkeit › 2. beschränkt geschäftsfähig, § 106 BGB")], rechts_frei([
    *tafel("p104", "1. und 2. Geschäftsfähigkeit"),
    z("§ 104 BGB: geschäftsunfähig, wer noch nicht 7 ist", 110, 190, beim("p104", "Geschäftsunfähig"), "Bold", 34),
    z("oder wegen krankhafter Störung der Geistestätigkeit", 150, 245, "krank", size=32),
    z("dauerhaft nicht frei entscheiden kann", 150, 290, beim("krank", "dauerhaft"), size=32),
    z("§ 105 Abs. 1 BGB: Willenserklärung nichtig", 110, 360, "p105", "Bold", 34),
    fl_block(AX0, AY, AX7 - AX0, 90, ROT, beim("p104", "sieben"), [("unter 7", "ExtraBold", 32, INK)]),
    fl_block(AX7, AY, AX18 - AX7, 90, GELB, beim("p106", "minderjährig"), [("7 bis 17: minderjährig", "ExtraBold", 32, INK)]),
    z("Alter", AX0, AY - 55, beim("p104", "sieben"), size=28, farbe=TEXT),
    linienzug([(alter_x(15), AY - 30), (alter_x(15), AY + 110)], beim("p106", "fünfzehn"), breite=6, farbe=DROT),
    pl("Frieda: 15", alter_x(15), AY + 120, beim("p106", "fünfzehn"), fill=GRUEN, size=30, anker="m"),
    block(110, 760, 1040, 100, GRUEN, beim("p106", "beschränkt"), "§ 106 BGB: beschränkt geschäftsfähig", size=38),
    ficon("tabler", "baby-carriage", MB, 380, 120, beim("p104", "sieben"), fuell=PINK, bis="p106"),
    ficon("tabler", "school", MB, 380, 130, "p106", fuell=GELB, anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "p104"),
    peep_voll("FR_ruhig", X2, BR, FR, "p104", d=0.2, bis=beim("p106", "beschränkt")),
    peep_voll("FR_denkt", X2, BR, FR, beim("p106", "beschränkt"), anim="cut"),
    namensschild("Ritter", X1, BR, "p104", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "p104", GRUEN, d=0.3),
]))

# F II. 3. lediglich rechtlicher Vorteil, § 107 ----------------------------------------------------------------------------
folie([("p107", "II. Wirksamkeit › 3. lediglich rechtlicher Vorteil? § 107 BGB")], rechts_frei([
    *tafel("p107", "3. Lediglich rechtlicher Vorteil?"),
    *wortlaut(110, 180, 1040, 200, "p107w", [
        [("„Der Minderjährige bedarf zu einer Willenserklärung,", 0)],
        [("durch die er ", 0), ("nicht lediglich einen rechtlichen Vorteil", "a")],
        [("erlangt, der ", 0), ("Einwilligung", "b"), (" seines gesetzlichen Vertreters.“", 0)],
    ], 34, {"a": beim("p107w", "nicht"), "b": beim("p107w", "Einwilligung")}, "§ 107 BGB"),
    z("gesetzlicher Vertreter: Friedas Eltern", 110, 450, "eltern", "Bold", 34),
    z("Kaufvertrag: Pflicht, 600 € zu zahlen", 110, 530, "pflicht", "Bold", 34),
    *plusminus("rechtlicher Nachteil", 150, 585, beim("pflicht", "rechtlicher"), False, size=34),
    z("Schnäppchen? Spielt keine Rolle.", 110, 680, "schnapp", "Bold", 34),
    z("Es zählt die rechtliche Folge, nicht die wirtschaftliche.", 150, 735, beim("schnapp", "Es"), size=32),
    ficon("tabler", "users", MB, 380, 130, "eltern", fuell=ROT, bis="pflicht"),
    ficon("tabler", "receipt", MB, 380, 110, "pflicht", fuell=WEISS, anim="cut", bis="schnapp"),
    ficon("tabler", "discount", MB, 380, 110, "schnapp", fuell=GELB, anim="cut"),
    pl("600 €", MB, 160, "pflicht", fill=GELB, size=32, anker="m", bis="schnapp"),
    pl("statt 800 €", MB, 160, "schnapp", fill=WEISS, size=30, anker="m", anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "p107"),
    peep_voll("FR_ruhig", X2, BR, FR, "p107", d=0.2, bis="pflicht"),
    peep_voll("FR_sorge", X2, BR, FR, "pflicht", anim="cut"),
    namensschild("Ritter", X1, BR, "p107", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "p107", GRUEN, d=0.3),
]))

# G II. 4. Einwilligung ---------------------------------------------------------------------------------------------------
folie([("einw", "II. Wirksamkeit › 4. Einwilligung? §§ 107, 183 BGB")], rechts_frei([
    *tafel("einw", "4. Einwilligung der Eltern?"),
    z("Einwilligung = vorherige Zustimmung", 110, 200, beim("einw", "Einwilligung"), "Bold", 36),
    z("§ 183 S. 1 BGB", 150, 260, beim("einw", "Paragraf"), size=34),
    nein(135, 370, beim("keine", "nichts"), gr=22),
    z("Die Eltern wussten vom Kauf nichts", 175, 350, "keine", size=34),
    block(110, 460, 1040, 100, ROT, beim("keine", "Eine"), "Eine Einwilligung fehlt.", size=40),
    ficon("tabler", "user-check", MB, 380, 120, beim("einw", "vorherige"), fuell=WEISS, bis=beim("keine", "Eine")),
    ficon("tabler", "user-x", MB, 380, 120, beim("keine", "Eine"), fuell=WEISS, anim="cut"),
    peep_voll("MU_ruhig", X1, BR, FR, "einw", bis="keine"),
    peep_voll("MU_denkt", X1, BR, FR, "keine", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "einw", d=0.2),
    namensschild("Mutter", X1, BR, "einw", ROT, d=0.2),
    namensschild("Frieda", X2, BR, "einw", GRUEN, d=0.3),
]))

# H II. 5. Taschengeld, § 110 -----------------------------------------------------------------------------------------------
RX0, RW = 110, 160                      # Ratenleiste: Anzahlung + 5 Raten
folie([("p110", "II. Wirksamkeit › 5. Taschengeld? § 110 BGB")], rechts_frei([
    *tafel("p110", "5. Taschengeldparagraf"),
    *wortlaut(110, 170, 1040, 270, "p110w", [
        [("„Ein von dem Minderjährigen ohne Zustimmung des gesetzlichen", 0)],
        [("Vertreters geschlossener Vertrag gilt als ", 0), ("von Anfang an wirksam,", "a")],
        [("wenn der Minderjährige die vertragsmäßige Leistung mit Mitteln", 0)],
        [("bewirkt,", "b"), (" die ihm ", 0), ("zu diesem Zweck oder zu freier Verfügung", "c")],
        [("… überlassen worden sind.“", 0)],
    ], 29, {"a": beim("p110w", "Anfang"), "b": beim("p110w", "bewirkt"), "c": beim("p110w", "Zweck")}, "§ 110 BGB"),
    *[fl_block(RX0 + i * (RW + 15), 510, RW, 80, GRUEN if i == 0 else WEISS,
               beim("nur", "Anzahlung") if i == 0 else beim("nur", "Fünfhundert"),
               [("100 €", "ExtraBold", 30, INK)]) for i in range(6)],
    z("Anzahlung", RX0 + 10, 600, beim("nur", "Anzahlung"), size=26, farbe=TEXT),
    pl("500 € offen", RX0 + 3 * (RW + 15) + RW / 2, 610, beim("nur", "Fünfhundert"), fill=ORANGE, size=28, anker="m"),
    z("Ratenkauf: bewirkt erst mit der letzten Rate", 110, 690, "rate", "Bold", 34),
    nein(RX0 + 5 * (RW + 15) + RW / 2, 628, beim("rate", "letzten"), gr=24),
    block(110, 760, 1040, 100, ROT, beim("rate", "Bis"), "Bis dahin hilft § 110 BGB nicht.", size=38),
    ficon("tabler", "pig-money", MB, 380, 130, "p110", fuell=PINK),
    peep_voll("RI_ruhig", X1, BR, FR, "p110"),
    peep_voll("FR_ruhig", X2, BR, FR, "p110", d=0.2, bis="nur"),
    peep_voll("FR_sorge", X2, BR, FR, "nur", anim="cut"),
    namensschild("Ritter", X1, BR, "p110", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "p110", GRUEN, d=0.3),
]))

# I Gegenfall: Kopfhörer, sofort bezahlt -----------------------------------------------------------------------------------
folie([("kopf", "Gegenfall · Kopfhörer, sofort bezahlt")], rechts_frei([
    *tafel("kopf", "Gegenfall: Kopfhörer"),
    z("Kopfhörer für 40 €", 110, 200, beim("kopf", "Kopfhörern"), "Bold", 38),
    ok(135, 290, beim("kopf", "Taschengeld"), gr=22),
    z("sofort von ihrem Taschengeld bezahlt", 175, 270, beim("kopf", "sofort"), size=34),
    block(110, 380, 1040, 110, GRUEN, "kopf_ok", "Von Anfang an wirksam, § 110 BGB", size=40),
    ficon("tabler", "headphones", MB, 380, 130, beim("kopf", "Kopfhörern"), fuell=LILA),
    pl("40 €", MB, 160, beim("kopf", "vierzig"), fill=GELB, size=32, anker="m"),
    bewegt(ficon("tabler", "cash-banknote", X1 + 120, 650, 80, beim("kopf", "bezahlt"), fuell=GRUEN),
           beim("kopf", "bezahlt"), beim("kopf", "bezahlt", ende=True), X2 - X1 - 240, 0),
    peep_voll("RI_ruhig", X1, BR, FR, "kopf", bis="kopf_ok"),
    peep_voll("RI_froh", X1, BR, FR, "kopf_ok", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "kopf", d=0.2, bis="kopf_ok"),
    peep_voll("FR_froh", X2, BR, FR, "kopf_ok", anim="cut"),
    namensschild("Ritter", X1, BR, "kopf", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "kopf", GRUEN, d=0.3),
]))

# J II. 6. Genehmigung, § 108 I, § 184 ---------------------------------------------------------------------------------------
folie([("p108", "II. Wirksamkeit › 6. Genehmigung, § 108 Abs. 1 BGB")], rechts_frei([
    *tafel("p108", "6. Genehmigung der Eltern"),
    z("§ 108 Abs. 1 BGB: Ohne Einwilligung hängt die", 110, 200, beim("schwebe", "Ohne"), "Bold", 34),
    z("Wirksamkeit von der Genehmigung der Eltern ab", 110, 250, beim("schwebe", "Genehmigung"), "Bold", 34),
    block(110, 330, 1040, 110, GELB, beim("schwebe", "schwebend"), "schwebend unwirksam", size=42),
    z("Genehmigung wirkt zurück auf den Vertragsschluss,", 110, 510, "rueck", size=34),
    z("§ 184 Abs. 1 BGB", 150, 565, beim("rueck", "Paragraf"), size=34),
    ficon("tabler", "hourglass", MB, 380, 110, beim("schwebe", "schwebend"), fuell=GELB, bis="rueck"),
    ficon("tabler", "arrow-back-up", MB, 380, 110, "rueck", fuell=WEISS, anim="cut"),
    peep_voll("MU_ruhig", X1, BR, FR, "p108"),
    peep_voll("FR_ruhig", X2, BR, FR, "p108", d=0.2, bis=beim("schwebe", "schwebend")),
    peep_voll("FR_ueberlegt", X2, BR, FR, beim("schwebe", "schwebend"), anim="cut"),
    namensschild("Mutter", X1, BR, "p108", ROT, d=0.2),
    namensschild("Frieda", X2, BR, "p108", GRUEN, d=0.3),
]))

# K Aufforderung, § 108 II ------------------------------------------------------------------------------------------------
WX0, WX1 = 200, 1000                    # Zwei-Wochen-Leiste
folie([("verw", "II. Wirksamkeit › 6. Aufforderung, § 108 Abs. 2 BGB")], rechts_frei([
    *tafel("verw", "Ritters Aufforderung"),
    z("Mutter verweigert nur gegenüber Frieda", 110, 180, beim("verw", "Mutter"), "Bold", 34),
    *wortlaut(110, 240, 1040, 268, "auff", [
        [("„Fordert der andere Teil den Vertreter zur Erklärung über die", 0)],
        [("Genehmigung auf, so kann die Erklärung ", 0), ("nur ihm gegenüber", "b"), (" erfolgen;", 0)],
        [("eine vor der Aufforderung dem Minderjährigen gegenüber erklärte", 0)],
        [("… Verweigerung der Genehmigung ", 0), ("wird unwirksam.", "a"), (" Die Genehmigung", 0)],
        [("kann nur bis zum Ablauf von ", 0), ("zwei Wochen", "c"), (" nach dem Empfang der", 0)],
        [("Aufforderung erklärt werden; wird sie nicht erklärt, so ", 0), ("gilt sie als verweigert.“", "d")],
    ], 26, {"a": beim("auff", "unwirksam"), "b": beim("nurihm", "ihm"), "c": beim("zwei", "zwei"),
            "d": beim("fikt", "verweigert")}, "§ 108 Abs. 2 BGB"),
    linienzug([(WX0, 610), (WX1, 610)], "zwei", breite=6, farbe=INK),
    pl("Empfang", WX0, 640, "zwei", fill=GELB, size=26, anker="m"),
    pl("+ 2 Wochen", WX1, 640, beim("zwei", "Wochen"), fill=ROT, size=26, anker="m"),
    pl("Eltern schweigen", (WX0 + WX1) / 2, 560, beim("fikt", "schweigen"), fill=WEISS, size=26, anker="m"),
    block(110, 730, 1040, 100, ROT, beim("fikt", "Damit"), "Die Genehmigung gilt als verweigert.", size=38),
    ficon("tabler", "mail", X2 - 150, 600, 80, "auff", fuell=GELB, bis="fikt"),
    ficon("tabler", "calendar-event", MB, 380, 110, "zwei", fuell=WEISS, bis="fikt"),
    ficon("tabler", "message-off", MB, 380, 100, "fikt", fuell=WEISS, anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "verw", bis="fikt"),
    peep_voll("RI_sorge", X1, BR, FR, "fikt", anim="cut"),
    peep_voll("MU_ruhig", X2, BR, FR, "verw", d=0.2, bis="nurihm"),
    peep_voll("MU_denkt", X2, BR, FR, "nurihm", anim="cut"),
    namensschild("Ritter", X1, BR, "verw", BLAU, d=0.2),
    namensschild("Mutter", X2, BR, "verw", ROT, d=0.3),
]))

# L Widerruf, § 109, Zugang § 131 II -----------------------------------------------------------------------------------------
folie([("p109", "II. Wirksamkeit › 6. Widerruf? § 109 BGB")], rechts_frei([
    *tafel("p109", "Darf Ritter widerrufen?"),
    z("§ 109 Abs. 1 BGB: Widerruf bis zur Genehmigung", 110, 190, beim("p109", "Bis"), "Bold", 34),
    z("sogar gegenüber Frieda selbst", 150, 245, "p109s", size=34),
    z("sonst Zugang erst bei den Eltern, § 131 Abs. 2 BGB", 150, 300, beim("p131", "erst"), size=32, farbe=TEXT),
    z("§ 109 Abs. 2 BGB: Ritter kannte Friedas Alter", 110, 400, beim("kannte", "Ritter"), "Bold", 34),
    z("Widerruf nur, wenn sie wahrheitswidrig behauptet", 150, 455, beim("kannte", "Dann"), size=32),
    z("hätte, die Eltern seien einverstanden", 150, 500, beim("kannte", "ihre"), size=32),
    nein(175, 590, "nicht", gr=22), z("Das hat sie nicht: kein Widerruf", 215, 570, "nicht", size=34),
    ficon("tabler", "arrow-back-up", MB, 360, 100, beim("p109", "widerrufen"), fuell=WEISS, bis="p131"),
    ficon("tabler", "mail", MB, 360, 90, "p131", fuell=GELB, anim="cut", bis="kannte"),
    pl("an die Eltern", MB, 160, "p131", fill=ROT, size=28, anker="m", bis="kannte"),
    pl("15 Jahre", MB, 300, beim("kannte", "minderjährig"), fill=GELB, size=30, anker="m"),
    peep_voll("RI_ruhig", X1, BR, FR, "p109", bis="kannte"),
    peep_voll("RI_denkt", X1, BR, FR, "kannte", anim="cut", bis="nicht"),
    peep_voll("RI_sorge", X1, BR, FR, "nicht", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "p109", d=0.2),
    namensschild("Ritter", X1, BR, "p109", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "p109", GRUEN, d=0.3),
]))

# M III. Ergebnis und Ausblick §§ 112, 113 ------------------------------------------------------------------------------------
folie([("erg", "III. Ergebnis · Vertrag endgültig unwirksam"), ("aus", "Ausblick · §§ 112, 113 BGB")], rechts_frei([
    *tafel("erg", "III. Ergebnis"),
    block(110, 190, 1040, 100, ROT, beim("erg", "Der"), "Kaufvertrag endgültig unwirksam", size=40),
    nein(135, 360, beim("erg", "nicht"), gr=22), z("Ritter kann die 500 € nicht verlangen", 175, 340, beim("erg", "Ritter"), size=34),
    z("Rückgabe von Handy und Anzahlung: eigene Frage", 110, 420, "rabw", size=32, farbe=TEXT),
    z("Nur am Rande:", 110, 520, "aus", "Bold", 34),
    z("§ 112 BGB: Erwerbsgeschäft, mit Genehmigung des", 150, 575, beim("aus", "Erwerbsgeschäft"), size=32),
    z("Familiengerichts", 150, 620, beim("aus", "Familiengerichts"), size=32),
    z("§ 113 BGB: Dienst oder Arbeit", 150, 680, beim("p113", "Dienst"), size=32),
    z("dafür unbeschränkt geschäftsfähig", 150, 750, beim("p113", "unbeschränkt"), "Bold", 34),
    ficon("tabler", "building-store", MB, 380, 130, beim("aus", "Erwerbsgeschäft"), fuell=BLAU, bis="p113"),
    ficon("tabler", "briefcase", MB, 380, 120, "p113", fuell=GELB, anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "erg", bis=beim("erg", "Ritter")),
    peep_voll("RI_sorge", X1, BR, FR, beim("erg", "Ritter"), anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "erg", d=0.2, bis=beim("erg", "Ritter")),
    peep_voll("FR_froh", X2, BR, FR, beim("erg", "Ritter"), anim="cut"),
    namensschild("Ritter", X1, BR, "erg", BLAU, d=0.2),
    namensschild("Frieda", X2, BR, "erg", GRUEN, d=0.3),
]))

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Verpflichtung und Verfügung trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne Verpflichtung und Verfügung.", 200, 200, beim("tipp", "Trenne"), "Bold", 38),
    fl_block(110, 310, 500, 110, ROT, "tipp2", [("Kaufvertrag", "ExtraBold", 38, INK)]),
    *plusminus("rechtlich nachteilig", 130, 440, beim("tipp2", "nachteilig"), False, size=32),
    fl_block(650, 310, 500, 110, GRUEN, "tipp3", [("Übereignung", "ExtraBold", 38, INK)]),
    z("des Handys: nur Eigentum,", 670, 440, beim("tipp3", "Eigentum"), size=32),
    z("keine Pflicht", 670, 485, beim("tipp3", "keine"), size=32),
    *plusminus("lediglich rechtlich vorteilhaft", 110, 590, "tipp4", True, size=36, stil="Bold"),
    z("keine Einwilligung nötig", 150, 650, beim("tipp4", "keine"), size=34),
    *redet("LX_warnt", LXX, BR, 560, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema -----------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Ritter gegen Frieda, § 433 Abs. 2 BGB", 110, 90, "sch", 46),
    z("I. Einigung (Angebot und Annahme)", K1, 195, "k1", "Bold", 38, rechts=1820),
    z("II. Wirksamkeit: Geschäftsfähigkeit", K1, 265, "k2", "Bold", 38, rechts=1820),
    z("1. geschäftsunfähig? §§ 104, 105 BGB", K2, 325, "k2a", size=34, rechts=1820),
    z("2. beschränkt geschäftsfähig, § 106 BGB", K2, 380, "k2b", size=34, rechts=1820),
    z("3. lediglich rechtlicher Vorteil? § 107 BGB", K2, 435, "k2c", size=34, rechts=1820),
    z("4. Einwilligung? §§ 107, 183 BGB", K2, 490, "k2d", size=34, rechts=1820),
    z("5. Taschengeld? § 110 BGB", K2, 545, "k2e", size=34, rechts=1820),
    z("6. Genehmigung, §§ 108, 184 BGB", K2, 600, "k2f", size=34, rechts=1820),
    z("samt Aufforderung (§ 108 Abs. 2 BGB) und Widerruf (§ 109 BGB)", K2 + 40, 650, beim("k2f", "samt"), size=32,
      farbe=TEXT, rechts=1820),
    z("III. Ergebnis", K1, 730, "k3", "Bold", 38, rechts=1820),
])

# P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Was eine Minderjährige verpflichtet,", 0)],
                 [("braucht die ", 0), ("Zustimmung ihrer Eltern,", "a")]], 750, 320, 44, "merke",
                {"a": beim("merke", "Zustimmung")}),
    *markertext([[("vorher als ", 0), ("Einwilligung", "b"), (" oder nachher als ", 0), ("Genehmigung.", "c")]],
                750, 480, 40, "m2", {"b": beim("m2", "Einwilligung"), "c": beim("m2", "Genehmigung")}),
    *markertext([[("Der Taschengeldparagraf hilft nur, wenn sie", 0)],
                 [("mit überlassenem Geld ", 0), ("schon alles bezahlt", "d"), (" hat.", 0)]], 750, 600, 40, "m3",
                {"d": beim("m3", "schon")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
