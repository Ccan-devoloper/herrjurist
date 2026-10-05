# Redaktionsregeln Instagram · Herrjurist (verbindlich, Stand 04.10.2026)

Open-Peeps-Stil (Variante C) wie beim Schwesterkanal Examenscampus, mit den Besonderheiten des juristischen
Staatsexamens. Tagesbeschreibungen in `op/tage/<datum>.json` (Format: [SPEC.md](SPEC.md)); gerendert wird mit
`python3 op/tag.py <datum> --ziel <instagram-assets-Checkout>`. `bin/op-pruefen.mjs` prüft jeden Tag mit
`pruefeBeitrag` (keine Übernahmen aus dem Themenpool, keine gesperrten Namen); ein Befund verhindert das Ablegen.

## Farben (sichtbare Kategorie = Rahmenfarbe)
Zivilrecht **blau** (`klausur: 1`), Strafrecht **orange** (`2`), Öffentliches Recht **grün** (`3`), alles Sonstige
**lila**: Klausurmethodik/Kopfsache (`0`) und Wochenrückblick (`4`, `fach: "wochenrueckblick"`). Fachgebundene
Klausurtechnik bleibt in der Farbe ihres Rechtsgebiets. Kleidung der Figuren nie in der Rahmenfarbe.

## Fachliche Genauigkeit
1. Jede Norm, Fundstelle und Zahl wird vor der Produktion geprüft (gesetze-im-internet.de, eur-lex, amtliche
   Entscheidungssammlungen, Rechtsprechungsdatenbanken des Bundes). Was nicht belegt ist, wird gestrichen.
2. Zitierweise: Abs., S., Nr., Alt., Var.; die Kurzform „§ 6 (1) S. 1 Nr. 2“ ist zulässig. Nie „3.“ allein,
   immer „Nr. 3“. GG und EU-Recht mit Art. Entscheidungen mit amtlicher Fundstelle (BGHSt 30, 105; BVerfGE 124, 300;
   EuGH, Rs. 120/78) oder Gericht, Datum, Az.
3. Klausurkonvention: Gutachtenstil im ersten, Praxisaufbau (Anklage, Relation, Urteil, Bescheid) im zweiten
   Examen. Streitstände mit Rechtsprechung und Gegenansicht; die Klausurempfehlung folgt im Zweifel der
   Rechtsprechung, die Gegenansicht wird genannt, wo sie klausurrelevant ist. Landesrecht nur mit Hinweis
   „Landesrecht prüfen“, sofern nicht das Bundesrecht entscheidet.
4. Fälle sind frei erfunden (kurze Namen wie A, B, O oder Vornamen), keine echten Personen, keine Fallnamen aus
   Lehrbüchern.

## Titel und Hooks (aus der Reichweite der Beiträge seit 13.09.)
1. Leicht zugespitzt, nie leer: Der Titel nennt den Rechtsinhalt und baut eine konkrete Wendung oder einen
   konkreten Fehler ein. Muster, die getragen haben: „Gutgläubig gekauft – und trotzdem nicht Eigentümer“,
   „Sie unterschreibt – trotzdem unverwertbar“, „Vormerkung = Eigentum? Genau dieser Schluss ist falsch“,
   „Der Fehler, der dich in jeder GbR-Klausur verrät“. Reels mit Wendung oder Fehler im Titel erreichten im
   Median rund 50 % mehr Konten als Reels ohne (575 zu 378).
2. Kein Rätsel ohne Inhalt: Hooks wie „Rex unterschreibt allein“, „Die Werkstatt ist gesperrt“, „Und jetzt? Keine
   Ahnung.“ lagen am Ende der Reichweite. Wer nur den Titel liest, muss wissen, um welche Rechtsfrage es geht.
3. Nicht übertreiben: keine falschen Versprechen („100 % bestehen“), keine Großbuchstaben-Schreie, höchstens ein
   „falsch“/„nicht“ je Titel, die Aussage muss fachlich stimmen.

## Karussell (1080×1350)
1. 6–9 Folien (höchstens 10, Grenze der Instagram-API), ≤ 40 Wörter je Folie, ein Gedanke je Folie.
2. Cover: Schlagzeile ≤ 6 Wörter nach den Titelregeln oben; Badge = Format (Prüfungsfrage, Klausurschema,
   Mini-Fall, Spickzettel, Streitstand, Vergleich, Klausurtechnik, Wochenrückblick); Norm als N3-Zeile, wenn sie
   nicht in der Schlagzeile steht; `unter` kurz (die Teaser-Pille daneben muss passen).
