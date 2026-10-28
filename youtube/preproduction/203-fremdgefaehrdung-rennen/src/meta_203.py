"""Nachbearbeitung der Upload-Texte für Folge 203 (nach meta_198.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung (Rn. nach der
amtlichen Fassung), Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Daten als Ziffern).
Aufruf: python3 meta_203.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Beifahrer beim nächtlichen Rennen"),
       (T("bgh"), "Der echte Fall: BGHSt 53, 55"),
       (T("p222"), "§ 222 StGB: fahrlässige Tötung"),
       (T("problem"), "Selbstgefährdung oder einverständliche Fremdgefährdung?"),
       (T("krit"), "Abgrenzung nach der Tatherrschaft"),
       (T("hier"), "Im Fall: Wer beherrscht das Geschehen?"),
       (T("roxin"), "Gegenansicht: Gleichstellung"),
       (T("einw"), "Einwilligung und § 228 StGB"),
       (T("indiv"), "Grenze: konkrete Todesgefahr"),
       (T("erg"), "Ergebnis"),
       (T("p315d"), "Heute: § 315d StGB"),
       (T("tipp"), "Klausurtipp: Prüfungsreihenfolge"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Einverständliche Fremdgefährdung oder Selbstgefährdung? Der Beifahrer beim Straßenrennen (BGHSt 53, 55) und die Rolle des § 228 StGB bei § 222 StGB.

Der Fall: Hilmar fährt nachts auf einer Landstraße ein Rennen, sein Kollege Eike sitzt daneben und feuert ihn an. Beide sind nüchtern und kennen die Gefahr. In einer Kurve verliert Hilmar die Kontrolle, Eike stirbt. Hat Hilmar ihn fahrlässig getötet – oder hat Eike sich selbst gefährdet?

Inhalt:
– Der echte Fall: BGH, Urteil vom 20.11.2008 (Beschleunigungstests, Beifahrer gab Startzeichen und filmte)
– § 222 StGB im Wortlaut: Erfolg, Kausalität, Sorgfaltspflichtverletzung, Vorhersehbarkeit
– Zurechnung: eigenverantwortliche Selbstgefährdung oder einverständliche Fremdgefährdung?
– Abgrenzung nach der Tatherrschaft über die gefährdende Handlung – auch beim Fahrlässigkeitsdelikt
– Im Fall: Wer am Steuer sitzt, beherrscht das Geschehen; Anfeuern ist untergeordnet
– Gegenansicht (Gleichstellung mit der Selbstgefährdung, etwa Roxin) und warum der BGH sie hier ablehnt
– Einwilligung: § 228 StGB im Wortlaut; Grenze der Sittenwidrigkeit bei konkreter Todesgefahr; anders bei § 315c StGB
– Heute: § 315d StGB (verbotenes Kraftfahrzeugrennen, seit 13.10.2017), Abs. 5 Todesfolge
– Klausurtipp mit Prüfungsreihenfolge und Merksatz

Normen: §§ 222, 228, 315c, 315d StGB

Rechtsprechung:
– BGH, Urt. v. 20.11.2008 – 4 StR 328/08, BGHSt 53, 55, Rn. 21–25 (Selbst- und Fremdgefährdung, Tatherrschaft, Gleichstellung abgelehnt), Rn. 27–30 (Einwilligung, konkrete Todesgefahr, § 315c); Randnummern nach der amtlichen Fassung auf bundesgerichtshof.de
– BGH, Beschl. v. 26.10.2022 – 4 StR 248/22, Rn. 11 (§ 315d: Mitinsassen als „andere Menschen“, jedenfalls wenn sie nicht Tatbeteiligte sind)
– BGH, Beschl. v. 18.6.2025 – 4 StR 8/25, Rn. 5 f. (§ 315d Abs. 5 setzt den Gefährdungsvorsatz des Abs. 2 voraus)

Hinweise: Der Fall im Video ist ein Übungsfall nach dem Vorbild von BGHSt 53, 55. Ob ein anfeuernder Beifahrer bei § 315d selbst Tatbeteiligter ist und deshalb nicht als „anderer Mensch“ zählt, lässt das Video offen. Die Gegenansicht ist nach ihrer Wiedergabe im BGH-Urteil dargestellt. Prüfungsschemata sind Klausurkonventionen. Mehr zur eigenverantwortlichen Selbstgefährdung im „Heroinspritzen-Fall“, zur Sittenwidrigkeit nach § 228 StGB in der Folge zur verabredeten Schlägerei.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT), Phosphor (MIT), Tabler (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Jura #Fremdgefährdung
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in [("ein Uhr zehn", "1:10 Uhr"), ("Anfang fünfzig", "Anfang 50"), ("Erlaubt sind hundert,", "Erlaubt sind 100,"),
                 ("fast hundertneunzig", "fast 190"),
                 ("dreizehnten\nOktober 2017", "13.\nOktober 2017")]:
    n = srt.count(alt)
    assert n, alt
    srt = srt.replace(alt, neu)
# Datum über eine Untertitelgrenze: „vom zwanzigsten November“ | „2008. …“
srt, n = re.subn(r"vom zwanzigsten November(\n\n\d+\n[^\n]+\n)2008\.", r"vom 20. November\g<1>2008.", srt)
assert n == 1, "Datum 20.11.2008"
assert "fast 190" in srt and srt.count("fast 190") == 2
for w in ("hundert", "zwanzigsten", "dreizehnten", "fünfzig", "Paragraf", "Uhr zehn"):
    assert w not in srt, f"Zahlwort im Untertitel: {w}"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["einverständliche Fremdgefährdung", "Tatherrschaft", "§ 315d StGB", "Straßenrennen"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen;", len(m["tags"]), "Tags")
