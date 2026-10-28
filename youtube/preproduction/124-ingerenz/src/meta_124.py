"""Nachbearbeitung der Upload-Texte für Folge 124 (Kopie von meta_115.py) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_124.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Unfall im Dorf – und weitergefahren"),
       (T("fahrt"), "Fahrt (§ 229) und Weiterfahren (Unterlassen)"),
       (T("p13"), "§ 13 Abs. 1 StGB und Ingerenz"),
       (T("pfl"), "Ingerenz im Fall: pflichtwidriges Vorverhalten"),
       (T("entspr"), "Entsprechung, Vorsatz, unmittelbares Ansetzen"),
       (T("mord"), "Mord? Verdeckungsabsicht, § 211 Abs. 2 StGB"),
       (T("streit"), "Streit: Verdecken durch Unterlassen?"),
       (T("p142"), "§ 142, § 323c und Konkurrenzen"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Ingerenz nach § 13 StGB: Wann begründet pflichtwidriges Vorverhalten eine Garantenstellung – und kommt sogar Mord durch Unterlassen in Betracht?

Der Fall: Eckhard fährt im Dorf mit 70 statt 50 km/h und erfasst einen älteren Fußgänger. Der Mann liegt schwer verletzt am Straßenrand, ohne schnelle Hilfe droht er zu sterben. Eckhard hält an, sieht ihn liegen – und fährt weiter, weil er nicht als Unfallverursacher entdeckt werden will. Den Tod nimmt er in Kauf. Eine Radfahrerin ruft den Rettungsdienst, der Mann überlebt. Musste Eckhard helfen? Und ist das versuchter Mord?

Inhalt:
– Die Fahrt: fahrlässige Körperverletzung, § 229 StGB; das Weiterfahren als Unterlassen
– § 13 Abs. 1 StGB im Wortlaut: „rechtlich dafür einzustehen“
– Ingerenz: pflichtwidriges Vorverhalten, das die nahe Gefahr des Erfolgs schafft – und warum verkehrsgerechtes Verhalten nicht genügt
– Entsprechung, bedingter Tötungsvorsatz, unmittelbares Ansetzen, kein Rücktritt
– Mordmerkmal Verdeckungsabsicht (§ 211 Abs. 2 StGB im Wortlaut): andere Straftat, bedingter Vorsatz, Streit „Verdecken durch Unterlassen“
– Strafmilderung nach § 13 Abs. 2 StGB
– Unerlaubtes Entfernen vom Unfallort, § 142 Abs. 1 StGB (Wortlaut); § 323c StGB tritt zurück; Konkurrenzen
– Klausurtipp, Prüfschema, Merksatz
– Garantenstellungen im Überblick: Video „Garantenstellung § 13 StGB“; Versuch: Video „Versuch Schema“

Normen: §§ 13, 211, 212, 22, 23, 24, 142, 229, 323c StGB; § 3 Abs. 3 StVO

Rechtsprechung:
– BGH, Beschl. v. 24.3.2021 – 4 StR 416/20 (BGHSt 66, 66), Rn. 22 (Garant aus Ingerenz: pflichtwidriges Vorverhalten, das die nahe Gefahr des Erfolgs verursacht hat; Unterschied zur Jedermannspflicht aus § 323c StGB)
– BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 19, 21 f. (ohne pflichtwidriges Vorverhalten keine Ingerenz)
– BGH, Urt. v. 15.2.2018 – 4 StR 361/17, Rn. 11, 14, 16 (Verdeckungsmord durch Unterlassen nach einem Unfall; bedingter Tötungsvorsatz und Verdeckungsabsicht schließen sich nicht aus)
– BGH, Urt. v. 12.12.2002 – 4 StR 297/02, Rn. 6, 11 (Verdeckungsmord durch Unterlassen; keine „andere Straftat“, wenn schon die Vortat mit Tötungsvorsatz begangen wurde)
– BGH, Beschl. v. 10.3.2000 – 1 StR 675/99, Rn. 11, 21 (Verdeckungsabsicht bei bedingtem Vorsatz; Entsprechung beim Verdeckungsmord durch Unterlassen)
– BGH, Urt. v. 19.8.2020 – 1 StR 474/19, Rn. 14, 16 (bedingter Tötungsvorsatz beim Unterlassen)
– vgl. BGH, Urt. v. 23.7.2015 – 3 StR 633/14, Rn. 21 (Subsidiarität des § 323c StGB)
– Kaspar/Broichmann, ZJS 2013, 346, 351 f. (Streitstand Verdecken durch Unterlassen)

Hinweise: Das Video prüft Aussetzung (§ 221 StGB) nicht. Dass verkehrsgerechtes Verhalten keine Ingerenz begründet, folgt aus dem Erfordernis des pflichtwidrigen Vorverhaltens. Die frühere Gegenansicht zum Verdecken durch Unterlassen ist nach der Darstellung bei Kaspar/Broichmann wiedergegeben.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Ingerenz #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("§ 323 c", "§ 323c").replace("mit siebzig\nstatt der erlaubten fünfzig", "mit 70 km/h\nstatt der erlaubten 50 km/h")
srt = srt.replace("Mit fünfzig hätte er", "Mit 50 km/h hätte er").replace("zwanzig Kilometer\npro Stunde ", "20 km/h\n")
srt = srt.replace("Römisch eins,", "I.").replace("Römisch zwei,", "II.").replace("Römisch drei und vier:", "III. und IV.:")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
