"""Folge 060 · Hinreichender Tatverdacht: Wann die Staatsanwaltschaft anklagt – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A In der Wohnstraße (Fahrrad aus dem Vorgarten, Zeugin beim Blumengießen), B Bei der Polizei
(Anzeige, Bestreiten), C Beim Staatsanwalt (Akte, Frage), D Sachverhalt, E Abschluss der Ermittlungen (Wortlautkarten
§ 170 I und § 170 II 1 StPO), F Verdachtsstufen (Treppe § 152 II – hinreichend – § 112), G Prognose (Wortlautkarte BGH
StB 58/25 Rn. 5, OLG Düsseldorf 4 Ws 73/23 Rn. 18, OLG Köln 2 Ws 264/13 Rn. 13), H Beweistabelle (§ 160 II), I Aussage gegen
Aussage (Wortlautkarte BGH StB 58/25 Rn. 6), J „Im Zweifel für den Angeklagten“?, K Ergebnis mit Beurteilungsspielraum,
L Gegenfall und Klageerzwingung, M § 203 (Wortlautkarte) und Ausblick §§ 153, 153a, N Abschlussverfügung, O Klausurtipp
(Lexi), P Prüfschema, Q Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Freilauf des geschobenen Fahrrads (Szene A), Akte auf dem Schreibtisch (Szene C);
Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_060/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
GRAU = (205, 205, 210, 255)
HOLZ = (214, 160, 110, 255)
DUNKEL = (58, 58, 72, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. amtlicher Volltext, Abruf 02.10.2026) in einer hellen
    Karte, Fundstelle darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}
    (Hervorhebung synchron zum gesprochenen Wort)."""
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
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hart(e):
    e.anim = "cut"
    return e


# --- Eigene Hilfsfunktion (wie Folge 024/048/054): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause; redet() kürzt jedes Wortende auf
# das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
import wave as _wave
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel

# A Fall: in der Wohnstraße ------------------------------------------------------------------------------------------------
HX, WX = 330, 1500                      # Frau Hesse (gegenüber, blickt nach rechts), Frau Wessel (vor ihrem Haus)
RADX = 1335                             # Fahrrad im Vorgarten
MX1 = 1500                              # Herr Mertens kommt rechts vom Rad (blickt zum Rad) und schiebt es nach links davon
WEG = -420
HEa = ("HE_redet_r", HX, BODEN, FH)
WEa = ("WE_redet", WX, BODEN, FH)
t_weg0, t_weg1 = beim("schiebt", "schiebt"), beim("schiebt", "davon", ende=True)
rad_weg = szene(bewegt(ficon("tabler", "bike", RADX + WEG, BODEN - 2, 200, "schiebt", fuell=BLAU, anim="cut", bis="mittag"),
                       t_weg0, t_weg1, -WEG), "060freilauf*", 1.0, versatz=0.05)
folie([(NULL, "Fall · In der Wohnstraße"), (beim("mertens", "Herr"), "Fall · Das Fahrrad verschwindet"),
       ("mittag", "Fall · Am Mittag")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("In einer ruhigen Wohnstraße", 70, 40, NULL, fill=GELB, size=40),
    # Haus und Vorgarten von Frau Wessel (rechts)
    ficon("tabler", "home", 1700, BODEN - 2, 300, NULL, fuell=GELB),
    ficon("tabler", "fence", 1170, BODEN - 2, 170, NULL, fuell=HOLZ),
    ficon("tabler", "bike", RADX, BODEN - 2, 200, beim("rad", "Fahrrad"), fuell=BLAU, bis="schiebt"),
    pl("Dienstagvormittag", 960, 150, beim("fall", "Dienstagvormittag"), fill=WEISS, size=30, anker="m", bis="mittag"),
    pl("Fahrrad: 900 €", RADX - 60, 600, beim("rad", "neunhundert"), fill=BLAU, size=30, anker="m", bis="schiebt"),
    # Frau Hesse gießt gegenüber ihre Blumen (links)
    peep_voll("HE_ruhig_r", HX, BODEN, FH, NULL, bis=beim("mertens", "Herr")),
    peep_voll("HE_denkt_r", HX, BODEN, FH, beim("mertens", "Herr"), anim="cut", bis="mittag"),
    peep_voll("HE_ruhig_r", HX, BODEN, FH, "mittag", anim="cut", bis="h1"),
    *redet("HE_redet_r", HX, BODEN, FH, "h1", "anzeige"),
    namensschild("Frau Hesse", HX, BODEN, beim("hesse", "Frau"), GRUEN),
    ficon("tabler", "flower", 560, BODEN - 2, 70, NULL, fuell=PINK),
    ficon("tabler", "flower", 640, BODEN - 2, 70, NULL, fuell=GELB),
    ficon("tabler", "flower", 720, BODEN - 2, 70, NULL, fuell=ROT),
    ficon("tabler", "droplet", 600, 760, 34, beim("hesse", "gießt"), fuell=BLAU, bis="mertens"),
    ficon("tabler", "droplet", 680, 735, 34, beim("hesse", "gießt"), fuell=BLAU, d=0.15, bis="mertens"),
    pl("Frau Hesse gießt ihre Blumen", 640, 560, beim("hesse", "gießt"), fill=WEISS, size=28, anker="m", bis="mertens"),
    # Herr Mertens kommt und schiebt das Rad davon
    peep_voll("ME_ruhig", MX1, BODEN, FH, beim("mertens", "Herr"), anim="fade", bis="schiebt"),
    namensschild("Herr Mertens", MX1, BODEN, beim("mertens", "Herr"), ROT, bis="schiebt"),
    pl("ein Nachbar", MX1, 330, beim("mertens", "Nachbar"), fill=WEISS, size=28, anker="m", bis="schiebt"),
    bewegt(peep_voll("ME_ruhig", MX1 + WEG, BODEN, FH, "schiebt", anim="cut", bis="mittag"), t_weg0, t_weg1, -WEG),
    bewegt(namensschild("Herr Mertens", MX1 + WEG, BODEN, "schiebt", ROT, anim="cut", bis="mittag"), t_weg0, t_weg1, -WEG),
    rad_weg,
    pl("durch das Gartentor davon", 960, 150, beim("schiebt", "Gartentor"), fill=PINK, size=30, anker="m", bis="mittag"),
    # am Mittag: Frau Wessel kommt nach Hause, das Rad ist weg
    ficon("tabler", "sun", 960, 230, 90, "mittag", fuell=GELB, bis="w1"),
    pl("am Mittag", 960, 300, "mittag", fill=WEISS, size=30, anker="m", bis="w1"),
    peep_voll("WE_ruhig", WX, BODEN, FH, beim("mittag", "Frau"), anim="fade", bis="w1"),
    *redet("WE_redet", WX, BODEN, FH, "w1", "h1"),
    peep_voll("WE_sorge", WX, BODEN, FH, "h1", anim="cut"),
    namensschild("Frau Wessel", WX, BODEN, beim("mittag", "Frau"), BLAU),
    ring(RADX - 20, 795, 100, 80, "w1"),
    blase("sprech", 520, 170, "w1", 1150, 300, inhalt=["Mein Fahrrad ist weg!"], textsize=36, figur=WEa, bis="h1"),
    blase("sprech", 640, 200, "h1", 760, 260, inhalt=["Ich habe es gesehen. Herr", "Mertens hat es weggeschoben."],
          textsize=32, figur=HEa, bis="anzeige"),
])

