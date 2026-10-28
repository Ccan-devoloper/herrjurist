"""Folge 043 · Stellvertretung Schema: Wann bindet der Vertreter den Chef? (Mo · Der Fall, Format Schema).
Beispielfall: Werbeagentur-Inhaber Herr Gruber bevollmächtigt seine Angestellte Wiebke mündlich, fünfzig Bürostühle für
höchstens 200 Euro das Stück zu kaufen; Wiebke wählt im Möbelhaus von Frau Engel selbst ein Modell zu 180 Euro und kauft
„für die Agentur Gruber“; Frau Engel verlangt von Herrn Gruber 9.000 Euro (§ 433 II i. V. m. § 164 I BGB).
Schema § 164 I: 1. eigene Willenserklärung (Abgrenzung Bote, § 165), 2. im fremden Namen (Offenkundigkeit, § 164 I 2,
unternehmensbezogenes Geschäft, Geschäft für den, den es angeht, § 164 II), 3. mit Vertretungsmacht (Vollmacht §§ 166 II,
167 I, Umfang); Rechtsfolge, Wissenszurechnung § 166 I (mit § 442). Gegenfälle: Überschreitung (Designerstühle 400 Euro) →
§ 177 I, Verweigerung → § 179 I als Ausblick; ohne Vollmacht, aber wiederholtes geduldetes Auftreten → Duldungs-/
Anscheinsvollmacht (Rechtsscheinsvollmacht, BGH VIII ZR 289/09 Rn. 15 f.); § 181 in einem Satz.
Wortlautkarten: § 164 I 1, § 167 I, § 177 I BGB. Fiktive Figuren: Herr Gruber, Wiebke, Frau Engel.
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) =
Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor. Keine Genitivformen der Namen."""

P, PS = 0.4, 0.9

