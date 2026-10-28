# Folge 236 · Schadensersatz Kaufrecht § 437 Nr. 3 BGB: Welche Anspruchsgrundlage? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_236.py`](src/skript_236.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Kaufrecht · Schema. Hook nach Plan („Das gekaufte Heizgerät ist defekt und setzt nach einer Woche den Keller in Brand.“). Fiktiver Fall: Katharina kauft für ihren Hobbykeller im Elektrogeschäft von Raimund ein Heizgerät für 600 €, original verpackt vom Hersteller; eine Woche später schmort ein Bauteil durch, Rauch, Regal angebrannt, Wand verrußt, niemand verletzt, Kellerschaden 4.000 €; Fehler ab Werk, für Raimund nicht erkennbar; Katharina verlangt ein neues Gerät und 4.000 €, Raimund bietet das Gerät an und lehnt das Geld ab.
Ablauf: Fall (Kauf, Keller, Forderung/Antwort) → Frage → Sachverhalt → A. § 437 Nr. 3 (Wortlautkarte) als Rechtsgrundverweisung, Sachmangel → B. Kontrollfrage (Lehre; BGH VIII ZR 169/12 Rn. 26 f.) mit Subsumtion Gerät/Keller → C. die passende Norm: 1. behebbar §§ 280 I, III, 281 (Frist, Ausnahmen §§ 281 II, 440, beim Verbrauchsgüterkauf § 475d; Verweis 209) – 2. nachträglich unbehebbar § 283 (Wortlautkarte) – 3. anfänglich unbehebbar § 311a II (Wortlautkarte) – 4. Mangelfolgeschaden § 280 I ohne Frist (BT-Drucks. 14/6040 S. 225) – Verzögerungsschaden §§ 280 II, 286 → D. Vertretenmüssen des Händlers (V ZR 93/08 Rn. 19; VIII ZR 211/07 Rn. 29) – Hersteller (ProdHaftG, § 823 I; Verweis 070) → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:24,3 (5.673 gesprochene Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Katharina (KA), um 35 | Käuferin, Verbraucherin | `standing/crossed_arms-2` (schwarzes Oberteil der Pose, Hose Lila `#B8A9F5`, schwarze Schuhe), Kopf `Long Curly`, Haut `#EAC1A0`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile`, `Concerned\|Serious` (auch redet), `Fear`, `Serious`, `Suspicious`, `Tired`, `Awe` | `lucy` (Frau, jung) |
| Raimund (RM), um 50 | Inhaber eines Elektrogeschäfts, Verkäufer, Händler (nicht Hersteller); freundlich, kein Bösewicht | `standing/blazer-3` (Sakko Blau `#8DB3F2`, schwarzes Oberteil der Pose, Hose Grau `#8A8F99`), Kopf `Short 5`, Brille `Glasses 3`, Haut `#D9A47E`, kein Bart; Mimiken `Calm` (auch erklärt), `Smile` (auch redet), `Concerned\|Serious`, `Suspicious`, `Solemn`, `Awe`, `Fear`, `Smile Big\|Smile` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (stephan, hilde, christian, lucy); stephan und lucy, christian nicht verwendet (keine Szene mit stephan und christian). 177 nutzte hilde/christian, 209 andere Stimmen.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags, nicht in `namen_reserviert.txt` der parallelen Folgen und in keinem `.py/.md/.json/.txt/.csv` unter `youtube/` (Volltextsuche 07.10.2026: Katharina 0, Raimund 0 Treffer; verworfen: Ortwin, Henrike, Arnulf, Reinald – schon verwendet, Hannes/Wilhelm/Lothar – schon verwendet). Reserviert als „236: Katharina, Raimund“. Nie im Genitiv (Skript-Assertion). Namensschilder Katharina Blau, Raimund Grün, Lexi Gelb.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fallszenen im Laden: Raimund links (x 1180) blickt nach rechts zu Katharina, Katharina rechts (x 1650) blickt nach links; Keller: Katharina rechts blickt nach links zum Heizgerät. Tafelszenen: beide nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `KA_redet`, `RM_redet`, `RM_erklaert` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild (der Hersteller nur als Fabrik-Symbol). Figuren-PNGs `../peeps/op_236/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten Folgen nicht verwendet (231: walking-2, robot_dance-3; 232: resting-1, easing-1, crossed_arms-1; 233: easing-1, blazer-4, pointing_finger-1, sitting/bike, resting-2; 235: walking-3, blazer-4); robot_dance-1 bleibt Lexi; Prothesen-Posen verworfen; keine Polka Dots, keine Bärte. Kleidung neu: schwarz/lila (Katharina), blaues Sakko/grau (Raimund).
- **Schauplätze neu:** Elektrogeschäft (Wandregal mit zwei Heizgeräten, Mikrowellen, Glühbirne – Tabler `microwave`, `bulb`, Heizgeräte als Grundform), Hobbykeller (graue Wand, Kellerfenster, Regal mit Kisten – Tabler `package`), Heizgerät als programmatischer Ölradiator ohne Marke. Gegenüber 209 (Reifenhandel, Carport), 215, 177 (Druckerei) neu.
- **Darstellung Brand:** nur Rauchwolken (Tabler `cloud`, grau) und Brandflecken (weiche Rußflächen) an Regal, Wand und Gerät; kein Feuer, keine Verletzten. Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Der Kauf** `fall`–`ra1` | ab 0,0 s Laden mit Regal und Ware; Hook-Pillen „Heizgerät defekt“, „setzt den Keller in Brand“; Katharina bei ihrem Namen; Raimund bei „Raimund“; „Elektrogeschäft von Raimund“; Heizgerät bei „Heizgerät“, „Heizgerät: 600 €“; Karton und „original verpackt vom Hersteller“; Blase Raimund „Bitte schön, Ihr neues Heizgerät. / Viel Freude damit!“ | tabler:`microwave`, `bulb`, `package`; Heizgerät (Grundform) | `Fall · Das Heizgerät` → `… Der Kauf im Elektrogeschäft` → `… Original verpackt vom Hersteller` → `… Raimund übergibt das Gerät` | `szene_236karton_1` beim Wort „verpackt“ |
| **A2 Im Keller** `woche`–`erkenn` | Keller, Regal mit Kisten, Heizgerät; „1 Woche später“; kleine Rauchwolke bei „durch“; Rauch bei „qualmt“, Gerät verrußt; Brandfleck am Regal bei „Regal“, an der Wand bei „Wand“; „niemand verletzt“, „Kellerschaden: 4.000 €“; Fabrik-Symbol „Bauteil ab Werk fehlerhaft“ → „Fehler des Herstellers“; „für Raimund nicht erkennbar“; Katharina ruhig → erschrocken → besorgt → nachdenklich | tabler:`package`, `cloud`, `building-factory` | `Fall · Eine Woche später` → `… Rauch im Keller` → `… Schaden 4.000 €` → `… Fehler des Herstellers` → `… Für Raimund nicht erkennbar` | `szene_236schmoren_1` beim Wort „durch“ |
| **A3 Forderung, Antwort, Frage** `ka1`–`frage2` | Laden, verrußtes Gerät zwischen beiden; Blase Katharina (3 Zeilen) „Ihr Heizgerät hat meinen Keller / verrußt! Ich will ein neues Gerät / und 4.000 € für den Schaden.“; Blase Raimund „Ein neues Gerät bekommen Sie. / Aber für den Fehler des / Herstellers kann ich nichts.“; Pillen der Frage | – | `Fall · Katharina: neues Gerät und 4.000 €` → `… Raimund: neues Gerät ja, Geld nein` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (35 px), ≈ 10 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 437 Nr. 3** `agl`–`sys` | **Wortlautkarte § 437 (Auszug)** mit Markern (Voraussetzungen, vorliegen, 3., Schadensersatz, 311a); Block Rechtsgrundverweisung; ✓ Mangel (§ 434 Abs. 1, 3 Satz 1 Nr. 1), ✓ schon bei Übergabe (§ 446 Satz 1); Verweis 046 | tabler:`scale`, `file-text`, `route`, `alert-triangle` | `A. Anspruchsgrundlage › …` | – |
| **D Kontrollfrage** `kf`–`kf6` | Block Kontrollfrage (Lehre/Klausurformel), Blöcke ja/nein, BGH-Satz mit Fundstelle; ✓ Gerät → statt, ✓ Keller → neben | tabler:`help-circle`, `refresh`, `replace`, `home-x` | `B. Kontrollfrage › …` | – |
| **E1 Wege 1 und 2** `wege`–`t2b` | „1. Mangel behebbar“, §§ 280 Abs. 1, 3, 281; Ausnahmen §§ 281 II, 440, § 475d; Verweis 209; „2. unbehebbar, Hindernis nach Vertragsschluss“; **Wortlautkarte § 283 Satz 1**; „keine Frist“ | tabler:`arrows-split`, `tool`, `hourglass`, `hourglass-off`, `ban` | `C. Die passende Norm › 1. … › 2. …` | – |
| **E2 Wege 3 und 4** `t3`–`t5b` | „3. schon bei Vertragsschluss unbehebbar“, **Wortlautkarte § 311a Abs. 2 Satz 1, 2** (Marker nicht kannte, Unkenntnis, vertreten); „4. Mangelfolgeschaden, etwa am Keller“, § 280 Abs. 1 allein, BT-Drucks.; Block Verzögerungsschaden/Verzug | tabler:`file-text`, `user-question`, `home-x`, `scale`, `clock` | `C. Die passende Norm › 3. … › 4. … › Verzögerungsschaden …` | – |
| **F Vertretenmüssen** `vm`–`vm7` | Zeile „Auch beim Keller …“; Block vermutet; Punkte keine Untersuchungspflicht (V ZR 93/08 Rn. 19), Hersteller kein Erfüllungsgehilfe (VIII ZR 211/07 Rn. 29), anders etwa Garantie/Anhaltspunkte; Fall; ✗ „mangelhafte Lieferung nicht zu vertreten“ | tabler:`user-question`, `scale`, `zoom-cancel`, `building-factory`, `certificate`, `package`, `circle-x` | `D. Vertretenmüssen › …` | – |
| **G Hersteller** `ph`, `ph2` | Punkte § 1 ProdHaftG, § 823 Abs. 1 BGB; Verweis 070; Katharina allein mit Namensschild | tabler:`building-factory` | `D. Vertretenmüssen › Keller: Anspruch gegen den Hersteller` | – |
| **H Ergebnis** `erg`–`erg4` | Laden; Pillen „Gerät: Schadensersatz statt der Leistung“, „Vorrang: Nacherfüllung, neues Gerät“ (verrußtes Gerät → neues Gerät bei „neue“), „Keller: § 280 Abs. 1 BGB, ohne Frist“, „Raimund: nichts zu vertreten“, Fabrik „4.000 € beim Hersteller“ | tabler:`building-factory` | `Ergebnis · …` | – |
| **I Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **J Klausurschema** `sch`–`k5` | breite Karte, Anspruchsgrundlage, 1.–5., jede Zeile zum Wort | – | `Klausurschema › …` | – |
| **K Merksatz** `merke`–`mk4` | Lexi erklärt (redet), vier Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund, wortgleich mit dem Gesprochenen, Zahlen in Ziffern („4.000 €“).
**Bewertungszeichen:** Haken nur bei gesprochener Bejahung (Mangel, Übergabe, Zuordnung Gerät/Keller), Kreuz bei „nicht zu vertreten“; Normen und Hinweise als neutrale Punkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Laden, Keller, Regale, Heizgerät, Brandflecken aus Grundformen (`folien_236.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Katharina kauft für sich privat im Elektrogeschäft von Raimund ein Heizgerät für ihren Hobbykeller, Preis 600 €. Raimund hat das Gerät original verpackt vom Hersteller bezogen.
>
> Eine Woche später schmort im Gerät ein Bauteil durch. Es qualmt, ein Regal brennt an, die Wand ist verrußt. Verletzt wird niemand; der Schaden im Keller beträgt 4.000 €. Das Bauteil war schon ab Werk fehlerhaft, ein Fehler des Herstellers. Für Raimund war das nicht erkennbar.
>
> Katharina verlangt von Raimund ein neues Gerät und 4.000 € für den Schaden. Raimund antwortet: „Ein neues Gerät bekommen Sie. Aber für den Fehler des Herstellers kann ich nichts.“
>
> **Was kann Katharina verlangen, und muss Raimund für den Keller zahlen?**
