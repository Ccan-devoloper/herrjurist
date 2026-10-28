# Folge 104 · Mittäterschaft § 25 II StGB: Tatplan, Tatbeitrag, Zurechnung – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_104.py`](src/skript_104.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Format „Schema“. Fall nach dem Plan-Hook (Kioskraub: Schmiere, Drohung, Griff in die Kasse; ein Vierter hat nur geplant) → Frage → Sachverhalt → Wortlautkarte § 25 Abs. 2 und Voraussetzungen → Aufbau (gemeinsam/getrennt, im Fall begründet) → A. Kilian und Fenja: Raub kurz (Verweis Folge 087), 1. gemeinsamer Tatplan (konkludent, sukzessiv in einem Satz), 2. gemeinsame Tatausführung (wesentlicher Beitrag, Zueignungsabsicht selbst) → Abgrenzung Täter/Gehilfe (Tatherrschaftslehre, BGH) → B. Thea: Schmiere stehen, Wortlautkarte § 27 Abs. 1 → C. Ansgar: strenge/gemäßigte Tatherrschaftslehre/BGH, Streitentscheid → Rechtsfolge, Exzess (ein Satz) → Ergebnis für alle vier → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 087 (Raub, Aufbau, Hilfsfunktionen), 091/094 (Täterschaft; mittelbare Täterschaft nicht wiederholt), 015 (Namens- und Sichtprüfung).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ansgar (AN), um 50 | Planer, bleibt zu Hause | `standing/blazer-4` (Blazer Blau `#8DB3F2`, hellblaues Shirt der Pose, schwarze Hose), Kopf `Gray Short`, Haut `#E8B896`. Mimiken `Calm`, `Smile`, `Serious` (redet), `Driven`, `Solemn` | `helmut` (Mann, älter) |
| Kilian (KI), um 25 | droht nur mit Worten und verschränkten Armen | `standing/crossed_arms-2` (schwarzer Pullover der Pose, Hose Rot `#F07A6A`), Kopf `Short 4`, Haut `#F0C8A8`. Mimiken `Calm`, `Serious` (redet), `Driven`, `Solemn` | `niklas` (Mann, jung) |
| Fenja (FE), um 25 | greift in die Kasse | `standing/walking-1` (T-Shirt Lila `#B8A9F5`, schwarze Hose), Kopf `Long`, Haut `#EDC1A0`. Mimiken `Calm`, `Driven` (redet), `Serious`, `Solemn` | `julia` (Frau, jung, ruhig) |
| Thea (TH), um 20 | steht Schmiere (spricht nicht) | `standing/resting-1` (Langarmshirt Grün `#8FD694`, schwarze Hose), Kopf `Medium Bangs 3`, Haut `#D9A07A`. Mimiken `Calm`, `Suspicious` (wachsam), `Serious`, `Concerned|Serious`, `Solemn` | – |
| Emil (EM), um 60 | Kioskinhaber (spricht nicht) | `standing/shirt-4` (schwarzes Hemd der Pose, Hose Blau), Kopf `No Hair 3` (grauer Haarkranz), Haut `#F2CDB0`. Mimiken `Calm`, `Fear` (erschrickt), `Concerned|Serious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Unterscheidbarkeit der vier Beteiligten:** je eigene Pose, Farbe und Frisur (blauer Blazer/graues Haar; schwarzer Pullover, rote Hose, verschränkte Arme; lila T-Shirt, langes Haar; grünes Langarmshirt, Pony) und farbige Namensschilder (Ansgar Blau, Kilian Rot, Fenja Lila, Thea Grün, Emil Gelb) ab dem ersten Auftritt und durchgehend, solange die Figur im Bild ist. In den Tafelfolien stehen die vier immer in derselben Reihenfolge (Kilian, Fenja, Thea, Ansgar).
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Küche: Ansgar zu den anderen; Kiosk: Kilian und Fenja zu Emil).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AN_redet`, `KI_redet`, `FE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-1/2`, `shirt-1/2` bewusst nicht verwendet), keine Waffe. 76 Figuren-PNGs in `../peeps/op_104/` (Drive-Master).
- **Klischeeprüfung:** Täterrollen gewöhnlich gekleidet, gemischte Geschlechter und Hauttöne ohne Zuordnung von Herkunft oder Hautfarbe zu einer Rolle, keine „fiese“ Mimik (Drohung nur `Serious`/`Driven`); Emil respektvoll (erschrocken, nicht leidend).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen oder Themenplan unter `youtube/` (03.10.2026): Ansgar, Kilian, Fenja, Thea, Emil („Hannes“ wegen Folge 005, „Greta“ wegen 003, „Merle“ wegen englischer Lesart verworfen). Im Sprechtext nie im Genitiv mit -s („die Küche von Ansgar“, „den Gewahrsam von Emil“).
- **Stimmen** nur aus dem zugeteilten Pool (helmut, niklas, julia; `ela_froh` nicht verwendet, da ernste Rolle). Vorfolge 087 (marc, laura_ruhig): keine Überschneidung. Thea und Emil sprechen nicht (geschlossener Mund).

