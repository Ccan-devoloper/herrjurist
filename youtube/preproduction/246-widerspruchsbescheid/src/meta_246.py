"""Nachbearbeitung der Upload-Texte für Folge 246 (nach meta_234.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Landesrecht-Hinweis, Rechtsprechung mit
Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Datum in Ziffern).
Aufruf: python3 meta_246.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Hundehaltung untersagt"),
       (T("frage"), "Die Frage"),
       (T("vv"), "1. Gibt es ein Vorverfahren? Landesrecht"),
       (T("abhilfe"), "2. Abhilfe und Zuständigkeit"),
       (T("kopf"), "3. Kopf und Tenor"),
       (T("gruende"), "Gründe: Sachverhalt und Zulässigkeit"),
       (T("begr"), "Begründetheit: Rechtmäßigkeit und Zweckmäßigkeit"),
       (T("kosten"), "Kosten: § 73 III 3 VwGO, § 80 VwVfG"),
       (T("belehr"), "Rechtsbehelfsbelehrung"),
       (T("zust"), "Zustellung"),
       (T("fehler"), "4. Typische Fehler"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Widerspruchsbescheid nach §§ 68 ff., 73 VwGO: Zulässigkeit, Recht- und Zweckmäßigkeit prüfen und Tenor, Gründe, Kostenentscheidung (§ 73 III 3 VwGO, § 80 VwVfG bzw. Landes-VwVfG) und Belehrung bauen.

Der Fall: Als Referendarin im Landratsamt entwirfst du den Widerspruchsbescheid. Die Gemeinde hat Herrn Holzapfel die Hundehaltung untersagt, weil sein verspielter Mischling trotz Leinenanordnung dreimal frei durch den Ort lief. Herr Holzapfel legt Widerspruch ein, die Gemeinde hilft nicht ab. Was gehört in den Bescheid?

Inhalt (Perspektive 2. Examen):
– Gibt es ein Vorverfahren? § 68 Abs. 1 Satz 1, 2 VwGO und Landesrecht
– Abhilfe (§ 72 VwGO) und Zuständigkeit der Widerspruchsbehörde (§ 73 Abs. 1 VwGO)
– Kopf und Tenor: Zurückweisung, Kosten, Gebühr
– Gründe: Sachverhalt, Zulässigkeit (§ 70 VwGO), Begründetheit mit Rechtmäßigkeit und Zweckmäßigkeit
– Kosten: § 73 Abs. 3 Satz 3 VwGO, § 80 Abs. 1 Satz 3, Abs. 3 Satz 2 VwVfG
– Rechtsbehelfsbelehrung (§§ 58, 74, 79 VwGO) mit Muster, Zustellung (§ 73 Abs. 3 VwGO, VwZG)
– typische Fehler, Klausurtipp, Schema, Merksatz

Normen: §§ 58, 68, 70, 72, 73, 74, 79 VwGO; §§ 39, 80 VwVfG (bei Landesbehörden das Verwaltungsverfahrensgesetz des Landes, z. B. § 80 VwVfG NRW); §§ 2, 3 VwZG.

Landesrecht: Ob es ein Widerspruchsverfahren gibt, regelt jedes Land selbst (§ 68 Abs. 1 Satz 2 VwGO). Weitgehend abgeschafft, jeweils mit Ausnahmen, ist es z. B. in Nordrhein-Westfalen (§ 110 JustG NRW; Widerspruchsbehörde ist dann die Ausgangsbehörde, § 111 JustG NRW) und in Niedersachsen (§ 80 NJG). Die Regeln der übrigen Länder konnten nicht an allen amtlichen Portalen geprüft werden – bitte im Landesrecht deines Landes nachlesen. Auch Gebühren für den Widerspruchsbescheid richten sich nach dem Kostenrecht des Landes. Land und Behörden im Video sind fiktiv.

Rechtsprechung:
– BVerwG, Urt. v. 12.8.2014 – 1 C 2.14, Rn. 11–13 (Zweckmäßigkeitskontrolle durch die Widerspruchsbehörde, Zustellung nach § 73 Abs. 3 VwGO)

Hinweise: Herr Holzapfel, Herr Sperling und Frau Körner sind erfundene Figuren. Mehr dazu: Folge 069 (Anfechtungsklage: Vorverfahren), Folge 102 (Anfechtungsurteil).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Widerspruchsbescheid #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"§ (\d+)\n\n(\d+\n[^\n]+\n)Abs\. (\d+)\. ", r"§ \1 Abs. \3.\n\n\2", srt)   # über die Cue-Grenze
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("zweiten März 2026", "2. März 2026")]:
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Paragraf|§ \d+\nAbs|§ \d+\n\n\d+\n[^\n]+\nAbs", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Widerspruchsbescheid Aufbau", "Widerspruchsbescheid Tenor", "Assessorexamen VwGO"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
