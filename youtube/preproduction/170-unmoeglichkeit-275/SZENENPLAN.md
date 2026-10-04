# Folge 170 · Unmöglichkeit § 275 BGB: Wenn die Leistung nicht mehr geht – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_170.py`](src/skript_170.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Der verkaufte Oldtimer brennt eine Nacht vor der Übergabe aus.“): Waldemar verkauft Adelheid privat seinen Oldtimer (genau diesen Wagen, Stückschuld) für 20.000 €; Übergabe und Zahlung am Samstag. In der Nacht davor brennt der Wagen in der Garage von Waldemar aus. Variante A: Blitzschlag. Variante B: Waldemar hat mit offener Flamme hantiert. Marktwert 25.000 €; die Versicherung zahlt Waldemar 25.000 €.

Ablauf: Fall (Verkauf, Nacht mit Varianten, Morgen mit Versicherung) → Frage → Sachverhalt → Aufbau (drei Schritte) → I. § 275 Abs. 1 (Wortlautkarte) → Unmöglichkeit im Fall (§ 433 Abs. 1, Stückschuld, objektiv/subjektiv, nachträglich, § 311a Abs. 1) → Rechtsfolge kraft Gesetzes, § 275 Abs. 2, 3 als Einrede → II. § 326 Abs. 1 Satz 1 (Wortlautkarte) → Ausnahmen § 326 Abs. 2, § 446, Rücktritt § 326 Abs. 5 (Verweis 116) → III. 1. § 283 Satz 1 (Wortlautkarte, Verweis 046) → Pflichtverletzung, Vermutung (Verweis 141/147), Variante B 5.000 €, Variante A nichts → III. 2. § 285 Abs. 1 (Wortlautkarte) → Commodum im Fall (§ 326 Abs. 3, § 285 Abs. 2) → Lösungstabelle → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:37,7 (5.709 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Waldemar, um 55 | privater Verkäufer, Schuldner | `standing/robot_dance-3` (Oberteil Blau `#8DB3F2`, Hose Dunkelgrau `#4A4A58`, offene Hand), Kopf `Short 2`, Brille `Glasses`, Haut `#E8B48E`, kein Bart; Mimiken `Calm`, `Smile` (redet), `Concerned|Serious` (Sorge, redet), `Fear`, `Tired`, `Suspicious`, `Smile Big|Smile`, `Serious` | `stephan` (Mann, mittel) |
| Adelheid, um 65 | private Käuferin, Gläubigerin | `standing/blazer-2` (Blazer Grün `#8FD694`, Oberteil Weiß, Beinprothese der Pose), Kopf `Gray Medium` (Haar `#BDBDBD`), Brille `Glasses 2`, Haut `#F0CDB0`; Mimiken `Calm`, `Smile` (redet), `Serious` (bestimmt, redet), `Concerned|Serious`, `Awe`, `Suspicious`, `Smile Big|Smile` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle `.py/.md/.json` in `youtube/preproduction`: 0 Treffer, und gegen die Koordinatorliste): Waldemar, Adelheid. Verworfen: Henrike (in fünf Szenenplänen als Kandidat genannt), Ortwin. Kein Genitiv eines Namens im Sprechtext („in der Garage“, „die Ansprüche von Adelheid“, „Die Versicherung zahlt Waldemar“). Die Figuren nennen keine Namen.
- **Stimmen nur aus dem Pool** stephan, hilde, christian, lucy: `stephan` (Waldemar, freundlich, dann besorgt) und `hilde` (Adelheid, älter, bestimmt). `christian` nicht besetzt (keine zweite Männerrolle; damit auch keine Szene stephan/christian), `lucy` (jung) passt nicht zur Käuferin um 65. Vorfolge 169: ela_froh/helmut – keine Überschneidung.
- Präfixe `WA_`/`AD_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen blickt Waldemar nach rechts zu Adelheid (`_r`), Adelheid nach links zu ihm; in Variante B blickt Waldemar nach links zur Garage; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `WA_redet`, `WA_sorge_redet`, `AD_redet`, `AD_bestimmt` (je links/rechts) und Lexi. Keine Bärte, keine Karikatur. Die Prothesen-Pose trägt die Käuferin (keine Täterrolle). **Keine weiteren Menschen im Bild.**
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 167 (`resting-1`, `blazer-1`), 168 (`crossed_arms-1`, `blazer-4`, `pointing_finger-1`), 169 (`doctor-nurse-02`, `shirt-4`) und 166 (`resting-2`, `pointing_finger-2`, `blazer-3`, `walking-1`); keine Polka Dots. Figurenrezepte verglichen.
- Figuren-PNGs: `../peeps/op_170/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 169 (Apotheke, Gericht), 168 (Gerichtssaal/Kanzlei, Frist), 167 (Urkunde/Kopie), 166 (Weinversteigerung). Hier neu: **Garage** (programmatisch: Wand, Satteldach, offenes Tor) mit dem Oldtimer als neutralem Tabler-Auto (Lila, ausgebrannt Grau). Leitmotiv: derselbe Wagen in drei Zuständen (heil – ausgebrannt – Versicherungsersatz). **Cremegrund durchgehend:** Die Nacht wird nur durch Mond-Icon und Pille „Nacht vor der Übergabe“ angezeigt, kein Nachtverlauf. Brand nur angedeutet (kleine Flamme und Rauchwolke am Dach), keine Verletzten.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Der Verkauf** `fall`–`ad1` | ab 0,0 s: Garage mit Oldtimer, Waldemar und Adelheid mit Namensschild; Pillen „Privatverkauf“, „genau dieser Wagen“, „Kaufpreis: 20.000 €“, „Übergabe und Zahlung: Samstag“ zum Wort; Blasen Waldemar „Am Samstag gehört er Ihnen. / Bis dahin steht er sicher / in meiner Garage.“, Adelheid „Gut. Dann bringe ich / die 20.000 € mit.“ | tabler:`car` (Lila), `calendar-event`; Garage programmatisch | `Fall · Der Verkauf` | – |
| **A2 Die Nacht** `nacht`–`varB` | „Nacht vor der Übergabe“ + Mond; kleine Flamme und Rauch am Dach bei „brennt“; Wagen grau bei „vollständig“, „Oldtimer ausgebrannt“; „Variante A: Blitzschlag“, Gewitterwolke bei „Blitz“ (bis Variante B); „Variante B: offene Flamme“, Waldemar erscheint (ernst), Feuerzeug an seiner Hand bei „offener“ | tabler:`moon-stars` (Gelb), `flame` (Rot), `cloud-fog`, `cloud-bolt`, `lighter` (Rot) | `Fall · Die Nacht` → `· Variante A: Blitzschlag` → `· Variante B: offene Flamme` | `szene_170donner_1` bei „Blitz“, `szene_170feuerzeug_1` bei „offener“ |
| **A3 Am Morgen / Frage** `wa2`–`frage2` | ausgebrannter Wagen, Rauchrest; Blase Waldemar „Der Wagen ist ausgebrannt. / Ich kann ihn Ihnen / nicht mehr geben.“, Blase Adelheid „Dann zahle ich auch nichts. / Aber er war / 25.000 € wert!“; „Marktwert: 25.000 €“, „Versicherung zahlt Waldemar 25.000 €“ + Schild; Pillen „Muss Waldemar noch liefern, muss Adelheid noch zahlen?“, „Und was kann sie verlangen?“ | tabler:`car` (Grau), `cloud-fog`, `shield-check` (Grün) | `Fall · Am Morgen` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ≈ 9,7 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Aufbau** `plan`–`p3` | Tafel „Unmöglichkeit: drei Schritte“: I. Anspruch auf den Wagen / II. Kaufpreis / III. Ansprüche auf Ersatz | tabler:`list-numbers`, `car`, `coin-euro`, `shield-check` | `Unmöglichkeit, § 275 BGB › Aufbau` | – |
| **D § 275 Abs. 1** `w275` | Wortlautkarte, Marker „ausgeschlossen“, „für den Schuldner“, „für jedermann“, „unmöglich“; Block „unmöglich: Anspruch ausgeschlossen“ | tabler:`scale`, `car-off` | `I. Anspruch auf den Wagen › § 275 Abs. 1 BGB` | – |
| **E Unmöglichkeit im Fall** `u1`–`u6` | ✓ Anspruch auf Übergabe und Übereignung (§ 433 Abs. 1); ✓ Stückschuld, kein anderer Wagen; ✓ objektiv, subjektiv; ✓ nachträglich; „schon vorher? Vertrag trotzdem wirksam, § 311a Abs. 1 BGB“ | tabler:`key`, `car`, `car-off`, `calendar-event`, `file-certificate` | `I. … › § 433 Abs. 1 BGB` → `I. Unmöglichkeit › Stückschuld` → `› objektiv, subjektiv` → `› nachträglich` | – |
| **F Rechtsfolge** `rf1`–`rf5` | Block „Anspruch ausgeschlossen, kraft Gesetzes“; ✓ „muss sich nicht darauf berufen“ (BT-Drucks. 14/6040 S. 129); Abs. 2, Abs. 3; Block „Schuldner kann nur verweigern: Einrede“ | tabler:`scale`, `hand-stop` | `I. Rechtsfolge › kraft Gesetzes` → `› § 275 Abs. 2, 3 BGB` | – |
| **G § 326 Abs. 1 Satz 1** `g1`–`g2` | Wortlautkarte, Marker „nicht zu“, „entfällt“, „Anspruch auf die Gegenleistung“; ✓ „Adelheid muss die 20.000 € nicht zahlen“, „in beiden Varianten“ | tabler:`coin-euro` | `II. Kaufpreis › § 326 Abs. 1 Satz 1 BGB` → `› der Fall` | – |
| **H Ausnahmen** `g3`–`g5` | § 326 Abs. 2 (zwei Fälle), ✗ beides nicht; § 446, ✗ nicht übergeben; Block Rücktritt § 326 Abs. 5 ohne Frist; Block „Mehr dazu: Video „Rücktritt § 323 BGB““ | tabler:`user-question`, `key`, `arrow-back-up` | `II. Kaufpreis › Ausnahmen, § 326 Abs. 2 BGB` → `› Gefahrübergang, § 446 BGB` → `› Rücktritt, § 326 Abs. 5 BGB` | – |
| **I § 283 Satz 1** `s1`–`s046` | Wortlautkarte, Marker „unter den Voraussetzungen“, „des § 280 Abs. 1“, „Schadensersatz statt der Leistung“; Block „Mehr dazu: Video „Das System der §§ 280 ff.““ | tabler:`scale`, `list-numbers` | `III. 1. Schadensersatz › § 283 Satz 1 BGB` | – |
| **J Subsumtion** `s2`–`va` | ✓ Pflichtverletzung; Vertretenmüssen vermutet (§ 280 Abs. 1 Satz 2); Block Verweis Beweislast/Anscheinsbeweis; ✓ Variante B fahrlässig, Rechnung 25.000 € - 20.000 € = 5.000 €, Block „Variante B: 5.000 € Schadensersatz“; ✗ Variante A, „kein Schadensersatz“ | tabler:`car-off`, `scale`, `lighter`, `coin-euro`, `cloud-bolt` | `III. 1. Schadensersatz › Pflichtverletzung` → `› Vertretenmüssen` → `› Variante B` → `› Variante A` | – |
| **K § 285 Abs. 1** `c1`–`w285` | Wortlautkarte (6 Zeilen), Marker „infolge des Umstands“, „für den geschuldeten Gegenstand“, „Ersatz oder einen Ersatzanspruch“, „Herausgabe“, „Abtretung“ | tabler:`bulb` (Klausurclou), `shield-check` | `III. 2. Stellvertretendes Commodum › § 285 Abs. 1 BGB` | – |
| **L Commodum im Fall** `c2`–`c7` | ✓ Versicherungszahlung = Ersatz (BT-Drucks. 14/6040 S. 144); ✓ kein Vertretenmüssen, auch A; 25.000 € verlangen, 20.000 € zahlen (§ 326 Abs. 3 Satz 1); Block „unterm Strich: 5.000 €“; Variante B § 285 Abs. 2 | tabler:`shield-check`, `cash-banknote`, `coin-euro`, `calculator`, `scale` | `III. 2. Commodum › Versicherung` → `› Gegenleistung, § 326 Abs. 3 BGB` → `› Variante B, § 285 Abs. 2 BGB` | – |
| **M Lösung** `loes`–`l4` | Tabelle Variante A/B: Wagen ausgeschlossen/ausgeschlossen; Kaufpreis entfällt/entfällt; Schadensersatz ✗/✓ 5.000 €; Ersatz § 285 ✓ „ja, aber zahlen“ in beiden – je Zeile zum Wort | tabler:`table`, `coin-euro`, `shield-check` | `Lösung › beide Varianten` | – |
| **N Klausurtipp** `tipp`–`t3` | hellgelbe Tafel, Lexi warnt: „Reihenfolge einhalten: 1. Primäranspruch 2. Gegenleistung 3. Schadensersatz und Commodum“ | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge` | – |
| **O Klausurschema** `sch`–`k32` | breite Karte: I. Anspruch auf Übergabe und Übereignung (§ 433 Abs. 1) – ausgeschlossen nach § 275 Abs. 1; II. Anspruch auf den Kaufpreis – entfallen nach § 326 Abs. 1 – Ausnahmen § 326 Abs. 2; III. Sekundäransprüche – 1. Schadensersatz statt der Leistung, mit Vertretenmüssen (§§ 280, 283) – 2. Herausgabe des Ersatzes, mit Gegenleistung (§§ 285, 326 III); jede Zeile zum Wort | – | `Klausurschema` → `› I. Primäranspruch` → `› II. Kaufpreis` → `› III. Sekundäransprüche` | – |
| **P Merksatz** `merke`–`mk4` | Lexi erklärt; Marker „fällt der Anspruch weg“, „der Kaufpreis.“, „Schadensersatz gibt es nur / bei Vertretenmüssen,“, „den Ersatz nach § 285 auch ohne.“ | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („20.000 €“, „25.000 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern; Normwortlaut wörtlich.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Waldemar verkauft Adelheid privat seinen Oldtimer, genau diesen einen Wagen, für 20.000 Euro. Übergabe und Zahlung sollen am Samstag sein. Bis dahin steht der Wagen in der Garage von Waldemar.
>
> In der Nacht vor der Übergabe brennt es in der Garage; der Oldtimer brennt vollständig aus. Variante A: Ein Blitz hat eingeschlagen. Variante B: Waldemar hat am Abend in der Garage mit offener Flamme hantiert.
>
> Der Wagen war 25.000 Euro wert. Die Versicherung zahlt Waldemar für den Wagen 25.000 Euro. Adelheid will nichts zahlen und fragt, was sie verlangen kann.
>
> **Muss Waldemar noch liefern, muss Adelheid noch zahlen – und was kann sie verlangen?**
