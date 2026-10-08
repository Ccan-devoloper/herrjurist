# Folge 281 · Mietminderung § 536 BGB: Schimmel, Baulärm, kalte Heizung – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_281.py`](src/skript_281.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Mietrecht · Alltagsfall. Aufbau nach Auftrag: Hook (Schimmel – darfst du weniger überweisen?) → Fall im Schlafzimmer (Schimmel, Baustelle nebenan, kalte Heizung), Dialog Vermieterin/Mieter → Frage → Sachverhalt → **§ 536 Abs. 1 (Wortlautkarte Satz 1–3)** → kraft Gesetzes (Vergleich § 441 Abs. 1 in einem Satz), Mangel, Unerheblichkeit, Bruttomiete → **drei Beispiele als Tafeln**: 1. Schimmel (Baumangel oder Lüften, Beweislast, Wärmebrücken), 2. Baulärm (Bolzplatz/Baustelle), 3. kalte Heizung → **§ 536c (Wortlautkarten Abs. 1 Satz 1, Abs. 2 Satz 2 Nr. 1)** → **§ 536b (Wortlautkarte Satz 1)** → Praxisrisiko (Verzug, § 543, Irrtum, Vorbehalt, § 320) → Ergebnis im Zimmer → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 6:26,6 (5.805 vertonte Zeichen). Vorlagen: 278 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 063 (nur Vergleich Kaufrecht), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Vermieterin und Mieter fair: Frau Teuber kommt und sieht sich alles an, ruhige Haltung (Hände locker, kein Zeigefinger, keine verschränkten Arme), sachliche Einwände; Friedemann besorgt, nicht wütend. Schimmel **nur als dezentes Symbol** (sieben kleine graugrüne Flecken neben dem Schrank). Baustelle nur im Fenster (Kran, Bagger, Presslufthammer als Tabler-Icons). Kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Friedemann (FR), um 35 | Mieter | `standing/shirt-4` (Hemd schwarz der Pose, Hose Blau `#8DB3F2`), Kopf `Short 3`, Haut `#E8B894`, keine Brille, kein Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Fear` (Schreck bei der kalten Heizung), `Awe`, `Suspicious`, `Concerned\|Serious` (Sorge), `Tired` (Presslufthammer), `Smile Big\|Smile` (erleichtert), `Solemn` | `christian` (Mann, mittel) |
| Frau Teuber (TB), um 60 | Vermieterin, Eigentümerin | `standing/resting-1` (Pullover Orange `#F9A66C`, Hose schwarz der Pose), Kopf `Gray Short` (Haar `#D2D2D2`), Haut `#F0C8A8`, Brille `Glasses 3`. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned\|Serious`, `Awe` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): besetzt `christian` und `hilde`; `stephan` und `lucy` (Vorfolge 278) nicht besetzt, stephan und christian also nie gemeinsam.
- **Blickrichtung:** Beide Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Im Zimmer blickt Friedemann zunächst zu Wand, Fenster und Heizkörper (links), ab dem Auftritt von Frau Teuber zu ihr (rechts); Frau Teuber blickt nach links zu ihm. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `FR_redet`, `TB_redet` (je links/rechts) und Lexi. 56 Figuren-PNGs in `../peeps/op_281/` (nicht im Repository, im Drive-Master).
- **Namen:** Friedemann, Teuber – eindeutig deutsche Aussprache, nicht in der Liste vergebener Namen; `git grep -iw` über `youtube/`: beide ohne Treffer. Eingetragen in `namen_reserviert.txt` („281: Friedemann, Teuber“) vor der Vertonung. Kein Genitiv eines Namens (Skript-Assertion). Gesprochen von der Erzählerin (Friedemann 9×, Teuber 7×), die Figuren nennen sich nicht.

**Abweichung von den letzten Folgen (277–279; 280 lag bei Produktionsbeginn nicht im Repository):** Posen `shirt-4`, `resting-1` – dort nicht verwendet (277 `blazer-2`/`easing-1`, 278 `walking-1`/`blazer-3`, 279 `robot_dance-3`/`mid-2`/`blazer-4`); keine Polka Dots; Farben Blau/Orange statt Grün/Lila (278) und Lila/Türkis (279). Schauplatz **Schlafzimmer einer Altbauwohnung mit Schrank, Fenster zur Baustelle und Heizkörper** – neu gegenüber 277 (Baugrundstück, Behörde), 278 (Supermarkt) und 279 (Prüfungsamt). Das Zimmer kehrt im Ergebnis zurück, weil dort alle drei Mängel spielen. Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Im Zimmer** `fall`→`frage3` | ab 0,0 s Zimmer (Boden, Schrank, Fenster, Heizkörper); Pille „Darfst du weniger Miete überweisen?“; Friedemann mit Namensschild ab `fried`, Pille „Altbauwohnung: 850 € warm“; Schimmelflecken zum Wort „Schimmel“, Pillen „November: Schimmel an der Außenwand“, „Bescheid erst im Januar“; Bagger und Kran im Fenster zum Wort „baut“, Presslufthammer zum Wort; Pillen „Dezember: Neubau nebenan“, „tagsüber Presslufthammer“; Schneeflocke am Heizkörper, Pillen „Januar: Heizung 1 Woche kalt“, „am selben Tag gemeldet“ mit Telefon; Frau Teuber mit Namensschild und „Vermieterin“ (`teub`); Blasen Frau Teuber, Friedemann; drei Frage-Pillen | tabler `crane`, `backhoe`, `hammer-drill`, `snowflake`, `phone`; Schrank, Fenster, Heizkörper, Flecken programmatisch | `Fall · Die Altbauwohnung` → … (11 Stände) | Bagger im Fenster (`szene_281bagger_1`, Kopie der CC0-Datei aus Folge 277, Freesound 118974) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | – |
| **C1 § 536 Abs. 1** `w536`→`w536s3` | **Wortlautkarte Satz 1–3**, Marker „aufhebt“, „befreit“, „gemindert“, „angemessen“, „unerhebliche“; Friedemann | tabler `home`, `coins`, `tool` | `Minderung · …` (3 Stände) | – |
| **C2 kraft Gesetzes** `kraft`→`brutto` | Haken „kraft Gesetzes …“, Fundstelle § 441 Abs. 1 (Kaufrecht), Block Mangel + Fundstellen, Kreuz „unerheblich …“ + XII ZR 225/03, Block Bruttomiete, „700 € + 150 € = 850 €“; Frau Teuber | tabler `writing-sign`, `home-exclamation`, `tool`, `coins` | (4 Stände) | – |
| **D1 1. Schimmel** `drei`→`alt` | Haken „Mangel, wenn Baumangel …“, Kreuz „zu wenig gelüftet …“ + VIII ZR 138/11, Rahmen Beweislast mit zwei Stufen + XII ZR 272/97, VIII ZR 31/18, Kreuz Wärmebrücken + „zumutbares Lüften: Einzelfall“ + VIII ZR 271/17; beide Figuren | tabler `droplet`, `temperature`, `home`; Phosphor `scales` | `Drei Probleme · …` (5 Stände) | – |
| **D2 2. Baulärm** `s2`→`s2c` | Kreuz „grundsätzlich kein Mangel …“ + § 906; Blöcke Bolzplatz (VIII ZR 197/14) und Baustelle (VIII ZR 31/18) zum Wort; Darlegung Mieter, Beweis Vermieterin + Leitsätze 3, 5; Frau Teuber | tabler `crane`, `backhoe`, `volume`; Phosphor `soccer-ball`, `scales` | (4 Stände) | – |
| **D3 3. Kalte Heizung** `s3`→`s3c` | Haken „auch die Wärme …“ + XII ZR 225/03, Haken „Ausfall im Januar …“ + § 536 Abs. 1 Satz 2, Block „Um wie viel? Einzelfall …“; Friedemann | Phosphor `thermometer-cold`; tabler `snowflake`, `calendar` | (3 Stände) | – |
| **E § 536c** `w536c`→`anz2` | **zwei Wortlautkarten** (Abs. 1 Satz 1 mit „…“, Abs. 2 Satz 2 Nr. 1), Marker; „Schimmel: von November bis Januar unbekannt“, Kreuz „konnte sie deshalb nicht abhelfen …“, Haken „Heizung: sofort gemeldet …“; Friedemann | tabler `phone`, `calendar-x`, `phone-check` | `Anzeige · …` (4 Stände) | – |
| **F § 536b** `w536b`, `kennt` | **Wortlautkarte Satz 1** (Marker „Kennt“, „bei Vertragsschluss“, „nicht zu“), Kreuz „bei der Besichtigung gesehen …“; Frau Teuber | tabler `signature`, `eye` | `Kenntnis · …` (2 Stände) | – |
| **G Risiko** `risk`→`p320` | Kreuz Verzug, Kündigung + § 543, Kreuz Irrtum + VIII ZR 138/11, Block Vorbehalt + Rn. 20, § 320 + VIII ZR 19/14; beide | tabler `cash-banknote`, `file-x`, `alert-triangle`, `receipt`; Phosphor `hand-coins` | `Risiko · …` (5 Stände) | – |
| **H Ergebnis** `erg`→`erg3` | Zimmer wie A (Flecken, Baustelle, Heizkörper ohne Schneeflocke); drei Haken-Zeilen oben; beide blicken einander an | wie A | `Ergebnis · …` (3 Stände) | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **L Prüfungsschema** `sch`→`k3` | breite Karte, 8 Zeilen zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), jeweils über der sprechenden Figur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Bagger im Fenster zum Wort „baut“). Freesound-API am 08.10.2026 über den Proxy gesperrt (HTTP 403) → vorhandene CC0-Datei aus `sfx3/` unter eigenem Namen kopiert; Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Haken/Kreuz Fluent Emoji High Contrast (MIT). Zimmer, Schrank, Heizkörper, Flecken programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Friedemann mietet von Frau Teuber eine Altbauwohnung für 850 € warm: 700 € Kaltmiete und 150 € Vorauszahlung auf die Nebenkosten. Im November entdeckt er hinter dem Schrank im Schlafzimmer Schimmel an der Außenwand. Frau Teuber sagt er erst im Januar Bescheid.
>
> Seit Dezember baut der Nachbar ein neues Haus; tagsüber dröhnt der Presslufthammer. Im Januar bleibt die Heizung eine Woche lang kalt. Das meldet Friedemann noch am selben Tag.
>
> Frau Teuber meint, der Schimmel komme vom Lüften, und für die Baustelle könne sie nichts. Friedemann will ab Februar nur noch die halbe Miete überweisen.
>
> **Ist die Miete gemindert, und was riskiert Friedemann?**
