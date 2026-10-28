"""Folge 159 · Auslegungsmethoden Jura: Wortlaut, Systematik, Historie, Telos – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Die Jurastudentin Thekla fährt jeden Morgen ruhig mit ihrem E-Scooter zur Uni (kein Unfall, kein Alkohol).
Im Methodenseminar fragt Professor Lindhorst: Ist Ihr E-Scooter ein Kraftfahrzeug?
Szenen laut ../SZENENPLAN.md: A1 Radweg vor der Uni, A2 Methodenseminar, A3 Hook, B Sachverhalt, C vier Methoden –
gleiche Struktur, D1 1. Wortlaut (Wortlautkarte § 1 Abs. 2 StVG), D2 Wortlaut als Grenze (Wortlautkarte Art. 103 Abs. 2 GG),
E 2. Systematik (Wortlautkarte § 1 Abs. 1 eKFV, gekürzt; § 1 Abs. 3 StVG), F 3. Historie (Zitatkarte BR-Drs. 158/19),
G 4. Telos, H1 Ergebnis der Rechtsprechung, H2 Methodenseminar (Rückkehr), I1 Analogie, I2 teleologische Reduktion und
Analogieverbot, J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Jede Methode hat ihre Farbe (Wortlaut Gelb, Systematik Blau, Historie Lila, Telos Grün) und dieselbe Tafelstruktur
Frage – Werkzeug – Ergebnis am Beispiel.
Der E-Scooter ist programmatisch aus Palettenflächen und Tuschekontur gezeichnet (roller()), ohne Marke oder Logo.
Zwei Handlungsgeräusche (leises Motorsummen während der Fahrt, Ständer beim Abstellen; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist (auf dem Scooter fährt das Schild mit). Hilfsfunktionen glyphen/z/pl/
tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 158 (gemeinsame Dateien unverändert); neu: roller(),
tafel_m(), methode(), seminar(), hand().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_159/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_159/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149/158) ------------------------------------
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




def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel, nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel (Thekla links, Lindhorst rechts)
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1580, 150, 370                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
TH_N, LI_N = ROT, GRUEN                     # Namensschilder in der Kleidungsfarbe
FW, FS, FH_, FT = GELB, BLAU, LILA, GRUEN   # Methodenfarben: Wortlaut, Systematik, Historie, Telos
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BODEN = 880


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def fuesse(name, cx, unten, hoehe):
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    ys, xs = np.nonzero(a[int(h * 0.93):])
    return int(e.x + xs.min()), int(e.x + xs.max())


def _roller_bild(xb, xf, boden, r, top, kick=False, s=2):
    """E-Scooter (Seitenansicht) aus Palettenflächen mit Tuschekontur: Hinterrad bei xb, Vorderrad bei xf (Radmitte),
    Trittbrett auf Achshöhe, Lenkstange vom Vorderrad bis top=(x, y), Radnabenmotor gelb. Ohne Marke, ohne Logo."""
    x0 = min(xb, xf, top[0]) - r - 40
    x1 = max(xb, xf, top[0]) + r + 40
    y0 = top[1] - 30
    y1 = boden + 6
    W_, H_ = (x1 - x0) * s, (y1 - y0) * s
    im = Image.new("RGBA", (W_, H_))
    dr = ImageDraw.Draw(im)
    P = lambda x, y: ((x - x0) * s, (y - y0) * s)
    cy = boden - r
    rich = 1 if xf > xb else -1
    # Ständer (beim Abstellen)
    if kick:
        a, b = P(xb + rich * (r + 30), cy + 4), P(xb + rich * (r - 2), boden - 2)
        dr.line([a, b], fill=INK, width=7 * s)
    # Lenkstange
    dr.line([P(xf, cy), P(*top)], fill=INK, width=12 * s)
    gx, gy = P(*top)
    dr.rounded_rectangle((gx - 22 * s, gy - 8 * s, gx + 22 * s, gy + 8 * s), 7 * s, fill=INK)
    # Trittbrett
    d0, d1 = sorted((xb, xf - rich * r))
    dr.rounded_rectangle((*P(d0, cy - 9), *P(d1, cy + 9)), 8 * s, fill=INK)
    dr.rounded_rectangle((*P(d0 + 4, cy - 5), *P(d1 - 4, cy + 5)), 5 * s, fill=BLAU)
    # Räder
    for x, nabe in ((xb, WEISS), (xf, GELB)):
        cx_, cy_ = P(x, cy)
        dr.ellipse((cx_ - r * s, cy_ - r * s, cx_ + r * s, cy_ + r * s), fill=INK)
        dr.ellipse((cx_ - (r - 7) * s, cy_ - (r - 7) * s, cx_ + (r - 7) * s, cy_ + (r - 7) * s), fill=WEISS)
        dr.ellipse((cx_ - 11 * s, cy_ - 11 * s, cx_ + 11 * s, cy_ + 11 * s), fill=INK)
        dr.ellipse((cx_ - 7 * s, cy_ - 7 * s, cx_ + 7 * s, cy_ + 7 * s), fill=nabe)
    im = im.resize((W_ // s, H_ // s), Image.LANCZOS)
    return im, x0, y0


def roller_frei(xb, xf, boden, r, top, cue, kick=False, anim="pop", d=0.0, bis=None, name="roller"):
    im, x0, y0 = _roller_bild(xb, xf, boden, r, top, kick)
    return El(im, x0, y0, cue, anim, d, bis, name=name)


def fahrerin(name, cx, hoehe, cue, rechts=True, kick=False, bis=None, anim="cut", r=26):
    """Thekla auf dem E-Scooter: Füße auf dem Trittbrett, die ausgestreckte Hand an der Lenkstange.
    Gibt [Scooter, Figur] zurück (Scooter zuerst, damit die Hand den Griff verdeckt)."""
    deck = BODEN - r - 9
    seite = 1 if rechts else -1
    hx, hy = hand(name, cx, deck, hoehe, seite)
    f0, f1 = fuesse(name, cx, deck, hoehe)
    xb = (f0 - 24) if rechts else (f1 + 24)
    xf = hx + seite * 46
    ro = roller_frei(xb, xf, BODEN, r, (hx + seite * 4, hy - 4), cue, kick=kick, anim=anim, bis=bis)
    fi = peep_voll(name, cx, deck, hoehe, cue, anim=anim, bis=bis)
    return [ro, fi]


def tafel_m(cue, titel_, farbe, h=840, size=46):
    """Methodentafel: Titelmarker und Randstreifen in der Methodenfarbe."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue), karte(60, 60, 26, h, cue, fill=farbe, rund=10, schatten=0, rand=5),
            titel(titel_, 110, 100, cue, size, marker=farbe)]


