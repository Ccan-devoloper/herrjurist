"""Folge 101 · Formelle Verfassungsmäßigkeit: So entsteht ein Bundesgesetz – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Vorbild offengelegt: Zuwanderungsgesetz, BVerfG 2 BvF 1/02): Der Bundestag beschließt kurz vor Mitternacht ein
zustimmungsbedürftiges Gesetz (Art. 84 I 6 GG); im Bundesrat stimmt ein Land uneinheitlich (Hensel „Ja“, Rieger „Nein“), der
Präsident wertet das als Ja; Ausfertigung und Verkündung im elektronischen Bundesgesetzblatt.
Szenen laut ../SZENENPLAN.md: A Bundestag nachts, B Bundesrat, C Ausfertigung/Verkündung/Meldebehörde, D Sachverhalt,
E Einordnung und I. Zuständigkeit, F II. 1. Initiative, G 2. Beschluss des Bundestages (Wortlaut Art. 77 I 1),
H 3. Einspruchs- oder Zustimmungsgesetz, I Vermittlungsausschuss/Einspruch, J Wortlaut Art. 78, K Stimmabgabe (Wortlaut
Art. 51 III 2), L III. Form (Auszug Art. 82 I), M Ergebnis, N Klausurtipp (Lexi), O Klausurschema als Weg, P Merksatz (Lexi).
Ein Handlungsgeräusch: Unterschrift bei der Ausfertigung (Freesound CC0). Hilfsfunktionen wie Folge 098 (eigene Kopie)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_101/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
DUNKEL = (58, 58, 72, 255)
ROTHELL = (253, 232, 228, 255)
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
    """Zeile in zwei Teilen: erster Teil zur Marke, Rest erst zum gesprochenen Wort (nie vor dem Wort)."""
    a = z(kopf, x, y, c_kopf, stil, size, **k)
    dx = F(stil, size).getlength(kopf + " ")
    return [a, z(rest, x + dx, y, c_rest, rest_stil or stil, size, **k)]


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46, tc=None):
    """Karte zur Marke, Titel erst zum gesprochenen Titelwort (tc)."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, tc or cue, size)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_101/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe; feste
    Zeilen ergeben zusammen genau den Text. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen
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


# --- Eigene Hilfsfunktion (wie Folge 093/074/098): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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



def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts (Kopie aus Folge 081)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, x, y, cue, stil="Regular", size=34, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 22, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, x, y, cue, stil="Regular", size=34, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 22, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
X1, X2 = 1390, 1730                         # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
def boden(cue, hart_=False):
    e = linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e



NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PR_F, HS_F, RI_F, KA_F = BLAU, GRUEN, LILA, ROT   # Farben der Namensschilder
FV = "Formelle Verfassungsmäßigkeit"
VF = "II. Verfahren"
BR3 = f"{VF} › 3. Beteiligung des Bundesrates"
ZW = "BVerfG, Urt. v. 18.12.2002 – 2 BvF 1/02"
EV = "BVerfG, Beschl. v. 15.1.2008 – 2 BvL 12/01, Rn. 71"


