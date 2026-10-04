"""Folge 190 · Kontrolleur stürzt bei Verfolgung: Die Verfolgerfälle (§ 823 I BGB) – Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv, nach dem Plan-Hook): Kontrolleur Wendelin trifft im U-Bahnhof den Fahrgast Anselm ohne gültigen Fahrschein;
Anselm läuft zur Treppe am Ausgang, Wendelin rennt hinterher (2 Stufen auf einmal) und stürzt; Arm gebrochen, 6 Wochen
Armschlinge. Szenen laut ../SZENENPLAN.md: A1 Bahnsteig, A2 Treppe (Sturz nicht gezeigt: nur Treppen-Icon und Text
„stürzt“), A3 danach, B Sachverhalt, C Problem, D Wortlautkarte § 823 Abs. 1 BGB, E Kausalität, F Herausforderungsformel,
G Im Fall, H Verschulden, I Gegenbeispiele, J Wortlautkarte § 254 Abs. 1 BGB, K Ergebnis, L Ausblick, M Klausurtipp (Lexi),
N Prüfschema, O Merksatz (Lexi).
DARSTELLUNG: U-Bahnhof fiktiv ohne Namen und Logos (Zug als Tabler-Icon), kein Sturzbild, keine Gewalt, Fahrgast ohne
Klischee; zwei Handlungsgeräusche (Zug hält, Laufschritte; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 187 (gemeinsame Dateien unverändert); neu: bahnsteig(), deckenband().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_190/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_190/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch für Wortlautkarten (Wortlaut bleibt unverändert)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur] if cur else zeilen


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149) ------------------------------------
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



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante

NAME = {"WD": "Wendelin", "WS": "Wendelin", "AS": "Anselm", "AL": "Anselm"}
NFARBE = {"WD": BLAU, "WS": BLAU, "AS": GRUEN, "AL": GRUEN}


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


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


def zwei(folge_ws, folge_as):
    """Wendelin (mit Armschlinge) und Anselm rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("WS", X1, folge_ws), *stehend("AS", X2, folge_as)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_F = (214, 214, 208, 255)
G0 = 770                                     # Bahnsteigkante (Oberfläche)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def _hart_wenn(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def bahnsteig(c):
    """Seitenansicht: Bahnsteig mit Fliesenfugen und gelber Sicherheitslinie (Grundform, Tuschekontur oben)."""
    im = Image.new("RGBA", (1860, 130))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860, 130), fill=BODEN_F)
    dr.line((0, 2, 1860, 2), fill=INK, width=6)
    dr.rectangle((0, 14, 1860, 24), fill=GELB)
    for x in range(60, 1860, 150):
        dr.line((x, 34, x - 30, 130), fill=(190, 190, 184, 255), width=3)
    return _hart_wenn(c)(El(im, 30, G0, c, "cut", 0.0, None, name="bahnsteig"))


def deckenband(c):
    """Deckenkante des U-Bahnhofs mit Lampen (Grundform)."""
    im = Image.new("RGBA", (1860, 40))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860, 22), fill=HELLGRAU)
    dr.line((0, 22, 1860, 22), fill=INK, width=5)
    for x in range(140, 1860, 330):
        dr.rounded_rectangle((x, 20, x + 90, 34), 6, fill=GELB, outline=INK, width=3)
    return _hart_wenn(c)(El(im, 30, 18, c, "cut", 0.0, None, name="decke"))


