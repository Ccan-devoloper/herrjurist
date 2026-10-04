# Folge 198 · Heimtücke § 211: Arglosigkeit, Wehrlosigkeit & Schlafende – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_198.py`](src/skript_198.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Format „Schema“. Aufbau nach Auftrag: Fall nach dem Plan-Hook (Versöhnungsessen, Angriff beim Hinsetzen; Datum und Uhrzeit als Ziffern) → Frage → Sachverhalt → Wortlautkarten § 211 Abs. 1 und Abs. 2 (Auszug „heimtückisch“) → Definition (BGH mit Rn.) und Prüfschema a) Arglosigkeit, b) Wehrlosigkeit, c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung → Vertiefung a) bis d) → Sonderfälle (Schlafende, Kleinkinder/schutzbereite Dritte, Besinnungslose) → Lösung → Restriktion (Rechtsfolgenlösung mit einem Satz Verweis auf Folge 007; Lehre: verwerflicher Vertrauensbruch als Meinung) → Klausurtipp (Lexi) → Merksatz (Lexi). Vorlagen: 075 (Mordmerkmale, nur Verweis), 007 (Rechtsfolgenlösung, nur Verweis), 035, 194 (Hilfsfunktionen), 015 (Namens- und Sichtprüfung).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Heribert (HB), um 60 | Täter, lädt zum Versöhnungsessen | `standing/easing-1` (Jacke Lila `#B8A9F5`, Oberteil Weiß, schwarze Hose der Pose), Kopf `Gray Short` (Haar Grau `#BDBDBD`), Haut `#E8B894`. Mimiken `Calm`, `Serious`, `Suspicious` (Tatentschluss), `Solemn`, `Smile` (lädt ein; redet), `Concerned|Serious` (Streit) | `helmut` (Mann, älter) |
| Siegmund (SG), um 40 | Geschäftspartner und Opfer | `standing/resting-1` (Pullover Türkis `#7FD6D0`, schwarze Hose der Pose), Kopf `Short 5`, Haut `#D9A27A`. Mimiken `Calm`, `Smile` (froh; redet), `Concerned|Serious` (Streit), `Suspicious`, `Serious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Büro und Esszimmer: Heribert (`_r`) und Siegmund blicken einander an; Tafelfolien: beide zur Tafel; Lexi zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HB_redet`, `SG_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. 46 Figuren-PNGs in `../peeps/op_198/` (Drive-Master).
- **Klischeeprüfung:** Täter gewöhnlich gekleidet (lila Hemdjacke), keine „fiese“ Mimik, keine Waffe; keine Zuordnung von Herkunft oder Hautfarbe zur Täterrolle.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rliw` in keinem Text unter `youtube/` (04.10.2026): Heribert, Siegmund. Verworfen: Gerhard (160, 177, 196), Hermann (166), Leonhard (mögliche englische Lesart „Leonard“). Im Sprechtext nie im Genitiv („das Vertrauen in die Versöhnung“).
- **Stimmen** nur aus dem zugeteilten Pool (helmut, niklas; ela_froh und julia nicht verwendet: ela_froh nicht für ernste Rollen, julia möglichst meiden). Vorfolgen 194 (stephan, lucy), 195/196 (andere Pools): keine Überschneidung mit 194; helmut und niklas zuletzt gemeinsam in 193 (Pool-Vorgabe des Koordinators).

