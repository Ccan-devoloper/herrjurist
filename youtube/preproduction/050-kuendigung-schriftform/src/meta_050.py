"""Nachbearbeitung der Upload-Texte für Folge 050 (Ausgabe von tools/youtube_metadaten.py, gemeinsame Datei unverändert).
Aufruf: python3 meta_050.py <roh-ordner> <upload-ordner>
- Kapitel: sprechende Namen, alle ≥ 10 s, Zeiten aus ../cues.json (Hauptfilm + 8,0 s Intro, abgerundet)
- Beschreibung: Planbeginn ergänzt (Klagefrist), Fall, Kapitel, Normen, Rechtsprechung mit Rn., Rechtsstand, Lizenzen
- Untertitel: „Römisch eins“ → „I.“ usw., Jahreszahl in Ziffern, Sprecher mit „Frau“
- Tags: um Klagefrist und § 125 ergänzt"""
import json, math, os, re, sys, shutil

roh, ziel = sys.argv[1], sys.argv[2]
os.makedirs(ziel, exist_ok=True)
cj = json.load(open("../cues.json"))
t = lambda c: cj["cues"][c]["t"] + 8.0


def mmss(s):
    s = math.floor(s)
    return f"{s // 60}:{s % 60:02d}"


KAP = [(0.0, "Der Fall: Kündigung per WhatsApp"), (t("frage"), "Die Frage und der Sachverhalt"),
       (t("pruef"), "Prüfungsaufbau und I. Kündigungserklärung"), (t("form"), "II. Schriftform: Wortlaut § 623 BGB"),
       (t("stand"), "Rechtsstand 2026: § 623 BGB unverändert"), (t("p126"), "§ 126 Abs. 1 BGB: eigenhändige Unterschrift"),
       (t("subs"), "Foto, Fax, E-Mail?"), (t("nichtig"), "Rechtsfolge: nichtig, § 125 S. 1 BGB"),
       (t("zug"), "III. Zugang, § 130 BGB"), (t("vertr"), "IV. Vertretung: Zurückweisung, § 174 BGB"),
       (t("klage"), "V. Klagefrist, §§ 4, 7 KSchG, und Ergebnis"), (t("tipp"), "Klausurtipp: Fehlerquelle Klagefrist"),
       (t("sch"), "Klausurschema"), (t("merke"), "Merksatz")]
for (a, _), (b, n) in zip(KAP, KAP[1:]):
    assert b - a >= 10, f"Kapitel zu kurz vor {n}"
kapitel = [(mmss(a), n) for a, n in KAP]
kap_txt = "\n".join(f"{a} {n}" for a, n in kapitel)

BESCHREIBUNG = f"""Kündigung per WhatsApp: Reicht ein Foto des unterschriebenen Kündigungsschreibens für die Schriftform des § 623 BGB? Nein – und ohne schriftliche Kündigung läuft auch die dreiwöchige Klagefrist des § 4 KSchG nicht. Dazu Zugang (§ 130 BGB) und Zurückweisung nach § 174 BGB.

Der Fall: Werkstattinhaberin Frau Kuhlmann unterschreibt die Kündigung ihres Mechanikers Bastian, fotografiert das Schreiben und schickt das Foto per WhatsApp. Das Original bleibt im Ordner. Fünf Wochen später klagt Bastian – zu spät, meint Frau Kuhlmann. Hat sie recht?

Im Video:
– Wortlaut § 623 BGB: Schriftform, elektronische Form ausgeschlossen; Rechtsstand 2026
– § 126 Abs. 1 BGB: eigenhändige Namensunterschrift, Zugang der unterschriebenen Urkunde
– Foto, Fax, Scan, E-Mail und die Rechtsfolge (§ 125 S. 1 BGB)
– Zugang des Originals (§ 130 BGB) und Zurückweisung ohne Vollmachtsurkunde (§ 174 BGB)
– Klagefrist: § 4 S. 1 KSchG knüpft an die schriftliche Kündigung an, § 7 KSchG
– Klausurtipp (gesetzliche oder vereinbarte Schriftform, § 127 Abs. 2 BGB), Klausurschema und Merksatz

Kapitel:
{kap_txt}

Normen: §§ 125, 126, 127, 130, 174, 623 BGB; §§ 4, 7 KSchG

Rechtsprechung:
– BAG, Urteil vom 17.12.2015 – 6 AZR 709/14, Rn. 27, 46–48, 51 (Kündigung per Telefax formnichtig; Zweck der Schriftform; Treu und Glauben)
– BAG, Urteil vom 10.05.2016 – 9 AZR 145/15, Rn. 30–31 (die formgerecht errichtete Erklärung muss zugehen; Ablichtung genügt nicht)
– BAG, Urteil vom 06.09.2012 – 2 AZR 858/11, Rn. 11, 16 (Formmangel auch nach Ablauf der Dreiwochenfrist geltend zu machen)
– BAG, Urteil vom 07.05.2026 – 2 AZR 130/25, Rn. 17, 26, 29, 34–36 (§ 174 BGB: Zurückweisung, Wochenfrist, Inkenntnissetzen; elektronische Kündigung formnichtig)

Rechtsstand: 2. Oktober 2026. § 623 BGB ist unverändert; das Vierte Bürokratieentlastungsgesetz (BGBl. 2024 I Nr. 323) hat andere Formvorschriften gelockert, etwa für das Arbeitszeugnis (§ 109 Abs. 3 GewO), § 623 BGB aber nicht.

Der Fall ist ein Übungsfall. Prüfungsschemata sind Klausurkonventionen, keine gesetzlichen Vorgaben.

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT); Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#KündigungperWhatsApp #Arbeitsrecht #Jura"""

m = json.load(open(os.path.join(roh, "metadaten.json")))
m["beschreibung"] = BESCHREIBUNG
m["kapitel"] = [list(k) for k in kapitel]
m["tags"] = m["tags"] + ["Klagefrist § 4 KSchG", "§ 125 BGB"]
json.dump(m, open(os.path.join(ziel, "metadaten.json"), "w"), ensure_ascii=False, indent=1)
open(os.path.join(ziel, "beschreibung.txt"), "w").write(BESCHREIBUNG + "\n")
open(os.path.join(ziel, "kapitel.txt"), "w").write(kap_txt + "\n")

srt = open(os.path.join(roh, "untertitel.srt")).read()
for a, b in [("Römisch eins:", "I."), ("Römisch zwei:", "II."), ("Römisch drei:", "III."), ("Römisch vier:", "IV."),
             ("Römisch fünf:", "V."), ("zweitausendvierundzwanzig", "2024"), ("Kuhlmann: ", "Frau Kuhlmann: "),
             ("Petersen: ", "Frau Petersen: "), ("Satz zwei", "S. 2"), ("Satz eins", "S. 1")]:
    srt = srt.replace(a, b)
srt = srt.replace("Frau Frau ", "Frau ")
open(os.path.join(ziel, "untertitel.srt"), "w").write(srt)
print(len(kapitel), "Kapitel,", len(m["tags"]), "Tags ->", ziel)
