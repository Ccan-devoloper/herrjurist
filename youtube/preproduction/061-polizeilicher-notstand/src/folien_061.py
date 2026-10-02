"""Folge 061 · Polizeilicher Notstand: Muss ein Vermieter Obdachlose aufnehmen? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Winter, Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Wohnung im Winter
(Frau Brandt, zwei Kinder, Herr Bauer, Räumungsurteil), B Ordnungsamt (Herr Schmitz, Notunterkünfte belegt), C Die
Verfügung (Beschlagnahme, Wiedereinweisung, Herr Bauer am Briefkasten), D Frage, E Sachverhalt, F Landesrecht und
Zuständigkeit, G Ermächtigungsgrundlage und Gefahr, H Verantwortliche und Nichtstörer, I Wortlaut § 19 I OBG NRW,
J Nr. 1 und 2, K Nr. 3 (Kern), L Nr. 4, Dauer, Verhältnismäßigkeit, M Ergebnis und Variante, N Entschädigung mit
Wortlaut § 39 I OBG NRW, O Folgenbeseitigung nach Fristablauf, P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Tastatur am Ordnungsamt (Szene B), Brief in den Briefkasten (Szene C)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_061/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HOLZ = (236, 214, 178, 255)
WAND = (226, 218, 205, 255)
ZARTROT = (255, 240, 236, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf; Mindestschrift 26 px (mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26, rechts=1170):
    """Fundstellenzeile (grau, klein, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, rechts=rechts)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_061/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach der amtlichen Quelle (recht.nrw.de), als Zitat mit Normangabe; feste
    Zeilen ergeben zusammen genau den Normtext. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen
    Textmarker hinter die Wortgruppe (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    assert " ".join(t.strip() for t in zeilen) == text, "feste Zeilen weichen vom Normtext ab"
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} steht nicht in einer Zeile: {zeilen}"
        t = zeilen[zi]; a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", 26, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
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


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


def kinder(cx, unten, cue, anim="pop", bis=None, gr=110):
    """Die zwei Kinder als Linien-Icons (Fluent Emoji High Contrast „child“), keine Comicfiguren."""
    return [ficon(HC, "child", cx - 62, unten, gr, cue, fuell=WEISS, anim=anim, bis=bis),
            ficon(HC, "child", cx + 62, unten, int(gr * 0.86), cue, fuell=WEISS, anim=anim, bis=bis)]


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BR_F, BA_F, SC_F = BLAU, GRUEN, GELB        # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270

# A Fall: Winter, die Wohnung ------------------------------------------------------------------------------------------------
BRX, BAX = 820, 1600
BRb = ("BR_redet_r", BRX, BODEN, FH)
folie([(NULL, "Fall · Dezember, die Mietwohnung")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Dezember", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "window", 300, 560, 220, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "snowflake", 250, 440, 60, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "snowflake", 350, 500, 50, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "sofa", 300, BODEN - 2, 260, NULL, fuell=LILA, anim="cut"),
    *fig("BR", BRX, BODEN, FH, [(NULL, "ruhig_r"), (beim("job", "Jobverlust"), "sorge_r")], bis="br1", erst="cut"),
    *redet("BR_redet_r", BRX, BODEN, FH, "br1", "amt"),
    hart(schild("Frau Brandt, Mieterin", BRX, NULL, BR_F, unten=BODEN, d=0.0)),
    *kinder(1060, BODEN - 2, beim("fam", "zwei")),
    pl("2 Kinder", 1060, BODEN + 22, beim("fam", "zwei"), fill=WEISS, size=28, anker="m"),
    *fig("BA", BAX, BODEN, FH, [(beim("fam", "Bauer"), "ruhig"), ("urteil", "aerger"), ("br1", "denkt")]),
    schild("Herr Bauer, Vermieter", BAX, beim("fam", "Bauer"), BA_F, unten=BODEN),
    ficon("tabler", "receipt-euro", 1250, 420, 100, beim("job", "Miete"), fuell=GELB, bis=beim("urteil", "gekündigt")),
    pl("Miete offen", 1250, 450, beim("job", "Miete"), fill=GELB, size=30, anker="m", bis=beim("urteil", "gekündigt")),
    ficon("tabler", "gavel", 1250, 420, 110, beim("urteil", "gekündigt"), fuell=WEISS, bis="br1"),
    pl("Kündigung", 1250, 450, beim("urteil", "gekündigt"), fill=WEISS, size=30, anker="m", bis="br1"),
    pl("Räumungsurteil", 1250, 510, beim("urteil", "Räumungsurteil"), fill=WEISS, size=30, anker="m", bis="br1"),
    ficon("tabler", "calendar-event", 1250, 690, 90, beim("termin", "fünfzehnten"), fuell=ROT, bis="br1"),
    pl("Räumung am 15.1.", 1250, 710, beim("termin", "fünfzehnten"), fill=ROT, size=30, anker="m", bis="br1"),
    blase("sprech", 700, 220, "br1", 1180, 300, inhalt=["Ich finde keine Wohnung. Wo sollen", "wir mit den Kindern hin?"],
          textsize=31, figur=BRb),
])