def punkt(cx, cy, r, cue, fill=GELB):
    """Station auf dem Weg des Gesetzes (Klausurschema): Kreis mit Tuschekontur."""
    s = 3
    im = Image.new("RGBA", ((2 * r + 8) * s, (2 * r + 8) * s))
    ImageDraw.Draw(im).ellipse((4 * s, 4 * s, (2 * r + 4) * s, (2 * r + 4) * s), fill=fill, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")


# A Fall: Bundestag kurz vor Mitternacht ----------------------------------------------------------------------------------------
folie([(NULL, "Fall · Nachts im Bundestag")], [
    boden(NULL, True),
    hart(pl("Bundestag, kurz vor Mitternacht", 70, 40, NULL, fill=LILA, size=40)),
    ficon(HC, "classical-building", 330, BODEN - 2, 400, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "moon-stars", 1720, 260, 130, NULL, fuell=GELB, anim="cut"),
    pl("Entwurf: Bundesregierung", 700, 190, beim("entw", "Bundesregierung"), fill=WEISS, size=32),
    pl("Stellungnahme: Bundesrat", 700, 270, beim("entw", "Stellung"), fill=WEISS, size=32),
    pl("Gesetz: Meldebehörden nur noch digital", 700, 370, beim("gesetz", "digital"), fill=GELB, size=32),
    pl("festes Verfahren, ohne Abweichung der Länder", 700, 450, beim("gesetz", "festen"), fill=WEISS, size=30),
    *[ficon("tabler", "armchair", 780 + i * 190, BODEN - 2, 120, beim("leer", "leer"), fuell=WEISS) for i in range(6)],
    pl("Beschlussfähigkeit: kein Zweifel", 700, 560, beim("leer", "niemand"), fill=WEISS, size=30),
    pl("Mehrheit: Ja", 1330, 560, beim("mehrheit", "Ja"), fill=GRUEN, size=34),
    ok(1620, 590, beim("mehrheit", "Ja"), gr=24),
])

# B Fall: Abstimmung im Bundesrat -------------------------------------------------------------------------------------------------
PRX, HSX, RIX = 420, 1180, 1560
PRa = ("PR_redet_r", PRX, BODEN, FH)
HSa = ("HS_redet", HSX, BODEN, FH)
RIa = ("RI_redet", RIX, BODEN, FH)
HSN, RIN = beim("land", "Hensel"), beim("land", "Rieger")
folie([("br", "Fall · Abstimmung im Bundesrat")], [
    boden("br"),
    pl("Einige Wochen später: Bundesrat", 70, 40, "br", fill=BLAU, size=36),
    *fig("PR", PRX, BODEN, FH, [("br", "ruhig_r")], bis="p1"),
    *redet("PR_redet_r", PRX, BODEN, FH, "p1", "hen1"),
    *fig("PR", PRX, BODEN, FH, [("hen1", "ruhig_r")], erst="cut", bis="p2"),
    *redet("PR_redet_r", PRX, BODEN, FH, "p2", "knapp"),
    *fig("PR", PRX, BODEN, FH, [("knapp", "entschlossen_r")], erst="cut"),
    ficon("tabler", "podium", PRX + 200, BODEN - 2, 210, "br", fuell=WEISS),
    schild("Der Bundesratspräsident", PRX, "br", PR_F, unten=BODEN),
    *fig("HS", HSX, BODEN, FH, [(HSN, "ruhig")], bis="hen1"),
    *redet("HS_redet", HSX, BODEN, FH, "hen1", "rie1"),
    *fig("HS", HSX, BODEN, FH, [("rie1", "denkt"), ("knapp", "ruhig")], erst="cut"),
    schild("Ministerin Hensel", HSX, HSN, HS_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [(RIN, "ruhig"), ("hen1", "denkt")], bis="rie1"),
    *redet("RI_redet", RIX, BODEN, FH, "rie1", "p2"),
    *fig("RI", RIX, BODEN, FH, [("p2", "aerger")], erst="cut"),
    schild("Minister Rieger", RIX, RIN, RI_F, unten=BODEN),
    blase("sprech", 620, 200, "p1", 820, 230, inhalt=["Ich rufe das Land auf.", "Wie stimmt das Land ab?"], textsize=32,
          figur=PRa, bis="hen1"),
    blase("sprech", 440, 160, "hen1", 1100, 230, inhalt=["Für das Land: Ja."], textsize=32, figur=HSa, bis="rie1"),
    blase("sprech", 460, 160, "rie1", 1560, 230, inhalt=["Und ich sage: Nein."], textsize=32, figur=RIa, bis="p2"),
    blase("sprech", 760, 210, "p2", 880, 230, inhalt=["Das werte ich als Ja. Damit", "hat der Bundesrat zugestimmt."],
          textsize=32, figur=PRa, bis="knapp"),
    blk(1170, 170, 400, 76, GELB, beim("knapp", "vier"), [("das Land: 4 Stimmen", "ExtraBold", 34, INK)]),
    pl("ohne sie: keine Mehrheit", 1370, 280, beim("knapp", "keine"), fill=ROT, size=32, anker="m"),
])

# C Fall: Ausfertigung, Verkündung, Meldebehörde ---------------------------------------------------------------------------------
KAX = 1460
KAa = ("KA_redet", KAX, BODEN, FH)
KAN = beim("ka", "Kähler")
folie([("aus", "Fall · Ausgefertigt und verkündet"), ("frage", "Fall · Ist das Gesetz wirksam?")], [
    boden("aus"),
    pl("Ausfertigung und Verkündung", 70, 40, "aus", fill=GELB, size=36),
    ficon("tabler", "file-text", 300, 400, 120, "aus", fuell=WEISS),
    szene(ficon("tabler", "signature", 300, 560, 220, beim("aus", "fertigt"), fuell=WEISS), "101unterschrift*", 0.8, 0.05),
    pl("Bundespräsident: ausgefertigt", 300, 600, beim("aus", "fertigt"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "device-laptop", 790, 560, 280, beim("bgbl", "Bundesgesetzblatt"), fuell=WEISS),
    pl("Bundesgesetzblatt", 790, 600, beim("bgbl", "Bundesgesetzblatt"), fill=GELB, size=30, anker="m"),
    pl("im Internet", 790, 680, beim("bgbl", "Internet"), fill=WEISS, size=30, anker="m"),
    *fig("KA", KAX, BODEN, FH, [(KAN, "ruhig")], bis="ka1"),
    *redet("KA_redet", KAX, BODEN, FH, "ka1", "frage"),
    *fig("KA", KAX, BODEN, FH, [("frage", "denkt"), ("vorbild", "ruhig")], erst="cut"),
    schild("Frau Kähler, Meldebehörde", KAX, KAN, KA_F, unten=BODEN),
    blase("sprech", 620, 200, "ka1", 1160, 230, inhalt=["Ab 1. März machen wir", "also alles digital!"], textsize=32,
          figur=KAa, bis="frage"),
    blk(470, 170, 700, 80, PINK, beim("frage", "wirksam"), [("wirksam zustande gekommen?", "ExtraBold", 36, INK)]),
    pl("Vorbild: Zuwanderungsgesetz, BVerfG 2002", 820, 290, "vorbild", fill=WEISS, size=30, anker="m"),
])

# D Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Kurz vor Mitternacht beschließt der Bundestag ein Gesetz der Bundesregierung (der Bundesrat hatte Stellung "
    "genommen): Die Meldebehörden der Länder bearbeiten Anträge nur noch digital, nach einem festen Verfahren ohne "
    "Abweichungsmöglichkeit. Niemand bezweifelt die Beschlussfähigkeit.",
    "Im Bundesrat sagt für ein Land mit 4 Stimmen Ministerin Hensel „Ja“, Minister Rieger „Nein“. Der Präsident wertet "
    "das als Ja: Zustimmung. Ohne die 4 Stimmen gäbe es keine Mehrheit. Der Bundespräsident fertigt aus, das Gesetz wird "
    "im Bundesgesetzblatt verkündet.",
], "Ist das Gesetz wirksam zustande gekommen?")

