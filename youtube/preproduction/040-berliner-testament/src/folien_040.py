"""Folge 040 · Berliner Testament: Die Falle nach dem ersten Todesfall (§ 2271 BGB) – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Günter und Ingrid (Ehepaar) errichten am Küchentisch ein eigenhändiges gemeinschaftliches Testament (gegenseitige
Alleinerben, Schlusserben Petra und Uwe zu gleichen Teilen). Drei Jahre später stirbt Günter (zurückhaltend: Kalender, leerer
Sessel); Ingrid hat das Erbe angenommen und will Uwe allein einsetzen. Szenen laut ../SZENENPLAN.md:
A Am Küchentisch, B Drei Jahre später, C Sachverhalt, D I. Wirksamkeit (§§ 2265, 2267), E1 § 2269 Abs. 1 (Wortlaut),
E2 Einheitslösung, F1 § 2270 Abs. 1 (Wortlaut), F2 Auslegung und Vermutung (§ 2270 Abs. 2, 3), G1 Bindung zu Lebzeiten
(§ 2271 Abs. 1, § 2296), G2 § 2271 Abs. 2 Satz 1 (Wortlaut), H Ausschlagung, I Ergebnis, J Gestaltungstipp
Änderungsklausel, K1 Ausblick Schenkung (§ 2287 analog), K2 Pflichtteil, L Klausurtipp (Lexi), M Klausurschema,
N Merksatz (Lexi). Keine Geräusche: Freesound gesperrt, kein passendes vorhandenes CC0-Geräusch (Stift auf Papier).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns wie in
Folge 034 (eigene Kopie, gemeinsame Dateien unverändert); wortlaut_auto() bricht den Normtext selbst um."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_040/"


FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HOLZ = (214, 186, 150, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=44):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_040/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def _marker(f, tx, ty, lh, size, zi, t, wort, mc, bis):
    a = t.index(wort)
    x0 = tx + f.getlength(t[:a]) - 4
    x1 = tx + f.getlength(t[:a + len(wort)]) + 4
    y0 = ty + zi * lh + size * 0.30
    im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
    return El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort)


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        els.append(_marker(f, tx, ty, lh, size, zi, zeilen[zi], wort, mc, bis))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


def wortlaut_auto(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wie wortlaut(), bricht den Normtext aber selbst um; marken = [(wortgruppe, cue)] (Wortgruppe in einer Zeile)."""
    f = F("Regular", size)
    worte, zeilen, cur = text.split(), [], ""
    for wd in worte:
        t = (cur + " " + wd).strip()
        if f.getlength(t) <= w - 56:
            cur = t
        else:
            zeilen.append(cur); cur = wd
    zeilen.append(cur)
    mk = []
    for wort, mc in marken:
        zi = [i for i, t in enumerate(zeilen) if wort in t]
        assert zi, f"Markierung {wort!r} läuft über einen Zeilenumbruch: {zeilen}"
        mk.append((zi[0], wort, mc))
    return wortlaut(x, y, w, zeilen, quelle, cue, marken=mk, size=size, bis=bis)


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folge 031/034) ------------------------------------
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


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def gu(cx, unten, hoehe, folge, **k):
    return fig("GU", cx, unten, hoehe, folge, **k)


def ing(cx, unten, hoehe, folge, **k):
    return fig("IN", cx, unten, hoehe, folge, **k)


def pe(cx, unten, hoehe, folge, **k):
    return fig("PE", cx, unten, hoehe, folge, **k)


def uw(cx, unten, hoehe, folge, **k):
    return fig("UW", cx, unten, hoehe, folge, **k)


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
MX = (X1 + X2) // 2                         # Requisit zwischen zwei Figuren
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
GU_F, IN_F, PE_F, UW_F = BLAU, GRUEN, PINK, WEISS     # Farben der Namensschilder (nach der Kleidung)


