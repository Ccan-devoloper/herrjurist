"""Nachbearbeitung der Upload-Texte für Folge 214 (nach meta_211.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_214.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Äpfel für 20 € auf der Obstwiese"),
       (T("flucht"), "Warnschuss und Schuss auf die Beine"),
       (T("polizei"), "Die Frage und der Sachverhalt"),
       (T("tb"), "Tatbestand: §§ 223, 224 StGB"),
       (T("p32"), "§ 32 StGB im Wortlaut"),
       (T("lage"), "Notwehrlage: Diebstahl als Angriff"),
       (T("erf"), "Erforderlichkeit: mildestes Mittel"),
       (T("geb"), "Gebotenheit: unerträgliches Missverhältnis"),
       (T("hier"), "Im Fall: Äpfel gegen Schrot"),
       (T("kind"), "Keine Kinder; Streitpunkt Art. 2 EMRK"),
       (T("erg"), "Ergebnis und § 33 StGB"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Notwehr bei Bagatellen: Wann ist Verteidigung nach § 32 StGB wegen krassen Missverhältnisses nicht mehr geboten – etwa beim Schuss wegen ein paar Äpfeln?

Der Fall: Samstagnacht pflücken Jannes und Paulina, beide 16, auf der Obstwiese von Herrn Gehrke Äpfel im Wert von etwa 20 €. Herr Gehrke droht, gibt einen Warnschuss ab und schießt den Fliehenden mit Schrot auf die Beine; Jannes wird getroffen. War das Notwehr?

Inhalt:
– Tatbestand kurz: § 223 StGB und § 224 Abs. 1 Nr. 2 StGB (Waffe)
– § 32 StGB im Wortlaut
– Notwehrlage: Diebstahl als gegenwärtiger rechtswidriger Angriff auf das Eigentum, solange der Täter die Beute hat
– Erforderlichkeit: mildestes gleich wirksames Mittel; lebensgefährliche Waffe erst androhen, auf die Beine zielen
– Gebotenheit: keine Güterabwägung, aber sozialethische Einschränkung bei unerträglichem Missverhältnis
– Im Fall: Äpfel für 20 € gegen Schrot auf Menschen – nicht geboten
– Keine Kinder; Streitpunkt Art. 2 Abs. 2 lit. a EMRK bei tödlicher Abwehr (im Wortlaut)
– § 33 StGB (im Wortlaut): Ärger ist kein asthenischer Affekt
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 32, 33, 223, 224 Abs. 1 Nr. 2, 242 StGB; Art. 2 Abs. 2 lit. a EMRK.

Rechtsprechung:
– BGH, Beschl. v. 1.3.2011 – 3 StR 450/10, Rn. 16 (unerträgliches Missverhältnis, evident bagatellhafter Angriff)
– BGH, Urt. v. 12.4.2016 – 2 StR 523/15, Rn. 11, 21 (Androhung der Waffe; keine Güterproportionalität)
– BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 9, 14, 18 (Notwehrlage bei Flucht mit der Beute; Erforderlichkeit; Gebotenheit)
– BGH, Urt. v. 27.10.2015 – 3 StR 199/15, Rn. 9, 11, 18 (auf die Beine zielen; grobes Missverhältnis; § 33 StGB)

Hinweise: Herr Gehrke, Jannes und Paulina sind erfundene Figuren. Art. 2 EMRK zitiert nach der deutschen Fassung des Europarats; der Streit um die Bindung Privater ist eine Frage der Lehre. Mehr dazu: Folge 033 (Notwehr-Schema), Folge 042 (gefährliche Körperverletzung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Notwehr #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Gehrke: Halt!", "Herr Gehrke: Halt!"), ("Gehrke: Das waren", "Herr Gehrke: Das waren"),
             ("achtundsechzig", "68"), ("beide sechzehn", "beide 16"), ("Mit sechzehn", "Mit 16")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt, n = re.subn(r"zwanzig(\s+)Euro", r"20\1Euro", srt)
assert n == 3, n
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n|achtundsechzig|sechzehn|zwanzig", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Notwehrexzess § 33", "Schrotflinte Notwehr"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
