"""Nachbearbeitung der Upload-Texte für Folge 274 (nach meta_271.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Materialien,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_274.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Unterkunft im Gewerbegebiet"),
       (T("sv"), "Sachverhalt"),
       (T("kb"), "Klagebefugnis: Gebietserhaltungsanspruch"),
       (T("abwehr"), "Abwehr ohne Beeinträchtigung"),
       (T("p8"), "§ 8 BauNVO: Anlagen für soziale Zwecke"),
       (T("gv"), "Gebietsverträglichkeit: wohnähnlich?"),
       (T("p246"), "§ 246 Abs. 10 BauGB im Wortlaut"),
       (T("stand"), "§ 246 Abs. 10 am Fall (BVerwG 2018)"),
       (T("dring"), "Grenzen: Abs. 13a und Frist"),
       (T("rueck"), "Rücksichtnahme, § 15 BauNVO"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gebietserhaltungsanspruch (BVerwGE 94, 151): Kann ein Betrieb eine Unterkunft für Geflüchtete im Gewerbegebiet verhindern? § 246 BauGB – bundesweit erklärt.

Der Fall: In einem Gewerbegebiet mit Bebauungsplan betreibt Frau Hollenberg eine Schreinerei. Das leere Bürogebäude nebenan soll eine Gemeinschaftsunterkunft für 300 Geflüchtete werden. Die Bauaufsicht genehmigt die Nutzungsänderung mit einer Befreiung nach § 246 Abs. 10 BauGB. Frau Hollenberg fürchtet Auflagen für ihren Betrieb und klagt.

Inhalt:
– Klagebefugnis über den Gebietserhaltungsanspruch: Austauschverhältnis und „rechtliche Schicksalsgemeinschaft“ der Eigentümer im Baugebiet – Abwehr ohne tatsächliche Beeinträchtigung, aber nur im selben Baugebiet
– § 8 BauNVO im Wortlaut: Anlagen für soziale Zwecke nur ausnahmsweise; Gebietsverträglichkeit auch für Ausnahmen; wohnähnliche Nutzung im Gewerbegebiet
– § 246 Abs. 10 BauGB im Wortlaut: Befreiung für Flüchtlingsunterkünfte im Gewerbegebiet bis 31.12.2027 – ohne Bezug zum Gebietszweck und ohne Prüfung der Grundzüge der Planung
– Grenzen: dringender Bedarf (§ 246 Abs. 13a BauGB, im Wortlaut), Frist nur für das Zulassungsverfahren (§ 246 Abs. 17 BauGB)
– Rücksichtnahme: § 15 Abs. 1 Satz 2 BauNVO im Wortlaut – wer an einen Betrieb heranrückt, muss dessen zulässigen Lärm aushalten können
– Ergebnis, Klausurtipp (zwei Stufen, Datum, nur städtebauliche Belange), Klausurschema, Merksatz

Normen: §§ 30, 31, 36, 246 Abs. 10, 13a, 17 BauGB; §§ 1 Abs. 3, 8, 15 BauNVO; §§ 42 Abs. 2, 113 Abs. 1 VwGO.

Rechtsprechung:
– BVerwG, Urt. v. 16.9.1993 – 4 C 28.91, BVerwGE 94, 151 (Gebietserhaltungsanspruch)
– BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8 (Austauschverhältnis, Schicksalsgemeinschaft)
– BVerwG, Beschl. v. 15.9.2020 – 4 B 46.19, Rn. 6 (kein gebietsübergreifender Anspruch)
– BVerwG, Beschl. v. 27.8.2013 – 4 B 39.13, Rn. 3 (unabhängig von Beeinträchtigung)
– BVerwG, Urt. v. 2.2.2012 – 4 C 14.10, Rn. 16 f., 24 (Gebietsverträglichkeit auch bei Ausnahmen)
– BVerwG, Beschl. v. 13.5.2002 – 4 B 86.01 (Pflegeheim im Gewerbegebiet: wohnähnlich)
– BVerwG, Beschl. v. 27.2.2018 – 4 B 39.17, Rn. 1, 10, 11, 13 (Gemeinschaftsunterkunft im Gewerbegebiet, § 246 Abs. 10 BauGB)
– BVerwG, Urt. v. 29.11.2012 – 4 C 8.11, Rn. 16 (Rücksichtnahme, heranrückende Nutzung)
– BVerwG, Beschl. v. 6.12.2011 – 4 BN 20.11, Rn. 5, 7 (persönliche Eigenschaften der Bewohner kein städtebaulicher Gesichtspunkt)
Materialien: BT-Drs. 18/2752, S. 8, 12.

Hinweise: Frau Hollenberg und Herr Kerkhoff sind erfundene Figuren. Die Fristen des § 246 BauGB sind nach dem Stand vom 8. Oktober 2026 wiedergegeben – bitte bei späterer Nutzung prüfen. Mehr dazu: Folge 113 (Baurechtliche Nachbarklage), Folge 200 (Baugebiete der BauNVO).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gebietserhaltungsanspruch #Baurecht #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
srt = re.sub(r"(?m)^Kerkhoff:", "Herr Kerkhoff:", srt)
srt = re.sub(r"(?m)^Hollenberg:", "Frau Hollenberg:", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Gebietserhaltungsanspruch Gewerbegebiet", "Flüchtlingsunterkunft Baurecht",
                                    "246 Abs. 10 BauGB"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
