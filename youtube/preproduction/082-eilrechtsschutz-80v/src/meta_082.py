"""Nachbearbeitung der Upload-Texte für Folge 082 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Hinweis zum Landesrecht, Rechtsprechung mit Rn.,
Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_082.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Imbiss wird sofort geschlossen"), (T("klage"), "Klage, Frage und Sachverhalt"),
       (T("wl801"), "Grundsatz: aufschiebende Wirkung, § 80 I VwGO"), (T("wl802"), "Entfallen nach § 80 II VwGO"),
       (T("wl805"), "Antrag nach § 80 V 1 VwGO"), (T("zul"), "A. Zulässigkeit"),
       (T("begr"), "B. I. Formelle Rechtmäßigkeit der Anordnung, § 80 III VwGO"),
       (T("abw"), "B. II. Interessenabwägung"), (T("egl"), "Erfolgsaussichten im Fall"),
       (T("eilig"), "Besonderes Vollzugsinteresse und Beschluss"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 80 V VwGO Schema: aufschiebende Wirkung, Sofortvollzug nach § 80 II und Interessenabwägung – so stoppst du einen sofort vollziehbaren Bescheid im Eilverfahren.

Der Fall: Die Lebensmittelüberwachung findet in der Imbissbude von Herrn Hinrichs Mäusekot. Die Stadt schließt den Imbiss, bis die Mäuse bekämpft sind, und ordnet die sofortige Vollziehung an. Herr Hinrichs klagt – darf er jetzt wieder öffnen, und was kann er sofort tun? (Übungsfall)

Inhalt:
– Grundsatz: Widerspruch und Anfechtungsklage haben aufschiebende Wirkung (§ 80 I 1 VwGO)
– Entfallen nach § 80 II 1 Nr. 1–4 VwGO, hier Anordnung der sofortigen Vollziehung (Nr. 4)
– Antrag nach § 80 V 1 VwGO: Anordnung (Nr. 1–3a) oder Wiederherstellung (Nr. 4) der aufschiebenden Wirkung
– A. Zulässigkeit: Verwaltungsrechtsweg (§ 40 I 1 VwGO), Statthaftigkeit (Abgrenzung zu § 123 VwGO, § 123 V), Antragsbefugnis (§ 42 II VwGO analog), Antragsgegner (§ 78 VwGO analog), Rechtsschutzbedürfnis (§ 80 V 2, VI VwGO)
– B. Begründetheit: formelle Rechtmäßigkeit der Vollziehungsanordnung (Zuständigkeit, Begründung nach § 80 III 1 VwGO, Anhörung umstritten), Interessenabwägung nach den Erfolgsaussichten, besonderes Vollzugsinteresse, Folgenabwägung
– Im Fall: Schließung nach Art. 138 II h VO (EU) 2017/625 wegen Verstoßes gegen die Hygienevorschriften (VO (EG) Nr. 852/2004)
– Beschluss, Klausurtipp (§ 39 VII LFGB), Klausurschema, Merksatz

Landesrecht: Ob vor der Klage ein Widerspruch nötig ist und ob der Antrag gegen die Behörde selbst zu richten ist (§ 78 I Nr. 2 VwGO), regelt jedes Land selbst – bitte im Recht deines Landes nachschlagen. Auch welche Behörde die Lebensmittelüberwachung führt, bestimmt das Landesrecht.

Rechtsprechung:
– BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8 (eigene Interessenabwägung, summarische Prüfung, Folgenabwägung)
– OVG NRW, Beschl. v. 16.1.2020 – 15 B 814/19, Rn. 9 (offensichtlich rechtswidrig / rechtmäßig / offen)
– OVG NRW, Beschl. v. 12.7.2024 – 4 B 1116/23, Rn. 7 f., 43 (Begründung nach § 80 III 1 VwGO, besonderes Vollzugsinteresse)
– OVG NRW, Beschl. v. 17.2.2025 – 7 B 34/25, Rn. 3 (formelles Begründungserfordernis)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Eilrechtsschutz #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nHinrichs:", "\nHerr Hinrichs:"), ("\nSteinke:", "\nFrau Steinke:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
