# Folge 203 · Einverständliche Fremdgefährdung: Beifahrer beim Straßenrennen – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_203.py`](src/skript_203.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Format „Abgrenzung“. Aufbau nach Auftrag: Hook mit Zahlen als Ziffern (Samstag, 1:10 Uhr; 100 km/h erlaubt, fast 190 km/h) → Frage → Sachverhalt → echter Fall (BGHSt 53, 55, nur Icons) → § 222 (Wortlautkarte), Tatbestand unproblematisch → Zurechnung: eigenverantwortliche Selbstgefährdung (Verweis Folge 058) oder einverständliche Fremdgefährdung, Kriterium Tatherrschaft über die gefährdende Handlung (BGH Rn. 21–23) → im Fall Fremdgefährdung (Rn. 24) → Gegenansicht in einem Satz (Roxin, Rn. 25) → Einwilligung, § 228 (Wortlautkarte), Grenze konkrete Todesgefahr (Rn. 28 f.; Verweis Folge 157, gleicher Wortlaut wie dort), § 315c anders → Ergebnis → § 315d (Wortlautkarte, Auszug, seit 13.10.2017, im echten Fall nicht anwendbar, Abs. 5) in einem Satz → Klausurtipp mit Lexi (Prüfungsreihenfolge Schritt für Schritt) → Merksatz (Lexi). Vorlagen: 058 (Selbstgefährdung, nur Verweis), 157 (§ 228, nur Verweis), 198 (Hilfsfunktionen, Renderer), 015 (Namens- und Sichtprüfung), Katzenkönig (Tafel-/Figurenstil).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hilmar (HI), Anfang 50 | Fahrer | `standing/crossed_arms-1` (Pullover Orange `#F9A66C`, schwarze Hose der Pose), Kopf `No Hair 3` (Haarkranz Grau `#B5B5B5`), Haut `#EDC3A0`. Mimiken `Calm`, `Driven` (entschlossen; redet), `Serious`, `Solemn` (nach dem Unfall), `Suspicious` | `helmut` (Mann, älter) |
| Eike (EI), um 25 | Beifahrer, feuert an | `standing/pointing_finger-2` (schwarzes Oberteil der Pose, Hose Blau `#8DB3F2`), Kopf `Short 2`, Haut `#B9805A`. Mimiken `Calm`, `Smile`, `Smile Big|Smile` (begeistert; redet), `Suspicious`, `Serious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Parkplatz: Hilmar (`_r`) und Eike blicken einander an, Eikes Zeigefinger zeigt auf Hilmar („Los, Hilmar, gib Gas!“); Tafelfolien: beide zur Tafel; Lexi zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HI_redet`, `EI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. 46 Figuren-PNGs in `../peeps/op_203/` (Drive-Master).
- **Klischeeprüfung:** Fahrer gewöhnlich gekleidet, älter (kein „junger Raser“-Klischee), keine Rennkleidung, keine „fiese“ Mimik; keine Zuordnung von Herkunft oder Hautfarbe zur Täterrolle (der Fahrer hat den hellen Hautton).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rliw` in keinem Text unter `youtube/` (06.10.2026): Hilmar, Eike. Verworfen: Gerold (in 160 wegen Lesart „Gerald“ verworfen), Hannes (104, 107, 196), Jannik (010), Lasse (096), Timo (007, 010, 026). Im Sprechtext nie im Genitiv.
- **Stimmen** nur aus dem zugeteilten Pool (helmut, niklas; ela_froh und julia nicht verwendet: ela_froh nicht für ernste Rollen, julia möglichst meiden). Vorfolge 198 hatte dasselbe Paar (Pool-Vorgabe des Koordinators).

