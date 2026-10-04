# Folge 142 · Äste auf dem Garagendach: Beseitigungsanspruch aus § 1004 BGB – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_142.py`](src/skript_142.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Übungsfall nach dem Plan-Hook („Die Äste vom Baum des Nachbarn hängen auf dein Garagendach und verstopfen die Rinne“): Franziska (Nordrhein-Westfalen) hat neben ihrem Haus eine Garage. Der große Ahorn ihrer Nachbarin Rosemarie steht 4 m von der Grenze entfernt; seit dem letzten Sommer ragen seine Äste über das Garagendach, im Herbst verstopft das Laub die Dachrinne. Rosemarie lehnt den Rückschnitt ab: Laub im Herbst sei ganz normal. Respektvoll, ohne Streit; keine Säge, kein Fällen im Bild.

Ablauf: Fall (Grundstücke in Seitenansicht, Gespräch am Gartenzaun) → Frage → Sachverhalt → Wortlautkarte § 1004 Abs. 1 S. 1 und § 903 → vier Prüfungspunkte → 1. Eigentum / 2. Beeinträchtigung → 3. Störerin (Handlungs-/Zustandsstörer, Naturereignis, ordnungsgemäße Bewirtschaftung) → Gegenfall Laub vom Baum selbst (Grenzabstand § 41 NachbG NRW, § 906 Abs. 2 S. 2 analog) → 4. keine Duldungspflicht (§ 910 Abs. 2 statt § 906) → Verjährung und Zwischenergebnis → II. Wortlautkarte § 910 → Verhältnis zu § 1004, Grenzen (Baumschutzsatzung), Kosten → III. Unterlassung → Ergebnis am Gartenzaun mit Fristsetzung → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:07,2 (5.363 Zeichen vertont); Begründung für mehr als fünf Minuten in `ABNAHME.md`.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Franziska (FR), um 35 | Eigentümerin der Garage | `standing/easing-2` (hellblaues offenes Hemd über schwarzem Oberteil, gelbe Hose, weiße Turnschuhe), Kopf `Medium Bangs`, Haut `#E8B48C`; Mimiken `Calm`, `Smile` (redet), `Serious` (bittet, redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `lucy` (Frau, jung) |
| Rosemarie (RO), um 70 | Nachbarin, Eigentümerin des Ahorns | `standing/resting-2` (schwarzes Oberteil, grüne Hose `#8FD694`, schwarze Schuhe), Kopf `Gray Bun`, Haut `#F2CDB0`; Mimiken `Old` (ruhig), `Smile` (redet), `Calm` (meint, redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste und in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folge 141): Franziska, Rosemarie. Kein Genitiv eines Namens im Sprechtext.
- **Stimmen nur aus dem Pool:** `lucy` (jung, Garageneigentümerin) und `hilde` (älter, Nachbarin) – zwei klar unterscheidbare Frauenstimmen; `stephan`/`christian` nicht eingesetzt (keine Männerrolle). Erzählerin/Lexi Carla ohne Rolle. Die Vorfolge 141 nutzte `helmut`, `niklas`, `julia`.
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 139–141 (blazer-3, blazer-4, crossed_arms-1, crossed_arms-2, easing-1, pointing_finger-2, robot_dance-2, robot_dance-3, walking-1); keine Polka Dots, keine Prothesen-Posen, keine Bärte. Präfixe `FR_`/`RO_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Szene A1: Rosemarie links (blickt nach rechts), Franziska rechts (blickt nach links zur Garage); am Gartenzaun ebenso; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `FR_redet`, `FR_bittet`, `RO_redet`, `RO_meint` (je links/rechts) und Lexi. Kein Mensch als Icon.
- Figuren-PNGs: `../peeps/op_142/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 139 (Laden/Eigentumsvorbehalt), 140 (Landstraße mit Kuppe), 141 (Gerichtssaal/Beweislast). Neu: zwei Grundstücke in Seitenansicht mit gestrichelter Grenze, Zaun, Ahorn (Phosphor `tree`), Garage mit Flachdach, Sektionaltor und Dachrinne (einfache Tuscheform wie die Straße in 140), Ast als Tuschelinie mit Ahornblättern; zweite Fallbühne am Gartenzaun, zu der das Ergebnis erkennbar zurückkehrt. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Äste über der Garage** `fall`–`leiter` | Seitenansicht: ab 0,0 s Franziska mit Namensschild, Garage, Pillen „Äste auf dem Garagendach“, „Nordrhein-Westfalen“, „Garage von Franziska“; Ahorn und Rosemarie (`ahorn`), Grenze, Zaun und Maßlinie „4 m“ zum Wort; Ast über die Grenze mit Blättern, Pille „Äste ragen über die Grenze“; Laub in der Rinne, „Laub verstopft die Dachrinne“; Leiter, Franziska besorgt | ph:`tree` (Grün), tabler:`fence` (Holz), `leaf-maple` (Rot/Gelb); ph:`leaf`, `ladder`; Garage/Grenze/Ast programmatisch | `Fall · Äste über der Garage` (ab 0,0 s) | `szene_142laub_1` (Laub), `szene_142leiter_1` (Leiter) |
| **A2 Am Gartenzaun** `fr1`–`frage2` | Ahorn links, Zaun, Garage mit Laub rechts; Blasen Franziska „Rosemarie, kannst du bitte die Äste / über meiner Garage zurückschneiden?“, Rosemarie „Laub im Herbst ist ganz normal. / Das ist hier überall so.“; Frage-Pillen, Astschere zum Wort | ph:`tree`, tabler:`fence`, `scissors`; ph:`leaf` | `Fall · Am Gartenzaun` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 1004** `p1004`–`v4` | Wortlautkarte § 1004 Abs. 1 S. 1 (4 Marker), § 903 S. 1, vier Prüfungspunkte zum Wort | tabler:`leaf-maple`, `list-check`; ph:`house` | `Anspruchsgrundlage · § 1004 Abs. 1 S. 1 BGB` → `§ 1004 BGB › 4 Prüfungspunkte` | – |
| **D1 Eigentum, Beeinträchtigung** `eig`–`beein2` | ✓ Eigentümerin; nicht durch Besitzentziehung (§ 985); Äste und Laub; ✓ Beeinträchtigung | ph:`garage`; tabler:`hand-stop`, `leaf-maple`, `droplet` | `I. › 1. Eigentum` → `I. › 2. Beeinträchtigung` | – |
| **D2 Störerin** `stoer`–`stoer2` | ✗ Handlungsstörerin; Zustandsstörerin; Naturereignis, ordnungsgemäße Bewirtschaftung (V ZR 218/18 Rn. 8 f.); ✗ Äste über die Grenze wachsen lassen (V ZR 102/18 Rn. 9, 12); Block „Rosemarie ist Störerin“ | ph:`tree`, `wind`; tabler:`hand-stop`, `fence`, `leaf-maple` | `I. › 3. Störer` → `› Zustandsstörerin` → `› Naturereignis` | – |
| **D3 Gegenfall** `gegen`–`ausgl` | Laub vom Baum selbst; ✓ Abstand nach § 41 Abs. 1 NachbG NRW („in deinem Land ggf. andere Nummer“); ✗ in aller Regel nicht verantwortlich; ✗ kein Geldausgleich analog § 906 Abs. 2 S. 2 | ph:`wind`; tabler:`ruler-measure`, `coin-euro` | `I. › 3. Störer › Gegenfall: Laub vom Baum` → `Gegenfall › § 906 Abs. 2 S. 2 BGB analog` | – |
| **E Duldungspflicht** `duld`–`lnr` | § 1004 Abs. 2; Rosemaries Satz; ✗ § 906; ✓ allein § 910 Abs. 2 (V ZR 102/18 Rn. 8); objektiv, Beweislast (V ZR 234/19 Rn. 15); ✓ verstopfte Rinne; ✗ Grenzabstand hilft nicht | ph:`scales`; tabler:`leaf-maple`, `fence`, `droplet`, `ruler-measure` | `I. › 4. keine Duldungspflicht, § 1004 Abs. 2 BGB` → `I. › 4. › Überhang: § 910 Abs. 2 BGB` | – |
| **F Verjährung** `verj`, `erg1` | 3 Jahre (§§ 195, 199), ✓ nicht verjährt; Block Zwischenergebnis | tabler:`hourglass`, `scissors` | `I. › Verjährung, §§ 195, 199 BGB` → `I. › Zwischenergebnis` | – |
| **G § 910** `sh`–`w910c` | Wortlautkarte § 910 (5 Marker) | tabler:`scissors`, `calendar-event`, `droplet` | `II. Selbsthilferecht · § 910 BGB` | – |
| **H Verhältnis** `neben`–`kosten` | ✓ nebeneinander (Rn. 5); verjährt nicht; ✗ nicht den Baum fällen; Baumschutzsatzung; Kosten (vgl. V ZR 67/22 Rn. 10) | tabler:`arrows-exchange`, `hourglass-off`, `scissors`, `coin-euro`; ph:`tree` | `II. › Verhältnis zu § 1004 BGB` → `› Grenzen der Selbsthilfe` → `› Kosten der Selbsthilfe` | – |
| **I Unterlassung** `unt`–`wgef` | § 1004 Abs. 1 S. 2; ✓ Wiederholungsgefahr meist indiziert | ph:`tree`; tabler:`hand-stop`, `repeat` | `III. Unterlassungsanspruch · § 1004 Abs. 1 S. 2 BGB` | – |
| **J Ergebnis** `erg`–`schnitt` | zurück am Gartenzaun: Pille „Äste zurückschneiden: § 1004 BGB“, Kalender „Frist“ → „Frist: 4 Wochen“; Blasen Franziska „Bitte schneide die Äste in den / nächsten 4 Wochen zurück.“, Rosemarie „Gut, ich kümmere / mich darum.“; Astschere, „Sonst: nach Fristablauf selbst abschneiden“, „§ 910 BGB“ | tabler:`calendar-event`, `scissors`, `fence`; ph:`tree` | `Ergebnis · § 1004 Abs. 1 S. 1 BGB` → `Ergebnis › Fristsetzung, § 910 Abs. 1 S. 2 BGB` | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Duldung beim Überhang` | – |
| **L Klausurschema** `sch`–`k3b` | breite Karte, I.–III. mit Untermerkmalen, Zeile für Zeile | – | `Klausurschema` → `› II. Selbsthilferecht` → `› III. Unterlassung` | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung außer Einblendungen.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („4 Wochen“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Franziska wohnt in Nordrhein-Westfalen und hat neben ihrem Haus eine Garage. Im Garten ihrer Nachbarin Rosemarie steht ein großer Ahorn, 4 m von der Grenze entfernt.
>
> Seit dem letzten Sommer ragen seine Äste über die Grenze auf das Garagendach. Im Herbst fällt das Laub in die Dachrinne und verstopft sie; Franziska muss immer wieder auf die Leiter.
>
> Franziska bittet Rosemarie, die Äste zurückzuschneiden. Rosemarie lehnt ab: Laub im Herbst sei ganz normal, das sei hier überall so.
>
> **Kann Franziska den Rückschnitt verlangen oder selbst schneiden?**
