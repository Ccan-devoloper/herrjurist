"""Folge 215 · Differenzhypothese und Naturalrestitution: Schadensrecht §§ 249 ff. BGB – Schema – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Hedi stellt ihr Rad vor einer Bäckerei ab; Ludolf parkt rückwärts aus und fährt es an. In der Werkstatt von Trude
kostet die Reparatur 400 € plus 76 € Umsatzsteuer; ein gleichwertiges Rad 900 €. Ludolf will den Schwager reparieren lassen,
Hedi will das Geld. Abwandlung: Reparatur 1.200 €.
Szenen laut ../SZENENPLAN.md. Zwei Handlungsgeräusche (Aufprall, Ratsche; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 209 (gemeinsame Dateien unverändert); neu: baeckerei(), werkstatt(), buegel(), rad(), ticon().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026): § 249 Abs. 1, § 249 Abs. 2 Satz 1 und 2,
§ 251 Abs. 1, § 251 Abs. 2 Satz 1 BGB. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_215/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_215/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149/196) ------------------------------------
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




def pkt(text, y, cue, stil="Regular", size=34, x=185, **k):
    """Tafelzeile mit Aufzählungspunkt (Kriterium oder Argument, keine Bewertung)."""
    return [z("•", x - 38, y, cue, "ExtraBold", size), z(text, x, y, cue, stil, size, **k)]



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HD": "Hedi", "LU": "Ludolf", "TR": "Trude"}
NFARBE = {"HD": BLAU, "LU": GRUEN, "TR": GELB}


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


def zwei(k1, folge1, k2, folge2):
    """Zwei Figuren neben der Tafel, beide blicken nach links zur Tafel."""
    return [*stehend(k1, X1, folge1), *stehend(k2, X2, folge2)]




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
WAND = (236, 230, 220, 255)
WAND2 = (226, 240, 228, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
ORANGE = (244, 162, 89, 255)


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    """Boden in Seitenansicht: Tuschelinie, optional Fläche darunter."""
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def weg(e, s0, s1, dx, dy=0):
    """Bewegung: bis s0 um (dx, dy) versetzt, bis s1 an die Endposition (Renderer: versatz())."""
    e.weg = (s0, s1, dx, dy)
    return e


def ticon(*a, **k):
    """Requisit auf der Tafel (Teil der Tafelgrafik, deshalb von rechts_frei() ausgenommen)."""
    e = ficon(*a, **k)
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


def rad(cx, unten, breite, c, winkel=0, fuell=None, bis=None, anim="pop", tafel=False):
    """Fahrrad (Phosphor bicycle-bold, ohne Fahrerfigur); winkel ≠ 0 = schief/umgefallen nach dem Anfahren (gedreht, nicht umgezeichnet)."""
    e = (ticon if tafel else ficon)("ph", "bicycle-bold", cx, unten, breite, c, fuell=fuell, bis=bis, anim=anim)
    if winkel:
        sp = e.sprite.rotate(winkel, expand=True, resample=Image.BICUBIC)
        e.sprite = sp.crop(sp.getbbox())
        e.x, e.y = int(cx - e.sprite.width / 2), int(unten - e.sprite.height)
    return e


def buegel(cx, c, b=150, h=170):
    """Anlehnbügel eines Fahrradständers (umgedrehtes U, Tuschelinie)."""
    im = Image.new("RGBA", (b + 12, h + 6))
    dr = ImageDraw.Draw(im)
    r = b // 2
    dr.line((6, h, 6, r), fill=(120, 120, 128, 255), width=12)
    dr.line((b + 6, h, b + 6, r), fill=(120, 120, 128, 255), width=12)
    dr.arc((6, 6, b + 6, 2 * r), 180, 360, fill=(120, 120, 128, 255), width=12)
    return hart(El(im, cx - b // 2 - 6, G0 - h, c, "cut", 0.0, None, name="buegel"))


def baeckerei(c, x=70, w=640, h=520):
    """Bäckerei von außen: Wand, gestreifte Markise, Schaufenster, Tür, Schild (Grundformen)."""
    els = [hart(boden_(G0, c, fill=(226, 226, 222, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 40, w - 1, h - 1), 12, fill=WAND, outline=INK, width=5)
    for i in range(8):                                        # Markise
        dr.rectangle((i * w // 8, 70, (i + 1) * w // 8, 140), fill=(ROT if i % 2 == 0 else WEISS))
    dr.rectangle((0, 70, w - 1, 140), outline=INK, width=5)
    dr.rounded_rectangle((40, 190, 360, 430), 8, fill=HELLBLAU, outline=INK, width=5)   # Schaufenster
    dr.rounded_rectangle((430, 200, 580, h - 1), 8, fill=(190, 135, 90, 255), outline=INK, width=5)   # Tür
    dr.ellipse((550, 350, 564, 364), fill=INK)
    dr.rounded_rectangle((170, 0, 470, 60), 14, fill=GELB, outline=INK, width=5)            # Schild
    f = F("ExtraBold", 36); t = glyphen("Bäckerei")
    dr.text((320 - f.getlength(t) / 2, 6), t, font=f, fill=INK)
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="baeckerei")))
    els.append(hart(ficon("tabler", "bread", x + 200, G0 - h + 410, 150, c, fuell=GELB, anim="cut")))
    return els


def werkstatt(c, x=70, w=1000, h=560):
    """Fahrradwerkstatt von innen: Rückwand mit Lochwand, Werkbank (Grundformen, Werkzeug als Tabler-Icons)."""
    els = [hart(boden_(G0, c, fill=(220, 220, 214, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=WAND2, outline=INK, width=5)
    dr.rounded_rectangle((60, 50, 520, 260), 10, fill=(214, 160, 110, 255), outline=INK, width=5)   # Lochwand
    for yy in range(80, 250, 30):
        for xx in range(90, 500, 30):
            dr.ellipse((xx - 3, yy - 3, xx + 3, yy + 3), fill=(150, 105, 70, 255))
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="werkstatt")))
    els.append(hart(ficon("tabler", "tools", x + 180, G0 - h + 220, 130, c, fuell=None, anim="cut")))
    els.append(hart(ficon("tabler", "hammer", x + 390, G0 - h + 220, 120, c, fuell=None, anim="cut")))
    # Montageständer: Fuß und Stange, Rad oben eingespannt
    st = Image.new("RGBA", (160, 260)); d2 = ImageDraw.Draw(st)
    d2.rectangle((70, 0, 90, 250), fill=(120, 120, 128, 255), outline=INK, width=3)
    d2.rectangle((0, 240, 159, 259), fill=(120, 120, 128, 255), outline=INK, width=3)
    els.append(hart(El(st, x + 760 - 80, G0 - 260, c, "cut", 0.0, None, name="staender")))
    return els


def trenner(c):
    im = Image.new("RGBA", (8, 560)); ImageDraw.Draw(im).rectangle((0, 0, 7, 559), fill=INK)
    return hart(El(im, 956, G0 - 560, c, "cut", 0.0, None, name="trenner"))


_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# A1 Fall: das Rad vor der Bäckerei wird angefahren
# ===========================================================================================================================
RX, HX1, AX, LX1 = 860, 470, 1260, 1690           # Rad, Hedi, Auto (Endposition), Ludolf
T_AN = beim("stoss", "Rad", ende=True)              # Auto erreicht das Rad
_auto = ficon("tabler", "car", AX, G0 + 4, 440, "stoss", fuell=ORANGE, anim="cut")
weg(_auto, "stoss", T_AN, 400)
folie([(NULL, "Fall · Das Rad"), ("stoss", "Fall · Ludolf parkt aus"), ("kaputt", "Fall · Das Rad ist kaputt"),
       ("lu1", "Fall · Ludolf: „Das bringe ich in Ordnung“")], [
    *baeckerei(NULL),
    buegel(RX, NULL),
    pl("Dein Fahrrad wird angefahren", 760, 30, beim("fall", "angefahren"), fill=GELB, size=32),
    pl("Reparatur oder Geld?", 760, 100, beim("fall", "Reparatur"), fill=WEISS, size=32),
    rad(RX, G0, 320, NULL, fuell=None, bis=T_AN),
    szene(rad(RX - 30, G0, 320, T_AN, winkel=-24, fuell=None, anim="cut"), "215crash*", 0.55),
    *fig("HD", HX1, G0, FHA, [(beim("hedi", "Hedi"), "froh_r"), (T_AN, "schreck_r"), ("lu1", "sorge_r")]),
    ns("Hedi", HX1, G0, beim("hedi", "Hedi"), BLAU, d=0.1),
    _auto,
    pl("Ludolf parkt rückwärts aus", AX + 60, 470, beim("stoss", "parkt"), fill=WEISS, size=28, anker="m", bis="lu1"),
    pl("Rahmen verbogen, Hinterrad kaputt", RX + 90, 545, beim("kaputt", "Rahmen"), fill=HELLROT, size=28, anker="m"),
    *redet("LU_klagt", LX1, G0, FHA, "lu1", "werk"),
    ns("Ludolf", LX1, G0, "lu1", GRUEN),
    blase("sprech", 760, 200, "lu1", 1350, 250, inhalt=["Oh nein, das tut mir leid! Das", "bringe ich wieder in Ordnung."],
          textsize=34, figur=("LU_klagt", LX1, G0, FHA), bis="werk"),
])

# ===========================================================================================================================
# A2 Fall: in der Werkstatt von Trude
# ===========================================================================================================================
TX2, HX2, BX2 = 1270, 1690, 830
folie([("werk", "Fall · In der Werkstatt"), ("tr1", "Fall · 400 € plus 76 € Umsatzsteuer"),
       ("wert", "Fall · Gleichwertiges Rad: 900 €")], [
    *werkstatt("werk"),
    hart(rad(BX2, G0 - 260 + 30, 280, "werk", winkel=-8, anim="cut")),
    *fig("HD", HX2, G0, FHA, [("werk", "sorge"), ("wert", "denkt")], erst="cut"),
    ns("Hedi", HX2, G0, "werk", BLAU),
    *fig("TR", TX2, G0, FHA, [(beim("werk", "Trude"), "denkt")], bis="tr1"),
    szene(ficon("tabler", "tool", BX2 + 160, G0 - 300, 80, beim("werk", "Trude"), fuell=None), "215ratsche*", 0.40),
    *redet("TR_redet_r", TX2, G0, FHA, "tr1", "wert"),
    *fig("TR", TX2, G0, FHA, [("wert", "ruhig_r")], erst="cut"),
    ns("Trude", TX2, G0, beim("werk", "Trude"), GELB, d=0.1),
    blase("sprech", 760, 200, "tr1", 1400, 230, inhalt=["Die Reparatur kostet 400 €,", "plus 76 € Umsatzsteuer."],
          textsize=34, figur=("TR_redet_r", TX2, G0, FHA), bis="wert"),
    pl("Gleichwertiges Rad: 900 €", 70, 30, beim("wert", "gleichwertiges"), fill=GRUEN, size=32),
    rad(560, 160, 150, beim("wert", "gleichwertiges"), fuell=GRUEN),
])

# ===========================================================================================================================
# A3 Fall: geteiltes Bild – Ludolf und der Schwager, Hedi will das Geld; die Frage
# ===========================================================================================================================
LX3, HX3 = 600, 1480
folie([("idee", "Fall · Ludolf hat eine Idee"), ("lu2", "Fall · Der Schwager"), ("he1", "Fall · Hedi will das Geld"),
       ("frage", "Fall · Die Frage")], [
    hart(boden_(G0, "idee", fill=(226, 226, 222, 255), h=100)),
    trenner("idee"),
    hart(ficon("tabler", "car", 250, G0 + 4, 360, "idee", fuell=ORANGE, anim="cut")),
    ficon("tabler", "bulb", LX3, 400, 90, beim("idee", "Idee"), fuell=GELB, bis="lu2"),
    ficon("tabler", "phone", 830, 600, 80, "lu2", fuell=WEISS),
    ficon("tabler", "phone", 1090, 600, 80, "he1", fuell=WEISS),
    *fig("LU", LX3, G0, FHA, [("idee", "froh_r")], bis="lu2", erst="cut"),
    *redet("LU_redet_r", LX3, G0, FHA, "lu2", "he1"),
    *fig("LU", LX3, G0, FHA, [("he1", "schreck_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Ludolf", LX3, G0, "idee", GRUEN),
    hart(rad(1770, G0, 220, "idee", winkel=-20, anim="cut")),
    *fig("HD", HX3, G0, FHA, [("idee", "ruhig")], bis="he1", erst="cut"),
    *redet("HD_redet", HX3, G0, FHA, "he1", "frage"),
    *fig("HD", HX3, G0, FHA, [("frage", "ernst")], erst="cut"),
    ns("Hedi", HX3, G0, "idee", BLAU),
    blase("sprech", 700, 200, "lu2", 560, 210, inhalt=["Mein Schwager repariert Räder.", "Der macht das für mich."],
          textsize=34, figur=("LU_redet_r", LX3, G0, FHA), bis="he1"),
    blase("sprech", 820, 260, "he1", 1400, 230, inhalt=["Nein danke. Ich will das Geld.", "Was ich damit mache,",
                                                       "entscheide ich."],
          textsize=34, figur=("HD_redet", HX3, G0, FHA), bis="frage"),
    pl("Muss Hedi sich auf den Schwager einlassen?", 70, 30, "frage", fill=PINK, size=32),
    pl("Wie viel Geld bekommt sie ohne Reparatur?", 70, 105, "frage2", fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_215(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_215("sv", [
    "Hedi stellt ihr Fahrrad vor einer Bäckerei ab. Ludolf parkt rückwärts aus und fährt das Rad an: Der Rahmen ist "
    "verbogen, das Hinterrad kaputt. Ludolf sagt: „Das bringe ich wieder in Ordnung.“",
    "In der Werkstatt von Trude kostet die Reparatur 400 € plus 76 € Umsatzsteuer. Ein gleichwertiges Rad würde 900 € "
    "kosten.",
    "Ludolf will das Rad von seinem Schwager reparieren lassen. Hedi lehnt ab: „Ich will das Geld. Was ich damit mache, "
    "entscheide ich.“",
], "Muss Hedi den Schwager hinnehmen, und wie viel Geld bekommt sie?")

# ===========================================================================================================================
# C Haftungsgrund vorausgesetzt
# ===========================================================================================================================
PC = "Haftungsgrund (vorausgesetzt)"
folie([("grund", f"{PC} › etwa § 823 Abs. 1 BGB"), ("grund2", "Rechtsfolge: Schaden und Ersatz"),
       ("sys", "Rechtsfolge: Schaden und Ersatz › Anspruchsgrundlagen: Video 046")], rechts_frei([
    *tafel("grund", "Haftungsgrund vorausgesetzt", h=600),
    z("etwa § 823 Abs. 1 BGB:", 110, 190, beim("grund", "Paragraf"), "ExtraBold", 36),
    z("Ludolf hat fahrlässig das Eigentum", 110, 245, beim("grund", "fahrlässig"), "Regular", 34),
    z("von Hedi verletzt", 110, 292, beim("grund", "fahrlässig"), "Regular", 34),
    blk(110, 370, 1040, 170, GELB, "grund2", [("Heute: die Rechtsfolge", "ExtraBold", 38, INK),
                                            ("Was ist der Schaden? Wie wird er ersetzt?", "Bold", 32, INK)]),
    zit("Anspruchsgrundlagen: Video „Schadensersatz-Schema, §§ 280 ff. BGB“", 110, 575, "sys"),
    *requisit([("grund", ("tabler", "car-crash", 130, ORANGE), "Haftung: vorausgesetzt", WEISS),
               ("grund2", ("tabler", "scale", 120, WEISS), "Rechtsfolge", GELB)]),
    *zwei("HD", [("grund", "ernst"), ("grund2", "ruhig")], "LU", [("grund", "still"), ("sys", "ruhig")]),
]))

# ===========================================================================================================================
# D 1. Schaden: Differenzhypothese
# ===========================================================================================================================
PD = "Rechtsfolge › 1. Schaden: Differenzhypothese"
folie([("dh", PD), ("dh2", f"{PD} › tatsächliche Lage"), ("dh3", f"{PD} › Lage ohne den Unfall"),
       ("dh4", f"{PD} › BGH"), ("dh5", f"{PD} › der Fall"), ("dh6", f"{PD} › Differenz = Schaden")], rechts_frei([
    *tafel("dh", "1. Schaden: Differenzhypothese"),
    blk(110, 180, 500, 120, HELLROT, "dh2", [("tatsächliche Lage", "ExtraBold", 32, INK), ("nach dem Unfall", "Regular", 30, INK)]),
    blk(650, 180, 500, 120, HELLGRUEN, "dh3", [("hypothetische Lage", "ExtraBold", 32, INK), ("ohne den Unfall", "Regular", 30, INK)]),
    z("–", 614, 215, "dh3", "ExtraBold", 40),
    zit("so der BGH, Urt. v. 16.7.2024 – VI ZR 239/23, Rn. 8", 110, 320, beim("dh4", "Bundesgerichtshof")),
    rad(900, 540, 230, beim("dh5", "heiles"), fuell=GRUEN, tafel=True),
    z("heiles Rad", 820, 560, beim("dh5", "heiles"), "Bold", 32),
    rad(360, 540, 230, beim("dh5", "beschädigtes"), winkel=-24, tafel=True),
    z("beschädigtes Rad", 225, 560, beim("dh5", "beschädigtes"), "Bold", 32),
    blk(110, 660, 1040, 120, GELB, "dh6", [("Differenz = Schaden", "ExtraBold", 40, INK)]),
    *requisit([("dh", ("tabler", "scale", 120, WEISS), "Schaden?", WEISS),
               ("dh2", ("ph", "bicycle-bold", 140, HELLROT), "nach dem Unfall", HELLROT),
               ("dh3", ("ph", "bicycle-bold", 140, GRUEN), "ohne den Unfall", GRUEN),
               ("dh6", ("tabler", "equal", 90, None), "Schaden", GELB)]),
    *zwei("HD", [("dh", "ruhig"), ("dh5", "sorge"), ("dh6", "ernst")], "LU", [("dh", "ruhig"), ("dh2", "denkt")]),
]))

# ===========================================================================================================================
# E 2. Herstellung, § 249 Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W2491 = umbruch("„Wer zum Schadensersatz verpflichtet ist, hat den Zustand herzustellen, der bestehen würde, wenn der zum "
                "Ersatz verpflichtende Umstand nicht eingetreten wäre.“", 32, 1040)
w2491, w2491_y = wortlaut(80, 180, 1100, W2491, "§ 249 Abs. 1 BGB", beim("w1", "Paragraf"),
                          marken=[(_zl(W2491, "Zustand"), "Zustand herzustellen", beim("w1", "Zustand")),
                                  (_zl(W2491, "nicht eingetreten"), "nicht eingetreten", beim("w1", "nicht", nr=1))], size=32)
PE = "Rechtsfolge › 2. Herstellung, § 249 Abs. 1 BGB"
folie([("w1", PE), ("nr", f"{PE} › Naturalrestitution"), ("nr2", f"{PE} › Ludolf könnte selbst reparieren lassen")], rechts_frei([
    *tafel("w1", "2. Wie wird ersetzt?"),
    *w2491,
    blk(110, w2491_y + 40, 1040, 150, GELB, "nr", [("Naturalrestitution:", "ExtraBold", 38, INK),
                                                  ("grundsätzlich Herstellung, nicht Geld", "Bold", 34, INK)]),
    *pkt("nach Abs. 1 allein: Ludolf lässt das Rad", w2491_y + 230, "nr2", "Bold", 32, x=160),
    z("selbst reparieren, etwa beim Schwager", 160, w2491_y + 278, "nr2", "Bold", 32),
    *requisit([(beim("w1", "herzustellen"), ("tabler", "tools", 120, None), "Herstellung", WEISS),
               ("nr2", ("tabler", "tool", 100, None), "der Schwager?", WEISS)]),
    *zwei("HD", [("w1", "ruhig"), ("nr2", "sorge")], "LU", [("w1", "ruhig"), ("nr2", "froh")]),
]))
assert w2491_y + 330 <= 900, w2491_y

# ===========================================================================================================================
# F 3. Geld statt Herstellung, § 249 Abs. 2 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W24921 = umbruch("„Ist wegen Verletzung einer Person oder wegen Beschädigung einer Sache Schadensersatz zu leisten, so kann der "
                 "Gläubiger statt der Herstellung den dazu erforderlichen Geldbetrag verlangen.“", 32, 1040)
w24921, w24921_y = wortlaut(80, 180, 1100, W24921, "§ 249 Abs. 2 Satz 1 BGB", "w2",
                            marken=[(_zl(W24921, "Beschädigung"), "Beschädigung einer", beim("w2", "Beschädigung")),
                                    (_zl(W24921, "statt der"), "statt der", beim("w2", "statt")),
                                    (_zl(W24921, "erforderlichen"), "erforderlichen Geldbetrag", beim("w2", "erforderlichen"))],
                            size=32)
PF = "Rechtsfolge › 3. Geld statt Herstellung, § 249 Abs. 2 Satz 1 BGB"
folie([("w2", PF), ("wahl", f"{PF} › Ersetzungsbefugnis"), ("wahl2", f"{PF} › kein Schwager"),
       ("erf", f"{PF} › erforderlich: 400 €")], rechts_frei([
    *tafel("w2", "3. Geld statt Herstellung"),
    *w24921,
    *okz("Wahl bei Hedi: Ersetzungsbefugnis", w24921_y + 40, "wahl", "Bold", 32, x=160),
    zit("BGH, Urt. v. 19.2.2013 – VI ZR 69/12, Rn. 9", 160, w24921_y + 88, beim("wahl", "Ersetzungsbefugnis")),
    *okz("den Schwager muss sie nicht hinnehmen", w24921_y + 150, "wahl2", "Bold", 32, x=160),
    *pkt("erforderlich: was ein verständiger, wirtschaftlich", w24921_y + 230, "erf", "Regular", 32, x=160),
    z("denkender Eigentümer aufwenden würde", 160, w24921_y + 276, "erf", "Regular", 32),
    z("hier: Reparatur für 400 €", 160, w24921_y + 330, beim("erf", "hier"), "ExtraBold", 34),
    zit("BGH, Urt. v. 28.1.2025 – VI ZR 300/24, Rn. 11", 160, w24921_y + 382, beim("erf", "verständiger")),
    *requisit([(beim("w2", "statt"), ("tabler", "coin-euro", 110, GELB), "Geld statt Herstellung", GELB),
               ("wahl", ("tabler", "arrows-split", 110, None), "Hedi wählt", WEISS),
               ("wahl2", ("tabler", "hand-stop", 110, WEISS), "kein Schwager", HELLROT),
               ("erf", ("tabler", "calculator", 100, WEISS), "400 €", GRUEN)]),
    *zwei("HD", [("w2", "ruhig"), ("wahl", "froh"), ("erf", "ruhig")], "LU", [("w2", "ruhig"), ("wahl2", "sorge")]),
]))
assert w24921_y + 430 <= 920, w24921_y

# ===========================================================================================================================
# G fiktive Abrechnung, § 249 Abs. 2 Satz 2 BGB (Wortlautkarte)
# ===========================================================================================================================
W24922 = umbruch("„Bei der Beschädigung einer Sache schließt der nach Satz 1 erforderliche Geldbetrag die Umsatzsteuer nur mit "
                 "ein, wenn und soweit sie tatsächlich angefallen ist.“", 31, 1040)
PG = "Rechtsfolge › 3. Geld statt Herstellung"
w24922, w24922_y = wortlaut(80, 400, 1100, W24922, "§ 249 Abs. 2 Satz 2 BGB", "w3",
                            marken=[(_zl(W24922, "tatsächlich"), "tatsächlich", beim("w3", "tatsächlich"))], size=31)
folie([("fik", f"{PG} › ohne Reparatur?"), ("fik2", f"{PG} › fiktive Abrechnung"),
       ("w3", f"{PG} › Umsatzsteuer, § 249 Abs. 2 Satz 2 BGB"), ("ust", f"{PG} › fiktiv: 400 €"),
       ("ust2", f"{PG} › mit Reparatur: plus 76 €")], rechts_frei([
    *tafel("fik", "Ohne Reparatur: fiktiv abrechnen"),
    z("Und wenn Hedi gar nicht reparieren lässt?", 110, 180, "fik", "Bold", 32),
    *okz("darf sie: in der Verwendung des Geldes frei", 240, beim("fik2", "Sie"), "Bold", 32, x=160),
    z("fiktiv: nach den geschätzten Reparaturkosten", 160, 288, beim("fik2", "fiktiv"), "Regular", 32),
    zit("BGH, Urt. v. 23.5.2017 – VI ZR 9/17, Rn. 7; VI ZR 300/24, Rn. 12", 160, 338, beim("fik2", "fiktiv")),
    *w24922,
    z("fiktiv abgerechnet:", 160, w24922_y + 30, "ust", "Regular", 34),
    z("400 €", 760, w24922_y + 30, beim("ust", "vierhundert"), "ExtraBold", 34),
    z("repariert, Umsatzsteuer angefallen:", 160, w24922_y + 85, "ust2", "Regular", 34),
    z("+ 76 €", 760, w24922_y + 85, beim("ust2", "sechsundsiebzig"), "ExtraBold", 34),
    zit("BGH, Urt. v. 24.1.2017 – VI ZR 146/16, Rn. 9", 160, w24922_y + 140, beim("ust2", "sechsundsiebzig")),
    *requisit([("fik", ("tabler", "tools", 120, None), "Reparatur?", WEISS),
               ("fik2", ("tabler", "cash-banknote", 120, GRUEN), "fiktiv abrechnen", GRUEN),
               ("w3", ("tabler", "receipt-tax", 100, WEISS), "Umsatzsteuer", GELB),
               ("ust2", ("tabler", "receipt-euro", 100, WEISS), "mit Reparatur: + 76 €", GELB)]),
    *zwei("HD", [("fik", "denkt"), ("fik2", "froh"), ("ust2", "ruhig")], "LU", [("fik", "ruhig"), ("ust", "denkt")]),
]))
assert w24922_y + 240 <= 920, w24922_y

# ===========================================================================================================================
# H § 250 BGB
# ===========================================================================================================================
folie([("p250", "Rechtsfolge › 3. Geld statt Herstellung › § 250 BGB")], rechts_frei([
    *tafel("p250", "Wo Abs. 2 nicht greift: § 250 BGB", h=420),
    z("§ 250 BGB führt zum Geld:", 110, 190, beim("p250", "Paragraf"), "ExtraBold", 36),
    *pkt("Frist zur Herstellung", 265, beim("p250", "Frist"), "Bold", 34, x=160),
    *pkt("mit der Erklärung, sie danach abzulehnen", 330, beim("p250", "Erklärung"), "Bold", 34, x=160),
    *requisit([("p250", ("tabler", "hourglass", 100, HELLBLAU), "§ 250 BGB", WEISS)]),
    *zwei("HD", [("p250", "ruhig")], "LU", [("p250", "ruhig")]),
]))

# ===========================================================================================================================
# I 4. Geldentschädigung, § 251 Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W2511 = umbruch("„Soweit die Herstellung nicht möglich oder zur Entschädigung des Gläubigers nicht genügend ist, hat der "
                "Ersatzpflichtige den Gläubiger in Geld zu entschädigen.“", 32, 1040)
w2511, w2511_y = wortlaut(80, 180, 1100, W2511, "§ 251 Abs. 1 BGB", beim("w4", "Paragraf"),
                          marken=[(_zl(W2511, "nicht möglich"), "nicht möglich", beim("w4", "möglich")),
                                  (_zl(W2511, "genügend"), "nicht genügend", beim("w4", "genügend")),
                                  (_zl(W2511, "Geld zu"), "Geld", beim("w4", "Geld", nr=2))], size=32)
PI = "Rechtsfolge › 4. Geldentschädigung, § 251 BGB"
folie([("w4", f"{PI} › Abs. 1"), ("mmw", f"{PI} › Abs. 1: merkantiler Minderwert")], rechts_frei([
    *tafel("w4", "4. Wann gibt es von vornherein Geld?", size=44),
    *w2511,
    *pkt("beim Auto: merkantiler Minderwert", w2511_y + 50, "mmw", "Bold", 34, x=160),
    z("Unfallwagen bleibt trotz Reparatur weniger wert", 160, w2511_y + 100, beim("mmw", "Unfallwagen"), "Regular", 32),
    zit("BGH, Urt. v. 16.7.2024 – VI ZR 239/23, Rn. 6 f.", 160, w2511_y + 150, beim("mmw", "Unfallwagen")),
    *requisit([("w4", ("tabler", "coin-euro", 110, GELB), "von vornherein Geld?", WEISS),
               ("mmw", ("tabler", "car", 180, ORANGE), "merkantiler Minderwert", WEISS)]),
    *zwei("HD", [("w4", "ruhig"), ("mmw", "denkt")], "LU", [("w4", "ruhig"), ("mmw", "still")]),
]))
assert w2511_y + 200 <= 900

# ===========================================================================================================================
# J § 251 Abs. 2 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W2512 = umbruch("„Der Ersatzpflichtige kann den Gläubiger in Geld entschädigen, wenn die Herstellung nur mit "
                "unverhältnismäßigen Aufwendungen möglich ist.“", 32, 1040)
w2512, w2512_y = wortlaut(80, 180, 1100, W2512, "§ 251 Abs. 2 Satz 1 BGB", "w5",
                          marken=[(_zl(W2512, "unverhältnismäßigen"), "unverhältnismäßigen Aufwendungen",
                                   beim("w5", "unverhältnismäßigen"))], size=32)
folie([("w5", f"{PI} › Abs. 2 Satz 1"), ("vor", f"{PI} › Vorrang der Herstellung")], rechts_frei([
    *tafel("w5", "4. Unverhältnismäßige Aufwendungen"),
    *w2512,
    blk(110, w2512_y + 50, 1040, 150, HELLBLAU, "vor", [("Erst diese Grenze beendet den", "ExtraBold", 34, INK),
                                                       ("Vorrang der Herstellung", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 23.5.2017 – VI ZR 9/17, Rn. 6", 110, w2512_y + 220, beim("vor", "Bundesgerichtshof")),
    *requisit([("w5", ("tabler", "scale", 120, WEISS), "unverhältnismäßig?", HELLROT),
               ("vor", ("tabler", "tools", 120, None), "Herstellung zuerst", GELB)]),
    *zwei("HD", [("w5", "ruhig"), ("vor", "denkt")], "LU", [("w5", "denkt"), ("vor", "ruhig")]),
]))

# ===========================================================================================================================
# K Abwandlung: Reparatur 1.200 €
# ===========================================================================================================================
PK = "Abwandlung · Reparatur 1.200 €"
folie([("var", PK), ("var2", f"{PK} › Ersatzrad 900 €"), ("var3", f"{PK} › wirtschaftlicherer Weg"),
       ("var4", f"{PK} › abzüglich Restwert"), ("var5", f"{PK} › 850 €"), ("kfz", f"{PK} › Auto: 130 %"),
       ("kfz2", f"{PK} › 1.200 € läge darüber")], rechts_frei([
    *tafel("var", "Abwandlung: Reparatur für 1.200 €"),
    z("Reparatur:", 160, 180, "var", "Regular", 34),
    z("1.200 €", 820, 180, beim("var", "tausend"), "Bold", 34),
    z("gleichwertiges Rad:", 160, 235, "var2", "Regular", 34),
    z("900 €", 820, 235, beim("var2", "neunhundert"), "Bold", 34),
    *okz("Ersatzrad ist auch Herstellung:", 305, "var3", "Bold", 32, x=160),
    z("Hedi muss den wirtschaftlicheren Weg wählen", 160, 352, beim("var3", "Hedi"), "Regular", 32),
    zit("BGH, Urt. v. 25.3.2025 – VI ZR 174/24, Rn. 21", 160, 400, beim("var3", "Hedi")),
    z("900 € – Restwert 50 €", 160, 465, "var4", "Regular", 34),
    linienzug([(160, 520), (1060, 520)], "var5", breite=3),
    blk(110, 535, 1040, 100, GRUEN, "var5", [("Hedi bekommt 850 €", "ExtraBold", 38, INK)]),
    *pkt("Auto: Reparatur bis 130 % des", 665, "kfz", "Bold", 32, x=160),
    z("Wiederbeschaffungswerts, wenn fachgerecht repariert", 160, 711, beim("kfz", "Wiederbeschaffungswerts"), "Regular", 32),
    zit("BGH, Urt. v. 2.6.2015 – VI ZR 387/14, Rn. 6 f.", 160, 760, beim("kfz", "fachgerecht")),
    *pkt("1.200 € läge auch darüber", 815, "kfz2", "Bold", 32, x=160),
    *requisit([("var", ("tabler", "tools", 120, None), "1.200 €", HELLROT),
               ("var2", ("ph", "bicycle-bold", 150, GRUEN), "Ersatzrad: 900 €", GRUEN),
               ("var4", ("tabler", "recycle", 100, None), "Restwert 50 €", WEISS),
               ("var5", ("tabler", "cash-banknote", 120, GRUEN), "850 €", GRUEN),
               ("kfz", ("tabler", "car", 180, ORANGE), "Auto: 130 %", WEISS)]),
    *zwei("HD", [("var", "sorge"), ("var5", "ruhig"), ("kfz", "denkt")], "LU", [("var", "schreck"), ("var3", "ruhig")]),
]))

# ===========================================================================================================================
# L Ergebnis (zurück vor der Bäckerei)
# ===========================================================================================================================
HX9, LX9 = 1180, 1660
folie([("erg", "Ergebnis · kein Schwager"), ("erg2", "Ergebnis · 400 €, mit Rechnung 476 €")], [
    *baeckerei("erg"),
    buegel(RX - 40, "erg"),
    pl("Ergebnis: Den Schwager muss Hedi nicht hinnehmen", 760, 30, beim("erg", "Hedi"), fill=GRUEN, size=32),
    pl("400 € · mit Reparaturrechnung 476 €", 760, 100, beim("erg2", "vierhundert"), fill=WEISS, size=32),
    ficon("tabler", "cash-banknote", HX9 - 170, 600, 130, beim("erg2", "vierhundert"), fuell=GRUEN),
    *fig("HD", HX9, G0, FHA, [("erg", "ruhig_r"), (beim("erg2", "vierhundert"), "freut_r")], erst="cut"),
    ns("Hedi", HX9, G0, "erg", BLAU),
    *fig("LU", LX9, G0, FHA, [("erg", "still"), ("erg2", "ruhig")], erst="cut"),
    ns("Ludolf", LX9, G0, "erg", GRUEN),
])

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Haftungsgrund und Rechtsfolge trennen"), ("tipp2", "Klausurtipp · Werkvertragsrecht: keine fiktiven Mängelbeseitigungskosten"),
       ("tipp3", "Klausurtipp · Deliktsrecht: fiktive Abrechnung möglich")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Haftungsgrund und Rechtsfolge trennen:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("§§ 249–251 BGB erst beim Schaden", 200, 262, beim("tipp", "Paragrafen"), "Regular", 34),
    linienzug([(130, 335), (1130, 335)], "tipp2", breite=3),
    z("Vorsicht, fiktive Abrechnung:", 200, 360, "tipp2", "Bold", 34),
    *pkt("Werkvertragsrecht: für Mängelbeseitigungs-", 425, beim("tipp2", "Werkvertragsrecht"), "Regular", 32, x=245),
    z("kosten aufgegeben", 245, 470, beim("tipp2", "Werkvertragsrecht"), "Regular", 32),
    zit("BGH, Urt. v. 22.2.2018 – VII ZR 46/17, Leitsatz 1", 245, 520, beim("tipp2", "aufgegeben")),
    *okz("Deliktsrecht: bleibt möglich", 585, "tipp3", "Bold", 32, x=245),
    zit("BGH, Urt. v. 28.1.2025 – VI ZR 300/24, Rn. 12", 245, 635, beim("tipp3", "bleibt")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "1. Schaden: Differenzhypothese", True),
          ("k2", 0, "2. grundsätzlich Herstellung (§ 249 Abs. 1 BGB)", True),
          ("k3", 0, "3. beschädigte Sache: Geld statt Herstellung (§ 249 Abs. 2 Satz 1 BGB)", True),
          ("k3b", 1, "Umsatzsteuer nur, wenn angefallen (§ 249 Abs. 2 Satz 2 BGB)", False),
          ("k4", 0, "4. Geldentschädigung (§ 251 BGB):", True),
          ("k4", 1, "Herstellung unmöglich, ungenügend oder unverhältnismäßig", False),
          ("k5", 0, "Zur Höhe stets: erforderlicher Betrag, wirtschaftlicherer Weg", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Rechtsfolge, §§ 249–251 BGB"), 110, 90, "sch", 46)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    if c == "k5":
        y += 30
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 36, rechts=1800))
    y += {0: 95, 1: 85}[ebene]
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › 1. Schaden"), ("k2", "Klausurschema › 2. Herstellung"),
       ("k3", "Klausurschema › 3. Geld statt Herstellung"), ("k3b", "Klausurschema › 3. Umsatzsteuer"),
       ("k4", "Klausurschema › 4. Geldentschädigung, § 251 BGB"), ("k5", "Klausurschema › Höhe")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst die ", 0), ("Differenz", "a"), (" feststellen,", 0)], [("dann die Art des Ersatzes.", 0)]],
                750, 300, 46, "merke", {"a": beim("merke", "Differenz")}),
    *markertext([[("Bei einer beschädigten Sache", 0)], [("darf der Geschädigte statt der", 0)],
                 [("Herstellung ", 0), ("Geld", "b"), (" verlangen.", 0)]],
                750, 560, 46, "mk2", {"b": beim("mk2", "Geld")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
