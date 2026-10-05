"""Rendert einen Tag der Open-Peeps-Vorproduktion aus op/tage/<datum>.json.

    python3 op/tag.py 2026-10-04 --ziel <instagram-assets-Checkout> [--nur b1,stories] [--ohne-reel] [--pruefen-nur]

Ergebnis (Vertrag mit src/vorproduktion-live.mjs und dem Dashboard):
    <ziel>/vorproduktion/<datum>/fertig/b1/<datum>-b1-01.jpg …   Karussell-Folien
    <ziel>/vorproduktion/<datum>/fertig/b3/<datum>-b3.mp4 + -cover.jpg   Reel
    <ziel>/vorproduktion/<datum>/fertig/stories/<slot>-<art>.jpg   Stories
    <ziel>/vorproduktion/<datum>.json   Plan, Inhalte (Captions, Folientexte), renderVorschau
    <ziel>/vorproduktion/index.json   Eintrag des Tages (Dashboard)
Vor dem Schreiben laufen die Regelprüfungen: Wortgrenzen (im Renderer), Quellenregeln (bin/op-pruefen.mjs).
"""
import argparse, datetime, glob, json, os, shutil, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import opkern as k
from figuren import Besetzung
from karussell import Karussell
from story import Stories

SOCIAL = os.path.dirname(HIER)
TAGE = os.path.join(HIER, "tage")


def lade(datum):
    return json.load(open(os.path.join(TAGE, datum + ".json"), encoding="utf-8"))


