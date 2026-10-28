"""Folge 249 · Gefahr im Verzug: Durchsuchung ohne Richter? (Art. 13 II GG) – Serienstandard Open Peeps (Katzenkönig).
Fall: Sonntag, 19 Uhr. Kommissar Bader und Kommissarin Ebner (Ermittlungspersonen) wollen ohne Beschluss Wohnung und Atelier
von Ines durchsuchen, „ein Richter sei am Sonntagabend nicht zu erreichen“; Anzeige wegen gefälschter Konzertkarten um 15 Uhr,
niemand hat den (erreichbaren) Bereitschaftsdienst zu erreichen versucht, Ines ahnt nichts; Durchsuchung trotz Widerspruch,
Fund eines Stapels Konzertkarten. Szenen laut ../SZENENPLAN.md: A1 Wohnungstür (Treppenhaus, Abendlicht der Lampe; 19 Uhr ist
Tageszeit, daher Cremegrund), A2 was vorher geschah (Anzeige, Konto, Atelier, Bereitschaftsrichterin zu Hause), A3 Atelier
(Durchsuchung, Fund), B Sachverhalt, C Schutzbereich/Eingriff (Wortlautkarte Art. 13 Abs. 1), D Rechtfertigung (Wortlautkarte
Art. 13 Abs. 2), E Anforderungen (BVerfGE 103, 142), F Bereitschaftsdienst (Tagesband), G § 105 StPO (Wortlautkarte),
H Lösung (Tagesband mit Marke 19 Uhr), I Gegenfall und Verwertung (Verweis 221), J Klausurtipp (Lexi), K Schema, L Merksatz.
Keine Gewalt, keine Waffen, keine Abzeichen oder Wappen, kein Rammbock, kein Richterhammer (Gericht als Säulengebäude).
Zwei Handlungsgeräusche (Klingel, Tür; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 151 (gemeinsame Dateien
unverändert); neu bzw. angepasst: flurboden(), deckenlampe(), tisch(), tagesband(marke=…). Zahlen auf Tafeln, Pillen und
Blasen als Ziffern. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026; amtlich „im Verzuge“ in Art. 13 GG)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_249/"

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e)
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
TUERKIS_ = (127, 214, 208, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (Mindestgröße 26 px, mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_249/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine: Treppenhaus, Atelier, Wohnzimmer der Richterin (Palettenflächen, Tuschekontur) ------------
BODEN_T = (214, 206, 192, 255)               # Fliesen im Treppenhaus
BODEN_H = (222, 196, 160, 255)               # Holzboden im Atelier / Wohnzimmer
F_O, F_U = 930, 1000                         # Bodenfläche (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def flurboden(cue, farbe, fugen=True):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=farbe)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    if fugen:
        for x in range(100, 1860, 220):
            dr.line(((x + 30) * s, 6 * s, (x - 10) * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def deckenlampe(cx, cue, boden=F_O):
    """Deckenlampe (Tabler bulb, gelb) mit Lichtkegel bis zum Boden (Abendlicht, Lampe brennt)."""
    birne = ficon("tabler", "bulb", cx, 150, 90, cue, fuell=GELB, anim="cut")
    kabel = linienzug([(cx, 30), (cx, 70)], cue, breite=5)
    kegel = lichtkegel(cx, 150, 260, boden, cue)
    return [hart(kegel), hart(kabel), birne]


def tisch(x0, x1, y, cue, fill=HOLZ):
    """Arbeitstisch (Platte + zwei Beine) bis zum Boden."""
    return [karte(x0, y, x1 - x0, 40, cue, fill=fill, rund=10, schatten=4, rand=4, anim="cut"),
            linienzug([(x0 + 50, y + 42), (x0 + 50, F_O)], cue, breite=10),
            linienzug([(x1 - 50, y + 42), (x1 - 50, F_O)], cue, breite=10)]


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"IN": "Ines", "BA": "Kommissar Bader", "EB": "Kommissarin Ebner", "RI": "Bereitschaftsrichterin"}
NFARBE = {"IN": TUERKIS_, "BA": BLAU, "EB": BLAUHELL, "RI": LILA}


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def tagesband(x0, y0, w, h, cue_tag, cue_nacht, marke=None):
    """Band 0–24 Uhr: Tageszeit 6–21 Uhr grün (uneingeschränkte Erreichbarkeit), Nachtzeit grau-blau.
    marke = (cue, Stunde, Text): senkrechter Strich mit Pille (z. B. Sonntag, 19 Uhr)."""
    px = lambda std: x0 + w * std / 24
    els = [karte(x0, y0, w, h, cue_tag, fill=(200, 205, 225, 255), rund=12, schatten=4, rand=4)]
    els.append(karte(int(px(6)), y0, int(px(21) - px(6)), h, cue_tag, fill=GRUEN, rund=12, schatten=0, rand=4))
    for std in (0, 6, 21, 24):
        dx = {0: 0, 24: -40}.get(std, -40)
        els.append(z(f"{std} Uhr" if std in (6, 21) else f"{std}", int(px(std)) + dx, y0 + h + 10, cue_tag, "Bold", 28))
    els.append(z("Tag: Richter erreichbar", int(px(7)), y0 + 12, cue_tag, "Bold", 30))
    if cue_nacht:
        els.append(z("Nacht", int(px(21.4)), y0 + 12, cue_nacht, "Bold", 30))
        els.append(z("Nacht", int(px(1.2)), y0 + 12, cue_nacht, "Bold", 30))
    if marke:
        c, std, txt = marke
        els.append(linienzug([(px(std), y0 - 30), (px(std), y0 + h + 4)], c, breite=8, farbe=DROT))
        els.append(pl(txt, int(px(std)), y0 - 82, c, fill=GELB, size=28, anker="m"))
    return els


P = "Art. 13 GG"

# ===========================================================================================================================
# A1 Fall: Sonntag, 19 Uhr, an der Wohnungstür (Tageszeit im Sinne von BVerfGE 151, 67: Cremegrund, Lampe brennt)
# ===========================================================================================================================
TX = 1060                                   # Wohnungstür
HX, BX, EX = 1300, 720, 380                 # Ines (vor ihrer Tür, blickt nach links), Bader, Ebner (blicken nach rechts)
KL = szene(ficon("tabler", "bell-ringing", 1350, 560, 70, "klingel", fuell=GELB, bis="tuer"), "249klingel*", 0.9, 0.0)
TUER_ZU = ficon("tabler", "door", TX, F_O + 8, 800, NULL, fuell=HOLZ, bis="tuer", anim="cut")
TUER_AUF = szene(ficon("tabler", "door", TX, F_O + 8, 800, "tuer", fuell=(255, 238, 180, 255), anim="cut"), "249tuer*", 0.7, 0.0)
folie([(NULL, "Fall · Sonntag, 19 Uhr"), ("klingel", "Fall · Es klingelt"), ("tuer", "Fall · Kommissar Bader, Kommissarin Ebner"),
       ("b1", "Fall · „Kein Richter zu erreichen“"), ("i1", "Fall · Bereitschaftsdienst?"), ("b2", "Fall · „Das dauert zu lange“")], [
    hart(flurboden(NULL, BODEN_T)),
    *deckenlampe(560, NULL),
    hart(ficon("tabler", "clock-hour-7", 200, 420, 130, NULL, fuell=WEISS, anim="cut")),
    hart(TUER_ZU),
    hart(pl("Sonntag, 19 Uhr: ein Mietshaus", 70, 30, NULL, fill=GELB, size=40)),
    KL,
    pl("Es klingelt.", 1350, 470, "klingel", fill=WEISS, size=28, anker="m", bis="tuer"),
    TUER_AUF,
    *fig("IN", HX, FU, FH, [("tuer", "schreck"), ("b1", "sorge")], bis="i1", erst="pop"),
    *redet("IN_redet", HX, FU, FH, "i1", "b2"),
    *fig("IN", HX, FU, FH, [("b2", "fest")], bis="vorher", erst="cut"),
    ns("Ines", HX, FU, "tuer", TUERKIS_, d=0.1),
    *redet("BA_redet_r", BX, FU, FH, "b1", "i1"),
    *fig("BA", BX, FU, FH, [(beim("tuer", "Kommissar"), "ernst_r")], bis="b1", erst="pop"),
    *fig("BA", BX, FU, FH, [("i1", "denkt_r")], bis="b2", erst="cut"),
    *redet("BA_redet_r", BX, FU, FH, "b2", "vorher"),
    ns("Kommissar Bader", BX, FU, beim("tuer", "Kommissar"), BLAU, d=0.1),
    *fig("EB", EX, FU, FH, [(beim("tuer", "Kommissarin"), "ruhig_r"), ("b2", "still_r")], erst="pop"),
    ns("Kommissarin Ebner", EX, FU, beim("tuer", "Kommissarin"), BLAUHELL, d=0.1),
    blase("sprech", 900, 330, "b1", 600, 240, inhalt=["Wir müssen sofort Ihre Wohnung", "und Ihr Atelier durchsuchen.",
          "Ein Richter ist am Sonntagabend", "nicht zu erreichen."], textsize=34, figur=("BA_redet_r", BX, FU, FH), bis="i1"),
    blase("sprech", 760, 250, "i1", 1440, 235, inhalt=["Ohne Beschluss? Dann rufen Sie", "doch den Bereitschaftsdienst an!"],
          textsize=34, figur=("IN_redet", HX, FU, FH), bis="b2"),
    blase("sprech", 820, 250, "b2", 640, 255, inhalt=["Das dauert zu lange. Bis dahin", "haben Sie alles verschwinden lassen."],
          textsize=34, figur=("BA_redet_r", BX, FU, FH)),
])

# ===========================================================================================================================
# A2 Fall: was vorher geschah (Anzeige 15 Uhr, Konto, Atelier, Bereitschaftsdienst, Ines ahnt nichts)
# ===========================================================================================================================
def beistelltisch(cx, cue, anim="cut"):
    """Kleiner Beistelltisch mit Diensttelefon (Bereitschaftsrichterin zu Hause)."""
    return [karte(cx - 90, 790, 180, 30, cue, fill=HOLZ, rund=8, schatten=3, rand=4, anim=anim),
            linienzug([(cx, 822), (cx, F_O)], cue, breite=10),
            ficon("tabler", "phone", cx, 792, 80, cue, fuell=WEISS, anim=anim)]


folie([("vorher", "Fall · Was vorher geschah"), ("anz", "Fall · 15 Uhr: die Anzeige"), ("konto", "Fall · Konto von Ines"),
       ("atelier", "Fall · Ines, Grafikerin mit Atelier"), ("ruf", "Fall · Bereitschaftsdienst: kein Versuch"),
       ("richterin", "Fall · Die Richterin war erreichbar"), ("ahnt", "Fall · Ines weiß von nichts")], [
    flurboden("vorher", BODEN_H, fugen=False),
    pl("Was vorher geschah", 70, 30, "vorher", fill=GELB, size=40),
    ficon("tabler", "clock-2", 1590, 260, 120, "vorher", fuell=WEISS, bis="konto"),
    ficon("tabler", "ticket", 1780, 260, 150, beim("anz", "Eintrittskarten"), fuell=GELB, bis="konto"),
    pl("15 Uhr: Anzeige – Eintrittskarten gefälscht", 70, 105, beim("anz", "fünfzehn"), fill=WEISS, size=32),
    pl("online gekauft, bezahlt auf ein Konto von Ines", 70, 172, "konto", fill=WEISS, size=32),
    ficon("tabler", "credit-card", 1680, 260, 170, "konto", fuell=BLAU, bis="atelier"),
    pl("Ines: Grafikerin, Atelier neben der Wohnung", 70, 239, "atelier", fill=WEISS, size=32),
    ficon("tabler", "palette", 1680, 260, 150, "atelier", fuell=GELB, bis="ruf"),
    *neinz("Bereitschaftsdienst: niemand hat es versucht", 312, "ruf", "Bold", 32, x=115),
    ficon("tabler", "building-bank", 1680, 260, 170, "ruf", fuell=BLAU, bis="richterin"),
    *beistelltisch(1420, "richterin", anim="pop"),
    pl("Bereitschaftsrichterin: erreichbar", 1600, 175, "richterin", fill=GRUEN, size=30, anker="m"),
    pl("kein Hinweis, dass Ines von der Anzeige weiß", 70, 372, "ahnt", fill=WEISS, size=32),
    *fig("IN", 700, FU, FH, [("atelier", "ruhig_r"), ("ahnt", "froh_r")], erst="pop"),
    ns("Ines", 700, FU, "atelier", TUERKIS_, d=0.1),
    ficon("tabler", "palette", 930, 920, 110, "atelier", fuell=GELB),
    *fig("RI", 1650, FU, FH, [("richterin", "ruhig"), ("ahnt", "wartet")], erst="pop"),
    ns("Bereitschaftsrichterin", 1650, FU, "richterin", LILA, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: Durchsuchung von Wohnung und Atelier, Fund der Konzertkarten
# ===========================================================================================================================
KARTEN = [ficon("tabler", "ticket", 820 + 14 * i, 690 - 20 * i, 150, (beim("fund", "Stapel")[0], round(beim("fund", "Stapel")[1] + 0.1 * i, 3)),
                fuell=GELB) for i in range(4)]
folie([("wider", "Fall · Ines widerspricht"), (beim("wider", "Trotzdem"), "Fall · Durchsuchung von Wohnung und Atelier"),
       ("fund", "Fall · Ein Stapel Konzertkarten"), ("frage", "Fall · Die Frage")], [
    hart(flurboden("wider", BODEN_H, fugen=False)),
    *deckenlampe(800, "wider"),
    *[hart(e) for e in tisch(520, 1100, 700, "wider")],
    hart(ficon("tabler", "printer", 640, 702, 150, "wider", fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "palette", 1000, 702, 110, "wider", fuell=GELB, anim="cut")),
    pl("Ines widerspricht", 70, 30, "wider", fill=HELLROT, size=36),
    pl("… trotzdem: Durchsuchung von Wohnung und Atelier", 70, 105, beim("wider", "Trotzdem"), fill=WEISS, size=32),
    *KARTEN,
    pl("Fund: ein Stapel Konzertkarten", 70, 180, beim("fund", "Stapel"), fill=GELB, size=32),
    ring(845, 640, 150, 105, beim("fund", "Konzertkarten"), bis="frage"),
    pl("Verletzt die Durchsuchung Ines in ihrem", 70, 270, "frage", fill=PINK, size=36),
    pl("Grundrecht aus Art. 13 GG?", 70, 340, "frage", fill=PINK, size=36),
    *fig("IN", 1650, FU, FH, [("wider", "fest"), ("fund", "sorge"), ("frage", "denkt")], erst="cut"),
    ns("Ines", 1650, FU, "wider", TUERKIS_),
    *fig("BA", 1300, FU, FH, [("wider", "ernst_r"), (beim("fund", "Stapel"), "denkt")], erst="cut"),
    ns("Kommissar Bader", 1300, FU, "wider", BLAU),
    *fig("EB", 300, FU, FH, [("wider", "ernst_r"), ("fund", "denkt_r")], erst="cut"),
    ns("Kommissarin Ebner", 300, FU, "wider", BLAUHELL),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_249(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.3)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_249("sv", [
    "Sonntag, 19 Uhr: Kommissar Bader und Kommissarin Ebner, Ermittlungspersonen der Staatsanwaltschaft, klingeln bei Ines. "
    "Sie wollen sofort ihre Wohnung und ihr Atelier durchsuchen; ein Richter sei am Sonntagabend nicht zu erreichen. "
    "Einen Beschluss haben sie nicht.",
    "Um 15 Uhr hatte ein Konzertbesucher angezeigt, dass seine online gekauften Eintrittskarten gefälscht sind; bezahlt hatte "
    "er auf ein Konto von Ines. Ines ist Grafikerin und arbeitet in einem Atelier neben ihrer Wohnung. Niemand hat versucht, "
    "den Bereitschaftsdienst des Amtsgerichts zu erreichen, obwohl die Bereitschaftsrichterin an diesem Abend erreichbar war. "
    "Nichts deutet darauf hin, dass Ines von der Anzeige weiß.",
    "Ines widerspricht. Die beiden durchsuchen trotzdem und finden im Atelier einen Stapel Konzertkarten.",
], "Verletzt die Durchsuchung Ines in ihrem Grundrecht aus Art. 13 GG?")

# ===========================================================================================================================
# C 1. Schutzbereich und 2. Eingriff (Wortlautkarte Art. 13 Abs. 1 GG)
# ===========================================================================================================================
w13a, w13a_y = wortlaut(80, 160, 1100, ["„(1) Die Wohnung ist unverletzlich. …“"], "Art. 13 Abs. 1 GG", "art13",
                        marken=[(0, "unverletzlich", beim("art13", "unverletzlich"))], size=34)
PS_, PE_ = f"{P} › 1. Schutzbereich", f"{P} › 2. Eingriff"
y0 = w13a_y + 30
folie([("art13", f"{PS_} › Die Wohnung ist unverletzlich"), ("raum", f"{PS_} › räumliche Sphäre des Privatlebens"),
       ("weit", f"{PS_} › weiter Wohnungsbegriff"), ("gesch", f"{PS_} › auch Geschäftsräume"),
       ("eingr", f"{PE_} › Durchsuchung"), ("schwer", f"{PE_} › schwerer Eingriff")], rechts_frei([
    *tafel("art13", "1. Schutzbereich, 2. Eingriff", h=840),
    *w13a,
    z("Wohnung: räumliche Sphäre, in der sich", 110, y0, "raum", "Bold", 32),
    z("das Privatleben entfaltet", 110, y0 + 46, beim("raum", "Privatleben"), "Bold", 32),
    zit("BVerfG, Beschl. v. 30.9.2025 – 2 BvR 460/25, Rn. 28", 110, y0 + 94, beim("raum", "entfaltet")),
    z("weit:", 110, y0 + 150, "weit", "ExtraBold", 32),
    *okz("auch Arbeits- und Geschäftsräume (Atelier)", y0 + 150, "gesch", size=32, x=250),
    zit("BVerfGE 109, 279, Rn. 142; 2 BvR 460/25, Rn. 28", 250, y0 + 198, beim("gesch", "Atelier")),
    z("Eingriff: Durchsuchung = gezieltes Suchen des", 110, y0 + 265, "eingr", "Bold", 32),
    z("Staates nach etwas, das die Inhaberin nicht", 110, y0 + 311, beim("eingr", "gezielte"), size=32),
    z("von sich aus offenlegen oder herausgeben will", 110, y0 + 357, beim("eingr", "gezielte"), size=32),
    zit("2 BvR 460/25, Rn. 36", 110, y0 + 405, beim("eingr", "herausgeben")),
    blk(110, y0 + 455, 1040, 76, HELLROT, "schwer", [("schwerer Eingriff in Art. 13 Abs. 1 GG", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, Rn. 26 (BVerfGE 103, 142)", 110, y0 + 545, beim("schwer", "schwer")),
    *requisit([("art13", ("tabler", "home", 110, LILA), "Art. 13 Abs. 1 GG", GELB),
               ("raum", ("tabler", "home", 110, LILA), "Privatleben", WEISS),
               ("gesch", ("tabler", "palette", 110, GELB), "Atelier: geschützt", GRUEN),
               ("eingr", ("tabler", "search", 100, WEISS), "Durchsuchung", WEISS),
               ("schwer", ("tabler", "alert-triangle", 100, HELLROT), "schwerer Eingriff", HELLROT)]),
    *stehend("IN", FX, [("art13", "ruhig"), ("gesch", "froh"), ("eingr", "sorge")]),
]))

# ===========================================================================================================================
# D 3. Rechtfertigung: Art. 13 Abs. 2 GG (Wortlautkarte)
# ===========================================================================================================================
W13 = ["„(2) Durchsuchungen dürfen nur durch den Richter, bei Gefahr",
       "im Verzuge auch durch die in den Gesetzen vorgesehenen anderen",
       "Organe angeordnet und nur in der dort vorgeschriebenen Form",
       "durchgeführt werden.“"]
w13, w13_y = wortlaut(80, 160, 1100, W13, "Art. 13 Abs. 2 GG", "abs2", marken=[
    (0, "nur durch den Richter", beim("richter", "Richter")), (0, "bei Gefahr", beim("giv", "Gefahr")),
    (1, "im Verzuge", beim("giv", "Gefahr")), (1, "anderen", beim("giv", "anderen")),
    (2, "Organe", beim("giv", "Organe"))], size=32)
PR = f"{P} › 3. Rechtfertigung"
folie([("abs2", f"{PR} › Art. 13 Abs. 2 GG"), ("richter", f"{PR} › Richtervorbehalt"),
       ("giv", f"{PR} › Gefahr im Verzuge: andere Organe"), ("regel", f"{PR} › Richter: Regel, sonst Ausnahme"),
       ("neutral", f"{PR} › vorbeugende, neutrale Kontrolle"), ("eng", f"{PR} › Gefahr im Verzug: eng")], rechts_frei([
    *tafel("abs2", "3. Rechtfertigung: Art. 13 Abs. 2 GG", h=w13_y + 360 - 60, size=44),
    *w13,
    blk(110, w13_y + 30, 1040, 80, GELB, "regel", [("Richter: die Regel · ohne Richter: die Ausnahme", "ExtraBold", 34, INK)]),
    zit("BVerfGE 103, 142, Rn. 31", 110, w13_y + 122, beim("regel", "Ausnahme")),
    z("Richter prüft vorher – unabhängig und neutral", 110, w13_y + 175, "neutral", "Bold", 32),
    zit("BVerfGE 103, 142, Rn. 27", 110, w13_y + 223, beim("neutral", "neutral")),
    blk(110, w13_y + 268, 1040, 76, HELLROT, "eng", [("Gefahr im Verzug: eng auszulegen", "ExtraBold", 34, INK)]),
    zit("Rn. 32", 1060, w13_y + 290, beim("eng", "eng"), rechts=1170),
    *requisit([("abs2", ("tabler", "scale", 110, WEISS), "Art. 13 Abs. 2 GG", GELB),
               ("richter", ("tabler", "building-bank", 120, BLAU), "Richtervorbehalt", WEISS),
               ("giv", ("tabler", "hourglass", 100, GELB), "Gefahr im Verzuge", WEISS),
               ("regel", ("tabler", "scale", 110, WEISS), "Regel und Ausnahme", GELB),
               ("neutral", ("tabler", "eye", 110, WEISS), "Kontrolle vorher", WEISS),
               ("eng", ("tabler", "hourglass", 100, GELB), "eng auszulegen", HELLROT)]),
    *stehend("IN", X1, [("abs2", "ruhig"), ("regel", "denkt")]),
    *stehend("BA", X2, [("abs2", "ernst"), ("eng", "still")]),
]))

# ===========================================================================================================================
# E Anforderungen an Gefahr im Verzug (BVerfGE 103, 142)
# ===========================================================================================================================
PG = f"{P} › 3. Rechtfertigung › Gefahr im Verzug"
RN = 1035                                   # Spalte der Randnummern
GZ = [("def", 230, [("nur wenn schon die vorherige Einholung der", "Bold"),
                    ("richterlichen Anordnung den Erfolg gefährden würde", "Bold")], "Rn. 34"),
      ("tats", 345, [("Tatsachen des Einzelfalls – keine Spekulation,", "Regular"),
                     ("keine fallunabhängige Vermutung", "Regular")], "Rn. 38"),
      ("versuch", 460, [("regelmäßig zuerst versuchen, einen Richter", "Regular"),
                        ("zu erreichen", "Regular")], "Rn. 40"),
      ("selbst", 575, [("Eile nicht selbst herbeiführen", "Regular")], "Rn. 39"),
      ("doku", 640, [("Gründe in den Akten dokumentieren –", "Regular"),
                     ("auch den Versuch, den Richter zu erreichen", "Regular")], "Rn. 54")]
els_g = [*tafel("def", "Wann liegt Gefahr im Verzug vor?", h=780, size=44),
         zit("BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00 (BVerfGE 103, 142)", 110, 165, "def")]
for i, (c, y, zeilen, rn) in enumerate(GZ):
    els_g.append(z(f"{i + 1}.", 110, y, c, "ExtraBold", 32))
    for j, (t, st) in enumerate(zeilen):
        cz = c if j == 0 or i else beim("def", "richterlichen")
        els_g.append(z(t, 160, y + j * 46, cz, st, 32, rechts=RN - 10 if j == len(zeilen) - 1 else 1170))
    els_g.append(zit(rn, RN, y + 4 + (len(zeilen) - 1) * 46, c if i else beim("def", "richterlichen"), rechts=1170))
folie([("def", f"{PG} › Erfolg gefährdet"), ("tats", f"{PG} › Tatsachen des Einzelfalls"),
       ("versuch", f"{PG} › zuerst den Richter versuchen"), ("selbst", f"{PG} › nicht selbst herbeigeführt"),
       ("doku", f"{PG} › Dokumentation")], rechts_frei([
    *els_g,
    *requisit([("def", ("tabler", "hourglass", 100, GELB), "Erfolg gefährdet?", WEISS),
               ("tats", ("tabler", "list-check", 100, WEISS), "Tatsachen, keine Spekulation", WEISS),
               ("versuch", ("tabler", "phone-call", 100, WEISS), "Richter erreichen", WEISS),
               ("selbst", ("tabler", "clock", 100, WEISS), "nicht selbst herbeiführen", HELLROT),
               ("doku", ("tabler", "file-text", 100, WEISS), "in den Akten", WEISS)]),
    *stehend("BA", X1, [("def", "ernst"), ("tats", "denkt"), ("doku", "still")]),
    *stehend("EB", X2, [("def", "ruhig"), ("versuch", "denkt")]),
]))

# ===========================================================================================================================
# F Bereitschaftsdienst: Tagesband 6–21 Uhr (BVerfGE 103, 142, Rn. 40; BVerfGE 151, 67)
# ===========================================================================================================================
PB = f"{PG} › Bereitschaftsdienst"
folie([("bereit", f"{PB}"), ("tag", f"{PB} › bei Tage: 6 bis 21 Uhr"), ("nacht", f"{PB} › nachts nach Bedarf"),
       ("abstr", f"{PB} › abstrakter Hinweis genügt nicht")], rechts_frei([
    *tafel("bereit", "Ist ein Richter erreichbar?", h=800, size=46),
    z("Gerichte müssen einen Ermittlungsrichter erreichbar", 110, 175, "bereit", "Bold", 32),
    z("halten – auch durch einen Bereitschaftsdienst", 110, 223, beim("bereit", "Bereitschaftsdienst"), "Bold", 32),
    zit("BVerfGE 103, 142, Rn. 40", 110, 271, beim("bereit", "Bereitschaftsdienst")),
    *tagesband(110, 340, 1040, 70, "tag", "nacht"),
    z("bei Tage, ganzjährig 6 bis 21 Uhr: uneingeschränkt,", 110, 480, beim("tag", "Bei"), size=32),
    z("auch außerhalb der Dienststunden", 110, 526, beim("tag", "außerhalb"), size=32),
    zit("BVerfG, Beschl. v. 12.3.2019 – 2 BvR 675/14, Rn. 58 (BVerfGE 151, 67)", 110, 572, beim("tag", "ganzjährig")),
    z("nachts: nur bei Bedarf über den Ausnahmefall hinaus", 110, 625, "nacht", size=32),
    zit("BVerfGE 151, 67, Rn. 58, 67", 110, 671, beim("nacht", "Bedarf")),
    *neinz("„gewöhnlich kein Richter erreichbar“: reicht nicht", 720, "abstr", "Bold", 32, x=160),
    zit("BVerfGE 103, 142, Rn. 40; BVerfGE 151, 67, Rn. 56", 160, 768, beim("abstr", "erreichen")),
    *requisit([("bereit", ("tabler", "building-bank", 120, BLAU), "Bereitschaftsdienst", GELB),
               ("tag", ("tabler", "sun", 110, GELB), "6 bis 21 Uhr", GRUEN),
               ("nacht", ("tabler", "moon", 100, GELB), "nachts nach Bedarf", WEISS),
               ("abstr", ("tabler", "phone-off", 100, WEISS), "abstrakter Hinweis", HELLROT)]),
    *beistelltisch(1340, "bereit"),
    *stehend("RI", FX + 60, [("bereit", "ruhig"), ("tag", "froh"), ("abstr", "wartet")]),
]))

# ===========================================================================================================================
# G 4. Einfaches Recht: § 105 Abs. 1 S. 1 StPO (Wortlautkarte)
# ===========================================================================================================================
W105 = ["„(1) Durchsuchungen dürfen nur durch den Richter, bei Gefahr",
        "im Verzug auch durch die Staatsanwaltschaft und ihre",
        "Ermittlungspersonen (§ 152 des Gerichtsverfassungsgesetzes)",
        "angeordnet werden. …“"]
w105, w105_y = wortlaut(80, 160, 1100, W105, "§ 105 Abs. 1 S. 1 StPO", "p105", marken=[
    (0, "nur durch den Richter", beim("p105a", "Richter")), (0, "bei Gefahr", beim("p105b", "Gefahr")),
    (1, "im Verzug", beim("p105b", "Gefahr")), (1, "Staatsanwaltschaft", beim("p105b", "Staatsanwaltschaft")),
    (2, "Ermittlungspersonen", beim("p105b", "Ermittlungspersonen"))], size=32)
PA = f"{P} › 3. Rechtfertigung › einfaches Recht"
folie([("p105", f"{PA} › § 105 StPO"), ("p105b", f"{PA} › bei Gefahr im Verzug: StA, Ermittlungspersonen"),
       ("kompet", f"{PA} › Bader und Ebner: nur bei Gefahr im Verzug"), ("p102", f"{PA} › Befugnis: § 102 StPO"),
       ("f151", f"{PA} › StPO-Durchsuchung: Folge 151")], rechts_frei([
    *tafel("p105", "Einfaches Recht: § 105 StPO", h=w105_y + 330 - 60, size=46),
    *w105,
    *okz("Bader und Ebner: Ermittlungspersonen", w105_y + 30, "kompet", size=32, x=160),
    blk(110, w105_y + 90, 1040, 76, GELB, beim("kompet", "ohne"), [("ohne Richter nur bei Gefahr im Verzug", "ExtraBold", 34, INK)]),
    z("Befugnis zur Durchsuchung beim Verdächtigen: § 102 StPO", 110, w105_y + 190, "p102", "Bold", 30),
    z("Durchsuchung nach der StPO im Ganzen: Folge 151", 110, w105_y + 245, "f151", "Bold", 30),
    *requisit([("p105", ("tabler", "book", 100, WEISS), "§ 105 StPO", GELB),
               ("p105b", ("tabler", "hourglass", 100, GELB), "nur bei Gefahr im Verzug", WEISS),
               ("kompet", ("tabler", "id-badge", 100, WEISS), "Ermittlungspersonen", WEISS),
               ("p102", ("tabler", "search", 100, WEISS), "§ 102 StPO", WEISS),
               ("f151", ("tabler", "book", 100, WEISS), "Folge 151", WEISS)]),
    *stehend("BA", X1, [("p105", "ernst"), ("kompet", "denkt")]),
    *stehend("EB", X2, [("p105", "ruhig"), ("kompet", "still")]),
]))

# ===========================================================================================================================
# H 5. Lösung
# ===========================================================================================================================
PL = "Lösung"
folie([("loes", f"{PL} › Zurück zu Ines"), ("sonntag", f"{PL} › Sonntag, 19 Uhr: Tageszeit"),
       ("anruf", f"{PL} › kein Versuch, den Richter zu erreichen"), ("muendl", f"{PL} › Richter entscheidet auch mündlich"),
       ("spek", f"{PL} › bloße Vermutung"), ("neg", f"{PL} › Gefahr im Verzug (−)"), ("erg", f"{PL} › Art. 13 GG verletzt")],
      rechts_frei([
    *tafel("loes", "Lösung: Durfte Bader ohne Richter?", h=860, size=44),
    *tagesband(110, 250, 1040, 60, "sonntag", None, marke=(beim("sonntag", "Sonntag"), 19, "So, 19 Uhr")),
    *okz("Tageszeit: Ermittlungsrichter musste erreichbar sein", 360, beim("sonntag", "Ein"), size=30, x=160),
    z("– die Bereitschaftsrichterin war es auch", 160, 404, beim("sonntag", "Richterin"), size=30),
    *neinz("kein Versuch, über die StA den Richter zu erreichen", 460, "anruf", size=30, x=160),
    z("seit 15 Uhr war dafür Zeit", 160, 504, beim("anruf", "seit"), size=30),
    z("einfache Fälle: Richter entscheidet auch mündlich", 160, 560, "muendl", size=30),
    zit("BVerfG, Beschl. v. 16.6.2015 – 2 BvR 2718/10 u. a., Rn. 71 (BVerfGE 139, 245)", 160, 604, beim("muendl", "mündlicher")),
    *neinz("„alles verschwinden lassen“: bloße Vermutung", 655, "spek", size=30, x=160),
    blk(110, 715, 500, 76, HELLROT, "neg", [("Gefahr im Verzug (−)", "ExtraBold", 32, INK)]),
    blk(640, 715, 510, 76, ROT, "erg", [("Art. 13 GG verletzt", "ExtraBold", 32, INK)]),
    *requisit([("loes", ("tabler", "door", 120, HOLZ), "Ines", TUERKIS_),
               ("sonntag", ("tabler", "sun", 110, GELB), "Sonntag, 19 Uhr", GRUEN),
               ("anruf", ("tabler", "phone-off", 100, WEISS), "kein Versuch", HELLROT),
               ("muendl", ("tabler", "phone-call", 100, WEISS), "auch mündlich", WEISS),
               ("spek", ("tabler", "hourglass", 100, GELB), "nur Vermutung", HELLROT),
               ("neg", ("tabler", "hourglass", 100, GELB), "Gefahr im Verzug (−)", HELLROT),
               ("erg", ("tabler", "home", 110, LILA), "Art. 13 verletzt", HELLROT)]),
    *stehend("IN", X1, [("loes", "ruhig"), ("spek", "denkt"), ("erg", "froh")]),
    *stehend("BA", X2, [("loes", "ernst"), ("anruf", "still"), ("erg", "sorge")]),
]))

# ===========================================================================================================================
# I Gegenfall und Verwertung (ein Satz, Verweis Folge 221)
# ===========================================================================================================================
PGF = "Gegenfall"
folie([("gegen", f"{PGF} › konkretes Wissen der Polizei"), ("gegen2", f"{PGF} › Tatsache des Einzelfalls"),
       ("gegen3", f"{PGF} › Versuch käme zu spät"), ("verw", "Verwertung › Abwägung: Folge 221")], rechts_frei([
    *tafel("gegen", "Gegenfall: Karten sollen heute weg", h=780, size=44),
    z("Polizei weiß konkret: Ines will die Karten noch", 110, 180, beim("gegen", "konkret"), "Bold", 32),
    z("an diesem Abend wegschaffen", 110, 226, beim("gegen", "Abend"), "Bold", 32),
    *okz("Tatsache des Einzelfalls", 300, "gegen2", size=32, x=160),
    *okz("schon der Versuch, einen Richter zu erreichen,", 360, "gegen3", size=32, x=160),
    z("kann zu spät kommen", 160, 406, beim("gegen3", "spät"), size=32),
    zit("BVerfGE 103, 142, Rn. 38, 40", 160, 454, beim("gegen3", "spät")),
    blk(110, 540, 1040, 120, GELB, "verw", [("Verwertbarkeit der Karten: eigene Frage", "ExtraBold", 32, INK),
                                           ("der Abwägung – mehr in Folge 221", "ExtraBold", 32, INK)]),
    zit("BVerfG, Beschl. v. 2.7.2009 – 2 BvR 2225/08, Rn. 16 f.", 110, 672, beim("verw", "Abwägung")),
    *requisit([("gegen", ("tabler", "ticket", 140, GELB), "heute Abend weg?", WEISS),
               ("gegen2", ("tabler", "list-check", 100, WEISS), "Tatsache", GRUEN),
               ("gegen3", ("tabler", "clock", 100, WEISS), "Versuch zu spät?", WEISS),
               ("verw", ("tabler", "scale", 110, WEISS), "Folge 221", GELB)]),
    *stehend("IN", X1, [("gegen", "denkt"), ("verw", "ruhig")]),
    *stehend("EB", X2, [("gegen", "ernst"), ("gegen3", "denkt")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · in der Rechtfertigung prüfen"), ("tipp1", "Klausurtipp · Begriff der Verfassung"),
       ("tipp2", "Klausurtipp · volle gerichtliche Kontrolle"), ("tipp3", "Klausurtipp · Durchsuchung oder Betreten?")], [
    *tafel("tipp", "Klausurtipp: Wo prüfe ich das?", fill=HELL, h=680),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Gefahr im Verzug: in der Rechtfertigung,", 200, 200, "tipp", "Bold", 34),
    z("bei Art. 13 Abs. 2 GG", 200, 250, beim("tipp", "Artikel"), size=32),
    z("2. Begriff der Verfassung –", 200, 325, "tipp1", "Bold", 34),
    z("volle gerichtliche Kontrolle, kein", 200, 375, "tipp2", size=32),
    z("Beurteilungsspielraum der Ermittlungsbehörden", 200, 421, beim("tipp2", "Beurteilungsspielraum"), size=32),
    zit("BVerfGE 103, 142, Rn. 44 f.", 200, 469, beim("tipp2", "Beurteilungsspielraum")),
    z("3. Durchsuchung vom bloßen Betreten abgrenzen:", 200, 530, "tipp3", "Bold", 34),
    z("Richtervorbehalt nur für die Durchsuchung", 200, 580, beim("tipp3", "Nur"), size=32),
    zit("Art. 13 Abs. 2, 7 GG; 2 BvR 460/25, Rn. 34 ff.", 200, 626, beim("tipp3", "Richtervorbehalt")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Schema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Schutzbereich: Wohnung, auch Geschäftsräume", True),
          ("s2", 0, "II. Eingriff: Durchsuchung", True),
          ("s3", 0, "III. Rechtfertigung: Art. 13 Abs. 2 GG", True),
          ("s3a", 1, "1. Grundlage: § 102 StPO", False),
          ("s3b", 1, "2. Anordnung: Richter, § 105 Abs. 1 S. 1 StPO", False),
          ("s3c", 1, "3. ohne Richter nur bei Gefahr im Verzug:", False),
          (beim("s3c", "Tatsachen"), 2, "auf Tatsachen gestützt · Richter zuvor versucht ·", False),
          (beim("s3c", "selbst"), 2, "nicht selbst herbeigeführt · dokumentiert", False),
          ("s3d", 1, "4. Verhältnismäßigkeit", False),
          ("s4", 0, "IV. Ergebnis", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Wohnungsdurchsuchung und Art. 13 GG"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 88, 1: 76, 2: 64}[ebene]
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › I. Schutzbereich"), ("s2", "Schema › II. Eingriff"),
       ("s3", "Schema › III. Rechtfertigung"), ("s3c", "Schema › III. 3. Gefahr im Verzug"),
       ("s3d", "Schema › III. 4. Verhältnismäßigkeit"), ("s4", "Schema › IV. Ergebnis")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Durchsuchung ordnet grundsätzlich", 0)], [("der Richter", "a"), (" an.", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Richter")}),
    *markertext([[("Gefahr im Verzug ist die ", 0), ("enge Ausnahme", "b"), (":", 0)],
                 [("Tatsachen", "c"), (" statt Vermutungen,", 0)],
                 [("und zuerst der ", 0), ("Versuch", "d"), (", einen", 0)],
                 [("Richter zu erreichen.", 0)]], 750, 470, 46, "m2",
                {"b": beim("m2", "enge"), "c": beim("m2", "Tatsachen"), "d": beim("m2", "Versuch")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
