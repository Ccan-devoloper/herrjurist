# Folge 067 · § 823 I BGB Schema: Radfahrer rammt dich – was musst du beweisen? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_067.py`](src/skript_067.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Deliktsrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Ein Radfahrer rammt dich auf dem Gehweg – was musst du beweisen, um Schadensersatz zu bekommen?“): Martina geht auf dem Gehweg an der Bäckerei von Erwin vorbei; Stefan fährt zügig mitten auf dem Gehweg, streift sie, sie stürzt (Handgelenk verstaucht, Brille zerbrochen – unblutig, keine Wunden). Stefan: „Sie sind mir doch vor das Rad gelaufen!“; Erwin: „Sie waren viel zu schnell!“. Martina verlangt 300 € für die Brille, die Behandlungskosten und Schmerzensgeld. Ablauf: Fall → Frage → Sachverhalt → Wortlaut § 823 I → **Beweislast als roter Faden** → I. Tatbestand (Rechtsgutsverletzung, Handlung, haftungsbegründende Kausalität; § 286 ZPO) → II. Rechtswidrigkeit → III. Verschulden (Deliktsfähigkeit als Einwendung; Fahrlässigkeit, § 2 StVO; keine Vermutung) → Abwandlung 9-Jähriger (Wortlaut § 828 II 1, III; Beweislast; § 829) → IV. Schaden (§ 287 ZPO) → V. Rechtsfolge (§§ 249 II 1, 253 II; § 254) → Ergebnis → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:38,7 (5.683 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Martina (MT), um 35 | Fußgängerin, Anspruchstellerin | `standing/walking-1` (geht, Brille `Glasses 2`), nach dem Sturz `sitting/hands_back-2` (am Boden), danach `standing/resting-1` – alle lila Oberteil `#B8A9F5`, schwarze Hose; Kopf `Medium Bangs`, Haut `#F0C8A8`; nach dem Sturz ohne Brille (die Brille ist zerbrochen); Mimiken `Calm`, `Fear` (Schreck), `Concerned|Serious` (Schmerz/Sorge; redet am Boden), `Suspicious`, `Smile`, `Serious` | `julia` (Frau, jung) |
| Stefan (ST), um 25 | Radfahrer, Schädiger | `sitting/bike` (fährt; Rahmen blau) und `standing/easing-1` (steht nach dem Absteigen, Rad als Tabler-Icon daneben) – beide orange Jacke `#F9A66C`, weißes Oberteil; Kopf `Short 3`, Haut `#D9A27A`, kein Bart; Mimiken `Driven` (fährt), `Fear` (Schreck/ertappt), `Very Angry` (redet), `Calm`, `Suspicious`, `Concerned|Serious` | `niklas` (Mann, jung) |
| Erwin (EW), um 60 | Bäcker, Zeuge | nur `standing/crossed_arms-1` (weißes Oberteil, schwarze Hose), Kopf `No Hair 2`, Haut `#E8B894`, kein Bart; Mimiken `Calm`, `Suspicious` (beobachtet), `Serious` (redet), `Smile`. Präfix `EW_`, weil `bausteine.peep_voll` Namen mit `ER_` dem Ordner `op_we` zuordnet | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |
| Kind (Abwandlung) | 9-jähriger Radfahrer | **keine Figur** (Open Peeps hat keine Kinder; eine verkleinerte Erwachsenenfigur wäre irreführend): Fluent Emoji High Contrast `child` + Tabler `bike` + Pille „9 Jahre“ | – (spricht nicht) |

