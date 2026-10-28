"""Nachbearbeitung der Upload-Texte für Folge 110 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Normen der Länder
(Gaststättenrecht ist Landesrecht, VIDEOLEITLINIEN: länderneutral), Lizenzzeile; Sprechernamen und Zahlen in den Untertiteln.
Aufruf: python3 meta_110.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die Shisha-Bar nebenan"), (T("p42"), "Ausgangspunkt § 42 II VwGO: keine Adressatin"),
       (T("snt"), "Schutznormtheorie: die Kriterien"), (T("fa"), "Frage 1: Welche Norm? § 4 I 1 Nr. 3 GastG"),
       (T("fb"), "Frage 2: Schützt sie auch Einzelne?"), (T("fc"), "Frage 3: Geschützter Kreis und Gegenfall"),
       (T("tab"), "Typische drittschützende Normen"), (T("grund"), "Grundrechte nur hilfsweise; Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Schema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schutznormtheorie bei § 42 II VwGO: Wann darfst du die Genehmigung eines anderen anfechten? Drittschutz und typische drittschützende Normen.

Der Fall: Neben dem Haus von Frau Brüning eröffnet Frau Hoppe eine Shisha-Bar mit Terrasse direkt unter ihrem Schlafzimmerfenster. Die Stadt erteilt die Gaststättenerlaubnis bis Mitternacht. Darf Frau Brüning eine Erlaubnis anfechten, die gar nicht an sie gerichtet ist? (Übungsfall, Beispielland Nordrhein-Westfalen)

Inhalt:
– Ausgangspunkt § 42 Abs. 2 VwGO: Die Adressatentheorie hilft der Nachbarin nicht
– Schutznormtheorie: Die Norm muss zumindest auch einen abgrenzbaren Personenkreis schützen, der sich von der Allgemeinheit unterscheidet
– Prüfung in drei Fragen: Welche Norm? Schützt sie auch Einzelne (Wortlaut, Systematik, Zweck)? Gehört der Kläger zum geschützten Kreis?
– § 4 Abs. 1 Satz 1 Nr. 3 GastG mit § 3 Abs. 1 BImSchG und § 5 Abs. 1 Nr. 3 GastG
– Typische Normen: drittschützend ja/nein (Lärmschutz im Gaststättenrecht, § 5 Abs. 1 Nr. 1 BImSchG, Abstandsflächen, Gebietserhaltungsanspruch; nicht: Vorsorgepflicht, Maß der baulichen Nutzung in der Regel)
– Grundrechte als Schutznorm nur hilfsweise
– Klausurtipp, Schema und Merksatz

Rechtsprechung:
– BVerwG, Urt. v. 6.6.2024 – 3 C 5.23, Rn. 40, 43 (Kriterien des Drittschutzes, Anwohner)
– BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 13, 24 (Möglichkeit, „reflexartig“)
– BVerwG, Urt. v. 12.12.2019 – 8 C 3.19, Rn. 39 (§ 4 Abs. 1 Satz 1 Nr. 3 GastG drittschützend)
– OVG NRW, Beschl. v. 3.11.2015 – 4 B 652/15, Rn. 27, 32 (Nachbarschutz bei Außengastronomie)
– BVerwG, Beschl. v. 9.4.2008 – 7 B 2.08, Rn. 15 (Vorsorgepflicht nicht drittschützend)
– BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9; Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8; Urt. v. 9.8.2018 – 4 C 7.17, Rn. 14 (Baurecht)
– BVerwG, Urt. v. 21.4.2009 – 4 C 3.08, Rn. 15 (Grundrechte und einfaches Recht)

Gaststättenrecht in den Ländern (Gaststättenrecht ist seit 2006 Landesrecht; prüfe Paragrafen und Erlaubnis- oder Anzeigepflicht in deinem Land):
– Gaststättengesetz des Bundes gilt fort (Art. 125a Abs. 1 GG; Versagungsgrund § 4 Abs. 1 Satz 1 Nr. 3 GastG, Auflagen § 5 Abs. 1 Nr. 3 GastG): Bayern, Berlin, Hamburg, Mecklenburg-Vorpommern, Nordrhein-Westfalen, Rheinland-Pfalz, Schleswig-Holstein
– Eigene Landesgesetze: Baden-Württemberg (LGastG), Brandenburg (BbgGastG), Bremen (BremGastG), Hessen (HGastG), Niedersachsen (NGastG), Saarland (SGastG), Sachsen (SächsGastG), Sachsen-Anhalt (GastG LSA), Thüringen (ThürGastG)

Kapitel:
{kapitel}

Das Schema und die Formulierungen sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Schutznormtheorie #Verwaltungsprozessrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nHoppe:", "\nFrau Hoppe:"), ("\nBrüning:", "\nFrau Brüning:"), ("\nRichter:", "\nDer Richter:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace(" S. 1", " Satz 1")
for alt, neu in (("seit dreißig\n", "seit 30\n"), ("seit dreißig ", "seit 30 "), ("der drei Straßen", "der 3 Straßen")):
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
