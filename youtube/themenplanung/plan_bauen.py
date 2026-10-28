"""Baut den LexVerse-Themenplan (5 Jahre × 52 Wochen × 3 Slots = 780 Folgen) aus den Kandidatenlisten."""
import json, math, collections, csv, re

A = []
for q in ["zivil", "oeff", "straf", "examen2", "methodik"]:      # Kandidatenlisten aus der Auswertung des Repetitoriums
    for x in json.load(open(f"kandidaten_{q}.json")):
        x["_q"] = q; A.append(x)
STREICHEN = {  # Dubletten über Rechtsgebiete hinweg (die breitere bzw. examenstypischere Fassung bleibt)
    "Reformatio in peius: Darf der Widerspruch alles schlimmer machen?",
    "§ 252 StPO: Wenn die Ehefrau in der Hauptverhandlung schweigt",
    "Wer will was von wem woraus? Die Zivilrechtsklausur in 6 Minuten",
    "Maßgeblicher Zeitpunkt: Wann die Sach- und Rechtslage zählt",
    "Auflage oder Inhaltsbestimmung? Nebenbestimmungen im Bescheid",
    "Wer ist der richtige Beklagte? Rechtsträger- vs. Behördenprinzip",
    "Faktischer Vollzug: Die Behörde vollstreckt trotz Widerspruch",
    "Bescheid im Briefkasten: Die Vier-Tages-Fiktion seit 2025",
    "Gutachtenstil statt Urteilsstil: So holst du Punkte in der Klausur",
    "Gutachtenstil vs. Urteilsstil: Wann welcher Stil?",
    "Einstweilige Anordnung § 123 VwGO: Anspruch, Grund, Vorwegnahme",
    # beim Abgleich der Suchbegriffe gefunden (gleiches Thema im 1. Examen vorhanden)
    "Einstellung gegen Geldauflage: So funktioniert § 153a StPO",
    "Strafbefehl im Briefkasten: Verfahren, Einspruch, Risiko",
    "Gestrecktes Verfahren: Androhung, Festsetzung, Anwendung",
    "Bau-Turbo § 246e BauGB: Das neue Baurecht in der Akte",
}
A = [x for x in A if x["titel"] not in STREICHEN]
assert len(STREICHEN) == 15

GEBIET = {"zivil": "Zivilrecht", "oeff": "Öffentliches Recht", "straf": "Strafrecht", "examen2": "2. Examen", "methodik": "Methodik"}
QUOTE = {"zivil": 235, "straf": 215, "oeff": 190, "examen2": 105, "methodik": 35}
assert sum(QUOTE.values()) == 780


def score(x):
    s = 2 * x["relevanz"] + 1.5 * x["breite"] + (2 if x["klassiker"] else 0)
    s += {"Klassiker-Fall": 1.5, "Alltagsfall": 1.0}.get(x["format"], 0)
    s += 0.5 if x["_q"] == "straf" else 0          # höchstes Suchinteresse (Jurafuchs-Studie, siehe Recherche)
    if x["format"] == "Schema" and x["relevanz"] == 5:
        s += 3.0                                  # Kernschemata: dauerhafte Suchnachfrage und Grundlage der Fallvideos
    elif x["format"] == "Schema" and x["relevanz"] == 4:
        s += 1.5                                  # Lernsuche ("… Schema") hängt nicht am Alltagsbezug
    return round(s, 2)


for x in A:
    x["score"] = score(x)
titel_idx = {x["titel"]: x for x in A}
from aufloesen import aufloesen
for x in A:   # Stichwort-Voraussetzungen -> Titel desselben Gebiets (Liste); Originaltext bleibt in 'voraussetzung'
    x["_alle_vor"] = aufloesen(x["voraussetzung"], x, A, titel_idx) if x["voraussetzung"] else []
    # verbindlich nur für Schema/Streitstand/Abgrenzung usw.; Fallvideos erklären ihren Hintergrund selbst (weiche Empfehlung)
    x["_vor"] = [] if x["format"] in ("Klassiker-Fall", "Alltagsfall") else x["_alle_vor"]

