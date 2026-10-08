"""Nachbearbeitung der Upload-Texte für Folge 260 (nach meta_257.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Norm, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Zahlen als Ziffern).
Aufruf: python3 meta_260.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: eingeschlossen im Schlaf"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("norm"), "§ 239 StGB: Wortlaut und Rechtsgut"),
       (T("pot"), "1. Ansicht: potenzielle Fortbewegungsfreiheit"),
       (T("akt"), "2. Ansicht: aktuelle Fortbewegungsfreiheit"),
       (T("bgh"), "Was sagt der BGH? (5 StR 406/21)"),
       (T("loes"), "Lösung nach der 1. Ansicht und dem BGH"),
       (T("erg2"), "Lösung nach der 2. Ansicht und Versuch"),
       (T("streit"), "Streitentscheid"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Freiheitsberaubung § 239 StGB im Schlaf: Schützt die Norm die potenzielle oder nur die aktuelle Fortbewegungsfreiheit – muss das Opfer es merken? Streitstand, BGH-Urteil 5 StR 406/21 und Lösung je Ansicht, mit dem Versuch nach § 239 Abs. 2 StGB.

Der Fall: Nachts in einer Altbauwohnung schließt Vermieter Herr Gerber das Zimmer seines schlafenden Untermieters Joscha von außen ab – einen anderen Ausgang gibt es nicht. Er ist sicher, dass Joscha durchschläft, und schließt nach zwei Stunden wieder auf. Joscha merkt nichts. Freiheitsberaubung?

Inhalt:
– § 239 Abs. 1 StGB: Wortlaut und Rechtsgut (Fortbewegungsfreiheit)
– 1. Ansicht: potenzielle Fortbewegungsfreiheit (BGH, Teile der Literatur)
– 2. Ansicht: aktuelle Fortbewegungsfreiheit (im Schrifttum weit verbreitet)
– Was der BGH 2022 entschieden hat – ein Täuschungsfall, kein Schlafender
– Lösung je Ansicht, Versuch (§ 239 Abs. 2 StGB) und Tatentschluss
– Streitentscheid, Klausurtipp, Schema, Merksatz

Normen (Wortlaut geprüft am 8. Oktober 2026 auf gesetze-im-internet.de): § 239 Abs. 1, 2 StGB; zum Vergleich § 240 Abs. 1 StGB, § 22 StGB.

Rechtsprechung:
– BGH, Urt. v. 8.6.2022 – 5 StR 406/21 (HRRS 2022 Nr. 801), Rn. 21–27: § 239 StGB schützt die potentielle persönliche Bewegungsfreiheit; ob der Betroffene die Freiheitsbeschränkung realisiert, ist ohne Belang (dort: durch Täuschung erschlichenes Einverständnis)
– BGH, Urt. v. 31.5.1960 – 1 StR 212/60, BGHSt 14, 314, 316 (zitiert in 5 StR 406/21, Rn. 21)

Hinweise: Herr Gerber und Joscha sind erfundene Figuren. Den dreistufigen Deliktsaufbau zeigt Folge 011.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Freiheitsberaubung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("Folge elf.", "Folge 011."), ("Folge 11.", "Folge 011."), ("kurz vor ein Uhr nachts.", "kurz vor 1 Uhr nachts."),
                 ("Bis drei bleibt die Tür zu.", "Bis 3 bleibt die Tür zu."), ("Um drei Uhr schließt", "Um 3 Uhr schließt"),
                 ("Um sieben wacht", "Um 7 wacht")]:
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Freiheitsberaubung Schlafender", "Versuch Freiheitsberaubung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
