"""Nachbearbeitung der Upload-Texte für Folge 155 (Kopie von meta_124.py) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch und Zahlen in den Untertiteln.
Aufruf: python3 meta_155.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Ein Faustschlag vor der Bar"),
       (T("va"), "Zwei Varianten: Auge verloren oder Tod"),
       (T("grund"), "Grunddelikt und Erfolgsqualifikation, § 18 StGB"),
       (T("p226"), "§ 226 Abs. 1 StGB im Wortlaut"),
       (T("sub_a"), "Variante A: Verlust des Sehvermögens"),
       (T("p227"), "Variante B: § 227 StGB"),
       (T("spez"), "Spezifischer Gefahrzusammenhang: Erfolg oder Handlung?"),
       (T("guben"), "Flucht des Opfers: Gubener Hetzjagd"),
       (T("sub_b"), "Lösung Variante B, Abgrenzung §§ 212, 222"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schwere Körperverletzung § 226 und Körperverletzung mit Todesfolge § 227 StGB: schwere Folgen, § 18 StGB und der spezifische Gefahrzusammenhang.

Der Fall: Vor einer Bar streiten Roswitha und Ludger um ein Taxi. Roswitha schlägt Ludger mit der Faust ins Gesicht – sie will ihn verletzen, mehr nicht. Ludger stürzt rückwärts auf das Pflaster. Variante A: Er verliert dauerhaft das Sehvermögen auf einem Auge. Variante B: Sein Kopf schlägt beim Sturz auf, Ludger stirbt. Was ändert die schwere Folge?

Inhalt:
– Grunddelikt § 223 StGB und erfolgsqualifizierte Delikte: Grunddelikt plus schwere Folge
– § 18 StGB im Wortlaut: wenigstens Fahrlässigkeit hinsichtlich der Folge
– § 226 Abs. 1 StGB im Wortlaut (Nr. 1 bis 3); Verlust des Sehvermögens auf einem Auge; Abs. 2 absichtlich oder wissentlich
– § 227 Abs. 1 StGB im Wortlaut: Kausalität allein reicht nicht
– Spezifischer Gefahrzusammenhang: Letalitätstheorie oder Gefahr der Körperverletzungshandlung (BGH)
– Versuchte Körperverletzung mit Todesfolge und Flucht des Opfers: Gubener Hetzjagd (BGHSt 48, 34)
– Vorhersehbarkeit, minder schwerer Fall § 227 Abs. 2, Abgrenzung zu §§ 212, 222 StGB
– Klausurtipp, Prüfungsschema, Merksatz
– Grunddelikt: Video „Körperverletzung § 223 StGB“; Tötungsdelikte im Überblick: eigenes Video

Normen: §§ 18, 223, 226, 227 StGB; Abgrenzung §§ 212, 222 StGB

Rechtsprechung:
– BGH, Urt. v. 9.10.2002 – 5 StR 42/02 (BGHSt 48, 34, „Gubener Hetzjagd“), Rn. 37–40, 42 (spezifischer Gefahrzusammenhang; Gefahr kann schon von der Körperverletzungshandlung ausgehen; erfolgsqualifizierter Versuch; Flucht des Opfers deliktstypisch; Vorhersehbarkeit)
– BGH, Urt. v. 10.1.2008 – 5 StR 435/07, Rn. 8, 10 (Kausalität genügt nicht; Gefahr der Handlung; älteres Urteil 3 StR 119/70, NJW 1971, 152, „ohnehin zu restriktiv“)
– BGH, Beschl. v. 14.12.2000 – 4 StR 327/00, Rn. 16 (faktischer Verlust der Sehkraft, § 226 Abs. 1 Nr. 1 StGB)
– BGHSt 31, 96, 98 (Formel der spezifischen Gefahr, zitiert nach 5 StR 42/02, Rn. 37)

Hinweise: Die Lösungen am Übungsfall (typische Sturzgefahr eines Faustschlags ins Gesicht, Vorhersehbarkeit in beiden Varianten) sind Wertungen auf Grundlage dieser Maßstäbe. Die Letalitätstheorie ist nach der Darstellung in BGHSt 48, 34 wiedergegeben. Gefährliche Körperverletzung (§ 224 StGB) und Konkurrenzen prüft das Video nicht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Körperverletzung #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("§ 226 a", "§ 226a").replace("§§ 223 bis 226 a", "§§ 223 bis 226a")
srt = srt.replace("bis zweihundertsechsundzwanzig a,", "bis 226a,").replace("Hake den §§ 227", "Hake den § 227")
srt = srt.replace("Nr. 2 und drei dagegen", "Nr. 2 und 3 dagegen")
for w, z in (("Eins:", "1."), ("Zwei:", "2."), ("Drei:", "3."), ("Vier:", "4."), ("Fünf:", "5.")):
    srt = srt.replace("\n" + w + " ", "\n" + z + " ")
assert "zweihundert" not in srt and "§§ 227 nicht" not in srt
srt = srt.replace("Römisch eins,", "I.").replace("Römisch zwei,", "II.").replace("Römisch drei,", "III.")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