# B Fall: Beim Ordnungsamt ---------------------------------------------------------------------------------------------------
BR2, SCX = 520, 1500
SCb = ("SC_redet", SCX, BODEN, FH)
folie([("amt", "Fall · Beim Ordnungsamt")], [
    linienzug([(60, BODEN), (1860, BODEN)], "amt", breite=7, farbe=INK),
    pl("Beim Ordnungsamt der Stadt", 70, 40, "amt", fill=GELB, size=40),
    karte(950, BODEN - 190, 380, 188, "amt", fill=HOLZ, rund=10, schatten=0, rand=4),
    ficon("tabler", "device-desktop", 1080, BODEN - 190, 150, "amt", fuell=BLAU),
    *fig("BR", BR2, BODEN, FH, [("amt", "sorge_r")]),
    schild("Frau Brandt", BR2, "amt", BR_F, unten=BODEN),
    *kinder(260, BODEN - 2, "amt"),
    *fig("SC", SCX, BODEN, FH, [(beim("voll", "Schmitz"), "ruhig"), ("hotel", "denkt")], bis="sc1"),
    *redet("SC_redet", SCX, BODEN, FH, "sc1", "verf"),
    schild("Herr Schmitz, Ordnungsamt", SCX, beim("voll", "Schmitz"), SC_F, unten=BODEN),
    szene(ficon("tabler", "keyboard", 1210, BODEN - 192, 90, beim("voll", "prüft"), fuell=WEISS), "061tastatur*", 0.8, 0.0),
    ficon("ph", "bed", 1000, 330, 110, beim("voll", "Notunterkünfte"), fuell=LILA, bis="sc1"),
    pl("Notunterkünfte der Stadt", 1000, 360, beim("voll", "Notunterkünfte"), fill=WEISS, size=28, anker="m", bis="sc1"),
    pl("alle belegt", 1000, 420, beim("voll", "belegt"), fill=ROT, size=30, anker="m", bis="sc1"),
    ficon(HC, "hotel", 1680, 330, 110, beim("hotel", "Hotels"), fuell=WEISS),
    pl("Hotels, Pensionen:", 1680, 360, beim("hotel", "Hotels"), fill=WEISS, size=28, anker="m"),
    pl("nicht gefragt", 1680, 420, beim("hotel", "fragt"), fill=ROT, size=30, anker="m"),
    blase("sprech", 660, 210, "sc1", 1080, 220, inhalt=["Dann bleibt nur eins: Wir weisen", "Sie wieder in Ihre Wohnung ein."],
          textsize=30, figur=SCb),
])

# C Fall: Die Verfügung -------------------------------------------------------------------------------------------------------
HX, BA3 = 520, 1450
BAb = ("BA_redet", BA3, BODEN, FH)
folie([("verf", "Fall · Die Verfügung")], [
    linienzug([(60, BODEN), (1860, BODEN)], "verf", breite=7, farbe=INK),
    pl("Die Stadt verfügt", 70, 40, "verf", fill=GELB, size=40),
    ficon("ph", "house", HX, BODEN - 2, 380, "verf", fuell=WEISS),
    pl("Wohnung von Herrn Bauer", HX, 290, "verf", fill=WEISS, size=28, anker="m"),
    pl("beschlagnahmt", HX, 350, beim("verf", "beschlagnahmt"), fill=ROT, size=32, anker="m"),
    *kinder(HX, BODEN - 40, beim("verf", "Familie"), gr=100),
    pl("Familie wieder eingewiesen: 3 Monate", HX, 420, beim("verf", "Monate"), fill=GELB, size=30, anker="m"),
    szene(ficon("tabler", "mailbox", 1080, BODEN - 2, 160, beim("post", "Bauer"), fuell=BLAU), "061brief*", 0.8, 0.0),
    ficon("tabler", "file-text", 1080, 600, 100, beim("post", "Verfügung"), fuell=WEISS),
    pl("Ordnungsverfügung", 1080, 630, beim("post", "Verfügung"), fill=WEISS, size=28, anker="m"),
    *fig("BA", BA3, BODEN, FH, [(beim("post", "Bauer"), "aerger")], bis="ba1"),
    *redet("BA_redet", BA3, BODEN, FH, "ba1", "frage"),
    schild("Herr Bauer", BA3, beim("post", "Bauer"), BA_F, unten=BODEN),
    blase("sprech", 820, 230, "ba1", 1240, 210, inhalt=["Ich habe ein Urteil! Warum muss", "ausgerechnet ich die Familie", "aufnehmen?"],
          textsize=30, figur=BAb),
])

