"""Folge 280 · Entschuldigender Notstand § 35: Das Brett des Karneades – Serienstandard Open Peeps (Katzenkönig).
Fall (Plan-Hook): Herr Tamm (Mitte 40) war Fahrgast auf einem Ausflugsboot, das im Sturm sinkt. Im Wasser treibt nur eine
Planke, die einen Menschen trägt; ein zweiter Schiffbrüchiger (ein Fremder) hält sich ebenfalls fest, die Planke geht unter
beiden unter. Herr Tamm stößt ihn weg, der andere kommt ums Leben; Stunden später rettet ihn ein Fischkutter.
Rahmenhandlung an Land: Hafenbüro der Wasserschutzpolizei, Kommissarin Petzold nimmt die Aussage auf.
Darstellung: kein Ertrinken, kein Stoß, keine Leiche im Bild – die See (Wellen, Planke, Sturmwolke, Kutter-Icon) ist ein
reines Symbolbild ohne Menschen; der Vorgang steht nur als Text auf Pillen.
Szenen laut ../SZENENPLAN.md: A1 Hafenbüro (Aussage), A2 Symbolbild See, A3 Hafenbüro (Frage, Karneades), B Sachverhalt,
C Tatbestand/Rechtswidrigkeit, D § 35 Abs. 1 S. 1 (Wortlautkarte), E § 35 Abs. 1 S. 2 (Wortlautkarte) Gefahrverursachung,
F besonderes Rechtsverhältnis, G Abwandlung 1 Kapitän, H Abwandlung 2 Irrtum (§ 35 Abs. 2, Wortlautkarte),
I Vermeidbarkeit (BGHSt 48, 255), J Ergebnis, K Hafenbüro (Blase Petzold), L Klausurtipp (Lexi), M Schema, N Merksatz (Lexi).
Handlungsgeräusch: Stift auf Papier, wenn Kommissarin Petzold zu schreiben beginnt (A1, szene_280stift_1);
../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 263 (gemeinsame Dateien unverändert); neu: buero(), stehpult(), see(), planke().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 08.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt


bausteine.FIGORDNER = "op_280/"

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
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_280/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
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
WAND = (230, 236, 240, 255)
HIMMEL = (214, 232, 250, 255)
SEE = (141, 179, 242, 255)
SEE2 = (112, 152, 222, 255)
HOLZ = (196, 142, 92, 255)
HOLZ2 = (150, 104, 64, 255)
PULTF = (176, 186, 200, 255)
HELLGRAU2 = (236, 236, 232, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def _welle(dr, s, x0, x1, y, amp, lang, farbe, breite):
    import math
    pts = [((x0 + k) * s, (y + amp * math.sin((x0 + k) / lang * 2 * math.pi)) * s) for k in range(0, x1 - x0 + 1, 6)]
    dr.line(pts, fill=farbe, width=breite * s, joint="curve")


def buero(c, name="buero"):
    """Hafenbüro der Wasserschutzpolizei: Wand, großes Fenster mit Blick auf das Hafenbecken (Wellenlinien), Bodenlinie;
    ohne Wappen, Logo oder Abzeichen."""
    w, h = 1800, BODEN_Y - 100

    def zz(dr, s):
        dr.rectangle((0, 0, w * s, h * s), fill=WAND)
        fx0, fy0, fw, fh = 80, 120, 600, 300
        dr.rounded_rectangle((fx0 * s, fy0 * s, (fx0 + fw) * s, (fy0 + fh) * s), 10 * s, fill=HIMMEL, outline=INK, width=6 * s)
        dr.rectangle(((fx0 + 4) * s, (fy0 + 190) * s, (fx0 + fw - 4) * s, (fy0 + fh - 4) * s), fill=SEE)
        for k, yy in enumerate((fy0 + 210, fy0 + 245, fy0 + 275)):
            _welle(dr, s, fx0 + 10, fx0 + fw - 10, yy, 5, 70 + 10 * k, (255, 255, 255, 255), 4)
        dr.line(((fx0 + fw / 2) * s, fy0 * s, (fx0 + fw / 2) * s, (fy0 + fh) * s), fill=INK, width=5 * s)
        dr.line((0, (h - 3) * s, w * s, (h - 3) * s), fill=INK, width=6 * s)
    return hart(El(_flaeche(w, h, zz), 60, 100, c, "cut", 0.0, None, name=name))


def stehpult(c, x0=760, x1=1000):
    """Stehpult der Wache (Ablage für das Klemmbrett), steht auf dem Boden."""
    w, h = x1 - x0, 300

    def zz(dr, s):
        dr.polygon([(0, 0), (w * s, 0), ((w - 14) * s, 40 * s), (14 * s, 40 * s)], fill=PULTF)
        dr.line([(0, 0), (w * s, 0), ((w - 14) * s, 40 * s), (14 * s, 40 * s), (0, 0)], fill=INK, width=5 * s)
        dr.rectangle(((w / 2 - 22) * s, 40 * s, (w / 2 + 22) * s, (h - 30) * s), fill=PULTF, outline=INK, width=5 * s)
        dr.rounded_rectangle(((w / 2 - 80) * s, (h - 32) * s, (w / 2 + 80) * s, (h - 3) * s), 8 * s, fill=PULTF, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="stehpult"))


# Symbolbild See (A2): nur Wasser, Planke, Wolke, Kutter – keine Menschen
SEE_Y = 560                                  # Wasserlinie


def see(c):
    """See als Grundfläche: Wasserfläche mit Wellenlinien, ohne Menschen."""
    w, h = 1800, 905 - SEE_Y
    def zz(dr, s):
        dr.rectangle((0, 30 * s, w * s, h * s), fill=SEE)
        _welle(dr, s, 0, w, 30, 14, 160, SEE, 30)
        _welle(dr, s, 0, w, 22, 14, 160, INK, 5)
        for k, yy in enumerate((110, 180, 250, 310)):
            _welle(dr, s, 20, w - 20, yy, 7, 120 + 20 * k, (255, 255, 255, 255), 4)
        dr.line((0, (h - 3) * s, w * s, (h - 3) * s), fill=INK, width=6 * s)
    return hart(El(_flaeche(w, h, zz), 60, SEE_Y - 30, c, "cut", 0.0, None, name="see"))


def planke(c, cx=960, y=SEE_Y - 6, bis=None, schraeg=False):
    """Die Planke (Holzbrett mit Maserung) auf der Wasserlinie; schraeg=True: unter Wasser gedrückt (halb verdeckt)."""
    w, h = 420, 46
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 12 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xx in (90, 210, 320):
            dr.line((xx * s, 14 * s, (xx + 50) * s, 14 * s), fill=HOLZ2, width=4 * s)
        dr.line((150 * s, 30 * s, 240 * s, 30 * s), fill=HOLZ2, width=4 * s)
    im = _flaeche(w, h, zz)
    if schraeg:                               # unter Wasser gedrückt: tiefer in der Wasserfläche, leicht geneigt und blasser
        im = im.rotate(-5, expand=True, resample=Image.BICUBIC)
        im.putalpha(im.getchannel("A").point(lambda v: int(v * 0.55)))
    e = El(im, cx - im.width / 2, y - h / 2 + (70 if schraeg else 0), c, "cut", 0.0, bis, name="planke" + ("_unter" if schraeg else ""))
    return e


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TA": "Herr Tamm", "PE": "Kommissarin Petzold", "KA": "Kapitän (Abwandlung)"}
NFARBE = {"TA": ORANGE, "PE": BLAU, "KA": LILA}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


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


def allein(k, folge):
    return stehend(k, FX, folge)


def bis_l(els, bis):
    for e in els:
        e.bis = bis
    return els


PA = "A. Herr Tamm, § 212 StGB"
PEX, TAX = 1110, 1600                       # Hafenbüro: Petzold (blickt nach rechts), Tamm (blickt nach links)

# ===========================================================================================================================
# A1 Fall: Hafenbüro der Wasserschutzpolizei – Aussage
# ===========================================================================================================================
folie([(NULL, "Fall · Hafenbüro der Wasserschutzpolizei"), ("tamm", "Fall · Aussage von Herrn Tamm"),
       ("pe1", "Fall · Was ist auf dem Wasser passiert?"), ("ta1", "Fall · Boot im Sturm gesunken")], [
    buero(NULL),
    stehpult(NULL),
    hart(pl("Dienstagmorgen", 70, 30, NULL, fill=WEISS, size=38)),
    hart(pl("Hafenbüro · Wasserschutzpolizei", 450, 30, NULL, fill=BLAU, size=38)),
    *fig("PE", PEX, BODEN_Y, FHA, [("petzold", "ruhig_r")], bis="pe1"),
    szene(ficon("tabler", "clipboard-text", 880, BODEN_Y - 296, 96, beim("petzold", "Aussage"), fuell=WEISS), "280stift*", 0.8, 0.0),
    ficon("tabler", "pencil", 930, BODEN_Y - 300, 56, beim("petzold", "Aussage"), fuell=GELB),
    pl("nimmt eine Aussage auf", PEX, 330, beim("petzold", "nimmt"), fill=WEISS, size=30, anker="m", bis="tamm"),
    *fig("TA", TAX, BODEN_Y, FHA, [("tamm", "muede")], bis="ta1"),
    pl("Mitte 40", TAX, 250, beim("tamm", "Mitte"), fill=WEISS, size=30, anker="m", bis="pe1"),
    pl("überlebte ein Bootsunglück", TAX, 330, beim("tamm", "Bootsunglück"), fill=ORANGE, size=30, anker="m", bis="pe1"),
    *redet("PE_redet_r", PEX, BODEN_Y, FHA, "pe1", "ta1"),
    blase("sprech", 900, 230, "pe1", 1080, 260, inhalt=["Herr Tamm, was ist draußen", "auf dem Wasser passiert?"],
          textsize=36, figur=("PE_redet_r", PEX, BODEN_Y, FHA), bis="ta1"),
    *fig("PE", PEX, BODEN_Y, FHA, [("ta1", "ernst_r")], erst="cut"),
    *redet("TA_redet", TAX, BODEN_Y, FHA, "ta1", "planke"),
    blase("sprech", 1040, 250, "ta1", 1180, 250, inhalt=["Unser Ausflugsboot ist im Sturm gesunken.",
                                                        "Im Wasser trieb nur eine einzige Planke."],
          textsize=34, figur=("TA_redet", TAX, BODEN_Y, FHA)),
    ns(NAME["PE"], PEX, BODEN_Y, "petzold", NFARBE["PE"], d=0.1),
    ns(NAME["TA"], TAX, BODEN_Y, "tamm", NFARBE["TA"], d=0.1),
])

# ===========================================================================================================================
# A2 Symbolbild See: Planke, Wellen, Sturm – keine Menschen, kein Stoß, kein Ertrinken im Bild
# ===========================================================================================================================
PS2 = "Fall · Symbolbild"
folie([("planke", f"{PS2}: Planke trägt nur 1 Menschen"), ("zweiter", f"{PS2}: 2 Schiffbrüchige an der Planke"),
       ("sinkt", f"{PS2}: Planke geht unter"), ("stoss", f"{PS2}: Herr Tamm stößt den anderen weg"),
       ("tot", f"{PS2}: der andere kommt ums Leben"), ("rettung", f"{PS2}: Rettung durch einen Fischkutter")], [
    see("planke"),
    hart(ficon("tabler", "cloud-storm", 260, 300, 190, "planke", fuell=HELLGRAU)),
    hart(pl("Symbolbild", 70, 30, "planke", fill=WEISS, size=34)),
    planke("planke", bis="sinkt"),
    pl("Die Planke trägt nur 1 Menschen", 960, 400, "planke", fill=GELB, size=34, anker="m", bis="sinkt"),
    pl("ein 2. Schiffbrüchiger, ein Fremder, hält sich fest", 960, 300, "zweiter", fill=WEISS, size=32, anker="m", bis="sinkt"),
    planke("sinkt", schraeg=True, bis="stoss"),
    pl("Unter beiden geht sie unter.", 960, 400, "sinkt", fill=HELLROT, size=34, anker="m", bis="stoss"),
    planke("stoss", bis=None),
    pl("Herr Tamm stößt den anderen weg.", 960, 400, "stoss", fill=ORANGE, size=34, anker="m", bis="tot"),
    pl("Der andere kommt ums Leben.", 960, 400, "tot", fill=HELLGRAU, size=34, anker="m", bis="rettung"),
    ficon("tabler", "ship", 1500, SEE_Y + 14, 230, "rettung", fuell=WEISS),
    pl("Stunden später: Ein Fischkutter rettet Herrn Tamm.", 960, 400, "rettung", fill=HELLGRUEN, size=34, anker="m"),
])

# ===========================================================================================================================
# A3 Hafenbüro: „Sonst wären wir beide ertrunken.“ – Frage – Brett des Karneades
# ===========================================================================================================================
folie([("ta2", "Fall · Herr Tamm: sonst beide ertrunken"), ("frage", "Fall · Strafbar wegen Totschlags?"),
       ("karneades", "Fall · Klassiker: Brett des Karneades")], [
    buero("ta2", name="buero2"),
    stehpult("ta2"),
    hart(ficon("tabler", "clipboard-text", 880, BODEN_Y - 296, 96, "ta2", fuell=WEISS)),
    hart(ficon("tabler", "pencil", 930, BODEN_Y - 300, 56, "ta2", fuell=GELB)),
    *fig("PE", PEX, BODEN_Y, FHA, [("ta2", "ernst_r"), ("frage", "skeptisch_r"), ("antik", "ruhig_r")], erst="cut"),
    *redet("TA_redet2", TAX, BODEN_Y, FHA, "ta2", "frage"),
    blase("sprech", 820, 200, "ta2", 1180, 250, inhalt=["Sonst wären wir", "beide ertrunken."], textsize=40,
          figur=("TA_redet2", TAX, BODEN_Y, FHA), bis="frage"),
    *fig("TA", TAX, BODEN_Y, FHA, [("frage", "still"), ("karneades", "skeptisch")], erst="cut"),
    pl("Totschlag, § 212 StGB?", 70, 30, "frage", fill=PINK, size=38),
    ficon("tabler", "book", 1520, 330, 110, "karneades", fuell=GELB),
    pl("Klassiker: das Brett des Karneades", 70, 110, "karneades", fill=GELB, size=38),
    pl("antikes Gedankenexperiment, zurückgeführt", 770, 230, "antik", fill=WEISS, size=28),
    pl("auf den griechischen Philosophen Karneades", 770, 290, beim("antik", "griechischen"), fill=WEISS, size=28),
    hart(ns(NAME["PE"], PEX, BODEN_Y, "ta2", NFARBE["PE"])),
    hart(ns(NAME["TA"], TAX, BODEN_Y, "ta2", NFARBE["TA"])),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_280(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_280("sv", [
    "Herr Tamm (Mitte 40) ist Fahrgast auf einem Ausflugsboot. Im Sturm sinkt das Boot. Im Wasser treibt nur eine "
    "einzige Planke, die einen Menschen tragen kann. Rettung ist nicht in Sicht.",
    "Ein zweiter Schiffbrüchiger, den Herr Tamm nicht kennt, hält sich ebenfalls an der Planke fest. Unter beiden geht "
    "sie unter. Um nicht zu ertrinken, stößt Herr Tamm den anderen weg; er weiß, dass dieser dann ertrinken wird. "
    "Der andere kommt ums Leben.",
    "Stunden später zieht ein Fischkutter Herrn Tamm aus dem Wasser. Den Untergang des Bootes hat er nicht verursacht.",
], "Hat sich Herr Tamm wegen Totschlags (§ 212 StGB) strafbar gemacht?")

# ===========================================================================================================================
# C Tatbestand und Rechtswidrigkeit
# ===========================================================================================================================
folie([("tb", f"{PA} › I. Tatbestand"), ("tb212", f"{PA} › I. Tatbestand: § 212 Abs. 1"),
       ("vors", f"{PA} › I. Tatbestand: Vorsatz"), ("rw", f"{PA} › II. Rechtswidrigkeit"),
       ("p34", f"{PA} › II. Rechtswidrigkeit: § 34 (−)")], rechts_frei([
    *tafel("tb", "Tatbestand und Rechtswidrigkeit"),
    *okz("einen Menschen getötet, § 212 Abs. 1 StGB", 200, "tb212", "Bold", 34, x=160),
    *okz("vorsätzlich", 280, "vors", "Bold", 34, x=160),
    blk(110, 380, 1040, 90, GELB, "rw", [("II. Rechtswidrigkeit: gerechtfertigt?", "ExtraBold", 36, INK)]),
    *neinz("§ 34 StGB: Leben gegen Leben nicht abwägbar", 510, "p34", "Bold", 34, x=160),
    z("Tat bleibt rechtswidrig", 160, 580, beim("p34", "abwägen"), "Bold", 34),
    zit("mehr im Video „Leben gegen Leben: Übergesetzlicher", 110, 680, "v263"),
    zit("entschuldigender Notstand“", 110, 720, "v263"),
    *requisit([("tb", ("tabler", "lifebuoy", 110, ROT), "Tatbestand", WEISS),
               ("vors", ("tabler", "eye", 100, WEISS), "Vorsatz", WEISS),
               ("rw", ("tabler", "scale", 100, GELB), "gerechtfertigt?", GELB),
               ("p34", ("tabler", "ban", 100, HELLROT), "§ 34 (−)", HELLROT)]),
    *allein("TA", [("tb", "ruhig"), ("tb212", "still"), ("rw", "skeptisch"), ("p34", "sorge")]),
]))

# ===========================================================================================================================
# D § 35 Abs. 1 S. 1 StGB (Wortlautkarte) und Subsumtion
# ===========================================================================================================================
PS_ = f"A. Herr Tamm › III. Schuld › § 35 Abs. 1 S. 1"
W35 = ("„Wer in einer gegenwärtigen, nicht anders abwendbaren Gefahr für Leben, Leib oder Freiheit eine rechtswidrige Tat "
       "begeht, um die Gefahr von sich, einem Angehörigen oder einer anderen ihm nahestehenden Person abzuwenden, handelt "
       "ohne Schuld.“")
w35, w35_y = wortlaut(80, 165, 1100, W35, "§ 35 Abs. 1 S. 1 StGB", "p35", marken=[
    ("handelt", beim("w1", "handelt")), ("ohne Schuld.", beim("w1", "ohne")), ("Leben,", beim("gefahr", "Tod")), ("gegenwärtigen,", beim("gegenw", "gegenwärtig")),
    ("nicht anders abwendbaren", beim("anders", "abwendbar")), ("von sich,", beim("eigen", "eigenes")),
    ("um die Gefahr", beim("rettw", "Rettungswillen"))], size=32)
folie([("p35", f"{PS_} · Wortlaut"), ("gefahr", f"{PS_} › Gefahr für Leben"), ("gegenw", f"{PS_} › gegenwärtig (+)"),
       ("anders", f"{PS_} › nicht anders abwendbar (+)"), ("eigen", f"{PS_} › eigene Person (+)"),
       ("rettw", f"{PS_} › Rettungswille (+)")], rechts_frei([
    *tafel("p35", "Entschuldigender Notstand"),
    *w35,
    *okz("Gefahr für Leben: droht zu ertrinken", w35_y + 20, beim("gefahr", "Tod"), "Bold", 32, x=160),
    *okz("gegenwärtig: jetzt, im Wasser", w35_y + 78, "gegenw", "Bold", 32, x=160),
    *okz("nicht anders abwendbar: keine Rettung, 1 Planke", w35_y + 136, beim("anders", "abwendbar"), "Bold", 32, x=160),
    *okz("eigenes Leben", w35_y + 194, "eigen", "Bold", 32, x=160),
    *okz("Rettungswille: „um die Gefahr abzuwenden“", w35_y + 252, beim("rettw", "Rettungswillen"), "Bold", 32, x=160),
    *requisit([("p35", ("tabler", "book", 100, WEISS), "§ 35 Abs. 1 S. 1", WEISS),
               ("gefahr", ("tabler", "heartbeat", 100, HELLROT), "Lebensgefahr", HELLROT),
               ("anders", ("tabler", "lifebuoy", 100, ROT), "nur 1 Planke", WEISS),
               ("rettw", ("tabler", "shield-check", 100, HELLGRUEN), "Rettungswille", HELLGRUEN)]),
    *allein("TA", [("p35", "ruhig"), ("gefahr", "angst"), ("anders", "sorge"), ("rettw", "still")]),
]))
assert w35_y + 310 <= 900, w35_y

# ===========================================================================================================================
# E § 35 Abs. 1 S. 2 StGB (Wortlautkarte): Hinnahmepflicht – 1. Gefahr selbst verursacht
# ===========================================================================================================================
PH = "A. Herr Tamm › III. Schuld › § 35 Abs. 1 S. 2: Hinnahmepflicht?"
W352 = ("„Dies gilt nicht, soweit dem Täter nach den Umständen, namentlich weil er die Gefahr selbst verursacht hat oder "
        "weil er in einem besonderen Rechtsverhältnis stand, zugemutet werden konnte, die Gefahr hinzunehmen; jedoch kann "
        "die Strafe nach § 49 Abs. 1 gemildert werden, wenn der Täter nicht mit Rücksicht auf ein besonderes "
        "Rechtsverhältnis die Gefahr hinzunehmen hatte.“")
MK2 = [("zugemutet werden konnte, die Gefahr hinzunehmen;", beim("s2w", "zugemutet")),
       ("die Gefahr selbst verursacht hat", beim("verurs", "selbst"))]
w352, w352_y = wortlaut(80, 165, 1100, W352, "§ 35 Abs. 1 S. 2 StGB", "satz2", marken=MK2, size=30)
folie([("satz2", f"{PH} · Wortlaut"), ("verurs", f"{PH} › 1. Gefahr selbst verursacht?"),
       ("gast", f"{PH} › 1. selbst verursacht (−)")], rechts_frei([
    *tafel("satz2", "Ausnahme: Hinnahmepflicht"),
    *w352,
    z("2 Beispiele im Gesetz:", 110, w352_y + 22, "zwei", "ExtraBold", 34),
    z("1. Gefahr selbst verursacht", 110, w352_y + 82, "verurs", "Bold", 34),
    z("bloße Ursächlichkeit genügt nicht – pflichtwidrig", 160, w352_y + 136, "kaus", size=32),
    *neinz("Herr Tamm: nur Fahrgast, Untergang nicht verursacht", w352_y + 200, "gast", "Bold", 32, x=160),
    *requisit([("satz2", ("tabler", "alert-triangle", 100, GELB), "Ausnahme", GELB),
               ("verurs", ("tabler", "cloud-storm", 110, HELLGRAU), "selbst verursacht?", WEISS),
               ("gast", ("tabler", "ship", 130, WEISS), "nur Fahrgast", HELLGRUEN)]),
    *allein("TA", [("satz2", "skeptisch"), ("verurs", "ernst"), ("gast", "ruhig")]),
]))
assert w352_y + 260 <= 900, w352_y

# ===========================================================================================================================
# F 2. besonderes Rechtsverhältnis → entschuldigt
# ===========================================================================================================================
w352b, _ = wortlaut(80, 165, 1100, W352, "§ 35 Abs. 1 S. 2 StGB", "rv",
                    marken=[("in einem besonderen", beim("rv", "besonderes")), ("Rechtsverhältnis stand,", beim("rv", "Rechtsverhältnis"))], size=30)
folie([("rv", f"{PH} › 2. besonderes Rechtsverhältnis?"), ("beruf", f"{PH} › 2. etwa Feuerwehr, Polizei, Soldaten"),
       ("frei", f"{PH} › 2. besonderes Rechtsverhältnis (−)"), ("entsch", "A. Herr Tamm › III. Schuld › § 35 (+): entschuldigt")],
      rechts_frei([
    *tafel("rv", "Ausnahme: Hinnahmepflicht"),
    *w352b,
    z("2. besonderes Rechtsverhältnis", 110, w352_y + 22, "rv", "Bold", 34),
    z("etwa Feuerwehrleute, Polizisten, Soldaten", 160, w352_y + 78, "beruf", size=32),
    z("Schutzpflichten für andere: berufstypische", 160, w352_y + 126, "pflicht", size=32),
    z("Gefahren eher hinnehmen", 160, w352_y + 170, beim("pflicht", "berufstypische"), size=32),
    *neinz("Herr Tamm: kein solches Verhältnis", w352_y + 226, "frei", "Bold", 32, x=160),
    blk(110, w352_y + 286, 1040, 80, HELLGRUEN, "entsch", [("§ 35 (+): Herr Tamm ist entschuldigt", "ExtraBold", 34, INK)]),
    *requisit([("rv", ("tabler", "id-badge-2", 100, WEISS), "besonderes Rechtsverhältnis", WEISS),
               ("beruf", ("tabler", "firetruck", 130, ROT), "Feuerwehr, Polizei, Soldaten", WEISS),
               ("frei", ("tabler", "ship", 130, WEISS), "Fahrgast: (−)", HELLGRUEN),
               ("entsch", ("tabler", "shield-check", 100, HELLGRUEN), "ohne Schuld", HELLGRUEN)]),
    *allein("TA", [("rv", "skeptisch"), ("frei", "ruhig"), ("entsch", "erleichtert")]),
]))
assert w352_y + 380 <= 900, w352_y

# ===========================================================================================================================
# G Abwandlung 1: Der Kapitän stößt einen Fahrgast von der Planke
# ===========================================================================================================================
PK = "Abwandlung 1: Kapitän › § 35 Abs. 1 S. 2"
folie([("abw1", "Abwandlung 1: Kapitän stößt Fahrgast weg"), ("kap1", f"{PK} › verantwortlich für die Sicherheit"),
       ("kap2", f"{PK} › besonderes Rechtsverhältnis (+)"), ("kap3", f"{PK} › kein Muss zum sicheren Tod?"),
       ("kap4", f"{PK} › Gefahr auf die Geschützten abgewälzt"), ("kap5", "Abwandlung 1: Kapitän › nicht entschuldigt, § 212"),
       ("kap6", "Abwandlung 1: Kapitän › keine Milderung nach S. 2")], rechts_frei([
    *tafel("abw1", "Abwandlung 1: der Kapitän"),
    z("Der Kapitän stößt einen Fahrgast von der Planke.", 110, 175, "abw1", "Bold", 32),
    *okz("verantwortlich für die Sicherheit an Bord", 255, "kap1", "Bold", 32, x=160),
    *okz("Pflicht: Schutz der Fahrgäste", 315, "kap2", "Bold", 32, x=160),
    blk(110, 380, 1040, 80, BLAU, beim("kap2", "besonderen"), [("besonderes Rechtsverhältnis (+)", "ExtraBold", 34, INK)]),
    z("zwar: niemand muss den sicheren Tod hinnehmen", 110, 495, "kap3", size=32),
    zit("(verbreitete Ansicht)", 160, 541, beim("kap3", "verbreiteter")),
    z("aber: Gefahr auf den Geschützten abgewälzt", 110, 600, "kap4", "Bold", 32),
    z("also: § 35 hilft ihm nicht", 160, 648, beim("kap4", "zugute"), "Bold", 32),
    blk(110, 715, 1040, 80, HELLROT, "kap5", [("strafbar wegen Totschlags, § 212 StGB", "ExtraBold", 34, INK)]),
    z("keine Strafmilderung nach § 35 Abs. 1 S. 2", 110, 815, "kap6", "Bold", 32),
    *requisit([("abw1", ("tabler", "steering-wheel", 110, WEISS), "Abwandlung 1", LILA),
               ("kap1", ("tabler", "lifebuoy", 100, ROT), "Sicherheit an Bord", WEISS),
               ("kap4", ("tabler", "ban", 100, HELLROT), "abgewälzt", HELLROT),
               ("kap5", ("tabler", "scale", 100, HELLROT), "§ 212 StGB", HELLROT)]),
    *allein("KA", [("abw1", "ernst"), ("kap3", "muede"), ("kap4", "still"), ("kap5", "skeptisch")]),
]))

# ===========================================================================================================================
# H Abwandlung 2: Irrtum – § 35 Abs. 2 StGB (Wortlautkarte)
# ===========================================================================================================================
PI = "Abwandlung 2: Irrtum › § 35 Abs. 2"
W35_2 = ("„Nimmt der Täter bei Begehung der Tat irrig Umstände an, welche ihn nach Absatz 1 entschuldigen würden, so wird er "
         "nur dann bestraft, wenn er den Irrtum vermeiden konnte. Die Strafe ist nach § 49 Abs. 1 zu mildern.“")
wi, wi_y = wortlaut(80, 330, 1100, W35_2, "§ 35 Abs. 2 StGB", "abs2",
                    marken=[("irrig Umstände an,", beim("w2", "irrig")), ("wenn er den Irrtum vermeiden konnte.", beim("w2", "vermeiden"))], size=32)
folie([("abw2", "Abwandlung 2: Rettungsboot übersehen"), ("objektiv", "Abwandlung 2: objektiv anders abwendbar"),
       ("abs2", f"{PI} · Wortlaut")], rechts_frei([
    *tafel("abw2", "Abwandlung 2: der Irrtum"),
    z("Ein Rettungsboot hätte beide rechtzeitig erreicht –", 110, 175, "abw2", "Bold", 32),
    z("Herr Tamm sah es in den Wellen nicht.", 110, 221, beim("abw2", "doch"), "Bold", 32),
    *neinz("objektiv anders abwendbar", 280, "objektiv", "Bold", 32, x=160),
    *wi,
    *requisit([("abw2", ("tabler", "speedboat", 140, WEISS), "Rettungsboot", WEISS),
               ("objektiv", ("tabler", "eye-off", 100, WEISS), "übersehen", WEISS),
               ("abs2", ("tabler", "book", 100, WEISS), "§ 35 Abs. 2", WEISS)]),
    *allein("TA", [("abw2", "sorge"), ("objektiv", "zu"), ("abs2", "ernst")]),
]))
assert wi_y <= 900, wi_y

# ===========================================================================================================================
# I Vermeidbarkeit (BGHSt 48, 255 Rn. 35) – Verweis 007
# ===========================================================================================================================
PV = f"{PI} › Irrtum vermeidbar?"
folie([("bgh", f"{PV} · BGHSt 48, 255"), ("streng", f"{PV} › strenge Anforderungen"), ("zeit", f"{PV} › Zeit zur Überlegung"),
       ("sek", f"{PI} › unvermeidbar: straflos"), ("verm", f"{PI} › vermeidbar: Strafe zwingend gemildert")], rechts_frei([
    *tafel("bgh", "Vermeidbar? BGHSt 48, 255"),
    z("Hat der Täter mögliche Auswege", 110, 180, "bgh", "Bold", 34),
    z("gewissenhaft geprüft?", 110, 228, beim("bgh", "gewissenhaft"), "Bold", 34),
    zit("BGH, Urt. v. 25.3.2003 – 1 StR 483/02, Rn. 35 (Haustyrannen-Fall)", 110, 284, "bgh"),
    z("Menschenleben: strenge Anforderungen", 110, 350, "streng", "Bold", 32),
    z("aber: Zeit für ruhige Überlegung zählt", 110, 405, "zeit", "Bold", 32),
    blk(110, 470, 1040, 130, HELLGRUEN, "sek", [("Sturm, Sekunden: eher unvermeidbar", "ExtraBold", 34, INK),
                                               ("also: Herr Tamm bliebe straflos", "Bold", 32, INK)]),
    blk(110, 630, 1040, 130, GELB, "verm", [("vermeidbar: strafbar, aber Strafe", "ExtraBold", 34, INK),
                                           ("zwingend gemildert, § 35 Abs. 2 S. 2, § 49 Abs. 1", "Bold", 32, INK)]),
    zit("mehr im Video „Haustyrannen-Fall: Den Peiniger im Schlaf töten?“", 110, 790, "v007"),
    *requisit([("bgh", ("tabler", "file-search", 100, WEISS), "gewissenhaft geprüft?", WEISS),
               ("zeit", ("tabler", "stopwatch", 100, WEISS), "Sekunden", WEISS),
               ("sek", ("tabler", "shield-check", 100, HELLGRUEN), "unvermeidbar: straflos", HELLGRUEN),
               ("verm", ("tabler", "scale", 100, GELB), "vermeidbar: gemildert", GELB)]),
    *allein("TA", [("bgh", "ruhig"), ("streng", "ernst"), ("sek", "still"), ("verm", "sorge")]),
]))

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis"), ("erg1", "Ergebnis › Herr Tamm: rechtswidrig"), ("erg2", "Ergebnis › Herr Tamm: entschuldigt, straflos"),
       ("erg3", "Ergebnis › Abwandlung 1: Kapitän strafbar")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Herr Tamm: Totschlag, rechtswidrig", 200, "erg1", "Bold", 34, x=160),
    blk(110, 280, 1040, 130, HELLGRUEN, "erg2", [("§ 35 Abs. 1 S. 1: entschuldigt", "ExtraBold", 36, INK),
                                                ("und bleibt straflos", "Bold", 34, INK)]),
    blk(110, 450, 1040, 130, HELLROT, "erg3", [("Abwandlung 1: Kapitän", "ExtraBold", 36, INK),
                                              ("strafbar, § 212 StGB", "Bold", 34, INK)]),
    *requisit([("erg", ("tabler", "scale", 100, WEISS), "Ergebnis", WEISS),
               ("erg2", ("tabler", "shield-check", 100, HELLGRUEN), "straflos", HELLGRUEN),
               ("erg3", ("tabler", "steering-wheel", 110, HELLROT), "Kapitän: strafbar", HELLROT)]),
    *allein("TA", [("erg", "ruhig"), ("erg1", "still"), ("erg2", "erleichtert")]),
]))

# ===========================================================================================================================
# K Hafenbüro: Kommissarin Petzold (Blase)
# ===========================================================================================================================
folie([("pe2", "Ergebnis · Hafenbüro")], [
    buero("pe2", name="buero3"),
    stehpult("pe2"),
    hart(ficon("tabler", "clipboard-text", 880, BODEN_Y - 296, 96, "pe2", fuell=WEISS)),
    hart(pl("Hafenbüro · Wasserschutzpolizei", 70, 30, "pe2", fill=BLAU, size=38)),
    *redet("PE_redet_r", PEX, BODEN_Y, FHA, "pe2", "tipp"),
    *fig("TA", TAX, BODEN_Y, FHA, [("pe2", "ruhig")], erst="cut"),
    blase("sprech", 960, 220, "pe2", 1080, 250, inhalt=["Ihre Aussage geht jetzt", "an die Staatsanwaltschaft."],
          textsize=36, figur=("PE_redet_r", PEX, BODEN_Y, FHA), bis="tipp"),
    hart(ns(NAME["PE"], PEX, BODEN_Y, "pe2", NFARBE["PE"])),
    hart(ns(NAME["TA"], TAX, BODEN_Y, "pe2", NFARBE["TA"])),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: § 35 in der Schuld", fill=HELL, size=44), warnung_i(150, 215, "tipp", gr=26),
         z("§ 35 erst nach der Rechtswidrigkeit prüfen", 200, 190, "tipp", "Bold", 34),
         blk(130, 270, 1020, 90, GELB, "t1", [("Tat bleibt rechtswidrig: Notwehr möglich", "ExtraBold", 32, INK)]),
         zit("§ 32 Abs. 2 StGB: „gegenwärtigen rechtswidrigen Angriff“", 160, 380, beim("t1", "Notwehr")),
         blk(130, 450, 1020, 90, BLAU, "t2", [("Satz 2 nicht vergessen: Hinnahmepflicht", "ExtraBold", 32, INK)]),
         z("häufiger Fehler: nur Gefahr und Personenkreis", 160, 570, "t3", "Bold", 32),
         z("geprüft, Hinnahmepflicht übersehen", 160, 618, beim("t3", "übersehen"), "Bold", 32),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · § 35 in der Schuld"), ("t1", "Klausurtipp › Notwehr gegen die Tat möglich"),
       ("t2", "Klausurtipp › Hinnahmepflicht prüfen")], els_k)

# ===========================================================================================================================
# M Klausurschema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", "I. Tatbestand, § 212 Abs. 1 StGB", 130),
          ("s2", "II. Rechtswidrigkeit: kein § 34", 130),
          ("s3", "III. Schuld: § 35 StGB", 130),
          ("s4", "1. gegenwärtige Gefahr für Leben, Leib, Freiheit", 200),
          ("s4b", "von dir oder einem Nahestehenden", 250),
          ("s5", "2. nicht anders abwendbar, Rettungswille", 200),
          ("s6", "3. keine Hinnahmepflicht, § 35 Abs. 1 S. 2", 200),
          ("s7", "4. bei Irrtum: § 35 Abs. 2", 200),
          ("s8", "IV. Ergebnis", 130)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Totschlag und entschuldigender Notstand"), 110, 90, "sch", 46)]
y = 200
for c, text, xx in REIHEN:
    cue = beim("s4", "dir") if c == "s4b" else c
    els_sch.append(z(text, xx, y, cue, "ExtraBold" if xx == 130 else "Bold", 38, rechts=1800))
    y += 84
assert y <= 960, y
folie([("sch", "Klausurschema · Totschlag, entschuldigender Notstand"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s3", "Klausurschema › III. Schuld: § 35"),
       ("s6", "Klausurschema › III. Schuld: Hinnahmepflicht"), ("s7", "Klausurschema › III. Schuld: Irrtum"),
       ("s8", "Klausurschema › IV. Ergebnis")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Brett des Karneades:", 0)], [("rechtswidrig, ", 0), ("aber entschuldigt.", "a")]], 750, 290, 44, "merke",
                {"a": beim("merke", "entschuldigt")}),
    *markertext([[("Gefahr selbst verursacht oder", 0)], [("besonderes Rechtsverhältnis:", 0)],
                 [("Gefahr ", 0), ("unter Umständen hinnehmen.", "b")]], 750, 500, 42, "m2", {"b": beim("m2", "Umständen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
