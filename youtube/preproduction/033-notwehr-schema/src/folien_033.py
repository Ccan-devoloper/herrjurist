"""Folge 033 · Notwehr Schema § 32 StGB – so prüfst du die Notwehr. Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Vor der Stadtbibliothek (Fall), B Sachverhalt, C Tatbestand § 223 kurz, D Wortlautkarte § 32,
E 1. Notwehrlage, F 2. Notwehrhandlung: gegen den Angreifer, Erforderlichkeit, G milderes Mittel?, H Androhung,
I Gebotenheit (Überblick), J Gebotenheit bei Ulrike, K 3. Verteidigungswille, L Ergebnis, M Abgrenzung § 33 (Wortlautkarte),
N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Gewalt zurückhaltend: Der Tritt selbst wird nicht gezeigt (Pille und Schuh-Icon, danach Torsten mit Schmerzmimik).
Geräusch nur bei sichtbarer Handlung: Fahrradschloss beim Aufschließen (CC0, Kopie aus Folge 027, Herkunft in geraeusche_herkunft.json)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_033/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
LEDER = (205, 140, 90, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen); Ersatzschrift-Zeichen wie „→“ werden nicht verwendet."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def quelle(text, x, y, cue, **k):
    return z(text, x, y, cue, "Bold", 27, farbe=TEXT, **k)


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def wortlaut(x, y, w, zeilen, quelle_, cue, marken=(), size=31, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(zeile, wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
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
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle_, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 022/026/029): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------
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


BODEN, FH = 880, 430
BR, FR = 930, 450                            # Figuren rechts neben der Tafel
NAMEN = {"UL": ("Ulrike", LILA), "TO": ("Torsten", ORANGE), "KL": ("Herr Kluge", BLAU)}


def name(p, cx, cue, unten=BODEN, size=28, d=0.2, bis=None, anim="pop", text=None):
    t, f = NAMEN[p]
    return pl(text or t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def tasche(cx, unten, breite, cue, bis=None, anim="pop"):
    return ficon("ph", "handbag", cx, unten, breite, cue, fuell=LEDER, nebenfarbe=LEDER, anim=anim, bis=bis)


# A Fall: vor der Stadtbibliothek ---------------------------------------------------------------------------------------
KLX, RADX, ULX, TOX, TOX2, BIBX = 230, 510, 770, 1065, 1420, 1720
ULb = ("UL_redet_r", ULX, BODEN, FH)
TOb = ("TO_redet", TOX, BODEN, FH)
KLb = ("KL_redet_r", KLX, BODEN, FH)
TASCHE_MITTE = (ULX + TOX) // 2 + 20
folie([(NULL, "Fall · Vor der Stadtbibliothek"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=6, farbe=INK)),
    hart(pl("Dienstagnachmittag", 70, 40, NULL, fill=GELB, size=40, anim="cut")),
    hart(ficon("tabler", "building-community", BIBX, BODEN, 300, NULL, fuell=WEISS, nebenfarbe=BLAU, anim="cut")),
    hart(ficon("tabler", "books", BIBX + 10, 470, 90, NULL, fuell=GELB, nebenfarbe=WEISS, anim="cut")),
    hart(pl("Stadtbibliothek", BIBX, 540, NULL, fill=WEISS, size=30, anker="m", anim="cut")),
    hart(ficon("ph", "bicycle", RADX, BODEN, 250, NULL, fuell=WEISS, nebenfarbe=WEISS, anim="cut")),
    szene(ficon("tabler", "lock-open", RADX + 20, 690, 60, beim("ulrike", "schließt"), fuell=GRAU, bis="torsten"), "033schloss*", 1.0, 0.0),
    pl("schließt ihr Fahrrad auf", RADX + 20, 600, beim("ulrike", "schließt"), fill=WEISS, size=28, anker="m", bis="torsten"),
    # Tasche: über der Schulter – zwischen beiden (Torsten zerrt) – wieder bei Ulrike
    tasche(ULX + 55, 690, 90, beim("ulrike", "Tasche"), bis=beim("torsten", "packt")),
    hart(tasche(TASCHE_MITTE, 712, 100, beim("torsten", "packt"), bis="los", anim="cut")),
    hart(tasche(ULX + 55, 690, 90, "los", anim="cut")),
    pl("packt die Tasche und zerrt", TASCHE_MITTE, 360, beim("torsten", "packt"), fill=ORANGE, size=28, anker="m", bis="t1"),
    pl("hält mit beiden Händen fest", TASCHE_MITTE, 360, "haelt", fill=LILA, size=28, anker="m", bis="u1"),
    pl("zerrt nur noch fester", TASCHE_MITTE, 360, "zerrt", fill=ORANGE, size=28, anker="m", bis="tritt"),
    ficon("tabler", "shoe", TASCHE_MITTE + 30, BODEN - 10, 80, "tritt", fuell=GRAU, bis="los"),
    pl("Tritt gegen das Schienbein", TASCHE_MITTE, 360, "tritt", fill=ROT, size=28, anker="m", bis="los"),
    pl("lässt los und humpelt davon", TOX2, 330, "los", fill=WEISS, size=28, anker="m", bis="frage"),
    pl("Bluterguss am Schienbein", TOX2, 395, "blau", fill=ROT, size=28, anker="m"),
    # Ulrike
    *fig("UL", ULX, BODEN, FH, [("ulrike", "ruhig_r"), (beim("torsten", "packt"), "schreck_r"), ("haelt", "fest_r")], bis="u1"),
    *redet("UL_redet_r", ULX, BODEN, FH, "u1", "kluge"),
    *fig("UL", ULX, BODEN, FH, [("kluge", "fest_r"), ("los", "sorge_r"), ("frage", "denkt_r")], erst="cut"),
    name("UL", ULX, "ulrike", text="Ulrike, Mitte 40"),
    # Torsten: kommt, packt, redet, zerrt fester, Tritt (Schmerz), humpelt davon (blickt weg, nach rechts)
    *fig("TO", TOX, BODEN, FH, [("torsten", "gier")], bis="t1"),
    *redet("TO_redet", TOX, BODEN, FH, "t1", "haelt"),
    *fig("TO", TOX, BODEN, FH, [("haelt", "gier"), ("zerrt", "wut"), ("tritt", "schmerz")], erst="cut", bis="los"),
    name("TO", TOX, "torsten", text="Torsten, Mitte 20", bis="los"),
    *fig("TO", TOX2, BODEN, FH, [("los", "muede_r")], erst="cut"),
    name("TO", TOX2, "los", text="Torsten, Mitte 20", anim="cut", d=0.0),
    # Herr Kluge
    *fig("KL", KLX, BODEN, FH, [("kluge", "ruhig_r")], bis="kl1"),
    *redet("KL_redet_r", KLX, BODEN, FH, "kl1", "zerrt"),
    *fig("KL", KLX, BODEN, FH, [("zerrt", "schreck_r"), ("frage", "ernst_r")], erst="cut"),
    name("KL", KLX, "kluge", text="Herr Kluge, Passant"),
    ficon("tabler", "device-mobile", KLX + 95, 640, 46, beim("kluge", "Handy"), fuell=BLAU),
    # Blasen
    blase("sprech", 520, 170, "t1", 1180, 230, inhalt=["Her mit der Tasche!"], textsize=38, figur=TOb, bis="haelt"),
    blase("sprech", 600, 200, "u1", 700, 230, inhalt=["Lass los, sonst", "wehre ich mich!"], textsize=38, figur=ULb, bis="kluge"),
    blase("sprech", 500, 170, "kl1", 420, 230, inhalt=["Ich rufe die Polizei!"], textsize=36, figur=KLb, bis="zerrt"),
    # Frage
    pl("Hat Ulrike sich wegen Körperverletzung strafbar gemacht?", 960, 190, "frage", fill=PINK, size=36, anker="m"),
    ficon("tabler", "shield-check", 960, 340, 100, "frage2", fuell=GRUEN),
    pl("Notwehr, Schritt für Schritt", 960, 360, beim("frage2", "Notwehr"), fill=GRUEN, size=30, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Dienstagnachmittag vor der Stadtbibliothek: Torsten (Mitte 20) packt die Tasche von Ulrike (Mitte 40) und zerrt daran: "
    "„Her mit der Tasche!“ Ulrike hält sie mit beiden Händen fest und warnt: „Lass los, sonst wehre ich mich!“ Der Passant "
    "Herr Kluge ruft die Polizei; sie kann erst nach einigen Minuten da sein.",
    "Torsten zerrt nur noch fester. Ulrike tritt ihm kräftig gegen das Schienbein, um ihre Tasche zu behalten. Torsten lässt "
    "los und humpelt davon; am Schienbein bekommt er einen Bluterguss.",
    "Annahme: Torsten ist erwachsen und erkennbar bei klarem Verstand. Ulrike hat ihn vorher nicht provoziert.",
], "Hat Ulrike sich wegen Körperverletzung strafbar gemacht?")

# C Tatbestand § 223 (kurz) ----------------------------------------------------------------------------------------------
PA = "A. Ulrike, § 223 Abs. 1 StGB"
folie([("tb", f"{PA} › I. Tatbestand"), ("rw", f"{PA} › II. Rechtswidrigkeit")], [
    *tafel("tb", "Körperverletzung, § 223 Abs. 1 StGB", h=720),
    z("I. Tatbestand", 110, 190, "tb", "ExtraBold", 40),
    ok(135, 283, beim("tb2", "Misshandlung"), gr=22), z("Tritt: körperliche Misshandlung", 175, 260, beim("tb2", "Tritt"), size=36),
    ok(135, 343, beim("tb2", "Gesundheitsschädigung"), gr=22), z("Bluterguss: Gesundheitsschädigung", 175, 320, beim("tb2", "Bluterguss"), size=36),
    ok(135, 403, beim("tb2", "vorsätzlich"), gr=22), z("Vorsatz", 175, 380, beim("tb2", "vorsätzlich"), size=36),
    z("II. Rechtswidrigkeit?", 110, 490, "rw", "ExtraBold", 40),
    fl_block(110, 570, 1040, 90, GRUEN, beim("rw", "Notwehr"), [("gerechtfertigt durch Notwehr?", "ExtraBold", 38, INK)]),
    *fig("UL", 1420, BR, FR, [("tb", "denkt"), ("rw", "fest")]),
    name("UL", 1420, "tb", unten=BR),
    *fig("TO", 1760, BR, FR, [("tb", "schmerz")]),
    name("TO", 1760, "tb", unten=BR),
    ficon("tabler", "shoe", 1610, BR - 10, 80, beim("tb2", "Tritt"), fuell=GRAU),
    pl("Bluterguss", 1760, 420, beim("tb2", "Bluterguss"), fill=ROT, size=28, anker="m"),
])

# D Wortlautkarte § 32 -----------------------------------------------------------------------------------------------------
PN = "A. Ulrike › II. Rechtswidrigkeit › Notwehr, § 32 StGB"
P32 = ["„(1) Wer eine Tat begeht, die durch Notwehr geboten ist, handelt",
       "nicht rechtswidrig.",
       "(2) Notwehr ist die Verteidigung, die erforderlich ist, um einen",
       "gegenwärtigen rechtswidrigen Angriff von sich oder einem anderen",
       "abzuwenden.“"]
wl32, y32 = wortlaut(100, 160, 1060, P32, "§ 32 StGB", "p32",
                     marken=[(0, "geboten", beim("p32", "geboten")), (1, "nicht rechtswidrig", beim("p32", "nicht")),
                             (2, "Verteidigung", beim("abs2", "Verteidigung")), (2, "erforderlich", beim("abs2", "erforderlich")),
                             (3, "gegenwärtigen rechtswidrigen Angriff", beim("abs2", "gegenwärtigen"))])
folie([("p32", PN)], [
    *tafel("p32", "Notwehr, § 32 StGB"),
    *wl32,
    z("Aufbau:", 110, y32 + 40, "aufbau", "Bold", 36),
    fl_block(110, y32 + 95, 300, 90, BLAU, beim("aufbau", "Notwehrlage"), [("1. Notwehrlage", "ExtraBold", 30, INK)]),
    fl_block(425, y32 + 95, 345, 90, GRUEN, beim("aufbau", "Notwehrhandlung"), [("2. Notwehrhandlung", "ExtraBold", 30, INK)]),
    fl_block(785, y32 + 95, 365, 90, LILA, beim("aufbau", "Verteidigungswille"), [("3. Verteidigungswille", "ExtraBold", 30, INK)]),
    *fig("UL", 1560, BR, FR, [("p32", "denkt")]),
    name("UL", 1560, "p32", unten=BR),
    ficon("tabler", "shield-check", 1560, 330, 120, "p32", fuell=GRUEN),
])

# E 1. Notwehrlage ---------------------------------------------------------------------------------------------------------
PL = f"A. Ulrike › Notwehr, § 32 StGB › 1. Notwehrlage"
ULk, TOk, TAk = 1380, 1760, 1575                # kleine Bühne rechts: Ulrike – Tasche – Torsten
folie([("lage", PL), ("angriff", f"{PL} › a) Angriff"), ("gegenw", f"{PL} › b) gegenwärtig"),
       ("rechtsw", f"{PL} › c) rechtswidrig")], [
    *tafel("lage", "1. Notwehrlage"),
    z("a) Angriff", 110, 180, "angriff", "ExtraBold", 38),
    z("Torsten will die Tasche entreißen", 150, 235, beim("angriff", "Torsten"), size=34),
    ok(135, 312, beim("angriff", "verteidigen"), gr=22), z("Eigentum und Besitz: notwehrfähig", 175, 290, beim("angriff", "Eigentum"), size=34),
    quelle("vgl. BGH, 1 StR 126/21, Rn. 9 (Wegnahme einer Geldtasche)", 150, 342, beim("angriff", "verteidigen")),
    z("b) gegenwärtig", 110, 405, "gegenw", "ExtraBold", 38),
    z("bevorstehend, gerade stattfindend, andauernd", 150, 460, beim("gegenw", "unmittelbar"), size=34),
    ok(135, 537, beim("gegenw", "Torsten"), gr=22), z("Torsten zerrt in diesem Moment", 175, 515, beim("gegenw", "Torsten"), size=34),
    quelle("BGH, 4 StR 551/12, Rn. 16; 4 StR 318/20, Rn. 13", 150, 567, beim("gegenw", "Torsten")),
    z("c) rechtswidrig", 110, 630, "rechtsw", "ExtraBold", 38),
    ok(135, 707, beim("rechtsw", "Widerspruch"), gr=22), z("Widerspruch zur Rechtsordnung", 175, 685, beim("rechtsw", "Widerspruch"), size=34),
    quelle("BGH, 4 StR 551/12, Rn. 17", 150, 737, beim("rechtsw", "Widerspruch")),
    fl_block(110, 790, 1040, 90, BLAU, "lage_ok", [("Notwehrlage (+)", "ExtraBold", 40, INK)]),
    *fig("UL", ULk, BR, 400, [("lage", "fest_r")]),
    name("UL", ULk, "lage", unten=BR),
    *fig("TO", TOk, BR, 400, [("lage", "wut")]),
    name("TO", TOk, "lage", unten=BR),
    tasche(TAk, 760, 85, "lage"),
    pl("Eigentum, Besitz", TAk, 420, beim("angriff", "Eigentum"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "clock", TAk, 330, 70, beim("gegenw", "Torsten"), fuell=WEISS),
    pl("jetzt", TAk, 350, beim("gegenw", "Torsten"), fill=WEISS, size=26, anker="m"),
    pl("rechtswidrig", TAk, 250, beim("rechtsw", "Rechtswidrig"), fill=ROT, size=28, anker="m"),
])

# F 2. Notwehrhandlung: gegen den Angreifer, Erforderlichkeit ----------------------------------------------------------------
PH = f"A. Ulrike › Notwehr, § 32 StGB › 2. Notwehrhandlung"
folie([("handl", PH), ("gegen", f"{PH} › a) gegen den Angreifer"), ("erf", f"{PH} › b) erforderlich")], [
    *tafel("handl", "2. Notwehrhandlung"),
    z("a) Verteidigung gegen den Angreifer", 110, 180, "gegen", "ExtraBold", 38),
    ok(135, 257, beim("gegen", "Tritt"), gr=22), z("der Tritt trifft Torsten selbst", 175, 235, beim("gegen", "Tritt"), size=34),
    z("b) Erforderlichkeit", 110, 330, "erf", "ExtraBold", 38),
    z("Abwehr sofort und endgültig", 150, 385, beim("erf", "sofort"), size=34),
    z("mildestes Mittel in der konkreten Lage", 150, 437, beim("erf", "mildeste"), size=34),
    quelle("BGH, 4 StR 551/12, Rn. 26; 1 StR 126/21, Rn. 14", 150, 489, beim("erf", "mildeste")),
    ok(135, 567, "geeig", gr=22), z("geeignet: Torsten ließ los", 175, 545, "geeig", "Bold", 36),
    *fig("UL", 1420, BR, FR, [("handl", "fest")]),
    name("UL", 1420, "handl", unten=BR),
    *fig("TO", 1770, BR, FR, [("handl", "wut"), (beim("gegen", "Tritt"), "schmerz")]),
    name("TO", 1770, "handl", unten=BR),
    ficon("tabler", "shoe", 1600, BR - 30, 80, beim("gegen", "Tritt"), fuell=GRAU),
    pl("gegen den Angreifer", 1600, 300, "gegen", fill=WEISS, size=28, anker="m"),
    pl("Torsten ließ los", 1600, 380, "geeig", fill=GRUEN, size=28, anker="m"),
])

# G Milderes Mittel? ---------------------------------------------------------------------------------------------------------
IX = 1350
folie([("milder", f"{PH} › b) erforderlich: milderes Mittel?")], [
    *tafel("milder", "Gab es ein milderes Mittel?"),
    z("genauso sicher wirksam?", 110, 175, beim("milder", "genauso"), size=34, farbe=TEXT),
    nein(135, 262, beim("warn", "ohne"), gr=22), z("Warnung: ohne Erfolg", 175, 240, "warn", size=36),
    nein(135, 327, beim("festh", "Torsten"), gr=22), z("nur festhalten: Torsten zerrte fester", 175, 305, "festh", size=36),
    nein(135, 392, beim("polizei", "zu"), gr=22), z("Polizei: wäre zu spät gekommen", 175, 370, "polizei", size=36),
    z("milderes Mittel nur, wenn Wirkung unzweifelhaft", 110, 455, "risiko", "Bold", 34),
    quelle("BGH, 4 StR 197/12, Rn. 8; 2 StR 523/15, Rn. 10", 110, 507, beim("risiko", "unzweifelhaft")),
    nein(135, 587, "flucht", gr=22), z("fliehen, Tasche loslassen: nicht verlangt", 175, 565, "flucht", size=36),
    z("sonst würde sie den Angriff hinnehmen", 175, 617, beim("flucht", "damit"), size=32, farbe=TEXT),
    quelle("BGH, 4 StR 551/12, Rn. 26; 2 StR 523/15, Rn. 12", 175, 667, beim("flucht", "damit")),
    fl_block(110, 740, 1040, 90, GRUEN, "erf_ok", [("Tritt erforderlich (+)", "ExtraBold", 40, INK)]),
    ficon("tabler", "speakerphone", IX, 260, 80, "warn", fuell=GELB),
    pl("Warnung", IX + 140, 215, "warn", fill=WEISS, size=26),
    ficon("tabler", "hand-grab", IX, 410, 80, "festh", fuell=GELB),
    pl("festhalten", IX + 140, 365, "festh", fill=WEISS, size=26),
    ficon("ph", "siren", IX, 560, 80, "polizei", fuell=ROT),
    ficon("tabler", "clock", IX + 95, 560, 60, beim("polizei", "zu"), fuell=WEISS),
    pl("zu spät", IX + 140, 515, beim("polizei", "zu"), fill=WEISS, size=26),
    ficon("tabler", "run", IX, 710, 80, "flucht", fuell=GELB),
    pl("fliehen?", IX + 140, 665, "flucht", fill=WEISS, size=26),
    *fig("UL", 1770, BR, FR, [("milder", "denkt"), ("erf_ok", "fest")]),
    name("UL", 1770, "milder", unten=BR),
])

# H Androhung (nur Text und Warnsymbol, keine Waffe im Bild) ---------------------------------------------------------------
folie([("droh", f"{PH} › b) erforderlich: Androhung")], [
    *tafel("droh", "Übrigens: Androhung", h=600),
    z("gegen einen unbewaffneten Angreifer", 110, 190, beim("droh", "unbewaffneten"), size=36),
    z("eine lebensgefährliche Waffe:", 110, 245, beim("droh", "lebensgefährlichen"), "Bold", 38),
    z("in der Regel erst androhen", 150, 330, beim("droh", "anzudrohen"), "Bold", 36),
    z("oder weniger gefährlich versuchen", 150, 385, beim("droh", "weniger"), "Bold", 36),
    quelle("BGH, 2 StR 523/15, Rn. 11; 4 StR 197/12, Rn. 8", 150, 445, beim("droh", "weniger")),
    ficon("tabler", "alert-triangle", 1560, 420, 200, "droh", fuell=GELB),
    pl("erst androhen", 1560, 470, beim("droh", "anzudrohen"), fill=WEISS, size=30, anker="m"),
    pl("weniger gefährlich", 1560, 550, beim("droh", "weniger"), fill=WEISS, size=30, anker="m"),
])

# I Gebotenheit (Überblick) ------------------------------------------------------------------------------------------------
PG = f"{PH} › c) geboten"
GX1, GX2, GY1, GY2 = 1400, 1720, 330, 690
folie([("geboten", PG)], [
    *tafel("geboten", "c) Gebotenheit"),
    z("grundsätzlich keine Güterabwägung", 110, 180, beim("geboten", "Abwägung"), "Bold", 36),
    quelle("BGH, 2 StR 523/15, Rn. 21", 110, 232, beim("geboten", "grundsätzlich")),
    z("Ausnahmen aus sozialethischen Gründen:", 110, 300, "sozial", "Bold", 36),
    quelle("BGH, 1 StR 126/21, Rn. 18", 110, 352, beim("sozial", "sozialethischen")),
    z("erkennbar Schuldlose, z. B. Kinder", 150, 410, "fg1", size=34),
    quelle("BGH, 2 StR 523/15, Rn. 19", 150, 455, "fg1"),
    z("krasses Missverhältnis: Abwehr gegen Bagatelle", 150, 505, "fg2", size=34),
    quelle("BGH, 3 StR 450/10, Rn. 16; 2 StR 523/15, Rn. 21", 150, 550, "fg2"),
    z("vorwerfbare Provokation", 150, 600, "fg3", size=34),
    quelle("BGH, 4 StR 197/12, Rn. 15", 150, 645, "fg3"),
    z("enge familiäre Verbundenheit", 150, 695, "fg4", size=34),
    quelle("BGH, 2 StR 523/15, Rn. 18", 150, 740, "fg4"),
    fl_block(110, 790, 1040, 90, GELB, "fg_rf", [("dann: ausweichen, schonender wehren", "ExtraBold", 36, INK)]),
    ficon("tabler", "mood-kid", GX1, GY1, 120, "fg1", fuell=GELB),
    pl("Kinder", GX1, GY1 + 20, "fg1", fill=WEISS, size=26, anker="m"),
    ficon("tabler", "scale", GX2, GY1, 130, "fg2", fuell=GELB),
    pl("Bagatelle", GX2, GY1 + 20, beim("fg2", "Bagatelle"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "flame", GX1, GY2, 110, "fg3", fuell=ORANGE),
    pl("Provokation", GX1, GY2 + 20, beim("fg3", "provoziert"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "home-heart", GX2, GY2, 120, "fg4", fuell=PINK),
    pl("Familie", GX2, GY2 + 20, beim("fg4", "familiärer"), fill=WEISS, size=26, anker="m"),
    pl("sozialethische Grenzen", 1560, 120, "sozial", fill=GELB, size=30, anker="m"),
])

# J Gebotenheit bei Ulrike -------------------------------------------------------------------------------------------------
folie([("geb_ok", f"{PG}: bei Ulrike")], [
    *tafel("geb_ok", "Gebotenheit bei Ulrike", h=700),
    z("keine Fallgruppe passt", 110, 180, "geb_ok", "Bold", 38),
    ok(135, 267, beim("geb_ok", "erwachsen"), gr=22), z("Torsten ist erwachsen", 175, 245, beim("geb_ok", "Torsten"), size=36),
    ok(135, 327, beim("geb_ok", "provoziert"), gr=22), z("Ulrike hat nichts provoziert", 175, 305, beim("geb_ok", "Ulrike", 2), size=36),
    ok(135, 387, beim("geb_ok", "krassen"), gr=22), z("Tritt gegen Griff nach der Tasche:", 175, 365, beim("geb_ok", "Tritt"), size=36),
    z("kein krasses Missverhältnis", 175, 417, beim("geb_ok", "krassen"), "Bold", 36),
    fl_block(110, 520, 1040, 90, GRUEN, "geb_erg", [("geboten (+)", "ExtraBold", 40, INK)]),
    *fig("UL", 1420, BR, FR, [("geb_ok", "ruhig")]),
    name("UL", 1420, "geb_ok", unten=BR),
    *fig("TO", 1770, BR, FR, [("geb_ok", "denkt")]),
    name("TO", 1770, "geb_ok", unten=BR),
    pl("erwachsen", 1770, 330, beim("geb_ok", "erwachsen"), fill=WEISS, size=28, anker="m"),
    pl("nichts provoziert", 1420, 330, beim("geb_ok", "provoziert"), fill=WEISS, size=28, anker="m"),
])

# K 3. Verteidigungswille --------------------------------------------------------------------------------------------------
folie([("wille", "A. Ulrike › Notwehr, § 32 StGB › 3. Verteidigungswille")], [
    *tafel("wille", "3. Verteidigungswille", h=700),
    z("zumindest auch zur Abwehr des Angriffs", 110, 185, beim("wille", "zumindest"), "Bold", 36),
    quelle("BGH, 1 StR 126/21, Rn. 11", 110, 237, beim("wille", "abzuwehren")),
    z("Ärger oder Wut daneben: schaden nicht,", 110, 305, "wut", size=36),
    z("solange der Abwehrzweck nicht ganz zurücktritt", 110, 357, beim("wut", "solange"), size=36),
    ok(135, 447, "wille_ok", gr=22), z("Ulrike wollte ihre Tasche behalten", 175, 425, "wille_ok", "Bold", 36),
    fl_block(110, 520, 1040, 90, LILA, beim("wille_ok", "behalten"), [("Verteidigungswille (+)", "ExtraBold", 40, INK)]),
    *fig("UL", 1600, BR, FR, [("wille", "fest"), ("wille_ok", "froh")]),
    name("UL", 1600, "wille", unten=BR),
    ficon("tabler", "flame", 1400, 400, 90, "wut", fuell=ORANGE),
    pl("Wut", 1400, 420, "wut", fill=WEISS, size=26, anker="m"),
    tasche(1700, 760, 80, "wille_ok"),
    pl("Tasche behalten", 1600, 320, "wille_ok", fill=GELB, size=28, anker="m"),
])

# L Ergebnis -----------------------------------------------------------------------------------------------------------------
folie([("ergebnis", "A. Ulrike › Ergebnis")], [
    *tafel("ergebnis", "Ergebnis", h=640),
    fl_block(110, 180, 1040, 90, GRUEN, beim("ergebnis", "Notwehr"), [("Notwehr: nicht rechtswidrig", "ExtraBold", 40, INK)]),
    z("§ 32 Abs. 1 StGB", 110, 290, beim("ergebnis", "Notwehr"), "Bold", 30, farbe=TEXT),
    ok(135, 377, beim("ergebnis", "Sie"), gr=22), z("Ulrike ist nicht strafbar", 175, 355, beim("ergebnis", "Sie"), "Bold", 38),
    nein(135, 477, beim("duld", "kann"), gr=22), z("Torsten: keine Notwehr gegen", 175, 455, beim("duld", "kann"), size=36),
    z("Ulrikes rechtmäßige Abwehr", 175, 507, beim("duld", "kann"), size=36),
    *fig("UL", 1420, BR, FR, [("ergebnis", "froh")]),
    name("UL", 1420, "ergebnis", unten=BR),
    *fig("TO", 1770, BR, FR, [("ergebnis", "muede")]),
    name("TO", 1770, "ergebnis", unten=BR),
    ficon("tabler", "shield-check", 1420, 330, 100, beim("ergebnis", "Notwehr"), fuell=GRUEN),
    ficon("tabler", "ban", 1770, 330, 90, beim("duld", "kann"), fuell=ROT),
])

# M Abgrenzung § 33 ----------------------------------------------------------------------------------------------------------
P33 = ["„Überschreitet der Täter die Grenzen der Notwehr aus Verwirrung,",
       "Furcht oder Schrecken, so wird er nicht bestraft.“"]
wl33, y33 = wortlaut(100, 270, 1060, P33, "§ 33 StGB", "p33b",
                     marken=[(0, "Verwirrung", beim("p33b", "Verwirrung")), (1, "Furcht", beim("p33b", "Furcht")),
                             (1, "Schrecken", beim("p33b", "Schrecken"))])
folie([("p33", "Abgrenzung · Notwehrexzess, § 33 StGB")], [
    *tafel("p33", "Abgrenzung: § 33 StGB"),
    nein(135, 202, beim("p33", "nicht"), gr=22), z("stärker als erforderlich: nicht gerechtfertigt", 175, 180, beim("p33", "stärker"), size=34),
    *wl33,
    z("Tat bleibt rechtswidrig,", 110, y33 + 40, "p33c", "Bold", 36),
    z("aber der Täter ist entschuldigt", 110, y33 + 92, beim("p33c", "aber"), "Bold", 36),
    quelle("BGH, 3 StR 450/10, Rn. 13; 3 StR 199/15, Rn. 18", 110, y33 + 146, beim("p33c", "entschuldigt")),
    fl_block(110, y33 + 205, 1040, 90, GELB, "p33d", [("Voraussetzung: echte Notwehrlage", "ExtraBold", 38, INK)]),
    quelle("BGH, 3 StR 199/15, Rn. 19", 110, y33 + 310, "p33d"),
    ficon("tabler", "mood-nervous", 1400, 400, 110, beim("p33b", "Verwirrung"), fuell=GELB),
    pl("Verwirrung", 1400, 420, beim("p33b", "Verwirrung"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "mood-sad", 1720, 400, 110, beim("p33b", "Furcht"), fuell=BLAU),
    pl("Furcht", 1720, 420, beim("p33b", "Furcht"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "mood-surprised", 1560, 680, 110, beim("p33b", "Schrecken"), fuell=LILA),
    pl("Schrecken", 1560, 700, beim("p33b", "Schrecken"), fill=WEISS, size=26, anker="m"),
])

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Schwerpunkt Erforderlichkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Notwehr in der Rechtswidrigkeit,", 200, 200, beim("tipp", "Notwehr"), "Bold", 36),
    z("nach dem Tatbestand", 200, 250, beim("tipp", "nach"), "Bold", 36),
    z("Schwerpunkt meist: Erforderlichkeit", 240, 315, beim("tipp", "Schwerpunkt"), size=34),
    z("mildere Mittel konkret nennen:", 200, 400, "tipp2", "Bold", 36),
    z("Warnung, Festhalten, Hilfe rufen", 240, 455, beim("tipp2", "Warnung"), size=34),
    z("begründen: warum nicht genauso sicher?", 240, 507, beim("tipp2", "begründe"), size=34),
    z("Gebotenheit nur, wenn der Sachverhalt", 200, 595, "tipp3", "Bold", 36),
    z("eine Fallgruppe nahelegt", 200, 645, beim("tipp3", "eine"), "Bold", 36),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 250
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Notwehr, § 32 StGB", 110, 90, "sch", 50),
    z("1. Notwehrlage", K1, 190, "k1", "ExtraBold", 40, rechts=1820),
    z("a) Angriff", K3, 250, "k1a", size=36, rechts=1820),
    z("b) gegenwärtig", K3 + 290, 250, "k1b", size=36, rechts=1820),
    z("c) rechtswidrig", K3 + 620, 250, "k1c", size=36, rechts=1820),
    z("2. Notwehrhandlung", K1, 330, "k2", "ExtraBold", 40, rechts=1820),
    z("a) Verteidigung gegen den Angreifer", K3, 390, "k2a", size=36, rechts=1820),
    z("b) erforderlich: geeignet und mildestes gleich wirksames Mittel", K3, 445, "k2b", size=36, rechts=1820),
    z("c) geboten", K3, 500, "k2c", size=36, rechts=1820),
    z("3. Verteidigungswille", K1, 580, "k3", "ExtraBold", 40, rechts=1820),
    fl_block(K1, 680, 1000, 90, GRUEN, "k4", [("Folge: Tat nicht rechtswidrig", "ExtraBold", 40, INK)]),
])

# P Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Notwehr", "a"), (" braucht: Notwehrlage,", 0)], [("erforderliche und gebotene Verteidigung,", 0)],
                 [("Verteidigungswille.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "Notwehr")}),
    *markertext([[("Erforderlich", "b"), (": das mildeste Mittel,", 0)], [("das sicher wirkt.", 0)]], 750, 520, 44, "m2",
                {"b": beim("m2", "Erforderlich")}),
    *markertext([[("Fliehen", "c"), (" muss der Angegriffene", 0)], [("grundsätzlich nicht.", 0)]], 750, 700, 44, "m3", {"c": beim("m3", "fliehen")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
