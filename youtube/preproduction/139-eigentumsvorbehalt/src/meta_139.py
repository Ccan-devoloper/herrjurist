"""Nachbearbeitung der Upload-Texte für Folge 139 (Kopie von meta_116.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Sprecherbezeichnung und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_139.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das Sofa auf Raten"),
       (T("plan"), "Eigentumsvorbehalt: drei Schritte"),
       (T("tr1"), "1. Trennungsprinzip: Kaufvertrag und Übereignung"),
       (T("w449"), "§ 449 Abs. 1 BGB im Wortlaut"),
       (T("w158"), "Aufschiebende Bedingung, § 158 Abs. 1 BGB"),
       (T("anw"), "2. Anwartschaftsrecht"),
       (T("her"), "3. Herausgabe: § 985 BGB und Recht zum Besitz (§ 986 BGB)"),
       (T("w4492"), "§ 449 Abs. 2 BGB: erst nach dem Rücktritt"),
       (T("rt1"), "Rücktritt, Teilzahlungsgeschäft, Rückabwicklung"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: die letzte Rate"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Eigentumsvorbehalt nach §§ 449, 929, 158 I BGB: Wie wird er konstruiert und wann darf der Händler das auf Raten gekaufte Sofa zurückholen?

Der Fall: Sonja kauft in einem Möbelhaus ein Sofa für 2.400 Euro, zahlbar in 12 Monatsraten zu je 200 Euro. Im Kaufvertrag steht: Bis zur letzten Rate bleibt das Sofa Eigentum des Möbelhauses. Das Sofa wird geliefert. Nach fünf Raten zahlt Sonja nicht mehr, und der Verkäufer kündigt am Telefon an, das Sofa am Montag abzuholen. Eine Frist hat das Möbelhaus nicht gesetzt. Wem gehört das Sofa – und darf das Möbelhaus es einfach abholen?

Inhalt:
– 1. Trennungsprinzip: Kaufvertrag (§ 433 BGB) unbedingt, Übereignung (§ 929 S. 1 BGB) aufschiebend bedingt
– § 449 Abs. 1 und § 158 Abs. 1 BGB im Wortlaut: Eigentum erst mit vollständiger Zahlung
– 2. Anwartschaftsrecht der Käuferin
– 3. Herausgabe: § 985 BGB, Recht zum Besitz aus dem Kaufvertrag (§ 986 Abs. 1 BGB)
– § 449 Abs. 2 BGB im Wortlaut: Herausgabe erst nach dem Rücktritt
– Rücktritt nach § 323 BGB mit Fristsetzung; Teilzahlungsgeschäft (§§ 506, 508 BGB) als offene Frage; Rückabwicklung nach §§ 346 ff. BGB
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 158 I, 433, 449, 929 S. 1, 985, 986 I BGB; §§ 323, 346, 506, 508 BGB

Rechtsprechung:
– BGH, Urt. v. 8.5.2014 – IX ZR 128/12, Rn. 10 f. (Eigentumsübergang erst mit vollständiger Zahlung; Recht zum Besitz des Vorbehaltskäufers, solange es nicht zum Rücktritt gekommen ist)
– BGH, Urt. v. 27.6.2025 – V ZR 143/24, Rn. 16 (Anwartschaftsrecht: weitgehend gesicherte Rechtsposition, dem Volleigentum wesensähnlich)
– BGH, Beschl. v. 24.1.2019 – IX ZR 110/17, Rn. 65 (Herausgabe nach § 985 BGB, sofern der Vorbehaltsverkäufer wirksam zurückgetreten ist)

Hinweise: Ob beim Ratenkauf zusätzlich die Verbraucherregeln zum entgeltlichen Teilzahlungsgeschäft gelten (§§ 506 ff. BGB), hängt vom Einzelfall ab; dann gelten für den Rücktritt wegen Zahlungsverzugs die strengeren Voraussetzungen der §§ 508, 498 BGB. Die Grundlagen der Übereignung erklärt Folge 80, den Herausgabeanspruch Folge 92, den Rücktritt Folge 116. Das Klausurschema ist eine Klausurkonvention.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Eigentumsvorbehalt #Sachenrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nSchuster: ", "\nHerr Schuster: ")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
