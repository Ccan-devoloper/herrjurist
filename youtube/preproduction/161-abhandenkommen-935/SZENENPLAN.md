# Folge 161 · Abhandenkommen § 935 BGB: Gestohlen oder verliehen? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_161.py`](src/skript_161.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Sachenrecht, Themenplan-Format „Abgrenzung“. Hook nach Plan („Die verliehene Kamera kann wirksam weiterverkauft werden – die gestohlene nicht“) als **zwei Parallelfälle mit gleicher Bildstruktur** (links Hella, Mitte der Veräußerer, rechts Berta am Flohmarktstand): Fall A Leihe an Knut, Fall B Diebstahl im Park. Ablauf: Fall A → Fall B → Frage (zwei Karten nebeneinander) → Sachverhalt → Einordnung (§§ 929, 932, Verweis 083) und Wortlautkarte § 935 Abs. 1 S. 1 → 1. Begriff (BGH-Zitatkarte), Täuschung → 2. mittelbarer Besitz (Wortlautkarte S. 2), es kommt auf Knut an → 3. Besitzdiener (Wortlautkarte § 855, Verweis 027), Gedankenfall Fotoladen, Gegenbeispiel Probefahrt → 4. Ausnahmen (Wortlautkarte Abs. 2) → 5. Wertung (BGH-Zitatkarte, Lehrbegriff Veranlassungsprinzip, Dauer der Sperre) → 6. Lösung beider Fälle nebeneinander (§ 985, Verweis 092) → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 5:59,6.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hella (HE), um 35 | Eigentümerin der Kamera | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Hose Blau `#8DB3F2`, schwarzes Oberteil), Kopf `Medium Straight` (schwarzes Haar; der Kopf hat keine Haarfläche zum Umfärben), Haut `#F1C9A5`; Mimiken `Calm`, `Smile` (redet), `Serious`, `Suspicious`, `Concerned\|Serious`, `Fear`, `Solemn` | `sabrina` (Frau, mittel) |
| Knut (KN), um 35 | Freund und Entleiher; im Gedankenfall Angestellter im Fotoladen | `standing/resting-1` (Pullover Orange `#F9A66C`, schwarze Hose), Kopf `Short 2`, Haut `#E8B48C`, kein Bart; `Calm`, `Smile` (redet), `Suspicious`, `Concerned\|Serious`, `Serious`, `Solemn` | `marc` (Mann, mittel) |
| Berta (BT), um 60 | gutgläubige Käuferin in beiden Fällen, spricht nicht | `standing/crossed_arms-1` (Oberteil Gelb `#F9D56E`, schwarze Hose), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#F3D3B8`; `Calm`, `Smile`, `Suspicious`, `Concerned\|Serious`, `Serious` | – |
| Dieb (DI), um 40 | Fall B, spricht nicht, ohne Namen (Schild „Dieb“) | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Graublau `#9FB4C7`), Kopf `Short 3`, Haut `#EDC09A`; `Calm`, `Serious`. **Kein Täterklischee:** Alltagskleidung, keine Kapuze, keine Maske, keine Waffe, ruhige Mimik, Hautton wie die übrigen Figuren | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste des Auftrags und in keiner Datei unter `youtube/` (Volltextsuche `grep -rlw` in `*.py`, `*.md`, `*.json`, 04.10.2026; „Merle“ und „Ole“ verworfen, weil sie in früheren Szenenplänen stehen): Hella, Knut, Berta. Nie im Genitiv („im Fotoladen von Hella“).
- **Stimmen nur aus dem Pool:** `sabrina` (Hella), `marc` (Knut); `william` und `laura_ruhig` nicht eingesetzt (beide in der Vorfolge 158). Berta und der Dieb sprechen nicht (weniger Credits, keine „Täterstimme“).
- Präfixe `HE_`, `KN_`, `BT_`, `DI_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen blickt Hella nach rechts zu Knut, Knut am Stand nach rechts zu Berta, Berta nach links; im Fall B wendet sich Hella ab, als der Dieb kommt („unbemerkt“). In den Tafelszenen blicken beide Figuren nach links zur Tafel (Kontaktbild `besetzung_161.png` im Master).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HE_redet`, `KN_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur.
- Figuren-PNGs: `../peeps/op_161/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen der letzten drei Folgen (156: `easing-2`, `shirt-3`, `walking-2`, `robot_dance-2`, `pointing_finger-2`; 157: `resting-2`, `walking-1`; 158: `shirt-4`, `easing-1`) nicht verwendet. 083 nutzte `resting-1` mit grünem Pullover (Benno) – hier Orange, anderer Kopf. Schauplätze neu: **Haustür / Park mit Bank / Flohmarktstand** (083: Garage, Park, Straße mit Fahrrad; 158: Wohnstraße mit Autos). Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall A** `fall`–`glaub` | links Hellas Haus, Mitte Knut, rechts Flohmarktstand mit Berta; Kamera wandert Hella → Knut (Leihe), Blase Hella „Hier, bring sie mir / am Montag zurück.“; Knut geht mit der Kamera zum Stand; Blase Knut „Die Kamera gehört mir. / Für 300 € ist sie deine.“; Geldschein wandert zu Knut, Kamera zu Berta | tabler:`home` (Lila), `camera` (Hellgrau), `calendar-event`, `wallet`, `building-store` (Gelb), `cash-banknote` (Grün); ph:`basket`; Tisch aus Grundformen | `Fall A · verliehen` (ab 0,0 s) → `· Knut braucht Geld` → `· auf dem Flohmarkt` → `· Zahlung und Übergabe` | `szene_161geld_1` bei der Zahlung |
| **B Fall B** `fallb`–`glaub2` | **gleiche Bildstruktur**: links Park mit Baum und Bank, Kamera auf der Bank; Dieb kommt, Kamera wandert zu ihm, Hella blickt weg; Dieb geht zum Stand, Geld zu ihm, Kamera zu Berta | ph:`tree` (Grün), `bank()` (ostil), tabler:`camera`, `building-store`, `cash-banknote` | `Fall B · gestohlen` → `· der Dieb` → `· auf dem Flohmarkt` | `szene_161scheine_1` bei der Zahlung |
| **C Frage** `frage`, `frage2` | zwei Karten nebeneinander, je Hella → Knut/Dieb → Berta mit Kamera-Pfeilen (kleine Open Peeps, Namensschilder) | tabler:`camera` | `Die Frage · Zweimal derselbe Kauf` → `· Wird Berta Eigentümerin?` | – |
| **D Sachverhalt** `sv` | Karte vollständig (34 px), ≈ 10 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **E Einordnung** `nb`–`w1b` | ✗ nicht dem Verkäufer, §§ 929 S. 1, 932, Verweis 083, ✓ gutgläubig; **Wortlautkarte § 935 Abs. 1 S. 1** (vorgelesen, 4 Marker) | tabler:`camera`, `shield-check`, `lock`; ph:`handshake` | `Einordnung · …` → `Die Weiche · § 935 Abs. 1 S. 1 BGB` | – |
| **F 1. Begriff** `begr`–`fb` | Zeile „nur Beispiele“, **Zitatkarte BGH V ZR 92/25 Rn. 11** (Marker „unmittelbaren“, „ohne“), Grund (V ZR 8/19 Rn. 9), Block Fall B | tabler:`camera-off`, `hand-grab`, `shield-off`, `camera` | `1. Abhandenkommen › …` | – |
| **G Täuschung** `taeu`, `taeu2` | Block „Mit einer Lüge erschwindelt: trotzdem freiwillig bekommen“, ✗ Zeile mit V ZR 8/19 Rn. 9 | tabler:`masks-theater`, `hand-grab` | `1. Abhandenkommen › Täuschung: trotzdem freiwillig` | – |
| **H 2. mittelbarer Besitz** `mb`–`w2` | Blöcke Hella mittelbar / Knut unmittelbar (§ 868, V ZR 8/19 Rn. 26), **Wortlautkarte § 935 Abs. 1 S. 2** (vorgelesen) | tabler:`camera`, `calendar-event`, `book` | `2. mittelbarer Besitz › …` | – |
| **I Knut entscheidet** `knut`–`umg` | ✓ freiwillig übergeben, Block „kein Abhandenkommen“, ✗ mittelbarer Besitz reicht nicht (V ZR 58/13 Rn. 16, 19), Gegenprobe | tabler:`hand-grab`, `camera`, `link-off`, `alert-triangle` | `2. mittelbarer Besitz › Es kommt auf Knut an` → `› … reicht nicht` → `› Gegenprobe` | – |
| **J 3. Besitzdiener** `bd`, `w3` | Verweis 027, **Wortlautkarte § 855** (4 Marker) | tabler:`alert-triangle`, `briefcase` | `3. Besitzdiener › die Falle` → `› § 855 BGB` | – |
| **K Fotoladen** `studio`–`streit` | Gedankenfall, Blöcke Hella / Knut, ✓ „kann abhandengekommen sein“ (V ZR 58/13 Rn. 9), Block „Die Einzelheiten sind streitig.“ (V ZR 8/19 Rn. 16) | tabler:`building-store`, `briefcase`, `camera`; ph:`scales` | `3. Besitzdiener › Gedankenfall Fotoladen` → … | – |
| **L Probefahrt** `probe`–`probe3` | ✗ kein Besitzdiener, gefälschte Papiere/1 Stunde, Block „kein Abhandenkommen“, Leitsätze V ZR 8/19 | tabler:`car`, `file-text`, `hand-grab` | `3. Besitzdiener › Probefahrt …` | – |
| **M 4. Ausnahmen** `abs2`–`abs2b` | **Wortlautkarte § 935 Abs. 2** (Marker Geld, Inhaberpapiere, öffentlicher, § 979 Absatz 1a), Zeile § 979 Abs. 1a, ✗ Kamera kein Geld, ✗ Flohmarkt keine Versteigerung | tabler:`book`, `coin-euro`, `gavel`, `camera` | `4. Ausnahmen, § 935 Abs. 2 BGB › …` | – |
| **N 5. Wertung** `wert`–`dauer` | **Zitatkarte BGH V ZR 92/25 Rn. 15** (4 Marker), Block „Lehrbegriff: Veranlassungsprinzip“, Block Dauer der Sperre (Leitsatz, Rn. 13) | ph:`scales`; tabler:`hand-grab`, `shield-check`, `user-check`, `lock` | `5. Wertung › …` | – |
| **O 6. Lösung** `loes`–`lb2` | zwei Karten nebeneinander (gleiche Struktur): Fall A grün, Fall B rot; Verweis 092 | ph:`gavel`; tabler:`camera` | `Lösung · beide Fälle` → `› Fall A …` → `› Fall B …` | – |
| **P Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **Q Prüfschema** `sch`–`c3` | breite Karte, I.–III. mit Untermerkmalen | – | `Prüfschema` → je Punkt | – |
| **R Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahl als Ziffer („300 €“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo Kamera und Geld die Hand wechseln und Knut bzw. der Dieb zum Stand gehen (Namensschild wandert mit).
**Geräusche:** zwei Handlungsgeräusche (Geldscheine), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons, Phosphor (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tisch, Bank und Boden aus Grundformen.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Fall A: Hella leiht ihre Kamera ihrem Freund Knut bis Montag. Knut braucht Geld. Auf dem Flohmarkt gibt er die Kamera als seine eigene aus und verkauft sie für 300 € an Berta. Berta zahlt, Knut übergibt ihr die Kamera, beide sind sich über den Eigentumsübergang einig. Berta hat keinen Grund zu zweifeln.
>
> Fall B: Hella legt die Kamera im Park neben sich auf eine Bank. Ein Dieb nimmt sie unbemerkt weg und verkauft sie auf demselben Flohmarkt als seine eigene für 300 € an Berta, die auch diesmal keinen Grund zu zweifeln hat.
>
> Hella hat keinem der Verkäufe zugestimmt.
>
> **Ist Berta jeweils Eigentümerin geworden?**
