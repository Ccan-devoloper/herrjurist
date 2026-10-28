"""Folge 113 · Baurechtliche Nachbarklage: Welche Vorschriften schützen dich? (Mi · Examenswissen · Schema · Baurecht).
Übungsfall nach dem Hook des Themenplans („Dein Nachbar bekommt eine Genehmigung für einen großen Anbau – du hältst ihn für
baurechtswidrig“), Beispielland Nordrhein-Westfalen (Abstandsflächen § 6 BauO NRW 2018, Fassung ab 01.09.2026):
Frau Mahnke und Herr Pütz wohnen nebeneinander in einem allgemeinen Wohngebiet mit Bebauungsplan (Geschossflächenzahl 0,4)
und Gestaltungssatzung (Satteldach). Herr Pütz erhält im vereinfachten Verfahren die Baugenehmigung für einen
zweigeschossigen Anbau mit Flachdach: Wand 6 m hoch, nur 1,50 m vor der Grenze, Geschossflächenzahl danach 0,55; keine
Befreiung, keine Abweichung, keine Baulast. Frau Mahnke rügt drei Verstöße und klagt.
Schema: 1. Zulässigkeit kurz (Anfechtungsklage, Klagebefugnis über die Abstandsflächen, Verweis 105/110, NRW ohne
Vorverfahren § 110 I 1, III 2 Nr. 8 JustG NRW); 2. Begründetheit § 113 I 1 VwGO (Wortlautkarte): rechtswidrig UND dadurch
in eigenen Rechten verletzt (OVG NRW 7 A 75/23 Rn. 32); 3. Ampel-Tabelle: Abstandsflächen (OVG NRW 7 A 1367/22 Rn. 53, 80;
BVerwG 4 B 52.15 Rn. 9), Gebietserhaltungsanspruch (BVerwG 4 C 6.20 Rn. 8), Rücksichtnahmegebot (ein Satz, Verweis 088);
nicht: Maß (BVerwG 4 C 7.17 Rn. 14, 21; OVG NRW 10 B 645/23 Rn. 42–48), Gestaltung (OVG NRW 7 A 75/23 Rn. 41; § 89 I Nr. 1
BauO NRW); 4. die drei Rügen am Fall (§ 30 I, § 31 II BauGB; Wortlautkarte § 6 II 1, IV 1, V 1 BauO NRW; 7 A 1367/22
Rn. 48, 53, 57); Ergebnis: begründet nur wegen der Abstandsfläche; Eilrechtsschutz nur Verweis (090).
Fiktive Figuren: Frau Mahnke (sabrina), Herr Pütz (marc). Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Mahnke": "sabrina", "Pütz": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: zwei Häuser, Bebauungsplan, Anbau, Baugenehmigung -------------------------------------------------------
    ("[fall]Frau Mahnke wohnt in einem Einfamilienhaus in einem Wohngebiet in Nordrhein-Westfalen. [plan]Der Bebauungsplan "
     "setzt dort eine Geschossflächenzahl von null Komma vier fest, eine Gestaltungssatzung schreibt Satteldächer vor. "
     "[puetz]Ihr Nachbar, Herr Pütz, will sein Haus vergrößern.", 0.2),
    ("[pu1]Ich baue an: zwei Geschosse mit Flachdach, bis kurz vor die Grenze.", 0.3, "Pütz"),
    ("[genehm]Die Bauaufsichtsbehörde erteilt ihm die Baugenehmigung. [anbau]Die Wand des Anbaus wird sechs Meter hoch "
     "und steht nur eineinhalb Meter vor der Grenze zu Frau Mahnke. [gfz]Die Geschossflächenzahl steigt auf null Komma "
     "fünf fünf.", 0.2),
    ("[ma1]Viel zu groß, ein Flachdach, und dann noch direkt an meiner Grenze! Dagegen klage ich.", 0.3, "Mahnke"),
    ("[frage]Drei Verstöße hat Frau Mahnke gefunden. [frage2]Aber mit welchem davon gewinnt sie ihre Klage?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Zulässigkeit kurz -------------------------------------------------------------------------------------------
    ("[zul]Erstens, kurz zur Zulässigkeit. Frau Mahnke erhebt Anfechtungsklage gegen die Genehmigung ihres Nachbarn, in "
     "Nordrhein-Westfalen ohne Widerspruchsverfahren. [kb]Klagebefugt ist sie, weil sie die Verletzung einer Norm geltend "
     "macht, die auch sie schützt: der Abstandsflächen. [v110]Wie du das prüfst, zeigen unsere Videos zur Klagebefugnis "
     "und zur Schutznormtheorie.", P),
    # --- D 2. Begründetheit, Wortlautkarte § 113 I 1 VwGO -------------------------------------------------------------------
    ("[p113]Zweitens, die Begründetheit. Paragraf hundertdreizehn Absatz eins Satz eins: Soweit der Verwaltungsakt "
     "rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht den Verwaltungsakt auf. "
     "[zwei]Du brauchst also beides: Die Genehmigung ist rechtswidrig, und sie verletzt gerade die Klägerin. "
     "[faden]Objektive Rechtswidrigkeit ist nicht gleich Rechtsverletzung. Ein Verstoß hilft dem Nachbarn nur, wenn die "
     "verletzte Norm auch ihn schützt.", P),
    # --- E 3. Ampel-Tabelle: Welche Bauvorschriften schützen dich? ----------------------------------------------------------
    ("[tab]Drittens: Welche Bauvorschriften schützen dich? [t1]Die Abstandsflächen der Landesbauordnung. Sie sichern "
     "Licht, Luft und Sozialabstand, auch für den Nachbarn. [t2]Die Art der baulichen Nutzung. Über den "
     "Gebietserhaltungsanspruch kann jeder Eigentümer im Baugebiet eine gebietsfremde Nutzung abwehren, auch ohne "
     "konkrete Beeinträchtigung. [t3]Und das Gebot der Rücksichtnahme aus Paragraf fünfzehn der Baunutzungsverordnung, "
     "aus dem Einfügen nach Paragraf vierunddreißig und aus Paragraf fünfunddreißig Absatz drei. Es schützt nur vor "
     "Unzumutbarem; dazu gibt es ein eigenes Video.", P),
    ("[t4]Das Maß der baulichen Nutzung schützt dich dagegen in der Regel nicht, sondern nur, wenn die Gemeinde als "
     "Plangeber das will. [t5]Ebenso wenig schützen dich in der Regel Gestaltungsvorschriften. Sie dienen dem Ortsbild.", P),
    # --- F 4. Die drei Rügen: Geschossflächenzahl, Flachdach ------------------------------------------------------------------
    ("[r1]Jetzt die drei Rügen am Fall. Erstens die Geschossflächenzahl. [r1a]Der Anbau widerspricht der Festsetzung im "
     "Bebauungsplan. Nach Paragraf dreißig Absatz eins des Baugesetzbuchs ist die Genehmigung insoweit objektiv "
     "rechtswidrig. [r1b]Für einen Schutzwillen der Gemeinde gibt der Plan aber nichts her. Frau Mahnke ist dadurch nicht "
     "in ihren Rechten verletzt. [befr]Hätte die Behörde befreit, könnte sie nach Paragraf einunddreißig Absatz zwei nur "
     "rügen, dass ihre nachbarlichen Interessen nicht gewürdigt wurden.", P),
    ("[r2]Zweitens das Flachdach. Es verstößt gegen die Gestaltungssatzung, [r2a]doch diese Vorschrift schützt das "
     "Ortsbild, nicht Frau Mahnke.", P),
    # --- G Rüge 3: Abstandsfläche, Wortlautkarte § 6 BauO NRW ---------------------------------------------------------------
    ("[r3]Drittens die Abstandsfläche. [wl6]Nach Paragraf sechs der Landesbauordnung Nordrhein-Westfalen müssen "
     "Abstandsflächen auf dem Grundstück selbst liegen. Ihre Tiefe bemisst sich nach der Wandhöhe H und beträgt null "
     "Komma vier H, mindestens drei Meter. [rech]Die Wand ist sechs Meter hoch. Null Komma vier mal sechs ergibt zwei "
     "Komma vier Meter, also gilt das Mindestmaß von drei Metern.", P),
    ("[luecke]Der Anbau steht aber nur eineinhalb Meter vor der Grenze. Eineinhalb Meter seiner Abstandsfläche liegen "
     "auf dem Grundstück von Frau Mahnke. [abw]Eine Abweichung hat die Behörde nicht zugelassen. [verl]Weil die Norm auch "
     "Frau Mahnke schützt, verletzt die Genehmigung sie in ihren Rechten. Eine konkrete Beeinträchtigung muss sie nicht "
     "nachweisen. [land]In deinem Land kann die Regel anders lauten, das Prinzip bleibt gleich.", P),
    # --- H Ergebnis -----------------------------------------------------------------------------------------------------------
    ("[erg]Das Ergebnis: Die Klage ist begründet, aber nur wegen der Abstandsfläche. Das Gericht hebt die Baugenehmigung "
     "auf. [eil]Weil ihre Klage den Bau nicht aufhält, braucht Frau Mahnke zusätzlich Eilrechtsschutz. Dazu gibt es unser "
     "Video zur Drittanfechtung.", 0.3),
    ("[pu2]Dann plane ich den Anbau eben neu, mit drei Metern Abstand.", PS, "Pütz"),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe in der Begründetheit nicht alle Fehler der Genehmigung der Reihe nach durch. [tipp1]Frag "
     "bei jedem Verstoß sofort: Schützt die verletzte Norm auch den Kläger? [tipp2]Und prüfe, ob sie zum Prüfprogramm "
     "der Genehmigung gehört. In Nordrhein-Westfalen gehören die Abstandsflächen dazu.", PS),
    # --- J Schema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zur baurechtlichen Nachbarklage. [s1]Eins, Zulässigkeit: [s1a]Anfechtungsklage, [s1b]Klagebefugnis "
     "über eine drittschützende Norm, die verletzt sein kann. [s2]Zwei, Begründetheit nach Paragraf hundertdreizehn "
     "Absatz eins Satz eins: [s2a]Die Genehmigung ist rechtswidrig, [s2b]und zwar wegen eines Verstoßes gegen eine "
     "drittschützende Norm: [s2c]Abstandsflächen, Gebietserhaltung oder Rücksichtnahme, nicht aber Maß oder Gestaltung. "
     "[s3]Drei, die Klägerin ist dadurch in ihren Rechten verletzt.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nicht jeder Baurechtsverstoß deines Nachbarn verletzt dein Recht. [m2]Du gewinnst nur mit einer Norm, "
     "die auch dich schützt, etwa mit der Abstandsfläche.", 1.4),
]
