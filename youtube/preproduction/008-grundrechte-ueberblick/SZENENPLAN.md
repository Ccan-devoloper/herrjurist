# Folge 008 · Grundrechte Überblick: Freiheitsrechte, Gleichheitsrechte, Prüfung – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_008.py`](src/skript_008.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Examenswissen (Mi), Themenplan-Format „Schema“. Ein frei erfundener, länderneutraler Alltagsfall trägt beide Prüfungen: Eine Stadt verbietet per Parksatzung Verkaufswagen im Stadtpark; die Eisverkäuferin Lina verliert ihren Standort, der feste Kiosk am Teich verkauft weiter. Welches Grundrecht passt? → A. Freiheitsrecht Art. 12 I GG (Schutzbereich – Eingriff – Rechtfertigung: Schranke, Verhältnismäßigkeit) → B. Gleichheitsrecht Art. 3 I GG (Ungleichbehandlung – Rechtfertigung) → Ergebnis, Gegenfall (nur Eiswagen verboten), Klausurtipp (Reihenfolge, Art. 94 I Nr. 4a GG), Schema, Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Lina (LI), um 30 | Eisverkäuferin, Grundrechtsträgerin | Pose `standing/easing-1`, Kopf `Long Curly`; Jacke Rosa `#F6A5C0`, Oberteil Weiß, Haut `#E0AC84`; Mimiken `Calm` (ruhig), `Smile` (froh), `Fear` (Schreck), `Driven` (redet), `Serious` (denkt), `Contempt` (verärgert), `Tired` (müde) – alle mit geschlossenem Mund | `sabrina` (Frau, mittel) |
| Tom (TO), um 28 | Mitarbeiter des Ordnungsamts, verkündet die Satzung | Pose `standing/blazer-4`, Kopf `Short 3`; Jackett Blau `#8DB3F2`, Oberteil Weiß, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet) | `niklas` (Mann, jung) |
| Frau Kranz (KR), um 70 | Spaziergängerin, steht für den Satzungszweck | Pose `standing/walking-1`, Kopf `Gray Bun`, Brille `Glasses 4`; Oberteil Lila `#B8A9F5`, Haut `#EBC4A0`; Mimiken `Calm`, `Driven` (redet), `Smile` | `hilde` (Frau, älter) |
| Herr Brenner (BR), um 55 | Kioskbetreiber, Vergleichsgruppe | Pose `standing/shirt-3`, Kopf `No Hair 1`, Bart `Goatee 1`; Hemd Türkis `#7FD6D0`, Haut `#A86B48`; Mimiken `Calm`, `Smile` (redet/froh) | `christian` (Mann, mittel) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Lina in Szene A zu Tom, Brenner in Szene C zu Lina). Keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` nicht gewählt). **Alle Grundmimiken mit geschlossenem Mund** (FOLGE-ABLAUF); Mundzustände a/o/e nur in den sprechenden Ansichten `LI_redet`, `TO_redet`, `KR_redet`, `BR_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (sabrina, niklas, hilde, christian); keine Überschneidung mit 006 (william, ela_warm, timo) und 007 (marc, laura_klar, julia). Figuren-PNGs: `../peeps/op_008/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 006: Anspruchsaufbau, 007: Haus/Nacht (Haustyrann). 004 (letzte öffentlich-rechtliche Folge): Ministerbüro, Parteitag.
- 008: Stadtpark bei Tag mit Eiswagen, Wiese, Teich und Kiosk; erstmals eine Grundrechtsprüfung (Verfassungsbeschwerde-Begründetheit) statt Organstreit; vier neue Figuren, zwei Frauen. Cremegrund durchgehend.
- Landesrecht: nur als unterstellte Ermächtigungsgrundlage („Landesrecht“), kein Land genannt.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Stadtpark** `fall`→`t1` | Bodenlinie, Eiswagen links, Lina daneben (blickt zu Tom), Tom kommt von rechts | tabler:`truck` (Rosa) + `ice-cream` (Gelb), `tree`/`trees` (Grün), `bell` (Gelb), `coins` (Gelb), `file-text` (Weiß), `truck-off` (Rot) | `Fall · Im Stadtpark` | 1 Park · 2 Eiswagen, Lina froh, Glocke · 3 Münzen „ihr Lebensunterhalt“ · 4 Tom kommt · 5 Tom redet, Blase, Satzung · 6 Lina erschrickt · 7 Verbotszeichen | Handglocke (Lina läutet) |
| **B Der Grund** `grund`→`k1` | Wiese, ein blauer Verkaufswagen fährt quer darüber, Spuren, Frau Kranz | tabler:`truck` (Blau), `tree`; Wiese als Pastellblock, Reifenspuren als Linienzug | `Fall · Der Grund` | 1 Wiese, Kranz · 2 Wagen fährt · 3 „kreuz und quer …“ · 4 Spuren · 5 „tiefe Spuren im Rasen“ · 6 „Spaziergänger müssen ausweichen“ · 7 Kranz redet, Blase | fahrender Wagen |
| **C Der Kiosk** `kiosk`→`frage` | Teich, Kiosk, Brenner (blickt zu Lina), Lina rechts | tabler:`ripple` (Blau), `building-store` (Türkis), `ice-cream` | `Fall · Der Kiosk` → `Fall · Die Frage` | 1 Kiosk, „Kiosk: Eis erlaubt“ · 2 Brenner redet, Blase „Mein Kiosk fährt ja nirgendwohin.“ · 3 Lina redet, Blase · 4 Frage-Pille · 5–6 „Freiheitsrecht?“/„Gleichheitsrecht?“ | – |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 10 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **E Grundrechtskatalog** `katalog`→`bind` | Tafel links, Lina rechts | tabler:`pray`, `message`, `users-group`, `briefcase`, `shield`, `scale`, `building-bank` | `Welches Grundrecht passt?` → `› Freiheitsrechte` → `› Gleichheitsrechte` → `› Bindung, Art. 1 III GG` | Art. 4/5/8/12 einzeln zum Wort · Block Freiheitsrechte · Block Gleichheitsrechte · Art. 1 III · Rathaus „Stadt“ | – |
| **F Welches Grundrecht passt?** `passt`→`passt2` | Tafel, Lina | `briefcase`, `building-store`, `equal-not` | `… › Art. 12 I GG` → `… › Art. 3 I GG` | Art. 12 (✓) · spezieller als Art. 2 I · Block A · Art. 3 I (✓) · Block B · Kiosk ≠ | – |
| **G A. I. Schutzbereich** `sb`→`sb_s` | Tafel, Lina | tabler:`id`, `world`, `building-store`, Eiswagen, `coins` | `A. Berufsfreiheit, Art. 12 I GG › I. Schutzbereich` → `› persönlich` → `› sachlich` | „Alle Deutschen“ · Lina Deutsche (✓) · Ausländer Art. 2 I · GmbH Art. 19 III · Beruf, Definition · Lina lebt davon (✓) · „Schutzbereich eröffnet“ | – |
| **H A. II. Eingriff** `ein` | Tafel, Lina müde | `file-text` „Parksatzung“, `truck-off` | `A. … › II. Eingriff` | Satzung · regelt das Wo · Eingriff (+) | – |
| **I A. III. Rechtfertigung** `rf`→`geeignet` | Tafel; rechts Rathaus „Landesrecht“, Waage, dann Frau Kranz + Lina mit Pflanze | `building-bank`, `scale`, `plant`, `truck-off` | `A. … › III. Rechtfertigung` → `› 1. Schranke, Art. 12 I 2 GG` → `› 2. Verhältnismäßigkeit` → `› legitimer Zweck` → `› geeignet` | Schranke · Landesrecht (unterstellt) · VHM · Zweck (✓) · geeignet (✓) | – |
| **J A. III. 2. Erforderlichkeit, Angemessenheit** `erf`→`erg1` | Tafel; rechts Alternative „nur Wiese gesperrt“: Wagen auf dem Weg vor Frau Kranz; dann Waage „Lina: ein Standort“ / „viele Spaziergänger“ | `truck-off`, `truck`, `scale`; Wiese/Weg als Pastellblöcke | `… › erforderlich` → `› angemessen` → `A. … › nicht verletzt` | erforderlich (✓) · Alternative (✗) · angemessen (✓) · drei Abwägungszeilen · Ergebnisblock A | – |
| **K B. Ungleichbehandlung** `gl`→`ungl` | Tafel; Lina und Brenner | `ice-cream`, Kreuz/Haken | `B. Gleichheit, Art. 3 I GG` → `› I. Ungleichbehandlung` | zwei Schritte · Vergleichsgruppe · beide verkaufen Eis · Kiosk ✓ / Lina ✗ | – |
| **L B. II. Rechtfertigung** `rf3`→`erg2` | Tafel; Kiosk und Eiswagen | `building-store`, `truck`, `scale`; Maßstabsleiste Willkürverbot → strenge VHM | `… › II. Rechtfertigung` → `› Maßstab` → `› Sachgrund` → `B. … › nicht verletzt` | Sachgrund-Formel · Maßstab · strenger möglich · „steht fest“/„fährt“ · Ergebnisblock B | – |
| **M Ergebnis, Gegenfall** `ergebnis`→`gegen2` | Tafel; Eiswagen ✗ und Kaffeewagen ✓, „=“ | Eiswagen, tabler:`truck` (Blau) + `coffee`, `equal` | `Ergebnis` → `Gegenfall · nur Eiswagen verboten` | Ergebnisblock · Gegenfall · Kaffeewagen · kein Unterschied · Art. 3 I verletzt (✗) | – |
| **N Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Prüfungsreihenfolge` → `Klausurtipp · Art. 94 I Nr. 4a GG` | Reihenfolge · Art. 2 I subsidiär · Verfassungsbeschwerde · Art. 94 I Nr. 4a · BVerfGG · früher Art. 93 | – |
| **O Klausurschema** `sch`→`sB2` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | A · I · II · III · 1. · 2. · B · I · II · Maßstab | – |
| **P Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb der Folien harte Schnitte und Pops; eine Bewegung (Verkaufswagen fährt in Szene B).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_008glocke_1`, `szene_008wagen_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Lina, eine Deutsche, verkauft seit Jahren im Sommer Eis aus ihrem Verkaufswagen im Stadtpark; davon lebt sie. Weil Verkaufswagen im letzten Sommer kreuz und quer über Wege und Wiesen fuhren, tiefe Spuren im Rasen hinterließen und Spaziergänger ausweichen mussten, erlässt die Stadt eine neue Parksatzung: Ab Montag dürfen Verkaufswagen nicht mehr in den Park fahren; der Verkauf aus Fahrzeugen im Park ist verboten. Der fest gebaute Kiosk am Teich darf weiter Eis verkaufen. Lina meint: „Das ist mein Beruf! Und der Kiosk verkauft dasselbe Eis wie ich!“
>
> Annahme: Die Satzung beruht auf einer wirksamen landesrechtlichen Grundlage und ist formell rechtmäßig.
>
> **Verletzt das Verbot Lina in ihren Grundrechten?**
