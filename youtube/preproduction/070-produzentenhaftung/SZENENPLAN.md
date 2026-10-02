# Folge 070 · Explodierende Flasche: Produzentenhaftung nach § 823 I BGB – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_070.py`](src/skript_070.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Deliktsrecht, Themenplan-Format „Klassiker-Fall“. Erfundener Ausgangsfall nach dem Plan-Hook („Eine Mineralwasserflasche explodiert beim Öffnen und verletzt dein Auge“), danach die echten Fälle korrekt eingeordnet: Hühnerpest (BGHZ 51, 91, 1968: Beweislastumkehr beim Verschulden), Limonadenflasche (BGHZ 104, 323, 1988: Befundsicherungspflicht) und Mineralwasserflasche II (BGHZ 129, 353, 1995: Kontrolle jeder Flasche). Ablauf: Fall → Frage → Sachverhalt → § 823 I (Wortlaut) → Grundsatz der Beweislast (Anknüpfung an Folge 067) und Beweisnot → vier Herstellerpflichten → Hühnerpest (Fall, Beweisregel) → Befundsicherung (Limonadenflasche, Mineralwasserflasche II) → Ausreißer und Entlastung → Lösung → Abgrenzung § 1 ProdHaftG (Wortlaut, § 11, § 15 II, RL 2024/2853) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:43,4 (6.007 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Bettina (BE), um 35 | Kundin, Geschädigte | nur `standing/robot_dance-3` (ausgestreckte Hand: hält die Flasche, zeigt zur Tafel), Oberteil Blau `#8DB3F2`, Hose `#4A5A85`, Kopf `Long`, Haut `#E8BE9A`, kein Bart; vor dem Unfall ohne, danach mit Augenklappe (`Eyepatch`, abstrakt, keine Wunde); Mimiken `Calm`, `Smile`, `Fear` (Schreck), `Concerned|Serious` (redet, Sorge), `Suspicious`, `Serious`, `Smile` | `lucy` (Frau, jung) |
| Herr Kroll (KR), um 55 | Inhaber des Mineralbrunnens, Hersteller | nur `standing/shirt-3` (Hemd Grün `#8FD694`, schwarze Hose), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#E2B08C`, kein Bart; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Concerned|Serious`, `Fear` (ertappt), `Smile`, `Solemn` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |
| Beteiligte der echten Fälle | Hühnerfarm, Tierarzt, Impfstoffwerk; Kind aus BGHZ 129, 353 | **keine Figuren**, nur Symbole (Tabler `building-factory-2`, `vaccine-bottle`; Fluent High Contrast `syringe`, `chicken`) bzw. reine Tafelzeilen | – |

