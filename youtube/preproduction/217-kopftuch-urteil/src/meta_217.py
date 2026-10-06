"""Nachbearbeitung der Upload-Texte für Folge 217 (nach meta_211.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben nicht über den Zeilenumbruch getrennt).
Keine Namen realer Beschwerdeführerinnen. Länderregelungen nicht aufgelistet (nicht an Primärquellen geprüft; RECHTSSTAND.md).
Aufruf: python3 meta_217.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Lehrerin mit Kopftuch"),
       (T("pause"), "Das neue Schulgesetz und die Ausnahme"),
       (T("frage"), "Die Fragen und der Sachverhalt"),
       (T("art4"), "Art. 4 GG im Wortlaut"),
       (T("einh"), "Schutzbereich und Eingriff"),
       (T("vorb"), "Schranken: kollidierendes Verfassungsrecht"),
       (T("neg"), "Schüler, Eltern, Erziehungsauftrag (Art. 6, 7 GG)"),
       (T("k1"), "Kopftuch I (2003): Gesetz nötig"),
       (T("k2"), "Kopftuch II (2015): konkrete Gefahr nötig"),
       (T("zurech"), "Warum die abstrakte Gefahr nicht reicht"),
       (T("priv"), "Die Ausnahme: Art. 33 Abs. 3 GG"),
       (T("erg"), "Ergebnis im Fall"),
       (T("ref"), "Rechtsreferendarin (2020): Justiz ist anders"),
       (T("heute"), "Heute: § 34 Abs. 2 BeamtStG"),
       (T("tipp"), "Klausurtipp: Prüfungsaufbau"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Kopftuch-Urteil (BVerfGE 108, 282; 138, 296): Darf ein Land Lehrerinnen das Kopftuch pauschal verbieten? Glaubensfreiheit nach Art. 4 GG gegen negative Glaubensfreiheit, Elternrecht und staatliche Neutralität – und warum vor Gericht strengere Regeln gelten können (BVerfGE 153, 1).

Der Fall: Frau Sander unterrichtet Mathematik in der Klasse 8b. Sie trägt ein Kopftuch, weil sie es als Gebot ihres Glaubens versteht; Streit darüber gab es nie. Das Land verbietet Lehrkräften religiöse Zeichen an allen Schulen – ausgenommen nur die Darstellung christlicher und abendländischer Bildungs- und Kulturwerte. Ist das pauschale Verbot mit dem Grundgesetz vereinbar?

Inhalt:
– Art. 4 Abs. 1, 2 GG (im Wortlaut): ein einheitliches Grundrecht; ein plausibel dargelegtes Glaubensgebot genügt
– Eingriff: Beruf oder Glaubensgebot
– Schranken: vorbehaltlos, nur kollidierendes Verfassungsrecht und ein hinreichend bestimmtes Gesetz; negative Glaubensfreiheit, Art. 6 Abs. 2 und Art. 7 Abs. 1 GG (im Wortlaut)
– Kopftuch I (2003): Ein Verbot braucht eine hinreichend bestimmte gesetzliche Grundlage
– Kopftuch II (2015): Ein landesweites Verbot wegen bloß abstrakter Gefahr ist unverhältnismäßig; nötig ist eine hinreichend konkrete Gefahr für Schulfrieden oder Neutralität
– Die Ausnahme für christlich-abendländische Werte: gleichheitswidrig (Art. 3 Abs. 3, Art. 33 Abs. 3 GG, im Wortlaut), nichtig
– Rechtsreferendarin (2020): In der Justiz darf das Land das Kopftuch verbieten, muss es aber nicht
– Heute: § 34 Abs. 2 S. 4 BeamtStG (im Wortlaut)
– Klausurtipp mit Prüfungsaufbau, Merksatz

Normen: Art. 4 Abs. 1, 2, Art. 6 Abs. 2, Art. 7 Abs. 1, Art. 3 Abs. 3, Art. 33 Abs. 2, 3 GG; § 34 Abs. 2 BeamtStG; § 61 Abs. 2 BBG.

Rechtsprechung:
– BVerfG, Urt. v. 24.9.2003 – 2 BvR 1436/02, BVerfGE 108, 282 (Kopftuch I), Rn. 30, 36–41, 49, 57–71
– BVerfG, Beschl. v. 27.1.2015 – 1 BvR 471/10, 1 BvR 1181/10, BVerfGE 138, 296 (Kopftuch II), Rn. 83–116, 123–138
– BVerfG, Beschl. v. 14.1.2020 – 2 BvR 1333/17, BVerfGE 153, 1 (Rechtsreferendarin), Rn. 77–105

Hinweise: Frau Sander, Herr Steffens, Herr Röder, die Schule und das Land sind erfunden; die Rechtsreferendarin und die Richterin sind Funktionsrollen. Wie die Länder das Erscheinungsbild ihrer Beamtinnen und Beamten im Einzelnen regeln, bestimmt das jeweilige Landesrecht (§ 34 Abs. 2 S. 5 BeamtStG); schau in dein Landesrecht. Mehr dazu: Folge 020 (Grundrechtsprüfung Schema), Folge 008 (Grundrechte Überblick), Folge 004 (Neutralitätspflicht).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#KopftuchUrteil #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Steffens: Lehrkräfte", "Herr Steffens: Lehrkräfte"), ("Steffens: Dann", "Herr Steffens: Dann"),
             ("Sander: Ich unterrichte", "Frau Sander: Ich unterrichte"), ("Roeder: Mein Sohn", "Herr Röder: Mein Sohn"),
             ("Richterin: Heute", "Vorsitzende Richterin: Heute"),
             ("Klasse acht b, siebenundzwanzig Kinder", "Klasse 8b, 27 Kinder"), ("die acht b weiter", "die 8b weiter"),
             ("Ab dem ersten\nAugust", "Ab dem 1.\nAugust"), ("Kopftuch eins", "Kopftuch I"), ("Kopftuch zwei", "Kopftuch II")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n|zweitausend|acht b|siebenund|Roeder", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["Rechtsreferendarin Kopftuch", "§ 34 BeamtStG"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
