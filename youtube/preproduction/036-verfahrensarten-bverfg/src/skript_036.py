"""Folge 036 · Verfahrensarten BVerfG: Welches Verfahren wann? Der Überblick (Fr · Klausurpraxis · Verfassungsprozessrecht).
Beispielfall (Übungsfall): Ein Bundesgesetz verbietet privates Silvesterfeuerwerk (Verkauf und Abbrennen, bußgeldbewehrt).
Daraus fünf Wege nach Karlsruhe: Verfassungsbeschwerde (Ladeninhaberin Frau Pfeiffer), Organstreit (Fraktionschef Pohl gegen
die Bundesregierung, Frage- und Informationsrecht), abstrakte Normenkontrolle (Landesregierung Süd, Ministerpräsidentin
Hagedorn), konkrete Normenkontrolle (Amtsrichter Glaser im Bußgeldverfahren, Art. 100 I GG) und Bund-Länder-Streit
(Bundesregierung gegen Land Süd, das das Gesetz nicht ausführt). Entscheidungsfrage „Wer will was gegen wen?“ als
Klausurkonvention. Zuständigkeiten nach Art. 94 GG n. F. (seit 28.12.2024, BGBl. 2024 I Nr. 439), §§ 13 ff. BVerfGG.
Wortlautkarten: Art. 94 I Nr. 4a, 1, 2, 3 GG (Merkmale), Art. 100 I GG (vorgelesen mit Auslassung).
Fiktive Figuren: Frau Pfeiffer (sabrina), Fraktionschef Pohl (niklas), Ministerpräsidentin Hagedorn (laura_ruhig),
Richter Glaser (helmut). Keine realen Politiker oder Parteien.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Pfeiffer": "sabrina", "Pohl": "niklas", "Hagedorn": "laura_ruhig", "Glaser": "helmut"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: das Gesetz -------------------------------------------------------------------------------------------
    ("[fall]Der Bundestag beschließt ein neues Gesetz. [verbot]Privates Silvesterfeuerwerk ist ab sofort verboten, Verkauf "
     "und Abbrennen. [bussgeld]Wer dagegen verstößt, zahlt ein Bußgeld. [viele]Gleich mehrere wollen nach Karlsruhe.", 0.3),
    # --- B Frau Pfeiffer --------------------------------------------------------------------------------------------------
    ("[pfeiffer]Frau Pfeiffer verkauft in ihrem Laden seit Jahren Feuerwerk.", 0.2),
    ("[pf1]Das Gesetz nimmt mir mein Geschäft. Dagegen wehre ich mich in Karlsruhe.", 0.3, "Pfeiffer"),
    # --- C Fraktionschef Pohl ---------------------------------------------------------------------------------------------
    ("[pohl]Im Bundestag fragt die Fraktion von Herrn Pohl, auf welches Gutachten sich das Verbot stützt. [schweigt]Die "
     "Bundesregierung verweigert die Antwort.", 0.2),
    ("[po1]Die Regierung muss uns Auskunft geben. Das klären wir in Karlsruhe.", 0.3, "Pohl"),
    # --- D Ministerpräsidentin Hagedorn -----------------------------------------------------------------------------------
    ("[hagedorn]Ministerpräsidentin Hagedorn regiert das Land Süd.", 0.2),
    ("[ha1]Dieses Gesetz ist verfassungswidrig. Wir lassen es in Karlsruhe prüfen.", 0.3, "Hagedorn"),
    # --- E Richter Glaser -------------------------------------------------------------------------------------------------
    ("[kunde]Ein Kunde zündet trotzdem Raketen. Er soll ein Bußgeld zahlen und legt Einspruch ein. [glaser]Am Amtsgericht "
     "entscheidet Richter Glaser.", 0.2),
    ("[gl1]Ich halte das Gesetz für verfassungswidrig. Deshalb lege ich es dem Bundesverfassungsgericht vor.", 0.3, "Glaser"),
    # --- F Die Frage --------------------------------------------------------------------------------------------------------
    ("[frage]Bürgerin, Fraktion, Landesregierung, Amtsgericht: Welches Verfahren passt wann? [regel]Die Klausurfrage lautet "
     "immer: Wer will was gegen wen?", 0.6),
    # --- G Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- H Zuständigkeit: Art. 94 GG n. F. -----------------------------------------------------------------------------------
    ("[art94]Die Zuständigkeiten des Bundesverfassungsgerichts stehen seit dem achtundzwanzigsten Dezember "
     "zweitausendvierundzwanzig in Artikel vierundneunzig Grundgesetz. [art93]Vorher standen sie in Artikel dreiundneunzig. "
     "Der regelt heute Stellung und Organisation des Gerichts. [p13]Das Verfahren regelt das "
     "Bundesverfassungsgerichtsgesetz, den Katalog Paragraf dreizehn.", PS),
    # --- I Verfassungsbeschwerde ----------------------------------------------------------------------------------------------
    ("[vb]Erstens: Frau Pfeiffer. Wer? Jedermann. Was? Die Verletzung eigener Grundrechte, hier der Berufsfreiheit. "
     "[vbgegen]Gegen wen? Gegen die öffentliche Gewalt, hier das Gesetz. [wl4a]Das ist die Verfassungsbeschwerde, Artikel "
     "vierundneunzig Absatz eins Nummer vier a.", P),
    ("[vbbef]Stichwort Beschwerdebefugnis: Gegen ein Gesetz muss sie selbst, gegenwärtig und unmittelbar betroffen sein. "
     "[vbfrist]Die Frist beträgt dann ein Jahr ab Inkrafttreten. Gegen ein Urteil gilt ein Monat, und vorher ist in der "
     "Regel der Rechtsweg zu erschöpfen.", PS),
    # --- J Organstreit --------------------------------------------------------------------------------------------------------
    ("[os]Zweitens: Herr Pohl und seine Fraktion. Sie streitet mit der Bundesregierung um eigene Rechte aus dem "
     "Grundgesetz, hier das Frage- und Informationsrecht. [wl1]Das ist der Organstreit, Artikel vierundneunzig Absatz eins "
     "Nummer eins.", P),
    ("[osbet]Antragsberechtigt ist die Fraktion als Teil des Bundestages, Antragsgegnerin ist die Bundesregierung. "
     "[osfrist]Die Frist beträgt sechs Monate. [osfest]Gewinnt die Fraktion, stellt das Gericht die Verletzung nur fest.", PS),
    # --- K abstrakte Normenkontrolle -----------------------------------------------------------------------------------------
    ("[ank]Drittens: Ministerpräsidentin Hagedorn. Ihre Landesregierung will nur eines: das Gesetz prüfen lassen, ohne "
     "Gegner. [wl2]Das ist die abstrakte Normenkontrolle, Artikel vierundneunzig Absatz eins Nummer zwei.", P),
    ("[ankber]Antragsberechtigt sind die Bundesregierung, eine Landesregierung oder ein Viertel der Mitglieder des "
     "Bundestages. [ankobj]Eigene Rechte muss niemand geltend machen, und eine Frist gibt es nicht.", PS),
    # --- L konkrete Normenkontrolle ------------------------------------------------------------------------------------------
    ("[knk]Viertens: Richter Glaser. Hier geht kein Bürger und kein Organ nach Karlsruhe, sondern ein Gericht. "
     "[wl100]Artikel hundert Absatz eins: Hält ein Gericht ein Gesetz, auf dessen Gültigkeit es bei der Entscheidung "
     "ankommt, für verfassungswidrig, so ist das Verfahren auszusetzen und die Entscheidung des "
     "Bundesverfassungsgerichtes einzuholen.", P),
    ("[knkmon]Ein Parlamentsgesetz wegen Verstoßes gegen das Grundgesetz verwerfen darf nur das Bundesverfassungsgericht. [knkueb]Glaser muss von der "
     "Verfassungswidrigkeit überzeugt sein, Zweifel reichen nicht. [knkerh]Und es muss für seine Entscheidung auf das "
     "Gesetz ankommen. [knkpart]Der Kunde selbst kann eine Vorlage nicht erzwingen.", PS),
    # --- M Bund-Länder-Streit ------------------------------------------------------------------------------------------------
    ("[bls]Und dann ist da noch die Bundesregierung. Das Land Süd setzt das Gesetz nicht um, der Bund rügt das. "
     "[blsstreit]Jetzt streiten Bund und Land über ihre Pflichten bei der Ausführung von Bundesrecht. [wl3]Das ist der "
     "Bund-Länder-Streit, Artikel vierundneunzig Absatz eins Nummer drei.", P),
    ("[blsbet]Gegenüber stehen sich nur Bundesregierung und Landesregierung. [blsbr]Führt das Land das Gesetz als eigene "
     "Angelegenheit aus, entscheidet zuerst der Bundesrat. Gegen seinen Beschluss geht es binnen eines Monats nach "
     "Karlsruhe.", PS),
    # --- N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst die Verfahrensart, erst dann prüfst du die Zulässigkeit. [tipp1]Die Frage, wer was "
     "gegen wen will, ist eine Klausurkonvention, keine Norm. [tipp2]Und zitiere die Zuständigkeit nach Artikel "
     "vierundneunzig. Ältere Urteile und Bücher nennen noch Artikel dreiundneunzig.", PS),
    # --- O Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]Punkt A: Geht es nur um die Gültigkeit einer Norm? [sa1]Römisch eins: Ein Gericht ist von der "
     "Verfassungswidrigkeit überzeugt: konkrete Normenkontrolle. [sa2]Römisch zwei: Eine Regierung oder ein Viertel des "
     "Bundestages: abstrakte Normenkontrolle.", P),
    ("[sb]Punkt B: Geht es um eigene Rechte? [sb1]Römisch eins: jedermann gegen die öffentliche Gewalt: Verfassungsbeschwerde. "
     "[sb2]Römisch zwei: Organ gegen Organ: Organstreit. [sb3]Römisch drei: Bund gegen Land oder umgekehrt: Bund-Länder-Streit.", PS),
    # --- P Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Geht es nur um die Gültigkeit eines Gesetzes, führt der Weg zur Normenkontrolle. [m2]Geht es um eigene Rechte, "
     "entscheidet, wer gegen wen streitet.", 1.4),
]
