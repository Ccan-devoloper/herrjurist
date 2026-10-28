# Folge 021 · Geschäftsfähigkeit Schema §§ 104 ff. BGB: Minderjährige im Vertrag – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_021.py`](src/skript_021.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · BGB AT, Themenplan-Format „Schema“. Ein frei erfundener Fall trägt das ganze Schema: Die 15-jährige Frieda kauft im Handyladen von Herrn Ritter ein Smartphone für 600 € (sonst 800 €), 100 € Anzahlung aus gespartem Taschengeld, Rest in fünf Monatsraten; Ritter weiß, dass sie 15 ist. Die Mutter verweigert die Genehmigung nur gegenüber Frieda, Ritter fordert die Eltern zur Erklärung auf, sie schweigen. Prüfung Ritter gegen Frieda, § 433 II: I. Einigung, II. Wirksamkeit (1. §§ 104, 105 – 2. § 106 – 3. § 107 – 4. Einwilligung § 183 – 5. § 110 mit Gegenfall Kopfhörer – 6. Genehmigung §§ 108, 184, Aufforderung § 108 II, Widerruf § 109 mit § 131 II), III. Ergebnis; Ausblick §§ 112, 113. Klausurtipp „Verpflichtung und Verfügung trennen“, Schema, Merksatz. Länge: Hauptfilm 5:59 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frieda (FR), 15 | Schülerin, Käuferin | Pose `standing/easing-1` (offenes Hemd über Shirt, Turnschuhe), Kopf `Long Bangs`; Hemd Grün `#8FD694`, Shirt Weiß, Haut `#D9A47A`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile` (froh), `Concerned|Serious` (Sorge), `Serious` (denkt), `Suspicious` (überlegt) | `ela_froh` (Frau, jung) |
| Herr Ritter (RI), um 60 | Inhaber des Handyladens, Verkäufer | Pose `standing/shirt-3` (blaues Hemd), Kopf `Gray Short`, Brille `Glasses 3`; Hemd Blau `#8DB3F2`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet/froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge), `Serious` (ernst, schreibt) | `helmut` (Mann, älter) |
| Friedas Mutter (MU), um 45 | gesetzliche Vertreterin (zugleich für den Vater) | Pose `standing/blazer-3` (roter Blazer), Kopf `Medium 2`; Blazer Rot `#F07A6A`, Hose `#3D3D58`, Haut `#D9A47A` (wie Frieda); Mimiken `Calm`, `Serious` (redet, ernst), `Suspicious` (denkt), `Smile` | `julia` (Frau, jung; ruhig) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Frieda im Laden zu Ritter, Mutter zu Hause zu Frieda). Keine Prothesen-Posen, keine Bärte. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `FR_redet`, `RI_redet`, `MU_redet` (je links/rechts) und Lexi. Stimmen nur aus dem zugeteilten Pool (`ela_froh`, `helmut`, `julia`; `niklas` nicht benötigt). Namen mit eindeutig deutscher Aussprache (Frieda, Ritter); die Mutter bleibt ohne Namen (Funktionsrolle). Die Minderjährige wird respektvoll gezeigt: Sie kauft offen, sagt nichts Unwahres, Mimik froh/besorgt/nachdenklich, keine Bloßstellung. Figuren-PNGs: `../peeps/op_021/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 017: Café, Büro mit Briefkasten (Nacht), Boten (Helga, Werner, Paula); 014: Hof mit Kombi, Schreibtisch/Handy, Wochenleiste (Gerd, Lotte, Malte).
- Neue Posen (`easing-1`, `shirt-3`, `blazer-3`) gegenüber 014/017; Schauplätze Ladentheke im Handyladen und Wohnzimmer (Lampe, Sofa) im geteilten Bild mit Ritters Laden; neue Leitelemente Altersleiste (unter 7 / 7 bis 17), Ratenleiste (6 × 100 €), Zwei-Wochen-Leiste. Cremegrund, Tageslicht (der Abend ist nur Uhrzeit, kein Nachtbild).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Im Handyladen** `fall`→`r1` | Bodenlinie, Frieda links (blickt zu Ritter), Ladentheke (Karte), Ritter rechts | tabler:`device-mobile` (Weiß, wandert zu Frieda), `cash-banknote` (Grün, wandert auf die Theke); Schild „Handyladen Ritter“ | `Fall · Im Handyladen` (ab 0,0 s) | Frieda · „15 Jahre“ · Ritter kommt · Handy · „600 €“ · „sonst 800 €“ · Frieda redet, Blase · Schein wandert · „100 € Anzahlung“ · „aus Taschengeld“ · „Rest: 5 Monatsraten“ · „Ritter weiß: Frieda ist 15“ · „Eltern wissen nichts“ · Ritter redet, Blase · Handy wandert zu Frieda | Geld auf der Theke (`szene_021muenzen_1`) |
| **B Am Abend zu Hause / Ritters Brief** `abend`→`frage` | Wohnzimmer links (Lampe, Sofa, Mutter, Frieda mit Handy), Trennlinie, rechts Ritter im Laden | tabler:`lamp`, `sofa` (Lila), `device-mobile`, `pencil`, `mail` (wandert), `mail-opened`, `message-off` | `Fall · Am Abend zu Hause` → `Fall · Ritters Brief` → `Fall · Die Frage` | „Am Abend“ · „das neue Handy“ · Mutter redet, Blase · Frieda besorgt · Ritter erscheint, „erfährt davon nichts“ · Stift · Brief wandert, öffnet sich · „Aufforderung an die Eltern“ · „Genehmigen Sie den Kauf?“ · „keine Antwort“ · Frage-Pille | Umschlag öffnet sich (`szene_021umschlag_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **D Anspruch, I. Einigung** `ansp`→`wirk` | Tafel links, Ritter und Frieda rechts | tabler:`cash-banknote`, `file-text` | `Ritter gegen Frieda · § 433 Abs. 2 BGB` → `I. Einigung · Angebot und Annahme` → `II. Wirksamkeit · Friedas Geschäftsfähigkeit` | Anspruch · restlicher Kaufpreis · I. Einigung ✓ · II. Wirksamkeit? · Block | – |
| **E II. 1./2.** `p104`→`p106` | Tafel mit Altersleiste | tabler:`baby-carriage`, `school` | `II. Wirksamkeit › 1. geschäftsunfähig? §§ 104, 105 BGB` → `› 2. beschränkt geschäftsfähig, § 106 BGB` | § 104 · „unter 7“ · krankhafte Störung · § 105 · „7 bis 17: minderjährig“ · Strich „Frieda: 15“ · Block § 106 | – |
| **F II. 3. § 107** `p107`→`schnapp` | Tafel mit **Wortlautkarte § 107** | tabler:`users`, `receipt`, `discount` | `II. Wirksamkeit › 3. lediglich rechtlicher Vorteil? § 107 BGB` | Karte · Marker „nicht lediglich …“ · Marker „Einwilligung“ · Eltern · Pflicht 600 € · (−) Nachteil · Schnäppchen | – |
| **G II. 4. Einwilligung** `einw`→`keine` | Tafel, Mutter und Frieda | tabler:`user-check`, `user-x` | `II. Wirksamkeit › 4. Einwilligung? §§ 107, 183 BGB` | Definition · § 183 · ✗ wussten nichts · Block „fehlt“ | – |
| **H II. 5. § 110** `p110`→`rate` | Tafel mit **Wortlautkarte § 110**, Ratenleiste | tabler:`pig-money` | `II. Wirksamkeit › 5. Taschengeld? § 110 BGB` | Karte · Marker „von Anfang an wirksam“, „bewirkt“, „zu diesem Zweck …“ · Anzahlung grün · 5 offene Raten · „500 € offen“ · Ratenkauf-Zeile · ✗ letzte Rate · Block | – |
| **I Gegenfall Kopfhörer** `kopf`→`kopf_ok` | Tafel, Schein wandert zu Ritter | tabler:`headphones`, `cash-banknote` | `Gegenfall · Kopfhörer, sofort bezahlt` | Kopfhörer · 40 € · ✓ sofort bezahlt · Block „von Anfang an wirksam“ | – |
| **J II. 6. Genehmigung** `p108`→`rueck` | Tafel, Mutter und Frieda | tabler:`hourglass`, `arrow-back-up` | `II. Wirksamkeit › 6. Genehmigung, § 108 Abs. 1 BGB` | § 108 I · „schwebend unwirksam“ · § 184 | – |
| **K Aufforderung** `verw`→`fikt` | Tafel mit **Wortlautkarte § 108 II**, Zwei-Wochen-Leiste; Ritter und Mutter | tabler:`mail`, `calendar-event`, `message-off` | `II. Wirksamkeit › 6. Aufforderung, § 108 Abs. 2 BGB` | Verweigerung nur ggü. Frieda · Karte · Marker „wird unwirksam“, „nur ihm gegenüber“, „zwei Wochen“, „gilt sie als verweigert“ · Leiste · „Eltern schweigen“ · Block | – |
| **L Widerruf** `p109`→`nicht` | Tafel, Ritter und Frieda | tabler:`arrow-back-up`, `mail` | `II. Wirksamkeit › 6. Widerruf? § 109 BGB` | § 109 I · auch ggü. Frieda · § 131 II, „an die Eltern“ · § 109 II · „15 Jahre“ · ✗ hat sie nicht | – |
| **M III. Ergebnis, Ausblick** `erg`→`p113` | Tafel | tabler:`building-store`, `briefcase` | `III. Ergebnis · Vertrag endgültig unwirksam` → `Ausblick · §§ 112, 113 BGB` | Block · ✗ 500 € · Rückabwicklung · § 112 · § 113 · „unbeschränkt“ | – |
| **N Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Verpflichtung und Verfügung trennen` | Satz · Kaufvertrag (−) · Übereignung · (+) · keine Einwilligung | – |
| **O Klausurschema** `sch`→`k3` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · II. · 1.–6. · Zusatz · III. | – |
| **P Merksatz** `merke`→`m3` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker · Satz 3 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo etwas übergeben oder geschickt wird (Geldschein, Handy, Brief).
**Wortlautkarten:** §§ 107, 108 II, 110 BGB wörtlich nach gesetze-im-internet.de (Abruf 01.10.2026) mit Fundstelle; Auslassungen mit „…“; Hervorhebungen synchron zum gesprochenen Merkmal (Ausnahme von „Tafeltext hat gesprochene Entsprechung“ nach FOLGE-ABLAUF Abschnitt 2).
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort). Tafeln dürfen Ziffern verwenden („600 €“).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Die 15-jährige Frieda kauft im Handyladen von Herrn Ritter ein Smartphone für 600 Euro, das sonst 800 Euro kostet. 100 Euro zahlt sie sofort aus gespartem Taschengeld, das ihr die Eltern zur freien Verfügung geben; den Rest soll sie in fünf Monatsraten zahlen. Ritter weiß, dass Frieda 15 ist. Er übergibt und übereignet ihr das Handy sofort, ohne Eigentumsvorbehalt. Die Eltern wissen nichts von dem Kauf; Frieda behauptet auch nichts anderes.
>
> Am Abend sagt die Mutter, auch für den Vater, zu Frieda: „Das genehmigen wir nicht!“ Ritter erfährt davon nichts. Er fordert die Eltern per Brief auf, zu erklären, ob sie den Kauf genehmigen. Sie antworten nicht; zwei Wochen nach Empfang des Briefes ist nichts geschehen.
>
> *(Frei erfundener Übungsfall.)*
>
> **Muss Frieda die restlichen 500 Euro zahlen?**
