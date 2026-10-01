"""Folge 003 · Gutachtenstil in 6 Minuten: Obersatz, Definition, Subsumtion (Methodik).
Beispielfall: Fahrradkauf auf dem Flohmarkt (frei erfunden), Anspruch auf Kaufpreiszahlung aus § 433 Abs. 2 BGB mit
abändernder Annahme (§ 150 Abs. 2 BGB) als Problemstelle. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Greta": "lisa", "Paul": "marc", "Mia": "ela_froh"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Flohmarkt ---------------------------------------------------------------------------------------
    ("[markt]Samstag auf dem Flohmarkt. [rad]Greta will ihr altes Fahrrad verkaufen. "
     "[paul]Paul bleibt stehen und fragt nach dem Preis.", 0.3),
    ("[g1]Achtzig Euro, und es gehört Ihnen.", 0.3, "Greta"),
    ("[p1]Ich nehme es für siebzig. Das Geld bringe ich morgen.", 0.3, "Paul"),
    ("[g2]Na gut, siebzig.", 0.4, "Greta"),
    ("[faehrt]Paul fährt mit dem Rad davon. [morgen]Doch am nächsten Tag kommt kein Geld. "
     "[achtzig]Greta ist verärgert und verlangt jetzt sogar achtzig Euro.", 0.5),
    # --- B Klausurfrage --------------------------------------------------------------------------------------------
    ("[klausur]Genau so beginnt deine erste Klausur: Hat Greta gegen Paul einen Anspruch auf achtzig Euro?", 0.3),
    ("[mia]Und wie schreibe ich das jetzt auf?", 0.4, "Mia"),
    ("[vier]Im Gutachtenstil, in vier Schritten: Obersatz, Definition, Subsumtion, Ergebnis.", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Schritt 1: Obersatz -------------------------------------------------------------------------------------------
    ("[ob]Schritt eins, der Obersatz. Er nennt die Frage, die du gleich prüfst: [wer]Wer will was von wem woraus?", P),
    ("[ob_satz]Hier also: Greta könnte gegen Paul einen Anspruch auf Zahlung von achtzig Euro "
     "aus Paragraf vierhundertdreiunddreißig Absatz zwei BGB haben. [konj]Das Wort könnte zeigt: Das Ergebnis ist noch offen.", P),
    ("[vor]Die Norm verpflichtet den Käufer, den vereinbarten Kaufpreis zu zahlen. "
     "[vor2]Dazu müssten Greta und Paul einen Kaufvertrag geschlossen haben.", PS),
    # --- E Schritt 2: Definition -------------------------------------------------------------------------------------------
    ("[def]Schritt zwei, die Definition. Sie sagt abstrakt, wann ein Merkmal erfüllt ist. "
     "[def2]Ein Vertrag kommt durch zwei übereinstimmende Willenserklärungen zustande: Angebot und Annahme, "
     "Paragrafen hundertfünfundvierzig folgende.", P),
    ("[quelle]Definitionen stammen aus dem Gesetz, aus der Rechtsprechung oder aus der Lehre. "
     "[bgh]Diese hier formuliert auch der Bundesgerichtshof so.", PS),
    # --- F Schritt 3: Subsumtion -------------------------------------------------------------------------------------------
    ("[sub]Schritt drei, die Subsumtion. Jetzt legst du den Sachverhalt neben die Definition. "
     "[ang]Greta bietet das Rad für achtzig Euro an. Das ist ein Angebot.", P),
    ("[ann]Hat Paul es angenommen? [ann2]Er will das Rad zwar, aber nur für siebzig Euro. "
     "[p150]Nach Paragraf hundertfünfzig Absatz zwei gilt eine Annahme mit Änderungen als Ablehnung, "
     "verbunden mit einem neuen Antrag.", P),
    ("[neu]Gretas Angebot über achtzig Euro ist damit erloschen. Paul macht ein neues Angebot über siebzig. "
     "[gr_ann]Und Greta nimmt es sofort an, [p147]wie es unter Anwesenden nötig ist: Paragraf hundertsiebenundvierzig Absatz eins.", P),
    ("[problem]Hier liegt das Problem des Falls. Darum schreibst du genau an dieser Stelle ausführlich.", PS),
    # --- G Schritt 4: Ergebnis -----------------------------------------------------------------------------------------------
    ("[erg]Schritt vier, das Ergebnis. Es beantwortet den Obersatz, jetzt ohne Konjunktiv. "
     "[erg2]Also haben Greta und Paul einen Kaufvertrag über siebzig Euro geschlossen.", P),
    ("[gezahlt]Gezahlt hat Paul nicht, der Anspruch ist also auch nicht erloschen. "
     "[erg3]Greta kann siebzig Euro verlangen, nicht achtzig.", PS),
    # --- H Gutachtenstil gegen Urteilsstil ------------------------------------------------------------------------------------
    ("[urteil]Und der Urteilsstil? Er dreht die Reihenfolge um: erst das Ergebnis, dann die Begründung. "
     "[urteil2]Greta hat gegen Paul einen Anspruch auf siebzig Euro, denn die beiden haben einen Kaufvertrag geschlossen.", P),
    ("[gericht]So begründen Gerichte ihre Entscheidungen. [signal]Typisch sind Wörter wie denn und weil. "
     "[signal2]Das Gutachten arbeitet dagegen mit könnte, müsste und also. "
     "[examen]Im zweiten Examen schreibst du die Entscheidungsgründe eines Urteils deshalb im Urteilsstil.", PS),
    # --- I Typische Fehler --------------------------------------------------------------------------------------------------------
    ("[fehler]Jetzt die typischen Fehler. Mia schreibt in ihrer Klausur:", 0.3),
    ("[mia2]Greta hat einen Anspruch, weil Paul das Rad gekauft hat.", 0.4, "Mia"),
    ("[f1]Erstens: Das Ergebnis steht am Anfang. Am Problem gehört es ans Ende. "
     "[f2]Zweitens: Die Anspruchsgrundlage fehlt, also das Woraus. "
     "[f3]Drittens: Gekauft ist nur eine Behauptung. Ob ein Kaufvertrag vorliegt, zeigst du erst mit Definition und Subsumtion.", PS),
    # --- J Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ausführlich im Gutachtenstil schreibst du nur dort, wo es ein Problem gibt. "
     "[tipp2]Was klar ist, stellst du in einem Satz im Urteilsstil fest. "
     "[tipp3]Gretas Angebot braucht keine vier Schritte. Pauls Antwort schon.", P),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zum Fall. [k1]Teil A: der Anspruch auf den Kaufpreis aus Paragraf vierhundertdreiunddreißig Absatz zwei. "
     "[k2]Römisch eins: Anspruch entstanden, durch einen Kaufvertrag. [k3]Erstens: Gretas Angebot über achtzig. "
     "[k4]Zweitens: Pauls Annahme? Nein, nach Paragraf hundertfünfzig Absatz zwei ein neues Angebot über siebzig. "
     "[k5]Drittens: Gretas Annahme.", P),
    ("[k6]Römisch zwei: Anspruch nicht erloschen, denn Paul hat nicht gezahlt. [k7]Römisch drei: Ergebnis, siebzig Euro. "
     "[k8]Und an jedem Prüfungspunkt dieselben vier Schritte: Obersatz, Definition, Subsumtion, Ergebnis.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Gutachten steht das Ergebnis am Ende, nicht am Anfang. "
     "[m2]Erst fragen, dann definieren, dann subsumieren, dann entscheiden.", 1.4),
]