# E Einordnung, I. Zuständigkeit ---------------------------------------------------------------------------------------------------
folie([("einord", f"{FV} des Bundesgesetzes"), ("komp", f"{FV} › I. Zuständigkeit, Art. 73 I Nr. 3 GG")], rechts_frei([
    *tafel("einord", "Formelle Verfassungsmäßigkeit", tc=beim("einord", "formelle")),
    z("des Bundesgesetzes", 110, 175, beim("einord", "Bundesgesetzes"), "Bold", 34),
    blk(110, 245, 1040, 80, GELB, "zust", [("I. Zuständigkeit", "ExtraBold", 36, INK)]),
    z("II. Verfahren", 110, 350, beim("verf", "Verfahren"), "Bold", 36),
    z("III. Form", 110, 410, beim("form", "Form"), "Bold", 36),
    z("Zuständigkeit: Meldewesen, Art. 73 Abs. 1 Nr. 3 GG", 110, 510, beim("komp", "Meldewesen"), size=34),
    *okz("ausschließliche Gesetzgebung des Bundes", 195, 570, beim("komp", "ausschließlichen"), "Bold", 34),
    pl("Mehr dazu: Video Gesetzgebungskompetenz", 110, 680, beim("verw", "Video"), fill=WEISS, size=30),
    ficon(HC, "classical-building", IX, IU, 150, "einord", fuell=WEISS),
    *fig("KA", FX, FB, FR, [("einord", "ruhig"), ("komp", "denkt"), ("verw", "froh")]),
    schild("Frau Kähler", FX, "einord", KA_F),
]))

