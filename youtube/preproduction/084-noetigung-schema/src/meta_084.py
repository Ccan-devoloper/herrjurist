"""Nachbearbeitung der Upload-Texte für Folge 084 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: „Römisch eins/zwei/…“ als I./II./…, Paragrafen-Umbruch.
Aufruf: python3 meta_084.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Kaution gegen Rücknahme der Beschwerde"),
       (T("pruef"), "§ 240 Abs. 1: Nötigungsmittel und Nötigungserfolg"), (T("gewalt"), "Gewalt"),
       (T("drohung"), "Drohung"), (T("unterl"), "Drohung mit einem Unterlassen"), (T("empf"), "Empfindliches Übel"),
       (T("erfolg"), "Nötigungserfolg, Kausalität, Vorsatz"), (T("rw"), "Rechtswidrigkeit: Verwerflichkeit, § 240 Abs. 2"),
       (T("mz"), "Mittel-Zweck-Relation und Inkonnexität"), (T("gegen"), "Gegenfall: Klage auf die Miete"),
       (T("schuld"), "Schuld, § 240 Abs. 4, Ergebnis"), (T("erpr"), "Abgrenzung: Erpressung, § 253 StGB"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Nötigung § 240 Schema: Gewalt oder Drohung, Nötigungserfolg und die Verwerflichkeitsprüfung nach § 240 II StGB (Mittel-Zweck-Relation) – Schritt für Schritt an einem Klausurfall.

Der Fall: Gesine ist aus ihrer Mietwohnung ausgezogen. Ihr Vermieter Gernot schuldet ihr noch die Kaution von 1.500 €. Er sagt: „Ihre Kaution bekommen Sie erst, wenn Sie die Beschwerde beim Bauamt zurückziehen.“ Gesine zieht die Beschwerde zurück. Hat Gernot sich strafbar gemacht? (Übungsfall)

Inhalt:
– § 240 Abs. 1 StGB im Wortlaut: Nötigungsmittel und Nötigungserfolg
– Gewalt (kurz; ausführlich in unserer Folge zur Sitzblockade)
– Drohung: künftiges Übel, auf das der Täter Einfluss hat oder zu haben vorgibt
– Drohung mit einem Unterlassen – hier: die geschuldete Kaution nicht zurückzahlen
– Empfindliches Übel und besonnene Selbstbehauptung
– Nötigungserfolg, Kausalität, Vorsatz
– Rechtswidrigkeit in zwei Stufen: Rechtfertigungsgründe, dann Verwerflichkeit nach § 240 Abs. 2 StGB („sozial unerträglich“)
– Mittel-Zweck-Relation, fehlender Zusammenhang (Inkonnexität), Gegenfall: Drohung mit einer Klage auf offene Miete
– Schuld, besonders schwerer Fall (§ 240 Abs. 4), Abgrenzung zur Erpressung (§ 253 StGB)
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 240, 253 StGB

Rechtsprechung:
– BGH, Beschl. v. 5.9.2013 – 1 StR 162/13, Rn. 64, 65, 68, 70, 74 (Übel, Drohung, empfindliches Übel, besonnene Selbstbehauptung, Verwerflichkeit)
– BGH, Urt. v. 25.2.2021 – 3 StR 204/20, Rn. 30, 31 (Gewalt; Verwerflichkeit nicht durch das Nötigungsmittel indiziert)
– BGH, Beschl. v. 10.6.2025 – 3 StR 561/24, Rn. 10 (Gläubiger haben sich staatlicher Hilfe zu bedienen)
– OLG Köln, Urt. v. 11.6.2024 – 1 ORs 52/24, Rn. 43, 46 (Drohung, Drohung mit einem Unterlassen)
– OLG Hamm, Beschl. v. 14.12.2021 – 7 U 8/21, Rn. 9 (Mittel-Zweck-Relation, fehlender Zusammenhang)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Nötigung240Schema #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III."), ("vier", "IV.")):
    srt = re.sub(r"Römisch\s+" + alt + r"\b,?", neu, srt)
srt = re.sub(r"[Ee]intausendfünfhundert Euro", "1.500 €", srt).replace("IV.:", "IV.")
assert "Römisch" not in srt and "tausend" not in srt
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("§ 253 StGB", "Verwerflichkeit", "Drohung mit Unterlassen", "Inkonnexität"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
