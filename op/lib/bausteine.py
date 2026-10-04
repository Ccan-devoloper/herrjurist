"""Gemeinsame Bausteine der Open-Peeps-Testvideos (Stand Katzenkönig, 30.09.2026).

Figuren: nur Open-Peeps-Posen, nie seitlich/oben angeschnitten. Karten sofort vollständig, Punkte nacheinander.
Geräusche nur bei Haken/Kreuz. Requisiten aus Bibliotheken: Tabler (MIT), Phosphor (MIT), Fluent Emoji (MIT),
Pepicons (CC BY 4.0); Linien-Icons werden nur mit Palettenfarben ausgefüllt, nicht umgezeichnet.
"""
import re, sys
from ostil import *
from ostil import _icsets
import engine
from scipy import ndimage

FOLIEN = []
FIGORDNER = "op_ab/"
FIG = SP + "peeps/"
BG_FARBE = {"creme": (255, 248, 236, 255)}
PFAD_FARBE = {"creme": (21, 21, 21, 140)}
RAND = 24


def folie(pfade, els):
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def peep_voll(name, cx, unten, hoehe, cue, unten_offen=False, **k):
    """Nie links/rechts/oben angeschnitten; unten nur mit unten_offen=True."""
    ordner = "op_we/" if name.startswith("ER_") else FIGORDNER
    e = bild(FIG + ordner + name + ".png", cx, unten, hoehe, cue, **k)
    assert e.x >= RAND and e.y >= RAND and e.x + e.sprite.width <= engine.W - RAND, f"Figur {name} seitlich/oben angeschnitten"
    if not unten_offen:
        assert e.y + e.sprite.height <= engine.H - RAND, f"Figur {name} unten angeschnitten"
    return e


def figuren(liste, cx, unten, hoehe, erst="pop", d=0.0):
    els = []
    for i, (n, c) in enumerate(liste):
        bis = liste[i + 1][1] if i + 1 < len(liste) else None
        if isinstance(n, tuple):
            n, bis = n
        els.append(peep_voll(n, cx, unten, hoehe, c, anim=(erst if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=bis))
    return els


def ok(x, y, cue, gr=30, d=0.0):
    return ton(haken_i(x, y, cue, gr=gr, d=d), "haken*")          # Bleistift-Haken, Varianten reihum


def nein(x, y, cue, gr=28):
    return ton(kreuz_i(x, y, cue, gr=gr), "kreuz*")                # Bleistift-Kreuz, Varianten reihum


def zeile(text, x, y, cue, stil="Regular", size=42, farbe=INK, d=0.0, **k):
    return OT(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)


def plusminus(text, x, y, cue, plus, size=40, stil="Regular", d=0.0):
    z = "(+)" if plus else "(-)"
    breite = OT(text, 0, 0, "_", stil, size).sprite.width - 8 + F(stil, size).getlength(" ")
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(z, x + breite, y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT), d=d)]


_icf = {}
def ficon(setname, name, cx, unten, breite, cue, fuell=None, nebenfarbe=WEISS, spiegeln=False, d=0.0, bis=None, anim="pop"):
    """Linien-Icon aus einer Bibliothek, unten auf 'unten' gestellt. Die größte umschlossene Fläche wird mit
    'fuell' gefüllt, kleinere umschlossene Flächen (Fenster, Radnaben) mit 'nebenfarbe' – die Linien bleiben original."""
    key = (setname, name, breite, fuell, nebenfarbe, spiegeln)
    if key not in _icf:
        if setname not in _icsets:
            _icsets[setname] = json.load(open(SP + f"blasen/{setname}/package/icons.json"))
        d_ = _icsets[setname]
        ic = d_["icons"][name]
        w = ic.get("width", d_.get("width", 24)); h = ic.get("height", d_.get("height", 24))
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{ic["body"]}</svg>'.replace("currentColor", "#151515")
        im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=breite, output_height=int(breite * h / w)))).convert("RGBA")
        if fuell is not None:
            a = np.asarray(im)[..., 3] > 60
            lab, n = ndimage.label(~a)
            rand = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
            innen = [(int((lab == i).sum()), i) for i in range(1, n + 1) if i not in rand]
            arr = np.asarray(im).copy()
            if innen:
                groesste = max(innen)[1]
                for gr_, i in innen:
                    if gr_ < 30:
                        continue
                    m = ndimage.binary_dilation(lab == i, iterations=1) & (arr[..., 3] < 250)
                    farbe = fuell if i == groesste else nebenfarbe
                    arr[m, :3] = farbe[:3]; arr[m, 3] = np.maximum(arr[m, 3], 255)
            im = Image.fromarray(arr)
            # Linien wieder obenauf, damit die Füllung nicht über die Kontur blutet
            linie = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=breite, output_height=int(breite * h / w)))).convert("RGBA")
            im.alpha_composite(linie)
        if spiegeln:
            im = ImageOps.mirror(im)
        im = im.crop(im.getbbox())
        _icf[key] = im
    im = _icf[key]
    return El(im, cx - im.width / 2, unten - im.height, cue, anim, d, bis, name=f"ficon:{name}")


