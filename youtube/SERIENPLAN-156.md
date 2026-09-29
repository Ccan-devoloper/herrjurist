# Herrjurist · Serienplan für 156 Examensvideos (16:9)

**Stand 29.09.2026.** Dies ist der verbindliche Produktions- und Statusrahmen, kein Ersatz für die individuelle [Abnahme je Folge](ABNAHME-16x9.md). Der zeichnerische Master ist **02/06**, die Rechtskarten stammen aus **06**, der Rhythmus und die Prüfpfadlogik aus **09 v3**. Die 80/100-Stilprüfung nach [MASTERSTANDARD-09.md](MASTERSTANDARD-09.md) und [`style_gate_80.py`](style_gate_80.py) gilt **für jeden Anker und jedes finale Szenenbild**, nicht nur für ein Musterbild. [VIDEOLEITLINIEN-16x9.md](VIDEOLEITLINIEN-16x9.md), [STANDARDINTRO.md](STANDARDINTRO.md) und [SOUNDBIBLIOTHEK.md](SOUNDBIBLIOTHEK.md) bleiben maßgeblich.

## Gesicherter Nacharbeitsbestand

Ein alter Export belegt keine Freigabe nach dem heutigen Standard. Vorhandene, sachlich richtige AAC-Sprachdateien bei Bildrevisionen wiederverwenden; Änderung nur bei einem notwendigen Text-/Stimmfehler.

| Arbeitsfolge | Folge | Stand und erforderlicher Eingriff | Abnahme |
| ---: | --- | --- | --- |
| 1 | **05 · Wohnungsdurchsuchung** (v2) | Alter Zeichenstil im ganzen Film. Fallbezogene 02/06-Bildfamilien und ca. 45 eigenständige Bilder neu; Karten/Pfad/Cues/Mund bei sichtbarer Rede neu prüfen. | Offen |
| 2 | **07** (v2) | Durchgehenden aktuellen Prüfpfad und tongebundene sichtbare Sprechbewegungen ergänzen; alle Bilder am 80er-Maßstab prüfen. | Offen |
| 3 | **08** (v2) | Prüfpfad und LipSync fehlen; eigene Cues, 80er-Bildbericht und Endfilmabnahme. | Offen |
| 4 | **09 · Kleinanzeigen-Betrug** (v3) | Historisch bestätigter Rhythmus-/Kartenmaster, aber neue Pflicht für tongebundene Mundbewegungen und 80er-Einzelbildbericht nachholen. | Nach heutigem Standard offen |
| 5 | **10 · Schweigen als Annahme** (v3) | LipSync fehlt und die Kulisse wiederholt 09. Eigenständigen fallbezogenen Schauplatz samt nötigen neuen Bildern, 80er-Gate und Cue-/Kartenprüfung herstellen. | Offen |
| 6 | **11 · Versammlungsverbot** (v3) | Gezielt **alle** verwendeten Bilder gegen 02/06 mit der 80er-Rubrik prüfen; Film komplett mit Ton sichten, gegebenenfalls reparieren. | 80er- und Hörprüfung offen |
| 7 | **12 · Raub/§ 249 StGB** (v4) | 45 neu illustrierte Bilder und technische v4-QA liegen vor. 80er-Einzelbildscores nachtragen und tatsächliches MP4 vollständig mit Ton sichten; v4-Bogen benennt diese Hörprüfung selbst als offen. | Noch nicht pauschal freigegeben |
| 8 | **13 · Minderjährigenrecht: E-Bike/100 € Anzahlung** (Altfilm) | §§ 106–110 BGB, § 433 II: vollständige Neufassung der Bilder nach bestehendem, noch Wort für Wort abzunehmendem Sprachtext; Mutter Mara, minderjährige Lina als neue Fallfigur, Verkäuferin Zylla trennen. 45 Bilder, Pfad, Karten, Mund, 80er-Gate. `episode-13-revision/research/recht-und-kartenplan.md` ist ein Vorplan. Dort ist die alte Abschiedsfloskel ab etwa 300,63 s vermerkt; **Schnitt erst nach Gegenhören**. | Offen |
| 9 | **14 · Abschleppen bei nachträglichem Haltverbot/Kostenfolge** (Altfilm) | Eigener öffentlich-rechtlicher Fall, aktueller Rechtscheck, vollständige 02/06-Neuillustration und 45-Cue-Revision. Titel nur Arbeitsbezeichnung des alten Films. | Offen |
| danach | **15–156 · Themenliste fehlt** | Die früher erwähnte 156er Liste ist in diesem Arbeitsstand nicht abrufbar. Themen, exakte Reihenfolge und bereits belegte IDs nicht erfinden. Erst verifizierte Liste einpflegen und mit vorhandenen Folgen abgleichen. | Nicht begonnen |

Zu Folgen 01–04 und 06 liegen im Projekt frühere Fassungen/Referenzen vor. Ihre Zuordnung zur noch zu beschaffenden 156er Liste und ihr heutiger Abnahmestand werden erst nach Bestandsabgleich eingetragen. 02 und 06 bleiben visuelle Master, auch wenn dies für andere Fassungen keine pauschale QA begründet.

## Schnellster sicherer Durchlauf

