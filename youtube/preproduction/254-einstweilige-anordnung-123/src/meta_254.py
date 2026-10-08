"""Nachbearbeitung der Upload-Texte für Folge 254 (nach meta_233.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, „80a“, „Satz“ statt „S.“).
Aufruf: python3 meta_254.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kein Standplatz beim Stadtfest"),
       (T("frage"), "Die Frage"),
       (T("zul"), "Zulässigkeit: Rechtsweg und § 123 Abs. 5 VwGO"),
       (T("wl1"), "Sicherungs- oder Regelungsanordnung"),
       (T("befugt"), "Antragsbefugnis und Rechtsschutzbedürfnis"),
       (T("begr"), "Begründetheit: Glaubhaftmachung"),
       (T("aa"), "Anordnungsanspruch: § 70 GewO"),
       (T("ag"), "Anordnungsgrund und Vorwegnahme der Hauptsache"),
       (T("ausn"), "Ausnahme: unzumutbare Nachteile"),
       (T("erg"), "Der Beschluss"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 123 VwGO Schema: einstweilige Anordnung, Abgrenzung zu § 80 V, Anordnungsanspruch und -grund, Glaubhaftmachung und Vorwegnahme der Hauptsache.

Der Fall: Das Stadtfest ist in zehn Tagen. Magda verkauft dort seit Jahren Waffeln – doch die Stadt verweigert ihr den Standplatz, weil sie die Stadt in einem Leserbrief kritisiert hat. Plätze sind noch frei, eine Klage würde Monate dauern. Wie kommt Magda schnell zu ihrem Stand?

Inhalt:
– Statthaftigkeit: § 123 Abs. 5 VwGO im Wortlaut, Vorrang von §§ 80, 80a VwGO; Hauptsache Verpflichtungsklage
– Sicherungsanordnung (§ 123 Abs. 1 Satz 1) und Regelungsanordnung (Satz 2) im Wortlaut
– Antragsbefugnis analog § 42 Abs. 2 VwGO, Rechtsschutzbedürfnis (vorheriger Antrag bei der Behörde)
– Begründetheit: Anordnungsanspruch und Anordnungsgrund, Glaubhaftmachung nach § 123 Abs. 3 VwGO i. V. m. §§ 920 Abs. 2, 294 ZPO
– Zulassungsanspruch zum festgesetzten Volksfest, § 70 Abs. 1 und 3 GewO
– Verbot der Vorwegnahme der Hauptsache und Ausnahme (Art. 19 Abs. 4 GG)
– Klausurtipp, Klausurschema, Merksatz

Normen: § 123 VwGO; §§ 920, 294 ZPO; §§ 40, 42 Abs. 2 VwGO; §§ 60b, 69, 70 GewO; Art. 5 Abs. 1, Art. 19 Abs. 4 GG.

Rechtsprechung:
– BVerwG, Beschl. v. 26.11.2013 – 6 VR 3.13, Rn. 5, 7 (Vorwegnahme der Hauptsache nur ausnahmsweise; strenger Maßstab)
– BVerfG, Beschl. v. 12.5.2005 – 1 BvR 569/05, Rn. 23–25 (effektiver Eilrechtsschutz, Art. 19 Abs. 4 GG)
– BVerwG, Beschl. v. 22.11.2021 – 6 VR 4.21, Rn. 7 f., 10 (Rechtsschutzbedürfnis: Vorbefassung der Behörde)
– OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 7, 29, 32 (Anordnungsanspruch; Vorwegnahme vor einem Veranstaltungstermin)
– OVG NRW, Beschl. v. 26.7.2018 – 4 B 1069/18, Rn. 4, 7 (Kirmes, § 70 Abs. 3 GewO: Zulassung nur bei Spielraum null, sonst Neubescheidung)
– VG Gelsenkirchen, Beschl. v. 9.4.2026 – 18 L 76/26, Rn. 7, 14 f. (Kirmes: Regelungsanordnung)

Hinweise: Magda und Herr Eckstein sind erfundene Figuren. Mehr dazu: Folge 082 (§ 80 V VwGO), Folge 093 (Verpflichtungsklage).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#123VwGO #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("§§ 80\nund achtzig a.", "§§ 80\nund 80a.").replace("achtzig a", "80a")
srt = srt.replace("Absätze eins bis\ndrei", "Absätze 1 bis\n3")
srt = re.sub(r"\bS\. (\d)", r"Satz \1", srt)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf|achtzig", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["123 VwGO Schema", "Vorwegnahme der Hauptsache Ausnahme", "Zulassung Volksfest 70 GewO"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
