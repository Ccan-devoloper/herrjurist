# Folge 038 · Körperverletzung § 223 StGB: Misshandlung & Gesundheitsschädigung – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_038.py`](src/skript_038.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Ein Wohngemeinschaftsfall trägt den Film (Hook des Themenplans): Sigrid schneidet ihrer auf dem Sofa eingeschlafenen Mitbewohnerin Katrin heimlich die langen Haare ab. Frage → Sachverhalt (Grundfall und fünf Varianten) → Wortlautkarte § 223 I, II → 1. körperliche Misshandlung (Grundfall) → Bagatellgrenze (Ohrfeige/Stups) → 2. Gesundheitsschädigung (Abführmittel) → psychische Folgen → ärztlicher Heileingriff (Rspr./Lehre) → Versuch → Grundfall: Ergebnis und Strafantrag (§§ 230, 77b) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Verhältnis zu Folge 035:** Dort steht § 223 nur als Feld der Landkarte (Definitionen in zwei Sätzen, Prellungen). Hier wird vertieft: beide Varianten mit Grenzfällen, Haare ohne Schmerz, Bagatellgrenze, psychische Folgen, Heileingriff, Versuch, Strafantragsfrist. Keine Wiederholung des Überblicks.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Katrin (KA/KAL), Ende 20 | Mitbewohnerin, Opfer im Grundfall; Ohrfeige in Variante 1; Patientin in Variante 4 | `sitting/closed_legs-1` (sitzt mit angezogenen Knien auf dem Sofa bzw. auf der Behandlungsliege), Kopf `Long` (vor dem Schnitt, KAL_) bzw. `Medium 1` (danach, KA_), Jacke Blau `#8DB3F2`, gestreiftes Oberteil der Pose, Haut `#F0C8A8`. Mimiken `Eyes Closed` (schläft), `Fear`, `Concerned|Serious` (redet; krank), `Very Angry` (Ohrfeige), `Calm`, `Serious`, `Tired`, `Suspicious`, `Smile` (redet einverstanden) | `lucy` (Frau, jung) |
| Sigrid (SI), Mitte 50 | Mitbewohnerin, schneidet die Haare ab | `standing/walking-1` (schleicht), Kopf `Gray Medium` (Haar grau `#BDBDC6`), Oberteil Lila `#B8A9F5`, Haut `#E0B48E`. Mimiken `Calm`, `Suspicious` (schleicht), `Driven` (schneidet), `Contempt` (redet abwinkend), `Fear` (ertappt), `Concerned|Serious` (Ohrfeige), `Serious` | `hilde` (Frau, älter) |
| Doktor Lindner (LI), um 60 | Hautarzt in Variante 4 | `standing/doctor-nurse-02` (Arztkittel), Kopf `Gray Short` (Haar `#D9D9DE`), Brille `Glasses 3`, Haut `#D9A27A`. Mimiken `Calm`, `Smile` (redet; froh), `Serious` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Sigrid zu Katrin, alle Figuren rechts zur Tafel), `_r` blickt nach rechts (Katrin im Wohnzimmer zu Sigrid, in der Praxis zu Doktor Lindner, bei der Ohrfeige zu Sigrid).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`. Mundzustände a/o/e bei `KA_redet`, `KA_einv`, `SI_redet`, `LI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen. 82 Figuren-PNGs in `../peeps/op_038/` (Drive-Master).
- **Frisurwechsel Katrin** (lang → kurz) ist der Sachverhalt selbst und deshalb die einzige gewollte Abweichung von „Frisur konstant“. Varianten, in denen die Haare nicht abgeschnitten sind (2 Abführmittel, 5 Versuch), zeigen sie mit langen Haaren.
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen alle Skripte 001–036 geprüft): Katrin, Sigrid, Lindner. („Brandt“ verworfen, in 004 vergeben.)
- **Stimmen** nur aus dem zugeteilten Pool (lucy, hilde, william; `timo` nicht gebraucht). Vorfolge 035 (julia, marc), 036 (sabrina, niklas, laura_ruhig, helmut): keine Überschneidung. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 036 (BVerfG-Verfahrensarten), 035 (Unibibliothek mit Whiteboard), 034 (Baustelle), 033 (Stadtbibliothek). Hier neu: Wohnzimmer einer Wohngemeinschaft am Abend (Sofa, Fenster mit Mond, Stehlampe), in den Tafelszenen ein kleines WG-Sofa rechts; für Variante 4 eine Hautarztpraxis mit Behandlungsliege. Neue Posen (`closed_legs-1`, `walking-1`, `doctor-nurse-02`), erstmals eine sitzende Fallfigur.
**Tageslicht/Abend:** durchgehend Cremegrund; der Abend nur über Fenster mit Mond und Lampe (kein Nachtverlauf nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Wohngemeinschaft** `fall`→`frage2` | Wohnzimmer: Lampe, Sofa mit Katrin (schläft), Fenster mit Mond; Sigrid am Fenster denkt „Haare im Abfluss!“ (Denkblase, Badewanne), holt die Schere, schneidet (Pillen „heimlich“, „Haare ab“; Katrins Kopf lang → kurz), Katrin wacht auf; Blasen Katrin/Sigrid; Frage-Pillen | ph:`couch-thin`; tabler:`lamp`, `moon`, `zzz`, `bath`, `scissors` | `Fall · Die Haare` (ab 0,0 s) → `Fall · Die Frage` | ≈ 16 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10,5 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p223`→`eine` | Wortlautkarte § 223 I, II mit Markern; zwei Variantenblöcke | Sofa | `§ 223 StGB › Wortlaut und Varianten` | ≈ 11 | – |
| **D Misshandlung** `mh`→`mh_ok` | Definition (BGH-Formel), „Schmerz ist nicht nötig“, Subsumtion Haare, Dreadlockfall, Block mit Haken; rechts Schere/„Haare ab“, dann „nichts gespürt“ | tabler:`scissors`, `zzz` | `I. Tatbestand › 1. körperliche Misshandlung › Grundfall: Haare ab` | ≈ 13 | – |
| **E Bagatellgrenze** `bag`→`stups_no` | „Nicht jeder Schlag oder Stoß“; Ohrfeige (Hand an Sigrids Wange, Haken), Stups (Kreuz) | tabler:`hand-stop`, `hand-finger` | `I. Tatbestand › 1. körperliche Misshandlung › Bagatellgrenze, Variante 1` | ≈ 9 | – |
| **F Gesundheitsschädigung** `gs`→`beide` | Definition, Abführmittel im Tee, zwei Haken; Katrin (lange Haare) krank | tabler:`mug`, `pill` | `I. Tatbestand › 2. Gesundheitsschädigung › Variante 2: Abführmittel` | ≈ 10 | – |
| **G Psychische Folgen** `psy`→`v3_no` | zwei Kreuze, gelber Block „pathologischer, körperlich objektivierbarer Zustand“, Kreuz „reicht nicht“ | tabler:`moon`, `brain` | `I. Tatbestand › 2. Gesundheitsschädigung › psychische Folgen, Variante 3` | ≈ 10 | – |
| **H Heileingriff** `arzt`→`v4_erg` | Hautarztpraxis: Katrin auf der Liege, Doktor Lindner; Blasen; Rechtsprechung/Lehre nebeneinander; Ergebnisblock | tabler:`bed-flat`, `stethoscope` | `Variante 4 · Ärztlicher Heileingriff` → `Variante 4 · Heileingriff: Rechtsprechung und Lehre` | ≈ 17 | – |
| **I Versuch** `vers`→`vers_ok` | Katrin (lang) schläft → wacht auf, hält die Haare fest; Sigrid mit Schere ertappt; zwei Haken, Block | tabler:`scissors`, `hand-grab` | `Variante 5 · Versuch, §§ 223 Abs. 2, 22 StGB` | ≈ 8 | – |
| **J Ergebnis, Strafantrag** `erg`→`kennt` | Ergebnisblock mit Haken, § 230, Frist § 77b | tabler:`signature`, `calendar-time` | `Grundfall › II. Rechtswidrigkeit, III. Schuld` → `› Ergebnis: § 223 Abs. 1 StGB` → `› Strafantrag, § 230 StGB` | ≈ 9 | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), tabler:`scissors` | `Klausurtipp · Varianten trennen, § 224 nicht vorschnell` | ≈ 7 | – |
| **L Klausurschema** `sch`→`k_v` | breite Karte, progressiv | – | `Klausurschema` | ≈ 11 | – |
| **M Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Sigrid am Fenster → neben dem Sofa; Katrin lange Haare → kurze Haare; schläft → wach).
**Geräusche:** keine. Die sichtbare Handlung wäre ein Scherenschnitt; Freesound ist über den Proxy gesperrt (HTTP 403, geprüft 02.10.2026), und `sfx3/` enthält kein Scheren- oder passendes Wohnungsgeräusch („lieber kein Geräusch als ein unpassendes“). Schritte passen nicht zum heimlichen Schleichen.
**Gewalt zurückhaltend:** kein Blut, keine Verletzung im Bild; Ohrfeige und Stups nur als Hand-Icons mit Pille; die Schere ist ein Alltagsgegenstand, nie gegen den Körper gerichtet.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 223 I, II vollständig, wörtlich nach gesetze-im-internet.de (amtliche Schreibung „mißhandelt“), Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Sonntagabend in einer Wohngemeinschaft: Katrin ist auf dem Sofa eingeschlafen. Ihre Mitbewohnerin Sigrid ärgert sich über Katrins lange Haare im Abfluss und schneidet sie ihr heimlich mit einer Schere ab. Katrin hat nichts gespürt.
>
> Variante 1: Katrin gibt Sigrid eine kräftige Ohrfeige; die Wange brennt und rötet sich. Gegenstück: Katrin stupst Sigrid nur leicht an die Schulter. Variante 2: Sigrid rührt heimlich ein Abführmittel in Katrins Tee; Katrin bekommt Durchfall und Bauchkrämpfe. Variante 3: Katrin schläft vor Aufregung zwei Nächte schlecht. Variante 4: Hautarzt Doktor Lindner klärt Katrin auf und entfernt mit ihrer Einwilligung fachgerecht ein verdächtiges Muttermal. Variante 5: Sigrid setzt die Schere an, doch Katrin wacht auf und hält ihre Haare fest.
>
> **Wer hat sich nach § 223 StGB strafbar gemacht?**
