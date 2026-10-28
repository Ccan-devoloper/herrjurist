# Folge 004 · Neutralitätspflicht: Darf eine Ministerin gegen eine Partei posten? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_004.py`](src/skript_004.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ministerin Brandt (BR), um 50 | Bundesministerin, postet die „Rote Karte“ | Pose `standing/easing-2`, Kopf `Medium Bangs 2`; lila Jackett `#B8A9F5`, Hose `#3D3D58`, Haut `#E6B48F`; Mimiken `Calm` (ruhig), `Serious` (denkt/verärgert), `Driven` (redet), `Cheeky` (cool, redet), `Smile Big` (zufrieden), `Concerned` (ertappt), `Smile` (Parteitag) | `laura_klar` (Frau, mittel) |
| Pressesprecher Krüger (KR), um 40 | warnt vor dem Dienstkanal | Pose `standing/resting-1`, Kopf `Short 1`, Brille `Glasses 2`; Oberteil Türkis `#7FD6D0`, Haut `#B07552`; Mimiken `Calm`, `Concerned` (redet), `Fear` (Schreck) | `christian` (Mann, mittel) |
| Studentin Mia (MI), Anfang 20 | wollte zur Kundgebung, bleibt weg (abschreckende Wirkung) | Pose `standing/walking-2`, Kopf `Buns`; Hose Blau `#8DB3F2`, Haut `#8D5A3B`; Mimiken `Smile`, `Serious` (liest), `Concerned` (redet) | `julia` (Frau, jung) |
| Vorsitzender Hahn (HA), um 60 | Vorsitzender von Partei X, Antragsteller | Pose `standing/robot_dance-3`, Kopf `Gray Short`, Bart `Moustache 4`; Oberteil Grau `#B0B2BE`, Haut `#F0C8A8`; Mimiken `Calm`, `Rage` (redet), `Serious`, `Smile` | `william` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle vier Posen blicken im Original nach rechts. Die Grundansicht ist gespiegelt und blickt nach links zur Tafel; `_r` blickt nach rechts (Brandt im Büro links, Blick zu Krüger). Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2`) wurden bewusst nicht gewählt.

**Reale Personen:** Keine realen Politiker als Figuren, keine realen Parteinamen in Bild oder Ton. Die Leitentscheidungen erscheinen nur als Fundstelle (Sachverhaltskarte „Frei nach BVerfGE 148, 11“, Tafeln „BVerfGE 154, 320 (2020)“, „BVerfGE 162, 207 (2022)“). Szene L (Kanzlerin 2022) zeigt deshalb keine Figur, nur Requisiten.

Figuren-PNGs: `../peeps/op_004/` (76 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Katzenkönig: Wohnung und Laden, vier Figuren; Folge 001: nächtliche Straße, Autos, zwei junge Männer.
- Hier: Tageslicht, Ministerbüro, Smartphone-Beitrag, Kundgebungsplakat, Parteizentrale, Parteitagsbühne; vier neue Figuren, zwei davon Frauen. Erstes Video aus dem Öffentlichen Recht: Organstreit statt Strafbarkeitsprüfung.
- Stimmen: keine Stimme aus 001 (timo, niklas) wiederverwendet.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Ministerbüro** `buero`→`b2` | Brandt links, Krüger rechts, Schreibtisch dazwischen | tabler:`building-bank` (Gelb) + Schild „Bundesministerium“, tabler:`desk` (Gelb), tabler:`device-laptop` (Blau), tabler:`speakerphone` (Orange) + Pille „Partei X: Kundgebung am Samstag“, tabler:`device-mobile` (Weiß) mit tabler:`rectangle-vertical` (Rot) | `Fall · Im Ministerium` | 1 Büro · 2 Kundgebung angekündigt · 3 Brandt verärgert · 4 Brandt redet, Blase „Das poste ich sofort: Rote Karte für Partei X!“, Handy · 5 rote Karte im Handy · 6 Krüger redet, Blase „Über den offiziellen Kanal des Ministeriums?“ · 7 Brandt `cool` redet, Blase „Natürlich. Dort lesen es die meisten.“, Krüger erschrocken | Tippen auf dem Handy bei „poste“ |
| **B Der Beitrag** `post`→`post3` | Handy-Ansicht des Beitrags in der Mitte, Brandt links, Krüger rechts | Karte als Handy, fluent-emoji-high-contrast:`eagle` (Gelb) als Wappen, tabler:`rectangle-vertical` (Rot) | `Fall · Der Beitrag` | 1 leerer Kanal „Bundesministerium · offizieller Kanal“ · 2 Wappen · 3 Rote Karte + Zeile 1 · 4 Zeilen 2/3 · 5 Zeilen 4/5, Brandt zufrieden | – |
| **C Die Leserin** `mia`→`m1` | Straße, Kundgebungsplakat links, Mia rechts mit Handy | fluent-emoji-high-contrast:`placard` (Orange) + Pille „Kundgebung Partei X · Samstag“, tabler:`device-mobile` mit roter Karte | `Fall · Die Leserin` | 1 Mia · 2 Plakat · 3 Handy · 4 Mia redet, Blase „Wenn sogar die Ministerin das sagt, bleibe ich lieber weg.“ | – |
| **D Partei X / Frage** `hahn`→`frage` | Hahn vor Parteifahne | Pille „Partei X“ (Orange), tabler:`flag` (Orange), fluent-emoji-high-contrast:`classical-building` (Weiß) + „Karlsruhe“, tabler:`podium` (Lila) | `Fall · Partei X` → `Fall · Die Frage` | 1 Hahn ernst · 2 Hahn redet, Blase „Das ist Missbrauch des Amtes! Wir gehen nach Karlsruhe.“ · 3 Gericht · 4 Frage-Pille „Durfte die Ministerin so posten?“ · 5 Pille „Und auf dem Parteitag?“ + Pult | – |
| **E Sachverhalt** `sv` | Sachverhaltskarte vollständig, ca. 10 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **F Zulässigkeit** `zul`→`frist` | Tafel links; rechts Gericht, Hahn (Antragsteller), Brandt (Antragsgegnerin) | classical-building, tabler:`trash` (Grau), tabler:`repeat` (Gelb), tabler:`calendar` + „6 Monate“ | `A. Zulässigkeit › Organstreit, Art. 94 I Nr. 1 GG` → `› Beteiligtenfähigkeit` → `› Maßnahme` → `› Antragsbefugnis` → `› Rechtsschutzbedürfnis` → `› Frist, § 64 III BVerfGG` | Tafelzeilen je Merkmal mit Haken, Figuren und Requisiten wechseln mit dem Merkmal (≈ 13 Halte) | – |
| **G Maßstab** `mass`→`info` | Tafel links; rechts Schema Volk → Staatsorgane, dann Waage mit drei Parteien, dann Präsentation + Brandt | tabler:`users` (Blau), tabler:`building-bank`, Pfeile, Kreuz, tabler:`scale` (Gelb), Pillen „Partei A/B/X“, tabler:`calendar`, tabler:`presentation` | `B. Begründetheit › Maßstab, Art. 20 II GG` → `› Chancengleichheit, Art. 21 I GG` → `› Öffentlichkeitsarbeit` | ≈ 10 Halte | – |
| **H Schritt 1: amtlich?** `amt`→`sub_amt` | Tafel links; Brandt rechts, darüber „Ministerin“ vs. „Parteipolitikerin“, dann die Amtsressourcen | building-bank/podium, tabler:`file-text`, tabler:`world`, eagle, tabler:`device-mobile` mit Wappen und roter Karte | `B. Begründetheit › I. Amtliches Handeln?` → `› I. Autorität oder Ressourcen des Amtes` → `› I. Amtliches Handeln (+)` | ≈ 11 Halte, Brandt am Ende `ertappt` | – |
| **I Schritt 2: Eingriff** `eingriff`→`mia2` | Tafel links; Mia rechts, rote Karte, durchgestrichenes Kundgebungsplakat | rectangle-vertical (Rot), placard (Orange) + Kreuz | `B. Begründetheit › II. Eingriff in Art. 21 I GG` | ≈ 6 Halte | – |
| **J Schritt 3: Rechtfertigung, Ergebnis** `recht`→`wanka` | Tafel links; Brandt rechts, dann Hahn dazu, Gericht | tabler:`arrow-back-up` (Rot) + Kreuz („Gegenschlag“), classical-building | `B. Begründetheit › III. Rechtfertigung?` → `› Ergebnis` | ≈ 9 Halte, Kreuze zur Verneinung, grüner Ergebnisblock | – |
| **K Gegenfall Parteitag** `parteitag`→`urt20` | Tafel links; Bühne rechts: Brandt hinter dem Pult, Publikum, später Handy mit Wappen und Teilen-Symbol | Pille „Parteitag“ (Lila), tabler:`podium` (Lila) + Namensschild, tabler:`users` ×2, tabler:`device-mobile`, eagle, tabler:`share` | `Gegenfall · Rede auf dem Parteitag` → `· Ministertitel` → `· Ministerium teilt das Video` → `· BVerfGE 154, 320 (2020)` | ≈ 12 Halte; (+)/(−) zum Urteil 2020 | Applaus bei „Parteitag“ |
| **L Linie 2022** `kanzler`→`kanzler3` | Tafel links; rechts nur Requisiten (keine Figur, reale Person) | tabler:`plane` (Blau), tabler:`microphone`, tabler:`scale` | `Linie · BVerfGE 162, 207 (2022)` | ≈ 8 Halte | – |
| **M Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi rechts (warnt) | Warnsymbol | `Klausurtipp · Erst amtlich, dann neutral` → `Klausurtipp · Art. 94 I Nr. 1 GG` | 5 Halte | – |
| **N Klausurschema** `sch`→`s2d` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | 12 Halte (A, I.–V., B, I.–IV.) | – |
| **O Merksatz** `merke`→`m2` | Lexi, Merksatz mit Marker | – | `Merksatz` | 5 Halte | – |

**Bildhalte:** 115 eigenständige Bildhalte (Manifest). Mundzustände getrennt: Brandt 2 sprechende Ansichten (`BR_redet_r`, `BR_cool_r`), Krüger 1, Mia 1, Hahn 1, Lexi 2, je zu/a/o/e.

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb einer Folie harte Schnitte und Pops.

**Geräusche:** nur zwei Handlungsgeräusche aus Freesound CC0 (Herkunft in `geraeusche_herkunft.json`): Tippen auf dem Handy (Brandt postet), Applaus (Publikum vor der Parteitagsbühne).

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Partei X kündigt für Samstag eine Kundgebung gegen die Politik der Bundesregierung an. Bundesministerin Brandt veröffentlicht daraufhin über den offiziellen Social-Media-Kanal ihres Ministeriums, mit dem Wappen des Ministeriums im Profil: „Rote Karte für Partei X! Ihre Redner treiben die Radikalisierung voran. Wer am Samstag mitläuft, stärkt sie.“
>
> Die Studentin Mia beschließt, der Kundgebung fernzubleiben. Partei X will vor das Bundesverfassungsgericht ziehen.
>
> *(Frei nach BVerfGE 148, 11 – 2 BvE 1/16, „Rote Karte“; Personen und Partei erfunden.)*
>
> **Hat Ministerin Brandt Partei X in ihren Rechten verletzt?**

## Hinweis zur Schreibung „Partei Iks“

Im Skript steht „Partei Iks“, damit die Stimme den Buchstaben sicher als „Iks“ spricht. In Blasen, Tafeln und Sachverhaltskarte steht „Partei X“. Das ist die einzige Abweichung zwischen Blasentext und Sprechtext.
