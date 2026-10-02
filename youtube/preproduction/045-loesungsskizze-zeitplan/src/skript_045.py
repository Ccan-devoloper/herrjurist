"""Folge 045 · Lösungsskizze Klausur: Zeitplan für die 5-Stunden-Examensklausur (Fr · Methodik · Klausurtechnik).
Beispielfall: Erster Examenstag, Zivilrechtsklausur von neun bis vierzehn Uhr. Jakob überfliegt den Sachverhalt und schreibt
sofort los, Johanna liest und markiert zuerst. Um zwölf Uhr ist Jakob erst bei der Hälfte, Johanna schreibt nach ihrer Skizze
schon am Schwerpunkt. Gezeigt werden: Bearbeitungszeit nach Landesrecht (§ 5d Abs. 6 DRiG; Beispiel § 13 Abs. 1 S. 1 JAG NRW),
ein Zeitraster als Empfehlung (Erfahrungswert, keine Pflicht), Skizzentechnik und Umgang mit Zeitnot.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Johanna (spricht nicht), Jakob; die Aufsicht
bleibt ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Jakob": "niklas", "Aufsicht": "elinor"}  # Lexi = Erzählerstimme (Carla); Johanna spricht nicht

SEGMENTE = [
    # --- A Fall: neun Uhr im Klausursaal ------------------------------------------------------------------------------------
    ("[fall]Neun Uhr im Klausursaal. Erster Examenstag, eine Klausur im Zivilrecht. "
     "[aufgabe]Die Aufsicht legt die Aufgaben auf die Tische.", 0.3),
    ("[auf1]Die Bearbeitungszeit beginnt jetzt. Sie haben fünf Stunden.", 0.4, "Aufsicht"),
    ("[jakob]Jakob blättert kurz durch den Sachverhalt [los]und schreibt sofort los. "
     "[johanna]Johanna liest erst einmal, [marker]mit dem Textmarker in der Hand.", 0.5),
    # --- B Fall: zwölf Uhr ----------------------------------------------------------------------------------------------------
    ("[zwoelf]Zwölf Uhr.", 0.2),
    ("[auf2]Noch zwei Stunden.", 0.3, "Aufsicht"),
    ("[j1]Drei Stunden um, und ich bin erst bei der Hälfte!", 0.4, "Jakob"),
    ("[seiten]Jakob hat schon viele Seiten geschrieben, [nochnicht]aber das Problem des Falls kommt erst noch. "
     "[joh2]Johanna schreibt gerade am Schwerpunkt. [plan0]Ihr Plan liegt neben ihr.", 0.5),
    # --- C Frage --------------------------------------------------------------------------------------------------------------
    ("[frage]Was hat Johanna anders gemacht? [frage2]Sie hat die fünf Stunden geplant, mit einem Zeitplan und einer "
     "Lösungsskizze.", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Die Bearbeitungszeit ---------------------------------------------------------------------------------------------------
    ("[land]Wie lange eine Examensklausur dauert, regelt das Landesrecht, also das Ausbildungsgesetz oder die Prüfungsordnung deines Landes. "
     "[nrw]In Nordrhein-Westfalen etwa stehen für jede Aufsichtsarbeit der Pflichtfachprüfung fünf Stunden zur Verfügung. "
     "[regel]In der Regel sind es fünf Stunden. [eigen]Was für dich gilt, prüfst du in deiner eigenen Prüfungsordnung.", PS),
    # --- F Das Zeitraster ------------------------------------------------------------------------------------------------------
    ("[raster]Ein Zeitplan als Empfehlung, aus Erfahrung, nicht als Pflicht: [t1]etwa dreißig Minuten, um den Sachverhalt "
     "zu lesen und zu markieren. [t2]Zehn Minuten für die Fallfrage. [t3]Rund eine Stunde für die Lösungsskizze. "
     "[t4]Drei Stunden für die Niederschrift. [t5]Und zwanzig Minuten Puffer. "
     "[drittel]Ein Drittel der Zeit planst du, zwei Drittel schreibst du, den Puffer eingeschlossen. "
     "[verh]Wichtig ist dieses Verhältnis, nicht die einzelne Minute. "
     "[zweit]Im zweiten Examen bekommst du meist eine Akte statt eines fertigen Sachverhalts. Dann planst du fürs Lesen mehr "
     "Zeit ein.", PS),
    # --- G Schritt 1: Sachverhalt -----------------------------------------------------------------------------------------------
    ("[s1]Erstens: der Sachverhalt. Lies ihn zweimal, das erste Mal ohne Stift. "
     "[mark]Beim zweiten Lesen markierst du Personen, Daten und Geldbeträge. "
     "[ansicht]Achte auch auf die Rechtsansichten der Beteiligten. Sie zeigen oft, wo die Probleme liegen. "
     "[angabe]Und fast jede Angabe im Sachverhalt brauchst du später in der Lösung.", P),
    # --- H Schritt 2: Fallfrage ----------------------------------------------------------------------------------------------------
    ("[s2]Zweitens: die Fallfrage und der Bearbeitervermerk. [wer]Wer will was von wem? "
     "[nicht]Und was sollst du ausdrücklich nicht prüfen? "
     "[aufbau]Fragt der Vermerk nach Ansprüchen, baust du anders auf als bei der Strafbarkeit oder bei den Erfolgsaussichten "
     "einer Klage.", P),
    # --- I Schritt 3: Lösungsskizze ------------------------------------------------------------------------------------------------
    ("[s3]Drittens: die Lösungsskizze. [sammeln]Sammle zuerst alle Anspruchsgrundlagen, die in Betracht kommen, "
     "etwa aus Vertrag, aus Delikt und aus Bereicherung. [probl]Dann markierst du die Probleme. "
     "[schwer]Wo der Sachverhalt viele Einzelheiten liefert, liegt meist der Schwerpunkt. "
     "[stich]Schreib in Stichworten, aber mit Ergebnis und Argument. Dann musst du beim Schreiben nicht neu nachdenken.", P),
    ("[gewicht]Gib jedem Punkt eine Zeit. Am Schwerpunkt schreibst du ausführlich. "
     "[urteil]Was unproblematisch ist, stellst du im Urteilsstil in einem Satz fest. "
     "[jo3]Bei Johanna sind es drei Anspruchsgrundlagen. [jo4]Zwei sind schnell erledigt, eine trägt das Problem. "
     "[jo5]Dafür plant sie neunzig Minuten der Niederschrift ein.", P),
    # --- J Schritt 4 und 5: Niederschrift und Puffer ---------------------------------------------------------------------------------
    ("[s4]Viertens: die Niederschrift. Jetzt schreibst du aus, was die Skizze vorgibt, in ihrer Reihenfolge. "
     "[s5]Fünftens: der Puffer. [puffer]Er fängt Verzögerungen auf, und am Ende liest du deine Ergebnisse noch einmal.", PS),
    # --- K Zeitnot ---------------------------------------------------------------------------------------------------------------------
    ("[fehler]Und Jakob? Er hat alles gleich ausführlich geprüft, auch das Unproblematische. Ohne Skizze wusste er nicht, "
     "wo das Problem liegt. [not]Was tust du, wenn die Zeit trotzdem knapp wird? [not1]Dann formulierst du zuerst die Schwerpunkte aus. "
     "[not2]Den Rest schreibst du knapp im Urteilsstil. [glied]Die Gliederung bleibt trotzdem vollständig, so sieht der "
     "Korrektor, dass du den Aufbau kennst.", 0.3),
    ("[j2]Also erst das Problem. Der Rest kommt kurz.", 0.4, "Jakob"),
    ("[not3]Und gib nie leer ab: Jede Frage bekommt wenigstens ein Ergebnis.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib dir Uhrzeiten an die Skizze, nicht nur Minuten. "
     "[tipp2]Zum Beispiel: Skizze fertig um zehn Uhr vierzig, Niederschrift fertig um dreizehn Uhr vierzig. "
     "[tipp3]So merkst du sofort, wenn du hinter deinem Plan liegst.", PS),
    # --- M Zeitplan als Schema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Zeitplan für die Fünf-Stunden-Klausur. [k1]Römisch eins: Sachverhalt lesen und markieren, etwa dreißig Minuten. "
     "[k2]Römisch zwei: Fallfrage und Bearbeitervermerk, etwa zehn Minuten. [k3]Römisch drei: die Lösungsskizze, etwa eine "
     "Stunde, [k3a]mit Anspruchsgrundlagen, Problemen und Schwerpunkten. [k4]Römisch vier: die Niederschrift, etwa drei "
     "Stunden. [k5]Römisch fünf: der Puffer, etwa zwanzig Minuten.", PS),
    # --- N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Skizze verteilt die Zeit. [m2]Ausführlich wird es nur am Schwerpunkt, und abgegeben wird immer.", 1.4),
]
