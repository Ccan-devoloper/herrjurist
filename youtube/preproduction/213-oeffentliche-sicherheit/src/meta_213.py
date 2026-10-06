"""Nachbearbeitung der Upload-Texte für Folge 213 (nach meta_210.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit korrigierter Planbeschreibung, Fall, Inhalt, Normen
(nur am Landesportal geprüfte Landesnormen), Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel: Sprechernamen.
Aufruf: python3 meta_213.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Graffiti auf der eigenen Garage"),
       (T("gk"), "Die Generalklausel, § 8 PolG NRW"),
       (T("drei"), "Drei Schutzgüter der öffentlichen Sicherheit"),
       (T("sachsen"), "Legaldefinition, Regel, öffentliche Ordnung"),
       (T("pr1"), "Fall: Rechtsordnung und § 303 StGB"),
       (T("pr2"), "Fall: Rechte des Einzelnen, Staat, Ergebnis"),
       (T("gegen"), "Gegenfall: die Mietgarage"),
       (T("subs"), "Schutz privater Rechte: Subsidiarität"),
       (T("tab"), "Länder-Overlay: NRW, Brandenburg, Sachsen"),
       (T("tipp"), "Klausurtipp: Rechtsordnung zuerst"),
       (T("sch"), "Klausurschema öffentliche Sicherheit"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Öffentliche Sicherheit als Schutzgut der polizeilichen Generalklausel (Beispiel NRW, § 8 I PolG NRW): Rechtsordnung, Rechte des Einzelnen und Staat – mit Graffiti auf der eigenen Garage, Gegenfall Mietgarage und Subsidiarität beim Schutz privater Rechte (§ 1 II PolG NRW).

Der Fall: Frau Schulze sprüht ein buntes Bild aus Blumen und Wellen auf das Tor ihrer eigenen Garage. Der Nachbar ruft die Polizei. Darf die Polizei einschreiten?

Inhalt:
– Generalklausel im Wortlaut (§ 8 Abs. 1 PolG NRW) und das Merkmal „öffentliche Sicherheit“
– Die drei Schutzgüter: Unverletzlichkeit der objektiven Rechtsordnung, subjektive Rechte und Rechtsgüter des Einzelnen, Bestand und Funktionsfähigkeit des Staates und seiner Einrichtungen (BVerfG, Brokdorf); Sachsen definiert den Begriff im Gesetz (§ 4 Nr. 1 SächsPVDG)
– Regel: Gefahr, wenn eine strafbare Verletzung dieser Schutzgüter droht; Abgrenzung zur öffentlichen Ordnung
– Fall: § 303 Abs. 2 StGB verlangt eine fremde Sache; keine Gestaltungssatzung (§ 89 Abs. 1 Nr. 1 BauO NRW); Eigentümerin darf nach Belieben verfahren (§ 903 S. 1 BGB) – keine Gefahr
– Gegenfall: Die Garage gehört der Vermieterin – Sachbeschädigung, die Polizei darf einschreiten
– Nur private Rechte (Kreide): Subsidiaritätsklausel im Wortlaut (§ 1 Abs. 2 PolG NRW)
– Länder-Overlay, Klausurtipp, Klausurschema, Merksatz

Normen im Ländervergleich (im Video als Overlay; am amtlichen Landesportal geprüft, Abruf 6.10.2026):
– Nordrhein-Westfalen: Generalklausel § 8 Abs. 1 PolG NRW; Schutz privater Rechte § 1 Abs. 2 PolG NRW
– Brandenburg: Generalklausel § 10 Abs. 1 BbgPolG; Schutz privater Rechte § 1 Abs. 2 BbgPolG
– Sachsen: Generalklausel § 12 Abs. 1 SächsPVDG; Schutz privater Rechte § 2 Abs. 2 SächsPVDG (nur auf Antrag der berechtigten Person); Begriff der öffentlichen Sicherheit § 4 Nr. 1 SächsPVDG
Die übrigen Länder haben vergleichbare Regeln unter eigenen Nummern; bitte im eigenen Landespolizeigesetz nachschlagen.

Weitere Normen: § 303 Abs. 1, 2 StGB; § 903 S. 1 BGB; § 89 Abs. 1 Nr. 1 BauO NRW 2018; § 1 Abs. 1 S. 2 PolG NRW

Rechtsprechung:
– BVerfG, Beschl. v. 14.5.1985 – 1 BvR 233, 341/81 (Brokdorf), BVerfGE 69, 315 (352), Rn. 77 nach der Zählung von „Das Fallrecht (DFR)“: Begriffe öffentliche Sicherheit und öffentliche Ordnung

Hinweise: Polizeirecht ist Landesrecht; Nordrhein-Westfalen ist das Beispielland. Wie du eine polizeiliche Maßnahme insgesamt prüfst (Standardmaßnahme vor Generalklausel), zeigt das Video „Polizeirecht-Schema: Standardmaßnahme vor Generalklausel“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Polizeirecht #ÖffentlicheSicherheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n +", "\n", srt)
for alt, neu in [("\nSchulze: ", "\nFrau Schulze: "), ("\nNeumann: ", "\nHerr Neumann: "), ("\nGebauer: ", "\nHerr Gebauer: "),
                 ("\nDietz: ", "\nFrau Dietz: ")]:
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert not re.search(r"hundert|Paragraf|zwölf", srt), "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
# Tags: „Selbstgefährdung“ behandelt das Video nicht allgemein (kein Primärbeleg), „Landes-PolG“ durch konkrete Begriffe ersetzt
m["tags"] = ["öffentliche Sicherheit", "Schutzgüter", "Unverletzlichkeit der Rechtsordnung", "Schutz privater Rechte",
             "Subsidiarität", "Generalklausel", "Polizeirecht", "Sachbeschädigung"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
