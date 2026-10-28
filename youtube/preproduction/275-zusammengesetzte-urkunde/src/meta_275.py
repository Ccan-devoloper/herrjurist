"""Nachbearbeitung der Upload-Texte für Folge 275 (nach meta_273.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Quellen,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen in Figurenrede wie in den Blasen).
Aufruf: python3 meta_275.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: das vertauschte Preisschild"),
       (T("p267"), "§ 267 StGB und Urkundenbegriff"),
       (T("allein"), "Zusammengesetzte Urkunde: Schild und Ware"),
       (T("fest"), "Wann ist das Schild fest verbunden?"),
       (T("umk"), "Umkleben: Verfälschen oder Herstellen?"),
       (T("gebr"), "Gebrauchen, Vorsatz, offener Karton"),
       (T("betrug"), "Betrug an der Kasse, § 263 StGB"),
       (T("erg"), "Konkurrenzen und Ergebnis"),
       (T("tipp"), "Klausurtipp: § 274 nicht vergessen"),
       (T("sch"), "Prüfschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Zusammengesetzte Urkunde nach § 267 StGB: Wann bilden Preisschild und Ware eine Beweiseinheit – und was folgt aus dem Umkleben (auch § 263 StGB)?

Der Fall: Im Baumarkt zieht Karlheinz das 29-€-Schild einer billigen Bohrmaschine ab, reißt das 149-€-Schild der teuren ab und klebt das billige fest darauf. An der Kasse zahlt er 29 €. Hat er eine Urkunde gefälscht, obwohl das Schild selbst echt ist?

Inhalt:
– § 267 Abs. 1 StGB im Wortlaut, Urkundenbegriff kurz (ausführlich in der Folge „Was ist eine Urkunde? Die gefälschte Entschuldigung“)
– Zusammengesetzte Urkunde: Erklärung und Bezugsobjekt fest verbunden = neue Beweiseinheit; Beweiszeichen wie die Fahrzeugidentifikationsnummer; aufgeklebte Preisschilder und Strichcode (OLG Karlsruhe)
– Wann fest verbunden? Aufgeklebt ja, lose angeheftet oder bloß aufgesteckt nein
– Umkleben: Verfälschen durch Austausch des Bezugsobjekts (Rechtsprechung), zugleich Herstellen einer unechten Urkunde, Gegenansicht
– Gebrauchen an der Kasse, Vorsatz, Täuschung im Rechtsverkehr; Variante: teure Ware im offenen Karton der billigen
– Betrug an der Kasse nach § 263 Abs. 1 StGB, Tateinheit
– Klausurtipp (§ 274 StGB beim abgerissenen Schild), Prüfschema, Merksatz

Normen: §§ 267, 263, 274 Abs. 1 Nr. 1, 52 StGB
Rechtsprechung: OLG Karlsruhe, Beschl. v. 13.3.2019 – 1 Rv 3 Ss 691/18 (Strichcode-Etikett und Ware als zusammengesetzte Urkunde; Verfälschen durch Austausch des Bezugsobjekts nur bei fester Verbindung); BGH, Urt. v. 17.10.2019 – 3 StR 521/18 (FIN als Beweiszeichen, Gebrauchen)

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT), Phosphor Icons (MIT), Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound 590417 (MrFossy), 489967 (falcospizaetus), 378269 (13GPanska_Jirova_Tereza), jeweils CC0.

#Urkundenfälschung #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"hundertneunundvierzig(\s+)Euro", r"149\1€"), (r"[Nn]eunundzwanzig(\s+)Euro", r"29\1€")]:
    srt, n = re.subn(muster, ersatz, srt, flags=re.M | re.S)
    assert n, muster
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
