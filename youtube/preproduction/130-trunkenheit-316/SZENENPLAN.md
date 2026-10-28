# Folge 130 · Trunkenheit im Verkehr § 316: 0,3 – 0,5 – 1,1 – 1,6 Promille – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_130.py`](src/skript_130.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · StGB BT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Autofahrer wird mit 0,8 Promille kontrolliert, fährt aber schnurgerade – ein anderer hat 1,2 Promille“): Verkehrskontrolle am Ortsausgang; Heinrich (0,8 ‰, schnurgerade, keine Ausfallerscheinungen) und Siegfried (1,2 ‰, unauffällig, hält sich für fit). Niemand wird gefährdet. Ablauf: Fall → Frage → Sachverhalt → Wortlautkarte § 316 Abs. 1 (Führen im Verkehr, Kern, Grenzwerte = Beweisregeln) → 1. absolute Fahruntüchtigkeit (1,1 ‰, BGHSt 37, 89, Sicherheitszuschlag, unwiderleglich; Radfahrer 1,6 ‰ OLG) → 2. relative Fahruntüchtigkeit (etwa ab 0,3 ‰, Ausfallerscheinungen, Kausalität) → 3. Wortlautkarte § 24a Abs. 1 StVG (0,5 ‰ / 0,25 mg/l, Fahrverbot; Abs. 1a, § 24c je ein Satz) → 4. Vorsatz/Fahrlässigkeit → 5. Abgrenzung § 315c → Ergebnis (§ 21 OWiG, § 69) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 5:27,3.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Heinrich, um 45 | Autofahrer, 0,8 ‰, fährt schnurgerade | `standing/robot_dance-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`, offene Handgeste), Kopf `Short 4` (dunkelbraun), Haut `#E8B894`, kein Bart, keine Brille. Mimiken `Calm`, `Concerned|Serious` (redet, Sorge), `Suspicious`, `Solemn`, `Awe` (Atemtest schlägt an) | `marc` (Mann, mittel) |
| Siegfried, um 60 | Autofahrer, 1,2 ‰, unauffällig, hält sich für fit | `standing/blazer-3` (gelbes Jackett `#F9D56E`, schwarzes Shirt, graue Hose), Kopf `No Hair 2` (grauer Haarkranz), Brille `Glasses 2`, Haut `#F0CDB4`. Mimiken `Calm`, `Smile` (redet, froh), `Solemn`, `Concerned|Serious`, `Tired` (Ergebnis) | `william` (Mann, älter) |
| Polizistin, um 35 | Funktionsrolle ohne Namen: kontrolliert | `standing/blazer-4` (Jackett Dunkelblau `#2F3D63`, Oberteil Hellblau – uniformähnlich), Kopf `Medium Bangs`, Haut `#D9A47E`. Mimiken `Calm`, `Serious` (redet, ernst) | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** Alle Posen blicken im Original nach rechts (Kontaktbild `out/besetzung_130.png`); Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. Kontrollstelle: Autos kommen von links und halten; Heinrich bzw. Siegfried stehen rechts neben ihrem Auto und blicken nach rechts zur Polizistin; die Polizistin blickt nach links zu ihnen. Tafelszenen: Figuren rechts, blicken nach links. **Sachlich:** keine bösen Mimiken, keine Karikatur, keine Prothesen-Posen für die Fahrer. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HE_redet`, `SI_redet`, `PO_redet` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool (marc, william, sabrina; laura_ruhig nicht benötigt); Vorgängerfolge 124 nutzte christian/lucy. **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und als Figurenname in keinem Skript oder Szenenplan unter `youtube/preproduction/` (Volltextsuche 04.10.2026): Heinrich, Siegfried. Figuren-PNGs: `../peeps/op_130/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 127 (`blazer-2`, `crossed_arms-2`), 128 (`easing-1`, `resting-2`), 129 (`pointing_finger-2`, `shirt-4`), 124 (`walking-2`, `shirt-4`, `sitting/bike`; Dorfstraße mit Häusern und Tempo-50-Schild). 130: **Kontrollstelle am Ortsausgang** (Landstraße mit durchgezogener Randlinie, Bäume, Ortsausgangsschild als Grundform ohne Ortsnamen, Streifenwagen, Leitkegel) – andere Kulisse als 124, keine Häuser, kein Tempo-Schild; Posen `robot_dance-2`, `blazer-3`, `blazer-4` in 127–129 nicht verwendet; keine Polka Dots, keine Bärte. Neues Element: Promille-Thermometer als wachsende Skala.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Kontrolle Heinrich** `fall`→`h1` | Landstraße am Ortsausgang; Heinrichs Auto steht ab 0,0 s links, fährt schnurgerade heran und hält; Polizistin mit Streifenwagen und Leitkegeln; Heinrich steht neben dem Auto | tabler:`car` (Blau), `trees` (Grün), `cone` (Rot), `test-pipe`; fluent:`police-car`; `kontrollstelle()`, `ortsschild()` programmatisch; grüne Fahrlinie | `Fall · Am Ortsausgang` (ab 0,0 s) → `Fall · Die Verkehrskontrolle` → `Fall · Heinrich wird kontrolliert` → `Fall · Heinrich: 0,8 ‰` | Kulisse + Auto ab 0,0 s · „Verkehrskontrolle“, Polizistin, Streifenwagen · Auto fährt heran, „fährt schnurgerade, kein Fahrfehler“, Fahrlinie · Polizistin redet (Blase) · „Atemtest schlägt an“, Heinrich staunt · „Blutprobe: 0,8 ‰“ · Heinrich redet (Blase) | Heranfahren und Anhalten (`szene_130anfahrt_1`, Freesound CC0 136536) |
| **A2 Kontrolle Siegfried** `sieg`→`frage2` | derselbe Ort kurz darauf; Siegfrieds gelbes Auto fährt heran | wie A1, tabler:`car` (Gelb) | `Fall · Siegfried wird kontrolliert` → `Fall · Siegfried: 1,2 ‰` → `Fall · Niemand gefährdet` → `Fall · Die Frage` | „Kurz darauf“, Auto fährt heran · „fährt völlig unauffällig“ · Siegfried, „Blutprobe: 1,2 ‰“ · Siegfried redet (Blase), froh · „niemand gefährdet oder verletzt“ · zwei Fragepillen | Abbremsen und Halt (`szene_130halt_1`, Freesound CC0 369901) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C § 316 Abs. 1** `p316`→`zahl` | **Wortlautkarte § 316 Abs. 1 (vollständig)**, fünf Marker zum Vorlesen; beide Fahrer rechts | tabler:`book`, `glass` (neutral, bei „alkoholischer Getränke“), `car`, `help-circle`, `gavel` | `§ 316 StGB › Wortlaut Abs. 1` → `› Führen eines Fahrzeugs im Verkehr` → `› Fahruntüchtigkeit infolge Alkohols` → `› Grenzwerte: Beweisregeln` | Karte + Marker, Haken, Zeilen | – |
| **D 1. Absolute Fahruntüchtigkeit** `abs`→`radbgh` | Tafel; rechts **Promille-Thermometer** (Röhre, 1,1-‰-Marke mit roter Zone, Siegfried-Punkt 1,2 ‰, 1,6-‰-Marke Radfahrer + Fahrrad-Icon); Siegfried | tabler:`bike` (Gelb) | `§ 316 StGB › 1. Absolute Fahruntüchtigkeit` → `› ab 1,1 ‰` → `› unwiderleglich` → `› Siegfried: 1,2 ‰` → `› Radfahrer: 1,6 ‰` | Zeile für Zeile, Skala wächst | – |
| **E 2. Relative Fahruntüchtigkeit** `rel`→`hein_neg` | Tafel; Thermometer mit 0,3-‰-Marke (gelbe Zone 0,3–1,1), Heinrich-Punkt 0,8 ‰; Heinrich | – | `§ 316 StGB › 2. Relative Fahruntüchtigkeit` → `› Ausfallerscheinungen` → `› Heinrich: 0,8 ‰` → `› Heinrich (−)` | Haken/Kreuze, Block | – |
| **F 3. § 24a StVG** `owi`→`anf` | **Wortlautkarte § 24a Abs. 1 StVG (vollständig)**, vier Marker; Thermometer mit 0,5-‰-Marke; Heinrich | – | `3. Ordnungswidrigkeit, § 24a StVG` → `› Wortlaut Abs. 1` → `› ohne Ausfallerscheinungen` → `› Heinrich: 0,8 ‰ (+)` → `§ 24a Abs. 1a, § 24c StVG` | Karte + Marker, Zeilen | – |
| **G 4. Vorsatz/Fahrlässigkeit** `vors`→`fahrl` | Tafel; vollständiges Thermometer; Siegfried | – | `§ 316 StGB › 4. Vorsatz oder Fahrlässigkeit` → `› Grenzwert kein Vorsatzgegenstand` → `› Siegfried: fahrlässig, Abs. 2` | Zeilen, Block | – |
| **H 5. Abgrenzung § 315c** `p315c`→`subs` | Tafel; beide Fahrer rechts | tabler:`alert-triangle` (Gelb, Rot), `shield-check`, `book` | `5. Abgrenzung: § 315c StGB` → `› konkrete Gefahr: Beinahe-Unfall` → `› hier (−)` → `› § 316 bleibt anwendbar` | Zeile für Zeile | – |
| **I Ergebnis** `erg`→`erg2` | Blöcke zum Wort | tabler:`gavel`, `id` | `Ergebnis · Siegfried: § 316 Abs. 1, 2 StGB` → `· § 21 Abs. 1 OWiG` → `· § 69 Abs. 2 Nr. 2 StGB` → `· Heinrich: § 24a Abs. 1 StVG` | 5 | – |
| **J Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Grenzwert = Beweisregel` → `· unter 1,1 ‰: Ausfallerscheinungen` | Zeile für Zeile | – |
| **K Prüfschema** `sch`→`k4` | breite Karte, grüner Kasten Fahruntüchtigkeit | – | `Prüfschema` → je Gliederungspunkt ein Pfadstand | 10 Aufbaustufen | – |
| **L Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`, stiller Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („0,8 ‰“, „1,1 ‰“, „§ 24a Abs. 1 StVG“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Heinrichs Auto (1,4 s), Siegfrieds Auto (1,9 s).
**Darstellung:** kein Alkoholkonsum im Bild, keine Flaschen, kein Anstoßen; einziges Getränke-Icon ist das neutrale leere Glas (tabler:`glass`) an der Stelle „alkoholischer Getränke“ der Wortlautkarte. Kein Unfall, keine Verletzten, keine Sirene.
**Geräusche:** zwei Handlungsgeräusche (beide Autos fahren heran und halten), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT; Streifenwagen), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Straße, Ortsausgangsschild und Thermometer aus Grundformen (`kontrollstelle()`, `ortsschild()`, `skala()` in `folien_130.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> An einem Freitagnachmittag kontrolliert eine Polizistin am Ortsausgang den Verkehr. Heinrich fährt mit seinem Auto heran, schnurgerade und ohne jeden Fahrfehler; auch sonst zeigt er keine Auffälligkeiten. Der Atemtest schlägt an. Die Blutprobe ergibt eine Blutalkoholkonzentration von 0,8 ‰.
>
> Kurz darauf hält die Polizistin Siegfried an. Auch er ist völlig unauffällig gefahren. Seine Blutprobe ergibt 1,2 ‰. Siegfried hält sich für fahrtüchtig: „Ich fühle mich topfit.“
>
> Gefährdet oder verletzt wurde niemand.
>
> **Wie haben sich Heinrich und Siegfried strafbar gemacht? Ordnungswidrigkeiten?**
