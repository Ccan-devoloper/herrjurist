# Folge 200 · Baugebiete BauNVO: Was darf ins Wohngebiet? (§ 30 BauGB) – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_200.py`](src/skript_200.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Baurecht, Format **Schema** mit Beispielfall nach dem Plan-Hook („Im reinen Wohngebiet soll eine Kita öffnen, im allgemeinen Wohngebiet ein Tattoo-Studio.“): Ein Bebauungsplan von 2022 setzt für eine neue Siedlung im Norden ein reines, im Süden ein allgemeines Wohngebiet fest. Frau Möhring will im Norden eine Kita (2 Gruppen, 30 Plätze, Kinder aus der Siedlung) eröffnen, Herr Tiemann im Süden ein kleines Tattoo-Studio (nur nach Termin, kein Lärm, Kundschaft aus der ganzen Stadt).
Ablauf: Fall (Siedlung Nord → Ladenlokal Süd) → Sachverhalt → § 30 Abs. 1 BauGB (Wortlautkarte) → Baugebiete § 1 Abs. 2 BauNVO (Tabelle), § 1 Abs. 3 S. 2 → Aufbau §§ 2–9 (Abs. 1–3), § 31 Abs. 1 BauGB (Wortlautkarte), Gebietsverträglichkeit → Kita im WR (§ 3 BauNVO, Wortlautkarte; Gegenfall große Kita) → Kinderlärm (§ 22 Abs. 1a BImSchG, Wortlautkarte) → Studio im WA (§ 4 Abs. 1, 2 Nr. 2, Wortlautkarte; Gebietsversorgung) → Ausnahme (§ 4 Abs. 3 Nr. 2, Wortlautkarte; § 31 Abs. 1; § 246e BauGB) → § 15 Abs. 1 BauNVO (Wortlautkarte; Verweis 113) → Ergebnis (zurück am Plan, Blase Tiemann) → Prüfschema → Klausurtipp (Lexi) → Merksatz (Lexi). Folge 188 (Prüfschema Baugenehmigung, § 29, Weiche §§ 30, 34, 35) nur als Verweis, Folge 113 (Gebietserhaltungsanspruch) nur als Verweis, Folge 085 (§ 35) nicht berührt.
**Länge:** Hauptfilm 6:23,8 bei 5.489 gesprochenen Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Möhring (MO), um 35 | gründet die Kita | `standing/shirt-3` (Hemdbluse Rosé `#F2A7C3`, schwarze Hose), Kopf `Long Curly`, Haut `#E8B48F`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile`, `Solemn`, `Concerned\|Serious`; redet: `Smile Big\|Smile` | `lucy` (Frau, jung) |
| Herr Tiemann (TI), um 30 | Tätowierer, mietet ein Ladenlokal | `standing/resting-2` (schwarzer Pullover, Hose Blau `#8DB3F2`), Kopf `Short 1`, Haut `#D9A47E`, kein Bart, keine Tätowierungen; `Calm`, `Smile`, `Suspicious`, `Concerned\|Serious`, `Serious`; redet: `Calm`, redet2: `Smile` | `stephan` (Mann, mittel) |
| zwei Kinder (KA, KB), um 5 | Kinder aus der Siedlung, sprechen nicht, ohne Namen (ohne Schild) | `standing/walking-1` (T-Shirt Rot `#F07A6A`), Kopf `Buns`, Haut `#F0C8A8`, `Cute`; `standing/walking-2` (Hose Grün `#8FD694`), Kopf `Short 2`, Haut `#C58E64`, `Smile`; Höhe 58 % der Erwachsenen | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 04.10.2026: Möhring 0, Tiemann 0). Nie im Genitiv („die Kundschaft von Herrn Tiemann“).
- **Stimmen nur aus dem Pool:** `lucy` und `stephan`; `hilde` und `christian` nicht verwendet. Vorfolgen: 197 `hilde`/`christian`, 198 `helmut`/`niklas`, 199 `marc`/`laura_ruhig` – keine Wiederholung zur Vorfolge.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Fallszenen: Frau Möhring und die Kinder blicken nach links zur Kita, Herr Tiemann nach links zu seinem Ladenlokal; Ergebnis: Frau Möhring (`_r`) blickt zu Herrn Tiemann; Tafelfolien: alle blicken nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MO_redet`, `TI_redet`, `TI_redet2` (je links/rechts) und Lexi.
- Figuren-PNGs: `../peeps/op_200/` (56 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_200.png`.
- **Darstellung:** Kita und Studio nur als Icons (Phosphor `house-line`, Tabler `building-store`), keine Marken; Tattoo-Studio neutral (kein Totenkopf, keine Tätowierungen an der Figur, ruhiger Betrieb); Kinder nur als Open-Peeps-Figuren.
- Verworfen: `robot_dance-3` für Herrn Tiemann (Armgeste wie Lexi).

