"""Nachbearbeitung der Upload-Texte für Folge 179 (nach meta_161.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Beträge, Paragrafen).
Aufruf: python3 meta_179.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Auto des Nachbarn gekauft"),
       (T("p929"), "Einigung und Übergabe – und die Zulassungsbescheinigung"),
       (T("s1"), "1. Übereignung kurzer Hand, § 929 S. 2 BGB"),
       (T("s2"), "2. Besitzkonstitut, § 930 BGB"),
       (T("p868"), "Besitzmittlungsverhältnis, § 868 BGB: konkret!"),
       (T("sue"), "Sicherungsübereignung und Bestimmtheit"),
       (T("s3"), "3. Abtretung des Herausgabeanspruchs, § 931 BGB"),
       (T("tab"), "Merktabelle und Ausblick gutgläubiger Erwerb"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Besitzkonstitut (§ 930), Übereignung kurzer Hand (§ 929 S. 2) und Abtretung des Herausgabeanspruchs (§ 931 BGB): So wird man Eigentümer ohne Übergabe.

Der Fall: Käthe kauft das Auto ihres Nachbarn Herrn Wöhler für 4.000 € und zahlt sofort. Herr Wöhler zieht um und darf den Wagen noch bis Samstag fahren – Käthe leiht ihn ihm. Ist sie trotzdem schon heute Eigentümerin?

Inhalt:
– Einordnung: § 929 S. 1 BGB (Einigung und Übergabe); warum die Zulassungsbescheinigung Teil II die Übergabe nicht ersetzt
– 1. Übereignung kurzer Hand: § 929 S. 2 BGB (im Wortlaut)
– 2. Besitzkonstitut: § 930 BGB und § 868 BGB (im Wortlaut); das Besitzmittlungsverhältnis braucht einen konkreten Inhalt; Sicherungsübereignung und Bestimmtheit
– 3. Abtretung des Herausgabeanspruchs: § 931 BGB (im Wortlaut), §§ 398, 870 BGB, § 986 Abs. 2 BGB
– Merktabelle: Wer hat die Sache – was ersetzt die Übergabe?
– Ausblick: gutgläubiger Erwerb nach §§ 932 Abs. 1 S. 2, 933, 934 BGB
– Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 398, 598, 868, 870, 929, 930, 931, 932, 933, 934, 986 BGB

Rechtsprechung:
– BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 20 (Besitzmittlungsverhältnis braucht einen konkreten Inhalt)
– BGH, Urt. v. 23.9.2022 – V ZR 148/21, Rn. 20 f. (Zulassungsbescheinigung Teil II verbrieft nicht das Eigentum, kein Traditionspapier)
– BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 26 (Entleiher als Besitzmittler)
– BGH, Urt. v. 17.3.2017 – V ZR 70/16, Rn. 16 (Werkvertrag als Besitzmittlungsverhältnis)
– BGH, Urt. v. 11.1.2018 – IX ZR 295/16, Rn. 34 (Abtretung des Herausgabeanspruchs ohne Mitwirkung des Besitzers)
– BGH, Beschl. v. 16.9.2015 – V ZR 8/15, Rn. 7 (Sicherungsübereignung nach § 930 BGB)
– BGH, Urt. v. 16.12.2022 – V ZR 174/21, Rn. 10 (Bestimmtheitsgrundsatz)

Hinweise: Dass eine bloß abstrakte Abrede („ab jetzt besitze ich für dich“) nicht genügt, ist herrschende Meinung; der BGH verlangt einen konkreten Inhalt des Besitzmittlungsverhältnisses. Nicht behandelt: Geheißerwerb, Nebenbesitz, antizipiertes Besitzkonstitut, Werkunternehmerpfandrecht. Den gutgläubigen Erwerb zeigen die Folgen „Gutgläubiger Erwerb §§ 932 ff. BGB“ und „Abhandenkommen § 935 BGB“, Einigung und Übergabe die Folge zu § 929 S. 1 BGB.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Sachenrecht #Besitzkonstitut #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
for a, b in [("viertausend Euro", "4.000 Euro"), ("Teil zwei", "Teil II"), ("gilt S. 2:", "gilt Satz 2:"), ("besitzt: S. 2.", "besitzt: Satz 2."),
             ("neunhundertdreiunddreißig und\nneunhundertvierunddreißig.", "933 und 934.")]:
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
