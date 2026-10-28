"""Folge 107 · Computerbetrug § 263a: Fremde Karte am Geldautomaten – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Flur der WG (Karte aus der Geldbörse), A2 Geldautomat an der Ecke, A3 Flur (Karte zurück,
nächster Morgen, Frage), B Sachverhalt, C Wortlaut § 263a Abs. 1 und Struktur, D Tathandlung (Variante 3), E drei
Auslegungen von „unbefugt“, F Probe mit der gedachten Bankangestellten, G Beeinflussung, H Vermögensschaden, I subjektiver
Tatbestand und Ergebnis zu § 263a, J § 242 am Geld (Wortlaut auszugsweise, Gewahrsam), K Streit, L § 242 an der Karte,
M Ergebnis und Konkurrenzen, N Klausurtipp (Lexi), O Prüfschema, P Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/wortlaut/redet/rechts_frei als eigene Kopie aus den Folgen 065/106 (gemeinsame Dateien
unverändert). Namensschild jeder Figur, solange sie im Bild ist. Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Keine realen Banknamen oder Logos: Geldautomat aus Karten und Tabler-Icons gebaut, Bank als Tabler building-bank.
Geräusche nur bei sichtbarer Handlung: Karte in den Schlitz, Geldausgabe (Freesound CC0, ../geraeusche_herkunft.json)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_107/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (205, 205, 210, 255)
HOLZ = (214, 160, 110, 255)
METALL = (226, 229, 236, 255)
SCHIRM = (214, 228, 252, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t
NULL = ("fall", -round(T_("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobil: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein für mobile Lesbarkeit: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def bis_(el, bis):
    el.bis = bis
    return el


def kb(*a, bis=None, **k):
    """Karte mit Ende (karte() kennt kein bis)."""
    return bis_(karte(*a, **k), bis)


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


def okz(text, y, cue, stil="Regular", size=32, x=175, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 40, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=32, x=175, gr=18, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 40, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=28, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 30 + lh * len(zeilen) + 44
    els = [kb(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4, bis=bis)]
    f = F("Regular", size)
    tx, ty = x + 26, y + 20
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
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 12, bis=bis))
    q = z(quelle, 0, 0, cue, "Bold", 26, farbe=TEXT, bis=bis)
    q.x = x + w - q.sprite.width - 24; q.y = ty + len(zeilen) * lh + 4
    els.append(q)
    return els, y + hgt


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_107/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def tafelicon(e):
    """Icon als Teil der Tafel (nicht rechts_frei-pflichtig)."""
    e.name = "tafel" + (e.name or "")
    return e


def namensschild(text, cx, unten, cue, fill, **k):
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 062/065/106) ------------------------------
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # Meike (näher an der Tafel), Heiko
MB = (X1 + X2) // 2
FM = ("Meike", LILA)
FHk = ("Heiko", GRUEN)


def paar(cue, mk, he, mk_cues=(), he_cues=()):
    """Meike (X1) und Heiko (X2) neben der Tafel mit Namensschild; *_cues = [(Cue, Ansicht)] für Mimikwechsel."""
    els = []
    for x, basis, wechsel, (name, farbe), dd in ((X1, mk, mk_cues, FM, 0.0), (X2, he, he_cues, FHk, 0.2)):
        folge = [(cue, basis)] + list(wechsel)
        for i, (c, ans) in enumerate(folge):
            bis = folge[i + 1][0] if i + 1 < len(folge) else None
            els.append(peep_voll(ans, x, BR, FR, c, anim=("fade" if i == 0 else "cut"), d=(dd if i == 0 else 0.0), bis=bis))
        els.append(namensschild(name, x, BR, cue, farbe, d=dd + 0.2))
    return els


def symbol(sets, name, c, bis=None, fuell=None, breite=100, anim="pop", y=380):
    return ficon(sets, name, MB, y, breite, c, fuell=fuell, bis=bis, anim=anim)


def mpille(text, c, bis=None, fill=WEISS, size=30, anim="pop", y=160):
    return pl(text, MB, y, c, fill=fill, size=size, anker="m", bis=bis, anim=anim)


def karte_icon(cx, unten, cue, breite=80, bis=None, anim="pop"):
    """Bankkarte ohne Logo (Fluent Emoji credit-card)."""
    return ficon("fluent-emoji-flat", "credit-card", cx, unten, breite, cue, bis=bis, anim=anim)


# --- Kulisse Flur der WG ------------------------------------------------------------------------------------------------
def flur(cue, kx=820, tuer=True):
    """Boden, Badezimmertür (links), Kommode mit Geldbörse."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)]
    if tuer:
        els.append(ficon("tabler", "door", 260, BODEN - 2, 290, cue, fuell=HOLZ))
    els += [karte(kx - 130, 690, 260, 186, cue, fill=HOLZ, rund=12, schatten=6, rand=5),
            linienzug([(kx - 110, 780), (kx + 110, 780)], cue, breite=4, farbe=INK)]
    return els


KX = 820                                    # Kommode
TOP = 690                                   # Oberkante Kommode
HX1 = 1180                                  # Heiko im Flur (blickt nach links zur Kommode)
HAND = (HX1 - 70, 700)                      # ungefähre Handhöhe (Karte, Geld)

# A1 Fall: Karte aus der Geldbörse --------------------------------------------------------------------------------------
HEd = ("HE_denkt", HX1, BODEN, FH)
HEr = ("HE_redet", HX1, BODEN, FH)
karte_weg = bewegt(karte_icon(HAND[0], HAND[1], beim("nimmt", "heimlich"), breite=80, anim="cut"), beim("nimmt", "heimlich"),
                   beim("nimmt", "Bankkarte", ende=True), KX - HAND[0], TOP - 6 - HAND[1])
