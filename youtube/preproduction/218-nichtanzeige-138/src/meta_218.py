"""Nachbearbeitung der Upload-Texte für Folge 218 (nach meta_185.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Paragrafen, Ziffern).
Aufruf: python3 meta_218.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: der Überfall-Plan im Chat"),
       (T("p138"), "§ 138 Abs. 1 StGB im Wortlaut (Nr. 7)"),
       (T("echt"), "Echtes Unterlassungsdelikt"),
       (T("kat"), "1. Geplante Katalogtat und Vorhaben"),
       (T("glaub"), "2. Glaubhafte Kenntnis"),
       (T("rz"), "3. Rechtzeitig"),
       (T("anz"), "4. Unterlassen der Anzeige und 5. Vorsatz"),
       (T("p139"), "§ 139 StGB: Angehörige"),
       (T("abs4"), "§ 139 Abs. 4, 2 und 1"),
       (T("bet"), "Abgrenzung: Beteiligte und § 323c StGB"),
       (T("loes"), "Lösung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Nichtanzeige geplanter Straftaten (§§ 138, 139 StGB): Katalogtat, glaubhafte Kenntnis, rechtzeitige Anzeige – wann macht Schweigen strafbar?

Der Fall: Sören liest im privaten Chat, dass sein Freund Mirko am Samstag den Juwelier am Markt überfallen will. Auf Nachfrage bestätigt Mirko: kein Witz. Sören schweigt, weil er seinen Freund nicht verraten will. Am Samstag versucht Mirko den Überfall. Hat sich Sören strafbar gemacht?

Inhalt:
– § 138 Abs. 1 StGB im Wortlaut, Raub und räuberische Erpressung in Nr. 7, Strafrahmen
– Echtes Unterlassungsdelikt: keine Garantenstellung nötig
– 1. Geplante Katalogtat: abschließender Katalog, Vorhaben als ernsthafter Tatplan
– 2. Glaubhafte Kenntnis
– 3. Rechtzeitig: nicht sofort, aber so früh, dass die Tat noch verhindert werden kann
– 4. Unterlassen der Anzeige bei Behörde oder Bedrohtem
– 5. Vorsatz, leichtfertige Nichtanzeige nach § 138 Abs. 3 StGB
– § 139 StGB: Angehörige (§ 11 Abs. 1 Nr. 1 StGB), Abwendung auf andere Weise, Geistliche, nicht versuchte Tat
– Abgrenzung: Beteiligte an der Tat, unterlassene Hilfeleistung (§ 323c StGB)
– Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 138, 139 StGB; § 11 Abs. 1 Nr. 1 StGB

Rechtsprechung:
– BGH, Urt. v. 19.5.2010 – 5 StR 464/09 (NJW 2010, 2291), Rn. 7, 14 f., 17 (Beteiligte nicht anzeigepflichtig; bei fortbestehendem Beteiligungsverdacht Verurteilung nach § 138 StGB)
– BGH, Urt. v. 10.8.2016 – 2 StR 493/15, Rn. 42 (nach Zusage keine fremde Tat: keine Anzeigepflicht)
– BGH, Beschl. v. 10.11.2016 – StB 33/16, Rn. 22 (Vorhaben: ernsthafter Tatplan, Grundzüge festgelegt)
– BGH, Beschl. v. 10.8.2017 – AK 33/17, Rn. 28 (glaubhaft erfahren: ernsthaft mit der Ausführung rechnen)
– BGH, Urt. v. 19.3.1996 – 1 StR 497/95 (BGHSt 42, 86), Rn. 6 f. (Anzeige muss nicht unverzüglich, aber rechtzeitig erfolgen)

Hinweise: Nicht behandelt: § 138 Abs. 2 StGB (Terrorismus), § 139 Abs. 3 Satz 2 und 3 StGB (Berufsgeheimnisträger), die dogmatische Einordnung der Ausnahmen des § 139 StGB, Konkurrenzen, Strafzumessung. Die unterlassene Hilfeleistung erklärt die Folge „Unterlassene Hilfeleistung § 323c“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Nichtanzeige #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"Römisch(\s)(eins|zwei|drei|vier)([,:]?)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(2)], srt)
for a, b in [("\nSoeren: ", "\nSören: "), ("achtzehn Uhr", "18 Uhr"), ("achtzehn\nUhr", "18\nUhr")]:
    srt = srt.replace(a, b)
assert "Soeren" not in srt
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt and "achtzehn" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
