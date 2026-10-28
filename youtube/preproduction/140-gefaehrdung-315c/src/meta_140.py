"""Nachbearbeitung der Upload-Texte für Folge 140 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_130.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und Lizenzzeile;
Beträge, Jahreszahlen und Gliederungsziffern in den Untertiteln als Ziffern.
Aufruf: python3 meta_140.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Überholen vor der Kuppe, Sachverhalt"),
       (T("p315c"), "§ 315c Abs. 1 StGB im Überblick"),
       (T("th"), "Tathandlung: die sieben Todsünden (Nr. 2 a–g)"),
       (T("p2b"), "Nr. 2 b: falsch überholt (§ 5 StVO)"),
       (T("grob"), "Grob verkehrswidrig und rücksichtslos"),
       (T("gefahr"), "Konkrete Gefahr: Beinahe-Unfall, 750 €"),
       (T("kombi"), "Vorsatz-Fahrlässigkeits-Kombinationen (Abs. 3)"),
       (T("rws"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gefährdung des Straßenverkehrs nach § 315c StGB: sieben Todsünden, konkrete Gefahr und Vorsatz-Fahrlässigkeits-Kombinationen – das Prüfungsschema.

Der Fall: Reinhold ist spät dran und überholt auf einer Landstraße einen langsamen Lastwagen – vor einer Kuppe, ohne Sicht auf den Gegenverkehr. Hinter der Kuppe kommt ihm Gertrud entgegen; nur ihre Vollbremsung verhindert den Zusammenstoß. Verletzt wird niemand. Hat Reinhold sich nach § 315c StGB strafbar gemacht – vorsätzlich oder fahrlässig?

Inhalt:
– § 315c Abs. 1 StGB im Wortlaut (Auszug): Nr. 1 Fahruntüchtigkeit, Nr. 2 die sieben Verkehrsverstöße, „und dadurch“ konkrete Gefahr
– Die „sieben Todsünden“ (Lehrbuchbegriff) als Übersicht: Nr. 2 a–g
– Nr. 2 b „falsch überholt“ mit § 5 Abs. 2 S. 1 StVO
– Grob verkehrswidrig (objektiv) und rücksichtslos (subjektiv: eigensüchtige Gründe oder Gleichgültigkeit)
– Konkrete Gefahr: Beinahe-Unfall; fremde Sachen von bedeutendem Wert (Wertgrenze 750 €); Tatfahrzeug und Mitfahrer
– Vorsatz-Fahrlässigkeits-Kombinationen: Abs. 1, Abs. 3 Nr. 1, Abs. 3 Nr. 2 (Wortlaut Abs. 3)
– Ergebnis mit Konkurrenzen (§ 316 tritt zurück) und § 69 Abs. 2 Nr. 1 StGB, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 315c, 316, 69 StGB; § 5 StVO

Rechtsprechung:
– BGH, Urt. v. 14.3.2024 – 4 StR 354/23, Rn. 29 f. (rücksichtslos: eigensüchtige Gründe oder Gleichgültigkeit; nach BGHSt 5, 392)
– BGH, Beschl. v. 17.2.2021 – 4 StR 225/20 (BGHSt 66, 27), Rn. 14 (grob verkehrswidrig und rücksichtslos beziehen sich auf die objektive Tathandlung)
– OLG Koblenz, Beschl. v. 20.7.2023 – 4 ORs 4 Ss 16/23 (grob verkehrswidrig: besonders gefährliches Abweichen; Rücksichtslosigkeit nicht allein aus dem Tathergang)
– BGH, Beschl. v. 19.6.2024 – 4 StR 73/24, Rn. 6, 7, 9 (Beinahe-Unfall; Mitfahrer und Tatfahrzeug; „und dadurch“)
– BGH, Beschl. v. 13.3.2025 – 4 StR 391/24, Rn. 4 (konkrete Gefahr, Wertgrenze 750 €)
– BGH, Beschl. v. 2.2.2023 – 4 StR 293/22, Rn. 6 (falsches Überholen: „starke Bremsung“ allein belegt keinen Beinahe-Unfall)
– BGH, Beschl. v. 10.4.2019 – 4 StR 86/19, Rn. 7 f. (Wert der Sache und drohender Schaden; vom Täter geführtes Fahrzeug)
– BGH, Beschl. v. 28.9.2010 – 4 StR 245/10, Rn. 4 (Wertgrenze 750 €)
– BGH, Beschl. v. 4.12.2012 – 4 StR 435/12, Rn. 5 f. (Tatfahrzeug, tatbeteiligte Mitfahrer)
– BGH, Beschl. v. 27.3.2024 – 4 StR 493/23, Rn. 14 (Gefährdungsvorsatz: Beinahe-Unfall billigend in Kauf nehmen)

Hinweise: „Sieben Todsünden“ ist ein Lehrbuchbegriff, kein Gesetzesbegriff. Der Fall ist ein vereinfachter Übungsfall; in der Klausur muss der Beinahe-Unfall mit Tatsachen (Abstände, Geschwindigkeiten) belegt sein. Zur Fahruntüchtigkeit (Nr. 1) siehe unsere Folge zu § 316 StGB.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026, StVO zuletzt geändert durch Verordnung vom 30.1.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#GefährdungdesStraßenverkehrs #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("siebenhundertfünfzig Euro", "750 Euro").replace("von fünf auf zwei Jahre", "von 5 auf 2 Jahre")
srt = srt.replace("Römisch eins,", "I.").replace("Römisch zwei und drei:", "II. und III.:")
srt = re.sub(r"§ 315\n\n(\d+\n[^\n]+\n)c ", r"§ 315c\n\n\1", srt)   # Paragraf über eine Untertitelgrenze
srt = srt.replace("Nr. 2b", "Nr. 2 b")
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert "Römisch" not in srt and "hundert" not in srt and "Paragraf" not in srt, re.findall(r".*(?:Römisch|hundert|Paragraf).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