folie([(NULL, "Fall · Die Karte im Flur")], [
    *flur(NULL),
    pl("Freitagabend: die Wohngemeinschaft", 70, 40, NULL, fill=GELB, size=40),
    peep_voll("HE_ruhig", HX1, BODEN, FH, NULL, bis="heiko"),
    namensschild("Heiko", HX1, BODEN, NULL, GRUEN),
    peep_voll("HE_denkt", HX1, BODEN, FH, "heiko", anim="cut", bis="h1"),
    blase("denk", 360, 220, beim("heiko", "kennt"), HX1 - 20, 225, inhalt=[" ", "Geheimzahl"], textsize=30, figur=HEd,
          bis="nimmt"),
    ficon("tabler", "password", HX1 - 20, 222, 90, beim("heiko", "kennt"), bis="nimmt"),
    pl("beim Einkaufen gesehen", 1570, 340, beim("heiko", "Einkaufen"), fill=WEISS, size=28, anker="m", bis="nimmt"),
    # Meike unter der Dusche, Geldbörse im Flur
    ficon("fluent-emoji-flat", "shower", 260, 520, 110, "dusche", bis=None),
    pl("Meike unter der Dusche", 260, 330, beim("dusche", "Meike"), fill=LILA, size=28, anker="m"),
    ficon("tabler", "wallet", KX, TOP, 110, beim("dusche", "Geldbörse"), fuell=GELB),
    pl("Geldbörse im Flur", KX, 560, beim("dusche", "Geldbörse"), fill=WEISS, size=28, anker="m"),
    # Heiko nimmt heimlich die Karte
    karte_weg,
    pl("heimlich", 960, 300, beim("nimmt", "heimlich"), fill=ROTHELL, size=32, anker="m"),
    *redet("HE_redet", HX1, BODEN, FH, "h1", "automat"),
    blase("sprech", 520, 200, "h1", 880, 250, inhalt=["Die Karte lege ich", "gleich wieder zurück."], textsize=34, figur=HEr),
])

# A2 Fall: am Geldautomaten ----------------------------------------------------------------------------------------------
AX = 760                                     # Mitte Geldautomat
SCHLITZ = (AX, 655)
FACH = (AX, 770)
HX2 = 1200
HAND2 = (HX2 - 75, 700)
karte_rein = szene(bewegt(karte_icon(SCHLITZ[0], SCHLITZ[1] - 6, beim("automat", "steckt"), breite=70, anim="cut", bis="geld"),
                          beim("automat", "steckt"), beim("automat", "Karte", ende=True), HAND2[0] - SCHLITZ[0],
                          HAND2[1] - SCHLITZ[1]), "107karte*", 1.0, versatz=round(T_(beim("automat", "Karte", ende=True)) -
                                                                                   T_(beim("automat", "steckt")) - 0.1, 3))
geld_raus = szene(bewegt(ficon("fluent-emoji-flat", "euro-banknote", HAND2[0], HAND2[1] - 35, 90, beim("geld", "zahlt"), anim="cut"),
                         beim("geld", "zahlt"), beim("geld", "aus", ende=True), FACH[0] - HAND2[0], FACH[1] + 55 - HAND2[1]),
                  "107geld*", 0.8, versatz=-0.15)
folie([("automat", "Fall · Am Geldautomaten")], [
    linienzug([(60, BODEN), (1860, BODEN)], "automat", breite=7, farbe=INK),
    pl("Am Geldautomaten an der Ecke", 70, 40, "automat", fill=GELB, size=40),
    karte(AX - 170, 250, 340, 626, "automat", fill=METALL, rund=20, schatten=8, rand=5),
    karte(AX - 130, 290, 260, 170, "automat", fill=SCHIRM, rund=12, schatten=0, rand=4),
    pl("Geldautomat", AX, 165, "automat", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "dialpad", AX, 585, 100, "automat", fuell=WEISS, bis="pin"),
    ficon("tabler", "dialpad", AX, 585, 100, "pin", fuell=GELB, anim="cut", bis="geld"),
    ficon("tabler", "dialpad", AX, 585, 100, "geld", fuell=WEISS, anim="cut"),
    linienzug([(AX - 90, SCHLITZ[1]), (AX + 90, SCHLITZ[1])], "automat", breite=8, farbe=INK),
    linienzug([(AX - 120, FACH[1]), (AX + 120, FACH[1])], "automat", breite=10, farbe=INK),
    peep_voll("HE_ruhig", HX2, BODEN, FH, "automat", anim="fade", bis="pin"),
    namensschild("Heiko", HX2, BODEN, "automat", GRUEN),
    karte_rein,
    # Geheimzahl, Betrag, Auszahlung
    peep_voll("HE_ernst", HX2, BODEN, FH, "pin", anim="cut", bis="geld"),
    ficon("tabler", "password", AX, 372, 100, beim("pin", "Geheimzahl"), bis="betrag"),
    z("Geheimzahl", AX - 78, 390, beim("pin", "Geheimzahl"), "Bold", 28, rechts=1700, bis="betrag"),
    z("500 €", AX - 70, 335, beim("betrag", "fünfhundert"), "ExtraBold", 50, rechts=1700, bis="geld"),
    z("Auszahlung", AX - 92, 345, "geld", "Bold", 36, rechts=1700),
    peep_voll("HE_eifrig", HX2, BODEN, FH, "geld", anim="cut"),
    geld_raus,
    karte_icon(HAND2[0], HAND2[1] + 35, "geld", breite=70, anim="cut"),
    pl("500 €", 1000, 520, beim("geld", "aus"), fill=GRUEN, size=32, anker="m"),
])

