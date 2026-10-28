# Folge 032 · Verhältnismäßigkeit prüfen: Die 4 Schritte im Öffentlichen Recht – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_032.py`](src/skript_032.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Ein Übungsfall nach dem Hook des Themenplans trägt die vier Schritte: Um Graffiti zu stoppen, verbietet das Ordnungsamt per Allgemeinverfügung den Verkauf aller Spraydosen, auch Deo und Haarspray. Ablauf: Fall → Frage → Sachverhalt (mit Bearbeitervermerk: Ermächtigung unterstellt) → Herleitung (Wortlaut Art. 20 III GG; Rechtsstaatsprinzip und Wesen der Grundrechte) → Prüfungsort (Schranken-Schranken, Art. 12 I GG; Ermessensgrenze, Wortlaut § 40 VwVfG; § 15 BPolG als ausdrückliche Regelung) → 1. legitimer Zweck → 2. Geeignetheit → 3. Erforderlichkeit (Jugendliche ✗ gleich wirksam; nur Farbsprühdosen ✓) → Ergebnis rechtswidrig → Variante „nur Farbsprühdosen“ → 4. Angemessenheit (Maßstab, Abwägung) → Klausurtipp → Schema → Merksatz.
**Vertiefung gegenüber 020:** Dort war die Verhältnismäßigkeit ein Unterpunkt der Schranken-Schranken. Hier: Herleitung und Verfassungsrang, zwei Prüfungsorte (Grundrecht und Verwaltungsermessen), einfachgesetzliche Ausformung, je Schritt Definition, Argumentationsmuster und typischer Fehler, Einschätzungsspielraum, Abwägungsformel „je empfindlicher …, desto gewichtiger …“.
**Länge:** Hauptfilm rund 6:28 (5.460 gesprochene Zeichen). Mehr als fünf Minuten wegen der drei Wortlautkarten (Art. 20 III GG, § 40 VwVfG, § 15 I, II BPolG), der Herleitung mit zwei Prüfungsorten und der Variante, ohne die die Angemessenheit im Fall nicht zu erreichen wäre (der Ausgangsfall scheitert schon an der Erforderlichkeit).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Kühn (KU), um 50 | Inhaber eines Farbengeschäfts, Grundrechtsträger (Art. 12 I GG) | Pose `standing/pointing_finger-2` (schwarzer Pullover, Zeigefinger), Kopf `Short 3`, Brille `Glasses 2`; Hose Blau `#8DB3F2`, Haut `#E3B48C`; Mimiken `Smile` (ruhig), `Serious` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Cute` (froh), `Tired` (müde) | `christian` (Mann, mittel) |
| Frauke (FR), um 28 | Wandmalerin, Kundin | Pose `standing/easing-1` (offenes Hemd Grün `#8FD694`, Top Lila `#B8A9F5`, Turnschuhe), Kopf `Medium Bangs 2` (blond), Haut `#F1C6A5`; Mimiken `Smile`, `Serious` (redet), `Concerned|Serious`, `Suspicious`, `Cute` | `ela_warm` (Frau, jung) |
| Frau Dörr (DO), um 35 | Ordnungsamt | Pose `standing/blazer-2` (Jackett Blau `#8DB3F2`, Beinprothese im Original), Kopf `Medium Straight`, Haut `#D9A07A`; Mimiken `Serious` (ruhig/redet), `Solemn` (denkt) | `julia` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (im Laden: Kühn und Frauke zu Frau Dörr).
- **Alle Grundmimiken mit geschlossenem Mund**; `Calm` nicht verwendet (schließt bei diesen Köpfen die Augen). Mundzustände a/o/e nur in `KU_redet`, `FR_redet`, `DO_redet` (je links/rechts) und Lexi. Keine Bärte.
- Die Prothese der Pose `blazer-2` gehört zur Behördenmitarbeiterin (keine Täterrolle, kein Bezug zur Handlung).
- **Stimmen nur aus dem Pool** julia, christian, ela_warm, otto: verwendet christian, ela_warm, julia (otto „unsicher“, nicht nötig); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Kühn (Umlaut), Frauke, Dörr (Umlaut); nicht in der Liste früherer Namen.
- Figuren-PNGs: `../peeps/op_032/` (54 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_032.png`.

**Abweichung von den letzten Folgen:** 028 Marschlandschaft/Behördenzimmer/Lagekarte (Art. 8 GG), 020 Fußgängerzone mit Skateverbot (Art. 2 I GG). Hier: Altstadtstraße mit besprühter Hauswand und Ladenfront, Innenraum eines Farbengeschäfts mit Regal (Farbsprühdosen, Deo/Haarspray, Lackeimer) und Ladentür; Rückkehr in den Laden in der Variante bewusst (gleicher Ort, nur Farbsprühdosen gesperrt). Posen `pointing_finger-2`, `easing-1`, `blazer-2` in 023–031 nicht verwendet.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Altstadt** `fall`/`kuehn` | Haus, Ziegelwand mit Graffiti, Ladenfront, Sonne; Herr Kühn blickt zur Wand | tabler:`home` (Pink), ph:`wall` (Orange), ph:`scribble-loop` (Lila), ph:`scribble`, tabler:`sun`, `building-store` (Blau), `bucket`, `brush`, streamline-freehand:`color-spray` | `Fall · Graffiti in der Altstadt` (ab 0,0 s) | Straße · „über Nacht besprüht“ · Kühn · Schild · Lacke · Pinsel · Spraydosen · Kühn froh | – |
| **B Im Farbengeschäft / Die Frage** `frauke`–`frage` | Regal links, Kühn, Frauke, Tür rechts; Frau Dörr tritt ein, Allgemeinverfügung; Verbotszeichen über dem Regal | Regal als Karte, `color-spray` ×4, tabler:`perfume` ×4, `bucket` ×2, `door`, `brush`, `file-text`, `ban` | `Fall · Im Farbengeschäft` → `Fall · Die Frage` | Laden · Frauke · Pinsel · Dörr tritt ein · Allgemeinverfügung · Blase Dörr · Verbot · „alle Spraydosen“ · Blase Kühn · Deo · Haarspray · Blase Frauke · Frage · „4 Schritte“ | Ladenglocke (`szene_032tuerglocke_1`) |
| **C Sachverhalt** `sv` | Sachverhaltskarte vollständig mit Bearbeitervermerk, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D Wortlaut Art. 20 III** `herk`–`nicht` | Wortlautkarte, vorgelesen, Marker zum Wort; Kühn | `book` | `Herleitung · Woher kommt der Grundsatz?` → `› Wortlaut Art. 20 III GG` | Titel · Karte · sechs Marker · ✗ „steht da nicht“ | – |
| **E Herleitung** `rsp`–`rang` | Tafel; Frauke | fluent-hc:`classical-building`, `shield-check`, `book` | `Herleitung › Rechtsstaatsprinzip und Grundrechte` → `› Verfassungsrang` | sechs Zeilen zum Wort, Block | – |
| **F Prüfungsort** `ort`–`ermess` | Tafel; Kühn | `building-store`, `file-text` | `Prüfungsort › Grundrechte: Schranken-Schranken` → `› Art. 12 I GG, Berufsausübung` → `› Ermessen der Behörde` | sechs Zeilen zum Wort | – |
| **G Wortlaut § 40 VwVfG** `wl40`/`land` | Wortlautkarte, vorgelesen; Frau Dörr | `file-text` | `Prüfungsort › Ermessen, § 40 VwVfG` → `› Landesrecht und Verfassung` | Karte · drei Marker · zwei Zeilen | – |
| **H Wortlaut § 15 BPolG** `wl15`–`abs2` | Wortlautkarte Abs. 1 und 2, Merkmale markiert; Frau Dörr | `book` | `Prüfungsort › ausdrücklich geregelt: § 15 BPolG` | Karte · vier Marker | – |
| **I 1. legitimer Zweck** `s1`–`legit` | Tafel; Kühn | `shield-check`, ph:`wall`, `scribble-loop` | `Verhältnismäßigkeit · die vier Schritte` → `› 1. legitimer Zweck` | Titel · vier Zeilen · Block ✓ | – |
| **J 2. Geeignetheit** `s2`–`fehl1` | Tafel; Kühn widerspricht (Blase), denkt, müde | `world-www`, `building-store` | `Verhältnismäßigkeit › 2. Geeignetheit` | Definition · Blase · online · um die Ecke · Block ✓ · ✗ Fehler | – |
| **K 3. Erforderlichkeit** `s3`–`jung` | Tafel; Frauke | `color-spray`, `mood-kid` | `› 3. Erforderlichkeit` | Definition · beides · eindeutig · Spielraum · Jugendliche ✓ milder ✗ nicht gleich wirksam | – |
| **L engeres Verbot, Ergebnis** `farbe`–`erg1` | Tafel; Kühn (froh beim Ergebnis) | `color-spray`, `perfume` | `› 3. Erforderlichkeit › nur Farbsprühdosen?` → `Ergebnis: Verbot aller Spraydosen rechtswidrig` | Frage · Deo/Haarspray · ✓ ✓ · eindeutig · Block ✗ · rechtswidrig | – |
| **M Variante** `var`/`var2` | zurück im Laden: Frau Dörr tritt erneut ein, Verbotszeichen nur über der Reihe der Farbsprühdosen | wie B | `Gutachten · Prüfung beendet` → `Variante · nur Farbsprühdosen verboten` | Laden · Dörr · neues Verbot · drei Pillen · Kühn denkt | Ladenglocke (`szene_032tuerglocke_1`) |
| **N 4. Angemessenheit** `s4`/`je` | Tafel; Frauke | fluent-hc:`balance-scale` | `Variante › 4. Angemessenheit` | Maßstab in vier Zeilen · Je-desto-Formel | – |
| **O Abwägung** `last`–`abw` | Tafel; Kühn und Frauke nebeneinander, Frauke fragt (Blase) | – | `Variante › 4. Angemessenheit › Abwägung` → `Ergebnis Variante: eher unangemessen` | Last (drei Zeilen) · Blase · Nutzen (zwei Zeilen) · Block · vertretbar · gewichten | – |
| **P Klausurtipp** `tipp`–`t3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Aufbau` → `Klausurtipp · typische Fehler` | Konvention · ausführlich · drei Fehler | – |
| **Q Klausurschema** `sch`–`q4` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | Titel · Oberbegriff · 4 Schritte mit Unterzeilen einzeln | – |
| **R Merksatz** `merke`/`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb der Folien harte Schnitte und Pops; keine Bewegungen außer dem Auftritt von Frau Dörr.
**Geräusche:** ein Handlungsgeräusch (Ladenglocke beim Eintreten von Frau Dörr, zweimal), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> In der Altstadt werden über Nacht immer wieder Hauswände unerlaubt mit Graffiti besprüht. Das Ordnungsamt der Stadt erlässt deshalb eine Allgemeinverfügung: Ab sofort darf im Stadtgebiet niemand mehr Spraydosen verkaufen, und zwar alle, auch Deo und Haarspray. Herr Kühn betreibt ein Farbengeschäft. Frauke kauft dort Sprühfarbe für Wandbilder, die sie erlaubt malt. Gesprüht wird von Jugendlichen und Erwachsenen; viele Sprayer bestellen ihre Dosen ohnehin im Internet. Die meisten Kunden kaufen Sprühfarbe für erlaubte Zwecke.
>
> Bearbeitervermerk: Die Allgemeinverfügung stützt sich auf eine wirksame Ermächtigung zur Gefahrenabwehr, die Ermessen einräumt; ihre Voraussetzungen sind zu unterstellen. Zu prüfen ist nur die Verhältnismäßigkeit.
>
> **Ist das Verbot verhältnismäßig?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext (Vorgabe Kanalinhaber 01.10.2026).

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen in Ziffern („§ 303 II StGB“, „Art. 12 I GG“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Wortlautkarten sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe); die § 15-BPolG-Karte wird nicht vorgelesen, ihre Merkmale werden genannt und markiert.
