"""Folge 013 · Luftsicherheitsgesetz: Darf der Staat ein Flugzeug abschießen? (frei nach BVerfGE 115, 118 – 1 BvR 357/05,
Urt. v. 15.2.2006; Plenum BVerfGE 132, 1 – 2 PBvU 1/11; BVerfGE 133, 241 – 2 BvF 1/05; LuftSiG i. d. F. vom 11.3.2026).
Personen erfunden (Verteidigungsminister Lorenz, die Pilotin, Herr Seiler), keine realen Politiker, kein realer Anschlag.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad. Sensibles Thema: Abschuss nur als Frage, kein Treffer, keine Opferbilder."""

P, PS = 0.4, 0.9

STIMMEN = {"Lorenz": "helmut", "Pilotin": "lucy", "Seiler": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Entführung -----------------------------------------------------------------------------
    ("[lage]Ein Passagierflugzeug auf dem Weg nach Berlin, hundertvierzig Menschen an Bord. [entf]Entführer bringen "
     "die Maschine in ihre Gewalt. [drohung]Sie kündigen an, das Flugzeug in ein volles Fußballstadion "
     "zu steuern.", 0.5),
    # --- B Fall: die Alarmrotte -----------------------------------------------------------------------------
    ("[jets]Zwei Kampfflugzeuge der Luftwaffe steigen auf. [warn]Sie warnen die Maschine und versuchen, "
     "sie abzudrängen. [meldet]Die Pilotin meldet:", 0.3),
    ("[p1]Keine Reaktion. Die Maschine hält Kurs auf das Stadion.", 0.5, "Pilotin"),
    # --- C Fall: die Entscheidung ---------------------------------------------------------------------------
    ("[minister]Im Lagezentrum muss Verteidigungsminister Lorenz entscheiden.", 0.3),
    ("[l1]Hundertvierzig an Bord, fünfzigtausend im Stadion. Darf ich den Abschuss befehlen?", 0.5, "Lorenz"),
    ("[gesetz]Nach dem Luftsicherheitsgesetz von zweitausendfünf durfte er das. [p143]Paragraf vierzehn Absatz drei "
     "erlaubte, mit Waffengewalt auf ein Flugzeug einzuwirken, das gegen das Leben von Menschen eingesetzt werden soll, "
     "[einzig]als einziges Mittel.", 0.6),
    # --- D Fall: die Verfassungsbeschwerde --------------------------------------------------------------------
    ("[seiler]Herr Seiler fliegt fast jede Woche.", 0.2),
    ("[s1]Dann dürfte der Staat auch mein Flugzeug abschießen. Dagegen wehre ich mich in Karlsruhe.", 0.4, "Seiler"),
    ("[frage]Darf der Staat ein entführtes Flugzeug abschießen, um andere zu retten, auch wenn Unbeteiligte an Bord sind?", 0.6),
    # --- E Sachverhalt ---------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Zulässigkeit ----------------------------------------------------------------------------------------
    ("[zul]Herr Seiler erhebt Verfassungsbeschwerde, heute nach Artikel vierundneunzig Absatz eins Nummer vier a "
     "Grundgesetz. [gegen]Sie richtet sich direkt gegen ein Gesetz. [befugt]Dann muss er selbst, gegenwärtig und "
     "unmittelbar betroffen sein. [oft]Weil er häufig fliegt, ist das hinreichend wahrscheinlich.", PS),
    # --- G Schutzbereich, Eingriff, Schranke ----------------------------------------------------------------------
    ("[sb]Zur Begründetheit. Geschützt ist das Recht auf Leben, Artikel zwei Absatz zwei Satz eins. [ein]Ein Abschuss "
     "führt mit an Sicherheit grenzender Wahrscheinlichkeit zum Tod aller an Bord.", P),
    ("[schranke]Eingriffe sind auf Grund eines Gesetzes erlaubt. [jeder]Aber nur, wenn es in jeder Hinsicht "
     "verfassungsgemäß ist.", PS),
    # --- H formell: Wehrverfassung ---------------------------------------------------------------------------------
    ("[formell]Formell scheiterte die Vorschrift schon an der Wehrverfassung. [art87]Die Bundeswehr darf "
     "außer zur Verteidigung nur eingesetzt werden, wo das Grundgesetz es ausdrücklich erlaubt. [art35]Hier passt nur "
     "Artikel fünfunddreißig: Hilfe bei einem besonders schweren Unglücksfall. [waffen]Spezifisch militärische Waffen "
     "wie die Bordwaffen eines Kampfjets erlaubt das nach dem Ersten Senat nicht.", P),
    ("[plenum]Zweitausendzwölf hat das Plenum des Gerichts das gelockert: Militärische Mittel sind nicht grundsätzlich "
     "ausgeschlossen, aber nur unter engen Voraussetzungen und als letztes Mittel.", PS),
    # --- I materiell: Menschenwürde -------------------------------------------------------------------------------
    ("[mw]Materiell geht es um die Menschenwürde, Artikel eins Absatz eins. [objekt]Der Staat darf keinen Menschen zum "
     "bloßen Objekt machen. [ausweg]Passagiere und Besatzung sitzen in einer ausweglosen Lage. [rettung]Schießt der "
     "Staat sie ab, benutzt er ihre Tötung als Mittel, um andere zu retten. [objekt2]Er behandelt sie als bloße Objekte "
     "seiner Rettungsaktion.", P),
    ("[ohnehin]Und wenn sie ohnehin sterben würden? Das Leben ist geschützt, egal wie lange es noch dauert. "
     "[waffe]Die Passagiere als Teil der Waffe zu sehen, macht sie zur Sache. [einw]Und eine Einwilligung beim "
     "Einsteigen ist eine lebensfremde Fiktion.", P),
    ("[schutz]Der Staat muss zwar auch die Menschen im Stadion schützen. [mittel]Aber nur mit "
     "verfassungsgemäßen Mitteln. [erg]Ergebnis: Paragraf vierzehn Absatz drei verletzt das Recht auf Leben in "
     "Verbindung mit der Menschenwürde. [nichtig]Zweitausendsechs erklärte das Gericht ihn für nichtig.", PS),
    # --- J Gegenfall: nur Täter an Bord ---------------------------------------------------------------------------
    ("[taeter]Anders, wenn nur die Entführer an Bord sind. [verantw]Wer ein Flugzeug als Waffe einsetzt, wird nicht zum "
     "Objekt. Ihm wird sein Handeln zugerechnet. [vhm]Insoweit hielt das Gericht einen Abschuss sogar für "
     "verhältnismäßig. [trotzdem]Nichtig war die Norm trotzdem ganz, wegen der Wehrverfassung.", PS),
    # --- K Rechtslage heute, Strafrecht ---------------------------------------------------------------------------
    ("[heute]Heute fehlt im Luftsicherheitsgesetz jede Befugnis, mit Waffengewalt auf ein Flugzeug mit Menschen an Bord "
     "einzuwirken. "
     "[drohne]Neu ist seit März zweitausendsechsundzwanzig Paragraf fünfzehn a: Gegen Drohnen darf die Bundeswehr "
     "Waffengewalt einsetzen, um einen besonders schweren Unglücksfall zu verhindern.", P),
    ("[straf]Ob ein trotzdem befohlener Abschuss strafbar wäre, hat das Gericht offengelassen. [streit]Diskutiert wird ein "
     "übergesetzlicher Notstand, das ist umstritten.", PS),
    # --- L Klausurtipp (Lexi) -----------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei den Unbeteiligten wägt das Gericht nicht ab. [tipp1]Die Verletzung der Würde entscheidet. "
     "[tipp2]Die Verhältnismäßigkeit prüfst du nur für die Täter.", PS),
    # --- M Klausurschema --------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]A, Zulässigkeit: Verfassungsbeschwerde, [k1b]selbst, gegenwärtig und "
     "unmittelbar betroffen. [k2]B, Begründetheit: Römisch eins, Schutzbereich Leben. [k3]Römisch zwei, Eingriff "
     "durch den Abschuss.", P),
    ("[k4]Römisch drei, Rechtfertigung: [k5]formell die Wehrverfassung, [k6]materiell die Menschenwürde. "
     "[k7]Bei Unbeteiligten verletzt, bei reinen Tätern verhältnismäßig.", PS),
    # --- N Merksatz (Lexi) ------------------------------------------------------------------------------------
    ("[merke]Merke: Der Staat darf Unbeteiligte nicht töten, um andere zu retten. [m2]Ihre Würde lässt sich nicht "
     "gegen die Zahl der Geretteten aufrechnen.", 1.4),
]
