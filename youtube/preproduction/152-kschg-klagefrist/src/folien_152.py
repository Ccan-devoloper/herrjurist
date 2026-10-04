"""Folge 152 · Kündigungsschutzgesetz: Wann gilt das KSchG – und die 3-Wochen-Frist – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Kornelia, seit acht Jahren Gärtnerin in der Gärtnerei von Herrn Steinmetz (25 Beschäftigte), erhält am Montag,
5.10.2026, persönlich eine schriftliche ordentliche Kündigung ohne Begründung und will es sich „in Ruhe überlegen“.
Szenen laut ../SZENENPLAN.md: A Gewächshaus (Fall), B Sachverhalt, C Aufbau, D Wortlautkarte § 1 Abs. 1 KSchG, E Wortlautkarte
§ 23 Abs. 1 S. 3 KSchG, F Wortlautkarte § 1 Abs. 2 S. 1 mit drei Gründen, G Begründung und Beweislast (§ 1 Abs. 2 S. 4),
H1 Wortlautkarte § 4 S. 1, H2 Wortlautkarte § 7 und § 5, I Fristberechnung im Kalender, J Lösung, K Klausurtipp (Lexi),
L Prüfschema, M Merksatz (Lexi).
Zwei Handlungsgeräusche (Schritte, als Herr Steinmetz ins Gewächshaus kommt; Umschlag, als Kornelia den Brief öffnet;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 149 (gemeinsame Dateien unverändert); neu: gewaechshaus(),
pflanztisch(), grundkarte(), kalender(), markiere(), zelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_152/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_152/" in n:
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
GLAS = (222, 238, 250, 255)
ERDE = (168, 120, 80, 255)
BODEN_Y = 905                                # Boden im Gewächshaus = Unterkante der Figuren
FHA = 480                                    # Figurenhöhe in der Fallszene
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def gewaechshaus(c):
    """Gewächshaus (Grundform): Glasfläche mit Satteldach, Sprossen, Erdstreifen; harter Schnitt ab 0,0 s."""
    s = 2
    x0, y0, w, h = 80, 380, 1760, BODEN_Y - 380
    im = Image.new("RGBA", (w * s, (h + 40) * s))
    dr = ImageDraw.Draw(im)
    poly = [(0, h), (0, 90), (w / 2, 0), (w, 90), (w, h)]
    P_ = [(int(px * s) + 3 * s, int(py * s) + 3 * s) for px, py in [(p[0] * (w - 6) / w, p[1]) for p in poly]]
    dr.polygon(P_, fill=GLAS)
    for xs in range(220, w, 220):                                   # senkrechte Sprossen bis zur Dachlinie
        yt = 90 - 90 * (1 - abs(xs - w / 2) / (w / 2))
        dr.line((xs * s, yt * s + 6 * s, xs * s, h * s), fill=(150, 170, 190, 255), width=4 * s)
    dr.line((6 * s, 300 * s, (w - 6) * s, 300 * s), fill=(150, 170, 190, 255), width=4 * s)
    dr.line(P_ + [P_[0]], fill=INK, width=6 * s, joint="curve")
    dr.rectangle((0, h * s, w * s, (h + 36) * s), fill=ERDE)
    dr.line((0, h * s, w * s, h * s), fill=INK, width=5 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return hart(El(im, x0, y0, c, "cut", 0.0, None, name="gewaechshaus"))


def pflanztisch(c):
    """Pflanztisch (Grundform) mit Topfpflanzen aus Tabler (Grün/Rot/Gelb gefüllt)."""
    s = 2
    im = Image.new("RGBA", (700 * s, 150 * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 0, 697 * s, 26 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xl in (40, 640):
        dr.rectangle((xl * s, 26 * s, (xl + 20) * s, 148 * s), fill=HOLZ, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    els = [hart(El(im, 110, BODEN_Y - 148, c, "cut", 0.0, None, name="pflanztisch"))]
    for cx, ic, fu, br in ((190, "plant", GRUEN, 120), (330, "plant-2", GRUEN, 120), (470, "flower", ROT, 110),
                           (610, "seedling", GRUEN, 110), (740, "plant", GRUEN, 100)):
        els.append(hart(ficon("tabler", ic, cx, BODEN_Y - 150, br, c, fuell=fu, anim="cut")))
    return els


def stehend(k, x, folge, unten=930, hoehe=480):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KO": "Kornelia", "ST": "Herr Steinmetz"}
NFARBE = {"KO": GRUEN, "ST": BLAU}


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


def zwei(folge_ko, folge_st):
    """Kornelia und Herr Steinmetz rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("KO", X1, folge_ko), *stehend("ST", X2, folge_st)]


def allein(k, folge):
    return stehend(k, FX, folge)


