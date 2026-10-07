"""Nachbearbeitung der Upload-Texte für Folge 228 (nach meta_225.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel: Zahlen in Schriftform, Sprechernamen.
Aufruf: python3 meta_228.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Filesharing über den Familienanschluss"),
       (T("plan"), "Aufbau in fünf Schritten"),
       (T("g1"), "Grundsatz: Darlegungs- und Beweislast der Klägerin"),
       (T("e1"), "§ 138 ZPO im Wortlaut: Erklärungspflicht und Geständnisfiktion"),
       (T("v1"), "Tatsächliche Vermutung und sekundäre Darlegungslast"),
       (T("i1"), "Was muss der Anschlussinhaber vortragen?"),
       (T("u1"), "Keine Umkehr der Beweislast"),
       (T("f1"), "Der Fall: Vortrag genügt, Klage abgewiesen"),
       (T("gf"), "Gegenfall: pauschales Bestreiten, § 138 Abs. 3 ZPO"),
       (T("tipp"), "Klausurtipp: Relation und Beklagtenstation"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Sekundäre Darlegungslast nach § 138 ZPO: Wann muss die nicht beweisbelastete Partei näher vortragen – und warum verschiebt sich die Beweislast dadurch nicht? Am Filesharing-Fall nach BGH „BearShare“, für die Relation im 2. Examen.

Der Fall: Bei Familie Mehnert nutzen vier Menschen denselben Router. Eine Filmfirma verklagt Herrn Mehnert als Anschlussinhaber auf Schadensersatz, weil über seinen Anschluss ein Spielfilm in einer Tauschbörse angeboten wurde. Was muss er vortragen, und wer muss am Ende was beweisen?

Inhalt:
– Grundsatz: Die Klägerin trägt die Darlegungs- und Beweislast für die Täterschaft (§ 97 Abs. 2 UrhG)
– § 138 Abs. 1, 2 ZPO (Wahrheits- und Erklärungspflicht) und § 138 Abs. 3 ZPO (Geständnisfiktion) im Wortlaut
– Tatsächliche Vermutung der Täterschaft des Anschlussinhabers; Voraussetzungen der sekundären Darlegungslast
– Inhalt: Mitnutzer mit selbständigem Zugang benennen, im Rahmen des Zumutbaren nachforschen und das Ergebnis mitteilen; keine Pflicht, den Computer des Ehegatten zu untersuchen
– Keine Umkehr der Beweislast
– Fall: konkreter Vortrag, die Klägerin muss beweisen; Gegenfall: pauschales Bestreiten, § 138 Abs. 3 ZPO, Haftung als Täter; Name des geständigen Kindes
– Klausurtipp für die Relation (Beklagtenstation), Klausurschema, Merksatz

Normen: § 138 Abs. 1–3 ZPO; § 97 Abs. 2 UrhG

Rechtsprechung:
– BGH, Urt. v. 8.1.2014 – I ZR 169/12 (BearShare), BGHZ 200, 76, Rn. 14–20
– BGH, Urt. v. 6.10.2016 – I ZR 154/15 (Afterlife), Rn. 14, 15, 26
– BGH, Urt. v. 30.3.2017 – I ZR 19/16 (Loud), Leitsatz, Rn. 15, 27, 29

Hinweise: Fall und Personen sind erfunden; keine echten Filme, Firmen oder Tauschbörsen. Die Stationen der Relation sind Ausbildungs- und Klausurkonvention. Die Beweislast beim non liquet erklärt das Video „Beweislast ZPO: Wer verliert beim non liquet?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Darlegungslast #ZPO #Referendariat
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n +", "\n", srt)
for a_, b_ in [("tausend Euro", "1.000 Euro"), ("zwölften Mai", "12. Mai"), ("21 Uhr 47", "21:47 Uhr"),
               ("einundzwanzig Uhr siebenundvierzig", "21:47 Uhr")]:
    srt = srt.replace(a_, b_)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
