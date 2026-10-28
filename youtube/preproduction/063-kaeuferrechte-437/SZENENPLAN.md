# Folge 063 · § 437 BGB: Die Käuferrechte auf einen Blick – Schema – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_063.py`](src/skript_063.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Kaufrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Der neue Kühlschrank kühlt nicht – was kannst du jetzt verlangen, und in welcher Reihenfolge?“): Manfred kauft im Elektrogeschäft von Frau Kemper einen neuen Kühlschrank für 600 €, sie liefert ihn in seine Küche; am Abend ist er innen warm (Kompressor von Anfang an defekt). Manfred verlangt am Telefon einen neuen innerhalb von zwei Wochen, Frau Kemper sagt zu und vergisst den Auftrag. Manfred kauft woanders für 700 € und will sein Geld zurück und die 100 € Mehrkosten. Ablauf: Fall → Frage → Sachverhalt → Wortlaut § 437 → I. Voraussetzungen (Verweis Folge 059) → II. Nacherfüllung (Wortlaut § 439 I; Abs. 2–4) → III. Frist als Brücke (BGH Vorrang; Entbehrlichkeit; § 475d) → IV. Rücktritt (§§ 323, 326 V, Erheblichkeit, BGH 5 %) oder Minderung (§ 441, Rechenbeispiel) → V. Schadensersatz (§§ 280, 281, 283, 311a; Vermutung; Deckungskauf; § 325; § 284) → Ergebnis, Verjährung § 438 → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:54,3 (5.969 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Manfred (MA), um 65 | Käufer, Verbraucher | `standing/shirt-3` (hellblaues Hemd, schwarze Hose, weiße Schuhe), Kopf `Gray Short`, Haut `#EDC4A0`, kein Bart, keine Brille; Mimiken `Calm`, `Smile` (zufrieden), `Smile Big|Smile` (froh), `Serious` (redet), `Very Angry` (Ärger; redet), `Suspicious` (denkt), `Concerned|Serious` (Sorge) | `william` (Mann, älter) |
| Frau Kemper (KM), um 45 | Inhaberin des Elektrogeschäfts, Unternehmerin | `standing/blazer-4` (grüner Blazer, hellblaues Oberteil, schwarze Hose), Kopf `Long`, Haut `#C99272`, kein Bart; Mimiken `Calm`, `Smile` (froh; redet), `Suspicious` (denkt), `Serious` (ernst), `Concerned|Serious` (Sorge) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep` gegen das ganze Repository und gegen die Liste des Koordinators; „Brandt“ verworfen, weil in Folge 004 vergeben): Manfred, Kemper. Kein Genitiv eines Namens im Sprechtext.
- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zu Frau Kemper), `_r` blickt nach rechts (Frau Kemper in den Fallszenen zu Manfred).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MA_redet`, `MA_aerger`, `KM_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig; gebraucht william (älterer Käufer) und laura_ruhig (Händlerin). Vorfolge 059 nutzte sabrina/marc – keine Überschneidung.
- Kopfprobe: `shirt-1`, `shirt-2`, `blazer-1`, `blazer-2` verworfen (Prothesen-Posen, nicht reflexhaft verwenden; zudem Shorts bzw. Kleidung unpassend). `shirt-3` zuletzt in 056, `blazer-4` zuletzt in 057; in 058–061 nicht verwendet.
- Figuren-PNGs: `../peeps/op_063/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 059 (Computerladen, Laptop, Schreibtisch), 058 (Heroinspritze), 057 (Seeufer). Hier neu: Elektrogeschäft mit Kühlschrank, Küche mit Küchenzeile, Lieferung (Kühlschrank gleitet in die Küche), Telefonat als Ausschnitt (Frau Kemper in ihrem Geschäft), anderes Geschäft mit zwei Kühlschränken (defekt rot / neu grün).

## Szenen