# B Fall: bei der Polizei ----------------------------------------------------------------------------------------------------
WXb, MXb = 360, 1480
MEb = ("ME_redet", MXb, BODEN, FH)
folie([("anzeige", "Fall · Die Anzeige"), ("vern", "Fall · Er bestreitet alles"), ("spur", "Fall · Keine weiteren Beweise")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "anzeige", breite=7, farbe=INK)),
    pl("Bei der Polizei", 70, 40, "anzeige", fill=BLAU, size=40, anim="cut"),
    ficon("tabler", "desk", 900, BODEN - 2, 440, "anzeige", fuell=HOLZ, anim="cut"),
    ficon("tabler", "file-text", 820, 690, 90, beim("anzeige", "zeigt"), fuell=WEISS),
    pl("Anzeige gegen Herrn Mertens", 900, 150, beim("anzeige", "zeigt"), fill=WEISS, size=30, anker="m", bis="vern"),
    peep_voll("WE_denkt_r", WXb, BODEN, FH, "anzeige", anim="cut", bis="vern"),
    namensschild("Frau Wessel", WXb, BODEN, "anzeige", BLAU, anim="cut", bis="vern"),
    peep_voll("ME_ruhig", MXb, BODEN, FH, "vern", anim="fade", bis="m1"),
    *redet("ME_redet", MXb, BODEN, FH, "m1", "spur"),
    peep_voll("ME_denkt", MXb, BODEN, FH, "spur", anim="cut"),
    namensschild("Herr Mertens", MXb, BODEN, "vern", ROT),
    pl("bestreitet alles", MXb, 330, beim("vern", "bestreitet"), fill=PINK, size=30, anker="m", bis="m1"),
    blase("sprech", 700, 200, "m1", 900, 250, inhalt=["Ich war das nicht. Ich war den ganzen", "Vormittag gar nicht zu Hause."],
          textsize=32, figur=MEb, bis="spur"),
    ficon("tabler", "bike-off", 420, 700, 130, beim("spur", "Fahrrad"), fuell=BLAU),
    pl("Fahrrad verschwunden", 420, 500, beim("spur", "Fahrrad"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "device-cctv-off", 900, 560, 110, beim("spur", "Kamera"), fuell=WEISS),
    pl("keine Kamera", 900, 380, beim("spur", "Kamera"), fill=WEISS, size=28, anker="m"),
    pl("Alibi: niemand bestätigt", 1480, 200, beim("spur", "niemand"), fill=GELB, size=28, anker="m"),
])

# C Fall: beim Staatsanwalt --------------------------------------------------------------------------------------------------
SAX = 1180
SAc = ("SA_redet", SAX, BODEN, FH)
akte = szene(bewegt(ficon("tabler", "folders", 560, 531, 190, "akte", fuell=GELB), "akte", ("akte", 0.35), 0, -260),
             "060akte*", 1.0, versatz=0.30)
