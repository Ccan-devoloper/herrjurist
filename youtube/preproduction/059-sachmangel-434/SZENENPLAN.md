# Folge 059 · Sachmangel § 434 BGB: Wann ist eine Sache mangelhaft? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_059.py`](src/skript_059.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Kaufrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Der Laptop funktioniert – nur nicht mit der Software, die ihr ausdrücklich vereinbart hattet“): Kerstin (privat) fragt im Computerladen von Herrn Kranich, ob ihr Schnittprogramm auf dem Laptop läuft; er bejaht, Netzteil und Anleitung sind dabei. Sie kauft für 900 € und nimmt den Laptop mit. Zu Hause funktionieren Internet und E-Mail, das Schnittprogramm startet nicht (Grafikkarte zu schwach). Ablauf: Fall → Frage → Sachverhalt → § 433 I 2 und Wortlaut § 434 I (Gleichrang, Gefahrübergang § 446) → I. subjektiv (Wortlautkarte § 434 II, Subsumtion) → II. objektiv (Wortlautkarte § 434 III 1, Subsumtion, Werbung und III 3, Wortlautkarte III 2 mit Reparierbarkeit) → Gleichrang am Fall → Verbrauchsgüterkauf (§ 476 I 2, § 475b) → III. Montage § 434 IV → IV. Gleichstellung § 434 V (Wortlautkarte), Menge → Rechtsmangel § 435, Vermutung § 477 → Ergebnis, Ausblick § 437 (Folge 063) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:52,4 (5.885 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Kerstin (KE), um 40 | Käuferin, Verbraucherin | `standing/polka_dots` (gepunktete Bluse, Hose Lila `#B8A9F5`, schwarze Schuhe), Kopf `Medium Straight`, Haut `#F2C9A5`; Mimiken `Calm`, `Smile Big|Smile` (froh), `Smile` (redet), `Very Angry` (Ärger; redet), `Serious` (denkt), `Suspicious` (überlegt), `Concerned|Serious` (Sorge) | `sabrina` (Frau, mittel) |
| Herr Kranich (KR), um 45 | Inhaber des Computerladens, Unternehmer | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`, schwarze Schuhe), Kopf `Short 3`, Brille `Glasses 2`, Haut `#E0A47E`, kein Bart; Mimiken `Calm`, `Smile` (froh; redet), `Suspicious` (denkt), `Serious` (ernst), `Concerned|Serious` (Sorge) | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft gegen alle `skript_*.py`, `SZENENPLAN.md`, `ABNAHME.md` und die Liste des Koordinators): Kerstin, Kranich. Kein Genitiv eines Namens im Sprechtext („der Laptop von Kerstin“).
- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zu Herrn Kranich), `_r` blickt nach rechts (Herr Kranich im Laden zu Kerstin).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `KE_redet`, `KE_aerger`, `KR_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig; gebraucht sabrina (Käuferin) und marc (Händler). Vorfolge 058 nutzte niklas/helmut; 057 nutzte alle vier Pool-Stimmen (nicht vermeidbar).
- Kopfprobe: `standing/pointing_finger-1` für Kerstin verworfen (Oberteil ließ sich nicht einfärben, ganz schwarz, Haar verschmolz). Keine Prothesen-Posen, keine Bärte. `crossed_arms-2` und `polka_dots` erscheinen in 053–058 nicht.
- Figuren-PNGs: `../peeps/op_059/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 058 (Heroinspritze), 057 (Seeufer/Steg), 056 (Lernplatz, Zimmerwand), 053 (Vorgarten, Fahrrad, Internetanzeige). Hier neu: Computerladen mit Ladentisch, Laptop, Netzteil und Anleitung; Schreibtisch zu Hause mit Statussymbolen (Internet/E-Mail mit Haken, Schnittprogramm durchgestrichen mit Kreuz).

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Laden** `fall`–`kauf` | Kerstin (Videoschnitt), Computerladen, Ladentisch, Laptop; Blasen Kerstin und Kranich; Netzteil, Anleitung; 900 €; Laptop wandert zu Kerstin | tabler:`movie`, `building-store` (Gelb), `device-laptop` (Hellblau), `plug`, `book`, `cash-banknote` (Grün); Ladentisch aus `karte` | `Fall · Videos in der Freizeit` (ab 0,0 s) → `Fall · Im Computerladen` → `Fall · Der Kauf` | Freizeit · Laden · Laptop · Blase Kerstin · Blase Kranich · Netzteil · Anleitung · 900 € · Mitnahme | – |
| **A2 zu Hause** `haus`–`frage2` | Tisch mit Laptop; Internet ✓, E-Mail ✓, Schnittprogramm ✗, „Grafikkarte zu schwach“; Kerstin ärgert sich (Blase); zwei Fragen | tabler:`world-www`, `mail`, `movie-off` (Rot), `device-laptop`; Tisch aus `karte`/`linienzug` | `Fall · Zu Hause` → `Fall · Das Schnittprogramm startet nicht` → `Fall · Die Frage` | Zuhause · Internet · E-Mail · Programm ✗ · Grafikkarte · Blase · Frage 1 · Frage 2 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 434 I** `norm`–`gefahr` | Tafel, Wortlautkarte mit 5 Markern, drei Farbblöcke, Gefahrübergang | tabler:`device-laptop`, `building-store` | `Mangelfreie Sache · § 433 Abs. 1 Satz 2 BGB` → `§ 434 Abs. 1 BGB › Wortlaut` → `› drei Anforderungen gleichrangig` → `› bei Gefahrübergang, § 446 Satz 1 BGB` | | – |
| **D1 § 434 II** `sub`–`kompat` | Wortlautkarte (Auszug) mit 6 Markern, drei Punkte | tabler:`device-laptop`, `movie`, `plug` | `I. Subjektive Anforderungen › § 434 Abs. 2 BGB` → `› Kompatibilität, § 434 Abs. 2 Satz 2 BGB` | | – |
| **D2 Subsumtion subjektiv** `subs`–`sube` | Kreuze/Haken, roter Block | tabler:`movie-off`, `plug`, `device-laptop` | `I. Subjektive Anforderungen › der Laptop von Kerstin` | | – |
| **E1 § 434 III 1** `obj`–`o4` | Wortlautkarte (Auszug) mit 5 Markern | tabler:`device-laptop`, `plug` | `II. Objektive Anforderungen › § 434 Abs. 3 BGB` | | – |
| **E2 Subsumtion objektiv** `osub`, `ook` | Haken, grüner Block | tabler:`world-www`, `file-text` | `II. Objektive Anforderungen › der Laptop von Kerstin` | | – |
| **E3 Werbung** `werb`–`ausn` | Tafel, Akku-Abwandlung, drei Ausnahmen, BGH-Randbeleg | tabler:`speakerphone` (Gelb), `battery-4` (Grün), `battery-1` (Rot) | `› Werbung, § 434 Abs. 3 Satz 1 Nr. 2 b BGB` → `› Ausnahme, § 434 Abs. 3 Satz 3 BGB` | | – |
| **E4 § 434 III 2** `rep`, `rep2` | Wortlautkarte mit 3 Markern, Pille Reparierbarkeit, Übergangsrecht | tabler:`shield-check`, `tool` | `› übliche Beschaffenheit, § 434 Abs. 3 Satz 2 BGB` → `› Reparierbarkeit, Art. 229 § 72 EGBGB` | | – |
| **F1 Gleichrang** `gleich`–`gl3` | zwei Blöcke mit ✗/✓, roter Block, Abwandlung Akku | tabler:`device-laptop`, `battery-1` | `Gleichrang · eine verfehlte Anforderung genügt` | | – |
| **F2 Verbrauchsgüterkauf** `vgk`–`p475b` | Tafel, Rollenpillen | tabler:`file-certificate`, `refresh` | `Verbrauchsgüterkauf · …` → `· Abweichung, § 476 Abs. 1 Satz 2 BGB` → `· Aktualisierungen, § 475b BGB` | | – |
| **G Montage** `mont`–`mo3` | Tafel, zwei Kreuze | tabler:`assembly`, `tools`, `book` (Rot), `device-laptop` | `III. Montageanforderungen › § 434 Abs. 4 BGB` | | – |
| **H Gleichstellung** `ali`, `menge` | Wortlautkarte § 434 V, zwei Laptops (anderes Modell orange), Pakete | tabler:`device-laptop`, `packages` | `IV. Gleichstellung › andere Sache, § 434 Abs. 5 BGB` → `› Menge gehört zur Beschaffenheit, § 434 Abs. 2 Satz 2 BGB` | | – |
| **I1 Abgrenzung, Beweis** `recht`, `p477` | zwei Blöcke Sach-/Rechtsmangel, § 477 | tabler:`users` (Lila), `calendar-event` | `Abgrenzung · Rechtsmangel, § 435 BGB` → `Beweis · Vermutung, § 477 Abs. 1 BGB` | | – |
| **I2 Ergebnis** `erg`, `p437` | roter Block, Verweis Folge 063 | tabler:`movie-off`, `scale` | `Ergebnis · der Laptop ist mangelhaft` → `Ausblick · Käuferrechte, § 437 BGB` | | – |
| **J Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · alle drei Anforderungen prüfen` | | – |
| **K Klausurschema** `sch`–`k5` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` → `Klausurschema › Montage und Gleichstellung` | | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt, Merksatz mit 2 Markern | – | `Merksatz` | | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Mitnahme des Laptops.
**Blasen:** Stil C (Standard seit 02.10.2026, `bausteine.blase`), wortgleich mit dem Gesprochenen; keine Zahlen in den Blasen. Zahlen auf Tafeln und Pillen als Ziffern („900 €“, „10 Stunden“, „31.7.2026“, „2028“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Kerstin schneidet in ihrer Freizeit Videos. Im Computerladen von Herrn Kranich fragt sie: „Auf dem Laptop muss mein Schnittprogramm laufen. Geht das?“ Herr Kranich antwortet: „Ja, das läuft darauf. Netzteil und Anleitung sind dabei.“
>
> Kerstin kauft den Laptop für 900 Euro und nimmt ihn gleich mit. Zu Hause startet er sofort, Internet und E-Mail funktionieren. Nur das Schnittprogramm startet nicht, weil die Grafikkarte zu schwach ist.
>
> **Ist der Laptop mangelhaft, obwohl er funktioniert?**
