"""Nachbearbeitung der Upload-Texte für Folge 098 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_098.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Ein Land deckelt die Miete"), (T("frage"), "Frage und Sachverhalt"),
       (T("einord"), "Einordnung: formelle Verfassungsmäßigkeit"), (T("wl70"), "Grundsatz: Art. 70 Abs. 1 GG"),
       (T("aus"), "Ausschließliche Gesetzgebung, Art. 71, 73 GG"), (T("konk"), "Konkurrierende Gesetzgebung: Kompetenztitel"),
       (T("wohn"), "Wohnungswesen, Föderalismusreform 2006, Art. 125a GG"),
       (T("wl72"), "Sperrwirkung, Art. 72 Abs. 1 GG"), (T("wl722"), "Erforderlichkeitsklausel, Art. 72 Abs. 2 GG"),
       (T("abw"), "Abweichungsrecht und ungeschriebene Kompetenzen"), (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: Art. 31 GG"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gesetzgebungskompetenz nach Art. 70 ff. GG: Wann darf der Bund, wann das Land ein Gesetz erlassen? Ausschließliche und konkurrierende Gesetzgebung, Sperrwirkung, Erforderlichkeitsklausel und Abweichungsrecht – als Prüfungsschema für die formelle Verfassungsmäßigkeit.

Der Fall: Ein Land beschließt, dass die Miete für frei finanzierte Wohnungen höchstens 9 € pro Quadratmeter betragen darf. Der Vermieter verlangt nach dem BGB trotzdem die Zustimmung zu einer Erhöhung auf die ortsübliche Vergleichsmiete. Durfte das Land dieses Gesetz überhaupt machen? (Übungsfall nach dem Vorbild des Berliner Mietendeckels)

Inhalt:
– Einordnung: Gesetzgebungskompetenz am Anfang der formellen Verfassungsmäßigkeit (danach Verfahren und Form)
– 1. Grundsatz: Länder, Art. 70 Abs. 1 GG
– 2. Ausschließliche Gesetzgebung des Bundes, Art. 71, 73 GG
– 3. Konkurrierende Gesetzgebung, Art. 72, 74 GG: a) Kompetenztitel nach dem Hauptzweck (Miethöhe = bürgerliches Recht, Art. 74 Abs. 1 Nr. 1 GG; Wohnungswesen seit der Föderalismusreform 2006 Ländersache; Fortgeltung nach Art. 125a Abs. 1 GG), b) Sperrwirkung nach Art. 72 Abs. 1 GG (§§ 556 bis 561 BGB abschließend), c) Erforderlichkeitsklausel nach Art. 72 Abs. 2 GG nur für die dort genannten Nummern, d) Abweichungsrecht nach Art. 72 Abs. 3 GG
– 4. Ungeschriebene Kompetenzen (Sachzusammenhang, Annex, Natur der Sache)
– Ergebnis: Landesgesetz formell verfassungswidrig und nichtig
– Klausurtipp: zuerst die Kompetenz, nicht vorschnell Art. 31 GG
– Klausurschema und Merksatz

Rechtsprechung:
– BVerfG, Beschl. v. 25.3.2021 – 2 BvF 1/20, 2 BvL 4/20, 2 BvL 5/20 (Berliner Mietendeckel, BVerfGE 157, 223), Rn. 81 (keine Doppelzuständigkeit), Rn. 86 (Art. 72 Abs. 2 nur für die genannten Materien), Rn. 87, 89 (Sperrwirkung), Rn. 104 f. (Zuordnung nach dem Hauptzweck), Rn. 107 f. (Miethöhe als bürgerliches Recht), Rn. 148, 160 (§§ 556 ff. BGB abschließend), Rn. 178, 184 f. (Wohnungswesen und Föderalismusreform 2006), Rn. 186 (Nichtigkeit des ganzen Gesetzes)
– BVerfG, Urt. v. 24.10.2002 – 2 BvF 1/01 (Altenpflegegesetz, BVerfGE 106, 62), Rn. 320 f. (gleichwertige Lebensverhältnisse)

Wie ein Gesetz nach Karlsruhe kommt (abstrakte Normenkontrolle, Art. 94 Abs. 1 Nr. 2 GG), zeigt unser Video zu den Verfahrensarten des Bundesverfassungsgerichts.

Kapitel:
{kapitel}

Das Prüfungsschema ist eine Klausurkonvention. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gesetzgebungskompetenz #Staatsorganisationsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nDahlke:", "\nFrau Dahlke:"), ("\nHenke:", "\nHerr Henke:"), ("\nLandesministerin:", "\nDie Landesministerin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("neun Euro", "9 Euro"), ("zehn Euro", "10 Euro"), ("zweitausendeinundzwanzig", "2021"),
                 ("zweitausendsechs", "2006")):
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Sperrwirkung", "Mietendeckel", "Art. 74 GG"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
