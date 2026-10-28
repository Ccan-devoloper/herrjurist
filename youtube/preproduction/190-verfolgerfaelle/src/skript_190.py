"""Folge 190 · Kontrolleur stürzt bei Verfolgung: Die Verfolgerfälle (§ 823 I BGB) (Mo · Der Fall · Deliktsrecht,
Klassiker-Fall). Fall nach dem Plan-Hook („Ein Schwarzfahrer flüchtet, der Kontrolleur stürzt bei der Verfolgung die Treppe
hinunter“), U-Bahnhof fiktiv, ohne Verkehrsunternehmen und Logos: Kontrolleur Wendelin trifft im U-Bahnhof den Fahrgast
Anselm ohne gültigen Fahrschein und bittet um den Ausweis; Anselm läuft zur Treppe am Ausgang, Wendelin rennt hinterher, die
steile Treppe hinunter, zwei Stufen auf einmal, und stürzt (im Bild nur Treppen-Icon und Text „stürzt“). Arm gebrochen,
sechs Wochen Armschlinge. Wendelin verlangt Schadensersatz; Anselm: „Ich habe Sie nicht berührt.“
Vorbild ist der Verfolgerfall BGH, Urt. v. 13.7.1971 – VI ZR 125/70, BGHZ 57, 25 (Datum, Az. und Fundstelle gesichert über
BGH VI ZR 43/11 Rn. 8, 11 und IX ZR 149/15 Rn. 11; Inhalt nach nichtamtlichem Volltext, Kerngehalt über VI ZR 43/11 belegt).
Prüfung: Problem (psychisch vermittelte Kausalität) → § 823 Abs. 1 BGB (Wortlautkarte, Merkmale genannt; Schema nur Verweis
Folge 067) → Äquivalenz, wertende Zurechnung → Herausforderungsformel (VI ZR 43/11 Rn. 8, 11, 20) → Subsumtion (billigenswert,
Verhältnis, gesteigertes Risiko; Verschulden Rn. 9, 14) → Gegenbeispiel allgemeines Lebensrisiko (BGHZ 132, 164; BGHZ 57, 25)
und übersteigertes Risiko → § 254 Abs. 1 BGB (Wortlautkarte, vorgelesen; Verweis Folge 046) → Ergebnis → Ausblick Retter,
Strafrecht (je ein Satz), § 265a StGB (ein Satz) → Klausurtipp (Lexi) → Prüfschema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Wendelin, Anselm
(nie im Genitiv). Stimmen: Wendelin helmut, Anselm niklas. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Wendelin": "helmut", "Anselm": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Bahnsteig und Treppe --------------------------------------------------------------------------------------
    ("[fall]Im U-Bahnhof hält ein Zug. [kontr]Kontrolleur Wendelin prüft die Fahrscheine. [anselm]Der Fahrgast Anselm hat "
     "keinen gültigen Fahrschein dabei.", P),
    ("[w1]Dann brauche ich bitte Ihren Ausweis.", P, "Wendelin"),
    ("[flucht]Doch Anselm läuft los, zur Treppe am Ausgang. [verfolg]Wendelin rennt hinterher, die steile Treppe hinunter, "
     "zwei Stufen auf einmal. [sturz]Auf den Stufen stürzt er. [arm]Sein Arm ist gebrochen, sechs Wochen trägt er eine "
     "Armschlinge.", P),
    # --- A2 Fall: danach ---------------------------------------------------------------------------------------------------
    ("[w2]Für meinen gebrochenen Arm müssen Sie aufkommen.", P, "Wendelin"),
    ("[a1]Ich habe Sie doch gar nicht berührt. Sie sind selbst gestürzt!", P, "Anselm"),
    ("[frage]Muss Anselm für den Sturz haften? [klass]Ein Klassiker: Neunzehnhunderteinundsiebzig entschied der "
     "Bundesgerichtshof einen sehr ähnlichen Fall, den Verfolgerfall.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem und die Norm ------------------------------------------------------------------------------------------
    ("[problem]Das Problem: Anselm hat Wendelin weder gestoßen noch berührt. [selbst]Wendelin hat sich selbst entschieden, "
     "hinterherzulaufen. [psych]Der Weg zur Verletzung führt also über seinen eigenen Willensentschluss; man spricht von "
     "psychisch vermittelter Kausalität.", PS),
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertdreiundzwanzig Absatz eins BGB. [koerper]Der Körper von Wendelin ist "
     "verletzt, das ist klar. [kaus]Fraglich ist, ob Anselm ihn verletzt hat, also die haftungsbegründende Kausalität. "
     "[schema]Das ganze Prüfschema zeigt das Video zum Deliktsrecht.", PS),
    ("[aequ]Ursächlich im Sinne der Äquivalenz ist die Flucht: Ohne sie wäre Wendelin nicht gerannt. [wert]Doch tritt ein "
     "freier Entschluss des Verletzten dazwischen, genügt das allein nicht. [wert2]Dann braucht es eine wertende Zurechnung.", PS),
    # --- D Herausforderungsformel ------------------------------------------------------------------------------------------
    ("[formel]Dafür hat der Bundesgerichtshof eine Formel entwickelt. [h1]Wer einen anderen durch vorwerfbares Verhalten zu "
     "einer Verfolgung herausfordert, haftet für dessen Schaden, [h2]wenn sich der Verfolger herausgefordert fühlen durfte. "
     "[h3]Dafür braucht er ein mindestens im Ansatz billigenswertes Motiv. [h4]Die Risiken der Verfolgung dürfen nicht außer "
     "Verhältnis zu ihrem Zweck stehen. [h5]Und im Schaden muss sich gerade das gesteigerte Risiko der Verfolgung "
     "verwirklicht haben.", PS),
    # --- E Im Fall ----------------------------------------------------------------------------------------------------------
    ("[mot]Erstens: Wendelin wollte die Personalien feststellen, um den Anspruch des Verkehrsbetriebs zu sichern. "
     "[mot2]Das ist billigenswert. [verh]Zweitens: Eine Verfolgung zu Fuß über eine Treppe steht dazu nicht außer "
     "Verhältnis; so sah es auch der Bundesgerichtshof. [risk]Drittens: Wer eine steile Treppe in hohem Tempo hinabrennt, "
     "trägt ein deutlich erhöhtes Risiko, [risk2]und genau das hat sich im Sturz verwirklicht. [zur]Der Sturz ist Anselm "
     "also objektiv zuzurechnen.", PS),
    ("[versch]Und Anselm handelte fahrlässig: Er musste damit rechnen, verfolgt zu werden, [versch2]und dass sein Verfolger "
     "dabei zu Schaden kommen kann.", PS),
    # --- F Gegenbeispiele --------------------------------------------------------------------------------------------------
    ("[gegen]Anders liegt es beim normalen Risiko jedes Laufens. [gg1]Das gehört nach dem Bundesgerichtshof zum allgemeinen "
     "Lebensrisiko, und dafür haftet der Flüchtende nicht. [gg2]Knickt Wendelin also auf ebenem Boden einfach um, ohne dass "
     "die Verfolgung eine besondere Gefahr geschaffen hat, bekommt er von Anselm nichts. [gg3]Und wer sich gänzlich unangemessen in "
     "Gefahr bringt, etwa mit einem Sprung aus großer Höhe, durfte sich nicht mehr herausgefordert fühlen.", PS),
    # --- G Mitverschulden § 254 Abs. 1 BGB ---------------------------------------------------------------------------------
    ("[mit]Bleibt das Mitverschulden nach Paragraf zweihundertvierundfünfzig Absatz eins: [w254]Hat bei der Entstehung des "
     "Schadens ein Verschulden des Beschädigten mitgewirkt, so hängt die Verpflichtung zum Ersatz sowie der Umfang des zu "
     "leistenden Ersatzes von den Umständen, insbesondere davon ab, inwieweit der Schaden vorwiegend von dem einen oder dem "
     "anderen Teil verursacht worden ist.", P),
    ("[stufen]Zwei Stufen auf einmal: Das kann ein Mitverschulden von Wendelin sein, dann wird sein Anspruch gekürzt. "
     "[abw]Statt alles oder nichts wird also abgewogen. [orig]Im Originalfall bekam der Kontrolleur zwei Drittel seines "
     "Schadens ersetzt.", PS),
    # --- H Ergebnis und Ausblick -------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Anselm muss Wendelin den Schaden aus dem Sturz nach Paragraf achthundertdreiundzwanzig Absatz eins "
     "ersetzen, gekürzt um ein etwaiges Mitverschulden.", PS),
    ("[retter]Derselbe Gedanke trägt die Retterfälle: Bei Gefahr für Leib und Leben ist das Eingreifen eines Retters nach "
     "dem Bundesgerichtshof nahezu zwangsläufig herausgefordert. [straf]Auch das Strafrecht kennt solche Fälle, dort bei der "
     "objektiven Zurechnung. [fahrt]Und ob die Fahrt ohne Fahrschein als Erschleichen von Leistungen nach Paragraf "
     "zweihundertfünfundsechzig a StGB strafbar ist, ist eine eigene Frage.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Herausforderung prüfst du bei der haftungsbegründenden Kausalität, als objektive Zurechnung der "
     "Rechtsgutsverletzung. [tp2]Verneine sie nicht vorschnell mit dem Argument, der Verfolger sei freiwillig gerannt. "
     "[tp3]Das Verschulden prüfst du danach gesondert, das Mitverschulden erst beim Umfang des Ersatzes.", PS),
    # --- J Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für Verfolgerfälle im Rahmen von Paragraf achthundertdreiundzwanzig Absatz eins. [c1]Römisch "
     "eins: haftungsbegründende Kausalität, zuerst die Äquivalenz, [c2]dann die Herausforderung: billigenswertes Motiv, "
     "Risiko nicht außer Verhältnis zum Zweck, gesteigertes Verfolgungsrisiko verwirklicht. [c3]Römisch zwei: Verschulden, "
     "Verfolgung und Verletzung voraussehbar. [c4]Römisch drei: Mitverschulden nach Paragraf zweihundertvierundfünfzig.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer flieht, haftet für den Sturz seines Verfolgers, wenn er ihn vorwerfbar zur Verfolgung herausgefordert "
     "hat und sich gerade das gesteigerte Verfolgungsrisiko verwirklicht. [m2]Das allgemeine Lebensrisiko trägt der Verfolger selbst.",
     1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
