"""Folge 058 · Heroinspritzen-Fall: Eigenverantwortliche Selbstgefährdung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Freitagabend bei Udo (Fall), B Die Frage, C Sachverhalt, D Der echte Fall (BGHSt 32, 262),
E § 222 StGB (Wortlaut), F Eigenverantwortliche Selbstgefährdung, G Begründung, H Am Fall, I Variante 1 (überlegenes
Sachwissen), J Variante 2 (fehlende Eigenverantwortlichkeit), K Fremdgefährdung/Tatherrschaft (Ausblick Gisela-Fall),
L Variante 3 in der Wohnung, M Unterlassen (Ingerenz), N § 30 Abs. 1 Nr. 3 BtMG (Wortlaut), O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi).
Sehr zurückhaltende Darstellung: keine Spritzen, kein Konsum, keine Drogen- oder Sterbebilder; nur Päckchen, Warnschild,
leere Wohnung, Rettungswagen-Symbol. Geräusche nur bei sichtbarer Handlung: Klopfen an der Tür (szene_058klopfen_1),
Tür fällt ins Schloss (szene_058tuer_1) – Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_058/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobile Lesbarkeit: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def zitat(text, x, y, cue, size=26, **k):
    """BGH-Fundstelle unter einer Aussage (klein, grau, mindestens 26 px)."""
    return z(text, x, y, cue, "Bold", size, farbe=TEXT, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (zweizeilige Blöcke bleiben im Kasten)."""
    for t_, *_ in zeilen:
        glyphen(t_)
        assert F(_[0], _[1]).getlength(t_) <= w - 40, f"Block zu breit: {t_}"
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


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


