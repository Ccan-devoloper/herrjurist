"""Nachbearbeitung der Upload-Texte für Folge 259 (nach meta_255.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Hinweis zur Rechtsprechung
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_259.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: E-Bike auf Raten, Anzahlung vom Taschengeld"),
       (T("ansp"), "Anspruch auf die Raten, § 433 II BGB"),
       (T("p107"), "Lediglich rechtlicher Vorteil? § 107 BGB"),
       (T("p108"), "Schwebend unwirksam, § 108 I BGB"),
       (T("p110"), "Der Taschengeldparagraph, § 110 BGB"),
       (T("bewirkt"), "„Bewirkt“ heißt vollständig erfüllt"),
       (T("rate"), "Ratenkauf: erst mit der letzten Rate"),
       (T("eltern"), "Genehmigung, Verweigerung, Aufforderung"),
       (T("erg"), "Ergebnis und Rückabwicklung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Taschengeldparagraph (§ 110 BGB): Wirkt er nur, wenn die Leistung vollständig bewirkt ist – und hängt der Ratenkauf eines 16-Jährigen deshalb bis zur letzten Rate an der Genehmigung der Eltern?

Der Fall: Der 16-jährige Fridolin kauft im Radladen von Herrn Heinemann ein gebrauchtes E-Bike für 900 €. 300 € zahlt er sofort aus seinem gesparten Taschengeld, den Rest von 600 € soll er in 6 Monatsraten zu je 100 € aus künftigem Taschengeld zahlen. Die Eltern fragt er nicht. Am nächsten Tag ruft die Mutter bei Herrn Heinemann an: „Diesen Ratenkauf genehmigen wir nicht.“ Muss Fridolin die restlichen 600 € zahlen?

Inhalt:
– Anspruch auf den Kaufpreis (§ 433 Abs. 2 BGB), beschränkte Geschäftsfähigkeit (§ 106 BGB)
– § 107 BGB im Wortlaut: Die Zahlungspflicht ist ein rechtlicher Nachteil
– § 108 Abs. 1 BGB im Wortlaut: ohne Einwilligung schwebend unwirksam
– § 110 BGB im Wortlaut: Mittel zur freien Verfügung, aber ist die Leistung „bewirkt“?
– „Bewirkt“ heißt vollständig erbracht (vgl. § 362 Abs. 1 BGB); die Anzahlung macht den Kauf nicht teilweise wirksam
– Ratenkauf nach herrschender Lehre: erst mit der letzten Rate wirksam; Kreditgeschäfte deckt § 110 nicht
– Genehmigung (§ 184 BGB), Verweigerung, Aufforderung (§ 108 Abs. 2 BGB)
– Ergebnis und Rückabwicklung (§ 812 BGB)
– Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 106, 107, 108, 110 BGB; § 184 Abs. 1 BGB; § 362 Abs. 1 BGB; § 433 Abs. 2 BGB; § 812 Abs. 1 Satz 1 BGB

Hinweise: Zur Wirkung von § 110 BGB beim Ratenkauf wird im Video die herrschende Lehre dargestellt; eine einschlägige Gerichtsentscheidung haben wir nicht ausgewertet. Fridolin, Herr Heinemann und der Radladen sind erfunden. Das Grundschema zu Minderjährigen zeigt unsere Folge „Geschäftsfähigkeit Schema §§ 104 ff. BGB: Minderjährige im Vertrag“, die Rückabwicklung die Folge „Leistungskondiktion § 812 I 1 Alt. 1 BGB – Prüfungsschema“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Taschengeldparagraph #Minderjährige #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
# Ein Untertitel nur aus „Euro.“ (Zeilenumbruch des Werkzeugs zwischen Zahl und Einheit) wird mit dem vorigen vereint
bl = [b_.split("\n") for b_ in srt.strip().split("\n\n")]
neu = []
for b_ in bl:
    if neu and b_[2:] == ["Euro."]:
        neu[-1][1] = neu[-1][1].split(" --> ")[0] + " --> " + b_[1].split(" --> ")[1]
        neu[-1][-1] += " Euro."
    else:
        neu.append(b_)
srt = "\n\n".join("\n".join([str(i + 1)] + b_[1:]) for i, b_ in enumerate(neu)) + "\n"
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Heinemann: Dreihundert", "Herr Heinemann: Dreihundert")]
for a, b in ERSATZ:
    if a in srt:
        srt = srt.replace(a, b)
ZAHL = [(r"sechzehn", "16"), (r"neunhundert(\s)Euro", r"900\1€"), (r"[Dd]reihundert(\s)Euro", r"300\1€"),
        (r"sechshundert(\s)Euro", r"600\1€"), (r"hundert(\s)Euro", r"100\1€"), (r"sechs(\s)Monatsraten", r"6\1Monatsraten"),
        (r"sechs(\s)Raten", r"6\1Raten"), (r"zwei(\s)Wochen", r"2\1Wochen"), (r"dreihundert(\s)von", r"300\1von")]
for a, b in ZAHL:
    srt = re.sub(a, b, srt)
srt = re.sub(r"(\d)\n€ ?", r"\1 €\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|hundert|tausend", srt, re.I), re.findall(r".{0,30}(?:hundert|tausend).{0,30}", srt, re.I)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
