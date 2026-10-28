"""Folge 093 · Verpflichtungsklage Schema: Spruchreife und Bescheidungsurteil (Fr · Klausurpraxis ·
Verwaltungsprozessrecht, Format Schema). Übungsfall nach dem Hook des Themenplans („Die Stadt lehnt deinen Antrag auf
Außengastronomie vor deinem Café ab“), Beispielland Nordrhein-Westfalen – bewusst anders als Folge 074 (dort Ermessensausfall):
Herr Feldmann beantragt eine Sondernutzungserlaubnis für sechs Tische auf dem Gehweg vor seinem Café. Frau Siebert von der Stadt
lehnt ab, weil der Gehweg zu schmal sei und Fußgänger auf die Fahrbahn ausweichen müssten. Tatsächlich ist der Gehweg fünf
Meter breit; mit den Tischen bleiben drei Meter frei. Die Stadt hat also abgewogen, aber auf falscher Tatsachengrundlage.
A. Zulässigkeit: § 40 I 1 VwGO; § 42 I Alt. 2 (Wortlautkarte; Versagungsgegenklage, BVerwG 1 C 10.06 Rn. 16; Untätigkeitsklage
§ 75 ein Satz); § 42 II (möglicher Anspruch; BVerwG 4 C 3.20 Rn. 9; Anspruch auf fehlerfreie Bescheidung OVG NRW 11 A 114/20
Rn. 62); Vorverfahren § 68 II VwGO, § 110 I 2 JustG NRW; Frist § 74 II i. V. m. I 2; Klagegegner § 78 I Nr. 1.
B. Begründetheit § 113 V (Wortlautkarte), anspruchsorientiert; maßgeblicher Zeitpunkt (BVerwG 4 C 33.13 Rn. 18);
Anspruchsgrundlage § 18 I StrWG NRW (OVG NRW 11 A 2068/14 Rn. 49, 56); Ermessen (OVG NRW 11 A 114/20 Rn. 29, 58);
Ermessensfehler durch unzutreffende Sachverhaltsannahme (OVG NRW 11 A 2068/14 Rn. 57, 90); Spruchreife: Pflicht des
Gerichts zur Spruchreifmachung (BVerwG 1 C 18.17 Rn. 28, 36), Ermessensreduzierung auf null (BVerwG 1 B 16.13 Rn. 4);
Bescheidungsurteil § 113 V 2; Tenorformeln als Klausurkonvention.
Fiktive Figuren: Herr Feldmann (stephan), Frau Siebert (hilde), die Richterin (lucy). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Feldmann": "stephan", "Siebert": "hilde", "Richterin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Café, der Antrag, der Bescheid ---------------------------------------------------------------------
    ("[fall]Herr Feldmann führt ein Café an einer belebten Straße. [antrag]Für den Sommer beantragt er bei der Stadt, "
     "sechs Tische auf den Gehweg vor seinem Café zu stellen. [siebert]Frau Siebert von der Stadt bringt den Bescheid.", 0.2),
    ("[si1]Herr Feldmann, Ihr Gehweg ist zu schmal. Mit den Tischen müssten Fußgänger auf die Fahrbahn ausweichen. Das ist "
     "zu gefährlich, wir lehnen ab.", 0.3, "Siebert"),
    ("[fe1]Zu schmal? Der Gehweg ist fünf Meter breit. Da bleiben drei Meter frei!", 0.3, "Feldmann"),
    ("[klage]Drei Wochen später klagt Herr Feldmann beim Verwaltungsgericht und verlangt die Erlaubnis. [frage]Hat die "
     "Klage Erfolg? [frage2]Und bekommt er die Erlaubnis oder nur eine neue Entscheidung?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau, Rechtsweg ----------------------------------------------------------------------------------------------
    ("[aufbau]Die Verpflichtungsklage prüfst du in zwei Schritten: [aufbau2]A, Zulässigkeit, B, Begründetheit. "
     "[verweis1]Unser Beispiel spielt in Nordrhein-Westfalen. "
     "[rweg]Erstens, der Verwaltungsrechtsweg nach Paragraf vierzig: Die Sondernutzung regelt das "
     "Straßen- und Wegegesetz, also öffentliches Recht.", P),
    # --- D Statthaftigkeit, Wortlaut § 42 I Alt. 2 ------------------------------------------------------------------------
    ("[wl42]Zweitens, die statthafte Klageart. Paragraf zweiundvierzig Absatz eins, zweite Alternative: Durch Klage kann "
     "die Verurteilung zum Erlass eines abgelehnten oder unterlassenen Verwaltungsakts begehrt werden, die "
     "Verpflichtungsklage. [va]Die Stadt hat die Erlaubnis, einen Verwaltungsakt, abgelehnt: [vgk]die "
     "Versagungsgegenklage. Sie umfasst die Aufhebung des Ablehnungsbescheids. [untaet]Hätte die Stadt ohne zureichenden "
     "Grund nicht in angemessener Frist entschieden, wäre es eine Untätigkeitsklage nach Paragraf fünfundsiebzig.", P),
    # --- E Klagebefugnis ------------------------------------------------------------------------------------------------
    ("[kb]Drittens, die Klagebefugnis nach Absatz zwei. Hier muss es möglich sein, dass der Kläger einen Anspruch auf den "
     "Verwaltungsakt hat. [kb2]Bei Ermessen genügt ein möglicher Anspruch auf eine fehlerfreie Entscheidung. [kb3]Den kann "
     "Herr Feldmann aus dem Straßen- und Wegegesetz haben: klagebefugt.", P),
    # --- F Vorverfahren und Klagefrist ----------------------------------------------------------------------------------
    ("[vv]Viertens, das Vorverfahren. Nach Paragraf achtundsechzig Absatz zwei braucht auch die Verpflichtungsklage "
     "grundsätzlich einen Widerspruch. [nrw]In Nordrhein-Westfalen entfällt er nach Paragraf hundertzehn Justizgesetz, "
     "auch hier. [land]In deinem Land kann das anders sein. [frist]Fünftens, die Klagefrist: Nach Paragraf vierundsiebzig "
     "Absatz zwei gilt ein Monat ab Bekanntgabe der Ablehnung. [frist2]Herr Feldmann klagt nach drei Wochen, rechtzeitig.", P),
    # --- G Klagegegner ----------------------------------------------------------------------------------------------------
    ("[kg]Sechstens, der Klagegegner nach Paragraf achtundsiebzig: die Körperschaft, deren Behörde den Antrag abgelehnt "
     "hat, also die Stadt. [zul]Die Klage ist zulässig.", PS),
    # --- H Begründetheit, Wortlaut § 113 V ------------------------------------------------------------------------------
    ("[wl113]B, Begründetheit. Paragraf hundertdreizehn Absatz fünf: Soweit die Ablehnung oder Unterlassung des "
     "Verwaltungsakts rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, spricht das Gericht die "
     "Verpflichtung der Verwaltungsbehörde aus, die beantragte Amtshandlung vorzunehmen, wenn die Sache spruchreif ist. "
     "[satz2]Andernfalls spricht es die Verpflichtung aus, den Kläger unter Beachtung der Rechtsauffassung des Gerichts zu "
     "bescheiden.", P),
    ("[anspr]In der Klausur prüfst du das vom Anspruch her: Hat Herr Feldmann einen Anspruch auf die Erlaubnis? "
     "[zeit]Maßgeblich ist dafür in der Regel die Sach- und Rechtslage der letzten mündlichen Verhandlung. [zeit2]Das "
     "materielle Recht kann Abweichendes bestimmen.", P),
    # --- I Anspruchsprüfung -----------------------------------------------------------------------------------------------
    ("[agl]Erstens, die Anspruchsgrundlage: Paragraf achtzehn Straßen- und Wegegesetz, die Sondernutzungserlaubnis. "
     "[form]Zweitens, die formellen Voraussetzungen: Er hat den Antrag bei der zuständigen Stadt gestellt. [mat]Drittens, "
     "die materiellen Voraussetzungen: Sechs Tische auf dem Gehweg nutzen die Straße über den Gemeingebrauch hinaus, eine "
     "Sondernutzung. [rf]Viertens, die Rechtsfolge: gebunden oder Ermessen? Über die Erlaubnis entscheidet die Stadt nach "
     "Ermessen.", P),
    # --- J Ermessensfehler: falscher Sachverhalt ----------------------------------------------------------------------------
    ("[fehler]Dann hat Herr Feldmann grundsätzlich nur einen Anspruch auf eine fehlerfreie Entscheidung. [fehler2]Die Stadt "
     "hat zwar abgewogen, aber auf falscher Grundlage. [messen]Das Gericht stellt fest: Der Gehweg ist fünf Meter breit, "
     "drei Meter bleiben frei. [fehler3]Wer sein Ermessen auf einen falschen Sachverhalt stützt, entscheidet fehlerhaft. "
     "[rw]Die Ablehnung ist rechtswidrig und verletzt ihn in diesem Anspruch.", P),
    # --- K Spruchreife --------------------------------------------------------------------------------------------------
    ("[spruch]Bleibt die Spruchreife. Das Gericht muss die Sache grundsätzlich selbst spruchreif machen, also den "
     "Sachverhalt aufklären. [spruch2]Spruchreif ist sie, wenn feststeht, welche Entscheidung die Behörde treffen muss: "
     "bei einer gebundenen Entscheidung oder wenn das Ermessen auf null reduziert ist. [vu]Dann ergeht ein "
     "Verpflichtungsurteil nach Satz eins. [grenze]Das Ermessen selbst übt das Gericht aber nicht aus. [bu]Bleibt der "
     "Behörde ein Spielraum, ergeht ein Bescheidungsurteil nach Satz zwei.", P),
    ("[fall2]Im Fall bleibt der Stadt Raum für andere Gründe mit Bezug zur Straße, etwa das Stadtbild oder Lärm für die "
     "Anwohner. [null]Das Ermessen ist nicht auf null reduziert, [nsr]die Sache also nicht spruchreif. [erg]Herr Feldmann "
     "bekommt ein Bescheidungsurteil.", P),
    # --- L Tenor ----------------------------------------------------------------------------------------------------------
    ("[tenor]Zwei Tenorformeln für die Klausur. [tv]Verpflichtungsurteil: Die Beklagte wird unter Aufhebung des Bescheids "
     "verpflichtet, dem Kläger die beantragte Erlaubnis zu erteilen. [tb]Bescheidungsurteil: Die Beklagte wird unter "
     "Aufhebung des Bescheids verpflichtet, über den Antrag des Klägers unter Beachtung der Rechtsauffassung des Gerichts "
     "erneut zu entscheiden. [tim]Hat der Kläger die Erlaubnis verlangt, kommt hinzu: Im Übrigen wird die "
     "Klage abgewiesen.", P),
    # --- M Das Urteil -----------------------------------------------------------------------------------------------------
    ("[urteil]Die Richterin verkündet:", 0.2),
    ("[ri1]Die Stadt muss über den Antrag neu entscheiden, unter Beachtung der Rechtsauffassung des Gerichts. Im Übrigen "
     "wird die Klage abgewiesen.", 0.3, "Richterin"),
    ("[fe2]Immerhin. Diesmal mit den richtigen Zahlen.", PS, "Feldmann"),
    # --- N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schau dir den Antrag genau an. [tipp1]Hat die Behörde Ermessen, führt ein Ermessensfehler "
     "meist nur zum Bescheidungsurteil. [tipp2]Prüfe deshalb am Ende immer die Spruchreife und formuliere den Tenor passend.", PS),
    # --- O Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Verwaltungsrechtsweg, [s2]Statthaftigkeit, [s3]Klagebefugnis, "
     "[s4]Vorverfahren, [s5]Klagefrist, [s6]Klagegegner. "
     "[sb]B, Begründetheit: [sz]maßgeblicher Zeitpunkt, [s7]Anspruchsgrundlage, [s8]formelle und [s9]materielle "
     "Voraussetzungen, [s10]Rechtsfolge, [s11]und die Spruchreife: Verpflichtung oder Bescheidung.", PS),
    # --- P Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Spruchreif ist die Sache, wenn feststeht, was die Behörde tun muss. [m2]Dann verpflichtet das Gericht "
     "zum Erlass, sonst nur zur neuen Entscheidung.", 1.4),
]
