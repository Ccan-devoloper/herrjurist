# Folge 055 · Ladendiebstahl: Wann ist die Ware weg? Gewahrsamsenklave erklärt – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_055.py`](src/skript_055.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker, Leitentscheidung BGHSt 16, 271). Hook des Themenplans: Monika steckt im Supermarkt einen Lippenstift in ihre Jackentasche, Ladendetektiv Rainer beobachtet alles über einen Deckenspiegel und spricht sie noch vor der Kasse ruhig an. Frage (vollendet, obwohl noch im Laden und beobachtet?) → Sachverhalt (Grundfall, drei Varianten) → Wortlaut § 242 Abs. 1 und 2 → Sache, Wegnahme, Gewahrsam des Supermarkts → Gewahrsamsenklave → Beobachtung unerheblich, Ergebnis → Variante 1 (Zurücklegen nach Vollendung, § 24) → Variante 2 (schwere Kiste offen im Einkaufswagen: Versuch, Rücktritt) → Variante 3 (Versteck unter der Zeitung: Diebstahl statt Betrug) → Folgen (Rücktritt, Ausblick § 252) → § 248a und § 127 StPO → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi).
**Verhältnis zu Folge 051 (Diebstahl-Schema):** Dort steht die Gewahrsamsenklave in einem Satz (Ladekabel im Rucksack im Lesesaal). Hier wird sie vertieft: Selbstbedienungsladen, Kleidung, Beobachtung, gesicherter Gewahrsam, Abgrenzung zu sperriger Ware im Einkaufswagen und zum Versteck im Wagen (Diebstahl/Betrug), Folgen der Vollendung für Rücktritt und § 252. Wortlaut, Gewahrsamsbegriff und Zueignungsabsicht werden nur so weit wiederholt, wie der Fall sie braucht.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Monika (MO), um 40 | Kundin, steckt den Lippenstift ein | `standing/blazer-3` (Blazer mit Taschen Lila `#B8A9F5`, schwarzes Top, Hose Blau `#8DB3F2`), Kopf `Medium Straight`, Haut `#F1C6A5`. Mimiken `Calm`, `Serious`, `Suspicious` (schaut sich um), `Cheeky|Smile` (redet), `Smile`, `Fear`, `Concerned|Serious` (reuig), `Tired`, `Awe` | `laura_klar` (Frau, mittel) |
| Rainer (RA), um 45 | Ladendetektiv in Zivil | `standing/crossed_arms-1` (Pullover Grün `#8FD694`, schwarze Hose, verschränkte Arme), Kopf `Short 3`, Haut `#D9A07A`. Mimiken `Serious` (beobachtet), `Suspicious` (wach), `Calm` (redet, ruhig), `Smile` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Monika zum Regal, Rainer zu Monika, beide in den Tafelszenen zur Tafel), `_r` blickt nach rechts (Monika schaut sich um und geht zur Kasse; Rainer in Variante 2 zu Monika am Einkaufswagen).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Cheeky|Smile`, `Concerned|Serious`. Mundzustände a/o/e bei `MO_redet`, `RA_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-2` wurde wegen der Beinprothese für die Täterin verworfen), keine Uniform, keine Waffe. 48 Figuren-PNGs in `../peeps/op_055/` (Drive-Master).
- **Klischeeprüfung:** Monika ist eine gewöhnliche Kundin (lila Blazer), keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung; Rainer ein ruhiger Detektiv in Zivil. Keine Rangelei, keine Gewalt im Bild (§ 252 nur als gesprochener Ausblick).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen alle Skripte und Dokumente in `preproduction/` geprüft, auch 054): Monika, Rainer. Im Sprechtext nie im Genitiv mit -s.
- **Stimmen** nur aus dem zugeteilten Pool (laura_klar, marc; helmut und sabrina nicht gebraucht). Vorfolgen 052 (sabrina, niklas, helmut) und 053 (ela_froh, timo): keine Überschneidung. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 053 (Fahrradladen/Kaufvertrag), 052 (Treppenhaus/Anscheinsgefahr), 051 (Lesesaal der Unibibliothek). Hier erstmals ein **Supermarkt**: Kosmetikregal mit drei Böden (Lippenstifte, Parfüm, Sprays), Kassentresen mit Scanner, Deckenspiegel mit Auge; in den Varianten Einkaufswagen mit Kiste Wein bzw. Zeitung, Kassenband. Der Kameraladen von 047 wird nicht übernommen. Neue Posen (`blazer-3`, `crossed_arms-1`) gegenüber 051–053.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Supermarkt** `fall`→`frage3` | Regal links, Kasse rechts; Monika nimmt den Lippenstift, schaut sich um, steckt ihn ein (Ring um die Jackentasche), Blase „Den behalte ich einfach.“; Rainer, Deckenspiegel, Auge; Monika geht Richtung Kasse; Rainer spricht sie an, Blase „Entschuldigung, ich bin der Ladendetektiv. Kommen Sie bitte kurz mit.“; Frage-Pillen | Fluent Emoji HC: `lipstick`, `mirror`; tabler: `perfume`, `spray`, `barcode`, `eye`; Regal, Tresen als Karten | `Fall · Der Supermarkt` (ab 0,0 s) → `Fall · Die Frage` | ≈ 20 | Kleidung/Tasche (`szene_055tasche_1`) beim Einstecken |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p242`→`kern` | Wortlautkarten § 242 Abs. 1 (Marker „wegnimmt“) und Abs. 2, Block „vollendet oder versucht?“ | lipstick | `§ 242 StGB › Wortlaut` | ≈ 5 | – |
| **D Sache und Wegnahme** `sache`→`gewahr` | Haken, Definition, Block Gewahrsam Supermarkt | tabler: `building-store`; lipstick | `Grundfall › I. Tatbestand › 1. objektiv › a) fremde bewegliche Sache` → `… › b) Wegnahme` | ≈ 6 | – |
| **E Gewahrsamsenklave** `enkl`→`vollendet` | rechts der Laden als blaue Fläche „Gewahrsam Supermarkt“, darin Monika groß, Ring um die Jackentasche, Pille „Enklave: Monika“ | lipstick | `… › b) Wegnahme › Gewahrsamsenklave` | ≈ 8 | – |
| **F Beobachtung, Ergebnis** `beob`→`erg2` | Spiegel und Auge, Rainer beobachtet, Kreuz „keine heimliche Tat“, Haken, Ergebnisblock | mirror, tabler: `eye` | `… › b) Wegnahme › Beobachtung` → `Grundfall › I. 2. subjektiv, II., III. › Ergebnis` | ≈ 10 | – |
| **G Variante 1** `v1`→`v1e` | kleines Regal, Lippenstift zurück (Pfeil), Monika reuig, Pille „zu spät: vollendet“ | tabler: `arrow-back-up`; lipstick | `Variante 1 › zurück ins Regal` → `Variante 1 › Rücktritt, § 24 StGB?` | ≈ 7 | – |
| **H Variante 2** `v2`→`v2g` | Einkaufswagen mit Kiste Wein, Monika hinter dem Wagen, Rainer tritt hinzu, Pillen „schwer“, „Wagen des Ladens“, „noch Gewahrsam des Ladens“ | tabler: `shopping-cart`, `box`, `bottle` | `Variante 2 › Kiste im Einkaufswagen` → `… › versuchter Diebstahl, §§ 242 Abs. 2, 22 StGB` → `… › Rücktritt, § 24 StGB` | ≈ 11 | Kiste in den Wagen (`szene_055kiste_1`) |
| **I Variante 3** `v3`→`v3f` | Wagen mit Lippenstift, Zeitung deckt ihn ab; Kassentresen mit Ware und Scanner, Pillen „aufs Band: übrige Waren“, „sieht nur das Band“ | tabler: `shopping-cart`, `bottle`, `barcode`; Phosphor: `newspaper`; lipstick | `Variante 3 › Versteck im Einkaufswagen` → `Variante 3 › Betrug? Diebstahl?` | ≈ 11 | – |
| **J Folgen** `folgen`→`p252c` | Monika mit Ring (vollendet) gegen Wagen mit Kiste (Versuch); Haken/Kreuz zu § 252 | shopping-cart, box, bottle | `Folgen › Rücktritt, § 24 StGB` → `Ausblick › räuberischer Diebstahl, § 252 StGB` | ≈ 7 | – |
| **K Strafantrag, Festnahme** `p248a`→`p127b` | Tafel § 248a, Wortlautkarte § 127 Abs. 1 Satz 1 StPO mit drei Markern; Monika und Rainer | lipstick | `Grundfall › Strafantrag, § 248a StGB` → `Ausblick › vorläufige Festnahme, § 127 StPO` | ≈ 8 | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), lipstick | `Klausurtipp · Vollendung an der Wegnahme prüfen` | ≈ 6 | – |
| **M Klausurschema** `sch`→`s_v` | breite Karte, progressiv | – | `Klausurschema` | ≈ 10 | – |
| **N Merksatz** `merke`→`m_3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Lippenstift im Regal → in der Hand → in der Tasche mit Ring; Monika am Regal → auf dem Weg zur Kasse; Spiegel und Auge erscheinen beim Wort; Kiste erscheint im Wagen; Zeitung deckt den Lippenstift ab).
**Geräusche:** nur zwei sichtbare Handgriffe (Einstecken in die Jackentasche, Kiste in den Einkaufswagen), Freesound CC0, siehe `geraeusche_herkunft.json`.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 242 Abs. 1 und 2 wörtlich vorgelesen; § 127 Abs. 1 Satz 1 StPO als Zitat mit Normangabe, gesprochen als Paraphrase, Marker synchron zu „frischer Tat“, „fluchtverdächtig“, „nicht sofort festgestellt“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagvormittag im Supermarkt: Monika nimmt am Kosmetikregal einen Lippenstift für 9 Euro, schaut sich um und steckt ihn in ihre Jackentasche. Bezahlen will sie ihn nicht. Ladendetektiv Rainer beobachtet alles über einen Spiegel an der Decke. Noch bevor Monika die Kasse erreicht, spricht er sie ruhig an.
>
> Variante 1: Bevor Rainer sie anspricht, legt Monika den Lippenstift von sich aus zurück ins Regal.
> Variante 2: Monika stellt eine schwere Kiste Wein offen in den Einkaufswagen, um sie ohne Bezahlung hinauszuschieben. Rainer spricht sie vor der Kasse an.
> Variante 3: Monika versteckt den Lippenstift im Einkaufswagen unter einer Zeitung und legt an der Kasse nur die übrigen Waren aufs Band.
>
> **Hat Monika einen vollendeten Diebstahl begangen?**
