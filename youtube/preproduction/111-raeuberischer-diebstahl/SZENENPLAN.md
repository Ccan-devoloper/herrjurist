# Folge 111 · Räuberischer Diebstahl § 252 StGB: Gewalt auf der Flucht – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_111.py`](src/skript_111.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Format „Schema“. Fall nach dem Plan-Hook (Kopfhörer im Elektromarkt eingesteckt, draußen gestellt, Stoß, Flucht) → Frage → Sachverhalt (Grundfall, Gegenvariante) → Wortlautkarte § 252 und Aufbau → 1. Vortat (vollendet durch Einstecken, Verweis auf Folge 055; nicht beendet; warum kein Raub) → 2. auf frischer Tat betroffen (Streit Zuvorkommen in einem Satz, BGHSt 26, 95) → 3. Nötigungsmittel (Gewalt, Schubsen des Ladendetektivs) → 4. subjektiv (Vorsatz, Besitzerhaltungsabsicht) → Ergebnis, Rechtsfolge „gleich einem Räuber“, Konkurrenz → Gegenvariante (Beute weggeworfen) → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 087 (Raubschema, Abgrenzung § 252), 055 (Gewahrsamsenklave, nur verwiesen), 051 (Diebstahlsschema).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gottfried (GO), um 60 | Täter, steckt die Kopfhörer ein | `standing/easing-1` (offene Überjacke Lila `#B8A9F5` über weißem T-Shirt, schwarze Hose und Turnschuhe der Pose), Kopf `Gray Short` (helles, graues Haar), Haut `#EDC1A0`. Mimiken `Calm`, `Suspicious`, `Driven` (redet; entschlossen), `Serious`, `Fear` (ertappt), `Solemn` | `william` (Mann, älter) |
| Edda (ED), um 35 | Mitarbeiterin des Elektromarkts | `standing/pointing_finger-2` (schwarzes Oberteil der Pose, Hose Rot `#F07A6A`), Kopf `Bun`, Haut `#C68E62`. Mimiken `Calm`, `Serious` (redet), `Fear` (Schreck beim Stoß), `Concerned|Serious` (Sorge), `Awe`, `Smile` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts.
- Im Fall: Gottfried am Regal blickt zum Regal (links), Edda beobachtet ihn (blickt nach links), nach der Kasse dreht sie sich mit ihm (`_r`); draußen kommt Edda aus der Tür (blickt nach rechts), Gottfried dreht sich zu ihr (links), beim Davonrennen nach rechts.
- In den Tafelfolien steht Gottfried links (X 1440), Edda rechts (X 1740); Eddas Zeigefinger zeigt zur Tafel, nicht auf eine Person.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GO_redet`, `ED_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Waffe. 48 Figuren-PNGs in `../peeps/op_111/` (Drive-Master).
- **Klischeeprüfung:** Gottfried gewöhnlich gekleidet (Überjacke, T-Shirt), heller Hautton, älterer Mann statt des reflexhaften jungen Täters, keine „fiese“ Mimik; Edda sachlich und bestimmt, nach dem Stoß erschrocken, nicht leidend.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen oder Themenplan unter `youtube/` (03.10.2026): Gottfried, Edda („Hilde“ verworfen: Stimmenname im Ensemble). Im Sprechtext nie im Genitiv mit -s.
- **Stimmen** nur aus dem zugeteilten Pool (`william`, `sabrina`; `marc` sprach in 087 den Täter, `laura_ruhig` nicht gebraucht). Lea nicht verwendet.

