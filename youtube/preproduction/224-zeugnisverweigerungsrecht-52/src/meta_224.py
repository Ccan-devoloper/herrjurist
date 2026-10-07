"""Nachbearbeitung der Upload-Texte für Folge 224 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_221.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen und Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel: Sprecherbezeichnung „Frau Wehner:“, lautliche Schreibung „Ladewich“ (nur Vertonung) → „Ladewig“.
Aufruf: python3 meta_224.py <upload-ordner>"""
import json, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Aussage gegen den Verlobten"),
       (T("pol"), "Fall: Polizei und Ermittlungsrichter"),
       (T("hv"), "Fall: Zeugnisverweigerung in der Hauptverhandlung"),
       (T("wg"), "Fall: Aussage gegen den Mitbewohner?"),
       (T("fragen"), "Die Fragen und der Sachverhalt"),
       (T("pflicht"), "Grundsatz: Zeugenpflicht, § 48 StPO"),
       (T("a52"), "§ 52 Abs. 1 StPO: Wer darf schweigen?"),
       (T("verl"), "Verlobte – und wer nicht erfasst ist"),
       (T("bel"), "Belehrung, § 52 Abs. 3 StPO"),
       (T("a252"), "§ 252 StPO: Schweigen erst in der Hauptverhandlung"),
       (T("a53"), "§ 53 StPO: Berufsgeheimnisträger"),
       (T("a55"), "§ 55 StPO: Auskunftsverweigerung"),
       (T("l1"), "Lösung: gegen den Verlobten"),
       (T("l2"), "Lösung: gegen den Mitbewohner"),
       (T("tipp"), "Klausurtipp: Zeuge in drei Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Zeugnisverweigerungsrecht nach § 52 StPO: Muss ich gegen meinen Partner aussagen? Wer schweigen darf, wann zu belehren ist, was § 252 StPO mit früheren Aussagen macht – und was § 53 und § 55 StPO regeln.

Der Fall: Frau Wehner ist mit Herrn Störmer verlobt. Gegen ihn wird wegen Betrugs ermittelt. Bei der Polizei und vor dem Ermittlungsrichter sagt sie nach Belehrung gegen ihn aus – in der Hauptverhandlung verweigert sie das Zeugnis. Später soll sie gegen ihren Mitbewohner aussagen. Darf sie schweigen, und was wird aus ihren früheren Aussagen?

Inhalt:
– Grundsatz: Zeugenpflicht, § 48 Abs. 1 S. 2 StPO
– § 52 Abs. 1 StPO: Verlobte, Ehegatten (auch nach der Scheidung), Lebenspartner, Verwandte und Verschwägerte
– Verlöbnis: keine Form, beiderseitiger Heiratswille; nicht erfasst: Freunde, Mitbewohner, Paare ohne Verlobung
– Belehrung vor jeder Vernehmung, § 52 Abs. 3 StPO – auch bei Polizei und Staatsanwaltschaft
– § 252 StPO: Verlesungs- und Verwertungsverbot, Ausnahme für den Ermittlungsrichter (mehr in Folge 221)
– Abgrenzung: § 53 StPO (Berufsgeheimnisträger) und § 55 StPO (Auskunftsverweigerung für einzelne Fragen)
– Lösung des Falls, Klausurtipp mit Prüfung in drei Schritten, Merksatz

Rechtsprechung:
– BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, BGHSt 61, 221, Leitsatz und Rn. 32: § 252 StPO als Verwertungsverbot; Vernehmung des Richters nach Belehrung gemäß § 52 Abs. 3 S. 1 StPO zulässig, keine weitergehende Belehrung nötig
– BGH, Urt. v. 28.5.2003 – 2 StR 445/02, BGHSt 48, 294: Verlöbnis formlos, Heiratswille; Verwertungsverbot bei fehlender Belehrung
– BGH, Beschl. v. 9.3.2010 – 4 StR 606/09, BGHSt 55, 65, Rn. 13 f.: Beurteilung des Verlöbnisses durch das Gericht
– BGH, Urt. v. 10.2.2021 – 6 StR 326/20, Rn. 18, 22: Zweck des § 52 StPO, Belehrungsfehler, Mitbeschuldigte
– BGH, Beschl. v. 21.8.2024 – StB 39/24, Rn. 8, 10: Verfolgungsgefahr und einzelne Fragen bei § 55 StPO

Hinweise: Der Fall ist ein Übungsfall. BGHSt 48, 294 ist nach der Gliederung des amtlichen Abdrucks zitiert (ohne Randnummern). Das frühere „Versprechen, eine Lebenspartnerschaft zu begründen“ steht seit 22.12.2018 nicht mehr in § 52 Abs. 1 Nr. 1 StPO.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StPO #Zeugnisverweigerungsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nWehner: ", "\nFrau Wehner: "), ("Ladewich", "Ladewig"), ("des §§ 52", "des § 52")):
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert "Paragraf" not in srt and "Ladewich" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["§ 52 StPO", "Zeugnisverweigerungsrecht", "Angehörige als Zeugen", "§ 252 StPO", "GSSt 1/16",
             "§ 55 StPO Auskunftsverweigerung", "§ 53 StPO Berufsgeheimnisträger", "Belehrung Zeuge", "Strafprozessrecht"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
