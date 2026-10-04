"""Nachbearbeitung der Upload-Texte für Folge 191 (Kopie von meta_155.py) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Beschreibungsanfang und Tags an den neuen Zuschnitt (§ 239 Abs. 4 statt § 227) angepasst; römische
Gliederungsziffern in den Untertiteln.
Aufruf: python3 meta_191.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Eingesperrt in der Wohnung"),
       (T("eq"), "Struktur der Erfolgsqualifikation"),
       (T("p18"), "§ 18 StGB im Wortlaut"),
       (T("p112"), "§ 11 Abs. 2 StGB: Teilnahme und Versuch"),
       (T("sch"), "Prüfungsschema I. bis V."),
       (T("p239"), "§ 239 Abs. 4 StGB im Wortlaut"),
       (T("gd"), "Im Fall: Grunddelikt, Folge, Kausalität"),
       (T("spez"), "Spezifischer Gefahrzusammenhang: die Flucht"),
       (T("fahrl"), "Fahrlässigkeit, Schuld und Ergebnis"),
       (T("vers"), "Erfolgsqualifizierter Versuch und versuchte Erfolgsqualifikation"),
       (T("rt"), "Rücktritt (BGHSt 42, 158)"),
       (T("wf"), "Fahrlässig oder leichtfertig (§ 251 StGB)"),
       (T("tipp"), "Klausurtipp"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

ANFANG = ("Erfolgsqualifiziertes Delikt Schema: Grunddelikt, schwere Folge, spezifischer Gefahrzusammenhang und "
          "Fahrlässigkeit nach § 18 StGB – am Beispiel der Freiheitsberaubung mit Todesfolge, § 239 Abs. 4 StGB.")
BESCHR = f"""{ANFANG}

Der Fall: Bertram und Hubertus wohnen zusammen in einer Wohnung im 2. Stock. Nach einem Streit schließt Bertram Hubertus in seinem Zimmer ein und nimmt den Schlüssel mit. Hubertus will hinaus, steigt aus dem Fenster, stürzt ab und stirbt. Bertram wollte ihn nur eine Weile einsperren. Haftet er für den Tod – und wie prüfst du ein erfolgsqualifiziertes Delikt?

Inhalt:
– Struktur: vorsätzliches Grunddelikt plus schwere Folge
– § 18 StGB im Wortlaut: wenigstens Fahrlässigkeit hinsichtlich der Folge
– § 11 Abs. 2 StGB im Wortlaut: die Vorsatz-Fahrlässigkeits-Kombination gilt als vorsätzliche Tat – Anstiftung, Beihilfe und Versuch möglich
– Prüfungsschema: I. Grunddelikt, II. schwere Folge und Kausalität, III. spezifischer Gefahrzusammenhang, IV. wenigstens Fahrlässigkeit (bzw. Leichtfertigkeit), V. Rechtswidrigkeit und Schuld
– § 239 Abs. 1, 4 StGB im Wortlaut; Einsperren trotz Fenster
– Gefahrzusammenhang: der Fluchtversuch als typische Gefahr der Freiheitsberaubung; Abgrenzung zur frei verantwortlichen Selbstgefährdung
– Vorhersehbarkeit beim Fluchtversuch
– Erfolgsqualifizierter Versuch und versuchte Erfolgsqualifikation; Rücktritt vom erfolgsqualifizierten Versuch
– „wenigstens fahrlässig“ oder „leichtfertig“ (§ 251 StGB)
– Klausurtipp und Merksatz
– Der Faustschlag mit tödlichem Sturz (§ 227 StGB): Video „Schwere Körperverletzung & Todesfolge“; Vorsatzformen und Fahrlässigkeitsdelikt: eigene Videos

Normen: §§ 11 Abs. 2, 18, 239 Abs. 1 und 4, 251 StGB; §§ 26, 27 StGB

Rechtsprechung:
– BGH, Beschl. v. 15.2.2017 – 4 StR 375/16 (BGHSt 62, 49), Rn. 14 f., 17, 20, 22 (spezifischer Gefahrzusammenhang; Verhalten des Opfers; Vorhersehbarkeit)
– BGH, Urt. v. 28.1.2021 – 3 StR 279/20, Rn. 18 (Freiheitsberaubung, Sturz aus dem Fenster; Selbstbefreiungsversuch, mit BGHSt 19, 382, 386 f.; Vorhersehbarkeit beim Fluchtversuch)
– BGH, Beschl. v. 8.3.2001 – 1 StR 590/00, Rn. 1 (Einsperren muss nicht unüberwindlich sein)
– BGH, Urt. v. 12.8.2021 – 3 StR 415/20, Rn. 9, 12, 15 (erfolgsqualifizierter Versuch und versuchte Erfolgsqualifikation; § 11 Abs. 2)
– BGH, Urt. v. 14.5.1996 – 1 StR 51/96 (BGHSt 42, 158), Rn. 12, 16 f., 26 (Rücktritt vom versuchten Raub mit Todesfolge)
– BGH, Urt. v. 3.6.2015 – 5 StR 628/14, Rn. 8 (Leichtfertigkeit)

Hinweise: Die Lösung am Übungsfall (Fluchtversuch als typische Gefahr der Freiheitsberaubung, Vorhersehbarkeit) ist eine Wertung auf Grundlage dieser Maßstäbe; die Entscheidung von 2021 betraf eine schwere Gesundheitsschädigung (§ 239 Abs. 3 Nr. 2 StGB). Die Aufteilung der Vorhersehbarkeit auf Tatbestand und Schuld folgt dem üblichen Klausuraufbau. Konkurrenzen und minder schwere Fälle prüft das Video nicht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Jura #ErfolgsqualifiziertesDelikt
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for w, z in (("eins", "I."), ("zwei", "II."), ("drei", "III."), ("vier", "IV."), ("fünf", "V.")):
    srt = re.sub(rf"Römisch {w}[:,]", z, srt)
    srt = srt.replace(f"Römisch {w}", z)
assert "Römisch" not in srt and "zweihundert" not in srt
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = [t if t != "§ 227 StGB" else "§ 239 Abs. 4 StGB" for t in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
