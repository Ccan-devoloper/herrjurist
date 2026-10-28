# Folge 001 · Raser-Fall: Mord mit dem Auto? – Szenenplan (Entwurf zur Freigabe)

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_raser.py`](src/skript_raser.py)

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
| **D Vorsatz Jonas** `a`→`vors_erg` | Tafel links, JO rechts mit wechselnder Mimik | tabler:`brain` (Wissen), tabler:`scale` (Wollen), Zeitstrahl mit Marke „hier noch bremsen“, tabler:`car` → tabler:`car-suv` Seitenansicht (abgestufte Eigengefahr), tabler:`trophy` (Siegeswille) | `A. Jonas › §§ 212, 211 StGB` → `› I. 1. Objektiver Tatbestand` → `› I. 2. Vorsatz` → `› Vorsatz › Abgrenzung` → `› Vorsatz › Eigengefahr` → `› Vorsatz › BGH 2018` → `› Vorsatz › BGH 2020` | 1 Obersatz §§ 212, 211 · 2 obj. TB ✓ · 3 Vorsatzformen: Absicht ✗, Wissen ✗, bedingter Vorsatz ? · 4 Definition (Wissen + Wollen) · 5 bewusste Fahrlässigkeit, Denkblase JO „Wird schon gutgehen“ · 6 Eigengefahr (−), JO `schock` · 7 BGH 2018: Zeitstrahl, Marke „zu spät“ · 8 „Panzer“ durchgestrichen · 9 BGH 2020: Aufprall auf Seite = „leicht verletzt“, Zusammenstoß mit Max = „nicht erwartet“ · 10 Pokal, Weiterfahrt trotz möglicher Bremsung · 11 Vorsatz ✓ (JO `muede`) | – |
| **E Mordmerkmale** `mm`→`a_erg` | Tafel links; rechts Miniatur der Kreuzung (Ampel grün für den Geländewagen) | tabler:`car` (Rot), tabler:`car-suv` (Grau), tabler:`traffic-lights` (grün gefüllt), tabler:`users` (weitere Menschen), tabler:`trophy` vs. tabler:`heart` | `A. Jonas › I. 3. Mordmerkmale › gemeingefährliches Mittel` → `› Heimtücke` → `› niedrige Beweggründe` → `› II./III. RW, Schuld` → `› Ergebnis` | 1 Tafel: drei Merkmale untereinander · 2 Definition gemeingefährliches Mittel · 3 objektiv (+), weitere Menschen erscheinen · 4 subjektiv nicht belegt (−), Kreuz · 5 Heimtücke: Ampel grün, „arg- und wehrlos“ ✓ · 6 niedrige Beweggründe: Pokal ↔ Leben, „krasses Missverhältnis“ ✓ · 7 RW/Schuld ✓, Ergebnis: Mord, Tateinheit § 315c | – |
| **F Gegenfall Max** `max`→`versuch` | Tafel links, MX rechts; sein blaues Auto ohne Treffer | tabler:`car` (Blau), tabler:`car-suv` (Grau) knapp daneben | `B. Max › Mittäterschaft, § 25 II StGB` → `› Ergebnis: Versuch` | 1 MX `cool`, Frage · 2 Mittäterschaft: gemeinsamer Tatentschluss auch zur Tötung? · 3 Rennabrede ≠ Tötungsplan ✗, BGH hebt auf · 4 eigener Tötungsvorsatz, Treffer „Zufall“ · 5 versuchter Mord ✓ (MX `ernst`) | – |
| **G Klausurtipp** `tipp` | hellgelbe Tafel, Lexi rechts (erklärt/warnt) | Warnsymbol | `Klausurtipp · Vorsatz begründen` | 1 Tipp: kein Schluss allein aus Gefährlichkeit; Motiv, Eigengefahr, Zeitpunkt; Mordmerkmal subjektiv · 2 heute: § 315d V (seit 13.10.2017, hier nicht anwendbar) | – |
| **H Klausurschema** `sch`→`k4` | Schema baut sich auf | – | `Klausurschema` | 1 Titel · 2 I. 1. objektiv · 3 I. 2. Vorsatz (Wissen, Wollen, Eigengefahr, Zeitpunkt) · 4 I. 3. Mordmerkmale obj./subj. · 5 II. RW, III. Schuld, Konkurrenzen · 6 B. zweiter Raser: Mittäterschaft? sonst eigene Tat/Versuch | – |
| **I Merksatz** `merke` | Lexi `freut`, Merksatz mit Marker | – | `Merksatz` | 1 · 2 | – |

**Bildhalte:** Geplant sind etwa 45 Grundhalte (A 5, B 6, C 1, D 11, E 7, F 5, G 2, H 6, I 2, dazu Mimikwechsel innerhalb der Szenen). Mundzustände kommen getrennt hinzu: JO und MX je zu/a/o/e, Lexi erklärt/warnt je zu/a/o/e.

**Übergänge:** Schiebeblenden nur zwischen den Szenen A→B→C→D, E→F, F→G, G→H und H→I; sie bleiben stumm. Innerhalb einer Szene gibt es harte Schnitte und Pops.

**Geräusche:** nur zwei Handlungsgeräusche, Motor (A5) und Aufprall (B3). Zuerst kommen sie aus `Everyday_SFX_50`, sonst aus Freesound CC0, jeweils mit Herkunft in `geraeusche_herkunft.json`. Kein Sirenen- oder Dauerton.

**Darstellung realer Tat:**
- Fiktive Namen, Hinweis „nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, vereinfacht“.
- Kein Blut, keine Opferfigur.
- Der Tod wird nur benannt.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Gegen 0:30 Uhr stehen Jonas und Max mit ihren Autos nebeneinander an einer roten Ampel in der Innenstadt und verabreden ein Rennen. Sie rasen über mehrere Kreuzungen, teils bei Rot. An der letzten Kreuzung fahren beide ungebremst bei Rot ein, Jonas mit mehr als 160 km/h. Er rammt einen Geländewagen, der bei Grün von rechts kommt. Dessen 69-jähriger Fahrer stirbt. Max trifft niemanden.
>
> **Strafbarkeit von Jonas und Max?**
>
> *nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19 (Berliner Ku’damm-Fall), vereinfacht, Namen geändert*
