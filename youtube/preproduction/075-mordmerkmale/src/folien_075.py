"""Folge 075 · Mordmerkmale § 211 StGB: Mord oder Totschlag? Alle Gruppen – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall 1 an der Hofeinfahrt (Norbert, Horst), A2 Fall 2 im Wohnzimmer (Dietmar, Friederike),
A3 die Frage, B Sachverhalt, C Totschlag und Mord (§ 212 Wortlaut, Streit, § 28, lebenslang), D Wortlautkarte § 211 Abs. 2 mit
drei Gruppen, E 1. Gruppe: Mordlust, Geschlechtstrieb, Habgier (Friederike), F 1. Gruppe: niedrige Beweggründe (Norbert),
G 2. Gruppe: Heimtücke (Definitionen), H Heimtücke: Ausnutzen, feindliche Willensrichtung, Fall Horst, I grausam und
gemeingefährliche Mittel, J 3. Gruppe: Ermöglichung und Verdeckung, K Ergebnis, L Klausurtipp (Lexi), M Klausurschema,
N Merksatz (Lexi).
Sehr zurückhaltend: kein Messer, kein Stich, kein Blut, keine Leiche, keine Gewaltpose. Die Tat selbst ist nie im Bild; nach der
Tat verschwindet das Opfer, an seiner Stelle steht ein kleines Grablicht. Wut = Gewitterwolke, Erbschaft = Testament/Haus/Münze,
Ergebnis = Gerichtssymbol. Geräusche nur bei sichtbarer Handlung (Tür beim Hinausgehen von Dietmar, falls vorhanden)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_075/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (233, 241, 253, 255)
GRAU = (205, 205, 210, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def markertext_farbig(zeilen_tokens, cx, y, size, cue, hl_cues, farben, lh=1.3):
    """Wie ostil.markertext, aber mit eigener Markerfarbe je Schlüssel (drei Gruppen: Gelb, Blau, Lila)."""
    fr, fb = F("Regular", size), F("ExtraBold", size)
    lines, maxw = [], 0
    for toks in zeilen_tokens:
        glyphen("".join(t for t, _ in toks))
        wid = sum((fb if h else fr).getlength(t) for t, h in toks)
        maxw = max(maxw, wid); lines.append((toks, wid))
    hgt = int(len(lines) * size * lh + size * 0.5)
    im = Image.new("RGBA", (int(maxw) + 40, hgt))
    ov = {}
    dr = ImageDraw.Draw(im)
    yy = 0
    for toks, wid in lines:
        xx = 20 + (maxw - wid) / 2
        for t, h in toks:
            f = fb if h else fr
            tw = f.getlength(t)
            if h:
                if h not in ov:
                    ov[h] = Image.new("RGBA", im.size)
                od = ImageDraw.Draw(ov[h])
                od.rounded_rectangle((xx - 6, yy + size * 0.45, xx + tw + 6, yy + size * 1.12), 8, fill=farben[h])
                od.text((xx, yy), t, font=f, fill=INK)
            dr.text((xx, yy), t, font=f, fill=INK)
            xx += tw
        yy += size * lh
    x0 = cx - im.width / 2
    els = [El(im, x0, y, cue, "rise", 0.0, name="markertext")]
    for key, oim in ov.items():
        els.append(El(oim, x0, y, hl_cues[key], "fade", 0.0, name="marker:" + key))
    return els


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, farben=None, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    farben = farben or {k: GELB for k in hl}
    m = markertext_farbig(zeilen, x + w / 2, y + 22, size, cue, hl, farben, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


# --- Eigene Hilfsfunktion (wie Folge 062/068): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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


BODEN = 880
BR, FR_H = 930, 480                     # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel
SCHILD = {"NO": ("Norbert", BLAU), "HO": ("Horst", ROT), "DI": ("Dietmar", LILA), "FR": ("Friederike", GRUEN)}


def figur_kette(p, x, cue, mimik, folge=(), bis=None, d=0.0, unten=BR, hoehe=FR_H, schild=True, schild_d=0.2):
    """Eine Figur mit Mimikfolge [(mimik, cue), …] (Zwiebelschalenprinzip) und Namensschild ab dem ersten Bild."""
    kette = [(mimik, cue)] + list(folge)
    els = []
    for i, (m, c) in enumerate(kette):
        b = kette[i + 1][1] if i + 1 < len(kette) else bis
        els.append(peep_voll(f"{p}_{m}", x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    if schild:
        n, f = SCHILD[p]
        els.append(namensschild(n, x, unten, cue, f, d=schild_d, bis=bis))
    return els


def paar(cue, li, re, li_folge=(), re_folge=()):
    """Zwei Figuren rechts neben der Tafel: li = (Person, Mimik) bei X1, re bei X2."""
    return figur_kette(li[0], X1, cue, li[1], li_folge) + figur_kette(re[0], X2, cue, re[1], re_folge, d=0.2, schild_d=0.3)


# A1 Fall 1: Streit an der Hofeinfahrt ------------------------------------------------------------------------------------
NX, HX, FH = 760, 1180, 540            # Norbert (blickt nach rechts zu Horst), Horst (blickt nach links)
NOw = ("NO_wut_r", NX, BODEN, FH)
T_WEG = beim("wut", "mit")              # „… tötet Norbert Horst, mit Tötungsvorsatz.“ – danach steht Horst nicht mehr da
folie([(NULL, "Fall 1 · Streit an der Hofeinfahrt"), ("abend", "Fall 1 · Wieder ein Streit"),
       ("wut", "Fall 1 · Spontane Wut")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Zwei Fälle, zwei Tote", 70, 40, NULL, fill=WEISS, size=34),
    ficon("fluent-emoji-flat", "candle", 520, 112, 50, NULL, bis="norbert"),
    ficon("fluent-emoji-flat", "candle", 590, 112, 50, NULL, bis="norbert"),
    pl("von außen: alles gleich", 960, 450, beim("fall", "außen"), fill=WEISS, size=32, anker="m", bis="norbert"),
    ficon("fluent-emoji-flat", "house", 260, BODEN - 2, 300, NULL),
    ficon("fluent-emoji-flat", "house", 1660, BODEN - 2, 300, NULL, spiegeln=True),
    # gemeinsame Hofeinfahrt: helle Fläche zwischen den Häusern, Auto am Rand
    karte(470, BODEN - 4, 980, 40, NULL, fill=GRAU, rund=8, schatten=0, rand=4),
    pl("gemeinsame Hofeinfahrt", 960, 985, beim("norbert", "Hofeinfahrt"), fill=GRAU, size=28, anker="m"),
    ficon("fluent-emoji-flat", "automobile", 560, BODEN - 8, 150, beim("norbert", "Hofeinfahrt")),
    *figur_kette("NO", NX, "norbert", "ruhig_r", [("aerger_r", "abend")], bis="n1", unten=BODEN, hoehe=FH, schild=False),
    *redet("NO_wut_r", NX, BODEN, FH, "n1", "wut"),
    peep_voll("NO_wut_r", NX, BODEN, FH, "wut", anim="cut", bis=T_WEG),
    peep_voll("NO_still_r", NX, BODEN, FH, T_WEG, anim="cut"),
    namensschild("Norbert", NX, BODEN - 8, "norbert", BLAU, d=0.2),
    peep_voll("HO_ruhig", HX, BODEN, FH, beim("norbert", "Horst"), bis="rechnet"),
    peep_voll("HO_sorge", HX, BODEN, FH, "rechnet", anim="cut", bis=T_WEG),
    namensschild("Horst", HX, BODEN - 8, beim("norbert", "Horst"), ROT, d=0.2, bis=T_WEG),
    ficon("fluent-emoji-flat", "candle", HX, BODEN - 8, 70, T_WEG, anim="fade"),
    pl("seit Monaten Streit", 1450, 110, beim("norbert", "streiten"), fill=WEISS, size=32, anker="m", bis="abend"),
    ficon("tabler", "moon-stars", 1790, 180, 90, "abend", fuell=GELB),
    pl("an einem Abend: wieder Streit", 1450, 110, "abend", fill=WEISS, size=32, anker="m", anim="cut", bis="wut"),
    pl("rechnet mit einem Angriff", 1500, 330, beim("rechnet", "rechnet"), fill=ROTHELL, size=30, anker="m", bis=T_WEG),
    blase("sprech", 520, 170, "n1", 1010, 235, inhalt=["Jetzt reicht es mir", "endgültig!"], textsize=34, ziel=(805, 372), bis="wut"),
    ficon("fluent-emoji-flat", "cloud-with-lightning", NX - 10, 310, 190, beim("wut", "Wut")),
    pl("spontane Wut", 1450, 110, "wut", fill=GELB, size=32, anker="m", anim="cut"),
    pl("Tötung mit Tötungsvorsatz", 1450, 190, T_WEG, fill=WEISS, size=30, anker="m"),
])

# A2 Fall 2: die Erbschaft ----------------------------------------------------------------------------------------------------
FX, DX = 760, 1180
DIa = ("DI_redet", DX, BODEN, FH)
FRa = ("FR_redet_r", FX, BODEN, FH)
T_TAT2 = beim("tat2", "tötet")
folie([("dietmar", "Fall 2 · Die Erbschaft"), ("allein", "Fall 2 · Später, allein"), ("tat2", "Fall 2 · Um früher zu erben")], [
    linienzug([(60, BODEN), (1860, BODEN)], "dietmar", breite=7, farbe=INK),
    ficon("fluent-emoji-flat", "couch-and-lamp", 1600, BODEN - 2, 330, "dietmar"),
    ficon("fluent-emoji-flat", "framed-picture", 1400, 330, 140, "dietmar"),
    ficon("fluent-emoji-flat", "potted-plant", 320, BODEN - 2, 120, "dietmar"),
    *figur_kette("FR", FX, "dietmar", "froh_r", [("ruhig_r", "d1")], bis="f1", unten=BODEN, hoehe=FH, schild=False),
    *redet("FR_redet_r", FX, BODEN, FH, "f1", "tat2"),
    peep_voll("FR_denkt_r", FX, BODEN, FH, "tat2", anim="cut", bis=T_TAT2),
    peep_voll("FR_still_r", FX, BODEN, FH, T_TAT2, anim="cut"),
    namensschild("Friederike", FX, BODEN - 8, "dietmar", GRUEN, d=0.2),
    peep_voll("DI_froh", DX, BODEN, FH, beim("dietmar", "Onkels"), bis="d1"),
    *redet("DI_redet", DX, BODEN, FH, "d1", "allein"),
    namensschild("Dietmar", DX, BODEN - 8, beim("dietmar", "Onkels"), LILA, d=0.2, bis="allein"),
    ficon("fluent-emoji-flat", "scroll", 960, 760, 110, beim("dietmar", "einzige")),
    pl("Friederike: einzige Erbin", 960, 110, beim("dietmar", "einzige"), fill=WEISS, size=30, anker="m", bis="d1"),
    blase("sprech", 600, 190, "d1", 900, 240, inhalt=["Mein Haus und mein Geld", "bekommst du einmal, Friederike."],
          textsize=31, ziel=(1148, 410), bis="allein"),
    ficon("fluent-emoji-flat", "house-with-garden", 1440, 560, 110, beim("d1", "Haus"), bis="allein"),
    ficon("fluent-emoji-flat", "coin", 1560, 560, 80, beim("d1", "Geld"), bis="allein"),
    pl("später, allein", 960, 110, "allein", fill=WEISS, size=30, anker="m", anim="cut", bis="tat2"),
    blase("sprech", 560, 170, "f1", 1070, 250, inhalt=["Ich will das Erbe nicht", "erst in 20 Jahren."], textsize=32,
          ziel=(815, 392), bis="tat2"),
    pl("um früher an sein Vermögen zu kommen", 960, 110, "tat2", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "candle", DX, BODEN - 8, 70, T_TAT2, anim="fade"),
    pl("auf die gleiche Weise wie Norbert", DX, 520, beim("tat2", "gleiche"), fill=WEISS, size=28, anker="m"),
])

# A3 Die Frage --------------------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "frage", breite=7, farbe=INK),
    *figur_kette("NO", 520, "frage", "still_r", unten=BODEN, hoehe=FH),
    ficon("fluent-emoji-flat", "cloud-with-lightning", 510, 310, 150, "frage"),
    *figur_kette("FR", 1400, "frage", "still", unten=BODEN, hoehe=FH, schild_d=0.3),
    ficon("fluent-emoji-flat", "scroll", 1400, 310, 110, "frage"),
    pl("2 × dieselbe Tathandlung", 960, 420, beim("frage", "Zweimal"), fill=WEISS, size=34, anker="m"),
    pl("Beides Mord?", 960, 530, "frage2", fill=PINK, size=36, anker="m"),
    pl("Oder einmal nur Totschlag?", 960, 630, beim("frage2", "Oder"), fill=PINK, size=36, anker="m"),
])

# B Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Fall 1: Norbert und sein Nachbar Horst streiten seit Monaten um die gemeinsame Hofeinfahrt. An einem Abend "
            "geraten sie wieder aneinander; Horst rechnet damit, dass Norbert gleich auf ihn losgeht. In spontaner Wut tötet "
            "Norbert Horst mit Tötungsvorsatz."),
    glyphen("Fall 2: Friederike ist die einzige Erbin ihres Onkels Dietmar. Um früher an sein Vermögen zu kommen, tötet sie "
            "ihn auf die gleiche Weise wie Norbert."),
    glyphen("Weitere Umstände der beiden Taten sind nicht bekannt."),
], "Wie haben sich Norbert und Friederike strafbar gemacht?")

# C Totschlag und Mord -------------------------------------------------------------------------------------------------------
W212 = [[("„Wer ", 0), ("einen Menschen tötet", "a"), (", ", 0), ("ohne Mörder zu sein", "b"), (", wird", 0)],
        [("als Totschläger mit Freiheitsstrafe nicht unter fünf Jahren bestraft.“", 0)]]
folie([("p212", "A. Totschlag, § 212 StGB"), ("p211", "A. Mord, § 211 StGB › zusätzlich ein Mordmerkmal"),
       ("streit", "A. Mord und Totschlag › Verhältnis: Streit"), ("p28", "A. Mord und Totschlag › Teilnehmer, § 28 StGB"),
       ("lebensl", "A. Mord › Rechtsfolge, § 211 Abs. 1 StGB")], rechts_frei([
    *tafel("p212", "Totschlag und Mord: §§ 212, 211 StGB", size=46),
    *wortlaut(110, 175, 1040, 115, "p212", W212, 30, {"a": beim("p212", "Menschen"), "b": beim("p212", "ohne")}, "§ 212 Abs. 1 StGB"),
    ok(135, 365, "beide", gr=18),
    z("Norbert und Friederike: vorsätzlich getötet", 175, 345, "beide", "Bold", 32),
    z("Mord: zusätzlich ein Mordmerkmal, § 211 Abs. 2", 110, 415, "p211", "ExtraBold", 33),
    karte(110, 480, 505, 150, "streit", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Lehre:", 135, 495, beim("streit", "Lehre"), "ExtraBold", 30, rechts=600),
    z("Qualifikation", 135, 540, beim("streit", "Qualifikation"), "Bold", 30, rechts=600),
    z("des Totschlags", 135, 580, beim("streit", "Qualifikation"), size=30, rechts=600),
    karte(645, 480, 505, 150, beim("streit", "Bundesgerichtshof"), fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("BGH (bisher):", 670, 495, beim("streit", "Bundesgerichtshof"), "ExtraBold", 30, rechts=1135),
    z("selbständiger", 670, 540, beim("streit", "selbständigen"), "Bold", 30, rechts=1135),
    z("Tatbestand", 670, 580, beim("streit", "selbständigen"), "Bold", 30, rechts=1135),
    fund("BGH, Beschl. v. 10.1.2006 – 5 StR 341/05, Rn. 45, 46", 110, 645, beim("streit", "Bundesgerichtshof")),
    z("Bedeutung vor allem für Teilnehmer: § 28 StGB", 110, 705, "p28", "Bold", 32),
    fl_block(110, 770, 1040, 90, GELB, "lebensl", [("Strafe: lebenslange Freiheitsstrafe, § 211 Abs. 1", "ExtraBold", 32, INK)]),
    *paar("p212", ("NO", "still"), ("FR", "still"), li_folge=[("ernst", "p211")], re_folge=[("ernst", "p211")]),
    pl("§ 212 StGB", MB, 160, beim("p212", "Paragraf"), fill=WEISS, size=30, anker="m", bis="p211"),
    ficon("tabler", "users", MB, 380, 110, "beide", fuell=BLAU, bis="p211"),
    pl("+ Mordmerkmal?", MB, 160, "p211", fill=GELB, size=30, anker="m", anim="cut", bis="streit"),
    ficon("tabler", "scale", MB, 380, 110, "streit", fuell=LILA, bis="lebensl"),
    pl("Streit", MB, 160, "streit", fill=LILA, size=30, anker="m", anim="cut", bis="p28"),
    pl("§ 28 StGB", MB, 160, "p28", fill=WEISS, size=30, anker="m", anim="cut", bis="lebensl"),
    ficon("tabler", "gavel", MB, 380, 110, "lebensl", fuell=GELB, anim="cut"),
    pl("lebenslang", MB, 160, "lebensl", fill=GELB, size=30, anker="m", anim="cut"),
]))

# D Wortlautkarte § 211 Abs. 2, drei Gruppen ----------------------------------------------------------------------------------
W211 = [[("„Mörder ist, wer ", 0), ("aus Mordlust", "a"), (", ", 0), ("zur Befriedigung des", "a")],
        [("Geschlechtstriebs", "a"), (", ", 0), ("aus Habgier", "a"), (" oder ", 0), ("sonst aus niedrigen", "a")],
        [("Beweggründen", "a"), (", ", 0), ("heimtückisch", "b"), (" oder ", 0), ("grausam", "b"), (" oder ", 0),
         ("mit gemein-", "b")],
        [("gefährlichen Mitteln", "b"), (" oder um eine andere Straftat ", 0), ("zu ermöglichen", "c")],
        [("oder zu verdecken", "c"), (", einen Menschen tötet.“", 0)]]
folie([("wl", "B. Mordmerkmale, § 211 Abs. 2 StGB"), ("g1", "B. Mordmerkmale › 1. Gruppe: Motiv"),
       ("g2", "B. Mordmerkmale › 2. Gruppe: Tatausführung"), ("g3", "B. Mordmerkmale › 3. Gruppe: Zweck")], rechts_frei([
    *tafel("wl", "Die Mordmerkmale: § 211 Abs. 2 StGB", size=46),
    *wortlaut(110, 175, 1040, 255, "wl", W211, 31, {"a": "g1", "b": "g2", "c": "g3"}, "§ 211 Abs. 2 StGB",
              farben={"a": GELB, "b": BLAU, "c": LILA}),
    z("drei Gruppen:", 110, 490, "gruppen", "ExtraBold", 34),
    fl_block(110, 550, 1040, 80, GELB, "g1", [("1. Gruppe: Motiv", "ExtraBold", 34, INK)]),
    fl_block(110, 650, 1040, 80, BLAU, "g2", [("2. Gruppe: Art der Tatausführung", "ExtraBold", 34, INK)]),
    fl_block(110, 750, 1040, 80, LILA, "g3", [("3. Gruppe: Zweck der Tat", "ExtraBold", 34, INK)]),
    ficon("fluent-emoji-flat", "balance-scale", 1560, 370, 140, "wl", bis="g1"),
    pl("§ 211 Abs. 2 StGB", 1560, 160, beim("wl", "Paragraf"), fill=WEISS, size=30, anker="m", bis="g1"),
    pl("drei Gruppen", 1560, 420, "gruppen", fill=WEISS, size=30, anker="m", bis="g1"),
    ficon("tabler", "brain", 1400, 400, 110, "g1", fuell=GELB),
    pl("Motiv", 1400, 440, "g1", fill=GELB, size=30, anker="m"),
    ficon("tabler", "route", 1720, 400, 110, "g2", fuell=BLAU),
    pl("Tatausführung", 1720, 440, "g2", fill=BLAU, size=30, anker="m"),
    ficon("tabler", "target", 1560, 700, 110, "g3", fuell=LILA),
    pl("Zweck", 1560, 740, "g3", fill=LILA, size=30, anker="m"),
]))

# E 1. Gruppe: Mordlust, Geschlechtstrieb, Habgier ------------------------------------------------------------------------------
P1 = "B. 1. Gruppe"
folie([("mlust", f"{P1} › Mordlust"), ("sex", f"{P1} › Befriedigung des Geschlechtstriebs"), ("habgier", f"{P1} › Habgier"),
       ("erbe", "Fall 2 › Friederike: Habgier"), ("hab_ja", "Fall 2 › Habgier (+)")], rechts_frei([
    *tafel("mlust", "1. Gruppe: Motiv", fill=WEISS),
    z("Mordlust: aus Freude an der Vernichtung", 110, 180, "mlust", "Bold", 32),
    z("eines Menschenlebens", 110, 222, beim("mlust", "Vernichtung"), "Bold", 32),
    fund("BGH, Beschl. v. 13.8.2019 – 5 StR 257/19, Rn. 15", 150, 268, beim("mlust", "Vernichtung")),
    z("zur Befriedigung des Geschlechtstriebs", 110, 315, "sex", "Bold", 32),
    z("Habgier: Streben nach materiellen Gütern,", 110, 385, "habgier", "Bold", 32),
    z("das in seiner Hemmungslosigkeit und Rücksichtslosigkeit", 110, 427, beim("habgier", "Hemmungslosigkeit"), size=30),
    z("das erträgliche Maß weit übersteigt", 110, 467, beim("habgier", "erträgliche"), size=30),
    z("Vermögen soll sich durch den Tod vermehren,", 110, 517, "vermehr", size=30),
    z("zumindest nach Vorstellung des Täters", 110, 557, beim("vermehr", "zumindest"), size=30),
    fund("BGH, Beschl. v. 19.5.2020 – 4 StR 140/20, Rn. 4", 150, 600, beim("vermehr", "zumindest")),
    z("Friederike: tötet, um früher zu erben", 110, 660, "erbe", "Bold", 32),
    ok(135, 745, "hab_ja", gr=20),
    fl_block(110, 715, 1040, 90, GRUEN, "hab_ja", [("Habgier (+)", "ExtraBold", 36, INK)]),
    *figur_kette("FR", XS, "mlust", "ruhig", [("ernst", "habgier"), ("still", "erbe")]),
    pl("Motiv", XS, 160, "mlust", fill=GELB, size=30, anker="m", bis="habgier"),
    ficon("fluent-emoji-flat", "money-bag", XS, 380, 100, "habgier", bis="erbe"),
    pl("Habgier", XS, 160, "habgier", fill=GELB, size=30, anker="m", anim="cut", bis="erbe"),
    ficon("fluent-emoji-flat", "scroll", XS - 80, 380, 100, "erbe", anim="cut"),
    ficon("fluent-emoji-flat", "house-with-garden", XS + 80, 380, 100, beim("erbe", "erben"), anim="cut"),
    pl("früher erben", XS, 160, "erbe", fill=WEISS, size=30, anker="m", anim="cut", bis="hab_ja"),
    pl("Habgier (+)", XS, 160, "hab_ja", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# F 1. Gruppe: sonstige niedrige Beweggründe -------------------------------------------------------------------------------------
folie([("niedrig", f"{P1} › sonstige niedrige Beweggründe"), ("wutbgh", f"{P1} › niedrige Beweggründe: Wut, Zorn"),
       ("wutfall", "Fall 1 › Norbert: niedrige Beweggründe?"), ("nb_nein", "Fall 1 › niedrige Beweggründe (−)")], rechts_frei([
    *tafel("niedrig", "1. Gruppe: niedrige Beweggründe", size=46),
    z("niedrig: nach allgemeiner sittlicher Wertung", 110, 180, beim("niedrig", "Niedrig"), "Bold", 32),
    z("auf tiefster Stufe, besonders verachtenswert", 110, 222, beim("niedrig", "tiefster"), "Bold", 32),
    z("Gesamtwürdigung aller äußeren und inneren Umstände", 110, 282, "gesamt", size=31),
    fund("BGH, Urt. v. 16.4.2024 – 6 StR 365/23, Rn. 17", 150, 327, beim("gesamt", "Umstände")),
    fl_block(110, 380, 1040, 125, GELB, "wutbgh", [("Wut, Zorn: nur, wenn nicht menschlich verständlich,", "Bold", 31, INK),
                                                  ("sondern Ausdruck einer niedrigen Gesinnung", "Bold", 31, INK)]),
    z("Norbert: nur spontane Wut in einem langen Streit,", 110, 545, "wutfall", "Bold", 32),
    z("nichts weiter", 110, 587, beim("wutfall", "nichts"), "Bold", 32),
    nein(135, 690, "nb_nein", gr=20),
    fl_block(110, 650, 1040, 90, ROTHELL, "nb_nein", [("niedriger Beweggrund (−)", "ExtraBold", 36, INK)]),
    *figur_kette("NO", XS, "niedrig", "ernst", [("aerger", "wutbgh"), ("still", "wutfall")]),
    pl("niedrig?", XS, 160, "niedrig", fill=WEISS, size=30, anker="m", bis="wutbgh"),
    ficon("tabler", "scale", XS, 380, 100, "gesamt", fuell=GELB, bis="wutbgh"),
    ficon("fluent-emoji-flat", "cloud-with-lightning", XS, 380, 140, "wutbgh", anim="cut"),
    pl("Wut", XS, 160, "wutbgh", fill=GELB, size=30, anker="m", anim="cut", bis="nb_nein"),
    pl("niedrig (−)", XS, 160, "nb_nein", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# G 2. Gruppe: Heimtücke (Definitionen) --------------------------------------------------------------------------------------------
P2 = "B. 2. Gruppe"
folie([("heim", f"{P2} › heimtückisch"), ("arglos", f"{P2} › heimtückisch: arglos"),
       ("wehrlos", f"{P2} › heimtückisch: wehrlos")], rechts_frei([
    *tafel("heim", "2. Gruppe: heimtückisch", fill=WEISS),
    z("in feindlicher Willensrichtung die Arg- und", 110, 180, beim("heim", "Heimtückisch"), "Bold", 32),
    z("Wehrlosigkeit des Opfers bewusst zur Tötung ausnutzen", 110, 222, beim("heim", "Wehrlosigkeit"), "Bold", 31),
    fund("BGH, Urt. v. 4.12.2024 – 2 StR 352/24, Rn. 25", 150, 268, beim("heim", "Wehrlosigkeit")),
    z("arglos: rechnet bei Beginn des ersten mit", 110, 340, "arglos", size=32),
    z("Tötungsvorsatz geführten Angriffs", 110, 382, beim("arglos", "Tötungsvorsatz"), size=32),
    z("nicht mit einem erheblichen Angriff", 110, 424, beim("arglos", "erheblichen"), size=32),
    fund("BGH 2 StR 352/24, Rn. 25", 150, 470, beim("arglos", "erheblichen")),
    z("wehrlos: Verteidigungsfähigkeit infolge der", 110, 540, "wehrlos", size=32),
    z("Arglosigkeit aufgehoben oder erheblich eingeschränkt", 110, 582, beim("wehrlos", "aufgehoben"), size=31),
    fund("BGH, Urt. v. 24.9.2025 – 5 StR 423/25, Rn. 13", 150, 628, beim("wehrlos", "aufgehoben")),
    *figur_kette("HO", XS, "heim", "ruhig", [("ernst", "wehrlos")]),
    pl("heimtückisch", XS, 160, "heim", fill=BLAU, size=30, anker="m", bis="arglos"),
    ficon("tabler", "user-question", XS, 380, 100, "arglos", fuell=WEISS, bis="wehrlos"),
    pl("arglos?", XS, 160, "arglos", fill=WEISS, size=30, anker="m", anim="cut", bis="wehrlos"),
    ficon("tabler", "hand-stop", XS, 380, 100, "wehrlos", fuell=WEISS, anim="cut"),
    pl("wehrlos?", XS, 160, "wehrlos", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# H Heimtücke: Ausnutzen, feindliche Willensrichtung, Fall Horst ---------------------------------------------------------------------
folie([("ausnutz", f"{P2} › heimtückisch: bewusst ausgenutzt"), ("feind", f"{P2} › heimtückisch: feindliche Willensrichtung"),
       ("horst", "Fall 1 › Horst nicht arglos: Heimtücke (−)")], rechts_frei([
    *tafel("ausnutz", "Heimtücke: Ausnutzen und Fall 1", size=46),
    z("Täter nutzt die Lage bewusst aus", 110, 180, "ausnutz", "Bold", 32),
    fund("BGH 2 StR 352/24, Rn. 32 (Ausnutzungsbewusstsein)", 150, 226, "ausnutz"),
    z("feindliche Willensrichtung fehlt nur ausnahmsweise,", 110, 290, "feind", "Bold", 32),
    z("etwa bei ausdrücklichem Willen des Opfers", 110, 332, beim("feind", "ausdrücklichen"), size=32),
    fund("BGH, Urt. v. 19.6.2019 – 5 StR 128/19 (BGHSt 64, 111), Rn. 28", 150, 378, beim("feind", "ausdrücklichen")),
    z("Horst rechnete im Streit mit einem Angriff", 110, 450, "horst", "Bold", 32),
    nein(135, 525, beim("horst", "Er"), gr=18),
    z("nicht arglos", 175, 505, beim("horst", "Er"), "Bold", 32),
    fund("BGH 2 StR 352/24, Rn. 26", 175, 550, beim("horst", "Er")),
    fl_block(110, 600, 1040, 90, ROTHELL, beim("horst", "Heimtücke"), [("Heimtücke (−)", "ExtraBold", 36, INK)]),
    *paar("ausnutz", ("NO", "ernst"), ("HO", "ruhig"), re_folge=[("sorge", "horst")]),
    pl("bewusst ausgenutzt?", MB, 160, "ausnutz", fill=WEISS, size=28, anker="m", bis="feind"),
    ficon("tabler", "eye", MB, 380, 100, "ausnutz", fuell=WEISS, bis="feind"),
    pl("feindliche Willensrichtung", MB, 160, "feind", fill=WEISS, size=28, anker="m", anim="cut", bis="horst"),
    pl("rechnete mit Angriff", MB, 160, "horst", fill=ROTHELL, size=28, anker="m", anim="cut"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "horst", fuell=GELB, anim="cut"),
]))

# I grausam, gemeingefährliche Mittel --------------------------------------------------------------------------------------------
folie([("grausam", f"{P2} › grausam"), ("gemein", f"{P2} › mit gemeingefährlichen Mitteln")], rechts_frei([
    *tafel("grausam", "2. Gruppe: grausam, gemeingefährlich", size=44),
    z("grausam: in gefühlloser, unbarmherziger Gesinnung", 110, 180, "grausam", "Bold", 31),
    z("Schmerzen oder Qualen, die nach Stärke und Dauer", 110, 222, beim("grausam", "Schmerzen"), size=31),
    z("über das für die Tötung erforderliche Maß hinausgehen", 110, 264, beim("grausam", "über"), size=31),
    fund("BGH, Urt. v. 15.8.2019 – 5 StR 236/19, Rn. 12", 150, 310, beim("grausam", "über")),
    z("gemeingefährliches Mittel: kann in der konkreten", 110, 400, "gemein", "Bold", 31),
    z("Lage eine Mehrzahl von Menschen an Leib und", 110, 442, beim("gemein", "Mehrzahl"), size=31),
    z("Leben gefährden, weil der Täter die Ausdehnung", 110, 484, beim("gemein", "weil"), size=31),
    z("der Gefahr nicht in seiner Gewalt hat", 110, 526, beim("gemein", "weil"), size=31),
    fund("BGH, Urt. v. 18.6.2020 – 4 StR 482/19, Rn. 49", 150, 572, beim("gemein", "Gewalt")),
    pl("grausam", 1560, 160, "grausam", fill=BLAU, size=30, anker="m", bis="gemein"),
    ficon("tabler", "alert-triangle", 1560, 380, 110, beim("grausam", "Schmerzen"), fuell=GELB, bis="gemein"),
    pl("über das erforderliche Maß", 1560, 430, beim("grausam", "über"), fill=WEISS, size=28, anker="m", bis="gemein"),
    pl("gemeingefährlich", 1560, 160, "gemein", fill=BLAU, size=30, anker="m", anim="cut"),
    ficon("tabler", "users-group", 1560, 400, 150, beim("gemein", "Mehrzahl"), fuell=WEISS, anim="cut"),
    pl("Gefahr nicht in seiner Gewalt", 1560, 450, beim("gemein", "weil"), fill=WEISS, size=28, anker="m", anim="cut"),
]))

# J 3. Gruppe: Ermöglichung, Verdeckung -------------------------------------------------------------------------------------------
P3 = "B. 3. Gruppe"
folie([("g3a", f"{P3} › Ermöglichungsabsicht"), ("verdeck", f"{P3} › Verdeckungsabsicht"),
       ("keins", "Fall 1 und 2 › 3. Gruppe (−)")], rechts_frei([
    *tafel("g3a", "3. Gruppe: Zweck der Tat", fill=WEISS),
    z("Ermöglichung: Tötung, um ein weiteres", 110, 180, beim("g3a", "Ermöglichung"), "Bold", 32),
    z("kriminelles Ziel zu erreichen", 110, 222, beim("g3a", "kriminelles"), "Bold", 32),
    fund("BGH, Urt. v. 3.6.2015 – 2 StR 422/14, Rn. 10", 150, 268, beim("g3a", "kriminelles")),
    z("Verdeckung: eine vorangegangene Straftat verdecken", 110, 340, "verdeck", "Bold", 31),
    z("oder Spuren, die Aufschluss über bedeutsame", 110, 382, beim("verdeck", "Spuren"), size=31),
    z("Tatumstände geben könnten", 110, 424, beim("verdeck", "Tatumstände"), size=31),
    fund("BGH, Beschl. v. 30.3.2022 – 4 StR 356/21, Rn. 8", 150, 470, beim("verdeck", "Tatumstände")),
    nein(135, 565, "keins", gr=18),
    z("in beiden Fällen: keine Rolle", 175, 545, "keins", "Bold", 32),
    *paar("g3a", ("NO", "ruhig"), ("FR", "ruhig"), li_folge=[("ernst", "keins")], re_folge=[("ernst", "keins")]),
    pl("Zweck", MB, 160, "g3a", fill=LILA, size=30, anker="m", bis="verdeck"),
    ficon("tabler", "target", MB, 380, 100, "g3a", fuell=LILA, bis="verdeck"),
    pl("verdecken", MB, 160, "verdeck", fill=LILA, size=30, anker="m", anim="cut", bis="keins"),
    ficon("tabler", "eraser", MB, 380, 100, "verdeck", fuell=WEISS, anim="cut", bis="keins"),
    pl("3. Gruppe (−)", MB, 160, "keins", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# K Ergebnis -----------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · gleiche Tat, verschiedene Motive"), ("erg1", "Ergebnis · Norbert: Totschlag, § 212 StGB"),
       ("erg2", "Ergebnis · Friederike: Mord aus Habgier, § 211 StGB")], rechts_frei([
    *tafel("erg", "Ergebnis: gleiche Tat, verschiedene Motive", size=44),
    karte(110, 190, 1040, 230, "erg1", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Fall 1: Norbert", 140, 210, "erg1", "ExtraBold", 36),
    z("strafbar wegen Totschlags, § 212 StGB", 140, 270, beim("erg1", "Totschlags"), "ExtraBold", 34),
    z("kein Mordmerkmal", 140, 330, beim("erg1", "kein"), "Bold", 32),
    karte(110, 470, 1040, 230, "erg2", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Fall 2: Friederike", 140, 490, "erg2", "ExtraBold", 36),
    z("strafbar wegen Mordes, § 211 StGB", 140, 550, beim("erg2", "Mordes"), "ExtraBold", 34),
    z("Mordmerkmal Habgier", 140, 610, beim("erg2", "Habgier"), "Bold", 32),
    *paar("erg", ("NO", "still"), ("FR", "still")),
    ficon("fluent-emoji-flat", "cloud-with-lightning", X1, 400, 120, "erg1"),
    ficon("fluent-emoji-flat", "scroll", X2, 400, 100, "erg2"),
    pl("§ 212", X1, 160, "erg1", fill=BLAU, size=30, anker="m"),
    pl("§ 211", X2, 160, "erg2", fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "gavel", MB, 270, 90, "erg", fuell=GELB),
]))

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · zuerst die vorsätzliche Tötung"), ("tipp2", "Klausurtipp · 2. Gruppe: objektiver Tatbestand"),
       ("tipp3", "Klausurtipp · 1. und 3. Gruppe: subjektiver Tatbestand")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("zuerst die vorsätzliche Tötung als Grunddelikt,", 200, 200, beim("tipp", "vorsätzliche"), "Bold", 34),
    z("danach die Mordmerkmale", 200, 250, beim("tipp", "danach"), "Bold", 34),
    z("2. Gruppe: tatbezogen", 200, 340, "tipp2", "ExtraBold", 36),
    z("objektiver Tatbestand, vom Vorsatz umfasst", 200, 392, beim("tipp2", "objektiven"), size=34),
    z("1. und 3. Gruppe: täterbezogen", 200, 482, "tipp3", "ExtraBold", 36),
    z("subjektiver Tatbestand", 200, 534, beim("tipp3", "subjektiven"), size=34),
    *redet("LX_warnt", LXX, BR, FR_H + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Klausurschema ---------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PS_ = "Klausurschema"
folie([("sch", PS_), ("k1", f"{PS_} › I. Tatbestand: objektiv"), ("k1b", f"{PS_} › I. objektiv: 2. Gruppe"),
       ("k2", f"{PS_} › I. subjektiv: Vorsatz"), ("k2b", f"{PS_} › I. subjektiv: 1. und 3. Gruppe"),
       ("k3", f"{PS_} › II. Rechtswidrigkeit"), ("k4", f"{PS_} › III. Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Mord, §§ 212, 211 StGB", 110, 90, "sch", 52),
    z("I. Tatbestand", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("1. objektiver Tatbestand: Tötung eines Menschen", K2, 255, beim("k1", "Objektiv"), size=34, rechts=1820),
    z("tatbezogene Mordmerkmale der 2. Gruppe", K3, 310, "k1b", size=34, rechts=1820),
    z("2. subjektiver Tatbestand: Vorsatz, auch für diese Merkmale", K2, 380, "k2", size=34, rechts=1820),
    z("täterbezogene Mordmerkmale der 1. und 3. Gruppe", K3, 435, "k2b", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 520, "k3", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 595, "k4", "Bold", 38, rechts=1820),
])

# N Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Mord ist eine ", 0), ("vorsätzliche Tötung", "a")], [("mit ", 0), ("Mordmerkmal", "b"), (".", 0)]],
                750, 290, 46, "merke", {"a": beim("merke", "vorsätzliche"), "b": beim("merke", "Mordmerkmal")}),
    *markertext([[("1. Gruppe: ", 0), ("Motiv", "c"), (" · 2. Gruppe: ", 0), ("Art der Tat", "d")],
                 [("3. Gruppe: ", 0), ("Zweck", "e")]], 750, 470, 44, "m2",
                {"c": beim("m2", "Motiv"), "d": beim("m2", "Art"), "e": beim("m2", "Zweck")}),
    *markertext([[("Spontane Wut allein", "f")], [("macht noch keinen Mord.", 0)]], 750, 650, 46, "m3",
                {"f": beim("m3", "Spontane")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
