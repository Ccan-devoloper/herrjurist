# Folge 009 · Strafrechtsklausur Aufbau: Tatkomplexe, Beteiligte, Reihenfolge – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_009.py`](src/skript_009.py) · Methodikfolge (Fr), Beispielfall frei erfunden („Akku-Fall“) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Bruno (BR), um 60 | Fahrradmechaniker im Hinterhof, Auftraggeber (Anstifter) | Pose `standing/shirt-4` (schwarzes Hemd der Pose), Kopf `Gray Short`, Bart `Chin`, Haut `#F0C8A8`, Hose `#5A5A6A`; Mimiken `Calm`, `Suspicious` (redet), `Smile` (zufrieden), `Serious` (denkt), `Concerned|Serious` (ertappt) | `helmut` (Mann, älter) |
| Kim (KI), Anfang 20 | packt die Akkus ein, stößt Ohm weg (Tatnächste) | Pose `standing/robot_dance-3`, Kopf `Medium Bangs 3`, Oberteil Rot `#F07A6A`, Hose `#3D3D58`, Haut `#E8B98F`; Mimiken `Calm`, `Smile` (redet), `Cheeky|Smile` (cool), `Fear` (Schreck), `Very Angry` (wütend), `Concerned|Serious` (ertappt), `Serious` (denkt) | `lucy` (Frau, jung) |
| Tara (TA), Anfang 20 | lenkt Ohm ab (Mittäterin), wirft auf der Flucht die Flasche | Pose `standing/blazer-3` (ohne Prothese), Kopf `Twists 2`, Jacke Lila `#B8A9F5`, Hose `#2E2E3A`, Haut `#8D5A3B`; Mimiken `Calm`, `Smile` (freundlich), `Cheeky|Smile`, `Very Angry`, `Concerned|Serious`, `Serious` | – (spricht nicht) |
| Herr Ohm (OH), um 65 | Inhaber des Fahrradladens, Geschädigter | stehend `standing/walking-1`, am Boden `sitting/hands_back-2` (gleiches grünes Shirt `#8FD694`, schwarze Hose der Pose), Kopf `No Hair 3`, Bart `Moustache 4`, Brille `Glasses 2`, Haut `#EBC4A0`; Mimiken `Calm`, `Smile`, `Concerned|Serious` (Schreck), `Rage|Serious` (ruft), am Boden `Concerned|Serious` und `Fear` | `johann` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Grundbilder mit geschlossenem Mund (`Augen|Mund` bei `Cheeky`, `Concerned`, `Rage`); Mundzustände a/o/e nur für `BR_redet`, `KI_redet`, `OH_ruft` (je links- und rechtsblickend) und Lexi. Grundansicht gespiegelt = blickt nach links (Kopfprobe 01.10.2026), `_r` blickt nach rechts. Bruno trug zunächst Vollbart `Full 2`; im Lippen-Kontaktbild war der Mund darunter kaum sichtbar, daher Kinnbart `Chin`. Keine Prothesen-Posen. Ohm am Boden ist auf 232 px statt 480 px skaliert, damit der Kopf gleich groß bleibt. Figuren-PNGs: `../peeps/op_009/` (74 Dateien, nicht im Repository, im Drive-Master).

**Stimmenpool laut Koordinator:** lucy, helmut, ela_froh, johann. Tara spricht im Fall nicht, `ela_froh` wird nicht gebraucht. `lucy` und `johann` sprachen in einer früheren Folge (Emma, Karl), im Pool unvermeidlich.

