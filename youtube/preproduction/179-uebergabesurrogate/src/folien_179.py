"""Folge 179 · Besitzkonstitut & Co.: Eigentum ohne Übergabe (§§ 929 S. 2, 930, 931) – Serienstandard Open Peeps
(Katzenkönig).
Fall: Käthe kauft das Auto ihres Nachbarn Herrn Wöhler für 4.000 €, zahlt sofort und bekommt die Zulassungsbescheinigung
Teil II; Herr Wöhler darf den Wagen bis Samstag noch fahren (Leihe), das Auto soll ab heute Käthe gehören.
Drei kurze Fälle mit gleicher Bildstruktur (links Haus und Figur Herr Wöhler, rechts Haus und Figur Käthe, das Auto je
nach Fall bei Käthe, bei Herrn Wöhler oder in der Werkstatt in der Mitte).
Szenen laut ../SZENENPLAN.md: A Fall, B Sachverhalt, C Einordnung (§ 929 S. 1, Zulassungsbescheinigung), D Übergabesurrogate,
E/F 1. § 929 S. 2 (Bühne, Wortlautkarte), G–K 2. § 930 (Bühne, Wortlautkarte § 930, Wortlautkarte § 868, BGH-Zitatkarte
V ZR 92/25 Rn. 20, Sicherungsübereignung/Bestimmtheit), L–N 3. § 931 (Bühne, Wortlautkarte, Abtretung), O Merktabelle,
P Ausblick gutgläubiger Erwerb, Q Lösung, R Klausurtipp (Lexi), S Prüfschema, T Merksatz (Lexi).
Auto als neutrales Tabler-Icon ohne Marke und ohne Kennzeichen. Zwei Handlungsgeräusche (Geldscheine bei der Zahlung, Motor
beim Fahren des Autos in Käthes Einfahrt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 161 (gemeinsame Dateien unverändert); neu: auto(), buehne(), tabelle.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_179/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_179/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Folge 179), als Zitat mit Normangabe;
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
NAME = {"KA": "Käthe", "WO": "Herr Wöhler", "WM": "Werkstatt"}
NFARBE = {"KA": BLAU, "WO": GRUEN, "WM": ORANGE}
AUTOFARBE = GELB


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), bis_(ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1), bis)]


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


def zwei(a, folge_a, b, folge_b):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(a, X1, folge_a), *stehend(b, X2, folge_b)]


def auto(cx, unten, cue, bis=None, breite=280, anim="pop"):
    """Das Auto (Tabler „car“, neutral, ohne Marke und ohne Kennzeichen), Füllung Gelb."""
    return ficon("tabler", "car", cx, unten, breite, cue, fuell=AUTOFARBE, bis=bis, anim=anim)


# ===========================================================================================================================
# Bühne der Fallszenen: gleiche Bildstruktur (links Herr Wöhler vor seinem Haus, rechts Käthe vor ihrem Haus)
# ===========================================================================================================================
BODEN, FH = 880, 470
WX, KX = 400, 1500                          # Herr Wöhler, Käthe
CW, CK, CM = 760, 1160, 960                 # Auto in der Einfahrt von Herrn Wöhler / bei Käthe / in der Werkstatt
HAND = BODEN - 205                          # Unterkante kleiner Requisiten in Handhöhe


def buehne(c, h=lambda e: e):
    return [h(boden(BODEN, c)),
            h(ficon("tabler", "home", 150, BODEN, 200, c, fuell=GRUEN, anim="cut")),
            h(ficon("tabler", "home", 1770, BODEN, 200, c, fuell=BLAU, anim="cut"))]


def personen(c, wo, ka, bis=None, erst="cut"):
    """Herr Wöhler links (blickt nach rechts), Käthe rechts (blickt nach links); wo/ka = [(cue, suffix)]."""
    return [*fig("WO", WX, BODEN, FH, [(c, wo[0][1])] + wo[1:], bis=bis, erst=erst), bis_(ns("Herr Wöhler", WX, BODEN, c, GRUEN), bis),
            *fig("KA", KX, BODEN, FH, [(c, ka[0][1])] + ka[1:], bis=bis, erst=erst), bis_(ns("Käthe", KX, BODEN, c, BLAU), bis)]


# --- A Fall -----------------------------------------------------------------------------------------------------------
_h = lambda e: hart(e)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KA_DA, WO_DA = beim("kaethe", "Käthe"), beim("kauf", "Nachbar")
folie([(NULL, "Fall · Das Auto des Nachbarn"), ("aber", "Fall · noch eine Woche fahren"),
       ("frage", "Die Frage · Schon heute Eigentümerin?")], [
    *buehne(NULL, _h),
    _h(pl("Fall: das Auto des Nachbarn", 70, 30, NULL, fill=GELB, size=38)),
    _h(bis_(auto(CW, BODEN, NULL, anim="cut"), None)),
    bis_(pl("Du kaufst das Auto deines Nachbarn …", 70, 110, beim("fall", "du"), fill=WEISS, size=34), "kauf"),
    # Käthe vor ihrem Haus (blickt nach links zu Herrn Wöhler)
    *fig("KA", KX, BODEN, FH, [(KA_DA, "ruhig"), ("zahlt", "froh"), ("aber", "denkt"), ("ka1", "ruhig")], bis="ka1"),
    ns("Käthe", KX, BODEN, KA_DA, BLAU, d=0.1),
    # Herr Wöhler vor seinem Haus (blickt nach rechts zu Käthe)
    *fig("WO", WX, BODEN, FH, [(WO_DA, "froh_r"), ("aber", "sorge_r")], bis="wo1"),
    ns("Herr Wöhler", WX, BODEN, WO_DA, GRUEN, d=0.1),
    pl("Kleinwagen für 4.000 €", 70, 110, beim("kauf", "Kleinwagen"), fill=WEISS, size=34, bis="wo1"),
    # Zahlung: Geldschein wandert von Käthe zu Herrn Wöhler
    szene(bewegt(ficon("tabler", "cash-banknote", WX + 135, HAND, 84, beim("zahlt", "zahlt"), fuell=GRUEN, bis="wo1"),
                 beim("zahlt", "zahlt"), beim("zahlt", "sofort"), KX - 135 - (WX + 135), 0), "179geld*", 0.8, 0.1),
    pl("Käthe zahlt sofort", 70, 190, beim("zahlt", "zahlt"), fill=GRUEN, size=34, bis="wo1"),
    # Zulassungsbescheinigung Teil II wandert von Herrn Wöhler zu Käthe
    bewegt(ficon("tabler", "file-certificate", KX - 140, HAND, 76, beim("zb", "gibt"), fuell=WEISS, bis="wo1"),
           beim("zb", "gibt"), beim("zb", "Zulassungsbescheinigung"), WX + 140 - (KX - 140), 0),
    pl("Zulassungsbescheinigung Teil II an Käthe", 70, 270, beim("zb", "Zulassungsbescheinigung"), fill=WEISS, size=34,
       bis="wo1"),
    pl("Er braucht das Auto noch 1 Woche", 70, 350, "aber", fill=HELLROT, size=34, bis="wo1"),
    # Dialog
    *redet("WO_redet_r", WX, BODEN, FH, "wo1", "ka1"),
    blase("sprech", 760, 290, "wo1", 800, 215, inhalt=["Ich ziehe nächste Woche um.", "Darf ich den Wagen", "bis Samstag noch fahren?"],
          textsize=36, figur=("WO_redet_r", WX, BODEN, FH), bis="ka1"),
    *fig("WO", WX, BODEN, FH, [("ka1", "ruhig_r")], erst="cut", bis="wo2"),
    *redet("KA_redet", KX, BODEN, FH, "ka1", "wo2"),
    blase("sprech", 760, 290, "ka1", 1150, 215, inhalt=["Gut, ich leihe ihn Ihnen", "bis Samstag. Aber ab", "heute gehört er mir."],
          textsize=36, figur=("KA_redet", KX, BODEN, FH), bis="wo2"),
    ficon("tabler", "calendar-event", CW, BODEN - 215, 64, beim("ka1", "Samstag"), fuell=WEISS, bis="frage"),
    *redet("WO_redet_r", WX, BODEN, FH, "wo2", "frage"),
    blase("sprech", 440, 200, "wo2", 760, 260, inhalt=["Einverstanden."], textsize=40, figur=("WO_redet_r", WX, BODEN, FH),
          bis="frage"),
    *fig("KA", KX, BODEN, FH, [("wo2", "froh"), ("frage2", "denkt")], erst="cut"),
    *fig("WO", WX, BODEN, FH, [("frage", "froh_r")], erst="cut"),
    ficon("tabler", "key", WX + 130, HAND, 60, "frage", fuell=GELB),
    pl("Herr Wöhler fährt weiter", 70, 110, "frage", fill=WEISS, size=34),
    pl("Ist Käthe schon heute Eigentümerin?", 70, 190, "frage2", fill=PINK, size=38),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_179(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_179("sv", [
    "Käthe kauft von ihrem Nachbarn Herrn Wöhler dessen Kleinwagen für 4.000 €. Herr Wöhler ist Eigentümer des Autos. "
    "Käthe zahlt sofort, und Herr Wöhler gibt ihr die Zulassungsbescheinigung Teil II.",
    "Weil er nächste Woche umzieht, möchte Herr Wöhler den Wagen bis Samstag noch fahren. Käthe leiht ihm das Auto bis "
    "Samstag. Beide sind sich einig, dass das Auto ab heute Käthe gehört.",
], "Ist Käthe schon heute Eigentümerin?")

# ===========================================================================================================================
# C Einordnung: § 929 S. 1, Übergabe fehlt, Zulassungsbescheinigung Teil II
# ===========================================================================================================================
folie([("p929", "Einordnung · § 929 S. 1 BGB"), ("fehlt", "Einordnung · Übergabe fehlt"),
       ("zbk", "Einordnung · Zulassungsbescheinigung Teil II")], rechts_frei([
    *tafel("p929", "Eigentum ohne Übergabe?"),
    z("Normalfall § 929 S. 1 BGB: Einigung und Übergabe", 110, 180, "p929", "Bold", 34),
    z("Schema: Video „Einigung und Übergabe“", 110, 230, beim("p929", "Schema"), "Bold", 30, farbe=TEXT),
    *okz("Einigung: Die beiden sind sich einig.", 295, "einig", "Bold", 34, x=160),
    *neinz("Übergabe fehlt: Herr Wöhler fährt weiter.", 360, "fehlt", "Bold", 34, x=160),
    linienzug([(130, 440), (1130, 440)], "zbk", breite=3),
    *neinz("Die Zulassungsbescheinigung hilft nicht:", 465, "zbk", "Bold", 34, x=160),
    z("verbrieft nicht das Eigentum,", 160, 525, beim("zbk2", "verbrieft"), size=34),
    z("ihre Übergabe ersetzt nicht die Übergabe des Autos", 160, 575, beim("zbk2", "ersetzt"), size=34),
    zit("BGH, Urt. v. 23.9.2022 – V ZR 148/21, Rn. 20 f.", 160, 630, beim("zbk2", "verbrieft")),
    blk(110, 690, 1040, 76, HELL, "zbk3", [("wichtig erst beim guten Glauben", "Bold", 34, INK)]),
    *requisit([("p929", ("ph", "handshake", 110, GELB), "§ 929 S. 1", WEISS),
               ("einig", ("ph", "handshake", 110, GRUEN), "einig", GRUEN),
               ("fehlt", ("tabler", "car", 150, AUTOFARBE), "Übergabe fehlt", HELLROT),
               ("zbk", ("tabler", "file-certificate", 100, WEISS), "kein Eigentumsnachweis", WEISS),
               ("zbk3", ("tabler", "shield-check", 100, GRUEN), "guter Glaube", GELB)]),
    *zwei("WO", [("p929", "ruhig"), ("fehlt", "froh")], "KA", [("p929", "ruhig"), ("fehlt", "denkt"), ("zbk", "sorge"),
                                                              ("zbk3", "ernst")]),
]))

# ===========================================================================================================================
# D Übergabesurrogate: drei Wege
# ===========================================================================================================================
folie([("surr", "Übergabesurrogate · drei Wege")], ([   # Autos bewusst auf der Tafel (Illustration der 3 Fälle)
    *tafel("surr", "Die Übergabesurrogate"),
    blk(110, 190, 1040, 90, GELB, "surr", [("3 Wege, die Übergabe zu ersetzen", "ExtraBold", 38, INK)]),
    *[e for i in range(3) for e in (auto(300 + i * 330, 600, (("drei", 0.0) if i == 0 else beim("drei", "kurzen") if i == 1
                                                         else beim("drei", "Fällen")), breite=230),
                                     pl(str(i + 1), 300 + i * 330, 630, (("drei", 0.0) if i == 0 else beim("drei", "kurzen")
                                                                         if i == 1 else beim("drei", "Fällen")),
                                        fill=WEISS, size=40, anker="m"))],
    pl("3 kurze Fälle, immer dasselbe Auto", 630, 760, beim("drei", "immer"), fill=WEISS, size=34, anker="m"),
    *zwei("WO", [("surr", "ruhig")], "KA", [("surr", "froh")]),
]))

# ===========================================================================================================================
# E 1. § 929 S. 2: Bühne (Auto steht schon bei Käthe)
# ===========================================================================================================================
P1 = "1. § 929 S. 2 BGB"
FAEHRT0, FAEHRT1 = beim("s1fall", "geliehen"), beim("s1fall", "Einfahrt")
folie([("s1", f"{P1} › Erwerber hat das Auto")], [
    *buehne("s1", hart),
    hart(pl("1. § 929 S. 2 BGB", 70, 30, "s1", fill=GELB, size=38)),
    bis_(hart(auto(CW, BODEN, "s1", anim="cut")), FAEHRT0),
    szene(bewegt(auto(CK, BODEN, FAEHRT0, anim="cut"), FAEHRT0, FAEHRT1, CW - CK, 0), "179motor*", 0.7, 0.0),
    pl("Angenommen: vor 2 Wochen geliehen", 70, 110, FAEHRT0, fill=WEISS, size=34, bis="ka2"),
    pl("Das Auto steht schon bei Käthe.", 70, 190, FAEHRT1, fill=BLAU, size=34, bis="ka2"),
    *fig("WO", WX, BODEN, FH, [("s1", "ruhig_r")], bis="wo3", erst="cut"),
    hart(ns("Herr Wöhler", WX, BODEN, "s1", GRUEN)),
    *fig("KA", KX, BODEN, FH, [("s1", "ruhig")], bis="ka2", erst="cut"),
    hart(ns("Käthe", KX, BODEN, "s1", BLAU)),
    *redet("KA_redet", KX, BODEN, FH, "ka2", "wo3"),
    blase("sprech", 560, 230, "ka2", 1250, 230, inhalt=["Das Auto steht ja", "schon bei mir."], textsize=38,
          figur=("KA_redet", KX, BODEN, FH), bis="wo3"),
    *fig("KA", KX, BODEN, FH, [("wo3", "froh")], erst="cut"),
    *redet("WO_redet_r", WX, BODEN, FH, "wo3", "w929"),
    blase("sprech", 560, 230, "wo3", 720, 230, inhalt=["Dann gehört es", "ab jetzt Ihnen."], textsize=38,
          figur=("WO_redet_r", WX, BODEN, FH), bis="w929"),
])

# --- F 1. Tafel: Wortlautkarte § 929 S. 2 ----------------------------------------------------------------------------------
_zi = lambda zl, wort: next(i for i, t in enumerate(zl) if wort in t)
W2 = umbruch("„Ist der Erwerber im Besitz der Sache, so genügt die Einigung über den Übergang des Eigentums.“", 34, 1040)
w2, w2_y = wortlaut(80, 180, 1100, W2, "§ 929 S. 2 BGB", "w929", marken=[
    (_zi(W2, "im Besitz"), "im Besitz", beim("w929", "Besitz")),
    (_zi(W2, "genügt die Einigung"), "genügt die Einigung", beim("w929", "genügt"))], size=34)
folie([("w929", f"{P1} › Einigung genügt"), ("kh", f"{P1} › Übereignung kurzer Hand")], rechts_frei([
    *tafel("w929", "1. Der Erwerber hat die Sache"),
    *w2,
    *okz("Herr Wöhler muss nichts mehr übergeben.", w2_y + 40, "s1b", "Bold", 34, x=160),
    blk(110, w2_y + 115, 1040, 80, GRUEN, beim("s1b", "Käthe"), [("Käthe wird sofort Eigentümerin.", "ExtraBold", 36, INK)]),
    blk(110, w2_y + 225, 1040, 80, HELL, "kh", [("„Übereignung kurzer Hand“", "ExtraBold", 36, INK)]),
    *requisit([("w929", ("tabler", "book", 100, WEISS), "Satz 2", GELB),
               ("s1b", ("tabler", "car", 150, AUTOFARBE), "Auto schon bei Käthe", BLAU),
               ("kh", ("ph", "handshake", 110, GRUEN), "kurzer Hand", GRUEN)]),
    *zwei("WO", [("w929", "ruhig"), ("kh", "froh")], "KA", [("w929", "denkt"), ("s1b", "froh")]),
]))
assert w2_y + 305 <= 900, w2_y

# ===========================================================================================================================
# G 2. § 930: Bühne (Herr Wöhler behält das Auto)
# ===========================================================================================================================
P2 = "2. § 930 BGB"
folie([("s2", f"{P2} › Veräußerer behält das Auto")], [
    *buehne("s2", hart),
    hart(pl("2. § 930 BGB: unser Fall", 70, 30, "s2", fill=GELB, size=38)),
    hart(auto(CW, BODEN, "s2", anim="cut")),
    *personen("s2", [("s2", "ruhig_r"), (beim("s2", "behält"), "froh_r")], [("s2", "ruhig")]),
    ficon("tabler", "key", WX + 130, HAND, 60, beim("s2", "behält"), fuell=GELB),
    pl("Herr Wöhler behält das Auto.", 70, 110, beim("s2", "Herr"), fill=GRUEN, size=34),
])

# --- H Wortlautkarte § 930 --------------------------------------------------------------------------------------------------
W930 = umbruch("„Ist der Eigentümer im Besitz der Sache, so kann die Übergabe dadurch ersetzt werden, dass zwischen ihm und "
               "dem Erwerber ein Rechtsverhältnis vereinbart wird, vermöge dessen der Erwerber den mittelbaren Besitz "
               "erlangt.“", 34, 1040)
w930, w930_y = wortlaut(80, 180, 1100, W930, "§ 930 BGB", "w930", marken=[
    (_zi(W930, "Eigentümer im Besitz"), "Eigentümer im Besitz", beim("w930", "Eigentümer")),
    (_zi(W930, "Rechtsverhältnis"), "Rechtsverhältnis", beim("w930", "Rechtsverhältnis")),
    (_zi(W930, "mittelbaren Besitz"), "mittelbaren Besitz", beim("w930", "mittelbaren"))], size=34)
folie([("w930", f"{P2} › Wortlaut"), ("bk", f"{P2} › Besitzkonstitut")], rechts_frei([
    *tafel("w930", "2. Der Veräußerer behält die Sache"),
    *w930,
    blk(110, w930_y + 45, 1040, 90, GELB, "bk", [("= das Besitzkonstitut", "ExtraBold", 40, INK)]),
    *requisit([("w930", ("tabler", "book", 100, WEISS), "§ 930", GELB),
               (beim("w930", "Rechtsverhältnis"), ("tabler", "link", 100, WEISS), "Rechtsverhältnis", WEISS),
               ("bk", ("tabler", "car", 150, AUTOFARBE), "Besitzkonstitut", GRUEN)]),
    *zwei("WO", [("w930", "ruhig"), ("bk", "froh")], "KA", [("w930", "denkt"), ("bk", "ruhig")]),
]))
assert w930_y + 135 <= 900, w930_y

# --- I Wortlautkarte § 868, Leihe ---------------------------------------------------------------------------------------------
W868 = umbruch("„Besitzt jemand eine Sache als … Mieter, Verwahrer oder in einem ähnlichen Verhältnis, vermöge dessen er "
               "einem anderen gegenüber auf Zeit zum Besitz berechtigt oder verpflichtet ist, so ist auch der andere "
               "Besitzer (mittelbarer Besitz).“", 32, 1040)
w868, w868_y = wortlaut(80, 170, 1100, W868, "§ 868 BGB", "w868", marken=[
    (_zi(W868, "Mieter"), "Mieter", beim("w868", "Miete")),
    (_zi(W868, "Verwahrer"), "Verwahrer", beim("w868", "Verwahrung")),
    (_zi(W868, "ähnlichen Verhältnis"), "ähnlichen Verhältnis", beim("w868", "ähnliches")),
    (_zi(W868, "Zeit zum"), "Zeit", beim("w868", "Zeit"))], size=32)
folie([("p868", f"{P2} › Besitzmittlungsverhältnis, § 868 BGB"), ("leih", f"{P2} › Leihe bis Samstag")], rechts_frei([
    *tafel("p868", "Welches Rechtsverhältnis?"),
    *w868,
    *okz("Eine Leihe gehört dazu.", w868_y + 30, "leih", "Bold", 34, x=160),
    zit("Entleiher als Besitzmittler: BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 26", 160, w868_y + 80, "leih"),
    blk(110, w868_y + 135, 1040, 80, GRUEN, "sub", [("Herr Wöhler: unmittelbarer Besitzer, als Entleiher", "Bold", 32, INK)]),
    blk(110, w868_y + 235, 1040, 80, BLAU, "sub2", [("Käthe: mittelbare Besitzerin", "Bold", 32, INK)]),
    *requisit([("p868", ("tabler", "book", 100, WEISS), "§ 868", GELB),
               ("leih", ("tabler", "calendar-event", 100, WEISS), "Leihe bis Samstag", WEISS),
               ("sub", ("tabler", "key", 90, GELB), "unmittelbar", GRUEN),
               ("sub2", ("tabler", "link", 100, WEISS), "mittelbar", BLAU)]),
    *zwei("WO", [("p868", "ruhig"), ("sub", "froh")], "KA", [("p868", "denkt"), ("sub2", "froh")]),
]))
assert w868_y + 315 <= 900, w868_y

# --- J Vorsicht: konkretes Besitzmittlungsverhältnis (BGH V ZR 92/25 Rn. 20) -------------------------------------------
WK = umbruch("„Ein derartiges Verhältnis muss einen konkreten Inhalt haben, aus dem es dem unmittelbaren gegenüber dem "
             "mittelbaren Besitzer auf Zeit eine Besitzberechtigung verschafft …“", 32, 1040)
wk, wk_y = wortlaut(80, 180, 1100, WK, "BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 20", "bgh", marken=[
    (_zi(WK, "konkreten Inhalt"), "konkreten Inhalt", beim("bgh", "konkreten")),
    (_zi(WK, "auf Zeit"), "auf Zeit", beim("bgh", "Zeit"))], size=32)
folie([("konk", f"{P2} › konkretes Besitzmittlungsverhältnis"), ("abstr", f"{P2} › abstrakt reicht nicht")], rechts_frei([
    *tafel("konk", "Vorsicht: konkret!"),
    *wk,
    z("Herausgabeanspruch nicht endgültig ausgeschlossen", 110, wk_y + 25, beim("bgh", "Herausgabeanspruch"), "Bold", 32),
    *neinz("„Ab jetzt besitze ich für dich“ reicht nicht (h. M.)", wk_y + 100, "abstr", "Bold", 32, x=160),
    *okz("Hier konkret: Leihe bis Samstag, dann Herausgabe", wk_y + 170, "hier", "Bold", 32, x=160),
    *requisit([("konk", ("tabler", "alert-triangle", 100, GELB), "Vorsicht", HELLROT),
               (beim("bgh", "konkreten"), ("tabler", "list-check", 100, WEISS), "konkreter Inhalt", WEISS),
               ("abstr", ("tabler", "eye-off", 100, HELLGRAU), "bloß abstrakt", HELLROT),
               ("hier", ("tabler", "calendar-event", 100, WEISS), "Leihe bis Samstag", GRUEN)]),
    *zwei("WO", [("konk", "ernst"), ("hier", "froh")], "KA", [("konk", "denkt"), ("abstr", "sorge"), ("hier", "froh")]),
]))
assert wk_y + 240 <= 900, wk_y

# --- K Praxis: Sicherungsübereignung, Bestimmtheit --------------------------------------------------------------------------
folie([("sue", f"{P2} › Sicherungsübereignung"), ("best", f"{P2} › Bestimmtheit")], rechts_frei([
    *tafel("sue", "Praxis: Sicherungsübereignung"),
    blk(110, 185, 1040, 130, HELL, beim("sue", "Bank"), [("Die Bank wird Eigentümerin,", "Bold", 34, INK),
                                                       ("der Kreditnehmer behält die Sache.", "Bold", 34, INK)]),
    zit("§§ 929 S. 1, 930 BGB; BGH, Beschl. v. 16.9.2015 – V ZR 8/15, Rn. 7", 110, 335, beim("sue", "Bank")),
    linienzug([(130, 405), (1130, 405)], "best", breite=3),
    z("Bestimmtheit:", 110, 430, "best", "ExtraBold", 36),
    z("Wer die Abreden kennt, muss ohne Weiteres sehen,", 110, 490, beim("best", "Wer"), size=34),
    z("welche Sachen übereignet sind.", 110, 540, beim("best", "welche"), size=34),
    zit("BGH, Urt. v. 16.12.2022 – V ZR 174/21, Rn. 10", 110, 600, beim("best", "welche")),
    *requisit([("sue", ("tabler", "building-bank", 110, BLAU), "Bank: Eigentümerin", WEISS),
               (beim("sue", "Kreditnehmer"), ("tabler", "car", 150, AUTOFARBE), "Kreditnehmer behält", GELB),
               ("best", ("tabler", "list-check", 100, WEISS), "bestimmt?", WEISS)]),
    *zwei("WO", [("sue", "ruhig"), ("best", "denkt")], "KA", [("sue", "ruhig"), ("best", "ernst")]),
]))

# ===========================================================================================================================
# L 3. § 931: Bühne (das Auto steht in der Werkstatt)
# ===========================================================================================================================
P3 = "3. § 931 BGB"
WM_X = 1215
WM_DA = beim("s3fall", "Werkstatt")
folie([("s3", f"{P3} › Dritter hat das Auto")], [
    *buehne("s3", hart),
    hart(pl("3. § 931 BGB", 70, 30, "s3", fill=GELB, size=38)),
    *personen("s3", [("s3", "ruhig_r")], [("s3", "ruhig"), (WM_DA, "denkt")], bis="wo4"),
    pl("Das Auto steht bei einem Dritten.", 70, 110, beim("s3", "Auto"), fill=WEISS, size=34, bis="wo4"),
    ficon("tabler", "car-garage", CM - 60, BODEN, 300, beim("s3", "Dritten"), fuell=ORANGE),
    *fig("WM", WM_X, BODEN, FH, [(WM_DA, "ruhig_r"), ("wo4", "ruhig")]),
    ns("Werkstatt", WM_X, BODEN, WM_DA, ORANGE, d=0.1),
    pl("in der Werkstatt zur Reparatur", 70, 190, WM_DA, fill=ORANGE, size=34, bis="wo4"),
    ficon("tabler", "tool", WM_X, 400, 70, beim("s3fall", "Reparatur"), fuell=WEISS, bis="wo4"),
    *redet("WO_redet_r", WX, BODEN, FH, "wo4", "w931"),
    blase("sprech", 820, 300, "wo4", 760, 215, inhalt=["Holen Sie ihn in der Werkstatt ab.", "Meinen Anspruch auf Herausgabe",
                                                         "trete ich Ihnen ab."], textsize=36,
          figur=("WO_redet_r", WX, BODEN, FH), bis="w931"),
    *fig("KA", KX, BODEN, FH, [("wo4", "froh")], erst="cut"),
    ns("Herr Wöhler", WX, BODEN, "wo4", GRUEN, anim="cut"), ns("Käthe", KX, BODEN, "wo4", BLAU, anim="cut"),
])

# --- M Wortlautkarte § 931, Werkstatt als Besitzmittlerin -------------------------------------------------------------------
W931 = umbruch("„Ist ein Dritter im Besitz der Sache, so kann die Übergabe dadurch ersetzt werden, dass der Eigentümer dem "
               "Erwerber den Anspruch auf Herausgabe der Sache abtritt.“", 34, 1040)
w931, w931_y = wortlaut(80, 180, 1100, W931, "§ 931 BGB", "w931", marken=[
    (_zi(W931, "Dritter im Besitz"), "Dritter im Besitz", beim("w931", "Dritter")),
    (_zi(W931, "Anspruch"), "Anspruch", beim("w931", "Anspruch")),
    (_zi(W931, "abtritt"), "abtritt", beim("w931", "abtritt"))], size=34)
folie([("w931", f"{P3} › Abtretung des Herausgabeanspruchs"), ("werk", f"{P3} › Werkstatt als Besitzmittlerin")], rechts_frei([
    *tafel("w931", "3. Ein Dritter hat die Sache"),
    *w931,
    blk(110, w931_y + 40, 1040, 130, ORANGE, beim("werk", "Werkstatt"), [("Die Werkstatt besitzt für Herrn Wöhler:", "Bold", 32, INK),
                                                                     ("Werkvertrag = Besitzmittlungsverhältnis", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 17.3.2017 – V ZR 70/16, Rn. 16", 110, w931_y + 185, beim("werk", "Werkvertrag")),
    *requisit([("w931", ("tabler", "book", 100, WEISS), "§ 931", GELB),
               ("werk", ("tabler", "car-garage", 150, ORANGE), "Besitzmittlerin", WEISS)]),
    *zwei("WO", [("w931", "ruhig"), ("werk", "froh")], "WM", [("w931", "ruhig"), ("werk", "froh")]),
]))
assert w931_y + 230 <= 900, w931_y

# --- N Abtretung §§ 398, 870, § 986 Abs. 2 ---------------------------------------------------------------------------------
folie([("abtr", f"{P3} › §§ 398, 870 BGB"), ("p986", f"{P3} › § 986 Abs. 2 BGB")], rechts_frei([
    *tafel("abtr", "Abtretung des Herausgabeanspruchs"),
    z("Abtretung nach § 398 BGB", 110, 185, "abtr", "Bold", 36),
    z("mit dem Anspruch geht der mittelbare Besitz über,", 110, 245, "p870", size=34),
    z("§ 870 BGB", 110, 293, beim("p870", "Paragraf"), "Bold", 34),
    *okz("Werkstatt: in der Regel weder Mitwirkung", 370, beim("ohne", "weder"), "Bold", 34, x=160),
    z("noch Kenntnis nötig", 160, 420, beim("ohne", "wissen"), "Bold", 34),
    zit("BGH, Urt. v. 11.1.2018 – IX ZR 295/16, Rn. 34", 160, 475, beim("ohne", "wissen")),
    blk(110, 540, 1040, 130, HELLROT, beim("p986", "entgegenhalten"), [("§ 986 Abs. 2 BGB: Einwendungen bleiben,", "Bold", 32, INK),
                                                                    ("etwa: Reparatur noch nicht bezahlt", "Bold", 32, INK)]),
    *requisit([("abtr", ("tabler", "file-text", 100, WEISS), "Abtretung", GELB),
               ("p870", ("tabler", "link", 100, WEISS), "mittelbarer Besitz", BLAU),
               ("ohne", ("tabler", "eye-off", 100, HELLGRAU), "ohne Kenntnis", WEISS),
               ("p986", ("tabler", "file-invoice", 100, WEISS), "Rechnung offen?", HELLROT)]),
    *zwei("WM", [("abtr", "ruhig"), ("p986", "ernst")], "KA", [("abtr", "froh"), ("p986", "sorge")]),
]))

# ===========================================================================================================================
# O Merktabelle
# ===========================================================================================================================
SP_X = (110, 560, 1520)
ZEILEN = [("t1", "der Erwerber", "die Einigung genügt", "§ 929 S. 2", HELLGRUEN),
          ("t2", "der Veräußerer", "Besitzmittlungsverhältnis", "§ 930", HELL),
          ("t3", "ein Dritter", "Abtretung des Herausgabeanspruchs", "§ 931", (232, 240, 253, 255))]
els_tab = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Merktabelle: Wer hat die Sache?"), 110, 90, "tab", 46),
           z("Wer hat die Sache?", SP_X[0], 200, "tab", "ExtraBold", 36, rechts=1800),
           z("Was ersetzt die Übergabe?", SP_X[1], 200, "tab", "ExtraBold", 36, rechts=1800),
           z("Norm", SP_X[2], 200, "tab", "ExtraBold", 36, rechts=1800),
           linienzug([(100, 262), (1820, 262)], "tab", breite=4)]
for i, (c, wer, was, norm, fill) in enumerate(ZEILEN):
    y = 290 + i * 150
    els_tab += [karte(90, y, 1740, 125, c, fill=fill, rund=16, schatten=5, rand=4),
                z(wer, SP_X[0] + 20, y + 38, c, "Bold", 38, rechts=1800),
                z(was, SP_X[1], y + 38, c, "Bold", 38, rechts=1800),
                z(norm + " BGB", SP_X[2], y + 38, c, "ExtraBold", 38, rechts=1800)]
els_tab.append(blk(90, 770, 1740, 90, GELB, "t4", [("Die Einigung braucht es immer.", "ExtraBold", 40, INK)]))
folie([("tab", "Merktabelle · Wer hat die Sache?")], els_tab)

# ===========================================================================================================================
# P Ausblick: gutgläubiger Erwerb
# ===========================================================================================================================
folie([("gut", "Ausblick · gutgläubiger Erwerb")], rechts_frei([
    *tafel("gut", "Ausblick: nicht Eigentümer?"),
    z("Auto gehört gar nicht Herrn Wöhler?", 110, 185, "gut", "Bold", 34),
    blk(110, 255, 1040, 90, HELL, beim("gut2", "gutgläubigen"), [("Gutgläubig: §§ 932 Abs. 1 S. 2, 933, 934 BGB", "ExtraBold", 36, INK)]),
    z("beim Besitzkonstitut erst mit der Übergabe (§ 933 BGB)", 110, 380, "gut3", size=34),
    zit("Videos „Gutgläubiger Erwerb“ und „Abhandenkommen“", 110, 440, beim("gut3", "mehr")),
    *requisit([("gut", ("tabler", "alert-triangle", 100, GELB), "nicht Eigentümer?", HELLROT),
               (beim("gut2", "gutgläubigen"), ("tabler", "shield-check", 100, GRUEN), "guter Glaube", WEISS),
               ("gut3", ("tabler", "key", 90, GELB), "erst mit Übergabe", WEISS)]),
    *zwei("WO", [("gut", "denkt")], "KA", [("gut", "sorge"), ("gut3", "ernst")]),
]))

# ===========================================================================================================================
# Q Lösung
# ===========================================================================================================================
folie([("loes", "Lösung · Käthe"), ("l4", "Lösung › Käthe schon heute Eigentümerin")], rechts_frei([
    *tafel("loes", "Die Lösung"),
    *okz("Einigung: Eigentum soll sofort übergehen", 185, "l1", "Bold", 34, x=160),
    *okz("statt Übergabe: Leihe bis Samstag,", 255, "l2", "Bold", 34, x=160),
    z("ein konkretes Besitzmittlungsverhältnis", 160, 305, beim("l2", "konkretes"), size=34),
    *okz("Herr Wöhler: Eigentümer und Besitzer", 375, "l3", "Bold", 34, x=160),
    blk(110, 455, 1040, 90, GRUEN, "l4", [("Käthe ist schon heute Eigentümerin.", "ExtraBold", 38, INK)]),
    z("§§ 929 S. 1, 930 BGB", 110, 565, beim("l4", "Paragraf"), "Bold", 34),
    z("Samstag: Herr Wöhler muss den Wagen herausgeben.", 110, 640, "l5", size=34),
    *requisit([("loes", ("ph", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("l2", ("tabler", "calendar-event", 100, WEISS), "Leihe bis Samstag", WEISS),
               ("l4", ("tabler", "car", 150, AUTOFARBE), "Eigentümerin: Käthe", BLAU),
               ("l5", ("tabler", "key", 90, GELB), "Samstag: Herausgabe", WEISS)]),
    *zwei("WO", [("loes", "ruhig"), ("l5", "froh")], "KA", [("loes", "denkt"), ("l4", "froh")]),
]))

# ===========================================================================================================================
# R Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Wer hat die Sache?"), ("tp3", "Klausurtipp · Besitzmittlungsverhältnis nennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst die Einigung prüfen,", 200, 200, "tipp", "Bold", 36),
    z("dann fragen: Wer hat die Sache gerade?", 200, 260, beim("tipp", "Wer"), "Bold", 36),
    z("Davon hängt ab, welches Surrogat passt.", 200, 340, "tp2", size=34),
    linienzug([(130, 420), (1130, 420)], "tp3", breite=3),
    z("Besitzkonstitut: das konkrete", 200, 450, "tp3", "Bold", 36),
    z("Besitzmittlungsverhältnis nennen,", 200, 505, beim("tp3", "Besitzmittlungsverhältnis"), "Bold", 36),
    z("hier: die Leihe bis Samstag", 200, 565, beim("tp3", "Leihe"), "ExtraBold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# S Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Einigung", True),
          ("c2", 0, "II. Übergabe oder Übergabesurrogat", True),
          ("c2a", 1, "Erwerber besitzt: § 929 S. 2 BGB", False),
          ("c2b", 1, "Veräußerer besitzt: Besitzkonstitut, § 930 BGB", False),
          ("c2c", 1, "Dritter besitzt: Abtretung, § 931 BGB", False),
          ("c3", 0, "III. Einigsein in diesem Zeitpunkt", True),
          ("c4", 0, "IV. Berechtigung (sonst gutgläubiger Erwerb)", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Übereignung ohne Übergabe"), 110, 90, "sch", 46),
           z("§ 929 S. 1 BGB mit den Surrogaten §§ 929 S. 2, 930, 931 BGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 245
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 95, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Einigung"), ("c2", "Prüfschema › II. Übergabe oder Surrogat"),
       ("c3", "Prüfschema › III. Einigsein"), ("c4", "Prüfschema › IV. Berechtigung")], els_sch)

# ===========================================================================================================================
# T Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Eigentum geht auch", 0)], [("ohne Übergabe", "a"), (" über.", 0)]], 750, 300, 48, "merke",
                {"a": beim("merke", "ohne")}),
    *markertext([[("Entscheidend ist, wer die Sache hat:", 0)], [("der Erwerber, der Veräußerer", 0)],
                 [("oder ein ", 0), ("Dritter", "b"), (".", 0)]], 750, 540, 44, "m2", {"b": beim("m2", "Dritter")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
