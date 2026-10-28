# Folge 246 · Widerspruchsbescheid schreiben: Tenor, Gründe, Kosten, Belehrung – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_246.py`](src/skript_246.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · VwGO-Praxis, Themenplan-Format „Schema“; Perspektive Bescheidentwurf der Widerspruchsbehörde. Stilvorlagen 102/234 (Tenorierungstafeln) und 077 (Länder-Overlay) – nur verwiesen.
**Fall** (Hook „Als Referendarin im Landratsamt sollst du über einen Widerspruch gegen eine Hundehaltungsuntersagung entscheiden“; Land und Behörden fiktiv): Herr Holzapfel hält einen verspielten Mischling. Trotz Leinenanordnung läuft der Hund dreimal frei durch den Ort, einmal springt er eine Joggerin an. Die Gemeinde untersagt die Hundehaltung (2.3.2026). Herr Holzapfel: „Er ist doch ganz lieb! Und den Zaun habe ich erhöht. Ich lege Widerspruch ein.“ Herr Sperling (Gemeinde): „Die Untersagung bleibt. Wir helfen nicht ab und legen die Akte dem Landratsamt vor.“ Referendarin Körner: „Ich entwerfe den Widerspruchsbescheid. Aber was gehört da alles hinein?“
**Ablauf:** Fall → Frage → Sachverhalt → 1. Vorverfahren (Wortlautkarte § 68 Abs. 1, Overlay NRW/Niedersachsen) → 2. Abhilfe § 72 und Zuständigkeit § 73 Abs. 1 (Wortlautkarten) → 3. Bescheid: Kopf und Tenor → Gründe I/II (Zulässigkeit) → Begründetheit (Rechtmäßigkeit, Zweckmäßigkeit) → Kosten (§ 73 Abs. 3 Satz 3, Wortlautkarte § 80 Abs. 1 Satz 3 VwVfG) → Rechtsbehelfsbelehrung (Muster) → Zustellung (Wortlautkarte § 73 Abs. 3) → 4. typische Fehler → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:08,8 (5.141 Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Holzapfel (HO), um 68 | Hundehalter, Widerspruchsführer | Pose `standing/resting-2` (schwarzer Pullover der Pose, Hose Braun `#6B5A48`), Kopf `No Hair 3`, Brille `Glasses 2`, Haut `#EDBE9C`, 96 % Höhe; Mimiken `Calm`, `Smile` (redet), `Serious`, `Concerned\|Serious`, `Suspicious`, `Tired`, `Driven` | `william` (Mann, älter) |
| Herr Sperling (SP), um 45 | Sachbearbeiter der Gemeinde (Ausgangsbehörde) | `standing/crossed_arms-2` (schwarzes Oberteil der Pose, Hose `#3A4A6B`), Kopf `Short 5`, Haut `#A8714E`; `Calm`, `Serious` (redet), `Suspicious` | `marc` (Mann, mittel) |
| Frau Körner (KO), um 28 | Referendarin im Landratsamt (Widerspruchsbehörde) | `standing/blazer-4` (Blazer Lila `#B8A9F5`, weißes Oberteil, schwarze Hose der Pose), Kopf `Medium Bangs 2`, Haut `#F0C8A8`, 95 % Höhe; `Calm`, `Smile`, `Serious`, `Suspicious` (fragt), `Driven` | `laura_ruhig` (Frau, mittel) |
| Der Hund | verspielter Mischling, kein Mensch | Icon Fluent Emoji High Contrast `dog` (MIT), Füllung Holzbraun – freundlich, kein Kampfhund-Klischee | – |
| Lexi | Klausurtipp, Schema, Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Fallszene A1: Herr Holzapfel blickt nach rechts zu seinem Hund; A2/A3 und Tafeln: nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HO_redet`, `SP_spricht`, `KO_fragt` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots. Die Joggerin wird nicht gezeigt (nur Pille), also kein Icon-Mensch.
- **Posen/Kleidung nicht aus 243–245** (dort blazer-3, walking-2, blazer-2, pointing_finger-1, walking-3, robot_dance-2, shirt-1, robot_dance-3, crossed_arms-1, resting-1, polka_dots, shirt-4, shirt-3): resting-2, crossed_arms-2 und blazer-4 kommen dort nicht vor.
- **Stimmen nur aus dem Pool** (`william`, `marc`, `laura_ruhig`; `sabrina` nicht gebraucht). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Holzapfel, Sperling, Körner – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` unter `youtube/` ohne Treffer (außer Themenplan nicht gesucht); verworfen: Bruno (009), Lampe (007/035), Sauer (221), Kiefer (zu nah an Körner). Eingetragen als „246: Holzapfel, Sperling, Körner“ vor der Vertonung. Kein Genitiv eines Namens im Sprechtext.
- Figuren-PNGs: `../peeps/op_246/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 244 Innenstadtstraße/Jugendzentrum, 243 Malerbetrieb/Polizei/Hauptverhandlung, 242 Notar/Straße, 241 Redaktion/Büro/Amtsgericht, 234 Stadtbücherei/Gericht. Hier neu: **Haus mit rotem Dach und Garten am Ortsrand** (programmatisch, Zaun aus Tabler-Zaunfeldern, Baum, Briefkasten), **Gemeinde** und **Landratsamt** als Behördenschreibtische (Tabler `building-community`/`building`, Holztisch programmatisch). Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Haus mit Garten** `fall`–`ho1` | Haus, Zaun, Baum, Herr Holzapfel mit Hund; Leinenanordnung; Hund läuft frei; Bescheid im Briefkasten; Blase; höherer Zaun; Widerspruch | tabler:`fence`, `sun`, `file-text`; fluent-hc:`deciduous-tree`, `dog`, `paw-prints`, `closed-mailbox-with-raised-flag`; Haus programmatisch | `Fall · Ein Haus mit Garten am Ortsrand` (ab 0,0 s) … `Fall · Der Widerspruch` | Haus · Hund · Leine · frei · Joggerin · Bescheid · Blase · Zaun · Widerspruch | Briefkastenklappe (`szene_246briefkasten_1`) |
| **A2 Gemeinde** `wid`–`sp1` | Herr Sperling am Schreibtisch, Akte, Blase, Vorlage | tabler:`building-community`, `folder`, `arrow-big-right` | `Fall · Der Widerspruch liegt bei der Gemeinde` … | Akte · Abhilfe? · Blase · keine Abhilfe · Vorlage | – |
| **A3 Landratsamt** `lra`–`ko1` | Frau Körner am Schreibtisch, Akte, Tastatur, Blase | tabler:`building`, `folder`, `keyboard` | `Fall · Im Landratsamt`, `Fall · Der Entwurf` | Akte · Tastatur · Blase · Entwurf | Tippen (`szene_246tastatur_1`) |
| **A4 Frage** `frage`–`frage3` | Tafel mit drei Fragen, Körner und Holzapfel | – | `Die Frage · …` | 5 Stufen | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C 1. Vorverfahren** `vv`–`land2` | Wortlautkarte § 68 Abs. 1 (3 Marker), Overlay NRW/Niedersachsen, Fall ✓ | tabler:`scale`, `map-2` | `1. Vorverfahren › …` | 9 Stufen | – |
| **D 2. Wer entscheidet?** `abhilfe`–`ausn` | Wortlautkarten § 72, § 73 Abs. 1; Pillen Ausgangsbehörde/nächsthöhere Behörde; Sperling und Körner | – | `2. Wer entscheidet? › …` | 10 Stufen | – |
| **E 3. Kopf und Tenor** `kopf`–`tenor3` | Briefkopf Stück für Stück, Tenor 1–3 | tabler:`file-text`, `writing`, `currency-euro`, `receipt` | `3. Bescheid › Kopf` … `› Tenor › 3. Gebühr` | 14 Stufen | – |
| **F1 Gründe** `gruende`, `zul` | I. Sachverhalt, II. Zulässigkeit ✓ | tabler:`file-text`, `calendar-event` | `3. Bescheid › Gründe › …` | 10 Stufen | – |
| **F2 Begründetheit** `begr`–`zweck2` | Rechtmäßigkeit (+), Zweckmäßigkeit, Leinenpflicht ✗, Zaun ✗ | tabler:`scale`, `fence`; fluent-hc:`dog` | `… › a) Rechtmäßigkeit`, `… › b) Zweckmäßigkeit …` | 10 Stufen | – |
| **G Kosten** `kosten`–`anwalt` | Zitat § 73 Abs. 3 Satz 3, § 80 VwVfG / Land, Wortlautkarte § 80 Abs. 1 Satz 3 (2 Marker), Anwalt ✓; Holzapfel | tabler:`currency-euro`, `receipt`, `briefcase` | `3. Bescheid › Kosten › …` | 10 Stufen | – |
| **H Belehrung** `belehr`–`sitz` | vier Pillen zum Wort, Muster, Name/Sitz | tabler:`info-circle`; fluent-hc:`classical-building` | `3. Bescheid › Rechtsbehelfsbelehrung › …` | 9 Stufen | – |
| **I Zustellung** `zust`–`frist` | Wortlautkarte § 73 Abs. 3 (5 Marker), Post mit Zustellungsurkunde, Klagefrist ✓; Holzapfel | tabler:`mail`; fluent-hc:`closed-mailbox-with-raised-flag` | `3. Bescheid › Zustellung › …` | 11 Stufen | Briefkastenklappe |
| **J 4. Typische Fehler** `fehler`–`f2` | Zweckmäßigkeit fehlt ✗, falsche Belehrung ✗ | tabler:`alert-triangle`, `calendar-event` | `4. Typische Fehler › …` | 7 Stufen | – |
| **K Klausurtipp** `tipp`–`tipp3` | Lexi warnt: § 79 Abs. 1 Nr. 1, beide Bescheide, Vorbringen würdigen | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 6 Stufen | – |
| **L Schema** `sch`–`s5` | progressiv 1.–5. | – | `Schema › …` | 7 Stufen | – |
| **M Merksatz** `merke`/`m2` | Lexi, 4 Marker | – | `Merksatz` | 6 Stufen | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung nur in A1 (der Hund läuft bei „läuft er frei“ ein Stück); kein Zoom. Kein Richterhammer (Gericht als Säulengebäude).

## Sachverhaltskarte (erscheint vollständig)

> Herr Holzapfel hält einen verspielten Mischling. Die Gemeinde hat angeordnet, den Hund außerhalb des Grundstücks an der Leine zu führen. Danach läuft der Hund dreimal frei durch den Ort; einmal springt er eine Joggerin an, die stürzt. Mit Bescheid vom 2.3.2026, bekannt gegeben am 4.3.2026, untersagt die Gemeinde Herrn Holzapfel die Hundehaltung. / Am 16.3.2026 legt Herr Holzapfel schriftlich Widerspruch ein: Der Hund sei ganz lieb, den Gartenzaun habe er erhöht. Herr Sperling von der Gemeinde hilft nicht ab und legt die Akte dem Landratsamt als nächsthöherer Behörde vor. Das Landesrecht sieht den Widerspruch vor. / Bearbeitervermerk: Die Rechtmäßigkeit der Untersagung ist zu unterstellen. Referendarin Körner entwirft den Widerspruchsbescheid. – Frage: „Wie sieht der Widerspruchsbescheid aus?“ (kein Fiktiv-Hinweis)
