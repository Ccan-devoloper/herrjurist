# Folge 036 · Verfahrensarten BVerfG: Welches Verfahren wann? Der Überblick – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_036.py`](src/skript_036.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis (Themenplan-Format „Schema“). Ein Übungsfall trägt alle fünf Verfahren: Ein Bundesgesetz verbietet privates Silvesterfeuerwerk. Daraus: Verfassungsbeschwerde (Ladeninhaberin), Organstreit (Fraktion gegen Bundesregierung, Auskunft verweigert), abstrakte Normenkontrolle (Landesregierung Süd), konkrete Normenkontrolle (Amtsrichter im Bußgeldverfahren, Art. 100 I GG) und Bund-Länder-Streit (Bundesregierung gegen Land Süd, das nicht ausführt). Ablauf: Fall → Frage „Wer will was gegen wen?“ → Sachverhalt → Zuständigkeit Art. 94 GG n. F. → je Verfahren W-Fragen, Wortlautkarte, Stichworte (Antragsberechtigung/Befugnis, Frist) → Klausurtipp → Klausurschema (A: nur Gültigkeit einer Norm, B: eigene Rechte) → Merksatz.
**Länge:** Hauptfilm rund 5:51 (4.770 gesprochene Zeichen). Mehr als fünf Minuten, weil fünf Verfahrensarten je mit Mini-Fall und Wortlautkarte (Art. 94 I Nr. 4a, 1, 2, 3 GG; Art. 100 I GG vorgelesen) und der Rechtsstand Art. 93/94 GG gebraucht werden.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Pfeiffer (PF), um 45 | Inhaberin eines Feuerwerksladens, Verfassungsbeschwerde | Pose `standing/polka_dots` (Bluse Rosa `#F6A5C0` mit Punkten), Kopf `Medium Bangs 3`, Hose Blau `#8DB3F2`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Serious` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Driven` (entschlossen) | `sabrina` (Frau, mittel) |
| Herr Pohl (PO), um 35 | Fraktionschef im Bundestag, Organstreit | Pose `standing/blazer-3` (Sakko Blau `#8DB3F2`), Kopf `Short 1`, Hose `#3D3D58`, Haut `#B07552`; Mimiken `Smile`, `Serious` (redet), `Suspicious`, `Driven` | `niklas` (Mann, jung) |
| Ministerpräsidentin Hagedorn (HA), um 55 | Landesregierung Süd, abstrakte Normenkontrolle; Gegenseite im Bund-Länder-Streit | Pose `standing/easing-2` (Jacke Lila `#B8A9F5`), Kopf `Gray Bun`, Hose `#3D3D58`, Haut `#F0C8A8`; Mimiken `Smile`, `Serious` (redet), `Solemn` (denkt), `Driven`, `Concerned|Serious` | `laura_ruhig` (Frau, mittel) |
| Richter Glaser (GL), um 60 | Amtsrichter, konkrete Normenkontrolle | Pose `standing/shirt-3` (dunkles Hemd `#4A4A66`), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#E6B48F`; Mimiken `Serious` (ruhig/redet), `Suspicious`, `Solemn` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Pohl zur Bundesregierung, Pfeiffer und Pohl in der Fragezeile zur Mitte).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `PF_redet`, `PO_redet`, `HA_redet`, `GL_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikaturen.
- **Stimmen nur aus dem Pool** sabrina, niklas, laura_ruhig, helmut (alle vier verwendet); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Pfeiffer, Pohl, Hagedorn, Glaser (nicht in der Liste früherer Namen, in keiner Vorfolge verwendet).
- Der Kunde und die Bundesregierung erscheinen nur als Requisiten (Rakete/Feuerzeug/Bußgeld bzw. Gebäude „Bundesregierung“), ohne Figur und ohne Stimme.
- Figuren-PNGs: `../peeps/op_036/` (68 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 032 Altstadt/Farbengeschäft, 033/034/035 Strafrecht bzw. Schwarzarbeit mit eigenen Schauplätzen; 004 (Organstreit) Ministerbüro. Hier: Feuerwerksladen, Bundestag mit Gebäuden Bundestag/Bundesregierung, Landkarte „Land Süd“, Amtsgericht mit Hammer und Stempel; Gruppenbild aller vier Antragsteller. Posen `polka_dots`, `blazer-3`, `shirt-3` in 030–035 nicht verwendet; `easing-2` zuletzt in 004.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Das neue Gesetz** `fall`–`viele` | Bundestag links, Gesetzblatt, Feuerwerk rechts, Verbotszeichen | tabler:`building-bank` (Gelb), `file-text`, fluent-hc:`fireworks` (Gelb), tabler:`rocket` (Rot), fluent-hc:`firecracker` (Rot), tabler:`ban`, `receipt-euro`, fluent-hc:`classical-building` | `Fall · Das neue Gesetz` (ab 0,0 s) | Bundestag · Gesetz · Feuerwerk · Rakete/Böller · Verbot · Verkauf · Abbrennen · Bußgeld · Karlsruhe | – |
| **B Feuerwerksladen** `pfeiffer`/`pf1` | Regal mit Feuerwerk links, Frau Pfeiffer, Ladensymbol | Regal (Karte), fireworks, rocket, firecracker, tabler:`sparkle`, `building-store`, `ban` | `Fall · Frau Pfeiffer, Feuerwerksladen` | Laden · Blase · Verbot über dem Regal | – |
| **C Bundestag** `pohl`–`po1` | Bundestag links, Pohl, Bundesregierung rechts; Frage, Antwort verweigert | `building-bank` ×2 (Gelb/Blau), `message-question`, `ban` | `Fall · Fraktion fragt die Bundesregierung` | Bundestag · Pohl · Regierung · Frage · verweigert · Pohl denkt · Blase | – |
| **D Land Süd** `hagedorn`/`ha1` | Landkarte, Hagedorn | tabler:`map` (Grün), classical-building | `Fall · Landesregierung Süd` | Hagedorn · Karte · Blase · Karlsruhe | – |
| **E Amtsgericht** `kunde`–`gl1` | Kunde (nur Requisiten): Feuerzeug, Rakete, Bußgeld, Einspruch; Amtsgericht mit Hammer, Richter Glaser, Stempel „Vorlage“ | tabler:`lighter`, `rocket`, `receipt-euro`, `file-text`, `gavel`, `rubber-stamp` | `Fall · Bußgeld und Einspruch` → `Fall · Am Amtsgericht` | Feuerzeug · Rakete · Bußgeld · Einspruch · Amtsgericht · Glaser · Blase · Stempel | Feuerzeug (`szene_036feuerzeug_1`), Stempel (`szene_036stempel_1`) |
| **F Die Frage** `frage`/`regel` | alle vier nebeneinander mit Rollenpillen | – | `Fall · Welches Verfahren passt wann?` → `Fall · Wer will was gegen wen?` | vier Rollen einzeln · Frage · Klausurfrage | – |
| **G Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **H Zuständigkeit** `art94`–`p13` | Tafel; Gericht, Kalender „28.12.2024“ | classical-building, `calendar` | `Zuständigkeit › Art. 94 GG (seit 28.12.2024)` → `› früher Art. 93 GG` → `› BVerfGG, Katalog § 13` | sechs Zeilen zum Wort | – |
| **I1 Verfassungsbeschwerde** `vb`–`wl4a` | W-Fragen, Wortlautkarte Art. 94 I Nr. 4a mit Markern, Block; Pfeiffer | `building-store`, `file-text` | `1. Frau Pfeiffer › Wer will was gegen wen?` → `1. Verfassungsbeschwerde, Art. 94 I Nr. 4a GG` | Karte · Wer · Was · Gegen wen · drei Marker · Block | – |
| **I2 VB-Stichworte** `vbbef`/`vbfrist` | Beschwerdebefugnis, Fristen, Rechtsweg; Pfeiffer | `calendar` + „1 Jahr“/„1 Monat“ | `1. Verfassungsbeschwerde › Beschwerdebefugnis` → `› Frist, § 93 BVerfGG` | Zeilen zum Wort | – |
| **J1 Organstreit** `os`/`wl1` | W-Fragen, Wortlautkarte Nr. 1, Block; Pohl | `building-bank`, `message-question` | `2. Fraktion Pohl › Wer will was gegen wen?` → `2. Organstreit, Art. 94 I Nr. 1 GG` | wie I1 | – |
| **J2 Organstreit-Stichworte** `osbet`–`osfest` | Beteiligte, Frist, Feststellung; Pohl | tabler:`users`, `calendar`, classical-building | `2. Organstreit › Beteiligte, § 63 BVerfGG` → `› Frist, § 64 III BVerfGG` → `› nur Feststellung, § 67 BVerfGG` | Zeilen · Block | – |
| **K1 abstrakte NK** `ank`–`ankber` | W-Fragen, Wortlautkarte Nr. 2 (fünf Marker), Block; Hagedorn | `map`, tabler:`scale` | `3. Landesregierung Süd › …` → `3. Abstrakte Normenkontrolle, Art. 94 I Nr. 2 GG` → `› Antragsberechtigung` | wie I1 | – |
| **K2 abstrakte NK-Stichworte** `ankobj` | keine eigenen Rechte, keine Frist; Hagedorn | `hourglass-off` | `3. Abstrakte Normenkontrolle › keine eigenen Rechte, keine Frist` | Haken je Zeile | – |
| **L1 konkrete NK** `knk`/`wl100` | „Wer? Gericht“, Wortlautkarte Art. 100 I (vorgelesen, fünf Marker), Block; Glaser | `gavel` | `4. Richter Glaser › …` → `4. Konkrete Normenkontrolle, Art. 100 I GG` | Marker zum Wort | – |
| **L2 konkrete NK-Stichworte** `knkmon`–`knkpart` | Verwerfungsmonopol, Überzeugung, Entscheidungserheblichkeit, keine Vorlage auf Antrag; Glaser | classical-building, `file-text` | `4. Konkrete Normenkontrolle › Verwerfungsmonopol` → `› Überzeugung` → `› Entscheidungserheblichkeit` → `› keine Vorlage auf Antrag` | Zeilen, Kreuz | – |
| **M1 Bund-Länder-Streit** `bls`/`wl3` | W-Fragen, Wortlautkarte Nr. 3, Block; Gebäude „Bundesregierung“ gegen Hagedorn | `building-bank` (Blau), `arrows-exchange` | `5. Bundesregierung › …` → `5. Bund-Länder-Streit, Art. 94 I Nr. 3 GG` | wie I1 | – |
| **M2 BLS-Stichworte** `blsbet`/`blsbr` | Beteiligte, Vorverfahren Bundesrat, Monatsfrist; Hagedorn | `building-bank` + „Bundesrat“, `calendar` | `5. Bund-Länder-Streit › Beteiligte, § 68 BVerfGG` → `› zuerst der Bundesrat, Art. 84 IV GG` | Zeilen | – |
| **N Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Erst die Verfahrensart` → `Klausurtipp · Art. 94 statt Art. 93` | sechs Zeilen | – |
| **O Klausurschema** `sch`–`sb3` | Schema A/B mit I./II./III., je Zeile Kriterium und Verfahren mit Norm | – | `Klausurschema` | 12 Aufbaustufen | – |
| **P Merksatz** `merke`/`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; keine Bewegungen.
**Geräusche:** zwei Handlungsgeräusche (Feuerzeug, Stempel), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene G, erscheint vollständig)

> Ein neues Bundesgesetz verbietet privates Silvesterfeuerwerk, den Verkauf und das Abbrennen; Verstöße kosten ein Bußgeld. Frau Pfeiffer verkauft in ihrem Laden seit Jahren Feuerwerk und will sich in Karlsruhe gegen das Gesetz wehren. Die Fraktion von Herrn Pohl fragt im Bundestag, auf welches Gutachten sich das Verbot stützt; die Bundesregierung verweigert die Antwort. Die Landesregierung Süd hält das Gesetz für verfassungswidrig und will es prüfen lassen; bis dahin setzt das Land Süd es nicht um, die Bundesregierung rügt das.
>
> Ein Kunde zündet trotzdem Raketen, soll ein Bußgeld zahlen und legt Einspruch ein. Richter Glaser am Amtsgericht hält das Gesetz für verfassungswidrig und für seine Entscheidung erheblich.
>
> **Wer kann mit welchem Verfahren nach Karlsruhe?**

Kein Fiktiv-Hinweis auf Karten und im Sprechtext (Vorgabe Kanalinhaber 01.10.2026).