# F II. 1. Gesetzesinitiative ------------------------------------------------------------------------------------------------------
folie([("ini", f"{VF} · der Weg des Gesetzes"), (beim("ini", "Erstens"), f"{VF} › 1. Gesetzesinitiative, Art. 76 GG")], rechts_frei([
    pl("II. Verfahren: der Weg des Gesetzes", 110, 300, beim("ini", "Verfahren"), fill=GELB, size=36, bis=beim("ini", "Erstens")),
    *tafel(beim("ini", "Erstens"), "1. Gesetzesinitiative, Art. 76 GG", size=44, tc=beim("ini", "Gesetzesinitiative")),
    z("Vorlagen bringen ein, Art. 76 Abs. 1 GG:", 110, 175, "ini2", "Bold", 34),
    z("die Bundesregierung", 150, 235, beim("ini2", "Bundesregierung"), size=34),
    z("der Bundesrat", 150, 290, beim("ini2", "Bundesrat"), size=34),
    z("aus der Mitte des Bundestages", 150, 345, beim("ini2", "Mitte"), size=34),
    z("Vorlage der Bundesregierung: zuerst an den Bundesrat", 110, 440, beim("vor", "zuerst"), "Bold", 32),
    z("Vorlage des Bundesrates: über die Bundesregierung", 110, 495, beim("vor2", "über"), "Bold", 32),
    z("Frist in der Regel 6 Wochen", 150, 550, beim("vor2", "sechs"), size=32),
    zit("Art. 76 Abs. 2 Satz 2, Abs. 3 Satz 1 GG", 150, 600, beim("vor2", "Wochen")),
    *okz("im Fall: so geschehen", 195, 680, beim("ini3", "Fall"), "Bold", 34),
    ficon("tabler", "route", IX, IU, 130, beim("ini", "Weg"), fuell=None, bis="ini2"),
    ficon("tabler", "file-text", IX, IU, 120, "ini2", fuell=WEISS, anim="cut"),
    *fig("HS", FX, FB, FR, [("ini", "ruhig"), ("ini3", "froh")]),
    schild("Frau Hensel", FX, "ini", HS_F),
]))

# G II. 2. Beschluss des Bundestages, Wortlaut Art. 77 I 1 ----------------------------------------------------------------------------
W77 = "„Die Bundesgesetze werden vom Bundestage beschlossen.“"
w77, w77_y = wortlaut(80, 150, 1100, W77, "Art. 77 Abs. 1 Satz 1 GG", "bt", size=36, zeilen=[W77],
                      marken=[("vom Bundestage", beim("bt", "Bundestage", nr=2)), ("beschlossen.“", beim("bt", "beschlossen"))])
folie([("bt", f"{VF} › 2. Beschluss des Bundestages, Art. 77 I 1 GG"), ("nacht", f"{VF} › 2. Beschluss › Beschlussfähigkeit, § 45 GO-BT")],
      rechts_frei([
    titel(glyphen("2. Beschluss des Bundestages"), 110, 65, "bt", 46),
    *w77,
    z("Mehrheit der abgegebenen Stimmen, Art. 42 Abs. 2 GG", 110, w77_y + 30, beim("mehr", "Mehrheit"), "Bold", 34),
    z("nachts? schadet nicht", 110, w77_y + 110, beim("nacht", "schadet"), "Bold", 34),
    z("beschlussfähig: mehr als die Hälfte im Saal", 150, w77_y + 170, beim("nacht", "Hälfte"), size=34),
    zit("§ 45 Abs. 1 GO-BT", 150, w77_y + 220, beim("nacht", "Saal")),
    z("gezählt erst, wenn z. B. eine Fraktion zweifelt", 150, w77_y + 270, beim("nacht", "gezählt"), size=34),
    zit("§ 45 Abs. 2 GO-BT", 150, w77_y + 320, beim("nacht", "bezweifelt")),
    *okz("niemand hat gezweifelt: Beschluss in Ordnung", 195, w77_y + 400, beim("bt2", "niemand"), "Bold", 34),
    ficon(HC, "classical-building", IX, IU, 150, "bt", fuell=WEISS, bis="nacht"),
    ficon("tabler", "moon-stars", IX, IU, 120, "nacht", fuell=GELB, anim="cut"),
    *fig("RI", FX, FB, FR, [("bt", "ruhig"), ("nacht", "denkt"), ("bt2", "ruhig")]),
    schild("Herr Rieger", FX, "bt", RI_F),
]))

