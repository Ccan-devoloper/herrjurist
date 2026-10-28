"""Nachbearbeitung der Upload-Texte für Folge 269 (nach meta_266.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen der geprüften Länder, Rechtsprechung mit
Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Zahlen als Ziffern).
Aufruf: python3 meta_269.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Zwergenweitwurf in der Diskothek"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("begriff"), "Begriff: öffentliche Ordnung"),
       (T("unbest"), "Zu unbestimmt? Und in welchen Ländern?"),
       (T("zw"), "Klassiker: Zwergenweitwurf"),
       (T("pro"), "Würde trotz Einwilligung?"),
       (T("ld"), "Klassiker: Laserdrome"),
       (T("eu"), "Unionsrecht: Art. 56 AEUV"),
       (T("eng"), "EuGH Omega und Gegenfall"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Öffentliche Ordnung als Schutzgut im Polizei- und Ordnungsrecht: Definition und Kritik, Länderunterschiede, Zwergenweitwurf (Menschenwürde trotz Einwilligung?) und Laserdrome – EuGH Omega zur Dienstleistungsfreiheit (Art. 56 AEUV). Mit Klausurtipp, Schema und Merksatz.

Der Fall: Eine Diskothek in Nordrhein-Westfalen wirbt mit einem „Zwergenweitwurf“. Der kleinwüchsige Artist Herr Mehring macht freiwillig und gegen Bezahlung mit; es ist sein Beruf. Das Ordnungsamt untersagt die Veranstaltung: Sie verletze die Menschenwürde und gefährde die öffentliche Ordnung. Darf die Behörde verbieten, obwohl alle einverstanden sind?

Inhalt:
– Begriff der öffentlichen Ordnung (BVerfGE 69, 315 [352]) und Abgrenzung zur öffentlichen Sicherheit
– Bestimmtheitsbedenken und die Antwort des Bundesverfassungsgerichts
– Nicht jedes Land kennt das Schutzgut: Schleswig-Holstein strich es 1992
– Zwergenweitwurf: VG Neustadt 1992 (Gewerberecht, gute Sitten), Art. 1 Abs. 1 GG, Argumente beider Seiten
– Laserdrome: Verbot des „spielerischen Tötens“ in Bonn, EuGH Omega
– Unionsrecht: Art. 56 AEUV, Rechtfertigung aus Gründen der öffentlichen Ordnung (Art. 52 Abs. 1, Art. 62 AEUV)
– Klausurtipp, Schema, Merksatz

Normen (Wortlaut am Landesportal, auf gesetze-im-internet.de bzw. in der EU-Veröffentlichung geprüft am 8. Oktober 2026):
– Art. 1 Abs. 1, Art. 12 Abs. 1 GG; § 33a GewO
– Nordrhein-Westfalen: § 14 Abs. 1 OBG NRW, § 8 Abs. 1 PolG NRW
– Niedersachsen: §§ 11, 2 Nr. 1 NPOG
– Sachsen: § 12 Abs. 1 SächsPVDG, Legaldefinition § 4 Nr. 2 SächsPVDG
– Brandenburg: § 10 Abs. 1 BbgPolG
– Art. 56, 52 Abs. 1, 62 AEUV
Schleswig-Holstein hat die öffentliche Ordnung 1992 aus dem Landesverwaltungsgesetz gestrichen (Landtags-Drucksache 16/2115). Die Landesportale der übrigen Länder waren am Prüftag nicht abrufbar; ob und unter welcher Nummer dein Land die öffentliche Ordnung schützt, bitte am Landesrecht prüfen.

Rechtsprechung und Quellen:
– EuGH, Urt. v. 14.10.2004 – C-36/02 (Omega), Rn. 3–7, 11 f., 25, 28–41
– BVerfG, Beschl. v. 14.5.1985 – 1 BvR 233, 341/81 (Brokdorf), BVerfGE 69, 315 (352)
– VG Neustadt, Beschl. v. 21.5.1992 – 7 L 1271/92, NVwZ 1993, 98 (Zwergenweitwurf; Volltext nicht online, wiedergegeben nach Sekundärquellen)
– Schlussanträge GA Stix-Hackl, C-36/02, Nr. 78, 94 (dort auch der UN-Menschenrechtsausschuss zu einem Verbot in Frankreich, 2002)
– Schleswig-Holsteinischer Landtag, Drucksache 16/2115 (2008)

Hinweise: Frau Leuschner, Frau Bredemeier und Herr Mehring sind erfundene Figuren. Mehr dazu: Folge 213 (öffentliche Sicherheit), Folge 257 (konkrete Gefahr), Folge 266 (Generalklausel und Spezialbefugnis).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#Polizeirecht #Menschenwürde #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+[a-z]?)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("zweihundertdreizehn;", "213;"), ("zweihundertdreizehn.", "213."), ("dazu Folge\n213.", "dazu\nFolge 213.")]:
    srt = srt.replace(alt, neu)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["öffentliche Ordnung Polizeirecht", "Art. 56 AEUV", "Dienstleistungsfreiheit"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
