# Übergabe: Start der Videoproduktion (Stand 01.10.2026)

Diese Notiz beschreibt den Stand nach Themenplan, Such-Optimierung und Thumbnails. Sie richtet sich an die erste Sitzung, die mit der Produktion der 780 Folgen beginnt. Verbindlich bleiben die in `AGENTS.md` genannten Standards.

## Fertig im Repository

| Was | Wo |
|---|---|
| Themenplan, 780 Folgen über 5 Jahre (Mo „Der Fall“, Mi „Examenswissen“, Fr Klausurpraxis/2. Examen/Methodik) | `THEMENPLAN-780.md`, `themenplanung/themenplan-780.csv` |
| Je Folge: YouTube-Titel, Suchbegriff, Beschreibungsanfang, Tags, Playlists, Thumbnail A/B | CSV oben; Quellen `themenplanung/seo_*.json`, `themenplanung/thumbs_*.json` |
| Thumbnail-Standard und Generator, alle 780 Angaben geprüft (0 Fehler) | `THUMBNAILS.md`, `thumbnails/` |
| Kapitelmarken, Untertitel (SRT) und Metadaten aus Sprachaufnahme und Renderer | `tools/youtube_metadaten.py` |
| Referenzproduktion mit aktuellem Setup (Katzenkönig) | `preproduction/katzenkoenig-test/` |
| Landesrecht länderneutral, Normen aller 16 Länder in der Beschreibung | `VIDEOLEITLINIEN-16x9.md` |

Neu erzeugen: `cd youtube/themenplanung && python3 plan_bauen.py && python3 ausgabe.py ../THEMENPLAN-780.md . <xlsx>`. Für `plan_bauen.py` werden `plan.json` und die übrigen Zwischendateien lokal erzeugt; sie sind nicht im Repository.

## Umgebung (vom Kanalinhaber eingerichtet)

- **Netzwerk: voll.** Normtexte und Urteile werden an amtlichen Quellen geprüft (gesetze-im-internet.de, rechtsprechung-im-internet.de, Landesrechtsportale, EUR-Lex). Bot-Schutz wird nicht umgangen.
- **API-Anmeldedaten:** ElevenLabs (`api.elevenlabs.io`, Header `xi-api-key`) und Freesound (`freesound.org`).
- **Drive per rclone:**
  - Das Setup-Skript installiert rclone.
  - Umgebungsvariablen: `RCLONE_CONFIG_LEXVERSE_TYPE=drive` und `RCLONE_CONFIG_LEXVERSE_SCOPE=drive.file`, dazu entweder `RCLONE_CONFIG_LEXVERSE_TOKEN` (JSON) oder `RCLONE_LEXVERSE_AUTH` (base64-Block aus neueren rclone-Versionen).
  - **Die Werte nie ausgeben oder loggen.** Im Fall `RCLONE_LEXVERSE_AUTH` den Block base64-dekodieren, das Feld `token` herauslösen und nur innerhalb des Prozesses als `RCLONE_CONFIG_LEXVERSE_TOKEN` setzen.
  - Wegen `drive.file` sieht rclone nur selbst angelegte Dateien. Zuerst den Ordner `LexVerse Produktion` anlegen und den Upload mit einer kleinen Testdatei prüfen (Upload, Auflisten, Löschen).
- **Ablage:**
  - In Drive je Folge `LexVerse Produktion/NNN Titel/` mit MP4, `thumb_A.jpg`, `thumb_B.jpg`, `master.zip` und den Upload-Texten (`beschreibung.txt`, `kapitel.txt`, `untertitel.srt`, `metadaten.json`).
  - Im Container nach erfolgreichem Upload aufräumen; die Festplatte ist begrenzt.
  - Binärdateien nie ins Repository.
- **YouTube-Upload** macht der Kanalinhaber in YouTube Studio. Nur dort gibt es Test & Compare für die Thumbnail-Varianten.

