"""Nachbearbeitung der Upload-Texte für Folge 102 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Landesrecht-Hinweis (Beispiel NRW), Rechtsprechung
mit Rn., Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_102.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Abwassergebühr 2.400 € statt 1.500 €"), (T("klage"), "Klage, Frage und Sachverhalt"),
       (T("vv"), "Vorfrage: Widerspruchsverfahren (Beispiel NRW)"), (T("wl79"), "Gegenstand: § 79 I Nr. 1 VwGO"),
       (T("wl113"), "Umfang: „soweit“, § 113 I 1 VwGO"), (T("t2"), "Tenor: aufheben, soweit – im Übrigen abweisen"),
       (T("tipp"), "Klausurtipp: § 113 II VwGO"), (T("kosten"), "Kosten: § 155 I 1 VwGO"),
       (T("vollstr"), "Vorläufige Vollstreckbarkeit"), (T("ber"), "Berufung"), (T("voll"), "Der vollständige Tenor und das Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anfechtungsurteil Tenor nach § 113 I 1 VwGO: Wie du ganze und teilweise Aufhebung formulierst und wann der Widerspruchsbescheid (§ 79 VwGO) einbezogen wird.

Der Fall: Frau Rehbein betreibt eine Wäscherei. Die Stadt setzt die Abwassergebühr auf 2.400 Euro fest und rechnet mit 400 Kubikmetern – der Zähler zeigt nur 250. Der Widerspruch wird zurückgewiesen, Frau Rehbein klagt auf Aufhebung des ganzen Bescheids. Rechtswidrig sind nur 900 Euro. Wie lautet der Tenor? (Übungsfall)

Inhalt:
– Gegenstand der Anfechtungsklage: der Bescheid „in Gestalt des Widerspruchsbescheids“ (§ 79 Abs. 1 Nr. 1 VwGO); isolierte Anfechtung des Widerspruchsbescheids (§ 79 Abs. 1 Nr. 2, Abs. 2 VwGO)
– Umfang: „soweit“ (§ 113 Abs. 1 Satz 1 VwGO), Teilbarkeit, Teilaufhebung und „Im Übrigen wird die Klage abgewiesen.“
– Klausurtipp: Änderung des Betrags nach § 113 Abs. 2 VwGO
– Kosten bei teilweisem Obsiegen (§ 155 Abs. 1 Satz 1 VwGO): Quote 5/8 zu 3/8
– Vorläufige Vollstreckbarkeit nur wegen der Kosten (§ 167 Abs. 2 VwGO, §§ 708 Nr. 11, 711 ZPO); Berufungszulassung (§ 124a Abs. 1 VwGO)
– Der vollständige Tenor zum Mitschreiben, Schema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel. Dort entfällt das Vorverfahren vor der Anfechtungsklage in der Regel (§ 110 Abs. 1 JustG NRW), nicht aber bei Bescheiden auf Grundlage des Kommunalabgabengesetzes (§ 110 Abs. 2 Satz 1 Nr. 6 JustG NRW); über den Widerspruch entscheidet dann die erlassende Behörde (§ 111 Satz 1 JustG NRW). Die anderen Länder regeln das Vorverfahren teils anders – bitte im Recht deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Beschl. v. 10.10.2023 – 9 B 18.23, Rn. 7 (Teilaufhebung, Teilbarkeit eines Gebührenbescheids)
– BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18 (Rechtsverletzung des Adressaten, § 113 Abs. 1 Satz 1 VwGO)
– Tenorbeispiele: OVG NRW, Urt. v. 17.5.2022 – 9 A 1019/20; VG Gelsenkirchen, Urt. v. 19.8.2025 – 15 K 2823/21; OVG NRW, Urt. v. 3.12.2012 – 9 A 2646/11; VG Düsseldorf, Urt. v. 30.3.2023 – 17 K 3488/22

Kapitel:
{kapitel}

Die Tenorformeln und das Schema sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Anfechtungsklage #Referendariat #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nRehbein:", "\nFrau Rehbein:"), ("\nZimmermann:", "\nHerr Zimmermann:"), ("\nRichter:", "\nDer Richter:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace(" S. 1", " Satz 1").replace("Nr. 3 oder vier", "Nr. 3 oder 4")
for alt, neu in (("zweitausendvierhundert", "2.400"), ("Tausendfünfhundert", "1.500"), ("tausendfünfhundert", "1.500"),
                 ("zweihundertfünfzig", "250"), ("vierhundert", "400"), ("neunhundert", "900"), ("sechs Euro", "6 Euro"),
                 ("hundertzehn Prozent", "110 %"), ("hundertzehn\nProzent", "110\n%"), ("fünf Achteln", "5/8"),
                 ("drei Achteln", "3/8"), ("fünf Achtel", "5/8"), ("oder hundertfünfundfünfzig", "oder 155"),
                 ("zweiten März", "2. März"), ("vierten Mai", "4. Mai")):
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n", srt)
assert "S. 1" not in srt and "oder vier" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
