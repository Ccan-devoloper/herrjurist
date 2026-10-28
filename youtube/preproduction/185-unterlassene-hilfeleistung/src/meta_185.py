"""Nachbearbeitung der Upload-Texte für Folge 185 (nach meta_182.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Paragrafen, Ziffern).
Aufruf: python3 meta_185.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: bewusstlos im Vorraum der Bank"),
       (T("p323"), "§ 323c Abs. 1 StGB im Wortlaut"),
       (T("echt"), "Echtes Unterlassungsdelikt: Pflicht für jeden"),
       (T("ungl"), "1. Unglücksfall (Sicht ex ante)"),
       (T("nicht"), "2. Nichthilfeleisten und 3. Erforderlichkeit"),
       (T("zum"), "4. Zumutbarkeit"),
       (T("vors"), "5. Vorsatz und Irrtum"),
       (T("p13"), "§ 13 StGB und § 323c Abs. 2 StGB"),
       (T("loes"), "Lösung: die 4 Kunden"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Unterlassene Hilfeleistung § 323c StGB: Unglücksfall, Erforderlichkeit, Zumutbarkeit – wann wird Wegsehen strafbar?

Der Fall: Im Vorraum einer Bankfiliale bricht ein älterer Mann zusammen und bleibt bewusstlos liegen. In 20 Minuten steigen 4 Kunden über ihn hinweg: einer hat gleich einen Termin, eine meint, gleich kämen andere, einer glaubt, der Mann schlafe nur, eine hat nie Erste Hilfe gelernt. Erst die 5. Kundin wählt den Notruf und bringt ihn in die stabile Seitenlage. Wer hat sich strafbar gemacht?

Inhalt:
– § 323c Abs. 1 StGB im Wortlaut, Strafrahmen
– Echtes Unterlassungsdelikt: Die Pflicht trifft jeden, auch ohne Garantenstellung
– 1. Unglücksfall: BGH-Definition, objektivierte ex-ante-Sicht
– 2. Nichthilfeleisten: geschuldet ist die mögliche Hilfe, oft schon der Notruf
– 3. Erforderlichkeit: andere könnten helfen? Wann die Hilfe nicht mehr erforderlich ist
– 4. Zumutbarkeit: erhebliche eigene Gefahr, andere wichtige Pflichten – Prüfung im Tatbestand
– 5. Vorsatz: Irrtum über den Unglücksfall (§ 16 StGB), keine Fahrlässigkeitsstrafbarkeit
– Abgrenzung zu § 13 StGB und Behinderung von Helfern (§ 323c Abs. 2 StGB)
– Lösung je Kunde, Klausurtipp, Prüfschema, Merksatz

Normen: § 323c Abs. 1 und 2 StGB; §§ 13, 15, 16 StGB

Rechtsprechung:
– BGH, Urt. v. 1.9.2020 – 1 StR 373/19, Rn. 11 f. (Unglücksfall und Erforderlichkeit in objektivierter ex-ante-Sicht; Hilfe auch, wenn sie vergeblich bleibt)
– BGH, Urt. v. 20.10.2011 – 4 StR 71/11 (BGHSt 57, 42), Rn. 20 f. (Definition Unglücksfall; Freispruch wegen nicht geprüftem § 323c aufgehoben)
– BGH, Urt. v. 12.8.2015 – 2 StR 115/15, Rn. 10, 12 (erhebliche Gefahr; Vorsatz)
– BGH, Urt. v. 31.3.2021 – 2 StR 109/20, Rn. 18 (Handlungspflicht, solange keine Gewähr für sofortige anderweitige Hilfe)
– BGH, Beschl. v. 15.9.2015 – 5 StR 363/15, Rn. 5 f. (mögliche Hilfe; Hilfe erübrigt sich bei ausreichender anderweitiger Hilfe)
– BGH, Urt. v. 3.7.2019 – 5 StR 132/18 (BGHSt 64, 121), Rn. 46 (Zumutbarkeit als Tatbestandsmerkmal)
– BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 14, 17 (bloße Kenntnis der Hilfsbedürftigkeit: nur § 323c, keine Garantenstellung)
– BGH, Urt. v. 23.3.1993 – 1 StR 21/93 (BGHSt 39, 164), Rn. 4 f. (Alarmierung von Hilfskräften; Kognitionspflicht)

Hinweise: „Bedingter Vorsatz genügt“ entspricht der herrschenden Meinung. Nicht behandelt: gemeine Gefahr oder Not im Einzelnen, Suizid als Unglücksfall, Konkurrenzen, Strafzumessung. Das unechte Unterlassen zeigen die Folgen „Unterlassungsdelikt“ und „Garantenstellung“. Im Notfall: 112.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #UnterlasseneHilfeleistung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"Römisch(\s)(eins|zwei|drei)([,:]?)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(2)], srt)
srt = re.sub(r"§ 323\nc ", "§ 323c\n", srt)
srt = re.sub(r"§ 323\n\n(\d+\n[^\n]+\n)c ", r"§ 323c\n\n\1", srt)          # „c“ über die Untertitelgrenze
assert not re.search(r"§ 323\s", srt), "§ 323c getrennt"
for a, b in [("\nBrauer: ", "\nHerr Brauer: "), ("\nHauser: ", "\nFrau Hauser: "), ("\nKessel: ", "\nHerr Kessel: "),
             ("\nBuehler: ", "\nFrau Bühler: "), ("nächsten zwanzig\nMinuten kommen vier", "nächsten 20\nMinuten kommen 4"),
             ("fünfte Kundin", "5. Kundin"), ("Haben sich die vier", "Haben sich die 4"), ("hilft zwanzig Minuten", "hilft 20 Minuten"),
             ("nennt zwei Beispiele", "nennt 2 Beispiele"), ("eins, eins, zwei", "112")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert "Buehler" not in srt
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
