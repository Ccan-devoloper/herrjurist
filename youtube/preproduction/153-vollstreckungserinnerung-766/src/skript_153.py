"""Folge 153 · Vollstreckungserinnerung § 766 ZPO: Das Prüfschema (Fr · 2. Examen · ZV, Format Schema).
Übungsfall nach dem Hook des Themenplans: Die Konditorin Frau Bergmann hat gegen Herrn Mühlbauer ein vorläufig
vollstreckbares Urteil des Amtsgerichts über 900 Euro (Hochzeitstorte, § 708 Nr. 11 ZPO) und eine Ausfertigung mit
Vollstreckungsklausel. Der Gerichtsvollzieher pfändet in Herrn Mühlbauers Wohnung den Fernseher und klebt eine Siegelmarke
auf (§ 808 I, II 2 ZPO). Das Urteil ist Herrn Mühlbauer weder vorher noch bei der Pfändung zugestellt worden.
A. Zulässigkeit: 1. Statthaftigkeit (Wortlautkarte § 766 I 1; Vollstreckungsvoraussetzungen §§ 704 ff., BGH VII ZB 38/16
Rn. 37); Abgrenzung zu § 793 (Wortlautkarte; Maßnahme/Entscheidung, Anhörung: BGH V ZB 77/23 Rn. 13, VII ZB 18/18 Rn. 25,
§ 834 ZPO; § 11 I RPflG, BGH IX ZB 60/21 Rn. 34). 2. Zuständigkeit (§ 764 I, II, § 802 ZPO, § 20 I Nr. 17 RPflG).
3. Erinnerungsbefugnis (BGH I ZB 91/08 Rn. 9, VII ZB 22/12 Rn. 25; Gläubiger § 766 II; Dritte VII ZB 22/13 Rn. 19).
4. keine Frist, Rechtsschutzbedürfnis bis zur Beendigung der Maßnahme (BGH I ZB 66/16 Rn. 5).
B. Begründetheit: Wortlautkarte § 750 I 1 Nr. 2 a n. F.; Zweck rechtliches Gehör (BGH V ZB 42/13 Rn. 9); nur anfechtbar,
Heilung durch Nachholung (BGH V ZB 48/15 Rn. 9 f.); Zeitpunkt der Entscheidung (BGH VII ZB 18/18 Rn. 23).
Entscheidung durch Beschluss (§ 764 III), Tenor als üblich gekennzeichnet (BGH I ZB 66/16 Rn. 5), einstweilige Anordnung
(§ 766 I 2 i. V. m. § 732 II). Merktabelle § 766 / § 767 / § 771 (Verweis auf die Videos 054, 078, 096).
Klausurtipp (Lexi) → Prüfschema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Fiktive Figuren: Herr Mühlbauer (niklas), der Gerichtsvollzieher (helmut); Frau Bergmann spricht nicht.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.6

STIMMEN = {"Mühlbauer": "niklas", "Gerichtsvollzieher": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Torte und das Urteil ---------------------------------------------------------------------------
    ("[fall]Frau Bergmann führt eine Konditorei. [torte]Für die Hochzeit von Herrn Mühlbauer backt sie eine Torte, für "
     "neunhundert Euro. [zahlt]Er zahlt nicht. [urteil]Das Amtsgericht verurteilt ihn, das Urteil ist vorläufig "
     "vollstreckbar. [klausel]Frau Bergmann erhält eine Ausfertigung mit Vollstreckungsklausel [auftrag]und beauftragt "
     "den Gerichtsvollzieher.", 0.3),
    # --- B Fall: die Pfändung in der Wohnung ------------------------------------------------------------------------------
    ("[g1]Wegen der Forderung von Frau Bergmann pfände ich Ihren Fernseher.", 0.25, "Gerichtsvollzieher"),
    ("[siegel]Er klebt eine Siegelmarke auf das Gerät.", 0.25),
    ("[m1]Das Urteil wurde mir nie zugestellt!", 0.25, "Mühlbauer"),
    ("[g2]Die Gläubigerin hat eine vollstreckbare Ausfertigung. Das genügt mir.", 0.3, "Gerichtsvollzieher"),
    ("[zust]Tatsächlich wurde Herrn Mühlbauer das Urteil weder vorher noch bei der Pfändung zugestellt. [frage]Wie wehrt "
     "er sich? [frage2]Und wann wäre stattdessen die sofortige Beschwerde der richtige Weg?", 0.5),
    # --- C Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D A. Zulässigkeit, 1. Statthaftigkeit (Wortlaut § 766 I 1) -------------------------------------------------------
    ("[zul]A: Zulässigkeit. [statt]Erstens die Statthaftigkeit. [wl766]Nach Paragraf siebenhundertsechsundsechzig "
     "Absatz eins entscheidet das Vollstreckungsgericht über Einwendungen, welche die Art und Weise der "
     "Zwangsvollstreckung oder das vom Gerichtsvollzieher zu beobachtende Verfahren betreffen. [vor]Dazu gehören nach dem "
     "Bundesgerichtshof die Vollstreckungsvoraussetzungen, also auch die Zustellung. [statt_ok]Herr Mühlbauer rügt, wie "
     "der Gerichtsvollzieher vorgegangen ist. Die Erinnerung ist statthaft.", P),
    # --- E Abgrenzung zur sofortigen Beschwerde (Wortlaut § 793) ----------------------------------------------------------
    ("[a793]Abzugrenzen ist die sofortige Beschwerde. [wl793]Paragraf siebenhundertdreiundneunzig: Gegen Entscheidungen, "
     "die im Zwangsvollstreckungsverfahren ohne mündliche Verhandlung ergehen können, findet sofortige Beschwerde statt. "
     "[formel]Die Faustformel: Gegen Vollstreckungsmaßnahmen hilft die Erinnerung, gegen Entscheidungen die sofortige "
     "Beschwerde. [anh]Ob Erinnerung oder sofortige Beschwerde statthaft ist, hängt nach dem Bundesgerichtshof oft davon ab, "
     "ob das Vollstreckungsgericht vorher angehört hat. [pfueb]Ein Pfändungs- und Überweisungsbeschluss etwa ergeht ohne Anhörung des Schuldners, "
     "Paragraf achthundertvierunddreißig. Der Schuldner greift ihn deshalb mit der Erinnerung an. [rpfl]Entscheidet ein Rechtspfleger, ist "
     "nach Paragraf elf Absatz eins Rechtspflegergesetz das Rechtsmittel gegeben, das nach den allgemeinen Vorschriften "
     "zulässig ist, bei Vollstreckungsentscheidungen also die sofortige Beschwerde. [hier793]Bei Herrn Mühlbauer hat der Gerichtsvollzieher gepfändet. Eine "
     "Entscheidung liegt nicht vor.", P),
    # --- F 2. Zuständigkeit -----------------------------------------------------------------------------------------------
    ("[zust2]Zweitens die Zuständigkeit. Zuständig ist das Vollstreckungsgericht, also das Amtsgericht, in dessen Bezirk "
     "vollstreckt wird. [p802]Diese Zuständigkeit ist ausschließlich, Paragraf achthundertzwei. [richter]Und entscheiden "
     "muss der Richter, nicht der Rechtspfleger: Das behält ihm Paragraf zwanzig Absatz eins Nummer siebzehn Rechtspflegergesetz vor.", P),
    # --- G 3. Erinnerungsbefugnis -------------------------------------------------------------------------------------------
    ("[bef]Drittens die Erinnerungsbefugnis. Befugt ist, wer durch die Vollstreckung in eigenen Rechten betroffen ist. "
     "[bef_s]Meist ist das der Schuldner, [bef_g]aber auch der Gläubiger, etwa wenn sich der Gerichtsvollzieher weigert, "
     "einen Vollstreckungsauftrag zu übernehmen, Absatz zwei, [bef_d]und mitunter ein Dritter. [bef_ok]Gepfändet wurde Herrn Mühlbauers "
     "Fernseher. Er ist befugt.", P),
    # --- H 4. Frist und Rechtsschutzbedürfnis -------------------------------------------------------------------------------
    ("[frist]Viertens: Eine Frist hat die Erinnerung nicht. [rsb]Nötig ist aber ein Rechtsschutzbedürfnis. Es besteht, "
     "solange die beanstandete Maßnahme nicht beendet ist. [rsb_ok]Hier klebt das Siegel noch, der Fernseher ist nicht "
     "versteigert. Die Erinnerung ist zulässig.", PS),
    # --- I B. Begründetheit: § 750 I ------------------------------------------------------------------------------------------
    ("[begr]B: Begründetheit. Die Erinnerung ist begründet, wenn die Maßnahme gegen Vorschriften des Vollstreckungsverfahrens "
     "verstößt. [wl750]Hier Paragraf siebenhundertfünfzig Absatz eins: Die Zwangsvollstreckung darf nur beginnen, wenn dem "
     "Schuldner das Urteil zugestellt ist oder gleichzeitig zugestellt wird. [zweck]Die Zustellung dient seinem "
     "rechtlichen Gehör: Er soll die Grundlagen der Vollstreckung prüfen können. [verst]Ihm wurde das Urteil "
     "nicht zugestellt. Die Pfändung verstößt gegen Paragraf siebenhundertfünfzig. [anf]Unwirksam ist sie deshalb nicht: "
     "Nach dem Bundesgerichtshof macht die fehlende Zustellung sie nur anfechtbar. [begr_ok]Die Erinnerung ist begründet.", P),
    # --- J Zeitpunkt und Heilung ------------------------------------------------------------------------------------------------
    ("[zeit]Aber Achtung beim Zeitpunkt: Maßgeblich ist die Sach- und Rechtslage, wenn über die Erinnerung entschieden "
     "wird. [heil]Wird das Urteil vorher noch zugestellt, kann der Mangel geheilt werden. Dann wird die Erinnerung "
     "unbegründet.", PS),
    # --- K Entscheidung und Eilschutz ------------------------------------------------------------------------------------------
    ("[ent]Das Gericht entscheidet durch Beschluss. [tenor]Üblich ist etwa der Tenor: Die Pfändung des Fernsehers wird für "
     "unzulässig erklärt. [aufh]Der Gerichtsvollzieher hebt die Pfändung dann auf. [eil]Vor der Entscheidung kann das "
     "Gericht eine einstweilige Anordnung erlassen, etwa die Zwangsvollstreckung einstweilen einstellen, Paragraf siebenhundertsechsundsechzig Absatz eins Satz zwei "
     "mit Paragraf siebenhundertzweiunddreißig Absatz zwei.", PS),
    # --- L Merktabelle ------------------------------------------------------------------------------------------------------------
    ("[tab]Zur Abgrenzung je eine Zeile: [t766]Die Erinnerung rügt das Verfahren. [t767]Die Vollstreckungsabwehrklage, "
     "Paragraf siebenhundertsiebenundsechzig, bringt materielle Einwendungen gegen den titulierten Anspruch. [t771]Die "
     "Drittwiderspruchsklage, Paragraf siebenhunderteinundsiebzig, schützt ein die Veräußerung hinderndes Recht eines Dritten. "
     "[verw]Mehr dazu in unseren Videos zu diesen Klagen.", PS),
    # --- M Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag zuerst, wer gehandelt hat und wie. [tipp2]Als Faustregel: Gerichtsvollzieher, oder Gericht "
     "ohne Anhörung: Erinnerung. Gericht nach Anhörung: sofortige Beschwerde. [tipp3]Und prüfe in der Begründetheit, ob ein Mangel "
     "bis zur Entscheidung geheilt ist.", PS),
    # --- N Prüfschema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [sA]A: Zulässigkeit. [s1]Erstens Statthaftigkeit: eine Vollstreckungsmaßnahme, keine "
     "Entscheidung. [s2]Zweitens Zuständigkeit: das Vollstreckungsgericht, ausschließlich, durch den Richter. [s3]Drittens "
     "Erinnerungsbefugnis. [s4]Viertens keine Frist, aber ein Rechtsschutzbedürfnis bis zur Beendigung. [sB]B: "
     "Begründetheit: ein Verstoß gegen Verfahrensvorschriften, beurteilt im Zeitpunkt der Entscheidung.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ohne Zustellung, spätestens gleichzeitig, darf die Vollstreckung nicht beginnen. [m2]Wer rügt, wie "
     "vollstreckt wird, erhebt Erinnerung. Wer eine Entscheidung angreift, legt sofortige Beschwerde ein.", 1.4),
]
