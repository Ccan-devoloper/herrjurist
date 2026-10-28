"""Folge 216 · Beweiswürdigung Revision: Lücken, Widersprüche, in dubio pro reo – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung zu 60 Tagessätzen; er soll seine Kollegin
Frau Bremer in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben (Aussage gegen Aussage). Laut Urteil schilderte
sie den Vorfall 3-mal verschieden; das Urteil nennt die Aussage „konstant“ und erörtert die Abweichungen nicht; Zweifel habe
das Gericht nicht. Rechtsanwalt Wegmann prüft die Revision.
Szenen laut ../SZENENPLAN.md: A1 Kanzlei, A2 Rückblick Paketlager (3 Schilderungen), A3 Rückblick Amtsgericht, A4 Kanzlei,
B Sachverhalt, C1 Wortlautkarte § 261, C2 nur Rechtsfehler, D1/D2 Aussage gegen Aussage, E1 Fall: Lücke und Widerspruch,
E2 Ergebnis (§§ 337, 353, 354), F1 in dubio pro reo, F2 Wortlautkarte Art. 6 Abs. 2 EMRK, G Klausurtipp (Lexi), H Prüfschema,
I Merksatz (Lexi).
Ein Handlungsgeräusch (Karton wird im Lager abgestellt; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie
im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 204
(gemeinsame Dateien unverändert); neu: schreibtisch(), urkunde(), hochregal(), richtertisch().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 06.10.2026), Art. 6 Abs. 2 EMRK
nach der deutschen Übersetzung des EGMR (Quelle auf der Karte genannt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_216/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_216/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe;
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); das lange Schild
    „Rechtsanwalt Wegmann“ in 26 px, damit es neben der zweiten Figur Platz hat."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if text.startswith("Rechtsanw") else 30, anker="m", **k)


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
GRAU = (190, 190, 186, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))




KRAFT = (214, 172, 120, 255)                 # Kartonfarbe (Paketlager)
METALL = (120, 140, 170, 255)                # Regalstützen


def schreibtisch(c, x0=110, w=360):
    """Schreibtisch der Kanzlei (Grundform): Platte, Schubladenblock, Bein; Lampe aus Tabler."""
    h = 215
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, 34 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.rectangle((22 * s, 34 * s, 150 * s, (h - 3) * s), fill=HOLZ, outline=INK, width=5 * s)
        for yy in (80, 145):
            dr.line((22 * s, yy * s, 150 * s, yy * s), fill=INK, width=4 * s)
            dr.rounded_rectangle((70 * s, (yy - 30) * s, 102 * s, (yy - 22) * s), 3 * s, fill=INK)
        dr.rectangle(((w - 46) * s, 34 * s, (w - 22) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=5 * s)
    return [hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch")),
            hart(ficon("tabler", "lamp", x0 + w - 90, BODEN_Y - h + 4, 120, c, fuell=GELB))]


UX, UY, UW, UH = 500, 340, 560, 535           # Urteilsurkunde (vergrößertes Blatt) in der Kanzlei


def urkunde(c, anim="pop"):
    """Das schriftliche Urteil als großes Blatt (Grundform); Inhalt wird zum gesprochenen Wort eingetragen."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (UW - 3) * s, (UH - 3) * s), 12 * s, fill=WEISS, outline=INK, width=5 * s)
        dr.line((36 * s, 86 * s, (UW - 36) * s, 86 * s), fill=(215, 215, 210, 255), width=5 * s)
    e = El(_flaeche(UW, UH, zz), UX, UY, c, anim, 0.0, None, name="urkunde")
    return [e, z("Urteil", UX + 36, UY + 22, c, "ExtraBold", 44, rechts=UX + UW)]


