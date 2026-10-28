"""Nachbearbeitung der Upload-Texte für Folge 119 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fällen, Inhalt, Belegen, Offenlegung, Lizenzzeile,
zusätzliche Tags; Untertitel: „Römisch eins/zwei/…“ als I./II./…, „Abs. 1, Alt. 1“ ohne Komma.
Aufruf: python3 meta_119.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Badewannen-Fall und Staschinski-Fall"),
       (T("prob"), "Täter, Anstifter, Gehilfe: §§ 25, 26, 27 StGB"), (T("straf"), "Warum die Abgrenzung zählt"),
       (T("rg1"), "Subjektive Theorie des Reichsgerichts"), (T("bgh56"), "BGH 1956 und der Staschinski-Fall"),
       (T("krit"), "Kritik und Wende: § 25 Abs. 1 Alt. 1 StGB"), (T("thl"), "Tatherrschaftslehre"),
       (T("zw"), "Streitstand: Rechtsprechung gegen Lehre"), (T("ents"), "Streitentscheid"),
       (T("erg"), "Ergebnis nach heutigem Recht"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Abgrenzung Täter Teilnehmer nach §§ 25 ff. StGB: Rechtsprechung (wertende Gesamtbetrachtung) gegen Lehre (Tatherrschaft) – mit Badewannen- und Staschinski-Fall (auch: Staschynskij-Fall).

Die Fälle: 1940 sieht das Reichsgericht in einer Frau, die auf Drängen ihrer Schwester deren Neugeborenes tötet, nur eine Gehilfin (Badewannen-Fall, RGSt 74, 84). 1962 verurteilt der Bundesgerichtshof einen Agenten, der im Auftrag seiner Vorgesetzten in München zwei Exilpolitiker getötet hat, nur wegen Beihilfe zum Mord (Staschinski-Fall, BGHSt 18, 87). Wer selbst tötet – ist der nicht immer Täter?

Inhalt:
– §§ 25, 26, 27 StGB: Täter, Anstifter, Gehilfe (§ 25 Abs. 1 und § 27 Abs. 1 im Wortlaut)
– warum die Abgrenzung zählt: Milderung beim Gehilfen nach § 27 Abs. 2 Satz 2, § 49 Abs. 1 StGB
– die subjektive Theorie des Reichsgerichts: animus auctoris und animus socii
– BGHSt 8, 393 (1956) und der Staschinski-Fall (1962)
– Kritik und Wende: § 25 Abs. 1 Alt. 1 StGB seit 1975
– Tatherrschaftslehre: Zentralgestalt, Handlungs-, Willens- und funktionale Tatherrschaft
– heutige Rechtsprechung: wertende Gesamtbetrachtung (Interesse, Umfang, Tatherrschaft oder Wille dazu)
– Streitentscheid und wann der Streit in der Klausur dahinstehen kann
– Ergebnis beider Klassiker nach heutigem Recht
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 25, 26, 27 StGB; § 49 Abs. 1 StGB

Rechtsprechung:
– RG, Urt. v. 19.2.1940 – 3 D 69/40, RGSt 74, 84 (Badewannen-Fall)
– BGHSt 8, 393 (1956)
– BGH, Urt. v. 19.10.1962 – 9 StE 4/62, BGHSt 18, 87 (Staschinski-Fall)
– BGH, Urt. v. 22.7.1992 – 3 StR 35/92, BGHSt 38, 315, Rn. 4–6 (wer alle Tatbestandsmerkmale selbst verwirklicht, ist grundsätzlich Täter)
– BGH, Urt. v. 23.3.2023 – 3 StR 363/22, Rn. 8 (wertende Gesamtbetrachtung)
– BGH, Beschl. v. 6.8.2019 – 3 StR 189/19, Rn. 6 (Tatherrschaft nur ein Kriterium)
Die Urteile des Reichsgerichts von 1940 und des BGH von 1956 und 1962 sind nicht frei im Volltext abrufbar; ihr Inhalt ist nach dem BGH-Urteil von 1992 und dem Vorlesungsskript Hefendehl wiedergegeben.

Lehrmeinungen nach dem Vorlesungsskript Hefendehl, Strafrecht AT, Universität Freiburg (strafrecht-online.org), § 27 KK 680–689 und § 28 KK 717. § 25 StGB in der Fassung des 2. StrRG (BGBl. I 1969 S. 717), in Kraft seit 1.1.1975 (BGBl. I 1973 S. 909).

Mehr dazu: Mittäterschaft (Folge 104), Katzenkönig-Fall (Folge 91).

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#AbgrenzungTäterTeilnehmer #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III."), ("vier", "IV.")):
    srt = re.sub(r"Römisch\s+" + alt + r"\b:?", neu, srt)
srt = re.sub(r"(Abs\. \d+), Alt\.", r"\1 Alt.", srt)
assert "Römisch" not in srt and "Euro" not in srt, "Untertitel prüfen"
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Staschinski-Fall", "animus auctoris", "Täterschaft und Teilnahme", "§ 25 I StGB", "Beihilfe § 27"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
