"""Nachbearbeitung der Upload-Texte für Folge 128 (nach tools/youtube_metadaten.py, nichts dort geändert), wie Folge 094:
Hilfsangebot ganz oben in der Beschreibung (TelefonSeelsorge, Nummern verifiziert auf telefonseelsorge.de am 03.10.2026),
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Fall ohne Methode, Inhalt, Rechtsprechung mit Randnummern, Lizenzzeile,
zusätzliche Tags; Untertitel: lautliche Schreibung „ernst-liche“ zurück auf „ernstliche“, Zahlen und Paragrafen in Ziffern.
Aufruf: python3 meta_128.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Hedwig und Wilfried – und die Frage"),
       (T("aus"), "1. Ausgangspunkt: Suizid und Hilfe straflos"),
       (T("p216"), "§ 216 Abs. 1 StGB im Wortlaut: Privilegierung des Totschlags"),
       (T("krit"), "2. Abgrenzung: Wer beherrscht den letzten Akt?"),
       (T("gis"), "Der Gisela-Fall, BGHSt 19, 135"),
       (T("neu"), "3. Neuere Rechtsprechung: BGH 2022, 6 StR 68/21"),
       (T("merk"), "4. Merkmale: ausdrücklich, ernstlich, bestimmt"),
       (T("zw"), "5. Täter oder Gehilfe? Ergebnis und Gegenvariante"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz"), (T("hilfe"), "Hilfsangebot")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Wenn dich das Thema selbst betrifft: Die TelefonSeelsorge ist rund um die Uhr und kostenlos erreichbar, unter 0800 111 0 111, 0800 111 0 222 oder 116 123 (telefonseelsorge.de).

Tötung auf Verlangen (§ 216 StGB) oder straflose Suizidhilfe? Der Gisela-Fall zeigt, warum es darauf ankommt, wer den letzten, unwiderruflichen Akt beherrscht.

Der Fall: Hedwig ist schwer krank und bittet ihren Mann Wilfried seit Monaten ausdrücklich, ihr beim Sterben zu helfen; sie hat es sich lange und klar überlegt. Eines Abends führt Wilfried den tödlichen Schritt selbst aus, Hedwig kann danach nichts mehr ändern. Ist er wegen Tötung auf Verlangen strafbar – und wäre er straflos geblieben, wenn er den letzten Schritt ihr überlassen hätte?

Inhalt:
– Ausgangspunkt: Selbsttötung und Hilfe dazu straflos (vgl. Folge 094); § 212 StGB und § 216 Abs. 1 StGB im Wortlaut
– Abgrenzung: Wer beherrscht das zum Tod führende Geschehen zuletzt? Tatherrschaft (vgl. Folge 119)
– Der Gisela-Fall: BGH, Urteil vom 14.8.1963, BGHSt 19, 135
– Neuere Rechtsprechung: BGH, Beschluss vom 28.6.2022 – normative Betrachtung, Gesamtplan; Recht auf selbstbestimmtes Sterben (BVerfG 2020)
– Merkmale des § 216 StGB: ausdrücklich, ernstlich, bestimmt
– Zweispalter Täter des § 216 / strafloser Gehilfe, Ergebnis und Gegenvariante
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 212, 216 StGB; § 217 StGB a. F.

Rechtsprechung:
– BGH, Urt. v. 14.8.1963 – 2 StR 181/63, BGHSt 19, 135, 139 f. (Gisela-Fall): Wer das Geschehen nach dem Gesamtplan bis zuletzt in der Hand hat, hat die Tatherrschaft; Freispruch aufgehoben (wiedergegeben nach BGH 6 StR 68/21 Rn. 14, 18 f.)
– BGH, Urt. v. 4.7.2018 – 2 StR 245/17, BGHSt 63, 161, Rn. 18 (wer das zum Tod führende Geschehen zuletzt beherrscht), Rn. 19 (Verlangen mehr als bloße Zustimmung, handlungsleitend)
– BGH, Urt. v. 7.10.2010 – 3 StR 168/10, Rn. 12 f., 17 (Ernstlichkeit)
– BGH, Beschl. v. 28.6.2022 – 6 StR 68/21, Rn. 13–17 (normative Betrachtung, Gesamtplan, straflose Suizidhilfe, Freispruch), Rn. 21, 23 (verfassungskonforme Einschränkung des § 216 offengelassen), Rn. 25, 29 (keine Rettungspflicht des Ehegatten bei freiem Sterbewillen)
– BVerfG, Urt. v. 26.2.2020 – 2 BvR 2347/15 u. a., Leitsatz 1, Rn. 337 (§ 217 StGB nichtig)

Kapitel:
{kapitel}

Der Beispielfall ist erfunden. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#Strafrecht #Jura #Examen
"""
for verboten in ("Spritze", "Becher", "Insulin", "Tablett", "Gas", "Auspuff", "Schlauch", "Medikament"):
    assert verboten.lower() not in BESCHR.lower(), verboten
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("ernst-liche", "ernstliche")
for a, b in [("neunzehnhundertdreiundsechzig", "1963"), ("zweitausendzweiundzwanzig", "2022"), ("zweitausendzwanzig", "2020"),
             ("Folge vierundneunzig", "Folge 94"), ("Folge hundertneunzehn", "Folge 119"),
             ]:
    srt = srt.replace(a, b)
srt, n_ = re.subn(r"sechs(\s+)Monate(\s+)bis(\s+)fünf(\s+)Jahre", r"6\1Monate\2bis\g<3>5\4Jahre", srt)
assert n_ == 1, n_
for w in ("ernst-liche", "neunzehnhundert", "zweitausend", "vierundneunzig", "hundertneunzehn"):
    assert w not in srt, w
srt = re.sub(r"mindestens\s+fünf\s+Jahren", lambda m_: m_.group(0).replace("fünf", "5"), srt)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
for verboten in ("Spritze", "Becher", "Insulin"):
    assert verboten not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["thumbnail_text"] = "TÖTUNG AUF VERLANGEN"
m["thumbnail_b"] = "WER HANDELT ZULETZT?"
m["hook_vorschlag"] = ("Ein Mann erfüllt den Wunsch seiner schwerkranken Frau und führt den tödlichen Schritt selbst aus – "
                       "wäre er straflos geblieben, wenn er ihr den letzten Schritt überlassen hätte?")
for t in ("Tötung auf Verlangen", "Suizidhilfe", "6 StR 68/21", "BGHSt 63, 161", "Ernstlichkeit des Verlangens"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
