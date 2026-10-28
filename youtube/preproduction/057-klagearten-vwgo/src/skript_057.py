"""Folge 057 · Klagearten VwGO: Welche Klage passt? Der komplette Überblick (Fr · Klausurpraxis · Verwaltungsprozessrecht).
Beispielfall (Übungsfall nach dem Hook des Themenplans „Bescheid aufheben, Genehmigung erzwingen, Äußerung stoppen,
Rechtslage klären – vier Ziele, vier Klagen“): Frau Behrens betreibt einen Bootsverleih am See. Frau Thiele vom Bauamt
ordnet per Bescheid an, dass der Steg wegmuss, und lehnt den Kiosk ab; Bürgermeister Harms schreibt auf der
Internetseite der Stadt, ihre Boote seien nicht sicher; Herr Lindemann vom Ordnungsamt meint, für die neuen Elektroboote
brauche sie eine Erlaubnis. Abwandlungen: Verbot für das Seefest-Wochenende, das sich nach Klageerhebung erledigt
(Fortsetzungsfeststellungsklage), Bebauungsplan ohne Kioske am Ufer (Normenkontrolle).
Ausgangspunkt Klagebegehren § 88 VwGO, Rechtsweg § 40 I (ein Satz), Anfechtungs- und Verpflichtungsklage § 42 I
(Versagungsgegen-, Untätigkeitsklage § 75), allgemeine Leistungsklage (vorausgesetzt in § 43 II, § 111 VwGO),
Feststellungsklage § 43 I, II, Fortsetzungsfeststellungsklage § 113 I 4, Normenkontrolle § 47 I, II, V;
Entscheidungsbaum als Klausurkonvention.
Wortlautkarten: § 88 (vorgelesen), § 42 I (vorgelesen), § 43 I (vorgelesen), § 43 II 1 (vorgelesen), § 113 I 4 (vorgelesen).
Fiktive Figuren: Frau Behrens (sabrina), Frau Thiele (laura_ruhig), Bürgermeister Harms (william), Herr Lindemann (marc).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Behrens": "sabrina", "Thiele": "laura_ruhig", "Harms": "william", "Lindemann": "marc"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: der Bootsverleih am See, Post vom Bauamt ---------------------------------------------------------------
    ("[fall]Frau Behrens vermietet Tretboote am See. [woche]Diese Woche geht alles schief. "
     "[thiele]Frau Thiele vom Bauamt bringt einen Bescheid.", 0.2),
    ("[th1]Frau Behrens, Ihr Steg muss bis Monatsende weg. Und den Kiosk genehmigen wir nicht.", 0.3, "Thiele"),
    ("[be1]Der Bescheid muss weg. Und die Genehmigung hole ich mir!", 0.3, "Behrens"),
    # --- B Fall: ein Satz auf der Internetseite --------------------------------------------------------------------------
    ("[netz]Abends steht auf der Internetseite der Stadt ein Satz von Bürgermeister Harms.", 0.2),
    ("[ha1]Die Boote von Frau Behrens sind nicht sicher.", 0.3, "Harms"),
    ("[be2]Das ist falsch. Das soll er lassen!", 0.3, "Behrens"),
    # --- C Fall: die Elektroboote ----------------------------------------------------------------------------------------
    ("[lindemann]Dann kommt Herr Lindemann vom Ordnungsamt.", 0.2),
    ("[li1]Für Ihre neuen Elektroboote brauchen Sie eine Erlaubnis.", 0.3, "Lindemann"),
    ("[be3]Brauche ich nicht. Ich will wissen, woran ich bin.", 0.3, "Behrens"),
    # --- D Die Frage ----------------------------------------------------------------------------------------------------
    ("[frage]Bescheid aufheben, Genehmigung erzwingen, Äußerung stoppen, Rechtslage klären. Vier Ziele, vier Klagen. "
     "[frage2]Welche passt wann? [frage3]Und was, wenn sich ein Verbot erledigt oder eine Satzung stört?", 0.6),
    # --- E Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Ausgangspunkt: Klagebegehren, Rechtsweg ---------------------------------------------------------------------------
    ("[wl88]Ausgangspunkt ist das Klagebegehren, Paragraf achtundachtzig: Das Gericht darf über das Klagebegehren nicht "
     "hinausgehen, ist aber an die Fassung der Anträge nicht gebunden. [ziel]Es zählt also, was Frau Behrens wirklich "
     "erreichen will. [rweg]Vorab muss der Verwaltungsrechtsweg offen sein, Paragraf vierzig: eine öffentlich-rechtliche "
     "Streitigkeit nichtverfassungsrechtlicher Art. Hier ist er offen.", P),
    # --- G Wortlaut § 42 I ------------------------------------------------------------------------------------------------
    ("[wl42]Paragraf zweiundvierzig Absatz eins: Durch Klage kann die Aufhebung eines Verwaltungsakts, Anfechtungsklage, "
     "sowie die Verurteilung zum Erlass eines abgelehnten oder unterlassenen Verwaltungsakts, Verpflichtungsklage, "
     "begehrt werden.", P),
    # --- H Anfechtungsklage: der Steg ------------------------------------------------------------------------------------
    ("[anf]Erstens, der Steg. Die Anordnung ist ein Verwaltungsakt, und Frau Behrens will ihn loswerden. [anf2]Das ist "
     "die Anfechtungsklage. [anf3]Hat sie Erfolg, hebt das Gericht den Bescheid selbst auf, Paragraf hundertdreizehn "
     "Absatz eins Satz eins. Deshalb heißt sie Gestaltungsklage.", P),
    # --- I Verpflichtungsklage: der Kiosk ------------------------------------------------------------------------------------
    ("[vpf]Zweitens, der Kiosk. Hier will sie keinen Bescheid loswerden, sondern einen bekommen: die Genehmigung. "
     "[vpf2]Das ist die Verpflichtungsklage, nach einer Ablehnung auch Versagungsgegenklage genannt. [untaet]Hätte das "
     "Bauamt ohne zureichenden Grund gar nicht entschieden, wäre es eine Untätigkeitsklage, Paragraf fünfundsiebzig, in der Regel frühestens drei "
     "Monate nach dem Antrag. [vpf3]Gewinnt sie, verpflichtet das Gericht die Behörde, "
     "Paragraf hundertdreizehn Absatz fünf.", P),
    # --- J allgemeine Leistungsklage: der Satz im Internet ----------------------------------------------------------------
    ("[leist]Drittens, der Satz auf der Internetseite. Er regelt nichts, ist also kein Verwaltungsakt, sondern schlichtes "
     "Verwaltungshandeln. [leist2]Hier hilft die allgemeine Leistungsklage, gerichtet auf Unterlassen. [leist3]Eigens "
     "geregelt ist sie nicht, die Verwaltungsgerichtsordnung setzt sie aber voraus, etwa in Paragraf dreiundvierzig "
     "Absatz zwei und Paragraf hundertelf. [leist4]Erfolg hat Frau Behrens, wenn der Satz rechtswidrig in ihre "
     "Berufsfreiheit eingreift und eine Wiederholung droht.", P),
    # --- K Feststellungsklage: die Elektroboote --------------------------------------------------------------------------
    ("[wl43]Viertens, die Elektroboote. Paragraf dreiundvierzig Absatz eins: Durch Klage kann die Feststellung des "
     "Bestehens oder Nichtbestehens eines Rechtsverhältnisses oder der Nichtigkeit eines Verwaltungsakts begehrt werden, wenn der Kläger ein berechtigtes Interesse "
     "an der baldigen Feststellung hat. [rv]Ein Rechtsverhältnis sind rechtliche Beziehungen aus einem konkreten Sachverhalt, nach "
     "denen jemand etwas tun muss, darf oder nicht zu tun braucht. [rv2]Hier: Braucht Frau "
     "Behrens für die Elektroboote eine Erlaubnis? Die Stadt hat sich festgelegt, und die Boote "
     "sollen bald fahren.", P),
    ("[wl432]Aber Absatz zwei: Die Feststellung kann nicht begehrt werden, soweit der Kläger seine Rechte durch "
     "Gestaltungs- oder Leistungsklage verfolgen kann oder hätte verfolgen können. [subs]Verbietet die Stadt ihr die Boote "
     "per Bescheid, muss sie ihn anfechten. [subs2]Solange es nur Streit und keinen Bescheid gibt, bleibt die "
     "Feststellungsklage.", P),
    # --- L Ergebnis Ausgangsfall -----------------------------------------------------------------------------------------
    ("[erg]Also: [e1]Steg, Anfechtung. [e2]Kiosk, Verpflichtung. [e3]Internetseite, Leistung. [e4]Elektroboote, "
     "Feststellung.", PS),
    # --- M Abwandlung 1: Seefest, erledigtes Verbot ----------------------------------------------------------------------
    ("[seefest]Erste Abwandlung. Vor dem Seefest ordnet Herr Lindemann an:", 0.2),
    ("[li2]Am Seefest-Wochenende vermieten Sie keine Boote!", 0.3, "Lindemann"),
    ("[klagt]Frau Behrens klagt, [vorbei]dann ist das Seefest vorbei. Das Verbot hat sich erledigt, aufheben lässt sich "
     "nichts mehr.", P),
    ("[wl113]Paragraf hundertdreizehn Absatz eins Satz vier: Hat sich der Verwaltungsakt vorher durch Zurücknahme oder "
     "anders erledigt, so spricht das Gericht auf Antrag durch Urteil aus, dass der Verwaltungsakt rechtswidrig gewesen "
     "ist, wenn der Kläger ein berechtigtes Interesse an dieser Feststellung hat. [ffk]Das ist die "
     "Fortsetzungsfeststellungsklage. [ffk2]Das berechtigte Interesse folgt hier aus der "
     "Wiederholungsgefahr: Das Seefest kommt jedes Jahr, dasselbe Verbot droht erneut.", P),
    # --- N Abwandlung 2: Bebauungsplan, Normenkontrolle -------------------------------------------------------------------
    ("[bplan]Zweite Abwandlung: Die Gemeinde beschließt einen Bebauungsplan. Am Ufer sind keine Kioske zulässig. "
     "[nk]Der Bebauungsplan ist eine Satzung nach dem Baugesetzbuch. Dagegen gibt es die Normenkontrolle, Paragraf "
     "siebenundvierzig Absatz eins Nummer eins. [nk2]Das ist ein Antrag beim Oberverwaltungsgericht, keine Klage. "
     "[nk3]Stellen kann ihn, wer geltend macht, in seinen Rechten verletzt zu sein, binnen eines Jahres nach der "
     "Bekanntmachung. [nk4]Andere Vorschriften unter dem Landesgesetz nur, wenn das Landesrecht es "
     "vorsieht, Nummer zwei. [nk5]Erklärt es den Plan für unwirksam, gilt das für alle.", P),
    # --- O Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die statthafte Klageart prüfst du in der Zulässigkeit, direkt nach dem Rechtsweg. [tipp1]Beginne "
     "mit dem Begehren und lege einen schiefen Antrag aus. [tipp2]Und ordne erst, dann prüfe weiter: Klagebefugnis, "
     "Vorverfahren und Frist hängen von der Klageart ab.", PS),
    # --- P Klausurschema: der Entscheidungsbaum -----------------------------------------------------------------------------
    ("[sch]Dein Klausurschema, der Entscheidungsbaum. Eine Klausurkonvention, keine Norm. [q0]Eins: das Begehren nach "
     "Paragraf achtundachtzig. [q1]Zwei: Geht es um einen Verwaltungsakt? [q2]Aufhebung: Anfechtungsklage. [q3]Erlass: "
     "Verpflichtungsklage. [q4]Schon erledigt: Fortsetzungsfeststellungsklage. [q5]Drei, kein Verwaltungsakt: [q6]Tun "
     "oder Unterlassen: allgemeine Leistungsklage. [q7]Klärung eines Rechtsverhältnisses: Feststellungsklage, nachrangig. "
     "[q8]Vier: Bebauungsplan oder, je nach Land, andere Satzung: Normenkontrolle.", PS),
    # --- Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst das Ziel, dann die Klage. [m2]Gibt es einen Verwaltungsakt: Anfechtung, "
     "Verpflichtung oder Fortsetzungsfeststellung. Sonst: Leistung, Feststellung oder Normenkontrolle.", 1.4),
]
