# Folge 186 · Einstellung § 170 II StPO: Beschwerde und Klageerzwingung – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_186.py`](src/skript_186.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Format **Schema** mit Fall aus Sicht der Staatsanwaltschaft (Einstellungsverfügung/Bescheid). Beispielfall nach dem Plan-Hook: Di, 13.1.2026, Augenoperation bei Dr. Wallner; Frau Rautenberg sieht danach rechts nichts mehr, zeigt ihn an und verlangt Bestrafung; Vernehmung als Beschuldigter, Gutachten ohne Behandlungsfehler, unterschriebener Aufklärungsbogen; Juni 2026: Referendarin Hölscher will einstellen und „die Akte weglegen“ (Mitteilungen fehlen). Fortsetzung in der Lösung: Bescheid zugestellt Do, 2.7.; Beschwerde Mo, 13.7. (Frist bis Do, 16.7.); Bescheid der Generalstaatsanwaltschaft zugestellt Mi, 5.8.; Antragsfrist bis Mo, 7.9.2026 (§ 43 Abs. 2 StPO).
Ablauf: Fall (Praxis → zu Hause → Vernehmung → Staatsanwaltschaft) → Sachverhalt → § 170 Abs. 1/Abs. 2 S. 1 (Wortlaut; tatsächliche/rechtliche Gründe, Verfahrenshindernis; Verweis 060/180) → Einstellungsverfügung Ziff. 1/Ziff. 2 → § 170 Abs. 2 S. 2 (Wortlaut, Nr. 88 RiStBV) → § 171 S. 1, 2 (Wortlaut), § 373b, Nr. 91 Abs. 2 RiStBV → korrigierter Entwurf (Blase Hölscher) → § 172 Abs. 1 (Wortlaut, § 147 Nr. 3 GVG) → § 172 Abs. 2 S. 1, Abs. 4 (Wortlaut) → § 172 Abs. 3 S. 1, 2 (Wortlaut, BVerfG 2 BvR 1550/17 Rn. 18, 19) → Ausschluss § 172 Abs. 2 S. 3 (Wortlaut; Fall: § 226 Abs. 1 Nr. 1 StGB im Raum) → §§ 174, 175 → Lösung Kalender Juli/September 2026 → Kanzlei (Blase Rautenberg) → Prüfschema → Klausurtipp (Lexi) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:32,5 bei 5.755 gesprochenen Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Rautenberg (RA), um 66 | Patientin, Verletzte und Antragstellerin | `standing/easing-2` (offene Jacke Orange `#F9A66C`, schwarzes Oberteil, Hose Anthrazit `#3A3A44`, weiße Schuhe), Kopf `Gray Medium` mit grauem Haar `#C9C9C9`, Brille `Glasses 4`, Haut `#F1C9A8`; Mimiken `Calm`, `Serious`, `Concerned\|Serious`, `Tired`, `Driven`, `Smile`, `Suspicious`; redet: `Concerned\|Serious`, redet2: `Driven` | `hilde` (Frau, älter) |
| Dr. Wallner (WA), um 50 | Augenarzt, Beschuldigter | `standing/doctor-nurse-01` (Arztkleidung der Pose mit Stethoskop, **ohne Logo**), Kopf `Short 4`, Haut `#E3B08C`, kein Bart, keine Brille; `Calm`, `Serious`, `Concerned\|Serious`, `Smile`; redet: `Serious` | `stephan` (Mann, mittel; ein Satz) |
| Referendarin Hölscher (HO), um 28 | Referendarin bei der Staatsanwaltschaft, entwirft die Verfügung | `standing/resting-1` (Oberteil Türkis `#7FD6D0`, schwarze Hose), Kopf `Long Bangs`, Haut `#EDC3A0`; `Smile`, `Smile Big\|Smile`, `Calm`, `Suspicious`, `Fear`, `Serious`; redet: `Smile Big\|Smile` | `lucy` (Frau, jung) |
| Rechtsanwältin (AN), um 45, Funktionsrolle, spricht nicht | Anwältin der Patientin (Anwaltszwang) | `standing/blazer-3` (Blazer Anthrazit `#3A3A44`, Hose Grau `#9A9AA8`), Kopf `Bun`, Haut `#C68E62`; `Calm`, `Serious`, `Smile` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 04.10.2026: Rautenberg 0, Wallner 0, Hölscher 0). Nie im Genitiv. Auf Tafeln „Dr. Wallner“, gesprochen „Doktor Wallner“.
- **Stimmen nur aus dem Pool** (stephan, hilde, christian, lucy): `stephan` spricht nur in Szene A3, `christian` nicht verwendet (keine Stephan/Christian-Paarung). Vorfolge 185 nutzt keine dieser Stimmen.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Praxis: Dr. Wallner (`_r`) und Frau Rautenberg einander zugewandt; Kanzlei: Anwältin (`_r`) blickt zu Frau Rautenberg, sie zu ihr; Tafelfolien: alle blicken nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `RA_redet`, `RA_redet2`, `WA_redet`, `HO_redet`, `HO_redet2` (je links/rechts) und Lexi.
- Figuren-PNGs: `../peeps/op_186/` (88 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_186.png`.
- **Darstellung Arzt/Patientin:** fiktiv und neutral, keine Klinik- oder Praxislogos, kein Blut, Behandlung nur als Icon (Tabler `eye`, `eye-off`), keine Karikatur, kein Ärzte-Bashing (Gutachten entlastet, Nr. 88 S. 2 RiStBV „kein begründeter Verdacht mehr“ wird gezeigt).

**Abweichung von den letzten Folgen:** 183 (`shirt-3`, `robot_dance-3`, `blazer-4`), 184 (`sitting/mid-2`, `blazer-1`), 185 (`resting-2`, `closed_legs-2`, `walking-1`, `walking-2`, `crossed_arms-2`, `shirt-4`). 186: `easing-2`, `doctor-nurse-01`, `resting-1`, `blazer-3` in keiner der drei Vorfolgen; Kleidung Orange/Türkis/Anthrazit (Grün aus 184/185, Lila-Hose aus 185, Koralle aus 183 vermieden), keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplätze neu: Augenarztpraxis mit Sehtafel und Schrank, Wohnzimmer, Vernehmungsraum, Büro der Staatsanwaltschaft, Kanzlei; Kalender Juli und September 2026 (Muster 168/180, neue Monate).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Praxis** `fall`→`danach` | Sehtafel, Schrank; Dr. Wallner und Frau Rautenberg ab 0,0 s mit Namensschildern | tabler:`eye` (Weiß), `eye-off` (Hellrot); `praxis()` | `Fall · In der Augenarztpraxis` → `· Operation am rechten Auge` → `· nach der Operation` | Grundbild · ernst · Auge + Pille „Operation am rechten Auge“ · Auge durchgestrichen · „danach: rechts kein Sehvermögen“ (beide besorgt) | – |
| **A2 zu Hause** `ra1`, `anz` | Wohnzimmer, Tisch | tabler:`file-text` | `Fall · der Vorwurf` → `· Strafanzeige wegen Körperverletzung` | Blase Rautenberg · Anzeige · „Antrag: Er soll bestraft werden.“ | – |
| **A3 Vernehmung** `verm`→`bogen` | Tisch, Fenster, Dr. Wallner | tabler:`file-certificate`, `writing-sign` | `Fall · Ermittlungen` → `· Vernehmung als Beschuldigter` → `· das Gutachten` → `· der Aufklärungsbogen` | Grundbild · Pille · Blase Wallner · Gutachten · Bogen | – |
| **A4 Staatsanwaltschaft** `akte`→`frage2` | Schreibtisch, Fenster, Akte, Hölscher | tabler:`folders` (Gelb) | `Fall · Juni: bei der Staatsanwaltschaft` → `· der Entwurf` → `· reicht das?` → `· die Fragen` | Akte landet · Blase Hölscher · erschrocken „Reicht das?“ · 2 Fragen | Akte (`szene_186akte_1`) |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,9 s) | – | `Sachverhalt` | 1 | – |
| **C § 170** `p170`→`fall2` | Wortlautkarte Abs. 1, Abs. 2 S. 1; Hölscher + Wallner | tabler:`scale`, `zoom-question`, `file-x`, `ban`, `folder` | `Einstellung › § 170 Abs. 1 StPO: Anklage` → … → `› hier: Einstellung` | Karte · 3 Marker · tatsächlich · rechtlich · Verfahrenshindernis · Verweis · Fall | – |
| **D Einstellungsverfügung** `verfg`→`fehlt` | Tafel als Verfügungsentwurf, Hölscher | tabler:`file-pencil`, `folder`, `mail`, `file-alert` | `Einstellungsverfügung · zwei Teile` → `› Ziff. 1` → `› Ziff. 2` → `› im Entwurf: Mitteilungen fehlen` | 4 | – |
| **E § 170 Abs. 2 S. 2** `p170s2`→`nr88` | Wortlautkarte, Dr. Wallner (am Ende froh) | tabler:`user-check`, `mail`, `circle-check` | `Mitteilung an den Beschuldigten › …` | Karte · 3 Marker · ✓ vernommen · Mitteilung · Nr. 88 | – |
| **F § 171** `p171`→`zust` | Wortlautkarte, Frau Rautenberg | tabler:`file-text`, `user-check`, `info-circle`, `eye-off`, `mail` | `Bescheid an die Antragstellerin › …` | Karte · Marker · ✓ Antragstellerin · ✓ Verletzte (§ 373b) · Zustellung (Nr. 91 Abs. 2) | – |
| **F2 korrigierter Entwurf** `ho2` | Tafel Ziff. 1, 2a, 2b; Blase Hölscher | – | `Einstellungsverfügung › der korrigierte Entwurf` | 3 | – |
| **G § 172 Abs. 1** `p172`→`nobel` | Wortlautkarte, Frau Rautenberg | tabler:`hourglass`, `building-bank`, `user-x`, `send`, `alert-triangle` | `Beschwerde › …` | Karte · 5 Marker · GenStA · ✗ nicht verletzt · ✓ Einlegung | – |
| **H1 § 172 Abs. 2 S. 1, Abs. 4** `p172b`, `olg` | Wortlautkarte, Frau Rautenberg | tabler:`calendar-event`, `gavel` | `Klageerzwingungsantrag › …` | Karte · 4 Marker · „1 Monat“ · ✓ OLG | – |
| **H2 § 172 Abs. 3** `p172c`→`anw` | Wortlautkarte; Rechtsanwältin kommt bei „Rechtsanwalt“ dazu | tabler:`list-check`, `scale`, `signature` | `Klageerzwingungsantrag › Form …` → `› Darlegung nach dem BVerfG` → `› keine Überspannung` → `› Anwalt` | Karte · Marker · BVerfG · ✗ Überspannung · ✓ Anwaltszwang | – |
| **H3 Ausschluss** `ausschl`→`offen` | Wortlautkarte § 172 Abs. 2 S. 3 (Auszug) | tabler:`ban`, `scale`, `eye-off`, `lock-open` | `Ausschluss › …` → `› kein Ausschluss (+)` | Karte · 3 Marker · §§ 223, 229 · § 226 · ✓ | – |
| **I §§ 174, 175** `p174`→`durchf` | Tafel mit zwei Ausgängen; Wallner + Rautenberg | tabler:`gavel`, `building-bank` | `Oberlandesgericht › …` | Verwerfung · Anklagebeschluss · Durchführung | – |
| **J1 Kalender Juli 2026** `lsg`→`mo13` | Kalender, Frau Rautenberg | tabler:`mail-opened`, `calendar-x`, `calendar-check` | `Lösung › Beschwerde: Frist` → … → `› Beschwerde am 13.7.2026: rechtzeitig (+)` | 2 · 16 Ende · 13 · ✓ | Briefumschlag (`szene_186brief_1`) |
| **J2 Kalender September 2026** `ablehn`→`mo7` | Kalender, Frau Rautenberg | tabler:`file-x`, `calendar-event`, `calendar-x` | `Lösung › Antrag …` → `› 1 Monat: Sa, 5.9.2026` → `› § 43 Abs. 2 StPO: Ende Mo, 7.9.2026, 24 Uhr` | 5 Sa · 7 Ende · ✓ | – |
| **J3 Kanzlei** `ra2` | Schreibtisch, Fenster; Anwältin + Rautenberg (Blase) | tabler:`file-pencil` | `Lösung › mit Anwältin zum Oberlandesgericht` | 1 | – |
| **K Prüfschema** `sch`→`s3` | breite Karte, Punkt für Punkt | – | `Prüfschema › I. …` | 9 Stufen | – |
| **L Klausurtipp** `tipp`→`k3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol | `Klausurtipp · Mitteilungen` → … | 4 | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Sätze, 4 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (Akte auf dem Schreibtisch, Öffnen des zugestellten Bescheids), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Auslassungen mit „…“, amtliche Schreibung („Anlaß“, „Abschluß“, „muß“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Am Dienstag, 13. Januar 2026, operiert Augenarzt Dr. Wallner Frau Rautenberg am rechten Auge. Danach sieht sie auf diesem Auge nichts mehr. Sie meint, über dieses Risiko nicht aufgeklärt worden zu sein, erstattet Strafanzeige wegen Körperverletzung und verlangt, dass er bestraft wird.
>
> Dr. Wallner wird als Beschuldigter vernommen und erklärt, er habe sie über die Risiken aufgeklärt. Ein Gutachten findet keinen Behandlungsfehler; der von Frau Rautenberg unterschriebene Aufklärungsbogen nennt das Risiko.
>
> Im Juni 2026 entwirft Referendarin Hölscher bei der Staatsanwaltschaft die Einstellungsverfügung. Ihr Plan: einstellen und die Akte weglegen.
>
> **Was gehört in die Einstellungsverfügung – und was kann Frau Rautenberg dagegen tun?**
