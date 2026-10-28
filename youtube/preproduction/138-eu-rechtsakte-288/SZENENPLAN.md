# Folge 138 · EU-Rechtsakte Art. 288 AEUV: Verordnung, Richtlinie, Beschluss – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_138.py`](src/skript_138.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Öffentliches Recht/Europarecht, Themenplan-Format „Schema“. Hook nach dem Plan („Die DSGVO galt sofort überall, die Pauschalreiserichtlinie brauchte erst ein deutsches Gesetz – warum?“) als fiktive Mini-Szene im Reisebüro (Herr Stegemann, Frau Kettner). Kern als Schema/Übersicht: 1. Primär- und Sekundärrecht → 2. Art. 288 AEUV (Abs. 1 als Aufzählung, Abs. 2–5 als Wortlautkarte, vorgelesen) mit Verordnung (DSGVO, BDSG), Richtlinie (Pauschalreiserichtlinie, §§ 651a ff. BGB), Beschluss (Beihilfe, Art. 108 Abs. 2 AEUV), Empfehlung/Stellungnahme → 3. nicht umgesetzte Richtlinie (Ratti/Becker vertikal, Faccini Dori nicht horizontal, richtlinienkonforme Auslegung, Francovich, Dillenkofer) → Ergebnis im Reisebüro → Klausurtipp → Klausurschema als Tabelle → Merksatz. Hauptfilm 6:36,8 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Stegemann (ST), um 58 | führt ein kleines Reisebüro, stellt Pauschalreisen zusammen | `standing/resting-1` (Pullover Grün `#8FD694`, schwarze Hose aus der Pose), Kopf `No Hair 2` (Halbglatze), Brille `Glasses`, Haut `#E8B894`, ohne Bart. Mimiken `Calm`, `Smile` (froh), `Suspicious` (denkt; redet beim Fragen), `Smile` (redet froh im Ergebnis), `Awe` (staunt), `Solemn` (still) | `william` (Mann, älter) |
| Frau Kettner (KE), um 40 | seine Datenschutzbeauftragte | `standing/blazer-1` (Blazer in der Originalfarbe Pink, schwarzes Oberteil, Hose Schwarz, Prothese aus der Originalpose – keine Täterrolle), Kopf `Bun`, Haut `#C68E6A`, ohne Brille. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Awe` | `sabrina` (Frau, mittel) |
| Frau Faccini Dori, Herr Ratti, Frau Becker, Herr Dillenkofer, Herr Francovich | Kläger bzw. Beteiligte echter Fälle | **keine Figuren**, nur als Fallnamen (Tafel, Sprechtext) | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig); `laura_ruhig` (133, 136) und `marc` (136) nicht verwendet. Vorfolge 137: lucy, hilde – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt, 0 Treffer vor Produktionsbeginn): **Stegemann**, **Kettner**. Kein Genitiv eines Namens („Zurück zu Herrn Stegemann“).
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Reisebüro: Herr Stegemann links blickt nach rechts zu Frau Kettner, Frau Kettner rechts blickt nach links zu ihm. Tafeln: Figuren rechts blicken zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `ST_redet`, `ST_redetfroh`, `KE_redet` (je beide Blickrichtungen) und Lexi. 52 Figuren-PNGs in `../peeps/op_138/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 135 (blazer-4 lila, crossed_arms-2; Agrarbetrieb/Kommission), 136 (blazer-3 blau, robot_dance-2, pointing_finger-1), 137 (easing-2, shirt-3, resting-2). 138: **Reisebüro mit Schreibtisch, Bildschirm, Globus, Koffer und Reiseplakat** – neuer Schauplatz; Posen `resting-1` und `blazer-1` in 135–137 nicht verwendet; keine Polka Dots. Die parallel entstehende Folge 139 nutzt `robot_dance-3` und `pointing_finger-2` mit grauem Kurzhaar und Brille – deshalb wurde ein erster Entwurf (Stegemann in `robot_dance-3`, Kettner mit Korallen-Blazer) vor dem Render verworfen. Der Ergebnis-Halt (K) kehrt bewusst ins Reisebüro zurück, weil dort die Frage des Falls beantwortet wird.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Reisebüro** `fall`→`warum` | Bodenlinie, Schreibtisch (Grundformen) mit Bildschirm und Globus, Koffer, Reiseplakat (Rahmen + Flugzeug); Herr Stegemann links ab 0,0 s mit Namensschild; Tür rechts, Frau Kettner kommt; Ordner auf dem Tisch; zwei Sprechblasen; Frage-Pillen | tabler: `device-desktop` (Hellblau), `world` (Blau), `luggage` (Rot), `plane` (Hellblau), `door` (Holz), `folder` (Rot) | `Fall · Herr Stegemann und sein Reisebüro` → `· Frau Kettner, die Datenschutzbeauftragte` → `· Beides kommt aus der EU` → `· Die Frage` | Grundbild · Pauschalreisen/froh · Tür/Kettner · Ordner · Kettner redet · Stegemann redet · 4 Frage-Pillen mit Mimikwechseln | Klopfen beim Erscheinen der Tür (`szene_138tuer_1`, Freesound CC0 193833), Ordner auf dem Tisch (`szene_138ordner_1`, CC0 484897) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Ebenen** `ebene`→`formen` | Tafel, zwei Kästen (Primär-/Sekundärrecht) mit Pfeil, grüner Block; beide Figuren rechts | – | `1. Primär- und Sekundärrecht` → `› Primärrecht: die Verträge` → `› Sekundärrecht: Rechtsakte der Organe` → `› Formen: Art. 288 AEUV` | Zeilen zum Wort, Mimik | – |
| **D Art. 288 im Wortlaut** `abs1`→`abs5` | Abs. 1: fünf Pillen zum Wort; **Wortlautkarte Abs. 2–5**, Absatz für Absatz zum Vorlesen, Textmarker an den Merkmalen; rechts Pille + Requisit je Absatz | tabler: `books`, `file-certificate` (Blau), `target` (Grün), `mail` (Gelb), `message-circle` | `2. Art. 288 AEUV › Abs. 1: fünf Handlungsformen` → `› Abs. 2: Verordnung` → … `› Abs. 5: Empfehlung, Stellungnahme` | 5 Pillen, 4 Absätze, 8 Marker, 5 Requisiten | – |
| **E Verordnung** `vo`→`bdsg` | Tafel, drei Haken (allgemein/vollständig/unmittelbar), Zitat Art. 99 DSGVO mit Marker, lila Kasten BDSG; Frau Kettner rechts | – | `› Verordnung: allgemein, vollständig, unmittelbar` → `› Verordnung: Beispiel DSGVO` → `› Verordnung: das BDSG ergänzt nur` | Zeilen, Haken, Marker, Mimik | – |
| **F Richtlinie** `rl`→`bgb` | Tafel, gelber Kasten Pauschalreiserichtlinie (Fristen), grüner Block BGB; Herr Stegemann rechts, Koffer | tabler: `luggage` (Rot) | `› Richtlinie: verbindlich nur das Ziel` → `› Wahl der Form und der Mittel` → `› Umsetzungsfrist` → `› Umsetzung im BGB` | Zeilen, Mimik | – |
| **G Beschluss, Empfehlung** `be`→`empf` | Tafel, gelber Kasten Beihilfebeispiel mit Haken, roter Block mit Kreuz; rechts Pille + Requisit | tabler: `mail` (Gelb), `building-bank` (Blau), `message-circle` | `› Beschluss: bindet seine Adressaten` → `› Beispiel Beihilfe` → `› Empfehlung, Stellungnahme: nicht verbindlich` | Zeilen, Haken, Kreuz | – |
| **H Vertikal** `prob`→`vert` | Tafel (Ratti/Becker), zwei Haken, grüner Block; rechts Schema Staat oben, Einzelner unten, grüner Pfeil „vertikal“ | tabler: `building-bank` (Blau), `id` (Ausweis, Gelb) | `3. Nicht umgesetzte Richtlinie › Frist abgelaufen` → `› kein Berufen auf das eigene Versäumnis` → `› unbedingt und hinreichend genau` → `› vertikale unmittelbare Wirkung` | Zeilen, Haken, Icons, Pfeil | – |
| **I Horizontal** `horiz`→`fd3` | Tafel Faccini Dori, Kreuze; rechts Verbraucherin – Unternehmen mit Linie, Kreuz bei „nicht stützen“ | tabler: `language` (Hellblau), `shopping-bag` (Gelb), `building-store` | `› keine Wirkung zwischen Privaten` → `› Faccini Dori, EuGH 1994` → `› kein Widerruf aus der Richtlinie gegen Private` | Zeilen, Icons, Kreuze | – |
| **J Auswege** `ausw`→`qual` | Tafel: 1. richtlinienkonforme Auslegung, 2. Francovich mit drei Haken, blauer Kasten Dillenkofer; Herr Stegemann rechts mit Pille + Requisit | tabler: `scale`, `coins`, `luggage-off` | `› zwei Auswege` → `› Ausweg 1: richtlinienkonforme Auslegung` → `› Ausweg 2: Staatshaftung nach Francovich` → `› Staatshaftung: Dillenkofer, EuGH 1996` | Zeilen, Haken, Mimik | – |
| **K Ergebnis** `erg`→`s2` | zurück im Reisebüro: Ergebnis-Pillen, dann Sprechblase Herr Stegemann (froh) | wie A | `Ergebnis · Verordnung gilt unmittelbar, Richtlinie braucht Umsetzung` | 3 Pillen, Mimik, Blase | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet), drei Prüffragen, gelber Block | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst die Umsetzungsfrist` → `· Staat oder Privater?` | Zeile für Zeile | – |
| **M Klausurschema** `sch`→`z4c` | breite Karte als **Tabelle**: Spalten Verordnung/Richtlinie/Beschluss, Zeilen I.–IV., Zelle für Zelle | – | `Klausurschema` → `› I. verbindlich?` → `› II. für wen?` → `› III. Umsetzung nötig?` → `› IV. Beispiele` | 17 Aufbaustufen | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln und Pillen als Ziffern („25.5.2018“, „1.1.2018“, „§§ 651a ff.“, „Art. 288 AEUV“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Klopfen, Ordner), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Schreibtisch und Plakatrahmen aus Grundformen. Kein Mensch als Icon: Einzelner und Verbraucherin erscheinen in H/I nur als Gegenstandssymbole (Ausweis, Einkaufstasche), weil die Verbraucherin im Fall Faccini Dori eine reale Person ist und nicht als Figur gezeigt wird.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Stegemann führt ein kleines Reisebüro und stellt dort auch Pauschalreisen zusammen. Frau Kettner, seine Datenschutzbeauftragte, erklärt ihm: Für seine Kundendaten gilt die Datenschutz-Grundverordnung unmittelbar, wie in jedem Mitgliedstaat.
>
> Herr Stegemann wundert sich: Sein Pauschalreiserecht steht im BGB und nicht in der EU-Richtlinie.
>
> Die Datenschutz-Grundverordnung galt ab dem 25.5.2018 unmittelbar in allen Mitgliedstaaten. Die Pauschalreiserichtlinie brauchte dagegen erst ein deutsches Gesetz.
>
> **Warum gilt die eine unmittelbar – und die andere erst über ein deutsches Gesetz?**