def methode(cue, titel_, farbe, fc, frage, wc, werkzeug, wc2=None, werkzeug2=None):
    """Gleiche Struktur für alle vier Methoden: Titel, Frage, Werkzeug (Ergebnis folgt am Beispiel)."""
    els = [*tafel_m(cue, titel_, farbe),
           pl("Frage", 110, 172, fc, fill=farbe, size=28), z(frage, 330, 176, fc, "Bold", 32),
           pl("Werkzeug", 110, 236, wc, fill=farbe, size=28), z(werkzeug, 330, 240, wc, "Bold", 32)]
    if werkzeug2:
        els.append(z(werkzeug2, 330 + F("Bold", 32).getlength(werkzeug + " "), 240, wc2, "Bold", 32))
    return els


def ergebnis(y, cue, farbe, text="Ergebnis am Beispiel: Kraftfahrzeug"):
    return [pl("Ergebnis", 110, y + 20, cue, fill=farbe, size=28),
            blk(300, y, 850, 84, farbe, cue, [(text.split(": ", 1)[-1], "ExtraBold", 36, INK)])]


def wl_karte(text, quelle, x, y, cue, marken=(), size=30, w=1040, bis=None):
    """Wortlautkarte mit automatischem Umbruch; ein Marker, der über einen Zeilenumbruch reicht, wird je Zeile gesetzt."""
    zeilen = umbruch(text, size, w - 70)
    mk = []
    for wort, c in marken:
        try:
            mk.append((zi(zeilen, wort), wort, c))
        except KeyError:
            teile = wort.split()
            for k in range(len(teile) - 1, 0, -1):
                a, b = " ".join(teile[:k]), " ".join(teile[k:])
                i = next((i for i, t in enumerate(zeilen[:-1]) if t.endswith(a) and zeilen[i + 1].startswith(b)), None)
                if i is not None:
                    mk += [(i, a, c), (i + 1, b, c)]
                    break
            else:
                raise KeyError(wort)
    return wortlaut(x, y, w, zeilen, quelle, cue, marken=mk, size=size, bis=bis)


def zi(zeilen, wort):
    for i, t in enumerate(zeilen):
        if wort in t:
            return i
    raise KeyError(wort)


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