**Abweichung von den letzten Folgen (198 Büro/Esszimmer, 199 Tankstelle, 200 Baugebiet):** neue Schauplätze nächtlicher Parkplatz am Stadtrand (Laterne mit Lichtkegel, Parkschild, zwei Wagen) und Landstraße bei Nacht (Fahrbahnränder, Mittellinie, Tannen, Kurvenschild). Gegenüber Folge 001 (Raser-Fall: Innenstadt, Häuser, Ampeln, Tabler-`car`, `car-crash`) bewusst anders: kein Stadtbild, keine Ampeln, Wagen als Phosphor `car-profile`, kein Unfallbild. Posen `crossed_arms-1` und `pointing_finger-2` in 198–200 nicht verwendet (dort `easing-1/-2`, `resting-1/-2`, `pointing_finger-1`, `shirt-3`, `walking-1/-2`); kein Polka-Dots-Muster; Farben Orange/Schwarz-Blau neu gegenüber 198 (Lila/Türkis).
**Nacht (begründet):** Der Hook verlangt ein nächtliches Rennen; Nachtverlauf (Renderer `hintergrund("nacht")`, wie Folge 001) nur in den Fallszenen A1/A2, Prüfpfad dort weiß (Deckkraft 170). Alle übrigen Folien Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Parkplatz** (Nacht) `fall`→`h1` | ab 0,0 s Laterne mit Lichtkegel, Parkschild, roter Wagen, Mond, Pillen „Samstag, 1:10 Uhr“, „leerer Parkplatz am Stadtrand“; Hilmar tritt auf (Tacho über dem Wagen), Eike tritt auf, zweiter (blauer) Wagen, „Rennen gegen einen 2. Wagen“, „beide nüchtern, kennen die Gefahr“ (Warnsymbol); Blase Eike „Los, Hilmar, gib Gas! Den hängen wir ab!“, Blase Hilmar „Halt dich fest!“ | ph:`car-profile`, `speedometer`; tabler:`parking`; fluent-hc:`warning`; Laterne/Lichtkegel/Mond als Bausteine (`ostil`) | `Fall · Samstag, 1:10 Uhr: ein Parkplatz am Stadtrand` (ab 0,0 s) → … → `Fall · Hilmar: „Halt dich fest!“` | – |
| **A2 Landstraße** (Nacht) `start`→`frage2` | Fahrbahn, Tannen; beide Wagen fahren nebeneinander los (Bewegung), weiter nach rechts; „erlaubt: 100 km/h“, „Hilmar: fast 190 km/h“, „Eike feuert ihn weiter an“; Kurvenschild, „Kurve: Hilmar verliert die Kontrolle“; bei „ab“ verschwinden die Wagen, Warndreieck, „Wagen kommt von der Straße ab“; Blaulicht, „Eike stirbt an der Unfallstelle“, „Hilmar überlebt verletzt“; „Fahrlässige Tötung durch Hilmar?“, „Oder: Selbstgefährdung von Eike?“ | ph:`car-profile`; fluent-hc:`evergreen-tree`, `warning`, `police-car-light`; tabler:`road-sign` | `Fall · Das Rennen auf der Landstraße` → … → `Fall · Oder: Selbstgefährdung von Eike?` | Motor (`szene_203motor_1`) beim Start |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | – |
| **C Der echte Fall** `bgh`→`bgh4` | Tafel BGHSt 53, 55; rechts nur Icons: Gericht, zwei Wagen, Kamera, Warnsymbol, Waage (keine Figuren für reale Beteiligte) | fluent-hc:`classical-building`, `video-camera`, `warning`, `balance-scale`; ph:`car-profile` | `Der echte Fall · BGHSt 53, 55 › …` | – |
| **D § 222** `p222`→`unpro` | Wortlautkarte, Haken Erfolg/Kausalität/Sorgfaltspflicht/Vorhersehbarkeit, „bis hierhin unproblematisch“; Hilmar | fluent-hc:`balance-scale`; ph:`speedometer` | `A. Hilmar: § 222 StGB › …` | – |
| **E1 Zurechnung** `problem`→`fremd` | Selbst- oder Fremdgefährdung; Blöcke; Verweis Folge 058; beide Figuren | fluent-hc:`white-question-mark` | `A. Hilmar › Zurechnung …` | – |
| **E2 Tatherrschaft** `krit`→`unmittel` | Kriterium, auch bei Fahrlässigkeit, unmittelbares Geschehen | fluent-hc:`crown`; ph:`steering-wheel` | `A. Hilmar › Zurechnung › Abgrenzung: Tatherrschaft` → … | – |
| **F1 Im Fall** `hier`→`fg` | am Steuer, Geschwindigkeit/Lenkung, Eike nur ausgesetzt, Anfeuern untergeordnet, Ergebnis Fremdgefährdung | ph:`steering-wheel`, `seat`; fluent-hc:`crown`, `balance-scale` | `A. Hilmar › Zurechnung › im Fall: …` | – |
| **F2 Gegenansicht** `roxin` | ein Satz: Gleichstellung (etwa Roxin), BGH dagegen | fluent-hc:`balance-scale`; ph:`steering-wheel` | `… › Gegenansicht: Gleichstellung?` | – |
| **G1 Einwilligung** `einw`, `p228` | Pillen, Wortlautkarte § 228 mit Markern | fluent-hc:`handshake`, `balance-scale` | `A. Hilmar › Rechtswidrigkeit: Einwilligung …` | – |
| **G2 Grenze** `indiv`→`allg` | Rechtsgüter des Einzelnen, Grenze konkrete Todesgefahr, Verweis Folge 157, § 315c anders; Hilmar | fluent-hc:`handshake`, `warning`, `vertical-traffic-light` | `… › Einwilligung bei § 222 …` | – |
| **G3 Ergebnis** `erg`→`erg3` | konkrete Todesgefahr, Einwilligung (−), Schuld (+), § 222 | ph:`speedometer`; fluent-hc:`handshake`, `balance-scale` | `Ergebnis · …` | – |
| **H § 315d** `p315d`, `abs5` | Pillen „in Kraft seit 13.10.2017“, „im echten Fall noch nicht anwendbar“, Wortlautkarte (Auszug) mit Markern | ph:`car-profile`; fluent-hc:`balance-scale` | `Ausblick · § 315d StGB …` | – |
| **I Klausurtipp** `tipp`→`k5` | hellgelbe Tafel, Lexi warnt; I. Tatbestand – Zurechnung – II. Rechtswidrigkeit – III. Schuld – § 315d, Punkt für Punkt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | – |
| **J Merksatz** `merke`, `mk2` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien (14 Blenden); innerhalb harte Schnitte und Pops; einzige Bewegung: die Wagen im Rennen (A2).
**Gewalt zurückhaltend:** kein Aufprall, kein Wrack, kein Blut, keine Verletzten oder Toten im Bild; Unfall nur über Kurvenschild, Warndreieck und Blaulicht. Keine echten Automarken, kein Rennwagen-Icon, keine Zielflagge.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 222 (vorgelesen bis „verursacht“), § 228 (vollständig vorgelesen), § 315d Abs. 1 Nr. 2, Abs. 5 als gekennzeichneter Auszug, wörtlich nach gesetze-im-internet.de.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstag, 1:10 Uhr: Hilmar (Anfang 50) hat seinen Wagen auf Tempo getrimmt. Mit seinem jungen Kollegen Eike als Beifahrer will er auf einer Landstraße gegen einen zweiten Wagen ein Rennen fahren. Beide sind nüchtern und wissen, wie gefährlich das ist.
>
> Eike: „Los, Hilmar, gib Gas! Den hängen wir ab!“ Hilmar: „Halt dich fest!“
>
> Die Wagen starten nebeneinander. Erlaubt sind 100 km/h, Hilmar fährt fast 190 km/h; Eike feuert ihn weiter an. In einer Kurve verliert Hilmar die Kontrolle, der Wagen kommt von der Straße ab. Eike stirbt noch an der Unfallstelle, Hilmar überlebt verletzt.
>
> **Hat sich Hilmar wegen fahrlässiger Tötung strafbar gemacht?**
