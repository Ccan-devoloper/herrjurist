# Folge 229 · Dein Foto in fremder Werbung: Die Eingriffskondiktion (§ 812 BGB) – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_229.py`](src/skript_229.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Bereicherungsrecht · Klassiker-Fall. Aufbau nach Auftrag: Hook mit Zahlen als Ziffern (Plakat, „120 Plakate“, „übliche Lizenz: 3.000 €“) → Frage, Klassiker (Pille „BGH, Urt. v. 8.5.1956 · I ZR 62/54 · BGHZ 20, 345 (Paul Dahlke)“) → Sachverhalt → I. Anspruchsgrundlage (Wortlautkarte § 812 Abs. 1 Satz 1 BGB, „in sonstiger Weise auf dessen Kosten“), Vorrang der Leistungskondiktion in einem Satz mit Verweis auf Folge 073 → 1. etwas erlangt (Nutzung des Bildnisses) → 2. auf Kosten (Lehre vom Zuweisungsgehalt; Wortlautkarte § 22 Satz 1 KUG; vermögensrechtlicher Bestandteil) → 3. ohne rechtlichen Grund (keine Einwilligung, keine Zeitgeschichte-Ausnahme) → III. Rechtsfolge (Wortlautkarte § 818 Abs. 2 BGB; fiktive Lizenz; Einwand „hätte nie zugestimmt“ unerheblich; Entreicherung ein Satz) → IV. parallele Ansprüche (§ 823 Abs. 1, § 823 Abs. 2 i. V. m. § 22 KUG mit Verschulden; Unterlassung § 1004 Abs. 1 Satz 2 analog) → Ergebnis an der Haltestelle → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 6:12,0 (5.373 vertonte Zeichen). Vorlagen: 226 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 073 (Kondiktionsarten, nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung (Vorgabe Koordinator):** Paul Dahlke (reale Person) erscheint nicht als Figur und wird nicht gesprochen; sein Name steht nur als Fallbezeichnung auf der Fundstellen-Pille, im Prüfpfad und in einer Fundstellenzeile der Rechtsfolgen-Tafel. Im Fall der fiktive Kai Möbius und die fiktive Limonadenfirma „Brauselust“ (keine echte Marke, kein Logo; Plakat aus Grundformen mit einem Ausschnitt der Open-Peeps-Figur Kai und einer Tabler-Flasche).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Kai Möbius (KA), um 28 | Abgebildeter, Anspruchsteller | `standing/robot_dance-3` (Pullover Grün `#8FD694`, Hose Dunkelgrau `#4A4A55`, offene Hand), Kopf `Short 4`, Haut `#E8B894`, kein Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Awe` (staunt), `Smile`, `Suspicious`, `Concerned\|Serious`, `Eating Happy` (trinkt im Park) | `niklas` (Mann, jung) |
| Marketingleiter Wendorf (WE), um 58 | Firma Brauselust | `standing/blazer-3` (Sakko Dunkelgrün `#4E7D5B`, schwarzes Shirt der Pose, Hose Grau `#5A5A66`), Kopf `No Hair 3` (Haarkranz Grau `#9A9A9A`), Brille `Glasses 3`, Haut `#EBC29E`, kein Bart. Mimiken `Calm` (ruhig/redet), `Smile`, `Suspicious`, `Serious`, `Concerned\|Serious` | `helmut` (Mann, älter) |
| Kollegin (KO), um 30 | erkennt Kai auf dem Plakat (heiterer Satz) | `standing/easing-2` (Jacke Rot `#F07A6A`, Hose Blaugrau `#3A4A6B`), Kopf `Medium Bangs 2` (Haar `#2B2B2B`), Haut `#B07552`. Mimiken `Calm`, `Cute` (redet), `Smile`, `Awe` | `ela_froh` (Frau, jung, heiter) |
| Fotograf (FO) | stumm, nur Rückblick | `standing/walking-1` (Shirt Blau `#8DB3F2`), Kopf `hat-beanie` (Mütze Gelb `#F9D56E`), Haut `#D9A47E`, Mimik `Driven` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Kollegin und Kai blicken zum Plakat (links); A2: Fotograf (`_r`) blickt zu Kai, Kai (`_r`) trinkt und blickt vom Fotografen weg (er bemerkt nichts); A3: Kai (`_r`) und Wendorf blicken einander an; Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Eating Happy`); Mundzustände a/o/e nur in `KA_redet`, `WE_redet`, `KO_redet` (je links/rechts) und Lexi. 64 Figuren-PNGs in `../peeps/op_229/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Wendorf sachlich (Sakko, ruhige bis nachdenkliche Mimik), keine „fiese“ Figur, keine Prothesen-Posen (`shirt-1`, `blazer-1` verworfen), keine Bärte, keine Polka Dots. Keine Zuordnung von Herkunft oder Hautfarbe zu einer Rolle. Kopf `Gray Medium` für Wendorf verworfen (Bibliothek färbt ihn rot, wirkte wie eine Frau); `shirt-3` für Kai verworfen (Hände in den Taschen, Flasche hätte geschwebt).
- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh; julia nicht besetzt). Vorfolgen: 226 julia/niklas/helmut/ela_froh; 228 und 230 laufen parallel.
- **Namen:** Kai, Möbius, Wendorf – eindeutig deutsch (Kai klingt deutsch und englisch gleich), nicht in der Liste vergebener Namen, per `grep -rliw` in keiner `*.py/*.md/*.json/*.csv/*.txt` unter `youtube/` (07.10.2026; „Hannes“ verworfen wegen 005, „Johannes“ wegen Ensemble, „Jannik“ wegen 010, „Bredow“ verworfen wegen uneindeutiger -ow-Aussprache), in `namen_reserviert.txt` als „229: Kai, Möbius, Bredow“ und „229: Wendorf (ersetzt Bredow …)“ eingetragen. Gesprochen: „Kai“ (Erzählerin 14×, Kollegin 1×), „Kais“ (1×), „Möbius“ (1×), „Herrn Wendorf“/„Herr Wendorf“ (je 1×).

