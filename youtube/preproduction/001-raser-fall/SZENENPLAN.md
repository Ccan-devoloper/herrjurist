# Folge 001 · Raser-Fall: Mord mit dem Auto? – Szenenplan (Entwurf zur Freigabe)

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`skript_raser.py`](skript_raser.py)

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Jonas (JO), Mitte 20 | Fahrer, der den Geländewagen rammt (entspricht dem Angeklagten H.) | Pose `standing/blazer-4`, Kopf `Short 4`; rotes Jackett `#F07A6A`, Haut `#E8B98F`; Mimiken `Cheeky` (lässig), `Suspicious` (redet), `Fear` (Schock), `Tired` (Gericht) | `timo` (Mann, jung) |
| Max (MX), Mitte 20 | zweiter Raser, keine Kollision (entspricht N.) | Pose `standing/shirt-4`, Kopf `Flat Top`, Bart `Goatee 1`; hellblaue Hose `#8DB3F2`, Haut `#C99470`; Mimiken `Calm`, `Smile` (redet), `Serious` | `niklas` (Mann, jung) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Das Opfer wird nicht als Figur gezeigt, sondern nur als Geländewagen-Icon. Das ist eine bewusste Entscheidung: ein realer Todesfall, kein Opfer als Comicfigur.

Vorschau der Figuren: `besetzung_001.png` (nicht im Repository, Drive-Master).

**Abweichung von den letzten Folgen:**
- Katzenkönig hatte vier Figuren in Wohnung und Laden.
- Hier gibt es zwei neue Figuren in einer Straßenszene.
- Kein Innenraum.

## Szenen