Alle Szenen auf Cremegrund (Tag; „Am Abend“ nur als Pille, kein Nachtgrund nötig).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Elektrogeschäft** `fall` | Frau Kemper und Manfred, Kühlschrank, „neu“, Geldschein, 600 € | tabler:`building-store` (Gelb), `fridge`, `cash-banknote` (Grün) | `Fall · Kauf im Elektrogeschäft` (ab 0,0 s) | Grundbild · Manfred zufrieden · neu · 600 € | – |
| **A2 Küche** `liefer`–`verg` | Lieferung (Kühlschrank gleitet zu der Küchenzeile), Frau Kemper geht; am Abend innen warm, Kompressor defekt; Telefonat: Manfred (Blase), Ausschnitt Frau Kemper im Geschäft (Blase); Auftrag vergessen, 2 Wochen, Frist abgelaufen | tabler:`fridge`, `temperature-plus` (Rot), `device-mobile`, `building-store`, `calendar-time`; Küchenzeile aus `karte` | `Fall · Lieferung in die Küche` → `Fall · Der Kühlschrank kühlt nicht` → `Fall · Nacherfüllung verlangt, Frist 2 Wochen` → `Fall · Die Frist läuft ab` | Lieferung · Bewegung · Abend · warm · Kompressor · Anruf · Blase Manfred · Blase Kemper · vergessen · 2 Wochen · abgelaufen | – |
| **A3 Ersatzkauf** `neu`–`frage2` | anderes Geschäft, defekter Kühlschrank (rot), neuer (grün), 700 €, Blase Manfred (verärgert), 600 € zurück?, 100 € mehr, zwei Fragen | tabler:`building-store` (Grün), `fridge-off` (Rot), `fridge` (Grün) | `Fall · Ersatzkauf in einem anderen Geschäft` → `Fall · Die Frage` | | – |
| **B Sachverhalt** `sv` | Karte vollständig, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 437** `norm`–`verw` | Wortlautkarte vollständig mit 8 Markern, drei Farbblöcke 1./2./3., Verweiszeile | tabler:`fridge`, `list-check` | `Käuferrechte · § 437 BGB › Wortlaut` → `› Verweis auf die Einzelvorschriften` | | – |
| **D I. Voraussetzungen** `vor`–`vok` | drei Merkmale, Subsumtion, Haken, Pille Folge 059 | tabler:`fridge`, `fridge-off`, `device-tv`, `shield-check` | `I. Voraussetzungen › …` → `› Sachmangel bei Gefahrübergang, § 434 Abs. 3 Satz 1 Nr. 1 BGB` → `› kein Ausschluss` | | – |
| **E1 II. Nacherfüllung** `ne`–`wahl` | zweite Chance, Wortlautkarte § 439 I mit 4 Markern, grüner Block „Manfred wählt“ | tabler:`fridge`, `refresh`, `tools` | `II. Nacherfüllung › Vorrang, §§ 437 Nr. 1, 439 BGB` → `› Wahlrecht, § 439 Abs. 1 BGB` | | – |
| **E2 § 439 II–IV** `kost`–`andere` | Kosten, Ein-/Ausbau, Verweigerung, gelber Block | tabler:`truck-delivery`, `hammer`, `calculator`, `arrows-exchange` | `› Kosten, § 439 Abs. 2 BGB` → `› Aus- und Einbau, § 439 Abs. 3 BGB` → `› Verweigerung, § 439 Abs. 4 BGB` | | – |
| **F1 III. Frist** `brue`–`fsub` | Block „Brücke“, Fristzeilen, lila Block Vorrang, BGH-Fundstelle, Haken 2 Wochen | tabler:`hourglass`, `calendar-time` | `III. Frist zur Nacherfüllung › Brücke …` → `› Manfred: 2 Wochen` | | – |
| **F2 Entbehrlichkeit** `entb`–`p475d` | drei Fälle, gelber Block § 475d, Rollenpillen | tabler:`hand-stop`, `tools`, `fridge-off` | `› entbehrlich, §§ 323 Abs. 2, 440, 326 Abs. 5 BGB` → `› Verbrauchsgüterkauf, § 475d BGB` | | – |
| **G1 IV. Rücktritt** `rt`–`rfolge` | Normkette, Erheblichkeit, BGH 5 %, Haken, grüner Block 600 € zurück | tabler:`fridge-off`, `percentage`, `cash-banknote` | `IV. Rücktritt › §§ 437 Nr. 2, 440, 323 BGB` → `› Erheblichkeit, § 323 Abs. 5 Satz 2 BGB` → `› Rückgewähr, § 346 Abs. 1 BGB` | | – |
| **G2 Minderung** `mi`–`mre2` | Minderung, Abwandlung Gefrierfach, Rechnung | tabler:`receipt`, `snowflake-off`, `calculator`, `coins` | `IV. Minderung › § 441 BGB` → `› Berechnung, § 441 Abs. 3 BGB` | | – |
| **H1 V. Schadensersatz** `se`–`se3` | drei Normgruppen | tabler:`scale`, `hourglass`, `fridge-off` | `V. Schadensersatz › § 437 Nr. 3 BGB` → `› §§ 280 Abs. 1, 3, 281 BGB` → `› §§ 283, 311a Abs. 2 BGB` | | – |
| **H2 Schadensersatz am Fall** `vm`–`p284` | Vermutung, Kreuz Entlastung, Mehrkosten, grüner Block, § 325, § 284 | tabler:`scale`, `calendar-x`, `cash-banknote`, `arrows-exchange`, `receipt` | `› Vertretenmüssen, § 280 Abs. 1 Satz 2 BGB` → `› Mehrkosten statt der Leistung, § 281 BGB` → `› neben dem Rücktritt, § 325 BGB` → `› Aufwendungsersatz, § 284 BGB` | | – |
| **I Ergebnis** `erg`–`p438` | zwei grüne Blöcke, Verjährung | tabler:`cash-banknote`, `calendar-time` | `Ergebnis · Rücktritt und Schadensersatz` → `Ausblick · Verjährung, § 438 BGB` | | – |
| **J Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt, drei Schritte | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge der Prüfung` | | – |
| **K Klausurschema** `sch`–`k5` | breite Karte, Aufbau Punkt für Punkt I.–V. | – | `Klausurschema` → `Klausurschema › Rücktritt, Minderung, Schadensersatz` | | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Lieferung des Kühlschranks.
**Blasen:** Stil C (Standard seit 02.10.2026, `bausteine.blase`), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („2 Wochen“, „100 €“). Zahlen auf Tafeln und Pillen als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Manfred kauft im Elektrogeschäft von Frau Kemper einen neuen Kühlschrank für 600 Euro. Am nächsten Tag liefert sie ihn in seine Küche. Am Abend ist er innen noch warm: Der Kompressor ist von Anfang an defekt.
>
> Manfred ruft an: „Der Kühlschrank kühlt nicht! Bringen Sie mir bitte innerhalb von 2 Wochen einen neuen.“ Frau Kemper sagt: „Ja, ich kümmere mich darum.“ Doch sie vergisst den Auftrag, und die 2 Wochen vergehen. Manfred kauft woanders einen gleichen Kühlschrank für 700 Euro. Er will sein Geld zurück und die 100 Euro mehr.
>
> **Was kann Manfred verlangen, und in welcher Reihenfolge?**
