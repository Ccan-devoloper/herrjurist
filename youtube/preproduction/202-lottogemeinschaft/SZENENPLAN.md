# Folge 202 · Tippgemeinschaft ohne Tippschein: Gefälligkeitsverhältnis und Haftung – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_202.py`](src/skript_202.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/BGB AT, Klassiker-Fall. Hook nach Plan („Deine Tipprunde hätte gewonnen – aber der Kollege hat vergessen, den Schein abzugeben.“). Fiktiver Fall: Erna, Ulf und Gerold spielen als Tipprunde Lotto, je 5 € pro Woche; Gerold füllt ohne Entgelt den Lottoschein aus und gibt ihn ab, vergisst ihn einmal; mit ihren Zahlen hätte die Runde 12.000 € gewonnen; Ulf verlangt für sich und Erna je 4.000 €. Ablauf: Fall → Frage, Leitentscheidung → Sachverhalt → Anspruch § 280 Abs. 1 (Wortlautkarte § 241 Abs. 1 S. 1) → Rechtsbindungswille/Gefälligkeit (Kriterien, Verweis § 145) → BGH-Fall (§ 762 OLG, § 763) → was bindet (Gewinnverteilung, Einsätze; GbR offen; Leitsatz) → Gründe → Ausnahmen, Ergebnis → § 823 Abs. 1 (Wortlautkarte) → Abgrenzung Haftungsmaßstab (VI ZR 467/15) → zurück in der Teeküche → Klausurtipp → Prüfschema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gerold (HI), um 55 | gibt den Schein ab, vergisst ihn einmal; reumütig, kein Bösewicht | `standing/robot_dance-3` (Pullover Grün `#8FD694`, Hose Dunkelblau `#3D3D58`, weiße Schuhe, offene Hand), Kopf `Gray Short`, Brille `Glasses 4`, Haut `#E8B894`, kein Bart; Mimiken `Calm`, `Smile`, `Concerned\|Serious` (Sorge, redet), `Fear`, `Tired`, `Solemn`, `Serious`, `Suspicious` | `william` (Mann, älter) |
| Erna (EN), um 45 | Kollegin, merkt den entgangenen Gewinn | `standing/blazer-3` (Blazer Rot `#F07A6A` über schwarzem Oberteil, Hose Schiefer `#3F4A5A`), Kopf `Medium 3`, Haut `#C99470`; Mimiken `Calm`, `Smile` (redet in H), `Smile Big\|Smile` (freut sich, redet in A3), `Awe`, `Serious`, `Suspicious`, `Concerned\|Serious` | `sabrina` (Frau, mittel) |
| Ulf (UL), um 35 | Kollege, verlangt das Geld | `standing/shirt-4` (schwarzes Hemd, Hose Gelb `#F9D56E`; Blau nach Sichtung verworfen, weil Herr Tiemann in 200 Schwarz zu Hellblau trug), Kopf `Medium 1`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Serious` (redet), `Suspicious`, `Awe` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (william, sabrina, marc; `laura_ruhig` nicht gebraucht). Vorfolge 199 nutzte marc/laura_ruhig, 200 lucy/stephan; `marc` wiederholt sich gegenüber 199, weil der Pool nur zwei Männerstimmen enthält und Gerold (älter) `william` braucht.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags und in keinem Skript, Szenenplan, Rechtsstand, Abnahmebogen oder JSON unter `youtube/preproduction/` (Volltextsuche 06.10.2026; verworfen: Wilhelm (150, 155), Edith/Irene/Doris wegen möglicher englischer Lesart). Die erste Fassung hieß die Hauptfigur „Hilmar“; weil die parallel produzierte Folge 203 denselben Namen trägt (dort Hauptfigur), auf Weisung des Koordinators in **Gerold** umbenannt (in 160 und 203 wegen möglicher Lesart „Gerald“ verworfen, nie vergeben; Aussprache geprüft, siehe ABNAHME.md): Gerold, Erna, Ulf – nie im Genitiv. Namensschilder Erna Gelb, Ulf Blau, Gerold Grün.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. A1/A3/H: Erna und Ulf blicken nach rechts zu Gerold, Gerold nach links zu ihnen. A2: Gerold blickt nach links zu seinem Schreibtisch. Tafelszenen: beide blicken nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HI_klagt`, `EN_redet`, `EN_froh_redet`, `UL_redet` (je links/rechts) und Lexi. Figuren-PNGs `../peeps/op_202/` (80 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten Folgen nicht verwendet (197: easing-1, blazer-1; 198: easing-1, resting-1; 199: easing-2, pointing_finger-1; 200: shirt-3, resting-2, walking-1/2; 201 läuft parallel). Keine Polka Dots, keine Bärte, keine Prothesen-Posen (shirt-1/2, blazer-2 verworfen), keine Karikatur. Kleidung neu (grüner Pullover, roter Blazer, schwarzes Hemd zu gelber Hose; 199 orange Jacke, 198 lila Jacke/türkis, 200 Rosé).
- **Schauplätze neu:** Büro mit Schreibtisch, Laptop, Pflanze und Wanduhr (A1, A2), Fernseher mit gezogenen Zahlen (A2), Teeküche mit Küchenzeile, Kaffee und Tassen (A3, H). Lottoschein, Kugeln, Tisch und Küchenzeile aus Grundformen; **keine Lotterie-Marke, kein Logo, kein Produktname**, nur „Lottoschein“, „Annahmestelle“, „Ziehung“. Kein Werbeton: kein Jubel über Gewinne, der Gewinn erscheint als entgangen.
- Cremegrund durchgehend, Tageslicht („Am Abend“ nur als Pille, kein Nachtgrund).

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Die Tipprunde** `fall`–`gratis` | Büro (ab 0,0 s: Schreibtisch, Laptop, Pflanze, Uhr, leerer Lottoschein); „Tipprunde: hätte gewonnen“, „Schein vergessen“; Erna und Ulf erscheinen bei ihren Namen; „seit Jahren Lotto“; Gerold; zwei Münzen wandern zu Gerold, „je 5 € pro Woche“; Lottoschein mit Kreuzchen an Gerolds Hand, „feste Zahlen“, Annahmestelle; „ohne Entgelt“ | tabler:`device-laptop` (Hellblau), `plant-2` (Grün), `clock` (Weiß), `coin-euro` (Gelb), `building-store` (Hellblau); Schein und Tisch programmatisch | `Fall · Die Tipprunde` → `… Erna und Ulf` → `… Gerold spielt mit` → `… Jede Woche 5 € pro Kopf` → `… Gerold gibt den Schein ab` → `… ohne Entgelt` | ≈ 12 | `szene_202muenzen_1` (Freesound CC0 187144) beim Einsammeln |
| **A2 Samstag** `samstag`–`ziehung` | Gerold am Schreibtisch (müde), „Samstag“, „lange arbeiten“; Schein bleibt liegen („Schein vergessen“); Fernseher „Ziehung am Abend“, Kugeln 4 · 9 · 17 · 23 · 31 · 42, „12.000 € Gewinn – ohne Schein“ | tabler:`device-tv`; Kugeln programmatisch | `Fall · Samstag: Gerold arbeitet lange` → `… Der Schein bleibt liegen` → `… Die Ziehung am Abend` | ≈ 6 | `szene_202tastatur_1` (Freesound CC0 215745) beim Arbeiten am Laptop |
| **A3 Teeküche** `montag`–`bgh` | Küchenzeile, Kaffee, Tassen; Erna redet (Blase), Gerold redet (Blase), Ulf redet (Blase); Frage-Pillen; Leitentscheidung mit Fundstelle | tabler:`coffee`, `mug`, `clock` | `Fall · Montag in der Teeküche` → `… Erna: 12.000 € gewonnen` → `… Gerold: Schein nicht abgegeben` → `… Ulf: je 4.000 €` → `… Die Frage` → `… Der Lottogemeinschaft-Fall des BGH` | ≈ 12 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Anspruch** `ansp`–`frage3` | § 280 Abs. 1, Pflicht aus Schuldverhältnis; **Wortlautkarte § 241 Abs. 1 S. 1** (Marker „Schuldverhältnisses“, „Leistung“); Block „Schuldete Gerold das Einreichen?“ | tabler:`coin-euro`, `scale`, `ticket` | `Anspruch: § 280 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **D Vertrag oder Gefälligkeit?** `rbw`–`alltag` | Rechtsbindungswille (wie § 145), Gefallen, objektiver Beobachter, zwei Kriterien als Punkte, Block Gefälligkeit des täglichen Lebens, Fundstelle III ZR 346/14 Rn. 8 | tabler:`file-certificate`, `heart-handshake`, `eye`, `coin-euro`, `briefcase`, `coffee` | `Schuldverhältnis? › Rechtsbindungswille › …` | Zeile für Zeile | – |
| **E1 Der Fall des BGH** `urteil`–`p763` | Sachverhalt BGH (10.550 DM), Block OLG § 762, Kreuz „kein Spiel, Nebengeschäft“, Block § 763 | tabler:`ticket`, `dice-5`, `building-bank`, `gavel` | `BGH, 16.5.1974 – II ZR 12/73 › …` | Zeile für Zeile | – |
| **E2 Was bindet?** `bind`–`lsatz` | Haken Gewinnverteilung, Einsätze „können geschuldet sein“; GbR offengelassen (§ 705 n. F.); Leitsatz-Block | tabler:`users`, `coin-euro`, `question-mark`, `ticket` | `Lottogemeinschaft: was bindet? › …` | Zeile für Zeile | – |
| **F1 Gründe** `warum`–`niemand` | Abwägung, fünf Gründe als Punkte, Block „Niemand würde dieses Risiko übernehmen“ | tabler:`scale`, `alarm`, `moneybag`, `home-off`, `heart-handshake`, `clover`, `users` | `Rechtsbindungswille › Gründe des BGH › …` | Zeile für Zeile | – |
| **F2 Ausnahmen, Ergebnis** `anders`–`erg` | Block Entgelt/geschäftliche Zwecke, besondere Vereinbarung, Ergebnis-Block, Kreuz „Anspruch aus § 280 Abs. 1“ | tabler:`building-store`, `file-certificate`, `ticket-off` | `Rechtsbindungswille › Ausnahmen › …` → `Ergebnis · keine Pflicht, keine Pflichtverletzung` | Zeile für Zeile | – |
| **G1 Delikt** `delikt`–`verm` | **Wortlautkarte § 823 Abs. 1** (Marker auf den sechs Rechtsgütern zum gesprochenen Wort); Kreuz Gewinnchance, Vermögen als solches, Fundstelle III ZR 211/17 Rn. 19 | tabler:`shield-x`, `clover` | `Delikt: § 823 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **G2 Abgrenzung Haftungsmaßstab** `garten`–`still` | Nachbargarten/Wasserschaden, Block einfache Fahrlässigkeit (§ 276 Abs. 2), Haftungsbeschränkung nur ausnahmsweise, VI ZR 467/15 | tabler:`plant`, `bucket-droplet` | `Abgrenzung: Haftung bei Gefälligkeiten › …` | Zeile für Zeile | – |
| **H Teeküche** `leer`, `e2` | „leer ausgegangen“; Erna (froh) redet, Lottoschein auf der Küchenzeile | wie A3 | `Fall · Erna und Ulf gehen leer aus` → `Fall · Erna gibt ab jetzt den Schein ab` | 3 | – |
| **I Klausurtipp** `tipp`–`tp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **J Prüfschema** `sch`–`c7` | breite Karte, I. (1., Rechtsbindungswille, hier verneint, 2.), II. | – | `Prüfschema › …` | 9 Aufbaustufen | – |
| **K Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Kopf/Mund der Sprecherfigur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („5 €“, „12.000 €“, „4.000 €“, „10.550 DM“, „16.5.1974“, Paragrafen).
**Bewertungszeichen:** Haken/Kreuz nur bei gesprochener Bejahung/Verneinung (Gewinnverteilung bindend, „kein Spiel“, Gewinnchance kein Rechtsgut, Anspruch verneint, Klausurtipp); Kriterien und Gründe als neutrale Aufzählungspunkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Tisch, Küchenzeile, Lottoschein und Kugeln aus Grundformen (`folien_202.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Erna, Ulf und Gerold sind Kollegen und spielen seit Jahren als Tipprunde Lotto. Jede Woche zahlt jeder 5 € an Gerold. Gerold füllt den Lottoschein mit ihren festen Zahlen aus und gibt ihn in der Annahmestelle ab. Dafür bekommt er nichts.
>
> An einem Samstag muss Gerold lange arbeiten und vergisst den Schein. Am Abend wird gezogen: Mit ihren Zahlen hätte die Runde 12.000 € gewonnen.
>
> Am Montag sagt Gerold: „Ich habe den Schein diesmal nicht abgegeben.“ Ulf verlangt: „Dann schuldest du Erna und mir je 4.000 €.“
>
> **Muss Gerold den entgangenen Gewinn ersetzen?**
