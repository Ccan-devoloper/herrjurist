# Abnahmebogen je Herrjurist-YouTube-Folge · Master 09 v3

**Folge/Titel:** …  
**Datum/Rechtsstand:** …  
**MP4 (Drive-Link):** …  
**Produktionsmaster (Drive-Link):** …  
**Golden References und Figuren:** …  
**Skript-/Schnittrevision:** …  
**Prüfer und Datum:** …

Jeden Punkt am **fertig exportierten MP4** und am Produktionsmaster belegen. `OK` und Zeitstempel bzw. Pfad eintragen, andernfalls korrigieren. Maßstab: [verbindlicher Master 09 v3](MASTERSTANDARD-09.md), [Folge 09 v3](https://drive.google.com/file/d/1cm_Z5JCs1YNAEGUj1_6K3feIsnJBSH4t/view?usp=drivesdk) sowie 02/06 für Zeichnung und Karten.

| Gate | Nachweis / Ergebnis |
| --- | --- |
| Fallhook nach vollständigem achtsekündigem Intro; Frage, Prüfung und Schluss bilden einen roten Faden | … |
| Jede juristische Aussage am aktuellen Normtext und einschlägigen Primärquellen geprüft; Fundstellen, Datum und Fallannahmen dokumentiert | … |
| Klausurschema mit römischer Gliederung und Untermerkmalen im Sprechertext und **progressiv** im Bild; Merksatz am Ende | … |
| Figuren aus Golden References; Alter/Stimme/Akzent passend; Figurenensemble nicht reflexhaft wie in letzter Folge | … |
| Bei **jeder Figurenrede** spricht im Bild die richtige Figur sichtbar; relevante Objekte und Tafeln passen zum Satz | … |
| Zeichenstil 02/06, reduzierte helle blau-orange Bühne, Requisiten mit Aussage; Nacht nur falls begründet | … |
| Serienkonstante Gestaltung: Zeichenstil/Golden References, ruhige blaue Kartenfläche links sowie Position und Grundgestaltung von Prüfpfad und Rechtskarten stimmen mit dem Master überein | Vergleichsbilder/Zeitstempel: … |
| Eigenständiges, zum Fall passendes Setting: Orte, Möbel, Architektur, Requisiten und Perspektiven aus dem Szenenplan nachvollziehbar; Schlüsselbilder/Kontaktbögen der letzten mindestens zwei Folgen nebeneinander geprüft; keine versehentlich gleiche Büro-/Tischkulisse | Szenenplan / Vergleichsfolgen / Bildstellen / ggf. begründete Rückkehr an denselben Ort: … |
| Ziel ca. 45 **verschiedene** Quelldateien, Hashes und einmalige Einsätze im Bildmanifest; kleine Variationen je stabiler Szene, keine künstlichen Wiederholungen | Anzahl / SHA-Manifeste / … |
| Ruhige Halte und sinnvolle Bildwechsel; Zäsur-Wischer nur sparsam, keine hektischen Sprünge oder Zoomersatz | Szenenliste / … |
| Prüfpfad während des **gesamten Hauptfilms** an derselben Stelle sichtbar und am gesprochenen Tatbestandsmerkmal aktuell | Anfang / Merkmalwechsel / Schluss: … |
| Marineblaue/orange Rechtstafeln **innerhalb** der Szene links, ohne Gesichter zu verdecken; keine geisternden Texte in Übergängen | Stichproben mit Zeitstempel: … |
| Sämtliche Texte einschließlich römischer Gliederung innerhalb ihrer Box; 100-%-Ansicht und verkleinerte mobile Vorschau lesbar | Text-Bounds / Sichtprüfung: … |
| Keine Untertitel/Untertitelspur, keine Kapitel-/Fortschrittsanzeige, keine unerwünschten Labels und keine Extra-Schlusseinblendung | … |
| Vorhandene Stimmen bei unverändertem Text wiederverwendet; natürliche Sprache und saubere Pausen; ElevenLabs-Credits nur für erforderliche Neuaufnahme | Voice-Provenienz / Hörprüfung: … |
| Jeder hörbare Wisch stimmt zeitlich mit einem sichtbaren Wisch überein; konkrete Geräusche sind sichtbar motiviert, leise und ohne Dauersound | SFX-Cueliste / Hörprüfung: … |
| Kein gesprochener Abschiedsgruß; letztes Sachwort vollständig; sanfter Anschluss an das vollständige Originaloutro | Zeitstempel / Hörprüfung: … |
| MP4 H.264/yuv420p/AAC, 1920×1080/30 fps/48 kHz Stereo, sinnvolle Länge, keine Subtitle-Streams; vollständiger Audio-/Video-Decode ohne Fehler | ffprobe / ffmpeg-Protokoll: … |
| Produktionsmaster vollständig (Skript, Bild-/SHA-Timeline, Rechtsquellen, Stimmen/SFX, Renderdateien, Intro/Outro-Verweise); ZIP lesbar | ZIP-Inhaltsliste / Integritätsprüfung: … |
| Video und Master auf Drive gespeichert; IDs, Größe, Name und Ordner per Readback bestätigt; GitHub ohne Binärpakete | … |

**Schlussprüfung:** ganze Folge mit Ton und Bild sichten, nicht allein Kontaktbogen und Stichproben. Offene Mängel: …  
**Freigabe:** `bestanden / noch nicht bestanden` · Datum …

Technische Beispielbefehle für eine lokale Datei `VIDEO.mp4`:

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=index,codec_name,width,height,r_frame_rate,sample_rate,channels -of json VIDEO.mp4
ffmpeg -hide_banner -v error -xerror -i VIDEO.mp4 -map 0:v:0 -map 0:a:0 -f null -
```

Diese Befehle prüfen **nicht**, ob der richtige Charakter spricht, Rechtstext zum Satz passt oder die Aussagen rechtlich stimmen; dafür sind die inhaltlichen Gates oben Pflicht.
