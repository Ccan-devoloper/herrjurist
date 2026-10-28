"""Folge 156 · Gesetzliche Erbfolge §§ 1924 ff. BGB: Wer erbt ohne Testament? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Kurt stirbt mit 78 Jahren ohne Testament; Ehefrau Christa (Zugewinngemeinschaft), Tochter Verena (mit Tochter
Mathilda), Enkel Severin (Sohn des vorverstorbenen Andreas), Bruder Egbert.
Szenen laut ../SZENENPLAN.md: A Esszimmer (Fall), B Sachverhalt, C Stammbaum, D Wortlautkarte § 1922 Abs. 1, E Ordnungen
(Wortlautkarte § 1924 Abs. 1, Stufen §§ 1925, 1926), F Wortlautkarte § 1930 mit Stammbaum, G1 Wortlautkarte § 1924 Abs. 2,
G2 Wortlautkarte § 1924 Abs. 3 (Abs. 4), H1 Wortlautkarte § 1931 Abs. 1 S. 1, H2 § 1931 Abs. 3 und Wortlautkarte § 1371 Abs. 1,
I Ergebnis als Bruch-Diagramm, J Variante § 1931 Abs. 4 (Wortlautkarte), K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Takt: kein Sterbebild, kein Sarg, kein Grab, kein Kreuz-Symbol für den Tod; Kurt und Andreas nur als Namen im Stammbaum
(grauer Rahmen), der Tod nur als Text. Ein Handlungsgeräusch (Schritte, als Egbert hereinkommt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als
eigene Kopie aus Folge 152 (gemeinsame Dateien unverändert); neu: umbruch(), wortkarte(), linien(), knoten(), Baum, kreis(),
kommode(), zimmer(), stamm(). Zahlen und Brüche auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_156/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_156/" in n:
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




# --- eigene Bausteine Folge 156 ----------------------------------------------------------------------------------------------
HELLGRAU = (226, 226, 222, 255)
GRAU = (150, 150, 150, 255)
BODEN_Y = 905                                # Fußboden im Esszimmer = Unterkante der Figuren
FHA = 470                                    # Figurenhöhe in der Fallszene
KIND = 0.58                                  # Mathilda (um 6): Anteil der Erwachsenenhöhe
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch nach Breite (Wortlautkarten)."""
    f = F(stil, size); zeilen, cur = [], ""
    worte = []
    for w in text.split():                       # „§“ nie allein am Zeilenende
        if worte and worte[-1] in ("§", "§§", "Abs."):
            worte[-1] += " " + w
        else:
            worte.append(w)
    for w in worte:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def wortkarte(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte mit automatischem Umbruch; marken = [(wort, cue)] sucht das Wort in den Zeilen (erste Fundstelle)."""
    zeilen = umbruch(text, size, w - 60)
    mk = []
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} über Zeilenumbruch: {zeilen}"
        mk.append((zi, wort, mc))
    return wortlaut(x, y, w, zeilen, quelle, cue, marken=mk, size=size, bis=bis)


def linien(segmente, cue, breite=4, farbe=INK, bis=None, name="baumlinie"):
    """Mehrere gerade Linien in einem Element (Verbindungen im Stammbaum)."""
    s = 3
    xs = [p for sg in segmente for p in (sg[0], sg[2])]; ys = [p for sg in segmente for p in (sg[1], sg[3])]
    x0, y0 = min(xs) - breite, min(ys) - breite
    im = Image.new("RGBA", (int((max(xs) - x0 + breite) * s) + 2, int((max(ys) - y0 + breite) * s) + 2))
    dr = ImageDraw.Draw(im)
    for a, b, c, d_ in segmente:
        dr.line(((a - x0) * s, (b - y0) * s, (c - x0) * s, (d_ - y0) * s), fill=farbe, width=breite * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0, y0, cue, "fade", 0.0, bis, name=name)


# Stammbaum: (Name, Unterzeile, Füllung oder None = verstorben/grauer Rahmen, Spalte, Reihe)
PERS = {"Eltern": ("Eltern", "verstorben", None, 305, 0), "Egbert": ("Egbert", "Bruder", ORANGE, 140, 1),
        "Kurt": ("Kurt", "Erblasser", None, 470, 1), "Christa": ("Christa", "Ehefrau", LILA, 800, 1),
        "Verena": ("Verena", "Tochter", BLAU, 470, 2), "Andreas": ("Andreas", "vorverstorben", None, 800, 2),
        "Mathilda": ("Mathilda", "Enkelin", PINK, 470, 3), "Severin": ("Severin", "Enkel", GRUEN, 800, 3)}


def knoten(name, cx, y, w, h, cue, size=30, bis=None):
    t, sub, fill, _, _ = PERS[name]
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    tot = fill is None
    dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), 14 * s, fill=HELLGRAU if tot else fill,
                         outline=GRAU if tot else INK, width=(5 if tot else 4) * s)
    im = im.resize((w, h), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    f1, f2 = F("ExtraBold", size), F("Regular", 26)
    assert f1.getlength(glyphen(t)) <= w - 20 and f2.getlength(glyphen(sub)) <= w - 20, name
    dr.text((w / 2, h * 0.34), t, font=f1, fill=TEXT if tot else INK, anchor="mm")
    dr.text((w / 2, h * 0.73), sub, font=f2, fill=TEXT if tot else INK, anchor="mm")
    return El(im, cx - w / 2, y, cue, "pop", 0.0, bis, name="knoten:" + name)


class Baum:
    """Stammbaum der Familie (programmatisch). teil='voll' (mit Eltern und Egbert) oder 'erste' (nur Kurt, Christa und
    die erste Ordnung). cues: Name -> Cue des Erscheinens (Standard: alle mit cue0)."""

    def __init__(self, ox, oy, cue0, cues=None, w=230, h=78, dy=110, size=30, teil="voll"):
        self.ox, self.oy, self.w, self.h, self.dy, self.size = ox, oy, w, h, dy, size
        self.r0 = 0 if teil == "voll" else 1
        self.namen = [n for n in PERS if teil == "voll" or PERS[n][4] >= 1 and n != "Egbert"]
        self.c = {n: (cues or {}).get(n, cue0) for n in self.namen}

    def box(self, n):
        _, _, _, sp, r = PERS[n]
        cx, y = self.ox + sp, self.oy + (r - self.r0) * self.dy
        return cx - self.w / 2, y, cx + self.w / 2, y + self.h

    def mitte(self, n):
        x0, y0, x1, y1 = self.box(n)
        return (x0 + x1) / 2, (y0 + y1) / 2

    def els(self):
        b = self.box; c = self.c; h, w = self.h, self.w
        out = []
        if "Eltern" in self.namen:                     # Eltern -> Egbert und Kurt
            ex = (b("Eltern")[0] + b("Eltern")[2]) / 2; yb = b("Eltern")[3] + (self.dy - h) / 2
            out.append(linien([(ex, b("Eltern")[3], ex, yb), (self.ox + 140, yb, self.ox + 470, yb),
                               (self.ox + 140, yb, self.ox + 140, b("Egbert")[1]), (self.ox + 470, yb, self.ox + 470, b("Kurt")[1])],
                              c["Egbert"]))
        ym = b("Kurt")[1] + h / 2                       # Ehe: Doppellinie Kurt = Christa
        out.append(linien([(b("Kurt")[2], ym - 6, b("Christa")[0], ym - 6), (b("Kurt")[2], ym + 6, b("Christa")[0], ym + 6)],
                          c["Christa"]))
        mx = (b("Kurt")[2] + b("Christa")[0]) / 2; yb2 = b("Kurt")[3] + (self.dy - h) / 2
        out.append(linien([(mx, ym + 6, mx, yb2), (self.ox + 470, yb2, self.ox + 800, yb2),
                           (self.ox + 470, yb2, self.ox + 470, b("Verena")[1]), (self.ox + 800, yb2, self.ox + 800, b("Andreas")[1])],
                          c["Verena"]))
        out.append(linien([(self.ox + 470, b("Verena")[3], self.ox + 470, b("Mathilda")[1])], c["Mathilda"]))
        out.append(linien([(self.ox + 800, b("Andreas")[3], self.ox + 800, b("Severin")[1])], c["Severin"]))
        for n in self.namen:
            x0, y0, x1, y1 = b(n)
            out.append(knoten(n, (x0 + x1) / 2, y0, w, h, c[n], size=self.size))
        return out

    def raus(self, n, cue, kreuz=True):
        """Person erbt nicht: Knoten blass, Bleistift-Kreuz rechts oben."""
        x0, y0, x1, y1 = self.box(n)
        im = Image.new("RGBA", (int(x1 - x0), int(y1 - y0)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 14, fill=(255, 255, 255, 150))
        els = [El(im, x0, y0, cue, "fade", 0.0, None, name="blass:" + n)]
        if kreuz:
            els.append(nein(x1 - 6, y0 + 8, cue, gr=22))
        return els

    def rein(self, n, cue):
        """Person erbt: dunkelgrüner Rahmen und Haken."""
        x0, y0, x1, y1 = self.box(n)
        im = Image.new("RGBA", (int(x1 - x0) + 16, int(y1 - y0) + 16))
        ImageDraw.Draw(im).rounded_rectangle((2, 2, im.width - 3, im.height - 3), 18, outline=DGRUEN, width=6)
        return [El(im, x0 - 8, y0 - 8, cue, "pop", 0.0, None, name="erbt:" + n), ok(x1 - 4, y0 + 6, cue, gr=22)]

    def bruch(self, n, text, cue, fill=WEISS, seite="r"):
        """Erbquote als Ziffern-Pille neben dem Knoten."""
        x0, y0, x1, y1 = self.box(n)
        if seite == "r":
            return pl(text, x1 + 18, y0 + 10, cue, fill=fill, size=34)
        return pl(text, x0 - 18 - F("Bold", 34).getlength(text) - 60, y0 + 10, cue, fill=fill, size=34)


def kreis(cx, cy, r, teile, cue_liste, labels, bis=None):
    """Bruch-Diagramm (Kreis): teile = [(start_grad, ende_grad, farbe)], je Teil ein Element mit Ziffern-Label."""
    s = 2
    els = []
    for (a0, a1, fu), c, lab in zip(teile, cue_liste, labels):
        im = Image.new("RGBA", ((2 * r + 12) * s, (2 * r + 12) * s))
        dr = ImageDraw.Draw(im)
        dr.pieslice((6 * s, 6 * s, (2 * r + 6) * s, (2 * r + 6) * s), a0, a1, fill=fu, outline=INK, width=5 * s)
        im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
        if lab:
            import math as _m
            am = _m.radians((a0 + a1) / 2)
            lx, ly = r + 6 + _m.cos(am) * r * 0.55, r + 6 + _m.sin(am) * r * 0.55
            ImageDraw.Draw(im).text((lx, ly), glyphen(lab), font=F("ExtraBold", 44 if r > 150 else 34), fill=INK, anchor="mm")
        els.append(El(im, cx - r - 6, cy - r - 6, c, "pop" if lab else "fade", 0.0, bis, name=f"kreis:{a0}-{a1}"))
    return els


def kommode(c):
    """Kommode mit gerahmtem Familienfoto (Rahmen, darin nur das Familien-Symbol, keine Person) und Blumen."""
    s = 2
    w, h = 250, 160
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for yy in (55, 105):
        dr.line((14 * s, yy * s, (w - 14) * s, yy * s), fill=INK, width=3 * s)
        dr.ellipse(((w / 2 - 7) * s, (yy - 30) * s, (w / 2 + 7) * s, (yy - 16) * s), fill=INK)
    im = im.resize((w, h), Image.LANCZOS)
    els = [hart(El(im, 60, BODEN_Y - h, c, "cut", 0.0, None, name="kommode"))]
    # Bilderrahmen auf der Kommode
    fw, fh = 150, 120
    fr = Image.new("RGBA", (fw * s, fh * s))
    d2 = ImageDraw.Draw(fr)
    d2.rounded_rectangle((3 * s, 3 * s, (fw - 3) * s, (fh - 3) * s), 6 * s, fill=(170, 120, 80, 255), outline=INK, width=4 * s)
    d2.rectangle((18 * s, 18 * s, (fw - 18) * s, (fh - 18) * s), fill=(232, 240, 250, 255), outline=INK, width=3 * s)
    fr = fr.resize((fw, fh), Image.LANCZOS)
    els.append(hart(El(fr, 85, BODEN_Y - h - fh, c, "cut", 0.0, None, name="bilderrahmen")))
    els.append(hart(ficon("tabler", "users-group", 160, BODEN_Y - h - 26, 78, c, fuell=WEISS, anim="cut")))
    els.append(hart(ficon("tabler", "flower", 270, BODEN_Y - h, 64, c, fuell=ROT, anim="cut")))
    return els


def zimmer(c):
    """Esszimmer: Fußboden und Fußleiste (Grundform), harter Schnitt ab 0,0 s."""
    im = Image.new("RGBA", (1880, 70))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1880, 70), fill=(236, 220, 198, 255))
    dr.line((0, 2, 1880, 2), fill=INK, width=5)
    return hart(El(im, 20, BODEN_Y, c, "cut", 0.0, None, name="boden"))


NAME = {"CH": "Christa", "VE": "Verena", "MA": "Mathilda", "SE": "Severin", "EG": "Egbert"}
NFARBE = {"CH": LILA, "VE": BLAU, "MA": PINK, "SE": GRUEN, "EG": ORANGE}
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def hoehe(k, h):
    return int(h * KIND) if k == "MA" else h


def stehend(k, x, folge, unten=FB, h=FR):
    return [*fig(k, x, unten, hoehe(k, h), folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


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
    return [*stehend(k1, X1, folge1), *stehend(k2, X2, folge2)]


def allein(k, folge):
    return stehend(k, FX, folge)


# ===========================================================================================================================
# A Fall: die Familie im Esszimmer (der Todesfall nur als Text; Kurt und Andreas erscheinen nicht als Figuren)
# ===========================================================================================================================
CX, VX, MX, SX, EX = 460, 705, 945, 1270, 1620
E_LOS, E_DA = beim("egb", "Auch"), beim("egb", "da", ende=True)
folie([(NULL, "Fall · Ohne Testament"), ("fam", "Fall · Die Familie"), ("rs", "Fall · Wer bekommt etwas?"),
       ("frage", "Fall · Die Frage")], [
    zimmer(NULL),
    *kommode(NULL),
    hart(pl("Kurt ist mit 78 Jahren gestorben.", 70, 30, NULL, fill=HELLGRAU, size=38)),
    pl("Kein Testament", 70, 110, "test", fill=WEISS, size=34, bis="frage"),
    ficon("tabler", "file-off", 400, 168, 60, "test", fuell=WEISS, bis="frage"),
    pl("Andreas, Vater von Severin: vor 3 Jahren gestorben", 70, 190, "andr", fill=HELLGRAU, size=32, bis="frage"),
    # die Familie (links blicken nach rechts, rechts nach links)
    *[hart(e) for e in fig("CH", CX, BODEN_Y, FHA, [(NULL, "still_r"), ("frage", "muede_r")])],
    hart(ns("Christa", CX, BODEN_Y, NULL, LILA)),
    *[hart(e) for e in fig("VE", VX, BODEN_Y, FHA, [(NULL, "still_r"), ("rs", "sorge_r"), ("frage", "ernst_r")])],
    hart(ns("Verena", VX, BODEN_Y, NULL, BLAU)),
    *[hart(e) for e in fig("MA", MX, BODEN_Y, int(FHA * KIND), [(NULL, "ruhig_r")])],
    hart(ns("Mathilda", MX, BODEN_Y, NULL, PINK)),
    *[hart(e) for e in fig("SE", SX, BODEN_Y, FHA, [(NULL, "still"), ("andr", "sorge")], bis="rs")],
    hart(ns("Severin", SX, BODEN_Y, NULL, GRUEN)),
    # Rollen über den Köpfen, wenn die Erzählerin sie nennt (bis die Figurenrede beginnt)
    pl("Ehefrau", CX, BODEN_Y - FHA - 62, "chr", fill=LILA, size=28, anker="m", bis="rs"),
    pl("Tochter", VX, BODEN_Y - FHA - 62, "ver", fill=BLAU, size=28, anker="m", bis="rs"),
    pl("Tochter von Verena", MX + 40, BODEN_Y - int(FHA * KIND) - 62, beim("ver", "Mathilda"), fill=PINK, size=28, anker="m",
       bis="rs"),
    pl("Enkel", SX, BODEN_Y - FHA - 62, "sev", fill=GRUEN, size=28, anker="m", bis="rs"),
    # Egbert kommt von rechts herein (Schritte)
    szene(bewegt(peep_voll("EG_ruhig", EX, BODEN_Y, FHA, "egb", anim="pop", bis="re"), E_LOS, E_DA, 120, 0),
          "156schritte*", 1.0, 0.0),
    bewegt(ns("Egbert", EX, BODEN_Y, "egb", ORANGE, d=0.1), E_LOS, E_DA, 120, 0),
    pl("Egbert, Bruder von Kurt", 70, 270, beim("egb", "Bruder"), fill=ORANGE, size=32, bis="frage"),
    # Figurenrede
    *redet("SE_redet", SX, BODEN_Y, FHA, "rs", "re"),
    blase("sprech", 600, 270, "rs", 1230, 245, inhalt=["Mein Vater lebt nicht mehr.", "Bekomme ich dann",
                                                    "überhaupt etwas?"], textsize=36, figur=("SE_redet", SX, BODEN_Y, FHA), bis="re"),
    *fig("SE", SX, BODEN_Y, FHA, [("re", "sorge"), ("frage", "still")], erst="cut"),
    *redet("EG_redet", EX, BODEN_Y, FHA, "re", "frage"),
    blase("sprech", 520, 220, "re", 1560, 250, inhalt=["Und ich? Ich bin", "immerhin sein Bruder."], textsize=36,
          figur=("EG_redet", EX, BODEN_Y, FHA), bis="frage"),
    *fig("EG", EX, BODEN_Y, FHA, [("frage", "skeptisch")], erst="cut"),
    pl("Wer erbt ohne Testament?", 70, 110, "frage", fill=PINK, size=36),
    pl("Wie viel bekommt jeder?", 70, 190, "frage2", fill=PINK, size=36),
    ficon("tabler", "chart-pie", 560, 250, 64, "frage2", fuell=GELB),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================


def sachverhalt_156(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_156("sv", [
    "Kurt ist im Alter von 78 Jahren gestorben. Ein Testament oder einen Erbvertrag hat er nicht hinterlassen. Er war mit "
    "Christa verheiratet; die beiden lebten im gesetzlichen Güterstand der Zugewinngemeinschaft.",
    "Ihre gemeinsamen Kinder sind Verena und Andreas. Andreas ist drei Jahre vor Kurt gestorben; sein einziges Kind ist "
    "Severin. Verena hat eine Tochter, Mathilda.",
    "Die Eltern von Kurt sind schon lange verstorben. Sein Bruder Egbert lebt.",
], "Wer wird gesetzlicher Erbe von Kurt, und zu welchen Teilen?")

# ===========================================================================================================================
# C Der Stammbaum baut sich mit dem Sprechtext auf
# ===========================================================================================================================
B0 = Baum(150, 210, "bk", cues={"Kurt": "bk", "Christa": "bc", "Verena": "bkin", "Andreas": "band",
                                 "Mathilda": "benk", "Severin": beim("benk", "Severin"), "Egbert": "beg",
                                 "Eltern": beim("beg", "Eltern")}, w=250, h=86, dy=165, size=32)
folie([("baum", "Stammbaum"), ("bk", "Stammbaum › Erblasser: Kurt"), ("bc", "Stammbaum › Ehefrau: Christa"),
       ("bkin", "Stammbaum › Kinder: Verena und Andreas"), ("benk", "Stammbaum › Enkel: Mathilda und Severin"),
       ("beg", "Stammbaum › Bruder: Egbert")], rechts_frei([
    *tafel("baum", "Der Stammbaum"),
    *B0.els(),
    pl("Zugewinngemeinschaft", 832, 205, beim("bc", "Zugewinngemeinschaft"), fill=WEISS, size=28),
    *requisit([("baum", ("tabler", "sitemap", 100, WEISS), "Stammbaum", WEISS),
               ("bc", ("tabler", "heart", 90, LILA), "verheiratet", LILA),
               ("bkin", ("tabler", "users", 100, WEISS), "Kinder", BLAU),
               ("benk", ("tabler", "users-group", 110, WEISS), "Enkel", GRUEN),
               ("beg", ("tabler", "user", 90, ORANGE), "Bruder", ORANGE)]),
    *zwei("CH", [("baum", "still"), ("bc", "ruhig")], "SE", [("baum", "ruhig"), ("band", "still")]),
]))
assert B0.box("Severin")[3] <= 890

# ===========================================================================================================================
# D § 1922 Abs. 1 BGB: Gesamtrechtsnachfolge
# ===========================================================================================================================
w22, w22_y = wortkarte(80, 165, 1100, "„Mit dem Tode einer Person (Erbfall) geht deren Vermögen (Erbschaft) als Ganzes auf "
                       "eine oder mehrere andere Personen (Erben) über.“", "§ 1922 Abs. 1 BGB", "p1922", marken=[
    ("Tode einer Person", beim("p1922", "Tode")), ("Vermögen", beim("p1922", "Vermögen")),
    ("als Ganzes", beim("p1922", "Ganzes")), ("mehrere", beim("p1922", "mehrere"))], size=32)
folie([("p1922", "Erbfall › § 1922 Abs. 1 BGB"), ("univ", "Erbfall › Universalsukzession"),
       ("ges", "Erbfall › kein Testament: gesetzliche Erbfolge")], rechts_frei([
    *tafel("p1922", "Was geht über? § 1922 BGB"),
    *w22,
    blk(110, w22_y + 30, 1040, 80, GELB, "univ", [("Gesamtrechtsnachfolge (Universalsukzession)", "ExtraBold", 36, INK)]),
    *okz("Kein Testament: gesetzliche Erbfolge", w22_y + 150, "ges", "Bold", 34, x=160),
    zit("Mit Testament: Video „Berliner Testament“", 160, w22_y + 204, "v040"),
    *requisit([("p1922", ("tabler", "book", 100, WEISS), "§ 1922 Abs. 1 BGB", GELB),
               ("univ", ("tabler", "box", 100, GELB), "Vermögen als Ganzes", GELB),
               ("ges", ("tabler", "file-off", 100, WEISS), "kein Testament", WEISS),
               ("v040", ("tabler", "file-text", 100, WEISS), "Video: Berliner Testament", WEISS)]),
    *zwei("VE", [("p1922", "ruhig"), ("ges", "ernst")], "CH", [("p1922", "ruhig"), ("univ", "still")]),
]))

# ===========================================================================================================================
# E Ordnungen: § 1924 Abs. 1 (Wortlaut), §§ 1925, 1926 als Stufen
# ===========================================================================================================================
PO = "Ordnungen"
w24, w24_y = wortkarte(80, 165, 1100, "„Gesetzliche Erben der ersten Ordnung sind die Abkömmlinge des Erblassers.“",
                       "§ 1924 Abs. 1 BGB", "p1924", marken=[("ersten Ordnung", beim("p1924", "ersten")),
                                                             ("Abkömmlinge", beim("p1924", "Abkömmlinge"))], size=32)
SY = w24_y + 40
folie([("ord", PO), ("p1924", f"{PO} › 1. Ordnung, § 1924 Abs. 1 BGB"), ("o2", f"{PO} › 2. Ordnung, § 1925 BGB"),
       ("o3", f"{PO} › 3. Ordnung, § 1926 BGB")], rechts_frei([
    *tafel("ord", "Die Ordnungen"),
    *w24,
    blk(110, SY, 560, 100, GELB, beim("p1924", "Abkömmlinge"), [("1. Ordnung: Abkömmlinge", "ExtraBold", 32, INK),
                                                               ("§ 1924 BGB", "Regular", 26, INK)]),
    pl("Kinder, Enkel, Urenkel", 700, SY + 22, "abk", fill=WEISS, size=30),
    blk(230, SY + 125, 900, 100, BLAU, "o2", [("2. Ordnung: Eltern und deren Abkömmlinge", "ExtraBold", 32, INK),
                                              ("§ 1925 BGB", "Regular", 26, INK)]),
    pl("Egbert", 950, SY + 178, beim("o2", "Egbert"), fill=ORANGE, size=30),
    blk(350, SY + 250, 800, 100, LILA, "o3", [("3. Ordnung: Großeltern und deren Abkömmlinge", "ExtraBold", 32, INK),
                                              ("§ 1926 BGB", "Regular", 26, INK)]),
    *requisit([("ord", ("tabler", "stairs", 100, WEISS), "Ordnungen", WEISS),
               ("p1924", ("tabler", "users-group", 110, GELB), "1. Ordnung", GELB),
               ("o2", ("tabler", "users", 100, BLAU), "2. Ordnung", BLAU),
               ("o3", ("tabler", "users", 100, LILA), "3. Ordnung", LILA)]),
    *zwei("SE", [("ord", "ruhig")], "EG", [("ord", "ruhig"), (beim("o2", "Egbert"), "skeptisch")]),
]))
assert SY + 350 <= 890, SY

# ===========================================================================================================================
# F § 1930 BGB: Ausschluss entfernterer Ordnungen
# ===========================================================================================================================
w30, w30_y = wortkarte(80, 165, 1100, "„Ein Verwandter ist nicht zur Erbfolge berufen, solange ein Verwandter einer "
                       "vorhergehenden Ordnung vorhanden ist.“", "§ 1930 BGB", "p1930", marken=[
    ("nicht zur Erbfolge berufen", beim("p1930", "nicht")), ("vorhergehenden Ordnung", beim("p1930", "vorhergehenden"))],
                       size=32)
B1 = Baum(150, w30_y + 30, "p1930", w=230, h=78, dy=104)
folie([("p1930", f"{PO} › Ausschluss, § 1930 BGB"), ("egb2", f"{PO} › Kurt hat Abkömmlinge"),
       ("egb3", f"{PO} › Egbert erbt nicht (−)")], rechts_frei([
    *tafel("p1930", "Die Rangfolge: § 1930 BGB"),
    *w30,
    *B1.els(),
    pl("1. Ordnung", 130, B1.box("Mathilda")[1] + 15, "egb2", fill=GELB, size=28),
    *[e for n in ("Verena", "Severin") for e in B1.rein(n, "egb2")],
    *B1.raus("Egbert", beim("egb3", "nichts")),
    pl("2. Ordnung", 130, B1.box("Verena")[1] + 15, beim("egb3", "nichts"), fill=BLAU, size=28),
    *requisit([("p1930", ("tabler", "stairs", 100, WEISS), "vorhergehende Ordnung", WEISS),
               (beim("egb3", "nichts"), ("tabler", "user-x", 100, ORANGE), "Egbert erbt nichts", ORANGE)]),
    *allein("EG", [("p1930", "ruhig"), ("egb2", "skeptisch"), (beim("egb3", "nichts"), "muede")]),
]))
assert B1.box("Severin")[3] <= 890, B1.box("Severin")

# ===========================================================================================================================
# G1 § 1924 Abs. 2 BGB: Repräsentationsprinzip
# ===========================================================================================================================
PE = "Erste Ordnung"
w2, w2_y = wortkarte(80, 165, 1100, "„Ein zur Zeit des Erbfalls lebender Abkömmling schließt die durch ihn mit dem "
                     "Erblasser verwandten Abkömmlinge von der Erbfolge aus.“", "§ 1924 Abs. 2 BGB", "p2", marken=[
    ("lebender Abkömmling", beim("p2", "lebender")), ("schließt", beim("p2", "schließt")),
    ("durch ihn", beim("p2", "durch")), ("von der Erbfolge aus", beim("p2", "Erbfolge"))], size=32)
B2 = Baum(150, w2_y + 40, "inn", w=230, h=78, dy=112, teil="erste")
folie([("inn", f"{PE} › Wer erbt?"), ("p2", f"{PE} › Repräsentation, § 1924 Abs. 2 BGB"),
       ("repr2", f"{PE} › Mathilda erbt nicht (−)")], rechts_frei([
    *tafel("inn", "Repräsentation: § 1924 Abs. 2"),
    *w2,
    *B2.els(),
    pl("Repräsentationsprinzip", 560, B2.box("Severin")[3] + 18, "repr", fill=GELB, size=30),
    *B2.rein("Verena", "repr2"),
    pl("lebt", B2.box("Verena")[0] - 110, B2.box("Verena")[1] + 18, "repr2", fill=GRUEN, size=28),
    *B2.raus("Mathilda", beim("repr2", "erbt")),
    *requisit([("inn", ("tabler", "users-group", 110, GELB), "1. Ordnung", GELB),
               ("p2", ("tabler", "user-check", 100, BLAU), "Verena lebt", BLAU),
               (beim("repr2", "erbt"), ("tabler", "user-x", 100, PINK), "Mathilda erbt nicht", PINK)]),
    *zwei("VE", [("inn", "ruhig"), ("repr2", "ernst")], "MA", [("inn", "ruhig"), ("repr", "suess")]),
]))
assert B2.box("Severin")[3] <= 890

# ===========================================================================================================================
# G2 § 1924 Abs. 3, 4 BGB: Eintrittsrecht, Erbfolge nach Stämmen
# ===========================================================================================================================
w3, w3_y = wortkarte(80, 165, 1100, "„An die Stelle eines zur Zeit des Erbfalls nicht mehr lebenden Abkömmlings treten die "
                     "durch ihn mit dem Erblasser verwandten Abkömmlinge (Erbfolge nach Stämmen).“", "§ 1924 Abs. 3 BGB", "p3",
                     marken=[("An die Stelle", beim("p3", "Stelle")), ("nicht mehr lebenden", beim("p3", "nicht")),
                             ("treten", beim("p3", "treten")), ("nach Stämmen", beim("staemme", "Erbfolge"))],
                     size=30)
B3 = Baum(150, w3_y + 70, "p3", w=230, h=78, dy=110, teil="erste")
SX0, SY0, SX1, SY1 = B3.box("Andreas")[0] - 18, B3.box("Andreas")[1] - 14, B3.box("Severin")[2] + 18, B3.box("Severin")[3] + 14
VX0, VY0, VX1, VY1 = B3.box("Verena")[0] - 18, B3.box("Verena")[1] - 14, B3.box("Mathilda")[2] + 18, B3.box("Mathilda")[3] + 14


def stamm(x0, y0, x1, y1, cue, fill):
    im = Image.new("RGBA", (int(x1 - x0), int(y1 - y0)))
    ImageDraw.Draw(im).rounded_rectangle((2, 2, im.width - 3, im.height - 3), 20, fill=fill[:3] + (70,), outline=fill[:3] + (255,),
                                         width=5)
    return El(im, x0, y0, cue, "fade", 0.0, None, name="stamm")


folie([("p3", f"{PE} › Eintrittsrecht, § 1924 Abs. 3 BGB"), ("eintr", f"{PE} › Severin statt Andreas (+)"),
       ("p4", f"{PE} › gleiche Teile, § 1924 Abs. 4 BGB"), ("staemme", f"{PE} › Erbfolge nach Stämmen")], rechts_frei([
    *tafel("p3", "Eintritt: § 1924 Abs. 3, 4"),
    *w3,
    z("§ 1924 Abs. 4 BGB: „Kinder erben zu gleichen Teilen.“", 110, w3_y + 14, "p4", "Bold", 30),
    stamm(VX0, VY0, VX1, VY1, "staemme", BLAU),
    stamm(SX0, SY0, SX1, SY1, "staemme", GRUEN),
    *B3.els(),
    *B3.raus("Mathilda", "p3", kreuz=False),
    pfeil(B3.box("Severin")[2] + 40, B3.box("Severin")[1] + 40, B3.box("Andreas")[2] + 40, B3.box("Andreas")[1] + 40,
          "eintr", breite=6, kopf=22, farbe=DGRUEN),
    pl("Stamm Verena", VX0, VY1 + 8, beim("staemme", "Verena"), fill=BLAU, size=28),
    pl("Stamm Andreas", SX0, SY1 + 8, beim("staemme", "Andreas"), fill=GRUEN, size=28),
    blk(110, VY0 - 70, 300, 60, GELB, "gleich", [("gleich viel", "ExtraBold", 32, INK)]),
    *requisit([("p3", ("tabler", "replace", 100, WEISS), "Andreas vorverstorben", HELLGRAU),
               ("eintr", ("tabler", "arrow-big-up", 90, GRUEN), "Eintrittsrecht", GRUEN),
               ("p4", ("tabler", "scale", 100, WEISS), "zu gleichen Teilen", WEISS),
               ("staemme", ("tabler", "hierarchy", 100, WEISS), "nach Stämmen", WEISS)]),
    *zwei("VE", [("p3", "ruhig"), ("gleich", "ernst")], "SE", [("p3", "sorge"), ("eintr", "ruhig")]),
]))
assert SY1 <= 890 and VY0 - 70 > w3_y + 60, (SY1, VY0, w3_y)

# ===========================================================================================================================
# H1 § 1931 Abs. 1 S. 1 BGB: Ehegatte neben der ersten Ordnung
# ===========================================================================================================================
PG = "Ehegatte"
w31, w31_y = wortkarte(80, 165, 1100, "„Der überlebende Ehegatte des Erblassers ist neben Verwandten der ersten Ordnung zu "
                       "einem Viertel, neben Verwandten der zweiten Ordnung oder neben Großeltern zur Hälfte der Erbschaft als "
                       "gesetzlicher Erbe berufen.“", "§ 1931 Abs. 1 S. 1 BGB", "p1931", marken=[
    ("überlebende Ehegatte", beim("p1931", "überlebende")), ("ersten Ordnung", beim("p1931", "ersten")),
    ("einem Viertel", beim("p1931", "Viertel"))], size=32)
folie([("ehe", PG), ("p1931", f"{PG} › § 1931 Abs. 1 S. 1 BGB"), ("viertel", f"{PG} › neben 1. Ordnung: 1/4")],
      rechts_frei([
    *tafel("ehe", "Und Christa? § 1931 BGB"),
    *w31,
    blk(110, w31_y + 40, 760, 80, LILA, "viertel", [("Christa: zunächst 1/4", "ExtraBold", 38, INK)]),
    z("neben Verena und Severin (1. Ordnung)", 110, w31_y + 140, "viertel", size=32),
    *kreis(1010, w31_y + 140, 115, [(-90, 0, LILA), (0, 270, WEISS)], [beim("viertel", "Viertel"), beim("viertel", "Viertel")],
           ["1/4", ""]),
    *requisit([("ehe", ("tabler", "heart", 90, LILA), "Ehefrau", LILA),
               ("viertel", ("tabler", "chart-pie", 100, LILA), "1/4", LILA)]),
    *allein("CH", [("ehe", "ruhig"), ("p1931", "ernst"), ("viertel", "ruhig")]),
]))
assert w31_y + 260 <= 890

# ===========================================================================================================================
# H2 § 1931 Abs. 3 i. V. m. § 1371 Abs. 1 BGB: pauschale Erhöhung um ein Viertel
# ===========================================================================================================================
w71, w71_y = wortkarte(80, 240, 1100, "„Wird der Güterstand durch den Tod eines Ehegatten beendet, so wird der Ausgleich des "
                       "Zugewinns dadurch verwirklicht, dass sich der gesetzliche Erbteil des überlebenden Ehegatten um ein "
                       "Viertel der Erbschaft erhöht; hierbei ist unerheblich, ob die Ehegatten im einzelnen Falle einen "
                       "Zugewinn erzielt haben.“", "§ 1371 Abs. 1 BGB", "p1371", marken=[
    ("durch den Tod", beim("p1371", "Tod")), ("Erbteil des überlebenden", beim("p1371", "Erbteil")),
    ("um ein Viertel der Erbschaft erhöht", beim("p1371", "Viertel")),
    ("unerheblich", "pausch")], size=30)
folie([("abs3", f"{PG} › § 1931 Abs. 3 BGB"), ("p1371", f"{PG} › § 1371 Abs. 1 BGB: plus 1/4"),
       ("halb", f"{PG} › Christa: 1/2")], rechts_frei([
    *tafel("abs3", "Zugewinngemeinschaft: § 1371"),
    z("§ 1931 Abs. 3 BGB: „Die Vorschrift des § 1371 bleibt unberührt.“", 110, 175, beim("abs3", "lässt"), "Bold", 30),
    *w71,
    blk(110, w71_y + 36, 700, 80, LILA, beim("halb", "Christa"), [("1/4 + 1/4 = 1/2", "ExtraBold", 40, INK)]),
    *kreis(1000, w71_y + 80, 95, [(-90, 0, LILA), (0, 90, LILA), (90, 270, WEISS)], ["halb", beim("halb", "plus"), "halb"],
           ["1/4", "1/4", ""]),
    *requisit([("abs3", ("tabler", "book", 100, WEISS), "§ 1371 BGB", WEISS),
               ("p1371", ("tabler", "plus", 90, LILA), "plus 1/4", LILA),
               (beim("halb", "Christa"), ("tabler", "chart-pie-2", 100, LILA), "Christa: 1/2", LILA)]),
    *zwei("CH", [("abs3", "ruhig"), ("pausch", "ernst"), (beim("halb", "Christa"), "ruhig")],
          "VE", [("abs3", "ruhig"), ("p1371", "still")]),
]))
assert w71_y + 180 <= 890, w71_y

# ===========================================================================================================================
# I Ergebnis als Bruch-Diagramm mit Gegenprobe
# ===========================================================================================================================
KX_, KY_, KR = 370, 520, 230
folie([("erg", "Ergebnis"), ("e_rest", "Ergebnis › Rest nach Stämmen"), ("probe", "Ergebnis › Gegenprobe: Summe 1"),
       ("e_nicht", "Ergebnis › Mathilda, Egbert: nichts")], rechts_frei([
    *tafel("erg", "Das Ergebnis"),
    *kreis(KX_, KY_, KR, [(90, 270, LILA)], ["e_chr"], ["1/2"]),
    *kreis(KX_, KY_, KR, [(-90, 90, HELLGRAU)], ["e_rest"], [""]),
    *kreis(KX_, KY_, KR, [(-90, 0, BLAU), (0, 90, GRUEN)], ["e_ver", "e_sev"], ["1/4", "1/4"]),
    pl("Christa: 1/2", 680, 260, "e_chr", fill=LILA, size=38),
    z("andere Hälfte: 2 Stämme", 680, 345, "e_rest", "Bold", 32),
    pl("Verena: 1/4", 680, 405, "e_ver", fill=BLAU, size=38),
    pl("Severin: 1/4", 680, 490, beim("e_sev", "Severin"), fill=GRUEN, size=38),
    blk(110, 790, 760, 80, GELB, "probe", [("Gegenprobe: 1/2 + 1/4 + 1/4 = 1", "ExtraBold", 36, INK)]),
    *neinz("Mathilda, Egbert: nichts", 600, "e_nicht", "Bold", 34, x=725),
    *requisit([("erg", ("tabler", "chart-pie", 100, WEISS), "Ergebnis", WEISS),
               ("probe", ("tabler", "equal", 90, GELB), "Summe = 1", GELB)]),
    peep_voll("CH_ruhig", 1360, FB, 440, "erg", anim="pop"), ns("Christa", 1360, FB, "erg", LILA, d=0.1),
    *fig("VE", 1560, FB, 440, [("erg", "ruhig"), ("e_ver", "froh"), ("e_nicht", "ruhig")]),
    ns("Verena", 1560, FB, "erg", BLAU, d=0.1),
    *fig("SE", 1760, FB, 440, [("erg", "ruhig"), ("e_sev", "froh"), ("e_nicht", "ruhig")]),
    ns("Severin", 1760, FB, "erg", GRUEN, d=0.1),
], x0=1230))

# ===========================================================================================================================
# J Variante: Gütertrennung, § 1931 Abs. 4 BGB
# ===========================================================================================================================
w34, w34_y = wortkarte(80, 165, 1100, "„Bestand beim Erbfall Gütertrennung und sind als gesetzliche Erben neben dem "
                       "überlebenden Ehegatten ein oder zwei Kinder des Erblassers berufen, so erben der überlebende Ehegatte "
                       "und jedes Kind zu gleichen Teilen; § 1924 Abs. 3 gilt auch in diesem Falle.“", "§ 1931 Abs. 4 BGB",
                       "guet", marken=[("Gütertrennung", beim("guet", "Gütertrennung")), ("ein oder zwei Kinder", beim("guet", "zwei")),
                                       ("zu gleichen Teilen", beim("guet", "gleichen")), ("§ 1924 Abs. 3", beim("drittel", "Stelle"))],
                       size=30)
folie([("guet", "Variante › Gütertrennung, § 1931 Abs. 4 BGB"), ("drittel", "Variante › je 1/3")], rechts_frei([
    *tafel("guet", "Variante: Gütertrennung"),
    *w34,
    *kreis(270, w34_y + 160, 130, [(-90, 30, LILA), (30, 150, BLAU), (150, 270, GRUEN)],
           [beim("drittel", "Drittel")] * 3, ["1/3", "1/3", "1/3"]),
    pl("Christa: 1/3", 470, w34_y + 50, beim("drittel", "Drittel"), fill=LILA, size=34),
    pl("Verena: 1/3", 470, w34_y + 130, beim("drittel", "Drittel"), fill=BLAU, size=34),
    pl("Severin (statt Andreas): 1/3", 470, w34_y + 210, beim("drittel", "Drittel"), fill=GRUEN, size=34),
    *requisit([("guet", ("tabler", "arrows-split", 100, WEISS), "Gütertrennung", WEISS),
               (beim("drittel", "Drittel"), ("tabler", "chart-pie", 100, WEISS), "je 1/3", WEISS)]),
    *zwei("CH", [("guet", "ruhig")], "SE", [("guet", "ruhig"), ("drittel", "ernst")]),
]))
assert w34_y + 300 <= 890, w34_y

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Ehegattenquote zuerst"), ("t3", "Klausurtipp · Rest nach Stämmen"),
       ("t4", "Klausurtipp · Erbengemeinschaft, § 2032 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst: die Quote des Ehegatten", 200, 200, beim("tipp", "Bestimme"), "Bold", 38),
    z("Dafür nötig: Welche Ordnung kommt zum Zug?", 200, 275, "t1", size=34),
    z("und welcher Güterstand galt (§ 1371, § 1931 Abs. 4)", 200, 330, "t2", size=34),
    linienzug([(130, 405), (1130, 405)], "t3", breite=3),
    z("Erst dann: den Rest nach Stämmen verteilen", 200, 430, "t3", "Bold", 36),
    z("§ 1924 Abs. 2–4 BGB", 200, 485, "t3", size=30, farbe=TEXT),
    z("Mehrere Erben: Erbengemeinschaft", 200, 560, "t4", "Bold", 36),
    z("§ 2032 Abs. 1 BGB", 200, 615, "t4", size=30, farbe=TEXT),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Erbfall ohne Verfügung von Todes wegen", True),
          ("s1", 1, "§§ 1922, 1937 BGB", False),
          ("s2", 0, "II. Vorrangige Ordnung, §§ 1924–1930 BGB", True),
          ("s3", 0, "III. Erbteil des Ehegatten", True),
          ("s3a", 1, "§ 1931 Abs. 1 BGB: neben der 1. Ordnung 1/4", False),
          ("s3b", 1, "Zugewinngemeinschaft: plus 1/4, § 1371 Abs. 1 BGB", False),
          ("s4", 0, "IV. Rest nach Stämmen", True),
          ("s4a", 1, "Repräsentation und Eintrittsrecht, § 1924 Abs. 2, 3 BGB", False),
          ("s5", 0, "V. Gegenprobe: Summe = 1", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Gesetzliche Erbfolge"), 110, 90, "sch", 46),
           z("§§ 1922, 1924–1931, 1371 BGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 80, 1: 70}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Erbfall"), ("s2", "Prüfschema › II. Vorrangige Ordnung"),
       ("s3", "Prüfschema › III. Erbteil des Ehegatten"), ("s4", "Prüfschema › IV. Rest nach Stämmen"),
       ("s5", "Prüfschema › V. Gegenprobe")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst die ", 0), ("Quote des Ehegatten", "a"), (",", 0)], [("dann der Rest nach", 0)],
                 [("Ordnungen und Stämmen.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "Quote")}),
    *markertext([[("Wer lebt, schließt seine", 0)], [("Abkömmlinge aus;", 0)], [("an die Stelle eines Verstorbenen", 0)],
                 [("treten seine ", 0), ("Abkömmlinge", "b"), (".", 0)]], 750, 560, 44, "m2",
                {"b": beim("m2", "Abkömmlinge", nr=2)}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