# A3 Fall: Karte zurück, nächster Morgen, die Frage ---------------------------------------------------------------------
KX3 = 600
HX3 = 940
HAND3 = (HX3 - 70, 700)
MX = 1520
MKr = ("MK_redet", MX, BODEN, FH)
karte_zurueck = bewegt(karte_icon(KX3 + 20, TOP - 8, beim("zurueck", "legt"), breite=70, anim="cut", bis="morgen"),
                       beim("zurueck", "legt"), beim("zurueck", "zurück", ende=True), HAND3[0] - KX3 - 20, HAND3[1] - TOP + 8)
folie([("zurueck", "Fall · Die Karte zurück"), ("morgen", "Fall · Der nächste Morgen"), ("frage", "Fall · Die Frage")], [
    *flur("zurueck", kx=KX3, tuer=False),
    pl("Zu Hause", 70, 40, "zurueck", fill=GELB, size=40, bis="morgen"),
    ficon("tabler", "wallet", KX3, TOP, 110, "zurueck", fuell=GELB),
    peep_voll("HE_ruhig", HX3, BODEN, FH, "zurueck", anim="fade", bis="morgen"),
    namensschild("Heiko", HX3, BODEN, "zurueck", GRUEN, bis="morgen"),
    karte_zurueck,
    pl("unbemerkt zurück", KX3, 560, beim("zurueck", "unbemerkt"), fill=WEISS, size=28, anker="m", bis="morgen"),
    # Der nächste Morgen: Meike sieht die Kontoumsätze
    pl("Am nächsten Morgen", 70, 40, "morgen", fill=GELB, size=40, anim="cut"),
    ficon("fluent-emoji-flat", "sunrise", 1760, 200, 120, "morgen"),
    peep_voll("MK_ruhig", MX, BODEN, FH, "morgen", anim="fade", bis=beim("morgen", "Kontoumsätze")),
    namensschild("Meike", MX, BODEN, "morgen", LILA),
    peep_voll("MK_denkt", MX, BODEN, FH, beim("morgen", "Kontoumsätze"), anim="cut", bis="m1"),
    ficon("tabler", "device-mobile", 1400, 700, 80, beim("morgen", "Handy"), fuell=WEISS),
    pl("Kontoumsatz: −500 €", 1250, 540, beim("morgen", "Kontoumsätze"), fill=ROTHELL, size=30, anker="m"),
    *redet("MK_redet", MX, BODEN, FH, "m1", "frage"),
    blase("sprech", 480, 200, "m1", 1060, 215, inhalt=["500 € abgehoben?", "Das war ich nicht!"], textsize=34, figur=MKr,
          bis="frage"),
    peep_voll("MK_schreck", MX, BODEN, FH, "frage", anim="cut"),
    # Die Frage: Heiko wieder im Bild
    peep_voll("HE_ernst_r", 300, BODEN, FH, "frage", anim="fade"),
    namensschild("Heiko", 300, BODEN, "frage", GRUEN),
    pl("Computerbetrug, § 263a StGB?", 960, 140, "frage", fill=WEISS, size=34, anker="m"),
    pl("Diebstahl am Geld und an der Karte?", 960, 230, beim("frage2", "Diebstahl"), fill=PINK, size=32, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Heiko und Meike wohnen in einer Wohngemeinschaft. Heiko kennt die Geheimzahl (PIN) der Bankkarte von Meike, "
            "weil er sie beim gemeinsamen Einkaufen gesehen hat. An einem Freitagabend steht Meike unter der Dusche, ihre "
            "Geldbörse liegt im Flur. Heiko nimmt heimlich die Bankkarte heraus; er will sie von Anfang an gleich wieder "
            "zurücklegen."),
    glyphen("Am Geldautomaten an der Ecke steckt er die Karte ein, tippt die Geheimzahl und hebt 500 € ab. Zu Hause legt er "
            "die Karte unbemerkt in die Geldbörse zurück. Am nächsten Morgen sieht Meike die Abbuchung."),
], "Wie hat sich Heiko strafbar gemacht?")

# C Wortlaut § 263a Abs. 1 und Struktur -------------------------------------------------------------------------------------------
W263A = ["„Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen",
         "Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch",
         "beschädigt, daß er das Ergebnis eines Datenverarbeitungsvorgangs",
         "durch unrichtige Gestaltung des Programms, durch Verwendung",
         "unrichtiger oder unvollständiger Daten, durch unbefugte Verwendung",
         "von Daten oder sonst durch unbefugte Einwirkung auf den Ablauf",
         "beeinflußt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit",
         "Geldstrafe bestraft.“"]
wl, wl_ende = wortlaut(110, 165, 1040, W263A, "§ 263a Abs. 1 StGB", "p263a", marken=[
    (0, "Absicht", beim("w263a", "Bereicherungsabsicht")),
    (2, "beschädigt", beim("w263a", "beschädigt")),
    (2, "Ergebnis eines Datenverarbeitungsvorgangs", beim("w263a", "Ergebnis")),
    (4, "unbefugte Verwendung", beim("w263a", "unbefugte")),
    (5, "von Daten", beim("w263a", "unbefugte"))], size=28)