# ===========================================================================================================================
# A1 Fall: Bahnsteig, Kontrolle, Flucht
# ===========================================================================================================================
FHA = 430                                    # Figurenhöhe in den Fallszenen
WX0, AX0 = 950, 1250                         # Wendelin und Anselm bei der Kontrolle
AX1, WX1 = 1560, 1290                        # Anselm an der Treppe, Wendelin rennt hinterher
TR_X = 1790                                  # Treppe zum Ausgang (Tabler „stairs-down“)
folie([(NULL, "Fall · Im U-Bahnhof"), ("kontr", "Fall · Fahrscheinkontrolle"), ("w1", "Fall · Wendelin bittet um den Ausweis"),
       ("flucht", "Fall · Anselm läuft zur Treppe"), ("verfolg", "Fall · Wendelin rennt hinterher")], [
    deckenband(NULL), bahnsteig(NULL),
    szene(hart(ficon("tabler", "train", 380, G0 + 4, 420, NULL, fuell=BLAU, anim="cut")), "190zug*", 0.6, 0.0),
    hart(ficon("tabler", "stairs-down", TR_X, G0 + 4, 180, NULL, fuell=WEISS, anim="cut")),
    hart(pl("Ausgang", TR_X, 470, NULL, fill=WEISS, size=30, anker="m")),
    hart(ficon("tabler", "arrow-down", TR_X, 590, 70, NULL, fuell=WEISS, anim="cut")),
    hart(pl("Im U-Bahnhof hält ein Zug", 70, 70, NULL, fill=GELB, size=34)),
    pl("Kontrolleur Wendelin prüft die Fahrscheine", 70, 140, "kontr", fill=WEISS, size=32, bis="flucht"),
    # Wendelin bei der Kontrolle (blickt nach rechts zu Anselm), dann rennt er hinterher
    *fig("WD", WX0, G0, FHA, [("kontr", "ruhig_r")], bis="w1"),
    *redet("WD_redet_r", WX0, G0, FHA, "w1", "flucht"),
    *fig("WD", WX0, G0, FHA, [("flucht", "schreck_r")], bis="verfolg", erst="cut"),
    bis_(ns("Wendelin", WX0, G0, "kontr", BLAU, d=0.1), "verfolg"),
    *fig("WD", WX1, G0, FHA, [("verfolg", "ernst_r")], erst="cut"),
    ns("Wendelin", WX1, G0, "verfolg", BLAU),
    bis_(ficon("tabler", "ticket", WX0 - 200, 420, 90, beim("kontr", "Fahrscheine"), fuell=GELB), "w1"),
    # Anselm ohne gültigen Fahrschein, dann läuft er zur Treppe
    *fig("AS", AX0, G0, FHA, [(beim("anselm", "Anselm"), "ruhig"), ("w1", "sorge")], bis="flucht"),
    bis_(ns("Anselm", AX0, G0, beim("anselm", "Anselm"), GRUEN, d=0.1), "flucht"),
    pl("Fahrgast Anselm: kein gültiger Fahrschein", 70, 210, beim("anselm", "Anselm"), fill=HELLROT, size=32, bis="flucht"),
    bis_(ficon("tabler", "ticket-off", AX0 + 200, 420, 90, beim("anselm", "gültigen"), fuell=HELLROT), "w1"),
    blase("sprech", 640, 160, "w1", 1180, 210, inhalt=["Dann brauche ich bitte", "Ihren Ausweis."], textsize=36,
          figur=("WD_redet_r", WX0, G0, FHA), bis="flucht"),
    szene(hart(peep_voll("AL_lauf_r", AX1, G0, FHA, "flucht", anim="cut")), "190schritte*", 0.7, 0.0),
    ns("Anselm", AX1, G0, "flucht", GRUEN),
    pl("Anselm läuft los, zur Treppe am Ausgang", 70, 140, "flucht", fill=WEISS, size=32),
    pl("Wendelin rennt hinterher: steile Treppe, 2 Stufen auf einmal", 70, 210, beim("verfolg", "rennt"), fill=HELLROT,
       size=30),
])

