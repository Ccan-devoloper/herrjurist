# Folge 023 · Anfechtung Schema §§ 119 ff. BGB: Die Prüfung in 5 Schritten – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_023.py`](src/skript_023.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · BGB AT, Themenplan-Format „Schema“. Ein frei erfundener Fall nach dem Plan-Hook („vertippt, 100 statt 10“) trägt das Schema: Buchhändlerin Ilse bestellt per E-Mail beim Großhändler Winkler 100 statt 10 Kartons Kalender (je 20 €); Winkler nimmt an und bucht eine Spedition (80 €, nicht stornierbar); Ilse ruft sofort an und lässt die Bestellung „so nicht gelten“. Ablauf: Fall → Frage → Sachverhalt → Anspruch § 433 II → Wortlaut § 142 I → Schritt 1 Anfechtungsgegenstand (Auslegung zuerst) → Schritt 2 Anfechtungsgrund (Wortlaut § 119 I, Inhalts-/Erklärungsirrtum, Kausalität; Wortlaut § 119 II, §§ 120, 123) → Gegenfall Motiv- und Kalkulationsirrtum → Schritt 3 Anfechtungserklärung § 143 → Schritt 4 Frist §§ 121, 124 → Schritt 5 Bestätigung § 144 → Rechtsfolge § 142 I und Vertrauensschaden § 122 → Gegenfall arglistige Täuschung (Lieferwagen „unfallfrei“) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:47,7 (5.674 Zeichen, Grenze 6.200). Mehr als fünf Minuten wegen dreier Wortlautkarten (§ 142 I vorgelesen, § 119 I und II mit synchronen Markern), zweier zusätzlicher Gegenfälle (Motiv-/Kalkulationsirrtum; arglistige Täuschung mit eigener Frist und ohne § 122) und der Rechtsfolge mit Vertrauensschaden (Vorgabe Kanalinhaber 01.10.2026: bis 7 Minuten, wo der Stoff es erfordert).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ilse (IL), um 55 | Buchhändlerin, Anfechtende | Pose `standing/resting-2` (Hand in der Hüfte), Kopf `Bun` (Haar `#8A6A55`), Brille `Glasses 4`; Oberteil schwarz (Pose), Hose Lila `#B8A9F5`, Haut `#EBC4A0`; Mimiken `Calm`, `Smile`, `Smile Big|Smile` (strahlt), `Concerned|Serious` (redet/Sorge), `Suspicious` (denkt), `Fear` (Schreck), `Serious` (ernst), `Tired` – alle mit geschlossenem Mund | `lisa` (Frau, älter) |
| Herr Winkler (WI), um 50 | Großhändler, Anfechtungsgegner | Pose `standing/robot_dance-2` (offene Hand), Kopf `Short 3`; Hose Blau `#8DB3F2`, Haut `#D9A07A`; Mimiken `Calm`, `Smile`, `Serious` (redet), `Contempt` (Ärger), `Suspicious` | `christian` (Mann, mittel) |
| Jörg (JO), um 40 | Verkäufer des Lieferwagens (Gegenfall § 123) | Pose `standing/walking-2`, Kopf `Short 5`; Hose Grün `#8FD694`, Haut `#F0C8A8`; Mimiken `Calm`, `Cheeky|Smile` (redet), `Fear` (ertappt) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zum Laptop), `_r` blickt nach rechts (Ilse im Telefonat zu Winkler, Jörg zu Ilse).
- Die „-2“-Posen haben ein festes schwarzes Oberteil (nicht umfärbbar); die Figuren unterscheiden sich über Hose, Frisur, Brille und Hautton.
- **Alle Grundmimiken mit geschlossenem Mund** (FOLGE-ABLAUF); Mundzustände a/o/e nur in `IL_redet`, `WI_redet`, `JO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** lisa, christian, stephan (sabrina nicht benötigt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache:** Ilse, Winkler, Jörg (Umlaut erzwingt die deutsche Lesart). Nicht vergeben in früheren Folgen; parallel vergeben (021/022: Frieda, Ritter, Jens, Birgit, Renate) vermieden.
- Figuren-PNGs: `../peeps/op_023/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 021/022 (parallel): Geschäftsfähigkeit, Tankstelle; 020: Fußgängerzone/Skateverbot; 017: Café und Bürobriefkasten (Café bewusst **nicht** wiederholt, daher Buchladen statt Café).
- Hier: Buchladen mit Regal, Ladentisch und Laptop; Großhändlerlager mit Lieferwagen der Spedition; Telefonat; Gegenfall mit Lieferwagen und Werkstatt. Neue Posen gegenüber 020 (`easing-2`, `crossed_arms-2`, `blazer-3`) und 017 (`blazer-4`, `shirt-4`, `resting-1`, `walking-1`).
- Erstmals drei BGB-Wortlautkarten in einer BGB-AT-Folge (§ 142 I, § 119 I, § 119 II).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Bestellung** `fall`–`null` | Buchladen: Regal mit Büchern, Ladentisch mit Laptop, Ilse am Tisch; rechts erscheint das Lager | tabler:`books` (Rot, Blau, Grün, Gelb), `desk` (Gelb), `device-laptop`, `mail` (Gelb), `building-warehouse` (Blau), `calendar` | `Fall · Die Bestellung` (ab 0,0 s) | Laden mit Ilse · Mail · Lager · „Großhändler Winkler“ · Kalender · Denkblase „zehn Kartons“ · „100 Kartons“ (Ilse ernst) · „„0“ zu viel“ · „je 20 €“ · Mail fliegt zum Lager | Tippen (`szene_023tippen_1`) |
| **B Annahme, Anruf, Frage** `annahme`–`frage` | Ilse links (blickt zu Winkler), Winkler vor seinem Lager, Lieferwagen der Spedition | tabler:`mail-check` (Grün, fliegt zu Ilse), `truck-delivery` (Gelb), `mail-opened`, `device-mobile`, `phone-call` (Grün) | `Fall · Die Annahme` → `Fall · Der Anruf` → `Fall · Die Frage` | Dienstagmorgen, Winkler froh · Mail fliegt · Spedition · gelesen · „9 Uhr“ · Schreck · Telefon · Ilse redet, Blase · Winkler redet, Blase · Frage-Pillen, fünf Schritte | Telefonklingeln (`szene_023telefon_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D Anspruch** `ansp`–`nichtig` | Tafel, Winkler und Ilse, Geldschein | tabler:`cash-banknote` | `Winkler gegen Ilse · § 433 II BGB` → `… › nichtig nach § 142 I BGB?` | Anspruch · Vertrag ✓ · Block „fällt weg“ · Rechtsfolge § 142 I | – |
| **E Wortlaut § 142 I** `p142` | Wortlautkarte, vorgelesen, Marker zum Wort | tabler:`book` | `§ 142 I BGB › Wortlaut` | Karte · Marker anfechtbares Rechtsgeschäft/angefochten/von Anfang an nichtig · Block ex tunc | – |
| **F 1. Anfechtungsgegenstand** `s1`–`s1ok` | Tafel, Winkler mit Mail, Ilse | tabler:`mail` | `II. Anfechtung, § 142 I › 1. Anfechtungsgegenstand` → `› Auslegung, §§ 133, 157 BGB` | Willenserklärung · Auslegung · Empfängerhorizont · VIII ZR 59/16 · nicht erkennbar · ✓ 100 Kartons · Block | – |
| **G 2. Anfechtungsgrund** `s2`–`kaus2` | Wortlautkarte § 119 I mit Markern, Zeilen darunter, Ilse mit Laptop | tabler:`device-laptop` | `› 2. Anfechtungsgrund, § 119 I BGB` → `› Kausalität` | Karte · Inhaltsirrtum + Marker · Erklärungsirrtum + Marker · ✓ Ilse · Kausalität + Marker · ✓ Dritter · IV ZB 39/14 | – |
| **H weitere Gründe** `weitere`–`p123` | Wortlautkarte § 119 II, Zeilen §§ 120, 123 | tabler:`user-search`, `run`, `mask` | `› weitere Gründe` → `› Eigenschaftsirrtum, § 119 II` → `› Übermittlung, § 120` → `› Täuschung, Drohung, § 123` | Karte · drei Marker · § 120 · § 123 · Drohung | – |
| **I Gegenfall Motiv/Kalkulation** `motiv`–`treu` | Tafel, Ilse strahlt → Sorge → denkt | tabler:`confetti`, `confetti-off`, `calculator` | `Gegenfall · Motivirrtum` → `Gegenfall · Kalkulationsirrtum` | bewusst · Stadtfest · ✗ abgesagt · Beweggrund · ✗ keine Anfechtung · BAG · Kalkulation · gebunden · § 242 · X ZR 32/14 | – |
| **J 3. Anfechtungserklärung** `s3`–`s3ok` | Tafel, Telefonat Ilse–Winkler | tabler:`device-mobile`, `phone-call` | `› 3. Anfechtungserklärung, § 143 BGB` | § 143 I · andere Teil · ✓ Winkler · Wort „anfechten“ · unzweideutig · Rn. 29 · Zitatblock | – |
| **K 4. Frist** `s4`–`zehn` | Tafel, Uhr → Kalender | tabler:`clock`, `calendar-event` | `› 4. Anfechtungsfrist, § 121 BGB` → `› Täuschung, Drohung, § 124 BGB` → `› Höchstfrist, §§ 121 II, 124 III BGB` | unverzüglich · ohne Zögern · ab Kenntnis · 9:00 · Anruf · ✓ rechtzeitig · ein Jahr · zehn Jahre | – |
| **L 5. kein Ausschluss** `s5`–`s5ok` | Tafel, Daumen hoch → Kreuz | tabler:`thumb-up`, `x` | `› 5. kein Ausschluss, § 144 BGB` | § 144 · Beispiel · Zitat-Pille · V ZR 142/14 · ✓ nicht getan · Block alle fünf Schritte | – |
| **M Rechtsfolge** `folge`–`gewinn` | Tafel, Winkler mit Geld → Lieferwagen | tabler:`cash-banknote`, `truck-delivery` | `Rechtsfolge · § 142 I BGB` → `Rechtsfolge · Vertrauensschaden, § 122 BGB` | nichtig · ✗ 2.000 € · § 122 · § 122 II · ✓ 80 € · ✗ Gewinn · Obergrenze | – |
| **N Gegenfall Täuschung** `jg`–`t122` | Tafel, Jörg (blickt zu Ilse) und Ilse; Lieferwagen → Unfall → Werkstatt | tabler:`truck`, `car-crash` (Rot), `tools` | `Gegenfall · arglistige Täuschung, § 123 I BGB` → `› Frist, § 124 BGB` → `› kein § 122 BGB` | Kauf · Lieferwagen · Jörg redet, Blase · Unfall · ½ Jahr · ✓ § 123 · ✓ § 124 · ✗ § 122 | – |
| **O Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst auslegen, dann anfechten` → `Klausurtipp · Klausurkonvention` | Satz · übereinstimmend Gewolltes · IX ZR 223/20 · 10 Kartons? · ✓ nichts anzufechten · Konvention | – |
| **P Klausurschema** `sch`–`k3` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · II. · 1.–5. einzeln · III. (−) · § 122 | – |
| **Q Merksatz** `merke`–`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur beim Versand der Bestellung und der Annahme-Mail.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_023tippen_1`, `szene_023telefon_1`), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort). Tafeln dürfen Ziffern verwenden („100 Kartons“, „2.000 €“).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Ilse führt einen kleinen Buchladen. Am Montagabend bestellt sie per E-Mail beim Großhändler Winkler Kalender. Sie will 10 Kartons, tippt aber versehentlich „100 Kartons“ zu je 20 Euro. Für Herrn Winkler ist der Tippfehler nicht erkennbar.
>
> Am Dienstagmorgen nimmt Herr Winkler die Bestellung per E-Mail an und bucht gleich eine Spedition für 80 Euro, die er nicht mehr stornieren kann. Ilse liest die Antwort um 9 Uhr und ruft sofort an: „Ich habe mich vertippt! Ich wollte zehn Kartons, nicht hundert. Diese Bestellung lasse ich so nicht gelten.“ Herr Winkler verlangt 2.000 Euro.
>
> *(Frei erfundener Übungsfall.)*
>
> **Muss Ilse die 2.000 Euro zahlen?**
