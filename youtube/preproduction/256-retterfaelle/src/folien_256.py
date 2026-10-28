"""Folge 256 · Retterfälle: Der Retter stirbt – haftet der Brandstifter? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall nach dem Plan-Hook: Siegbert legt im Keller seines Mehrfamilienhauses Feuer und geht; Mieterin Liesbeth kommt vom
Einkaufen, ihre Kinder sind noch in der Wohnung; Nachbar Arndt läuft hinein, schickt die Kinder über das Vordach ins Freie und
stürzt beim Rückweg durch die brennende Decke (nicht im Bild). Echter Fall BGHSt 39, 322 (BGH, Urt. v. 8.9.1993 – 3 StR 341/93,
keine realen Personen als Figuren); § 222 (Wortlautkarte), Selbstgefährdung (Verweis 058), Fremdgefährdung (Verweis 203),
BGH Rn. 9 f., Leitsatz 1, Grenze; Berufsretter (BGHSt 66, 119); Lehre; § 306c (Wortlautkarte), § 306a Abs. 1 Nr. 1, § 307 Nr. 1
a. F.; Leichtfertigkeit; Klausurtipp, Schema und Merksatz mit Lexi.
DARSTELLUNG: Feuer stilisiert (Tabler flame, cloud-fog), keine brennenden Menschen, kein Sturz, keine Leiche; Kinder nur als
Silhouetten in Sicherheit; Arndt respektvoll (entschlossen), nach seinem Tod nicht mehr im Bild, nur eine Kerze.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit als eigene
Kopie aus Folge 235 (gemeinsame Dateien unverändert); neu: Haus, flamme().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_256/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_256/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SI": "Siegbert", "AR": "Arndt", "LI": "Liesbeth"}
NFARBE = {"SI": GRUEN, "AR": BLAU, "LI": LILA}
WAND = (246, 236, 220, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))

def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]



# --- Folge 256: Größen, Haus- und Feuerbausteine --------------------------------------------------------------------------
GROESSE = {"SI": 1.0, "AR": 1.0, "LI": 0.94, "K1": 0.62, "K2": 0.55}
BLAUHELL_ = BLAUHELL


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


class Haus:
    """Mehrfamilienhaus aus dem Tabler-Icon „building“ (Rahmen x 5–19, y 3–21, Fenster bei x 9,5/14,5 und y 8/12/16);
    xy() rechnet Icon-Einheiten in Bildpunkte um, damit Flammen und Rauch an Fenstern und Keller sitzen."""

    def __init__(self, cx, breite, cue):
        self.el = hart(ficon("tabler", "building", cx, BODEN + 4, breite, cue, fuell=WAND, anim="cut"))
        self.u = self.el.sprite.width / 20.0          # Grundlinie 2–22 inkl. Strich

    def xy(self, X, Y):
        return self.el.x + (X - 2) * self.u, self.el.y + (Y - 2) * self.u


def flamme(haus, X, Y, breite, cue, bis=None):
    x, y = haus.xy(X, Y)
    return ficon("tabler", "flame", x, y + breite * 0.55, breite, cue, fuell=ROT, nebenfarbe=GELB, bis=bis)


# ===========================================================================================================================
# A Fall: Abend vor dem Mehrfamilienhaus – Siegbert legt Feuer, Liesbeth, Arndt läuft hinein, Kinder in Sicherheit
# ===========================================================================================================================
HAUS = Haus(470, 780, NULL)
SIX0, SIX1, LIX, ARX, TUER = 950, 1300, 1500, 1200, 470
FH_ = {k: hh(k, FH) for k in GROESSE}
VERL = beim("feuer", "verlässt")
HOFFT = beim("feuer", "hofft")
LAUF = beim("rein", "läuft"), beim("rein", "Haus", ende=True)
SICHER = beim("kinder", "Sie", nr=2)
STIRBT = beim("decke", "Arndt")
keller = flamme(HAUS, 6.5, 19.2, 70, beim("feuer", "Feuer"))
fl1 = flamme(HAUS, 9.5, 15.0, 80, "rauch")
szene(fl1, "256feuer*", 0.55, 0.0)                     # Knistern, wenn die Flammen sichtbar im Haus stehen
arndt_lauf = bewegt(peep_voll("AR_entschlossen", TUER, BODEN, FH_["AR"], LAUF[0], anim="cut", bis="kinder"),
                    LAUF[0], LAUF[1], ARX - TUER)
szene(arndt_lauf, "256laufen*", 0.5, 0.0)              # Laufschritte, während Arndt sichtbar zum Haus läuft
folie([(NULL, "Fall · Ein Mittwochabend in der Stadt"), ("siegbert", "Fall · Siegbert und sein Mehrfamilienhaus"),
       ("feuer", "Fall · Feuer im Keller"), ("rauch", "Fall · Flammen und Rauch"),
       ("liesbeth", "Fall · Liesbeth kommt vom Einkaufen"), ("li1", "Fall · Die Kinder sind noch im Haus"),
       ("arndt", "Fall · Nachbar Arndt"), ("ar1", "Fall · „Ich hole sie raus!“"), ("rein", "Fall · Arndt läuft ins Haus"),
       ("kinder", "Fall · Die Kinder sind in Sicherheit"), ("decke", "Fall · Der Retter stirbt")], [
    boden(NULL),
    HAUS.el,
    hart(ficon("tabler", "home", 1770, BODEN + 4, 240, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "moon", 1820, 160, 80, NULL, fuell=GELB, anim="cut")),
    bis_(hart(pl("Ein Mittwochabend in der Stadt", 70, 30, NULL, fill=GELB, size=32)), "siegbert"),
    # Siegbert: Hauseigentümer, legt Feuer, geht
    *fig("SI", SIX0, BODEN, FH_["SI"], [("siegbert", "ruhig"), ("feuer", "ernst")], bis=VERL),
    bis_(ns(NAME["SI"], SIX0, BODEN, "siegbert", NFARBE["SI"], d=0.1), VERL),
    *fig("SI", SIX1, BODEN, FH_["SI"], [(VERL, "ruhig_r"), (HOFFT, "denkt_r")], bis="rauch", erst="cut"),
    bis_(ns(NAME["SI"], SIX1, BODEN, VERL, NFARBE["SI"], anim="cut"), "rauch"),
    bis_(pl("Siegbert, Anfang 60, besitzt ein Mehrfamilienhaus.", 70, 30, "siegbert", fill=GRUEN, size=32), "feuer"),
    bis_(pl("Darin wohnen mehrere Familien.", 70, 94, beim("siegbert", "Darin"), fill=WEISS, size=30), "feuer"),
    bis_(ficon("tabler", "users", 1180, 330, 90, beim("siegbert", "Darin"), fuell=WEISS), "feuer"),
    keller,
    bis_(pl("Im Keller legt er Feuer und verlässt das Haus.", 70, 30, "feuer", fill=ROT, size=32), "rauch"),
    bis_(pl("Er hofft, dass niemand zu Schaden kommt.", 70, 94, HOFFT, fill=WEISS, size=30), "rauch"),
    fl1,
    flamme(HAUS, 14.5, 11.0, 80, beim("rauch", "Rauch")),
    ficon("tabler", "cloud-fog", HAUS.xy(16, 3)[0], HAUS.xy(12, 5.5)[1], 240, beim("rauch", "Rauch"), fuell=HELLGRAU),
    bis_(pl("Flammen und Rauch breiten sich schnell aus.", 70, 30, "rauch", fill=ROT, size=32), "liesbeth"),
    # Liesbeth: kommt vom Einkaufen, ruft; Arndt: Nachbar, läuft hinein
    *fig("LI", LIX, BODEN, FH_["LI"], [("liesbeth", "ruhig"), (beim("liesbeth", "Ihre"), "angst")], bis="li1"),
    *redet("LI_redet", LIX, BODEN, FH_["LI"], "li1", "arndt"),
    *fig("LI", LIX, BODEN, FH_["LI"], [("arndt", "sorge"), (LAUF[0], "angst"), (SICHER, "froh"),
                                        ("decke", "schreck"), (STIRBT, "feierlich")], erst="cut"),
    ns(NAME["LI"], LIX, BODEN, "liesbeth", NFARBE["LI"], d=0.1),
    bis_(ficon("tabler", "shopping-bag", LIX - 115, BODEN - 4, 70, "liesbeth", fuell=GELB), "li1"),
    bis_(pl("Liesbeth kommt vom Einkaufen.", 70, 30, "liesbeth", fill=LILA, size=32), "arndt"),
    bis_(pl("Ihre beiden Kinder sind noch oben in der Wohnung.", 70, 94, beim("liesbeth", "Ihre"), fill=WEISS, size=30), "arndt"),
    blase("sprech", 560, 200, "li1", 1330, 200, inhalt=["Meine Kinder sind", "noch da drin!"], textsize=36,
          figur=("LI_redet", LIX, BODEN, FH_["LI"]), bis="arndt"),
    *fig("AR", ARX, BODEN, FH_["AR"], [("arndt", "entschlossen")], bis="ar1"),
    *redet("AR_redet_r", ARX, BODEN, FH_["AR"], "ar1", "rein"),
    *fig("AR", ARX, BODEN, FH_["AR"], [("rein", "entschlossen")], bis=LAUF[0], erst="cut"),
    bis_(ns(NAME["AR"], ARX, BODEN, "arndt", NFARBE["AR"], d=0.1), LAUF[0]),
    bis_(pl("Arndt, um die 40, wohnt im Haus nebenan.", 70, 30, "arndt", fill=BLAU, size=32), "rein"),
    bis_(pl("Er zögert keinen Moment.", 70, 94, beim("arndt", "Er"), fill=WEISS, size=30), "rein"),
    blase("sprech", 460, 170, "ar1", 1250, 250, inhalt=["Ich hole sie raus!"], textsize=36,
          figur=("AR_redet_r", ARX, BODEN, FH_["AR"]), bis="rein"),
    arndt_lauf,
    bewegt(bis_(ns(NAME["AR"], TUER, BODEN, LAUF[0], NFARBE["AR"], anim="cut"), "kinder"), LAUF[0], LAUF[1], ARX - TUER),
    bis_(pl("Arndt läuft in das brennende Haus.", 70, 30, "rein", fill=BLAU, size=32), "kinder"),
    flamme(HAUS, 9.5, 7.0, 80, "kinder"),
    # Kinder in Sicherheit (Silhouetten, ohne Namen), Arndt stirbt (nicht im Bild)
    peep_voll("K1_kind_r", 1270, BODEN, FH_["K1"], SICHER, anim="pop"),
    peep_voll("K2_kind_r", 1360, BODEN, FH_["K2"], SICHER, anim="pop", d=0.15),
    bis_(pl("Er schickt die Kinder über das Vordach ins Freie.", 70, 30, "kinder", fill=BLAU, size=32), "decke"),
    bis_(pl("Sie sind in Sicherheit.", 70, 94, SICHER, fill=GRUEN, size=30), "decke"),
    flamme(HAUS, 14.5, 7.0, 80, "decke"),
    flamme(HAUS, 14.5, 15.0, 80, "decke"),
    pl("Als er selbst folgen will, stürzt er durch die brennende Decke.", 70, 30, "decke", fill=ROT, size=30),
    pl("Arndt stirbt.", 70, 94, STIRBT, fill=WEISS, size=30),
    ficon("tabler", "candle", 900, BODEN - 4, 80, STIRBT, fuell=WEISS, nebenfarbe=GELB),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Der Retter ging freiwillig ins Feuer"), ("frage2", "Die Frage · Unterbrochene Zurechnung?")], [
    *tafel("frage", "Die Frage"),
    z("Arndt ging freiwillig ins Feuer.", 110, 190, "frage", "Bold", 38),
    blk(110, 270, 1040, 130, GELB, beim("frage", "Muss"), [("Muss Siegbert trotzdem für", "ExtraBold", 38, INK),
                                                         ("seinen Tod einstehen?", "ExtraBold", 38, INK)]),
    blk(110, 450, 1040, 130, LILAHELL, "frage2", [("Oder unterbricht seine freie", "ExtraBold", 36, INK),
                                               ("Entscheidung die Zurechnung?", "ExtraBold", 36, INK)]),
    *requisit([("frage", ("tabler", "flame", 100, ROT), "freiwillig ins Feuer", WEISS),
               ("frage2", ("tabler", "link", 110, LILAHELL), "Zurechnung?", LILAHELL)]),
    *stehend("SI", FX, [("frage", "ernst"), ("frage2", "denkt")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_256(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_256("sv", [
    "Ein Mittwochabend. Siegbert besitzt ein Mehrfamilienhaus, in dem mehrere Familien wohnen. Im Keller legt er Feuer "
    "und verlässt das Haus; er hofft, dass niemand zu Schaden kommt. Flammen und Rauch breiten sich schnell aus.",
    "Mieterin Liesbeth kommt vom Einkaufen. Ihre beiden Kinder sind noch in der Wohnung: „Meine Kinder sind noch da "
    "drin!“ Nachbar Arndt (um 40) aus dem Haus nebenan ruft „Ich hole sie raus!“ und läuft in das brennende Haus.",
    "Er findet die Kinder und schickt sie über das Vordach ins Freie; sie sind in Sicherheit. Als er selbst folgen will, "
    "stürzt er durch die brennende Decke und stirbt.",
], "Wie hat sich Siegbert strafbar gemacht?")

# ===========================================================================================================================
# C Der echte Fall: BGH, Urt. v. 8.9.1993 – 3 StR 341/93, BGHSt 39, 322 (keine realen Personen als Figuren)
# ===========================================================================================================================
QB = "BGH, Urt. v. 8.9.1993 – 3 StR 341/93"
folie([("bgh", "Der echte Fall · BGHSt 39, 322"), ("bgh2", "Der echte Fall · Brand während einer Feier"),
       ("bgh3", "Der echte Fall · Verurteilung bestätigt")], [
    *tafel("bgh", "Der echte Fall: BGHSt 39, 322"),
    z(f"{QB}", 110, 180, beim("bgh", "Urteil"), "Bold", 34),
    z("Während einer Feier zündet der Angeklagte", 110, 260, "bgh2", size=34),
    z("ein Wohnhaus an.", 110, 308, "bgh2", size=34),
    z("Der 22-jährige Sohn der Eigentümer läuft ins", 110, 378, beim("bgh2", "zweiundzwanzigjährige"), size=34),
    z("brennende Obergeschoss, um Sachen oder Menschen", 110, 426, beim("bgh2", "zweiundzwanzigjährige"), size=34),
    z("zu retten, etwa seinen kleinen Bruder.", 110, 474, beim("bgh2", "etwa"), size=34),
    z("Er bricht im Rauch bewusstlos zusammen und stirbt.", 110, 544, "bgh3", "Bold", 34),
    zit("Sachverhalt: BGHSt 39, 322, Rn. 2 f. (HRRS)", 110, 596, "bgh3"),
    blk(110, 660, 1040, 90, HELLGRUEN, beim("bgh3", "Bundesgerichtshof"),
        [("BGH bestätigt: fahrlässige Tötung (§ 222)", "ExtraBold", 34, INK)]),
    zit("Revision verworfen; Tenor und Rn. 4 f.", 110, 768, beim("bgh3", "Bundesgerichtshof")),
    *requisit([("bgh", ("tabler", "scale", 230, WEISS), "Bundesgerichtshof", WEISS),
               ("bgh2", ("tabler", "building", 230, WAND), "Feier im Wohnhaus", GELB),
               (beim("bgh2", "zweiundzwanzigjährige"), ("tabler", "stairs", 220, WEISS), "ins Obergeschoss", WEISS),
               ("bgh3", ("tabler", "cloud-fog", 250, HELLGRAU), "Rauch", HELLGRAU),
               (beim("bgh3", "Bundesgerichtshof"), ("tabler", "scale", 230, HELLGRUEN), "§ 222 bestätigt", HELLGRUEN)],
              pu=640, py=240),
])

# ===========================================================================================================================
# D A. Siegbert, § 222 StGB (Wortlautkarte): Erfolg, Kausalität, Sorgfaltswidrigkeit und Vorhersehbarkeit
# ===========================================================================================================================
PA = "A. Siegbert, § 222 StGB"
w222, w222_y = wortlaut(80, 170, 1100,
                        "„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis zu "
                        "fünf Jahren oder mit Geldstrafe bestraft.“", "§ 222 StGB", "p222",
                        marken=[("Fahrlässigkeit", beim("p222", "Fahrlässigkeit")), ("verursacht", beim("p222", "verursacht"))],
                        size=34)
folie([("p222", f"{PA} · Wortlaut"), ("erfolg", f"{PA} › 1. Erfolg"), ("kaus", f"{PA} › 2. Kausalität"),
       ("vorh", f"{PA} › 3. Sorgfaltswidrig und vorhersehbar")], [
    *tafel("p222", "A. Fahrlässige Tötung"),
    *w222,
    *okz("1. Erfolg: Arndt ist tot.", w222_y + 40, beim("erfolg", "Arndt"), "Bold", 34),
    z("2. Ohne das Feuer kein Rettungsversuch:", 185, w222_y + 110, "kaus", "Bold", 34),
    *okz("eigener Entschluss unterbricht nicht", w222_y + 162, beim("kaus", "Dass"), size=33, x=230),
    zit("BGHSt 39, 322, Rn. 6", 230, w222_y + 214, beim("kaus", "Dass")),
    *okz("3. Sorgfaltswidrig, Rettungsversuch vorhersehbar", w222_y + 280, "vorh", "Bold", 33),
    zit("BGHSt 39, 322, Rn. 7", 185, w222_y + 332, beim("vorh", "dass")),
    *requisit([("p222", ("tabler", "book", 110, WEISS), "§ 222 StGB", WEISS),
               ("erfolg", ("tabler", "candle", 80, WEISS), "Erfolg", WEISS),
               ("kaus", ("tabler", "link", 110, GELB), "kausal", GELB),
               ("vorh", ("tabler", "eye", 110, BLAUHELL), "vorhersehbar", BLAUHELL)]),
    *stehend("SI", FX, [("p222", "ruhig"), ("erfolg", "feierlich"), ("kaus", "ernst"), ("vorh", "sorge")]),
])
assert w222_y + 380 <= 900, w222_y

# ===========================================================================================================================
# E Problem: eigenverantwortliche Selbstgefährdung (Verweis 058), keine Fremdgefährdung (Verweis 203)
# ===========================================================================================================================
PZ = f"{PA} › 4. Zurechnung"
folie([("problem", f"{PZ}"), ("heroin", f"{PZ} › Selbstgefährdung (Folge 058)"),
       ("retter", f"{PZ} › Der Retter gefährdet sich selbst?"), ("fremd", f"{PZ} › keine Fremdgefährdung (Folge 203)")], [
    *tafel("problem", "Problem: Zurechnung"),
    z("Grundsatz aus dem Heroinspritzen-Fall (Folge 058):", 110, 180, "heroin", "Bold", 34),
    blk(110, 240, 1040, 170, BLAUHELL, beim("heroin", "Wer"),
        [("Wer nur eine eigenverantwortliche", "ExtraBold", 33, INK),
         ("Selbstgefährdung veranlasst oder fördert:", "ExtraBold", 33, INK),
         ("keine Zurechnung", "ExtraBold", 33, INK)]),
    zit("BGHSt 32, 262; BGHSt 59, 150, Rn. 71; BGHSt 39, 322, Rn. 9", 110, 424, beim("heroin", "Wer")),
    z("Arndt kannte die Gefahr und ging trotzdem hinein.", 110, 494, "retter", "Bold", 34),
    blk(110, 560, 1040, 90, GELB, beim("retter", "Also"), [("Also eine Selbstgefährdung?", "ExtraBold", 36, INK)]),
    z("Keine Fremdgefährdung wie beim Rennen (Folge 203):", 110, 700, "fremd", "Bold", 33),
    z("Den Schritt ins Feuer beherrschte Arndt selbst.", 110, 748, beim("fremd", "Den"), size=33),
    *requisit([("problem", ("tabler", "link", 110, WEISS), "Zurechnung?", WEISS),
               ("heroin", ("tabler", "shield-x", 110, BLAUHELL), "Selbstgefährdung", BLAUHELL),
               ("retter", ("tabler", "flame", 100, ROT), "Retter im Feuer", WEISS),
               ("fremd", ("tabler", "walk", 110, GELB), "eigener Schritt", GELB)]),
    *stehend("SI", FX, [("problem", "ruhig"), ("heroin", "denkt"), ("retter", "ernst"), ("fremd", "denkt")]),
])

# ===========================================================================================================================
# F1 BGHSt 39, 322: keine schematische Übertragung, einsichtiges Motiv (Rn. 9 f.)
# ===========================================================================================================================
PR = f"{PZ} › Rechtsprechung: BGHSt 39, 322"
folie([("nein", f"{PR}"), ("schema", f"{PR} › nicht schematisch"), ("motiv", f"{PR} › einsichtiges Motiv")], [
    *tafel("nein", "BGH: Der Brandstifter haftet"),
    z("Die Grundsätze aus dem Heroinfall passen nicht", 110, 180, "schema", "Bold", 34),
    z("schematisch, wenn der Täter durch deliktisches", 110, 228, "schema", "Bold", 34),
    z("Verhalten zur Selbstgefährdung veranlasst.", 110, 276, beim("schema", "Verhalten"), "Bold", 34),
    zit(f"{QB}, Rn. 9", 110, 328, beim("schema", "Verhalten")),
    karte(80, 390, 1100, 330, "motiv", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("„… naheliegende Möglichkeit einer bewussten", 110, 412, "motiv", size=33, rechts=1160),
    z("Selbstgefährdung …, dass er ohne Mitwirkung …", 110, 458, "motiv", size=33, rechts=1160),
    z("des Opfers eine erhebliche Gefahr … begründet", 110, 504, beim("motiv", "Er"), size=33, rechts=1160),
    z("und damit … ein einsichtiges Motiv für", 110, 550, beim("motiv", "einsichtiges"), "Bold", 33, rechts=1160),
    z("gefährliche Rettungsmaßnahmen schafft“", 110, 596, beim("motiv", "einsichtiges"), "Bold", 33, rechts=1160),
    z(f"{QB}, Rn. 10", 110, 652, "motiv", "Bold", 30, farbe=TEXT, rechts=1160),
    *requisit([("nein", ("tabler", "scale", 120, WEISS), "Bundesgerichtshof", WEISS),
               ("schema", ("tabler", "shield-x", 110, BLAUHELL), "nicht schematisch", BLAUHELL),
               ("motiv", ("tabler", "heart-handshake", 120, GELB), "einsichtiges Motiv", GELB)]),
    *stehend("SI", FX, [("nein", "ernst"), ("schema", "denkt"), ("motiv", "sorge")]),
])

# ===========================================================================================================================
# F2 Erfolgsabwendung kommt zugute – Leitsatz 1
# ===========================================================================================================================
folie([("zugute", f"{PR} › Rettung gelingt oder misslingt"), ("leitsatz", f"{PR} › Leitsatz 1")], [
    *tafel("zugute", "Der Gedanke dahinter"),
    *okz("Gelingt die Rettung: kommt dem Täter zugute.", 190, beim("zugute", "Gelingt"), "Bold", 34),
    *neinz("Misslingt sie: Er muss dafür einstehen.", 260, beim("zugute", "Misslingt"), "Bold", 34),
    zit(f"{QB}, Rn. 10", 185, 314, beim("zugute", "Misslingt")),
    blk(110, 400, 1040, 220, BLAUHELL, "leitsatz", [("Leitsatz 1 (allgemein gefasst):", "ExtraBold", 34, INK),
                                                 ("Stirbt ein Dritter bei Rettungshandlungen,", "Regular", 34, INK),
                                                 ("kann das dem Brandstifter als", "Regular", 34, INK),
                                                 ("fahrlässige Tötung zugerechnet werden.", "Regular", 34, INK)]),
    zit("BGHSt 39, 322, Leitsatz 1 (sinngemäß)", 110, 636, beim("leitsatz", "kann")),
    *requisit([("zugute", ("tabler", "scale", 120, WEISS), "Erfolg und Misserfolg", WEISS),
               ("leitsatz", ("tabler", "book", 110, BLAUHELL), "Leitsatz 1", BLAUHELL)]),
    *stehend("LI", FX, [("zugute", "feierlich"), ("leitsatz", "ruhig")]),
])

# ===========================================================================================================================
# G Die Grenze – H Subsumtion: Arndt
# ===========================================================================================================================
folie([("grenze", f"{PR} › Grenze"), ("unvern", f"{PR} › Grenze › echter Fall: nicht unvernünftig")], [
    *tafel("grenze", "Die Grenze"),
    z("Anders mag es bei einem Rettungsversuch sein,", 110, 190, beim("grenze", "Anders"), "Bold", 34),
    *neinz("von vornherein sinnlos", 260, beim("grenze", "sinnlosen"), "ExtraBold", 34),
    *neinz("mit offensichtlich unverhältnismäßigen Wagnissen", 330, beim("grenze", "offensichtlich"), "ExtraBold", 33),
    zit(f"{QB}, Rn. 10", 185, 386, beim("grenze", "offensichtlich")),
    blk(110, 470, 1040, 90, HELLGRUEN, "unvern", [("Echter Fall: nicht offenkundig unvernünftig", "ExtraBold", 34, INK)]),
    *requisit([("grenze", ("tabler", "hand-stop", 110, HELLROT), "Grenze", HELLROT),
               ("unvern", ("tabler", "shield-check", 110, HELLGRUEN), "vernünftig", HELLGRUEN)]),
    *stehend("SI", FX, [("grenze", "denkt"), ("unvern", "ernst")]),
])

folie([("subs", "A. Siegbert › 4. Zurechnung › Arndt: einsichtiges Motiv"), ("sinn", "A. Siegbert › 4. Zurechnung › nicht sinnlos"),
       ("zu222", "A. Siegbert › Ergebnis: § 222 (+)")], [
    *tafel("subs", "Und Arndt?"),
    *okz("Zwei Kinder in Lebensgefahr: einsichtiges Motiv", 190, beim("subs", "Zwei"), "Bold", 34),
    *okz("weder sinnlos noch unvernünftig", 270, "sinn", "Bold", 34),
    z("sogar gelungen", 185, 322, beim("sinn", "sie"), size=34),
    blk(110, 420, 1040, 90, HELLGRUEN, "zu222", [("Tod ist Siegbert zuzurechnen", "ExtraBold", 36, INK)]),
    *plusminus("Fahrlässige Tötung, § 222 StGB", 110, 560, beim("zu222", "Fahrlässige"), True, size=36, stil="ExtraBold"),
    *requisit([("subs", ("tabler", "heart-handshake", 120, GELB), "Kinder retten", GELB),
               ("sinn", ("tabler", "shield-check", 110, HELLGRUEN), "Rettung gelungen", HELLGRUEN),
               ("zu222", ("tabler", "scale", 120, WEISS), "§ 222 (+)", WEISS)]),
    *stehend("LI", FX, [("subs", "sorge"), ("sinn", "feierlich"), ("zu222", "ruhig")]),
])

# ===========================================================================================================================
# I Berufsretter (BGHSt 66, 119)
# ===========================================================================================================================
QB2 = "BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, BGHSt 66, 119"
folie([("beruf", "Rechtsprechung › Berufsretter (2021)"), ("pflicht", "Rechtsprechung › Berufsretter › Rechtspflicht")], [
    *tafel("beruf", "Berufsretter"),
    z("2021: übertragen auf Berufsretter,", 110, 190, "beruf", "Bold", 36),
    z("etwa Feuerwehrleute", 110, 242, beim("beruf", "etwa"), "Bold", 36),
    zit(f"{QB2}, Leitsatz 1", 110, 300, beim("beruf", "etwa")),
    blk(110, 380, 1040, 130, BLAUHELL, "pflicht", [("Statt des einsichtigen Motivs:", "ExtraBold", 34, INK),
                                                ("die Rechtspflicht zum Eingreifen", "Regular", 34, INK)]),
    zit("BGHSt 66, 119, Rn. 27", 110, 526, beim("pflicht", "Rechtspflicht")),
    *requisit([("beruf", ("tabler", "firetruck", 150, ROT), "Feuerwehr", WEISS),
               ("pflicht", ("tabler", "helmet", 110, GELB), "Rechtspflicht", GELB)]),
    *stehend("SI", FX, [("beruf", "ruhig"), ("pflicht", "ernst")]),
])

# ===========================================================================================================================
# J Lehre: drei Ansichten, je ein Satz (Belege über ZJS 2016 und Uni Freiburg; Originale nicht eingesehen)
# ===========================================================================================================================
PL = "Retterfälle in der Lehre"
folie([("lehre", PL), ("l1", f"{PL} › 1. Eigenverantwortlichkeit"), ("l2", f"{PL} › 2. Rettungspflicht / Zwangslage"),
       ("l3", f"{PL} › 3. Risikosphäre des Täters")], [
    *tafel("lehre", "Retterfälle in der Lehre"),
    z("1. Freiwilliger Retter gefährdet sich", 110, 180, "l1", "Bold", 34),
    z("eigenverantwortlich: keine Zurechnung", 150, 228, beim("l1", "die"), size=34),
    zit("Roxin AT I, 4. Aufl., § 11 Rn. 115, 139 (später aufgegeben)", 150, 278, beim("l1", "die")),
    z("2. Zurechnung nur bei Rettungspflicht oder", 110, 346, "l2", "Bold", 34),
    z("notstandsähnlicher Zwangslage", 150, 394, beim("l2", "notstandsähnlichen"), size=34),
    zit("Radtke/Hoffmann GA 2007, 201; Rengier BT II § 40 Rn. 44a f.;", 150, 444, beim("l2", "notstandsähnlichen")),
    zit("Schönke/Schröder/Heine/Bosch § 306c Rn. 6 f.", 150, 478, beim("l2", "notstandsähnlichen")),
    z("3. Zurechnung unabhängig von einer Rettungspflicht:", 110, 546, "l3", "Bold", 34),
    z("Risikosphäre des Erstverursachers", 150, 594, beim("l3", "weil"), size=34),
    zit("Jescheck/Weigend AT § 28 IV 4", 150, 644, beim("l3", "weil")),
    zit("Nachweise nach ZJS 2016, 62 (63 f.); Uni Freiburg, Vorlesung BT, KK 709", 110, 730, "lehre"),
    *requisit([("lehre", ("tabler", "list-check", 110, WEISS), "Lehre", WEISS),
               ("l1", ("tabler", "shield-x", 110, HELLROT), "keine Zurechnung", HELLROT),
               ("l2", ("tabler", "helmet", 110, GELB), "Pflicht oder Zwangslage", GELB),
               ("l3", ("tabler", "flame", 100, ROT), "Risiko des Täters", WEISS)]),
    *stehend("SI", FX, [("lehre", "ruhig"), ("l1", "staunt"), ("l2", "denkt"), ("l3", "ernst")]),
])

# ===========================================================================================================================
# K1 B. § 306c StGB (Wortlautkarte), Grunddelikt, altes und neues Recht
# ===========================================================================================================================
PB = "B. Siegbert, § 306c StGB"
w306c, w306c_y = wortlaut(80, 170, 1100,
                          "„Verursacht der Täter durch eine Brandstiftung nach den §§ 306 bis 306b wenigstens leichtfertig "
                          "den Tod eines anderen Menschen, so ist die Strafe lebenslange Freiheitsstrafe oder Freiheitsstrafe "
                          "nicht unter zehn Jahren.“", "§ 306c StGB", "p306c",
                          marken=[("Brandstiftung", beim("p306c", "Brandstiftung", nr=2)),
                                  ("wenigstens leichtfertig", beim("p306c", "wenigstens")),
                                  ("anderen Menschen", beim("p306c", "anderen"))], size=33)
folie([("p306c", f"{PB} · Wortlaut"), ("grund", f"{PB} › 1. Grunddelikt: § 306a Abs. 1 Nr. 1")], [
    *tafel("p306c", "B. Brandstiftung mit Todesfolge"),
    *w306c,
    *okz("1. Grunddelikt: schwere Brandstiftung, § 306a I Nr. 1", w306c_y + 50, "grund", "Bold", 33),
    z("„ein Gebäude …, die der Wohnung von Menschen dient“", 185, w306c_y + 102, beim("grund", "denn"), size=32),
    z("auch wenn es Siegbert gehört", 185, w306c_y + 150, beim("grund", "auch"), size=32),
    zit("§ 306a Abs. 1 Nr. 1 StGB (Wortlaut gekürzt)", 185, w306c_y + 196, beim("grund", "denn")),
    *requisit([("p306c", ("tabler", "book", 110, WEISS), "§ 306c StGB", WEISS),
               ("grund", ("tabler", "building", 120, WAND), "Wohngebäude", GELB)]),
    *stehend("SI", FX, [("p306c", "ruhig"), ("grund", "ernst")]),
])
assert w306c_y + 240 <= 900, w306c_y

folie([("alt", f"{PB} › 2. Tod des Retters: früheres Recht"), ("heute", f"{PB} › 2. Tod des Retters: heute")], [
    *tafel("alt", "Erfasst § 306c den Retter?"),
    z("Früher (§ 307 Nr. 1 a. F.): Opfer musste sich zur", 110, 190, "alt", "Bold", 34),
    z("Zeit der Tat im Gebäude befinden", 110, 238, beim("alt", "der"), "Bold", 34),
    *neinz("der Retter nicht", 290, beim("alt", "Retter"), size=34),
    zit("BGHSt 39, 322, Rn. 4", 185, 344, beim("alt", "Retter")),
    z("Heute verzichtet § 306c darauf.", 110, 430, "heute", "Bold", 34),
    *okz("h. L.: grundsätzlich auch der Retter", 500, beim("heute", "Nach"), "Bold", 34),
    z("außer bei unvernünftig großem Risiko", 185, 552, beim("heute", "außer"), size=34),
    zit("Lehre: Uni Freiburg, Vorlesung BT, KK 709; ZJS 2016, 62 (63)", 185, 606, beim("heute", "Nach")),
    *requisit([("alt", ("tabler", "calendar", 110, WEISS), "bis 1998", WEISS),
               ("heute", ("tabler", "users", 110, BLAUHELL), "anderer Mensch", BLAUHELL)]),
    *stehend("SI", FX, [("alt", "denkt"), ("heute", "staunt")]),
])


# ===========================================================================================================================
# K2 Wenigstens leichtfertig – sonst § 222
# ===========================================================================================================================
folie([("leicht", f"{PB} › 3. Wenigstens Leichtfertigkeit"), ("leicht2", f"{PB} › Ergebnis: § 306c (+)"),
       ("p222neben", f"{PB} › sonst § 222")], [
    *tafel("leicht", "Wenigstens leichtfertig"),
    z("Leichtfertig: aus besonderem Leichtsinn oder", 110, 190, beim("leicht", "also"), "Bold", 34),
    z("besonderer Gleichgültigkeit", 110, 238, beim("leicht", "besonderer", nr=1), "Bold", 34),
    zit("BGHSt 46, 279, Rn. 24 (zu § 30 BtMG); ZJS 2016, 62 (64)", 110, 290, beim("leicht", "also")),
    *okz("Bewohntes Haus angezündet: Tod drängt sich auf,", 380, "leicht2", "Bold", 33),
    z("auch der Tod von Rettern", 185, 428, beim("leicht2", "auch"), size=33),
    *plusminus("§ 306c StGB", 110, 520, beim("leicht2", "Dann"), True, size=38, stil="ExtraBold"),
    blk(110, 620, 1040, 90, BLAUHELL, "p222neben", [("Ohne Leichtfertigkeit: § 222 StGB", "ExtraBold", 34, INK)]),
    *requisit([("leicht", ("tabler", "alert-triangle", 110, GELB), "leichtfertig", GELB),
               ("leicht2", ("tabler", "flame", 100, ROT), "bewohntes Haus", WEISS),
               ("p222neben", ("tabler", "book", 110, BLAUHELL), "§ 222 StGB", BLAUHELL)]),
    *stehend("SI", FX, [("leicht", "sorge"), ("leicht2", "muede"), ("p222neben", "zu")]),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Standort: objektive Zurechnung"), ("k1", "Klausurtipp › Selbstgefährdung und Streit"),
       ("k2", "Klausurtipp › Motiv und Grenze")], [
    *tafel("tipp", "Klausurtipp: Wo prüfe ich den Retter?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bei der objektiven Zurechnung,", 200, 200, beim("tipp", "objektiven"), "ExtraBold", 35),
    z("bei § 306c im spezifischen Gefahrzusammenhang", 240, 252, beim("tipp", "Paragraf"), size=33),
    linienzug([(130, 320), (1130, 320)], "k1", breite=3),
    z("Eigenverantwortliche Selbstgefährdung prüfen,", 200, 344, "k1", "ExtraBold", 34),
    z("Streit kurz darstellen", 240, 396, beim("k1", "stell"), size=34),
    linienzug([(130, 464), (1130, 464)], "k2", breite=3),
    z("Einsichtiges Motiv?", 200, 488, beim("k2", "Gab"), "ExtraBold", 34),
    z("Rettung nicht offensichtlich unvernünftig?", 200, 540, beim("k2", "war"), "ExtraBold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Siegbert"), ("s1", "Klausurschema › I. § 306a Abs. 1 Nr. 1"),
       ("s2", "Klausurschema › II. § 306c › 1. Tod eines anderen Menschen"), ("s3", "Klausurschema › II. § 306c › 2. Zurechnung"),
       ("s4", "Klausurschema › II. § 306c › 3. Leichtfertigkeit"), ("s5", "Klausurschema › III. § 222")], [
    *tafel("sch", "Klausurschema: Siegbert"),
    *plusminus("I. Schwere Brandstiftung, § 306a I Nr. 1", 110, 180, "s1", True, size=34, stil="ExtraBold"),
    z("II. § 306c StGB", 110, 260, "s2", "ExtraBold", 34),
    z("1. Tod eines anderen Menschen durch die", 150, 320, beim("s2", "der"), "Bold", 33),
    *plusminus("Brandstiftung", 196, 366, beim("s2", "der"), True, size=33, stil="Bold"),
    *plusminus("2. Zurechnung trotz Rettungshandlung", 150, 436, "s3", True, size=33, stil="Bold"),
    *plusminus("3. Wenigstens Leichtfertigkeit", 150, 506, "s4", True, size=33, stil="Bold"),
    z("III. § 222 StGB, falls die Leichtfertigkeit fehlt", 110, 600, "s5", "ExtraBold", 34),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Nach dem BGH wird dem Brandstifter auch der", 0)],
                 [("Tod des Retters", "a"), (" zugerechnet, wenn er ein", 0)],
                 [("einsichtiges Motiv", "b"), (" zur Rettung geschaffen hat.", 0)]], 750, 290, 40, "merke",
                {"a": beim("merke", "Tod"), "b": beim("merke", "einsichtiges")}),
    *markertext([[("Anders kann es nur bei einem ", 0), ("sinnlosen", "c")],
                 [("oder offensichtlich unverhältnismäßigen", 0)],
                 [("Rettungsversuch sein.", 0)]], 750, 560, 40, "m2",
                {"c": beim("m2", "sinnlosen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