3. **Das Titelbild trägt den Inhalt.** Das Motiv zeigt den Gegenstand, die Zahl oder die Frist des Falls: ein Icon
   des Tatobjekts oder Streitgegenstands (Auto, Schlüssel, Messer, Haus, Vertrag, Handy …), ein Kalenderblatt mit
   der entscheidenden Frist, ein Zahlblock mit der Schlüsselzahl oder den zwei Begriffen der Abgrenzung. Kein
   beliebiges Symbol (Liste, Glühbirne, Buch, Waage für alles). Die Figur reagiert passend zur Frage.
4. Aufbau nach Format: Fall bzw. Frage → „Jetzt du“ → Lösung; typischer Fehler als Klausurfalle; Schritte bzw.
   Prüfschema; Merke-Folie (Lösung oben, Markertext); **letzte Folie = Baustein für die Klausur** („So im Gutachten“,
   „So in der Anklage“, „So im Urteil“, „So im Bescheid“) als `schritte`-Folie: Obersatz, Definition bzw. Norm,
   Subsumtion, Ergebnis. Angeteasert auf dem Cover („+ Gutachten-Baustein“), auf der Schritte-Folie und auf der
   Merke-Folie. Keine Gesetzesmarkierungen (das gibt es nur beim Examenscampus).
5. Normen auf Folgefolien grau direkt unter der Aussage. Keine Fläche leer, nichts überladen; Figuren mit Funktion
   (Sprechblase mit Reaktion auf den Inhalt), die Merke-Folie kommt ohne Figur aus.
6. Wochenrückblick (`klausur: 4`, lila): je Rechtsgebiet eine Folie mit den Kernsätzen der Woche, dann
   Klausurtechnik & Kopfsache, Selbsttest (merke) und Wiederholungsplan.

## Reel (1080×1920, etwa 30 s)
1. **Der erste Satz macht den Inhalt verständlich**: Er nennt die Rechtsfrage und die Wendung („Gutgläubig gekauft
   und trotzdem nicht Eigentümer? Bei gestohlenen Sachen ja.“). Kein Einstieg mit Namen oder Szene ohne Rechtsfrage.
2. Länge etwa 30 s: Sprechertext gesamt 330–380 Zeichen (der Prüflauf schätzt ≤ 33 s, sonst Abbruch). Aufbau:
   Hook, zwei bis drei Szenen, Merke.
3. Layout **D** (`"layout": "D"`): Unter den Szenen läuft das Prüfschema mit (die Szenentitel, höchstens vier,
   je ≤ 32 Zeichen). Hook-Stile wechseln (kippen mit Irrtum/Richtig und „Falsch!“-Stempel, split, knall).
4. Je Szene ein bis drei Elemente, höchstens eine Norm als ruhige lila Zeile; alle Fundstellen in der Caption.
5. Sprechertext so geschrieben, wie er gesprochen wird: keine §-Zeichen, Ziffern, „Abs.“, „Nr.“ oder Kürzel
   („Bundesgerichtshof“ statt BGH, „Paragraf zweihundertelf“). Der Renderer bricht sonst ab.
6. Eigenes Reel-Cover mit Fach-Pille und Hook (wird automatisch aus dem Hook gebaut).

## Story (1080×1920)
Inhalt zwischen y 260 und 1660, ≤ 25 Wörter, ein Gedanke. Arten wie im Tagesplan: frage/antwort (Quizpaar,
dieselbe Figur), teaser (echtes Cover), norm, tipp, merksatz, fehler, streitstand, begriff, zahl.
Bei `zahl` ist die Zahl eine echte, tragende Ziffernangabe (max. 8 Zeichen), keine Paragrafennummer.

## Plan
Slots, Zeiten, Formate, Fächer und Themen kommen aus der bisherigen Vorproduktion (`vorproduktion/<datum>.json`
bzw. der Fassung im Asset-Zweig mit den Dashboard-Änderungen) und bleiben unverändert. Gerendert wird 14 Tage
im Voraus (Workflow „Vorproduktion · Open Peeps“).
