"""Folge 006 · Anspruchsaufbau Zivilrecht: Wer will was von wem woraus? (Methodik).
Beispielfall: Mieterin zieht nach eigener Kündigung nicht aus und hält die Schlüssel wegen der Kaution zurück (frei erfunden).
Fallfrage zerlegen (Wer/Was/Von wem/Woraus), Prüfungsreihenfolge der Anspruchsgrundlagen mit Begründung (Lehre, an Normen
festgemacht: §§ 986, 812, 677, 993 BGB), Anspruch entstanden – nicht erloschen – durchsetzbar am § 546 Abs. 1 BGB (§ 570 BGB).
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Albers": "william", "Jana": "ela_warm", "Noah": "timo"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: an der Wohnungstür ---------------------------------------------------------------------------------
    ("[haus]Jana wohnt zur Miete in einer Wohnung, die Herrn Albers gehört. "
     "[kuend]Am zweiten Januar kündigt sie schriftlich zum einunddreißigsten März.", 0.3),
    ("[april]Am ersten April klingelt Albers. [noch]Jana wohnt immer noch dort.", 0.3),
    ("[a1]Der Mietvertrag ist vorbei. Ich will meine Wohnung zurück!", 0.3, "Albers"),
    ("[j1]Erst will ich meine Kaution zurück. Vorher bekommen Sie die Schlüssel nicht.", 0.3, "Jana"),
    ("[tuer]Dann schließt sie die Tür.", 0.5),
    # --- B Klausurfrage --------------------------------------------------------------------------------------------
    ("[klausur]In der Klausur lautet die Frage: Kann Albers von Jana die Rückgabe der Wohnung verlangen?", 0.3),
    ("[n1]Mietvertrag, Eigentum, Kaution … wo fange ich bloß an?", 0.4, "Noah"),
    ("[vier]Mit vier Fragen: Wer will was von wem woraus?", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Fallfrage zerlegen ---------------------------------------------------------------------------------------------
    ("[wer]Wer? Albers, der Anspruchsteller. [was]Was? Die Rückgabe der Wohnung, kein Geld, kein Schadensersatz. "
     "[vonwem]Von wem? Von Jana, der Anspruchsgegnerin.", P),
    ("[woraus]Woraus? Aus einer Anspruchsgrundlage: einer Norm, deren Rechtsfolge genau dieses Ziel gewährt.", PS),
    # --- E Reihenfolge -------------------------------------------------------------------------------------------------------
    ("[reihe]Die Anspruchsgrundlagen prüfst du in fester Reihenfolge. [r1]Erstens Vertrag. "
     "[r2]Zweitens vertragsähnliche Ansprüche, etwa culpa in contrahendo oder Geschäftsführung ohne Auftrag. "
     "[r3]Drittens dingliche Ansprüche, [r4]viertens Delikt, [r5]fünftens Bereicherung.", P),
    ("[lehre]Diese Reihenfolge steht in keinem Gesetz. Sie ist Lehre, aber gut begründet: "
     "Was früher kommt, kann spätere Ansprüche ausschließen.", PS),
    # --- F Warum? Vorrang ----------------------------------------------------------------------------------------------------
    ("[w1]Ein Vertrag kann ein Recht zum Besitz geben. Dann scheitert die Herausgabe nach Paragraf neunhundertfünfundachtzig "
     "an Paragraf neunhundertsechsundachtzig. [w2]Und er liefert den rechtlichen Grund für das Geleistete. Dann scheitert die "
     "Bereicherung nach Paragraf achthundertzwölf.", P),
    ("[w3]Geschäftsführung ohne Auftrag setzt schon nach dem Wortlaut voraus, dass kein Auftrag besteht, also erst den Vertrag klären. "
     "[w4]Und nach Paragraf neunhundertdreiundneunzig schuldet der redliche Besitzer dem Eigentümer im Übrigen keinen Schadensersatz. [w4b]Darum dinglich vor Delikt. "
     "[w5]Die Bereicherung kommt zuletzt: Ob etwas ohne rechtlichen Grund erlangt ist, hängt von allem davor ab.", PS),
    # --- G I. Vertrag: § 546 Abs. 1 ----------------------------------------------------------------------------------------------
    ("[i]Also zuerst der Vertrag: Paragraf fünfhundertsechsundvierzig Absatz eins, die Rückgabepflicht des Mieters.", P),
    ("[drei]Jeden Anspruch prüfst du in drei Schritten: entstanden, nicht erloschen, durchsetzbar.", P),
    ("[entst]Entstanden? Es gab einen Mietvertrag, [entst2]und Janas fristgerechte Kündigung hat ihn zum einunddreißigsten März beendet.", P),
    ("[erl]Nicht erloschen? Erfüllt wäre der Anspruch mit der Rückgabe. [erl2]Die Schlüssel hat Jana aber noch.", P),
    ("[durch]Durchsetzbar? Jana verlangt erst ihre Kaution. "
     "[p570]Doch nach Paragraf fünfhundertsiebzig hat der Mieter gegen den Rückgabeanspruch kein Zurückbehaltungsrecht. "
     "[faellig]Zurückzahlen muss Albers die Kaution ohnehin erst nach einer angemessenen Prüfungsfrist.", PS),
    # --- H II. bis V. ------------------------------------------------------------------------------------------------------------
    ("[ii]Vertragsähnliche Ansprüche sind nicht ersichtlich. "
     "[iii]Dann dinglich: Paragraf neunhundertfünfundachtzig. Albers ist Eigentümer, Jana Besitzerin. "
     "[rzb]Ein Recht zum Besitz hätte sie nur aus dem Mietvertrag, und der ist beendet. Auch dieser Anspruch besteht.", P),
    ("[feb]Anders im Februar: Da lief der Vertrag noch, [feb2]und Jana hätte die Herausgabe nach Paragraf "
     "neunhundertsechsundachtzig verweigern dürfen. [sperre]So entscheidet der Vertrag über den dinglichen Anspruch.", PS),
    ("[ivv]Delikt und Bereicherung hältst du kurz: Das Deliktsrecht führt zu Schadensersatz, Albers will aber seine Wohnung.", P),
    ("[erg]Ergebnis: Albers kann die Rückgabe verlangen, aus Paragraf fünfhundertsechsundvierzig und aus Paragraf "
     "neunhundertfünfundachtzig. [konk]Beide Ansprüche stehen nebeneinander.", PS),
    # --- I Typische Fehler -------------------------------------------------------------------------------------------------------
    ("[fehler]Und so beginnt Noah sein Gutachten:", 0.3),
    ("[n2]Albers könnte einen Anspruch aus Paragraf neunhundertfünfundachtzig haben. Jana hat aber einen Anspruch auf die Kaution.", 0.4, "Noah"),
    ("[f1]Erster Fehler: Er startet beim Eigentum. Ob Jana besitzen darf, sagt ihm aber erst der Vertrag. "
     "[f2]Zweiter Fehler: Die Kaution ist ein eigener Anspruch, Jana gegen Albers. "
     "[f3]Hier taucht sie nur als Gegenrecht auf, beim Punkt durchsetzbar.", PS),
    # --- J Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Jedes Gegenrecht hat seinen festen Platz. [t1]Was den Anspruch hindert, etwa Nichtigkeit, "
     "gehört zu entstanden. [t2]Erfüllung oder Aufrechnung lassen ihn erlöschen. "
     "[t3]Verjährung und Zurückbehaltungsrecht sind Einreden: Sie hindern nur die Durchsetzung. "
     "[t4]Wer die Verjährung beim Erlöschen prüft, verschenkt Punkte.", P),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]A: Albers gegen Jana auf Rückgabe der Wohnung. "
     "[k2]Römisch eins: Paragraf fünfhundertsechsundvierzig Absatz eins. [k3]Erstens entstanden: Mietvertrag, beendet. "
     "[k4]Zweitens nicht erloschen: keine Rückgabe. [k5]Drittens durchsetzbar: kein Zurückbehaltungsrecht, Paragraf fünfhundertsiebzig.", P),
    ("[k6]Römisch zwei: vertragsähnlich. [k7]Römisch drei: Paragraf neunhundertfünfundachtzig, "
     "kein Recht zum Besitz. [k8]Römisch vier und fünf: Delikt, Bereicherung. [k9]Römisch sechs: Ergebnis.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst fragst du, wer was von wem will. [m2]Das Woraus suchst du dann in fester Reihenfolge: "
     "Vertrag, vertragsähnlich, dinglich, Delikt, Bereicherung.", 1.4),
]
