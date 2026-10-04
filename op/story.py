"""Stories 1080×1920 (Variante C): Inhalt nur zwischen y 260 und 1660, ≤ 25 Wörter, Schrift ≥ 46 px.

Arten: frage, antwort, teaser, norm, countdown, tipp, merksatz, anlass, fehler, streitstand, begriff, zahl. Keine Sticker (die Graph-API kann sie
nicht setzen): Quiz als Paar aus Frage und Auflösung, Teaser mit dem echten Cover des Beitrags.
"""
import os
from PIL import Image, ImageDraw
import opkern as k
from opkern import (C, F, OT, titel, pille, absatz, fl_block, karte, ficon, markertext, haken_i, warnung_i,
                    WEISS, GELB, GRUEN, LILA, INK, PINK, PASTELL, FARBEN, GRAUTEXT, HELL, FALLE_FILL)

OBEN, UNTEN = 260, 1660
MAX_WORTE = 25


class Stories:
    def __init__(self, stories, besetzung, out_dir, datum, covers):
        self.st, self.b, self.out, self.datum, self.covers = stories, besetzung, out_dir, datum, covers
        self.texte, self.dateien = {}, []
        self._t = []

    def T(self, *t):
        self._t.extend(x for x in t if isinstance(x, str) and x.strip())

    def f(self, ref, cx):
        return self.b.name(ref, cx)

    def kopfzeile(self, s, art_text, art_fill=WEISS):
        kk = int(s["klausur"])
        self.T(s["fachLabel"], art_text)
        return [pille(s["fachLabel"], 64, OBEN, C, fill=PASTELL[kk], size=40, pad=(26, 11)),
                pille(art_text, 64, OBEN + 86, C, fill=art_fill, size=40, stil="ExtraBold", pad=(26, 11))]

    def gross(self, zeilen, y, size, kk, marker=None):
        self.T(*zeilen)
        return k.schlagzeile(zeilen, y, groesse=size, abstand=1.16, klausur=kk, x0=64, x1=1016, marker=marker)

    def speichern(self, s, els, worte):
        datei = f"{s['slot']}-{s['art']}.jpg"
        assert worte <= MAX_WORTE, f"Story {datei}: {worte} Wörter (> {MAX_WORTE})"
        img = k.zusammensetzen(els, int(s["klausur"]), k.STORY, rund=34)
        pfad = os.path.join(self.out, datei)
        img.save(pfad, quality=93)
        self.dateien.append(pfad)
        self.texte[f"{self.datum}-{datei}"] = list(self._t); self._t = []

    def option(self, buchst, text, y, zustand=None, size=54):
        fill = {None: WEISS, "richtig": GRUEN, "falsch": (236, 236, 236, 255)}[zustand]
        farbe = INK if zustand != "falsch" else (150, 150, 155, 255)
        self.T(text)
        e, y2 = absatz(text, 190, y + 34, 790, C, size=size, stil="Bold" if zustand == "richtig" else "Regular", zeilenabstand=1.18, farbe=farbe)
        h = int(y2 - y + 30)
        els = [fl_block(64, y, 952, h, fill, C, [(" ", "Bold", 10, INK)])]
        els.append(pille(buchst, 94, y + h / 2 - 34, C, fill=PASTELL[2] if zustand != "falsch" else WEISS, size=46, stil="ExtraBold", pad=(20, 6)))
        els += e
        if zustand == "richtig": els.append(haken_i(975, y + h / 2, C, gr=32))
        return els, y + h

    def punkte(self, els, liste, y, size=54, normsize=40):
        for p in liste:
            t, z, nm = (list(p) + [None, None])[:3]
            self.T(t, nm)
            e, y2 = absatz(t, 136, y + 24, 870, C, size=size, zeilenabstand=1.2); els += e
            zz = (haken_i(94, y + 58, C, gr=30) if z in (None, "ok") else warnung_i(94, y + 58, C, gr=26) if z == "warn"
                  else k.kreuz_i(94, y + 58, C, gr=28))
            els.append(zz)
            if nm:
                els.append(OT(nm, 136, y2 + 6, C, "Bold", normsize, farbe=GRAUTEXT)); y2 += normsize + 26
            y = y2 + 44
        return y

    # ------------------------------------------------------------ Arten
    def frage(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Prüfungsfrage"))
        t, y = self.gross(s["frage"], OBEN + 200, 104, kk); els += t; y += 30
        for i, o in enumerate(s["optionen"]):
            e, y = self.option("ABC"[i], o, y); els += e; y += 22
        hinweis = s.get("hinweis", "Auflösung in der nächsten Story"); self.T(hinweis)
        e, _ = absatz(hinweis, 64, y + 20, 520, C, size=44, stil="Bold", farbe=GRAUTEXT); els += e
        if s.get("figur"):
            els.append(k.nah(self.f(s["figur"], 790), 790, int(y + 80), 600))
        self.speichern(s, els, k.worte(*s["frage"], *s["optionen"], hinweis))

    def antwort(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Auflösung"), GRUEN)
        t, y = self.gross(s["titel"], OBEN + 200, 96, kk); els += t; y += 30
        for i, o in enumerate(s["optionen"]):
            e, y = self.option("ABC"[i], o, y, "richtig" if i == s["richtig"] else "falsch", size=48); els += e; y += 18
        self.T(s["text"], s.get("norm"))
        e, y = absatz(s["text"], 64, y + 20, 952, C, size=54, zeilenabstand=1.25); els += e
        if s.get("norm"):
            els.append(OT(s["norm"], 64, y + 12, C, "Bold", 42, farbe=GRAUTEXT))
        if s.get("figur"):
            els.append(k.nah(self.f(s["figur"], 820), 820, int(y + 70), 520))
        self.speichern(s, els, k.worte(*s["titel"], s["text"]) + (1 if s.get("norm") else 0))

    def teaser(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Neu im Feed"), GELB)
        bild = self.covers[s["beitragSlot"]]
        reel = bild.endswith("-cover.jpg")
        breite = 560 if reel else 740
        im = Image.open(bild).convert("RGBA")
        h = int(im.height * breite / im.width)
        im = im.resize((breite, h), Image.LANCZOS)
        rahmen = Image.new("RGBA", (breite + 60, h + 60)); d = ImageDraw.Draw(rahmen)
        d.rounded_rectangle((22, 22, breite + 34, h + 34), 26, fill=INK)
        d.rounded_rectangle((8, 8, breite + 20, h + 20), 26, fill=INK)
        rahmen.alpha_composite(im, (14, 14))
        rahmen = rahmen.rotate(-4, resample=Image.BICUBIC, expand=True)
        y0 = OBEN + 190
        els.append(k.engine.El(rahmen, (k.STORY.W - rahmen.width) // 2, y0, C, "pop", 0.0, name="cover"))
        y = y0 + rahmen.height + 20
        t, y = self.gross(s["titel"], y, 90, kk); els += t
        self.T(s["unter"])
        els.append(OT(s["unter"], 64, y + 18, C, "Bold", k.passt(s["unter"], "Bold", 48, 940, 34), farbe=GRAUTEXT))
        self.speichern(s, els, k.worte(*s["titel"], s["unter"]))

    def norm(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Norm des Tages"))
        t, y = self.gross(s["titel"], OBEN + 200, 112, kk); els += t
        self.T(s["norm"])
        nt = k.titel_passend(s["norm"], 48, y + 8, 84, rechts=1030, marker=LILA); els.append(nt); y += 150
        y = self.punkte(els, s["punkte"], y, size=56, normsize=42)
        if s.get("figur"):
            els.append(k.nah(self.f(s["figur"], 300), 300, int(y + 10), 600))
        self.speichern(s, els, k.worte(*s["titel"], *[p[0] for p in s["punkte"]]) + 1 + sum(1 for p in s["punkte"] if len(p) > 2 and p[2]))

    def countdown(self, s):
        els = self.kopfzeile(s, s.get("ueberzeile", "Countdown"))
        self.T(s.get("monat", "NOCH"), str(s["zahl"]), s.get("einheit", "Tage"))
        els.append(k.kalenderblatt(330, OBEN + 200, 500, s.get("monat", "NOCH"), str(s["zahl"]), s.get("einheit", "Tage")))
        y = OBEN + 200 + 570
        t, y = self.gross([s["titel"]], y, 104, 0); els += t; y += 40
        for txt in s["punkte"]:
            self.T(txt)
            els.append(haken_i(98, y + 40, C, gr=34)); els.append(OT(txt, 150, y, C, "ExtraBold", 62)); y += 112
        if s.get("figur"):
            els.append(k.peep(self.f(s["figur"], 830), 830, OBEN + 770, 700))
        self.speichern(s, els, k.worte(s.get("monat", "NOCH"), str(s["zahl"]), s.get("einheit", "Tage"), s["titel"], *s["punkte"]))

    def tipp(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Klausurtipp"))
        t, y = self.gross(s["titel"], OBEN + 200, 100, kk, marker=LILA if s.get("normImTitel") else None); els += t; y += 10
        y = self.punkte(els, s["punkte"], y, size=54, normsize=40)
        if s.get("icon"):
            setn, nm = s["icon"].split(":")
            els.append(ficon(setn, nm, 790, UNTEN - 10, 260, C, fuell=FARBEN.get(s.get("iconFarbe"), GELB)))
        if s.get("figur"):
            hf = int(UNTEN - 10 - (y + 30))
            if hf >= 420:
                els.append(k.peep(self.f(s["figur"], 330), 330, UNTEN - 10, hf))
        self.speichern(s, els, k.worte(*s["titel"], *[p[0] for p in s["punkte"]]) + sum(1 for p in s["punkte"] if len(p) > 2 and p[2]))

    def merksatz(self, s):
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Merksatz"))
        t, y = self.gross(s["titel"], OBEN + 200, 92, kk); els += t
        els.append(karte(64, y + 50, 952, 560, C, fill=(255, 251, 230, 255)))
        zeilen = [[(a, m or 0) for a, m in z] for z in s["zeilen"]]
        self.T(*["".join(a for a, _ in z) for z in zeilen])
        groesse = s.get("groesse", 66)
        els += markertext(zeilen, 540, y + 110, groesse, C, {"a": C, "b": C, "c": C, "d": C}, marker=PINK, lh=1.3)
        if s.get("norm"):
            self.T(s["norm"]); els.append(OT(s["norm"], 92, y + 640, C, "Bold", 44, farbe=GRAUTEXT))
        if s.get("figur"):
            els.append(k.nah(self.f(s["figur"], 800), 800, int(y + 700), 600))
        self.speichern(s, els, k.worte(*s["titel"], *[a for z in zeilen for a, _ in z]) + (1 if s.get("norm") else 0))

    def anlass(self, s):
        """Prüfungstag/Anlass: große Schlagzeile, kurze Ermutigung, Figur."""
        kk = int(s.get("klausur", 0)); els = self.kopfzeile(s, s.get("ueberzeile", "Heute"))
        t, y = self.gross(s["titel"], OBEN + 200, 112, kk); els += t; y += 30
        self.T(s.get("text"))
        if s.get("text"):
            e, y = absatz(s["text"], 64, y, 952, C, size=56, zeilenabstand=1.25); els += e
        y = self.punkte(els, s.get("punkte", []), y + 20)
        if s.get("figur"):
            els.append(k.nah(self.f(s["figur"], 540), 540, int(y + 20), 700))
        self.speichern(s, els, k.worte(*s["titel"], s.get("text"), *[p[0] for p in s.get("punkte", [])]))

    def textkarte(self, els, y, kopf, text, fill, size=52, zeichen=None, norm=None):
        """Karte mit kleiner Kopfzeile und Fließtext; Höhe nach dem Text. Gibt die Unterkante zurück."""
        self.T(kopf, text, norm)
        e, y2 = absatz(text, 104, y + 92, 872, C, size=size, zeilenabstand=1.22)
        if norm:
            e.append(OT(norm, 104, y2 + 6, C, "Bold", 40, farbe=GRAUTEXT)); y2 += 52
        h = int(y2 - y + 36)
        els.append(karte(64, y, 952, h, C, fill=fill))
        els.append(OT(kopf, 104 + (52 if zeichen else 0), y + 28, C, "ExtraBold", 42))
        if zeichen == "nein": els.append(k.kreuz_i(124, y + 54, C, gr=26))
        elif zeichen == "ok": els.append(haken_i(124, y + 54, C, gr=28))
        els += e
        return y + h

    def fehler(self, s):
        """Typischer Fehler: Irrtum (rot) und Richtig (grün) als zwei Karten."""
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Typischer Fehler"))
        t, y = self.gross(s["titel"], OBEN + 200, 96, kk); els += t
        y = self.textkarte(els, y + 30, "Falsch", s["falsch"], FALLE_FILL, zeichen="nein")
        y = self.textkarte(els, y + 30, "Richtig", s["richtig"], (226, 245, 228, 255), zeichen="ok", norm=s.get("norm"))
        if s.get("figur") and UNTEN - y >= 380:
            els.append(k.nah(self.f(s["figur"], 820), 820, int(y + 40), min(520, UNTEN - y - 20)))
        self.speichern(s, els, k.worte(*s["titel"], s["falsch"], s["richtig"]) + (1 if s.get("norm") else 0))

    def streitstand(self, s):
        """Streitstand: zwei Ansichten als Karten, darunter die Klausurempfehlung."""
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Streitstand"))
        t, y = self.gross(s["titel"], OBEN + 200, 92, kk); els += t; y += 20
        for i, (kopf, text) in enumerate(s["ansichten"]):
            y = self.textkarte(els, y + 10, kopf, text, WEISS if i == 0 else HELL, size=50) + 14
        if s.get("klausur_tipp"):
            self.T(s["klausur_tipp"])
            e, y2 = absatz(s["klausur_tipp"], 136, y + 30, 870, C, size=50, stil="Bold", zeilenabstand=1.2)
            els.append(warnung_i(94, y + 62, C, gr=26)); els += e; y = y2
        if s.get("norm"):
            self.T(s["norm"]); els.append(OT(s["norm"], 64, y + 20, C, "Bold", 42, farbe=GRAUTEXT)); y += 70
        if s.get("figur") and UNTEN - y >= 380:
            els.append(k.nah(self.f(s["figur"], 820), 820, int(y + 40), min(560, UNTEN - y - 20)))
        self.speichern(s, els, k.worte(*s["titel"], *[x for a in s["ansichten"] for x in a], s.get("klausur_tipp")) + (1 if s.get("norm") else 0))

    def begriff(self, s):
        """Begriff des Tages: Begriff groß, Definition auf heller Karte, Norm, Figur."""
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Begriff des Tages"))
        t, y = self.gross(s["titel"], OBEN + 200, 104, kk); els += t
        y = self.textkarte(els, y + 40, s.get("kopf", "Definition"), s["text"], HELL, size=54, norm=s.get("norm"))
        if s.get("figur") and UNTEN - y >= 380:
            els.append(k.nah(self.f(s["figur"], 820), 820, int(y + 40), min(560, UNTEN - y - 20)))
        self.speichern(s, els, k.worte(*s["titel"], s.get("kopf", "Definition"), s["text"]) + (1 if s.get("norm") else 0))

    def zahl(self, s):
        """Zahl des Tages: große Zahl links, Titel daneben, darunter die Punkte."""
        kk = int(s["klausur"]); els = self.kopfzeile(s, s.get("ueberzeile", "Zahl des Tages"))
        self.T(s["zahl"])
        zs = k.passt(s["zahl"], "ExtraBold", 230, 330, 120)
        els.append(k.zahlblock(64, OBEN + 200, 380, 330, FARBEN.get(s.get("farbe"), GELB), s.get("einheit", " "), s["zahl"], zs=zs, ls=40))
        self.T(*s["titel"])
        yy = OBEN + 210
        for z in s["titel"]:
            gr = k.passt(z, "ExtraBold", 72, 540, 46)
            els.append(OT(z, 476, yy, C, "ExtraBold", gr)); yy += int(gr * 1.2)
        y = self.punkte(els, s["punkte"], max(OBEN + 560, yy + 30), size=52, normsize=40)
        if s.get("figur") and UNTEN - y >= 380:
            els.append(k.nah(self.f(s["figur"], 820), 820, int(y + 40), min(560, UNTEN - y - 20)))
        self.speichern(s, els, k.worte(s["zahl"], *s["titel"], *[p[0] for p in s["punkte"]]) + sum(1 for p in s["punkte"] if len(p) > 2 and p[2]))

    def rendern(self):
        k.STORY.aktiv()
        os.makedirs(self.out, exist_ok=True)
        for s in self.st:
            getattr(self, s["art"])(s)
        k.KARUSSELL.aktiv()
        return self.dateien
