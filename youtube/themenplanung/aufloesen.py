"""Löst Stichwort-Voraussetzungen der Kandidatenlisten ('Organstreit', 'Notwehrschema', '§ 242; § 263') in Titel
desselben Gebiets auf. Nur die Reihenfolge hängt davon ab; unsichere Stichworte bleiben unaufgelöst."""
import re, difflib

STOP = set("der die das und oder ein eine im in zu mit von vom zum zur den dem des bei auf für als nach über schema "
           "prüfungsschema grundvideos grundschema".split())
KEINE = {"keine", "keine voraussetzung", "-", "–", "—", "ohne", "n/a", ""}
ALIAS = {  # Sammelbegriffe -> Grundlagentitel (nur wenn es ihn gibt)
    "deliktsaufbau": "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "aufbau der straftat": "Straftat prüfen in 3 Schritten: Tatbestand, Rechtswidrigkeit, Schuld",
    "betrugsschema": "Betrug § 263: Das Prüfungsschema",
    "diebstahlsschema": "Diebstahl § 242: Das Prüfungsschema",
    "notwehrschema": "Notwehr § 32: Das Prüfungsschema",
    "notstandsschema": "Rechtfertigender Notstand § 34: Einbruch in die Berghütte",
    "versuchsschema": "Versuch: Das Prüfungsschema mit Vorprüfung",
    "rücktrittsschema": "Rücktritt vom Versuch: Das Schema des § 24",
    "unterlassungsschema": "Unechtes Unterlassen § 13: Strafbar durch Nichtstun",
    "urkundenbegriff": "Was ist eine Urkunde? Die gefälschte Entschuldigung",
    "verbrechen/vergehen": "Verbrechen oder Vergehen? Die Unterscheidung mit großen Folgen",
    "tötungsdelikte": "Mord oder Totschlag? Die Mordmerkmale im Überblick",
    "vorsatz": "Absicht, Wissen, Eventualvorsatz: Die drei Vorsatzformen",
    "vorsatzformen": "Absicht, Wissen, Eventualvorsatz: Die drei Vorsatzformen",
    "täterschaft/teilnahme": "Mittäterschaft § 25 II: Gemeinsam geplant, gemeinsam verantwortlich",
    "tkü": "Staatstrojaner: Online-Durchsuchung und Quellen-TKÜ",
    "gesetzgebungsverfahren": "Wie ein Bundesgesetz entsteht: Formelle Verfassungsmäßigkeit prüfen",
    "formelle verfassungsmäßigkeit": "Wie ein Bundesgesetz entsteht: Formelle Verfassungsmäßigkeit prüfen",
    "rücknahme und widerruf": "Fördergeld zurück? Die Rücknahme nach § 48 VwVfG",
    "anfechtungs- und verpflichtungsklage": "Anfechtungsklage: Das komplette Prüfungsschema",
    "rechtmäßigkeit des va": "Anfechtungsklage: Das komplette Prüfungsschema",
    "klagearten": "Welche Klage passt? Die Klagearten der VwGO im Überblick",
    "rechtskraft": "Streitgegenstand und Rechtskraft: Was ist eigentlich entschieden?",
    "§ 91a zpo": "§ 91a ZPO: Wer zahlt, wenn sich der Streit von selbst erledigt?",
    "grundvideos revisionsklausur": "Revision in 6 Minuten: Sachrüge vs. Verfahrensrüge",
    "sachliche zuständigkeit": "Strafrichter, Schöffengericht oder Landgericht? Die Straferwartung",
    "erfolgsqualifikation": "Erfolgsqualifizierte Delikte: Das Schema mit dem Gefahrzusammenhang",
    "fahrlässigkeitsschema": "Fahrlässigkeitsdelikt: Das Prüfungsschema",
    "verwertungsverbote": "Beweisverwertungsverbote: Das System in 6 Minuten",
    "zeugnisverweigerungsrecht": "Muss ich gegen meinen Partner aussagen?",
    "echte unterlassungsdelikte": "Unterlassene Hilfeleistung: Muss ich jedem helfen?",
    "verwaltungsakt-begriff": "Was ist ein Verwaltungsakt? § 35 VwVfG in sechs Minuten",
    "verhaltens- und zustandsstörer": "Verhaltensstörer: Die Theorie der unmittelbaren Verursachung",
    "neutralitätspflicht der regierung": "Darf eine Ministerin gegen eine Partei posten? Die Neutralitätspflicht",
    "bekanntgabe/vier-tages-fiktion": "Wann gilt ein Bescheid als bekannt gegeben? Die Vier-Tages-Fiktion",
    "vier-tages-fiktion / fristberechnung": "Wann gilt ein Bescheid als bekannt gegeben? Die Vier-Tages-Fiktion",
    "gefahr im verzug (art. 13)": "Durchsuchung ohne Richter? 'Gefahr im Verzug' erklärt",
    "zv-grundschema": "Titel, Klausel, Zustellung: Das Grundschema der Zwangsvollstreckung",
    "relationstechnik-grundvideo": "Relationstechnik: Mit 3 Stationen durch jede Zivilakte",
    "beweisstation": "Relationstechnik: Mit 3 Stationen durch jede Zivilakte",
    "leistungstenor": "Der perfekte Tenor: Zinsen, Zug um Zug, Annahmeverzug",
    "non liquet / beweislast": "Non liquet: Wer verliert, wenn niemand etwas beweisen kann?",
    "zeugenbeweis": "Zeugen würdigen wie ein Richter: Glaubhaftigkeit statt Floskeln",
    "anwaltsklausur-grundaufbau": "Anwaltsklausur: Gutachten, Zweckmäßigkeit, Schriftsatz",
    "hauptverhandlung": None, "grundvideos urteil": None, "verfahrensablauf": None, "staatsstrukturprinzipien": None,
}