# ===========================================================================================================================
# A2 Fall: die Treppe (Sturz nicht gezeigt: nur Treppen-Icon und Text), danach Wendelin mit Armschlinge
# ===========================================================================================================================
folie([("sturz", "Fall · Der Sturz"), ("arm", "Fall · Arm gebrochen")], [
    deckenband("sturz"),
    ficon("tabler", "stairs-down", 640, 860, 520, "sturz", fuell=HELLGRAU, anim="cut"),
    pl("Wendelin stürzt auf den Stufen", 640, 200, beim("sturz", "stürzt"), fill=HELLROT, size=40, anker="m"),
    *fig("WS", 1450, 930, 520, [("arm", "ruhig")], erst="cut"),
    ns("Wendelin", 1450, 930, "arm", BLAU),
    ficon("tabler", "bandage", 1700, 400, 110, beim("arm", "gebrochen"), fuell=WEISS),
    pl("Arm gebrochen", 1700, 140, beim("arm", "gebrochen"), fill=HELLROT, size=32, anker="m"),
    pl("6 Wochen Armschlinge", 1700, 210, beim("arm", "sechs"), fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: danach am Fuß der Treppe
# ===========================================================================================================================
WX2, AX2 = 900, 1330
folie([("w2", "Fall · Wendelin verlangt Ersatz"), ("frage", "Fall · Die Frage"), ("klass", "Fall · Ein Klassiker")], [
    deckenband("w2"), bahnsteig("w2"),
    ficon("tabler", "stairs-down", 300, G0 + 4, 260, "w2", fuell=HELLGRAU, anim="cut"),
    *redet("WS_redet_r", WX2, G0, FHA, "w2", "a1"),
    blase("sprech", 700, 160, "w2", 1130, 200, inhalt=["Für meinen gebrochenen Arm", "müssen Sie aufkommen."], textsize=36,
          figur=("WS_redet_r", WX2, G0, FHA), bis="a1"),
    *fig("WS", WX2, G0, FHA, [("a1", "ernst_r"), ("frage", "denkt_r"), ("klass", "ruhig_r")], erst="cut"),
    ns("Wendelin", WX2, G0, "w2", BLAU),
    *fig("AS", AX2, G0, FHA, [("w2", "sorge")], bis="a1", erst="cut"),
    *redet("AS_redet", AX2, G0, FHA, "a1", "frage"),
    blase("sprech", 760, 160, "a1", 1080, 200, inhalt=["Ich habe Sie doch gar nicht berührt.", "Sie sind selbst gestürzt!"],
          textsize=34, figur=("AS_redet", AX2, G0, FHA), bis="frage"),
    *fig("AS", AX2, G0, FHA, [("frage", "denkt"), ("klass", "still")], erst="cut"),
    ns("Anselm", AX2, G0, "w2", GRUEN),
    pl("Muss Anselm für den Sturz haften?", 70, 70, "frage", fill=PINK, size=34),
    pl("Klassiker: der Verfolgerfall", 70, 145, beim("klass", "Klassiker"), fill=GELB, size=32),
    zit("BGH, Urt. v. 13.7.1971 – VI ZR 125/70, BGHZ 57, 25", 80, 212, beim("klass", "Verfolgerfall")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def absatz_190(text, x, y, breite, cue, size=33, zeilenabstand=1.30):
    """Wie bausteine.absatz(), aber eine Zahl bleibt mit dem folgenden Wort in einer Zeile („2 Stufen“, „6 Wochen“)."""
    f = F("Regular", size)
    worte, zeilen, cur = [], [], ""
    for w in text.split():
        if worte and worte[-1].isdigit():
            worte[-1] += " " + w
        else:
            worte.append(w)
    for w in worte:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    if cur:
        zeilen.append(cur)
    els = [OT(z_, x, y + i * size * zeilenabstand, cue, "Regular", size, farbe=INK, anim="fade") for i, z_ in enumerate(zeilen)]
    return els, y + len(zeilen) * size * zeilenabstand


def sachverhalt_190(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz_190(glyphen(a), 210, y, 1500, cue)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_190("sv", [
    "Kontrolleur Wendelin prüft in einem U-Bahnhof die Fahrscheine. Der Fahrgast Anselm hat keinen gültigen Fahrschein "
    "dabei. Wendelin bittet ihn um seinen Ausweis, um die Personalien festzustellen.",
    "Anselm läuft los, zur Treppe am Ausgang. Wendelin rennt hinterher, die steile Treppe hinunter, 2 Stufen auf einmal. "
    "Auf den Stufen stürzt er. Anselm hat ihn dabei weder gestoßen noch berührt. Der Arm von Wendelin ist gebrochen; "
    "6 Wochen trägt er eine Armschlinge.",
    "Wendelin sagt zu Anselm: „Für meinen gebrochenen Arm müssen Sie aufkommen.“ Anselm antwortet: „Ich habe Sie doch gar "
    "nicht berührt. Sie sind selbst gestürzt!“",
], "Kann Wendelin von Anselm Schadensersatz aus § 823 Abs. 1 BGB verlangen?")

# ===========================================================================================================================
# C Das Problem: psychisch vermittelte Kausalität
# ===========================================================================================================================
PP = "Das Problem"
folie([("problem", f"{PP} · kein Stoß, keine Berührung"), ("selbst", f"{PP} › eigener Entschluss"),
       ("psych", f"{PP} › psychisch vermittelte Kausalität")], rechts_frei([
    *tafel("problem", "Das Problem: verletzt er sich „selbst“?"),
    *neinz("Anselm hat Wendelin weder gestoßen noch berührt", 190, beim("problem", "weder"), "Bold", 32, x=160),
    z("Wendelin hat sich selbst entschieden,", 110, 290, "selbst", "Bold", 34),
    z("hinterherzulaufen", 110, 340, beim("selbst", "hinterherzulaufen"), "Bold", 34),
    z("Der Weg zur Verletzung führt über", 110, 440, "psych", size=34),
    z("seinen eigenen Willensentschluss", 110, 490, beim("psych", "Willensentschluss"), size=34),
    blk(110, 580, 1040, 90, GELB, beim("psych", "psychisch"), [("psychisch vermittelte Kausalität", "ExtraBold", 38, INK)]),
    *requisit([("problem", ("tabler", "hand-off", 100, WEISS), "nicht berührt", WEISS),
               ("selbst", ("tabler", "route", 100, WEISS), "selbst entschieden", WEISS),
               ("psych", ("tabler", "brain", 100, LILA), "psychisch vermittelt", GELB)]),
    *zwei([("problem", "ernst"), ("psych", "denkt")], [("problem", "ruhig"), ("selbst", "denkt")]),
]))

# ===========================================================================================================================
# D Die Norm: § 823 Abs. 1 BGB (Wortlautkarte, Merkmale genannt)
# ===========================================================================================================================
W823 = umbruch("„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein "
               "sonstiges Recht eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden "
               "Schadens verpflichtet.“", 34, 1040)
_zi = lambda t_, wort: next(i for i, t in enumerate(t_) if wort in t)
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 1 BGB", "norm",
                        marken=[(_zi(W823, "Körper"), "Körper", beim("koerper", "Körper")),
                                (_zi(W823, "verletzt,"), "verletzt", beim("kaus", "verletzt"))], size=34)
PN = "Die Norm: § 823 Abs. 1 BGB"
folie([("norm", PN), ("koerper", f"{PN} › Körper verletzt"), ("kaus", f"{PN} › haftungsbegründende Kausalität?"),
       ("schema", f"{PN} › Schema: Video „Deliktsrecht“")], rechts_frei([
    *tafel("norm", "Die Norm: § 823 Abs. 1 BGB"),
    *w823,
    *okz("Körper von Wendelin verletzt", w823_y + 30, beim("koerper", "Körper"), "Bold", 32, x=160),
    blk(110, w823_y + 100, 1040, 130, GELB, beim("kaus", "Fraglich"), [("Hat Anselm ihn verletzt?", "ExtraBold", 34, INK),
                                                                     ("haftungsbegründende Kausalität", "ExtraBold", 34, INK)]),
    z("ganzes Prüfschema: Video „Deliktsrecht“", 110, w823_y + 260, beim("schema", "Prüfschema"), "Bold", 30, farbe=TEXT),
    *requisit([("norm", ("tabler", "book", 100, WEISS), "§ 823 Abs. 1 BGB", GELB),
               ("koerper", ("tabler", "bandage", 100, WEISS), "Körper verletzt", HELLROT),
               ("kaus", ("tabler", "link", 100, WEISS), "Kausalität?", GELB)]),
    *zwei([("norm", "ruhig"), ("koerper", "muede"), ("kaus", "ernst")], [("norm", "ruhig"), ("kaus", "sorge")]),
]))

# ===========================================================================================================================
# E Kausalität: Äquivalenz und wertende Zurechnung
# ===========================================================================================================================
PK = "Haftungsbegründende Kausalität"
folie([("aequ", f"{PK} › Äquivalenz"), ("wert", f"{PK} › freier Entschluss dazwischen"),
       ("wert2", f"{PK} › wertende Zurechnung")], rechts_frei([
    *tafel("aequ", "Haftungsbegründende Kausalität"),
    *okz("1. Äquivalenz: die Flucht ist ursächlich", 190, beim("aequ", "Äquivalenz"), "Bold", 34, x=160),
    z("ohne sie wäre Wendelin nicht gerannt", 160, 245, beim("aequ", "Ohne"), size=32),
    z("Doch: freier Entschluss des Verletzten", 110, 350, "wert", "Bold", 34),
    z("tritt dazwischen", 110, 400, beim("wert", "dazwischen"), "Bold", 34),
    *neinz("Äquivalenz genügt allein nicht", 470, beim("wert", "genügt"), "Bold", 34, x=160),
    blk(110, 570, 1040, 90, GELB, "wert2", [("2. wertende Zurechnung nötig", "ExtraBold", 38, INK)]),
    *requisit([("aequ", ("tabler", "link", 100, WEISS), "ursächlich", HELLGRUEN),
               ("wert", ("tabler", "route", 100, WEISS), "freier Entschluss", WEISS),
               ("wert2", ("tabler", "scale", 100, WEISS), "wertende Zurechnung", GELB)]),
    *zwei([("aequ", "ernst"), ("wert2", "denkt")], [("aequ", "muede"), ("wert", "denkt")]),
]))

# ===========================================================================================================================
# F Die Herausforderungsformel des BGH
# ===========================================================================================================================
PF = "Herausforderungsformel"
folie([("formel", f"{PF} des BGH"), ("h1", f"{PF} › vorwerfbar herausgefordert"),
       ("h2", f"{PF} › durfte sich herausgefordert fühlen"), ("h3", f"{PF} › 1. billigenswertes Motiv"),
       ("h4", f"{PF} › 2. kein Missverhältnis"), ("h5", f"{PF} › 3. gesteigertes Risiko verwirklicht")], rechts_frei([
    *tafel("formel", "Die Herausforderungsformel"),
    zit("grundlegend: BGH, Urt. v. 13.7.1971 – VI ZR 125/70, BGHZ 57, 25", 110, 165, beim("formel", "Formel")),
    blk(110, 215, 1040, 135, HELL, "h1", [("Wer vorwerfbar zu einer Verfolgung", "Bold", 32, INK),
                                         ("herausfordert, haftet für den Schaden,", "Bold", 32, INK)]),
    z("wenn sich der Verfolger herausgefordert", 110, 375, "h2", "ExtraBold", 34),
    z("fühlen durfte:", 110, 422, "h2", "ExtraBold", 34),
    z("1. Motiv: mindestens im Ansatz billigenswert", 150, 500, "h3", "Bold", 32),
    z("2. Risiko nicht außer Verhältnis zum Zweck", 150, 570, beim("h4", "Risiken"), "Bold", 32),
    z("3. gesteigertes Verfolgungsrisiko verwirklicht", 150, 640, beim("h5", "gesteigerte"), "Bold", 32),
    zit("BGH, Urt. v. 31.1.2012 – VI ZR 43/11, Rn. 8, 11, 20", 110, 720, beim("h5", "gesteigerte")),
    *requisit([("formel", ("tabler", "book", 100, WEISS), "Formel des BGH", GELB),
               ("h1", ("tabler", "arrows-split", 100, WEISS), "herausgefordert", WEISS),
               ("h3", ("tabler", "heart-handshake", 100, GRUEN), "billigenswert", HELLGRUEN),
               ("h4", ("tabler", "scale", 100, WEISS), "Verhältnis", WEISS),
               ("h5", ("tabler", "alert-triangle", 100, GELB), "gesteigertes Risiko", GELB)]),
    *zwei([("formel", "ruhig"), ("h3", "denkt"), ("h5", "ernst")], [("formel", "ernst"), ("h2", "denkt"), ("h4", "sorge")]),
]))

# ===========================================================================================================================
# G Im Fall: Subsumtion
# ===========================================================================================================================
PI = "Im Fall"
folie([("mot", f"{PI} › 1. Motiv"), ("mot2", f"{PI} › 1. billigenswert"), ("verh", f"{PI} › 2. kein Missverhältnis"),
       ("risk", f"{PI} › 3. steile Treppe, hohes Tempo"), ("risk2", f"{PI} › 3. Risiko verwirklicht"),
       ("zur", f"{PI} › objektiv zuzurechnen")], rechts_frei([
    *tafel("mot", "Im Fall: herausgefordert?"),
    z("1. Personalien feststellen, um den Anspruch", 110, 180, beim("mot", "Personalien"), "Bold", 32),
    z("des Verkehrsbetriebs zu sichern", 150, 225, beim("mot", "Anspruch"), "Bold", 32),
    *okz("billigenswert", 280, "mot2", "ExtraBold", 32, x=195),
    *okz("2. Treppe zu Fuß: nicht außer Verhältnis", 360, beim("verh", "Verfolgung"), "Bold", 32, x=160),
    zit("so schon BGHZ 57, 25 (Treppe am Bahnhofsausgang)", 160, 410, beim("verh", "Bundesgerichtshof")),
    z("3. steile Treppe in hohem Tempo:", 110, 480, "risk", "Bold", 32),
    z("deutlich erhöhtes Risiko", 150, 525, beim("risk", "erhöhtes"), "Bold", 32),
    *okz("im Sturz verwirklicht", 580, "risk2", "ExtraBold", 32, x=195),
    blk(110, 660, 1040, 90, GRUEN, "zur", [("Sturz ist Anselm objektiv zuzurechnen", "ExtraBold", 36, INK)]),
    *requisit([("mot", ("tabler", "id", 100, WEISS), "Personalien", WEISS),
               ("verh", ("tabler", "scale", 100, WEISS), "nicht außer Verhältnis", HELLGRUEN),
               ("risk", ("tabler", "stairs-down", 120, WEISS), "steile Treppe", HELLROT),
               ("zur", ("tabler", "check", 100, GRUEN), "zuzurechnen", HELLGRUEN)]),
    *zwei([("mot", "ruhig"), ("risk", "muede"), ("zur", "froh")], [("mot", "ernst"), ("verh", "sorge"), ("zur", "muede")]),
]))

# ===========================================================================================================================
# H Verschulden
# ===========================================================================================================================
folie([("versch", "Verschulden · fahrlässig"), ("versch2", "Verschulden › Schaden voraussehbar")], rechts_frei([
    *tafel("versch", "Verschulden"),
    *okz("Anselm musste damit rechnen, verfolgt zu werden", 200, beim("versch", "rechnen"), "Bold", 32, x=160),
    *okz("und dass sein Verfolger dabei zu Schaden kommt", 280, beim("versch2", "Verfolger"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 31.1.2012 – VI ZR 43/11, Rn. 9, 14", 160, 335, beim("versch2", "Verfolger")),
    blk(110, 400, 1040, 90, GRUEN, beim("versch2", "Schaden"), [("Anselm handelte fahrlässig", "ExtraBold", 38, INK)]),
    *requisit([("versch", ("tabler", "zoom-question", 100, WEISS), "damit rechnen", WEISS),
               ("versch2", ("tabler", "alert-triangle", 100, GELB), "fahrlässig", HELLGRUEN)]),
    *zwei([("versch", "denkt")], [("versch", "ernst"), ("versch2", "muede")]),
]))

# ===========================================================================================================================
# I Gegenbeispiele: allgemeines Lebensrisiko, übersteigertes Risiko
# ===========================================================================================================================
PG = "Gegenbeispiele"
folie([("gegen", f"{PG} · normales Risiko jedes Laufens"), ("gg1", f"{PG} › allgemeines Lebensrisiko"),
       ("gg2", f"{PG} › Umknicken auf ebenem Boden"), ("gg3", f"{PG} › gänzlich unangemessen")], rechts_frei([
    *tafel("gegen", "Gegenbeispiele: keine Zurechnung"),
    blk(110, 180, 1040, 80, HELL, "gegen", [("normales Risiko jedes Laufens?", "ExtraBold", 34, INK)]),
    *neinz("allgemeines Lebensrisiko: keine Haftung", 300, beim("gg1", "Lebensrisiko"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 12.3.1996 – VI ZR 12/95, BGHZ 132, 164; BGHZ 57, 25", 160, 350, beim("gg1", "Lebensrisiko")),
    z("z. B. Umknicken auf ebenem Boden, ohne", 160, 415, "gg2", size=32),
    z("besondere Gefahr durch die Verfolgung", 160, 460, beim("gg2", "Verfolgung"), size=32),
    *neinz("gänzlich unangemessen, z. B. Sprung", 545, beim("gg3", "gänzlich"), "Bold", 32, x=160),
    z("aus großer Höhe: nicht mehr herausgefordert", 160, 590, beim("gg3", "Höhe"), "Bold", 32),
    zit("BGH, Urt. v. 12.3.1996 – VI ZR 12/95, BGHZ 132, 164", 160, 640, beim("gg3", "Höhe")),
    *requisit([("gegen", ("tabler", "shoe", 110, WEISS), "normales Risiko", WEISS),
               ("gg1", ("tabler", "clock", 100, WEISS), "Lebensrisiko", HELLROT),
               ("gg2", ("tabler", "road", 110, HELLGRAU), "ebener Boden", WEISS),
               ("gg3", ("tabler", "arrow-big-down-lines", 100, HELLROT), "große Höhe", HELLROT)]),
    *zwei([("gegen", "denkt"), ("gg2", "sorge")], [("gegen", "ernst"), ("gg1", "froh"), ("gg3", "denkt")]),
]))

# ===========================================================================================================================
# J Mitverschulden: § 254 Abs. 1 BGB (Wortlautkarte, vorgelesen)
# ===========================================================================================================================
W254 = umbruch("„Hat bei der Entstehung des Schadens ein Verschulden des Beschädigten mitgewirkt, so hängt die Verpflichtung "
               "zum Ersatz sowie der Umfang des zu leistenden Ersatzes von den Umständen, insbesondere davon ab, inwieweit "
               "der Schaden vorwiegend von dem einen oder dem anderen Teil verursacht worden ist.“", 32, 1040)
w254, w254_y = wortlaut(80, 160, 1100, W254, "§ 254 Abs. 1 BGB", "mit",
                        marken=[(_zi(W254, "Verschulden"), "Verschulden", beim("w254", "Verschulden")),
                                (_zi(W254, "Umfang"), "Umfang", beim("w254", "Umfang")),
                                (_zi(W254, "vorwiegend"), "vorwiegend", beim("w254", "vorwiegend"))], size=32)
PM = "Mitverschulden, § 254 Abs. 1 BGB"
folie([("mit", PM), ("stufen", f"{PM} › 2 Stufen auf einmal"), ("abw", f"{PM} › abwägen"),
       ("orig", f"{PM} › Originalfall: 2/3")], rechts_frei([
    *tafel("mit", "Mitverschulden: § 254 Abs. 1 BGB", size=44),
    *w254,
    z("2 Stufen auf einmal: Mitverschulden möglich,", 110, w254_y + 30, "stufen", "Bold", 32),
    z("dann wird der Anspruch gekürzt", 110, w254_y + 75, beim("stufen", "gekürzt"), "Bold", 32),
    blk(110, w254_y + 135, 1040, 80, GELB, "abw", [("abwägen statt alles oder nichts", "ExtraBold", 34, INK)]),
    z("Originalfall: 2/3 des Schadens ersetzt", 110, w254_y + 240, beim("orig", "Originalfall"), "Bold", 32),
    zit("BGH, Urt. v. 13.7.1971 – VI ZR 125/70, BGHZ 57, 25", 110, w254_y + 288, beim("orig", "Originalfall")),
    *requisit([("mit", ("tabler", "book", 100, WEISS), "§ 254 BGB", GELB),
               ("stufen", ("tabler", "stairs-down", 120, WEISS), "2 Stufen auf einmal", HELLROT),
               ("abw", ("tabler", "scale", 100, WEISS), "abwägen", GELB),
               ("orig", ("tabler", "chart-pie-2", 100, GRUEN), "2/3 ersetzt", HELLGRUEN)]),
    *zwei([("mit", "ruhig"), ("stufen", "sorge"), ("orig", "ruhig")], [("mit", "ernst"), ("stufen", "denkt")]),
]))

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Wendelin gegen Anselm")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 135, GRUEN, "erg", [("Anselm muss Wendelin den Schaden", "ExtraBold", 34, INK),
                                          ("aus dem Sturz ersetzen", "ExtraBold", 34, INK)]),
    z("§ 823 Abs. 1 BGB", 110, 360, beim("erg", "Paragraf"), "Bold", 34),
    z("gekürzt um ein etwaiges Mitverschulden (§ 254 BGB)", 110, 420, beim("erg", "gekürzt"), "Bold", 32),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", WEISS)]),
    *zwei([("erg", "froh")], [("erg", "muede")]),
]))

# ===========================================================================================================================
# L Ausblick: Retter, Strafrecht, § 265a StGB (je ein Satz)
# ===========================================================================================================================
folie([("retter", "Ausblick · Retterfälle"), ("straf", "Ausblick › Strafrecht"), ("fahrt", "Ausblick › § 265a StGB")],
      rechts_frei([
    *tafel("retter", "Ausblick"),
    z("Retterfälle: bei Gefahr für Leib und Leben", 110, 190, "retter", "Bold", 32),
    z("Eingreifen nahezu zwangsläufig herausgefordert", 110, 235, beim("retter", "nahezu"), "Bold", 32),
    zit("BGHZ 57, 25 mit BGH, Urt. v. 24.3.1964 – VI ZR 33/63", 110, 285, beim("retter", "nahezu")),
    z("Strafrecht: objektive Zurechnung", 110, 370, "straf", "Bold", 32),
    zit("z. B. BGH, Beschl. v. 5.5.2021 – 4 StR 19/20", 110, 420, beim("straf", "objektiven")),
    z("Fahrt ohne Fahrschein, § 265a StGB", 110, 500, "fahrt", "Bold", 32),
    z("(Erschleichen von Leistungen): eigene Frage", 110, 545, beim("fahrt", "Erschleichen"), size=32),
    *requisit([("retter", ("tabler", "lifebuoy", 100, ROT), "Retter", WEISS),
               ("straf", ("tabler", "gavel", 100, HOLZ), "Strafrecht", WEISS),
               ("fahrt", ("tabler", "ticket-off", 100, HELLROT), "§ 265a StGB", WEISS)]),
    *zwei([("retter", "ruhig")], [("retter", "ruhig"), ("fahrt", "sorge")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Herausforderung bei der Kausalität"), ("tp2", "Klausurtipp · nicht vorschnell verneinen"),
       ("tp3", "Klausurtipp · Verschulden, Mitverschulden getrennt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Die Herausforderung prüfst du bei der", 200, 200, beim("tipp", "Herausforderung"), "Bold", 36),
    z("haftungsbegründenden Kausalität", 200, 255, beim("tipp", "haftungsbegründenden"), "Bold", 36),
    z("als objektive Zurechnung der Rechtsgutsverletzung", 200, 310, beim("tipp", "objektive"), size=32),
    linienzug([(130, 385), (1130, 385)], "tp2", breite=3),
    z("Nicht vorschnell verneinen mit dem Argument,", 200, 410, "tp2", "Bold", 36),
    z("der Verfolger sei freiwillig gerannt", 200, 465, beim("tp2", "freiwillig"), size=34),
    linienzug([(130, 540), (1130, 540)], "tp3", breite=3),
    z("Dann gesondert: das Verschulden,", 200, 565, beim("tp3", "Verschulden"), "Bold", 36),
    z("das Mitverschulden erst beim Umfang des Ersatzes", 200, 620, beim("tp3", "Mitverschulden"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Haftungsbegründende Kausalität", True),
          ("c1", 1, "1. Äquivalenz: Flucht ursächlich", False),
          ("c2", 1, "2. Herausforderung: billigenswertes Motiv,", False),
          ("c2", 2, "Risiko nicht außer Verhältnis zum Zweck,", False),
          ("c2", 2, "gesteigertes Verfolgungsrisiko verwirklicht", False),
          ("c3", 0, "II. Verschulden: Verfolgung und Verletzung voraussehbar", True),
          ("c4", 0, "III. Mitverschulden, § 254 BGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Zurechnung in Verfolgerfällen"), 110, 90, "sch", 46),
           z("im Rahmen von § 823 Abs. 1 BGB; übriges Schema: Video „Deliktsrecht“", 110, 160, "sch", "Bold", 32, farbe=TEXT,
             rechts=1800)]
y = 250
for i, (c, ebene, text, fett) in enumerate(REIHEN):
    x = (130, 200, 260)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    nxt = REIHEN[i + 1][1] if i + 1 < len(REIHEN) else 0
    y += 95 if nxt == 0 else 75
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Kausalität: Äquivalenz"), ("c2", "Prüfschema › I. Kausalität: Herausforderung"),
       ("c3", "Prüfschema › II. Verschulden"), ("c4", "Prüfschema › III. Mitverschulden")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer flieht, haftet für den Sturz", 0)], [("seines Verfolgers, wenn er ihn", 0)],
                 [("vorwerfbar ", 0), ("herausgefordert", "a"), (" hat und", 0)],
                 [("sich das ", 0), ("gesteigerte Risiko", "b"), (" verwirklicht.", 0)]], 750, 270, 42, "merke",
                {"a": beim("merke", "herausgefordert"), "b": beim("merke", "gesteigerte")}),
    *markertext([[("Das allgemeine ", 0), ("Lebensrisiko", "c")], [("trägt der Verfolger selbst.", 0)]],
                750, 680, 42, "m2", {"c": beim("m2", "Lebensrisiko")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