# D Die Frage -----------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Muss Herr Bauer die Familie aufnehmen?")], [
    pl("Darf die Stadt Herrn Bauer dazu zwingen?", 640, 90, beim("frage", "Darf"), fill=PINK, size=42, anker="m"),
    ficon("ph", "house", 420, 560, 220, beim("frage", "Herrn"), fuell=WEISS),
    *kinder(800, 560, beim("frage", "zwingen"), gr=110),
    ficon("tabler", "coin-euro", 640, 730, 110, beim("frage2", "Geld"), fuell=GELB),
    pl("Und bekommt er dafür Geld?", 640, 760, beim("frage2", "Geld"), fill=GELB, size=42, anker="m"),
    *fig("BA", FX, FB, FR, [("frage", "denkt")]),
    schild("Herr Bauer", FX, "frage", BA_F),
])

# E Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Nordrhein-Westfalen, Dezember: Frau Brandt wohnt mit ihren zwei Kindern zur Miete bei Herrn Bauer. Nach einem "
    "Jobverlust konnte sie die Miete monatelang nicht zahlen. Herr Bauer hat gekündigt und ein Räumungsurteil erstritten; "
    "der Gerichtsvollzieher räumt am 15. Januar. Frau Brandt findet keine Wohnung. Herr Schmitz vom Ordnungsamt prüft die "
    "Notunterkünfte der Stadt: alle belegt. Bei Hotels und Pensionen fragt er nicht nach. Die Stadt beschlagnahmt die "
    "Wohnung und weist die Familie für drei Monate wieder ein. Herr Bauer wehrt sich.",
], "Muss Herr Bauer die Familie aufnehmen? Bekommt er Geld?")

# F Landesrecht und Zuständigkeit ----------------------------------------------------------------------------------------------
folie([("land", "Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen"),
       ("zust", "Prüfung › formell: Zuständigkeit, §§ 3 I, 5 I OBG NRW")], rechts_frei([
    *tafel("land", "Gefahrenabwehr ist Landesrecht"),
    z("Beispiel hier: Nordrhein-Westfalen", 110, 190, beim("land", "Nordrhein"), "Bold", 36),
    zit("OBG NRW (Fassung ab 1.7.2026), PolG NRW (ab 13.12.2025)", 150, 245, beim("land", "Beispiel")),
    z("andere Länder: ähnliche Regeln,", 110, 310, beim("land", "anderen"), size=34),
    z("oft unter anderer Nummer", 150, 365, beim("land", "Nummer"), size=34),
    z("formell: zuständig ist die Stadt", 110, 465, "zust", "Bold", 36),
    z("als örtliche Ordnungsbehörde", 150, 520, beim("zust", "örtliche"), size=34),
    zit("§§ 3 Abs. 1, 4 Abs. 1, 5 Abs. 1 OBG NRW", 150, 575, beim("zust", "Ordnungsbehörde")),
    ficon("tabler", "map", IX, IU, 150, "land", fuell=GRUEN, bis="zust"),
    ficon("tabler", "building", IX, IU, 140, "zust", fuell=WEISS),
    *fig("SC", FX, FB, FR, [("land", "ruhig")]),
    schild("Herr Schmitz", FX, "land", SC_F),
]))

