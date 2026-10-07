"""Folge 224 · Zeugnisverweigerungsrecht § 52 StPO: Aussage gegen den Partner? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Wohnung (Verlobung, Vorwurf, Anzeigen gesehen), B Polizei (Belehrung, Aussage),
C Ermittlungsrichter (Aussage nach Belehrung), D Hauptverhandlung (Belehrung, Zeugnisverweigerung), E Wohngemeinschaft
(Mitbewohner, Laptop, Ladung), F drei Fragen, G Sachverhalt, H Grundsatz § 48, I § 52 Abs. 1 (Wortlaut), J Verlobte und
nicht erfasste Personen, K Belehrung § 52 Abs. 3 (Wortlaut), L § 252 (Wortlaut, GSSt 1/16), M § 53, N § 55 (Wortlaut),
O/P Lösung, Q Klausurtipp (Lexi), R Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Wohnungstür (Herr Ladewig kommt heim), Briefumschlag (Ladung), Freesound CC0.
Hilfsfunktionen glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 221 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlautkarten wörtlich nach gesetze-im-internet.de
(Abruf 07.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_224/"

_run0 = bausteine._sp.run


def _run_c(args, **k):
    """Sprechblasen müssen im Stil C gelingen (kein stiller Rückfall auf Stil E)."""
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
ROSE = (242, 167, 184, 255)
HOLZ = (214, 160, 110, 255)
GRAU = (225, 225, 230, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobil: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein für mobile Lesbarkeit: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, _ in zeilen:
        glyphen(t)
        assert F(s, g).getlength(t) <= w - 30, f"Blockzeile zu breit: {t}"
    return block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                 randbreite=5, anim=k.pop("anim", "rise"), d=k.pop("d", 0.0), bis=k.pop("bis", None), zeilen=zeilen)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 07.10.2026) in einer hellen Karte, Fundstelle
    darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 22, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_224/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def auf_tafel(e):
    """Requisit bewusst auf der Tafel (Bildzeile), von rechts_frei ausgenommen."""
    e.name = "tafel-" + (e.name or "")
    return e


def hart(e):
    e.anim = "cut"
    return e


def fund(text, x, y, cue, rechts=1170):
    return z(text, x, y, cue, size=26, farbe=TEXT, rechts=rechts)


def geht(e, s0, s1, dx, dy=0):
    """Bewegung: Element startet um (dx, dy) versetzt und kommt zwischen s0 und s1 an seiner Position an."""
    e.weg = (s0, s1, dx, dy)
    return e


# --- Eigene Hilfsfunktion (wie Folge 171/221): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
import wave as _wave
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


def hand(name, cx, unten, hoehe, seite):
    """Position der Hand (äußerster Pixel links/rechts im mittleren Körperband) für ein Requisit."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    h = a.shape[0]
    band = a[int(h * 0.30):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    x = xs.min() if seite < 0 else xs.max()
    y = int(np.median(ys[xs == x])) + int(h * 0.30)
    return e.x + x, e.y + y


def figur_mit(name, cx, unten, hoehe, folge, schild, fill, schild_cue=None, d=0.0):
    """Figur mit Mimikwechseln: folge = [(Ansicht, ab-Cue), …]; Namensschild ab dem ersten Auftritt durchgehend."""
    els = []
    for i, (ans, c) in enumerate(folge):
        bis = folge[i + 1][1] if i + 1 < len(folge) else None
        els.append(peep_voll(ans, cx, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=bis))
    els.append(namensschild(schild, cx, unten, schild_cue or folge[0][1], fill, d=d + 0.1))
    return els


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2


# A Wohnung: Verlobung und Vorwurf -----------------------------------------------------------------------------------------
STX, WEX = 470, 1320
TI = (700, BODEN - 190, 400, 188)       # Tisch
folie([(NULL, "Fall · Frau Wehner und Herr Störmer"), (beim("fall", "verlobt"), "Fall · Verlobt seit dem Frühjahr"),
       ("hochzeit", "Fall · Hochzeit im Sommer"), ("vorwurf", "Fall · Ermittlungen gegen Herrn Störmer"),
       (beim("vorwurf", "Konzertkarten"), "Fall · Vorwurf: Konzertkarten, die es nie gab"),
       ("gesehen", "Fall · Frau Wehner hat es gesehen")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    pl("In der Wohnung von Herrn Störmer", 70, 40, NULL, fill=GELB, size=40, anim="cut"),
    hart(karte(*TI, NULL, fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "device-laptop", 900, BODEN - 190, 190, NULL, fuell=WEISS, anim="cut"),
    peep_voll("ST_froh_r", STX, BODEN, FH, NULL, anim="cut", bis="vorwurf"),
    peep_voll("ST_denkt_r", STX, BODEN, FH, "vorwurf", anim="cut"),
    namensschild("Herr Störmer", STX, BODEN, NULL, GELB, anim="cut"),
    peep_voll("WE_froh", WEX, BODEN, FH, NULL, anim="cut", bis="vorwurf"),
    peep_voll("WE_sorge", WEX, BODEN, FH, "vorwurf", anim="cut", bis="gesehen"),
    peep_voll("WE_denkt", WEX, BODEN, FH, "gesehen", anim="cut"),
    namensschild("Frau Wehner", WEX, BODEN, NULL, GELB, anim="cut"),
    ficon("tabler", "heart", 900, 300, 100, beim("fall", "verlobt"), fuell=ROSE, bis="vorwurf"),
    pl("verlobt seit dem Frühjahr", 900, 330, beim("fall", "verlobt"), fill=WEISS, size=30, anker="m", bis="vorwurf"),
    ficon("tabler", "calendar-heart", 1680, 250, 100, "hochzeit", fuell=ROSE, bis="gesehen"),
    pl("Hochzeit im Sommer", 1680, 280, "hochzeit", fill=WEISS, size=30, anker="m", bis="gesehen"),
    ficon("tabler", "ticket", 840, 300, 100, beim("vorwurf", "Konzertkarten"), fuell=GELB),
    ficon("tabler", "ticket", 960, 300, 100, beim("vorwurf", "Konzertkarten"), fuell=GELB, d=0.15),
    pl("Konzertkarten, die es nie gab", 900, 330, beim("vorwurf", "nie"), fill=ROTHELL, size=30, anker="m"),
    nein(1150, 355, beim("vorwurf", "nie"), gr=18),
    pl("Ermittlungen gegen ihn", 900, 410, beim("vorwurf", "ermittelt"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "eye", 1680, 250, 100, "gesehen", fuell=WEISS, anim="cut"),
    pl("Sie sah ihn die Anzeigen schreiben.", 1840, 280, beim("gesehen", "Anzeigen"), fill=GELB, size=28, anker="r"),
])

# B Polizei -------------------------------------------------------------------------------------------------------------------
PZX = 600
SCH = (380, BODEN - 200, 520, 198)
folie([("pol", "Fall · Vernehmung bei der Polizei"), (beim("pol", "belehrt"), "Fall · Belehrung"),
       ("aus1", "Fall · Sie sagt trotzdem aus")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "pol", breite=7, farbe=INK)),
    pl("Polizei: Zeugenvernehmung", 70, 40, "pol", fill=GELB, size=40, anim="cut"),
    peep_voll("PZ_ruhig_r", PZX, BODEN, FH, "pol", anim="cut", bis="p1"),
    *redet("PZ_redet_r", PZX, BODEN, FH, "p1", "aus1"),
    peep_voll("PZ_ruhig_r", PZX, BODEN, FH, "aus1", anim="cut"),
    hart(karte(*SCH, "pol", fill=GRAU, rund=10, schatten=6)),
    ficon("tabler", "notebook", 760, BODEN - 200, 90, "pol", fuell=WEISS, anim="cut"),
    namensschild("Polizist", PZX, BODEN, "pol", BLAU, anim="cut"),
    peep_voll("WE_ruhig", WEX, BODEN, FH, "pol", anim="cut", bis="p1"),
    peep_voll("WE_denkt", WEX, BODEN, FH, "p1", anim="cut", bis="aus1"),
    peep_voll("WE_ernst", WEX, BODEN, FH, "aus1", anim="cut"),
    namensschild("Frau Wehner", WEX, BODEN, "pol", GELB, anim="cut"),
    pl("Zeugin", WEX, 330, "pol", fill=WEISS, size=28, anker="m", bis="p1"),
    ok(1660, 382, beim("pol", "belehrt"), gr=16),
    pl("Belehrung", 1700, 360, beim("pol", "belehrt"), fill=GRUENHELL, size=28),
    blase("sprech", 760, 190, "p1", 860, 210, inhalt=["Gegen Ihren Verlobten müssen", "Sie nicht aussagen."], textsize=32,
          figur=("PZ_redet_r", PZX, BODEN, FH), bis="aus1"),
    ficon("tabler", "file-text", 1000, 330, 100, "aus1", fuell=WEISS),
    pl("Sie sagt trotzdem aus.", 1000, 360, "aus1", fill=GELB, size=30, anker="m"),
])

# C Ermittlungsrichter ------------------------------------------------------------------------------------------------------
EJX = 600
folie([("er", "Fall · Vor dem Ermittlungsrichter"), (beim("er", "Belehrung"), "Fall · Wieder nach Belehrung")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "er", breite=7, farbe=INK)),
    pl("Beim Ermittlungsrichter", 70, 40, "er", fill=GELB, size=40, anim="cut"),
    peep_voll("EJ_ruhig_r", EJX, BODEN, FH, "er", anim="cut", bis=beim("er", "Belehrung")),
    peep_voll("EJ_ernst_r", EJX, BODEN, FH, beim("er", "Belehrung"), anim="cut"),
    hart(karte(*SCH, "er", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "gavel", 760, BODEN - 200, 100, "er", fuell=HOLZ, anim="cut"),
    namensschild("Ermittlungsrichter", EJX, BODEN, "er", BLAU, anim="cut"),
    peep_voll("WE_ernst", WEX, BODEN, FH, "er", anim="cut"),
    namensschild("Frau Wehner", WEX, BODEN, "er", GELB, anim="cut"),
    ficon("tabler", "file-text", 1000, 330, 100, beim("er", "wiederholt"), fuell=WEISS),
    pl("wiederholt alles", 1000, 360, beim("er", "wiederholt"), fill=GELB, size=30, anker="m"),
    ok(1000 - 160, 462, beim("er", "Belehrung"), gr=16),
    pl("wieder nach Belehrung", 1000, 440, beim("er", "Belehrung"), fill=GRUENHELL, size=28, anker="m"),
])

