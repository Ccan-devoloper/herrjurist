# Folge 005 · Abstraktionsprinzip & Trennungsprinzip: Ein Kauf, drei Verträge – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_005.py`](src/skript_005.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Examenswissen (Mi), Themenplan-Format „Schema“. Einstieg mit dem Brötchenkauf aus dem Themenplan (drei Verträge, alles wirksam), danach ein frei erfundener Beispielfall, an dem die drei Verträge getrennt geprüft werden: Minderjähriger kauft einen Plattenspieler, die Eltern verweigern die Genehmigung. Ergebnis: Kaufvertrag unwirksam, Übereignung des Plattenspielers wirksam (Abstraktionsprinzip), Übereignung des Geldes unwirksam (Fehleridentität), Rückabwicklung über § 985 (Geld) und § 812 I 1 Alt. 1 (Plattenspieler).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Sandra (SA), um 45 | Kundin in der Bäckerei, Bens Mutter; verweigert für beide Eltern die Genehmigung | Posen derselben Reihe `-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`): `standing/pointing_finger-2` (zeigt/redet) und `standing/crossed_arms-2` (wartet/verärgert/zufrieden); Kopf `Long Bangs`; Haut `#E8B98F`; Mimiken `Calm`, `Smile` (redet), `Serious` (streng, redet), `Contempt` (verärgert), `Smile` | `sabrina` (Frau, mittel) |
| Hanne (HA), um 65 | Bäckermeisterin, Inhaberin, verkauft das Brötchen | `standing/doctor-nurse-02` als weißer Bäckerkittel (ohne Haube, ohne Stethoskop), Originalfarben; Kopf `Gray Medium`, Haar grau `#C9C9C9`, Brille `Glasses 3`; Haut `#D9A07A`; Mimiken `Calm`, `Serious` (redet), `Smile` | `elinor` (Frau, älter, „ruppige Tante“: kurz angebunden „Sechzig Cent.“) |
| Ben (BE), 17 | Käufer des Plattenspielers, beschränkt geschäftsfähig | `standing/shirt-3`, Hemd Grün `#8FD694`, schwarze Hose; Kopf `Short 5`; Haut `#C99470`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile` (froh, Mund zu), `Concerned|Serious` (ertappt, Mund zu), `Serious` (denkt), `Tired` (müde) | `niklas` (Mann, jung) |
| Walter (WA), um 70 | Nachbar, Verkäufer des Plattenspielers | `standing/robot_dance-2` (übergibt mit offener Hand), schwarzes Oberteil, Hose Braun `#9C7A5B`; Kopf `No Hair 2`, Brille `Glasses 4`; Haut `#F0C8A8`; Mimiken `Old` (ruhig), `Smile` (redet), `Serious` (fordert, redet), `Contempt` (verärgert), `Suspicious` (denkt) | `helmut` (Mann, älter) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts. Die Grundansicht ist gespiegelt und blickt nach links zur Tafel; `_r` blickt nach rechts (Hanne hinter der Theke zu Sandra, Walter an seiner Tür zu Ben). Keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` nicht gewählt). Grundmimiken mit offenem Mund werden als „Augen|Mund“ mit geschlossenem Mund gesetzt (Befund Folge 004). Stimmen ausschließlich aus dem für diese Folge zugeteilten Pool (sabrina, niklas, elinor, helmut); keine Überschneidung mit 003 (lisa, marc, ela_froh) und 004 (laura_klar, christian, julia, william). Figuren-PNGs: `../peeps/op_005/` (88 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 003: Flohmarkt bei Tag, Greta/Paul/Mia. 004: Ministerbüro, Parteizentrale, Parteitagsbühne. 002 (ebenfalls Kauf mit Anfechtung): Wohnzimmer/Garage, Erklärungsirrtum.
- 005: Bäckerei mit Theke und Auslage, Haustür des Nachbarn; Unwirksamkeitsgrund bewusst **nicht** wieder die Anfechtung (wie 002), sondern Minderjährigenrecht (§§ 107, 108 BGB). Tageslicht, Cremegrund durchgehend.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Bäckerei** `baeck`→`drei` | Bodenlinie; Theke (Pastellblock Orange) mit Auslage, Hanne dahinter (blickt nach rechts), Sandra kommt von rechts | fluent-hc:`croissant`, `pretzel`, `bread` (Gelb, = Roggenbrötchen), ph:`cash-register` (Blau), tabler:`coins` (Gelb), tabler:`paper-bag` (Weiß) | `Fall · Beim Bäcker` | 1 Theke, Hanne · 2 Sandra zeigt · 3 Sandra redet, Blase „Ein Roggenbrötchen, bitte.“, Pille „Roggenbrötchen“ · 4 Hanne redet, Blase „Sechzig Cent.“, Pille „0,60 €“ · 5 Münzen auf der Theke · 6 Brötchen weg, Tüte in Sandras Hand · 7 „1 Kauf = 3 Verträge“ | Münzen auf Theke (A5) |
| **B Drei Verträge** `kv`→`verf` | Tafel links, Hanne und Sandra rechts | tabler:`file-text` (Kaufvertrag), fluent-hc:`bread` mit Pfeil Hanne→Sandra, tabler:`coins` mit Pfeil Sandra→Hanne | `Ein Kauf, drei Verträge › 1. Kaufvertrag, § 433 BGB` → `› 2. Übereignung Brötchen, § 929 S. 1 BGB` → `› 3. Übereignung Münzen, § 929 S. 1 BGB` | 1 Kaufvertrag · 2 Pflichten Hanne · 3 Pflicht Sandra · 4 „Verpflichtungsgeschäft“ · 5 Übereignung Brötchen + Icon · 6 Einigung + Übergabe, Pfeil · 7 Übereignung Münzen · 8 Pfeil zurück · 9 Block „Verfügungsgeschäfte“, Sandra zufrieden | – |
| **C Trennung/Abstraktion** `trenn`→`spannend` | Tafel links, rechts Kaufvertrag und Übereignungen als Icons | tabler:`file-text`, fluent-hc:`bread`, tabler:`coins`, tabler:`link-off` | `Trennungsprinzip` → `Abstraktionsprinzip` | 1 Trennungsprinzip · 2–3 Definition, Trennstrich · 4 Abstraktionsprinzip · 5–6 Definition, „unabhängig wirksam“ · 7 „Und wenn der Kaufvertrag scheitert?“, Kreuz am Kaufvertrag, „?“ | – |
| **D Walters Haustür** `ben`→`frage` | Bodenlinie; links Walters Tür, Walter blickt nach rechts; Ben kommt; Plattenspieler und Geldscheine wechseln die Hände; Sandra kommt dazu | tabler:`door` (Rot), tabler:`vinyl` (Plattenspieler), tabler:`cash-banknote` (Grün), tabler:`steering-wheel` (Führerschein) | `Fall · Der Plattenspieler` → `Fall · Die Eltern sagen Nein` | 1 Walter an der Tür · 2 Ben kommt, „Ben, 17“ · 3 Plattenspieler, „120 €“ · 4 Ben redet mit Scheinen, Blase · 5 Walter redet, Scheine wandern zu Walter, Plattenspieler zu Ben, Ben froh · 6 Lenkrad, „Geld der Eltern: für den Führerschein“ · 7 Sandra kommt · 8 Sandra redet streng, Blase, Ben ertappt, Walter verärgert · 9 Walter fordert, Blase · 10 Frage-Pillen | Geldscheine (D4) |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **F 1. Kaufvertrag** `v1`→`verweigert` | Tafel links, Ben und Sandra rechts | tabler:`steering-wheel` | `1. Kaufvertrag Ben–Walter, § 433 BGB › beschränkte Geschäftsfähigkeit` → `› rechtlich nachteilig, § 107 BGB` → `› § 110 BGB?` → `› § 108 I BGB: unwirksam` | 1 Tafel + Leiste der drei Verträge · 2 §§ 2, 106 · 3 nachteilig · 4 § 107 · 5 § 110 ✗ + Lenkrad · 6 Führerschein-Zeile · 7 schwebend unwirksam · 8 Block „endgültig unwirksam“, Ben ertappt, Sandra verärgert | – |
| **G 2. Übereignung Plattenspieler** `v2`→`eig` | Tafel links, Walter und Ben rechts, Plattenspieler über Ben | tabler:`vinyl` | `2. Übereignung Plattenspieler, § 929 S. 1 BGB › Einigung, Übergabe` → `› lediglich rechtlicher Vorteil, § 107 BGB` → `› Abstraktionsprinzip` | 1 Tafel · 2 Einigung ✓ · 3 Übergabe ✓ · 4 nur Eigentum ✓ · 5 lediglich rechtlicher Vorteil · 6 „Spielt keine Rolle“, Walter verärgert · 7 Pille Abstraktionsprinzip · 8 BGH-Zitat V ZB 13/04 · 9 Block „Ben ist Eigentümer“, Ben froh | – |
| **H 3. Übereignung Geld** `v3`→`geld_unw` | Tafel links, Walter und Ben, Geldschein über Walter | tabler:`cash-banknote` | `3. Übereignung Geld, § 929 S. 1 BGB › rechtlich nachteilig` | 1 Tafel · 2 Eigentumsverlust · 3 nachteilig · 4 keine Zustimmung ✗ · 5 Block „unwirksam, §§ 107, 108 I“, Kreuz am Schein, Ben ertappt | – |
| **I Fehleridentität** `fi`→`fi3` | Tafel links, rechts Übersicht der drei Geschäfte | tabler:`file-text`, `vinyl`, `cash-banknote` | `3. Übereignung Geld › Fehleridentität` | 1 Übersicht ✗/✓/✗ · 2 „nicht: weil der Kaufvertrag scheitert“ · 3 „sondern: derselbe Fehler …“ · 4 Ring um Geld · 5 Pille Fehleridentität · 6–7 keine Durchbrechung · 8 Block Geschäftsunfähigkeit § 105 I | – |
| **J Rückabwicklung Geld** `rueck`→`geld_zur` | Tafel links, Walter und Ben | tabler:`cash-banknote` wandert von Walter zu Ben | `Rückabwicklung › Geld: § 985 BGB` | 1 Tafel · 2 Ben Eigentümer ✓ · 3 „solange …“ · 4 Block § 985 · 5 Schein wandert zu Ben | – |
| **K Rückabwicklung Plattenspieler** `w985`→`rf` | wie J | tabler:`vinyl` wandert von Ben zu Walter | `Rückabwicklung › Plattenspieler: § 985 BGB?` → `› Plattenspieler: § 812 I 1 Alt. 1 BGB` | 1 § 985 ✗, Walter verärgert · 2 § 812 · 3 erlangt ✓ · 4 Leistung ✓ · 5 ohne Rechtsgrund ✓ · 6 Block Rückübereignung, Plattenspieler wandert, Ben müde | – |
| **L Klausurtipp** `tipp` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst § 985, jede Übereignung einzeln` | 1–4 Zeilen nacheinander | – |
| **M Klausurschema** `sch`→`k10` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | 1 Titel · 2 A. · 3 I. · 4 II. · 5 1. · 6 2. · 7 III. · 8 B. · 9 I. · 10 II. · 11 III. · 12 IV. | – |
| **N Merksatz** `merke` | Lexi erklärt, Merksatz mit Marker | – | `Merksatz` | 1 · 2 · 3 · 4 | – |

**Übergänge:** stumme Schiebeblenden zwischen allen 14 Folien, innerhalb der Folien harte Schnitte, Pops und kurze Bewegungen (Scheine/Plattenspieler wechseln die Hände).

**Geräusche:** zwei Handlungsgeräusche (Münzen auf der Theke, Geldscheine an der Haustür), Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json); Dateien mit Folgennummer (`szene_005…`).

**Sprechblasen:** Blasentext wortgleich mit dem Gesprochenen (Zahlen als Wort: „Hier sind hundertzwanzig Euro, bar.“). Tafeln und Pillen dürfen Ziffern verwenden („120 €“, „0,60 €“).

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Der 17-jährige Ben kauft seinem Nachbarn Walter dessen alten Plattenspieler für 120 Euro ab. Er zahlt bar mit Geld, das ihm seine Eltern für den Führerschein gegeben haben. Walter übergibt den Plattenspieler und legt die Scheine in eine Schublade.
>
> Als Ben zu Hause davon erzählt, geht seine Mutter Sandra zu Walter und erklärt für beide Eltern: „Den Kauf genehmigen wir nicht! Wir wollen das Geld zurück.“ Walter verlangt daraufhin den Plattenspieler zurück.
>
> *(Frei erfundener Übungsfall.)*
>
> **Wem gehören Plattenspieler und Geld – und wie kommt beides zurück?**
