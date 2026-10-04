"""Nachbearbeitung der Upload-Texte für Folge 143 (Kopie von meta_118.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen/Daten als Ziffern, Sprechername).
Aufruf: python3 meta_143.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Flugblätter im Terminal 1 (2003)"),
       (T("aktien"), "Wem gehört die Fraport? Der Weg durch die Instanzen"),
       (T("bind"), "Grundrechtsbindung: Art. 1 Abs. 3 GG"),
       (T("gemischt"), "Gemischtwirtschaftliche Unternehmen: mehr als 50 %"),
       (T("fraport"), "Fraport unmittelbar gebunden, private Aktionäre"),
       (T("a8"), "Versammlungsfreiheit: Art. 8 Abs. 1 GG"),
       (T("kein"), "Kein Zutrittsrecht zu beliebigen Orten"),
       (T("forum"), "Das öffentliche Forum"),
       (T("a5"), "Meinungsfreiheit: Flugblätter verteilen"),
       (T("schranke"), "Rechtfertigung: „unter freiem Himmel“, Hausrecht"),
       (T("zweck"), "Legitimer Zweck: Sicherheit statt Wohlfühlatmosphäre"),
       (T("s2b"), "Verhältnismäßigkeit im Terminal"),
       (T("erg"), "Ergebnis und Stadionverbot (mittelbare Drittwirkung)"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fraport-Urteil (BVerfGE 128, 226): Warum eine staatlich beherrschte Flughafen-AG unmittelbar an Art. 1 III GG gebunden ist – öffentliches Forum erklärt.

Der Fall: Am 11. März 2003 verteilt eine Aktivistin mit fünf weiteren Aktivisten im Terminal 1 des Frankfurter Flughafens Flugblätter zu einer bevorstehenden Abschiebung. Die Betreiberin, die Fraport AG – damals zu rund 70 % in der Hand von Land Hessen, Stadt Frankfurt und Bund –, erteilt ihr ein Flughafenverbot. Amtsgericht, Landgericht und BGH weisen ihre Klage ab. Am 22. Februar 2011 entscheidet das Bundesverfassungsgericht.

Inhalt:
– Grundrechtsbindung nach Art. 1 Abs. 3 GG (im Wortlaut): keine Flucht ins Privatrecht; gemischtwirtschaftliche Unternehmen sind gebunden, wenn die öffentliche Hand sie beherrscht – in der Regel bei mehr als der Hälfte der Anteile; keine Bindung „nach Quoten“; keine eigenen Grundrechte gegenüber Bürgern; private Aktionäre
– Versammlungsfreiheit, Art. 8 Abs. 1 GG (im Wortlaut): kein Zutrittsrecht zu beliebigen Orten (Behörden, Schwimmbad, Krankenhaus, Sicherheitsbereich, Gepäckausgabe); das öffentliche Forum; Eingriff
– Meinungsfreiheit, Art. 5 Abs. 1 Satz 1 GG: Flugblätter verteilen, kein besonderer Raumbezug
– Rechtfertigung: Versammlung im Terminal „unter freiem Himmel“ (Art. 8 Abs. 2 GG), Hausrecht (§§ 903, 1004 BGB), legitime Zwecke (Sicherheit und Funktionsfähigkeit, keine „Wohlfühlatmosphäre“), Verhältnismäßigkeit – mehr Beschränkungen als auf der Straße, aber kein pauschales Verbot
– Ergebnis und Bedeutung: mittelbare Drittwirkung bei rein Privaten (Stadionverbot)
– Klausurtipp, Prüfschema, Merksatz

Normen: Art. 1 Abs. 3, Art. 5 Abs. 1, 2, Art. 8 Abs. 1, 2 GG; §§ 903, 1004 BGB

Rechtsprechung:
– BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, BVerfGE 128, 226 (Fraport): Rn. 2, 9 f. (Sachverhalt), Rn. 46, 48 (keine Flucht ins Privatrecht), Rn. 49–55, 60 (Beherrschung, mehr als die Hälfte der Anteile, private Anteilseigner), Rn. 64–73 (öffentliches Forum, Eingriff), Rn. 76–79 („unter freiem Himmel“, Hausrecht), Rn. 86–95 (legitimer Zweck, Verhältnismäßigkeit), Rn. 97–107 (Meinungsfreiheit, Flugblätter)
– BVerfG, Beschl. v. 11.4.2018 – 1 BvR 3080/09 (Stadionverbot), Rn. 32, 41 (mittelbare Drittwirkung)

Hinweise: Dorothea und Herr Sievers sind erfundene Figuren; die realen Beteiligten werden nicht dargestellt. Der Inhalt der Flugblätter wird nicht bewertet. Den Versammlungsbegriff und den Aufbau der Grundrechtsprüfung erklären eigene Folgen. Nicht behandelt: Befugnisse der Versammlungsbehörden im Flughafen, Anzeigepflicht, Spontanversammlungen, abweichende Meinung.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#FraportUrteil #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("elfter\nMärz 2003, Terminal eins.", "11.\nMärz 2003, Terminal 1."), ("siebzig Prozent", "70 %"),
             ("zweiundzwanzigsten\nFebruar", "22.\nFebruar"), ("Sievers: ", "Herr Sievers: ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt) and "zweiundzwanzig" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
