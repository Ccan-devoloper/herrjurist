"""Nachbearbeitung der Upload-Texte für Folge 111 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: „Römisch eins/zwei/…“ als I./II./…, Paragrafen-Umbruch, Beträge in Ziffern.
Aufruf: python3 meta_111.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Stoß und die Handtasche"),
       (T("p249"), "§ 249 Abs. 1 im Wortlaut und Aufbau"), (T("sache"), "Fremde bewegliche Sache und Wegnahme"),
       (T("nm"), "Qualifiziertes Nötigungsmittel: Gewalt gegen eine Person"), (T("final"), "Finaler Zusammenhang"),
       (T("ab1"), "Abwandlung 1: Gewalt aus Wut, Entschluss erst danach"),
       (T("p252"), "Abgrenzung: § 252 und § 255 StGB"), (T("vors"), "Vorsatz und Zueignungsabsicht"),
       (T("rs"), "Ergebnis und Qualifikationen §§ 250, 251"), (T("ab2"), "Abwandlung 2: Entreißen der Handtasche"),
       (T("tipp"), "Klausurtipp: Finalität"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Raub § 249 StGB: Wie prüft man den Raub – und warum muss die Gewalt gerade zur Wegnahme eingesetzt werden (Finalzusammenhang)? Das Prüfungsschema Schritt für Schritt an einem Klausurfall.

Der Fall: Auf dem Weg vom Wochenmarkt zur Bushaltestelle stößt Hagen Margit zu Boden, um an ihre Handtasche zu kommen, nimmt die Tasche und rennt davon. Margit bleibt bis auf einen Schreck unverletzt. Hat Hagen einen Raub begangen? Dazu zwei Abwandlungen: Gewalt nur aus Wut mit späterem Wegnahmeentschluss – und das Entreißen der Handtasche im Vorbeilaufen. (Übungsfall)

Inhalt:
– § 249 Abs. 1 StGB im Wortlaut: Raub = Wegnahme mit qualifiziertem Nötigungsmittel
– fremde bewegliche Sache und Wegnahme (Einzelheiten in unserer Folge zum Diebstahl)
– qualifiziertes Nötigungsmittel: Gewalt gegen eine Person oder Drohung mit gegenwärtiger Gefahr für Leib oder Leben – der Unterschied zu § 240 StGB
– finaler Zusammenhang: Gewalt als Mittel zur Wegnahme, maßgeblich ist die Vorstellung des Täters
– Abwandlung 1: Entschluss zur Wegnahme erst nach der Gewalt – bloßes Ausnutzen genügt nicht
– Abgrenzung: räuberischer Diebstahl (§ 252) und räuberische Erpressung (§ 255), Abgrenzungsansätze BGH und Lehre
– Vorsatz, Zueignungsabsicht, Rechtswidrigkeit der erstrebten Zueignung
– Qualifikationen §§ 250, 251 im Überblick
– Abwandlung 2: Entreißen der Handtasche – Überraschung oder Kraft gegen die Person?
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 249, 250, 251, 252, 255 StGB; Vergleich §§ 240, 242 StGB

Rechtsprechung:
– BGH, Beschl. v. 20.3.2024 – 6 StR 572/23, Rn. 5 (finale Verknüpfung; bloßes Ausnutzen fortwirkender Gewalt genügt nicht)
– BGH, Beschl. v. 24.10.2024 – 4 StR 368/24, Rn. 7 (späterer Wegnahmeentschluss: zumindest konkludente neue Drohung nötig)
– BGH, Urt. v. 20.1.2016 – 1 StR 398/15, Rn. 17 (Vorstellung und Wille des Täters maßgebend)
– BGH, Beschl. v. 26.1.2022 – 3 StR 445/21, Rn. 5, 8 (Gewalt gegen eine Person; Entreißen der Handtasche)
– BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 11 (§ 252: bloße Fluchtabsicht genügt nicht)
– BGH, Beschl. v. 24.4.2018 – 5 StR 606/17, Rn. 13 (Abgrenzung Raub/räuberische Erpressung nach dem äußeren Erscheinungsbild)
– BGH, Beschl. v. 3.5.2018 – 3 StR 148/18, Rn. 7 (Zueignungsabsicht)
– BGH, Beschl. v. 28.10.2025 – 3 StR 458/25, Rn. 5 (Rechtswidrigkeit der Zueignung)
– BGH, Beschl. v. 3.3.2021 – 4 StR 338/20, Rn. 5 (Wegnahme)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Raub249 #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("Weck-nahme", "Wegnahme")      # Aussprachehilfe aus synth_el.AUSSPRACHE nur für die Vertonung
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III.")):
    srt = re.sub(r"Römisch\s+" + alt + r"\b:?", neu, srt)
srt = re.sub(r"\bachtzig Euro", "80 €", srt).replace("80 Euro", "80 €")
srt = re.sub(r"mit achtzig\n\n(\d+\n[^\n]+\n)Euro\. ", r"mit 80 €.\n\n\1", srt)      # Betrag über zwei Untertitel
srt = srt.replace("§ 249, Abs. 1", "§ 249 Abs. 1")
assert "achtzig" not in srt and "Abs. 1:" in srt
assert "Römisch" not in srt and "Weck-" not in srt
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Raub Prüfungsschema", "§ 252 StGB", "§ 255 StGB", "Handtaschenraub", "Finalität"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
