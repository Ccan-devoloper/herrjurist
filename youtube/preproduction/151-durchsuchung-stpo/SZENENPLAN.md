# Folge 151 · Durchsuchung StPO: Wann darf die Polizei in meine Wohnung? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_151.py`](src/skript_151.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Strafrecht/StPO, Themenplan-Format „Schema“. Fall nach dem Plan-Hook („Nachts klingelt die Polizei ohne Beschluss und will wegen ‚Gefahr im Verzug‘ die Wohnung durchsuchen“): Dienstag, 23 Uhr, Verdacht der Hehlerei mit gestohlenen Fahrrädern; keine Gewalt, keine Waffen, kein Blaulicht, keine Abzeichen oder Wappen. Ablauf: Fall (Wohnungstür → Rückblick 14 Uhr auf der Wache → Flur) → Frage → Sachverhalt → 1. Art. 13 GG (Wortlautkarte; Verweis 020) → 2. § 102 (Wortlautkarte), § 103 als Kontrast (Wortlautkarte, Auszug) → 3. § 105 Abs. 1 S. 1 (Wortlautkarte) → 4. Gefahr im Verzug: BVerfGE 103, 142 (6 Punkte mit Rn.), Zitatkarte Rn. 39 (selbst herbeigeführt), Bereitschaftsdienst mit Tagesband (BVerfGE 151, 67) → 5. Nachtzeit § 104 (Wortlautkarte Abs. 1, 3) → 6. Lösung → 7. Verwertungsverbot (BGHSt 51, 285; Verweis 132) → Klausurtipp → Schema → Merksatz. Hauptfilm 6:33,4 (Begründung für mehr als fünf Minuten in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Helene (HE), um 30 | Wohnungsinhaberin, Verdacht der Hehlerei | Pose `standing/easing-1` (Strickjacke Lila `#B8A9F5` über weißem Shirt, schwarze Hose – Hauskleidung am späten Abend), Kopf `Long Curly`, Haut `#F2D0B4`; Mimiken `Calm`, `Concerned|Serious` (redet, sorgt sich), `Fear` (öffnet die Tür), `Suspicious`, `Solemn`, `Tired`, `Smile` | `lucy` (Frau, jung) |
| Polizeikommissar Steiger (ST), um 45 | Ermittlungsperson der Staatsanwaltschaft | Pose `standing/shirt-4` (dunkles Hemd, Hose Dunkelblau `#2F3E5C` – neutral wie Dienstkleidung, **ohne** Abzeichen, Wappen, Mütze oder Waffe), Kopf `Short 5`, Haut `#E8B894`, ohne Bart; Mimiken `Calm`, `Serious` (redet, ernst), `Suspicious`, `Solemn`, `Concerned|Serious` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, `_r` nach rechts (Steiger an der Tür und im Flur zu Helene). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HE_redet`, `ST_redet` (je links/rechts) und Lexi. Keine Bärte, keine Polka Dots, keine Prothesen-Posen, keine Karikatur. **Stimmen** nur aus dem Pool (lucy, stephan; christian nicht verwendet, also nie zusammen mit stephan). **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/` (grep über *.py, *.md, *.csv, *.json; „Greta“ wäre in 003 vergeben gewesen und wurde verworfen): **Helene**, **Steiger** (nie im Genitiv). Figuren-PNGs: `../peeps/op_151/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 148 (`robot_dance-3`, `walking-3`), 149 (`blazer-4`, `crossed_arms-2`), 150 (`shirt-3`, `blazer-3`) – in 151 keine dieser Posen; `easing-1` zuletzt in 145, `shirt-4` zuletzt in 143 (andere Figuren, Farben und Köpfe; die parallel entstehenden Folgen 152/153 nutzen sie ebenfalls – Hinweis an den Koordinator). Schauplätze neu: **Treppenhaus vor der Wohnungstür bei Nacht**, **Wache am Nachmittag** (Rückblick), **Flur der Wohnung bei Nacht** – keine Wiederholung gegenüber 148 (Parkplatz), 149 (Straße/Unfall), 150 (Wald/Behörde). **Nachtverlauf** in A1 und A3, weil der Fall in der Nachtzeit des § 104 StPO spielt (Pflichtpunkt); Prüfpfad dort weiß. Sonst Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Wohnungstür, 23 Uhr** `fall`→`st2` | Treppenhaus: Fliesenboden, Fenster mit Mond, Deckenlampe mit Lichtkegel, Wohnungstür; Klingel erscheint bei „Bei“; Tür öffnet sich (Öffnung wird hell) bei „Vor“, Helene steht davor; Steiger kommt bei „Polizeikommissar“; drei Blasen (Steiger, Helene, Steiger) | tabler:`door` (Holz, offen hellgelb), `bell-ringing` (Gelb), `window`, `bulb` (Gelb); Mond/Lichtkegel `ostil` | `Fall · Dienstag, 23 Uhr` (ab 0,0 s) → `· Es klingelt` → `· Polizeikommissar Steiger` → `· „Gefahr im Verzug“` → `· Wo ist der Beschluss?` → `· Ohne Beschluss` | leeres Treppenhaus · Klingel · Tür offen + Helene · Steiger · Blase 1 · Blase 2 · Blase 3 | Klingel (`szene_151klingel_1`), Tür (`szene_151tuer_1`) |
| **A2 Rückblick: Wache, 14 Uhr** `weiss`→`ahnt` | Schreibtisch mit Laptop, Steiger daneben; Pillen in Sprechreihenfolge; Rad im Inserat, Haus (Abholadresse), 7 Räder nacheinander, Kreuz „nicht bemüht“, Gericht + Telefon „Bereitschaftsdienst bis 21 Uhr erreichbar“, „kein Hinweis …“ | tabler:`device-laptop`, `clock-2`, `sun`, `home` (Lila), `building-bank` (Blau), `phone-call`; ph:`bicycle` | `Fall · Rückblick: 14 Uhr` → `· Die Anzeige` → `· Die Abholadresse` → `· 7 Räder in 3 Wochen` → `· Kein Beschluss beantragt` → `· Helene weiß von nichts?` | 10 Halte | – |
| **A3 Flur, Nacht** `wider`→`frage2` | Wohnungstür von innen, Lampe, E-Bike; Helene steht zuerst in der Tür und tritt bei „tritt“ zur Seite; Ring um das E-Bike; zwei Fragepillen | tabler:`door`, `bulb`; ph:`bicycle` | `Fall · Helene widerspricht` → `· Im Flur: das E-Bike` → `· Die Frage` | 6 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C 1. Art. 13 GG** `art13`→`gr020` | **Wortlautkarte Art. 13 Abs. 1, 2 GG** (Marker zum Wort), gelber Block Regel/Ausnahme mit Rn. 31, Verweis Folge 20; Helene, Steiger | tabler:`home`, `gavel`, `hourglass`, `scale` | `1. Art. 13 GG › …` (4 Stände) | 9 | – |
| **D 2. § 102** `p102`→`auff` | **Wortlautkarte § 102 StPO** (Marker Täter/Teilnehmer, Hehlerei, verdächtig, zu vermuten, Auffindung, Beweismitteln), Anfangsverdacht (StB 40/23 Rn. 11), zwei Haken; Helene | tabler:`book`, `user`, `search`, `file-search`, `home`; ph:`bicycle` | `Durchsuchung › 2. Ermächtigungsgrundlage › …` (6 Stände) | 13 | – |
| **E § 103** `p103`, `p103b` | **Wortlautkarte § 103 Abs. 1 S. 1** (Auszug), lila Block „Tatsachen statt bloßer Vermutung“, Rn. 14; Steiger | tabler:`users`, `list-check` | `… › § 103: andere Personen` → `… › § 103: Tatsachen nötig` | 7 | – |
| **F 3. § 105** `p105`→`kompet` | **Wortlautkarte § 105 Abs. 1 S. 1**, Haken „Steiger: Ermittlungsperson“, gelber Block „ohne Beschluss nur bei Gefahr im Verzug“; Steiger | tabler:`gavel`, `hourglass`, `file-x` | `Durchsuchung › 3. Anordnungskompetenz › …` (3) | 7 | – |
| **G 4. BVerfGE 103, 142** `bverfg`→`kontr` | sechs nummerierte Punkte mit Rn. (32, 34, 38, 40, 54, 44) | tabler:`building-bank`, `hourglass`, `list-check`, `phone-call`, `file-text`, `scale` | `Durchsuchung › 4. Gefahr im Verzug › …` (7) | 7 | – |
| **H selbst herbeigeführt** `selbst`, `zuw` | **Zitatkarte BVerfGE 103, 142, Rn. 39**, Kreuz „nicht warten …“; Steiger | tabler:`hourglass`, `clock` | `… › nicht selbst herbeigeführt` → `… › nicht abwarten` | 4 | – |
| **I Bereitschaftsdienst** `bereit`→`nacht` | Tagesband 0–24 Uhr (6–21 Uhr grün „Tag: Richter erreichbar“, Nacht), Rn. 40, BVerfGE 151, 67 Rn. 58; Helene | tabler:`building-bank`, `sun`, `moon` | `… › Bereitschaftsdienst › …` (3) | 7 | – |
| **J 5. § 104** `p104`→`ngiv` | **Wortlautkarte § 104 Abs. 1, 3** (Nr. 3 gekürzt), Marker in Sprechreihenfolge, gelber Block „schon das Warten bis zum Morgen …“ (BVerfGE 151, 67 Rn. 62) | tabler:`moon`, `clock`, `list-numbers`, `sun` | `Durchsuchung › 5. Nachtzeit, § 104 StPO › …` (4) | 11 | – |
| **K 6. Lösung** `loes`→`lerg` | Haken/Kreuze in Sprechreihenfolge, Blöcke „Gefahr im Verzug (−)“, „Die Durchsuchung war rechtswidrig.“ | tabler:`door`, `hourglass`, `clock-2`, `moon`, `gavel`; ph:`bicycle` | `6. Lösung › …` (8) | 10 | – |
| **L 7. Verwertungsverbot** `bvv`→`f132` | Abwägung, gelber Block bewusste/grobe Missachtung, BGH 2007, Haken, Kreuz „zählt nicht“, Verweis Folge 132 | tabler:`scale`, `eye-off`, `clock`, `file-x`, `gavel`, `book`; ph:`bicycle` | `7. Verwertungsverbot › …` (7) | 11 | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (4) | 8 | – |
| **N Schema** `sch`→`s6` | breite Karte I.–V. und Folge (roter Kasten) | – | `Prüfschema › …` (7) | 9 | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), drei Marker | – | `Merksatz` | 5 | – |

**Blasen:** Stil C (Standard seit 02.10.2026; Assertion gegen stillen Rückfall auf Stil E). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („23 Uhr“, „14 Uhr“, „7 teure Räder in 3 Wochen“, „bis 21 Uhr“, „6 bis 21 Uhr“, „Folge 20“, „Folge 132“); Wortlautkarten wörtlich (amtlich „daß“, „im Verzuge“ in Art. 13 GG).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung: Helene tritt zur Seite (A3).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (442280 Klingel, 648830 Tür; neu über die API ohne Schlüssel geladen), Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT, `bicycle` – das Tabler-Rad zeigt einen Fahrer), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Schreibtisch, Tagesband programmatisch; Mond und Lichtkegel aus `ostil.py`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Dienstag, 23 Uhr: Polizeikommissar Steiger, Ermittlungsperson der Staatsanwaltschaft, klingelt bei Helene. Er sagt, sie stehe im Verdacht, gestohlene Fahrräder zu verkaufen; wegen Gefahr im Verzug durchsuche er jetzt ihre Wohnung. Einen Beschluss hat er nicht.
>
> Schon um 14 Uhr hatte ein Mann angezeigt, dass sein gestohlenes E-Bike im Internet angeboten wird; Abholadresse ist die Wohnung von Helene. Über dasselbe Konto wurden in 3 Wochen 7 teure Räder angeboten. Um einen Beschluss hat sich Steiger nicht bemüht, obwohl der richterliche Bereitschaftsdienst bis 21 Uhr erreichbar war. Nichts deutet darauf hin, dass Helene von den Ermittlungen weiß.
>
> Helene widerspricht, tritt aber zur Seite. Im Flur steht das E-Bike.
>
> **Durfte Steiger durchsuchen? Darf das E-Bike als Beweis verwertet werden?**
