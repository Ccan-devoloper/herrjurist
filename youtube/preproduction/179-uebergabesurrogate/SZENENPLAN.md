# Folge 179 · Besitzkonstitut & Co.: Eigentum ohne Übergabe (§§ 929 S. 2, 930, 931) – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_179.py`](src/skript_179.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Sachenrecht, Themenplan-Format „Schema“. Hook nach Plan („Du kaufst das Auto deines Nachbarn, der es aber noch eine Woche weiterfahren darf“): Käthe kauft den Kleinwagen ihres Nachbarn Herrn Wöhler, der ihn bis Samstag geliehen weiterfährt. Ablauf: Fall → Frage → Sachverhalt → Einordnung (§ 929 S. 1, Verweis 080; Zulassungsbescheinigung Teil II) → drei Übergabesurrogate in **drei kurzen Fällen mit gleicher Bildstruktur** (links Herr Wöhler vor seinem grünen Haus, rechts Käthe vor ihrem blauen Haus, das Auto je nach Fall bei Käthe, bei Herrn Wöhler oder in der Werkstatt in der Mitte): 1. § 929 S. 2 (Wortlautkarte) → 2. § 930 (Wortlautkarte), § 868 (Wortlautkarte), BGH-Zitatkarte V ZR 92/25 Rn. 20, Sicherungsübereignung und Bestimmtheit → 3. § 931 (Wortlautkarte), Werkstatt als Besitzmittlerin, §§ 398, 870, § 986 Abs. 2 → Merktabelle → Ausblick gutgläubiger Erwerb (eine Tafelzeile, Verweis 083/161) → Lösung → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 6:33,6.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Käthe (KA), um 30 | Käuferin, später Eigentümerin | `standing/blazer-4` (Blazer Blau `#8DB3F2`, Oberteil Weiß, schwarze Hose), Kopf `Medium Bangs 2` (Haar Kastanienbraun `#8B5A2B`), Haut `#F3CDB0`; Mimiken `Calm`, `Smile` (redet), `Suspicious`, `Concerned\|Serious`, `Serious` | `sabrina` (Frau, mittel) |
| Herr Wöhler (WO), um 45 | Nachbar, Verkäufer, später Entleiher | `standing/shirt-3` (Hemd Grün `#8FD694`, schwarze Hose), Kopf `Short 5`, Brille `Glasses`, Haut `#D9A07A`, kein Bart; `Calm`, `Smile` (redet), `Suspicious`, `Concerned\|Serious`, `Serious` | `marc` (Mann, mittel) |
| Werkstattmeisterin (WM), um 50 | Fall 3, spricht nicht, Schild „Werkstatt“ | `standing/crossed_arms-2` (schwarzes Oberteil, Arbeitshose Orange `#F9A66C`), Kopf `Bun`, Haut `#C99470`; `Calm`, `Serious`, `Smile` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste des Auftrags und in keiner Datei unter `youtube/` (Volltextsuche `grep -rlw` in `*.py`, `*.md`, `*.json`, `*.csv`, 04.10.2026): Käthe, Wöhler. Nie im Genitiv gesprochen.
- **Stimmen nur aus dem Pool:** `sabrina` (Käthe), `marc` (Herr Wöhler); `william` und `laura_ruhig` nicht eingesetzt (beide in 176). Vorfolgen 177 (hilde/christian) und 178 (niklas/helmut) nutzen andere Stimmen. Die Werkstattmeisterin spricht nicht.
- Präfixe `KA_`, `WO_`, `WM_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen blickt Herr Wöhler nach rechts zu Käthe, Käthe nach links zu ihm; die Werkstattmeisterin blickt zuerst zu Käthe, dann zu Herrn Wöhler, wenn er spricht. In den Tafelszenen blicken alle zur Tafel nach links (Kontaktbild `besetzung_179.png` im Master).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `KA_redet`, `WO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur. `robot_dance-3` für Herrn Wöhler verworfen (Silhouette zu nah an Lexi).
- Figuren-PNGs: `../peeps/op_179/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen der letzten drei Folgen (176: `blazer-1`, `pointing_finger-2`; 177: `blazer-3`, `robot_dance-2`; 178: noch ohne Figuren) nicht verwendet. Schauplatz neu: **Wohnstraße mit zwei Häusern und Einfahrt, Werkstatt in der Mitte** (161: Haustür, Park, Flohmarktstand; 080: Hof mit Fahrrad). Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall** `fall`–`frage2` | Häuser links (grün) und rechts (blau), Auto vor dem Haus von Herrn Wöhler; Pillen „Du kaufst das Auto deines Nachbarn …“, „Kleinwagen für 4.000 €“; Geldschein wandert Käthe → Herr Wöhler, Zulassungsbescheinigung Herr Wöhler → Käthe; Blasen Herr Wöhler „Ich ziehe nächste Woche um. / Darf ich den Wagen / bis Samstag noch fahren?“, Käthe „Gut, ich leihe ihn Ihnen / bis Samstag. Aber ab / heute gehört er mir.“, Herr Wöhler „Einverstanden.“; Kalender am Auto, Schlüssel in der Hand | tabler:`home`, `car` (Gelb), `cash-banknote` (Grün), `file-certificate`, `calendar-event`, `key` | `Fall · Das Auto des Nachbarn` (ab 0,0 s) → `Fall · noch eine Woche fahren` → `Die Frage · Schon heute Eigentümerin?` | `szene_179geld_1` bei der Zahlung |
| **B Sachverhalt** `sv` | Karte vollständig (40 px), ≈ 9 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Einordnung** `p929`–`zbk3` | § 929 S. 1 (Verweis 080), ✓ Einigung, ✗ Übergabe fehlt, ✗ Zulassungsbescheinigung (V ZR 148/21 Rn. 20 f.), Block „wichtig erst beim guten Glauben“ | ph:`handshake`; tabler:`car`, `file-certificate`, `shield-check` | `Einordnung · …` | – |
| **D Surrogate** `surr`, `drei` | Block „3 Wege, die Übergabe zu ersetzen“, drei Autos 1–3, Pille „3 kurze Fälle, immer dasselbe Auto“ | tabler:`car` | `Übergabesurrogate · drei Wege` | – |
| **E 1. Bühne** `s1`–`wo3` | gleiche Bühne; Auto fährt in Käthes Einfahrt; Blasen Käthe „Das Auto steht ja / schon bei mir.“, Herr Wöhler „Dann gehört es / ab jetzt Ihnen.“ | tabler:`home`, `car` | `1. § 929 S. 2 BGB › Erwerber hat das Auto` | `szene_179motor_1` beim Fahren |
| **F 1. Tafel** `w929`–`kh` | **Wortlautkarte § 929 S. 2** (vorgelesen, Marker „im Besitz“, „genügt die Einigung“), ✓ nichts mehr übergeben, Block „Käthe wird sofort Eigentümerin.“, Block „Übereignung kurzer Hand“ | tabler:`book`, `car`; ph:`handshake` | `1. … › Einigung genügt` → `› Übereignung kurzer Hand` | – |
| **G 2. Bühne** `s2` | gleiche Bühne, Auto bei Herrn Wöhler, Schlüssel; Pille „Herr Wöhler behält das Auto.“ | tabler:`home`, `car`, `key` | `2. § 930 BGB › Veräußerer behält das Auto` | – |
| **H 2. Wortlaut** `w930`, `bk` | **Wortlautkarte § 930** (vorgelesen, 3 Marker), Block „= das Besitzkonstitut“ | tabler:`book`, `link`, `car` | `2. … › Wortlaut` → `› Besitzkonstitut` | – |
| **I § 868** `p868`–`sub2` | **Wortlautkarte § 868** (Auslassung „…“, Marker Mieter, Verwahrer, ähnlichen Verhältnis, Zeit), ✓ Leihe (V ZR 8/19 Rn. 26), Blöcke Herr Wöhler unmittelbar/Entleiher, Käthe mittelbar | tabler:`book`, `calendar-event`, `key`, `link` | `2. … › Besitzmittlungsverhältnis, § 868 BGB` → `› Leihe bis Samstag` | – |
| **J konkret** `konk`–`hier` | **Zitatkarte BGH V ZR 92/25 Rn. 20** (Marker „konkreten Inhalt“, „auf Zeit“), Zeile Herausgabeanspruch, ✗ „Ab jetzt besitze ich für dich“ (h. M.), ✓ hier konkret | tabler:`alert-triangle`, `list-check`, `eye-off`, `calendar-event` | `2. … › konkretes Besitzmittlungsverhältnis` → `› abstrakt reicht nicht` | – |
| **K Praxis** `sue`, `best` | Block Sicherungsübereignung (V ZR 8/15 Rn. 7), Bestimmtheit (V ZR 174/21 Rn. 10) | tabler:`building-bank`, `car`, `list-check` | `2. … › Sicherungsübereignung` → `› Bestimmtheit` | – |
| **L 3. Bühne** `s3`–`wo4` | gleiche Bühne, Werkstatt (Garage mit Auto) in der Mitte, Werkstattmeisterin; Blase Herr Wöhler „Holen Sie ihn in der Werkstatt ab. / Meinen Anspruch auf Herausgabe / trete ich Ihnen ab.“ | tabler:`home`, `car-garage` (Orange), `tool` | `3. § 931 BGB › Dritter hat das Auto` | – |
| **M 3. Wortlaut** `w931`, `werk` | **Wortlautkarte § 931** (vorgelesen, 3 Marker), Block Werkvertrag = Besitzmittlungsverhältnis (V ZR 70/16 Rn. 16) | tabler:`book`, `car-garage` | `3. … › Abtretung des Herausgabeanspruchs` → `› Werkstatt als Besitzmittlerin` | – |
| **N Abtretung** `abtr`–`p986` | §§ 398, 870, ✓ weder Mitwirkung noch Kenntnis (IX ZR 295/16 Rn. 34), Block § 986 Abs. 2 | tabler:`file-text`, `link`, `eye-off`, `file-invoice` | `3. … › §§ 398, 870 BGB` → `› § 986 Abs. 2 BGB` | – |
| **O Merktabelle** `tab`–`t4` | breite Karte, drei Zeilen zum Wort (Wer hat die Sache? / Was ersetzt die Übergabe? / Norm), Block „Die Einigung braucht es immer.“ | – | `Merktabelle · Wer hat die Sache?` | – |
| **P Ausblick** `gut`–`gut3` | eine Tafelzeile §§ 932 Abs. 1 S. 2, 933, 934, Zeile § 933, Verweis 083/161 | tabler:`alert-triangle`, `shield-check`, `key` | `Ausblick · gutgläubiger Erwerb` | – |
| **Q Lösung** `loes`–`l5` | ✓ Einigung, ✓ Leihe als konkretes Besitzmittlungsverhältnis, ✓ Eigentümer und Besitzer, Block „Käthe ist schon heute Eigentümerin.“, §§ 929 S. 1, 930, Herausgabe am Samstag | ph:`gavel`; tabler:`calendar-event`, `car`, `key` | `Lösung · Käthe` → `Lösung › Käthe schon heute Eigentümerin` | – |
| **R Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **S Prüfschema** `sch`–`c4` | breite Karte, I.–IV. mit drei Unterpunkten zu II. | – | `Prüfschema` → je Punkt | – |
| **T Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo Geld und Zulassungsbescheinigung die Hand wechseln und das Auto in Käthes Einfahrt fährt.
**Geräusche:** zwei Handlungsgeräusche (Geldscheine, Motor), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons, Phosphor (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden aus Grundformen. Auto ohne Marke und ohne Kennzeichen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Käthe kauft von ihrem Nachbarn Herrn Wöhler dessen Kleinwagen für 4.000 €. Herr Wöhler ist Eigentümer des Autos. Käthe zahlt sofort, und Herr Wöhler gibt ihr die Zulassungsbescheinigung Teil II.
>
> Weil er nächste Woche umzieht, möchte Herr Wöhler den Wagen bis Samstag noch fahren. Käthe leiht ihm das Auto bis Samstag. Beide sind sich einig, dass das Auto ab heute Käthe gehört.
>
> **Ist Käthe schon heute Eigentümerin?**