**Abweichung von den letzten Folgen:** 006 Treppenhaus/Mietwohnung, 007 und 008 andere Gebiete. Hier: Hinterhofwerkstatt, Fahrradladen, Straßenecke (drei Orte, Tageslicht). Erste Strafrechts-Methodikfolge; zum Raser-Fall (001) kein gemeinsamer Fall, keine Nacht, andere Personen.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht). 17 Folien, 16 stumme Schiebeblenden.

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Werkstatt** `werk`→`k1` | Bodenlinie; links Fahrrad und Werkzeug, Bruno blickt nach rechts zu Kim und Tara | ph:`bicycle` (Weiß), tabler:`tools` (Grau), tabler:`battery-vertical` (leer), tabler:`battery-vertical-charging` (Grün), Pille „200 €“ | `Fall · In der Werkstatt` | Titel/Werkstatt · Bruno · „Akku fehlt“ · Kim und Tara · Bruno redet (Blase) · zwei Akkus · 200 € · Kim redet (Blase) · Tara cool, Bruno zufrieden | – |
| **B Fahrradladen** `laden`→`ecke` | Tür links, Ohm, Tara im Gespräch, Kim am Regal mit Akkus und Helmen | tabler:`door`→`door-exit` (Blau), tabler:`bell`/`bell-ringing`, tabler:`helmet` (Rot/Blau/Gelb/Lila), tabler:`battery-vertical-charging`, tabler:`backpack` (Rot) | `Fall · Im Fahrradladen` → `Fall · Ohm bemerkt die Lücke` | Laden mit Ohm · Tara lenkt ab, Helm, Ohm freundlich · Kim am Regal · zwei Akkus verschwinden, Akku über Rucksack, Kim cool · beide weg, Tür offen, Glocke · Ring um die Lücke, Ohm erschrocken | Ladenglocke (`raus`) |
| **C Ecke** `o1`→`vorbei` | Hausecke links; Ohm läuft von links, Kim und Tara rechts | tabler:`building` (Gelb), tabler:`backpack`, tabler:`hand-stop` (Gelb), ph:`beer-bottle` (Grün), roter Pfeil als Wurfbahn | `Fall · Flucht an der Ecke` | Ohm ruft (Blase) · Rucksack bei Ohm · hält Kim am Arm, „Kim will nur noch weg“ · Ohm am Boden, Prellung · Kim flieht, Tara wirft (Pfeil auf den Kopf) · Pfeil knapp vorbei, Flasche am Boden, Ohm erschrocken | Sturz (`stoss`) |
| **D Klausurfrage** `frage`→`orte` | Tafel links, Kim/Tara/Bruno rechts | tabler:`clock`, `tools`, `building-store`, `map-pin` | `Fallfrage · Wen prüfst du zuerst?` | Bearbeitervermerk · 3 Beteiligte · drei Orte · „Wen prüfst du zuerst?“, alle denken | – |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **F Tatkomplexe** `tk`→`konv` | Tafel links, rechts senkrechte Zeitleiste Werkstatt–Laden–Ecke | Icons wie D, Ringe Blau/Orange | `Aufbau › Tatkomplexe bilden` → `› Brunos Auftrag: kein eigener Tatkomplex` → `› Klausurregel, kein Gesetz` | Zeit · TK 1 · TK 2 · Auftrag kein TK · Pfeil Werkstatt→TK 1 · Klausurregel | – |
| **G1–G3 Tatkomplex 1** `naechst`→`tvt` | Tafel links, rechts Kim–Tara–Bruno mit Platzziffern 1–3 | tabler:`backpack`, `helmet` | `1. TK Diebstahl im Laden › Tatnächste zuerst` → `› A. Kim › § 242 I StGB` → `› B. Tara › §§ 242 I, 25 II StGB` → `› Mittäter getrennt prüfen` → `› C. Bruno › §§ 242 I, 26 StGB` → `Aufbau › Täter vor Teilnehmer` | je Satz eine Zeile, Ringe um „einem Dritten“ und „vorsätzlich begangener rechtswidriger Tat“, Haken, Ziffern 1/2/3, Mimikwechsel | – |
| **H1–H4 Tatkomplex 2** `flucht`→`bruno3` | Tafel links, rechts Ohm am Boden mit Rucksack, Kim bzw. Tara | tabler:`backpack`, `hand-stop`, ph:`beer-bottle` | `2. TK Flucht an der Ecke › A. Kim › I. § 252 StGB` → `› § 252 StGB: Beute schon weg` → `› II. § 223 I` → `› III. § 240 I` → `› RW: § 127 I StPO` → `› B. Tara › §§ 223 I, 224 I Nr. 2, 22, 23 I` → `› Strafbarkeit des Versuchs, § 224 II` → `› keine wechselseitige Zurechnung` → `› Bruno: kein Auftrag zur Gewalt` | § 252 mit Ring „im Besitz“, Kreuz, (−) · Haken §§ 223/240 · Notwehr/§ 127 · „Vollendetes vor Versuchtem“, Kreuz, Versuch, Qualifikation mit Grunddelikt, § 224 II · Kreuze Zurechnung | – |
| **I Konkurrenzen** `konk`→`ebenso` | Tafel links (Normtext §§ 52, 53), rechts Blöcke TK 1/TK 2 je Person | – | `Konkurrenzen` → `› Tateinheit, § 52 StGB` → `› Tatmehrheit, § 53 StGB` | § 52 · Kim Tateinheit · § 53 · Kim Tatmehrheit · Tara | – |
| **J Klausurtipp** `tipp`→`t2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Aufbau zeigen, nicht erklären` | Zeilen nacheinander | – |
| **K Klausurschema** `sch`→`s8` | breite Karte | – | `Klausurschema` | Titel · 8 Aufbaustufen | – |
| **L Merksatz** `merke`→`m3` | Lexi erklärt, Merksatz mit Marker | – | `Merksatz` | 3 Zeilenblöcke, 6 Marker | – |

**Geräusche:** zwei Handlungsgeräusche, Freesound CC0, Dateien `sfx3/szene_009glocke_1.wav`, `sfx3/szene_009sturz_1.wav`, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json). Ein geplantes Flaschen-Zerschellen entfiel, weil das Bild keine Scherben zeigt.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Bruno bittet Kim und Tara in seiner Werkstatt, ihm zwei E-Bike-Akkus aus dem Fahrradladen von Ohm zu holen; er zahlt 200 €. Die beiden sind einverstanden: Tara soll Ohm ablenken, Kim einpacken, das Geld wollen sie teilen.
>
> Im Laden verwickelt Tara Ohm in ein Gespräch, Kim steckt zwei Akkus in ihren Rucksack, beide gehen. Ohm rennt hinterher, reißt Kim an der Ecke den Rucksack vom Rücken und hält sie am Arm fest. Kim will nur noch fliehen und stößt Ohm weg; er stürzt und prellt sich den Ellenbogen. Tara wirft im Weglaufen wütend eine Glasflasche nach Ohms Kopf, um ihn zu treffen; sie fliegt knapp vorbei. Eine weitere Flasche hat Tara nicht. Für die Flucht gab es keine Absprache. Ohm stellt Strafantrag.
>
> *(Frei erfundener Übungsfall.)*
>
> **Wie haben sich Kim, Tara und Bruno strafbar gemacht?**
