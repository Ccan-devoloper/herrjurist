# Folge 069 · Anfechtungsklage Schema (§ 42 I VwGO): Zulässigkeit und Begründetheit – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_069.py`](src/skript_069.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“; Voraussetzung laut Plan: Folge 057 (Klagearten), dazu Folge 044 (Verwaltungsakt). Übungsfall nach dem Hook („Die Stadt untersagt dir per Bescheid den Betrieb deines Foodtrucks“), Beispielland Nordrhein-Westfalen: Frau Ebeling verkauft mittags Suppen aus ihrem Foodtruck im Gewerbegebiet; sie hat seit drei Jahren 30.000 € Steuerschulden; die Stadt hört sie an, Herr Gerlach vom Gewerbeamt bringt die Untersagungsverfügung (§ 35 I 1 GewO); drei Wochen später klagt sie. Ablauf: Fall → Klage und Frage → Sachverhalt → Aufbau → A. Zulässigkeit I.–VIII. (Wortlautkarten § 42 I, § 42 II) → B. Begründetheit (Wortlautkarte § 113 I 1) mit I. 1. Ermächtigungsgrundlage (Wortlautkarte § 35 I 1 GewO), 2. formell, 3. materiell (Tatbestand, Rechtsfolge, § 114) und II. Rechtsverletzung → Urteil → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:57,3 (5.835 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Ebeling (EB), um 38 | betreibt den Foodtruck, Klägerin | Pose `standing/easing-2` (hellblaues Hemd `#8DB3F2` über schwarzem Shirt, gelbe Hose), Kopf `Long Bangs` (Haar `#4A3428`), Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Driven` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Rage|Serious` (Ärger), `Tired` (müde) | `sabrina` (Frau, mittel) |
| Herr Gerlach (GE), um 58 | Gewerbeamt der Stadt | Pose `standing/blazer-3` (dunkelblaues Jackett `#3D4A7A`, graue Hose), Kopf `No Hair 3` (Glatze mit grauem Haarkranz), Haut `#E6B48F`; Mimiken `Serious` (ruhig, redet), `Solemn` (denkt) | `william` (Mann, älter) |
| die Richterin (RI), um 50 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/resting-1` (dunkles Oberteil `#34343C`), Kopf `Medium Bangs 3`, Brille `Glasses 2`, Haut `#D9A07A`; Mimiken `Calm` (ruhig), `Serious` (redet) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Ebeling blickt nach rechts zu Herrn Gerlach, er nach links zu ihr; Szene B: Frau Ebeling blickt nach links zum Verwaltungsgericht; Szene R: Frau Ebeling blickt nach rechts zur Richterin, die nach links zu ihr blickt; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `EB_redet`, `GE_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`shirt-1/-2`, `blazer-1/-2` bewusst nicht verwendet).
- **Stimmen nur aus dem Pool** (`william`, `sabrina`, `laura_ruhig`; `marc` nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Ebeling, Gerlach (nicht in der Liste früherer Namen, `grep` über alle Folgen ohne Treffer); die Richterin bleibt namenlos.
- Frau Ebeling ist keine Bösewichtin: sie arbeitet, hofft auf den Sommer, ist verärgert und am Ende müde. Herr Gerlach sachlich.
- Figuren-PNGs: `../peeps/op_069/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 064 (Straße vor der Apotheke, Abschleppwagen), 057 (Seeufer, Bootsverleih), 044 (Kaffeewagen auf dem Marktplatz – ähnliches Gewerbe, deshalb hier bewusst **Gewerbegebiet** mit Fabrikhalle statt Marktplatz und Foodtruck statt Kaffeewagen) und ein Gerichtsbild (Verwaltungsgericht, Waage) – ohne Richterhammer, weil deutsche Gerichte keinen verwenden. Posen `easing-2`, `blazer-3`, `resting-1` in 057/064 nicht als Fallfigur verwendet. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Gewerbegebiet** `fall`–`eb1` | Foodtruck, Fabrikhalle, Sonne; Frau Ebeling; Brief der Stadt (Anhörung); Herr Gerlach bringt den Bescheid; Blasen Gerlach/Ebeling | tabler:`truck` (Gelb) + ph:`bowl-steam` (Weiß) + Pille „Suppen“, tabler:`building-factory-2` (Blau), `sun`, fluent-hc:`envelope`, tabler:`file-text` | `Fall · Mittag im Gewerbegebiet` (ab 0,0 s), `Fall · Der Bescheid` | Gewerbegebiet · Ebeling denkt · Brief · Äußerung · Gerlach kommt · Bescheid · Blase · 30.000 € · Kreuz am Truck · Sorge · Blase Ebeling | Papier (`szene_069brief_1`), als der Bescheid erscheint |
| **B Verwaltungsgericht** `klage`–`frage2` | 3 Wochen später; Frau Ebeling vor dem Gericht mit der Klage; Frage | fluent-hc:`classical-building`, tabler:`file-text` | `Fall · Die Klage`, `Fall · Hat die Klage Erfolg?` | Gericht · Pille · Klage · Frage · Beispiel NRW | – |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Aufbau** `aufbau` | Tafel zwei Schritte | fluent-hc:`classical-building` | `Aufbau · Anfechtungsklage, § 42 I Alt. 1 VwGO` | Titel · A · B | – |
| **E I. Rechtsweg** `rweg`–`rweg3` | Tafel § 40 I 1; Herr Gerlach | fluent-hc:`classical-building` | `A. Zulässigkeit › I. Verwaltungsrechtsweg, § 40 I 1 VwGO` | zwei Merkmale · Behörde · öffentliches Recht · Haken · Verfassungsorgane · Sonderzuweisung | – |
| **F II. Statthafte Klageart** `wl42`–`va3` | Wortlautkarte § 42 I (Auszug), VA-Merkmale, Anfechtungsklage, Verweis 044/057 | tabler:`file-text` + Pille „Untersagung“ | `… › II. Statthafte Klageart, § 42 I Alt. 1 VwGO` | Karte · Marker · Regelung · Außenwirkung · VA · Block · Verweis | – |
| **G III. Klagebefugnis** `wl422`–`adr2` | Wortlautkarte § 42 II, Möglichkeit (4 C 3.20), Adressatentheorie (9 B 4.19) | tabler:`file-text` + Pille „an Frau Ebeling“ | `… › III. Klagebefugnis, § 42 II VwGO` | Karte · 2 Marker · möglich · ausgeschlossen · Fundstelle · Adressatin · Art. 2 I · Block | – |
| **H IV. Vorverfahren** `vv`–`land` | § 68, NRW § 110 JustG, Länderhinweis | fluent-hc:`envelope` + Kreuz | `… › IV. Vorverfahren, §§ 68 ff. VwGO`, `… › NRW: § 110 JustG NRW` | Widerspruch · Gesetz · NRW · Gewerbeordnung · Länderhinweis | – |
| **I V. Klagefrist** `frist`–`frist2` | § 74 I 2, § 58 II, drei Wochen | tabler:`calendar` + Pillen „1 Monat“/„3 Wochen“ | `… › V. Klagefrist, § 74 I VwGO` | Monat · Belehrung · Jahresfrist · 3 Wochen · rechtzeitig | – |
| **J VI. Klagegegner** `kg`–`kg3` | § 78 I Nr. 1, Rechtsträgerprinzip, Nr. 2, NRW; Herr Gerlach | tabler:`building` + Pille „Stadt“ | `… › VI. Klagegegner, § 78 I Nr. 1 VwGO` | Körperschaft · Block · Stadt · Gewerbeamt · Nr. 2 · NRW | – |
| **K VII./VIII.** `bet`–`zul` | §§ 61, 62; Rechtsschutzbedürfnis; zulässig | – | `… › VII. Beteiligten- und Prozessfähigkeit`, `… › VIII. Rechtsschutzbedürfnis` | Personen · RSB · Block zulässig | – |
| **L B. Begründetheit** `wl113`–`zwei` | Wortlautkarte § 113 I 1, zwei Fragen | fluent-hc:`classical-building` | `B. Begründetheit, § 113 I 1 VwGO` | Karte · 3 Marker · I. · II. | – |
| **M 1. Ermächtigungsgrundlage** `egl` | § 35 I 1 GewO (Wortlautkarte, Auszug); Herr Gerlach | tabler:`file-text` + Pille „§ 35 GewO“ | `B. Begründetheit › I. 1. Ermächtigungsgrundlage` | Karte · Gesetz · § 35 · Marker | – |
| **N 2. formell** `formell`–`form` | Zuständigkeit, Anhörung, Heilung, Form | fluent-hc:`envelope`, tabler:`file-text` | `… › I. 2. formelle Rechtmäßigkeit` | Zuständigkeit · Anhörung · geäußert · Heilung · Form | – |
| **O 3. materiell** `tb`–`steuer2` | Tatbestand, Definition (8 C 6.14), Steuerrückstände, Sanierungskonzept, Subsumtion | tabler:`receipt-tax` + Pille | `… › I. 3. materielle Rechtmäßigkeit › Tatbestand` | Tatbestand · Definition · Rückstände · Ausnahme · Sommer · unzuverlässig · Schutz | – |
| **P Rechtsfolge** `rf`–`erm` | gebunden, § 114 | fluent-hc:`balance-scale` | `… › Rechtsfolge` | Wortlaut · gebunden · Ermessensfehler | – |
| **Q II. Rechtsverletzung** `rv`–`rv2` | rechtmäßig; Adressatin | tabler:`file-text` | `B. Begründetheit › II. Rechtsverletzung` | rechtmäßig · Adressatin | – |
| **R Urteil** `urteil`–`ri1` | Verwaltungsgericht: Richterin, Frau Ebeling; Blase | fluent-hc:`balance-scale` | `Ergebnis · Das Urteil` | Ebeling · Richterin · Blase · Pille · Ebeling müde | – |
| **S Klausurtipp** `tipp`–`tipp2` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Schwerpunkte setzen` | 3 Stufen | – |
| **T Klausurschema** `sch`–`s12` | progressiv: A I.–VIII., B I. 1.–3., II. | – | `Klausurschema · Anfechtungsklage` | 15 Aufbaustufen | – |
| **U Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Frau Ebeling verkauft mittags Suppen aus ihrem Foodtruck im Gewerbegebiet einer Stadt in Nordrhein-Westfalen. Sie schuldet dem Finanzamt seit 3 Jahren 30.000 € Steuern; einen Plan zur Tilgung hat sie nicht. Die Stadt gibt ihr Gelegenheit, sich zu äußern. Dann übergibt Herr Gerlach vom Gewerbeamt den schriftlichen, begründeten Bescheid mit richtiger Rechtsbehelfsbelehrung: Die Stadt untersagt ihr das Gewerbe. Frau Ebeling will zahlen, sobald der Sommer gut läuft. 3 Wochen später erhebt sie Klage beim Verwaltungsgericht.“ – Frage: „Hat die Klage Erfolg?“ (kein Fiktiv-Hinweis)
