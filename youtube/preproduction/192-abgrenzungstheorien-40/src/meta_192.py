"""Nachbearbeitung der Upload-Texte für Folge 192 (nach meta_188.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Landesrecht-Hinweis, Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Normen,
Sprecher).
Aufruf: python3 meta_192.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kündigung der Parzelle im Kleingarten"),
       (T("wl40"), "§ 40 Abs. 1 S. 1 VwGO und § 13 GVG im Wortlaut"),
       (T("mm"), "Die drei Merkmale des Verwaltungsrechtswegs"),
       (T("norm"), "Die streitentscheidende Norm: §§ 4, 9 BKleingG"),
       (T("th1"), "Interessentheorie"),
       (T("th2"), "Subordinationstheorie"),
       (T("th3"), "Modifizierte Subjektstheorie (h. M.)"),
       (T("sf"), "Sonderfälle: Zwei-Stufen-Theorie, Hausverbot, Fiskalverwaltung"),
       (T("loes"), "Lösung: Zivilrechtsweg, § 13 GVG"),
       (T("ki2"), "Falscher Rechtsweg: Verweisung nach § 17a Abs. 2 GVG"),
       (T("bed"), "Bedeutung für Handlungsform und Verfahrensrecht"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema Verwaltungsrechtsweg"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Abgrenzungstheorien: Interessen-, Subordinations- und modifizierte Subjektstheorie – so bestimmst du, ob öffentliches Recht gilt und § 40 I VwGO greift.

Der Fall: Die Stadt kündigt einer Kleingärtnerin die Parzelle in der städtischen Kleingartenanlage. Sie will vor das Verwaltungsgericht – schließlich ist die Stadt doch eine Behörde. Zivilgericht oder Verwaltungsgericht?

Inhalt:
– § 40 Abs. 1 S. 1 VwGO und § 13 GVG im Wortlaut; die drei Merkmale: öffentlich-rechtliche Streitigkeit, nichtverfassungsrechtlicher Art, keine abdrängende Sonderzuweisung
– Erst die streitentscheidende Norm bestimmen: § 4 Abs. 1 und § 9 Abs. 1 BKleingG im Wortlaut
– Interessentheorie, Subordinationstheorie und modifizierte Subjektstheorie (Sonderrechtstheorie, h. M.) – je mit Beispiel und Kritik als Tabelle
– Sonderfälle: Zwei-Stufen-Theorie (Zugang zur öffentlichen Einrichtung), Hausverbot, Fiskalverwaltung
– Lösung: Die Stadt kündigt als Verpächterin – Zivilrechtsweg nach § 13 GVG
– Falscher Rechtsweg: Verweisung nach § 17a Abs. 2 S. 1 GVG (i. V. m. § 173 S. 1 VwGO) statt Abweisung; § 17b Abs. 1 S. 2 GVG
– Bedeutung für Handlungsform (Verwaltungsakt oder Vertrag, § 35 S. 1 VwVfG) und Verfahrensrecht (§ 1 Abs. 1 VwVfG)
– Klausurtipp, Prüfschema, Merksatz

Normen: § 40 Abs. 1 S. 1, Abs. 2 S. 1, § 173 S. 1 VwGO; §§ 13, 17a Abs. 2 S. 1, 17b Abs. 1 S. 2 GVG; §§ 4 Abs. 1, 9 BKleingG; §§ 581 ff. BGB; §§ 1 Abs. 1, 28, 35 S. 1, 54 VwVfG; § 54 Abs. 1 BeamtStG

In deinem Land ggf. andere Nummer: Den Anspruch auf Zulassung zu öffentlichen Einrichtungen regelt die Gemeindeordnung, z. B. § 8 Abs. 2 GO NRW (am amtlichen Text geprüft); in den übrigen Ländern bitte die eigene Gemeindeordnung nachschlagen. Die Landes-Verwaltungsverfahrensgesetze gelten ebenfalls nur für öffentlich-rechtliche Verwaltungstätigkeit (z. B. § 1 Abs. 1 VwVfG NRW).

Rechtsprechung:
– BVerwG, Beschl. v. 21.11.2016 – 10 AV 1.16, Rn. 5 f. (modifizierte Subjektstheorie; Gemeinde nicht als Verwaltungsträger; Verweisung an das Landgericht)
– BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 4, 6, 8, 15 (Über-/Unterordnung und Sonderrecht; Fiskalverwaltung; „nicht das Ziel, sondern die Rechtsform“; Zweistufentheorie)
– VG Düsseldorf, Beschl. v. 28.6.2018 – 15 L 1022/18, Rn. 20 (Hausverbot: Zweck entscheidet)
– BGH, Urt. v. 17.7.2025 – III ZR 92/24 (Kündigung eines Kleingarten-Pachtvertrags durch eine Stadt vor den Zivilgerichten)

Hinweise: Ob die Kündigung im Fall wirksam ist, prüft das Video nicht – es geht allein um den Rechtsweg. Die Abgrenzungstheorien und ihre Kritik sind Lehrbegriffe; die Rechtsprechung verwendet die Formel der modifizierten Subjektstheorie. Den Aufbau von Zulässigkeit und Begründetheit zeigt die Folge „Zulässigkeit und Begründetheit: Aufbau im Öffentlichen Recht“, die Klagearten die Folge „Klagearten VwGO“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Verwaltungsrecht #Jura #Abgrenzungstheorien
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"§\n(\d+)", r"§ \1\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei)([,:])( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(3), srt)
for muster, ersatz in [(r"seit zwanzig\sJahren", "seit 20 Jahren"), (r"zum dreißigsten\sNovember", "zum 30. November")]:
    srt, n = re.subn(muster, lambda m: ersatz.replace(" ", "\n", 1) if "\n" in m.group(0) else ersatz, srt)
    assert n, muster
srt = srt.replace("\nKirschner: ", "\nFrau Kirschner: ")
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
