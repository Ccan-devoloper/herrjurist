# Folge 153 · Vollstreckungserinnerung § 766 ZPO: Das Prüfschema – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_153.py`](src/skript_153.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZV, Themenplan-Format „Schema“; Voraussetzungen Folge 024 (Titel, Klausel, Zustellung) und 054 (Überblick der Rechtsbehelfe, nicht wiederholt). Übungsfall nach dem Plan-Hook: Die Konditorin Frau Bergmann hat gegen Herrn Mühlbauer ein vorläufig vollstreckbares Urteil des Amtsgerichts über 900 € (Hochzeitstorte) und eine Ausfertigung mit Klausel; der Gerichtsvollzieher pfändet in Herrn Mühlbauers Wohnung dessen Fernseher (Siegelmarke), ohne dass das Urteil vorher oder gleichzeitig zugestellt wurde. Aufbau: A. Zulässigkeit – 1. Statthaftigkeit (**Wortlautkarte § 766 I 1**; Vollstreckungsvoraussetzungen) mit Abgrenzung zu § 793 (**Wortlautkarte § 793**, Faustformel, Anhörung, § 834, **Wortlautkarte § 11 I RPflG**), 2. Zuständigkeit (§ 764, § 802, **Wortlautkarte § 20 I Nr. 17 RPflG**), 3. Erinnerungsbefugnis, 4. keine Frist/Rechtsschutzbedürfnis → B. Begründetheit (**Wortlautkarte § 750 I 1 Nr. 2 a**; Zweck, Verstoß, nur anfechtbar; Zeitpunkt und Heilung) → Entscheidung (Beschluss, üblicher Tenor, Aufhebung) → Eilschutz (**Wortlautkarte § 732 II**) → Merktabelle § 766/767/771 → Klausurtipp → Prüfschema → Merksatz. Hauptfilm ≈ 6:31 (5.635 vertonte Zeichen; Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Mühlbauer (MB), um 30 | Schuldner, Erinnerungsführer | Pose `standing/easing-1` (offenes lila Hemd `#B8A9F5` über weißem Shirt, schwarze Hose), Kopf `Short 5`, Haut `#D9A07A`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile`, `Concerned|Serious`, `Fear` (Schreck bei der Pfändung) | `niklas` (Mann, jung) |
| Der Gerichtsvollzieher (GV), um 60, ohne Namen | Vollstreckungsorgan, sachlich | Pose `standing/resting-2` (schwarzes Oberteil, graue Hose `#6B6B78`), Kopf `Gray Short` (helles Haar, Originalfarbe), Brille `Glasses 2`, Haut `#E8B98F`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Solemn`; keine Uniform, keine Abzeichen | `helmut` (Mann, älter) |
| Frau Bergmann (BE), um 45 | Konditorin, Gläubigerin (spricht nicht) | Pose `standing/resting-1` (grünes Oberteil `#8FD694`, schwarze Hose), Kopf `Bun`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Concerned|Serious`, `Suspicious` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel bzw. zum Gegenüber), `_r` blickt nach rechts (Frau Bergmann hinter der Theke, Herr Mühlbauer in seiner Wohnung). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MB_redet`, `GV_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Muster. **Verworfen:** `robot_dance-2` für Herrn Mühlbauer (gleiche Haltung wie Lexi, Kontaktbild). Stimmen ausschließlich aus dem Pool (niklas, helmut; ela_froh und julia nicht verwendet). Da der Pool nur zwei Männerstimmen hat, sind dieselben Stimmen wie in Folge 150 nicht vermeidbar (dort Torben/Herr Haupt); hier andere Rollen und Figuren. **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Folgenordner (`grep -rlw` ohne Treffer): Bergmann, Mühlbauer. Figuren-PNGs: `../peeps/op_153/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 147–150: Posen `pointing_finger-2`, `easing-2`, `robot_dance-3`, `walking-3`, `blazer-4`, `crossed_arms-2`, `shirt-3`, `blazer-3`; hier `easing-1`, `resting-2`, `resting-1` mit `Short 5`, `Gray Short`, `Bun`; keine Polka Dots.
- 054 (Fernseher, Siegel, Autowerkstatt, GV `shirt-4`) und 096 (Gemälde, Studentenwohnung, GV `blazer-4`, Vollmer `easing-1` grün): neuer Gläubigerort (Konditorei mit Theke), Wohnzimmer mit Sofa, Pflanze und Fernsehschrank, neutrale rote Siegelmarke mit Schriftzug statt Icon; GV älter, ohne Sakko; `easing-1` mit anderer Farbe, anderem Kopf und Hautton.
- Rückkehr in die Wohnung (H2), weil die Geschichte dorthin zurückkehrt (Aufhebung der Pfändung).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Konditorei** `fall`→`auftrag` | Bodenlinie; Frau Bergmann hinter der Theke (blickt nach rechts), Herr Mühlbauer rechts, Requisiten in der Mitte | Theke (`theke()`, Holz/Weiß), tabler:`cookie` (Gelb), `cake` (Weiß/Pink), `heart` (Rot), `cash-off` (Rot), `building-bank`, `file-certificate` | `Fall · Die Hochzeitstorte` (ab 0,0 s) → `· Die offene Rechnung` → `· Das Urteil` → `· Klausel und Vollstreckungsauftrag` | Theke · Mühlbauer + Hochzeit · Torte · 900 € · nicht bezahlt · Urteil · vorläufig vollstreckbar · Klausel · Auftrag | – |
| **A2 Wohnung** `g1`→`frage2` | Sofa links, Herr Mühlbauer (blickt nach rechts), Fernsehschrank mit Fernseher, Gerichtsvollzieher rechts, Pflanze | tabler:`sofa` (Hellblau), `plant-2` (Grün), `device-tv` (Dunkel), Fernsehschrank (`lowboard()`), Siegelmarke (`siegelmarke()`), tabler:`file-x` | `Fall · Die Pfändung` → `· Ohne Zustellung` → `· Die Frage` | GV-Blase · Siegel · „gepfändet“ · Mühlbauer-Blase · GV-Blase · nicht zugestellt · zwei Frage-Pillen | Aufkleben (`szene_153siegel_1`) |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,8 s) | – | `Sachverhalt` | 1 | – |
| **C1 Statthaftigkeit** `zul`→`statt_ok` | Tafel mit **Wortlautkarte § 766 I 1** (Marker „Einwendungen“, „Art und Weise“, „Verfahren“, „Vollstreckungsgericht“); Mühlbauer und GV | tabler:`list-check`, `gavel`, `file-x`, `circle-check` | `A. Zulässigkeit` → `› 1. Statthaftigkeit` → `…, § 766 Abs. 1 Satz 1 ZPO` → `› Vollstreckungsvoraussetzungen` → `› statthaft (+)` | Titel · 1. · Karte · vier Marker · Voraussetzungen + BGH · Haken · Block | – |
| **C2 Abgrenzung § 793** `a793`→`formel` | Tafel mit **Wortlautkarte § 793** (Marker „Entscheidungen“, „ohne mündliche Verhandlung“, „sofortige“), zwei Kästen Maßnahme/Entscheidung | tabler:`file-text`, `scale` | `… › Abgrenzung, § 793 ZPO` → `› Faustformel` | Titel · Karte · drei Marker · Faustformel · Maßnahme · Entscheidung + BGH | – |
| **C3 Maßnahme oder Entscheidung?** `anh`→`hier793` | Tafel; **Wortlautkarte § 11 I RPflG**; GV | tabler:`ear`, `file-text`, `user`, `device-tv` | `… › vorherige Anhörung?` → `› Pfändungs- und Überweisungsbeschluss, § 834 ZPO` → `› Rechtspfleger, § 11 Abs. 1 RPflG` → `› hier: keine Entscheidung` | Anhörung + BGH · PfÜB + BGH · Karte · Marker · § 793 + BGH · Block | – |
| **D Zuständigkeit** `zust2`→`richter` | Tafel; **Wortlautkarte § 20 I Nr. 17 RPflG** (Auszug); Mühlbauer | tabler:`building-bank`, `lock`, `gavel` | `A. › 2. Zuständigkeit` → `› ausschließlich, § 802 ZPO` → `› Richter, § 20 Abs. 1 Nr. 17 RPflG` | Amtsgericht · Bezirk · § 802 · Karte · Marker · „nicht der Rechtspfleger“ | – |
| **E Befugnis** `bef`→`bef_ok` | Tafel; Mühlbauer, ab „Gläubiger“ Frau Bergmann | tabler:`users`, `device-tv` | `A. › 3. Erinnerungsbefugnis` → `› Schuldner, Gläubiger, Dritte` → `› Herr Mühlbauer befugt (+)` | Grundsatz + BGH · Schuldner · Gläubiger + § 766 II · Dritter + BGH · Haken | – |
| **F Frist, RSB** `frist`→`rsb_ok` | Tafel mit Zeitstrahl (Pfändung – jetzt – Versteigerung); Mühlbauer | tabler:`hourglass`, `calendar-event`, `circle-check` | `A. › 4. keine Frist` → `› bis zur Beendigung der Maßnahme` → `A. Zulässigkeit › Ergebnis: zulässig (+)` | Kreuz Frist · RSB + BGH · Zeitstrahl · Ende · jetzt · Haken · Block | – |
| **G1 Begründetheit** `begr`→`zweck` | Tafel mit **Wortlautkarte § 750 I 1 Nr. 2 a** (Marker „darf nur beginnen“, „das Urteil“, „zugestellt ist“, „gleichzeitig“); Mühlbauer und GV | tabler:`list-check`, `mail`, `ear` | `B. Begründetheit` → `› § 750 Abs. 1 ZPO: Zustellung` → `› Zweck: rechtliches Gehör` | Maßstab · Karte · vier Marker · Zweck + BGH | – |
| **G2 Verstoß** `verst`→`begr_ok` | Tafel; Mühlbauer und GV | tabler:`file-x`, `alert-triangle`, `circle-check` | `B. › Verstoß gegen § 750 Abs. 1 ZPO` → `› nicht unwirksam, nur anfechtbar` → `› Ergebnis: begründet (+)` | Kreuz · Verstoß · anfechtbar + BGH · Block | – |
| **G3 Zeitpunkt** `zeit`→`heil` | Tafel mit Zeitstrahl (Pfändung – Zustellung nachgeholt – Entscheidung); Mühlbauer und Frau Bergmann | tabler:`clock`, `mail` | `B. › Zeitpunkt der Entscheidung` → `› Heilung durch Nachholung der Zustellung` | maßgeblich + BGH · Zeitstrahl · Entscheidung · nachgeholt · Heilung + BGH, Mühlbauer besorgt | – |
| **H1 Entscheidung** `ent`→`tenor` | Tafel mit grünem Tenorblock („üblicher Tenor“); Mühlbauer und GV | tabler:`file-text`, `gavel` | `Entscheidung · Beschluss, § 764 Abs. 3 ZPO` → `· Tenor (üblich)` | Beschluss · Tenor-Pille · Block + BGH · Mühlbauer froh | – |
| **H2 Wohnung** `aufh` | wie A2; der Gerichtsvollzieher entfernt die Siegelmarke | wie A2 | `Entscheidung · Aufhebung der Pfändung` | Siegel · Siegel weg + „Pfändung aufgehoben“, Mühlbauer froh | Abziehen (`szene_153abziehen_1`) |
| **H3 Eilschutz** `eil` | Tafel mit **Wortlautkarte § 732 II** (Marker „vor der Entscheidung“, „einstweilige“, „einstweilen einzustellen“); Mühlbauer | tabler:`hand-stop` | `Eilschutz · § 766 Abs. 1 Satz 2, § 732 Abs. 2 ZPO` | Karte · drei Marker · § 766 I 2 | – |
| **I Merktabelle** `tab`→`verw` | breite Karte, drei Zeilen | – | `Abgrenzung · § 766, § 767, § 771 ZPO` | Titel · § 766 · § 767 · § 771 · Video-Pillen | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Wer hat gehandelt – und wie?` → `· Heilung prüfen` | Frage · Faustregel · Erinnerung · sofortige Beschwerde · Heilung | – |
| **K Prüfschema** `sch`→`sB` | breite Karte, baut sich auf | – | `Prüfschema` → `› A. Zulässigkeit` → `› B. Begründetheit` | Titel · A · 1 · 2 · 3 · 4 · B · Verstoß · Zeitpunkt | – |
| **L Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Merkzeilen mit Marker | – | `Merksatz` | Zustellung · Erinnerung · sofortige Beschwerde | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („900 €“, „§ 766 Abs. 1 Satz 1 ZPO“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_153siegel_1` beim Aufkleben, `szene_153abziehen_1` beim Entfernen der Siegelmarke), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Bergmann führt eine Konditorei. Für die Hochzeit von Herrn Mühlbauer backt sie eine Torte für 900 €; er zahlt nicht. Das Amtsgericht verurteilt ihn zur Zahlung, das Urteil ist vorläufig vollstreckbar. Frau Bergmann erhält eine Ausfertigung mit Vollstreckungsklausel und beauftragt den Gerichtsvollzieher.
>
> Der Gerichtsvollzieher pfändet in der Wohnung von Herrn Mühlbauer dessen Fernseher und klebt eine Siegelmarke auf. Das Urteil wurde Herrn Mühlbauer weder vorher noch bei der Pfändung zugestellt. Der Fernseher ist noch nicht versteigert.
>
> Annahme: Der Fernseher ist pfändbar; weitere Fehler gibt es nicht.
>
> **Wie wehrt sich Herr Mühlbauer – und wann wäre die sofortige Beschwerde richtig?**