**Nacht ist begründet:** Die Tat geschah gegen 0:50 Uhr. Szenen A und B nutzen den Nachtverlauf wie `hintergrund("nacht")` im Katzenkönig. Ab Szene C gilt der Cremegrund.

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Ampel** `nacht`→`m1` | Innenstadtboulevard bei Nacht; JO und MX stehen neben ihren Wagen an der roten Ampel und verabreden das Rennen; dann allein die Autos, Ampel grün, Abfahrt | tabler:`buildings` als Silhouette am Boden (Blau), tabler:`traffic-lights` (rot gefüllt → grün), tabler:`car` ×2 (JO Rot, MX Blau), tabler:`moon-stars` (Gelb) | Prüfpfad `Fall · Das Rennen` | 1 Ankunft (beide `cool`) · 2 JO redet, Blase „Bis zum Ende vom Boulevard. Wer zuerst da ist?“ · 3 MX redet, Blase „Abgemacht!“ · 4 Figuren weg (eingestiegen), Ampel grün · 5 Autos fahren nach rechts (`weg`), Pille „mehrere Kreuzungen, rote Ampeln“ | Motoraufheulen bei Abfahrt (A5) |
| **B Kreuzung** `kreuzung`→`frage` | Letzte Kreuzung; JO fährt bei Rot ein, von rechts der Geländewagen bei Grün; Kollision; danach JO neben dem Wrack | tabler:`car` (Rot), tabler:`car-suv` (Grau), tabler:`traffic-lights` (rot), tabler:`car-crash` | Prüfpfad `Fall · Die Kreuzung` | 1 Einfahrt, Pille „≈ 160 km/h“ · 2 SUV erscheint, Pille „Grün“ · 3 Kollision (`car-crash`) · 4 Pille „Fahrer (69) stirbt“, Szene stumm gehalten · 5 JO `schock` redet, Blase „Ich wollte doch niemanden töten!“ · 6 Frage-Pille „Mord?“ + MX klein dazu | Aufprall (B3), leise |
| **C Sachverhalt** `sv` | Sachverhaltskarte vollständig, 5 s Lesepause | – | Prüfpfad `Sachverhalt` | 1 | – |
| **D Vorsatz Jonas** `a`→`vors_erg` | Tafel links, JO rechts mit wechselnder Mimik | tabler:`brain` (Wissen), tabler:`heart-broken`/`scale` (Wollen), tabler:`shield` um tabler:`car` (Sicherheitsgefühl), tabler:`trophy` (Rennsieg), Zeitstrahl mit Marke „hier noch bremsen?“ | `A. Jonas › §§ 212, 211 StGB` → `› I. 1. Objektiver Tatbestand` → `› I. 2. Vorsatz` → `› Vorsatz › Abgrenzung` → `› Vorsatz › Eigengefahr` → `› Vorsatz › BGH 2018: Zeitpunkt` → `› Vorsatz › BGH 2020: Gesamtschau` | 1 Obersatz §§ 212, 211 · 2 obj. TB ✓ · 3 Vorsatzformen: Absicht ✗, Wissen ✗, Eventualvorsatz ? · 4 Definition dolus eventualis · 5 bewusste Fahrlässigkeit, Denkblase JO „Wird schon gutgehen“ · 6 Eigengefahr: JO `schock`, (−)-Argument · 7 BGH 2018: Zeitstrahl, Marke · 8 BGH 2020: Schild ums Auto · 9 Pokal, Gleichgültigkeit · 10 Ergebnis Vorsatz ✓ (JO `muede`) | – |
| **E Mordmerkmal** `mm`→`rws` | Tafel links, rechts die Kreuzung als Miniatur mit vielen Menschen | tabler:`car` (Rot), tabler:`users` ×3 (Blau/Grün/Lila), tabler:`traffic-lights` | `A. Jonas › I. 3. Mordmerkmal › gemeingefährliches Mittel` → `› II./III. Rechtswidrigkeit, Schuld` → `› Ergebnis` | 1 Tafel Mordmerkmal · 2 Definition · 3 Miniatur Kreuzung, Menschen erscheinen · 4 „nicht beherrschbar“ ✓ · 5 Vorsatz bzgl. Mittel ✓ · 6 RW/Schuld ✓ · 7 Ergebnis + Tateinheit § 315d V | – |
| **F Gegenfall Max** `max`→`max_erg` | Tafel links, MX rechts | tabler:`car` (Blau) ohne Wrack | `B. Max › Mittäterschaft, § 25 II StGB` → `› gemeinsamer Tatentschluss` → `› Ergebnis` | 1 MX `cool`, Frage · 2 Mittäterschaft: Tatentschluss + Tatbeitrag · 3 Rennabrede ≠ Tötungsplan ✗ · 4 Ergebnis (Rechtsprüfung) | – |
| **G Klausurtipp** `tipp` | hellgelbe Tafel, Lexi rechts (erklärt/warnt) | Warnsymbol | `Klausurtipp · Vorsatz begründen` | 1 Tipp Teil 1 · 2 Tipp Teil 2 (§ 315d V) | – |
| **H Klausurschema** `sch`→`k4` | Schema baut sich auf | – | `Klausurschema` | 1 Titel · 2 I. Tatbestand 1.–3. · 3 II., III. · 4 Konkurrenzen · 5 B. zweiter Raser | – |
| **I Merksatz** `merke` | Lexi `freut`, Merksatz mit Marker | – | `Merksatz` | 1 · 2 | – |

**Bildhalte:** Geplant sind etwa 50 (A 5, B 6, C 1, D 10, E 7, F 4, G 2, H 5, I 2, dazu Mimikwechsel innerhalb der Szenen). Mundzustände kommen getrennt hinzu: JO und MX je zu/a/o/e, Lexi erklärt/warnt je zu/a/o/e.

**Übergänge:** Schiebeblenden nur zwischen den Szenen A→B→C→D, E→F, F→G, G→H und H→I; sie bleiben stumm. Innerhalb einer Szene gibt es harte Schnitte und Pops.

**Geräusche:** nur zwei Handlungsgeräusche, Motor (A5) und Aufprall (B3). Zuerst kommen sie aus `Everyday_SFX_50`, sonst aus Freesound CC0, jeweils mit Herkunft in `geraeusche_herkunft.json`. Kein Sirenen- oder Dauerton.

**Darstellung realer Tat:**
- Fiktive Namen, Hinweis „nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, vereinfacht“.
- Kein Blut, keine Opferfigur.
- Der Tod wird nur benannt.
