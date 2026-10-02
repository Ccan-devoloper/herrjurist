"""Nachbearbeitung der Upload-Texte für Folge 077 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), fachlich korrigierte Beschreibung (Planbeschreibung „bundesweit“ ungenau, siehe
RECHTSSTAND.md), Sprechernamen und Paragrafen-Umbruch in den Untertiteln, Lizenzzeile. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_077.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Geburtstag im Park, die Polizei kommt"), (T("zurueck"), "Fall: Der Platzverweis – auf welcher Grundlage?"),
       (T("aufbau"), "Aufbau der Prüfung und Landesrecht"), (T("egl"), "Ermächtigungsgrundlage: die Reihenfolge"),
       (T("wl8"), "Generalklausel, § 8 PolG NRW"), (T("warum"), "Warum zuerst die Standardmaßnahme?"),
       (T("wl34"), "Platzverweis, § 34 PolG NRW"), (T("formell"), "Formelle Rechtmäßigkeit"),
       (T("mat"), "Tatbestand: konkrete Gefahr"), (T("owi"), "Lärm: § 117 OWiG, § 9 LImschG NRW"),
       (T("adr"), "Adressat: Verhaltensstörer"), (T("rf"), "Rechtsfolge: Ermessen und Verhältnismäßigkeit"),
       (T("grenze"), "Zeitlich und räumlich begrenzt"), (T("erg"), "Ergebnis und Rechtsschutz"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Polizeirecht Schema (Beispiel NRW): Platzverweis im Park – Ermächtigungsgrundlage (Spezialgesetz, Standardmaßnahme vor Generalklausel, § 34 I und § 8 I PolG NRW), formelle und materielle Rechtmäßigkeit, Verhältnismäßigkeit.

Der Fall: Herr Schröder feiert nachts mit zwei Freunden im Stadtpark Geburtstag, die Musikbox ist laut. Eine Anwohnerin ruft die Polizei. Erst bittet die Polizistin um Ruhe, eine Stunde später ist die Box wieder voll aufgedreht – Platzverweis bis 6 Uhr. „Auf welcher Grundlage eigentlich?“ (Übungsfall)

Inhalt:
– Prüfungsaufbau: Ermächtigungsgrundlage, formelle und materielle Rechtmäßigkeit
– Reihenfolge: Spezialgesetz (hier keine Versammlung, § 2 Abs. 3 VersG NRW), Standardmaßnahme, Generalklausel
– Generalklausel § 8 Abs. 1 PolG NRW im Wortlaut: „soweit nicht die §§ 9 bis 46 die Befugnisse der Polizei besonders regeln“
– Platzverweisung § 34 Abs. 1 Satz 1 PolG NRW im Wortlaut
– Formell: Zuständigkeit (§ 1 Abs. 1 Satz 3 PolG NRW; Ordnungsamt seit 1.7.2026 mit eigener Platzverweisung, § 24o OBG NRW), Anhörung (§ 28 Abs. 2 Nr. 1 VwVfG NRW), Form (§ 37 Abs. 2 VwVfG NRW)
– Materiell: konkrete Gefahr für die öffentliche Sicherheit, Lärm (§ 117 Abs. 1 OWiG, § 9 Abs. 1 LImschG NRW), Verhaltensstörer (§ 4 Abs. 1 PolG NRW), Ermessen und Verhältnismäßigkeit (§§ 2, 3 PolG NRW), zeitliche und räumliche Begrenzung, Abgrenzung zum Aufenthaltsverbot (§ 34 Abs. 2 PolG NRW)
– Rechtsschutz: Fortsetzungsfeststellungsklage (§ 113 Abs. 1 Satz 4 VwGO analog) – mehr im Video zu den Klagearten
– Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel (PolG NRW ab 13.12.2025, OBG NRW ab 1.7.2026). Die anderen Länder haben ähnliche Regeln, oft unter anderer Nummer – bitte im Polizeigesetz deines Landes nachschlagen.

Rechtsprechung:
– OVG NRW, Urt. v. 27.9.2021 – 5 A 2807/19, Rn. 30, 67, 70, 77, 82 f. (Platzverweis für ein ganzes Stadtgebiet; konkrete Gefahr; Fortsetzungsfeststellungsklage)
– OVG NRW, Beschl. v. 9.1.2023 – 5 B 14/23, Rn. 20 (Dauer eines Platzverweises)
– OVG NRW, Beschl. v. 2.7.2020 – 15 A 2100/18, Rn. 72 (öffentliche Sicherheit)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Polizeirecht #Prüfungsschema #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nSchröder:", "\nHerr Schröder:"), ("\nGötz:", "\nFrau Götz:"), ("\nKrämer:", "\nFrau Krämer:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("zweiundzwanzig", "22").replace("bis sechs Uhr", "bis 6 Uhr").replace("um sechs Uhr", "um 6 Uhr")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