# A Fall: am Küchentisch ---------------------------------------------------------------------------------------------------
GU_A, IN_A = 470, 1450
GU_R1 = ("GU_redet_r", GU_A, BODEN, FH)
IN_R1 = ("IN_redet", IN_A, BODEN, FH)
TX0, TX1, TY = 720, 1200, 640                # Tischplatte
folie([(NULL, "Fall · Das gemeinsame Testament")], [
    hart(pl("Am Küchentisch", 70, 40, NULL, fill=GELB, size=40)),
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    hart(karte(TX0, TY, TX1 - TX0, 30, NULL, fill=HOLZ, rund=10, schatten=0, rand=5)),
    hart(linienzug([(TX0 + 40, TY + 30), (TX0 + 40, BODEN)], NULL, breite=10, farbe=INK)),
    hart(linienzug([(TX1 - 40, TY + 30), (TX1 - 40, BODEN)], NULL, breite=10, farbe=INK)),
    ficon("tabler", "heart", 960, 330, 110, beim("fall", "verheiratet"), fuell=PINK, bis="g1"),
    pl("seit über 40 Jahren verheiratet", 960, 360, beim("fall", "verheiratet"), fill=GELB, size=30, anker="m", bis="g1"),
    # Testament auf dem Tisch, Stift
    ficon("tabler", "file-text", 940, TY + 2, 120, beim("tisch", "Testament"), fuell=WEISS),
    ficon("tabler", "pencil", 1050, TY + 2, 70, beim("tisch", "schreibt"), fuell=GELB, bis="unter"),
    pl("mit der Hand", 960, 720, beim("tisch", "Hand"), fill=WEISS, size=28, anker="m", bis="unter"),
    ficon("tabler", "signature", 1060, TY + 2, 80, "unter", fuell=None),
    pl("beide unterschreiben", 960, 720, "unter", fill=GRUEN, size=28, anker="m"),
    # Günter (links, blickt nach rechts zu Ingrid)
    *[hart(e) for e in gu(GU_A, BODEN, FH, [(NULL, "ruhig_r")], bis="g1")],
    *redet("GU_redet_r", GU_A, BODEN, FH, "g1", "unter"),
    *gu(GU_A, BODEN, FH, [("unter", "froh_r")], erst="cut"),
    hart(ns("Günter", GU_A, BODEN, NULL, GU_F)),
    blase("sprech", 820, 300, "g1", 860, 230, inhalt=["Wir setzen uns gegenseitig", "als Alleinerben ein. Nach dem Tod",
                                                  "des Letzten von uns erben Petra", "und Uwe zu gleichen Teilen."],
          textsize=32, figur=GU_R1, bis="unter"),
    # Ingrid (rechts, blickt nach links zu Günter)
    *[hart(e) for e in ing(IN_A, BODEN, FH, [(NULL, "ruhig"), ("g1", "froh")], bis="i1")],
    *redet("IN_redet", IN_A, BODEN, FH, "i1", "tod"),
    hart(ns("Ingrid", IN_A, BODEN, NULL, IN_F)),
    blase("sprech", 700, 210, "i1", 1130, 230, inhalt=["Dann bleibt alles", "in der Familie."], textsize=38, figur=IN_R1),
])

