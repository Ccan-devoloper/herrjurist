"""Nachbearbeitung der Upload-Texte für Folge 167 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: verbliebene Zahlwörter in Ziffern. Aufruf: python3 meta_167.py <upload-ordner>"""
import json, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: das bearbeitete Zeugnis als PDF – mit Sachverhalt"),
       (T("begriff"), "Die einfache Fotokopie: keine Urkunde"),
       (T("streit"), "Streitstand: Ist die Kopie eine Urkunde?"),
       (T("aus"), "Ausnahmen: Anschein des Originals, beglaubigte Kopie, Collage"),
       (T("datei"), "Scan und PDF: § 269 StGB im Wortlaut"),
       (T("bgh"), "Scan oder digitales Original?"),
       (T("olg"), "Zeugnis als PDF-Anhang: OLG Celle, Gegenansicht, § 270"),
       (T("loes"), "Lösung: PDF und Ausdruck als Kopie, Ausblick Betrug"),
       (T("tab"), "Merktabelle: Original, Kopie, Scan"),
       (T("tipp"), "Klausurtipp und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Kopie als Urkunde? Warum die einfache Fotokopie keine Urkunde nach § 267 StGB ist, wann doch – und wann bei Scan und PDF § 269 StGB greift.

Der Fall: Janosch (20) bewirbt sich um eine Stelle. Er scannt sein Abiturzeugnis ein, ändert am Rechner die Note von 2,8 in 1,8 und schickt das PDF per E-Mail an die Personalabteilung. Variante: Er druckt die Datei aus und schickt den Ausdruck als Kopie per Post. Urkundenfälschung oder Fälschung beweiserheblicher Daten?

Inhalt:
– Die einfache Fotokopie: keine Urkunde, solange sie als Reproduktion erscheint (BGHSt 24, 140)
– Streitstand: Gegenansicht in der Literatur und Rechtsprechung
– Ausnahmen: Kopie mit dem Anschein des Originals; Kopie eines gefälschten Originals, auch beglaubigt; Grenze: die Collage
– Scan und PDF: § 269 StGB im Wortlaut und der hypothetische Urkundenvergleich
– Eingescanntes Papierdokument oder digitales Original?
– Zeugnis als PDF-Anhang (OLG Celle), Gegenansicht, § 270 StGB
– Lösung beider Varianten, Ausblick Anstellungsbetrug
– Merktabelle Original, Kopie, Scan; Klausurtipp; Merksatz

Normen: §§ 267, 269, 270 StGB; § 263 StGB (Ausblick)

Rechtsprechung:
– BGH, Urt. v. 11.5.1971 – 1 StR 387/70, BGHSt 24, 140 (wiedergegeben nach den folgenden Entscheidungen)
– BGH, Beschl. v. 9.3.2011 – 2 StR 428/10, Rn. 11, 12
– BGH, Beschl. v. 27.1.2010 – 5 StR 488/09, Rn. 8–10, 12, 13
– BGH, Beschl. v. 2.5.2001 – 2 StR 149/01, Rn. 7, 8
– BGH, Beschl. v. 26.2.2003 – 2 StR 411/02, Rn. 6
– BGH, Beschl. v. 23.5.2017 – 4 StR 141/17, Rn. 9
– BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 17, 27, 28
– OLG Celle, Urt. v. 15.12.2023 – 1 ORs 2/23 (amtlicher Leitsatz)
– BGH, Beschl. v. 21.8.2019 – 3 StR 221/18, Rn. 30
(BGH-Randnummern nach HRRS)

Kapitel:
{kapitel}

Der Fall und die Personen sind ausgedacht. Die Gegenansicht in der Literatur wird nach Nestler, ZJS 2010, 608, und OLG Celle wiedergegeben. Der Betrug ist nur Ausblick. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Urkundenfälschung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in (("zwanzig", "20"), ("zwei Komma acht", "2,8"), ("Eins Komma acht", "1,8"), ("eins Komma acht", "1,8"),
             ("neunzehnhunderteinundsiebzig", "1971"), ("Eine Eins vorne", "Eine 1 vorne")):
    srt = srt.replace(a, b)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Fälschung beweiserheblicher Daten", "§ 270 StGB", "Kopie Urkunde Klausur"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
