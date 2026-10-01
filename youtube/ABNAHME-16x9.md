# Abnahmebogen je Herrjurist/LexVerse-YouTube-Folge · Serienstandard Open Peeps (Katzenkönig)

**Folge/Titel (Nr. laut Themenplan):** …  
**Datum/Rechtsstand:** …  
**MP4 (Drive-Link):** …  
**Produktionsmaster (Drive-Link):** …  
**Figuren und Stimmen:** …  
**Skript-/Schnittrevision:** …  
**Prüfer und Datum:** …

Jeden Punkt am **fertig exportierten MP4** und am Produktionsmaster belegen. `OK` und Zeitstempel bzw. Pfad eintragen, andernfalls korrigieren. Maßstab sind der [Serienstandard](MASTERSTANDARD-09.md) und die Katzenkönig-Referenz ([`preproduction/katzenkoenig-test/`](preproduction/katzenkoenig-test/)). Das frühere 80-%-Stil-Gate gegen 02/06 entfällt seit dem 01.10.2026.

| Gate | Nachweis / Ergebnis |
| --- | --- |
| Fallhook nach vollständigem achtsekündigem Intro; Frage, Sachverhaltskarte (≈ 5 s Lesepause), Prüfung und Schluss bilden einen roten Faden | … |
| Jede juristische Aussage am aktuellen Normtext und an einschlägigen Primärquellen geprüft; Fundstellen, Abrufdatum und Fallannahmen dokumentiert; Hinweise „Rechtsstand“ aus dem Themenplan erledigt | … |
| Klausurschema mit römischer bzw. Buchstabengliederung und Untermerkmalen im Sprechertext und **progressiv** im Bild; Klausurtipp und Merksatz mit Lexi | … |
| Figuren ausschließlich Open Peeps (`lexpeeps.py`), Lexi nach `lexi.py`; Statur und Outfit je Person konstant; Besetzung nicht reflexhaft wie in der letzten Folge | Figurenrezept / … |
| Stimmen aus Erzählerin (Carla Blum) und Ensemble; Alter, Geschlecht und Akzent passen zur Rolle; Lea nicht bei Gewalt/Tat | Besetzung / … |
| Bei **jeder Figurenrede** spricht die richtige Figur sichtbar; der Blasenschwanz zeigt auf ihren Mund; Blasentext gleich dem Gesprochenen; Objekte und Tafeln passen zum Satz | Zeitfenster je Sprecher: … |
| Mundbewegung tongebunden (zu/a/o/e) aus ElevenLabs-Wortgrenzen; Pausen und andere Sprecher mit geschlossenem Mund; kein Loop, keine Patchkante; **gesamte** Redeabschnitte im finalen MP4 bei normaler Geschwindigkeit und frameweise gesichtet; Viseme als geschätzt dokumentiert | Mundassets / Lippen-Kontaktbild / … |
| Figuren und Requisiten nie seitlich oder oben angeschnitten (Assertionen `peep_voll`/`pruefe_im_bild` bestanden); Requisiten nur aus Icon-Bibliotheken mit Palettenfüllung; Lizenzen notiert | … |
| Serienkonstante Gestaltung: Cremegrund, Tafeln links (x ≤ 1200) und Figuren rechts (x ≥ 1260), Prüfpfad unten links, Nunito, Palette; Nacht nur falls begründet | Vergleichsbilder / Zeitstempel: … |
| Eigenständiges, zum Fall passendes Setting laut Szenenplan; Kontaktbögen der letzten mindestens zwei Folgen nebeneinander geprüft; kein versehentlich wiederholter Schauplatz | Szenenplan / Vergleichsfolgen / … |
| Mindestens 45 **unterschiedliche** Bildhalte im Zwiebelschalenprinzip; Bildhalt-Manifest mit Start/Ende und SHA-256 je Keyframe; keine künstlichen Wiederholungen | Anzahl / Manifest / … |
| Bildhalte und zusätzliche Mundzustände getrennt gezählt | Bildhalte / Mundassets: … |
| Ruhige Halte und sinnvolle Bildwechsel; Schiebeblenden nur zwischen Szenen; kein Zoomersatz | Szenenliste / … |
| Prüfpfad während des **gesamten Hauptfilms** an derselben Stelle sichtbar und am gesprochenen Merkmal aktuell | Anfang / Merkmalwechsel / Schluss: … |
| Rechtstafeln **innerhalb** der Szene links, Punkte erscheinen zum gesprochenen Begriff, Haken/Kreuz zur Bejahung/Verneinung; keine Gesichter verdeckt; keine geisternden Texte in Übergängen | Stichproben mit Zeitstempel: … |
| Sämtliche Texte innerhalb ihrer Box bzw. Blase (Assertionen `z()`/`blase()` bestanden); 100-%-Ansicht und mobile Vorschau lesbar | … |
| Ton-Bild-Gate: Cue-Timeline mit mindestens 45 Zeilen aus der verwendeten Sprachspur; jeder Bild-, Tafel- und Pfadstart an gehörten Wortgrenzen geprüft | Timeline-Pfad / … |
| Keine Untertitel/Untertitelspur, keine Kapitel-/Fortschrittsanzeige, keine unerwünschten Labels und keine Extra-Schlusseinblendung | … |
| Vorhandene Stimmen bei unverändertem Text wiederverwendet (Cache); natürliche Sprache und saubere Pausen; Credits nur für erforderliche Neuaufnahmen | Voice-Provenienz / Zeichenzahl / Hörprüfung: … |
| Nur Handlungsgeräusche bei sichtbarer Handlung (Renderer-Assertion `szene_*`), leise und sparsam; Schiebeblenden stumm; Herkunft je Datei in `geraeusche_herkunft.json` | SFX-Cueliste / Hörprüfung: … |
| Kein gesprochener Abschiedsgruß; letztes Sachwort vollständig; sanfter Anschluss an das vollständige Originaloutro | Zeitstempel / Hörprüfung: … |
| MP4 H.264/yuv420p/AAC, 1920×1080/30 fps/48 kHz Stereo, sinnvolle Länge, etwa −16 LUFS, keine Subtitle-Streams; vollständiger Audio-/Video-Decode ohne Fehler | ffprobe / ffmpeg-Protokoll: … |
| Thumbnail nach [THUMBNAILS.md](THUMBNAILS.md): Vorlage (Fall/Lern), Gebietsfarbe, Text ≤ 4 Wörter mit einem gelben Wort, Generatorprüfung ohne Fehler, Handy-Vorschau (246 × 138 px) lesbar, Aussage durch das Video eingelöst; Variante B für Test & Compare | Spezifikation / Generatorlauf / Vorschau: … |
| Upload-Texte (`beschreibung.txt`, `kapitel.txt`, `untertitel.srt`, `metadaten.json`) mit `tools/youtube_metadaten.py` erzeugt und gegengelesen; bei Landesrecht Normen aller 16 Länder in der Beschreibung | … |
| Produktionsmaster vollständig (Skript, Szenenplan, Rechtsquellen, Figurenrezepte, Bildhalt-Manifest, Cue-Timeline, Stimmen/SFX, Renderdateien, Intro/Outro-Verweise); ZIP lesbar | ZIP-Inhaltsliste / Integritätsprüfung: … |
| Video, Thumbnails, Upload-Texte und Master in Drive unter `LexVerse Produktion/NNN Titel/`; IDs, Größe, Name und Ordner per Readback bestätigt; Container aufgeräumt; GitHub ohne Binärdateien | … |

**Schlussprüfung:** ganze Folge mit Ton und Bild sichten, nicht allein Kontaktbogen und Stichproben. Offene Mängel: …  
**Freigabe:** `bestanden / noch nicht bestanden` · Datum …

Technische Beispielbefehle für eine lokale Datei `VIDEO.mp4`:

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=index,codec_name,width,height,r_frame_rate,sample_rate,channels -of json VIDEO.mp4
ffmpeg -hide_banner -v error -xerror -i VIDEO.mp4 -map 0:v:0 -map 0:a:0 -f null -
ffmpeg -hide_banner -i VIDEO.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
```

Diese Befehle prüfen **nicht**, ob die richtige Figur spricht, der Rechtstext zum Satz passt oder die Aussagen rechtlich stimmen. Dafür sind die inhaltlichen Gates oben Pflicht.
