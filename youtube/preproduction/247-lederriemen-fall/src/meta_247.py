"""Nachbearbeitung der Upload-Texte für Folge 247 (nach meta_235.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lehrmaterial, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_247.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Lederriemen und Sandsack"),
       (T("frage"), "Die Frage"),
       (T("p15"), "§ 15 StGB: Vorsatz oder Fahrlässigkeit"),
       (T("bgh"), "BGHSt 7, 363: Billigen im Rechtssinne"),
       (T("formel"), "Eventualvorsatz heute: Wissen und Wollen"),
       (T("gesamt"), "Gesamtschau und Hemmschwelle"),
       (T("sub"), "Subsumtion am Fall"),
       (T("erg"), "Ergebnis: Totschlag und Mord"),
       (T("lehre"), "Gegenansichten der Lehre"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Lederriemen-Fall (BGHSt 7, 363): Wie grenzt man Eventualvorsatz von bewusster Fahrlässigkeit ab – was bedeutet Billigen im Rechtssinne (§ 15 StGB)?

Der Fall (echter Fall, vereinfacht und mit anderen Namen): Zwei Männer wollen einen Bekannten ausrauben. Den Lederriemen verwerfen sie, weil das Opfer daran sterben könnte, und nehmen einen Sandsack. Doch der Sandsack platzt – und sie greifen zum heimlich mitgebrachten Riemen. Der Mann stirbt. Den Tod wollten sie nicht. Haben sie trotzdem vorsätzlich getötet?

Inhalt:
– § 15 StGB im Wortlaut: Vorsatz als Weiche zwischen §§ 212, 211 und §§ 222, 251 StGB
– BGHSt 7, 363: Billigen im Rechtssinne – auch ein höchst unerwünschter Erfolg kann gebilligt sein
– Die heutige Formel: Wissenselement und Willenselement; bewusste Fahrlässigkeit als ernsthaftes, nicht nur vages Vertrauen
– Gesamtschau aller Umstände; warum das Schlagwort „Hemmschwelle“ keine Begründung ersetzt
– Subsumtion am Fall: Eventualvorsatz
– Ergebnis: Totschlag, Mord (Habgier, Ermöglichungsabsicht)
– Gegenansichten der Lehre: Möglichkeits- und Wahrscheinlichkeitstheorie
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 15, 211, 212, 222, 251 StGB.

Rechtsprechung:
– BGH, Urt. v. 22.4.1955 – 5 StR 35/55, BGHSt 7, 363 (Lederriemen-Fall)
– BGH, Urt. v. 30.11.2005 – 5 StR 344/05, Rn. 28 (Erfolg muss den Wünschen des Täters nicht entsprechen; BGHSt 7, 363, 369)
– BGH, Beschl. v. 10.1.2023 – 1 StR 333/22, Rn. 2 („Billigen im Rechtssinne“; BGHSt 7, 363, 368 ff.)
– BGH, Urt. v. 18.6.2020 – 4 StR 482/19, BGHSt 65, 42, Rn. 22 f. (bedingter Tötungsvorsatz, bewusste Fahrlässigkeit, Gesamtschau)
– BGH, Urt. v. 22.3.2012 – 4 StR 558/11, BGHSt 57, 183, Rn. 42, 45 (Hemmschwelle)
– BGH, Beschl. v. 16.2.2021 – 2 StR 391/20, Rn. 27 f.; BGH, Urt. v. 9.3.1993 – 1 StR 870/92, BGHSt 39, 159 (Ermöglichungsabsicht und bedingter Tötungsvorsatz, Habgier)

Lehrmaterial: Universität Freiburg (Hefendehl), Vorlesung Strafrecht AT, § 10 KK 197–209 (Möglichkeits-, Wahrscheinlichkeits- und Billigungstheorie; Lösung Lederriemenfall).

Hinweise: Willi und Hans sind erfundene Namen für die Angeklagten des echten Falls; der Sachverhalt ist vereinfacht. Die drei Vorsatzformen erklärt Folge 029.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Eventualvorsatz #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Lederriemenfall", "Billigungstheorie", "bedingter Tötungsvorsatz"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
