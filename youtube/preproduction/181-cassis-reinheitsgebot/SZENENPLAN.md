# Folge 181 · Cassis de Dijon: Warum fremdes Bier trotz Reinheitsgebot rein darf – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_181.py`](src/skript_181.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · Öffentliches Recht/Europarecht. Voraussetzung: Folge 176 (Prüfschema Art. 34 AEUV mit Dassonville) – das Schema wird nicht wiederholt, nur verwiesen. Ablauf: Fall im Getränkehandel (Herr Brodersen will ein belgisches Bier mit Reis und Mais verkaufen, Frau Timmermann: „nach dem Reinheitsgebot kein Bier“) → Sachverhalt → Einordnung (Verweis auf 176, Schwerpunkt Rechtfertigung) → **Cassis de Dijon 1979** (der echte Fall ohne Figuren; unterschiedslos anwendbar; Cassis-Formel Rn. 8 als Zitatkarte; Deutschlands Argumente und das Etikett, Rn. 9–13; Rn. 14 und gegenseitige Anerkennung) → **Reinheitsgebot 1987** (der echte Fall ohne Figuren; Bezeichnungsverbot Rn. 29–37; Zusatzstoffverbot mit Art. 36 AEUV als Wortlautkarte, Rn. 40–53; Tenor; heute § 1 Abs. 2 BierV als Wortlautkarte, Inländerdiskriminierung) → Lösung → zurück im Getränkehandel → Klausurtipp (Lexi) → Schema der Rechtfertigung → Merksatz (Lexi). Hauptfilm 6:41,8 (Begründung in ABNAHME.md).

**Darstellung (Vorgabe Koordinator):** Bier und Likör nur als neutrale Flaschen-, Kisten- und Fass-Icons ohne Marke (Tabler `bottle`, `package`, `barrel`); kein Trinken, keine Gläser, keine Bar. Händler und Kontrolleurin fiktiv. Rewe-Zentral nur sachlich als Name auf der Tafel, kein Logo, keine Figur. Keine Länderflaggen, keine Klischees; „Belgien“ und „Frankreich“ nur als Wort.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Brodersen (BD), um 45 | betreibt einen Getränkehandel | `standing/easing-2` (offenes Hemd Lila `#B8A9F5` über schwarzem Shirt aus der Pose, Hose Anthrazit `#3A3A44`, weiße Schuhe), Kopf `Short 1`, Haut `#E8B98F`, ohne Brille, ohne Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned\|Serious` (Sorge), `Awe`, `Driven` | `christian` (Mann, mittel) |
| Frau Timmermann (TM), um 30 | Lebensmittelüberwachung | `standing/resting-2` (schwarzer Pullover aus der Pose, Hose Blau `#5E7FB8`, schwarze Schuhe), Kopf `Medium Straight`, Brille `Glasses`, Haut `#F2C9A4`. Mimiken `Calm`, `Serious` (redet/ernst), `Smile` (redet einsichtig/froh), `Suspicious`, `Awe`, `Solemn` | `lucy` (Frau, jung) |
| Rewe-Zentral, Kommission, Bundesregierung | Beteiligte der echten Fälle | **keine Figuren**, nur als Name auf Tafeln und im Sprechtext; keine Logos, keine Flaggen | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): ein Mann, eine Frau; stephan nicht verwendet (keine Paarung stephan/christian). 176: laura_ruhig, william; 177: hilde, christian (andere Rollen); 179: sabrina, marc; 180 (parallel): helmut, ela_froh.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und vor Produktionsbeginn in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt am 04.10.2026: je 0 Treffer): **Brodersen**, **Timmermann** („Albers“ verworfen, 34 Treffer). Kein Genitiv eines Namens.
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Getränkehandel: Herr Brodersen links blickt nach rechts zu Frau Timmermann, sie blickt nach links zu ihm (Kopfausschnitte geprüft). Tafeln: Figuren rechts blicken zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `BD_redet`, `TM_redet`, `TM_einsicht` (je beide Blickrichtungen) und Lexi. 58 Figuren-PNGs in `../peeps/op_181/` (nicht im Repository, im Drive-Master).
- **Verworfen:** `crossed_arms-1`/`Glasses 4` für Frau Timmermann und Kopf `Short 3` für Herrn Brodersen, weil die parallel produzierte Folge 180 sie verwendet.