**Abweichung von den letzten Folgen (101 Gesetzgebung, 102 Anfechtungsurteil, 103 Werkstatt/Tilda; 087 Wochenmarkt):** neue Schauplätze Küche mit Pinnwand und Kiosk an der Ecke (Regale, Theke, Kasse, Telefon). Posen `blazer-4`, `crossed_arms-2`, `walking-1`, `resting-1`, `shirt-4` in 101–103 nicht verwendet (dort `crossed_arms-1`, `pointing_finger-1/2`, `robot_dance-2`, `polka_dots`, `shirt-3`, `easing-1/2`); kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund (Abend kurz vor Ladenschluss, beleuchteter Kiosk; kein Nachtgrund nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Küche** `fall`→`weg_a` | Ansgar ab 0,0 s mit Pinnwand; Kiosk, Uhrzeit, Rollen erscheinen zum Wort; Blase „Kilian redet, Fenja holt das Geld, Thea passt draußen auf. Ich bleibe zu Hause.“; die drei erscheinen bei ihrer Nennung mit Rollenpillen; Beute, „Thea: fest 50 €“, „während der Tat: kein Kontakt“ | fluent:`pushpin`, `convenience-store`, `eight-oclock`, `clipboard`, `light-bulb`, `money-bag`, `mobile-phone-off` | `Fall · Der Plan` (ab 0,0 s) → `Fall · Die Rollen` → `Fall · Die Beute` | – |
| **A2 Kiosk** `ecke`→`frage2` | Thea an der Ecke (wachsam, Pillen Schmiere/pfeifen/Sicherheit); Kilian baut sich vor der Theke auf, Blase „Hände weg vom Telefon, sonst schlage ich zu!“; Emil weicht erschrocken zurück; Geldschein wandert aus der Kasse in Fenjas Hand, „650 €“; Blase „Ich hab das Geld. Los!“; Kilian und Fenja laufen nach links; „Verletzt wird niemand.“; Frage-Pillen, Haus für Ansgar | fluent:`eyes`, `newspaper`, `chocolate-bar`, `candy`, `cup-with-straw`, `telephone`, `euro-banknote`, `house` | `Fall · Thea steht Schmiere` → `… Kilian droht` → `… Fenja greift in die Kasse` → `… Die drei laufen davon` → `… Die Frage` | Kassenschublade (`szene_104kasse_1`), Laufschritte (`szene_104laufen_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | – |
| **C Wortlaut § 25 II** `p25`→`v2` | Wortlautkarte, Marker; Blöcke 1./2.; alle vier rechts | fluent:`spiral-notepad`, `puzzle-piece` | `Mittäterschaft, § 25 Abs. 2 StGB › Wortlaut` → `… › Voraussetzungen` | – |
| **D Aufbau** `aufbau`→`wahl2` | Karten gemeinsam/getrennt; „Hier: Kilian und Fenja gemeinsam“, „Thea und Ansgar danach getrennt“; Pillen über den Paaren | fluent:`link` | `Aufbau › …` | – |
| **E Raub kurz** `raub`→`keiner` | Haken Drohung/Wegnahme/Finalität, Verweis Folge 087, Kreuz „keiner erfüllt alles allein“, „Deshalb: Zurechnung“ | fluent:`telephone`, `euro-banknote`, `link` | `A. Kilian und Fenja: Raub, §§ 249, 25 Abs. 2 StGB › …` | – |
| **F Tatplan** `tp`→`sukz` | verabredet, stillschweigend (5 StR 533/22), sukzessive Mittäterschaft (4 StR 115/24) | fluent:`spiral-notepad`, `handshake`, `door` | `A. … › 1. gemeinsamer Tatplan` → `… › 1. sukzessive Mittäterschaft` | – |
| **G Tatausführung** `ta`→`kf` | wesentlicher Beitrag (3 StR 363/22), Puzzleteile, Zueignungsabsicht selbst (3 StR 148/18), Ergebnis A | fluent:`puzzle-piece`, `brain` | `A. … › 2. gemeinsame Tatausführung` → `… › Zueignungsabsicht in eigener Person` → `Ergebnis A · …` | – |
| **H Abgrenzung** `abgr`→`kr3` | Karten Tatherrschaftslehre / BGH mit drei Kriterien; Thea und Ansgar | fluent:`puzzle-piece`, `balance-scale` | `Abgrenzung Täter – Gehilfe › …` | – |
| **I Thea: Schmiere** `thea`→`beide` | Kreuze Interesse/Einfluss, BGH 4 StR 665/11, 4 StR 420/05, „beide Ansichten: Thea keine Mittäterin“ | fluent:`eyes`, `coin` | `B. Thea: Mittäterin? › …` | – |
| **J § 27 I** `p27`→`thea5` | Wortlautkarte § 27 Abs. 1 mit Markern, Hilfeleisten (3 StR 496/23), Ergebnis B | fluent:`eyes` | `B. … › Beihilfe, § 27 Abs. 1 StGB` → `Ergebnis B · Thea: Gehilfin` | – |
| **K Ansgar: Streit** `ans`→`bgh_a` | drei Karten (streng, gemäßigt, BGH) | fluent:`house`, `spiral-notepad`, `balance-scale` | `C. Ansgar: Planer ohne Mitwirkung am Tatort › …` | – |
| **L Streitentscheid** `ents`→`ans3` | gemäßigte Ansicht, Argumente, Subsumtion, Ergebnis C | fluent:`balance-scale`, `money-bag` | `C. … › Streitentscheid` → `Ergebnis C · Ansgar: Mittäter` | – |
| **M Rechtsfolge** `rf`, `exz` | wechselseitige Zurechnung, Exzess (4 StR 115/24) | fluent:`link`, `spiral-notepad` | `Rechtsfolge › …` | – |
| **N Ergebnis** `erg`, `erg2` | zwei Ergebniskarten, Pillen über den Figuren | – | `Ergebnis · …` | – |
| **O Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **P Klausurschema** `sch`→`s_iii` | breite Karte, progressiv | – | `Klausurschema › …` | – |
| **Q Merksatz** `merke`→`m_3` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops. Einzige Bewegungen: Geldschein aus der Kasse in Fenjas Hand, Kilian und Fenja laufen nach links.
**Gewalt zurückhaltend:** Drohung nur mit Worten und verschränkten Armen, keine Faust, keine Waffe, kein Schlag; Emil erschrocken, nicht verletzt („Verletzt wird niemand.“).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 25 Abs. 2 und § 27 Abs. 1 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ansgar hat die Idee, den Kiosk an der Ecke kurz vor Ladenschluss zu überfallen, wenn der Inhaber Emil allein ist. Er sucht den Kiosk aus, legt die Uhrzeit fest und verteilt die Rollen: Kilian redet, Fenja holt das Geld, Thea passt draußen auf. Ansgar bleibt zu Hause und hat während des Überfalls keinen Kontakt zu den anderen. Die Beute wollen sich Ansgar, Kilian und Fenja teilen; Thea, die nicht mitgeplant hat, bekommt fest 50 €. Es soll bei diesem einen Überfall bleiben.
>
> Am Abend steht Thea an der Ecke und soll pfeifen, falls jemand kommt; das gibt den anderen Sicherheit. Kilian baut sich vor der Theke auf: „Hände weg vom Telefon, sonst schlage ich zu!“ Emil weicht erschrocken zurück. Fenja greift in die Kasse und nimmt 650 €. Die drei laufen davon. Niemand kommt vorbei, niemand wird verletzt, keiner hat eine Waffe dabei.
>
> **Wie haben sich Ansgar, Kilian, Fenja und Thea strafbar gemacht?**