# H II. 3. Bundesrat: Einspruchs- oder Zustimmungsgesetz ---------------------------------------------------------------------------
folie([("brt", f"{BR3} › Einspruchs- oder Zustimmungsgesetz")], rechts_frei([
    *tafel("brt", "3. Beteiligung des Bundesrates", size=44),
    z("Einspruchsgesetz oder Zustimmungsgesetz?", 110, 175, beim("brt", "Einspruchsgesetz"), "Bold", 34),
    blk(110, 250, 1040, 76, BLAU, beim("regel", "Regel"), [("Regel: Einspruchsgesetz", "ExtraBold", 36, INK)]),
    z("zustimmungsbedürftig nur, wenn das Grundgesetz", 110, 355, beim("regel", "Zustimmungsbedürftig"), size=34),
    z("es ausdrücklich anordnet", 150, 410, beim("regel", "ausdrücklich"), "Bold", 34),
    z("z. B. Art. 84 Abs. 1 Satz 6 GG:", 110, 495, beim("b84", "Artikel"), "Bold", 34),
    z("Verwaltungsverfahren ohne Abweichungsmöglichkeit", 150, 550, beim("b84", "Verwaltungsverfahren"), size=34),
    *okz("unser Gesetz: braucht die Zustimmung", 195, 645, beim("b84b", "unser"), "Bold", 34),
    ficon(HC, "ballot-box-with-ballot", MB, 380, 130, "brt", fuell=WEISS),
    *fig("HS", X1, FB, FR, [("brt", "ruhig"), ("b84b", "froh")]),
    schild("Frau Hensel", X1, "brt", HS_F),
    *fig("RI", X2, FB, FR, [("brt", "ruhig"), ("b84b", "denkt")], d=0.2),
    schild("Herr Rieger", X2, "brt", RI_F, d=0.3),
]))

# I Vermittlungsausschuss, Einspruch, Zurückweisung ---------------------------------------------------------------------------------
folie([("vma", f"{BR3} › Vermittlungsausschuss, Einspruch, Art. 77 II–IV GG")], rechts_frei([
    *tafel("vma", "Ablauf im Bundesrat", size=44),
    z("Vermittlungsausschuss: binnen 3 Wochen", 110, 175, beim("vma", "Vermittlungsausschuss"), "Bold", 34),
    zit("Art. 77 Abs. 2 Satz 1 GG", 150, 225, beim("vma", "Artikel")),
    z("bei Zustimmungsgesetzen auch Bundestag und Bundesregierung", 110, 275, beim("vma", "Zustimmungsgesetzen"), size=31),
    blk(110, 350, 1040, 76, GELB, beim("ein", "Einspruchsgesetz"), [("Einspruchsgesetz: Einspruch binnen 2 Wochen", "ExtraBold", 33, INK)]),
    zit("Art. 77 Abs. 3 Satz 1 GG", 150, 438, beim("ein", "einlegen")),
    z("Zurückweisung: Mehrheit der Mitglieder des Bundestages", 110, 495, beim("zur", "zurückweisen"), size=32),
    z("Einspruch mit 2/3: Bundestag braucht 2/3", 110, 550, beim("zur", "zwei"), "Bold", 32),
    zit("Art. 77 Abs. 4 GG", 150, 600, beim("zur", "Drittel", nr=2)),
    blk(110, 665, 1040, 76, GRUEN, beim("zug", "Zustimmungsgesetz"), [("Zustimmungsgesetz: Bundesrat muss zustimmen", "ExtraBold", 33, INK)]),
    ficon("tabler", "arrows-split", IX, IU, 120, "vma", fuell=None),
    *fig("PR", FX, FB, FR, [("vma", "ruhig"), ("zug", "entschlossen")]),
    schild("Der Bundesratspräsident", FX, "vma", PR_F),
]))

# J Zustandekommen, Wortlaut Art. 78 --------------------------------------------------------------------------------------------------
W78 = ("„Ein vom Bundestage beschlossenes Gesetz kommt zustande, wenn der Bundesrat zustimmt, den Antrag gemäß Artikel 77 "
       "Abs. 2 nicht stellt, innerhalb der Frist des Artikels 77 Abs. 3 keinen Einspruch einlegt oder ihn zurücknimmt oder "
       "wenn der Einspruch vom Bundestage überstimmt wird.“")