**Abweichung von den letzten Folgen (107 WG-Flur und Geldautomat, 108 Marktplatz mit Gasthaus, 109 Café und Park im Herbst; 087 Weg vom Wochenmarkt; Kontaktbögen von 107 und 109 gesichtet):** neuer Schauplatz Elektromarkt (Regal mit Fernseher, Laptop, Handys, Kopfhörern; Kasse; Ausgang) und Gehweg vor dem Eingang (Fassade mit Schild „Elektromarkt“ ohne Logo, Tür, Baum). Posen `easing-1` und `pointing_finger-2` in 105–109 und 087 nicht verwendet; keine Polka Dots.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Markt** `fall`→`kasse` | Gottfried am Regal ab 0,0 s (Namensschild), Kopfhörer in der Hand, Pille „Kopfhörer · 129 €“, „in die Innentasche seiner Jacke“; Edda erscheint („Mitarbeiterin“, Augen); Gottfried hinter der Kasse auf dem Weg zum Ausgang, „vorbei, ohne zu bezahlen“ | fluent:`television`, `laptop`, `mobile-phone`, `headphone`, `receipt`, `credit-card`, `door`, `eyes`; tabler:`arrow-right` | `Fall · Im Elektromarkt` → `… · Gottfried steckt die Kopfhörer ein` → `… · An der Kasse vorbei` | ≈ 9 | – |
| **A2 vor dem Eingang** `drauss`→`frage2` | Edda stellt Gottfried (Blase „Halt! Die Kopfhörer in Ihrer Jacke gehören uns!“), greift nach der Jacke; Stoß nur als Abstand, Eddas Schreck und Warnsymbol („stößt Edda weg“, „damit sie ihm die Kopfhörer nicht abnimmt“); Gottfried: „Die Kopfhörer behalte ich!“; rennt nach rechts davon (Bewegungslinien), Edda „taumelt zurück, nicht verletzt“; Frage | fluent:`door`, `television`, `deciduous-tree`, `warning`; tabler:`hand-grab` | `Fall · Vor dem Eingang` → `… · Der Stoß` → `… · Gottfried rennt davon` → `… · Die Frage` | ≈ 13 | Laufschritte (`szene_111laufen_1`) |
| **B Sachverhalt** `sv` | Karte vollständig (Grundfall, Gegenvariante), ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p252`→`auf4` | Wortlautkarte § 252 (Marker blau Diebstahl, grün frische Tat, gelb Gewalt/Drohung, lila Besitzerhaltung, rot gleich einem Räuber), vier Blöcke Aufbau | fluent:`balance-scale`, `headphone` | `A. Räuberischer Diebstahl, § 252 StGB › Wortlaut` → `… › Aufbau` | ≈ 12 | – |
| **D 1. Vortat** `vt`→`p249c` | vollendet durch Einstecken, Beobachtung unschädlich, nicht beendet; Zeitleiste Vollendung/Beendigung, § 249 / § 252 | fluent:`headphone`, `coat`, `running-shoe`, `balance-scale`, `hourglass-not-done` | `A. § 252 StGB › I. Tatbestand › 1. Vortat: Diebstahl vollendet` → `… nicht beendet` → `Abgrenzung › Raub, § 249 StGB?` | ≈ 13 | – |
| **E 2. frische Tat** `ft`→`zuvor` | Definition, Subsumtion (+), Beobachtung unschädlich, Streitkarte Zuvorkommen | fluent:`stopwatch`, `door`, `eyes`, `balance-scale` | `… › 2. auf frischer Tat betroffen` → `… (+)` → `… › 2. Streit: Zuvorkommen` | ≈ 14 | – |
| **F 3. Nötigungsmittel** `nm`→`nm5` | Wortlaut, Gewaltformel, Wegstoßen, BGH Schubsen, (+) | fluent:`warning`, `leftwards-pushing-hand` (abstrakte Hand) | `… › 3. Nötigungsmittel` → `… › 3. Gewalt gegen eine Person` → `… (+)` | ≈ 9 | – |
| **G 4. subjektiv** `subj`→`bea5` | Vorsatz, Besitzerhaltungsabsicht, zwei Karten (nicht einziges Motiv / bloße Flucht), Subsumtion (+) | tabler:`brain`, `arrow-right`; fluent:`headphone` | `… › 4. subjektiv › Vorsatz` → `… › Besitzerhaltungsabsicht` → `… (+)` | ≈ 13 | – |
| **H Ergebnis** `rs`→`konk` | Ergebniskarte, Rechtsfolge, Qualifikationen, Konkurrenz | tabler:`gavel`; fluent:`balance-scale` | `A. § 252 StGB › II. Rechtswidrigkeit, III. Schuld` → `Ergebnis · Gottfried: § 252 StGB` → `Rechtsfolge › gleich einem Räuber` → `Konkurrenzen › § 242 tritt zurück` | ≈ 9 | – |
| **I Gegenvariante** `gv`→`gv3` | blaue Tafel; Kopfhörer am Boden, nur Flucht, (−), Diebstahl | fluent:`headphone`; tabler:`arrow-right` | `Gegenvariante › Beute weggeworfen` → `… › Besitzerhaltungsabsicht (−)` → `… › Diebstahl, § 242 StGB` | ≈ 8 | – |
| **J Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Besitzerhaltungsabsicht` → `… · Anhaltspunkte im Sachverhalt` | ≈ 8 | – |
| **K Klausurschema** `sch`→`s_iv` | breite Karte, progressiv | – | `Klausurschema › …` | ≈ 13 | – |
| **L Merksatz** `merke`→`m_2` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops. Die Schiebeblende A1 → A2 ist der Ortswechsel nach draußen (beim Wort „Direkt“).
**Geräusche:** ein Handlungsgeräusch (Laufschritte, als Gottfried sichtbar davonrennt; Freesound CC0), Herkunft in `geraeusche_herkunft.json`. Kein Stoß- oder Aufprallgeräusch, keine Geräusche bei Tafeln.
**Gewalt zurückhaltend:** Der Stoß wird gesprochen und nur als größerer Abstand, Eddas Schreck und Warnsymbol gezeigt; keine Berührung, kein Sturz, keine Verletzung. In der Gewaltdefinition nur eine abstrakte Emoji-Hand.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 252 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagvormittag im Elektromarkt: Gottfried nimmt Kopfhörer für 129 € aus dem Regal und steckt sie in die Innentasche seiner Jacke. Mitarbeiterin Edda hat das gesehen. Gottfried geht an der Kasse vorbei, ohne zu bezahlen, und verlässt den Markt. Direkt vor dem Eingang holt Edda ihn ein und greift nach seiner Jacke. Gottfried stößt sie weg, damit sie ihm die Kopfhörer nicht abnimmt, ruft „Die Kopfhörer behalte ich!“ und rennt mit ihnen davon. Edda taumelt zurück, verletzt ist sie nicht.
>
> Gegenvariante: Gottfried wirft die Kopfhörer weg und stößt Edda nur, um zu entkommen.
>
> **Hat sich Gottfried nach § 252 StGB strafbar gemacht?**
