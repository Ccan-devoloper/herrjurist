# Folge 014 · Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_014.py`](src/skript_014.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · BGB AT, Themenplan-Format „Schema“. Ein frei erfundener Fall unter Abwesenden trägt das ganze Schema: Gerd bietet Lotte am Sonntag per E-Mail seinen Kombi für 4.000 € an, „Mein Angebot gilt bis Freitag“ (§ 148). Am Mittwoch bietet Malte mehr, Gerd widerruft per Mail – zu spät (§ 145, § 130 I 2). Lotte nimmt am Donnerstag an: Vertrag mit Zugang der Annahme geschlossen. Gegenfälle: Annahme erst am Samstag (§§ 146, 150 I, Schweigen), Angebot ohne Frist (§ 147 II, Zusammensetzung der Frist nach BGH), Telefon „Deal!“ (§ 147 I 2 – greift den Plan-Hook auf). Klausurtipp „Zeitleiste“, Schema I.–IV., Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gerd (GE), um 70 | Verkäufer, Antragender | Pose `standing/robot_dance-3` (offene Hand), Kopf `No Hair 3`, Brille `Glasses 3`; Oberteil Blau `#8DB3F2`, Hose `#3D3D58`, Haut `#EBC4A0`; Mimiken `Calm`, `Smile` (redet/froh), `Serious` (Protest, redet), `Suspicious` (denkt), `Contempt` (verärgert), `Concerned|Serious` (Sorge) | `johann` (Mann, älter) |
| Lotte (LO), um 25 | Käuferin, Annehmende | Pose `standing/polka_dots`, Kopf `Medium Straight`; Hose Lila `#B8A9F5`, Haut `#C99470`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile` (froh), `Serious` (denkt), `Suspicious` (überlegt), `Concerned|Serious` (Sorge) | `lucy` (Frau, jung) |
| Malte (MA), um 30 | zweiter Interessent, nur im Telefonbild | Brustbild `body/Hoodie`, Kopf `Short 2`; Hoodie Orange `#F9A66C`, Haut `#F0C8A8`; Mimiken `Calm`, `Driven` (redet) | `timo` (Mann, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Gerd in den Fallszenen zu Lotte). Keine Prothesen-Posen, keine Bärte. **Alle Grundmimiken mit geschlossenem Mund** (FOLGE-ABLAUF); Mundzustände a/o/e nur in den sprechenden Ansichten `GE_redet`, `GE_protest`, `LO_redet`, `MA_redet` (je links/rechts) und Lexi. Stimmen nur aus dem zugeteilten Pool (lucy, timo, johann; `laura_ruhig` nicht benötigt). Namen mit eindeutig deutscher Aussprache (Gerd, Lotte, Malte). Figuren-PNGs: `../peeps/op_014/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 012: Amtsgericht/Klavier (Seidel, Krüger); 013: Himmel, Lagezentrum, Flughafen (Lorenz, Pilotin, Seiler).
- 003 (Flohmarkt, § 150 II unter Anwesenden) und 002 (Internetanzeige als invitatio): bewusst **nicht** wiederholt. 014 spielt unter Abwesenden per E-Mail mit Fristfragen; § 150 II und die invitatio nur je ein Satz.
- Neue Posen (robot_dance-3, polka_dots, Brustbild Hoodie) gegenüber 012/013; Schauplätze Hof mit Kombi, Gerds Schreibtisch und Lottes Handy im geteilten Bild, Wochenleiste als wiederkehrendes Element. Cremegrund, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Probefahrt** `fall`→`probe` | Bodenlinie, Gerd links (blickt zu Lotte), Kombi, Lotte kommt | tabler:`car` (Blau), `key` (Gelb, wandert von Gerd zu Lotte) | `Fall · Die Probefahrt` (ab 0,0 s, Elemente ab −0,4 s) | 1 Gerd, Kombi, „Samstag“ · 2 „alter Kombi“ · 3 „zu verkaufen“ · 4 Lotte kommt · 5 Schlüssel wandert · 6 „Probefahrt“, Lotte froh | Schlüsselklirren (Übergabe) |
| **B E-Mails der Woche** `mail`→`frage` | Geteiltes Bild: links Gerd am Tisch mit Laptop, rechts Lotte mit Handy; oben Wochenleiste So–Sa | tabler:`desk`, `device-laptop`, `device-mobile`, `mail`, `mail-opened`, `phone-call`, `mail-x` (Rot), `mail-check` (Grün) | `Fall · Die E-Mail am Sonntag` → `Fall · Mittwoch: Malte ruft an` → `Fall · Donnerstag: Lottes Antwort` → `Fall · Die Frage` | So markiert · Mail wandert · Gerd redet, Blase (Mailtext) · „Frist bis Freitag“ · gelesen: Sonntag · Mi · Telefon · Telefonbild Malte · Malte redet, Blase · Widerrufsmail wandert, Zitat-Pille · Do · Antwortmail wandert zurück · „gelesen: Donnerstagmittag“ · Lotte redet, Blase · Gerd protestiert, Blase · zwei Frage-Pillen | Telefonklingeln (Mittwoch) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **D Anspruch** `ansp`→`vertrag` | Tafel links, Gerd und Lotte rechts, Kombi darüber | tabler:`car` | `Lotte gegen Gerd · § 433 I 1 BGB` → `Kaufvertrag · Angebot und Annahme, §§ 145 ff. BGB` | Anspruch · Kaufvertrag · zwei Erklärungen · Block Angebot · Block Annahme · §§ 145 ff. | – |
| **E I. Angebot** `ang`→`ang_ok` | Tafel, Figuren | tabler:`car`, `currency-euro`, `users`, `mail`, `speakerphone`, `mail-opened` | `I. Angebot › wesentliche Punkte` → `› Rechtsbindungswille` → `› Zugang, § 130 I 1 BGB` | Ware · Preis · Vertragspartner (je Pille + Requisit) · „Ja“ ✓ · Bindungswille · Zitat ✓ · Werbeschreiben ✗ · Abwesende · Zugang · gelesen ✓ · Block „wirksam“ | – |
| **F II. Bindung** `bind`→`spaet` | Tafel mit Mini-Zeitleiste So–Mi | tabler:`mail`, `mail-x` | `II. Bindung › § 145 BGB` → `II. Bindung › Widerruf, § 130 I 2 BGB` | Frage-Pille · § 145 · Ausnahme · § 130 I 2 · vorher/gleichzeitig · Zeitleiste · Widerruf ✗ · „drei Tage zu spät“ · Block „Das Angebot steht“ | – |
| **G III. Annahme, Ergebnis** `ann`→`pflicht` | Tafel mit Wochenleiste und Frist | tabler:`mail-check`, `calendar-event`, `car` (wandert zu Lotte) | `III. Annahme › deckungsgleich` → `› Änderungen, § 150 II BGB` → `› rechtzeitig, § 148 BGB` → `Ergebnis · Vertrag am Donnerstag geschlossen` | deckungsgleich ✓ · 3.500 € · § 150 II · Frist · Fr rot · Do grün ✓ · Block Ergebnis · Pflichten, Kombi wandert | – |
| **H Gegenfall Samstag** `sams`→`schweig` | Tafel, Wochenleiste mit Sa | tabler:`mail` (Orange, Lotte→Gerd), `message-off` | `Gegenfall · Antwort erst am Samstag` → `Gegenfall · neues Angebot, § 150 I BGB` | Sa · erloschen ✗ · neues Angebot · Gerd muss annehmen · Block Schweigen | – |
| **I Gegenfall ohne Frist** `ohne`→`drei` | Tafel, Mail wandert hin, Sanduhr, Antwort zurück | tabler:`clock`, `mail`, `hourglass`, `mail-check` | `Gegenfall · ohne Frist, § 147 II BGB` | § 147 II · regelmäßige Umstände · BGH-Zeile · Hinweg · Überlegungszeit · Rückweg | – |
| **J Gegenfall Telefon** `tel`→`spaeter` | Tafel, beide mit Handy | tabler:`device-mobile` | `Gegenfall · am Telefon, § 147 I BGB` | Anwesende · § 147 I · Pille „Kombi für 4.000 €?“ · Lotte redet „Deal! Abgemacht.“ · ✓ Vertrag · ✗ später | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Zeitleiste` | Zeitleiste · Angebot · Widerruf · Annahme/Fristende · ✗ · ✓ | – |
| **L Klausurschema** `sch`→`k4` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · 1. · 2. · II. · III. · 1. · 2. · IV. (+) | – |
| **M Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo etwas übergeben oder verschickt wird (Schlüssel, E-Mails, Kombi).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_014schluessel_1`, `szene_014telefon_1`), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort). Tafeln dürfen Ziffern verwenden („4.000 €“).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Gerd möchte seinen alten Kombi verkaufen. Am Samstag macht Lotte eine Probefahrt. Am Sonntagabend schreibt Gerd ihr per E-Mail: „Liebe Lotte, du kannst den Kombi für 4.000 Euro haben. Mein Angebot gilt bis Freitag.“ Lotte liest die Mail noch am Sonntag.
>
> Am Mittwoch bietet Malte Gerd am Telefon 4.500 Euro. Gerd schreibt Lotte sofort: „Ich ziehe mein Angebot zurück.“ Am Donnerstagmittag antwortet Lotte per E-Mail: „Ich nehme den Kombi für 4.000 Euro!“ Gerd liest die Mail gleich und meint, er habe sein Angebot doch zurückgezogen.
>
> *(Frei erfundener Übungsfall.)*
>
> **Kann Lotte von Gerd den Kombi verlangen – und wann kam der Vertrag zustande?**
