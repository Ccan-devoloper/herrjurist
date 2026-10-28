# Folge 012 · Zivilprozess Ablauf: Von der Klage bis zur Vollstreckung – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_012.py`](src/skript_012.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“. Ein frei erfundener Kaufpreisfall trägt den ganzen Ablauf: Frau Seidel verkauft Herrn Krüger ihr Klavier für 8.000 Euro, er zahlt nicht und behauptet klemmende Tasten. Stationen: I. zuständiges Gericht (§ 23 Nr. 1 GVG n. F.: bis 10.000 €) → II. Klageerhebung (Zustellung, Rechtshängigkeit, Online-Verfahren) → III. Verfahrenseinleitung (schriftliches Vorverfahren) mit Abzweig Versäumnisurteil → IV. Güteverhandlung, streitige Verhandlung, Sachverständigenbeweis → V. Urteil → VI. Berufung (über 1.000 €) → VII. Rechtskraft und Zwangsvollstreckung (Titel, Klausel, Zustellung, Gerichtsvollzieher, § 754a n. F., Pfändung) → Klausurtipp (Anwaltsklausur: Fristen; Urteilsklausur: Relation) → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Seidel (SE), um 65 | Verkäuferin, Klägerin | Pose `standing/pointing_finger-1` (erhobener Zeigefinger: sie besteht auf ihrem Geld), Kopf `Gray Bun`, Brille `Glasses 2`; Kleidung schwarz (Pose ohne einfärbbares Oberteil), Haut `#F0C8A8`; Mimiken `Calm` (ruhig), `Driven` (redet), `Contempt` (ärgert sich), `Smile` (froh), `Serious` (denkt), `Concerned|Serious` (Sorge, nicht verwendet) | `hilde` (Frau, älter) |
| Herr Krüger (KR), um 28 | Käufer, Beklagter, Schuldner | Pose `standing/shirt-4`, Kopf `Short 4`; schwarzes Hemd, Hose Blau `#8DB3F2`, Haut `#D9A07A`; Mimiken `Calm`, `Suspicious` (redet), `Contempt` (trotzig), `Fear` (Schreck), `Serious` (denkt), `Tired` (müde), `Smile` (froh beim Kauf) | `niklas` (Mann, jung) |
| Richterin (RI), um 45, ohne Namen | Richterin am Amtsgericht | Pose `standing/blazer-3`, Kopf `Medium Bangs`; dunkles Kostüm `#3A3A48` (robenähnlich), Haut `#B07552`; Mimiken `Calm`, `Serious` (redet) | `sabrina` (Frau, mittel) |
| Gerichtsvollzieher (GV), um 50, ohne Namen | Vollstreckungsorgan | Pose `standing/walking-2` (kommt an), Kopf `Short 5`, Bart `Moustache 6` (Mund bleibt sichtbar); schwarzes Shirt, Hose Türkis `#7FD6D0`, Haut `#E0AC84`; Mimiken `Calm`, `Serious` (redet) | `christian` (Mann, mittel) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Seidel in der Wohnung und im Sitzungssaal zu Krüger, Krüger in seiner Wohnung zur Tür). Keine Prothesen-Posen. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in den sprechenden Ansichten `SE_redet`, `KR_redet`, `RI_redet`, `GV_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (sabrina, christian, hilde, niklas). **Namen mit eindeutig deutscher Aussprache** (Vorgabe des Kanalinhabers): Seidel, Krüger; „Albrecht“ verworfen, weil Folge 011 den Namen schon nutzt. Figuren-PNGs: `../peeps/op_012/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 008: Stadtpark (Eiswagen, Kiosk), 010: Einrichtungshaus, 011: Deliktsaufbau. 012: Wohnzimmer mit Klavier, Sitzungssaal des Amtsgerichts mit Richtertisch, Krügers Wohnung mit Tür; erstmals ein Gerichtssaal und ein Gerichtsvollzieher.
- Das Stimmen-Pool ist dasselbe wie in 008 (Vorgabe des Koordinators); die Rollen sind anders verteilt (hilde jetzt Klägerin statt Spaziergängerin, niklas Beklagter statt Ordnungsamt, sabrina Richterin, christian Gerichtsvollzieher). Posen und Köpfe neu (008: easing-1, blazer-4, walking-1, shirt-3).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Das Klavier** `fall`→`frage` | Wohnzimmer von Frau Seidel: Bodenlinie, Lampe, Pflanze; Seidel links (blickt zu Krüger), Klavier, Krüger kommt rechts; das Klavier rollt zu Krüger | tabler:`lamp` (Gelb), `plant` (Grün), `piano` (Holzton), `currency-euro-off` (Rot), `building-bank` (Grau) | `Fall · Das Klavier` → `Fall · Die Frage` | Titel, Seidel froh mit Klavier · Krüger · „Kaufpreis: 8.000 €“ · Klavier rollt, „holt es gleich ab“ · „keine Zahlung“, Seidel ärgert sich · Krüger redet, Blase · Seidel redet, Blase · Frage-Pille · „Zivilprozess“ | Klavier wird gerollt (`szene_012rollen_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C I. Zuständiges Gericht** `gericht`→`anwalt` | Tafel links, Seidel rechts; zwei Gerichtsgebäude | tabler:`building-bank` (Grün/Blau), `map-pin` (Rot), `briefcase-off` (Gelb) | `I. Zuständiges Gericht` → `› sachlich, §§ 23 Nr. 1, 71 GVG` → `› örtlich, §§ 12, 13 ZPO` → `› kein Anwaltszwang, § 78 I ZPO` | Streitwert 8.000 € · Amtsgericht (✓) · Landgericht · Grenze seit 2026/vorher 5.000 € · Wohnsitz Krüger · ohne Anwalt | – |
| **D II. Klageerhebung** `klage`→`online` | Tafel, Seidel mit Klageschrift, Brief wandert in Krügers Briefkasten | tabler:`file-text`, `mailbox` (Blau), `mail`, `hourglass` (Gelb), `device-laptop` (Blau) | `II. Klageerhebung › Klageschrift, § 253 ZPO` → `› Zustellung von Amts wegen` → `› Rechtshängigkeit, § 261 ZPO` → `› Online-Verfahren, §§ 1122 ff. ZPO` | Inhalt der Klageschrift Zeile für Zeile · Antrag · Zustellung (Brief) · erhoben (✓) · rechtshängig (✓) · Verjährung gehemmt (✓) · Online-Verfahren | – |
| **E III. Verfahrenseinleitung** `weg`→`frist2` | Tafel mit zwei Wegen; Richterin, dann Krüger | tabler:`file-text` (Gelb), `calendar` | `III. Verfahrenseinleitung › § 272 II ZPO` → `› schriftliches Vorverfahren, § 276 ZPO` | früher erster Termin · schriftliches Vorverfahren · (✓) · 2 Wochen · + 2 Wochen | – |
| **F Abzweig Versäumnisurteil** `vu`→`zurueck` | lila getönte Tafel (Abzweig), Krüger müde/denkt | tabler:`mail-off`, `file-text` (Rot), `arrow-back-up` (Grün) | `… › Abzweig: Versäumnisurteil, § 331 III ZPO` → `… › Abzweig: Einspruch, §§ 338, 339 ZPO` | keine Anzeige · Versäumnisurteil · schlüssig · Einspruch · zurück vor die Säumnis | – |
| **G IV. Güteverhandlung** `mv`→`k2` | Sitzungssaal: Richtertisch in der Mitte, Seidel links, Krüger rechts | Richtertisch als dunkler Block | `IV. Mündliche Verhandlung › Termin` → `› Güteverhandlung, § 278 II ZPO` | Saal · „Krüger: Klavier mangelhaft“ · Güteverhandlung · Richterin redet, Blase · Krüger redet, Blase, Seidel ärgert sich | – |
| **H IV. Verhandlung und Beweis** `streit`→`gutachten` | Tafel; Seidel und Krüger, Klavier mit Fragepille, Gutachten | tabler:`piano`, `file-certificate` | `IV. … › streitige Verhandlung, § 279 ZPO` → `› Beweisaufnahme, §§ 284 ff. ZPO` | streitig · Beweis über streitige Tatsachen · Sachverständiger · Gutachten (✓), Seidel froh, Krüger erschrickt | – |
| **I V. Urteil** `urteil`→`r2` | Tafel; Richterin verkündet den Tenor | tabler:`file-text` | `V. Urteil › Endurteil, § 300 ZPO` → `› Aufbau, § 313 ZPO` → `› Tenor` | Endurteil · Rubrum · Tenor · Tatbestand · Entscheidungsgründe · Tenor-Block, Richterin redet, Blase | – |
| **J VI. Berufung** `beruf`→`frist` | Tafel; Krüger mit Denkblase „Berufung?“ | tabler:`calendar` | `VI. Berufung › Statthaftigkeit, § 511 I ZPO` → `› Beschwerdewert, § 511 II ZPO` → `› Frist, § 517 ZPO` | Berufung · über 1.000 € · bis 2025 600 € · Zulassung · 8.000 € (✓) · 1 Monat | – |
| **K VII. Rechtskraft und Vollstreckung** `rk`→`digital` | Tafel; Seidel, Krüger, dann der Gerichtsvollzieher | tabler:`hourglass`, `currency-euro-off`, `file-text`, `rubber-stamp` (Gelb), `mail`, `device-laptop` | `VII. Rechtskraft und Zwangsvollstreckung › Rechtskraft, § 705 ZPO` → `› Voraussetzungen` → `› 1. Titel, § 704 ZPO` → `› 2. Klausel, § 724 ZPO` → `› 3. Zustellung, § 750 ZPO` → `› Gerichtsvollzieher, §§ 753, 754a ZPO` | rechtskräftig · zahlt nicht · Titel (✓) · Klausel (✓) · Zustellung (✓) · Gerichtsvollzieher · elektronisch | – |
| **L Bei Herrn Krüger** `g1`→`siegel` | Krügers Wohnung: Klavier, Krüger blickt zur Tür, Gerichtsvollzieher steht davor | tabler:`piano`, `door` (Holzton), `file-text`, `sticker` (Rot, Pfandsiegel) | `VII. Zwangsvollstreckung › Gerichtsvollzieher bei Krüger` → `› Pfändung, § 808 ZPO` | Klingeln · GV redet, Blase · Pfändung · Siegel auf dem Klavier · „bleibt in der Regel beim Schuldner“, Krüger müde | Türklingel (`szene_012klingel_1`) |
| **M Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Anwaltsklausur: Fristen` → `Klausurtipp · Urteilsklausur: Relation` | Fristen Zeile für Zeile · Relation · schlüssig · erheblich · Beweis | – |
| **N Klausurschema** `sch`→`sVII` | Schema baut sich auf | – | `Klausurschema` | I. · II. · III. · Abzweig · IV. · V. · VI. · VII. · Titel/Klausel/Zustellung | – |
| **O Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb der Folien harte Schnitte und Pops; zwei Bewegungen (Klavier rollt in Szene A, Brief fällt in Szene D in den Briefkasten).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_012rollen_1`, `szene_012klingel_1`), Herkunft in `geraeusche_herkunft.json`. Ein drittes (Pfandsiegel) wurde verworfen, weil kein passendes Klebegeräusch vorlag (ein Stempelgeräusch hätte nicht zum aufgeklebten Siegel gepasst).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Seidel verkauft Herrn Krüger ihr altes Klavier für 8.000 Euro. Krüger holt es sofort ab, zahlt den Kaufpreis aber nicht. Er meint: „Die Tasten klemmen. Dafür zahle ich keine 8.000 Euro!“ Frau Seidel hält das Klavier für mangelfrei und will klagen.
>
> Annahme: Die Klage wird 2026 erhoben; Krüger wohnt im Bezirk des Amtsgerichts seiner Stadt.
>
> **Wie kommt Frau Seidel an ihr Geld?**
