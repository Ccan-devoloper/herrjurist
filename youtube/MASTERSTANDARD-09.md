# Herrjurist/LexVerse YouTube 16:9 – verbindlicher Serienstandard (Open Peeps, Referenz Katzenkönig)

**Freigabestand: 01.10.2026.** Der Kanalinhaber hat am 01.10.2026 entschieden: Der Open-Peeps-Stil des Katzenkönig-Videos ist der verbindliche Serienstandard für alle 780 Folgen des [Themenplans](THEMENPLAN-780.md). Diese Datei behält aus Verlinkungsgründen ihren Namen.

- **Stilreferenz:** die Produktion [`preproduction/katzenkoenig-test/`](preproduction/katzenkoenig-test/) (Skript, Folien, Bausteine, Renderer, Abnahmebogen) und ihr MP4 (3:36,9 min, SHA-256 `bc6c1e5a…d09231`).
- **Nicht mehr Maßstab:** Folge 02, Folge 06 v2 und Folge 09 v3. Sie bleiben Archiv. Für den Zeichenstil gelten sie nicht mehr, ebenso wenig die marineblauen 09-Karten und die blaue Bühne.
- **Entfallen:** das 80-%-Stil-Gate und `style_gate_80.py` als Freigabevoraussetzung sowie die Pflicht, Illustrationen mit einem Bildmodell aus Referenzbildern zu erzeugen.
- **Bleiben:** der stets sichtbare Prüfpfad, synchrone Rechtstafeln, die passende Stimme je Figur mit tongebundener Mundbewegung, Intro und Outro, die Soundregeln und die Drive-Ablage.

Ergänzend gelten die [allgemeinen Leitlinien](VIDEOLEITLINIEN-16x9.md), die [Intro-Regel](STANDARDINTRO.md), die [Soundbibliothek](SOUNDBIBLIOTHEK.md), [THUMBNAILS.md](THUMBNAILS.md) und die [Übergabenotiz](PRODUKTION-START.md). Bei Widersprüchen gilt die jüngste ausdrückliche Entscheidung des Kanalinhabers.

## 1. Dramaturgie und Examensnutzen

1. **Einstieg:**
   - Vollständiges achtsekündiges Originalintro.
   - Direkt danach ein **konkreter, verständlicher Fall** in einer Fallszene mit Figuren und eine neugierig machende Rechtsfrage.
   - Kein abstrakter Normenvortrag als erster Satz. Der Fall trägt den ganzen Film; ein gut gewählter Gegenfall schärft die Abgrenzung.
2. **Sachverhaltskarte:** Nach der Frage zeigt eine Karte den Sachverhalt vollständig zum Nachlesen. Sie erscheint auf einmal, mit etwa 5 s Lesepause und dem Hinweis, das Video kurz anzuhalten.
3. **Roter Faden:**
   - Ablauf: Rechtsfrage → Norm und Gliederung → Merkmale mit Subsumtion am Fall → Ergebnis/Gegenfall → Klausurtipp → Schritt für Schritt aufgebautes Klausurschema → Merksatz.
   - Prüfpfad, Tafeln und gesprochener Text verwenden dieselben Bezeichnungen in derselben Reihenfolge.
4. **Examensnutzen:**
   - Der Anspruch ist Examenswissen für Jura-Studierende.
   - Definitionen, Streitstände und Ausnahmen nur, wo der Fall sie trägt.
   - Typische Klausurfehler und die konkrete Stelle im Gutachten benennen.
5. **Rechtsprüfung:**
   - Vor dem Sprechen an der **aktuellen amtlichen Norm** und der maßgeblichen Primärrechtsprechung validieren.
   - Fundstellen, Abrufdatum, Fallannahmen und notwendige Einschränkungen im Produktionsmaster dokumentieren.
   - Themenplan und Gesamtwissen („UNCERTIFIED“) sind Material, keine geprüfte Rechtsquelle.
