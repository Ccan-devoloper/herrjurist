"""Reel 1080×1920 aus Szenen (Variante C, Reel-Regeln aus REDAKTION.md).

* Thema ab Bild 0 groß lesbar; keine eingebrannten Wort-für-Wort-Untertitel (Redundanzprinzip).
* Je Moment ein Blickfang, ≤ 5–7 Wörter, ≥ 60 px; Elemente erscheinen zu ihrem Wort und ersetzen ältere (neu=true).
* Höchstens eine Norm je Szene als ruhige lila Zeile; Fundstellen in der Beschreibung.
* Hook-Stile: split, kippen, knall (Zittern höchstens jedes fünfte Reel – der Planer achtet darauf).
"""
import json, math, os, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw
import imageio_ffmpeg
import opkern as k
from opkern import (C, F, OT, titel, pille, fl_block, karte, ficon, icon, haken_i, kreuz_i, boden,
                    WEISS, GELB, GRUEN, ROT, LILA, INK, PASTELL, FARBEN, NORMFARBE)
import stimme

W_, H_, FPS = 1080, 1920, 30
BODEN = 1400
SFX_DIR = os.path.join(k.HIER, "ressourcen", "sfx")
SCHNITT = {"stempel": (0.28, 0.75), "riss": (1.15, 1.95), "rechner": (4.95, 5.75), "muenzen": (0.0, 1.5)}