# G Ermächtigungsgrundlage und Gefahr ------------------------------------------------------------------------------------------
folie([("egl", "Ermächtigungsgrundlage: Generalklausel, § 14 I OBG NRW"),
       ("obdach", "materiell › Gefahr: unfreiwillige Obdachlosigkeit")], rechts_frei([
    titel(glyphen("Grundlage und Gefahr"), 110, 75, "egl", 50),
    z("Generalklausel, § 14 Abs. 1 OBG NRW:", 110, 170, beim("egl", "Generalklausel"), "Bold", 34),
    z("„… Gefahr für die öffentliche Sicherheit oder Ordnung …“", 150, 225, "gefahr", size=33),
    blk(110, 300, 1040, 80, GELB, "obdach", [("unfreiwillige Obdachlosigkeit = Gefahr", "ExtraBold", 36, INK)]),
    z("bedroht: Leben und Gesundheit", 150, 400, beim("obdach", "Leben"), size=34),
    zit("OVG NRW, Beschl. v. 24.3.2023 – 9 B 95/23, Rn. 8", 150, 450, beim("obdach", "Gesundheit")),
    z("unfreiwillig: keine Unterkunft aus eigener Kraft", 110, 525, "unfrei", "Bold", 34),
    zit("VG Köln, Beschl. v. 13.1.2023 – 22 L 43/23, Rn. 9", 150, 580, beim("unfrei", "beschaffen")),
    ok(150, 668, beim("winter", "Hand"), gr=20),
    z("Winter, zwei Kinder: Gefahr liegt auf der Hand", 195, 645, beim("winter", "Winter"), size=34),
    ficon("tabler", "snowflake", IX, IU, 130, "egl", fuell=WEISS, bis="obdach"),
    ficon("tabler", "heart", IX, IU, 130, "obdach", fuell=ROT),
    *fig("BR", FX, FB, FR, [("egl", "sorge")]),
    schild("Frau Brandt", FX, "egl", BR_F),
]))

# H Verantwortliche und Nichtstörer ---------------------------------------------------------------------------------------------
folie([("stoerer", "materiell › Adressat: Verantwortliche, § 17 OBG NRW"),
       ("nicht", "materiell › Adressat: Nichtstörer"),
       ("notstand", "materiell › Adressat › polizeilicher Notstand, § 19 OBG NRW")], rechts_frei([
    *tafel("stoerer", "Gegen wen darf die Stadt vorgehen?", size=42),
    z("verantwortlich: Frau Brandt selbst,", 110, 185, beim("stoerer", "Verantwortlich"), "Bold", 34),
    z("§ 17 Abs. 1 OBG NRW", 150, 240, beim("stoerer", "siebzehn"), size=33),
    zit("vgl. VG Köln, Urt. v. 16.2.2022 – 22 K 838/20, Rn. 40", 150, 290, beim("stoerer", "Brandt")),
    nein(150, 383, beim("nicht", "nicht"), gr=18),
    z("Herr Bauer hat die Gefahr nicht verursacht", 195, 360, beim("nicht", "nicht"), size=34),
    blk(110, 430, 1040, 80, ROT, beim("nicht", "Nichtstörer"), [("Herr Bauer = Nichtstörer", "ExtraBold", 36, INK)]),
    zit("VG Köln, Beschl. v. 28.11.2022 – 22 L 1749/22, Rn. 25", 150, 525, beim("nicht", "Nichtstörer")),
    z("nur im polizeilichen Notstand, § 19 OBG NRW", 110, 600, "notstand", "Bold", 34),
    z("für die Polizei gleich: § 6 PolG NRW", 150, 660, "pol6", size=34),
    ficon("tabler", "users", IX, IU, 140, "stoerer", fuell=WEISS, bis="nicht"),
    ficon("ph", "house", IX, IU, 140, "nicht", fuell=WEISS),
    *fig("BA", FX, FB, FR, [("stoerer", "denkt"), ("notstand", "aerger")]),
    schild("Herr Bauer", FX, "stoerer", BA_F),
]))

# I Wortlaut § 19 Abs. 1 OBG NRW ------------------------------------------------------------------------------------------------
N = "polizeilicher Notstand"
W19 = ("„Die Ordnungsbehörde kann Maßnahmen gegen andere Personen als die nach den §§ 17 oder 18 Verantwortlichen richten, "
       "wenn 1. eine gegenwärtige erhebliche Gefahr abzuwehren ist, 2. Maßnahmen gegen die nach den §§ 17 oder 18 "
       "Verantwortlichen nicht oder nicht rechtzeitig möglich sind oder keinen Erfolg versprechen, 3. die Ordnungsbehörde "
       "die Gefahr nicht oder nicht rechtzeitig selbst oder durch Beauftragte abwehren kann und 4. die Personen ohne "
       "erhebliche eigene Gefährdung und ohne Verletzung höherwertiger Pflichten in Anspruch genommen werden können.“")
