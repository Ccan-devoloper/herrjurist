"""Folge 028 · Brokdorf-Beschluss: Darf man eine Demo verbieten? (Art. 8 GG)
Echter Fall sachlich nacherzählt: BVerfG, Beschl. v. 14.5.1985 – 1 BvR 233, 341/81 (BVerfGE 69, 315), Allgemeinverfügung
des Landrats des Kreises Steinburg vom 23.2.1981 gegen die Großdemonstration am Kernkraftwerk Brokdorf (28.2.1981).
Heutige Rechtslage: Versammlungsrecht seit der Föderalismusreform 2006 Ländersache (BVerfGE 122, 342 Rn. 2), VersG des Bundes
gilt fort, soweit kein Landesgesetz besteht (Art. 125a Abs. 1 GG).
Veranstalter, Richter und Politiker treten nicht als Figuren auf und werden nicht genannt. Neutral zur Kernkraft.
Figuren: Herr Böhm (Mitarbeiter der Kreisverwaltung), Elke (Anwohnerin, will friedlich demonstrieren).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Boehm": "christian", "Elke": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Großdemonstration ----------------------------------------------------------------------------
    ("[fall]Februar neunzehnhunderteinundachtzig, die Wilstermarsch in Schleswig-Holstein. [bau]In Brokdorf soll der Bau "
     "eines Kernkraftwerks weitergehen. [aufruf]Bürgerinitiativen rufen bundesweit zu einer Großdemonstration auf, am "
     "achtundzwanzigsten Februar. [frueher]Frühere Demonstrationen dort verliefen teilweise unfriedlich.", 0.3),
    ("[elke]Elke wohnt in der Marsch und will dabei sein.", 0.2),
    ("[e1]Ich will friedlich demonstrieren, so nah am Bauplatz wie möglich.", 0.3, "Elke"),
    # --- B Fall: das Verbot -----------------------------------------------------------------------------------------
    ("[boehm]Herr Böhm arbeitet beim Landrat des Kreises Steinburg, der Versammlungsbehörde. [zahl]Sie rechnet "
     "mit bis zu fünfzigtausend Menschen.", 0.2),
    ("[b1]Angemeldet ist nichts. Und in Flugblättern heißen einige Gruppen Gewalt gut. Wir verbieten alles.", 0.3, "Boehm"),
    ("[verbot]Am dreiundzwanzigsten Februar verbietet der Landrat per Allgemeinverfügung jede Demonstration gegen das "
     "Kraftwerk, [gebiet]drei Tage lang, auf rund zweihundertzehn Quadratkilometern. [sofort]Sofort vollziehbar.", 0.4),
    # --- C Fall: der Weg durch die Instanzen ---------------------------------------------------------------------------
    ("[vg]Das Verwaltungsgericht beschränkt das Verbot auf die Umgebung der Baustelle. [ovg]In der Nacht vor der "
     "Demonstration stellt das Oberverwaltungsgericht das ganze Verbot wieder her. [demo]Trotzdem demonstrieren weit mehr "
     "als fünfzigtausend Menschen, und es kommt auch zu Ausschreitungen. [vb]Es folgen Verfassungsbeschwerden. "
     "[frage]Durfte der Staat diese Demonstration verbieten? Und wann darf er das überhaupt?", 0.6),
    # --- D Sachverhalt --------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Bedeutung der Versammlungsfreiheit --------------------------------------------------------------------------
    ("[demok]Das Bundesverfassungsgericht beginnt grundsätzlich: Versammlungsfreiheit gehört zu den unentbehrlichen "
     "Funktionselementen eines demokratischen Gemeinwesens. [minder]Sie kommt gerade auch andersdenkenden Minderheiten "
     "zugute. [frueh]Versammlungen enthalten ein Stück unmittelbarer Demokratie, sie gehören zu einem politischen Frühwarnsystem. [selbst]Wer sich versammelt, bestimmt selbst über Ort, Zeitpunkt, Art und Inhalt.", P),
    # --- F Wortlaut Art. 8 I, Schutzbereich ----------------------------------------------------------------------------
    ("[wl8]Artikel acht Absatz eins: Alle Deutschen haben das Recht, sich ohne Anmeldung oder Erlaubnis friedlich und "
     "ohne Waffen zu versammeln.", P),
    ("[sb]Römisch eins: der Schutzbereich. [vers]Geschützt ist gemeinschaftliche, auf Kommunikation "
     "angelegte Entfaltung, auch die Demonstration. [fried]Unfriedlich ist jedenfalls, wer Gewalttätigkeiten gegen "
     "Personen oder Sachen begeht.", P),
    ("[einzel]Und wenn nur einige gewalttätig werden? Dann bleibt der Schutz für die friedlichen Teilnehmer erhalten. "
     "[umfunk]Sonst könnten Einzelne jede Demonstration umfunktionieren und praktisch jede "
     "Großdemonstration verbieten lassen. [kollek]Anders ist es nur, wenn die Demonstration im Ganzen unfriedlich "
     "verlaufen soll oder Veranstalter und Anhang Gewalt anstreben oder billigen.", P),
    ("[elke2]Auch die Behörde ging davon aus, dass die meisten friedlich demonstrieren wollten. Elke ist also geschützt. "
     "[ein]Römisch zwei: Das Verbot ist ein Eingriff.", PS),
    # --- G Wortlaut Art. 8 II, Anmeldepflicht ------------------------------------------------------------------------
    ("[wl82]Römisch drei: die Rechtfertigung. Artikel acht Absatz zwei: Für Versammlungen unter freiem Himmel kann dieses "
     "Recht durch Gesetz oder auf Grund eines Gesetzes beschränkt werden. [gleich]Aber nur zum Schutz gleichwertiger "
     "Rechtsgüter und unter strikter Wahrung der Verhältnismäßigkeit.", P),
    ("[anm]Und die fehlende Anmeldung? Paragraf vierzehn des Versammlungsgesetzes verlangt sie unter freiem Himmel. "
     "[ausn]Das ist verfassungsgemäß, solange die Pflicht nicht ausnahmslos gilt. [spontan]Spontanversammlungen, die sich aus aktuellem Anlass augenblicklich bilden, brauchen "
     "keine Anmeldung. [auto]Wer nicht anmeldet, riskiert nicht automatisch ein Verbot. Das Eingreifen "
     "wird nur leichter.", P),
    # --- H Wortlaut § 15 I VersG und strenge Voraussetzungen -----------------------------------------------------------
    ("[wl15]Grundlage des Verbots ist Paragraf fünfzehn Absatz eins. [merk]Die Behörde kann "
     "verbieten oder Auflagen machen, wenn nach den erkennbaren Umständen die öffentliche Sicherheit oder Ordnung "
     "unmittelbar gefährdet ist.", P),
    ("[eng]Das Gericht legt die Norm eng aus. [elem]Erstens: Verbote kommen im Wesentlichen nur zum Schutz elementarer "
     "Rechtsgüter in Betracht, die öffentliche Ordnung allein genügt im Allgemeinen nicht. "
     "[unmit]Zweitens: Die Gefährdung muss unmittelbar sein. [prog]Die Prognose braucht Tatsachen, "
     "bloßer Verdacht reicht nicht. [ultima]Drittens: Das Verbot ist ultima ratio, erst müssen Auflagen ausgeschöpft sein.", PS),
    # --- I Kooperation ---------------------------------------------------------------------------------------------------
    ("[koop]Und die Behörde muss versammlungsfreundlich verfahren und zu Dialog und Kooperation bereit sein. [schwelle]Je mehr die Veranstalter ihrerseits kooperieren, desto höher rückt die Schwelle für ein "
     "Eingreifen.", 0.3),
    ("[b2]Mit wem hätten wir denn sprechen sollen? Es gab keinen Veranstalter.", 0.3, "Boehm"),
    ("[e2]Wer zur Demonstration aufgerufen hat, war doch bekannt.", 0.3, "Elke"),
    ("[abm]Doch die Behörde kannte Zeit, Ort und Trägergruppen. Die selbst erwogene "
     "Abmahnung unterließ sie aber.", PS),
    # --- J Anwendung und Ergebnis ------------------------------------------------------------------------------------
    ("[subs]Und im Fall? Das enge Verbot um die Baustelle hält das Gericht für vertretbar: [zaun]Für Gewalt am Bauzaun "
     "gab es erkennbare Anhaltspunkte, und die Demonstranten trugen selbst nichts zur Entschärfung bei. [rest]Für die übrige Marsch fehlten sie. [angst]Befürchtungen in der Bevölkerung "
     "genügen nicht. [mehr]Und die weit überwiegende Mehrheit wollte friedlich demonstrieren.", P),
    ("[erg]Am vierzehnten Mai neunzehnhundertfünfundachtzig gibt das Gericht den Verfassungsbeschwerden teilweise statt. "
     "[verf]Den Ausschlag gibt ein Verfahrensfehler: Nach damaligem Recht durfte das Oberverwaltungsgericht den "
     "Beschluss des Verwaltungsgerichts gar nicht zum Nachteil der Beschwerdeführer ändern. [kuenft]Verbote in diesem "
     "Umfang und mit dieser Begründung könnten künftig aber schwerlich gebilligt werden.", PS),
    # --- K Rechtslage heute ---------------------------------------------------------------------------------------------
    ("[heute]Und heute? Seit der Föderalismusreform zweitausendsechs ist das Versammlungsrecht Ländersache. [bayern]Bayern "
     "hatte als erstes Land ein eigenes Gesetz. [fort]Wo ein Land keines erlassen hat, gilt das Versammlungsgesetz des "
     "Bundes fort. [bind]Die Maßstäbe aus Brokdorf folgen "
     "aus Artikel acht und binden jeden Gesetzgeber.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei einem Verbot immer zuerst das mildere Mittel. [tipp1]Genügen Auflagen "
     "oder ein räumlich begrenztes Verbot, ist das Totalverbot unverhältnismäßig.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Schutzbereich: [k1a]Versammlung, [k1b]friedlich und ohne Waffen, "
     "Unfriedlichkeit Einzelner schadet den übrigen nicht. [k2]Römisch zwei: Eingriff durch Verbot oder Auflösung. "
     "[k3]Römisch drei, Rechtfertigung: [k3a]Schranke aus Artikel acht Absatz zwei, [k3b]Paragraf fünfzehn: "
     "unmittelbare Gefährdung aus erkennbaren Umständen, [k3c]Auflagen vor Verbot, [k3d]fehlende "
     "Anmeldung allein genügt nicht, [k3e]und die Kooperation der Behörde.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Demonstration zu verbieten, ist das letzte Mittel. [m2]Unfriedliche Einzelne nehmen der "
     "friedlichen Mehrheit den Schutz von Artikel acht nicht.", 1.4),
]
