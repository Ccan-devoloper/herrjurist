# Folge 030 · Schlüssigkeitsprüfung: Der Test, den jede Klage bestehen muss – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_030.py`](src/skript_030.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“. Vertiefung der in Folge 018 nur angerissenen Klägerstation. Beispielfall: Frau Schubert leiht ihrem Nachbarn Herrn Franke 6.000 €, mündlich ist Rückzahlung bis Ende Juni vereinbart. Ihre Klageschrift nennt Vereinbarung und Überweisung, sonst nur „Das Darlehen ist fällig.“ (bloße Rechtsbehauptung; Plan-Hook „grob pflichtwidrig“ übertragen). Ablauf: Fall → Frage → Sachverhalt → Test und BGH-Formel → I. Anspruchsgrundlage (§ 488 I 2 BGB) → II. Tatsachenvortrag (Merkmal für Merkmal; Fälligkeit, § 488 III BGB) → III. Hinweis (§ 139 ZPO) → IV. Ergebnis → Substantiierung → Abgrenzung Beweisstation → Abgrenzung Zulässigkeit (§ 253 II Nr. 2 ZPO) → Folge der Unschlüssigkeit und Versäumnisurteil (§ 331 I, II ZPO) → Klausurtipp → Schema → Merksatz. Die Stationen werden als Ausbildungs- und Klausurkonvention gekennzeichnet.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Schubert (SC), um 45 | Darlehensgeberin, Klägerin | Pose `standing/resting-2` (Hand an der Hüfte), Kopf `Medium Straight`; schwarzes Oberteil, blaue Hose `#8DB3F2`, Haut `#E8B98F`; Mimiken `Calm`, `Driven` (redet), `Smile`, `Concerned\|Serious` (Sorge), `Serious`, `Contempt`, `Fear` | `lea` (Frau, mittel; nur der harmlose Satz der Klageschrift) |
| Herr Franke (FR), um 60 | Nachbar, Darlehensnehmer, Beklagter | Pose `standing/pointing_finger-1` (erhobener Zeigefinger: „Von Juni war nie die Rede!“), Kopf `No Hair 1`, Brille `Glasses`, ohne Bart; schwarz, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet, bedankt sich), `Suspicious` (redet, bestreitet), `Serious`, `Tired` | `william` (Mann, älter) |
| Richterin (RI), um 50, ohne Namen | Amtsgericht: Hinweis nach § 139 ZPO, Verhandlung | Pose `standing/robot_dance-2` (offene Hand), Kopf `Long Bangs`, Brille `Glasses 2`; schwarzes Oberteil, dunkle Hose `#3A3A48`, Haut `#B07552`; Mimiken `Calm`, `Serious` (redet), `Suspicious` (denkt), `Smile` | `laura_ruhig` (Frau, mittel) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel bzw. zum Gegenüber, `_r` blickt nach rechts (Schubert am Gartenzaun und im Sitzungssaal). Keine Prothesen-Posen (`blazer-1`, `blazer-2`, `shirt-1`, `shirt-2` verworfen). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in den sprechenden Ansichten `SC_redet`, `FR_redet`, `FR_trotz`, `RI_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (william, lea, laura_ruhig; `stephan` nicht gebraucht). **Namen mit eindeutig deutscher Aussprache**, in früheren Folgen nicht vergeben: Schubert, Franke; die Namen spricht nur die Erzählerin. Figuren-PNGs: `../peeps/op_030/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 028/029 (Besitz/Eigentum, Vorsatzformen) und 018 (Relation: Arbeitszimmer, Café, Sitzungssaal). 030: Gartenzaun zwischen zwei Häusern, Schreibtisch mit Laptop neben dem Amtsgericht, Sitzungssaal der mündlichen Verhandlung. Der Sitzungssaal kehrt gegenüber 018 zurück, weil das Bestreiten in der Verhandlung fällt; Aufbau anders (Klägerin links, Beklagter rechts, Richterin hinter dem Tisch mit Text).
- Neue Posen (`resting-2`, `pointing_finger-1`, `robot_dance-2`; 029 und 028 ohne diese Posen), andere Stimmen als in 029 (timo, niklas).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Am Gartenzaun** `fall`→`juli` | zwei Häuser, Zaun; Schubert links (blickt rechts), Franke rechts; Geldschein wandert zu Franke | tabler:`home` (Blau/Gelb), `fence` (Holz), `device-mobile`, `cash` (Grün), `calendar-event`, `calendar-x` (Rot), `cash-off` (Rot) | `Fall · Das Darlehen` → `Fall · Herr Franke zahlt nicht` | ab 0,0 s vollständig · Franke · 6.000 € · Januar überwiesen · Geld wandert · Franke redet (Blase), Ende Juni · Juli · zahlt nicht | – |
| **B Die Klageschrift** `klage`→`frage2` | Schreibtisch mit Laptop, Schubert rechts daneben, Amtsgericht rechts | tabler:`desk`, `device-laptop`, `file-text`, `building-bank` (Grün) | `Fall · Die Klage` → `Fall · Die Frage` | Schreibtisch · Amtsgericht · Klageschrift entsteht (Tippen) · Klage 6.000 € · Schubert redet (Blase) · „Der Test …“ · „Ist sie schlüssig?“ | Tippen am Laptop (`szene_030tastatur_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **D Der Test** `stat`→`formel` | Tafel, Schubert und Franke | tabler:`file-text` | `Klägerstation · Schlüssigkeit` → `› Ausbildungs- und Klausurkonvention` → `› Der Test: als wahr unterstellt` → `› Die Formel des BGH` | Ort · Konvention · Test · Wortlautkarte BGH (Rn. 11) mit vier Hervorhebungen | – |
| **E I. Anspruchsgrundlage** `rs`→`drei` | Tafel | tabler:`book` (Blau) | `I. Anspruchsgrundlage` → `› § 488 Abs. 1 S. 2 BGB` → `› drei Merkmale` | Rechtssatz · Wortlautkarte § 488 I 2 · drei Merkmale nacheinander | – |
| **F II. Tatsachenvortrag** `tats`→`m3` | Tafel als Zuordnungstabelle | tabler:`file-text` | `II. Tatsachenvortrag` → `› Darlehensvertrag` → `› Auszahlung` → `› Fälligkeit?` | Kopfzeile · Vertrag (✓) · Auszahlung (✓) · „fällig“ (✗) · „nur Tatsachen“ | – |
| **G II. Fälligkeit** `p488`→`fehlt` | Tafel | tabler:`calendar-x`, `mail`, `file-x` (Rot) | `› Fälligkeit, § 488 Abs. 3 BGB` → `› kein Termin, keine Kündigung vorgetragen` → `› unschlüssig` | Wortlautkarte § 488 III · Termin (✗) · Kündigung (✗) · „unschlüssig“, Schubert erschrickt | – |
| **H III. Hinweis, IV. Ergebnis** `hinw`→`schl` | Tafel, Schubert und Richterin (redet) | tabler:`file-text`, `calendar-check` (Grün) | `III. Hinweis` → `III. Hinweis, § 139 Abs. 1 ZPO` → `› so früh wie möglich, aktenkundig` → `› die Richterin` → `› Ergänzung` → `IV. Ergebnis › schlüssig` | sofort abweisen? (✗) · Wortlautkarte § 139 I 2 · § 139 IV · Richterin (Blase) · Ergänzung · schlüssig (✓) | – |
| **I Substantiierung** `subst`→`unter` | Tafel | tabler:`calendar-event` | `Substantiierung › Tag und Ort der Abrede?` → `› Einzelheiten nur, soweit bedeutsam` → `Schlüssigkeit oder Substantiierung?` → `Substantiierung › nicht überspannen` | Frage (✗) · BGH-Zitat Rn. 11 · zwei Kästen · Rn. 10 | – |
| **J Beweisstation** `f2`→`bew` | Sitzungssaal: Schubert links, Richterin hinter dem Tisch, Franke rechts | Richtertisch als dunkler Block, tabler:`scale` (Gelb) | `Abgrenzung › Bestreiten` → `› Bestreiten: Beklagtenstation` → `› Beweisstation` | Franke redet (Blase), Schubert ärgert sich · Bestreiten · Beklagtenstation · Beweisstation, Waage · Zeugen | – |
| **K Zulässigkeit** `zul`→`hier` | Tafel, Schubert und Richterin | tabler:`file-text` | `Abgrenzung › Zulässigkeit, § 253 Abs. 2 Nr. 2 ZPO` → `› individualisierbar` → `› zulässig, aber nicht schlüssig` | Wortlautkarte § 253 II Nr. 2 · BGH VII ZR 21/16 · hier (✓) · Kästen gegeben/fehlte | – |
| **L Folge, Versäumnisurteil** `folge`→`vu3` | Tafel, Schubert; Beklagter nicht erschienen (Symbol) | tabler:`file-x`, `user-off` | `IV. Ergebnis › unschlüssig: Abweisung als unbegründet` → `Versäumnisurteil, § 331 Abs. 1 ZPO` → `› nur Tatsachen gelten als zugestanden` → `Versäumnisurteil, § 331 Abs. 2 ZPO` → `› ohne Ergänzung: verloren` | Abweisung · Wortlautkarte § 331 I 1 · nur Tatsächliches · Wortlautkarte § 331 II · trotz Säumnis · verloren, Schubert erschrickt | – |
| **M Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Merkmal für Merkmal` → `Klausurtipp · Stationen trennen` | Zeile für Zeile | – |
| **N Klausurschema** `sch`→`sIVb` | Schema baut sich auf | – | `Klausurschema` | I. · II. · III. · IV. · schlüssig · unschlüssig | – |
| **O Merksatz** `merke`, `mz` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Geldschein wandert zu Franke). Das erste Bild nach dem Intro ist ab 0,0 s vollständig (Häuser, Zaun, Schubert, Titel, Prüfpfad).
**Geräusch:** ein Handlungsgeräusch aus Freesound CC0 (`szene_030tastatur_1`, Tippen, während die Klageschrift auf dem Laptop entsteht), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Frau Schubert leiht ihrem Nachbarn Herrn Franke 6.000 Euro und überweist sie ihm im Januar 2026. Mündlich vereinbaren beide: Rückzahlung bis Ende Juni. Herr Franke zahlt nicht. Im August klagt Frau Schubert vor dem Amtsgericht auf Zahlung von 6.000 Euro.
>
> In der Klageschrift steht nur: „Ich habe mit dem Beklagten vereinbart, ihm 6.000 Euro zu leihen, und sie überwiesen. Das Darlehen ist fällig.“ Zum Rückzahlungstermin schreibt sie nichts. Gekündigt hat sie das Darlehen nicht, auch nicht in der Klageschrift.
>
> Annahme: Zinsen bleiben außen vor; die übrigen Zulässigkeitsvoraussetzungen liegen vor.
>
> **Ist die Klage schlüssig?**