- **Namen** mit eindeutig deutscher Aussprache, nicht in früheren Folgen vergeben (geprüft per `grep -w` im ganzen Repository und gegen die Liste des Koordinators): Martina, Stefan, Erwin. Kein Genitiv eines Namens im Sprechtext („die Bäckerei von Erwin“).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In A1 blicken Erwin und Martina nach rechts, Stefan (kommt von rechts) nach links; in den Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MT_boden_redet`, `ST_redet`, `EW_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia; gebraucht julia, niklas, helmut. Vorfolge 063 nutzte william/laura_ruhig – keine Überschneidung.
- Keine Prothesen-Posen. Figuren-PNGs: `../peeps/op_067/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 063 (Elektrogeschäft, Küche, Kühlschrank), 064 (Abschleppfall), 059 (Computerladen). Hier neu: Gehweg vor einer Bäckerei (Tabler `building-store` gelb, `baguette`), fahrendes Rad, Sturz, zerbrochene Brille. Folge 011 hatte ebenfalls einen Radfahrer (Uferweg, Joggerin, Strafrecht); hier anderer Ort (Bäckerei in der Stadt), andere Figuren und Posen für die Fußgängerin, anderer Rechtsbereich.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Gehweg** `fall`–`er1` | Bäckerei, Erwin davor, Martina geht; Stefan fährt von rechts heran (Bewegung), Zusammenstoß, Martina am Boden; Pillen Handgelenk/Brille; Blasen Martina, Stefan (abgestiegen, Rad daneben), Erwin | tabler:`building-store` (Gelb), `baguette` (Gelb), `eyeglass-off`, `bike`; fluent-hc:`collision` | `Fall · Auf dem Gehweg` (ab 0,0 s) → `Fall · Der Zusammenstoß` → `Fall · Wer sagt was?` | Grundbild · Rad kommt · zügig · Sturz · Handgelenk · Brille · Blase Martina · Blase Stefan · Blase Erwin | `szene_067sturz_1` bei `stoss` |
| **A2 Forderung** `ford`–`frage2` | Martina und Stefan, drei Forderungen untereinander, zwei Fragen | tabler:`eyeglass`, `first-aid-kit`, `coins` | `Fall · Die Forderung` → `Fall · Die Frage` | | – |
| **B Sachverhalt** `sv` | Karte vollständig, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 823 I** `norm`–`bew2` | Wortlautkarte mit 7 Markern; roter Faden: Block Anspruchsteller (Blau), Block Schädiger (Gelb), Rollenpillen | tabler:`scale` | `Anspruchsgrundlage · § 823 Abs. 1 BGB › Wortlaut` → `Beweislast · der rote Faden` | | – |
| **D1 I. Tatbestand** `tb`–`hd` | Rechtsgutsverletzung (Körper, Gesundheit; Eigentum), Handlung, Haken | tabler:`bandage`, `eyeglass-off`, `bike` | `I. Tatbestand` → `› 1. Rechtsgutsverletzung` → `› 2. Verletzungshandlung` | | – |
| **D2 Kausalität** `ks`–`kzeu` | Äquivalenz, Adäquanz, Schutzzweck (Fundstellen), Haken, Block § 286 ZPO, Zeuge | tabler:`bike`, `bandage`, `link`, `zoom-question`, `shield-check`, `scale`, `eye` | `› 3. haftungsbegründende Kausalität` → `› Beweis: volle Überzeugung, § 286 ZPO` | | – |
| **E II. Rechtswidrigkeit** `rw`, `rw2` | indiziert (h. M.), Kreuz „keinen“ | tabler:`scale`, `shield-x` | `II. Rechtswidrigkeit › indiziert` | | – |
| **F1 III. Deliktsfähigkeit** `vs`–`dfbew` | §§ 827, 828, Haken, Block Einwendungen, Fundstellen | tabler:`brain`, `user-check`, `scale` | `III. Verschulden` → `› 1. Deliktsfähigkeit, §§ 827, 828 BGB` → `› Ausschlussgründe: Beweislast beim Schädiger` | | – |
| **F2 Fahrlässigkeit** `fl`–`zeuge` | § 276 II, § 2 I, V StVO, Haken, lila Block „nicht vermutet“, Zeuge | tabler:`brain`, `road`, `bike`, `scale`, `eye` | `› 2. Fahrlässigkeit, § 276 Abs. 2 BGB` → `› Gehweg, § 2 Abs. 1, 5 StVO` → `› keine Vermutung: Martina beweist` | | – |
| **G1 Abwandlung** `abw`–`abs3` | Kind als Icon, Wortlautkarte § 828 II 1, III mit 6 Markern, roter Block „Fahrrad kein Kraftfahrzeug“; Martina allein | fluent-hc:`child`, tabler:`bike` | `Abwandlung · Radfahrer 9 Jahre` → `› § 828 Abs. 2 BGB: nur Kraftfahrzeug, Schienen- oder Schwebebahn` → `› § 828 Abs. 3 BGB: Einsicht` | | – |
| **G2 Abwandlung** `abs3b`–`p829` | Einsicht vermutet, Kind beweist, Altersgruppe, Block § 829 | wie G1, tabler:`brain`, `scale`, `users` | `› Einsicht vermutet: Beweislast beim Kind` → `› Fahrlässigkeit nach Altersgruppe` → `› Billigkeitshaftung, § 829 BGB` | | – |
| **H IV. Schaden** `sd`–`sdbew` | Behandlungskosten, Brille (Haken), grüner Block § 287 ZPO | tabler:`receipt`, `first-aid-kit`, `eyeglass`, `scale` | `IV. Schaden und haftungsausfüllende Kausalität` → `IV. Schaden › Beweis: § 287 ZPO` | | – |
| **I V. Rechtsfolge** `rf`–`erg` | § 249 II 1, § 253 II, § 254 mit Fundstelle, grüner Ergebnisblock | tabler:`receipt`, `cash-banknote`, `coins`, `scale` | `V. Rechtsfolge › §§ 249 ff. BGB` → `› Schmerzensgeld, § 253 Abs. 2 BGB` → `› Mitverschulden, § 254 BGB` → `Ergebnis` | | – |
| **J Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt, zwei Kausalitäten | Warnsymbol (Streamline Freehand) | `Klausurtipp · zwei Kausalitäten` | | – |
| **K Klausurschema** `sch`–`k5` | breite Karte, Aufbau I.–V. | – | `Klausurschema` → `Klausurschema › Schaden und Rechtsfolge` | | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Fahrt des Rades.
**Blasen:** Stil C (Standard seit 02.10.2026, `bausteine.blase`), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern („300 €“, „9 Jahre“, „§ 828 Abs. 2 Satz 1“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Martina geht auf dem Gehweg an der Bäckerei von Erwin vorbei. Stefan fährt mit dem Fahrrad zügig mitten auf dem Gehweg, streift sie am Arm, und Martina stürzt. Ihr Handgelenk ist verstaucht, ihre Brille zerbrochen.
>
> Stefan sagt: „Sie sind mir doch vor das Rad gelaufen!“ Erwin hat alles gesehen: „Sie waren viel zu schnell!“ Martina verlangt 300 Euro für eine neue Brille, die Behandlungskosten und ein Schmerzensgeld.
>
> **Woraus kann Martina das verlangen, und was muss sie beweisen?**