from PIL import ImageOps
BODEN = 870
AUTO = (246, 165, 192, 255)
LKW = (249, 213, 110, 255)



# --- Neue Regeln: alles vollständig im Bild, Sachverhalt-Karte ------------------------------------------
def pruefe_im_bild(els, rand=12):
    for e in els:
        if getattr(e, "unten_offen", False):
            continue
        bb = e.sprite.getbbox()
        if not bb:
            continue
        x0, y0, x1, y1 = e.x + bb[0], e.y + bb[1], e.x + bb[2], e.y + bb[3]
        if hasattr(e, "weg"):
            dx, dy = e.weg[2], e.weg[3]
            x0, x1 = min(x0, x0 + dx), max(x1, x1 + dx)
        assert x0 >= rand and y0 >= rand and x1 <= engine.W - rand and y1 <= engine.H - rand, \
            f"Element ragt aus dem Bild: {e.name} ({x0},{y0})-({x1},{y1})"


def folie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def absatz(text, x, y, breite, cue, size=38, stil="Regular", zeilenabstand=1.35, farbe=INK, d=0.0):
    """Fließtext mit Zeilenumbruch; gibt (Elemente, y_ende) zurück."""
    f = F(stil, size)
    worte, zeilen, cur = [w for w in re.split(r"[ \t\n]+", text) if w], [], ""   # geschützte Leerzeichen trennen nicht
    for w in worte:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    if cur:
        zeilen.append(cur)
    els = []
    for i, z in enumerate(zeilen):
        els.append(OT(z, x, y + i * size * zeilenabstand, cue, stil, size, farbe=farbe, d=d, anim="fade"))
    return els, y + len(zeilen) * size * zeilenabstand


def sachverhalt(cue, absaetze, frage, pfad="Sachverhalt"):
    """Karte mit dem vollständigen Sachverhalt zum Nachlesen (erscheint komplett auf einmal)."""
    els = [karte(140, 60, 1640, 900, cue, fill=(255, 251, 230, 255)), titel("Sachverhalt", 210, 110, cue, 64)]
    y = 225
    for a in absaetze:
        e, y = absatz(a, 210, y, 1480, cue, size=38)
        els += e; y += 22
    els.append(pille(frage, 210, min(y + 10, 860), cue, fill=PINK, size=38))
    folie([(cue, pfad)], els)


# --- Blasen im Pinselstil (Variante E): Form Comical.js, Kontur perfect-freehand, Text Nunito -------------------------
import hashlib, os, json, math, subprocess as _sp
from PIL import Image, ImageDraw
_BL2 = os.path.join(SP, "bl2")


def kopfziel(figur, art, bx):
    """Zielpunkt am Kopf einer Figur (name, cx, unten, hoehe): Denkblase knapp über den Kopf, Sprechblase schräg
    über den Mund auf der Seite der Blase."""
    name, cx, unten, hoehe = figur
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    ys, xs = np.nonzero(a); top = ys.min()
    band = a[top:top + int(hoehe * 0.12)]
    yy, xx = np.nonzero(band)
    hx, ty = e.x + xx.mean(), e.y + top
    seite = 1 if bx > hx else -1
    if art == "denk":
        return (round(hx + seite * 0.02 * hoehe), round(ty - 0.025 * hoehe))
    return (round(hx + seite * 0.13 * hoehe), round(ty - 0.035 * hoehe))


