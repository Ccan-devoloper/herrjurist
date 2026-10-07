"""Folge 237 · Probeklausuren Examen: Wie viele schreiben und wie auswerten? (Fr · Methodik · Lernen, Format Schritte).
Rahmen nach dem Plan-Hook („Du schreibst jede Woche eine Klausur, aber die Noten bleiben gleich“): Der Jurastudent
Friedrich (Mitte 20, studiert in Nordrhein-Westfalen) kommt mit einem Stapel von zwölf korrigierten Probeklausuren in die
Sprechstunde seines Mentors Herrn Seebach (um 60). Fast immer sechs Punkte – die Korrekturen hat er nie ausgewertet.
Aufbau: Hook → Sachverhalt → Problem: schreiben ohne auswerten → wie viele (Faustregel als Empfehlung; Verteilung wie im
Examen, Beispiel NRW § 10 Abs. 2 JAG NRW; Verweis 201) → wie im Examen (5 Stunden § 13 Abs. 1 S. 1 JAG NRW, Hilfsmittel
§ 13 Abs. 3 JAG NRW, elektronisch § 10 Abs. 1 JAG NRW; Landesrecht § 5d Abs. 6 S. 1 DRiG) → Auswertung in 4 Schritten
(Korrektur, Musterlösung gegen Gliederung, Fehlerprotokoll mit Aufbau/Schwerpunkt/Wissen/Zeit – Verweis 117 –,
Wiederholungskarten – Verweis 201) → Wochenrhythmus (Auswertungstag, Klausurtag) → Ergebnis → Klausurtipp (Lexi) →
Klausurtraining I.–V. → Merksatz (Lexi).
Alle Zahlen zur Menge (1 pro Woche, im Endspurt 2) sind Empfehlungen und im Sprechtext so gekennzeichnet („Eine
Faustregel, keine Vorschrift“); keine Studien, keine Anbieter, „Klausurenkurs“ nur allgemein. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche unter youtube/: 0 Treffer, Reservierung
„237: Friedrich, Seebach“): Friedrich, Herr Seebach; nie im Genitiv.
Stimmen (Pool niklas, helmut, ela_froh, julia): Friedrich niklas (Mann, jung), Herr Seebach helmut (Mann, älter); ela_froh
(nicht für ernste Rollen) und julia (möglichst meiden) nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Friedrich": "niklas", "Seebach": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Sprechstunde, der Stapel Klausuren --------------------------------------------------------------------
    ("[fall]Sprechstunde an der Uni. [stapel]Friedrich legt seinem Mentor, [seebach]Herrn Seebach, einen Stapel "
     "korrigierter Klausuren auf den Tisch.", P),
    ("[f1]Zwölf Klausuren in zwölf Wochen. Und fast immer sechs Punkte.", P, "Friedrich"),
    ("[s1]Und was machst du mit den Korrekturen?", P, "Seebach"),
    ("[f2]Ich schaue auf die Note. Und dann schreibe ich die nächste.", P, "Friedrich"),
    ("[hook]Du schreibst jede Woche eine Klausur, aber die Noten bleiben gleich? [hook2]Schreiben allein reicht nicht. "
     "Punkte bringt erst, was du aus jeder Korrektur lernst. [wie]Hier siehst du, wie viele Probeklausuren du schreibst "
     "und wie du sie auswertest.", P),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist die Ausgangslage von Friedrich. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem: schreiben ohne auswerten ------------------------------------------------------------------------
    ("[warum]Warum bleibt die Note stehen? [ohne]Friedrich schreibt, aber er wertet nicht aus. [gleich]Wer die "
     "Korrektur nicht liest, macht leicht in der nächsten Klausur wieder dieselben Fehler. [zwei]Eine Probeklausur hat "
     "zwei Hälften: [z1]das Schreiben, das die Routine trainiert, [z2]und die Auswertung, die dir zeigt, was du ändern "
     "musst.", P),
    ("[s2]Eine Klausur, die du nicht auswertest, hast du nur zur Hälfte geschrieben.", P, "Seebach"),
    # --- D Wie viele? ------------------------------------------------------------------------------------------------------
    ("[viele]Wie viele Klausuren solltest du schreiben? [faust]Eine Faustregel, keine Vorschrift: [woche]in der "
     "Stoffphase eine Klausur pro Woche, [spurt]in den letzten Wochen vor dem Examen zwei. [mehr]Mehr bringt nur etwas, "
     "wenn du jede davon auch auswertest. [lieber]Lieber eine Klausur weniger als eine ohne Auswertung.", P),
    ("[fach]Verteile die Probeklausuren auf die Fächer wie im Examen. [nrw]Dort schreibt Friedrich in Nordrhein-Westfalen "
     "sechs Klausuren: "
     "[nrw3]drei im Zivilrecht, [nrw2]zwei im Öffentlichen Recht [nrw1]und eine im Strafrecht. [haelfte]Also ist etwa "
     "die Hälfte seiner Probeklausuren Zivilrecht, [drittel]ein Drittel Öffentliches Recht [sechstel]und ein Sechstel "
     "Strafrecht. [land]Dein Land kann das anders regeln. [v201]Wie das in deinen Lernplan passt, zeigt Folge "
     "zweihunderteins.", P),
    # --- E Wie im Examen ----------------------------------------------------------------------------------------------------
    ("[bed]Schreib jede Probeklausur unter Examensbedingungen. [zeit]In Nordrhein-Westfalen stehen für jede "
     "Examensklausur fünf Stunden zur Verfügung. Dann schreibst du auch die Probeklausur fünf Stunden am Stück, im "
     "Klausurenkurs oder zu Hause. [hilf]Nur mit den "
     "Hilfsmitteln, die dein Land erlaubt, [form]und in deiner Form: von Hand oder am Computer. [handy]Das Handy bleibt "
     "aus, das Lehrbuch bleibt zu. [abbr]Und brich nicht ab, wenn es schlecht läuft. Gerade diese Klausur zeigt dir, wo "
     "deine Fehler liegen.", P),
    ("[ref]Im Referendariat funktioniert die Auswertung genauso. Zahl und Dauer der Klausuren regelt auch dort dein "
     "Land.", P),
    # --- F Auswertung in vier Schritten ---------------------------------------------------------------------------------
    ("[aus]Jetzt die Auswertung, in vier Schritten. [a1]Erstens: Lies die ganze Korrektur, nicht nur die Note. "
     "[a1b]Jede Randbemerkung zeigt dir eine Stelle, an der Punkte verloren gingen.", P),
    ("[a2]Zweitens: Leg die Musterlösung neben deine Gliederung. [a2b]Welches Problem hast du übersehen? [a2c]Wo hast "
     "du anders aufgebaut, und warum?", P),
    ("[a3]Drittens: das Fehlerprotokoll. [a3b]Jeden Fehler ordnest du einer Fehlerart zu: [fa]Aufbau, [fs]Schwerpunkt, "
     "[fw]Wissen [fz]oder Zeit. [v117]Die typischen Fehler im Einzelnen zeigt Folge hundertsiebzehn.", P),
    ("[prot]Friedrich wertet seine zwölf Klausuren nachträglich aus. [pa]Beim Aufbau findet er zwei Fehler, "
     "[ps]beim Schwerpunkt sieben, [pw]beim Wissen drei [pz]und bei der Zeit fünf.", P),
    ("[f3]Ich dachte, mir fehlt Wissen. Dabei verliere ich die Punkte am Schwerpunkt.", P, "Friedrich"),
    ("[a4]Viertens: Aus jedem Fehler wird eine Wiederholungskarte. [a4b]Vorn steht die Stelle, an der du Punkte verloren "
     "hast, hinten, wie es richtig geht. [a4c]Die Karten kommen in deine Wiederholung, wie in Folge zweihunderteins.", P),
    # --- G Wochenrhythmus -------------------------------------------------------------------------------------------------
    ("[wr]So sieht jetzt eine Woche von Friedrich aus. [wmo]Montag ist Auswertungstag: [wmo2]Er liest die Korrektur, "
     "die zurückgekommen ist, legt die Musterlösung daneben und trägt die Fehler ins Protokoll ein. [wdi]Von Dienstag "
     "bis Freitag lernt er Stoff, [wkarte]und jeden Morgen beginnt er mit seinen Fehlerkarten. [wfr]Am Freitag zählt "
     "er nach: Welche Fehlerart kommt am häufigsten? [wsa]Samstag ist Klausurtag, fünf Stunden. [wso]Und der Sonntag "
     "bleibt frei.", P),
    # --- H Ergebnis -------------------------------------------------------------------------------------------------------
    ("[erg]Drei Wochen später liegt die nächste Korrektur auf dem Tisch. [erg2]Diesmal steht am Rand kein "
     "Schwerpunkt-Fehler.", 0.2),
    ("[f4]Sieben Punkte. Und als Nächstes nehme ich mir die Zeit vor.", P, "Friedrich"),
    ("[s3]Genau so. Ein Fehler nach dem anderen.", PS, "Seebach"),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Nimm in jede Probeklausur ein einziges Ziel mit, deine häufigste Fehlerart. [tipp2]Schreib sie "
     "oben auf deine Lösungsskizze. [tipp3]Bevor du ausformulierst, prüfst du die Gliederung genau darauf.", PS),
    # --- J Klausurtraining als Schema -------------------------------------------------------------------------------------
    ("[sch]Dein Klausurtraining in fünf Schritten. [k1]Römisch eins: eine Klausur pro Woche, im Endspurt zwei. "
     "[k2]Römisch zwei: verteilt wie im Examen. [k3]Römisch drei: unter Examensbedingungen, fünf Stunden am Stück. "
     "[k4]Römisch vier: auswerten, also Korrektur, Musterlösung, Fehlerprotokoll und Karten. [k5]Römisch fünf: ein "
     "fester Auswertungstag in jeder Woche.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Klausur bringt dir erst Punkte, wenn du sie auswertest. [m2]Schreib so viele, wie du gründlich "
     "auswerten kannst, [m3]damit dir jeder Fehler nur einmal passiert.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
