"""Folge 180 · Verfahrenshindernisse StPO: Strafantrag, Verjährung & Co. – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Am Mi, 11.3.2026, beleidigt Herr Stolte seinen Nachbarn Herrn Ostwald im Treppenhaus (nur Text-Pille
„beleidigende Äußerung“), am Do, 12.3.2026, schubst er ihn an den Briefkästen (Prellung; kein Bild der Handlung). Erst am
Mo, 13.7.2026, stellt Herr Ostwald bei der Polizei Strafantrag. Im August entwirft Referendarin Hartlieb die
Abschlussverfügung und macht vier typische Klausurfehler (roter Faden: falsch – richtig – Fundstelle).
Szenen laut ../SZENENPLAN.md: A1 Treppenhaus, A2 Polizeiwache, A3 Staatsanwaltschaft, B Sachverhalt, C Aufbau, D Strafantrag
(Wortlautkarte § 194 Abs. 1 S. 1), E Antragsfrist (Wortlautkarte § 77b), F Kalender Juni 2026, Fehler 1, G § 230 (Wortlautkarte),
H Beleidigung (absolutes Antragsdelikt), Fehler 2, I Verjährung (Wortlautkarte § 78 Abs. 3 Nr. 4, 5), Fehler 3,
J Strafklageverbrauch (Wortlautkarte Art. 103 Abs. 3 GG), K Verfügung (Wortlautkarte § 170 Abs. 2 S. 1 StPO), Fehler 4,
L Fehlertabelle, M Prüfschema, N Klausurtipp (Lexi), O Merksatz (Lexi).
Ein Handlungsgeräusch (Aktenstapel, als die Akte auf dem Schreibtisch landet; ../geraeusche_herkunft.json). Namensschild jeder
Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus
Folge 168 (gemeinsame Dateien unverändert); neu: treppenhaus(), tresen(), fenster(), fehler(), Kalender Juni 2026.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 04.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_180/"

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
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
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
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_180/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/124) -----------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder
    („Referendarin Hartlieb“, „Polizeibeamtin“) in 26 px, damit sie neben der zweiten Figur Platz haben."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]





# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (238, 230, 214, 255)
HOLZD = (176, 122, 78, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


def treppenhaus(c):
    """Treppenhaus (Grundform): Wand, Treppe links mit Geländer, Briefkästen rechts an der Wand."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 575 * s), fill=WAND)
        # Treppe links: Stufen steigen nach links an
        pts = [(0, 575)]
        for i in range(8):
            x = 470 - i * 55
            y = 575 - i * 48
            pts += [(x, y), (x, y - 48)]
        pts += [(0, 575 - 8 * 48)]
        dr.polygon([(px * s, py * s) for px, py in pts], fill=(222, 196, 160, 255), outline=INK)
        for i in range(len(pts) - 1):
            dr.line((pts[i][0] * s, pts[i][1] * s, pts[i + 1][0] * s, pts[i + 1][1] * s), fill=INK, width=4 * s)
        # Geländer
        dr.line((40 * s, 120 * s, 500 * s, 500 * s), fill=INK, width=7 * s)
        for i in range(7):
            x = 70 + i * 62
            y = 145 + i * 51
            dr.line((x * s, y * s, x * s, (y + 125) * s), fill=INK, width=4 * s)
        # Briefkästen
        for r in range(2):
            for k in range(3):
                x0, y0 = 1470 + k * 100, 230 + r * 95
                dr.rounded_rectangle((x0 * s, y0 * s, (x0 + 88) * s, (y0 + 82) * s), 8 * s, fill=GRAUW, outline=INK, width=4 * s)
                dr.line(((x0 + 18) * s, (y0 + 22) * s, (x0 + 70) * s, (y0 + 22) * s), fill=INK, width=4 * s)
        dr.line((0, 575 * s - 2, 1800 * s, 575 * s - 2), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 575, zz), 60, BODEN_Y - 575, c, "cut", 0.0, None, name="treppenhaus"))


def tresen(c, x0, x1, h=250):
    """Tresen der Polizeiwache (verdeckt die Beine der Beamtin), ohne Logo."""
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 34 * s), 8 * s, fill=(226, 226, 222, 255), outline=INK, width=5 * s)
        dr.rectangle((20 * s, 34 * s, (w - 20) * s, (h - 3) * s), fill=(141, 179, 242, 255), outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="tresen"))


def schreibtisch(c, x0, x1):
    w, h = x1 - x0, 170
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"OS": "Herr Ostwald", "ST": "Herr Stolte", "HA": "Referendarin Hartlieb", "PB": "Polizeibeamtin"}
NFARBE = {"OS": BLAU, "ST": ROT, "HA": LILA, "PB": WEISS}


def stehend(k, x, folge, unten=930, hoehe=480):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)];
    ein Eintrag (cue, None, None, None) beendet das vorige Requisit (z. B. vor einer Sprechblase)."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_l, folge_r, links="HA", rechts="OS"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


def fehler(nr, c_f, c_r, falsch, richtig, fund, mimik_f="schreck", mimik_r="froh", pf=None):
    """Klausurfehler-Karte (roter Faden): falsch (Kreuz, hellrot) – richtig (Haken, hellgrün) – Fundstelle;
    Referendarin Hartlieb rechts, die den Fehler im Entwurf macht."""
    pf = pf or f"Klausurfehler {nr}"
    els = [*tafel(c_f, f"Klausurfehler {nr}", fill=HELL), warnung_i(150, 215, c_f, gr=24),
           z("falsch:", 200, 190, c_f, "ExtraBold", 34, farbe=DROT)]
    hf = 40 + 46 * len(falsch)
    els += [karte(110, 250, 1040, hf, c_f, fill=HELLROT, rund=18, schatten=6, rand=4), nein(155, 250 + hf / 2 - 2, c_f, gr=22)]
    for i, t in enumerate(falsch):
        els.append(z(t, 200, 268 + 46 * i, c_f, "Bold", 34))
    y = 250 + hf + 50
    els.append(z("richtig:", 200, y, c_r, "ExtraBold", 34, farbe=DGRUEN))
    hr = 40 + 46 * len(richtig)
    els += [karte(110, y + 60, 1040, hr, c_r, fill=HELLGRUEN, rund=18, schatten=6, rand=4), ok(155, y + 60 + hr / 2 - 2, c_r, gr=22)]
    for i, t in enumerate(richtig):
        els.append(z(t, 200, y + 78 + 46 * i, c_r, "Bold", 34))
    y2 = y + 60 + hr + 30
    els.append(zit("Fundstelle: " + fund, 130, y2, c_r, size=28))
    assert y2 + 40 <= 890, y2
    els += allein("HA", [(c_f, mimik_f), (c_r, mimik_r)])
    return rechts_frei(els)


