"""Nachbearbeitung der Upload-Texte für Folge 194 (nach meta_192.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung (Förderungskausalität präzisiert),
Fall, Inhalt, Normen, Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Normen).
Aufruf: python3 meta_194.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Hedda leiht Falko ihr Auto"),
       (T("p27"), "§ 27 StGB im Wortlaut"),
       (T("sch"), "Prüfschema: die Haupttat und § 29 StGB"),
       (T("s1b"), "Hilfeleisten: physisch und psychisch"),
       (T("streit"), "Förderungsformel (BGH) oder Kausalität (h. L.)?"),
       (T("s2"), "Doppelter Gehilfenvorsatz"),
       (T("s_ii"), "Rechtswidrigkeit, Schuld, Strafmilderung"),
       (T("loes"), "Lösung: Haupttat und Mittäterschaft"),
       (T("hl"), "Lösung: Hilfeleisten und Vorsatz"),
       (T("erg"), "Ergebnis und Strafrahmen"),
       (T("sf"), "Sukzessive Beihilfe"),
       (T("taxi"), "Neutrale Handlungen und Unterlassen"),
       (T("tipp"), "Klausurtipp"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Beihilfe § 27 StGB: Hilfeleisten (Förderungsformel des BGH oder Kausalität?) und doppelter Gehilfenvorsatz – so prüfst du die Beihilfe in der Klausur.

Der Fall: Falko will in ein bewohntes Einfamilienhaus einbrechen und bittet seine Freundin Hedda um ihr Auto. Sie findet das falsch, gibt ihm aber den Schlüssel. Falko fährt hin, bricht ein und bringt den Schmuck im Kofferraum weg. Hat sich Hedda strafbar gemacht – und wie viel Hilfe macht strafbar?

Inhalt:
– § 27 Abs. 1 und 2 StGB im Wortlaut (zwingende Milderung nach § 49 Abs. 1)
– Prüfschema: vorsätzliche, rechtswidrige Haupttat – limitierte Akzessorietät, § 29 StGB im Wortlaut
– Hilfeleisten: physisch oder psychisch, schon im Vorbereitungsstadium
– Meinungsstand: Förderungsformel der Rechtsprechung (Kausalität für den Erfolg nicht nötig) oder Kausalitätserfordernis der h. L.
– Doppelter Gehilfenvorsatz: Haupttat in ihren wesentlichen Merkmalen (Unrechtsgehalt, Angriffsrichtung), keine Einzelheiten; Vorsatz bezüglich der eigenen Hilfe
– Lösung: Beihilfe zum schweren Wohnungseinbruchdiebstahl (§§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4, 27 StGB); Strafrahmen 3 Monate bis 7 Jahre 6 Monate
– Sonderfälle: sukzessive Beihilfe bis zur Beendigung, neutrale Handlungen (Taxifahrt), Beihilfe durch Unterlassen (§ 13 StGB)
– Klausurtipp (Täterschaft vor Teilnahme) und Merksatz

Normen: §§ 27, 29, 49 Abs. 1 StGB; §§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4 StGB; § 13 Abs. 1 StGB

Rechtsprechung:
– BGH, Urt. v. 1.8.2000 – 5 StR 624/99, BGHSt 46, 107 (Hilfeleisten ohne Kausalität; Gehilfenvorsatz; Missbilligung unerheblich; neutrale Handlungen)
– BGH, Beschl. v. 21.4.2020 – 4 StR 287/19, Rn. 15 (Förderungsformel; Vorbereitungsstadium; bis zur Beendigung)
– BGH, Urt. v. 31.10.2019 – 3 StR 322/19, Rn. 8, 10 (Hilfeleisten; Gehilfenvorsatz: Unrechtsgehalt und Angriffsrichtung)
– BGH, Beschl. v. 7.2.2017 – 3 StR 430/16, Rn. 11 (Tatmittel an die Hand geben; keine Einzelheiten)
– BGH, Beschl. v. 20.9.2016 – 3 StR 49/16, Rn. 18 (psychische Beihilfe; Beihilfe bis zur Beendigung)
– BGH, Urt. v. 22.1.2014 – 5 StR 468/12, Rn. 26 (berufstypische, neutrale Handlungen)
– BGH, Urt. v. 24.6.2020 – 5 StR 671/19, Rn. 10, 13, 37 (Wohnung; dauerhaft genutzte Privatwohnung)

Hinweise: Die Lehrmeinungen (Kausalitätserfordernis der h. L., sukzessive Beihilfe nur bis zur Vollendung) folgen dem Vorlesungsskript von Prof. Dr. Roland Hefendehl (Universität Freiburg, Strafrecht AT, § 29 Teilnahme Teil 2). Das Taxifahrer-Beispiel ist ein Lehrbeispiel, kein BGH-Fall. Prüfschemata sind Klausurkonventionen. Die Abgrenzung zur Mittäterschaft erklärt die Folge „Mittäterschaft § 25 II StGB: Tatplan, Tatbeitrag, Zurechnung“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Jura #Beihilfe
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"§\n(\d+)", r"§ \1\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei)([,:])( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(3), srt)
for vorn, hinten, e1, e2 in [("um zweiundzwanzig", "Uhr", "um 22", "Uhr"), ("für dreitausend", "Euro", "für 3.000", "€"),
                             ("statt ein bis zehn", "Jahren drei Monate", "statt 1 bis 10", "Jahren 3 Monate"),
                             ("bis sieben Jahre", "und sechs Monate", "bis 7 Jahre", "und 6 Monate")]:
    srt, n = re.subn(re.escape(vorn) + r"(\s)" + re.escape(hinten), lambda m: e1 + m.group(1) + e2, srt)
    assert n, vorn
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt and "Römisch" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = [t if t != "Förderungskausalität" else "Förderungsformel" for t in m["tags"]] + \
            ["Beihilfe StGB", "Gehilfenvorsatz", "neutrale Beihilfe", "sukzessive Beihilfe", "Wohnungseinbruchdiebstahl"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen;", len(m["tags"]), "Tags")
