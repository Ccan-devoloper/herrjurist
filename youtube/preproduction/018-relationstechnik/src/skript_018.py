"""Folge 018 · Relationstechnik: Kläger-, Beklagten- und Beweisstation erklärt (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall (frei erfunden): Herr Brenner verkauft und liefert Frau Lehmann für ihr Café einen Kühlschrank für
3.000 Euro und klagt auf den Kaufpreis. Frau Lehmann bestreitet Kauf und Lieferung nicht, behauptet aber, sie habe dem
Fahrer bar bezahlt; Brenner bestreitet das. Der Fahrer sagt als Zeuge aus, er habe kein Geld bekommen.
Stationen (Ausbildungs- und Klausurkonvention, kein Gesetz): I. Prozessstation (§ 23 Nr. 1 GVG, § 253 II Nr. 2 ZPO) →
II. Klägerstation (§ 433 II BGB) → III. Beklagtenstation (§ 138 II–IV ZPO, § 362 I BGB, § 214 I BGB; BGH IV ZR 158/24
Rn. 10, IV ZR 9/22 Rn. 12) → IV. Beweisstation (§ 286 ZPO, Beweislast) → V. Tenor (§§ 91, 709 ZPO); Urteil § 313 ZPO.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Brenner, Lehmann; Referendarin und
Fahrer ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Referendarin": "julia", "Brenner": "christian", "Lehmann": "sabrina", "Fahrer": "johann"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: die Akte -------------------------------------------------------------------------------------------
    ("[fall]Vor dir liegen vierzig Seiten Schriftsätze, eine ganze Zivilakte.", 0.3),
    ("[r1]Vierzig Seiten. Wo fange ich an?", 0.5, "Referendarin"),
    ("[akte]In der Akte: [brenner]Herr Brenner verkauft Frau Lehmann für ihr Café einen Kühlschrank für dreitausend "
     "Euro [liefer]und liefert ihn. [klage]Jetzt klagt er auf den Kaufpreis.", 0.3),
    ("[b1]Der Kühlschrank ist geliefert. Gezahlt hat sie nie!", 0.4, "Brenner"),
    ("[l1]Doch! Ich habe dem Fahrer bar bezahlt.", 0.5, "Lehmann"),
    ("[frage]Wer gewinnt? Die Antwort liefert die Relation. [trennt]Sie trennt Rechtsfragen von Tatsachenfragen.", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Die Stationen --------------------------------------------------------------------------------------------
    ("[stat]Die Relation prüft in Stationen: Prozess, Kläger, Beklagter, Beweis, Tenor. [konv]Diese Reihenfolge steht "
     "in keinem Gesetz. Sie ist Ausbildungs- und Klausurkonvention. [prinzip]Erst prüfst du das Recht mit unterstellten "
     "Tatsachen, erst am Ende den Beweis.", PS),
    # --- D I. Prozessstation ----------------------------------------------------------------------------------------
    ("[proz]Erste Station: die Prozessstation. Ist die Klage zulässig? [ag]Hier kurz: Das Amtsgericht ist bis "
     "zehntausend Euro sachlich zuständig, [antrag]und der Antrag auf dreitausend Euro ist bestimmt.", PS),
    # --- E II. Klägerstation ----------------------------------------------------------------------------------------
    ("[kl]Zweite Station: die Klägerstation. Unterstelle alles, was Herr Brenner vorträgt, als wahr. Trägt das seinen "
     "Antrag? [kv]Er trägt einen Kaufvertrag über den Kühlschrank zu dreitausend Euro vor. [anspr]Daraus folgt der Anspruch "
     "auf den Kaufpreis, Paragraf vierhundertdreiunddreißig Absatz zwei BGB. [schl]Die Klage ist schlüssig. [unschl]Fehlte eine nötige Tatsache, wäre sie unschlüssig. Ergänzt der Kläger nach einem Hinweis nichts, "
     "wird sie abgewiesen. Den Beklagten müsstest du dann gar nicht mehr prüfen.", PS),
    # --- F III. Beklagtenstation: Bestreiten ------------------------------------------------------------------------
    ("[bk]Dritte Station: die Beklagtenstation. Jetzt unterstellst du Frau Lehmanns Vortrag als wahr. Bringt er den "
     "Anspruch zu Fall? [zug]Kauf und Lieferung bestreitet sie nicht. Sie gelten als zugestanden, Paragraf "
     "hundertachtunddreißig Absatz drei ZPO. [nw]Auch mit Nichtwissen dürfte sie das nicht bestreiten. Es geht um ihre "
     "eigenen Handlungen und Wahrnehmungen, Absatz vier.", P),
    # --- G III. Beklagtenstation: Einwendung ------------------------------------------------------------------------
    ("[zahl]Erheblich ist aber die Barzahlung. Der Fahrer durfte kassieren. Hat sie ihn bezahlt, ist der Anspruch durch Erfüllung erloschen, Paragraf "
     "dreihundertzweiundsechzig BGB. [einw]Das ist eine Einwendung. Das Gericht beachtet sie, sobald die Tatsachen "
     "dazu vorgetragen sind. [einr]Eine Einrede wie die Verjährung muss die Partei dagegen erheben.", P),
    # --- H III. Gegenvortrag: substantiiertes Bestreiten ------------------------------------------------------------
    ("[best]Herr Brenner bestreitet die Zahlung. [p2]Jede Partei muss sich zu den Behauptungen des Gegners erklären, "
     "Paragraf hundertachtunddreißig Absatz zwei. [subst]Weil Frau Lehmann genau sagt, wann und wem sie gezahlt hat, "
     "genügt kein bloßes Nein. Er muss schildern, wie es aus seiner Sicht war, so der Bundesgerichtshof. [lief]Das tut "
     "er: Der Fahrer habe nur den Lieferschein unterschreiben lassen.", PS),
    # --- I IV. Beweisstation ----------------------------------------------------------------------------------------
    ("[bs]Vierte Station: die Beweisstation. Beweis braucht nur, was streitig und erheblich ist. [nur]Hier also allein "
     "die Barzahlung. [last]Wer muss sie beweisen? Grundregel: Jede Partei beweist die Tatsachen der Norm, die ihr nützt. "
     "Die Erfüllung nützt Frau Lehmann. [zeuge]Sie benennt den Fahrer als Zeugen.", 0.4),
    ("[f1]Geld habe ich nicht bekommen. Nur ihre Unterschrift.", 0.5, "Fahrer"),
    ("[wuerd]Das Gericht würdigt die Aussage nach freier Überzeugung, Paragraf zweihundertsechsundachtzig. [regel]An "
     "Beweisregeln ist es nur gebunden, wo das Gesetz sie anordnet. Auch einem Mitarbeiter des Klägers darf es glauben. [nl]Hier glaubt "
     "es dem Fahrer: Die Zahlung ist nicht bewiesen. [lastfolge]Und selbst wenn nur Zweifel blieben, ginge das zulasten von Frau Lehmann, denn sie trägt die Beweislast.", PS),
    # --- J V. Tenor -------------------------------------------------------------------------------------------------
    ("[ten]Letzte Station: der Tenor. Die Referendarin formuliert ihn.", 0.3),
    ("[t1]Die Beklagte wird verurteilt, an den Kläger dreitausend Euro zu zahlen.", 0.4, "Referendarin"),
    ("[neben]Dazu kommen die Entscheidungen über Kosten und vorläufige Vollstreckbarkeit. [urt]Und im Urteil? Dort "
     "steht die Relation nicht als Überschrift. [p313]Das Urteil gliedert nach Urteilsformel, Tatbestand und Entscheidungsgründen, "
     "Paragraf dreihundertdreizehn. [ugr]Die Gründe fassen die tragenden Erwägungen kurz zusammen, im Urteilsstil.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Erhebe nie Beweis über Unstreitiges. [tipp2]Und frage immer, wer die Beweislast trägt. "
     "Bestreiten hilft nur gegen Tatsachen, die der Gegner beweisen muss.", PS),
    # --- L Klausurschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [sI]Römisch eins: Prozessstation, die Zulässigkeit. [sII]Römisch zwei: Klägerstation, die "
     "Schlüssigkeit. [sIII]Römisch drei: Beklagtenstation, die Erheblichkeit, mit Bestreiten, Einwendungen und Einreden. "
     "[sIV]Römisch vier: Beweisstation, mit Beweislast und freier Beweiswürdigung. [sV]Römisch fünf: Tenor.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst prüfst du das Recht mit unterstellten Tatsachen. [m2]Bewiesen wird nur, was streitig und "
     "erheblich ist.", 1.4),
]
