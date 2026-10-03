"""Nachbearbeitung der Upload-Texte für Folge 111 (§ 252) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: „Römisch eins/zwei/…“ als I./II./…, Paragrafen-Umbruch, Beträge in Ziffern.
Aufruf: python3 meta_111.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Kopfhörer im Elektromarkt"),
       (T("p252"), "§ 252 StGB im Wortlaut und Aufbau"), (T("vt"), "Vortat: vollendeter, nicht beendeter Diebstahl"),
       (T("ft"), "Auf frischer Tat betroffen"), (T("nm"), "Nötigungsmittel: Gewalt gegen eine Person"),
       (T("subj"), "Vorsatz und Besitzerhaltungsabsicht"), (T("rs"), "Ergebnis, Rechtsfolge, Konkurrenzen"),
       (T("gv"), "Gegenvariante: Beute weggeworfen"), (T("tipp"), "Klausurtipp: Besitzerhaltungsabsicht"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Räuberischer Diebstahl § 252 StGB: Vollendeter Diebstahl, auf frischer Tat betroffen, Besitzerhaltungsabsicht – wann wird der Dieb zum Räuber? Das Prüfungsschema Schritt für Schritt an einem Klausurfall.

Der Fall: Gottfried steckt im Elektromarkt Kopfhörer für 129 € in die Innentasche seiner Jacke und geht ohne zu bezahlen hinaus. Direkt vor dem Eingang stellt ihn Mitarbeiterin Edda und greift nach seiner Jacke. Gottfried stößt sie weg, damit sie ihm die Kopfhörer nicht abnimmt, und rennt davon. Edda bleibt unverletzt. Ist Gottfried jetzt ein Räuber? Dazu die Gegenvariante: Gottfried wirft die Beute weg und will nur fliehen. (Übungsfall)

Inhalt:
– § 252 StGB im Wortlaut und die vier Prüfpunkte
– Vortat: Diebstahl vollendet (Einstecken, Verweis auf unsere Folge zur Gewahrsamsenklave), aber nicht beendet
– warum kein Raub: Gewalt erst nach Vollendung der Wegnahme
– auf frischer Tat betroffen: enger räumlicher und zeitlicher Zusammenhang; Streit um das Zuvorkommen (BGHSt 26, 95)
– Nötigungsmittel: Gewalt gegen eine Person, das Wegschubsen eines Ladendetektivs
– Vorsatz und Besitzerhaltungsabsicht: nicht einziges Motiv, bloße Fluchtabsicht genügt nicht
– Rechtsfolge „gleich einem Räuber“, Qualifikationen §§ 250, 251, Konkurrenz zu § 242
– Gegenvariante: Beute weggeworfen, nur Flucht
– Klausurtipp, Klausurschema, Merksatz

Normen: § 252 StGB; §§ 242, 249, 250, 251 StGB

Rechtsprechung:
– BGH, Urt. v. 27.2.1975 – 4 StR 310/74, BGHSt 26, 95 (Betreffen auch beim Zuvorkommen durch schnelles Zuschlagen)
– BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 11 f. (Besitzerhaltungsabsicht; bloße Fluchtabsicht genügt nicht)
– BGH, Urt. v. 9.3.2023 – 3 StR 392/22, Rn. 8 (Schubsen des Ladendetektivs als Gewalt; Fluchtwille daneben unschädlich)
– BGH, Beschl. v. 14.3.2023 – 4 StR 451/22, Rn. 7 (auf frischer Tat betroffen)
– BGH, Urt. v. 8.10.2014 – 5 StR 395/14, Rn. 6 f. (nicht beendet; frische Tat vor dem Markt)
– BGH, Beschl. v. 4.8.2015 – 3 StR 112/15, Rn. 5, 7 (Beobachtung von Anfang an; Vorsatz zum Betroffensein)
– BGH, Urt. v. 18.2.2010 – 3 StR 556/09, Rn. 11 f. (Vollendung durch Einstecken, auch unter Beobachtung)
– BGH, Urt. v. 18.4.2002 – 3 StR 52/02, Rn. 16 (§ 249 bis zur Vollendung, § 252 von der Vollendung bis zur Beendigung)
– BGH, Beschl. v. 13.3.2002 – 1 StR 47/02, Rn. 6 (Gewalt gegen eine Person)
– BGH, Beschl. v. 22.11.2012 – 1 StR 378/12, Rn. 9 (Gesetzeseinheit mit dem Diebstahl)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#RäuberischerDiebstahl #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("Weck-nahme", "Wegnahme")      # Aussprachehilfe aus synth_el.AUSSPRACHE nur für die Vertonung
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III.")):
    srt = re.sub(r"Römisch\s+" + alt + r"\b:?", neu, srt)
srt = re.sub(r"\bhundertneunundzwanzig Euro", "129 €", srt).replace("129 Euro", "129 €")
srt = srt.replace("\nund zweihunderteinundfünfzig\n", "\nund 251\n")    # „§§ 250 und 251“ über zwei Untertitel
assert "Römisch" not in srt and "Weck-" not in srt and "neunundzwanzig" not in srt and "zweihundert" not in srt
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("räuberischer Diebstahl Prüfungsschema", "§ 252 StGB", "Ladendiebstahl Gewalt", "Gewahrsamsenklave", "BGHSt 26, 95"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
