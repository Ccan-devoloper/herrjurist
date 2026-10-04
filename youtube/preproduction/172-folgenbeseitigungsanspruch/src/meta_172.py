"""Nachbearbeitung der Upload-Texte für Folge 172 (Kopie von meta_170.py, angepasst) nach tools/youtube_metadaten.py (nichts
dort geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung, Hinweisen und
Lizenzzeile; Untertitel in Schriftform (Ziffern, „I.“ statt „Römisch eins“, VwGO, Sprecher „Herr Wernicke“).
Aufruf: python3 meta_172.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die Gemeinde pflastert den Vorgarten mit"),
       (T("einord"), "Einordnung: § 1004 BGB oder Folgenbeseitigung?"),
       (T("rg"), "I. Rechtsgrundlage: ungeschrieben, Grundrechte und Rechtsstaatsprinzip"),
       (T("w20"), "Art. 20 Abs. 3 GG und Art. 14 Abs. 1 GG im Wortlaut"),
       (T("w113"), "§ 113 Abs. 1 Satz 2 VwGO und der Herleitungsstreit"),
       (T("vor"), "II. Die vier Voraussetzungen"),
       (T("a1"), "1. und 2. Hoheitlicher Eingriff (Realakt) in das Eigentum"),
       (T("c1"), "3. Rechtswidriger Zustand – der Radweg-Fall des BVerwG"),
       (T("d1"), "4. Wiederherstellung möglich und zumutbar"),
       (T("rf"), "III. Rechtsfolge: Status quo ante, kein Schadensersatz"),
       (T("w34"), "Kontrast: Amtshaftung (Art. 34 GG, § 839 BGB)"),
       (T("mv"), "Mitverschulden (§ 254 BGB)"),
       (T("proz"), "Prozessuales: allgemeine Leistungsklage"),
       (T("loes"), "Lösung"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Folgenbeseitigungsanspruch (Art. 20 III GG, § 113 I 2 VwGO): Was tun, wenn die Gemeinde deinen Vorgarten mitpflastert? Voraussetzungen und Grenzen.

Der Fall: Beim Ausbau des Gehwegs pflastern die Bauarbeiter der Gemeinde versehentlich einen 30 cm breiten Streifen von Ottilies Vorgarten mit. Wo Rosen standen, liegt jetzt Pflaster. Herr Wernicke vom Bauamt bietet Geld an – Ottilie will ihren Vorgarten zurück. Kann sie verlangen, dass die Gemeinde das Pflaster entfernt und den Vorgarten wiederherstellt?

Inhalt:
– Einordnung: unter Privaten § 1004 BGB, gegenüber der hoheitlich handelnden Gemeinde der Folgenbeseitigungsanspruch
– I. Rechtsgrundlage: ungeschrieben, in ständiger Rechtsprechung anerkannt; verankert in den Grundrechten und im Rechtsstaatsprinzip; Art. 20 Abs. 3 GG, Art. 14 Abs. 1 Satz 1 GG und § 113 Abs. 1 Satz 2 VwGO im Wortlaut; § 113 Abs. 1 Satz 2 VwGO als prozessuales Mittel
– II. Voraussetzungen: 1. hoheitlicher Eingriff (Realakt, schlicht-hoheitliches Handeln), 2. in ein subjektives Recht (Eigentum), 3. rechtswidriger Zustand, der andauert (keine Duldungspflicht; Legalisierung), 4. Wiederherstellung tatsächlich und rechtlich möglich und zumutbar
– III. Rechtsfolge: Wiederherstellung des Status quo ante, kein Schadensersatz; Kontrast Amtshaftung (Art. 34 Satz 1 GG im Wortlaut, § 839 BGB)
– Mitverschulden nach dem Rechtsgedanken des § 254 BGB
– Prozessuales: Verwaltungsrechtsweg (§ 40 Abs. 1 VwGO), allgemeine Leistungsklage
– Lösung, Klausurtipp, Klausurschema, Merksatz

Normen: Art. 14 Abs. 1, Art. 20 Abs. 3, Art. 34 GG; § 40 Abs. 1, § 113 Abs. 1 Satz 2 VwGO; §§ 254, 839, 1004 BGB

Rechtsprechung (Volltexte bverwg.de): BVerwG, Urt. v. 19.9.2019 – 9 C 5.19, Rn. 12–15 (Radweg auf Privatgrundstück); Urt. v. 19.2.2015 – 1 C 13.14, Rn. 24 f.; Urt. v. 29.7.2015 – 6 C 35.14, Rn. 8; Beschl. v. 27.5.2015 – 7 B 14.15, Rn. 8 f.; Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14; Beschl. v. 12.7.2013 – 9 B 12.13, Rn. 4 f.; Urt. v. 28.1.2010 – 3 C 17.09, Rn. 28; Urt. v. 27.2.2019 – 6 C 1.18, Rn. 14

Hinweise: Fall und Personen sind erfunden; keine echte Gemeinde. Den zivilrechtlichen Beseitigungsanspruch aus § 1004 BGB erklärt Folge 142, die Anfechtungsklage und § 113 VwGO Folge 069. Schadensersatz wegen der zerstörten Rosen wäre eine Frage der Amtshaftung (§ 839 BGB, Art. 34 GG) vor den ordentlichen Gerichten; sie ist nicht Gegenstand des Videos.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Folgenbeseitigungsanspruch #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
ers = [("Otti-lie", "Ottilie"), ("dreißig Zentimeter", "30 cm"), ("VWGO", "VwGO"), ("Römisch eins:", "I."), ("Römisch zwei:", "II."),
       ("Römisch drei:", "III."), ("\nWernicke: ", "\nHerr Wernicke: ")]
for a, b in ers:
    srt = srt.replace(a, b)
assert "Otti-lie" not in srt and "Römisch" not in srt and "VWGO" not in srt and "dreißig" not in srt, [l for l in srt.split("\n") if "Römisch" in l]
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
