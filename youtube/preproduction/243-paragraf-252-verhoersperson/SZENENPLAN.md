# Folge 243 · § 252 StPO: Die Ehefrau schweigt – Verhörsperson als Zeuge? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_243.py`](src/skript_243.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Strafrecht/StPO, Format „Streitstand“. Fall nach dem Plan-Hook: Frau Hasselbach belastet ihren Mann bei der Polizei schwer (Betrug im gemeinsamen Malerbetrieb: Rechnungen für Arbeiten, die nie gemacht wurden) und verweigert in der Hauptverhandlung das Zeugnis; das Gericht hört den Polizeibeamten, Herr Hasselbach wird verurteilt, die Verteidigerin legt Revision ein. Delikt neutral, keine häusliche Gewalt, keine Beziehungskonflikte. Ablauf: Fall (Malerbetrieb → Polizei → Hauptverhandlung → Polizeibeamter als Zeuge, Urteil → Revision) → drei Fragen → Sachverhalt → § 252 (Wortlaut) → Rechtsprechung → Streitstand → Ausnahme Richter → Ausnahme Gestattung → Äußerungen außerhalb einer Vernehmung → Lösung → Revisionsrüge (§ 344 Abs. 2 S. 2, Wortlaut) → Vortrag und Beruhen → Klausurtipp (Lexi) → Merksatz (Lexi). Verweise: 224 und 221 (Grundlagen), 072 (Verfahrensrüge).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Hasselbach (FH), um 45 | Ehefrau, Zeugin, Buchhaltung | `standing/blazer-3`, Blazer Petrol `#2E8B84`, schwarzes Oberteil der Pose, Hose Grau `#6B6F80`; Kopf `Long`, Haut `#E8BB98`; Mimiken `Calm`, `Serious` (redet), `Concerned|Serious`, `Suspicious`, `Smile`, `Solemn` | `sabrina` (Frau, mittel) |
| Herr Hasselbach (HH), um 45 | Ehemann, Malermeister, Angeklagter, spricht nicht | `standing/walking-2`, schwarzes Oberteil der Pose, Hose Khaki `#C9A46A`; Kopf `Short 1`, Haut `#F2D0B5`, ohne Bart; gewöhnlicher Mann ohne Täterklischee | – |
| Polizeibeamter (PB), um 40 | Vernehmungsbeamter, später Zeuge | `standing/blazer-2`, Jacke Dunkelblau `#2F4B7C` ohne Abzeichen, Oberteil Hellblau, schwarze Hose; Kopf `Short 2`, Haut `#C68E6A`; Unterschenkelprothese der Pose (keine Täterrolle) | `marc` (Mann, mittel) |
| Vorsitzender (VR), um 60 | Vorsitzender Richter, belehrt | `standing/pointing_finger-1` (schwarz wie eine Robe, erhobener Zeigefinger), Kopf `No Hair 2`, Brille `Glasses 2` | `william` (Mann, älter) |
| Verteidigerin (VT), um 40 | erhebt die Verfahrensrüge | `standing/walking-3` (schwarz wie eine Robe), Kopf `Medium Bangs 3`, Haut `#B07552` | `laura_ruhig` (Frau, mittel) |
| Ermittlungsrichterin (EJ), um 55 | Gegenbeispiel richterliche Vernehmung, spricht nicht | `standing/robot_dance-2`, Oberteil Schwarz, Hose `#3A3A44`; Kopf `Medium 3`, Brille `Glasses 4` | – |
| Freundin (FR), um 45 | hypothetischer Gegenfall, spricht nicht | `standing/shirt-1`, Hemd Terrakotta `#E58E5A`, schwarze kurze Hose der Pose, Unterschenkelprothese der Pose; Kopf `Bangs` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig), alle vier eingesetzt; Erzählerin und Lexi Carla.
- **Blickrichtung:** Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Fallszenen: Vernehmungs- und Gerichtspersonen links (`_r`) mit Blick nach rechts, Zeugin/Zeuge und Angeklagter rechts mit Blick nach links. Tafelfolien: Figuren nach links zur Tafel; in Szene M blickt Frau Hasselbach (`_r`) zur Freundin.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `FH_redet`, `PB_redet`, `VR_redet`, `VT_redet` (je links/rechts) und Lexi. Keine Bärte. 96 Figuren-PNGs in `../peeps/op_243/` (Drive-Master).
- **Name** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste, per Volltextsuche über `youtube/` (Text- und Codedateien) nur als verworfener Kandidat in 223 erwähnt, nie vergeben; in `namen_reserviert.txt` eingetragen: **Hasselbach** (Ehepaar). Übrige Figuren Funktionsrollen. Kein Genitiv des Namens im Sprechtext.

