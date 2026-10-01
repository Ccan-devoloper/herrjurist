"""Folge 008 · Grundrechte Überblick: Freiheitsrechte, Gleichheitsrechte, Prüfung (Examenswissen, Format Schema).
Beispielfall (frei erfunden, länderneutral): Eine Stadt verbietet per Parksatzung Verkaufsfahrzeuge im Stadtpark; die
Eisverkäuferin Lina verliert ihren Standort, der feste Kiosk am Teich verkauft weiter. Prüfung: Welches Grundrecht passt?
A. Freiheitsrecht Art. 12 I GG (Schutzbereich – Eingriff – Rechtfertigung: Schranke, Verhältnismäßigkeit),
B. Gleichheitsrecht Art. 3 I GG (Ungleichbehandlung – Rechtfertigung), Gegenfall Eis-/Kaffeewagen.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Lina": "sabrina", "Tom": "niklas", "Kranz": "hilde", "Brenner": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Stadtpark -------------------------------------------------------------------------------------
    ("[fall]Sommer im Stadtpark. [lina]Lina verkauft hier seit Jahren Eis aus ihrem Wagen. Davon lebt sie. "
     "[tom]Dann kommt Tom vom Ordnungsamt.", 0.3),
    ("[t1]Die Stadt hat eine neue Parksatzung. Ab Montag dürfen Verkaufswagen nicht mehr in den Park fahren.", 0.4, "Tom"),
    # --- B Fall: der Grund ------------------------------------------------------------------------------------------
    ("[grund]Der Grund: Im letzten Sommer fuhren Verkaufswagen kreuz und quer über Wege und Wiesen. "
     "[spuren]Auf dem Rasen blieben tiefe Spuren, und Spaziergänger mussten ausweichen.", 0.3),
    ("[k1]Endlich! Ständig musste ich den Wagen ausweichen.", 0.4, "Kranz"),
    # --- C Fall: der Kiosk ------------------------------------------------------------------------------------------
    ("[kiosk]Der Kiosk am Teich darf weiter Eis verkaufen.", 0.3),
    ("[b1]Mein Kiosk fährt ja nirgendwohin.", 0.4, "Brenner"),
    ("[l1]Das ist mein Beruf! Und der Kiosk verkauft dasselbe Eis wie ich!", 0.5, "Lina"),
    ("[frage]Verletzt das Verbot Lina in ihren Grundrechten? An diesem Fall siehst du, wie du Freiheitsrechte und "
     "Gleichheitsrechte prüfst.", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Welches Grundrecht passt? ------------------------------------------------------------------------------
    ("[katalog]Zuerst: Welches Grundrecht passt? Die Artikel eins bis neunzehn schützen etwa Glauben, Meinung, Versammlung "
     "und Beruf. [frei]Das sind Freiheitsrechte. Sie wehren staatliche Eingriffe ab. [gleich]Daneben stehen die "
     "Gleichheitsrechte, vor allem Artikel drei. [bind]Gebunden sind Gesetzgebung, vollziehende Gewalt und "
     "Rechtsprechung, also auch die Stadt, Artikel eins Absatz drei.", P),
    ("[passt]Lina geht es um ihren Beruf, also um Artikel zwölf. Er ist spezieller als die allgemeine Handlungsfreiheit "
     "aus Artikel zwei Absatz eins. [passt2]Und weil der Kiosk anders behandelt wird, kommt Artikel drei hinzu.", PS),
    # --- F A. Art. 12: Schutzbereich ------------------------------------------------------------------------------
    ("[sb]Freiheitsrechte prüfst du in drei Schritten. Erstens der Schutzbereich. [sb_p]Persönlich: Artikel zwölf "
     "schützt nur Deutsche. Lina ist Deutsche. [ausl]Für Ausländer bliebe Artikel zwei Absatz eins. [gmbh]Und führte Lina "
     "ihr Geschäft als GmbH, könnte sich die GmbH über Artikel neunzehn Absatz drei auf die Berufsfreiheit berufen.", P),
    ("[sb_s]Sachlich: Beruf ist jede auf Dauer angelegte Tätigkeit, die der Schaffung und Aufrechterhaltung einer Lebensgrundlage "
     "dient. Lina lebt vom Eisverkauf.", PS),
    # --- G Eingriff -------------------------------------------------------------------------------------------------
    ("[ein]Zweitens der Eingriff. Die Satzung verbietet Lina, mit ihrem Wagen im Park zu verkaufen. Sie regelt also, wo sie ihren Beruf "
     "ausübt. Das ist ein Eingriff.", PS),
    # --- H Rechtfertigung: Schranke, Zweck, Eignung ---------------------------------------------------------------
    ("[rf]Drittens: Ist der Eingriff gerechtfertigt? [schranke]Die Berufsausübung darf durch Gesetz oder auf Grund eines "
     "Gesetzes geregelt werden, Artikel zwölf Absatz eins Satz zwei. [lr]Die Satzung stützt sich auf Landesrecht. Dass diese "
     "Grundlage trägt und die Satzung formell in Ordnung ist, unterstellen wir.", P),
    ("[vhm]Entscheidend ist die Schranken-Schranke, vor allem die Verhältnismäßigkeit. [zweck]Spaziergänger und Wiesen zu "
     "schützen, ist ein legitimer Zweck. [geeignet]Ohne Wagen im Park gibt es keine Spuren und weniger Gefahr. Das Verbot "
     "ist geeignet.", P),
    # --- I Erforderlichkeit, Angemessenheit -----------------------------------------------------------------------
    ("[erf]Erforderlich ist es, wenn kein milderes, gleich wirksames Mittel bereitsteht. Ein Fahrverbot nur für die Wiesen "
     "würde die Spaziergänger auf den Wegen nicht schützen.", P),
    ("[angem]Und angemessen? Das Verbot regelt nur, wo Lina verkauft, nicht ob. Sie darf ihren Beruf weiter ausüben, nur "
     "nicht im Park. Dem steht die Sicherheit vieler Spaziergänger gegenüber. [erg1]Der Eingriff ist gerechtfertigt, "
     "Artikel zwölf ist nicht verletzt.", PS),
    # --- J B. Art. 3 I --------------------------------------------------------------------------------------------
    ("[gl]Jetzt Artikel drei Absatz eins. Hier prüfst du nicht Schutzbereich und Eingriff, sondern zwei andere Schritte. "
     "[vgl]Erstens: Werden wesentlich Gleiche ungleich behandelt? Bilde Vergleichsgruppen. Lina und der Kiosk verkaufen "
     "beide Eis im Park. [ungl]Der Kiosk darf weiter verkaufen, Lina nicht. Das ist eine Ungleichbehandlung.", P),
    ("[rf3]Zweitens: Ist sie gerechtfertigt? Nötig ist ein Sachgrund, der Ziel und Ausmaß der Ungleichbehandlung "
     "angemessen ist. [mass]Der Maßstab reicht vom bloßen Willkürverbot bis zu strenger Verhältnismäßigkeit. Weil Linas "
     "Berufsfreiheit berührt ist, kann ein strengerer Maßstab gelten.", P),
    ("[sachgrund]Selbst dann hält die Unterscheidung: Der Kiosk steht fest an seinem Platz. Er fährt weder über Wege "
     "noch über Wiesen. Genau das will die Satzung verhindern. [erg2]Die Ungleichbehandlung ist gerechtfertigt.", PS),
    # --- K Ergebnis und Gegenfall ---------------------------------------------------------------------------------
    ("[ergebnis]Ergebnis: Das Verbot verletzt Lina weder in Artikel zwölf noch in Artikel drei. "
     "[gegen]Gegenfall: Die Satzung verbietet nur Eiswagen, Kaffeewagen dürfen weiter durch den Park fahren. "
     "[gegen2]Für Wege und Spaziergänger macht das keinen Unterschied. Findet sich kein anderer Sachgrund, ist Artikel "
     "drei verletzt.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst das speziellste Freiheitsrecht, danach Artikel drei. Artikel zwei Absatz eins "
     "brauchst du nur, wenn kein spezielleres Grundrecht passt. [tipp2]Oft steckt das alles in der Begründetheit einer "
     "Verfassungsbeschwerde. Die steht heute in Artikel vierundneunzig Absatz eins Nummer vier a. Ältere Bücher nennen "
     "noch Artikel dreiundneunzig.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sA]A, Freiheitsrecht. [sA1]Römisch eins: Schutzbereich, persönlich und sachlich. "
     "[sA2]Römisch zwei: Eingriff. [sA3]Römisch drei: verfassungsrechtliche Rechtfertigung, also Schranke und "
     "Schranken-Schranken, vor allem die Verhältnismäßigkeit.", P),
    ("[sB]B, Gleichheitsrecht. [sB1]Römisch eins: Ungleichbehandlung wesentlich Gleicher. [sB2]Römisch zwei: "
     "verfassungsrechtliche Rechtfertigung durch einen Sachgrund.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Freiheitsrechte fragen, ob der Staat so weit eingreifen darf. [m2]Gleichheitsrechte fragen, ob er "
     "ungleich behandeln darf.", 1.4),
]
