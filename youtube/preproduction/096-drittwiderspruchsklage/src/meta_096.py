"""Nachbearbeitung der Upload-Texte für Folge 096 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_096.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Omas Gemälde wird beim Enkel gepfändet"), (T("frage"), "Frage und Sachverhalt"),
       (T("zul"), "Statthaftigkeit, § 771 Abs. 1 ZPO"), (T("a766"), "Abgrenzung zu § 766 und § 805 ZPO"),
       (T("zust"), "Zuständigkeit, Streitwert und Parteien"), (T("rsb"), "Rechtsschutzbedürfnis"),
       (T("begr"), "Begründetheit: Eigentum als die Veräußerung hinderndes Recht"),
       (T("beweis"), "Beweislast und Eigentumsvermutung, § 1006 BGB"), (T("einw"), "Einwendungen, Ergebnis und Tenor"),
       (T("tipp"), "Klausurtipp: der Eilantrag"),
       (T("wl769"), "Einstweilige Einstellung, §§ 771 III, 769, 770 ZPO"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Drittwiderspruchsklage nach § 771 ZPO: Wann ist sie statthaft, welche Rechte hindern die Veräußerung, und welche Einwendungen hat der Gläubiger? Das komplette Klausurschema für das 2. Examen.

Der Fall: Frau Wendland lässt ihre Wohnung renovieren und gibt ihr Ölgemälde so lange ihrem Enkel zur Aufbewahrung. Der Enkel, ein Student, hat beim Fahrradhändler Schulden. Die Gerichtsvollzieherin pfändet das Gemälde in seiner Wohnung – die Versteigerung ist schon angesetzt. Wie wehrt sich die Großmutter, und wie stoppt sie die Versteigerung rechtzeitig? (Übungsfall)

Inhalt:
– A. Zulässigkeit: Statthaftigkeit nach dem Wortlaut des § 771 Abs. 1 ZPO; Abgrenzung zur Erinnerung (§ 766 ZPO) und zur Klage auf vorzugsweise Befriedigung (§ 805 ZPO); Zuständigkeit (örtlich ausschließlich, §§ 771 Abs. 1, 802 ZPO; sachlich nach dem Streitwert, § 6 ZPO, §§ 23, 71 GVG); Parteien (§ 771 Abs. 2 ZPO); Rechtsschutzbedürfnis vom Beginn bis zur Beendigung der Vollstreckung
– B. Begründetheit: Eigentum als die Veräußerung hinderndes Recht; Verwahrung und mittelbarer Besitz (§§ 688, 868 BGB); Beweislast und Eigentumsvermutung (§ 1006 Abs. 1, 3 BGB); keine Einwendungen des Beklagten
– Tenor als Klausurkonvention
– Klausurtipp: einstweilige Einstellung über § 771 Abs. 3 i. V. m. §§ 769, 770 ZPO, Glaubhaftmachung, Vorlage nach § 775 Nr. 2 ZPO
– Klausurschema und Merksatz

Rechtsprechung:
– BGH, Urt. v. 5.7.2007 – III ZR 143/06, Rn. 9, 12 (Gerichtsvollzieher prüft grundsätzlich nur den Gewahrsam; der Dritte klagt nach § 771 ZPO gegen den Gläubiger)
– BGH, Urt. v. 14.9.2018 – V ZR 267/17, Rn. 2, 6 (Übergriff der Vollstreckung auf das Vermögen eines Dritten, das nicht für die Titelforderung haftet)
– BGH, Beschl. v. 7.2.2008 – IX ZR 69/05, Rn. 2 (Streitwert nach § 6 ZPO)
– BGH, Urt. v. 11.1.2007 – IX ZR 181/05, Rn. 2 (Vollstreckungsmaßnahme für unzulässig erklärt)
– Zur Beweislast und § 1006 BGB im Drittwiderspruchsprozess: BGH, Urt. v. 16.10.2003 – IX ZR 55/02 (Gründe II 3); zum Rechtsschutzbedürfnis: BGH, VU v. 27.11.2003 – IX ZR 310/00 (Gründe II 1, 2) – beide Volltexte ohne Randnummern

Mehr zur Abgrenzung der Rechtsbehelfe (§§ 766, 767, 771, 805 ZPO) im Video „Rechtsbehelfe in der Zwangsvollstreckung“.

Kapitel:
{kapitel}

Das Prüfungsschema und die Tenorformel sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Drittwiderspruchsklage #Zwangsvollstreckung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nWendland:", "\nFrau Wendland:"), ("\nVollmer:", "\nHerr Vollmer:"),
                 ("\nGerichtsvollzieherin:", "\nDie Gerichtsvollzieherin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("tausendachthundert Euro", "1.800 Euro").replace("drei Wochen", "3 Wochen")
assert not re.search(r"§\n", srt)
assert "tausend" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("§ 1006 BGB", "Eigentumsvermutung", "§ 769 ZPO"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
