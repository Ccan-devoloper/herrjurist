# Folge 136 · GoA Schema: Wann bekommt der Helfer seine Kosten? (§ 683 BGB) – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_136.py`](src/skript_136.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/GoA, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Du löschst den brennenden Mülleimer deines Nachbarn – und ruinierst dabei deine teure Jacke“): Frau Huber ist zwei Wochen verreist. Am dritten Tag brennt die Mülltonne vor ihrem Haus, das Feuer droht auf ihren Carport überzugreifen. Ihr Nachbar Harald hat keinen Feuerlöscher zur Hand und erstickt die Flammen mit seiner Jacke; niemand ist verletzt, die Jacke (noch 250 € wert) ist ruiniert. Harald verlangt 250 €; Frau Huber: „Um Hilfe gebeten habe ich Sie nicht.“

Ablauf: Fall (Abreise, Feuer, Löschen, Rückkehr) → Frage → Sachverhalt → Anspruchsgrundlage und fünf Prüfungspunkte → 1. Geschäftsbesorgung → 2. fremdes Geschäft (Vermutung, auch-fremdes Geschäft) → 3. ohne Auftrag (Wortlaut § 677) → 4. Berechtigung (Wortlaut § 683 S. 1: Interesse, wirklicher/mutmaßlicher Wille, Zeitpunkt) → §§ 679, 680 kurz → 5. Rechtsfolge (Wortlaut § 670, Erforderlichkeit) → Jacke als Aufwendung / risikotypischer Begleitschaden, Höhe → Abgrenzung § 684 S. 1 (Wortlaut, Verweis Bereicherungsrecht) → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:28,4 (4.748 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Harald (HJ/HA), um 45 | Nachbar, Geschäftsführer | mit Jacke `standing/blazer-3` (Jacke Blau `#5B8FD9`, schwarzes Oberteil, Hose Anthrazit `#3A3F47`, weiße Schuhe), nach dem Löschen ohne Jacke `standing/robot_dance-2` (dasselbe schwarze Oberteil, dieselbe Hose) – der Wechsel ist die Handlung; Kopf `Short 1`, Haut `#E6B08A`, kein Bart, keine Brille; Mimiken `Calm`, `Concerned|Serious` (Sorge; redet in A2), `Driven`, `Smile` (redet in A4), `Smile Big|Smile`, `Suspicious`, `Awe`, `Serious` | `marc` (Mann, mittel) |
| Frau Huber (HU), um 55 | Nachbarin, Geschäftsherrin | `standing/pointing_finger-1` (schwarze Kleidung der Pose, erhobener Zeigefinger), Kopf `Medium 3`, Brille `Glasses 3`, Haut `#F2D2B6`; Mimiken `Calm`, `Smile Big|Smile`, `Serious` (redet), `Suspicious`, `Awe`, `Smile` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste und per `grep -rlw` im `youtube/`-Ordner nicht als Figur vergeben: Harald, Huber („Karl“ verworfen – in Folge 002 vergeben). Kein Genitiv eines Namens im Sprechtext („Haralds Haus“ nur auf einer Pille; gesprochen „sein Haus“).
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig: `marc` (in 133–135 nicht eingesetzt) für Harald, `laura_ruhig` für Frau Huber (in 133 eingesetzt; mit dem Pool nicht ganz vermeidbar, weil die Rolle eine Frau mittleren Alters ist und sabrina ebenfalls in 133 lief). `william` und `sabrina` nicht gebraucht. Lea nicht verwendet.
- Präfixe `HJ_`/`HA_`/`HU_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. A1: Frau Huber zieht ihren Koffer nach rechts (blickt nach rechts), Harald blickt nach rechts zu ihr; A2/A3: Harald blickt nach links zur Tonne; A4: Harald nach rechts zu Frau Huber, Frau Huber nach links zu ihm; Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HJ_redet`, `HA_redet`, `HU_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` deshalb verworfen), keine Karikatur. Keine weiteren Menschen im Bild (keine Feuerwehr).
- **Abwechslung:** Posen nicht aus 133 (`resting-1`, `easing-1`, `blazer-2`), 134 (`shirt-4`, `blazer-4`, `crossed_arms-2`), 135 (`blazer-4`, `crossed_arms-2`); Besetzungs-/Kontaktbögen von 133–135 daneben gelegt; keine Polka Dots. `robot_dance-3` für Frau Huber verworfen (gleiche Silhouette wie Harald ohne Jacke).
- Figuren-PNGs: `../peeps/op_136/` (66 Dateien, nicht im Repository, im Drive-Master); Kontaktbild `out/besetzung_136.png`.

