# Folge 152 · Kündigungsschutzgesetz: Wann gilt das KSchG – und die 3-Wochen-Frist – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_152.py`](src/skript_152.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Arbeitsrecht, Format Schema. Beispielfall nach dem Plan-Hook („Nach acht Jahren im Betrieb bekommst du ohne jede Begründung die Kündigung“): Gärtnerin Kornelia erhält von Inhaber Herrn Steinmetz eine schriftliche, ordentliche Kündigung ohne Grund und will es sich „in Ruhe überlegen“. Ablauf: Fall → Sachverhalt → Aufbau (Schriftform/Zugang nur als Verweis auf Folge 050) → Anwendbarkeit persönlich (Wortlaut § 1 Abs. 1, Wartezeit) → betrieblich (Wortlaut § 23 Abs. 1 S. 3, „in der Regel“, Teilzeit S. 4, §§ 4–7 auch im Kleinbetrieb) → Sozialwidrigkeit (Wortlaut § 1 Abs. 2 S. 1, drei Gründe mit Icon, Abmahnung) → Begründung und Beweislast (§ 623 BGB nur Schriftform, Wortlaut § 1 Abs. 2 S. 4, Betriebsgröße, Verweis Folge 141) → die Falle (Wortlaut § 4 S. 1) → § 7 (Wortlaut) und § 5 → Fristberechnung im Kalender (§§ 187 Abs. 1, 188 Abs. 2 BGB) → Lösung → Klausurtipp (Reihenfolge, § 102 BetrVG) → Prüfschema I.–V. → Merksatz.
**Länge:** Hauptfilm 6:24,9 bei 5.624 Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Kornelia (KO), um 40 | Gärtnerin seit 2018, Arbeitnehmerin | `standing/walking-1` (T-Shirt Grün `#8FD694`, schwarze Hose, weiße Schuhe), Kopf `Medium Bangs` (schwarzes Haar), Haut `#E8B48F`; Mimiken `Smile` (froh), `Calm`, `Fear` (Schreck), `Concerned\|Serious` (Sorge; redet), `Serious`, `Suspicious`, `Tired`, `Solemn` | `laura_ruhig` (Frau, mittel) |
| Herr Steinmetz (ST), um 60 | Inhaber der Gärtnerei, Arbeitgeber | `standing/shirt-4` (schwarzes Hemd – Pose ohne Oberteilfläche –, Hose Dunkelblau `#2E3550`), Kopf `Gray Short`, Brille `Glasses 2`, kein Bart, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet, ernst), `Suspicious`, `Solemn`, `Smile` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner bisherigen Folge (Volltextsuche 04.10.2026): Kornelia, Steinmetz. Keine Genitivformen.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Fallszene: Kornelia (`_r`) blickt zu Herrn Steinmetz, er blickt nach links zu ihr. Tafelfolien: beide bzw. Kornelia allein blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KO_redet`, `ST_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** (william, sabrina, marc, laura_ruhig); gebraucht: laura_ruhig, william – nicht die Stimmen der Vorfolge 149 (sabrina, marc).
- Figuren-PNGs: `../peeps/op_152/` (50 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_152.png`.
- Keine Prothesen-Posen, keine Bärte, keine Polka Dots, keine Karikatur, keine realen Personen oder Unternehmen.

**Abweichung von den letzten Folgen:** 148 (Unfallflucht, Nachtstraße; `robot_dance-3`, `walking-3`), 149 (Supermarktparkplatz; `blazer-4`, `crossed_arms-2`), 150 (Elfes, Behörde; `shirt-3`, `blazer-3`). 152: Gewächshaus einer Gärtnerei (neu), Kalender als Fristbild (neu), Posen `walking-1` und `shirt-4` in keiner der drei Vorfolgen. Arbeitsrechtliche Vorgänger 050 (Fahrradwerkstatt) und 037 (Landstraße/Büro) nur über Verweise, kein Schauplatz übernommen.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Gewächshaus** `fall`→`frage2` | Glashaus (Grundform) mit Pflanztisch; Kornelia ab 0,0 s; Herr Steinmetz kommt von rechts; Brief wandert zu Kornelia, sie öffnet ihn | tabler:`plant`, `plant-2`, `flower`, `seedling` (Grün/Rot), `users`, `mail`, `mail-opened`, `file-text`, `writing-sign`, `hourglass` | `Fall · In der Gärtnerei` (ab 0,0 s) → `· Der Brief` → `· Die Kündigung` → `· Ohne jeden Grund?` → `· Die Frage` | Kornelia + Pille · 25 Beschäftigte · seit 8 Jahren · Steinmetz kommt · Inhaber · Brief unterwegs · geöffnet · Kündigung · fristgerecht · unterschrieben · kein Grund · drei Blasen · zwei Fragen | Schritte (`szene_152schritte_1`), Umschlag (`szene_152umschlag_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C Aufbau** `aufbau`→`a4` | Tafel, beide Figuren | tabler:`file-text`, `book`, `scale`, `hourglass` | `Aufbau · …` → `Aufbau › 1. Anwendbarkeit des KSchG` → `› 2. Sozialwidrigkeit` → `› 3. Die Falle: Klagefrist` | ✓ erklärt/zugegangen · Verweis 050 · drei Blöcke nacheinander | – |
| **D § 1 Abs. 1** `p1`→`p1fall` | Wortlautkarte (vorgelesen), Kornelia allein | tabler:`book`, `hourglass`, `calendar` | `Anwendbarkeit › persönlich, § 1 Abs. 1 KSchG` → `› Wartezeit` → `› Wartezeit erfüllt (+)` | Karte · 5 Marker · Wartezeit · ✓ Fall · ✓ erfüllt | – |
| **E § 23 Abs. 1 S. 3** `p23`→`klein` | Wortlautkarte mit Auslassung, beide Figuren | tabler:`users`, `calendar`, `clock`, `plant`, `hourglass` | `Anwendbarkeit › betrieblich, § 23 Abs. 1 S. 3 KSchG` → `› „in der Regel“` → `› Teilzeit, § 23 Abs. 1 S. 4` → `› mehr als 10 Arbeitnehmer (+)` → `› Klagefrist auch im Kleinbetrieb` | Karte · Marker 2003/Regel/zehn/Berufsbildung · BAG Rn. 11 · Teilzeit · ✓ 25 · §§ 4–7 | – |
| **F § 1 Abs. 2 S. 1** `p12`→`betr` | Wortlautkarte und drei Grundkarten | tabler:`user-exclamation`, `alert-triangle`, `briefcase-off`, `scale` | `Sozialwidrigkeit, § 1 Abs. 2 S. 1 KSchG` → `› personenbedingt` → `› verhaltensbedingt: Abmahnung` → `› betriebsbedingt` | Karte · Marker Person/Verhalten/dringende/bedingt · Karte 1 · Karte 2 + Abmahnung + BAG · Karte 3 | – |
| **G Begründung, Beweislast** `begr`→`v141` | Tafel, Wortlautkarte § 1 Abs. 2 S. 4 (vorgelesen) | tabler:`file-text`, `search`, `scale`, `users` | `Sozialwidrigkeit › Begründung im Schreiben?` → `› Grund muss vorliegen` → `› Beweislast, § 1 Abs. 2 S. 4 KSchG` → `Beweislast › Betriebsgröße: Arbeitnehmerin` | ✗ Grund im Schreiben · § 623 · ✓ Grund muss vorliegen · Karte + Marker · Betriebsgröße + BAG Rn. 27 · Verweis 141 | – |
| **H1 Die Falle** `falle`→`p4` | hellgelbe Tafel, Wortlautkarte § 4 S. 1 (vorgelesen), Kornelia allein | tabler:`alert-triangle`, `hourglass`, `building-bank` | `Klagefrist · die Falle` → `Klagefrist › § 4 S. 1 KSchG: drei Wochen` | Karte · Marker anderen Gründen/drei Wochen/Zugang/Klage · Block 3 Wochen | – |
| **H2 § 7, § 5** `p7`→`p5` | Wortlautkarte § 7 | tabler:`file-certificate`, `question-mark`, `first-aid-kit` | `Klagefrist › § 7 KSchG: gilt als wirksam` → `› Grund dann egal` → `› § 5 KSchG: nachträgliche Zulassung` | Karte · Marker rechtzeitig/von Anfang an · Block egal · § 5 · Sorgfalt | – |
| **I Fristberechnung** `frist`→`ende` | Kalender Oktober 2026 (Grundform), Kornelia allein | tabler:`calendar-event`, `mail-opened`, `calendar-week`, `alarm` | `Klagefrist › Fristberechnung` → `› Zugang: Mo, 5.10.2026` → `› § 187 Abs. 1 BGB …` → `› § 188 Abs. 2 BGB …` → `› Ende: Mo, 26.10.2026, 24 Uhr` | Kalender · 5 gelb „Zugang“ · 5 grau durchgestrichen · § 187 · § 188 · 12/19/26 markiert · Block Fristende | – |
| **J Lösung** `loes`→`l5` | Tafel, beide Figuren | tabler:`gavel`, `building-bank`, `hourglass`, `file-certificate` | `Lösung` → `› KSchG anwendbar (+)` → `› Arbeitsgericht entscheidet` → `› Klage bis 26.10.2026` → `› sonst § 7: wirksam` | ✓ · Arbeitsgericht · Beweis · Block Frist · Block § 7 | – |
| **K Klausurtipp** `tipp`→`t6` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Prüfungsreihenfolge` → `· sonstige Gründe, § 102 BetrVG` → `· die Frist gehört an den Anfang` | 1.–5. nacheinander · § 102 · Frist an den Anfang · versäumt · übrige Gründe | – |
| **L Prüfschema** `sch`→`s5` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfschema › I. …` bis `› V. Sonstige Unwirksamkeitsgründe` | Titel · I. · II. · III. · persönlich · betrieblich · IV. · Gründe · V. | – |
| **M Merksatz** `merke`/`m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | Satz 1 + Marker · Satz 2 + Marker | – |

**Prüfpfad und Reihenfolge:** Das Video prüft in der Erklärreihenfolge des Auftrags (Anwendbarkeit → Sozialwidrigkeit → Klagefrist als „Falle“) und benennt die Abschnitte im Prüfpfad ohne römische Ziffern. Die Klausurreihenfolge (Erklärung – Klagefrist – Anwendbarkeit – Sozialwidrigkeit – sonstige Gründe) stellt Lexi im Klausurtipp ausdrücklich vor; das Schema verwendet sie mit I.–V. und denselben Bezeichnungen.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Herr Steinmetz kommt 200 px von rechts, der Brief wandert von ihm zu Kornelia.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen, Zahlen als Ziffern („Nach 8 Jahren?“). Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Auslassungen mit „…“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Kornelia arbeitet seit 2018, also seit acht Jahren, als Gärtnerin in der Gärtnerei von Herrn Steinmetz am Stadtrand. Dort sind in der Regel 25 Arbeitnehmer beschäftigt; einen Betriebsrat gibt es nicht.
>
> Am Montag, 5. Oktober 2026, übergibt Herr Steinmetz ihr im Gewächshaus persönlich ein eigenhändig unterschriebenes Schreiben: die ordentliche Kündigung, fristgerecht zum 31. Januar 2027. Einen Grund nennt das Schreiben nicht. Auf ihre Frage sagt er: „Einen Grund muss ich Ihnen nicht nennen.“
>
> Kornelia will sich erst einmal in Ruhe überlegen, was sie tut.
>
> **Ist die Kündigung wirksam, und bis wann muss Kornelia handeln?**
