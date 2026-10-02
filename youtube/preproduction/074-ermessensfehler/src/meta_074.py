"""Nachbearbeitung der Upload-Texte für Folge 074 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Landesrecht-Hinweis (Beispiel NRW), Rechtsprechung
mit Rn., Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_074.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: „Das machen wir grundsätzlich nie.“"), (T("klage"), "Klage, Frage und Sachverhalt"),
       (T("norm"), "Sondernutzung: Erlaubnis nach Ermessen"), (T("geb"), "Gebunden oder Ermessen: muss, kann, soll"),
       (T("rfs"), "Rechtsfolgenseite und Beurteilungsspielraum"), (T("wl40"), "§ 40 VwVfG: Bindung der Behörde"),
       (T("wl114"), "§ 114 Satz 1 VwGO: Was das Gericht prüft"), (T("drei"), "Ermessensnichtgebrauch"),
       (T("f2"), "Ermessensfehlgebrauch"), (T("f3"), "Ermessensüberschreitung, Reduzierung auf null"),
       (T("zurueck"), "Der Fall: Ermessensausfall"), (T("prozess"), "Nachschieben, § 114 Satz 2 VwGO"),
       (T("vk"), "Bescheidungsurteil, § 113 V 2 VwGO"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Ermessensfehler nach § 40 VwVfG und § 114 VwGO: Nichtgebrauch, Fehlgebrauch, Überschreitung – und wann die Behörde ihre Ermessenserwägungen im Prozess noch ergänzen darf.

Der Fall: Frau Kampmann möchte im Sommer vier Tische auf den breiten Gehweg vor ihrem Café stellen und beantragt eine Sondernutzungserlaubnis. Die Stadt lehnt ab: „Das machen wir grundsätzlich nie.“ Frau Kampmann klagt; im Prozess schiebt die Stadt Gründe nach. Was darf das Gericht kontrollieren, und hat die Klage Erfolg? (Übungsfall)

Inhalt:
– Gebundene Entscheidung oder Ermessen: „muss“, „kann“, „soll“; Entschließungs- und Auswahlermessen; Beurteilungsspielraum nur als Ausnahme
– § 40 VwVfG: Ermessen entsprechend dem Zweck der Ermächtigung, gesetzliche Grenzen
– § 114 Satz 1 VwGO: Das Gericht prüft nur Rechtsfehler, nicht die Zweckmäßigkeit
– Ermessensnichtgebrauch (Ermessensausfall), Ermessensfehlgebrauch (sachfremde Erwägungen, Ermessensdefizit), Ermessensüberschreitung (Rechtsfolge außerhalb des Rahmens, Grundrechte, Verhältnismäßigkeit)
– Ermessensreduzierung auf null
– Begründung von Ermessensentscheidungen, § 39 Abs. 1 Satz 3 VwVfG
– Nachschieben, § 114 Satz 2 VwGO: nur Ergänzung, keine erstmalige Ermessensausübung
– Verpflichtungsklage und Bescheidungsurteil, § 113 Abs. 5 Satz 2 VwGO
– Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel. Dort ist die Sondernutzung in § 18 StrWG NRW geregelt; über die Erlaubnis entscheidet die Straßenbaubehörde nach Ermessen, und zwar nur aus Gründen mit Bezug zur Straße (OVG NRW). Die anderen Länder regeln die Sondernutzung in ihren eigenen Straßengesetzen (z. B. Art. 18 BayStrWG) – bitte im Recht deines Landes nachschlagen. § 40 VwVfG gilt über die gleichlautenden Landesverwaltungsverfahrensgesetze.

Rechtsprechung:
– BVerwG, Urt. v. 24.2.2021 – 8 C 25.19, Rn. 13 (Ermessensausfall nicht durch Nachschieben heilbar)
– BVerwG, Urt. v. 13.12.2011 – 1 C 14.10, Rn. 9 (§ 114 Satz 2 VwGO: Ergänzung, keine erstmalige Ausübung)
– BVerwG, Urt. v. 5.9.2006 – 1 C 20.05, Rn. 17–22 (Ermessen nicht ausgeübt)
– BVerwG, Beschl. v. 23.1.2014 – 1 B 16.13, Rn. 4 (Ermessensreduzierung)
– BVerwG, Beschl. v. 3.12.2009 – 9 B 79.09, Rn. 2 (Soll-Vorschriften)
– BVerwG, Beschl. v. 8.11.2016 – 3 B 11.16, Rn. 8 (unbestimmte Rechtsbegriffe, Beurteilungsspielraum)
– OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 29, 58–62, 67 und Beschl. v. 1.7.2014 – 11 A 1081/12, Rn. 9, 11 (Sondernutzungserlaubnis, Ermessen, straßenbezogene Gründe)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Ermessensfehler #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nKampmann:", "\nFrau Kampmann:"), ("\nHornung:", "\nHerr Hornung:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("Hilft ihr S. 2?", "Hilft ihr Satz 2?")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