**Stand 01.10.2026 (geprüft):**
- rclone funktioniert. Upload, Auflisten und Löschen sind getestet.
- Der Ordner `LexVerse Produktion` hat die ID `1FPgTKSlZzqQiXg4N9b5qjTdBrvYKwigV`. rclone hat ihn angelegt.
- Das Gesamtwissen liegt in `_Quellen/`, die MD5-Summe `422ec58a376f07e72917b7acdf4ac90b` ist geprüft.
- **Ordner und Dateien nur mit rclone anlegen, nicht über den Drive-Connector.** Wegen `drive.file` sieht rclone nur seine eigenen Dateien; Ordner, die der Connector anlegt, wären für rclone unsichtbar und entstünden doppelt. Lesen geht mit beiden Wegen.
- **Offen:** Das Remote nutzt noch die gemeinsame rclone-Client-ID, die 2026 abgeschaltet wird. Ohne eigene Client-ID (`RCLONE_CONFIG_LEXVERSE_CLIENT_ID`/`_SECRET`) und ein damit neu erzeugtes Token fällt der Zugang dann aus.

## Wissensquelle

Die Gesamtwissen-HTML (`Jura_Gesamtwissen_…UPDATE30_FULL4958_UNCERTIFIED_2026-09-24.html`, 28,8 MB) liegt nicht im Repository. Der Kanalinhaber lädt sie zu Beginn neu hoch. Danach in Drive unter `LexVerse Produktion/_Quellen/` ablegen und in späteren Sitzungen von dort holen. Sie ist ausdrücklich „UNCERTIFIED“: Jede Aussage im Video an Normtext und Primärquelle prüfen. `tools/gesamtwissen_index.py` erschließt sie nach Überschriften.

## ElevenLabs-Budget

- **Verbrauch:** etwa 820 Zeichen pro Sprechminute (Katzenkönig), also rund 4.500 Zeichen je Folge. Mit Puffer für Neuaufnahmen sind das etwa 5.600 Credits je Folge und rund 4,4 Mio. für alle 780 Folgen.
- **Tarif:** Empfohlen ist Pro (600.000 Credits pro Monat, etwa 100 Folgen).
- **Sprachaufnahmen bei unverändertem Text wiederverwenden.**

## Vor Veröffentlichung inhaltlich zu prüfen (aus der Thumbnail-Arbeit)

- **Rechtsstand:**
  - 270: Amtsgericht bis 10.000 €
  - 766: Recht auf Reparatur, §§ 479a ff. BGB
  - 651: Ersatzlieferung beim Tierkauf
- **Clickbait-Grenze:** 358 („MUSS ER TAUCHEN?“, § 275 II BGB).
- **Heikle Darstellung oder Wortwahl:**
  - 25 B: „AUSCHWITZLÜGE“
  - 119: Badewannen-Fall
  - 238: „ACAB STRAFBAR?“
  - 269: Menschenwürde trotz Einwilligung
  - 494: HIV
  - 583: K.-o.-Tropfen
  - 770: Pkw-Maut
- **Gekürzte Suchbegriffe:**
  - 233/234: FFK
  - 465: „REFORMATIO IN PEIUS“
  - 524: „ZWECKVERFEHLUNG“
  - 610: „TRENNUNG OHNE TRAUSCHEIN“
  - 713: „FIKTIVE MÄNGELKOSTEN“
- **Abkürzungen:** 136 GOA, 209 SE, 482 WE.

## Offen aus früheren Arbeiten

- Katzenkönig-Video: Intro und Outro fehlen noch. Das MP4 hat der Kanalinhaber per Chat erhalten.
- Die Git-Historie ist 1,5 GB groß, wegen alter MP4s in `bilder/`, `vorschau/` und `youtube/willenserklaerung/`. Bereinigen hieße die Historie umschreiben und force-pushen; das nur auf ausdrücklichen Wunsch des Kanalinhabers.
