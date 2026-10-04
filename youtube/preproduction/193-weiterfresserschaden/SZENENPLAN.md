# Folge 193 · Weiterfresserschaden: Ein 40-Euro-Teil zerstört den ganzen Motor – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_193.py`](src/skript_193.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Deliktsrecht, Klassiker-Fall. Hook nach Plan: „Ein fehlerhaftes Kleinteil im Wert von 40 Euro zerstört nach einigen Wochen den ganzen Motor.“ Fiktiver Fall: Hinnerk kauft im Autohaus einen fabrikneuen Kleinwagen (26.000 €); die Spannrolle am Zahnriemen (40 €) hat der Hersteller fehlerhaft gefertigt. Nach 6 Wochen bricht sie, der Motor ist zerstört, Hinnerk rollt sicher an den Straßenrand. In der Werkstatt: Meister Ottokar (neuer Motor 7.800 €). Ablauf: Fall → Frage, Klassiker (Schwimmerschalter 1976, Gaszug 1983) → Sachverhalt → Warum Deliktsrecht? (§ 437, Hersteller) → Fristen (§ 438 vs. §§ 195, 199) → § 823 Abs. 1 BGB (Wortlautkarte) und das Problem → zwei Interessen, Mangelunwert → Kriterien der Stoffgleichheit → Anwendung → Gegenbeispiel → Kritik (Meinung) und Gesetzgeber → Kontrast § 1 Abs. 1 S. 2 ProdHaftG (Wortlautkarte) → Ergebnis → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:20,7 (Begründung in `ABNAHME.md`).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hinnerk (HI), um 30 | Käufer des Neuwagens, verlangt Ersatz vom Hersteller | `standing/shirt-3` (hellblaues Hemd `#8DB3F2`, schwarze Hose, weiße Schuhe), Kopf `Short 5` (dunkelbraun `#4A3222`), Haut `#F1C9A5`, keine Brille, kein Bart; Mimiken `Smile` (froh), `Calm`, `Fear` (Motor zerstört), `Concerned\|Serious` (redet, Sorge), `Serious`, `Suspicious` (denkt), `Very Angry`, `Tired`, `Solemn` | `niklas` (Mann, jung) |
| Ottokar (OT), um 60 | Kfz-Meister der Werkstatt | `standing/shirt-4` (dunkles Hemd, blaue Arbeitshose `#3F6FB5`, weiße Schuhe), Kopf `No Hair 3` (Glatze, grauer Haarkranz `#C9C9C9`), Brille `Glasses 2`, Haut `#E2B08C`, kein Bart; Mimiken `Serious` (redet), `Suspicious` (denkt), `Calm`, `Concerned\|Serious`, `Smile`, `Tired`, `Solemn` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool. ela_froh (nicht für ernste Rollen) und julia (möglichst meiden) nicht gebraucht. niklas/helmut waren auch in 187 und 190 besetzt – bei diesem Pool für zwei Männerrollen nicht vermeidbar; junge und ältere Männerstimme klar unterscheidbar.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan, Rechtsstand oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026, auch die parallel laufenden Folgen 191/192): Hinnerk, Ottokar – nie im Genitiv („das Eigentum von Hinnerk“). Namensschilder Hinnerk Blau, Ottokar Grün.
**Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. A2: Hinnerk steht am Wagen und blickt nach rechts zu den Bildern von Spannrolle und Motor; A3: Ottokar (links) blickt nach rechts zu Hinnerk, Hinnerk blickt nach links zu Ottokar. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HI_redet`, `OT_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_193/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen (188: `pointing_finger-2`, `crossed_arms-1`; 189: `blazer-4`, `crossed_arms-2`; 190: `resting-1`, `resting-2`, `walking-2`) und der Folge 187 (`easing-1`, `pointing_finger-1`, Kopf `Gray Short`) nicht verwendet; Kopfprobe `Gray Medium` für Ottokar verworfen (wirkte wie eine Frauenfrisur). Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur.
- Schauplätze neu: **Autohaus** (Tabler `building-store`), **Straße in Seitenansicht** (Asphaltband mit Mittelstreifen), **Werkstatt** (grauer Boden, Werkzeug). 187 hatte eine Baustelle, 188 ein Bauamt, 190 einen U-Bahnhof.
- Kein Unfall mit Personen: Spannrolle mit roten Bruchlinien, Motor-Icon mit Bruchlinien, Wagen steht mit Warndreieck am Rand.
- Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Autohaus** `fall`–`teil` | Autohaus, Neuwagen, Hinnerk froh; Lupe oben rechts: Hersteller → Spannrolle mit Bruchlinien, 40 € | tabler:`building-store` (Blau), `car` (Pink), `building-factory-2` (Grün), `disc` (Gelb, Spannrolle); Boden, Pfeil, Bruchlinien programmatisch | `Fall · Im Autohaus` (ab 0,0 s) → `Fall · Die fehlerhafte Spannrolle` | Autohaus ab 0,0 s · Hinnerk · Kleinwagen · 26.000 € · Lupe · Hersteller · Spannrolle · fehlerhaft · 40 € | – |
| **A2 Straße** `fahrt`–`rand` | Wagen auf der Straße, Kalender „6 Wochen“, Spannrolle bricht, Zahnriemen springt über, Motor zerstört; Wagen am Rand mit Warndreieck, Hinnerk steigt aus (erschrocken) | tabler:`car`, `calendar`, `disc`, `engine` (Grau), `alert-triangle` (Rot); Straße programmatisch | `Fall · 6 Wochen später` → `… Die Spannrolle bricht` → `… Motor zerstört` → `… Am Straßenrand` | 7 | `szene_193motor_1` (Freesound CC0 96724) beim Bruch |
| **A3 Werkstatt** `werk`–`klass2` | Werkstattboden, Wagen, zerstörter Motor, Werkzeug; Ottokar redet (2 Blasen), Hinnerk redet; Frage, Klassiker, zwei Fundstellen | tabler:`car`, `engine`, `tools` (Gelb), `disc` | `Fall · In der Werkstatt` → `… Ottokar: Spannrolle gebrochen` → `… neuer Motor: 7.800 €` → `… Hinnerk will Ersatz vom Hersteller` → `… Die Frage` → `… Ein Klassiker` | 13 | `szene_193ratsche_1` (Freesound CC0 551497), als das Werkzeug erscheint |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Warum Deliktsrecht?** `warum`–`hst` | Blöcke Autohaus (§ 437, Verweis 059) und Hersteller (kein Vertrag) | tabler:`car`, `building-store`, `building-factory-2` | `Warum Deliktsrecht? › …` | 4 | – |
| **C2 Fristen** `fr1`–`fr4` | Wortlaut kurz § 438 Abs. 1 Nr. 3, Abs. 2 und § 195, Beginn § 199 Abs. 1, Anspruch erst mit der Zerstörung (VI ZR 21/20 Rn. 21) | tabler:`calendar`, `hourglass`, `engine` | `Warum Deliktsrecht? › Fristen: …` | Zeile für Zeile | – |
| **D § 823 Abs. 1 BGB** `norm`–`prob3` | **Wortlautkarte** (wörtlich vorgelesen), Marker „Eigentum“, „verletzt“; Verweis Schema-Video; Problem | tabler:`book`, `disc` | `Die Norm: § 823 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **E Zwei Interessen** `int`–`mehr` | zwei Blöcke Äquivalenz-/Integritätsinteresse, Mangelunwert, Kreuz „stoffgleich“, Haken „darüber hinaus“ | tabler:`scale`, `receipt-euro`, `shield-check`, `disc` | `Eigentumsverletzung › Stoffgleichheit …` | Zeile für Zeile | – |
| **F Kriterien** `krit`–`k6` | roter Block „stoffgleich, wenn …“, grüner Block „nicht stoffgleich, wenn …“, Haken (Rn. 16) | tabler:`zoom-scan`, `engine-off`, `disc`, `engine` | `Stoffgleichheit › Kriterien …` | Zeile für Zeile | – |
| **G Im Fall** `anw`–`a5` | drei Haken, grüner Block „Eigentumsverletzung am Motor“, Kreuz Spannrolle selbst | tabler:`car`, `disc`, `engine` | `Stoffgleichheit › im Fall …` → `Eigentumsverletzung am Motor (+)` → `Spannrolle selbst: Kaufrecht` | Zeile für Zeile | – |
| **H Gegenbeispiel** `gegen`–`g2` | ganzer Motor falsch konstruiert, Kreuz „stoffgleich“, roter Block „allein Kaufrecht“ | tabler:`engine-off`, `building-store` | `Gegenbeispiel · …` | Zeile für Zeile | – |
| **I1 Kritik** `lehre`, `bt` | Block „Meinung (Teil der Lehre)“, Gesetzgeber mit BT-Drucks. 14/6040 S. 229 | tabler:`book-2`, `building-bank` | `Kritik · …` | 5 | – |
| **I2 ProdHaftG** `phg`–`phg2` | **Wortlautkarte** § 1 Abs. 1 Satz 2 ProdHaftG, Marker „andere“, „Produkt“; Kreuz „Motor: Teil des fehlerhaften Autos“, Block „nur § 823 BGB“ | tabler:`book`, `car` | `Kontrast: Produkthaftungsgesetz › …` | Zeile für Zeile | – |
| **J Ergebnis** `erg`–`erg3` | grüner Block, Bedingung, Haken Hersteller, Spannrolle: Autohaus | tabler:`gavel`, `building-factory-2`, `building-store` | `Ergebnis · …` | 5 | – |
| **K Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **L Prüfschema** `sch`–`c5` | breite Karte, I. (1., 2.), II., III. | – | `Prüfschema › …` | 6 Aufbaustufen | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („40 €“, „26.000 €“, „7.800 €“, „6 Wochen“, „§ 823 Abs. 1 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien (Orts-/Zeitwechsel Autohaus → Straße → Werkstatt); innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Straße, Bruchlinien und Pfeil aus Grundformen (`boden_()`, `strasse()`, `riss()` in `folien_193.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hinnerk kauft in einem Autohaus einen fabrikneuen Kleinwagen für 26.000 €. Der Hersteller hat eine Spannrolle am Zahnriemen fehlerhaft gefertigt, ein Kleinteil im Wert von 40 €. Rechtzeitig erkannt, hätte man die Rolle mit geringem Aufwand tauschen können. Eine Garantie des Herstellers gibt es nicht.
>
> Sechs Wochen fährt der Wagen problemlos. Dann bricht die Spannrolle, der Zahnriemen springt über, und der Motor ist zerstört. Hinnerk rollt sicher an den Straßenrand. Meister Ottokar stellt in der Werkstatt fest: Ein neuer Motor kostet 7.800 €.
>
> Hinnerk sagt: „Der Wagen ist 6 Wochen alt! Dann soll der Hersteller den Motor bezahlen.“
>
> **Kann Hinnerk vom Hersteller Ersatz für den Motor aus § 823 Abs. 1 BGB verlangen?**
