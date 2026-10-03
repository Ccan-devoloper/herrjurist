# Folge 089 · Abtretung § 398 BGB: Voraussetzungen und Schuldnerschutz – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_089.py`](src/skript_089.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Dein Handwerker verkauft seine offene Rechnung an ein Inkassobüro“): Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen (abgenommen, Rechnung 2.400 €), verkauft die Forderung an ein Inkassobüro (Sachbearbeiter Sven) und tritt sie ab. Tanja weiß nichts und überweist eine Woche später an Ewald; dann meldet sich das Inkassobüro.

Ablauf: Fall (Auftrag, Verkauf der Rechnung, Zahlung, Anruf) → Frage (zwei Teilfragen) → Sachverhalt → § 398 (Wortlautkarte, Zedent/Zessionar) → I. Voraussetzungen: 1. Abtretungsvertrag, 2. Bestehen (§ 405), 3. Bestimmbarkeit (BGH VIII ZR 130/19 Rn. 81), 4. kein Ausschluss (§ 399, § 354a HGB, § 400), Abstraktionsprinzip (§ 453) → II. Rechtsfolge (§ 398 S. 2, § 401) → III. Schuldnerschutz (§§ 404, 406; Wortlautkarte § 407 Abs. 1; Subsumtion mit BGH VII ZR 13/20 Rn. 35; §§ 409, 410) → Ergebnis (§ 816 Abs. 2) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:25,1 (5.615 Zeichen vertont); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ewald (EW), um 58 | Malermeister, Altgläubiger (Zedent) | `standing/shirt-3` (weißes Hemd mit Brusttasche `#F7F7F2` als Malerkleidung, schwarze Hose), Kopf `Gray Short`, Haut `#E8B48F`; Mimiken `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `helmut` (Mann, älter) |
| Tanja (TA), um 32 | Kundin, Schuldnerin | `standing/easing-2` (grünes offenes Hemd `#8FD694`, blaue Hose `#8DB3F2`, Turnschuhe), Kopf `Medium Bangs`, Haut `#B07552`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Awe` | `julia` (Frau, jung) |
| Sven (SV), um 30 | Sachbearbeiter im Inkassobüro (Neugläubiger-Seite) | `standing/walking-2` (schwarzes T-Shirt, lila Hose `#B8A9F5`), Kopf `Short 4`, Haut `#F5D0B5`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner und gegen die Koordinatorliste): Ewald, Tanja, Sven. Verworfen: „Hubert“ (auch englisch lesbar), „Greta“ (Folge 003), „Jana“ (Folge 006). Kein Genitiv eines Namens im Sprechtext („das Wohnzimmer von Tanja“).
- **Stimmen nur aus dem Pool** (`niklas`, `helmut`, `ela_froh`, `julia`): `helmut`, `julia`, `niklas`; `ela_froh` nicht gebraucht. Drei klar verschiedene Stimmen (älterer Mann, junge Frau, junger Mann).
- Präfixe `EW_`/`TA_`/`SV_` (nie `ER_`).
- **Kein Klischee:** Das Inkassobüro ist eine sachliche Gläubigerseite, Sven tritt ruhig und höflich auf („Bitte zahlen Sie …“). Hauttöne bewusst verteilt (die Schuldnerin mit dunklerem Hautton, Sven hell), keine Herkunftsstereotype. Keine Bärte, keine Prothesen-Posen, keine Karikatur, kein echtes Unternehmen, kein Firmenname, kein Logo.
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Wohnzimmer: Ewald (links) blickt nach rechts zu Tanja, Tanja nach links. Büro: Ewald nach rechts zu Sven, Sven nach links. Zahlung: Tanja nach rechts zur Überweisung. Anruf: Tanja nach rechts, Sven nach links (getrennte Orte, Trennlinie). Ergebnis: Tanja und Ewald nach rechts, Sven nach links zu Ewald. Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EW_redet`, `TA_redet`, `SV_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild.
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 084 (`blazer-3`, `resting-2`), 085 (`robot_dance-3`, `blazer-3`), 086 (`walking-1`, `crossed_arms-1`); keine Polka Dots.
- Figuren-PNGs: `../peeps/op_089/` (58 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 084 (Nötigung), 085 (Außenbereich, Wald), 086 (Wohnung mit Laptop, Fitnessstudio). Hier: Wohnzimmer als Malerbaustelle (frisch gestrichene Wand, Leiter, Farbeimer, Farbrolle – bewusst ein Wohnraum, weil der Fall dort spielt; anderes Sofa-Icon und andere Einrichtung als 086), Inkassobüro mit Schreibtisch und Bürogebäude, Überweisung am Smartphone mit Bank-Symbol, Telefonat in zwei getrennten Bildhälften, Ergebnis als Bühne mit drei Figuren. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Auftrag** `fall`, `rech` | Wohnzimmer ab 0,0 s vollständig: Wand (Fläche), Leiter, Sofa, Farbeimer, Farbrolle, Ewald und Tanja mit Namensschild; „frisch gestrichen“, „Arbeit abgenommen“ (beide froh), „Rechnung: 2.400 €“ mit Beleg | ph:`ladder`, `paint-bucket`, `paint-roller`; tabler:`sofa` (Lila), `receipt-euro` (Gelb) | `Fall · Der Auftrag` (ab 0,0 s) | – |
| **A2 Verkauf** `verk`–`sn1` | Büro: Ewald, Schreibtisch, Beleg bei „offene“, Bürogebäude + „Inkassobüro“, Sven; Blase Ewald „Die Forderung gegen Tanja / über 2.400 € trete ich Ihnen ab.“, Beleg wandert bei „ab“ zu Sven; Blase Sven „Einverstanden. Ab jetzt / zahlt sie an uns.“, Handschlag + „Abtretungsvertrag“ | tabler:`desk`, `receipt-euro`; ph:`building-office` (Blau), `handshake` (Gelb) | `Fall · Ewald verkauft die Rechnung` | – |
| **A3 Zahlung** `nichts`, `zahlt` | Wohnzimmer (Pflanze, Sofa, Lampe): „Tanja weiß nichts von der Abtretung“, „1 Woche später“, Smartphone, Karte „Überweisung / 2.400 € an Ewald“, Bank, Geldschein wandert zur Bank, „Konto von Ewald“ | tabler:`device-mobile`, `building-bank`, `cash-banknote`, `sofa`, `lamp`; ph:`potted-plant` | `Fall · Tanja zahlt an Ewald` | `szene_089tippen_1` bei „überweist“ |
| **A4 Anruf, Frage** `meldet`–`frage2` | zwei Orte mit Trennlinie: Tanja mit Smartphone, Anrufsymbol; Sven mit Anrufsymbol, Inkassobüro; Blase Sven „Bitte zahlen Sie die / 2.400 € jetzt an uns.“, Blase Tanja „Aber ich habe doch schon / an den Maler gezahlt!“; Pillen „Muss Tanja noch einmal zahlen?“, „1. Ist die Forderung übergegangen?“, „2. Wie schützt das Gesetz Tanja?“ | tabler:`phone-call` (Grün/Lila), `device-mobile`; ph:`building-office` | `Fall · Das Inkassobüro meldet sich` → `Fall · Die Frage` | `szene_089vibration_1` bei „meldet“ |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 398** `w398`–`rollen` | Wortlautkarte (3 Marker), Zedent/Zessionar/Schuldnerin | tabler:`file-text`, `arrows-exchange` | `Abtretung › § 398 BGB` → `§ 398 BGB › Zedent und Zessionar` | – |
| **D1 Abtretungsvertrag** `vor`–`v1c` | Einigung, formfrei, ohne Schuldner, ✓ geeinigt, ✓ Unkenntnis schadet nicht | tabler:`list-numbers`; ph:`handshake` | `Abtretung › I. Voraussetzungen` → `I. Voraussetzungen › 1. Abtretungsvertrag` | – |
| **D2 Bestehen** `v2`–`v2c` | ✗ kein gutgläubiger Erwerb, Ausnahme § 405, ✓ Werklohn § 631 | tabler:`receipt-euro`, `file-certificate`; ph:`paint-roller` | `I. Voraussetzungen › 2. Bestehen der Forderung` | – |
| **D3 Bestimmbarkeit** `v3`–`v3b` | bestimmt/bestimmbar, künftige Forderung, BGH VIII ZR 130/19 Rn. 81, ✓ eindeutig | tabler:`search`, `receipt-euro` | `I. Voraussetzungen › 3. Bestimmbarkeit` | – |
| **D4 kein Ausschluss** `v4`–`v4b` | § 399, § 354a HGB, § 400, ✓ nichts ausgeschlossen | tabler:`ban`, `building`, `lock`, `shield-check` | `I. Voraussetzungen › 4. kein Ausschluss` | – |
| **D5 Abstraktion** `abstr`, `abstr2` | Block Forderungskauf § 453 Abs. 1, Block Verfügung § 398, „Wirksamkeit grundsätzlich unabhängig …“ | tabler:`receipt-euro`, `arrows-exchange` | `I. Voraussetzungen › Abstraktionsprinzip` | – |
| **E Rechtsfolge** `rf`–`rf2` | § 398 S. 2, § 401, Block „Tanja schuldet 2.400 € dem Inkassobüro“ | tabler:`arrows-exchange`, `shield-check`, `receipt-euro` | `Abtretung › II. Rechtsfolge, § 398 Satz 2 BGB` | – |
| **F Schuldnerschutz** `schutz`–`p406` | nicht schlechter stehen, § 404 + Beispiel, § 406 | tabler:`shield-check`, `arrows-exchange`; ph:`paint-roller` | `Abtretung › III. Schuldnerschutz` → `III. Schuldnerschutz › §§ 404, 406 BGB` | – |
| **G1 § 407 Abs. 1** `w407`–`kenn` | Wortlautkarte (3 Marker), Kenntnis bei Zahlung, ✗ Kennenmüssen | tabler:`cash-banknote`, `eye-off` | `III. Schuldnerschutz › § 407 Abs. 1 BGB` | – |
| **G2 Subsumtion** `sub407`, `frei` | ✓ wusste nichts, ✓ nach der Abtretung an Ewald, Block „Inkassobüro muss Zahlung gelten lassen: Tanja wird frei“, BGH VII ZR 13/20 Rn. 35 | tabler:`cash-banknote`, `shield-check` | `§ 407 Abs. 1 BGB › Tanja zahlt an Ewald` | – |
| **H §§ 409, 410** `p409`, `p410` | Anzeige, Abtretungsurkunde | tabler:`mail`, `certificate` | `III. Schuldnerschutz › §§ 409, 410 BGB` | – |
| **I Ergebnis** `erg`–`p816b` | Bühne: Block „Ergebnis: Tanja muss nicht noch einmal zahlen“, Zeile § 407 Abs. 1, Tanja „frei“, Pfeil Sven → Ewald „§ 816 Abs. 2 BGB“, „Nichtberechtigter“, „2.400 € herausgeben“ | ph:`building-office` | `Ergebnis · Tanja muss nicht noch einmal zahlen` → `Ergebnis › Inkassobüro gegen Ewald, § 816 Abs. 2 BGB` | – |
| **J Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Abtretung im Anspruchsaufbau` | – |
| **K Klausurschema** `sch`–`k5` | breite Karte, I.–IV. Zeile für Zeile | – | `Klausurschema` → `› II. Übergang durch Abtretung` → `› III. nicht erloschen, durchsetzbar` → `› IV. Ergebnis` | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Beleg (Ewald → Sven) und beim Geldschein (Überweisung → Bank).
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahl als Ziffer („2.400 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen. Tanja hat die Arbeit abgenommen. Die Rechnung lautet auf 2.400 Euro.
>
> Ewald verkauft die offene Forderung an ein Inkassobüro und tritt sie ab; Sven schließt den Vertrag für das Büro. Ein Abtretungsverbot haben Ewald und Tanja nicht vereinbart.
>
> Tanja erfährt davon nichts. Eine Woche später überweist sie die 2.400 Euro an Ewald. Danach verlangt das Inkassobüro von ihr Zahlung der 2.400 Euro.
>
> **Muss Tanja noch einmal zahlen?**
