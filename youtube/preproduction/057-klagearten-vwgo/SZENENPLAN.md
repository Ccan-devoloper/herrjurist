# Folge 057 · Klagearten VwGO: Welche Klage passt? Der komplette Überblick – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_057.py`](src/skript_057.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“. Ein Übungsfall nach dem Hook des Themenplans („Bescheid aufheben, Genehmigung erzwingen, Äußerung stoppen, Rechtslage klären – vier Ziele, vier Klagen“) trägt den Film: Frau Behrens (Bootsverleih am See) bekommt vom Bauamt einen Bescheid (Steg muss weg, Kiosk abgelehnt), Bürgermeister Harms schreibt auf der Internetseite der Stadt, ihre Boote seien nicht sicher, und Herr Lindemann vom Ordnungsamt verlangt für die Elektroboote eine Erlaubnis. Zwei Abwandlungen: Verbot für das Seefest-Wochenende, das sich nach Klageerhebung erledigt; Bebauungsplan ohne Kioske am Ufer. Ablauf: Fall → Frage → Sachverhalt → § 88 (Begehren) und § 40 (Rechtsweg, ein Satz) → Wortlaut § 42 I → 1. Anfechtungsklage → 2. Verpflichtungsklage (Versagungsgegen-/Untätigkeitsklage) → 3. allgemeine Leistungsklage → 4. Feststellungsklage (Wortlaut § 43 I, Rechtsverhältnis, Wortlaut § 43 II 1, Subsidiarität) → Ergebnis → Abwandlung 1 mit Wortlaut § 113 I 4 (Fortsetzungsfeststellungsklage) → Abwandlung 2 (Normenkontrolle § 47) → Klausurtipp → Klausurschema als Entscheidungsbaum → Merksatz.
**Länge:** Hauptfilm 6:55,9 (5.794 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Behrens (BE), um 45 | betreibt einen Bootsverleih am See, Klägerin in allen Fällen | Pose `standing/walking-3` (schwarzes Outfit, gehend), Kopf `Long`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Driven` (redet, entschlossen), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Cute` (froh) | `sabrina` (Frau, mittel) |
| Frau Thiele (TH), um 40 | Sachbearbeiterin im Bauamt | Pose `standing/resting-2`, Kopf `Medium Bangs`, Brille `Glasses`, blaue Hose `#8DB3F2`, Haut `#F0C8A8`; Mimik `Serious` (ruhig/redet) | `laura_ruhig` (Frau, mittel) |
| Bürgermeister Harms (HA), um 62 | Bürgermeister, Satz auf der Internetseite | Pose `standing/blazer-4` (dunkelblaues Jackett `#3D4A7A`), Kopf `No Hair 2` mit grauem Haarkranz `#9A9AA6`, Haut `#E6B48F`; Mimiken `Calm` (ruhig), `Serious` (redet) | `william` (Mann, älter) |
| Herr Lindemann (LI), um 45 | Ordnungsamt | Pose `standing/easing-1` (hellblaues Hemd), Kopf `Short 2`, Haut `#D9A07A`; Mimiken `Serious` (ruhig/redet), `Solemn` (denkt) | `marc` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. In den Fallszenen am Ufer blickt Frau Behrens nach rechts zu Frau Thiele bzw. Herrn Lindemann, die nach links zu ihr blicken; auf der Internetseiten-Szene blickt Harms nach links zur Internetseite und zu Frau Behrens, sie nach rechts zu ihm; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BE_redet`, `TH_redet`, `HA_redet`, `LI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet).
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig (alle vier verwendet); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Behrens, Thiele, Harms, Lindemann (nicht in der Liste früherer Namen; `grep` über alle Folgen ohne Treffer; „Albers“ wegen Folge 006 verworfen). Genitive vermieden („die Boote von Frau Behrens“).
- Figuren-PNGs: `../peeps/op_057/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 056 (Lernplatz, Zimmerwand), 055 (Supermarkt), 054 (Wohnung, Gerichtsvollzieher), 049 (Café, Förderstelle), 044 (Marktplatz, Rathaus). Hier erstmals ein **Seeufer**: Wasserfläche mit Wellen (Tabler ripple), Holzsteg mit Pfosten, Tretboote (Fluent canoe), Elektroboote (Tabler speedboat mit Blitz), Kiosk (Tabler building-store), Internetseite der Stadt als Browserfenster, Seefest mit Fahnen und Konfetti. Das Ufer kehrt in Szene C und N wieder, weil die Geschichte am selben Bootsverleih spielt. Posen: `walking-3` in 040–056 nicht verwendet; `resting-2` zuletzt 054, `blazer-4` zuletzt 048, `easing-1` zuletzt 053 – jeweils mit anderem Kopf, anderen Farben und anderer Rolle.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht; „Abends“ nur als Pille).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Seeufer** `fall`–`be1` | Ufer mit Steg und zwei Tretbooten, Baum, Sonne; Frau Thiele bringt den Bescheid; Kreuz am Steg, Kiosk mit Kreuz | Baustein Wasser/Steg (`karte`, `linienzug`), tabler:`ripple`, fluent-hc:`canoe` (Gelb/Rot), tabler:`sun`, `tree`, `file-text`, `building-store` | `Fall · Der Bootsverleih am See` (ab 0,0 s) → `Fall · Post vom Bauamt` | Ufer · Sorge · Thiele · Bescheid · Blase · Steg ✗ · Kiosk ✗ · Blase Behrens | Papier (`szene_057brief_1`) beim Bescheid |
| **B Internetseite** `netz`–`be2` | Browserfenster „Internetseite der Stadt“; Harms; Frau Behrens reagiert | Baustein Browser (`karte`) | `Fall · Ein Satz auf der Internetseite` | Abends · Fenster · Harms · Blase · Zitat · Behrens · Blase | – |
| **C Elektroboote** `lindemann`–`be3` | Ufer wie A; Lindemann; Tretboote werden zu Elektrobooten | tabler:`speedboat` (Blau/Grün), `bolt` | `Fall · Die neuen Elektroboote` | Ufer · Lindemann · Boote · Erlaubnis? · Blasen | – |
| **D Die Frage** `frage`–`frage3` | vier Ziele nebeneinander | `file-text`, `building-store`, `browser`, `speedboat` | `Fall · Vier Ziele, vier Klagen` → `Fall · Welche Klage passt wann?` | vier Ziele einzeln · Titel · Frage · erledigt? · Satzung? | – |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **F Begehren/Rechtsweg** `wl88`–`rweg` | Wortlautkarte § 88, vorgelesen; Rechtsweg | tabler:`target`, fluent-hc:`classical-building` | `Statthafte Klageart › Klagebegehren, § 88 VwGO` → `Vorab › Verwaltungsrechtsweg, § 40 I VwGO` | Karte · Marker · Ziel · Rechtsweg · ✓ | – |
| **G Wortlaut § 42 I** `wl42` | Wortlautkarte, vorgelesen, sechs Marker | `file-text` | `Statthafte Klageart › § 42 I VwGO` | Karte · Marker · zwei Pillen | – |
| **H 1. Anfechtungsklage** `anf`–`anf3` | Tafel; Bescheid mit Kreuz | `file-text` | `… › 1. Steg: Anfechtungsklage, § 42 I Alt. 1` | Zeilen zum Wort, Block, ✗ am Bescheid | – |
| **I 2. Verpflichtungsklage** `vpf`–`vpf3` | Tafel; Frau Thiele | `building-store`, `calendar`, `gavel` | `… › 2. Kiosk: Verpflichtungsklage, § 42 I Alt. 2` → `… › Untätigkeitsklage, § 75 VwGO` | Ziel · Block · Versagungsgegenklage · Untätigkeit · 3 Monate · Erfolg | – |
| **J 3. allgemeine Leistungsklage** `leist`–`leist4` | Tafel; Harms | `browser` | `… › 3. Internetseite: allgemeine Leistungsklage` | kein VA · Block · vorausgesetzt · Erfolg | – |
| **K 4. Feststellungsklage** `wl43`–`rv2` | Wortlautkarte § 43 I, vorgelesen; Rechtsverhältnis; Lindemann | `speedboat` | `… › 4. Elektroboote: Feststellungsklage, § 43 I` | Karte · Marker · Definition · Erlaubnis? | – |
| **L Subsidiarität** `wl432`–`subs2` | Wortlautkarte § 43 II 1, vorgelesen; Behrens | `file-text`, `speedboat` | `… › 4. Elektroboote › Subsidiarität, § 43 II` | Karte · Marker · ✗ Bescheid · ✓ Feststellung | – |
| **M Ergebnis** `erg`–`e4` | vier Ziele wie D mit Haken und Klageart | wie D | `Ergebnis Ausgangsfall` | vier Haken nacheinander | – |
| **N Abwandlung 1** `seefest`–`vorbei` | Ufer mit Seefest (Fahnen, Konfetti); Lindemann verbietet; Klage; Seefest vorbei | tabler:`flag`, fluent-hc:`confetti-ball`, tabler:`gavel`, `calendar-x` | `Abwandlung 1 · Das Seefest-Verbot` | Seefest · Lindemann · Blase · Klage · vorbei · erledigt | – |
| **O § 113 I 4** `wl113`–`ffk2` | Wortlautkarte, vorgelesen; Block FFK; Wiederholungsgefahr | `calendar-x`, `flag` | `Abwandlung 1 › Fortsetzungsfeststellungsklage, § 113 I 4` | Karte · Marker · Block · Interesse · jedes Jahr | – |
| **P Abwandlung 2** `bplan`–`nk5` | Tafel Normenkontrolle; Behrens | ph:`map-trifold`, `building-store`, fluent-hc:`classical-building`, `calendar`, `users` | `Abwandlung 2 · Bebauungsplan` → `Abwandlung 2 › Normenkontrolle, § 47 VwGO` | Plan · Satzung · Block · OVG · Frist · Landesrecht · für alle | – |
| **Q Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Statthafte Klageart` | drei Hinweise | – |
| **R Klausurschema** `sch`–`q8` | Entscheidungsbaum baut sich auf | – | `Klausurschema · Entscheidungsbaum` | Titel · Konvention · 4 Stufen mit 5 Ästen | – |
| **S Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Papier, wenn Frau Thiele den Bescheid überreicht), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Weitere Geräusche bewusst weggelassen (keine sichtbare Handlung mit passendem Klang).
**Wasser, Steg, Browserfenster:** als Bausteine (`karte`, `linienzug`) in Palettenfarben, kein Icon umgezeichnet.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Frau Behrens betreibt einen Bootsverleih am See. Frau Thiele vom Bauamt übergibt ihr einen Bescheid: Der Steg muss bis Monatsende beseitigt werden, und der beantragte Kiosk wird nicht genehmigt. Bürgermeister Harms schreibt auf der Internetseite der Stadt, ihre Boote seien nicht sicher. Herr Lindemann vom Ordnungsamt meint, für ihre neuen Elektroboote brauche sie eine Erlaubnis; sie hält das für falsch.
>
> Abwandlung 1: Herr Lindemann verbietet ihr, am Seefest-Wochenende Boote zu vermieten. Sie klagt, dann ist das Seefest vorbei.
>
> Abwandlung 2: Die Gemeinde beschließt einen Bebauungsplan: Am Ufer sind keine Kioske zulässig.
>
> **Welche Klage ist jeweils statthaft?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen in Ziffern („§ 42 I Alt. 1 VwGO“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Alle fünf Wortlautkarten (§ 88, § 42 I, § 43 I, § 43 II 1, § 113 I 4) werden vorgelesen; Klammerbegriffe („(Anfechtungsklage)“) werden ohne Klammer gesprochen, „(Feststellungsklage)“ in § 43 I nicht.