**Abweichung von den letzten Folgen:** 176 (blazer-1, pointing_finger-2), 177 (blazer-3, robot_dance-2), 178 (resting-1, shirt-3), 179 (blazer-4, shirt-3, crossed_arms-2), 180 (easing-1, crossed_arms-1, robot_dance-3, shirt-4) – 181 nutzt **easing-2** und **resting-2**; keine Polka Dots, keine Bärte, keine Prothesen-Posen. **Schauplatz neu:** Verkaufsraum eines Getränkehandels mit Regal, neutralen Flaschen, Kisten und zwei Fässern; vorn die neue gelbe Kiste mit dem belgischen Bier. Anders als das Lager in 176 (Großhandel, Whisky) mit Fass und Ladentür; die Lösung kehrt in den Getränkehandel zurück, weil dort entschieden wird, ob das Bier Bier heißen darf.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall** `fall`→`frage` | Getränkehandel; Herr Brodersen links ab 0,0 s mit Namensschild, Titelpille „Getränkehandel“; die neue Kiste erscheint; Pillenband (Bier aus Belgien → Gerstenmalz, Reis, Mais mit drei Icons); Tür, Frau Timmermann kommt, Pille „Lebensmittelüberwachung“; Blase Timmermann; Blase Brodersen; Frage-Pillen | tabler `bottle` (Bernstein), `package` (Karton, neue Kiste Gelb), `barrel` (Holz), `wheat`, `door`; Fluent Emoji High Contrast `sheaf-of-rice`, `ear-of-corn` | `Fall · Herr Brodersen und das Bier aus Belgien` → `· Frau Timmermann prüft` → `· Die Frage` | Kiste (`szene_181kiste_1`, Freesound CC0 19830), Tür (`szene_181tuer_1`, CC0 702171) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | – |
| **C Einordnung** `verweis`→`zwei` | Tafel „Heute: die Rechtfertigung“; Verweis auf das Video zu Dassonville; zwei Klassiker-Kästen; Herr Brodersen rechts | – | `Einordnung › Prüfschema Art. 34 AEUV: Video zu Dassonville` → `› heute: die Rechtfertigung` | – |
| **D1 Der Fall Cassis** `c79`→`cgehalt` | Tafel, rechts Requisiten im Wechsel (ohne Figuren): Likörflasche, Lieferwagen, Behörde, Verbot, Flasche; Kreuz „Cassis: nur 15 bis 20 %“ | tabler `bottle` (Lila), `truck-delivery`, `building-bank`, `ban` | `Cassis de Dijon, EuGH 1979 · Der Fall` → `· nicht verkehrsfähig` | – |
| **D2 Unterschiedslos** `unter`, `behind` | zwei Haken (Deutschland/Ausland), grüner Block, lila Block „Maßnahme gleicher Wirkung“; beide Figuren | – | `… › unterschiedslos anwendbare Maßnahme` → `› Maßnahme gleicher Wirkung` | – |
| **D3 Cassis-Formel** `formel`→`neben` | Zitatkarte Rn. 8 mit acht Markern (vier Beispiele einzeln), gelber Block „neben den Gründen aus Art. 36 AEUV“; Frau Timmermann rechts | – | `… › zwingende Erfordernisse, Rn. 8` → `› neben Art. 36 AEUV` | – |
| **D4 Argumente** `gesund`→`milder` | zwei Argumente mit Kreuz, grüner Block „Etikett: das mildere Mittel“; Requisiten rechts | tabler `activity-heartbeat`, `scale`, `label`, `bottle` | `… › Gesundheit?` → `› unlauterer Wettbewerb?` → `› Etikett als milderes Mittel` | – |
| **D5 Anerkennung** `anerk`, `grundsatz` | Zitatkarte Rn. 14 mit drei Markern; Block „heute: Grundsatz der gegenseitigen Anerkennung“; beide Figuren | – | `… › gegenseitige Anerkennung` | – |
| **E1 Der Fall Reinheitsgebot** `r87`→`nurde` | Tafel (ohne Figuren), Requisiten im Wechsel: Fass, Hammer, Gerste, Reis, Kolben, Fabrik; Kreuz „Reis und Mais: kein Getreide“; grauer Kasten „Brauvorschrift nur für Brauereien in Deutschland“ | tabler `barrel`, `gavel`, `wheat`, `flask`, `building-factory-2`; Fluent HC `sheaf-of-rice` | `Reinheitsgebot, EuGH 1987 · Der Fall` → `· § 10 Biersteuergesetz a. F.` → `· Brauvorschrift nur für Brauereien in Deutschland` | – |
| **E2 Bezeichnungsverbot** `name`→`gattung` | Zeilen zum Wort, Zitatkasten „zementieren“; Frau Timmermann rechts (ihr Argument wird geprüft) | – | `… › 1. Bezeichnungsverbot` → `› Verbraucherschutz?` | – |
| **E3 Etikett** `etik2`→`v1` | grüner Block, Haken/Kreuz, roter Block „Bezeichnungsverbot: Verstoß“; Etikett-Icon zwischen den Figuren | tabler `label` | `… › Etikett als milderes Mittel` → `› Verstoß` | – |
| **E4a Zusatzstoffe** `zus`→`erf` | Wortlautkarte Art. 36 AEUV (Auszug) mit Marker „zum Schutze der Gesundheit …“, Haken „Zulassungspflicht grundsätzlich zulässig“, gelber Block; Requisiten rechts | tabler `flask`, `shield-check`, `certificate`, `scale` | `… › 2. Zusatzstoffverbot` → `› Art. 36 AEUV` → `› nur so weit tatsächlich erforderlich` | – |
| **E4b Pauschalverbot** `muss`→`v2` | zwei Haken, grüner Block „dann muss der Einfuhrstaat zulassen“, zwei Kreuze, roter Block; beide Figuren | – | `… › im anderen Mitgliedstaat zugelassen` → `› pauschales Verbot` → `› unverhältnismäßig` | – |
| **E5 Ergebnis und heute** `tenor`→`ilnd` | Tenor; Wortlautkarte § 1 Abs. 2 Satz 1 BierV mit zwei Markern; Zeile § 1 Abs. 1 BierV; Block „Inländerdiskriminierung“; beide Figuren | – | `Reinheitsgebot, EuGH 1987 · Ergebnis` → `Heute · § 1 Abs. 2 BierV` → `Heute · Inländerdiskriminierung` | – |
| **F1 Lösung** `loes`→`l4` | drei Haken, roter Block „Verbot wäre unverhältnismäßig“; beide Figuren | – | `Lösung · Herr Brodersen` → `· Etikett statt Verbot` | – |
| **F2 Zurück im Getränkehandel** `l5`, `t2` | Schauplatz A; Pillen „darf als Bier verkauft werden“, „Etikett: Gerstenmalz, Reis und Mais“, Etikett an der Kiste; Blase Timmermann | wie A, tabler `label` | `Lösung · Das Bier darf Bier heißen` | – |
| **G Klausurtipp** `tipp`→`eng` | hellgelbe Tafel, Lexi warnt; zwingende Erfordernisse nur bei unterschiedslosen Maßnahmen, sonst allein Art. 36, abschließend und eng | Warnsymbol (Streamline Freehand) | `Klausurtipp · zwingende Erfordernisse nur bei unterschiedslosen Maßnahmen` → `· nur eingeführte Waren betroffen: allein Art. 36 AEUV` | – |
| **H Schema** `sch`→`s2b` | breite Karte, I. Rechtfertigungsgrund (1., 2. mit Zusatz), II. Verhältnismäßigkeit (1., 2. mit Beispiel), Fundstellen rechts | – | `Schema · Rechtfertigung` → `› I. Rechtfertigungsgrund` → `› II. Verhältnismäßigkeit` | – |
| **I Merksatz** `merke`, `m2` | Lexi erklärt, zwei Sätze mit drei Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Stil-C-Pflicht per Assertion), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Blasen als Ziffern („25 %“, „15 bis 20 %“, „§ 10“, „20.2.1979“, „Rn. 8“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Kiste wird abgestellt, Tür), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT): bottle, package, barrel, wheat, door, truck-delivery, building-bank, ban, activity-heartbeat, scale, label, gavel, flask, building-factory-2, shield-check, certificate; Fluent Emoji High Contrast (MIT): sheaf-of-rice, ear-of-corn, Haken/Kreuz; Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Regal und Boden aus Grundformen. Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Brodersen betreibt einen Getränkehandel. Neu im Sortiment hat er ein Bier aus Belgien, gebraut aus Gerstenmalz, Reis und Mais. In Belgien wird es rechtmäßig als Bier verkauft.
>
> Frau Timmermann von der Lebensmittelüberwachung meint, nach dem Reinheitsgebot sei das kein Bier. Unter dieser Bezeichnung dürfe er es nicht verkaufen.
>
> **Darf ein Staat den Namen „Bier“ nach eigenen Brauregeln reservieren?**

Kein Fiktiv-Hinweis; die Quellen der echten Fälle (EuGH, Datum, Rs.) stehen auf den Tafeln.
