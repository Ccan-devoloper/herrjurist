"""Nachbearbeitung der Upload-Texte für Folge 268 (nach meta_265.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, „§§ 269“ → „§ 269“).
Aufruf: python3 meta_268.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: zum dritten Mal reparieren?"),
       (T("sv"), "Sachverhalt und Ausgangslage"),
       (T("p439"), "1. Wahlrecht des Käufers, § 439 Abs. 1 BGB"),
       (T("ort"), "2. Ort der Nacherfüllung (§ 269 BGB)"),
       (T("p4"), "3. Verweigerung: relative und absolute Unverhältnismäßigkeit (§ 439 Abs. 4 BGB)"),
       (T("rsub"), "3. Verweigerung im Fall"),
       (T("ruek"), "4. Fehlgeschlagen? § 440 BGB"),
       (T("vgk"), "Beim Verbraucher: § 475d BGB und § 475 Abs. 4 BGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Nacherfüllung § 439 BGB: Wer wählt zwischen Reparatur und Neulieferung, wo ist nachzuerfüllen, wann darf der Verkäufer verweigern und wann ist sie fehlgeschlagen (§ 440 BGB, beim Verbraucher § 475d BGB)?

Der Fall: Undine kauft im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. 3 Wochen später schaltet es sich immer wieder von selbst aus. Herr Stelzer repariert zweimal – ohne Erfolg. Jetzt will er es ein drittes Mal reparieren, Undine will endlich ein neues Handy. Ein neues kostet ihn 450 €, eine Reparatur nur 60 €. Wer entscheidet? Und kann Undine sogar ohne weitere Frist zurücktreten?

Inhalt:
– § 439 Abs. 1 BGB im Wortlaut: Das Wahlrecht hat der Käufer; Wechsel von der Reparatur zur Lieferung (BGH VIII ZR 66/17)
– Ort der Nacherfüllung: § 269 BGB, beim Kauf im Laden regelmäßig beim Verkäufer; Kosten trägt der Verkäufer (§ 439 Abs. 2 BGB)
– § 439 Abs. 4 BGB im Wortlaut: relative und absolute Unverhältnismäßigkeit; kein Verweis auf eine Reparatur, die den Mangel nicht nachhaltig beseitigt
– § 440 S. 2 BGB im Wortlaut: Nachbesserung nach dem zweiten erfolglosen Versuch in der Regel fehlgeschlagen
– Beim Verbrauchsgüterkauf: § 475d Abs. 1 Nr. 2 BGB statt § 440 BGB – keine feste Zahl an Versuchen; Informationspflicht nach § 475 Abs. 4 BGB (Käufe ab 31.7.2026)
– Ergebnis, Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 437 Nr. 1, 2, 439 Abs. 1, 2, 4, 440, 441, 475 Abs. 4, 475d Abs. 1 Nr. 2, 475e Abs. 5, 477 BGB; § 269 BGB; Art. 229 § 72 EGBGB

Rechtsprechung: BGH, Urt. v. 24.10.2018 – VIII ZR 66/17 (Leitsätze 3a, 4c; Rn. 42 f., 47 f., 57, 59, 76); BGH, Urt. v. 13.4.2011 – VIII ZR 220/10 (Rn. 29, 33); BGH, Urt. v. 19.7.2017 – VIII ZR 278/16 (Rn. 21); BGH, Urt. v. 4.4.2014 – V ZR 275/12 (Rn. 39). Gesetzesbegründung: BT-Drs. 19/27424, S. 37 (zu § 475d Abs. 1 Nr. 2).

Hinweise: Undine und Herr Stelzer sind erfunden; der Laden ist fiktiv. Die zitierten BGH-Entscheidungen ergingen zu § 439 BGB vor 2022 (Abs. 4 hieß bis 2017 Abs. 3); die Rechtssätze betreffen unveränderten Wortlaut. Alle Käuferrechte zeigt unsere Folge „§ 437 BGB: Die Käuferrechte auf einen Blick“, die Kosten für Ausbau und Einbau die Folge „Aus- und Einbaukosten § 439 III BGB: Der Fliesen-Fall Weber/Putz“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Nacherfüllung #Kaufrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(^|\n)Stelzer: ", r"\1Herr Stelzer: ", srt)
ZAHL = [(r"sechshundert(\n\n\d+\n[^\n]+\n)Euro\. ", r"600 €.\1"), (r"sechshundert(\s)Euro", r"600\1€"), (r"[Vv]ierhundertfünfzig(\s)Euro", r"450\1€"),
        (r"vierhundertfünfzig(\s)mit sechzig(\s)Euro", r"450\1mit 60\2€"), (r"nur sechzig\.", "nur 60."),
        (r"Drei(\s)Wochen", r"3\1Wochen"), (r"einunddreißigsten(\s)Juli", r"31.\1Juli"), (r"zwölf(\s)Monate", r"12\1Monate"),
        (r"§§ 269", "§ 269"), (r"Und S\. 2:", "Und Satz 2:"), (r"Römisch eins:", "I."), (r"Römisch zwei:", "II."), (r"Römisch drei:", "III."),
        (r"Römisch vier:", "IV."), (r"Römisch fünf:", "V.")]
for a, b in ZAHL:
    srt = re.sub(a, b, srt)
srt = re.sub(r"(\d)\n€ ?", r"\1 €\n", srt)
assert not re.search(r"§\n|hundert|sechzig|zwölf|Römisch|§§ 269|(^|\n)Stelzer:", srt), "SRT-Korrektur unvollständig"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
