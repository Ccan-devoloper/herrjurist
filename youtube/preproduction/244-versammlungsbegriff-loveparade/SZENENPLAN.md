# Folge 244 · Versammlungsbegriff: Ist die Love Parade eine Demo? (Art. 8 GG) – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_244.py`](src/skript_244.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Grundrechte, Themenplan-Format „Klassiker-Fall“; Voraussetzung laut Plan: Grundrechtsprüfung (Schutzbereich, Eingriff, Rechtfertigung). Versammlungsrecht wie Folgen 028/233/234 nur verwiesen, Landesrecht am Beispiel NRW.
**Fall** (Hook „Ein Techno-Umzug mit politischem Motto will als Versammlung gelten, damit die Stadt die Reinigungskosten trägt“): Frühjahr, eine Stadt in NRW. Herr Brendel plant für den Sommer einen Sound-Umzug durch die Innenstadt (20 Musikwagen, Techno, Tausende Tanzende), will ihn als Versammlung durchführen, Motto „Mehr Raum für Kultur“, ohne Reden, Flugblätter oder Transparente. Herr Zander von der Stadt: „Das ist keine Versammlung, sondern eine Party. Sie brauchen eine Erlaubnis und zahlen die Reinigung: rund 38.000 €.“ Herr Brendel: „Wir haben doch ein Motto! Als Demo zahlt die Stadt.“
**Ablauf:** Fall → Frage (Love-Parade-Beschluss, Eilverfahren 2001) → Sachverhalt → 1. Wortlaut Art. 8 I GG (Wortlautkarte) → 2. Versammlungsbegriff: weit, erweitert, eng (Definitionskarte BVerfGE 104, 92), Warum eng? (Wortlautkarte § 2 III VersG NRW), Party oder Versammlung? → 3. gemischte Veranstaltungen: Gesamtgepräge, Zitatkarte „Bleiben Zweifel …“ (Rn. 25), drei Schritte (BVerwG 6 C 23.06), Love Parade und Gegenveranstaltung → 4. Fall: keine Versammlung, Folgen (Sondernutzung, StrWG NRW) → 5. Gegenfall Frau Lechner → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:05,7 (5.328 Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Brendel (BR), um 30 | Veranstalter des Sound-Umzugs | Pose `standing/robot_dance-3` (Pullover Koralle `#F07A6A`, Hose `#3D3D48`), Kopf `Pomp`, Haut `#E9B994`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile`, `Driven` (redet), `Suspicious`, `Concerned\|Serious`, `Serious`, `Tired`, `Awe` | `niklas` (Mann, jung) |
| Herr Zander (ZA), um 60 | Mitarbeiter der Stadt (Straßenbehörde) | `standing/crossed_arms-1` (Pullover Tannengrün `#4F7A63`), Kopf `No Hair 1`, Brille `Glasses`, Haut `#F0C8A8`, 97 % Höhe; `Serious` (redet), `Calm`, `Solemn`, `Suspicious`, `Smile` | `helmut` (Mann, älter) |
| Frau Lechner (LE), um 30 | Organisatorin des Umzugs gegen die Schließung des Jugendzentrums (Gegenfall) | `standing/resting-1` (Oberteil Hellblau `#8DB3F2`), Kopf `Long Bangs`, Haut `#C68E6A`, 94 % Höhe; `Smile` (redet), `Calm`, `Driven`, `Smile Big\|Smile` | `ela_froh` (Frau, jung; heitere Rolle, ein Satz) |
| Tänzerin (TA), Tänzer (TB) | namenlos, sprechen nicht | `robot_dance-2` (Hose Hellblau, Kopf `Bun`, Haut `#F2D0B5`); `polka_dots` (Grün, Kopf `Afro`, Haut `#8D5A3B`); `Smile`, `Cute` | – |
| Teilnehmer (TC) | namenlos, hält das Transparent im Gegenfall | `walking-3`, Kopf `Medium 1`, Haut `#D9A47E`; `Smile`, `Driven` | – |
| Lexi | Klausurtipp, Schema, Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Fallszene: Herr Brendel blickt zunächst zum geplanten Umzug (links), ab „Herr Zander“ nach rechts zu Herrn Zander, der nach links blickt. Gegenfall: Frau Lechner und der Teilnehmer blicken zum Musikwagen (links). Tafelszenen: alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BR_redet`, `ZA_spricht`, `LE_spricht` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Posen/Kleidung der Hauptfiguren nicht aus 239–243** (Figurenrezepte verglichen: dort resting-2, shirt-4, easing-1, walking-1, shirt-3, easing-2, crossed_arms-2, blazer-4, walking-2, blazer-3, pointing_finger-1/-2, blazer-2, shirt-1, walking-3, robot_dance-2); robot_dance-2 und walking-3 nur für namenlose Nebenfiguren in anderen Farben; Polka Dots nur beim namenlosen Tänzer (in 239–243 nicht verwendet).
- **Stimmen nur aus dem Pool** (`niklas`, `helmut`, `ela_froh`; `julia` nicht gebraucht; `ela_froh` nur für die heitere Gegenfall-Rolle mit einem Satz). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Brendel, Zander, Lechner – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` in keiner Text-/Codedatei unter `youtube/` (07.10.2026); verworfen: Kirchner (zu nah an „Kirschner“, Folge 192), Gerber (bereits in Kandidatenlisten). Eingetragen als „244: Brendel, Zander, Lechner“ vor der Vertonung. Alle Namen spricht nur die Erzählerin; kein Genitiv eines Namens.
- **Darstellung:** fiktiver Sound-Umzug ohne echte Marke/Veranstalter, keine Drogen- oder Alkoholklischees (nur Musikwagen, Noten, Lautsprecher, Tanzende); „Love Parade“ nur als Fallbezeichnung; die echte Gegenveranstaltung wird nicht benannt. Stadt sachlich. Alle Menschen Open Peeps, keine Icon-Gesichter; kein Richterhammer (Gericht als Waage).
- Figuren-PNGs: `../peeps/op_244/` (80 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 234 Stadtbücherei/Gerichtssaal, 233 Marktplatz mit Hausfassade, 241–243 (Atelier/Zeitung, Grundbuch, Strafverfahren). Hier neu: **Innenstadtstraße mit Musikwagen und Tanzenden** (Musikwagen aus Tabler `truck` + `device-speaker`, Fassaden programmatisch) und **Jugendzentrum** im Gegenfall. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Innenstadt** `fall`–`br1` | Häuser, Herr Brendel; Plan-Pille; Musikwagen, Noten, Tanzende; Anmeldung mit Motto, „keine Reden …“; Herr Zander, Blase; Eimer/Reinigung; Blase Brendel | tabler:`sun`, `truck`, `device-speaker`, `music`, `file-text`, `ban`, `bucket`; Fassaden programmatisch | `Fall · Frühjahr in einer Stadt in NRW` (ab 0,0 s) … `Fall · „Wir haben doch ein Motto!“` | 12 | – |
| **A2 Frage** `frage`–`frage2` | Tafel, Fallblock Love Parade | tabler:`help`, fluent-hc:`balance-scale` | `Die Frage · …` | 3 | – |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **C 1. Wortlaut** `art8`–`nichtdef` | Wortlautkarte Art. 8 I GG, Marker „versammeln“, „keine Definition“ | tabler:`book`, `help` | `1. Wortlaut · …` | 4 | – |
| **D1 2. Begriff** `begriff`–`def` | weit (−), erweitert (−), eng (+), Definitionskarte mit drei Markern | tabler:`users-group`, `music`, `messages`, `speakerphone` | `2. Versammlungsbegriff · drei Ansichten › …` | 10 | – |
| **D2 Warum eng?** `grund`–`nrw` | Schutz/Meinungsbildung (+), beliebiger Zweck (−), Wortlautkarte § 2 III VersG NRW mit Markern | tabler:`speakerphone`, `book` | `2. Versammlungsbegriff › Warum eng? / NRW` | 6 | – |
| **D3 Party?** `party`–`mittel` | Massenparty (−), Musik als Mittel (+), Tanzende rechts | tabler:`confetti`, `speakerphone` | `… › keine Massenparty / Musik und Tanz als Mittel` | 4 | – |
| **E1 3. Gemischt** `gemischt`–`zweifel` | bei Gelegenheit (−), Gesamtgepräge, Zitatkarte Rn. 25 mit Markern | tabler:`confetti`, `help`, fluent-hc:`balance-scale` | `3. Gemischte Veranstaltungen › …` | 7 | – |
| **E2 Drei Schritte** `schritte`–`sc` | progressiv 1.–3., Block „wie eine Versammlung“ | tabler:`list-numbers`, `music`, fluent-hc:`balance-scale` | `… › Gesamtschau in 3 Schritten › 1./2./3.` | 8 | – |
| **E3 2001** `lp`–`gv2` | Love Parade (rot), Gegenveranstaltung (grün), (+) | tabler:`music`, `files`, `speakerphone` | `… › Love Parade / Gegenveranstaltung / wie eine Versammlung` | 3 | – |
| **F1 4. Fall** `subs`–`erg` | Subsumtion mit Haken/Kreuzen, Ergebnis (−) | tabler:`truck`, `currency-euro`, `ban` | `4. Der Fall › …` | 8 | – |
| **F2 Folgen** `folge`–`land` | Sondernutzung, Love Parade Rn. 9, Auflagen/Kosten, Versammlung erlaubnisfrei, Landesrecht | tabler:`currency-euro`, `road`, `bucket`, `speakerphone`, `map-pin` | `4. Der Fall › Folgen … › Landesrecht` | 7 | – |
| **G 5. Gegenfall** `gegen`–`gegen3` | Jugendzentrum, Musikwagen (Türkis), Teilnehmer mit Transparent, Frau Lechner, Mikrofon, Flugblätter, Blase; Pillen „Musik als Mittel“, „Versammlung (+)“ | tabler:`truck`, `device-speaker`, `microphone`, `files`, `sun`; Fassade, Transparent programmatisch | `5. Gegenfall › …` | 8 | – |
| **H Klausurtipp** `tipp`–`tipp3` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | 5 | – |
| **I Schema** `sch`–`k4` | progressiv I.–III. | – | `Schema › …` | 9 | – |
| **J Merksatz** `merke`–`m2` | Lexi, Marker | – | `Merksatz` | 6 | – |

**Geräusche:** keine. In keiner Szene läuft eine sichtbare Handlung mit passendem Geräusch (der Umzug ist erst geplant, niemand geht oder hantiert); Musik unter dem Sprechtext würde die Sprache verdecken. „Lieber kein Geräusch als ein unpassendes“ (Auftrag); `geraeusche_herkunft.json` dokumentiert das.

## Sachverhaltskarte

„Frühjahr in einer Stadt in Nordrhein-Westfalen: Herr Brendel plant für den Sommer einen Sound-Umzug durch die Innenstadt mit 20 Musikwagen, Techno und Tausenden Tanzenden. Er will ihn als Versammlung durchführen, Motto: „Mehr Raum für Kultur“. Reden, Flugblätter oder Transparente sind nicht geplant. / Herr Zander von der Stadt hält den Umzug für keine Versammlung: Herr Brendel brauche eine Erlaubnis für die Nutzung der Straße und müsse die Reinigung tragen, rund 38.000 €. / Herr Brendel: „Wir haben doch ein Motto! Als Demo zahlt die Stadt.““ – Frage: „Ist der Sound-Umzug eine Versammlung im Sinne von Art. 8 Abs. 1 GG?“ (kein Fiktiv-Hinweis)