6. **Schluss:**
   - Ein Merksatz, der ohne Zusatzsatz trägt; **keine gesprochene Verabschiedung**.
   - Unmittelbar danach das vollständige [Standardoutro](https://drive.google.com/file/d/1YFU3DVhWsWLJpgPuSOJvLp7JjcF_K3JL/view?usp=drivesdk) mit Originalton, ohne zusätzlichen Endscreen.

## 2. Bildsprache: Open Peeps nach Katzenkönig

- **Format:** 16:9, 1920 × 1080, 30 fps.
- **Grundfläche:** heller Cremegrund `(255, 248, 236)`.
  - Tageslicht ist die Normalform.
  - Ein Nachtverlauf nur, wenn der Fall ihn verlangt; den Grund dann im Szenenplan festhalten.
- **Figuren:**
  - Ausschließlich Open Peeps (CC0) aus [`openpeeps-erweiterung/figma-bibliothek`](openpeeps-erweiterung/figma-bibliothek/), zusammengesetzt mit `lexpeeps.py`.
  - Nur echte Open-Peeps-Posen, Köpfe, Gesichter und Bärte; nichts umzeichnen.
  - Statur, Kleidung, Hautton und Frisur einer Person bleiben im ganzen Video gleich. Für ein einheitliches Outfit Posen derselben Reihe (`…-1` oder `…-2`) kombinieren.
  - Aliens nur mit `Cyclops`/`Monster`-Gesicht und menschlichem Hautton.
- **Bildrand:**
  - Figuren und Requisiten nie seitlich oder oben angeschnitten (Mindestabstand 24 px, `peep_voll()`, `pruefe_im_bild()`).
  - Unten anschneiden nur bewusst (`unten_offen=True`).
- **Lexi** ist die feste Moderatorin. Ihr Aussehen ist in `lexi.py` festgelegt:
  - Aussehen: Dutt mit rosa Haarband, „Glasses 5“, gelbes Oberteil.
  - Stimme: Carla Blum.
  - Einsatz: 2–3 Auftritte je Video: Klausurtipp, Merksatz, optional ein weiterer. Nicht durchgehend im Bild.
- **Besetzung:** Fallfiguren aus dem Ensemble. Sie wechseln sinnvoll zwischen Folgen, kein reflexhaft gleiches Personal wie in der letzten Folge.
- **Requisiten:**
  - Nur Linien-Icons aus Bibliotheken: Tabler, Phosphor und Fluent Emoji (MIT), Pepicons (CC BY 4.0).
  - Gefüllt nur mit Palettenfarben über `ficon()`, nicht umgezeichnet.
  - Jedes Requisit illustriert den gerade gesprochenen Gedanken; keine Dekoration.
  - Herkunft und Lizenz der verwendeten Sets im Master notieren.
- **Palette:**
  - Tusche `INK (21, 21, 21)`, Weiß.
  - Flächen: Gelb `(249, 213, 110)`, Grün `(143, 214, 148)`, Blau `(141, 179, 242)`, Lila `(184, 169, 245)`, Rot `(240, 122, 106)`.
  - (+)/(−) in Dunkelgrün `(40, 150, 85)` und Dunkelrot `(215, 60, 45)`.
- **Schrift:** Nunito, Ersatzschrift DM Sans.
- **Blasen:**
  - Sprech- und Denkblasen im Pinselstil.
  - Der Schwanz zeigt auf den Mund der sprechenden Figur bzw. die Gedankenpunkte auf ihren Kopf (`blase(…, figur=…)`).
  - Blasentext kurz und wörtlich gleich mit dem Gesprochenen.
- **Setting:** Für jede Folge neu aus dem Fall entwickeln.
  - Ort, Raumaufteilung, Gegenstände und Perspektive tragen die konkrete Handlung.
  - Frühere Schauplätze nur, wenn die Geschichte erkennbar dorthin zurückkehrt; den Grund im Szenenplan festhalten.
- **Szenenplan vor dem Bau:** Für jede Szene festhalten:
  - Ort, Fallhandlung, Figuren mit Posen und Mimiken, Requisiten (Iconset/Name)
  - Tafelinhalt, Prüfpfadtext, Cue-Marken
  - beabsichtigte Abweichung von den letzten zwei Folgen
- **Zwiebelschalentechnik:**
  - Innerhalb einer Szene bleiben Bildausschnitt, Figurenposition und Requisiten stabil.
  - Benachbarte Bildhalte unterscheiden sich in sinntragenden Kleinigkeiten: Mimik, Pose, Blase, Requisit, Tafelpunkt.
  - Kein künstlicher Dauerzoom als Ersatz für neue Bildzustände.
- **Bildhalte:**
  - Ziel für etwa fünf Minuten Hauptfilm: **mindestens 45 unterschiedliche Bildhalte**, bei längeren Folgen anteilig mehr (rund 9 je Minute). Katzenkönig hatte 70 in 3:37 min, im Median etwa 3 s.
  - Die Bilder werden programmatisch komponiert. Nachweis über ein Bildhalt-Manifest: Start/Ende, Szene, Figurenzustände und SHA-256 des gerenderten Keyframes.
  - Wiederholte identische Zustände zählen nicht.
- **Mundzustände:**
  - Sie sind zusätzliche Assets und zählen nicht als Bildhalte.
  - Je sprechender Ansicht mindestens: zu (Grundmimik), a (`Explaining`), o (`Concerned Fear`), e (`Hectic`), montiert über `gesicht="Grund|Mund"` mit Schnitt bei 60 % der Gesichtshöhe, ohne Patchkante.
- **Übergänge:**
  - Zwischen Szenen eine Schiebeblende (14 Frames, endet am Folienstart).
  - Innerhalb einer Szene harte Schnitte oder kurze Pops.
  - Keine Effekte auf jeder Textzeile.

## 3. Rechtstafeln und stets sichtbarer Prüfpfad

Referenz ist die gerenderte Katzenkönig-Folge und [`bausteine.py`](preproduction/katzenkoenig-test/bausteine.py)/[`folien_kk.py`](preproduction/katzenkoenig-test/folien_kk.py).

| Element | Referenz Katzenkönig (1920 × 1080) | Verpflichtende Wirkung |
| --- | --- | --- |
| Prüfpfad unten links | x=40, y≈1034; Nunito Medium 30 px; Tusche mit Deckkraft 140 | Vom ersten Bild **nach dem Intro** bis zum letzten Bild **vor dem Outro** ohne Unterbrechung sichtbar. Bei jedem neuen Merkmal am gesprochenen Wort aktualisiert, z. B. `A. Richard › Schuld › Verbotsirrtum, § 17 StGB`. Kein Kapitel-/Fortschrittszähler. |
| Rechtstafel links | `karte(60, 60, 1140, h≤840)`: weiße Fläche, 5 px Tuschekontur, Radius 26, 10 px Versatzschatten. Titel Nunito ~50 px, Zeilen ~38 px. | Steht links in der Szene; die Figuren stehen rechts (Tafeln x ≤ 1200, Figuren x ≥ 1260). Die Karte erscheint vollständig, die Punkte folgen nacheinander genau zum gesprochenen Begriff. Keine Überdeckung von Gesichtern. |
| Klausurtipp | Tafel mit hellgelber Fläche `(255, 251, 230)`, Warnsymbol, Lexi rechts | Nur bei echtem Klausurhinweis. |
| Bewertungen | Bleistift-Haken/-Kreuz, (+)/(−) in Dunkelgrün/Dunkelrot | Genau zur gesprochenen Bejahung oder Verneinung. |
| Textgrenzen | `z()` begrenzt jede Tafelzeile auf x ≤ 1170; `blase()` prüft die Textbreite; `pruefe_im_bild()` prüft alle Elemente | Vor dem Rendern per Assertion, danach Sichtprüfung bei 100 % und in der mobilen Vorschau. |

- **Prüfpfad:** Er nennt immer die **aktuelle** Ebene. Fall, Sachverhalt, Klausurtipp, Schema und Merksatz bekommen eigene Pfadbezeichnungen.
- **Klausurschema:** Es baut sich **Gliederungspunkt für Gliederungspunkt** auf, mit den relevanten Untermerkmalen und denselben Bezeichnungen wie zuvor.
- **Übergänge:** Die Schiebeblende schiebt die leere Fläche; es gibt keine doppelt geisternden Texte.
- **Verboten im Hauptfilm:**
  - Untertitelband und eingebrannte Captions
  - Folgen-/Kapitelnummer und Fortschrittsanzeige
  - zusätzliche Schlusseinblendung

## 4. Stimmen, Mundbewegung, Geräusche und Schnitt

- **Stimmen:**
  - Erzählerin ist **Carla Blum** (Kanalstimme), Reserve Moritz Wegner.
  - Fallfiguren aus dem [Ensemble](preproduction/stimme-elevenlabs/BESETZUNG.md), innerhalb eines Videos klar unterscheidbar.
  - Rolle, Alter, Geschlecht und Akzent passen zusammen. Lea nicht für Gewalt- oder Tatbeschreibungen.
  - Modell `eleven_v4` über `synth_el.py` mit Zeichenzeiten.
- **Wiederverwendung:**
  - Bestehende Aufnahmen bei unverändertem Text aus dem Cache (Text + Stimme + Settings) wiederverwenden.
  - Neue Credits nur für neuen Text oder eine korrigierte Stimme.
- **Sichtbare Figurenrede:**
  - Genau die sprechende Figur zeigt tongebundene Mundbewegung (`redet()`).
  - Die Zeiten stammen aus den ElevenLabs-Wortgrenzen. Zwischen Wörtern, in Pausen und bei anderen Sprechern ist der Mund zu.
  - Kein Endlosloop, kein dauernd offener Mund.
  - Die Viseme sind aus der Schreibung geschätzt. So dokumentieren und nicht als Phonem-Alignment ausgeben.
- **Geräusche (Stand 30.09.2026):**
  - **Nur Handlungsgeräusche** bei sichtbarer Handlung (`szene_*`, im Renderer per Assertion erzwungen).
  - **Keine** Wisch-, UI-, Blätter- oder Markergeräusche; Schiebeblenden bleiben stumm.
  - Wenige Einsätze, Transient am visuellen Ereignis, sanft ein- und ausgeblendet, Sprache klar vorn.
  - Zuerst die [Soundbibliothek](SOUNDBIBLIOTHEK.md), dann Freesound CC0; jede Datei mit Herkunft in `geraeusche_herkunft.json`.
- **Intro und Outro:**
  - Introbild und -ton vollständig übernehmen und auf das Ausgabeformat bringen.
  - Nach dem letzten Sachwort sauber auf das vollständige Outro wechseln, ohne abgeschnittenes Wort.

## 5. Export, Quellen und zwingende Abnahme

- **MP4:**
  - H.264, yuv420p, 1920 × 1080, 30 fps; AAC Stereo 48 kHz, ohne Untertitelspur.
  - Länge in der Regel etwa fünf Minuten Inhalt plus Intro und Outro; wo der Stoff es erfordert, bis zu sieben Minuten Hauptfilm (Vorgabe Kanalinhaber, 01.10.2026), mit Begründung im Abnahmebogen.
  - Lautheit wie Katzenkönig, etwa −16 LUFS, True Peak unter −1 dBTP.
- **Ton-Bild-Gate vor dem Render:**
  - Cue-Timeline aus der tatsächlich verwendeten Sprachspur mit **mindestens 45 Zeilen**, je Bildhalt eine.
  - Jede Zeile: Start/Ende, Sprecher, Wort-/Satz-Cue, Bildhandlung, Tafelpunkt, Prüfpfad.
  - Jeden Start an den gehörten Wortgrenzen prüfen. Kein Gegenfallbild Sekunden nach der Erwähnung, kein fertiges Schema vor dem gesprochenen Aufbau.
  - Nach jeder Änderung die betroffenen Cues neu abgleichen.
- **Produktionsmaster in Drive** (`LexVerse Produktion/NNN Titel/master.zip`):
  - Skript, Quellen und Rechtsstand, Szenenplan
  - Figurenrezepte (`figuren_*.py`) und erzeugte Figuren-PNGs
  - Bildhalt-Manifest mit SHA-256, Cue-Timeline, Audio und Voice-Provenienz, SFX mit Herkunft
  - Fonts-Verweis, Render-/Schnittdateien, finale Videoverweise
- **Upload-Texte:** Nach [PRODUKTION-START.md](PRODUKTION-START.md) liegen sie im Folgenordner: MP4, `thumb_A.jpg`, `thumb_B.jpg`, `beschreibung.txt`, `kapitel.txt`, `untertitel.srt`, `metadaten.json`. Keine Binärdateien in GitHub.
- **Bildabnahme:**
  - Jeden Bildhalt im **finalen MP4** als Kontaktbogen sichten, kritische Stellen in voller Auflösung, Sprechfenster frameweise.
  - Kontaktbögen der letzten mindestens zwei Folgen danebenlegen. Stil, Tafel- und Prüfpfadposition bleiben konstant; Schauplätze und Requisiten passen zum neuen Fall.
- **Abnahmebogen:**
  - [Abnahmebogen](ABNAHME-16x9.md) **je Folge** ausfüllen.
  - Sicht- und Hörprüfung an Anfang, allen Merkmal- und Figurenwechseln, Szenenwechseln, komplettem Schema und Übergang ins Outro.
  - Technikprüfung: Metadaten, Manifest, Textgrenzen, fehlende Untertitelspur, vollständiger Fehler-Decode.
- **Freigabe:**
  - Endprodukt und Master in Drive ablegen und per Readback prüfen.
  - Eine Folge nie allein deshalb abnehmen, weil der Renderer fehlerfrei durchlief. Bild-Satz-Passung, Figurensprache, rechtliche Präzision und Lesbarkeit brauchen die menschliche Sicht- und Hörprüfung des Kanalinhabers.

**Nicht zu kopieren:** Fall, Wortlaut, Schauplätze, Figurenbesetzung und Zeitmarken des Katzenkönigs sind themenspezifisch. Zu übernehmen sind Stil, Layout, Tafel- und Prüfpfad-Logik, Mund- und Blasenlogik, die Ton-Zurückhaltung und das Abnahmeverfahren.