def blase(art, w, h, cue, cx, cy, inhalt=None, textsize=44, ziel=None, d=0.0, bis=None, stil="Bold", fill=None,
          spiegeln=None, bild_=None, bildhoehe=None, figur=None):
    """art = 'denk' | 'sprech'; (cx, cy) Blasenmitte, w/h ungefähre Außenmaße; ziel = Kopf (denk) bzw. Mund (sprech).
    Der Schwanz zeigt immer auf ziel; die Gedankenpunkte werden zum Kopf hin kleiner."""
    if figur:
        ziel = kopfziel(figur, art, cx)
    assert ziel, "Blase braucht ziel (Kopf/Mund der Figur) oder figur=(name, cx, unten, hoehe)"
    iw, ih = w * 0.78, h * 0.62
    x0, y0 = cx - iw / 2, cy - ih / 2
    tx, ty = ziel
    vx, vy = tx - cx, ty - cy
    ln = math.hypot(vx, vy)
    if art == "denk":
        mid = (cx + vx * 0.7, cy + vy * 0.7)
    else:  # leicht gebogener Schwanz
        nx, ny = -vy / ln, vx / ln
        if ny > 0: nx, ny = -nx, -ny          # Bogen nach oben/außen
        mid = (cx + vx * 0.62 + nx * 0.08 * ln, cy + vy * 0.62 + ny * 0.08 * ln)
    spec = dict(art=art, x=round(x0, 1), y=round(y0, 1), w=round(iw, 1), h=round(ih, 1), tip=[tx, ty],
                mid=[round(mid[0], 1), round(mid[1], 1)], fill=fill or "#ffffff")
    key = hashlib.sha1(json.dumps(spec, sort_keys=True).encode()).hexdigest()[:16]
    cache = os.path.join(_BL2, "cache"); os.makedirs(cache, exist_ok=True)
    png = os.path.join(cache, key + ".png")
    if not os.path.exists(png):
        sj = os.path.join(cache, key + ".json"); json.dump(spec, open(sj, "w"))
        _sp.run(["node", os.path.join(_BL2, "blase_e.js"), sj, png], check=True, cwd=_BL2)
    voll = Image.open(png).convert("RGBA")
    bb = voll.getbbox()
    im = voll.crop(bb)
    dr = ImageDraw.Draw(im)
    zeilen = inhalt if isinstance(inhalt, list) else ([inhalt] if inhalt else [])
    f = F(stil, textsize); lh = int(textsize * 1.15)
    yy = cy - bb[1] - len(zeilen) * lh / 2
    for z in zeilen:
        b2 = f.getbbox(z)
        assert b2[2] - b2[0] <= iw * 1.08, f"Blasentext zu breit: {z} ({b2[2]-b2[0]} > {iw:.0f})"
        dr.text((cx - bb[0] - (b2[2] - b2[0]) / 2 - b2[0], yy + (lh - (b2[3] - b2[1])) / 2 - b2[1]), z, font=f, fill=INK)
        yy += lh
    return El(im, bb[0], bb[1], cue, "pop", d, bis, name=f"blase:{art}:" + "/".join(zeilen))


# --- Figurenrede: Mundbewegung aus den Wortzeiten der Vertonung -------------------------------------------------------
def spricht(offen, zu, cx, unten, hoehe, cue, bis, oeffnen=0.7):
    """Figur mit geschlossenem Mund (zu) von cue bis bis; während jedes gesprochenen Wortes der Rolle wird kurz das
    Gesicht mit offenem Mund (offen) gezeigt. Wortzeiten aus cues.json (ElevenLabs-Zeichenzeiten) – Mundformen sind
    daraus geschätzt, kein Phonem-Lip-Sync."""
    cj = json.load(open("../cues.json"))
    t0 = cj["cues"][cue]["t"]
    seg = cj["segmente"][cj["cues"][cue]["seg"]]
    els = [peep_voll(zu, cx, unten, hoehe, cue, anim="cut", bis=bis)]
    for a, b in seg["woerter"]:
        ende = b if b - a < 0.15 else a + (b - a) * oeffnen
        els.append(peep_voll(offen, cx, unten, hoehe, (cue, round(a - t0, 3)), anim="cut", bis=(cue, round(ende - t0, 3))))
    return els



# --- Geräusch-Standard (Stand 30.09.2026): Papier/Stift-Welt ------------------------------------------------------------
_warnung_i, _markertext, _sachverhalt = warnung_i, markertext, sachverhalt


def warnung_i(cx, cy, cue, gr=40, d=0.0):
    """Klausurtipp-Symbol mit kurzem Unterstreichen."""
    return ton(_warnung_i(cx, cy, cue, gr=gr, d=d), "unterstreichen*")


def markertext(*a, **k):
    """Merksatz: jede Textmarker-Hervorhebung mit leisem Markerstrich."""
    els = _markertext(*a, **k)
    for e in els:
        if (e.name or "").startswith("marker:"):
            ton(e, "textmarker*")
    return els


