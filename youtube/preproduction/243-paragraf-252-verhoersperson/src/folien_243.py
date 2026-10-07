"""Folge 243 · § 252 StPO: Die Ehefrau schweigt – Verhörsperson als Zeuge? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Malerbetrieb, B Polizei (Belehrung, belastende Aussage), C Hauptverhandlung (Belehrung,
Zeugnisverweigerung), D Polizeibeamter als Zeuge, Urteil, E Revision, F drei Fragen, G Sachverhalt, H § 252 (Wortlaut),
I Rechtsprechung, J Streitstand, K Ausnahme Richter, L Gestattung, M Äußerungen außerhalb einer Vernehmung, N Lösung,
O/P Revisionsrüge (§ 344 Abs. 2 S. 2 Wortlaut), Q Klausurtipp (Lexi), R Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Freesound CC0, Herkunft ../geraeusche_herkunft.json).
Hilfsfunktionen glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 224/221 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlautkarten wörtlich nach gesetze-im-internet.de
(Abruf 07.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_243/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_243/" in n:
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



# A Malerbetrieb ---------------------------------------------------------------------------------------------------------
HHX, FHX = 470, 1320
TI = (880, BODEN - 170, 300, 168)       # Schreibtisch der Buchhaltung
folie([(NULL, "Fall · Malerbetrieb Hasselbach"), ("buero", "Fall · Sie macht die Buchhaltung"),
       ("vorwurf", "Fall · Ermittlungen wegen Betrugs"),
       (beim("vorwurf", "Kunden"), "Fall · Vorwurf: Arbeiten berechnet, nie gemacht")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    pl("Im Malerbetrieb Hasselbach", 70, 40, NULL, fill=GELB, size=40, anim="cut"),
    ficon("tabler", "bucket-droplet", HHX + 200, BODEN, 110, NULL, fuell=BLAU, anim="cut"),
    peep_voll("HH_froh_r", HHX, BODEN, FH, NULL, anim="cut", bis="vorwurf"),
    peep_voll("HH_denkt_r", HHX, BODEN, FH, "vorwurf", anim="cut"),
    namensschild("Herr Hasselbach", HHX, BODEN, NULL, GELB, anim="cut"),
    peep_voll("FH_ruhig", FHX, BODEN, FH, NULL, anim="cut", bis="buero"),
    peep_voll("FH_froh", FHX, BODEN, FH, "buero", anim="cut", bis="vorwurf"),
    peep_voll("FH_sorge", FHX, BODEN, FH, "vorwurf", anim="cut"),
    namensschild("Frau Hasselbach", FHX, BODEN, NULL, GELB, anim="cut"),
    ficon("tabler", "heart-handshake", 1030, 300, 100, NULL, fuell=ROSE, anim="cut", bis="buero"),
    pl("gemeinsamer Malerbetrieb", 1030, 330, NULL, fill=WEISS, size=30, anker="m", anim="cut", bis="buero"),
    hart(karte(*TI, "buero", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "calculator", 1030, BODEN - 170, 100, "buero", fuell=WEISS),
    pl("Buchhaltung", 1030, 330, "buero", fill=WEISS, size=30, anker="m", bis="vorwurf"),
    pl("Ermittlungen wegen Betrugs", 960, 200, beim("vorwurf", "Betrugs"), fill=ROTHELL, size=30, anker="m"),
    ficon("tabler", "file-invoice", 900, 380, 100, beim("vorwurf", "Arbeiten"), fuell=WEISS),
    ficon("tabler", "file-invoice", 1020, 380, 100, beim("vorwurf", "Arbeiten"), fuell=WEISS, d=0.15),
    pl("Arbeiten berechnet, die nie gemacht wurden", 960, 410, beim("vorwurf", "nie"), fill=GELB, size=28, anker="m"),
    nein(1110, 330, beim("vorwurf", "nie"), gr=18),
])

# B Polizei ----------------------------------------------------------------------------------------------------------------
PBX = 600
SCH = (380, BODEN - 200, 520, 198)
_pbb = ("PB_redet_r", PBX, BODEN, FH)
folie([("pol", "Fall · Zeugenvernehmung bei der Polizei"), (beim("pol", "belehrt"), "Fall · Belehrung"),
       ("aus1", "Fall · Sie belastet ihn schwer")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "pol", breite=7, farbe=INK)),
    pl("Polizei: Zeugenvernehmung", 70, 40, "pol", fill=GELB, size=40, anim="cut"),
    peep_voll("PB_ruhig_r", PBX, BODEN, FH, "pol", anim="cut", bis="p1"),
    *redet("PB_redet_r", PBX, BODEN, FH, "p1", "aus1"),
    peep_voll("PB_denkt_r", PBX, BODEN, FH, "aus1", anim="cut"),
    hart(karte(*SCH, "pol", fill=GRAU, rund=10, schatten=6)),
    ficon("tabler", "notebook", 760, BODEN - 200, 90, "pol", fuell=WEISS, anim="cut", bis="aus1"),
    szene(ficon("tabler", "keyboard", 760, BODEN - 200, 120, "aus1", fuell=WEISS, anim="cut"), "243tastatur*", 1.0),
    namensschild("Polizeibeamter", PBX, BODEN, "pol", BLAU, anim="cut"),
    peep_voll("FH_ruhig", FHX, BODEN, FH, "pol", anim="cut", bis="p1"),
    peep_voll("FH_denkt", FHX, BODEN, FH, "p1", anim="cut", bis="w0"),
    *redet("FH_redet", FHX, BODEN, FH, "w0", "hv"),
    namensschild("Frau Hasselbach", FHX, BODEN, "pol", GELB, anim="cut"),
    pl("Zeugin", FHX, 330, "pol", fill=WEISS, size=28, anker="m", bis="p1"),
    ok(1660, 382, beim("pol", "belehrt"), gr=16),
    pl("Belehrung", 1700, 360, beim("pol", "belehrt"), fill=GRUENHELL, size=28),
    blase("sprech", 760, 190, "p1", 860, 210, inhalt=["Gegen Ihren Ehemann müssen", "Sie nicht aussagen."], textsize=32,
          figur=_pbb, bis="aus1"),
    pl("Sie belastet ihn schwer.", 960, 410, "aus1", fill=ROTHELL, size=30, anker="m"),
    blase("sprech", 760, 190, "w0", 1050, 200, inhalt=["Die falschen Rechnungen hat", "er selbst geschrieben."], textsize=32,
          figur=("FH_redet", FHX, BODEN, FH)),
])

# C Hauptverhandlung: Belehrung und Zeugnisverweigerung -------------------------------------------------------------------
VRX, MIX, SAX = 420, 1080, 1620
BANK = (VRX - 270, BODEN - 250, 540, 248)
folie([("hv", "Fall · Hauptverhandlung gegen Herrn Hasselbach"), ("r1", "Fall · Belehrung durch den Vorsitzenden"),
       ("w1", "Fall · Sie verweigert das Zeugnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "hv", breite=7, farbe=INK)),
    pl("Hauptverhandlung", 70, 40, "hv", fill=GELB, size=40, anim="cut"),
    peep_voll("VR_ruhig_r", VRX, BODEN, FH, "hv", anim="cut", bis="r1"),
    *redet("VR_redet_r", VRX, BODEN, FH, "r1", "w1"),
    peep_voll("VR_ruhig_r", VRX, BODEN, FH, "w1", anim="cut"),
    hart(karte(*BANK, "hv", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "scale", VRX + 150, BODEN - 250, 100, "hv", fuell=WEISS, anim="cut"),
    namensschild("Vorsitzender", VRX, BODEN, "hv", BLAU, anim="cut"),
    peep_voll("FH_sorge", MIX, BODEN, FH, "hv", anim="cut", bis="w1"),
    *redet("FH_redet", MIX, BODEN, FH, "w1", "verh"),
    namensschild("Frau Hasselbach", MIX, BODEN, "hv", GELB, anim="cut"),
    pl("Zeugin", MIX, 330, "hv", fill=WEISS, size=28, anker="m", bis="r1"),
    peep_voll("HH_sorge", SAX, BODEN, FH, "hv", anim="cut", bis="w1"),
    peep_voll("HH_ruhig", SAX, BODEN, FH, "w1", anim="cut"),
    namensschild("Herr Hasselbach", SAX, BODEN, "hv", GELB, anim="cut"),
    pl("Angeklagter", SAX, 330, beim("hv", "Hauptverhandlung"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 900, 200, "r1", 820, 205, inhalt=["Als Ehefrau des Angeklagten dürfen", "Sie das Zeugnis verweigern."],
          textsize=32, figur=("VR_redet_r", VRX, BODEN, FH), bis="w1"),
    blase("sprech", 700, 190, "w1", 1260, 200, inhalt=["Gegen meinen Mann", "sage ich nicht aus."], textsize=34,
          figur=("FH_redet", MIX, BODEN, FH)),
])

# D Polizeibeamter als Zeuge, Urteil -------------------------------------------------------------------------------------
folie([("verh", "Fall · Der Polizeibeamte als Zeuge"), (beim("p2", "Sie"), "Fall · Bericht über ihre frühere Aussage"),
       ("urteil", "Fall · Verurteilung")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "verh", breite=7, farbe=INK)),
    pl("Hauptverhandlung: Zeuge Polizeibeamter", 70, 40, "verh", fill=GELB, size=40, anim="cut"),
    peep_voll("VR_ruhig_r", VRX, BODEN, FH, "verh", anim="cut", bis="urteil"),
    peep_voll("VR_ernst_r", VRX, BODEN, FH, "urteil", anim="cut"),
    hart(karte(*BANK, "verh", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "scale", VRX + 150, BODEN - 250, 100, "verh", fuell=WEISS, anim="cut"),
    namensschild("Vorsitzender", VRX, BODEN, "verh", BLAU, anim="cut"),
    peep_voll("PB_ruhig", MIX, BODEN, FH, "verh", anim="cut", bis="p2"),
    *redet("PB_redet", MIX, BODEN, FH, "p2", "urteil"),
    peep_voll("PB_ruhig", MIX, BODEN, FH, "urteil", anim="cut"),
    namensschild("Polizeibeamter", MIX, BODEN, "verh", BLAU, anim="cut"),
    pl("Zeuge", MIX, 330, beim("verh", "Zeugen"), fill=WEISS, size=28, anker="m", bis="p2"),
    peep_voll("HH_ruhig", SAX, BODEN, FH, "verh", anim="cut", bis="p2"),
    peep_voll("HH_sorge", SAX, BODEN, FH, "p2", anim="cut", bis="urteil"),
    peep_voll("HH_muede", SAX, BODEN, FH, "urteil", anim="cut"),
    namensschild("Herr Hasselbach", SAX, BODEN, "verh", GELB, anim="cut"),
    pl("Angeklagter", SAX, 330, "verh", fill=WEISS, size=28, anker="m", anim="cut", bis="urteil"),
    pl("verurteilt", SAX, 330, beim("urteil", "verurteilt"), fill=ROTHELL, size=28, anker="m", anim="cut"),
    blase("sprech", 880, 200, "p2", 780, 205, inhalt=["Sie sagte, die falschen Rechnungen", "habe er selbst geschrieben."],
          textsize=32, figur=("PB_redet", MIX, BODEN, FH), bis="urteil"),
])

# E Revision ----------------------------------------------------------------------------------------------------------------
VTX = 640
_vt = ("VT_ruhig_r", VTX, BODEN, FH)
vhx, vhy = hand(*_vt, +1)
folie([("rev", "Fall · Revision")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "rev", breite=7, farbe=INK)),
    pl("Kanzlei der Verteidigerin", 70, 40, "rev", fill=GELB, size=40, anim="cut"),
    peep_voll("VT_ruhig_r", VTX, BODEN, FH, "rev", anim="cut", bis=beim("rev", "Revision")),
    peep_voll("VT_ernst_r", VTX, BODEN, FH, beim("rev", "Revision"), anim="cut"),
    namensschild("Verteidigerin", VTX, BODEN, "rev", BLAU, anim="cut"),
    peep_voll("HH_denkt", FHX, BODEN, FH, "rev", anim="cut"),
    namensschild("Herr Hasselbach", FHX, BODEN, "rev", GELB, anim="cut"),
    szene(ficon("tabler", "file-text", vhx + 40, vhy + 70, 110, beim("rev", "Revision"), fuell=WEISS), "243papier*", 1.0),
    pl("Revision", 980, 330, beim("rev", "Revision"), fill=GELB, size=32, anker="m"),
])

# F Drei Fragen --------------------------------------------------------------------------------------------------------------
KX = (70, 680, 1290)
KW, KY, KH = 560, 150, 690
folie([("fragen", "Fall · Durfte der Polizeibeamte berichten?"), ("frage2", "Fall · Was wäre bei einem Richter anders?"),
       ("frage3", "Fall · Wie rügt man das?")], [
    pl("Die Fragen", 70, 40, "fragen", fill=GELB, size=40, anim="cut"),
    *[karte(x, KY, KW, KH, "fragen", fill=WEISS, d=0.15 * i) for i, x in enumerate(KX)],
    pl("Verhörsperson", KX[0] + KW // 2, KY + 30, "fragen", fill=BLAUHELL, size=30, anker="m"),
    peep_voll("PB_denkt_r", KX[0] + KW // 2, KY + 520, 400, "fragen"),
    namensschild("Polizeibeamter", KX[0] + KW // 2, KY + 520, "fragen", BLAU),
    pl("Richter", KX[1] + KW // 2, KY + 30, "fragen", fill=WEISS, size=30, anker="m", d=0.15),
    peep_voll("EJ_ruhig", KX[1] + KW // 2, KY + 520, 400, "fragen", d=0.15),
    namensschild("Ermittlungsrichterin", KX[1] + KW // 2, KY + 520, "fragen", BLAU, d=0.15),
    pl("Revision", KX[2] + KW // 2, KY + 30, "fragen", fill=WEISS, size=30, anker="m", d=0.3),
    peep_voll("VT_denkt", KX[2] + KW // 2, KY + 520, 400, "fragen", d=0.3),
    namensschild("Verteidigerin", KX[2] + KW // 2, KY + 520, "fragen", BLAU, d=0.3),
    pl("Durfte er berichten?", KX[0] + KW // 2, KY + 610, beim("fragen", "berichten"), fill=GELB, size=32, anker="m"),
    pl("Beim Richter anders?", KX[1] + KW // 2, KY + 610, "frage2", fill=GELB, size=32, anker="m"),
    pl("Wie rügt man das?", KX[2] + KW // 2, KY + 610, beim("frage3", "rügt"), fill=GELB, size=32, anker="m"),
])

# G Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr und Frau Hasselbach sind verheiratet und führen zusammen einen Malerbetrieb; sie macht die Buchhaltung. "
            "Gegen ihn wird wegen Betrugs ermittelt: Er soll Kunden Arbeiten berechnet haben, die nie gemacht wurden."),
    glyphen("Ein Polizeibeamter vernimmt Frau Hasselbach als Zeugin und belehrt sie über ihr Zeugnisverweigerungsrecht. "
            "Sie belastet ihren Mann schwer: Die falschen Rechnungen habe er selbst geschrieben."),
    glyphen("In der Hauptverhandlung verweigert sie nach Belehrung das Zeugnis; einer Verwertung ihrer früheren Aussage "
            "stimmt sie nicht zu. Das Gericht vernimmt den Polizeibeamten über ihre Aussage und verurteilt Herrn Hasselbach. "
            "Die Verteidigerin legt Revision ein."),
], "Durfte der Polizeibeamte über ihre Aussage berichten?")

# H § 252 StPO (Wortlaut) ----------------------------------------------------------------------------------------------------
P252 = "§ 252 StPO"
folie([("a252", "§ 52 Abs. 1 Nr. 2 StPO › Ehefrau darf schweigen"), ("a252b", f"{P252} › frühere Aussage"),
       (beim("wl", "verlesen"), f"{P252} › nicht verlesen"), ("wort", f"{P252} › Verhörsperson nicht erwähnt"),
       ("verw", f"{P252} › Grundlagen: Folgen 224, 221")], rechts_frei([
    *tafel("a252", "§ 252 StPO: Was sagt der Wortlaut?"),
    z("Ehefrau: Zeugnisverweigerungsrecht", 110, 180, beim("a252", "Ehefrau"), "Bold", 32),
    fund("§ 52 Abs. 1 Nr. 2 StPO", 150, 225, beim("a252", "Paragraf")),
    *wortlaut(110, 290, 1040, 205, "a252b", [
        [("„Die Aussage eines vor der Hauptverhandlung vernommenen", 0)],
        [("Zeugen, der ", 0), ("erst in der Hauptverhandlung", "h"), (" von seinem Recht,", 0)],
        [("das Zeugnis zu verweigern, Gebrauch macht, ", 0), ("darf nicht", "v")],
        [("verlesen werden.“", "v2")],
    ], 28, {"h": beim("wl", "erst"), "v": beim("wl", "verlesen"), "v2": beim("wl", "verlesen")}, "§ 252 StPO"),
    nein(140, 600, "wort", gr=18),
    z("Polizeibeamter als Zeuge? Steht dort nicht.", 175, 580, "wort", "Bold", 32),
    fb(110, 680, 1040, 130, BLAUHELL, "verw", [("Grundlagen: Folge 224 · § 52 StPO", "ExtraBold", 30, INK),
                                             ("und Folge 221 · Beweisverwertungsverbote", "ExtraBold", 30, INK)]),
    peep_voll("FH_ruhig", X1, BR, FR, "a252", bis="wort"),
    peep_voll("FH_denkt", X1, BR, FR, "wort", anim="cut"),
    namensschild("Frau Hasselbach", X1, BR, "a252", GELB, d=0.2),
    peep_voll("PB_ruhig", X2, BR, FR, "a252", d=0.2, bis="wort"),
    peep_voll("PB_denkt", X2, BR, FR, "wort", anim="cut"),
    namensschild("Polizeibeamter", X2, BR, "a252", BLAU, d=0.3),
    ficon("tabler", "heart-handshake", MB, 380, 100, "a252", fuell=ROSE, bis="a252b"),
    pl("Ehefrau", MB, 160, "a252", fill=ROSE, size=28, anker="m", bis="a252b"),
    ficon("tabler", "file-text", MB, 380, 100, "a252b", fuell=WEISS, anim="cut", bis="wort"),
    pl("frühere Aussage", MB, 160, "a252b", fill=WEISS, size=28, anker="m", anim="cut", bis=beim("wl", "verlesen")),
    pl("nicht verlesen", MB, 160, beim("wl", "verlesen"), fill=ROTHELL, size=28, anker="m", anim="cut", bis="wort"),
    ficon("tabler", "help-circle", MB, 380, 100, "wort", fuell=GELB, anim="cut", bis="verw"),
    pl("Verhörsperson?", MB, 160, "wort", fill=GELB, size=28, anker="m", anim="cut", bis="verw"),
    ficon("tabler", "player-play", MB, 380, 100, "verw", fuell=BLAUHELL, anim="cut"),
    pl("Folgen 224, 221", MB, 160, "verw", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# I Rechtsprechung: Verwertungsverbot ----------------------------------------------------------------------------------------
PR = "Rspr. zu § 252 StPO"
folie([("rspr", f"{PR} › Verwertungsverbot"), ("rspr2", f"{PR} › auch nicht auf anderem Weg"),
       ("verhb", f"{PR} › Verhörsperson gesperrt"), ("zweck", f"{PR} › Zweck")], rechts_frei([
    *tafel("rspr", "Rechtsprechung: Verwertungsverbot"),
    z("§ 252 StPO: Verlesungs- und Verwertungsverbot", 110, 180, beim("rspr", "Verwertungsverbot"), "Bold", 32),
    fund("BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, Rn. 32 (BGHSt 61, 221)", 150, 227, beim("rspr", "Verwertungsverbot")),
    z("frühere Aussage grundsätzlich auch nicht", 110, 300, "rspr2", "Bold", 32),
    z("auf anderem Weg einführen", 110, 345, beim("rspr2", "anderem"), "Bold", 32),
    nein(140, 440, "verhb", gr=18),
    z("auch nicht durch die Verhörsperson,", 175, 420, "verhb", "ExtraBold", 32),
    z("etwa den Polizeibeamten", 175, 465, beim("verhb", "Polizeibeamten"), "ExtraBold", 32),
    fund("BGH, Urt. v. 30.6.2020 – 3 StR 377/18, Rn. 12", 175, 512, beim("verhb", "Polizeibeamten")),
    fb(110, 590, 1040, 130, GRUENHELL, "zweck", [("Zweck: Die Zeugin entscheidet bis zur HV,", "ExtraBold", 30, INK),
                                               ("ob ihre frühere Aussage verwertet wird", "ExtraBold", 30, INK)]),
    fund("BGH, Beschl. v. 18.10.2023 – 1 StR 222/23, Rn. 7", 150, 732, beim("zweck", "voreilige")),
    peep_voll("PB_ruhig", X1, BR, FR, "rspr", bis="verhb"),
    peep_voll("PB_ernst", X1, BR, FR, "verhb", anim="cut"),
    namensschild("Polizeibeamter", X1, BR, "rspr", BLAU, d=0.2),
    peep_voll("FH_ruhig", X2, BR, FR, "rspr", d=0.2, bis="zweck"),
    peep_voll("FH_fest", X2, BR, FR, "zweck", anim="cut"),
    namensschild("Frau Hasselbach", X2, BR, "rspr", GELB, d=0.3),
    ficon("tabler", "file-off", MB, 380, 100, "rspr", fuell=ROTHELL, bis="verhb"),
    pl("Verwertungsverbot", MB, 160, beim("rspr", "Verwertungsverbot"), fill=ROTHELL, size=28, anker="m", bis="verhb"),
    ficon("tabler", "microphone-off", MB, 380, 100, "verhb", fuell=ROTHELL, anim="cut", bis="zweck"),
    pl("Polizeibeamter: nein", MB, 160, beim("verhb", "Polizeibeamten"), fill=ROTHELL, size=28, anker="m", bis="zweck"),
    ficon("tabler", "scale", MB, 380, 110, "zweck", fuell=GRUENHELL, anim="cut"),
    pl("Zeugin entscheidet", MB, 160, "zweck", fill=GRUENHELL, size=28, anker="m", anim="cut"),
]))

# J Streitstand ---------------------------------------------------------------------------------------------------------------
PS_ = "Streit: Verhörsperson als Zeuge?"
folie([("ga1", f"{PS_} › Wortlaut-Ansicht"), ("ga2", f"{PS_} › umfassendes Verbot"),
       ("gsst", f"{PS_} › Großer Senat: offen"), ("praxis", f"{PS_} › BGH: Sperre bleibt")], rechts_frei([
    *tafel("ga1", "Streit: Verhörsperson als Zeuge?"),
    z("1. Wortlaut: nur Verlesen verboten,", 110, 180, "ga1", "ExtraBold", 32),
    z("jede Vernehmungsperson, die belehrt hat, darf aussagen", 110, 225, beim("ga1", "jede"), "Bold", 30),
    fund("Teile der Literatur; vgl. GSSt 1/16, Rn. 29, 36", 150, 270, beim("ga1", "jede")),
    z("2. Umfassend: alles gesperrt, sogar der Richter", 110, 340, "ga2", "ExtraBold", 32),
    fund("Teile der Literatur; vgl. GSSt 1/16, Rn. 36", 150, 387, beim("ga2", "sperren")),
    fb(110, 450, 1040, 130, BLAUHELL, "gsst", [("Großer Senat: Frage zur Polizei offen,", "ExtraBold", 30, INK),
                                             ("Gesetzgeber aufgerufen", "ExtraBold", 30, INK)]),
    fund("GSSt 1/16, Rn. 26, 64", 150, 592, beim("gsst", "Gesetzgeber")),
    ok(140, 680, "praxis", gr=16),
    z("3. BGH: Sperre für die Verhörsperson bleibt", 175, 660, "praxis", "ExtraBold", 32),
    fund("BGH 3 StR 377/18, Rn. 12 (2020); 1 StR 222/23, Rn. 7 (2023)", 175, 707, beim("praxis", "Sperre")),
    peep_voll("PB_ruhig", X1, BR, FR, "ga1", bis="ga2"),
    peep_voll("PB_denkt", X1, BR, FR, "ga2", anim="cut", bis="praxis"),
    peep_voll("PB_ernst", X1, BR, FR, "praxis", anim="cut"),
    namensschild("Polizeibeamter", X1, BR, "ga1", BLAU, d=0.2),
    peep_voll("EJ_ruhig", X2, BR, FR, "ga1", d=0.2, bis="ga2"),
    peep_voll("EJ_denkt", X2, BR, FR, "ga2", anim="cut"),
    namensschild("Ermittlungsrichterin", X2 - 40, BR, "ga1", BLAU, d=0.3),
    ficon("tabler", "book", MB, 380, 100, "ga1", fuell=WEISS, bis="ga2"),
    pl("Wortlaut-Ansicht", MB, 160, "ga1", fill=WEISS, size=28, anker="m", bis="ga2"),
    ficon("tabler", "ban", MB, 380, 100, "ga2", fuell=ROTHELL, anim="cut", bis="gsst"),
    pl("alles gesperrt", MB, 160, "ga2", fill=ROTHELL, size=28, anker="m", anim="cut", bis="gsst"),
    ficon("tabler", "help-circle", MB, 380, 100, "gsst", fuell=BLAUHELL, anim="cut", bis="praxis"),
    pl("Großer Senat: offen", MB, 160, "gsst", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="praxis"),
    ficon("tabler", "scale", MB, 380, 110, "praxis", fuell=GELB, anim="cut"),
    pl("BGH: Sperre", MB, 160, "praxis", fill=GELB, size=28, anker="m", anim="cut"),
]))

# K Ausnahme 1: Richter ----------------------------------------------------------------------------------------------------------
PA = "Ausnahme 1: Richter"
folie([("richter", f"{PA} › hat belehrt"), (beim("richter", "darf"), f"{PA} › darf als Zeuge gehört werden"),
       ("qual", f"{PA} › keine weitergehende Belehrung"), ("grund", f"{PA} › Grund"),
       ("vorhalt", f"{PA} › Erinnerung, Protokoll nur Vorhalt")], rechts_frei([
    *tafel("richter", "Ausnahme 1: Der Richter hat belehrt"),
    z("Ein Richter hat die Zeugin vorher belehrt:", 110, 180, "richter", "Bold", 32),
    ok(140, 245, beim("richter", "darf"), gr=16),
    z("Er darf als Zeuge gehört werden.", 175, 225, beim("richter", "darf"), "ExtraBold", 32),
    fund("BGH (GrS), GSSt 1/16, Leitsatz, Rn. 32", 175, 272, beim("richter", "darf")),
    ok(140, 355, "qual", gr=16),
    z("keine weitergehende Belehrung nötig", 175, 335, "qual", "Bold", 32),
    fund("GSSt 1/16, Leitsatz, Rn. 53", 175, 382, beim("qual", "nötig")),
    z("Grund: höheres Gewicht richterlicher Vernehmungen", 110, 450, "grund", "Bold", 30),
    fund("GSSt 1/16, Rn. 33, 63", 150, 495, beim("grund", "richterlicher")),
    fb(110, 570, 1040, 90, GELB, "vorhalt", [("Beweismittel: die Erinnerung des Richters", "ExtraBold", 32, INK)]),
    z("Protokoll: nur Vorhalt, nicht verlesen", 110, 685, beim("vorhalt", "Protokoll"), "ExtraBold", 32),
    fund("BGH, Beschl. v. 11.4.2012 – 3 StR 108/12, Rn. 3 f.", 150, 732, beim("vorhalt", "Protokoll")),
    peep_voll("EJ_ruhig", X1, BR, FR, "richter", bis="qual"),
    peep_voll("EJ_ernst", X1, BR, FR, "qual", anim="cut"),
    namensschild("Ermittlungsrichterin", X1 + 20, BR, "richter", BLAU, d=0.2),
    peep_voll("FH_ruhig", X2, BR, FR, "richter", d=0.2, bis="vorhalt"),
    peep_voll("FH_denkt", X2, BR, FR, "vorhalt", anim="cut"),
    namensschild("Frau Hasselbach", X2, BR, "richter", GELB, d=0.3),
    ficon("tabler", "gavel", MB, 380, 100, "richter", fuell=GELB, bis="qual"),
    pl("Richter: ja", MB, 160, beim("richter", "darf"), fill=GELB, size=28, anker="m", bis="qual"),
    ficon("tabler", "info-circle", MB, 380, 100, "qual", fuell=GRUENHELL, anim="cut", bis="grund"),
    pl("einfache Belehrung genügt", MB, 160, "qual", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="grund"),
    ficon("tabler", "scale", MB, 380, 110, "grund", fuell=WEISS, anim="cut", bis="vorhalt"),
    pl("höheres Gewicht", MB, 160, "grund", fill=WEISS, size=28, anker="m", anim="cut", bis="vorhalt"),
    ficon("tabler", "file-text", MB, 380, 100, "vorhalt", fuell=GELB, anim="cut"),
    pl("Erinnerung zählt", MB, 160, "vorhalt", fill=GELB, size=28, anker="m", anim="cut"),
]))

# L Ausnahme 2: Gestattung --------------------------------------------------------------------------------------------------------
PG = "Ausnahme 2: Gestattung"
folie([("gest", f"{PG} › ausdrücklich erlaubt"), ("gest2", f"{PG} › Polizeibeamter darf berichten"),
       ("gest3", f"{PG} › qualifizierte Belehrung"), ("teil", f"{PG} › nicht teilbar")], rechts_frei([
    *tafel("gest", "Ausnahme 2: Die Zeugin gestattet"),
    z("Sie verweigert das Zeugnis, erlaubt aber", 110, 180, beim("gest", "Die"), "Bold", 32),
    z("ausdrücklich die Verwertung.", 110, 225, beim("gest", "ausdrücklich"), "ExtraBold", 32),
    fund("GSSt 1/16, Rn. 32; BGH, Beschl. v. 18.10.2023 – 1 StR 222/23, Rn. 8", 150, 272, beim("gest", "ausdrücklich")),
    ok(140, 350, "gest2", gr=16),
    z("Dann darf auch der Polizeibeamte berichten.", 175, 330, "gest2", "Bold", 32),
    fb(110, 410, 1040, 130, GELB, "gest3", [("Vorher: qualifizierte Belehrung", "ExtraBold", 32, INK),
                                          ("über Möglichkeit und Folgen", "ExtraBold", 32, INK)]),
    z("Belehrung und Erklärung ins Protokoll", 110, 555, beim("gest3", "beides"), "Bold", 30),
    fund("BGH, Beschl. v. 13.6.2012 – 2 StR 112/12, Rn. 7 f. (BGHSt 57, 254)", 150, 600, beim("gest3", "beides")),
    nein(140, 690, "teil", gr=18),
    z("nicht auf einzelne Vernehmungen beschränkbar:", 175, 670, "teil", "Bold", 30),
    z("sonst alles gesperrt, außer Richter nach Belehrung", 175, 713, beim("teil", "Dann"), "Bold", 30),
    fund("BGH, Beschl. v. 18.10.2023 – 1 StR 222/23, Leitsatz", 175, 758, beim("teil", "Dann")),
    peep_voll("FH_ruhig", X1, BR, FR, "gest", bis=beim("gest", "ausdrücklich")),
    peep_voll("FH_froh", X1, BR, FR, beim("gest", "ausdrücklich"), anim="cut", bis="teil"),
    peep_voll("FH_denkt", X1, BR, FR, "teil", anim="cut"),
    namensschild("Frau Hasselbach", X1, BR, "gest", GELB, d=0.2),
    peep_voll("PB_ruhig", X2, BR, FR, "gest", d=0.2, bis="gest2"),
    peep_voll("PB_froh", X2, BR, FR, "gest2", anim="cut", bis="teil"),
    peep_voll("PB_denkt", X2, BR, FR, "teil", anim="cut"),
    namensschild("Polizeibeamter", X2, BR, "gest", BLAU, d=0.3),
    ficon("tabler", "signature", MB, 380, 100, beim("gest", "ausdrücklich"), fuell=GRUENHELL, bis="gest2"),
    pl("Erlaubnis", MB, 160, beim("gest", "ausdrücklich"), fill=GRUENHELL, size=28, anker="m", bis="gest2"),
    ficon("tabler", "messages", MB, 380, 100, "gest2", fuell=WEISS, anim="cut", bis="gest3"),
    pl("Polizeibeamter: ja", MB, 160, "gest2", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="gest3"),
    ficon("tabler", "info-circle", MB, 380, 100, "gest3", fuell=GELB, anim="cut", bis="teil"),
    pl("qualifiziert belehren", MB, 160, "gest3", fill=GELB, size=28, anker="m", anim="cut", bis="teil"),
    ficon("tabler", "ban", MB, 380, 100, "teil", fuell=ROTHELL, anim="cut"),
    pl("kein Teilverzicht", MB, 160, "teil", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# M Äußerungen außerhalb einer Vernehmung ---------------------------------------------------------------------------------------
PV = "Außerhalb einer Vernehmung"
folie([("spont", f"{PV} › nicht gesperrt"), ("spont2", f"{PV} › Gespräch mit einer Freundin")], rechts_frei([
    *tafel("spont", "Außerhalb einer Vernehmung"),
    ok(140, 200, "spont", gr=16),
    z("nicht gesperrt: Äußerungen außerhalb", 175, 180, "spont", "Bold", 32),
    z("einer Vernehmung, etwa eine echte Spontanäußerung", 175, 225, beim("spont", "etwa"), "Bold", 30),
    fund("BGH, Beschl. v. 23.10.2012 – 1 StR 137/12, Rn. 12", 175, 272, beim("spont", "Spontan")),
    fb(110, 360, 1040, 90, GRUENHELL, "spont2", [("Hätte sie es einer Freundin erzählt:", "ExtraBold", 32, INK)]),
    z("Die Freundin dürfte darüber aussagen.", 110, 475, beim("spont2", "dürfte"), "ExtraBold", 32),
    fund("Anwendung von 1 StR 137/12, Rn. 12: Gespräch ist keine Vernehmung", 150, 522, beim("spont2", "dürfte")),
    peep_voll("FH_ruhig_r", X1, BR, FR, "spont", bis="spont2"),
    peep_voll("FH_froh_r", X1, BR, FR, "spont2", anim="cut"),
    namensschild("Frau Hasselbach", X1, BR, "spont", GELB, d=0.2),
    peep_voll("FR_ruhig", X2, BR, FR, "spont2", bis=beim("spont2", "dürfte")),
    peep_voll("FR_denkt", X2, BR, FR, beim("spont2", "dürfte"), anim="cut"),
    namensschild("Freundin", X2, BR, "spont2", GELB, d=0.1),
    ficon("tabler", "message-circle", MB, 380, 100, "spont", fuell=WEISS, bis="spont2"),
    pl("keine Vernehmung", MB, 160, "spont", fill=GRUENHELL, size=28, anker="m", bis="spont2"),
    ficon("tabler", "messages", MB, 380, 100, "spont2", fuell=GELB, anim="cut"),
    pl("Gespräch unter Freundinnen", MB, 160, "spont2", fill=GELB, size=28, anker="m", anim="cut"),
]))

# N Lösung: der Polizeibeamte als Zeuge -------------------------------------------------------------------------------------------
PL = "Lösung"
folie([("l1", f"{PL} › der Polizeibeamte als Zeuge"), ("l1a", f"{PL} › Ehefrau, erst in der HV geschwiegen"),
       ("l1b", f"{PL} › polizeiliche Aussage, keine Gestattung"), ("l1c", f"{PL} › Polizeibeamter durfte nicht aussagen")],
      rechts_frei([
    *tafel("l1", "Lösung: der Polizeibeamte als Zeuge"),
    ok(140, 200, beim("l1a", "Ehefrau"), gr=16),
    z("Ehefrau, § 52 Abs. 1 Nr. 2 StPO", 175, 180, beim("l1a", "Ehefrau"), "Bold", 32),
    ok(140, 255, beim("l1a", "erst"), gr=16),
    z("Zeugnisverweigerung erst in der HV", 175, 235, beim("l1a", "erst"), "Bold", 32),
    ok(140, 310, "l1b", gr=16),
    z("frühere Aussage: polizeiliche Vernehmung", 175, 290, "l1b", "Bold", 32),
    nein(140, 365, beim("l1b", "Verwertung"), gr=18),
    z("Gestattung: nein", 175, 345, beim("l1b", "Verwertung"), "Bold", 32),
    fb(110, 440, 1040, 130, ROTHELL, "l1c", [("Der Polizeibeamte durfte nicht über", "ExtraBold", 32, INK),
                                           ("ihre Aussage gehört werden.", "ExtraBold", 32, INK)]),
    fund("§ 252 StPO; GSSt 1/16, Rn. 32; 3 StR 377/18, Rn. 12", 150, 582, beim("l1c", "gehört")),
    peep_voll("FH_ruhig", X1, BR, FR, "l1", bis="l1b"),
    peep_voll("FH_fest", X1, BR, FR, "l1b", anim="cut"),
    namensschild("Frau Hasselbach", X1, BR, "l1", GELB, d=0.2),
    peep_voll("PB_ruhig", X2, BR, FR, "l1", d=0.2, bis="l1c"),
    peep_voll("PB_ernst", X2, BR, FR, "l1c", anim="cut"),
    namensschild("Polizeibeamter", X2, BR, "l1", BLAU, d=0.3),
    ficon("tabler", "heart-handshake", MB, 380, 100, beim("l1a", "Ehefrau"), fuell=ROSE, bis="l1b"),
    pl("Ehefrau", MB, 160, beim("l1a", "Ehefrau"), fill=ROSE, size=28, anker="m", bis="l1b"),
    ficon("tabler", "notebook", MB, 380, 90, "l1b", fuell=WEISS, anim="cut", bis="l1c"),
    pl("nur Polizei", MB, 160, "l1b", fill=WEISS, size=28, anker="m", anim="cut", bis="l1c"),
    ficon("tabler", "microphone-off", MB, 380, 100, "l1c", fuell=ROTHELL, anim="cut"),
    pl("Verhörsperson: gesperrt", MB, 160, "l1c", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# O Revisionsrüge: Vortrag ----------------------------------------------------------------------------------------------------------
PRV = "Revision"
folie([("v1", f"{PRV} › Rüge der Verteidigerin"), ("l2", f"{PRV} › Verfahrensrüge"),
       ("l2a", f"{PRV} › § 344 Abs. 2 S. 2 StPO"), ("l2c", f"{PRV} › Tatsachen vortragen")], rechts_frei([
    *tafel("v1", "Revision: die Verfahrensrüge"),
    z("Verfahrensrüge, § 344 Abs. 2 S. 1 StPO", 110, 180, beim("l2", "Verfahrensrüge"), "Bold", 32),
    *wortlaut(110, 245, 1040, 125, "l2a", [
        [("„Ersterenfalls müssen die ", 0), ("den Mangel enthaltenden", "t")],
        [("Tatsachen", "t2"), (" angegeben werden.“", 0)],
    ], 30, {"t": beim("l2b", "Mangel"), "t2": beim("l2b", "Mangel")}, "§ 344 Abs. 2 S. 2 StPO"),
    z("Tatsachen, etwa:", 110, 435, "l2c", "ExtraBold", 32),
    z("· die Ehe", 130, 480, beim("l2c", "Ehe"), size=30),
    z("· die polizeiliche Aussage", 130, 522, beim("l2c", "polizeiliche"), size=30),
    z("· die Zeugnisverweigerung in der HV", 130, 564, beim("l2c", "Zeugnisverweigerung"), size=30),
    z("· die Vernehmung des Polizeibeamten", 130, 606, beim("l2c", "Vernehmung"), size=30),
    z("· das Urteil baut auf seiner Aussage auf", 130, 648, beim("l2c", "Urteil"), size=30),
    fund("vgl. BGH, Beschl. v. 18.10.2023 – 1 StR 222/23, Rn. 3 f.", 150, 700, beim("l2c", "Urteil")),
    *redet("VT_redet", X1, BR, FR, "v1", "l2"),
    peep_voll("VT_ruhig", X1, BR, FR, "l2", anim="cut", bis="l2c"),
    peep_voll("VT_ernst", X1, BR, FR, "l2c", anim="cut"),
    namensschild("Verteidigerin", X1, BR, "v1", BLAU, d=0.2),
    peep_voll("HH_ruhig", X2, BR, FR, "v1", d=0.2, bis="l2c"),
    peep_voll("HH_denkt", X2, BR, FR, "l2c", anim="cut"),
    namensschild("Herr Hasselbach", X2, BR, "v1", GELB, d=0.3),
    blase("sprech", 560, 190, "v1", 1560, 250, inhalt=["Ich rüge die Verletzung", "von § 252 StPO."], textsize=32,
          figur=("VT_redet", X1, BR, FR), bis="l2"),
    ficon("tabler", "file-text", MB, 380, 100, "l2", fuell=WEISS, bis="l2a"),
    pl("Verfahrensrüge", MB, 160, beim("l2", "Verfahrensrüge"), fill=WEISS, size=28, anker="m", bis="l2a"),
    ficon("tabler", "list-check", MB, 380, 100, "l2a", fuell=GELB, anim="cut"),
    pl("Tatsachen angeben", MB, 160, "l2a", fill=GELB, size=28, anker="m", anim="cut"),
]))

# P Revisionsrüge: was nicht nötig ist, Beruhen -----------------------------------------------------------------------------------
folie([("l2d", f"{PRV} › Gestattung: kein Vortrag nötig"), ("l2e", f"{PRV} › kein Widerspruch nötig"),
       ("l2f", f"{PRV} › Beruhen, § 337 StPO"), ("verw072", f"{PRV} › siehe Folge 072")], rechts_frei([
    *tafel("l2d", "Verfahrensrüge: Vortrag und Beruhen"),
    ok(140, 200, "l2d", gr=16),
    z("fehlende Gestattung: kein eigener Vortrag nötig", 175, 180, "l2d", "Bold", 30),
    fund("BGH, Beschl. v. 13.6.2012 – 2 StR 112/12, Leitsatz 1, Rn. 6 f.", 175, 225, beim("l2d", "vortragen")),
    z("anders als beim Belehrungsfehler des Beschuldigten:", 175, 295, "l2e", "Bold", 30),
    ok(140, 360, beim("l2e", "keinen"), gr=16),
    z("kein Widerspruch in der HV nötig", 175, 340, beim("l2e", "keinen"), "ExtraBold", 32),
    fund("BGH, Beschl. v. 11.4.2012 – 3 StR 108/12, Rn. 3 f.", 175, 387, beim("l2e", "Widerspruch")),
    fb(110, 460, 1040, 90, GRUENHELL, "l2f", [("Das Urteil kann auf der Aussage beruhen.", "ExtraBold", 32, INK)]),
    z("Die Rüge hat Erfolg.", 110, 575, beim("l2f", "hat"), "ExtraBold", 36),
    fund("§ 337 Abs. 1 StPO; 1 StR 222/23, Rn. 12", 150, 627, beim("l2f", "beruhen")),
    fb(110, 710, 1040, 90, BLAUHELL, "verw072", [("Mehr dazu: Folge 072 · Verfahrensrüge", "ExtraBold", 30, INK)]),
    peep_voll("VT_ruhig", X1, BR, FR, "l2d", bis="l2f"),
    peep_voll("VT_froh", X1, BR, FR, "l2f", anim="cut"),
    namensschild("Verteidigerin", X1, BR, "l2d", BLAU, d=0.2),
    peep_voll("HH_denkt", X2, BR, FR, "l2d", d=0.2, bis="l2f"),
    peep_voll("HH_froh", X2, BR, FR, beim("l2f", "hat"), anim="cut"),
    peep_voll("HH_ruhig", X2, BR, FR, "l2f", anim="cut", bis=beim("l2f", "hat")),
    namensschild("Herr Hasselbach", X2, BR, "l2d", GELB, d=0.3),
    ficon("tabler", "file-description", MB, 380, 100, "l2d", fuell=WEISS, bis="l2e"),
    pl("kein Negativvortrag", MB, 160, "l2d", fill=WEISS, size=28, anker="m", bis="l2e"),
    ficon("tabler", "message-off", MB, 380, 100, "l2e", fuell=GELB, anim="cut", bis="l2f"),
    pl("kein Widerspruch nötig", MB, 160, beim("l2e", "keinen"), fill=GELB, size=28, anker="m", bis="l2f"),
    ficon("tabler", "circle-check", MB, 380, 100, "l2f", fuell=GRUENHELL, anim="cut", bis="verw072"),
    pl("Rüge begründet", MB, 160, beim("l2f", "hat"), fill=GRUENHELL, size=28, anker="m", bis="verw072"),
    ficon("tabler", "player-play", MB, 380, 100, "verw072", fuell=BLAUHELL, anim="cut"),
    pl("Folge 072", MB, 160, "verw072", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# Q Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · § 252 in vier Schritten"), ("s1", "Klausurtipp · I. § 52 und Schweigen erst in der HV?"),
       ("s2", "Klausurtipp · II. Verlesen oder Verhörsperson?"), ("s3", "Klausurtipp · III. Ausnahme?"),
       ("s4", "Klausurtipp · IV. Revision: Rüge und Beruhen")], [
    *tafel("tipp", "Klausurtipp: § 252 in vier Schritten", h=860, fill=HELL),
    warnung_i(150, 205, "tipp", gr=26),
    z("Prüf in dieser Reihenfolge:", 200, 180, beim("tipp", "Prüf"), "Bold", 36),
    z("I. Recht nach § 52 StPO, Schweigen erst in der HV?", 130, 275, "s1", "ExtraBold", 32),
    z("II. Weg: Verlesen oder Verhörsperson?", 130, 375, "s2", "ExtraBold", 32),
    z("III. Ausnahme: belehrter Richter,", 130, 475, "s3", "ExtraBold", 32),
    z("Gestattung, Äußerung außerhalb einer Vernehmung", 190, 522, beim("s3", "Gestattung"), size=30),
    z("IV. Revision: Verfahrensrüge mit allen Tatsachen,", 130, 625, "s4", "ExtraBold", 32),
    z("Beruhen, § 337 StPO", 190, 672, beim("s4", "Beruhen"), size=30),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "merke"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# R Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("§ 252 StPO verbietet dem Wortlaut nach", 0)], [("nur das ", 0), ("Verlesen.", "a")]],
                750, 300, 50, "merke", {"a": beim("merke", "Verlesen")}),
    *markertext([[("Nach der Rechtsprechung sperrt er auch", 0)], [("die ", 0), ("Verhörsperson.", "b")],
                 [("Berichten darf nur der ", 0), ("Richter, der belehrt hat,", "c")],
                 [("es sei denn, die Zeugin ", 0), ("gestattet", "d"), (" die Verwertung.", 0)]], 750, 470, 44, "mz",
                {"b": beim("mz", "Verhörsperson"), "c": beim("mz", "Richter"), "d": beim("mz", "gestattet")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