# ===========================================================================================================================
# A1 Fall: Treppenhaus – Streit, beleidigende Äußerung, Schubser (ohne Bild der Handlung)
# ===========================================================================================================================
STX, OSX = 820, 1300                         # Herr Stolte (blickt nach rechts), Herr Ostwald (blickt nach links)
folie([(NULL, "Fall · Im Treppenhaus"), ("bel", "Fall · die beleidigende Äußerung"), ("schub", "Fall · am nächsten Tag")], [
    treppenhaus(NULL),
    boden(NULL),
    hart(pl("Mietshaus · Treppenhaus", 70, 30, NULL, fill=GELB, size=38)),
    hart(pl("Mittwoch, 11.3.2026", 70, 110, NULL, fill=WEISS, size=34)),
    hart(ficon("ph", "bicycle-bold", 1060, BODEN_Y, 230, NULL, fuell=WEISS, anim="cut")),
    *fig("ST", STX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("streit", "ernst_r"), ("bel", "abfaellig_r"), ("schub", "ernst_r")], erst="cut"),
    hart(ns("Herr Stolte", STX, BODEN_Y, NULL, ROT)),
    *fig("OS", OSX, BODEN_Y, FHA, [(NULL, "ruhig"), ("streit", "ernst"), (beim("bel", "beleidigende"), "schreck"),
                                   ("schub", "sorge")], erst="cut"),
    hart(ns("Herr Ostwald", OSX, BODEN_Y, NULL, BLAU)),
    pl("Streit ums Fahrrad", 70, 190, beim("streit", "streiten"), fill=WEISS, size=32, bis="schub"),
    pl("beleidigende Äußerung", STX, 345, beim("bel", "beleidigende"), fill=HELLROT, size=32, anker="m"),
    pl("Am nächsten Tag (12.3.): Schubser an den Briefkästen – Prellung am Arm", 70, 190, "schub",
       fill=HELLROT, size=32),
])

# ===========================================================================================================================
# A2 Fall: Polizeiwache – Anzeige und Strafantrag im Juli
# ===========================================================================================================================
PBX, OS2 = 600, 1290
folie([("juli", "Fall · Juli: auf der Polizeiwache"), ("os1", "Fall · Anzeige und Strafantrag")], [
    boden("juli"),
    hart(pl("Polizeiwache", 70, 30, "juli", fill=BLAU, size=38)),
    pl("4 Monate später", 70, 110, beim("juli", "vier"), fill=HELLROT, size=34),
    pl("Montag, 13.7.2026", 405, 110, beim("juli", "Juli"), fill=WEISS, size=34),
    *stehend("PB", PBX, [("juli", "ruhig_r"), ("os1", "ernst_r")], unten=BODEN_Y),
    tresen("juli", 330, 870),
    ficon("tabler", "calendar-event", 470, BODEN_Y - 250, 90, "juli", fuell=WEISS),
    *stehend("OS", OS2, [("juli", "ernst")], unten=BODEN_Y),
    *redet("OS_redet", OS2, BODEN_Y, FHA, "os1", "akte"),
    blase("sprech", 720, 240, "os1", 1160, 235, inhalt=["Ich zeige meinen Nachbarn an", "und stelle Strafantrag.",
                                                        "Ich wollte erst Frieden im Haus."], textsize=34,
          figur=("OS_redet", OS2, BODEN_Y, FHA), bis="akte"),
    ficon("tabler", "clipboard-text", 760, BODEN_Y - 250, 90, beim("os1", "Strafantrag"), fuell=WEISS),
    pl("Anzeige und Strafantrag", 70, 190, beim("os1", "Strafantrag"), fill=GELB, size=34),
])

