"""Nachbearbeitung der Upload-Texte für Folge 092 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen zu Sätzen ohne
Aktenzeichen und Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_092.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Plattenspieler nach der Trennung"),
       (T("p985"), "§ 985 BGB: Wortlaut und Prüfungspunkte"), (T("eig"), "I. Eigentum historisch prüfen"),
       (T("p1006"), "Eigentumsvermutung, § 1006 BGB"), (T("bes"), "II. Besitz"),
       (T("rzb"), "III. Kein Recht zum Besitz, § 986 BGB"), (T("eigen"), "Eigenes und abgeleitetes Besitzrecht"),
       (T("einw"), "Einwendung und Beweislast"), (T("erg"), "Ergebnis: Herausgabe als Holschuld"),
       (T("p604"), "§ 604 BGB und Ausblick §§ 987 ff. BGB"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 985 BGB im Schema: Eigentum, Besitz, kein Recht zum Besitz (§ 986 BGB). Wie du das Eigentum historisch prüfst – am Plattenspieler, den der Ex behalten hat.

Der Fall: Theresa kauft sich einen Plattenspieler, lange bevor sie mit Clemens zusammenzieht. In der gemeinsamen Wohnung erlaubt sie ihm, ihn mitzubenutzen. Nach der Trennung zieht sie aus, der Plattenspieler bleibt bei Clemens. Kann Theresa ihn herausverlangen?

Inhalt:
– Anspruchsgrundlage § 985 BGB im Wortlaut, drei Prüfungspunkte
– I. Eigentum des Anspruchstellers, historisch geprüft: Erwerb vom Händler (§ 929 S. 1 BGB), kein Verlust durch das Zusammenziehen, kein Erwerb Dritter; Eigentumsvermutung § 1006 BGB
– II. Besitz des Anspruchsgegners: tatsächliche Gewalt (§ 854 I BGB), auch mittelbarer Besitz (§ 868 BGB)
– III. Kein Recht zum Besitz (§ 986 I 1 BGB im Wortlaut): eigenes Besitzrecht aus Leihe (§§ 598, 604 BGB) und sein Ende, abgeleitetes Besitzrecht, Einwendung statt Einrede, Beweislast
– Rechtsfolge: Herausgabe am Ort der Sache (Holschuld); daneben § 604 BGB; Ausblick Eigentümer-Besitzer-Verhältnis (§§ 987 ff. BGB)
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 985, 986 BGB; §§ 598, 604, 854, 868, 929, 1006 BGB; §§ 987 ff. BGB

Rechtsprechung:
– BGH, Versäumnisurt. v. 3.3.2017 – V ZR 268/15, Rn. 18, 27 (Eigentumsvermutung des § 1006 BGB und ihre Widerlegung)
– BGH, Beschl. v. 10.3.2021 – XII ZB 243/20, Rn. 41, 42 (Recht zum Besitz aus Nutzungsvereinbarung, etwa Leihe; Darlegungs- und Beweislast beim Besitzer)

Hinweise: „Einwendung, von Amts wegen zu beachten“ und „Herausgabe am Ort der Sache (Holschuld)“ geben die herrschende Auffassung wieder; im Video ohne Aktenzeichen. Das Prüfungsschema ist Klausurkonvention.

Mehr dazu: Folge 80 (Übereignung nach § 929 S. 1 BGB), Folge 83 (gutgläubiger Erwerb), Folge 27 (Besitz und Eigentum).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#985BGB #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
