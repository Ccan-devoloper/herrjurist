"""Folge 283 · § 80a VwGO: Der Bagger rollt – Eilrechtsschutz des Nachbarn (Mo · Der Fall · Baurecht · Schema).
Übungsfall nach dem Plan-Hook („Am Tag nach der Genehmigung beginnen nebenan die Bauarbeiten – dein Widerspruch stoppt
nichts“): Frau Fehling wohnt in einem Haus mit Garten. Ihr Nachbar Herr Brodbeck erhält die Baugenehmigung für ein
Mehrfamilienhaus mit 3 Geschossen und 6 Wohnungen; kaum ist sie da, rollt der Bagger. Frau Fehling rügt, das Haus nehme
ihrem Garten die Abendsonne (Rücksichtnahmegebot), und legt fristgerecht Widerspruch ein (je nach Land; sonst Klage). Das
Haus hält die Abstandsflächen der Landesbauordnung ein. Ergebnis: Antrag zulässig, aber unbegründet; Herr Brodbeck baut auf
eigenes Risiko. Gegenfall (ein Satz): verletzte Abstandsflächen → Anordnung trotz § 212a.
Aufbau (Plan): 1. Warum stoppt der Widerspruch nichts? § 212a Abs. 1 BauGB (Wortlautkarte) i. V. m. § 80 Abs. 2 S. 1 Nr. 3
VwGO (Wortlautkarte) → 2. Statthaftigkeit: § 80a Abs. 3 (Wortlautkarte) i. V. m. § 80 Abs. 5 S. 1 (Wortlautkarte),
Abgrenzung § 123 Abs. 5 (ein Satz, Verweis Folge 254), behördlicher Antrag § 80a Abs. 1 Nr. 2 (ein Satz, Wortlautkarte
§ 80a Abs. 1) → 3. Zulässigkeit: Rechtsweg, Antragsbefugnis analog § 42 Abs. 2 (Verweis Folge 113), Rechtsbehelf eingelegt
(OVG NRW 8 B 1108/15 Rn. 15; 7 B 334/26 Rn. 3–5), § 80 Abs. 5 S. 2 → 4. Begründetheit: Interessenabwägung (BVerwG 7 VR 7.19
Rn. 8), Wertung des § 212a (OVG NRW 7 B 359/25 Rn. 12; 10 B 645/23 Rn. 90), Rücksichtnahme und Abstandsflächen (BVerwG 4 B
52.15 Rn. 9), Ergebnis, eigenes Risiko (10 B 645/23 Rn. 90), Gegenfall (10 B 603/20 Rn. 16) → 5. Umgekehrt: § 80a Abs. 1
Nr. 1 (ein Satz) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Grundschema § 80 V (Folge 082) nur vorausgesetzt.
Darstellung: Bauherr und Nachbarin fair (beide sachlich, beide mit nachvollziehbarem Anliegen), Bagger als Symbol.
Namen eindeutig deutsch, nicht vergeben (Koordinatorliste, namen_reserviert.txt, Volltextsuche 08.10.2026): Brodbeck,
Fehling (nie im Genitiv mit -s). Stimmen aus dem Pool (william, sabrina, marc, laura_ruhig): Herr Brodbeck william (Mann,
älter), Frau Fehling laura_ruhig (Frau, mittel); marc und sabrina nicht verwendet (Folgen 277 und 280). Lexi = Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Brodbeck": "william", "Fehling": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Haus mit Garten, Baugenehmigung nebenan, Bagger, Widerspruch ------------------------------------------------
    ("[fall]Frau Fehling wohnt in einem Haus mit Garten. [gen]Ihr Nachbar, Herr Brodbeck, bekommt die Baugenehmigung für "
     "ein Mehrfamilienhaus mit drei Geschossen und sechs Wohnungen. [bagger]Kaum ist die Genehmigung da, rollt auf seinem "
     "Grundstück der Bagger.", P),
    ("[fe1]Das Haus nimmt meinem Garten die Abendsonne. Dagegen wehre ich mich.", P, "Fehling"),
    ("[br1]Ich habe alles genehmigen lassen. Und die Wohnungen werden gebraucht.", P, "Brodbeck"),
    ("[wid]Frau Fehling legt fristgerecht Widerspruch ein. Je nach Land gibt es dieses Vorverfahren, sonst erhebt man "
     "gleich Klage. [weiter]Doch der Bagger gräbt weiter. [frage]Warum stoppt ihr Widerspruch nichts? [frage2]Und wie "
     "kommt sie schnell zu einem Baustopp?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Warum stoppt der Widerspruch nichts? § 212a Abs. 1 BauGB, § 80 Abs. 2 S. 1 Nr. 3 VwGO ---------------------------
    ("[grund]Erstens: Warum stoppt der Widerspruch nichts? Normalerweise haben Widerspruch und Anfechtungsklage "
     "aufschiebende Wirkung, Paragraf achtzig Absatz eins. [w212]Doch Paragraf zweihundertzwölf a Absatz eins "
     "Baugesetzbuch sagt: Widerspruch und Anfechtungsklage eines Dritten gegen die bauaufsichtliche Zulassung eines "
     "Vorhabens haben keine aufschiebende Wirkung. [w802]Das ist ein Fall von Paragraf achtzig Absatz zwei Satz eins "
     "Nummer drei: Die aufschiebende Wirkung entfällt, wo ein Bundesgesetz das vorschreibt. [darf]Herr Brodbeck darf "
     "deshalb vorerst bauen.", PS),
    # --- D 2. Statthaftigkeit: § 80a Abs. 3 VwGO, § 80 Abs. 5 S. 1 VwGO, § 123 Abs. 5, § 80a Abs. 1 Nr. 2 --------------------
    ("[statt]Zweitens, die Statthaftigkeit. [va]Die Baugenehmigung begünstigt Herrn Brodbeck und belastet Frau Fehling. "
     "Für solche Fälle gibt es Paragraf achtzig a. [w80a]Sein Absatz drei: Das Gericht kann auf Antrag Maßnahmen nach den "
     "Absätzen eins und zwei ändern oder aufheben oder solche Maßnahmen treffen. Paragraf achtzig Absatz fünf bis acht "
     "gilt entsprechend.", P),
    ("[w805]Nach Paragraf achtzig Absatz fünf ordnet das Gericht die aufschiebende Wirkung in den Fällen der Nummern eins "
     "bis drei a an. Bei Nummer vier stellt es sie wieder her. [anord]Hier geht es um Anordnung: Die Wirkung entfällt "
     "kraft Gesetzes, nicht durch eine Anordnung der Behörde. [p123]Die einstweilige Anordnung nach Paragraf "
     "hundertdreiundzwanzig tritt nach dessen Absatz fünf zurück. Mehr dazu im Video zur einstweiligen Anordnung. "
     "[beh]Frau Fehling könnte auch zuerst die Behörde bitten, die Vollziehung auszusetzen, Paragraf achtzig a Absatz eins "
     "Nummer zwei. Nach dem Wortlaut muss sie das aber nicht.", PS),
    # --- E 3. Zulässigkeit: Rechtsweg, Antragsbefugnis, Rechtsbehelf eingelegt ------------------------------------------------
    ("[zul]Drittens, die übrige Zulässigkeit. [weg]Der Verwaltungsrechtsweg ist offen. "
     "[befugt]Antragsbefugt ist Frau Fehling analog Paragraf zweiundvierzig Absatz zwei nur, wenn sie die Verletzung einer "
     "Norm geltend macht, die auch sie schützt. [rueck]Sie beruft sich auf das Gebot der Rücksichtnahme. Das schützt "
     "auch die Nachbarn, eine Verletzung ist möglich. [v113]Welche Normen Nachbarn schützen, zeigt unser Video zur "
     "Nachbarklage.", P),
    ("[rbh]Außerdem muss ein Rechtsbehelf eingelegt sein. Sonst gibt es keine aufschiebende Wirkung, die das Gericht "
     "anordnen könnte. [frist]Fehlt er und ist die Frist verstrichen, scheitert der Eilantrag, so das "
     "Oberverwaltungsgericht Nordrhein-Westfalen. [vor]Frau Fehling hat Widerspruch eingelegt. Entschieden sein muss "
     "über ihn noch nicht: Der Antrag ist schon vor der Klage zulässig.", PS),
    # --- F 4. Begründetheit: Interessenabwägung, Wertung des § 212a -----------------------------------------------------------
    ("[begr]Viertens, die Begründetheit. [abw]Das Gericht wägt selbst ab: das Interesse von Frau Fehling, dass die "
     "Arbeiten ruhen, gegen das Interesse von Herrn Brodbeck, zu bauen. [eaus]Wesentlich sind die Erfolgsaussichten in der "
     "Hauptsache, geprüft nur summarisch. [folg]Lassen sie sich nicht beurteilen, entscheidet eine Abwägung der Folgen. "
     "[wert]Dabei zählt die Wertung des Paragrafen zweihundertzwölf a: Die Genehmigung soll während des Prozesses "
     "vollziehbar sein.", P),
    # --- G Subsumtion: Rücksichtnahme, Abstandsflächen, Ergebnis, eigenes Risiko, Gegenfall ------------------------------------
    ("[nur]Es kommt also darauf an, ob die Genehmigung voraussichtlich eine Norm verletzt, die auch Frau Fehling schützt. "
     "[abst]Das Haus hält die Abstandsflächen der Landesbauordnung ein. [sonne]Für Sonne und Einblick konkretisieren sie "
     "die Rücksichtnahme. Mehr kann Frau Fehling insoweit grundsätzlich nicht verlangen, so das "
     "Bundesverwaltungsgericht. [nicht]Die Genehmigung verletzt sie also voraussichtlich nicht in ihren Rechten. "
     "[vollz]Dann überwiegt mit der Wertung des Paragrafen zweihundertzwölf a das Interesse des Bauherrn. [abgel]Das "
     "Gericht lehnt den Antrag ab.", P),
    ("[fe2]Dann warte ich auf das Hauptverfahren.", P, "Fehling"),
    ("[br2]Und ich baue genau so, wie es genehmigt ist.", P, "Brodbeck"),
    ("[risiko]Herr Brodbeck baut allerdings auf eigenes Risiko, bis die Hauptsache entschieden ist. [gegen]Anders wäre es, "
     "wenn das Haus voraussichtlich die Abstandsflächen zu ihrem Grundstück verletzte: Dann überwiegt trotz Paragraf "
     "zweihundertzwölf a ihr Interesse, und das Gericht ordnet die aufschiebende Wirkung an.", PS),
    # --- H 5. Umgekehrt: § 80a Abs. 1 Nr. 1 -----------------------------------------------------------------------------------
    ("[umg]Fünftens, der umgekehrte Fall. Hat der Rechtsbehelf eines Dritten aufschiebende Wirkung, weil kein Gesetz wie "
     "Paragraf zweihundertzwölf a sie ausschließt, kann der Begünstigte bei der Behörde die sofortige Vollziehung "
     "beantragen, Paragraf achtzig a Absatz eins Nummer eins. [umg2]Beim Gericht geht das über Absatz drei.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Benenne zuerst, warum die aufschiebende Wirkung fehlt. [k1]Bei der Baugenehmigung ist das "
     "Paragraf zweihundertzwölf a. [k2]Deshalb beantragst du die Anordnung, nicht die Wiederherstellung. [k3]Und in der "
     "Begründetheit prüfst du nur Normen, die auch den Nachbarn schützen. Dass die Genehmigung irgendwie rechtswidrig "
     "ist, genügt nicht.", PS),
    # --- J Schema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zum Eilantrag des Nachbarn. [s1]A, die Zulässigkeit. [s1a]Eins, der Verwaltungsrechtsweg. "
     "[s1b]Zwei, die Statthaftigkeit: Antrag nach Paragraf achtzig a Absatz drei in Verbindung mit Paragraf achtzig Absatz "
     "fünf auf Anordnung. [s1c]Drei, die Antragsbefugnis analog Paragraf zweiundvierzig Absatz zwei. [s1d]Vier, ein "
     "eingelegter Rechtsbehelf. [s2]B, die Begründetheit: die Interessenabwägung. [s2a]Vor allem die Erfolgsaussichten, "
     "gemessen an Normen, die auch den Nachbarn schützen. [s2b]Dazu die Wertung des Paragrafen zweihundertzwölf a.", PS),
    # --- K Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gegen die Baugenehmigung des Nachbarn stoppen Widerspruch und Klage nichts. [m2]Verletzt die "
     "Genehmigung voraussichtlich eine Norm, die auch den Nachbarn schützt, ordnet das Gericht die aufschiebende Wirkung "
     "in der Regel an. [m3]Sonst setzt sich meist die Wertung des Gesetzes durch: Es wird gebaut.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
