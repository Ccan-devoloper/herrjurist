"""Karussell 1080×1350 aus der Tagesbeschreibung (Folientypen siehe REDAKTION.md)."""
import os
import opkern as k
from opkern import (C, F, OT, titel, pille, absatz, fl_block, karte, ficon, icon, markertext, haken_i,
                    WEISS, GELB, GRUEN, ROT, LILA, INK, PINK, PASTELL, FARBEN, HELL, FALLE_FILL, GRAUTEXT, TITEL, TEXT, KLEIN,
                    X0, X1)

MAX_WORTE = 40
MAX_FOLIEN = 10   # Grenze der Instagram-Graph-API für Karussells (die App erlaubt 20, die API nur 10)


class Karussell:
    def __init__(self, spec, besetzung, out_dir, datum):
        self.s, self.b, self.out, self.datum = spec, besetzung, out_dir, datum
        self.k = int(spec["klausur"])
        self.n = len(spec["folien"])
        self.texte, self.dateien, self.worte = {}, [], {}
        self._t = []

    # ------------------------------------------------------------ Hilfen
    def f(self, ref, cx):
        return self.b.name(ref, cx)

    def T(self, *t):
        self._t.extend(x for x in t if isinstance(x, str) and x.strip())

    def kopf(self, seite):
        self.T(self.s["fachLabel"])
        return [pille(self.s["fachLabel"], 48, 46, C, fill=PASTELL[self.k], size=34),
                pille(f"{seite}/{self.n}", 1032, 46, C, fill=WEISS, size=KLEIN, anker="r", pad=(20, 8))]

    def speichern(self, els, seite, worte, ausnahme=False):
        datei = f"{self.datum}-{self.s['slot']}-{seite:02d}.jpg"
        if not ausnahme:
            assert worte <= MAX_WORTE, f"{datei}: {worte} Wörter (> {MAX_WORTE})"
        img = k.zusammensetzen(els, self.k, k.KARUSSELL)
        pfad = os.path.join(self.out, datei)
        img.save(pfad, quality=93)
        self.dateien.append(pfad)
        self.texte[datei] = list(self._t); self._t = []
        self.worte[datei] = worte

    def punkte(self, liste, y, x=148, breite=840, size=TEXT):
        els = []
        for p in liste:
            t, z, st, nm = (list(p) + [None, "Regular", None])[:4]
            self.T(t, nm)
            e, y2 = absatz(t, x, y, breite, C, size=size, stil=st or "Regular", zeilenabstand=1.32)
            els += e
            zz = k.zeichen(z, x - 36, y + 30)
            if zz: els.append(zz)
            if nm:
                els.append(OT(nm, x, y2 + 4, C, "Bold", 30, farbe=GRAUTEXT)); y2 += 46
            y = y2 + 26
        return els, y

    def figur_unten(self, els, ref, cx, unten, blase_=None, max_h=520):
        if not ref:
            return
        self.T(blase_)
        k.blase_zu(els, (self.f(ref, cx), cx), unten, blase_, max_h)

    # ------------------------------------------------------------ Folientypen
    def cover(self, f, seite):
        els = [pille(self.s["fachLabel"], X0, 50, C, fill=PASTELL[self.k], size=34),
               pille(f["badge"], X0, 140, C, fill=FARBEN.get(f.get("badgeFarbe"), GELB), size=46, pad=(26, 10))]
        self.T(self.s["fachLabel"], f["badge"], *f["zeilen"], f.get("norm"), f.get("unter"), f.get("teaser"))
        t, y = k.schlagzeile(f["zeilen"], 232, klausur=self.k); els += t
        if f.get("norm"):
            nt, y = k.norm_titel(f["norm"], y); els.append(nt)
        else:
            y += 18
        if f.get("unter"):
            els.append(OT(f["unter"], X0 + 4, y, C, "ExtraBold", 56))
            if f.get("teaser"):
                tx = X0 + 4 + F("ExtraBold", 56).getlength(f["unter"]) + 28
                ts = k.passt(f["teaser"], "ExtraBold", 34, 1020 - tx - 40, 26)
                assert tx + F("ExtraBold", ts).getlength(f["teaser"]) + 40 <= 1020, f"{self.s['slot']}-{seite}: Cover-Teaser zu lang: {f['teaser']}"
                els.append(pille(f["teaser"], tx, y - 2 + (34 - ts) // 2, C, fill=GELB, size=ts, stil="ExtraBold", pad=(20, 9)))
            y += 70
        m = f.get("motiv") or {}
        if m.get("typ") == "kalender":
            self.T(m["monat"], m["tag"], m["unter"])
            els.append(k.kalenderblatt(255, y + 40, 330, m["monat"], m["tag"], m["unter"]))
        elif m.get("typ") == "zahlblock":
            z = m["zeilen"]; self.T(*[a for a, *_ in z])
            els.append(fl_block(X0, y + 40, 540, 330, WEISS, C, [(a, b, c, INK) for a, b, c in z]))
        elif m.get("typ") == "icon":
            setn, nm = m["name"].split(":")
            els.append(ficon(setn, nm, 280, min(k.AKTIV.innen_unten - 60, y + 420), 320, C, fuell=FARBEN.get(m.get("farbe"), GELB)))
        if f.get("figur"):
            cx = 800 if m else 700
            els.append(k.nah(self.f(f["figur"], cx), cx, y + 30, 680))
        self.speichern(els, seite, k.worte(f["badge"], *f["zeilen"], f.get("unter"), f.get("teaser"), m.get("monat"), m.get("tag"), m.get("unter"),
                                           *[a for a, *_ in m.get("zeilen", [])]) + (1 if f.get("norm") else 0))

    def schritte(self, f, seite):
        els = self.kopf(seite)
        inhalt = [k.titel_passend(f["titel"], 88, 168, TITEL, marker=PASTELL[self.k])]; self.T(f["titel"])
        y = 300
        for i, (t, norm, txt) in enumerate(f["schritte"]):
            self.T(t, norm, txt)
            inhalt.append(pille(str(i + 1), 92, y - 2, C, fill=PASTELL[self.k], size=46, pad=(24, 8)))
            inhalt.append(OT(t, 186, y, C, "ExtraBold", 48))
            if txt:
                e, y = absatz(txt, 186, y + 68, 802, C, size=40); inhalt += e
            else:
                y += 62
            if norm:
                inhalt.append(OT(norm, 186, y + 4, C, "Bold", 32, farbe=GRAUTEXT)); y += 40
            y += 30                                     # gleicher Abstand zwischen allen Schritten, mit oder ohne Norm
        kk, unten = k.karte_um(inhalt); els += kk
        n = k.worte(f["titel"], *[a + " " + (b or "") for a, _, b in f["schritte"]]) + sum(1 for _, nm, _ in f["schritte"] if nm)
        if f.get("teaser"):
            self.T(f["teaser"])
            assert unten + 40 + 120 <= k.AKTIV.innen_unten - 10, f"{self.s['slot']}-{seite}: Teaser passt nicht"
            yb = unten + max(40, (k.AKTIV.innen_unten - unten - 130) // 2)
            els.append(fl_block(48, yb, 984, 120, GELB, C, [(" ", "Bold", 10, INK)]))
            els.append(ficon("tabler", "highlight", 130, yb + 104, 80, C, fuell=WEISS))
            ts = k.passt(f["teaser"], "ExtraBold", 44, 1000 - 200, 32)
            assert F("ExtraBold", ts).getlength(f["teaser"]) <= 800, f"{self.s['slot']}-{seite}: Teaser-Leiste zu lang: {f['teaser']}"
            els.append(OT(f["teaser"], 200, yb + 60 - int(ts * 0.6), C, "ExtraBold", ts))
            n += k.worte(f["teaser"]) - 1
        self.speichern(els, seite, n)

    def inhalt(self, f, seite):
        els = self.kopf(seite)
        y0, inhalt = 168, []
        falle = bool(f.get("falle"))
        if falle:
            inhalt.append(pille("Klausurfalle", 88, 150, C, fill=ROT, size=40, pad=(24, 10))); y0 = 262
        self.T(f["titel"])
        inhalt.append(k.titel_passend(f["titel"], 88, y0, TITEL, marker=ROT if falle else PASTELL[self.k]))
        e, y = self.punkte(f.get("punkte", []), y0 + 104); inhalt += e
        ex = f.get("extra")
        if ex:
            txt, farbe, nm = (list(ex) + [None, None])[:3]
            self.T(txt, nm)
            inhalt.append(fl_block(92, y + 4, 896, 96, FARBEN.get(farbe, GELB), C, [(txt, "ExtraBold", k.passt(txt, "ExtraBold", TEXT, 860, 32), INK)])); y += 110
            if nm:
                inhalt.append(OT(nm, 100, y + 2, C, "Bold", 30, farbe=GRAUTEXT)); y += 46
        if f.get("fundstellen"):
            fs = "Fundstellen: " + "; ".join(f["fundstellen"]); self.T(fs)
            e, y = absatz(fs, 92, y + 8, 896, C, size=30, stil="Bold", farbe=GRAUTEXT); inhalt += e
        kk, unten = k.karte_um(inhalt, fill=FALLE_FILL if falle else WEISS); els += kk
        if f.get("figur"):
            cx = f.get("x", 790)
            self.figur_unten(els, f["figur"], cx, unten, f.get("blase"))
        if f.get("kalender"):
            (m1, t1, u1), (m2, t2, u2) = f["kalender"]
            self.T(m1, t1, u1, m2, t2, u2)
            w = min(300, int((k.AKTIV.innen_unten - unten - 90) / 1.08))
            oben = unten + 50 + (k.AKTIV.innen_unten - unten - 90 - int(w * 1.08)) // 2
            els.append(k.kalenderblatt(300, oben, w, m1, t1, u1))
            els.append(k.kalenderblatt(780, oben, w, m2, t2, u2))
            els.append(ficon("tabler", "arrow-big-right", 540, oben + int(w * 0.75), 130, C, fuell=GELB))
        n = (k.worte(f["titel"], *[p[0] for p in f.get("punkte", [])], ex[0] if ex else "", f.get("blase"))
             + sum(1 for p in f.get("punkte", []) if len(p) > 3 and p[3]) + (1 if ex and len(ex) > 2 and ex[2] else 0)
             + len(f.get("fundstellen") or []) + (1 if falle else 0))
        self.speichern(els, seite, n)

    def zeitstrahl(self, f, seite):
        els = self.kopf(seite)
        inhalt = [k.titel_passend(f["titel"], 88, 168, TITEL, marker=PASTELL[self.k])]; self.T(f["titel"])
        y = 290
        for d_, t, farbe, norm in f["zeilen"]:
            self.T(d_, t, norm)
            h = 178 if norm else 120
            inhalt.append(fl_block(92, y, 896, h, FARBEN.get(farbe, WEISS), C, [(" ", "Bold", 10, INK)]))
            zs = k.passt(f"{d_}   {t}", "ExtraBold", 48, 896 - 64, 36)
            assert F("ExtraBold", zs).getlength(f"{d_}   {t}") <= 896 - 64, f"{self.s['slot']}-{seite}: Zeitstrahl-Zeile zu lang: {d_} {t}"
            inhalt.append(OT(f"{d_}   {t}", 124, y + 30 + (48 - zs) // 2, C, "ExtraBold", zs))
            if norm:
                ns = k.passt(norm, "Bold", 34, 896 - 64, 28)
                assert F("Bold", ns).getlength(norm) <= 896 - 64, f"{self.s['slot']}-{seite}: Norm zu lang: {norm}"
                inhalt.append(OT(norm, 124, y + 110, C, "Bold", ns, farbe=GRAUTEXT))
            y += h + 22
        kk, unten = k.karte_um(inhalt); els += kk
        if f.get("figur"):
            self.figur_unten(els, f["figur"], f.get("x", 290), unten, f.get("blase"))
        self.speichern(els, seite, k.worte(f["titel"], *[a + " " + b for a, b, _, _ in f["zeilen"]], f.get("blase"))
                       + sum(1 for z in f["zeilen"] if z[3]))

    def rechnung(self, f, seite):
        els = self.kopf(seite)
        inhalt = [k.titel_passend(f["titel"], 88, 168, TITEL, marker=PASTELL[self.k])]; self.T(f["titel"])
        y = 268
        if f.get("normen"):
            z = " · ".join(f["normen"]); self.T(z)
            inhalt.append(OT(z, 92, y, C, "Bold", 34, farbe=GRAUTEXT)); y += 56
        y += 50
        for lab, betrag, stil, farbe in f["zeilen"]:
            self.T(lab, betrag)
            if farbe:
                inhalt.append(fl_block(84, y - 24, 912, 102, FARBEN[farbe], C, [(" ", "Bold", 10, INK)]))
            bw = F("ExtraBold", TEXT + 8).getlength(betrag)
            inhalt.append(OT(lab, 110, y, C, stil or "Regular", k.passt(lab, stil or "Regular", TEXT + 6, 970 - bw - 150, 30)))
            inhalt.append(OT(betrag, 970, y, C, "ExtraBold", TEXT + 8, anker="r"))
            y += 142 if len(f["zeilen"]) <= 6 else 118
        ex = f.get("extra")
        if ex:
            self.T(ex[0])
            inhalt.append(fl_block(84, y + 6, 912, 110, FARBEN.get(ex[1], ROT), C, [(ex[0], "ExtraBold", k.passt(ex[0], "ExtraBold", 46, 870), INK)])); y += 130
        kk, unten = k.karte_um(inhalt); els += kk
        if f.get("figur"):
            self.figur_unten(els, f["figur"], f.get("x", 790), unten, f.get("blase"))
        self.speichern(els, seite, k.worte(f["titel"], *[a + " " + b for a, b, _, _ in f["zeilen"]], ex[0] if ex else "", f.get("blase"))
                       + len(f.get("normen") or []))

    def vergleich(self, f, seite):
        """Gegenüberstellung: zwei Spalten, Normen grau unter den Punkten."""
        els = self.kopf(seite)
        inhalt = [k.titel_passend(f["titel"], 88, 168, TITEL, marker=PASTELL[self.k])]; self.T(f["titel"])
        n = k.worte(f["titel"])
        ymax = 0
        for i, seite_ in enumerate((f["links"], f["rechts"])):
            x = 84 + i * 466
            self.T(seite_["kopf"])
            inhalt.append(fl_block(x, 280, 446, 96, FARBEN.get(seite_.get("farbe"), WEISS), C, [(seite_["kopf"], "ExtraBold", k.passt(seite_["kopf"], "ExtraBold", 42, 410), INK)]))
            y = 400; n += k.worte(seite_["kopf"])
            for p in seite_["punkte"]:
                t, nm = (list(p) + [None])[:2] if isinstance(p, (list, tuple)) else (p, None)
                self.T(t, nm)
                e, y = absatz(t, x + 10, y, 420, C, size=38, zeilenabstand=1.28); inhalt += e
                if nm:
                    inhalt.append(OT(nm, x + 10, y + 2, C, "Bold", 30, farbe=GRAUTEXT)); y += 44; n += 1
                y += 26; n += k.worte(t)
            ymax = max(ymax, y)
        inhalt.append(k.linienzug([(540, 300), (540, ymax - 10)], C, breite=4, farbe=INK))
        kk, unten = k.karte_um(inhalt); els += kk
        if f.get("figur"):
            self.figur_unten(els, f["figur"], f.get("x", 790), unten, f.get("blase"))
            n += k.worte(f.get("blase"))
        self.speichern(els, seite, n)

    def merke(self, f, seite):
        els = self.kopf(seite)
        y0 = 128
        n = 0
        if f.get("oben"):
            t1, t2, farbe = f["oben"]; self.T(t1, t2)
            els.append(fl_block(48, y0, 984, 190, FARBEN.get(farbe, GELB), C, [(t1, "ExtraBold", k.passt(t1, "ExtraBold", 46, 940), INK), (t2, "Bold", k.passt(t2, "Bold", 38, 940), INK)]))
            y0 += 230; n += k.worte(t1, t2)
        inhalt = [titel("Merke", 540, y0 + 40, C, 80, anker="m", marker=PASTELL[self.k])]
        zeilen = [[(t, m or 0) for t, m in z] for z in f["zeilen"]]
        self.T(*["".join(t for t, _ in z) for z in zeilen])
        inhalt += markertext(zeilen, 540, y0 + 190, f.get("groesse", 58), C, {"a": C, "b": C, "c": C, "d": C}, marker=PINK, lh=1.35)
        kk, unten = k.karte_um(inhalt, y=y0, fill=HELL); els += kk
        reihen = [(f["speichern"], "bookmark", WEISS), (f["frage"], "message-circle", WEISS)]
        if f.get("teaser"):
            reihen.append((f["teaser"], "highlight", GELB))
        for i, (t, ic, farbe) in enumerate(reihen):
            self.T(t)
            els.append(icon("tabler", ic, 100, unten + 86 + i * 104, 58, C))
            ps = k.passt(t, "Bold", 38, 1020 - 150 - 60, 30)
            assert 150 + F("Bold", ps).getlength(t) + 60 <= 1020, f"{self.s['slot']}-{seite}: Zeile zu lang: {t}"
            els.append(pille(t, 150, unten + 54 + i * 104 + (38 - ps) // 2, C, fill=farbe, size=ps))
        n += k.worte(*[t for z in zeilen for t, _ in z], *[t for t, _, _ in reihen])
        self.speichern(els, seite, n)

    def gesetz(self, f, seite):
        """Im Gesetz (oder im Erlass/in der Richtlinie) markieren: Seite mit Markierungen, Randnotizen in Handschrift, Hinweiskasten.
        Für Verwaltungsanweisungen titel="Im Erlass markieren" bzw. "In der Richtlinie markieren" und kopf mit Beck-Erlass-Fundstelle.
        Optional "zweite": {kopf, absaetze, notizen} – zweite Seite (meist die Verwaltungsanweisung) unter der ersten auf
        derselben Folie; so bleiben Gesetz und Richtlinie/Erlass zusammen in der 10-Folien-Grenze."""
        els = self.kopf(seite)
        titel_ = f.get("titel") or ("Gesetz und Richtlinie markieren" if f.get("zweite") else "Im Gesetz markieren")
        els.append(k.titel_passend(titel_, 64, 150, TITEL, rechts=1016, marker=PASTELL[self.k]))
        PW, PX, PY = 700, 56, 252
        seiten = [f] + ([f["zweite"]] if f.get("zweite") else [])
        zwei = len(seiten) > 1
        kasten_h = 140 if zwei else 170
        unten_frei = (kasten_h + 36) if f.get("randnotiz") else 30
        abstand = 26 if zwei else 34
        for gr in range(37 if len(seiten) == 1 else 33, 21, -1):
            gebaut, y = [], PY
            for sd in seiten:
                el, pos, h = k.gesetzesseite(PX, y, PW, sd["kopf"], sd["absaetze"], size=gr, kompakt=zwei)
                gebaut.append((sd, el, pos, y, h)); y += h + abstand
            if y - abstand + unten_frei <= k.AKTIV.innen_unten - 20:
                break
        assert y - abstand + unten_frei <= k.AKTIV.innen_unten - 20 + 60, f"Folie {seite}: Gesetzesauszüge zu lang"
        hand, NX = k.HAND(int(min(44, max(30, gr * 1.3)))), PX + PW + 30   # Handschrift wächst mit der Textgröße, damit Notizen bei engen Zeilen auf Höhe bleiben
        NW = 1030 - NX
        rot = (205, 40, 40, 255)
        from PIL import Image, ImageDraw
        frei = PY + 90
        for sd, el, pos, sy, h in gebaut:
            els.append(el)
            self.T(sd["kopf"])
            frei = max(frei, sy + (64 if zwei else 90))
            for txt, mk in sd.get("notizen", []):
                self.T(txt)
                x0, y0, x1, y1 = pos[mk][0]
                zl, cur = [], ""
                for w_ in txt.split(" "):
                    if cur and hand.getlength(cur + " " + w_) > NW - 10: zl.append(cur); cur = w_
                    else: cur = (cur + " " + w_).strip()
                zl.append(cur)
                zh = hand.size + 2
                ny = max(sy + y0 + gr // 2 - zh // 2 - 2, frei)   # Pfeil auf Mitte der markierten Zeile
                im = Image.new("RGBA", (NW + 60, zh * len(zl) + 20)); dd = ImageDraw.Draw(im)
                for i, z_ in enumerate(zl):
                    dd.text((40, 2 + i * zh), z_, font=hand, fill=rot)
                ay = zh // 2 + 2
                dd.line((4, ay, 32, ay), fill=rot, width=4); dd.line((4, ay, 16, ay - 10), fill=rot, width=4); dd.line((4, ay, 16, ay + 10), fill=rot, width=4)
                els.append(k.engine.El(im, NX - 40, ny, C, "fade", 0.0, name="notiz"))
                frei = ny + zh * len(zl) + (18 if zh >= 44 else 6)
        letzte = gebaut[-1]
        yb = max(letzte[3] + letzte[4] + 46, frei + 10)
        if f.get("randnotiz"):
            t1, t2 = f["randnotiz"]; self.T(t1, t2)
            yb = min(yb, k.AKTIV.innen_unten - 20 - kasten_h)
            els.append(fl_block(56, yb, 968, kasten_h, GELB, C, [(t1, "ExtraBold", k.passt(t1, "ExtraBold", 40 if zwei else 44, 930), INK), (t2, "Bold", k.passt(t2, "Bold", 34 if zwei else 38, 930), INK)]))
        self.speichern(els, seite, 0, ausnahme=True)

    # ------------------------------------------------------------ Ablauf
    def rendern(self):
        k.KARUSSELL.aktiv()
        os.makedirs(self.out, exist_ok=True)
        n = len(self.s["folien"])
        assert n <= MAX_FOLIEN, f"{self.s['slot']}: {n} Folien (> {MAX_FOLIEN}, die API veröffentlicht nur die ersten {MAX_FOLIEN})"
        for i, f in enumerate(self.s["folien"], 1):
            getattr(self, f["typ"])(f, i)
        return self.dateien
