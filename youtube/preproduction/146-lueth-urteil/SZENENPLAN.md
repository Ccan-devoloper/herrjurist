# Folge 146 · Lüth-Urteil: Mittelbare Drittwirkung der Grundrechte erklärt – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_146.py`](src/skript_146.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Klassiker-Fall · Grundrechte. Ablauf: moderner Einstieg (Wenkes Filmblog, Unterlassungsklage) → Frage „Gelten Grundrechte zwischen Privaten?“ → der echte Fall sachlich (Hamburg 1950, LG Hamburg 1951, Verfassungsbeschwerde) → Sachverhalt → I. Grundrechte im Privatrecht (Abwehrrechte, objektive Wertordnung, Medium des Privatrechts, Generalklauseln als Einbruchstellen, mittelbare Drittwirkung, Wortlautkarte Art. 1 Abs. 3 GG, Bindung des Zivilrichters, Kontrast Fraport) → II. Meinungsfreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 1, Abs. 2 GG, Wirkung, § 826 BGB als allgemeines Gesetz, Wechselwirkung, Güterabwägung, Vermutung für die freie Rede) → III. Abwägung im Fall Lüth → IV. Prüfungsmaßstab (keine Superrevision, Ausstrahlungswirkung) → Ergebnis → zurück zu Wenke → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:30,9 (5.778 vertonte Zeichen).

