"""Nachbearbeitung der Upload-Texte für Folge 161 (nach meta_158.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Beträge).
Aufruf: python3 meta_161.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Zwei Fälle: verliehene und gestohlene Kamera"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("nb"), "Die Weiche: § 935 Abs. 1 S. 1 BGB im Wortlaut"),
       (T("begr"), "1. Abhandenkommen: unfreiwilliger Besitzverlust"),
       (T("mb"), "2. Mittelbarer Besitz: § 935 Abs. 1 S. 2 BGB"),
       (T("bd"), "3. Besitzdiener § 855 BGB"),
       (T("probe"), "Probefahrt: kein Besitzdiener"),
       (T("abs2"), "4. Ausnahmen: § 935 Abs. 2 BGB"),
       (T("wert"), "5. Wertung: Wer freiwillig weggibt, trägt das Risiko"),
       (T("loes"), "6. Lösung beider Fälle"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Abhandenkommen § 935 BGB: Wann ist eine Sache abhandengekommen, was gilt beim Besitzdiener – und warum kann die verliehene Kamera weiterverkauft werden, die gestohlene nicht?

Zwei Fälle: Hella leiht ihre Kamera ihrem Freund Knut. Knut verkauft sie auf dem Flohmarkt als seine eigene an Berta. Im zweiten Fall stiehlt ein Dieb die Kamera im Park und verkauft sie ebenfalls an Berta. Beide Male ist Berta gutgläubig. Wird sie jedes Mal Eigentümerin?

Inhalt:
– Einordnung: gutgläubiger Erwerb nach §§ 929 S. 1, 932 BGB und die Sperre des § 935 Abs. 1 S. 1 BGB (im Wortlaut)
– 1. Abhandenkommen: unfreiwilliger Verlust des unmittelbaren Besitzes; Täuschung macht die Besitzaufgabe nicht unfreiwillig
– 2. Mittelbarer Besitz: § 935 Abs. 1 S. 2 BGB (im Wortlaut) – es kommt auf den Besitzmittler an
– 3. Besitzdiener: § 855 BGB (im Wortlaut); eigenmächtige Weggabe; Probefahrt-Fall des BGH
– 4. Ausnahmen: § 935 Abs. 2 BGB (im Wortlaut) mit § 979 Abs. 1a BGB
– 5. Wertung: Wer freiwillig aus der Hand gibt, trägt das Risiko (in der Lehre: Veranlassungsprinzip); die Sperre gilt auch für weitere Käufer
– 6. Lösung beider Fälle mit § 985 BGB, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 855, 868, 929, 932, 935, 979, 985 BGB

Rechtsprechung:
– BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 11, 13, 15 (Begriff des Abhandenkommens; Wertung; Dauer der Sperre)
– BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9, 16, 21 (Täuschung macht nicht unfreiwillig; Probefahrer ist kein Besitzdiener)
– BGH, Urt. v. 13.12.2013 – V ZR 58/13, Rn. 9, 16, 19 (Besitzdiener; Verlust nur des mittelbaren Besitzes genügt nicht)

Hinweise: Wann die eigenmächtige Weggabe durch einen Besitzdiener ein Abhandenkommen begründet, ist im Einzelnen streitig; das Video nennt nur die Linie der Rechtsprechung. „Veranlassungsprinzip“ ist ein Lehrbegriff. Nicht behandelt: Besitzlockerung, Mitbesitz, Erbenbesitz, Ersitzung sowie die Ansprüche gegen Knut und den Dieb. Das Schema des gutgläubigen Erwerbs zeigt die Folge „Gutgläubiger Erwerb §§ 932 ff. BGB“, Besitz und Besitzdiener die Folge „Besitz und Eigentum“, den Herausgabeanspruch die Folge zu § 985 BGB.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Sachenrecht #Abhandenkommen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for a, b in [("dreihundert Euro", "300 Euro"), ("bis neunhundertvierunddreißig,", "bis 934,")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