def umbruch(text, breite, size):
    f = F("Regular", size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter die Wortgruppe (sie muss in einer Zeile stehen)."""
    zeilen = umbruch(text, w - 60, size)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


def sachverhalt_klein(cue, absaetze, frage, size=34, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber Schrift passend zu Grundfall und drei Varianten."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 14
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


# --- Eigene Hilfsfunktion (wie Folge 029/035/047/055): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----
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





# --- Figuren, Namensschilder, Requisiten ------------------------------------------------------------------------------
NAMEN = {"AC": ("Achim", GRUEN), "UD": ("Udo", LILA)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
X1, X2 = 1420, 1750                         # zwei Figuren rechts neben der Tafel
GLAS = (214, 230, 250, 255)
HOLZ = (222, 184, 135, 255)
TISCH = (249, 196, 140, 255)
GRAU = (205, 205, 210, 255)


def name(p, cx, cue, unten=BR, size=28, d=0.0, bis=None, anim="cut"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def figname(p, cx, folge, cue, unten=BR, hoehe=FR, bis=None, erst="cut"):
    """Figur mit Namensschild ab ihrem ersten Bild, solange sie im Bild ist."""
    return [*fig(p, cx, unten, hoehe, folge, bis=bis, erst=erst), name(p, cx, folge[0][0], unten=unten, bis=bis)]


def paeckchen(cx, unten, breite, cue, bis=None, anim="pop"):
    """Päckchen (tabler package, MIT) – abstraktes Symbol, kein Drogenbild."""
    return ficon("tabler", "package", cx, unten, breite, cue, fuell=WEISS, bis=bis, anim=anim)


def warnschild(cx, unten, breite, cue, bis=None, anim="pop", d=0.0):
    return ficon("tabler", "alert-triangle", cx, unten, breite, cue, fuell=GELB, bis=bis, anim=anim, d=d)


def grau(e):
    """Requisit „weggedacht“: gleiches Icon, nur blasser (wie Folge 026)."""
    a = np.asarray(e.sprite).copy()
    a[..., :3] = (a[..., :3].astype(float) * 0.35 + 255 * 0.65).astype(np.uint8)
    e.sprite = Image.fromarray(a)
    e.name = (e.name or "") + ":grau"
    return e


# --- Wohnung (Szene A und L) -----------------------------------------------------------------------------------------
BA, SH = 900, 560                           # Boden und Standhöhe im Fall
UDX, ACX = 1150, 1540                       # Udo, Achim
FEN = (230, 250, 400, 300)                  # Fenster
TUER = (1690, 380, 180, 520)                # Wohnungstür


def wohnung(cue, mit_fenster_mond=True, bis_mond=None):
    """Kleine Wohnung: Boden, Fenster, Stehlampe, Sofa, Tisch, Tür (Bausteine und Tabler-Icons, MIT)."""
    x, y, w, h = FEN
    tx, ty, tw, th = TUER
    els = [hart(linienzug([(60, BA + 2), (1860, BA + 2)], cue, breite=6, farbe=INK)),
           hart(karte(x, y, w, h, cue, fill=GLAS, rund=10, schatten=0, rand=5, anim="cut")),
           hart(linienzug([(x + w / 2, y + 4), (x + w / 2, y + h - 4)], cue, breite=5, farbe=INK)),
           hart(linienzug([(x + 4, y + h / 2), (x + w - 4, y + h / 2)], cue, breite=5, farbe=INK)),
           hart(ficon("tabler", "lamp", 120, BA, 150, cue, fuell=GELB, anim="cut")),
           hart(ficon("tabler", "sofa", 470, BA, 380, cue, fuell=BLAU, anim="cut")),
           hart(karte(760, 735, 250, 30, cue, fill=TISCH, rund=8, schatten=0, rand=4, anim="cut")),
           hart(linienzug([(790, 765), (790, BA)], cue, breite=6, farbe=INK)),
           hart(linienzug([(980, 765), (980, BA)], cue, breite=6, farbe=INK)),
           hart(karte(tx, ty, tw, th, cue, fill=HOLZ, rund=8, schatten=0, rand=5, anim="cut")),
           hart(karte(tx + 22, ty + th / 2 - 8, 26, 26, cue, fill=GELB, rund=13, schatten=0, rand=4, anim="cut"))]
    if mit_fenster_mond:
        els.append(hart(bis_(ficon("tabler", "moon-stars", x + w * 0.27, y + h / 2 - 18, 100, cue, fuell=GELB, anim="cut"), bis_mond)))
    return els


# A Fall: Freitagabend bei Udo ---------------------------------------------------------------------------------------
UDb = ("UD_redet_r", UDX, BA, SH)
ACb = ("AC_redet", ACX, BA, SH)
GEHT_ENDE = beim("geht", "Hause", ende=True)
folie([(NULL, "Fall · Freitagabend bei Udo"), ("morgen", "Fall · Am nächsten Morgen")], [
    *wohnung(NULL, bis_mond="morgen"),
    bis_(pl("Freitagabend", 100, 64, NULL, fill=GELB, size=34, anim="cut"), "morgen"),
    pl("kleine Wohnung", 100, 140, beim("fall", "Wohnung"), fill=WEISS, size=30, bis="morgen"),
    # Udo (blickt nach rechts zu Achim)
    *fig("UD", UDX, BA, SH, [("udo", "ruhig_r")], bis="u1"),
    *redet("UD_redet_r", UDX, BA, SH, "u1", "geht"),
    *fig("UD", UDX, BA, SH, [("geht", "ruhig_r"), ("allein", "denkt_r")], erst="cut", bis="morgen"),
    name("UD", UDX, "udo", unten=BA, bis="morgen"),
    pl("Mitte 50", UDX, 250, beim("udo", "Mitte"), fill=WEISS, size=28, anker="m", bis="achim"),
    pl("kennt die Gefahren", UDX, 250, beim("udo", "kennt"), fill=GELB, size=28, anker="m", bis="paeck"),
    # Achim klopft, kommt herein, übergibt das Päckchen
    szene(bewegt(peep_voll("AC_ruhig", ACX, BA, SH, "achim", anim="cut", bis="a1"), beim("achim", "kommt"),
                 beim("achim", "vorbei", ende=True), 180), "058klopfen*", 1.0, 0.0),
    bewegt(name("AC", ACX, "achim", unten=BA, bis="a1"), beim("achim", "kommt"), beim("achim", "vorbei", ende=True), 180),
    *redet("AC_redet", ACX, BA, SH, "a1", "u1"),
    name("AC", ACX, "a1", unten=BA, bis="u1"),
    peep_voll("AC_sorge", ACX, BA, SH, "u1", anim="cut", bis="geht"),
    name("AC", ACX, "u1", unten=BA, bis="geht"),
    paeckchen(ACX - 150, 640, 90, beim("paeck", "Päckchen"), bis="a1"),
    pl("wie verabredet", ACX, 250, beim("paeck", "verabredet"), fill=WEISS, size=28, anker="m", bis="a1"),
    paeckchen(905, 735, 80, "a1", anim="cut", bis="morgen"),
    blase("sprech", 540, 200, "a1", 1420, 175, inhalt=["Hier, wie besprochen.", "Pass auf dich auf."], textsize=34,
          figur=ACb, bis="u1"),
    blase("sprech", 560, 200, "u1", 780, 175, inhalt=["Keine Sorge,", "ich weiß, was ich tue."], textsize=34,
          figur=UDb, bis="geht"),
    # Achim geht hinaus (läuft zur Tür und verschwindet), die Tür fällt ins Schloss
    bewegt(peep_voll("AC_ruhig_r", 1700, BA, SH, "geht", anim="cut", bis=GEHT_ENDE), "geht", GEHT_ENDE, ACX - 1700),
    bewegt(name("AC", 1700, "geht", unten=BA, bis=GEHT_ENDE), "geht", GEHT_ENDE, ACX - 1700),
    szene(pl("Achim geht nach Hause", 1450, 140, GEHT_ENDE, fill=WEISS, size=28, anker="m", bis="morgen"), "058tuer*", 1.0, -0.05),
    pl("allein", UDX, 250, "allein", fill=WEISS, size=28, anker="m", bis="morgen"),
    warnschild(905, 660, 90, beim("allein", "Sie"), bis="morgen"),
    pl("Dosis zu hoch", 895, 520, beim("allein", "zu"), fill=ROT, size=30, anker="m", bis="morgen"),
    # Am nächsten Morgen: leere Wohnung, Rettungswagen vor dem Fenster
    pl("Am nächsten Morgen", 100, 64, "morgen", fill=GELB, size=34, anim="cut"),
    ficon("tabler", "sun", 1780, 230, 110, "morgen", fuell=GELB, anim="cut"),
    ficon("tabler", "ambulance", FEN[0] + FEN[2] / 2, FEN[1] + FEN[3] - 14, 200, beim("morgen", "kommt"), fuell=WEISS),
    pl("jede Hilfe zu spät", 960, 470, beim("morgen", "Hilfe"), fill=GRAU, size=32, anker="m"),
])

# B Die Frage ----------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BA + 2), (1860, BA + 2)], "frage", breite=6, farbe=INK)),
    *figname("AC", 1350, [("frage", "sorge"), ("frage2", "denkt")], "frage", unten=BA, hoehe=SH),
    pl("Hat Achim seinen Freund fahrlässig getötet?", 960, 120, "frage", fill=PINK, size=38, anker="m"),
    paeckchen(1640, 700, 110, "frage2"),
    pl("hat das Heroin besorgt", 1640, 470, beim("frage2", "Heroin"), fill=GELB, size=30, anker="m"),
])

# C Sachverhalt --------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Freitagabend bringt Achim seinem alten Freund Udo (Mitte 50) wie verabredet ein Päckchen Heroin. Udo nimmt seit "
    "vielen Jahren Heroin, ist nüchtern und kennt die Gefahren. Allein setzt er sich die Dosis selbst; sie ist zu hoch. "
    "Am nächsten Morgen kommt jede Hilfe zu spät.",
    "Variante 1: Achim weiß, dass das Heroin ungewöhnlich stark ist; Udo weiß es nicht.",
    "Variante 2: Udo ist schwer betrunken und kann das Risiko nicht mehr abwägen.",
    "Variante 3: Achim bleibt. Udo wird bewusstlos, Achim geht ohne Notruf. Mit Hilfe hätte Udo überlebt.",
], "Hat Achim Udo fahrlässig getötet?", size=38)

# D Der echte Fall: BGHSt 32, 262 ----------------------------------------------------------------------------------------
folie([("bgh", "Der echte Fall · BGHSt 32, 262")], [
    *tafel("bgh", "Der echte Fall"),
    z("BGH, Urteil vom 14. Februar 1984", 110, 180, beim("bgh", "Urteil"), "Bold", 36),
    zitat("1 StR 808/83 (BGHSt 32, 262)", 110, 230, beim("bgh", "Februar")),
    z("Der Angeklagte besorgte seinem Freund", 110, 310, "bgh2", size=34),
    z("die Spritzen,", 110, 357, beim("bgh2", "Spritzen"), size=34),
    z("das Heroin hatte der Freund selbst", 110, 404, beim("bgh2", "Heroin"), "Bold", 34),
    z("Landgericht: fahrlässige Tötung", 110, 490, "bgh3", "Bold", 36),
    nein(135, 583, beim("bgh3", "hob"), gr=22),
    z("BGH: aufgehoben", 175, 560, beim("bgh3", "hob"), "ExtraBold", 38),
    ficon("tabler", "calendar", 1450, 420, 150, beim("bgh", "Februar"), fuell=WEISS),
    pl("1984", 1450, 440, beim("bgh", "neunzehnhundert"), fill=GELB, size=34, anker="m"),
    ficon("tabler", "building-bank", 1720, 420, 170, beim("bgh", "Bundesgerichtshofs"), fuell=WEISS),
    pl("BGH", 1720, 440, beim("bgh", "Bundesgerichtshofs"), fill=BLAU, size=30, anker="m"),
    ficon("tabler", "gavel", 1580, 800, 160, "bgh3", fuell=HOLZ),
    pl("Landgericht", 1580, 830, "bgh3", fill=WEISS, size=28, anker="m"),
    pl("aufgehoben", 1720, 520, beim("bgh3", "hob"), fill=ROT, size=28, anker="m"),
])

# E § 222 StGB ------------------------------------------------------------------------------------------------------------
T222 = "„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“"
wl222, y222 = wortlaut(90, 170, 1090, T222, "§ 222 StGB", "p222", size=31,
                       marken=[("verursacht", beim("p222", "verursacht"))])
A = "A. § 222 StGB"
folie([("p222", f"{A} › Wortlaut"), ("erfolg", f"{A} › Erfolg"), ("kaus", f"{A} › Kausalität"),
       ("vorh", f"{A} › Vorhersehbarkeit"), ("aber", f"{A} › und doch keine Strafbarkeit?")], [
    *tafel("p222", "Fahrlässige Tötung"),
    *wl222,
    ok(135, y222 + 63, "erfolg", gr=22), z("Erfolg: Tod von Udo", 175, y222 + 40, "erfolg", "Bold", 34),
    ok(135, y222 + 128, beim("kaus", "Achim"), gr=22),
    z("Kausalität: Übergabe weggedacht,", 175, y222 + 105, "kaus", "Bold", 34),
    z("diese Dosis nicht gesetzt", 175, y222 + 152, beim("kaus", "hätte"), size=34),
    ok(135, y222 + 240, beim("vorh", "konnte"), gr=22),
    z("vorhersehbar: Heroin kann tödlich sein", 175, y222 + 217, "vorh", "Bold", 34),
    blk(110, y222 + 300, 1040, 90, ROT, "aber", [("BGH: trotzdem keine fahrlässige Tötung", "ExtraBold", 34, INK)]),
    *figname("AC", X1, [("p222", "denkt"), ("aber", "ernst")], "p222"),
    paeckchen(1720, 560, 120, "kaus", bis=beim("kaus", "weg")),
    grau(paeckchen(1720, 560, 120, beim("kaus", "weg"), anim="cut", bis="vorh")),
    pl("weggedacht", 1720, 590, beim("kaus", "weg"), fill=WEISS, size=28, anker="m", bis="vorh"),
    pl("kausal", 1720, 660, beim("kaus", "Achim"), fill=GRUEN, size=28, anker="m"),
    hart(paeckchen(1720, 560, 120, "vorh")),
    warnschild(1720, 400, 100, "vorh"),
])

# F Eigenverantwortliche Selbstgefährdung -------------------------------------------------------------------------------
B_ = f"{A} › objektive Zurechnung › eigenverantwortliche Selbstgefährdung"
folie([("eigen", B_)], [
    *tafel("eigen", "Eigenverantwortliche Selbstgefährdung", size=42),
    z("Eigenverantwortlich gewollte und", 110, 180, "satz", size=34),
    z("verwirklichte Selbstgefährdung:", 110, 227, beim("satz", "verwirklichte"), "Bold", 34),
    nein(135, 300, beim("satz", "fällt"), gr=20), z("fällt nicht unter die Tötungsdelikte,", 175, 277, beim("satz", "fällt"), size=34),
    z("wenn sich das bewusst eingegangene", 175, 324, beim("satz", "wenn"), size=34),
    z("Risiko verwirklicht", 175, 371, beim("satz", "Risiko"), "Bold", 34),
    zitat("BGHSt 32, 262, 264 f.; BGHSt 59, 150 Rn. 71; BGHSt 61, 21 Rn. 14", 110, 430, beim("satz", "Risiko")),
    z("Wer sie nur veranlasst, ermöglicht oder fördert:", 110, 510, "ermoegl", "Bold", 34),
    nein(135, 583, beim("ermoegl", "kann"), gr=20),
    z("keine Verurteilung wegen eines Tötungsdelikts", 175, 560, beim("ermoegl", "kann"), size=34),
    *figname("UD", X1, [("eigen", "denkt")], "eigen"),
    warnschild(X1, 380, 110, beim("satz", "Risiko")),
    pl("eigenes Risiko", X1, 230, beim("satz", "bewusst"), fill=GELB, size=28, anker="m"),
    *figname("AC", X2, [("ermoegl", "ruhig")], "ermoegl"),
    paeckchen(X2, 380, 90, beim("ermoegl", "ermöglicht")),
    pl("ermöglicht", X2, 230, beim("ermoegl", "ermöglicht"), fill=WEISS, size=28, anker="m"),
])

# G Begründung -----------------------------------------------------------------------------------------------------------
folie([("warum", f"{A} › objektive Zurechnung › Begründung")], [
    *tafel("warum", "Warum keine fahrlässige Tötung?", size=44),
    z("Das Gesetz bestraft nur,", 110, 180, beim("warum", "Gesetz"), size=34),
    z("wer einen anderen tötet", 110, 227, beim("warum", "anderen"), "Bold", 34),
    z("Vorsätzliche Teilnahme an einer freien", 110, 305, beim("warum", "Selbst"), size=34),
    z("Selbsttötung: grundsätzlich straflos", 110, 352, beim("warum", "Selbsttötung"), "Bold", 34),
    z("Dann auch nicht strafbar:", 110, 430, "wider", size=34),
    z("die fahrlässige Förderung", 110, 477, beim("wider", "fahrlässige"), "Bold", 34),
    zitat("BGHSt 32, 262, 263 ff.", 110, 530, beim("wider", "fahrlässige")),
    blk(110, 600, 1040, 90, GELB, "lehre", [("Lehre: Fall der objektiven Zurechnung", "ExtraBold", 34, INK)]),
    ficon("tabler", "scale", 1560, 520, 260, beim("warum", "Selbst"), fuell=WEISS),
    pl("vorsätzlich: straflos", 1560, 580, beim("warum", "Selbst"), fill=GRUEN, size=28, anker="m"),
    pl("fahrlässig: auch straflos", 1560, 660, beim("wider", "fahrlässige"), fill=GRUEN, size=28, anker="m"),
    pl("nur: einen anderen", 1560, 180, beim("warum", "anderen"), fill=WEISS, size=28, anker="m"),
])

# H Am Fall ------------------------------------------------------------------------------------------------------------
folie([("subs", f"{A} › objektive Zurechnung › am Fall")], [
    *tafel("subs", "Am Fall: Udo"),
    ok(135, 203, beim("subs", "erfahren"), gr=22), z("erfahren", 175, 180, beim("subs", "erfahren"), "Bold", 36),
    ok(135, 268, beim("subs", "nüchtern"), gr=22), z("nüchtern", 175, 245, beim("subs", "nüchtern"), "Bold", 36),
    ok(135, 333, beim("subs", "kannte"), gr=22), z("kannte das Risiko", 175, 310, beim("subs", "kannte"), "Bold", 36),
    ok(135, 413, "selbst", gr=22), z("Dosis selbst gesetzt:", 175, 390, "selbst", "Bold", 36),
    z("das Geschehen in seiner Hand", 175, 440, beim("selbst", "er"), size=34),
    blk(110, 530, 1040, 150, GRUEN, "ergebnis", [("Tod Achim nicht zuzurechnen", "ExtraBold", 36, INK),
                                                ("fahrlässige Tötung scheidet aus", "Bold", 34, INK)]),
    *figname("UD", X1, [("subs", "ruhig"), ("selbst", "denkt")], "subs"),
    *figname("AC", X2, [("subs", "ruhig"), ("ergebnis", "froh")], "subs"),
    pl("Udo selbst", X1, 380, "selbst", fill=LILA, size=28, anker="m"),
])

# I Variante 1: überlegenes Sachwissen ------------------------------------------------------------------------------------
G1 = "B. Grenzen › 1. überlegenes Sachwissen"
folie([("var1", f"{G1} (Variante 1)"), ("warn", f"{G1} › Warnung")], [
    *tafel("var1", "Variante 1: überlegenes Wissen"),
    z("Achim weiß: ungewöhnlich stark", 110, 180, beim("var1", "Achim"), "Bold", 34),
    z("Udo weiß es nicht", 110, 227, beim("var1", "Udo"), "Bold", 34),
    z("Strafbarkeit kann beginnen, wo jemand kraft", 110, 305, beim("ueber", "Strafbarkeit"), size=34),
    z("überlegenen Sachwissens das Risiko besser", 110, 352, beim("ueber", "überlegenen"), "Bold", 34),
    z("erfasst als der, der sich selbst gefährdet", 110, 399, beim("ueber", "erfasst"), size=34),
    zitat("BGHSt 32, 262, 265; BGH 1 StR 638/99, Rn. 10", 110, 455, beim("ueber", "erfasst")),
    ok(135, 553, "warn", gr=22), z("deutliche Warnung: Wissen weitergegeben", 175, 530, "warn", "Bold", 34),
    z("dann bleibt es bei der Selbstgefährdung", 175, 577, beim("warn", "Dann"), size=34),
    zitat("BGH, Urt. v. 11.4.2000 – 1 StR 638/99, Rn. 13–15", 175, 630, beim("warn", "Dann")),
    *figname("AC", X1, [("var1", "weiss"), ("warn", "sorge")], "var1"),
    *figname("UD", X2, [("var1", "froh"), ("warn", "denkt")], "var1"),
    ficon("tabler", "brain", X1, 380, 100, beim("var1", "weiß"), fuell=PINK),
    pl("sehr stark", X1, 170, beim("var1", "ungewöhnlich"), fill=ROT, size=28, anker="m", bis="warn"),
    ficon("tabler", "help-circle", X2, 380, 100, beim("var1", "Udo"), fuell=WEISS, bis="warn"),
    pl("überlegenes Wissen", 1585, 90, beim("ueber", "überlegenen"), fill=GELB, size=28, anker="m", bis="warn"),
    warnschild(1585, 300, 110, "warn"),
    pl("Warnung", X2, 230, beim("warn", "deutlich"), fill=GELB, size=28, anker="m"),
])

# J Variante 2: fehlende Eigenverantwortlichkeit -------------------------------------------------------------------------
G2 = "B. Grenzen › 2. fehlende Eigenverantwortlichkeit"
folie([("var2", f"{G2} (Variante 2)"), ("irrtum", f"{G2} › Irrtum, Täuschung"), ("jung", f"{G2} › Maßstab (Lehre)")], [
    *tafel("var2", "Variante 2: Rausch"),
    z("Udo ist schwer betrunken,", 110, 180, beim("var2", "Udo"), "Bold", 34),
    z("kann das Risiko nicht mehr abwägen", 110, 227, beim("var2", "kann"), size=34),
    nein(135, 313, "rausch", gr=22), z("Eigenverantwortlichkeit fehlt", 175, 290, "rausch", "ExtraBold", 36),
    z("Ebenso: Irrtum über die Gefahr,", 110, 380, "irrtum", "Bold", 34),
    z("etwa durch Täuschung", 110, 427, beim("irrtum", "etwa"), size=34),
    zitat("BGHSt 59, 150 Rn. 73; BGH 2 StR 563/18, Rn. 20", 110, 480, beim("irrtum", "täuscht")),
    blk(110, 560, 1040, 150, LILA, "jung", [("Wie streng der Maßstab ist, etwa bei", "Bold", 34, INK),
                                           ("Jugendlichen: in der Lehre umstritten", "Bold", 34, INK)]),
    *figname("UD", X1, [("var2", "muede"), ("irrtum", "fragt")], "var2"),
    ficon("tabler", "beer", X1 - 30, 380, 80, beim("var2", "betrunken"), fuell=GELB, bis="irrtum"),
    ficon("tabler", "beer", X1 + 50, 380, 80, beim("var2", "betrunken"), fuell=GELB, d=0.1, bis="irrtum"),
    pl("Rausch", X1, 230, beim("var2", "betrunken"), fill=GELB, size=28, anker="m", bis="irrtum"),
    *figname("AC", X2, [("irrtum", "weiss")], "irrtum"),
    pl("Täuschung", X2, 230, beim("irrtum", "täuscht"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "help-circle", X1, 380, 100, beim("irrtum", "irrt"), fuell=WEISS),
])

# K Fremdgefährdung: Tatherrschaft --------------------------------------------------------------------------------------
G3 = "B. Grenzen › 3. Fremdgefährdung: Tatherrschaft"
folie([("fremd", G3), ("gisela", f"{G3} › Ausblick: Gisela-Fall")], [
    *tafel("fremd", "Abgrenzung: Fremdgefährdung"),
    z("Achim setzt die Dosis eigenhändig:", 110, 180, "fremd", "Bold", 34),
    z("keine Selbstgefährdung mehr,", 110, 227, beim("fremd", "keine"), size=34),
    z("sondern Fremdgefährdung", 110, 274, beim("fremd", "sondern"), "Bold", 34),
    z("Entscheidend: die Tatherrschaft", 110, 350, "herr", "ExtraBold", 36),
    z("liegt sie auch beim Beteiligten:", 110, 402, beim("herr", "Liegt"), size=34),
    z("eigene Tat", 110, 449, beim("herr", "begeht"), "Bold", 34),
    zitat("BGHSt 49, 34 (3 StR 120/03) Rn. 17 f.; BGH 2 StR 563/18, Rn. 20", 110, 502, beim("herr", "begeht")),
    blk(110, 570, 1040, 150, LILA, "gisela", [("Gisela-Fall (BGHSt 19, 135): Tötung auf Verlangen", "Bold", 32, INK),
                                             ("Täter ist, wer das Geschehen beherrscht", "ExtraBold", 33, INK)]),
    zitat("zitiert in BGH, Beschl. v. 28.6.2022 – 6 StR 68/21, Rn. 14", 110, 735, beim("gisela", "Täter")),
    *figname("AC", X1, [("fremd", "ernst")], "fremd"),
    *figname("UD", X2, [("fremd", "fragt")], "fremd"),
    ficon("tabler", "hand-finger", X1 + 160, 440, 90, beim("fremd", "eigenhändig"), fuell=WEISS),
    pl("eigenhändig", X1, 270, beim("fremd", "eigenhändig"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "crown", 1585, 140, 70, "herr", fuell=GELB),
    pl("Tatherrschaft", 1585, 150, "herr", fill=GELB, size=28, anker="m"),
    pl("Fremdgefährdung", X2, 270, beim("fremd", "Fremdgefährdung"), fill=WEISS, size=28, anker="m"),
])

# L Variante 3 in der Wohnung ------------------------------------------------------------------------------------------
folie([("var3", "C. Variante 3 · Udo wird bewusstlos")], [
    *wohnung("var3", mit_fenster_mond=True),
    pl("Variante 3", 100, 64, "var3", fill=LILA, size=34, anim="cut"),
    *fig("AC", ACX - 80, BA, SH, [("var3", "ruhig"), (beim("var3", "Achim", 2), "angst")], erst="cut", bis=beim("var3", "geht")),
    name("AC", ACX - 80, "var3", unten=BA, bis=beim("var3", "geht")),
    bewegt(peep_voll("AC_angst_r", 1700, BA, SH, beim("var3", "geht"), anim="cut", bis=beim("var3", "Notruf", ende=True)),
           beim("var3", "geht"), beim("var3", "Notruf"), ACX - 80 - 1700),
    bewegt(name("AC", 1700, beim("var3", "geht"), unten=BA, bis=beim("var3", "Notruf", ende=True)),
           beim("var3", "geht"), beim("var3", "Notruf"), ACX - 80 - 1700),
    pl("Achim bleibt", ACX - 80, 250, beim("var3", "bleibt"), fill=WEISS, size=28, anker="m", bis=beim("var3", "geht")),
    ficon("tabler", "heart-rate-monitor", 885, 735, 110, beim("var3", "bewusstlos"), fuell=WEISS),
    pl("Udo bewusstlos", 885, 555, beim("var3", "bewusstlos"), fill=ROT, size=30, anker="m"),
    ficon("tabler", "phone-off", 1250, 560, 110, beim("var3", "Notruf"), fuell=WEISS),
    pl("kein Notruf", 1250, 380, beim("var3", "Notruf"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "ambulance", FEN[0] + 300, FEN[1] + FEN[3] - 14, 150, "rettung", fuell=WEISS),
    pl("mit Hilfe: überlebt", 960, 140, "rettung", fill=GRUEN, size=28, anker="m"),
])

# M Unterlassen: Garant aus Ingerenz -----------------------------------------------------------------------------------
C3 = "C. Variante 3 › Unterlassen, § 13 StGB"
folie([("ing", f"{C3}: Ingerenz"), ("verzicht", f"{C3} › kein Verzicht auf Rettung"), ("unterl", f"{C3} › §§ 222, 212 StGB")], [
    *tafel("ing", "Garant aus Ingerenz"),
    nein(135, 203, beim("ing", "Jetzt"), gr=20), z("Selbstgefährdung hilft Achim jetzt nicht", 175, 180, beim("ing", "Jetzt"), "Bold", 34),
    z("Strafbares Überlassen des Heroins:", 110, 255, beim("ing", "Wer"), size=34),
    z("Garant aus Ingerenz, sobald die Gefahr", 110, 302, beim("ing", "Garant"), "Bold", 34),
    z("eintritt, etwa mit der Bewusstlosigkeit", 110, 349, beim("ing", "etwa"), size=34),
    zitat("BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 19 f.; BGHSt 46, 279 Rn. 28", 110, 402, beim("ing", "etwa")),
    z("Entscheidung von Udo: Gefahr ja,", 110, 475, "verzicht", "Bold", 34),
    z("Verzicht auf Rettung nein", 110, 522, beim("verzicht", "nicht"), "Bold", 34),
    zitat("BGHSt 61, 21 (1 StR 328/15) Rn. 18", 110, 575, beim("verzicht", "Rettung")),
    blk(110, 645, 1040, 150, GELB, "unterl", [("Tötung durch Unterlassen, § 13 StGB", "ExtraBold", 34, INK),
                                             ("fahrlässig: § 222 · mit Vorsatz: § 212", "Bold", 34, INK)]),
    *figname("AC", X1, [("ing", "angst"), ("unterl", "ernst")], "ing"),
    ficon("tabler", "phone-call", X2, 600, 130, beim("ing", "Garant"), fuell=GRUEN),
    pl("Garant", X2, 630, beim("ing", "Garant"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "heart-rate-monitor", X2, 380, 110, beim("ing", "Bewusstlosigkeit"), fuell=WEISS),
    pl("Gefahr tritt ein", X2, 230, beim("ing", "Bewusstlosigkeit"), fill=ROT, size=28, anker="m"),
])

# N § 30 Abs. 1 Nr. 3 BtMG -------------------------------------------------------------------------------------------------
T30 = ("„(1) Mit Freiheitsstrafe nicht unter zwei Jahren wird bestraft, wer … 3. Betäubungsmittel abgibt, einem anderen "
       "verabreicht oder zum unmittelbaren Verbrauch überläßt und dadurch leichtfertig dessen Tod verursacht, …“")
wl30, y30 = wortlaut(90, 160, 1090, T30, "§ 30 Abs. 1 Nr. 3 BtMG", "btm", size=30,
                     marken=[("abgibt", beim("btm", "abgibt")), ("leichtfertig dessen Tod", beim("btm", "leichtfertig"))])
D_ = "D. § 30 Abs. 1 Nr. 3 BtMG"
folie([("btm", f"{D_} › Wortlaut"), ("immanent", f"{D_} › Selbstgefährdung unerheblich"), ("leicht", f"{D_} › Leichtfertigkeit"),
       ("abgabe", f"{D_} › Abgabe, § 29 BtMG")], [
    *tafel("btm", "Betäubungsmittelgesetz"),
    *wl30,
    ok(135, y30 + 58, "immanent", gr=20), z("Selbstgefährdung hindert die Zurechnung nicht", 175, y30 + 35, "immanent", "Bold", 33),
    zitat("BGH 1 StR 638/99, Rn. 11; BGHSt 37, 179, 182 f.", 175, y30 + 82, beim("immanent", "Tatbestand")),
    z("aber leichtfertig: besonderer Leichtsinn", 175, y30 + 140, "leicht", "Bold", 33),
    z("oder besondere Gleichgültigkeit", 175, y30 + 185, beim("leicht", "oder"), size=33),
    zitat("BGHSt 46, 279 (5 StR 474/00) Rn. 24", 175, y30 + 232, beim("leicht", "Gleichgültigkeit")),
    z("unerlaubte Abgabe ohnehin strafbar,", 175, y30 + 290, "abgabe", "Bold", 33),
    z("§ 29 Abs. 1 Satz 1 Nr. 1 BtMG", 175, y30 + 335, beim("abgabe", "Paragraf"), size=33),
    *figname("AC", X1, [("btm", "denkt"), ("leicht", "ernst")], "btm"),
    paeckchen(X2, 560, 120, beim("btm", "abgibt")),
    pl("abgegeben", X2, 590, beim("btm", "abgibt"), fill=WEISS, size=28, anker="m"),
    pl("echter Fall: kein Heroin abgegeben", 1590, 300, "echt", fill=GELB, size=28, anker="m"),
])

# O Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Selbstgefährdung bei der objektiven Zurechnung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nicht bei der Kausalität stehen bleiben", 200, 200, beim("tipp", "Bleib"), "Bold", 34),
    z("Selbstgefährdung: bei der objektiven Zurechnung", 200, 250, beim("tipp", "Die"), size=33),
    z("Dort fragen:", 110, 340, "tipp2", "Bold", 34),
    z("Eigenverantwortlichkeit?", 150, 390, beim("tipp2", "Eigenverantwortlichkeit"), size=34),
    z("überlegenes Wissen?", 150, 437, beim("tipp2", "überlegenem"), size=34),
    z("Tatherrschaft?", 150, 484, beim("tipp2", "Tatherrschaft"), size=34),
    blk(110, 570, 1040, 150, GELB, "tipp3", [("§ 222 scheidet aus? Dann noch:", "Bold", 34, INK),
                                            ("Unterlassen und Betäubungsmittelgesetz", "ExtraBold", 34, INK)]),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m"),
])

# P Klausurschema ----------------------------------------------------------------------------------------------------------
K1, K2, K3 = 130, 190, 250
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: fahrlässige Tötung, § 222 StGB", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 180, "k1", "ExtraBold", 38, rechts=1820),
    z("1. Erfolg, Handlung, Kausalität", K2, 236, "k1a", "Bold", 34, rechts=1820),
    z("2. objektive Sorgfaltspflichtverletzung bei Vorhersehbarkeit", K2, 286, "k1b", "Bold", 34, rechts=1820),
    z("3. objektive Zurechnung", K2, 336, "k1c", "Bold", 34, rechts=1820),
    z("Selbstgefährdung eigenverantwortlich?", K3, 384, "k1d", size=34, rechts=1820),
    z("kein überlegenes Wissen?", K3, 432, "k1e", size=34, rechts=1820),
    z("Tatherrschaft beim Opfer?", K3, 480, "k1f", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 545, "k2", "ExtraBold", 38, rechts=1820),
    z("III. Schuld", K1, 605, "k3", "ExtraBold", 38, rechts=1820),
    z("Danach: Unterlassen ab der Bewusstlosigkeit, §§ 222/212, 13 StGB", K1, 680, "k4", "ExtraBold", 38, rechts=1820),
    z("und § 30 Abs. 1 Nr. 3 BtMG", K2, 745, "k5", "ExtraBold", 38, rechts=1820),
])

# Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 140, "merke", 80, anker="m"),
    *markertext([[("Wer nur die ", 0), ("eigenverantwortliche", "a")], [("Selbstgefährdung eines anderen", 0)],
                 [("ermöglicht, tötet ihn nicht.", 0)]], 750, 250, 40, "merke", {"a": beim("merke", "eigenverantwortliche")}),
    *markertext([[("Das ", 0), ("kippt", "b"), (" bei überlegenem Wissen,", 0)], [("fehlender Eigenverantwortlichkeit", 0)],
                 [("oder eigener Tatherrschaft.", 0)]], 750, 470, 38, "m2", {"b": beim("m2", "kippt")}),
    *markertext([[("Das ", 0), ("Betäubungsmittelgesetz", "c")], [("bleibt trotzdem anwendbar.", 0)]], 750, 690, 40, "m3",
                {"c": beim("m3", "Betäubungsmittelgesetz")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m"),
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