# B Fall: drei Jahre später ------------------------------------------------------------------------------------------------
IN_B, PE_B, UW_B = 720, 1380, 1710
IN_R2 = ("IN_entschl_r", IN_B, BODEN, FH)
PE_R1 = ("PE_redet", PE_B, BODEN, FH)
folie([("tod", "Fall · Drei Jahre später"), ("i2", "Fall · Das neue Testament"), ("frage", "Fall · Die Frage")], [
    pl("Drei Jahre später", 70, 40, "tod", fill=GELB, size=40),
    linienzug([(40, BODEN), (1880, BODEN)], "tod", breite=7, farbe=INK),
    ficon("tabler", "calendar", 300, 360, 150, "tod", fuell=WEISS),
    ficon("tabler", "armchair", 310, BODEN - 2, 300, "tod", fuell=BLAU),
    *ing(IN_B, BODEN, FH, [("tod", "traurig_r"), ("erbt", "ruhig_r"), ("streit", "ernst_r")], bis="i2"),
    *redet("IN_entschl_r", IN_B, BODEN, FH, "i2", "p1"),
    *ing(IN_B, BODEN, FH, [("p1", "ernst_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Ingrid", IN_B, BODEN, "tod", IN_F),
    ficon("tabler", "home", IN_B, 300, 110, "erbt", fuell=GELB, bis="i2"),
    pl("erbt alles, nimmt an", IN_B, 315, beim("erbt", "nimmt"), fill=GELB, size=28, anker="m", bis="i2"),
    # Petra (Tochter) und Uwe (Sohn) rechts, blicken nach links zu Ingrid
    *pe(PE_B, BODEN, FH, [(beim("streit", "Petra"), "ernst")], bis="p1"),
    *redet("PE_redet", PE_B, BODEN, FH, "p1", "frage"),
    *pe(PE_B, BODEN, FH, [("frage", "sorge")], erst="cut"),
    ns("Petra, Tochter", PE_B, BODEN, beim("streit", "Petra"), PE_F),
    ficon("tabler", "heart-broken", 1050, 560, 100, beim("streit", "zerstritten"), fuell=ROT, bis="i2"),
    pl("zerstritten", 1050, 580, beim("streit", "zerstritten"), fill=ROT, size=28, anker="m", bis="i2"),
    *uw(UW_B, BODEN, FH, [(beim("uwe", "Uwe"), "froh"), ("frage", "denkt")]),
    ns("Uwe, Sohn", UW_B, BODEN, beim("uwe", "Uwe"), UW_F),
    pl("hilft im Alltag", UW_B, 300, beim("uwe", "hilft"), fill=WEISS, size=28, anker="m", bis="i2"),
    # das neue Testament
    ficon("tabler", "file-pencil", 1050, 640, 110, beim("i2", "neues"), fuell=WEISS),
    pl("neues Testament: Uwe alles", 1050, 660, beim("i2", "Uwe"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 760, 210, "i2", 800, 210, inhalt=["Ich schreibe ein neues Testament.", "Uwe soll alles bekommen."],
          textsize=36, figur=IN_R2, bis="p1"),
    blase("sprech", 700, 210, "p1", 1180, 210, inhalt=["Das hast du mit Papa", "anders ausgemacht!"], textsize=38,
          figur=PE_R1, bis="frage"),
    # Die Frage
    pl("Darf Ingrid ihr Testament noch ändern?", 960, 110, "frage", fill=PINK, size=36, anker="m"),
    pl("Oder sitzt sie in der Falle?", 960, 205, "frage2", fill=PINK, size=36, anker="m"),
])

# C Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Günter und Ingrid sind seit über 40 Jahren verheiratet. Günter schreibt mit der Hand und unterschreibt: „Wir setzen "
    "uns gegenseitig als Alleinerben ein. Nach dem Tod des Letzten von uns erben Petra und Uwe zu gleichen Teilen.“ "
    "Ingrid unterschreibt mit. Weitere Bestimmungen enthält das Testament nicht.",
    "Drei Jahre später stirbt Günter. Ingrid nimmt die Erbschaft an. Mit ihrer Tochter Petra hat sie sich inzwischen "
    "zerstritten, ihr Sohn Uwe hilft ihr im Alltag. Ingrid will ein neues Testament schreiben: Uwe soll alles bekommen.",
], "Kann Ingrid ihr Testament noch wirksam ändern?")

# D I. Wirksamkeit: §§ 2265, 2267 ------------------------------------------------------------------------------------------------
folie([("gt", "I. Wirksamkeit des gemeinschaftlichen Testaments"), ("p2265", "I. Wirksamkeit › nur Ehegatten, § 2265 BGB"),
       ("form", "I. Wirksamkeit › Form, § 2267 BGB")], rechts_frei([
    *tafel("gt", "I. Ist das Testament wirksam?"),
    ok(140, 210, beim("p2265", "Ehegatten"), gr=20), z("nur Ehegatten, § 2265 BGB", 185, 190, beim("p2265", "nur"), "Bold"),
    z("auch eingetragene Lebenspartner, § 10 Abs. 4 LPartG", 225, 245, "lp", size=31),
    nein(140, 335, "nicht", gr=20), z("nicht: ein unverheiratetes Paar", 185, 315, "nicht", size=32),
    z("Form, § 2267 BGB:", 185, 410, "form", "Bold"),
    z("einer schreibt eigenhändig und unterschreibt,", 225, 465, beim("form", "Einer"), size=32),
    z("der andere unterschreibt eigenhändig mit", 225, 515, "form2", size=32),
    ok(140, 620, "formok", gr=20), z("Günter schreibt, beide unterschreiben", 185, 600, "formok", size=32),
    blk(110, 690, 1040, 100, GRUEN, beim("formok", "Das"), [("Testament wirksam", "ExtraBold", 38, INK)]),
    ficon("tabler", "heart", MX, 320, 100, beim("p2265", "Ehegatten"), fuell=PINK, bis="form"),
    pl("Ehegatten", MX, 340, beim("p2265", "Ehegatten"), fill=GELB, size=26, anker="m", bis="form"),
    ficon("tabler", "signature", MX, 320, 100, "form", fuell=None),
    pl("eigenhändig", MX, 340, "form", fill=WEISS, size=26, anker="m"),
    *gu(X1, FB, FR, [("gt", "ruhig"), ("formok", "froh")]),
    ns("Günter", X1, FB, "gt", GU_F),
    *ing(X2, FB, FR, [("gt", "ruhig"), ("formok", "froh")], d=0.2),
    ns("Ingrid", X2, FB, "gt", IN_F, d=0.2),
]))

# E1 II. Inhalt: Wortlaut § 2269 Abs. 1 ------------------------------------------------------------------------------------------
W2269 = ("„Haben die Ehegatten in einem gemeinschaftlichen Testament, durch das sie sich gegenseitig als Erben einsetzen, "
         "bestimmt, dass nach dem Tode des Überlebenden der beiderseitige Nachlass an einen Dritten fallen soll, so ist im "
         "Zweifel anzunehmen, dass der Dritte für den gesamten Nachlass als Erbe des zuletzt versterbenden Ehegatten "
         "eingesetzt ist.“")
w2269, w2269_y = wortlaut_auto(80, 175, 1100, W2269, "§ 2269 Abs. 1 BGB", "p2269", marken=[
    ("gegenseitig als Erben", beim("w2269", "gegenseitig")), ("an einen Dritten", beim("w2269", "Dritten")),
    ("im Zweifel", beim("w2269b", "Zweifel")), ("gesamten Nachlass", beim("w2269b", "gesamten")),
    ("als Erbe", beim("w2269b", "Erbe")), ("des zuletzt versterbenden Ehegatten", beim("w2269b", "zuletzt"))])
folie([("inhalt", "II. Inhalt durch Auslegung"), ("p2269", "II. Inhalt › Auslegungsregel, § 2269 Abs. 1 BGB")], rechts_frei([
    *tafel("inhalt", "II. Was haben die beiden verfügt?"),
    *w2269,
    ficon("tabler", "file-text", MX, 320, 100, "inhalt", fuell=WEISS),
    pl("Auslegungsregel", MX, 340, beim("p2269", "Auslegungsregel"), fill=WEISS, size=26, anker="m"),
    *gu(X1, FB, FR, [("inhalt", "ruhig"), ("w2269b", "ernst")]),
    ns("Günter", X1, FB, "inhalt", GU_F),
    *ing(X2, FB, FR, [("inhalt", "denkt"), ("w2269b", "ruhig")], d=0.2),
    ns("Ingrid", X2, FB, "inhalt", IN_F, d=0.2),
]))

# E2 Einheitslösung -----------------------------------------------------------------------------------------------------------------
BY = 210
folie([("einheit", "II. Inhalt › Einheitslösung"), ("trenn", "II. Inhalt › Abgrenzung: Trennungslösung")], rechts_frei([
    *tafel("einheit", "Die Einheitslösung"),
    blk(110, BY, 290, 100, BLAU, "einheit", [("Günter", "ExtraBold", 38, INK)]),
    pfeil_ink(410, BY + 50, 470, BY + 50, beim("einheit", "Ingrid")),
    blk(480, BY, 290, 100, GRUEN, beim("einheit", "Ingrid"), [("Ingrid", "ExtraBold", 38, INK)]),
    z("Vollerbin", 560, BY + 115, beim("einheit", "Vollerbin"), "Bold", 32),
    pfeil_ink(780, BY + 50, 840, BY + 50, "schluss"),
    blk(850, BY, 300, 100, PINK, "schluss", [("Petra · Uwe", "ExtraBold", 36, INK)]),
    z("Schlusserben", 895, BY + 115, beim("schluss", "Schlusserben"), "Bold", 32),
    z("erben erst nach Ingrid,", 110, BY + 200, beim("schluss", "Sie"), size=34),
    z("dann aber alles (beiderseitiger Nachlass)", 110, BY + 250, beim("schluss", "dann"), size=34),
    z("Vor- und Nacherbschaft (Trennungslösung):", 110, BY + 350, "trenn", "Bold"),
    z("nur, wenn sich das aus dem Testament ergibt", 150, BY + 405, beim("trenn", "nur"), size=32),
    zit("OLG Düsseldorf, Beschl. v. 1.6.2012 – I-3 Wx 113/12, Rn. 34 f.", 150, BY + 460, beim("trenn", "nur")),
    ficon("tabler", "home", MX, 320, 110, beim("schluss", "alles"), fuell=GELB),
    pl("alles", MX, 340, beim("schluss", "alles"), fill=GELB, size=26, anker="m"),
    *ing(X1, FB, FR, [("einheit", "ruhig"), (beim("einheit", "Vollerbin"), "froh")]),
    ns("Ingrid", X1, FB, "einheit", IN_F),
    *pe(X2, FB, FR, [("einheit", "ruhig"), ("schluss", "froh")], d=0.2),
    ns("Petra", X2, FB, "einheit", PE_F, d=0.2),
]))

# F1 III. Wechselbezüglichkeit: Wortlaut § 2270 Abs. 1 ------------------------------------------------------------------------------
W2270 = ("„Haben die Ehegatten in einem gemeinschaftlichen Testament Verfügungen getroffen, von denen anzunehmen ist, dass "
         "die Verfügung des einen nicht ohne die Verfügung des anderen getroffen sein würde, so hat die Nichtigkeit oder der "
         "Widerruf der einen Verfügung die Unwirksamkeit der anderen zur Folge.“")
w2270, w2270_y = wortlaut_auto(80, 175, 1100, W2270, "§ 2270 Abs. 1 BGB", "p2270", marken=[
    ("nicht", beim("w2270", "nicht")), ("ohne die Verfügung des anderen", beim("w2270", "ohne")), ("Nichtigkeit", beim("w2270b", "Nichtigkeit")),
    ("Widerruf", beim("w2270b", "Widerruf")), ("Unwirksamkeit der anderen", beim("w2270b", "andere"))])
folie([("p2270", "III. Wechselbezüglichkeit, § 2270 Abs. 1 BGB")], rechts_frei([
    *tafel("p2270", "III. Die Falle: Wechselbezüglichkeit"),
    *w2270,
    ficon("tabler", "link", MX, 320, 110, "w2270", fuell=None),
    pl("wechselbezüglich", MX, 340, "w2270", fill=GELB, size=26, anker="m", bis="w2270b"),
    pl("reißt die andere mit", MX, 340, "w2270b", fill=ROT, size=26, anker="m"),
    *gu(X1, FB, FR, [("p2270", "ruhig"), ("w2270b", "ernst")]),
    ns("Günter", X1, FB, "p2270", GU_F),
    *ing(X2, FB, FR, [("p2270", "ruhig"), ("w2270b", "sorge")], d=0.2),
    ns("Ingrid", X2, FB, "p2270", IN_F, d=0.2),
]))

# F2 Auslegung und Vermutung § 2270 Abs. 2, 3 ----------------------------------------------------------------------------------------
folie([("ausl", "III. Wechselbezüglichkeit › erst Auslegung"), ("vermut", "III. Wechselbezüglichkeit › Vermutung, § 2270 Abs. 2 BGB"),
       ("abs3", "III. Wechselbezüglichkeit › § 2270 Abs. 3 BGB")], rechts_frei([
    *tafel("ausl", "Erst Auslegung, dann Vermutung"),
    z("1. Auslegung des Testaments", 110, 190, "ausl", "Bold"),
    z("2. bleibt es offen: Vermutung, § 2270 Abs. 2 BGB", 110, 255, "vermut", "Bold"),
    ok(140, 340, "zuw", gr=20), z("Günter wendet Ingrid sein Vermögen zu", 185, 320, "zuw", size=32),
    ok(140, 410, "kinder", gr=20), z("Ingrid setzt für ihr Überleben Petra und Uwe ein,", 185, 390, "kinder", size=32),
    z("die mit Günter verwandt sind", 225, 440, beim("kinder", "die"), size=32),
    blk(110, 510, 1040, 130, GELB, "wb", [("Ingrids Schlusserbeneinsetzung ist", "ExtraBold", 34, INK),
                                       ("wechselbezüglich zu Günters Einsetzung", "ExtraBold", 34, INK)]),
    zit("OLG Köln, Beschl. v. 12.1.2026 – 2 W 169/25, Rn. 19–21", 150, 655, "wb"),
    z("Abs. 3: nur Erbeinsetzungen, Vermächtnisse,", 110, 730, "abs3", size=31),
    z("Auflagen und die Wahl des anwendbaren Erbrechts", 150, 778, beim("abs3", "Auflagen"), size=31),
    ficon("tabler", "gift", MX, 320, 100, "zuw", fuell=GELB, bis="kinder"),
    pl("Zuwendung an Ingrid", MX, 340, "zuw", fill=GELB, size=26, anker="m", bis="kinder"),
    ficon("tabler", "users", MX, 320, 110, "kinder", fuell=PINK, bis="wb"),
    pl("Petra und Uwe", MX, 340, "kinder", fill=PINK, size=26, anker="m", bis="wb"),
    ficon("tabler", "link", MX, 320, 110, "wb", fuell=None),
    pl("wechselbezüglich", MX, 340, "wb", fill=GELB, size=26, anker="m"),
    *gu(X1, FB, FR, [("ausl", "ruhig"), ("zuw", "froh"), ("abs3", "ruhig")]),
    ns("Günter", X1, FB, "ausl", GU_F),
    *ing(X2, FB, FR, [("ausl", "denkt"), ("zuw", "froh"), ("wb", "sorge")], d=0.2),
    ns("Ingrid", X2, FB, "ausl", IN_F, d=0.2),
]))

# G1 IV. Bindung zu Lebzeiten beider: § 2271 Abs. 1, § 2296 -------------------------------------------------------------------------
folie([("leb", "IV. Bindung › zu Lebzeiten beider, § 2271 Abs. 1 BGB")], rechts_frei([
    *tafel("leb", "IV. Bindung: solange beide leben"),
    ok(140, 210, "wid", gr=20), z("Widerruf möglich, § 2271 Abs. 1 S. 1 BGB", 185, 190, "wid", "Bold"),
    z("nur durch notariell beurkundete Erklärung", 225, 245, beim("wid", "notariell"), size=32),
    z("gegenüber dem anderen Ehegatten, § 2296 Abs. 2 BGB", 225, 295, beim("wid", "gegenüber"), size=32),
    nein(140, 390, "allein", gr=20), z("neues Testament allein reicht nicht,", 185, 370, "allein", "Bold"),
    z("§ 2271 Abs. 1 S. 2 BGB", 225, 425, "allein", size=32),
    zit("BGH, Urt. v. 12.1.2011 – IV ZR 230/09, Rn. 10", 225, 480, "allein"),
    ficon("tabler", "file-certificate", MX, 320, 100, beim("wid", "notariell"), fuell=WEISS, bis="allein"),
    pl("notariell", MX, 340, beim("wid", "notariell"), fill=WEISS, size=26, anker="m", bis="allein"),
    ficon("tabler", "file-x", MX, 320, 100, "allein", fuell=WEISS),
    pl("reicht nicht", MX, 340, "allein", fill=ROT, size=26, anker="m"),
    *gu(X1, FB, FR, [("leb", "ruhig"), ("allein", "ernst")]),
    ns("Günter", X1, FB, "leb", GU_F),
    *ing(X2, FB, FR, [("leb", "ruhig"), ("wid", "denkt")], d=0.2),
    ns("Ingrid", X2, FB, "leb", IN_F, d=0.2),
]))

# G2 IV. Bindung nach dem ersten Todesfall: Wortlaut § 2271 Abs. 2 Satz 1 ----------------------------------------------------------
W2271 = ("„Das Recht zum Widerruf erlischt mit dem Tode des anderen Ehegatten; der Überlebende kann jedoch seine Verfügung "
         "aufheben, wenn er das ihm Zugewendete ausschlägt.“")
w2271, w2271_y = wortlaut_auto(80, 175, 1100, W2271, "§ 2271 Abs. 2 Satz 1 BGB", "tod2", marken=[
    ("erlischt", beim("w2271", "erlischt")), ("mit dem Tode des anderen Ehegatten", beim("w2271", "mit")),
    ("seine Verfügung", beim("w2271b", "seine")), ("Zugewendete ausschlägt", beim("w2271b", "Zugewendete"))], size=32)
folie([("tod2", "IV. Bindung › nach dem ersten Todesfall, § 2271 Abs. 2 BGB")], rechts_frei([
    *tafel("tod2", "IV. Bindung nach Günters Tod"),
    *w2271,
    ok(140, w2271_y + 75, "gebunden", gr=20), z("Ingrid ist grundsätzlich gebunden,", 185, w2271_y + 55, "gebunden", "Bold"),
    z("ähnlich wie bei einem Erbvertrag", 225, w2271_y + 110, beim("gebunden", "ähnlich"), size=32),
    zit("BGH, Urt. v. 25.5.2016 – IV ZR 205/15, Rn. 12", 225, w2271_y + 165, beim("gebunden", "ähnlich")),
    ficon("tabler", "armchair", 1400, FB - 2, 230, "tod2", fuell=BLAU),
    ficon("tabler", "lock", X2, 300, 90, "gebunden", fuell=GELB),
    pl("gebunden", X2, 320, "gebunden", fill=GELB, size=26, anker="m"),
    *ing(X2, FB, FR, [("tod2", "traurig"), ("w2271b", "denkt"), ("gebunden", "sorge")]),
    ns("Ingrid", X2, FB, "tod2", IN_F),
]))

# H Ausweg Ausschlagung -------------------------------------------------------------------------------------------------------------
folie([("aus", "IV. Bindung › Ausweg Ausschlagung?")], rechts_frei([
    *tafel("aus", "Ausweg: Ausschlagung?"),
    z("§ 2271 Abs. 2 S. 1 Hs. 2 BGB: Ausschlagung", 110, 190, "aus", "Bold"),
    zit("BGH, Urt. v. 12.1.2011 – IV ZR 230/09, Rn. 10 f., 15", 150, 245, "aus"),
    z("Preis: Ingrid verliert, was Günter ihr zugewendet hat", 150, 300, "preis", size=31),
    z("Frist: in der Regel sechs Wochen, § 1944 Abs. 1 BGB", 150, 355, "frist", size=31),
    z("ausgeschlossen nach Annahme, § 1943 BGB", 150, 410, "angen", size=31),
    nein(140, 510, "zu", gr=20), z("Ingrid hat angenommen: Weg versperrt", 185, 490, "zu", "Bold"),
    z("Sonderfälle, § 2271 Abs. 2 S. 2 BGB (etwa schwere", 110, 590, "sonder", size=30, farbe=TEXT),
    z("Verfehlungen eines Kindes): hier beiseite", 150, 635, beim("sonder", "lassen"), size=30, farbe=TEXT),
    ficon("tabler", "hourglass", MX, 320, 90, "frist", fuell=GELB, bis="zu"),
    pl("sechs Wochen", MX, 340, "frist", fill=GELB, size=26, anker="m", bis="zu"),
    ficon("tabler", "lock", MX, 320, 90, "zu", fuell=ROT),
    pl("versperrt", MX, 340, "zu", fill=ROT, size=26, anker="m"),
    *ing(X1, FB, FR, [("aus", "denkt"), ("preis", "sorge"), ("zu", "muede")]),
    ns("Ingrid", X1, FB, "aus", IN_F),
    *pe(X2, FB, FR, [("aus", "ernst")], d=0.2),
    ns("Petra", X2, FB, "aus", PE_F, d=0.2),
]))

# I V. Ergebnis -------------------------------------------------------------------------------------------------------------------
folie([("erg", "V. Ergebnis")], rechts_frei([
    *tafel("erg", "V. Ergebnis"),
    nein(140, 210, "e1", gr=20), z("Ingrids neues Testament: unwirksam,", 185, 190, "e1", "Bold"),
    z("soweit es Petra beeinträchtigt", 225, 245, beim("e1", "soweit"), size=32),
    zit("OLG Köln, Beschl. v. 12.1.2026 – 2 W 169/25, Rn. 23", 225, 300, beim("e1", "soweit")),
    blk(110, 380, 1040, 110, GELB, "e2", [("Nach Ingrids Tod erben Petra und Uwe je zur Hälfte", "ExtraBold", 33, INK)]),
    ficon("tabler", "file-x", MX, 320, 100, "e1", fuell=WEISS),
    pl("unwirksam", MX, 340, "e1", fill=ROT, size=26, anker="m", bis="e2"),
    pl("je zur Hälfte", MX, 340, beim("e2", "Hälfte"), fill=GELB, size=26, anker="m"),
    *pe(X1, FB, FR, [("erg", "ruhig"), (beim("e1", "soweit"), "froh")]),
    ns("Petra", X1, FB, "erg", PE_F),
    *uw(X2, FB, FR, [("erg", "ruhig"), ("e1", "denkt"), ("e2", "ruhig")], d=0.2),
    ns("Uwe", X2, FB, "erg", UW_F, d=0.2),
]))

# J Gestaltungstipp: Änderungsvorbehalt ---------------------------------------------------------------------------------------------
folie([("klausel", "Gestaltungstipp · Änderungsvorbehalt")], rechts_frei([
    *tafel("klausel", "Hätten sie das vermeiden können?"),
    z("Ja: mit einer Änderungsklausel", 110, 190, beim("klausel", "Ja"), "Bold"),
    karte(110, 260, 1040, 130, "kl2", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("„Der Überlebende darf die Verteilung", 140, 280, "kl2", size=34),
    z("unter den Kindern ändern.“", 140, 330, "kl2", size=34),
    ok(140, 470, "kl3", gr=20), z("Vorbehalt schließt die Bindung in seinem Umfang aus", 185, 450, "kl3", "Bold", 32),
    zit("OLG Köln, Beschl. v. 12.1.2026 – 2 W 169/25, Rn. 25", 225, 505, "kl3"),
    ok(140, 590, beim("kl4", "sogar"), gr=20), z("kann sogar decken: ein Kind bekommt alles", 185, 570, beim("kl4", "sogar"), "Bold", 32),
    zit("OLG Hamm, Beschl. v. 5.5.2022 – 10 W 40/21, Rn. 23, 27", 225, 625, beim("kl4", "sogar")),
    ficon("tabler", "file-pencil", MX, 320, 100, "kl2", fuell=WEISS),
    pl("Änderungsklausel", MX, 340, "kl2", fill=GRUEN, size=26, anker="m"),
    *gu(X1, FB, FR, [("klausel", "ruhig"), ("kl3", "froh")]),
    ns("Günter", X1, FB, "klausel", GU_F),
    *ing(X2, FB, FR, [("klausel", "denkt"), ("kl3", "froh")], d=0.2),
    ns("Ingrid", X2, FB, "klausel", IN_F, d=0.2),
]))

# K1 Ausblick: lebzeitige Schenkung, § 2287 analog -----------------------------------------------------------------------------------
HAUS = (beim("p2287", "Haus"), beim("p2287", "Uwe", ende=True))
folie([("schenk", "Ausblick · lebzeitige Schenkung, § 2287 BGB analog")], rechts_frei([
    *tafel("schenk", "Zu Lebzeiten bleibt Ingrid frei"),
    ok(140, 210, beim("schenk", "Als"), gr=20),
    z("Als Vollerbin darf sie über ihr Vermögen verfügen", 185, 190, beim("schenk", "Als"), size=32),
    zit("OLG Düsseldorf, Beschl. v. 1.6.2012 – I-3 Wx 113/12, Rn. 34", 225, 245, beim("schenk", "Als")),
    z("Schenkung an Uwe, um Petra zu beeinträchtigen,", 110, 320, beim("p2287", "Haus"), "Bold"),
    z("ohne eigenes lebzeitiges Interesse:", 150, 375, beim("p2287", "kein"), size=32),
    z("Petra kann nach Ingrids Tod ihren Anteil herausverlangen", 150, 430, beim("p2287", "kann"), size=31),
    blk(110, 510, 1040, 100, GELB, "bgh", [("§ 2287 BGB entsprechend", "ExtraBold", 38, INK)]),
    zit("BGH, Beschl. v. 26.10.2011 – IV ZR 72/11, Rn. 7, 11; Urt. v. 28.9.2016 – IV ZR 513/15, Rn. 7", 110, 625, "bgh",
        size=24),
    bewegt(ficon("tabler", "home", X2 - 20, 330, 110, HAUS[0], fuell=GELB, anim="cut"), *HAUS, -300),
    pl("Haus an Uwe", X2 - 20, 350, HAUS[1], fill=GELB, size=26, anker="m"),
    *ing(X1, FB, FR, [("schenk", "ruhig"), (beim("p2287", "Haus"), "entschl")]),
    ns("Ingrid", X1, FB, "schenk", IN_F),
    *uw(X2, FB, FR, [("schenk", "ruhig"), (HAUS[1], "froh"), ("bgh", "denkt")], d=0.2),
    ns("Uwe", X2, FB, "schenk", UW_F, d=0.2),
]))

# K2 Ausblick: Pflichtteil beim ersten Erbfall ---------------------------------------------------------------------------------------
folie([("pfl", "Ausblick · Pflichtteil beim ersten Erbfall, § 2303 BGB")], rechts_frei([
    *tafel("pfl", "Und beim ersten Erbfall?", h=520),
    nein(140, 210, beim("pfl", "Da"), gr=20), z("Petra und Uwe gingen leer aus", 185, 190, beim("pfl", "Da"), "Bold"),
    ok(140, 300, "pfl2", gr=20), z("Pflichtteil von Ingrid verlangen,", 185, 280, "pfl2", "Bold"),
    z("§ 2303 Abs. 1 BGB", 225, 335, beim("pfl2", "verlangen"), size=32),
    ficon("tabler", "cash-banknote", MX, 320, 110, "pfl2", fuell=GRUEN),
    pl("Pflichtteil", MX, 340, "pfl2", fill=GRUEN, size=26, anker="m"),
    *pe(X1, FB, FR, [("pfl", "ernst"), ("pfl2", "ruhig")]),
    ns("Petra", X1, FB, "pfl", PE_F),
    *uw(X2, FB, FR, [("pfl", "denkt"), ("pfl2", "ruhig")], d=0.2),
    ns("Uwe", X2, FB, "pfl", UW_F, d=0.2),
]))

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Wechselbezüglichkeit je Verfügung"), ("tipp2", "Klausurtipp · erst Auslegung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Wechselbezüglichkeit je Verfügung prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("im Verhältnis zur Verfügung des anderen", 200, 260, beim("tipp", "Verhältnis"), size=34),
    z("Erst auslegen:", 110, 370, "tipp2", "Bold", 36),
    z("Vermutung, § 2270 Abs. 2, nur ohne Auslegungsergebnis", 150, 430, beim("tipp2", "Die"), size=32),
    z("Viel mehr Vermögen eines Ehegatten kann", 150, 520, "tipp3", size=34),
    z("gegen die Wechselbezüglichkeit sprechen", 150, 575, beim("tipp3", "gegen"), size=34),
    zit("BGH, Beschl. v. 26.10.2011 – IV ZR 72/11, Rn. 8", 150, 635, beim("tipp3", "gegen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# M Klausurschema ----------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Wer beerbt Ingrid?"), 110, 90, "sch", 46),
    z("I. Wirksamkeit des gemeinschaftlichen Testaments, §§ 2265, 2267 BGB", K1, 190, "s1", "Bold", 34, rechts=1820),
    z("II. Inhalt durch Auslegung: Einheitslösung, § 2269 Abs. 1 BGB", K1, 260, "s2", "Bold", 34, rechts=1820),
    z("III. Wechselbezüglichkeit, § 2270 BGB", K1, 330, "s3", "Bold", 34, rechts=1820),
    z("erst Auslegung, dann Vermutung (§ 2270 Abs. 2 BGB)", K2, 385, "s4", size=32, rechts=1820),
    z("IV. Bindung des Überlebenden, § 2271 BGB", K1, 465, "s5", "Bold", 34, rechts=1820),
    z("1. kein Widerruf zu Lebzeiten beider (§ 2271 Abs. 1, § 2296 BGB)", K2, 520, "s6", size=32, rechts=1820),
    z("2. Widerrufsrecht mit dem Tod erloschen (§ 2271 Abs. 2 S. 1 Hs. 1 BGB)", K2, 570, beim("s7", "Widerrufsrecht"), size=32,
      rechts=1820),
    z("3. keine Ausschlagung, kein Änderungsvorbehalt", K2, 620, "s8", size=32, rechts=1820),
    z("V. Ergebnis: neues Testament unwirksam, soweit es beeinträchtigt", K1, 700, "s9", "Bold", 34, rechts=1820),
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nach dem ersten Todesfall ist der Überlebende", 0)],
                 [("an wechselbezügliche Verfügungen ", 0), ("gebunden.", "a")]], 750, 320, 44,
                "merke", {"a": beim("merke", "gebunden")}),
    *markertext([[("Lösen kann er sich grundsätzlich nur", 0)], [("durch ", 0), ("Ausschlagung,", "b")],
                 [("es sei denn, das Testament behält", 0)], [("ihm die Änderung vor.", 0)]],
                750, 520, 40, "mk2", {"b": beim("mk2", "Ausschlagung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