# --- Auswahl je Rechtsgebiet: Mindestabdeckung je Teilgebiet, Rest nach Punktzahl --------------------------------
auswahl = []
for q, n in QUOTE.items():
    pool = sorted([x for x in A if x["_q"] == q], key=lambda x: -x["score"])
    if len(pool) <= n:
        auswahl += pool; continue
    tg = collections.defaultdict(list)
    for x in pool:
        tg[x["teilgebiet"]].append(x)
    gew = set()
    for t, l in tg.items():
        boden = min(len(l), max(2, round(0.6 * len(l) * n / len(pool))))
        gew |= {id(x) for x in l[:boden]}
    for x in pool:
        if len(gew) >= n: break
        gew.add(id(x))
    sel = [x for x in pool if id(x) in gew]
    # Voraussetzungen nachziehen (schwächstes Nicht-Grundlagenthema weicht)
    while True:
        fehl = [titel_idx[v] for x in sel for v in x["_vor"] if titel_idx[v] not in sel]
        if not fehl: break
        benoetigt = {v for x in sel for v in x["_vor"]}
        raus = min((x for x in sel if x["titel"] not in benoetigt), key=lambda x: x["score"])
        sel.remove(raus); sel.append(fehl[0])
    auswahl += sel
assert len(auswahl) == 780, len(auswahl)

# --- Reihenfolge: Punktzahl, aber Grundlagen vor darauf aufbauenden Themen -------------------------------------------
eff = {x["titel"]: x["score"] for x in auswahl}
for _ in range(10):
    for x in auswahl:
        for v in x["_vor"]:
            if v in eff and eff[v] <= eff[x["titel"]]:
                eff[v] = eff[x["titel"]] + 0.01
for x in auswahl:
    x["eff"] = eff[x["titel"]]

