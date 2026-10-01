"""Folge 020 · Grundrechtsprüfung Schema: Schutzbereich, Eingriff, Rechtfertigung (Examenswissen, Format Schema).
Beispielfall (frei erfunden, länderneutral, Hook laut Themenplan): Eine Stadt verbietet per Verordnung das
Skateboardfahren in der Fußgängerzone von 8 bis 20 Uhr; die sechzigjährige Gudrun fährt dort jeden Morgen mit dem
Skateboard zur Arbeit. Geprüft wird das Freiheitsrecht Art. 2 I GG (allgemeine Handlungsfreiheit) im Dreischritt:
I. Schutzbereich (persönlich, sachlich), II. Eingriff (klassisch; moderner Eingriffsbegriff am Osho-Beschluss),
III. Rechtfertigung (1. Schranke verfassungsmäßige Ordnung, 2. Schranken-Schranken: formell inkl. Zitiergebot nur wo
einschlägig, Bestimmtheit, Verhältnismäßigkeit, Wesensgehalt Art. 19 II GG), Gegenfall Verbot rund um die Uhr.
Wortlautkarten: Art. 2 I GG, Art. 19 I 2 GG, Art. 19 II GG (vorgelesen). Fiktive Figuren: Gudrun (Skaterin),
Frau Krüger (Passantin), Herr Brückner (Ordnungsamt).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Gudrun": "lisa", "Krueger": "elinor", "Brueckner": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: in der Fußgängerzone ------------------------------------------------------------------------------
    ("[fall]Montagmorgen in der Fußgängerzone. [gudrun]Gudrun ist sechzig und fährt jeden Tag mit dem Skateboard "
     "zur Arbeit.", 0.3),
    # --- B Fall: beinahe ein Zusammenstoß -----------------------------------------------------------------------
    ("[mittag]Mittags ist es hier voll. Immer wieder rollen Skater knapp an Fußgängern vorbei. [krueger]Frau Krüger "
     "kann gerade noch ausweichen.", 0.2),
    ("[k1]Das war knapp! Hier gehen doch Kinder und alte Leute!", 0.4, "Krueger"),
    # --- C Fall: das Verbot ----------------------------------------------------------------------------------------
    ("[stadt]Die Stadt erlässt eine Verordnung. [brueckner]Herr Brückner vom Ordnungsamt hängt das neue Schild auf.", 0.2),
    ("[b1]Ab sofort ist Skateboardfahren hier von acht bis zwanzig Uhr verboten. Wer es trotzdem tut, zahlt ein "
     "Bußgeld.", 0.3, "Brueckner"),
    ("[g1]Skaten ist doch kein Verbrechen! Das ist meine Freiheit!", 0.4, "Gudrun"),
    ("[frage]Verletzt das Verbot Gudrun in ihren Grundrechten? An diesem Fall lernst du das Schema für Freiheitsrechte: "
     "Schutzbereich, Eingriff, Rechtfertigung.", 0.6),
    # --- D Sachverhalt ------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Vorfragen: Bindung, welches Grundrecht -----------------------------------------------------------------
    ("[bind]Zuerst: Die Stadt ist an die Grundrechte gebunden. Sie binden auch die vollziehende Gewalt, Artikel "
     "eins Absatz drei. [welches]Welches Grundrecht passt? Gudrun skatet weder beruflich, noch "
     "will sie demonstrieren. [auffang]Also bleibt Artikel zwei Absatz eins, die allgemeine Handlungsfreiheit. Sie "
     "greift, wo kein spezielleres Grundrecht schützt.", P),
    ("[wortlaut]Der Wortlaut: Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit, soweit er nicht die "
     "Rechte anderer verletzt und nicht gegen die verfassungsmäßige Ordnung oder das Sittengesetz verstößt.", PS),
    # --- F I. Schutzbereich ---------------------------------------------------------------------------------------
    ("[sb]Römisch eins: der Schutzbereich. [sb_p]Persönlich: Das Recht hat jeder, also auch Gudrun. [sb_s]Sachlich "
     "schützt Artikel zwei Absatz eins jede Form menschlichen Handelns, ganz gleich, welches Gewicht sie für die "
     "Persönlichkeit hat. [reiten]Das Bundesverfassungsgericht hat das sogar für das Reiten im Walde entschieden. "
     "[skaten]Also ist auch Skaten geschützt. Der Schutzbereich ist eröffnet.", PS),
    # --- G II. Eingriff -------------------------------------------------------------------------------------------
    ("[ein]Römisch zwei: der Eingriff. [klass]Der klassische Eingriff ist rechtsförmig, unmittelbar, gezielt und "
     "notfalls mit Zwang durchsetzbar, also ein Gebot oder Verbot. [verbot]Das Verbot mit Bußgeld erfüllt alle vier "
     "Merkmale.", P),
    ("[modern]Der Schutz reicht aber weiter. [osho]Im Osho-Beschluss maß das Bundesverfassungsgericht Äußerungen der "
     "Bundesregierung über eine religiöse Bewegung an Artikel vier, obwohl sie nichts verboten. [faktisch]Auch "
     "faktische und mittelbare Beeinträchtigungen zählen. Das ist der moderne Eingriffsbegriff. [hier]Hier brauchst du "
     "ihn nicht: Der klassische Eingriff liegt klar vor.", PS),
    # --- H III. 1. Schranke ---------------------------------------------------------------------------------------
    ("[rf]Römisch drei: die verfassungsrechtliche Rechtfertigung. [schranke]Erstens die Schranke. Artikel zwei Absatz "
     "eins steht unter dem Vorbehalt der verfassungsmäßigen Ordnung. [elfes]Dazu zählt jede Rechtsnorm, die formell "
     "und materiell verfassungsgemäß ist. [leicht]Die Schranke ist also leicht erreicht. Entscheidend ist, ob die "
     "Verordnung selbst verfassungsgemäß ist.", PS),
    # --- I III. 2. Schranken-Schranken: formell, Zitiergebot ------------------------------------------------------------
    ("[ss]Das prüfst du in den Schranken-Schranken. [formell]Formell geht es um Zuständigkeit, Verfahren und Form. Dass "
     "die Verordnung auf einem wirksamen Landesgesetz beruht und formell stimmt, unterstellen wir.", P),
    ("[zitier]Hierher gehört auch das Zitiergebot, Artikel neunzehn Absatz eins Satz zwei: Das Gesetz muss das "
     "Grundrecht unter Angabe des Artikels nennen. [nur]Das gilt aber nur, wo das Grundgesetz Einschränkungen durch "
     "Gesetz oder auf Grund eines Gesetzes ausdrücklich erlaubt, etwa beim Fernmeldegeheimnis. [nicht]Für die "
     "allgemeine Handlungsfreiheit gilt es nach dem Bundesverfassungsgericht nicht.", PS),
    # --- J III. 2. materiell: Bestimmtheit, Verhältnismäßigkeit ---------------------------------------------------------
    ("[best]Materiell zuerst die Bestimmtheit: Betroffene müssen die Rechtslage erkennen und ihr Verhalten danach "
     "ausrichten können. [klar]Skateboard, Fußgängerzone, acht bis zwanzig Uhr: Das ist klar.", P),
    ("[vhm]Kern ist die Verhältnismäßigkeit. [zweck]Der Zweck: Fußgänger vor Zusammenstößen schützen, also ihre "
     "Gesundheit. Das ist legitim. [geeignet]Geeignet ist das Verbot, wenn es den Zweck fördern kann. Die "
     "Möglichkeit genügt: Ohne Skater gibt es weniger Zusammenstöße.", P),
    ("[erf]Erforderlich ist es, wenn kein milderes, gleich wirksames Mittel bereitsteht. [schritt]Wie wäre eine "
     "Pflicht, nur im Schritttempo zu rollen? Das lässt sich kaum kontrollieren. Und dass eine Alternative gleich "
     "wirksam ist, muss eindeutig feststehen. [tag]Außerdem gilt das Verbot nur tagsüber, wenn es voll ist.", P),
    ("[angem]Angemessen ist es, wenn der Zweck nicht außer Verhältnis zur Schwere des Eingriffs steht. "
     "[last]Gudrun muss tagsüber absteigen und ihr Brett tragen. Abends und überall sonst darf sie fahren. "
     "[schutz]Dem steht die Gesundheit vieler Fußgänger gegenüber. Das Verbot ist angemessen.", P),
    # --- K Wesensgehalt, Ergebnis, Gegenfall --------------------------------------------------------------------------
    ("[wesen]Zuletzt Artikel neunzehn Absatz zwei: In keinem Falle darf ein Grundrecht in seinem Wesensgehalt "
     "angetastet werden. [wesen2]Ein Verbot nur in der Fußgängerzone und nur tagsüber lässt ihn unberührt. [erg]Ergebnis: Der "
     "Eingriff ist gerechtfertigt. Gudrun ist nicht in Artikel zwei Absatz eins verletzt.", PS),
    ("[gegen]Gegenfall: Die Stadt verbietet das Skaten rund um die Uhr, auch nachts, wenn die Fußgängerzone leer ist. "
     "[gegen2]Geht es ihr nur um die Fußgänger, wäre ein Verbot am Tag gleich wirksam und milder. [gegen3]Dann spricht "
     "viel dafür, dass das Verbot nicht erforderlich ist.", PS),
    # --- L Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der Dreischritt ist Klausurkonvention, kein Gesetzestext. Halte ihn trotzdem ein. "
     "[fehler]Typische Fehler: [f1]die Verhältnismäßigkeit vor der "
     "Schranke prüfen, [f2]das Zitiergebot bei jedem Grundrecht abhaken [f3]oder Artikel zwei Absatz eins prüfen, bevor "
     "du speziellere Grundrechte ausgeschlossen hast. [kurz]Was eindeutig ist, prüfst du kurz.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Römisch eins: Schutzbereich, persönlich und sachlich. [s2]Römisch zwei: Eingriff. "
     "[s3]Römisch drei: verfassungsrechtliche Rechtfertigung. [s31]Eins: Schranke. [s32]Zwei: Schranken-Schranken. "
     "[s32f]Formell, mit Zitiergebot, wo es gilt. [s32m]Materiell: Bestimmtheit, [s32v]Verhältnismäßigkeit mit "
     "legitimem Zweck, Eignung, Erforderlichkeit und Angemessenheit, [s32w]und Wesensgehalt.", PS),
    # --- N Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Schutzbereich und Eingriff sind oft schnell bejaht. [m2]Die eigentliche Arbeit steckt in den "
     "Schranken-Schranken, vor allem in der Verhältnismäßigkeit.", 1.4),
]