folie([("akte", "Fall · Beim Staatsanwalt"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "akte", breite=7, farbe=INK)),
    pl("Bei der Staatsanwaltschaft", 70, 40, "akte", fill=GELB, size=40, anim="cut"),
    ficon("tabler", "desk", 560, BODEN - 2, 560, "akte", fuell=HOLZ, anim="cut"),
    akte,
    peep_voll("SA_ruhig", SAX, BODEN, FH, "akte", bis="sa1"),
    *redet("SA_redet", SAX, BODEN, FH, "sa1", "frage"),
    peep_voll("SA_denkt", SAX, BODEN, FH, "frage", anim="cut"),
    namensschild("Staatsanwalt", SAX, BODEN, "akte", LILA),
    blase("sprech", 640, 200, "sa1", 1540, 250, inhalt=["Eine einzige Zeugin, und er", "bestreitet alles. Klage ich an?"],
          textsize=32, figur=SAc, bis="frage"),
    pl("eine einzige Zeugin", 360, 270, beim("sa1", "Zeugin"), fill=GRUEN, size=28, anker="m"),
    pl("er bestreitet alles", 770, 270, beim("sa1", "bestreitet"), fill=PINK, size=28, anker="m"),
    pl("Reicht eine Zeugin für die Anklage?", 1460, 160, "frage", fill=WEISS, size=32, anker="m"),
    pl("Wann ist der Tatverdacht hinreichend?", 1460, 250, "frage2", fill=PINK, size=32, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("An einem Dienstagvormittag schiebt ein Mann das neue Fahrrad von Frau Wessel (Wert 900 Euro, nicht "
            "angeschlossen) aus ihrem Vorgarten durch das Gartentor davon. Frau Hesse sieht das gegenüber beim Blumengießen, "
            "bei Tageslicht über die schmale Straße. Sie kennt ihren Nachbarn Herrn Mertens seit Jahren. Am Mittag sagt sie "
            "Frau Wessel, er habe das Rad weggeschoben; bei der Polizei wiederholt sie das."),
    glyphen("Frau Wessel erstattet Anzeige. Herr Mertens wird als Beschuldigter vernommen und bestreitet alles: Er sei den "
            "ganzen Vormittag nicht zu Hause gewesen. Das bestätigt niemand. Das Rad bleibt verschwunden, eine Kamera gibt "
            "es nicht. Die Akte liegt dem Staatsanwalt vor."),
], "Erhebt der Staatsanwalt Anklage?")

# E Abschluss der Ermittlungen: § 170 StPO ----------------------------------------------------------------------------------
PE = "Abschluss der Ermittlungen"
folie([("abschl", f"{PE} · zwei Wege"), ("p170", f"{PE} › Anklage, § 170 Abs. 1 StPO"),
       ("p170b", f"{PE} › Einstellung, § 170 Abs. 2 StPO"), ("hinr", f"{PE} › genügender Anlass = hinreichender Tatverdacht")],
      rechts_frei([
    *tafel("abschl", "Abschluss der Ermittlungen: § 170 StPO", size=46),
    *wortlaut(110, 180, 1040, 150, "p170", [
        [("„Bieten die Ermittlungen ", 0), ("genügenden Anlaß", "a"), (" zur Erhebung der", 0)],
        [("öffentlichen Klage, so erhebt die Staatsanwaltschaft sie durch", 0)],
        [("Einreichung einer ", 0), ("Anklageschrift", "b"), (" bei dem zuständigen Gericht.“", 0)],
    ], 30, {"a": beim("p170", "genügenden"), "b": beim("p170", "Anklageschrift")}, "§ 170 Abs. 1 StPO"),
    *wortlaut(110, 400, 1040, 70, "p170b", [
        [("„Andernfalls stellt die Staatsanwaltschaft das Verfahren ", 0), ("ein", "a"), (".“", 0)]], 30,
        {"a": beim("p170b", "ein")}, "§ 170 Abs. 2 S. 1 StPO"),
    fl_block(110, 560, 1040, 120, GELB, "hinr", [("genügender Anlass = hinreichender Tatverdacht", "ExtraBold", 36, INK)]),
    z("derselbe Maßstab wie bei der Eröffnung, § 203 StPO", 110, 705, beim("hinr", "derselbe"), "Bold", 32),
    z("BVerfG, Beschl. v. 21.12.2022 – 2 BvR 378/20, Rn. 78", 150, 755, beim("hinr", "derselbe"), size=26, farbe=TEXT),
    peep_voll("ME_ruhig", X1, BR, FR, "abschl", bis="hinr"),
    peep_voll("ME_sorge", X1, BR, FR, "hinr", anim="cut"),
    peep_voll("SA_denkt", X2, BR, FR, "abschl", d=0.2, bis="p170b"),
    peep_voll("SA_ruhig", X2, BR, FR, "p170b", anim="cut"),
    namensschild("Herr Mertens", X1, BR, "abschl", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "abschl", LILA, d=0.3),
    pl("zwei Wege", MB, 160, "abschl", fill=WEISS, size=30, anker="m", bis=beim("p170", "Anklageschrift")),
    ficon("tabler", "file-check", MB, 380, 100, beim("p170", "Anklageschrift"), fuell=GRUEN, bis="p170b"),
    pl("Anklage", MB, 160, beim("p170", "Anklageschrift"), fill=GRUEN, size=30, anker="m", anim="cut", bis="p170b"),
    ficon("tabler", "file-x", MB, 380, 100, "p170b", fuell=ROT, anim="cut", bis="hinr"),
    pl("Einstellung", MB, 160, "p170b", fill=ROTHELL, size=30, anker="m", anim="cut", bis="hinr"),
    ficon("tabler", "scale", MB, 380, 110, "hinr", fuell=GELB, anim="cut"),
    pl("hinreichender Tatverdacht", MB, 160, "hinr", fill=GELB, size=28, anker="m", anim="cut"),
]))

