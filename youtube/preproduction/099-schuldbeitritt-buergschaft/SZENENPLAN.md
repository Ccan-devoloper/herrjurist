# Folge 099 · Schuldbeitritt, Schuldübernahme oder Bürgschaft? Die Abgrenzung – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_099.py`](src/skript_099.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Schuldrecht AT, Themenplan-Format „Abgrenzung“. Fall nach dem Plan-Hook („Die Freundin ‚übernimmt‘ schriftlich die Autoschulden ihres Partners – was hat sie da eigentlich unterschrieben?“): Jochen finanziert ein gebrauchtes Auto mit einem Bankkredit über 18.000 €; das Auto gehört ihm, nur er fährt es. Frau Zöllner von der Bank will eine weitere Sicherheit, Jochen bleibt Kreditnehmer. Seine Freundin Katja (verdient gut, braucht kein Auto) schreibt mit der Hand „Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro.“ und unterschreibt. Ein Jahr später sind 12.000 € offen, die Bank verlangt Zahlung von Katja.

Ablauf: Fall (Autokredit, Bank, Erklärung, Zahlungsverlangen) → Frage (drei Rechtsinstitute) → Sachverhalt → Auslegung §§ 133, 157 → 1. befreiende Schuldübernahme (Wortlautkarte § 414, § 415, Folge, § 417, Entlassungswille) → 2. Schuldbeitritt (§ 311 Abs. 1, § 421, nicht akzessorisch, formfrei) → 3. Bürgschaft (Wortlautkarte § 765 Abs. 1, §§ 767, 768, 770, 771; Wortlautkarte § 766 S. 1, 2) → Dreispalter (progressiv) → Abgrenzung in 2 Schritten (Entlassung, eigene oder fremde Schuld, Indiz Eigeninteresse, im Zweifel Bürgschaft) → Subsumtion → Ergebnis (Bürgschaft, § 767, § 771) → Klausurtipp (Lexi; Verbraucherdarlehensrecht beim Beitritt, Sittenwidrigkeit) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:22,1 (Sprachspur 382,1 s, 5.731 Zeichen Skript); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Jochen (JO), um 35 | Kreditnehmer, Hauptschuldner | `standing/shirt-4` (schwarzes Hemd, hellblaue Hose `#8DB3F2`, weiße Schuhe), Kopf `Short 5`, Haut `#E8B998`; Mimiken `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `christian` (Mann, mittel) |
| Katja (KA), um 32 | Freundin von Jochen, unterschreibt die Erklärung | `standing/walking-3` (schwarzes T-Shirt, schwarze Hose, Schrittpose), Kopf `Long` (schwarzes Haar), Haut `#D9A27C`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Awe` | `lucy` (Frau, jung) |
| Frau Zöllner (ZO), um 60 | Mitarbeiterin der Bank (Gläubigerseite) | `standing/blazer-1` (blauer Blazer `#5B7DB8`, dunkelblaue Hose `#3D4A7A`, Beinprothese), Kopf `Gray Bun`, Brille `Glasses 4`, Haut `#F2C9A5`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folge 098 und gegen die Koordinatorliste): Jochen, Katja, Zöllner (Katja steht nur als Azure-Stimmenname in `STIMMEN-FALLBACK.md`, nicht als Figur). Kein Genitiv eines Namens im Sprechtext („die Schulden von Jochen“, „die Erklärung von Katja“).
- **Stimmen nur aus dem Pool** (`stephan`, `hilde`, `christian`, `lucy`): `christian`, `lucy`, `hilde`; `stephan` nicht eingesetzt (klingt wie `christian`, nie beide in einer Szene). Drei klar verschiedene Stimmen (Mann mittel, junge Frau, ältere Frau). Vorfolge 098 nutzt `julia`, `ela_froh`, `helmut` – keine Überschneidung.
- Präfixe `JO_`/`KA_`/`ZO_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Autoszene: Jochen blickt nach links zum Auto, Katja nach links zu Jochen. Bank: Frau Zöllner (links) nach rechts, Jochen nach links zu ihr, bei seiner Frage an Katja nach rechts zu ihr; Katja nach links. Zahlungsverlangen: Frau Zöllner nach rechts zu Katja, Katja und Jochen nach links. Ergebnis: Frau Zöllner nach rechts, Jochen und Katja nach links. Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `JO_redet`, `KA_redet`, `ZO_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild.
- **Kein Klischee:** Die Bank bleibt sachlich (keine „fiese“ Gläubigerin), die Beinprothese trägt die Bankmitarbeiterin als selbstverständliches Merkmal, keine Täterrolle. Keine Bärte, keine Karikatur, keine echte Bank, kein Logo.
- **Abwechslung:** Posen nicht aus 096 (`resting-1`, `easing-1`, `blazer-4`, `crossed_arms-1`), 097 (`pointing_finger-2`, `walking-1`), 098 (noch ohne Figuren); keine Polka Dots.
- Figuren-PNGs: `../peeps/op_099/` (58 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 096 (Pfändung, Wohnung), 097 (Versuch, Tür/Schloss), 098 (Gesetzgebungskompetenz). Hier neu: Straße mit Auto, Bankschalter mit Schreibtisch und handschriftlicher Erklärung als Karte, Zahlungsverlangen mit Brief, Dreispalter-Tabelle. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Autokredit** `fall`–`katja` | ab 0,0 s: Auto, Jochen mit Namensschild; „für den Weg zur Arbeit“, Bank + „Kredit: 18.000 €“, „gehört Jochen, nur er fährt“ (Jochen froh), Katja mit Schild, „Freundin: verdient gut“, „braucht kein Auto“ | tabler:`car` (Blau), `building-bank` (Blau) | `Fall · Der Autokredit` | – |
| **A2 Bank** `bank`–`unter` | Bank, Schreibtisch; Blase Frau Zöllner „Wir brauchen noch eine Sicherheit. / Sie bleiben natürlich / unser Kreditnehmer.“; Blase Jochen „Katja, kannst du für mich / einspringen?“; Blase Katja „Klar, ich helfe dir.“; Karte „An die Bank: / Ich übernehme die Schulden von Jochen / aus dem Autokredit über 18.000 Euro.“ zeilenweise zum Wort, Stift in der Hand von Katja, Unterschrift „Katja“ bei „unterschreibt“, „Bank nimmt an“ | tabler:`building-bank`, `desk` (Gelb), `pencil` (Gelb) | `Fall · Die Bank will eine Sicherheit` → `Fall · Katja unterschreibt` | `szene_099unterschrift_1` bei „unterschreibt“ |
| **A3 Ein Jahr später, Frage** `spaet`–`frage2` | Jochen besorgt, Kalender, „offen: 12.000 €“; Bank, Frau Zöllner, Brief, Katja; Blase Zöllner „Sie haben die Schulden übernommen. / Bitte zahlen Sie die 12.000 €.“; Blase Katja „Ich wollte Jochen doch nur helfen, / den Kredit zu bekommen!“; Pillen „Was hat Katja da eigentlich unterschrieben?“, „Schuldübernahme?“, „Schuldbeitritt?“, „Bürgschaft?“ | tabler:`calendar`, `building-bank`, `mail` | `Fall · Ein Jahr später` → `Fall · Die Frage` | `szene_099brief_1` bei „wendet“ |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Auslegung** `ausl`–`drei` | „nicht allein das Wort ‚übernehmen‘“, §§ 133, 157, Empfängerhorizont, BGH III ZR 56/19 Rn. 19, Block „3 Rechtsinstitute kommen in Betracht“ | tabler:`file-text`, `search`, `list-numbers` | `Abgrenzung › Auslegung, §§ 133, 157 BGB` | – |
| **D1 § 414, § 415** `w414`, `p415` | Wortlautkarte § 414 (2 Marker), § 415 Genehmigung | tabler:`arrows-exchange`, `circle-check` | `Abgrenzung › 1. Schuldübernahme, § 414 BGB` → `1. Schuldübernahme › § 415 BGB` | – |
| **D2 Folge, § 417, Entlassungswille** `frei`–`streng` | Block „Folge: Der Altschuldner wird frei“, § 417, BGH VII ZR 13/11 Rn. 7 | tabler:`user-check`, `shield`, `user-x` | `1. Schuldübernahme › Folge, § 417 BGB` → `› Entlassungswille` | – |
| **D3 Schuldbeitritt** `beit`–`formfr` | kumulative Schuldübernahme, § 311 Abs. 1, Gesamtschuld § 421 (III ZR 56/19 Rn. 18), nicht akzessorisch (I ZR 168/14 Rn. 40), formfrei (IX ZR 208/15 Rn. 7) | tabler:`users`, `users-plus`, `link-off`, `file-text` | `Abgrenzung › 2. Schuldbeitritt` | – |
| **D4 Bürgschaft** `w765`–`p771` | Wortlautkarte § 765 Abs. 1 (2 Marker), fremde Schuld, § 767, § 768, § 770, § 771 | tabler:`file-certificate`, `user-plus`, `link`, `shield` | `Abgrenzung › 3. Bürgschaft, § 765 Abs. 1 BGB` → `3. Bürgschaft › Akzessorietät und Einreden` | – |
| **D5 § 766** `w766`, `w766b` | Wortlautkarte § 766 S. 1, 2 (2 Marker), ✓ schriftlich, ✗ elektronische Form | tabler:`signature`, `mail` | `3. Bürgschaft › Schriftform, § 766 BGB` | – |
| **E1 Dreispalter** `tab`–`t4` | breite Karte, Spalten Schuldübernahme / Schuldbeitritt / Bürgschaft, Zeilen Altschuldner, Haftung, akzessorisch, Form – Zelle für Zelle zum Wort | – | `Abgrenzung › Überblick` | – |
| **E2 Zwei Schritte** `k1q`–`zweif` | 1. Altschuldner frei? 2. eigene Schuld / fremde Schuld; Indiz Eigeninteresse (III ZR 56/19 Rn. 20); im Zweifel Bürgschaft (h. M.) | tabler:`user-check`, `users`, `briefcase`, `file-certificate` | `Abgrenzung › 1. Wird der Altschuldner frei?` → `› 2. Eigene oder fremde Schuld?` → `› Indiz: eigenes Interesse` | – |
| **F Subsumtion** `sub`–`s4` | ✗ keine Schuldübernahme, ✗ kein eigenes Interesse, ✓ Bürgschaft trotz „übernehmen“, ✓ eigenhändig unterschrieben | tabler:`building-bank`, `car`, `file-certificate`, `signature` | `Subsumtion · Die Erklärung von Katja` | – |
| **G Ergebnis** `erg`–`erg3` | Bühne: Block „Ergebnis: Katja haftet als Bürgin für 12.000 €“, § 767, Pillen „Bürgin“, „Kreditschuld“, „Einrede der Vorausklage, § 771 BGB“, Pfeil Bank → Jochen „zuerst bei Jochen vollstrecken“ | tabler:`building-bank` | `Ergebnis · Katja haftet als Bürgin` → `Ergebnis › Einrede der Vorausklage, § 771 BGB` | – |
| **H Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; XI ZR 650/20 Rn. 11, XI ZR 82/11 Rn. 9 | Warnsymbol (Streamline Freehand) | `Klausurtipp · Abgrenzung durch Auslegung` | – |
| **I Klausurschema** `sch`–`k5` | breite Karte, I.–V. Zeile für Zeile | – | `Klausurschema` → `› II. Bürgschaftsvertrag` → `› III. Hauptschuld` → `› IV. Einreden` → `› V. Ergebnis` | – |
| **J Merksatz** `merke`, `m2` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Beträge als Ziffern („12.000 €“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Jochen kauft für den Weg zur Arbeit ein gebrauchtes Auto. Eine Bank finanziert es mit einem Kredit über 18.000 Euro. Das Auto gehört Jochen, nur er fährt es. Seine Freundin Katja verdient gut, braucht aber kein Auto.
>
> Frau Zöllner von der Bank verlangt eine weitere Sicherheit; Jochen soll Kreditnehmer bleiben. Katja schreibt mit der Hand an die Bank: „Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro.“ Sie unterschreibt, die Bank nimmt die Erklärung an.
>
> Ein Jahr später zahlt Jochen die Raten nicht mehr; 12.000 Euro sind offen. Die Bank verlangt sie von Katja.
>
> **Was hat Katja unterschrieben, und muss sie zahlen?**