**Abweichung von den letzten Folgen:** 133 (Bank/Bürgschaft), 134 (Nachbarschaftsstreit/Treppenhaus), 135 (Feld/Grundwasser, Kommission), 129 (Haus mit Dach im Aufriss). Hier neu: Wohnstraße mit kleinem Haus von Frau Huber (eigene Proportionen, Fenster/Tür, Ziegeldach ohne Schornstein), Carport mit Auto, Mülltonne mit stilisierter Flamme, Haralds blaue Jacke als Requisit (Tabler `jacket`, später rußgrau), Koffer und Flugzeug-Symbol für die Reise. Cremegrund durchgehend, Tageslicht („am dritten Tag“, kein Nachtbild nötig). Flammen nur als ruhiges Icon, keine Verletzten.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Frau Huber verreist** `fall`, `nachbar` | Straße ab 0,0 s (Haus, Carport mit Auto, Tonne, Frau Huber mit Koffer und Namensschild, Pille „Haus von Frau Huber“); „2 Wochen Urlaub“ und Flugzeug; Frau Huber zieht den Koffer nach rechts; Harald (mit Jacke) kommt mit Namensschild, Pille „Nachbar“ | tabler:`car` (Blau), `trash` (Grau), `plane-departure`, `luggage` (Lila) | `Fall · Frau Huber verreist` (ab 0,0 s) → `Fall · Der Nachbar Harald` | `szene_136koffer_1` bei „fährt“ (Koffer rollt) |
| **A2 Die Mülltonne brennt** `feuer`–`ha1` | „Am 3. Tag“; Flamme über der Tonne bei „brennt“, Pille „Mülltonne brennt“; Pille „Carport von Frau Huber“; Blase Harald „Das Feuer greift gleich / auf den Carport über!“, roter Pfeil Flamme → Carport bei „greift“ | tabler:`flame` (Orange/Gelb) | `Fall · Die Mülltonne brennt` | `szene_136feuer_1` bei „brennt“ (Knistern) |
| **A3 Harald löscht mit der Jacke** `loesch`–`wert` | Feuerlöscher-Symbol mit Kreuz, Pille „kein Feuerlöscher zur Hand“; bei „zieht“ Harald ohne Jacke, Jacke an seiner Hand; bei „erstickt“ Jacke über der Tonne, Pille; bei „aus“ Flamme weg, Pille „Feuer aus, niemand verletzt“, Harald froh; bei „ruiniert“ Jacke rußgrau, Pille „Jacke ruiniert“, Harald besorgt; „Wert: 250 €“ | tabler:`fire-extinguisher`, `jacket` (Blau/Rußgrau) | `Fall · Harald löscht mit der Jacke` → `Fall · Die Jacke ist ruiniert` | – |
| **A4 Frau Huber kommt zurück** `zurueck`–`frage` | „2 Wochen später“, Frau Huber mit Koffer; Blase Harald „Ihre Mülltonne hat gebrannt. / Ich habe das Feuer mit meiner / Jacke gelöscht. Bitte zahlen / Sie mir 250 €.“; Blase Frau Huber „Danke! Aber um Hilfe / gebeten habe ich Sie nicht.“; Frage-Pille | tabler:`jacket` (Rußgrau), `luggage` | `Fall · Frau Huber kommt zurück` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Anspruchsgrundlage** `agl`–`auf5` | Tafel „Anspruch auf Aufwendungsersatz“, §§ 677, 683 Satz 1, 670 BGB, fünf Farbblöcke 1.–5. zum Wort | tabler:`cash-banknote`, `list-numbers` | `Anspruch: §§ 677, 683 S. 1, 670 BGB` → `Anspruch › Prüfung in 5 Punkten` | – |
| **D 1. Geschäftsbesorgung** `p1`–`p1b` | „Jede Tätigkeit, auch eine rein tatsächliche“ (vgl. III ZR 291/11 Rn. 12), ✓ Feuer löschen | tabler:`flame`, `checklist` | `1. Geschäftsbesorgung` | – |
| **E 2. Fremdes Geschäft** `p2`–`p2c` | ✓ objektiv fremd, gelber Block „Fremdgeschäftsführungswille wird vermutet“ (III ZR 273/16 Rn. 20; III ZR 53/17 Rn. 8), ✓ wollte für sie handeln, auch-fremdes Geschäft mit Beispiel-Pille | tabler:`car-garage`, `heart-handshake`, `home` | `2. Fremdes Geschäft` → `2. › Fremdgeschäftsführungswille vermutet` → `2. › auch-fremdes Geschäft` | – |
| **F 3. Ohne Auftrag** `p3`–`p3c` | Wortlautkarte § 677 vollständig, vier Marker zum gesprochenen Halbsatz, ✓ kein Auftrag, ✓ kein Vertrag | tabler:`file-x`, `hand-stop` | `3. Ohne Auftrag, § 677 BGB` | – |
| **G 4. Berechtigung** `p4`–`p4e` | Wortlautkarte § 683 S. 1 (3 Marker), ✓ Interesse (V ZR 102/15 Rn. 8), ✗ wirklicher Wille unbekannt, ✓ mutmaßlicher Wille (Rn. 12), gelber Block „Maßgeblich: Zeitpunkt der Übernahme“ | tabler:`scale`, `shield-check`, `plane-departure`, `clock` | `4. Berechtigung, § 683 S. 1 BGB` → `4. › Interesse` → `4. › wirklicher oder mutmaßlicher Wille` → `4. › Zeitpunkt der Übernahme` | – |
| **H Sonderregeln** `p679`, `p680` | § 679 (Wortlaut-nah, Beispiel III ZR 273/16 Rn. 20), § 680 (III ZR 54/17 Rn. 48, 55) zeilenweise zum Wort | tabler:`building-community`, `alert-triangle` | `4. › Sonderregel § 679 BGB` → `4. › Sonderregel § 680 BGB` | – |
| **I1 5. Rechtsfolge** `p5`–`p5b` | Wortlautkarte § 670 (3 Marker), „wie ein Beauftragter“, ✓ Jacke durfte er einsetzen | tabler:`receipt-euro`, `fire-extinguisher` | `5. Rechtsfolge, § 670 BGB` → `5. › erforderlich?` | – |
| **I2 Jacke als Aufwendung** `p5c`–`p5f` | freiwillige Vermögensopfer (III ZR 273/16 Rn. 28; III ZR 399/14 Rn. 17), ✓ bewusst geopfert, „nach h. M.“ Begleitschäden, Pille „risikotypische Begleitschäden“, grüner Block „Harald verlangt nur den Wert der Jacke: 250 €“ | tabler:`jacket` (Rußgrau), `flame`, `cash-banknote` | `5. › Jacke als Aufwendung?` → `5. › risikotypische Begleitschäden` → `5. › Höhe` | – |
| **J Abgrenzung** `p684`, `p073` | Wortlautkarte § 684 S. 1 (4 Marker), „nur Herausgabe des Erlangten nach Bereicherungsrecht“, Pille Verweis | tabler:`arrow-back-up` | `Abgrenzung: unberechtigte GoA, § 684 S. 1 BGB` | – |
| **K Ergebnis** `erg`, `erg2` | ✓ berechtigt geführt, grüner Block „Frau Huber muss Harald 250 € für die Jacke zahlen“, Normenkette als Fundstelle | tabler:`checklist`, `cash-banknote` | `Ergebnis` | – |
| **L Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; „„ohne Auftrag“ ist nicht „gegen den Willen““, ✓ Punkt 3, ✓ Punkt 4 | Warnsymbol (Streamline Freehand), tabler:`clock` | `Klausurtipp · ohne Auftrag ist nicht gegen den Willen` | – |
| **M Klausurschema** `sch`–`k5` | breite Karte „Schema: Aufwendungsersatz, §§ 677, 683 Satz 1, 670 BGB“, I.–V. mit Unterzeilen zum Wort | – | `Schema: §§ 677, 683 S. 1, 670 BGB` → `Schema › I. Geschäftsbesorgung` … `Schema › V. Rechtsfolge` | – |
| **N Merksatz** `merke`–`mk3` | Lexi erklärt, drei Teile mit Markern (Interesse, mutmaßlichen Willen, Aufwendungen ersetzt, typische Schäden) | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; einzige Bewegung: Frau Huber zieht in A1 den Koffer (Handlung, mit Rollgeräusch). Kein Zoom.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („250 €“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Huber fährt für zwei Wochen in den Urlaub. Am dritten Tag brennt die Mülltonne vor ihrem Haus; die Flammen drohen auf ihren Carport überzugreifen. Ihr Nachbar Harald hat keinen Feuerlöscher zur Hand. Er zieht seine Jacke aus und erstickt damit die Flammen. Verletzt ist niemand, aber die Jacke ist ruiniert. Sie war noch 250 Euro wert.
>
> Als Frau Huber zurückkommt, erzählt Harald ihr alles und verlangt 250 Euro. Frau Huber bedankt sich, sagt aber: „Um Hilfe gebeten habe ich Sie nicht.“
>
> **Muss Frau Huber die Jacke bezahlen?**
