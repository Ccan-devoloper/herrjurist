"""Folge 069 · Anfechtungsklage Schema (§ 42 I VwGO): Zulässigkeit und Begründetheit – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Foodtruck im Gewerbegebiet, Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Gewerbegebiet (Herr Gerlach bringt den Bescheid), B Verwaltungsgericht (Klage, Frage), C Sachverhalt, D Aufbau,
E I. Rechtsweg, F II. statthafte Klageart (Wortlaut § 42 I), G III. Klagebefugnis (Wortlaut § 42 II), H IV. Vorverfahren,
I V. Klagefrist, J VI. Klagegegner, K VII./VIII. Beteiligte, Rechtsschutzbedürfnis, L B. Begründetheit (Wortlaut § 113 I 1),
M 1. Ermächtigungsgrundlage (Wortlaut § 35 I 1 GewO), N 2. formell, O 3. materiell: Tatbestand, P Rechtsfolge, Q II.
Rechtsverletzung, R Urteil (Richterin), S Klausurtipp (Lexi), T Klausurschema, U Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, wenn Herr Gerlach den Bescheid bringt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_069/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_069/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach der amtlichen Quelle, als Zitat mit Normangabe; feste Zeilen ergeben zusammen
    genau den Normtext. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    Wortgruppe (die Wortgruppe muss in einer Zeile stehen)."""
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


# --- Eigene Hilfsfunktion (wie Folge 064/061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
EB_F, GE_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
K1, K2 = 150, 210
ZU = "A. Zulässigkeit"
BG = "B. Begründetheit"


def foodtruck(cx, cue, anim="pop", breite=420, bis=None):
    """Der Foodtruck von Frau Ebeling: Tabler „truck“ (gelb), darüber eine dampfende Schale (Phosphor „bowl-steam“) und das
    Schild „Suppen“ – in jeder Szene gleich."""
    els = [ficon("tabler", "truck", cx, BODEN, breite, cue, fuell=GELB, anim=anim, bis=bis),
           ficon("ph", "bowl-steam", cx - 60, BODEN - 300, 110, cue, fuell=WEISS, anim=anim, bis=bis),
           pl("Suppen", cx - 70, BODEN - 235, cue, fill=WEISS, size=30, anker="m", anim=anim, bis=bis)]
    return els


