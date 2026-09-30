# Abnahmebogen · Testvideo Katzenkönig-Fall (LexVerse, Open Peeps)

**Folge/Titel:** Der Katzenkönig – Täter hinter dem Täter (Testvideo, BGHSt 35, 347 vereinfacht)
**Datum/Rechtsstand:** 30.09.2026; StGB §§ 17, 22, 23, 25, 26, 34, 35, 49, 211, 212
**MP4:** lokal gerendert und im Chat übergeben (`Katzenkoenig.mp4`, 11,2 MB, SHA-256 `bc6c1e5a0a66f49e888e112421421bc63d16f94dc440bf8cd2276ecae5d09231`); Drive-Ablage steht noch aus
**Produktionsmaster:** Quellen in diesem Ordner; Bilder werden mit `figuren_kk.py` aus der Figma-Bibliothek neu erzeugt
**Figuren:** Barbara, Peter, Richard, Nora (Open Peeps, `figuren_kk.py`), Lexi als feste Moderatorin (`figma-bibliothek/lexi.py`)
**Skript-/Schnittrevision:** v1
**Prüfer und Datum:** Claude (automatische und Bildprüfung), 30.09.2026. Die Hör- und Sichtprüfung durch den Kanalinhaber steht noch aus.

Gilt für diese Open-Peeps-Testreihe. Nach AGENTS.md und dem Master haben die jüngeren ausdrücklichen Nutzerentscheidungen Vorrang: Open-Peeps-Stil, Lexi, Carla, Pinselblasen, Sachverhaltskarte und nur Handlungsgeräusche. Abweichungen vom Master 09 v3 sind unten einzeln aufgeführt.