# Grundstock: Einsteigerpfad je Gebiet, verbindlich in Jahr 1 und in didaktischer Reihenfolge
GRUNDSTOCK = [
    # Methodik
    "Gutachtenstil in 6 Minuten: Obersatz, Definition, Subsumtion",
    "Wer will was von wem woraus? Der Aufbau jeder Zivilrechtsklausur",
    "Strafrechtsklausur aufbauen: Tatkomplexe, Beteiligte, Reihenfolge",
    "Lösungsskizze und Zeitplan für die 5-Stunden-Klausur",
    "Öffentliches Recht: Zulässigkeit und Begründetheit sauber trennen",
    "Die 10 häufigsten Fehler in Jura-Klausuren",
    "Prüfungsschemata lernen – aber richtig",
    # Strafrecht
    "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "Strafrecht AT im Überblick: Welches Prüfungsschema wann?",
    "Kausalität einfach erklärt: die conditio-sine-qua-non-Formel",
    "Absicht, Wissen, Eventualvorsatz: Die drei Vorsatzformen",
    "Notwehr § 32: Das Prüfungsschema",
    "Tötungs- und Körperverletzungsdelikte im Überblick: §§ 211–229 StGB",
    "Körperverletzung § 223: Ohrfeige, Haare ab, Spucke",
    "Gefährliche Körperverletzung § 224 StGB: Das Prüfungsschema",
    "Vermögensdelikte im Überblick: Diebstahl, Betrug, Raub, Erpressung",
    "Diebstahl § 242: Das Prüfungsschema",
    "Einwilligung: Wann ist eine Körperverletzung erlaubt?",
    "Betrug § 263: Das Prüfungsschema",
    "Tatbestandsirrtum § 16: Der Jäger und der Pilzsammler",
    "Unechtes Unterlassen § 13: Strafbar durch Nichtstun",
    "Mord oder Totschlag? Die Mordmerkmale im Überblick",
    "Raub § 249: Gewalt, Wegnahme, Finalität",
    "Versuch: Das Prüfungsschema mit Vorprüfung",
    "Rücktritt vom Versuch: Das Schema des § 24",
    "Mittäterschaft § 25 II: Gemeinsam geplant, gemeinsam verantwortlich",
    # Öffentliches Recht
    "Grundrechte im Überblick: Freiheitsrechte, Gleichheitsrechte, Prüfung",
    "Grundrechtsprüfung: Schutzbereich, Eingriff, Rechtfertigung",
    "Verhältnismäßigkeit: Der wichtigste Prüfungspunkt im Öffentlichen Recht",
    "Verfahren vor dem BVerfG im Überblick: Welches Verfahren wann?",
    "Verfassungsbeschwerde: Das Prüfungsschema in sechs Minuten",
    "Was ist ein Verwaltungsakt? § 35 VwVfG in sechs Minuten",
    "Welche Klage passt? Die Klagearten der VwGO im Überblick",
    "Anfechtungsklage: Das komplette Prüfungsschema",
    "Ermessen und Ermessensfehler: Was darf das Gericht kontrollieren?",
    "Polizeirecht-Schema: Standardmaßnahme vor Generalklausel",
    "Verpflichtungsklage: Spruchreife und Bescheidungsurteil",
    "Gesetzgebungskompetenz: Bund oder Land? Art. 70 ff. GG",
    "Wie ein Bundesgesetz entsteht: Formelle Verfassungsmäßigkeit prüfen",
    "Eilrechtsschutz nach § 80 V VwGO: Das Grundschema",
    # Zivilrecht
    "BGB AT im Überblick: Vom Vertragsschluss bis zur Anfechtung",
    "Trennungs- und Abstraktionsprinzip: Warum ein Kauf drei Verträge braucht",
    "Angebot und Annahme: Wann ist ein Vertrag wirklich geschlossen?",
    "Zugang unter Abwesenden: Wann ist der Brief „angekommen“?",
    "Minderjährige im Vertragsrecht: Das Grundschema §§ 104 ff. BGB",
    "Anfechtung in fünf Schritten: Das Prüfungsschema §§ 119 ff. BGB",
    "Stellvertretung in drei Schritten: Wann bindet der Vertreter den Chef?",
    "Das System der §§ 280 ff. BGB: Welcher Schadensersatz wann?",
    "Die Käuferrechte des § 437 BGB auf einen Blick",
    "§ 823 I BGB: Das Prüfungsschema der unerlaubten Handlung",
    "Bereicherungsrecht im Überblick: Welche Kondiktion wann?",
    "Sachenrecht im Überblick: Eigentum an Sachen und Grundstücken",
    "Eigentum übertragen: Einigung und Übergabe nach § 929 S. 1 BGB",
    "Gutgläubiger Erwerb: Eigentum vom Nichteigentümer?",
    # 2. Examen
    "Der Zivilprozess im Überblick: Von der Klage bis zur Vollstreckung",
]
PFLICHT = [  # Grundlagen/Alltagsthemen, die unabhängig von der Punktzahl in den Plan gehören (Jahr nach Punktzahl)
    "Kausalität einfach erklärt: die conditio-sine-qua-non-Formel",
    "Fehlgeschlagener Versuch: Wenn kein Rücktritt mehr möglich ist",
    "Tun oder Unterlassen? Der weggezogene Rettungsring",
    "Selbstbedienung im Supermarkt: Wann kaufst du die Milch?",
    "Unbestellte Ware im Briefkasten: Darfst du sie behalten?",
    "Nach der Anfechtung: Wer zahlt den Vertrauensschaden? (§ 122 BGB)",
    "Sperrwirkung des EBV: Warum der redliche Besitzer nicht aus § 823 haftet",
]
LERNSUCHE = [  # Verfahrensarten und Kernbegriffe, die Studierende gezielt suchen: im Plan und früh (Jahr 1–2)
    "Schwere Körperverletzung und Todesfolge: §§ 226, 227 StGB",
    "Freiheitsberaubung im Schlaf: Muss das Opfer es merken?",
    "Was darf die Prokuristin? Prokura und Handlungsvollmacht",
    "Schutzgesetzverletzung: Wann hilft § 823 II BGB?",
    "Abstrakte Normenkontrolle: Opposition gegen Regierungsgesetz",
    "Konkrete Normenkontrolle: Wenn ein Richter ein Gesetz stoppt",
    "Bund-Länder-Streit: Wenn Bund und Land vor Gericht ziehen",
    "Verfahren vor dem EuGH im Überblick: Vorlage, Nichtigkeits- und Vertragsverletzungsklage",
    "Vorabentscheidung: Wann ein Gericht den EuGH fragen muss",
    "Nichtigkeitsklage: Können Bürger EU-Gesetze anfechten?",
    "Vertragsverletzungsverfahren: Wenn Brüssel Deutschland verklagt",
]
PFLICHT += LERNSUCHE
fehlt = [t for t in GRUNDSTOCK + PFLICHT if t not in titel_idx]
assert not fehlt, fehlt
for t in GRUNDSTOCK + PFLICHT:
    x = titel_idx[t]
    if x not in auswahl:                      # falls bei der Auswahl gefallen: schwächstes Thema desselben Gebiets weicht
        raus = min((y for y in auswahl if y["_q"] == x["_q"] and y["titel"] not in GRUNDSTOCK + PFLICHT), key=lambda y: y["score"])
        auswahl.remove(raus); auswahl.append(x); x["eff"] = x["score"]
