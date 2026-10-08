"""Nachbearbeitung der Upload-Texte für Folge 273 (nach meta_237.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen der drei
geprüften Länder, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen in Figurenrede wie in den Blasen).
Landesrecht: Konkrete Fristen und Gebühren nur für die am Wortlaut geprüften Länder NRW, Niedersachsen, Sachsen (Abruf
08.10.2026); Bayern war gesperrt, die übrigen Länder wurden nicht geprüft – die Beschreibung verweist dafür auf das
Juristenausbildungsgesetz bzw. die Prüfungsordnung und das Prüfungsamt des eigenen Landes.
Aufruf: python3 meta_273.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: im 7. Semester schon melden?"),
       (T("was"), "Was ist der Freiversuch? § 5d Abs. 5 DRiG"),
       (T("vor"), "Voraussetzungen: NRW, Niedersachsen, Sachsen"),
       (T("frei"), "Semester, die nicht mitzählen"),
       (T("leo2"), "Der Fall: Auslandssemester"),
       (T("verb"), "Der Verbesserungsversuch: Fristen und Gebühren"),
       (T("besser"), "Was am Ende zählt"),
       (T("strat"), "Lohnt sich der Freischuss?"),
       (T("erg"), "Ergebnis: Leonore entscheidet"),
       (T("tipp"), "Klausurtipp: wie ein echter Versuch"),
       (T("sch"), "Dein Freischuss in 5 Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Freischuss Jura: Wie funktionieren Freiversuch und Verbesserungsversuch im Staatsexamen, welche Fristen gelten, und was regelt das Landesrecht?

Der Fall: Leonore ist im 7. Fachsemester und steht vor dem Aushang mit den Meldefristen. Soll sie sich jetzt schon zum Examen melden – und was passiert, wenn sie durchfällt? Ihr Freund Rasmus hat früh geschrieben und danach seine Note verbessert.

Inhalt:
– Was ist der Freiversuch? Nach § 5d Abs. 5 DRiG gilt eine nicht bestandene Pflichtfachprüfung als nicht unternommen, wenn du dich frühzeitig gemeldet und alle vorgesehenen Prüfungsleistungen vollständig erbracht hast. Das Nähere regelt dein Land.
– Voraussetzungen, drei Beispiele: Nordrhein-Westfalen (Meldung spätestens bis zum Ende des 8. Fachsemesters), Niedersachsen (Zulassung zum Prüfungsdurchgang nach dem 8. Fachsemester), Sachsen (Prüfung spätestens im Termin nach dem 9. Semester bei Studienbeginn ab 1.10.2020) – jeweils nach ununterbrochenem Studium
– Semester, die nicht mitzählen: etwa schwere Krankheit oder Auslandsstudium (NRW und Niedersachsen bis zu 3, Sachsen bis zu 2 Semester); NRW insgesamt höchstens 4
– Der Verbesserungsversuch: Antragsfristen und Gebühren in NRW, Niedersachsen (160 €) und Sachsen (500 €) – nach einem bestandenen Freiversuch jeweils ohne Gebühr
– Lohnt sich der Freischuss? Chancen und Risiken
– Klausurtipp, dein Freischuss in 5 Schritten, Merksatz

Normen: § 5d Abs. 5 DRiG · Nordrhein-Westfalen: §§ 24, 25, 26, 65 Abs. 2 Nr. 1 JAG NRW · Niedersachsen: §§ 17, 18, 19 NJAG, § 17 NJAVO, Anlage 2 NJG Nr. 7.3 · Sachsen: §§ 29, 30, 31 SächsJAPO · zweites Examen: § 56a JAG NRW, § 19 NJAG, § 56 SächsJAPO

Hinweise: Fristen, anrechnungsfreie Semester, Verbesserungsversuch und Gebühren regelt jedes Land selbst. Im Video stehen nur Nordrhein-Westfalen, Niedersachsen und Sachsen als Beispiele (Wortlaut am 8. Oktober 2026 auf den amtlichen Landesportalen geprüft). Für alle anderen Länder gilt dein Juristenausbildungsgesetz bzw. deine Prüfungsordnung. Ob ein Semester bei dir mitzählt, klärst du mit dem Prüfungsamt deines Landes. Passend dazu: Folge 201 „Lernplan Examen“ und Folge 237 „Probeklausuren Examen“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechts- oder Studienberatung im Einzelfall. Rechtsstand: 8. Oktober 2026 (DRiG zuletzt geändert am 22. Oktober 2024; JAG NRW in der Fassung ab 7. Mai 2025; NJAG § 18 in der Fassung ab 7. Mai 2026; SächsJAPO in der Fassung ab 31. Juli 2025).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT), Fluent Emoji High Contrast (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound 257913 (SOUNDSCAPE_HUMFAK, CC0).

#Freischuss #Freiversuch #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"im siebten Semester\.", r"im 7. Semester."),
                       (r"brachte sieben(\s+)Punkte, der Verbesserungsversuch neun", r"brachte 7\1Punkte, der Verbesserungsversuch 9"),
                       (r"hundertsechzig(\s+)Euro", r"160\1Euro"), (r"fünf(\s*)hundert(\s+)Euro", r"500\2Euro")]:
    srt, n = re.subn(muster, ersatz, srt, flags=re.M | re.S)
    assert n, muster
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
