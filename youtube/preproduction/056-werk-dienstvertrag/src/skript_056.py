"""Folge 056 · Werkvertrag oder Dienstvertrag? Abgrenzung nach §§ 611, 631, 650 BGB (Mi · Examenswissen ·
Zivilrecht/Werkvertragsrecht, Format Abgrenzung). Beispielfall nach dem Plan-Hook („Der Nachhilfelehrer garantiert keine
Note – der Maler aber eine gestrichene Wand“): Mareike bucht bei Henrik zehn Stunden Nachhilfe (Dienstvertrag) und lässt
ihr Zimmer von der Malerin Frau Ostertag streichen (Werkvertrag); Gegenfall Regal vom Schreiner (§ 650 Abs. 1 BGB).
Kern: Wortlautkarten § 611 Abs. 1, § 631 Abs. 1 und 2, § 650 Abs. 1 Satz 1 BGB; Kriterium Erfolg oder Tätigkeit,
Auslegung (BGH III ZR 79/09 Rn. 16); Grenzfälle Arzt (§§ 630a, 630b; BGH III ZR 294/16 Rn. 15), Website/Software und
Wartung (III ZR 79/09 Rn. 21, 23); Werklieferung (X ZR 82/07 Rn. 8; VII ZR 243/17 Rn. 25, 29); Folgen: Abnahme § 640,
Fälligkeit § 641, Herstellungsanspruch vor Abnahme und Mängelrechte § 634 erst danach (VII ZR 301/13 Rn. 31 f.),
Dienstvertrag ohne Gewährleistung (III ZR 294/16 Rn. 16), § 280 Abs. 1; Vergütung §§ 612, 632; § 611a in einem Satz.
Figuren: Mareike (julia), Henrik (niklas), Frau Ostertag (ela_warm); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.7

STIMMEN = {"Mareike": "julia", "Henrik": "niklas", "Ostertag": "ela_warm"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Nachhilfe -------------------------------------------------------------------------------------------
    ("[fall]Mareike schreibt in sechs Wochen ihre Statistikklausur. [nh]Sie bucht bei Henrik zehn Stunden Nachhilfe, "
     "zu je dreißig Euro.", 0.3),
    ("[h1]Ich erkläre dir den Stoff. Bestehen musst du selbst.", 0.4, "Henrik"),
    # --- A2 Fall: die Malerin ---------------------------------------------------------------------------------------------
    ("[maler]Außerdem lässt Mareike ihr Zimmer streichen, von der Malerin Frau Ostertag.", 0.3),
    ("[o1]Bis Freitag ist die Wand weiß. Das macht vierhundert Euro.", 0.4, "Ostertag"),
    ("[streif]Am Freitag ist die Wand fleckig und voller Streifen.", 0.3),
    ("[m1]So nehme ich die Wand nicht ab. Bitte streichen Sie noch einmal!", 0.4, "Mareike"),
    # --- A3 Fall: die Klausur ---------------------------------------------------------------------------------------------
    ("[stunden]Henrik gibt alle zehn Stunden wie vereinbart. [durch]Trotzdem fällt Mareike durch.", 0.3),
    ("[m2]Ich bin durchgefallen. Dafür zahle ich nichts!", 0.4, "Mareike"),
    ("[frage]Muss Mareike für die Nachhilfe zahlen? [frage2]Und was kann sie von Frau Ostertag verlangen? "
     "[hook]Der Nachhilfelehrer garantiert keine Note, die Malerin aber eine gestrichene Wand.", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 611 I, § 631 I, II ----------------------------------------------------------------------------------
    ("[p611]Erst die beiden Vertragstypen. Paragraf sechshundertelf Absatz eins: Durch den Dienstvertrag wird derjenige, "
     "welcher Dienste zusagt, zur Leistung der versprochenen Dienste, der andere Teil zur Gewährung der vereinbarten "
     "Vergütung verpflichtet.", P),
    ("[p631]Paragraf sechshunderteinunddreißig Absatz eins: Durch den Werkvertrag wird der Unternehmer zur Herstellung des "
     "versprochenen Werkes, der Besteller zur Entrichtung der vereinbarten Vergütung verpflichtet. [p631b]Und nach Absatz "
     "zwei kann Gegenstand die Herstellung oder Veränderung einer Sache sein, [p631c]aber auch ein anderer durch Arbeit "
     "oder Dienstleistung herbeizuführender Erfolg.", PS),
    # --- D Kriterium ----------------------------------------------------------------------------------------------------
    ("[krit]Der Unterschied steckt im Wort Erfolg. [kd]Beim Dienstvertrag wird die Tätigkeit selbst geschuldet, "
     "[kw]beim Werkvertrag das Ergebnis. [ausl]Was geschuldet ist, ermittelst du durch Auslegung: [ausl2]aus dem Willen "
     "der Parteien, dem Vertragszweck und den Umständen. [hilf]Eine Hilfsfrage: Hat der Leistende den Erfolg überhaupt "
     "allein in der Hand?", P),
    # --- E Subsumtion ---------------------------------------------------------------------------------------------------
    ("[nhs]Henrik verspricht Unterricht. [nhs2]Ob Mareike besteht, hängt auch von ihr selbst ab, eine Note sagt er gerade "
     "nicht zu. [dv]Das ist ein Dienstvertrag. [mal]Frau Ostertag verspricht dagegen eine weiße Wand, also die Veränderung "
     "einer Sache. [wv]Ein Werkvertrag.", PS),
    # --- F Grenzfälle ---------------------------------------------------------------------------------------------------
    ("[grenz]Drei Grenzfälle. [arzt]Der Arzt schuldet eine Behandlung nach dem fachlichen Standard, aber keine Heilung. "
     "[arzt2]Auf den Behandlungsvertrag, Paragraf sechshundertdreißig a, ist deshalb nach Paragraf sechshundertdreißig b "
     "Dienstvertragsrecht anzuwenden.", P),
    ("[web]Wer für einen Kunden eine individuelle Website oder Software erstellt, schuldet nach dem Bundesgerichtshof "
     "dagegen regelmäßig ein Werk. [wart]Und bei der Wartung kommt es darauf an: Soll sie Störungen beseitigen und die "
     "Funktion erhalten, ist sie ein Werkvertrag. [wart2]Wird nur laufender Service als Tätigkeit geschuldet, liegt ein "
     "Dienstvertrag nahe.", PS),
    # --- G Werklieferungsvertrag § 650 ----------------------------------------------------------------------------------
    ("[wl]Und wenn eine Sache erst hergestellt und dann geliefert wird? [schr]Ein Schreiner baut Mareike in seiner "
     "Werkstatt ein Regal nach ihren Maßen und liefert es. [p650]Paragraf sechshundertfünfzig Absatz eins: Auf einen "
     "Vertrag, der die Lieferung herzustellender oder zu erzeugender beweglicher Sachen zum Gegenstand hat, finden die "
     "Vorschriften über den Kauf Anwendung.", P),
    ("[x82]Nach dem Bundesgerichtshof gilt das auch, wenn die Sache nach den Vorgaben des Kunden gebaut wird. "
     "[einb]Anders, wenn der Schwerpunkt auf dem Einbau und der Anpassung vor Ort liegt, etwa bei einem Lift, der an die "
     "Hausfassade angepasst wird. [einb2]Dann ist es ein Werkvertrag.", PS),
    # --- H Folgen Werkvertrag -------------------------------------------------------------------------------------------
    ("[folg]Warum ist die Einordnung so wichtig? Wegen der Folgen. [abn]Beim Werkvertrag muss der Besteller das "
     "vertragsmäßig hergestellte Werk abnehmen, Paragraf sechshundertvierzig. [faell]Erst bei der Abnahme ist die "
     "Vergütung zu entrichten, Paragraf sechshunderteinundvierzig.", P),
    ("[fleck]Flecken und Streifen auf der ganzen Wand sind kein unwesentlicher Mangel. [verw]Mareike darf die Abnahme "
     "also verweigern und muss noch nicht zahlen. [herst]Sie kann weiter verlangen, dass Frau Ostertag die Wand "
     "mangelfrei streicht. [m634]Nach der Abnahme hätte sie die Mängelrechte aus Paragraf sechshundertvierunddreißig: "
     "Nacherfüllung, Selbstvornahme, Rücktritt oder Minderung und Schadensersatz.", PS),
    # --- I Folgen Dienstvertrag -----------------------------------------------------------------------------------------
    ("[dfolg]Beim Dienstvertrag gibt es keine Abnahme und keine Mängelrechte. [bgh]Der Bundesgerichtshof sagt: Das "
     "Dienstvertragsrecht kennt keine Gewährleistung, die Vergütung wird bei schlechter Leistung grundsätzlich nicht "
     "gekürzt. [p280]Verletzt der Verpflichtete schuldhaft seine Pflichten, bleibt Schadensersatz nach Paragraf "
     "zweihundertachtzig Absatz eins. [hen]Henrik hat aber wie vereinbart unterrichtet. Dass Mareike durchfällt, ist "
     "keine Pflichtverletzung. [zahl]Sie muss die dreihundert Euro zahlen.", PS),
    # --- J Vergütung, Arbeitsvertrag ------------------------------------------------------------------------------------
    ("[verg]Übrigens: Ist über Geld nicht gesprochen worden, gilt eine Vergütung als stillschweigend vereinbart, wenn die "
     "Leistung den Umständen nach nur gegen Vergütung zu erwarten ist, [verg2]beim Dienstvertrag nach Paragraf "
     "sechshundertzwölf, beim Werkvertrag nach Paragraf sechshundertzweiunddreißig. [p611a]Und wer weisungsgebundene, "
     "fremdbestimmte Arbeit in persönlicher Abhängigkeit leistet, hat einen Arbeitsvertrag, Paragraf sechshundertelf a.", PS),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ordne den Vertrag gleich am Anfang ein, wenn du die Anspruchsgrundlage bestimmst. [tipp2]Frag "
     "nicht nach dem Etikett, sondern nach dem Inhalt: Tätigkeit oder Erfolg? [tipp3]Und prüfe beim Dienstvertrag nie "
     "die Mängelrechte aus Paragraf sechshundertvierunddreißig.", PS),
    # --- L Entscheidungsbaum --------------------------------------------------------------------------------------------
    ("[sch]Dein Entscheidungsbaum. [s1]Erste Frage: Ist ein Erfolg geschuldet? Das klärst du durch Auslegung. "
     "[s1n]Nein, nur eine Tätigkeit: Dienstvertrag, Paragraf sechshundertelf, ohne Mängelrechte, bei schuldhafter "
     "Pflichtverletzung Schadensersatz nach Paragraf zweihundertachtzig.", P),
    ("[s2]Ja: Dann die zweite Frage: Wird eine bewegliche Sache hergestellt und geliefert? [s2j]Ja: Paragraf "
     "sechshundertfünfzig, es gilt Kaufrecht. [s2n]Nein: Werkvertrag, Paragraf sechshunderteinunddreißig, mit Abnahme "
     "und Mängelrechten.", PS),
    # --- M Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nur sein Bemühen schuldet, schließt einen Dienstvertrag. [mk2]Wer einen Erfolg verspricht, einen "
     "Werkvertrag. [mk3]Und wird eine bewegliche Sache hergestellt und geliefert, gilt Kaufrecht.", 1.4),
]
