"""Nachbearbeitung der Upload-Texte für Folge 088 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Hinweis zum Landesrecht, Rechtsprechung mit Rn.,
Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_088.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Riesenbau neben dem Einfamilienhaus"), (T("sv"), "Sachverhalt"),
       (T("klage"), "Drittanfechtung und Schutznormtheorie"), (T("ueber"), "Drittschützende Normen im Überblick"),
       (T("herkunft"), "Herkunft: §§ 35 III, 34 I BauGB"), (T("wl15"), "§ 15 I 2 BauNVO und § 31 II BauGB"),
       (T("mst"), "Maßstab: Abwägung der Zumutbarkeit"), (T("schat"), "Schatten und Abstandsflächen als Indiz"),
       (T("erdr"), "Erdrückende Wirkung"), (T("fall2"), "Lösung und Eilrechtsschutz"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rücksichtnahmegebot (§ 15 I 2 BauNVO, § 34 BauGB): Wann ist ein achtstöckiger Bau nebenan rücksichtslos? Erdrückende Wirkung – bundesweit erklärt.

Der Fall: Frau Kolbe wohnt seit 40 Jahren in ihrem kleinen Einfamilienhaus am Stadtrand. Nebenan genehmigt die Bauaufsicht einen Wohnblock mit 8 Geschossen – 25 m hoch, 50 m lang, 14 m vor ihrem Haus. Die Abstandsflächen sind eingehalten, ihr Garten läge im Schatten. Kann sie die Baugenehmigung zu Fall bringen? (Übungsfall)

Inhalt:
– Nachbarklage: Anfechtungsklage eines Dritten, Klagebefugnis nach § 42 II VwGO, Schutznormtheorie, § 113 I 1 VwGO
– Drittschützende Normen im Überblick: Abstandsflächen, Gebietserhaltungsanspruch, Maß der baulichen Nutzung
– Herkunft des Rücksichtnahmegebots: § 35 III BauGB (Außenbereich), Einfügen nach § 34 I 1 BauGB (Innenbereich), § 15 I 2 BauNVO (mit Bebauungsplan), § 31 II BauGB (Befreiung)
– Maßstab: Abwägung der Zumutbarkeit (BVerwGE 52, 122)
– Verschattung, Abstandsflächen als Indiz, erdrückende und abriegelnde Wirkung
– Ergebnis und Eilrechtsschutz (§ 212a BauGB, §§ 80a III, 80 V VwGO – eigenes Video)
– Klausurtipp, Klausurschema, Merksatz

Landesrecht: Die Abstandsflächen regelt die Bauordnung deines Landes – bitte dort nachschlagen; ebenso, ob vor der Klage ein Widerspruch nötig ist. Das Rücksichtnahmegebot selbst ist Bundesrecht und überall gleich.

Rechtsprechung:
– BVerwG, Urt. v. 25.2.1977 – IV C 22.75, BVerwGE 52, 122 (grundlegend; Abwägungsformel wiedergegeben in BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 12)
– BVerwG, Beschl. v. 27.3.2018 – 4 B 50.17, Rn. 4 (Einfügen nach § 34 I, Abstandsflächen als Regelindiz)
– BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9, 10 (Besonnung, gleiche Geschosshöhe)
– BVerwG, Beschl. v. 11.12.2006 – 4 B 72.06, Rn. 8, 9 (§ 35 III, erdrückende und abriegelnde Wirkung)
– BVerwG, Urt. v. 29.11.2012 – 4 C 8.11, Rn. 16 (§ 15 I 2 BauNVO)
– BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 12, 21 (§ 31 II BauGB, Maßfestsetzungen)
– BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8 (Gebietserhaltungsanspruch)
– OVG NRW, Urt. v. 17.3.2021 – 7 A 1791/19, Rn. 39, 42 (erdrückende Wirkung, Verschattung)
– OVG NRW, Beschl. v. 9.2.2009 – 10 B 1713/08, Rn. 8 (§ 34 I nachbarschützend nur über das Rücksichtnahmegebot)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026 (BauGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nKolbe:", "\nFrau Kolbe:"), ("\nReimers:", "\nHerr Reimers:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
