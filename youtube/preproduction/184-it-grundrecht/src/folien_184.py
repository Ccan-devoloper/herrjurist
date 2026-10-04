"""Folge 184 · Staatstrojaner und IT-Grundrecht: Darf die Polizei mitlesen? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall (geteiltes Bild: Herr Weinhold am Laptop | Kommissar Hollstein im Büro), B Sachverhalt,
C1–C4 Schutzbereich (Art. 10 GG mit Wortlaut, Art. 13 GG mit Wortlaut, informationelle Selbstbestimmung als Verweis auf das
Video zum Volkszählungsurteil, Schutzlücke und IT-Grundrecht nach BVerfGE 120, 274), D1 Quellen-TKÜ (§ 100a Abs. 1 S. 2 StPO als
Wortlautkarte, S. 3), D2 Maßstab 2008/2025, D3 Online-Durchsuchung (§ 100b Abs. 1 StPO als Wortlautkarte), E1 Rechtfertigung
(Gefahrenabwehr/Strafverfolgung), E2 Richtervorbehalt und Kernbereich, E3 seit 2025 (Trojaner II), F1 Lösung (Tafel), F2 zurück
am Laptop und im Büro, G Klausurtipp (Lexi), H Klausurschema, I Merksatz (Lexi).
Polizei neutral (Kommissar in Zivil, keine Uniform, kein Logo), Software als Holzpferdchen (Tabler horse-toy), Chats nur als
Sprechblasen-Icons, kein echtes Messenger-Logo. Geräusch nur bei sichtbarer Handlung: Tippen am Laptop (Freesound CC0,
../geraeusche_herkunft.json).
Hilfsfunktionen (glyphen, z, pl, tafel, fb, wl_links, zitatkarte, redet mit hörbarem Wortende, kette, stufen, wechsel, icons …)
als eigene Kopie aus Folge 181 (gemeinsame Dateien unverändert); neu: stuhl(), sitzt(), paar(), zimmer(). Zahlen auf Tafeln,
Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
from engine import El, F

bausteine.FIGORDNER = "op_184/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (214, 214, 210, 255)
GRAUD = (176, 176, 170, 255)
HOLZ = (214, 160, 110, 255)
DAUER = bausteine._cj()["dauer"]

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e) – wie Folge 161
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

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
    e = pille(glyphen(text), *a, **k)
    assert e.x >= 30 and e.x + e.sprite.width <= 1890, f"Pille ragt aus dem Bild: {text}"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Block mit Zeilen; Zeilenabstand passend zur Schriftgröße, Textbreite geprüft."""
    from engine import block
    for zz in zeilen:
        glyphen(zz[0])
        assert F(zz[1], zz[2]).getlength(zz[0]) <= w - 30, f"Blockzeile zu breit: {zz[0]}"
    lh = int(max(zz[2] for zz in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    return block(x, y, w, h, fill, None, cue, textsize=lh, rund=rund, rand=INK, randbreite=5, anim=anim, d=d, bis=bis,
                 zeilen=zeilen)


def wl_links(zeilen, x, y, size, cue, hl, rechts=1170, lh=1.28, marker=GELB):
    """Linksbündiger Wortlaut (wörtliches Zitat nach gesetze-im-internet.de, Abruf 04.10.2026) mit Textmarker zum gesprochenen Wort.
    zeilen = [[(text, Schlüssel|0), …], …]; hl = {Schlüssel: Cue}. Gibt (Elemente, y_ende) zurück."""
    fr, fbold = F("Regular", size), F("ExtraBold", size)
    breite = 0
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
        breite = max(breite, sum((fbold if h else fr).getlength(t) for t, h in toks))
    assert x + breite <= rechts, f"Wortlaut zu breit ({x + breite:.0f} > {rechts}): {zeilen}"
    hgt = int(len(zeilen) * size * lh + size * 0.5)
    im = Image.new("RGBA", (int(breite) + 20, hgt)); dr = ImageDraw.Draw(im); ov = {}
    yy = 0
    for toks in zeilen:
        xx = 4
        for t, h in toks:
            f = fbold if h else fr
            tw = f.getlength(t)
            if h:
                if h not in ov:
                    ov[h] = Image.new("RGBA", im.size)
                od = ImageDraw.Draw(ov[h])
                od.rounded_rectangle((xx - 5, yy + size * 0.45, xx + tw + 5, yy + size * 1.12), 8, fill=marker)
                od.text((xx, yy), t, font=f, fill=INK)
            dr.text((xx, yy), t, font=f, fill=INK)
            xx += tw
        yy += size * lh
    els = [El(im, x - 4, y, cue, "fade", 0.0, name="wortlaut")]
    for k_, oim in ov.items():
        els.append(El(oim, x - 4, y, hl[k_], "fade", 0.0, name="marker:" + str(k_)))
    return els, y + len(zeilen) * size * lh


def zitatkarte(zeilen, x, y, size, cue, hl, fill=ZITAT):
    """Wortlautkarte: Karte + linksbündiger Wortlaut mit Markern; gibt (Elemente, y_ende) zurück."""
    els, y1 = wl_links(zeilen, x + 30, y + 18, size, cue, hl, rechts=x + 1040 - 16)
    return [karte(x, y, 1040, int(y1 - y + 22), cue, fill=fill, rund=18, schatten=6, rand=4)] + els, y1 + 22


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (wie 161)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_184/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


# --- Eigene Hilfsfunktion (wie Folge 127/138): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
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


BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren
XE = 1600                               # eine Figur
IX = 1580                               # Requisiten rechts (Folien ohne Figuren)
FARBE = {"WH": GRUEN, "HS": BLAU}
NAME = {"WH": "Herr Weinhold", "HS": "Kommissar Hollstein"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def einzeln(p, cue, folge, x=XE):
    """Eine Figur rechts neben der Tafel (blickt zur Tafel) mit Namensschild."""
    return kette(p + "_", x, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], x, BR, cue, FARBE[p], d=0.2)]


def stufen(folge, x, unten, hoehe, rede=None, erst="pop", ende=None):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: 1} für Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else ende
        if rede and n in rede:
            els += redet(n, x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(n, x, unten, hoehe, c, anim=(erst if i == 0 else "cut"), bis=b))
    return els


