# Folge 128 · Tötung auf Verlangen § 216 oder Suizidhilfe? Der Gisela-Fall – Szenenplan

**Stand:** 03./04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_128.py`](src/skript_128.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Format „Abgrenzung“. Beispielfall nach dem Plan-Hook ohne Methodendetail (Hedwig bittet ihren Mann Wilfried ausdrücklich um Hilfe beim Sterben; er führt den tödlichen Schritt selbst aus, sie kann danach nichts mehr ändern; Gegenvariante: Sie geht den letzten Schritt selbst) → Frage → Sachverhalt → 1. Ausgangspunkt (Suizid und Hilfe straflos, Verweis 094; § 212; Wortlautkarte § 216 Abs. 1, Privilegierung) → 2. Abgrenzungskriterium (wer beherrscht das Geschehen zuletzt, Tatherrschaft, Verweis 119) → Gisela-Fall (BGHSt 19, 135) → 3. neuere Rechtsprechung (BGH 6 StR 68/21: normative Betrachtung, Gesamtplan, Freispruch; BVerfG 2020 ein Satz; Verfassungsfrage offen) → 4. Merkmale (ausdrücklich, ernstlich, bestimmt) → 5. Zweispalter Täter des § 216 / strafloser Gehilfe, Ergebnis und Gegenvariante → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi) → Hilfsangebot. Hauptfilm 6:31,2.

## Zurückhaltung beim Thema Suizid (Auftrag, Vorbild Folge 094)

- **Keine Methode** in Bild, Ton, Tafeln, Sachverhaltskarte, Untertiteln oder Beschreibung: keine Mittel, Spritzen, Becher, Tabletten, Fahrzeuge, Schläuche; auch nicht beim Gisela-Fall (nur „gemeinsamer Plan, zusammen aus dem Leben zu scheiden“, „den letzten Schritt bis zuletzt in der Hand“) und beim Fall von 2022 (nur „Hauptteil er selbst, ihr aktiver Beitrag sollte den Tod vor allem absichern“).
- **Neutrale Symbole:** Schlüssel (tabler `key`) für die Herrschaft über den letzten Schritt, Schloss (tabler `lock`) für „danach nichts mehr zu ändern“, Gerichtsgebäude (Fluent `classical-building`), Akten (tabler `folder`), Jahreszahlen, Kalender, Kerze und Mond nur für „in derselben Nacht“.
- **Hedwig** erscheint nach ihrem Tod nicht mehr als Figur (A2: Wilfried allein am Fenster mit Mond und Kerze; Tafelszenen nur Wilfried). Ruhige Mimiken (`Tired`, `Serious`, `Solemn`), keine lächelnde Mimik bei Hedwig, kein „fieser“ Wilfried. Keine Musik, keine Geräusche.
- Die Beteiligten des Gisela-Falls und des Falls von 2022 erscheinen **nicht als Figuren**; das Alter der Getöteten im Gisela-Fall (16) wird nicht genannt.
- Ruhige Hilfetafel am Ende (TelefonSeelsorge, Nummern verifiziert), Hilfsangebot ganz oben in der Beschreibung.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hedwig (HE), um 70 | schwer krank, verlangt ausdrücklich und ernstlich | `standing/easing-1` (offenes Hemd Grün `#8FD694` über Shirt Lila `#B8A9F5`, schwarze Hose), Kopf `Gray Bun`, Haut `#EBC3A0`. Mimiken `Tired` (krank), `Serious` (überlegt, auch redet), `Solemn` | `hilde` (Frau, älter) |
| Wilfried (WF), um 70 | ihr Mann; Täter des § 216 bzw. in der Gegenvariante strafloser Gehilfe | `standing/resting-2` (schwarzer Pullover, Hose Blau `#8DB3F2`, ruhige Haltung), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#D9A47E`. Mimiken `Serious`, `Concerned\|Serious` (Sorge), `Solemn` (auch redet) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem zugeteilten Pool (stephan, hilde; christian und lucy nicht gebraucht). Wenig Figurenrede: je ein Satz von Hedwig und Wilfried, nicht als Dialog in derselben Szene mit stephan/christian.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Datei unter `youtube/` (`git grep -lw`, auch die unversionierten Ordner 126 ff.): Hedwig, Wilfried. „Gisela“ steht auf der Liste vergebener Figurennamen, fällt hier aber nur als Name des echten Falls („Gisela-Fall“), nie als Figur. Kein Genitiv eines Namens.
- **Blickrichtung:** Grundansicht gespiegelt (blickt nach links), Suffix `_r` blickt nach rechts. A1: Hedwig links (`_r`) blickt zu Wilfried, Wilfried rechts blickt zu ihr; A2/A3: Wilfried rechts blickt nach links zu Fenster bzw. Gericht; Tafelszenen: Wilfried rechts zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HE_redet`, `WF_redet` (je beide Blickrichtungen) und Lexi. 38 Figuren-PNGs in `../peeps/op_128/` (nicht im Repository, im Drive-Master). Keine Bärte, keine Prothesen-Posen.
- **Verworfen:** `robot_dance-3` für Hedwig (gleiche Silhouette wie Lexi), `crossed_arms-2` für Wilfried (wirkt mit ernster Mimik abweisend), `Calm`/`Smile` für Hedwig (lächelnd), sitzende Posen (sitzen auf dem Boden, ohne Möbel).

**Abweichung von den letzten Folgen (124 Ingerenz, 125 Verbrauchsgüterkauf, 126 absolute Revisionsgründe):** Posen `easing-1` und `resting-2` dort nicht verwendet (124: `shirt-4`, `walking-2`, `bike`; 125: `easing-2`, `crossed_arms-1`; 126: `blazer-1`, `blazer-4`, `resting-1`, `shirt-3`, `walking-1`); kein Polka-Dots-Muster. Schauplätze neu: Wohnzimmer des Paares (Sofa, Fenster, Pflanze, Stehlampe), Fenster bei Nacht mit Kerze, Gericht mit Akte. **Tageslicht/Cremegrund** durchgehend; die Nacht nur als Mond im Fenster.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Wohnzimmer** `fall`→`danach` | Hedwig links, Wilfried rechts, Namensschilder und Titelpille ab 0,0 s; Pillen „schwer krank“, „Schmerzen werden stärker“, „bittet ihn ausdrücklich um Hilfe beim Sterben“, Kalender „seit Monaten“, „lange und klar überlegt“; Blase Hedwig; Schlüssel bei Wilfried „führt den tödlichen Schritt selbst aus“; Schloss bei Hedwig „danach nichts mehr zu ändern“ | tabler:`sofa`, `window`, `plant-2`, `lamp`, `calendar-event`, `key`, `lock` | `Fall · Hedwig und Wilfried` → `· Die Bitte` → `· Der letzte Schritt` | Grundbild · krank · Schmerzen · Bitte · Kalender · überlegt · Hedwig redet · Wilfried Sorge · Schlüssel · Schloss | – |
| **A2 In derselben Nacht** `stirbt` | Fenster mit Mond, Kerze, Pille „Hedwig stirbt.“, Wilfried allein (`Solemn`) | tabler:`window`, `moon`, `candle` | `Fall · In derselben Nacht` | 1–2 | – |
| **A3 Anklage** `anklage`→`frage2` | Gericht, Akte „Anklage“, „Staatsanwaltschaft“; Blase Wilfried; Frage-Pillen; Schlüssel zur Gegenfrage | fluent:`classical-building`; tabler:`folder`, `key` | `Fall · Die Anklage` → `· Die Frage` | Gericht · Akte · Wilfried redet · Frage 1 · Frage 2 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,5 s | – | `Sachverhalt` | 1 | – |
| **C1 1. Ausgangspunkt** `aus`→`p212` | Tafel; Wilfried rechts | – | `1. Ausgangspunkt › Selbsttötung straflos` → `› Tötung eines anderen, § 212 StGB` | Zeilen, Pillen | – |
| **C2 § 216 Abs. 1** `p216`→`grenze` | **Wortlautkarte § 216 Abs. 1** mit Markern (Verlangen, bestimmt, Strafrahmen), „statt mindestens 5 Jahren“, gelber Block „privilegiert den Totschlag“ | tabler:`scale`, `arrows-split-2` | `1. Ausgangspunkt › § 216 Abs. 1 StGB` → `› Privilegierung des Totschlags` | Marker nacheinander | – |
| **D 2. Abgrenzungskriterium** `krit`→`selbst` | Tafel: Frage, letzter Akt, Tatherrschaft (Folge 119), roter und grüner Block | tabler:`key` | `2. Abgrenzung › Wer beherrscht den letzten Akt?` → `› Tatherrschaft, vgl. Folge 119` | Zeilen, Blöcke, Pillen | – |
| **E Gisela-Fall** `gis`→`rg` | Tafel; rechts nur Gerichtsgebäude, „Bundesgerichtshof“, „1963“, Akte (keine Figuren) | fluent:`classical-building`; tabler:`folder` | `2. Abgrenzung › Gisela-Fall, BGHSt 19, 135` → `› Gisela-Fall: Tatherrschaft` → `› subjektive Sicht verworfen` | Zeilen, Haken, Kreuz | – |
| **F1 3. BGH 2022** `neu`→`frei` | Tafel; Gerichtsgebäude, „2022“, Akte (keine Figuren) | fluent:`classical-building`; tabler:`folder` | `3. Neuere Rechtsprechung › BGH, 6 StR 68/21 (2022)` → `› normative Betrachtung` → `› Gesamtplan` → `› straflose Suizidhilfe` | Zeilen, Block, Haken, grüner Block | – |
| **F2 Selbstbestimmtes Sterben** `bverfg`, `offen` | blauer Block BVerfG 2020, offene Frage; Gerichtsgebäude „Bundesverfassungsgericht“, „2020“ | fluent:`classical-building`; tabler:`help-circle` | `3. … › Recht auf selbstbestimmtes Sterben` → `› § 216 einschränken? offen` | 2–4 | – |
| **G 4. Merkmale** `merk`→`best` | drei Blöcke ausdrücklich / ernstlich / bestimmt mit Fundstellen; Wilfried | – | `4. Merkmale des § 216 StGB` → `› ausdrücklich` → `› ernstlich` → `› bestimmt` | Block für Block | – |
| **H 5. Zweispalter und Ergebnis** `zw`→`gegen2` | Zweispalter „Täter des § 216 StGB“ (rot) / „strafloser Gehilfe“ (grün), Zeilen zum Wort; Ergebnis mit Haken, grüner Ergebnisblock, Gegenvariante; Schlüssel und Pillen bei Wilfried | tabler:`key`, `gavel` | `5. Ergebnis › Täter oder Gehilfe?` → `› Wilfried: Tatherrschaft` → `› Wilfried: § 216 Abs. 1 StGB` → `› Gegenvariante: straflos` | Zeile für Zeile | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · zuerst die Tatherrschaft` → `· an das Unterlassen denken` | Zeile für Zeile | – |
| **J Klausurschema** `sch`→`s4` | breite Karte, 1. a)–d), 2.–4. | – | `Klausurschema` → je Gliederungspunkt | 9 Aufbaustufen | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |
| **L Hilfsangebot** `hilfe`, `nummern` | ruhige hellblaue Tafel, keine Figur | tabler:`phone-call` | `Hilfsangebot` | 2 | – |

**Blasen:** Stil C (`bausteine.blase`, Assertion gegen stillen Rückfall), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Karte als Ziffern („§ 216“, „6 Monate bis 5 Jahre“, „14.8.1963“, „2022“, „0800 111 0 111“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** keine. Die Folge zeigt keine Handlung, die ein Handlungsgeräusch tragen sollte; beim Thema Suizid bewusst ruhig („lieber kein Geräusch als ein unpassendes“, `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hedwig ist schwer krank, ihre Schmerzen werden immer stärker. Seit Monaten bittet sie ihren Mann Wilfried ausdrücklich, ihr beim Sterben zu helfen; sie hat es sich lange und klar überlegt. Wilfried handelt nur, weil sie ihn darum bittet.
>
> Eines Abends gibt Wilfried nach und führt den tödlichen Schritt selbst aus. Hedwig kann danach nichts mehr ändern und stirbt in derselben Nacht. Die Staatsanwaltschaft klagt Wilfried an.
>
> Gegenvariante: Wilfried bereitet alles vor, den letzten Schritt geht Hedwig selbst.
>
> **Tötung auf Verlangen, § 216 StGB, oder straflose Suizidhilfe?**
