"""Folge 105 · Klagebefugnis § 42 II VwGO: Möglichkeitstheorie und Adressatentheorie – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Gebührenbescheid über 180 € für eine Fällgenehmigung; Freund klagt aus Solidarität mit), Figuren fiktiv.
Szenen laut ../SZENENPLAN.md: A Garten, B Verwaltungsgericht (Klagen, Frage), C Sachverhalt, D Einordnung und 1. Wortlaut
§ 42 II (Wortlautkarte, § 2 I 1 UmwRG), E 2. eigene Rechte, F 3. Möglichkeitstheorie, G 4. Adressatentheorie (Wortlautkarte
Art. 2 I GG), H 5. Dritte, I 6. Zweck/Popularklage und Herr Wilke, J Urteil, K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Papier, als der Gebührenbescheid erscheint). Hilfsfunktionen wie 102 (dort wie 093)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_105/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_105/" in n:
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
F2A, F2B, F2H = 1400, 1720, 420             # zwei Figuren neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
NO_F, WI_F, RI_F = GRUEN, BLAU, LILA        # Farben der Namensschilder
KB = "Klagebefugnis"

# A Fall: der Garten, die Kastanie, der Gebührenbescheid --------------------------------------------------------------------
NOX, WIX, PX = 1180, 1680, 840
NOb = ("NO_redet_r", NOX, BODEN, FH)
WIb = ("WI_redet", WIX, BODEN, FH)
KOMMT = "wilke"
folie([(NULL, "Fall · Der Gebührenbescheid"), (KOMMT, "Fall · Der Freund will mitklagen")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Garten von Frau Nolte", 70, 40, NULL, fill=GELB, size=40)),
    ficon("ph", "tree", 330, BODEN - 2, 380, NULL, fuell=GRUEN, anim="cut"),
    ficon("tabler", "fence", 585, BODEN - 2, 110, NULL, fuell=WEISS, anim="cut"),
    pl("kranke Kastanie", 330, 455, beim("fall", "Kastanie"), fill=WEISS, size=30, anker="m"),
    *fig("NO", NOX, BODEN, FH, [(NULL, "ruhig_r"), (beim("bescheid", "hundertachtzig"), "sorge_r"), ("no1", "aerger_r")],
         bis="no1", erst="cut"),
    *redet("NO_redet_r", NOX, BODEN, FH, "no1", "wi1"),
    *fig("NO", NOX, BODEN, FH, [("wi1", "froh_r")], erst="cut", bis="klage"),
    hart(schild("Frau Nolte", NOX, NULL, NO_F, unten=BODEN, d=0.0)),
    ficon("tabler", "license", PX, 560, 90, beim("erlaubt", "erlaubt"), fuell=WEISS),
    pl("Fällgenehmigung", PX, 600, beim("erlaubt", "erlaubt"), fill=GRUEN, size=28, anker="m"),
    szene(ficon("tabler", "mail-opened", PX, 730, 90, beim("bescheid", "Gebührenbescheid"), fuell=WEISS), "105papier*", 0.8, -0.3),
    pl("Gebührenbescheid: 180 €", PX, 770, beim("bescheid", "hundertachtzig"), fill=ROT, size=28, anker="m"),
    *fig("WI", WIX, BODEN, FH, [(KOMMT, "ruhig")], bis="wi1"),
    *redet("WI_redet", WIX, BODEN, FH, "wi1", "klage"),
    schild("Herr Wilke, ihr Freund", WIX, KOMMT, WI_F, unten=BODEN, d=0.0),
    blase("sprech", 720, 210, "no1", 700, 250, inhalt=["180 € für einen Stempel?", "Dagegen klage ich."], textsize=34,
          figur=NOb, bis="wi1"),
    blase("sprech", 940, 250, "wi1", 1240, 230, inhalt=["Ich klage mit! Ich wohne auch in dieser Stadt,",
                                                       "und solche Gebühren sind einfach ungerecht."], textsize=30,
          figur=WIb, bis="klage"),
])

# B Verwaltungsgericht: die Klagen, die Frage --------------------------------------------------------------------------------
NOX2, WIX2 = 1330, 1700
folie([("klage", "Fall · Die Klagen"), ("frage", "Fall · Sind beide klagebefugt?")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "klage", fill=GELB, size=40),
    ficon(HC, "classical-building", 330, BODEN - 2, 400, "klage", fuell=WEISS),
    ficon("tabler", "file-text", 780, 520, 80, beim("klage", "Anfechtungsklage"), fuell=WEISS),
    pl("Anfechtungsklage von Frau Nolte", 780, 560, beim("klage", "Anfechtungsklage"), fill=GRUEN, size=28, anker="m"),
    pl("Anfechtungsklage von Herrn Wilke", 780, 625, beim("klage", "Anfechtungsklage"), fill=BLAU, size=28, anker="m", d=0.3),
    pl("gegen den Gebührenbescheid: 180 €", 780, 700, beim("klage", "Gebührenbescheid"), fill=WEISS, size=28, anker="m"),
    *fig("NO", NOX2, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Frau Nolte", NOX2, "klage", NO_F, unten=BODEN),
    *fig("WI", WIX2, BODEN, FH, [("klage", "ruhig"), ("frage", "denkt")]),
    schild("Herr Wilke", WIX2, "klage", WI_F, unten=BODEN),
    pl("Sind beide klagebefugt?", 1510, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("§ 42 Abs. 2 VwGO", 1510, 240, beim("frage2", "Paragraf"), fill=WEISS, size=34, anker="m"),
])

# C Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Nolte will die kranke Kastanie in ihrem Garten fällen lassen. Die Stadt erteilt ihr die Fällgenehmigung und "
    "setzt mit Gebührenbescheid an Frau Nolte eine Verwaltungsgebühr von 180 € fest. Frau Nolte hält die Gebühr für zu "
    "hoch.",
    "Ihr Freund Herr Wilke wohnt in derselben Stadt. Er findet solche Gebühren ungerecht und will aus Solidarität "
    "mitklagen. Ein Widerspruchsverfahren ist nach dem Landesrecht nicht vorgesehen. Beide erheben fristgerecht "
    "Anfechtungsklage gegen den Gebührenbescheid.",
], "Sind Frau Nolte und Herr Wilke klagebefugt?")

# D Einordnung und 1. Wortlaut § 42 Abs. 2 VwGO --------------------------------------------------------------------------------
W422 = ("„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage nur zulässig, wenn der Kläger geltend macht, durch den "
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen Rechten verletzt zu sein.“")
Z422 = ["„Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage",
        "nur zulässig, wenn der Kläger geltend macht, durch den",
        "Verwaltungsakt oder seine Ablehnung oder Unterlassung",
        "in seinen Rechten verletzt zu sein.“"]
w422, w422_y = wortlaut(80, 290, 1100, W422, "§ 42 Abs. 2 VwGO", "wl422", size=32, zeilen=Z422,
                        marken=[("Soweit gesetzlich nichts anderes bestimmt ist", beim("wl422", "Soweit")),
                                ("geltend macht", beim("wl422", "geltend")),
                                ("in seinen Rechten verletzt", beim("wl422", "Rechten"))])
folie([("einord", f"{KB} · Platz in der Zulässigkeit"), ("wl422", f"{KB} › 1. Wortlaut, § 42 II VwGO"),
       ("umw", f"{KB} › 1. „soweit gesetzlich nichts anderes …“")], rechts_frei([
    titel(glyphen("Klagebefugnis, § 42 Abs. 2 VwGO"), 110, 60, "einord", 44),
    z("Zulässigkeit: Rechtsweg – Klageart – Klagebefugnis – …", 110, 150, beim("einord", "Zulässigkeit"), size=32),
    pl("ganzes Schema: Video zur Anfechtungsklage", 110, 205, beim("einord", "Schema"), fill=WEISS, size=28),
    *w422,
    z("Etwas anderes bestimmt etwa § 2 Abs. 1 Satz 1 UmwRG:", 110, w422_y + 26, beim("umw", "Umwelt"), "Bold", 32),
    z("anerkannte Umweltvereinigungen klagen gegen bestimmte", 150, w422_y + 78, beim("umw", "Anerkannte"), size=32),
    z("Entscheidungen ohne Verletzung eigener Rechte", 150, w422_y + 126, beim("umw", "ohne"), size=32),
    *fig("NO", F2A, FB, F2H, [("einord", "ruhig"), ("wl422", "denkt"), ("umw", "ruhig")]),
    schild("Frau Nolte", F2A, "einord", NO_F),
    *fig("WI", F2B, FB, F2H, [("einord", "ruhig"), ("wl422", "denkt"), ("umw", "ruhig")]),
    schild("Herr Wilke", F2B, "einord", WI_F),
    ficon("tabler", "scale", (F2A + F2B) // 2, 380, 120, "wl422", fuell=WEISS),
]))

# E 2. Verletzung eigener Rechte ------------------------------------------------------------------------------------------------
folie([("eigen", f"{KB} › 2. Verletzung eigener Rechte")], rechts_frei([
    *tafel("eigen", "2. Eigene Rechte"),
    z("Der Kläger muss eine Verletzung in seinen", 110, 190, beim("eigen", "Kläger"), "Bold", 36),
    z("eigenen Rechten geltend machen.", 150, 245, beim("eigen", "eigenen"), "Bold", 36),
    karte(110, 330, 1040, 130, beim("eigen2", "subjektive"), fill=GELB, rund=18, schatten=0, rand=5),
    z("subjektive Rechte:", 140, 348, beim("eigen2", "subjektive"), "ExtraBold", 36),
    z("Rechte, die dem Kläger selbst zustehen", 140, 400, beim("eigen2", "Rechte"), "Bold", 34),
    z("nur objektiv rechtswidriger Bescheid?", 110, 530, beim("objektiv", "objektiv"), size=36),
    z("genügt nicht", 150, 585, beim("objektiv", "genügt"), "Bold", 36),
    nein(420, 605, beim("objektiv", "genügt"), gr=26),
    *fig("NO", F2A, FB, F2H, [("eigen", "ruhig")]),
    schild("Frau Nolte", F2A, "eigen", NO_F),
    *fig("WI", F2B, FB, F2H, [("eigen", "ruhig"), ("objektiv", "denkt")]),
    schild("Herr Wilke", F2B, "eigen", WI_F),
    ficon("tabler", "user-check", (F2A + F2B) // 2, 380, 110, beim("eigen", "eigenen"), fuell=GRUEN),
]))

# F 3. Möglichkeitstheorie -----------------------------------------------------------------------------------------------------------
folie([("mt", f"{KB} › 3. Möglichkeitstheorie")], rechts_frei([
    *tafel("mt", "3. Möglichkeitstheorie"),
    z("Wie sicher muss die Verletzung sein?", 110, 180, beim("mt", "wie"), "Bold", 36),
    z("Es genügt: Nach dem Klagevorbringen erscheint", 110, 255, beim("mt", "genügt"), size=34),
    z("eine Verletzung möglich.", 150, 305, beim("mt", "möglich", 2), "Bold", 34),
    karte(110, 375, 1040, 180, beim("mt2", "Auszuschließen"), fill=ROT, rund=18, schatten=0, rand=5),
    z("ausgeschlossen nur, wenn offensichtlich", 140, 392, beim("mt2", "Auszuschließen"), "ExtraBold", 34),
    z("und nach keiner Betrachtungsweise subjektive", 140, 444, beim("mt2", "nach"), "Bold", 32),
    z("Rechte des Klägers verletzt sein können", 140, 494, beim("mt2", "Rechte"), "Bold", 32),
    zit("BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 13", 150, 580, beim("mt2", "verletzt")),
    z("Ob er wirklich verletzt ist: erst in der Begründetheit", 110, 660, beim("mt3", "Ob"), size=34),
    zit("§ 113 Abs. 1 Satz 1 VwGO", 150, 712, beim("mt3", "Begründetheit")),
    ficon(HC, "balance-scale", IX, IU, 150, "mt", fuell=WEISS),
    pl("möglich?", IX, 190, beim("mt", "möglich", 2), fill=GELB, size=30, anker="m"),
    *fig("RI", FX, FB, FR, [("mt", "ruhig")]),
    schild("die Richterin", FX, "mt", RI_F),
]))

# G 4. Adressatentheorie, Wortlaut Art. 2 Abs. 1 GG -------------------------------------------------------------------------------------
W2 = ("„Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit, soweit er nicht die Rechte anderer verletzt und "
      "nicht gegen die verfassungsmäßige Ordnung oder das Sittengesetz verstößt.“")
Z2 = ["„Jeder hat das Recht auf die freie Entfaltung seiner",
      "Persönlichkeit, soweit er nicht die Rechte anderer verletzt",
      "und nicht gegen die verfassungsmäßige Ordnung oder das",
      "Sittengesetz verstößt.“"]
w2, w2_y = wortlaut(80, 300, 1100, W2, "Art. 2 Abs. 1 GG", beim("wl2", "Artikel"), size=32, zeilen=Z2,
                    marken=[("freie Entfaltung seiner", beim("wl2", "freie")), ("Persönlichkeit,", beim("wl2", "Persönlichkeit"))])
folie([("adr", f"{KB} › 4. Adressatentheorie, Art. 2 I GG"), ("nolte", f"{KB} › 4. Frau Nolte: klagebefugt")], rechts_frei([
    titel(glyphen("4. Adressatentheorie"), 110, 60, "adr", 44),
    z("Frau Nolte: Adressatin des Gebührenbescheids", 110, 145, beim("adr", "Adressatin"), "Bold", 34),
    pl("Pflicht: 180 € zahlen", 110, 200, beim("adr", "verpflichtet"), fill=ROT, size=28),
    pl("Eingriff in die allgemeine Handlungsfreiheit", 470, 200, beim("wl2", "allgemeine"), fill=GELB, size=28),
    *w2,
    z("Adressat eines belastenden Verwaltungsakts: stets ein", 110, w2_y + 24, beim("stets", "Adressat"), size=32),
    z("staatlicher Freiheitseingriff – allein deshalb klagebefugt", 110, w2_y + 72, beim("stets", "staatlichen"), "Bold", 32),
    zit("BVerwG, Beschl. v. 19.7.2010 – 6 B 20.10, Rn. 16", 150, w2_y + 122, beim("stets", "allein")),
    zit("ebenso BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18", 150, w2_y + 160, beim("stets", "klagebefugt")),
    z("Frau Nolte: klagebefugt", 110, w2_y + 215, beim("nolte", "klagebefugt"), "ExtraBold", 36),
    ok(560, w2_y + 238, beim("nolte", "klagebefugt"), gr=24),
    ficon("tabler", "mail-opened", IX, IU - 40, 100, "adr", fuell=WEISS),
    pl("Gebührenbescheid: 180 €", IX, 230, beim("adr", "Gebührenbescheids"), fill=ROT, size=26, anker="m"),
    *fig("NO", FX, FB, FR, [("adr", "denkt"), ("nolte", "froh")]),
    schild("Frau Nolte", FX, "adr", NO_F),
]))

# H 5. Dritte: Schutznormtheorie ----------------------------------------------------------------------------------------------------
folie([("dritt", f"{KB} › 5. Dritte: Schutznormtheorie")], rechts_frei([
    *tafel("dritt", "5. Dritte"),
    z("Wer nicht Adressat ist, braucht eine Norm,", 110, 185, beim("dritt", "Wer"), "Bold", 34),
    z("die zumindest auch ihn schützt", 150, 238, beim("dritt", "zumindest"), "Bold", 34),
    z("und nicht nur reflexartig seine Interessen berührt", 150, 291, beim("dritt", "reflexartig"), size=34),
    zit("vgl. BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 24", 150, 343, beim("dritt", "berührt")),
    blk(110, 410, 1040, 70, GELB, beim("snt", "Schutznormtheorie"), [("= Schutznormtheorie", "ExtraBold", 36, INK)]),
    z("typisch: der Nachbar gegen eine Baugenehmigung", 110, 540, beim("nachbar", "Nachbar"), size=34),
    pl("Videos: Rücksichtnahmegebot, Drittanfechtung", 110, 605, beim("nachbar", "Videos"), fill=WEISS, size=28),
    ficon("tabler", "home", IX - 90, IU, 110, beim("nachbar", "Nachbar"), fuell=BLAU),
    ficon("tabler", "crane", IX + 90, IU, 110, beim("nachbar", "Baugenehmigung"), fuell=GELB),
    *fig("WI", FX, FB, FR, [("dritt", "denkt")]),
    schild("Herr Wilke", FX, "dritt", WI_F),
]))

# I 6. Zweck: keine Popularklage; Herr Wilke -------------------------------------------------------------------------------------------
folie([("zweck", f"{KB} › 6. Zweck: keine Popularklage"), ("wilke2", f"{KB} › 6. Herr Wilke")], rechts_frei([
    *tafel("zweck", "6. Zweck: keine Popularklage"),
    z("§ 42 Abs. 2 VwGO schließt die Popularklage aus:", 110, 180, beim("zweck", "Paragraf"), "Bold", 34),
    z("niemand bringt fremde Rechte oder das", 150, 235, beim("zweck2", "Niemand"), size=34),
    z("Allgemeininteresse vor Gericht", 150, 285, beim("zweck2", "Allgemeininteresse"), size=34),
    z("Herr Wilke:", 110, 380, beim("wilke2", "Herr"), "ExtraBold", 36),
    z("Der Bescheid richtet sich nicht an ihn", 150, 440, beim("wilke2", "Bescheid"), size=34),
    z("und verpflichtet ihn zu nichts.", 150, 490, beim("wilke2", "verpflichtet"), size=34),
    zit("vgl. BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 14", 150, 540, beim("wilke2", "nichts")),
    z("Eine Norm, die ihn hier schützt: nicht ersichtlich", 150, 600, beim("wilke3", "Norm"), size=34),
    z("selbe Stadt, Gebühr ungerecht: kein eigenes Recht", 150, 655, beim("wilke3", "Dass"), "Bold", 34),
    nein(1110, 675, beim("wilke3", "kein"), gr=24),
    ficon("tabler", "users", IX, IU, 130, "zweck", fuell=WEISS),
    pl("Allgemeininteresse", IX, 200, beim("zweck2", "Allgemeininteresse"), fill=PINK, size=30, anker="m"),
    *fig("WI", FX, FB, FR, [("zweck", "ruhig"), ("wilke2", "denkt"), (beim("wilke3", "kein"), "sorge")]),
    schild("Herr Wilke", FX, "zweck", WI_F),
]))

# J Urteil: Herr Wilke ist nicht klagebefugt -----------------------------------------------------------------------------------------
RIX, WIX3, NOX3 = 760, 1330, 1690
RIb = ("RI_redet_r", RIX, BODEN, FH)
folie([("urteil", "Ergebnis · Klage von Herrn Wilke unzulässig")], [
    linienzug([(60, BODEN), (1860, BODEN)], "urteil", breite=7, farbe=INK),
    pl("Verwaltungsgericht", 70, 40, "urteil", fill=GELB, size=40),
    ficon(HC, "classical-building", 290, BODEN - 2, 340, "urteil", fuell=WEISS),
    *fig("RI", RIX, BODEN, FH, [("urteil", "ruhig_r")], bis="ri1"),
    *redet("RI_redet_r", RIX, BODEN, FH, "ri1", "tipp"),
    schild("die Richterin", RIX, "urteil", RI_F, unten=BODEN),
    *fig("WI", WIX3, BODEN, FH, [("urteil", "ruhig"), (beim("ri1", "unzulässig"), "muede")]),
    schild("Herr Wilke", WIX3, "urteil", WI_F, unten=BODEN),
    *fig("NO", NOX3, BODEN, FH, [("urteil", "ruhig")]),
    schild("Frau Nolte", NOX3, "urteil", NO_F, unten=BODEN),
    blase("sprech", 820, 210, "ri1", 1240, 200, inhalt=["Herr Wilke, Sie sind nicht klagebefugt.",
                                                       "Ihre Klage ist unzulässig."], textsize=32, figur=RIb),
    pl("Herr Wilke: unzulässig", 290, 470, beim("ri1", "unzulässig"), fill=BLAU, size=28, anker="m"),
    nein(500, 472, beim("ri1", "unzulässig"), gr=22),
])

# K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Klagebefugnis in einem Satz"), ("vk", "Klausurtipp · Verpflichtungsklage")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Adressat gegen belastenden Bescheid:", 200, 180, beim("tipp", "Adressat"), "Bold", 34),
    z("zur Klagebefugnis nur ein Satz", 200, 232, beim("tipp", "Satz"), "Bold", 34),
    karte(100, 300, 1080, 250, beim("tipp2", "Etwa"), fill=ZITAT, rund=18, schatten=6, rand=4),
    z("„Als Adressatin eines belastenden Verwaltungsakts", 130, 325, beim("tipp2", "Als"), size=32),
    z("ist Frau Nolte möglicherweise in ihrem Recht aus", 130, 373, beim("tipp2", "ist"), size=32),
    z("Art. 2 Abs. 1 GG verletzt und daher klagebefugt.“", 130, 421, beim("tipp2", "Artikel"), size=32),
    zit("Formulierungsbeispiel (Klausurkonvention)", 130, 485, beim("tipp2", "klagebefugt")),
    blk(110, 590, 1040, 64, GELB, "tipp3", [("Mehr gehört da nicht hin.", "ExtraBold", 34, INK)]),
    z("Verpflichtungsklage: Ist ein Anspruch auf den", 110, 705, beim("vk", "Verpflichtungsklage"), "Bold", 32),
    z("Verwaltungsakt möglich?", 150, 755, beim("vk", "Anspruch"), "Bold", 32),
    pl("Video zur Verpflichtungsklage", 110, 815, beim("vk", "Video"), fill=WEISS, size=28),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Schema --------------------------------------------------------------------------------------------------------------------------
SZ, LH = 40, 105
els_s = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Schema: Klagebefugnis, § 42 Abs. 2 VwGO"), 110, 85, "sch", 46)]
zeilen_s = [
    zz("1. Wortlaut:", "§ 42 Abs. 2 VwGO – „soweit gesetzlich nichts anderes bestimmt ist“", 110, 200, "s1",
       beim("s1", "Paragraf"), size=SZ, rest_stil="Regular", rechts=1820),
    zz("2. Geltendmachen:", "Verletzung in eigenen Rechten", 110, 200 + LH, "s2", beim("s2", "Verletzung"), size=SZ,
       rest_stil="Regular", rechts=1820),
    zz("3. Möglichkeitstheorie:", "nicht offensichtlich ausgeschlossen", 110, 200 + 2 * LH, "s3", beim("s3", "nicht"),
       size=SZ, rest_stil="Regular", rechts=1820),
    zz("4. Adressat eines belastenden VA:", "Art. 2 Abs. 1 GG", 110, 200 + 3 * LH, "s4", beim("s4", "Artikel"), size=SZ,
       rest_stil="Regular", rechts=1820),
    zz("5. Dritte:", "drittschützende Norm (Schutznormtheorie)", 110, 200 + 4 * LH, "s5", beim("s5", "drittschützende"),
       size=SZ, rest_stil="Regular", rechts=1820),
    zz("6. Zweck:", "keine Popularklage", 110, 200 + 5 * LH, "s6", beim("s6", "Popularklage"), size=SZ, rest_stil="Regular",
       rechts=1820),
]
for zl in zeilen_s:
    els_s += zl
folie([("sch", "Schema · Klagebefugnis, § 42 II VwGO")], els_s)

# M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Klagebefugt ist, wer ", 0), ("möglicherweise", "a")]], 750, 320, 46, "merke",
                {"a": beim("merke", "möglicherweise")}),
    *markertext([[("in eigenen Rechten verletzt ist.", 0)]], 750, 385, 46, beim("merke", "in"), {}),
    *markertext([[("Der Adressat eines belastenden", 0)]], 750, 535, 46, "m2", {}),
    *markertext([[("Bescheids ist es ", 0), ("immer", "b"), (".", 0)]], 750, 600, 46, beim("m2", "Bescheids"),
                {"b": beim("m2", "immer")}),
    *markertext([[("Wer nur aus Solidarität klagt, ist es nie.", 0)]], 750, 700, 46, beim("m2", "Wer"), {}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
