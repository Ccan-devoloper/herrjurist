"""Nachbearbeitung der Upload-Texte für Folge 148 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_140.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung, Hinweisen und Lizenzzeile;
Beträge, Fristen und Gliederungsziffern in den Untertiteln als Ziffern.
Aufruf: python3 meta_148.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Nachts auf dem Parkplatz, Zettel, Sachverhalt"),
       (T("p142"), "§ 142 Abs. 1 StGB im Wortlaut"),
       (T("unfall"), "Unfall im Straßenverkehr"),
       (T("abs5"), "Unfallbeteiligte (Abs. 5)"),
       (T("entf"), "Wartepflicht: Wie lange muss ich warten?"),
       (T("zett"), "Warum der Zettel nicht reicht, Vorsatz"),
       (T("abs2"), "Nachträgliche Meldung (Abs. 2 und 3)"),
       (T("abs22"), "Unfall nicht bemerkt: BVerfG zu Abs. 2 Nr. 2"),
       (T("abs4"), "Tätige Reue (Abs. 4)"),
       (T("rws"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Unfallflucht § 142 StGB: Wer ist Unfallbeteiligter, wie lange muss man warten, warum reicht der Zettel nicht – und was gilt bei tätiger Reue?

Der Fall: Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus und schrammt dabei das Auto von Bernhard. Niemand ist zu sehen. Sie klemmt einen Zettel mit Name und Telefonnummer unter den Scheibenwischer und fährt sofort weiter. Hat sie sich wegen unerlaubten Entfernens vom Unfallort strafbar gemacht – und wie lange hätte sie warten müssen?

Inhalt:
– § 142 Abs. 1 StGB im Wortlaut: Anwesenheit (Nr. 1) oder Wartepflicht (Nr. 2)
– Unfall im Straßenverkehr: Parkplatz, Grenze des völlig belanglosen Schadens
– Unfallbeteiligte nach Abs. 5
– Wartepflicht: keine feste Minutenzahl, es kommt auf die Umstände an (Beispiel OLG Dresden: mindestens 10 Minuten)
– Warum der Zettel weder das Warten noch die nachträgliche Meldung nach Abs. 2 und 3 ersetzt
– Abs. 2 Nr. 2: Wer den Unfall nicht bemerkt, entfernt sich nicht „berechtigt oder entschuldigt“ (BVerfG, Analogieverbot)
– Tätige Reue nach Abs. 4: Parkunfall, nicht bedeutender Sachschaden, Meldung binnen 24 Stunden
– Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: § 142 StGB; Art. 103 Abs. 2 GG

Rechtsprechung:
– BVerfG, Beschl. v. 19.3.2007 – 2 BvR 2273/06, Rn. 18, 20 (unvorsätzliches Entfernen nicht von § 142 Abs. 2 Nr. 2 erfasst)
– BGH, Beschl. v. 15.11.2010 – 4 StR 413/10, Rn. 4 f.
– BGH, Urt. v. 15.11.2001 – 4 StR 233/01 (BGHSt 47, 158), Rn. 7 (Unfall im Straßenverkehr)
– OLG Naumburg, Beschl. v. 6.5.2024 – 1 ORs 38/24 (Parkplatz; völlig belangloser Schaden)
– OLG Dresden, Urt. v. 17.4.2018 – 6 U 1480/17 (Zivilsenat; Wartezeit nach den Umständen, Mindestwartezeit 10 Minuten im entschiedenen Fall)

Hinweise: Der Fall ist ein vereinfachter Übungsfall. Eine feste Wartezeit gibt es nicht; die Beispielzeit stammt aus einem Einzelfall. Ob die Strafe nach Abs. 4 gemildert oder von Strafe abgesehen wird, entscheidet das Gericht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026; § 142 unverändert).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Unfallflucht #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("vierhundert\nEuro", "400\nEuro")
srt = re.sub(r"vierhundert(\n\n\d+\n[^\n]+\n)Euro", r"400\1Euro", srt)   # Betrag über eine Untertitelgrenze
srt = srt.replace("zehn Minuten", "10 Minuten")
srt = srt.replace("vierundzwanzig Stunden", "24 Stunden")
srt = srt.replace("Römisch eins,", "I.").replace("Römisch zwei und drei:", "II. und III.:").replace("Römisch vier:", "IV.:")
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert "Römisch" not in srt and "hundert" not in srt and "Paragraf" not in srt and "vierundzwanzig" not in srt, \
    re.findall(r".*(?:Römisch|hundert|Paragraf|vierundzwanzig).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
