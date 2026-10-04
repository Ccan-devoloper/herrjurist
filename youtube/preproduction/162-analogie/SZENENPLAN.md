# Folge 162 · Analogie Jura: Regelungslücke und vergleichbare Interessenlage – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_162.py`](src/skript_162.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Auslegung, Themenplan-Format „Methodik“ (ein Beispielfall trägt den Film). Leitbeispiel nach dem Plan-Hook („Das Gesetz regelt den Fall nicht – darf der Richter trotzdem entscheiden?“): Ilona wird von ihrem Nachbarn Bertold seit Wochen immer wieder vor anderen Nachbarn im Hof beleidigt und klagt auf Unterlassung; vor Gericht beruft sich Bertold auf den Wortlaut des § 1004 BGB. **Ruhige Darstellung:** keine Beleidigungsworte, nur die Text-Pille „beleidigende Äußerungen“ mit einem neutralen Icon; keine Drohgebärde, keine Karikatur.

Ablauf: Fall im Hof → Gerichtssaal (Frage) → Sachverhalt → Wortlautkarte § 1004 Abs. 1 → Wortlautkarte § 823 Abs. 1 → Begriff der Analogie → BGH-Formel (Zitatkarte IX ZR 91/24 Rn. 14) → drei Schritte mit **je eigener Farbe: 1. Regelungslücke Gelb, 2. planwidrig Lila, 3. vergleichbare Interessenlage Grün** (Tafelfläche, Pille „Schritt n“, Ergebnisblock, Schema-Punkte) → quasinegatorischer Unterlassungsanspruch (Verweis 142) → Einzel- und Gesamtanalogie → Umkehrschluss und teleologische Reduktion (Verweis 159) → Grenzen (Wortlautkarte Art. 103 Abs. 2 GG, Verweis 148; Vorbehalt des Gesetzes) → Lösung im Gerichtssaal → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 6:29,7 (5.564 vertonte Zeichen; Begründung der Länge in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ilona (IL), um 30 | wird beleidigt, Klägerin | `standing/easing-1` (offenes Hemd Pink `#F6A5C0`, Oberteil Weiß, schwarze Hose), Kopf `Long Bangs` (schwarzes Haar), Haut `#F1C9A5`; Mimiken `Calm`, `Serious` (redet), `Concerned\|Serious`, `Suspicious`, `Smile`, `Smile Big\|Smile`, `Tired` | `lucy` (Frau, jung) |
| Bertold (BE), um 45 | Nachbar, Beklagter | `standing/blazer-4` (Sakko Ocker `#C9A27A`, Oberteil Weiß, schwarze Hose), Kopf `Short 5`, Haut `#E2B48E`, kein Bart; `Calm`, `Serious` (redet), `Contempt`, `Suspicious`, `Concerned\|Serious`, `Solemn` | `christian` (Mann, mittel) |
| Richterin (RI), um 60, ohne Namen | Gericht | `sitting/closed_legs-1` (Jacke Schwarz `#2B2B33` als Robe, gestreiftes Oberteil Weiß), Kopf `Gray Bun`, Brille `Glasses 4`, Haut `#EFC6A6`; sitzt hinter dem Richtertisch, der sie ab der Schulter verdeckt; `Calm`, `Serious` (redet), `Suspicious`, `Smile` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung** (Kontaktbild `out/besetzung_162.png`, im Master): Grundansicht gespiegelt = blickt nach links, `_r` = nach rechts. Hof: Bertold vor der Haustür blickt nach rechts zu Ilona, Ilona nach links zu ihm. Gerichtssaal: Ilona links blickt nach rechts, Bertold rechts nach links; die Richterin blickt in A2 nach rechts (zu Bertold, ihre Blase rechts), in J nach links (zu Ilona, Blase links). Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `IL_redet`, `BE_redet`, `RI_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool:** `lucy` (Ilona), `christian` (Bertold), `hilde` (Richterin); `stephan` nicht besetzt (also kein Paar stephan/christian). Der Pool hat nur vier Stimmen; `lucy` und `hilde` sprachen auch in 160 (unvermeidbar), `christian` statt `stephan` aus 160.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Textdatei unter `youtube/` (Suche `grep -rlw` über .md/.py/.json/.csv/.txt/.js/.html, 04.10.2026: Ilona 0, Bertold 0 Treffer; verworfen: Greta 44, Gerhard 2, Hubert 4, Leonie 3, Jule 1). Kein Genitiv eines Namens im Sprechtext. Die Richterin bleibt ohne Namen (Schild „Richterin“).
- Präfixe `IL_`/`BE_`/`RI_` (nie `ER_`). Figuren-PNGs: `../peeps/op_162/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 159–161 verglichen): 159 `robot_dance-3`, `crossed_arms-1`; 160 `crossed_arms-1`, `sitting/closed_legs-2`, `resting-1`; 161 `blazer-3`, `resting-1`, `crossed_arms-1`, `crossed_arms-2`. 162: `easing-1`, `blazer-4`, `sitting/closed_legs-1` – nicht in 159–161; keine Polka Dots, keine Prothesen-Posen (`shirt-1/-2`, `blazer-1/-2` verworfen), keine Bärte; `pointing_finger-1` und `walking-3` verworfen (Kleidung nicht umfärbbar). Kleidung Pink/Ocker/Schwarz kommt in 159–161 so nicht vor. Schauplätze neu: **Hof vor einem Mehrfamilienhaus mit Haustür** und **Gerichtssaal mit Richtertisch** (159 Radweg/Seminar, 160 Buchhandlung, 161 Haustür/Park/Flohmarkt). Der Gerichtssaal kehrt in J wieder, weil die Geschichte zum Prozess zurückkehrt. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Hof** `fall`–`klage` | ab 0,0 s Mehrfamilienhaus (programmatisch: Fassade, Dach, Fenster, Haustür), Ilona mit Schild; Bertold kommt aus der Tür (Tür geht auf) beim Wort „Nachbar“; Pille „beleidigende Äußerungen“ beim Wort „beleidigt“, Ilona besorgt, Bertold verächtlich; Pillen „seit Wochen, immer wieder“, „vor anderen Nachbarn im Hof“; Blase Ilona „Bertold, ich will, / dass das aufhört.“; Pille „Klage auf Unterlassung“ | tabler:`message-x` (Hellrot), `file-text`; Haus, Tür programmatisch | `Fall · Im Hof des Mehrfamilienhauses` (ab 0,0 s) → `· Beleidigungen vor den Nachbarn` → `· Ilona will, dass es aufhört` → `· Klage auf Unterlassung` | Haustür öffnet (`szene_162tuer_1`) |
| **A2 Gericht** `gericht`–`ri1` | Richtertisch (programmatisch) mit Richterhammer, Richterin dahinter; Ilona links, Bertold rechts; Blase Bertold „§ 1004 schützt doch / nur das Eigentum!“; Frage-Pillen; Blase Richterin „Dann prüfen wir / eine Analogie.“ | tabler:`gavel` (Holz) | `Fall · Vor Gericht` → `· „§ 1004 schützt nur das Eigentum“` → `Die Frage · …` | – |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C1 § 1004** `w1004`, `nureig` | Wortlautkarte § 1004 Abs. 1 (Marker „Sind weitere Beeinträchtigungen“, „Eigentümer“, „Unterlassung“, dann „Eigentum“); Kreuz „die Ehre ist kein Eigentum“ | tabler:`home`, `user-shield` | `Das Problem · § 1004 Abs. 1 S. 2 BGB` → `› Wortlaut: nur das Eigentum` | – |
| **C2 § 823** `p823`–`kunft` | Wortlautkarte § 823 Abs. 1 (Marker „sonstiges“, „Ersatz des daraus entstehenden Schadens“); Haken APR/Ehre; Kreuze „nur Schadensersatz“, „keine Unterlassung künftiger Beleidigungen“ | tabler:`user-shield`, `coin-euro`, `calendar-event` | `Das Problem › § 823 Abs. 1 BGB …` | – |
| **C3 Begriff** `ana`, `erst` | Diagramm geregelt (§ 1004, Eigentum) → „entsprechend“ → ungeregelt (Ehre); Block „erst, wenn die Auslegung ausgeschöpft ist“ | tabler:`arrows-right`, `book` | `Analogie · …` → `› erst nach der Auslegung` | – |
| **D1 BGH-Formel** `bgh`–`abw` | Zitatkarte BGH IX ZR 91/24 Rn. 14 mit Markern („planwidrige Regelungslücke“, „vergleichbar“, „gleichen … Abwägungsergebnis“) | tabler:`gavel`, `puzzle`, `scale` | `Voraussetzungen · die BGH-Formel` → … | – |
| **D2 drei Schritte** `drei`–`s3` | drei Farbblöcke Gelb/Lila/Grün zum Wort | tabler:`list-numbers`, `puzzle`, `eye-off`, `scale` | `Voraussetzungen › 1. … 2. … 3.` | – |
| **E1 1. Regelungslücke** (Gelb) `l1`–`l3` | Definition, „Bei Ilona:“ zwei Kreuze, Block „Regelungslücke (+)“ | tabler:`puzzle`, `circle-check` | `1. Regelungslücke · …` → `(+)` | – |
| **E2a 2. planwidrig** (Lila) `pw1`–`pw4` | Definition (IX ZR 91/24 Rn. 15), Kreuz „bewusst ausgespart“, Historie/Zweck, Beispiel Kilometerleasing (VIII ZR 36/20) | tabler:`eye-off`, `ban`, `history`, `car` | `2. planwidrig · …` | – |
| **E2b Systematik** (Lila) `pwf`–`ehre` | vier Kacheln: § 12 Name, § 862 Besitz, § 1004 Eigentum („Unterlassung“), Ehre „Unterlassung?“; „schutzlos gewollt? nicht erkennbar“; Block „planwidrige Lücke (+)“ | tabler:`id`, `key`, `home`, `user-shield`, `circle-check` | `2. planwidrig › …` → `2. planwidrig (+)` | – |
| **E3 3. vergleichbar** (Grün) `vi1`–`vi3` | Wertung (VIII ZR 36/20 Rn. 41), Zitatkarte I ZR 12/23 Rn. 16 (Marker „nicht zuzumuten“, „tatenlos“), Haken, Block „(+)“ | tabler:`scale`, `hand-stop`, `circle-check` | `3. vergleichbare Interessenlage · …` → `(+)` | – |
| **F Rechtsprechung** `rspr`–`f142` | § 1004 entsprechend für alle Rechtsgüter des § 823 (V ZR 110/14 Rn. 20), Block „quasinegatorischer Unterlassungsanspruch“, Anspruchsgrundlage, Verweis Folge 142 | tabler:`gavel`, `hand-stop`, `user-shield`, `home` | `Rechtsprechung · …` | – |
| **G Arten** `einzel`–`gbsp` | zwei Blöcke Einzel-/Gesamtanalogie; §§ 604 Abs. 3 + 671 Abs. 1 → „unentgeltliche Versorgungsvereinbarung: jederzeit kündbar“ (V ZR 56/12 Rn. 17) | tabler:`file-text`, `files`, `gift` | `Arten der Analogie · …` | – |
| **H Gegenstücke** `gegen`–`tr` | Umkehrschluss („argumentum e contrario“ als Randnotiz), teleologische Reduktion (BVerwG 6 C 17/09 Rn. 30), Verweis Folge 159 | tabler:`arrows-exchange`, `arrow-back-up`, `scissors` | `Gegenstücke · …` | – |
| **I Grenzen** `grenz`–`oer2` | Wortlautkarte Art. 103 Abs. 2 GG (Marker „gesetzlich bestimmt“), Block „Verbot strafbegründender Analogie“, Kreuz „nie zulasten des Täters“, Verweis Folge 148; Öffentliches Recht: Vorbehalt des Gesetzes | tabler:`barrier-block`, `book`, `ban`, `building-bank` | `Grenzen · …` | – |
| **J Lösung** `loes`–`erg` | Gerichtssaal wie A2; Pillen „Lücke (+) · planwidrig (+) · vergleichbar (+)“, „Die Richterin darf die Lücke schließen.“, „Ehre verletzt …“, „Wiederholungsgefahr vermutet“; Blase Richterin „Der Beklagte muss die beleidigenden / Äußerungen künftig unterlassen.“ mit Hammerschlag; Pille „Unterlassungsanspruch analog § 1004 BGB“ | tabler:`gavel` | `Lösung · …` → `Ergebnis · Unterlassungsanspruch analog § 1004 BGB` | Richterhammer (`szene_162hammer_1`) |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **L Prüfschema** `sch`–`k4` | breite Karte, I.–IV., Farbpunkte der drei Schritte | – | `Prüfschema › …` | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; keine Bewegung außer Einblendungen.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („§ 1004“).
**Geräusche:** zwei Handlungsgeräusche, Freesound CC0 (IDs 704609, 618138) über die API ohne Schlüssel, eigene Namen `sfx3/szene_162tuer_1.wav`, `sfx3/szene_162hammer_1.wav`; Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ilona wohnt in einem Mehrfamilienhaus. Ihr Nachbar Bertold beleidigt sie seit Wochen immer wieder, auch vor anderen Nachbarn im Hof. Einen sachlichen Anlass gibt es nicht.
>
> Ilona verlangt, dass er das künftig unterlässt, und klagt auf Unterlassung.
>
> Bertold hält dagegen: § 1004 BGB schütze nur das Eigentum, nicht die Ehre.
>
> **Hat Ilona einen Anspruch darauf, dass Bertold weitere Beleidigungen unterlässt?**
