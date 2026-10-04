# Folge 144 · Verfügungsbewusstsein: Versteckte Ware – Diebstahl oder Betrug? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_144.py`](src/skript_144.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Abgrenzung. Hook des Themenplans: Ein Kunde versteckt teure Kopfhörer in einer Waschmittelpackung und bezahlt an der Kasse nur das Waschmittel. Fall → Frage (hat Carina mit der Packung auch über die Kopfhörer verfügt?) → Sachverhalt (Grundfall und Gegenvariante) → Abgrenzung (Täter nimmt eigenmächtig weg / Opfer gibt getäuscht heraus, Exklusivität) → Wortlautkarten § 242 Abs. 1 und § 263 Abs. 1 → Kernfrage Verfügungsbewusstsein (BGHSt 41, 198) → Gegenansicht (generelles Verfügungsbewusstsein, OLG Düsseldorf 1992) und Argumente (Fiktion, Nachfrage an der Kasse, § 252) → Subsumtion § 242 → Gegenvariante Etikettentausch (Betrug) → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi).
**Verhältnis zu den Vorfolgen:** 055 (Gewahrsamsenklave) behandelte das Versteck unter der Zeitung in einem Satz und die Vollendung ausführlich – hier nur Verweis („dazu unsere Folge zur Gewahrsamsenklave“). 065 (Betrug-Schema) erklärte die Vermögensverfügung – hier nur Verweis. 022 (Tankbetrug) ist eine andere Abgrenzung (Geben statt Nehmen beim Tanken) und wird nicht wiederholt.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Fabian (FA), um 30 | Kunde, versteckt die Kopfhörer | `standing/walking-2` (schwarzes T-Shirt, Hose Blau `#8DB3F2`, weiße Schuhe; gehend), Kopf `Short 4`, Haut `#E8B48F`. Mimiken `Calm`, `Smile` (redet), `Suspicious` (prüfender Blick beim Verstecken), `Serious`, `Concerned|Serious`, `Solemn`, `Tired` | `niklas` (Mann, jung) |
| Carina (CA), um 30 | Kassiererin | `standing/shirt-3` (Hemdbluse Orange `#F9A66C`, schwarze Hose), Kopf `Long`, Haut `#F4D0B5`. Mimiken `Calm`, `Smile` (redet, freundlich), `Serious`, `Suspicious`, `Awe` (Nachfrage), `Concerned|Serious` | `ela_froh` (Frau, jung; nur ein freundlicher Kassensatz, keine ernste Rolle) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts (Fabian an der Kasse zu Carina und auf dem Weg zum Ausgang). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e bei `FA_redet`, `CA_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`shirt-1/-2`, `blazer-2` bewusst nicht), keine Uniform, kein Logo. 50 Figuren-PNGs in `../peeps/op_144/` (Drive-Master). Die Köpfe `Short 4` und `Long` haben keine einfärbbare Haarfläche (Haar schwarz wie im Original).
- **Klischeeprüfung:** Fabian ist ein gewöhnlicher Kunde (T-Shirt, Jeansblau), kein „fieser“ Täter, keine listige Mimik, keine Herkunftszuschreibung; Carina eine freundliche Kassiererin. Keine Gewalt, kein Detektiv.
- **Namen** Fabian, Carina: eindeutig deutsche Aussprache, in keiner Vorfolge vergeben (Auftragsliste und Volltextsuche in allen Skripten/Dokumenten unter `preproduction/`, auch 142/143). Nie im Genitiv.
- **Stimmen** nur aus dem Pool (niklas, ela_froh; helmut nicht gebraucht, julia vermieden). Vorfolgen 141–143 nicht verglichen mit Stimmen (Pool vom Koordinator vergeben).
- **Abwechslung:** Posen und Kleidung nicht aus 141–143 (blazer-4, crossed_arms-2, easing-1, robot_dance-2, blazer-3, easing-2, resting-2, shirt-4); keine Polka Dots.

**Setting:** Supermarkt mit Regal (Kopfhörer oben, Waschmittelpackungen in der Mitte, Flaschen unten), neutralem Kassentresen mit Band und Scanner, Ausgang. 055 zeigte einen Supermarkt mit Kosmetikregal und Deckenspiegel; hier kehrt der Fall bewusst an eine Kasse zurück (der Plan verlangt die Kassensituation), aber mit anderem Regal, anderer Kasse (Tresen mit Band, Kassiererin hinter dem Tresen), anderen Waren und Figuren und neuem Bildelement Waschmittelpackung mit Röntgenblick. **Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Supermarkt** `fall`→`frage2` | Regal links, Kasse rechts; Fabian nimmt Kopfhörer (Pille „Kopfhörer · 120 €“), öffnet eine Waschmittelpackung, Pfeil, Kopfhörer im Durchblick, Packung zu („von außen: nichts zu sehen“); an der Kasse nur die Packung aufs Band; Carina erscheint mit Namen, scannt („Waschmittel · 8 €“); Blasen „8 €, bitte.“ (Carina), „Hier, bitte. Schönen Tag noch.“ (Fabian); Fabian mit der Packung am Ausgang; Frage-Pillen | tabler: `headphones`, `wash` (Aufdruck), `barcode`, `bottle`, `door-exit`; Packung, Regal, Tresen als Bausteine (`packung()`, `karte`) | `Fall · Im Supermarkt` (ab 0,0 s) → `Fall · Das Versteck` → `Fall · An der Kasse` → `Fall · Die Frage` | ≈ 19 | Packung schließen (`szene_144packung_1`), Scanner (`szene_144scan_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Abgrenzung** `abgr`→`wille` | zwei Blöcke § 242 / § 263, Zitatkarte BGH 1 StR 402/16 Rn. 11, Block „Entscheidend: der Wille von Carina“; Fabian und Carina rechts | tabler: `headphones`, `hand-grab`, `hand-move`, `help-circle` | `Abgrenzung · Diebstahl oder Betrug?` → `… › Wille des Getäuschten` | ≈ 6 | – |
| **D Wortlaut** `p242`→`vf` | Wortlautkarten § 242 Abs. 1 (Marker „fremde bewegliche Sache“, „wegnimmt“) und § 263 Abs. 1 (Marker „Vorspiegelung falscher“, „einen Irrtum“, „Vermögen … beschädigt“); Zeile „ungeschriebene Vermögensverfügung“; Pille „Folge 065: Betrug-Schema“ | tabler: `book`, `list-numbers` | `Wortlaut › § 242 Abs. 1 StGB` → `… › § 263 Abs. 1 StGB` → `… › ungeschriebene Vermögensverfügung` | ≈ 8 | – |
| **E Kernfrage** `kern`→`hm` | Tafel Verfügungsbewusstsein, Kreuz „Carina weiß nichts“, Zitatkarte BGHSt 41, 198, 203, Kreuz „keine bewusste Verfügung“, Block h. M.; Carina mit Packung (Durchblick) | tabler: `help-circle`, `headphones-off`, `wash`, `barcode` | `Kernfrage › …` | ≈ 10 | – |
| **F Gegenansicht** `gegen`→`raeub` | Gegenansicht (Packung samt Inhalt), OLG Düsseldorf 1992, Kreuz „bloße Fiktion“, Nachfrage „Ist das alles?“, Wertung § 252 | Packung (Baustein), tabler: `shopping-cart`, `ban`, `help-circle`, `hand-grab`, `alert-triangle` | `Streit › …` | ≈ 13 | – |
| **G Subsumtion § 242** `wegn`→`kein263` | Haken je Merkmal, Block „Wegnahme vollendet“, Verweis Folge 055, Ergebnisblock, Kreuz § 263 | tabler: `headphones`, `building-store`, `hand-grab`, `door-exit`, `gavel`, `ban` | `I. Diebstahl, § 242 › …` → `Ergebnis · § 242 (+), § 263 (−)` | ≈ 12 | – |
| **H1 Gegenvariante Kasse** `gv`→`gv3` | Etikett „8 €“ von der Packung auf die Kopfhörer (Pfeil), Kopfhörer offen auf dem Band, Scan „Kopfhörer · 8 €“, Ring, „sieht die Kopfhörer“, „gibt sie bewusst heraus“, „nur zum falschen Preis“ | tabler: `headphones`, `barcode`; Packung | `Gegenvariante · Etikettentausch` → `… · Carina sieht die Kopfhörer` | ≈ 9 | Scanner (`szene_144scan_1`) |
| **H2 Gegenvariante § 263** `gv4`→`gv6` | Haken Täuschung, Irrtum, Verfügung, Schaden; Block Sachbetrug | tabler: `tag`, `headphones`, `gavel` | `Gegenvariante › …` | ≈ 6 | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | ≈ 6 | – |
| **J Prüfschema** `sch`→`s3` | breite Karte, progressiv, grüner Kasten Verfügungsbewusstsein | – | `Prüfschema › …` | ≈ 9 | – |
| **K Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 12 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Kopfhörer im Regal → in der Hand → über der offenen Packung → im Durchblick → Packung zu; Fabian am Regal → an der Kasse → am Ausgang; Etikett wandert auf die Kopfhörer).
**Geräusche:** zwei Handlungsgeräusche, drei Einsätze (Packung schließen; Scannen in A und H1), Freesound CC0, siehe `geraeusche_herkunft.json`.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 242 Abs. 1 wörtlich vorgelesen; § 263 Abs. 1 als Zitat mit Normangabe, gesprochen die Merkmale; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagnachmittag im Supermarkt: Fabian nimmt Kopfhörer für 120 € aus dem Regal. Er öffnet eine Waschmittelpackung, schiebt die Kopfhörer hinein und verschließt die Packung wieder; von außen ist nichts zu sehen.
>
> An der Kasse legt er nur die Packung aufs Band. Kassiererin Carina scannt das Waschmittel für 8 €. Fabian zahlt und verlässt mit der Packung samt Kopfhörern den Laden.
>
> Gegenvariante: Fabian klebt das Preisetikett des Waschmittels (8 €) auf die Kopfhörer und legt sie offen aufs Band. Carina scannt sie und gibt sie ihm für 8 € heraus.
>
> **Hat sich Fabian wegen Diebstahls (§ 242) oder Betrugs (§ 263 StGB) strafbar gemacht?**