# F Verdachtsstufen ------------------------------------------------------------------------------------------------------------
PV = "Verdachtsstufen"
folie([("stufen", f"{PV} · drei Stufen"), ("anf", f"{PV} › Anfangsverdacht, § 152 Abs. 2 StPO"),
       ("mitte", f"{PV} › hinreichender Tatverdacht: Anklage"), ("dring", f"{PV} › dringender Tatverdacht, § 112 StPO")],
      rechts_frei([
    *tafel("stufen", "Drei Verdachtsstufen"),
    fl_block(110, 640, 620, 150, WEISS, "anf", [("Anfangsverdacht", "ExtraBold", 34, INK),
                                               ("§ 152 Abs. 2 StPO", "Bold", 28, INK)], rand=4),
    z("zureichende tatsächliche Anhaltspunkte", 110, 810, beim("anf", "zureichende"), size=28, farbe=TEXT),
    fl_block(310, 440, 620, 150, GELB, "mitte", [("hinreichender Tatverdacht", "ExtraBold", 34, INK),
                                                ("für die Anklage", "Bold", 28, INK)], rand=4),
    fl_block(510, 240, 620, 150, ROTHELL, "dring", [("dringender Tatverdacht", "ExtraBold", 34, INK),
                                                   ("§ 112 Abs. 1 S. 1 StPO", "Bold", 28, INK)], rand=4),
    peep_voll("ME_ruhig", X1, BR, FR, "stufen", bis="dring"),
    peep_voll("ME_schreck", X1, BR, FR, "dring", anim="cut"),
    peep_voll("SA_ruhig", X2, BR, FR, "stufen", d=0.2),
    namensschild("Herr Mertens", X1, BR, "stufen", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "stufen", LILA, d=0.3),
    ficon("tabler", "stairs-up", MB, 380, 110, "stufen", fuell=GELB),
    pl("3 Stufen", MB, 160, "stufen", fill=WEISS, size=30, anker="m", bis="anf"),
    pl("Beginn der Ermittlungen", MB, 160, "anf", fill=WEISS, size=28, anker="m", anim="cut", bis="mitte"),
    pl("für die Anklage", MB, 160, "mitte", fill=GELB, size=30, anker="m", anim="cut", bis="dring"),
    pl("Untersuchungshaft", MB, 160, beim("dring", "Untersuchungshaft"), fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# G Prognose -------------------------------------------------------------------------------------------------------------------
PP = "Prognose"
folie([("prog", f"{PP} › Verurteilung wahrscheinlich"), ("prog2", f"{PP} › weniger als dringender Tatverdacht"),
       ("formel", f"{PP} › mehr für Verurteilung als für Freispruch"), ("verw", f"{PP} › nur verwertbare Beweise")],
      rechts_frei([
    *tafel("prog", "Die Prognose", size=46),
    *wortlaut(110, 170, 1040, 190, "prog", [
        [("„Ein hinreichender Tatverdacht ist zu bejahen, wenn bei", 0)],
        [("vorläufiger Tatbewertung", "a"), (" auf Grundlage des Ermittlungsergebnisses", 0)],
        [("die Verurteilung in einer Hauptverhandlung mit vollgültigen", 0)],
        [("Beweismitteln ", 0), ("wahrscheinlich", "b"), (" ist …“", 0)],
    ], 30, {"a": beim("prog", "vorläufiger"), "b": beim("prog", "wahrscheinlich")},
        "BGH, Beschl. v. 10.12.2025 – StB 58/25, Rn. 5"),
    z("weniger als beim dringenden Tatverdacht", 110, 420, beim("prog2", "weniger"), "Bold", 32),
    z("keine volle Überzeugung des Gerichts", 110, 468, beim("prog2", "volle"), "Bold", 32),
    *wortlaut(110, 535, 1040, 70, "formel", [
        [("„… ", 0), ("mehr für eine Verurteilung", "a"), (" als für einen Freispruch spricht.“", 0)]], 28,
        {"a": beim("formel", "mehr")}, "OLG Düsseldorf, Beschl. v. 21.6.2023 – 4 Ws 73/23, Rn. 18"),
    z("nur verwertbare Beweise zählen", 110, 705, "verw", "Bold", 32),
    z("OLG Köln, Beschl. v. 24.6.2013 – 2 Ws 264/13, Rn. 13", 150, 752, "verw", size=26, farbe=TEXT),
    peep_voll("ME_ruhig", X1, BR, FR, "prog", bis="verw"),
    peep_voll("ME_denkt", X1, BR, FR, "verw", anim="cut"),
    peep_voll("SA_denkt", X2, BR, FR, "prog", d=0.2, bis="formel"),
    peep_voll("SA_ruhig", X2, BR, FR, "formel", anim="cut"),
    namensschild("Herr Mertens", X1, BR, "prog", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "prog", LILA, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "prog", fuell=GELB, bis="verw"),
    pl("Verurteilung wahrscheinlich?", MB, 160, beim("prog", "wahrscheinlich"), fill=GELB, size=28, anker="m", bis="formel"),
    pl("mehr für Verurteilung", MB, 160, beim("formel", "mehr"), fill=GRUEN, size=28, anker="m", anim="cut", bis="verw"),
    ficon("tabler", "file-check", MB, 380, 100, "verw", fuell=WEISS, anim="cut"),
    pl("verwertbar?", MB, 160, "verw", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# H Beweistabelle ---------------------------------------------------------------------------------------------------------------
PT = "Beweistabelle"
C1, C2, C3 = 110, 440, 820
folie([("tab", f"{PT} · Klausurtechnik"), ("tab1", f"{PT} › Merkmal: Wegnahme"), ("tab2", f"{PT} › belastend: Frau Hesse"),
       ("tab3", f"{PT} › entlastend: Bestreiten"), ("tab4", f"{PT} › § 160 Abs. 2 StPO")], rechts_frei([
    *tafel("tab", "Beweistabelle"),
    z("Merkmal", C1, 185, "tab", "ExtraBold", 32),
    z("belastend", C2, 185, "tab", "ExtraBold", 32, farbe=DROT),
    z("entlastend", C3, 185, "tab", "ExtraBold", 32, farbe=DGRUEN),
    linienzug([(100, 240), (1160, 240)], "tab", breite=4, farbe=INK),
    linienzug([(420, 185), (420, 500)], "tab", breite=4, farbe=INK),
    linienzug([(800, 185), (800, 500)], "tab", breite=4, farbe=INK),
    z("Wegnahme", C1, 265, "tab1", "Bold", 30),
    z("durch Herrn", C1, 305, "tab1", "Bold", 30),
    z("Mertens?", C1, 345, "tab1", "Bold", 30),
    z("Zeugin Frau Hesse:", C2, 265, "tab2", "Bold", 30, rechts=790),
    z("kennt ihn seit Jahren", C2, 315, beim("tab2", "kennt"), size=29, rechts=790),
    z("es war hell", C2, 360, beim("tab2", "hell"), size=29, rechts=790),
    z("bei der Polizei", C2, 405, beim("tab2", "Polizei"), size=29, rechts=790),
    z("dasselbe wie am Mittag", C2, 445, beim("tab2", "dasselbe"), size=29, rechts=790),
    z("sein Bestreiten", C3, 265, "tab3", "Bold", 30),
    z("Alibi: bestätigt", C3, 315, beim("tab3", "Alibi"), size=29),
    z("niemand", C3, 355, beim("tab3", "niemand"), size=29),
    fl_block(110, 560, 1040, 120, HELL, "tab4", [("§ 160 Abs. 2 StPO: auch entlastende", "Bold", 32, INK),
                                               ("Umstände ermitteln", "Bold", 32, INK)]),
    peep_voll("HE_ruhig", X1, BR, FR, "tab", bis="tab2"),
    peep_voll("HE_froh", X1, BR, FR, "tab2", anim="cut", bis="tab3"),
    peep_voll("HE_denkt", X1, BR, FR, "tab3", anim="cut"),
    peep_voll("ME_ruhig", X2, BR, FR, "tab", d=0.2, bis="tab3"),
    peep_voll("ME_denkt", X2, BR, FR, "tab3", anim="cut"),
    namensschild("Frau Hesse", X1, BR, "tab", GRUEN, d=0.2),
    namensschild("Herr Mertens", X2, BR, "tab", ROT, d=0.3),
    ficon("tabler", "clipboard-list", MB, 380, 100, "tab", fuell=WEISS, bis="tab2"),
    pl("Beweistabelle", MB, 160, "tab", fill=WEISS, size=30, anker="m", bis="tab2"),
    ficon("tabler", "eye", MB, 380, 110, "tab2", fuell=GELB, anim="cut", bis="tab3"),
    pl("belastend", MB, 160, "tab2", fill=ROTHELL, size=30, anker="m", anim="cut", bis="tab3"),
    ficon("tabler", "user-question", MB, 380, 100, "tab3", fuell=WEISS, anim="cut"),
    pl("entlastend", MB, 160, "tab3", fill=GRUENHELL, size=30, anker="m", anim="cut"),
]))

# I Aussage gegen Aussage ---------------------------------------------------------------------------------------------------------
PA = "Aussage gegen Aussage"
folie([("aga", PA), ("bgh6", f"{PA} › nicht vorab nach Aktenlage entscheiden"), ("hv", f"{PA} › Klärung in der Hauptverhandlung")],
      rechts_frei([
    *tafel("aga", "Aussage gegen Aussage"),
    fl_block(110, 180, 460, 110, ROTHELL, beim("aga", "Aussage"), [("Frau Hesse: Zeugin", "ExtraBold", 32, INK)]),
    z("gegen", 595, 212, beim("aga", "gegen"), "ExtraBold", 34),
    fl_block(710, 180, 440, 110, GRUENHELL, beim("aga", "Aussage", 2), [("Herr Mertens: bestreitet", "ExtraBold", 30, INK)]),
    *wortlaut(110, 335, 1040, 235, "bgh6", [
        [("„In einem derartigen ", 0), ("Zweifelsfall", "d"), (" dürfen diffizile", 0)],
        [("Beweiswürdigungsfragen nicht im Zuge einer vorläufigen", 0)],
        [("Tatbewertung ", 0), ("auf Aktenbasis", "a"), (", ohne den ", 0), ("unmittelbaren Eindruck", "b")],
        [("gerade des Personalbeweises auf das erkennende Gericht,", 0)],
        [("womöglich ", 0), ("endgültig entschieden", "c"), (" werden …“", 0)],
    ], 30, {"d": beim("bgh6", "Zweifelsfällen"), "a": beim("bgh6", "Aktenlage"), "b": beim("bgh6", "unmittelbaren"),
            "c": beim("bgh6", "endgültig")}, "BGH, Beschl. v. 10.12.2025 – StB 58/25, Rn. 6 (zu § 203 StPO)"),
    fl_block(110, 660, 1040, 120, GELB, "hv", [("Ob Frau Hesse sich irrt, klärt das Gericht", "ExtraBold", 32, INK),
                                             ("in der Hauptverhandlung", "Bold", 32, INK)]),
    peep_voll("HE_ruhig", X1, BR, FR, "aga", bis="hv"),
    peep_voll("HE_sorge", X1, BR, FR, "hv", anim="cut"),
    peep_voll("ME_ruhig", X2, BR, FR, "aga", d=0.2),
    namensschild("Frau Hesse", X1, BR, "aga", GRUEN, d=0.2),
    namensschild("Herr Mertens", X2, BR, "aga", ROT, d=0.3),
    ficon("tabler", "folders", MB, 380, 110, beim("bgh6", "Aktenlage"), fuell=GELB, bis="hv"),
    pl("nicht nach Aktenlage", MB, 160, beim("bgh6", "Aktenlage"), fill=WEISS, size=28, anker="m", bis="hv"),
    ficon("tabler", "gavel", MB, 380, 110, "hv", fuell=HOLZ, anim="cut"),
    pl("Hauptverhandlung", MB, 160, "hv", fill=GELB, size=30, anker="m", anim="cut"),
]))

# J „Im Zweifel für den Angeklagten“? --------------------------------------------------------------------------------------------
PI = "Im Zweifel für den Angeklagten?"
folie([("idpr", PI), ("idpr2", f"{PI} › grundsätzlich noch nicht"), ("idpr3", f"{PI} › nur mittelbar")], rechts_frei([
    *tafel("idpr", "„Im Zweifel für den Angeklagten“?", fill=LILAHELL, size=46),
    nein(135, 270, beim("idpr2", "grundsätzlich"), gr=20),
    z("Bei der Prüfung des hinreichenden Tatverdachts:", 175, 190, "idpr2", "Bold", 32),
    z("grundsätzlich noch nicht", 175, 240, beim("idpr2", "grundsätzlich"), "Bold", 32),
    z("nur mittelbar:", 110, 340, "idpr3", "ExtraBold", 34),
    z("Wird das Gericht nach Aktenlage am Ende", 150, 395, beim("idpr3", "Wird"), size=32),
    z("wahrscheinlich nach diesem Grundsatz", 150, 440, beim("idpr3", "wahrscheinlich"), size=32),
    z("freisprechen, fehlt der hinreichende Tatverdacht.", 150, 485, beim("idpr3", "freisprechen"), size=32),
    z("OLG Düsseldorf, Beschl. v. 21.6.2023 – 4 Ws 73/23, Rn. 18", 150, 560, beim("idpr3", "fehlt"), size=26, farbe=TEXT),
    peep_voll("ME_ruhig", X1, BR, FR, "idpr", bis="idpr2"),
    peep_voll("ME_sorge", X1, BR, FR, "idpr2", anim="cut", bis="idpr3"),
    peep_voll("ME_denkt", X1, BR, FR, "idpr3", anim="cut"),
    peep_voll("SA_skeptisch", X2, BR, FR, "idpr", d=0.2),
    namensschild("Herr Mertens", X1, BR, "idpr", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "idpr", LILA, d=0.3),
    ficon("fluent-emoji-flat", "red-question-mark", MB, 380, 90, "idpr", bis="idpr3"),
    pl("noch nicht", MB, 160, "idpr2", fill=ROTHELL, size=30, anker="m", bis="idpr3"),
    ficon("tabler", "scale", MB, 380, 110, "idpr3", fuell=GELB, anim="cut"),
    pl("nur mittelbar", MB, 160, "idpr3", fill=LILA, size=30, anker="m", anim="cut"),
]))

# K Beurteilungsspielraum und Ergebnis ------------------------------------------------------------------------------------------
PK = "Ergebnis"
folie([("spiel", f"{PK} › Beurteilungsspielraum"), ("erg", f"{PK} › mehr spricht für eine Verurteilung"),
       ("ankl", f"{PK} › hinreichender Tatverdacht: Anklage")], rechts_frei([
    *tafel("spiel", "Ergebnis im Fall"),
    fl_block(110, 175, 1040, 120, LILAHELL, "spiel", [("Beurteilungsspielraum der Staatsanwaltschaft", "ExtraBold", 32, INK),
                                                     ("mehr als eine vertretbare Entscheidung", "Bold", 30, INK)]),
    z("OLG Hamm, Urt. v. 17.2.2021 – 11 U 51/19, Rn. 42;", 110, 308, beim("spiel", "Es"), size=26, farbe=TEXT),
    z("BGH, Urt. v. 13.2.2025 – III ZR 63/24, Rn. 26", 110, 343, beim("spiel", "Es"), size=26, farbe=TEXT),
    z("Für eine Verurteilung spricht:", 110, 410, "erg", "ExtraBold", 34),
    ok(135, 485, beim("erg", "kennt"), gr=20),
    z("Die Zeugin kennt Herrn Mertens", 175, 465, beim("erg", "kennt"), size=32),
    ok(135, 535, beim("erg", "sah"), gr=20),
    z("sah ihn aus der Nähe", 175, 515, beim("erg", "sah"), size=32),
    ok(135, 585, beim("erg", "bleibt"), gr=20),
    z("bleibt bei ihrer Aussage", 175, 565, beim("erg", "bleibt"), size=32),
    fl_block(110, 660, 1040, 120, GRUEN, "ankl", [("hinreichender Tatverdacht:", "ExtraBold", 34, INK),
                                                 ("Anklage, § 170 Abs. 1 StPO", "Bold", 32, INK)]),
    peep_voll("ME_ruhig", X1, BR, FR, "spiel", bis="ankl"),
    peep_voll("ME_schreck", X1, BR, FR, "ankl", anim="cut"),
    peep_voll("SA_denkt", X2, BR, FR, "spiel", d=0.2, bis="ankl"),
    peep_voll("SA_froh", X2, BR, FR, beim("ankl", "erhebt"), anim="cut"),
    peep_voll("SA_ruhig", X2, BR, FR, "ankl", anim="cut", bis=beim("ankl", "erhebt")),
    namensschild("Herr Mertens", X1, BR, "spiel", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "spiel", LILA, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "spiel", fuell=LILA, bis="ankl"),
    pl("vertretbar?", MB, 160, "spiel", fill=WEISS, size=30, anker="m", bis="erg"),
    pl("mehr für Verurteilung", MB, 160, "erg", fill=GRUEN, size=28, anker="m", anim="cut", bis="ankl"),
    ficon("tabler", "file-check", MB, 380, 100, "ankl", fuell=GRUEN, anim="cut"),
    pl("Anklage", MB, 160, beim("ankl", "Anklage"), fill=GRUEN, size=30, anker="m"),
]))

# L Gegenfall: Einstellung, Klageerzwingung ---------------------------------------------------------------------------------------
PG = "Gegenfall"
folie([("gegen", f"{PG} · unsichere Zeugin"), ("gegen2", f"{PG} › Einstellung, § 170 Abs. 2 StPO"),
       ("kez", f"{PG} › Klageerzwingungsverfahren, §§ 172 ff. StPO")], rechts_frei([
    *tafel("gegen", "Gegenfall: unsichere Zeugin", fill=ROTHELL, size=46),
    z("nur eine Gestalt von hinten gesehen", 110, 190, beim("gegen", "Gestalt"), "Bold", 34),
    z("Angaben geändert", 110, 245, beim("gegen", "Angaben"), "Bold", 34),
    z("Freispruch wahrscheinlicher", 110, 345, "gegen2", "ExtraBold", 36),
    fl_block(110, 420, 1040, 110, WEISS, beim("gegen2", "stellt"), [("Einstellung, § 170 Abs. 2 StPO", "ExtraBold", 34, INK)]),
    z("Verletzte: Klageerzwingungsverfahren,", 110, 590, "kez", "Bold", 34),
    z("§§ 172 ff. StPO", 150, 645, beim("kez", "Paragrafen"), "Bold", 34),
    peep_voll("HE_sorge", X1, BR, FR, "gegen", bis="kez"),
    peep_voll("HE_ruhig", X1, BR, FR, "kez", anim="cut"),
    peep_voll("WE_ruhig", X2, BR, FR, "gegen", d=0.2, bis="gegen2"),
    peep_voll("WE_sorge", X2, BR, FR, "gegen2", anim="cut", bis="kez"),
    peep_voll("WE_denkt", X2, BR, FR, "kez", anim="cut"),
    namensschild("Frau Hesse", X1, BR, "gegen", GRUEN, d=0.2),
    namensschild("Frau Wessel", X2, BR, "gegen", BLAU, d=0.3),
    ficon("tabler", "user-question", MB, 380, 100, "gegen", fuell=WEISS, bis="gegen2"),
    pl("Gestalt von hinten", MB, 160, beim("gegen", "Gestalt"), fill=WEISS, size=28, anker="m", bis="gegen2"),
    ficon("tabler", "file-x", MB, 380, 100, "gegen2", fuell=ROT, anim="cut", bis="kez"),
    pl("Einstellung", MB, 160, beim("gegen2", "stellt"), fill=ROTHELL, size=30, anker="m", bis="kez"),
    ficon("tabler", "building-bank", MB, 380, 120, "kez", fuell=BLAU, anim="cut"),
    pl("Klageerzwingung", MB, 160, "kez", fill=BLAU, size=28, anker="m", anim="cut"),
]))

# M Eröffnung, § 203 StPO, und Ausblick §§ 153, 153a ---------------------------------------------------------------------------
PM = "Nach der Anklage"
folie([("p203", f"{PM} › Eröffnung, § 203 StPO"), ("opp", "Ausblick › §§ 153, 153a StPO")], rechts_frei([
    *tafel("p203", "Nach der Anklage: § 203 StPO", size=46),
    z("Das Gericht prüft denselben Maßstab noch einmal.", 110, 180, beim("p203", "Nach"), "Bold", 34),
    *wortlaut(110, 245, 1040, 190, beim("p203", "Es"), [
        [("„Das Gericht beschließt die Eröffnung des Hauptverfahrens,", 0)],
        [("wenn nach den Ergebnissen des vorbereitenden Verfahrens", 0)],
        [("der Angeschuldigte einer Straftat ", 0), ("hinreichend verdächtig", "a")],
        [("erscheint.“", 0)],
    ], 30, {"a": beim("p203", "hinreichend")}, "§ 203 StPO"),
    fl_block(110, 520, 1040, 300, LILAHELL, "opp", [("", "Bold", 30, INK)]),
    z("Ausblick bei Vergehen:", 140, 545, "opp", "ExtraBold", 34),
    z("§ 153 StPO: geringe Schuld, kein öffentliches Interesse", 150, 610, beim("opp", "Paragraf"), size=31),
    z("§ 153a StPO: vorläufig, gegen Auflagen", 150, 665, beim("opp", "hundertdreiundfünfzig", 2), size=31),
    z("ein eigenes Thema", 150, 735, beim("opp", "Das"), "Bold", 31, farbe=TEXT),
    peep_voll("ME_sorge", X1, BR, FR, "p203", bis="opp"),
    peep_voll("ME_denkt", X1, BR, FR, "opp", anim="cut"),
    peep_voll("SA_ruhig", X2, BR, FR, "p203", d=0.2),
    namensschild("Herr Mertens", X1, BR, "p203", ROT, d=0.2),
    namensschild("Staatsanwalt", X2, BR, "p203", LILA, d=0.3),
    ficon("tabler", "gavel", MB, 380, 110, "p203", fuell=HOLZ, bis="opp"),
    pl("Eröffnung?", MB, 160, beim("p203", "Es"), fill=WEISS, size=30, anker="m", bis="opp"),
    ficon("tabler", "list-check", MB, 380, 100, "opp", fuell=WEISS, anim="cut"),
    pl("Opportunität", MB, 160, "opp", fill=LILA, size=30, anker="m", anim="cut"),
]))

# N Abschlussverfügung (Klausurkonvention) --------------------------------------------------------------------------------------
folie([("verf", "Klausur › Abschlussverfügung"), ("verf3", "Klausur › Abschlussverfügung: Klausurkonvention")], rechts_frei([
    *tafel("verf", "Abschlussverfügung"),
    karte(140, 190, 960, 330, "verf", fill=HELL, rund=10, schatten=6),
    z("Verfügung", 180, 215, "verf", "ExtraBold", 36),
    z("1. Vermerk: Die Ermittlungen sind abgeschlossen.", 180, 290, "verf1", "Bold", 32, rechts=1080),
    z("§ 169a StPO", 220, 340, beim("verf1", "Paragraf"), size=30, farbe=TEXT, rechts=1080),
    z("2. Anklageschrift (§ 170 Abs. 1 StPO)", 180, 420, "verf2", "Bold", 32, rechts=1080),
    fl_block(110, 600, 1040, 120, LILAHELL, "verf3", [("Klausurkonvention:", "ExtraBold", 34, INK),
                                                     ("von Land zu Land verschieden", "Bold", 32, INK)]),
    peep_voll("SA_ruhig", XS, BR, FR, "verf", bis="verf2"),
    peep_voll("SA_froh", XS, BR, FR, "verf2", anim="cut"),
    namensschild("Staatsanwalt", XS, BR, "verf", LILA, d=0.2),
    ficon("tabler", "file-certificate", XS, 380, 100, "verf", fuell=GELB, bis="verf3"),
    pl("Abschlussverfügung", XS, 160, "verf", fill=GELB, size=30, anker="m", bis="verf3"),
    ficon("tabler", "map-pin", XS, 380, 90, "verf3", fuell=ROT, anim="cut"),
    pl("von Land zu Land", XS, 160, "verf3", fill=LILA, size=30, anker="m", anim="cut"),
]))

# O Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Glaubhaftigkeit nicht endgültig entscheiden"), ("tipp3", "Klausurtipp · kein bloßes „im Zweifel“")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nicht endgültig entscheiden, ob die", 200, 200, beim("tipp", "Entscheide"), "Bold", 36),
    z("Zeugin die Wahrheit sagt", 200, 250, beim("tipp", "Zeugin"), "Bold", 36),
    z("Was spricht für, was gegen ihre Aussage?", 200, 345, "tipp2", size=34),
    z("Wie entscheidet das Gericht voraussichtlich", 200, 400, beim("tipp2", "wie"), size=34),
    z("nach der Hauptverhandlung?", 200, 450, beim("tipp2", "Hauptverhandlung"), size=34),
    nein(220, 560, beim("tipp3", "Im"), gr=18),
    z("Einstellung nie allein mit:", 260, 535, "tipp3", "Bold", 36),
    z("„Im Zweifel für den Angeklagten“", 260, 590, beim("tipp3", "Im"), "Bold", 36),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# P Prüfschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Strafbarkeit und Verfolgbarkeit"), ("s2", "Prüfschema › II. Beweistabelle"),
       ("s3", "Prüfschema › III. Prognose"), ("s4", "Prüfschema › IV. Ergebnis")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: hinreichender Tatverdacht", 110, 90, "sch", 54),
    z("I. Strafbarkeit und Verfolgbarkeit nach der Akte", K1, 200, "s1", "Bold", 38, rechts=1820),
    z("II. Beweistabelle", K1, 300, "s2", "Bold", 38, rechts=1820),
    z("belastende und entlastende Beweise – nur verwertbare", K2, 355, beim("s2", "belastende"), size=34, farbe=TEXT,
      rechts=1820),
    z("III. Prognose", K1, 455, "s3", "Bold", 38, rechts=1820),
    z("ohne die Hauptverhandlung vorwegzunehmen", K2, 510, beim("s3", "ohne"), size=34, farbe=TEXT, rechts=1820),
    z("IV. Ergebnis", K1, 610, "s4", "Bold", 38, rechts=1820),
    z("Verurteilung wahrscheinlich: Anklage, § 170 Abs. 1 StPO", K2, 665, beim("s4", "Ist"), size=34, rechts=1820),
    z("sonst: Einstellung, § 170 Abs. 2 StPO", K2, 720, beim("s4", "sonst"), size=34, rechts=1820),
])

# Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Angeklagt wird, wenn eine", 0)], [("Verurteilung ", 0), ("wahrscheinlich", "a"), (" ist.", 0)]],
                750, 300, 50, "merke", {"a": beim("merke", "wahrscheinlich")}),
    *markertext([[("Ob die einzige Zeugin recht hat,", 0)], [("entscheidet am Ende das Gericht", 0)],
                 [("in der ", 0), ("Hauptverhandlung", "b"), (".", 0)]], 750, 520, 46, "mz",
                {"b": beim("mz", "Hauptverhandlung")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
