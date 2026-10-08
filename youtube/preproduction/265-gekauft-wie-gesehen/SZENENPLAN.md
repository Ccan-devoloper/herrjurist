# Folge 265 · „Gekauft wie gesehen“: Hält der Gewährleistungsausschluss? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_265.py`](src/skript_265.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Kaufrecht · Alltagsfall. Fall: Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Nach Besichtigung und Probefahrt sagt er: „Der Motor läuft einwandfrei.“ Im handschriftlichen, gemeinsam formulierten Vertrag: „Motor läuft einwandfrei.“ und „Gekauft wie gesehen, keine Gewährleistung.“ 3 Wochen später ist der Motor hinüber, der Schaden war schon beim Kauf da; Herr Burmeister wusste nichts und beruft sich auf den Ausschluss. Ablauf (Plan): Hook → 1. Sachmangel, § 434 (Wortlautkarte; Verweis 059) → 2. Ausschluss wirksam? (§ 476 nur Verbrauchsgüterkauf, Individualvereinbarung, § 309 Nr. 7 in einem Satz) → 3. Reichweite „gekauft wie gesehen“ (+ „keine Gewährleistung“) → Grenze § 444 (Wortlautkarte): Arglist (−), Abgrenzung 262, Garantie (−) → vereinbarte Beschaffenheit geht vor (BGHZ 170, 86) → Ergebnis je Variante (Verweis 063) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:12,8 (5.483 vertonte Zeichen, Grenze 6.200). Mehr als fünf Minuten wegen zweier Wortlautkarten (§ 434 als Auszug, § 444 vollständig vorgelesen), der im Plan verlangten Auslegungsstufe („gekauft wie gesehen“ allein und mit „keine Gewährleistung“, zwei BGH-Entscheidungen), der Rechtsprechungslinie BGHZ 170, 86 → VIII ZR 161/23 und der Ergebnistafel mit vier Varianten.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Christel (CH), um 40 | Käuferin, kauft privat | Pose `standing/resting-2` (schwarzes Oberteil der Pose, Hose Lila `#B8A9F5`), Kopf `Medium 2`, Haut `#F1C9A5`; Mimiken `Calm`, `Smile`, `Smile Big|Smile`, `Suspicious`, `Concerned|Serious`, `Serious`, `Awe`, `Very Angry`; redet `Concerned|Serious` – alle mit geschlossenem Mund | `laura_ruhig` (Frau, mittel) |
| Herr Burmeister (BU), um 65 | privater Verkäufer, ehrlich (wusste nichts) | Pose `standing/shirt-1` (Hemd Grün `#8FD694`, schwarze kurze Hose, Beinprothese der Pose – keine Täterrolle), Kopf `Gray Short` (Haar `#C9C9C9`), Brille `Glasses 4`, Haut `#E8B48F`, kein Bart; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`, `Concerned|Serious`, `Awe`; redet `Smile` (Szene A) und `Serious` (Szene C) | `william` (Mann, älter) |
| Mechanikerin (ME), um 35 | Kfz-Werkstatt (Funktionsrolle ohne Namen) | Pose `standing/walking-2` (schwarzes Shirt, Arbeitshose Blau `#5B7DB1`), Kopf `Cornrows 2`, Haut `#B07552`; Mimiken `Calm`, `Serious` (redet), `Suspicious` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `CH_redet`, `BU_redet`, `BU_redet2`, `ME_redet` (je links/rechts) und Lexi. Stimmen nur aus dem Pool; `marc` nicht besetzt. Namen Christel und Burmeister: eindeutig deutsch, nicht in der Liste vergebener Namen und unter `youtube/preproduction` (`grep -rlw`, .md/.py/.json/.txt) nicht vorhanden, vor der Vertonung in `namen_reserviert.txt` eingetragen („265: Christel, Burmeister“). „Ingeborg“ verworfen (in der ec-Reihe vergeben). Kein Genitiv eines Namens (Assertion). Figuren-PNGs: `../peeps/op_265/` (74 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 262 (`easing-1`, `blazer-3`, `pointing_finger-2`; Autohof, Prüfhalle), 263 (`easing-1`, `shirt-4`; Stellwerk), 264 (`resting-1`, `blazer-4`, `robot_dance-2`, `crossed_arms-2`; Staatsanwaltschaft) und die parallelen 266/267 (`crossed_arms-1`, `blazer-2`, `shirt-3`, `robot_dance-3`, `walking-3`, `polka_dots`, `easing-2`): Posen `resting-2`, `shirt-1`, `walking-2` dort nicht verwendet; keine Polka Dots, keine Bärte. Schauplätze: Einfahrt vor dem Wohnhaus (Privatverkauf), Kfz-Werkstatt ohne Hebebühne (262 hatte die Prüfhalle mit Hebebühne), Rückkehr vor das Haus (Christel stellt Herrn Burmeister zur Rede – bewusste Rückkehr an den Kaufort). 262 (Händler, Unfallwagen, Anfechtung) nur in einem Satz abgegrenzt; anderes Fahrzeug (roter Kleinwagen statt gelbem Kombi).

