"""Nachbearbeitung der Upload-Texte für Folge 243 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_224.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen und Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel: Sprecherbezeichnung „Frau Hasselbach:“.
Aufruf: python3 meta_243.py <upload-ordner>"""
import json, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die Ehefrau belastet ihren Mann bei der Polizei"),
       (T("hv"), "Fall: Zeugnisverweigerung und der Polizeibeamte als Zeuge"),
       (T("fragen"), "Die Fragen und der Sachverhalt"),
       (T("a252"), "§ 252 StPO: Was sagt der Wortlaut?"),
       (T("rspr"), "Rechtsprechung: Verwertungsverbot"),
       (T("ga1"), "Streitstand: Verhörsperson als Zeuge?"),
       (T("richter"), "Ausnahme 1: der Richter, der belehrt hat"),
       (T("gest"), "Ausnahme 2: Gestattung durch die Zeugin"),
       (T("spont"), "Äußerungen außerhalb einer Vernehmung"),
       (T("l1"), "Lösung des Falls"),
       (T("v1"), "Revision: die Verfahrensrüge"),
       (T("tipp"), "Klausurtipp: § 252 in vier Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 252 StPO: Die Ehefrau schweigt in der Hauptverhandlung – dürfen Polizeibeamte oder der Ermittlungsrichter über ihre frühere Aussage berichten? Der Streitstand zur Verhörsperson, die Ausnahmen und die Revisionsrüge.

Der Fall: Frau Hasselbach belastet ihren Mann bei der Polizei schwer – er soll im gemeinsamen Malerbetrieb Kunden Arbeiten berechnet haben, die nie gemacht wurden. In der Hauptverhandlung verweigert sie als Ehefrau das Zeugnis. Das Gericht hört stattdessen den Polizeibeamten und verurteilt. Hat die Revision Erfolg?

Inhalt:
– § 252 StPO im Wortlaut: nur ein Verlesungsverbot
– Rechtsprechung: Verwertungsverbot, auch die Verhörsperson ist gesperrt
– Streitstand: Wortlaut-Ansicht, umfassendes Verbot, Großer Senat (GSSt 1/16)
– Ausnahme 1: Vernehmung des Richters nach Belehrung – keine weitergehende Belehrung nötig, Protokoll nur als Vorhalt
– Ausnahme 2: Gestattung der Verwertung nach qualifizierter Belehrung, kein Teilverzicht
– Äußerungen außerhalb einer Vernehmung
– Lösung als Verfahrensrüge (§ 344 Abs. 2 S. 2 StPO), Beruhen (§ 337 StPO)
– Klausurtipp in vier Schritten, Merksatz

Rechtsprechung:
– BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, BGHSt 61, 221, Leitsatz, Rn. 26, 32, 33, 36, 53, 64
– BGH, Urt. v. 30.6.2020 – 3 StR 377/18, Rn. 12: Vernehmung des Polizeibeamten grundsätzlich unzulässig
– BGH, Beschl. v. 18.10.2023 – 1 StR 222/23, Leitsatz, Rn. 6–8, 12: Gestattung, kein Teilverzicht, Beruhen
– BGH, Beschl. v. 13.6.2012 – 2 StR 112/12, BGHSt 57, 254, Leitsatz, Rn. 6–8: qualifizierte Belehrung, Protokoll, Rügevortrag
– BGH, Beschl. v. 11.4.2012 – 3 StR 108/12, Rn. 3 f.: Protokoll nur als Vorhalt; kein Widerspruch nötig
– BGH, Beschl. v. 23.10.2012 – 1 StR 137/12, Rn. 12: Äußerungen außerhalb einer Vernehmung

Mehr dazu: Folge 224 (Zeugnisverweigerungsrecht § 52 StPO), Folge 221 (Beweisverwertungsverbote), Folge 072 (Verfahrensrüge).

Hinweise: Der Fall ist ein Übungsfall. Die Gegenansichten sind nach der Darstellung in GSSt 1/16, Rn. 29, 36 wiedergegeben. Das Beispiel mit der Freundin wendet die Formel aus 1 StR 137/12, Rn. 12 an.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StPO #Strafprozessrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nHasselbach: ", "\nFrau Hasselbach: "),):
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert "Paragraf" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["§ 252 StPO", "Verwertungsverbot § 252 StPO", "Vernehmung der Verhörsperson", "Ermittlungsrichter Ausnahme",
             "GSSt 1/16", "Gestattung Verwertung", "§ 52 StPO", "Zeugnisverweigerung Hauptverhandlung", "Verfahrensrüge",
             "Strafprozessrecht"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
