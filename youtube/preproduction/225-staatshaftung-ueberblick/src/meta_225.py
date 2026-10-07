"""Nachbearbeitung der Upload-Texte für Folge 225 (nach meta_213.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen (nur am Landesportal geprüfte
Landesnormen), Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel: Sprechernamen.
Aufruf: python3 meta_225.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Zaun, Auto und Laden"),
       (T("ebenen"), "Primärebene und Sekundärebene"),
       (T("ah"), "Amtshaftung: § 839 BGB und Art. 34 GG im Wortlaut"),
       (T("s1"), "Prüfschema Amtshaftung am Fall Zaun"),
       (T("ab"), "Abschleppen: Anfechtung und Folgenbeseitigung"),
       (T("taxi"), "Entschädigung für rechtswidrige Maßnahmen, Länder-Overlay"),
       (T("la"), "Ist das eine Enteignung? Art. 14 Abs. 3 GG"),
       (T("auf"), "Enteignungsgleicher und enteignender Eingriff"),
       (T("anl"), "Anliegerentschädigung bei Straßenarbeiten"),
       (T("ueb"), "Welcher Anspruch wann?"),
       (T("rw"), "Rechtsweg"),
       (T("tipp"), "Klausurtipp: Primärebene zuerst"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Staatshaftungsrecht Überblick: Folgenbeseitigung, Amtshaftung (§ 839 BGB, Art. 34 GG), enteignungsgleicher und enteignender Eingriff, Aufopferung und Entschädigung nach Landesrecht – welcher Anspruch wann passt.

Der Fall: Die Stadt baut die Straße vor Herrn Bergners Fahrradladen um. Ein Bagger des Bauhofs beschädigt seinen Gartenzaun, sein Auto wird abgeschleppt, obwohl es außerhalb des Haltverbots stand, und die Baustelle versperrt fünf Monate lang den Weg in seinen Laden. Welche Ansprüche hat er gegen die Stadt?

Inhalt:
– Primärebene (Abwehr der Maßnahme) und Sekundärebene (Schadensersatz, Entschädigung)
– Amtshaftung: § 839 Abs. 1 S. 1 BGB und Art. 34 S. 1 GG im Wortlaut; Prüfschema: Beamter im haftungsrechtlichen Sinn (auch Angestellte und private Helfer), Amtspflichtverletzung, Drittbezogenheit, Verschulden, Schaden, kein Ausschluss (§ 839 Abs. 1 S. 2, Abs. 3 BGB)
– Abschleppen: Kosten nur für rechtmäßiges Abschleppen; Anfechtung des Kostenbescheids und Rückzahlung (§ 113 Abs. 1 S. 2 VwGO, Folgenbeseitigung); Entschädigung für rechtswidrige Maßnahmen ohne Verschulden (Beispiel § 39 Abs. 1 b OBG NRW)
– Laden: keine Enteignung (Art. 14 Abs. 3 GG, Naßauskiesung); Aufopferungsgedanke; enteignungsgleicher und enteignender Eingriff; Anliegerentschädigung bei Straßenarbeiten (Beispiel § 20 Abs. 6 StrWG NRW)
– Übersicht „Welcher Anspruch wann?“, Rechtsweg (Art. 34 S. 3 GG, § 40 Abs. 2 VwGO), Klausurtipp, Merksatz

Landesrecht im Ländervergleich (im Video als Overlay; am amtlichen Landesportal geprüft, Abruf 7.10.2026):
– Nordrhein-Westfalen: Entschädigung bei rechtswidrigen Maßnahmen § 39 Abs. 1 Buchst. b OBG NRW (für die Polizei über § 67 PolG NRW); Anliegerentschädigung bei Straßenarbeiten § 20 Abs. 6 StrWG NRW; Straßenbau als hoheitliche Aufgabe § 9a Abs. 1 StrWG NRW
– Brandenburg: § 38 Abs. 1 Buchst. b OBG (für die Polizei über § 70 BbgPolG); Anliegerentschädigung § 22 Abs. 6 BbgStrG
– Sachsen: § 41 Abs. 1 Nr. 2 SächsPBG (Polizeibehörden), § 47 Abs. 1 Nr. 2 SächsPVDG (Polizeivollzugsdienst)
– Bundesstraßen: § 8a Abs. 5 FStrG
Die übrigen Länder haben eigene Regeln unter eigenen Nummern; bitte im eigenen Polizei-, Ordnungs- bzw. Straßengesetz nachschlagen.

Rechtsprechung:
– BVerfG, Beschl. v. 15.7.1981 – 1 BvL 77/78 (Naßauskiesung), BVerfGE 58, 300 (324, 330 f.)
– BGH, Urt. v. 18.2.2014 – VI ZR 383/12, Rn. 5–7 (Abschleppunternehmer als Beamter im haftungsrechtlichen Sinn)
– BGH, Urt. v. 4.7.2013 – III ZR 250/12, Rn. 13 (Amtspflicht, Eigentum nicht zu beschädigen)
– BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 11 (Kosten nur bei rechtmäßigem Abschleppen)
– BVerwG, Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14 (§ 113 Abs. 1 S. 2 VwGO und Folgenbeseitigung)
– BGH, Urt. v. 19.1.2006 – III ZR 82/05, Rn. 9 (§ 39 Abs. 1 b OBG NRW verschuldensunabhängig)
– BGH, Urt. v. 7.9.2017 – III ZR 71/17, Rn. 16 (Aufopferung, § 75 EinlALR)
– BGH, Urt. v. 15.12.2016 – III ZR 387/14, Rn. 20 f. (enteignungsgleicher Eingriff)
– BGH, Urt. v. 17.3.2022 – III ZR 79/21, Rn. 56–58 (enteignender Eingriff)

Hinweise: Fall und Personen sind erfunden; keine echte Stadt. Nordrhein-Westfalen ist das Beispielland. Den Folgenbeseitigungsanspruch erklärt Folge 172 ausführlich.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Staatshaftungsrecht #Amtshaftung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n +", "\n", srt)
for a_, b_ in [("zwölfhundert Euro", "1.200 Euro"), ("dreißig Euro", "30 Euro"), ("VWGO", "VwGO")]:
    srt = srt.replace(a_, b_)
for alt, neu in [("\nBergner: ", "\nHerr Bergner: "), ("\nWilmsen: ", "\nFrau Wilmsen: ")]:
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert not re.search(r"hundert|Paragraf|zwölf", srt), [l for l in srt.split("\n") if re.search(r"hundert|Paragraf|zwölf", l)]
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
