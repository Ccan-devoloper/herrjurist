"""Folge 103 · Einwendung und Einrede: Warum Verjährung den Anspruch nicht tötet (Mo · Der Fall · Zivilrecht/Grundlagen &
Methodik, Format Schema). Beispielfall nach dem Plan-Hook („Die Handwerkerrechnung ist vier Jahre alt – musst du trotzdem
noch zahlen?“): Der Tischler Herr Grünwald restauriert im Herbst 2022 den alten Esstisch von Tilda (31); im Oktober 2022 holt
sie ihn zufrieden ab (Abnahme) und erhält die Rechnung über 1.400 €, die in einer Schublade landet. Im September 2026
spricht Herr Grünwald sie auf die offene Rechnung an. Keine Klage, kein Mahnbescheid, keine Verhandlungen, keine Zahlung.
Kern: Dreischritt entstanden – untergegangen – durchsetzbar als Treppe; rechtshindernde Einwendungen (§§ 105, 125, 134, 138
BGB; Schwarzarbeit BGH VII ZR 6/13 Rn. 13), rechtsvernichtende Einwendungen (§§ 362 I, 389, 142 I BGB), rechtshemmende
Einreden: dauernd § 214 I (Wortlautkarte; Fristrechnung §§ 195, 199 I, § 641 I nur angedeutet), aufschiebend §§ 320, 273
(Zug um Zug §§ 274 I, 322 I); Wirkung: Einwendungen von Amts wegen, Einreden nur auf Einrede (BGH XII ZB 104/22 Rn. 16,
V ZR 273/16 Rn. 27); § 214 II (Wortlautkarte) mit § 813 I 2; Ergebnis; Klausurtipp mit § 215 (Wortlaut); Schema; Merksatz.
Figuren: Tilda (lucy), Herr Grünwald (stephan); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Tilda": "lucy", "Grünwald": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Werkstatt, Herbst 2022 -------------------------------------------------------------------------
    ("[fall]Herbst zweitausendzweiundzwanzig. Tilda bringt den alten Esstisch ihrer Oma zum Tischler, Herrn Grünwald. "
     "[rest]Er schleift ihn ab, leimt die Beine neu und ölt das Holz. [abh]Im Oktober holt Tilda den Tisch ab und ist "
     "zufrieden.", 0.3),
    ("[gr1]Schön geworden, oder? Hier ist die Rechnung: tausendvierhundert Euro.", 0.3, "Grünwald"),
    ("[schub]Tilda legt die Rechnung in eine Schublade. Und vergisst sie.", 0.5),
    # --- A2 Fall: September 2026 -------------------------------------------------------------------------------------
    ("[sept]Fast vier Jahre später, im September zweitausendsechsundzwanzig, findet Herr Grünwald die offene Rechnung "
     "und kommt bei Tilda vorbei.", 0.3),
    ("[gr2]Sie schulden mir noch tausendvierhundert Euro für den Tisch!", 0.3, "Grünwald"),
    ("[ti1]Die Rechnung ist fast vier Jahre alt. Muss ich die wirklich noch zahlen?", 0.4, "Tilda"),
    ("[frage]Muss Tilda zahlen? [frage2]Und kann sie das Geld zurückverlangen, wenn sie erst zahlt und dann von der "
     "Verjährung erfährt?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Dreischritt (Treppe) --------------------------------------------------------------------------------------
    ("[drei]Gegen einen Anspruch kann sich der Schuldner auf drei Stufen wehren. [st1]Ist der Anspruch entstanden? "
     "[st2]Ist er untergegangen? [st3]Und ist er durchsetzbar? [stufe]Zu jeder Stufe gehören eigene Gegenrechte: "
     "[e1]rechtshindernde Einwendungen, [e2]rechtsvernichtende Einwendungen [e3]und rechtshemmende Einreden.", PS),
    # --- D I. entstanden: rechtshindernde Einwendungen -----------------------------------------------------------------
    ("[i]Erste Stufe: entstanden. Rechtshindernde Einwendungen lassen den Anspruch gar nicht erst entstehen. "
     "[h105]Etwa die Willenserklärung eines Geschäftsunfähigen, Paragraf hundertfünf. [h125]Ein Grundstückskauf ohne "
     "Notar, Paragraf hundertfünfundzwanzig. [h134]Ein Werkvertrag über Schwarzarbeit, Paragraf hundertvierunddreißig. "
     "[h138]Oder ein Wuchergeschäft, Paragraf hundertachtunddreißig.", P),
    ("[isub]Hier ist Tilda volljährig, der Vertrag braucht keine Form, und Herr Grünwald rechnet ordentlich ab. "
     "[iok]Der Anspruch auf Werklohn aus Paragraf sechshunderteinunddreißig ist entstanden.", PS),
    # --- E II. untergegangen: rechtsvernichtende Einwendungen ---------------------------------------------------------
    ("[ii]Zweite Stufe: untergegangen. Rechtsvernichtende Einwendungen lassen einen entstandenen Anspruch erlöschen. "
     "[v362]Vor allem die Erfüllung, Paragraf dreihundertzweiundsechzig. [v389]Die Aufrechnung, Paragraf "
     "dreihundertneunundachtzig. [v142]Und die Anfechtung: Sie vernichtet das Geschäft nach Paragraf "
     "hundertzweiundvierzig rückwirkend.", P),
    ("[iisub]Tilda hat nichts gezahlt, nicht aufgerechnet und nicht angefochten. [iiok]Der Anspruch besteht also noch.", PS),
    # --- F1 III. durchsetzbar: Verjährung § 214 Abs. 1 (Wortlaut) -------------------------------------------------------
    ("[iii]Dritte Stufe: durchsetzbar. Rechtshemmende Einreden lassen den Anspruch bestehen. Sie geben dem Schuldner nur "
     "das Recht, die Leistung zu verweigern. [dauer]Die wichtigste dauernde Einrede ist die Verjährung. [p214]Paragraf "
     "zweihundertvierzehn Absatz eins: Nach Eintritt der Verjährung ist der Schuldner berechtigt, die Leistung zu "
     "verweigern.", P),
    ("[frist]Die regelmäßige Frist beträgt drei Jahre. Sie beginnt mit dem Schluss des Jahres, in dem der Anspruch "
     "entstanden ist und der Gläubiger davon weiß oder grob fahrlässig nicht weiß. [rech]Fällig wurde der Werklohn mit der Abnahme im Oktober "
     "zweitausendzweiundzwanzig. Die Frist lief also vom Jahresende zweitausendzweiundzwanzig bis zum Ablauf des "
     "einunddreißigsten Dezember zweitausendfünfundzwanzig. [hemm]Gehemmt war sie nicht: Die beiden haben nie verhandelt, "
     "und Herr Grünwald hat weder geklagt noch einen Mahnbescheid beantragt.", PS),
    # --- F2 aufschiebende Einreden -----------------------------------------------------------------------------------
    ("[aufsch]Daneben gibt es aufschiebende Einreden. [p320]Beim gegenseitigen Vertrag darf man seine Leistung "
     "verweigern, bis die Gegenleistung bewirkt ist, außer man muss vorleisten, Paragraf dreihundertzwanzig. [p273]Ein Zurückbehaltungsrecht hat "
     "auch, wer aus demselben rechtlichen Verhältnis einen fälligen Gegenanspruch hat, Paragraf zweihundertdreiundsiebzig. "
     "[zug]Im Prozess führen beide nur zur Verurteilung Zug um Zug. [nicht]Für Tilda passt keine: Der Tisch ist fertig, "
     "und einen Gegenanspruch hat sie nicht.", PS),
    # --- G Wirkung im Prozess ----------------------------------------------------------------------------------------
    ("[amt]Jetzt der Unterschied in der Wirkung. Einwendungen beachtet das Gericht von Amts wegen, sobald die Tatsachen "
     "vorgetragen sind. [einr]Einreden wirken nur, wenn sich der Schuldner darauf beruft. [beruf]Erhebt Tilda die "
     "Einrede nicht, muss sie zahlen.", PS),
    # --- H § 214 Abs. 2 (Wortlaut): Der Anspruch lebt -----------------------------------------------------------------
    ("[tot]Und deshalb tötet die Verjährung den Anspruch nicht. [p214b]Paragraf zweihundertvierzehn Absatz zwei: Das zur "
     "Befriedigung eines verjährten Anspruchs Geleistete kann nicht zurückgefordert werden, auch wenn in Unkenntnis der "
     "Verjährung geleistet worden ist. [p813]Paragraf achthundertdreizehn erlaubt die Rückforderung bei dauernden "
     "Einreden zwar grundsätzlich, nimmt aber genau diesen Fall aus.", PS),
    # --- I Ergebnis --------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Herr Grünwald hat einen Anspruch auf tausendvierhundert Euro. Er ist entstanden und nicht "
     "untergegangen. [erg2]Aber er ist verjährt: Beruft sich Tilda darauf, muss sie nicht zahlen. [erg3]Zahlt sie "
     "trotzdem, ist das Geld weg, auch wenn sie von der Verjährung nichts wusste.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Verjährung prüfst du nie beim Untergang, sondern bei der Durchsetzbarkeit. [tipp2]Und "
     "Vorsicht bei der Aufrechnung. Nach Paragraf zweihundertfünfzehn schließt die Verjährung die Aufrechnung nicht aus, "
     "wenn der Anspruch in dem Zeitpunkt noch nicht verjährt war, in dem erstmals aufgerechnet werden konnte.", PS),
    # --- K Klausurschema (Treppe) ------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Anspruch aus Paragraf sechshunderteinunddreißig. [k1]Römisch eins: Anspruch "
     "entstanden. Hier stehen die rechtshindernden Einwendungen, etwa die Nichtigkeit. [k2]Römisch zwei: Anspruch "
     "untergegangen, durch rechtsvernichtende Einwendungen wie Erfüllung, Aufrechnung und Anfechtung. [k3]Römisch drei: "
     "Anspruch durchsetzbar. Hier prüfst du die Einreden, [k3a]dauernd wie die Verjährung, [k3b]aufschiebend wie die "
     "Paragrafen dreihundertzwanzig und zweihundertdreiundsiebzig. [k4]Römisch vier: Ergebnis.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Einwendungen hindern oder vernichten den Anspruch, und das Gericht beachtet sie von selbst. "
     "[mk2]Einreden lassen ihn bestehen und wirken nur, wenn der Schuldner sie erhebt. [mk3]Darum tötet die Verjährung "
     "den Anspruch nicht: Wer zahlt, bekommt nichts zurück.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
