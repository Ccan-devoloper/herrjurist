# Folge 017 · Zugang Willenserklärung § 130 BGB: Wann ist der Brief angekommen? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_017.py`](src/skript_017.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · BGB AT, Themenplan-Format „Schema“. Ein frei erfundener Fall nach dem Plan-Hook trägt das Schema („Silvester-Fall“): Café-Inhaberin Helga muss den Wartungsvertrag mit Werners Firma bis 31. Dezember kündigen; sie wirft den Brief an Silvester um 23 Uhr in den Briefkasten von Werners Büro, Werner leert ihn am 2. Januar. Prüfung des Wirksamwerdens nach § 130 I: I. Abgabe, II. Zugang (Machtbereich, Kenntnisnahme unter gewöhnlichen Umständen, BGH XII ZR 148/05), III. kein Widerruf (§ 130 I 2), Ergebnis. Gegen- und Sonderfälle: E-Mail im Geschäftsverkehr (BGH VII ZR 895/21), Empfangsbotin Paula und eigener Bote (Erklärungsbote), grundlose Annahmeverweigerung (§ 242), Beweis beim Einwurf-Einschreiben (BAG/BGH). Klausurtipp, Schema I.–IV., Merksatz. Der E-Mail-Zugang wurde in 014 ausdrücklich auf diese Folge verschoben.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Helga (HE), um 50 | Café-Inhaberin, Kündigende (Erklärende) | `standing/blazer-4` (lila Blazer `#B8A9F5`, weißes Oberteil, schwarze Hose), Kopf `Gray Medium` (rotbraun), Brille `Glasses 2`, Haut `#E8B894`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile` (froh), `Concerned|Serious` (Sorge), `Serious` (denkt), `Suspicious` (überlegt) | `laura_klar` (Frau, mittel) |
| Werner (WE), um 55 | Inhaber der Wartungsfirma, Empfänger | `standing/shirt-4` (schwarzes Hemd, Hose Blau `#8DB3F2`), Kopf `No Hair 1`, Brille `Glasses 4`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet „Zu spät!“), `Very Angry` (redet „Den nehme ich nicht an!“), `Suspicious`, `Serious` (liest), `Cheeky|Smile` (froh), `Tired` | `marc` (Mann, mittel) |
| Paula (PA), um 25 | Werners Büroangestellte, Empfangsbotin | `standing/resting-1` (grünes Oberteil `#8FD694`), Kopf `Long`, Haut `#D9A47A`; Mimiken `Calm`, `Smile` (redet), `Cute` | `ela_froh` (Frau, jung) |
| Bote (BO) | Helgas eigener Bote (Erklärungsbote), spricht nicht | `standing/walking-1` (orange T-Shirt `#F9A66C`), Kopf `Short 4`, Haut `#C99470`; Mimiken `Calm`, `Concerned|Serious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel bzw. zum Briefkasten, `_r` blickt nach rechts (Helga im Café zu Werner und bei der Übergabe an Paula, der Bote zu Werner). Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 bewusst nicht gewählt), keine Bärte. **Alle Grundmimiken mit geschlossenem Mund** (FOLGE-ABLAUF); Mundzustände a/o/e nur in den sprechenden Ansichten `HE_redet`, `WE_redet`, `WE_abwehr`, `PA_redet` (je links/rechts) und Lexi. Stimmen nur aus dem zugeteilten Pool (laura_klar, marc, ela_froh; `otto` nicht benötigt, der Bote spricht nicht). Namen mit eindeutig deutscher Aussprache (Helga, Werner, Paula), anders als in 014 (Gerd, Lotte, Malte) und 015 (Otto, Konrad, Ina, Rudolf, Bernd, Gerda). Figuren-PNGs: `../peeps/op_017/` (68 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 014: Hof mit Kombi, Schreibtisch/Handy, Wochenleiste (Fristen bei Angebot und Annahme); 015: Kleingartenanlage. 017: Café und Bürogebäude mit Briefkasten an der Straße, eine **Nachtszene** (Silvester 23 Uhr – der Fall verlangt die Nacht, Verlauf wie 007), Tagesbild am 2. Januar am selben Ort (bewusste Rückkehr: gleicher Briefkasten, nun bei Tag), danach Tafelfolien mit Briefkasten, Mailserver, Tür, Belegen.
- Neue Posen (`blazer-4`, `shirt-4`, `resting-1`, `walking-1`) gegenüber 014 (`robot_dance-3`, `polka_dots`, `Hoodie`) und 015.
- Keine Wochenleiste wie in 014; stattdessen eine Drei-Tage-Leiste 31.12. / 1.1. / 2.1. in Szene H.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Café** `fall`→`silv` | Bodenlinie, links Helgas Café, Helga blickt zu Werner; Werner kommt mit Werkzeug; Vertrag in der Mitte | tabler:`building-store` (Gelb), `coffee`, `tools`, `file-text`, `writing`, `mail` | `Fall · Der Wartungsvertrag` (ab 0,0 s) → `Fall · Die Kündigung` | Café + Helga · Kaffeetasse · Werner · Wartung · Vertrag · „+1 Jahr“ · „bis 31. Dezember“ · Silvester: Werner weg, Helga schreibt · Brief | – |
| **B Silvesternacht** `einwurf`→`h1` | Nacht, Werners Büro, Briefkasten am Pfosten, Helga rechts davon | Mond (`mond()`), tabler:`building` (Nachtblau), `mailbox` (weiß → gelb, sobald der Brief drin ist), `clock-hour-11`, `mail` (wandert in den Schlitz) | `Fall · Silvester, 23 Uhr` | Büro, Mond, „31. Dezember“ · „23 Uhr“ · Brief wandert · Briefkasten gefüllt · Helga redet, Blase | Brief fällt in den Briefkasten (`szene_017einwurf_1`) |
| **C Der zweite Januar** `jan`→`frage` | Derselbe Ort bei Tag; Werner leert den Briefkasten, liest, protestiert | tabler:`sun`, `building` (Blau), `lock`, `mailbox`, `mail-opened` | `Fall · Der zweite Januar` → `Fall · Die Frage` | „über Neujahr geschlossen“ + Schloss · Werner kommt, „2. Januar“ · Klappe, Brief wandert zu Werner, liest · Werner redet, Blase · Frage-Pille, Werner froh | Briefkastenklappe (`szene_017klappe_1`) |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **E Wirksamwerden** `norm`→`glied` | Tafel links, Helga und Werner rechts, Brief | tabler:`mail` | `Wirksamwerden · § 130 Abs. 1 S. 1 BGB` → `Wirksamwerden · Abgabe, Zugang, kein Widerruf` | empfangsbedürftig · Abwesenheit · § 130 · wirksam mit Zugang · drei Blöcke nacheinander | – |
| **F I. Abgabe** `abg`→`abg_ok` | Tafel, Brief wandert von Helga in den Briefkasten | tabler:`mailbox`, `mail` | `I. Abgabe` | willentlich · erreichen · Einwurf ✓ · Block | – |
| **G II. Zugang** `zug`→`feste` | Tafel, Briefkasten, Auge, Uhr mit Fragezeichen | tabler:`mailbox`, `eye`, `clock-question` | `II. Zugang › Machtbereich` → `II. Zugang › Kenntnisnahme zu erwarten` | Machtbereich · Briefkasten ✓ · Kenntnisnahme · gewöhnliche Umstände · Verkehrsanschauung · ✗ tatsächliches Nachsehen · „keine feste Uhrzeit“ | – |
| **H II. Zugang: BGH Silvester** `bgh`→`zug_erg` | Tafel mit Drei-Tage-Leiste, Bürogebäude mit Schloss, Mond → Kalender | tabler:`building`, `lock`, `moon`, `calendar-event` | `II. Zugang › nach Geschäftsschluss, BGH` | BGH-Zeilen · Silvester nachmittags · Az. · 31.12. ✗ / 1.1. ✗ / 2.1. ✓ · Block „Zugang erst am 2. Januar“ | – |
| **I III. Widerruf, Ergebnis** `wid`→`erg2` | Tafel; Telefon bei Helga, geöffneter Brief bei Werner | tabler:`phone-call`, `mail-opened`, `calendar-event` | `III. kein Widerruf, § 130 Abs. 1 S. 2 BGB` → `Ergebnis · Zugang erst am 2. Januar, zu spät` | § 130 I 2 · vorher/gleichzeitig · Anruf ✗ · ungelesen · Block zu spät · Block Verlängerung, „+ 1 Jahr“ | – |
| **J Gegenfall E-Mail** `mail`→`mail4` | Tafel; Laptop Helga, Mailserver Werner, Mail wandert | tabler:`device-laptop`, `server`, `mail`, `clock`, `clock-question` | `Gegenfall · E-Mail im Geschäftsverkehr` | Pille 30.12. · BGH-Zeilen · Az. · Lesen egal ✓ · offengelassen | – |
| **K Empfangsbotin** `bote`→`weiter` | Tafel; Helga übergibt Paula den Brief, Paula redet | tabler:`mail`, `desk` | `Sonderfall · Empfangsbotin` | Silvestermorgen · Paula kommt, Brief wandert · Büroangestellte · Empfangsbotin · Paula redet, Blase, Schreibtisch · Weitergabe · Az. | – |
| **L Erklärungsbote, Verweigerung** `erkl`→`zumut` | Tafel; Bote mit Brief vor Werners Tür, Werner wehrt ab | tabler:`door`, `mail`, `mail-check`, `hand-stop` | `Sonderfall · Erklärungsbote` → `Sonderfall · Annahme verweigert, § 242 BGB` | Bote · Risiko · Werner kommt (Klingel) · Werner redet, Hand, Blase · Treu und Glauben, Brief gilt als zugegangen · § 242 · Zumutbares · Az. | Türklingel (`szene_017klingel_1`) |
| **M Beweis** `bew`→`scan` | Tafel; Belege als Requisiten | tabler:`receipt`, `file-certificate`, `scan` | `Beweis · Einwurf-Einschreiben` | Beweislast · Einlieferungsbeleg ✗ · Auslieferungsbeleg ✓ · Scan ✗ · Az. | – |
| **N Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · zwei Fragen beim Zugang` | Satz · Frage 1 · Frage 2 · ✗ gelesen | – |
| **O Klausurschema** `sch`→`k4` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · II. · 1. · 2. · 3. · III. · IV. | – |
| **P Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker · Schlusssatz | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo ein Brief oder eine Mail tatsächlich unterwegs ist.
**Geräusche:** drei Handlungsgeräusche aus Freesound CC0 (`szene_017einwurf_1`, `szene_017klappe_1`, `szene_017klingel_1`), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen. Tafeln verwenden Ziffern („31. Dezember“, „23 Uhr“, „§ 130 Abs. 1 S. 2 BGB“).

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Helga betreibt ein kleines Café. Die Firma von Werner wartet ihre Kaffeemaschine. Laut Vertrag verlängert sich der Wartungsvertrag um ein Jahr, wenn Helgas Kündigung Werner nicht bis zum 31. Dezember zugeht. Eine Form ist nicht vereinbart.
>
> Helga schreibt die Kündigung erst an Silvester und wirft den Brief um 23 Uhr in den Briefkasten von Werners Büro. Das Büro ist, wie in der Branche üblich, an Silvester nachmittags und an Neujahr geschlossen. Werner leert den Briefkasten am Morgen des 2. Januar, einem Werktag, und meint, die Kündigung sei zu spät gekommen.
>
> *(Frei erfundener Übungsfall.)*
>
> **Ist Helgas Kündigung rechtzeitig wirksam geworden?**
