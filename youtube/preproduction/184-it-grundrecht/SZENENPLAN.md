# Folge 184 · Staatstrojaner und IT-Grundrecht: Darf die Polizei mitlesen? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_184.py`](src/skript_184.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Fiktiver Fall nach dem Plan-Hook: Die Polizei will heimlich Software auf dem Laptop von Herrn Weinhold installieren, um seine verschlüsselten Chats mitzulesen; Kommissar Hollstein ermittelt wegen des Verdachts der Geldfälschung durch eine Bande. Der Klassiker BVerfGE 120, 274 (Online-Durchsuchung, 2008) wird sachlich erklärt, ohne reale Beteiligte als Figuren; der heutige Stand nach Trojaner I/II (2025) ist eingearbeitet. Ablauf: Fall → Frage → Sachverhalt → I. Schutzbereich (Art. 10 GG, Art. 13 GG, informationelle Selbstbestimmung als Verweis auf das Video zum Volkszählungsurteil, Schutzlücke, IT-Grundrecht) → II. Eingriff (Quellen-TKÜ § 100a Abs. 1 S. 2, 3 StPO, Maßstab 2008/2025, Online-Durchsuchung § 100b StPO) → III. Rechtfertigung (Gefahrenabwehr: konkrete Gefahr für überragend wichtiges Rechtsgut; Strafverfolgung: besonders schwere Straftat; Richtervorbehalt; Kernbereich; seit 2025: Straftatengewicht der Quellen-TKÜ, Zitiergebot) → Lösung → Klausurtipp → Prüfungsschema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Weinhold (WH), um 35 | Beschuldigter; Laptop mit verschlüsseltem Messenger | Pose `sitting/mid-2` (grünes T-Shirt `#8FD694`, schwarze Hose aus der Pose, weiße Schuhe), sitzt auf einem Stuhl (Phosphor `chair`, Holz `#D6AA78`), Kopf `Pomp`, Haut `#E3B08C`; keine Brille, kein Bart; Mimiken `Calm`, `Driven` (tippt/konzentriert), `Cheeky|Smile` (selbstsicher, redet), `Suspicious`, `Concerned|Serious`, `Serious`, `Fear` | `niklas` (Mann, jung) |
| Kommissar Hollstein (HS), um 55 | Kriminalhauptkommissar, in Zivil (kein Logo, keine Uniform) | Pose `standing/blazer-1` (Sakko Schiefergrau `#6E7F99`, schwarzes Shirt, Hose Anthrazit `#3A3A44`, Beinprothese aus der Pose), Kopf `No Hair 2`, Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Driven`, `Smile`, `Solemn`, `Awe`; `HS_beschluss` (`Calm`, redet am Schluss) | `helmut` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner Datei unter `youtube/` und nicht auf der Koordinatorliste: **Weinhold**, **Hollstein** (beide nur von der Erzählerin genannt).
- **Stimmen** nur aus dem Pool (niklas, helmut); `ela_froh` und `julia` nicht verwendet, weil beide Sprechrollen ernst und männlich sind.
- **Keine realen Personen/Behörden:** Beschwerdeführer, Richter und Politiker treten nicht auf; das Gericht erscheint nur als Gebäude-Icon (Tabler `building-bank`), die Polizei nur als Kommissar in Zivil. Software als Holzpferdchen (Tabler `horse-toy`), Chats als Sprechblasen-Icons, kein echtes Messenger-Logo, keine technische Anleitung.
- **Prothesen-Pose** bewusst beim Ermittler, nicht beim Beschuldigten. Keine Bärte, keine Karikaturen, keine Herkunftsklischees.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `WH_redet`, `HS_redet`, `HS_beschluss` (je links/rechts) und Lexi.
- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zu Herrn Weinholds Seite), `_r` blickt nach rechts (Herr Weinhold zum Laptop).
- Figuren-PNGs: `../peeps/op_184/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen nicht aus 180–183 (dort easing-1/-2, crossed_arms-1, resting-1/-2, shirt-3/-4, blazer-3/-4, pointing_finger-2, robot_dance-3); erstmals eine sitzende Hauptfigur (`sitting/mid-2`); keine Polka Dots. Schauplatz neu: geteiltes Bild – links Herrn Weinholds Schreibtisch mit Laptop und Lampe, rechts das Büro von Kommissar Hollstein mit Schreibtisch und Bildschirm, getrennt durch eine graue Linie (180: Strafverfahren, 181: Getränkehandel, 182: Baustelle/Werkstatt, 183: Grundstückskauf).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Fall** `fall`→`frage` | geteiltes Bild: Laptop (links) · Büro mit Hollstein (rechts, ab 0,0 s) | tabler:`desk`, `device-laptop`, `lamp`, `device-desktop`, `horse-toy` (Software), `message-circle` ×2, `lock`; fluent-hc:`euro-banknote` | `Fall · Die Polizei und der Laptop` → `· Herr Weinhold` → `· Kommissar Hollstein` → `· Die Frage` | 16: Grundbild · „heimlich Software“ · Pferdchen · Chats · Weinhold · Verdacht · Banknote · Messenger/Schloss · Blase Weinhold · Hollstein redet (Blase) · Schloss am Bildschirm · zwei Fragen | – |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,9 s) | – | `Sachverhalt` | 1 | – |
| **C1 Art. 10 GG** `art10`→`ganz` | Tafel + Wortlautkarte Art. 10 Abs. 1; Weinhold sitzt | `mail`, `messages`, `database`, `file-search` | `I. Schutzbereich › 1. Art. 10 GG: Fernmeldegeheimnis` | 7 | – |
| **C2 Art. 13 GG** `art13`→`fern` | Tafel + Wortlautkarte Art. 13 Abs. 1 | `home`, `device-laptop`, `world` | `… › 2. Art. 13 GG: Wohnung` | 6 | – |
| **C3 Informationelle Selbstbestimmung** `ris`→`ris3` | Tafel, Verweis auf das Video zum Volkszählungsurteil | `user-shield`, `database` | `… › 3. informationelle Selbstbestimmung` | 5 | – |
| **C4 Schutzlücke, IT-Grundrecht** `luecke`→`integr` | Tafel | `shield`, `building-bank`, `shield-lock`, `lock`, `device-laptop` | `… › Schutzlücke` → `I. Schutzbereich › 4. IT-Grundrecht` | 7 | – |
| **D1 Quellen-TKÜ** `stpo`→`q2` | Tafel + Wortlautkarte § 100a Abs. 1 S. 2 StPO (3 Marker), Satz 3; Hollstein | `gavel`, `horse-toy`, `lock-open`, `messages` | `II. Eingriff › Strafprozessordnung` → `… › Quellen-TKÜ, § 100a Abs. 1 S. 2, 3 StPO` | 7 | – |
| **D2 Maßstab 2008/2025** `q08`→`beide` | Tafel, beide Figuren | – | `II. Eingriff › Quellen-TKÜ: Maßstab 2008` → `… seit 2025` | 3 | – |
| **D3 Online-Durchsuchung** `od`→`odm` | Tafel + Wortlautkarte § 100b Abs. 1 StPO (2 Marker), beide Figuren | `device-laptop`, `folders`, `shield-lock` | `II. Eingriff › Online-Durchsuchung, § 100b StPO` | 7 | – |
| **E1 Rechtfertigung** `schr`→`straf` | Tafel; Hollstein | `scale`, `shield`, `heart`, `file-search` | `III. Rechtfertigung › nicht schrankenlos` → `› Gefahrenabwehr: konkrete Gefahr` → `› Strafverfolgung: besonders schwere Straftat` | 8 | – |
| **E2 Richtervorbehalt, Kernbereich** `richt`→`kern3` | Tafel; Hollstein | `gavel`, `shield-lock`, `notebook`, `trash` | `› Richtervorbehalt` → `› Kernbereich privater Lebensgestaltung` | 6 | – |
| **E3 Seit 2025** `n1`→`fort` | Tafel; beide Figuren | – | `› seit 2025: Quellen-TKÜ` → `› Zitiergebot, Art. 19 I 2 GG` | 6 | – |
| **F1 Lösung (Tafel)** `loes`→`l4` | Tafel § 100b Abs. 1 Nr. 1–3, Abs. 2; Hollstein | fluent-hc:`euro-banknote`, `file-search`, `scale`, `device-laptop` | `Lösung · Herr Weinhold · § 100b Abs. 1, 2 StPO` | 6 | – |
| **F2 Zurück am Laptop und im Büro** `l5`→`h2` | geteiltes Bild wie A; Pillen zu Quellen-TKÜ/Online-Durchsuchung, Gericht, Löschen; Hollstein redet | `message-circle`, `folders`, `building-bank`, `trash` | `Lösung · Quellen-TKÜ oder Online-Durchsuchung` → `· Anordnung durch das Gericht` | 8 | – |
| **G Klausurtipp** `tipp`→`t4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Grundrecht nach der Art des Zugriffs` | 9 | – |
| **H Prüfungsschema** `sch`→`k8` | Schema baut sich auf | – | `Klausurschema` → `› I. Schutzbereich` → `› II. Eingriff` → `› III. Rechtfertigung` | 10 | – |
| **I Merksatz** `merke`/`m2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 6 | – |

**Übergänge:** 16 stumme Schiebeblenden zwischen 17 Folien; innerhalb harte Schnitte/Pops; keine Bewegung, kein Zoom.
**Geräusche:** keine. Ein Tippgeräusch (Freesound CC0 841434) war für die Marke `chat` vorgesehen und wurde nach der Sichtprüfung verworfen, weil Herr Weinhold im Bild nicht sichtbar tippt („lieber kein Geräusch als ein unpassendes“); die Datei wurde wieder entfernt.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Bestimmte Tatsachen begründen den Verdacht, dass Herr Weinhold mit einer Bande Falschgeld herstellt. Die Absprachen laufen über einen verschlüsselten Messenger auf seinem Laptop.
>
> Kommissar Hollstein meint, normales Abhören bringe nichts. Die Ermittler wollen heimlich Software auf dem Laptop installieren: nur um die laufenden Chats mitzulesen oder um den ganzen Laptop zu durchsuchen.
>
> **Welches Grundrecht schützt den Laptop? Ist der Zugriff zulässig?**

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen (Stil C). Tafeln schreiben Normen, Jahreszahlen und Strafrahmen in Ziffern („§ 100a“, „2008“, „3 Jahren“). Kleine graue Fundstellenzeilen (26–28 px) sind Belege, kein Sprechtext. Die Wortlautkarten (Art. 10 Abs. 1, Art. 13 Abs. 1 GG, § 100a Abs. 1 S. 2, § 100b Abs. 1 StPO) stehen als Zitat mit Normangabe; Art. 10 und Art. 13 liest die Erzählerin wörtlich, bei den StPO-Karten nennt sie die Merkmale, die Marker erscheinen zum Wort.
