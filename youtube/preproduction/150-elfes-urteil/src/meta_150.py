"""Nachbearbeitung der Upload-Texte für Folge 150 (nach meta_146.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Daten als Ziffern, Sprechername, Gliederungsziffern).
Aufruf: python3 meta_150.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Reisepass versagt"),
       (T("elfes"), "Der echte Fall: Wilhelm Elfes, 1953"),
       (T("norm"), "§ 7 PaßG 1952 und Verfassungsbeschwerde"),
       (T("urteil"), "Art. 11 GG: Ausreise nicht erfasst"),
       (T("a2"), "Art. 2 Abs. 1 GG: allgemeine Handlungsfreiheit"),
       (T("kern"), "Kernbereich oder umfassende Handlungsfreiheit?"),
       (T("auff"), "Das Auffanggrundrecht"),
       (T("schranke"), "Schranke: verfassungsmäßige Ordnung"),
       (T("passg"), "Passgesetz: sonstige erhebliche Belange"),
       (T("erg"), "Ergebnis"),
       (T("tor"), "Bedeutung, Reiten im Walde"),
       (T("o2"), "Zurück zum Fall: § 7 PassG heute"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Elfes-Urteil (BVerfGE 6, 32): Warum Art. 2 I GG als allgemeine Handlungsfreiheit jedes Verhalten schützt und die Ausreise nicht unter Art. 11 GG fällt.

Der Fall: Wilhelm Elfes, nach dem Krieg Oberbürgermeister von Mönchengladbach und später dort Oberstadtdirektor, kritisiert öffentlich, auch im Ausland, die Politik der Bundesregierung, vor allem zur Wehrpolitik und zur Frage der Wiedervereinigung. 1953 verweigert ihm die Passbehörde ohne nähere Begründung die Verlängerung seines Reisepasses (§ 7 Abs. 1 Buchst. a PaßG 1952: Gefährdung „sonstiger erheblicher Belange“ der Bundesrepublik). Am 16. Januar 1957 entscheidet das Bundesverfassungsgericht über seine Verfassungsbeschwerde.

Inhalt:
– Einstieg: Einem Antragsteller wird der Reisepass nach § 7 Abs. 1 Nr. 1 PassG versagt
– Art. 11 Abs. 1 GG (im Wortlaut): Freizügigkeit „im ganzen Bundesgebiet“ – die Ausreise ist nicht erfasst
– Art. 2 Abs. 1 GG (im Wortlaut): Handlungsfreiheit im umfassenden Sinn statt nur eines Kernbereichs; Ausreisefreiheit als Ausfluss; Auffanggrundrecht
– Schranke verfassungsmäßige Ordnung: jede formell und materiell verfassungsmäßige Rechtsnorm; unantastbarer Bereich privater Lebensgestaltung; Bestimmtheit der „sonstigen erheblichen Belange“
– Ergebnis: Verfassungsbeschwerde zurückgewiesen; Anspruch auf Begründung
– Bedeutung: Verfassungsbeschwerde gegen jede die Handlungsfreiheit beschränkende Norm; Reiten im Walde (1989); Verhältnismäßigkeit
– § 7 PassG heute (im Wortlaut), Klausurtipp, Prüfschema, Merksatz

Normen: Art. 2 Abs. 1, Art. 11 GG; § 7 Abs. 1 Nr. 1, Abs. 2 PassG (früher § 7 Abs. 1 Buchst. a PaßG 1952)

Rechtsprechung:
– BVerfG, Urt. v. 16.1.1957 – 1 BvR 253/56, BVerfGE 6, 32 (Elfes): S. 32 (Leitsätze, Entscheidungsformel), 33 f. (Sachverhalt), 34–36 (Art. 11 GG), 36 f. (allgemeine Handlungsfreiheit, Auffangfunktion), 37–41 (verfassungsmäßige Ordnung), 42 f. (Passgesetz), 43–45 (Ergebnis, Begründungspflicht)
– BVerfG, Beschl. v. 6.6.1989 – 1 BvR 921/85, BVerfGE 80, 137 (Reiten im Walde), S. 152 f.

Hinweise: Torben und Herr Haupt sind erfundene Figuren; Wilhelm Elfes wird nicht dargestellt. Die politische Tätigkeit wird nur so wiedergegeben, wie sie das Urteil beschreibt, und nicht bewertet. Den Aufbau der Grundrechtsprüfung erklärt eine eigene Folge. Nicht behandelt: die Rügen aus Art. 3, 5 und 6 GG, die Entstehungsgeschichte im Einzelnen.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Stempel und Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ElfesUrteil #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("sechzehnten Januar", "16. Januar"), ("Haupt: ", "Herr Haupt: ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n", srt) and "sechzehnt" not in srt and "Römisch" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
