# Folge 081 · Zulässigkeit und Begründetheit: Aufbau im Öffentlichen Recht – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_081.py`](src/skript_081.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Klausuraufbau. Beispielfall als roter Faden nach dem Hook des Themenplans („Die Klage ist zulässig, aber hat sie Erfolg?“): Die Studentin Tabea teilt ihr kleines Auto mit zwei Mitbewohnern. Vor drei Monaten wurde jemand damit geblitzt (25 km/h zu schnell); den Anhörungsbogen hat sie liegen lassen, den Fahrer hat die Stadt nicht ermittelt. Jetzt ordnet die Stadt per Bescheid ein Fahrtenbuch für ein halbes Jahr an (§ 31a Abs. 1 Satz 1 StVZO). Tabea: „Ich bin doch gar nicht gefahren!“ Mitbewohner Lennart: „Dann ist der Bescheid rechtswidrig. Deine Klage ist also zulässig.“ – der typische Fehler. Ablauf: Fall → Frage → Sachverhalt → Obersatz (Klausurkonvention) und Trennung → fehlende Zulässigkeit (Prozessabweisung, Verweisung, § 109 VwGO) → Bausteine der Zulässigkeit I.–V. als Überblick → III. Klagebefugnis (Wortlautkarte § 42 II, Fehler 1) → Fehler 2 (Lennart korrigiert sich) → B. Begründetheit (Wortlautkarte § 113 I 1) → I. Rechtswidrigkeit mit § 31a StVZO (Wortlautauszug) → Argument von Tabea, II. Rechtsverletzung, Ergebnis → Übertragung (Verfassungsbeschwerde, § 80 V VwGO) → Gewichtung (Verweis Folge 003) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:36,9 (5.688 gesprochene Zeichen); Begründung in ABNAHME.md. Die Folge verallgemeinert Folge 069 (Anfechtungsklage Schema), ohne deren Einzelprüfung zu wiederholen; der Fall bleibt in der Begründetheit bewusst offen (Methodik).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Tabea (TA), Anfang 20 | Studentin, Halterin des Autos, Klägerin | Pose `standing/polka_dots` (weißes Oberteil mit schwarzen Punkten, Hose Lila `#B8A9F5`), Kopf `Medium Straight`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Serious` (liest), `Rage|Serious` (Ärger, redet), `Concerned|Serious` (Sorge, fragt), `Suspicious` (denkt) | `julia` (Frau, jung) |
| Lennart (LE), Anfang 20 | Mitbewohner, studiert Jura | Pose `standing/pointing_finger-1` (erhobener Zeigefinger, schwarzer Pullover und Hose – die Pose hat keine einfärbbare Kleidung), Kopf `Short 2`, Haut `#E0A979`; Mimiken `Calm` (ruhig), `Driven` (redet), `Suspicious` (denkt), `Smile` (Einsicht, redet) | `niklas` (Mann, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Tabea blickt nach rechts zum Auto; Szene B: Tabea blickt nach rechts zu Lennart, er nach links zu ihr (Zeigefinger zu ihr); an den Tafeln blicken alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `TA_redet`, `TA_fragt`, `LE_redet`, `LE_einsicht` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** (`julia`, `niklas`; `helmut`, `ela_froh` nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Tabea, Lennart (nicht in der Liste vergebener Namen; `grep` über alle Skripte, Szenenpläne und Abnahmebögen ohne Treffer; „Hannes“ wegen Folge 005, „Merle“ wegen möglicher englischer Lesart verworfen). Kein Genitiv eines Namens im Sprechtext („das Argument von Tabea“).
- Kein Fiktiv-Hinweis; zweiter Mitbewohner nur erwähnt, nicht gezeigt (keine Icon-Menschen).
- Figuren-PNGs: `../peeps/op_081/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 080 (Hof am Abend, Fahrrad, Nachtbühne), 079 (Sitzungsraum einer Firma), 078 (Tischlerei, Wohnungstür, Kanzlei), 077 (Stadtpark bei Nacht), 069 (Gewerbegebiet mit Foodtruck, Verwaltungsgericht). Hier neu: **Straße vor dem WG-Haus** mit geparktem Auto und einem Rückblende-Feld (Auto fährt am Blitzer vorbei) und **Hausflur mit Briefkasten**. Posen `polka_dots` und `pointing_finger-1` in 075–080 nicht verwendet. Tageslicht auf Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Straße** `fall`–`fahrer` | WG-Haus, Sonne, Auto, Tabea; Schlüssel und Pille „Auto geteilt“; Rückblende-Feld: Auto fährt zum Blitzer, Blitz, Pille „25 km/h zu schnell“; Brief und Pille „Anhörungsbogen: liegen gelassen“; Lupe „Fahrer: unbekannt“ | tabler:`building` (Blau), `sun`, `car` (Gelb), `key`, `camera`, `bolt`, `zoom-question`; fluent-hc:`envelope` | `Fall · Das geteilte Auto` (ab 0,0 s), `Fall · Vor 3 Monaten: geblitzt`, `Fall · Der Anhörungsbogen` | Straße · Schlüssel · Pille · Rückblende · Blitz · 25 km/h · Brief · Pille · Sorge · Fahrer unbekannt | Auto fährt vorbei (`szene_081auto_1`), Spitze am Blitzer |
| **B Hausflur** `bescheid`–`frage2` | Briefkasten, Tabea mit Bescheid, Lennart; Blasen Tabea – Lennart – Tabea; Pillen „Lennart vermischt 2 Fragen“, Blöcke „Zulässigkeit“/„Begründetheit“ | tabler:`mailbox` (Blau), `file-text`, `notebook` (Gelb) | `Fall · Der Bescheid`, `Fall · Zwei Fragen vermischt` | Flur · Bescheid · Fahrtenbuch · drei Blasen · Ärger · Frage · zwei Blöcke | Briefkastenklappe (`szene_081briefkasten_1`) beim Wort „Bescheid“ |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Obersatz** `ober`–`begr` | Zitatblock Obersatz, Pille „Klausurkonvention“, A./B. mit Leitfrage | fluent-hc:`classical-building` | `Obersatz · Zulässigkeit und Begründetheit` | Zeilen zum Wort | – |
| **E Fehlt die Zulässigkeit** `unz`–`p109` | keine Sachentscheidung, Abweisung, Verweisung (§ 17a GVG), Zwischenurteil § 109 | classical-building | `A. Zulässigkeit › fehlt sie: keine Sachentscheidung` → `› Zwischenurteil, § 109 VwGO` | 5 | – |
| **F Bausteine I.–II.** `bau`–`b2a` | Rechtsweg, Klageart, Fahrtenbuchauflage | tabler:`notebook` + Pille | `A. Zulässigkeit · die Bausteine` → `› I. Rechtsweg, § 40 I 1 VwGO` → `› II. statthafte Klageart` | Zeilen zum Wort, Haken | – |
| **G Bausteine III.–V.** `b3`–`b6` | besondere Voraussetzungen, Beteiligte, RSB, Verweis 069 | tabler:`list-check` | `… › III. besondere Voraussetzungen der Klageart` → `› IV. Beteiligte` → `› V. Rechtsschutzbedürfnis` | Zeilen | – |
| **H III. Klagebefugnis** `wl42`–`f1` | Wortlautkarte § 42 II (zwei Marker), Möglichkeit (4 C 3.20), Adressatin (9 B 4.19), Fehler 1 | tabler:`file-text` + Pille „an Tabea“ | `… › III. Klagebefugnis, § 42 II VwGO` → `Typische Fehler › volle Rechtsverletzung geprüft` | Karte · Marker · Zeilen · Fehlerblock mit Kreuz | – |
| **I Fehler 2** `f2`–`zulerg` | Zitat Lennart mit Kreuz, „Frage der Begründetheit“, Blase Lennart (Einsicht), Ergebnis zulässig | – | `Typische Fehler › Begründetheit in der Zulässigkeit` → `A. Zulässigkeit › Ergebnis: zulässig` | Zitat · Kreuz · Zeile · Blase · Annahme · Ergebnis mit Haken | – |
| **J B. Begründetheit** `wl113`–`zwei` | Wortlautkarte § 113 I 1 (drei Marker), I./II. | classical-building | `B. Begründetheit, § 113 I 1 VwGO` | Karte · Marker · Blöcke | – |
| **K I. Rechtswidrigkeit** `rw`–`tb` | 1.–3., § 31a StVZO, Wortlautauszug mit Markern | tabler:`notebook` + Pille „§ 31a StVZO“ | `B. Begründetheit › I. Rechtswidrigkeit` → `› I. 1. Ermächtigungsgrundlage, § 31a StVZO` → `› I. 3. materielle Rechtmäßigkeit › Tatbestand` | Zeilen · Karte · Marker | – |
| **L Argument, Ergebnis** `arg`–`erg2` | Zitat Tabea, Kreuz/Haken, Rechtsverletzung, Ergebnis | tabler:`zoom-question` | `… › Feststellung des Fahrers` → `B. Begründetheit › II. Rechtsverletzung` → `Ergebnis · Hat die Klage Erfolg?` | Zeilen · Kreuz · Haken · Block | – |
| **M Andere Verfahren** `ueb`–`eil2` | Verfassungsbeschwerde, Eilverfahren | classical-building → tabler:`hourglass` | `Übertragung · gleicher Grundaufbau` → `› Verfassungsbeschwerde, Art. 94 I Nr. 4a GG` → `› Eilverfahren, § 80 V VwGO` | Zeilen | – |
| **N Gewichtung** `gew`–`gew3` | Urteilsstil/Gutachtenstil, Verweis 003 | tabler:`writing` | `Gewichtung · Urteilsstil und Gutachtenstil` | 5 | – |
| **O Klausurtipp** `tipp`–`tipp2` | Lexi warnt; zwei Leitfragen | Warnsymbol (Streamline Freehand) | `Klausurtipp · Wohin gehört der Gedanke?` | 5 | – |
| **P Klausurschema** `sch`–`sc` | progressiv: Obersatz, A I.–V., B I. 1.–3., II., C | – | `Klausurschema · Zulässigkeit und Begründetheit` | 14 Aufbaustufen | – |
| **Q Merksatz** `merke`, `m2` | Lexi erklärt, Marker | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Tabea teilt ihr kleines Auto mit 2 Mitbewohnern. Vor 3 Monaten wurde jemand damit geblitzt, 25 km/h zu schnell. Den Anhörungsbogen hat Tabea liegen lassen; wer gefahren ist, hat die Stadt nicht herausgefunden. – Heute erhält Tabea einen Bescheid der Stadt: Sie muss für ihr Auto ein halbes Jahr lang ein Fahrtenbuch führen. Tabea: ‚Ich bin doch gar nicht gefahren!‘ Ihr Mitbewohner Lennart meint: ‚Dann ist der Bescheid rechtswidrig. Deine Klage ist also zulässig.‘“ – Frage: „Hat die Klage Erfolg?“ (kein Fiktiv-Hinweis)