def quellenpruefung(texte_json):
    r = subprocess.run(["node", os.path.join(SOCIAL, "bin", "op-pruefen.mjs"), texte_json], cwd=SOCIAL, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        raise SystemExit(f"Quellenprüfung mit Befund – nichts geschrieben.\n{r.stderr}")


def folien_eintraege(texte, datum, slot, n):
    out = []
    for i in range(1, n + 1):
        t = texte.get(f"{datum}-{slot}-{i:02d}.jpg", [])
        t = [x for x in t if x.strip()]
        f = {"art": "titel" if i == 1 else "text", "titel": t[1] if i == 1 and len(t) > 1 else (t[0] if t else ""), "text": " · ".join(t[1:])}
        if i == 1: f["bild"] = "op-cover"     # kein Icon-Cover des alten Renderers
        out.append(f)
    return out


def zeichen_pruefen(spec):
    """Alle sichtbaren Zeichen müssen in Nunito vorhanden sein (sonst leere Kästchen im Bild)."""
    from fontTools.ttLib import TTFont
    cmap = TTFont(os.path.join(k.RES, "fonts", "Nunito.ttf")).getBestCmap()
    fehlend = set()
    def lauf(x):
        if isinstance(x, str):
            fehlend.update(ch for ch in x if ord(ch) > 31 and ord(ch) not in cmap and ch not in "\n\t")
        elif isinstance(x, list):
            for y in x: lauf(y)
        elif isinstance(x, dict):
            for key, y in x.items():
                if key not in ("caption", "sprecher", "figuren", "absaetze"): lauf(y)
    lauf(spec)
    if fehlend:
        raise SystemExit(f"Zeichen ohne Glyphe in Nunito: {' '.join(sorted(fehlend))} – bitte umschreiben (z. B. → als „dann“ oder „:“).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("datum")
    ap.add_argument("--ziel", required=True)
    ap.add_argument("--nur", default="")
    ap.add_argument("--ohne-reel", action="store_true")
    ap.add_argument("--pruefen-nur", action="store_true")
    ap.add_argument("--reel-bilder", default="", help="nur Standbilder des Reels zu diesen Zeiten (Sekunden, Komma-getrennt)")
    a = ap.parse_args()
    spec = lade(a.datum)
    zeichen_pruefen(spec)
    datum = spec["datum"]
    nur = set(x for x in a.nur.split(",") if x)
    arbeit = tempfile.mkdtemp(prefix=f"op-{datum}-")
    texte, covers, ergebnisse = {}, {}, {}

    for b in spec["beitraege"]:
        if nur and b["slot"] not in nur: continue
        texte[f"{datum}-{b['slot']}-caption"] = [b.get("caption", "")]   # vor jedem continue: auch Reel-Captions im Prüflauf
        bes = Besetzung(b.get("figuren"))
        out = os.path.join(arbeit, b["slot"])
        if b["format"] == "reel":
            if a.ohne_reel: continue
            from reel import Reel
            if a.pruefen_nur:
                os.environ["OP_TTS_TROCKEN"] = "1"
            r = Reel(b, bes, out, datum)
            if a.reel_bilder:
                r.rendern(nur_bilder=[float(x) for x in a.reel_bilder.split(",")])
                print("Reel-Standbilder:", out)
                texte[f"{datum}-{b['slot']}-reel"] = r.texte + [x["text"] for x in b["sprecher"]]
                continue
            if a.pruefen_nur:
                # Trockenlauf: geschätzte Wortzeiten, Standbilder je Szene statt Video (prüft Aufbau, Wortmarken, Länge)
                r.rendern(nur_bilder=[0.5, 6.0, 12.0, 20.0, 28.0, 36.0, 42.0])
                print(f"Reel {b['slot']}: geschätzt {r.Z['dauer']:.1f} s · Standbilder unter {out}")
                covers[b["slot"]] = os.path.join(out, f"{datum}-{b['slot']}-cover.jpg")
                texte[f"{datum}-{b['slot']}-reel"] = r.texte + [x["text"] for x in b["sprecher"]]
                continue
            dateien = r.rendern()
            texte[f"{datum}-{b['slot']}-reel"] = r.texte + [x["text"] for x in b["sprecher"]]
            covers[b["slot"]] = dateien[1]
            ergebnisse[b["slot"]] = dict(dateien=dateien, dauer=r.Z["dauer"], tempo=r.Z["tempo"])
        else:
            kk = Karussell(b, bes, out, datum)
            dateien = kk.rendern()
            texte.update(kk.texte)
            covers[b["slot"]] = dateien[0]
            ergebnisse[b["slot"]] = dict(dateien=dateien, texte=kk.texte)

    if not nur or "stories" in nur:
        # Teaser brauchen das echte Cover: bei Teilläufen aus dem Ziel nehmen
        for b in spec["beitraege"]:
            if b["slot"] not in covers:
                fertig = os.path.join(a.ziel, "vorproduktion", datum, "fertig", b["slot"])
                c = sorted(glob.glob(os.path.join(fertig, "*-cover.jpg" if b["format"] == "reel" else "*-01.jpg")))
                if c: covers[b["slot"]] = c[0]
        bmap = {b["slot"]: b for b in spec["beitraege"]}
        for s_ in spec["stories"]:
            if s_["art"] == "teaser" and s_.get("beitragSlot") in bmap:
                b_ = bmap[s_["beitragSlot"]]
                s_.setdefault("klausur", b_["klausur"]); s_.setdefault("fachLabel", b_.get("fachLabel", k.MARKE["fachLabel"]))
                s_.setdefault("fach", b_.get("fach"))
        bes = Besetzung({r: f for s in spec["stories"] for r, f in (s.get("figuren") or {}).items()})
        st = Stories(spec["stories"], bes, os.path.join(arbeit, "stories"), datum, covers)
        st.rendern()
        texte.update(st.texte)
        ergebnisse["stories"] = dict(dateien=st.dateien)

    tj = os.path.join(arbeit, "texte.json")
    json.dump(texte, open(tj, "w"), ensure_ascii=False, indent=1)
    quellenpruefung(tj)
    if a.pruefen_nur:
        print("Nur geprüft:", arbeit); return

    # ---------------------------------------------------------- in den Asset-Checkout schreiben
    vp = os.path.join(a.ziel, "vorproduktion")
    fertig = os.path.join(vp, datum, "fertig")
    for slot, r in ergebnisse.items():
        z = os.path.join(fertig, slot)
        if os.path.isdir(z): shutil.rmtree(z)
        os.makedirs(z)
        for d in r["dateien"]:
            shutil.copy(d, z)
    pfad = os.path.join(vp, datum + ".json")
    alt = json.load(open(pfad, encoding="utf-8")) if os.path.exists(pfad) else {}
    tag = alt if alt else {}
    jetzt = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    tag.update(datum=datum, status="vorproduziert", freigabeBetreiber=True, liveVerknuepft=False, vorproduktionStatus="live-freigegeben",
               layoutQuelle="open-peeps-variante-c", semantikQuelle=k.MARKE["kanal"], liveVorrangAktiv=True, normalbetriebGesperrt=True,
               bildStatus="open-peeps-render")
    tag["kostenPolicy"] = {"textUndFaktencheckUsd": 0, "bildgenerierungUsd": 0, "providerKostenUsd": 0, "coverbilder": False,
                           "bildgenerierungErlaubt": False, "reelStimme": "elevenlabs-abo"}
    # Uhrzeiten aus dem Dashboard (stehen nur in der Tagesdatei des Asset-Zweigs) haben Vorrang vor der Beschreibung;
    # OP_ZEIT_AUS_SPEC=1 setzt bewusst die Zeiten der Beschreibung durch.
    alt_zeit = {} if os.environ.get("OP_ZEIT_AUS_SPEC") else \
        {e.get("slot"): e.get("zeit") for e in (alt.get("plan") or {}).get("beitraege", []) + (alt.get("plan") or {}).get("stories", []) if e.get("zeit")}
    def zeit(e): return alt_zeit.get(e["slot"]) or e.get("zeit")
    tag["plan"] = {"beitraege": [{**{x: b.get(x) for x in ("slot", "zeit", "format", "themaId", "themaTitel", "fach", "klausur")}, "zeit": zeit(b)} for b in spec["beitraege"]],
                   "stories": [{**{x: s.get(x) for x in ("slot", "zeit", "art", "themaId", "beitragSlot") if s.get(x) is not None}, "zeit": zeit(s)} for s in spec["stories"]]}
    geaendert = [f"{e['slot']} {e['zeit']}" for e in tag["plan"]["beitraege"] + tag["plan"]["stories"]
                 if e["zeit"] != next(x.get("zeit") for x in spec["beitraege"] + spec["stories"] if x["slot"] == e["slot"])]
    if geaendert: print(f"  Uhrzeiten aus dem Dashboard übernommen: {', '.join(geaendert)}")
    inh = tag.get("inhalte") or {}
    for b in spec["beitraege"]:
        slot = b["slot"]
        if nur and slot not in nur: inh.setdefault(slot, {}); continue
        basis = {x: b.get(x) for x in ("format", "fach", "klausur", "fachLabel", "themaId", "caption", "hashtags", "quellen")}
        basis.update(slug=f"{datum}-{slot}", kurztitel=b.get("themaTitel"), regelGeprueft=True, manuellGeprueft=False, freigabeBetreiber=True,
                     vorproduktionStatus="live-freigegeben", textProviderKostenUsd=0, faktencheckProviderKostenUsd=0,
                     bildStatus="open-peeps-render", renderer="open-peeps-v4", liveVorrangAktiv=True)
        if b["format"] == "reel":
            basis.update(bild="op-cover", reelTyp=b.get("reelTyp"), hookStil=b["hook"].get("stil"), coverBadge="Reel",
                         szenen=[{"art": "hook", "titel": " ".join(b["hook"]["zeilen"])}] + [{"art": "schritt", "titel": s["titel"]} for s in b["szenen"]],
                         sprecher=[x["text"] for x in b["sprecher"]])
            if slot in ergebnisse: basis.update(dauerS=ergebnisse[slot]["dauer"], tempo=ergebnisse[slot]["tempo"])
        else:
            basis.update(coverBadge=b["folien"][0].get("badge"), folien=folien_eintraege(texte, datum, slot, len(b["folien"])))
        inh[slot] = basis
    if not nur or "stories" in nur:
        for s in spec["stories"]:
            e = {x: s.get(x) for x in ("slot", "art", "fach", "klausur", "fachLabel", "themaId", "beitragSlot", "quellen")}
            # Inhaltsfelder mitgeben: Der Bot prüft vor dem Posten z. B. das Quizpaar (optionen, richtig, pairId).
            e.update({x: v for x, v in s.items() if x not in e and x not in ("figuren", "figur", "zeit")})
            if s["art"] in ("frage", "antwort") and s.get("themaId"): e.setdefault("pairId", s["themaId"])
            e.update(sichtbareTexte=texte.get(f"{datum}-{s['slot']}-{s['art']}.jpg", []), renderer="open-peeps-v4", bildStatus="open-peeps-render",
                     freigabeBetreiber=True, vorproduktionStatus="live-freigegeben", liveVorrangAktiv=True, regelGeprueft=True)
            inh[s["slot"]] = e
    tag["inhalte"] = inh
    tag["renderVorschau"] = {"status": "fertig", "erzeugtAm": jetzt, "pfad": f"vorproduktion/{datum}/fertig", "providerKostenUsd": 0,
                             "coverbilder": False, "coverIcons": False, "renderer": "open-peeps-v4", "layoutQuelle": "open-peeps-variante-c",
                             "reelStimme": "elevenlabs-laura", "sfx": "freesound-cc0", "freigabeBetreiber": True, "liveVorrangAktiv": True,
                             "normalbetriebGesperrt": True, "wartetLive": []}
    json.dump(tag, open(pfad, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(pfad, "a").write("\n")
    ip = os.path.join(vp, "index.json")
    if os.path.exists(ip):
        idx = json.load(open(ip, encoding="utf-8"))
        e = next((x for x in idx.get("tage", []) if x.get("datum") == datum), None)
        if e is None:
            e = {"datum": datum}; idx.setdefault("tage", []).append(e); idx["tage"].sort(key=lambda x: x["datum"])
        e.update(status="vorproduziert", freigabeBetreiber=True, liveVerknuepft=False, vorproduktionStatus="live-freigegeben",
                 feed=len(spec["beitraege"]), storiesEigenstaendig=sum(1 for s in spec["stories"] if s["art"] != "teaser"),
                 teaserAbgeleitet=sum(1 for s in spec["stories"] if s["art"] == "teaser"), wartetLive=0,
                 reviewPfad=f"vorproduktion/{datum}/fertig", coverbilder=False, providerKostenUsd=0, liveVorrangAktiv=True,
                 normalbetriebGesperrt=True, bilderStatus="open-peeps-render", renderStatus="fertig", renderErzeugtAm=jetzt,
                 coverIcons=False, renderer="open-peeps-v4")
        idx["stand"] = jetzt
        json.dump(idx, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(ip, "a").write("\n")
    print(f"✓ {datum}: " + ", ".join(f"{s} ({len(r['dateien'])})" for s, r in ergebnisse.items()))


if __name__ == "__main__":
    main()
