"""Nachbearbeitung der Upload-Texte für Folge 277 (nach meta_274.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Materialien,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Sprechernamen).
Aufruf: python3 meta_277.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Wohnblock in der Einfamilienhausstraße, Sachverhalt"),
       (T("anw"), "Anwendbarkeit: Innen- oder Außenbereich?"),
       (T("p34"), "§ 34 Abs. 1 BauGB im Wortlaut"),
       (T("naeh"), "Nähere Umgebung und Rahmen"),
       (T("p2"), "Art der Nutzung: § 34 Abs. 2 BauGB"),
       (T("mass"), "Maß: Rahmenüberschreitung und Spannungen"),
       (T("bauw"), "Bauweise, Grundstücksfläche, Erschließung"),
       (T("rueck"), "Rücksichtnahme"),
       (T("p3b"), "Neu: § 34 Abs. 3b BauGB"),
       (T("zust"), "Zustimmung der Gemeinde, § 36a BauGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 34 BauGB: Wann fügt sich ein sechsstöckiger Neubau in eine Einfamilienhausstraße ein? Nähere Umgebung, faktisches Baugebiet – bundesweit erklärt.

Der Fall: In einer Straße mit Einfamilienhäusern gibt es keinen Bebauungsplan. Herr Kronberg will ein altes Haus abreißen und einen Wohnblock mit 6 Geschossen und 24 Wohnungen bauen. Seine Nachbarin Frau Morgenstern fragt: Passt das in diese Straße? Und kann die Gemeinde mit dem neuen § 34 Abs. 3b BauGB trotzdem den Weg frei machen?

Inhalt:
– Anwendbarkeit: kein qualifizierter Bebauungsplan (§ 30 Abs. 1 BauGB), Innenbereich oder Außenbereich – Ortsteil und Bebauungszusammenhang
– § 34 Abs. 1 BauGB im Wortlaut: Einfügen nach Art, Maß, Bauweise und überbaubarer Grundstücksfläche; nähere Umgebung und Rahmen
– § 34 Abs. 2 BauGB im Wortlaut: faktisches Baugebiet – die Art der Nutzung nach der BauNVO
– Maß der baulichen Nutzung: Rahmenüberschreitung, bodenrechtlich beachtliche Spannungen, Vorbildwirkung
– Rücksichtnahme als Teil des Einfügens
– Neu seit 30.10.2025: § 34 Abs. 3b BauGB im Wortlaut (Abweichung für Wohngebäude mit Zustimmung der Gemeinde), Zustimmung nach § 36a BauGB (im Wortlaut), unbefristet – anders als § 246e BauGB
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 30, 34 Abs. 1, 2, 3b, 36a, 246e BauGB; § 3 BauNVO.

Rechtsprechung:
– BVerwG, Urt. v. 26.5.1978 – 4 C 9.77, BVerwGE 55, 369 (Rahmen, Einfügen, Rücksichtnahme)
– BVerwG, Urt. v. 8.12.2016 – 4 C 7.15, Rn. 9, 10, 13, 15, 17 (nähere Umgebung, Rahmen, Maß, Rahmenüberschreitung)
– BVerwG, Urt. v. 30.6.2015 – 4 C 5.14, BVerwGE 152, 275, Rn. 11, 13 (Ortsteil, Bebauungszusammenhang)
Gesetzgebung: Gesetz zur Beschleunigung des Wohnungsbaus und zur Wohnraumsicherung v. 27.10.2025 (BGBl. 2025 I Nr. 257), in Kraft 30.10.2025; BT-Drs. 21/781 (neu), S. 23 f.

Hinweise: Herr Kronberg und Frau Morgenstern sind erfundene Figuren. Rechtsstand 8. Oktober 2026 – bitte bei späterer Nutzung prüfen. Mehr dazu: Folge 200 (Baugebiete der BauNVO), Folge 274 (Gebietserhaltungsanspruch), Folge 188 (Baugenehmigung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Baurecht #Innenbereich #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
srt = re.sub(r"Abs\. 3\n\n(\d+)\n([^\n]+)\nb\. ", r"Abs. 3b.\n\n\1\n\2\n", srt)   # „drei b“ nicht über den Cue trennen
srt = re.sub(r"Abs\. 3\n\n(\d+)\n([^\n]+)\nb ", r"Abs. 3b\n\n\1\n\2\n", srt)
srt = srt.replace("dem dreißigsten\nOktober 2025", "dem 30.\nOktober 2025")
assert not re.search(r"Abs\. 3\n", srt), "Abs. 3b getrennt"
srt = re.sub(r"(?m)^Kronberg:", "Herr Kronberg:", srt)
srt = re.sub(r"(?m)^Morgenstern:", "Frau Morgenstern:", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["34 Abs. 3b BauGB", "Einfügen nähere Umgebung", "unbeplanter Innenbereich"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
