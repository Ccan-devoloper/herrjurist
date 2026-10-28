# Folge 135 · Vertragsverletzungsverfahren (Art. 258 AEUV): Das Prüfungsschema – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_135.py`](src/skript_135.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Öffentliches Recht/Europarecht, Themenplan-Format „Schema“. Einstieg mit dem **echten Nitrat-Fall** (EuGH, C-543/16) sachlich und nur so weit, wie im Volltext belegt; keine Landwirte als Figuren, Feld und Grundwasser als neutrale Icons. Rahmen: zwei fiktive Jurastudierende nehmen den Fall in der Lerngruppe als Klausur („Hat die Klage der Kommission Erfolg?“). Ablauf: Fall (Grundwasser) → Zeitleiste des Vorverfahrens → Lerngruppe/Frage → Sachverhalt → Verweis auf Folge 131 und Aufbau → Wortlaut Art. 258 → A. Zulässigkeit (1.–4.) → B. Begründetheit (Zurechnung, Pflicht, Befund, Rechtfertigung) → C. Urteil (Art. 260 Abs. 1, Wortlaut Abs. 2, Abs. 3, Nachgang 2019) → Ergebnis → Klausurtipp → Klausurschema → Merksatz. Hauptfilm 6:13,9 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Antonia (AN), um 24 | Jurastudentin, stellt die Klausurfrage, löst den Einwand | `standing/blazer-4` (Blazer Lila `#B8A9F5`, Oberteil Weiß, schwarze Hose), Kopf `Long`, Brille `Glasses 2`, Haut `#F0CDB4`; Mimiken `Calm` (ruhig, redet), `Suspicious` (denkt), `Smile` (froh), `Serious` (ernst), `Awe` (staunt) | `julia` (Frau, jung) |
| Konstantin (KO), um 25 | Jurastudent, wendet die Düngeverordnung 2017 ein | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`), Kopf `Short 3`, Haut `#B07552`, ohne Bart und Brille; Mimiken `Calm`, `Driven` (redet), `Suspicious`, `Smile`, `Awe`, `Serious` | `niklas` (Mann, jung) |
| Kommission, Deutschland, Gerichtshof | Parteien und Gericht des echten Falls | **keine Figuren** (EU-Tafel mit Sternen, Gerichtsgebäude als Icon); Bevollmächtigte und Richter des Urteils nicht genannt | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia); `helmut` und `ela_froh` nicht gebraucht. Vorfolge 131: hilde, lucy, christian – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt: 0 Treffer): **Antonia**, **Konstantin**. Verworfen: Greta (38 Treffer), Hannes (8), Merle (7), Carola (zu nah an „Carla“, der Erzählerin). Kein Genitiv eines Namens.
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Lerngruppe: Antonia links blickt nach rechts zu Konstantin, Konstantin rechts blickt nach links. Tafelszenen: Figuren rechts blicken zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AN_redet`, `KO_redet` (je beide Blickrichtungen) und Lexi. 44 Figuren-PNGs in `../peeps/op_135/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 131 (blazer-3, crossed_arms-1, shirt-3; Gericht, Baustofffirma, Kommission), 132 (robot_dance-3, easing-2, walking-3, shirt-2, shirt-1), 133 (resting-1, easing-1, blazer-2; Bank). 135: neue Schauplätze **Feld mit Grundwasser und Messstelle** (Querschnitt), **Zeitleiste Brüssel → Luxemburg** und **Lerngruppe am Tisch**; Posen `blazer-4`, `crossed_arms-2` in 131–133 nicht verwendet; keine Polka Dots, keine Prothesen-Posen. Die Lerngruppe kehrt beim Ergebnis zurück, weil dort die Klausurfrage beantwortet wird.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Grundwasser** `fall`–`zusatz` | Querschnitt: Ackerboden (Grundform), Grundwasser (Grundform), Pflanzen, Wassertropfen; Messstelle (Rohr + Reagenzglas); Pillen zum Wort | tabler `plant-2` (Grün), `wheat` (Gelb), `droplet` (Blau), `test-pipe` (Gelb), `file-certificate` (Blau) | `Fall · Nitrat im Grundwasser` → `· Messstellen: 50 mg/l oder mehr` → `· Nitratrichtlinie 91/676/EWG` → `· Reichen die Maßnahmen nicht?` | Grundbild · Messstelle · 50 mg/l · Richtlinie · Regeln · zusätzliche Maßnahmen | – |
| **A2 Zeitleiste** `bericht`–`klage` | EU-Tafel mit Sternen (Kommission, Brüssel), Zeitstrahl mit fünf Stationen zum Wort, Kreuz bei „nicht“ | tabler `stars`, `report-analytics`, `mail`, `file-text` (Gelb), `hourglass`; fluent-hc `classical-building` | `Fall · 2012: der Nitratbericht` → `· Das Vorverfahren` → `· Fristablauf am 11.9.2014` → `· Die Klage der Kommission, Oktober 2016` | 10 Stufen | – |
| **A3 Lerngruppe** `lern`–`ko1` | Bodenlinie, Tisch (Grundformen) mit Büchern; Klausurbogen wird abgelegt; Antonia links, Konstantin rechts; zwei Sprechblasen | tabler `books` (Rot), `file-text` (Weiß) | `Fall · Die Klausur in der Lerngruppe` → `· Die Klausurfrage` → `· Konstantin: die neue Düngeverordnung` | Grundbild · Bogen · Antonia redet · Konstantin redet | Blatt auf den Tisch (`szene_135papier_1`, Freesound CC0 379888) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C1 Aufbau** `verw`, `heute` | Tafel; Verweis auf das Video zu den Klagearten; drei Blöcke A/B/C zum Wort; beide Figuren rechts | – | `Prüfungsschema Art. 258 AEUV · Überblick: Video zu den Klagearten` → `· Aufbau` | 5 | – |
| **C2 Wortlaut Art. 258** `wl258`–`w258b` | **Wortlautkarte** (vollständig; Marker „Gelegenheit zur Äußerung“, „mit Gründen versehene Stellungnahme“, „gesetzten Frist“, „Gerichtshof der Europäischen Union anrufen“), drei Stufen-Pillen; Konstantin rechts | – | `Art. 258 AEUV · Wortlaut` → `· begründete Stellungnahme` → `· Frist und Klage` | Karte, 4 Marker, 3 Pillen | – |
| **D1 Zulässigkeit 1./2.** `zul`–`a259` | Tafel, Haken, zwei Partei-Kästen, Block Art. 259; Antonia rechts | – | `A. Zulässigkeit` → `› 1. Zuständigkeit des Gerichtshofs` → `› 2. Parteifähigkeit` → `› 2. Parteifähigkeit: Staatenklage, Art. 259` | Zeilen zum Wort | – |
| **D2 Vorverfahren** `vorv`–`nit3` | zwei Stufenkästen mit Pfeil, grüner Block „Streitgegenstand deckungsgleich“, Nitrat-Fall mit Haken | – | `A. Zulässigkeit › 3. ordnungsgemäßes Vorverfahren` → `› 3. deckungsgleicher Streitgegenstand` → `› 3. Vorverfahren im Nitrat-Fall` | Zeilen | – |
| **D3 Zeitpunkt, 4.** `zeit`–`zul2` | lila Block Fristablauf, Kreuz „spätere Änderungen“, Haken 4., grüner Block „zulässig“ | – | `› 3. maßgeblicher Zeitpunkt: Fristablauf` → `› 4. Klageart und Rechtsschutzbedürfnis` → `› Ergebnis: zulässig` | Zeilen | – |
| **E1 Begründetheit** `bgr`–`pfl` | Tafel, Kasten Länder, blauer Block Pflicht; Antonia rechts | – | `B. Begründetheit › Verstoß gegen Unionsrecht?` → `› Zurechnung: alle Stellen des Staates` → `› Pflicht aus Art. 5 Abs. 5 RL 91/676` | Zeilen | – |
| **E2 Befund** `eutro`, `prog` | Wellen-Icon, Kreuz „reichten nicht“, vier Mängel als Icon + Pille zum Wort | tabler `ripple`, `calendar`, `snowflake`, `mountain` (Grün), `building-warehouse` (Holz) | `› Maßnahmen reichten nicht` → `› Aktionsprogramm mangelhaft` | 7 | – |
| **E3 Rechtfertigung** `recht`–`bgr2` | zwei Einwände, Kreuze, roter Block, Zeile 2017, grüner Block „begründet“; Antonia (redet, Blase) und Konstantin rechts | – | `› Rechtfertigung durch Deutschland?` → `› keine Berufung auf innerstaatliche Gründe` → `› Düngeverordnung 2017: nach Fristablauf` → `› Ergebnis: begründet` | Zeilen, Blase | – |
| **F1 Urteil** `urt`, `fest` | Tafel, Haken, gelber Block, Hammer-Icon in der Tafel; Antonia rechts | tabler `gavel` (Holz) | `C. Urteil › Urteil vom 21.6.2018, C-543/16` → `› Feststellungsurteil, Art. 260 Abs. 1` | Zeilen | – |
| **F2 Art. 260** `wl260`–`danach` | **Wortlautkarte Art. 260 Abs. 2** (auszugsweise; Marker „Gerichtshof anrufen“, „Gelegenheit zur Äußerung“, „Pauschalbetrags oder Zwangsgelds“), lila Block Abs. 3, Zeile Nachgang 2019; Konstantin rechts | – | `› Art. 260 Abs. 2: zweites Verfahren` → `› Pauschalbetrag oder Zwangsgeld` → `› Art. 260 Abs. 3: schon im ersten Urteil` → `› Nitrat-Fall: Aufforderung 2019` | Karte, 3 Marker, Zeilen | – |
| **G Ergebnis** `erg`, `ko2` | zurück am Tisch der Lerngruppe; Pillen „zulässig“, „begründet“ mit Haken; Konstantin redet (Blase) | tabler `books`, `file-text` | `Ergebnis · Die Klage der Kommission hat Erfolg` | 4 | – |
| **H Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Streitgegenstand vergleichen` → `· Änderungen nach Fristablauf` | Zeile für Zeile | – |
| **I Klausurschema** `sch`–`sc2` | breite Karte, Gliederung A/B/C mit Unterpunkten Zeile für Zeile zum Wort | – | `Klausurschema` → `› A. Zulässigkeit` → `› B. Begründetheit` → `› C. Urteil` | 13 Aufbaustufen | – |
| **J Merksatz** `merke`–`m2` | Lexi erklärt (redet), vier Zeilen mit drei Markern | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen, Jahreszahlen als Ziffern („2017“). **Zahlen** auf Tafeln und Pillen als Ziffern („50 mg/l“, „11.9.2014“, „Art. 260 Abs. 2“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** ein Handlungsgeräusch (Klausurbogen auf den Tisch), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT; Gebäude, Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Grundwasser, Rohr, Tische und EU-Tafel aus Grundformen. Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nach der Nitratrichtlinie 91/676/EWG muss Deutschland Aktionsprogramme mit Regeln zum Düngen aufstellen und zusätzliche Maßnahmen treffen, sobald deutlich wird, dass sie nicht reichen. Im Nitratbericht von 2012 lag an rund der Hälfte der Messstellen des Belastungsmessnetzes der Nitratwert bei 50 mg/l oder darüber; die Wasserqualität hatte sich nach Ansicht der Kommission nicht verbessert.
>
> Die Kommission schickt im Oktober 2013 ein Mahnschreiben und im Juli 2014 eine begründete Stellungnahme mit einer Frist von zwei Monaten (bis 11.9.2014). Die angekündigte neue Düngeverordnung gilt bei Fristablauf nicht; ihr stimmt der Bundesrat erst 2017 zu. Im Oktober 2016 erhebt die Kommission Klage.
>
> **Hat die Klage der Kommission nach Art. 258 AEUV Erfolg?**