# A Fall: Mittag im Gewerbegebiet, der Bescheid ----------------------------------------------------------------------------
TRX, EBX, GEX = 470, 960, 1620
EBb = ("EB_redet_r", EBX, BODEN, FH)
GEb = ("GE_redet", GEX, BODEN, FH)
KOMMT = beim("gerlach", "Herr")
BESCHEID = beim("gerlach", "Bescheid")
folie([(NULL, "Fall · Mittag im Gewerbegebiet"), ("gerlach", "Fall · Der Bescheid")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Mittags im Gewerbegebiet", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "building-factory-2", 1250, BODEN - 2, 260, NULL, fuell=BLAU, anim="cut"),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *foodtruck(TRX, NULL, anim="cut"),
    *fig("EB", EBX, BODEN, FH, [(NULL, "ruhig_r"), ("brief", "denkt_r"), (KOMMT, "ruhig_r"),
                               (beim("ge1", "dreißigtausend"), "sorge_r")], bis="eb1", erst="cut"),
    *redet("EB_redet_r", EBX, BODEN, FH, "eb1", "klage"),
    hart(schild("Frau Ebeling, Foodtruck", EBX, NULL, EB_F, unten=BODEN, d=0.0)),
    ficon(HC, "envelope", 1330, 360, 120, "brief", fuell=WEISS, bis="gerlach"),
    pl("Vor 2 Wochen: Brief der Stadt", 1330, 400, beim("brief", "Stadt"), fill=WEISS, size=30, anker="m", bis="gerlach"),
    pl("Äußerung zu den Steuerschulden", 1330, 470, beim("brief", "äußern"), fill=GELB, size=30, anker="m", bis="gerlach"),
    *fig("GE", GEX, BODEN, FH, [(KOMMT, "ruhig")], bis="ge1"),
    *redet("GE_redet", GEX, BODEN, FH, "ge1", "eb1"),
    peep_voll("GE_ruhig", GEX, BODEN, FH, "eb1", anim="cut"),
    schild("Herr Gerlach, Gewerbeamt", GEX, KOMMT, GE_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", GEX - 125, 700, 90, BESCHEID, fuell=WEISS), "069brief*", 0.8, -0.30),
    pl("30.000 € Steuerschulden", TRX - 30, 410, beim("ge1", "dreißigtausend"), fill=ROT, size=30, anker="m"),
    nein(TRX - 70, BODEN - 125, beim("ge1", "untersagen"), gr=40),
    blase("sprech", 760, 230, "ge1", 1180, 215, inhalt=["Frau Ebeling, Sie schulden dem", "Finanzamt seit 3 Jahren 30.000 €.",
                                                      "Wir untersagen Ihnen das Gewerbe."], textsize=30, figur=GEb, bis="eb1"),
    blase("sprech", 680, 200, "eb1", 760, 215, inhalt=["Ich zahle doch, sobald der", "Sommer gut läuft! Dagegen klage ich."],
          textsize=29, figur=EBb, bis="klage"),
])

# B Die Klage und die Frage --------------------------------------------------------------------------------------------------
GERICHT = beim("klage", "Verwaltungsgericht")
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Hat die Klage Erfolg?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("3 Wochen später", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 560, BODEN - 2, 420, "klage", fuell=WEISS),
    pl("Verwaltungsgericht", 560, 330, GERICHT, fill=WEISS, size=34, anker="m"),
    ficon("tabler", "file-text", 1000, 640, 100, beim("klage", "Klage"), fuell=WEISS),
    pl("Klage", 1000, 660, beim("klage", "Klage"), fill=GRUEN, size=30, anker="m"),
    *fig("EB", 1180, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Frau Ebeling", 1180, "klage", EB_F, unten=BODEN),
    pl("Hat die Klage Erfolg?", 1250, 150, "frage", fill=PINK, size=44, anker="m"),
    pl("Das Schema, Beispiel: Nordrhein-Westfalen", 1250, 250, beim("frage2", "Schema"), fill=WEISS, size=32, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Ebeling verkauft mittags Suppen aus ihrem Foodtruck im Gewerbegebiet einer Stadt in Nordrhein-Westfalen. "
    "Sie schuldet dem Finanzamt seit 3 Jahren 30.000 € Steuern; einen Plan zur Tilgung hat sie nicht. Die Stadt gibt ihr "
    "Gelegenheit, sich zu äußern. Dann übergibt Herr Gerlach vom Gewerbeamt den schriftlichen, begründeten Bescheid mit "
    "richtiger Rechtsbehelfsbelehrung: Die Stadt untersagt ihr das Gewerbe. Frau Ebeling will zahlen, sobald der Sommer "
    "gut läuft. 3 Wochen später erhebt sie Klage beim Verwaltungsgericht.",
], "Hat die Klage Erfolg?")

# D Aufbau --------------------------------------------------------------------------------------------------------------------
folie([("aufbau", "Aufbau · Anfechtungsklage, § 42 I Alt. 1 VwGO")], rechts_frei([
    *tafel("aufbau", "Die Anfechtungsklage: zwei Schritte"),
    blk(110, 220, 1040, 110, BLAU, beim("aufbau2", "Zulässigkeit"), [("A. Zulässigkeit", "ExtraBold", 44, INK)]),
    blk(110, 380, 1040, 110, GRUEN, beim("aufbau2", "Begründetheit"), [("B. Begründetheit", "ExtraBold", 44, INK)]),
    ficon(HC, "classical-building", IX, IU, 150, "aufbau", fuell=WEISS),
    *fig("EB", FX, FB, FR, [("aufbau", "denkt")]),
    schild("Frau Ebeling", FX, "aufbau", EB_F),
]))

# E I. Verwaltungsrechtsweg -----------------------------------------------------------------------------------------------------
folie([("rweg", f"{ZU} › I. Verwaltungsrechtsweg, § 40 I 1 VwGO")], rechts_frei([
    *tafel("rweg", "I. Verwaltungsrechtsweg, § 40 I 1 VwGO", size=44),
    z("öffentlich-rechtliche Streitigkeit", 110, 190, beim("rweg", "öffentlich-rechtliche"), "Bold", 36),
    z("nichtverfassungsrechtlicher Art", 110, 245, beim("rweg", "nichtverfassungsrechtlicher"), "Bold", 36),
    z("Gewerbe untersagen darf nur eine Behörde,", 195, 340, beim("rweg2", "Gewerbe"), size=34),
    z("keine Privatperson: öffentliches Recht", 195, 392, beim("rweg2", "keine"), size=34),
    ok(150, 415, beim("rweg2", "öffentliches"), gr=20),
    zit("vgl. BVerwG, Beschl. v. 6.7.2022 – 3 B 40.21, Rn. 10", 195, 447, beim("rweg2", "Recht")),
    ok(150, 533, beim("rweg3", "Verfassungsorgane"), gr=20),
    z("keine Verfassungsorgane im Streit", 195, 510, beim("rweg3", "Verfassungsorgane"), size=34),
    zit("vgl. BVerwG, 3 B 40.21, Rn. 12", 195, 562, beim("rweg3", "streiten")),
    ok(150, 643, beim("rweg3", "abdrängende"), gr=20),
    z("keine abdrängende Sonderzuweisung", 195, 620, beim("rweg3", "abdrängende"), size=34),
    ficon(HC, "classical-building", IX, IU, 150, "rweg", fuell=WEISS),
    *fig("GE", FX, FB, FR, [("rweg", "ruhig"), ("rweg3", "denkt")]),
    schild("Herr Gerlach, Gewerbeamt", FX, "rweg", GE_F),
]))

# F II. Statthafte Klageart, Wortlaut § 42 I --------------------------------------------------------------------------------------
W42 = "„Durch Klage kann die Aufhebung eines Verwaltungsakts (Anfechtungsklage) … begehrt werden.“"
Z42 = ["„Durch Klage kann die Aufhebung eines Verwaltungsakts", "(Anfechtungsklage) … begehrt werden.“"]
w42, w42_y = wortlaut(80, 175, 1100, W42, "§ 42 Abs. 1 Alt. 1 VwGO (Auszug)", "wl42", size=36, zeilen=Z42,
                      marken=[("Aufhebung eines Verwaltungsakts", beim("wl42", "Aufhebung")),
                              ("(Anfechtungsklage)", beim("wl42", "Anfechtungsklage"))])
folie([("wl42", f"{ZU} › II. Statthafte Klageart, § 42 I Alt. 1 VwGO")], rechts_frei([
    titel(glyphen("II. Statthafte Klageart"), 110, 75, "wl42", 46),
    *w42,
    z("Untersagung: verbindliche Regelung eines Einzelfalls", 110, w42_y + 35, beim("va", "regelt"), size=34),
    z("mit Wirkung nach außen", 150, w42_y + 88, beim("va", "außen"), size=34),
    z("= Verwaltungsakt, § 35 Satz 1 VwVfG", 150, w42_y + 141, beim("va", "Verwaltungsakt"), "Bold", 34),
    blk(110, w42_y + 215, 1040, 80, GRUEN, beim("va2", "Anfechtungsklage"),
        [("will ihn loswerden: Anfechtungsklage", "ExtraBold", 36, INK)]),
    pl("Mehr dazu: Videos Verwaltungsakt und Klagearten", 110, w42_y + 330, beim("va3", "Videos"), fill=WEISS, size=28),
    ficon("tabler", "file-text", IX, IU, 120, "wl42", fuell=WEISS),
    pl("Untersagung", IX, 180, beim("va", "Untersagung"), fill=WEISS, size=28, anker="m"),
    *fig("EB", FX, FB, FR, [("wl42", "ruhig"), ("va2", "aerger")]),
    schild("Frau Ebeling", FX, "wl42", EB_F),
]))

# G III. Klagebefugnis, Wortlaut § 42 II -----------------------------------------------------------------------------------------
W422 = ("„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage nur zulässig, wenn der Kläger geltend macht, durch den "
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen Rechten verletzt zu sein.“")
Z422 = ["„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage",
        "nur zulässig, wenn der Kläger geltend macht, durch den",
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung",
        "in seinen Rechten verletzt zu sein.“"]
w422, w422_y = wortlaut(80, 160, 1100, W422, "§ 42 Abs. 2 VwGO", "wl422", size=34, zeilen=Z422,
                        marken=[("geltend macht", beim("wl422", "geltend")),
                                ("in seinen Rechten verletzt", beim("wl422", "verletzt"))])
folie([("wl422", f"{ZU} › III. Klagebefugnis, § 42 II VwGO")], rechts_frei([
    titel(glyphen("III. Klagebefugnis"), 110, 70, "wl422", 46),
    *w422,
    z("Verletzung muss möglich sein", 110, w422_y + 30, beim("mt", "möglich"), "Bold", 34),
    z("ausgeschlossen nur, wenn Rechte offensichtlich und", 150, w422_y + 83, beim("mt", "Ausgeschlossen"), size=32),
    z("eindeutig nach keiner Betrachtungsweise bestehen", 150, w422_y + 130, beim("mt", "eindeutig"), size=32),
    zit("BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9", 150, w422_y + 178, beim("mt", "können")),
    z("Adressatin eines belastenden Bescheids:", 110, w422_y + 235, beim("adr", "Adressatin"), "Bold", 34),
    z("allgemeine Handlungsfreiheit, Art. 2 Abs. 1 GG", 150, w422_y + 288, beim("adr", "allgemeinen"), size=32),
    blk(110, w422_y + 345, 700, 70, GRUEN, "adr2", [("Adressatentheorie", "ExtraBold", 34, INK)]),
    zit("BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 150, w422_y + 428, beim("adr2", "Adressatentheorie")),
    ficon("tabler", "file-text", IX, IU, 120, "wl422", fuell=WEISS),
    pl("an Frau Ebeling", IX, 180, beim("adr", "Adressatin"), fill=WEISS, size=28, anker="m"),
    *fig("EB", FX, FB, FR, [("wl422", "denkt"), ("adr", "ruhig")]),
    schild("Frau Ebeling", FX, "wl422", EB_F),
]))

# H IV. Vorverfahren -----------------------------------------------------------------------------------------------------------
NRW = beim("nrw", "entfällt")
folie([("vv", f"{ZU} › IV. Vorverfahren, §§ 68 ff. VwGO"), ("nrw", f"{ZU} › IV. Vorverfahren › NRW: § 110 JustG NRW")],
      rechts_frei([
    *tafel("vv", "IV. Vorverfahren, §§ 68 ff. VwGO", size=44),
    z("vor der Klage: Widerspruch", 110, 190, beim("vv", "Widerspruch"), "Bold", 36),
    zit("§ 68 Abs. 1 Satz 1 VwGO", 150, 245, beim("vv", "Widerspruch")),
    z("außer ein Gesetz bestimmt etwas anderes", 110, 300, beim("vv", "Gesetz"), size=34),
    zit("§ 68 Abs. 1 Satz 2 VwGO", 150, 352, beim("vv", "bestimmt")),
    blk(110, 420, 1040, 80, GELB, NRW, [("NRW: entfällt in der Regel", "ExtraBold", 36, INK)]),
    zit("§ 110 Abs. 1 Satz 1 JustG NRW", 150, 512, beim("nrw", "Paragraf")),
    z("ausdrücklich auch bei der Gewerbeordnung", 110, 570, beim("nrw", "ausdrücklich"), "Bold", 34),
    zit("§ 110 Abs. 3 Satz 2 Nr. 4 JustG NRW", 150, 622, beim("nrw", "Gewerbeordnung")),
    pl("In deinem Land kann das anders sein.", 110, 700, "land", fill=PINK, size=32),
    ficon(HC, "envelope", IX, IU, 140, "vv", fuell=WEISS),
    pl("Widerspruch", IX, 190, beim("vv", "Widerspruch"), fill=WEISS, size=28, anker="m"),
    nein(IX + 90, IU - 60, NRW, gr=34),
    *fig("EB", FX, FB, FR, [("vv", "ruhig"), ("land", "denkt")]),
    schild("Frau Ebeling", FX, "vv", EB_F),
]))

# I V. Klagefrist -------------------------------------------------------------------------------------------------------------
folie([("frist", f"{ZU} › V. Klagefrist, § 74 I VwGO")], rechts_frei([
    *tafel("frist", "V. Klagefrist, § 74 I VwGO"),
    z("ohne Vorverfahren: 1 Monat ab Bekanntgabe", 110, 190, beim("frist", "Monat"), "Bold", 36),
    zit("§ 74 Abs. 1 Satz 2 VwGO", 150, 245, beim("frist", "Bekanntgabe")),
    z("Rechtsbehelfsbelehrung fehlt oder ist falsch:", 110, 320, beim("rbb", "Fehlt"), size=34),
    z("Jahresfrist, § 58 Abs. 2 VwGO", 150, 373, beim("rbb", "Jahresfrist"), "Bold", 34),
    z("Frau Ebeling klagt nach 3 Wochen", 110, 470, beim("frist2", "Frau"), size=34),
    blk(110, 540, 600, 76, GRUEN, beim("frist2", "rechtzeitig"), [("rechtzeitig", "ExtraBold", 36, INK)]),
    ok(760, 578, beim("frist2", "rechtzeitig"), gr=26),
    ficon("tabler", "calendar", IX, IU, 140, "frist", fuell=WEISS),
    pl("1 Monat", IX, 180, beim("frist", "Monat"), fill=GELB, size=30, anker="m", bis="frist2"),
    pl("3 Wochen", IX, 180, "frist2", fill=GRUEN, size=30, anker="m"),
    *fig("EB", FX, FB, FR, [("frist", "ruhig")]),
    schild("Frau Ebeling", FX, "frist", EB_F),
]))

# J VI. Klagegegner -------------------------------------------------------------------------------------------------------------
folie([("kg", f"{ZU} › VI. Klagegegner, § 78 I Nr. 1 VwGO")], rechts_frei([
    *tafel("kg", "VI. Klagegegner, § 78 I Nr. 1 VwGO", size=44),
    z("die Körperschaft, deren Behörde den Bescheid", 110, 190, beim("kg", "Körperschaft"), "Bold", 34),
    z("erlassen hat", 110, 243, beim("kg", "erlassen"), "Bold", 34),
    blk(110, 310, 1040, 76, BLAU, beim("kg", "Rechtsträgerprinzip"), [("Rechtsträgerprinzip", "ExtraBold", 36, INK)]),
    ok(150, 448, beim("kg2", "Stadt"), gr=20),
    z("Klage gegen die Stadt", 195, 425, beim("kg2", "Stadt"), "Bold", 34),
    nein(150, 503, beim("kg2", "Gewerbeamt"), gr=18),
    z("nicht gegen das Gewerbeamt", 195, 480, beim("kg2", "Gewerbeamt"), size=34),
    z("Nr. 2: die Behörde selbst, wenn das Landesrecht", 110, 575, beim("kg3", "Nummer"), size=34),
    z("es bestimmt", 110, 628, beim("kg3", "Landesrecht"), size=34),
    z("Nordrhein-Westfalen: nicht genutzt", 110, 700, beim("kg3", "Nordrhein-Westfalen"), "Bold", 34),
    ficon("tabler", "building", IX, IU, 140, "kg", fuell=WEISS),
    pl("Stadt", IX, 190, beim("kg2", "Stadt"), fill=GRUEN, size=30, anker="m"),
    *fig("GE", FX, FB, FR, [("kg", "ruhig"), ("kg3", "denkt")]),
    schild("Herr Gerlach, Gewerbeamt", FX, "kg", GE_F),
]))

# K VII. Beteiligten- und Prozessfähigkeit, VIII. Rechtsschutzbedürfnis -------------------------------------------------------------
folie([("bet", f"{ZU} › VII. Beteiligten- und Prozessfähigkeit"), ("rsb", f"{ZU} › VIII. Rechtsschutzbedürfnis")], rechts_frei([
    *tafel("bet", "VII. Beteiligten- und Prozessfähigkeit", size=44),
    zit("§§ 61, 62 VwGO", 110, 165, beim("bet", "Paragrafen")),
    z("Frau Ebeling: natürliche Person", 110, 215, beim("bet", "natürliche"), size=34),
    z("die Stadt: juristische Person", 110, 268, beim("bet", "juristische"), size=34),
    z("VIII. Rechtsschutzbedürfnis", 110, 370, "rsb", "Bold", 40),
    z("ohne Klage würde der Bescheid bestandskräftig", 110, 435, beim("rsb", "Ohne"), size=34),
    blk(110, 540, 1040, 90, GRUEN, beim("zul", "zulässig"), [("Die Klage ist zulässig.", "ExtraBold", 40, INK)]),
    ok(1100, 585, beim("zul", "zulässig"), gr=28),
    *fig("EB", FX, FB, FR, [("bet", "ruhig"), ("zul", "denkt")]),
    schild("Frau Ebeling", FX, "bet", EB_F),
]))

# L B. Begründetheit, Wortlaut § 113 I 1 ------------------------------------------------------------------------------------------
W113 = ("„Soweit der Verwaltungsakt rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht den "
        "Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“")
Z113 = ["„Soweit der Verwaltungsakt rechtswidrig und der Kläger",
        "dadurch in seinen Rechten verletzt ist, hebt das Gericht",
        "den Verwaltungsakt und den etwaigen Widerspruchsbescheid auf.“"]
w113, w113_y = wortlaut(80, 175, 1100, W113, "§ 113 Abs. 1 Satz 1 VwGO", "wl113", size=32, zeilen=Z113,
                        marken=[("rechtswidrig", beim("wl113", "rechtswidrig")),
                                ("in seinen Rechten verletzt", beim("wl113", "verletzt")),
                                ("hebt das Gericht", beim("wl113", "hebt"))])
folie([("wl113", f"{BG}, § 113 I 1 VwGO")], rechts_frei([
    titel(glyphen("B. Begründetheit"), 110, 75, "wl113", 50),
    *w113,
    blk(110, w113_y + 45, 1040, 80, BLAU, beim("zwei", "rechtswidrig"), [("I. Ist der Bescheid rechtswidrig?", "ExtraBold", 36, INK)]),
    blk(110, w113_y + 150, 1040, 80, GRUEN, beim("zwei", "Rechten"), [("II. Ist sie dadurch in ihren Rechten verletzt?", "ExtraBold", 34, INK)]),
    ficon(HC, "classical-building", IX, IU, 150, "wl113", fuell=WEISS),
    *fig("EB", FX, FB, FR, [("wl113", "denkt")]),
    schild("Frau Ebeling", FX, "wl113", EB_F),
]))

# M 1. Ermächtigungsgrundlage, Wortlaut § 35 I 1 GewO ------------------------------------------------------------------------------
W35 = ("„Die Ausübung eines Gewerbes ist von der zuständigen Behörde ganz oder teilweise zu untersagen, wenn Tatsachen vorliegen, "
       "welche die Unzuverlässigkeit des Gewerbetreibenden … in bezug auf dieses Gewerbe dartun, sofern die Untersagung zum "
       "Schutze der Allgemeinheit … erforderlich ist.“")
Z35 = ["„Die Ausübung eines Gewerbes ist von der zuständigen Behörde",
       "ganz oder teilweise zu untersagen, wenn Tatsachen vorliegen,",
       "welche die Unzuverlässigkeit des Gewerbetreibenden … in bezug",
       "auf dieses Gewerbe dartun, sofern die Untersagung zum Schutze",
       "der Allgemeinheit … erforderlich ist.“"]
w35, w35_y = wortlaut(80, 330, 1100, W35, "§ 35 Abs. 1 Satz 1 GewO (Auszug)", "egl", size=32, zeilen=Z35,
                      marken=[("zu untersagen,", beim("egl", "Gewerbeuntersagung"))])
folie([("egl", f"{BG} › I. 1. Ermächtigungsgrundlage")], rechts_frei([
    titel(glyphen("I. Rechtswidrigkeit: 1. Ermächtigungsgrundlage"), 110, 75, "egl", 40),
    z("belastender Bescheid: braucht ein Gesetz", 110, 160, beim("egl", "Gesetz"), "Bold", 34),
    z("hier: § 35 Abs. 1 Satz 1 GewO, Gewerbeuntersagung", 110, 225, beim("egl", "Paragraf"), size=34),
    *w35,
    ficon("tabler", "file-text", IX, IU, 120, "egl", fuell=WEISS),
    pl("§ 35 GewO", IX, 180, beim("egl", "Paragraf"), fill=GELB, size=30, anker="m"),
    *fig("GE", FX, FB, FR, [("egl", "ruhig")]),
    schild("Herr Gerlach, Gewerbeamt", FX, "egl", GE_F),
]))

# N 2. formelle Rechtmäßigkeit ------------------------------------------------------------------------------------------------------
folie([("formell", f"{BG} › I. 2. formelle Rechtmäßigkeit")], rechts_frei([
    *tafel("formell", "2. formelle Rechtmäßigkeit"),
    z("Zuständigkeit: die Stadt, nach Landesrecht", 110, 185, beim("formell", "Zuständig"), "Bold", 34),
    zit("§ 155 Abs. 2 GewO", 150, 238, beim("formell", "Landesrecht")),
    z("Verfahren: Anhörung, § 28 Abs. 1 VwVfG", 110, 300, beim("anh", "anzuhören"), "Bold", 34),
    zit("für die Stadt: § 28 Abs. 1 VwVfG NRW, wortgleich", 150, 353, beim("anh", "Paragraf")),
    ok(150, 428, beim("anh", "äußern"), gr=20),
    z("Frau Ebeling durfte sich äußern", 195, 405, beim("anh", "äußern"), size=34),
    z("fehlt sie: nachholbar bis zum Abschluss der", 110, 490, beim("heil", "Fehlt"), size=34),
    z("letzten Tatsacheninstanz", 150, 543, beim("heil", "Tatsacheninstanz"), size=34),
    zit("§ 45 Abs. 1 Nr. 3, Abs. 2 VwVfG", 150, 596, beim("heil", "Paragraf")),
    ok(150, 678, beim("form", "schriftlich"), gr=20),
    z("Form: schriftlich und begründet, § 39 Abs. 1 VwVfG", 195, 655, beim("form", "schriftlich"), "Bold", 34),
    ficon("tabler", "building", IX, IU, 140, "formell", fuell=WEISS, bis="anh"),
    pl("Stadt", IX, 190, beim("formell", "Stadt"), fill=GRUEN, size=30, anker="m", bis="anh"),
    ficon(HC, "envelope", IX, IU, 140, "anh", fuell=WEISS, bis="form"),
    pl("Anhörung", IX, 190, beim("anh", "anzuhören"), fill=WEISS, size=28, anker="m", bis="form"),
    ficon("tabler", "file-text", IX, IU, 120, "form", fuell=WEISS),
    *fig("GE", FX, FB, FR, [("formell", "ruhig"), ("heil", "denkt"), ("form", "ruhig")]),
    schild("Herr Gerlach, Gewerbeamt", FX, "formell", GE_F),
]))

# O 3. materielle Rechtmäßigkeit: Tatbestand ----------------------------------------------------------------------------------------
folie([("tb", f"{BG} › I. 3. materielle Rechtmäßigkeit › Tatbestand")], rechts_frei([
    *tafel("tb", "3. materielle Rechtmäßigkeit"),
    z("Tatbestand: Tatsachen belegen die Unzuverlässigkeit", 110, 180, beim("tb", "Tatbestand"), "Bold", 34),
    z("unzuverlässig: nach dem Gesamteindruck keine Gewähr", 110, 255, beim("unz", "Gesamteindruck"), size=32),
    z("für einen künftig ordnungsgemäßen Betrieb", 150, 302, beim("unz", "künftig"), size=32),
    zit("BVerwG, Urt. v. 15.4.2015 – 8 C 6.14, Rn. 14", 150, 350, beim("unz", "betreiben")),
    z("Anhaltspunkt: erhebliche Steuerrückstände", 110, 410, beim("steuer", "Steuerrückstände"), "Bold", 34),
    z("außer: zahlungswillig und sinnvolles,", 150, 463, beim("steuer", "zahlungswillig"), size=32),
    z("erfolgversprechendes Sanierungskonzept", 150, 510, beim("steuer", "Sanierungskonzept"), size=32),
    nein(150, 593, beim("steuer2", "Sommer"), gr=18),
    z("Frau Ebeling: nur Hoffnung auf den Sommer", 195, 570, beim("steuer2", "hofft"), size=34),
    blk(110, 640, 1040, 76, GRUEN, beim("steuer2", "unzuverlässig"), [("unzuverlässig", "ExtraBold", 36, INK)]),
    ok(150, 790, beim("steuer2", "Schutz"), gr=20),
    z("Untersagung zum Schutz der Allgemeinheit erforderlich", 195, 767, beim("steuer2", "Schutz"), size=30),
    ficon("tabler", "receipt-tax", IX, IU, 130, "tb", fuell=WEISS),
    pl("Steuerrückstände: 30.000 €", IX, 190, beim("steuer", "Steuerrückstände"), fill=ROT, size=28, anker="m"),
    *fig("EB", FX, FB, FR, [("tb", "sorge"), ("steuer2", "muede")]),
    schild("Frau Ebeling", FX, "tb", EB_F),
]))

# P Rechtsfolge --------------------------------------------------------------------------------------------------------------------
folie([("rf", f"{BG} › I. 3. materielle Rechtmäßigkeit › Rechtsfolge")], rechts_frei([
    *tafel("rf", "Rechtsfolge"),
    z("§ 35 Abs. 1 Satz 1 GewO: „ist … zu untersagen“", 110, 190, beim("rf", "untersagen"), "Bold", 36),
    blk(110, 270, 1040, 80, GELB, beim("rf", "Ermessen"), [("gebunden: kein Ermessen", "ExtraBold", 38, INK)]),
    z("bei Ermessen der Behörde:", 110, 410, beim("erm", "Ermessen"), "Bold", 34),
    zit("§ 114 Satz 1 VwGO", 150, 463, beim("erm", "Paragraf")),
    z("Gericht prüft nur Ermessensfehler", 150, 510, beim("erm", "Ermessensfehler"), "Bold", 34),
    ficon(HC, "balance-scale", IX, IU, 150, "rf", fuell=WEISS),
    *fig("GE", FX, FB, FR, [("rf", "ruhig")]),
    schild("Herr Gerlach, Gewerbeamt", FX, "rf", GE_F),
]))

# Q II. Rechtsverletzung ----------------------------------------------------------------------------------------------------------
folie([("rv", f"{BG} › II. Rechtsverletzung")], rechts_frei([
    *tafel("rv", "II. Rechtsverletzung"),
    blk(110, 190, 1040, 80, GRUEN, beim("rv", "rechtmäßig"), [("I. Der Bescheid ist rechtmäßig.", "ExtraBold", 38, INK)]),
    z("wäre er rechtswidrig: Adressatin regelmäßig", 110, 330, beim("rv2", "Wäre"), size=34),
    z("in ihren Rechten verletzt", 150, 383, beim("rv2", "Rechten"), size=34),
    zit("BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 150, 436, beim("rv2", "verletzt")),
    ficon("tabler", "file-text", IX, IU, 120, "rv", fuell=WEISS),
    *fig("EB", FX, FB, FR, [("rv", "muede")]),
    schild("Frau Ebeling", FX, "rv", EB_F),
]))

# R Das Urteil ---------------------------------------------------------------------------------------------------------------------
RIX, EBX2 = 1320, 620
RIb = ("RI_redet", RIX, BODEN, FH)
folie([("urteil", "Ergebnis · Das Urteil")], [
    linienzug([(60, BODEN), (1860, BODEN)], "urteil", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "urteil", fill=GELB, size=40),
    ficon(HC, "balance-scale", 960, 700, 150, "urteil", fuell=WEISS),
    *fig("EB", EBX2, BODEN, FH, [("urteil", "denkt_r"), (beim("ri1", "abgewiesen"), "muede_r")]),
    schild("Frau Ebeling", EBX2, "urteil", EB_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [(beim("urteil", "Verwaltungsgericht"), "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "tipp"),
    schild("die Richterin", RIX, beim("urteil", "Verwaltungsgericht"), RI_F, unten=BODEN, d=0.0),
    blase("sprech", 700, 200, "ri1", 1240, 200, inhalt=["Die Klage ist zulässig, aber", "unbegründet. Sie wird abgewiesen."],
          textsize=30, figur=RIb),
    pl("zulässig, aber unbegründet", 960, 740, beim("ri1", "unbegründet"), fill=ROT, size=30, anker="m"),
])

# S Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Schwerpunkte setzen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Reihenfolge einhalten,", 200, 200, beim("tipp", "Reihenfolge"), "Bold", 36),
    z("aber nicht zu jedem Punkt einen Absatz", 200, 255, beim("tipp", "Absatz"), "Bold", 36),
    z("Unproblematisches in einem Satz feststellen,", 200, 350, beim("tipp1", "unproblematisch"), size=34),
    z("etwa das Rechtsschutzbedürfnis", 200, 405, beim("tipp1", "Rechtsschutzbedürfnis"), size=34),
    z("Zeit für die echten Probleme:", 200, 500, beim("tipp2", "Zeit"), size=34),
    z("hier die Unzuverlässigkeit", 200, 555, beim("tipp2", "Unzuverlässigkeit"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# T Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ, LH = 32, 62
LX0, RX0 = 110, 1010
links = [("s1", "I. Verwaltungsrechtsweg, § 40 I 1"), ("s2", "II. statthafte Klageart, § 42 I Alt. 1"),
         ("s3", "III. Klagebefugnis, § 42 II"), ("s4", "IV. Vorverfahren, §§ 68 ff. (Landesrecht)"),
         ("s5", "V. Klagefrist, § 74 I"), ("s6", "VI. Klagegegner, § 78 I"),
         ("s7", "VII. Beteiligten-, Prozessfähigkeit, §§ 61, 62"), ("s8", "VIII. Rechtsschutzbedürfnis")]
rechts_ = [("s9", "I. Rechtswidrigkeit:", "Bold"), ("s9", "1. Ermächtigungsgrundlage", "Regular"),
           ("s10", "2. formelle Rechtmäßigkeit", "Regular"), ("s11", "3. materielle Rechtmäßigkeit", "Regular"),
           ("s12", "II. Verletzung in eigenen Rechten", "Bold")]
els_t = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: Anfechtungsklage"), 110, 85, "sch", 46),
         z("A. Zulässigkeit", LX0, 190, "sa", "ExtraBold", 38, rechts=980),
         z("B. Begründetheit, § 113 I 1", RX0, 190, "sb", "ExtraBold", 38, rechts=1820)]
for i, (c, t) in enumerate(links):
    els_t.append(z(t, LX0 + 30, 260 + i * LH, c, size=SZ, rechts=980))
for i, (c, t, s) in enumerate(rechts_):
    els_t.append(z(t, RX0 + (30 if s == "Bold" else 70), 260 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · Anfechtungsklage")], els_t)

# U Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Anfechtungsklage ist ", 0), ("begründet,", "a")]], 750, 320, 46, "merke",
                {"a": beim("merke", "begründet")}),
    *markertext([[("soweit der Verwaltungsakt ", 0), ("rechtswidrig", "b"), (" ist", 0)]], 750, 385, 46,
                beim("merke", "soweit"), {"b": beim("merke", "rechtswidrig")}),
    *markertext([[("und den Kläger in seinen ", 0), ("Rechten verletzt.", "c")]], 750, 450, 46,
                beim("merke", "und"), {"c": beim("merke", "Rechten")}),
    *markertext([[("Unproblematisches kurz,", 0)]], 750, 600, 46, "m2", {}),
    *markertext([[("Probleme ", 0), ("gründlich.", "d")]], 750, 665, 46, beim("m2", "Probleme"),
                {"d": beim("m2", "gründlich")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
