"""Katzenkönig-Fall (BGHSt 35, 347, vereinfacht): Verbotsirrtum des Vordermanns, Täter hinter dem Täter.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede."""

P, PS = 0.4, 0.9

STIMMEN = {"Barbara": "laura_klar", "Peter": "stephan", "Richard": "niklas"}

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------------------------------
    ("[fall]Barbara und ihr Freund Peter haben großen Einfluss auf Richard. [glaeubig]Richard ist leichtgläubig und glaubt an übersinnliche Mächte.", P),
    ("[kk]Die beiden erzählen ihm vom Katzenkönig, einer uralten, bösen Macht.", 0.3),
    ("[b1]Der Katzenkönig verlangt ein Menschenopfer. Er will Nora.", 0.3, "Barbara"),
    ("[p1]Wenn du es nicht tust, sterben Millionen Menschen.", 0.4, "Peter"),
    ("[motiv]In Wahrheit will Barbara nur ihre Rivalin Nora loswerden.", 0.3),
    ("[r1]Aber töten ist doch Unrecht …", 0.3, "Richard"),
    ("[b2]Nicht, wenn du damit Millionen rettest!", 0.4, "Barbara"),
    ("[tat]Richard glaubt ihnen. Er geht in Noras Laden und sticht ihr von hinten mit einem Messer in den Rücken, während sie nichts ahnt. "
     "[ueberlebt]Nora überlebt schwer verletzt.", P),
    ("[frage]Wie haben sich Richard, Barbara und Peter strafbar gemacht?", 0.6),
    # --- Sachverhalt ------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- Richard -------------------------------------------------------------------------------------------------
    ("[r_sch]Beginne mit dem Tatnächsten, also mit Richard. [versuch]Nora hat überlebt. In Betracht kommt versuchter Mord. "
     "[tb]Richard wollte Nora töten und hat mit dem Messerstich unmittelbar angesetzt.", P),
    ("[heim]Er greift die arglose Nora von hinten an. Das ist heimtückisch.", PS),
    ("[rw]Gerechtfertigt ist die Tat nicht. [n34]Leben darf nicht gegen Leben abgewogen werden, und eine echte Gefahr gab es ohnehin nicht.", P),
    ("[schuld]In der Schuld prüfst du den entschuldigenden Notstand. [n35]Paragraf fünfunddreißig schützt aber nur bei Gefahren für einen selbst, "
     "Angehörige oder nahestehende Personen. Millionen Fremde gehören nicht dazu.", P),
    ("[irrt]Richard hielt die Tötung für erlaubt, um Millionen zu retten. Das ist ein Verbotsirrtum nach Paragraf siebzehn. "
     "[verm]Bei gehöriger Gewissensanspannung hätte er das Unrecht erkennen können. Der Irrtum war vermeidbar. "
     "[r_erg]Richard handelt schuldhaft und ist wegen versuchten Mordes strafbar. Die Strafe kann aber gemildert werden.", PS),
    # --- Barbara und Peter -------------------------------------------------------------------------------------------
    ("[hp]Jetzt Barbara und Peter. Sie haben selbst nicht zugestochen. [anst]Naheliegend wäre Anstiftung. "
     "[mt]Oder sind sie mittelbare Täter, obwohl Richard selbst voll strafbar ist?", P),
    ("[vp]Nach dem Verantwortungsprinzip ist das ausgeschlossen. [vp2]Wer einen voll verantwortlichen Menschen vorschiebt, ist nur Anstifter.", P),
    ("[bgh]Der BGH hat im Katzenkönig-Fall anders entschieden. [bgh1]Barbara und Peter haben Richards Irrtum bewusst hervorgerufen "
     "und für ihre Zwecke eingesetzt. [bgh2]Sie steuerten das Geschehen kraft überlegenen Wissens. Man spricht vom Täter hinter dem Täter.", P),
    ("[hp_erg]Barbara und Peter sind deshalb wegen versuchten Mordes in mittelbarer Täterschaft strafbar, "
     "Paragraf fünfundzwanzig Absatz eins, zweite Alternative.", PS),
    # --- Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Den Täter hinter dem Täter gibt es nur in wenigen Fallgruppen. [tipp2]Neben der Irrtumsherrschaft wie hier "
     "vor allem die Organisationsherrschaft, etwa bei Befehlen in staatlichen Machtapparaten.", PS),
    # --- Schema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Erstens: der Vordermann, hier versuchter Mord, mit Rechtswidrigkeit und Schuld, vor allem dem Verbotsirrtum. "
     "[k2]Zweitens: die Hintermänner. Mittelbare Täterschaft trotz voll verantwortlichem Werkzeug? [k3]Streit darstellen und dem BGH folgen.", PS),
    # --- Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Auch wer einen voll verantwortlichen Menschen lenkt, kann mittelbarer Täter sein. "
     "[m2]Entscheidend ist, ob er das Geschehen durch einen bewusst erzeugten Irrtum beherrscht.", 1.4),
]