Z19 = ["„Die Ordnungsbehörde kann Maßnahmen gegen andere Personen als die",
       "nach den §§ 17 oder 18 Verantwortlichen richten, wenn",
       "1. eine gegenwärtige erhebliche Gefahr abzuwehren ist,",
       "2. Maßnahmen gegen die nach den §§ 17 oder 18 Verantwortlichen",
       "nicht oder nicht rechtzeitig möglich sind oder keinen Erfolg versprechen,",
       "3. die Ordnungsbehörde die Gefahr nicht oder nicht rechtzeitig",
       "selbst oder durch Beauftragte abwehren kann und",
       "4. die Personen ohne erhebliche eigene Gefährdung und ohne",
       "Verletzung höherwertiger Pflichten in Anspruch genommen werden können.“"]
w19, w19_y = wortlaut(70, 160, 1120, W19, "§ 19 Abs. 1 OBG NRW (für die Polizei gleichlautend: § 6 Abs. 1 PolG NRW)", "wl19",
                      marken=[("gegenwärtige erhebliche Gefahr", beim("n1", "gegenwärtige")),
                              ("Maßnahmen gegen die nach den §§ 17 oder 18 Verantwortlichen", "n2"),
                              ("keinen Erfolg versprechen", beim("n2", "Erfolg")),
                              ("selbst oder durch Beauftragte abwehren", beim("n3", "selbst")),
                              ("ohne erhebliche eigene Gefährdung", beim("n4", "ohne")),
                              ("Verletzung höherwertiger Pflichten", beim("n4", "Verletzung"))], size=30, zeilen=Z19)
folie([("wl19", f"{N} › Wortlaut § 19 I OBG NRW"), ("n1", f"{N} › § 19 I Nr. 1–4: alle vier Voraussetzungen")], rechts_frei([
    titel(glyphen("Polizeilicher Notstand: vier Voraussetzungen"), 100, 75, "wl19", 44),
    *w19,
    *fig("BA", FX, FB, FR, [("wl19", "denkt")]),
    schild("Herr Bauer", FX, "wl19", BA_F),
    ficon(HC, "balance-scale", IX, IU, 140, "wl19", fuell=GELB),
]))

# J Nr. 1 und Nr. 2 ---------------------------------------------------------------------------------------------------------
folie([("s1", f"{N} › Nr. 1: gegenwärtige erhebliche Gefahr"), ("s2", f"{N} › Nr. 2: Maßnahmen gegen Verantwortliche")],
      rechts_frei([
    *tafel("s1", "Nr. 1 und Nr. 2"),
    z("Nr. 1: Räumungstermin steht fest", 110, 185, "s1", "Bold", 34),
    ok(150, 263, beim("s1", "gegenwärtig"), gr=20),
    z("Schaden steht unmittelbar bevor: gegenwärtig", 195, 240, beim("s1", "unmittelbar"), size=34),
    zit("OVG NRW, Urt. v. 2.3.2021 – 5 A 942/19, Rn. 42", 195, 290, beim("s1", "gegenwärtig")),
    ok(150, 373, beim("s1b", "erheblich"), gr=20),
    z("Leben und Gesundheit: erheblich", 195, 350, beim("s1b", "Leben"), size=34),
    z("Nr. 2: Frau Brandt kann sich nicht selbst helfen", 110, 470, "s2", "Bold", 34),
    ok(150, 548, beim("s2", "Leere"), gr=20),
    z("Verfügung gegen sie liefe ins Leere", 195, 525, beim("s2", "Verfügung"), size=34),
    ficon("tabler", "calendar-event", IX, IU, 130, "s1", fuell=ROT, bis="s1b"),
    ficon("tabler", "heart", IX, IU, 130, "s1b", fuell=ROT, bis="s2"),
    *kinder(IX, IU, "s2", gr=110),
    *fig("BR", FX, FB, FR, [("s1", "sorge"), ("s2", "muede")]),
    schild("Frau Brandt", FX, "s1", BR_F),
]))

