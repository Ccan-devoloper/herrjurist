"""Folge 016 · Volkszählungsurteil: Die Geburtsstunde des Datenschutzes (Art. 2 I GG).
Echter Fall sachlich nacherzählt: BVerfG, Urt. v. 15.12.1983 – 1 BvR 209, 269, 362, 420, 440, 484/83 (BVerfGE 65, 1);
Volkszählungsgesetz 1983 vom 25.3.1982 (BGBl. I S. 369). Ausblick: BVerfGE 152, 216 (Recht auf Vergessen II).
Beschwerdeführer, Richter und Politiker treten nicht als Figuren auf. Fiktive Figuren: Frau Hartmann (soll den Fragebogen
ausfüllen), Herr Lehmann (ehrenamtlicher Zähler, Behördenfigur), Herr Sommer (Nachbar, Bürgerinitiative).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Hartmann": "lisa", "Lehmann": "niklas", "Sommer": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: der Fragebogen ----------------------------------------------------------------------------------
    ("[fall]Frühjahr neunzehnhundertdreiundachtzig. Die Bundesrepublik plant eine Volkszählung. [bogen]Frau Hartmann "
     "soll den Fragebogen ausfüllen. [fragen]Gefragt wird nach Beruf und Arbeitsstätte, nach dem Weg zur Arbeit, nach Wohnung, "
     "Miete und Religion.", 0.3),
    ("[zaehler]Bringen soll ihn Herr Lehmann, ein ehrenamtlicher Zähler.", 0.2),
    ("[z1]Ausfüllen müssen Sie das. Sonst droht ein Bußgeld.", 0.3, "Lehmann"),
    ("[h1]Und wer bekommt meine Angaben am Ende alles zu sehen?", 0.4, "Hartmann"),
    # --- B Fall: was mit den Daten geschehen soll ---------------------------------------------------------------
    ("[melde]Das Gesetz erlaubt sogar, die Angaben mit dem Melderegister zu vergleichen und es damit zu berichtigen. "
     "[weiter]Einzelangaben dürfen außerdem an Behörden und Gemeinden gehen.", 0.3),
    ("[sommer]Nebenan wohnt Herr Sommer. Er ist in einer Bürgerinitiative aktiv.", 0.2),
    ("[s1]Wenn der Staat das alles speichert und verknüpft, gehe ich da lieber nicht mehr hin.", 0.4, "Sommer"),
    ("[frage]Viele Bürger erheben Verfassungsbeschwerde direkt gegen das Volkszählungsgesetz. Darf der Staat so fragen? "
     "Und was darf er mit den Antworten tun?", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Zulässigkeit -----------------------------------------------------------------------------------------
    ("[zul]Zulässig waren die Beschwerden ausnahmsweise direkt gegen das Gesetz. [eile]Die Bögen sollten binnen weniger "
     "Wochen verteilt und eingesammelt werden. Für den Weg durch die Verwaltungsgerichte blieb kaum Zeit.", PS),
    # --- E Schutzbereich ----------------------------------------------------------------------------------------
    ("[sb]Maßstab ist das allgemeine Persönlichkeitsrecht, Artikel zwei Absatz eins in Verbindung mit Artikel eins "
     "Absatz eins. [ris]Das Gericht entwickelt daraus das Recht auf informationelle Selbstbestimmung: [ris2]Jeder darf "
     "grundsätzlich selbst über die Preisgabe und Verwendung seiner persönlichen Daten bestimmen.", P),
    ("[edv]Warum gerade jetzt? Mit automatischer Datenverarbeitung lassen sich Daten unbegrenzt speichern, in Sekunden "
     "abrufen und zu einem Persönlichkeitsbild zusammenfügen. [belang]Deshalb gibt es kein belangloses Datum mehr. "
     "[wofuer]Entscheidend ist, wofür es verwendet und womit es verknüpft werden kann.", P),
    ("[wer]Wer nicht weiß, wer was wann über ihn weiß, wird vorsichtig. [bi]Wer fürchtet, dass seine Teilnahme an einer "
     "Bürgerinitiative registriert wird, verzichtet vielleicht darauf. [gemein]Das schadet auch dem Gemeinwohl.", PS),
    # --- F Eingriff und Schranke --------------------------------------------------------------------------------
    ("[ein]Die Auskunftspflicht mit drohendem Bußgeld ist ein Eingriff. [schranke]Schrankenlos gilt das Recht aber "
     "nicht. Einschränkungen im überwiegenden Allgemeininteresse muss jeder hinnehmen. [gesetz]Nötig ist eine "
     "gesetzliche Grundlage, aus der Voraussetzungen und Umfang klar erkennbar sind: Normenklarheit. "
     "[vhm]Dazu kommen Verhältnismäßigkeit [vork]und organisatorische und verfahrensrechtliche Schutzvorkehrungen.", PS),
    # --- G Zweckbindung -----------------------------------------------------------------------------------------
    ("[zweck]Daten für die Verwaltung unterliegen einer strengen Zweckbindung: Der Zweck muss bereichsspezifisch und "
     "präzise bestimmt sein. [stat]Bei der Statistik geht das nicht, sie dient vielen Zwecken. [abschott]Zum Ausgleich "
     "verlangt das Gericht Abschottung: Statistikgeheimnis und möglichst frühe Anonymisierung.", PS),
    # --- H Die Erhebung selbst ----------------------------------------------------------------------------------
    ("[fragenok]Die Fragen selbst hielt das Gericht für zulässig: klar genug und verhältnismäßig. [stich]Stichproben "
     "seien noch zu fehleranfällig. Und vorhandene Register zusammenzuführen, bräuchte ein einheitliches "
     "Personenkennzeichen.", P),
    ("[umschlag]Aber Frau Hartmann darf den Bogen im verschlossenen Umschlag abgeben oder per Post schicken. "
     "[nach]Und der Gesetzgeber muss nachbessern: [nach1]über diese Rechte belehren, [nach2]Namen und Anschriften früh "
     "löschen, [nach3]Zähler nicht in ihrer eigenen Nachbarschaft einsetzen.", PS),
    # --- I Paragraf 9 -------------------------------------------------------------------------------------------
    ("[abgl]Anders der Melderegisterabgleich. [unver]Er verbindet Statistik und Verwaltungsvollzug, also tendenziell "
     "Unvereinbares. [wohin]Welche Behörde die Daten danach wofür nutzt, ist nicht vorhersehbar. [nachteil]Das Verbot, "
     "die Erkenntnisse gegen den Einzelnen zu verwenden, verspricht mehr, als es leisten kann.", P),
    ("[uebermit]Auch die Regeln zur Weitergabe an Behörden und Gemeinden hielten nicht stand. [wiss]Nur die "
     "Weitergabe für die Wissenschaft war in Ordnung.", P),
    ("[erg]Am fünfzehnten Dezember neunzehnhundertdreiundachtzig entscheidet das Gericht: Die Volkszählung als solche ist "
     "zulässig. [nichtig]Paragraf neun Absatz eins bis drei des Gesetzes ist nichtig.", PS),
    # --- J Heute ------------------------------------------------------------------------------------------------
    ("[heute]Heute gilt für viele Datenverarbeitungen die Datenschutz-Grundverordnung der EU. [charta]Wo sie vollständig "
     "vereinheitlicht, prüft Karlsruhe in aller Regel an der EU-Grundrechtecharta, Artikel sieben und acht.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag nicht nur, welches Datum erhoben wird. [tipp1]Frag, wofür es verwendet und womit es "
     "verknüpft werden kann. [tipp2]Und trenne Statistik und Verwaltungsvollzug.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Schutzbereich: informationelle Selbstbestimmung. [k2]Römisch zwei, "
     "Eingriff: Erhebung, Speicherung, Verwendung oder Weitergabe. [k3]Römisch drei, Rechtfertigung: [k4]gesetzliche "
     "Grundlage im überwiegenden Allgemeininteresse, [k5]Normenklarheit, [k6]Verhältnismäßigkeit, [k7]Zweckbindung "
     "[k8]und Schutzvorkehrungen.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------
    ("[merke]Merke: Unter automatischer Datenverarbeitung gibt es kein belangloses Datum. [m2]Der Staat darf Daten nur "
     "auf klarer gesetzlicher Grundlage verlangen und nur für erkennbare Zwecke verwenden.", 1.4),
]
