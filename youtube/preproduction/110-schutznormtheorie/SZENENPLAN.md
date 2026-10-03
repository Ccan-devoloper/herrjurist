# Folge 110 · Schutznormtheorie: Klagen gegen die Genehmigung eines anderen – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_110.py`](src/skript_110.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Verwaltungsprozessrecht, Themenplan-Format „Schema“; Voraussetzungsfolge 105 (Klagebefugnis, Möglichkeits- und Adressatentheorie; hier ein Verweissatz), Abgrenzung zu 088/090 (Baugenehmigung, Rücksichtnahmegebot, Drittanfechtung; nur ein Verweissatz). Übungsfall nach dem Hook („Neben deinem Haus soll eine Shisha-Bar mit Außenbereich öffnen – du willst die Erlaubnis angreifen“), **Beispielland Nordrhein-Westfalen** (GastG des Bundes gilt fort): Frau Hoppe eröffnet im Nachbarhaus eine Shisha-Bar mit Terrasse unter dem Schlafzimmerfenster von Frau Brüning; die Stadt erteilt die Gaststättenerlaubnis für Bar und Terrasse bis 24 Uhr; Frau Brüning klagt. Ablauf: Fall → Frage → Sachverhalt → 1. Ausgangspunkt (Wortlautkarte § 42 II, Adressatentheorie hilft nicht, Verweis 105) → 2. Schutznormtheorie (Kriterien BVerwG) → Frage 1: Welche Norm? (NRW, Wortlautkarte § 4 I 1 Nr. 3 GastG) → Frage 2: Schützt sie auch Einzelne? (Wortlaut § 3 I BImSchG als Karte, Systematik § 5 I Nr. 3 GastG, Zweck; BVerwG 8 C 3.19) → Frage 3: geschützter Kreis, Möglichkeit, Gegenfall → 3. Tabelle typischer Normen ja/nein → 4. Grundrechte nur hilfsweise → Ergebnis (Verwaltungsgericht, Begründetheit offen) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 5:23,0 (4.733 gesprochene Zeichen); Begründung für die leichte Überschreitung des Regelrahmens in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Brüning (BR), um 68 | Nachbarin, Klägerin | Pose `standing/shirt-4` (schwarze Bluse der Pose, lila Hose `#B8A9F5`), Kopf `Medium Bangs 2` (graues Haar `#C9C6C0`), Brille `Glasses 2`, Haut `#F2D3B8`; Mimiken `Calm` (ruhig), `Concerned|Serious` (Sorge; Grundbild beim Reden), `Suspicious` (denkt), `Smile` (froh) | `hilde` (Frau, älter) |
| Frau Hoppe (HO), um 28 | Betreiberin der Shisha-Bar, Adressatin der Erlaubnis | Pose `standing/easing-1` (offenes hellblaues Hemd über lila Shirt, schwarze Hose), Kopf `Bangs 2` (dunkles Haar `#2E2420`; bewusst kein Dutt, damit sie nicht wie Lexi aussieht), Haut `#E3B48E`; Mimiken `Calm`, `Smile` (redet), `Cheeky|Smile` (stolz), `Suspicious` (denkt) | `lucy` (Frau, jung) |
| der Richter (RI), um 50 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/blazer-1` (dunkelblauer Blazer `#3D4E6E`, schwarzes Oberteil, weiße Hose, Beinprothese – positive Rolle), Kopf `Short 5`, Brille `Glasses`, Haut `#C68E62`; Mimiken `Calm`, `Serious` (redet) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Szene A: Frau Hoppe blickt nach rechts zu Frau Brüning, diese nach links zu ihr; Szene J: der Richter blickt nach rechts zu Frau Brüning und Frau Hoppe, beide nach links zu ihm; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BR_redet`, `HO_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, kein Muster, keine Polka-Dots.
- **Stimmen nur aus dem Pool** `stephan`, `hilde`, `christian`, `lucy`; verwendet `hilde`, `lucy`, `stephan` (`christian` nicht gebraucht, damit nie zwei ähnliche Männerstimmen; die beiden Frauenstimmen klar verschieden: älter/jung). Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Brüning, Hoppe (nicht in der Liste früherer Namen; `grep -w` über alle Folgenordner ohne Treffer). Der Richter bleibt namenlos. Namen nie im Genitiv mit -s („Schlafzimmerfenster von Frau Brüning“).
- Shisha-Bar ohne Klischees: neutrale Icons (Ladenfront, Schirm, Tisch, Cocktailglas), **keine Wasserpfeife, kein Rauch, niemand raucht**; die Betreiberin ist eine gewöhnliche junge Gastronomin.
- Figuren-PNGs: `../peeps/op_110/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 107 (Bank/Geldautomat; `shirt-3`, `resting-2`, `blazer-3`), 108 (Gasthaus am Marktplatz, Behörde; `robot_dance-3`, `pointing_finger-1`, `crossed_arms-1`), 109 (`easing-2`, `walking-3`, koralles Hemd). Hier **Wohnstraße mit Reihenhaus, Ladenfront der Bar und Terrasse**; Posen `shirt-4`, `easing-1`, `blazer-1` in 105–109 nicht verwendet; keine Polka-Dots. Das Verwaltungsgericht (Säulengebäude) kehrt bewusst zurück, weil dort entschieden wird. Kein Richterhammer. Tageslicht-Cremegrund; „bis Mitternacht“ nur über Mond-Icon und Pille, kein Nachtverlauf (die Szene zeigt die Lage, nicht eine Nacht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wohnstraße** `fall`–`frage2` | Haus von Frau Brüning mit Schlafzimmerfenster; Bar mit Terrasse kommt dazu; Erlaubnis bis 24 Uhr; Blasen Hoppe/Brüning; Frage | tabler:`home` (Blau), `window`, `building-store` (Gelb), `umbrella` (Rot), `table`, `glass-cocktail` (Pink), `license`, `moon` (Gelb) | `Fall · Die Shisha-Bar nebenan` (ab 0,0 s), `Fall · Die Gaststättenerlaubnis`, `Fall · Darf sie die Erlaubnis anfechten?` | Haus · Fenster · Bar · Terrasse · Erlaubnis · bis 24 Uhr/Sorge · Blase Hoppe · Blase Brüning · Frage | Gläser (`szene_110glas_1`), als Terrasse und Glas erscheinen |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **C 1. Ausgangspunkt** `p42`–`v105` | Wortlautkarte § 42 II mit 2 Markern; Adressatentheorie hilft nicht + Kreuz; Verweis 105; Brüning/Hoppe | tabler:`license` (Grün) | `… › 1. Ausgangspunkt, § 42 II VwGO`, `… › 1. Frau Brüning ist nicht Adressatin` | Titel · Karte · 2 Marker · 3 Zeilen · Pille | – |
| **D 2. Schutznormtheorie** `snt`–`reflex` | Kriterienkasten (3 C 5.23 Rn. 40), Allgemeinheit, reflexartig + Kreuz (6 C 2.23 Rn. 24) | tabler:`shield-check` (Grün) + Pille | `… › 2. Schutznormtheorie` | 11 | – |
| **E Frage 1** `fa`–`wl4` | NRW, GastG fort, andere Länder; Wortlautkarte § 4 I 1 Nr. 3 GastG mit 3 Markern; Fallannahme Erlaubnispflicht | tabler:`building-store` | `… › 2. Frage 1: Welche Norm?`, `… › 2. Frage 1: § 4 I 1 Nr. 3 GastG` | 9 | – |
| **F Frage 2** `fb`–`ja` | Auslegung; Karte § 3 I BImSchG (Marker „die Nachbarschaft“); Systematik § 5 I Nr. 3 GastG; Zweck; grüner Kasten „insoweit drittschützend“ + Haken; 8 C 3.19 Rn. 39 | tabler:`home` (Blau) + Pille „Nachbarschaft“ | `… › 2. Frage 2: Schützt sie auch Einzelne?` | 11 | – |
| **G Frage 3** `fc`–`gegen` | Nachbarschaft = Einwirkungsbereich; direkt über der Terrasse + Haken; nicht offensichtlich ausgeschlossen + Haken; Gegenfall „3 Straßen weiter“ + Kreuz | tabler:`bed`, `moon`, `map-pin` (Rot) | `… › 2. Frage 3: Gehört Frau Brüning dazu?`, `… › 2. Frage 3: Gegenfall` | 11 | – |
| **H 3. Typische Normen** `tab`–`t6` | Tabelle volle Breite, Zeilen zum Wort, ja/nein-Pillen mit Haken/Kreuz, Belege mit Rn.; Verweispille 088/090 | – | `… › 3. Typische Normen: drittschützend?` | 14 | – |
| **I 4. Grundrechte** `grund` | „nur hilfsweise“, „zuerst entscheidet das einfache Gesetz“ (4 C 3.08 Rn. 15) | tabler:`book`, `shield` (Lila) | `… › 4. Grundrechte nur hilfsweise` | 5 | – |
| **J Ergebnis** `erg`–`ri1` | Gericht; „Lärmschutz im Gaststättengesetz“, „Frau Brüning: klagebefugt“ + Haken; Richter kommt, Blase; „Begründetheit: offen“ | fluent-hc:`classical-building` | `Ergebnis · Frau Brüning ist klagebefugt` | 7 | – |
| **K Klausurtipp** `tipp`–`tipp2` | Lexi warnt; Schutznorm schon in der Klagebefugnis; Begründetheit nur drittschützende Normen + Kreuz | Warnsymbol (Streamline Freehand) | `Klausurtipp · Schutznorm schon in der Klagebefugnis`, `Klausurtipp · Begründetheit` | 11 | – |
| **L Schema** `sch`–`s4` | progressiv 1.–4. mit a)–c), Gliederungspunkt zur Marke, Inhalt zum Wort | – | `Schema · Klagebefugnis Dritter` | 15 | – |
| **M Merksatz** `merke`–`m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | 5 | – |

## Sachverhaltskarte

„Frau Brüning wohnt in einem Haus in einer ruhigen Wohnstraße in Nordrhein-Westfalen. Im Nachbarhaus eröffnet Frau Hoppe eine Shisha-Bar, die auch Bier und Cocktails ausschenkt. Die Stadt erteilt Frau Hoppe die Gaststättenerlaubnis für die Gasträume und eine Terrasse mit 40 Plätzen, Betrieb bis 24 Uhr. / Die Terrasse liegt direkt unter dem Schlafzimmerfenster von Frau Brüning. Sie befürchtet, nachts nicht mehr schlafen zu können, und erhebt fristgerecht Anfechtungsklage gegen die Gaststättenerlaubnis.“ – Frage: „Ist Frau Brüning klagebefugt?“ (kein Fiktiv-Hinweis)
