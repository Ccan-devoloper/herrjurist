"""Nachbearbeitung der Upload-Texte für Folge 101 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_101.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Nachts im Bundestag, Streit im Bundesrat"), (T("frage"), "Frage und Sachverhalt"),
       (T("einord"), "Einordnung und I. Zuständigkeit"), (T("ini"), "1. Gesetzesinitiative, Art. 76 GG"),
       (T("bt"), "2. Beschluss des Bundestages, Art. 77 Abs. 1 GG"),
       (T("brt"), "3. Bundesrat: Einspruchs- oder Zustimmungsgesetz"),
       (T("vma"), "Vermittlungsausschuss und Einspruch, Art. 77 GG"), (T("wl78"), "Zustandekommen, Art. 78 GG"),
       (T("st"), "Einheitliche Stimmabgabe, Art. 51 Abs. 3 GG"), (T("form1"), "III. Form: Ausfertigung und Verkündung, Art. 82 GG"),
       (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp: Welche Fehler machen nichtig?"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Formelle Verfassungsmäßigkeit prüfen: Kompetenz, Verfahren (Art. 76–78 GG), Form (Art. 82 GG) – und welche Verfahrensfehler ein Bundesgesetz wirklich nichtig machen.

Der Fall: Kurz vor Mitternacht beschließt der Bundestag ein zustimmungsbedürftiges Gesetz. Im Bundesrat sagt für ein Land eine Ministerin „Ja“, ein Minister „Nein“ – der Präsident wertet das als Ja. Der Bundespräsident fertigt aus, das Gesetz wird im Bundesgesetzblatt verkündet. Ist es wirksam zustande gekommen? (Übungsfall nach dem Vorbild des Zuwanderungsgesetzes)

Inhalt:
– Einordnung: formelle Verfassungsmäßigkeit mit I. Zuständigkeit, II. Verfahren, III. Form
– I. Zuständigkeit: Melde- und Ausweiswesen, Art. 73 Abs. 1 Nr. 3 GG (Details im Video zur Gesetzgebungskompetenz)
– II. 1. Gesetzesinitiative und Vorverfahren, Art. 76 GG
– II. 2. Beschluss des Bundestages, Art. 77 Abs. 1 Satz 1, Art. 42 Abs. 2 GG; Beschlussfähigkeit nach § 45 GO-BT
– II. 3. Beteiligung des Bundesrates: Einspruchs- oder Zustimmungsgesetz (z. B. Art. 84 Abs. 1 Satz 6 GG), Vermittlungsausschuss, Einspruch und Zurückweisung (Art. 77 Abs. 2–4 GG), Zustandekommen (Art. 78 GG), einheitliche Stimmabgabe (Art. 51 Abs. 3 Satz 2, Art. 52 Abs. 3 Satz 1 GG)
– III. Form: Gegenzeichnung (Art. 58 GG), Ausfertigung und Verkündung (Art. 82 Abs. 1 GG), elektronisches Bundesgesetzblatt seit 1.1.2023 (§ 2 Abs. 1 Verkündungs- und Bekanntmachungsgesetz), Inkrafttreten (Art. 82 Abs. 2 GG)
– Ergebnis: Gesetz formell verfassungswidrig und nichtig
– Klausurtipp: Geschäftsordnungsverstoß und evidenter Verfassungsverstoß
– Klausurschema und Merksatz

Rechtsprechung:
– BVerfG, Urt. v. 18.12.2002 – 2 BvF 1/02 (Zuwanderungsgesetz, BVerfGE 106, 310), Tenor und Rn. 134 (keine Zustimmung, nichtig), Rn. 139 f. (einheitliche Stimmabgabe)
– BVerfG, Beschl. v. 15.1.2008 – 2 BvL 12/01 (BVerfGE 120, 56), Rn. 71 (Verfahrensmangel führt nur bei Evidenz zur Nichtigkeit)

Kapitel:
{kapitel}

Das Prüfungsschema ist eine Klausurkonvention. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#FormelleVerfassungsmäßigkeit #Gesetzgebungsverfahren #Staatsorganisationsrecht
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nPraesident:", "\nDer Bundesratspräsident:"), ("\nHensel:", "\nFrau Hensel:"), ("\nRieger:", "\nHerr Rieger:"),
                 ("\nKaehler:", "\nFrau Kähler:")):
    srt = srt.replace(alt, neu)
for alt, neu in ((r"ersten\s+März", "1. März"), (r"ersten\s+Januar", "1. Januar"), (r"vierzehnten\s+Tag", "14. Tag"),
                 (r"vier\s+Stimmen", "4 Stimmen"), (r"binnen\s+drei\s+Wochen", "binnen 3 Wochen"),
                 (r"binnen\s+zwei\s+Wochen", "binnen 2 Wochen"), (r"sechs\s+Wochen", "6 Wochen")):
    srt = re.sub(alt, neu, srt)
assert not re.search(r"\n(Praesident|Kaehler|Hensel|Rieger):", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Zuwanderungsgesetz", "Art. 51 GG", "Bundesgesetzblatt"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
