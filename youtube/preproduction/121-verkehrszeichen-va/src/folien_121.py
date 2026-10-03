"""Folge 121 · Verkehrszeichen als Verwaltungsakt: Kannst du ein Schild anfechten? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Das neue Schild (Frau
Wittmann, Nachbarin Frau Wolter), B Der Anruf bei der Stadt (Herr Buchholz, Straßenverkehrsbehörde), C Frage, D Sachverhalt,
E 1. Rechtsnatur (Wortlaut § 35 S. 2 VwVfG), F 2. Bekanntgabe und Wirksamkeit, G 3. Zulässigkeit: Rechtsweg, Klageart,
Klagebefugnis, H Vorverfahren, Frist, Klagegegner, I keine aufschiebende Wirkung, J 4. Begründetheit: Rechtsgrundlage
(Wortlaut § 45 I 1 StVO), formell, K § 45 IX StVO (Wortlaut S. 1 und S. 3), L zwingend erforderlich und Ermessen,
M Subsumtion und Ergebnis, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Zeichen 283 (absolutes Haltverbot) als stilisierte, korrekte Darstellung: blauer Grund, roter Rand, rotes Kreuz (Paletten-
farben Blau und Dunkelrot, Tuschekontur), Mast als Tuschelinie – geometrisch wie karte()/linienzug(), keine Bilddatei.
Geräusche nur bei sichtbarer Handlung: Haustür, als Frau Wittmann aus dem Haus kommt (Szene A)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_121/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
ZARTGRUEN = (236, 248, 236, 255)
ZARTBLAU = (236, 243, 253, 255)
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
        if n.startswith(("bild:", "ficon:", "zeichen283")):
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


# --- Eigene Hilfsfunktion (wie Folge 064/061): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
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


_Z283 = {}
def z283_bild(d):
    """Zeichen 283 (absolutes Haltverbot), stilisiert: blauer Grund, roter Rand, rotes Kreuz, Tuschekontur."""
    if d not in _Z283:
        s = 3; D = d * s
        im = Image.new("RGBA", (D + 4 * s, D + 4 * s)); dr = ImageDraw.Draw(im)
        o = 2 * s
        dr.ellipse((o, o, o + D, o + D), fill=INK)                                  # Tuschekontur
        k = int(D * 0.025)
        dr.ellipse((o + k, o + k, o + D - k, o + D - k), fill=DROT)                 # roter Rand
        r = int(D * 0.13)
        innen = (o + r, o + r, o + D - r, o + D - r)
        blau = Image.new("RGBA", im.size); ImageDraw.Draw(blau).ellipse(innen, fill=BLAU)
        maske = Image.new("L", im.size, 0); ImageDraw.Draw(maske).ellipse(innen, fill=255)
        kreuz = Image.new("RGBA", im.size); kd = ImageDraw.Draw(kreuz)
        b = int(D * 0.13); c0, c1 = o, o + D
        kd.line([(c0, c0), (c1, c1)], fill=DROT, width=b); kd.line([(c0, c1), (c1, c0)], fill=DROT, width=b)
        blau.alpha_composite(Image.composite(kreuz, Image.new("RGBA", im.size), maske))
        im.alpha_composite(Image.composite(blau, Image.new("RGBA", im.size), maske))
        _Z283[d] = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return _Z283[d]


def zeichen283(cx, cue, boden=None, d=170, mast=True, oben=None, anim="pop", bis=None):
    """Verkehrsschild Zeichen 283 am Mast (Tuschelinie) oder allein (mast=False, oben = Oberkante)."""
    boden = boden or BODEN
    im = z283_bild(d)
    y = oben if oben is not None else boden - 560
    els = []
    if mast:
        els.append(bis_(linienzug([(cx, y + d // 2), (cx, boden)], cue, breite=10, farbe=INK), bis))
        els[-1].anim = "cut" if anim == "cut" else "fade"
    els.append(El(im, cx - im.width / 2, y, cue, anim, 0.0, bis, name="zeichen283"))
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WI_F, BU_F, WO_F = LILA, BLAU, GRUEN        # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270

# A Fall: Das neue Schild ---------------------------------------------------------------------------------------------------
WIX, WOX, SX, AX, HX = 1240, 400, 820, 700, 1600
WIb = ("WI_redet", WIX, BODEN, FH)
WOb = ("WO_redet_r", WOX, BODEN, FH)
TUER = beim("haus", "Frau")
folie([(NULL, "Fall · Das neue Schild")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Ein Morgen in Nordrhein-Westfalen", 1150, 40, NULL, fill=GELB, size=38)),
    hart(ficon("tabler", "home", HX, BODEN, 470, NULL, fuell=GELB)),
    szene(fig("WI", WIX, BODEN, FH, [(TUER, "ruhig"), ("schild", "sorge")], bis="wi1")[0], "121tuer*", 0.8, -0.15),
    *fig("WI", WIX, BODEN, FH, [("schild", "sorge")], bis="wi1", erst="cut"),
    *redet("WI_redet", WIX, BODEN, FH, "wi1", "wolter"),
    *fig("WI", WIX, BODEN, FH, [("wolter", "denkt")], bis="amt", erst="cut"),
    schild("Frau Wittmann", WIX, TUER, WI_F, unten=BODEN, d=0.0),
    pl("seit 20 Jahren hier", WIX, 330, beim("haus", "zwanzig"), fill=WEISS, size=30, anker="m", bis="wi1"),
    ficon("tabler", "car", AX, BODEN, 330, beim("haus", "Auto"), fuell=PINK, bis="schild"),
    pl("immer direkt vor dem Haus", AX, 600, beim("haus", "parkt"), fill=WEISS, size=30, anker="m", bis="schild"),
    *zeichen283(SX, "schild"),
    pl("heute: neues Schild", SX, 560, beim("schild", "neues"), fill=WEISS, size=30, anker="m"),
    pl("absolutes Haltverbot", SX, 630, beim("schild", "absolutes"), fill=ROT, size=30, anker="m"),
    blase("sprech", 560, 200, "wi1", 1300, 220, inhalt=["Seit wann steht", "das denn hier?"], textsize=34, figur=WIb,
          bis="wolter"),
    *fig("WO", WOX, BODEN, FH, [("wolter", "ruhig_r")], bis="wo1"),
    *redet("WO_redet_r", WOX, BODEN, FH, "wo1", "amt"),
    schild("Frau Wolter, Nachbarin", WOX, "wolter", WO_F, unten=BODEN),
    blase("sprech", 760, 240, "wo1", 520, 190, inhalt=["Seit gestern Abend. Jetzt darf", "hier keiner mehr halten,",
                                                      "nicht mal zum Ausladen."], textsize=31, figur=WOb),
])

# B Fall: Der Anruf bei der Stadt ---------------------------------------------------------------------------------------------
WBX, BUX = 560, 1330
WBb = ("WI_aerger_redet_r", WBX, BODEN, FH)
BUb = ("BU_redet", BUX, BODEN, FH)
folie([("amt", "Fall · Der Anruf bei der Stadt")], [
    linienzug([(60, BODEN), (1860, BODEN)], "amt", breite=7, farbe=INK),
    linienzug([(960, 150), (960, BODEN - 10)], "amt", breite=5, farbe=INK),
    pl("Anruf bei der Stadt", 70, 40, "amt", fill=GELB, size=38),
    *fig("WI", WBX, BODEN, FH, [("amt", "entschl_r")], bis="wi2"),
    *redet("WI_aerger_redet_r", WBX, BODEN, FH, "wi2", "bu2"),
    *fig("WI", WBX, BODEN, FH, [("bu2", "aerger_r")], erst="cut"),
    schild("Frau Wittmann", WBX, "amt", WI_F, unten=BODEN, d=0.0),
    ficon(HC, "mobile-phone", WBX + 100, 505, 64, "amt", fuell=WEISS),
    ficon("tabler", "building", 1700, BODEN, 260, "buchholz", fuell=BLAU),
    pl("Straßenverkehrsbehörde", 1660, 560, beim("buchholz", "Straßenverkehrsbehörde"), fill=WEISS, size=28, anker="m"),
    *fig("BU", BUX, BODEN, FH, [(beim("buchholz", "Herr"), "ruhig")], bis="bu1"),
    *redet("BU_redet", BUX, BODEN, FH, "bu1", "wi2"),
    *fig("BU", BUX, BODEN, FH, [("wi2", "ernst")], bis="bu2", erst="cut"),
    *redet("BU_redet", BUX, BODEN, FH, "bu2", "frage"),
    schild("Herr Buchholz, Stadt", BUX, beim("buchholz", "Herr"), BU_F, unten=BODEN),
    ficon("tabler", "phone", BUX - 105, 505, 64, beim("buchholz", "Herr"), fuell=WEISS),
    blase("sprech", 640, 200, "bu1", 1420, 210, inhalt=["Das Haltverbot dient der", "Sicherheit und Ordnung", "des Verkehrs."],
          textsize=31, figur=BUb, bis="wi2"),
    blase("sprech", 640, 200, "wi2", 520, 210, inhalt=["Welche Gefahr denn? Hier", "ist noch nie etwas passiert!"],
          textsize=31, figur=WBb, bis="bu2"),
    blase("sprech", 600, 190, "bu2", 1420, 210, inhalt=["Mehr kann ich Ihnen", "dazu nicht sagen."], textsize=32, figur=BUb),
])

# C Frage ------------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Kann man ein Schild anfechten?")], [
    *zeichen283(450, "frage", boden=760, d=220, oben=200),
    linienzug([(60, 760), (840, 760)], "frage", breite=6, farbe=INK),
    pl("Frau Wittmann will gegen das Schild vorgehen", 640, 800, beim("frage", "Frau"), fill=WEISS, size=32, anker="m"),
    pl("Kann man ein Verkehrsschild anfechten?", 1000, 300, beim("frage", "Kann"), fill=PINK, size=40, anker="m"),
    pl("Und hat sie Erfolg?", 1000, 420, "frage2", fill=GELB, size=40, anker="m"),
    *fig("WI", FX, FB, FR, [("frage", "entschl")]),
    schild("Frau Wittmann", FX, "frage", WI_F),
])

# D Sachverhalt -----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [glyphen(
    "Nordrhein-Westfalen: Frau Wittmann parkt seit 20 Jahren direkt vor ihrem Haus. Über Nacht lässt die Stadt dort ein "
    "dauerhaftes absolutes Haltverbot aufstellen (Zeichen 283), gut sichtbar. Frau Wittmann sieht es am nächsten Morgen zum "
    "ersten Mal. Auf ihre Nachfrage nennt Herr Buchholz von der Straßenverkehrsbehörde nur einen pauschalen Grund: "
    "„Sicherheit und Ordnung des Verkehrs“. Besondere Umstände an der Stelle nennt die Stadt auch später nicht. "
    "Frau Wittmann will gegen das Schild klagen."),
], glyphen("Kann sie das Schild anfechten – und hat sie Erfolg?"))

# E 1. Rechtsnatur ---------------------------------------------------------------------------------------------------------
RN = "1. Rechtsnatur"
W35 = ("„Allgemeinverfügung ist ein Verwaltungsakt, der sich an einen nach allgemeinen Merkmalen bestimmten oder "
       "bestimmbaren Personenkreis richtet oder die öffentlich-rechtliche Eigenschaft einer Sache oder ihre Benutzung "
       "durch die Allgemeinheit betrifft.“")
Z35 = ["„Allgemeinverfügung ist ein Verwaltungsakt, der sich an einen nach",
       "allgemeinen Merkmalen bestimmten oder bestimmbaren Personenkreis",
       "richtet oder die öffentlich-rechtliche Eigenschaft einer Sache oder",
       "ihre Benutzung durch die Allgemeinheit betrifft.“"]
w35, w35_y = wortlaut(70, 290, 1120, W35, "§ 35 Satz 2 VwVfG", "wl35", size=30, zeilen=Z35,
                      marken=[("bestimmbaren Personenkreis", beim("wl35", "drei")),
                              ("öffentlich-rechtliche Eigenschaft einer Sache", beim("wl35", "Varianten")),
                              ("ihre Benutzung durch die Allgemeinheit", beim("var3", "Benutzung"))])
folie([("natur", f"{RN}: Verwaltungsakt?"), ("strspr", f"{RN}: Allgemeinverfügung, § 35 S. 2 VwVfG"),
       ("dauer", f"{RN} › Dauerverwaltungsakt")], rechts_frei([
    *tafel("natur", "Ist das Schild ein Verwaltungsakt?"),
    ok(140, 203, beim("strspr", "Ja"), gr=20),
    z("ja: Verwaltungsakt in Form einer Allgemeinverfügung", 180, 180, beim("strspr", "Ja"), "Bold", 34),
    zit("ständige Rechtsprechung, BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 16", 180, 232, beim("strspr", "Rechtsprechung")),
    *w35,
    z("hier die 3. Variante: Benutzung der Straße", 110, w35_y + 22, beim("var3", "Benutzung"), "Bold", 34),
    zit("so etwa VG Münster, Urt. v. 14.11.2011 – 1 K 605/10, Rn. 18", 150, w35_y + 74, beim("var3", "Straße")),
    z("Merkmale des Verwaltungsakts: Folge 44", 110, w35_y + 130, "verweis", size=32),
    blk(110, w35_y + 190, 1040, 72, GELB, "dauer", [("regelt die Stelle auf Dauer: Dauerverwaltungsakt", "ExtraBold", 34, INK)]),
    zit("BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Rn. 21", 150, w35_y + 276, beim("dauer", "Dauerverwaltungsakt")),
    *zeichen283(IX, "natur", mast=False, oben=230, d=170),
    *fig("WI", FX, FB, FR, [("natur", "denkt"), ("dauer", "ruhig")]),
    schild("Frau Wittmann", FX, "natur", WI_F),
]))

# F 2. Bekanntgabe und Wirksamkeit --------------------------------------------------------------------------------------------
BW = "2. Bekanntgabe und Wirksamkeit"
folie([("bekannt", f"{BW}: § 43 I VwVfG"), ("aufstellen", f"{BW} › Aufstellen des Schildes"),
       ("sicht", f"{BW} › Sichtbarkeitsgrundsatz")], rechts_frei([
    *tafel("bekannt", "Bekanntgabe und Wirksamkeit"),
    z("wirksam mit der Bekanntgabe, § 43 Abs. 1 VwVfG", 110, 180, beim("bekannt", "Wirksam"), "Bold", 34),
    nein(150, 268, beim("aufstellen", "Brief"), gr=18),
    z("kein Brief", 195, 245, beim("aufstellen", "Brief"), size=34),
    nein(150, 328, beim("aufstellen", "ortsübliche"), gr=18),
    z("keine ortsübliche Bekanntmachung, § 41 Abs. 4 VwVfG", 195, 305, beim("aufstellen", "ortsübliche"), size=32),
    z("sondern: Aufstellen nach den Spezialregeln der StVO", 110, 380, beim("aufstellen", "Spezialregeln"), "Bold", 33),
    zit("vgl. § 39 Abs. 1, § 45 Abs. 4 StVO", 150, 432, beim("aufstellen", "Straßenverkehrs")),
    z("besondere Form der öffentlichen Bekanntgabe", 150, 480, beim("aufstellen", "besondere"), size=32),
    zit("BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 16", 150, 530, beim("aufstellen", "Bekanntgabe")),
    z("wirkt gegenüber jedem: Sichtbarkeitsgrundsatz", 110, 600, "sicht", size=32),
    z("erklärt im Abschleppfall, Folge 64", 150, 650, beim("sicht", "erklärt"), size=30),
    ok(150, 753, beim("wirksam", "wirksam"), gr=20),
    blk(195, 720, 955, 72, GRUEN, beim("wirksam", "gut"), [("gut zu sehen: wirksam", "ExtraBold", 36, INK)]),
    ficon("tabler", "mail", IX, IU, 150, "bekannt", fuell=WEISS, bis="aufstellen"),
    *zeichen283(IX, "aufstellen", mast=False, oben=230, d=170, bis="sicht"),
    ficon("tabler", "eye", IX, IU, 160, "sicht", fuell=WEISS),
    *fig("WI", FX, FB, FR, [("bekannt", "denkt"), ("wirksam", "sorge")]),
    schild("Frau Wittmann", FX, "bekannt", WI_F),
]))

# G 3. Zulässigkeit: Rechtsweg, Klageart, Klagebefugnis -------------------------------------------------------------------------
ZU = "3. Zulässigkeit"
folie([("zul", f"{ZU}: Verwaltungsrechtsweg"), ("statt", f"{ZU} › Anfechtungsklage"),
       ("befugt", f"{ZU} › Klagebefugnis")], rechts_frei([
    *tafel("zul", "Die Klage: Zulässigkeit"),
    ok(140, 203, beim("weg", "offen"), gr=20),
    z("Verwaltungsrechtsweg, § 40 Abs. 1 VwGO", 180, 180, "weg", "Bold", 34),
    ok(140, 283, beim("statt", "Anfechtungsklage"), gr=20),
    z("statthaft: Anfechtungsklage, § 42 Abs. 1 VwGO", 180, 260, "statt", "Bold", 34),
    z("Ziel: Aufhebung des Schildes", 220, 313, beim("statt", "Aufhebung"), size=32),
    z("Klagebefugnis, § 42 Abs. 2 VwGO:", 180, 390, "befugt", "Bold", 34),
    z("Verkehrsteilnehmerin, auf das Schild getroffen", 220, 445, beim("befugt", "Verkehrsteilnehmerin"), size=32),
    z("Adressatin eines belastenden Verwaltungsakts", 220, 495, beim("befugt", "Adressatin"), size=32),
    z("möglich: Verletzung der allgemeinen Handlungsfreiheit", 220, 545, beim("befugt", "allgemeinen"), size=32),
    blk(180, 610, 970, 76, GRUEN, beim("befugt", "Artikel"),
        [("Art. 2 Abs. 1 GG", "ExtraBold", 34, INK)]),
    ok(140, 633, beim("befugt", "Grundgesetz"), gr=20),
    ficon("tabler", "gavel", IX, IU, 170, "zul", fuell=WEISS),
    *fig("WI", FX, FB, FR, [("zul", "entschl")]),
    schild("Frau Wittmann", FX, "zul", WI_F),
]))

# H Vorverfahren, Frist, Klagegegner ----------------------------------------------------------------------------------------
folie([("vorv", f"{ZU} › Vorverfahren: in NRW nicht nötig"), ("frist", f"{ZU} › Klagefrist"),
       ("gegner", f"{ZU} › Klagegegner")], rechts_frei([
    *tafel("vorv", "Vorverfahren und Frist"),
    z("Vorverfahren: in Nordrhein-Westfalen nicht nötig", 110, 180, "vorv", "Bold", 34),
    zit("§ 110 Abs. 1 Satz 1 JustG NRW (Ausnahmen in Abs. 2)", 150, 230, beim("vorv", "Justizgesetz")),
    z("andere Länder: ggf. erst Widerspruch, § 68 VwGO", 150, 278, beim("vorv", "anderen"), size=32),
    z("Frist: Schild ohne Rechtsbehelfsbelehrung", 110, 350, "frist", "Bold", 34),
    z("1 Jahr, § 74 Abs. 1 Satz 2, § 58 Abs. 2 VwGO", 150, 403, beim("frist", "Jahresfrist"), size=32),
    blk(110, 465, 1040, 76, GELB, "erstmals", [("Beginn: erste Begegnung mit dem Schild", "ExtraBold", 36, INK)]),
    zit("BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Leitsatz 1, Rn. 14, 16", 150, 555, beim("erstmals", "trifft")),
    z("hier: an diesem Morgen", 150, 600, beim("erstmals", "also"), size=32),
    nein(150, 675, beim("nichtneu", "nicht"), gr=18),
    z("später wieder vorbei: kein neuer Fristbeginn", 195, 652, "nichtneu", size=32),
    zit("BVerwG, 3 C 37.09, Rn. 18", 195, 700, beim("nichtneu", "neu")),
    z("Klagegegner: die Stadt, § 78 Abs. 1 Nr. 1 VwGO", 110, 765, "gegner", "Bold", 34),
    ficon("tabler", "calendar", IX, IU, 160, "frist", fuell=WEISS, bis="gegner"),
    ficon("tabler", "building", IX, IU, 190, "gegner", fuell=BLAU),
    *fig("WI", FX, FB, FR, [("vorv", "ruhig"), ("frist", "denkt"), ("erstmals", "entschl")]),
    schild("Frau Wittmann", FX, "vorv", WI_F),
]))

# I Keine aufschiebende Wirkung -------------------------------------------------------------------------------------------
folie([("aufsch", f"{ZU} › keine aufschiebende Wirkung")], rechts_frei([
    *tafel("aufsch", "Aufschiebende Wirkung?", fill=HELL),
    warnung_i(150, 225, beim("aufsch", "Achtung"), gr=26),
    z("Achtung: Die Klage hat keine aufschiebende Wirkung.", 200, 200, beim("aufsch", "Klage"), "Bold", 34),
    blk(110, 290, 1040, 80, ROT, beim("aufsch", "sofort"), [("Haltverbot sofort vollziehbar", "ExtraBold", 38, INK)]),
    z("entsprechend § 80 Abs. 2 Satz 1 Nr. 2 VwGO", 150, 400, beim("aufsch", "entsprechend"), size=34),
    zit("BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 14", 150, 452, beim("aufsch", "Verwaltungsgerichtsordnung")),
    z("schnell Schutz nötig: Eilantrag", 110, 540, "eil", "Bold", 34),
    z("§ 80 Abs. 5 VwGO beim Verwaltungsgericht", 150, 595, beim("eil", "Eilantrag"), size=32),
    *zeichen283(IX, "aufsch", mast=False, oben=230, d=170, bis="eil"),
    ficon("tabler", "hourglass", IX, IU, 140, "eil", fuell=WEISS),
    *fig("WI", FX, FB, FR, [("aufsch", "sorge"), ("eil", "denkt")]),
    schild("Frau Wittmann", FX, "aufsch", WI_F),
]))

# J 4. Begründetheit: Rechtsgrundlage, formell --------------------------------------------------------------------------------
BG = "4. Begründetheit"
W451 = ("„Die Straßenverkehrsbehörden können die Benutzung bestimmter Straßen oder Straßenstrecken aus Gründen der "
        "Sicherheit oder Ordnung des Verkehrs beschränken oder verbieten und den Verkehr umleiten.“")
Z451 = ["„Die Straßenverkehrsbehörden können die Benutzung bestimmter Straßen",
        "oder Straßenstrecken aus Gründen der Sicherheit oder Ordnung des",
        "Verkehrs beschränken oder verbieten und den Verkehr umleiten.“"]
w451, w451_y = wortlaut(70, 330, 1120, W451, "§ 45 Abs. 1 Satz 1 StVO", "egl", size=30, zeilen=Z451,
                        marken=[("Benutzung bestimmter Straßen", beim("egl", "Benutzung")),
                                ("Sicherheit oder Ordnung des", beim("egl", "Sicherheit")),
                                ("beschränken", beim("egl", "beschränken"))])
folie([("begr", f"{BG}: § 113 I 1 VwGO"), ("egl", f"{BG} › Rechtsgrundlage: § 45 I 1 StVO"),
       ("formell", f"{BG} › formell")], rechts_frei([
    *tafel("begr", "Begründetheit"),
    z("§ 113 Abs. 1 Satz 1 VwGO: Haltverbot rechtswidrig", 110, 180, "begr", "Bold", 34),
    z("und Frau Wittmann dadurch in ihren Rechten verletzt", 150, 233, beim("begr", "Frau"), size=32),
    *w451,
    zit("Parkverbot: BVerwG, Urt. v. 24.1.2019 – 3 C 7.17, Rn. 11", 150, w451_y + 18, beim("egl", "Verkehrs")),
    ok(150, w451_y + 103, beim("formell", "zuständig"), gr=20),
    z("formell: Stadt zuständig", 195, w451_y + 80, "formell", "Bold", 34),
    ok(150, w451_y + 163, beim("formell", "Anhörung"), gr=20),
    z("Anhörung entbehrlich, § 28 Abs. 2 Nr. 4 VwVfG", 195, w451_y + 140, beim("formell", "Anhörung"), size=32),
    ficon("tabler", "building", IX, IU, 190, "begr", fuell=BLAU),
    *fig("BU", FX, FB, FR, [("begr", "ruhig"), ("formell", "ernst")]),
    schild("Herr Buchholz", FX, "begr", BU_F),
]))

# K § 45 Abs. 9 StVO: Satz 1 und Satz 3 ----------------------------------------------------------------------------------------
W459 = ("„Verkehrszeichen und Verkehrseinrichtungen sind nur dort anzuordnen, wo dies auf Grund der besonderen Umstände "
        "zwingend erforderlich ist. … Insbesondere Beschränkungen und Verbote des fließenden Verkehrs dürfen nur angeordnet "
        "werden, wenn auf Grund der besonderen örtlichen Verhältnisse eine Gefahrenlage besteht, die das allgemeine Risiko "
        "einer Beeinträchtigung der in den vorstehenden Absätzen genannten Rechtsgüter erheblich übersteigt. …“")
Z459 = ["„Verkehrszeichen und Verkehrseinrichtungen sind nur dort anzuordnen,",
        "wo dies auf Grund der besonderen Umstände zwingend erforderlich ist. …",
        "Insbesondere Beschränkungen und Verbote des fließenden Verkehrs dürfen",
        "nur angeordnet werden, wenn auf Grund der besonderen örtlichen",
        "Verhältnisse eine Gefahrenlage besteht, die das allgemeine Risiko einer",
        "Beeinträchtigung der in den vorstehenden Absätzen genannten",
        "Rechtsgüter erheblich übersteigt. …“"]
w459, w459_y = wortlaut(70, 150, 1120, W459, "§ 45 Abs. 9 Satz 1 und 3 StVO (Auszug)", "wl45", size=29, zeilen=Z459,
                        marken=[("zwingend erforderlich", beim("s1", "zwingend")),
                                ("besonderen örtlichen", beim("s3", "besonderen")),
                                ("eine Gefahrenlage besteht", beim("s3", "Gefahrenlage")),
                                ("erheblich übersteigt", beim("s3", "erheblich")),
                                ("des fließenden Verkehrs", beim("fliess", "fließenden"))])
folie([("wl45", f"{BG} › § 45 IX StVO"), ("s3", f"{BG} › § 45 IX 3 StVO: qualifizierte Gefahrenlage"),
       ("ruhend", f"{BG} › Haltverbot: ruhender Verkehr, § 45 IX 1 StVO")], rechts_frei([
    titel(glyphen("Entscheidend: § 45 Abs. 9 StVO"), 100, 75, "wl45", 44),
    *w459,
    z("Satz 3 nur für den fließenden Verkehr, etwa ein Überholverbot", 110, w459_y + 20, beim("fliess", "Das"), size=31),
    zit("BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Rn. 23–25 (Lkw-Überholverbot)", 150, w459_y + 66, beim("fliess", "Überholverbot")),
    blk(110, w459_y + 112, 1040, 76, GRUEN, "ruhend", [("Haltverbot = ruhender Verkehr: nur Satz 1", "ExtraBold", 36, INK)]),
    zit("BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 36", 150, w459_y + 200, beim("ruhend", "Bundesverwaltungsgericht")),
    *zeichen283(IX, "wl45", mast=False, oben=230, d=170),
    *fig("BU", FX, FB, FR, [("wl45", "ernst"), ("ruhend", "denkt")]),
    schild("Herr Buchholz", FX, "wl45", BU_F),
]))

# L zwingend erforderlich, Ermessen ------------------------------------------------------------------------------------------
folie([("zwingend", f"{BG} › zwingend erforderlich, § 45 IX 1 StVO"), ("ermessen", f"{BG} › Ermessen")], rechts_frei([
    *tafel("zwingend", "Satz 1: zwingend erforderlich", fill=ZARTBLAU),
    z("Behörde muss zurückhaltend sein:", 110, 180, beim("zwingend", "Behörde"), "Bold", 34),
    z("Schild nur, wenn die allgemeinen Verkehrsregeln", 150, 235, beim("zwingend", "Schild"), size=33),
    z("für einen sicheren und geordneten Verkehr", 150, 283, beim("zwingend", "sicheren"), size=33),
    z("nicht ausreichen", 150, 331, beim("zwingend", "ausreichen"), "Bold", 33),
    zit("BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 35", 150, 383, beim("zwingend", "ausreichen")),
    z("erst dann: Ermessen der Stadt", 110, 460, "ermessen", "Bold", 34),
    zit("BVerwG, Urt. v. 24.1.2019 – 3 C 7.17, Rn. 13", 150, 510, beim("ermessen", "Ermessen")),
    z("Wahl des Mittels: Verhältnismäßigkeit", 150, 560, beim("ermessen", "Wahl"), size=33),
    zit("BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Rn. 35", 150, 610, beim("ermessen", "Verhältnismäßigkeit")),
    ficon("tabler", "scale", IX, IU, 170, "ermessen", fuell=WEISS),
    *zeichen283(IX, "zwingend", mast=False, oben=230, d=170, bis="ermessen"),
    *fig("BU", FX, FB, FR, [("zwingend", "denkt"), ("ermessen", "ruhig")]),
    schild("Herr Buchholz", FX, "zwingend", BU_F),
]))

# M Subsumtion und Ergebnis ----------------------------------------------------------------------------------------------
folie([("hier", f"{BG} › Subsumtion: nur ein pauschaler Grund"), ("zeit", f"{BG} › maßgeblicher Zeitpunkt"),
       ("erg", "Ergebnis: Klage begründet")], rechts_frei([
    *tafel("hier", "Und hier?"),
    z("Stadt: nur „Sicherheit und Ordnung des Verkehrs“", 110, 180, beim("hier", "Stadt"), "Bold", 33),
    nein(150, 258, beim("hier", "Besondere"), gr=18),
    z("keine besonderen Umstände an dieser Stelle", 195, 235, beim("hier", "Besondere"), size=32),
    z("darlegen muss das die Behörde", 195, 290, "last", size=32),
    zit("vgl. BVerwG, 3 C 37.09, Rn. 37", 195, 337, beim("last", "darlegen")),
    z("Dauerverwaltungsakt: maßgeblich ist die letzte", 110, 395, "zeit", size=32),
    z("mündliche Verhandlung; neue Tatsachen noch möglich,", 150, 440, beim("zeit", "mündlichen"), size=32),
    z("etwa eine Feuerwehrzufahrt", 150, 485, beim("zeit", "Feuerwehrzufahrt"), size=32),
    zit("BVerwG, 3 C 37.09, Rn. 21, 28", 150, 532, beim("zeit", "Feuerwehrzufahrt", ende=True)),
    blk(110, 585, 1040, 72, ROT, "erg", [("rechtswidrig, verletzt Art. 2 Abs. 1 GG", "ExtraBold", 36, INK)]),
    blk(110, 675, 1040, 76, GRUEN, "aufheb", [("Klage begründet: Aufhebung, § 113 Abs. 1 Satz 1", "ExtraBold", 34, INK)]),
    z("kein Bescheidungsurteil: nur bei der Verpflichtungsklage", 110, 775, "keinbesch", size=30),
    zit("§ 113 Abs. 5 Satz 2 VwGO", 150, 818, beim("keinbesch", "Verpflichtungsklage")),
    *fig("WI", FX, FB, FR, [("hier", "denkt"), ("aufheb", "froh")]),
    schild("Frau Wittmann", FX, "hier", WI_F),
]))

# N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Das Schild gilt bis zur Aufhebung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bis zur Aufhebung gilt das Schild.", 200, 200, beim("tipp", "Bis"), "Bold", 36),
    z("Wer es ignoriert, riskiert:", 200, 265, beim("tipp", "Wer"), size=34),
    z("Bußgeld, § 49 Abs. 3 Nr. 4 StVO", 240, 320, beim("tipp", "Bußgeld"), size=34),
    z("Abschleppen: Abschleppfall, Folge 64", 240, 375, beim("tipp", "Abschleppen"), size=34),
    z("Haltverbot: keine besondere Gefahrenlage", 200, 470, "tipp2", "Bold", 34),
    z("aus § 45 Abs. 9 Satz 3 StVO prüfen", 240, 525, beim("tipp2", "Satz"), size=34),
    z("Satz 3 gilt nur für den fließenden Verkehr", 240, 580, beim("tipp2", "gilt"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema -----------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anfechtungsklage gegen ein Verkehrszeichen"), 110, 90, "sch", 44),
    z("I. Zulässigkeit", K1, 190, "q1", "Bold", 36, rechts=1820),
    z("1. Verwaltungsrechtsweg; Anfechtungsklage: Schild = Allgemeinverfügung, § 35 Satz 2 VwVfG", K2, 245, "q1a",
      size=32, rechts=1820),
    z("2. Klagebefugnis: Adressatin, Art. 2 Abs. 1 GG", K2, 300, "q1b", size=SZ, rechts=1820),
    z("3. Vorverfahren je nach Land (NRW: entbehrlich)", K2, 355, "q1c", size=SZ, rechts=1820),
    z("4. Frist: 1 Jahr ab der ersten Begegnung, § 58 Abs. 2 VwGO", K2, 410, "q1d", size=SZ, rechts=1820),
    z("II. Begründetheit, § 113 Abs. 1 Satz 1 VwGO", K1, 490, "q2", "Bold", 36, rechts=1820),
    z("1. Rechtsgrundlage: § 45 Abs. 1 Satz 1 StVO", K2, 545, "q2a", size=SZ, rechts=1820),
    z("2. zwingend erforderlich, § 45 Abs. 9 Satz 1 StVO", K2, 600, "q2b", size=SZ, rechts=1820),
    z("fließender Verkehr: zusätzlich Satz 3 (qualifizierte Gefahrenlage)", K3, 650, beim("q2b", "fließenden"), size=32,
      rechts=1820),
    z("3. Ermessen", K2, 715, "q2c", size=SZ, rechts=1820),
    z("4. Rechtsverletzung", K2, 770, "q2d", size=SZ, rechts=1820),
])

# P Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein Verkehrsschild ist eine ", 0), ("Allgemeinverfügung", "a"), (".", 0)]], 750, 320, 42, "merke",
                {"a": beim("merke", "Allgemeinverfügung")}),
    *markertext([[("Du kannst es anfechten, binnen eines Jahres", 0)]], 750, 378, 42, beim("merke", "Du"), {}),
    *markertext([[("ab der ", 0), ("ersten Begegnung", "b"), (".", 0)]], 750, 436, 42, beim("merke", "ersten", 1),
                {"b": beim("merke", "ersten")}),
    *markertext([[("Ein Haltverbot ist nur rechtmäßig, wenn es", 0)]], 750, 560, 42, "m2", {}),
    *markertext([[("auf Grund besonderer Umstände", 0)]], 750, 618, 42, beim("m2", "auf"), {}),
    *markertext([[("zwingend erforderlich", "c"), (" ist.", 0)]], 750, 676, 42, beim("m2", "zwingend"),
                {"c": beim("m2", "zwingend")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
