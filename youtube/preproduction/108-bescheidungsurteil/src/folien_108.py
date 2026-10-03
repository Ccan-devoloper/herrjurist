"""Folge 108 · Bescheidungsurteil oder Verpflichtungsurteil? Spruchreife erklärt – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Gasthaus am Marktplatz, acht Tische, Ablehnung aus Konkurrenzschutz, Beispielland Brandenburg), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Marktplatz (Antrag, Ablehnung, Widerspruch), B Verwaltungsgericht (Feststellung, Frage),
C Sachverhalt, D Spruchreife kurz (§ 18 II 3 BbgStrG), E Antrag (Wortlaut § 88 VwGO, Minus), F Tenor (Wortlaut § 113 V VwGO),
G Tenor bei Spruchreife (Behördenprinzip § 8 II BbgVwGG), H Bescheidungsurteil, I Kosten (Wortlaut § 155 I 1 VwGO), J Klausurtipp
mit Kostenvergleich (Lexi), K Vorläufige Vollstreckbarkeit, L vollständiger Tenor, M Schema, N Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als Frau Seeger den Bescheid bringt). Hilfsfunktionen wie 102."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_108/"
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


def zz(kopf, rest, x, y, c_kopf, c_rest, stil="Bold", size=34, rest_stil=None, **k):
    """Zeile in zwei Teilen: Gliederungspunkt zur Marke, Inhalt erst zum gesprochenen Wort (nie vor dem Wort)."""
    a = z(kopf, x, y, c_kopf, stil, size, **k)
    dx = F(stil, size).getlength(kopf + " ")
    return [a, z(rest, x + dx, y, c_rest, rest_stil or stil, size, **k)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_108/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 074/069): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
HA_F, SE_F, RI_F = GRUEN, LILA, BLAU        # Farben der Namensschilder
TN = "Tenor"


def tenorbox(x, y, w, h, cue, bis=None):
    """Kasten für den Urteilstenor (hellgelb, schmale Kontur) mit kleinem Etikett „Tenor“."""
    return [bis_(karte(x, y, w, h, cue, fill=HELL, rund=16, schatten=6, rand=4), bis),
            pl("Tenor", x + 20, y - 48, cue, fill=GELB, size=26, bis=bis)]


def reihe(teile, x, y, gap=18):
    """Pillen nebeneinander (Breite aus dem Sprite): teile = [(text, cue, fill)]."""
    els = []
    for text, cue, fill in teile:
        e = pl(text, x, y, cue, fill=fill, size=30)
        els.append(e)
        x = e.x + e.sprite.width + gap
    assert x - gap <= 1170, "Pillenreihe zu breit"
    return els



# A Fall: Gasthaus am Marktplatz, Antrag, Ablehnung, Widerspruch ---------------------------------------------------------------
GHX, HAX, SEX = 230, 1130, 1660
HAb = ("HA_redet_r", HAX, BODEN, FH)
SEb = ("SE_redet", SEX, BODEN, FH)
KOMMT = beim("seeger", "Frau")
TISCHE = [(450, BODEN - 2), (560, BODEN - 2), (670, BODEN - 2)]
folie([(NULL, "Fall · Die Terrasse am Marktplatz"), ("wsp", "Fall · Ablehnung und Widerspruch")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Gasthaus am Marktplatz, Brandenburg", 70, 40, NULL, fill=GELB, size=40)),
    ficon("ph", "storefront", GHX, BODEN - 2, 300, NULL, fuell=GELB, anim="cut"),
    ficon("tabler", "fountain", 900, BODEN - 2, 150, NULL, fuell=BLAU, anim="cut"),
    *fig("HA", HAX, BODEN, FH, [(NULL, "ruhig_r"), ("antrag", "hofft_r"), (KOMMT, "ruhig_r"),
                               (beim("se1", "Konkurrenz"), "sorge_r"), ("wsp", "aerger_r")], bis="ha1", erst="cut"),
    *redet("HA_redet_r", HAX, BODEN, FH, "ha1", "klage"),
    hart(schild("Herr Haberland, Wirt", HAX, NULL, HA_F, unten=BODEN, d=0.0)),
    ficon("tabler", "file-text", 560, 560, 90, beim("antrag", "Sondernutzungserlaubnis"), fuell=WEISS),
    pl("Antrag: Sondernutzungserlaubnis", 560, 600, beim("antrag", "Sondernutzungserlaubnis"), fill=WEISS, size=28, anker="m"),
    *[ficon("ph", "table", x, y, 95, beim("antrag", "acht"), fuell=WEISS) for x, y in TISCHE],
    pl("8 Tische, Mai bis September", 560, 665, beim("antrag", "Mai"), fill=GELB, size=28, anker="m"),
    *fig("SE", SEX, BODEN, FH, [(KOMMT, "ruhig")], bis="se1"),
    *redet("SE_redet", SEX, BODEN, FH, "se1", "wsp"),
    *fig("SE", SEX, BODEN, FH, [("wsp", "denkt")], erst="cut"),
    schild("Frau Seeger, Stadt", SEX, KOMMT, SE_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", SEX - 260, 700, 90, beim("seeger", "Antwort"), fuell=WEISS), "108brief*", 0.8, -0.42),
    pl("Bescheid", SEX - 260, 745, beim("seeger", "Antwort"), fill=WEISS, size=26, anker="m"),
    nein(560, 760, beim("se1", "Abgelehnt"), gr=40),
    pl("Widerspruch: zurückgewiesen", 800, 400, "wsp", fill=ROT, size=26, anker="m"),
    blase("sprech", 980, 240, "se1", 1260, 230, inhalt=["Am Markt gibt es schon 2 Terrassen.",
                                                       "Wir schützen die anderen Wirte vor Konkurrenz.",
                                                       "Abgelehnt."], textsize=30, figur=SEb, bis="wsp"),
    blase("sprech", 760, 210, "ha1", 800, 240, inhalt=["Dann klage ich.", "Die Stadt muss mir die Erlaubnis erteilen!"],
          textsize=30, figur=HAb, bis="klage"),
])

# B Gericht: Feststellung und Frage -------------------------------------------------------------------------------------------
HAX2, RIX = 1190, 1670
RIb = ("RI_redet", RIX, BODEN, FH)
folie([("klage", "Fall · Die Verpflichtungsklage"), ("frage", "Fall · Verpflichtung oder Bescheidung?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 300, BODEN - 2, 380, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 760, 600, 90, beim("klage", "Verpflichtungsklage"), fuell=WEISS),
    pl("Klage: Erlaubnis erteilen", 760, 640, beim("klage", "beantragt"), fill=WEISS, size=28, anker="m"),
    pl("Konkurrenzschutz: nichts mit der Straße", 760, 720, beim("ri1", "Straße"), fill=ROT, size=28, anker="m"),
    pl("offen: Markttage und Wege", 760, 790, beim("ri1", "Markttage"), fill=GELB, size=28, anker="m"),
    *fig("HA", HAX2, BODEN, FH, [("klage", "ruhig_r"), (beim("ri1", "Über"), "denkt_r"), ("frage", "ruhig_r")]),
    schild("Herr Haberland", HAX2, "klage", HA_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [("gericht", "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "frage"),
    peep_voll("RI_ruhig", RIX, BODEN, FH, "frage", anim="cut"),
    schild("die Richterin", RIX, "gericht", RI_F, unten=BODEN),
    blase("sprech", 960, 250, "ri1", 1240, 220, inhalt=["Konkurrenzschutz hat mit der Straße nichts zu tun.",
                                                       "Über Markttage und Wege muss die Stadt",
                                                       "aber noch selbst entscheiden."], textsize=30, figur=RIb, bis="frage"),
    pl("Verpflichtungsurteil oder Bescheidungsurteil?", 1240, 170, "frage", fill=PINK, size=36, anker="m"),
    pl("Und die Kosten?", 1240, 255, "frage2", fill=WEISS, size=34, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Haberland führt ein Gasthaus am Marktplatz einer amtsfreien Stadt in Brandenburg. Am 2. Februar 2026 beantragt er "
    "eine Sondernutzungserlaubnis für 8 Tische auf dem Platz, von Mai bis September. Mit Bescheid vom 10. März 2026 lehnt "
    "die Stadt ab: Am Markt gebe es schon 2 Terrassen, man wolle die anderen Wirte vor Konkurrenz schützen. Der Widerspruch "
    "wird mit Widerspruchsbescheid vom 5. Mai 2026 zurückgewiesen.",
    "Herr Haberland erhebt fristgerecht Verpflichtungsklage und beantragt, ihm die Erlaubnis zu erteilen. Das Gericht "
    "stellt fest: Andere Belange mit Bezug zur Straße (Wochenmarkt, Wege für Fußgänger) hat die Stadt noch nicht abgewogen.",
], "Verpflichtungsurteil oder Bescheidungsurteil? Und wer trägt die Kosten?")

# D Spruchreife kurz ------------------------------------------------------------------------------------------------------------
folie([("spr", "Vorfrage · Spruchreife, § 113 V VwGO")], rechts_frei([
    *tafel("spr", "Kurz zur Spruchreife"),
    z("Erlaubnis: „nach pflichtgemäßem Ermessen“", 110, 190, beim("spr", "Ermessen"), "Bold", 34),
    zit("§ 18 Abs. 2 Satz 3 BbgStrG (Beispiel Brandenburg)", 150, 242, beim("spr", "Paragraf")),
    z("Konkurrenzschutz: kein Bezug zur Straße", 110, 320, beim("sach", "Konkurrenzschutz"), "Bold", 34),
    z("Ablehnung ermessensfehlerhaft", 150, 372, beim("sach", "ermessensfehlerhaft"), size=34),
    nein(700, 392, beim("sach", "ermessensfehlerhaft"), gr=24),
    zit("vgl. OVG NRW, Beschl. v. 1.7.2014 – 11 A 1081/12, Rn. 8 f.", 150, 424, beim("sach", "ermessensfehlerhaft")),
    z("spruchreif nur bei Ermessensreduzierung auf null", 110, 500, beim("null", "Spruchreif"), "Bold", 34),
    z("hier: Markttage und Wege noch abzuwägen", 150, 552, beim("null", "Markttage"), size=34),
    blk(110, 630, 1040, 70, ROT, beim("null", "abzuwägen"), [("nicht spruchreif", "ExtraBold", 38, INK)]),
    pl("Prüfung: Video zur Verpflichtungsklage", 110, 750, "verweis", fill=PINK, size=30),
    ficon("tabler", "calendar", IX, IU, 120, beim("null", "Markttage"), fuell=WEISS),
    pl("Wochenmarkt", IX, 200, beim("null", "Markttage"), fill=WEISS, size=28, anker="m"),
    *fig("RI", FX, FB, FR, [("spr", "ruhig")]),
    schild("die Richterin", FX, "spr", RI_F),
]))

# E 1. Antrag: Wortlaut § 88 VwGO ----------------------------------------------------------------------------------------------
W88 = "„Das Gericht darf über das Klagebegehren nicht hinausgehen, ist aber an die Fassung der Anträge nicht gebunden.“"
Z88 = ["„Das Gericht darf über das Klagebegehren nicht hinausgehen,",
       "ist aber an die Fassung der Anträge nicht gebunden.“"]
w88, w88_y = wortlaut(80, 150, 1100, W88, "§ 88 VwGO", "wl88", size=34, zeilen=Z88,
                      marken=[("nicht hinausgehen,", beim("wl88", "hinausgehen")),
                              ("nicht gebunden.“", beim("wl88", "gebunden"))])
folie([("wl88", "1. Antrag › Klagebegehren, § 88 VwGO")], rechts_frei([
    titel(glyphen("Erstens: der Antrag"), 110, 60, "wl88", 44),
    *w88,
    z("maßgeblich: das wirkliche Rechtsschutzziel", 110, w88_y + 30, beim("ziel", "wirkliche"), "Bold", 34),
    zit("BVerwG, Beschl. v. 23.11.2022 – 6 B 22.22, Rn. 19", 150, w88_y + 82, beim("ziel", "Rechtsschutzziel")),
    z("Verpflichtungsantrag enthält regelmäßig als Minus", 110, w88_y + 150, beim("minus", "Verpflichtungsantrag"), "Bold", 34),
    z("den Antrag auf Bescheidung", 150, w88_y + 202, beim("minus", "Antrag"), size=34),
    zit("BVerwG, Beschl. v. 23.11.2022 – 6 B 22.22, Rn. 20", 150, w88_y + 254, beim("minus", "Bescheidung")),
    z("ausdrücklicher Hilfsantrag auf Neubescheidung: nicht nötig", 110, w88_y + 322, beim("hilfs", "Hilfsantrag"), size=32),
    z("nie mehr als beantragt: nicht 10 statt 8 Tische", 110, w88_y + 390, beim("mehr", "Mehr"), "Bold", 32),
    nein(950, w88_y + 410, beim("mehr", "zehn"), gr=22),
    ficon("tabler", "file-text", IX, IU, 110, "wl88", fuell=WEISS),
    pl("Antrag: Erlaubnis erteilen", IX, 150, "wl88", fill=WEISS, size=28, anker="m"),
    pl("darin: Bescheidung", IX, 215, beim("minus", "Minus"), fill=GRUEN, size=28, anker="m"),
    *fig("HA", FX, FB, FR, [("wl88", "denkt"), ("minus", "ruhig")]),
    schild("Herr Haberland", FX, "wl88", HA_F),
]))

# F 2. Tenor: Wortlaut § 113 Abs. 5 VwGO -------------------------------------------------------------------------------------------
W113 = ("„Soweit die Ablehnung oder Unterlassung des Verwaltungsakts rechtswidrig und der Kläger dadurch in seinen Rechten "
        "verletzt ist, spricht das Gericht die Verpflichtung der Verwaltungsbehörde aus, die beantragte Amtshandlung "
        "vorzunehmen, wenn die Sache spruchreif ist. Andernfalls spricht es die Verpflichtung aus, den Kläger unter Beachtung "
        "der Rechtsauffassung des Gerichts zu bescheiden.“")
Z113 = ["„Soweit die Ablehnung oder Unterlassung des Verwaltungsakts",
        "rechtswidrig und der Kläger dadurch in seinen Rechten verletzt",
        "ist, spricht das Gericht die Verpflichtung der Verwaltungsbehörde",
        "aus, die beantragte Amtshandlung vorzunehmen, wenn die Sache",
        "spruchreif ist. Andernfalls spricht es die Verpflichtung aus,",
        "den Kläger unter Beachtung der Rechtsauffassung des Gerichts",
        "zu bescheiden.“"]
w113, w113_y = wortlaut(80, 150, 1100, W113, "§ 113 Abs. 5 VwGO", "wl113", size=31, zeilen=Z113,
                        marken=[("rechtswidrig", beim("wl113", "rechtswidrig")),
                                ("Verpflichtung der Verwaltungsbehörde", beim("wl113", "Verpflichtung")),
                                ("spruchreif ist.", beim("wl113", "spruchreif")),
                                ("Andernfalls", beim("satz2", "Andernfalls")),
                                ("unter Beachtung der Rechtsauffassung des Gerichts", beim("satz2", "Beachtung"))])
folie([("wl113", "2. Tenor › Verpflichtung oder Bescheidung, § 113 V VwGO")], rechts_frei([
    titel(glyphen("Zweitens: der Tenor"), 110, 60, "wl113", 44),
    *w113,
    *reihe([("Satz 1: Verpflichtungsurteil", beim("wl113", "spruchreif"), GRUEN),
            ("Satz 2: Bescheidungsurteil", beim("satz2", "Andernfalls"), GELB)], 110, w113_y + 34),
    ficon(HC, "balance-scale", IX, IU, 150, "wl113", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("wl113", "ruhig")]),
    schild("die Richterin", FX, "wl113", RI_F),
]))

# G Tenor bei Spruchreife (Verpflichtungsurteil), Beklagter in Brandenburg ---------------------------------------------------------
folie([("bekl", "2. Tenor › wenn spruchreif: Verpflichtungsurteil, § 113 V 1 VwGO")], rechts_frei([
    *tafel("bekl", "Vorweg: Wer ist Beklagter?"),
    *zz("Beklagter:", "die Behörde selbst, hier der Bürgermeister", 110, 180, beim("bekl", "Brandenburg"),
        beim("bekl", "Behörde"), size=32, rest_stil="Regular"),
    zit("§ 78 Abs. 1 Nr. 2 VwGO i. V. m. § 8 Abs. 2 BbgVwGG", 150, 230, beim("bekl", "Paragraf")),
    z("Wäre die Sache spruchreif:", 110, 300, beim("vu", "Wäre"), "ExtraBold", 34),
    *tenorbox(90, 420, 1090, 270, beim("vu", "Bescheid")),
    z("Der Bescheid des Beklagten vom 10. März 2026", 120, 440, beim("vu", "Bescheid"), size=32),
    z("in Gestalt des Widerspruchsbescheids vom 5. Mai 2026", 120, 488, beim("vu", "Gestalt"), size=32),
    z("wird aufgehoben.", 120, 536, beim("vu", "aufgehoben"), "Bold", 32),
    z("Der Beklagte wird verpflichtet, dem Kläger die beantragte", 120, 584, beim("vu2", "Beklagte"), "Bold", 32),
    z("Sondernutzungserlaubnis zu erteilen.", 120, 632, beim("vu2", "Sondernutzungserlaubnis"), "Bold", 32),
    z("Aufhebung: zur Klarstellung, üblich mit ausgesprochen", 110, 730, beim("klar", "Aufhebung"), size=32),
    zit("BVerwG, Beschl. v. 12.5.2020 – 6 B 53.19, Rn. 5", 150, 778, beim("klar", "Klarstellung")),
    zit("Tenorformel: Klausurkonvention nach § 113 Abs. 5 Satz 1 VwGO", 110, 830, beim("klar", "mit")),
    ficon(HC, "classical-building", IX, IU, 150, "bekl", fuell=WEISS),
    pl("wenn spruchreif", IX, 160, beim("vu", "spruchreif"), fill=GRUEN, size=28, anker="m"),
    *fig("HA", FX, FB, FR, [("bekl", "ruhig"), ("vu2", "hofft")]),
    schild("Herr Haberland", FX, "bekl", HA_F),
]))

# H Bescheidungsurteil ------------------------------------------------------------------------------------------------------------
folie([("bu", "2. Tenor › hier: Bescheidungsurteil, § 113 V 2 VwGO")], rechts_frei([
    *tafel("bu", "Hier fehlt die Spruchreife"),
    *tenorbox(90, 230, 1090, 430, beim("bu", "erste")),
    z("Der Bescheid des Beklagten vom 10. März 2026 in Gestalt", 120, 250, beim("bu", "erste"), size=32),
    z("des Widerspruchsbescheids vom 5. Mai 2026 wird aufgehoben.", 120, 298, beim("bu", "erste"), size=32),
    z("Der Beklagte wird verpflichtet, über den Antrag des Klägers", 120, 360, beim("bu2", "Beklagte"), "Bold", 32),
    z("vom 2. Februar 2026 unter Beachtung der Rechtsauffassung", 120, 408, beim("bu2", "zweiten"), "Bold", 32),
    z("des Gerichts erneut zu entscheiden.", 120, 456, beim("bu2", "erneut"), "Bold", 32),
    pl("Antrag: Erlaubnis erteilen", 120, 520, beim("ueb", "Erlaubnis"), fill=WEISS, size=28),
    z("Im Übrigen wird die Klage abgewiesen.", 120, 590, beim("ueb", "Im"), "Bold", 34),
    zit("vgl. Tenor OVG NRW, Urt. v. 12.5.2023 – 7 D 328/21.AK", 110, 690, beim("ueb", "abgewiesen")),
    ficon("tabler", "file-text", IX, IU, 110, "bu", fuell=WEISS),
    pl("neu entscheiden", IX, 150, beim("bu2", "erneut"), fill=GELB, size=28, anker="m"),
    pl("im Übrigen: abgewiesen", IX, 215, beim("ueb", "abgewiesen"), fill=ROT, size=28, anker="m"),
    *fig("HA", FX, FB, FR, [("bu", "denkt"), (beim("ueb", "abgewiesen"), "sorge")]),
    schild("Herr Haberland", FX, "bu", HA_F),
]))

# I 3. Kosten: Wortlaut § 155 Abs. 1 Satz 1 VwGO -------------------------------------------------------------------------------------
W155 = "„Wenn ein Beteiligter teils obsiegt, teils unterliegt, so sind die Kosten gegeneinander aufzuheben oder verhältnismäßig zu teilen.“"
Z155 = ["„Wenn ein Beteiligter teils obsiegt, teils unterliegt, so sind",
        "die Kosten gegeneinander aufzuheben oder verhältnismäßig",
        "zu teilen.“"]
w155, w155_y = wortlaut(80, 150, 1100, W155, "§ 155 Abs. 1 Satz 1 VwGO", "kosten", size=32, zeilen=Z155,
                        marken=[("teils unterliegt,", beim("kosten", "unterliegt")),
                                ("verhältnismäßig", beim("kosten", "verhältnismäßig"))])
folie([("kosten", "3. Kosten › teilweises Unterliegen, § 155 I 1 VwGO")], rechts_frei([
    titel(glyphen("Drittens: die Kosten"), 110, 60, "kosten", 44),
    *w155,
    z("Erlaubnis verlangt, nur Bescheidung erhalten:", 110, w155_y + 30, beim("teil", "Erlaubnis"), size=34),
    z("teilweise unterlegen", 150, w155_y + 82, beim("teil", "unterliegt"), "Bold", 34),
    zit("vgl. OVG NRW, Urt. v. 12.5.2023 – 7 D 328/21.AK, Rn. 24, 116", 150, w155_y + 134, beim("teil", "teilweise")),
    z("keine feste Quote im Gesetz; häufig hälftig", 110, w155_y + 200, beim("quote", "Quote"), size=34),
    *tenorbox(90, w155_y + 310, 1090, 120, beim("t3", "Kosten")),
    z("Die Kosten des Verfahrens tragen der Kläger und", 120, w155_y + 328, beim("t3", "Kosten"), size=32),
    z("der Beklagte je zur Hälfte.", 120, w155_y + 376, beim("t3", "Beklagte"), "Bold", 32),
    zit("vgl. BVerwG, Urt. v. 7.10.2020 – 2 C 5.20, Rn. 56", 110, w155_y + 452, beim("t3", "Hälfte")),
    ficon("tabler", "calculator", IX, IU, 110, "kosten", fuell=WEISS),
    pl("je 1/2", IX, 210, beim("t3", "Hälfte"), fill=GELB, size=30, anker="m"),
    *fig("HA", FX, FB, FR, [("kosten", "denkt"), (beim("teil", "unterliegt"), "sorge")]),
    schild("Herr Haberland", FX, "kosten", HA_F),
]))

# J Klausurtipp (Lexi): Kostenvergleich ---------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Bescheidungsantrag, wenn nicht spruchreif")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Ermessen nicht auf null reduziert:", 200, 200, beim("tipp", "Ermessen"), "Bold", 34),
    z("von Anfang an nur die Bescheidung beantragen", 200, 252, beim("tipp", "beantrage"), "Bold", 34),
    pl("angenommen: Kosten insgesamt 3.000 €", 110, 340, beim("rech", "dreitausend"), fill=WEISS, size=30),
    blk(110, 410, 1040, 60, ROT, beim("rech", "Verpflichtungsantrag"), [("Verpflichtungsantrag", "ExtraBold", 34, INK)]),
    z("Herr Haberland trägt 1/2 = 1.500 €", 140, 485, beim("rech", "Hälfte"), "Bold", 34),
    blk(110, 570, 1040, 60, GRUEN, beim("rech2", "Bescheidungsantrag"), [("Bescheidungsantrag", "ExtraBold", 34, INK)]),
    z("Herr Haberland trägt 0 €, der Beklagte alles", 140, 645, beim("rech2", "Beklagte"), "Bold", 34),
    zit("§ 154 Abs. 1 VwGO", 140, 697, beim("rech2", "Paragraf")),
    z("soweit das Gericht seiner Rechtsauffassung folgt", 110, 770, beim("rech3", "Gericht"), size=32),
    zit("vgl. BVerwG, Urt. v. 24.9.2009 – 7 C 2.09, Rn. 67", 150, 818, beim("rech3", "folgt")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "vollstr"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# K 4. Vorläufige Vollstreckbarkeit -------------------------------------------------------------------------------------------------
folie([("vollstr", "4. Vorläufige Vollstreckbarkeit, § 167 II VwGO")], rechts_frei([
    *tafel("vollstr", "Viertens: vorläufige Vollstreckbarkeit", h=520),
    z("nur wegen der Kosten", 110, 200, beim("vollstr", "Kosten"), "Bold", 36),
    zit("§ 167 Abs. 2 VwGO", 150, 254, beim("vollstr", "Paragraf")),
    pl("Formel: Video zum Anfechtungsurteil", 110, 340, beim("vollstr", "Formel"), fill=PINK, size=30),
    ficon("tabler", "coin", IX, IU, 110, "vollstr", fuell=GELB),
    *fig("RI", FX, FB, FR, [("vollstr", "ruhig")]),
    schild("die Richterin", FX, "vollstr", RI_F),
]))

# L Der vollständige Tenor (zum Mitschreiben, erscheint auf einmal) ----------------------------------------------------------------
els_v = [karte(110, 60, 1700, 900, "voll", fill=HELL), titel(glyphen("Der vollständige Tenor"), 170, 105, "voll", 56)]
y = 215
for absz, stil in (("Der Bescheid des Beklagten vom 10. März 2026 in Gestalt des Widerspruchsbescheids vom 5. Mai 2026 "
                    "wird aufgehoben.", "Bold"),
                   ("Der Beklagte wird verpflichtet, über den Antrag des Klägers vom 2. Februar 2026 unter Beachtung der "
                    "Rechtsauffassung des Gerichts erneut zu entscheiden.", "Bold"),
                   ("Im Übrigen wird die Klage abgewiesen.", "Bold"),
                   ("Die Kosten des Verfahrens tragen der Kläger und der Beklagte je zur Hälfte.", "Regular"),
                   ("Das Urteil ist wegen der Kosten vorläufig vollstreckbar. …", "Regular")):
    e, y = absatz(glyphen(absz), 170, y, 1580, "voll", size=38, stil=stil)
    els_v += e; y += 28
assert y < 860, y
els_v.append(zit("Tenorformeln: Klausurkonvention nach §§ 113 Abs. 5, 155 Abs. 1, 167 Abs. 2 VwGO; Abwendungsbefugnis wie beim "
                 "Anfechtungsurteil", 170, 880, "voll", rechts=1790))
folie([("voll", "Ergebnis · Der vollständige Tenor")], els_v)

# M Schema ----------------------------------------------------------------------------------------------------------------------
SZ, LH = 36, 88
els_s = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Schema: Verpflichtungs- oder Bescheidungsurteil"), 110, 85, "sch", 46)]
zeilen_s = [
    zz("1. Antrag:", "Klagebegehren, § 88 VwGO", 110, 200, "s1", beim("s1", "Klagebegehren"), size=SZ, rest_stil="Regular", rechts=1820),
    [z("Bescheidung steckt als Minus im Verpflichtungsantrag", 160, 200 + LH, beim("s1", "Bescheidung"), size=SZ, rechts=1820)],
    zz("2. Tenor:", "Aufhebung, dann Verpflichtung zum Erlass, wenn spruchreif (§ 113 Abs. 5 Satz 1)", 110, 200 + 2 * LH,
       "s2", beim("s2", "Aufhebung"), size=SZ, rest_stil="Regular", rechts=1820),
    [z("sonst Verpflichtung zur Neubescheidung (§ 113 Abs. 5 Satz 2)", 160, 200 + 3 * LH, "s2b", size=SZ, rechts=1820)],
    [z("im Übrigen Klageabweisung", 160, 200 + 4 * LH, "s2c", size=SZ, rechts=1820)],
    zz("3. Kosten:", "§ 154 Abs. 1 oder § 155 Abs. 1 Satz 1 VwGO", 110, 200 + 5 * LH, "s3", beim("s3", "Paragraf"), size=SZ,
       rest_stil="Regular", rechts=1820),
    zz("4. Vorläufige Vollstreckbarkeit:", "wegen der Kosten (§ 167 Abs. 2 VwGO)", 110, 200 + 6 * LH, "s4",
       beim("s4", "wegen"), size=SZ, rest_stil="Regular", rechts=1820),
]
for zl in zeilen_s:
    els_s += zl
folie([("sch", "Schema · Verpflichtungs- oder Bescheidungsurteil")], els_s)

# N Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Fehlt die ", 0), ("Spruchreife", "a"), (",", 0)]], 750, 320, 46, "merke", {"a": beim("merke", "Spruchreife")}),
    *markertext([[("ergeht nur ein Bescheidungsurteil.", 0)]], 750, 385, 46, beim("merke", "ergeht"), {}),
    *markertext([[("Wer trotzdem die Verpflichtung beantragt,", 0)]], 750, 535, 46, "m2", {}),
    *markertext([[("unterliegt ", 0), ("teilweise", "b")]], 750, 600, 46, beim("m2", "unterliegt"), {"b": beim("m2", "teilweise")}),
    *markertext([[("und trägt anteilig die Kosten.", 0)]], 750, 665, 46, beim("m2", "trägt"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
