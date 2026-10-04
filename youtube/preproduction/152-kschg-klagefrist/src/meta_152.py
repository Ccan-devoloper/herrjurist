"""Nachbearbeitung der Upload-Texte für Folge 152 (nach meta_149.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Normzitate, Zahlen).
Aufruf: python3 meta_152.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kündigung nach acht Jahren ohne Grund, Sachverhalt"),
       (T("aufbau"), "Aufbau: Anwendbarkeit, Sozialwidrigkeit, Klagefrist"),
       (T("p1"), "§ 1 Abs. 1 KSchG: Wartezeit (persönlich)"),
       (T("p23"), "§ 23 KSchG: Kleinbetrieb und Schwellenwert"),
       (T("p12"), "§ 1 Abs. 2 KSchG: personen-, verhaltens-, betriebsbedingt"),
       (T("begr"), "Muss die Kündigung begründet werden? Beweislast"),
       (T("falle"), "Die Falle: Klagefrist § 4 KSchG"),
       (T("p7"), "§ 7 KSchG: Kündigung gilt als wirksam, § 5 KSchG"),
       (T("frist"), "Fristberechnung §§ 187, 188 BGB"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp: Prüfungsreihenfolge"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Kündigungsschutzgesetz (§§ 1, 4, 7, 23 KSchG): Wann gilt es, welche Kündigungsgründe gibt es und warum ist die Drei-Wochen-Frist für die Klage so gefährlich?

Der Fall: Kornelia arbeitet seit acht Jahren als Gärtnerin in einer Gärtnerei mit 25 Beschäftigten. Der Inhaber übergibt ihr eine schriftliche, ordentliche Kündigung – ohne jeden Grund. „Einen Grund muss ich Ihnen nicht nennen.“ Kornelia will es sich erst einmal in Ruhe überlegen.

Inhalt:
– Persönlicher Anwendungsbereich: § 1 Abs. 1 KSchG im Wortlaut, Wartezeit von mehr als sechs Monaten
– Betrieblicher Anwendungsbereich: § 23 Abs. 1 S. 3 KSchG im Wortlaut, „in der Regel“ mehr als zehn Arbeitnehmer, Teilzeit anteilig (S. 4); die Klagefrist gilt auch im Kleinbetrieb
– Soziale Rechtfertigung: § 1 Abs. 2 S. 1 KSchG im Wortlaut – personen-, verhaltens- und betriebsbedingte Gründe; Abmahnung bei verhaltensbedingter Kündigung in der Regel erforderlich
– Muss das Kündigungsschreiben einen Grund nennen? Beweislast nach § 1 Abs. 2 S. 4 KSchG, Betriebsgröße
– Die Falle: Klage binnen drei Wochen nach Zugang der schriftlichen Kündigung, § 4 S. 1 KSchG; sonst gilt die Kündigung nach § 7 KSchG als von Anfang an wirksam; nachträgliche Zulassung nach § 5 KSchG
– Fristberechnung mit §§ 187 Abs. 1, 188 Abs. 2 BGB am Beispiel (Zugang Montag, 5.10.2026 – Fristende Montag, 26.10.2026)
– Lösung, Klausurtipp (Prüfungsreihenfolge, § 102 BetrVG), Prüfschema, Merksatz

Normen: §§ 1, 4, 5, 7, 23 KSchG; §§ 187, 188, 623 BGB; § 102 BetrVG

Rechtsprechung:
– BAG, Urt. v. 24.1.2013 – 2 AZR 140/12, Rn. 9, 11, 27 (Schwellenwert des § 23 Abs. 1 S. 3 KSchG „in der Regel“; Darlegungs- und Beweislast für die Betriebsgröße beim Arbeitnehmer)
– BAG, Urt. v. 20.6.2013 – 2 AZR 790/11, Rn. 11 f. (Wartezeit des § 1 Abs. 1 KSchG)
– BAG, Urt. v. 10.6.2010 – 2 AZR 541/09, Rn. 36 f. (Kündigung wegen Pflichtverletzung setzt regelmäßig eine Abmahnung voraus)

Hinweise: Ob die Kündigung im Fall sozial gerechtfertigt ist, bleibt offen – das entscheidet das Arbeitsgericht. Die Grenze von zehn Arbeitnehmern gilt für Arbeitsverhältnisse, die nach dem 31.12.2003 begonnen haben. Dass die Kündigung schriftlich erklärt und zugegangen sein muss, zeigt die Folge „Kündigung per WhatsApp“ (§ 623 BGB), die Beweislast im Prozess die Folge zur Beweislast.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Kündigungsschutz #Arbeitsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier|fünf):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV.", "fünf": "V."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"fünfundzwanzig(\s)Beschäftigten", r"25\1Beschäftigten"),
                       (r"null Komma fünf ", "0,5 "),
                       (r"null Komma(\n\n\d+\n[^\n]+\n)fünfundsiebzig\. ?", r"0,75.\1"),
                       (r"fünften(\s)Oktober", r"5.\1Oktober"), (r"sechsundzwanzigsten(\s)Oktober", r"26.\1Oktober"),
                       (r"acht(\s)Jahren", r"8\1Jahren"), (r"und mit fünfundzwanzig", "und mit 25")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nSteinmetz: ", "\nHerr Steinmetz: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