# K Nr. 3: Kann die Stadt selbst abwehren? ---------------------------------------------------------------------------------
folie([("s3", f"{N} › Nr. 3: eigene Abwehr durch die Stadt")], rechts_frei([
    *tafel("s3", "Nr. 3: Kann die Stadt selbst abwehren?", fill=ZARTROT, size=42),
    z("Vorrang: eigene Abwehr durch die Stadt", 110, 180, beim("s3", "Vorrang"), "Bold", 34),
    z("geschuldet: keine Wohnung, sondern eine", 110, 255, "unterk", size=34),
    z("menschenwürdige Unterkunft, Schutz vor Witterung", 150, 305, beim("unterk", "menschenwürdige"), size=34),
    zit("OVG NRW, Beschl. v. 24.3.2023 – 9 B 95/23, Rn. 6", 150, 355, beim("unterk", "Witterung")),
    z("eigene Plätze voll: Hotels, Pensionen,", 110, 420, "anmiet", size=34),
    z("Wohnungen anmieten", 150, 470, beim("anmiet", "anmieten"), size=34),
    zit("VG Köln, 22 L 1749/22, Rn. 28, 32, 34; 22 L 43/23, Rn. 29", 150, 520, beim("anmiet", "anmieten")),
    z("Kosten spielen keine Rolle", 110, 585, "kosten", "Bold", 34),
    z("hier: nur eigene Notunterkünfte geprüft,", 110, 660, "s3neg", size=34),
    z("dass nichts frei war, steht nicht fest", 150, 710, beim("s3neg", "nirgends"), size=34),
    nein(150, 803, beim("s3neg", "Nummer"), gr=18),
    blk(195, 770, 955, 70, ROT, beim("s3neg", "Nummer"), [("Nr. 3 nicht erfüllt", "ExtraBold", 34, INK)]),
    ficon("ph", "bed", 1420, 330, 120, "s3", fuell=LILA),
    ficon(HC, "hotel", 1700, 330, 120, beim("anmiet", "Hotels"), fuell=WEISS),
    ficon("tabler", "coin-euro", 1420, 520, 90, "kosten", fuell=GELB),
    *fig("SC", FX, FB, FR, [("s3", "ruhig"), ("s3neg", "denkt")]),
    schild("Herr Schmitz", FX, "s3", SC_F),
]))

# L Nr. 4, Dauer, Verhältnismäßigkeit ---------------------------------------------------------------------------------------
folie([("s4", f"{N} › Nr. 4: keine eigene Gefährdung"), ("frist", f"{N} › Dauer, § 19 II OBG NRW"),
       ("verh", "Ermessen › Verhältnismäßigkeit, § 15 OBG NRW")], rechts_frei([
    *tafel("s4", "Nr. 4, Dauer, Verhältnismäßigkeit", size=44),
    ok(150, 203, beim("s4", "Gefahr"), gr=20),
    z("Nr. 4: Herr Bauer gerät selbst nicht in Gefahr", 195, 180, beim("s4", "Bauer"), size=34),
    z("Dauer, § 19 Abs. 2 OBG NRW:", 110, 270, "frist", "Bold", 34),
    z("„Die Maßnahmen nach Absatz 1 dürfen nur aufrechterhalten", 150, 325, beim("frist", "Absatz"), size=30),
    z("werden, solange die Abwehr der Gefahr nicht auf", 150, 370, beim("frist", "Absatz"), size=30),
    z("andere Weise möglich ist.“", 150, 415, beim("frist", "Absatz"), size=30),
    pl("VG Köln: höchstens 6 Monate", 150, 470, beim("sechsm", "höchstens"), fill=GELB, size=32),
    zit("VG Köln, Beschl. v. 9.10.2020 – 22 L 1688/20, Rn. 18", 150, 545, beim("sechsm", "Monaten")),
    z("verhältnismäßig nur als letztes Mittel, § 15 OBG NRW", 110, 615, "verh", "Bold", 33),
    z("erst recht bei einem Räumungsurteil", 150, 670, beim("verh", "Räumungsurteil"), size=34),
    zit("VG Köln, Urt. v. 16.2.2022 – 22 K 838/20, Rn. 61", 150, 720, beim("verh", "Räumungsurteil")),
    ficon("tabler", "hourglass", IX, IU, 130, "frist", fuell=GELB, bis="verh"),
    ficon("tabler", "gavel", IX, IU, 130, "verh", fuell=WEISS),
    *fig("BA", FX, FB, FR, [("s4", "ruhig")]),
    schild("Herr Bauer", FX, "s4", BA_F),
]))

# M Ergebnis und Variante ----------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis"), ("anders", "Variante: Stadt hat alles versucht")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 85, ROT, beim("erg", "rechtswidrig"), [("Beschlagnahme rechtswidrig", "ExtraBold", 38, INK)]),
    z("Herr Bauer muss die Familie nicht aufnehmen,", 110, 300, beim("erg", "Herr"), size=34),
    z("die Stadt muss sie anders unterbringen", 150, 355, "erg2", size=34),
    z("Variante: Die Stadt hat nachweislich alles", 110, 470, "anders", "Bold", 34),
    z("versucht, und nichts ist frei", 150, 525, beim("anders", "nichts"), "Bold", 34),
    blk(110, 600, 1040, 85, GELB, "dulden", [("dann: Herr Bauer duldet für kurze Zeit", "ExtraBold", 36, INK)]),
    ficon(HC, "hotel", IX, IU, 130, "erg2", fuell=WEISS, bis="anders"),
    ficon("ph", "house", IX, IU, 130, "dulden", fuell=WEISS),
    *fig("BA", FX, FB, FR, [("erg", "froh"), ("anders", "denkt")]),
    schild("Herr Bauer", FX, "erg", BA_F),
]))