def wechsel(texte, cx, y, size=28, fill=WEISS, anker="m", ende=None):
    """Pillen nacheinander an derselben Stelle: texte = [(Text, Cue, Füllung|None), …]."""
    els = []
    for i, (t, c, f) in enumerate(texte):
        b = texte[i + 1][1] if i + 1 < len(texte) else ende
        els.append(pl(t, cx, y, c, fill=f or fill, size=size, anker=anker, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def icons(folge, cx, unten, breite, ende=None):
    """Requisiten nacheinander an derselben Stelle: folge = [(set, name, Cue, Füllung), …]."""
    els = []
    for i, (s, n, c, f) in enumerate(folge):
        b = folge[i + 1][2] if i + 1 < len(folge) else ende
        els.append(ficon(s, n, cx, unten, breite, c, fuell=f, anim=("pop" if i == 0 else "cut"), bis=b))
    return els






# --- Eigene Ergänzungen Folge 184 ---------------------------------------------------------------------------------------
HC = "fluent-emoji-high-contrast"
HOLZ2 = (214, 170, 120, 255)
SH = 330                                            # Höhe der sitzenden Figur (Herr Weinhold, sitting/mid-2)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def kasten(x, y, w, h, cue, fill):
    return karte(x, y, w, h, cue, fill=fill, rund=18, schatten=6, rand=4)


def stuhl(x, unten, cue, rechts=False, anim="pop", bis=None, hoehe=SH):
    """Hocker unter der sitzenden Figur (Phosphor chair, gespiegelt je Blickrichtung)."""
    return ficon("ph", "chair", x + (-0.16 if rechts else 0.16) * hoehe, unten, int(hoehe * 0.62), cue, fuell=HOLZ2,
                 spiegeln=not rechts, anim=anim, bis=bis)


def sitzt(cue, folge, x=XE, unten=BR, rechts=False, schild=True, d=0.0, bis_=None):
    """Herr Weinhold sitzt (Hocker + Mimikfolge [(suffix, cue)…]); rechts=True blickt nach rechts."""
    r = "_r" if rechts else ""
    els = [stuhl(x, unten, cue, rechts, bis=bis_)]
    els += kette("WH_", x, [(folge[0][0] + r, cue)] + [(s + r, c) for s, c in folge[1:]], bis_=bis_, d=d, hoehe=SH, unten=unten)
    if schild:
        els.append(namensschild(NAME["WH"], x, unten, cue, FARBE["WH"], d=0.2, bis=bis_))
    return els


def paar(cue, fw, fh, xw=1390, xh=1700):
    """Herr Weinhold (sitzt, links) und Kommissar Hollstein (steht, rechts) neben der Tafel, beide blicken zur Tafel."""
    return sitzt(cue, fw, x=xw) + kette("HS_", xh, [(fh[0][0], cue)] + list(fh[1:]), d=0.2) + \
        [namensschild(NAME["HS"], xh, BR, cue, FARBE["HS"], d=0.3)]


# A Fall: Laptop von Herrn Weinhold | Büro von Kommissar Hollstein ----------------------------------------------------------
BODEN = 900
TRENN = 1180                                        # Trennlinie zwischen den beiden Orten
WHX, HSX = 330, 1640
DX = 700                                            # Schreibtisch mit Laptop
WHa = ("WH_redet_r", WHX, BODEN, SH)
HSa = ("HS_redet", HSX, BODEN, FR)
HSb = ("HS_beschluss", HSX, BODEN, FR)


def zimmer(cue, anim="cut"):
    """Boden, Trennlinie, Schreibtisch mit Laptop (links) und Büro mit Bildschirm (rechts); neutral, ohne Logos."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           linienzug([(TRENN, 120), (TRENN, BODEN - 10)], cue, breite=5, farbe=GRAUD)]
    tisch = ficon("tabler", "desk", DX, BODEN - 2, 380, cue, fuell=HOLZ, anim=anim)
    els += [tisch, ficon("tabler", "device-laptop", DX, tisch.y + 12, 190, cue, fuell=BLAUHELL, anim=anim),
            ficon("tabler", "lamp", DX + 130, tisch.y + 12, 80, cue, fuell=GELB, anim=anim),
            ficon("tabler", "device-desktop", 1340, BODEN - 260, 170, cue, fuell=WEISS, anim=anim),
            linienzug([(1250, BODEN - 260), (1430, BODEN - 260)], cue, breite=6, farbe=INK),
            linienzug([(1340, BODEN - 260), (1340, BODEN - 4)], cue, breite=6, farbe=INK)]
    return els, tisch.y


_za, TY = zimmer("fall")
LY = TY - 150                                       # Höhe über dem Laptop für Chat-Symbole
folie([("fall", "Fall · Der Laptop"), ("weinh", "Fall · Herr Weinhold"), ("holl", "Fall · Kommissar Hollstein"),
       ("frage", "Fall · Die Frage")], [
    *_za,
    pl("Laptop", DX, TY + 30, "fall", fill=WEISS, size=28, anker="m", bis="chat"),
    ficon("tabler", "horse-toy", DX - 210, TY - 60, 120, beim("fall", "Software"), fuell=HOLZ, bis="weinh"),
    pl("heimlich Software installieren", 600, 40, beim("fall", "heimlich"), fill=ROTHELL, size=32, anker="m", bis="verd"),
    ficon("tabler", "message-circle", DX - 40, LY, 90, beim("fall", "Chats"), fuell=WEISS, bis="frage"),
    pl("Chats mitlesen?", 600, 120, beim("fall", "Chats"), fill=WEISS, size=30, anker="m", bis="verd"),
    *stufen([("WH_ruhig_r", "weinh"), ("WH_tippt_r", "chat"), ("WH_redet_r", "w1"), ("WH_selbst_r", "holl"),
             ("WH_tippt_r", "frage")], WHX, BODEN, SH, rede={"WH_redet_r": 1}),
    stuhl(WHX, BODEN, "weinh", rechts=True),
    namensschild(NAME["WH"], WHX, BODEN, beim("weinh", "Herrn"), FARBE["WH"]),
    pl("Verdacht: Falschgeld, mit einer Bande", 600, 40, "verd", fill=GELB, size=32, anker="m", bis="w1"),
    ficon(HC, "euro-banknote", DX + 250, TY - 60, 110, beim("verd", "Falschgeld"), fuell=GRUENHELL, bis="w1"),
    pl("bestimmte Tatsachen", 600, 120, beim("verd", "Bestimmte"), fill=WEISS, size=30, anker="m", bis="w1"),
    szene(ficon("tabler", "message-circle", DX + 40, LY - 70, 80, "chat", fuell=GRUENHELL, bis="frage"), "184tippen*", 0.8,
          versatz=0.05),
    ficon("tabler", "lock", DX + 110, LY - 10, 70, beim("chat", "verschlüsselten"), fuell=GELB, bis="frage"),
    pl("verschlüsselter Messenger", 600, 40, beim("chat", "verschlüsselten"), fill=BLAUHELL, size=32, anker="m", bis="w1"),
    blase("sprech", 520, 190, "w1", 560, 200, inhalt=["Alles verschlüsselt.", "Da liest keiner mit."], textsize=34,
          figur=WHa, bis="holl"),
    # Büro: Kommissar Hollstein
    *stufen([("HS_ruhig", "holl"), ("HS_redet", "h1"), ("HS_entschlossen", "frage")], HSX, BODEN, FR, rede={"HS_redet": 1}),
    namensschild(NAME["HS"], HSX, BODEN, "holl", FARBE["HS"], d=0.2),
    ficon("tabler", "lock", 1340, BODEN - 330, 60, beim("h1", "verschlüsselt"), fuell=GELB, bis="frage"),
    blase("sprech", 640, 250, "h1", 1500, 210, inhalt=["Abhören bringt uns nichts, die Chats", "sind verschlüsselt. Wir müssen",
          "direkt auf seinen Laptop."], textsize=31, figur=HSa, bis="frage"),
    pl("Darf der Staat heimlich in einen Computer eindringen?", 940, 40, "frage", fill=PINK, size=32, anker="m"),
    pl("Welches Grundrecht schützt davor?", 940, 120, beim("frage", "Und"), fill=PINK, size=32, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Bestimmte Tatsachen begründen den Verdacht, dass Herr Weinhold mit einer Bande Falschgeld herstellt. Die "
            "Absprachen laufen über einen verschlüsselten Messenger auf seinem Laptop."),
    glyphen("Kommissar Hollstein meint, normales Abhören bringe nichts. Die Ermittler wollen heimlich Software auf dem "
            "Laptop installieren: nur um die laufenden Chats mitzulesen oder um den ganzen Laptop zu durchsuchen."),
], "Welches Grundrecht schützt den Laptop? Ist der Zugriff zulässig?")

# C1 Erster Kandidat: Art. 10 GG ------------------------------------------------------------------------------------------
PS1 = "I. Schutzbereich"
W10 = [[("„Das Briefgeheimnis sowie das Post- und ", 0), ("Fernmeldegeheimnis", "a")], [("sind unverletzlich.“", 0)]]
_k10, _y10 = zitatkarte(W10, 110, 180, 34, "art10", {"a": beim("art10", "Fernmeldegeheimnis")})
folie([("art10", f"{PS1} › 1. Art. 10 GG: Fernmeldegeheimnis")], rechts_frei([
    *tafel("art10", "1. Kandidat: Art. 10 GG"),
    *_k10,
    fund("Art. 10 Abs. 1 GG", 110, int(_y10 + 10), "art10"),
    *okz("laufende Kommunikation über Distanz,", int(_y10 + 80), "lauf", "Bold", 34),
    z("auch im Internet", 185, int(_y10 + 130), beim("lauf", "Internet"), size=34),
    *neinz("Daten, die nach Abschluss der Kommunikation", int(_y10 + 215), "gesp", size=34),
    z("auf dem Gerät liegen", 185, int(_y10 + 265), beim("gesp", "Gerät"), size=34),
    *neinz("Durchsuchen des ganzen Systems", int(_y10 + 345), "ganz", size=34),
    fund("BVerfGE 120, 274 (Online-Durchsuchung), Rn. 183–186", 110, int(_y10 + 425), "ganz"),
    *icons([("tabler", "mail", "art10", WEISS), ("tabler", "messages", "lauf", GRUENHELL),
            ("tabler", "database", "gesp", BLAUHELL), ("tabler", "file-search", "ganz", ROTHELL)], IX, 470, 170),
    *sitzt("art10", [("ruhig",), ("denkt", "lauf"), ("selbst", "gesp"), ("sorge", "ganz")], x=1600),
]))

# C2 Zweiter Kandidat: Art. 13 GG -----------------------------------------------------------------------------------------
W13 = [[("„Die ", 0), ("Wohnung", "a"), (" ist unverletzlich.“", 0)]]
_k13, _y13 = zitatkarte(W13, 110, 180, 36, "art13", {"a": beim("art13", "Wohnung")})
folie([("art13", f"{PS1} › 2. Art. 13 GG: Wohnung")], rechts_frei([
    *tafel("art13", "2. Kandidat: Art. 13 GG"),
    *_k13,
    fund("Art. 13 Abs. 1 GG", 110, int(_y13 + 10), "art13"),
    *okz("geschützt: der Raum", int(_y13 + 85), "raum", "Bold", 34),
    *neinz("nicht das Gerät", int(_y13 + 150), beim("raum", "nicht"), "Bold", 34),
    *neinz("Zugriff über das Netz: unabhängig vom Standort", int(_y13 + 240), "fern", size=34),
    z("gerade bei einem Laptop", 185, int(_y13 + 290), beim("fern", "gerade"), size=34),
    fund("BVerfGE 120, 274, Rn. 191–195", 110, int(_y13 + 370), "fern"),
    *icons([("tabler", "home", "art13", HELL), ("tabler", "device-laptop", beim("raum", "nicht"), BLAUHELL),
            ("tabler", "world", "fern", BLAUHELL)], IX, 470, 170),
    *sitzt("art13", [("ruhig",), ("denkt", beim("raum", "nicht")), ("ernst", "fern")], x=1600),
]))

# C3 Informationelle Selbstbestimmung (Verweis auf das Video zum Volkszählungsurteil) --------------------------------------
folie([("ris", f"{PS1} › 3. informationelle Selbstbestimmung")], rechts_frei([
    *tafel("ris", "3. Informationelle Selbstbestimmung"),
    z("siehe Video „Volkszählungsurteil“", 110, 185, beim("ris", "Video"), size=34),
    *neinz("reicht hier nicht ganz aus", 285, "ris2", "Bold", 34),
    z("Wer in ein ganzes System eindringt, bekommt", 110, 380, "ris3", size=34),
    fb(110, 450, 1040, 90, ROTHELL, beim("ris3", "riesigen"), [("einen riesigen Datenbestand", "ExtraBold", 36, INK)]),
    fund("BVerfGE 120, 274, Rn. 196–200 (Anschluss an BVerfGE 65, 1)", 110, 570, beim("ris3", "riesigen")),
    *icons([("tabler", "user-shield", "ris", HELL), ("tabler", "database", beim("ris3", "riesigen"), ROTHELL)], IX, 470, 170),
    *sitzt("ris", [("ruhig",), ("denkt", "ris2"), ("schreck", beim("ris3", "riesigen"))], x=1600),
]))

# C4 Die Schutzlücke und das IT-Grundrecht (BVerfGE 120, 274) --------------------------------------------------------------
P8 = "I. Schutzbereich › 4. IT-Grundrecht"
folie([("luecke", f"{PS1} › Schutzlücke"), ("itgr", P8)], rechts_frei([
    *tafel("luecke", "Die Schutzlücke"),
    fb(110, 180, 1040, 80, ROTHELL, "luecke", [("Schutzlücke", "ExtraBold", 36, INK)]),
    z("BVerfG 2008: Fall zum Verfassungsschutz in NRW", 110, 290, "d08", "Bold", 33),
    z("Allgemeines Persönlichkeitsrecht, Art. 2 I i. V. m. Art. 1 I GG:", 110, 360, "itgr", size=32),
    fb(110, 420, 1040, 130, GELB, beim("itgr", "Grundrecht"), [("Grundrecht auf Gewährleistung der Vertraulichkeit", "ExtraBold", 31, INK),
                                                            ("und Integrität informationstechnischer Systeme", "ExtraBold", 31, INK)]),
    pl("kurz: IT-Grundrecht", 110, 575, beim("itgr", "IT"), fill=GELB, size=32),
    *okz("Vertraulichkeit: Daten bleiben vertraulich", 650, "vertr", size=33),
    *okz("Integrität: keine heimliche Infiltration", 705, "integr", size=33),
    fund("BVerfG, Urt. v. 27.2.2008 – 1 BvR 370/07, BVerfGE 120, 274, LS 1, Rn. 187, 201, 204", 110, 775, "itgr"),
    *icons([("tabler", "shield", "luecke", ROTHELL), ("tabler", "building-bank", "d08", WEISS),
            ("tabler", "shield-lock", beim("itgr", "Grundrecht"), GELB), ("tabler", "lock", "vertr", GELB),
            ("tabler", "device-laptop", "integr", GRUENHELL)], IX, 470, 170),
    *sitzt("luecke", [("sorge",), ("denkt", "d08"), ("ruhig", beim("itgr", "Grundrecht")), ("selbst", "integr")], x=1600),
]))

# D1 Quellen-TKÜ, § 100a Abs. 1 S. 2, 3 StPO (Wortlautkarte) ---------------------------------------------------------------
PQ = "II. Eingriff › Quellen-TKÜ, § 100a Abs. 1 S. 2, 3 StPO"
WQ = [[("„Die Überwachung und Aufzeichnung der Telekommunikation darf", 0)],
      [("auch in der Weise erfolgen, dass mit technischen Mitteln in von", 0)],
      [("dem Betroffenen genutzte informationstechnische Systeme", 0)],
      [("eingegriffen", "a"), (" wird, wenn dies ", 0), ("notwendig", "b"), (" ist, um die Überwachung", 0)],
      [("und Aufzeichnung ", 0), ("insbesondere in unverschlüsselter Form", "c"), (" zu", 0)],
      [("ermöglichen.“", 0)]]
_kq, _yq = zitatkarte(WQ, 110, 240, 30, "q1", {"a": beim("q1b", "eingreifen"), "b": beim("q1b", "nötig"),
                                              "c": beim("q1b", "unverschlüsselt")})
folie([("stpo", "II. Eingriff › Strafprozessordnung"), ("q1", PQ)], rechts_frei([
    *tafel("stpo", "Strafprozessordnung: Quellen-TKÜ"),
    z("§ 100a Abs. 1 Satz 2 StPO:", 110, 180, "q1", "Bold", 34),
    *_kq,
    fund("§ 100a Abs. 1 S. 2 StPO (gesetze-im-internet.de, Abruf 4.10.2026)", 110, int(_yq + 10), "q1"),
    z("Satz 3: auch gespeicherte Nachrichten, die schon bei der", 110, int(_yq + 70), "q2", "Bold", 32),
    z("Übertragung hätten überwacht werden können", 110, int(_yq + 115), beim("q2", "während"), "Bold", 32),
    *icons([("tabler", "gavel", "stpo", HELL), ("tabler", "horse-toy", "q1", HOLZ),
            ("tabler", "lock-open", beim("q1b", "unverschlüsselt"), GELB), ("tabler", "messages", "q2", BLAUHELL)],
           IX, 470, 170),
    *kette("HS_", 1600, [("ruhig", "stpo"), ("ernst", "q1"), ("entschlossen", beim("q1b", "unverschlüsselt")),
                         ("denkt", "q2")]),
    namensschild(NAME["HS"], 1600, BR, "stpo", FARBE["HS"], d=0.2),
]))

# D2 Maßstab der Quellen-TKÜ: 2008 und 2025 ------------------------------------------------------------------------------
folie([("q08", "I. Schutzbereich › Quellen-TKÜ: 2008"), ("q25", "I. Schutzbereich › Quellen-TKÜ: seit 2025")], rechts_frei([
    *tafel("q08", "Quellen-TKÜ: welches Grundrecht?"),
    fb(110, 180, 1040, 130, GRAU, "q08", [("2008: nur laufende Kommunikation", "ExtraBold", 33, INK),
                                         ("dann allein Art. 10", "Regular", 33, INK)]),
    fund("BVerfGE 120, 274, Rn. 190", 110, 325, "q08"),
    fb(110, 400, 1040, 130, GRUENHELL, "q25", [("2025: Eingriff in das eigene System", "ExtraBold", 33, INK),
                                              ("zugleich IT-Grundrecht", "Regular", 33, INK)]),
    fund("BVerfG, 24.6.2025 – 1 BvR 2466/19 (Trojaner I), LS 3, Rn. 93–110", 110, 545, "q25"),
    fb(110, 620, 1040, 90, GELB, "beide", [("geprüft an Art. 10 und am IT-Grundrecht", "ExtraBold", 34, INK)]),
    fund("BVerfG, 24.6.2025 – 1 BvR 180/23 (Trojaner II), LS 1, Rn. 172–174", 110, 725, "beide"),
    *paar("q08", [("ruhig",), ("denkt", "q25"), ("ernst", "beide")], [("ruhig",), ("staunt", "q25"), ("ernst", "beide")]),
]))

# D3 Online-Durchsuchung, § 100b Abs. 1 StPO (Wortlautkarte) ---------------------------------------------------------------
PO = "II. Eingriff › Online-Durchsuchung, § 100b StPO"
WO = [[("„Auch ohne Wissen des Betroffenen darf mit technischen Mitteln", 0)],
      [("in ein von dem Betroffenen genutztes informationstechnisches", 0)],
      [("System ", 0), ("eingegriffen", "a"), (" und dürfen ", 0), ("Daten daraus erhoben", "b")],
      [("werden (Online-Durchsuchung), wenn …“", 0)]]
_ko, _yo = zitatkarte(WO, 110, 240, 30, "od", {"a": beim("od1", "eingreifen"), "b": beim("od1", "Daten")})
folie([("od", PO)], rechts_frei([
    *tafel("od", "Online-Durchsuchung"),
    z("§ 100b Abs. 1 StPO:", 110, 180, "od", "Bold", 34),
    *_ko,
    fund("§ 100b Abs. 1 StPO (gesetze-im-internet.de, Abruf 4.10.2026)", 110, int(_yo + 10), "od"),
    z("also alles, was dort gespeichert ist", 110, int(_yo + 70), beim("od1", "also"), "Bold", 34),
    fb(110, int(_yo + 145), 1040, 80, GELB, "odm", [("Maßstab: IT-Grundrecht", "ExtraBold", 34, INK)]),
    *okz("zugleich Art. 10: auch laufende Kommunikation", int(_yo + 255), beim("odm", "zugleich"), size=34),
    fund("BVerfG, Trojaner II, LS 3, Rn. 241–243", 110, int(_yo + 320), beim("odm", "zugleich")),
    *icons([("tabler", "device-laptop", "od", BLAUHELL), ("tabler", "folders", beim("od1", "also"), GELB),
            ("tabler", "shield-lock", "odm", GELB)], IX, 470, 170),
    *paar("od", [("ruhig",), ("schreck", beim("od1", "also")), ("ernst", "odm")],
          [("ruhig",), ("entschlossen", "od1"), ("denkt", "odm")]),
]))

# E1 Rechtfertigung: Gefahrenabwehr und Strafverfolgung --------------------------------------------------------------------
PR = "III. Rechtfertigung"
folie([("schr", f"{PR} › nicht schrankenlos"), ("gef", f"{PR} › Gefahrenabwehr: konkrete Gefahr"),
       ("straf", f"{PR} › Strafverfolgung: besonders schwere Straftat")], rechts_frei([
    *tafel("schr", "III. Rechtfertigung"),
    z("nicht schrankenlos: Gefahrenabwehr", 110, 180, "schr", "Bold", 34),
    z("und Strafverfolgung", 110, 228, beim("schr", "Strafverfolgung"), "Bold", 34),
    kasten(110, 300, 1040, 250, "gef", BLAUHELL),
    z("Gefahrenabwehr: tatsächliche Anhaltspunkte einer", 140, 318, "gef", "Bold", 32, rechts=1140),
    z("konkreten Gefahr für ein überragend wichtiges Rechtsgut", 140, 366, beim("gef", "konkreten"), size=32, rechts=1140),
    z("Leib, Leben, Freiheit der Person; Grundlagen", 140, 430, "gut", size=32, rechts=1140),
    z("des Staates und der Existenz der Menschen", 140, 478, beim("gut", "Grundlagen"), size=32, rechts=1140),
    fund("BVerfGE 120, 274, LS 2, Rn. 207, 247; BVerfGE 141, 220 (BKAG), Rn. 212", 110, 565, "gut"),
    kasten(110, 630, 1040, 130, "straf", LILAHELL),
    z("Strafverfolgung: Verdacht einer", 140, 648, "straf", "Bold", 33, rechts=1140),
    z("besonders schweren Straftat", 140, 698, beim("straf", "Nötig"), "ExtraBold", 33, rechts=1140),
    fund("BVerfG, Trojaner II, Rn. 134, 204, 209", 110, 775, beim("straf", "Nötig")),
    *icons([("tabler", "scale", "schr", GELB), ("tabler", "shield", "gef", BLAUHELL), ("tabler", "heart", "gut", ROTHELL),
            ("tabler", "file-search", "straf", LILAHELL)], IX, 470, 170),
    *kette("HS_", 1600, [("ruhig", "schr"), ("ernst", "gef"), ("denkt", "gut"), ("entschlossen", "straf")]),
    namensschild(NAME["HS"], 1600, BR, "schr", FARBE["HS"], d=0.2),
]))

# E2 Richtervorbehalt und Kernbereich ------------------------------------------------------------------------------------
folie([("richt", f"{PR} › Richtervorbehalt"), ("kern", f"{PR} › Kernbereich privater Lebensgestaltung")], rechts_frei([
    *tafel("richt", "Richtervorbehalt und Kernbereich"),
    *okz("Richtervorbehalt: grundsätzlich vorher", 180, "richt", "Bold", 34),
    z("ein Richter", 185, 230, beim("richt", "Richter", 2), "Bold", 34),
    fund("BVerfGE 120, 274, LS 3, Rn. 257–259", 110, 290, beim("richt", "Richter", 2)),
    fb(110, 350, 1040, 130, ROTHELL, "kern", [("Kernbereich privater Lebensgestaltung:", "ExtraBold", 33, INK),
                                             ("absolut geschützt", "Regular", 33, INK)]),
    z("Höchstpersönliches, etwa tagebuchartige Dateien:", 110, 515, "kern2", size=33),
    z("möglichst gar nicht erheben", 110, 563, beim("kern2", "möglichst"), "Bold", 33),
    *neinz("doch erfasst: unverzüglich löschen, nicht verwerten", 640, "kern3", size=33),
    fund("BVerfGE 120, 274, Rn. 271–283; heute § 100d StPO", 110, 715, "kern3"),
    *icons([("tabler", "gavel", "richt", HELL), ("tabler", "shield-lock", "kern", ROTHELL),
            ("tabler", "notebook", "kern2", HELL), ("tabler", "trash", "kern3", GRAU)], IX, 470, 170),
    *kette("HS_", 1600, [("ruhig", "richt"), ("still", "kern"), ("ernst", "kern3")]),
    namensschild(NAME["HS"], 1600, BR, "richt", FARBE["HS"], d=0.2),
]))

# E3 Seit 2025 (Trojaner II): Straftatengewicht und Zitiergebot ----------------------------------------------------------
folie([("n1", f"{PR} › seit 2025: Quellen-TKÜ"), ("zit", f"{PR} › Zitiergebot, Art. 19 I 2 GG")], rechts_frei([
    *tafel("n1", "Seit 2025"),
    *okz("Quellen-TKÜ: Verdacht einer besonders", 180, "n1", "Bold", 34),
    z("schweren Straftat, wegen des Systemzugriffs", 185, 230, beim("n1", "wegen"), "Bold", 34),
    *neinz("für Taten mit höchstens 3 Jahren Freiheitsstrafe:", 320, "n2", size=33),
    z("nichtig", 185, 368, beim("n2", "nichtig"), "Bold", 33),
    fund("BVerfG, Beschl. v. 24.6.2025 – 1 BvR 180/23 (Trojaner II), Tenor 1, Rn. 201–213, 270", 110, 430, beim("n2", "nichtig")),
    *neinz("§ 100b nennt Art. 10 nicht: Zitiergebot", 500, "zit", "Bold", 34),
    fund("Art. 19 Abs. 1 Satz 2 GG; Trojaner II, Rn. 245–251", 110, 560, "zit"),
    fb(110, 620, 1040, 130, ROTHELL, "fort", [("verfassungswidrig, gilt aber bis zu", "ExtraBold", 33, INK),
                                             ("einer Neuregelung fort", "ExtraBold", 33, INK)]),
    fund("Trojaner II, Tenor 2, Rn. 275 f.", 110, 765, "fort"),
    *paar("n1", [("ruhig",), ("denkt", "n2"), ("staunt", "fort")], [("ruhig",), ("ernst", "n2"), ("still", "fort")]),
]))

# F1 Lösung (Tafel): § 100b Abs. 1, 2 StPO ---------------------------------------------------------------------------------
PL_ = "Lösung · Herr Weinhold"
folie([("loes", f"{PL_} · § 100b Abs. 1, 2 StPO")], rechts_frei([
    *tafel("loes", "Lösung: Herr Weinhold"),
    *okz("Geldfälschung: im Katalog der besonders", 180, "l1", "Bold", 34),
    z("schweren Straftaten", 185, 230, beim("l1", "besonders"), "Bold", 34),
    fund("§ 100b Abs. 2 Nr. 1 Buchst. d StPO; § 146 Abs. 1, 2 StGB", 110, 290, beim("l1", "besonders")),
    *okz("Nr. 1: Verdacht aus bestimmten Tatsachen", 360, "l2", size=34),
    *okz("Nr. 2: im Einzelfall besonders schwer", 430, "l3", size=34),
    *okz("Nr. 3: sonst Aufklärung wesentlich erschwert", 500, "l4", size=34),
    fund("§ 100b Abs. 1 Nr. 1–3 StPO", 110, 570, "l4"),
    *icons([(HC, "euro-banknote", "l1", GRUENHELL), ("tabler", "file-search", "l2", HELL),
            ("tabler", "scale", "l3", GELB), ("tabler", "device-laptop", "l4", BLAUHELL)], IX, 470, 170),
    *kette("HS_", 1600, [("ruhig", "loes"), ("ernst", "l2"), ("entschlossen", "l4")]),
    namensschild(NAME["HS"], 1600, BR, "loes", FARBE["HS"], d=0.2),
]))

# F2 Zurück am Laptop und im Büro --------------------------------------------------------------------------------------------
_zb, _ = zimmer("l5")
folie([("l5", "Lösung · Quellen-TKÜ oder Online-Durchsuchung"), ("l7", "Lösung · Anordnung durch das Gericht")], [
    *_zb,
    *stufen([("WH_tippt_r", "l5"), ("WH_ruhig_r", "l7")], WHX, BODEN, SH, erst="cut"),
    stuhl(WHX, BODEN, "l5", rechts=True, anim="cut"),
    namensschild(NAME["WH"], WHX, BODEN, "l5", FARBE["WH"], anim="cut"),
    ficon("tabler", "message-circle", DX - 40, LY, 90, "l5", fuell=WEISS, bis="l6"),
    ficon("tabler", "message-circle", DX + 40, LY - 70, 80, beim("l5", "Chats"), fuell=GRUENHELL, bis="l6"),
    pl("laufende Chats: Quellen-TKÜ", 600, 40, "l5", fill=BLAUHELL, size=32, anker="m", bis="l6"),
    pl("Art. 10 und IT-Grundrecht", 600, 120, beim("l5", "gemessen"), fill=GELB, size=30, anker="m", bis="l6"),
    ficon("tabler", "folders", DX, LY, 110, "l6", fuell=GELB, bis="l7"),
    pl("ganzer Laptop: Online-Durchsuchung", 600, 40, "l6", fill=ROTHELL, size=32, anker="m", bis="l7"),
    pl("§ 100b StPO", 600, 120, beim("l6", "Paragraf"), fill=WEISS, size=30, anker="m", bis="l7"),
    *stufen([("HS_ruhig", "l5"), ("HS_denkt", "l6"), ("HS_entschlossen", "l7"), ("HS_beschluss", "h2")], HSX, BODEN, FR,
            rede={"HS_beschluss": 1}, erst="cut", ende="tipp"),
    namensschild(NAME["HS"], HSX, BODEN, "l5", FARBE["HS"], anim="cut"),
    ficon("tabler", "building-bank", 1340, BODEN - 330, 110, "l7", fuell=WEISS),
    pl("Gericht, auf Antrag der Staatsanwaltschaft", 600, 40, "l7", fill=GRUENHELL, size=32, anker="m"),
    ficon("tabler", "trash", DX, LY, 90, "l8", fuell=GRAU),
    pl("Höchstpersönliches löschen", 600, 120, "l8", fill=WEISS, size=30, anker="m"),
    blase("sprech", 620, 200, "h2", 1500, 230, inhalt=["Dann geht der Antrag ans Gericht.", "Ohne Beschluss läuft nichts."],
          textsize=32, figur=HSb),
])

# G Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Grundrecht nach der Art des Zugriffs")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Grundrecht nach der Art des Zugriffs", 200, 200, beim("tipp", "Bestimme"), "Bold", 34),
    z("nur auf dem Übertragungsweg abgefangen:", 200, 290, "t1", size=33),
    z("Art. 10", 960, 290, beim("t1", "Artikel"), "Bold", 33),
    z("Eingriff in das eigene Gerät:", 200, 360, "t2", size=33),
    z("Art. 10 und IT-Grundrecht", 720, 360, beim("t2", "Artikel"), "Bold", 33),
    z("System durchsucht: IT-Grundrecht,", 200, 430, "t3", size=33),
    z("bei laufender Kommunikation zusätzlich Art. 10", 200, 478, beim("t3", "bei"), size=33),
    fb(200, 560, 950, 130, GELB, "t4", [("Art. 13 nur: Wohnung betreten oder", "ExtraBold", 31, INK),
                                      ("über Kamera und Mikrofon hineinschauen", "ExtraBold", 31, INK)]),
    fund("BVerfGE 120, 274, Rn. 184, 193; Trojaner II, LS 1–3", 200, 710, "t4"),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# H Klausurschema -------------------------------------------------------------------------------------------------------
PS_ = "Klausurschema"
FX = 1290
folie([("sch", PS_), ("k1", f"{PS_} › I. Schutzbereich"), ("k2", f"{PS_} › II. Eingriff"), ("k3", f"{PS_} › III. Rechtfertigung")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Prüfungsschema: heimlicher Zugriff auf IT-Systeme", 110, 85, "sch", 46),
    pl("I.", 110, 182, "k1", fill=GELB, size=32), z("Schutzbereich: Grundrecht nach der Zugriffsart", 220, 180, "k1", "Bold", 34, rechts=FX - 20),
    z("Art. 10 · IT-Grundrecht · Art. 13", FX, 186, "k1", size=28, farbe=TEXT, rechts=1840),
    pl("II.", 110, 262, "k2", fill=BLAU, size=32), z("Eingriff: heimlicher Zugriff auf das System", 220, 260, "k2", "Bold", 34, rechts=FX - 20),
    pl("III.", 110, 342, "k3", fill=GRUEN, size=32), z("Rechtfertigung", 220, 340, "k3", "Bold", 34, rechts=FX - 20),
    z("1. normenklare gesetzliche Grundlage", 220, 410, "k4", size=33, rechts=FX - 20),
    z("BVerfGE 120, 274, Rn. 208 f.", FX, 415, "k4", size=28, farbe=TEXT, rechts=1840),
    z("2. Verdacht einer besonders schweren Straftat", 220, 470, "k5", size=33, rechts=FX - 20),
    z("oder konkrete Gefahr für ein überragend", 265, 520, beim("k5", "oder"), size=33, rechts=FX - 20),
    z("wichtiges Rechtsgut", 265, 570, beim("k5", "oder"), size=33, rechts=FX - 20),
    z("Trojaner II, Rn. 134; BVerfGE 120, 274, Rn. 247", FX, 475, "k5", size=28, farbe=TEXT, rechts=1840),
    z("3. Richtervorbehalt", 220, 630, "k6", size=33, rechts=FX - 20),
    z("BVerfGE 120, 274, Rn. 257–259", FX, 635, "k6", size=28, farbe=TEXT, rechts=1840),
    z("4. Schutz des Kernbereichs", 220, 690, "k7", size=33, rechts=FX - 20),
    z("Rn. 271–283; § 100d StPO", FX, 695, "k7", size=28, farbe=TEXT, rechts=1840),
    z("5. Zitiergebot, wenn Art. 10 betroffen ist", 220, 750, "k8", size=33, rechts=FX - 20),
    z("Art. 19 I 2 GG; Trojaner II, Rn. 245", FX, 755, "k8", size=28, farbe=TEXT, rechts=1840),
])

# I Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer heimlich in einen Computer", 0)], [("eindringt, greift in das ", 0)],
                 [("IT-Grundrecht", "a"), (" ein.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "IT")}),
    *markertext([[("Nur beim Verdacht ", 0), ("besonders schwerer", "b")], [("Straftaten", "b"), (" oder bei ", 0),
                  ("konkreter Gefahr", "c")], [("für überragend wichtige Rechtsgüter,", 0)],
                 [("mit ", 0), ("Richtervorbehalt", "d"), (" und Kernbereichsschutz.", 0)]], 750, 520, 40, "m2",
                {"b": beim("m2", "besonders"), "c": beim("m2", "konkreter"), "d": beim("m2", "Richtervorbehalt")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