**Sensibilität (Vorgabe Koordinator):** Erich Lüth und Veit Harlan treten nicht als Figuren auf. Keine NS-Symbole, keine Filmbilder, keine Plakate; der Film „Jud Süß“ wird nur sachlich benannt, nichts daraus gezeigt oder zitiert. Die Hamburg-Szene zeigt nur neutrale Icons (Rednerpult, Mikrofon, Zeitung, Filmrolle), das Landgericht nur als Tafel mit Gerichts-/Hammer-Icon. Im echten Fall stehen keine Figuren im Bild.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Wenke (WE), um 30 | fiktive Filmbloggerin, ruft zum Nichtbesuch eines Films auf | `standing/resting-1` (Pullover Grün `#8FD694`, schwarze Hose), Kopf `Medium Bangs 3`, Haut `#F1C6A5`, ohne Brille. Mimiken `Smile` (ruhig), `Serious` (redet), `Suspicious` (denkt), `Cute` (froh), `Concerned\|Serious` (Sorge) | `lucy` (Frau, jung) |
| Herr Gerstner (GE), um 55 | fiktiver Filmproduzent, klagt auf Unterlassung; sachlich, kein Bösewicht | `standing/crossed_arms-1` (Pullover Lila `#B8A9F5`), Kopf `Gray Short` (Haar `#B5B5B5`), Brille `Glasses 4`, Haut `#E0AC84`, ohne Bart. Mimiken wie Wenke | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Wenke blickt erst zum Laptop (links), ab Gerstners Auftritt zu ihm (`_r`); Gerstner blickt zu ihr (links). H: Wenke spricht zu Gerstner (`_r`). Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_146.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WE_redet`, `GE_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): stephan und lucy; christian nicht verwendet (keine Dialogpaarung stephan/christian). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Wenke, Gerstner – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Szenenplan/Skript/Abnahmebogen unter `youtube/preproduction` (Volltextsuche 04.10.2026; „Henrike“ wegen 106/127 verworfen). Gesprochen werden zusätzlich die realen Namen Lüth und Harlan (Namensprüfung).
- Figuren-PNGs: `../peeps/op_146/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 142 (`easing-2`, `resting-2`), 143 (`shirt-4`, `easing-2`), 144 (`walking-2`, `shirt-3`) – hier `resting-1` und `crossed_arms-1`; keine Polka Dots, keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` verworfen), keine Bärte. `pointing_finger-1` verworfen, weil die Kleidung dort nicht einfärbbar ist (schwarze Silhouette). Schauplätze **Wohnzimmer mit Schreibtisch und Laptop** (Filmblog) und **Hamburger Rednerpult/Zeitung/Kino als Stationen** – neu gegenüber 142–144 (Kontaktbögen und Figurenrezepte verglichen). Der Blog-Schauplatz kehrt in H wieder, weil die Geschichte zum Einstiegsfall zurückkehrt.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Wenkes Filmblog** `fall`→`g1` | Schreibtisch mit Laptop, Blogkarte „Wenkes Filmblog“; Wenke redet (Blase), Herr Gerstner kommt von rechts, redet (Blase) | tabler `device-laptop`, `movie`, `car`; Pillen „Schaut ihn euch nicht an!“, „Produzent: Sorge um den Kinostart“, „Klage auf Unterlassung“ | `Fall · Wenkes Filmblog` (ab 0,0 s) → `Fall · Die Unterlassungsklage` | 10 | Schritte (`szene_146schritte_1`, Freesound CC0 707248) beim Hereinkommen |
| **A2 Die Frage** `frage0`, `klassiker` | Tafel „Zwei Private streiten“, beide Figuren | tabler `building-bank`, `scale` | `Die Frage · Grundrechte zwischen Privaten?` → `· Das Lüth-Urteil` | 4 | – |
| **B1 Hamburg 1950** `lueth`→`film` | drei Stationen ohne Figuren: Rednerpult/Mikrofon, Zeitung (offener Brief), Filmrolle; Pillen zum Wort | tabler `podium`, `microphone-2`, `news`, `movie` | `Der echte Fall · Hamburg, 20.9.1950` → `· Der Boykottaufruf` | 10 | – |
| **B2 LG Hamburg** `klage`→`frage` | Tafel, Requisit rechts (ohne Figuren) | tabler `file-text`, `gavel`, `book`, `building-bank`, `message` | `Der echte Fall · LG Hamburg, 22.11.1951` → `· Verfassungsbeschwerde` → `· Die Frage` | 8 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D1 Abwehr und Wertordnung** `urteil`→`buerg` | Tafel, beide Figuren | tabler `building-bank`, `shield-check`, `scale`, `book` | `I. Grundrechte im Privatrecht · BVerfG, 15.1.1958` → `› Abwehrrechte …` → `› objektive Wertordnung` → `› auch im bürgerlichen Recht` | 6 | – |
| **D2 Durch das Privatrecht** `medium`→`mittelbar` | Schaubild Grundrechte → Vorschriften des Privatrechts, Block Generalklauseln, Pille „mittelbare Drittwirkung“ | tabler `book`, `door-enter`, `users-group` | `… › durch das Privatrecht` → `› Einbruchstellen: Generalklauseln` → `› mittelbare Drittwirkung` | 7 | – |
| **D3 Art. 1 III** `a13`→`verkennt` | **Wortlautkarte Art. 1 Abs. 3 GG**, Herr Gerstner | tabler `book`, `gavel`, `alert-triangle` | `… › Art. 1 Abs. 3 GG` → `› gebunden: der Zivilrichter` → `› Verkennen verletzt das Grundrecht` | 6 | – |
| **D4 Kontrast Fraport** `kontrast`, `privatmann` | Tafel mit zwei Blöcken | tabler `building-airport`, `user` | `… › Kontrast: Fraport-Fall` → `› Lüth sprach als Privatmann` | 2 | – |
| **E1 Art. 5** `a5`→`allg` | **Wortlautkarte Art. 5 Abs. 1 Satz 1, Abs. 2 GG**, Wenke | tabler `message`, `fence`, `speakerphone`, `book` | `II. Meinungsfreiheit · Art. 5 Abs. 1 Satz 1 GG` → `› Schranke …` → `› auch die Wirkung geschützt` → `› § 826 BGB: allgemeines Gesetz` | 9 | – |
| **E2 Wechselwirkung** `g2`→`ww` | Schaubild Art. 5 ↔ § 826 mit zwei Pfeilen; Gerstner redet (Blase) | – | `… › Schützt § 826 BGB das Geschäft?` → `› Wechselwirkung` | 7 | – |
| **E3 Güterabwägung** `abw`, `verm` | Tafel, Zitatkarte <212>, grüner Block | tabler `scale`, `message` | `› Güterabwägung` → `› Vermutung für die freie Rede` | 4 | – |
| **F Abwägung im Fall Lüth** `motiv`→`erwidern` | Tafel mit vier Haken | tabler `coins`, `world`, `hand-stop`, `messages` | `III. Abwägung im Fall Lüth › Motive` → `› Ziel` → `› Mittel` → `› Gegenrede` | 6 | – |
| **G1 Prüfungsmaßstab** `pruef`→`ausstr` | Tafel, Gerstner | tabler `search`, `ban`, `sun` | `IV. Prüfungsmaßstab des BVerfG` → `› keine Superrevisionsinstanz` → `› Ausstrahlungswirkung` | 6 | – |
| **G2 Ergebnis** `erg`→`zurueck` | Tafel | tabler `circle-check`, `arrow-back-up` | `Ergebnis · …` (3 Stände) | 4 | – |
| **H Zurück zum Fall** `w2`→`h4` | Schauplatz A1; Wenke redet (Blase), Prüfliste mit Haken auf der Blogkarte, Gerstner | tabler `device-laptop`, `messages` | `Zurück zum Fall · Wenke` → `· Abwägung` → `· Gegenrede` | 7 | – |
| **I Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | 6 | – |
| **J Prüfschema** `sch`→`k6` | breite Karte, 8 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | 9 | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 4 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („20.9.1950“, „§ 826“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Herr Gerstner kommt von rechts (1,0 s).
**Geräusch:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Schreibtisch aus Grundformen (`tisch()` in `folien_146.py`).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Hamburg, 20. September 1950: Senatsdirektor Erich Lüth spricht als Vorsitzender des Hamburger Presseklubs vor Filmverleihern und Filmproduzenten gegen das Wiederauftreten des Regisseurs Veit Harlan, der den antisemitischen Film „Jud Süß“ gedreht hatte. In einem offenen Brief ruft er dazu auf, sich gegen Harlan auch zum Boykott bereitzuhalten. Harlans neuer Film heißt „Unsterbliche Geliebte“.
>
> Auf die Klage der Produktionsfirma und der Verleiherin verurteilt das Landgericht Hamburg Lüth am 22. November 1951 zur Unterlassung: Er darf Kinobesitzer und Verleiher nicht auffordern, den Film nicht zu zeigen, und das Publikum nicht, ihn nicht zu besuchen. Der Boykottaufruf sei sittenwidrig nach § 826 BGB. Lüth erhebt Verfassungsbeschwerde.
>
> **Verletzt das Urteil Lüths Meinungsfreiheit aus Art. 5 Abs. 1 Satz 1 GG?**

Kein Fiktiv-Hinweis; die Quelle des echten Falls (BVerfG, Datum, Az.) steht auf den Tafeln.
