# Folge 048 · Versäumnisurteil Voraussetzungen: § 331 ZPO und unechtes VU – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_048.py`](src/skript_048.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Schema“. Vertiefung von Folge 030 (Schlüssigkeit, dort nur kurz § 331 I, II ZPO) und Folge 012 (VU als Abzweig im Vorverfahren). Beispielfall nach dem Plan-Hook: Herr Baumann verkauft Frau Ehlers seine Wiese am Dorfrand für 8.500 €, nur mündlich per Handschlag, ohne Notar. Sie zahlt nicht; Kaufpreisklage zum Amtsgericht, früher erster Termin, die Beklagte erscheint trotz ordnungsgemäßer Ladung nicht, der Kläger beantragt ein Versäumnisurteil. Ablauf: Fall → Frage → Sachverhalt → Wer ist säumig? (§ 330 / § 331) → I. Antrag → II. Säumnis (§ 333, § 335 I Nr. 2, 3) → III. Zulässigkeit (von Amts wegen, § 331 I 2) → IV. Schlüssigkeit: Geständnisfiktion (§ 331 I 1, II) → Formnichtigkeit (§§ 311b I, 125 BGB), Hinweis § 139 ZPO → unechtes Versäumnisurteil, Prozessurteil, Berufung statt Einspruch → Gegenfall echtes VU: Einspruch (§§ 338, 339), Wirkung (§ 342), zweites VU (§ 345) → § 331 III → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Baumann (BA), um 55 | Verkäufer, Kläger | Pose `standing/pointing_finger-2` (erhobener Zeigefinger: „Dann beantrage ich ein Versäumnisurteil!“), Kopf `Gray Short`, ohne Bart und Brille; schwarzes Oberteil (Pose ohne einfärbbares Oberteil), Hose Blau `#8DB3F2`, Haut `#E8B98F`; Mimiken `Calm`, `Smile`, `Driven` (redet), `Concerned\|Serious` (Sorge; redet als `BA_klagt`), `Serious`, `Fear`, `Contempt` | `marc` (Mann, mittel) |
| Frau Ehlers (EH), um 35 | Käuferin, Beklagte (im Termin säumig) | Pose `standing/easing-2`, Kopf `Medium Bangs 2`; rosa Jacke `#F6A5C0`, dunkle Hose `#3A3A48`, Haut `#D9A07A`; Mimiken `Calm`, `Smile` (redet), `Suspicious` (redet, Einspruch), `Serious`, `Concerned\|Serious` | `ela_froh` (Frau, jung) |
| Richterin (RI), um 55, ohne Namen | Amtsgericht: Aufruf, Hinweis | Pose `standing/blazer-4` (dunkler Blazer `#3A3A48` wie eine Robe, weißes Oberteil), Kopf `Gray Medium`, Brille `Glasses 4`, Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile` | `laura_ruhig` (Frau, mittel) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel bzw. zum Gegenüber, `_r` blickt nach rechts (Baumann auf der Wiese zu Frau Ehlers und im Sitzungssaal zur Richterin). Keine Prothesen-Posen (`blazer-1`, `blazer-2`, `shirt-1`, `shirt-2` verworfen), keine Bärte. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in den sprechenden Ansichten `BA_redet`, `BA_klagt`, `EH_redet`, `EH_trotz`, `RI_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (`christian` nicht gebraucht). **Namen mit eindeutig deutscher Aussprache**, nicht in der Liste vergebener Namen und in keiner früheren Folge verwendet (Skripte 001–047 durchsucht): Baumann, Ehlers. Die Richterin spricht im Aufruf beide Namen, sonst nennt sie nur die Erzählerin. Figuren-PNGs: `../peeps/op_048/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 047 (Kameraladen in der Altstadt), 046 (Elektrogeschäft, Wohnung, Waschsalon), 045 (Klausursaal), 044 (Marktplatz). 048: **Wiese am Dorfrand** mit Zaun, Bäumen und Verkaufsschild (erstmals ein unbebautes Grundstück) und **Sitzungssaal des Amtsgerichts mit leerem Beklagtenstuhl und Wanduhr**. Der Sitzungssaal kehrt gegenüber 012/030 erzählerisch zwingend zurück (die Säumnis im Termin ist der Fall); Aufbau anders: Richterin hinter dem Tisch in der Mitte, Kläger links, rechts der leere Stuhl mit Schild „Beklagte: Frau Ehlers“, Uhr für den Termin.
- Neue Posen gegenüber 046/047 (`easing-1`, `blazer-3`, `blazer-1`, `shirt-3`): `pointing_finger-2`, `easing-2`, `blazer-4`. Andere Stimmen als in 047 (stephan, sabrina) und 046 (hilde, timo).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Auf der Wiese** `fall`→`zahlt` | Bodenlinie, Verkaufsschild links, Baumann (blickt rechts), Zaun in der Mitte, Ehlers rechts, Bäume | tabler:`sign-right` (Weiß), `fence` (Holz), `trees` (Grün), `rubber-stamp-off` (Rot), `cash-off` (Rot); ph:`handshake` (Gelb) | `Fall · Die Wiese` → `Fall · Kein Notar` → `Fall · Frau Ehlers zahlt nicht` | ab 0,0 s Wiese mit Baumann · „zu verkaufen“ · Ehlers · Kaufpreis 8.500 € · Handschlag · „per Handschlag“ · Ehlers redet (Blase) · kein Notar · zahlt nicht, Baumann besorgt | Handschlag (`szene_048handschlag_1`) |
| **B Im Sitzungssaal** `klage`→`frage2` | Richterin hinter dem Richtertisch (dunkler Block „Gericht“), Baumann links (blickt rechts), rechts leerer Stuhl, Wanduhr | tabler:`file-text` (Akte fällt auf den Tisch), `clock-hour-9`; ph:`chair` (Blau) | `Fall · Die Klage` → `Fall · Der Termin` → `Fall · Die Beklagte fehlt` → `Fall · Antrag auf Versäumnisurteil` → `Fall · Die Frage` | Saal · Akte · Klage 8.500 € · Klageschrift „mündlich geeinigt“ · Uhr, früher erster Termin · Richterin ruft auf (Blase) · Schild „Beklagte: Frau Ehlers“ · ordnungsgemäß geladen · nicht erschienen · Baumann redet (Blase) · „Bekommt er es?“ · „Was prüft das Gericht …?“ | Akte auf dem Richtertisch (`szene_048akte_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D Wer ist säumig?** `wer`→`p331` | Tafel, Baumann und Richterin | ph:`chair` | `Vorab: Wer ist säumig?` → `› Kläger: § 330 ZPO` → `› Beklagter: § 331 ZPO` | Frage · Wortlautkarte § 330 mit zwei Markern · keine Schlüssigkeitsprüfung · § 331 · „So hier“ (✓) | – |
| **E I. Antrag, II. Säumnis** `antrag`→`hier2` | Tafel, Baumann und Richterin | tabler:`file-text`, `mail`; ph:`chair` | `I. Antrag des Klägers` → `II. Säumnis der Beklagten` → `› kein Hindernis, § 335 ZPO` → `› ordnungsgemäß geladen, Nr. 2` → `› rechtzeitig mitgeteilt, Nr. 3` → `› gegeben` | Antrag (✓) · Säumnis · § 333 · § 335 · Wortlautkarte § 335 I Nr. 2, 3 mit drei Markern · säumig (✓) | – |
| **F III. Zulässigkeit** `zul`→`hier3` | Tafel | tabler:`file-text`, `building-bank` (Grün) | `III. Zulässigkeit der Klage` → `› von Amts wegen` → `› § 331 Abs. 1 S. 2 ZPO` → `› zulässig` | von Amts wegen · Prozessfähigkeit (✗ kein VU, BGH Rn. 10) · § 331 I 2 · Kasten Wohnsitz/Streitwert · zulässig (✓) | – |
| **G IV. Schlüssigkeit** `schl`→`abs2` | Tafel | tabler:`file-text`; ph:`handshake` | `IV. Schlüssigkeit` → `› Geständnisfiktion, § 331 Abs. 1 S. 1 ZPO` → `› als zugestanden: mündliche Einigung` → `› § 331 Abs. 2 ZPO: trägt das den Antrag?` | Wortlautkarte § 331 I 1 mit zwei Markern · Geständnisfiktion · zugestanden · Wortlautkarte § 331 II mit zwei Markern | – |
| **H IV. Schlüssigkeit: die Form** `form`→`b2` | Tafel, Richterin redet (Hinweis), Baumann redet | tabler:`rubber-stamp-off` (Rot) | `› Form, § 311b Abs. 1 S. 1 BGB` → `› nichtig, § 125 S. 1 BGB` → `› keine Heilung` → `› unschlüssig` → `Hinweis, § 139 ZPO` | Wortlautkarte § 311b I 1 (zwei Marker) · Wortlautkarte § 125 S. 1 · Heilung (✗) · kein Kaufpreisanspruch · unschlüssig, Baumann erschrickt · Hinweis · Richterin (Blase) · Baumann (Blase) | – |
| **I Das unechte VU** `unecht`→`inhalt` | Tafel | ph:`chair` | `Ergebnis › Abweisung trotz Säumnis` → `› unechtes Versäumnisurteil` → `› unzulässige Klage: Prozessurteil` → `› Berufung statt Einspruch` → `› Inhalt, nicht Überschrift` | Abweisung · „kein VU“ / „streitiges Endurteil“ · BGH I ZR 186/25 · Prozessurteil · Einspruch (✗) · Berufung (✓) · Inhalt (BGH IX ZB 59/20) | – |
| **J Gegenfall: echtes VU** `gegen`→`p345` | Tafel, Baumann und Ehlers (redet: Einspruch) | tabler:`file-check` (Grün), `calendar-event`, `arrow-back-up`; ph:`chair` | `Gegenfall › notariell beurkundet: schlüssig` → `› echtes Versäumnisurteil` → `Einspruch, §§ 338, 339 ZPO` → `Einspruch › Wirkung, § 342 ZPO` → `Einspruch › zweites Versäumnisurteil, § 345 ZPO` | schlüssig (✓) · echtes VU, Ehlers besorgt · Ehlers redet (Blase) · zwei Wochen · Notfrist · § 342 · § 345 | – |
| **K § 331 III** `vv`→`vv3` | Tafel, Ehlers und Richterin | tabler:`mailbox`, `mailbox-off` (Rot) | `Vorverfahren › Anzeige binnen zwei Wochen` → `› § 331 Abs. 3 ZPO` → `› Antrag schon in der Klageschrift` | Vorverfahren · zwei Wochen · ohne mündliche Verhandlung · Antrag in der Klageschrift | – |
| **L Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Zulässigkeit und Schlüssigkeit` → `Klausurtipp · streitiges Urteil entwerfen` | Zeile für Zeile | – |
| **M Klausurschema** `sch`→`serg2` | Schema baut sich auf | – | `Klausurschema` | Vorab · I. · II. · III. · IV. · Ergebnis echt · unecht | – |
| **N Merksatz** `merke`, `mz` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Akte fällt auf den Richtertisch). Das erste Bild nach dem Intro ist ab 0,0 s vollständig (Wiese, Schild, Zaun, Bäume, Baumann mit Namensschild, Titel, Prüfpfad).
**Geräusche:** zwei Handlungsgeräusche (Handschlag, Akte), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Herr Baumann und Frau Ehlers einigen sich im März 2026 mündlich: Frau Ehlers kauft seine Wiese am Dorfrand, ein eigenes Grundstück, für 8.500 Euro. Einen Notar beauftragen sie nicht. Frau Ehlers zahlt nicht.
>
> Herr Baumann klagt vor dem Amtsgericht an ihrem Wohnort auf Zahlung von 8.500 Euro; in der Klageschrift schildert er die mündliche Einigung. Das Gericht bestimmt einen frühen ersten Termin. Frau Ehlers wird die Klageschrift zugestellt, sie wird ordnungsgemäß und rechtzeitig geladen. Im Termin erscheint sie nicht. Herr Baumann beantragt ein Versäumnisurteil.
>
> Annahme: Auflassung und Eintragung im Grundbuch gibt es nicht; die übrigen Zulässigkeitsvoraussetzungen liegen vor.
>
> **Wie entscheidet das Gericht?**
