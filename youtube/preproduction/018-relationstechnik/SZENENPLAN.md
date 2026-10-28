# Folge 018 · Relationstechnik: Kläger-, Beklagten- und Beweisstation erklärt – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_018.py`](src/skript_018.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“. Hook nach Plan: Vor der Referendarin liegen 40 Seiten Schriftsätze. Ein frei erfundener Kaufpreisfall trägt die Relation: Herr Brenner verkauft und liefert Frau Lehmann für ihr Café einen Kühlschrank für 3.000 €, sie behauptet Barzahlung an den Fahrer. Stationen (als Ausbildungs- und Klausurkonvention gekennzeichnet): I. Prozessstation → II. Klägerstation (Schlüssigkeit) → III. Beklagtenstation (Bestreiten § 138 II–IV ZPO, Einwendung Erfüllung § 362 BGB, Einrede § 214 BGB, Bestreiten der Zahlung) → IV. Beweisstation (streitig und erheblich, Beweislast, Zeuge, § 286 ZPO) → V. Tenor (Nebenentscheidungen) → Und im Urteil? (§ 313 ZPO) → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Referendarin (RF), um 27, ohne Namen | bearbeitet die Akte, formuliert den Tenor | Pose `standing/polka_dots`, Kopf `Long`; grünes gepunktetes Oberteil `#8FD694`, dunkle Hose `#3A3A48`, Haut `#E8B98F`; Mimiken `Calm`, `Concerned\|Serious` (fragt, redet), `Serious` (denkt), `Smile` (froh), `Driven` (redet den Tenor) | `julia` (Frau, jung) |
| Herr Brenner (BR), um 50 | Händler, Kläger | Pose `standing/easing-1`, Kopf `Short 5`, Brille `Glasses 4`; blaue Jacke `#8DB3F2`, gelbes Shirt `#F9D56E`, Haut `#E0AC84`; Mimiken `Calm`, `Suspicious` (redet), `Contempt` (ärgert sich), `Smile`, `Serious` | `christian` (Mann, mittel) |
| Frau Lehmann (LE), um 45 | Café-Inhaberin, Beklagte | Pose `standing/pointing_finger-2` (erhobener Zeigefinger: „Doch!“), Kopf `Medium Bangs 2`; schwarzes Oberteil, rote Hose `#F07A6A`, Haut `#D9A07A`; Mimiken `Calm`, `Driven` (redet), `Concerned\|Serious` (Sorge), `Contempt` (trotzig), `Serious`, `Fear` (Schreck beim Ergebnis) | `sabrina` (Frau, mittel) |
| Fahrer (FA), um 60, ohne Namen | Brenners Mitarbeiter, Zeuge | Pose `standing/walking-3` (kommt mit dem Lieferwagen), Kopf `Gray Short`, ohne Bart; schwarz, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet) | `johann` (Mann, älter) |
| Richterin (RI), ohne Namen und Text | Beweisaufnahme | Pose `standing/blazer-4`, Kopf `Gray Medium`; dunkles Kostüm `#3A3A48`, Haut `#B07552`; Mimiken `Calm`, `Serious` | – |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Lehmann im Café und im Saal, Brenner im Saal). Keine Prothesen-Posen (`blazer-1` und `shirt-1` wegen gezeichneter Beinprothese verworfen). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in den sprechenden Ansichten `RF_fragt`, `RF_redet`, `BR_redet`, `LE_redet`, `FA_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (sabrina, johann, julia, christian). **Namen mit eindeutig deutscher Aussprache** (Vorgabe des Kanalinhabers): Brenner, Lehmann (nicht Seidel/Krüger aus 012, nicht Namen aus 010–015). Figuren-PNGs: `../peeps/op_018/` (78 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 012: Wohnzimmer mit Klavier, Sitzungssaal, Wohnung des Schuldners; 015: Gartenfest. 018: Arbeitszimmer der Referendarin (Schreibtisch, Aktenstapel), Café mit Lieferwagen, Sitzungssaal der Beweisaufnahme. Der Sitzungssaal kehrt gegenüber 012 wieder, weil die Beweisaufnahme dort stattfindet; Aufbau anders (Zeuge rechts, Parteien links, Richterin ohne Text hinter dem Tisch „Gericht“).
- Neues Personal und neue Posen (012: pointing_finger-1, shirt-4, blazer-3, walking-2). Stimmen-Pool laut Vorgabe; `sabrina` und `christian` in anderen Rollen als in 012 (dort Richterin und Gerichtsvollzieher).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Akte** `fall`, `r1` | Arbeitszimmer: Schreibtisch links, Referendarin rechts blickt zum Tisch; der Aktenstapel fällt auf den Tisch | tabler:`desk` (Holzton), `coffee` (Weiß), `file-stack` (Weiß) | `Fall · Die Akte` | Tisch und Referendarin ab 0,0 s · Stapel fällt · „40 Seiten Schriftsätze“ · „Zivilakte“ · Referendarin fragt (Blase) | Aktenstapel landet (`szene_018akte_1`) |
| **B Im Café** `akte`→`trennt` | Café links mit Frau Lehmann, Brenner rechts; Kühlschrank beim Händler, Lieferwagen fährt vor, Kühlschrank steht beim Café, Fahrer steigt aus | tabler:`building-store` (Rosa), `fridge` (Türkis), `truck-delivery` (gespiegelt, Weiß), `cash` (Grün) | `Fall · Im Café` → `Fall · Die Frage` | „In der Akte“ · Brenner · Kühlschrank · 3.000 € · Lieferwagen fährt · geliefert, Fahrer · „Klage: 3.000 €“ · Brenner redet · Lehmann redet, Geldschein · „Wer gewinnt?“ · Rechtsfragen · Tatsachenfragen | Lieferwagen hält (`szene_018transporter_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **D Die Stationen** `stat`→`prinzip` | Tafel, Referendarin mit Aktenstapel | tabler:`file-stack` | `Die Stationen der Relation` → `… › Ausbildungs- und Klausurkonvention` | I.–V. Zeile für Zeile · in keinem Gesetz · Konvention · Merkblock „Erst das Recht …“, Referendarin froh | – |
| **E I. Prozessstation** `proz`→`antrag` | Tafel, Brenner | tabler:`building-bank` (Grün), `file-text` | `I. Prozessstation` → `› Zulässigkeit` → `› sachlich zuständig, § 23 Nr. 1 GVG` → `› bestimmter Antrag, § 253 II Nr. 2 ZPO` | Frage · Amtsgericht (✓) · Antrag (✓) | – |
| **F II. Klägerstation** `kl`→`unschl` | Tafel, Brenner | tabler:`fridge` | `II. Klägerstation` → `› Kaufvertrag` → `› Kaufpreis, § 433 II BGB` → `› schlüssig` → `› fehlt eine Tatsache` → `› unschlüssig: Abweisung` | als wahr unterstellt · Kaufvertrag · Anspruch · schlüssig (✓), Brenner froh · lila Kasten unschlüssig/Hinweis/Beklagtenstation entfällt | – |
| **G III. Beklagtenstation** `bk`→`nw` | Tafel, Lehmann | tabler:`fridge`, `eye` | `III. Beklagtenstation › Erheblichkeit` → `› nicht bestritten, § 138 III ZPO` → `› kein Nichtwissen, § 138 IV ZPO` | als wahr unterstellt · nicht bestritten · zugestanden (✓), „unstreitig“ · Nichtwissen (✗), Auge | – |
| **H III. Einwendung** `zahl`→`einr` | Tafel, Lehmann (blickt rechts) und Fahrer; Geldschein wandert zum Fahrer | tabler:`cash` (Grün), `hourglass` (Gelb) | `› erheblich: die Barzahlung` → `› Erfüllung, § 362 I BGB` → `› Einwendung` → `› Einrede, z. B. Verjährung` | Barzahlung (✓) · Fahrer durfte kassieren · Erfüllung · erloschen · Einwendung · Einrede, Sanduhr | – |
| **I III. Bestreiten der Zahlung** `best`→`lief` | Tafel, Brenner | tabler:`cash-off` (Rot), `clipboard-text`, `signature` | `› Bestreiten, § 138 II ZPO` → `› Bestreiten: kein bloßes Nein` | Erklärungspflicht · genau vorgetragen · kein bloßes Nein · BGH-Zitat · Lieferschein (✓) | – |
| **J IV. Beweisstation** `bs`→`zeuge` | Tafel, Lehmann, dann Fahrer als Zeuge | tabler:`cash`, `scale` (Gelb) | `IV. Beweisstation` → `› streitig und erheblich` → `› Beweislast` → `› Zeuge, § 373 ZPO` | streitig/erheblich · allein die Barzahlung · Beweislast · Grundregel · Lehmann · Zeuge | – |
| **K Beweisaufnahme** `f1`→`lastfolge` | Sitzungssaal: Lehmann und Brenner links, Richterin hinter dem Tisch, Fahrer rechts | Richtertisch als dunkler Block, tabler:`scale` | `› Zeuge: der Fahrer` → `› freie Beweiswürdigung, § 286 ZPO` → `› Ergebnis: Zahlung nicht bewiesen` → `› Beweislast: Frau Lehmann` | Fahrer redet (Blase) · § 286 I · Beweisregeln · Mitarbeiter des Klägers · nicht bewiesen, Lehmann erschrickt, Brenner froh · Beweislast | – |
| **L V. Tenor** `ten`→`neben` | Tafel, Referendarin spricht den Tenor | tabler:`file-text` | `V. Tenor` → `› Kosten und vorläufige Vollstreckbarkeit` | Ansage · Tenor-Block, Referendarin redet (Blase) · Kosten · Vollstreckbarkeit | – |
| **M Und im Urteil?** `urt`→`ugr` | Tafel, Referendarin; Stationsnamen werden durchgestrichen | tabler:`file-text` | `Und im Urteil?` → `Urteil › keine Relations-Überschriften` → `Urteil › Aufbau, § 313 ZPO` | Stationsnamen · Kreuz · Gliederung 1.–3. · Gründe, Urteil | – |
| **N Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · kein Beweis über Unstreitiges` → `Klausurtipp · Beweislast prüfen` | Zeile für Zeile | – |
| **O Klausurschema** `sch`→`sV` | Schema baut sich auf | – | `Klausurschema` | I. · II. · III. · Bestreiten · Einwendungen/Einreden · IV. · Beweislast · V. | – |
| **P Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; drei Bewegungen (Aktenstapel fällt, Lieferwagen fährt vor, Geldschein wandert zum Fahrer). Das erste Bild nach dem Intro ist ab 0,0 s vollständig (harte Schnitte für Tisch, Referendarin, Titel und Prüfpfad).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_018akte_1`, `szene_018transporter_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Herr Brenner, ein Händler, verkauft Frau Lehmann für ihr Café einen Kühlschrank für 3.000 Euro und lässt ihn liefern. Sein Fahrer darf bei der Lieferung kassieren. Brenner klagt vor dem Amtsgericht auf Zahlung von 3.000 Euro.
>
> Frau Lehmann bestreitet Kauf und Lieferung nicht. Sie sagt: „Ich habe dem Fahrer bei der Lieferung 3.000 Euro bar bezahlt.“ Eine Quittung hat sie nicht. Brenner bestreitet die Zahlung: Der Fahrer habe nur den Lieferschein unterschreiben lassen. Frau Lehmann benennt den Fahrer als Zeugen.
>
> Annahme: Klage 2026, Amtsgericht auch örtlich zuständig; Zinsen bleiben außen vor.
>
> **Wer gewinnt?**