STIMMEN = {"Gruber": "stephan", "Wiebke": "sabrina", "Engel": "laura_klar"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: der Auftrag in der Agentur ------------------------------------------------------------------------
    ("[fall]Herr Gruber führt eine Werbeagentur. [auftrag]Seine Angestellte Wiebke soll neue Bürostühle besorgen.", 0.3),
    ("[g1]Wiebke, kaufen Sie fünfzig Bürostühle für die Agentur. Höchstens zweihundert Euro das Stück!", 0.4, "Gruber"),
    # --- B Fall: im Möbelhaus ----------------------------------------------------------------------------------------
    ("[laden]Wiebke fährt ins Möbelhaus von Frau Engel. [probe]Sie testet mehrere Modelle und wählt einen Stuhl für "
     "hundertachtzig Euro.", 0.3),
    ("[w1]Ich kaufe für die Agentur Gruber fünfzig Stück von diesem Modell.", 0.4, "Wiebke"),
    ("[e1]Sehr gern. Das macht neuntausend Euro, die Rechnung geht an Herrn Gruber.", 0.4, "Engel"),
    # --- C Fall: die Rechnung, die Frage ------------------------------------------------------------------------------
    ("[rechnung]Eine Woche später öffnet Herr Gruber die Rechnung.", 0.3),
    ("[g2]Ich habe mit Frau Engel nie ein Wort gewechselt. Warum soll ich zahlen?", 0.4, "Gruber"),
    ("[frage]Bindet Wiebke ihren Chef? Wir prüfen die Stellvertretung in drei Schritten.", 0.6),
    # --- D Sachverhalt ---------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Anspruch und Wortlaut § 164 I -----------------------------------------------------------------------------
    ("[ansp]Frau Engel verlangt neuntausend Euro nach Paragraf vierhundertdreiunddreißig Absatz zwei. [vertrag]Dafür "
     "braucht sie einen Kaufvertrag mit Herrn Gruber. Erklärt hat aber nur Wiebke. [p164]Paragraf hundertvierundsechzig "
     "Absatz eins: Eine Willenserklärung, die jemand innerhalb der ihm zustehenden Vertretungsmacht im Namen des "
     "Vertretenen abgibt, wirkt unmittelbar für und gegen den Vertretenen. [drei]Daraus ergeben sich also drei Prüfungspunkte.", PS),
    # --- F 1. eigene Willenserklärung ---------------------------------------------------------------------------------
    ("[s1]Erstens: eine eigene Willenserklärung. [bote]Ein Bote überbringt nur eine fremde Erklärung, ein Vertreter "
     "erklärt selbst. [aussen]Entscheidend ist, wie die Person nach außen auftritt. [s1ok]Wiebke wählt das Modell selbst "
     "aus und erklärt den Kauf: Sie ist Vertreterin, keine Botin. [p165]Übrigens könnte sogar eine siebzehnjährige "
     "Praktikantin wirksam vertreten, Paragraf hundertfünfundsechzig.", PS),
    # --- G 2. im fremden Namen -------------------------------------------------------------------------------------------
    ("[s2]Zweitens: im fremden Namen. Das ist das Offenkundigkeitsprinzip. [ausdr]Wiebke sagt ausdrücklich: für die "
     "Agentur Gruber. [umst]Nach Satz zwei genügt es aber auch, wenn sich das aus den Umständen ergibt. [unt]Wer erkennbar "
     "für ein Unternehmen handelt, macht im Zweifel dessen Inhaber zum Vertragspartner: das unternehmensbezogene "
     "Geschäft. [angeht]Bei Bargeschäften des täglichen Lebens darf die Offenlegung sogar fehlen, wenn es dem Partner "
     "gleichgültig ist, mit wem er abschließt: das Geschäft für den, den es angeht. [p164b]Bleibt der Wille, für den "
     "Chef zu handeln, dagegen unerkennbar, ist Wiebke selbst gebunden, Absatz zwei.", PS),
    # --- H 3. mit Vertretungsmacht ---------------------------------------------------------------------------------------
    ("[s3]Drittens: mit Vertretungsmacht. [p1662]Wird sie durch Rechtsgeschäft erteilt, heißt sie Vollmacht, Paragraf "
     "hundertsechsundsechzig Absatz zwei. [p167]Nach Paragraf hundertsiebenundsechzig Absatz eins erteilt man sie "
     "gegenüber dem Vertreter oder gegenüber dem Dritten. [innen]Herr Gruber hat sie Wiebke gegenüber erklärt: eine "
     "Innenvollmacht, mündlich genügt. [umfang]Ihr Umfang: fünfzig Stühle, höchstens zweihundert Euro das Stück. "
     "[s3ok]Hundertachtzig Euro liegen darunter. Die Vollmacht deckt den Kauf.", PS),
    # --- I Rechtsfolge, Wissenszurechnung --------------------------------------------------------------------------------
    ("[folge]Rechtsfolge: Die Erklärung von Wiebke wirkt unmittelbar für und gegen Herrn Gruber. [zahlt]Er ist "
     "Vertragspartner und muss die neuntausend Euro zahlen, Wiebke selbst nicht. [p166]Bei Willensmängeln und Wissen "
     "zählt aber die Person der Vertreterin, Paragraf hundertsechsundsechzig Absatz eins. [kratzer]Sieht Wiebke beim "
     "Kauf Kratzer an den Stühlen, hat Herr Gruber wegen dieser Kratzer keine Mängelrechte, Paragraf "
     "vierhundertzweiundvierzig.", PS),
    # --- J Gegenfall 1: Überschreitung, § 177, § 179 -------------------------------------------------------------------
    ("[ueber]Nun der erste Gegenfall: Wiebke verliebt sich in Designerstühle für vierhundert Euro das Stück. Frau Engel weiß "
     "von der Grenze nichts. [ueber2]Der Kauf überschreitet die Vollmacht. Wiebke handelt ohne Vertretungsmacht. "
     "[p177]Paragraf hundertsiebenundsiebzig Absatz eins: Schließt jemand ohne Vertretungsmacht im Namen eines anderen "
     "einen Vertrag, so hängt die Wirksamkeit des Vertrags für und gegen den Vertretenen von dessen Genehmigung ab. "
     "[schwebend]Bis dahin ist der Vertrag schwebend unwirksam.", P),
    ("[g3]Zwanzigtausend Euro für Stühle? Das genehmige ich nicht!", 0.4, "Gruber"),
    ("[p179]Dann haftet Wiebke selbst. Sie kannte ihre Grenze, also kann Frau Engel nach Paragraf "
     "hundertneunundsiebzig Absatz eins wählen: Erfüllung oder Schadensersatz.", PS),
    # --- K Gegenfall 2: Rechtsscheinsvollmacht --------------------------------------------------------------------------
    ("[schein]Zweiter Gegenfall: Herr Gruber hat Wiebke nie bevollmächtigt. Sie kauft aber seit Monaten Möbel bei "
     "Frau Engel, und Herr Gruber weiß das und zahlt jedes Mal. [duld]Lässt der Chef das Auftreten willentlich "
     "geschehen und darf der Partner daraus auf eine Vollmacht schließen, liegt eine Duldungsvollmacht vor. "
     "[anschein]Kennt er es nicht, hätte es aber bei pflichtgemäßer Sorgfalt erkennen und verhindern können, und darf "
     "der Partner auf seine Billigung vertrauen, kommt eine Anscheinsvollmacht in Betracht, in der Regel nur bei "
     "gewisser Dauer und Häufigkeit. [rs]Beide stehen nicht ausdrücklich im Gesetz. Die Rechtsprechung erkennt sie als "
     "Rechtsscheinsvollmacht an. [rsok]Hier kann Herr Gruber also aus Duldungsvollmacht gebunden sein.", PS),
    # --- L § 181 in einem Satz ------------------------------------------------------------------------------------------
    ("[p181]Zuletzt in einem Satz: Verkauft Wiebke der Agentur im Namen von Herrn Gruber ihre eigenen alten Stühle, "
     "kann sie dieses Insichgeschäft nach Paragraf hunderteinundachtzig nur vornehmen, wenn es ihr gestattet ist oder "
     "ausschließlich eine Verbindlichkeit erfüllt.", PS),
    # --- M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Paragraf hundertvierundsechzig ist keine Anspruchsgrundlage. [tipp2]Du prüfst ihn beim "
     "Vertragsschluss, also innerhalb des Anspruchs auf den Kaufpreis. [tipp3]Und bei der Vertretungsmacht gehst du der "
     "Reihe nach vor: erst echte Vollmacht, dann Rechtsscheinsvollmacht, zuletzt die Genehmigung.", PS),
    # --- N Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Engel gegen Gruber aus Paragraf vierhundertdreiunddreißig Absatz zwei. [k1]Römisch eins: "
     "Kaufvertrag zwischen Engel und Gruber, durch die Erklärung von Wiebke nach Paragraf hundertvierundsechzig Absatz "
     "eins. [k11]Eins: eigene Willenserklärung. [k12]Zwei: im fremden Namen. [k13]Drei: mit Vertretungsmacht, sonst "
     "Genehmigung nach Paragraf hundertsiebenundsiebzig. [k2]Römisch zwei: Ergebnis. Herr Gruber muss zahlen.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Vertreter bindet den Chef, wenn er eine eigene Erklärung im Namen des Chefs abgibt und "
     "Vertretungsmacht hat. [m2]Fehlt die Vertretungsmacht, entscheidet der Chef mit seiner Genehmigung.", 1.4),
]