GR = {t: i for i, t in enumerate(GRUNDSTOCK)}
# Didaktische Abhängigkeiten, die in den Kandidatenlisten fehlten (Folgethema -> Grundlage)
VORHER = {
    "Was ist ein Verwaltungsakt? § 35 VwVfG in sechs Minuten": None,
    "Welche Klage passt? Die Klagearten der VwGO im Überblick": "Was ist ein Verwaltungsakt? § 35 VwVfG in sechs Minuten",
    "Anfechtungsklage: Das komplette Prüfungsschema": "Welche Klage passt? Die Klagearten der VwGO im Überblick",
    "Verpflichtungsklage: Spruchreife und Bescheidungsurteil": "Anfechtungsklage: Das komplette Prüfungsschema",
    "Eilrechtsschutz nach § 80 V VwGO: Das Grundschema": "Anfechtungsklage: Das komplette Prüfungsschema",
    "Nachbar gegen Baugenehmigung: Eilrechtsschutz nach §§ 80a, 80 V": "Eilrechtsschutz nach § 80 V VwGO: Das Grundschema",
    "Verhältnismäßigkeit: Der wichtigste Prüfungspunkt im Öffentlichen Recht": "Grundrechtsprüfung: Schutzbereich, Eingriff, Rechtfertigung",
    "Verfassungsbeschwerde: Das Prüfungsschema in sechs Minuten": "Grundrechtsprüfung: Schutzbereich, Eingriff, Rechtfertigung",
    "Notwehr § 32: Das Prüfungsschema": "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "Diebstahl § 242: Das Prüfungsschema": "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "Absicht, Wissen, Eventualvorsatz: Die drei Vorsatzformen": "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "Rücktritt vom Versuch: Das Schema des § 24": "Versuch: Das Prüfungsschema mit Vorprüfung",
    "Explodierende Flasche: Die Produzentenhaftung nach § 823 I BGB": "§ 823 I BGB: Das Prüfungsschema der unerlaubten Handlung",
    "Anfechtung in fünf Schritten: Das Prüfungsschema §§ 119 ff. BGB": "Angebot und Annahme: Wann ist ein Vertrag wirklich geschlossen?",
    "Gutgläubiger Erwerb: Eigentum vom Nichteigentümer?": "Eigentum übertragen: Einigung und Übergabe nach § 929 S. 1 BGB",
    "Vorabentscheidung: Wann ein Gericht den EuGH fragen muss": "Verfahren vor dem EuGH im Überblick: Vorlage, Nichtigkeits- und Vertragsverletzungsklage",
    "Nichtigkeitsklage: Können Bürger EU-Gesetze anfechten?": "Verfahren vor dem EuGH im Überblick: Vorlage, Nichtigkeits- und Vertragsverletzungsklage",
    "Vertragsverletzungsverfahren: Wenn Brüssel Deutschland verklagt": "Verfahren vor dem EuGH im Überblick: Vorlage, Nichtigkeits- und Vertragsverletzungsklage",
    "Abstrakte Normenkontrolle: Opposition gegen Regierungsgesetz": "Verfahren vor dem BVerfG im Überblick: Welches Verfahren wann?",
    "Konkrete Normenkontrolle: Wenn ein Richter ein Gesetz stoppt": "Verfahren vor dem BVerfG im Überblick: Welches Verfahren wann?",
    "Bund-Länder-Streit: Wenn Bund und Land vor Gericht ziehen": "Verfahren vor dem BVerfG im Überblick: Welches Verfahren wann?",
    "Gefährliche Körperverletzung § 224 StGB: Das Prüfungsschema": "Körperverletzung § 223: Ohrfeige, Haare ab, Spucke",
    "Schwere Körperverletzung und Todesfolge: §§ 226, 227 StGB": "Gefährliche Körperverletzung § 224 StGB: Das Prüfungsschema",
}
for t, v in VORHER.items():
    assert t in titel_idx and (v is None or v in titel_idx), (t, v)
    if v:
        titel_idx[t]["voraussetzung"] = v; titel_idx[t]["_vor"] = [v]; titel_idx[t]["_alle_vor"] = [v]
