"""Nachbearbeitung der Upload-Texte für Folge 104 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: „Römisch eins/zwei/…“ als I./II./…, Aussprachehilfe „Weck-nahme“ zurück, Beträge in Ziffern.
Aufruf: python3 meta_104.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Überfall auf den Kiosk"),
       (T("p25"), "§ 25 Abs. 2 StGB im Wortlaut"), (T("aufbau"), "Aufbau: gemeinsam oder getrennt prüfen"),
       (T("raub"), "Raub durch Kilian und Fenja: Zurechnung"), (T("tp"), "Gemeinsamer Tatplan"),
       (T("ta"), "Gemeinsame Tatausführung"), (T("abgr"), "Abgrenzung Täter und Gehilfe"),
       (T("thea"), "Schmiere stehen: Mittäterschaft oder Beihilfe?"), (T("p27"), "Beihilfe, § 27 Abs. 1 StGB"),
       (T("ans"), "Der Planer ohne Mitwirkung am Tatort: der Streit"), (T("ents"), "Streitentscheid"),
       (T("rf"), "Rechtsfolge, Exzess und Ergebnis"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Mittäterschaft § 25 II StGB: Gemeinsamer Tatplan, arbeitsteilige Ausführung, wechselseitige Zurechnung – und reicht ein Beitrag im Vorbereitungsstadium? Das Schema der Mittäterschaft Schritt für Schritt an einem Klausurfall.

Der Fall: Ansgar plant den Überfall auf einen Kiosk und bleibt zu Hause. Thea steht an der Ecke Schmiere, Kilian bedroht den Inhaber Emil mit Worten, Fenja greift in die Kasse und nimmt 650 €. Wer ist Mittäter, wer nur Gehilfe – und was ist mit dem Planer, der gar nicht dabei war? (Übungsfall)

Inhalt:
– § 25 Abs. 2 StGB im Wortlaut: gemeinsamer Tatplan und gemeinsame Tatausführung
– Aufbau im Gutachten: gemeinsame oder getrennte Prüfung – und warum
– wechselseitige Zurechnung beim Raub (Drohung durch den einen, Wegnahme durch die andere)
– gemeinsamer Tatplan: auch stillschweigend; sukzessive Mittäterschaft
– wesentlicher Tatbeitrag; Zueignungsabsicht in eigener Person
– Abgrenzung Täter und Gehilfe: Tatherrschaftslehre und wertende Gesamtbetrachtung des BGH
– Schmiere stehen: Mittäterschaft oder Beihilfe (§ 27 Abs. 1 StGB im Wortlaut)
– der Planer ohne Mitwirkung im Ausführungsstadium: strenge und gemäßigte Tatherrschaftslehre, BGH – mit Streitentscheid
– Rechtsfolge und Exzess
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 25 Abs. 2, 27 Abs. 1 StGB; § 249 StGB; § 26 StGB

Rechtsprechung:
– BGH, Urt. v. 23.3.2023 – 3 StR 363/22, Rn. 8 (Mittäterschaft ohne Anwesenheit am Tatort; wertende Gesamtbetrachtung)
– BGH, Beschl. v. 6.8.2019 – 3 StR 189/19, Rn. 4–7 (Planer als Mittäter eines Raubes)
– BGH, Urt. v. 13.4.2023 – 5 StR 533/22, Rn. 7 (konkludenter Tatplan)
– BGH, Urt. v. 26.9.2024 – 4 StR 115/24, Rn. 44 (Exzess), Rn. 56 (sukzessive Mittäterschaft)
– BGH, Urt. v. 26.4.2012 – 4 StR 665/11, Rn. 24 (Schmierestehen als untergeordneter Beitrag)
– BGH, Beschl. v. 29.9.2005 – 4 StR 420/05, Rn. 4 f. (Wache mit geringem Beuteanteil: Beihilfe)
– BGH, Beschl. v. 10.7.2025 – 3 StR 496/23, Rn. 42 (Hilfeleisten)
– BGH, Beschl. v. 3.5.2018 – 3 StR 148/18, Rn. 7 (Zueignungsabsicht beim Raub)

Lehrmeinungen nach dem Vorlesungsskript Hefendehl, Strafrecht AT, Universität Freiburg (strafrecht-online.org), § 28 KK 710–718.

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Mittäterschaft #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("Weck-nahme", "Wegnahme")      # Aussprachehilfe aus synth_el.AUSSPRACHE nur für die Vertonung
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III.")):
    srt = re.sub(r"Römisch\s+" + alt + r"\b:?", neu, srt)
srt = srt.replace("sechshundertfünfzig Euro", "650 €")
srt = re.sub(r"(§§? \d+), Abs\.", r"\1 Abs.", srt)          # „§ 25, Abs. 2“ → „§ 25 Abs. 2“
srt = re.sub(r"\bfünfzig Euro", "50 €", srt).replace("50 Euro", "50 €").replace("650 Euro", "650 €")
assert "Römisch" not in srt and "Weck-" not in srt and "Euro" not in srt, "Untertitel prüfen"
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Mittäterschaft Prüfungsschema", "§ 25 II StGB", "Schmiere stehen", "Beihilfe § 27", "Tatherrschaftslehre"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
