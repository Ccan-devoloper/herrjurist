"""Nachbearbeitung der Upload-Texte für Folge 094 (nach tools/youtube_metadaten.py, nichts dort geändert):
Hilfsangebot ganz oben in der Beschreibung (TelefonSeelsorge, Nummern verifiziert auf telefonseelsorge.de am 03.10.2026),
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Fall ohne Methode, Inhalt, Rechtsprechung, Lizenzzeile, zusätzliche Tags;
Untertitel: Datum und Paragrafen in Ziffern.
Aufruf: python3 meta_094.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Wilma und Hartwig"), (T("abend"), "Der verabredete Abend – und die Frage"),
       (T("sv"), "Sachverhalt zum Nachlesen"), (T("echt"), "Der echte Fall: BGHSt 32, 38"),
       (T("aus"), "Ausgangspunkt: Selbsttötung und Teilnahme straflos"), (T("hand"), "§ 25 Abs. 1 StGB: Werkzeug gegen sich selbst"),
       (T("streit"), "Streit: Exkulpations- oder Einwilligungslösung"), (T("art"), "Täuschung über den Tod: Täter kraft überlegenen Wissens"),
       (T("subs"), "Subsumtion"), (T("versuch"), "Versuch"), (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz"), (T("hilfe"), "Hilfsangebot")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Wenn dich das Thema selbst betrifft: Die TelefonSeelsorge ist rund um die Uhr und kostenlos erreichbar, unter 0800 111 0 111, 0800 111 0 222 oder 116 123 (telefonseelsorge.de).

Sirius-Fall (BGHSt 32, 38): Straflose Beteiligung an Selbsttötung oder Tötung in mittelbarer Täterschaft nach §§ 25 I Alt. 2, 212 StGB kraft Wissensherrschaft? Der Klassiker zum „Werkzeug gegen sich selbst“ – Schritt für Schritt wie in der Klausur.

Der Fall (frei nach dem Sirius-Fall, abgewandelt): Wilma vertraut seit Jahren Hartwig, der sich spiritueller Lehrer nennt. Er redet ihr ein, sie werde nicht sterben, sondern sofort in einem höheren Körper weiterleben. Sterben will Wilma nicht. Hartwig weiß, dass sie sterben würde – und will genau das. Ihr Bruder hält sie auf; sie bleibt unverletzt. Ist Hartwig nur straflos an einer Selbsttötung beteiligt oder Täter durch das Opfer selbst?

Inhalt:
– Der echte Fall: BGH, Urteil vom 5.7.1983, BGHSt 32, 38
– Ausgangspunkt: Selbsttötung straflos, Teilnahme mangels Haupttat ebenfalls; § 217 StGB a. F. nichtig (BVerfG, 26.2.2020)
– § 25 Abs. 1 StGB im Wortlaut: das Opfer als Werkzeug gegen sich selbst
– Wann ist der Entschluss unfrei? Exkulpationslösung, Einwilligungslösung, Kriterien des BGH
– Täuschung über den Tod: Täter kraft überlegenen Wissens (vgl. Folge 091, Katzenkönig)
– Subsumtion, Versuch, Ergebnis: versuchter Totschlag in mittelbarer Täterschaft
– Klausurtipp, Klausurschema, Merksatz
– Verweis: Folge 058 (eigenverantwortliche Selbstgefährdung)

Normen: §§ 22, 23 Abs. 1, 24, 25 Abs. 1 Alt. 2, 26, 27, 211, 212 StGB; § 217 StGB a. F.

Rechtsprechung:
– BGH, Urt. v. 5.7.1983 – 1 StR 168/83, BGHSt 32, 38 (Sirius-Fall): Abgrenzung nach Art und Tragweite des Irrtums; Täuschung über die Tatsache des eigenen Todes begründet Täterschaft kraft überlegenen Wissens; versuchter Mord aus Habgier bestätigt
– BGH, Urt. v. 3.7.2019 – 5 StR 132/18, BGHSt 64, 121, Rn. 17 (Selbsttötung kein Tötungsdelikt, Beihilfe mangels Haupttat straflos), Rn. 20 f. (unfreies Handeln, Wissens- oder Verantwortlichkeitsdefizit, Täuschung; mit BGHSt 32, 38, 41 f., 43), Rn. 25 (Exkulpations- und Einwilligungslösung)
– BVerfG, Urt. v. 26.2.2020 – 2 BvR 2347/15 u. a., Rn. 337 (§ 217 StGB nichtig)

Kapitel:
{kapitel}

Der Fall ist abgewandelt, die Personen sind erfunden. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#SiriusFall #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"fünften\s+Juli\s+neunzehnhundertdreiundachtzig", "5. Juli 1983", srt)
srt = srt.replace("§ 25 Abs. 1, Alt. 2", "§ 25 Abs. 1 Alt. 2")
assert "neunzehnhundert" not in srt
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["titel_plan"] = m.get("titel")
m["titel_vorschlag"] = "Sirius-Fall: In den Tod getäuscht – mittelbare Täterschaft?"
m["thumbnail_text"] = "TÖTEN DURCH TÄUSCHUNG?"
for t in ("Sirius-Fall", "Werkzeug gegen sich selbst", "Tatherrschaft kraft überlegenen Wissens", "Exkulpationslösung",
          "Einwilligungslösung"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
