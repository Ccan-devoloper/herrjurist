"""Folge 143 · Fraport-Urteil: Gilt das Grundgesetz für eine Flughafen-AG? – Serienstandard Open Peeps (Katzenkönig).
Echter Fall sachlich (BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, BVerfGE 128, 226; Rn. laut bundesverfassungsgericht.de):
Flugblätter im Terminal 1 (11.3.2003), Flughafenverbot der Fraport AG, Instanzen, Verfassungsbeschwerde. Reale Beteiligte
werden nicht dargestellt; fiktive Figuren im realen Schauplatz: Dorothea (Reisende) und Herr Sievers (Mitarbeiter der
Flughafengesellschaft). Neutrales Terminal aus Grundformen, kein Logo, Flugblattinhalt nur sachlich.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus
Folge 118 (gemeinsame Dateien unverändert); neu: terminal(), torte(), instanz(). Zahlen auf Tafeln, Pillen und Blasen als
Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_143/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_143/" in n:
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



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s




def terminal(cue):
    """Neutrales Terminal aus Grundformen (kein Logo): Fensterband mit Flugzeug, Schild „TERMINAL 1“, Abflugtafel, Schalter."""
    els = []
    # Fensterband rechts oben
    im, dr, s = _flaeche(800, 150)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + 800 * s, o + 150 * s), 12 * s, fill=BLAUHELL, outline=INK, width=5 * s)
    for i in range(1, 4):
        xx = o + i * 200 * s
        dr.line((xx, o, xx, o + 150 * s), fill=INK, width=4 * s)
    im = im.resize((812, 162), Image.LANCZOS)
    els.append(El(im, 1054, 34, cue, "cut", 0.0, None, name="fenster"))
    els.append(ficon("tabler", "plane-departure", 1560, 170, 150, cue, fuell=WEISS, anim="cut"))
    # Abflugtafel über dem Schalter
    im, dr, s = _flaeche(470, 150)
    dr.rounded_rectangle((o, o, o + 470 * s, o + 150 * s), 12 * s, fill=(60, 66, 84, 255), outline=INK, width=5 * s)
    f = F("ExtraBold", 30 * s)
    dr.text((o + 24 * s, o + 14 * s), "ABFLUG · TERMINAL 1", font=f, fill=GELB)
    for i in range(3):
        yy = o + (66 + i * 26) * s
        dr.rounded_rectangle((o + 24 * s, yy, o + 420 * s, yy + 14 * s), 5 * s, fill=(170, 176, 190, 255))
    im = im.resize((482, 162), Image.LANCZOS)
    els.append(El(im, 84, 484, cue, "cut", 0.0, None, name="abflug"))
    # Schalter
    im, dr, s = _flaeche(470, 190)
    dr.rectangle((o, o + 30 * s, o + 470 * s, o + 190 * s), fill=WEISS, outline=INK, width=5 * s)
    dr.rounded_rectangle((o - 2 * s, o, o + 472 * s, o + 36 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for i in (1, 2):
        xx = o + i * 157 * s
        dr.line((xx, o + 36 * s, xx, o + 190 * s), fill=INK, width=4 * s)
    im = im.resize((482, 202), Image.LANCZOS)
    els.append(El(im, 84, BODEN - 196, cue, "cut", 0.0, None, name="schalter"))
    return els


def torte(cx, cy, r, anteil, cue_a, cue_b, fa=GRUEN, fb=WEISS):
    """Tortendiagramm aus zwei Sektoren (öffentlich/privat), jeder Sektor erscheint zu seinem Wort."""
    els = []
    s = 2
    for k, (c, f_, a0, a1) in enumerate(((cue_a, fa, -90, -90 + 360 * anteil), (cue_b, fb, -90 + 360 * anteil, 270))):
        im = Image.new("RGBA", ((2 * r + 16) * s, (2 * r + 16) * s))
        dr = ImageDraw.Draw(im)
        bb = (8 * s, 8 * s, (2 * r + 8) * s, (2 * r + 8) * s)
        dr.pieslice(bb, a0, a1, fill=f_, outline=INK, width=6 * s)
        im = im.resize((2 * r + 16, 2 * r + 16), Image.LANCZOS)
        els.append(El(im, cx - r - 8, cy - r - 8, c, "fade", 0.0, None, name=f"torte{k}"))
    return els


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SI": "Herr Sievers", "DO": "Dorothea"}
NFARBE = {"SI": BLAU, "DO": GRUEN}
BRIEF = (255, 255, 255, 255)


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def requisit(folge, px=PX, bis=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def spricht_neben(k, x, cue, bis, davor, danach, zeilen, size=32, cy=250, w=600, h=200, cx=None):
    """Figur neben der Tafel spricht (Grundbild bis cue, Rede cue→bis, danach Folge); Blase über den Figuren."""
    els = [*fig(k, x, FB, FR, davor, bis=cue)] if davor else []
    els += redet(f"{k}_redet", x, FB, FR, cue, bis)
    els += fig(k, x, FB, FR, danach, erst="cut")
    els.append(blase("sprech", w, h, cue, cx or 1560, cy, inhalt=zeilen, textsize=size, figur=(f"{k}_redet", x, FB, FR),
                     bis=bis))
    return rechts_frei(els)


# ===========================================================================================================================
# A1 Fall: Terminal 1, 11.3.2003 (Rn. 9, 10)
# ===========================================================================================================================
DOX, SIX = 1080, 1620
FLUG_HAND = beim("flug", "Flugblätter")
folie([(NULL, "Fall · Terminal 1, 11.3.2003"), ("verbot", "Fall · Das Flughafenverbot")], [
    boden(NULL),
    *[hart(e) for e in terminal(NULL)],
    pl("Frankfurter Flughafen · 11.3.2003 · Terminal 1", 70, 30, beim("fall", "Frankfurter"), fill=GELB, size=34),
    pl("1 Aktivistin + 5 weitere: Initiative gegen Abschiebungen", 70, 110, "akt", fill=WEISS, size=30),
    pl("Flugblätter zu einer bevorstehenden Abschiebung", 70, 182, "flug", fill=HELL, size=30),
    *[ficon("tabler", "file-text", x_, BODEN - 196, 54, FLUG_HAND, fuell=GELB, d=d_) for x_, d_ in
      ((190, 0.0), (250, 0.15), (310, 0.3))],
    pl("Aktion beendet: Flughafengesellschaft, Bundesgrenzschutz", 70, 254, "ende", fill=WEISS, size=30),
    # Dorothea (Reisende) mit Koffer, bekommt ein Flugblatt; blickt erst zum Schalter, dann zu Herrn Sievers
    ficon("tabler", "luggage", DOX + 150, BODEN, 110, NULL, fuell=BLAUHELL, anim="cut"),
    *fig("DO", DOX, BODEN, FH, [(NULL, "ruhig"), ("flug", "denkt"), ("ende", "denkt_r"), ("verbot", "sorge_r")],
         erst="cut"),
    hart(ns("Dorothea", DOX, BODEN, NULL, GRUEN)),
    szene(bewegt(ficon("tabler", "file-text", DOX - 72, BODEN - 180, 60, (FLUG_HAND[0], FLUG_HAND[1] + 0.3), fuell=GELB,
                       anim="cut"), (FLUG_HAND[0], FLUG_HAND[1] + 0.3), (FLUG_HAND[0], FLUG_HAND[1] + 1.1), -520, -20),
          "143papier*", 0.7, -0.3),
    # Herr Sievers (Flughafengesellschaft) kommt von rechts, blickt nach links
    bewegt(peep_voll("SI_ruhig", SIX, BODEN, FH, "ende", anim="cut", bis="b1"), "ende", ("ende", 1.0), 70, 0),
    *redet("SI_redet", SIX, BODEN, FH, "b1", "verbot"),
    *fig("SI", SIX, BODEN, FH, [("verbot", "ruhig")], erst="cut"),
    bewegt(ns("Herr Sievers", SIX, BODEN, "ende", BLAU, anim="cut"), "ende", ("ende", 1.0), 70, 0),
    blase("sprech", 620, 240, "b1", 1390, 290, inhalt=["Ohne unsere Erlaubnis", "keine Flugblätter und keine",
                                                      "Demonstrationen im Terminal."], textsize=31,
          figur=("SI_redet", SIX, BODEN, FH), bis="verbot"),
    # Flughafenverbot per Brief (12.3.2003)
    pl("12.3.2003 · Flughafenverbot", 70, 326, "verbot", fill=HELLROT, size=32),
    ficon("tabler", "mail", 640, 395, 74, beim("verbot", "Flughafenverbot"), fuell=WEISS),
    pl("sonst: Strafantrag wegen Hausfriedensbruchs", 70, 398, "straf", fill=WEISS, size=30),
])

# ===========================================================================================================================
# A2 Wem gehört die Fraport? (Rn. 2)
# ===========================================================================================================================
folie([("aktien", "Fall · Wem gehört die Fraport?"), ("d1", "Fall · Darf eine AG das verbieten?")], [
    *tafel("aktien", "Wem gehört die Fraport AG (2003)?"),
    *torte(330, 430, 170, 0.70, beim("aktien", "siebzig"), "privat"),
    pl("rund 70 %", 405, 462, beim("aktien", "siebzig"), fill=WEISS, size=32, anker="m"),
    z("rund 70 % öffentlich:", 560, 300, beim("aktien", "siebzig"), "ExtraBold", 34),
    z("Land Hessen", 560, 350, beim("aktien", "Hessen"), size=34),
    z("Stadt Frankfurt", 560, 396, beim("aktien", "Stadt"), size=34),
    z("Bund", 560, 442, beim("aktien", "Bund"), size=34),
    z("Rest: private Aktionäre", 560, 520, "privat", "ExtraBold", 34),
    zit("BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, Rn. 2", 110, 680, "aktien"),
    *stehend("SI", X1, [("aktien", "ruhig")]),
    *spricht_neben("DO", X2, "d1", "klage", [("aktien", "ruhig")], [],
                   ["Darf eine Aktiengesellschaft", "so etwas einfach verbieten?"], size=32, cx=1580),
    bis_(ns("Dorothea", X2, FB, "aktien", GRUEN, d=0.1), "klage"),
])

# ===========================================================================================================================
# A3 Der Weg durch die Instanzen (Rn. 11–19), Frage
# ===========================================================================================================================
folie([("klage", "Fall · Der Weg durch die Instanzen"), ("vb", "Fall · Verfassungsbeschwerde"), ("frage", "Fall · Die Frage")], [
    *tafel("klage", "Der Weg durch die Instanzen"),
    z("Die Aktivistin klagt gegen das Flughafenverbot.", 110, 170, "klage", "Bold", 32),
    *neinz("Amtsgericht Frankfurt: abgewiesen", 235, beim("aglg", "Amtsgericht"), "Bold", 32, x=160),
    *neinz("Landgericht Frankfurt: abgewiesen", 290, beim("aglg", "Landgericht"), "Bold", 32, x=160),
    z("Hausrecht; nicht unmittelbar an die Grundrechte gebunden", 160, 340, beim("aglg", "Hausrecht"), size=30),
    *neinz("BGH, 20.1.2006 – V ZR 134/05: abgewiesen", 405, "bgh", "Bold", 32, x=160),
    z("Bindung offen; Verbot jedenfalls verhältnismäßig", 160, 455, beim("bgh", "offen"), size=30),
    zit("BVerfG, 1 BvR 699/06, Rn. 11–18", 160, 500, beim("bgh", "offen")),
    z("Verfassungsbeschwerde zum Bundesverfassungsgericht", 110, 560, "vb", "ExtraBold", 32),
    pl("Gilt das Grundgesetz für eine Flughafen-AG?", 110, 630, "frage", fill=PINK, size=34),
    pl("Und ist ein Terminal ein Ort für Demonstrationen", 110, 715, "frage2", fill=WEISS, size=30),
    pl("und Flugblätter?", 110, 778, beim("frage2", "Flugblätter"), fill=WEISS, size=30),
    *requisit([("klage", ("tabler", "file-text", 90, WEISS), "Klage", WEISS),
               ("aglg", ("tabler", "gavel", 100, HOLZ), "Zivilgerichte", WEISS),
               ("vb", ("tabler", "building-bank", 120, WEISS), "Karlsruhe", GELB),
               ("frage", ("tabler", "building-airport", 120, WEISS), "Grundgesetz für die AG?", PINK)]),
    *paar("SI", [("klage", "ruhig"), ("vb", "denkt")], "DO", [("klage", "denkt"), ("frage", "sorge")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_143(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_143("sv", [
    "Frankfurter Flughafen, 11. März 2003: Eine Aktivistin geht mit fünf weiteren Aktivisten einer Initiative gegen "
    "Abschiebungen in Terminal 1 und verteilt Flugblätter zu einer bevorstehenden Abschiebung. Mitarbeiter der "
    "Flughafengesellschaft und der Bundesgrenzschutz beenden die Aktion.",
    "Am 12. März 2003 erteilt die Betreiberin, die Fraport AG, ihr ein Flughafenverbot: Ohne Erlaubnis darf sie den "
    "Flughafen nicht für Meinungskundgaben und Demonstrationen nutzen; sonst droht ein Strafantrag wegen "
    "Hausfriedensbruchs. Land Hessen, Stadt Frankfurt und Bund halten damals rund 70 % der Aktien, der Rest ist in "
    "privater Hand.",
    "Die Klage der Aktivistin bleibt vor Amtsgericht, Landgericht und Bundesgerichtshof ohne Erfolg. Sie erhebt "
    "Verfassungsbeschwerde.",
], "Verletzen die Urteile, die das Flughafenverbot bestätigen, ihre Grundrechte?")

# ===========================================================================================================================
# C1 Grundrechtsbindung: Art. 1 Abs. 3 GG (Wortlautkarte), keine Flucht ins Privatrecht (Rn. 46–48)
# ===========================================================================================================================
PB = "Grundrechtsbindung"
W13 = ["„(3) Die nachfolgenden Grundrechte binden Gesetzgebung,",
       "vollziehende Gewalt und Rechtsprechung als unmittelbar",
       "geltendes Recht.“"]
w13, w13_y = wortlaut(80, 230, 1100, W13, "Art. 1 Abs. 3 GG", "a13", marken=[
    (0, "binden", beim("a13", "binden")), (1, "vollziehende Gewalt", beim("a13", "vollziehende")),
    (1, "unmittelbar", beim("a13", "unmittelbar"))], size=33)
folie([("bind", f"{PB} · BVerfG, 22.2.2011"), ("a13", f"{PB} › Art. 1 Abs. 3 GG"),
       ("flucht", f"{PB} › auch in privatrechtlicher Form"), ("verstellt", f"{PB} › keine Flucht ins Privatrecht"),
       ("frei", f"{PB} › Bürger frei, Staat gebunden")], [
    *tafel("bind", "Erster Schritt: die Grundrechtsbindung"),
    zit("BVerfG, Urteil vom 22.2.2011 – 1 BvR 699/06 (BVerfGE 128, 226)", 110, 168, "bind"),
    *w13,
    *okz("auch in privatrechtlicher Form gebunden", w13_y + 30, "flucht", "Bold", 34, x=160),
    zit("BVerfG, 1 BvR 699/06, Rn. 46", 160, w13_y + 80, "flucht"),
    *neinz("keine Flucht ins Privatrecht", w13_y + 135, beim("verstellt", "Flucht"), "Bold", 34, x=160),
    zit("Rn. 48", 160, w13_y + 185, beim("verstellt", "Flucht")),
    blk(110, w13_y + 245, 1040, 80, GELB, "frei", [("Bürger: prinzipiell frei · Staat: prinzipiell gebunden", "ExtraBold", 33, INK)]),
    *requisit([("bind", ("tabler", "building-bank", 120, WEISS), "BVerfG, 22.2.2011", GELB),
               ("a13", ("tabler", "book", 100, WEISS), "Art. 1 Abs. 3 GG", GELB)], bis="s1b"),
    *requisit([("flucht", ("tabler", "building-airport", 120, WEISS), "Privatrechtsform", WEISS),
               ("frei", ("tabler", "scale", 100, GELB), "frei / gebunden", GELB)]),
    *spricht_neben("SI", FX, "s1b", "flucht", [("bind", "ruhig")], [("flucht", "denkt"), ("frei", "sorge")],
                   ["Wir sind doch eine", "Aktiengesellschaft", "wie jede andere."], size=32, h=240),
    ns("Herr Sievers", FX, FB, "bind", BLAU, d=0.1),
])

# ===========================================================================================================================
# C2 Gemischtwirtschaftliche Unternehmen: Beherrschung (Rn. 49–53)
# ===========================================================================================================================
folie([("gemischt", f"{PB} › gemischtwirtschaftliche Unternehmen"), ("beherr", f"{PB} › Beherrschung"),
       ("haelfte", f"{PB} › mehr als 50 % öffentlich"), ("quote", f"{PB} › keine Bindung nach Quoten")], [
    *tafel("gemischt", "Gemischtwirtschaftliche Unternehmen"),
    z("Staat und Private sind beteiligt", 110, 180, "gemischt", "Bold", 34),
    *torte(1050, 365, 70, 0.55, beim("gemischt", "Staat"), beim("gemischt", "Private"), fa=GRUEN, fb=WEISS),
    *okz("gebunden, wenn die öffentliche Hand beherrscht", 260, "beherr", "Bold", 34, x=160),
    zit("BVerfG, 1 BvR 699/06, Rn. 49, 51", 160, 310, "beherr"),
    blk(110, 440, 1040, 120, GRUEN, "haelfte", [("in der Regel: mehr als die Hälfte", "ExtraBold", 36, INK),
                                              ("der Anteile in öffentlicher Hand", "ExtraBold", 36, INK)]),
    zit("Rn. 53 (Anknüpfung an §§ 16, 17 AktG)", 110, 575, "haelfte"),
    *neinz("keine Grundrechtsbindung nach Quoten", 650, "quote", "Bold", 34, x=160),
    zit("Rn. 52", 160, 700, "quote"),
    *requisit([("gemischt", ("tabler", "chart-pie", 110, GRUEN), "Staat + Private", WEISS),
               ("haelfte", ("tabler", "chart-pie-2", 110, GRUEN), "mehr als 50 %", GRUEN),
               ("quote", ("tabler", "x", 90, WEISS), "nicht nach Quoten", HELLROT)]),
    *paar("SI", [("gemischt", "denkt")], "DO", [("gemischt", "ruhig"), ("haelfte", "froh")]),
])

# ===========================================================================================================================
# C3 Fraport unmittelbar gebunden, keine eigenen Grundrechte, private Aktionäre (Rn. 45, 54, 55, 60, 86)
# ===========================================================================================================================
folie([("fraport", f"{PB} › Fraport: unmittelbar gebunden"), ("eigen", f"{PB} › keine eigenen Grundrechte"),
       ("aktion", f"{PB} › private Aktionäre")], [
    *tafel("fraport", "Und die Fraport?"),
    blk(110, 180, 1040, 120, GRUEN, "fraport", [("Fraport AG (2003 rund 70 % öffentlich):", "ExtraBold", 34, INK),
                                              ("unmittelbar an die Grundrechte gebunden", "ExtraBold", 34, INK)]),
    zit("BVerfG, 1 BvR 699/06, Rn. 2, 60", 110, 315, "fraport"),
    *neinz("keine eigenen Grundrechte gegenüber der", 395, "eigen", "Bold", 34, x=160),
    z("Aktivistin, etwa das Eigentum", 160, 443, beim("eigen", "Eigentum"), "Bold", 34),
    zit("Rn. 45, 54, 86", 160, 493, beim("eigen", "Eigentum")),
    z("Private Aktionäre: freiwillig beteiligt", 110, 575, "aktion", "Bold", 34),
    z("keine ungerechtfertigte Einbuße", 110, 623, beim("aktion", "keine"), size=34),
    zit("Rn. 55", 110, 673, beim("aktion", "keine")),
    *requisit([("fraport", ("tabler", "building-airport", 120, GRUEN), "unmittelbar gebunden", GRUEN),
               ("eigen", ("tabler", "key", 100, WEISS), "kein Eigentumsgrundrecht", HELLROT),
               ("aktion", ("tabler", "chart-pie", 110, WEISS), "private Aktionäre", WEISS)]),
    *paar("SI", [("fraport", "sorge"), ("aktion", "ruhig")], "DO", [("fraport", "froh")]),
])

# ===========================================================================================================================
# D1 Versammlungsfreiheit: Art. 8 Abs. 1 GG (Wortlautkarte), Wahl des Ortes (Rn. 63, 64)
# ===========================================================================================================================
PV = "Art. 8 Abs. 1 GG"
W8 = ["„(1) Alle Deutschen haben das Recht, sich ohne Anmeldung",
      "oder Erlaubnis friedlich und ohne Waffen zu versammeln.“"]
w8, w8_y = wortlaut(80, 190, 1100, W8, "Art. 8 Abs. 1 GG", "a8", marken=[
    (0, "ohne Anmeldung", beim("a8", "Anmeldung")), (1, "oder Erlaubnis", beim("a8", "Erlaubnis")),
    (1, "versammeln", beim("a8", "versammeln"))], size=33)
folie([("a8", f"{PV} · Versammlungsfreiheit"), ("ort", f"{PV} › Schutzbereich: Wahl des Ortes")], [
    *tafel("a8", "Zweiter Schritt: die Versammlungsfreiheit"),
    *w8,
    *okz("geschützt auch: die Wahl des Ortes", w8_y + 40, "ort", "Bold", 36, x=160),
    zit("BVerfG, 1 BvR 699/06, Rn. 64", 160, w8_y + 92, "ort"),
    *requisit([("a8", ("tabler", "book", 100, WEISS), "Art. 8 Abs. 1 GG", GELB),
               ("ort", ("tabler", "map-pin", 90, ROT), "Wahl des Ortes", WEISS)]),
    *stehend("DO", FX, [("a8", "ruhig"), ("ort", "froh")]),
])

# ===========================================================================================================================
# D2 Kein Zutrittsrecht zu beliebigen Orten (Rn. 65, 69, 72)
# ===========================================================================================================================
def kachel(setname, name, cx, txt, cue, fuell=WEISS, y=255):
    """Icon mit Beschriftung auf der Tafel und Bleistift-Kreuz (nicht geschützt)."""
    return [ficon(setname, name, cx, y + 120, 100, cue, fuell=fuell), pl(txt, cx, y + 140, cue, fill=WEISS, size=28, anker="m"),
            nein(cx + 62, y + 10, cue, gr=22)]


folie([("kein", f"{PV} › kein Zutritt zu beliebigen Orten"), ("schleuse", f"{PV} › nicht: Sicherheitsbereich"),
       ("gepaeck", f"{PV} › nicht: reine Funktionsbereiche")], [
    *tafel("kein", "Kein Zutrittsrecht zu beliebigen Orten"),
    z("Nicht geschützt sind etwa Versammlungen in …", 110, 180, "nicht", "Bold", 32),
    *kachel("tabler", "building", 260, "Verwaltungsgebäuden", beim("nicht", "Verwaltungsgebäuden")),
    *kachel("tabler", "swimming", 620, "Schwimmbädern", beim("nicht", "Schwimmbädern"), fuell=BLAUHELL),
    *kachel("tabler", "building-hospital", 960, "Krankenhäusern", beim("nicht", "Krankenhäusern")),
    zit("BVerfG, 1 BvR 699/06, Rn. 65", 110, 460, beim("nicht", "Krankenhäusern")),
    *neinz("hinter der Sicherheitskontrolle: nur Fluggäste", 530, "schleuse", "Bold", 34, x=160),
    zit("Rn. 69", 160, 580, "schleuse"),
    *neinz("Gepäckausgabe: dient nur einer Funktion", 645, "gepaeck", "Bold", 34, x=160),
    zit("Rn. 72", 160, 695, "gepaeck"),
    *requisit([("kein", ("tabler", "lock", 90, WEISS), "kein Zutrittsrecht", HELLROT),
               ("schleuse", ("tabler", "scan", 100, WEISS), "Sicherheitskontrolle", WEISS),
               ("gepaeck", ("tabler", "luggage", 100, BLAUHELL), "Gepäckausgabe", WEISS)]),
    *stehend("DO", FX, [("kein", "denkt"), ("schleuse", "sorge")]),
])

# ===========================================================================================================================
# D3 Das öffentliche Forum, Eingriff (Rn. 66, 70, 72, 73)
# ===========================================================================================================================
def kachel_ok(setname, name, cx, txt, cue, fuell=WEISS, y=312):
    return [ficon(setname, name, cx, y + 110, 96, cue, fuell=fuell), pl(txt, cx, y + 128, cue, fill=WEISS, size=28, anker="m")]


folie([("forum", f"{PV} › allgemeiner öffentlicher Verkehr"), ("leitbild", f"{PV} › Leitbild: öffentliches Forum"),
       ("ffm", f"{PV} › Frankfurter Flughafen (+)"), ("eingriff", "Art. 8 Abs. 1 GG › Eingriff")], [
    *tafel("forum", "Das öffentliche Forum"),
    *okz("geschützt: wo allgemeiner öffentlicher Verkehr eröffnet ist", 175, "forum", "Bold", 32, x=160),
    z("Leitbild: das öffentliche Forum", 110, 250, "leitbild", "ExtraBold", 34),
    *kachel_ok("tabler", "shopping-bag", 230, "Läden", beim("leitbild", "Läden"), fuell=GELB),
    *kachel_ok("tabler", "coffee", 470, "Cafés", beim("leitbild", "Cafés"), fuell=HOLZ),
    *kachel_ok("tabler", "armchair", 710, "Flanieren", beim("leitbild", "Flanieren"), fuell=BLAUHELL),
    z("offen für viele verschiedene Tätigkeiten", 110, 520, beim("leitbild", "offen"), size=32),
    zit("BVerfG, 1 BvR 699/06, Rn. 66, 70", 110, 565, beim("leitbild", "offen")),
    *okz("Frankfurter Flughafen: in wesentlichen Bereichen so gestaltet", 620, "ffm", "Bold", 31, x=160),
    zit("Rn. 72", 160, 668, "ffm"),
    blk(110, 720, 1040, 120, GELB, "eingriff", [("Eingriff: unbefristetes Verbot", "ExtraBold", 34, INK),
                                               ("für den ganzen Flughafen (Rn. 73)", "ExtraBold", 34, INK)]),
    *requisit([("forum", ("tabler", "building-airport", 120, WEISS), "öffentlicher Verkehr", WEISS),
               ("leitbild", ("tabler", "shopping-bag", 100, GELB), "öffentliches Forum", GELB),
               ("eingriff", ("tabler", "ban", 90, HELLROT), "Eingriff", HELLROT)]),
    *paar("SI", [("forum", "ruhig"), ("eingriff", "sorge")], "DO", [("forum", "ruhig"), ("ffm", "froh")]),
])

# ===========================================================================================================================
# E Meinungsfreiheit, Art. 5 Abs. 1 Satz 1 GG (Rn. 97, 98)
# ===========================================================================================================================
P5 = "Art. 5 Abs. 1 Satz 1 GG"
folie([("a5", f"{P5} · Meinungsfreiheit"), ("blatt", f"{P5} › Flugblätter verteilen"), ("raum", f"{P5} › ohne Raumbezug")], [
    *tafel("a5", "Dazu: die Meinungsfreiheit, Art. 5 Abs. 1 GG"),
    *okz("Flugblätter verteilen: geschützte Form,", 190, "blatt", "Bold", 34, x=160),
    z("eine Meinung zu verbreiten", 160, 238, beim("blatt", "Meinung"), "Bold", 34),
    zit("BVerfG, 1 BvR 699/06, Rn. 97", 160, 288, beim("blatt", "Meinung")),
    z("Anders als die Versammlung: kein besonderer Raum", 110, 370, "raum", "Bold", 34),
    blk(110, 440, 1040, 80, GRUEN, beim("raum", "überall"), [("gilt überall, wo man tatsächlich Zugang hat", "ExtraBold", 34, INK)]),
    zit("Rn. 98", 110, 535, beim("raum", "überall")),
    *requisit([("a5", ("tabler", "message", 100, WEISS), "Meinungsfreiheit", GELB),
               ("blatt", ("tabler", "file-text", 90, GELB), "Flugblatt", HELL),
               ("raum", ("tabler", "map-pin", 90, ROT), "überall mit Zugang", WEISS)]),
    *stehend("DO", FX, [("a5", "ruhig"), ("blatt", "froh")]),
])

# ===========================================================================================================================
# F1 Rechtfertigung: „unter freiem Himmel“, Hausrecht, allgemeines Gesetz (Rn. 76–79, 100)
# ===========================================================================================================================
PR = "Rechtfertigung"
folie([("schranke", f"{PR} · Schranken"), ("himmel", f"{PR} › „unter freiem Himmel“, Art. 8 Abs. 2 GG"),
       ("hausr", f"{PR} › Hausrecht, §§ 903, 1004 BGB"), ("allg", f"{PR} › Art. 5: allgemeines Gesetz")], [
    *tafel("schranke", "Dritter Schritt: die Rechtfertigung"),
    z("Versammlung im Terminal: „unter freiem Himmel“", 110, 180, "himmel", "Bold", 34),
    z("überdacht, aber mitten im allgemeinen Publikum", 110, 228, beim("himmel", "überdacht"), size=34),
    zit("BVerfG, 1 BvR 699/06, Rn. 76–78", 110, 278, beim("himmel", "überdacht")),
    *okz("Schranke: Art. 8 Abs. 2 GG, auch auf Grund", 350, "hausr", "Bold", 34, x=160),
    z("des Hausrechts, §§ 903 Satz 1, 1004 BGB", 160, 398, beim("hausr", "Hausrechts"), "Bold", 34),
    zit("Rn. 79", 160, 448, beim("hausr", "Hausrechts")),
    blk(110, 520, 1040, 80, LILA, "allg", [("Meinungsfreiheit: Hausrecht ist allgemeines Gesetz", "ExtraBold", 33, INK)]),
    zit("Art. 5 Abs. 2 GG; Rn. 100", 110, 615, "allg"),
    *requisit([("schranke", ("tabler", "scale", 100, WEISS), "Rechtfertigung", WEISS),
               ("himmel", ("tabler", "building-airport", 120, BLAUHELL), "unter freiem Himmel", BLAUHELL),
               ("hausr", ("tabler", "key", 100, GELB), "Hausrecht", GELB),
               ("allg", ("tabler", "book", 100, LILA), "allgemeines Gesetz", LILA)]),
    *paar("SI", [("schranke", "ruhig"), ("hausr", "froh")], "DO", [("schranke", "ruhig"), ("himmel", "denkt")]),
])

# ===========================================================================================================================
# F2 Legitimer Zweck (Rn. 86, 87, 103)
# ===========================================================================================================================
folie([("zweck", f"{PR} › legitimer Zweck"), ("sicher", f"{PR} › Sicherheit, Funktionsfähigkeit (+)"),
       ("wohl", f"{PR} › keine Wohlfühlatmosphäre")], [
    *tafel("zweck", "Hausrecht nicht nach Belieben"),
    z("nur für legitime Zwecke des Gemeinwohls", 110, 180, beim("zweck", "legitime"), "Bold", 34),
    zit("BVerfG, 1 BvR 699/06, Rn. 86", 110, 230, beim("zweck", "legitime")),
    *okz("Sicherheit und Funktionsfähigkeit des Flughafens", 310, "sicher", "Bold", 34, x=160),
    zit("Rn. 87", 160, 360, "sicher"),
    *neinz("Wohlfühlatmosphäre ohne politische Diskussionen", 440, "wohl", "Bold", 34, x=160),
    zit("Rn. 103", 160, 490, "wohl"),
    *requisit([("zweck", ("tabler", "scale", 100, WEISS), "legitimer Zweck?", WEISS),
               ("sicher", ("tabler", "shield-check", 100, GRUEN), "Sicherheit", GRUEN),
               ("wohl", ("tabler", "sofa", 110, WEISS), "Wohlfühlen", HELLROT)]),
    *paar("SI", [("zweck", "ruhig"), ("sicher", "froh"), ("wohl", "denkt")], "DO", [("zweck", "denkt"), ("wohl", "froh")]),
])

# ===========================================================================================================================
# F3 Verhältnismäßigkeit (Rn. 88–95, 105–107)
# ===========================================================================================================================
folie([("s2b", f"{PR} › Störung des Betriebs?"), ("mehr", f"{PR} › mehr Beschränkungen als auf der Straße"),
       ("pauschal", f"{PR} › pauschales Verbot unverhältnismäßig"), ("erlaub", f"{PR} › keine allgemeine Erlaubnispflicht")], [
    *tafel("s2b", "Verhältnismäßigkeit im Terminal"),
    z("im Flughafen: mehr Beschränkungen als auf der Straße", 110, 180, "mehr", "Bold", 32),
    zit("BVerfG, 1 BvR 699/06, Leitsatz 2, Rn. 88, 91", 110, 225, "mehr"),
    *okz("Großdemonstrationen untersagen", 290, beim("gross", "Großdemonstrationen"), "Bold", 32, x=160),
    *okz("Trommeln oder Megafone verbieten", 345, beim("gross", "Trommeln"), "Bold", 32, x=160),
    *okz("Flugblätter hinter der Sicherheitskontrolle: Erlaubnis", 400, "luft", "Bold", 32, x=160),
    zit("Rn. 91, 92, 106", 160, 448, "luft"),
    blk(110, 500, 1040, 120, HELLROT, "pauschal", [("Pauschales Verbot: ohne konkrete Gefahr,", "ExtraBold", 33, INK),
                                                 ("unbefristet, ganzer Flughafen", "ExtraBold", 33, INK)]),
    *neinz("unverhältnismäßig", 640, beim("pauschal", "unverhältnismäßig"), "ExtraBold", 36, x=160),
    zit("Rn. 95, 107", 160, 690, beim("pauschal", "unverhältnismäßig")),
    *neinz("allgemeine Erlaubnispflicht für Versammlungen", 740, "erlaub", "Bold", 32, x=160),
    z("und Flugblätter (Rn. 89, 105)", 160, 785, beim("erlaub", "Flugblätter"), "Bold", 32),
    *requisit([("mehr", ("tabler", "building-airport", 120, WEISS), "mehr als auf der Straße", WEISS),
               (beim("gross", "Trommeln"), ("tabler", "speakerphone", 100, WEISS), "Trommeln, Megafone", WEISS),
               ("luft", ("tabler", "scan", 100, WEISS), "Sicherheitskontrolle", WEISS),
               ("pauschal", ("tabler", "ban", 90, HELLROT), "pauschal: nein", HELLROT)]),
    *spricht_neben("SI", X1, "s2b", "mehr", [], [("mehr", "ruhig"), ("pauschal", "sorge")],
                   ["Und wenn eine Demonstration", "den Betrieb im Terminal stört?"], size=31),
    ns("Herr Sievers", X1, FB, "s2b", BLAU, d=0.1),
    *stehend("DO", X2, [("s2b", "denkt"), ("pauschal", "froh")]),
])

# ===========================================================================================================================
# G Ergebnis und Bedeutung (Tenor, Rn. 44, 59; 1 BvR 3080/09 Rn. 32, 41)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Verfassungsbeschwerde begründet (+)"), ("privu", "Bedeutung · rein private Unternehmen"),
       ("stadion", "Bedeutung · Stadionverbot, 1 BvR 3080/09")], [
    *tafel("erg", "Ergebnis"),
    blk(110, 170, 1040, 80, GRUEN, "erg", [("Verfassungsbeschwerde erfolgreich (+)", "ExtraBold", 36, INK)]),
    z("verletzt: Art. 8 Abs. 1 GG und Art. 5 Abs. 1 Satz 1 GG", 110, 270, beim("erg", "verletzen"), "Bold", 32),
    z("Die Urteile werden aufgehoben.", 110, 350, "zurueck", "Bold", 34),
    zit("BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, Tenor, Rn. 44", 110, 398, "zurueck"),
    linienzug([(110, 460), (1150, 460)], "privu", breite=3),
    z("Rein private Unternehmen: in der Regel nur mittelbar", 110, 485, "privu", "Bold", 32),
    z("gebunden; die Grundrechte wirken über das Zivilrecht", 110, 530, beim("privu", "Grundrechte"), size=32),
    zit("BVerfG, 1 BvR 699/06, Rn. 59", 110, 575, beim("privu", "Grundrechte")),
    *okz("Stadionverbot: kein Ausschluss ohne sachlichen Grund", 635, "stadion", "Bold", 32, x=160),
    z("von einem Spiel, das einem großen Publikum offensteht", 160, 680, beim("stadion", "großen"), size=32),
    zit("BVerfG, Beschl. v. 11.4.2018 – 1 BvR 3080/09, Rn. 32, 41", 160, 725, beim("stadion", "großen")),
    *requisit([("erg", ("tabler", "circle-check", 100, GRUEN), "Erfolg (+)", GRUEN),
               ("privu", ("tabler", "building", 100, WEISS), "privates Unternehmen", WEISS),
               ("stadion", ("tabler", "ball-football", 100, WEISS), "Stadionverbot", WEISS)]),
    *paar("SI", [("erg", "ruhig")], "DO", [("erg", "froh")]),
])

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst die Grundrechtsbindung"), ("tipp2", "Klausurtipp · Art. 8 Abs. 2 GG im Terminal")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Unternehmen in Privatrechtsform:", 200, 200, beim("tipp", "Unternehmen"), "Bold", 36),
    z("zuerst die Grundrechtsbindung prüfen", 200, 250, beim("tipp", "zuerst"), "Bold", 36),
    z("Wem gehört mehr als die Hälfte der Anteile?", 200, 330, beim("tipp", "Wem"), size=34),
    linienzug([(130, 410), (1130, 410)], "tipp2", breite=3),
    z("Art. 8 Abs. 2 GG: Im Terminal gilt die", 200, 440, "tipp2", "Bold", 34),
    z("Versammlung als eine „unter freiem Himmel“.", 200, 488, beim("tipp2", "freiem"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Prüfschema
# ===========================================================================================================================
REIHEN = [("k0", 0, "Vorab: Grundrechtsbindung, Art. 1 Abs. 3 GG", True),
          (beim("k0", "gemischten"), 1, "gemischtwirtschaftliche Unternehmen: durch Beherrschung", False),
          ("k1", 0, "I. Schutzbereich, Art. 8 Abs. 1 GG", True),
          (beim("k1", "Versammlung"), 1, "Versammlung an einem Ort allgemeinen kommunikativen Verkehrs", False),
          ("k2", 0, "II. Eingriff", True),
          ("k3", 0, "III. Rechtfertigung", True),
          (beim("k3", "Schranke"), 1, "Schranke aus Art. 8 Abs. 2 GG; Hausrecht (§§ 903, 1004 BGB)", False),
          (beim("k3", "legitimer"), 1, "legitimer Zweck und Verhältnismäßigkeit", False),
          ("k4", 0, "Danach: Meinungsfreiheit, Art. 5 Abs. 1 Satz 1 GG, entsprechend", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Versammlung im Flughafen eines Staatsunternehmens"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 78, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k0", "Prüfschema › Vorab: Grundrechtsbindung"), ("k1", "Prüfschema › I. Schutzbereich"),
       ("k2", "Prüfschema › II. Eingriff"), ("k3", "Prüfschema › III. Rechtfertigung"),
       ("k4", "Prüfschema › Art. 5 Abs. 1 Satz 1 GG")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Staat bleibt an die Grundrechte", 0)], [("gebunden, ", 0), ("auch als", "a"),
                 (" Aktiengesellschaft.", 0)]], 750, 300, 42, "merke", {"a": beim("merke", "auch")}),
    *markertext([[("Wo er ein öffentliches Forum eröffnet,", 0)], [("darf er Versammlungen und Flugblätter", 0)],
                 [("nicht ", 0), ("pauschal", "b"), (" verbieten.", 0)]], 750, 520, 42, "m2",
                {"b": beim("m2", "pauschal")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
