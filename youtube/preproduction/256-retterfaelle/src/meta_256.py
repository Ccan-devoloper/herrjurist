"""Nachbearbeitung der Upload-Texte für Folge 256 (nach meta_235.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lehrmaterial, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Zahlen in Ziffern).
Aufruf: python3 meta_256.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Retter stirbt"),
       (T("frage"), "Die Frage"),
       (T("bgh"), "Der echte Fall: BGHSt 39, 322"),
       (T("p222"), "§ 222 StGB: Erfolg, Kausalität, Vorhersehbarkeit"),
       (T("problem"), "Problem: eigenverantwortliche Selbstgefährdung?"),
       (T("nein"), "BGH: einsichtiges Motiv zur Rettung"),
       (T("grenze"), "Die Grenze: sinnlose Rettung"),
       (T("subs"), "Ergebnis zu § 222"),
       (T("beruf"), "Berufsretter (BGHSt 66, 119)"),
       (T("lehre"), "Retterfälle in der Lehre"),
       (T("p306c"), "§ 306c StGB: Brandstiftung mit Todesfolge"),
       (T("leicht"), "Wenigstens leichtfertig"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Retterfälle (BGHSt 39, 322): Wird der Tod eines freiwilligen Retters dem Brandstifter als fahrlässige Tötung (§ 222 StGB) zugerechnet, obwohl er sich selbst in Gefahr begibt – und erfasst § 306c StGB heute auch den Retter?

Der Fall: Siegbert legt im Keller seines Mehrfamilienhauses Feuer. Nachbar Arndt läuft in das brennende Haus, bringt zwei Kinder in Sicherheit und stürzt beim Rückweg durch die brennende Decke. Muss Siegbert für seinen Tod einstehen?

Inhalt:
– Der echte Fall: BGH, Urteil vom 8.9.1993 – 3 StR 341/93, BGHSt 39, 322
– § 222 StGB im Wortlaut: Erfolg, Kausalität trotz freiwilliger Rettung, Vorhersehbarkeit
– Problem: eigenverantwortliche Selbstgefährdung (mehr in Folge 058) – und keine Fremdgefährdung (Folge 203)
– BGH: kein schematischer Zurechnungsausschluss; der Täter schafft ein einsichtiges Motiv für gefährliche Rettungsmaßnahmen
– Grenze: von vornherein sinnlose oder offensichtlich unverhältnismäßige Rettungsversuche
– Berufsretter: BGHSt 66, 119 (2021)
– Retterfälle in der Lehre: drei Ansichten
– § 306c StGB im Wortlaut: Grunddelikt § 306a, früheres Recht (§ 307 Nr. 1 a. F.), Retter nach herrschender Lehre erfasst, wenigstens Leichtfertigkeit
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 222, 306a, 306c StGB.

Rechtsprechung:
– BGH, Urt. v. 8.9.1993 – 3 StR 341/93, BGHSt 39, 322, Leitsatz 1, Rn. 4, 6, 7, 9, 10 (Zurechnung beim freiwilligen Retter; Grenze)
– BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, BGHSt 66, 119, Leitsatz 1, Rn. 26–28 (Berufsretter)
– BGH, Urt. v. 28.1.2014 – 1 StR 494/13, BGHSt 59, 150, Rn. 71 (eigenverantwortliche Selbstgefährdung)
– BGH, Urt. v. 7.2.2001 – 5 StR 474/00, BGHSt 46, 279, Rn. 24 (Leichtfertigkeit, zu § 30 BtMG)

Lehrmaterial: von Atens/Schröder, Referendarexamensklausur „Eine feurige Spritztour“, ZJS 2016, 62 ff.; Universität Freiburg (Hefendehl), Vorlesung Strafrecht BT, § 49 Brandstiftungsdelikte, KK 709 f.

Hinweise: Siegbert, Arndt und Liesbeth sind erfundene Figuren; der echte Fall verlief anders (Feier im Wohnhaus, Sohn der Eigentümer starb im Rauch). Mehr dazu: Folge 058 (Heroinspritzen-Fall: Selbstgefährdung), Folge 203 (Fremdgefährdung beim Rennen), Folge 235 (objektive Zurechnung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Retterfälle #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§ \d+)\n\n(\d+\n[^\n]+\n)([a-c])([.,:]?) ?", r"\1\3\4\n\n\2", srt)   # „§ 306“ | „a, …“ → „§ 306a,“ | „…“
srt = re.sub(r"(§ \d+)\n([a-c])([.,:]?) ?", r"\1\2\3\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = srt.replace("achten September\n1993", "8. September\n1993").replace("achten September 1993", "8. September 1993")
srt = srt.replace("zweiundzwanzigjährige", "22-jährige")
srt = srt.replace("Folge\nachtundfünfzig", "Folge\n58").replace("Folge achtundfünfzig", "Folge 58")
srt = srt.replace("Folge zweihundertdrei", "Folge 203")
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|§ \d+\n\n\d+\n[^\n]+\n[a-c]\b|§ \d+\n[a-c]\b|Paragraf (?!verzichtet)|achtundfünfzig|zweihundertdrei", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["BGHSt 66, 119", "Berufsretter", "Brandstiftung mit Todesfolge"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
