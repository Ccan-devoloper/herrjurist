"""Nachbearbeitung der Upload-Texte für Folge 235 (nach meta_231.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lehrmaterial, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_235.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Neffe, das Gewitter und der Blitz"),
       (T("frage"), "Die Frage"),
       (T("p212"), "§ 212 StGB im Wortlaut, Mord?"),
       (T("erfolg"), "Erfolg und Kausalität"),
       (T("reicht"), "Reicht Kausalität? Objektive Zurechnung"),
       (T("gef"), "Gewitterfall: allgemeines Lebensrisiko"),
       (T("rspr"), "Weg der Rechtsprechung: Vorsatz"),
       (T("abw"), "Abwandlung: Täter im Wald"),
       (T("p222"), "§ 222 StGB: fahrlässige Tötung"),
       (T("gruppen"), "Weitere Fallgruppen"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Objektive Zurechnung am Gewitter-Fall: Warum genügt Kausalität nicht und wann hat der Täter eine rechtlich missbilligte Gefahr geschaffen, die sich realisiert (§ 212 StGB)?

Der Fall: Rupert ist der einzige Erbe seiner wohlhabenden Tante Hildegard. Als ein Gewitter aufzieht, rät er ihr zu einem Spaziergang im Wald – in der Hoffnung, dass ein Blitz sie trifft. Genau das passiert. Hat er sie getötet?

Inhalt:
– § 212 Abs. 1 StGB im Wortlaut; Mord aus Habgier (§ 211)?
– Erfolg und Kausalität nach der Conditio-sine-qua-non-Formel (mehr in Folge 026)
– Reicht Kausalität? Die Lehre von der objektiven Zurechnung: rechtlich missbilligte Gefahr, die sich im Erfolg verwirklicht
– Gewitterfall: allgemeines Lebensrisiko, Blitz nicht beherrschbar – keine Zurechnung
– Weg der Rechtsprechung: Lösung beim Vorsatz (Kausalverlauf in den Grenzen allgemeiner Lebenserfahrung; ein bloßer Wunsch ist kein Vorsatz)
– Abwandlung: Sonderwissen über einen Täter im Wald
– § 222 StGB im Wortlaut: fahrlässige Tötung entfällt ebenso
– Weitere Fallgruppen: Schutzzweck der Norm, eigenverantwortliche Selbstgefährdung, atypischer Kausalverlauf, rechtmäßiges Alternativverhalten
– Klausurtipp (Prüfungsstandort im objektiven Tatbestand), Klausurschema, Merksatz

Normen: §§ 211, 212, 222 StGB.

Rechtsprechung (der Gewitterfall selbst ist ein Lehrbuchfall, keine BGH-Entscheidung):
– BGH, Beschl. v. 10.8.2021 – 3 StR 394/20, Rn. 5 (Kausalität bleibt, wenn Opfer oder Dritte mitwirken), Rn. 8 (Vorsatz und Kausalverlauf: Grenzen allgemeiner Lebenserfahrung)
– BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, BGHSt 66, 119, Rn. 21 (Zurechnung beim Fahrlässigkeitsdelikt: Realisierung der Gefahr, Schutzzweck, pflichtgemäßes Alternativverhalten)
– BGH, Urt. v. 28.1.2014 – 1 StR 494/13, BGHSt 59, 150, Rn. 71 (eigenverantwortliche Selbstgefährdung)

Lehrmaterial: LMU München (Lehrstuhl Engländer), Strukturkarte Objektive Zurechnung; Universität Freiburg (Hefendehl), AG und Vorlesung Strafrecht AT, Übersicht Objektive Zurechnung, § 9 KK 169, 201; F.-C. Schroeder, Der Blitz als Mordinstrument (2009).

Hinweise: Hildegard und Rupert sind erfundene Figuren. Mehr dazu: Folge 026 (Kausalität), Folge 058 (Heroinspritzen-Fall: Selbstgefährdung), Folge 203 (Fremdgefährdung beim Rennen), Folge 182 (Fahrlässigkeitsdelikt).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ObjektiveZurechnung #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Gewitterfall", "allgemeines Lebensrisiko", "Erbonkel-Fall"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
