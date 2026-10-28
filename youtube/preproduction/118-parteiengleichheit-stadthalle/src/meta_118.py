"""Nachbearbeitung der Upload-Texte für Folge 118 (Kopie von meta_115.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen der Länder (nur am Wortlaut
geprüfte mit Paragraf, übrige mit Prüfhinweis), Rechtsprechung mit Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen.
Aufruf: python3 meta_118.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Stadthalle für die Weitblick-Partei?"),
       (T("anspr"), "Anspruch auf Zulassung: § 8 GO NRW (Beispiel)"),
       (T("tabelle"), "Andere Länder und Art. 28 Abs. 2 GG"),
       (T("p5"), "§ 5 Abs. 1 PartG: Gleichbehandlung der Parteien"),
       (T("widm"), "Widmung und Vergabepraxis"),
       (T("ratsb"), "Widmungsänderung aus konkretem Anlass"),
       (T("privi"), "Parteienprivileg, Art. 21 Abs. 4 GG"),
       (T("vs"), "Beobachtung durch den Verfassungsschutz"),
       (T("grenz"), "Grenzen und Ergebnis"),
       (T("eil"), "Durchsetzung: § 123 VwGO"),
       (T("wetz"), "Der Fall Wetzlar (BVerfG, 1 BvQ 18/18)"),
       (T("gruende"), "Bindung an Gerichtsentscheidungen, Art. 20 Abs. 3 GG"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Parteiengleichheit (§ 5 PartG, Art. 21 GG): Darf eine Stadt einer beobachteten Partei die Stadthalle verweigern? Der Fall Wetzlar – bundesweit erklärt.

Der Fall (fiktiv): Die Weitblick-Partei will ihren Landesparteitag in der Stadthalle abhalten; ihr Landesverband hat seinen Sitz in der Stadt. Der Verfassungsschutz beobachtet die Partei, verboten ist sie nicht. Der Termin ist frei, im letzten Jahr hielten zwei andere Parteien dort ihre Parteitage ab. Die Bürgermeisterin lehnt ab, eine Woche nach dem Antrag beschließt der Stadtrat: keine Parteiveranstaltungen mehr. Die Partei beantragt eine einstweilige Anordnung. Darf die Stadt Nein sagen?

Inhalt:
– Anspruch auf Zulassung zu öffentlichen Einrichtungen: Gemeindeordnung (Beispiel NRW: § 8 Abs. 2, 4 GO NRW im Wortlaut), Personenvereinigungen, „im Rahmen des geltenden Rechts“: Widmung und Kapazität
– Selbstverwaltung (Art. 28 Abs. 2 GG) und § 5 Abs. 1 PartG im Wortlaut: Gleichbehandlung der Parteien, Chancengleichheit (Art. 3, 21 GG) – auch für Parteien ohne Sitz in der Stadt
– Widmung durch Vergabepraxis; Widmungsänderung aus konkretem Anlass, nur um einen Antrag abzulehnen
– Parteienprivileg (Art. 21 Abs. 4 GG im Wortlaut): Bis zur Entscheidung des Bundesverfassungsgerichts keine Benachteiligung wegen der Ziele; die Beobachtung durch den Verfassungsschutz ändert daran nichts; Abgrenzung Art. 21 Abs. 3 GG (Finanzierungsausschluss)
– Grenzen: Termin vergeben (Priorität), sachliche Bedingungen für alle Parteien (§ 5 Abs. 3 PartG), Gegendemonstrationen und polizeilicher Notstand
– Durchsetzung im Eilverfahren (§ 123 VwGO), Vorwegnahme der Hauptsache
– Der Fall Wetzlar 2018: Die Stadt befolgte die Gerichtsentscheidungen nicht – Bindung an Gesetz und Recht (Art. 20 Abs. 3 GG)
– Klausurtipp, Prüfschema, Merksatz

Zulassung zu öffentlichen Einrichtungen in den Ländern (Kommunalrecht ist Landesrecht):
– Nordrhein-Westfalen: § 8 Abs. 2, 4 GO NRW
– Niedersachsen: § 30 Abs. 1, 3 NKomVG
– Sachsen: § 10 Abs. 2, 5 SächsGemO
– Brandenburg: § 12 Abs. 1 BbgKVerf („Jede Person“)
– Baden-Württemberg, Bayern, Hessen, Mecklenburg-Vorpommern, Rheinland-Pfalz, Saarland, Sachsen-Anhalt, Schleswig-Holstein, Thüringen: eigene Gemeindeordnung bzw. Kommunalverfassung – Paragraf bitte selbst nachschlagen (Wortlaut für dieses Video nicht geprüft)
– Berlin, Hamburg, Bremen (Stadtstaaten): nicht geprüft
Der Anspruch aus § 5 Abs. 1 PartG gilt bundesweit.

Normen: § 5 PartG; Art. 3, 20 Abs. 3, 21, 28 Abs. 2 GG; § 123 VwGO; Gemeindeordnungen der Länder

Rechtsprechung:
– BVerfG (K), Beschl. v. 24.3.2018 – 1 BvQ 18/18, Rn. 1 f., 5 (Stadthalle Wetzlar: Pflicht der Stadt, der verwaltungsgerichtlichen Entscheidung Folge zu leisten; Art. 8 Abs. 1 i. V. m. Art. 20 Abs. 3, 19 Abs. 4 GG); Pressemitteilungen Nr. 16/2018 und Nr. 26/2018
– BVerfG (K), Beschl. v. 26.8.2016 – 2 BvQ 46/16, Rn. 7 (Chancengleichheit der Parteien bei öffentlichen Einrichtungen; § 5 Abs. 1 PartG)
– BVerfG, Beschl. v. 29.10.1975 – 2 BvE 1/75, BVerfGE 40, 287, Rn. 16, 19 (Parteienprivileg; Verfassungsschutzbericht ohne rechtliche Wirkung)
– BVerfG, Urt. v. 17.1.2017 – 2 BvB 1/13, Rn. 526 (bis zur Feststellung kein administratives Einschreiten; politisch bekämpfen, nicht behindern)
– OVG NRW, Beschl. v. 12.5.2021 – 15 B 605/21, Rn. 10, 12, 14 (Stadthalle, Vergabepraxis, Gleichbehandlungsanspruch)
– OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 10, 13, 21, 24, 29 (Widmung durch Vergabepraxis, Gegendemonstrationen, Priorität, Vorwegnahme der Hauptsache)
– VG Minden, Beschl. v. 3.5.2023 – 2 L 353/23, Rn. 8 f., 42, 44, 51 (Anspruch ohne Sitz in der Gemeinde; Widmungsänderung nach Antragstellung)
– Nds. OVG, Beschl. v. 8.6.2022 – 10 ME 75/22, Leitsatz 1 (Widmungsänderung allein zur Ablehnung eines bestimmten Antrags)
– OVG NRW, Urt. v. 13.5.2024 – 5 A 1218/22, Rn. 111, 113 (Parteienprivileg; Beobachtung als Vorbereitung eines Verfahrens nach Art. 21 Abs. 4 GG)

Hinweise: Der Fall im Video ist erfunden; die Weitblick-Partei gibt es nicht. Der reale Fall Wetzlar betraf eine Wahlkampfveranstaltung; das Bundesverfassungsgericht stützte seine Anordnung auf die Versammlungsfreiheit in Verbindung mit Art. 20 Abs. 3 und 19 Abs. 4 GG. Nicht behandelt: abgestufte Chancengleichheit (§ 5 Abs. 1 Satz 2–4 PartG), privatrechtlich betriebene Hallen (Einwirkungsanspruch), Hauptsacheverfahren.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Parteiengleichheit #Kommunalrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("Art. 3 und einundzwanzig", "Art. 3 und 21")
assert not re.search(r"§\n", srt) and "einundzwanzig" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
