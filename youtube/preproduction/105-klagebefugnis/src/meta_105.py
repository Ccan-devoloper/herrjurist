"""Nachbearbeitung der Upload-Texte für Folge 105 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen und Zahlen in den Untertiteln. Kein Landesrecht (bundesrechtlich, länderneutral).
Aufruf: python3 meta_105.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Gebührenbescheid – der Freund will mitklagen"), (T("klage"), "Klagen, Frage und Sachverhalt"),
       (T("einord"), "Wortlaut § 42 II VwGO und Umweltverbandsklage"), (T("eigen"), "Verletzung eigener Rechte"),
       (T("mt"), "Möglichkeitstheorie"), (T("adr"), "Adressatentheorie, Art. 2 I GG"), (T("dritt"), "Dritte: Schutznormtheorie"),
       (T("zweck"), "Keine Popularklage: der Freund"), (T("tipp"), "Klausurtipp: ein Satz genügt"), (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Klagebefugnis nach § 42 II VwGO: Möglichkeitstheorie, Adressatentheorie und warum eine Popularklage unzulässig ist – kurz und klausurfertig.

Der Fall: Frau Nolte bekommt für die Fällgenehmigung ihrer kranken Kastanie einen Gebührenbescheid über 180 Euro. Sie klagt – und ihr Freund Herr Wilke will aus Solidarität mitklagen. Sind beide klagebefugt? (Übungsfall)

Inhalt:
– Wortlaut des § 42 Abs. 2 VwGO; „soweit gesetzlich nichts anderes bestimmt ist“: Umweltverbandsklage nach § 2 Abs. 1 Satz 1 UmwRG
– Geltendmachen einer Verletzung in eigenen (subjektiven) Rechten
– Möglichkeitstheorie: ausgeschlossen nur, wenn offensichtlich und nach keiner Betrachtungsweise subjektive Rechte verletzt sein können
– Adressatentheorie: Der Adressat eines belastenden Verwaltungsakts ist wegen Art. 2 Abs. 1 GG klagebefugt
– Dritte: drittschützende Norm (Schutznormtheorie)
– Zweck: keine Popularklage – warum der Freund nicht klagebefugt ist
– Klausurtipp: die Klagebefugnis des Adressaten in einem Satz; Verpflichtungsklage: möglicher Anspruch
– Schema und Merksatz

Rechtsprechung:
– BVerwG, Urt. v. 6.11.2024 – 6 C 2.23, Rn. 13 (Möglichkeitstheorie), Rn. 14 (kein Adressat), Rn. 24 (Schutznorm)
– BVerwG, Beschl. v. 19.7.2010 – 6 B 20.10, Rn. 16 (Adressatentheorie, Art. 2 Abs. 1 GG)
– BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18 (Adressatentheorie)

Kapitel:
{kapitel}

Das Schema und die Formulierung sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Klagebefugnis #Verwaltungsprozessrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nNolte:", "\nFrau Nolte:"), ("\nWilke:", "\nHerr Wilke:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace(" S. 1", " Satz 1")
for alt, neu in (("Hundertachtzig", "180"), ("hundertachtzig", "180")):
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