def _worte(s):
    s = s.lower().replace("-", " ")
    return [w for w in re.findall(r"[a-zäöüß0-9]+", s) if (len(w) >= 4 or w.isdigit()) and w not in STOP]


def _kopf(t):
    return t.split(":")[0].split("?")[0]


def _paragrafen(s):
    return re.findall(r"§+\s*(\d+[a-z]?)", s)


def aufloesen(label, x, A, titel_idx):
    """Liste aufgelöster Titel (gleiches Gebiet, nicht x selbst); leer, wenn nichts sicher passt."""
    if label in titel_idx:
        return [label]
    if label.strip().lower() in KEINE:
        return []
    pool = [y for y in A if y["_q"] == x["_q"] and y["titel"] != x["titel"]]
    treffer = []
    for teil in re.split(r";| sowie ", label):
        teil = teil.strip()
        tl = teil.lower()
        if not teil or tl in KEINE:
            continue
        if tl in ALIAS:
            z = ALIAS[tl]
            if z in titel_idx and z != x["titel"] and titel_idx[z]["_q"] == x["_q"]:
                treffer.append(z)
            continue
        par = _paragrafen(teil)
        if par and not _worte(re.sub(r"§+\s*\d+[a-z]?", "", teil)):
            # reiner Normverweis: Titel mit genau diesem Paragrafen, bevorzugt Schema-Videos
            kand = [y for y in pool if all(re.search(r"§+\s*" + p + r"(?![0-9a-z])", y["titel"]) for p in par)]
            if not kand:
                kand = [y for y in pool if all(re.search(r"§+\s*" + p + r"(?![0-9a-z])", y["normen"].split(",")[0]) for p in par)]
        else:
            w = _worte(teil)
            if not w:
                continue
            def stamm(v):
                return v[:max(5, len(v) - 3)]
            def in_text(text):
                woerter = re.findall(r"[a-zäöüß0-9]+", text.lower().replace("-", " "))
                return all(any(t.startswith(stamm(v)) for t in woerter) for v in w)
            kand = [y for y in pool if in_text(y["titel"])]
        if kand:
            best = max(kand, key=lambda y: (y["format"] == "Schema",
                                            difflib.SequenceMatcher(None, tl, _kopf(y["titel"]).lower()).ratio(), y["relevanz"]))
            treffer.append(best["titel"])
    return list(dict.fromkeys(treffer))
