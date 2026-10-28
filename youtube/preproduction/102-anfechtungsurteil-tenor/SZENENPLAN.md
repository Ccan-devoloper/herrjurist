# Folge 102 · Anfechtungsurteil Tenor: „in Gestalt des Widerspruchsbescheids“ – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_102.py`](src/skript_102.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · VwGO-Praxis, Themenplan-Format „Formulierung“; anknüpfend an Folge 069 (Anfechtungsklage-Schema) und 093 (Tenorformeln der Verpflichtungsklage). Übungsfall nach dem Hook („Ein Gebührenbescheid über 2.400 Euro ist nur in Höhe von 900 Euro rechtswidrig“), Beispielland Nordrhein-Westfalen, weil dort bei Kommunalabgaben ein Vorverfahren stattfindet (§ 110 Abs. 2 Satz 1 Nr. 6 JustG NRW): Frau Rehbein betreibt eine Wäscherei; die Stadt setzt die Abwassergebühr auf 2.400 € fest (6 € je m³ × 400 m³), der Zähler zeigt 250 m³; Herr Zimmermann bringt den zurückweisenden Widerspruchsbescheid; sie klagt auf Aufhebung des ganzen Bescheids; das Gericht stellt 250 m³ fest. Ablauf: Fall → Gericht und Frage → Sachverhalt → Vorfrage NRW → Gegenstand (Wortlautkarte § 79 I Nr. 1) mit Tenoranfang → Umfang (Wortlautkarte § 113 I 1, Teilbarkeit, Rechtsverletzung) → Tenor Hauptsache („soweit“, „Im Übrigen …“) → Klausurtipp § 113 II (Lexi) → Kosten (Wortlautkarte § 155 I 1, 5/8 zu 3/8) → vorläufige Vollstreckbarkeit → Berufung → vollständiger Tenor (Karte zum Mitschreiben) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:20,1 (5.416 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Rehbein (RE), um 60 | betreibt eine Wäscherei, Klägerin | Pose `standing/polka_dots` (weiße Bluse mit schwarzen Punkten, dunkelblaue Hose `#3D4A7A`), Kopf `Gray Medium` (Haar `#C4C4CC`), Haut `#F2C7A8`; Mimiken `Calm` (ruhig), `Driven` (redet), `Concerned|Serious` (Sorge), `Rage|Serious` (Ärger), `Suspicious` (denkt), `Smile` (froh) | `hilde` (Frau, älter) |
| Herr Zimmermann (ZI), um 45 | Gebührenabteilung der Stadt | Pose `standing/shirt-3` (hellblaues Hemd `#8DB3F2`, schwarze Hose), Kopf `Short 2`, Brille `Glasses 3`, Haut `#E0AC88`; Mimiken `Calm` (ruhig), `Serious` (redet), `Solemn` (denkt) | `christian` (Mann, mittel) |
| der Richter (RI), um 55 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/easing-2` (dunkelgraues offenes Hemd `#4A4A55` über schwarzem Shirt, dunkle Hose `#3A3A48`), Kopf `No Hair 2`, Brille `Glasses 2`, Haut `#D9A07A`; Mimiken `Calm` (ruhig), `Serious` (redet) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Rehbein blickt nach rechts zu Herrn Zimmermann, er nach links zu ihr; Szene B: Frau Rehbein blickt nach rechts zum Richter, er nach links zu ihr; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `RE_redet`, `ZI_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool:** `hilde`, `christian`, `stephan`; `christian` (Zimmermann, Szene A) und `stephan` (Richter, Szene B) treten nie in derselben Szene auf. `lucy` nicht gebraucht. Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Rehbein, Zimmermann (nicht in der Liste früherer Namen; `grep -w` über alle Folgenordner ohne Treffer). Der Richter bleibt namenlos.
- Frau Rehbein ist keine Querulantin: Sie hat in der Sache teilweise recht und will zu viel. Herr Zimmermann sachlich.
- Figuren-PNGs: `../peeps/op_102/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 093 (Café an der Hauptstraße, `robot_dance-2`, `blazer-3`, `pointing_finger-1`), 096–099 (`resting-1/2`, `easing-1`, `blazer-1/3/4`, `crossed_arms-1`, `pointing_finger-2`, `walking-1/3`, `shirt-4`). Hier **Wäscherei** (Haus, zwei Waschmaschinen, Wasserzähler), Posen `polka_dots`, `shirt-3`, `easing-2` in 096–099 und 093 nicht verwendet; Polka-Dots-Bluse in den Vorfolgen nicht getragen. Das Verwaltungsgericht (Säulengebäude, Waage) kehrt bewusst wieder, weil die Klage dort spielt. Kein Richterhammer. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wäscherei** `fall`–`re1` | Haus mit Waschmaschinen, Frau Rehbein; Gebührenbescheid; Satzung/400 m³; Zähler 250 m³; Widerspruch; Herr Zimmermann bringt den Widerspruchsbescheid; Blasen Zimmermann/Rehbein; Kreuz am Widerspruch | ph:`house` (Blau), ph:`washing-machine` ×2 (Weiß), tabler:`file-text` (Bescheid, Widerspruchsbescheid), tabler:`gauge` (Gelb) | `Fall · Der Gebührenbescheid` (ab 0,0 s), `Fall · Der Widerspruchsbescheid` | Haus · Bescheid · 2.400 € · Sorge · Satzung · 400 m³ · Zähler · 250 m³ · denkt · Widerspruch · Zimmermann · Widerspruchsbescheid · Blase · Kreuz · Ärger · Blase Rehbein | Papier (`szene_102brief_1`), als der Widerspruchsbescheid erscheint |
| **B Verwaltungsgericht** `klage`–`frage2` | Frau Rehbein mit Klage; Richter stellt 250 m³ fest; Balken 2.400 € = 1.500 € + 900 €; Fragen | fluent-hc:`classical-building`, tabler:`file-text`, tabler:`gauge` | `Fall · Die Klage`, `Fall · Wie lautet der Tenor?` | Gericht · Klage · Pille · Zähler · Richter · Blase · 250 m³ · 1.500 € · denkt · Balken · rechtswidrig · Frage 1 · Frage 2 | – |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Vorfrage NRW** `vv`–`wsb` | § 110 I, II 1 Nr. 6, § 111 JustG NRW; Länderhinweis; Herr Zimmermann | tabler:`rubber-stamp` + Pille „Widerspruchsbescheid“ | `Vorfrage · Vorverfahren in NRW, § 110 JustG NRW` | NRW · entfällt meist · nicht bei KAG · Fundstelle · Land · Stadt selbst · Fundstelle | – |
| **E Gegenstand** `wl79`–`isol` | Wortlautkarte § 79 I Nr. 1 mit zwei Markern; Tenoranfang im Tenorkasten; Beklagte; isolierte Anfechtung; Frau Rehbein | tabler:`file-text` ×2 + Pille | `Tenor › Gegenstand, § 79 I Nr. 1 VwGO` | Karte · Marker · Marker/Icons · angegriffen · Tenorkasten · Zeile 1 · Zeile 2 · Beklagte · isoliert 1 · 2 | – |
| **F Umfang** `wl113`–`rv` | Wortlautkarte § 113 I 1 (vollständig) mit Markern; „soweit“; Teilbarkeit (9 B 18.23 Rn. 7); 1.500 € bleiben; Rechtsverletzung (9 B 4.19 Rn. 18); Richter | fluent-hc:`balance-scale` + Pille „1.500 € bleiben“ | `Tenor › Umfang: „soweit“, § 113 I 1 VwGO` | Karte · rechtswidrig · hebt · soweit · teilbar · Rest · bleiben · Fundstelle · 1.500 € · Haken · Adressatin · Fundstelle | – |
| **G Tenor Hauptsache** `t2`–`fehler` | Tenorkasten wächst: aufgehoben, soweit … mehr als 1.500 €; Antrag ganz; „Im Übrigen …“; Klausurfehler; Frau Rehbein | tabler:`file-text` + Pillen „2.400 €“, „− 900 €“ | `Tenor › Umfang: aufheben, soweit; im Übrigen abweisen` | Kasten · aufgehoben · mehr als · Antrag · Im Übrigen · Sorge · Klausurfehler | – |
| **H Klausurtipp** `tipp`–`tipp3` | Lexi warnt: Antrag; Zitatkarte § 113 II 1 (Auszug); Formulierungsbeispiel Änderungstenor; Ergebnisgleichheit | Warnsymbol (Streamline Freehand) | `Klausurtipp · Änderung nach § 113 II VwGO` | Antrag · Karte · Marker · Tenor · 2 Zeilen · Hinweis · 1.500 € | – |
| **I Kosten** `kosten`–`t4` | Wortlautkarte § 155 I 1; Pillen 2.400/900/1.500; 5/8; Kostentenor; Frau Rehbein | tabler:`calculator` + Pille „5/8 zu 3/8“ | `Tenor › Kosten, § 155 I 1 VwGO` | Karte · Marker · 3 Pillen · Sorge · Bruch · Kasten · Zeile · 5/8 · 3/8 · Pille | – |
| **J Vorläufige Vollstreckbarkeit** `vollstr`–`jeweils` | § 167 II, I 1 VwGO; § 708 Nr. 11, § 711 ZPO; Vollstreckbarkeitstenor Zeile für Zeile; „jeweils“; Richter | tabler:`coin` (Gelb) + Pille „nur wegen der Kosten“ | `Tenor › Vorläufige Vollstreckbarkeit, § 167 VwGO` | § 167 II · Anfechtungsurteile · Abs. 1 · ZPO · 1.500 € · §§ 708, 711 · Kasten · 6 Zeilen · Fundstelle · jeweils | – |
| **K Berufung** `ber`–`ber2` | § 124a I 1, 3 VwGO; Richter | fluent-hc:`balance-scale` | `Tenor › Berufung, § 124a I VwGO` | Satz 1 · Zulassungsgrund · § 124 II · Nichtzulassung · Fundstelle | – |
| **L Vollständiger Tenor** `voll` | Karte mit dem ganzen Tenor (erscheint auf einmal, ≈ 8 s Lesezeit) | – | `Ergebnis · Der vollständige Tenor` | 1 | – |
| **M Schema** `sch`–`s4` | progressiv: 1. Gegenstand – 2. Umfang – im Übrigen – 3. Kosten – 4. Vollstreckbarkeit – ggf. Berufung | – | `Schema · Tenor des Anfechtungsurteils` | 10 Aufbaustufen | – |
| **N Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Frau Rehbein betreibt eine Wäscherei im eigenen Haus in einer Stadt in Nordrhein-Westfalen. Mit Bescheid vom 2. März 2026 setzt die Stadt die Abwassergebühr auf 2.400 € fest: Ihre Satzung verlangt 6 € je m³, die Stadt rechnet mit 400 m³. Frau Rehbein legt Widerspruch ein, der Zähler zeige nur 250 m³. Die Stadt weist den Widerspruch mit Bescheid vom 4. Mai 2026 zurück. Frau Rehbein klagt fristgerecht und beantragt, den ganzen Bescheid aufzuheben. / Das Gericht stellt fest: Verbraucht wurden 250 m³; im Übrigen ist der Bescheid rechtmäßig. Die Kosten, die jede Seite vollstrecken kann, liegen unter 1.500 €.“ – Frage: „Wie lautet der Tenor des Urteils?“ (kein Fiktiv-Hinweis)