# D Hauptverhandlung gegen Herrn Störmer ---------------------------------------------------------------------------------------
RIX, WHX, SAX = 420, 1080, 1620
BANK = (RIX - 270, BODEN - 250, 540, 248)
folie([("hv", "Fall · Hauptverhandlung gegen Herrn Störmer"), ("r1", "Fall · Belehrung durch die Richterin"),
       ("w1", "Fall · Sie verweigert das Zeugnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "hv", breite=7, farbe=INK)),
    pl("Hauptverhandlung", 70, 40, "hv", fill=GELB, size=40, anim="cut"),
    peep_voll("RI_ruhig_r", RIX, BODEN, FH, "hv", anim="cut", bis="r1"),
    *redet("RI_redet_r", RIX, BODEN, FH, "r1", "w1"),
    peep_voll("RI_ruhig_r", RIX, BODEN, FH, "w1", anim="cut"),
    hart(karte(*BANK, "hv", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "gavel", RIX + 150, BODEN - 250, 100, "hv", fuell=HOLZ, anim="cut"),
    namensschild("Richterin", RIX, BODEN, "hv", BLAU, anim="cut"),
    peep_voll("WE_sorge", WHX, BODEN, FH, "hv", anim="cut", bis="w1"),
    *redet("WE_redet", WHX, BODEN, FH, "w1", "wg"),
    namensschild("Frau Wehner", WHX, BODEN, "hv", GELB, anim="cut"),
    pl("Zeugin", WHX, 330, "hv", fill=WEISS, size=28, anker="m", bis="r1"),
    peep_voll("ST_sorge", SAX, BODEN, FH, "hv", anim="cut", bis="w1"),
    peep_voll("ST_ruhig", SAX, BODEN, FH, "w1", anim="cut"),
    namensschild("Herr Störmer", SAX, BODEN, "hv", GELB, anim="cut"),
    pl("Angeklagter", SAX, 330, beim("hv", "Herrn"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 900, 200, "r1", 820, 205, inhalt=["Frau Wehner, als Verlobte des Angeklagten",
                                                    "dürfen Sie das Zeugnis verweigern."], textsize=32,
          figur=("RI_redet_r", RIX, BODEN, FH), bis="w1"),
    blase("sprech", 720, 190, "w1", 1260, 200, inhalt=["Dann sage ich nichts", "gegen meinen Verlobten."], textsize=34,
          figur=("WE_redet", WHX, BODEN, FH)),
])

# E Wohngemeinschaft: Mitbewohner ----------------------------------------------------------------------------------------------
TUX, LAX, WGX = 300, 760, 1450
_la = ("LA_ruhig_r", LAX, BODEN, FH)
lhx, lhy = hand(*_la, +1)
folie([("wg", "Fall · Ermittlungen gegen den Mitbewohner"), ("lap", "Fall · Vorwurf: Laptop aus der Firma"),
       (beim("lap", "Frau"), "Fall · Sie sah ihn mit dem Laptop"), ("ladung", "Fall · Ladung als Zeugin"),
       ("w2", "Fall · Aussage gegen den Mitbewohner?")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "wg", breite=7, farbe=INK)),
    pl("In der Wohngemeinschaft", 70, 40, "wg", fill=GELB, size=40, anim="cut"),
    szene(ficon("tabler", "door-enter", TUX, BODEN + 4, 300, "wg", fuell=WEISS, anim="cut", bis=("wg", 1.8)),
          "224tuer*", 1.0, versatz=0.0),
    ficon("tabler", "door", TUX, BODEN + 4, 300, ("wg", 1.8), fuell=WEISS, anim="cut"),
    geht(peep_voll("LA_ruhig_r", LAX, BODEN, FH, "wg", anim="cut", bis="lap"), "wg", ("wg", 1.6), -280),
    peep_voll("LA_denkt_r", LAX, BODEN, FH, "lap", anim="cut"),
    geht(namensschild("Herr Ladewig", LAX, BODEN, "wg", GELB, anim="cut"), "wg", ("wg", 1.6), -280),
    pl("Mitbewohner", LAX, 330, beim("wg", "Mitbewohner"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "device-laptop", lhx + 30, lhy + 60, 120, beim("lap", "Laptop"), fuell=WEISS),
    pl("Vorwurf: Laptop aus der Firma gestohlen", 960, 200, beim("lap", "gestohlen"), fill=ROTHELL, size=30, anker="m",
       bis="w2"),
    peep_voll("WE_ruhig", WGX, BODEN, FH, "wg", anim="cut", bis=beim("lap", "Frau")),
    peep_voll("WE_denkt", WGX, BODEN, FH, beim("lap", "Frau"), anim="cut", bis="w2"),
    *redet("WE_redet", WGX, BODEN, FH, "w2", "fragen"),
    namensschild("Frau Wehner", WGX, BODEN, "wg", GELB, anim="cut"),
    ficon("tabler", "eye", 1080, 380, 90, beim("lap", "gesehen"), fuell=WEISS, bis="w2"),
    pl("sah ihn den Laptop heimbringen", 1080, 410, beim("lap", "nach"), fill=GELB, size=28, anker="m", bis="w2"),
    szene(ficon("tabler", "mail", 1720, 330, 100, "ladung", fuell=WEISS), "224brief*", 1.0, versatz=0.0),
    pl("Ladung als Zeugin", 1720, 360, beim("ladung", "Zeugin"), fill=GELB, size=28, anker="m"),
    blase("sprech", 700, 190, "w2", 1130, 200, inhalt=["Muss ich jetzt gegen meinen", "Mitbewohner aussagen?"], textsize=34,
          figur=("WE_redet", WGX, BODEN, FH)),
])

# F Drei Fragen ---------------------------------------------------------------------------------------------------------------
KX = (70, 680, 1290)
KW, KY, KH = 560, 150, 690
folie([("fragen", "Fall · Darf sie schweigen?"), ("frage2", "Fall · Was wird aus ihren früheren Aussagen?"),
       ("frage3", "Fall · Und beim Mitbewohner?")], [
    pl("Die Fragen", 70, 40, "fragen", fill=GELB, size=40, anim="cut"),
    *[karte(x, KY, KW, KH, "fragen", fill=WEISS, d=0.15 * i) for i, x in enumerate(KX)],
    pl("gegen den Verlobten", KX[0] + KW // 2, KY + 30, "fragen", fill=ROSE, size=30, anker="m"),
    peep_voll("ST_ruhig_r", KX[0] + KW // 2, KY + 520, 400, "fragen"),
    namensschild("Herr Störmer", KX[0] + KW // 2, KY + 520, "fragen", GELB),
    peep_voll("WE_denkt", KX[1] + KW // 2, KY + 520, 400, "fragen", d=0.15),
    namensschild("Frau Wehner", KX[1] + KW // 2, KY + 520, "fragen", GELB, d=0.15),
    pl("Zeugin", KX[1] + KW // 2, KY + 30, "fragen", fill=WEISS, size=30, anker="m", d=0.15),
    pl("gegen den Mitbewohner", KX[2] + KW // 2, KY + 30, "fragen", fill=WEISS, size=30, anker="m", d=0.3),
    peep_voll("LA_denkt", KX[2] + KW // 2, KY + 520, 400, "fragen", d=0.3),
    namensschild("Herr Ladewig", KX[2] + KW // 2, KY + 520, "fragen", GELB, d=0.3),
    pl("Darf sie schweigen?", KX[0] + KW // 2, KY + 610, beim("fragen", "schweigen"), fill=GELB, size=32, anker="m"),
    pl("Frühere Aussagen?", KX[1] + KW // 2, KY + 610, "frage2", fill=GELB, size=32, anker="m"),
    pl("Und beim Mitbewohner?", KX[2] + KW // 2, KY + 610, "frage3", fill=GELB, size=32, anker="m"),
])

# G Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Frau Wehner ist seit dem Frühjahr mit Herrn Störmer verlobt; im Sommer wollen beide heiraten. Gegen ihn wird "
            "wegen Betrugs ermittelt: Er soll im Internet Konzertkarten verkauft haben, die es nie gab. Frau Wehner hat "
            "gesehen, wie er die Anzeigen schrieb."),
    glyphen("Nach Belehrung über ihr Zeugnisverweigerungsrecht sagt sie bei der Polizei gegen ihn aus, kurz darauf – wieder "
            "nach Belehrung – vor dem Ermittlungsrichter. In der Hauptverhandlung verweigert sie das Zeugnis; einer "
            "Verwertung ihrer früheren Aussagen stimmt sie nicht zu."),
    glyphen("Später soll sie im Verfahren gegen ihren Mitbewohner Herrn Ladewig aussagen. Er soll in seiner Firma einen "
            "Laptop gestohlen haben; sie hat gesehen, wie er ihn nach Hause brachte."),
], "Darf sie schweigen – und was gilt für ihre früheren Aussagen?")

# H Grundsatz: Zeugenpflicht § 48 --------------------------------------------------------------------------------------------
PG = "Grundsatz"
folie([("pflicht", f"{PG} › Zeugen müssen aussagen"), ("p48", f"{PG} › § 48 Abs. 1 S. 2 StPO"),
       ("ausn", f"{PG} › Ausnahme: § 52 StPO")], rechts_frei([
    *tafel("pflicht", "Grundsatz: Zeugenpflicht"),
    z("Zeugen müssen aussagen.", 110, 180, beim("pflicht", "Zeugen"), "ExtraBold", 36),
    *wortlaut(110, 270, 1040, 130, "p48", [
        [("„Sie haben die Pflicht auszusagen, wenn keine im", 0)],
        [("Gesetz zugelassene ", 0), ("Ausnahme", "a"), (" vorliegt.“", 0)],
    ], 30, {"a": beim("p48", "Ausnahme")}, "§ 48 Abs. 1 S. 2 StPO"),
    fb(110, 520, 1040, 130, GELB, "ausn", [("Wichtigste Ausnahme für die Familie:", "ExtraBold", 34, INK),
                                         ("§ 52 StPO", "ExtraBold", 34, INK)]),
    peep_voll("RI_ruhig", X1, BR, FR, "pflicht", bis="ausn"),
    peep_voll("RI_denkt", X1, BR, FR, "ausn", anim="cut"),
    namensschild("Richterin", X1, BR, "pflicht", BLAU, d=0.2),
    peep_voll("WE_ruhig", X2, BR, FR, "pflicht", d=0.2, bis="p48"),
    peep_voll("WE_sorge", X2, BR, FR, "p48", anim="cut", bis="ausn"),
    peep_voll("WE_froh", X2, BR, FR, "ausn", anim="cut"),
    namensschild("Frau Wehner", X2, BR, "pflicht", GELB, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "pflicht", fuell=WEISS, bis="ausn"),
    pl("Aussagepflicht", MB, 160, "pflicht", fill=WEISS, size=28, anker="m", bis="ausn"),
    ficon("tabler", "heart", MB, 380, 100, "ausn", fuell=ROSE, anim="cut"),
    pl("Ausnahme: Familie", MB, 160, "ausn", fill=GELB, size=28, anker="m", anim="cut"),
]))

# I § 52 Abs. 1 StPO (Wortlaut) ----------------------------------------------------------------------------------------------
P52 = "§ 52 Abs. 1 StPO"
folie([("a52", f"{P52} › Wer darf schweigen?"), ("n1", f"{P52} › Nr. 1: Verlobte"), ("n2", f"{P52} › Nr. 2: Ehegatten"),
       ("n2a", f"{P52} › Nr. 2a: Lebenspartner"), ("n3", f"{P52} › Nr. 3: Verwandte, Verschwägerte"),
       ("zweck", f"{P52} › Zweck")], rechts_frei([
    *tafel("a52", "§ 52 StPO: Angehörige"),
    *wortlaut(110, 170, 1040, 440, "a52", [
        [("„Zur Verweigerung des Zeugnisses sind berechtigt", 0)],
        [("1. ", 0), ("der Verlobte des Beschuldigten;", "v")],
        [("2. ", 0), ("der Ehegatte", "e"), (" des Beschuldigten, auch wenn die", 0)],
        [("Ehe nicht mehr besteht;", "e2")],
        [("2a. ", 0), ("der Lebenspartner", "l"), (" des Beschuldigten, auch wenn", 0)],
        [("die Lebenspartnerschaft nicht mehr besteht;", 0)],
        [("3. wer mit dem Beschuldigten in gerader Linie ", 0), ("verwandt", "r")],
        [("oder ", 0), ("verschwägert", "r2"), (", in der Seitenlinie bis zum dritten", 0)],
        [("Grad verwandt oder bis zum zweiten Grad verschwägert", 0)],
        [("ist oder war.“", 0)],
    ], 28, {"v": beim("n1", "Verlobte"), "e": beim("n2", "Ehegatte"), "e2": beim("n2", "nicht"),
            "l": beim("n2a", "Lebenspartner"), "r": beim("n3", "Verwandte"), "r2": beim("n3", "Verschwägerte")},
        "§ 52 Abs. 1 StPO"),
    fb(110, 690, 1040, 130, GRUENHELL, "zweck", [("Zweck: kein Konflikt zwischen Wahrheitspflicht", "ExtraBold", 30, INK),
                                               ("und enger persönlicher Bindung", "ExtraBold", 30, INK)]),
    fund("BGH, Urt. v. 10.2.2021 – 6 StR 326/20, Rn. 22", 150, 830, beim("zweck", "Wahrheitspflicht")),
    peep_voll("WE_ruhig", X1, BR, FR, "a52", bis="n1"),
    peep_voll("WE_froh", X1, BR, FR, "n1", anim="cut", bis="zweck"),
    peep_voll("WE_denkt", X1, BR, FR, "zweck", anim="cut"),
    namensschild("Frau Wehner", X1, BR, "a52", GELB, d=0.2),
    peep_voll("ST_ruhig", X2, BR, FR, "a52", d=0.2, bis="n1"),
    peep_voll("ST_froh", X2, BR, FR, "n1", anim="cut"),
    namensschild("Herr Störmer", X2, BR, "a52", GELB, d=0.3),
    ficon("tabler", "heart", MB, 380, 100, "n1", fuell=ROSE, bis="n3"),
    pl("Nr. 1: Verlobte", MB, 160, "n1", fill=ROSE, size=28, anker="m", bis="n2"),
    pl("Nr. 2: auch nach Scheidung", MB, 160, "n2", fill=WEISS, size=28, anker="m", anim="cut", bis="n2a"),
    pl("Nr. 2a: Lebenspartner", MB, 160, "n2a", fill=WEISS, size=28, anker="m", anim="cut", bis="n3"),
    ficon("tabler", "home", MB, 380, 100, "n3", fuell=GELB, anim="cut", bis="zweck"),
    pl("z. B. Eltern, Kinder, Geschwister", 1850, 160, beim("n3", "Eltern"), fill=GELB, size=28, anker="r", bis="zweck"),
    ficon("tabler", "scale", MB, 380, 110, "zweck", fuell=GRUENHELL, anim="cut"),
    pl("Konflikt vermeiden", MB, 160, "zweck", fill=GRUENHELL, size=28, anker="m", anim="cut"),
]))

# J Verlobte und nicht erfasste Personen ------------------------------------------------------------------------------------
PV = "§ 52 Abs. 1 Nr. 1 StPO"
folie([("verl", f"{PV} › Verlobung: keine Form"), ("heir", f"{PV} › beide wollen wirklich heiraten"),
       ("zusatz", f"{PV} › nur solange die Verlobung besteht"), ("nicht", "§ 52 Abs. 1 StPO › nicht erfasst"),
       ("nicht2", "§ 52 Abs. 1 StPO › Aussagepflicht bleibt")], rechts_frei([
    *tafel("verl", "Verlobte: Was gilt?"),
    ok(140, 200, "verl", gr=16),
    z("keine Form nötig", 175, 180, "verl", "Bold", 32),
    ok(140, 255, "heir", gr=16),
    z("beide wollen wirklich heiraten", 175, 235, "heir", "Bold", 32),
    z("Ob das so ist, beurteilt das Gericht.", 175, 285, beim("heir", "Ob"), size=30),
    fund("BGH, Urt. v. 28.5.2003 – 2 StR 445/02 (BGHSt 48, 294);", 175, 330, beim("heir", "Ob")),
    fund("BGH, Beschl. v. 9.3.2010 – 4 StR 606/09, Rn. 13 f. (BGHSt 55, 65)", 175, 362, beim("heir", "Ob")),
    fb(110, 420, 1040, 130, BLAUHELL, "zusatz", [("Kein Zusatz „auch wenn … nicht mehr besteht“:", "ExtraBold", 30, INK),
                                               ("Recht nur, solange die Verlobung besteht", "ExtraBold", 30, INK)]),
    fund("vgl. § 52 Abs. 1 Nr. 2, 2a StPO", 150, 560, beim("zusatz", "Ehegatten")),
    nein(140, 650, "nicht", gr=18),
    z("nicht in der Liste: Freunde, Mitbewohner,", 175, 630, "nicht", "Bold", 32),
    z("Paare ohne Verlobung", 175, 677, beim("nicht", "Paare"), "Bold", 32),
    fb(110, 740, 1040, 100, ROTHELL, "nicht2", [("Für sie bleibt es bei der Aussagepflicht.", "ExtraBold", 32, INK)]),
    peep_voll("WE_ruhig", X1, BR, FR, "verl", bis="nicht"),
    peep_voll("WE_denkt", X1, BR, FR, "nicht", anim="cut"),
    namensschild("Frau Wehner", X1, BR, "verl", GELB, d=0.2),
    peep_voll("ST_froh", X2, BR, FR, "verl", d=0.2, bis="nicht"),
    namensschild("Herr Störmer", X2, BR, "verl", GELB, d=0.3, bis="nicht"),
    peep_voll("LA_denkt", X2, BR, FR, "nicht", anim="cut"),
    namensschild("Herr Ladewig", X2, BR, "nicht", GELB, anim="cut"),
    ficon("tabler", "heart", MB, 380, 100, "verl", fuell=ROSE, bis="zusatz"),
    pl("formlos", MB, 160, "verl", fill=ROSE, size=28, anker="m", bis="heir"),
    pl("Heiratswille beider", MB, 160, "heir", fill=ROSE, size=28, anker="m", anim="cut", bis="zusatz"),
    ficon("tabler", "calendar-heart", MB, 380, 100, "zusatz", fuell=BLAUHELL, anim="cut", bis="nicht"),
    pl("nur solange verlobt", MB, 160, "zusatz", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="nicht"),
    ficon("tabler", "home", MB, 380, 100, "nicht", fuell=WEISS, anim="cut"),
    pl("Mitbewohner: nicht erfasst", MB, 160, "nicht", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# K Belehrung § 52 Abs. 3 S. 1 (Wortlaut) -----------------------------------------------------------------------------------
PB = "§ 52 Abs. 3 StPO"
folie([("bel", f"{PB} › Belehrung"), ("bel2", f"{PB} › vor jeder Vernehmung"), ("bel3", f"{PB} › auch Polizei, Staatsanwaltschaft"),
       ("fehlt", f"{PB} › Belehrung fehlt: unverwertbar"), ("wider", f"{PB} › später umentscheiden")], rechts_frei([
    *tafel("bel", "§ 52 Abs. 3 StPO: Belehrung"),
    *wortlaut(110, 170, 1040, 170, "bel", [
        [("„Die zur Verweigerung des Zeugnisses berechtigten", 0)],
        [("Personen … sind ", 0), ("vor jeder Vernehmung", "j"), (" über ihr", 0)],
        [("Recht zu belehren.“", 0)],
    ], 30, {"j": beim("bel2", "vor")}, "§ 52 Abs. 3 S. 1 StPO (Auszug)"),
    z("auch bei Polizei und Staatsanwaltschaft", 110, 395, "bel3", "Bold", 32),
    fund("§ 163 Abs. 3 S. 2, § 161a Abs. 1 S. 2 StPO; BGH, GSSt 1/16, Rn. 33", 150, 440, beim("bel3", "Polizei")),
    fb(110, 500, 1040, 130, ROTHELL, "fehlt", [("Belehrung fehlt:", "ExtraBold", 32, INK),
                                             ("Aussage grundsätzlich unverwertbar", "ExtraBold", 32, INK)]),
    fund("BGH, Urt. v. 10.2.2021 – 6 StR 326/20, Rn. 22; BGHSt 48, 294", 150, 640, beim("fehlt", "unverwertbar")),
    z("Wer schon ausgesagt hat, darf sich später", 110, 700, "wider", "Bold", 32),
    z("noch umentscheiden.", 110, 745, beim("wider", "umentscheiden"), "Bold", 32),
    fund("§ 52 Abs. 3 S. 2 StPO; BGHSt 48, 294", 150, 795, beim("wider", "umentscheiden")),
    peep_voll("PZ_ruhig", X1, BR, FR, "bel", bis="fehlt"),
    peep_voll("PZ_ernst", X1, BR, FR, "fehlt", anim="cut"),
    namensschild("Polizist", X1, BR, "bel", BLAU, d=0.2),
    peep_voll("WE_ruhig", X2, BR, FR, "bel", d=0.2, bis="wider"),
    peep_voll("WE_froh", X2, BR, FR, "wider", anim="cut"),
    namensschild("Frau Wehner", X2, BR, "bel", GELB, d=0.3),
    ficon("tabler", "info-circle", MB, 380, 100, "bel", fuell=GRUENHELL, bis="bel3"),
    pl("Belehrung", MB, 160, "bel", fill=GRUENHELL, size=28, anker="m", bis="bel2"),
    pl("vor jeder Vernehmung", MB, 160, "bel2", fill=GELB, size=28, anker="m", anim="cut", bis="bel3"),
    ficon("tabler", "notebook", MB, 380, 90, "bel3", fuell=WEISS, anim="cut", bis="fehlt"),
    pl("auch bei der Polizei", MB, 160, "bel3", fill=WEISS, size=28, anker="m", anim="cut", bis="fehlt"),
    ficon("tabler", "circle-x", MB, 380, 100, "fehlt", fuell=ROTHELL, anim="cut", bis="wider"),
    pl("unverwertbar", MB, 160, "fehlt", fill=ROTHELL, size=28, anker="m", anim="cut", bis="wider"),
    ficon("tabler", "repeat", MB, 380, 100, "wider", fuell=GELB, anim="cut"),
    pl("Umentscheiden erlaubt", MB, 160, "wider", fill=GELB, size=28, anker="m", anim="cut"),
]))

# L § 252 StPO (Wortlaut) ----------------------------------------------------------------------------------------------------------
P252 = "§ 252 StPO"
folie([("a252", f"{P252} › frühere Aussage"), ("a252b", f"{P252} › nicht verlesen"), ("rspr", f"{P252} › Verwertungsverbot"),
       ("richter", f"{P252} › Ausnahme: Richter belehrte"), ("einf", f"{P252} › keine weitergehende Belehrung"),
       ("verw221", f"{P252} › siehe Folge 221")], rechts_frei([
    *tafel("a252", "§ 252 StPO: Schweigen erst in der HV"),
    *wortlaut(110, 165, 1040, 205, "a252", [
        [("„Die Aussage eines vor der Hauptverhandlung vernommenen", 0)],
        [("Zeugen, der erst in der Hauptverhandlung von seinem Recht,", 0)],
        [("das Zeugnis zu verweigern, Gebrauch macht, ", 0), ("darf nicht", "v")],
        [("verlesen werden.“", "v2")],
    ], 28, {"v": beim("a252b", "verlesen"), "v2": beim("a252b", "verlesen")}, "§ 252 StPO"),
    nein(140, 460, "rspr", gr=18),
    z("Rspr.: auch sonst nicht verwertbar, etwa nicht", 175, 440, "rspr", "Bold", 30),
    z("durch den Polizisten, der vernommen hat", 175, 482, beim("rspr", "Polizisten"), "Bold", 30),
    fund("BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, Rn. 32 (BGHSt 61, 221)", 175, 524, beim("rspr", "Polizisten")),
    fb(110, 575, 1040, 130, GELB, "richter", [("Ausnahme: Ein Richter hat vorher belehrt.", "ExtraBold", 30, INK),
                                            ("Dann darf der Richter als Zeuge gehört werden.", "ExtraBold", 30, INK)]),
    z("Weitergehende Belehrung nicht nötig", 110, 720, "einf", "Bold", 30),
    fund("GSSt 1/16, Leitsatz", 700, 726, "einf"),
    fb(110, 775, 1040, 80, BLAUHELL, "verw221", [("Mehr dazu: Folge 221 · Beweisverwertungsverbote", "ExtraBold", 30, INK)]),
    peep_voll("PZ_ruhig", X1, BR, FR, "a252", bis="rspr"),
    peep_voll("PZ_ernst", X1, BR, FR, "rspr", anim="cut"),
    namensschild("Polizist", X1, BR, "a252", BLAU, d=0.2),
    peep_voll("EJ_ruhig", X2, BR, FR, "a252", d=0.2, bis="richter"),
    peep_voll("EJ_denkt", X2, BR, FR, "richter", anim="cut"),
    namensschild("Ermittlungsrichter", X2 - 40, BR, "a252", BLAU, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "a252", fuell=WEISS, bis="rspr"),
    pl("nicht verlesen", MB, 160, beim("a252b", "verlesen"), fill=ROTHELL, size=28, anker="m", bis="rspr"),
    ficon("tabler", "microphone-off", MB, 380, 100, "rspr", fuell=ROTHELL, anim="cut", bis="richter"),
    pl("Polizist: nicht", MB, 160, "rspr", fill=ROTHELL, size=28, anker="m", anim="cut", bis="richter"),
    ficon("tabler", "gavel", MB, 380, 100, "richter", fuell=GELB, anim="cut", bis="verw221"),
    pl("Richter: ja", MB, 160, "richter", fill=GELB, size=28, anker="m", anim="cut", bis="verw221"),
    ficon("tabler", "player-play", MB, 380, 100, "verw221", fuell=BLAUHELL, anim="cut"),
    pl("Folge 221", MB, 160, "verw221", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# M § 53 StPO -----------------------------------------------------------------------------------------------------------------------
P53 = "§ 53 StPO"
folie([("a53", f"{P53} › Berufsgeheimnisträger"), ("a53b", f"{P53} › anvertraut oder bekannt geworden"),
       ("a53c", f"{P53} › entbunden: Aussagepflicht")], rechts_frei([
    *tafel("a53", "§ 53 StPO: Berufsgeheimnisträger"),
    z("schützt Berufsgeheimnisse, nicht die Familie", 110, 180, "a53b", "Bold", 32),
    auf_tafel(ficon("tabler", "building-church", 230, 380, 90, beim("a53b", "Geistlichen"), fuell=GELB)),
    pl("Geistliche", 230, 400, beim("a53b", "Geistlichen"), fill=WEISS, size=28, anker="m"),
    auf_tafel(ficon("tabler", "briefcase", 580, 380, 90, beim("a53b", "Verteidigern"), fuell=BLAU)),
    pl("Verteidiger", 580, 400, beim("a53b", "Verteidigern"), fill=WEISS, size=28, anker="m"),
    auf_tafel(ficon("tabler", "stethoscope", 930, 380, 90, beim("a53b", "Ärzten"), fuell=GRUENHELL)),
    pl("Ärzte", 930, 400, beim("a53b", "Ärzten"), fill=WEISS, size=28, anker="m"),
    z("über das, was ihnen in dieser Eigenschaft", 110, 500, beim("a53b", "für"), "Bold", 30),
    z("anvertraut oder bekannt wurde", 110, 543, beim("a53b", "anvertraut"), "Bold", 30),
    fund("§ 53 Abs. 1 S. 1 Nr. 1–3 StPO", 150, 590, beim("a53b", "anvertraut")),
    fb(110, 660, 1040, 130, GELB, "a53c", [("Von der Schweigepflicht entbunden:", "ExtraBold", 32, INK),
                                         ("Der Arzt muss aussagen.", "ExtraBold", 32, INK)]),
    fund("§ 53 Abs. 2 S. 1 StPO (Nr. 2 bis 3b)", 150, 800, beim("a53c", "aussagen")),
    peep_voll("RI_ruhig", X1, BR, FR, "a53", bis="a53c"),
    peep_voll("RI_denkt", X1, BR, FR, "a53c", anim="cut"),
    namensschild("Richterin", X1, BR, "a53", BLAU, d=0.2),
    peep_voll("WE_ruhig", X2, BR, FR, "a53", d=0.2, bis="a53b"),
    peep_voll("WE_denkt", X2, BR, FR, "a53b", anim="cut"),
    namensschild("Frau Wehner", X2, BR, "a53", GELB, d=0.3),
    pl("§ 53 StPO", MB, 160, "a53", fill=WEISS, size=28, anker="m", bis=beim("a53b", "Berufsgeheimnisse")),
    ficon("tabler", "lock", MB, 380, 90, beim("a53b", "Berufsgeheimnisse"), fuell=BLAUHELL, bis="a53c"),
    pl("Berufsgeheimnis", MB, 160, beim("a53b", "Berufsgeheimnisse"), fill=BLAUHELL, size=28, anker="m", anim="cut", bis="a53c"),
    ficon("tabler", "lock-open", MB, 380, 90, "a53c", fuell=GELB, anim="cut"),
    pl("entbunden: aussagen", MB, 160, "a53c", fill=GELB, size=28, anker="m", anim="cut"),
]))

# N § 55 StPO (Wortlaut) --------------------------------------------------------------------------------------------------------
P55 = "§ 55 StPO"
folie([("a55", f"{P55} › Auskunftsverweigerung"), ("a55b", f"{P55} › Gefahr eigener Verfolgung"),
       ("a55c", f"{P55} › nur einzelne Fragen"), ("a55d", f"{P55} › Belehrung, Abs. 2")], rechts_frei([
    *tafel("a55", "§ 55 StPO: Auskunftsverweigerung"),
    *wortlaut(110, 170, 1040, 245, "a55", [
        [("„Jeder Zeuge kann die ", 0), ("Auskunft auf solche Fragen", "f")],
        [("verweigern", "f2"), (", deren Beantwortung ihm selbst oder einem", 0)],
        [("der in § 52 Abs. 1 bezeichneten Angehörigen die ", 0), ("Gefahr", "g")],
        [("zuziehen würde, wegen einer Straftat oder einer", "g2")],
        [("Ordnungswidrigkeit verfolgt zu werden.“", "g3")],
    ], 28, {"f": beim("a55b", "Auskunft"), "f2": beim("a55b", "Auskunft"), "g": beim("a55b", "Gefahr"),
            "g2": beim("a55b", "Gefahr"), "g3": beim("a55b", "Gefahr")}, "§ 55 Abs. 1 StPO"),
    fb(110, 500, 1040, 130, GELB, "a55c", [("Kein Recht, ganz zu schweigen:", "ExtraBold", 32, INK),
                                         ("grundsätzlich nur einzelne Fragen", "ExtraBold", 32, INK)]),
    fund("BGH, Beschl. v. 21.8.2024 – StB 39/24, Rn. 8, 10", 150, 640, beim("a55c", "einzelnen")),
    ok(140, 725, "a55d", gr=16),
    z("Belehrung auch hier: § 55 Abs. 2 StPO", 175, 705, "a55d", "Bold", 32),
    peep_voll("LA_ruhig", X1, BR, FR, "a55", bis="a55b"),
    peep_voll("LA_sorge", X1, BR, FR, "a55b", anim="cut"),
    namensschild("Herr Ladewig", X1, BR, "a55", GELB, d=0.2),
    peep_voll("WE_ruhig", X2, BR, FR, "a55", d=0.2, bis="a55b"),
    peep_voll("WE_denkt", X2, BR, FR, "a55b", anim="cut"),
    namensschild("Frau Wehner", X2, BR, "a55", GELB, d=0.3),
    ficon("tabler", "help-circle", MB, 380, 100, "a55", fuell=WEISS, bis="a55b"),
    pl("Auskunft", MB, 160, "a55", fill=WEISS, size=28, anker="m", bis="a55b"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "a55b", fuell=ROTHELL, anim="cut", bis="a55c"),
    pl("Gefahr der Verfolgung", MB, 160, "a55b", fill=ROTHELL, size=28, anker="m", anim="cut", bis="a55c"),
    ficon("tabler", "list-check", MB, 380, 100, "a55c", fuell=GELB, anim="cut", bis="a55d"),
    pl("einzelne Fragen", MB, 160, "a55c", fill=GELB, size=28, anker="m", anim="cut", bis="a55d"),
    ficon("tabler", "info-circle", MB, 380, 100, "a55d", fuell=GRUENHELL, anim="cut"),
    pl("Belehrung", MB, 160, "a55d", fill=GRUENHELL, size=28, anker="m", anim="cut"),
]))

# O Lösung: gegen den Verlobten -------------------------------------------------------------------------------------------------
PL = "Lösung"
folie([("l1", f"{PL} › gegen Herrn Störmer"), ("l1a", f"{PL} › verlobt, § 52 Abs. 1 Nr. 1"),
       ("l1b", f"{PL} › Zeugnisverweigerung trotz früherer Aussagen"), ("l1c", f"{PL} › Polizei: nicht verwertbar"),
       ("l1d", f"{PL} › Ermittlungsrichter: darf gehört werden")], rechts_frei([
    *tafel("l1", "Lösung: gegen Herrn Störmer"),
    ok(140, 200, beim("l1a", "verlobt"), gr=16),
    z("Hochzeit geplant: verlobt, § 52 Abs. 1 Nr. 1 StPO", 175, 180, beim("l1a", "verlobt"), "Bold", 30),
    fb(110, 250, 1040, 130, GRUENHELL, "l1b", [("Sie darf das Zeugnis verweigern,", "ExtraBold", 32, INK),
                                             ("auch nach früheren Aussagen.", "ExtraBold", 32, INK)]),
    nein(140, 450, "l1c", gr=18),
    z("Polizei: Aussage nicht verlesen,", 175, 430, "l1c", "Bold", 30),
    z("Polizist darf nicht darüber aussagen", 175, 473, beim("l1c", "Polizist"), "Bold", 30),
    fund("§ 252 StPO; GSSt 1/16, Rn. 32", 175, 516, beim("l1c", "Polizist")),
    ok(140, 600, "l1d", gr=16),
    z("Ermittlungsrichter hat belehrt:", 175, 580, "l1d", "Bold", 30),
    fb(110, 640, 1040, 100, GELB, beim("l1d", "Er"), [("Er darf als Zeuge gehört werden.", "ExtraBold", 34, INK)]),
    fund("BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, Leitsatz", 150, 752, beim("l1d", "Er")),
    peep_voll("WE_ruhig", X1, BR, FR, "l1", bis="l1b"),
    peep_voll("WE_froh", X1, BR, FR, "l1b", anim="cut", bis="l1d"),
    peep_voll("WE_denkt", X1, BR, FR, "l1d", anim="cut"),
    namensschild("Frau Wehner", X1, BR, "l1", GELB, d=0.2),
    peep_voll("ST_ruhig", X2, BR, FR, "l1", d=0.2, bis="l1d"),
    peep_voll("ST_sorge", X2, BR, FR, "l1d", anim="cut"),
    namensschild("Herr Störmer", X2, BR, "l1", GELB, d=0.3),
    ficon("tabler", "heart", MB, 380, 100, "l1a", fuell=ROSE, bis="l1c"),
    pl("verlobt", MB, 160, "l1a", fill=ROSE, size=28, anker="m", bis="l1b"),
    pl("darf schweigen", MB, 160, "l1b", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="l1c"),
    ficon("tabler", "file-off", MB, 380, 100, "l1c", fuell=ROTHELL, anim="cut", bis="l1d"),
    pl("Polizei: gesperrt", MB, 160, "l1c", fill=ROTHELL, size=28, anker="m", anim="cut", bis="l1d"),
    ficon("tabler", "gavel", MB, 380, 100, "l1d", fuell=GELB, anim="cut"),
    pl("Richter: als Zeuge", MB, 160, "l1d", fill=GELB, size=28, anker="m", anim="cut"),
]))

# P Lösung: gegen den Mitbewohner -------------------------------------------------------------------------------------------------
folie([("l2", f"{PL} › gegen Herrn Ladewig"), ("l2a", f"{PL} › Aussagepflicht"), ("l2b", f"{PL} › § 55 für einzelne Fragen"),
       ("l2c", f"{PL} › anders: Verlobter mitbeschuldigt")], rechts_frei([
    *tafel("l2", "Lösung: gegen Herrn Ladewig"),
    nein(140, 200, beim("l2", "kein"), gr=18),
    z("Mitbewohner: kein Angehöriger, kein § 52", 175, 180, beim("l2", "kein"), "Bold", 32),
    fb(110, 250, 1040, 100, ROTHELL, "l2a", [("Sie muss aussagen.", "ExtraBold", 36, INK)]),
    fund("§ 48 Abs. 1 S. 2 StPO", 150, 362, "l2a"),
    z("Nur einzelne Fragen, die sie selbst belasten", 110, 425, "l2b", "Bold", 30),
    z("könnten (z. B. Laptop billig abgekauft):", 110, 468, beim("l2b", "etwa"), "Bold", 30),
    z("Auskunftsverweigerung, § 55 StPO", 110, 511, beim("l2b", "verweigern"), "ExtraBold", 30),
    fb(110, 600, 1040, 130, BLAUHELL, "l2c", [("Anders: Verlobter im selben Verfahren", "ExtraBold", 32, INK),
                                            ("wegen derselben Tat mitbeschuldigt", "ExtraBold", 32, INK)]),
    fund("BGH, Urt. v. 10.2.2021 – 6 StR 326/20, Rn. 18", 150, 742, beim("l2c", "mitbeschuldigt")),
    peep_voll("WE_denkt", X1, BR, FR, "l2", bis="l2b"),
    peep_voll("WE_sorge", X1, BR, FR, "l2b", anim="cut", bis="l2c"),
    peep_voll("WE_denkt", X1, BR, FR, "l2c", anim="cut"),
    namensschild("Frau Wehner", X1, BR, "l2", GELB, d=0.2),
    peep_voll("LA_ruhig", X2, BR, FR, "l2", d=0.2, bis="l2a"),
    peep_voll("LA_sorge", X2, BR, FR, "l2a", anim="cut"),
    namensschild("Herr Ladewig", X2, BR, "l2", GELB, d=0.3),
    ficon("tabler", "home", MB, 380, 100, "l2", fuell=WEISS, bis="l2a"),
    pl("kein Angehöriger", MB, 160, "l2", fill=ROTHELL, size=28, anker="m", bis="l2a"),
    ficon("tabler", "scale", MB, 380, 110, "l2a", fuell=WEISS, anim="cut", bis="l2b"),
    pl("Aussagepflicht", MB, 160, "l2a", fill=ROTHELL, size=28, anker="m", anim="cut", bis="l2b"),
    ficon("tabler", "list-check", MB, 380, 100, "l2b", fuell=GELB, anim="cut", bis="l2c"),
    pl("§ 55: einzelne Fragen", MB, 160, "l2b", fill=GELB, size=28, anker="m", anim="cut", bis="l2c"),
    ficon("tabler", "heart", MB, 380, 100, "l2c", fuell=BLAUHELL, anim="cut"),
    pl("Verlobter mitbeschuldigt?", MB, 160, "l2c", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# Q Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zeuge in drei Schritten"), ("s1", "Klausurtipp · I. Kreis des § 52 StPO?"),
       ("s2", "Klausurtipp · II. Vor jeder Vernehmung belehrt?"), ("s3", "Klausurtipp · III. Erst in der HV: § 252 StPO"),
       ("s4", "Klausurtipp · Sonst: § 53, § 55 StPO")], [
    *tafel("tipp", "Klausurtipp: Zeuge in drei Schritten", h=860, fill=HELL),
    warnung_i(150, 205, "tipp", gr=26),
    z("Prüf in dieser Reihenfolge:", 200, 180, beim("tipp", "Prüf"), "Bold", 36),
    z("I. Gehört er zum Kreis des § 52 StPO?", 130, 280, "s1", "ExtraBold", 34),
    z("II. Vor jeder Vernehmung belehrt?", 130, 380, "s2", "ExtraBold", 34),
    z("III. Schweigt er erst in der Hauptverhandlung:", 130, 480, "s3", "ExtraBold", 34),
    z("§ 252 StPO, Ausnahme für den Richter", 190, 528, beim("s3", "Paragraf"), size=30),
    z("Gehört er nicht dazu:", 130, 640, "s4", "ExtraBold", 34),
    z("§ 53 StPO, § 55 StPO für einzelne Fragen", 190, 688, beim("s4", "Paragraf"), size=30),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "merke"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# R Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("§ 52 StPO schützt nur die ", 0), ("Angehörigen,", "a")], [("die das Gesetz nennt.", 0)]],
                750, 300, 50, "merke", {"a": beim("merke", "Angehörigen")}),
    *markertext([[("Wer erst in der Hauptverhandlung schweigt,", 0)], [("sperrt grundsätzlich ", 0),
                 ("frühere Aussagen.", "b")], [("Nutzbar bleibt nur, was er ", 0), ("nach Belehrung", "c")],
                 [("vor einem ", 0), ("Richter", "d"), (" gesagt hat.", 0)]], 750, 470, 46, "mz",
                {"b": beim("mz", "früheren"), "c": beim("mz", "Belehrung"), "d": beim("mz", "Richter")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
