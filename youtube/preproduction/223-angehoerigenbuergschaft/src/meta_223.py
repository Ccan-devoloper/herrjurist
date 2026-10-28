"""Nachbearbeitung der Upload-Texte für Folge 223 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn./Seiten, Lizenzzeile;
Sprechernamen und Ziffern in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_223.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Anneke bürgt für den Firmenkredit ihres Mannes"), (T("frage"), "Frage und Sachverhalt"),
       (T("agl"), "Anspruch aus § 765 Abs. 1 BGB, Form nach § 766 BGB"),
       (T("bverfg"), "Bürgschaftsbeschluss: BVerfGE 89, 214 und Art. 2 Abs. 1 GG"),
       (T("korr"), "Pflicht der Zivilgerichte: §§ 138, 242 BGB"),
       (T("w138"), "§ 138 BGB: krasse finanzielle Überforderung und Nähe"),
       (T("verm"), "Vermutung und Widerlegung durch die Bank"),
       (T("sub"), "Subsumtion und Ergebnis: Bürgschaft nichtig"),
       (T("gegen"), "Gegenfall: eigenes Interesse am Kredit"),
       (T("tipp"), "Klausurtipp: Prognose bei Abgabe der Erklärung"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Angehörigenbürgschaft: Wann ist die Bürgschaft der einkommenslosen Ehefrau wegen krasser finanzieller Überforderung nach §§ 138 I, 765 BGB nichtig? BVerfGE 89, 214 – der Bürgschaftsbeschluss – und die Kriterien des BGH an einem Fall.

Der Fall: Tischlermeister Gero braucht für neue Maschinen einen Firmenkredit über 200.000 Euro, die Zinsen betragen 1.000 Euro im Monat. Die Bank verlangt, dass seine Frau Anneke bürgt. Anneke hat kein eigenes Einkommen und kein Vermögen – und unterschreibt. Drei Jahre später bleiben die Aufträge aus, 180.000 Euro sind offen, und die Bank verlangt das Geld von Anneke. Muss sie zahlen?

Inhalt:
– Anspruch aus § 765 Abs. 1 BGB (Wortlaut), Einigung und Form nach § 766 Satz 1 BGB
– Der Bürgschaftsbeschluss (BVerfGE 89, 214): Privatautonomie aus Art. 2 Abs. 1 GG (Wortlaut), Fremdbestimmung bei strukturell ungleicher Verhandlungsstärke, Inhaltskontrolle über die Generalklauseln §§ 138, 242 BGB
– § 138 Abs. 1 BGB (Wortlaut) und die Kriterien des BGH: krasse finanzielle Überforderung, persönliche Nähe, Vermutung der Ausnutzung und ihre Widerlegung durch die Bank
– Subsumtion: kein Einkommen, kein Vermögen, nur mittelbarer Vorteil – Bürgschaft nichtig
– Gegenfall: eigenes Interesse am Kredit; die erfolglose Verfassungsbeschwerde der Ehefrau im Bürgschaftsbeschluss
– Klausurtipp: Prognose bei Abgabe der Bürgschaftserklärung
– Klausurschema und Merksatz

Normen: §§ 126, 138, 242, 765, 766 BGB; Art. 2 Abs. 1 GG

Rechtsprechung:
– BVerfG, Beschl. v. 19.10.1993 – 1 BvR 567/89, 1 BvR 1044/89, BVerfGE 89, 214 (231 f., 234, 235 f.) (Bürgschaftsbeschluss)
– BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9 (krasse finanzielle Überforderung, widerlegliche Vermutung)
– BGH, Urt. v. 15.11.2016 – XI ZR 32/16, Rn. 20, 29 f. (Ehegatten, Beweislast der Bank, eigenes Interesse und nur mittelbare Vorteile)

Kapitel:
{kapitel}

Im Bürgschaftsbeschluss hatte die Verfassungsbeschwerde einer Tochter Erfolg, die für Geschäftskredite ihres Vaters gebürgt hatte; die Verfassungsbeschwerde einer einkommenslosen Ehefrau (Konsumkredit des Ehemanns) wurde zurückgewiesen. Im Fall ist unterstellt, dass die Bank wirksam gekündigt hat und keine Umstände die Vermutung widerlegen. Das Prüfungsschema ist eine Klausurkonvention. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Bürgschaft #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nWittkamp:", "\nHerr Wittkamp:")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("zweihunderttausend Euro", "200.000 Euro"), ("hundertachtzigtausend Euro", "180.000 Euro"),
                 ("hunderttausend Mark", "100.000 Mark"), ("tausend Euro", "1.000 Euro")):
    w, e = alt.split(" ")
    srt = re.sub(r"\b" + w + r"(\s+)" + e, lambda mm: neu.split(" ")[0] + mm.group(1) + e, srt)
srt = srt.replace("einundzwanzigjährige", "21-jährige").replace("seit acht Jahren", "seit 8 Jahren")
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III.")):
    srt = re.sub(r"Römisch(\s)" + alt, r"\g<1>" + neu, srt)
srt = re.sub(r"(^|\n) (I|II|III)\.", r"\1\2.", srt)
srt = re.sub(r"\b(I|II|III)\.:", r"\1.", srt).replace(".  ", ". ").replace(":  ", ": ")
assert "Römisch" not in srt, re.findall(r".{20}Römisch.{20}", srt)
assert not re.search(r"§\n", srt)
assert "tausend" not in srt, re.findall(r".{20}tausend.{20}", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Angehörigenbürgschaft", "Bürgschaftsbeschluss", "Ehegattenbürgschaft", "§ 138 BGB"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
