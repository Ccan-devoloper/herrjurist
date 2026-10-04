# Folge 163 · Betrunken Auto fahren: a.l.i.c. im Straßenverkehr – BGHSt 42, 235 – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_163.py`](src/skript_163.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · StGB AT. Ablauf: fiktiver Einstieg (Leopold: Kneipe, erstes Bier, Nachtfahrt, Polizeikontrolle ohne Unfall; Variante „scharfe Bremsung“ nur als Text) → Frage → Sachverhalt → § 20 (Wortlautkarte, Koinzidenzprinzip, Zeitpunkte) → a.l.i.c. knapp (Ausnahmemodell, Tatbestandsmodell; Zeitstrahl, 27 s) → der echte Fall BGHSt 42, 235 (sachlich, ohne Figuren, ohne Unfallbild) → Kern: Tatbestandsmodell scheitert am „Führen“ (Zitatkarte Rn. 17), Verhalten statt Erfolg → Ausnahmemodell scheitert an § 20 und Art. 103 Abs. 2 GG (Wortlautkarte) → offen gelassen, § 222 ohne a.l.i.c. → § 323a (Wortlautkarte) → Lösung (§ 69) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:39,0 (5.766 vertonte Zeichen).

**Darstellung (Vorgabe Plan):** kein Unfall, kein Aufprall, keine Verletzten im Bild; Alkohol nur als neutrale Glas-Icons (Tabler `glass-full`/`glass`), keine Flaschen, kein Anstoßen, kein Trunkenheitsklischee (kein Schwanken, keine roten Nasen); die Fahrt ist eine ruhige Nachtfahrt; keine Marken. Der echte Fall erscheint nur als Tafel mit neutralen Icons (Hammer, Lieferwagen, Glas, Bett, Fahne, Lenkrad, Gerichtsgebäude); der Tod der zwei Grenzschutzbeamten wird in einem sachlichen Satz genannt, nicht gezeigt. Keine realen Personen als Figuren.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Leopold (LE), um 60 | fährt nach dem Kneipenabend heim | `standing/easing-2` (offenes Hemd Türkis `#7FD6D0` über schwarzem Shirt, Hose Grau `#6B6B78`), Kopf `No Hair 3` (Glatze, grauer Haarkranz `#BDB6AE`), Haut `#EBC2A0`, ohne Bart, ohne Brille. Mimiken `Smile` (froh, Kneipe; redet froh), `Calm`, `Serious` (redet), `Suspicious`, `Concerned\|Serious`, `Solemn`, `Tired` (nach Mitternacht, nach der Blutprobe) | `william` (Mann, älter) |
| Polizistin (PO), um 40 | Funktionsrolle ohne Namen, kontrolliert | `standing/easing-1` (Jacke Dunkelblau `#2F3D63`, Oberteil Hellblau `#8DB3F2`, uniformähnlich), Kopf `Long Bangs`, Haut `#D7A27C`. Mimiken `Calm`, `Serious` (redet, ernst) | `laura_ruhig` (Frau, mittel) |
| Freund (FR), Freundin (FN) | stehen mit Leopold am Stehtisch, sprechen nicht (Mund zu), nur A1 | `standing/walking-3` (schwarz, Kopf `Short 3`, Haut `#E2B48E`); `standing/robot_dance-2` (Hose Lila `#B8A9F5`, Kopf `Medium Bangs 2`, Haar `#A0522D`, Haut `#F2D0B5`); Mimik `Smile` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Freund und Freundin blicken nach rechts zum Tisch und zu Leopold, Leopold blickt nach links zu ihnen. A2: Leopold steht rechts neben seinem Auto und blickt nach rechts zur Polizistin, die nach links blickt. Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_163.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LE_froh_redet`, `LE_redet`, `PO_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): william und laura_ruhig – nicht die Stimmen der Vorfolge 161 (sabrina, marc). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Leopold – eindeutig deutsch, nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/preproduction` (Volltextsuche `grep -rlw` 04.10.2026; „Anton“ verworfen, weil im `willenserklaerung-test` vergeben). Nie im Genitiv gesprochen. Polizistin, Freund, Freundin sind Funktionsrollen (Namensschild mit der Rolle).
- Figuren-PNGs: `../peeps/op_163/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 159 (`robot_dance-3`, `crossed_arms-1`), 160 (`crossed_arms-1`, `sitting/closed_legs-2`, `resting-1`), 161 (`blazer-3`, `resting-1`, `crossed_arms-1`, `crossed_arms-2`) – hier `easing-2`, `easing-1`, `walking-3`, `robot_dance-2`; Oberteilfarbe Türkis (in 159–161 nicht verwendet), keine Polka Dots, keine Bärte, keine Prothesen-Posen. Gegenüber den Verkehrsfolgen 130 (Kontrollstelle am Ortsausgang bei Tag, Polizistin `blazer-4`), 140 (Kuppe) und 148 (Parkplatz bei Nacht): **Kneipe mit Stehtisch und Fenster** (neu) und **Ortseingang bei Nacht** mit Ortseingangsschild ohne Ortsnamen; die Polizistin hat Pose, Kopf und Hautton anders als in 130. **Nacht** in A2, weil der Fall laut Plan nachts nach dem Kneipenabend spielt; die Kneipe (A1) bleibt auf Cremegrund, die Nacht ist nur im Fenster zu sehen.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 In der Kneipe** `fall`→`mitt` (Cremegrund) | Stehtisch, Freund und Freundin ab 0,0 s, Fenster mit Nachthimmel und Mond, Wanduhr; Leopold kommt dazu, Auto vor der Tür (im Fenster), erstes Glas und Autoschlüssel, Leopold redet (Blase), zwei weitere Gläser, Uhr 20 → 23 → 24 Uhr | tabler `glass-full`, `glass`, `key`, `car`, `clock-hour-8/11/12`; `mond()`; `stehtisch()`, `fenster()` programmatisch | `Fall · In der Kneipe` (ab 0,0 s) → `· Das erste Bier` → `· Nach Mitternacht` | 10 | – |
| **A2 Heimfahrt und Kontrolle** `fahrt`→`var` (Nachtverlauf) | Landstraße nachts, Bäume, Mond; Leopolds Auto rollt ruhig heran und hält (3,6 s); Ortseingangsschild, Streifenwagen, Polizistin; Polizistin redet (Blase), Leopold steigt aus, redet (Blase); Blutprobe, Sachverständiger, Frage, Variante als Text | tabler `car`, `trees`, `tree`, `test-pipe`; fluent `police-car`; `strasse_nacht()`, `ortsschild()` | `Fall · Die Heimfahrt` → `· Die Polizeikontrolle` → `· Schuldunfähig bei Fahrtantritt` → `· Die Frage` → `· Variante` | 8 | Auto fährt heran und hält (`szene_163ankunft_1`, Freesound CC0 508901); kein Aufprall |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C § 20 StGB** `p20`→`z2` | **Wortlautkarte § 20 (vollständig)** mit fünf Markern; Zeile Steuerungsfähigkeit, Block Koinzidenzprinzip, zwei Kästen „1. Bier: schuldfähig / am Steuer: schuldunfähig“ mit Pfeil; Leopold | tabler `book`, `clock`, `glass-full`, `steering-wheel` | `A. § 316 StGB › III. Schuld › § 20 StGB` → `› Koinzidenzprinzip` | 10 | – |
| **D a.l.i.c. knapp** `alic`→`tatb` | Tafel mit Zeitstrahl Trinken → Fahrt; roter Pfeil zurück (Ausnahmemodell), grüner Balken (Tatbestandsmodell); Leopold | tabler `glass-full`, `car`, `help-circle`, `arrow-back-up`, `arrow-bar-to-left` | `… › actio libera in causa` → `› a.l.i.c.: Ausnahmemodell` → `› a.l.i.c.: Tatbestandsmodell` | 9 | – |
| **E Der echte Fall** `echt`→`lg` | Tafel ohne Figuren, Zeile für Zeile, LG-Block | tabler `gavel`, `truck-delivery`, `glass-full`, `bed`, `flag`, `steering-wheel`, `building-bank` | `Der echte Fall · BGHSt 42, 235` → `· Sachverhalt` → `· LG Osnabrück` | 9 | – |
| **F1 Tatbestandsmodell scheitert** `kern`→`trink` | **Zitatkarte Rn. 17** mit Marker; „Führen“, Anfahren, Motor; Kreuz „Sich-Betrinken: noch kein Führen“; Leopold | tabler `gavel`, `steering-wheel`, `car`, `glass-full` | `BGHSt 42, 235 › keine a.l.i.c. bei Verkehrsdelikten` → `› 1. Tatbestandsmodell: „Führen“` → `› 1. Sich-Betrinken ist kein Führen` | 7 | – |
| **F2 Verhalten statt Erfolg** `verh`→`fahrl` | Tafel, gelber Block „verhaltensgebundene oder eigenhändige Delikte“ (Lehre), Haken „auch fahrlässig“ | tabler `steering-wheel`, `user`, `alert-triangle` | `› 1. Verhalten statt Erfolg` → `› 1. eigenhändige Delikte` → `› 1. auch bei Fahrlässigkeit` | 7 | – |
| **G Ausnahmemodell scheitert** `ausn2`→`at` | Tafel, Kreuz Gewohnheitsrecht, **Wortlautkarte Art. 103 Abs. 2 GG** mit drei Markern, gelber Block | tabler `book`, `ban`, `scale` | `› 2. Ausnahmemodell: § 20 StGB` → `› 2. Art. 103 Abs. 2 GG` | 8 | – |
| **H Offen gelassen, § 222** `offen`→`erg222` | Tafel ohne Figuren (echter Fall), Haken, lila Block Schuldspruch | tabler `help-circle`, `glass-full`, `gavel` | `BGHSt 42, 235 › offen gelassen` → `› § 222 StGB ohne a.l.i.c.` → `› Schuldspruch` | 6 | – |
| **I Vollrausch** `p323`→`bgh2` | **Wortlautkarte § 323a Abs. 1, 2** mit elf Markern zum gesprochenen Merkmal; Blöcke Bedingung der Strafbarkeit und echter Fall; Leopold | tabler `book`, `glass-full`, `gavel`, `scale` | `B. § 323a StGB › Vollrausch` → `› Bedingung der Strafbarkeit` → `› Strafrahmen` → `› im echten Fall` | 11 | – |
| **J Lösung** `loes`→`l69` | Tafel mit Kreuz/Haken, Variante, Block § 69; Leopold und Polizistin | tabler `car`, `glass-full`, `alert-triangle`, `id` | `Lösung · Leopold` → `· § 316 StGB (−)` → `· § 323a StGB (+)` → `· Variante: § 315c StGB` → `· § 69 StGB` | 7 | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Prüfungsreihenfolge` | 5 | – |
| **L Prüfschema** `sch`→`s6` | breite Karte, A. § 316 / B. § 323a, grüner Kasten a.l.i.c. | – | `Prüfschema` → `› A. § 316 StGB` → `› A. III. a.l.i.c.` → `› B. § 323a StGB` | 9 | – |
| **M Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Marker | – | `Merksatz` | 6 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („§ 323a Abs. 2“, „1. Bier“, „2 Beamte“, „1 Jahr“, „22.8.1996“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Leopolds Auto rollt heran und hält (3,6 s).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT; Streifenwagen), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Stehtisch, Fenster, Straße und Ortsschild aus Grundformen (`folien_163.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Leopold verbringt einen Freitagabend mit Freunden in der Kneipe; sein Auto steht vor der Tür. Schon beim ersten Bier ist ihm klar, dass er nachher selbst nach Hause fahren wird: „Das geht schon.“ Er trinkt bewusst weiter; es bleibt nicht bei einem Bier.
>
> Nach Mitternacht fährt Leopold los. Am Ortseingang gerät er in eine Polizeikontrolle. Die Blutprobe zeigt, dass er stark betrunken war. Ein Sachverständiger stellt fest: Bei Fahrtantritt war Leopold schuldunfähig. Gefährdet wurde niemand.
>
> Variante: Unterwegs muss ein anderer Fahrer scharf bremsen; beinahe wäre es zum Zusammenstoß gekommen.
>
> **Ist Leopold nach § 316 StGB strafbar – und in der Variante nach § 315c StGB?**

Kein Fiktiv-Hinweis; beim echten Fall stehen Gericht, Datum und Aktenzeichen auf der Tafel.
