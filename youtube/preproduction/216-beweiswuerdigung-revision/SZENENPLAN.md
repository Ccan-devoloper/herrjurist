# Folge 216 · Beweiswürdigung Revision: Lücken, Widersprüche, in dubio pro reo – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_216.py`](src/skript_216.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Sonderlage (Revisionsbegründung, Beweiswürdigung). Beispielfall nach dem Plan-Hook: Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung zu 60 Tagessätzen. Er soll seine Kollegin Frau Bremer in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben; Zeugen gibt es nicht, er bestreitet. Laut den Urteilsgründen schilderte Frau Bremer den Vorfall dreimal verschieden (Schichtleiterin: Stoß gegen das Regal; Polizei: Faustschlag auf den Arm; Hauptverhandlung: am Arm gepackt und zur Seite gerissen). Das Urteil nennt ihre Aussage „konstant“, erörtert die Abweichungen nicht und hält fest, Zweifel habe das Gericht nicht. Ablauf: Fall (Kanzlei → Rückblick Paketlager mit den drei Schilderungen → Rückblick Amtsgericht → Kanzlei) → Sachverhalt → § 261 (Wortlaut) → nur Rechtsfehler, allgemeine Sachrüge (Verweis 204) → Aussage gegen Aussage (Gesamtschau, Kriterien, frühere Angaben) → Fall: lückenhaft und widersprüchlich → Beruhen, §§ 353, 354 Abs. 2 → in dubio pro reo als Entscheidungsregel → Art. 6 Abs. 2 EMRK (Wortlaut) → Klausurtipp (Lexi) → Prüfschema I.–IV. → Merksatz (Lexi).
**Länge:** Hauptfilm 5:43,8 bei 4.880 gesprochenen Zeichen; Begründung in [`ABNAHME.md`](ABNAHME.md).
**Darstellung (Auftrag):** Delikt neutral und nicht sexualisiert (einfache Körperverletzung unter Kollegen, Gewalt nur erzählt, nicht gezeigt), Zeugin ruhig und ernst, nicht als unglaubwürdig karikiert; das Video betont, dass Abweichungen eine Aussage nicht automatisch unglaubhaft machen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Kerber (KE), um 40 | Angeklagter, Lagerarbeiter, Mandant | `standing/shirt-3` (Hemd Khaki `#C9A66B`, schwarze Hose, weiße Schuhe), Kopf `Short 1`, kein Bart, keine Brille, Haut `#E2B08A`; Mimiken `Calm`, `Serious`, `Concerned\|Serious` (Sorge; redet bei k1), `Suspicious`, `Smile` (redet2 bei k2) | `marc` (Mann, mittel) |
| Frau Bremer (BR), um 35 | Kollegin, Belastungszeugin (Rückblick, Tafel D1) | `standing/crossed_arms-1` (Pullover Lila `#B8A9F5`, schwarze Hose), Kopf `Medium Straight` (Haar `#6B4A35`), Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet), `Solemn` | `sabrina` (Frau, mittel) |
| Rechtsanwalt Wegmann (WG), um 60 | Verteidiger | `standing/blazer-3` (Sakko Stahlblau `#4F6D8F`, Hose `#3A3A44`), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#EBC3A3`; Mimiken `Calm`, `Serious`, `Suspicious` (redet), `Smile` | `william` (Mann, älter) |
| Die Richterin (RI), um 50 | Strafrichterin am Amtsgericht (nur Rückblick) | `standing/blazer-4` (Jacke Schwarzgrau `#2B2B35` wie eine Robe, weißes Oberteil), Kopf `Bun` (Haar `#3A2A20`), Haut `#D9A884`; Mimiken `Calm`, `Serious` (redet) | `laura_ruhig` (Frau, mittel, ruhig) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt` der Parallelfolgen (dort „216: Kerber, Bremer, Wegmann“ eingetragen, bevor vertont wurde) und als Figurenname in keiner bisherigen Folge (Volltextsuche über `youtube/` in `*.py/*.md/*.json/*.csv` am 06.10.2026: keine Treffer). „Seiler“ verworfen (in 014/015/016/164 vorhanden). Die Richterin bleibt namenlos (Funktionsrolle).
- **Stimmen nur aus dem Pool** (william, sabrina, marc, laura_ruhig); alle vier genutzt, je Figur eine.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Kanzlei: Wegmann (`_r`) und Kerber (links blickend) einander zugewandt; Paketlager: Frau Bremer blickt nach links zu den Karten ihrer Schilderungen; Amtsgericht: Richterin (`_r`) und Kerber einander zugewandt; Tafelfolien: alle blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KE_redet`, `KE_redet2`, `BR_redet`, `WG_redet`, `RI_redet` (je links/rechts) und Lexi.
- Keine Prothesen-Posen, keine Bärte, keine Polka Dots, keine Karikatur; der Angeklagte in Arbeitshemd ohne Herkunfts- oder Hautfarben-Klischee; keine realen Personen.
- Figuren-PNGs: `../peeps/op_216/` (76 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_216.png`.

**Abweichung von den letzten Folgen:** 213 (`robot_dance-3`, `easing-1`, `walking-2`, `shirt-1`), 214 (`easing-2`, `walking-1`, `walking-3`), 215 (`robot_dance-2`, `resting-1`, `crossed_arms-2`) – die Posen `shirt-3`, `crossed_arms-1`, `blazer-3`, `blazer-4` kommen in keiner der drei Vorfolgen vor; Farben Khaki/Lila/Stahlblau/Schwarzgrau, keine Muster. Schauplätze: Kanzlei mit Schreibtisch und Lampe (204: Aktenregal), Paketlager mit Hochregal und Kartons (neu; 215 spielt in einer Bäckerei, 152 in einer Gärtnerei), Sitzungssaal des Amtsgerichts mit Richtertisch ohne Hoheitszeichen.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Kanzlei** `fall`→`k1` | Schreibtisch, Wegmann und Kerber ab 0,0 s mit Namensschildern | `schreibtisch()` + tabler:`lamp` (Gelb), `urkunde()`, tabler:`messages` | `Fall · In der Kanzlei` (ab 0,0 s) → `· Das Urteil des Amtsgerichts` → `· Der Vorwurf` → `· Aussage gegen Aussage` → `· Herr Kerber bestreitet` | Grundbild · Urkunde · Pille § 223 · Pille 60 Tagessätze, Kerber besorgt · Vorwurf · Spätschicht · Zeugen: keine · Aussage gegen Aussage · Blase Kerber | – |
| **A2 Rückblick: Paketlager** `drei`→`attest` | Hochregal mit Kartons, Frau Bremer rechts; links drei Karten ihrer Schilderungen | `hochregal()`, tabler:`package` (Karton), `building-warehouse`, `shield`, `scale`, `report-medical` | `Fall · Rückblick: 3 Schilderungen` → `· 1. Schilderung: Schichtleiterin` → `· 2. … Polizei` → `· 3. … Hauptverhandlung` → `· Das Attest` | Grundbild · Karton · Karte 1 · Blase 1 + Zitat · Karte 2 · Blase 2 + Zitat · Karte 3 · Blase 3 + Zitat · Attest | Karton (`szene_216karton_1`) |
| **A3 Rückblick: Amtsgericht** `saal`, `r1` | Richtertisch mit Akten, Richterin und Kerber | `richtertisch()`, tabler:`folders` | `Fall · Rückblick: das Urteil` → `· „konstant und glaubhaft“` | Grundbild · Pille · Blase Richterin | – |
| **A4 Kanzlei** `w1`→`frage2` | wie A1 (Rückkehr nach dem Rückblick); Urkunde mit den drei Schilderungen | wie A1 | `Fall · Was steht im Urteil?` → `· „konstant“?` → `· „Im Zweifel für den Angeklagten“` → `· Die Fragen` | Liste zum Wort · „konstant“ ? · „kein Wort“ · Blase Wegmann · Blase Kerber + „Zweifel“-Zitat · zwei Fragepillen | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **C1 § 261** `p261`, `sache` | Wortlautkarte, beide Figuren | tabler:`brain`, `gavel` | `Beweiswürdigung · § 261 StPO` → `› freie Überzeugung` → `› Sache des Tatgerichts` | Karte + 3 Marker · Block + BGH | – |
| **C2 nur Rechtsfehler** `nurrf`→`sachr` | Tafel, Wegmann | tabler:`zoom-question`, `puzzle-off`, `arrows-split`, `brain`, `file-text` | `Revision › nur Rechtsfehler` → `› lückenhaft` … `› überspannte Anforderungen` → `› allgemeine Sachrüge genügt` | Zeile · 5 Fehler zum Wort · BGH · Block Sachrüge · Verweis | – |
| **D1 Aussage gegen Aussage** `aga2`→`det` | Tafel, Frau Bremer (ruhig, ernst) | tabler:`messages`, `search`, `list-check` | `Aussage gegen Aussage · eine Belastungszeugin` → `› besonders sorgfältige Würdigung` → `› Gesamtschau aller Umstände` → `› Entstehung, Motive, Konstanz, Details` | ✓ + BGH · Block · Gesamtschau + BGH · 5 Kriterien zum Wort | – |
| **D2 frühere Angaben** `frueh`→`erkl` | Tafel, Wegmann | tabler:`file-description`, `scale`, `message-2` | `› frühere Angaben mitteilen` → `› Abweichungen gewichtet?` → `› Abweichung: nicht automatisch unglaubhaft` → `› erkennen und erklären` | Block + BGH · Prüffrage · Linie + Satz · Block + BGH | – |
| **E1 Fall: Lücke und Widerspruch** `fall2`→`wid` | Tafel, beide Figuren | tabler:`file-text`, `messages`, `puzzle-off`, `arrows-split` | `Fall › die Beweiswürdigung im Urteil` → `› 3 Schilderungen im Urteil` → `› „konstant“ – ohne Erörterung` → `› lückenhaft (-)` → `› widersprüchlich (-)` | 3 Schilderungen zum Wort · „konstant“ · „keinem Wort“ · ✗ lückenhaft · ✗ widersprüchlich + BGH | – |
| **E2 Ergebnis** `beruh`→`frei` | Tafel, beide Figuren | tabler:`link`, `file-x`, `arrow-back-up`, `hand-stop` | `Ergebnis › Beruhen, § 337 Abs. 1 StPO` → `› Aufhebung, § 353 StPO` → `› Zurückverweisung, § 354 Abs. 2 StPO` → `› kein Freispruch durch das Revisionsgericht` | ✓ + BGH · Block · Block · ✗ + § 354 Abs. 1 | – |
| **F1 in dubio pro reo** `idpr`→`muss` | Tafel, Kerber | tabler:`help`, `list-check`, `file-text`, `zoom-question` | `in dubio pro reo` → `› Entscheidungsregel` → `› erst nach der Beweiswürdigung` → `› verletzt nur bei Zweifeln` → `› hier: keine Zweifel – nicht verletzt` → `› Fehler: die Beweiswürdigung` | Zeile · 2 Blöcke · Zeilen + BGH · Block · Urteilszitat · ✗ · Fazitzeile | – |
| **F2 Unschuldsvermutung** `emrk` | Wortlautkarte Art. 6 Abs. 2 EMRK (dt. Übersetzung des EGMR), beide Figuren | tabler:`shield-check` | `in dubio pro reo › Unschuldsvermutung, Art. 6 Abs. 2 EMRK` | Karte + 2 Marker | – |
| **G Klausurtipp** `tipp`→`t3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 1. Sachrüge · 2. Formulierung (3 Zeilen zum Wort) · 3. Block | – |
| **H Prüfschema** `sch`→`sc4` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfschema › I. …` bis `› IV. Beruhen, Aufhebung` | 9 Stufen | – |
| **I Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Sätze, 3 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch aus Freesound CC0 (Karton wird im Lager abgestellt), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen (Zahl als Ziffer: „3-mal“). Wortlautkarten wörtlich (§ 261 StPO nach gesetze-im-internet.de, Abruf 06.10.2026; Art. 6 Abs. 2 EMRK nach der deutschen Übersetzung des EGMR, Quelle auf der Karte).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Schreibtisch, Urkunde, Hochregal und Richtertisch programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung zu einer Geldstrafe von 60 Tagessätzen. Er soll seine Kollegin Frau Bremer in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben. Zeugen gab es nicht; Herr Kerber bestreitet die Tat. Ein Attest belegt einen Bluterguss am Oberarm.
>
> Laut den Urteilsgründen schilderte Frau Bremer den Vorfall 3-mal: der Schichtleiterin am selben Abend als Stoß gegen das Regal, 2 Wochen später der Polizei als Faustschlag auf den Arm, in der Hauptverhandlung so, dass er sie am Arm gepackt und zur Seite gerissen habe. Das Urteil nennt ihre Aussage konstant und glaubhaft, ohne auf die Abweichungen einzugehen. Zweifel habe das Gericht nicht.
>
> Rechtsanwalt Wegmann hat rechtzeitig Sprungrevision eingelegt und die Verletzung materiellen Rechts gerügt.
>
> **Ist die Beweiswürdigung revisibel – und ist „in dubio pro reo“ verletzt?**
