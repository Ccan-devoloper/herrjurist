# Folge 195 · Kostenentscheidung ZPO: Kostenquote nach §§ 91, 92 – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_195.py`](src/skript_195.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“ (Urteilstenor aus Sicht des 2. Examens). Beispielfall nach dem Plan-Hook („Der Kläger verlangt 10.000 Euro und bekommt 7.300 Euro zugesprochen“), Werklohnklage: Malermeister Herr Dressler streicht die Fassade am Haus von Frau Lindau und berechnet 10.000 €, davon 2.700 € für die Garage; Frau Lindau zahlt nichts. Das Amtsgericht spricht 7.300 € zu, weil ein Auftrag für die Garage nicht bewiesen ist. Ablauf: Fall → Urteil in der Hauptsache und Frage → Sachverhalt → Grundsatz § 91 Abs. 1 S. 1 (Wortlaut) → Teilunterliegen § 92 Abs. 1 S. 1 (Wortlaut) → Quote rechnen (Balken, 27 % / 73 %) → Prozent oder Bruch, Kostentenor → Kostenaufhebung (§ 92 Abs. 1 S. 2, Wortlaut) → Ausnahme § 92 Abs. 2 (Wortlaut Nr. 1, Skala mit Faustregel 10 % als Literaturangabe, Nr. 2 ein Satz) → vier Sonderregeln (§§ 93, 91a, 269 Abs. 3 S. 2, 344; Wortlautkarten) → Klausurtipp (Lexi; § 308 Abs. 2, Verweis vorläufige Vollstreckbarkeit) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 5:19,4; 106 eigenständige Bildhalte (Skript 4.464 Zeichen) – Regelumfang, keine Begründung für Überlänge nötig.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Dressler (DR), um 50 | Malermeister, Kläger | Pose `standing/pointing_finger-2` (schwarzes Oberteil, helle Malerhose `#F2EFE8`, erhobener Zeigefinger), Kopf `Short 3`, Haut `#EBBE9B`, kein Bart, keine Brille; Mimiken `Calm` (ruhig), `Smile` (froh), `Serious` (denkt), `Concerned\|Serious` (Sorge), `Suspicious` (skeptisch), `Driven` (redet), `Concerned\|Serious` (fragt, redet) | `marc` (Mann, mittel) |
| Frau Lindau (LI), um 45 | Hauseigentümerin, Beklagte | Pose `standing/crossed_arms-1` (Oberteil Koralle `#F07A6A`, schwarze Hose, verschränkte Arme), Kopf `Medium Straight`, Haut `#D9A07A`; Mimiken `Calm`, `Smile`, `Serious`, `Concerned\|Serious`, `Very Angry` (Ärger, Mund zu), `Suspicious` (redet) | `sabrina` (Frau, mittel) |
| Richterin (RI), um 55, ohne Namen | Amtsgericht: verkündet den Hauptsachetenor | Pose `standing/blazer-3` (dunkler Blazer und Hose `#3A3A48` wie eine Robe), Kopf `Medium 2` (Haar Grau), Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm`, `Suspicious` (denkt), `Serious` (redet) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Herr Dressler blickt nach rechts zu Frau Lindau, sie nach links zu ihm; Szene B: Kläger links (blickt nach rechts zur Richterin), Beklagte rechts (blickt nach links), Richterin hinter dem Richtertisch; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `DR_redet`, `DR_fragt`, `LI_redet`, `RI_redet` (je links/rechts) und Lexi. `pointing_finger-1` verworfen (Kleidung dort vollständig schwarz und nicht einfärbbar).
- **Stimmen nur aus dem Pool** (`william`, `sabrina`, `marc`, `laura_ruhig`); `william` nicht gebraucht. Vorfolge 194 nutzt `stephan`/`lucy`, 193 `helmut`/`niklas`, 192 `hilde`/`lucy` – keine Überschneidung mit den Vorfolgen 192–194.
- **Namen mit eindeutig deutscher Aussprache, neu:** Dressler, Lindau (nicht in der Liste vergebener Namen; Volltextsuche über `youtube/` ohne Treffer). Die Richterin bleibt namenlos. Gesprochen nur von der Erzählerin, nie von den Figuren.
- Figuren-PNGs: `../peeps/op_195/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 191 (`easing-2`, `walking-1`), 192 (Kleingarten; `shirt-3`, `blazer-2`), 193 (`shirt-3`, `shirt-4`). Hier **Haus mit Garage** (Malerarbeiten: Farbrolle, Farbeimer, Rechnung) und **Sitzungssaal des Amtsgerichts** (Richtertisch, Akte); Posen `pointing_finger-2`, `crossed_arms-1`, `blazer-3` in 191–193 nicht verwendet; keine Polka Dots, keine Bärte. Der Sitzungssaal kehrt gegenüber 048 erzählerisch zwingend zurück (die Kostenentscheidung ist Teil des Urteils), Aufbau mit beiden Parteien links und rechts statt leerem Stuhl. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Am Haus** `fall`–`dr1` | Bodenlinie, Haus, Garage, Farbeimer, Herr Dressler (ab 0,0 s mit Namensschild); Fassade mit Farbrolle; „Garage?“; Frau Lindau; Rechnung 10.000 €; „zahlt nichts“; Blasen Lindau/Dressler | ph:`house` (Weiß/Blau), ph:`garage` (Weiß/Grau), ph:`paint-bucket` (Gelb), ph:`paint-roller` (Gelb), tabler:`file-invoice` (Weiß), tabler:`sun` (Gelb) | `Fall · Der Malermeister` → `Fall · Fassade und Garage` → `Fall · Rechnung: 10.000 €` → `Fall · Frau Lindau zahlt nichts` → `Fall · Frau Lindau bestreitet` → `Fall · Herr Dressler will klagen` | 12 | – |
| **B Amtsgericht** `klage`–`frage2` | Richterin hinter dem Richtertisch, Akte fällt auf den Tisch, Kläger links, Beklagte rechts; „Klage: 10.000 € Werklohn“, „Fassade: in Ordnung“, „Garage: kein Auftrag bewiesen“; Blase der Richterin (Hauptsachetenor); „verlangt / bekommen“; Frage | tabler:`file-text` (Akte, bewegt) | `Fall · Die Klage: 10.000 € Werklohn` → `Fall · Nach der Beweisaufnahme` → `Fall · Das Urteil in der Hauptsache` → `Fall · 10.000 € verlangt, 7.300 € bekommen` → `Fall · Wer trägt die Kosten?` | 10 | Akte auf dem Richtertisch (`szene_195akte_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D Grundsatz** `p91`–`hier91` | Wortlautkarte § 91 Abs. 1 S. 1 mit vier Markern, Unterliegensprinzip, Gerichtskosten/notwendige Kosten (Haken), „Hier: Keiner hat ganz verloren.“ | tabler:`scale`, `receipt-euro`, `chart-pie` | `Grundsatz · § 91 Abs. 1 S. 1 ZPO` → `› Unterliegensprinzip` → `› Gerichtskosten und notwendige Kosten des Gegners` → `› hier: keiner hat ganz verloren` | 10 | – |
| **E Teilunterliegen** `p92`–`teilen` | Wortlautkarte § 92 Abs. 1 S. 1 mit vier Markern; Blöcke „Alternative: Kostenaufhebung“ (beim Wort „gegeneinander“) und „Normalfall: Teilen nach Quote“ | tabler:`chart-pie`, `calculator` | `Teilunterliegen · § 92 Abs. 1 S. 1 ZPO` → `› Normalfall: Teilen nach Quote` | 6 | – |
| **F Quote rechnen** `rech`–`basis` | Streitwert 10.000 €; Balken füllt sich: 2.700 € rot, 7.300 € gelb; Rechnung 2.700 : 10.000 = 27 %; Kläger 27 %, Beklagte 73 %; Blase Dressler; „Quote = Unterliegen : Streitwert“ | tabler:`calculator`, `percentage`, `chart-pie`; ph:`garage`, `house` | `Kostenquote · rechnen` → `› Streitwert: 10.000 €` → `› Kläger verliert 2.700 €` → `› 2.700 € : 10.000 € = 27 %` → `› Beklagte verliert 7.300 €: 73 %` → `› Unterliegen gemessen am Streitwert` | 10 | – |
| **G Prozent oder Bruch, Kostentenor** `bruch`–`tenor` | Blöcke Prozent / Bruch, glatte Anteile ¼ zu ¾ (OLG Hamm 24 U 53/06), 27/100 schwer lesbar (Kreuz), hier Prozent (Haken), Tenorkasten | tabler:`percentage`, `math-x-divide-y`, `file-text` | `Kostentenor · Prozent oder Bruch?` → `› hier: Prozent` → `› Formulierung` | 6 | – |
| **H Kostenaufhebung** `aufh`–`aufh3` | Wortlautkarte § 92 Abs. 1 S. 2 mit zwei Markern, eigene Anwaltskosten (Haken), „passt vor allem bei etwa hälftigem Gewinn“; Richterin und Herr Dressler | ph:`scales`, tabler:`building-bank`, `chart-pie` | `Kostenaufhebung · § 92 Abs. 1 S. 1 Alt. 1 ZPO` → `› § 92 Abs. 1 S. 2 ZPO` → `› wenn beide etwa zur Hälfte gewinnen` | 6 | – |
| **I Ausnahme § 92 Abs. 2** `p922`–`nr2` | Frage; Wortlautkarte Nr. 1 mit drei Markern; „beides muss vorliegen“ (AG Königs Wusterhausen); Skala 0–30 % mit grüner Zone bis 10 % „Faustregel (Literatur)“; roter Zeiger „hier: 27 %“; Kreuz; Nr. 2 | ph:`scales`, tabler:`percentage-10`, `percentage`, `zoom-question` | `Ausnahme · § 92 Abs. 2 ZPO` → `› Nr. 1: geringfügige Zuvielforderung` → `› Nr. 1: beides muss vorliegen` → `› Faustregel: bis etwa 10 %` → `› hier 27 %: nicht geringfügig` → `› Nr. 2: Ermessen, Sachverständige, Berechnung` | 10 | – |
| **J Vier Sonderregeln** `sonder`–`vu` | vier Normpillen, je Regel eine Wortlautkarte mit Markern und Kernsatz, Hinweis auf das Video zum Versäumnisurteil; Richterin und Frau Lindau | tabler:`list-check`, `circle-check`, `arrow-back-up`; ph:`handshake`, `chair` | `Sonderregeln · vier Fälle` → `› § 93: sofortiges Anerkenntnis` → `› § 91a: Erledigung der Hauptsache` → `› § 269 Abs. 3 S. 2: Klagerücknahme` → `› § 344: Versäumniskosten` | 16 | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet): „Vergiss den Kostentenor nie!“, Wortlautkarte § 308 Abs. 2, Verweis vorläufige Vollstreckbarkeit | Warnsymbol (Streamline Freehand) | `Klausurtipp · Kostentenor nie vergessen` → `› § 308 Abs. 2 ZPO` → `› danach: vorläufige Vollstreckbarkeit` | 5 | – |
| **L Schema** `sch`–`k5` | baut sich Zeile für Zeile auf: 1. Grundsatz – 2. Teilunterliegen (Quote) – 3. Ausnahme – 4. Sonderregeln – 5. Kostentenor | – | `Schema` → `Schema › 1. Grundsatz` … `Schema › 5. Kostentenor` | 9 | – |
| **M Merksatz** `merke`–`m2` | Lexi erklärt (redet), Merksatz mit drei Markern | – | `Merksatz` | 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Akte fällt auf den Richtertisch). Das erste Bild nach dem Intro ist ab 0,0 s vollständig (Haus, Garage, Farbeimer, Sonne, Herr Dressler mit Namensschild, Prüfpfad).
**Geräusche:** ein Handlungsgeräusch (Akte), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig, kein Fiktiv-Hinweis)

> Malermeister Herr Dressler streicht im April 2026 die Fassade am Haus von Frau Lindau. Nach seiner Darstellung hat sie auch den Anstrich ihrer Garage bestellt. Er stellt 10.000 Euro in Rechnung: 7.300 Euro für die Fassade, 2.700 Euro für die Garage.
>
> Frau Lindau zahlt nichts: Die Fassade sei fleckig, die Garage habe sie nie bestellt. Herr Dressler klagt vor dem Amtsgericht auf Zahlung von 10.000 Euro Werklohn; Zinsen verlangt er nicht.
>
> Nach der Beweisaufnahme steht fest: Die Fassade ist mangelfrei, der Werklohn dafür ist fällig. Einen Auftrag für die Garage kann Herr Dressler nicht beweisen. Das Gericht verurteilt Frau Lindau zur Zahlung von 7.300 Euro und weist die Klage im Übrigen ab.
>
> **Wer trägt die Kosten des Rechtsstreits, und wie lautet der Kostentenor?**
