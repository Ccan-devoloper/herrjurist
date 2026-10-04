# Folge 177 · Schadensersatz neben der Leistung oder statt? Die eine Kontrollfrage – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_177.py`](src/skript_177.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Schuldrecht AT, Themenplan-Format „Abgrenzung“. Fall nach dem Plan-Hook („Ein defekter Chip zerstört eine bis dahin intakte Steuerungseinheit – was ersetzt welcher Anspruch?“): Elfriede (Druckerei) kauft bei Dietrich, der Steuerchips selbst herstellt, einen Chip zum Nachrüsten ihrer Druckmaschine für 300 €. Der Chip überhitzt (Fertigungsfehler) und zerstört die bis dahin einwandfreie Steuerungseinheit; drei Tage Stillstand. Posten: 1. Chip 300 €, 2. Steuerungseinheit 6.000 €, 3. entgangener Gewinn 4.500 €; keine Frist gesetzt.

Ablauf: Fall (Kauf, Schaden, Streit, drei Posten) → Frage → Sachverhalt → Grundtatbestand § 437 Nr. 3, § 280 Abs. 1 (Wortlautkarte; Verweis 046) → Grundtatbestand im Fall (Kaufvertrag, Sachmangel, § 377 HGB, Vertretenmüssen, Händler-Hinweis) → statt der Leistung: § 280 Abs. 3, § 281 Abs. 1 Satz 1 (Wortlautkarten; Frist als letzte Chance) → Die Kontrollfrage (Lehre/Klausurformel, BGH mit Rn.) → Posten 1 Chip (statt, Frist fehlt) → Posten 2 Steuerungseinheit (neben) → Posten 3 Produktionsausfall (neben, BGH V ZR 93/08; Verzögerungsschaden §§ 280 Abs. 2, 286 mit Verweis 112) → Lösungstabelle → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:54,7 (5.139 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Elfriede, um 60 | Inhaberin einer Druckerei, Käuferin | `standing/blazer-3` (Blazer Lila `#B8A9F5`, schwarzes Oberteil der Pose, Hose Dunkelblau `#2E3550`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0CDB0`; Mimiken `Calm`, `Serious` (bestimmt, redet), `Concerned|Serious`, `Awe`, `Suspicious`, `Smile`, `Smile Big|Smile` | `hilde` (Frau, älter) |
| Dietrich, um 50 | stellt Steuerchips her und verkauft sie, Verkäufer | `standing/robot_dance-2` (schwarzes Oberteil der Pose, Hose Khaki `#C9A27A`, ausgestreckte Hand), Kopf `Short 4`, keine Brille, Haut `#D9A07A`; Mimiken `Calm`, `Smile` (redet), `Concerned|Serious`, `Suspicious`, `Serious`, `Tired`, `Smile Big|Smile` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle `.py/.md/.json` in `youtube/preproduction`: 0 Treffer für „Elfriede“ und „Dietrich“; gegen die Koordinatorliste und die parallel laufenden Folgen 175/176 geprüft). Verworfen: Gerhard, Hubert (bereits in Dateien genannt). Kein Genitiv eines Namens im Sprechtext; die Figuren nennen keine Namen.
- **Stimmen nur aus dem Pool:** `hilde` (Elfriede, älter, bestimmt) und `christian` (Dietrich, freundlich-abwehrend). `stephan` nicht besetzt (also kein Dialog stephan/christian), `lucy` (jung) passt nicht zur Inhaberin um 60. Vorfolge 176: ela_froh/helmut/niklas – keine Überschneidung.
- Präfixe `EL_`/`DI_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen blickt Elfriede nach rechts zu Dietrich (`_r`), Dietrich nach links zu ihr; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EL_bestimmt`, `DI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Karikatur. **Keine weiteren Menschen im Bild** (der Techniker wird nur erwähnt, sichtbar ist das Werkzeug-Icon am Steckplatz).
- **Abwechslung:** Posen nicht aus 174 (`crossed_arms-1`, `resting-2`, `shirt-4`, `crossed_arms-2`), 175 (`easing-1`, `pointing_finger-1`), 176 (`blazer-1`, `pointing_finger-2`) und nicht wie 170 (`robot_dance-3`, `blazer-2`); keine Polka Dots. Figurenrezepte verglichen.
- Figuren-PNGs: `../peeps/op_177/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 176 (Warenverkehr/Grenze), 175 (Klinik), 174 (Konto/Lohn), 170 (Garage). Hier neu: **Druckerei** mit programmatischer Druckmaschine (Gehäuse Blau, Walzenhaube mit zwei gelben Walzen, Papierablage) und eigener **Steuerungseinheit** (Bildschirm grün → grau mit Rissen und Rauch) mit Chip-Steckplatz (Tabler `cpu`). Leitmotiv: drei Posten mit Ziffern 1–3 und gleicher Tafelstruktur. Cremegrund durchgehend.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Der Kauf** `fall`–`einbau` | ab 0,0 s: Druckmaschine, Elfriede mit Namensschild; Dietrich erscheint bei „Dietrich“, hält bei „Chip“ den Chip; Pillen „Druckerei“, „stellt Steuerchips selbst her“, „Chip zum Nachrüsten: 300 €“, „Techniker setzt ihn ein“ zum Wort; bei `einbau` Chip im Steckplatz, Werkzeug | tabler:`cpu` (Grün), `tool` (Grau); Maschine programmatisch | `Fall · Der Kauf` | – |
| **A2 Schaden und Streit** `heiss`–`di1` | bei „überhitzt“ Chip rot + Thermometer, Pille „Chip fehlerhaft: überhitzt“; bei „zerstört“ Steuerungseinheit grau mit Rissen, Rauch, Pille; „3 Tage Stillstand“ + Uhr; „Fehler am selben Tag gemeldet“; Blasen Elfriede „Meine Maschine stand / 3 Tage still! Sie zahlen / mir alles, und zwar sofort.“, Dietrich „Ich schicke Ihnen gern / einen neuen Chip. Aber / zahlen werde ich nichts.“ | tabler:`cpu` (Rot), `temperature` (Rot), `cloud-fog`, `clock-pause` (Gelb) | `Fall · Der Schaden` → `Fall · Der Streit` | `szene_177funken_1` bei „zerstört“ |
| **A3 Drei Posten / Frage** `pos`–`frage2` | Tafel „Elfriede verlangt drei Posten“: 1 Chip 300 €, 2 neue Steuerungseinheit 6.000 €, 3 entgangener Gewinn 4.500 € je zum Wort; ✗ „keine Frist gesetzt“; Pillen „Welcher Posten – welcher Anspruch?“, „Wofür braucht sie eine Frist?“ | tabler:`list-numbers`, `cpu`, `settings-automation`, `clock-pause`, `hourglass`, `zoom-question` | `Fall · Drei Posten` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 280 Abs. 1** `agl`–`g046` | Zeile „Beim Kauf: § 437 Nr. 3 BGB führt ins allgemeine Schuldrecht“; Wortlautkarte mit Markern „Pflicht aus dem Schuldverhältnis“, „Ersatz des hierdurch entstehenden“, „nicht zu vertreten“; Block „Mehr dazu: Video „Das System der §§ 280 ff.““ | tabler:`file-text`, `scale`, `list-numbers` | `Grundtatbestand › § 437 Nr. 3 BGB` → `› § 280 Abs. 1 BGB` | – |
| **D Grundtatbestand im Fall** `gt1`–`gt5` | ✓ Kaufvertrag; ✓ Sachmangel (§ 434); ✓ Pflichtverletzung (§ 433 Abs. 1 Satz 2); ✓ § 377 HGB; ✓ Vertretenmüssen vermutet, keine Entlastung; Block „Bloßer Händler: Verschulden des Herstellers wird ihm nicht zugerechnet“ mit Rn. | tabler:`file-text`, `temperature`, `phone`, `scale`, `building-factory-2` | `Grundtatbestand › Schuldverhältnis` → `› Pflichtverletzung` → `› Rüge, § 377 HGB` → `› Vertretenmüssen` | – |
| **E Statt der Leistung** `w3`–`sinn` | Wortlautkarten § 280 Abs. 3 (Marker „zusätzlichen Voraussetzungen“, „des § 281“) und § 281 Abs. 1 Satz 1 (Marker „erfolglos“, „angemessene Frist“, „Leistung oder Nacherfüllung“); Block „Frist: letzte Chance für den Verkäufer“ mit Rn. | tabler:`list-numbers`, `hourglass`, `refresh` | `Statt der Leistung › § 280 Abs. 3 BGB` → `› § 281 Abs. 1 Satz 1 BGB` | – |
| **F Die Kontrollfrage** `kf`–`kf4` | „Lehre, Klausurformel“; Block (blau) „Würde eine ordnungsgemäße Nacherfüllung im letztmöglichen Zeitpunkt den Schaden noch beseitigen?“; gelb „ja: statt der Leistung, grundsätzlich nur nach Frist“; grün „nein: neben der Leistung, ohne Frist“; „BGH: ob eine Nacherfüllung den Schaden beseitigen würde“ mit Rn. | tabler:`zoom-question`, `hourglass`, `plus`, `scale` | `Die Kontrollfrage` → `› ja: statt …` → `› nein: neben …` → `› BGH` | – |
| **G Posten 1** `a1`–`a1x` | gleiche Tafel: Kontrollfrage „Beseitigt ein fehlerfreier Chip den Schaden?“ ✓ „ja, dieser Schaden ist weg“; Anspruchsgrundlage gelb „statt der Leistung: §§ 280 Abs. 1, 3, 281 BGB“; ✗ „ohne Frist kein Geld“; „zuerst Nacherfüllung verlangen und Frist setzen“; „Ausnahmen: § 281 Abs. 2, § 440 BGB“ | tabler:`cpu`, `hourglass` | `Posten 1: Chip › Kontrollfrage` → `› statt der Leistung` → `› Frist` | – |
| **H Posten 2** `b1`–`b1s` | gleiche Tafel: „Repariert ein neuer Chip die Steuerungseinheit?“ ✗ „nein, der Schaden bliebe“; grün „neben der Leistung: § 280 Abs. 1 BGB“ (vgl. VII ZR 63/18, BT-Drucks. S. 224); ✓ „6.000 € für Elfriede, ohne Frist“ | tabler:`settings-automation`, `cpu`, `plus`, `coin-euro` | `Posten 2: Steuerungseinheit › Kontrollfrage` → `› neben der Leistung` | – |
| **I Posten 3** `c1`–`c1v` | gleiche Tafel: „Macht eine Nacherfüllung den Stillstand ungeschehen?“ ✗; grün „neben der Leistung: § 280 Abs. 1 BGB“; „BGH: Nutzungsausfall ohne Verzug ersatzfähig“ (V ZR 93/08 Rn. 12, 14), BT-Drucks. S. 225; ✓ „4.500 € für Elfriede, ohne Frist“; „verzögerte Nacherfüllung: Verzug nötig, §§ 280 Abs. 2, 286 BGB“, Block „Video „Schuldnerverzug““ | tabler:`clock-pause`, `plus`, `scale`, `printer`, `coin-euro`, `hourglass` | `Posten 3: Produktionsausfall › Kontrollfrage` → `› neben der Leistung` → `› BGH, V ZR 93/08` → `Posten 3 › Verzögerungsschaden, § 280 Abs. 2 BGB` | – |
| **J Lösung** `loes`–`l4` | Tabelle Posten / Kontrollfrage / Anspruch / Ergebnis, je Zeile zum Wort; Block „zusammen sofort: 10.500 €“ | tabler:`table`, `hourglass`, `settings-automation`, `clock-pause`, `cash-banknote` | `Lösung › alle drei Posten` | – |
| **K Klausurtipp** `tipp`–`t3` | hellgelbe Tafel, Lexi warnt: „Schadensposten für Schadensposten prüfen“, „1. bei jedem die Kontrollfrage stellen“, „2. erst dann die Anspruchsgrundlage wählen“, ✗ „nie alle Posten in einen Topf“ | Warnsymbol (Streamline Freehand) | `Klausurtipp · Posten für Posten` | – |
| **L Klausurschema** `sch`–`k5` | breite Karte, I.–V. je zum Wort (Kontrollfrage; Schuldverhältnis und Pflichtverletzung; nur statt: erfolglose Frist; Vertretenmüssen, vermutet; Schaden) mit Normangaben | – | `Klausurschema` → `› I. Kontrollfrage` → … → `› V. Schaden` | – |
| **M Merksatz** `merke`–`mk4` | Lexi erklärt; Marker „statt der Leistung,“, „also grundsätzlich erst nach Frist.“, „gibt es neben der Leistung,“, „ohne Frist.“ | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („3 Tage“). Zahlen auf Tafeln, Pillen und Karte als Ziffern; Normwortlaut wörtlich.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Elfriede führt eine Druckerei. Bei Dietrich, der Steuerchips selbst herstellt, kauft sie für ihre Druckmaschine einen Chip zum Nachrüsten, für 300 Euro. Beide sind Kaufleute, der Kauf gehört zu ihrem Geschäft. Ihr Techniker setzt den Chip ein.
>
> Der Chip ist fehlerhaft: Durch Unsorgfalt in der Fertigung von Dietrich überhitzt er und zerstört die bis dahin einwandfreie Steuerungseinheit der Maschine. Elfriede meldet den Fehler noch am selben Tag. Drei Tage steht die Maschine still, bis eine neue Steuerungseinheit eingebaut ist; danach läuft sie vorerst ohne den neuen Chip.
>
> Elfriede verlangt sofort 300 Euro für den Chip (Posten 1), 6.000 Euro für die neue Steuerungseinheit (Posten 2) und 4.500 Euro entgangenen Gewinn (Posten 3). Eine Frist hat sie nicht gesetzt. Dietrich bietet einen neuen Chip an, will aber nichts zahlen.
>
> **Welcher Posten über welchen Anspruch – und wofür braucht sie eine Frist?**
