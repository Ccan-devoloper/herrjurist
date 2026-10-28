"""Folge 074 · Ermessensfehler: Was darf das Gericht kontrollieren? (§ 114 VwGO) – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Café in der Altstadt, Tische auf dem Gehweg, Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut
../SZENENPLAN.md: A Altstadt (Antrag, Antwort der Stadt), B Verwaltungsgericht (Klage, Frage), C Sachverhalt, D Sondernutzung,
E gebunden oder Ermessen, F Rechtsfolgenseite, G Wortlaut § 40 VwVfG, H Wortlaut § 114 Satz 1 VwGO, I–K die drei
Ermessensfehler, L Reduzierung auf null, M Fall: Ermessensausfall, N Nachschieben (Wortlaut § 114 Satz 2), O Urteil
(Bescheidungsurteil), P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als Herr Hornung den Bescheid bringt). Eigene Hilfsfunktionen wie Folge 069."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_074/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_074/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 069/064/061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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
KA_F, HO_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
E1 = "1. Räumt die Norm Ermessen ein?"
E2 = "2. Ermessensfehler"


def tische(x0, cue, anim="pop", bis=None, breite=86, abstand=96, unten=BODEN, geplant=False):
    """Die 4 Tische vor dem Café: Phosphor „picnic-table“ (weiß gefüllt), nebeneinander auf dem Gehweg.
    geplant=True: halbtransparent – die Tische sind nur beantragt, noch nicht aufgestellt."""
    els = [ficon("ph", "picnic-table", x0 + i * abstand, unten, breite, cue, fuell=WEISS, anim=anim, bis=bis) for i in range(4)]
    if geplant:
        for e in els:
            sp = e.sprite.copy()
            sp.putalpha(sp.getchannel("A").point(lambda v: int(v * 0.4)))
            e.sprite = sp
    return els


# A Fall: das Café in der Altstadt, die Antwort der Stadt -------------------------------------------------------------------
CAX, KAX, HOX = 300, 1110, 1660
KAb = ("KA_redet_r", KAX, BODEN, FH)
HOb = ("HO_redet", HOX, BODEN, FH)
KOMMT = beim("hornung", "Herr")
folie([(NULL, "Fall · Das Café in der Altstadt"), ("hornung", "Fall · Die Antwort der Stadt")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Altstadt, Sommer", 70, 40, NULL, fill=GELB, size=40)),
    ficon("tabler", "building-store", CAX, BODEN - 2, 400, NULL, fuell=GELB, anim="cut"),
    hart(pl("Café", CAX, 420, NULL, fill=WEISS, size=34, anker="m")),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut"),
    *fig("KA", KAX, BODEN, FH, [(NULL, "ruhig_r"), ("antrag", "hofft_r"), (KOMMT, "ruhig_r"),
                               (beim("ho1", "nie"), "sorge_r")], bis="ka1", erst="cut"),
    *redet("KA_redet_r", KAX, BODEN, FH, "ka1", "klage"),
    hart(schild("Frau Kampmann, Café", KAX, NULL, KA_F, unten=BODEN, d=0.0)),
    ficon("tabler", "file-text", 820, 560, 80, "antrag", fuell=WEISS, bis="hornung"),
    pl("Antrag an die Stadt", 820, 600, beim("antrag", "Stadt"), fill=WEISS, size=30, anker="m", bis="hornung"),
    *tische(570, beim("antrag", "Tische"), geplant=True),
    pl("4 Tische auf dem Gehweg", 715, 700, beim("antrag", "Gehweg"), fill=GELB, size=30, anker="m"),
    *fig("HO", HOX, BODEN, FH, [(KOMMT, "ruhig")], bis="ho1"),
    *redet("HO_redet", HOX, BODEN, FH, "ho1", "ka1"),
    peep_voll("HO_ruhig", HOX, BODEN, FH, "ka1", anim="cut"),
    schild("Herr Hornung, Stadt", HOX, KOMMT, HO_F, unten=BODEN, d=0.0),
    szene(ficon("tabler", "file-text", HOX - 140, 700, 90, beim("hornung", "Antwort"), fuell=WEISS), "074brief*", 0.8, -0.25),
    nein(715, 845, beim("ho1", "abgelehnt"), gr=40),
    blase("sprech", 820, 230, "ho1", 1180, 215, inhalt=["Frau Kampmann, Tische auf dem Gehweg?",
                                                      "Das machen wir grundsätzlich nie.",
                                                      "Ihr Antrag ist abgelehnt."], textsize=30, figur=HOb, bis="ka1"),
    blase("sprech", 760, 200, "ka1", 900, 215, inhalt=["Nie? Sie haben sich meinen Gehweg", "doch gar nicht angesehen!"],
          textsize=30, figur=KAb, bis="klage"),
])

# B Die Klage und die Frage --------------------------------------------------------------------------------------------------
GERICHT = beim("klage", "Verwaltungsgericht")
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Was darf das Gericht kontrollieren?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 520, BODEN - 2, 420, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 960, 640, 100, beim("klage", "klagt"), fuell=WEISS),
    pl("Klage", 960, 660, beim("klage", "klagt"), fill=GRUEN, size=30, anker="m"),
    *fig("KA", 1160, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Frau Kampmann", 1160, "klage", KA_F, unten=BODEN),
    pl("Was darf das Gericht hier kontrollieren?", 1290, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Und hat die Klage Erfolg?", 1290, 240, "frage2", fill=WEISS, size=36, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Kampmann betreibt ein kleines Café in der Altstadt einer Stadt in Nordrhein-Westfalen. Sie beantragt bei der "
    "Stadt eine Sondernutzungserlaubnis: Von Mai bis September will sie 4 Tische auf den breiten Gehweg vor dem Café "
    "stellen. Herr Hornung von der Stadt übergibt den schriftlichen Bescheid. Die Stadt lehnt ab, einzige Begründung: "
    "„Das machen wir grundsätzlich nie.“ Frau Kampmann erhebt rechtzeitig Klage beim Verwaltungsgericht und verlangt die "
    "Erlaubnis. Im Prozess trägt die Stadt erstmals vor, Fußgänger bräuchten dort Platz.",
], "Hat die Klage Erfolg?")

# D Sondernutzung, § 18 StrWG NRW ------------------------------------------------------------------------------------------
folie([("norm", "Grundlage · Sondernutzung, § 18 StrWG NRW")], rechts_frei([
    *tafel("norm", "Sondernutzung, § 18 StrWG NRW"),
    z("Tische auf dem Gehweg: Nutzung über den", 110, 190, beim("norm", "Tische"), size=34),
    z("Gemeingebrauch hinaus", 110, 243, beim("norm", "Gemeingebrauch"), size=34),
    blk(110, 310, 1040, 76, BLAU, beim("norm", "Sondernutzung"), [("= Sondernutzung", "ExtraBold", 36, INK)]),
    z("braucht eine Erlaubnis", 110, 430, beim("norm2", "Erlaubnis"), "Bold", 36),
    zit("§ 18 Abs. 1 Satz 1 und 2 StrWG NRW", 150, 485, beim("norm2", "Paragraf")),
    z("Entscheidung der Stadt: nach Ermessen", 110, 560, beim("norm3", "Ermessen"), "Bold", 36),
    zit("OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 29, 58", 150, 615, beim("norm3", "Ermessen")),
    pl("In deinem Land: andere Nummer", 110, 690, "land", fill=PINK, size=32),
    ficon("tabler", "building-store", IX, IU, 150, "norm", fuell=GELB),
    pl("Café", IX, 180, "norm", fill=WEISS, size=28, anker="m"),
    *fig("KA", FX, FB, FR, [("norm", "denkt"), ("norm3", "ruhig")]),
    schild("Frau Kampmann", FX, "norm", KA_F),
]))

# E Gebunden oder Ermessen ---------------------------------------------------------------------------------------------------
folie([("geb", f"{E1} › gebunden oder Ermessen")], rechts_frei([
    *tafel("geb", "Gebunden oder Ermessen?"),
    z("„muss“ oder „ist zu“: gebunden", 110, 190, beim("muss", "muss"), "Bold", 36),
    z("Tatbestand erfüllt: Rechtsfolge zwingend", 150, 245, beim("muss", "Tatbestand"), size=34),
    z("„kann“: Ermessen", 110, 335, beim("kann", "kann"), "Bold", 36),
    z("„soll“: im Regelfall gebunden,", 110, 425, beim("soll", "Soll"), "Bold", 36),
    z("Ermessen nur im atypischen Fall", 150, 480, beim("soll", "atypischen"), size=34),
    zit("BVerwG, Beschl. v. 3.12.2009 – 9 B 79.09, Rn. 2", 150, 532, beim("soll", "Fall")),
    ficon("tabler", "scale", IX, IU, 140, "geb", fuell=WEISS),
    *fig("HO", FX, FB, FR, [("geb", "ruhig"), ("soll", "denkt")]),
    schild("Herr Hornung, Stadt", FX, "geb", HO_F),
]))

# F Rechtsfolgenseite, Entschließungs- und Auswahlermessen, Beurteilungsspielraum -------------------------------------------
folie([("rfs", f"{E1} › Rechtsfolgenseite")], rechts_frei([
    *tafel("rfs", "Ermessen: Rechtsfolgenseite"),
    blk(110, 190, 1040, 76, GELB, beim("ent", "Entschließungsermessen"), [("Entschließungsermessen: ob", "ExtraBold", 36, INK)]),
    blk(110, 290, 1040, 76, GRUEN, beim("aus", "Auswahlermessen"), [("Auswahlermessen: wie", "ExtraBold", 36, INK)]),
    z("Tatbestand: unbestimmte Rechtsbegriffe", 110, 420, beim("bsr", "Unbestimmte"), "Bold", 34),
    z("prüft das Gericht grundsätzlich voll", 150, 473, beim("bsr", "voll"), size=34),
    z("Beurteilungsspielraum: seltene Ausnahme", 150, 535, beim("bsr", "Beurteilungsspielraum"), size=34),
    zit("BVerwG, Beschl. v. 8.11.2016 – 3 B 11.16, Rn. 8", 150, 588, beim("bsr", "Ausnahme")),
    *tische(IX - 126, "rfs", breite=72, abstand=84, unten=IU),
    pl("ob?", IX - 70, 250, beim("ent", "ob"), fill=GELB, size=30, anker="m"),
    pl("wie?", IX + 70, 250, beim("aus", "wie"), fill=GRUEN, size=30, anker="m"),
    *fig("KA", FX, FB, FR, [("rfs", "denkt")]),
    schild("Frau Kampmann", FX, "rfs", KA_F),
]))

# G Bindung der Behörde, Wortlaut § 40 VwVfG ---------------------------------------------------------------------------------
W40 = ("„Ist die Behörde ermächtigt, nach ihrem Ermessen zu handeln, hat sie ihr Ermessen entsprechend dem Zweck der "
       "Ermächtigung auszuüben und die gesetzlichen Grenzen des Ermessens einzuhalten.“")
Z40 = ["„Ist die Behörde ermächtigt, nach ihrem Ermessen zu handeln,",
       "hat sie ihr Ermessen entsprechend dem Zweck der Ermächtigung",
       "auszuüben und die gesetzlichen Grenzen des Ermessens",
       "einzuhalten.“"]
w40, w40_y = wortlaut(80, 175, 1100, W40, "§ 40 VwVfG", "wl40", size=34, zeilen=Z40,
                      marken=[("entsprechend dem Zweck der Ermächtigung", beim("wl40", "entsprechend")),
                              ("die gesetzlichen Grenzen des Ermessens", beim("grenz", "gesetzlichen"))])
folie([("wl40", f"{E1} › Bindung, § 40 VwVfG")], rechts_frei([
    titel(glyphen("Wie die Behörde ihr Ermessen ausübt"), 110, 75, "wl40", 44),
    *w40,
    z("für die Stadt: § 40 VwVfG NRW, gleichlautend", 110, w40_y + 40, beim("nrw40", "Stadt"), "Bold", 34),
    ficon("tabler", "building", IX, IU, 140, "wl40", fuell=WEISS),
    pl("Stadt", IX, 190, beim("nrw40", "Stadt"), fill=GRUEN, size=30, anker="m"),
    *fig("HO", FX, FB, FR, [("wl40", "ruhig")]),
    schild("Herr Hornung, Stadt", FX, "wl40", HO_F),
]))

# H Gerichtliche Kontrolle, Wortlaut § 114 Satz 1 VwGO ------------------------------------------------------------------------
W114 = ("„Soweit die Verwaltungsbehörde ermächtigt ist, nach ihrem Ermessen zu handeln, prüft das Gericht auch, ob der "
        "Verwaltungsakt oder die Ablehnung oder Unterlassung des Verwaltungsakts rechtswidrig ist, weil die gesetzlichen "
        "Grenzen des Ermessens überschritten sind oder von dem Ermessen in einer dem Zweck der Ermächtigung nicht "
        "entsprechenden Weise Gebrauch gemacht ist.“")
Z114 = ["„Soweit die Verwaltungsbehörde ermächtigt ist, nach ihrem",
        "Ermessen zu handeln, prüft das Gericht auch, ob der",
        "Verwaltungsakt oder die Ablehnung oder Unterlassung des",
        "Verwaltungsakts rechtswidrig ist, weil die gesetzlichen",
        "Grenzen des Ermessens überschritten sind oder von dem",
        "Ermessen in einer dem Zweck der Ermächtigung nicht",
        "entsprechenden Weise Gebrauch gemacht ist.“"]
w114, w114_y = wortlaut(80, 150, 1100, W114, "§ 114 Satz 1 VwGO", "wl114", size=32, zeilen=Z114,
                        marken=[("Grenzen des Ermessens überschritten", beim("wl114", "Grenzen")),
                                ("dem Zweck der Ermächtigung nicht", beim("zweck", "Zweck"))])
folie([("wl114", f"{E2} › Kontrolle, § 114 Satz 1 VwGO")], rechts_frei([
    titel(glyphen("Was das Gericht prüft"), 110, 70, "wl114", 44),
    *w114,
    blk(110, w114_y + 30, 1040, 76, GELB, beim("nurrf", "Rechtsfehler"), [("Das Gericht prüft nur Rechtsfehler.", "ExtraBold", 36, INK)]),
    z("nicht: Wäre eine andere Lösung zweckmäßiger?", 110, w114_y + 135, beim("nicht", "Lösung"), size=34),
    z("kein eigenes Ermessen an Stelle der Behörde", 110, w114_y + 190, beim("nicht", "setzt"), "Bold", 34),
    ficon(HC, "classical-building", IX, IU, 150, "wl114", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("wl114", "ruhig")]),
    schild("die Richterin", FX, "wl114", RI_F),
]))

# I 1. Ermessensnichtgebrauch --------------------------------------------------------------------------------------------------
folie([("drei", f"{E2} › a) Ermessensnichtgebrauch")], rechts_frei([
    *tafel("drei", "Drei Ermessensfehler"),
    blk(110, 180, 1040, 76, ROT, beim("f1", "Ermessensnichtgebrauch"), [("a) Ermessensnichtgebrauch", "ExtraBold", 36, INK)]),
    z("auch: Ermessensausfall", 150, 280, beim("f1", "Ermessensausfall"), "Bold", 34),
    z("Behörde übt ihr Ermessen gar nicht aus,", 150, 345, beim("f1", "übt"), size=34),
    z("etwa weil sie sich für gebunden hält", 150, 398, beim("f1", "gebunden"), size=34),
    zit("vgl. BVerwG, Urt. v. 5.9.2006 – 1 C 20.05, Rn. 17–19", 150, 450, beim("f1", "hält")),
    z("„Das machen wir grundsätzlich nie.“", 110, 540, beim("f1b", "Das"), "Bold", 38),
    z("pauschal abgelehnt: Einzelfall nicht angesehen", 150, 605, beim("f1b", "pauschal"), size=34),
    nein(1110, 625, beim("f1b", "Einzelfall"), gr=22),
    ficon("tabler", "eye-off", IX, IU, 130, beim("f1b", "schaut"), fuell=WEISS),
    pl("Einzelfall", IX, 200, beim("f1b", "Einzelfall"), fill=WEISS, size=28, anker="m"),
    *fig("HO", FX, FB, FR, [("drei", "ruhig"), ("f1b", "denkt")]),
    schild("Herr Hornung, Stadt", FX, "drei", HO_F),
]))

# J 2. Ermessensfehlgebrauch ---------------------------------------------------------------------------------------------------
folie([("f2", f"{E2} › b) Ermessensfehlgebrauch")], rechts_frei([
    *tafel("f2", "Drei Ermessensfehler"),
    blk(110, 180, 1040, 76, ROT, beim("f2", "Ermessensfehlgebrauch"), [("b) Ermessensfehlgebrauch", "ExtraBold", 36, INK)]),
    z("sachfremde Erwägungen", 150, 280, beim("f2", "sachfremden"), "Bold", 34),
    z("oder Wichtiges weggelassen: Ermessensdefizit", 150, 335, beim("defizit", "lässt"), size=34),
    z("Sondernutzung: nur Gründe mit Bezug zur Straße,", 110, 420, beim("f2b", "Sondernutzung"), "Bold", 34),
    z("etwa Sicherheit und Leichtigkeit des Verkehrs,", 150, 475, beim("f2b", "Sicherheit"), size=34),
    z("Stadtbild", 150, 528, beim("f2b", "Stadtbild"), size=34),
    zit("OVG NRW, Beschl. v. 1.7.2014 – 11 A 1081/12, Rn. 9, 11", 150, 580, beim("f2b", "Stadtbild")),
    z("Konkurrenzschutz für den Wirt nebenan: sachfremd", 150, 660, beim("f2c", "Konkurrenz"), size=34),
    nein(115, 683, beim("f2c", "sachfremd"), gr=20),
    ficon("tabler", "building-store", IX, IU, 140, beim("f2c", "Wirt"), fuell=BLAU),
    pl("Wirt nebenan", IX, 200, beim("f2c", "Wirt"), fill=WEISS, size=28, anker="m"),
    *fig("KA", FX, FB, FR, [("f2", "denkt"), ("f2c", "aerger")]),
    schild("Frau Kampmann", FX, "f2", KA_F),
]))

# K 3. Ermessensüberschreitung -------------------------------------------------------------------------------------------------
folie([("f3", f"{E2} › c) Ermessensüberschreitung")], rechts_frei([
    *tafel("f3", "Drei Ermessensfehler"),
    blk(110, 180, 1040, 76, ROT, beim("f3", "Ermessensüberschreitung"), [("c) Ermessensüberschreitung", "ExtraBold", 36, INK)]),
    z("Rechtsfolge, die das Gesetz nicht vorsieht", 150, 280, beim("f3", "Rechtsfolge"), "Bold", 34),
    z("etwa: Erlaubnis für immer", 150, 345, beim("f3b", "Erlaubnis"), size=34),
    z("erlaubt ist sie nur auf Zeit oder auf Widerruf", 150, 398, beim("f3b", "Zeit"), size=34),
    zit("§ 18 Abs. 2 Satz 1 StrWG NRW", 150, 450, beim("f3b", "Widerruf")),
    z("Verstoß gegen Grundrechte, Verhältnismäßigkeit", 150, 525, beim("f3c", "Grundrechte"), "Bold", 34),
    z("genügt eine Auflage (Durchgang frei halten),", 150, 590, beim("f3c", "Auflage"), size=34),
    z("kann eine Ablehnung unverhältnismäßig sein", 150, 643, beim("f3c", "Ablehnung"), size=34),
    zit("Auflagen: § 18 Abs. 2 Satz 2 StrWG NRW", 150, 695, beim("f3c", "unverhältnismäßig")),
    ficon("tabler", "infinity", IX, IU, 140, beim("f3b", "immer"), fuell=WEISS, bis="f3c"),
    pl("für immer?", IX, 230, beim("f3b", "immer"), fill=WEISS, size=28, anker="m", bis="f3c"),
    bis_(nein(IX, 340, beim("f3b", "Widerruf"), gr=34), "f3c"),
    ficon("tabler", "walk", IX, IU, 120, beim("f3c", "Durchgang"), fuell=WEISS),
    pl("Durchgang frei", IX, 230, beim("f3c", "Durchgang"), fill=GRUEN, size=28, anker="m"),
    *fig("HO", FX, FB, FR, [("f3", "ruhig"), ("f3c", "denkt")]),
    schild("Herr Hornung, Stadt", FX, "f3", HO_F),
]))

# L Ermessensreduzierung auf null --------------------------------------------------------------------------------------------
folie([("null", "3. Ermessensreduzierung auf null")], rechts_frei([
    *tafel("null", "Ermessensreduzierung auf null"),
    z("nur noch eine Entscheidung rechtmäßig", 110, 190, beim("null", "eine"), "Bold", 36),
    z("das Gericht kann die Behörde direkt verpflichten", 110, 270, beim("null2", "verpflichten"), size=34),
    zit("BVerwG, Beschl. v. 23.1.2014 – 1 B 16.13, Rn. 4; § 113 Abs. 5 Satz 1 VwGO", 150, 323, beim("null2", "verpflichten")),
    ficon(HC, "balance-scale", IX, IU, 150, "null", fuell=WEISS),
    *fig("RI", FX, FB, FR, [("null", "ruhig")]),
    schild("die Richterin", FX, "null", RI_F),
]))

# M Im Fall: Ermessensausfall, Begründung § 39 Abs. 1 Satz 3 VwVfG ------------------------------------------------------------
folie([("zurueck", f"{E2} › im Fall: Ermessensausfall")], rechts_frei([
    *tafel("zurueck", "Der Fall: Frau Kampmann"),
    z("Stadt: nur „grundsätzlich nie“", 110, 190, beim("ausfall", "grundsätzlich"), "Bold", 36),
    z("Gehweg, 4 Tische, Platz für Fußgänger:", 150, 255, beim("ausfall", "Gehweg"), size=34),
    z("nicht befasst", 150, 308, beim("ausfall", "befasst"), size=34),
    blk(110, 375, 1040, 76, ROT, beim("ausfall2", "Ermessensausfall"), [("Ermessensausfall: Ablehnung rechtswidrig", "ExtraBold", 34, INK)]),
    z("Begründung, § 39 Abs. 1 Satz 3 VwVfG:", 110, 500, beim("begr", "Paragraf"), "Bold", 34),
    z("soll die Gesichtspunkte des Ermessens", 150, 553, beim("begr", "Gesichtspunkte"), size=34),
    z("erkennen lassen", 150, 606, beim("begr", "erkennen"), size=34),
    zit("VwVfG NRW gleichlautend", 150, 658, beim("begr", "ausgegangen")),
    ficon("tabler", "file-text", IX, IU, 120, "zurueck", fuell=WEISS),
    pl("„grundsätzlich nie“", IX, 190, beim("ausfall", "grundsätzlich"), fill=ROT, size=28, anker="m"),
    *fig("KA", FX, FB, FR, [("zurueck", "ruhig"), ("ausfall2", "hofft")]),
    schild("Frau Kampmann", FX, "zurueck", KA_F),
]))

# N Nachschieben, Wortlaut § 114 Satz 2 VwGO ------------------------------------------------------------------------------------
W1142 = "„Die Verwaltungsbehörde kann ihre Ermessenserwägungen hinsichtlich des Verwaltungsaktes auch noch im verwaltungsgerichtlichen Verfahren ergänzen.“"
Z1142 = ["„Die Verwaltungsbehörde kann ihre Ermessenserwägungen",
         "hinsichtlich des Verwaltungsaktes auch noch im",
         "verwaltungsgerichtlichen Verfahren ergänzen.“"]
w1142, w1142_y = wortlaut(80, 245, 1100, W1142, "§ 114 Satz 2 VwGO", "wl1142", size=34, zeilen=Z1142,
                          marken=[("ergänzen.", beim("wl1142", "ergänzen"))])
folie([("prozess", "4. Nachschieben, § 114 Satz 2 VwGO")], rechts_frei([
    titel(glyphen("Nachschieben im Prozess"), 110, 70, "prozess", 44),
    z("Stadt im Prozess: Fußgänger bräuchten dort Platz", 110, 160, beim("prozess", "erstmals"), "Bold", 34),
    *w1142,
    z("ergänzen: vorhandene Erwägungen vervollständigen", 110, w1142_y + 35, beim("ergaenzen", "vorhandene"), size=34),
    blk(110, w1142_y + 105, 1040, 76, ROT, beim("heilung", "Ermessensausfall"), [("Ermessensausfall: nicht heilbar", "ExtraBold", 36, INK)]),
    z("von Anfang an Ermessen: im Prozess", 110, w1142_y + 210, beim("heilung", "Anfang"), size=34),
    z("nicht erstmals ausüben", 110, w1142_y + 263, beim("heilung", "erstmals"), "Bold", 34),
    zit("BVerwG, Urt. v. 24.2.2021 – 8 C 25.19, Rn. 13; Urt. v. 13.12.2011 – 1 C 14.10, Rn. 9", 110, w1142_y + 318,
        beim("heilung", "ausüben")),
    ficon("tabler", "walk", IX, IU, 120, beim("prozess", "Fußgänger"), fuell=WEISS),
    pl("Fußgänger", IX, 200, beim("prozess", "Fußgänger"), fill=WEISS, size=28, anker="m"),
    nein(IX + 80, IU - 40, beim("heilung", "heilen"), gr=30),
    *fig("HO", FX, FB, FR, [("prozess", "ruhig"), ("heilung", "denkt")]),
    schild("Herr Hornung, Stadt", FX, "prozess", HO_F),
]))

# O Das Urteil: Bescheidungsurteil ------------------------------------------------------------------------------------------------
RIX, KAX2 = 1420, 600
RIb = ("RI_redet", RIX, BODEN, FH)
folie([("vk", "5. Folge › Bescheidungsurteil, § 113 V 2 VwGO"), ("urteil", "Ergebnis · Das Urteil")], [
    linienzug([(60, BODEN), (1860, BODEN)], "vk", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "vk", fill=GELB, size=40),
    ficon(HC, "balance-scale", 1010, 700, 150, "vk", fuell=WEISS),
    pl("Verpflichtungsklage, § 42 Abs. 1 Alt. 2 VwGO", 70, 140, beim("vk", "Verpflichtungsklage"), fill=WEISS, size=30, bis="ri1"),
    pl("nicht auf null, nicht spruchreif", 70, 215, beim("spruch", "spruchreif"), fill=ROT, size=30, bis="ri1"),
    pl("Bescheidungsurteil, § 113 Abs. 5 Satz 2 VwGO", 70, 290, beim("bu", "Bescheidungsurteil"), fill=GRUEN, size=30, bis="ri1"),
    pl("Mehr dazu: Video Klagearten", 70, 365, beim("verweis", "Video"), fill=WEISS, size=28, bis="ri1"),
    *fig("KA", KAX2, BODEN, FH, [("vk", "ruhig_r"), ("spruch", "denkt_r"), ("teil", "froh_r")]),
    schild("Frau Kampmann", KAX2, "vk", KA_F, unten=BODEN),
    *fig("RI", RIX, BODEN, FH, [("vk", "ruhig")], bis="ri1"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "teil"),
    peep_voll("RI_ruhig", RIX, BODEN, FH, "teil", anim="cut"),
    schild("die Richterin", RIX, "vk", RI_F, unten=BODEN),
    blase("sprech", 900, 260, "ri1", 960, 215, inhalt=["Der Bescheid wird aufgehoben. Die Stadt muss",
                                                     "unter Beachtung der Rechtsauffassung des",
                                                     "Gerichts neu entscheiden. Im Übrigen wird",
                                                     "die Klage abgewiesen."], textsize=30, figur=RIb, bis="teil"),
    pl("Teilerfolg: neue, fehlerfreie Entscheidung", 70, 140, beim("teil", "Teilerfolg"), fill=GRUEN, size=30),
    pl("dann: Platz für Fußgänger abwägen", 70, 215, beim("neu", "Platz"), fill=WEISS, size=30),
])

# P Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Ermessen bei der Rechtsfolge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Ermessen in der Begründetheit prüfen:", 200, 200, beim("tipp", "Begründetheit"), "Bold", 36),
    z("bei der Rechtsfolge, erst wenn der Tatbestand steht", 200, 255, beim("tipp", "Rechtsfolge"), size=34),
    z("Fehler genau benennen:", 200, 350, beim("tipp1", "Benenne"), "Bold", 36),
    z("Nichtgebrauch, Fehlgebrauch oder Überschreitung", 200, 405, beim("tipp1", "Nichtgebrauch"), size=34),
    z("fehlt jede Ermessenserwägung:", 200, 500, beim("tipp2", "fehlt"), "Bold", 36),
    z("kein Nachschieben", 200, 555, beim("tipp2", "Nachschieben"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# Q Klausurschema --------------------------------------------------------------------------------------------------------------
SZ, LH = 36, 70
X0 = 130
zeilen_s = [("s1", "1. Räumt die Norm Ermessen ein? (kann, soll)", "Bold", 0),
            ("s2", "2. Ermessensfehler, § 114 Satz 1 VwGO?", "Bold", 0),
            ("s3", "a) Ermessensnichtgebrauch", "Regular", 1),
            ("s4", "b) Ermessensfehlgebrauch", "Regular", 1),
            ("s5", "c) Ermessensüberschreitung", "Regular", 1),
            ("s6", "3. Ermessensreduzierung auf null?", "Bold", 0),
            ("s7", "4. Erwägungen zulässig ergänzt, § 114 Satz 2 VwGO?", "Bold", 0),
            ("s8", "5. Folge: Aufhebung, Bescheidung oder Verpflichtung", "Bold", 0)]
els_t = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Klausurschema: Ermessensentscheidung"), 110, 85, "sch", 46)]
for i, (c, t, s, ein) in enumerate(zeilen_s):
    els_t.append(z(t, X0 + 60 * ein, 200 + i * LH, c, s, SZ, rechts=1820))
folie([("sch", "Klausurschema · Ermessensentscheidung")], els_t)

# R Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Beim Ermessen prüft das Gericht ", 0)]], 750, 320, 46, "merke", {}),
    *markertext([[("nur ", 0), ("Rechtsfehler,", "a")]], 750, 385, 46, beim("merke", "nur"), {"a": beim("merke", "Rechtsfehler")}),
    *markertext([[("nicht die Zweckmäßigkeit.", 0)]], 750, 450, 46, beim("merke", "nicht"), {}),
    *markertext([[("Wer sein Ermessen ", 0), ("nie ausgeübt", "b"), (" hat,", 0)]], 750, 600, 46, beim("m2", "wer"),
                {"b": beim("m2", "nie")}),
    *markertext([[("kann im Prozess ", 0), ("nichts ergänzen.", "c")]], 750, 665, 46, beim("m2", "kann"),
                {"c": beim("m2", "ergänzen")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
