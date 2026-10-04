# Folge 165 · Analogieverbot Strafrecht: Art. 103 II GG einfach erklärt – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_165.py`](src/skript_165.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Auslegung, Themenplan-Format „Methodik“ (ein Beispielfall trägt den Film). Leitbeispiel nach dem Plan-Hook („Die Tat ist verwerflich, aber kein Paragraf passt genau – Pech für den Staat?“): Wieland bindet am öffentlichen Steg das Tretboot von Hartwin los, fährt eine Stunde über den See und bringt es unbeschädigt zurück. Kein Diebstahl (bloße Gebrauchsanmaßung), § 248b StGB erfasst nur Kraftfahrzeuge und Fahrräder. **Ruhige, gewaltfreie Darstellung**, kein Streit, keine Drohgebärde.

Ablauf: Fall am See → Sachverhalt → Diebstahl? (Wortlautkarte § 242 Abs. 1) → § 248b (Wortlautkarte Abs. 1/4) → Art. 103 Abs. 2 GG und § 1 StGB (Wortlautkarten), nullum crimen, nulla poena sine lege → zwei Zwecke → vier Gewährleistungen (Überblick) → **je eine Tafel in eigener Farbe und gleicher Struktur: 1. lex scripta Blau, 2. lex certa Gelb, 3. lex stricta Lila (nur Verweis auf 162/148), 4. lex praevia Grün (Wortlautkarte § 2 Abs. 1)** → **Schwerpunkt Bestimmtheit:** Untreue-Beschluss (Zitatkarte Rn. 73), Präzisierungsgebot (Zitatkarte Rn. 80), Verschleifungsverbot, gescheiterte Verurteilung, Sitzblockaden-Beschluss (Wortlautkarte § 240 Abs. 1, Auszug) → nur zulasten: Analogie zugunsten (BGH § 306e analog) → § 3 OWiG (Wortlautkarte) → Lösung am See → Klausurtipp (Lexi) → Prüfraster → Merksatz (Lexi). Hauptfilm 6:10,2 (5.145 Skriptzeichen; Begründung der Länge in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Wieland (WI), um 30 | nimmt das Tretboot, bringt es zurück | `standing/walking-1` (T-Shirt Türkis `#7FD6D0`, schwarze Hose, weiße Schuhe), Kopf `Short 3` (Haar `#6B4A2E`), Haut `#EDC3A1`; im Boot `sitting/mid-2` in derselben Kleidung (Reihe -2: farbiges Oberteil, schwarze Hose), Beine vom Rumpf verdeckt; Mimiken `Calm`, `Smile` (redet), `Smile Big\|Smile`, `Cheeky\|Smile`, `Suspicious`, `Concerned\|Serious` | `niklas` (Mann, jung) |
| Hartwin (HA), um 65 | Eigentümer des Tretboots | `standing/crossed_arms-2` (Pullover Schwarz, Hose Braun `#6B5640`, Arme verschränkt), Kopf `No Hair 2`, Brille `Glasses 2`, Haut `#E6B796`, kein Bart; Mimiken `Calm`, `Serious` (redet), `Concerned\|Serious` (fragt), `Suspicious`, `Solemn`, `Tired` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung** (Kontaktbild `out/besetzung_165.png`, im Master): Grundansicht gespiegelt = blickt nach links, `_r` = nach rechts. See: Wieland steht auf dem Steg und blickt zuerst nach links zum Boot, nach der Rückkehr nach rechts zu Hartwin; Hartwin am Ufer blickt nach links zu Wieland. Im Boot blickt Wieland in Fahrtrichtung (hinaus nach links, zurück nach rechts; Boot gespiegelt). Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `WI_redet`, `HA_redet`, `HA_fragt` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: `niklas` (Wieland), `helmut` (Hartwin); `ela_froh` (keine ernste Rolle nötig) und `julia` nicht besetzt. 164 nutzte ebenfalls niklas/helmut – bei zwei Männerrollen und diesem Pool unvermeidbar (163: william/laura_ruhig, 162: lucy/christian/hilde).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Textdatei unter `youtube/` (Suche `grep -rlw` über .md/.py/.json/.csv/.txt/.js/.html, 04.10.2026: Wieland 0, Hartwin 0 Treffer; verworfen: Hannes 13, Jannik 20, Ole 3, Gerold 1, Eckart 1, Volkert (V/F-Lesart), Tjark). Kein Genitiv eines Namens im Sprechtext („das Tretboot von Hartwin“).
- Präfixe `WI_`/`WB_`/`HA_` (nie `ER_`). Figuren-PNGs: `../peeps/op_165/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 162–164 verglichen): 162 `easing-1`, `blazer-4`, `sitting/closed_legs-1`; 163 `easing-2`, `easing-1`, `walking-3`, `robot_dance-2`; 164 `shirt-3`, `blazer-4`. 165: `walking-1`, `sitting/mid-2`, `crossed_arms-2` – nicht in 162–164; keine Polka Dots, keine Bärte, keine Prothesen-Posen. Kleidung Türkis/Schwarz und Schwarz/Braun kommt in 162–164 so nicht vor (164: Blau, Grau; 163: Türkis-Jacke mit grauer Hose bei anderer Pose und Glatze). Schauplatz neu: **See mit Holzsteg, Tretboot und Uferböschung** (162 Hof/Gericht, 163 Straße, 164 Büro/Tafel). Der See kehrt in H zurück, weil der Fall dort gelöst wird. Cremegrund durchgehend, Tageslicht (Sommerabend als Icon `sunset`).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A See** `fall`–`frage2` | ab 0,0 s vollständig: Wasser, Steg mit Poller, festgemachtes Tretboot mit Seil, Wieland auf dem Steg mit Schild, Pille „Ein Sommerabend am See“; Pillen „Tretboot von Hartwin“, „nur mit einem Seil festgebunden“ (Ring um Seil/Poller); bei „bindet … los“ Seil lose, Wieland frech; bei „fährt“ Boot mit Wieland nach links über den See (Bewegung bis „See“); Pille „eine Stunde über den See, ohne zu fragen“; bei „bringt“ Rückfahrt nach rechts, Anlegen bei „zurück“; „wieder festgebunden“, „Kaputt ist nichts.“; Hartwin am Ufer (Blase „Das ist doch Diebstahl! / Dafür gehört er bestraft!“), Blase Wieland „Ich habe es doch / zurückgebracht.“; Fragepillen | tabler:`sunset` (Gelb), `trees` (Grün); See, Ufer, Steg, Poller, Seil, Tretboot (Rumpf Gelb/Rot, Radkasten Blau, Lehne) programmatisch | `Fall · Ein Sommerabend am See` → `· Das Tretboot von Hartwin` → `· Wieland fährt los, ohne zu fragen` → `· Wieland bringt das Boot zurück` → `· „Das ist doch Diebstahl!“` → `Die Frage · …` | Treten/Plätschern während der Fahrt (`szene_165treten_1`), Rumpf stößt beim Anlegen an den Steg (`szene_165steg_1`) |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ≈ 10 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C1 Diebstahl?** `dieb`, `rueck` | Wortlautkarte § 242 Abs. 1 (Auszug, Marker „Absicht“, „zuzueignen“), Zeilen Gebrauchsanmaßung (BGH 3 StR 484/14 Rn. 6), Kreuz „kein Diebstahl“ | tabler:`hand-grab`, `arrow-back-up`, `ban` | `Welcher Paragraf? · Diebstahl, § 242 StGB` → … | – |
| **C2 § 248b** `p248`, `kein` | Wortlautkarte § 248b Abs. 1 und 4 (Marker „Kraftfahrzeug“, „Fahrrad“, „Maschinenkraft“), Kreuze „kein Motor: kein Kraftfahrzeug“, „kein Fahrrad, auch wenn man tritt“; Tretboot als Requisit | tabler:`car`, `bike`; Tretboot programmatisch | `Welcher Paragraf? · § 248b StGB …` → `› Tretboot: kein Kraftfahrzeug` → `› kein Fahrrad` | – |
| **D1 Gesetzlichkeitsprinzip** `a103`–`latein` | Titel „Warum hilft das Gericht nicht nach?“, Wortlautkarten Art. 103 Abs. 2 GG und § 1 StGB, Haken „wortgleich“, Block „nullum crimen, nulla poena sine lege“, Übersetzung | tabler:`help`, `book`, `book-2`, `scale` | `Gesetzlichkeitsprinzip · …` | – |
| **D2 Zwei Zwecke** `zweck`–`z2` | zwei Blöcke (Gesetzgeber entscheidet / vorhersehbar), Rn. 69 f. | tabler:`gavel`, `building-bank`, `eye` | `Gesetzlichkeitsprinzip › …` | – |
| **E0 Überblick** `vier`–`vd` | vier Farbblöcke 1. geschrieben (Blau), 2. bestimmt (Gelb), 3. streng angewendet (Lila), 4. vor der Tat (Grün) zum Wort | tabler:`list-numbers` | `Vier Gewährleistungen › …` | – |
| **E1–E4** `sa`–`pc` | je eine Tafel in der Farbe der Gewährleistung, **gleiche Struktur**: Titel „n. lex …“ + Pille „Gewährleistung n“, Kernzeile (Begriff, Adressat), Inhalt (Zeile bzw. Wortlautkarte § 2 Abs. 1), farbiger Block (Fall/Beispiel/Verweis), Fundstelle | tabler:`writing`, `ban`, `heart-handshake`, `focus`, `building-bank`, `help`, `gavel`, `player-play`, `history`, `calendar-time`, `calendar-x` | `1. lex scripta · …` … `4. lex praevia › neues Gesetz zu spät` | – |
| **F1 Untreue** `best`–`gk` | Untreue-Beschluss, § 266 sehr weit (Rn. 89), Haken „noch vereinbar“ (Leitsatz 1, Rn. 84), Zitatkarte Rn. 73 (Marker „Generalklauseln“) | tabler:`focus`, `arrows-diagonal-minimize`, `circle-check` | `Bestimmtheit · …` | – |
| **F2 Pflichten** `pflicht`–`vs2` | Zitatkarte Rn. 80 (Marker „Präzisierung“, „Präzisierungsgebot“), Zeilen Verschleifung, roter Block „Verschleifung: verboten“ (Rn. 78) | tabler:`gavel`, `zoom-in`, `arrows-join` | `Bestimmtheit › Präzisierungsgebot` → … | – |
| **F3 Verurteilung** `nachteil`–`aufh` | Blöcke „Vermögensnachteil“ (zum Wort) und „Pflichtwidrigkeit“, Pfeil „gefolgert“, Kreuz „nicht eigenständig ermittelt“, grüner Block „Das Bundesverfassungsgericht hob das Urteil auf.“ (Rn. 152, 154, 158) | tabler:`coin-euro`, `gavel` | `Bestimmtheit › …` | – |
| **F4 Sitzblockaden** `sitz`–`vst` | Wortlautkarte § 240 Abs. 1 (Auszug, Marker „Gewalt“), „vergeistigt …“ (S. 15, 17), Kreuz „nicht mehr sicher vorhersehbar“ (S. 18), Haken „das Gesetz: bestimmt genug“ (S. 13), roter Block „die Auslegung: Verstoß gegen Art. 103 Abs. 2 GG“ (S. 1, 14; 5 : 3, S. 16) | tabler:`road`, `ghost`, `help`, `gavel` | `Bestimmtheit · Sitzblockaden-Beschluss 1995` → … | – |
| **G1 Nur zulasten** `zug`–`zbsp` | Haken „Analogie zugunsten des Täters: nicht verboten“ (BGH 1 StR 118/20 Rn. 21), Beispielblock § 306e analog (Leitsatz, Rn. 19 f.) | tabler:`shield-check`, `circle-check`, `lifebuoy` | `Nur zulasten · …` | – |
| **G2 OWiG** `owi`, `owi2` | Wortlautkarte § 3 OWiG (Marker „gesetzlich bestimmt“, „bevor“) | tabler:`receipt`, `book` | `Nur zulasten › § 3 OWiG` | – |
| **H Lösung** `loes`–`lg` | See wie A (Boot festgemacht); Pillen „Diebstahl scheidet aus“, „§ 248b StGB erfasst kein Tretboot“, „Wieland bleibt straflos“; Blase Hartwin „Das ist also / einfach erlaubt?“; Pillen „Strafbar ist es jedenfalls nicht. Pech für den Staat.“, „Strafbarkeitslücken schließt nur der Gesetzgeber, / und zwar nur für künftige Taten.“, Fundstelle Rn. 77 | wie A | `Lösung · …` → `Ergebnis · Wieland bleibt straflos` → … | – |
| **I Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; Block „üblich etwa: …“ | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **J Prüfraster** `sch`–`k5` | breite Karte, 1.–4. mit Farbpunkten der Gewährleistungen (Reihenfolge wie gesprochen: scripta, praevia, certa, stricta), Block „Nur wenn alles zutrifft, darf bestraft werden.“ | – | `Prüfraster › …` | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt, fünf Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur in A (Fahrt hinaus ≈ 2 s, Rückfahrt ≈ 1,4 s).
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen.
**Lateinische Begriffe:** auf Tafeln in normaler Schreibung (lex certa, lex praevia, nulla poena); gesprochen mit deutscher Juristenaussprache über Aussprachehilfen in `src/vertonen_165.py` („zerta“, „präwia“, „pöna“).
**Geräusche:** zwei Handlungsgeräusche, Freesound CC0 (IDs 378045, 637206) über die API ohne Schlüssel, eigene Namen `sfx3/szene_165treten_1.wav`, `sfx3/szene_165steg_1.wav`; Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hartwin hat sein Tretboot am öffentlichen Steg eines Sees mit einem Seil festgebunden. Ohne zu fragen, bindet Wieland es los und fährt eine Stunde damit über den See. Er will es von Anfang an zurückbringen.
>
> Danach bindet er das Boot wieder am Steg fest. Beschädigt ist nichts.
>
> Hartwin meint: „Das ist doch Diebstahl! Dafür gehört er bestraft!“
>
> **Hat Wieland sich strafbar gemacht?**