def hochregal(c, x0=1110, w=750):
    """Hochregal im Paketlager (Grundform): Stützen, drei Böden, Kartons mit Klebeband."""
    h = 525
    def zz(dr, s):
        for xs in (0, w // 2 - 7, w - 16):
            dr.rectangle((xs * s, 0, (xs + 16) * s, h * s), fill=METALL, outline=INK, width=4 * s)
        for yb in (150, 320, 490):
            dr.rectangle((0, yb * s, w * s, (yb + 18) * s), fill=GELB, outline=INK, width=4 * s)
        kartons = [(30, 60, 150, 90), (200, 80, 120, 70), (390, 40, 170, 110), (590, 70, 120, 80),
                   (40, 220, 130, 100), (230, 250, 110, 70), (410, 210, 150, 110), (600, 240, 110, 80)]
        for kx, ky, kw, kh in kartons:
            dr.rectangle((kx * s, ky * s, (kx + kw) * s, (ky + kh) * s), fill=KRAFT, outline=INK, width=4 * s)
            dr.line(((kx + kw // 2) * s, ky * s, (kx + kw // 2) * s, (ky + kh) * s), fill=(176, 130, 80, 255), width=6 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="hochregal"))


def richtertisch(c, x0=110, w=760):
    """Richtertisch im Sitzungssaal (Grundform) mit Akte; ohne Hoheitszeichen."""
    h = 265
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, 40 * s), 6 * s, fill=HOLZD, outline=INK, width=5 * s)
        dr.rectangle((20 * s, 40 * s, (w - 20) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=5 * s)
        for xx in range(20, w - 20, 145):
            dr.line((xx * s, 40 * s, xx * s, (h - 3) * s), fill=HOLZD, width=4 * s)
    return [hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="richtertisch")),
            hart(ficon("tabler", "folders", x0 + 150, BODEN_Y - h + 6, 130, c, fuell=WEISS))]


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KE": "Herr Kerber", "BR": "Frau Bremer", "WG": "Rechtsanwalt Wegmann", "RI": "Richterin"}
NFARBE = {"KE": GRUEN, "BR": LILA, "WG": BLAU, "RI": WEISS}


def stehend(k, x, folge, unten=930, hoehe=480, erst="pop"):
    """erst="cut": Figur steht beim Folienstart sofort (z. B. wenn sie gleich zu sprechen beginnt)."""
    return [*fig(k, x, unten, hoehe, folge, erst=erst), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


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


def zwei(folge_wg, folge_ke):
    """Rechtsanwalt Wegmann und Herr Kerber rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("WG", X1, folge_wg), *stehend("KE", X2, folge_ke)]


def allein(k, folge):
    return stehend(k, FX, folge)


def tafelicon(e):
    """Icon als Teil der Tafel bzw. Fallkarte, bewusst links: von rechts_frei() ausgenommen."""
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


# ===========================================================================================================================
# A1 Fall: in der Kanzlei – das Urteil des Amtsgerichts
# ===========================================================================================================================
HX, KX = 1240, 1650                          # Rechtsanwalt Wegmann (blickt nach rechts), Herr Kerber (blickt nach links)
folie([(NULL, "Fall · In der Kanzlei"), ("urteil", "Fall · Das Urteil des Amtsgerichts"), ("lager", "Fall · Der Vorwurf"),
       ("aga", "Fall · Aussage gegen Aussage"), ("k1", "Fall · Herr Kerber bestreitet")], [
    boden(NULL),
    *schreibtisch(NULL),
    hart(pl("Kanzlei Wegmann", 70, 30, NULL, fill=BLAU, size=38)),
    *urkunde(beim("fall", "Urteil")),
    pl("Amtsgericht: Körperverletzung, § 223 StGB", 70, 110, beim("urteil", "Körperverletzung"), fill=WEISS, size=34),
    pl("Geldstrafe: 60 Tagessätze", 70, 190, beim("urteil", "sechzig"), fill=HELLROT, size=34),
    z("Paketlager, Spätschicht", UX + 36, UY + 110, beim("lager", "Spätschicht"), size=32, rechts=UX + UW - 10),
    z("Vorwurf: Stoß gegen ein Regal", UX + 36, UY + 160, beim("lager", "Regal"), "Bold", 32, rechts=UX + UW - 10),
    z("Zeugen: keine", UX + 36, UY + 240, beim("aga", "Zeugen"), "Bold", 32, rechts=UX + UW - 10),
    blk(UX + 30, UY + 300, UW - 60, 80, GELB, beim("aga", "Aussage"), [("Aussage gegen Aussage", "ExtraBold", 32, INK)]),
    tafelicon(ficon("tabler", "messages", UX + UW // 2, UY + 490, 90, beim("aga", "Aussage"), fuell=WEISS)),
    *stehend("WG", HX, [(NULL, "ruhig_r"), (beim("fall", "Urteil"), "ernst_r")], unten=BODEN_Y),
    *stehend("KE", KX, [(NULL, "ruhig"), (beim("urteil", "sechzig"), "sorge")], unten=BODEN_Y),
    *redet("KE_redet", KX, BODEN_Y, FHA, "k1", "drei"),
    blase("sprech", 620, 160, "k1", 1470, 250, inhalt=["Ich habe sie nicht angefasst."], textsize=36,
          figur=("KE_redet", KX, BODEN_Y, FHA), bis="drei"),
])

# ===========================================================================================================================
# A2 Fall: Rückblick – die drei Schilderungen der Zeugin (laut Urteilsgründen)
# ===========================================================================================================================
BX = 1560                                    # Frau Bremer (blickt nach links zu den Karten)
KART = [("v1", "b1", "1. Schichtleiterin · am selben Abend", "„gegen das Regal gestoßen“", "Regal", "building-warehouse"),
        ("v2", "b2", "2. Polizei · 2 Wochen später", "„mit der Faust auf den Arm geschlagen“", "Faust", "shield"),
        ("v3", "b3", "3. Hauptverhandlung", "„am Arm gepackt, zur Seite gerissen“", "gepackt", "scale")]
els_a2 = [hochregal("drei"), boden("drei"),
          hart(pl("Rückblick: 3 Schilderungen", 70, 30, "drei", fill=GELB, size=38)),
          szene(ficon("tabler", "package", 1000, BODEN_Y + 4, 150, beim("drei", "Vorfall"), fuell=KRAFT), "216karton*", 0.8, -0.05)]
for i, (cv, cb, titel_, zitat, wort, ic) in enumerate(KART):
    y = 130 + i * 175
    els_a2 += [karte(70, y, 900, 150, cv, fill=WEISS, rund=18, schatten=6, rand=4),
               tafelicon(ficon("tabler", ic, 150, y + 118, 84, cv, fuell=HELL)),
               z(titel_, 225, y + 22, cv, "Bold", 32, rechts=955),
               z(zitat, 225, y + 82, beim(cb, wort), "ExtraBold", 32, rechts=955)]
els_a2 += [pl("Attest: Bluterguss am Oberarm", 70, 670, beim("attest", "Attest"), fill=HELLROT, size=34),
           tafelicon(ficon("tabler", "report-medical", 680, 735, 90, beim("attest", "Attest"), fuell=WEISS)),
           *stehend("BR", BX, [("drei", "ruhig"), ("v1", "ernst"), ("attest", "still")], unten=BODEN_Y)]
for cb, nxt, zeilen in [("b1", "v2", ["Er hat mich gegen", "das Regal gestoßen."]),
                        ("b2", "v3", ["Er hat mir mit der Faust", "auf den Arm geschlagen."]),
                        ("b3", "attest", ["Er hat mich am Arm gepackt", "und zur Seite gerissen."])]:
    els_a2 += [*redet("BR_redet", BX, BODEN_Y, FHA, cb, nxt),
               blase("sprech", 640, 180, cb, 1360, 245, inhalt=zeilen, textsize=34, figur=("BR_redet", BX, BODEN_Y, FHA), bis=nxt)]
folie([("drei", "Fall · Rückblick: 3 Schilderungen"), ("v1", "Fall · 1. Schilderung: Schichtleiterin"),
       ("v2", "Fall · 2. Schilderung: Polizei"), ("v3", "Fall · 3. Schilderung: Hauptverhandlung"),
       ("attest", "Fall · Das Attest")], els_a2)

# ===========================================================================================================================
# A3 Fall: Rückblick – die Urteilsverkündung
# ===========================================================================================================================
RX, KX3 = 1260, 1680                         # Richterin (blickt nach rechts), Herr Kerber (blickt nach links)
folie([("saal", "Fall · Rückblick: das Urteil"), ("r1", "Fall · „konstant und glaubhaft“")], [
    boden("saal"),
    *richtertisch("saal"),
    hart(pl("Rückblick: Amtsgericht", 70, 30, "saal", fill=GELB, size=38)),
    pl("Die Richterin folgt der Zeugin.", 70, 110, beim("saal", "folgt"), fill=WEISS, size=34),
    *stehend("RI", RX, [("saal", "ernst_r")], unten=BODEN_Y),
    *stehend("KE", KX3, [("saal", "sorge")], unten=BODEN_Y),
    *redet("RI_redet_r", RX, BODEN_Y, FHA, "r1", "w1"),
    blase("sprech", 880, 230, "r1", 680, 300, inhalt=["Die Zeugin hat den Vorfall konstant", "und glaubhaft geschildert.",
          "Zweifel hat das Gericht nicht."], textsize=34, figur=("RI_redet_r", RX, BODEN_Y, FHA), bis="w1"),
])

# ===========================================================================================================================
# A4 Fall: zurück in der Kanzlei – was steht im Urteil?
# ===========================================================================================================================
UL = [("1. Stoß gegen das Regal", "Dreimal"), ("2. Faustschlag auf den Arm", "Dreimal"), ("3. am Arm gepackt", "Dreimal")]
els_a4 = [boden("w1"), *schreibtisch("w1"),
          hart(pl("Kanzlei Wegmann", 70, 30, "w1", fill=BLAU, size=38)),
          *[hart(e) for e in urkunde("w1", anim="cut")],
          z("Schilderungen der Zeugin:", UX + 36, UY + 105, beim("w1", "Dreimal"), "Bold", 30, rechts=UX + UW - 10)]
for i, (t, w) in enumerate(UL):
    els_a4.append(z(t, UX + 56, UY + 155 + i * 48, beim("w1", w), size=30, rechts=UX + UW - 10))
els_a4 += [z("Würdigung: „konstant“ ?", UX + 36, UY + 320, beim("w1", "konstant"), "ExtraBold", 32, farbe=DROT, rechts=UX + UW - 10),
           z("Abweichungen: kein Wort", UX + 36, UY + 375, beim("w1", "kein"), "Bold", 30, farbe=DROT, rechts=UX + UW - 10),
           z("„Zweifel hat das Gericht nicht.“", UX + 36, UY + 445, beim("k2", "Zweifel"), "Bold", 28, rechts=UX + UW - 10),
           *stehend("WG", HX, [("w1", "ernst_r"), ("k2", "skeptisch_r"), ("frage", "ruhig_r")], unten=BODEN_Y, erst="cut"),
           *redet("WG_redet_r", HX, BODEN_Y, FHA, "w1", "k2"),
           blase("sprech", 740, 200, "w1", 1370, 235, inhalt=["3-mal anders geschildert,", "und das soll konstant sein?",
                 "Dazu steht im Urteil kein Wort."], textsize=32, figur=("WG_redet_r", HX, BODEN_Y, FHA), bis="k2"),
           *stehend("KE", KX, [("w1", "sorge"), ("frage", "skeptisch")], unten=BODEN_Y, erst="cut"),
           *redet("KE_redet2", KX, BODEN_Y, FHA, "k2", "frage"),
           blase("sprech", 700, 180, "k2", 1430, 245, inhalt=["Dann gilt doch: Im Zweifel", "für den Angeklagten!"], textsize=34,
                 figur=("KE_redet2", KX, BODEN_Y, FHA), bis="frage"),
           pl("Beweiswürdigung mit der Revision angreifbar?", 70, 110, "frage", fill=PINK, size=34),
           pl("Hilft „in dubio pro reo“?", 70, 190, "frage2", fill=PINK, size=34)]
folie([("w1", "Fall · Was steht im Urteil?"), (beim("w1", "konstant"), "Fall · „konstant“?"),
       ("k2", "Fall · „Im Zweifel für den Angeklagten“"), ("frage", "Fall · Die Fragen")], els_a4)


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_216(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_216("sv", [
    "Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung zu einer Geldstrafe von 60 Tagessätzen. Er soll seine "
    "Kollegin Frau Bremer in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben. Zeugen gab es nicht; Herr "
    "Kerber bestreitet die Tat. Ein Attest belegt einen Bluterguss am Oberarm.",
    "Laut den Urteilsgründen schilderte Frau Bremer den Vorfall 3-mal: der Schichtleiterin am selben Abend als Stoß gegen "
    "das Regal, 2 Wochen später der Polizei als Faustschlag auf den Arm, in der Hauptverhandlung so, dass er sie am Arm "
    "gepackt und zur Seite gerissen habe. Das Urteil nennt ihre Aussage konstant und glaubhaft, ohne auf die Abweichungen "
    "einzugehen. Zweifel habe das Gericht nicht.",
    "Rechtsanwalt Wegmann hat rechtzeitig Sprungrevision eingelegt und die Verletzung materiellen Rechts gerügt.",
], "Ist die Beweiswürdigung revisibel – und ist „in dubio pro reo“ verletzt?")

# ===========================================================================================================================
# C1 § 261 StPO: freie Überzeugung – Sache des Tatgerichts
# ===========================================================================================================================
PB = "Beweiswürdigung"
W261 = ["„Über das Ergebnis der Beweisaufnahme entscheidet das Gericht",
        "nach seiner freien, aus dem Inbegriff der Verhandlung",
        "geschöpften Überzeugung.“"]
w261, w261_y = wortlaut(80, 180, 1100, W261, "§ 261 StPO", "p261", marken=[
    (1, "freien", beim("p261", "freien")), (1, "Inbegriff der Verhandlung", beim("p261", "Inbegriff")),
    (2, "Überzeugung", beim("p261", "Überzeugung"))], size=32)
folie([("p261", f"{PB} · § 261 StPO"), (beim("p261", "freien"), f"{PB} › freie Überzeugung"),
       ("sache", f"{PB} › Sache des Tatgerichts")], rechts_frei([
    *tafel("p261", "Beweiswürdigung: § 261 StPO"),
    *w261,
    blk(110, w261_y + 45, 1040, 90, GELB, beim("sache", "Sache"), [("Beweiswürdigung: Sache des Tatgerichts", "ExtraBold", 36, INK)]),
    zit("BGH, Beschl. v. 26.6.2024 – 1 StR 176/24, Rn. 7", 110, w261_y + 155, beim("sache", "Sache")),
    *requisit([("p261", ("tabler", "brain", 110, WEISS), "freie Überzeugung", WEISS),
               ("sache", ("tabler", "gavel", 100, GELB), "Tatgericht", GELB)]),
    *zwei([("p261", "ruhig"), ("sache", "ernst")], [("p261", "ruhig"), ("sache", "skeptisch")]),
]))

# ===========================================================================================================================
# C2 Revisionsgericht: nur Rechtsfehler
# ===========================================================================================================================
PR = "Revision"
RF = [("l1", "lückenhaft"), ("l2", "widersprüchlich"), ("l3", "unklar"), ("l4", "gegen Denkgesetze oder Erfahrungssätze"),
      ("l5", "überspannte Anforderungen an die Gewissheit")]
els_c2 = [*tafel("nurrf", "Revision: nur Rechtsfehler"),
          z("Rechtsfehler, wenn die Würdigung …", 110, 180, "nurrf", "Bold", 36)]
for i, (c, t) in enumerate(RF):
    els_c2.append(z(f"– {t}", 150, 245 + i * 56, c, size=34))
els_c2 += [zit("BGH, Urt. v. 19.3.2025 – 6 StR 543/24, Rn. 16", 150, 530, "l5"),
           blk(110, 610, 1040, 110, BLAU, "sachr", [("Fehler ergeben sich aus dem Urteil selbst:", "ExtraBold", 32, INK),
                                                     ("die allgemeine Sachrüge genügt", "ExtraBold", 32, INK)]),
           zit("eigene Folge: „Sachrüge StPO“", 110, 745, beim("sachr", "eigene")),
           *requisit([("nurrf", ("tabler", "zoom-question", 100, WEISS), "nur Rechtsfehler", WEISS),
                      ("l1", ("tabler", "puzzle-off", 100, HELLROT), "Lücke", HELLROT),
                      ("l2", ("tabler", "arrows-split", 100, HELLROT), "Widerspruch", HELLROT),
                      ("l4", ("tabler", "brain", 100, WEISS), "Denkgesetze", WEISS),
                      ("sachr", ("tabler", "file-text", 100, BLAU), "Sachrüge", BLAU)]),
           *allein("WG", [("nurrf", "ruhig"), ("l1", "ernst"), ("sachr", "froh")])]
folie([("nurrf", f"{PR} › nur Rechtsfehler"), ("l1", f"{PR} › lückenhaft"), ("l2", f"{PR} › widersprüchlich"),
       ("l3", f"{PR} › unklar"), ("l4", f"{PR} › Denkgesetze, Erfahrungssätze"), ("l5", f"{PR} › überspannte Anforderungen"),
       ("sachr", f"{PR} › allgemeine Sachrüge genügt")], rechts_frei(els_c2))

# ===========================================================================================================================
# D1 Aussage gegen Aussage: Gesamtschau
# ===========================================================================================================================
PA = "Aussage gegen Aussage"
KRIT = [(beim("krit", "Entstehung"), "Entstehung", 110, 640, GELB), ("motiv", "Motive", 465, 640, BLAU),
        ("konst", "Konstanz", 820, 640, GRUEN), ("det", "Detailreichtum", 110, 740, LILA),
        (beim("det", "Plausibilität"), "Plausibilität", 465, 740, HELLGRUEN)]
els_d1 = [*tafel("aga2", "Aussage gegen Aussage"),
          *okz("Verurteilung auf 1 Belastungszeugin möglich,", 175, beim("aga2", "einzige"), "Bold", 32, x=160),
          z("wenn das Gericht von ihrer Aussage überzeugt ist", 160, 222, beim("aga2", "überzeugt"), "Bold", 32),
          zit("BGH, Urt. v. 25.4.2018 – 2 StR 194/17, Rn. 10", 160, 268, beim("aga2", "überzeugt")),
          blk(110, 325, 1040, 80, GELB, "sorgf", [("besonders sorgfältige Würdigung", "ExtraBold", 34, INK)]),
          z("Urteilsgründe: alle Umstände für und gegen den", 110, 440, "gesamt", "Bold", 32),
          z("Angeklagten erkannt und in einer Gesamtschau gewürdigt", 110, 486, beim("gesamt", "Gesamtschau"), "Bold", 32),
          zit("BGH, Beschl. v. 17.12.2025 – 6 StR 260/25, Rn. 5", 110, 532, beim("gesamt", "Gesamtschau")),
          z("Dazu gehören:", 110, 585, "krit", "Bold", 30)]
for c, t, x, y, f in KRIT:
    els_d1.append(blk(x, y, 330, 80, f, c, [(t, "ExtraBold", 30, INK)]))
els_d1 += [*requisit([("aga2", ("tabler", "messages", 110, WEISS), "Aussage gegen Aussage", WEISS),
                      ("sorgf", ("tabler", "search", 100, GELB), "besonders sorgfältig", GELB),
                      ("krit", ("tabler", "list-check", 100, WEISS), "Kriterien", WEISS)]),
           *allein("BR", [("aga2", "ruhig"), ("sorgf", "ernst")])]
folie([("aga2", f"{PA} · eine Belastungszeugin"), ("sorgf", f"{PA} › besonders sorgfältige Würdigung"),
       ("gesamt", f"{PA} › Gesamtschau aller Umstände"), ("krit", f"{PA} › Entstehung, Motive, Konstanz, Details")],
      rechts_frei(els_d1))

# ===========================================================================================================================
# D2 Aussage gegen Aussage: frühere Angaben, Abweichungen
# ===========================================================================================================================
folie([("frueh", f"{PA} › frühere Angaben mitteilen"), ("abw", f"{PA} › Abweichungen gewichtet?"),
       ("nicht", f"{PA} › Abweichung: nicht automatisch unglaubhaft"), ("erkl", f"{PA} › erkennen und erklären")], rechts_frei([
    *tafel("frueh", "Frühere Angaben der Zeugin"),
    blk(110, 180, 1040, 80, GELB, beim("frueh", "frühere"), [("Urteil teilt auch frühere Angaben mit", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 29.4.2025 – 6 StR 105/25, Rn. 6", 110, 278, beim("frueh", "frühere")),
    z("Nur so prüfbar: Hat das Gericht Abweichungen", 110, 345, "abw", "Bold", 34),
    z("gesehen und richtig gewichtet?", 110, 395, beim("abw", "gewichtet"), "Bold", 34),
    linienzug([(110, 470), (1150, 470)], "nicht", breite=3),
    z("Abweichung: nicht automatisch unglaubhaft", 110, 500, "nicht", "Bold", 34),
    blk(110, 575, 1040, 80, BLAU, "erkl", [("aber: erkennen und erklären", "ExtraBold", 34, INK)]),
    zit("vgl. BGH, Urt. v. 25.4.2018 – 2 StR 194/17, Rn. 12", 110, 673, beim("erkl", "erklären")),
    *requisit([("frueh", ("tabler", "file-description", 100, WEISS), "frühere Angaben", WEISS),
               ("abw", ("tabler", "scale", 100, WEISS), "Abweichungen", WEISS),
               ("erkl", ("tabler", "message-2", 100, BLAU), "erklären", BLAU)]),
    *allein("WG", [("frueh", "ruhig"), ("abw", "ernst"), ("erkl", "skeptisch")]),
]))

# ===========================================================================================================================
# E1 Der Fall: Lücke und Widerspruch
# ===========================================================================================================================
PF = "Fall"
SCH = [("s1", "1. Stoß gegen das Regal"), ("s2", "2. Faustschlag"), ("s3", "3. am Arm gepackt")]
els_e1 = [*tafel("fall2", "Der Fall: das Urteil"),
          z("Herr Kerber · das Urteil teilt mit:", 110, 175, "fall2", "Bold", 34),
          z("3 Schilderungen der Zeugin", 110, 222, "drei2", "ExtraBold", 34)]
for i, (c, t) in enumerate(SCH):
    els_e1.append(z(t, 150, 280 + i * 50, c, size=34))
els_e1 += [z("Würdigung: „konstant“", 110, 450, "konst2", "ExtraBold", 36),
           z("Abweichungen: mit keinem Wort erörtert", 110, 505, beim("kwort", "keinem"), "Bold", 34, farbe=DROT),
           *neinz("lückenhaft", 585, "luecke", "ExtraBold", 36, x=160),
           *neinz("widersprüchlich: „konstant“ trotz 3 Tatbildern", 650, beim("wid", "widersprüchlich"), "ExtraBold", 34, x=160),
           zit("vgl. BGH, Beschl. v. 29.4.2025 – 6 StR 105/25, Rn. 9, 12", 160, 705, beim("wid", "widersprüchlich")),
           *requisit([("fall2", ("tabler", "file-text", 100, WEISS), "Urteil", WEISS),
                      ("drei2", ("tabler", "messages", 100, WEISS), "3 Schilderungen", WEISS),
                      ("luecke", ("tabler", "puzzle-off", 100, HELLROT), "Lücke", HELLROT),
                      ("wid", ("tabler", "arrows-split", 100, HELLROT), "Widerspruch", HELLROT)]),
           *zwei([("fall2", "ruhig"), ("konst2", "skeptisch"), ("luecke", "ernst")], [("fall2", "sorge"), ("wid", "skeptisch")])]
folie([("fall2", f"{PF} › die Beweiswürdigung im Urteil"), ("drei2", f"{PF} › 3 Schilderungen im Urteil"),
       ("konst2", f"{PF} › „konstant“ – ohne Erörterung"), ("luecke", f"{PF} › lückenhaft (-)"),
       ("wid", f"{PF} › widersprüchlich (-)")], rechts_frei(els_e1))

# ===========================================================================================================================
# E2 Ergebnis: Beruhen, Aufhebung, Zurückverweisung
# ===========================================================================================================================
PE = "Ergebnis"
folie([("beruh", f"{PE} › Beruhen, § 337 Abs. 1 StPO"), ("aufh", f"{PE} › Aufhebung, § 353 StPO"),
       ("zur", f"{PE} › Zurückverweisung, § 354 Abs. 2 StPO"), ("frei", f"{PE} › kein Freispruch durch das Revisionsgericht")],
      rechts_frei([
    *tafel("beruh", "Ergebnis der Revision"),
    *okz("Beruhen: anderes Ergebnis nicht auszuschließen", 180, beim("beruh", "nicht"), "Bold", 32, x=160),
    zit("BGH, Beschl. v. 18.6.2024 – 2 StR 205/24, Rn. 21", 160, 228, beim("beruh", "nicht")),
    blk(110, 300, 1040, 80, GELB, "aufh", [("Aufhebung mit den Feststellungen, § 353 StPO", "ExtraBold", 34, INK)]),
    blk(110, 410, 1040, 110, BLAU, "zur", [("Zurückverweisung an eine andere Abteilung", "ExtraBold", 34, INK),
                                           ("des Amtsgerichts, § 354 Abs. 2 StPO", "ExtraBold", 34, INK)]),
    *neinz("selbst freisprechen: nein – neue Würdigung nötig", 575, beim("frei", "freisprechen"), "Bold", 32, x=160),
    zit("vgl. § 354 Abs. 1 StPO", 160, 623, beim("frei", "freisprechen")),
    *requisit([("beruh", ("tabler", "link", 100, BLAU), "Beruhen (+)", BLAU),
               ("aufh", ("tabler", "file-x", 100, GELB), "aufgehoben", GELB),
               ("zur", ("tabler", "arrow-back-up", 100, BLAU), "neue Verhandlung", BLAU),
               ("frei", ("tabler", "hand-stop", 100, HELLROT), "kein Freispruch", HELLROT)]),
    *zwei([("beruh", "ruhig"), ("aufh", "froh")], [("beruh", "skeptisch"), ("aufh", "froh"), ("frei", "ruhig")]),
]))

# ===========================================================================================================================
# F1 In dubio pro reo: Entscheidungsregel
# ===========================================================================================================================
PI = "in dubio pro reo"
folie([("idpr", PI), ("regel", f"{PI} › Entscheidungsregel"), ("erst", f"{PI} › erst nach der Beweiswürdigung"),
       ("verl", f"{PI} › verletzt nur bei Zweifeln"), ("hier", f"{PI} › hier: keine Zweifel – nicht verletzt"),
       ("muss", f"{PI} › Fehler: die Beweiswürdigung")], rechts_frei([
    *tafel("idpr", "In dubio pro reo"),
    z("„Im Zweifel für den Angeklagten“ – zu früh gerufen", 110, 170, beim("idpr", "früh"), "Bold", 32),
    blk(110, 230, 505, 80, HELLROT, beim("regel", "Beweisregel"), [("keine Beweisregel", "ExtraBold", 32, INK)]),
    blk(645, 230, 505, 80, HELLGRUEN, beim("regel", "Entscheidungsregel"), [("sondern Entscheidungsregel", "ExtraBold", 30, INK)]),
    z("greift erst nach abgeschlossener Beweiswürdigung,", 110, 345, "erst", "Bold", 32),
    z("wenn das Gericht nicht voll überzeugt ist", 110, 391, beim("erst", "nicht"), "Bold", 32),
    zit("BGH, Urt. v. 24.9.2025 – 2 StR 128/25, Rn. 31", 110, 435, beim("erst", "nicht")),
    blk(110, 490, 1040, 80, GELB, "verl", [("verletzt nur: Zweifel gehabt – und trotzdem verurteilt", "ExtraBold", 32, INK)]),
    karte(110, 605, 1040, 70, "hier", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("Urteil: „Zweifel hat das Gericht nicht.“", 140, 616, "hier", "Bold", 32, rechts=1140),
    *neinz("Zweifelssatz nicht verletzt", 700, beim("hier", "keine"), "ExtraBold", 34, x=160),
    z("„Hätte zweifeln müssen?“ – Frage der Beweiswürdigung", 110, 775, beim("muss", "Beweiswürdigung"), "Bold", 32),
    *requisit([("idpr", ("tabler", "help", 100, WEISS), "in dubio pro reo", WEISS),
               ("regel", ("tabler", "list-check", 100, HELLGRUEN), "Entscheidungsregel", HELLGRUEN),
               ("hier", ("tabler", "file-text", 100, ZITAT), "„keine Zweifel“", WEISS),
               ("muss", ("tabler", "zoom-question", 100, HELLROT), "Fehler: Würdigung", HELLROT)]),
    *allein("KE", [("idpr", "skeptisch"), ("regel", "ernst"), ("hier", "sorge"), ("muss", "ruhig")]),
]))

# ===========================================================================================================================
# F2 Unschuldsvermutung: Art. 6 Abs. 2 EMRK (Wortlautkarte, deutsche Übersetzung des EGMR)
# ===========================================================================================================================
W6 = ["„Jede Person, die einer Straftat angeklagt ist, gilt bis",
      "zum gesetzlichen Beweis ihrer Schuld als unschuldig.“"]
w6, w6_y = wortlaut(80, 260, 1100, W6, "Art. 6 Abs. 2 EMRK (deutsche Übersetzung des EGMR)", "emrk", marken=[
    (1, "gesetzlichen Beweis ihrer Schuld", beim("emrk", "gesetzlichen")), (1, "unschuldig", beim("emrk", "unschuldig"))], size=34)
folie([("emrk", f"{PI} › Unschuldsvermutung, Art. 6 Abs. 2 EMRK")], rechts_frei([
    *tafel("emrk", "Die Unschuldsvermutung"),
    z("Eng verwandt mit in dubio pro reo:", 110, 180, "emrk", "Bold", 34),
    *w6,
    *requisit([("emrk", ("tabler", "shield-check", 110, HELLGRUEN), "Unschuldsvermutung", HELLGRUEN)]),
    *zwei([("emrk", "ernst")], [("emrk", "ruhig")]),
]))

# ===========================================================================================================================
# G Klausurtipp (Lexi): Revisionsbegründung
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · die Revisionsbegründung"), ("t1", "Klausurtipp · 1. Sachrüge ausführen"),
       ("t2", "Klausurtipp · 2. eng am Urteil formulieren"), ("t3", "Klausurtipp · 3. Zweifelssatz nur bei Zweifeln")], [
    *tafel("tipp", "Klausurtipp: Revisionsbegründung", fill=HELL),
    warnung_i(150, 205, "tipp", gr=24),
    z("1. Allgemeine Sachrüge erheben und ausführen:", 200, 180, "t1", "Bold", 32),
    z("Beweiswürdigung lückenhaft und widersprüchlich", 200, 226, beim("t1", "lückenhaft"), "ExtraBold", 32),
    z("2. Eng am Urteil formulieren:", 200, 305, "t2", "Bold", 32),
    z("„Das Urteil teilt 3 unterschiedliche Schilderungen", 200, 351, beim("t2", "Das"), size=30),
    z("der Zeugin mit, nennt ihre Aussage aber konstant,", 200, 393, beim("t2", "nennt"), size=30),
    z("ohne die Abweichungen zu erörtern.“", 200, 435, beim("t2", "ohne"), size=30),
    blk(130, 520, 1020, 110, HELLGRUEN, "t3", [("3. In dubio pro reo nur rügen, wenn das", "ExtraBold", 32, INK),
                                               ("Urteil selbst Zweifel erkennen lässt", "ExtraBold", 32, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Prüfschema
# ===========================================================================================================================
REIHEN = [("sc1", 0, "I. Maßstab: § 261 StPO – nur Rechtsfehler", True),
          ("sc2", 0, "II. Aussage gegen Aussage: Gesamtschau", True),
          (beim("sc2", "Entstehung"), 1, "1. Entstehung der Aussage", False),
          (beim("sc2", "Konstanz"), 1, "2. Konstanz: Abweichungen erkannt und erklärt?", False),
          (beim("sc2", "früheren"), 1, "3. frühere Angaben im Urteil mitgeteilt?", False),
          ("sc3", 0, "III. Zweifelssatz: nur bei Zweifeln des Gerichts", True),
          ("sc4", 0, "IV. Beruhen, § 337 Abs. 1 StPO", True),
          (beim("sc4", "Aufhebung"), 1, "Aufhebung, § 353 StPO; Zurückverweisung, § 354 Abs. 2 StPO", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Beweiswürdigung in der Revision"), 110, 90, "sch", 46),
           z("Revisionsbegründung, allgemeine Sachrüge", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 245
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 32, rechts=1800))
    y += {0: 82, 1: 64}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("sc1", "Prüfschema › I. Maßstab, § 261 StPO"), ("sc2", "Prüfschema › II. Aussage gegen Aussage"),
       ("sc3", "Prüfschema › III. Zweifelssatz"), ("sc4", "Prüfschema › IV. Beruhen, Aufhebung")], els_sch)

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Das Revisionsgericht würdigt", 0)], [("die Beweise ", 0), ("nicht neu", "a"), (".", 0)]], 750, 270, 44,
                "merke", {"a": beim("merke", "nicht")}),
    *markertext([[("Es prüft, ob das Urteil ", 0), ("Widersprüche", "b")],
                 [("gesehen und erklärt hat.", 0)],
                 [("In dubio pro reo greift erst,", 0)],
                 [("wenn das Gericht ", 0), ("selbst zweifelt", "c"), (".", 0)]], 750, 470, 40, "m2",
                {"b": beim("m2", "Widersprüche"), "c": beim("m2", "selbst")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
