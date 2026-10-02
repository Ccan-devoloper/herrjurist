# Folge 062 · Rechtfertigende Einwilligung: Wann ist Körperverletzung erlaubt? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_062.py`](src/skript_062.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Tätowierer sticht einer 17-Jährigen ein großes Motiv auf den Unterarm – mit ihrer Zustimmung, aber ohne die der Eltern“), sachlich und unblutig: Marie (17) wünscht sich seit Monaten einen Zweig mit Blüten auf dem Unterarm; Tätowierer Herr Riedel zeigt die Skizze, erklärt Dauer, Schmerz und schwere Entfernbarkeit, fragt nach den Eltern („Nein. Aber ich bin 17, und es ist mein Arm.“), Marie unterschreibt, er sticht fachgerecht nach der Skizze. Ablauf: Fall → Frage → Sachverhalt → Tatbestand § 223 I (Wortlautkarte) → § 228 (Wortlautkarte), Einwilligung als Rechtfertigungsgrund, Einverständnis kurz → 1. Dispositionsbefugnis → 2. Einwilligungsfähigkeit (Zitatkarte BGH 1 StR 368/19 Rn. 57) → Jugendliche und Marie → Streit Minderjährige/Eltern, Zivilrecht ein Satz → 3.–5. Erklärung, Willensmängel, Kenntnis → 6. § 228 → Ergebnis → Abwandlung 14 Jahre → Abwandlung Täuschung → Ausblick mutmaßliche Einwilligung → Klausurtipp → Schema → Merksatz. Hauptfilm 6:50,6 (Begründung für mehr als 4.600 Zeichen in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Marie, 17 | Kundin, Einwilligende | Pose `standing/easing-1` (offene hellblaue Jacke, grünes Shirt `#8FD694`, schwarze Hose, Sneaker), Kopf `Long Bangs`, Haut `#F2CDB0`; Mimiken `Calm`, `Serious` (redet, ernst), `Smile`, `Suspicious` (denkt), `Concerned\|Serious` (Sorge), `Fear` (Schreck in Abwandlung 2) | `lucy` (Frau, jung) |
| Herr Riedel, um 40 | Tätowierer | Pose `standing/shirt-3` (lila Hemd `#B8A9F5`, schwarze Hose), Kopf `Short 1`, ohne Bart, Haut `#E2B088`; Mimiken `Calm` (redet), `Smile` (redet in Abwandlung 2: `RI_luegt`), `Serious` (denkt), `Suspicious`, `Concerned\|Serious` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** `shirt-3` blickt im Original nach rechts, `easing-1` nach links (im Fallbild geprüft); `figuren_062.py` erzeugt daher die Grundansicht beider Figuren mit Blick nach links (zur Tafel bzw. zum Gegenüber), `_r` mit Blick nach rechts (Herr Riedel im Studio zu Marie). **Keine Prothesen-Posen** (`shirt-1/2`, `blazer-1/2` verworfen), keine Bärte. `robot_dance-3` verworfen (Silhouette wie Lexi). Marie respektvoll als selbstbewusste, nachdenkliche Jugendliche in Alltagskleidung; Herr Riedel ohne Tattoo-, Rocker- oder Schwarz-Klischee (lila Hemd, ruhige Mimik; `pointing_finger-1` verworfen: ganz in Schwarz mit Stiefeln). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MA_redet`, `RI_redet`, `RI_luegt` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool; nur eine Männerstimme (stephan), christian wird nicht eingesetzt, hilde nicht benötigt. **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan oder Abnahmebogen 001–061 verwendet: Marie, Riedel. Figuren-PNGs: `../peeps/op_062/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 061 (Seeufer/Wohnung; `resting-1`, `blazer-3`, `easing-2`; julia, helmut, niklas), 060 (Wohnstraße, Polizei, Staatsanwalt; `walking-2`, `blazer-3`, `walking-1`, `crossed_arms-1`; lucy, hilde, christian, stephan). 062: **Tattoostudio** (Behandlungsstuhl, kleiner Tisch mit Skizze und Formular) – neuer Schauplatz; Posen `easing-1` (zuletzt 058) und `shirt-3` (nicht in 053–061). lucy und stephan wie in 060, aber andere Rollen, Posen und Szenen (Pool vorgegeben). Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Tattoostudio** `fall`→`frage2` | Bodenlinie; links Behandlungsstuhl, Mitte kleiner Tisch, Herr Riedel links (blickt nach rechts), Marie rechts | tabler:`armchair` (Lila), `table` (Holz), `infinity`, `writing-sign` (Formular), `plant-2` (Grün) + fluent:`cherry-blossom` (Skizze und Motiv), Ring um das Motiv am Unterarm | `Fall · Im Tattoostudio` (ab 0,0 s) → `Fall · Die Aufklärung` → `Fall · Ohne die Eltern` → `Fall · Unterschrift und Motiv` → `Fall · Die Frage` | Studio ab 0,0 s · Marie kommt, 17 Jahre · Denkblase „seit Monaten: ein großes Motiv“ · Zweig · Unterarm · Riedel und Skizze (schiebt sie auf den Tisch) · bleibt für immer · tut weh · schwer zu entfernen · Riedel redet (Blase) · Marie redet (Blase) · unterschreibt · fachgerecht · Motiv am Unterarm · zwei Fragepillen | Skizze über den Tisch geschoben (`szene_062skizze_1`), Unterschrift (`szene_062unterschrift_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C Tatbestand** `p223`→`vors` | **Wortlautkarte § 223 Abs. 1**, Misshandlungsdefinition, OLG Hamm | fluent:`cherry-blossom`, tabler:`circle-check` | `Tatbestand › § 223 Abs. 1 StGB` → `› körperliche Misshandlung` → `› Tätowierung als Körperverletzung` → `› Vorsatz: Tatbestand erfüllt` | Karte + 3 Marker · Definition (3 Zeilen) · Haut · OLG Hamm · Vorsatz-Block | – |
| **D Rechtswidrigkeit** `rw`→`einv` | **Wortlautkarte § 228**, Block Rechtfertigungsgrund, Kasten Einverständnis | tabler:`writing-sign`, `hand-stop` | `Rechtswidrigkeit › Einwilligung, § 228 StGB` → `› Einwilligung als Rechtfertigungsgrund` → `› Abgrenzung: Einverständnis` | Karte + 3 Marker · Block · Einverständnis 4 Zeilen | – |
| **E 1. Dispositionsbefugnis** `disp`, `leben` | Haken Individualrechtsgut, Kreuz Leben (§ 216) | tabler:`user-check`, `heartbeat` | `Einwilligung › 1. Dispositionsbefugnis` | Frage · Unversehrtheit · Leben | – |
| **F 2. Einwilligungsfähigkeit** `faehig`→`alter` | **Zitatkarte BGH 1 StR 368/19 Rn. 57**, je-desto, zwei Kreuze | tabler:`bulb`, `scale`, `calendar` | `Einwilligung › 2. Einwilligungsfähigkeit` → `› … keine feste Altersgrenze` | Karte + Marker · je-desto · Altersgrenze · Geschäftsfähigkeit | – |
| **G Jugendliche, Marie** `f15`, `mf` | BGH Rn. 52, drei Haken für Marie | tabler:`user-check` | `› 2. Einwilligungsfähigkeit: Jugendliche` → `› … Marie (+)` | Block · Marie · drei Haken · Ergebnis | – |
| **H Streit** `streit`→`zivil` | zwei Kästen Literatur / BGH, offene Frage, vertretbare Lösung, Zivilrecht | tabler:`users`, `user-check`, `file-text`; fluent:`red-question-mark` | `Einwilligung › Streit: Minderjährige und Eltern` → `› Streit: eigene Einwilligung genügt (vertretbar)` → `› Zivilrecht: Vertrag, §§ 107 ff. BGB` | Literatur · BGH · offen · vertretbar · Zivilrecht | – |
| **I 3.–5.** `vorher`→`subj` | drei Punkte mit Unterzeilen | tabler:`writing-sign`, `eye`, `bulb`; Skizze | `› 3. Erklärung vor der Tat` → `› 4. keine Willensmängel` → `› 5. Handeln in Kenntnis der Einwilligung` | Punkt für Punkt, Haken am Wort | – |
| **J 6. § 228** `sitten`→`tat` | Kern, Maßstab, Todesgefahr, Subsumtion | tabler:`scale`, `heartbeat`; fluent:`cherry-blossom` | `› 6. keine Sittenwidrigkeit, § 228 StGB` → `› 6. Maßstab: Art und Gewicht, Gefahr` → `› 6. Tattoo: kein Sittenverstoß` | Zeile für Zeile, zwei Haken, Block | – |
| **K Ergebnis** `erg` | Block und Haken | tabler:`circle-check` | `Ergebnis · Herr Riedel ist nicht strafbar` | 2 | – |
| **L Abwandlung 1** `ab1`→`ab1c` | hellrote Tafel | tabler:`hourglass`, `user-x` | `Abwandlung 1 · Marie ist erst 14` → `Abwandlung 1 › Einwilligungsfähigkeit eher (−)` | 14 Jahre · Motiv · Folgen · Kreuz · rechtswidrig | – |
| **M Abwandlung 2** `ab2`→`ab2d` | hellrote Tafel; Herr Riedel lügt (Blase) | fluent:`lying-face`; tabler:`file-x` | `Abwandlung 2 · Täuschung` → `› Einwilligung unwirksam` → `› Herr Riedel strafbar, § 223 StGB` | zögert · Blase · falsch · nur deshalb · unwirksam · strafbar | – |
| **N Ausblick** `mutm` | hell-lila Tafel | tabler:`bed`, `zzz` | `Ausblick › mutmaßliche Einwilligung` | Zeilen · Bett · nicht befragbar | – |
| **O Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Einwilligung in der Rechtswidrigkeit` → `Klausurtipp · Schwerpunkt Einwilligungsfähigkeit` | Zeile für Zeile, Kreuz | – |
| **P Prüfschema** `sch`→`k3` | breite Karte, I.–III. mit 1.–6. | – | `Prüfschema` → `› I. Tatbestand` → `› II. Rechtswidrigkeit: Einwilligung` → `› II. 2. Einwilligungsfähigkeit` → `› II. 6. keine Sittenwidrigkeit, § 228 StGB` → `› III. Schuld` | 10 Aufbaustufen | – |
| **Q Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Sätze mit Marker | – | `Merksatz` | Satz für Satz, Marker | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026), Schwanzspitze außerhalb der Blase am Mund; eine Denkblase (Marie). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („17 Jahre“, „§ 223 Abs. 1 StGB“, „14 Jahre“); „nach einem Jahr“ bleibt als unbestimmter Artikel ausgeschrieben.
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung: Herr Riedel schiebt die Skizze auf den Tisch (A).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_062skizze_1` aus 464302, `szene_062unterschrift_1` aus 173081), Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT; Kirschblüte, Fragezeichen, Lügengesicht), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> An einem Samstagvormittag kommt Marie, 17 Jahre alt, in ein Tattoostudio. Seit Monaten wünscht sie sich ein großes Motiv auf dem Unterarm: einen Zweig mit Blüten. Tätowierer Herr Riedel zeigt ihr die Skizze und erklärt: Das Motiv bleibt für immer, das Stechen tut weh, und entfernen lässt es sich nur schwer.
>
> Ihre Eltern hat Marie nicht gefragt. Sie unterschreibt vor dem ersten Stich ein Einwilligungsformular. Herr Riedel sticht das Motiv fachgerecht nach der gebilligten Skizze.
>
> **Hat sich Herr Riedel wegen Körperverletzung strafbar gemacht?**