class Reel:
    def __init__(self, spec, besetzung, out_dir, datum):
        self.s, self.b, self.out, self.datum = spec, besetzung, out_dir, datum
        self.k = int(spec["klausur"])
        self.ELS, self.SFX, self.texte = [], [], []

    # ------------------------------------------------------------ Zeit
    def wort(self, seg, w, nr=1):
        n = 0
        for t, a, e in self.SEG[seg]["woerter"]:
            if t.strip(",.:!?–-").lower().startswith(w.lower()):
                n += 1
                if n == nr: return a
        raise KeyError(f"Reel {self.datum}: Wort „{w}“ fehlt in Segment {seg}")

    def zeige(self, el, t0, t1=None, anim="pop"):
        for e in (el if isinstance(el, list) else [el]):
            self.ELS.append((e, t0, t1, anim))

    def T(self, *t):
        self.texte.extend(x for x in t if isinstance(x, str) and x.strip())

    def figur(self, ref, cx, hoehe, t0, t1, anim="pop", name_schild=None):
        self.zeige(k.peep(self.b.name(ref, cx), cx, BODEN, hoehe), t0, t1, anim)
        if name_schild:
            self.T(name_schild)
            self.zeige(pille(name_schild, cx, BODEN + 18, C, fill=GELB, size=34, anker="m", pad=(26, 10)), t0, t1, "cut" if anim == "cut" else "pop")

    # ------------------------------------------------------------ Aufbau
    def kopfzeile(self):
        kl = self.s.get("klausurLabel") or k.MARKE["klausurLabel"] or f"Klausur {self.k}"
        self.T(self.s["fachLabel"].upper(), kl)
        frei = (W_ - 48 - F("Bold", 32).getlength(kl) - 44) - 48 - 60 - 28
        self.zeige(pille(self.s["fachLabel"].upper(), 48, 50, C, fill=PASTELL[self.k], size=k.passt(self.s["fachLabel"].upper(), "Bold", 46, min(620, frei), 24), pad=(30, 12)), 0, None, "cut")
        self.zeige(pille(kl, W_ - 48, 56, C, fill=WEISS, size=32, anker="r", pad=(22, 10)), 0, None, "cut")

    def hook(self, h, t_ende):
        seg = "hook"
        zeilen = h["zeilen"]; self.T(*zeilen, h.get("pille"))
        # Kippen: die letzte Zeile ist die Irrtums-Aussage → eigener Kasten statt Durchstreichung in der Schlagzeile
        irrtum = zeilen[-1] if h.get("stil") == "kippen" and len(zeilen) > 1 else None
        kz = zeilen[:-1] if irrtum else zeilen
        gs = 140
        while max(F("ExtraBold", gs).getlength(z) for z in kz) + 40 > 984: gs -= 2
        for i, z in enumerate(kz):
            self.zeige(titel(z, 40, 220 + i * int(gs * 1.12), C, gs, marker=PASTELL[self.k]), 0, t_ende, "cut")
        y = 220 + len(kz) * int(gs * 1.12) + 10
        if h.get("pille"):
            self.zeige(pille(h["pille"], 48, y, C, fill=WEISS, size=40, pad=(24, 10)), 0, t_ende, "cut"); y += 90
        yk = y + 30
        y_irrtum = None
        if irrtum:
            y_irrtum = yk
            self.zeige(fl_block(90, yk, 900, 180, (252, 222, 216, 255), C,
                                [("Irrtum", "Bold", 38, INK), (irrtum, "ExtraBold", k.passt(irrtum, "ExtraBold", 66, 820, 40), INK)]), 0, t_ende, "cut")
            yk += 210
        self.zeige(boden(BODEN, C, 48, 1032), 0, t_ende, "cut")
        if h.get("figur"):
            self.figur(h["figur"], 300, 470, 0, t_ende, "cut", h.get("name"))
        for i, ic in enumerate(h.get("icons", [])):
            setn, nm = ic[0].split(":")
            t1 = self.wort(seg, ic[2]) if len(ic) > 2 and ic[2] else t_ende
            self.zeige(ficon(setn, nm, 640 + i * 220, BODEN - (0 if i == 0 else 40), 150 + i * 20, C, fuell=FARBEN.get(ic[1]) if ic[1] else None), 0, t1, "cut")
        stil = h.get("stil", "split")
        if stil == "split":
            for i, b in enumerate(h["split"]):
                self.T(b["label"], b["wert"])
                self.zeige(fl_block(48 + i * 514, yk, 470, 200, FARBEN[b.get("farbe", "WEISS")], C,
                                    [(b["label"], "ExtraBold", 44, INK), (b["wert"], "ExtraBold", 66, INK)]),
                           self.wort(seg, b["wort"]), t_ende, "slideL" if i == 0 else "slideR")
        elif stil == "kippen":
            # Aussage steht ab Bild 0; zum Stempelwort wird die letzte Schlagzeilenzeile rot durchgestrichen
            st = h.get("stempel") or {}
            if st and not irrtum:
                yl = 220 + (len(zeilen) - 1) * int(gs * 1.12) + int(gs * 0.55)
                bl_ = max(F("ExtraBold", gs).getlength(z) for z in zeilen[-1:]) + 40
                strich = Image.new("RGBA", (int(bl_) + 20, 28)); ImageDraw.Draw(strich).rounded_rectangle((0, 0, int(bl_) + 19, 27), 12, fill=(215, 60, 45, 255))
                self.zeige(k.engine.El(strich, 30, yl, C, "slideL", 0.0, name="strich"), self.wort(seg, st["wort"]), t_ende, "slideL")
            if h.get("richtig"):
                self.T(h["richtig"]["text"])
                r = h["richtig"]
                fr = FARBEN.get(r.get("farbe")) if isinstance(FARBEN.get(r.get("farbe")), tuple) else GRUEN
                self.zeige(fl_block(90, yk, 900, 180, fr, C, [(r.get("label", "Richtig"), "Bold", 38, INK),
                                                             (r["text"], "ExtraBold", k.passt(r["text"], "ExtraBold", 66, 820, 40), INK)]),
                           self.wort(seg, r["wort"]), t_ende, "pop")
        if h.get("stempel"):
            st = h["stempel"]; self.T(st["text"])
            t0 = self.wort(seg, st["wort"])
            if stil == "knall":
                self.zeige(kreuz_i(540, yk + 190, C, gr=200), t0, t_ende, "slam")   # Kreuz 300 px hoch, Oberkante unter der Pille
            elif irrtum:
                sp = pille(st["text"], 100, 100, C, fill=ROT, size=54, stil="ExtraBold", pad=(28, 12))
                rot = sp.sprite.rotate(10, resample=Image.BICUBIC, expand=True)
                self.zeige(k.engine.El(rot, 1000 - rot.width + 20, y_irrtum - 44, C, "punch", 0.0, name="stempel"), t0, t_ende, "punch")
            else:
                sw = F("Bold", 52).getlength(st["text"]) + 70
                px = min(797 if stil == "split" else 800, 1020 - sw / 2)
                self.zeige(pille(st["text"], px, yk + (230 if stil == "split" else -120), C, fill=ROT, size=52, anker="m", pad=(28, 12)),
                           t0, t_ende, "punch")
            self.SFX.append(("stempel", t0, 1.6))

    def szene(self, sz, nr, t0, t1):
        seg = sz["seg"]
        self.T(sz["titel"])
        self.zeige(k.titel_passend(sz["titel"], 48, 200, 88, rechts=900, marker=PASTELL[self.k]), t0, t1, "rise")
        self.zeige(pille(f"{nr}/{len(self.s['szenen'])}", W_ - 48, 216, C, fill=WEISS, size=34, anker="r", pad=(20, 8)), t0, t1, "cut")
        elemente = sz["elemente"]
        # Gruppen: ein Element mit neu=true beendet alle vorherigen und beginnt oben neu
        zeiten = []
        for e in elemente:
            zeiten.append(t0 + 0.15 if e.get("wort") is None else self.wort(seg, e["wort"], e.get("nr", 1)))
        enden = [t1] * len(elemente)
        for i, e in enumerate(elemente):
            if e.get("neu"):
                for j in range(i):
                    if enden[j] == t1: enden[j] = zeiten[i]
            if e.get("bis"):
                enden[i] = self.wort(seg, e["bis"])
        # Elemente bauen; jede Gruppe (bis zum nächsten neu=true) wird senkrecht in der freien Fläche zentriert
        gruppen, aktuelle = [], []
        y = 0
        for i, e in enumerate(elemente):
            if e.get("neu") and aktuelle:
                gruppen.append(aktuelle); aktuelle = []; y = 0
            typ = e["typ"]
            if typ == "zahl":
                self.T(e["text"]); size = e.get("size", 130)
                while F("ExtraBold", size).getlength(e["text"]) > 960: size -= 4
                el = OT(e["text"], 540, y, C, "ExtraBold", size, anker="m"); anim = "pop"
            elif typ == "pille":
                self.T(e["text"])
                size = k.passt(e["text"], "Bold", e.get("size", 60), 900)
                el = pille(e["text"], 540, y, C, fill=FARBEN.get(e.get("farbe"), WEISS), size=size, anker="m", pad=(30, 14)); anim = "pop"
            elif typ == "block":
                self.T(e["label"], e["wert"])
                el = k.zahlblock(90, y, 900, e.get("h", 270), FARBEN.get(e.get("farbe"), GELB), e["label"], e["wert"],
                                 zs=e.get("zs", 120), ls=e.get("ls", 54)); anim = e.get("anim", "punch")
            elif typ == "text":
                self.T(e["text"], e.get("unter"))
                ls = k.passt(e["text"], "Bold", e.get("ls", 76), 850)
                el = k.zahlblock(90, y, 900, e.get("h", 250 if e.get("unter") else 170), FARBEN.get(e.get("farbe"), WEISS), e["text"], e.get("unter", ""),
                                 zs=e.get("zs", 48), ls=ls); anim = e.get("anim", "pop")
            elif typ == "norm":
                self.T(e["text"])
                el = OT(e["text"], 540, y, C, "Bold", 48, farbe=NORMFARBE, anker="m"); anim = "rise"
            else:
                raise ValueError(f"Unbekanntes Reel-Element {typ}")
            aktuelle.append((el, zeiten[i], enden[i], anim))
            y = el.y + el.sprite.height + e.get("abstand", 46)
        if aktuelle: gruppen.append(aktuelle)
        L = self.s.get("layout", "A")
        if L == "B":                                      # groß: Elemente vergrößert, über die ganze Höhe verteilt
            for g in gruppen:
                yy = None
                for el, *_ in g:
                    f = min(1.12, 1000 / el.sprite.width) if el.sprite.width > 0 else 1
                    if f > 1.01:
                        alt_w = el.sprite.width
                        el.sprite = el.sprite.resize((int(el.sprite.width * f), int(el.sprite.height * f)), Image.LANCZOS)
                        el.x -= (el.sprite.width - alt_w) / 2
                    if yy is not None: el.y = yy
                    yy = el.y + el.sprite.height + 90
            unten_frei = 1640 - 280
        elif L == "C": unten_frei = 1000
        elif L == "D": unten_frei = self.schema_oben() - 20
        elif L == "E": unten_frei = 1040
        else: unten_frei = BODEN - (240 if (sz.get("icon") or sz.get("figur")) else 60)
        for g in gruppen:
            top = min(el.y for el, *_ in g); bot = max(el.y + el.sprite.height for el, *_ in g)
            dy = int(max(330, 330 + (unten_frei - 330 - (bot - top)) / 2) - top)
            for el, t0_, t1_, anim in g:
                el.y += dy
                self.zeige(el, t0_, t1_, anim)
        if L == "A":
            self.zeige(boden(BODEN, C, 48, 1032), t0, t1, "cut")
        if sz.get("icon") and L in ("A", "B"):
            setn, nm = sz["icon"][0].split(":")
            ti = self.wort(seg, sz["icon"][2]) if len(sz["icon"]) > 2 and sz["icon"][2] else t0
            if L == "A":
                self.zeige(ficon(setn, nm, 860, BODEN - 20, 170, C, fuell=FARBEN.get(sz["icon"][1]) if sz["icon"][1] else None), ti, t1, "pop")
            else:
                self.zeige(ficon(setn, nm, 540, 1640, 250, C, fuell=FARBEN.get(sz["icon"][1]) if sz["icon"][1] else None), ti, t1, "pop")
        if L in ("D", "E"):
            self.schema_leiste(nr - 1, t0, t1, kompakt=(L == "E"))
        hf = (self.s["hook"].get("figur") or "") if L in ("C", "E") else ""
        if hf:
            buchst, _, pose = hf.replace(":", "/").partition("/")
            blase_ = sz.get("blase")
            if L == "C":
                self.zeige(boden(1640, C, 48, 1032), t0, t1, "cut")
                p = k.peep(self.b.name(f"{buchst}/{sz.get('pose', 'erklaert')}", 300), 300, 1640, 620)
                self.zeige(p, t0, t1, "cut")
                if blase_:
                    self.T(blase_)
                    bw = min(600, max(380, int(F("Bold", 42).getlength(blase_) / 0.8) + 60))
                    tb = self.wort(seg, sz["blase_wort"]) if sz.get("blase_wort") else t0 + 0.6
                    self.zeige(k.bl("sprech", bw, 180, 1032 - bw / 2 - 10, 1080, blase_, k.kopfpunkt(p, 1), 42), tb, t1, "pop")
            else:
                b = k.nah(self.b.name(f"{buchst}:{sz.get('mimik', 'redet')}", 780), 780, 1300, 600)
                self.zeige(b, t0, t1, "cut")
                if blase_:
                    self.T(blase_)
                    bw = min(520, max(360, int(F("Bold", 40).getlength(blase_) / 0.8) + 60))
                    tb = self.wort(seg, sz["blase_wort"]) if sz.get("blase_wort") else t0 + 0.6
                    self.zeige(k.bl("sprech", bw, 160, 48 + bw / 2 + 10, 1400, blase_, k.kopfpunkt(b, -1), 40), tb, t1, "pop")
        for name, w, gain in sz.get("sfx", []):
            self.SFX.append((name, self.wort(seg, w), gain))
        if sz.get("figur"):
            f = sz["figur"]
            tf = self.wort(seg, f["wort"]) if f.get("wort") else t0
            self.figur(f["ref"], 300, f.get("hoehe", 440), tf, t1, "pop")

    def schema_oben(self):
        """Oberkante der Prüfschema-Karte (Layout D): wächst mit der Zahl der Schritte nach oben."""
        return min(1180, 1640 - 118 - 98 * len(self.s["szenen"]))

    def schema_leiste(self, aktiv, t0, t1, kompakt=False):
        """Prüfschema des Reels (Szenentitel) als Orientierung: erledigt grau mit Haken, aktuell farbig, kommend weiß."""
        schritte = [sz["titel"] for sz in self.s["szenen"]]
        grau = (140, 140, 145, 255)
        if not kompakt:
            y0 = self.schema_oben()
            self.zeige(karte(48, y0, 984, 1640 - y0, C, fill=(255, 255, 255, 255)), t0, t1, "cut")
            self.zeige(OT("Prüfschema", 90, y0 + 28, C, "ExtraBold", 44), t0, t1, "cut")
            y = y0 + 106
            schritt, hz = 98, 80
            for i, s_ in enumerate(schritte):
                fertig, akt = i < aktiv, i == aktiv
                fill = PASTELL[self.k] if akt else ((236, 236, 236, 255) if fertig else WEISS)
                self.zeige(fl_block(90, y, 900, hz, fill, C, [(" ", "Bold", 10, INK)]), t0, t1, "cut")
                self.zeige(pille(str(i + 1), 110, y + hz // 2 - 28, C, fill=WEISS, size=36, pad=(18, 4)), t0, t1, "cut")
                gr = k.passt(s_, "Bold", min(44, hz - 30), 720, 30)
                self.zeige(OT(s_, 190, y + hz // 2 - int(gr * 0.6), C, "ExtraBold" if akt else "Bold", gr, farbe=grau if fertig else INK), t0, t1, "cut")
                if fertig: self.zeige(haken_i(950, y + hz // 2, C, gr=26), t0, t1, "cut")
                y += schritt
        else:
            n = len(schritte); w = (984 - (n - 1) * 16) // n; x = 48
            for i, s_ in enumerate(schritte):
                fertig, akt = i < aktiv, i == aktiv
                fill = PASTELL[self.k] if akt else ((236, 236, 236, 255) if fertig else WEISS)
                t = f"{i + 1} · {s_}"
                self.zeige(fl_block(x, 1110, w, 90, fill, C, [(t, "ExtraBold" if akt else "Bold", k.passt(t, "Bold", 36, w - 30, 22), grau if fertig else INK)]), t0, t1, "cut")
                x += w + 16

    def merke(self, m, t0):
        seg = m.get("seg", "cta")
        self.zeige(titel("Merke", 48, 200, C, 88, marker=PASTELL[self.k]), t0, None, "rise")
        self.zeige(karte(48, 340, 984, 560, C, fill=(255, 251, 230, 255)), t0, None, "cut")
        for i, (z, w) in enumerate(zip(m["zeilen"], m["woerter"])):
            self.T(z)
            s = 66
            while F("ExtraBold", s).getlength(z) > 900: s -= 2
            self.zeige(OT(z, 540, 400 + i * 120, C, "ExtraBold", s, anker="m"), self.wort(seg, w) if w else t0, None, "rise")
        tc = self.wort(seg, m["cta_wort"]) if m.get("cta_wort") else t0 + 1.5
        self.T(m["cta"], m.get("hinweis"))
        self.zeige(icon("tabler", "bookmark", 200, 1040, 110, C), tc, None, "punch")
        self.zeige(pille(m["cta"], 270, 1005, C, fill=GELB, size=44), tc, None, "pop")
        if m.get("hinweis"):
            self.zeige(OT(m["hinweis"], 540, 1150, C, "Bold", 40, farbe=NORMFARBE, anker="m"), tc + 0.3, None, "rise")

    # ------------------------------------------------------------ Bild
    def rahmen(self):
        ov = Image.new("RGBA", (W_, H_), k.FEED[self.k])
        m = Image.new("L", (W_, H_), 0)
        ImageDraw.Draw(m).rounded_rectangle((24, 24, W_ - 24, H_ - 24), 36, fill=255)
        ov.putalpha(Image.eval(m, lambda v: 255 - v))
        ring = Image.new("RGBA", (W_, H_))
        ImageDraw.Draw(ring).rounded_rectangle((18, 18, W_ - 18, H_ - 18), 40, outline=INK, width=6)
        ov.alpha_composite(ring)
        return ov

    @staticmethod
    def _ease(x):
        return 1 + 2.70158 * (x - 1) ** 3 + 1.70158 * (x - 1) ** 2

    def _skaliert(self, sp, s):
        key = (id(sp), round(s, 3))
        if key not in self._cache:
            self._cache[key] = sp.resize((max(1, int(sp.width * s)), max(1, int(sp.height * s))), Image.LANCZOS)
        return self._cache[key]

    @staticmethod
    def _setze(img, sp, x, y, alpha=1.0):
        if alpha < 1:
            sp = sp.copy(); a = np.asarray(sp)[..., 3].astype(np.float32) * alpha
            sp.putalpha(Image.fromarray(a.astype(np.uint8)))
        x, y = int(round(x)), int(round(y))
        if x >= W_ or y >= H_ or x + sp.width <= 0 or y + sp.height <= 0:
            return
        cx0, cy0 = max(0, -x), max(0, -y)
        sp = sp.crop((cx0, cy0, min(sp.width, W_ - x), min(sp.height, H_ - y)))
        if sp.width > 0 and sp.height > 0:
            img.alpha_composite(sp, (x + cx0, y + cy0))

    def _mittig(self, img, sp, x, y, s, a=1.0):
        sk = self._skaliert(sp, max(0.05, s))
        self._setze(img, sk, x + (sp.width - sk.width) / 2, y + (sp.height - sk.height) / 2, a)

    def bild(self, t):
        img = self.BG.copy()
        wackeln = 0
        for e, t0, t1, anim in self.ELS:
            if t < t0 or (t1 is not None and t >= t1):
                continue
            p = t - t0
            sp, x, y = e.sprite, e.x, e.y
            if anim == "pop" and p < 0.32:
                self._mittig(img, sp, x, y, 0.3 + 0.7 * self._ease(p / 0.32), min(1, p / 0.12))
            elif anim == "punch" and p < 0.22:
                self._mittig(img, sp, x, y, 2.6 - 1.6 * (p / 0.22) ** 0.6, min(1, p / 0.05))
            elif anim == "slam" and p < 0.2:
                self._mittig(img, sp, x, y, 2.4 - 1.4 * (p / 0.2) ** 0.7, min(1, p / 0.06))
            elif anim == "rise" and p < 0.28:
                q = p / 0.28; self._setze(img, sp, x, y + 50 * (1 - q) ** 2, q)
            elif anim in ("slideL", "slideR") and p < 0.3:
                q = 1 - (1 - p / 0.3) ** 3; self._setze(img, sp, x + (1 - q) * (-1100 if anim == "slideL" else 1100), y)
            else:
                self._setze(img, sp, x, y)
            if anim == "slam" and 0.18 <= p < 0.45:
                wackeln = max(wackeln, 14 * (1 - (p - 0.18) / 0.27))
        if wackeln:
            img = Image.fromarray(np.roll(np.asarray(img), (int(wackeln * math.cos(t * 70)), int(wackeln * math.sin(t * 90))), axis=(0, 1)))
        img.alpha_composite(self.RAHMEN)
        return img.convert("RGB")

    # ------------------------------------------------------------ Cover
    def cover_bild(self):
        """Eigenes Reel-Cover: Hook groß im 3:4-Bereich des Profilrasters (y 260–1660), Element des Hook-Stils, Brustbild."""
        from figuren import POSE_MIMIK
        h, kk = self.s["hook"], self.k
        els = []
        lbl = self.s["fachLabel"].upper()
        kl = self.s.get("klausurLabel") or k.MARKE["klausurLabel"] or f"Klausur {kk}"
        frei = (W_ - 64 - F("Bold", 32).getlength(kl) - 44) - 64 - 56 - 28      # Fach-Pille endet vor der Klausur-Pille
        els.append(pille(lbl, 64, 272, C, fill=PASTELL[kk], size=k.passt(lbl, "Bold", 42, min(640, frei), 24), pad=(28, 11)))
        els.append(pille(kl, W_ - 64, 278, C, fill=WEISS, size=32, anker="r", pad=(22, 10)))
        zeilen = h["zeilen"]
        stil, st = h.get("stil", "split"), h.get("stempel") or {}
        # Kippen: Frage oben, Irrtum als eigener Kasten mit Stempel, darunter die Richtig-Aussage (keine Durchstreichung)
        irrtum = zeilen[-1] if stil == "kippen" and len(zeilen) > 1 else None
        kopf_z = zeilen[:-1] if irrtum else zeilen
        gs = 168
        while max(F("ExtraBold", gs).getlength(z) for z in kopf_z) + 40 > 952: gs -= 2
        y0 = 390
        t, y = k.schlagzeile(kopf_z, y0, groesse=gs, abstand=1.12, klausur=kk, x0=64, x1=1016); els += t
        y += 30
        if h.get("pille"):
            els.append(pille(h["pille"], 64, y, C, fill=WEISS, size=k.passt(h["pille"], "Bold", 44, 900, 30), pad=(26, 11))); y += 104
        if stil == "split":
            for i, b in enumerate(h["split"]):
                els.append(fl_block(64 + i * 486, y, 466, 210, FARBEN[b.get("farbe", "WEISS")], C,
                                    [(b["label"], "ExtraBold", k.passt(b["label"], "ExtraBold", 44, 420, 30), INK),
                                     (b["wert"], "ExtraBold", k.passt(b["wert"], "ExtraBold", 70, 420, 40), INK)]))
            y += 236
        elif stil == "kippen":
            if irrtum:
                els.append(fl_block(64, y, 952, 200, (252, 222, 216, 255), C,
                                    [("Irrtum", "Bold", 40, INK), (irrtum, "ExtraBold", k.passt(irrtum, "ExtraBold", 70, 700, 40), INK)]))
                if st:
                    sp = pille(st["text"], 100, 100, C, fill=ROT, size=56, stil="ExtraBold", pad=(30, 12))
                    rot = sp.sprite.rotate(10, resample=Image.BICUBIC, expand=True)
                    els.append(k.engine.El(rot, 1016 - rot.width + 30, y - 46, C, "cut", 0.0, name="stempel"))
                y += 228
            if h.get("richtig"):
                r = h["richtig"]
                fr = FARBEN.get(r.get("farbe")) if isinstance(FARBEN.get(r.get("farbe")), tuple) else GRUEN
                els.append(fl_block(64, y, 952, 200, fr, C, [(r.get("label", "Richtig"), "Bold", 40, INK),
                                                              (r["text"], "ExtraBold", k.passt(r["text"], "ExtraBold", 70, 880, 40), INK)])); y += 228
        elif stil == "knall":
            els.append(kreuz_i(300, y + 130, C, gr=170)); y += 280
        if st and not (stil == "kippen" and irrtum):
            sw = F("Bold", 52).getlength(st["text"]) + 70
            els.append(pille(st["text"], 1016 - sw / 2, y - 10 if stil != "knall" else y - 200, C, fill=ROT, size=52, anker="m", pad=(28, 12)))
            if stil != "knall": y += 70
        assert y <= 1500, f"Reel {self.datum}: Cover zu voll ({y})"
        fig = h.get("figur") or ""
        if fig:
            buchst, _, pose = fig.replace(":", "/").partition("/")
            ref = f"{buchst}:{POSE_MIMIK.get(pose, pose if pose in ('froh', 'sorge', 'fragt', 'ernst', 'staunt') else 'ernst')}"
            oben = max(y + 30, 1000)            # Brustbild füllt den Rest bis unten, ohne Lücke in der Mitte
            els.append(k.nah(self.b.name(ref, 800 if stil != "knall" else 760), 800 if stil != "knall" else 760, oben, 1880 - oben))
        self.T(lbl, kl, *zeilen, h.get("pille"), st.get("text"))
        img = Image.new("RGBA", (W_, H_), k.CREME)
        for e in els:
            self._setze(img, e.sprite, e.x, e.y)
        img.alpha_composite(self.rahmen())
        return img.convert("RGB")

    # ------------------------------------------------------------ Ablauf
    def rendern(self, nur_bilder=None):
        k.STORY.aktiv()
        os.makedirs(self.out, exist_ok=True)
        wav = os.path.join(self.out, "_stimme.wav")
        segs = [(x["id"], x["text"]) for x in self.s["sprecher"]]
        for sid, txt in segs:
            fehl = stimme.aussprache_pruefen(txt)
            assert not fehl, f"Reel {self.datum} {sid}: im Sprechertext ausschreiben: {fehl}"
        Z = stimme.vertonen(segs, wav, pausen={"hook": 0.3, "cta": 0.5})
        assert Z["dauer"] <= k.MARKE["reelMaxS"], f"Reel {self.datum}: {Z['dauer']} s – Sprechertext kürzen"
        self.Z, self.SEG = Z, {s["name"]: s for s in Z["segmente"]}
        starts = [self.SEG[x["id"]]["start"] for x in self.s["sprecher"]]
        ids = [x["id"] for x in self.s["sprecher"]]
        self.kopfzeile()
        t_hook_ende = self.SEG[ids[1]]["start"]
        self.hook(self.s["hook"], t_hook_ende)
        for nr, sz in enumerate(self.s["szenen"], 1):
            i = ids.index(sz["seg"])
            t1 = self.SEG[ids[i + 1]]["start"] if i + 1 < len(ids) else None
            self.szene(sz, nr, self.SEG[sz["seg"]]["start"], t1)
        if self.s.get("merke"):
            self.merke(self.s["merke"], self.SEG[self.s["merke"].get("seg", "cta")]["start"])
        self._cache = {}
        self.RAHMEN = self.rahmen()
        self.BG = Image.new("RGBA", (W_, H_), k.CREME)
        dauer = Z["dauer"] + 0.4
        cover_t = self.s.get("coverZeit") or (self.wort("hook", self.s["hook"]["stempel"]["wort"]) + 0.6 if self.s["hook"].get("stempel") else t_hook_ende - 0.3)
        if nur_bilder:
            for ts in nur_bilder:
                self.bild(ts).save(os.path.join(self.out, f"_t{ts:05.1f}.jpg"), quality=88)
            self.cover_bild().save(os.path.join(self.out, f"{self.datum}-{self.s['slot']}-cover.jpg"), quality=88)
            k.KARUSSELL.aktiv(); return []
        # Ton
        SR = stimme.SR
        w = wave.open(wav); voice = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        mix = np.zeros(int(dauer * SR) + SR, np.float32)
        n = min(len(voice), len(mix)); mix[:n] += voice[:n]
        for name, t, gain in self.SFX:
            pcm = np.frombuffer(subprocess.run([stimme.FF, "-v", "error", "-i", os.path.join(SFX_DIR, name + ".mp3"), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                               capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
            a, b = SCHNITT.get(name, (0, 1.0)); x = pcm[int(a * SR):int(b * SR)].copy()
            x[:480] *= np.linspace(0, 1, min(480, len(x))); x[-3840:] *= np.linspace(1, 0, min(3840, len(x)))
            i = int(t * SR); j = min(len(mix), i + len(x)); mix[i:j] += gain * x[:j - i]
        mix = np.clip(mix, -0.98, 0.98)
        ton = os.path.join(self.out, "_ton.wav")
        ww = wave.open(ton, "wb"); ww.setnchannels(1); ww.setsampwidth(2); ww.setframerate(SR); ww.writeframes((mix * 32767).astype(np.int16).tobytes()); ww.close()
        video = os.path.join(self.out, f"{self.datum}-{self.s['slot']}.mp4")
        ff = imageio_ffmpeg.get_ffmpeg_exe()
        p = subprocess.Popen([ff, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W_}x{H_}", "-r", str(FPS), "-i", "-",
                              "-i", ton, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                              "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", f"{dauer:.2f}",
                              "-movflags", "+faststart", video], stdin=subprocess.PIPE)
        for fr in range(int(dauer * FPS)):
            p.stdin.write(self.bild(fr / FPS).tobytes())
        p.stdin.close(); p.wait()
        cover = os.path.join(self.out, f"{self.datum}-{self.s['slot']}-cover.jpg")
        self.cover_bild().save(cover, quality=92)
        os.remove(wav); os.remove(ton)
        if os.environ.get("OP_TTS_TROCKEN"):
            os.remove(video)
            video = os.path.join(self.out, f"{self.datum}-{self.s['slot']}.trocken")
            open(video, "w").write("Trockenlauf ohne Stimme\n")
        k.KARUSSELL.aktiv()
        return [video, cover]