for x in auswahl:
    x["eff"] = 1000 - GR[x["titel"]] if x["titel"] in GR else x["score"] + (6 if x["titel"] in LERNSUCHE else 0)
eff = {x["titel"]: x["eff"] for x in auswahl}
for _ in range(20):                           # Grundlagen stets vor ihren Folgethemen
    for x in auswahl:
        for v in x["_vor"]:
            if v in eff and eff[v] <= eff[x["titel"]]:
                eff[v] = eff[x["titel"]] + 0.01
for x in auswahl:
    x["eff"] = eff[x["titel"]]

# Jahre: je Gebiet gleich große Pakete, stärkste Themen zuerst
jahr_pools = {j: collections.defaultdict(list) for j in range(1, 6)}
for q, n in QUOTE.items():
    l = sorted([x for x in auswahl if x["_q"] == q], key=lambda x: -x["eff"])
    grenzen = [round(n * k / 5) for k in range(6)]
    for j in range(5):
        for x in l[grenzen[j]:grenzen[j + 1]]:
            x["jahr"] = j + 1
            jahr_pools[j + 1][q].append(x)

# Lernsuche-Themen spätestens in Jahr 2: gegen das schwächste Jahr-2-Thema desselben Gebiets tauschen,
# das keine Grundlage eines anderen Themas ist
alle_vor = {v for x in auswahl for v in x["_vor"]}


def vorziehen(t, ziel=2):
    """Thema t (samt seinen Voraussetzungen) spätestens in Jahr ziel; Tausch mit dem schwächsten freien Thema."""
    x = titel_idx[t]
    for v in x["_vor"]:
        if v in eff:
            vorziehen(v, ziel)
    if x["jahr"] <= ziel:
        return
    q = x["_q"]
    kand = [y for y in jahr_pools[ziel][q] if y["titel"] not in PFLICHT and y["titel"] not in GR and y["titel"] not in alle_vor]
    y = min(kand, key=lambda y: y["eff"])
    jahr_pools[x["jahr"]][q].remove(x); jahr_pools[ziel][q].remove(y)
    jahr_pools[ziel][q].append(x); jahr_pools[x["jahr"]][q].append(y)
    y["jahr"], x["jahr"] = x["jahr"], ziel
    x["eff"], y["eff"] = max(x["eff"], y["eff"]), min(x["eff"], y["eff"])


for t in PFLICHT:                              # Pflicht- und Lernsuche-Themen spätestens in Jahr 2
    vorziehen(t)

FALL = {"Klassiker-Fall", "Alltagsfall"}
PRAXIS = {"Klausurfehler", "Abgrenzung", "Streitstand"}
METH_WOCHEN = [1, 2, 3, 15, 27, 39, 41]          # Semesterstart Okt/Apr, Klausurphasen Jan/Jul (Woche 1 = erste Oktoberwoche)
KLAUSURPHASE = set(range(14, 21)) | set(range(38, 44))
plan = []


def nimm(queue, geplant, bevorzugt):
    """Nächstes Thema: Voraussetzung muss schon geplant sein; unter den ersten 8 möglichen das mit passendem Format."""
    frei = [x for x in queue if all(v not in eff or v in geplant for v in x["_vor"])][:25 if bevorzugt is FALL else 8]
    if not frei:
        frei = queue[:1]
    for x in frei:
        if x["format"] in bevorzugt:
            queue.remove(x); return x
    queue.remove(frei[0]); return frei[0]


