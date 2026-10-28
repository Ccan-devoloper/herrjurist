"""Folge 158 · § 823 II BGB: Schutzgesetzverletzung – das Prüfungsschema – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Hiltrud hat ihr Auto am Straßenrand einer Wohnstraße geparkt. Ihr Nachbar Burkhard (keine Fahrerlaubnis,
Halter seines Autos) setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich beim Rangieren und streift ihr
Auto (langer Kratzer am hinteren Kotflügel). Reparatur 900 €.
Szenen laut ../SZENENPLAN.md: A Wohnstraße, B Sachverhalt, C Wortlautkarte § 823 Abs. 2 BGB, D Aufbau (sechs Schritte),
E I. Schutzgesetz (Wortlautkarte Art. 2 EGBGB, BGH-Formel), F Klassiker und Schutznormtheorie, G § 21 StVG (Wortlautkarten
§ 21 Abs. 1 Nr. 1 und § 2 Abs. 1 S. 1 StVG), H II. Schutzbereich, I III. Verstoß / IV. Rechtswidrigkeit, J V. Verschulden,
K VI. Schaden und Rechtsfolge, L Vorteil von Abs. 2, M Lösung, N Klausurtipp (Lexi), O Prüfschema, P Merksatz (Lexi).
DARSTELLUNG: kein Aufprallbild – Burkhards Auto rollt langsam rückwärts, bis sein Heck das Heck von Hiltruds Auto streift;
danach ein feiner Kratzerstrich am hinteren Kotflügel. Zwei Handlungsgeräusche (leises Schaben, Autotür;
../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist (im Auto: Schild unter dem Auto). Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz/requisit als eigene Kopie aus Folge 149 (gemeinsame Dateien unverändert); neu: strasse(),
kulisse(), kratzer(), umbruch(), zweikarten().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_158/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_158/" in n:
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
NAME = {"HI": "Hiltrud", "BU": "Burkhard"}
NFARBE = {"HI": GELB, "BU": BLAU}           # wie die Autos


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


def zwei(folge_hi, folge_bu):
    """Hiltrud und Burkhard rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HI", X1, folge_hi), *stehend("BU", X2, folge_bu)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