assert wl_ende <= 560, wl_ende
SC = "A. § 263a StGB"
folie([("p263a", f"{SC} › Wortlaut"), ("nach", f"{SC} › dem Betrug nachgebildet")], rechts_frei([
    *tafel("p263a", "Computerbetrug: § 263a Abs. 1 StGB"),
    *wl,
    z("Betrug, § 263", 140, 590, "nach", "ExtraBold", 32),
    z("Computerbetrug, § 263a", 600, 590, "nach", "ExtraBold", 32),
    linienzug([(130, 640), (1150, 640)], "nach", breite=3, farbe=INK),
    z("Täuschung", 140, 660, beim("ersetzt", "Täuschung"), size=32),
    tafelicon(ficon("tabler", "arrow-narrow-right", 520, 705, 44, beim("ersetzt", "Tathandlung"))),
    z("Tathandlung", 600, 660, beim("ersetzt", "Tathandlung"), "Bold", 32),
    z("Irrtum und Verfügung", 140, 725, beim("ersetzt", "Irrtum"), size=32),
    tafelicon(ficon("tabler", "arrow-narrow-right", 520, 770, 44, beim("ersetzt", "Beeinflussung"))),
    z("Beeinflussung eines", 600, 725, beim("ersetzt", "Beeinflussung"), "Bold", 32),
    z("Datenverarbeitungsvorgangs", 600, 770, beim("ersetzt", "Beeinflussung"), "Bold", 32),
    fund("BGH, Beschl. v. 28.5.2013 – 3 StR 80/13, Rn. 8", 140, 830, beim("ersetzt", "Beeinflussung")),
    *paar("p263a", "MK_ruhig", "HE_ruhig", mk_cues=[("nach", "MK_denkt")], he_cues=[("ersetzt", "HE_ernst")]),
    mpille("§ 263a StGB", beim("p263a", "Paragraf"), bis="nach"),
    symbol("tabler", "cpu", "p263a", fuell=BLAU, bis="nach"),
    symbol("tabler", "scale", "nach", fuell=GELB, anim="cut"),
    mpille("dem Betrug nachgebildet", "nach", size=28, anim="cut"),
]))

# D 1. Tathandlung: Variante 3 ----------------------------------------------------------------------------------------------------
PO = f"{SC} › I. 1. objektiver Tatbestand"
folie([("t1", f"{PO} › a) Tathandlung"), ("var3", f"{PO} › a) unbefugte Verwendung von Daten")], rechts_frei([
    *tafel("t1", "a) Tathandlung"),
    z("4 Varianten in § 263a Abs. 1 StGB, hier die dritte:", 110, 185, "var", "Bold", 32),
    blk(110, 250, 1040, 100, GELB, "var3", [("unbefugte Verwendung von Daten", "ExtraBold", 40, INK)]),
    *okz("Karte und Geheimzahl sind echt", 400, "echt", size=34),
    *okz("Heiko verwendet richtige Daten", 460, beim("echt", "Heiko"), size=34),
    blk(110, 560, 1040, 110, HELL, "frageu", [("Entscheidend: unbefugt?", "ExtraBold", 40, INK)]),
    *paar("t1", "MK_ruhig", "HE_ruhig", mk_cues=[("frageu", "MK_denkt")], he_cues=[("echt", "HE_ernst")]),
    mpille("Variante 3", "var3", bis="echt"),
    ficon("fluent-emoji-flat", "credit-card", MB - 70, 380, 110, "echt", bis="frageu"),
    ficon("tabler", "password", MB + 75, 365, 100, "echt", bis="frageu"),
    mpille("echt", beim("echt", "echt"), fill=GRUEN, anim="cut", bis="frageu"),
    pl("unbefugt?", MB, 300, "frageu", fill=HELL, size=36, anker="m", anim="cut"),
]))

# E Drei Auslegungen von „unbefugt“ ------------------------------------------------------------------------------------------------
PU = f"{PO} › a) „unbefugt“"
folie([("ausl", f"{PU}: drei Auslegungen"), ("betr", f"{PU}: betrugsspezifische Auslegung")], rechts_frei([
    *tafel("ausl", "Was heißt „unbefugt“? (umstritten)"),
    z("subjektiv: jede Verwendung gegen den Willen", 110, 180, "subj", "Bold", 32),
    *plusminus("des Berechtigten", 150, 225, beim("subj", "gegen"), True, size=32),
    z("computerspezifisch: Automat fehlerhaft beeinflusst?", 110, 300, "comp", "Bold", 32),
    *plusminus("hier: Automat arbeitet fehlerfrei", 150, 345, beim("comp", "fehlerfrei"), False, size=32),
    blk(110, 415, 1040, 215, GRUENHELL, "betr", [("betrugsspezifisch (Rspr., h. M.):", "ExtraBold", 34, INK),
                                                ("unbefugt nur, was gegenüber einem", "Bold", 32, INK),
                                                ("Menschen eine Täuschung wäre", "Bold", 32, INK)]),
    fund("BGH, Beschl. v. 16.7.2015 – 2 StR 16/15, Rn. 10", 140, 645, beim("betr", "Täuschung")),
    z("Zweck: nur die Lücke des Betrugs beim Computer", 110, 705, "arg", size=32),
    z("schließen", 110, 750, "arg", size=32),
    fund("BGHSt 47, 160, 162 f. (BGH, Beschl. v. 21.11.2001 – 2 StR 260/01)", 140, 800, beim("arg", "Lücke")),
    *paar("ausl", "MK_ruhig", "HE_denkt", mk_cues=[("subj", "MK_ernst"), ("betr", "MK_ruhig")], he_cues=[("comp", "HE_ruhig")]),
    mpille("umstritten", "ausl", fill=HELL, bis="subj"),
    mpille("subjektiv", "subj", anim="cut", bis="comp"),
    mpille("computerspezifisch", "comp", size=28, anim="cut", bis="betr"),
    mpille("betrugsspezifisch", "betr", fill=GRUEN, size=28, anim="cut"),
    symbol("tabler", "user-question", "ausl", fuell=GELB, breite=100, bis="comp"),
    symbol("tabler", "cpu", "comp", fuell=BLAU, anim="cut", bis="betr"),
    symbol("fluent-emoji-flat", "balance-scale", "betr", anim="cut"),
]))

