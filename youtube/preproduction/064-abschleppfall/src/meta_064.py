"""Nachbearbeitung der Upload-Texte für Folge 064 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), fachlich korrigierte Beschreibung (Planbeschreibung „bundesweit“ ungenau, siehe
RECHTSSTAND.md), Sprechernamen und Paragrafen-Umbruch in den Untertiteln, Lizenzzeile. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_064.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Nur fünf Minuten auf dem Behindertenparkplatz"), (T("meier"), "Fall: Das Ordnungsamt lässt abschleppen"),
       (T("zurueck"), "Fall: Das Auto hängt am Haken"), (T("bescheid"), "Kostenbescheid, Frage und Sachverhalt"),
       (T("ebenen"), "Drei Ebenen und Landesrecht"), (T("egl"), "Der Kostenbescheid: Grundlage, formell, Konnexität"),
       (T("gva"), "Das Schild: Zeichen 314 mit Zusatzzeichen"), (T("va"), "Allgemeinverfügung, Sichtbarkeit, Wegfahrgebot"),
       (T("ev"), "Ersatzvornahme, § 59 VwVG NRW"), (T("wege"), "Gestreckt oder sofort? § 55 VwVG NRW"),
       (T("vhm"), "Verhältnismäßigkeit: erforderlich, Wartezeit"), (T("angem"), "Angemessen? Gegenfälle"),
       (T("erg"), "Ergebnis und Kosten"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Abschleppfall (Beispiel NRW): Fünf Minuten auf dem Behindertenparkplatz – Verkehrszeichen als Allgemeinverfügung, Wegfahrgebot (§ 80 II 1 Nr. 2 VwGO analog), Ersatzvornahme im Sofortvollzug, Verhältnismäßigkeit und Kostenbescheid.

Der Fall: Frau Kaiser parkt „nur fünf Minuten“ ohne Parkausweis auf einem Parkplatz für schwerbehinderte Menschen vor der Apotheke. Das Ordnungsamt findet niemanden am Wagen und lässt abschleppen. Nach zehn Minuten hängt ihr Auto am Haken – und eine Woche später kommt ein Kostenbescheid über 250 €. Muss sie zahlen? (Übungsfall)

Inhalt:
– Drei Ebenen: Verkehrszeichen, Abschleppen, Kosten
– Kostenbescheid: § 77 Abs. 1 VwVG NRW mit § 15 Abs. 1 Nr. 7, § 20 Abs. 2 Satz 2 Nr. 7 VO VwVG NRW; Kosten nur bei rechtmäßigem Abschleppen
– Das Schild: Zeichen 314 mit Zusatzzeichen (Anlage 3 StVO, lfd. Nr. 7) und § 12 Abs. 2 StVO
– Allgemeinverfügung (§ 35 Satz 2 VwVfG), Sichtbarkeitsgrundsatz, Wegfahrgebot sofort vollziehbar (§ 80 Abs. 2 Satz 1 Nr. 2 VwGO analog)
– Ersatzvornahme (§ 59 Abs. 1 VwVG NRW): gestrecktes Verfahren oder sofortiger Vollzug (§ 55 Abs. 2, § 63 Abs. 1 Satz 5, § 64 Satz 2 VwVG NRW)
– Verhältnismäßigkeit: Erreichbarkeit der Fahrerin, keine feste Wartezeit, Behindertenparkplatz, Gegenfälle
– Kostenpflicht (§ 17 Abs. 1 OBG NRW), Klausurtipp (Sicherstellung, § 24w OBG NRW), Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel (VwVG NRW ab 1.4.2025, VO VwVG NRW ab 1.1.2026, OBG NRW ab 1.7.2026). Die anderen Länder haben ähnliche Regeln, oft unter anderer Nummer; manche lösen das Abschleppen über die unmittelbare Ausführung – bitte im Gesetz deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 9.4.2014 – 3 C 5.13, Rn. 12, 16 f. (Wartezeit, Erreichbarkeit, Behinderung)
– BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 16, 19 (Allgemeinverfügung, Sichtbarkeitsgrundsatz)
– BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 11, 14 (Kosten nur bei rechtmäßiger Maßnahme; Wegfahrgebot)
– OVG NRW, Urt. v. 20.8.2020 – 5 A 2289/18, Rn. 30 f. (Ersatzvornahme im Sofortvollzug)
– OVG NRW, Beschl. v. 21.3.2000 – 5 A 2339/99, Rn. 4, 6, 12 (Behindertenparkplatz: Abschleppen auch ohne konkrete Behinderung)
– VG Münster, Urt. v. 14.11.2011 – 1 K 605/10, Rn. 17–23; VG Düsseldorf, Urt. v. 28.3.2017 – 14 K 6945/16, Rn. 17–26

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Abschleppfall #Polizeirecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nKaiser:", "\nFrau Kaiser:"), ("\nMeier:", "\nHerr Meier:"), ("\nBecker:", "\nHerr Becker:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
