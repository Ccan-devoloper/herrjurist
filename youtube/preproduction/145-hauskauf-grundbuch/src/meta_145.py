"""Nachbearbeitung der Upload-Texte für Folge 145 (Kopie von meta_139.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Sprecherbezeichnung und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_145.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Ute und Joachim bei der Notarin"),
       (T("sv"), "Sachverhalt und Aufbau in drei Schritten"),
       (T("k1"), "1. Kaufvertrag: notarielle Form, § 311b Abs. 1 BGB"),
       (T("heil"), "Heilung und Trennungsprinzip"),
       (T("a1"), "2. Auflassung, § 925 Abs. 1 BGB"),
       (T("w9252"), "Bedingungsfeindlich: § 925 Abs. 2 BGB"),
       (T("sofa"), "Eigentumsvorbehalt? Beim Haus nicht"),
       (T("e1"), "3. Eintragung, § 873 Abs. 1 BGB"),
       (T("vorm"), "Bis zur Eintragung: Vormerkung und Fälligkeit"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: Prüfungsreihenfolge"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Auflassung und Eintragung (§§ 873, 925 BGB): Wie wird Grundeigentum erworben, warum braucht der Kaufvertrag den Notar (§ 311b I BGB) und ab wann gehört euch das Haus?

Der Fall: Ute und Joachim kaufen von Herrn Ackermann ein Haus. Bei der Notarin wird der Kaufvertrag beurkundet, im selben Termin erklären alle die Auflassung. Herr Ackermann möchte zuerst, dass das Eigentum erst nach Zahlung übergeht – die Notarin winkt ab. Wochen später zahlen die beiden, danach werden sie ins Grundbuch eingetragen. Ab wann gehört ihnen das Haus?

Inhalt:
– 1. Kaufvertrag: notarielle Beurkundung (§ 311b Abs. 1 S. 1 BGB), Nichtigkeit bei Formmangel (§ 125 S. 1 BGB), Heilung (§ 311b Abs. 1 S. 2 BGB)
– Trennungsprinzip: Der Kaufvertrag verpflichtet nur
– 2. Auflassung (§ 925 Abs. 1 BGB): gleichzeitige Anwesenheit vor einer zuständigen Stelle, Vertretung möglich
– Bedingungsfeindlichkeit (§ 925 Abs. 2 BGB) und der Kontrast zum Eigentumsvorbehalt bei beweglichen Sachen
– 3. Eintragung ins Grundbuch (§ 873 Abs. 1 BGB); Auflassungsvormerkung (§ 883 BGB) und Fälligkeitsmitteilung nur im Überblick
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 311b I, 125, 873, 925, 883 BGB

Rechtsprechung:
– BGH, Urt. v. 14.9.2018 – V ZR 213/17, Rn. 12–14, 20 f. (Zweck der Beurkundung; Auflassung heute regelmäßig mit dem Kaufvertrag; Eigentumsverschaffung erst mit Eintragung; Vorlagensperre statt Bedingung, § 925 Abs. 2 BGB)
– BGH, Beschl. v. 13.2.2020 – V ZB 3/16, Rn. 25 (Auflassung bei gleichzeitiger Anwesenheit vor dem Notar; Bindung nach § 873 Abs. 2 BGB)
– BGH, Urt. v. 27.5.2020 – XII ZR 107/17, Rn. 19 (Auflassungsvollmacht)
– BGH, Beschl. v. 22.10.2015 – V ZB 126/14, Rn. 10 (sachenrechtliche Zuordnung braucht in erhöhtem Maße Rechtssicherheit und Rechtsklarheit)

Hinweise: Wie lange es bis zur Eintragung dauert und wann der Kaufpreis fällig wird, regelt der Einzelfall bzw. der Kaufvertrag. Die Grundlagen zu Trennungs- und Abstraktionsprinzip erklärt Folge 5, den Eigentumsvorbehalt Folge 139, den gutgläubigen Erwerb vom Nichtberechtigten Folge 76; die Vormerkung bekommt eine eigene Folge. Prüfungsreihenfolge und Klausurschema sind Klausurkonvention.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Auflassung #Sachenrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nAckermann: ", "\nHerr Ackermann: ")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
