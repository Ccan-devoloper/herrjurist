"""Nachbearbeitung der Upload-Texte für Folge 176 (nach meta_164.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung).
Aufruf: python3 meta_176.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Whisky ohne Echtheitszeugnis"),
       (T("norm"), "Art. 34 AEUV und das Prüfschema"),
       (T("s1"), "1. Schutzbereich: Ware, grenzüberschreitender Bezug"),
       (T("s2"), "2. Adressat: staatliche Maßnahme"),
       (T("s3"), "3. Beschränkung: der Fall Dassonville"),
       (T("formel"), "Die Dassonville-Formel"),
       (T("keck"), "Grenze: Keck"),
       (T("s4"), "4. Rechtfertigung: Art. 36 AEUV"),
       (T("cassis"), "Cassis de Dijon und Verhältnismäßigkeit"),
       (T("dfal"), "Dassonville: Nachweis für alle"),
       (T("loes"), "Lösung"),
       (T("tipp"), "Klausurtipp: Art. 30 AEUV und Keck"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Warenverkehrsfreiheit Schema (Art. 34, 36 AEUV): Schutzbereich, Maßnahme gleicher Wirkung nach Dassonville und Rechtfertigung – klausurfertig erklärt.

Der Fall: Frau Trautmann betreibt einen Getränkegroßhandel und kauft Whisky als Parallelimporteurin bei einem Großhändler im Nachbarland. Eine Verordnung ihres Landes verlangt für importierten Whisky ein Echtheitszeugnis der Behörden des Herstellerlandes – das bekommt praktisch nur, wer direkt beim Hersteller kauft. Verstößt die Pflicht gegen die Warenverkehrsfreiheit?

Inhalt:
– Art. 34 AEUV im Wortlaut und das Prüfschema in vier Schritten
– 1. Schutzbereich: Ware (EuGH, Kommission/Italien 1968) und grenzüberschreitender Bezug
– 2. Adressat: Mitgliedstaat, staatliche Maßnahme
– 3. Beschränkung: mengenmäßige Beschränkung oder Maßnahme gleicher Wirkung – der echte Fall Dassonville und die Dassonville-Formel (Rn. 5); Grenze Keck für Verkaufsmodalitäten
– 4. Rechtfertigung: Art. 36 AEUV im Wortlaut, zwingende Erfordernisse (Cassis de Dijon), Verhältnismäßigkeit; Dassonville Rn. 6 und 7/9: Nachweis für alle, nicht nur für Direktimporteure
– Lösung: Maßnahme gleicher Wirkung, unverhältnismäßig, unmittelbare Wirkung von Art. 34 AEUV, Anwendungsvorrang
– Klausurtipp (Abgrenzung zu Art. 30 AEUV, Keck), Klausurschema, Merksatz

Normen: Art. 28, 30, 34, 36 AEUV

Rechtsprechung:
– EuGH, Urt. v. 11.7.1974 – Rs. 8/74 (Dassonville), Slg. 1974, 837, Rn. 2/4, 5, 6, 7/9
– EuGH, Urt. v. 10.12.1968 – Rs. 7/68 (Kommission/Italien), Slg. 1968, 634
– EuGH, Urt. v. 12.7.1973 – Rs. 2/73 (Geddo), Slg. 1973, 865, Rn. 7
– EuGH, Urt. v. 22.3.1977 – Rs. 74/76 (Iannelli & Volpi), Slg. 1977, 557, Rn. 13
– EuGH, Urt. v. 20.2.1979 – Rs. 120/78 (Rewe-Zentral, „Cassis de Dijon“), Slg. 1979, 649, Rn. 8
– EuGH, Urt. v. 24.11.1993 – verb. Rs. C-267/91 und C-268/91 (Keck und Mithouard), Slg. 1993, I-6097, Rn. 16 f.
– EuGH (Große Kammer), Urt. v. 10.2.2009 – C-110/05 (Kommission/Italien, Anhänger), Rn. 59

Hinweise: Der Fall ist ein Übungsfall nach dem Vorbild Dassonville; die Staaten sind bewusst nicht benannt, das Herstellerland ist ein EU-Staat. Die Gliederung in vier Schritte ist eine Klausurkonvention. Nicht behandelt: Waren aus Drittstaaten im freien Verkehr (Art. 28 Abs. 2 AEUV), Marktzugangs-Rechtsprechung nach Keck, Art. 35 AEUV (Ausfuhr), Bindung Privater, heutiges Unionsrecht zu Ursprungsbezeichnungen. Den Anwendungsvorrang erklärt die Folge zu Costa/ENEL.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Europarecht #Warenverkehrsfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt and "zig" not in srt and "dreißig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ["Keck", "Cassis de Dijon", "Parallelimport", "Prüfungsschema Warenverkehrsfreiheit", "Examenswissen Europarecht"]:
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
