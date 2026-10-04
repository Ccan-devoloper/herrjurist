"""Nachbearbeitung der Upload-Texte für Folge 130 (Kopie von meta_124.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Promillewerte, Jahreszahl und Gliederungsziffern in den Untertiteln als Ziffern.
Aufruf: python3 meta_130.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Verkehrskontrolle mit 0,8 und 1,2 Promille"),
       (T("p316"), "§ 316 StGB im Wortlaut"),
       (T("abs"), "Absolute Fahruntüchtigkeit: 1,1 ‰ (Radfahrer 1,6 ‰)"),
       (T("rel"), "Relative Fahruntüchtigkeit: etwa ab 0,3 ‰"),
       (T("owi"), "Ordnungswidrigkeit: 0,5 ‰, § 24a StVG"),
       (T("vors"), "Vorsatz oder Fahrlässigkeit"),
       (T("p315c"), "Abgrenzung: § 315c StGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Trunkenheit im Verkehr (§ 316 StGB): Was bedeuten 0,3, 0,5, 1,1 und 1,6 Promille – absolute und relative Fahruntüchtigkeit, Straftat oder Ordnungswidrigkeit?

Der Fall: Bei einer Verkehrskontrolle am Ortsausgang hat Heinrich 0,8 Promille – er ist aber schnurgerade und ohne jeden Fahrfehler gefahren. Kurz darauf wird Siegfried mit 1,2 Promille angehalten; auch er fuhr unauffällig und fühlt sich „topfit“. Gefährdet wurde niemand. Wer macht sich strafbar, wer handelt nur ordnungswidrig?

Inhalt:
– § 316 Abs. 1 StGB im Wortlaut: Führen eines Fahrzeugs im Verkehr, Fahruntüchtigkeit infolge Alkohols
– Grenzwerte sind Beweisregeln der Rechtsprechung, keine Tatbestandsmerkmale
– Absolute Fahruntüchtigkeit: ab 1,1 ‰ für Kraftfahrer (BGHSt 37, 89; Grundwert 1,0 ‰ + Sicherheitszuschlag 0,1 ‰), unwiderleglich – kein Gegenbeweis durch gerades Fahren; Radfahrer nach OLG-Rechtsprechung 1,6 ‰
– Relative Fahruntüchtigkeit: etwa ab 0,3 ‰, nur mit alkoholbedingten Ausfallerscheinungen
– Ordnungswidrigkeit nach § 24a Abs. 1 StVG (Wortlaut): 0,5 ‰ bzw. 0,25 mg/l Atemalkohol, ohne Ausfallerscheinungen; Fahrverbot in der Regel; Cannabis (§ 24a Abs. 1a), Fahranfänger (§ 24c StVG)
– Vorsatz oder Fahrlässigkeit (§ 316 Abs. 2 StGB)
– Abgrenzung zu § 315c StGB: konkrete Gefahr (Beinahe-Unfall)
– Ergebnis mit § 21 OWiG und § 69 StGB, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 316, 315c, 69 StGB; §§ 24a, 24c, 25 StVG; § 21 OWiG

Rechtsprechung:
– BGH, Beschl. v. 28.6.1990 – 4 StR 297/90, BGHSt 37, 89 (absolute Fahruntüchtigkeit für Kraftfahrer ab 1,1 ‰)
– BGH, Beschl. v. 20.7.1999 – 4 StR 106/99 (BGHSt 45, 140), Rn. 12, 15 f. (Grundwert 1,0 ‰ und Sicherheitszuschlag 0,1 ‰)
– BGH, Beschl. v. 2.3.2021 – 4 StR 366/20, Rn. 8 f. (1,1 ‰ als unwiderleglicher Indizwert; relative Fahruntüchtigkeit nur mit zusätzlichen Tatsachen; Fahrfehler muss alkoholbedingt sein)
– BGH, Beschl. v. 13.4.2023 – 4 StR 439/22, Rn. 4, 6 (Grenzwert gilt unwiderleglich für alle Kraftfahrer)
– BGH, Beschl. v. 26.2.2025 – 4 StR 526/24, Rn. 5, 7 (Beweisanzeichen der relativen Fahruntüchtigkeit; bloße Enthemmung genügt nicht)
– BGH, Urt. v. 9.4.2015 – 4 StR 401/14 (BGHSt 60, 227), Rn. 7 (Vorsatz bei § 316; Grenzwerte sind Beweisregeln)
– BGH, Beschl. v. 21.6.2017 – 4 StR 386/16, Rn. 2 (obergerichtliche Rechtsprechung zum Radfahrer-Grenzwert nicht beanstandet)
– OLG Karlsruhe, Beschl. v. 14.7.2020 – 2 Rv 35 Ss 175/20 (Grenzwert für Radfahrer 1,6 ‰; Pedelecs)
– OLG Hamm, Urt. v. 25.8.2010 – I-20 U 74/10, Rn. 28 (relative Fahruntüchtigkeit beginnt etwa bei 0,3 ‰)
– BGH, Beschl. v. 13.3.2025 – 4 StR 391/24, Rn. 4 (konkrete Gefahr bei § 315c: Beinahe-Unfall)

Hinweise: 0,3 ‰ ist keine starre Grenze; die Rechtsprechung nennt einen ungefähren Wert. Der Radfahrer-Grenzwert von 1,6 ‰ stammt aus der Rechtsprechung der Oberlandesgerichte. Ob der 1,1-‰-Grenzwert auch für E-Scooter gilt, hat der BGH bisher offengelassen. Der Fall ist ein vereinfachter Übungsfall (Blutalkoholwerte zur Tatzeit, keine Rückrechnung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026, StVG zuletzt geändert durch Gesetz vom 25.9.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#TrunkenheitimVerkehr #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

ZIFFER = {"null": "0", "eins": "1", "zwei": "2", "drei": "3", "fünf": "5", "sechs": "6", "acht": "8"}


srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)


def ersetze(m):
    vor, nach = m.group(1), m.group(2)
    nach_z = "25" if re.fullmatch(r"zwei\s+fünf", nach) else ZIFFER[nach]
    text = f"{ZIFFER[vor]},{nach_z}"
    return text + ("\n" if "\n" in m.group(0) else "")


srt = re.sub(r"\b(null|eins|zwei)\n\n(\d+\n[^\n]+-->[^\n]+\n)Komma\s+(fünf|eins|drei|sechs|acht|null|zwei)\b",
             lambda m: f"{ZIFFER[m.group(1)]},{ZIFFER[m.group(3)]}\n\n{m.group(2)}", srt)   # Zahl über eine Untertitelgrenze
srt = re.sub(r"\b(null|eins|zwei)\s+Komma\s+(zwei\s+fünf|null|eins|zwei|drei|fünf|sechs|acht)\b(?:\n)?", ersetze, srt)
srt = srt.replace("neunzehnhundertneunzig", "1990").replace("unter\neinundzwanzig", "unter 21\n").replace(
    "unter einundzwanzig", "unter 21")
srt = srt.replace("Römisch eins,", "I.").replace("Römisch zwei und drei:", "II. und III.:")
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert not re.search(r"§\n", srt) and "Komma" not in srt, re.findall(r".*Komma.*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
