# Folge 196 · Flugreise-Fall: Der Minderjährige, der ohne Ticket mitflog (§ 812 BGB) – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_196.py`](src/skript_196.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Bereicherungsrecht, Klassiker-Fall. Hook nach Plan: „Ein 17-Jähriger schmuggelt sich ohne gültiges Ticket an Bord eines Fluges nach New York.“ Historischer Sachverhalt BGHZ 55, 128 (1968) mit erfundenen Namen: Till (17) fliegt mit gültigem Ticket bis zu einer Zwischenlandung, steigt mit den Transitpassagieren wieder ein und fliegt ohne Ticket weiter nach New York; Einreise verweigert (nur als Text); Stationsleiter Ruprecht fliegt ihn zurück; Rechnung für den Hinflug 1.188 DM; die Mutter genehmigt nichts. Ablauf: Fall → Frage, Leitentscheidung → Sachverhalt → Vertrag? Schadensersatz? → § 812 Abs. 1 Satz 1 (Wortlautkarte), Eingriffskondiktion → Was ist erlangt? (Meinungsstand) → § 818 Abs. 2, 3 (Wortlautkarte), Luxus → § 819 Abs. 1 (Wortlautkarte), § 818 Abs. 4 → Wessen Kenntnis? (Meinungsstand, BGH) → § 828 Abs. 3 analog (Wortlautkarte), Einsicht → Ergebnis, Rückflug GoA → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:26,5 (Begründung in `ABNAHME.md`).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Till (TI), 17 | fliegt ohne Ticket weiter, sympathisch und neugierig, nicht kriminalisiert | `standing/robot_dance-2` (schwarzer Pullover, Jeans `#3F6FB5`, weiße Schuhe, offene Handgeste), Kopf `Pomp` (dunkles Haar), Haut `#F0C8A0`, keine Brille, kein Bart; Mimiken `Smile` (froh, redet), `Awe` (staunt), `Fear`, `Concerned\|Serious` (Sorge, klagt), `Suspicious`, `Tired`, `Solemn`, `Serious`, `Calm` | `niklas` (Mann, jung) |
| Ruprecht (RU), um 60 | Stationsleiter der Fluggesellschaft in New York | `standing/blazer-4` (Uniform-Sakko Navy `#2F4A7A`, weißes Shirt, schwarze Hose), Kopf `No Hair 2` (Haarkranz grau), Brille `Glasses 4`, Haut `#E6B897`, kein Bart; Mimiken `Serious` (redet), `Calm`, `Suspicious`, `Smile` | `helmut` (Mann, älter) |
| Mutter (MU), um 45 | gesetzliche Vertreterin, genehmigt nichts; spricht nicht (Mund immer zu) | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Lila `#B8A9F5`), Kopf `Medium 3` (Haar `#5A3A22`), Haut `#F2CDB2`; Mimiken `Serious`, `Suspicious`, `Solemn`, `Calm` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool; der 17-Jährige `niklas`, der ältere Stationsleiter `helmut` (klar unterscheidbar). ela_froh und julia nicht gebraucht (die Mutter spricht nicht). niklas/helmut auch in 193 – bei diesem Pool für zwei Männerrollen nicht vermeidbar.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan, Rechtsstand, Abnahmebogen oder JSON unter `youtube/preproduction/` (Volltextsuche 04.10.2026, auch 194/195; verworfen: Jannik (010), Gerhard (160, 177), Hannes (104), Edmund wegen möglicher englischer Lesart): Till, Ruprecht – nie im Genitiv. Die Mutter bleibt Funktionsrolle (Namensschild „Mutter“). Namensschilder Till Blau, Ruprecht Grün, Mutter Lila.
**Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. A1: Till blickt nach links zum Flugzeug; A2: Till blickt nach rechts (staunt, redet); A3: Till (links) blickt nach rechts zu Ruprecht, Ruprecht nach links zu Till; A4: Till blickt nach rechts zur Mutter, die Mutter nach links. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `TI_redet`, `TI_klagt`, `RU_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_196/` (68 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten Folgen nicht verwendet (190: resting-1/-2, walking-2; 191: easing-2, walking-1; 192: shirt-3, blazer-2; 193: shirt-3, shirt-4; parallel 194: robot_dance-3, blazer-3; 195: pointing_finger-2, crossed_arms-1, blazer-3). Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur.
- Schauplätze neu: **Zwischenlandung** (Flugzeug-Icon am Boden, Fluggasttreppe), **Kabine** (Fensterreihe, Sitze), **New York** (Hochhaus-Icons, Absperrung), **Zuhause** (Haus, Rechnung). 193 hatte Autohaus/Straße/Werkstatt.
- Fluggesellschaft ohne Namen und Logo; keine Flughäfen; Einreiseverweigerung nur als Pille „Einreise verweigert: kein Visum“; keine Grenzbeamten im Bild.
- Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Zwischenlandung** `fall`–`transit` | Flugzeug am Boden; Till (froh), „17 Jahre“, „gültiges Ticket bis zur Zwischenlandung“; dann Till an der Treppe, „mit den Transitpassagieren wieder eingestiegen“ | tabler:`plane-inflight` (Blau), `ticket` (Grün); Treppe programmatisch (`treppe()`) | `Fall · 1968: Till fliegt mit Ticket` (ab 0,0 s) → `Fall · Wieder eingestiegen, ohne Ticket` | 7 | `szene_196schritte_1` (Freesound CC0 467992) bei `transit` |
| **A2 Kabine** `ny`, `t1` | Fensterreihe, drei Sitze; „ohne Ticket“, „Weiterflug nach New York“; Till staunt, dann redet | tabler:`armchair` (Lila), `ticket-off` (Hellrot); ph:`airplane-in-flight` (Blau); Fenster programmatisch | `Fall · Weiterflug nach New York, ohne Ticket` → `Fall · Till: Einmal New York sehen!` | 4 | `szene_196flugzeug_1` (Freesound CC0 235956) beim Flugzeug |
| **A3 New York** `visum`–`r1` | Hochhäuser, Absperrung, Pille „Einreise verweigert: kein Visum“; Ruprecht kommt, redet; Till erschrocken → besorgt → müde | tabler:`building-skyscraper` (Hellblau/Blau), `barrier-block` (Rot), `plane-departure` (Blau) | `Fall · New York: Einreise verweigert` → `Fall · Stationsleiter Ruprecht` → `Fall · Rückflug noch am selben Tag` | 5 | – |
| **A4 Zuhause** `forder`–`klass2` | Haus, Rechnung „Preis für den Hinflug: 1.188 DM“; Mutter „genehmigt nichts“; Till redet (klagt); Frage, Leitentscheidung mit Fundstelle | tabler:`home` (Gelb), `receipt` (Weiß) | `Fall · Die Rechnung: 1.188 DM` → `… Die Mutter genehmigt nichts` → `… Till: nichts gespart` → `… Die Frage` → `… Der Flugreise-Fall` | 10 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Vertrag? Schadensersatz?** `vertrag`–`bleibt` | §§ 107, 108 (Verweis 021), sozialtypisches Verhalten, kein Schaden, „Bleibt: das Bereicherungsrecht“ | tabler:`file-text`, `scale`; ph:`airplane` | `Vertrag? › …` → `Schadensersatz? › kein Schaden` → `Bleibt: Bereicherungsrecht` | Zeile für Zeile | – |
| **D § 812 Abs. 1 Satz 1 BGB** `norm`–`ogrund` | **Wortlautkarte** (vorgelesen), Marker „Leistung“, „sonstiger“, „ohne“; Leistungsbegriff, keine Leistung, Eingriffskondiktion, BGH legt sich nicht fest, kein Rechtsgrund | tabler:`book`, `ticket-off`, `plane` | `Anspruch: § 812 Abs. 1 Satz 1 BGB › …` | Zeile für Zeile | – |
| **E Was erlangt?** `erl`–`bg2` | zwei Ansichten als Blöcke, Kreuz „erspart: nichts“, BGH-Zeilen mit Fundstellen | tabler:`plane`, `coins` | `Etwas erlangt? › Ansicht 1 …` → `… BGH: erlangte Beförderung, Ersparnis bei § 818 Abs. 3` | Zeile für Zeile | – |
| **F § 818 Abs. 2, 3 BGB** `w2`–`lux2` | **Wortlautkarte** (Abs. 2 mit „…“), Marker „Wert“, „nicht mehr bereichert“; übliche Vergütung, Luxus, nur gutgläubig | tabler:`plane`, `coins`, `gift` | `Umfang › Wertersatz …` → `Umfang › Entreicherung …` | Zeile für Zeile | – |
| **G § 819 Abs. 1 BGB** `w819`–`aber` | **Wortlautkarte**, Marker „Kennt“, „rechtshängig“; § 818 Abs. 4, als hätte er erspart, Till wusste, „Aber: 17 Jahre alt“ | tabler:`book`, `ticket-off`, `users` | `Verschärfte Haftung: § 819 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **H Wessen Kenntnis?** `mst`–`b3` | drei Ansichten (gekennzeichnet), zwei BGH-Blöcke, § 265a StGB, Fundstellen; Till und Mutter | tabler:`users`, `file-text`, `ticket-off` | `§ 819 Abs. 1 › Kenntnis des Minderjährigen › …` | Zeile für Zeile | – |
| **I § 828 Abs. 3 BGB analog** `w828`–`ein2` | **Wortlautkarte** (vollständig), Marker „18. Lebensjahr“, „Einsicht“; 1971 Abs. 2; Einsicht (+); Till allein mit Namensschild | tabler:`book`, `ticket` | `Einsichtsfähigkeit: § 828 Abs. 3 BGB analog › …` | Zeile für Zeile | – |
| **J Ergebnis** `erg`–`rueck` | grüner Block, Haken Wertersatz, Kreuz Entreicherung, Rückflug GoA mit Fundstelle | tabler:`gavel`, `coins`, `plane-arrival` | `Ergebnis · …` | 6 | – |
| **K Klausurtipp** `tipp`–`tp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **L Prüfschema** `sch`–`c8` | breite Karte, I. (1.–3.), II. (1.–3.) | – | `Prüfschema › …` | 9 Aufbaustufen | – |
| **M Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Kopf/Mund der Sprecherfigur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („1968“, „17 Jahre“, „1.188 DM“, „§ 812 Abs. 1 Satz 1 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien (Orts-/Zeitwechsel Zwischenlandung → Kabine → New York → Zuhause); innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Treppe und Kabinenfenster aus Grundformen (`boden_()`, `treppe()`, `fenster()` in `folien_196.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> 1968: Der 17-jährige Till fliegt mit gültigem Ticket bis zu einer Zwischenlandung. Dort steigt er mit den Transitpassagieren wieder ein und fliegt ohne Ticket weiter nach New York. Er weiß, dass er für den Weiterflug kein Ticket hat. Die Maschine ist nicht ausgebucht.
>
> In New York wird ihm die Einreise verweigert, weil er kein Visum hat. Die Fluggesellschaft fliegt ihn noch am selben Tag zurück.
>
> Sie verlangt von Till den Preis für den Hinflug: 1.188 DM. Seine Mutter genehmigt keine Verträge ihres Sohnes mit der Fluggesellschaft. Till sagt: „Ich habe doch nichts gespart! Ohne den Gratisflug wäre ich nie geflogen.“
>
> **Muss Till den Hinflug nach New York bezahlen?**