- **Namen** mit eindeutig deutscher Aussprache, nicht in früheren Folgen und nicht auf der Koordinatorliste (geprüft per `grep -w` im ganzen Repository): Bettina, Kroll. Kein Genitiv eines Namens („der Mineralbrunnen von Herrn Kroll“). Mineralbrunnen ohne Firmennamen, keine Marke, Flaschen ohne Etikett.
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. A1: Bettina blickt nach links zum Tisch; A2: Herr Kroll blickt nach rechts zu Bettina, Bettina nach links zu ihm; Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `BE_redet`, `KR_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** stephan, hilde, christian, lucy; gebraucht lucy und stephan (stephan und christian nie zusammen). Vorfolge 069 nutzte sabrina/william/laura_ruhig, 068 julia/helmut – keine Überschneidung.
- Keine Prothesen-Posen. Figuren-PNGs: `../peeps/op_070/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 067 (Gehweg vor der Bäckerei, Fahrrad, Sturz), 068 (Tatbestandsirrtum), 069 (Anfechtungsklage). Hier neu: Küche mit Tisch und Getränkekasten, platzende Mehrwegflasche, Mineralbrunnen mit Abfüllband, Symbolbild Hühnerfarm/Impfstoffwerk. Posen `robot_dance-3` und `shirt-3` in 067–069 nicht verwendet.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Küche** `fall`–`riss` | Tisch, Getränkekasten mit Flaschen, Bettina; Supermarkt- und Mehrweg-Pillen; Flasche in der Hand, Explosion, Augenklappe, Blase, Gutachten | tabler: `bottle` (Grün), `shopping-cart`, `recycle` (Grün), `bottle-off`, `first-aid-kit`, `microscope`; fluent-hc: `collision`; Tisch/Kasten aus `karte`/`linienzug` | `Fall · In der Küche` (ab 0,0 s) → `Fall · Die Flasche explodiert` → `Fall · Das Gutachten` | Grundbild · Supermarkt · Mehrweg · Flasche in der Hand · Explosion · Splitter am Auge · Behandlung · Blase · Mikroskop · Haarriss | `szene_070flasche_1` bei `knall` |
| **A2 Mineralbrunnen** `kroll`–`frage2` | Werk mit Abfüllband links, Herr Kroll, Bettina; Blase Herr Kroll, Forderungen, Fragen | tabler: `building-factory-2`, `bottle`, `eye`, `first-aid-kit`, `coins` (Gelb), `shopping-cart` | `Fall · Der Hersteller` → `Fall · Die Forderung` → `Fall · Die Frage` | | – |
| **B Sachverhalt** `sv` | Karte vollständig, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 823 I** `norm`–`bew2` | Wortlautkarte mit 6 Markern, blauer Block Grundsatz (mit Fundstelle BGHZ 51, 91), roter Block Problem | tabler: `scale`, `eye-off` (Rot-Pille) | `Anspruchsgrundlage · § 823 Abs. 1 BGB › Wortlaut` → `Beweislast · Grundsatz: Anspruchsteller beweist` → `Beweislast · Problem: Blick in den Betrieb` | | – |
| **D Herstellerpflichten** `vsp`–`pfall` | vier Pflichten nacheinander mit Fundstellen, gelber Block Haarriss, Haken; Herr Kroll allein | tabler: `building-factory-2`, `ruler-2`, `file-alert`, `zoom-check`, `bottle` | `Herstellerpflichten · Verkehrssicherungspflichten` → `› 1. Konstruktion` … `› 4. Produktbeobachtung` → `› Haarriss: Fabrikationsfehler` | | – |
| **E1 Hühnerpest-Fall** `huhn`–`h4` | Symbolbild: Impfstoffwerk → Impfstoff/Spritze (Tierarzt) → Hühnerfarm; Seuche, Verunreinigung, „kein Vertrag“-Linie mit Kreuz | tabler: `building-factory-2`, `vaccine-bottle` (Grün), `virus` (Rot); fluent-hc: `syringe`, `chicken` | `Hühnerpest-Fall · BGH 1968` → `· Sachverhalt` → `· kein Vertrag` | | – |
| **E2 Beweisregel** `regel`–`huhn3` | blauer Block (Geschädigte), gelber Block (Hersteller), Grund, Kreuz „nicht entlastet“ | tabler: `zoom-check`, `scale`, `building-factory-2`, `vaccine-bottle` | `Hühnerpest-Fall › Geschädigte beweist den Produktfehler` → `› Beweislastumkehr beim Verschulden` → `› keine Entlastung` | | – |
| **F1 Befundsicherung** `mehr`–`bumk` | Frage „wann entstand der Riss?“, Limonadenflasche 1988, gelber Block Beweislastumkehr | tabler: `home`, `recycle`, `clipboard-check`, `scale` | `Befundsicherung · Wann entstand der Riss?` → `· Limonadenflasche 1988` → `› Beweislastumkehr` | | – |
| **F2 Mineralwasserflasche II** `mw`–`mw3` | Tafel mit Sachverhalt (ohne Figur des Kindes), Haken „jede Flasche“, Kreuz „kaum geeignet“; Herr Kroll ertappt | tabler: `bottle-off`, `checklist`, `eye` | `Mineralwasserflasche II · 1995` → `› Kontrolle jeder Flasche` → `› Sichtkontrolle reicht kaum` | | – |
| **G Ausreißer** `aus`–`aus3` | Frage, Definition, grüner Block Entlastung | tabler: `shield-check`, `bottle`, `scale` | `Ausreißer und Entlastung` | | – |
| **H1 Lösung** `loes`–`l3` | 1.–3. mit Haken, gelber Block Beweislast bei Herrn Kroll | tabler: `gavel`, `eye`, `microscope`, `clipboard-check`, `scale` | `Lösung · Bettina gegen Herrn Kroll, § 823 Abs. 1 BGB` → `› 1. Rechtsgutsverletzung` → `› 2. Produktfehler und Kausalität` → `› 3. Befundsicherung verletzt` | | – |
| **H2 Ergebnis** `l4`–`erg2` | 4. Verschulden mit Kreuz „Entlastung gelingt nicht“, grüner Ergebnisblock, Haken Behandlungskosten/Schmerzensgeld | tabler: `scale`, `gavel`, `first-aid-kit`, `coins` | `Lösung › 4. Verschulden: Beweislastumkehr` → `Ergebnis` | | – |
| **I ProdHaftG** `phg`–`eu` | Wortlautkarte § 1 I 1 mit 3 Markern, Zeilen § 11, § 1 I 2, § 15 II, lila Block Richtlinie; Bettina allein | tabler: `book`, `bottle`, `coins`, `scale`, `refresh` | `Abgrenzung · § 1 ProdHaftG` → `› ohne Verschulden, auch für Ausreißer` → `› Sachschäden: 500 € selbst` → `› beide Ansprüche nebeneinander` → `› Reform: Richtlinie (EU) 2024/2853` | | – |
| **J Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · getrennt prüfen, Verschulden bleibt` | | – |
| **K Klausurschema** `sch`–`k4` | breite Karte, Aufbau I.–IV. mit Unterzeilen | – | `Klausurschema` → `Klausurschema › Rechtswidrigkeit, Verschulden, Schaden` | | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung (die Explosion ist ein harter Schnitt mit Symbol).
**Blasen:** Stil C (Standard seit 02.10.2026, `bausteine.blase`), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern („4.000“, „500 €“, „9-jährig“, „9.12.2026“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Bettina kauft im Supermarkt einen Kasten Mineralwasser in Mehrwegflaschen aus Glas. Zu Hause will sie eine Flasche öffnen, da explodiert die Flasche. Ein Splitter trifft Bettina am Auge; sie muss ärztlich behandelt werden. Ein Gutachter findet an der Bruchstelle einen feinen Haarriss im Glas.
>
> Abgefüllt hat das Wasser der Mineralbrunnen von Herrn Kroll. Dort sehen Mitarbeiter die Flaschen am Band nur flüchtig an. Herr Kroll sagt: „Unsere Leute schauen sich jede Flasche an. Vielleicht ist sie bei Ihnen heruntergefallen!“ Bettina verlangt von ihm die Behandlungskosten und ein Schmerzensgeld.
>
> **Haftet Herr Kroll, obwohl Bettina nur mit dem Supermarkt einen Vertrag hat?**