Z78 = ["„Ein vom Bundestage beschlossenes Gesetz kommt zustande,",
       "wenn der Bundesrat zustimmt, den Antrag gemäß Artikel 77",
       "Abs. 2 nicht stellt, innerhalb der Frist des Artikels 77 Abs. 3",
       "keinen Einspruch einlegt oder ihn zurücknimmt oder wenn der",
       "Einspruch vom Bundestage überstimmt wird.“"]
w78, w78_y = wortlaut(80, 170, 1100, W78, "Art. 78 GG", "wl78", size=34, zeilen=Z78,
                      marken=[("der Bundesrat zustimmt", "z1"), ("nicht stellt", "z2"),
                              ("keinen Einspruch einlegt oder ihn zurücknimmt", "z3"),
                              ("vom Bundestage überstimmt wird", beim("z4", "überstimmt"))])
folie([("wl78", f"{BR3} › Zustandekommen, Art. 78 GG")], rechts_frei([
    titel(glyphen("Wann kommt ein Gesetz zustande?"), 110, 70, "wl78", 46),
    *w78,
    z("Vermittlungsausschuss = Antrag nach Art. 77 Abs. 2", 110, w78_y + 40, beim("z2", "Vermittlungsausschuss"), size=32),
    ficon(HC, "check-box-with-check", IX, IU, 120, "z1", fuell=WEISS),
    *fig("HS", FX, FB, FR, [("wl78", "ruhig"), ("z4", "denkt")]),
    schild("Frau Hensel", FX, "wl78", HS_F),
]))

# K Stimmabgabe, Wortlaut Art. 51 III 2 -------------------------------------------------------------------------------------------------
W51 = "„Die Stimmen eines Landes können nur einheitlich und nur durch anwesende Mitglieder oder deren Vertreter abgegeben werden.“"
Z51 = ["„Die Stimmen eines Landes können nur einheitlich und nur",
       "durch anwesende Mitglieder oder deren Vertreter",
       "abgegeben werden.“"]
w51, w51_y = wortlaut(80, 220, 1100, W51, "Art. 51 Abs. 3 Satz 2 GG", "wl51", size=34, zeilen=Z51,
                      marken=[("nur einheitlich", beim("wl51", "einheitlich"))])
folie([("st", f"{BR3} › Stimmabgabe, Art. 51 III 2, 52 III 1 GG")], rechts_frei([
    titel(glyphen("Stimmabgabe im Bundesrat"), 110, 65, "st", 46),
    z("Bundesrat: Mehrheit seiner Stimmen, Art. 52 Abs. 3 Satz 1 GG", 110, 150, beim("st", "Mehrheit"), "Bold", 32),
    *w51,
    *neinz("Ja und Nein: nicht einheitlich", 195, w51_y + 30, beim("uneinh", "nicht"), "Bold", 34),
    z("Präsident durfte nicht als Ja werten", 110, w51_y + 105, beim("nichtja", "Präsident"), "Bold", 34),
    zit(f"{ZW}, Rn. 134, 139 f.", 150, w51_y + 155, beim("nichtja", "Bundesverfassungsgericht")),
    blk(110, w51_y + 215, 1040, 76, ROTHELL, beim("keine", "Mehrheit"), [("keine Mehrheit: keine Zustimmung", "ExtraBold", 36, INK)]),
    z("Gesetz nicht zustande gekommen, Art. 78 GG", 150, w51_y + 310, beim("keine", "zustande"), size=34),
    pl("Ja", X1, 350, beim("uneinh", "ja"), fill=GRUEN, size=34, anker="m"),
    pl("Nein", X2, 350, beim("uneinh", "nein"), fill=ROT, size=34, anker="m"),
    *fig("HS", X1, FB, FR, [("st", "ruhig"), ("nichtja", "denkt")]),
    schild("Frau Hensel", X1, "st", HS_F),
    *fig("RI", X2, FB, FR, [("st", "ruhig"), (beim("uneinh", "nein"), "aerger"), ("keine", "ruhig")], d=0.2),
    schild("Herr Rieger", X2, "st", RI_F, d=0.3),
]))

# L III. Form, Auszug Art. 82 I --------------------------------------------------------------------------------------------------------
W82 = ("„Die nach den Vorschriften dieses Grundgesetzes zustande gekommenen Gesetze werden vom Bundespräsidenten nach "
       "Gegenzeichnung ausgefertigt und im Bundesgesetzblatt verkündet. Das Bundesgesetzblatt kann in elektronischer Form "
       "geführt werden.“")
