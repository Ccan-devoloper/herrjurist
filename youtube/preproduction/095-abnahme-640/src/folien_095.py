"""Folge 095 · Abnahme Werkvertrag § 640 BGB: Wirkungen und fiktive Abnahme – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Susanne (Verbraucherin) lässt ihr Bad vom Fliesenleger Herrn Fiedler sanieren (Rechnung 3.800 €); hinter der
Tür ist eine Fuge etwas breiter und ungleichmäßig (Schönheitsfehler, Nachbessern 150 €); E-Mail mit Frist zur Abnahme
(2 Wochen) und Hinweis auf die Folgen.
Szenen laut ../SZENENPLAN.md: A1 Das neue Bad, A2 Die E-Mail/Frage, B Sachverhalt, C Begriff, D § 640 Abs. 1 (Wortlaut),
E1 § 640 Abs. 2 Satz 1 (Wortlaut), E2 Verbraucher (Wortlaut Satz 2), E3 Mangel genannt/endgültige Verweigerung,
F Vorbehalt § 640 Abs. 3, G1/G2 Wirkungen 1–5, H Ergebnis (§ 641 Abs. 3), I Klausurtipp (Lexi), J Klausurschema,
K Merksatz (Lexi). Ein Handlungsgeräusch (Rechnung wird übergeben; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 086 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_095/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (250, 205, 198, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_095/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083) ------------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
SU_N, FI_N = ROT, BLAU                      # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SU": "Susanne", "FI": "Herr Fiedler"}
NFARBE = {"SU": SU_N, "FI": FI_N}


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel SU/FI."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


def fliesenwand(x0, y0, w, h, cue, kachel=110, fill=(226, 238, 250, 255), fuge=(150, 150, 158, 255), breit=None, bis=None,
                alt=False):
    """Bad-Wand im Aufriss: Fliesenraster mit Fugen (programmatisch, Palettengrau). breit = (Spalte, Zeile von, Zeile bis):
    diese senkrechte Fuge ist breiter und ungleichmäßig (der optische Mangel). alt = alte, vergilbte Wand ohne Fliesen."""
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    if alt:
        dr.rectangle((0, 0, w * s, h * s), fill=(232, 214, 178, 255))
        for i, (a, b) in enumerate([(0.18, 0.30), (0.55, 0.22), (0.72, 0.60), (0.30, 0.70)]):
            cx, cy = a * w * s, b * h * s
            dr.ellipse((cx - 40 * s, cy - 18 * s, cx + 40 * s, cy + 18 * s), fill=(214, 192, 150, 255))
    else:
        dr.rectangle((0, 0, w * s, h * s), fill=fill)
        for x in range(kachel, w, kachel):
            dr.line((x * s, 0, x * s, h * s), fill=fuge, width=3 * s)
        for y in range(h - kachel, 0, -kachel):
            dr.line((0, y * s, w * s, y * s), fill=fuge, width=3 * s)
        if breit:
            sp, z0, z1 = breit
            x = sp * kachel
            ya, yb = h - z1 * kachel, h - z0 * kachel
            pts = [((x + (3, -2, 4, 0, -3, 2, -1, 3, 0)[i]) * s, (ya + (yb - ya) * i / 8) * s) for i in range(9)]
            dr.line(pts, fill=(118, 118, 126, 255), width=12 * s, joint="curve")
    dr.rectangle((0, 0, w * s - 1, h * s - 1), outline=INK, width=5 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x0, y0, cue, "cut", 0.0, bis, name="wand:" + ("alt" if alt else "fliesen"))


def tuer(x0, unten, cue, w=175, h=450):
    """Badezimmertür im Aufriss (programmatisch: Türblatt in Palettengelb, Tuschekontur, Klinke)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 10 * s, fill=GELB, outline=INK, width=5 * s)
    dr.rounded_rectangle((26 * s, 30 * s, (w - 14) * s, (h * 0.45) * s), 8 * s, outline=INK, width=3 * s)
    dr.rounded_rectangle((26 * s, (h * 0.52) * s, (w - 14) * s, (h - 20) * s), 8 * s, outline=INK, width=3 * s)
    dr.rounded_rectangle(((w - 40) * s, (h * 0.47) * s, (w - 6) * s, (h * 0.47 + 12) * s), 5 * s, fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x0 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tuer")


# A1 Fall: das neue Bad ------------------------------------------------------------------------------------------------
WX, WY, WW, WH, K = 80, 200, 880, 660, 110             # Wand: links oben, Breite, Höhe, Kachel
FUGE = (7, 1, 4)                                       # breite Fuge: senkrechte Fuge 7 (letzte vor der Tür), Zeilen 1–4
FUX, FUY = WX + FUGE[0] * K, WY + WH - int(2.5 * K)    # Mitte der breiten Fuge
FIX, SUX = 1440, 1740                                  # Fiedler (blickt nach rechts), Susanne (blickt nach links)
NEU = beim("neu", "Neue")
WANNE = beim("neu", "Wanne")
RECH = beim("fi1", "Rechnung")
FI_HAND = hand("FI_redet_r", FIX, BODEN, FH, +1)
SU_HAND = hand("SU_ruhig", SUX, BODEN, FH, -1)
folie([(NULL, "Fall · Das neue Bad"), ("pruef", "Fall · Die Fuge hinter der Tür")], [
    hart(pl("Susanne lässt ihr Bad sanieren", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(fliesenwand(WX, WY, WW, WH, NULL, alt=True, bis=NEU)),
    fliesenwand(WX, WY, WW, WH, NEU, kachel=K, breit=FUGE),
    hart(tuer(975, BODEN, NULL)),
    hart(ficon("tabler", "bucket", 1290, BODEN, 90, NULL, fuell=WEISS)),
    hart(ficon("tabler", "trowel", 1290, BODEN - 100, 70, NULL, fuell=WEISS)),
    pl("neue Fliesen an Wand und Boden", 70, 118, NEU, fill=WEISS, size=32),
    ficon("ph", "bathtub", 400, BODEN, 360, WANNE, fuell=WEISS),
    pl("neue Wanne", 400, 470, WANNE, fill=WEISS, size=30, anker="m"),
    # Fiedler (links, blickt zu Susanne)
    *fig("FI", FIX, BODEN, FH, [(NULL, "ruhig_r")], bis="fi1", erst="cut"),
    hart(ns("Herr Fiedler", FIX, BODEN, NULL, FI_N)),
    *redet("FI_redet_r", FIX, BODEN, FH, "fi1", "pruef"),
    *fig("FI", FIX, BODEN, FH, [("pruef", "froh_r"), ("su1", "ernst_r")], erst="cut"),
    blase("sprech", 640, 200, "fi1", 1210, 245, inhalt=["Fertig! Hier ist meine", "Rechnung: 3.800 €."], textsize=36,
          figur=("FI_redet_r", FIX, BODEN, FH), bis="pruef"),
    # die Rechnung wandert von Fiedler zu Susanne
    szene(bewegt(ficon("tabler", "receipt-euro", SU_HAND[0] - 10, SU_HAND[1] + 45, 80, RECH, fuell=WEISS),
                 RECH, (RECH[0], RECH[1] + 0.8), FI_HAND[0] - SU_HAND[0] + 20, FI_HAND[1] - SU_HAND[1]), "095rechnung*", 0.7, 0.0),
    pl("3.800 €", 1700, 110, beim("fi1", "dreitausendachthundert"), fill=GELB, size=40, anker="m", bis="su1"),
    # Susanne (rechts, blickt zu Fiedler und zur Wand)
    *fig("SU", SUX, BODEN, FH, [(NULL, "ruhig"), ("pruef", "denkt"), ("schoen", "sorge")], bis="su1", erst="cut"),
    hart(ns("Susanne", SUX, BODEN, NULL, SU_N)),
    *redet("SU_redet", SUX, BODEN, FH, "su1", "mail"),
    # die Fuge hinter der Tür
    ficon("ph", "magnifying-glass", FUX - 150, FUY + 60, 110, "pruef", fuell=WEISS),
    ring(FUX, FUY, 46, 140, "fuge", farbe=ROT, breite=7),
    pl("Fuge hinter der Tür: breiter, ungleichmäßig", 110, 230, "fuge", fill=WEISS, size=30),
    pl("reiner Schönheitsfehler", 110, 300, "schoen", fill=GRUEN, size=30),
    pl("Nachbessern: 150 €", 110, 370, beim("schoen", "hundertfünfzig"), fill=WEISS, size=30),
    blase("sprech", 660, 250, "su1", 1440, 230, inhalt=["Die Fuge hinter der Tür ist", "nicht sauber. Muss ich da",
                                                     "gleich alles zahlen?"], textsize=34,
          figur=("SU_redet", SUX, BODEN, FH), bis="mail"),
])

# A2 Fall: die E-Mail, die Frage ---------------------------------------------------------------------------------------
MX0, MY0, MW, MH = 80, 120, 1100, 540
folie([("mail", "Fall · Die E-Mail"), ("frage", "Fall · Die Frage")], [
    pl("Am nächsten Tag", 70, 30, "mail", fill=GELB, size=44),
    karte(MX0, MY0, MW, MH, "mail", fill=WEISS, rund=18, schatten=8),
    ficon("tabler", "mail", MX0 + 58, MY0 + 70, 56, "mail", fuell=GELB),
    z("E-Mail von Fliesen Fiedler", MX0 + 110, MY0 + 22, "mail", "Bold", 34, rechts=MX0 + MW - 16),
    z("Betreff: Abnahme Ihres Bades", MX0 + 30, MY0 + 90, "mail", size=32, rechts=MX0 + MW - 16),
    linienzug([(MX0 + 4, MY0 + 145), (MX0 + MW - 4, MY0 + 145)], "mail", breite=4),
    z("Bitte nehmen Sie das Bad innerhalb von", MX0 + 30, MY0 + 170, "frist", "Bold", 36, rechts=MX0 + MW - 16),
    z("2 Wochen ab.", MX0 + 30, MY0 + 222, beim("frist", "zwei"), "Bold", 36, rechts=MX0 + MW - 16),
    z("Hinweis: Wer schweigt oder die Abnahme ohne", MX0 + 30, MY0 + 310, "hinw", size=34, rechts=MX0 + MW - 16),
    z("Angabe eines Mangels verweigert, bei dem gilt", MX0 + 30, MY0 + 360, beim("hinw", "Angabe"), size=34, rechts=MX0 + MW - 16),
    z("das Bad als abgenommen.", MX0 + 30, MY0 + 410, beim("hinw", "Bad"), size=34, rechts=MX0 + MW - 16),
    *requisit([("mail", ("tabler", "mail", 110, WEISS), "E-Mail", WEISS),
               ("frist", ("tabler", "calendar-event", 100, WEISS), "Frist: 2 Wochen", GELB),
               ("frage", ("ph", "question", 100, PINK), "Abnahme?", PINK)]),
    *fig("SU", 1570, FB, FR, [("mail", "ruhig"), ("frist", "denkt"), (beim("hinw", "gilt"), "staunt"), ("frage", "sorge")]),
    ns("Susanne", 1570, FB, "mail", SU_N, d=0.1),
    pl("Abnehmen und zahlen?", 630, 730, "frage", fill=PINK, size=40, anker="m"),
    pl("Und wenn sie schweigt?", 630, 820, "frage2", fill=WEISS, size=36, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------
def sachverhalt_095(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_095("sv", [
    "Susanne lässt das Bad ihrer Wohnung vom Fliesenleger Herrn Fiedler sanieren: neue Fliesen an Wand und Boden, dazu "
    "eine neue Wanne. Als er fertig ist, gibt er ihr die Rechnung über 3.800 Euro, in der alle Posten aufgelistet sind.",
    "Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig. Das ist ein reiner Schönheitsfehler, das Bad ist dicht "
    "und voll nutzbar. Nachbessern kostet 150 Euro.",
    "Am nächsten Tag schreibt Herr Fiedler ihr eine E-Mail: Sie möge das Bad innerhalb von 2 Wochen abnehmen. Dazu der "
    "Hinweis: Wer schweigt oder die Abnahme ohne Angabe eines Mangels verweigert, bei dem gilt das Bad als abgenommen.",
], "Muss Susanne abnehmen und zahlen, und was gilt, wenn sie schweigt?")

# C Begriff -------------------------------------------------------------------------------------------------------------
folie([("begr", "Abnahme › Begriff")], rechts_frei([
    *tafel("begr", "Was ist Abnahme?"),
    z("1. körperliche Entgegennahme des Werks", 110, 200, "b1", "Bold", 38),
    z("2. Billigung als im Wesentlichen vertragsgemäß", 110, 270, "b2", "Bold", 38),
    zit("BGH, Urt. v. 5.6.2014 – VII ZR 276/13, Rn. 21", 160, 326, beim("b2", "vertragsgemäß")),
    linienzug([(110, 400), (1150, 400)], "b3", breite=3),
    *okz("ausdrücklich", 430, "b3", "Bold", 36, x=160),
    *okz("stillschweigend durch schlüssiges Verhalten", 500, "b4", "Bold", 36, x=160),
    z("meist erst nach angemessener Prüfzeit", 160, 556, beim("b4", "meist"), size=34),
    zit("BGH, Urt. v. 25.2.2010 – VII ZR 64/09, Rn. 21 f.", 160, 608, beim("b4", "meist")),
    *requisit([("begr", ("tabler", "zoom-question", 100, WEISS), "Begriff", WEISS),
               ("b1", ("tabler", "hand-grab", 100, WEISS), "entgegennehmen", WEISS),
               ("b2", ("tabler", "thumb-up", 100, GRUEN), "billigen", GRUEN)]),
    *paar("begr", "SU", [("begr", "ruhig"), ("b2", "denkt")], "FI", [("begr", "ruhig"), ("b2", "froh")]),
]))

# D § 640 Abs. 1 (Wortlaut), Subsumtion -------------------------------------------------------------------------------
W640A = ["„(1) Der Besteller ist verpflichtet, das vertragsmäßig hergestellte",
         "Werk abzunehmen, sofern nicht nach der Beschaffenheit des Werkes",
         "die Abnahme ausgeschlossen ist. Wegen unwesentlicher Mängel kann",
         "die Abnahme nicht verweigert werden.“"]
w640a, w640a_y = wortlaut(80, 170, 1100, W640A, "§ 640 Abs. 1 BGB", "p640", marken=[
    (0, "verpflichtet", beim("p640", "verpflichtet")), (2, "Wegen unwesentlicher Mängel", "p640b"),
    (3, "nicht verweigert", beim("p640b", "nicht"))], size=32)
folie([("p640", "Abnahme › Pflicht, § 640 Abs. 1 BGB"), ("fsub", "§ 640 Abs. 1 BGB › die Fuge")], rechts_frei([
    *tafel("p640", "§ 640 Abs. 1 BGB: Pflicht zur Abnahme"),
    *w640a,
    z("Abnahme ist Pflicht; verweigern nur wegen", 110, w640a_y + 30, "pfl", "Bold", 36),
    z("eines wesentlichen Mangels", 160, w640a_y + 82, beim("pfl", "wesentlichen"), "Bold", 36),
    *okz("Fuge: Mangel, aber nur optisch", w640a_y + 170, "fsub", "Bold", 34, x=160),
    *okz("Bad dicht und voll nutzbar", w640a_y + 228, beim("fsub", "Bad"), "Bold", 34, x=160),
    blk(110, w640a_y + 310, 1040, 100, GRUEN, "unw", [("unwesentlich: Susanne muss abnehmen", "ExtraBold", 38, INK)]),
    *requisit([("p640", ("tabler", "gavel", 100, WEISS), "Pflicht", WEISS),
               ("fsub", ("tabler", "grid-pattern", 100, WEISS), "Fuge: optisch", WEISS),
               ("unw", ("tabler", "checks", 100, GRUEN), "abnehmen", GRUEN)]),
    *paar("p640", "SU", [("p640", "ruhig"), ("pfl", "denkt"), ("unw", "sorge")], "FI", [("p640", "ruhig"), ("unw", "froh")]),
]))

# E1 § 640 Abs. 2 Satz 1 (Wortlaut) -----------------------------------------------------------------------------------
W640B = ["„(2) Als abgenommen gilt ein Werk auch, wenn der Unternehmer dem",
         "Besteller nach Fertigstellung des Werks eine angemessene Frist zur",
         "Abnahme gesetzt hat und der Besteller die Abnahme nicht innerhalb",
         "dieser Frist unter Angabe mindestens eines Mangels verweigert hat. …“"]
w640b, w640b_y = wortlaut(80, 250, 1100, W640B, "§ 640 Abs. 2 Satz 1 BGB", "w640", marken=[
    (1, "nach Fertigstellung", beim("w640", "Fertigstellung")), (1, "angemessene Frist", beim("w640", "angemessene")),
    (3, "unter Angabe mindestens eines Mangels", beim("w640", "Angabe"))], size=32)
folie([("fikt", "Abnahme › fiktive Abnahme, § 640 Abs. 2 Satz 1 BGB")], rechts_frei([
    *tafel("fikt", "§ 640 Abs. 2 BGB: fiktive Abnahme"),
    z("Und wenn der Besteller schweigt?", 110, 180, "fikt", "Bold", 38),
    *w640b,
    z("1. Fertigstellung", 160, w640b_y + 30, beim("w640", "Fertigstellung"), "Bold", 34),
    z("2. angemessene Frist zur Abnahme", 160, w640b_y + 84, beim("w640", "angemessene"), "Bold", 34),
    z("3. keine Verweigerung unter Angabe eines Mangels", 160, w640b_y + 138, beim("w640", "Angabe"), "Bold", 34),
    *requisit([("fikt", ("tabler", "hourglass", 90, WEISS), "Schweigen?", WEISS),
               ("w640", ("tabler", "calendar-event", 100, WEISS), "Frist", WEISS)]),
    *paar("fikt", "SU", [("fikt", "denkt")], "FI", [("fikt", "ruhig"), (beim("w640", "Angabe"), "denkt")]),
]))

# E2 Verbraucher: § 640 Abs. 2 Satz 2 (Wortlaut), Subsumtion ------------------------------------------------------------
W640S2 = ["„Ist der Besteller ein Verbraucher, so treten die Rechtsfolgen des",
          "Satzes 1 nur dann ein, wenn der Unternehmer den Besteller zusammen",
          "mit der Aufforderung zur Abnahme auf die Folgen einer nicht erklärten",
          "oder ohne Angabe von Mängeln verweigerten Abnahme hingewiesen hat;",
          "der Hinweis muss in Textform erfolgen.“"]
w640s2, w640s2_y = wortlaut(80, 160, 1100, W640S2, "§ 640 Abs. 2 Satz 2 BGB", "verb", marken=[
    (1, "zusammen", beim("verb", "zusammen")), (2, "auf die Folgen", beim("verb", "Folgen")),
    (4, "in Textform", beim("verb", "Textform"))], size=30)
folie([("verb", "fiktive Abnahme › Verbraucher, § 640 Abs. 2 Satz 2 BGB"), ("schw", "fiktive Abnahme › Susanne schweigt")],
      rechts_frei([
    *tafel("verb", "Verbraucher: Hinweis in Textform"),
    *w640s2,
    *okz("Susanne: Verbraucherin (§ 13 BGB)", w640s2_y + 24, "vsub", "Bold", 34, x=160),
    *okz("nach Fertigstellung, Frist 2 Wochen, mit Hinweis", w640s2_y + 82, beim("vsub", "Die"), "Bold", 34, x=160),
    *okz("E-Mail wahrt grundsätzlich die Textform", w640s2_y + 140, beim("vsub", "Eine"), "Bold", 34, x=160),
    zit("§ 126b BGB; BGH, Urt. v. 11.3.2026 – I ZR 202/25, Rn. 20", 160, w640s2_y + 190, beim("vsub", "Textform")),
    blk(110, w640s2_y + 250, 1040, 90, GELB, "schw", [("Schweigen bis Fristende: gilt als abgenommen", "ExtraBold", 34, INK)]),
    *requisit([("verb", ("tabler", "mail", 110, WEISS), "Hinweis", WEISS),
               ("vsub", ("tabler", "user-check", 100, WEISS), "Verbraucherin", WEISS),
               ("schw", ("tabler", "hourglass", 90, GELB), "gilt als abgenommen", GELB)]),
    *paar("verb", "SU", [("verb", "ruhig"), ("vsub", "denkt"), ("schw", "staunt")], "FI", [("verb", "ruhig"), ("schw", "froh")]),
]))

# E3 Mangel genannt; endgültige Verweigerung ----------------------------------------------------------------------------
folie([("mang", "fiktive Abnahme › Verweigerung unter Angabe eines Mangels"),
       ("endg", "Abnahmepflicht › endgültige Verweigerung")], rechts_frei([
    *tafel("mang", "Und wenn Susanne die Fuge nennt?"),
    *neinz("keine fiktive Abnahme", 200, beim("mang", "tritt"), "Bold", 38, x=160),
    z("1 Mangel genügt, auch ein unwesentlicher", 110, 290, "ein", "Bold", 36),
    zit("BT-Drs. 18/11437, S. 40; BT-Drs. 18/8486, S. 48", 160, 342, beim("ein", "unwesentlicher")),
    z("missbräuchlich nur: offensichtlich nicht bestehende", 110, 405, beim("ein", "Missbräuchlich"), size=34),
    z("oder eindeutig unwesentliche Mängel", 160, 455, beim("ein", "eindeutig"), size=34),
    blk(110, 540, 1040, 100, GELB, "endg", [("aber: Abnahmepflicht bleibt", "ExtraBold", 38, INK)]),
    z("zu Unrecht endgültig verweigert: Werklohn fällig", 110, 680, beim("endg", "Verweigert"), "Bold", 36),
    zit("BGH, Beschl. v. 18.5.2010 – VII ZR 158/09, Rn. 5", 160, 734, beim("endg", "Bundesgerichtshof")),
    *requisit([("mang", ("tabler", "grid-pattern", 100, WEISS), "Fuge genannt", WEISS),
               ("endg", ("tabler", "cash-banknote", 110, GRUEN), "trotzdem fällig", GRUEN)]),
    *paar("mang", "SU", [("mang", "ruhig"), ("ein", "froh"), ("endg", "sorge")], "FI", [("mang", "sorge"), ("endg", "ruhig")]),
]))

# F Vorbehalt, § 640 Abs. 3 --------------------------------------------------------------------------------------------
folie([("vorb", "Abnahme › Vorbehalt, § 640 Abs. 3 BGB")], rechts_frei([
    *tafel("vorb", "§ 640 Abs. 3 BGB: Vorbehalt"),
    blk(110, 190, 1040, 100, GELB, beim("vorb", "Abnehmen"), [("Abnehmen, aber unter Vorbehalt", "ExtraBold", 40, INK)]),
    z("Mangel bekannt und bei der Abnahme", 110, 350, "p640c", "Bold", 36),
    z("kein Vorbehalt:", 160, 402, beim("p640c", "nicht"), "Bold", 36),
    *neinz("verloren: Nacherfüllung, Selbstvornahme,", 480, beim("p640c", "verliert"), "Bold", 34, x=160),
    z("Rücktritt und Minderung (§ 634 Nr. 1–3 BGB)", 160, 532, beim("p640c", "Rücktritt"), size=34),
    *okz("bleibt: Schadensersatz (§ 634 Nr. 4 BGB)", 620, "se", "Bold", 34, x=160),
    *requisit([("vorb", ("tabler", "writing", 110, WEISS), "Vorbehalt", GELB),
               ("p640c", ("tabler", "alert-triangle", 100, GELB), "ohne Vorbehalt?", WEISS)]),
    *paar("vorb", "SU", [("vorb", "denkt"), ("se", "ruhig")], "FI", [("vorb", "ruhig")]),
]))

# G1 Wirkungen 1–2 -------------------------------------------------------------------------------------------------------
folie([("wirk", "Abnahme › Wirkungen"), ("w1", "Wirkungen › 1. Fälligkeit, § 641 Abs. 1 BGB"),
       ("w2", "Wirkungen › 2. Gefahrübergang, § 644 BGB")], rechts_frei([
    *tafel("wirk", "Wirkungen der Abnahme"),
    z("1. Vergütung fällig, § 641 Abs. 1 BGB", 110, 200, "w1", "Bold", 38),
    z("Bauvertrag: auch prüffähige Schlussrechnung,", 160, 262, "bau", size=34),
    z("§ 650g Abs. 4 BGB", 160, 310, beim("bau", "Paragraf"), size=34),
    *okz("Rechnung mit allen Posten liegt vor", 372, beim("bau", "Rechnung"), "Bold", 34, x=160),
    linienzug([(110, 450), (1150, 450)], "w2", breite=3),
    z("2. Gefahrübergang, § 644 Abs. 1 Satz 1 BGB", 110, 480, "w2", "Bold", 38),
    z("bis zur Abnahme: Risiko des Unternehmers", 160, 542, "w2b", size=34),
    z("z. B. Rohrbruch zerstört die Fliesen", 160, 594, beim("w2b", "Rohrbruch"), size=34),
    *requisit([("wirk", ("tabler", "list-numbers", 100, WEISS), "5 Wirkungen", WEISS),
               ("w1", ("tabler", "cash-banknote", 110, GRUEN), "fällig", GRUEN),
               ("bau", ("tabler", "receipt-euro", 90, WEISS), "Schlussrechnung", WEISS),
               ("w2", ("tabler", "shield", 100, WEISS), "Gefahr", WEISS),
               (beim("w2b", "Rohrbruch"), ("tabler", "droplet", 90, BLAU), "Rohrbruch", BLAU)]),
    *paar("wirk", "SU", [("wirk", "ruhig"), (beim("w2b", "Rohrbruch"), "staunt")],
          "FI", [("wirk", "ruhig"), ("w1", "froh"), (beim("w2b", "Rohrbruch"), "sorge")]),
]))

# G2 Wirkungen 3–5 -------------------------------------------------------------------------------------------------------
folie([("w3", "Wirkungen › 3. Verjährung, § 634a Abs. 2 BGB"), ("w4", "Wirkungen › 4. Beweislast"),
       ("w5", "Wirkungen › 5. Mängelrechte, § 634 BGB")], rechts_frei([
    *tafel("w3", "Wirkungen der Abnahme"),
    z("3. Verjährung beginnt, § 634a Abs. 2 BGB", 110, 190, "w3", "Bold", 38),
    z("2 Jahre: Arbeiten an einer Sache, 5 Jahre: Bauwerk", 160, 248, "w3b", size=34),
    zit("§ 634a Abs. 1 Nr. 1, 2 BGB", 160, 296, beim("w3b", "fünf")),
    z("4. Beweislast kehrt sich um", 110, 360, "w4", "Bold", 38),
    z("vorher: Unternehmer beweist Mangelfreiheit", 160, 418, beim("w4", "Vor"), size=34),
    z("danach: Besteller beweist den Mangel,", 160, 470, "w4b", size=34),
    z("außer bei vorbehaltenen Mängeln", 160, 522, beim("w4b", "außer"), size=34),
    zit("BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Rn. 36", 160, 572, beim("w4", "Bundesgerichtshof")),
    z("5. Ende des Erfüllungsstadiums:", 110, 636, "w5", "Bold", 38),
    z("statt Herstellung grundsätzlich Mängelrechte, § 634 BGB", 160, 694, beim("w5", "Statt"), size=34),
    zit("BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Leitsatz 1 (Rn. 31), Rn. 35", 160, 744, beim("w5", "Mängelrechte")),
    *requisit([("w3", ("tabler", "hourglass", 90, WEISS), "Verjährung läuft", WEISS),
               ("w4", ("ph", "scales", 120, WEISS), "Beweislast", WEISS),
               ("w5", ("tabler", "tool", 100, WEISS), "Mängelrechte", GRUEN)]),
    *paar("w3", "SU", [("w3", "ruhig"), ("w4b", "denkt"), ("w5", "ruhig")], "FI", [("w3", "ruhig"), ("w4b", "froh")]),
]))

# H Ergebnis ---------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Abnahme unter Vorbehalt"), ("zbr", "Ergebnis › § 641 Abs. 3 BGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Susanne nimmt ab, Vorbehalt: die Fuge", 190, "erg", "Bold", 36, x=160),
    *okz("Werklohn fällig", 250, "erg2", "Bold", 36, x=160),
    *okz("Herr Fiedler muss den Mangel beseitigen", 310, beim("erg2", "verlangen"), "Bold", 36, x=160),
    zit("§ 634 Nr. 1, § 635 BGB", 160, 364, beim("erg2", "beseitigt")),
    linienzug([(110, 430), (1150, 430)], "zbr", breite=3),
    z("§ 641 Abs. 3 BGB: angemessener Teil zurück,", 110, 455, "zbr", "Bold", 36),
    z("in der Regel das Doppelte der Kosten", 160, 507, beim("zbr", "Doppelte"), size=36),
    blk(110, 580, 1040, 90, WEISS, "zbr2", [("2 × 150 € = 300 € zurückhalten", "ExtraBold", 38, INK)]),
    blk(110, 690, 1040, 90, GRUEN, beim("zbr2", "Jetzt"), [("jetzt 3.500 €, Rest nach der Nachbesserung", "ExtraBold", 36, INK)]),
    *requisit([("erg", ("tabler", "writing", 110, WEISS), "Vorbehalt", GELB),
               ("erg2", ("tabler", "cash-banknote", 110, GRUEN), "fällig", GRUEN),
               ("zbr", ("tabler", "coins", 100, GELB), "300 € zurück", GELB)]),
    *paar("erg", "SU", [("erg", "froh"), ("zbr", "denkt"), (beim("zbr2", "Jetzt"), "froh")],
          "FI", [("erg", "ruhig"), ("zbr", "sorge"), (beim("zbr2", "Jetzt"), "ruhig")]),
]))

# I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Abnahme bei der Fälligkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Abnahme beim Werklohn unter der Fälligkeit", 200, 200, beim("tipp", "Abnahme"), "Bold", 36),
    z("Reihenfolge:", 200, 290, "tipp2", "Bold", 36),
    z("1. erklärt oder stillschweigend", 240, 345, beim("tipp2", "erklärt"), size=36),
    z("2. fiktiv, § 640 Abs. 2 BGB", 240, 400, beim("tipp2", "fiktiv"), size=36),
    z("3. zu Unrecht endgültig verweigert", 240, 455, beim("tipp2", "Unrecht"), size=36),
    z("Mängelrechte: zuerst „Ist schon abgenommen?“", 200, 560, "tipp3", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# J Klausurschema ---------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Fälligkeit"), ("k3", "Klausurschema › III. Durchsetzbarkeit")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Werklohn, § 631 Abs. 1 BGB"), 110, 90, "sch", 46),
    z("I. Anspruch entstanden: wirksamer Werkvertrag", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("II. Fälligkeit, § 641 Abs. 1 BGB", K1, 290, "k2", "Bold", 40, rechts=1820),
    z("Abnahme:", K2, 360, "k2a", "Bold", 38, rechts=1820),
    z("1. erklärt oder stillschweigend", K2 + 40, 420, "k2a", size=38, rechts=1820),
    z("2. fiktiv, § 640 Abs. 2 BGB", K2 + 40, 480, "k2b", size=38, rechts=1820),
    z("3. zu Unrecht endgültig verweigert", K2 + 40, 540, "k2c", size=38, rechts=1820),
    z("III. Durchsetzbarkeit", K1, 630, "k3", "Bold", 40, rechts=1820),
    z("Leistungsverweigerungsrecht, § 641 Abs. 3 BGB", K2, 700, beim("k3", "Leistungsverweigerungsrecht"), size=38, rechts=1820),
])

# K Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Abnahme ist die ", 0), ("Zäsur", "a")], [("im Werkvertrag.", 0)]],
                750, 290, 46, "merke", {"a": beim("merke", "Zäsur")}),
    *markertext([[("Lohn ", 0), ("fällig,", "b"), (" Gefahr über,", 0)], [("Verjährung beginnt, Beweislast wechselt.", 0)]],
                750, 480, 42, "mk2", {"b": beim("mk2", "fällig")}),
    *markertext([[("Wer auf die Frist ", 0), ("schweigt,", "c")], [("riskiert die fiktive Abnahme.", 0)]],
                750, 680, 42, "mk3", {"c": beim("mk3", "schweigt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
