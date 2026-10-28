# Folge 194 · Beihilfe § 27 StGB: Schema – wie viel Hilfe macht strafbar? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_194.py`](src/skript_194.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Format „Schema“. Aufbau nach Auftrag: Fall nach dem Plan-Hook (Autoleihe zum Einbruch) → Frage → Sachverhalt → Wortlautkarte § 27 Abs. 1 und Abs. 2 → Prüfschema I. 1. a) Haupttat (limitierte Akzessorietät, Wortlautkarte § 29) → b) Hilfeleisten (physisch/psychisch, Vorbereitung) → Meinungsstand Förderungsformel (BGH) gegen Kausalität (h. L.) → 2. doppelter Gehilfenvorsatz → Schema komplett mit II., III. und Strafe → Lösung (Haupttat §§ 242, 244 Abs. 1 Nr. 3, Abs. 4; Mittäterschaft ein Satz mit Verweis; Hilfeleisten; Vorsatz; Ergebnis und Strafrahmen) → Sonderfälle (sukzessive Beihilfe, neutrale Handlungen/Taxi, Unterlassen) → Klausurtipp (Lexi) → Merksatz (Lexi). Vorlagen: 104 (Mittäterschaft; nur ein Satz Verweis), 026 (Kausalität; nicht wiederholt), 192 (Hilfsfunktionen), 015 (Namens- und Sichtprüfung).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Falko (FA), um 35 | Haupttäter, bittet um das Auto | `standing/robot_dance-3` (Oberteil Grün `#8FD694`, Hose Dunkelblau `#3F5F8F`, weiße Schuhe; offene Hand), Kopf `Short 3`, Haut `#EBC0A0`. Mimiken `Calm`, `Serious` (redet), `Driven`, `Suspicious`, `Solemn` | `stephan` (Mann, mittel) |
| Hedda (HE), um 35 | Freundin, leiht das Auto | `standing/blazer-3` (Blazer Rot `#F07A6A`, schwarzes Shirt der Pose, Hose Grau `#5A5A5A`), Kopf `Long Bangs`, Haut `#E2B08C`. Mimiken `Calm`, `Suspicious`, `Concerned|Serious` (redet), `Solemn`, `Serious` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Haustür: Hedda (`_r`) blickt zu Falko, Falko zu ihr; Haus am Stadtrand: Falko blickt zum Haus; Frage: beide zueinander; Tafelfolien: beide zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `FA_redet`, `HE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Mütze, keine Maske, kein Werkzeug. 44 Figuren-PNGs in `../peeps/op_194/` (Drive-Master).
- **Klischeeprüfung:** Täterrolle gewöhnlich gekleidet (grünes Oberteil, Jeans), keine „fiese“ Mimik (nur `Serious`/`Driven`), keine Zuordnung von Herkunft oder Hautfarbe zur Täterrolle; Hedda respektvoll (besorgt, nicht komplizenhaft lächelnd).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen, Manifest oder Themenplan unter `youtube/` (04.10.2026): Falko, Hedda („Jannik“ wegen Folge 010, „Viktor“ wegen möglicher Herkunftsassoziation bei einer Täterfigur verworfen). Im Sprechtext nie im Genitiv („mit dem Auto von Hedda“).
- **Stimmen** nur aus dem zugeteilten Pool (stephan, lucy; hilde und christian nicht verwendet). Falko und Hedda sprechen je einmal. Vorfolgen: 191 (william, marc), 192 (hilde, lucy), 193 (helmut, niklas); lucy wiederholt sich aus 192, weil der zugeteilte Pool für eine junge Frau nur lucy bietet (hilde ist „Frau, älter“).

**Abweichung von den letzten Folgen (191 Erfolgsqualifikation, 192 Kleingarten/Abgrenzungstheorien, 193 Weiterfresserschaden; 104 Kiosk):** neue Schauplätze Hauswand mit Tür und Fenster am Freitagabend sowie Einfamilienhaus am Stadtrand mit Auto; Posen `robot_dance-3` und `blazer-3` in 189–193 nicht verwendet (dort `easing-2`, `walking-1`, `shirt-3`, `blazer-2`, `shirt-4`, `blazer-4`, `crossed_arms-2`, `resting-1/-2`, `walking-2`); kein Polka-Dots-Muster; Hedda trägt Rot (191: Lila-T-Shirt, 192: Orange-Hemd, 193: Blau).
**Tageslicht/Abend:** Cremegrund durchgehend; Abend und 22 Uhr nur über Mond-Icon, Uhr und Pille (kein Nachtgrund nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Haustür** `fall`→`nichts` | Hedda vor ihrer Tür, Falko ihr gegenüber, ihr Auto am Straßenrand ab 0,0 s; Pillen „Samstag: Einbruch in ein Einfamilienhaus“, „dort wohnt eine Familie – abends nicht zu Hause“, „Welches Haus? Sagt er nicht.“; Blase Falko „Leihst du mir dein Auto? …“; Blase Hedda „Ich finde das falsch. …“; Schlüssel wandert zu Falko; „von der Beute: nichts“ | fluent-hc:`crescent-moon`, `automobile`, `house`, `key`; Hauswand, Tür, Fenster als Bausteine | `Fall · Freitagabend bei Hedda` (ab 0,0 s) → … → `Fall · Hedda will nichts von der Beute` | Schlüssel (`szene_194schluessel_1`) |
| **A2 Haus am Stadtrand** `sa`→`koffer` | Auto fährt vor, Falko daneben; Schloss-Icon zu → offen („Einbruch“), Schmuck erscheint („Schmuck: 3.000 €“), wandert in das Auto („im Kofferraum weg“) | fluent-hc:`house-with-garden`, `locked`, `unlocked`, `gem-stone`, `ring`, `ten-oclock`, `crescent-moon`, `automobile` | `Fall · Samstag, 22 Uhr: das Haus am Stadtrand` → `… Falko bricht ein` → `… Schmuck für 3.000 €` → `… Die Beute im Kofferraum` | Kofferraumklappe (`szene_194kofferraum_1`) |
| **A3 Frage** `frage`, `frage2` | Falko, Auto mit Schlüssel, Hedda; Haken „Falko: Täter“, „Und Hedda?“, „nur ein Auto verliehen“, „Wie viel Hilfe macht strafbar?“ | fluent-hc:`automobile`, `key` | `Fall · Falko: Täter. Und Hedda?` → `Fall · Wie viel Hilfe macht strafbar?` | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | – |
| **C Wortlaut § 27** `p27`→`p27s2` | Wortlautkarten Abs. 1 und Abs. 2, Marker synchron; beide Figuren rechts | fluent-hc:`balance-scale` | `Beihilfe, § 27 StGB › Wortlaut Abs. 1` → `… › zwingende Milderung, § 49 Abs. 1` | – |
| **D Prüfschema I. 1. a)** `sch`→`lim` | breite Schemakarte, Punkt für Punkt; Kreuz „schuldhaft? nicht nötig“, Wortlautkarte § 29, „= limitierte Akzessorietät“ | – | `Prüfschema › I. Tatbestand › 1. a) …` | – |
| **E1 b) Hilfeleisten** `s1b`→`zeit` | Blöcke physisch/psychisch, Haken Vorbereitung, Fundstellen | fluent-hc:`handshake`, `automobile`, `light-bulb`, `spiral-calendar` | `Prüfschema › I. 1. b) Hilfeleisten › …` | – |
| **E2 Meinungsstand** `streit`→`meist` | Block „Rspr. (BGH): Förderungsformel“ (Haken/Kreuz), Block „h. L.: Kausalität“, Argument, „meist gleiches Ergebnis“, Fundstellen (BGH mit Rn., Lehre nach Hefendehl) | fluent-hc:`balance-scale`, `classical-building`, `link`, `handshake` | `Prüfschema › I. 1. b) Wie stark muss die Hilfe wirken? › …` | – |
| **F 2. Gehilfenvorsatz** `s2`→`v2` | Vorsatz 1 (wesentliche Merkmale: Unrechtsgehalt, Angriffsrichtung; Kreuz Einzelheiten), Vorsatz 2 (eigene Hilfe) | fluent-hc:`brain`, `house`, `white-question-mark`, `handshake` | `Prüfschema › I. 2. doppelter Gehilfenvorsatz › …` | – |
| **G Schema komplett** `s_ii`→`strafe` | breite Karte: I. (Zusammenfassung), II., III. zum Wort, Block Strafe | – | `Prüfschema › II. …` → `… › Strafe: § 27 Abs. 2 StGB` | – |
| **H1 Lösung Haupttat** `loes`→`mitt` | Haken Haupttat, Block schwerer Wohnungseinbruchdiebstahl, Privatwohnung (BGH 5 StR 671/19), Kreuz Mittäterschaft, Verweis | fluent-hc:`house`, `unlocked`, `house-with-garden`, `gem-stone` | `Lösung › Hedda › 1. a) …` → `… › zuerst: Mittäterin? nein` | – |
| **H2 Hilfeleisten** `hl`→`hl4` | Auto: Fahrt und Abtransport; BGH (+), h. L. (+), Streitentscheid entbehrlich | fluent-hc:`automobile`, `classical-building`, `link`, `handshake` | `Lösung › Hedda › 1. b) …` | – |
| **H3 Vorsatz** `vs`→`rws` | vier Haken (Haupttat bekannt, Einzelheit, Auto hilft, Missbilligung unerheblich), II./III. (+) | fluent-hc:`house`, `white-question-mark`, `key`, `thinking-face`, `balance-scale` | `Lösung › Hedda › 2. …` → `… › II. Rechtswidrigkeit, III. Schuld` | – |
| **H4 Ergebnis** `erg`, `rahmen` | Ergebnisblock mit Normkette; Strafrahmen Täter 1–10 Jahre, Gehilfin 3 Monate bis 7 Jahre 6 Monate | fluent-hc:`balance-scale` | `Ergebnis · …` | – |
| **I1 sukzessive Beihilfe** `sf`→`sukz2` | BGH bis Beendigung, Teile der Lehre bis Vollendung | fluent-hc:`white-question-mark`, `package`, `stopwatch` | `Sonderfälle › 1. …` | – |
| **I2 neutrale Handlungen, Unterlassen** `taxi`→`unterl` | Taxi: sicheres Wissen (+), nur möglich (−), Ausnahme tatgeneigter Täter; Unterlassen nur mit Garantenstellung | fluent-hc:`taxi`, `house`, `white-question-mark`, `shield` | `Sonderfälle › 2. …` → `… › 3. Beihilfe durch Unterlassen` | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **K Merksatz** `merke`→`mk3` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops. Bewegungen: Schlüssel wandert von Hedda zu Falko, Auto fährt vor, Schmuck wandert ins Auto.
**Darstellung des Einbruchs:** nur Haus-Icon und Schloss-Icon (zu → offen) mit Pille „Einbruch“; keine Tür, kein Fenster, kein Werkzeug, keine Methode, kein Opfer im Bild.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 27 Abs. 1 und 2, § 29 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, vorgelesen; Marker synchron.
**Abweichung vom Standardablauf (bewusst, nach Auftrag):** Das Klausurschema steht nicht am Ende, sondern trägt das Video: Es baut sich in D–G Punkt für Punkt auf (Zwischenfolien E1, E2, F vertiefen b) und 2.), danach folgt die Lösung am Fall entlang derselben Gliederung.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Am Freitagabend erzählt Falko seiner Freundin Hedda offen, dass er am Samstag in ein Einfamilienhaus am Stadtrand einbrechen will. Dort wohnt eine Familie, die an dem Abend nicht zu Hause ist. Welches Haus genau, sagt er nicht.
>
> Falko: „Leihst du mir dein Auto? Mit dem Bus komme ich da nicht hin, und die Beute muss ja auch weg.“ Hedda: „Ich finde das falsch. Aber gut, hier ist der Schlüssel. Bring ihn mir Sonntag zurück.“ Von der Beute will Hedda nichts.
>
> Am Samstag um 22 Uhr fährt Falko mit dem Auto von Hedda zu dem Haus, bricht ein und nimmt Schmuck für 3.000 € mit. Die Beute bringt er im Kofferraum weg.
>
> **Hat sich Hedda strafbar gemacht?**
