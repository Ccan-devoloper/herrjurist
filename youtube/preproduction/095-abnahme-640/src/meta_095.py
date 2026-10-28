"""Nachbearbeitung der Upload-Texte für Folge 095 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen zu Sätzen ohne
Aktenzeichen und Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_095.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das neue Bad und die Fuge hinter der Tür"),
       (T("begr"), "Was ist Abnahme?"), (T("p640"), "§ 640 Abs. 1 BGB: Pflicht zur Abnahme"),
       (T("fikt"), "Fiktive Abnahme, § 640 Abs. 2 BGB"), (T("verb"), "Verbraucher: Hinweis in Textform"),
       (T("mang"), "Mangel genannt, endgültige Verweigerung"), (T("vorb"), "Vorbehalt, § 640 Abs. 3 BGB"),
       (T("wirk"), "Wirkungen: Fälligkeit und Gefahr"), (T("w3"), "Wirkungen: Verjährung, Beweislast, Mängelrechte"),
       (T("erg"), "Ergebnis: Abnahme unter Vorbehalt, § 641 Abs. 3 BGB"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema Werklohn"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Abnahme Werkvertrag (§§ 640, 641, 644 BGB): Fälligkeit, Gefahr, Beweislast, Verjährung – und wann die Abnahme nach § 640 II BGB fingiert wird. Am Fall des Fliesenlegers, der fertig ist und sein Geld will.

Der Fall: Susanne lässt ihr Bad vom Fliesenleger Herrn Fiedler sanieren, Rechnung 3.800 Euro. Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig – ein Schönheitsfehler, Nachbessern kostet 150 Euro. Herr Fiedler setzt per E-Mail 2 Wochen Frist zur Abnahme und weist auf die Folgen hin. Muss Susanne abnehmen und zahlen? Und was gilt, wenn sie schweigt?

Inhalt:
– Begriff: körperliche Entgegennahme und Billigung als im Wesentlichen vertragsgemäß; ausdrücklich oder stillschweigend
– § 640 Abs. 1 BGB im Wortlaut: Abnahmepflicht, Verweigerung nur wegen wesentlicher Mängel
– Fiktive Abnahme, § 640 Abs. 2 BGB im Wortlaut: Fertigstellung, angemessene Frist, keine Verweigerung unter Angabe mindestens eines Mangels; bei Verbrauchern Hinweis in Textform (§ 640 Abs. 2 S. 2 BGB)
– Ein Mangel genügt, um die Fiktion zu verhindern; endgültige unberechtigte Verweigerung macht den Werklohn trotzdem fällig
– Vorbehalt bekannter Mängel, § 640 Abs. 3 BGB
– Wirkungen: Fälligkeit (§ 641 Abs. 1 BGB; beim Bauvertrag § 650g Abs. 4 BGB), Gefahrübergang (§ 644 BGB), Verjährungsbeginn (§ 634a Abs. 2 BGB), Beweislastumkehr, Übergang ins Mängelstadium (§ 634 BGB)
– Ergebnis: Abnahme unter Vorbehalt, Leistungsverweigerungsrecht in Höhe des Doppelten der Mängelbeseitigungskosten (§ 641 Abs. 3 BGB)
– Klausurtipp, Klausurschema Werklohn, Merksatz

Normen: §§ 640, 641, 644, 634, 634a BGB; §§ 13, 126b, 631, 635, 650g BGB

Rechtsprechung und Materialien:
– BGH, Urt. v. 5.6.2014 – VII ZR 276/13, Rn. 21 (Begriff der Abnahme)
– BGH, Urt. v. 25.2.2010 – VII ZR 64/09, Rn. 21 f. (konkludente Abnahme, Prüfungsfrist)
– BGH, Beschl. v. 18.5.2010 – VII ZR 158/09, Rn. 5 (Werklohn fällig bei unberechtigter endgültiger Abnahmeverweigerung)
– BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Leitsatz 1, Rn. 35, 36 (Abnahme als Zäsur; Beweislastumkehr, soweit kein Vorbehalt)
– BGH, Urt. v. 11.3.2026 – I ZR 202/25, Rn. 20 (E-Mail wahrt grundsätzlich die Textform)
– BT-Drs. 18/8486, S. 48 f.; BT-Drs. 18/11437, S. 40 (fiktive Abnahme seit 1.1.2018: ein Mangel genügt)

Hinweise: Ob die Badsanierung ein Bauvertrag (§ 650a BGB) oder eine Arbeit an einem Bauwerk (§ 634a Abs. 1 Nr. 2 BGB) ist, hängt vom Umfang ab; das Video lässt es offen. Die Klausurreihenfolge im Klausurtipp und im Schema ist Klausurkonvention.

Mehr dazu: Folge 56 (Werkvertrag oder Dienstvertrag?), Folge 63 (Käuferrechte, § 437 BGB).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#640BGB #Werkvertrag #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
