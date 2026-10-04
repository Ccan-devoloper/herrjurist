# Folge 141 · Beweislast ZPO: Wer verliert beim non liquet? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_141.py`](src/skript_141.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“. Hook nach Plan: Zwei Zeugen widersprechen sich exakt, niemand weiß, ob das Darlehen ausgezahlt wurde. Beispielfall: Herr Wiedemann klagt gegen Frau Krause auf Rückzahlung von 5.000 € (§ 488 Abs. 1 S. 2 BGB); die Barauszahlung ohne Quittung ist streitig; Zeuge Herr Reichert (Übergabe) und Zeugin Frau Fischer (keine Übergabe) sind gleich glaubwürdig. Ablauf: 1. streitige Tatsache (Verweis 018) → 2. freie Beweiswürdigung § 286 Abs. 1 ZPO (Wortlautkarte, BGH-Formel) → 3. non liquet → 4. Beweislast: Normentheorie, Sonderregeln, subjektive Beweislast (Verweis 103) → 5. Fall und Gegenvariante Rückzahlung → 6. Formulierung im Urteil → Klausurtipp → Schema mit Waage → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Wiedemann (WI), um 65 | Darlehensgeber, Kläger | `standing/blazer-4`, Kopf `No Hair 2`, Brille `Glasses 2`; Sakko Blau `#8DB3F2`, Shirt Weiß, schwarze Hose, Haut `#EDC3A3`; Mimiken `Calm`, `Smile`, `Serious`, `Suspicious`, `Concerned\|Serious`, `Tired`; spricht mit `Driven` | `helmut` (Mann, älter) |
| Frau Krause (KR), um 35 | Darlehensnehmerin, Beklagte, spricht nicht | `standing/crossed_arms-2` (verschränkte Arme: sie bestreitet), Kopf `Long Curly` (Haar `#4A3222`); schwarzes Oberteil, Hose Lila `#B8A9F5`, Haut `#F0C29E`; Mimiken `Calm`, `Serious`, `Suspicious`, `Concerned\|Serious`, `Smile`, `Fear` | – |
| Herr Reichert (RT), um 30 | Zeuge des Klägers | `standing/easing-1`, Kopf `Short 3`; offenes Hemd Grün `#8FD694` über gelbem Shirt, schwarze Hose, Haut `#E0AC84`; spricht mit `Serious` | `niklas` (Mann, jung) |
| Frau Fischer (FI), um 30 | Zeugin der Beklagten | `standing/robot_dance-2`, Kopf `Medium Straight`, Brille `Glasses 3`; schwarzes Oberteil, Hose Grün `#8FD694`, Haut `#C68E6A`; spricht mit `Serious` | `julia` (Frau, jung) |
| Richterin (RI), um 55, ohne Namen und Text | Beweisaufnahme, non liquet, Urteil | `standing/blazer-3`, Kopf `Gray Bun`; dunkles Sakko `#3A3A48`, Hose Graublau `#5B6B8C`, Haut `#F2D3BD`; Mimiken `Calm`, `Serious`, `Suspicious` | – |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e (Explaining / Concerned Fear / Hectic, Schnitt bei 60 %) nur in `WI_redet`, `RT_redet`, `FI_redet` (je links/rechts) und Lexi. Keine Prothesen-Posen, keine Bärte, keine Polka Dots. Stimmen nur aus dem Pool (helmut, niklas, julia; `ela_froh` nicht verwendet, weil keine heitere Rolle). Namen mit eindeutig deutscher Aussprache, nicht aus früheren Folgen. Figuren-PNGs: `../peeps/op_141/` (74 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen (138: `resting-1`, `blazer-1`; 139: `robot_dance-3`, `pointing_finger-2`; 140: `crossed_arms-1`, `walking-1`) nicht wiederholt; `crossed_arms-2` und `robot_dance-2` sind andere Varianten (andere Kleidung). Keine Muster.
- Schauplätze neu: Sitzungssaal mit Richtertisch „Gericht“ in der Mitte und den Zeugen links und rechts (in 018 standen Parteien und Zeuge anders; Rückkehr in den Saal, weil der Hook die Beweisaufnahme ist), Küche von Frau Krause am Abend (Kühlschrank, Küchentisch, Mond), freie Bühne für Klage und Frage mit Waage.
- Wiederkehrendes Diagramm dieser Folge: Balkenwaage im Gleichstand (programmatisch, `waage()`), als Bild für das non liquet.
- Cremegrund durchgehend; der Abend wird nur durch das Mond-Icon gezeigt, kein Nachtverlauf.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Im Sitzungssaal** `fall`–`niemand` | Richtertisch Mitte, Herr Reichert links (blickt nach rechts), Frau Fischer rechts (blickt nach links) | Richtertisch (Pastellblock), tabler:`cash-banknote` (Grün), `question-mark` | `Fall · Im Sitzungssaal` → `Fall · Aussage gegen Aussage` | Richterin ab 0,0 s · Zeugen treten auf · „eine Frage“ · „zwei Antworten“ · Reichert redet (Blase) · Fischer redet (Blase) · Geldschein · „ausgezahlt?“ | – |
| **A2 In der Küche** `streit`–`wi1` | Frau Krause links, Herr Wiedemann rechts, Küchentisch Mitte, Kühlschrank links | tabler:`fridge` (Weiß), `moon` (Gelb), `mail` (Umschlag, Weiß), `question-mark`, `receipt-off` | `Fall · Das Darlehen` → `Fall · Der Abend in der Küche` | Darlehen 5.000 € · rückzahlbar · Abend (Mond) · Umschlag auf dem Tisch · „bar übergeben?“ · keine Quittung · Wiedemann redet (Blase) | Umschlag rutscht auf den Tisch (`szene_141umschlag_1`) |
| **A3 Klage und Frage** `best`–`frage` | freie Bühne, Krause links, Wiedemann rechts | tabler:`cash-banknote-off` (Rot), `building-bank` (Amtsgericht), Waage | `Fall · Das Bestreiten` → `Fall · Die Klage` → `Fall · Die Frage` | „nie Geld bekommen“ · Wiedemann tritt auf · Amtsgericht · Klage 5.000 € · Waage mit beiden Zeugen · „gleich glaubwürdig“ · „Wer verliert?“ | – |
| **B Sachverhalt** `sv` | Sachverhaltskarte vollständig, 4,8 s Lesepause | – | `Sachverhalt` | 1 | – |
| **C Aufbau** `plan`–`s6` | Tafel links, Wiedemann und Krause rechts | tabler:`list-numbers`, `bulb`, `question-mark`, `scale`, `cash-banknote`, `file-text` | `Beweislast › Aufbau` | sechs Schritte nacheinander, Requisit wechselt je Schritt | – |
| **D 1. Streitige Tatsache** `st1`–`st5` | Tafel, Wiedemann/Krause | tabler:`scale`, `coin-euro`, `file-check`, `cash-banknote` | `1. Streitige Tatsache` → `› § 488 Abs. 1 S. 2 BGB` → `› die Auszahlung` | Verweis 018 · Anspruch · Wortlautkarte § 488 I 2 (Markierung „zur Verfügung gestellte“) · Vereinbarung ✓ · Fälligkeit ✓ · „streitig: allein die Auszahlung“ · „ohne Auszahlung nichts zurückzuzahlen“ | – |
| **E 2. § 286 Abs. 1 ZPO** `bw`, `w286` | Tafel, Reichert/Fischer | tabler:`scale`, `bulb` | `2. Freie Beweiswürdigung` → `› § 286 Abs. 1 ZPO` | Wortlautkarte, Hervorhebungen „gesamten“, „freier Überzeugung“, „für wahr“, „für nicht wahr“ synchron · „wahr oder nicht wahr?“ | – |
| **F 2. Maßstab, Aussage gegen Aussage** `voll`–`gleich` | Tafel mit Waage, Reichert/Fischer | tabler:`shield-check`, `messages`, `scale` | `› volle Überzeugung` → `› Aussage gegen Aussage` | volle Überzeugung · keine absolute Gewissheit · BGH-Formel zeilenweise mit Az./Rn. · Waage „Geld übergeben“/„kein Geld“ · „Gleichstand“ | – |
| **G 3. Non liquet** `nl`–`nl4` | Tafel, Richterin rechts | tabler:`question-mark`, `file-text`, `scale` | `3. Non liquet` → `› Urteil, § 300 Abs. 1 ZPO` → `› jetzt erst: Beweislast` | Übersetzung · nicht überzeugt … ✗ Auszahlung ✗ Gegenteil · ✓ Urteil § 300 I · „jetzt erst entscheidet die Beweislast“ · „Unklarheit zulasten …“ | – |
| **H 4. Normentheorie** `nt`–`nt4` | Tafel, Wiedemann/Krause | tabler:`scale`, `coin-euro`, `shield-check` | `4. Beweislast › Normentheorie` → `› Kläger: anspruchsbegründend` → `› Beklagter: …` | Normentheorie (Leo Rosenberg) · BGH-Zitat mit Az./Rn. · Kläger-Block · Beklagter: rechtshindernde, -vernichtende, -hemmende nacheinander · Verweis 103 | – |
| **I 4. Sonderregeln, subjektive Beweislast** `sonder`–`subj2` | Tafel, Wiedemann (bei `subj2` kommt Reichert dazu) | tabler:`book`, `file-text`, `receipt`, `key`, `user-check` | `› gesetzliche Sonderregeln` → `› subjektive Beweislast` | § 280 I 2 · § 477 · § 1006 · Beweisführungslast · „Herr Wiedemann: Zeuge Herr Reichert benannt“ ✓ | – |
| **J 5. Der Fall** `fall5`–`f4` | Tafel mit Waage, Wiedemann/Krause | tabler:`cash-banknote`, `scale`, `file-x` | `5. Der Fall › …` | Auszahlung = Voraussetzung ✓ · anspruchsbegründend · Beweislast Kläger · Waage non liquet, „zu seinen Lasten“ · „Klage abgewiesen“ | – |
| **K 5. Gegenvariante** `gv`–`gv4` | Tafel mit Waage, Wiedemann/Krause | tabler:`arrow-back-up`, `circle-check`, `scale` | `5. Gegenvariante › …` | Rückzahlung behauptet · Auszahlung unstreitig ✓ · Erfüllung § 362 · rechtsvernichtend · Waage „Rückzahlung: non liquet“, Beweislast Beklagte · „Frau Krause wird verurteilt“ | – |
| **L 6. Im Urteil** `urt`–`u3` | Tafel, Richterin | tabler:`file-text`, `writing`, `list-numbers` | `6. Im Urteil` → `› § 286 Abs. 1 S. 2 ZPO` → `› Aufbau der Gründe` | übliche Formulierung (Fundstelle) · Wortlautkarte § 286 I 2 · 1. Warum überzeugt keine Aussage? · 2. Wer trägt die Beweislast? | – |
| **M Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi rechts | Streamline Freehand: Warnsymbol | `Klausurtipp · …` | Warnsymbol · Satz · 1. · 2. · Sonderregel/Vermutung | – |
| **N Klausurschema** `sch`–`k5` | breite Schema-Tafel (x ≤ 1820) mit Waage | Waage | `Klausurschema › I.` … `› V. Ergebnis` | I. bis V. nacheinander, IV. mit 1./2. · Waage mit „Beweislast?“ und „zulasten“ | – |
| **O Merksatz** `merke`, `mk2` | Merkkarte, Lexi rechts | – | `Merksatz` | Satz 1 · Markierung · Satz 2 · Markierungen | – |

## Sachverhaltskarte (Szene B)

Herr Wiedemann und Frau Krause vereinbaren ein zinsloses Darlehen über 5.000 €, rückzahlbar bis zum 31. März 2026. Herr Wiedemann sagt, er habe ihr das Geld an einem Abend in ihrer Küche bar in einem Umschlag gegeben. Eine Quittung gibt es nicht. Frau Krause bestreitet die Auszahlung: Sie habe nie Geld bekommen. Im April 2026 klagt Herr Wiedemann vor dem Amtsgericht auf Rückzahlung der 5.000 Euro. Vereinbarung und Fälligkeit sind unstreitig. Am Tisch saßen Herr Reichert, ein Bekannter von Herrn Wiedemann, und Frau Fischer, eine Freundin von Frau Krause. Herr Reichert sagt aus, das Geld sei übergeben worden; Frau Fischer sagt, es sei kein Geld übergeben worden. Beide wirken gleich glaubwürdig. Andere Beweise gibt es nicht. — Frage: Wer verliert, wenn sich die Auszahlung nicht klären lässt?

## Ton

Erzählerin und Lexi: Carla Blum. Figurenrede: Reichert (`re1`), Fischer (`fi1`), Wiedemann (`wi1`). Ein Handlungsgeräusch (Umschlag), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json). Schiebeblenden stumm.
