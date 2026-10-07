# Folge 223 · Mittellose Ehefrau bürgt: Ist die Angehörigenbürgschaft sittenwidrig? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_223.py`](src/skript_223.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall; Zivilrecht, weitere Vertragstypen. Fiktiver Fall nach dem Plan-Hook („Die Ehefrau ohne eigenes Einkommen bürgt für 200.000 Euro Firmenkredit ihres Mannes“): Tischlermeister Gero braucht für neue Maschinen einen Firmenkredit über 200.000 € (Zinsen 1.000 € im Monat). Herr Wittkamp von der Bank verlangt die Bürgschaft seiner Frau Anneke, die kein Einkommen und kein Vermögen hat. Sie unterschreibt „Ich bürge für den Firmenkredit von Gero über 200.000 Euro.“ Drei Jahre später sind nach der Kündigung 180.000 € offen; die Bank verlangt sie von Anneke.

Ablauf: Fall (Werkstatt, Bank, Bitte, Urkunde, Zahlungsverlangen) → Frage → Sachverhalt → Anspruch § 765 Abs. 1 (Wortlautkarte), Einigung, Form § 766 S. 1, Hauptschuld → Problem § 138 → Bürgschaftsbeschluss BVerfGE 89, 214 (Tochter; Wortlautkarte Art. 2 Abs. 1 GG; Privatautonomie, Fremdbestimmung; Pflicht der Zivilgerichte, Generalklauseln §§ 138, 242) → § 138 Abs. 1 (Wortlautkarte) mit BGH-Kriterien (XI ZR 82/11 Rn. 9; XI ZR 32/16 Rn. 20) → Vermutung und Widerlegung → Subsumtion (XI ZR 32/16 Rn. 29 f.) → Ergebnis (Bühne) → Gegenfall eigenes Interesse (XI ZR 32/16 Rn. 29 f.; BVerfGE 89, 214, 235 f.) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Sprachspur 346,1 s (5.129 Zeichen Skript); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Anneke (AN), um 32 | Bürgin, Ehefrau von Gero, ohne eigenes Einkommen | `standing/shirt-3` (türkisfarbene Bluse `#7FD6D0`, schwarze Hose), Kopf `Medium Straight` (dunkelbraun `#5A3A28`), Haut `#F0C8A8`; Mimiken `Calm`, `Serious` (redet), `Concerned|Serious`, `Suspicious`, `Smile`, `Tired` | `julia` (Frau, jung) |
| Gero (GE), um 35 | Tischlermeister, Hauptschuldner | `standing/shirt-4` (schwarzes Hemd, blaue Arbeitshose `#6F8FC9`), Kopf `Short 4`, Haut `#E3B08C`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Tired` | `niklas` (Mann, jung) |
| Herr Wittkamp (WI), um 60 | Firmenkundenberater der Bank (Gläubigerseite) | `standing/blazer-3` (schiefergrauer Blazer `#6B7A8F`, weißes Shirt, dunkle Hose `#3D3D58`), Kopf `No Hair 2`, Brille `Glasses 3`, Haut `#EBC29E`; `Calm`, `Serious` (redet), `Smile`, `Solemn` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt` (Eintrag „223: Anneke, Gero, Wittkamp“ vor der Vertonung) und per Volltextsuche (`grep -rlw`, Text- und Codedateien unter `youtube/`) in keiner früheren Folge vergeben. Verworfen: Henrike (106/127, 146/199 erwähnt), Jannik (010), Lasse (094/206), Annelie (ecU9), Marit (ecE1), Hasselbach/Tegtmeier (zulässig, aber länger). Kein Genitiv eines Namens im Sprechtext („die Werkstatt von Gero“, „die Hauptschuld von Gero“).
- **Stimmen nur aus dem Pool** (`niklas`, `helmut`, `ela_froh`, `julia`): `julia` für Anneke, weil `ela_froh` nicht für ernste Rollen vorgesehen ist und die Bürgin die ernste Hauptrolle ist (zwei kurze Sätze; „julia möglichst meiden“ deshalb nicht einhaltbar); `niklas` für Gero (jung), `helmut` für den älteren Bankmitarbeiter. Vorfolge 220: `niklas`, `helmut` (Überschneidung durch den vorgegebenen Pool unvermeidbar).
- Präfixe `AN_`/`GE_`/`WI_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts.
- **Blickrichtung:** Werkstatt: Gero nach links zur Werkbank. Bank: Herr Wittkamp (links, hinter dem Schreibtisch) nach rechts; Gero nach links zu ihm, bei seiner Bitte nach rechts zu Anneke; Anneke nach links zu Gero/Bank. Drei Jahre später: Wittkamp nach rechts zu Anneke, Anneke und Gero nach links. Ergebnis: Wittkamp nach rechts, Anneke und Gero nach links. Tafelszenen: beide Figuren nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AN_redet`, `GE_redet`, `WI_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild; die Beschwerdeführerinnen des Bürgschaftsbeschlusses werden nicht als Figuren gezeigt (reale Personen).
- **Darstellung:** Anneke sachlich und selbstbestimmt (sie entscheidet sich bewusst für die Werkstatt, sagt klar „Davon kann ich nicht einmal die Zinsen bezahlen“), keine naive Karikatur, keine Schürze o. Ä.; Gero als Handwerker ohne Klischee (kein Hochstapler, die Aufträge bleiben aus); die Bank sachlich, kein Logo, keine „fiese“ Figur. Keine Bärte.
- **Abwechslung:** Posen nicht aus 220 (`robot_dance-2`, `walking-3`, `blazer-4`, `resting-1`, `pointing_finger-1`, `crossed_arms-2`), 221 (`sitting/mid-1`, `pointing_finger-1`, `resting-1`, `crossed_arms-2`, `blazer-2`, `polka_dots`, `robot_dance-2`) und 222 (`easing-1`, `resting-1`, `robot_dance-2`, `crossed_arms-2`); Köpfe nicht aus 220–222; keine Polka Dots.
- Figuren-PNGs: `../peeps/op_223/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 220 (Klassenzimmer, Schulleitung), 221 (Beweisverwertung), 222 (Assessorklausur). Neu: Tischlerwerkstatt mit Werkbank, Säge, Holz und Werkzeugkiste. **Wiederkehr der Bank:** wie in 099 und 133, weil die Gläubigerin eine Bank ist; anders gebaut (Schreibtisch statt Schalter, neues Personal, gedruckte Urkunde ohne „selbstschuldnerisch“). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Werkstatt** `fall`–`zins` | ab 0,0 s: Werkbank, Gero mit Schild, Pille „Gero ist Tischlermeister“; Bank + „für neue Maschinen“, „Firmenkredit: 200.000 €“, „Zinsen: 1.000 € im Monat“ | fluent-hc:`carpentry-saw`, `wood` (Holz), `toolbox` (Rot); tabler:`building-bank` (Blau); Werkbank als Grundform | `Fall · Die Werkstatt von Gero` | – |
| **A2 Bank** `bank`–`nimmt` | Schreibtisch; Blase Wittkamp „Den Kredit gibt es nur, wenn / Ihre Frau dafür bürgt.“; Anneke kommt, Ring + „seit 8 Jahren verheiratet“, „kein eigenes Einkommen“, „kein Vermögen“; Blase Gero „Anneke, ohne deine Bürgschaft / bekomme ich den Kredit nicht.“; Blase Anneke „Wenn es für die Werkstatt sein / muss, unterschreibe ich.“; Urkunde zeilenweise, Stift bei „eigenhändig“, Unterschrift, „Bank nimmt an“ | tabler:`building-bank`, `ballpen`; fluent-hc:`ring` | `Fall · Bei der Bank` → `Fall · Die Bank will die Bürgschaft von Anneke` → `Fall · Anneke unterschreibt` | `szene_223unterschrift_1` bei der Unterschrift |
| **A3 Drei Jahre später, Frage** `spaet`–`frage2` | Gero besorgt, Kalender, „Raten bleiben aus“, „Bank kündigt“, „offen: 180.000 €“; Wittkamp, Brief, Anneke; Blasen Wittkamp „Sie haben gebürgt. Bitte zahlen / Sie die 180.000 €.“ und Anneke „Davon kann ich nicht einmal / die Zinsen bezahlen.“; Pillen „Muss Anneke zahlen?“, „Oder ist ihre Bürgschaft sittenwidrig und nichtig?“ | tabler:`calendar`, `building-bank`, `mail` | `Fall · Drei Jahre später` → `Fall · Die Frage` | `szene_223brief_1` bei „wendet“ |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ohne Fiktiv-Hinweis, ≈ 9 s | – | `Sachverhalt` | – |
| **C Anspruch** `agl`–`problem` | Wortlautkarte § 765 Abs. 1 (2 Marker), ✓ Einigung, ✓ Form § 766 S. 1 / § 126 Abs. 1, ✓ Hauptschuld, Block „Problem: nichtig nach § 138 Abs. 1 BGB?“ | tabler:`building-bank`, `file-certificate`, `signature`, `scale` | `Anspruch · Bank gegen Anneke, § 765 Abs. 1 BGB` → `I. Entstanden › Bürgschaftsvertrag und Form` → `I. Entstanden › Nichtigkeit, § 138 Abs. 1 BGB?` | – |
| **D1 Bürgschaftsbeschluss** `bverfg`–`fremd` | Block BVerfG mit Datum und Az., Tochter (S. 218), Wortlautkarte Art. 2 Abs. 1 GG (Marker), Privatautonomie (S. 231), Fremdbestimmung (S. 232) | tabler:`building-bank`, `briefcase`, `user-check`, `scale` | `Bürgschaftsbeschluss · BVerfGE 89, 214` → `› Privatautonomie, Art. 2 Abs. 1 GG` | – |
| **D2 Pflicht der Zivilgerichte** `korr`–`vvv` | 1. ungewöhnlich belastend, 2. strukturell ungleiche Verhandlungsstärke, Korrektur (S. 234), Generalklauseln §§ 138, 242 (S. 229 f.), ✗ „Vertrag ist Vertrag“ | tabler:`gavel`, `books`, `file-certificate` | `Bürgschaftsbeschluss › Inhaltskontrolle durch die Zivilgerichte` → `› Generalklauseln, §§ 138, 242 BGB` | – |
| **E1 § 138** `w138`–`nahe` | Wortlautkarte § 138 Abs. 1 (2 Marker), BGH-Kriterien 1. krasse Überforderung (XI ZR 82/11 Rn. 9), 2. besondere Nähe (XI ZR 32/16 Rn. 20) | tabler:`scale`, `coin-euro`, `heart-handshake` | `I. Entstanden › Nichtigkeit, § 138 Abs. 1 BGB` → `› 1. krasse finanzielle Überforderung` → `› 2. besondere persönliche Nähe` | – |
| **E2 Vermutung** `verm`, `widerl` | Vermutung (Rn. 9), Widerlegung durch die Bank, Beweislast (XI ZR 32/16 Rn. 20) | tabler:`heart`, `building-bank` | `§ 138 Abs. 1 BGB › 3. Vermutung` → `› Widerlegung durch die Bank` | – |
| **F Subsumtion** `sub`–`nichts` | 0 € / 1.000 € Zinsen, ✓ krass überfordert, ✓ Ehefrau nahe, ✗ kein eigenes Interesse, mittelbarer Vorteil (Rn. 29 f.), ✗ Vermutung nicht widerlegt | tabler:`wallet`, `coin-euro`; fluent-hc:`ring`, `toolbox` | `§ 138 Abs. 1 BGB › im Fall` → `› im Fall: Nähe und Eigeninteresse` | – |
| **G Ergebnis** `erg`, `erg2` | Bühne: Block „Ergebnis: Bürgschaft sittenwidrig, nach § 138 Abs. 1 BGB nichtig“, Urkunde ungültig, „Anneke muss nichts zahlen“ | tabler:`building-bank`, `file-off` | `Ergebnis · Bürgschaft nichtig, § 138 Abs. 1 BGB` | – |
| **H Gegenfall** `gegen`, `bf2` | eigenes Interesse, Hälfte des finanzierten Objekts, ✓ Vermutung widerlegt (Rn. 29 f.); Block 2. Beschwerdeführerin, ✗ Verfassungsbeschwerde ohne Erfolg (S. 235 f.) | tabler:`home`, `shopping-cart` | `Gegenfall · eigenes Interesse am Kredit` → `› Bürgschaftsbeschluss, zweite Beschwerde` | – |
| **I Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; XI ZR 82/11 Rn. 9 | Warnsymbol (Streamline Freehand) | `Klausurtipp · § 138 BGB beim Entstehen prüfen` | – |
| **J Klausurschema** `sch`–`k3` | breite Karte, I. 1., 2. a)–c), 3., II., III. Zeile für Zeile | – | `Klausurschema` → `› I. 2. keine Nichtigkeit, § 138 Abs. 1 BGB` → `› II. nicht erloschen` → `› III. durchsetzbar` | – |
| **K Merksatz** `merke`–`m3` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil E per Assertion verboten), wortgleich mit dem Gesprochenen, Beträge als Ziffern („180.000 €“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Tischlermeister Gero braucht für neue Maschinen seiner Werkstatt einen Firmenkredit über 200.000 Euro; die Zinsen betragen 1.000 Euro im Monat. Herr Wittkamp von der Bank verlangt, dass seine Ehefrau Anneke bürgt.
>
> Anneke ist seit acht Jahren mit Gero verheiratet. Sie hat kein eigenes Einkommen und kein Vermögen; daran wird sich absehbar nichts ändern. Die Werkstatt gehört Gero allein. Anneke unterschreibt eigenhändig die Urkunde: „Ich bürge für den Firmenkredit von Gero über 200.000 Euro.“ Herr Wittkamp nimmt die Erklärung an.
>
> Drei Jahre später bleiben die Aufträge aus. Die Bank kündigt den Kredit wirksam, 180.000 Euro sind offen. Sie verlangt das Geld von Anneke. Umstände, die eine Ausnutzung durch die Bank ausschließen, sind nicht ersichtlich.
>
> **Muss Anneke zahlen?**