# ===========================================================================================================================
# A3 Fall: Staatsanwaltschaft – der Entwurf von Referendarin Hartlieb
# ===========================================================================================================================
HAX = 1520
folie([("akte", "Fall · August: bei der Staatsanwaltschaft"), ("verf", "Fall · die Abschlussverfügung"),
       ("frage", "Fall · ein Klausurfehler?"), ("frage2", "Fall · die Fragen")], [
    boden("akte"),
    fenster("akte", 1100, 380),
    schreibtisch("akte", 640, 1220),
    hart(pl("Staatsanwaltschaft", 70, 30, "akte", fill=LILA, size=38)),
    pl("August 2026", 70, 110, beim("akte", "August"), fill=WEISS, size=34),
    szene(ficon("tabler", "folders", 860, BODEN_Y - 170, 150, beim("akte", "Akte"), fuell=GELB), "180akte*", 1.0, 0.0),
    pl("Akte Stolte", 860, 560, beim("akte", "Akte"), fill=WEISS, size=28, anker="m"),
    pl("Abschlussverfügung", 355, 110, "verf", fill=GELB, size=34),
    *stehend("HA", HAX, [("akte", "froh"), ("verf", "eifrig")], unten=BODEN_Y),
    *redet("HA_redet", HAX, BODEN_Y, FHA, "ha1", "frage"),
    blase("sprech", 640, 220, "ha1", 1230, 225, inhalt=["Der Strafantrag liegt vor.", "Ich klage beides an!"], textsize=38,
          figur=("HA_redet", HAX, BODEN_Y, FHA), bis="frage"),
    pl("Entwurf: Anklage", 1090, 690, beim("ha1", "klage"), fill=HELLROT, size=28, anker="m"),
    *fig("HA", HAX, BODEN_Y, FHA, [("frage", "schreck"), ("frage2", "skeptisch")], erst="cut"),
    pl("Ein typischer Klausurfehler!", 70, 190, "frage", fill=HELLROT, size=36),
    pl("Welche Verfahrenshindernisse stehen im Weg?", 70, 270, "frage2", fill=PINK, size=36),
    pl("Was verfügt die Staatsanwaltschaft?", 70, 350, beim("frage2", "was"), fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_180(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_180("sv", [
    "Am Mittwoch, 11. März 2026, streiten Herr Stolte und sein Nachbar Herr Ostwald im Treppenhaus ihres Mietshauses "
    "über ein Fahrrad. Herr Stolte macht dabei eine beleidigende Äußerung. Am Donnerstag, 12. März 2026, schubst er "
    "Herrn Ostwald an den Briefkästen; Herr Ostwald erleidet eine Prellung am Arm, ein ärztliches Attest liegt vor.",
    "Herr Ostwald erkennt Herrn Stolte jeweils sofort. Erst am Montag, 13. Juli 2026, erstattet er bei der Polizei "
    "Anzeige und stellt Strafantrag wegen beider Taten. Herr Stolte ist wegen Körperverletzung vorbestraft.",
    "Im August 2026 entwirft Referendarin Hartlieb bei der Staatsanwaltschaft die Abschlussverfügung.",
], "Welche Verfahrenshindernisse bestehen – und was verfügt die Staatsanwaltschaft?")

# ===========================================================================================================================
# C Aufbau: vier Verfahrenshindernisse, zwei prozessuale Taten
# ===========================================================================================================================
folie([("aufbau", "Aufbau · Verfahrenshindernisse"), ("a1", "Aufbau › 1. Strafantrag"),
       ("a2", "Aufbau › 2. besonderes öffentliches Interesse"), ("a3", "Aufbau › 3. Verjährung"),
       ("a4", "Aufbau › 4. Strafklageverbrauch"), ("taten", "Aufbau · zwei prozessuale Taten")], rechts_frei([
    *tafel("aufbau", "Verfahrenshindernisse"),
    z("sperren die Verfolgung – so klar die Tat auch ist", 110, 175, "aufbau", "Bold", 34),
    blk(110, 245, 1040, 76, GELB, "a1", [("1. Strafantrag", "ExtraBold", 34, INK)]),
    blk(110, 340, 1040, 76, BLAU, "a2", [("2. besonderes öffentliches Interesse", "ExtraBold", 34, INK)]),
    blk(110, 435, 1040, 76, HELLGRUEN, "a3", [("3. Verjährung", "ExtraBold", 34, INK)]),
    blk(110, 530, 1040, 76, LILA, "a4", [("4. Strafklageverbrauch", "ExtraBold", 34, INK)]),
    z("Vorweg: 2 Tage (11.3. und 12.3.) = 2 prozessuale Taten,", 110, 650, "taten", "Bold", 32),
    z("je Tat eine eigene Entscheidung", 110, 698, beim("taten", "je"), size=32),
    zit("mehr dazu im Video „Anklageklausur“", 110, 752, beim("taten", "Video")),
    *requisit([("aufbau", ("tabler", "ban", 100, HELLROT), "Verfahrenshindernis", HELLROT),
               ("a1", ("tabler", "file-text", 100, GELB), "Strafantrag", GELB),
               ("a2", ("tabler", "users", 110, BLAU), "öffentliches Interesse", BLAU),
               ("a3", ("tabler", "hourglass", 90, HELLGRUEN), "Verjährung", HELLGRUEN),
               ("a4", ("tabler", "gavel", 100, LILA), "Strafklageverbrauch", LILA),
               ("taten", ("tabler", "calendar-event", 100, WEISS), "11.3. | 12.3.", WEISS)]),
    *zwei([("aufbau", "ruhig"), ("a2", "skeptisch"), ("taten", "ernst")], [("aufbau", "ruhig"), ("taten", "ernst")]),
]))

# ===========================================================================================================================
# D Strafantrag: § 194 Abs. 1 S. 1 (Wortlaut), § 230, § 77, Form § 158 Abs. 2 StPO
# ===========================================================================================================================
PS_ = "Strafantrag"
W194 = ["„Die Beleidigung wird nur auf Antrag verfolgt. …“"]
w194, w194_y = wortlaut(80, 170, 1100, W194, "§ 194 Abs. 1 S. 1 StGB", "p194", marken=[
    (0, "nur auf Antrag", beim("p194", "nur"))], size=36)
folie([("p194", f"{PS_} › § 194 Abs. 1 S. 1 StGB"), ("p230k", f"{PS_} › Körperverletzung: § 230 StGB"),
       ("p77", f"{PS_} › antragsberechtigt: § 77 Abs. 1 StGB"), ("form", f"{PS_} › Form: § 158 Abs. 2 StPO")], rechts_frei([
    *tafel("p194", "Strafantrag: §§ 194, 230, 77 StGB"),
    *w194,
    z("§ 230 Abs. 1 S. 1: Körperverletzung grundsätzlich ebenso", 110, w194_y + 40, "p230k", "Bold", 34),
    *okz("§ 77 Abs. 1: Antrag stellt der Verletzte", w194_y + 125, "p77", "Bold", 34, x=160),
    z("hier: Herr Ostwald", 160, w194_y + 175, beim("p77", "Herr"), size=34),
    z("Form, § 158 Abs. 2 StPO:", 110, w194_y + 265, "form", "Bold", 34),
    z("Identität und Verfolgungswille sichergestellt", 110, w194_y + 313, beim("form", "Identität"), size=34),
    *requisit([("p194", ("tabler", "file-text", 100, WEISS), "nur auf Antrag", WEISS),
               ("p230k", ("tabler", "hand-stop", 100, GELB), "Körperverletzung: ebenso", GELB),
               ("p77", ("tabler", "user-check", 100, GRUEN), "der Verletzte", HELLGRUEN),
               ("form", ("tabler", "id", 110, BLAU), "Identität + Verfolgungswille", BLAU)]),
    *allein("OS", [("p194", "ruhig"), ("p77", "froh"), ("form", "ruhig")]),
]))

# ===========================================================================================================================
# E Antragsfrist: § 77b Abs. 1 S. 1, Abs. 2 S. 1 StGB (Wortlaut)
# ===========================================================================================================================
PF = "Antragsfrist"
W77B = ["„(1) Eine Tat, die nur auf Antrag verfolgbar ist, wird nicht",
        "verfolgt, wenn der Antragsberechtigte es unterläßt, den Antrag",
        "bis zum Ablauf einer Frist von drei Monaten zu stellen. …",
        "(2) Die Frist beginnt mit Ablauf des Tages, an dem der",
        "Berechtigte von der Tat und der Person des Täters Kenntnis",
        "erlangt. …“"]
w77b, w77b_y = wortlaut(80, 165, 1100, W77B, "§ 77b Abs. 1 S. 1, Abs. 2 S. 1 StGB", "p77b", marken=[
    (0, "wird nicht", beim("p77b", "nicht")), (1, "verfolgt", beim("p77b", "nicht")),
    (2, "drei Monaten", beim("p77b", "drei")), (3, "mit Ablauf des Tages", beim("beginn", "Ablauf")),
    (4, "von der Tat und der Person des Täters", beim("beginn", "von")), (4, "Kenntnis", beim("beginn", "Kenntnis"))],
    size=32)
folie([("p77b", f"{PF} › § 77b Abs. 1 S. 1 StGB: 3 Monate"), ("beginn", f"{PF} › Beginn: § 77b Abs. 2 S. 1 StGB")], rechts_frei([
    *tafel("p77b", "Antragsfrist: § 77b StGB"),
    *w77b,
    blk(110, w77b_y + 40, 1040, 80, GELB, beim("beginn", "Kenntnis"), [("3 Monate ab Kenntnis von Tat und Täter", "ExtraBold", 34, INK)]),
    *requisit([("p77b", ("tabler", "hourglass", 90, GELB), "Frist: 3 Monate", GELB),
               ("beginn", ("tabler", "user-check", 100, WEISS), "ab Kenntnis", WEISS)]),
    *allein("HA", [("p77b", "skeptisch"), ("beginn", "ernst")]),
]))

# ===========================================================================================================================
# F Kalender Juni 2026: Fristende 11.6. bzw. 12.6., Antrag am 13.7.
# ===========================================================================================================================
KW_, KH_, KCX, KCY = 148, 76, 115, 330       # Kalenderzelle: Breite, Höhe, links, oben
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
JUNI = [[(d, 1) for d in range(1, 8)], [(d, 1) for d in range(8, 15)], [(d, 1) for d in range(15, 22)],
        [(d, 1) for d in range(22, 29)], [(29, 1), (30, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]]
import datetime as _dt
assert _dt.date(2026, 6, 1).weekday() == 0 and _dt.date(2026, 6, 11).weekday() == 3 and _dt.date(2026, 6, 12).weekday() == 4
assert _dt.date(2026, 3, 11).weekday() == 2 and _dt.date(2026, 3, 12).weekday() == 3 and _dt.date(2026, 7, 13).weekday() == 0
assert _dt.date(2026, 4, 5) + _dt.timedelta(60) == _dt.date(2026, 6, 4)          # Fronleichnam 4.6. – nicht am Fristende


def zelle(tag):
    for r, w in enumerate(JUNI):
        for c, (d, im_m) in enumerate(w):
            if d == tag and im_m:
                return KCX + c * KW_, KCY + r * KH_
    raise KeyError(tag)


def kalender(cue):
    s = 2
    im = Image.new("RGBA", (7 * KW_ * s + 8 * s, (5 * KH_ + 50) * s))
    dr = ImageDraw.Draw(im)
    fk, fz = F("Bold", 28 * s), F("Bold", 32 * s)
    for c, t in enumerate(TAGE):
        dr.text(((c * KW_ + KW_ / 2) * s, 22 * s), glyphen(t), font=fk, fill=TEXT if c >= 5 else INK, anchor="mm")
    for r, w in enumerate(JUNI):
        for c, (d, im_m) in enumerate(w):
            x0, y0 = c * KW_ * s + 4 * s, (50 + r * KH_) * s
            dr.rounded_rectangle((x0, y0, x0 + (KW_ - 8) * s, y0 + (KH_ - 8) * s), 10 * s,
                                 fill=(255, 255, 255, 255) if im_m else (238, 238, 234, 255), outline=INK, width=3 * s)
            dr.text((x0 + 14 * s, y0 + 6 * s), str(d), font=fz, fill=INK if im_m else (150, 150, 150, 255))
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, KCX - 4, KCY - 50, cue, "fade", 0.0, None, name="kalender")


def markiere(tag, cue, fill, text=None, bis=None):
    x, y = zelle(tag)
    im = Image.new("RGBA", (KW_ - 8, KH_ - 8))
    d_ = ImageDraw.Draw(im)
    d_.rounded_rectangle((0, 0, im.width - 1, im.height - 1), 10, fill=fill[:3] + (255,), outline=INK, width=3)
    d_.text((14, 6), str(tag), font=F("Bold", 32), fill=INK)
    if text:
        d_.text((im.width - 8, im.height - 5), glyphen(text), font=F("Bold", 26), fill=INK, anchor="rd")
    return El(im, x, y, cue, "pop", 0.0, bis, name=f"tag:{tag}")


folie([("kenn", f"{PF} › Kenntnis: Mi, 11.3.2026"), (beim("ende", "elften"), f"{PF} › Ende: Do, 11.6.2026, 24 Uhr"),
       (beim("schub2", "zwölften", nr=2), f"{PF} › Schubser: Ende Fr, 12.6.2026"), ("spaet", f"{PF} › Antrag am 13.7.2026: zu spät (-)")], rechts_frei([
    *tafel("kenn", "Antragsfrist berechnen"),
    z("Beleidigung: Kenntnis am Tattag, Mi, 11.3.2026", 110, 172, "kenn", "Bold", 32),
    z("Schubser: Kenntnis am Do, 12.3.2026", 110, 218, "schub2", "Bold", 32),
    z("Juni 2026", 1150 - F("ExtraBold", 30).getlength("Juni 2026"), 172, "ende", "ExtraBold", 30, farbe=TEXT),
    kalender("ende"),
    markiere(11, beim("ende", "elften"), GELB, "Ende"),
    markiere(12, beim("schub2", "zwölften", nr=2), BLAU, "Ende"),
    *neinz("Antrag am Mo, 13.7.2026: für beide Taten zu spät", 745, "spaet", "ExtraBold", 32, x=160),
    *requisit([("kenn", ("tabler", "user-check", 100, WEISS), "Kenntnis: 11.3.", WEISS),
               (beim("ende", "elften"), ("tabler", "calendar-event", 100, GELB), "Ende: Do, 11.6.", GELB),
               (beim("schub2", "zwölften", nr=2), ("tabler", "calendar-event", 100, BLAU), "Ende: Fr, 12.6.", BLAU),
               ("spaet", ("tabler", "calendar-x", 100, HELLROT), "Antrag 13.7.: zu spät", HELLROT)]),
    *allein("OS", [("kenn", "ruhig"), ("spaet", "sorge")]),
]))

# Klausurfehler 1
folie([("f1", "Klausurfehler 1 › Antrag ohne Frist"), ("f1r", "Klausurfehler 1 › Frist ab Kenntnis rechnen")],
      fehler(1, "f1", "f1r", ["„Strafantrag liegt vor, also verfolgbar.“"],
             ["die Frist rechnen: ab Kenntnis von Tat und Täter,", "nicht ab der Anzeige"],
             "§ 77b Abs. 1 S. 1, Abs. 2 S. 1 StGB"))

# ===========================================================================================================================
# G Ausweg: besonderes öffentliches Interesse, § 230 Abs. 1 S. 1 StGB (Wortlaut), Nr. 234 RiStBV
# ===========================================================================================================================
PI = "Öffentliches Interesse"
W230 = ["„(1) Die vorsätzliche Körperverletzung nach § 223 und die",
        "fahrlässige Körperverletzung nach § 229 werden nur auf Antrag",
        "verfolgt, es sei denn, daß die Strafverfolgungsbehörde wegen des",
        "besonderen öffentlichen Interesses an der Strafverfolgung ein",
        "Einschreiten von Amts wegen für geboten hält. …“"]
w230, w230_y = wortlaut(80, 160, 1100, W230, "§ 230 Abs. 1 S. 1 StGB", "p230", marken=[
    (1, "nur auf Antrag", beim("p230", "nur")), (2, "es sei denn", beim("p230", "sei")),
    (3, "besonderen öffentlichen Interesses", beim("p230", "besonderen")), (4, "von Amts wegen", beim("p230", "Amts"))],
    size=30)
folie([("p230", f"{PI} › § 230 Abs. 1 S. 1 StGB"), ("rel", f"{PI} › relatives Antragsdelikt"),
       ("vorstr", f"{PI} › vorbestraft: Nr. 234 RiStBV"), ("bejaht", f"{PI} › bejaht (+)")], rechts_frei([
    *tafel("p230", "Ausweg: § 230 StGB"),
    *w230,
    blk(110, w230_y + 30, 1040, 76, HELLGRUEN, "rel", [("relatives Antragsdelikt", "ExtraBold", 34, INK)]),
    z("hilft auch über den verspäteten Antrag hinweg", 110, w230_y + 122, beim("rel", "hilft"), size=32),
    z("Herr Stolte: wegen Körperverletzung vorbestraft", 110, w230_y + 190, "vorstr", "Bold", 32),
    zit("Nr. 234 Abs. 1 S. 1 RiStBV: „einschlägig vorbestraft“", 110, w230_y + 238, beim("vorstr", "Richtlinien")),
    *okz("besonderes öffentliches Interesse: bejaht", w230_y + 300, "bejaht", "ExtraBold", 34, x=160),
    *requisit([("p230", ("tabler", "scale", 100, WEISS), "Gibt es einen Ausweg?", WEISS),
               ("rel", ("tabler", "lock-open", 100, HELLGRUEN), "relatives Antragsdelikt", HELLGRUEN),
               ("vorstr", ("tabler", "file-text", 100, WEISS), "vorbestraft", WEISS),
               ("bejaht", ("tabler", "shield-check", 100, GRUEN), "Interesse bejaht", HELLGRUEN)]),
    *zwei([("p230", "skeptisch"), ("bejaht", "froh")], [("p230", "ruhig"), ("vorstr", "ernst")], links="HA", rechts="ST"),
]))

# ===========================================================================================================================
# H Beleidigung: absolutes Antragsdelikt; Referendarin Hartlieb will auch hier das Interesse bejahen
# ===========================================================================================================================
folie([("absol", f"{PI} › und die Beleidigung?"), ("abs2", f"{PI} › § 194: absolutes Antragsdelikt"),
       ("ausn", f"{PI} › Ausnahmen S. 2, 3: nicht einschlägig"), ("ha2", f"{PI} › auch bei der Beleidigung?")], rechts_frei([
    *tafel("absol", "Beleidigung: § 194 Abs. 1 StGB"),
    z("Und die Beleidigung?", 110, 180, "absol", "Bold", 36),
    *neinz("kein Ausweg über das öffentliche Interesse", 260, beim("abs2", "Ausweg"), "Bold", 34, x=160),
    blk(110, 340, 1040, 80, HELLROT, beim("abs2", "absolutes"), [("absolutes Antragsdelikt", "ExtraBold", 36, INK)]),
    z("Ausnahmen der Sätze 2 und 3: nur Sonderfälle,", 110, 470, "ausn", "Bold", 34),
    z("etwa § 188 (Personen des politischen Lebens)", 110, 518, beim("ausn", "Paragraf"), size=32),
    *neinz("Streit im Treppenhaus: nicht erfasst", 600, beim("ausn", "Streit"), "Bold", 34, x=160),
    *requisit([("absol", ("tabler", "message-off", 100, HELLROT), "Beleidigung", HELLROT),
               (beim("abs2", "absolutes"), ("tabler", "lock", 100, HELLROT), "absolut", HELLROT),
               ("ha2", None, None, None)]),
    *fig("HA", FX, FB, FR, [("absol", "ernst"), ("ausn", "ruhig")], bis="ha2"),
    ns(NAME["HA"], FX, FB, "absol", NFARBE["HA"], d=0.1),
    *redet("HA_redet", FX, FB, FR, "ha2", "f2"),
    blase("sprech", 560, 240, "ha2", 1560, 235, inhalt=["Dann bejahe ich eben", "auch hier das", "öffentliche Interesse!"],
          textsize=36, figur=("HA_redet", FX, FB, FR), bis="f2"),
]))

# Klausurfehler 2
folie([("f2", "Klausurfehler 2 › Interesse bei der Beleidigung"), ("f2r", "Klausurfehler 2 › nichts ersetzt den Antrag")],
      fehler(2, "f2", "f2r", ["„Dann bejahe ich eben auch hier das", "öffentliche Interesse!“"],
             ["Für diese Beleidigung ersetzt nichts", "den rechtzeitigen Antrag."],
             "§ 194 Abs. 1 S. 1, 3 StGB; nur § 230 StGB kennt den Ausweg"))

# ===========================================================================================================================
# I Verjährung: § 78 Abs. 3 Nr. 4, 5 (Wortlaut), §§ 78a, 78c StGB
# ===========================================================================================================================
PV = "Verjährung"
W78 = ["„(3) Soweit die Verfolgung verjährt, beträgt die Verjährungsfrist …",
       "4. fünf Jahre bei Taten, die im Höchstmaß mit Freiheitsstrafen von",
       "mehr als einem Jahr bis zu fünf Jahren bedroht sind,",
       "5. drei Jahre bei den übrigen Taten.“"]
w78, w78_y = wortlaut(80, 160, 1100, W78, "§ 78 Abs. 3 Nr. 4, 5 StGB", "p78", marken=[
    (1, "fünf Jahre", beim("p78", "fünf")), (2, "mehr als einem Jahr", beim("p78", "mehr")),
    (3, "drei Jahre", beim("nr5", "drei")), (3, "übrigen Taten", beim("nr5", "übrigen"))], size=30)
folie([("p78", f"{PV} › § 78 Abs. 3 StGB"), ("rahmen", f"{PV} › Beleidigung: 3 Jahre (Nr. 5)"),
       ("qual", f"{PV} › öffentliche Beleidigung: 5 Jahre (Nr. 4)"), ("kv5", f"{PV} › Körperverletzung: 5 Jahre (Nr. 4)"),
       ("p78a", f"{PV} › Beginn: § 78a StGB"), ("p78c", f"{PV} › Unterbrechung: § 78c StGB"),
       ("nichtv", f"{PV} › nicht verjährt")], rechts_frei([
    *tafel("p78", "Verjährung: §§ 78 ff. StGB"),
    *w78,
    z("§ 185: bis 1 Jahr – Nr. 5: 3 Jahre", 110, w78_y + 30, "rahmen", "ExtraBold", 32),
    z("§ 185 öffentlich: bis 2 Jahre – Nr. 4: 5 Jahre", 110, w78_y + 80, "qual", "Bold", 32),
    z("§ 223: bis 5 Jahre – Nr. 4: 5 Jahre", 110, w78_y + 130, "kv5", "ExtraBold", 32),
    z("Beginn: Beendigung der Tat, § 78a", 110, w78_y + 195, "p78a", size=32),
    z("Unterbrechung: 1. Vernehmung, § 78c Abs. 1 Nr. 1", 110, w78_y + 243, "p78c", size=32),
    *okz("August 2026: nichts verjährt", w78_y + 310, "nichtv", "ExtraBold", 34, x=160),
    *requisit([("p78", ("tabler", "hourglass", 90, WEISS), "Verjährung", WEISS),
               ("rahmen", ("tabler", "message-off", 100, HELLROT), "Beleidigung: 3 Jahre", HELLROT),
               ("kv5", ("tabler", "hand-stop", 100, GELB), "Körperverletzung: 5 Jahre", GELB),
               ("p78c", ("tabler", "report", 100, WEISS), "Vernehmung unterbricht", WEISS),
               ("nichtv", ("tabler", "calendar-check", 100, GRUEN), "nicht verjährt", HELLGRUEN)]),
    *allein("HA", [("p78", "ruhig"), ("rahmen", "skeptisch"), ("nichtv", "froh")]),
]))
assert w78_y + 350 <= 890

# Klausurfehler 3
folie([("f3", "Klausurfehler 3 › 5 Jahre für jedes Vergehen"), ("f3r", "Klausurfehler 3 › Höchstmaß ablesen")],
      fehler(3, "f3", "f3r", ["„5 Jahre für jedes Vergehen.“"], ["das Höchstmaß ablesen:", "§ 185 bis 1 Jahr – 3 Jahre"],
             "§ 78 Abs. 3 Nr. 4, 5, Abs. 4 StGB", mimik_r="ernst"))

# ===========================================================================================================================
# J Strafklageverbrauch: Art. 103 Abs. 3 GG (Wortlaut), BVerfG 2 BvR 900/22
# ===========================================================================================================================
PK = "Strafklageverbrauch"
W103 = ["„Niemand darf wegen derselben Tat auf Grund der allgemeinen",
        "Strafgesetze mehrmals bestraft werden.“"]
w103, w103_y = wortlaut(80, 170, 1100, W103, "Art. 103 Abs. 3 GG", "p103", marken=[
    (0, "derselben Tat", beim("p103", "derselben")), (1, "mehrmals bestraft", beim("p103", "mehrmals"))], size=34)
folie([("p103", f"{PK} › Art. 103 Abs. 3 GG"), ("urt", f"{PK} › rechtskräftiges Strafurteil?"),
       ("keins", f"{PK} › hier keines (-)")], rechts_frei([
    *tafel("p103", "Strafklageverbrauch"),
    *w103,
    z("Sperre: rechtskräftiges Strafurteil", 110, w103_y + 40, beim("urt", "sperrt"), "Bold", 34),
    z("über dieselbe Tat", 110, w103_y + 88, beim("urt", "dieselbe"), "Bold", 34),
    zit("BVerfG, Urt. v. 31.10.2023 – 2 BvR 900/22, Rn. 3, 95", 110, w103_y + 142, beim("urt", "dieselbe")),
    *neinz("hier: kein früheres Urteil", w103_y + 220, "keins", "ExtraBold", 34, x=160),
    *requisit([("p103", ("tabler", "gavel", 100, LILA), "dieselbe Tat?", LILA),
               ("keins", ("tabler", "file-x", 100, WEISS), "kein Urteil", WEISS)]),
    *allein("ST", [("p103", "ruhig"), ("urt", "skeptisch"), ("keins", "ernst")]),
]))

# ===========================================================================================================================
# K Verfügung: § 170 Abs. 2 S. 1 StPO (Wortlaut), §§ 374, 376 StPO; Referendarin Hartlieb korrigiert ihren Entwurf
# ===========================================================================================================================
PE = "Verfügung"
W170 = ["„Andernfalls stellt die Staatsanwaltschaft das Verfahren ein. …“"]
w170, w170_y = wortlaut(80, 170, 1100, W170, "§ 170 Abs. 2 S. 1 StPO", "p170", marken=[
    (0, "stellt die Staatsanwaltschaft das Verfahren ein", beim("p170", "stellt"))], size=34)
folie([("p170", f"{PE} › § 170 Abs. 2 S. 1 StPO"), ("bele", f"{PE} › Tat 1, Beleidigung: Einstellung"),
       ("kva", f"{PE} › Tat 2, Körperverletzung: Anklage"), ("ha3", f"{PE} › der korrigierte Entwurf")], rechts_frei([
    *tafel("p170", "Verfügung: § 170 StPO"),
    *w170,
    z("Tat 1, Beleidigung: kein genügender Anlass", 110, w170_y + 40, "bele", "Bold", 34),
    blk(110, w170_y + 95, 1040, 76, HELLROT, beim("bele", "Einstellung"), [("Einstellung, § 170 Abs. 2 StPO", "ExtraBold", 34, INK)]),
    z("Tat 2, Körperverletzung: Privatklagedelikt", 110, w170_y + 210, "kva", "Bold", 34),
    z("§ 376 StPO: öffentliches Interesse – mit dem besonderen gegeben", 110, w170_y + 258, beim("kva", "verlangt"), size=30),
    blk(110, w170_y + 310, 1040, 76, HELLGRUEN, beim("kva", "Anklage"), [("Anklage, § 170 Abs. 1 StPO", "ExtraBold", 34, INK)]),
    *requisit([("p170", ("tabler", "folder", 100, WEISS), "Verfügung", WEISS),
               (beim("bele", "Einstellung"), ("tabler", "file-x", 100, HELLROT), "Tat 1: Einstellung", HELLROT),
               (beim("kva", "Anklage"), ("tabler", "file-check", 100, HELLGRUEN), "Tat 2: Anklage", HELLGRUEN),
               ("ha3", None, None, None)]),
    *fig("HA", X1, FB, FR, [("p170", "ruhig"), ("bele", "ernst")], bis="ha3"),
    ns(NAME["HA"], X1, FB, "p170", NFARBE["HA"], d=0.1),
    *redet("HA_redet2", X1, FB, FR, "ha3", "f4"),
    blase("sprech", 600, 210, "ha3", 1560, 230, inhalt=["Also: Beleidigung einstellen,", "Körperverletzung anklagen."],
          textsize=34, figur=("HA_redet2", X1, FB, FR), bis="f4"),
    *stehend("ST", X2, [("p170", "ruhig"), ("kva", "muede")]),
]))
assert w170_y + 390 <= 890

# Klausurfehler 4
folie([("f4", "Klausurfehler 4 › Privatklageweg trotz verspätetem Antrag"), ("f4r", "Klausurfehler 4 › auch Privatklage braucht den Antrag")],
      fehler(4, "f4", "f4r", ["bei verspätetem Antrag: Verweisung", "auf den Privatklageweg, § 374 StPO"],
             ["Auch die Privatklage braucht", "einen rechtzeitigen Antrag."],
             "§ 77b Abs. 1 S. 1 StGB („wird nicht verfolgt“)", mimik_f="skeptisch", mimik_r="froh"))

# ===========================================================================================================================
# L Fehlertabelle: die vier Fehler auf einen Blick
# ===========================================================================================================================
TAB = [("t1", ["Antrag liegt vor,", "also verfolgbar"], ["Frist rechnen:", "3 Monate ab Kenntnis"], ["§ 77b StGB"]),
       ("t2", ["öffentliches Interesse", "bei der Beleidigung"], ["nur relative Antrags-", "delikte, z. B. § 230"], ["§§ 194, 230", "StGB"]),
       ("t3", ["Verjährung pauschal:", "5 Jahre"], ["Höchstmaß ablesen:", "§ 185 – 3 Jahre"], ["§ 78 Abs. 3", "StGB"]),
       ("t4", ["Privatklage trotz", "verspätetem Antrag"], ["auch sie braucht den", "rechtzeitigen Antrag"], ["§ 77b StGB;", "§ 374 StPO"])]
els_tab = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Die vier Fehler auf einen Blick"), 110, 90, "tab", 46),
           z("falsch", 200, 180, "tab", "ExtraBold", 32, farbe=DROT, rechts=1800),
           z("richtig", 880, 180, "tab", "ExtraBold", 32, farbe=DGRUEN, rechts=1800),
           z("Fundstelle", 1500, 180, "tab", "ExtraBold", 32, farbe=TEXT, rechts=1800),
           linienzug([(110, 232), (1810, 232)], "tab", breite=3)]
y = 255
for i, (c, fa, ri, fu) in enumerate(TAB):
    h = 150
    els_tab.append(karte(110, y, 1700, h, c, fill=WEISS, rund=18, schatten=6, rand=4))
    els_tab.append(z(f"{i + 1}.", 135, y + 50, c, "ExtraBold", 40, rechts=1800))
    els_tab.append(nein(170 + 20, y + 30, c, gr=18))
    for j, t in enumerate(fa):
        els_tab.append(z(t, 240, y + 30 + 48 * j, c, "Bold", 34, rechts=840))
    els_tab.append(ok(855, y + 30, c, gr=18))
    for j, t in enumerate(ri):
        els_tab.append(z(t, 905, y + 30 + 48 * j, c, "Bold", 34, rechts=1470))
    for j, t in enumerate(fu):
        els_tab.append(z(t, 1500, y + 30 + 48 * j, c, size=30, farbe=TEXT, rechts=1800))
    y += h + 22
assert y <= 960, y
folie([("tab", "Fehlertabelle · die vier Fehler"), ("t1", "Fehlertabelle · 1. Frist"), ("t2", "Fehlertabelle · 2. öffentliches Interesse"),
       ("t3", "Fehlertabelle · 3. Verjährung"), ("t4", "Fehlertabelle · 4. Privatklage")], els_tab)

# ===========================================================================================================================
# M Prüfschema je prozessuale Tat; Reihenfolge = übliche Klausurpraxis
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Strafbarkeit und hinreichender Tatverdacht"),
          ("s2", 0, "II. Verfahrenshindernisse"),
          (beim("s2", "Strafantrag"), 1, "1. Strafantrag mit Frist (§§ 77, 77b StGB; Form § 158 Abs. 2 StPO)"),
          (beim("s2", "sonst"), 2, "sonst: besonderes öffentliches Interesse – nur relative Antragsdelikte (§ 230 StGB)"),
          (beim("s2", "Verjährung"), 1, "2. Verjährung (§§ 78 ff. StGB)"),
          (beim("s2", "Strafklageverbrauch"), 1, "3. Strafklageverbrauch (Art. 103 Abs. 3 GG)"),
          ("s3", 0, "III. Verfügung: Anklage (§ 170 Abs. 1) oder Einstellung (§ 170 Abs. 2 StPO)")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: je prozessuale Tat"), 110, 90, "sch", 46)]
y = 185
for c, ebene, text in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 78, 1: 64, 2: 64}[ebene]
y += 20
els_sch += [karte(110, y, 1700, 150, "reihe", fill=HELL, rund=18, schatten=6, rand=4),
            warnung_i(160, y + 50, "reihe", gr=22),
            z("Reihenfolge: Klausurpraxis, kein Gesetz", 210, y + 26, "reihe", "ExtraBold", 34, rechts=1800),
            z("manche prüfen den Strafantrag direkt beim Delikt – maßgeblich: Bearbeitervermerk", 210, y + 80,
              beim("reihe", "manche"), size=30, rechts=1800)]
assert y + 150 <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Strafbarkeit"), ("s2", "Prüfschema › II. Verfahrenshindernisse"),
       ("s3", "Prüfschema › III. Verfügung"), ("reihe", "Prüfschema · Reihenfolge: Klausurpraxis")], els_sch)