Z82 = ["„Die nach den Vorschriften dieses Grundgesetzes zustande",
       "gekommenen Gesetze werden vom Bundespräsidenten nach",
       "Gegenzeichnung ausgefertigt und im Bundesgesetzblatt",
       "verkündet. Das Bundesgesetzblatt kann in elektronischer",
       "Form geführt werden.“"]
w82, w82_y = wortlaut(80, 130, 1100, W82, "Art. 82 Abs. 1 Satz 1, 2 GG", "wl82", size=32, zeilen=Z82,
                      marken=[("Gegenzeichnung", beim("wl82", "gegengezeichnet")), ("ausgefertigt", beim("wl82", "ausgefertigt")),
                              ("verkündet.", beim("wl82", "verkündet")),
                              ("nach den Vorschriften dieses Grundgesetzes", beim("pruef", "Vorschriften")),
                              ("in elektronischer", beim("ebgbl", "elektronisch"))])
folie([("form1", f"{FV} › III. Form, Art. 82 GG"), ("ebgbl", "III. Form › Verkündung im elektronischen BGBl."),
       ("inkr", "III. Form › Inkrafttreten, Art. 82 II GG"), ("heil", "III. Form › keine Heilung des Fehlers")], rechts_frei([
    titel(glyphen("III. Form"), 110, 55, "form1", 46),
    *w82,
    z("Gegenzeichnung: Bundeskanzler oder zuständiger Minister", 110, w82_y + 25, beim("gegen", "Bundeskanzler"), size=32),
    zit("Art. 58 Satz 1 GG", 150, w82_y + 75, beim("gegen", "Artikel")),
    z("Bundespräsident prüft: nach dem GG zustande gekommen?", 110, w82_y + 125, beim("pruef", "prüft"), "Bold", 32),
    z("BGBl. seit 1.1.2023 elektronisch: www.recht.bund.de", 110, w82_y + 190, beim("ebgbl", "elektronisch"), "Bold", 32),
    zit("§ 2 Abs. 1 VkBkmG", 150, w82_y + 240, beim("ebgbl", "Verkündungs")),
    z("Inkrafttreten: bestimmter Tag, sonst 14. Tag nach Ausgabe", 110, w82_y + 295, beim("inkr", "Kraft"), size=32),
    zit("Art. 82 Abs. 2 GG", 150, w82_y + 345, beim("inkr", "Artikel")),
    *neinz("Ausfertigung und Verkündung heilen nicht", 195, w82_y + 405, beim("heil", "heilen"), "Bold", 34),
    ficon("tabler", "signature", IX, IU, 170, beim("wl82", "ausgefertigt"), fuell=WEISS, bis="ebgbl"),
    ficon("tabler", "device-laptop", IX, IU, 190, "ebgbl", fuell=WEISS, anim="cut"),
    *fig("KA", FX, FB, FR, [("form1", "ruhig"), ("ebgbl", "froh"), ("heil", "sorge")]),
    schild("Frau Kähler", FX, "form1", KA_F),
]))

# M Ergebnis -------------------------------------------------------------------------------------------------------------------------
KAe = ("KA_redetstaunt", FX, FB, FR)
folie([("erg", "Ergebnis · Gesetz nichtig")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *neinz("ohne wirksame Zustimmung des Bundesrates ausgefertigt", 195, 185, beim("erg", "ohne"), "Bold", 32),
    blk(110, 270, 1040, 134, ROTHELL, beim("erg", "formell"),
        [("Das Gesetz ist formell", "ExtraBold", 36, INK), ("verfassungswidrig und nichtig.", "ExtraBold", 36, INK)]),
    z("so auch beim Zuwanderungsgesetz", 110, 440, beim("erg2", "Zuwanderungsgesetz"), "Bold", 34),
    zit(f"{ZW}: mit Art. 78 GG unvereinbar und nichtig", 110, 495, beim("erg2", "Zuwanderungsgesetz", ende=True)),
    *fig("KA", FX, FB, FR, [("erg", "ruhig"), (beim("erg", "nichtig"), "sorge")], bis="ka2"),
    *redet("KA_redetstaunt", FX, FB, FR, "ka2", "tipp"),
    schild("Frau Kähler", FX, "erg", KA_F),
    blase("sprech", 560, 190, "ka2", 1520, 260, inhalt=["Ein Gesetz im Gesetzblatt,", "und trotzdem nichtig!"],
          textsize=30, figur=KAe),
]))

