# Folge 143 · Fraport-Urteil: Gilt das Grundgesetz für eine Flughafen-AG? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_143.py`](src/skript_143.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Klassiker-Fall · Grundrechte. Der echte Fall wird sachlich nacherzählt (BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, BVerfGE 128, 226). Ablauf: Fall im Terminal (11.3.2003) → Flughafenverbot → Aktionäre → Instanzen → Frage → Sachverhalt → 1. Grundrechtsbindung (Wortlautkarte Art. 1 Abs. 3 GG, keine Flucht ins Privatrecht, gemischtwirtschaftliche Unternehmen/Beherrschung > 50 %, keine Quoten, Fraport gebunden, keine eigenen Grundrechte, private Aktionäre) → 2. Versammlungsfreiheit (Wortlautkarte Art. 8 Abs. 1 GG, Wahl des Ortes, kein Zutrittsrecht zu beliebigen Orten, Sicherheitsbereich/Gepäckausgabe, öffentliches Forum, Eingriff) → Meinungsfreiheit Art. 5 Abs. 1 (ein Absatz) → 3. Rechtfertigung („unter freiem Himmel“, Hausrecht, allgemeines Gesetz, legitimer Zweck, Wohlfühlatmosphäre, Verhältnismäßigkeit) → Ergebnis → mittelbare Drittwirkung/Stadionverbot (ein Satz) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:41,8 (5.887 vertonte Zeichen).