# N Entschädigung, Wortlaut § 39 I OBG NRW --------------------------------------------------------------------------------------
W39 = ("„Ein Schaden, den jemand durch Maßnahmen der Ordnungsbehörden erleidet, ist zu ersetzen, wenn er a) infolge einer "
       "Inanspruchnahme nach § 19 oder b) durch rechtswidrige Maßnahmen, gleichgültig, ob die Ordnungsbehörden ein "
       "Verschulden trifft oder nicht, entstanden ist.“")
Z39 = ["„Ein Schaden, den jemand durch Maßnahmen der Ordnungsbehörden",
       "erleidet, ist zu ersetzen, wenn er",
       "a) infolge einer Inanspruchnahme nach § 19 oder",
       "b) durch rechtswidrige Maßnahmen, gleichgültig, ob die",
       "Ordnungsbehörden ein Verschulden trifft oder nicht,",
       "entstanden ist.“"]
w39, w39_y = wortlaut(80, 150, 1100, W39, "§ 39 Abs. 1 OBG NRW (§ 19 = Nichtstörer)", "wl39", marken=[
    ("ist zu ersetzen,", beim("wl39", "ersetzt")), ("infolge einer Inanspruchnahme nach § 19", beim("wl39", "Inanspruchnahme")),
    ("durch rechtswidrige Maßnahmen,", beim("wl39", "rechtswidrige"))], size=29, zeilen=Z39)
folie([("entsch", "Entschädigung, § 39 I OBG NRW"), ("regress", "Entschädigung › Rückgriff, § 42 II OBG NRW")], rechts_frei([
    titel(glyphen("Und das Geld?"), 110, 70, "entsch", 50),
    *w39,
    ok(150, w39_y + 48, beim("beide", "beiden"), gr=20),
    z("in beiden Fällen Geld (a oder b)", 195, w39_y + 25, beim("beide", "beiden"), "Bold", 34),
    zit("VG Köln, Urt. v. 16.2.2022 – 22 K 838/20, Rn. 47–49", 195, w39_y + 75, beim("beide", "Geld")),
    z("vor allem: entgangene Miete (§ 40 Abs. 1: Vermögensschäden)", 110, w39_y + 135, "miete", size=32),
    z("auch danach, wenn sonst früher geräumt worden wäre", 110, w39_y + 190, "danach", size=32),
    zit("OLG Köln, Urt. v. 16.9.1993 – 7 U 83/93, Rn. 21", 150, w39_y + 238, beim("danach", "Oberlandesgericht")),
    z("rechtmäßig: Rückgriff bei der Familie, § 42 Abs. 2 OBG NRW", 110, w39_y + 295, "regress", size=32),
    ficon("tabler", "coin-euro", IX, IU, 130, "entsch", fuell=GELB),
    *fig("BA", FX, FB, FR, [("entsch", "denkt"), ("beide", "froh")]),
    schild("Herr Bauer", FX, "entsch", BA_F),
]))

# O Nach Fristablauf: Folgenbeseitigung -----------------------------------------------------------------------------------------
folie([("ende", "Nach Fristablauf › Folgenbeseitigung"), ("streit", "Nach Fristablauf › Streit: Wiedereinweisung")],
      rechts_frei([
    *tafel("ende", "Und wenn die Frist abläuft?"),
    z("Folgenbeseitigungsanspruch des Vermieters:", 110, 185, "fba", "Bold", 34),
    z("die Stadt beendet die Nutzung,", 150, 240, beim("fba", "Stadt"), size=34),
    z("notfalls Räumungsverfügung gegen die Familie", 150, 295, beim("fba", "notfalls"), size=34),
    zit("VG Köln, Beschl. v. 9.10.2020 – 22 L 1688/20, Rn. 16", 150, 345, beim("fba", "Räumungsverfügung")),
    z("umstritten, wenn die Familie vorher dort wohnte:", 110, 430, "streit", "Bold", 34),
    nein(150, 508, beim("streit", "verneint"), gr=18),
    z("OLG Köln: verneint", 195, 485, beim("streit", "verneint"), size=34),
    zit("OLG Köln, Urt. v. 16.9.1993 – 7 U 83/93, Rn. 43", 195, 535, beim("streit", "verneint")),
    zit("a. A. VG Köln, Beschl. v. 28.11.2022 – 22 L 1749/22, Rn. 41 f.", 195, 580, beim("streit", "verneint")),
    ficon("tabler", "hourglass", IX, IU, 130, "ende", fuell=GELB, bis="fba"),
    ficon("tabler", "door-exit", IX, IU, 130, "fba", fuell=WEISS),
    *fig("BA", FX, FB, FR, [("ende", "ruhig"), ("streit", "denkt")]),
    schild("Herr Bauer", FX, "ende", BA_F),
]))

