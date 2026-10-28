"""Nachbearbeitung der Upload-Texte für Folge 158 (nach meta_149.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Beträge).
Aufruf: python3 meta_158.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Nachbar ohne Fahrerlaubnis, Sachverhalt"),
       (T("norm"), "§ 823 Abs. 2 BGB im Wortlaut"),
       (T("aufbau"), "Aufbau in sechs Schritten"),
       (T("sg"), "I. Schutzgesetz: Art. 2 EGBGB und BGH-Formel"),
       (T("klass"), "Klassiker §§ 223, 263 StGB; Schutznormtheorie"),
       (T("p21"), "§ 21 StVG als Schutzgesetz"),
       (T("sb"), "II. Schutzbereich: persönlich und sachlich"),
       (T("verst"), "III. Verstoß, IV. Rechtswidrigkeit"),
       (T("vs"), "V. Verschulden, § 823 Abs. 2 S. 2 BGB"),
       (T("sd"), "VI. Schaden, Kausalität, §§ 249 ff. BGB"),
       (T("vort"), "Vorteil: reiner Vermögensschaden"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 823 II BGB im Schema: Wann ist eine Norm Schutzgesetz und wie prüfst du Schutzbereich und Verschulden? Am Nachbarn, der ohne Führerschein dein Auto beschädigt.

Der Fall: Hiltrud hat ihr Auto am Straßenrand einer Wohnstraße geparkt. Ihr Nachbar Burkhard hat keine Fahrerlaubnis, will aber sein eigenes Auto umparken. Er setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich beim Rangieren und streift Hiltruds Auto. Die Reparatur kostet 900 €. Hilft es Hiltrud, dass Burkhard ohne Fahrerlaubnis gefahren ist?

Inhalt:
– § 823 Abs. 2 BGB (im Wortlaut): Schutzgesetz und Verschulden nach Satz 2
– I. Schutzgesetz: jede Rechtsnorm (Art. 2 EGBGB, im Wortlaut); BGH-Formel „zumindest auch“ zum Schutz des Einzelnen; kein bloßer Reflex; Klassiker §§ 223, 263 StGB; Abgrenzung zur Schutznormtheorie
– § 21 Abs. 1 Nr. 1 StVG und § 2 Abs. 1 StVG (im Wortlaut): Fahren ohne Fahrerlaubnis als Schutzgesetz
– II. Schutzbereich: persönlich und sachlich
– III. Verstoß, IV. Rechtswidrigkeit, V. Verschulden (subjektiver Tatbestand des Schutzgesetzes), VI. Schaden und Kausalität, §§ 249 ff. BGB
– Vorteil von Abs. 2: auch reine Vermögensschäden, etwa beim Betrug
– Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: § 823 Abs. 1, 2 BGB; Art. 2 EGBGB; §§ 2, 7, 21 StVG; §§ 223, 263 StGB; § 249 BGB

Rechtsprechung:
– BGH, Urt. v. 26.6.2023 – VIa ZR 335/21, Rn. 20, 37 f. (Schutzgesetzbegriff; Verschulden nach dem subjektiven Tatbestand des Schutzgesetzes)
– BGH, Urt. v. 23.7.2019 – VI ZR 307/18, Rn. 12, 14 (kein bloßer Reflex; persönlicher und sachlicher Schutzbereich)
– BGH, Urt. v. 2.12.2010 – IX ZR 41/10, Rn. 13 (§ 823 Abs. 2 BGB, § 223 StGB)
– BGH, Urt. v. 15.11.2011 – VI ZR 4/11, Rn. 9, 13 (§ 823 Abs. 2 BGB, § 263 StGB, Vermögensschaden)
– BGH, Urt. v. 5.4.2018 – III ZR 211/17, Rn. 19 (Vermögen als solches nicht von § 823 Abs. 1 BGB geschützt)

Hinweise: Dass § 21 StVG ein Schutzgesetz ist, wird im Video unter die BGH-Formel subsumiert; ob der Schaden gerade auf der fehlenden Fahrbefähigung beruhen muss, bleibt offen, weil im Fall ein Fahrfehler den Schaden verursacht hat. Eine Fahrerlaubnis braucht nur, wer auf öffentlichen Straßen fährt (§ 2 Abs. 1 StVG). Nicht behandelt: Mithaftung aus der Betriebsgefahr des geparkten Autos, Schadensumfang im Einzelnen, Verschuldensvermutung. Das Schema zu § 823 Abs. 1 BGB zeigt die Folge zum Deliktsrecht, die Halterhaftung nach § 7 StVG die Folge zur Halterhaftung, die Schutznormtheorie die Folge dazu im Öffentlichen Recht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Schutzgesetz #Deliktsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier|fünf|sechs):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV.", "fünf": "V.", "sechs": "VI."}[m.group(1)]
             + m.group(2), srt)
for a, b in [("neunhundert Euro", "900 Euro")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