# N Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Welche Fehler machen nichtig?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nicht jeder Verfahrensfehler macht nichtig", 200, 200, beim("tipp", "Nicht"), "Bold", 36),
    z("nur Geschäftsordnung verletzt: in der Regel nicht", 200, 270, beim("tipp1", "Geschäftsordnung"), size=33),
    z("entscheidend: zugleich das GG verletzt?", 200, 325, beim("tipp1", "zugleich"), size=33),
    blk(200, 405, 900, 76, BLAU, beim("tipp2", "Verfahrensverstoß"), [("Verfahrensverstoß gegen das GG:", "ExtraBold", 34, INK)]),
    z("nichtig nur, wenn evident", 240, 505, beim("tipp2", "evident"), "Bold", 36),
    zit(EV, 240, 560, beim("tipp2", "evident", ende=True)),
    *okz("hier offensichtlich: Art. 51 Abs. 3 Satz 2 GG", 245, 640, beim("tipp3", "offensichtlich"), "Bold", 34),
    z("verlangt einheitliche Stimmen", 245, 695, beim("tipp3", "einheitliche"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema: der Weg des Gesetzes ----------------------------------------------------------------------------------------------
SZ, LH, Y0 = 32, 60, 180
WX = 150
schema = [("s1", 0, "I. Zuständigkeit, Art. 70 ff. GG", "Bold"),
          ("s2", 0, "II. Verfahren", "Bold"),
          ("s21", 1, "1. Initiative, Art. 76 GG", "Regular"),
          ("s22", 1, "2. Beschluss des Bundestages, Art. 77 Abs. 1 Satz 1, 42 Abs. 2 GG", "Regular"),
          ("s23", 1, "3. Beteiligung des Bundesrates: Einspruch oder Zustimmung", "Regular"),
          ("s24", 2, "Vermittlungsausschuss, Art. 77 Abs. 2 GG", "Regular"),
          ("s25", 2, "einheitliche Stimmen, Art. 51 Abs. 3 Satz 2, 52 Abs. 3 GG", "Regular"),
          ("s3", 0, "III. Form, Art. 82 GG", "Bold"),
          ("s31", 1, "Gegenzeichnung, Ausfertigung und Verkündung", "Regular"),
          ("s4", 0, "Ergebnis", "Bold"),
          ("s5", 1, "bei Fehlern: Nichtigkeit?", "Regular")]
els_s = [karte(60, 50, 1800, 900, "sch"),
         titel(glyphen("Klausurschema: der Weg des Gesetzes"), 110, 80, "sch", 46),
         linienzug([(WX, Y0 + 10), (WX, Y0 + (len(schema) - 1) * LH + 30)], "sch", breite=8, farbe=(200, 200, 205, 255))]
for i, (c, ebene, t, s) in enumerate(schema):
    y = Y0 + i * LH
    els_s.append(punkt(WX, y + 20, 14 if ebene == 0 else 9, c, fill=GELB if ebene == 0 else WEISS))
    els_s.append(z(t, 200 + ebene * 60, y, c, s, SZ, rechts=1820))
els_s.append(ficon("tabler", "flag", 1720, Y0 + 9 * LH + 40, 90, "s4", fuell=GRUEN))
folie([("sch", "Klausurschema · Formelle Verfassungsmäßigkeit")], els_s)

# P Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein ", 0), ("Zustimmungsgesetz", "a"), (" kommt nur", 0)]], 750, 310, 46, "merke",
                {"a": beim("merke", "Zustimmungsgesetz")}),
    *markertext([[("zustande, wenn der ", 0), ("Bundesrat zustimmt.", "b")]], 750, 375, 46, beim("merke", "zustande"),
                {"b": beim("merke", "Bundesrat")}),
    *markertext([[("Dafür braucht es die ", 0), ("Mehrheit", "c")]], 750, 510, 46, "m2", {"c": beim("m2", "Mehrheit")}),
    *markertext([[("seiner Stimmen, und jedes Land", 0)]], 750, 575, 46, beim("m2", "seiner"), {}),
    *markertext([[("kann nur ", 0), ("einheitlich", "d"), (" abstimmen.", 0)]], 750, 640, 46, beim("m2", "kann"),
                {"d": beim("m2", "einheitlich")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