**Neutralität:** Reale Beteiligte (Beschwerdeführerin, Aktivisten, Mitarbeiter, Richter) werden nicht gezeigt; die Aktivistin erscheint nur in der Erzählung. Flugblattinhalt nur sachlich („zu einer bevorstehenden Abschiebung“). Terminal aus Grundformen mit „ABFLUG · TERMINAL 1“, Tabler `plane-departure`/`building-airport`, kein Logo, keine Fluggesellschaft.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Sievers (SI), um 45 | fiktiver Mitarbeiter der Flughafengesellschaft; vertritt sachlich die Position der Betreiberin | `standing/shirt-4` (schwarzes Hemd, Hose Marine `#4A5A85`), Kopf `Short 5` (Haar `#4A3222`), Haut `#E2B08C`, ohne Bart/Brille. Mimiken `Smile` (ruhig), `Serious` (redet), `Cute` (froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge) | `marc` (Mann, mittel) |
| Dorothea (DO), um 40 | fiktive Reisende im Terminal, bekommt ein Flugblatt, fragt | `standing/easing-2` (Jacke Koralle `#F07A6A` über schwarzem Oberteil, Hose `#3D3D58`), Kopf `Medium Bangs 2` (Haar `#8A5A3C`), Haut `#F1C6A5`. Mimiken `Smile` (ruhig), `Serious` (redet), `Cute` (froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge) | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Dorothea blickt zuerst zum Schalter (links), ab „Mitarbeiter …“ zu Herrn Sievers (`_r`); Sievers blickt zu ihr (links). Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_143.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SI_redet`, `DO_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): marc und sabrina; Erzählerin/Lexi Carla.
- **Namen:** Dorothea, Sievers – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Szenenplan/Skript/Abnahmebogen unter `youtube/preproduction` (Volltextsuche 04.10.2026). Beide Namen werden **nicht gesprochen** (nur Namensschild; auch im Sachverhalt nicht genannt). Gesprochene Eigennamen: Fraport, Frankfurt(er), Hessen.
- Figuren-PNGs: `../peeps/op_143/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 139 (`robot_dance-3`, `pointing_finger-2`), 140 (`crossed_arms-1`, `walking-1`), 141 (`blazer-4`, `crossed_arms-2`, `easing-1`, `robot_dance-2`, `blazer-3`) – hier `shirt-4` und `easing-2`, keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz **Flughafenterminal** (Fensterband mit Flugzeug, Abflugtafel, Schalter) – neu gegenüber 139–141 (Kontaktbögen und Figurenrezepte verglichen).

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Terminal 1** `fall`→`straf` | Terminal: Fensterband mit Flugzeug, Abflugtafel, Schalter; Dorothea mit Koffer; Flugblätter auf dem Schalter, eines gleitet in Dorotheas Hand; Sievers kommt von rechts, redet (Blase) | tabler `plane-departure`, `luggage`, `file-text` (Gelb), `mail` | `Fall · Terminal 1, 11.3.2003` (ab 0,0 s) → `Fall · Das Flughafenverbot` | Grundbild ab 0,0 s, Pillen Ort/Datum, Aktivisten, Flugblätter, Aktion beendet, Sievers kommt, Blase, Flughafenverbot, Brief, Strafantrag | Papier (`szene_143papier_1`, Freesound CC0 464302), als das Flugblatt Dorotheas Hand erreicht |
| **A2 Aktionäre** `aktien`→`d1` | Tafel mit Tortendiagramm 70/30 | – | `Fall · Wem gehört die Fraport?` → `Fall · Darf eine AG das verbieten?` | Sektoren und Zeilen zum Wort, Dorothea fragt (Blase) | – |
| **A3 Instanzen** `klage`→`frage2` | Tafel: AG/LG/BGH mit Kreuz, Verfassungsbeschwerde, Fragepillen | tabler `file-text`, `gavel`, `building-bank`, `building-airport` | `Fall · Der Weg durch die Instanzen` → `· Verfassungsbeschwerde` → `· Die Frage` | Zeile für Zeile | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C1 Art. 1 III** `bind`→`frei` | **Wortlautkarte Art. 1 Abs. 3 GG**, Sievers redet | tabler `building-bank`, `book`, `building-airport`, `scale` | `Grundrechtsbindung · BVerfG, 22.2.2011` → `› Art. 1 Abs. 3 GG` → `› auch in privatrechtlicher Form` → `› keine Flucht ins Privatrecht` → `› Bürger frei, Staat gebunden` | Karte, 3 Marker, Blase, Haken, Kreuz, Block | – |
| **C2 Beherrschung** `gemischt`→`quote` | Tafel mit kleiner Torte | tabler `chart-pie`, `chart-pie-2`, `x` | `… › gemischtwirtschaftliche Unternehmen` → `› Beherrschung` → `› mehr als 50 % öffentlich` → `› keine Bindung nach Quoten` | Zeilen, grüner Block, Kreuz | – |
| **C3 Fraport** `fraport`→`aktion` | Tafel | tabler `building-airport`, `key`, `chart-pie` | `… › Fraport: unmittelbar gebunden` → `› keine eigenen Grundrechte` → `› private Aktionäre` | Block, Kreuz, Zeilen | – |
| **D1 Art. 8 I** `a8`, `ort` | **Wortlautkarte Art. 8 Abs. 1 GG**, Dorothea | tabler `book`, `map-pin` | `Art. 8 Abs. 1 GG · Versammlungsfreiheit` → `› Schutzbereich: Wahl des Ortes` | Karte, 3 Marker, Haken | – |
| **D2 Keine beliebigen Orte** `kein`→`gepaeck` | Tafel mit Icon-Kacheln und Kreuzen | tabler `building`, `swimming`, `building-hospital`, `lock`, `scan`, `luggage` | `› kein Zutritt zu beliebigen Orten` → `› nicht: Sicherheitsbereich` → `› nicht: reine Funktionsbereiche` | Kachel für Kachel, Kreuze | – |
| **D3 Öffentliches Forum** `forum`→`eingriff` | Tafel mit Kacheln Läden/Cafés/Flanieren | tabler `shopping-bag`, `coffee`, `armchair`, `building-airport`, `ban` | `› allgemeiner öffentlicher Verkehr` → `› Leitbild: öffentliches Forum` → `› Frankfurter Flughafen (+)` → `Art. 8 Abs. 1 GG › Eingriff` | Haken, Kacheln, Block | – |
| **E Art. 5 I** `a5`→`raum` | Tafel, Dorothea | tabler `message`, `file-text`, `map-pin` | `Art. 5 Abs. 1 Satz 1 GG · Meinungsfreiheit` → `› Flugblätter verteilen` → `› ohne Raumbezug` | Haken, Zeile, Block | – |
| **F1 Schranken** `schranke`→`allg` | Tafel | tabler `scale`, `building-airport`, `key`, `book` | `Rechtfertigung · Schranken` → `› „unter freiem Himmel“, Art. 8 Abs. 2 GG` → `› Hausrecht, §§ 903, 1004 BGB` → `› Art. 5: allgemeines Gesetz` | Zeilen, Haken, lila Block | – |
| **F2 Legitimer Zweck** `zweck`→`wohl` | Tafel | tabler `scale`, `shield-check`, `sofa` | `› legitimer Zweck` → `› Sicherheit, Funktionsfähigkeit (+)` → `› keine Wohlfühlatmosphäre` | Zeile, Haken, Kreuz | – |
| **F3 Verhältnismäßigkeit** `s2b`→`erlaub` | Tafel, Sievers redet (Blase) | tabler `building-airport`, `speakerphone`, `scan`, `ban` | `› Störung des Betriebs?` → `› mehr Beschränkungen als auf der Straße` → `› pauschales Verbot unverhältnismäßig` → `› keine allgemeine Erlaubnispflicht` | Blase, 3 Haken, roter Block, 2 Kreuze | – |
| **G Ergebnis, Bedeutung** `erg`→`stadion` | Tafel | tabler `circle-check`, `building`, `ball-football` | `Ergebnis · Verfassungsbeschwerde begründet (+)` → `Bedeutung · rein private Unternehmen` → `Bedeutung · Stadionverbot, 1 BvR 3080/09` | Block, Zeilen, Haken | – |
| **H Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | Zeile für Zeile | – |
| **I Prüfschema** `sch`→`k4` | breite Karte: Vorab Grundrechtsbindung – I. Schutzbereich – II. Eingriff – III. Rechtfertigung – Art. 5 entsprechend | – | `Prüfschema` → je Gliederungspunkt | 10 Aufbaustufen | – |
| **J Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („11.3.2003“, „70 %“, „§§ 903, 1004 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Flugblatt gleitet in Dorotheas Hand (0,8 s), Sievers kommt von rechts (1,0 s).
**Geräusch:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Terminal, Abflugtafel, Schalter und Tortendiagramm aus Grundformen (`terminal()`, `torte()` in `folien_143.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frankfurter Flughafen, 11. März 2003: Eine Aktivistin geht mit fünf weiteren Aktivisten einer Initiative gegen Abschiebungen in Terminal 1 und verteilt Flugblätter zu einer bevorstehenden Abschiebung. Mitarbeiter der Flughafengesellschaft und der Bundesgrenzschutz beenden die Aktion.
>
> Am 12. März 2003 erteilt die Betreiberin, die Fraport AG, ihr ein Flughafenverbot: Ohne Erlaubnis darf sie den Flughafen nicht für Meinungskundgaben und Demonstrationen nutzen; sonst droht ein Strafantrag wegen Hausfriedensbruchs. Land Hessen, Stadt Frankfurt und Bund halten damals rund 70 % der Aktien, der Rest ist in privater Hand.
>
> Die Klage der Aktivistin bleibt vor Amtsgericht, Landgericht und Bundesgerichtshof ohne Erfolg. Sie erhebt Verfassungsbeschwerde.
>
> **Verletzen die Urteile, die das Flughafenverbot bestätigen, ihre Grundrechte?**