**Darstellung:** keine echten Automarken (Tabler `car`, ohne Logo), **kein Unfall** – der Schaden erscheint nur als Motor-Symbol (Tabler `engine-off`) und als Anlassergeräusch. Keine Richterhämmer (Rechtsprechung als Waage `ph:scales`). Werkstatt nur mit Schild und Werkzeugkiste (`ph:toolbox`).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Einfahrt** `fall`→`schluessel` | Haus links, Christel, Auto Mitte, Herr Burmeister rechts | ph:`house`, tabler:`car`, `eye`, `steering-wheel`, `engine`, `signature`, `key` | `Fall · Christel sucht einen Kleinwagen` (ab 0,0 s) → `… Privatverkauf: Kleinwagen für 4.500 €` → `… Besichtigung und Probefahrt` → `… Herr Burmeister: „Der Motor läuft einwandfrei.“` → `… Handschriftlicher Kaufvertrag` → `… Unterschrieben, Schlüssel übergeben` | sucht · Herr Burmeister · „privat“ · Auto · „Zu verkaufen: 4.500 €“ · Besichtigung · Probefahrt · „alles in Ordnung“ · Blase · Motor-Symbol · Vertrag, Zeilen zum Wort · 2 Unterschriften · Schlüssel wandert | Unterschrift (`szene_265unterschrift_1`), Schlüssel (`szene_265schluessel_1`) |
| **B Werkstatt** `werk`→`m1` | Christel links, Auto, Mechanikerin rechts, Werkzeugkiste, Schild „Kfz-Werkstatt“ | tabler:`key`, `engine-off`, ph:`toolbox` | `Fall · 3 Wochen später: in der Werkstatt` → `Fall · Mechanikerin: „Der Motor ist hinüber.“` | „3 Wochen später“ · Schlüssel steckt · Blase · Motor aus · „Motorschaden“ · „schon beim Kauf da“ · Christel staunt/Sorge | Anlasser (`szene_265anlasser_1`) |
| **C Vor dem Haus, Frage** `c1`→`frage2` | Christel stellt Herrn Burmeister zur Rede | ph:`house` | `Fall · Christel: …` → `Fall · Herr Burmeister: …` → `Die Frage · …` | Blase Christel · Blase Burmeister · zwei Frage-Pillen | – |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s, ohne Fiktiv-Zusatz | – | `Sachverhalt` | 1 | – |
| **E 1. Sachmangel** `mangel`→`v059` | **Wortlautkarte § 434** (Abs. 1, Abs. 2 S. 1 Nr. 1, Abs. 3 S. 1 Nr. 1), Christel | tabler:`car`, `contract`, `engine-off` | `A. Sachmangel? · § 434 BGB` → `… › subjektiv …` → `… › objektiv …` → `A. Sachmangel (+)` → `… › Folge …` | Karte · 5 Marker · ✓ vereinbart · ✓ objektiv · (+) · Verweis | – |
| **F 2. Ausschluss wirksam?** `aus`→`agb` | Tafel, Christel und Herr Burmeister | tabler:`shield-off`, ph:`house`, tabler:`user`, `writing-sign` | `B. Gewährleistungsausschluss · 2. wirksam?` → … → `… › falls AGB: § 309 Nr. 7 BGB` | privat · ✗ § 476 · Unternehmer an Verbraucher · ✓ keine AGB · ✓ wirksam · Block § 309 Nr. 7 | – |
| **G 3. Reichweite** `ausl`→`zwerg` | Tafel, Christel | tabler:`eye`, `eye-off`, `shield-off` | `… › 3. Reichweite` → `… › „wie gesehen“: nur wahrnehmbare Mängel` → … → `… › Motorschaden grundsätzlich erfasst` | Feld „wie gesehen“, Zeilen · ✗ nicht zu sehen · Feld „keine Gewährleistung“ · umfassend · Block | – |
| **H1 § 444** `p444`→`v262` | **Wortlautkarte § 444**, beide | tabler:`shield-off`, `help` | `… › Grenze: § 444 BGB` → `… › Arglist (−)` → `… › Händler und Anfechtung: Folge …` | Karte · 4 Marker · ✗ Arglist · Verweis 262 | – |
| **H2 Garantie** `gar`→`garnein` | Tafel, Herr Burmeister | tabler:`certificate`, ph:`house`, tabler:`x` | `… › § 444 BGB: Garantie?` → … → `… › Garantie (−): § 444 BGB hilft nicht` | Zeilen · Fundstellen · ✗ · (−) | – |
| **I Beschaffenheit geht vor** `vorrang`→`ergeb` | Tafel: zwei Vertragssätze nebeneinander, BGHZ 170, 86, beide | tabler:`contract`, ph:`scales`, tabler:`engine` | `… › vereinbarte Beschaffenheit geht vor` → `… › BGHZ 170, 86 …` → … → `… › Haftung für den Motor (+)` | 2 Kästen · Regel zeilenweise · „ohne Sinn und Wert“ · st. Rspr. · ✓ · (+) | – |
| **J Varianten** `var`→`v063` | Ergebnistafel, Christel | tabler:`list-check`, `engine`, `tools` | `C. Ergebnis je Variante` → … | 4 Varianten mit (−)/(+) · Nacherfüllung · Verweis 063 | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 3 Schritte · Linie · Vertrag lesen · Beschaffenheit/Garantie | – |
| **L Schema** `sch`→`s3` | breite Karte, Punkt für Punkt | – | `Prüfungsschema …` | Titel · I. · II. · 1.–4. · III. | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei sichtbarer Handlung (Schlüssel wandert von Herrn Burmeister zu Christel).
**Wortlautkarten:** § 434 (Auszug mit „…“) und § 444 BGB wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026) mit Fundstelle; Marker synchron zum gesprochenen Merkmal.
**Ziffern:** Auf Blasen, Tafeln und Pillen Zahlen als Ziffern („4.500 €“, „3 Wochen später“, „§ 444 BGB“), im Sprechtext als Wörter.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Nach Besichtigung und Probefahrt sagt Herr Burmeister: „Der Motor läuft einwandfrei.“ In den handschriftlichen Kaufvertrag, den beide gemeinsam formulieren, schreiben sie: „Motor läuft einwandfrei.“ Darunter steht: „Gekauft wie gesehen, keine Gewährleistung.“ Weitere Zusagen macht Herr Burmeister nicht.
>
> 3 Wochen später ist der Motor hinüber. Die Mechanikerin stellt fest: Der Schaden war schon bei der Übergabe da; sehen konnte man ihn nicht. Herr Burmeister wusste davon nichts. Er beruft sich auf den Ausschluss.
>
> **Kann Christel trotzdem ihre Mängelrechte geltend machen?**