| Gate | Nachweis / Ergebnis |
| --- | --- |
| Fallhook, roter Faden | Fall ab 0:00 (Wohnung, Laden), Frage bei 0:44, dann die Sachverhaltskarte mit 5 s Lesepause. Danach Prüfung A. Richard und B. Barbara/Peter, Klausurtipp, Schema, Merksatz. **Abweichung:** Intro und Outro fehlen im Test. Die Drive-Dateien sind größer als die 10-MB-Grenze des Drive-Connectors. |
| Rechtsprüfung | BGHSt 35, 347 (Urteil vom 15.09.1988, 4 StR 352/88). Vereinfacht, Namen geändert, Tatort „Laden“. Richard: versuchter Mord (Heimtücke). § 34 scheitert, weil Leben nicht abwägbar ist und die Gefahr nur eingebildet war. § 35 scheitert, weil Millionen Fremde nicht vom geschützten Personenkreis erfasst sind. Vermeidbarer Verbotsirrtum § 17 S. 2 mit Milderung nach § 49 I. Barbara und Peter: mittelbare Täterschaft kraft Irrtumsherrschaft gegen das Verantwortungsprinzip. **Offen:** gesetze-im-internet.de ist aus dem Container gesperrt (Proxy 403). Die Normtexte wurden deshalb nicht online gegengelesen; die einschlägigen Absätze sind seit dem 2. StrRG unverändert. Mordmerkmale der Hintermänner (niedrige Beweggründe bei Barbara) werden bewusst nicht vertieft. |
| Klausurschema progressiv, Merksatz | Schema 3:04–3:24 Punkt für Punkt (A. Vordermann, B. Hintermänner, Streit, Ergebnis). Merksatz mit Lexi ab 3:25. |
| Figuren/Stimmen | Carla (Erzählerin und Lexi). Barbara `laura_klar`, Peter `stephan`, Richard `niklas` (ElevenLabs `eleven_v4`, Besetzung laut `stimme-elevenlabs/besetzung.json`). Nora spricht nicht. Die Statur jeder Person bleibt im ganzen Video gleich. |
| Richtige Figur spricht | 0:14 Barbara, 0:19 Peter, 0:27 Richard, 0:30 Barbara, 2:50 Lexi (Klausurtipp), 3:24 Lexi (Merksatz). Sprechblasen zeigen jeweils mit dem Schwanz auf den Mund der Sprecherin oder des Sprechers. |
| Mundbewegung | Vier Mundzustände je sprechender Ansicht: zu, a (`Explaining`), o (`Concerned Fear`) und e (`Hectic`). Augen und Nase bleiben aus der Grundmimik (`lexpeeps` „Augen\|Mund“, Schnitt bei 60 % der Gesichtshöhe, keine Patchkante). Die Zeiten stammen aus den ElevenLabs-Zeichenzeiten (Wortgrenzen). Die Viseme sind **aus der Schreibung geschätzt, kein Phonem-Alignment**. Zwischen Wörtern und bei anderen Sprechern ist der Mund geschlossen. Einzelbildprüfung von je zehn Frames bei Barbara, Peter, Richard und Lexi (`lip/lipsync.png`). Peters Bart wurde von `Full 2` auf `Full` geändert, weil `Full 2` den Mund verdeckte. |
| Zeichenstil / 80-%-Gate | **Nicht anwendbar:** Die Testreihe nutzt auf Nutzerwunsch Open Peeps (CC0) statt der Golden References 02/06. Es gibt keine Scorecard. |
| Serienkonstanten | Die Tafeln stehen links, die Figuren rechts, der Prüfpfad unten links (Open-Peeps-Layout der Testreihe). **Abweichung:** kein marineblaues 09-Kartendesign, keine blaue Bühne. |
| Eigenes Setting | Wohnung mit Kerze und Kristallkugel, danach Noras Laden (Ladenicon, Türglocke). Keine Bürokulisse. |
| Ca. 45 Bilder | 14 Szenen und Tafeln mit **70 Bildhalten**, jeweils kleine Änderungen innerhalb einer Szene (Zwiebelschalenprinzip). Die Figuren stammen aus 24 Grundbildern. **Abweichung:** Die Bilder werden programmatisch komponiert, statt als 45 einzelne Illustrationsdateien vorzuliegen. |
| Mundassets getrennt gezählt | 21 zusätzliche Mundzustände (Barbara 2×3, Peter 3, Richard 3, Lexi 3×3). |
| Ruhige Halte | Median etwa 3 s je Zustand, Szenenwechsel als Schiebeblende zwischen den Tafeln, **ohne Wischgeräusch** (Nutzervorgabe vom 30.09.2026). |
| Prüfpfad | Ist durchgehend sichtbar (unten links) und wird am Prüfpunkt aktualisiert, z. B. „A. Richard › Schuld › Verbotsirrtum, § 17 StGB“. |
| Tafeln verdecken keine Gesichter | Tafeln stehen x ≤ 1200, Figuren x ≥ 1260. Kein Textgeisterbild in den Übergängen (die Blende schiebt die leere Fläche). |
| Texte in Boxen | `z()` prüft den rechten Rand jeder Tafelzeile, `pruefe_im_bild()` prüft alle Elemente, `blase()` prüft die Textbreite. Die Sichtprüfung erfolgte am Kontaktbogen. |
| Keine Untertitel/Labels | Keine Untertitelspur, keine Kapitelzähler. |
| Stimmen wiederverwendet | Erstaufnahme mit 2.920 Zeichen. Der Cache `el_cache` (Text + Stimme + Settings) verhindert, dass beim Nachschnitt neu vertont wird. |
| Geräusche | Nur Handlungsgeräusche, 4 Einsätze: 0:09 Miau (Katzenkönig erscheint), 0:34 Schritte (Richard geht, etwa 3 s Gang ≈ 3 s Klang), 0:36 Ladenglocke (Ankunft im Laden), 0:41 Sturz (Nora fällt). Herkunft: Freesound CC0 (`geraeusche_herkunft.json`). |
| Schluss | Das letzte Sachwort „beherrscht“ ist vollständig. Das Outro fehlt (siehe oben). |
| Technik | H.264 High, yuv420p, 1920×1080, 30 fps, AAC 48 kHz stereo, 3:36,9. Vollständiger Decode ohne Fehler, −16,6 LUFS, True Peak −4,4 dBTP. |
| Produktionsmaster/Drive | **Offen:** Das MP4 wurde über den Chat übergeben. Die Drive-Ablage per Connector ist wegen der Dateigröße nicht möglich und muss manuell erfolgen. |

**Schlussprüfung:** Kontaktbogen aller 70 Bildhalte und Lippen-Einzelbilder gesichtet. Die Hörprüfung durch den Kanalinhaber steht aus.
**Freigabe:** noch nicht bestanden (Testvideo; Intro/Outro, Drive-Ablage und menschliche Hörprüfung offen) · 30.09.2026