def sachverhalt(cue, absaetze, frage, pfad="Sachverhalt"):
    """Sachverhaltskarte: erscheint mit dem Geräusch eines abgelegten Blattes."""
    n0 = len(FOLIEN)
    _sachverhalt(cue, absaetze, frage, pfad)
    ton(FOLIEN[n0]["els"][0], "papier*")


def szene(el, klang, gain=1.0, versatz=0.0):
    """Handlungsgeräusch in einer Fallszene (nur bei sichtbarer Handlung), Datei sfx3/szene_<name>.wav."""
    return ton(el, "szene_" + klang if not klang.startswith("szene_") else klang, gain, versatz)


# --- Stand 30.09.2026 (Katzenkönig): nur noch Handlungsgeräusche -----------------------------------------------------
# Haken, Kreuz, Klausurtipp-Symbol, Textmarker und Sachverhaltskarte bleiben stumm; Geräusche nur über szene().
warnung_i, markertext, sachverhalt = _warnung_i, _markertext, _sachverhalt


def ok(x, y, cue, gr=30, d=0.0):
    return haken_i(x, y, cue, gr=gr, d=d)


def nein(x, y, cue, gr=28, d=0.0):
    return kreuz_i(x, y, cue, gr=gr, d=d)


# --- Wortzeiten und Mundzustände ----------------------------------------------------------------------------------------
import re as _re
_CJ = None
def _cj():
    global _CJ
    if _CJ is None:
        _CJ = json.load(open("../cues.json"))
    return _CJ


def _t(c):
    cj = _cj()
    return cj["cues"][c[0]]["t"] + c[1] if isinstance(c, tuple) else cj["cues"][c]["t"]


def beim(cue, wort, nr=1, ende=False):
    """(cue, Versatz) zum Beginn (bzw. Ende) des nr-ten Wortes ab der Marke, das mit 'wort' beginnt."""
    cj = _cj(); t0 = cj["cues"][cue]["t"]
    for s in cj["segmente"][cj["cues"][cue]["seg"]:]:
        for w, (a, b) in zip(s["text"].split(), s["woerter"]):
            if a < t0 - 0.05:
                continue
            if _re.sub(r"[^\wäöüÄÖÜß.\-]", "", w).lower().startswith(wort.lower()):
                nr -= 1
                if nr == 0:
                    return (cue, round((b if ende else a) - t0, 3))
    raise KeyError(f"Wort {wort!r} nach Marke {cue!r} nicht gefunden")


_VOKAL = [("au", "a"), ("ai", "a"), ("ei", "e"), ("eu", "o"), ("äu", "o"), ("ie", "e"),
          ("a", "a"), ("ä", "e"), ("e", "e"), ("i", "e"), ("y", "e"), ("o", "o"), ("u", "o"), ("ö", "o"), ("ü", "o")]
_VRX = _re.compile("|".join(v for v, _ in _VOKAL))


def mundfolge(wort):
    """Grobe Visemfolge aus der Schreibung: a = weit offen, o = rund, e = breit (Zähne)."""
    m = dict(_VOKAL)
    folge = [m[g] for g in _VRX.findall(wort.lower())] or ["a"]
    return folge


def redet(basis, cx, unten, hoehe, cue, bis, **k):
    """Sprechende Figur: Grundbild (Mund zu) von cue bis bis; während jedes Wortes wechseln die Mundzustände
    basis_a/_o/_e entlang der Vokale des Wortes, zwischen Wörtern und in Pausen ist der Mund geschlossen.
    Zeiten aus den ElevenLabs-Zeichenzeiten (Wortgrenzen); Viseme aus der Schreibung geschätzt, kein Phonem-Alignment."""
    cj = _cj(); ta, tb = _t(cue), _t(bis)
    els = [peep_voll(basis, cx, unten, hoehe, cue, anim="cut", bis=bis, **k)]
    for s in cj["segmente"]:
        for w, (a, b) in zip(s["text"].split(), s["woerter"]):
            if a < ta - 0.01 or b > tb + 0.01:
                continue
            folge = mundfolge(w)
            dauer = (b - a) * 0.88
            n = max(1, min(len(folge), int(dauer / 0.1)))
            folge = folge[:: max(1, len(folge) // n)][:n]
            for j, v in enumerate(folge):
                s0, s1 = a + dauer * j / n, a + dauer * (j + 1) / n
                els.append(peep_voll(f"{basis}_{v}", cx, unten, hoehe, (cue, round(s0 - ta, 3)), anim="cut",
                                     bis=(cue, round(s1 - ta, 3)), **k))
    return els
