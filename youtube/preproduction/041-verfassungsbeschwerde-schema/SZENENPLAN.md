# Folge 041 · Verfassungsbeschwerde Schema: Zulässigkeit und Begründetheit – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_041.py`](src/skript_041.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen (Themenplan-Format „Schema“). Ein Beispielfall trägt das ganze Schema: Ein Bundesgesetz erlaubt den Behörden, die Bienenhaltung in Wohngebieten zu untersagen; Hobbyimkerin Frau Wendt erhält den Untersagungsbescheid, klagt durch alle Instanzen und verliert zuletzt vor dem Bundesverwaltungsgericht → Urteilsverfassungsbeschwerde (mittelbar gegen das Gesetz). Gegenfall Herr Seifert: will ohne Bescheid direkt gegen das Gesetz vorgehen (Unmittelbarkeit, Jahresfrist). Ablauf: Fall → Frage → Sachverhalt → A. Zulässigkeit I.–VII. (je Tafel, drei Wortlautkarten) → Gegenfall nach V. → B. Begründetheit (Prüfungsmaßstab, verfassungswidriges Gesetz) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:19,8 (5.212 gesprochene Zeichen). Mehr als fünf Minuten, weil das vollständige Zulässigkeitsschema mit sieben Prüfpunkten, drei Wortlautkarten (Art. 94 I Nr. 4a GG, § 90 I und II 1, § 93 I 1 und III BVerfGG), der Gegenfall zur Rechtssatzverfassungsbeschwerde und der Begründetheitsmaßstab getragen werden müssen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Wendt (WE), 32 | Hobbyimkerin, Beschwerdeführerin | Pose `standing/resting-1` (Pullover Grün `#8FD694`, Hose schwarz), Kopf `Long`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Serious` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Driven` (entschlossen) | `julia` (Frau, jung) |
| Herr Hübner (HU), um 60 | Sachbearbeiter Ordnungsamt, übergibt den Bescheid | Pose `standing/robot_dance-2` (dunkles Oberteil, ausgestreckte Hand), Kopf `Gray Short`, Brille `Glasses`, Hose `#3D3D58`, Haut `#E6B48F`; Mimiken `Calm` (ruhig), `Serious` (redet) | `william` (Mann, älter) |
| Richterin Reuter (RE), um 60 | Vorsitzende am Bundesverwaltungsgericht | Pose `standing/resting-2` (schwarzes Oberteil wie Robe), Kopf `Gray Medium` (Haar grau `#D6D6D6`), Brille `Glasses 2`, Hose `#3D3D58`, Haut `#F0C8A8`; Mimiken `Serious` (ruhig), `Solemn` (redet) | `elinor` (Frau, älter) |
| Herr Seifert (SE), um 45 | Hobbyimker im Nachbarort (Gegenfall) | Pose `standing/crossed_arms-1` (Pullover Orange `#F9A66C`), Kopf `Short 3`, Haut `#B07552`; Mimiken `Smile`, `Driven` (redet), `Suspicious` (denkt) | `marc` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts (Frau Wendt in den Fallszenen zu Hübner bzw. zu den Gerichten).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WE_redet`, `HU_redet`, `RE_redet`, `SE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (Posen mit Prothese wie `shirt-2`, `blazer-1`, `blazer-2`, `shirt-1` bewusst nicht gewählt), keine Karikaturen.
- **Stimmen nur aus dem Pool** marc, julia, elinor, william (alle vier verwendet); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Wendt, Hübner, Reuter, Seifert (nicht in der Liste früherer Namen, `grep` über alle Folgen ohne Treffer; „Albers“ wegen Folge 006 verworfen).
- Figuren-PNGs: `../peeps/op_041/` (56 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `besetzung_041.png` im Master.

**Abweichung von den letzten Folgen:** 036 Feuerwerksladen/Bundestag/Amtsgericht, 037–039 eigene Schauplätze; 020 (Grundrechtsprüfung) Fußgängerzone/Skateboard. Hier: Garten am Stadtrand mit Bienenbeuten, Haus und Sonnenblume; Instanzentreppe VG–OVG–BVerwG mit Briefkasten; Bundesverfassungsgericht als Gebäude. Posen `resting-1`, `resting-2`, `robot_dance-2` in 030–039 nicht verwendet, `crossed_arms-1` zuletzt 034. Stimmen anders als in 036 (sabrina, niklas, laura_ruhig, helmut).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Garten** `fall`–`we1` | Haus, zwei Bienenbeuten, Bienen, Sonnenblume; Wendt blickt nach rechts; Gesetz als Pille; Hübner kommt mit Bescheid, spricht; Wendt antwortet | tabler:`home`, Beuten (Karte/Linien), fluent-hc:`honeybee` (Gelb), fluent-hc:`sunflower`, tabler:`file-text` | `Fall · Bienen im Garten` (ab 0,0 s) → `Fall · Der Bescheid` | Garten · Völker-Pille · Gesetz · Untersagen · Sorge · Hübner · Bescheid · Blase Hübner · Wendt denkt · Blase Wendt | – |
| **B Instanzen** `klage`–`we2` | Wendt links, drei Gerichtsgebäude ansteigend (VG, OVG, BVerwG) mit Kreuzen; Richterin Reuter verkündet; Briefkasten, Umschlag „vollständiges Urteil“; Wendt: nach Karlsruhe | tabler:`building-bank` ×3, `mailbox` (Blau), `mail`, fluent-hc:`classical-building` | `Fall · Durch alle Instanzen` → `Fall · Das Urteil wird zugestellt` | VG · Kreuz · OVG · Kreuz · BVerwG · Reuter · Blase · Kreuz · Briefkasten · Umschlag · Blase Wendt · Karlsruhe | Einwurf (`szene_041einwurf_1`), wenn der Umschlag am Briefkasten erscheint |
| **C Die Frage** `frage`/`frage2` | Bundesverfassungsgericht, Wendt; Pillen A./B. | classical-building | `Fall · Hat die Verfassungsbeschwerde Erfolg?` | Frage · A · B | – |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **E I. Zuständigkeit** `zust`–`p13` | Wortlautkarte Art. 94 I Nr. 4a GG, Zeilen zum Wort; Wendt | classical-building, tabler:`calendar` | `A. Zulässigkeit › I. Zuständigkeit, Art. 94 I Nr. 4a GG` → `… § 13 Nr. 8a BVerfGG` | Karte · zwei Marker · seit 2024 · vorher · § 13 | – |
| **F1 II. Beschwerdeberechtigung** `berecht`–`art193` | Wortlautkarte § 90 I BVerfGG (Marker „Jedermann“, „einem seiner Grundrechte“), Haken Frau Wendt, Art. 19 III | tabler:`user` → `building` | `… II. Beschwerdeberechtigung, § 90 I BVerfGG` → `… › Art. 19 III GG` | Zeilen zum Wort | – |
| **F2 III. Prozessfähigkeit** `prozess` | Definition, Haken „volljährig“ | tabler:`id` + Pille „32 Jahre“ | `… III. Prozessfähigkeit` | 3 | – |
| **G IV. Beschwerdegegenstand** `gegenst`–`mittelbar` | Akt der öffentlichen Gewalt, Pillen Gesetz/Bescheid/Urteil, hier/dazu/mittelbar | `building-bank` → tabler:`book` | `… IV. Beschwerdegegenstand` | Zeilen, Pillen | – |
| **H V. Beschwerdebefugnis** `befugt`–`adressat` | Möglichkeit, Art. 2 I, Haken; selbst/gegenwärtig/unmittelbar, Haken | honeybee | `… V. Beschwerdebefugnis` → `… › Art. 2 I GG` → `… › selbst, gegenwärtig, unmittelbar` | Zeilen, zwei Haken | – |
| **I Gegenfall Seifert** `seifert`–`vollzug` | Tafel „Gegenfall“, Seifert spricht (Blase), denkt; Vollzugsakt | tabler:`file-text` | `Gegenfall · Herr Seifert` → `… Gesetz direkt angreifen?` → `… unmittelbar betroffen?` | Zeilen · Blase · Bescheid | – |
| **J VI. Rechtsweg und Subsidiarität** `rechtsweg`–`vortrag` | Wortlautkarte § 90 II 1 (zwei Marker), Haken „alle Instanzen“, Subsidiarität | `building-bank` ×3 | `… VI. Rechtswegerschöpfung, § 90 II 1 BVerfGG` → `… VI. Subsidiarität` | Zeilen zum Wort | – |
| **K1 VII. Form** `form`/`p92` | § 23 I, § 92 | tabler:`file-pencil` | `… VII. Form, §§ 23 I, 92 BVerfGG` | 2 Zeilen | – |
| **K2 VII. Frist** `frist`–`zul` | Wortlautkarte § 93 I 1, III (fünf Marker), Fristbeginn, Block „zulässig“; Kalender mit Pillen 1 Monat → Gesetz: 1 Jahr → zulässig | `calendar` | `… VII. Frist, § 93 I BVerfGG` → `… Frist gegen Gesetze, § 93 III BVerfGG` → `… Ergebnis: zulässig` | Marker zum Wort, Block | – |
| **L1 B. Begründetheit** `begr`–`heck2` | Prüfungsmaßstab, spezifisches Verfassungsrecht | classical-building | `B. Begründetheit › Prüfungsmaßstab` → `… › spezifisches Verfassungsrecht` | Zeilen zum Wort | – |
| **L2 B. Begründetheit: das Gesetz** `gesetzpr`–`nichtig` | verfassungswidriges Gesetz, Pillen Schutzbereich/Eingriff/Rechtfertigung, Block Erfolg | `book` | `B. Begründetheit › verfassungswidriges Gesetz?` | Zeilen, Pillen, Block | – |
| **M Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Nur Verfassungsrecht prüfen` | sechs Zeilen | – |
| **N Klausurschema** `sch`–`sb1` | A. I.–VII., B. | – | `Klausurschema` | 12 Aufbaustufen | – |
| **O Merksatz** `merke`/`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegungen.
**Geräusche:** ein Handlungsgeräusch (Einwurf am Briefkasten), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Kein Hammer: deutsche Gerichte verkünden ohne Hammer.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Ein neues Bundesgesetz erlaubt den Behörden, die Bienenhaltung in Wohngebieten zu untersagen. Frau Wendt (32) hält seit acht Jahren zwei Bienenvölker in ihrem Garten am Stadtrand. Herr Hübner vom Ordnungsamt untersagt ihr das per Bescheid: Die Bienen müssen bis Ende Mai weg. Frau Wendt klagt und verliert vor dem Verwaltungsgericht und dem Oberverwaltungsgericht; das Bundesverwaltungsgericht weist ihre Revision zurück. Das vollständige Urteil wird ihr zugestellt. Sie sieht sich in ihrer Freiheit verletzt und will nach Karlsruhe.
>
> Herr Seifert hält im Nachbarort Bienen und hat noch keinen Bescheid. Er will gleich gegen das Gesetz selbst vorgehen.
>
> **Hat die Verfassungsbeschwerde von Frau Wendt Erfolg?**

Kein Fiktiv-Hinweis auf Karten und im Sprechtext (Vorgabe Kanalinhaber 01.10.2026).