# ===========================================================================================================================
# N Klausurtipp (Lexi): drei Fragen je Antragsdelikt
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: 3 Fragen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("bei jedem Antragsdelikt", 200, 200, "tipp", "Bold", 36),
         blk(130, 300, 1020, 90, GELB, "k1", [("1. Antrag gestellt – vom Berechtigten?", "ExtraBold", 34, INK)]),
         blk(130, 420, 1020, 90, BLAU, "k2", [("2. Rechtzeitig – ab Kenntnis gerechnet?", "ExtraBold", 34, INK)]),
         blk(130, 540, 1020, 130, HELLGRUEN, "k3", [("3. Wenn nicht: Ausweg über das", "ExtraBold", 34, INK),
                                                   ("besondere öffentliche Interesse?", "ExtraBold", 34, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · 3 Fragen"), ("k1", "Klausurtipp › 1. Antrag gestellt?"), ("k2", "Klausurtipp › 2. rechtzeitig?"),
       ("k3", "Klausurtipp › 3. öffentliches Interesse?")], els_k)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein ", 0), ("Verfahrenshindernis", "a"), (" schlägt", 0)],
                 [("jede noch so klare Strafbarkeit.", 0)]], 750, 290, 42, "merke", {"a": beim("merke", "Verfahrenshindernis")}),
    *markertext([[("Die Antragsfrist läuft ", 0), ("3 Monate ab Kenntnis;", "b")],
                 [("das besondere öffentliche Interesse", 0)],
                 [("rettet nur ", 0), ("relative", "c"), (" Antragsdelikte.", 0)]], 750, 540, 40, "m2",
                {"b": beim("m2", "drei"), "c": beim("m2", "relative")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
