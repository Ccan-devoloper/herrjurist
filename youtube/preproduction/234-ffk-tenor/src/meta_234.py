"""Nachbearbeitung der Upload-Texte für Folge 234 (nach meta_233.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Landesrecht-Hinweis,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_234.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die Polizei löst die Mahnwache auf"),
       (T("frage"), "Die Frage"),
       (T("antrag"), "1. Der Antrag: Feststellung statt Aufhebung"),
       (T("umst"), "Umstellung im Prozess: keine Klageänderung"),
       (T("ffi"), "2. Feststellungsinteresse im Urteil"),
       (T("wh"), "Wiederholungsgefahr"),
       (T("reha"), "Rehabilitation und tiefgreifender Grundrechtseingriff"),
       (T("tenor"), "3. Der Tenor"),
       (T("kosten"), "Kosten und vorläufige Vollstreckbarkeit"),
       (T("fehler"), "4. Typische Fehler, Hilfsantrag"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fortsetzungsfeststellungsklage nach § 113 I 4 VwGO: Fallgruppen des Feststellungsinteresses und der richtige Tenor bei Anfechtungs- und Verpflichtungssituation.

Der Fall: Herr Strauch leitet eine Mahnwache vor der Stadtbücherei. Die Polizei löst die Versammlung auf, weil die Teilnehmer vor dem Eingang stehen. Die Mahnwache ist längst vorbei – doch Herr Strauch plant schon die nächste. Was beantragt er, wie begründet das Urteil sein Feststellungsinteresse, und wie lautet der Tenor?

Inhalt (Perspektive 2. Examen):
– Antrag: Feststellung statt Aufhebung, § 113 Abs. 1 Satz 4 VwGO entsprechend bei Erledigung vor Klageerhebung
– Umstellung bei Erledigung im Prozess: keine Klageänderung, § 173 Satz 1 VwGO i. V. m. § 264 Nr. 2 ZPO (teils Nr. 3), Formulierung im Tatbestand
– Feststellungsinteresse im Urteil: Wiederholungsgefahr, Rehabilitation, tiefgreifender Grundrechtseingriff (BVerwG 2024: kurze Dauer und gewichtiger Eingriff)
– Tenor: „Es wird festgestellt, dass … rechtswidrig gewesen ist.“; Verpflichtungssituation
– Kosten § 154 Abs. 1 VwGO, vorläufige Vollstreckbarkeit § 167 VwGO i. V. m. §§ 708 Nr. 11, 711 ZPO
– typische Fehler, Hilfsantrag, Klausurtipp, Schema, Merksatz

Normen: § 113 Abs. 1 Satz 4 VwGO; § 173 Satz 1 VwGO i. V. m. § 264 Nr. 2 ZPO; §§ 154 Abs. 1, 167 VwGO; §§ 708 Nr. 11, 711 ZPO; Art. 8 GG.

Landesrecht: Das Versammlungsrecht ist Ländersache. Beispiel im Video ist Nordrhein-Westfalen (§ 13 Abs. 1, 2 VersG NRW). In Ländern ohne eigenes Versammlungsgesetz gilt § 15 VersG des Bundes fort. Tenor, Kosten und Vollstreckbarkeit richten sich überall nach VwGO und ZPO.

Rechtsprechung:
– BVerwG, Urt. v. 16.5.2013 – 8 C 14.12, BVerwGE 146, 303, Rn. 19–21, 25 (Fortsetzungsfeststellungsinteresse)
– BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 15–17, 21 f. (qualifizierter Grundrechtseingriff)
– BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 11, 19, 21 (Umstellung keine Klageänderung; Verpflichtungssituation)
– BVerfG, Beschl. v. 3.3.2004 – 1 BvR 461/03, BVerfGE 110, 77, Rn. 36 f., 41–43 (Versammlungsauflösung, Wiederholungsgefahr)
– VG Gelsenkirchen, Urt. v. 19.7.2022 – 14 K 4207/19 (Tenor bei aufgelöster Versammlung, Kosten, Vollstreckbarkeit)
– VG Düsseldorf, Urt. v. 3.2.2022 – 29 K 78/22, Rn. 18; Urt. v. 25.9.2024 – 18 K 8760/23, Rn. 13 (Umstellung)

Hinweise: Herr Strauch, Herr Nagel und Frau Bollmann sind erfundene Figuren. Mehr dazu: Folge 233 (Prüfungsschema der Fortsetzungsfeststellungsklage), Folge 102 (Anfechtungsurteil und Abwendungsformel), Folge 108 (Bescheidungsurteil).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Fortsetzungsfeststellungsklage #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("siebenhundertelf ZPO", "711 ZPO"), ("tausendfünfhundert Euro", "1.500 Euro"),
                 ("hundertzehn Prozent", "110 Prozent"), ("siebten März 2026", "7. März 2026"), ("rund zwanzig", "rund 20")]:
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["FFK Tenor", "Fortsetzungsfeststellungsinteresse Urteil", "Assessorexamen VwGO"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