**Abweichung von den letzten Folgen (194 Haustür/Stadtrand, 195 Gerichtssaal/Kosten, 196 Flughafen):** neue Schauplätze Büro einer kleinen Firma (Rückwand, Fenster, Schreibtisch mit Abrechnung und Geldsack) und Esszimmer (Tisch mit Pfanne, Salat, Brot, zwei Stühle); Posen `easing-1` und `resting-1` in 194–196 nicht verwendet (dort `robot_dance-2/-3`, `blazer-3/-4`, `pointing_finger-2`, `crossed_arms-1/-2`); kein Polka-Dots-Muster; Farben Lila/Türkis neu gegenüber 194 (Grün/Rot) und 196 (Rot/Dunkelblau).
**Tageslicht:** Cremegrund durchgehend; 19 Uhr nur über Uhr-Icon und Pille.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Büro** `fall`→`le1` | Rückwand, Fenster, Schreibtisch; Heribert links, Siegmund rechts ab 0,0 s; Pillen „zusammen eine kleine Firma“, „seit Wochen: heftiger Streit ums Geld“ (Geldsack, Ärger-Symbole), „Heribert beschließt: Siegmund töten“, „Einladung zum Versöhnungsessen“ (Teller mit Spaghetti); Blase Heribert „Lass uns den Streit begraben. Komm am Donnerstag um 19 Uhr zu mir zum Essen.“; Blase Siegmund „Gern. Ich bin froh, dass wir uns wieder vertragen.“ | fluent-hc:`office-building`, `page-facing-up`, `money-bag`, `anger-symbol`, `spaghetti`; Wand, Fenster, Tisch als Bausteine | `Fall · Heribert und Siegmund: eine Firma` (ab 0,0 s) → … → `Fall · Siegmund sagt zu` | – |
| **A2 Esszimmer** `abend`→`frage2` | Tisch mit Pfanne, Salat, Brot, zwei Stühle; Pille „Donnerstag, 12.3., 19 Uhr“ mit Uhr; Siegmund kommt (froh), „glaubt an die Versöhnung“; beim Wort „setzt“ tritt er an seinen Stuhl (Stuhlrücken); Pille „Heribert greift ihn mit Tötungsvorsatz an“ (nur Text); nach „stirbt“ ist Siegmund nicht mehr da, Pille „Siegmund stirbt“; „Ist das Mord?“, „wusste vom Streit – trotzdem arglos?“ | fluent-hc:`chair`, `shallow-pan-of-food`, `green-salad`, `bread`, `seven-oclock` | `Fall · Donnerstag, 12.3., 19 Uhr: das Versöhnungsessen` → … → `Fall · Trotz Streit arglos?` | Stuhl (`szene_198stuhl_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | – |
| **C Wortlaut § 211** `p211`→`v075` | Wortlautkarten Abs. 1 und Abs. 2 (Auszug), Marker synchron; Pillen „2. Gruppe …“, Verweis Folge Mordmerkmale; beide Figuren rechts | fluent-hc:`balance-scale`, `spaghetti` | `Mord, § 211 StGB › …` | – |
| **D Definition und Schema** `def`→`sd` | breite Karte: Definition (BGH 2 StR 352/24 Rn. 25), Prüfschema a)–d) Punkt für Punkt | – | `Heimtücke › …` → `… › Prüfschema › d) feindliche Willensrichtung` | – |
| **E a) Arglosigkeit** `arg`→`angst` | Block Definition, „maßgeblich: genau dieser Moment“, heimlich nicht nötig/offen feindselig, latente Angst | fluent-hc:`dove`, `stopwatch`, `high-voltage`, `anger-symbol` | `Heimtücke › a) Arglosigkeit › …` | – |
| **F b) Wehrlosigkeit** `wehr`→`folge` | Block Definition, drei Kreuze (verteidigen, fliehen, Hilfe holen), „Folge der Arglosigkeit“ | fluent-hc:`shield`, `door`, `dove` | `Heimtücke › b) Wehrlosigkeit › …` | – |
| **G c) und d)** `aus`→`feind` | Ausnutzungsbewusstsein, „mit einem Blick“, feindliche Willensrichtung | fluent-hc:`brain`, `eye`, `balance-scale` | `Heimtücke › c) …` → `Heimtücke › d) feindliche Willensrichtung` | – |
| **H1 Schlafende** `sf`→`schlaf2` | „Drei Sonderfälle“, 1. Schlafende; Bett, „zzz“ | fluent-hc:`white-question-mark`, `bed`, `zzz` | `Sonderfälle › 1. Schlafende …` | – |
| **H2 Kleinkinder** `kind`→`kind3` | 2. Kleinkinder, schutzbereiter Dritter, Eltern in der Nähe; nur Gegenstands-Icons (keine Menschen-Icons) | fluent-hc:`baby-bottle`, `shield`, `house` | `Sonderfälle › 2. …` | – |
| **H3 Besinnungslose** `koma`, `koma2` | 3. Besinnungslose, Pflegepersonal | fluent-hc:`hospital`, `stethoscope` | `Sonderfälle › 3. …` | – |
| **I1 Lösung a)** `loes`→`falle` | Arglosigkeit trotz Streit, Lockfall | fluent-hc:`spaghetti`, `anger-symbol`, `dove` | `Lösung › Heribert › a) …` | – |
| **I2 Lösung b)–d)** `lb`→`ld` | Haken zu b), c), d) | fluent-hc:`chair`, `shield`, `brain`, `balance-scale` | `Lösung › Heribert › b) … d)` | – |
| **I3 Ergebnis** `erg`, `erg2` | Ergebnisblock Mord; Heribert allein | fluent-hc:`spaghetti`, `balance-scale` | `Ergebnis · …` | – |
| **J Restriktion** `restr`→`hier` | Grund, BGH Rechtsfolgenlösung (Verweis 007), Meinung Lehre, BGH dagegen, Subsumtion | fluent-hc:`balance-scale`, `classical-building`, `handshake`, `spaghetti` | `Einschränkung der Heimtücke? › …` | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | – |
| **L Merksatz** `merke`→`mk3` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Gewalt zurückhaltend:** kein Angriff, keine Waffe (auch kein Messer-Icon; Besteck-Icons mit Messer bewusst vermieden), kein Blut, keine Leiche; der Angriff steht nur als Text auf einer Pille.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 211 Abs. 1 (vorgelesen) und Abs. 2 als gekennzeichneter Auszug, wörtlich nach gesetze-im-internet.de.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Heribert und Siegmund führen zusammen eine kleine Firma und streiten seit Wochen heftig ums Geld. Heribert beschließt, Siegmund zu töten, und lädt ihn zu einem Versöhnungsessen ein.
>
> Heribert: „Lass uns den Streit begraben. Komm am Donnerstag um 19 Uhr zu mir zum Essen.“ Siegmund: „Gern. Ich bin froh, dass wir uns wieder vertragen.“
>
> Am Donnerstag, dem 12.3., kommt Siegmund um 19 Uhr pünktlich. Er glaubt an die Versöhnung und rechnet mit einem friedlichen Abend. Als er sich an den Tisch setzt, greift Heribert ihn mit Tötungsvorsatz an. Siegmund stirbt.
>
> **Hat sich Heribert wegen Mordes strafbar gemacht?**