**Abweichung von den letzten Folgen:** 240 (`easing-1`, `walking-1`, `shirt-3`), 241 (`easing-2`, `crossed_arms-2`, `blazer-4`), 242 (parallel, nicht eingesehen) und das Schwesterthema 224 (`easing-2`, `resting-2`, `walking-1`, `blazer-1`, `robot_dance-3`, `pointing_finger-2`) – in 243 keine dieser Posen, keine Polka Dots. Neue Kleidung: Petrol-Blazer, Khaki, Terrakotta. Schauplätze **Malerbetrieb mit Buchhaltungstisch und Farbeimer**, **Polizei mit Tastatur**, **Hauptverhandlung mit Vorsitzendem**, **Hauptverhandlung mit dem Polizeibeamten als Zeugen**, **Kanzlei der Verteidigerin** – neu gegenüber 224 (Wohnung mit Laptop, Wohngemeinschaft) und 240/241. Die Gerichtsszene kehrt bewusst als Ort der Handlung wieder (zwei Halte derselben Hauptverhandlung). Cremegrund durchgehend.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Malerbetrieb** `fall`→`vorwurf` | Herr Hasselbach mit Farbeimer, Frau Hasselbach, Tisch mit Rechner bei „Buchhaltung“; Pillen „gemeinsamer Malerbetrieb“, „Buchhaltung“, „Ermittlungen wegen Betrugs“, „Arbeiten berechnet, die nie gemacht wurden“ mit Kreuz | tabler:`bucket-droplet`, `heart-handshake`, `calculator`, `file-invoice` | `Fall · Malerbetrieb Hasselbach` (ab 0,0 s) → `· Sie macht die Buchhaltung` → `· Ermittlungen wegen Betrugs` → `· Vorwurf: Arbeiten berechnet, nie gemacht` | – |
| **B Polizei** `pol`→`w0` | Polizeibeamter hinter dem Schreibtisch, Notizbuch, dann Tastatur; Haken „Belehrung“; Blase Polizeibeamter; Pille „Sie belastet ihn schwer.“; Blase Frau Hasselbach | tabler:`notebook`, `keyboard` | `Fall · Zeugenvernehmung bei der Polizei` → `· Belehrung` → `· Sie belastet ihn schwer` | Tastatur (`szene_243tastatur_1`) |
| **C Hauptverhandlung** `hv`→`w1` | Vorsitzender hinter dem Richtertisch, Frau Hasselbach (Pille „Zeugin“), Herr Hasselbach („Angeklagter“); zwei Blasen | tabler:`scale` | `Fall · Hauptverhandlung gegen Herrn Hasselbach` → `· Belehrung durch den Vorsitzenden` → `· Sie verweigert das Zeugnis` | – |
| **D Zeuge Polizeibeamter** `verh`→`urteil` | gleicher Saal; Polizeibeamter an der Stelle der Zeugin („Zeuge“), Blase; Pille „verurteilt“ | tabler:`scale` | `Fall · Der Polizeibeamte als Zeuge` → `· Bericht über ihre frühere Aussage` → `· Verurteilung` | – |
| **E Kanzlei** `rev` | Verteidigerin mit Revisionsschrift in der Hand, Herr Hasselbach; Pille „Revision“ | tabler:`file-text` | `Fall · Revision` | Papier (`szene_243papier_1`) |
| **F Die Fragen** `fragen`→`frage3` | drei Karten: Verhörsperson (Polizeibeamter), Richter (Ermittlungsrichterin), Revision (Verteidigerin) | – | `Fall · Durfte der Polizeibeamte berichten?` → `· Was wäre bei einem Richter anders?` → `· Wie rügt man das?` | – |
| **G Sachverhalt** `sv` | Karte vollständig, Hinweis zum Anhalten | – | `Sachverhalt` | – |
| **H § 252 Wortlaut** `a252`→`verw` | Ehefrau § 52 Abs. 1 Nr. 2; **Wortlautkarte § 252** (Marker „erst in der Hauptverhandlung“, „darf nicht verlesen werden“); Kreuz „Polizeibeamter als Zeuge? Steht dort nicht.“; Verweisblock 224/221 | tabler:`heart-handshake`, `file-text`, `help-circle`, `player-play` | `§ 52 Abs. 1 Nr. 2 StPO › Ehefrau darf schweigen` → `§ 252 StPO › frühere Aussage` → `› nicht verlesen` → `› Verhörsperson nicht erwähnt` → `› Grundlagen: Folgen 224, 221` | – |
| **I Rechtsprechung** `rspr`→`zweck` | Verlesungs- und Verwertungsverbot (GSSt 1/16 Rn. 32); nicht auf anderem Weg; Kreuz Verhörsperson (3 StR 377/18 Rn. 12); Block Zweck (1 StR 222/23 Rn. 7) | tabler:`file-off`, `microphone-off`, `scale` | `Rspr. zu § 252 StPO › Verwertungsverbot` → `› auch nicht auf anderem Weg` → `› Verhörsperson gesperrt` → `› Zweck` | – |
| **J Streitstand** `ga1`→`praxis` | 1. Wortlaut-Ansicht, 2. umfassendes Verbot (GSSt Rn. 29, 36), Block Großer Senat offen (Rn. 26, 64), Haken 3. BGH: Sperre bleibt | tabler:`book`, `ban`, `help-circle`, `scale` | `Streit: Verhörsperson als Zeuge? › Wortlaut-Ansicht` → `› umfassendes Verbot` → `› Großer Senat: offen` → `› BGH: Sperre bleibt` | – |
| **K Ausnahme Richter** `richter`→`vorhalt` | Haken „Er darf als Zeuge gehört werden“ (Leitsatz, Rn. 32), Haken „keine weitergehende Belehrung“ (Rn. 53), Grund (Rn. 33, 63), Block „Erinnerung des Richters“, „Protokoll: nur Vorhalt“ (3 StR 108/12) | tabler:`gavel`, `info-circle`, `scale`, `file-text` | `Ausnahme 1: Richter › hat belehrt` → `› darf als Zeuge gehört werden` → `› keine weitergehende Belehrung` → `› Grund` → `› Erinnerung, Protokoll nur Vorhalt` | – |
| **L Gestattung** `gest`→`teil` | ausdrückliche Erlaubnis; Haken Polizeibeamter darf berichten; Block qualifizierte Belehrung, Protokoll (2 StR 112/12); Kreuz kein Teilverzicht (1 StR 222/23) | tabler:`signature`, `messages`, `info-circle`, `ban` | `Ausnahme 2: Gestattung › ausdrücklich erlaubt` → `› Polizeibeamter darf berichten` → `› qualifizierte Belehrung` → `› nicht teilbar` | – |
| **M Außerhalb einer Vernehmung** `spont`, `spont2` | Haken „nicht gesperrt“ (1 StR 137/12 Rn. 12); hypothetische Freundin erscheint | tabler:`message-circle`, `messages` | `Außerhalb einer Vernehmung › nicht gesperrt` → `› Gespräch mit einer Freundin` | – |
| **N Lösung** `l1`→`l1c` | Haken Ehefrau, erst in der HV, polizeiliche Vernehmung; Kreuz Gestattung; roter Block „durfte nicht … gehört werden“ | tabler:`heart-handshake`, `notebook`, `microphone-off` | `Lösung › der Polizeibeamte als Zeuge` → `› Ehefrau, erst in der HV geschwiegen` → `› polizeiliche Aussage, keine Gestattung` → `› Polizeibeamter durfte nicht aussagen` | – |
| **O Revisionsrüge** `v1`→`l2c` | Blase Verteidigerin; **Wortlautkarte § 344 Abs. 2 S. 2** (Marker „den Mangel enthaltenden Tatsachen“); Tatsachenliste Punkt für Punkt | tabler:`file-text`, `list-check` | `Revision › Rüge der Verteidigerin` → `› Verfahrensrüge` → `› § 344 Abs. 2 S. 2 StPO` → `› Tatsachen vortragen` | – |
| **P Vortrag und Beruhen** `l2d`→`verw072` | Haken kein Negativvortrag (2 StR 112/12), Haken kein Widerspruch (3 StR 108/12), Block Beruhen, „Die Rüge hat Erfolg.“, Verweis 072 | tabler:`file-description`, `message-off`, `circle-check`, `player-play` | `Revision › Gestattung: kein Vortrag nötig` → `› kein Widerspruch nötig` → `› Beruhen, § 337 StPO` → `› siehe Folge 072` | – |
| **Q Klausurtipp** `tipp`→`s4` | hellgelbe Tafel, Warnsymbol, I.–IV. progressiv; Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · § 252 in vier Schritten` → `· I. …` → `· II. …` → `· III. Ausnahme?` → `· IV. Revision: Rüge und Beruhen` | – |
| **R Merksatz** `merke`, `mz` | Lexi erklärt, zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (Assertion gegen Rückfall auf Stil E). **Zahlen** auf Blasen, Tafeln und Pillen als Ziffern; Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tische als Baustein (`karte`). Kein Mensch als Icon.

## Sachverhaltskarte (Szene G, erscheint vollständig)

> Herr und Frau Hasselbach sind verheiratet und führen zusammen einen Malerbetrieb; sie macht die Buchhaltung. Gegen ihn wird wegen Betrugs ermittelt: Er soll Kunden Arbeiten berechnet haben, die nie gemacht wurden.
>
> Ein Polizeibeamter vernimmt Frau Hasselbach als Zeugin und belehrt sie über ihr Zeugnisverweigerungsrecht. Sie belastet ihren Mann schwer: Die falschen Rechnungen habe er selbst geschrieben.
>
> In der Hauptverhandlung verweigert sie nach Belehrung das Zeugnis; einer Verwertung ihrer früheren Aussage stimmt sie nicht zu. Das Gericht vernimmt den Polizeibeamten über ihre Aussage und verurteilt Herrn Hasselbach. Die Verteidigerin legt Revision ein.
>
> **Durfte der Polizeibeamte über ihre Aussage berichten?**