1. **Katalog und Recht:** Jeder Folge eindeutige ID, Thema, Status, Sprach- und Drive-IDs zuordnen. Den Themenpool nur als Material nehmen; amtlichen Normtext und einschlägige Primärrechtsprechung mit Datum prüfen. Fallhook, Gegenfall, examensorientierte Subsumtion und korrekten gliederungspunktweisen Schluss freigeben.
2. **Ton und Cues sperren:** Vorhandene AAC bei Revisionen ohne ElevenLabs erneut nutzen. Bei neuen Texten Sprecher/Charakter, Alter, Aussprache von Normen und natürlichem Hochdeutsch anhand echter Hörproben freigeben. Den **wirklichen** finalen Ton mit mindestens einer Wort-/Bild-/Karten-/Prüfpfad-Zeile je der ca. 45 Bildhalte versehen. ASR ist nur Suchhilfe. Bei erschöpften ElevenLabs-Credits nur eine kommerziell nutzbare Alternative nach Blindhörvergleich der wiederkehrenden Stimmen und deutschen Aussprache nutzen; keine ungeprüfte Stimme stillschweigend austauschen.
3. **Nur geprüfte Anker vervielfältigen:** Pro Film 4–6 fallgerechte Bildfamilien, jede mit eigener sinnvoller Bühne. Vollformatige 02/06-Bilder und Figuren-Golden-Reference **tatsächlich** in jeden Anker-Bildaufruf geben. Mit `style_gate_80.py` Anker erst bei ≥80/100 und allen Mindest-/Veto-Regeln freigeben. Danach ca. 45 unterschiedliche, kleine Bewegungsvarianten aus den Ankern erstellen; sämtliche finalen PNGs einzeln mit gleicher Rubrik prüfen. Personen, Requisiten und Fallchronologie bleiben konsistent. Sprechansichten erhalten eigene zur endgültigen Basis passende Viseme.
4. **Render und Abnahme:** 1920×1080/30 H.264, AAC Stereo 48 kHz; achtsekündiges Originalintro, keine gesprochene Schlussfloskel, vollständiges Originaloutro. Stets aktueller Prüfpfad oben links, marine/orange Rechtskarten in der Szene zum gehörten Satz; Text-Bounds, SHA-Bilder, vollständiger Decode, Untertitelspur-Abwesenheit prüfen. SFX nur an sichtbarer Handlung oder echten Wischzäsuren. Danach **das ganze finale MP4 mit Bild und Ton** und jeden Bildhalt sichten; Recht, Rollenstimmen, Lippen, Karten, Mobile-Lesbarkeit und Schluss separat abzeichnen.
5. **Dauerhaft ablegen:** MP4 plus vollständigen Produktionsmaster pro Folge in Drive, Metadaten/Größe/Hash nach Upload zurücklesen. Kein Binärmaterial nach GitHub; lokale große Renderzwischenstände erst nach überprüfter Archivierung löschen.

**Auslastung:** Maximal drei Folgen zugleich in den drei Stadien Vorproduktion, Illustration, Endkontrolle. Bis zu fünf Bildfamilien einer Folge können parallel laufen, aber Varianten erst nach dem jeweiligen Stil-Gate. Die Folge im Endcheck darf nicht als fertig gezählt werden. 11/12-Audits können neben der Bebilderung früherer Folgen bearbeitet werden; bei einem Fehler wird gezielt die abhängige Stufe erneut geprüft. Mit fünf vollständigen Pilotfolgen Durchsatz und Fehlerquote messen, bevor Batches vergrößert werden. Bei drei Veröffentlichungen pro Woche ergibt 156 ein Jahr; vor tatsächlicher Veröffentlichung den Rechtsstand nochmals kurz kontrollieren.

## Kapazität und ehrliche Grenzen

| Größe | Überschlagsrechnung für die ganze 156er Serie | Aussagegrenze |
| --- | ---: | --- |
| Hauptfilmlaufzeit | 156 × ca. 5 min = **780 min = 13 h** | Intro und Outro kommen je Folge hinzu; komplette Sicht-/Hörprüfung dauert mindestens die Filmlaufzeit, Korrekturrunden zusätzlich. |
| Hauptillustrationen | 156 × ca. 45 = **7.020** verschiedene Bilder als Bruttoziel | Bereits verwendbare, heute bestandene Bilder abziehen; verworfene Anker/Varianten hinzuzählen. Mundsprites zählen extra. |
| Szenenbildspeicher | Episode 12 v4: ca. 73 MB / 45 PNG; bei ähnlicher Größe ca. **11 GB** | Motive/Kompression schwanken. |
| MP4-Speicher | Episode 12 v4: ca. 37 MB; grob **5–7 GB** für 156 | Qualität/Kompression variieren. Ein Master-ZIP enthält dieselben Bilder erneut; Größen nicht unbesehen addieren. |
| TTS | `Summe Zeichen(final freigegebene Sprechertexte − wiederverwendbarer Altton)` | Keine seriöse Credit- oder Kostenangabe ohne aktuelle Anbieterpreise, Modell, Kontostand und wirkliche Texte. |
| Render-Temporärdaten | Episode 12 v4: ca. 677 MB in `work/` | Nur Arbeitskopie; nach Drive-Readback bereinigen. |

Die Episode-12-v4-Assetdateien wurden bei paralleler Erzeugung in etwa 19 Minuten geschrieben. Das ist **kein** End-to-End-Durchsatz: Recht, Audio, Bildankerfreigabe, Fehlversuche, Render und vollständige audiovisuelle Abnahme sind darin nicht enthalten. Für 156 Filme brauchen wir eine Folge-für-Folge dokumentierte Freigabe und laufende Rechtsstandsprüfung; eine Massenmarkierung als „perfekt“ ohne diese Nachweise ist ausgeschlossen.
