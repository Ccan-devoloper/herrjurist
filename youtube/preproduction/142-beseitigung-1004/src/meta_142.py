"""Nachbearbeitung der Upload-Texte für Folge 142 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_140.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Landesrecht aller Länder
(länderneutral, VIDEOLEITLINIEN), Hinweisen und Lizenzzeile; Zahlen und Gliederungsziffern in den Untertiteln als Ziffern.
Aufruf: python3 meta_142.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Äste über der Garage, Sachverhalt"),
       (T("p1004"), "§ 1004 Abs. 1 S. 1 BGB im Wortlaut, 4 Prüfungspunkte"),
       (T("eig"), "Eigentum und Beeinträchtigung"),
       (T("stoer"), "Störer: Handlungs- oder Zustandsstörer"),
       (T("gegen"), "Gegenfall: Laub vom Baum selbst"),
       (T("duld"), "Duldungspflicht: § 910 Abs. 2 statt § 906 BGB"),
       (T("verj"), "Verjährung"),
       (T("sh"), "Selbsthilferecht § 910 BGB"),
       (T("neben"), "Verhältnis zu § 1004, Baumschutz, Kosten"),
       (T("unt"), "Unterlassungsanspruch"),
       (T("erg"), "Ergebnis mit Fristsetzung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 1004 BGB: Wann kannst du Beseitigung und Unterlassung verlangen und wann musst du dulden? Am Fall der Äste vom Nachbargrundstück auf deinem Garagendach – mit Selbsthilferecht aus § 910 BGB.

Der Fall: Franziska wohnt in Nordrhein-Westfalen. Der große Ahorn ihrer Nachbarin Rosemarie steht 4 m von der Grenze entfernt, seine Äste ragen seit dem letzten Sommer über das Garagendach, und im Herbst verstopft das Laub die Dachrinne. Rosemarie meint, Laub im Herbst sei ganz normal. Kann Franziska den Rückschnitt verlangen – oder selbst zur Astschere greifen?

Inhalt:
– § 1004 Abs. 1 S. 1 BGB im Wortlaut, § 903 BGB, die vier Prüfungspunkte
– Eigentum und Beeinträchtigung (nicht durch Besitzentziehung, dafür § 985 BGB)
– Störer: Handlungs- und Zustandsstörer; Naturereignisse und ordnungsgemäße Bewirtschaftung
– Gegenfall: Laub vom Baum selbst bei eingehaltenem Grenzabstand; kein Ausgleich analog § 906 Abs. 2 S. 2 BGB
– Duldungspflicht (§ 1004 Abs. 2 BGB): beim Überhang allein § 910 Abs. 2 BGB, nicht § 906 BGB – Ortsüblichkeit spielt keine Rolle
– Verjährung (§§ 195, 199 BGB) und Zwischenergebnis
– Selbsthilferecht § 910 BGB im Wortlaut: Frist, Verhältnis zu § 1004 BGB, keine Verjährung, nur Zweige, Baumschutzsatzung, Kosten
– Unterlassungsanspruch (§ 1004 Abs. 1 S. 2 BGB), Ergebnis mit Fristsetzung, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 903, 906, 910, 1004, 195, 199 BGB; § 41 NachbG NRW

Rechtsprechung:
– BGH, Urt. v. 14.6.2019 – V ZR 102/18, Leitsatz, Rn. 5, 7–10, 12, 14 f., 17 (Douglasie: Duldungspflicht beim Überhang allein nach § 910 Abs. 2 BGB; § 910 und § 1004 gleichrangig nebeneinander; Störer, wer Zweige hinüberwachsen lässt)
– BGH, Urt. v. 20.9.2019 – V ZR 218/18, Rn. 8 f., 13, 15, 18 f., 29 f. (Birken: Störer bei Naturereignissen nur ohne ordnungsgemäße Bewirtschaftung; Grenzabstand eingehalten – kein Ausgleich nach § 906 Abs. 2 S. 2 BGB)
– BGH, Urt. v. 11.6.2021 – V ZR 234/19, Rn. 6, 9 f., 15, 29 („Kiefernfall“: Selbsthilferecht verjährt nicht, nur Zweige, Beweislast der Baumeigentümerin, Naturschutzrecht)
– BGH, Urt. v. 22.2.2019 – V ZR 136/18, Rn. 10, 12, 15 (§ 910 Abs. 2 gilt für den Beseitigungsanspruch; Verjährung)
– BGH, Urt. v. 23.3.2023 – V ZR 67/22, Rn. 10 (Ersatz der Beseitigungskosten bei Selbstvornahme)

Landesrecht (Grenzabstände für Bäume; im Video als Beispiel § 41 NachbG NRW – die Abstände unterscheiden sich stark): BW § 16 NRG · BY Art. 47 AGBGB · BE § 27 NachbG Bln · BB § 37 BbgNRG · HE § 38 NachbRG · NI § 50 NNachbG · NRW § 41 NachbG NRW · RP § 44 LNRG · SL § 44 NachbG · SN § 9 SächsNRG · ST § 34 NbG · SH § 37 NachbG · TH § 44 ThürNRG · HB, HH und MV haben kein Nachbarrechtsgesetz mit Pflanzabständen. Bitte im jeweiligen Landesgesetz nachlesen.

Hinweise: „Handlungs-“ und „Zustandsstörer“ sind Lehrbuchbegriffe; der BGH fragt bei Naturereignissen, ob das Grundstück ordnungsgemäß bewirtschaftet wird. Vor einem Rückschnitt können Baumschutzsatzungen und das Naturschutzrecht Grenzen ziehen. Das Herausgabe-Video zu § 985 BGB ist die Voraussetzung zu dieser Folge.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#1004BGB #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in (("vier Meter", "4 Meter"), ("vier Punkte", "4 Punkte"), ("drei Jahre", "3 Jahre"), ("vier Wochen", "4 Wochen"),
             ("Römisch eins:", "I."), ("Römisch zwei:", "II."), ("Römisch drei:", "III.")):
    srt = srt.replace(a, b)
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert "Römisch" not in srt and "hundert" not in srt and "Paragraf" not in srt, re.findall(r".*(?:Römisch|hundert|Paragraf).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
