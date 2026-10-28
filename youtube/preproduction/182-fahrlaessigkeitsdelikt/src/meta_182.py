"""Nachbearbeitung der Upload-Texte für Folge 182 (nach meta_179.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Paragrafen).
Aufruf: python3 meta_182.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: die morsche Balkonbrüstung"),
       (T("p15"), "§ 15 StGB: Fahrlässigkeit nur bei ausdrücklicher Strafdrohung"),
       (T("p229"), "§ 229 und § 222 StGB im Wortlaut"),
       (T("stufen"), "Das Schema in drei Stufen"),
       (T("erfolg"), "1. Erfolg, 2. Unterlassen und Garantenstellung"),
       (T("kaus"), "3. Kausalität"),
       (T("sorg"), "4. Objektive Sorgfaltspflichtverletzung"),
       (T("vorh"), "5. Objektive Vorhersehbarkeit"),
       (T("pwz"), "6. Pflichtwidrigkeitszusammenhang und Schutzzweck"),
       (T("rw"), "Rechtswidrigkeit und Schuld"),
       (T("erg"), "Ergebnis und Variante § 222 StGB"),
       (T("vors"), "Bewusste Fahrlässigkeit oder bedingter Vorsatz?"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fahrlässigkeitsdelikt Schema: Wie prüft man §§ 222, 229 StGB mit Sorgfaltspflichtverletzung, Vorhersehbarkeit und Zurechnungszusammenhang?

Der Fall: Herr Berger vermietet in seinem Haus eine Wohnung mit Balkon. Die Holzbrüstung ist morsch, die Mieterin weist ihn dreimal darauf hin – er tut sechs Wochen nichts. Dann lehnt sich ein Gast an die Brüstung, sie bricht, der Gast wird schwer verletzt. Ist Herr Berger strafbar, obwohl er niemanden verletzen wollte?

Inhalt:
– § 15 StGB: Fahrlässigkeit ist nur strafbar, wo das Gesetz es ausdrücklich sagt (im Wortlaut)
– § 229 und § 222 StGB im Wortlaut – ein Schema für beide
– I. Tatbestand: 1. Erfolg, 2. Handlung oder Unterlassen (Garantenstellung aus Verkehrssicherungspflicht, § 13 StGB), 3. Kausalität, 4. objektive Sorgfaltspflichtverletzung, 5. objektive Vorhersehbarkeit, 6. Pflichtwidrigkeitszusammenhang (rechtmäßiges Alternativverhalten) und Schutzzweck
– II. Rechtswidrigkeit, III. Schuld: subjektive Sorgfaltspflichtverletzung und subjektive Vorhersehbarkeit
– Ergebnis: fahrlässige Körperverletzung durch Unterlassen (§§ 229, 13 StGB), Strafantrag (§ 230 StGB); Variante: fahrlässige Tötung (§§ 222, 13 StGB)
– Abgrenzung: bewusste Fahrlässigkeit oder bedingter Vorsatz
– Klausurtipp, Prüfschema, Merksatz

Normen: §§ 13, 15, 222, 229, 230 StGB

Rechtsprechung:
– BGH, Beschl. v. 5.5.2021 – 4 StR 19/20 (BGHSt 66, 119), Rn. 11, 14, 18, 21 f. (Fahrlässigkeit: Sorgfaltsmaßstab, Vorhersehbarkeit, Schutzzweck- und Pflichtwidrigkeitszusammenhang)
– BGH, Urt. v. 12.1.2010 – 1 StR 272/09, Rn. 60, 65 f. (fahrlässige Tötung durch Unterlassen; Quasi-Kausalität, im Zweifel für den Angeklagten)
– BGH, Urt. v. 13.11.2008 – 4 StR 252/08 (BGHSt 53, 38), Rn. 17 f. (Verkehrssicherungspflicht für Gefahrenquellen)
– BGH, Urt. v. 17.7.2009 – 5 StR 394/08, Rn. 23 (Garantenstellung für eine Gefahrenquelle)
– BGH, Urt. v. 19.8.2020 – 1 StR 474/19, Rn. 14 (bedingter Vorsatz und bewusste Fahrlässigkeit)

Hinweise: Prüfung nach dem in der Ausbildung üblichen zweistufigen Aufbau (objektive Sorgfaltspflichtverletzung und Vorhersehbarkeit im Tatbestand, subjektive in der Schuld). Die Einordnung des Eigentümers als Überwachergarant folgt der herrschenden Lehre. Nicht behandelt: Vertrauensgrundsatz, eigenverantwortliche Selbstgefährdung, Risikoerhöhungslehre, zivilrechtliche Haftung. Das Unterlassungsdelikt im Einzelnen zeigt die Folge „Unterlassungsdelikt“, den Deliktsaufbau die Folge „Straftat prüfen in 3 Schritten“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Fahrlässigkeit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"Römisch(\s)(eins|zwei|drei)([,:]?)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(2)], srt)
for a, b in [("\nund dreizehn, mit", "\nund 13, mit"), ("im zweiten\nStock", "im 2.\nStock"),
             ("Sechs Wochen nach", "6 Wochen nach")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert "dreizehn" not in srt, "Paragraf als Zahlwort"
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
