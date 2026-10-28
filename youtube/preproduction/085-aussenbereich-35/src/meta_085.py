"""Nachbearbeitung der Upload-Texte für Folge 085 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Hinweis zum Landesrecht, Rechtsprechung mit Rn.,
Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_085.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das Wochenendhaus im Wald"), (T("antrag"), "Bauantrag, Ablehnung und Sachverhalt"),
       (T("ebenen"), "Zwei Ebenen des Baurechts, Vorhaben § 29"), (T("reihe"), "Der Bereich: §§ 30, 34, 35 BauGB"),
       (T("abs1"), "Privilegierte Vorhaben, § 35 I BauGB"), (T("wl352"), "Sonstige Vorhaben, § 35 II BauGB"),
       (T("wl353"), "Öffentliche Belange, § 35 III BauGB"), (T("split"), "Splittersiedlung"),
       (T("abs4"), "§ 35 IV BauGB und Ergebnis"), (T("wald"), "Waldrecht und Rechtsschutz"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Außenbereich § 35 BauGB: Warum ein Wochenendhaus im Wald meist unzulässig ist – privilegierte und sonstige Vorhaben, öffentliche Belange. Bundesweit erklärt.

Der Fall: Frau Wiesner kauft ein Waldgrundstück weit draußen vor dem Dorf und will dort ein kleines Wochenendhaus bauen. Es gibt keinen Bebauungsplan, der Flächennutzungsplan stellt Wald dar. Die Bauaufsichtsbehörde lehnt den Bauantrag ab – zu Recht? (Übungsfall)

Inhalt:
– Zwei Ebenen: Bauplanungsrecht (BauGB) und Bauordnungsrecht (Landesbauordnung)
– I. Vorhaben nach § 29 I BauGB
– II. Der Bereich: Bebauungsplan (§ 30), Innenbereich (§ 34) oder Außenbereich (§ 35 BauGB)
– III. Privilegierte Vorhaben nach § 35 I BauGB (z. B. Land- und Forstwirtschaft Nr. 1, Windenergie Nr. 5; Nr. 4 und Wochenendhausgebiete nach § 10 BauNVO)
– IV. Sonstige Vorhaben nach § 35 II BauGB: öffentliche Belange nach § 35 III 1 BauGB (Flächennutzungsplan Nr. 1, natürliche Eigenart der Landschaft Nr. 5, Splittersiedlung Nr. 7), begünstigte Vorhaben nach § 35 IV BauGB, Erschließung
– Ergebnis, Waldrecht (§ 9 I BWaldG), Rechtsschutz durch Verpflichtungsklage (§ 42 I VwGO)
– Klausurtipp, Klausurschema, Merksatz

Landesrecht: Ob und wie eine Baugenehmigung zu beantragen ist und wann sie erteilt werden muss, regelt die Bauordnung deines Landes; die Waldumwandlung regelt das Landeswaldgesetz im Rahmen von § 9 BWaldG, ob vor der Klage ein Widerspruch nötig ist, ebenfalls das Landesrecht. Bitte im Recht deines Landes nachschlagen. Die Prüfung nach § 35 BauGB ist Bundesrecht und überall gleich.

Rechtsprechung:
– BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 11 (Außenbereich), Rn. 19 (Splittersiedlung), Rn. 20 (Bevorrechtigung privilegierter Vorhaben), Rn. 21 f. (Zersiedlung, Vorbildwirkung)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026 (BauGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nWiesner:", "\nFrau Wiesner:"), ("\nDreher:", "\nHerr Dreher:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