ASPH = (206, 206, 202, 255)
PFLASTER = (232, 228, 218, 255)
S_O, S_U = 700, 905                          # Straße (Seitenansicht): Oberkante, Unterkante
EIN_X = 1390                                 # Beginn der Einfahrt (rechts, vor Burkhards Haus)
FAHR = 858                                   # Unterkante der Autos
FBA, FHA = 905, 470                          # Figuren auf der Straße: Unterkante, Höhe
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def _hart_wenn(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def strasse(c):
    """Wohnstraße mit Bordsteinkante; rechts die gepflasterte Einfahrt (abgesenkter Bordstein, Fugenstriche)."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (S_U - S_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (S_U - S_O) * s), fill=ASPH)
    ex = (EIN_X - 30) * s
    dr.rectangle((ex, 0, 1860 * s, 70 * s), fill=PFLASTER)                      # Einfahrt (hinten, Pflaster)
    for x in range(ex + 40 * s, 1860 * s, 60 * s):
        dr.line((x, 6 * s, x - 14 * s, 64 * s), fill=(200, 194, 182, 255), width=3 * s)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (S_U - S_O) * s - 3 * s, 1860 * s, (S_U - S_O) * s - 3 * s), fill=INK, width=6 * s)
    dr.line((0, 70 * s, ex, 70 * s), fill=INK, width=4 * s)                      # Bordsteinkante links der Einfahrt
    for x in range(60, 1300, 180):                                                # Mittelstreifen-Andeutung entfällt: Wohnstraße
        pass
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return _hart_wenn(c)(El(im, 30, S_O, c, "cut", 0.0, None, name="strasse"))


def kulisse(c):
    """Zwei Wohnhäuser (Tabler „home“), Baum, Straße mit Einfahrt."""
    h = _hart_wenn(c)
    return [strasse(c),
            h(ficon("tabler", "home", 250, S_O + 4, 270, c, fuell=GELB, anim="cut")),
            h(ficon("tabler", "tree", 470, S_O + 4, 150, c, fuell=GRUEN, anim="cut")),
            h(ficon("tabler", "home", 1640, S_O + 4, 270, c, fuell=BLAU, anim="cut"))]


def kratzer(cx, cy, cue, bis=None):
    """Langer feiner Kratzer am Kotflügel: Zickzackstrich (Grundform, Dunkelrot)."""
    pts = [(cx - 40, cy), (cx - 26, cy - 6), (cx - 12, cy + 2), (cx + 2, cy - 5), (cx + 16, cy + 1), (cx + 30, cy - 5),
           (cx + 42, cy)]
    e = linienzug(pts, cue, breite=5, farbe=DROT)
    e.bis = bis
    return e


# ===========================================================================================================================
# A Fall: die Wohnstraße
# ===========================================================================================================================
CW = 380                                     # Autobreite (Renderbreite des Icons)
CWB = ficon("tabler", "car", 0, 0, CW, "_", fuell=GELB).sprite.width     # tatsächliche Breite nach dem Zuschnitt
HX = 640                                     # Hiltruds Auto (blickt nach links, Heck rechts), parkt am Straßenrand
BXK = round(HX + CWB - 6)                    # Burkhards Auto (blickt nach rechts, Heck links) beim Streifen: Heck an Heck
BX0 = 1600                                   # Burkhards Auto in der Einfahrt
HFX, BFX0, BFX = 300, 1250, 1360             # Hiltrud vor ihrem Haus; Burkhard neben seinem Auto (vorher / nach dem Aussteigen)
B_LOS = beim("rang", "setzt")
AUS = "schaden"
folie([(NULL, "Fall · In der Wohnstraße"), ("ohne", "Fall · Burkhard ohne Fahrerlaubnis"),
       ("rang", "Fall · Rangieren aus der Einfahrt"), ("kratz", "Fall · Der Kratzer"), ("fe", "Fall · Fahrerlaubnis"),
       ("frage", "Fall · Die Frage")], [
    *kulisse(NULL),
    hart(pl("Samstagmittag: ruhige Wohnstraße", 70, 30, NULL, fill=GELB, size=38)),
    # Hiltruds Auto parkt am Straßenrand (blickt nach links); Burkhards Auto steht in der Einfahrt (blickt nach rechts)
    hart(ficon("tabler", "car", HX, FAHR, CW, NULL, fuell=GELB, spiegeln=True, anim="cut")),
    hart(bewegt(ficon("tabler", "car", BXK, FAHR, CW, NULL, fuell=BLAU, anim="cut"), B_LOS, "kratz", BX0 - BXK, 0)),
    # Hiltrud vor ihrem Haus, blickt nach rechts zur Straße
    *fig("HI", HFX, FBA, FHA, [(beim("park", "Hiltrud"), "ruhig_r"), ("kratz", "schreck_r")], bis="h1"),
    ns("Hiltrud", HFX, FBA, beim("park", "Hiltrud"), GELB, d=0.1),
    pl("Hiltrud: Auto am Straßenrand geparkt", 70, 110, beim("park", "Auto"), fill=WEISS, size=34, bis="rang"),
    # Burkhard neben seinem Auto in der Einfahrt, blickt nach links
    *fig("BU", BFX0, FBA, FHA, [(beim("burk", "Burkhard"), "ruhig"), ("ohne", "denkt")], bis=B_LOS),
    bis_(ns("Burkhard", BFX0, FBA, beim("burk", "Burkhard"), BLAU, d=0.1), B_LOS),
    pl("Nachbar Burkhard will umparken", 70, 190, beim("burk", "umparken"), fill=WEISS, size=34, bis="rang"),
    pl("keine Fahrerlaubnis, nie eine Prüfung", 70, 270, "ohne", fill=HELLROT, size=34, bis="rang"),
    ficon("tabler", "license-off", BFX0, FBA - FHA - 20, 110, "ohne", fuell=HELLROT, bis=B_LOS),
    # er steigt ein: Namensschild fährt unter dem Auto mit
    bis_(bewegt(ns("Burkhard", BXK, FAHR, B_LOS, BLAU), B_LOS, "kratz", BX0 - BXK, 0), AUS),
    pl("rückwärts aus der Einfahrt auf die Straße", 70, 110, B_LOS, fill=WEISS, size=34, bis="h1"),
    pfeil(1360, 500, 1180, 500, B_LOS, breite=10, kopf=30, bis="kratz"),
    pl("verschätzt sich beim Rangieren", 70, 190, beim("rang", "verschätzt"), fill=WEISS, size=34, bis="h1"),
    szene(pl("streift das Auto von Hiltrud", 70, 270, "kratz", fill=HELLROT, size=34, bis="h1"), "158kratzer*", 0.8, 0.0),
    kratzer(HX + CWB / 2 - 70, FAHR - 112, beim("schaden", "Kratzer")),
    pl("langer Kratzer am hinteren Kotflügel", 70, 350, beim("schaden", "Kotflügel"), fill=WEISS, size=34, bis="h1"),
    # Burkhard steigt aus (Autotür), blickt nach links zu Hiltrud
    szene(peep_voll("BU_schreck", BFX, FBA, FHA, AUS, anim="pop", bis="b1"), "158tuer*", 0.6, 0.0),
    ns("Burkhard", BFX, FBA, AUS, BLAU, d=0.1),
    *redet("HI_redet_r", HFX, FBA, FHA, "h1", "b1"),
    blase("sprech", 600, 230, "h1", 640, 250, inhalt=["Burkhard, du hast doch gar", "keinen Führerschein!"], textsize=38,
          figur=("HI_redet_r", HFX, FBA, FHA), bis="b1"),
    *fig("HI", HFX, FBA, FHA, [("b1", "skeptisch_r"), ("fe", "ernst_r"), ("frage", "sorge_r")], erst="cut"),
    *redet("BU_redet", BFX, FBA, FHA, "b1", "fe"),
    blase("sprech", 560, 200, "b1", 1180, 230, inhalt=["Ich wollte doch nur", "kurz umparken."], textsize=38,
          figur=("BU_redet", BFX, FBA, FHA), bis="fe"),
    *fig("BU", BFX, FBA, FHA, [("fe", "sorge"), ("frage", "still")], erst="cut"),
    pl("rechtlich: die Fahrerlaubnis", 70, 110, "fe", fill=WEISS, size=34, bis="frage"),
    pl("Führerschein: nur die Bescheinigung darüber", 70, 190, beim("fe", "Führerschein"), fill=WEISS, size=34, bis="frage"),
    pl("Reparatur: 900 €", 70, 270, "rep", fill=GELB, size=34, bis="frage"),
    ficon("tabler", "receipt-euro", 450, 328, 64, beim("rep", "neunhundert"), fuell=WEISS, bis="frage"),
    pl("Reparatur: 900 €", 70, 110, "frage", fill=GELB, size=34),
    ficon("tabler", "receipt-euro", 450, 168, 64, "frage", fuell=WEISS),
    pl("Hilft es, dass er ohne Fahrerlaubnis fuhr?", 70, 190, "frage", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_158(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_158("sv", [
    "An einem Samstagmittag hat Hiltrud ihr Auto ordnungsgemäß am Straßenrand einer öffentlichen Wohnstraße vor ihrem "
    "Haus geparkt. Ihr Nachbar Burkhard will sein eigenes Auto umparken. Eine Fahrerlaubnis hat er nicht; die Prüfung hat "
    "er nie gemacht.",
    "Burkhard setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich beim Rangieren und streift das Auto von "
    "Hiltrud. Am hinteren Kotflügel bleibt ein langer Kratzer. Hiltrud ruft: „Burkhard, du hast doch gar keinen "
    "Führerschein!“ Burkhard antwortet: „Ich wollte doch nur kurz umparken.“",
    "Die Reparatur kostet 900 €. Hiltrud verlangt das Geld von Burkhard.",
], "Hat Hiltrud einen Anspruch aus § 823 Abs. 2 BGB?")

# ===========================================================================================================================
# C Wortlautkarte § 823 Abs. 2 BGB
# ===========================================================================================================================
W823 = ["„Die gleiche Verpflichtung trifft denjenigen, welcher gegen ein",
        "den Schutz eines anderen bezweckendes Gesetz verstößt.",
        "Ist nach dem Inhalt des Gesetzes ein Verstoß gegen dieses auch",
        "ohne Verschulden möglich, so tritt die Ersatzpflicht nur im",
        "Falle des Verschuldens ein.“"]
_zi = lambda wort: next(i for i, t in enumerate(W823) if wort in t)
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 2 BGB", "norm", marken=[
    (_zi("gleiche Verpflichtung"), "gleiche Verpflichtung", beim("norm", "gleiche")),
    (_zi("Schutz eines anderen"), "Schutz eines anderen", beim("norm", "Schutz")),
    (_zi("verstößt"), "verstößt", beim("norm", "verstößt")),
    (_zi("ohne Verschulden"), "ohne Verschulden", beim("s2", "ohne")),
    (_zi("Falle des Verschuldens"), "Falle des Verschuldens", beim("s2", "Falle"))], size=34)
PN = "Die Norm: § 823 Abs. 2 BGB"
folie([("norm", f"{PN} › S. 1: Schutzgesetz"), ("s2", f"{PN} › S. 2: Verschulden"), ("gleich", f"{PN} › Rechtsfolge wie Abs. 1")],
      rechts_frei([
    *tafel("norm", "Die Norm: § 823 Abs. 2 BGB"),
    *w823,
    z("„gleiche Verpflichtung“: Schadensersatz wie in Abs. 1", 110, w823_y + 40, "gleich", "Bold", 32),
    z("Schema zu Abs. 1: Video „Deliktsrecht“", 110, w823_y + 90, beim("gleich", "Schema"), "Bold", 30, farbe=TEXT),
    *requisit([("norm", ("tabler", "book", 100, WEISS), "§ 823 Abs. 2 BGB", GELB),
               ("s2", ("tabler", "alert-triangle", 100, GELB), "nur mit Verschulden", HELLROT),
               ("gleich", ("tabler", "scale", 100, WEISS), "Schadensersatz", WEISS)]),
    *zwei([("norm", "ruhig"), ("s2", "skeptisch")], [("norm", "ernst"), ("gleich", "sorge")]),
]))

# ===========================================================================================================================
# D Aufbau in sechs Schritten
# ===========================================================================================================================
SCHRITTE = [("a1", "I. Schutzgesetz", GELB), ("a2", "II. Schutzbereich", BLAU), ("a3", "III. Verstoß", GRUEN),
            ("a4", "IV. Rechtswidrigkeit", LILA), ("a5", "V. Verschulden", ROT), ("a6", "VI. Schaden", HELLGRAU)]
folie([("aufbau", "Aufbau · sechs Schritte"), *[(c, f"Aufbau › {t}") for c, t, _ in SCHRITTE]], rechts_frei([
    *tafel("aufbau", "Der Aufbau: sechs Schritte"),
    *[blk(110 + (i % 2) * 530, 190 + (i // 2) * 120, 500, 90, f_, c, [(t, "ExtraBold", 36, INK)]) for i, (c, t, f_) in
      enumerate(SCHRITTE)],
    *requisit([("aufbau", ("tabler", "list-check", 100, WEISS), "Prüfschema", GELB),
               ("a1", ("tabler", "book", 100, WEISS), "Schutzgesetz", GELB),
               ("a3", ("tabler", "license-off", 100, HELLROT), "Verstoß", GRUEN),
               ("a5", ("tabler", "alert-triangle", 100, GELB), "Verschulden", ROT),
               ("a6", ("tabler", "receipt-euro", 100, WEISS), "Schaden", HELLGRAU)]),
    *zwei([("aufbau", "ernst")], [("aufbau", "ruhig"), ("a3", "sorge")]),
]))

# ===========================================================================================================================
# E I. Schutzgesetz: Art. 2 EGBGB, BGH-Formel, Allgemeinheit, kein Reflex
# ===========================================================================================================================
PI = "I. Schutzgesetz"
WEG = ["„Gesetz im Sinne des Bürgerlichen Gesetzbuchs und dieses", "Gesetzes ist jede Rechtsnorm.“"]
weg, weg_y = wortlaut(80, 165, 1100, WEG, "Art. 2 EGBGB", "eg", marken=[(1, "jede Rechtsnorm", beim("eg", "jede"))], size=32)
WF = umbruch("„… wenn sie zumindest auch dazu dienen soll, den Einzelnen oder einzelne Personenkreise gegen die Verletzung "
             "eines bestimmten Rechtsguts zu schützen.“", 32, 1040)
_zf = lambda wort: next(i for i, t in enumerate(WF) if wort in t)
wf, wf_y = wortlaut(80, weg_y + 70, 1100, WF, "BGH, Urt. v. 26.6.2023 – VIa ZR 335/21, Rn. 20", "formel", marken=[
    (_zf("zumindest auch"), "zumindest auch", beim("formel", "zumindest")),
    (_zf("den Einzelnen"), "den Einzelnen", beim("formel", "Einzelnen"))], size=32)
folie([("sg", PI), ("eg", f"{PI} › jede Rechtsnorm, Art. 2 EGBGB"), ("formel", f"{PI} › zumindest auch Schutz des Einzelnen"),
       ("allg", f"{PI} › Allgemeinheit in erster Linie: unschädlich"), ("reflex", f"{PI} › bloßer Reflex: kein Schutzgesetz")],
      rechts_frei([
    *tafel("sg", "I. Das Schutzgesetz"),
    *weg,
    z("also zum Beispiel auch eine Verordnung", 110, weg_y + 12, beim("eg", "Verordnung"), "Bold", 30),
    *wf,
    *okz("in erster Linie die Allgemeinheit: schadet nicht", wf_y + 25, beim("allg", "schadet"), "Bold", 32, x=160),
    *neinz("nur Allgemeinheit oder Ordnung, bloßer Reflex", wf_y + 78, beim("reflex", "Reflex"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 23.7.2019 – VI ZR 307/18, Rn. 12", 160, wf_y + 126, beim("reflex", "Reflex")),
    *requisit([("sg", ("tabler", "book", 100, WEISS), "Schutzgesetz?", GELB),
               ("eg", ("tabler", "file-text", 100, WEISS), "jede Rechtsnorm", WEISS),
               ("formel", ("tabler", "user-check", 100, GRUEN), "zumindest auch der Einzelne", GRUEN),
               ("allg", ("tabler", "users-group", 110, BLAU), "Allgemeinheit", WEISS),
               ("reflex", ("tabler", "users", 100, HELLGRAU), "nur Reflex", HELLROT)]),
    *zwei([("sg", "ruhig"), ("formel", "ernst")], [("sg", "denkt"), ("allg", "ruhig")]),
]))

# ===========================================================================================================================
# F Klassiker und Schutznormtheorie
# ===========================================================================================================================
LK, RK, KW = 110, 640, 510


def zweikarten(cue_l, titel_l, zeilen_l, fill_l, cue_r, titel_r, zeilen_r, fill_r, y=180, h=260):
    els = []
    for x, c, t, zl, f_ in ((LK, cue_l, titel_l, zeilen_l, fill_l), (RK, cue_r, titel_r, zeilen_r, fill_r)):
        els += [karte(x, y, KW, h, c, fill=f_, rund=18, schatten=6, rand=4),
                z(t, x + 25, y + 18, c, "ExtraBold", 34, rechts=x + KW - 10)]
        for i, (txt, cc, stil, gr) in enumerate(zl):
            els.append(z(txt, x + 25, y + 78 + i * 46, cc, stil, gr, rechts=x + KW - 10))
    return els


folie([("klass", f"{PI} › Klassiker: Strafgesetze"), ("snt", "Abgrenzung · Schutznormtheorie (Öffentliches Recht)")],
      rechts_frei([
    *tafel("klass", "Klassische Schutzgesetze"),
    *zweikarten(beim("klass", "Körperverletzung"), "Körperverletzung", [("§ 223 StGB", beim("klass", "Körperverletzung"), "Bold", 32),
                                                      ("schützt die Person", beim("klass", "Körperverletzung"), "Regular", 30)],
                HELLGRUEN,
                beim("klass", "Betrug"), "Betrug", [("§ 263 StGB", beim("klass", "Betrug"), "Bold", 32),
                                                    ("schützt das Vermögen", beim("klass", "Betrug"), "Regular", 30)], HELLGRUEN),
    zit("BGH, Urt. v. 2.12.2010 – IX ZR 41/10, Rn. 13 (§ 223 StGB);", 110, 470, beim("klass", "Betrug")),
    zit("Urt. v. 15.11.2011 – VI ZR 4/11, Rn. 9, 13 (§ 263 StGB)", 110, 508, beim("klass", "Betrug")),
    blk(110, 580, 1040, 150, HELL, "snt", [("Ähnlich: Schutznormtheorie im Öffentlichen Recht", "ExtraBold", 32, INK),
                                          ("dort: Rechte gegen den Staat, nicht Schadensersatz", "Regular", 32, INK)]),
    z("Video „Schutznormtheorie“", 110, 755, beim("snt", "dort"), "Bold", 30, farbe=TEXT),
    *requisit([("klass", ("tabler", "gavel", 100, HOLZ), "Strafgesetze", WEISS),
               ("snt", ("tabler", "building", 100, BLAU), "Öffentliches Recht", WEISS)]),
    *zwei([("klass", "ernst")], [("klass", "ruhig"), ("snt", "denkt")]),
]))

# ===========================================================================================================================
# G § 21 StVG als Schutzgesetz (Wortlautkarten § 21 Abs. 1 Nr. 1, § 2 Abs. 1 S. 1 StVG)
# ===========================================================================================================================
P21 = "I. Schutzgesetz › § 21 StVG"
W21 = ["„Mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe wird",
       "bestraft, wer 1. ein Kraftfahrzeug führt, obwohl er die dazu",
       "erforderliche Fahrerlaubnis nicht hat …“"]
w21, w21_y = wortlaut(80, 165, 1100, W21, "§ 21 Abs. 1 Nr. 1 StVG (Auszug)", "p21", marken=[
    (1, "ein Kraftfahrzeug führt", beim("p21a", "Kraftfahrzeug")),
    (2, "erforderliche Fahrerlaubnis nicht hat", beim("p21a", "erforderliche"))], size=32)
W2 = ["„Wer auf öffentlichen Straßen ein Kraftfahrzeug führt, bedarf",
      "der Erlaubnis (Fahrerlaubnis) der zuständigen Behörde …“"]
w2, w2_y = wortlaut(80, w21_y + 18, 1100, W2, "§ 2 Abs. 1 S. 1 StVG", "p2", marken=[
    (0, "auf öffentlichen Straßen", beim("p2", "öffentlichen"))], size=30)
folie([("p21", P21), ("p2", f"{P21} › § 2 StVG: öffentliche Straßen"), ("p2b", f"{P21} › Befähigung geprüft"),
       ("zweck", f"{P21} › Schutzzweck"), ("sgja", f"{P21} › Schutzgesetz (+)")], rechts_frei([
    *tafel("p21", "Im Fall: § 21 StVG"),
    *w21, *w2,
    z("Erteilung nur bei Befähigung, in einer Prüfung nachgewiesen", 110, w2_y + 22, "p2b", "Bold", 30),
    zit("§ 2 Abs. 2 S. 1 Nr. 5 StVG", 110, w2_y + 64, "p2b"),
    z("schützt die Allgemeinheit, zumindest auch jeden", 110, w2_y + 112, "zweck", "Bold", 30),
    z("anderen im Straßenverkehr vor ungeprüften Fahrern", 110, w2_y + 154, beim("zweck", "jeden"), "Bold", 30),
    blk(110, w2_y + 210, 1040, 76, GRUEN, "sgja", [("§ 21 StVG ist ein Schutzgesetz", "ExtraBold", 34, INK)]),
    *requisit([("p21", ("tabler", "license-off", 110, HELLROT), "ohne Fahrerlaubnis", HELLROT),
               ("p2", ("tabler", "road", 100, WEISS), "öffentliche Straße", WEISS),
               ("p2b", ("tabler", "certificate", 100, GELB), "Prüfung", GELB),
               ("zweck", ("tabler", "users-group", 110, BLAU), "Schutz aller im Verkehr", WEISS),
               ("sgja", ("tabler", "shield-check", 100, GRUEN), "Schutzgesetz (+)", GRUEN)]),
    *zwei([("p21", "skeptisch"), ("zweck", "ruhig")], [("p21", "sorge"), ("sgja", "muede")]),
]))
assert w2_y + 290 <= 900, w2_y

# ===========================================================================================================================
# H II. Schutzbereich: persönlich und sachlich
# ===========================================================================================================================
PII = "II. Schutzbereich"
folie([("sb", PII), ("pers", f"{PII} › persönlich"), ("sach", f"{PII} › sachlich"), ("offen", f"{PII} › Schutzzweck")],
      rechts_frei([
    *tafel("sb", "II. Der Schutzbereich"),
    karte(LK, 175, KW, 330, "pers", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("persönlich", LK + 25, 193, "pers", "ExtraBold", 34, rechts=LK + KW - 10),
    z("Geschädigter gehört zum", LK + 25, 248, beim("pers", "Geschädigte"), size=30, rechts=LK + KW - 10),
    z("geschützten Kreis", LK + 25, 290, beim("pers", "Geschädigte"), size=30, rechts=LK + KW - 10),
    z("alle anderen im", LK + 25, 358, "pers2", "Bold", 30, rechts=LK + KW - 10),
    z("Straßenverkehr: Hiltrud", LK + 25, 400, "pers2", "Bold", 30, rechts=LK + KW - 10),
    ok(LK + KW - 50, 460, beim("pers2", "Hiltrud"), gr=20),
    karte(RK, 175, KW, 330, "sach", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("sachlich", RK + 25, 193, "sach", "ExtraBold", 34, rechts=RK + KW - 10),
    z("gerade die Gefahr hat sich", RK + 25, 248, beim("sach", "gerade"), size=30, rechts=RK + KW - 10),
    z("verwirklicht", RK + 25, 290, beim("sach", "gerade"), size=30, rechts=RK + KW - 10),
    z("verschätzt beim Rangieren:", RK + 25, 358, "sach2", "Bold", 30, rechts=RK + KW - 10),
    z("ungeprüfter Fahrer", RK + 25, 400, beim("sach2", "Genau"), "Bold", 30, rechts=RK + KW - 10),
    ok(RK + KW - 50, 460, beim("sach2", "Genau"), gr=20),
    zit("BGH, Urt. v. 23.7.2019 – VI ZR 307/18, Rn. 14;", 110, 535, "sach"),
    zit("Urt. v. 26.6.2023 – VIa ZR 335/21, Rn. 20", 110, 573, "sach"),
    blk(110, 640, 1040, 150, HELL, "offen", [("Muss gerade das fehlende Können den", "Bold", 32, INK),
                                            ("Schaden verursacht haben? Hier nicht entscheidend.", "Bold", 32, INK)]),
    *requisit([("sb", ("tabler", "target", 100, WEISS), "Schutzbereich", GELB),
               ("pers", ("tabler", "user-check", 100, GRUEN), "persönlich", HELLGRUEN),
               ("sach", ("tabler", "car", 150, GELB), "sachlich", HELLGRUEN),
               ("offen", ("tabler", "bulb", 100, GELB), "Schutzzweck", WEISS)]),
    *zwei([("sb", "ruhig"), ("pers2", "froh"), ("offen", "ernst")], [("sb", "ernst"), ("sach2", "sorge")]),
]))

# ===========================================================================================================================
# I III. Verstoß, IV. Rechtswidrigkeit
# ===========================================================================================================================
folie([("verst", "III. Verstoß gegen § 21 StVG"), ("rw", "IV. Rechtswidrigkeit")], rechts_frei([
    *tafel("verst", "III. Verstoß · IV. Rechtswidrigkeit"),
    z("III. Verstoß", 110, 185, "verst", "ExtraBold", 38),
    *okz("Kraftfahrzeug geführt", 255, beim("verst2", "Auto"), "Bold", 34, x=160),
    *okz("auf der öffentlichen Straße", 320, beim("verst2", "öffentlichen"), "Bold", 34, x=160),
    *okz("ohne die erforderliche Fahrerlaubnis", 385, beim("verst2", "ohne"), "Bold", 34, x=160),
    linienzug([(130, 470), (1130, 470)], "rw", breite=3),
    z("IV. Rechtswidrigkeit", 110, 500, "rw", "ExtraBold", 38),
    *okz("durch den Verstoß indiziert", 570, beim("rw", "indiziert"), "Bold", 34, x=160),
    *neinz("Rechtfertigungsgründe: keine", 635, beim("rw", "Rechtfertigungsgründe"), "Bold", 34, x=160),
    *requisit([("verst", ("tabler", "license-off", 110, HELLROT), "Verstoß", HELLROT),
               ("verst2", ("tabler", "road", 100, WEISS), "öffentliche Straße", WEISS),
               ("rw", ("tabler", "scale", 100, WEISS), "rechtswidrig", LILA)]),
    *zwei([("verst", "ernst")], [("verst", "muede"), ("rw", "still")]),
]))

# ===========================================================================================================================
# J V. Verschulden
# ===========================================================================================================================
PV = "V. Verschulden"
folie([("vs", PV), ("vs1", f"{PV} › Bezugspunkt: der Verstoß"), ("vs2", f"{PV} › subjektiver Tatbestand des Strafgesetzes"),
       ("vs3", f"{PV} › Vorsatz (+)"), ("vs5", f"{PV} › § 823 Abs. 2 S. 2 BGB")], rechts_frei([
    *tafel("vs", "V. Das Verschulden"),
    blk(110, 175, 1040, 80, GELB, "vs1", [("Bezugspunkt: der Verstoß gegen das Schutzgesetz", "ExtraBold", 32, INK)]),
    z("Strafgesetz: dessen subjektiver Tatbestand", 110, 285, "vs2", "Bold", 32),
    z("verlangt es Vorsatz: Vorsatz im Sinne des Strafrechts", 110, 330, beim("vs2", "verlangt"), size=32),
    zit("BGH, Urt. v. 26.6.2023 – VIa ZR 335/21, Rn. 38", 110, 375, beim("vs2", "verlangt")),
    *okz("Burkhard wusste: keine Fahrerlaubnis, Vorsatz", 430, beim("vs3", "vorsätzlich"), "Bold", 32, x=160),
    z("Kratzer muss er nicht vorhergesehen haben:", 160, 495, "vs4", size=30),
    z("§ 21 StVG verlangt keinen Schaden", 160, 537, beim("vs4", "denn"), size=30),
    blk(110, 610, 1040, 150, HELLROT, "vs5", [("§ 823 Abs. 2 S. 2 BGB: auch bei einem", "Bold", 32, INK),
                                             ("verschuldensunabhängigen Schutzgesetz", "Bold", 32, INK),
                                             ("haftet nur, wer schuldhaft handelt", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 26.6.2023 – VIa ZR 335/21, Rn. 37", 110, 775, beim("vs5", "schuldhaft")),
    *requisit([("vs", ("tabler", "alert-triangle", 100, GELB), "Verschulden", ROT),
               ("vs2", ("tabler", "gavel", 100, HOLZ), "Strafrecht", WEISS),
               ("vs3", ("tabler", "bulb", 100, GELB), "wusste es", HELLROT),
               ("vs5", ("tabler", "book", 100, WEISS), "Satz 2", WEISS)]),
    *zwei([("vs", "ruhig"), ("vs3", "skeptisch")], [("vs", "ernst"), ("vs3", "still"), ("vs5", "muede")]),
]))

# ===========================================================================================================================
# K VI. Schaden, Kausalität, Rechtsfolge
# ===========================================================================================================================
folie([("sd", "VI. Schaden und Kausalität"), ("rf", "VI. Schaden › Rechtsfolge, §§ 249 ff. BGB")], rechts_frei([
    *tafel("sd", "VI. Schaden und Kausalität"),
    *okz("Kratzer am Auto von Hiltrud: Schaden", 190, beim("sd", "Schaden"), "Bold", 34, x=160),
    *okz("ohne die verbotene Fahrt kein Kratzer", 260, beim("kaus", "verbotene"), "Bold", 34, x=160),
    linienzug([(130, 345), (1130, 345)], "rf", breite=3),
    z("Rechtsfolge: §§ 249 ff. BGB", 110, 375, "rf", "ExtraBold", 36),
    z("für die Reparatur erforderlicher Geldbetrag", 110, 440, beim("rf", "erforderlichen"), "Bold", 32),
    zit("§ 249 Abs. 2 S. 1 BGB", 110, 487, beim("rf", "erforderlichen")),
    blk(110, 545, 520, 80, GELB, beim("rf", "Geldbetrag"), [("900 €", "ExtraBold", 38, INK)]),
    *requisit([("sd", ("tabler", "car", 150, GELB), "Kratzer", HELLROT),
               ("kaus", ("tabler", "link", 100, WEISS), "Kausalität", WEISS),
               ("rf", ("tabler", "receipt-euro", 100, WEISS), "900 €", GELB)]),
    *zwei([("sd", "sorge"), ("rf", "ruhig")], [("sd", "still")]),
]))

# ===========================================================================================================================
# L Vorteil von Abs. 2: reiner Vermögensschaden
# ===========================================================================================================================
folie([("vort", "Vorteil · Warum Abs. 2?"), ("vt1", "Vorteil › Abs. 1: kein Vermögensschutz als solcher"),
       ("vt2", "Vorteil › Abs. 2: auch reiner Vermögensschaden")], rechts_frei([
    *tafel("vort", "Warum lohnt Abs. 2?"),
    *zweikarten("vt1", "Abs. 1", [("bestimmte Rechtsgüter", "vt1", "Bold", 30),
                                  ("wie das Eigentum", beim("vt1", "Eigentum"), "Regular", 30),
                                  ("Vermögen als solches: nein", beim("vt1", "Vermögen"), "Bold", 30)], HELLROT,
                "vt2", "Abs. 2", [("auch reiner", "vt2", "Bold", 30),
                                  ("Vermögensschaden, wenn das", beim("vt2", "Vermögensschaden"), "Regular", 30),
                                  ("Schutzgesetz ihn erfasst", beim("vt2", "Schutzgesetz"), "Regular", 30)], HELLGRUEN,
                y=180, h=290),
    zit("BGH, Urt. v. 5.4.2018 – III ZR 211/17, Rn. 19", 110, 495, beim("vt1", "Vermögen")),
    blk(110, 560, 1040, 80, GELB, beim("vt2", "Betrug"), [("Beispiel: Betrug, § 263 StGB", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 15.11.2011 – VI ZR 4/11, Rn. 9", 110, 655, beim("vt2", "Betrug")),
    *requisit([("vort", ("tabler", "bulb", 100, GELB), "Vorteil", WEISS),
               ("vt1", ("tabler", "home", 110, GELB), "Eigentum", HELLROT),
               ("vt2", ("tabler", "wallet", 100, GELB), "Vermögen", HELLGRUEN)]),
    *zwei([("vort", "ruhig")], [("vort", "denkt")]),
]))

# ===========================================================================================================================
# M Lösung
# ===========================================================================================================================
folie([("loes", "Lösung · Hiltrud gegen Burkhard"), ("l2", "Lösung › daneben § 823 Abs. 1 BGB"),
       ("l3", "Lösung › daneben § 7 StVG")], rechts_frei([
    *tafel("loes", "Lösung: Hiltrud gegen Burkhard"),
    blk(110, 180, 1040, 150, GRUEN, "l1", [("§ 823 Abs. 2 BGB i. V. m. § 21 StVG:", "ExtraBold", 34, INK),
                                          ("Burkhard ersetzt die 900 €", "ExtraBold", 34, INK)]),
    *okz("daneben § 823 Abs. 1 BGB: Eigentum fahrlässig verletzt", 375, "l2", "Bold", 32, x=160),
    *okz("§ 7 StVG: Burkhard ist Halter, ohne Verschulden", 440, "l3", "Bold", 32, x=160),
    z("Video „Halterhaftung“", 160, 492, beim("l3", "siehe"), "Bold", 30, farbe=TEXT),
    *requisit([("loes", ("tabler", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("l1", ("tabler", "coin-euro", 100, GELB), "900 €", GRUEN),
               ("l2", ("tabler", "home", 110, GELB), "§ 823 Abs. 1", WEISS),
               ("l3", ("tabler", "car", 150, BLAU), "Halter", BLAU)]),
    *zwei([("loes", "ernst"), ("l1", "froh")], [("loes", "sorge"), ("l1", "muede")]),
]))

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · konkretes Schutzgesetz zitieren"), ("tp2", "Klausurtipp · Schutzgesetz inzident prüfen"),
       ("tp3", "Klausurtipp · öffentliche Straße?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zitiere das konkrete Schutzgesetz:", 200, 200, beim("tipp", "Zitiere"), "Bold", 36),
    z("§ 823 Abs. 2 BGB i. V. m. § 21 StVG", 200, 262, "tp1", size=34),
    z("Schutzgesetz inzident prüfen:", 200, 345, "tp2", "Bold", 36),
    z("objektiver und subjektiver Tatbestand", 200, 405, beim("tp2", "objektivem"), size=34),
    linienzug([(130, 485), (1130, 485)], "tp3", breite=3),
    z("Achte auf den Ort:", 200, 515, "tp3", "Bold", 36),
    z("nur private Einfahrt: in der Regel keine", 200, 575, beim("tp3", "Wer"), size=34),
    z("öffentliche Straße, keine Fahrerlaubnis nötig", 200, 620, beim("tp3", "öffentlichen"), size=34),
    zit("§ 2 Abs. 1 S. 1 StVG", 200, 670, beim("tp3", "öffentlichen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Schutzgesetz", True),
          ("c1", 1, "Rechtsnorm (Art. 2 EGBGB), die zumindest auch den Einzelnen schützt", False),
          ("c2", 0, "II. Schutzbereich", True),
          ("c2", 1, "persönlich und sachlich", False),
          ("c3", 0, "III. Verstoß gegen das Schutzgesetz", True),
          ("c4", 0, "IV. Rechtswidrigkeit", True),
          ("c5", 0, "V. Verschulden", True),
          ("c5", 1, "bezogen auf den Verstoß; § 823 Abs. 2 S. 2 BGB", False),
          ("c6", 0, "VI. Schaden und Kausalität", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: § 823 Abs. 2 BGB"), 110, 90, "sch", 46),
           z("Anspruch aus § 823 Abs. 2 BGB i. V. m. dem Schutzgesetz", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 80, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Schutzgesetz"), ("c2", "Prüfschema › II. Schutzbereich"),
       ("c3", "Prüfschema › III. Verstoß"), ("c4", "Prüfschema › IV. Rechtswidrigkeit"), ("c5", "Prüfschema › V. Verschulden"),
       ("c6", "Prüfschema › VI. Schaden und Kausalität")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("§ 823 Abs. 2 BGB macht aus einem", 0)], [("Gesetz, das den Einzelnen schützt,", 0)],
                 [("einen ", 0), ("Anspruch auf Schadensersatz", "a"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "Anspruch")}),
    *markertext([[("Das Verschulden prüfst du", 0)], [("am ", 0), ("Verstoß", "b"), (" gegen dieses Gesetz.", 0)]],
                750, 600, 44, "m2", {"b": beim("m2", "Verstoß")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
