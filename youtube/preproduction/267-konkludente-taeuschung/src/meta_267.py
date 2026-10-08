"""Nachbearbeitung der Upload-Texte für Folge 267 (nach meta_264.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Rechtsprechung mit
Fundstellen, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Beträge und Zahlen in Ziffern).
Aufruf: python3 meta_267.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall 1: das Drei-Gänge-Menü ohne Geld"),
       (T("ortrud"), "Fall 2: ein Angebot, das wie eine Rechnung aussieht"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("p263"), "§ 263 Abs. 1 StGB: die Täuschung"),
       (T("drei"), "Drei Wege der Täuschung und der Maßstab"),
       (T("f1"), "Fall 1: Bestellung als konkludente Erklärung"),
       (T("zech"), "Abwandlung: Entschluss erst nach dem Essen"),
       (T("f2"), "Fall 2: rechnungsähnliches Angebot (BGHSt 47, 1)"),
       (T("plan"), "Planmäßig und mit direktem Vorsatz"),
       (T("klein2"), "Und das Kleingedruckte?"),
       (T("kauf"), "Fall 2: das Ergebnis"),
       (T("tun"), "Abgrenzung: Tun oder Unterlassen"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Konkludente Täuschung beim Betrug (§ 263 StGB): Welchen Erklärungswert hat Verhalten im Geschäftsverkehr – und wann täuscht ein inhaltlich wahres Schreiben?

Fall 1: Baldur bestellt im Restaurant ein Drei-Gänge-Menü, obwohl er weiß, dass er nicht zahlen kann. Fall 2: Ortrud bekommt nach ihrer Zeitungsanzeige ein Schreiben mit Registernummer, Betrag, fett gedruckter Zahlungsfrist und ausgefülltem Überweisungsträger – dass es nur ein Angebot ist, steht im Kleingedruckten.

Inhalt:
– § 263 Abs. 1 StGB im Wortlaut: Täuschung über Tatsachen
– Drei Wege: ausdrücklich, konkludent, durch Unterlassen; Maßstab: Erklärungswert nach der Verkehrsanschauung
– Fall 1: Die Bestellung erklärt schlüssig, zahlen zu können und zu wollen; Abwandlung: Entschluss erst nach dem Essen
– Fall 2: rechnungsähnliche Angebotsschreiben (BGHSt 47, 1): planmäßig erweckter Eindruck einer Zahlungspflicht, direkter Vorsatz, Kleingedrucktes
– Abgrenzung: konkludentes Tun oder Unterlassen (Garantenpflicht, § 13 StGB)
– Klausurtipp, Schema, Merksatz

Normen: §§ 263, 13 StGB.

Rechtsprechung:
– BGH, Urt. v. 26.4.2001 – 4 StR 439/00, BGHSt 47, 1, 3–6 (rechnungsähnliche Angebotsschreiben)
– BGH, Urt. v. 15.12.2006 – 5 StR 181/06, Rn. 20–22 (Erklärungswert nach der Verkehrsanschauung)
– BGH, Beschl. v. 10.1.2012 – 4 StR 632/11, Rn. 4 (Tanken: Auftreten als Kunde) und Beschl. v. 23.5.2017 – 4 StR 141/17, Rn. 6 (Hotel)
– BGH, Urt. v. 5.3.2014 – 2 StR 616/12, Rn. 21 (Abofalle: Erkennbarkeit schließt die Täuschung nicht aus)
– BGH, Beschl. v. 9.9.2025 – 5 StR 244/25, Rn. 9 f. (Betrug durch Unterlassen nur mit Aufklärungspflicht)

Hinweise: Baldur, Kellnerin Kaja, Ortrud und Herr Weinert sind erfunden, ebenso das Restaurant und das Schreiben. Mehr dazu: „Betrug § 263 Schema: Täuschung, Irrtum, Verfügung, Schaden“ (Folge 65) und „Tankbetrug: Tanken ohne zu zahlen – Diebstahl oder Betrug?“ (Folge 22).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Betrug #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu, n in [("achtundvierzig Euro", "48 Euro", 1), ("zum achtzigsten\n", "zum 80.\n", 1),
                    ("neunundachtzig Euro sechzig", "89,60 Euro", 1), ("zehn Tagen", "10 Tagen", 1),
                    ("Fall eins:", "Fall 1:", 1), ("Fall zwei:", "Fall 2:", 1)]:
    assert srt.count(alt) == n, (alt, srt.count(alt))
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Paragraf |achtundvierzig|achtzig|sechzig", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["rechnungsähnliches Angebot", "Zechprellerei", "Täuschung durch Unterlassen"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