**Abweichung von den letzten Folgen:** 197 (`easing-1`, `blazer-1`; Lila/Grün), 198 (`easing-1`, `resting-1`; Lila/Türkis), 199 (`easing-2`, `pointing_finger-1`; Orange), 196 (`robot_dance-2`, `blazer-4`, `crossed_arms-2`). 200: `shirt-3`, `resting-2`, `walking-1/-2` in keiner der vier Vorfolgen; Farben Rosé und Blau/Schwarz; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz neu: **Planblatt „Bebauungsplan 2022“** mit Nord-/Südzone (WR gelb, WA orange) neben der Straße, Kita-Haus mit Rutsche, Ladenlokal; Tabelle der Baugebiete. Gegenüber 188 (Feldflur, Behörde) und 113 (Grundstücksgrenze, Anbau) andere Orte und Requisiten. Das Planblatt kehrt im Ergebnis zurück, weil das Ergebnis je Zone gezeigt wird.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Siedlung Nord** `fall`→`mo1` | Planblatt (Nord/Süd grau ab 0,0 s), Häuser und Baum an der Straße; Zonen WR/WA erscheinen; Kita-Haus, Frau Möhring, Blase, Kinder | fluent-hc:`houses`, `deciduous-tree`, `teddy-bear`, `playground-slide`; ph:`house-line` | `Fall · Die neue Siedlung` → `· Norden: reines Wohngebiet` → `· Süden: allgemeines Wohngebiet` → `· Die Kita von Frau Möhring` → `· 2 Gruppen, Kinder aus der Siedlung` | Grundbild · Zone WR · Häuser WR · Zone WA · Häuser WA · Möhring · Kita-Haus · Schild/Teddy · Blase · Pille 2 Gruppen · Kinder · Pille Kinder | – |
| **A2 Süden** `studio`→`frage2` | Planblatt mit Ladenlokal-Icon, Ladenlokal „Tattoo-Studio“, Herr Tiemann, Blase, Termin/kein Lärm/Stadt, Fragen mit Ringen | tabler:`building-store`, `calendar`, `volume-off`, `map-2`; `ring()` | `Fall · Süden: das Ladenlokal von Herrn Tiemann` → `· Herr Tiemann erklärt sein Studio` → `· Kita ins reine Wohngebiet?` → `· Studio ins allgemeine Wohngebiet?` | 10 | Ladenglocke (`szene_200tuerglocke_1`) beim Auftritt von Herrn Tiemann |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,6 s) | – | `Sachverhalt` | 1 | – |
| **C § 30 Abs. 1 BauGB** `p30`→`v188` | Wortlautkarte, beide Figuren | tabler:`map`, `circle-check`, `building-community` | `§ 30 Abs. 1 BauGB · der Ausgangspunkt` → … → `› Genehmigungspflicht: eigenes Video` | Karte · 5 Marker · ✓ · offen: Art · Verweis | – |
| **D Baugebiete** `bng`→`p13` | Tabelle WR, WA, MI, MU, GE, GI; Block § 1 Abs. 3 S. 2 | tabler:`book`, `table`, `map` | `Baugebiete · die Baunutzungsverordnung` → `› § 1 Abs. 2 BauNVO: 12 Baugebiete` → je Zeile → `› § 1 Abs. 3 S. 2 BauNVO: Teil des Plans` | 9 | – |
| **E Aufbau** `aufbau`→`gv` | Blöcke Abs. 1/2/3, Wortlautkarte § 31 Abs. 1, Ermessen, Gebietsverträglichkeit | tabler:`list-numbers`, `file-certificate`, `scale`, `home-check` | `Aufbau §§ 2–9 BauNVO · …` → `› ungeschrieben: Gebietsverträglichkeit` | 8 | – |
| **F Kita** `kita1`→`gross` | Wortlautkarte § 3 Abs. 1, 2; ✓ Bewohner, ✓ gebietsverträglich; Gegenfall | ph:`house-line`; fluent-hc:`teddy-bear`; tabler:`building-community`; Kinder | `Kita im reinen Wohngebiet · § 3 BauNVO` → … → `› Gegenfall: große Kita, Abs. 3 Nr. 2` | 9 | – |
| **G Kinderlärm** `laerm`→`kerg` | Wortlautkarte § 22 Abs. 1a, Ergebnis Kita | tabler:`volume`, `circle-check`; Kinder | `Kinderlärm · ein Problem?` → `› § 22 Abs. 1a BImSchG …` → `Kita › allgemein zulässig (+)` | 6 | – |
| **H Studio** `stu1`→`nein2` | Wortlautkarte § 4 Abs. 1, 2 Nr. 2; Handwerk offen; Gebietsversorgung; ✗ ganze Stadt | tabler:`building-store`, `tools`, `map-2` | `Studio im allgemeinen Wohngebiet · § 4 BauNVO` → … → `› Abs. 2 Nr. 2 (−)` | 10 | – |
| **I Ausnahme** `p4c`→`turbo` | Wortlautkarte § 4 Abs. 3 Nr. 2; ✓ nicht störend; Ausnahme § 31; Ermessen; ✗ § 246e | tabler:`building-store`, `calendar`, `file-certificate`, `home` | `Studio › Ausnahme: § 4 Abs. 3 Nr. 2 BauNVO` → … → `› § 246e BauGB hilft nicht` | 8 | – |
| **J § 15** `p15`→`v113` | Wortlautkarte § 15 Abs. 1, ✓ nichts ersichtlich, Verweis 113 | tabler:`zoom-check`, `users` | `§ 15 Abs. 1 BauNVO · der Einzelfall` → … → `› Nachbarn: Video „Nachbarklage“` | 7 | – |
| **K Ergebnis** `erg`→`ti2` | Planblatt mit ✓ WR und Studio-Icon, Pillen, beide Figuren, Blase Tiemann | wie A1/A2 | `Ergebnis › Kita: allgemein zulässig` → `› Studio: nur als Ausnahme` → `› Herr Tiemann beantragt die Ausnahme` | 5 | – |
| **L Prüfschema** `sch`→`s4` | breite Karte, Punkt für Punkt | – | `Prüfschema › …` | 10 Stufen | – |
| **M Klausurtipp** `tipp`→`k5` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol | `Klausurtipp · immer dieselbe Reihenfolge` → … | 6 | – |
| **N Merksatz** `merke`→`m4` | Lexi erklärt (redet), 4 Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusch:** ein Handlungsgeräusch (Ladenglocke, als Herr Tiemann an sein Ladenlokal tritt), Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json). Kinderlachen o. Ä. bewusst nicht (wäre Atmo, keine Handlung).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen (Zahlen als Ziffern). Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Auslassungen mit „…“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ein qualifizierter Bebauungsplan der Gemeinde aus dem Jahr 2022 setzt für eine neue Siedlung im Norden ein reines Wohngebiet und im Süden ein allgemeines Wohngebiet fest. Die Erschließung ist gesichert; die übrigen Festsetzungen halten beide Vorhaben ein.
> Frau Möhring will im Norden in einem Einfamilienhaus eine Kita mit 2 Gruppen und 30 Plätzen eröffnen. Alle Kinder kommen aus der Siedlung.
> Herr Tiemann mietet im Süden ein kleines Ladenlokal für sein Tattoo-Studio. Er arbeitet nur nach Termin, nach draußen dringt kein Lärm. Seine Kundschaft kommt aus der ganzen Stadt.
> **Frage:** Sind die Kita und das Studio nach der Art der baulichen Nutzung zulässig? (kein Fiktiv-Hinweis)
