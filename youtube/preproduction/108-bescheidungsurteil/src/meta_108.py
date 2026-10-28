"""Nachbearbeitung der Upload-Texte für Folge 108 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Landesrecht-Hinweis (Beispiel Brandenburg),
Rechtsprechung mit Rn., Lizenzzeile; Sprechernamen und Zahlen in den Untertiteln. Keine 16-Länder-Liste (nur Brandenburg geprüft).
Aufruf: python3 meta_108.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Terrasse am Marktplatz abgelehnt"), (T("klage"), "Verpflichtungsklage, Frage und Sachverhalt"),
       (T("spr"), "Spruchreife in Kürze"), (T("wl88"), "Antrag: § 88 VwGO und Bescheidung als Minus"),
       (T("wl113"), "Tenor: § 113 V VwGO"), (T("bekl"), "Tenor des Verpflichtungsurteils"),
       (T("bu"), "Tenor des Bescheidungsurteils"), (T("kosten"), "Kosten: § 155 I 1 VwGO"),
       (T("tipp"), "Klausurtipp: Kostenvergleich"), (T("voll"), "Vollständiger Tenor und Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Bescheidungsurteil oder Verpflichtungsurteil nach § 113 V VwGO: Wann ist die Sache spruchreif, und welche Kostenfolge hat ein zu weiter Antrag (§ 155 I VwGO)?

Der Fall: Herr Haberland führt ein Gasthaus am Marktplatz und beantragt eine Sondernutzungserlaubnis für acht Tische. Die Stadt lehnt ab, um die anderen Wirte vor Konkurrenz zu schützen; der Widerspruch bleibt erfolglos. Er klagt auf Erteilung der Erlaubnis. Über die Erlaubnis entscheidet die Stadt nach Ermessen – und das ist nicht auf null reduziert. Was steht im Tenor, und wer trägt die Kosten? (Übungsfall)

Inhalt:
– Spruchreife in Kürze (ausführlich im Video zur Verpflichtungsklage)
– Antrag und Klagebegehren (§ 88 VwGO): Bescheidung als Minus im Verpflichtungsantrag
– Tenor des Verpflichtungsurteils (§ 113 Abs. 5 Satz 1 VwGO) und des Bescheidungsurteils (§ 113 Abs. 5 Satz 2 VwGO), „Im Übrigen wird die Klage abgewiesen.“
– Kosten bei teilweisem Unterliegen (§ 155 Abs. 1 Satz 1 VwGO), Klausurtipp mit Kostenvergleich
– Vorläufige Vollstreckbarkeit nur wegen der Kosten (§ 167 Abs. 2 VwGO)
– Der vollständige Tenor zum Mitschreiben, Schema, Merksatz

Landesrecht: Das Video nutzt Brandenburg als Beispiel. Dort steht das Ermessen ausdrücklich im Gesetz (§ 18 Abs. 2 Satz 3 BbgStrG), vor der Verpflichtungsklage findet ein Widerspruchsverfahren statt, und die Klage richtet sich gegen die Behörde selbst (§ 78 Abs. 1 Nr. 2 VwGO i. V. m. § 8 Abs. 2 BbgVwGG). Andere Länder regeln Sondernutzung, Vorverfahren und Klagegegner teils anders – bitte im Recht deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Beschl. v. 23.11.2022 – 6 B 22.22, Rn. 19 f. (§ 88 VwGO; Bescheidungsantrag als Minus)
– BVerwG, Beschl. v. 12.5.2020 – 6 B 53.19, Rn. 5 (Aufhebung des Ablehnungsbescheids zur Klarstellung)
– BVerwG, Urt. v. 24.9.2009 – 7 C 2.09, Rn. 67 (teilweises Unterliegen beim Bescheidungsurteil)
– BVerwG, Urt. v. 7.10.2020 – 2 C 5.20, Rn. 56 (Kosten je zur Hälfte)
– OVG NRW, Beschl. v. 1.7.2014 – 11 A 1081/12, Rn. 9 (Ermessen nur aus Gründen mit Bezug zur Straße)
– Tenorbeispiel: OVG NRW, Urt. v. 12.5.2023 – 7 D 328/21.AK

Kapitel:
{kapitel}

Die Tenorformeln und das Schema sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Verpflichtungsklage #Referendariat #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nHaberland:", "\nHerr Haberland:"), ("\nSeeger:", "\nFrau Seeger:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace(" S. 1", " Satz 1")
for alt, neu in (("dreitausend", "3.000"), ("tausendfünfhundert", "1.500"), ("zwei Terrassen", "2 Terrassen"),
                 ("acht Tische", "8 Tische"), ("zehn statt acht", "10 statt 8"), ("zehn statt 8", "10 statt 8"), ("zehn\nstatt 8", "10\nstatt 8"),
                 ("oder hundertfünfundfünfzig", "oder 155"), ("zehnten März", "10. März"),
                 ("fünften Mai", "5. Mai"), ("zweiten Februar", "2. Februar"),
                 ("zweitausendsechsundzwanzig", "2026")):
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
