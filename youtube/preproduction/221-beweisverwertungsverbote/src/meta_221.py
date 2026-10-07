"""Nachbearbeitung der Upload-Texte für Folge 221 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_171.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fällen, Inhalt, Normen und Rechtsprechung mit Rn./Seite,
Hinweisen und Lizenzzeile; Untertitel: Sprecherbezeichnungen „Herr Haferkamp:“, „Frau Ruhnke:“.
Aufruf: python3 meta_221.py <upload-ordner>"""
import json, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Drei Fälle: Drohung, fehlende Belehrung, Durchsuchung ohne Beschluss"),
       (T("ebv"), "Beweiserhebungsverbot oder Beweisverwertungsverbot?"),
       (T("gesetz"), "Gesetzliche Verbote: unselbständig und selbständig"),
       (T("a136"), "§ 136a Abs. 3 S. 2 StPO: verbotene Vernehmungsmethoden"),
       (T("a252"), "§ 252 StPO: Zeugnisverweigerung in der Hauptverhandlung"),
       (T("a100"), "§ 100d Abs. 2 StPO: Kernbereich privater Lebensgestaltung"),
       (T("a479"), "§ 479 Abs. 2 StPO: Verwendung in anderen Verfahren"),
       (T("unge"), "Ungeschriebene Verbote: Abwägungslehre"),
       (T("rkt"), "Rechtskreistheorie und Widerspruchslösung"),
       (T("fern"), "Fernwirkung und Fortwirkung"),
       (T("l1"), "Lösung der drei Fälle"),
       (T("tipp"), "Klausurtipp: Prüfungsschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Beweisverwertungsverbote im System: Erhebungs- vs. Verwertungsverbot, gesetzlich geregelte Verbote (§ 136a Abs. 3 S. 2, § 252, § 100d Abs. 2, § 479 Abs. 2 StPO), unselbständig und selbständig, Abwägungslehre, Rechtskreis, Widerspruch, Fern- und Fortwirkung – an drei Fällen.

Die Fälle: (1) Ein Kommissar droht Herrn Kleinert in der Vernehmung mit Schmerzen – er gesteht. (2) Eine Polizistin sieht, wie Herr Haferkamp ein Auto zerkratzt, und fragt ihn ohne Belehrung – er gesteht, seine Verteidigerin widerspricht rechtzeitig. (3) Ein Polizist durchsucht die Wohnung von Frau Ruhnke ohne Beschluss, weil er „Gefahr im Verzug“ annimmt – und findet gestohlene Laptops. Drei Fehler, drei Ergebnisse: Warum führt nicht jeder Fehler zum Freispruch?

Inhalt:
– Beweiserhebungsverbot und Beweisverwertungsverbot: kein Automatismus
– Gesetzlich geregelte Verbote: § 136a Abs. 3 S. 2 StPO (unselbständig), § 252 StPO, § 100d Abs. 2 StPO (Kernbereich), § 479 Abs. 2 i. V. m. § 161 Abs. 3 StPO
– Ungeschriebene Verbote: Abwägungslehre, Rechtskreistheorie, Widerspruchslösung (mehr in Folge 132 und Folge 171)
– Reichweite: Fernwirkung grundsätzlich abgelehnt (mehr in Folge 211), Fortwirkung und qualifizierte Belehrung
– Lösung der drei Fälle, Klausurtipp mit Prüfungsschema I.–V., Merksatz

Rechtsprechung:
– BGH, Urt. v. 9.1.2025 – 1 StR 54/24, Rn. 24: Abwägungslehre (Aufklärungsinteresse, Gewicht des Verstoßes, Verbot bei bewusster Missachtung oder grober Verkennung)
– BGH, Urt. v. 22.12.2011 – 2 StR 509/10, Rn. 21: selbständiges Beweisverwertungsverbot aus der Verfassung (Kernbereich)
– BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, BGHSt 61, 221, Rn. 32: § 252 StPO als Verwertungsverbot, Ausnahme richterliche Vernehmung
– BGH, Beschl. v. 27.2.1992 – 5 StR 190/91, BGHSt 38, 214, 225 f.: Widerspruchslösung
– BGH (GrS), Beschl. v. 21.1.1958 – GSSt 4/57, BGHSt 11, 213, 215; BGH, Beschl. v. 5.7.2022 – 4 StR 61/22, Rn. 12: Rechtskreistheorie
– BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f.: keine Fernwirkung
– BGH, Urt. v. 3.5.2018 – 3 StR 390/17, Rn. 28: Fortwirkung, qualifizierte Belehrung
– BGH, Urt. v. 18.4.2007 – 5 StR 546/06, BGHSt 51, 285, Rn. 20, 22, 24: Richtervorbehalt und Verwertung
– BVerfG, Beschl. v. 2.7.2009 – 2 BvR 2225/08, Rn. 16 f.: Abwägung bei fehlerhafter Durchsuchung
– BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, BVerfGE 103, 142, Rn. 38: Gefahr im Verzug nur mit Tatsachen des Einzelfalls

Hinweise: BGHSt 11, 213 und 38, 214 sind mit den Seiten der amtlichen Sammlung zitiert (Volltext über das Deutschsprachige Fallrecht). Das Ergebnis in Fall 3 ist eine Abwägung im Übungsfall. Mehr zur Widerspruchslösung in Folge 132, zum Belehrungsverstoß in Folge 171, zum Fall Gäfgen in Folge 211 und zur Durchsuchung in Folge 151.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StPO #Beweisverwertungsverbot #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nHaferkamp: ", "\nHerr Haferkamp: "), ("\nRuhnke: ", "\nFrau Ruhnke: ")):
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert "Paragraf" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["Beweisverwertungsverbot", "Beweiserhebungsverbot", "Abwägungslehre", "Widerspruchslösung", "Fernwirkung",
             "§ 136a III StPO", "§ 252 StPO", "Rechtskreistheorie", "Strafprozessrecht"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
