"""Nachbearbeitung der Upload-Texte für Folge 231 (nach meta_227.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lehrmaterial, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_231.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Pfefferspray im Stadtpark"),
       (T("frage"), "Die Frage"),
       (T("tb"), "Tatbestand: §§ 223, 224 StGB"),
       (T("rw"), "§ 32 StGB: keine Notwehrlage"),
       (T("irrtum"), "Erlaubnistatbestandsirrtum und Erlaubnisirrtum"),
       (T("gesetz"), "Zwischen § 16 und § 17 StGB"),
       (T("t1"), "1. Vorsatztheorie"),
       (T("t2"), "2. Strenge Schuldtheorie"),
       (T("t3"), "3. Negative Tatbestandsmerkmale"),
       (T("t4"), "4. Eingeschränkte Schuldtheorie"),
       (T("t5"), "5. Rechtsfolgenverweisende Schuldtheorie"),
       (T("bgh"), "Bundesgerichtshof"),
       (T("erg"), "Ergebnis: § 229 StGB?"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Erlaubnistatbestandsirrtum: Wie wirkt die irrige Annahme einer Notwehrlage (§ 32 StGB) – strenge, eingeschränkte oder rechtsfolgenverweisende Schuldtheorie (§§ 16, 17)?

Der Fall: Nachts im Stadtpark verliert Bärbel beim Joggen ihr Handy. Helge hebt es auf und läuft ihr hinterher. Unter einer Laterne glänzt etwas in seiner Hand – Bärbel hält es für ein Messer und sprüht Pfefferspray. Helge wollte ihr nur das Handy bringen.

Inhalt:
– Tatbestand kurz: § 223 StGB, § 224 Abs. 1 Nr. 2 StGB (Pfefferspray)
– § 32 Abs. 2 StGB im Wortlaut: kein Angriff, keine Notwehrlage
– Erlaubnistatbestandsirrtum (Putativnotwehr) und Abgrenzung zum Erlaubnisirrtum (§ 17)
– § 16 Abs. 1 Satz 1 und § 17 Satz 1 StGB im Wortlaut
– Alle Theorien mit Ergebnis im Fall und Kritik: Vorsatztheorie, strenge Schuldtheorie, Lehre von den negativen Tatbestandsmerkmalen, eingeschränkte Schuldtheorie (§ 16 analog), rechtsfolgenverweisende eingeschränkte Schuldtheorie
– Teilnahme-Argument: §§ 26, 27 StGB verlangen eine vorsätzlich begangene rechtswidrige Tat
– Bundesgerichtshof: § 16 entsprechend
– Ergebnis: fahrlässige Körperverletzung (§ 229 StGB) nur bei vermeidbarem Irrtum
– Klausurtipp (Prüfungsstandort Schuld), Klausurschema, Merksatz

Normen: §§ 16 Abs. 1, 17, 26, 27, 32, 223, 224 Abs. 1 Nr. 2, 229 StGB.

Rechtsprechung:
– BGH, Beschl. v. 25.5.2022 – 4 StR 36/22, Rn. 10–12 (Erlaubnistatbestandsirrtum analog § 16 Abs. 1 Satz 1, st. Rspr.)
– BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 32, 36 (Ausschluss der Vorsatzschuld; Fahrlässigkeit nur bei vermeidbarem Irrtum)
– BGH, Urt. v. 27.10.2015 – 3 StR 199/15, Rn. 12
– BGH, Beschl. v. 1.3.2011 – 3 StR 450/10, Rn. 12
– BGH, Urt. v. 10.2.2000 – 4 StR 558/99, BGHSt 45, 378, Rn. 13 f.
– BGH, Beschl. v. 18.3.1952 – GSSt 2/51, BGHSt 2, 194 (Schuldtheorie statt Vorsatztheorie)
– BGH, Urt. v. 20.9.2017 – 1 StR 112/17, Rn. 16 (Pfefferspray als gefährliches Werkzeug)

Lehrmaterial: Universität Freiburg, AG Strafrecht AT, Übersicht Erlaubnistatbestandsirrtum; TU Dresden, Strafrecht IV, Übersicht Schuld.

Hinweise: Bärbel und Helge sind erfundene Figuren. Mehr dazu: Folge 033 (Notwehr-Schema), Folge 068 (Tatbestandsirrtum § 16), Folge 214 (Notwehr bei Bagatellen), Folge 227 (Notwehrprovokation).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Erlaubnistatbestandsirrtum #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Lehre von den negativen Tatbestandsmerkmalen", "Vorsatztheorie", "Putativnotwehr Pfefferspray"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
