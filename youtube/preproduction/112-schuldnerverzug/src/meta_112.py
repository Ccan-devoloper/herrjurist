"""Nachbearbeitung der Upload-Texte für Folge 112 (Kopie von meta_109.py) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_112.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Kunde zahlt nicht"),
       (T("plan"), "Schuldnerverzug, § 286 BGB: Aufbau"),
       (T("a1"), "I. 1. Fälliger, durchsetzbarer Anspruch"), (T("m1"), "I. 2. Mahnung, § 286 Abs. 1 BGB"),
       (T("ent"), "Mahnung entbehrlich? § 286 Abs. 2 BGB"), (T("d1"), "I. 3. Die 30-Tage-Regel, § 286 Abs. 3 BGB"),
       (T("v1"), "I. 4. Vertretenmüssen, § 286 Abs. 4 BGB"), (T("zs"), "Zwischenergebnis am Zeitstrahl"),
       (T("r1"), "II. Verzugszinsen, § 288 BGB"), (T("s1"), "Verzögerungsschaden: Mahngebühr und Anwaltskosten"),
       (T("s287"), "Haftungsverschärfung, § 287 BGB"), (T("e1"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: Tag des Verzugsbeginns"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schuldnerverzug nach § 286 BGB: Voraussetzungen und Rechtsfolgen – ab wann schuldet der säumige Kunde Verzugszinsen (§ 288) und Anwaltskosten (§§ 280 I, II BGB)?

Der Fall: Klara hat eine kleine Fahrradwerkstatt mit Laden. Am 2. Juli 2026 kauft Gustav dort privat ein Elektrorad für 2.400 Euro – Rechnung „zahlbar sofort“, ohne Hinweis auf den Verzug nach 30 Tagen. Gustav zahlt nicht. Klara mahnt selbst (plus 5 Euro Mahngebühr), der Brief liegt am 10. August im Briefkasten. Am 1. September schaltet sie eine Anwältin ein (231,95 Euro). Ab wann schuldet Gustav Verzugszinsen – und muss er Mahngebühr und Anwaltskosten ersetzen?

Inhalt:
– I. 1. Fälliger, durchsetzbarer Anspruch: Kaufpreis (§ 433 Abs. 2 BGB), sofort fällig (§ 271 Abs. 1 BGB), keine Einrede
– I. 2. Mahnung: § 286 Abs. 1 Satz 1 BGB im Wortlaut; Entbehrlichkeit nach § 286 Abs. 2 BGB (Kalender, ernsthafte und endgültige Verweigerung)
– I. 3. Die 30-Tage-Regel: § 286 Abs. 3 Satz 1 BGB im Wortlaut – beim Verbraucher nur mit besonderem Hinweis in der Rechnung
– I. 4. Vertretenmüssen: § 286 Abs. 4 BGB im Wortlaut – vermutet; Geldmangel entlastet nicht
– Zwischenergebnis am Zeitstrahl: Verzug ab Zugang der Mahnung
– II. Verzugszinsen: § 288 Abs. 1 BGB im Wortlaut – fünf Prozentpunkte über dem Basiszinssatz (1,52 % seit 1.7.2026, also 6,52 %); Abgrenzung § 288 Abs. 2 (neun Prozentpunkte) und Abs. 5 (40-Euro-Pauschale) ohne Verbraucher
– Verzögerungsschaden, §§ 280 Abs. 1, 2, 286 BGB: Kosten der verzugsbegründenden Erstmahnung nein, Anwaltskosten nach Verzugseintritt ja
– Haftungsverschärfung: § 287 BGB im Wortlaut
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 280 I, II, 286–288 BGB; §§ 13, 187, 247, 271, 433 BGB

Rechtsprechung:
– BGH, Urt. v. 19.2.2025 – VIII ZR 138/23, Rn. 71, 77 (Anwalts- und Inkassokosten nach Verzugseintritt ersatzfähig; Kosten der verzugsbegründenden Erstmahnung in der Regel nicht)
– BGH, Urt. v. 17.9.2015 – IX ZR 280/14, Rn. 9 (Anwaltskosten bei Zahlungsverzug, auch in einfach gelagerten Fällen)
– BGH, Urt. v. 27.5.2015 – IV ZR 292/13, Rn. 51 (Schaden muss durch den Verzug verursacht sein)
– BGH, Urt. v. 8.6.2016 – VIII ZR 215/15, Rn. 18, 23 (30-Tage-Regel ohne Hinweis beim Verbraucher; einseitiger Termin des Gläubigers genügt nicht für § 286 Abs. 2 Nr. 1)
– BGH, Urt. v. 7.5.2026 – VII ZR 107/25, Rn. 48 (Begriff der Mahnung)
– BGH, Urt. v. 4.2.2015 – VIII ZR 175/14, Rn. 18 (Einstehen für die finanzielle Leistungsfähigkeit)
– BGH, Urt. v. 12.10.2017 – IX ZR 267/16, Rn. 14 (Verzugszinsen ohne Schadensnachweis)
– BGH, Urt. v. 4.7.2017 – XI ZR 562/15, Rn. 103 (Zinsbeginn am Folgetag, § 187 Abs. 1 BGB entsprechend – zu Prozesszinsen; im Video für den Verzugszins übertragen)

Hinweise: Der Fall spielt bewusst als Kaufvertrag. Bei einer Reparatur (Werkvertrag) wäre der Werklohn schon ab der Abnahme mit 4 % zu verzinsen (§ 641 Abs. 4, § 246 BGB). Die Anwaltskosten im Fall entsprechen einer 0,9-Geschäftsgebühr (Nr. 2300 VV RVG, unbestrittene Forderung) aus 2.400 Euro plus Auslagenpauschale, netto. Der Basiszinssatz ändert sich zum 1. Januar und 1. Juli (§ 247 BGB, Deutsche Bundesbank). Das System der §§ 280 ff. BGB erklärt Folge 046, Einwendungen und Einreden Folge 103.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026; Basiszinssatz Stand 1.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Schuldnerverzug #BGB #Jura
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
