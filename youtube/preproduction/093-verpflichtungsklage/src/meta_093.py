"""Nachbearbeitung der Upload-Texte für Folge 093 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Landesrecht-Hinweis (Beispiel NRW), Rechtsprechung
mit Rn., Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_093.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die Stadt lehnt die Tische vor dem Café ab"), (T("klage"), "Klage, Frage und Sachverhalt"),
       (T("aufbau"), "Aufbau und Verwaltungsrechtsweg"), (T("wl42"), "Statthaftigkeit: Versagungsgegenklage, § 42 I Alt. 2"),
       (T("kb"), "Klagebefugnis: möglicher Anspruch"), (T("vv"), "Vorverfahren und Klagefrist"),
       (T("kg"), "Klagegegner"), (T("wl113"), "Begründetheit: § 113 V VwGO"),
       (T("anspr"), "Anspruch und maßgeblicher Zeitpunkt"), (T("agl"), "Anspruchsgrundlage bis Rechtsfolge"),
       (T("fehler"), "Ermessensfehler: falscher Sachverhalt"), (T("spruch"), "Spruchreife"),
       (T("fall2"), "Im Fall: Bescheidungsurteil"), (T("tenor"), "Tenor: Verpflichtung oder Bescheidung"),
       (T("urteil"), "Das Urteil"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verpflichtungsklage Schema (§ 42 I Alt. 2, § 113 V VwGO): Versagungsgegenklage, Klagebefugnis, Spruchreife und Bescheidungsurteil verständlich erklärt.

Der Fall: Herr Feldmann möchte im Sommer sechs Tische auf den Gehweg vor seinem Café stellen. Die Stadt lehnt ab: Der Gehweg sei zu schmal, Fußgänger müssten auf die Fahrbahn ausweichen. Tatsächlich ist der Gehweg fünf Meter breit. Herr Feldmann klagt auf die Erlaubnis. Bekommt er sie – oder nur eine neue Entscheidung? (Übungsfall)

Inhalt:
– A. Zulässigkeit: Verwaltungsrechtsweg; Statthaftigkeit nach § 42 Abs. 1 Alt. 2 VwGO (Versagungsgegenklage, Untätigkeitsklage § 75 VwGO); Klagebefugnis aus einem möglichen Anspruch; Vorverfahren (§ 68 Abs. 2 VwGO); Klagefrist (§ 74 Abs. 2 VwGO); Klagegegner (§ 78 VwGO)
– B. Begründetheit nach § 113 Abs. 5 VwGO, anspruchsorientiert: maßgeblicher Zeitpunkt, Anspruchsgrundlage, formelle und materielle Voraussetzungen, Rechtsfolge (gebunden oder Ermessen)
– Ermessensfehler durch einen falschen Sachverhalt
– Spruchreife: Verpflichtungsurteil (§ 113 Abs. 5 Satz 1) oder Bescheidungsurteil (§ 113 Abs. 5 Satz 2)
– Tenorformeln für die Klausur, Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel. Dort entfällt das Vorverfahren auch vor der Verpflichtungsklage in der Regel (§ 110 Abs. 1 Satz 2 JustG NRW), und die Sondernutzung ist in § 18 StrWG NRW geregelt; über die Erlaubnis entscheidet die Straßenbaubehörde nach Ermessen. Die anderen Länder regeln Vorverfahren und Sondernutzung teils anders und in ihren eigenen Gesetzen – bitte im Recht deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 11.7.2018 – 1 C 18.17, Rn. 28, 36 (Pflicht des Gerichts, die Sache spruchreif zu machen; Grenzen bei Ermessen)
– BVerwG, Beschl. v. 23.1.2014 – 1 B 16.13, Rn. 4 (Ermessensreduzierung: abschließende Entscheidung)
– BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 18 (Anspruch als Streitgegenstand, maßgeblicher Zeitpunkt)
– BVerwG, Urt. v. 21.11.2006 – 1 C 10.06, Rn. 16 (Versagungsgegenklage)
– BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9 (Möglichkeit der Rechtsverletzung)
– OVG NRW, Urt. v. 7.4.2017 – 11 A 2068/14, Rn. 49, 56, 57, 90 (Sondernutzungserlaubnis, unzutreffende Sachverhaltsannahme)
– OVG NRW, Urt. v. 12.3.2021 – 11 A 114/20, Rn. 29, 58–62, 67 (Ermessen, Anspruch auf fehlerfreie Bescheidung, straßenbezogene Gründe)

Kapitel:
{kapitel}

Die Prüfungsschemata und Tenorformeln sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Verpflichtungsklage #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nFeldmann:", "\nHerr Feldmann:"), ("\nSiebert:", "\nFrau Siebert:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("nach S. 1.", "nach Satz 1.").replace("nach S. 2.", "nach Satz 2.")
assert not re.search(r"§\n", srt)
assert "S. 1" not in srt and "S. 2" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
