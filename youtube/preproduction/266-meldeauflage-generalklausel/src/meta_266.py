"""Nachbearbeitung der Upload-Texte für Folge 266 (nach meta_257.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen der geprüften Länder, Rechtsprechung mit
Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Zahlen als Ziffern).
Aufruf: python3 meta_266.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Meldung auf der Polizeiwache"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("egl"), "Ermächtigungsgrundlage und Sperrwirkung"),
       (T("tni"), "Eigene Meldeauflage? Länder im Vergleich"),
       (T("wl8"), "Die Generalklausel"),
       (T("trag"), "Grundrechte: Art. 2 und Art. 11 GG"),
       (T("wes"), "Braucht es eine eigene Befugnis?"),
       (T("pass"), "Abgrenzung: § 10 Passgesetz"),
       (T("ausl"), "Gegenfall: Spiel im Ausland"),
       (T("tb"), "Tatbestand: konkrete Gefahr"),
       (T("vh"), "Verhältnismäßigkeit und Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Polizeiliche Generalklausel: Darf die Polizei einen gewaltbereiten Fußballfan verpflichten, sich am Spieltag auf der Wache zu melden? Sperrwirkung eigener Meldeauflagen, Tragfähigkeit der Generalklausel nach dem Bundesverwaltungsgericht, Abgrenzung zu § 10 Passgesetz und Verhältnismäßigkeit – Schema für die Klausur.

Der Fall: Samstag, 15 Uhr, eine Polizeiwache in Nordrhein-Westfalen. Herr Schütte wurde zweimal wegen Körperverletzung bei Auswärtsspielen verurteilt, seine Gruppe hat sich zu Schlägereien verabredet. Die Polizei verpflichtet ihn, sich an den nächsten drei Auswärtsspieltagen um 15 Uhr zu melden. Darf sie das – obwohl das Polizeigesetz die Meldeauflage gar nicht nennt?

Inhalt (Schema):
– Ermächtigungsgrundlage: Spezialbefugnis vor Generalklausel (Sperrwirkung)
– Länder im Vergleich: eigene Meldeauflage oder Generalklausel
– Trägt die Generalklausel den Eingriff? Art. 2 Abs. 1, Art. 11 GG, Wesentlichkeit
– Abgrenzung zu § 10 PassG: Zweck der Maßnahme
– Tatbestand: konkrete Gefahr, Prognose auf Tatsachen, Verhaltensstörer
– Ermessen und Verhältnismäßigkeit, Gefährderansprache als milderes Mittel
– Klausurtipp, Schema, Merksatz

Normen (Wortlaut am Landesportal bzw. auf gesetze-im-internet.de geprüft am 8. Oktober 2026):
– Nordrhein-Westfalen: keine eigene Meldeauflage; Generalklausel § 8 Abs. 1 PolG NRW, Zitiergebot § 7 PolG NRW, Verhältnismäßigkeit § 2 PolG NRW
– Niedersachsen: Meldeauflage § 16a NPOG (Gefährderansprache § 12a NPOG, Generalklausel § 11 NPOG)
– Sachsen: Meldeauflage § 20 SächsPVDG (Generalklausel § 12 Abs. 1 SächsPVDG)
– Brandenburg: Meldeauflage § 15a BbgPolG (Generalklausel § 10 Abs. 1 BbgPolG)
– Bund: § 10 Abs. 1, § 7 Abs. 1 Nr. 1 PassG (Ausreiseuntersagung); Art. 2 Abs. 1, Art. 11 GG
Die übrigen Länder regeln Generalklausel und ggf. Meldeauflage in ihrem Polizei- bzw. Ordnungsgesetz unter eigener Nummer; bitte am Landesrecht prüfen.

Rechtsprechung:
– BVerwG, Urt. v. 25.7.2007 – 6 C 39.06, BVerwGE 129, 142, Rn. 28 f., 33–36, 41, 43, 45 (Meldeauflage auf Grundlage der Generalklausel; Verhältnis zum Passgesetz)
– VG Düsseldorf, Beschl. v. 20.6.2024 – 18 L 1554/24, Rn. 15, 58 f. (NRW ohne eigene Meldeauflage)
– VG Gelsenkirchen, Beschl. v. 3.5.2023 – 17 L 615/23, Rn. 5, 7 (Zweck: Ausreise oder Straftaten verhindern)
– VG Köln, Urt. v. 12.2.2020 – 10 K 12258/17, Rn. 27, 35 (Ausreiseuntersagung, Ansehen Deutschlands)
– VG Minden, Urt. v. 14.5.2018 – 11 K 730/17, Rn. 32, 34, 41 f. (Prognose, Gefährderansprache, Meldeort)
– OVG NRW, Beschl. v. 22.8.2016 – 5 A 2532/14, Rn. 26 (Gefährderansprache und Grundrechtseingriff)

Hinweise: Herr Schütte, Polizistin Feddersen und Wachleiter Rabe sind erfundene Figuren; Verein und Spielorte sind nicht benannt. Mehr dazu: Folge 077 (Standardmaßnahme vor Generalklausel), Folge 257 (konkrete Gefahr), Folge 213 (Schutzgüter der öffentlichen Sicherheit).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Polizeirecht #Generalklausel #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+[a-z]?)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("siebenundsiebzig.", "077."), ("Folge 77.", "Folge 077."), ("zweihundertsiebenundfünfzig.", "257."),
                 ("zweihundertdreizehn.", "213.")]:
    srt = srt.replace(alt, neu)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Meldeauflage Fußball", "§ 10 PassG", "Sperrwirkung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
