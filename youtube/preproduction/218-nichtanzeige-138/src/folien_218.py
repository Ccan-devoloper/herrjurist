"""Folge 218 · Nichtanzeige geplanter Straftaten § 138: Freund verraten? – Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv, ohne Ort, ohne echte Personen, ohne echten Messenger und ohne Logos): Donnerstagabend liest Sören im privaten
Chat, dass sein Freund Mirko am Samstag den Juwelier am Markt überfallen will. Mirko bestätigt auf Nachfrage. Sören schweigt.
Am Samstag versucht Mirko den Überfall; die Verkäuferin löst den Alarm aus, niemand wird verletzt, die Polizei fasst Mirko.
DARSTELLUNG: keine Waffen, kein Überfall im Bild (nur Chat-Blasen auf einem Handy aus Grundformen und das Juweliersymbol),
Mirko ohne Gangster-Klischee (Alltagskleidung, ruhige Mimik).
Szenen laut ../SZENENPLAN.md: A1 Wohnzimmer (Chat), A2 Sören schweigt, A3 Samstag am Juwelier, A4 Frage, B Sachverhalt,
C Wortlaut § 138 Abs. 1, D echtes Unterlassungsdelikt, E 1. Katalogtat, F 2. glaubhafte Kenntnis, G 3. rechtzeitig,
H 4. Unterlassen der Anzeige, I 5. Vorsatz/Abs. 3, J § 139 Abs. 3 (Angehörige), K § 139 Abs. 4/2/1, L Abgrenzung,
M Lösung, N Klausurtipp (Lexi), O Prüfschema, P Merksatz (Lexi).
Jeder Prüfungspunkt hat eine eigene Farbe (PUNKTFARBE), gleich auf den Punkttafeln und im Prüfschema.
Zwei Handlungsgeräusche: Handyvibration bei Mirkos Nachricht, Ladenalarm (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
punkt/marken_aus als eigene Kopie aus Folge 185 (gemeinsame Dateien unverändert); neu: handy(), nachricht(), sofa(),
fenster(), laden().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_218/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_218/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026, Folge 218), als Zitat mit Normangabe;
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
NAME = {"SO": "Sören", "MI": "Mirko"}
NFARBE = {"SO": BLAU, "MI": ORANGE}
FIGDIR = bausteine.FIG + bausteine.FIGORDNER


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
    return [*stehend(a, X1, folge_a), *stehend(b, X2, folge_b)]


PUNKTFARBE = {1: GELB, 2: LILA, 3: BLAU, 4: ROT, 5: GRUEN, "II": TUERKIS, "III": PINK, "IV": ORANGE}


def punkt(nr, text, cue, y=170, h=78, size=36):
    return blk(110, y, 1040, h, PUNKTFARBE[nr], cue, [(text, "ExtraBold", size, INK)])


def marken_aus(zeilen, liste):
    """[(phrase, cue)] → [(zeile, phrase, cue)]; jede Phrase muss vollständig in einer Zeile stehen."""
    aus = []
    for ph, c in liste:
        zi = next((i for i, t in enumerate(zeilen) if ph in t), None)
        assert zi is not None, f"Marker {ph!r} nicht in einer Zeile: {zeilen}"
        aus.append((zi, ph, c))
    return aus


def plus(c, s):
    return (c[0], round(c[1] + s, 3)) if isinstance(c, tuple) else (c, s)


# ===========================================================================================================================
# Bühnenteile aus Grundformen (keine Logos, kein echter Messenger)
# ===========================================================================================================================
BODEN = 880
HELLGRAU = (226, 226, 222, 255)
GLAS = (226, 238, 250, 255)
SOFA = (184, 169, 245, 255)
WAND = (250, 240, 222, 255)
CHATGRUEN = (214, 242, 214, 255)
HX, HY, HW, HH = 120, 40, 700, 930          # Handy (Chat) links


def _bild(w, h, s=2):
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    return im, ImageDraw.Draw(im), s


def _klein(im, s):
    return im.resize((im.width // s, im.height // s), Image.LANCZOS)


def handy(c):
    """Großes Handy mit Chatfenster (Grundformen): Rahmen, Kopfzeile mit Initiale und Name, ohne App-Logo."""
    im, d, s = _bild(HW, HH)
    d.rounded_rectangle((2 * s, 2 * s, (HW + 2) * s, (HH + 2) * s), 46 * s, fill=INK)
    d.rounded_rectangle((18 * s, 18 * s, (HW - 14) * s, (HH - 14) * s), 32 * s, fill=(246, 244, 240, 255))
    d.rounded_rectangle((18 * s, 18 * s, (HW - 14) * s, 104 * s), 32 * s, fill=HELLGRAU)
    d.rectangle((18 * s, 70 * s, (HW - 14) * s, 104 * s), fill=HELLGRAU)
    d.line((18 * s, 104 * s, (HW - 14) * s, 104 * s), fill=INK, width=3 * s)
    d.ellipse((44 * s, 30 * s, 104 * s, 90 * s), fill=ORANGE, outline=INK, width=3 * s)
    f = F("ExtraBold", 34 * s)
    d.text((74 * s, 60 * s), "M", font=f, fill=INK, anchor="mm")
    d.text((124 * s, 60 * s), glyphen("Mirko"), font=F("Bold", 36 * s), fill=INK, anchor="lm")
    return El(_klein(im, s), HX, HY, c, "cut", 0.0, None, name="handy")


def nachricht(zeilen, zeit, y, c, ein=True):
    """Chatnachricht im Handy: eingehend (weiß, links) oder ausgehend (hellgrün, rechts); Text 30 px, Uhrzeit 26 px."""
    f, fz = F("Regular", 30), F("Regular", 26)
    for t in zeilen:
        glyphen(t)
    bw = int(max(f.getlength(t) for t in zeilen) + 50)
    bw = max(bw, int(fz.getlength(zeit)) + 60)
    bh = 26 + 40 * len(zeilen) + 34
    assert bw <= HW - 90, f"Nachricht zu breit: {zeilen}"
    im, d, s = _bild(bw, bh)
    d.rounded_rectangle((2 * s, 2 * s, (bw + 2) * s, (bh + 2) * s), 20 * s, fill=WEISS if ein else CHATGRUEN,
                        outline=INK, width=3 * s)
    fs, fzs = F("Regular", 30 * s), F("Regular", 26 * s)
    for i, t in enumerate(zeilen):
        d.text((24 * s, (16 + 40 * i) * s), t, font=fs, fill=INK)
    d.text(((bw - 18) * s, (bh - 8) * s), zeit, font=fzs, fill=TEXT, anchor="rd")
    im = _klein(im, s)
    x = HX + 44 if ein else HX + HW - 40 - im.width
    return El(im, x, y, c, "pop", 0.0, None, name="nachricht:" + "/".join(zeilen))


def sofa(c, x0=1110, x1=1870, sitz=790):
    """Sofa aus Grundformen: Rückenlehne, Sitzpolster, Armlehnen, Füße."""
    w, h = x1 - x0, BODEN - 520
    im, d, s = _bild(w, h)
    top = 0
    d.rounded_rectangle((40 * s, (top + 10) * s, (w - 40) * s, (sitz - 520 + 20) * s), 30 * s, fill=SOFA, outline=INK, width=5 * s)
    d.rounded_rectangle((4 * s, (sitz - 520 - 70) * s, 90 * s, (sitz - 520 + 60) * s), 26 * s, fill=SOFA, outline=INK, width=5 * s)
    d.rounded_rectangle(((w - 90) * s, (sitz - 520 - 70) * s, (w - 4) * s, (sitz - 520 + 60) * s), 26 * s, fill=SOFA, outline=INK, width=5 * s)
    d.rounded_rectangle((30 * s, (sitz - 520) * s, (w - 30) * s, (sitz - 520 + 64) * s), 18 * s, fill=SOFA, outline=INK, width=5 * s)
    for fx in (70, w - 90):
        d.rectangle((fx * s, (sitz - 520 + 64) * s, (fx + 22) * s, (h - 2) * s), fill=INK)
    return El(_klein(im, s), x0, 520, c, "cut", 0.0, None, name="sofa")


def fenster(c, x=880, y=130, w=190, h=250):
    """Fenster mit Nachthimmel (Abend), Mond als Tabler-Icon darüber gelegt."""
    im, d, s = _bild(w, h)
    d.rounded_rectangle((2 * s, 2 * s, (w + 2) * s, (h + 2) * s), 10 * s, fill=(70, 84, 130, 255), outline=INK, width=6 * s)
    d.line(((w // 2 + 2) * s, 4 * s, (w // 2 + 2) * s, h * s), fill=INK, width=5 * s)
    d.line((4 * s, (h // 2 + 2) * s, w * s, (h // 2 + 2) * s), fill=INK, width=5 * s)
    return El(_klein(im, s), x, y, c, "cut", 0.0, None, name="fenster")


def laden(c, x0=420, x1=1400, oben=300):
    """Juweliergeschäft aus Grundformen: Wand, Schild „Juwelier“, Schaufenster, Tür (ohne Logo, ohne Personen)."""
    w, h = x1 - x0, BODEN - oben
    im, d, s = _bild(w, h)
    d.rectangle((2 * s, 60 * s, (w + 2) * s, (h + 2) * s), fill=WAND, outline=INK, width=5 * s)
    d.rounded_rectangle((60 * s, 2 * s, (w - 56) * s, 110 * s), 16 * s, fill=WEISS, outline=INK, width=5 * s)
    d.text(((w // 2) * s, 56 * s), glyphen("Juwelier"), font=F("ExtraBold", 60 * s), fill=INK, anchor="mm")
    d.rounded_rectangle((60 * s, 170 * s, (w - 330) * s, 470 * s), 10 * s, fill=GLAS, outline=INK, width=5 * s)
    d.rectangle(((w - 250) * s, 170 * s, (w - 70) * s, (h + 2) * s), fill=(214, 160, 110, 255), outline=INK, width=5 * s)
    d.ellipse(((w - 110) * s, 380 * s, (w - 90) * s, 400 * s), fill=INK)
    return El(_klein(im, s), x0, oben, c, "cut", 0.0, None, name="laden")


_h = hart
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
RP = 1100                                    # Pillen der Fallszene rechts oben
SX, SU, SH = 1490, 800, 440                 # Sören sitzt im Schneidersitz auf dem Sofa

# ===========================================================================================================================
# A1 Fall: Donnerstagabend, der Chat
# ===========================================================================================================================
folie([(NULL, "Fall · Donnerstagabend"), ("chat", "Fall · Der Chat mit Mirko"), ("m1", "Fall · Mirko schreibt"),
       ("witz", "Fall · Sören fragt nach"), ("so1", "Fall · Sören will schweigen")], [
    _h(boden(BODEN, NULL)), _h(fenster(NULL, x=870, y=380, w=170, h=230)), _h(ficon("tabler", "moon", 955, 530, 64, NULL, fuell=GELB, anim="cut")),
    _h(sofa(NULL)), _h(handy(NULL)),
    _h(pl("Donnerstagabend", RP, 30, NULL, fill=GELB, size=36)),
    pl("Sören liest einen privaten Chat.", RP, 110, "chat", fill=WEISS, size=34, bis="so1"),
    _h(peep_voll("SO_sitzt", SX, SU, SH, NULL, anim="cut", bis="chat")),
    peep_voll("SO_liest", SX, SU, SH, "chat", anim="cut", bis="m3"),
    peep_voll("SO_sitzt_denkt", SX, SU, SH, "m3", anim="cut", bis="so1"),
    *redet("SO_sitzt_redet", SX, SU, SH, "so1", "schweigt"),
    _h(ns("Sören", SX, 870, NULL, BLAU, anim="cut")),
    ficon("fluent-emoji-flat", "mobile-phone", SX + 40, 668, 56, "chat"),
    szene(nachricht(["Am Samstag überfalle ich den", "Juwelier am Markt."], "21:40", 140, "m1"), "218handy*", 0.7, 0.0),
    nachricht(["Ich bedrohe die Verkäuferin,", "dann gibt sie mir den Schmuck."], "21:40", 300, "m2"),
    nachricht(["Das ist ein Witz, oder?"], "21:41", 460, "witz", ein=False),
    nachricht(["Nein. Ich brauche das Geld."], "21:42", 580, "m3"),
    nachricht(["Samstag, 18 Uhr,", "kurz vor Ladenschluss."], "21:42", 700, "m4"),
    blase("sprech", 600, 200, "so1", 1290, 215, inhalt=["Mirko ist mein Freund.", "Den verrate ich nicht."], textsize=36,
          figur=("SO_sitzt_redet", SX, SU, SH), bis="schweigt"),
])

# ===========================================================================================================================
# A2 Fall: Sören schweigt
# ===========================================================================================================================
folie([("schweigt", "Fall · Sören schweigt")], [
    hart(boden(BODEN, "schweigt")),
    peep_voll("SO_still", 960, BODEN, 470, "schweigt", anim="cut"),
    ns("Sören", 960, BODEN, "schweigt", BLAU, anim="cut"),
    pl("Sören sagt niemandem etwas.", 70, 30, "schweigt", fill=WEISS, size=36),
    ficon("fluent-emoji-flat", "police-car", 430, BODEN, 300, beim("schweigt", "Polizei")),
    pl("Polizei", 430, BODEN + 22, beim("schweigt", "Polizei"), fill=WEISS, size=30, anker="m"),
    nein(560, 600, beim("schweigt", "Polizei", ende=True), gr=34),
    ficon("tabler", "diamond", 1500, BODEN - 40, 220, beim("schweigt", "Juwelier"), fuell=BLAU),
    pl("Juwelier", 1500, BODEN + 22, beim("schweigt", "Juwelier"), fill=WEISS, size=30, anker="m"),
    nein(1640, 600, plus(beim("schweigt", "Juwelier"), 0.3), gr=34),
])

# ===========================================================================================================================
# A3 Fall: Samstag, 18 Uhr am Juwelier (kein Überfall im Bild, keine Personen)
# ===========================================================================================================================
folie([("samstag", "Fall · Samstag, 18 Uhr"), ("alarm", "Fall · Alarm im Laden"), ("polizei", "Fall · Die Polizei fasst Mirko")], [
    hart(boden(BODEN, "samstag")), hart(laden("samstag")),
    *[ficon("tabler", "diamond", x, 660, 90, "samstag", fuell=BLAU, anim="cut") for x in (600, 775, 950)],
    pl("Samstag, 18 Uhr", 70, 30, "samstag", fill=GELB, size=36),
    pl("Mirko versucht den Überfall.", 70, 110, beim("samstag", "versucht"), fill=WEISS, size=34),
    szene(ficon("tabler", "bell-ringing", 290, 440, 120, "alarm", fuell=ROT), "218alarm*", 0.6, 0.05),
    pl("Die Verkäuferin löst den Alarm aus.", 70, 190, "alarm", fill=HELLROT, size=34),
    pl("Niemand wird verletzt.", 1000, 30, beim("alarm", "niemand"), fill=GRUEN, size=34),
    ficon("fluent-emoji-flat", "police-car", 1650, BODEN, 320, "polizei"),
    pl("Die Polizei fasst Mirko noch am Abend.", 1000, 110, "polizei", fill=WEISS, size=34),
])

# ===========================================================================================================================
# A4 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Strafbar, weil er schweigt?")], [
    hart(boden(BODEN, "frage")),
    peep_voll("SO_denkt_r", 700, BODEN, 470, "frage", anim="pop"), ns("Sören", 700, BODEN, "frage", BLAU, d=0.1),
    peep_voll("MI_still", 1220, BODEN, 470, "frage", anim="pop"), ns("Mirko", 1220, BODEN, "frage", ORANGE, d=0.1),
    pl("Hat sich Sören strafbar gemacht, nur weil er geschwiegen hat?", 70, 30, "frage", fill=WEISS, size=36),
    pl("Muss man seinen Freund verraten?", 70, 110, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_218(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_218("sv", [
    "Donnerstagabend: Sören liest auf seinem Handy einen privaten Chat mit seinem Freund Mirko. Mirko schreibt: „Am "
    "Samstag überfalle ich den Juwelier am Markt. Ich bedrohe die Verkäuferin, dann gibt sie mir den Schmuck.“ Sören fragt "
    "zurück, ob das ein Witz ist. Mirko antwortet: „Nein. Ich brauche das Geld. Samstag, 18 Uhr, kurz vor Ladenschluss.“",
    "Sören denkt: „Mirko ist mein Freund. Den verrate ich nicht.“ Er sagt niemandem etwas, weder der Polizei noch dem "
    "Juwelier. Am Samstag um 18 Uhr versucht Mirko den Überfall. Die Verkäuferin löst den Alarm aus, niemand wird verletzt. "
    "Die Polizei fasst Mirko noch am selben Abend.",
], "Hat sich Sören strafbar gemacht?")

# ===========================================================================================================================
# C § 138 Abs. 1 StGB (Wortlautkarte, Nr. 7)
# ===========================================================================================================================
W138 = ["„(1) Wer von dem Vorhaben oder der Ausführung …", "7. eines Raubes oder einer räuberischen Erpressung",
        "(§§ 249 bis 251 oder 255) …"] + umbruch(
    "zu einer Zeit, zu der die Ausführung oder der Erfolg noch abgewendet werden kann, glaubhaft erfährt und es unterläßt, "
    "der Behörde oder dem Bedrohten rechtzeitig Anzeige zu machen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit "
    "Geldstrafe bestraft.“", 34, 1020)
w138, w138_y = wortlaut(80, 170, 1100, W138, "§ 138 Abs. 1 Nr. 7 StGB", "p138", marken=marken_aus(W138, [
    ("Vorhaben", beim("p138", "Vorhaben")), ("Raubes", beim("nr7", "Raubes")),
    ("räuberischen Erpressung", beim("nr7", "räuberischen")), ("abgewendet", beim("zeitw", "abgewendet")),
    ("glaubhaft erfährt", beim("zeitw", "glaubhaft")), ("unterläßt", beim("zeitw", "unterlässt")),
    ("Behörde", beim("zeitw", "Behörde")), ("Bedrohten", beim("zeitw", "Bedrohten")),
    ("rechtzeitig", beim("zeitw", "rechtzeitig")), ("fünf Jahren", beim("strafe", "fünf"))]), size=34)
folie([("p138", "Die Norm · § 138 Abs. 1 StGB"), ("nr7", "Die Norm · § 138 Abs. 1 Nr. 7: Raub, räuberische Erpressung"),
       ("strafe", "Die Norm · Strafrahmen, § 138 Abs. 1 StGB")], rechts_frei([
    *tafel("p138", "§ 138 StGB: Nichtanzeige geplanter Straftaten", size=40),
    *w138,
    blk(110, w138_y + 30, 1040, 78, GELB, beim("strafe", "Freiheitsstrafe"),
        [("Strafrahmen: bis 5 Jahre oder Geldstrafe", "ExtraBold", 36, INK)]),
    *requisit([("p138", ("tabler", "book", 100, WEISS), "§ 138 Abs. 1 StGB", GELB),
               ("nr7", ("tabler", "diamond", 100, BLAU), "Nr. 7: Raub", WEISS),
               (beim("strafe", "Freiheitsstrafe"), ("tabler", "scale", 100, WEISS), "bis 5 Jahre oder Geldstrafe", WEISS)]),
    *stehend("SO", FX, [("p138", "ruhig"), ("nr7", "ernst")]),
]))

# ===========================================================================================================================
# D Echtes Unterlassungsdelikt
# ===========================================================================================================================
folie([("echt", "Einordnung · echtes Unterlassungsdelikt"), ("garant", "Einordnung · keine Garantenstellung nötig"),
       ("jeder", "Einordnung · Anzeigepflicht für jeden")], rechts_frei([
    *tafel("echt", "Echtes Unterlassungsdelikt"),
    *okz("Bestraft wird das Schweigen selbst.", 200, beim("echt", "Bestraft"), "Bold", 36, x=160),
    zit("vgl. BGH 5 StR 464/09, Rn. 15", 160, 255, beim("echt", "Schweigen")),
    *okz("Keine Garantenstellung nötig", 340, "garant", "Bold", 36, x=160),
    *okz("Anzeigen muss grundsätzlich jeder,", 480, "jeder", "Bold", 36, x=160),
    z("der von der Tat erfährt.", 160, 532, beim("jeder", "der"), "Bold", 36),
    zit("§ 138 Abs. 1 StGB: „Wer …“", 160, 587, beim("jeder", "erfährt")),
    *requisit([("echt", ("tabler", "message-off", 100, WEISS), "Schweigen", HELLROT),
               ("garant", ("tabler", "shield", 100, WEISS), "keine Garantenstellung", WEISS),
               ("jeder", ("tabler", "speakerphone", 100, WEISS), "jeder muss anzeigen", GELB)]),
    *zwei("SO", [("echt", "still"), ("jeder", "ruhig")], "MI", [("echt", "ruhig"), ("jeder", "ernst")]),
]))

# ===========================================================================================================================
# E I. 1. Geplante Katalogtat (Vorhaben)
# ===========================================================================================================================
PT = "I. Tatbestand"
folie([("kat", f"{PT} › 1. Geplante Katalogtat"), ("raub", f"{PT} › 1. Katalogtat: Nr. 7 Raub"),
       ("vorh", f"{PT} › 1. Vorhaben: ernsthafter Tatplan"), ("vorh2", f"{PT} › 1. Geplante Katalogtat (+)")], rechts_frei([
    *tafel("kat", "I. Tatbestand: Katalogtat"),
    punkt(1, "1. Geplante Katalogtat", "kat"),
    z("§ 138 zählt die Taten abschließend auf.", 110, 278, "abschl", "Bold", 34),
    *okz("Raub, räuberische Erpressung: Nr. 7", 345, "raub", "Bold", 34, x=160),
    *neinz("Einbruch ohne Gewalt oder Drohung:", 410, "einbr", "Bold", 34, x=160),
    z("nicht im Katalog", 160, 460, beim("einbr", "stünde"), "Bold", 34),
    blk(110, 530, 1040, 120, GELB, "vorh", [("Vorhaben: ernsthafter Tatplan, Ziel und", "ExtraBold", 32, INK),
                                            ("Vorgehen wenigstens in Grundzügen fest", "ExtraBold", 32, INK)]),
    zit("BGH StB 33/16, Rn. 22", 110, 662, beim("vorh", "Grundzügen")),
    *okz("Laden, Tag, Uhrzeit, Drohung: Vorhaben", 725, "vorh2", "Bold", 34, x=160),
    *requisit([("kat", ("tabler", "list", 100, WEISS), "Katalog: Nr. 1 bis 8", GELB),
               ("raub", ("tabler", "diamond", 100, BLAU), "Nr. 7: Raub", WEISS),
               ("einbr", ("tabler", "lock-open", 100, WEISS), "Einbruch: nicht im Katalog", HELLROT),
               ("vorh", ("tabler", "clipboard-list", 100, WEISS), "ernsthafter Tatplan", GELB),
               ("vorh2", ("tabler", "calendar-event", 100, WEISS), "Samstag, 18 Uhr", GRUEN)]),
    *stehend("MI", FX, [("kat", "ruhig"), ("vorh2", "ernst")]),
]))

# ===========================================================================================================================
# F I. 2. Glaubhafte Kenntnis
# ===========================================================================================================================
folie([("glaub", f"{PT} › 2. Glaubhafte Kenntnis"), ("scherz", f"{PT} › 2. Scherz? Nachfrage!"),
       ("glaub2", f"{PT} › 2. Glaubhafte Kenntnis (+)")], rechts_frei([
    *tafel("glaub", "I. Tatbestand: glaubhafte Kenntnis"),
    punkt(2, "2. Glaubhafte Kenntnis", "glaub"),
    z("So erfahren, dass er ernsthaft mit", 110, 285, "ernst", "Bold", 36),
    z("der Tat rechnet", 110, 340, beim("ernst", "der"), "Bold", 36),
    zit("vgl. BGH AK 33/17, Rn. 28", 110, 397, beim("ernst", "rechnet")),
    *neinz("Erkennbarer Scherz: genügt nicht", 470, "scherz", "Bold", 34, x=160),
    *okz("Sören fragt nach, Mirko bestätigt den Plan:", 560, "glaub2", "Bold", 34, x=160),
    z("glaubhaft erfahren", 160, 612, beim("glaub2", "Sören", nr=2), "Bold", 34),
    *requisit([("glaub", ("tabler", "message-question", 100, WEISS), "ernst gemeint?", LILA),
               ("scherz", ("tabler", "mood-wink", 100, GELB), "nur ein Scherz?", WEISS),
               ("glaub2", ("tabler", "message", 100, WEISS), "„Nein. Ich brauche das Geld.“", GRUEN)]),
    *stehend("SO", FX, [("glaub", "denkt"), ("glaub2", "ernst")]),
]))

# ===========================================================================================================================
# G I. 3. Rechtzeitig (BGHSt 42, 86)
# ===========================================================================================================================
def zeitstrahl(cue, y=300):
    els = [linienzug([(160, y), (1100, y)], cue, breite=6)]
    els.append(pfeil(1050, y, 1120, y, cue, breite=6, kopf=26))
    for x, t, c in ((330, "Do: Sören erfährt davon", beim("rz1", "Donnerstag")),
                    (920, "Sa, 18 Uhr: Tat", beim("rz1", "Samstag"))):
        els.append(okreis(x, y, c))
        els.append(pl(t, x, y + 30, c, fill=WEISS, size=28, anker="m"))
    return els


def okreis(x, y, c):
    im = Image.new("RGBA", (40, 40))
    ImageDraw.Draw(im).ellipse((2, 2, 37, 37), fill=PUNKTFARBE[3], outline=INK, width=4)
    return El(im, x - 20, y - 20, c, "pop", 0.0, None, name="zeitpunkt")


folie([("rz", f"{PT} › 3. Rechtzeitig"), ("unv", f"{PT} › 3. Nicht sofort, aber rechtzeitig"),
       ("risiko", f"{PT} › 3. Wer abwartet, trägt das Risiko")], rechts_frei([
    *tafel("rz", "I. Tatbestand: rechtzeitig"),
    punkt(3, "3. Rechtzeitig", "rz"),
    *zeitstrahl("rz1"),
    *okz("Tat kann noch abgewendet werden.", 400, beim("rz1", "kann"), "Bold", 34, x=160),
    z("Nicht sofort, aber so früh, dass die", 110, 485, "unv", "Bold", 34),
    z("Anzeige die Tat noch verhindern kann", 110, 537, beim("unv", "aber"), "Bold", 34),
    zit("BGH 1 StR 497/95, Rn. 6 (BGHSt 42, 86)", 110, 592, beim("unv", "verhindern")),
    blk(110, 650, 1040, 78, PUNKTFARBE[3], "risiko", [("Wer abwartet, trägt das Risiko.", "ExtraBold", 34, INK)]),
    zit("BGH 1 StR 497/95, Rn. 7", 110, 740, beim("risiko", "Risiko")),
    *requisit([("rz", ("tabler", "clock", 100, BLAU), "rechtzeitig?", BLAU),
               ("rz1", ("tabler", "calendar-event", 100, WEISS), "Donnerstag bis Samstag", WEISS),
               ("risiko", ("tabler", "hourglass-high", 100, WEISS), "zu spät?", HELLROT)]),
    *stehend("SO", FX, [("rz", "ruhig"), ("risiko", "denkt")]),
]))

# ===========================================================================================================================
# H I. 4. Unterlassen der Anzeige (Behörde oder Bedrohter)
# ===========================================================================================================================
folie([("anz", f"{PT} › 4. Unterlassen der Anzeige"), ("wem", f"{PT} › 4. Anzeige an Behörde oder Bedrohten"),
       ("anz2", f"{PT} › 4. Unterlassen der Anzeige (+)")], rechts_frei([
    *tafel("anz", "I. Tatbestand: Unterlassen der Anzeige"),
    punkt(4, "4. Unterlassen der Anzeige", "anz"),
    z("Anzeigen kann er bei", 110, 285, "wem", "Bold", 36),
    blk(110, 350, 500, 120, WEISS, "wem", [("der Behörde,", "ExtraBold", 34, INK), ("etwa der Polizei", "Regular", 32, INK)]),
    blk(650, 350, 500, 120, WEISS, "bedr", [("dem Bedrohten,", "ExtraBold", 34, INK), ("hier dem Juwelier", "Regular", 32, INK)]),
    *neinz("Sören sagt keinem von beiden etwas.", 520, "anz2", "Bold", 34, x=160),
    *requisit([("anz", ("tabler", "message-off", 100, WEISS), "Anzeige?", ROT),
               ("wem", ("fluent-emoji-flat", "police-car", 150, None), "Polizei", WEISS),
               ("bedr", ("tabler", "diamond", 100, BLAU), "Juwelier: der Bedrohte", WEISS),
               ("anz2", ("tabler", "message-off", 100, WEISS), "Sören schweigt", HELLROT)]),
    *stehend("SO", FX, [("anz", "ruhig"), ("anz2", "still")]),
]))

# ===========================================================================================================================
# I I. 5. Vorsatz, Abs. 3 Leichtfertigkeit
# ===========================================================================================================================
folie([("vors", f"{PT} › 5. Vorsatz"), ("abs3", f"{PT} › 5. § 138 Abs. 3: Leichtfertigkeit")], rechts_frei([
    *tafel("vors", "I. Tatbestand: Vorsatz"),
    punkt(5, "5. Vorsatz", "vors"),
    *okz("Sören weiß, dass Mirko es ernst meint,", 285, "vors1", "Bold", 34, x=160),
    z("und schweigt bewusst.", 160, 337, beim("vors1", "und"), "Bold", 34),
    linienzug([(130, 430), (1130, 430)], "abs3", breite=3),
    z("§ 138 Abs. 3 StGB:", 110, 460, "abs3", "Bold", 34, farbe=TEXT),
    blk(110, 520, 1040, 78, PUNKTFARBE[5], beim("abs3", "leichtfertige"),
        [("Auch leichtfertige Nichtanzeige ist strafbar,", "ExtraBold", 32, INK)]),
    z("bis 1 Jahr oder Geldstrafe", 110, 620, beim("abs3", "Freiheitsstrafe"), "Bold", 34),
    *requisit([("vors", ("tabler", "eye-check", 100, GRUEN), "weiß Bescheid", GRUEN),
               ("abs3", ("tabler", "alert-triangle", 100, GELB), "Abs. 3: leichtfertig", WEISS)]),
    *stehend("SO", FX, [("vors", "ernst"), ("abs3", "still")]),
]))

# ===========================================================================================================================
# J § 139 Abs. 3 (Wortlautkarte), § 11 Abs. 1 Nr. 1, Gegenfall Bruder
# ===========================================================================================================================
W139_3 = umbruch("„(3) Wer eine Anzeige unterläßt, die er gegen einen Angehörigen erstatten müßte, ist straffrei, wenn er "
                 "sich ernsthaft bemüht hat, ihn von der Tat abzuhalten oder den Erfolg abzuwenden, es sei denn, daß es "
                 "sich um 1. einen Mord oder Totschlag (§§ 211 oder 212) … handelt. …“", 32, 1040)
w139, w139_y = wortlaut(80, 160, 1100, W139_3, "§ 139 Abs. 3 Satz 1 StGB", "ang", marken=marken_aus(W139_3, [
    ("Angehörigen", beim("ang", "Angehörigen")), ("ernsthaft", beim("ang", "ernsthaft")),
    ("Mord", beim("mord", "Mord"))]), size=32)
folie([("p139", "§ 139 StGB · Straflosigkeit: die Ausnahmen"), ("ang", "§ 139 StGB › Abs. 3: Angehörige"),
       ("p11", "§ 139 StGB › Angehörige, § 11 Abs. 1 Nr. 1 StGB"), ("freund", "§ 139 StGB › Freund: kein Angehöriger"),
       ("bruder", "§ 139 StGB › Gegenfall: Mirko als Bruder")], rechts_frei([
    *tafel("p139", "§ 139 StGB: die Ausnahmen", size=44),
    *w139,
    z("§ 11 Abs. 1 Nr. 1 StGB: z. B. Eltern, Kinder,", 110, w139_y + 26, "p11", "Bold", 32),
    z("Ehegatten, Verlobte, Geschwister", 110, w139_y + 72, beim("p11", "Ehegatten"), "Bold", 32),
    *neinz("Ein Freund ist kein Angehöriger.", w139_y + 140, "freund", "Bold", 34, x=160),
    z("Bruder: straffrei nur bei ernsthaftem Bemühen", 110, w139_y + 210, "bruder", "Bold", 32),
    *requisit([("p139", ("tabler", "book", 100, WEISS), "§ 139 StGB", ORANGE),
               ("ang", ("tabler", "home-heart", 100, WEISS), "Angehörige", WEISS),
               ("freund", ("tabler", "heart", 100, ROT), "Freund: nicht in § 11", HELLROT),
               ("bruder", ("tabler", "home-heart", 100, GELB), "wäre Mirko sein Bruder?", GELB)]),
    *zwei("SO", [("p139", "ruhig"), ("freund", "still")], "MI", [("p139", "ruhig"), ("bruder", "still")]),
]))

# ===========================================================================================================================
# K § 139 Abs. 4 (Wortlautkarte), Gegenfall Ausreden, Abs. 2, Abs. 1
# ===========================================================================================================================
W139_4 = umbruch("„(4) Straffrei ist, wer die Ausführung oder den Erfolg der Tat anders als durch Anzeige abwendet. …“",
                 34, 1020)
w4, w4_y = wortlaut(80, 160, 1100, W139_4, "§ 139 Abs. 4 Satz 1 StGB", "abs4", marken=marken_aus(W139_4, [
    ("abwendet", beim("abs4", "abwendet"))]), size=34)
folie([("abs4", "§ 139 StGB › Abs. 4: Abwendung auf andere Weise"), ("ausr", "§ 139 StGB › Gegenfall: Sören redet es Mirko aus"),
       ("ausr3", "§ 139 StGB › Abs. 4 hier (−)"), ("abs2", "§ 139 StGB › Abs. 2: Geistliche"),
       ("abs1", "§ 139 StGB › Abs. 1: Tat nicht versucht")], rechts_frei([
    *tafel("abs4", "§ 139 StGB: Abs. 4, 2 und 1", size=44),
    *w4,
    z("Gegenfall: Hätte Sören zu Mirko gesagt …", 110, w4_y + 30, "ausr", "Bold", 32),
    *okz("… und gibt Mirko deshalb auf: Sören straffrei", w4_y + 90, "ausr2", "Bold", 32, x=160),
    *neinz("Hier hat Sören nichts unternommen.", w4_y + 150, "ausr3", "Bold", 32, x=160),
    linienzug([(130, w4_y + 222), (1130, w4_y + 222)], "abs2", breite=3),
    z("Abs. 2: Geistliche müssen nicht anzeigen, was", 110, w4_y + 245, "abs2", "Bold", 32),
    z("ihnen als Seelsorger anvertraut wurde.", 110, w4_y + 291, beim("abs2", "was"), "Bold", 32),
    z("Abs. 1: Tat nicht versucht: Absehen von Strafe möglich", 110, w4_y + 360, "abs1", "Bold", 30),
    *redet("SO_redet_r", X1, FB, FR, "so2", "ausr2"),
    peep_voll("SO_ruhig_r", X1, FB, FR, "abs4", anim="pop", bis="so2"),
    peep_voll("SO_still", X1, FB, FR, "ausr2", anim="cut"),
    ns("Sören", X1, FB, "abs4", BLAU, d=0.1),
    peep_voll("MI_ernst", X2, FB, FR, "abs4", anim="pop", bis="ausr2"),
    peep_voll("MI_still", X2, FB, FR, "ausr2", anim="cut"),
    ns("Mirko", X2, FB, "abs4", ORANGE, d=0.1),
    blase("sprech", 560, 220, "so2", 1560, 250, inhalt=["Lass das, Mirko.", "Das ist es nicht wert."], textsize=36,
          figur=("SO_redet_r", X1, FB, FR), bis="ausr2"),
    *requisit([("abs2", ("tabler", "building-church", 110, WEISS), "Abs. 2: Seelsorger", LILA),
               ("abs1", ("tabler", "gavel", 100, WEISS), "Abs. 1: Absehen von Strafe", WEISS)]),
]))

# ===========================================================================================================================
# L Abgrenzung: Beteiligung (BGH), § 323c StGB (ein Satz, Verweis Folge 185)
# ===========================================================================================================================
folie([("bet", "Abgrenzung · Beteiligte an der Tat"), ("zusage", "Abgrenzung · Hilfe zugesagt? Beteiligung prüfen"),
       ("verd", "Abgrenzung · nur Verdacht der Beteiligung"), ("p323", "Abgrenzung · § 323c StGB")], rechts_frei([
    *tafel("bet", "Abgrenzung"),
    z("Beteiligt als Täter, Anstifter oder Gehilfe:", 110, 180, beim("bet", "Wer"), "Bold", 34),
    *neinz("nicht § 138, die Tat ist keine fremde", 232, beim("bet", "nicht"), "Bold", 34, x=160),
    zit("BGH 5 StR 464/09, Rn. 7, 17; 2 StR 493/15, Rn. 42", 160, 287, beim("bet", "fremde")),
    z("Hilfe zugesagt? Dann die Beteiligung prüfen.", 110, 352, "zusage", "Bold", 34),
    *okz("Nur Verdacht der Beteiligung: § 138 möglich", 425, "verd", "Bold", 34, x=160),
    zit("BGH 5 StR 464/09, Leitsatz und Rn. 14", 160, 480, beim("verd", "Nichtanzeige")),
    linienzug([(130, 555), (1130, 555)], "p323", breite=3),
    z("§ 323c StGB: verlangt einen Unglücksfall", 110, 585, beim("p323", "unterlassene"), "Bold", 34),
    z("§ 138 StGB: greift schon beim Vorhaben", 110, 640, beim("p323", "Paragraf"), "Bold", 34),
    z("Video: „Unterlassene Hilfeleistung“", 110, 700, beim("p323", "mehr"), "Bold", 30, farbe=TEXT),
    *requisit([("bet", ("tabler", "link", 100, WEISS), "Beteiligter?", LILA),
               ("zusage", ("fluent-emoji-flat", "handshake", 100, None), "Hilfe zugesagt?", WEISS),
               ("verd", ("tabler", "zoom-question", 100, WEISS), "nur Verdacht", GELB),
               ("p323", ("tabler", "first-aid-kit", 100, WEISS), "§ 323c: Unglücksfall", WEISS)]),
    *zwei("SO", [("bet", "denkt"), ("p323", "ruhig")], "MI", [("bet", "ruhig"), ("zusage", "ernst"), ("p323", "ruhig")]),
]))

# ===========================================================================================================================
# M Lösung
# ===========================================================================================================================
folie([("loes", "Lösung"), ("l1", "Lösung · Katalogtat: Raub"), ("l2", "Lösung · glaubhaft, rechtzeitig, keine Anzeige"),
       ("l3", "Lösung · § 139 Abs. 3 und 4 (−)"), ("l4", "Lösung · § 139 Abs. 1 (−)"),
       ("l5", "Lösung · Sören strafbar nach § 138 Abs. 1 Nr. 7")], rechts_frei([
    *tafel("loes", "Lösung: Sören"),
    *okz("Mirko plant einen Raub: Katalogtat", 190, "l1", "Bold", 34, x=160),
    *okz("glaubhaft und rechtzeitig erfahren,", 265, "l2", "Bold", 34, x=160),
    z("bewusst nicht angezeigt", 160, 317, beim("l2", "zeigt"), "Bold", 34),
    *neinz("kein Angehöriger, Tat nicht abgewendet", 400, "l3", "Bold", 34, x=160),
    *neinz("Tat versucht: kein Absehen von Strafe", 475, "l4", "Bold", 34, x=160),
    blk(110, 570, 1040, 78, GELB, "l5", [("Sören: strafbar nach § 138 Abs. 1 Nr. 7 StGB", "ExtraBold", 34, INK)]),
    *zwei("SO", [("loes", "ruhig"), ("l5", "still")], "MI", [("loes", "still")]),
]))

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Erst die Beteiligung prüfen"), ("tipp2", "Klausurtipp · Angehörige: ernsthaftes Bemühen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst: Ist der Schweigende an der", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("Tat selbst beteiligt?", 200, 255, beim("tipp", "an"), "Bold", 36),
    z("Erst wenn das ausscheidet: § 138 StGB", 200, 320, beim("tipp", "Erst"), "Bold", 36),
    linienzug([(130, 410), (1130, 410)], "tipp2", breite=3),
    z("Angehörige: Die Verwandtschaft allein", 200, 440, "tipp2", "Bold", 36),
    z("reicht nicht. Straffrei nur bei", 200, 495, beim("tipp2", "reicht"), "Bold", 36),
    z("ernsthaftem Bemühen.", 200, 550, beim("tipp2", "Straffrei"), "Bold", 36),
    zit("§ 139 Abs. 3 Satz 1 StGB", 200, 610, beim("tipp2", "bemüht")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Prüfschema (Farben wie auf den Punkttafeln)
# ===========================================================================================================================
REIHEN = [("s1", None, 0, "I. Tatbestand"),
          ("s1a", 1, 1, "1. Geplante Katalogtat (§ 138 Abs. 1 Nr. 1 bis 8; Vorhaben)"),
          ("s1b", 2, 1, "2. Glaubhafte Kenntnis"),
          ("s1c", 3, 1, "3. Rechtzeitig: Tat oder Erfolg noch abwendbar"),
          ("s1d", 4, 1, "4. Unterlassen der Anzeige (Behörde oder Bedrohter)"),
          ("s1e", 5, 1, "5. Vorsatz (Abs. 3: auch Leichtfertigkeit)"),
          ("s2", "II", 0, "II. Rechtswidrigkeit"),
          ("s3", "III", 0, "III. Schuld"),
          ("s4", "IV", 0, "IV. Straflosigkeit nach § 139 StGB")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Nichtanzeige geplanter Straftaten"), 110, 90, "sch", 46),
           z("§ 138 Abs. 1 StGB (echtes Unterlassungsdelikt)", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, farbe, ebene, text in REIHEN:
    x = (130, 220)[ebene]
    if farbe is not None:
        ch = Image.new("RGBA", (34, 34))
        ImageDraw.Draw(ch).rounded_rectangle((1, 1, 32, 32), 8, fill=PUNKTFARBE[farbe], outline=INK, width=3)
        els_sch.append(El(ch, x - 50, y + 8, c, "pop", 0.0, None, name="farbpunkt"))
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 80, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s2", "Prüfschema › II. Rechtswidrigkeit"),
       ("s3", "Prüfschema › III. Schuld"), ("s4", "Prüfschema › IV. Straflosigkeit, § 139 StGB")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei einer geplanten Katalogtat", 0)], [("schützt ", 0), ("Freundschaft nicht", "a"), (".", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "Freundschaft")}),
    *markertext([[("Wer glaubhaft davon erfährt, muss", 0)], [("rechtzeitig", "b"), (" die Polizei oder den", 0)],
                 [("Bedrohten warnen oder die Tat", 0)], [("anders abwenden", "c"), (".", 0)]],
                750, 480, 44, "mk2", {"b": beim("mk2", "rechtzeitig"), "c": beim("mk2", "anders")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
