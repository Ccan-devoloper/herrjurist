"""Folge 257 · Konkrete Gefahr: Wie wahrscheinlich muss der Schaden sein? – Serienstandard Open Peeps (Katzenkönig).
Fall (entschärfter Plan-Hook): Samstagnachmittag vor einem Mehrfamilienhaus. Herr Fichtner steht mit einem offenen
Benzinkanister am Hauseingang und raucht; Nachbar Sebastian ruft die Polizei; Polizistin Eilers riecht Benzin und fordert
ihn auf, die Zigarette auszumachen und den Kanister zu schließen; er will nur den Rasenmäher auftanken.
Szenen laut ../SZENENPLAN.md: A Mehrfamilienhaus (Fall), B Sachverhalt, C Generalklausel (Wortlautkarte § 8 Abs. 1 PolG NRW),
D Legaldefinition (Wortlautkarte § 2 Nr. 1 NPOG), E 1.–3. Merkmale am Fall, F 4. Je-desto-Formel (Zitatkarte BVerwG),
G Wahrscheinlichkeit am Fall und Grenze (Zitatkarte BVerfGE 115, 320), H 5. Prognose ex ante, I Ergebnis, J Abgrenzung der
Gefahrbegriffe (§ 2 NPOG), K Gegenfall und abstrakte Gefahr (Rückkehr zum Haus), L Länder-Overlay, M Klausurtipp (Lexi),
N Schema, O Merksatz (Lexi). Kein Feuer, keine Flamme, keine Explosion; Glut nur als Zigaretten-Icon (Phosphor) mit Rauch.
Ein Handlungsgeräusch (Autotür, ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend als eigene Kopie aus Folge 249
(gemeinsame Dateien unverändert); neu: gehweg(), haus(), auto(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Wortlautkarten wörtlich nach recht.nrw.de und voris (Abruf 08.10.2026); Zitatkarten wörtlich nach bverwg.de und
bundesverfassungsgericht.de."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_257/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_257/" in n:
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



# --- eigene Szenenbausteine: Gehweg, Mehrfamilienhaus, Auto (Palettenflächen, Tuschekontur) -----------------------------
GEHWEG = (214, 206, 192, 255)
F_O, F_U = 930, 1000                         # Gehweg (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen
BENZINROT = ROT


def gehweg(cue):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=GEHWEG)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    for x in range(120, 1860, 240):
        dr.line((x * s, 6 * s, x * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def haus(x0, cue, w=600, oben=300):
    """Mehrfamilienhaus: Fassade, Dach, 3 × 3 Fenster, Haustür (programmatisch, Palettenflächen)."""
    els = [karte(x0, oben, w, F_O - oben + 4, cue, fill=LILAHELL, rund=6, schatten=0, rand=5, anim="cut"),
           karte(x0 - 20, oben - 40, w + 40, 44, cue, fill=LILA, rund=8, schatten=0, rand=5, anim="cut")]
    for r in range(3):
        for c in range(3):
            if r == 2 and c == 2:
                continue
            els.append(karte(x0 + 50 + c * 185, oben + 60 + r * 190, 120, 120, cue, fill=BLAU, rund=8, schatten=0, rand=4,
                             anim="cut"))
    els.append(karte(x0 + w - 165, F_O - 230, 120, 234, cue, fill=HOLZ, rund=8, schatten=0, rand=5, anim="cut"))
    return els


def auto(cx, cue, breite=300, **k):
    return ficon("tabler", "car", cx, FU, breite, cue, fuell=BLAU, nebenfarbe=WEISS, **k)


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"FI": "Herr Fichtner", "EI": "Polizistin Eilers", "SE": "Sebastian"}
NFARBE = {"FI": GELB, "EI": BLAU, "SE": GRUEN}


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


K_GAS = ("ph", "gas-can", 100, BENZINROT)
K_ZIG = ("ph", "cigarette", 110, WEISS)

# ===========================================================================================================================
# A Fall: Samstagnachmittag vor einem Mehrfamilienhaus
# ===========================================================================================================================
FIX, EIX, SEX, AUX = 820, 1200, 1730, 1470    # Fichtner (blickt nach rechts), Eilers, Sebastian (blicken nach links), Auto
KAN = ficon("ph", "gas-can", 945, FU, 118, "kanister", fuell=BENZINROT)
ZIG = ficon("ph", "cigarette", 905, 735, 78, "rauch", fuell=WEISS)
TUER = szene(auto(AUX, "polizei", breite=290), "257tuer*", 0.8, 0.0)
folie([(NULL, "Fall · Samstagnachmittag vor dem Haus"), ("kanister", "Fall · Herr Fichtner mit Benzinkanister"),
       ("offen", "Fall · Der Deckel ist offen"), ("rauch", "Fall · Er raucht"), ("nachbar", "Fall · Nachbar Sebastian"),
       ("se1", "Fall · Der Anruf"), ("polizei", "Fall · Polizistin Eilers"), ("geruch", "Fall · Es riecht nach Benzin"),
       ("ei1", "Fall · „Zigarette aus, Kanister zu“"), ("fi1", "Fall · „Da passiert schon nichts“"),
       ("frage", "Fall · Die Frage")], [
    hart(gehweg(NULL)),
    *haus(70, NULL),
    hart(ficon("tabler", "sun", 1780, 200, 110, NULL, fuell=GELB, anim="cut")),
    hart(pl("Samstagnachmittag: ein Mehrfamilienhaus", 70, 30, NULL, fill=GELB, size=38, bis="frage")),
    pl("Herr Fichtner mit einem Benzinkanister", 70, 100, "kanister", fill=WEISS, size=32, bis="frage"),
    *fig("FI", FIX, FU, FH, [("kanister", "ruhig_r"), ("rauch", "froh_r"), ("ei1", "denkt_r")], bis="fi1", erst="pop"),
    *redet("FI_redet_r", FIX, FU, FH, "fi1", "frage"),
    *fig("FI", FIX, FU, FH, [("frage", "froh_r")], erst="cut"),
    ns("Herr Fichtner", FIX, FU, "kanister", GELB, d=0.1),
    KAN,
    pl("Deckel offen", 1015, 800, "offen", fill=HELLROT, size=28, bis="polizei"),
    ring(946, 820, 80, 50, beim("offen", "offen"), bis="rauch"),
    ZIG,
    pl("raucht", 935, 640, "rauch", fill=WEISS, size=28, bis="se1"),
    pl("Sebastian ruft die Polizei", 70, 170, "nachbar", fill=WEISS, size=32, bis="frage"),
    *fig("SE", SEX, FU, FH, [("nachbar", "sorge")], bis="se1", erst="pop"),
    *redet("SE_redet", SEX, FU, FH, "se1", "polizei"),
    *fig("SE", SEX, FU, FH, [("polizei", "ruhig"), ("fi1", "denkt")], erst="cut"),
    ns("Sebastian", SEX, FU, "nachbar", GRUEN, d=0.1),
    ficon("fluent-emoji-high-contrast", "mobile-phone", 1585, 640, 46, "nachbar", fuell=WEISS, bis="polizei"),
    TUER,
    pl("Polizei", AUX, 690, "polizei", fill=BLAU, size=28, anker="m"),
    *fig("EI", EIX, FU, FH, [("polizei", "ruhig"), ("geruch", "denkt")], bis="ei1", erst="pop"),
    *redet("EI_redet", EIX, FU, FH, "ei1", "fi1"),
    *fig("EI", EIX, FU, FH, [("fi1", "ernst"), ("frage", "denkt")], erst="cut"),
    ns("Polizistin Eilers", EIX, FU, "polizei", BLAU, d=0.1),
    pl("Es riecht nach Benzin.", 1000, 330, "geruch", fill=GELB, size=28, anker="m", bis="ei1"),
    ficon("tabler", "lawn-mower", 330, FU, 170, beim("fi1", "Rasenmäher"), fuell=GRUEN),
    blase("sprech", 780, 250, "se1", 1360, 250, inhalt=["Polizei? Vor unserem Haus raucht ein Mann", "neben einem offenen Benzinkanister.",
          "Bitte kommen Sie!"], textsize=32, figur=("SE_redet", SEX, FU, FH), bis="polizei"),
    blase("sprech", 830, 220, "ei1", 1290, 260, inhalt=["Machen Sie bitte sofort die Zigarette aus", "und schließen Sie den Kanister."],
          textsize=32, figur=("EI_redet", EIX, FU, FH), bis="fi1"),
    blase("sprech", 840, 220, "fi1", 1060, 280, inhalt=["Ich will doch nur den Rasenmäher auftanken.", "Da passiert schon nichts."],
          textsize=32, figur=("FI_redet_r", FIX, FU, FH), bis="frage"),
    pl("Durfte Polizistin Eilers das verlangen?", 70, 30, "frage", fill=PINK, size=36),
    pl("Konkrete Gefahr – wie wahrscheinlich muss der Schaden sein?", 70, 100, "frage2", fill=PINK, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_257(cue, absaetze, frage):
    els = [karte(140, 100, 1640, 740, cue, fill=HELL), titel("Sachverhalt", 210, 140, cue, 60)]
    y = 245
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_257("sv", [
    "Nordrhein-Westfalen, Samstagnachmittag: Herr Fichtner steht mit einem Benzinkanister am Eingang eines "
    "Mehrfamilienhauses. Der Deckel ist offen, es riecht nach Benzin, und er raucht direkt neben dem Kanister. "
    "Sein Nachbar Sebastian ruft die Polizei.",
    "Polizistin Eilers fordert Herrn Fichtner auf, sofort die Zigarette auszumachen und den Kanister zu schließen. "
    "Er antwortet: „Ich will doch nur den Rasenmäher auftanken. Da passiert schon nichts.“",
], "Durfte Polizistin Eilers das verlangen? Liegt eine konkrete Gefahr vor?")

# ===========================================================================================================================
# C Ermächtigungsgrundlage: Generalklausel (Wortlautkarte § 8 Abs. 1 PolG NRW)
# ===========================================================================================================================
W8 = ["„(1) Die Polizei kann die notwendigen Maßnahmen treffen, um eine",
      "im einzelnen Falle bestehende, konkrete Gefahr für die öffentliche",
      "Sicherheit oder Ordnung (Gefahr) abzuwehren, …“"]
PE = "Ermächtigungsgrundlage"
y8 = 385
w8, w8_y = wortlaut(80, y8, 1100, W8, "§ 8 Abs. 1 PolG NRW (Beispiel)", "wl8", marken=[
    (0, "notwendigen Maßnahmen", beim("wl8", "notwendigen")), (1, "im einzelnen Falle bestehende,", beim("wl8", "einzelnen")),
    (1, "konkrete Gefahr", beim("wl8", "konkrete"))], size=32)
folie([("egl", f"{PE} · keine Standardmaßnahme"), (beim("egl", "Grundlage"), f"{PE} · Generalklausel"),
       ("land", f"{PE} · Landesrecht, gleiche Dogmatik"), ("wl8", f"{PE} · Beispiel: § 8 Abs. 1 PolG NRW"),
       ("schutz", f"{PE} · Schutzgüter: Folge 213"), ("kern", "Konkrete Gefahr · die Kernfrage")], rechts_frei([
    *tafel("egl", "Ermächtigungsgrundlage", h=840),
    *neinz("keine Standardmaßnahme für „Zigarette aus“", 175, "egl", "Bold", 32, x=160),
    *okz("Grundlage: die Generalklausel", 230, beim("egl", "Grundlage"), "Bold", 32, x=160),
    z("Polizeirecht ist Landesrecht – die Dogmatik", 110, 290, "land", size=30),
    z("ist bundesweit gleich", 110, 330, beim("land", "bundesweit"), size=30),
    *[bis_(e, None) for e in w8],
    z("Schutzgüter der öffentlichen Sicherheit: Folge 213", 110, w8_y + 30, "schutz", "Bold", 30),
    blk(110, w8_y + 100, 1040, 76, GELB, "kern", [("Kernfrage: die konkrete Gefahr", "ExtraBold", 34, INK)]),
    *requisit([("egl", K_ZIG, "„Zigarette aus“", WEISS),
               ("land", ("tabler", "map-2", 110, GRUEN), "Landesrecht", WEISS),
               ("wl8", ("tabler", "book", 100, WEISS), "§ 8 Abs. 1 PolG NRW", GELB),
               ("schutz", ("tabler", "shield", 100, BLAU), "Folge 213", WEISS),
               ("kern", K_GAS, "konkrete Gefahr?", HELLROT)]),
    *stehend("EI", X1, [("egl", "ruhig"), ("wl8", "ernst")]),
    *stehend("FI", X2, [("egl", "denkt"), ("kern", "ruhig")]),
]))

# ===========================================================================================================================
# D Legaldefinition: § 2 Nr. 1 NPOG (Wortlautkarte) und BVerfGE 141, 220, Rn. 111
# ===========================================================================================================================
WN = ["„… 1. Gefahr: eine konkrete Gefahr, das heißt eine Sachlage, bei der",
      "im einzelnen Fall die hinreichende Wahrscheinlichkeit besteht,",
      "dass in absehbarer Zeit ein Schaden für die öffentliche",
      "Sicherheit oder Ordnung eintreten wird; …“"]
wn, wn_y = wortlaut(80, 170, 1100, WN, "§ 2 Nr. 1 NPOG (Niedersachsen)", "def", marken=[
    (0, "Sachlage", "defa"), (1, "im einzelnen Fall", beim("defa", "einzelnen")),
    (1, "hinreichende Wahrscheinlichkeit", beim("defa", "hinreichende")), (2, "in absehbarer Zeit", "defb"),
    (2, "Schaden", beim("defc", "Schaden"))], size=32)
PK = "Konkrete Gefahr"
folie([("def", f"{PK} › Legaldefinition: § 2 Nr. 1 NPOG"), ("defa", f"{PK} › Sachlage im Einzelfall"),
       (beim("defa", "hinreichende"), f"{PK} › hinreichende Wahrscheinlichkeit"), ("defb", f"{PK} › in absehbarer Zeit"),
       ("defc", f"{PK} › Schaden für ein Schutzgut"), ("bverfg", f"{PK} › BVerfG: ungehinderter Ablauf")], rechts_frei([
    karte(60, 60, 1140, 840, "def"), titel(glyphen("Was ist eine konkrete Gefahr?"), 110, 90, "def", 46),
    *wn,
    z("BVerfG: bei ungehindertem Ablauf des Geschehens", 110, wn_y + 40, "bverfg", "Bold", 32),
    z("droht die Verletzung eines Schutzguts", 110, wn_y + 86, beim("bverfg", "droht"), "Bold", 32),
    zit("BVerfG, Urt. v. 20.4.2016 – 1 BvR 966/09 u. a., Rn. 111 (BVerfGE 141, 220)", 110, wn_y + 136, beim("bverfg", "Verletzung")),
    *requisit([("def", ("tabler", "book", 100, WEISS), "§ 2 Nr. 1 NPOG", GELB),
               ("defa", K_GAS, "Sachlage im Einzelfall", WEISS),
               ("defb", ("tabler", "clock", 100, WEISS), "absehbare Zeit", WEISS),
               ("defc", ("ph", "building-apartment", 120, WEISS), "Schaden", HELLROT),
               ("bverfg", ("tabler", "building-bank", 110, BLAU), "BVerfG", WEISS)]),
    *stehend("EI", X1, [("def", "ruhig"), ("bverfg", "ernst")]),
    *stehend("FI", X2, [("def", "ruhig"), ("defc", "denkt")]),
]))

# ===========================================================================================================================
# E 1.–3. Merkmale am Fall
# ===========================================================================================================================
folie([("e1", f"{PK} › 1. Sachlage im Einzelfall"), ("e2", f"{PK} › 2. Schaden für ein Schutzgut"),
       ("e3", f"{PK} › 3. in absehbarer Zeit")], rechts_frei([
    *tafel("e1", "Die Merkmale am Fall", h=760),
    z("1. Sachlage im Einzelfall", 110, 180, "e1", "ExtraBold", 36),
    *okz("dieser Kanister, diese Zigarette, dieses Haus", 235, beim("e1", "dieser"), size=32, x=160),
    z("2. drohender Schaden", 110, 330, "e2", "ExtraBold", 36),
    *okz("Brand: Leben und Gesundheit der Bewohner", 385, beim("e2", "Brand"), size=32, x=160),
    z("und das Haus", 160, 431, beim("e2", "Haus"), size=32),
    zit("Schutzgüter der öffentlichen Sicherheit: Folge 213", 160, 479, beim("e2", "Haus")),
    z("3. in absehbarer Zeit", 110, 545, "e3", "ExtraBold", 36),
    *okz("kann jeden Moment geschehen", 600, beim("e3", "Das"), size=32, x=160),
    z("4. hinreichende Wahrscheinlichkeit?", 110, 690, beim("e3", "geschehen", ende=True), "ExtraBold", 36, farbe=TEXT),
    *requisit([("e1", K_GAS, "dieser Kanister", WEISS),
               ("e2", ("ph", "building-apartment", 120, WEISS), "Leben, Gesundheit, Haus", HELLROT),
               ("e3", ("tabler", "clock", 100, WEISS), "jeden Moment", WEISS)]),
    *stehend("EI", X1, [("e1", "ernst"), ("e3", "denkt")]),
    *stehend("FI", X2, [("e1", "froh"), ("e2", "sorge")]),
]))

# ===========================================================================================================================
# F 4. Hinreichende Wahrscheinlichkeit: Je-desto-Formel (Zitatkarte BVerwG 3 C 16.11, Rn. 32)
# ===========================================================================================================================
WJ = ["„… an die Wahrscheinlichkeit des Schadenseintritts um so geringere",
      "Anforderungen zu stellen sind, je größer und folgenschwerer der",
      "möglicherweise eintretende Schaden ist …“"]
wj, wj_y = wortlaut(80, 250, 1100, WJ, "BVerwG, Urt. v. 22.3.2012 – 3 C 16.11, Rn. 32", "jdf", marken=[
    (0, "um so geringere", beim("jdf", "geringere")), (1, "je größer und folgenschwerer", beim("jdf", "größer"))], size=32)
PW = f"{PK} › 4. hinreichende Wahrscheinlichkeit"


def balken(y, w, fill, cue, links, rechts):
    return [karte(110, y, w, 64, cue, fill=fill, rund=12, schatten=4, rand=4),
            z(links, 130, y + 12, cue, "Bold", 30),
            z(rechts, 110 + w + 30, y + 12, cue, size=30)]


folie([("jd", f"{PW}"), ("jdf", f"{PW} › Je-desto-Formel"), ("jdk", f"{PW} › kleiner Schaden: höhere Wahrscheinlichkeit")],
      rechts_frei([
    *tafel("jd", "4. Wie wahrscheinlich muss der Schaden sein?", h=820, size=42),
    z("Je-desto-Formel:", 110, 180, "jdf", "ExtraBold", 36),
    *wj,
    *balken(wj_y + 40, 470, ROT, beim("jdf", "größer"), "großer Schaden", "geringere Wahrscheinlichkeit genügt"),
    *balken(wj_y + 130, 260, GELB, "jdk", "kleiner Schaden", "umso wahrscheinlicher nötig"),
    zit("ständige Rechtsprechung im allgemeinen Polizei- und Ordnungsrecht (BVerwG, a. a. O.)", 110, wj_y + 215, beim("jdk", "wahrscheinlicher")),
    *requisit([("jd", ("tabler", "scale", 110, WEISS), "Wahrscheinlichkeit?", WEISS),
               ("jdf", ("tabler", "scale", 110, GELB), "Je-desto-Formel", GELB),
               ("jdk", ("tabler", "scale", 110, WEISS), "kleiner Schaden", WEISS)]),
    *stehend("EI", X1, [("jd", "denkt"), ("jdf", "ernst")]),
    *stehend("FI", X2, [("jd", "ruhig"), ("jdk", "denkt")]),
]))

# ===========================================================================================================================
# G Wahrscheinlichkeit am Fall und Grenze (Zitatkarte BVerfGE 115, 320, Rn. 136)
# ===========================================================================================================================
WG = ["„Selbst bei höchstem Gewicht der drohenden Rechtsgutbeeinträchtigung",
      "kann auf das Erfordernis einer hinreichenden Wahrscheinlichkeit",
      "nicht verzichtet werden.“"]
wg, wg_y = wortlaut(80, 560, 1100, WG, "BVerfG, Beschl. v. 4.4.2006 – 1 BvR 518/02, Rn. 136 (BVerfGE 115, 320)", "grenze",
                    marken=[(0, "Selbst bei höchstem Gewicht", beim("grenze", "Selbst")),
                            (2, "nicht verzichtet", beim("grenze", "nicht"))], size=30)
wg = [e for e in wg]
folie([("jdfall", f"{PW} › am Fall: sehr großer Schaden"), ("jdw", f"{PW} › ernsthaft möglich: genügt"),
       ("grenze", f"{PW} › Grenze: nie ohne Wahrscheinlichkeit")], rechts_frei([
    *tafel("jdfall", "Am Fall: Reicht das?", h=860),
    *okz("Brand in einem bewohnten Haus: sehr großer Schaden", 180, "jdfall", "Bold", 32, x=160),
    z("offener Kanister · Benzingeruch · Glut direkt daneben", 160, 260, "jdw", size=32),
    *okz("nicht sicher, aber ernsthaft möglich: genügt hier", 320, beim("jdw", "nicht"), "Bold", 32, x=160),
    blk(110, 400, 1040, 76, HELLROT, "grenze", [("Aber: Grenze der Je-desto-Formel", "ExtraBold", 34, INK)]),
    z("Vorsicht:", 110, 500, "grenze", "ExtraBold", 32),
    *wg,
    *requisit([("jdfall", ("ph", "building-apartment", 120, WEISS), "sehr großer Schaden", HELLROT),
               ("jdw", K_ZIG, "ernsthaft möglich", GELB),
               ("grenze", ("tabler", "alert-triangle", 100, HELLROT), "Grenze", HELLROT)]),
    *stehend("EI", X1, [("jdfall", "ernst"), ("jdw", "fest"), ("grenze", "denkt")]),
    *stehend("FI", X2, [("jdfall", "sorge"), ("grenze", "still")]),
]))

# ===========================================================================================================================
# H 5. Prognose ex ante
# ===========================================================================================================================
PP = f"{PK} › 5. Prognose ex ante"
folie([("exante", f"{PP}"), (beim("exante", "besonnenen"), f"{PP} › besonnener, sachkundiger Amtswalter"),
       ("tats", f"{PP} › Tatsachen, keine Vermutungen"), ("eisieht", f"{PP} › was Eilers wahrnimmt"),
       ("wasser", "Anscheinsgefahr · Folge 052")], rechts_frei([
    *tafel("exante", "5. Prognose ex ante", h=860),
    z("Zeitpunkt des Einschreitens: ex ante", 110, 180, "exante", "Bold", 34),
    z("aus Sicht eines besonnenen und sachkundigen Amtswalters", 110, 230, beim("exante", "besonnenen"), size=31),
    zit("OVG NRW, Urt. v. 15.7.2002 – 7 A 1717/01; VG Köln, Gerichtsbescheid", 110, 278, beim("exante", "Amtswalters")),
    zit("v. 11.2.2016 – 20 K 6403/14, Rn. 45", 110, 312, beim("exante", "Amtswalters")),
    z("Tatsachen statt bloßer Vermutungen", 110, 375, "tats", "Bold", 34),
    zit("BVerfG, Beschl. v. 4.4.2006 – 1 BvR 518/02, Rn. 145 (BVerfGE 115, 320)", 110, 423, beim("tats", "Vermutungen")),
    *okz("offener Kanister", 490, beim("eisieht", "offenen"), size=32, x=160),
    *okz("Benzingeruch", 540, beim("eisieht", "riecht"), size=32, x=160),
    *okz("Glut direkt daneben", 590, beim("eisieht", "Glut"), size=32, x=160),
    z("= Tatsachen", 600, 540, beim("eisieht", "Tatsachen"), "ExtraBold", 34),
    blk(110, 670, 1040, 120, GELB, "wasser", [("Nur Wasser im Kanister? Sah und roch alles nach", "ExtraBold", 30, INK),
                                            ("Benzin: Anscheinsgefahr – mehr in Folge 052", "ExtraBold", 30, INK)]),
    *requisit([("exante", ("tabler", "clock", 100, WEISS), "ex ante", GELB),
               ("tats", ("tabler", "list-check", 100, WEISS), "Tatsachen", WEISS),
               ("eisieht", K_GAS, "offen, Benzingeruch", WEISS),
               ("wasser", ("tabler", "droplet", 90, BLAU), "Folge 052", GELB)]),
    *stehend("EI", X1, [("exante", "ernst"), ("eisieht", "denkt"), ("wasser", "ruhig")]),
    *stehend("FI", X2, [("exante", "ruhig"), ("eisieht", "sorge"), ("wasser", "denkt")]),
]))

# ===========================================================================================================================
# I Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · konkrete Gefahr (+)"), ("stoerer", "Ergebnis · Herr Fichtner verursacht die Gefahr"),
       ("mild", "Ergebnis · mildes Mittel"), ("darf", "Ergebnis · Eilers durfte es verlangen")], rechts_frei([
    *tafel("erg", "Ergebnis", h=720),
    blk(110, 180, 1040, 80, GRUEN, "erg", [("konkrete Gefahr (+)", "ExtraBold", 36, INK)]),
    *okz("Herr Fichtner verursacht die Gefahr selbst", 300, "stoerer", size=32, x=160),
    zit("vgl. § 4 Abs. 1 PolG NRW", 160, 348, beim("stoerer", "selbst")),
    *okz("Aufforderung: ein mildes Mittel", 410, "mild", size=32, x=160),
    zit("vgl. § 2 Abs. 1 PolG NRW", 160, 458, beim("mild", "Mittel")),
    blk(110, 530, 1040, 120, GELB, "darf", [("Eilers durfte verlangen: Zigarette aus,", "ExtraBold", 32, INK),
                                          ("Kanister schließen", "ExtraBold", 32, INK)]),
    *requisit([("erg", ("tabler", "shield", 100, GRUEN), "konkrete Gefahr (+)", GRUEN),
               ("stoerer", K_ZIG, "verursacht sie selbst", WEISS),
               ("mild", ("ph", "cigarette-slash", 110, WEISS), "mildes Mittel", WEISS),
               ("darf", K_GAS, "Kanister zu", GRUEN)]),
    *stehend("EI", X1, [("erg", "ernst"), ("darf", "froh")]),
    *stehend("FI", X2, [("erg", "still"), ("darf", "ruhig")]),
]))

# ===========================================================================================================================
# J Abgrenzung der Gefahrbegriffe (§ 2 Nr. 2, 3, 4, 6 NPOG)
# ===========================================================================================================================
PA = "Abgrenzung"
AB = [("ab1", "gegenwärtig", ROT, ["Einwirkung hat begonnen oder steht unmittelbar",
                                   "bzw. in allernächster Zeit mit an Sicherheit",
                                   "grenzender Wahrscheinlichkeit bevor"]),
      ("ab2", "erheblich", ORANGE, ["Gefahr für ein bedeutsames Rechtsgut,", "etwa Leben, Gesundheit, Freiheit"]),
      ("ab3", "dringend", LILA, ["nach Ausmaß des Schadens und", "Wahrscheinlichkeit erhöhte Gefahr"]),
      ("ab4", "abstrakt", BLAU, ["nach allgemeiner Lebenserfahrung mögliche", "Sachlage, die im Fall ihres Eintritts",
                                 "eine Gefahr darstellt"])]
els_ab = [*tafel("abgr", "Abgrenzung: weitere Gefahrbegriffe", h=880, size=44),
          zit("Definitionen: § 2 Nr. 2, 3, 4, 6 NPOG", 110, 160, beim("abgr", "Niedersachsen"))]
y = 210
for c, lab, farbe, zeilen in AB:
    els_ab.append(pl(lab, 110, y - 4, c, fill=farbe, size=30))
    for j, t in enumerate(zeilen):
        els_ab.append(z(t, 380, y + j * 40, c, size=30))
    y += len(zeilen) * 40 + 26
els_ab += [*okz("Fichtner: Leben und Gesundheit bedroht – auch erheblich", y + 10, "abfall", "Bold", 30, x=160),
           z("gegenwärtig? nur, wenn die Befugnisnorm es verlangt", 160, y + 64, "abgen", size=30)]
assert y + 64 + 50 <= 940, y
folie([("abgr", f"{PA} › Gefahrbegriffe"), ("ab1", f"{PA} › gegenwärtige Gefahr"), ("ab2", f"{PA} › erhebliche Gefahr"),
       ("ab3", f"{PA} › dringende Gefahr"), ("ab4", f"{PA} › abstrakte Gefahr"), ("abfall", f"{PA} › am Fall: erheblich"),
       ("abgen", f"{PA} › gegenwärtig: nur wenn verlangt")], rechts_frei([
    *els_ab,
    *requisit([("abgr", ("tabler", "list-details", 100, WEISS), "Gefahrbegriffe", WEISS),
               ("ab1", ("tabler", "clock", 100, HELLROT), "gegenwärtig", ROT),
               ("ab2", ("tabler", "heart", 100, ROT), "erheblich", ORANGE),
               ("ab3", ("tabler", "alert-triangle", 100, LILA), "dringend", LILA),
               ("ab4", ("tabler", "users", 110, BLAU), "abstrakt", BLAU),
               ("abfall", ("tabler", "heart", 100, ROT), "erheblich", ORANGE),
               ("abgen", ("tabler", "book", 100, WEISS), "Befugnisnorm", WEISS)]),
    *stehend("EI", X1, [("abgr", "ruhig"), ("abfall", "ernst")]),
    *stehend("FI", X2, [("abgr", "ruhig"), ("abfall", "sorge")]),
]))

# ===========================================================================================================================
# K Gegenfall (Rückkehr vor das Haus) und abstrakte Gefahr
# ===========================================================================================================================
GFX, GAX = 1720, 1010                       # Fichtner auf der anderen Straßenseite, Auto mit Kanister im Kofferraum
folie([("gegen", "Gegenfall · Kanister verschlossen im Kofferraum"), ("gegen2", "Gegenfall · Rauchen auf der anderen Straßenseite"),
       ("gneg", "Gegenfall · keine konkrete Gefahr"), ("gabs", "Abgrenzung › abstrakte Gefahr"),
       ("gabs2", "Abgrenzung › abstrakte Gefahr › Verordnung")], [
    hart(gehweg("gegen")),
    *haus(70, "gegen"),
    hart(ficon("tabler", "sun", 1780, 200, 110, "gegen", fuell=GELB, anim="cut")),
    hart(auto(GAX, "gegen", breite=360)),
    ficon("ph", "gas-can", GAX - 95, FU - 128, 56, beim("gegen", "Kofferraum"), fuell=BENZINROT),
    pl("Gegenfall: Kanister fest verschlossen im Kofferraum", 70, 30, "gegen", fill=GELB, size=32),
    pl("Herr Fichtner raucht auf der anderen Straßenseite", 70, 100, "gegen2", fill=WEISS, size=32),
    *fig("FI", GFX, FU, FH, [("gegen2", "froh"), ("gabs", "ruhig")], erst="pop"),
    ns("Herr Fichtner", GFX, FU, "gegen2", GELB, d=0.1),
    ficon("ph", "cigarette", GFX - 85, 735, 78, "gegen2", fuell=WEISS),
    nein(110, 195, "gneg", gr=22),
    pl("Brand praktisch ausgeschlossen: keine konkrete Gefahr", 150, 170, "gneg", fill=HELLROT, size=32),
    karte(820, 250, 760, 330, "gabs", fill=WEISS, rund=18, schatten=6, rand=4),
    z("Abstrakte Gefahr:", 850, 275, "gabs", "ExtraBold", 32, rechts=1560),
    z("Rauchen beim Umgang mit Benzin –", 850, 322, beim("gabs", "Rauchen"), size=30, rechts=1560),
    z("allgemein gefährlich?", 850, 362, beim("gabs", "allgemein"), size=30, rechts=1560),
    z("gleichgelagerte Fälle: Verordnung,", 850, 420, "gabs2", "Bold", 30, rechts=1560),
    z("gilt auch ohne konkrete Gefahr", 850, 460, beim("gabs2", "auch"), "Bold", 30, rechts=1560),
    zit("BVerwG, Urt. v. 25.10.2017 – 6 C 44.16, Rn. 23;", 850, 508, beim("gabs2", "Verordnungen"), rechts=1560),
    zit("§ 55 Abs. 1 NPOG", 850, 540, beim("gabs2", "Verordnungen"), rechts=1560),
])

# ===========================================================================================================================
# L Länder-Overlay
# ===========================================================================================================================
SP0, SP1, SP2 = 130, 560, 1080
ZL = [("tnrw", "Nordrhein-Westfalen", "§ 8 Abs. 1 PolG NRW", "„konkrete Gefahr“ im Wortlaut"),
      ("tbb", "Brandenburg", "§ 10 Abs. 1 BbgPolG", "„konkrete Gefahr“ im Wortlaut"),
      ("tni", "Niedersachsen", "§ 11 NPOG", "„Gefahr“, definiert in § 2 Nr. 1 NPOG"),
      ("tsn", "Sachsen", "§ 12 Abs. 1 SächsPVDG", "„Gefahr“, definiert in § 4 Nr. 3 a SächsPVDG")]
els_t = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Länder-Overlay: Generalklausel und Gefahrbegriff"), 110, 90, "tab", 46),
         z("Land", SP0, 200, "tab", "ExtraBold", 34, rechts=1820), z("Generalklausel", SP1, 200, "tab", "ExtraBold", 34, rechts=1820),
         z("Gefahrbegriff", SP2, 200, "tab", "ExtraBold", 34, rechts=1820),
         linienzug([(110, 258), (1810, 258)], "tab", breite=5)]
y = 290
for c, land, norm, begr in ZL:
    els_t += [z(land, SP0, y, c, "Bold", 34, rechts=1820), z(norm, SP1, y, c, size=34, rechts=1820),
              z(begr, SP2, y, c, size=34, rechts=1820)]
    y += 92
els_t += [blk(110, y + 30, 1700, 80, GELB, "tdein", [("In deinem Land ggf. andere Nummer – die Prüfung bleibt gleich", "ExtraBold", 34, INK)]),
          zit("Wortlaut geprüft am 8.10.2026: recht.nrw.de, bravors.brandenburg.de, voris.wolterskluwer-online.de, revosax.sachsen.de",
              110, y + 140, "tdein", rechts=1820)]
folie([("tab", "Länder-Overlay · gleiche Prüfung, andere Nummern"), ("tnrw", "Länder-Overlay › Nordrhein-Westfalen"),
       ("tbb", "Länder-Overlay › Brandenburg"), ("tni", "Länder-Overlay › Niedersachsen"), ("tsn", "Länder-Overlay › Sachsen"),
       ("tdein", "Länder-Overlay › dein Landesgesetz")], els_t)

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · nicht nur behaupten"), ("tipp1", "Klausurtipp · Definition und Subsumtion"),
       ("tipp2", "Klausurtipp · Je-desto mit dem konkreten Schaden"), ("tipp3", "Klausurtipp · ex ante beurteilen")], [
    *tafel("tipp", "Klausurtipp: Gefahr sauber begründen", fill=HELL, h=680, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Nicht nur: „Es besteht eine Gefahr.“", 200, 200, "tipp", "Bold", 34),
    z("2. Definition angeben, jedes Merkmal", 200, 285, "tipp1", "Bold", 34),
    z("am Sachverhalt subsumieren", 200, 333, beim("tipp1", "Merkmal"), size=32),
    z("3. Je-desto-Formel in die Begründung –", 200, 418, "tipp2", "Bold", 34),
    z("mit dem konkret drohenden Schaden", 200, 466, beim("tipp2", "konkret"), size=32),
    z("4. alles ex ante beurteilen, nicht mit", 200, 551, "tipp3", "Bold", 34),
    z("dem Wissen von hinterher", 200, 599, beim("tipp3", "Wissen"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Schema
# ===========================================================================================================================
REIHEN = [("s1", "1. Sachlage im Einzelfall"),
          ("s2", "2. drohender Schaden für ein Schutzgut"),
          ("s3", "3. in absehbarer Zeit"),
          ("s4", "4. hinreichende Wahrscheinlichkeit: Je-desto-Formel"),
          ("s5", "5. Prognose ex ante, auf Tatsachen gestützt"),
          ("s6", "Danach: Verlangt die Norm eine besondere Gefahr – etwa gegenwärtig oder erheblich?")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: konkrete Gefahr"), 110, 90, "sch", 50),
           zit("z. B. § 8 Abs. 1 PolG NRW, § 11 i. V. m. § 2 Nr. 1 NPOG", 110, 175, beim("sch", "Schema"), rechts=1820)]
y = 250
for c, text in REIHEN:
    els_sch.append(z(text, 130, y, c, "ExtraBold" if c != "s6" else "Bold", 40 if c != "s6" else 36, rechts=1820))
    y += 104
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › 1. Sachlage im Einzelfall"), ("s2", "Schema › 2. Schaden für ein Schutzgut"),
       ("s3", "Schema › 3. in absehbarer Zeit"), ("s4", "Schema › 4. hinreichende Wahrscheinlichkeit"),
       ("s5", "Schema › 5. Prognose ex ante"), ("s6", "Schema › besondere Gefahr?")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Je ", 0), ("größer", "a"), (" der drohende Schaden,", 0)],
                 [("desto ", 0), ("geringer", "b"), (" die nötige", 0)], [("Wahrscheinlichkeit.", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "größer"), "b": beim("merke", "geringer")}),
    *markertext([[("Ganz verzichten darf man auf sie ", 0), ("nie", "c"), (",", 0)],
                 [("und geurteilt wird ", 0), ("ex ante", "d"), (",", 0)],
                 [("auf der Grundlage von ", 0), ("Tatsachen", "e"), (".", 0)]], 750, 560, 46, "m2",
                {"c": beim("m2", "nie"), "d": beim("m2", "ex"), "e": beim("m2", "Tatsachen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