# ===========================================================================================================================
# A Fall: im Gewächshaus der Gärtnerei
# ===========================================================================================================================
KX, SX = 1040, 1500                          # Kornelia (blickt nach rechts), Herr Steinmetz (blickt nach links)
S_LOS, S_DA = beim("stein", "kommt"), beim("stein", "Gewächshaus", ende=True)
BRIEF_LOS, BRIEF_DA = beim("brief", "übergibt"), beim("brief", "Brief", ende=True)
BX, BY = 1135, 770                           # Brief bei Kornelia (Unterkante)
folie([(NULL, "Fall · In der Gärtnerei"), ("stein", "Fall · Der Brief"), ("kuend", "Fall · Die Kündigung"),
       ("k1", "Fall · Ohne jeden Grund?"), ("frage", "Fall · Die Frage")], [
    gewaechshaus(NULL),
    *pflanztisch(NULL),
    hart(pl("Gärtnerei am Stadtrand", 70, 30, NULL, fill=GELB, size=38)),
    pl("25 Beschäftigte", 70, 110, beim("fall", "fünfundzwanzig"), fill=WEISS, size=34, bis="kuend"),
    ficon("tabler", "users", 420, 168, 64, beim("fall", "fünfundzwanzig"), fuell=WEISS, bis="kuend"),
    # Kornelia an ihrem Pflanztisch, blickt nach rechts
    *fig("KO", KX, BODEN_Y, FHA, [(NULL, "froh_r"), ("brief", "ruhig_r"), (beim("kuend", "Kündigung"), "schreck_r"),
                                  ("grund", "sorge_r")], bis="k1"),
    hart(ns("Kornelia", KX, BODEN_Y, NULL, GRUEN)),
    pl("Gärtnerin seit 8 Jahren", 70, 190, beim("korn", "seit"), fill=GRUEN, size=34, bis="kuend"),
    # Herr Steinmetz kommt von rechts ins Gewächshaus (Schritte)
    szene(bewegt(peep_voll("ST_ruhig", SX, BODEN_Y, FHA, "stein", anim="pop", bis="kuend"), S_LOS, S_DA, 200, 0),
          "152schritte*", 1.0, 0.0),
    bewegt(ns("Herr Steinmetz", SX, BODEN_Y, "stein", BLAU, d=0.1), S_LOS, S_DA, 200, 0),
    pl("Inhaber: Herr Steinmetz", 70, 270, beim("stein", "Inhaber"), fill=BLAU, size=34, bis="kuend"),
    *fig("ST", SX, BODEN_Y, FHA, [("kuend", "ernst"), ("st1", "ernst")], erst="cut", bis="st1"),
    # der Brief wandert von Herrn Steinmetz zu Kornelia, dann öffnet sie ihn
    bis_(bewegt(ficon("tabler", "mail", BX, BY, 90, BRIEF_LOS, fuell=WEISS), BRIEF_LOS, BRIEF_DA, 220, -10), "kuend"),
    szene(ficon("tabler", "mail-opened", BX, BY, 90, "kuend", fuell=WEISS, anim="cut", bis=beim("kuend", "Kündigung")),
          "152umschlag*", 1.0, 0.0),
    ficon("tabler", "file-text", BX, BY + 10, 110, beim("kuend", "Kündigung"), fuell=WEISS, anim="cut", bis="frage"),
    pl("Ordentliche Kündigung, fristgerecht", 70, 110, beim("kuend", "ordentliche"), fill=WEISS, size=34, bis="frage"),
    pl("eigenhändig unterschrieben", 70, 190, beim("kuend", "eigenhändig"), fill=WEISS, size=34, bis="frage"),
    ficon("tabler", "writing-sign", 660, 250, 64, beim("kuend", "eigenhändig"), fuell=WEISS, bis="frage"),
    pl("Grund: keiner angegeben", 70, 270, "grund", fill=HELLROT, size=34, bis="frage"),
    # Figurenrede
    *redet("KO_redet_r", KX, BODEN_Y, FHA, "k1", "st1"),
    blase("sprech", 560, 210, "k1", 1080, 240, inhalt=["Nach 8 Jahren?", "Ohne jeden Grund?"], textsize=40,
          figur=("KO_redet_r", KX, BODEN_Y, FHA), bis="st1"),
    *fig("KO", KX, BODEN_Y, FHA, [("st1", "sorge_r")], erst="cut", bis="k2"),
    *redet("ST_redet", SX, BODEN_Y, FHA, "st1", "k2"),
    blase("sprech", 600, 210, "st1", 1440, 230, inhalt=["Einen Grund muss ich", "Ihnen nicht nennen."], textsize=38,
          figur=("ST_redet", SX, BODEN_Y, FHA), bis="k2"),
    *fig("ST", SX, BODEN_Y, FHA, [("k2", "skeptisch"), ("frage", "still")], erst="cut"),
    *redet("KO_redet_r", KX, BODEN_Y, FHA, "k2", "frage"),
    blase("sprech", 680, 220, "k2", 1060, 240, inhalt=["Dann überlege ich mir erst mal", "in Ruhe, was ich mache."],
          textsize=36, figur=("KO_redet_r", KX, BODEN_Y, FHA), bis="frage"),
    *fig("KO", KX, BODEN_Y, FHA, [("frage", "ernst_r"), ("frage2", "muede_r")], erst="cut"),
    pl("Ist die Kündigung wirksam?", 70, 110, "frage", fill=PINK, size=36),
    pl("Wie viel Zeit hat Kornelia, sich zu wehren?", 70, 190, "frage2", fill=PINK, size=36),
    ficon("tabler", "hourglass", 1040, 250, 70, "frage2", fuell=GELB),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_152(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_152("sv", [
    "Kornelia arbeitet seit 2018, also seit acht Jahren, als Gärtnerin in der Gärtnerei von Herrn Steinmetz am Stadtrand. "
    "Dort sind in der Regel 25 Arbeitnehmer beschäftigt; einen Betriebsrat gibt es nicht.",
    "Am Montag, 5. Oktober 2026, übergibt Herr Steinmetz ihr im Gewächshaus persönlich ein eigenhändig unterschriebenes "
    "Schreiben: die ordentliche Kündigung, fristgerecht zum 31. Januar 2027. Einen Grund nennt das Schreiben nicht. "
    "Auf ihre Frage sagt er: „Einen Grund muss ich Ihnen nicht nennen.“",
    "Kornelia will sich erst einmal in Ruhe überlegen, was sie tut.",
], "Ist die Kündigung wirksam, und bis wann muss Kornelia handeln?")

# ===========================================================================================================================
# C Aufbau
# ===========================================================================================================================
folie([("aufbau", "Aufbau · Kündigung erklärt und zugegangen"), ("a1", "Aufbau · drei Schritte"),
       ("a2", "Aufbau › 1. Anwendbarkeit des KSchG"), ("a3", "Aufbau › 2. Sozialwidrigkeit"),
       ("a4", "Aufbau › 3. Die Falle: Klagefrist")], rechts_frei([
    *tafel("aufbau", "Der Aufbau"),
    *okz("Kündigung schriftlich erklärt und zugegangen", 180, "aufbau", "Bold", 34, x=160),
    zit("Schriftform, § 623 BGB: Video „Kündigung per WhatsApp“", 160, 232, beim("aufbau", "Worauf")),
    z("Wir prüfen drei Schritte:", 110, 310, "a1", "Bold", 36),
    blk(110, 380, 1040, 80, GELB, "a2", [("1. Gilt das KSchG?", "ExtraBold", 36, INK)]),
    blk(110, 490, 1040, 80, BLAU, "a3", [("2. Ist die Kündigung sozial gerechtfertigt?", "ExtraBold", 36, INK)]),
    blk(110, 600, 1040, 80, HELLROT, "a4", [("3. Die Falle: die Klagefrist", "ExtraBold", 36, INK)]),
    *requisit([("aufbau", ("tabler", "file-text", 100, WEISS), "Kündigung", WEISS),
               ("a2", ("tabler", "book", 100, WEISS), "KSchG", GELB),
               ("a3", ("tabler", "scale", 100, WEISS), "sozial gerechtfertigt?", BLAU),
               ("a4", ("tabler", "hourglass", 90, GELB), "Klagefrist", HELLROT)]),
    *zwei([("aufbau", "ruhig"), ("a4", "sorge")], [("aufbau", "ruhig"), ("a2", "skeptisch")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 1 Abs. 1 KSchG: persönlicher Anwendungsbereich, Wartezeit
# ===========================================================================================================================
PA = "Anwendbarkeit"
W1 = ["„Die Kündigung des Arbeitsverhältnisses gegenüber einem",
      "Arbeitnehmer, dessen Arbeitsverhältnis in demselben Betrieb",
      "oder Unternehmen ohne Unterbrechung länger als sechs",
      "Monate bestanden hat, ist rechtsunwirksam, wenn sie sozial",
      "ungerechtfertigt ist.“"]
w1, w1_y = wortlaut(80, 170, 1100, W1, "§ 1 Abs. 1 KSchG", "p1", marken=[
    (1, "Arbeitnehmer", beim("p1", "Arbeitnehmer")), (2, "ohne Unterbrechung", beim("p1", "Unterbrechung")),
    (2, "länger als sechs", beim("p1", "länger")), (3, "Monate", beim("p1", "länger")),
    (3, "rechtsunwirksam", beim("p1", "rechtsunwirksam"))], size=32)
folie([("p1", f"{PA} › persönlich, § 1 Abs. 1 KSchG"), ("warte", f"{PA} › Wartezeit"),
       ("p1fall", f"{PA} › Wartezeit erfüllt (+)")], rechts_frei([
    *tafel("p1", "Persönlich: § 1 Abs. 1 KSchG"),
    *w1,
    blk(110, w1_y + 30, 1040, 80, LILA, "warte", [("Wartezeit: länger als 6 Monate", "ExtraBold", 36, INK)]),
    zit("BAG, Urt. v. 20.6.2013 – 2 AZR 790/11, Rn. 11", 110, w1_y + 122, "warte"),
    *okz("Kornelia: Arbeitnehmerin, 8 Jahre ohne Unterbrechung", w1_y + 185, "p1fall", "Bold", 34, x=160),
    *okz("Wartezeit erfüllt", w1_y + 250, beim("p1fall", "Wartezeit"), "Bold", 34, x=160),
    *requisit([("p1", ("tabler", "book", 100, WEISS), "§ 1 Abs. 1 KSchG", GELB),
               ("warte", ("tabler", "hourglass", 90, GELB), "mehr als 6 Monate", LILA),
               ("p1fall", ("tabler", "calendar", 100, WEISS), "seit 2018", GRUEN)]),
    *allein("KO", [("p1", "ruhig"), ("warte", "skeptisch"), (beim("p1fall", "Wartezeit"), "froh")]),
]))

# ===========================================================================================================================
# E Wortlautkarte § 23 Abs. 1 S. 3 KSchG: betrieblicher Anwendungsbereich
# ===========================================================================================================================
W23 = ["„In Betrieben und Verwaltungen, in denen in der Regel zehn",
       "oder weniger Arbeitnehmer ausschließlich der zu ihrer",
       "Berufsbildung Beschäftigten beschäftigt werden, gelten die",
       "Vorschriften des Ersten Abschnitts mit Ausnahme der §§ 4",
       "bis 7 … nicht für Arbeitnehmer, deren Arbeitsverhältnis",
       "nach dem 31. Dezember 2003 begonnen hat; …“"]
w23, w23_y = wortlaut(80, 165, 1100, W23, "§ 23 Abs. 1 S. 3 KSchG", "p23", marken=[
    (5, "nach dem 31. Dezember 2003", beim("p23a", "nach")), (0, "in der Regel", beim("p23a", "Regel")),
    (0, "zehn", beim("p23a", "zehn")), (1, "oder weniger", beim("p23a", "zehn")),
    (1, "ausschließlich der zu ihrer", beim("p23a", "Auszubildende")), (2, "Berufsbildung Beschäftigten", beim("p23a", "Auszubildende")),
    (3, "mit Ausnahme der §§ 4", beim("klein", "Paragrafen")), (4, "bis 7", beim("klein", "Paragrafen"))], size=30)
folie([("p23", f"{PA} › betrieblich, § 23 Abs. 1 S. 3 KSchG"), ("regel", f"{PA} › „in der Regel“"),
       ("teil", f"{PA} › Teilzeit, § 23 Abs. 1 S. 4"), ("p23fall", f"{PA} › mehr als 10 Arbeitnehmer (+)"),
       ("klein", f"{PA} › Klagefrist auch im Kleinbetrieb")], rechts_frei([
    *tafel("p23", "Betrieblich: § 23 Abs. 1 KSchG"),
    *w23,
    z("„in der Regel“: kennzeichnende Beschäftigungslage", 110, w23_y + 22, "regel", "Bold", 32),
    zit("BAG, Urt. v. 24.1.2013 – 2 AZR 140/12, Rn. 11", 110, w23_y + 66, "regel"),
    z("Teilzeit (S. 4): bis 20 Std. zählt 0,5, bis 30 Std. 0,75", 110, w23_y + 112, "teil", size=32),
    *okz("Gärtnerei: 25 Beschäftigte, Kornelia seit 2018", w23_y + 172, "p23fall", "Bold", 32, x=160),
    blk(110, w23_y + 240, 1040, 80, HELLROT, "klein", [("§§ 4–7: Klagefrist gilt auch im Kleinbetrieb", "ExtraBold", 34, INK)]),
    *requisit([("p23", ("tabler", "users", 110, WEISS), "Betriebsgröße", WEISS),
               ("regel", ("tabler", "calendar", 100, WEISS), "in der Regel", WEISS),
               ("teil", ("tabler", "clock", 100, WEISS), "Teilzeit anteilig", WEISS),
               ("p23fall", ("tabler", "plant", 110, GRUEN), "25 Beschäftigte", GRUEN),
               ("klein", ("tabler", "hourglass", 90, GELB), "auch im Kleinbetrieb", HELLROT)]),
    *zwei([("p23", "ruhig"), ("p23fall", "froh"), ("klein", "ernst")], [("p23", "ruhig"), ("teil", "skeptisch"), ("p23fall", "still")]),
]))

# ===========================================================================================================================
# F Wortlautkarte § 1 Abs. 2 S. 1 KSchG: drei Kündigungsgründe
# ===========================================================================================================================
PB = "Sozialwidrigkeit"
W12 = ["„Sozial ungerechtfertigt ist die Kündigung, wenn sie nicht",
       "durch Gründe, die in der Person oder in dem Verhalten des",
       "Arbeitnehmers liegen, oder durch dringende betriebliche",
       "Erfordernisse, die einer Weiterbeschäftigung des",
       "Arbeitnehmers in diesem Betrieb entgegenstehen, bedingt ist.“"]
w12, w12_y = wortlaut(80, 165, 1100, W12, "§ 1 Abs. 2 S. 1 KSchG", "p12a", marken=[
    (1, "in der Person", beim("p12a", "Person")), (1, "in dem Verhalten", beim("p12a", "Verhalten")),
    (2, "dringende betriebliche", beim("p12a", "dringende")), (3, "Erfordernisse", beim("p12a", "dringende")),
    (4, "bedingt ist", beim("p12a", "bedingt"))], size=30)
GW, GY, GH = 335, w12_y + 22, 352             # drei Karten: Breite, Oberkante, Höhe


def grundkarte(i, cue, icon, fuell, kopf, zeilen, fund=None):
    x = 110 + i * (GW + 17)
    els = [karte(x, GY, GW, GH, cue, fill=HELL, rund=18, schatten=6, rand=4),
           ficon("tabler", icon, x + GW // 2, GY + 100, 80, cue, fuell=fuell),
           z(kopf, x + 20, GY + 112, cue, "ExtraBold", 32, rechts=x + GW - 10)]
    for j, (t, c) in enumerate(zeilen):
        els.append(z(t, x + 20, GY + 164 + j * 38, c, size=28, rechts=x + GW - 10))
    if fund:
        for j, t in enumerate(fund):
            els.append(zit(t, x + 20, GY + 282 + j * 30, zeilen[-1][1], rechts=x + GW - 10))
    return els


folie([("p12", PB + ", § 1 Abs. 2 S. 1 KSchG"), ("pers", f"{PB} › personenbedingt"),
       ("verh", f"{PB} › verhaltensbedingt: Abmahnung"), ("betr", f"{PB} › betriebsbedingt")], [
    *tafel("p12", "Sozialwidrig? § 1 Abs. 2 KSchG"),
    *w12,
    *grundkarte(0, "pers", "user-exclamation", GELB, "personenbedingt",
                [("Arbeit auf Dauer nicht", beim("pers", "Arbeit")), ("mehr möglich", beim("pers", "Arbeit"))]),
    *grundkarte(1, "verh", "alert-triangle", GELB, "verhaltensbedingt",
                [("Pflichten verletzt;", beim("verh", "verletzt")), ("in der Regel vorher", beim("verh", "Abmahnung")),
                 ("Abmahnung", beim("verh", "Abmahnung"))], fund=["BAG 2 AZR 541/09,", "Rn. 36 f."]),
    *grundkarte(2, "betr", "briefcase-off", BLAU, "betriebsbedingt",
                [("Arbeitsplatz fällt weg,", beim("betr", "Arbeitsplatz")), ("etwa: Abteilung", beim("betr", "Abteilung")),
                 ("schließt", beim("betr", "Abteilung"))]),
    *rechts_frei([*requisit([("p12", ("tabler", "scale", 100, WEISS), "sozial gerechtfertigt?", BLAU)]),
                  *zwei([("p12", "ruhig"), ("verh", "skeptisch"), ("betr", "sorge")], [("p12", "ruhig"), ("pers", "still")])]),
])
assert GY + GH <= 900, GY + GH

# ===========================================================================================================================
# G Begründung im Schreiben? Beweislast § 1 Abs. 2 S. 4 KSchG
# ===========================================================================================================================
W124 = ["„Der Arbeitgeber hat die Tatsachen zu beweisen, die die",
        "Kündigung bedingen.“"]
w124, w124_y = wortlaut(80, 380, 1100, W124, "§ 1 Abs. 2 S. 4 KSchG", "p124", marken=[
    (0, "Der Arbeitgeber", beim("p124", "Arbeitgeber")), (0, "zu beweisen", beim("p124", "beweisen"))], size=32)
folie([("begr", f"{PB} › Begründung im Schreiben?"), ("obj", f"{PB} › Grund muss vorliegen"),
       ("p124", f"{PB} › Beweislast, § 1 Abs. 2 S. 4 KSchG"), ("bwl", "Beweislast › Betriebsgröße: Arbeitnehmerin")], rechts_frei([
    *tafel("begr", "Begründung und Beweislast"),
    *neinz("Grund im Schreiben: grundsätzlich nicht nötig", 180, beim("begr2", "keinen"), "Bold", 34, x=160),
    zit("§ 623 BGB verlangt nur die Schriftform", 160, 232, beim("begr2", "Paragraf")),
    *okz("Ein Grund muss tatsächlich vorliegen", 295, "obj", "Bold", 34, x=160),
    *w124,
    z("Betriebsgröße (§ 23): grundsätzlich die Arbeitnehmerin", 110, w124_y + 30, "bwl", "Bold", 32),
    zit("BAG, Urt. v. 24.1.2013 – 2 AZR 140/12, Rn. 27", 110, w124_y + 76, "bwl"),
    z("Beweislast im Prozess: Video „Beweislast“", 110, w124_y + 140, "v141", "Bold", 30, farbe=TEXT),
    *requisit([("begr", ("tabler", "file-text", 100, WEISS), "kein Grund genannt", HELLROT),
               ("obj", ("tabler", "search", 100, WEISS), "Grund vorhanden?", WEISS),
               ("p124", ("tabler", "scale", 100, WEISS), "Beweis: Arbeitgeber", BLAU),
               ("bwl", ("tabler", "users", 110, WEISS), "Beweis: Arbeitnehmerin", GRUEN)]),
    *zwei([("begr", "skeptisch"), ("p124", "froh"), ("bwl", "ernst")], [("begr", "froh"), ("obj", "ernst"), ("p124", "still")]),
]))

# ===========================================================================================================================
# H1 Die Falle: Wortlautkarte § 4 S. 1 KSchG
# ===========================================================================================================================
PC = "Klagefrist"
W4 = ["„Will ein Arbeitnehmer geltend machen, dass eine Kündigung",
      "sozial ungerechtfertigt oder aus anderen Gründen",
      "rechtsunwirksam ist, so muss er innerhalb von drei Wochen",
      "nach Zugang der schriftlichen Kündigung Klage beim",
      "Arbeitsgericht auf Feststellung erheben, dass das",
      "Arbeitsverhältnis durch die Kündigung nicht aufgelöst ist.“"]
w4, w4_y = wortlaut(80, 165, 1100, W4, "§ 4 S. 1 KSchG", "p4", marken=[
    (1, "aus anderen Gründen", beim("p4", "anderen")), (2, "innerhalb von drei Wochen", beim("p4", "innerhalb")),
    (3, "nach Zugang der schriftlichen Kündigung", beim("p4", "Zugang")), (3, "Klage beim", beim("p4", "Klage")),
    (4, "Arbeitsgericht", beim("p4", "Klage"))], size=32)
folie([("falle", f"{PC} · die Falle"), ("p4", f"{PC} › § 4 S. 1 KSchG: drei Wochen")], rechts_frei([
    *tafel("falle", "Die Falle: § 4 S. 1 KSchG", fill=HELL),
    *w4,
    blk(110, w4_y + 40, 1040, 80, GELB, beim("p4", "aufgelöst"), [("Klage binnen 3 Wochen nach Zugang", "ExtraBold", 36, INK)]),
    *requisit([("falle", ("tabler", "alert-triangle", 100, GELB), "Achtung, Falle!", HELLROT),
               (beim("p4", "drei"), ("tabler", "hourglass", 90, GELB), "3 Wochen", GELB),
               (beim("p4", "Arbeitsgericht"), ("tabler", "building-bank", 120, BLAU), "Arbeitsgericht", WEISS)]),
    *allein("KO", [("falle", "skeptisch"), (beim("p4", "drei"), "schreck")]),
]))

# ===========================================================================================================================
# H2 Versäumt: § 7 KSchG, § 5 KSchG
# ===========================================================================================================================
W7 = ["„Wird die Rechtsunwirksamkeit einer Kündigung nicht",
      "rechtzeitig geltend gemacht (§ 4 Satz 1, §§ 5 und 6), so",
      "gilt die Kündigung als von Anfang an rechtswirksam; …“"]
w7, w7_y = wortlaut(80, 165, 1100, W7, "§ 7 KSchG", "p7", marken=[
    (1, "rechtzeitig", beim("p7", "rechtzeitig")), (2, "als von Anfang an rechtswirksam", beim("p7", "Anfang"))], size=34)
folie([("p7", f"{PC} › § 7 KSchG: gilt als wirksam"), ("p7b", f"{PC} › Grund dann egal"),
       ("p5", f"{PC} › § 5 KSchG: nachträgliche Zulassung")], rechts_frei([
    *tafel("p7", "Versäumt: § 7 KSchG"),
    *w7,
    blk(110, w7_y + 40, 1040, 80, HELLROT, "p7b", [("Ob es einen Grund gab: egal", "ExtraBold", 36, INK)]),
    z("§ 5 KSchG: nachträgliche Zulassung der Klage,", 110, w7_y + 170, "p5", "Bold", 34),
    z("wenn trotz aller zumutbaren Sorgfalt verhindert", 110, w7_y + 222, beim("p5", "Sorgfalt"), size=32),
    zit("§ 5 Abs. 1 S. 1 KSchG", 110, w7_y + 270, beim("p5", "Sorgfalt")),
    *requisit([("p7", ("tabler", "file-certificate", 100, HELLROT), "gilt als wirksam", HELLROT),
               ("p7b", ("tabler", "question-mark", 90, WEISS), "Grund egal", WEISS),
               ("p5", ("tabler", "first-aid-kit", 100, WEISS), "Ausnahme: § 5", GELB)]),
    *allein("KO", [("p7", "schreck"), ("p7b", "sorge"), ("p5", "skeptisch")]),
]))

# ===========================================================================================================================
# I Fristberechnung im Kalender Oktober 2026
# ===========================================================================================================================
KW_, KH_, KX0, KY0 = 148, 88, 115, 228       # Kalenderzelle: Breite, Höhe, links, oben
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
WOCHEN = [[(28, 0), (29, 0), (30, 0), (1, 1), (2, 1), (3, 1), (4, 1)], [(d, 1) for d in range(5, 12)],
          [(d, 1) for d in range(12, 19)], [(d, 1) for d in range(19, 26)], [(26, 1), (27, 1), (28, 1), (29, 1), (30, 1), (31, 1), (1, 0)]]
import datetime as _dt
assert _dt.date(2026, 10, 5).weekday() == 0 and _dt.date(2026, 10, 26).weekday() == 0 and _dt.date(2026, 9, 28).weekday() == 0


def zelle(tag):
    """(x, y) der Kalenderzelle eines Oktobertags."""
    for r, w in enumerate(WOCHEN):
        for c, (d, im_okt) in enumerate(w):
            if d == tag and im_okt:
                return KX0 + c * KW_, KY0 + r * KH_
    raise KeyError(tag)


def kalender(cue):
    s = 2
    im = Image.new("RGBA", (7 * KW_ * s + 8 * s, (5 * KH_ + 50) * s))
    dr = ImageDraw.Draw(im)
    fk, fz = F("Bold", 28 * s), F("Bold", 34 * s)
    for c, t in enumerate(TAGE):
        dr.text(((c * KW_ + KW_ / 2) * s, 22 * s), glyphen(t), font=fk, fill=TEXT if c >= 5 else INK, anchor="mm")
    for r, w in enumerate(WOCHEN):
        for c, (d, im_okt) in enumerate(w):
            x0, y0 = c * KW_ * s + 4 * s, (50 + r * KH_) * s
            dr.rounded_rectangle((x0, y0, x0 + (KW_ - 8) * s, y0 + (KH_ - 8) * s), 10 * s,
                                 fill=(255, 255, 255, 255) if im_okt else (238, 238, 234, 255), outline=INK, width=3 * s)
            dr.text((x0 + 14 * s, y0 + 8 * s), str(d), font=fz, fill=INK if im_okt else (150, 150, 150, 255))
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, KX0 - 4, KY0 - 50, cue, "fade", 0.0, None, name="kalender")


def markiere(tag, cue, fill, text=None, bis=None):
    """Farbige Fläche über einer Kalenderzelle (die Ziffer bleibt lesbar), optional mit kurzem Text (26 px)."""
    x, y = zelle(tag)
    im = Image.new("RGBA", (KW_ - 8, KH_ - 8))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 10, fill=fill[:3] + (255,), outline=INK, width=3)
    d_ = ImageDraw.Draw(im)
    d_.text((14, 8), str(tag), font=F("Bold", 34), fill=INK)
    if text:
        d_.text((im.width - 8, im.height - 6), glyphen(text), font=F("Bold", 26), fill=INK, anchor="rd")
    return El(im, x, y, cue, "pop", 0.0, bis, name=f"tag:{tag}")


folie([("frist", f"{PC} › Fristberechnung"), ("zug", f"{PC} › Zugang: Mo, 5.10.2026"),
       ("p187", f"{PC} › § 187 Abs. 1 BGB: Zugangstag zählt nicht"), ("p188", f"{PC} › § 188 Abs. 2 BGB: gleicher Wochentag"),
       ("ende", f"{PC} › Ende: Mo, 26.10.2026, 24 Uhr")], rechts_frei([
    *tafel("frist", "Fristberechnung: Oktober 2026"),
    kalender("frist"),
    markiere(5, "zug", GELB, "Zugang", bis="p187"),
    markiere(5, "p187", HELLGRAU),
    linienzug([(zelle(5)[0] + 8, zelle(5)[1] + 70), (zelle(5)[0] + 124, zelle(5)[1] + 8)], beim("p187", "zählt"), breite=4,
              farbe=DROT),
    markiere(12, beim("ende", "drei"), HELLGRUEN, "1 Wo."),
    markiere(19, beim("ende", "drei"), HELLGRUEN, "2 Wo."),
    markiere(26, beim("ende", "drei"), HELLROT, "3 Wo."),
    z("§ 187 Abs. 1 BGB: Tag des Zugangs zählt nicht mit", 110, 682, "p187", "Bold", 30),
    z("§ 188 Abs. 2 BGB: Ende am Tag mit derselben Benennung", 110, 728, "p188", "Bold", 30),
    blk(110, 785, 1040, 80, GELB, beim("ende", "Ablauf"), [("Klage bis Mo, 26.10.2026, 24 Uhr", "ExtraBold", 36, INK)]),
    *requisit([("frist", ("tabler", "calendar-event", 100, WEISS), "Wann endet die Frist?", WEISS),
               ("zug", ("tabler", "mail-opened", 100, WEISS), "Zugang Mo, 5.10.", GELB),
               ("p188", ("tabler", "calendar-week", 100, WEISS), "3 Wochen: Montag", WEISS),
               (beim("ende", "Ablauf"), ("tabler", "alarm", 100, HELLROT), "Mo, 26.10., 24 Uhr", HELLROT)]),
    *allein("KO", [("frist", "skeptisch"), ("zug", "ruhig"), (beim("ende", "Ablauf"), "ernst")]),
]))

# ===========================================================================================================================
# J Lösung
# ===========================================================================================================================
folie([("loes", "Lösung"), ("l1", "Lösung › KSchG anwendbar (+)"), ("l2", "Lösung › Arbeitsgericht entscheidet"),
       ("l4", "Lösung › Klage bis 26.10.2026"), ("l5", "Lösung › sonst § 7: wirksam")], rechts_frei([
    *tafel("loes", "Lösung"),
    *okz("KSchG anwendbar: § 1 Abs. 1 und § 23 Abs. 1 S. 3", 180, "l1", "Bold", 34, x=160),
    z("Sozial gerechtfertigt? Das entscheidet das Arbeitsgericht.", 110, 260, "l2", "Bold", 32),
    z("Herr Steinmetz muss einen Kündigungsgrund beweisen.", 110, 312, "l3", size=32),
    zit("§ 1 Abs. 2 S. 4 KSchG", 110, 358, "l3"),
    blk(110, 420, 1040, 80, GELB, "l4", [("Kornelia muss bis Mo, 26.10.2026 klagen", "ExtraBold", 36, INK)]),
    blk(110, 530, 1040, 120, HELLROT, "l5", [("Zu lange überlegt: wirksam,", "ExtraBold", 36, INK),
                                            ("auch ganz ohne Grund (§ 7 KSchG)", "ExtraBold", 36, INK)]),
    *requisit([("loes", ("tabler", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("l2", ("tabler", "building-bank", 120, BLAU), "Arbeitsgericht", WEISS),
               ("l4", ("tabler", "hourglass", 90, GELB), "bis 26.10.", GELB),
               ("l5", ("tabler", "file-certificate", 100, HELLROT), "§ 7 KSchG", HELLROT)]),
    *zwei([("loes", "ruhig"), ("l2", "skeptisch"), ("l4", "ernst"), ("l5", "sorge")],
          [("loes", "ruhig"), ("l3", "still"), ("l5", "skeptisch")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Prüfungsreihenfolge"), ("t5", "Klausurtipp · sonstige Gründe, § 102 BetrVG"),
       ("t6", "Klausurtipp · die Frist gehört an den Anfang")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe in dieser Reihenfolge:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("1. wirksame Kündigungserklärung", 200, 260, "t1", size=34),
    z("2. Klagefrist", 200, 310, "t2", size=34),
    z("3. Anwendbarkeit des KSchG", 200, 360, "t3", size=34),
    z("4. Sozialwidrigkeit", 200, 410, "t4", size=34),
    z("5. sonstige Unwirksamkeitsgründe,", 200, 460, "t5", size=34),
    z("z. B. Anhörung des Betriebsrats, § 102 BetrVG", 240, 508, beim("t5", "Anhörung"), size=30),
    linienzug([(130, 575), (1130, 575)], "t6", breite=3),
    z("Die Frist gehört an den Anfang:", 200, 600, "t6", "Bold", 36),
    z("versäumt: Kündigung gilt als wirksam (§ 7)", 200, 658, beim("t6", "versäumt"), size=34),
    z("übrige Gründe grundsätzlich unerheblich", 200, 710, beim("t6", "übrigen"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Wirksame Kündigungserklärung", True),
          ("s1", 1, "schriftlich (§ 623 BGB) und zugegangen", False),
          ("s2", 0, "II. Klagefrist, §§ 4, 7 KSchG", True),
          ("s2", 1, "3 Wochen nach Zugang der schriftlichen Kündigung", False),
          ("s3", 0, "III. Anwendbarkeit des KSchG", True),
          ("s3a", 1, "persönlich: Wartezeit, § 1 Abs. 1 KSchG", False),
          ("s3b", 1, "betrieblich: in der Regel mehr als 10 Arbeitnehmer, § 23 Abs. 1 S. 3 KSchG", False),
          ("s4", 0, "IV. Soziale Rechtfertigung, § 1 Abs. 2 KSchG", True),
          ("s4a", 1, "personen-, verhaltens- oder betriebsbedingt", False),
          ("s5", 0, "V. Sonstige Unwirksamkeitsgründe", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Wirksamkeit der Kündigung"), 110, 90, "sch", 46),
           z("§§ 1, 4, 7, 23 KSchG; § 623 BGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 235
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 72, 1: 64}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Kündigungserklärung"), ("s2", "Prüfschema › II. Klagefrist"),
       ("s3", "Prüfschema › III. Anwendbarkeit"), ("s4", "Prüfschema › IV. Soziale Rechtfertigung"),
       ("s5", "Prüfschema › V. Sonstige Unwirksamkeitsgründe")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Nach mehr als 6 Monaten schützt", 0)], [("das KSchG in Betrieben mit", 0)],
                 [("in der Regel ", 0), ("mehr als 10", "a"), (" Arbeitnehmern.", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "mehr", nr=2)}),
    *markertext([[("Doch nur wer innerhalb von", 0)], [("3 Wochen klagt", "b"), (",", 0)],
                 [("kann sich darauf berufen.", 0)]], 750, 580, 44, "m2", {"b": beim("m2", "drei")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
