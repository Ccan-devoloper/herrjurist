# Folge 045 · Lösungsskizze Klausur: Zeitplan für die 5-Stunden-Examensklausur – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_045.py`](src/skript_045.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Klausurtechnik, **ohne Normprüfung**. Beispielfall nach dem Hook des Themenplans („Nach drei Stunden bist du erst bei der Hälfte …“): Erster Examenstag, Zivilrechtsklausur. Jakob schreibt ohne Plan sofort los, Johanna liest und markiert zuerst; um zwölf Uhr ist Jakob erst bei der Hälfte, Johanna schreibt schon am Schwerpunkt. Ablauf: Fall → Frage → Sachverhalt → Bearbeitungszeit (Landesrecht, Wortlautkarte § 13 Abs. 1 S. 1 JAG NRW, „in der Regel fünf Stunden“) → Zeitraster als Empfehlung (Tortendiagramm, Stück für Stück) → 1. Sachverhalt → 2. Fallfrage → 3. Lösungsskizze (sammeln, Probleme, Schwerpunkt, Stichworte; Gewichtung, Urteilsstil, Skizze von Johanna) → 4. Niederschrift / 5. Puffer → Zeitnot (Jakob) → Klausurtipp mit Zeitleiste → Zeitplan als Klausurschema mit Zeitleiste → Merksatz.
**Länge:** Hauptfilm 5:06,3 (4.140 gesprochene Zeichen, Regelbereich).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Johanna (JO), Mitte 20 | Examenskandidatin, plant die Klausur; **spricht nicht** (im Stimmenpool gibt es keine junge Frauenstimme; ihr Handeln erzählt die Erzählerin) | Pose `standing/shirt-3` (türkises Hemd, schwarze Hose), Kopf `Long Bangs`, Haut `#E8B98F`; Mimiken `Calm` (ruhig), `Serious` (liest), `Driven` (schreibt), `Suspicious` (denkt), `Smile` (froh) | – |
| Jakob (JA), Mitte 20 | Examenskandidat ohne Plan (Gegenfall) | Pose `standing/resting-2` (schwarzes Shirt, blaue Hose `#5A6E9A`), Kopf `Short 4`, ohne Bart, Haut `#D9A47E`; Mimiken `Calm`, `Cheeky|Smile` (zuversichtlich), `Driven` (hektisch), `Fear` (Schreck), `Tired` (müde), `Concerned|Serious` (redet: „Drei Stunden um …“), `Serious` (redet: „Also erst das Problem …“) | `niklas` (Mann, jung) |
| Aufsicht (AU), um 60, ohne Namen | Klausuraufsicht | Pose `standing/robot_dance-2` (schwarzer Pullover, Hose `#3D3D58`), Kopf `Gray Medium` (Haar `#D6D6D6`), Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet) | `elinor` (Frau, älter; streng) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Im Klausursaal blicken alle nach links (Kandidaten auf ihr Blatt, die Aufsicht zu den Tischen); in den Tafelfolien blicken alle zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `JA_redet`, `JA_plan`, `AU_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** (niklas, elinor; lisa und william nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Johanna, Jakob – nicht in der Liste vergebener Namen und in keiner früheren Folge verwendet (Suche über alle Skripte und Szenenpläne). Die Aufsicht bleibt ohne Namen. Kein Genitiv eines Namens im Sprechtext.
- Figuren-PNGs: `../peeps/op_045/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 044 Marktplatz mit Rathaus und Kaffeewagen, 043 Möbelhaus, 039 Elektronikmarkt und Staatsanwaltschaft. Hier erstmals ein **Klausursaal** (zwei Tische, Wanduhr 9 bzw. 12 Uhr, Aufgabenblätter, Stift, Textmarker). Posen `shirt-3`, `resting-2`, `robot_dance-2` kommen in 043/044 nicht vor. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Klausursaal, 9 Uhr** `fall`→`marker` | Boden, zwei Tische (Johanna links, Jakob Mitte), Aufsicht rechts, Wanduhr | tabler:`desk` (Holz), `clock-hour-9`, `file-text` (Aufgabenblätter, gleiten von der Aufsicht auf die Tische), `writing` (Stift), `highlight` (Gelb) | `Fall · Im Klausursaal, 9 Uhr` | Saal ab 0,0 s mit allen drei Figuren und Namen · „9 Uhr“ · „Erster Examenstag: Zivilrecht“ · Blätter gleiten · Aufsicht redet (Blase) · „fünf Stunden“ · Jakob blättert · schreibt sofort los · Johanna liest · Textmarker | Blatt auf dem Tisch (`szene_045papier_1`), Stift (`szene_045stift_1`) |
| **B Klausursaal, 12 Uhr / Frage** `zwoelf`→`frage2` | wie A, Uhr auf 12 | tabler:`clock-hour-12`, `files` (viele Seiten), `list-check` (Plan) | `Fall · 12 Uhr` → `Fall · Die Frage` | 12 Uhr · Aufsicht „Noch zwei Stunden.“ · Jakob „Drei Stunden um …“ · viele Seiten · Problem kommt erst noch (Schreck) · am Schwerpunkt · ihr Plan · Frage · Zeitplan und Lösungsskizze | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D Bearbeitungszeit** `land`→`eigen` | Tafel, Johanna und Aufsicht | tabler:`map-pin` (Rot), `book` (Blau), `hourglass` (Gelb), `book-2` (Grün) | `Bearbeitungszeit › Landesrecht` → `› Beispiel: § 13 Abs. 1 JAG NRW` → `› in der Regel fünf Stunden` | Landesrecht · Ausbildungsgesetz/Prüfungsordnung · Wortlautkarte § 13 I 1 JAG NRW mit zwei Markern · in der Regel fünf Stunden · eigene Prüfungsordnung | – |
| **E Zeitraster** `raster`→`zweit` | Tafel mit Tortendiagramm (300 min = Vollkreis, ab 12 Uhr im Uhrzeigersinn), Johanna | tabler:`clock`, `folders` (Akte) | `Zeitplan › Empfehlung aus Erfahrung` → `› ein Drittel planen, zwei Drittel schreiben` → `› im zweiten Examen` | Empfehlung, keine Pflicht · fünf Tortenstücke mit Legende nacheinander · ein Drittel / zwei Drittel · Verhältnis zählt · 2. Examen: Akte | – |
| **F 1. Sachverhalt** `s1`→`angabe` | Tafel, Johanna | tabler:`file-text`, `highlight`, `message-2`, `list-check` | `1. Sachverhalt lesen und markieren` → `1. Sachverhalt › Rechtsansichten der Beteiligten` | zweimal lesen · ohne Stift · Personen / Daten / Geldbeträge · Rechtsansichten · fast jede Angabe | – |
| **G 2. Fallfrage** `s2`→`aufbau` | Tafel, Johanna | tabler:`file-description`, `zoom-question`, `hand-stop`, `list-numbers` | `2. Fallfrage und Bearbeitervermerk` → `2. Fallfrage › der Aufbau folgt der Frage` | Wer will was von wem? · nicht prüfen · Ansprüche / Strafbarkeit / Erfolgsaussichten einer Klage | – |
| **H 3. Lösungsskizze** `s3`→`stich` | Tafel, Johanna | tabler:`list`, `alert-triangle`, `star`, `notes` | `3. Lösungsskizze › Anspruchsgrundlagen sammeln` → `› Probleme markieren` → `› Schwerpunkt setzen` | aus Vertrag / Delikt / Bereicherung · Ring (Problem) · Schwerpunkt · Stichworte mit Ergebnis und Argument | – |
| **I 3. Gewichtung** `gewicht`→`jo5` | Tafel, Johanna | tabler:`clock`, `gavel` (Holz), `list-numbers`, `hourglass` | `3. Lösungsskizze › Gewichtung` → `› Unproblematisches im Urteilsstil` → `› die Skizze von Johanna` | eine Zeit je Punkt · Urteilsstil · drei gleiche Blöcke · zwei kurze, ein langer Block · 90 Minuten | – |
| **J 4./5.** `s4`→`puffer` | Tafel, Johanna | tabler:`writing`, `hourglass` (Rot), `eye` | `4. Niederschrift` → `5. Puffer` | Niederschrift · Reihenfolge · Puffer · noch einmal lesen | – |
| **K Zeitnot** `fehler`→`not3` | Tafel, Jakob | tabler:`files`, `alarm` (Rot), `writing` | `Zeitnot › Jakob ohne Skizze` → `› Schwerpunkte zuerst` → `› nie leer abgeben` | alles gleich ausführlich (Kreuz) · ohne Skizze · Zeit knapp · 1.–3. · Jakob redet (Blase) · nie leer abgeben | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet), Zeitleiste 9–14 Uhr | Warnsymbol (Streamline Freehand) | `Klausurtipp · Uhrzeiten an die Skizze` | Zeile · Zeitleiste · Skizze fertig 10:40 · Niederschrift fertig 13:40 · Satz | – |
| **M Klausurschema** `sch`→`k5` | breite Karte, Zeitplan I.–V. und farbige Zeitleiste (Farben wie die Torte) | – | `Klausurschema · Zeitplan` | Titel · I. · II. · III. · Unterpunkte · IV. · V. (jeweils mit Zeitleistenstück) | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Aufgabenblätter gleiten auf die Tische).
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0, über die API neu geladen), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Erster Examenstag, Klausur im Zivilrecht von 9 bis 14 Uhr. Die Aufsicht: „Die Bearbeitungszeit beginnt jetzt. Sie haben fünf Stunden.“ Jakob blättert kurz durch den Sachverhalt und schreibt sofort los. Johanna liest erst einmal, mit dem Textmarker in der Hand.
>
> Um 12 Uhr ist Jakob erst bei der Hälfte; das Problem des Falls kommt erst noch. Johanna schreibt nach ihrem Plan schon am Schwerpunkt.
>
> **Wie teilst du die fünf Stunden ein?**
