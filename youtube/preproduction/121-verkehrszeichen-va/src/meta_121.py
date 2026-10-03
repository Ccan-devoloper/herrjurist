"""Nachbearbeitung der Upload-Texte für Folge 121 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), fachlich korrigierte Normenzeile (Bekanntgabe nach StVO, nicht § 41 III, IV VwVfG,
siehe RECHTSSTAND.md), Fallabsatz, Rechtsprechung mit Az. und Rn. (3 C 15.03 ohne Rn. → ohne Az.), Landesrecht-Hinweis
(Beispiel NRW, keine Länderliste: nur NRW geprüft), Sprechernamen in den Untertiteln, Lizenzzeile.
Aufruf: python3 meta_121.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das neue Haltverbot vor der Haustür"), (T("amt"), "Fall: Der Anruf bei der Stadt"),
       (T("frage"), "Frage und Sachverhalt"), (T("natur"), "Rechtsnatur: Allgemeinverfügung, § 35 S. 2 VwVfG"),
       (T("bekannt"), "Bekanntgabe durch Aufstellen, Wirksamkeit"), (T("zul"), "Zulässigkeit: Anfechtungsklage, Klagebefugnis"),
       (T("vorv"), "Vorverfahren und Klagefrist: 1 Jahr ab erster Begegnung"), (T("aufsch"), "Keine aufschiebende Wirkung"),
       (T("begr"), "Begründetheit: § 45 I 1 StVO, formell"), (T("wl45"), "§ 45 IX StVO: ruhender und fließender Verkehr"),
       (T("zwingend"), "Zwingend erforderlich, Ermessen"), (T("hier"), "Subsumtion und Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verkehrszeichen als Verwaltungsakt: Warum ein Halteverbotsschild eine Allgemeinverfügung nach § 35 S. 2 VwVfG ist und wie du es anfechten kannst.

Der Fall: Frau Wittmann parkt seit zwanzig Jahren vor ihrem Haus. Über Nacht steht dort ein absolutes Haltverbot. Die Stadt nennt nur „Sicherheit und Ordnung des Verkehrs“. Kann sie das Schild anfechten – und hat sie Erfolg? (Übungsfall)

Inhalt:
– Rechtsnatur: Verwaltungsakt in Form einer Allgemeinverfügung (§ 35 Satz 2 VwVfG), Dauerverwaltungsakt
– Bekanntgabe durch Aufstellen nach den Spezialregeln der StVO, Wirksamkeit (§ 43 Abs. 1 VwVfG), Sichtbarkeitsgrundsatz
– Zulässigkeit: Anfechtungsklage (§ 42 Abs. 1 VwGO), Klagebefugnis (Art. 2 Abs. 1 GG), Vorverfahren je nach Land, Jahresfrist ab der ersten Begegnung (§ 58 Abs. 2 VwGO), keine aufschiebende Wirkung (§ 80 Abs. 2 Satz 1 Nr. 2 VwGO analog), Eilantrag (§ 80 Abs. 5 VwGO)
– Begründetheit: § 45 Abs. 1 Satz 1 StVO; § 45 Abs. 9 Satz 1 StVO (zwingend erforderlich); qualifizierte Gefahrenlage nach Satz 3 nur beim fließenden Verkehr
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 35 S. 2, 43 I VwVfG; §§ 39 I, 45 I 1, IV, IX StVO; §§ 42, 58 II, 74 I 2, 80 II 1 Nr. 2 analog, 113 I 1 VwGO

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel – dort entfällt das Vorverfahren in der Regel (§ 110 Abs. 1 Satz 1 JustG NRW). In anderen Ländern kann zuerst ein Widerspruch nötig sein; bitte im Ausführungsgesetz zur VwGO deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 16 (Allgemeinverfügung, Bekanntgabe durch Aufstellen, Sichtbarkeitsgrundsatz)
– BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Rn. 14, 16, 18, 21 (Frist ab der ersten Begegnung; Dauerverwaltungsakt)
– BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 35 f. (§ 45 Abs. 9 StVO; Satz 3 nicht für den ruhenden Verkehr)
– BVerwG, Urt. v. 24.1.2019 – 3 C 7.17, Rn. 11, 13 (Parkverbot: § 45 Abs. 1 Satz 1 i. V. m. Abs. 9 Satz 1 StVO, Ermessen)
– BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 14 (sofort vollziehbar entsprechend § 80 Abs. 2 Satz 1 Nr. 2 VwGO)
– VG Münster, Urt. v. 14.11.2011 – 1 K 605/10, Rn. 18 (dritte Variante des § 35 Satz 2)
Mehr zum Abschleppen und zum Sichtbarkeitsgrundsatz: Folge 64 (Abschleppfall); zu den Merkmalen des Verwaltungsakts: Folge 44.

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#VerkehrszeichenalsVerwaltungsakt #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nWittmann:", "\nFrau Wittmann:"), ("\nBuchholz:", "\nHerr Buchholz:"), ("\nWolter:", "\nFrau Wolter:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