**Abweichung von den letzten Folgen (226–228):** Posen `robot_dance-3`, `blazer-3`, `easing-2`, `walking-1` – in 226 (`resting-1`, `blazer-4`, `crossed_arms-2`, `walking-3`), 227 (`blazer-4`, `pointing_finger-1`, `easing-1`, `resting-1`, `robot_dance-2`) und 228 (`polka_dots`, sitzend, `blazer-2`, `shirt-2`, `crossed_arms-1`, `walking-2`) nicht verwendet. Schauplätze **Bushaltestelle mit Wartehäuschen und Plakat**, **Stadtpark mit Bäumen**, **Büro der Firma mit Plakat und Tisch** – neu gegenüber 226 (Kiosk, Redaktion, Kanzlei), 227, 228. Die Haltestelle kehrt in I zurück (Ergebnis bei Kai). Tageslicht-Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Haltestelle** `fall`→`ka1` | ab 0,0 s Wartehäuschen, Haltestellenschild „H“, Kollegin, Kai (Namensschilder); Plakat „BRAUSELUST – so schmeckt der Sommer“ zum Wort „Neben ihm hängt …“; Kai mit Flasche auf dem Plakat zum Wort „Und auf dem Plakat“; beide staunen; Blasen Kollegin, Kai | Wartehäuschen, Schild, Plakat aus Grundformen (`haltestelle()`, `plakat()`); tabler `bottle` | `Fall · An der Bushaltestelle` (ab 0,0 s) → `· Ein neues Werbeplakat: Brauselust` → `· Auf dem Plakat: Kai` → `· Gefragt hat ihn niemand` | – |
| **A2 Stadtpark** `park`→`plakate` | Bäume; Kai trinkt (Flasche auf der offenen Hand), Fotograf mit Kamera tritt auf, Blitz-Symbol zum Wort „fotografiert“; Pille „ohne dass er es bemerkte“; fünf kleine Plakate + Pille „120 Plakate in der ganzen Stadt“ | `baum()`; tabler `bottle`, `camera`, `sparkles` | `Fall · Im Sommer im Stadtpark` → `· Ein Fotograf der Firma` → `· 120 Plakate in der ganzen Stadt` | Kameraauslöser (`szene_229kamera_1`, Freesound CC0 579876) |
| **A3 Büro** `buero`→`bgh` | Plakat an der Wand, Tisch mit Flasche; Kai und Wendorf, Blasen; Pillen Frage, „übliche Lizenz … 3.000 €“, Klassiker, Fundstelle | `buero()`; tabler `bottle` | `Fall · Im Büro der Firma Brauselust` → `· Kai verlangt die übliche Lizenz` → `· Der Einwand des Marketingleiters` → `Die Frage · Muss die Firma zahlen?` → `Die Frage · BGHZ 20, 345 (Paul Dahlke)` | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | – |
| **C1 I. Anspruchsgrundlage** `norm`→`alt2` | **Wortlautkarte § 812 Abs. 1 Satz 1 BGB**, Marker „in sonstiger Weise“, „dessen Kosten“, „ohne rechtlichen Grund“, „erlangt“; gelber Block „2. Alternative … = Eingriffskondiktion“; Kai | tabler `scale`, `photo` | `I. Anspruchsgrundlage · § 812 Abs. 1 Satz 1 BGB` → `› Wortlaut` → `› 2. Alternative: Eingriffskondiktion` | – |
| **C2 Vorrang** `vorr`→`verweis` | Kreuz „Nein: nichts zugewendet“, Haken „Bild genommen“, Fundstelle I ZR 187/10 Rn. 46, blauer Block Verweis auf die Überblicksfolge; Wendorf, Kai | tabler `gift-off`, `books` | `› Vorrang: Hat Kai geleistet?` → `› keine Leistung` → `› Vorrang …: Folge Überblick` | – |
| **D 1. Etwas erlangt** `erl`→`bgh1` | Kreuz „nicht das Foto“, Haken „Nutzung von Kais Bildnis“, grüner Block BGH; Kai | tabler `help-circle`, `ad-2` | `II. Voraussetzungen › 1. etwas erlangt` → … | – |
| **E1 2. Auf Kosten** `kosten`→`def` | „Lehre vom Zuweisungsgehalt“, gelber Block Definition (IX ZR 204/11 Rn. 15); Kai | tabler `user-square`, `key` | `› 2. auf Kosten` → `› 2. Lehre vom Zuweisungsgehalt` | – |
| **E2 Recht am eigenen Bild** `kug`→`eing` | **Wortlautkarte § 22 Satz 1 KUG**, Marker „nur mit Einwilligung“, „verbreitet“; Haken Entscheidung über Werbung, vermögensrechtlicher Bestandteil; roter Block Eingriff; Wendorf, Kai | tabler `user-square`, `ad-2`, `ban` | `› 2. Recht am eigenen Bild` → `› 2. § 22 Satz 1 KUG` → `› 2. Kai entscheidet über Werbung` → `› 2. Eingriff in den Zuweisungsgehalt` | – |
| **F 3. Ohne rechtlichen Grund** `org`→`tbm` | Kreuze Einwilligung, Zeitgeschichte-Ausnahme (zum „nicht“), grüner Block 1.–3. (+); Wendorf | tabler `file-certificate`, `signature`, `circle-check` | `› 3. ohne rechtlichen Grund` → … → `› Voraussetzungen (+)` | – |
| **G1 III. Rechtsfolge** `rf`→`hier` | Kreuz „Nutzung kann nicht herausgegeben werden“, **Wortlautkarte § 818 Abs. 2 BGB** (Marker „Beschaffenheit des Erlangten“, „Wert zu ersetzen“), fiktive Lizenz, Fundstelle mit BGHZ 20, 345 (Paul Dahlke), Block „Hier: 3.000 €“; Kai | tabler `package`, `scale`, `coin-euro` | `III. Rechtsfolge · Herausgabe?` → `› § 818 Abs. 2 BGB: Wertersatz` → `› Wert = übliche Lizenzgebühr` → `› hier: 3.000 €` | – |
| **G2 Einwand** `einwand`→`wert` | Zitat-Pille Wendorf, Kreuz „unerheblich“, Haken „keine unterstellte Zustimmung“, Blöcke „misst ihm … Wert bei“ / „festhalten lassen“ zum Wort; Wendorf, Kai | tabler `message-circle-question`, `x`, `coin-euro` | `› Einwand: „nie für Limonade geworben“` → … | – |
| **G3 Entreicherung** `entr`, `kennt` | Kreuz § 818 Abs. 3, Haken Kenntnis, Block §§ 819 Abs. 1, 818 Abs. 4; Wendorf | tabler `receipt-euro`, `alert-triangle` | `› Entreicherung, § 818 Abs. 3 BGB?` → `› verschärfte Haftung, § 819 Abs. 1 BGB` | – |
| **H IV. Daneben** `par`→`unt` | § 823 Abs. 1, § 823 Abs. 2 i. V. m. § 22 KUG zum Wort, roter Block Verschulden, Unterlassung § 1004 Abs. 1 Satz 2 analog; Kai | tabler `list-check`, `coin-euro`, `alert-triangle`, `hand-stop` | `IV. Daneben · weitere Ansprüche` → … | – |
| **I Ergebnis (Haltestelle)** `erg`, `erg2` | Schauplatz A1; Haken „3.000 € Wertersatz …“, „keine Werbung mehr mit seinem Bild“; Münze, Stopp-Hand; Kai und Kollegin froh | tabler `coin-euro`, `hand-stop` | `Ergebnis · 3.000 € Wertersatz` → `› keine Werbung mehr mit Kais Bild` | – |
| **J Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | – |
| **K Prüfschema** `sch`→`s5` | breite Karte, 8 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („3.000 €“, „120 Plakate“, „8.5.1956“, „§ 812 Abs. 1 Satz 1 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Kameraauslöser; Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Wartehäuschen, Schild, Plakate, Bäume, Tisch programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ein Fotograf der Limonadenfirma „Brauselust“ fotografiert Kai Möbius im Stadtpark, ohne dass Kai es bemerkt. Ohne seine Einwilligung wirbt die Firma mit dem Bild: 120 Plakate zeigen Kai lachend mit einer Flasche Brauselust.
>
> Marketingleiter Wendorf wusste, dass für die Werbung eine Einwilligung nötig war und Kai nie gefragt wurde. Für ein solches Werbefoto zahlt man üblicherweise 3.000 €.
>
> Kai verlangt 3.000 €. Wendorf meint, Kai hätte ohnehin nie für Limonade geworben und deshalb nichts verloren.
>
> **Muss die Firma zahlen, und wie viel?**

Kein Fiktiv-Hinweis; beim Klassiker stehen Gericht, Datum, Aktenzeichen und Fundstelle auf der Pille.
