# Folge 043 · Stellvertretung Schema: Wann bindet der Vertreter den Chef? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_043.py`](src/skript_043.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/BGB AT, Themenplan-Format „Schema“. Übungsfall nach dem Plan-Hook (50 Bürostühle), auf Vorgabe des Koordinators mit einer Angestellten statt einer Praktikantin: Herr Gruber (Inhaber einer Werbeagentur) bevollmächtigt Wiebke mündlich, fünfzig Bürostühle für höchstens 200 € das Stück zu kaufen; Wiebke wählt bei Frau Engel ein Modell zu 180 € und kauft „für die Agentur Gruber“; Gruber will die 9.000 € nicht zahlen. Ablauf: Fall → Frage → Sachverhalt → Anspruch § 433 II → Wortlaut § 164 I 1 → 1. eigene Willenserklärung (Bote, § 165) → 2. im fremden Namen (Offenkundigkeit, unternehmensbezogenes Geschäft, Geschäft für den, den es angeht, § 164 II) → 3. mit Vertretungsmacht (§ 166 II, Wortlaut § 167 I, Umfang) → Rechtsfolge, § 166 I mit § 442 → Gegenfall Überschreitung (Wortlaut § 177 I, Genehmigung verweigert, Ausblick § 179 I) → Gegenfall Rechtsscheinsvollmacht (Duldungs-/Anscheinsvollmacht) → § 181 in einem Satz → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:25,1 (5.524 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Gruber (GR), um 55 | Inhaber der Werbeagentur, Vertretener („Chef“) | Pose `standing/blazer-4` (Sakko, Hand in der Hüfte), Kopf `Gray Short`, Brille `Glasses 3`; Sakko `#4A4A66`, Shirt weiß, Haut `#E8B98F`; Mimiken `Calm`, `Smile`, `Serious` (redet/ernst), `Contempt` (Ärger), `Suspicious` (denkt), `Fear` (Schreck) | `stephan` (Mann, mittel) |
| Wiebke (WI), um 30 | Angestellte, Vertreterin | Pose `standing/easing-1` (offene Jacke), Kopf `Long Bangs`; Jacke Grün `#8FD694`, Shirt weiß, Haut `#F1C6A5`; Mimiken `Calm`, `Smile` (redet/froh), `Suspicious`, `Concerned|Serious` (Sorge), `Smile Big|Smile` (strahlt), `Loving Grin 1|Smile` (verliebt in die Designerstühle), `Fear` | `sabrina` (Frau, mittel) |
| Frau Engel (EN), um 45 | Inhaberin des Möbelhauses, Vertragspartnerin | Pose `standing/resting-1`, Kopf `Long Curly`, Brille `Glasses 2`; Oberteil Rot `#F07A6A`, Haut `#C68E6A`; Mimiken `Calm`, `Smile` (redet/froh), `Suspicious` | `laura_klar` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Gruber zu Wiebke in Szene A; Wiebke zu Frau Engel in B und H; Gruber zu Wiebke in I und L; Wiebke zu Gruber in K).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `GR_redet`, `WI_redet`, `EN_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 bewusst nicht genommen).
- **Stimmen nur aus dem Pool** stephan, sabrina, laura_klar (marc nicht benötigt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, nicht vergeben:** Gruber, Wiebke, Engel. Keine Genitivformen der Namen im Sprechtext („die Erklärung von Wiebke“).
- Figuren-PNGs: `../peeps/op_043/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 041 (Garten am Stadtrand, Gericht), 040 (Küchentisch/Testament), 042 parallel (Körperverletzung). Hier neu: Büro einer Werbeagentur (Schreibtisch, Bildschirm, alter Bürostuhl) und Möbelhaus mit Ladenfront und drei Bürostühlen; Wiederkehr in die Agentur in Szene C, weil Herr Gruber dort die Rechnung öffnet. Neue Posen (`blazer-4`, `easing-1`, `resting-1`) gegenüber 041 (`resting-1` dort für Frau Wendt – andere Frisur, andere Farbe, andere Folge) und 023 (`resting-2`, `robot_dance-2`, `walking-2`).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Der Auftrag** `fall`–`g1` | Agentur: Schreibtisch mit Bildschirm, alter Stuhl; Gruber blickt zu Wiebke | tabler:`desk` (Gelb), `device-desktop`; ph:`office-chair` (Grau) | `Fall · Der Auftrag` (ab 0,0 s) | Gruber allein · Wiebke kommt · „neue Bürostühle“ · Gruber redet, Blase · „50 Bürostühle“ · „höchstens 200 € das Stück“, Wiebke denkt | – |
| **B Im Möbelhaus** `laden`–`e1` | Ladenfront, drei Bürostühle; der grüne rollt zu Wiebke; Frau Engel kommt | tabler:`building-store` (Rot); ph:`office-chair` (Blau, Lila, Grün) | `Fall · Im Möbelhaus` | Wiebke · Frau Engel · Stuhl rollt · „180 €“ · Wiebke froh · Wiebke redet, Blase · „50 Stück“ · Engel redet, Blase · „9.000 €“ | Ladenglocke (`szene_043glocke_1`), rollender Bürostuhl (`szene_043stuhl_1`) |
| **C Rechnung und Frage** `rechnung`–`frage` | Agentur: Umschlag auf dem Schreibtisch, Rechnung; Gruber erschrickt, ärgert sich; Wiebke kommt zur Frage | tabler:`mail-opened`; ph:`invoice` | `Fall · Die Rechnung` → `Fall · Die Frage` | Woche später · Umschlag · Rechnung 9.000 € · Schreck · Gruber redet, Blase · Ärger · Frage-Pille · „Stellvertretung in 3 Schritten“ · 1–3 · Wiebke | aufgerissener Umschlag (`szene_043umschlag_1`) |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **E Anspruch** `ansp`–`vertrag` | Tafel, Frau Engel und Gruber, Geldschein | tabler:`cash-banknote` | `Engel gegen Gruber · § 433 II BGB` | Anspruch · Kaufvertrag nötig · ✗ nur Wiebke, Gruber denkt | – |
| **F Wortlaut § 164 I** `p164`–`drei` | Wortlautkarte, vorgelesen, vier Marker | tabler:`book` | `§ 164 I BGB › Wortlaut` | Karte · Marker Willenserklärung / innerhalb der ihm / zustehenden Vertretungsmacht / im Namen / wirkt unmittelbar … · Block drei Prüfungspunkte, 1–3 | – |
| **G 1. eigene Willenserklärung** `s1`–`p165` | Tafel, Wiebke | tabler:`mail`, `message`, `school`; ph:`office-chair` | `I. Kaufvertrag, § 164 I BGB › 1. eigene Willenserklärung` → `› Bote oder Vertreter?` → `› § 165 BGB` | Bote · Vertreter · Auftreten nach außen · IV ZR 99/18 · Modell selbst · ✓ Vertreterin · § 165 | – |
| **H 2. im fremden Namen** `s2`–`p164b` | Tafel, Wiebke (blickt zu Engel), Frau Engel | tabler:`building` (Blau), `bread` (Gelb) | `› 2. im fremden Namen` → `› Offenkundigkeit, § 164 I 2 BGB` → `› unternehmensbezogenes Geschäft` → `› Geschäft für den, den es angeht` → `› § 164 II BGB` | Prinzip · ✓ ausdrücklich · S. 2 · unternehmensbezogen · Inhaber · Bargeschäft · gleichgültig · = Geschäft für den … · § 164 II, Wiebke erschrickt | – |
| **I 3. mit Vertretungsmacht** `s3`–`s3ok` | Tafel mit Wortlautkarte § 167 I, Gruber (blickt zu Wiebke) und Wiebke | tabler:`message` | `› 3. mit Vertretungsmacht` → `› Vollmacht, §§ 166 II, 167 I BGB` → `› Umfang der Vollmacht` | § 166 II · Karte · Marker · ✓ Innenvollmacht · Umfang · höchstens 200 € · ✓ 180 € · Block gedeckt | – |
| **J Rechtsfolge** `folge`–`kratzer` | Tafel, Gruber und Frau Engel; ab § 166 Wiebke statt Engel | tabler:`cash-banknote`; ph:`office-chair` | `Rechtsfolge · § 164 I BGB` → `Rechtsfolge › Wissenszurechnung, § 166 I BGB` | Block · ✓ Gruber zahlt · ✗ Wiebke nicht · § 166 I · Person der Vertreterin · Kratzer · ✗ § 442 | – |
| **K Gegenfall Überschreitung** `ueber`–`p179` | Tafel mit Wortlautkarte § 177 I; Wiebke verliebt in Designerstuhl; Gruber kommt, redet | ph:`armchair` (Pink) | `Gegenfall · Überschreitung der Vollmacht` → `Gegenfall › § 177 I BGB` → `Gegenfall › Ausblick: § 179 I BGB` | 400 € · Engel weiß nichts · ✗ ohne Vertretungsmacht, Gruber kommt · Karte · Marker · schwebend unwirksam · Gruber redet, Blase · ✗ genehmigt nicht · § 179 I · Wahl · 20.000 € | – |
| **L Gegenfall Rechtsschein** `schein`–`rsok` | Tafel, Gruber und Wiebke | tabler:`calendar-repeat`, `eye-check`, `eye-off`, `scale` | `Gegenfall · ohne Vollmacht` → `› Duldungsvollmacht` → `› Anscheinsvollmacht` → `› Rechtsscheinsvollmacht` | ✗ keine Vollmacht · seit Monaten · weiß und zahlt · Duldung · Anschein · Dauer/Häufigkeit · VIII ZR 289/09 · Block Rechtsscheinsvollmacht · ✓ Duldungsvollmacht möglich | – |
| **M § 181** `p181` | Tafel, Wiebke mit altem Stuhl | ph:`office-chair` (Grau) | `Ausblick · Insichgeschäft, § 181 BGB` | Zeilen in Sprechreihenfolge · Ausnahmen | – |
| **N Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · § 164 BGB ist keine Anspruchsgrundlage` → `Klausurtipp · Reihenfolge` | Satz · beim Vertragsschluss · Kaufpreis · Reihenfolge 1–3 | – |
| **O Klausurschema** `sch`–`k2` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · Erklärung von Wiebke · 1. · 2. · 3. · sonst Genehmigung · II. (+) | – |
| **P Merksatz** `merke`–`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim rollenden Stuhl in Szene B.
**Geräusche:** drei Handlungsgeräusche, CC0 von Freesound, als Kopien vorhandener Dateien (Freesound-API gesperrt), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort). Tafeln und Pillen dürfen Ziffern verwenden („50 Bürostühle“, „9.000 €“).
**Namensschilder:** jede Figur ab ihrem ersten Auftritt und durchgehend, solange sie im Bild ist (auch allein neben der Tafel).

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Herr Gruber betreibt als Inhaber eine Werbeagentur. Er sagt zu seiner Angestellten Wiebke: „Kaufen Sie fünfzig Bürostühle für die Agentur. Höchstens 200 Euro das Stück!“ Wiebke testet im Möbelhaus von Frau Engel mehrere Modelle, wählt selbst einen Stuhl für 180 Euro und erklärt: „Ich kaufe für die Agentur Gruber fünfzig Stück von diesem Modell.“ Frau Engel ist einverstanden: 9.000 Euro, die Rechnung geht an Herrn Gruber.
>
> Herr Gruber will nicht zahlen. Er habe mit Frau Engel nie ein Wort gewechselt.
>
> **Muss Herr Gruber die 9.000 Euro zahlen?**

(Kein Fiktiv-Hinweis auf der Karte, Vorgabe Kanalinhaber 01.10.2026.)