def paar(c0, tf, lf, bis=None, th_bis=None, li_bis=None):
    """Tafelszene: Thekla (links) und Lindhorst (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("TH", X1, FB, FR, tf, bis=th_bis or bis), ns("Thekla", X1, FB, c0, TH_N, d=0.1),
            *fig("LI", X2, FB, FR, lf, bis=li_bis or bis, d=0.2), ns("Prof. Lindhorst", X2, FB, c0, LI_N, d=0.3)]


# ===========================================================================================================================
# A1 Fall: Thekla fährt mit dem E-Scooter zur Uni und stellt ihn vor dem Hörsaal ab
# ===========================================================================================================================
TH_FAHRT = "TH_laechelt_r"
ZIELX = 900                                  # Halteposition vor dem Hörsaal
START = beim("fall", "fährt")
ANKUNFT = beim("fall", "Radweg", ende=True)
AB = beim("ab", "stellt")
DX = -560                                    # Startpunkt links (fährt nach rechts)
fahrt = fahrerin(TH_FAHRT, ZIELX, FR, NULL, rechts=True, bis=AB)
for e in fahrt:
    bewegt(e, START, ANKUNFT, DX)
szene(fahrt[0], "159summen*", 0.5, versatz=round(T_(START) - T_(NULL), 3))
schild_fahrt = bewegt(ns("Thekla", ZIELX, BODEN, NULL, TH_N, bis=AB), START, ANKUNFT, DX)
hx, hy = hand(TH_FAHRT, ZIELX, BODEN - 35, FR, 1)
f0, _ = fuesse(TH_FAHRT, ZIELX, BODEN - 35, FR)
geparkt = roller_frei(f0 - 24, hx + 46, BODEN, 26, (hx + 4, hy - 4), AB, kick=True, anim="cut")
folie([(NULL, "Fall · Thekla fährt zur Uni"), ("ab", "Fall · Vor dem Hörsaal")], [
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    hart(karte(60, BODEN + 14, 1800, 40, NULL, fill=(226, 226, 222, 255), rund=12, schatten=0, rand=4)),
    hart(pl("Radweg", 120, BODEN + 66, NULL, fill=WEISS, size=28)),
    hart(ficon("tabler", "sun", 190, 250, 130, NULL, fuell=GELB)),
    hart(pl("jeden Morgen zur Uni", 280, 150, NULL, fill=GELB, size=36)),
    hart(ficon("tabler", "tree", 120, BODEN - 4, 150, NULL, fuell=GRUEN)),
    hart(ficon("tabler", "building-bank", 1610, BODEN - 4, 420, NULL, fuell=WEISS)),
    pl("Hörsaal", 1610, 380, beim("ab", "Hörsaal"), fill=LILA, size=34, anker="m"),
    *[hart(e) for e in fahrt], hart(schild_fahrt),
    pl("ruhig, auf dem Radweg", 280, 225, beim("fall", "ruhig"), fill=WEISS, size=30),
    szene(geparkt, "159staender*", 0.7, versatz=0.15),
    *fig("TH", 1250, BODEN, FR, [(AB, "laechelt_r"), (beim("ab", "ab"), "froh_r")], erst="cut"),
    ns("Thekla", 1250, BODEN, AB, TH_N),
])

# ===========================================================================================================================
# A2 Methodenseminar: Professor Lindhorst fragt, Thekla antwortet
# ===========================================================================================================================
LX_, TX_ = 820, 1560                         # Lindhorst (blickt nach rechts), Thekla (blickt nach links)
SB = 930


def seminar(c0, hart_=False):
    """Seminarraum: Tafel mit Seminartitel, Fenster mit dem abgestellten E-Scooter draußen, Boden."""
    els = [linienzug([(40, SB), (1880, SB)], c0, breite=7, farbe=INK),
           karte(110, 120, 560, 330, c0, fill=GRUEN, rund=16, schatten=8),
           z("Methodenseminar", 150, 160, c0, "ExtraBold", 40, rechts=660),
           z("Auslegung", 150, 225, c0, "Bold", 36, rechts=660),
           karte(1440, 110, 400, 270, c0, fill=(214, 232, 250, 255), rund=14, schatten=6),
           linienzug([(1640, 116), (1640, 376)], c0, breite=5, farbe=INK),
           roller_frei(1520, 1740, 350, 16, (1730, 220), c0, kick=True, name="fenster:roller"),
           linienzug([(1450, 352), (1830, 352)], c0, breite=4, farbe=INK)]
    return [hart(e) for e in els] if hart_ else els


folie([("sem", "Fall · Im Methodenseminar"), ("l1", "Fall · Ist der E-Scooter ein Kraftfahrzeug?"),
       ("t1", "Fall · Kein Auto, kein Sitz")], [
    *seminar("sem"),
    *fig("LI", LX_, SB, FR, [("sem", "ruhig_r")], bis="l1", d=0.1),
    *redet("LI_redet_r", LX_, SB, FR, "l1", "t1"),
    *fig("LI", LX_, SB, FR, [("t1", "denkt_r")], bis="hook", erst="cut"),
    ns("Prof. Lindhorst", LX_, SB, "sem", LI_N, d=0.2),
    blase("sprech", 640, 210, "l1", 1110, 330, inhalt=["Ist Ihr E-Scooter eigentlich", "ein Kraftfahrzeug?"],
          textsize=36, figur=("LI_redet_r", LX_, SB, FR), bis="t1"),
    *fig("TH", TX_, SB, FR, [("sem", "ruhig"), ("l1", "staunt")], bis="t1", d=0.2),
    *redet("TH_redet", TX_, SB, FR, "t1", "hook"),
    ns("Thekla", TX_, SB, "sem", TH_N, d=0.3),
    blase("sprech", 600, 210, "t1", 1130, 300, inhalt=["Ein Kraftfahrzeug? Der hat", "doch nicht mal einen Sitz!"],
          textsize=36, figur=("TH_redet", TX_, SB, FR), bis="hook"),
])

# ===========================================================================================================================
# A3 Hook: Fahrzeug, sogar Kraftfahrzeug? Vier Wege – und warum es zählt
# ===========================================================================================================================
VIER = [("Wortlaut", FW), ("Systematik", FS), ("Historie", FH_), ("Telos", FT)]
folie([("hook", "Fall · Fahrzeug, sogar Kraftfahrzeug?"), ("hook2", "Fall · Vier Wege, ein Gesetz zu lesen"),
       ("folge", "Fall · Warum es zählt: 1,1 ‰"), ("nur", "Fall · § 316 StGB verlangt nur „ein Fahrzeug“")], rechts_frei([
    *tafel("hook", "E-Scooter: Fahrzeug? Kraftfahrzeug?"),
    roller_frei(170, 360, 330, 22, (350, 190), "hook", name="diagramm:roller"),
    z("Fahrzeug?", 430, 190, beim("hook", "Fahrzeug"), "Bold", 36),
    z("sogar Kraftfahrzeug?", 430, 250, beim("hook", "Kraftfahrzeug"), "ExtraBold", 36),
    z("4 Wege, ein Gesetz zu lesen:", 110, 375, beim("hook2", "Vier"), "Bold", 34),
    *[pl(t, 110 + i * 262, 430, beim("hook2", t), fill=f, size=32) for i, (t, f) in enumerate(VIER)],
    z("Die Antwort hat Folgen: Trunkenheit im Verkehr", 110, 535, "folge", "Bold", 32),
    dicon("tabler", "car", 170, 660, 90, beim("folge", "Kraftfahrer"), fuell=BLAU),
    z("Kraftfahrer: ab 1,1 ‰ absolut fahruntüchtig", 240, 605, beim("folge", "Kraftfahrer"), "Bold", 32),
    dicon("tabler", "bike", 170, 735, 90, beim("folge", "Radfahrer"), fuell=WEISS),
    z("Radfahrer: erst ab einem höheren Wert", 240, 680, beim("folge", "Radfahrer"), "Bold", 32),
    *okz("§ 316 StGB verlangt nur „ein Fahrzeug“: E-Scooter sicher", 770, beim("nur", "Paragraf"), "Bold", 30, x=160),
    pl("spannend: Kraftfahrzeug", 700, 830, beim("nur", "Spannend"), fill=PINK, size=30),
    *paar("hook", [("hook", "denkt"), ("folge", "staunt"), ("nur", "denkt")], [("hook", "ruhig"), ("hook2", "froh"),
                                                                             ("folge", "ernst")]),
]))

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================


def sachverhalt_159(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 215
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.34)
        els += e; y += 26
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_159("sv", [
    "Thekla fährt jeden Morgen mit ihrem E-Scooter auf dem Radweg zur Uni. Der E-Scooter hat einen Elektromotor, eine "
    "Lenkstange, keinen Sitz und fährt höchstens 20 km/h. Treten muss Thekla nicht; hinten klebt eine "
    "Versicherungsplakette.",
    "Im Methodenseminar fragt Professor Lindhorst: „Ist Ihr E-Scooter eigentlich ein Kraftfahrzeug?“ Thekla antwortet: "
    "„Ein Kraftfahrzeug? Der hat doch nicht mal einen Sitz!“",
    "Davon hängt ab, welcher Promille-Grenzwert für E-Scooter-Fahrer bei der Trunkenheit im Verkehr (§ 316 StGB) gilt.",
], "Ist der E-Scooter ein Kraftfahrzeug im Sinne von § 1 Abs. 2 StVG?")

# ===========================================================================================================================
# C Vier Methoden – gleiche Struktur: Frage, Werkzeug, Ergebnis am Beispiel
# ===========================================================================================================================
GX0 = 110
folie([("vier", "Methoden · Frage – Werkzeug – Ergebnis"), ("bv", "Methoden · ergänzen sich, Ausgangspunkt Wortlaut")],
      rechts_frei([
    *tafel("vier", "4 Methoden, gleiche Struktur"),
    *[blk(GX0, 190 + i * 74, 300, 62, f, "vier", [(f"{i + 1}. {t}", "ExtraBold", 30, INK)], anim="pop")
      for i, (t, f) in enumerate(VIER)],
    dicon("tabler", "help", 520, 300, 70, "fr", fuell=WEISS),
    pl("Frage", 470, 315, "fr", fill=WEISS, size=30),
    dicon("tabler", "tool", 760, 300, 70, "wz", fuell=WEISS),
    pl("Werkzeug", 690, 315, "wz", fill=WEISS, size=30),
    dicon("tabler", "checkbox", 1010, 300, 70, "eb", fuell=WEISS),
    pl("Ergebnis", 945, 315, beim("eb", "Beispiel"), fill=WEISS, size=30),
    z("am Beispiel", 955, 380, beim("eb", "Beispiel"), "Bold", 28),
    pfeil(640, 334, 680, 334, "wz", breite=6, kopf=18),
    pfeil(875, 334, 932, 334, beim("eb", "Beispiel"), breite=6, kopf=18),
    blk(110, 520, 1040, 150, HELL, "bv", [("Die Methoden ergänzen sich,", "Bold", 34, INK),
                                         ("keine hat einen unbedingten Vorrang.", "Bold", 34, INK)]),
    pl("Ausgangspunkt: der Wortlaut", 110, 700, beim("bv", "Ausgangspunkt"), fill=FW, size=34),
    zit("BVerfG, Urt. v. 19.3.2013 – 2 BvR 2628/10 u. a., Rn. 66", 110, 790, beim("bv", "Bundesverfassungsgericht")),
    *requisit([("vier", ("tabler", "list-numbers", 100, WEISS), "3 Schritte", WEISS),
               ("bv", ("tabler", "scale", 100, WEISS), "BVerfG", WEISS)]),
    *paar("vier", [("vier", "ruhig"), ("bv", "denkt")], [("vier", "froh"), ("bv", "ruhig")]),
]))

# ===========================================================================================================================
# D1 1. Wortlaut: § 1 Abs. 2 StVG
# ===========================================================================================================================
T12 = ("„Als Kraftfahrzeuge im Sinne dieses Gesetzes gelten Landfahrzeuge, die durch Maschinenkraft bewegt werden, ohne "
       "an Bahngleise gebunden zu sein.“")
w12, w12_y = wl_karte(T12, "§ 1 Abs. 2 StVG", 110, 300, "p12", marken=[
    ("Kraftfahrzeuge", "p12w"), ("Landfahrzeuge", beim("wl1", "Land")), ("Maschinenkraft", beim("wl2", "Maschinenkraft")),
    ("ohne", beim("wl3", "Schienen")), ("an Bahngleise gebunden", beim("wl3", "Schienen"))])
assert w12_y <= 525, w12_y
folie([("w1", "1. Wortlaut · Frage und Werkzeug"), ("p12", "1. Wortlaut · § 1 Abs. 2 StVG"),
       ("wl1", "1. Wortlaut · am Beispiel"), ("werg", "1. Wortlaut · Ergebnis: Kraftfahrzeug")], rechts_frei([
    *methode("w1", "1. Wortlaut", FW, beim("w1", "Frage"), "Was sagen die Worte?", beim("w2", "Werkzeug"), "Wortsinn,",
             beim("w2", "Legaldefinition"), "Legaldefinition"),
    *w12,
    *okz("fährt an Land: Landfahrzeug", 545, "wl1", "Bold", 32, x=160),
    *okz("Elektromotor = Maschinenkraft", 605, beim("wl2", "Elektromotor"), "Bold", 32, x=160),
    *okz("keine Schienen nötig", 665, beim("wl3", "Schienen"), "Bold", 32, x=160),
    *ergebnis(745, "werg", FW),
    *requisit([("w1", ("tabler", "abc", 110, GELB), "Wortlaut", GELB),
               ("p12", ("tabler", "book", 100, WEISS), "§ 1 Abs. 2 StVG", WEISS),
               ("werg", ("tabler", "circle-check", 100, GELB), "Kraftfahrzeug", GELB)]),
    *paar("w1", [("w1", "ruhig"), ("p12", "denkt"), ("wl1", "ruhig"), ("werg", "froh")],
          [("w1", "froh"), ("p12", "ruhig"), ("werg", "froh")]),
]))

# ===========================================================================================================================
# D2 Wortlaut als Grenze im Strafrecht: Art. 103 Abs. 2 GG
# ===========================================================================================================================
T103 = "„Eine Tat kann nur bestraft werden, wenn die Strafbarkeit gesetzlich bestimmt war, bevor die Tat begangen wurde.“"
w103, w103_y = wl_karte(T103, "Art. 103 Abs. 2 GG", 110, 270, "a103", marken=[("gesetzlich bestimmt",
                                                                              beim("a103w", "gesetzlich"))], size=32)
assert w103_y <= 520, w103_y
folie([("gr1", "1. Wortlaut · Grenze im Strafrecht"), ("a103", "1. Wortlaut · Art. 103 Abs. 2 GG"),
       ("gr2", "1. Wortlaut · möglicher Wortsinn als Grenze")], rechts_frei([
    *tafel_m("gr1", "Wortlaut als Grenze", FW),
    z("Im Strafrecht ist der Wortlaut zugleich die Grenze.", 110, 180, beim("gr1", "Strafrecht"), "Bold", 34),
    *w103,
    blk(110, 580, 1040, 150, FW, "gr2", [("Der mögliche Wortsinn ist die", "ExtraBold", 36, INK),
                                       ("äußerste Grenze der Auslegung.", "ExtraBold", 36, INK)]),
    zit("BVerfG, Beschl. v. 19.3.2007 – 2 BvR 2273/06, Rn. 11", 110, 755, beim("gr2", "mögliche")),
    *requisit([("gr1", ("tabler", "barrier-block", 120, GELB), "Grenze", GELB),
               ("a103", ("tabler", "book", 100, WEISS), "Art. 103 Abs. 2 GG", WEISS),
               ("gr2", ("tabler", "ruler-measure", 110, GELB), "Wortsinn", GELB)]),
    *paar("gr1", [("gr1", "denkt"), ("gr2", "ruhig")], [("gr1", "ernst"), ("a103", "ruhig"), ("gr2", "froh")]),
]))

# ===========================================================================================================================
# E 2. Systematik: § 1 Abs. 1 eKFV, § 1 Abs. 3 StVG (Umkehrschluss)
# ===========================================================================================================================
TEK = ("„Elektrokleinstfahrzeuge im Sinne dieser Verordnung sind Kraftfahrzeuge mit elektrischem Antrieb und einer "
       "bauartbedingten Höchstgeschwindigkeit von mehr als 6 km/h und nicht mehr als 20 km/h, die folgende Merkmale "
       "aufweisen: 1. Fahrzeug ohne Sitz oder selbstbalancierendes Fahrzeug mit oder ohne Sitz, …“")
wek, wek_y = wl_karte(TEK, "§ 1 Abs. 1 eKFV (Auszug)", 110, 300, "ek", marken=[
    ("Kraftfahrzeuge", beim("ekw", "Kraftfahrzeuge")), ("elektrischem Antrieb", beim("ekw", "elektrischem")),
    ("nicht mehr als 20 km/h", beim("ekv", "zwanzig")), ("Fahrzeug ohne Sitz", beim("ekv", "ohne"))], size=30, bis="s3")
assert wek_y <= 640, wek_y
folie([("s1", "2. Systematik · Frage und Werkzeug"), ("ek", "2. Systematik · § 1 Abs. 1 eKFV"),
       ("s3", "2. Systematik · § 1 Abs. 3 StVG"), ("serg", "2. Systematik · Ergebnis: Kraftfahrzeug")], rechts_frei([
    *methode("s1", "2. Systematik", FS, beim("s1", "Frage"), "Wie passt die Norm zu den anderen?",
             beim("s2", "Werkzeug"), "Stellung im Gesetz,", beim("s2", "Verhältnis"), "Nachbarnormen"),
    *wek,
    bis_(pl("typischer E-Scooter", 110, 665, beim("ekv", "typische"), fill=FS, size=30), "s3"),
    blk(110, 300, 1040, 150, HELL, "s3", [("§ 1 Abs. 3 StVG: Räder, die man selbst tritt", "Bold", 32, INK),
                                         ("und deren Motor nur hilft: keine Kfz", "Bold", 32, INK)]),
    dicon("tabler", "bike", 1080, 445, 80, beim("s3", "Räder"), fuell=WEISS),
    *neinz("E-Scooter: keine solche Ausnahme", 500, beim("s4", "Für"), "Bold", 34, x=160),
    z("Umkehrschluss: Der E-Scooter bleibt Kraftfahrzeug.", 160, 560, beim("s4", "Ausnahme"), "Bold", 30),
    zit("OLG Hamm, Urt. v. 8.1.2025 – 1 ORs 70/24, Rn. 22, 41", 160, 612, beim("s4", "Ausnahme")),
    *ergebnis(745, "serg", FS),
    *requisit([("s1", ("tabler", "puzzle", 110, BLAU), "Systematik", BLAU),
               ("ek", ("tabler", "book", 100, WEISS), "eKFV", WEISS),
               ("s3", ("tabler", "bike", 130, WEISS), "Pedelec: Ausnahme", WEISS),
               ("serg", ("tabler", "circle-check", 100, BLAU), "Kraftfahrzeug", BLAU)]),
    *paar("s1", [("s1", "denkt"), ("ek", "ruhig"), ("s3", "denkt"), ("serg", "froh")],
          [("s1", "ruhig"), ("ekv", "froh"), ("s3", "ernst"), ("serg", "froh")]),
]))

# ===========================================================================================================================
# F 3. Historie: Begründung der Verordnung (BR-Drs. 158/19)
# ===========================================================================================================================
TBR = ("„Da Elektrokleinstfahrzeuge über einen elektrischen Antriebsmotor verfügen, sind sie Kraftfahrzeuge nach § 1 "
       "Absatz 2 StVG.“")
wbr, wbr_y = wl_karte(TBR, "Begründung, BR-Drs. 158/19, S. 1", 110, 350, "h3", marken=[
    ("elektrischen Antriebsmotor", beim("h3w", "elektrischen")), ("sind sie Kraftfahrzeuge", beim("h3w", "sind"))],
    size=32)
assert wbr_y <= 580, wbr_y
folie([("h1", "3. Historie · Frage und Werkzeug"), ("h3", "3. Historie · BR-Drs. 158/19"),
       ("herg", "3. Historie · Ergebnis: bewusst Kraftfahrzeug")], rechts_frei([
    *methode("h1", "3. Historie", FH_, beim("h1", "Frage"), "Was wollte der Normgeber?", beim("h2", "Werkzeug"),
             "Materialien:", beim("h2", "Entwürfe"), "Entwürfe, Begründungen"),
    z("Begründung zur Verordnung, 2019:", 110, 302, beim("h3", "Begründung"), "Bold", 28, farbe=TEXT),
    *wbr,
    *ergebnis(745, "herg", FH_, "Ergebnis: bewusst als Kraftfahrzeug"),
    *requisit([("h1", ("tabler", "history", 110, LILA), "Historie", LILA),
               ("h3", ("tabler", "file-text", 100, WEISS), "Begründung", WEISS),
               ("herg", ("tabler", "circle-check", 100, LILA), "Kraftfahrzeug", LILA)]),
    *paar("h1", [("h1", "ruhig"), ("h3", "denkt"), ("herg", "froh")], [("h1", "froh"), ("h3", "ruhig")]),
]))

# ===========================================================================================================================
# G 4. Telos: Sinn und Zweck
# ===========================================================================================================================
MERKMALE = [(beim("te4", "Motor"), "bolt", "Motor, bis 20 km/h"), (beim("te4", "kleinen"), "circle-dot", "kleine Räder"),
            (beim("te4", "Fahrer"), "arrow-big-up-line", "der Fahrer steht")]
folie([("te1", "4. Telos · Frage und Werkzeug"), ("te3", "4. Telos · Zweck des Grenzwerts"),
       ("te4", "4. Telos · am Beispiel"), ("teerg", "4. Telos · Ergebnis: Kraftfahrzeug")], rechts_frei([
    *methode("te1", "4. Telos: Sinn und Zweck", FT, beim("te1", "Frage"), "Wozu gibt es die Regel?",
             beim("te2", "Werkzeug"), "Welche Gefahr soll sie abwehren?"),
    blk(110, 310, 1040, 130, HELL, "te3", [("Der Grenzwert schützt den Verkehr vor Fahrern,", "Bold", 32, INK),
                                          ("die ihr Kfz nicht mehr sicher führen können.", "Bold", 32, INK)]),
    *[e for i, (c, ic, t) in enumerate(MERKMALE) for e in (
        karte(110 + i * 350, 470, 330, 150, c, fill=WEISS, rund=16, schatten=5, rand=4),
        dicon("tabler", ic, 275 + i * 350, 560, 64, c, fuell=GELB if ic == "bolt" else WEISS),
        z(t, 275 + i * 350 - F("Bold", 28).getlength(t) / 2, 572, c, "Bold", 28))],
    z("deutliches Risiko auch für andere", 110, 650, beim("te5", "deutliches"), "ExtraBold", 32),
    zit("OLG Hamm, Urt. v. 8.1.2025 – 1 ORs 70/24, Rn. 32", 110, 698, beim("te5", "Oberlandesgericht")),
    *ergebnis(760, "teerg", FT),
    *requisit([("te1", ("tabler", "target-arrow", 110, GRUEN), "Telos", GRUEN),
               ("te3", ("tabler", "shield-check", 100, GRUEN), "Schutz", WEISS),
               ("te4", ("tabler", "gauge", 110, WEISS), "bis 20 km/h", WEISS),
               ("teerg", ("tabler", "circle-check", 100, GRUEN), "Kraftfahrzeug", GRUEN)]),
    *paar("te1", [("te1", "ruhig"), ("te3", "denkt"), ("te4", "staunt"), ("teerg", "froh")],
          [("te1", "froh"), ("te3", "ernst"), ("teerg", "froh")]),
]))

# ===========================================================================================================================
# H1 Ergebnis: Rechtsprechung
# ===========================================================================================================================
folie([("rs1", "Ergebnis · Rechtsprechung"), ("rs2", "Ergebnis · BayObLG 2020"), ("rs3", "Ergebnis · OLG Hamm 2025"),
       ("rs4", "Ergebnis · BGH: offengelassen")], rechts_frei([
    *tafel("rs1", "Ergebnis: Kraftfahrzeug"),
    *[e for i, (t, f) in enumerate(VIER) for e in (
        blk(110 + i * 262, 180, 248, 62, f, "rs1", [(t, "ExtraBold", 28, INK)], anim="pop"),
        ok(110 + i * 262 + 224, 210, "rs1", gr=18))],
    blk(110, 290, 1040, 140, GRUEN, "rs2", [("BayObLG: E-Scooter sind Kraftfahrzeuge,", "ExtraBold", 32, INK),
                                           ("für ihre Fahrer gilt die Grenze von 1,1 ‰", "ExtraBold", 32, INK)]),
    zit("BayObLG, Beschl. v. 24.7.2020 – 205 StRR 216/20, Leitsätze 2, 3", 110, 445, beim("rs2", "Bayerische")),
    *okz("andere OLG folgen, etwa Hamm 2025", 505, "rs3", "Bold", 32, x=160),
    zit("OLG Hamm, Urt. v. 8.1.2025 – 1 ORs 70/24, Rn. 30 f.", 160, 555, beim("rs3", "Hamm")),
    z("BGH: für Elektrokleinstfahrzeuge bisher offengelassen", 110, 625, "rs4", "Bold", 32),
    zit("BGH, Beschl. v. 13.4.2023 – 4 StR 439/22, Rn. 4 f.", 110, 675, beim("rs4", "offengelassen")),
    pl("mehr in Folge 130", 110, 745, beim("rs5", "Folge"), fill=LILA, size=30),
    *requisit([("rs1", ("tabler", "gavel", 100, HOLZ), "Rechtsprechung", WEISS),
               ("rs4", ("tabler", "help", 100, WEISS), "BGH offen", WEISS)]),
    *paar("rs1", [("rs1", "froh"), ("rs4", "denkt")], [("rs1", "ruhig"), ("rs2", "froh")]),
]))

# ===========================================================================================================================
# H2 Methodenseminar (Rückkehr): vier Methoden, ein Ergebnis
# ===========================================================================================================================
folie([("l2", "Ergebnis · Vier Methoden, ein Ergebnis"), ("t2", "Ergebnis · Nach der Party: stehen lassen")], [
    *seminar("l2"),
    *redet("LI_redetfroh_r", LX_, SB, FR, "l2", "t2"),
    *fig("LI", LX_, SB, FR, [("t2", "froh_r")], bis="ab1", erst="cut"),
    ns("Prof. Lindhorst", LX_, SB, "l2", LI_N, d=0.1),
    blase("sprech", 660, 260, "l2", 1110, 310, inhalt=["Vier Methoden, ein Ergebnis:", "Ihr Scooter ist ein", "Kraftfahrzeug."],
          textsize=36, figur=("LI_redetfroh_r", LX_, SB, FR), bis="t2"),
    *fig("TH", TX_, SB, FR, [("l2", "laechelt")], bis="t2", d=0.1),
    *redet("TH_redet", TX_, SB, FR, "t2", "ab1"),
    ns("Thekla", TX_, SB, "l2", TH_N, d=0.2),
    blase("sprech", 600, 210, "t2", 1130, 300, inhalt=["Dann lasse ich ihn nach der", "Party lieber stehen."],
          textsize=36, figur=("TH_redet", TX_, SB, FR), bis="ab1"),
])

# ===========================================================================================================================
# I1 Abgrenzung: Auslegung – Rechtsfortbildung; Analogie
# ===========================================================================================================================
folie([("ab1", "Abgrenzung · Auslegung und Rechtsfortbildung"), ("an1", "Abgrenzung · Analogie"),
       ("an3", "Abgrenzung · Analogie: § 1004 BGB")], rechts_frei([
    *tafel("ab1", "Wo die Auslegung endet"),
    blk(110, 175, 500, 70, FW, "ab1", [("Auslegung", "ExtraBold", 32, INK)], anim="pop"),
    linienzug([(630, 160), (630, 260)], beim("ab1", "endet"), breite=8, farbe=DROT),
    blk(650, 175, 500, 70, HELL, beim("ab1", "Rechtsfortbildung"), [("Rechtsfortbildung", "ExtraBold", 32, INK)],
        anim="pop"),
    z("Analogie: Norm auf einen Fall übertragen,", 110, 290, "an1", "ExtraBold", 32),
    z("den ihr Wortlaut nicht erfasst", 110, 338, beim("an1", "den"), "ExtraBold", 32),
    *okz("1. planwidrige Regelungslücke", 410, beim("an2", "planwidrige"), "Bold", 32, x=160),
    *okz("2. vergleichbare Interessenlage", 470, beim("an2", "vergleichbare"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 7.11.2019 – I ZR 42/19, Rn. 32", 160, 522, beim("an2", "vergleichbare")),
    blk(110, 585, 1040, 140, HELL, "an3", [("§ 1004 BGB: dem Wortlaut nach nur Eigentum,", "Bold", 32, INK),
                                          ("entsprechend auch Persönlichkeitsrecht", "Bold", 32, INK)]),
    pl("Beispiel", 900, 560, "an3", fill=PINK, size=28),
    zit("BGH, Urt. v. 14.12.2021 – VI ZR 403/19, Rn. 9", 110, 740, beim("an3", "Rechtsprechung")),
    *requisit([("ab1", ("tabler", "road", 110, WEISS), "Grenze", WEISS),
               ("an1", ("tabler", "arrows-right-left", 100, GELB), "Analogie", GELB),
               ("an3", ("tabler", "user-shield", 100, WEISS), "Persönlichkeitsrecht", WEISS)]),
    *paar("ab1", [("ab1", "ruhig"), ("an1", "denkt"), ("an3", "froh")], [("ab1", "ernst"), ("an2", "ruhig")]),
]))

# ===========================================================================================================================
# I2 Teleologische Reduktion und Analogieverbot
# ===========================================================================================================================
folie([("tr1", "Abgrenzung · teleologische Reduktion"), ("tr2", "Abgrenzung · teleologische Reduktion: § 181 BGB"),
       ("av", "Abgrenzung · Analogieverbot, Art. 103 Abs. 2 GG")], rechts_frei([
    *tafel("tr1", "Teleologische Reduktion"),
    z("Das Gegenstück zur Analogie:", 110, 180, "tr1", "Bold", 32),
    z("Der Wortlaut erfasst den Fall,", 110, 235, beim("tr1", "Der"), "ExtraBold", 32),
    z("der Zweck soll ihn nicht erfassen.", 110, 283, beim("tr1", "Zweck"), "ExtraBold", 32),
    blk(110, 365, 1040, 140, HELL, "tr2", [("§ 181 BGB: Insichgeschäft grundsätzlich verboten,", "Bold", 32, INK),
                                          ("nicht bei lediglich rechtlichem Vorteil", "Bold", 32, INK)]),
    pl("Beispiel", 900, 340, "tr2", fill=PINK, size=28),
    zit("BGH, Urt. v. 7.9.2017 – IX ZR 224/16, Rn. 17", 110, 520, beim("tr2", "greift")),
    blk(110, 600, 1040, 140, ROT, "av", [("Strafrecht: keine Analogie zulasten", "ExtraBold", 34, INK),
                                        ("des Täters, Art. 103 Abs. 2 GG", "ExtraBold", 34, INK)]),
    zit("BVerfG, Beschl. v. 19.3.2007 – 2 BvR 2273/06, Rn. 11", 110, 755, beim("av", "Artikel")),
    pl("mehr in Folge 148", 820, 790, beim("av", "Folge"), fill=LILA, size=30),
    *requisit([("tr1", ("tabler", "scissors", 100, WEISS), "Reduktion", WEISS),
               ("tr2", ("tabler", "user-check", 100, WEISS), "§ 181 BGB", WEISS),
               ("av", ("tabler", "ban", 100, ROT), "Analogieverbot", ROT)]),
    *paar("tr1", [("tr1", "denkt"), ("tr2", "ruhig"), ("av", "staunt")], [("tr1", "ruhig"), ("av", "ernst")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Reihenfolge der Auslegung"), ("tipp3", "Klausurtipp · Merkhilfe, keine Rangfolge"),
       ("tipp4", "Klausurtipp · Materialien nur, wenn bekannt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Beginne beim Wortlaut,", 200, 200, beim("tipp", "Beginne"), "Bold", 36),
    z("dann Systematik, Historie und Telos.", 200, 255, beim("tipp", "dann"), "Bold", 36),
    *okz("zu jeder Methode: Argument und Zwischenergebnis", 340, "tipp2", "Bold", 34, x=200),
    blk(160, 430, 990, 90, GELB, "tipp3", [("Merkhilfe: Wortlaut zuerst, Telos entscheidet oft", "ExtraBold", 34, INK)]),
    z("keine feste Rangfolge", 200, 545, beim("tipp3", "Eine"), "Bold", 32),
    zit("BVerfG 2 BvR 2628/10 u. a., Rn. 66", 560, 552, beim("tipp3", "Rangfolge")),
    *okz("Materialien nur zitieren, wenn du sie kennst", 630, "tipp4", "Bold", 34, x=200),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Klausurschema: Auslegung im Gutachten
# ===========================================================================================================================
REIHEN = [("sch", 0, "I. Auslegung", None),
          ("k1", 1, "1. Wortlaut (mit Legaldefinition)", FW),
          ("k2", 1, "2. Systematik", FS),
          ("k3", 1, "3. Historie", FH_),
          ("k4", 1, "4. Telos", FT),
          ("k5", 1, "5. Ergebnis der Auslegung", None),
          ("k6", 0, "II. Danach: Lücke oder zu weiter Wortlaut?", None),
          (beim("k6", "Analogie"), 1, "Analogie oder teleologische Reduktion,", None),
          (beim("k6", "Strafrecht"), 1, "im Strafrecht nie zulasten des Täters", None)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Auslegung im Gutachten"), 110, 90, "sch", 50)]
y = 200
for c, ebene, text, farbe in REIHEN:
    x = (130, 220)[ebene]
    if farbe:
        els_sch.append(karte(x - 14, y - 6, 36, 56, c, fill=farbe, rund=8, schatten=0, rand=4))
        x += 40
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Bold", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 80, 1: 70}[ebene] + (20 if c == "k5" else 0)
assert y <= 975, y
folie([("sch", "Klausurschema · Auslegung im Gutachten"), ("k1", "Klausurschema › I. 1. Wortlaut"),
       ("k2", "Klausurschema › I. 2. Systematik"), ("k3", "Klausurschema › I. 3. Historie"),
       ("k4", "Klausurschema › I. 4. Telos"), ("k5", "Klausurschema › I. 5. Ergebnis der Auslegung"),
       ("k6", "Klausurschema › II. Rechtsfortbildung")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Auslegen heißt, ein Gesetz", 0)], [("auf ", 0), ("4 Wegen", "a"), (" zu lesen:", 0)]], 750, 290, 44,
                "merke", {"a": beim("merke", "vier")}),
    *markertext([[("Wortlaut, Systematik, Historie, Telos.", 0)]], 750, 290 + 2 * 57, 44, beim("merke", "Wortlaut"), {}),
    *markertext([[("Der Wortlaut ist der Anfang,", 0)], [("im Strafrecht auch die ", 0), ("Grenze", "b"), (".", 0)]],
                750, 620, 44, "mm2", {"b": beim("mm2", "Grenze")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
