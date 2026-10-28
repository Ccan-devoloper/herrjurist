"""Nachbearbeitung der Upload-Texte für Folge 125 (Kopie von meta_122.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_125.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Gebrauchter Fernseher, „gekauft wie gesehen“"),
       (T("plan"), "Verbrauchsgüterkauf: von privat und vom Händler"),
       (T("a1"), "1. Anwendungsbereich, § 474 Abs. 1 BGB"),
       (T("b1"), "2. Abweichungsverbot, § 476 Abs. 1 S. 1 BGB"),
       (T("c1"), "3. Negative Beschaffenheitsvereinbarung, § 476 Abs. 1 S. 2 BGB"),
       (T("d1"), "4. Beweislastumkehr 1 Jahr, § 477 BGB"),
       (T("e1"), "5. Verjährung bei gebrauchten Waren, § 476 Abs. 2 BGB"),
       (T("f1"), "6. Abgrenzung: Versand, § 475 Abs. 2 BGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verbrauchsgüterkauf (§§ 474–479 BGB): Welche zwingenden Sonderregeln gelten beim Kauf vom Händler – Abweichungsverbot, negative Beschaffenheitsvereinbarung, Beweislastumkehr, Verjährung und Gefahrübergang beim Versand?

Der Fall: Dirk kauft im Laden von Frau Tillmann einen gebrauchten Fernseher für 250 Euro. Im vorgedruckten Kaufformular steht „Gekauft wie gesehen, keine Gewährleistung“. Vier Monate später fällt das Bild aus. Frau Tillmann: „Kaputtgegangen ist er erst bei Ihnen.“ Muss sie einstehen – und was wäre beim Kauf von privat anders?

Inhalt (immer im Vergleich „von privat“ / „vom Händler“):
– Anwendungsbereich: Verbraucher kauft von Unternehmer eine Ware (§ 474 Abs. 1 BGB, Wortlaut)
– Abweichungsverbot: Auf den Gewährleistungsausschluss kann sich der Händler nicht berufen (§ 476 Abs. 1 S. 1 BGB, Wortlaut); Schadensersatz nur in den Grenzen der §§ 307–309 BGB (§ 476 Abs. 3); von privat Grenze § 444 BGB
– Negative Beschaffenheitsvereinbarung seit 2022: nur mit eigenem Hinweis und ausdrücklicher, gesonderter Vereinbarung (§ 476 Abs. 1 S. 2 BGB, Wortlaut); Formularklausel genügt nicht
– Beweislastumkehr: ein Jahr ab Gefahrübergang (§ 477 Abs. 1 BGB, Wortlaut), auch bei gebrauchter Ware
– Verjährung: bei gebrauchten Waren nicht unter ein Jahr und nur mit gesonderter Vereinbarung (§ 476 Abs. 2 BGB, Wortlaut)
– Abgrenzung Versand: § 475 Abs. 2 BGB statt § 447 BGB
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Rechtsprechung und Materialien:
– BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 25, 27: Für die Vermutung genügt eine Mangelerscheinung; der Käufer muss die Ursache nicht beweisen (zu § 477 BGB a. F., gebrauchter Motorroller vom Händler)
– BGH, Urt. v. 12.10.2016 – VIII ZR 103/15, Rn. 36, 59: Mangelerscheinung genügt; der Verkäufer muss das Gegenteil beweisen (zu § 476 BGB a. F.)
– BT-Drs. 19/27424, S. 42 (negative Beschaffenheitsvereinbarung nicht im Formularvertrag), S. 43 (Verjährung gebrauchter Sachen), S. 44 (Beweislastumkehr ein Jahr)

Hinweise: Der Fall ist erfunden. Eine BGH-Entscheidung zur negativen Beschaffenheitsvereinbarung nach § 476 Abs. 1 S. 2 BGB n. F. haben wir nicht gefunden; die Einordnung folgt Wortlaut und Gesetzesbegründung. Die BGH-Urteile betreffen die Beweislastumkehr in der alten Fassung (sechs Monate); die neue Fassung übernimmt diese Rechtsprechung (BT-Drs. 19/27424, S. 44). Die Käuferrechte aus § 437 BGB erklärt Folge 63, den Sachmangel Folge 59, den Verbraucherbegriff Folge 106.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Verbrauchsgüterkauf #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt).replace("\nTillmann: ", "\nFrau Tillmann: ")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