geplant = set()
for j in range(1, 6):
    Q = {q: sorted(l, key=lambda x: -x["eff"]) for q, l in jahr_pools[j].items()}
    soll = {q: len(l) for q, l in Q.items()}
    n_ex2, n_meth = len(Q["examen2"]), len(Q["methodik"])
    # Freitag: Methodik an festen Wochen, 2. Examen gleichmäßig verteilt, sonst 1. Examen
    meth_w = METH_WOCHEN[:n_meth] + [w for w in range(1, 53) if w not in METH_WOCHEN][:max(0, n_meth - len(METH_WOCHEN))]
    rest_w = [w for w in range(1, 53) if w not in meth_w]
    ex2_w = set(rest_w[round(i * len(rest_w) / n_ex2)] for i in range(n_ex2)) if n_ex2 else set()
    erste = ["straf", "zivil", "oeff"]
    for w in range(1, 53):
        woche = []
        for slot, tag in ((1, "Mo"), (2, "Mi"), (3, "Fr")):
            if slot == 3 and w in meth_w:
                q = "methodik"
            elif slot == 3 and w in ex2_w:
                q = "examen2"
            else:
                # Gebiet mit dem größten Rückstand, nicht zweimal dasselbe Gebiet in einer Woche
                kand = [q for q in erste if Q[q] and q not in [p["_q"] for p in woche]] or [q for q in erste if Q[q]]
                q = max(kand, key=lambda q: len(Q[q]) / soll[q])
            bev = FALL if slot == 1 else (PRAXIS if (slot == 3 or w in KLAUSURPHASE) else {"Schema", "Streitstand", "Abgrenzung"})
            if q == "methodik":
                bev = {"Methodik"}
            x = nimm(Q[q], geplant, bev)
            geplant.add(x["titel"])
            x.update(woche_im_jahr=w, slot=slot, tag=tag)
            woche.append(x)
        plan += woche
    assert all(not l for l in Q.values()), {q: len(l) for q, l in Q.items()}

REIHE = {1: "Der Fall", 2: "Examenswissen", 3: "Klausurpraxis"}
for i, x in enumerate(plan, 1):
    x["nr"] = i
    x["woche"] = (x["jahr"] - 1) * 52 + x["woche_im_jahr"]
    x["reihe"] = REIHE[x["slot"]] if x["_q"] not in ("methodik", "examen2") else ("Methodik" if x["_q"] == "methodik" else "2. Examen")
    x["gebiet"] = GEBIET[x["_q"]]

# Kontrolle: Voraussetzung immer vorher
pos = {x["titel"]: x["nr"] for x in plan}
verletzt = [(x["titel"], v) for x in plan for v in x["_vor"] if v in pos and pos[v] > x["nr"]]
print("aufgelöste Abhängigkeiten im Plan:", sum(v in pos for x in plan for v in x["_vor"]))
weich = sum(1 for x in plan for v in x["_alle_vor"] if v in pos and pos[v] > x["nr"])
hart = sum(v in pos for x in plan for v in x["_vor"])
print("weiche Empfehlungen (Fallvideo vor Grundlage):", weich)
json.dump({"hart": hart, "hart_verletzt": len(verletzt), "weich_vorher": weich, "grundstock": len(GRUNDSTOCK),
           "pflicht": len(PFLICHT) - len(LERNSUCHE), "lernsuche": len(LERNSUCHE)}, open("stats.json", "w"))
for x in plan:
    x["grundstock"] = x["titel"] in GR
for x in plan + [y for y in A if y["titel"] not in pos]:
    if x["_alle_vor"]:
        x["voraussetzung"] = " + ".join(x["_alle_vor"])
    elif x["voraussetzung"].strip().lower() in ("keine", "-", "–"):
        x["voraussetzung"] = ""
print("Voraussetzung nach Folgethema:", len(verletzt))
for v in verletzt[:10]: print("  ", v)
json.dump([{k: v for k, v in x.items() if not k.startswith("_") and k != "eff"} for x in plan], open("plan.json", "w"), ensure_ascii=False, indent=1)
gewaehlt = {x["titel"] for x in plan}
reserve = sorted([x for x in A if x["titel"] not in gewaehlt], key=lambda x: (-x["score"], x["titel"]))
for x in reserve:
    x["gebiet"] = GEBIET[x["_q"]]
json.dump([{k: v for k, v in x.items() if not k.startswith("_") and k != "eff"} for x in reserve], open("reserve.json", "w"), ensure_ascii=False, indent=1)
print("Reserve:", len(reserve))

# CSV, Excel und Markdown schreibt ausgabe.py
c = collections.Counter((x["jahr"], x["gebiet"]) for x in plan)
for j in range(1, 6): print(j, {g: c[(j, g)] for g in GEBIET.values()})
print(collections.Counter(x["gebiet"] for x in plan))