# F Probe: die gedachte Bankangestellte --------------------------------------------------------------------------------------------
BAX = 1420
BAd = ("BA_denkt_r", BAX, BR, FR)
folie([("probe", f"{PU}: Probe mit dem Bankangestellten"), ("unbefok", f"{PO} › a) unbefugte Verwendung (+)")], rechts_frei([
    *tafel("probe", "Probe: der gedachte Bankangestellte"),
    z("statt des Automaten ein Bankangestellter,", 110, 180, "angest", "Bold", 32),
    z("der dasselbe prüft wie der Automat", 110, 225, beim("angest", "dasselbe"), "Bold", 32),
    *okz("Vorlage von Karte und Geheimzahl: erklärt", 305, "erkl", size=32),
    z("schlüssig, zur Verwendung berechtigt zu sein", 175, 350, beim("erkl", "schlüssig"), size=32),
    fund("BGHSt 47, 160, 163; BGH, Beschl. v. 3.12.2025 – 5 StR 362/25, Rn. 10", 175, 400, beim("erkl", "schlüssig")),
    *neinz("Heiko: nicht berechtigt, Karte heimlich genommen", 470, "nicht", size=32),
    *okz("der gedachte Angestellte würde getäuscht", 530, beim("nicht", "Der"), size=32),
    blk(110, 620, 1040, 100, GRUEN, "unbefok", [("unbefugte Verwendung von Daten (+)", "ExtraBold", 38, INK)]),
    fund("BGH, Beschl. v. 16.7.2015 – 2 StR 16/15, Rn. 12; BGHSt 47, 160, 162", 140, 740, "unbefok"),
    # gedachte Bankangestellte (blickt zu Heiko) und Heiko
    peep_voll("BA_ruhig_r", BAX, BR, FR, "angest", anim="fade", bis="erkl"),
    peep_voll("BA_denkt_r", BAX, BR, FR, "erkl", anim="cut", bis="unbefok"),
    peep_voll("BA_ruhig_r", BAX, BR, FR, "unbefok", anim="cut"),
    pl("gedachte Bankangestellte", BAX - 20, BR + 22, "angest", fill=BLAU, size=28, anker="m"),
    *[e for e in [peep_voll("HE_ruhig", X2, BR, FR, "probe", anim="fade", bis="nicht"),
                  peep_voll("HE_sorge", X2, BR, FR, "nicht", anim="cut")]],
    namensschild("Heiko", X2, BR, "probe", GRUEN, d=0.2),
    blase("denk", 330, 190, "erkl", 1400, 250, inhalt=["berechtigt?"], textsize=32, figur=BAd, bis="unbefok"),
    karte_icon(MB + 10, 640, beim("erkl", "Karte"), breite=80),
    ficon("tabler", "password", MB + 10, 700, 70, beim("erkl", "Geheimzahl")),
    pl("getäuscht", MB, 66, beim("nicht", "getäuscht"), fill=ROTHELL, size=30, anker="m", bis="unbefok"),
    pl("unbefugt (+)", MB, 66, "unbefok", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# G Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs ------------------------------------------------------------------
folie([("dv", f"{PO} › b) Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs")], rechts_frei([
    *tafel("dv", "b) Beeinflussung des Ergebnisses"),
    z("eines Datenverarbeitungsvorgangs", 110, 165, "dv", "ExtraBold", 38),
    tafelicon(karte_icon(220, 330, beim("dv2", "Karte"), breite=100)),
    tafelicon(ficon("tabler", "password", 360, 320, 90, beim("dv2", "Geheimzahl"))),
    tafelicon(ficon("tabler", "arrow-narrow-right", 480, 310, 60, beim("dv2", "Geheimzahl"))),
    tafelicon(ficon("tabler", "cpu", 600, 330, 100, beim("dv2", "Geheimzahl"), fuell=BLAU)),
    tafelicon(ficon("tabler", "arrow-narrow-right", 720, 310, 60, beim("dv2", "gibt"))),
    tafelicon(ficon("fluent-emoji-flat", "euro-banknote", 850, 320, 120, beim("dv2", "gibt"))),
    z("Automat prüft Karte und Geheimzahl, gibt Geld frei", 110, 360, beim("dv2", "Geld"), size=32),
    *okz("beeinflussen: auch den Vorgang in Gang setzen", 440, "dv3", size=32),
    fund("BGH, Urt. v. 22.11.1991 – 2 StR 376/91, Rn. 5 (HRRS)", 175, 488, beim("dv3", "Vorgang")),
    *okz("Ergebnis mindert das Vermögen unmittelbar,", 560, "dv4", size=32),
    z("ohne weitere menschliche Entscheidung", 175, 605, beim("dv4", "ohne"), size=32),
    fund("BGH, Beschl. v. 28.5.2013 – 3 StR 80/13, Rn. 8 f.", 175, 653, beim("dv4", "ohne")),
    blk(110, 720, 1040, 100, GRUEN, beim("dv4", "menschliche"),
        [("Beeinflussung (+)", "ExtraBold", 38, INK)]),
    *paar("dv", "MK_ruhig", "HE_ruhig", mk_cues=[("dv3", "MK_denkt")], he_cues=[("dv4", "HE_ernst")]),
    mpille("in Gang setzen", "dv3", bis="dv4"),
    mpille("unmittelbar", beim("dv4", "unmittelbar"), anim="cut"),
    symbol("tabler", "cpu", "dv", fuell=BLAU),
]))

# H Vermögensschaden -------------------------------------------------------------------------------------------------------------
folie([("schad", f"{PO} › c) Vermögensschaden"), ("jedenf", f"{PO} › c) Schaden jedenfalls bei der Bank")], rechts_frei([
    *tafel("schad", "c) Vermögensschaden"),
    *okz("500 € aus dem Vermögen der Bank", 190, "bank", "Bold", 34),
    fund("BGH, Beschl. v. 30.1.2001 – 1 StR 512/00, Rn. 6", 175, 240, beim("bank", "Vermögen")),
    z("nicht autorisierte Abhebung: kein Anspruch der", 110, 320, "erstatt", size=32),
    z("Bank gegen Meike auf Erstattung der Aufwendungen", 110, 365, beim("erstatt", "Anspruch"), size=32),
    z("Bank muss das Konto wieder ausgleichen", 110, 425, beim("erstatt", "Konto"), "Bold", 32),
    fund("§ 675u Satz 1, 2 BGB; BGH, Urt. v. 18.7.2007 – 2 StR 69/07, Rn. 23", 140, 475, beim("erstatt", "Konto")),
    blk(110, 560, 1040, 100, GRUEN, "jedenf", [("Schaden (+): jedenfalls bei der Bank", "ExtraBold", 38, INK)]),
    *paar("schad", "MK_ruhig", "HE_ruhig", mk_cues=[("erstatt", "MK_denkt"), ("jedenf", "MK_ruhig")],
          he_cues=[("jedenf", "HE_ernst")]),
    symbol("tabler", "building-bank", "bank", fuell=WEISS, breite=110),
    mpille("500 €", beim("bank", "fünfhundert"), fill=ROTHELL),
]))

# I Subjektiver Tatbestand, Ergebnis zu § 263a -----------------------------------------------------------------------------------
PS_ = f"{SC} › I. 2. subjektiver Tatbestand"
folie([("vors", f"{PS_} › a) Vorsatz"), ("abs", f"{PS_} › b) Absicht rechtswidriger Bereicherung"),
       ("rws", f"{SC} › II. Rechtswidrigkeit, III. Schuld"), ("erg1", f"{SC} › Ergebnis (+)")], rechts_frei([
    *tafel("vors", "2. Subjektiver Tatbestand"),
    z("a) Vorsatz", 110, 180, "vors", "ExtraBold", 34),
    *okz("weiß: darf die Karte nicht benutzen; will das Geld", 230, "vors2", size=32),
    z("b) Absicht rechtswidriger Bereicherung", 110, 320, "abs", "ExtraBold", 34),
    *okz("kein Anspruch auf die 500 €", 370, "abs2", size=32),
    *okz("II. Rechtswidrigkeit, III. Schuld", 460, "rws", "Bold", 34),
    blk(110, 560, 1040, 150, GRUEN, beim("erg1", "Heiko"), [("Heiko: strafbar wegen Computerbetrugs,", "ExtraBold", 36, INK),
                                                          ("§ 263a Abs. 1 StGB", "ExtraBold", 36, INK)]),
    *paar("vors", "MK_ruhig", "HE_ruhig", mk_cues=[("erg1", "MK_ernst")], he_cues=[("vors2", "HE_eifrig"), ("erg1", "HE_sorge")]),
    symbol("tabler", "bulb", "vors", fuell=GELB, bis="abs"),
    mpille("weiß und will", "vors2", bis="abs"),
    symbol("fluent-emoji-flat", "euro-banknote", "abs", anim="cut", bis="erg1"),
    mpille("kein Anspruch", beim("abs2", "keinen"), fill=ROTHELL, anim="cut", bis="erg1"),
    symbol("tabler", "circle-check", "erg1", fuell=GRUEN, anim="cut"),
    mpille("§ 263a (+)", beim("erg1", "Heiko"), fill=GRUEN, anim="cut"),
]))

# J B. § 242 am Geld ----------------------------------------------------------------------------------------------------------------
SB = "B. § 242 StGB am Geld"
wl2, wl2_ende = wortlaut(110, 165, 1040, ["„Wer eine fremde bewegliche Sache einem anderen in der Absicht",
                                          "wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, …“"],
                         "§ 242 Abs. 1 StGB (Auszug)", "w242", marken=[(0, "fremde bewegliche Sache", beim("w242", "fremde")),
                                                                      (1, "wegnimmt", beim("w242", "wegnimmt"))], size=28)
folie([("geld242", f"{SB}"), ("wegn", f"{SB} › Wegnahme: Bruch fremden Gewahrsams?")], rechts_frei([
    *tafel("geld242", "B. Diebstahl am Geld, § 242 StGB"),
    *wl2,
    *okz("fremd: Bank übereignet nur dem Berechtigten", wl2_ende + 25, "fremd", size=32),
    fund("BGH, Beschl. v. 21.3.2019 – 3 StR 333/18, Rn. 8", 175, wl2_ende + 72, beim("fremd", "Berechtigten")),
    *neinz("Wegnahme: kein Bruch fremden Gewahrsams", wl2_ende + 130, "wegn", "Bold", 32),
    z("Gewahrsam an jeden, der ordnungsgemäß mit Karte", 175, wl2_ende + 190, "gew", size=32),
    z("und Geheimzahl bedient; Berechtigung egal", 175, wl2_ende + 235, beim("gew", "Ob"), size=32),
    z("Heiko: Geld übergeben, nicht weggenommen", 175, wl2_ende + 295, "gew2", "Bold", 32),
    fund("BGHSt 38, 120, 122 f.; BGH, Beschl. v. 21.3.2019 – 3 StR 333/18, Rn. 16", 175, wl2_ende + 345, "gew2"),
    *paar("geld242", "MK_ruhig", "HE_ruhig", mk_cues=[("fremd", "MK_denkt")], he_cues=[("gew2", "HE_ernst")]),
    symbol("fluent-emoji-flat", "euro-banknote", "geld242", breite=110, bis="gew2"),
    mpille("§ 242 StGB?", "geld242", bis="fremd"),
    mpille("fremd (+)", "fremd", fill=GRUEN, anim="cut", bis="wegn"),
    mpille("Wegnahme?", "wegn", fill=HELL, anim="cut", bis="gew2"),
    mpille("übergeben", beim("gew2", "übergeben"), fill=WEISS, anim="cut"),
    symbol("tabler", "dialpad", "gew2", fuell=WEISS, anim="cut", breite=90),
]))

# K Streit ------------------------------------------------------------------------------------------------------------------------
folie([("streit", f"{SB} › Streit"), ("kein242", f"{SB} › Diebstahl (−)")], rechts_frei([
    *tafel("streit", "B. Streit: doch Diebstahl am Geld?"),
    blk(110, 185, 1040, 150, ROTHELL, "streit", [("früher manche Gerichte und Autoren:", "Bold", 32, INK),
                                                ("trotzdem Diebstahl", "ExtraBold", 34, INK)]),
    blk(110, 365, 1040, 215, GRUENHELL, "streit2", [("BGH: nein, der Gesetzgeber wollte diesen", "Bold", 32, INK),
                                                   ("Kartenmissbrauch gerade mit § 263a StGB", "Bold", 32, INK),
                                                   ("erfassen", "Bold", 32, INK)]),
    fund("BGH, Urt. v. 22.11.1991 – 2 StR 376/91 (BGHSt 38, 120), Rn. 17 f. (HRRS)", 140, 595, beim("streit2", "Gesetzgeber")),
    blk(110, 670, 1040, 100, GRUEN, "kein242", [("Diebstahl am Geld (−)", "ExtraBold", 38, INK)]),
    *paar("streit", "MK_denkt", "HE_ruhig", mk_cues=[("kein242", "MK_ruhig")], he_cues=[("streit2", "HE_ernst")]),
    symbol("tabler", "gavel", "streit", fuell=HOLZ),
    mpille("§ 242?", "streit", fill=ROTHELL, bis="streit2"),
    mpille("§ 263a", beim("streit2", "Paragraf"), fill=GRUEN, anim="cut", bis="kein242"),
    mpille("§ 242 (−)", "kein242", fill=WEISS, anim="cut"),
]))

# L C. § 242 an der Karte -----------------------------------------------------------------------------------------------------------
SK = "C. § 242 StGB an der Karte"
folie([("karte", f"{SK}"), ("zueig", f"{SK} › Zueignungsabsicht")], rechts_frei([
    *tafel("karte", "C. Diebstahl an der Karte, § 242 StGB"),
    *okz("fremde Sache, Meike weggenommen", 180, "karte2", size=32),
    z("Zueignungsabsicht?", 110, 255, "zueig", "ExtraBold", 36),
    z("Substanz oder Sachwert einverleiben wollen", 110, 310, "zdef", size=32),
    fund("BGH, Beschl. v. 13.8.2025 – 4 StR 308/25, Rn. 6", 140, 357, beim("zdef", "Sachwert")),
    *neinz("Substanz: unverändert zurück, nur", 420, "subst", size=32),
    z("Gebrauchsanmaßung", 175, 465, beim("subst", "Gebrauchsanmaßung"), "Bold", 32),
    *neinz("Sachwert: Karte verkörpert das Geld auf dem", 535, "sachw", size=32),
    z("Konto nicht selbst (anders: Sparbuch)", 175, 580, beim("sachw", "Karte"), size=32),
    fund("BGH, Beschl. v. 30.1.2001 – 1 StR 512/00, Rn. 5", 175, 627, beim("sachw", "Sparbuch")),
    blk(110, 690, 1040, 110, GRUEN, "kein242k", [("Zueignungsabsicht (−): kein Diebstahl", "ExtraBold", 36, INK)]),
    *paar("karte", "MK_ruhig", "HE_ruhig", mk_cues=[("zueig", "MK_denkt"), ("kein242k", "MK_ruhig")],
          he_cues=[("subst", "HE_ernst")]),
    karte_icon(MB, 380, "karte", breite=110, bis="subst"),
    mpille("Bankkarte", "karte", bis="zueig"),
    mpille("Zueignungsabsicht?", "zueig", size=28, anim="cut", bis="subst"),
    karte_icon(MB - 50, 380, "subst", breite=100, anim="cut", bis="sachw"),
    ficon("tabler", "arrow-back-up", MB + 70, 370, 80, "subst", anim="cut", bis="sachw"),
    mpille("zurücklegen", beim("subst", "zurücklegen"), anim="cut", bis="sachw"),
    karte_icon(MB - 70, 380, "sachw", breite=100, anim="cut"),
    ficon("tabler", "notebook", MB + 70, 380, 90, beim("sachw", "Sparbuch"), fuell=GELB, anim="cut"),
    mpille("Sachwert?", "sachw", anim="cut", bis="kein242k"),
    mpille("§ 242 (−)", "kein242k", fill=WEISS, anim="cut"),
]))

# M Ergebnis, Konkurrenzen -------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Heiko strafbar, § 263a Abs. 1 StGB"), ("konk", "D. Konkurrenzen")], rechts_frei([
    *tafel("erg", "Ergebnis und Konkurrenzen"),
    blk(110, 190, 1040, 150, GRUEN, beim("erg", "Heiko"), [("Heiko: strafbar wegen Computerbetrugs,", "ExtraBold", 36, INK),
                                                         ("§ 263a Abs. 1 StGB", "ExtraBold", 36, INK)]),
    z("Unterschlagung am Geld, § 246 StGB:", 110, 400, "konk", "Bold", 34),
    z("tritt dahinter zurück", 110, 450, beim("konk", "tritt"), size=34),
    fund("BGH, Beschl. v. 11.8.2021 – 3 StR 63/21, Rn. 33", 140, 505, beim("konk", "tritt")),
    *paar("erg", "MK_ernst", "HE_sorge"),
    symbol("tabler", "circle-check", beim("erg", "Heiko"), fuell=GRUEN),
    mpille("§ 263a (+)", beim("erg", "Heiko"), fill=GRUEN, bis="konk"),
    mpille("§ 246 tritt zurück", beim("konk", "tritt"), size=28, anim="cut"),
]))

# N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Wer benutzt die Karte?"), ("tipp3", "Klausurtipp · § 266b StGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Frag zuerst: Wer benutzt die Karte?", 200, 200, beim("tipp", "Frag"), "Bold", 36),
    z("berechtigter Karteninhaber überzieht sein Konto:", 150, 290, "tipp2", size=32),
    z("kein Computerbetrug, nicht unbefugt", 150, 340, beim("tipp2", "kein"), "ExtraBold", 34),
    z("Automat prüft nur den Verfügungsrahmen,", 150, 400, beim("tipp2", "Automat", nr=2), size=32),
    z("nicht die Zahlungsfähigkeit", 150, 445, beim("tipp2", "Zahlungsfähigkeit"), size=32),
    fund("BGHSt 47, 160, 162 f. (BGH, Beschl. v. 21.11.2001 – 2 StR 260/01)", 150, 495, beim("tipp2", "Zahlungsfähigkeit")),
    z("allenfalls § 266b StGB, nur im Drei-Partner-System", 150, 570, "tipp3", "Bold", 32),
    fund("BGHSt 47, 160, 164 ff.", 150, 620, beim("tipp3", "Drei")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Prüfschema ------------------------------------------------------------------------------------------------------------------------
K0, K1, K2 = 130, 190, 250
KA = K2 + int(F("Regular", 34).getlength("1. objektiv: "))
KS = K2 + int(F("Regular", 34).getlength("2. subjektiv: "))
PSCH = "Prüfschema"
folie([("sch", PSCH), ("s1", f"{PSCH} › A. Computerbetrug, § 263a StGB"), ("s1a", f"{PSCH} › A. I. 1. a) unbefugte Verwendung von Daten"),
       ("s1b", f"{PSCH} › A. I. 1. b) Beeinflussung"), ("s1c", f"{PSCH} › A. I. 1. c) Vermögensschaden"),
       ("s1d", f"{PSCH} › A. I. 2. a) Vorsatz"), ("s1e", f"{PSCH} › A. I. 2. b) Absicht rechtswidriger Bereicherung"),
       ("s1f", f"{PSCH} › A. II. Rechtswidrigkeit, III. Schuld"), ("s2", f"{PSCH} › B. Diebstahl am Geld"),
       ("s3", f"{PSCH} › C. Diebstahl an der Karte"), ("s4", f"{PSCH} › D. Konkurrenzen")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: fremde Karte am Geldautomaten", 110, 85, "sch", 50),
    z("A. Computerbetrug, § 263a StGB", K0, 165, "s1", "ExtraBold", 36, rechts=1820),
    z("I. Tatbestand", K1, 218, "s1a", "Bold", 34, rechts=1820),
    z("1. objektiv: a) unbefugte Verwendung von Daten", K2, 268, beim("s1a", "Objektiv"), size=34, rechts=1820),
    z("b) Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs", KA, 316, "s1b", size=34, rechts=1820),
    z("c) Vermögensschaden", KA, 364, "s1c", size=34, rechts=1820),
    z("2. subjektiv: a) Vorsatz", K2, 418, "s1d", size=34, rechts=1820),
    z("b) Absicht rechtswidriger Bereicherung", KS, 466, "s1e", size=34, rechts=1820),
    z("II. Rechtswidrigkeit, III. Schuld", K1, 524, "s1f", "Bold", 34, rechts=1820),
    z("B. Diebstahl am Geld: ohne Wegnahme", K0, 600, "s2", "ExtraBold", 36, rechts=1820),
    z("C. Diebstahl an der Karte: ohne Zueignungsabsicht", K0, 670, "s3", "ExtraBold", 36, rechts=1820),
    z("D. Konkurrenzen", K0, 740, "s4", "ExtraBold", 36, rechts=1820),
])

# P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Heimlich genommene Karte mit Geheimzahl", 0)],
                 [("am Automaten: ", 0), ("Computerbetrug", "a"), (",", 0)],
                 [("weil das gegenüber einem Menschen", 0)], [("eine ", 0), ("Täuschung", "b"), (" wäre.", 0)]], 750, 275, 42,
                "merke", {"a": beim("merke", "Computerbetrug"), "b": beim("merke", "Täuschung")}),
    *markertext([[("Das Geld stiehlt er nicht:", 0)], [("Der Automat ", 0), ("übergibt", "c"), (" es.", 0)]], 750, 540, 42, "mk2",
                {"c": beim("mk2", "übergibt")}),
    *markertext([[("Wer die Karte ", 0), ("zurücklegen", "d"), (" will,", 0)], [("stiehlt auch sie nicht.", 0)]], 750, 700, 42,
                "mk3", {"d": beim("mk3", "zurücklegen")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