# P Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Verfügungen trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne die Verfügungen:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("Herr Bauer greift die Beschlagnahme an;", 200, 265, "tipp1", size=34),
    z("die Einweisung betrifft nur Stadt und Familie", 200, 318, beim("tipp1", "Einweisung"), size=34),
    zit("VG Köln, Beschl. v. 28.5.2025 – 20 L 1292/25, Rn. 2", 200, 368, beim("tipp1", "Familie")),
    z("Ermächtigungsgrundlage umstritten:", 200, 440, "tipp2", "Bold", 34),
    z("Generalklausel oder Sicherstellung?", 200, 493, beim("tipp2", "Generalklausel"), size=34),
    zit("VG Köln, 20 L 1292/25, Rn. 7 f.: Sicherstellung (heute § 24w OBG NRW)", 200, 543, beim("tipp2", "Sicherstellung")),
    z("so oder so entscheidet § 19 OBG NRW", 200, 600, beim("tipp2", "Ausschlag"), size=34),
    z("Entschädigung: ordentliche Gerichte,", 200, 680, "tipp3", "Bold", 34),
    z("§ 43 Abs. 1 OBG NRW", 200, 733, beim("tipp3", "Paragraf"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# Q Klausurschema -----------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Inanspruchnahme des Nichtstörers"), 110, 90, "sch", 46),
    z("1. Ermächtigungsgrundlage: § 14 Abs. 1 OBG NRW (str.: Sicherstellung)", K1, 190, "q1", "Bold", 36, rechts=1820),
    z("2. formell: Zuständigkeit der örtlichen Ordnungsbehörde", K1, 260, "q2", "Bold", 36, rechts=1820),
    z("3. materiell: Gefahr durch unfreiwillige Obdachlosigkeit", K1, 330, "q3", "Bold", 36, rechts=1820),
    z("Adressat: Nichtstörer nur nach § 19 Abs. 1 Nr. 1–4 OBG NRW", K2, 400, "q4", size=SZ, rechts=1820),
    z("Nr. 1 gegenwärtige erhebliche Gefahr · Nr. 2 Verantwortliche erfolglos", K3, 455, beim("q4", "vier"), size=SZ, rechts=1820),
    z("Nr. 3 keine eigene Abwehr möglich · Nr. 4 keine eigene Gefährdung", K3, 510, beim("q4", "vier"), size=SZ, rechts=1820),
    z("4. Ermessen, Verhältnismäßigkeit, § 15 OBG NRW", K1, 590, "q5", "Bold", 36, rechts=1820),
    z("Befristung: nur vorübergehend, § 19 Abs. 2 OBG NRW", K2, 655, beim("q5", "Befristung"), size=SZ, rechts=1820),
    z("Danach: Entschädigung, § 39 Abs. 1 a oder b OBG NRW", K1, 740, "q6", "Bold", 36, rechts=1820),
    z("Folgenbeseitigung nach Fristablauf", K2, 805, beim("q6", "Folgenbeseitigung"), size=SZ, rechts=1820),
])

# R Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Vermieter ist das ", 0), ("letzte Mittel", "a"), (".", 0)]],
                750, 320, 46, "merke", {"a": beim("merke", "letzte")}),
    *markertext([[("Erst eigene Plätze, Hotels und Pensionen.", 0)]], 750, 480, 46, "m2", {}),
    *markertext([[("Dann nur vorübergehend seine Wohnung,", 0)]], 750, 540, 46, beim("m2", "Dann"), {}),
    *markertext([[("und nur gegen ", 0), ("Entschädigung", "c"), (".", 0)]], 750, 600, 46, beim("m2", "und", nr=2),
                {"c": beim("m2", "Entschädigung")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
