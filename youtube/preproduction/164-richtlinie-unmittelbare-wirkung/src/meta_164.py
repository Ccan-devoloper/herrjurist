"""Nachbearbeitung der Upload-Texte für Folge 164 (nach meta_161.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall (als Annahme), Inhalt,
Normen, Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen).
Aufruf: python3 meta_164.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Feuerwehrmann und die 48-Stunden-Woche"),
       (T("norm"), "Normen: Art. 288 Abs. 3 AEUV, Art. 4 Abs. 3 EUV"),
       (T("s1"), "1. Umsetzungsfrist abgelaufen: Ratti"),
       (T("s2"), "2. Nicht oder nicht ordnungsgemäß umgesetzt"),
       (T("s3"), "3. Unbedingt und hinreichend genau: Art. 6 Buchst. b"),
       (T("s4"), "4. Gegenüber dem Staat"),
       (T("staat"), "Funktionaler Staatsbegriff: Foster und Farrell"),
       (T("priv"), "Private und richtlinienkonforme Auslegung"),
       (T("loes1"), "Lösung und Rechtsfolge"),
       (T("fuss"), "Der echte Fall Fuß"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Richtlinie unmittelbare Wirkung (Art. 288 III AEUV): Wann kannst du dich gegenüber dem Staat auf eine nicht umgesetzte Richtlinie berufen? Ratti und Foster – Schritt für Schritt am Fall eines Feuerwehrmanns.

Der Fall: Herr Ruppert ist Feuerwehrmann bei der Berufsfeuerwehr seiner Stadt. Eine Landesverordnung erlaubt im Schnitt 54 Wochenstunden; die Arbeitszeitrichtlinie 2003/88/EG verlangt im Schnitt höchstens 48. Angenommen, Deutschland hätte die Richtlinie nicht rechtzeitig umgesetzt (in Wirklichkeit ist sie umgesetzt): Kann sich Herr Ruppert gegenüber der Stadt direkt auf die Richtlinie berufen?

Inhalt:
– Normen: Art. 288 Abs. 3 AEUV und Art. 4 Abs. 3 UAbs. 2 EUV (im Wortlaut) – Pflicht zur Umsetzung
– 1. Umsetzungsfrist abgelaufen: der Fall Ratti (Lösemittel und Lacke)
– 2. Nicht oder nicht ordnungsgemäß umgesetzt
– 3. Inhaltlich unbedingt und hinreichend genau: Art. 6 Buchst. b RL 2003/88/EG (im Wortlaut)
– 4. Gegenüber dem Staat, auch als Arbeitgeber; funktionaler Staatsbegriff nach Foster (Zitat Rn. 20) und Farrell
– Keine Wirkung zwischen Privaten, richtlinienkonforme Auslegung
– Lösung: unmittelbare Berufung, entgegenstehendes Recht bleibt unangewendet (Anwendungsvorrang); der echte Fall Fuß
– Klausurtipp, Klausurschema, Merksatz

Normen: Art. 288 Abs. 3 AEUV; Art. 4 Abs. 3 EUV; Art. 6 Buchst. b, Art. 22 RL 2003/88/EG

Rechtsprechung:
– EuGH, Urt. v. 5.4.1979 – Rs. 148/78 (Ratti), Rn. 22–24, 43; Tenor 1, 5
– EuGH, Urt. v. 26.2.1986 – Rs. 152/84 (Marshall), Rn. 46, 49
– EuGH, Urt. v. 12.7.1990 – Rs. C-188/89 (Foster), Rn. 17–20
– EuGH, Urt. v. 14.10.2010 – Rs. C-243/09 (Fuß), Rn. 56–61, 63
– EuGH, Urt. v. 25.11.2010 – Rs. C-429/09 (Fuß II), Rn. 38–40
– EuGH (Große Kammer), Urt. v. 10.10.2017 – Rs. C-413/15 (Farrell), Rn. 26, 28 f.
– EuGH, Urt. v. 14.7.1994 – Rs. C-91/92 (Faccini Dori), Rn. 20, 25 f.

Hinweise: Der Fall beruht auf einer Annahme – Deutschland hat die Arbeitszeitrichtlinie umgesetzt (u. a. im Arbeitszeitgesetz). „Vertikale“ unmittelbare Wirkung und „funktionaler Staatsbegriff“ sind Lehrbegriffe. Nicht behandelt: Opt-out nach Art. 22 im Einzelnen, Bereitschaftsdienst, Staatshaftung (Francovich), Wirkungen vor Fristablauf und Sonderfälle der Wirkung unter Privaten über die Grundrechtecharta. Die Rechtsakte im Überblick, Faccini Dori und die Staatshaftung zeigt die Folge „Verordnung, Richtlinie, Beschluss: EU-Rechtsakte erklärt“, den Anwendungsvorrang die Folge zu Costa/ENEL.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Europarecht #Richtlinie #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Art\. \d+)\n(Buchstabe b) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
srt = srt.replace("Buchstabe b", "Buchst. b")
for a, b in [("vierundfünfzig", "54"), ("achtundvierzig", "48"), ("fünfundsechzig", "65"), ("sechzig", "60")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt and "zig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ["Arbeitszeitrichtlinie", "Fuß", "Farrell", "Art. 4 III EUV", "Staatsbegriff", "Examenswissen Europarecht"]:
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
