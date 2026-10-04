"""Nachbearbeitung der Upload-Texte für Folge 187 (nach meta_158.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Beträge).
Aufruf: python3 meta_187.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Bagger trifft Stromkabel, Sachverhalt"),
       (T("norm"), "§ 823 Abs. 1 BGB im Wortlaut"),
       (T("liste"), "Warum das Vermögen fehlt"),
       (T("eig"), "I. Eigentum: Kabel und Maschinen"),
       (T("gegen"), "Gegenfall: Substanzschaden"),
       (T("gew"), "II. Recht am Gewerbebetrieb"),
       (T("subs"), "Betriebsbezogenheit im Stromkabel-Fall"),
       (T("abs2"), "§ 823 Abs. 2 BGB und Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Reiner Vermögensschaden: Warum ersetzt § 823 I BGB ihn nicht und wann ist der Gewerbebetrieb betriebsbezogen verletzt? Der Stromkabel-Fall (BGHZ 29, 65).

Der Fall: Fiete hebt mit seinem Bagger am Rand eines Gewerbegebiets einen Graben aus und reißt ein Stromkabel des Netzbetreibers auf. Zwei Kilometer weiter steht die Fahrradfabrik von Gotthard einen ganzen Tag still; kaputt geht nichts. Gotthard verlangt 48.000 € für den Produktionsausfall. Muss Fiete zahlen?

Inhalt:
– § 823 Abs. 1 BGB im Wortlaut: geschützte Rechtsgüter, das Vermögen als solches fehlt
– Grund: keine allgemeine deliktische Haftung für Vermögensschäden; Ausnahme § 826 BGB
– I. Eigentum: Kabel des Netzbetreibers, Maschinen unversehrt, bloße Unterbrechung der Fertigung, Nutzungsbeeinträchtigung nur bei Einwirkung auf die Sache
– Gegenfall: Stromausfall beschädigt Sachen (Asphaltmischwerk), Folgeschäden ersatzfähig
– II. Recht am eingerichteten und ausgeübten Gewerbebetrieb: sonstiges Recht, Auffangtatbestand, betriebsbezogener Eingriff
– § 823 Abs. 2 BGB (Verweis auf das Video zum Schutzgesetz), Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: § 823 Abs. 1, 2 BGB; § 826 BGB

Rechtsprechung:
– BGH, Urt. v. 9.12.1958 – VI ZR 199/57, BGHZ 29, 65 (Stromkabel-Fall)
– BGH, Urt. v. 9.12.2014 – VI ZR 155/14, Rn. 15, 18, 20 (reiner Vermögensschaden; Einwirkung auf die Sache; Betriebsbezogenheit)
– BGH, Urt. v. 13.4.2023 – III ZR 215/21, Rn. 7, 41, 44 (Stromausfall beschädigt Anlagensteuerung; bloße Unterbrechung der Fertigung)
– BGH, Urt. v. 8.5.2018 – VI ZR 295/17, Rn. 10 (Netzbetreiber: Eigentum am Stromkabel)
– BGH, Urt. v. 13.12.2011 – XI ZR 51/10, Rn. 26 (keine allgemeine deliktische Haftung für Vermögensschäden)
– BGH, Urt. v. 6.2.2014 – I ZR 75/13, Rn. 12; Urt. v. 3.6.2020 – XIII ZR 22/19, Rn. 22 (Gewerbebetrieb als sonstiges Recht und Auffangtatbestand)

Hinweise: Der Fall im Video ist dem Stromkabel-Fall nachgebildet. Ansprüche der Fabrik gegen den Netzbetreiber werden nicht behandelt. Das allgemeine Schema zu § 823 Abs. 1 BGB zeigt das Video zum Deliktsrecht, § 823 Abs. 2 BGB das Video zum Schutzgesetz.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ReinerVermögensschaden #Deliktsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for a, b in [("achtundvierzigtausend Euro", "48.000 Euro")]:
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
