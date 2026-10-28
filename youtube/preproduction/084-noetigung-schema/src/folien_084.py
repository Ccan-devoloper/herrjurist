"""Folge 084 · Nötigung § 240 Schema: Gewalt, Drohung & Verwerflichkeit – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Auszug, Kaution, Beschwerde, Drohung (Gesine, Gernot), A2 Rücknahme am Briefkasten und
Überweisung, B Sachverhalt, C Wortlaut § 240 Abs. 1, D Gewalt (kurz, Verweis auf Folge 019), E Drohung, F Drohung mit einem
Unterlassen, G empfindliches Übel, H Nötigungserfolg/Kausalität/Vorsatz, I Rechtswidrigkeit in zwei Stufen mit Wortlaut
§ 240 Abs. 2, J Mittel-Zweck-Relation (fehlender Zusammenhang), K Gegenfall Klage auf Miete, L Schuld, § 240 Abs. 4,
Ergebnis, M Abgrenzung § 253, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Gewaltfrei, Vermieter sachlich (Sakko, ruhige Mimik), keine Karikatur. Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Geräusch nur bei sichtbarer Handlung: Brief in den Briefkasten (szene_084brief_1, Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_084/"
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
NULL = "fall"                     # Szene A steht ab 0,0 s (render_084 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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
    """Wie ostil.markertext, aber mit eigener Markerfarbe je Schlüssel."""
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


# --- Eigene Hilfsfunktion (wie Folge 062/068/075): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
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
XS = 1600
SCHILD = {"GS": ("Gesine", GRUEN), "GE": ("Gernot", BLAU)}


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


def paar(cue, gs_folge=(), ge_folge=(), gs="ruhig", ge="ruhig"):
    """Gesine bei X1, Gernot bei X2, beide blicken zur Tafel."""
    return figur_kette("GS", X1, cue, gs, gs_folge) + figur_kette("GE", X2, cue, ge, ge_folge, d=0.2, schild_d=0.3)


P1 = "A. § 240 StGB › I. Tatbestand"
PR = "A. § 240 StGB › II. Rechtswidrigkeit"

# A1 Fall: Auszug, Kaution, Beschwerde, Drohung --------------------------------------------------------------------------------
GX, RX, FH = 700, 1160, 540             # Gesine (blickt nach rechts zu Gernot), Gernot (blickt nach links)
folie([(NULL, "Fall · Der Auszug"), ("kaution", "Fall · Die Kaution"), ("balkon", "Fall · Die Beschwerde beim Bauamt"),
       ("g1", "Fall · Gernots Bedingung")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    ficon("fluent-emoji-flat", "house", 260, BODEN - 2, 330, NULL),
    pl("Mietwohnung", 260, BODEN + 14, NULL, fill=WEISS, size=30, anker="m"),
    ficon("fluent-emoji-flat", "package", 470, BODEN - 2, 110, NULL),
    ficon("fluent-emoji-flat", "package", 500, BODEN - 104, 80, NULL),
    pl("Gesine ist ausgezogen", 960, 60, NULL, fill=WEISS, size=32, anker="m", bis="kaution"),
    *figur_kette("GS", GX, NULL, "ruhig_r", [("ernst_r", "balkon"), ("sorge_r", "g1")], bis="s1", unten=BODEN, hoehe=FH, schild=False),
    *redet("GS_redet_r", GX, BODEN, FH, "s1", "zurueck"),
    peep_voll("GS_sorge_r", GX, BODEN, FH, "zurueck", anim="cut"),
    namensschild("Gesine", GX, BODEN - 8, NULL, GRUEN, d=0.2),
    peep_voll("GE_ruhig", RX, BODEN, FH, beim("kaution", "Vermieter"), bis="g1"),
    *redet("GE_redet", RX, BODEN, FH, "g1", "s1"),
    peep_voll("GE_ernst", RX, BODEN, FH, "s1", anim="cut"),
    namensschild("Gernot (Vermieter)", RX, BODEN - 8, beim("kaution", "Vermieter"), BLAU, d=0.2),
    pl("Gernot schuldet ihr die Kaution: 1.500 €", 960, 60, beim("kaution", "schuldet"), fill=GELB, size=32, anker="m", anim="cut", bis="balkon"),
    ficon("fluent-emoji-flat", "euro-banknote", 930, 640, 130, beim("kaution", "eintausendfünfhundert"), bis="g1"),
    pl("Forderungen gegen Gesine: keine", 960, 140, beim("kaution", "Forderungen"), fill=WEISS, size=28, anker="m", bis="balkon"),
    pl("vor dem Auszug: Beschwerde beim Bauamt", 960, 60, "balkon", fill=WEISS, size=32, anker="m", anim="cut", bis="g1"),
    ficon("fluent-emoji-flat", "construction", 330, BODEN - 120, 70, beim("balkon", "Balkongeländer")),
    pl("lockeres Balkongeländer", 260, 450, beim("balkon", "Balkongeländer"), fill=ROTHELL, size=28, anker="m"),
    ficon("fluent-emoji-flat", "classical-building", 1640, BODEN - 2, 300, beim("balkon", "Bauamt")),
    pl("Bauamt", 1640, BODEN + 14, beim("balkon", "Bauamt"), fill=WEISS, size=30, anker="m"),
    ficon("fluent-emoji-flat", "envelope", 1640, 450, 90, beim("balkon", "Bauamt"), bis="g1"),
    blase("sprech", 900, 250, "g1", 800, 165, inhalt=["Ihre Kaution bekommen Sie erst, wenn Sie", "die Beschwerde beim Bauamt zurückziehen."],
          textsize=32, ziel=(1102, 428), bis="s1"),      # Spitze außerhalb des Gesichts am Mund (Bildprüfung)
    blase("sprech", 760, 190, "s1", 1000, 170, inhalt=["Aber die Kaution steht mir doch zu!"], textsize=34,
          ziel=(720, 418)),
])

# A2 Fall: Rücknahme und Überweisung ------------------------------------------------------------------------------------------
BX_ = 820
Z0 = beim("zurueck", "will")       # Folienstart nach Gesines letztem Wort (kein Mund im Wisch)
T_EIN = beim("zurueck", "Beschwerde")
folie([(Z0, "Fall · Gesine zieht die Beschwerde zurück"), ("ueberw", "Fall · Gernot überweist die Kaution"),
       ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], Z0, breite=7, farbe=INK),
    *figur_kette("GS", 520, Z0, "ernst_r", [("muede_r", "ueberw")], unten=BODEN, hoehe=FH, schild=False),
    namensschild("Gesine", 520, BODEN - 8, Z0, GRUEN, d=0.2),
    ficon("fluent-emoji-flat", "postbox", BX_, BODEN - 2, 150, Z0),
    pl("an das Bauamt", BX_ + 150, 700, Z0, fill=WEISS, size=28, anker="m"),
    bewegt(ficon("fluent-emoji-flat", "envelope-with-arrow", BX_, 790, 90, Z0, bis=beim("zurueck", "zurück")),
           beim("zurueck", "Sie"), T_EIN, -165, -150),
    szene(pl("Rücknahme der Beschwerde", BX_, 370, T_EIN, fill=GELB, size=30, anker="m"), "084brief_1", versatz=-0.2),
    pl("Gesine will ihr Geld", 520, 60, Z0, fill=WEISS, size=32, anker="m"),
    *figur_kette("GE", 1500, Z0, "ernst", [("ruhig", "ueberw")], unten=BODEN, hoehe=FH, schild=False),
    namensschild("Gernot (Vermieter)", 1500, BODEN - 8, Z0, BLAU, d=0.2),
    bewegt(ficon("fluent-emoji-flat", "euro-banknote", 690, 570, 120, beim("ueberw", "überweist"), anim="cut"),
           beim("ueberw", "überweist"), beim("ueberw", "Kaution"), 690, 0),
    pfeil(1380, 600, 900, 600, beim("ueberw", "überweist"), breite=8, kopf=26),
    pl("überweist 1.500 €", 1140, 628, beim("ueberw", "überweist"), fill=GELB, size=30, anker="m"),
    pl("Hat Gernot sich strafbar gemacht?", 1140, 230, "frage", fill=PINK, size=38, anker="m"),
])

# B Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Gesine ist aus ihrer Mietwohnung ausgezogen. Ihr Vermieter Gernot schuldet ihr noch die Kaution von 1.500 €; "
            "Forderungen gegen sie hat er keine. Kurz vor dem Auszug hatte Gesine sich beim Bauamt über das lockere "
            "Balkongeländer beschwert."),
    glyphen("Gernot sagt: „Ihre Kaution bekommen Sie erst, wenn Sie die Beschwerde beim Bauamt zurückziehen.“ Gesine will "
            "ihr Geld. Sie zieht die Beschwerde zurück, und Gernot überweist die Kaution."),
], "Hat Gernot sich strafbar gemacht?")

# C Wortlaut § 240 Abs. 1 ----------------------------------------------------------------------------------------------------------
W1 = [[("„Wer einen Menschen rechtswidrig ", 0), ("mit Gewalt", "a"), (" oder", 0)],
      [("durch Drohung mit einem empfindlichen Übel", "d"), (" zu einer", 0)],
      [("Handlung, Duldung oder Unterlassung nötigt", "b"), (", wird mit", 0)],
      [("Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe bestraft.“", 0)]]
folie([("pruef", "A. Nötigung, § 240 StGB"), ("mittel0", f"{P1} › Nötigungsmittel"),
       ("erfolg0", f"{P1} › Nötigungserfolg")], rechts_frei([
    *tafel("pruef", "Nötigung: § 240 Abs. 1 StGB"),
    *wortlaut(110, 180, 1040, 215, "pruef", W1, 31, {"a": beim("mittel0", "Gewalt"), "d": beim("mittel0", "Drohung"), "b": beim("erfolg0", "Handlung")},
              "§ 240 Abs. 1 StGB", farben={"a": GELB, "d": GELB, "b": BLAU}),
    fl_block(110, 470, 1040, 90, GELB, "mittel0", [("Nötigungsmittel: Gewalt oder Drohung", "ExtraBold", 34, INK)]),
    z("mit einem empfindlichen Übel", 150, 580, beim("mittel0", "empfindlichen"), "Bold", 32),
    fl_block(110, 660, 1040, 90, BLAU, "erfolg0", [("Nötigungserfolg: Handlung, Duldung, Unterlassung", "ExtraBold", 34, INK)]),
    *paar("pruef", gs_folge=[("ernst", "mittel0")], ge_folge=[("ernst", "erfolg0")]),
    pl("§ 240 StGB", MB, 160, beim("pruef", "Paragraf"), fill=WEISS, size=30, anker="m", bis="mittel0"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 130, "pruef", bis="mittel0"),
    pl("Mittel", MB, 160, "mittel0", fill=GELB, size=30, anker="m", anim="cut", bis="erfolg0"),
    ficon("tabler", "alert-triangle", MB, 380, 110, "mittel0", fuell=GELB, anim="cut", bis="erfolg0"),
    pl("Erfolg", MB, 160, "erfolg0", fill=BLAU, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "envelope-with-arrow", MB, 380, 110, "erfolg0", anim="cut"),
]))

# D Gewalt (kurz) --------------------------------------------------------------------------------------------------------------------
folie([("gewalt", f"{P1} › 1. Nötigungsmittel: Gewalt"), ("verweis", f"{P1} › 1. Gewalt: Folge zur Sitzblockade"),
       (beim("g_nein", "Gewalt"), f"{P1} › 1. Gewalt (−)")], rechts_frei([
    *tafel("gewalt", "Nötigungsmittel: Gewalt"),
    z("körperliche Kraftentfaltung des Täters", 110, 180, beim("gewalt", "körperliche"), "Bold", 33),
    z("und unmittelbare körperliche Zwangswirkung beim Opfer", 110, 225, beim("gewalt", "unmittelbare"), "Bold", 33),
    fund("BGH, Urt. v. 25.2.2021 – 3 StR 204/20, Rn. 30", 150, 275, beim("gewalt", "unmittelbare")),
    fl_block(110, 340, 1040, 90, LILAHELL, "verweis", [("Einzelheiten: unsere Folge zur Sitzblockade", "Bold", 33, INK)]),
    z("Gernot rührt Gesine nicht an", 175, 480, "g_nein", "Bold", 33),
    fl_block(110, 530, 1040, 90, ROTHELL, beim("g_nein", "Gewalt"), [("Gewalt (−)", "ExtraBold", 36, INK)]),
    *paar("gewalt", gs_folge=[("ernst", "g_nein")], ge="ernst", ge_folge=[("ruhig", "g_nein")]),
    pl("Gewalt?", MB, 160, "gewalt", fill=WEISS, size=30, anker="m", bis="verweis"),
    ficon("tabler", "hand-stop", MB, 380, 100, beim("gewalt", "körperliche"), fuell=WEISS, bis="verweis"),
    pl("Sitzblockade", MB, 160, "verweis", fill=LILA, size=30, anker="m", anim="cut", bis="g_nein"),
    ficon("fluent-emoji-flat", "automobile", MB, 380, 140, "verweis", anim="cut", bis="g_nein"),
    pl("keine Berührung", MB, 160, "g_nein", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "hand-off", MB, 380, 100, "g_nein", fuell=WEISS, anim="cut"),
]))

# E Drohung ------------------------------------------------------------------------------------------------------------------------
folie([("drohung", f"{P1} › 1. Nötigungsmittel: Drohung"), ("uebel", f"{P1} › 1. Drohung: Übel"),
       ("geld", f"{P1} › 1. Drohung: 1.500 € bleiben aus"), ("einfluss", f"{P1} › 1. Drohung: Einfluss des Täters")], rechts_frei([
    *tafel("drohung", "Nötigungsmittel: Drohung"),
    z("Drohung: ein künftiges Übel in Aussicht stellen,", 110, 180, "ddef", "Bold", 33),
    z("auf dessen Eintritt der Täter Einfluss hat", 110, 225, beim("ddef", "Einfluss"), "Bold", 33),
    z("oder zu haben vorgibt", 110, 270, beim("ddef", "vorgibt"), "Bold", 33),
    fund("OLG Köln, Urt. v. 11.6.2024 – 1 ORs 52/24, Rn. 43; BGH 1 StR 162/13, Rn. 65", 150, 320, beim("ddef", "vorgibt")),
    z("Übel: künftige nachteilige Veränderung der Außenwelt", 110, 385, "uebel", size=33),
    fund("BGH, Beschl. v. 5.9.2013 – 1 StR 162/13, Rn. 64", 150, 432, beim("uebel", "Außenwelt")),
    z("Gesine bekäme ihre 1.500 € nicht", 175, 500, "geld", "Bold", 33),
    ok(135, 520, beim("geld", "nicht"), gr=18),
    z("darüber entscheidet allein Gernot", 175, 560, "einfluss", "Bold", 33),
    ok(135, 580, beim("einfluss", "Gernot"), gr=18),
    *paar("drohung", gs_folge=[("sorge", "geld")], ge_folge=[("ernst", "ddef"), ("still", "einfluss")]),
    pl("Drohung?", MB, 160, "drohung", fill=WEISS, size=30, anker="m", bis="ddef"),
    pl("künftiges Übel", MB, 160, "ddef", fill=WEISS, size=30, anker="m", anim="cut", bis="geld"),
    ficon("tabler", "hourglass", MB, 380, 90, "ddef", fuell=GELB, bis="geld"),
    pl("1.500 € bleiben aus", MB, 160, "geld", fill=GELB, size=30, anker="m", anim="cut", bis="einfluss"),
    ficon("fluent-emoji-flat", "euro-banknote", MB, 380, 130, "geld", anim="cut", bis="einfluss"),
    pl("Gernot entscheidet", MB, 160, "einfluss", fill=BLAU, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "key", MB, 380, 100, "einfluss", anim="cut"),
]))

# F Drohung mit einem Unterlassen ------------------------------------------------------------------------------------------------------
folie([("unterl", f"{P1} › 1. Drohung mit einem Unterlassen"), ("pflicht", f"{P1} › 1. Unterlassen: Pflicht zur Rückzahlung")], rechts_frei([
    *tafel("unterl", "Drohung mit einem Unterlassen"),
    z("Gernot droht, nicht zu zahlen", 110, 180, beim("unterl", "nicht"), "Bold", 34),
    z("Auch mit einem Unterlassen kann man drohen,", 110, 260, "unterl2", size=33),
    z("sogar ohne Pflicht zum Handeln", 110, 305, beim("unterl2", "sogar"), size=33),
    fund("OLG Köln, Urt. v. 11.6.2024 – 1 ORs 52/24, Rn. 43, 46", 150, 355, beim("unterl2", "verpflichtet")),
    fl_block(110, 420, 1040, 125, GELB, "pflicht", [("Erst recht hier: Gernot muss die Kaution", "ExtraBold", 34, INK),
                                                   ("zurückzahlen", "ExtraBold", 34, INK)]),
    *paar("unterl", gs="sorge", ge="ernst", ge_folge=[("skeptisch", "pflicht")]),
    pl("nicht zahlen", MB, 160, "unterl", fill=WEISS, size=30, anker="m", bis="unterl2"),
    ficon("tabler", "cash-off", MB, 380, 110, beim("unterl", "nicht"), fuell=GELB, bis="pflicht"),
    pl("Unterlassen genügt", MB, 160, "unterl2", fill=WEISS, size=30, anker="m", anim="cut", bis="pflicht"),
    pl("Pflicht: zurückzahlen", MB, 160, "pflicht", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("tabler", "scale", MB, 380, 110, "pflicht", fuell=GELB, anim="cut"),
]))

# G empfindliches Übel ----------------------------------------------------------------------------------------------------------------
folie([("empf", f"{P1} › 1. Drohung: empfindliches Übel?"), ("besonnen", f"{P1} › 1. besonnene Selbstbehauptung?"),
       (beim("e_ja", "empfindlich"), f"{P1} › 1. empfindliches Übel (+)")], rechts_frei([
    *tafel("empf", "Empfindliches Übel"),
    z("Nachteil so erheblich, dass seine Ankündigung", 110, 180, "edef", "Bold", 33),
    z("die Bedrohte im Sinne des Täterverlangens", 110, 225, beim("edef", "Bedrohte"), "Bold", 33),
    z("motivieren kann", 110, 270, beim("edef", "motivieren"), "Bold", 33),
    fund("BGH, Beschl. v. 5.9.2013 – 1 StR 162/13, Rn. 68", 150, 318, beim("edef", "motivieren")),
    z("anders nur, wenn von ihr in ihrer Lage erwartet", 110, 385, "besonnen", size=33),
    z("werden kann, dass sie der Drohung in besonnener", 110, 430, beim("besonnen", "dass"), size=33),
    z("Selbstbehauptung standhält", 110, 475, beim("besonnen", "Selbstbehauptung"), size=33),
    fund("BGH 1 StR 162/13, Rn. 70", 150, 523, beim("besonnen", "Selbstbehauptung")),
    z("Gesine: keine solchen Besonderheiten", 175, 585, "e_ja", "Bold", 33),
    ok(135, 605, beim("e_ja", "Besonderheiten"), gr=18),
    fl_block(110, 650, 1040, 90, GRUENHELL, beim("e_ja", "empfindlich"), [("1.500 €: empfindliches Übel (+)", "ExtraBold", 36, INK)]),
    *paar("empf", gs="sorge", gs_folge=[("ernst", "e_ja")], ge="still"),
    pl("empfindlich?", MB, 160, "empf", fill=WEISS, size=30, anker="m", bis="besonnen"),
    ficon("tabler", "scale", MB, 380, 110, "edef", fuell=WEISS, bis="besonnen"),
    pl("standhalten?", MB, 160, "besonnen", fill=WEISS, size=30, anker="m", anim="cut", bis=beim("e_ja", "empfindlich")),
    ficon("tabler", "shield", MB, 380, 100, "besonnen", fuell=WEISS, anim="cut", bis=beim("e_ja", "empfindlich")),
    pl("empfindlich (+)", MB, 160, beim("e_ja", "empfindlich"), fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "euro-banknote", MB, 380, 130, beim("e_ja", "empfindlich"), anim="cut"),
]))

# H Nötigungserfolg, Kausalität, Vorsatz ------------------------------------------------------------------------------------------------
folie([("erfolg", f"{P1} › 2. Nötigungserfolg"), ("kausal", f"{P1} › 3. Kausalität"),
       ("vorsatz", f"{P1} › subjektiv: Vorsatz"), ("tb_ja", f"{P1} (+)")], rechts_frei([
    *tafel("erfolg", "Erfolg, Kausalität, Vorsatz"),
    z("Nötigungserfolg: eine Handlung", 110, 180, beim("erfolg", "Handlung"), "Bold", 34),
    z("Gesine zieht die Beschwerde zurück", 150, 225, beim("erfolg", "zieht"), size=33),
    z("Kausalität: gerade wegen der Drohung", 110, 305, "kausal", "Bold", 34),
    z("Vorsatz: Gernot will genau diese Rücknahme", 110, 385, "vorsatz", "Bold", 34),
    fl_block(110, 460, 1040, 90, GRUENHELL, "tb_ja", [("Tatbestand (+)", "ExtraBold", 36, INK)]),
    *paar("erfolg", gs="muede", ge="ernst", ge_folge=[("still", "vorsatz")]),
    pl("Handlung", MB, 160, "erfolg", fill=BLAU, size=30, anker="m", bis="kausal"),
    ficon("fluent-emoji-flat", "envelope-with-arrow", MB, 380, 110, beim("erfolg", "zieht"), bis="kausal"),
    pl("wegen der Drohung", MB, 160, "kausal", fill=WEISS, size=30, anker="m", anim="cut", bis="vorsatz"),
    ficon("tabler", "link", MB, 380, 100, "kausal", fuell=WEISS, anim="cut", bis="vorsatz"),
    pl("Vorsatz", MB, 160, "vorsatz", fill=WEISS, size=30, anker="m", anim="cut", bis="tb_ja"),
    ficon("tabler", "brain", MB, 380, 100, "vorsatz", fuell=GELB, anim="cut"),
    pl("Tatbestand (+)", MB, 160, "tb_ja", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# I Rechtswidrigkeit in zwei Stufen, Wortlaut § 240 Abs. 2 ------------------------------------------------------------------------------
W2 = [[("„Rechtswidrig ist die Tat, wenn die Anwendung der Gewalt oder", 0)],
      [("die ", 0), ("Androhung des Übels", "a"), (" zu dem ", 0), ("angestrebten Zweck", "b"), (" als", 0)],
      [("verwerflich", "c"), (" anzusehen ist.“", 0)]]
folie([("rw", f"{PR}"), ("rf", f"{PR} › 1. Rechtfertigungsgründe"), ("abs2", f"{PR} › 2. Verwerflichkeit, § 240 Abs. 2"),
       ("sozial", f"{PR} › 2. Verwerflichkeit: sozial unerträglich")], rechts_frei([
    *tafel("rw", "Rechtswidrigkeit in zwei Stufen"),
    z("1. allgemeine Rechtfertigungsgründe:", 110, 175, "rf", "Bold", 33),
    z("Notwehr, Notstand: liegen fern", 150, 218, beim("rf", "Notwehr"), size=33),
    z("2. Verwerflichkeit, § 240 Abs. 2 StGB", 110, 280, "abs2", "Bold", 33),
    *wortlaut(110, 330, 1040, 150, "abs2", W2, 30, {"a": beim("abs2", "Androhung"), "b": beim("abs2", "angestrebten"),
                                                    "c": beim("abs2", "verwerflich")}, "§ 240 Abs. 2 StGB"),
    z("verwerflich: Verquickung von Mittel und Zweck", 110, 540, "sozial", "Bold", 33),
    z("mit den Grundsätzen eines geordneten", 110, 585, beim("sozial", "Grundsätzen"), size=33),
    z("Zusammenlebens unvereinbar: „sozial unerträglich“", 110, 630, beim("sozial", "Zusammenlebens"), size=33),
    fund("BGH, Beschl. v. 5.9.2013 – 1 StR 162/13, Rn. 74", 150, 680, beim("sozial", "sozial")),
    *paar("rw", gs="ernst", ge="ernst", ge_folge=[("still", "sozial")]),
    pl("2 Stufen", MB, 160, "rw", fill=WEISS, size=30, anker="m", bis="rf"),
    pl("Stufe 1", MB, 160, "rf", fill=WEISS, size=30, anker="m", anim="cut", bis="abs2"),
    ficon("tabler", "shield", MB, 380, 100, "rf", fuell=WEISS, bis="abs2"),
    pl("Stufe 2", MB, 160, "abs2", fill=GELB, size=30, anker="m", anim="cut", bis="sozial"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 130, "abs2", anim="cut", bis="sozial"),
    pl("sozial unerträglich?", MB, 160, "sozial", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("tabler", "alert-triangle", MB, 380, 110, "sozial", fuell=ROT, anim="cut"),
]))

# J Mittel-Zweck-Relation ------------------------------------------------------------------------------------------------------------------
folie([("mz", f"{PR} › 2. Mittel-Zweck-Relation"), ("mittel", f"{PR} › 2. Mittel: Geld zurückhalten"),
       ("zweck", f"{PR} › 2. Zweck: Rücknahme der Beschwerde"), ("konnex", f"{PR} › 2. kein Zusammenhang"),
       (beim("v_ja", "verwerflich"), f"{PR} › 2. verwerflich (+)")], rechts_frei([
    *tafel("mz", "Mittel-Zweck-Relation"),
    karte(110, 180, 505, 190, "mittel", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Mittel:", 135, 195, "mittel", "ExtraBold", 32, rechts=600),
    z("Gernot hält Geld", 135, 245, beim("mittel", "hält"), "Bold", 32, rechts=600),
    z("zurück, das er schuldet", 135, 290, beim("mittel", "schuldet"), "Bold", 32, rechts=600),
    karte(645, 180, 505, 190, "zweck", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Zweck:", 670, 195, "zweck", "ExtraBold", 32, rechts=1135),
    z("Gesine soll ihre", 670, 245, beim("zweck", "Gesine"), "Bold", 32, rechts=1135),
    z("Beschwerde zurückziehen", 670, 290, beim("zweck", "Beschwerde"), "Bold", 32, rechts=1135),
    z("kein Zusammenhang zwischen Übel und Zweck:", 110, 410, beim("konnex", "Fehlt"), "Bold", 33),
    z("spricht für die Verwerflichkeit", 110, 455, beim("konnex", "spricht"), "Bold", 33),
    fund("OLG Hamm, Beschl. v. 14.12.2021 – 7 U 8/21, Rn. 9", 150, 503, beim("konnex", "spricht")),
    z("Lehre: Inkonnexität", 110, 560, "inkon", "ExtraBold", 33),
    z("fremdes Geld als Druckmittel gegen eine Beschwerde", 175, 630, "v_ja", size=33),
    fl_block(110, 690, 1040, 90, GRUENHELL, beim("v_ja", "verwerflich"), [("verwerflich (+)", "ExtraBold", 36, INK)]),
    *paar("mz", gs="ernst", ge="ernst", ge_folge=[("skeptisch", "konnex"), ("still", "v_ja")]),
    pl("Mittel und Zweck", MB, 160, "mz", fill=WEISS, size=30, anker="m", bis="mittel"),
    pl("Geld zurückhalten", MB, 160, "mittel", fill=BLAU, size=30, anker="m", anim="cut", bis="zweck"),
    ficon("tabler", "cash-off", MB, 380, 110, "mittel", fuell=BLAU, bis="zweck"),
    pl("Beschwerde zurückziehen", MB, 160, "zweck", fill=LILA, size=30, anker="m", anim="cut", bis="konnex"),
    ficon("fluent-emoji-flat", "classical-building", MB, 390, 140, "zweck", anim="cut", bis="konnex"),
    pl("kein Zusammenhang", MB, 160, "konnex", fill=ROTHELL, size=30, anker="m", anim="cut", bis=beim("v_ja", "verwerflich")),
    ficon("fluent-emoji-flat", "broken-chain", MB, 380, 120, beim("konnex", "nichts"), anim="cut"),
    pl("verwerflich (+)", MB, 160, beim("v_ja", "verwerflich"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# K Gegenfall: Klage auf die Miete --------------------------------------------------------------------------------------------------
folie([("gegen", "Gegenfall · Klage auf die offene Miete"), ("gegen2", "Gegenfall · Mittel und Zweck hängen zusammen"),
       (beim("gegen2", "Verwerflich"), "Gegenfall · nicht verwerflich")], rechts_frei([
    *tafel("gegen", "Gegenfall", fill=BLAUHELL),
    z("Gesine schuldet noch eine Monatsmiete,", 110, 180, beim("gegen", "Gesine"), "Bold", 34),
    z("Gernot droht mit einer Klage", 110, 225, beim("gegen", "droht"), "Bold", 34),
    z("Mittel und Zweck hängen zusammen", 175, 320, "gegen2", "Bold", 34),
    ok(135, 340, "gegen2", gr=18),
    z("Gernot hat einen Anspruch", 175, 380, beim("gegen2", "Gernot"), "Bold", 34),
    ok(135, 400, beim("gegen2", "Gernot"), gr=18),
    fund("OLG Hamm 7 U 8/21, Rn. 9; BGH, Beschl. v. 10.6.2025 – 3 StR 561/24, Rn. 10", 150, 435, beim("gegen2", "Anspruch")),
    fl_block(110, 495, 1040, 90, WEISS, beim("gegen2", "Verwerflich"), [("nicht verwerflich", "ExtraBold", 36, INK)]),
    *paar("gegen", gs="ernst", ge="ruhig"),
    pl("offene Miete", MB, 160, beim("gegen", "Monatsmiete"), fill=WEISS, size=30, anker="m", bis=beim("gegen", "Klage")),
    ficon("fluent-emoji-flat", "receipt", MB, 380, 100, beim("gegen", "Monatsmiete"), bis=beim("gegen", "Klage")),
    ficon("tabler", "gavel", MB, 380, 110, beim("gegen", "Klage"), fuell=GELB, anim="cut", bis="gegen2"),
    pl("Klage", MB, 160, beim("gegen", "Klage"), fill=WEISS, size=30, anker="m", anim="cut", bis="gegen2"),
    pl("Zusammenhang", MB, 160, "gegen2", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "link", MB, 380, 110, "gegen2", anim="cut"),
]))

# L Schuld, § 240 Abs. 4, Ergebnis ----------------------------------------------------------------------------------------------------
folie([("schuld", "A. § 240 StGB › III. Schuld"), ("abs4", "A. § 240 StGB › IV. besonders schwerer Fall, § 240 Abs. 4"),
       ("erg", "Ergebnis · Gernot: Nötigung, § 240 StGB")], rechts_frei([
    *tafel("schuld", "Schuld, Abs. 4, Ergebnis"),
    ok(135, 200, beim("schuld", "schuldhaft"), gr=18),
    z("III. Schuld (+)", 175, 180, beim("schuld", "schuldhaft"), "Bold", 34),
    z("IV. besonders schwerer Fall, § 240 Abs. 4:", 175, 260, "abs4", "Bold", 34),
    z("etwa Missbrauch als Amtsträger", 175, 305, beim("abs4", "Missbrauch"), size=33),
    nein(135, 360, beim("abs4", "liegt"), gr=18),
    z("liegt nicht vor", 175, 345, beim("abs4", "liegt"), size=33),
    karte(110, 440, 1040, 170, "erg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Ergebnis: Gernot ist strafbar", 140, 460, "erg", "ExtraBold", 36),
    z("wegen Nötigung, § 240 Abs. 1 StGB", 140, 525, beim("erg", "Nötigung"), "ExtraBold", 34),
    *figur_kette("GE", XS, "schuld", "ernst", [("still", "erg")]),
    pl("Schuld (+)", XS, 160, beim("schuld", "schuldhaft"), fill=WEISS, size=30, anker="m", bis="abs4"),
    pl("Abs. 4 (−)", XS, 160, "abs4", fill=ROTHELL, size=30, anker="m", anim="cut", bis="erg"),
    pl("§ 240 StGB", XS, 160, "erg", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "gavel", XS, 380, 110, "erg", fuell=GELB),
]))

# M Abgrenzung: Erpressung § 253 ------------------------------------------------------------------------------------------------------
folie([("erpr", "Abgrenzung · Erpressung, § 253 StGB?"), (beim("erpr", "scheidet"), "Abgrenzung · Erpressung, § 253 StGB (−)")], rechts_frei([
    *tafel("erpr", "Abgrenzung: Erpressung, § 253 StGB", size=44),
    z("Erpressung: scheidet aus", 110, 180, beim("erpr", "scheidet"), "ExtraBold", 34),
    nein(135, 280, "erpr2", gr=18),
    z("kein Vermögensnachteil für Gesine:", 175, 260, "erpr2", "Bold", 34),
    z("Rücknahme der Beschwerde", 175, 305, beim("erpr2", "Beschwerde"), size=33),
    nein(135, 400, "erpr3", gr=18),
    z("keine Bereicherungsabsicht:", 175, 380, "erpr3", "Bold", 34),
    z("Gernot will die Kaution nicht behalten", 175, 425, beim("erpr3", "Kaution"), size=33),
    fl_block(110, 500, 1040, 90, ROTHELL, beim("erpr3", "Bereicherungsabsicht"), [("§ 253 StGB (−)", "ExtraBold", 36, INK)]),
    *paar("erpr", gs="ruhig", ge="ruhig", ge_folge=[("ernst", "erpr3")]),
    pl("§ 253 StGB?", MB, 160, "erpr", fill=WEISS, size=30, anker="m", bis="erpr2"),
    pl("kein Vermögensnachteil", MB, 160, "erpr2", fill=ROTHELL, size=28, anker="m", anim="cut", bis="erpr3"),
    ficon("fluent-emoji-flat", "envelope", MB, 380, 100, "erpr2", bis="erpr3"),
    pl("Kaution nicht behalten", MB, 160, "erpr3", fill=ROTHELL, size=28, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "euro-banknote", MB, 380, 130, "erpr3", anim="cut"),
]))

# N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Rechtswidrigkeit in zwei Stufen"), ("tipp3", "Klausurtipp · Verwerflichkeit positiv feststellen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Rechtswidrigkeit in zwei Stufen prüfen", 200, 200, beim("tipp", "Rechtswidrigkeit"), "Bold", 34),
    z("1. allgemeine Rechtfertigungsgründe", 200, 290, "tipp2", "ExtraBold", 36),
    z("2. greift keiner: Verwerflichkeit nach", 200, 380, "tipp3", "ExtraBold", 36),
    z("Abs. 2 positiv feststellen", 240, 432, beim("tipp3", "positiv"), "ExtraBold", 36),
    z("Das Nötigungsmittel allein zeigt die", 200, 530, "tipp4", size=34),
    z("Verwerflichkeit noch nicht an.", 200, 578, beim("tipp4", "Verwerflichkeit"), size=34),
    fund("BGH, Urt. v. 25.2.2021 – 3 StR 204/20, Rn. 31", 240, 630, beim("tipp4", "noch")),
    *redet("LX_warnt", LXX, BR, FR_H + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema ---------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PS_ = "Klausurschema"
folie([("sch", PS_), ("k1", f"{PS_} › I. Tatbestand: objektiv"), ("k1a", f"{PS_} › I. 1. Nötigungsmittel"),
       ("k1b", f"{PS_} › I. 2. Nötigungserfolg"), ("k1c", f"{PS_} › I. 3. Kausalität"), ("k2", f"{PS_} › I. subjektiv: Vorsatz"),
       ("k3", f"{PS_} › II. Rechtswidrigkeit"), ("k3a", f"{PS_} › II. 1. Rechtfertigungsgründe"),
       ("k3b", f"{PS_} › II. 2. Verwerflichkeit, § 240 Abs. 2"), ("k4", f"{PS_} › III. Schuld"),
       ("k5", f"{PS_} › IV. besonders schwerer Fall, § 240 Abs. 4")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Nötigung, § 240 StGB", 110, 90, "sch", 52),
    z("I. Tatbestand", K1, 185, "k1", "Bold", 38, rechts=1820),
    z("objektiver Tatbestand:", K2, 245, beim("k1", "Objektiv"), "Bold", 34, rechts=1820),
    z("1. Nötigungsmittel: Gewalt oder Drohung mit einem empfindlichen Übel", K3, 297, "k1a", size=34, rechts=1820),
    z("2. Nötigungserfolg", K3, 349, "k1b", size=34, rechts=1820),
    z("3. Kausalität", K3, 401, "k1c", size=34, rechts=1820),
    z("subjektiver Tatbestand: Vorsatz", K2, 461, "k2", "Bold", 34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 535, "k3", "Bold", 38, rechts=1820),
    z("1. allgemeine Rechtfertigungsgründe", K3, 595, "k3a", size=34, rechts=1820),
    z("2. Verwerflichkeit nach § 240 Abs. 2", K3, 647, "k3b", size=34, rechts=1820),
    z("III. Schuld", K1, 720, "k4", "Bold", 38, rechts=1820),
    z("IV. besonders schwerer Fall, § 240 Abs. 4", K1, 790, "k5", "Bold", 38, rechts=1820),
])

# P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nötigung braucht ", 0), ("Gewalt", "a"), (" oder eine", 0)], [("Drohung mit einem ", 0),
                 ("empfindlichen Übel", "b"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "Gewalt"), "b": beim("merke", "empfindlichen")}),
    *markertext([[("Auch die Drohung, ", 0), ("nicht zu zahlen", "c"), (", genügt.", 0)]], 750, 480, 44, "m2",
                {"c": beim("m2", "nicht")}),
    *markertext([[("Rechtswidrig ist sie nur, wenn das ", 0), ("Mittel", "d")], [("zum angestrebten ", 0), ("Zweck", "e"), (" ", 0),
                 ("verwerflich", "f"), (" ist.", 0)]], 750, 610, 44, "m3",
                {"d": beim("m3", "Mittel"), "e": beim("m3", "Zweck"), "f": beim("m3", "verwerflich")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
