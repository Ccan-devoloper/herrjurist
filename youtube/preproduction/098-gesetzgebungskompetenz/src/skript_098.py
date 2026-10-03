"""Folge 098 · Gesetzgebungskompetenz: Bund oder Land? Art. 70 ff. GG erklärt (Mi · Examenswissen · Schema).
Beispielfall nach dem Hook des Themenplans (Vorbild offengelegt: Berliner Mietendeckel, BVerfG, Beschl. v. 25.3.2021 –
2 BvF 1/20 u. a., BVerfGE 157, 223): Der Landtag eines Landes beschließt ein Gesetz, nach dem die Miete für frei
finanzierte Wohnungen höchstens 9 €/m² betragen darf. Herr Henke (Vermieter) verlangt von Frau Dahlke (Mieterin, bisher
9 €/m²) nach § 558 BGB die Zustimmung zur Erhöhung auf die ortsübliche Vergleichsmiete von 10 €/m².
Schema der Gesetzgebungskompetenz in der formellen Verfassungsmäßigkeit: 1. Grundsatz Art. 70 I (Wortlautkarte),
2. ausschließliche Gesetzgebung Art. 71, 73, 3. konkurrierende Gesetzgebung Art. 72, 74: a) Kompetenztitel (Hauptzweck,
Art. 74 I Nr. 1; Föderalismusreform 2006/Wohnungswesen; Art. 125a I), b) Sperrwirkung Art. 72 I (Wortlautkarte),
c) Erforderlichkeitsklausel Art. 72 II (Auszug; BVerfGE 106, 62), d) Abweichungsrecht Art. 72 III, 4. ungeschriebene
Kompetenzen (ein Satz) → Ergebnis nichtig → Klausurtipp (Art. 31 GG) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Fiktive Figuren: die Landesministerin (julia), Frau Dahlke (ela_froh), Herr Henke (helmut).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Landesministerin": "julia", "Dahlke": "ela_froh", "Henke": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das neue Landesgesetz -------------------------------------------------------------------------------------
    ("[fall]Der Landtag eines Landes hat ein neues Gesetz beschlossen. [lm]Die Landesministerin stellt es vor.", 0.3),
    ("[lm1]Ab sofort gilt eine Mietobergrenze: Für frei finanzierte Wohnungen höchstens neun Euro pro Quadratmeter.", 0.4,
     "Landesministerin"),
    # --- B Fall: die Mieterhöhung ------------------------------------------------------------------------------------------
    ("[brief]Eine Woche später bekommt Frau Dahlke Post von ihrem Vermieter, Herrn Henke. [bisher]Sie zahlt bisher neun Euro "
     "pro Quadratmeter. [erh]Er verlangt nach dem BGB, dass sie einer Erhöhung auf zehn Euro zustimmt, der ortsüblichen "
     "Vergleichsmiete.", 0.3),
    ("[da1]Mehr als neun Euro verbietet doch das neue Landesgesetz!", 0.3, "Dahlke"),
    ("[he1]Die Miethöhe hat der Bund längst im BGB geregelt. Da hat das Land nichts zu sagen.", 0.4, "Henke"),
    ("[frage]Wer hat recht? Durfte das Land dieses Gesetz überhaupt machen? [vorbild]Vorbild ist der Berliner "
     "Mietendeckel. Über ihn hat das Bundesverfassungsgericht zweitausendeinundzwanzig entschieden.", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Einordnung --------------------------------------------------------------------------------------------------------
    ("[einord]Die Frage gehört in die formelle Verfassungsmäßigkeit des Landesgesetzes, und zwar an den Anfang: "
     "[zust]erst die Zuständigkeit, also die Gesetzgebungskompetenz, [verf]dann Verfahren und Form. [verw]Wie ein Gesetz "
     "nach Karlsruhe kommt, etwa mit der abstrakten Normenkontrolle, zeigt unser Video zu den Verfahrensarten.", PS),
    # --- E 1. Grundsatz, Wortlaut Art. 70 I ---------------------------------------------------------------------------------
    ("[wl70]Schritt eins: der Grundsatz. Artikel siebzig Absatz eins: Die Länder haben das Recht der Gesetzgebung, soweit "
     "dieses Grundgesetz nicht dem Bunde Gesetzgebungsbefugnisse verleiht. [frage70]Du fragst also: Gibt das Grundgesetz "
     "dem Bund diese Materie? [voll]Eine Doppelzuständigkeit gibt es nicht. Jede Materie gehört entweder dem Bund oder den "
     "Ländern.", PS),
    # --- F 2. ausschließliche Gesetzgebung -----------------------------------------------------------------------------------
    ("[aus]Schritt zwei: die ausschließliche Gesetzgebung des Bundes, Artikel einundsiebzig und dreiundsiebzig, etwa für "
     "auswärtige Angelegenheiten oder das Waffenrecht. [aus2]Dort dürfen die Länder nur, wenn ein Bundesgesetz sie "
     "ausdrücklich ermächtigt. [aus3]Die Miete steht nicht in Artikel dreiundsiebzig.", PS),
    # --- G 3. a) Kompetenztitel ----------------------------------------------------------------------------------------------
    ("[konk]Schritt drei: die konkurrierende Gesetzgebung, Artikel zweiundsiebzig und vierundsiebzig. [ta]Zuerst der "
     "Kompetenztitel. [haupt]Maßgeblich ist, was das Gesetz unmittelbar regelt, mit welchem Zweck und welcher Wirkung, "
     "nicht wie es heißt. Entscheidend ist der Hauptzweck. [nr1]Eine Mietobergrenze für frei finanzierte Wohnungen "
     "begrenzt den Preis im Mietvertrag. Das ist bürgerliches Recht, Artikel vierundsiebzig Absatz eins Nummer eins.", P),
    ("[wohn]Das Land beruft sich auf das Wohnungswesen. Diesen Titel hat die Föderalismusreform zweitausendsechs aus "
     "Artikel vierundsiebzig gestrichen, seitdem ist er Ländersache. [wohn2]Die Miethöhe auf dem freien Markt gehörte aber "
     "schon vorher zum bürgerlichen Recht, so das Bundesverfassungsgericht. [fort]Übrigens: Bundesrecht, das nach einer "
     "solchen Änderung nicht mehr als Bundesrecht erlassen werden könnte, gilt nach Artikel hundertfünfundzwanzig a als "
     "Bundesrecht fort. Die Länder können es ersetzen.", PS),
    # --- H 3. b) Sperrwirkung, Wortlaut Art. 72 I ------------------------------------------------------------------------------
    ("[wl72]Dann die Sperrwirkung, Artikel zweiundsiebzig Absatz eins: Im Bereich der konkurrierenden Gesetzgebung haben "
     "die Länder die Befugnis zur Gesetzgebung, solange und soweit der Bund von seiner Gesetzgebungszuständigkeit nicht "
     "durch Gesetz Gebrauch gemacht hat. [ab]Gebrauch gemacht hat er, soweit er die Materie abschließend geregelt hat. "
     "[bgb]Genau das hat er mit den Paragrafen fünfhundertsechsundfünfzig bis fünfhunderteinundsechzig BGB getan, mit "
     "Vergleichsmiete und Mietpreisbremse. [egal]Dann ist das Land gesperrt, ob sein Gesetz dem BGB widerspricht, es "
     "ergänzt oder nur wiederholt.", PS),
    # --- I 3. c) Erforderlichkeitsklausel, Art. 72 II ---------------------------------------------------------------------------
    ("[wl722]Und die Erforderlichkeitsklausel, Artikel zweiundsiebzig Absatz zwei? [liste]Sie gilt nur für die dort "
     "aufgezählten Nummern des Artikels vierundsiebzig. Dort darf der Bund nur regeln, wenn das erforderlich ist: für "
     "gleichwertige Lebensverhältnisse oder für die Rechts- oder Wirtschaftseinheit im gesamtstaatlichen Interesse. "
     "[streng]Das prüft das Bundesverfassungsgericht streng. Bundeseinheitliche Regeln allein genügen nicht. "
     "[streng2]Gleichwertige Lebensverhältnisse sind erst bedroht, wenn sie sich zwischen den Ländern erheblich "
     "auseinanderentwickeln. [n1]Nummer eins, das bürgerliche Recht, steht nicht in der Liste. Hier entfällt diese "
     "Prüfung.", P),
    # --- J 3. d) Abweichungsrecht, 4. ungeschriebene Kompetenzen ----------------------------------------------------------------
    ("[abw]Bleibt das Abweichungsrecht, Artikel zweiundsiebzig Absatz drei. In einigen Gebieten, etwa Jagdwesen, "
     "Naturschutz oder Grundsteuer, dürfen die Länder vom Bundesgesetz abweichen, und das spätere Gesetz geht vor. "
     "[abw2]Das Mietrecht steht nicht in diesem Katalog. [unge]Ungeschriebene Kompetenzen des Bundes, etwa kraft "
     "Sachzusammenhangs, als Annex oder aus der Natur der Sache, braucht es hier nicht: Der Titel steht ausdrücklich im "
     "Grundgesetz.", PS),
    # --- K Ergebnis ------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Dem Land fehlt die Gesetzgebungskompetenz. Das Landesgesetz ist formell verfassungswidrig und "
     "nichtig. [erg2]So hat das Bundesverfassungsgericht auch den Berliner Mietendeckel insgesamt für nichtig erklärt. "
     "[erg3]Über die Mieterhöhung entscheidet also allein das BGB.", 0.3),
    ("[da2]Dann prüfe ich die Mieterhöhung eben nach dem BGB.", 0.6, "Dahlke"),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Greif nicht vorschnell zu Artikel einunddreißig, Bundesrecht bricht Landesrecht. [tipp1]Prüfe "
     "zuerst die Kompetenz. Fehlt sie, ist das Landesgesetz schon deshalb nichtig. [tipp2]So hat auch das "
     "Bundesverfassungsgericht entschieden, obwohl sich die Antragsteller auch auf Artikel einunddreißig berufen hatten.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für die Gesetzgebungskompetenz. [s1]Erstens, der Grundsatz: die Länder, Artikel siebzig. "
     "[s2]Zweitens, die ausschließliche Gesetzgebung des Bundes, Artikel einundsiebzig und dreiundsiebzig. [s3]Drittens, "
     "die konkurrierende Gesetzgebung: [s3a]der Kompetenztitel aus Artikel vierundsiebzig, [s3b]die Sperrwirkung nach "
     "Artikel zweiundsiebzig Absatz eins, [s3c]die Erforderlichkeit nach Absatz zwei, nur bei den genannten Nummern, "
     "[s3d]und das Abweichungsrecht nach Absatz drei. [s4]Viertens, ungeschriebene Kompetenzen. [s5]Dann das Ergebnis, "
     "[s6]und danach Verfahren und Form.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gesetzgebung ist Ländersache, soweit das Grundgesetz sie nicht dem Bund gibt. [m2]Und im "
     "konkurrierenden Bereich sperrt ein abschließendes Bundesgesetz die Länder.", 1.4),
]
