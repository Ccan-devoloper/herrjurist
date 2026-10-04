"""Nachbearbeitung der Upload-Texte für Folge 163 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_140.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und Lizenzzeile;
Jahreszahlen und Gliederungsziffern in den Untertiteln als Ziffern.
Aufruf: python3 meta_163.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: betrunken nach dem Kneipenabend, Sachverhalt"),
       (T("p20"), "§ 20 StGB und das Koinzidenzprinzip"),
       (T("alic"), "Actio libera in causa: Ausnahme- und Tatbestandsmodell"),
       (T("echt"), "Der echte Fall: BGHSt 42, 235"),
       (T("kern"), "Tatbestandsmodell: Sich-Betrinken ist kein Führen"),
       (T("ausn2"), "Ausnahmemodell: § 20 StGB und Art. 103 Abs. 2 GG"),
       (T("offen"), "Offen gelassen: fahrlässige Tötung ohne a.l.i.c."),
       (T("p323"), "Was bleibt: Vollrausch, § 323a StGB"),
       (T("loes"), "Lösung des Falls und § 69 StGB"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""a.l.i.c. im Straßenverkehr: Warum lehnt der BGH die actio libera in causa bei §§ 315c, 316 StGB ab – und was bleibt übrig (§ 323a StGB)?

Der Fall: Leopold sitzt am Freitagabend in der Kneipe. Schon beim ersten Bier weiß er, dass er nachher selbst nach Hause fährt. Nach Mitternacht gerät er in eine Polizeikontrolle; bei Fahrtantritt war er schuldunfähig. Kann er wegen Trunkenheit im Verkehr bestraft werden? Und was gilt, wenn unterwegs ein anderer Fahrer scharf bremsen musste?

Inhalt:
– § 20 StGB im Wortlaut: Schuldfähigkeit „bei Begehung der Tat“ (Koinzidenzprinzip)
– Actio libera in causa knapp: Ausnahmemodell und Tatbestandsmodell
– Der Klassiker BGHSt 42, 235 (BGH, Urt. v. 22.8.1996 – 4 StR 217/96): Sachverhalt und Instanz
– Tatbestandsmodell scheitert: Führen beginnt erst mit dem Anfahren; Sich-Betrinken ist noch kein Führen; Verhalten statt trennbarer Erfolg
– Ausnahmemodell scheitert am Wortlaut von § 20 StGB und an Art. 103 Abs. 2 GG (Wortlaut)
– Offen gelassen: a.l.i.c. bei anderen Delikten; fahrlässige Tötung knüpft unmittelbar an das Trinken an
– Was bleibt: Vollrausch, § 323a StGB im Wortlaut (Rauschtat als Bedingung der Strafbarkeit, Strafgrenze nach Abs. 2)
– Lösung des Falls, Entziehung der Fahrerlaubnis (§ 69 Abs. 1, Abs. 2 Nr. 4 StGB), Klausurtipp, Prüfschema, Merksatz

Normen: §§ 20, 69, 222, 315c, 316, 323a StGB; Art. 103 Abs. 2 GG

Rechtsprechung:
– BGH, Urt. v. 22.8.1996 – 4 StR 217/96, BGHSt 42, 235 (Rn. 17: „Jedenfalls bei den Delikten der Straßenverkehrsgefährdung und des Fahrens ohne Fahrerlaubnis ist die Vorverlagerung der Schuld unzulässig.“; Rn. 18 f.: Tatbestandslösung, Führen eines Fahrzeugs; Rn. 22: Ausnahmemodell und Art. 103 Abs. 2 GG; Rn. 8 f.: fahrlässige Tötung; Rn. 23, 25: Vollrausch)
– BGH, Beschl. v. 19.6.2024 – 4 StR 73/24, Rn. 6 (konkrete Gefahr bei § 315c: Beinahe-Unfall)

Hinweise: Randnummern nach der HRRS-Fassung. Der Einstiegsfall ist ein vereinfachter Übungsfall; im echten BGH-Fall kamen bei dem Unglück an der Grenzkontrolle zwei Beamte ums Leben – das Video zeigt dazu keine Bilder. „Ausnahmemodell“, „Tatbestandsmodell“, „verhaltensgebundene“ und „eigenhändige Delikte“ sind Lehrbegriffe. Zu §§ 316 und 315c im Einzelnen siehe unsere Folgen zur Trunkenheit im Verkehr und zur Gefährdung des Straßenverkehrs.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ActioLiberaInCausa #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("neunzehnhundertsechsundneunzig", "1996")
srt = srt.replace("A: ", "A. ").replace("B: ", "B. ")
srt = srt.replace("Römisch eins:", "I.").replace("Römisch zwei:", "II.").replace("Römisch drei:", "III.")
srt = re.sub(r"§ 315\n\n(\d+\n[^\n]+\n)c([ ,])", r"§ 315c\2\n\n\1", srt)   # Paragraf über eine Untertitelgrenze
srt = re.sub(r"§ 323\n\n(\d+\n[^\n]+\n)a ", r"§ 323a\n\n\1", srt)
srt = srt.replace("Aus §\n316 ist", "Aus § 316\nist")
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert "Römisch" not in srt and "hundert" not in srt and "Paragraf" not in srt, re.findall(r".*(?:Römisch|hundert|Paragraf).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
