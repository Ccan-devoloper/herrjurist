"""Nachbearbeitung der Upload-Texte für Folge 120 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen und Ziffern in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_120.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Drei Mitbewohner, eine Stromrechnung"), (T("frage"), "Frage und Sachverhalt"),
       (T("eben"), "Zwei Ebenen: Außen- und Innenverhältnis"), (T("w421"), "Entstehen der Gesamtschuld, § 421 BGB"),
       (T("p427"), "Vertrag (§ 427), Gesetz (§ 840 Abs. 1) und Gleichstufigkeit"),
       (T("p422"), "Wirkung der Erfüllung, §§ 422, 425 BGB"), (T("w426"), "Ausgleich nach § 426 Abs. 1 Satz 1 BGB"),
       (T("w426s2"), "Ausfallhaftung, § 426 Abs. 1 Satz 2 BGB"), (T("w426b"), "Legalzession, § 426 Abs. 2 BGB"),
       (T("rech"), "Die Rechnung und das Ergebnis"), (T("tipp"), "Klausurtipp: Regress auf beiden Wegen"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gesamtschuld nach §§ 421–426 BGB: Der Gläubiger holt sich alles von einem – und dann? Außenverhältnis, Ausgleich nach § 426 Abs. 1 BGB, Ausfallhaftung und die Legalzession nach § 426 Abs. 2 BGB, mit Rechnung und Klausurschema.

Der Fall: Insa, Lars und Rieke wohnen in einer WG, alle drei haben den Stromvertrag unterschrieben. Rieke ist ausgezogen und zahlungsunfähig. Die Jahresabrechnung ergibt 900 Euro Nachzahlung – und der Versorger verlangt alles von Insa. Insa zahlt. Lars will ihr nur 300 Euro erstatten. Zu Recht?

Inhalt:
– Zwei Ebenen: Außenverhältnis (Gläubiger – Schuldner) und Innenverhältnis (Ausgleich untereinander)
– Entstehen der Gesamtschuld: Wortlaut § 421 Satz 1 BGB, gemeinsamer Vertrag (§ 427 BGB), Gesetz (z. B. § 840 Abs. 1 BGB), Gleichstufigkeit
– Wirkung der Erfüllung (§ 422 Abs. 1 BGB) und Einzelwirkung anderer Tatsachen (§ 425 BGB)
– Ausgleichsanspruch: Wortlaut § 426 Abs. 1 Satz 1 BGB, gleiche Anteile, soweit nichts anderes bestimmt ist
– Ausfallhaftung: Wortlaut § 426 Abs. 1 Satz 2 BGB
– Legalzession: Wortlaut § 426 Abs. 2 Satz 1 BGB, Sicherheiten über §§ 412, 401 BGB
– Absatz 1 und Absatz 2 als zwei selbständige Anspruchsgrundlagen
– Rechnung im Fall: Lars schuldet Insa 450 Euro
– Klausurtipp: Regress auf beiden Wegen, Einwendungen (§§ 412, 404 BGB), Verjährung getrennt, Befreiungsanspruch vor der Zahlung
– Klausurschema und Merksatz

Normen: §§ 401, 404, 412, 421, 422, 425, 426, 427, 840 Abs. 1 BGB

Rechtsprechung:
– BGH, Urt. v. 22.12.2011 – VII ZR 7/11, Rn. 12, 15, 18 (Gesamtschuld, Gleichstufigkeit: keiner haftet nur subsidiär oder vorläufig)
– BGH, Urt. v. 3.2.2010 – XII ZR 53/08, Rn. 9 (gemeinsamer Mietvertrag: Gesamtschuld nach § 427 BGB; anderweitige Bestimmung im Innenverhältnis)
– BGH, Urt. v. 17.3.2022 – IX ZR 216/20, Rn. 13, 19 (Legalzession lässt den Anspruch unverändert; Ausgleichsanspruch und übergegangene Forderung selbständig nebeneinander, Verjährung und Einreden getrennt)
– BGH, Versäumnisurt. v. 20.3.2012 – XI ZR 234/11, Rn. 20 (originärer Ausgleichsanspruch neben dem übergeleiteten Anspruch)
– BGH, Urt. v. 8.11.2016 – VI ZR 200/15, Rn. 11 (Ausgleichsanspruch entsteht mit der Gesamtschuld, zunächst als Mitwirkungs- und Befreiungsanspruch)

Kapitel:
{kapitel}

Das Prüfungsschema ist eine Klausurkonvention. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gesamtschuld #Schuldrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nVersorger:", "\nStromversorger:")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("neunhundert Euro", "900 Euro"), ("vierhundertfünfzig Euro", "450 Euro"),
                 ("dreihundert Euro", "300 Euro"), ("vierhundertfünfzig", "450"), ("dreihundert", "300"),
                 ("hundertfünfzig", "150"), ("neunhundert", "900")):
    srt = srt.replace(alt, neu)
for alt, neu in (("eins", "I."), ("zwei", "II.")):
    srt = re.sub(r"Römisch(\s)" + alt, r"\g<1>" + neu, srt)
srt = re.sub(r"(^|\n) (I|II)\.", r"\1\2.", srt)
srt = re.sub(r"\b(I|II)\.:", r"\1.", srt).replace(".  ", ". ")
assert "Römisch" not in srt
assert not re.search(r"§\n", srt)
assert "hundert" not in srt, re.findall(r".{20}hundert.{20}", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Gesamtschuld", "§ 421 BGB", "Ausfallhaftung § 426 BGB", "Gesamtschuldnerausgleich Rechnung"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
