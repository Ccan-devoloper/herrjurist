# Folge 252 · Anklageschrift § 200 StPO: Aufbau Schritt für Schritt – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_252.py`](src/skript_252.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Du hast den hinreichenden Tatverdacht bejaht und musst jetzt die Anklage zum Schöffengericht schreiben“): Referendar Hiller soll für seinen Ausbilder, Oberstaatsanwalt Endres, die Anklage entwerfen. In der Akte: Wohnungseinbruchdiebstahl ohne Gewalt (offenes Küchenfenster, Schmuck für 2.400 €, Fingerabdrücke, Ring im Ankaufsladen verkauft), Herr Unger schweigt und hat einen Verteidiger. Weil § 244 Abs. 4 StGB ein Verbrechen ist, scheidet der Strafrichter aus: Anklage zum Schöffengericht, wesentliches Ergebnis Pflicht.
Ablauf: Fall → Frage → Sachverhalt → § 200 Abs. 1 (Wortlautkarte) → § 200 Abs. 2 (Wortlautkarte) und Nr. 110 RiStBV → **Muster Schritt 1–5** (Kopf/Personalien/Verteidiger → Anklagesatz: Einleitung, Zeit/Ort, gesetzliche Merkmale → konkreter Tatvorwurf, Paragrafenkette → Beweismittel → wesentliches Ergebnis → Antrag, Gericht, Verweis 114) → zwei typische Fehler (Wortlautkarte BGH StB 39/21 Rn. 18) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Hauptfilm 6:42,7 (5.730 Zeichen), Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Referendar Hiller (HI), um 27 | schreibt die Anklage (Station Staatsanwaltschaft) | Pose `standing/pointing_finger-2` (schwarzer Pullover, Jeans `#3D5A80`, erhobener Zeigefinger = Frage), Kopf `Short 4_2` (blond), ohne Bart, Haut `#F0C8A8`; Mimiken `Calm`, `Concerned\|Serious` (redet), `Suspicious`, `Smile`, `Driven`, `Awe` | `niklas` (Mann, jung) |
| Oberstaatsanwalt Endres (EN), um 60 | Ausbilder | Pose `standing/blazer-3` (schiefergraues Sakko `#4A5568`, Hose `#3D3D48`), Kopf `Gray Short`, Brille `Glasses`, ohne Bart, Haut `#EBC29E`; Mimiken `Calm`, `Serious` (redet), `Smile`, `Suspicious`, `Solemn` | `helmut` (Mann, älter) |
| Herr Unger (UN), 41 | Angeschuldigter, spricht nicht | Pose `standing/walking-2` (schwarzes Shirt, Hose `#6B7A8F`), Kopf `Short 5` (Haar `#6B4A32`), ohne Bart, Haut `#E8B898`; Mimiken `Calm`, `Solemn` | – |
| Frau Probst (PR), um 65 | Zeugin, Geschädigte, spricht nicht | Pose `standing/robot_dance-2` (schwarzes Oberteil, Hose Lila `#B8A9F5`), Kopf `Gray Bun`, Haut `#F2D0B4`; Mimiken `Calm`, `Concerned\|Serious`, `Tired` | – |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel), `_r` blickt nach rechts (Hiller im Büro zu Endres). Keine Prothesen-Posen, keine Bärte, keine Polka Dots. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HI_redet`, `EN_redet` (je links/rechts) und Lexi. Angeschuldigter in Alltagskleidung mit ruhiger Mimik, ohne Herkunfts- oder Hautfarben-Klischee; keine Tatszene, keine Gewalt. Stimmen nur aus dem Pool (`ela_froh`, `julia` nicht gebraucht). **Namen:** Hiller, Endres, Unger, Probst (gesprochen), Dominik und Brack (nur Mustertafel) – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` unter `youtube/` ohne Treffer (verworfen: Faber – EuGH-Name in 125, Bruno – 009, Albers – 007/041, Wendler – zu nah an Wendt/Wendland); vor der Vertonung als „252: Hiller, Endres, Unger, Probst, Dominik“ eingetragen (Brack nachgetragen). Neben der Tafel heißt das Schild „OStA Endres“ (volle Schildbreite passt nicht neben Hiller), in den Fallszenen „Oberstaatsanwalt Endres“. Figuren-PNGs: `../peeps/op_252/` (58 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 249 (Treppenhaus, Atelier), 250 und 251 (parallel); Posen nicht aus 249–251 (`blazer-2`, `easing-1/-2`, `shirt-3/-4`, `resting-1/-2`, `crossed_arms-2`, `walking-1`). 039 (Anklageklausur, Strafrichter, Elektronikmarkt) und 114 (Zuständigkeit) nur verwiesen; hier Büro mit Schreibtisch, Fenster, Bücherregal und Tür sowie eine Erdgeschosswohnung mit Kommode. Schöffengericht statt Strafrichter (wesentliches Ergebnis Pflicht). Cremegrund durchgehend.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Büro** `fall`→`h1` | Fenster, Regal, Schreibtisch mit Akte und Lampe, Tür rechts; Hiller hinter dem Tisch (Tischfront verdeckt die Beine: er sitzt), Endres kommt zur Tür herein | tabler:`window` (Hellblau), `books` (Gelb), `door` (Holz → hell, offen), `folders`, `lamp` (Gelb); Tisch als `karte` | `Fall · Staatsanwaltschaft Ahornstadt` → `· Referendar Hiller` → `· Oberstaatsanwalt Endres` → `· „Schreiben Sie die Anklage“` → `· Womit fange ich an?` | Büro ab 0,0 s · Hiller · Tür auf, Endres · Endres redet (Blase) · Hiller redet (Blase), Endres lächelt | Tür öffnet sich (`szene_252tuer_1`) |
| **B In der Akte** `akte`→`schweigt` | Erdgeschosswohnung: Fenster, Kommode mit Schmuck; Frau Probst, später Herr Unger | tabler:`folder`, `calendar-event`, `window` (offen: hell), `diamonds` (Blau, verschwindet), `fingerprint` (Gelb), `receipt`; Ringe | `Fall · In der Akte` → `· 10.3.2026, gegen 14 Uhr` → … → `· Unger schweigt, hat einen Verteidiger` | Akte · Datum · Fenster offen, Probst · Schmuck weg (Ring), Probst besorgt · Fingerabdruck, Unger · Beleg · schweigt | – |
| **B2 Frage** `frage` | zurück im Büro (gleicher Ausschnitt) | wie A | `Fall · Die Frage` | Frage in zwei Pillen | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **D § 200 Abs. 1** `p200`→`vert` | Wortlautkarte mit zehn Markern zum Wort; Hiller und Endres | tabler:`book`, `user`, `file-description`, `calendar-event`, `list-check`, `file-text`, `fingerprint`, `building-bank` (Blau), `briefcase` | `§ 200 StPO › Inhalt …` → `› Abs. 1 › Angeschuldigter, Tat` → … → `› Beweismittel, Gericht, Verteidiger` | Karte · je Merkmal Marker und Requisit · „Anklagesatz“-Block · „außerdem …“ | – |
| **E § 200 Abs. 2, RiStBV** `abs2`→`land` | Wortlautkarte Abs. 2 (drei Marker), Haken Schöffengericht, Nr. 110 Abs. 1, Länderhinweis | tabler:`file-search`, `user`, `users` (Grün), `list-check`, `eye`, `map-pin` (Rot) | `§ 200 StPO › Abs. 2 › …` → `RiStBV › Nr. 110 …` | 6 | – |
| **F Schritt 1** `kopf`→`notw` | Musterblatt (weiß, rote Randlinie): Kopf, Überschrift, Personalien, Verteidiger; Block notwendige Verteidigung | tabler:`file-text`, `id`, `briefcase` | `Muster › 1. Kopf` → `› 1. Personalien` → `› 1. Verteidiger` → `› 1. notwendige Verteidigung` | Zeile für Zeile zum Wort | – |
| **G Schritt 2a** `as`→`abstr3` | Musterblatt mit Etiketten „Einleitung“, „Zeit und Ort“, „gesetzliche Merkmale“ | tabler:`file-text`, `user`, `calendar-event`, `list-check`, `home` (Lila) | `Muster › 2. Anklagesatz › …` | 5 | – |
| **H Schritt 2b** `konkr`→`kette2` | Musterblatt „konkreter Tatvorwurf“, „Paragrafenkette“ | tabler:`window`, `diamonds`, `book` | `› konkreter Tatvorwurf` → `› Paragrafenkette` | Zeile für Zeile | – |
| **I Schritt 3** `bm`→`bm6` | zwei Regeln mit Haken, Musterblatt Beweismittel 1.–4. | tabler:`list-check`, `user`, `fingerprint`, `receipt`, `camera` | `Muster › 3. Beweismittel › …` | 6 | – |
| **J Schritt 4** `we`→`we5` | Musterblatt wesentliches Ergebnis, Block „hier – nicht im Anklagesatz“, Kreuz „kein zweites Gutachten“ | tabler:`file-search`, `fingerprint`, `receipt`, `scale`, `x` | `Muster › 4. wesentliches Ergebnis › …` | 5 | – |
| **K Schritt 5** `an`→`e2` | Musterblatt Antrag; „Warum Schöffengericht?“ mit Kreuz/Haken, Verweis 114; Endres liest gegen (Blase) | tabler:`file-check`, `building-bank`, `users`, `user`, `book` | `Muster › 5. Antrag › …` → `Fall · Endres liest gegen` | 7 | – |
| **L Typische Fehler** `fehler`→`unw` | zwei Fehler mit Kreuz, Negativbeispiel, Wortlautkarte BGH StB 39/21 Rn. 18 mit Markern, roter Block „unwirksam“ | tabler:`alert-triangle`, `calendar-event`, `search`, `map-pin`, `building-bank`, `x` | `Typische Fehler › …` | 6 | – |
| **M Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 3 | – |
| **N Schema** `sch`→`s5` | I.–V. mit 1.–3. unter II. | – | `Schema › …` | 8 | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | Marker zum Wort | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom. Das erste Bild nach dem Intro zeigt ab 0,0 s das Büro (Fenster, Regal, Schreibtisch, Tür, Titelpille, Prüfpfad).
**Geräusche:** ein Handlungsgeräusch (Tür, wenn Endres hereinkommt). Freesound-API über den Proxy am 08.10.2026 HTTP 403 → vorhandene CC0-Datei unter eigenem Namen kopiert, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Am 10. März 2026 gegen 14 Uhr steigt jemand durch das offene Küchenfenster in die Erdgeschosswohnung von Frau Probst im Lindenweg 4 in Ahornstadt, in der sie lebt, und nimmt aus der Kommode Schmuck im Wert von 2.400 € mit.
>
> Am Fensterrahmen findet die Polizei Fingerabdrücke von Herrn Unger (41, nicht vorbestraft). Am 11. März verkauft er einen Ring aus dem Schmuck mit seinem Ausweis in einem Ankaufsladen. Lichtbilder vom Tatort liegen vor. Unger schweigt; er hat einen Verteidiger.
>
> Referendar Hiller hat den hinreichenden Tatverdacht bejaht; mehr als vier Jahre Freiheitsstrafe sind nicht zu erwarten. Oberstaatsanwalt Endres: „Schreiben Sie die Anklage zum Schöffengericht.“
>
> **Was gehört in die Anklageschrift, und in welcher Reihenfolge?**
