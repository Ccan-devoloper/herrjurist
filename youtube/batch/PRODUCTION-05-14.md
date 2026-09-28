# YouTube Folgen 05–14 · Produktionsstand 28.09.2026

Zehn veröffentlichungsfertige 16:9-Folgen mit dem achtsekündigen LexVerse-Intro. Die MP4-Master liegen in Google Drive im Ordner „Herr Jurist YouTube“; große Medien- und Audiodateien werden nicht im Git-Repository gespeichert.

| Folge | Thema | Video |
|---|---|---|
| 05 | Wohnung durchsuchen: Welche Hürden gelten? | https://drive.google.com/file/d/1XoCsdN2uP07P8BFleB2XN5siKZMqE4mA/view |
| 06 | Diebstahl: Wann ist eine Sache wirklich weggenommen? | https://drive.google.com/file/d/1x4gVoPurZeutUEddUhNJboe9QbxMYdN4/view |
| 07 | WhatsApp-Angebot: Ab wann gilt die Nachricht als zugegangen? | https://drive.google.com/file/d/1H5bDTm_uj1w4XerEVrBhBNqK-AiKvbQc/view |
| 08 | Meinungsfreiheit: Wann wird scharfe Kritik unzulässig? | https://drive.google.com/file/d/1wAIC9o0r7tulP8CfKy7zPQZ3Yi5hk2ri/view |
| 09 | Kleinanzeigen-Betrug: Wann ist es strafbar? | https://drive.google.com/file/d/1ZJbuuCERF560G96Z1e-f7HQzAin5B4Hi/view |
| 10 | Schweigen und Vertragsannahme | https://drive.google.com/file/d/1hEy-5oZ69rcbWKx5uPUCxtxlr4Cwsh0L/view |
| 11 | Demo verboten: Was schützt Art. 8 GG? | https://drive.google.com/file/d/1c4gDxcVZgPLIfA_3n3qmaM1qrD0Qz5Ol/view |
| 12 | Diebstahl oder Raub: Der Moment der Gewalt | https://drive.google.com/file/d/13zmZz2jHmcYXXrM3enBIls2gLWilDIc9/view |
| 13 | Mit 16 ein teures E-Bike kaufen: Was gilt? | https://drive.google.com/file/d/1zOUflGqVp6julgsUwK_DnO1fDOQOnal2/view |
| 14 | Abgeschleppt: Musst du die Kosten immer zahlen? | https://drive.google.com/file/d/1KoBCnq_3akmXZS8Tpqknyw2jGk1gnktz/view |

## Verbindliche Gestaltung für die nächsten Folgen

- Golden References für Figuren; passende ElevenLabs-Stimmen. Mara ist etwa 40–50 Jahre alt und bekommt eine entsprechend erwachsene Stimme.
- Ein echter Fall als Einstieg, daran entlang die Rechtsfrage, die Normen, die Subsumtion und das Ergebnis. Am Ende ein systematisches, gesprochenes Prüfschema für die Klausur.
- Helles Tageslicht als Grundstimmung. Nacht nur, wenn der Sachverhalt es trägt; Folge 07 zeigt deshalb nur den Freitagabend im Dunkeln und den weiteren Ablauf bei Tag.
- Ruhiger Bildrhythmus; in diesen Folgen jeweils neun unterschiedliche Szenenbilder ohne exakte Wiederverwendung, zusätzlich gezielte Prüfungsfolien. Mehrere Figuren wechseln je nach Fall.
- Lesbarer Text vollständig innerhalb der Karten; keine Untertitel, keine Kapitelzählung, keine Fortschrittsanzeige, keine Schluss-Einblendung. Schlusswort: „Bis zum nächsten Thema!“
- Leise, punktuelle Geräusche; natürliches Sprechtempo. Rechtliche Aussagen anhand aktueller Gesetzes- und Rechtsprechungsquellen prüfen.
- Ausspielung: 1920×1080, 30 fps, H.264/AAC, etwa fünf Minuten. Nach dem Rendern ffprobe und vollständige ffmpeg-Dekodierung durchführen, bevor eine Drive-Datei ersetzt oder freigegeben wird.

Die Drehbücher stehen unter `youtube/episodes/05` bis `14`; ElevenLabs-Erzeugung unter `youtube/batch/generate-audio.mjs`. Medien bleiben außerhalb des Repositories.
