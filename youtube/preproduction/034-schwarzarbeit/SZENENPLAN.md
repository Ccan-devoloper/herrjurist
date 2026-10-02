# Folge 034 · Schwarzarbeit: Kein Werklohn, keine Mängelrechte, kein Geld zurück? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_034.py`](src/skript_034.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall als Übungsfall nach dem Muster von BGHZ 198, 141). Ablauf: Fall (Angebot „ohne Rechnung“, Anzahlung, Pflaster, abgesackte Steine, Streit) → Frage → Sachverhalt → Vorfrage Nichtigkeit (Wortlaut § 134 BGB, § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG) → Verstoß im Fall (Vorsatz, Kenntnis und bewusstes Ausnutzen) → Gegenfall einseitiger Verstoß → A. Herr Fuchs (Werklohn, GoA, Wertersatz, Wortlaut § 817 S. 2) → B. Frau Ziegler (Mängelrechte, Anzahlung) → Ergebnis → Rechtsprechungslinie 1990–2017 → Streitstand nachträgliche Abrede → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:15 (5.296 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Ziegler (ZI), um 65 | Bestellerin, Hausbesitzerin | `standing/blazer-4` (Jackett Lila `#B8A9F5`, Oberteil Weiß, schwarze Hose), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Smile` (redet), `Driven` (redet, fordernd), `Fear`, `Concerned|Serious`, `Serious`, `Suspicious`, `Tired` | `lisa` (Frau, älter) |
| Herr Fuchs (FU), um 40–45 | selbstständiger Pflasterer, Unternehmer | `standing/crossed_arms-1` (Oberteil Blau `#8DB3F2`, schwarze Hose), Kopf `hat-beanie` (Arbeitsmütze), kein Bart, Haut `#D9A47A`; Mimiken `Calm`, `Smile`, `Smile` (redet), `Driven` (redet, fordernd), `Serious`, `Suspicious`, `Concerned|Serious`, `Tired` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen nur aus dem Pool** stephan, lisa (timo, hilde nicht gebraucht). Keine Überschneidung mit 033 (laura_klar, niklas, helmut) und 032 (christian, ela_warm, julia).
- **Namen:** „Ziegler“ und „Fuchs“ – eindeutig deutsch, nicht in früheren Folgen vergeben; Prüfung je Nennung in ABNAHME.md.
- **Keine Wertung über Personen:** neutrale Mimiken (ertappt/nachdenklich/müde), keine Karikatur, kein „Täter“-Klischee.
- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Frau Ziegler in der Fallszene zu Herrn Fuchs). Herr Fuchs blickt in der Fallszene nach links zu ihr.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `ZI_redet`, `ZI_fordert`, `FU_redet`, `FU_fordert` (je links/rechts) und Lexi.
- Figuren-PNGs: `../peeps/op_034/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 033 (Notwehr vor der Stadtbibliothek), 032 (Farbengeschäft), 031 (Selbstbedienungsladen 1963), 029 (Mauer im Garten). Hier neu: Wohnhaus mit Einfahrt im **Querschnitt** (Sandbett, eine Reihe Pflastersteine, die später absacken), Geld wandert sichtbar von der Bestellerin zum Pflasterer. Neue Posen gegenüber 031–033 (`blazer-4`, `crossed_arms-1`, Kopf `hat-beanie`, `Gray Bun`). Dritte Folge mit Wortlautkarten (hier drei: § 134 BGB, § 1 Abs. 2 S. 1 Nr. 2 SchwarzArbG, § 817 S. 2 BGB); erste Folge mit Rechtsprechungslinie als Jahresleiste.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Einfahrt** `fall`–`frage3` | Haus links, Einfahrt im Querschnitt (Sandbett), Frau Ziegler links (blickt nach rechts), Herr Fuchs rechts; Angebot, Zusage, Anzahlung (Geldschein wandert), Pflaster entsteht, Steine sacken ab, Streit, Frage-Pillen | tabler: `home` (Gelb), `receipt-off`, `cash-banknote` (Grün), `hammer` (Gelb); Einfahrt/Steine aus `karte`, Boden `linienzug` | `Fall · Die Einfahrt` (ab 0,0 s) → `· Das Angebot` → `· Anzahlung und Pflaster` → `· Der Streit` → `· Die Frage` | Grundbild · Fuchs · Blase Fuchs · ohne Rechnung · 5.000 € · Blase Ziegler · Geld · 2.000 € · Pflaster · uneben/Schreck · Blase Ziegler · Blase Fuchs/3.000 € · drei Frage-Pillen | Geldscheine `szene_034geld_1` bei „zahlt“; Hammer `szene_034hammer_1` beim Pflastern |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Vorfrage** `vor`–`verbot` | Wortlautkarten § 134 und § 1 Abs. 2 SchwarzArbG mit Markern; beide Figuren | tabler: `ban`, `receipt-off` | `Vorfrage · Ist der Werkvertrag wirksam?` → `· § 134 BGB: gesetzliches Verbot` → `· § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG` | Titel · Karte § 134 · 2 Marker · Karte § 1 · 4 Marker · Verbot-Block | – |
| **D Verstoß im Fall** `fu`–`nichtig` | Tafel, beide Figuren | tabler: `receipt-off`, `eye`, `coins` (Gelb) | `Nichtigkeit · Verstoß von Herrn Fuchs` → `· Kenntnis und bewusstes Ausnutzen` → `· Ergebnis` | ✓ Fuchs · vorsätzlich · offen (Rn. 22) · Kenntnis · ✓ spart · Block nichtig | – |
| **E Gegenfall** `gegen`–`gegen3` | Tafel, beide Figuren | tabler: `eye-off`, `tool` (Grün) | `Gegenfall · einseitiger Verstoß` | heimlich · ✓ wirksam · ✓ Mängelrechte | – |
| **F1 Herr Fuchs I.–III.** `a`–`b2` | Tafel, beide Figuren | tabler: `file-invoice`, `scale` | `A. Herr Fuchs gegen Frau Ziegler` → `› I. Werklohn` → `› II. GoA` → `› III. Wertersatz` | Titel · I. · ✗ · II. · ✗ · III. · ✓ · ✓ | – |
| **F2 § 817 S. 2** `p817`–`werg` | Wortlautkarte § 817 S. 2 mit Markern | tabler: `lock` (Gelb) | `A. Herr Fuchs › III. Wertersatz › § 817 Satz 2 BGB` → `› Ergebnis` | Karte · 2 Marker · ✓ selbst verstoßen · ✓ auch § 812 · Block | – |
| **G1 Mängelrechte** `m`–`m3` | Tafel, Frau Ziegler allein | tabler: `tool` (Grün) | `B. Frau Ziegler gegen Herrn Fuchs` → `› I. Mängelrechte, § 634 BGB` | I. · Rechte · Voraussetzung · ✗ · ✗ Treu und Glauben | – |
| **G2 Anzahlung** `r`–`r3` | Tafel, beide Figuren | tabler: `cash-banknote`, `lock` | `B. Frau Ziegler › II. Rückzahlung, § 812 Abs. 1 S. 1 Alt. 1 BGB` | II. · ✓ · diente · ✗ gesperrt | – |
| **H Ergebnis** `erg`–`e4` | Tafel, beide Figuren müde | – | `Ergebnis · kein Ausgleich` | ✗ Fuchs · ✗ Ziegler · kein Ausgleich · Block | – |
| **I Rechtsprechungslinie** `linie`–`l17` | Tafel mit Jahreszeilen, Richterhammer mit wechselnder Jahreszahl | tabler: `gavel` (Gelb) | `Rechtsprechungslinie · BGH, VII. Zivilsenat` | 1990 · 2013 · 2014 · Abschreckung · 2015 · 2017 | – |
| **J Streitstand** `st`, `st2` | Tafel, Waage, zwei Bücher | tabler: `scale`, `book` (Blau, Grün) | `Streitstand · nachträgliche Ohne-Rechnung-Abrede` | a. A. · Änderung · Ursprungsvertrag · BGH · Abrede · Block | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Nichtigkeit genau prüfen` → `· Teilbeträge ohne Rechnung` | 6 Halte | – |
| **L Klausurschema** `sch`–`s10` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · A · I. · Nichtigkeit · 1.–3. · II. · III. · B · I. · II. | – |
| **M Merksatz** `merke`, `mk2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 4 Halte | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Geldschein (Anzahlung).
**Geräusche:** zwei Handlungsgeräusche (Geldscheine, Hammer), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Ziegler lässt die Einfahrt vor ihrem Haus von dem selbstständigen Pflasterer Herrn Fuchs neu pflastern. Herr Fuchs bietet an: mit Rechnung teurer, ohne Rechnung bar 5.000 Euro. Frau Ziegler ist einverstanden. Herr Fuchs soll keine Rechnung stellen und keine Umsatzsteuer abführen; Frau Ziegler spart so die Umsatzsteuer.
>
> Frau Ziegler zahlt 2.000 Euro bar an, Herr Fuchs pflastert die Einfahrt. Wenige Wochen später sacken mehrere Steine ab, die Einfahrt ist uneben. Frau Ziegler verlangt Nachbesserung und will vorher nichts mehr zahlen. Herr Fuchs verlangt die restlichen 3.000 Euro.
>
> **Werklohn, Nachbesserung, Anzahlung zurück: Wer hat welche Ansprüche?**
