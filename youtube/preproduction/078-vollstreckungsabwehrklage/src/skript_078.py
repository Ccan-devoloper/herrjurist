"""Folge 078 · Vollstreckungsabwehrklage § 767 ZPO – Prüfung im 2. Examen (Fr · 2. Examen · ZV, Format Schema).
Fall nach dem Plan-Hook: Tischlermeister Rademacher baut Herrn Neubauer einen Einbauschrank für 3.600 Euro; Neubauer zahlt
nicht. Das Amtsgericht verhandelt am 4. März 2026 und verurteilt ihn am 18. März 2026 zur Zahlung; das Urteil wird
rechtskräftig. Am 4. Mai 2026 überweist Neubauer den vollen Betrag (Überweisungsbeleg seiner Bank). Trotzdem beauftragt
Rademacher die Gerichtsvollzieherin. Neubauer geht zu Rechtsanwältin Kellermann (Anwaltsklausur aus Schuldnersicht).
Aufbau, anknüpfend an Folge 054 (Rechtsbehelfe in der ZV): A. Zulässigkeit (Statthaftigkeit mit Wortlautkarte § 767 I,
Abgrenzung §§ 766, 771 je ein Satz; Zuständigkeit § 767 I, § 802; Rechtsschutzbedürfnis BGH I ZR 180/21 Rn. 11)
→ B. Begründetheit (Erfüllung § 362 BGB; Präklusion mit Wortlautkarte § 767 II; Aufrechnung BGH II ZR 170/17 Rn. 11 f.;
§ 767 III) → Tenor als Klausurkonvention → Eilrechtsschutz (§ 769 mit Glaubhaftmachung, § 775 Nr. 2; Wortlautkarte
§ 775 Nr. 5, Nr. 4, § 776; § 770) → Klausurtipp → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Rademacher, Neubauer, Kellermann;
die Gerichtsvollzieherin bleibt ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Rademacher": "william", "Neubauer": "marc", "Kellermann": "laura_ruhig", "Gerichtsvollzieherin": "sabrina"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: in der Tischlerei, Urteil, Überweisung --------------------------------------------------------------------------
    ("[fall]Herr Rademacher ist Tischlermeister. [schrank]Für Herrn Neubauer baut er einen Einbauschrank, für "
     "dreitausendsechshundert Euro. [zahlt]Herr Neubauer zahlt nicht. [klage]Er klagt vor dem Amtsgericht. "
     "[mv]Am vierten März wird mündlich verhandelt, [urteil]am achtzehnten März verurteilt das Gericht Herrn Neubauer zur "
     "Zahlung. Das Urteil wird rechtskräftig. [ueberw]Am vierten Mai überweist Herr Neubauer den vollen Betrag. "
     "[beleg]Seine Bank bestätigt die Überweisung mit einem Beleg.", 0.3),
    # --- B Fall: an der Wohnungstür ------------------------------------------------------------------------------------------------
    ("[tuer]Trotzdem beauftragt Herr Rademacher die Gerichtsvollzieherin. Im Juni klingelt sie bei Herrn Neubauer.", 0.3),
    ("[g1]Ich vollstrecke im Auftrag von Herrn Rademacher aus dem Urteil des Amtsgerichts.", 0.4, "Gerichtsvollzieherin"),
    ("[n1]Aber ich habe doch längst alles überwiesen!", 0.5, "Neubauer"),
    # --- C Fall: in der Kanzlei ----------------------------------------------------------------------------------------------------
    ("[kanzlei]Am nächsten Tag sitzt Herr Neubauer bei Rechtsanwältin Kellermann.", 0.3),
    ("[n2]Wie halte ich die Vollstreckung auf, und zwar endgültig?", 0.4, "Neubauer"),
    ("[k1]Wir erheben Vollstreckungsabwehrklage. Und bis zum Urteil sichern wir Sie mit einem Eilantrag ab.", 0.5, "Kellermann"),
    ("[frage]Wie prüfst du diese Klage in der Anwaltsklausur? [frage2]Und wie stoppt Herr Neubauer die Vollstreckung, "
     "bis das Gericht entscheidet?", 0.6),
    # --- D Sachverhalt -------------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E A. Zulässigkeit: Statthaftigkeit ----------------------------------------------------------------------------------------
    ("[zul]A: Zulässigkeit. [statt]Erstens die Statthaftigkeit. [wl767]Paragraf siebenhundertsiebenundsechzig Absatz eins: "
     "Einwendungen, die den durch das Urteil festgestellten Anspruch selbst betreffen, sind von dem Schuldner im Wege der "
     "Klage bei dem Prozessgericht des ersten Rechtszuges geltend zu machen. [erfE]Herr Neubauer wendet Erfüllung ein, also "
     "eine materielle Einwendung gegen den titulierten Anspruch. Die Klage ist statthaft. [a766]Rügt jemand nur die Art und "
     "Weise der Vollstreckung, ist die Erinnerung nach Paragraf siebenhundertsechsundsechzig statthaft. [a771]Beruft sich ein "
     "Dritter auf ein Recht am Gegenstand, die Drittwiderspruchsklage nach Paragraf siebenhunderteinundsiebzig. [verw]Die "
     "Abgrenzung im Einzelnen zeigt unser Video zu den Rechtsbehelfen in der Zwangsvollstreckung.", PS),
    # --- F Zuständigkeit und Rechtsschutzbedürfnis -----------------------------------------------------------------------------------
    ("[zust]Zweitens die Zuständigkeit. Zuständig ist das Prozessgericht des ersten Rechtszuges, [ag]hier das Amtsgericht, "
     "das Herrn Neubauer verurteilt hat. [p802]Diese Zuständigkeit ist ausschließlich, Paragraf achthundertzwei. "
     "[rsb]Drittens das Rechtsschutzbedürfnis. [rsb2]Nach dem Bundesgerichtshof hängt es nicht davon ab, dass Vollstreckung "
     "droht. Es besteht grundsätzlich, solange der Gläubiger den Titel noch in Händen hat. [rsb3]Herr Rademacher hat "
     "das Urteil noch. Die Klage ist zulässig.", PS),
    # --- G B. Begründetheit: Einwendung und Präklusion -------------------------------------------------------------------------------
    ("[begr]B: Begründetheit. Die Klage ist begründet, wenn dem titulierten Anspruch eine Einwendung entgegensteht, die "
     "nicht ausgeschlossen ist. [erf]Das Geld ist auf dem Konto von Herrn Rademacher angekommen. Damit ist die Schuld "
     "erloschen, Paragraf dreihundertzweiundsechzig BGB. [prae]Jetzt die Präklusion. [wl767b]Nach Absatz zwei sind "
     "Einwendungen nur zulässig, soweit ihre Gründe erst nach dem Schluss der mündlichen Verhandlung entstanden sind. "
     "[prae2]Maßgeblich ist hier der vierte März. [prae3]Herr Neubauer zahlte am vierten Mai. Die Einwendung ist nicht "
     "ausgeschlossen. [gest]Vorsicht bei Gestaltungsrechten wie der Aufrechnung: Nach dem Bundesgerichtshof ist sie "
     "ausgeschlossen, wenn die Forderungen sich schon vor dem Schluss der Verhandlung aufrechenbar gegenüberstanden, auch "
     "wenn erst später aufgerechnet wird. [abs3]Und Absatz drei: Alle Einwendungen, die der Schuldner bei Klageerhebung "
     "geltend machen kann, muss er in dieser Klage vorbringen.", PS),
    # --- H Tenor (Klausurkonvention) ----------------------------------------------------------------------------------------------
    ("[tenor]Der Tenor lautet nach Klausurkonvention: Die Zwangsvollstreckung aus dem Urteil des Amtsgerichts vom "
     "achtzehnten März wird für unzulässig erklärt. [antrag]In der Anwaltsklausur beantragst du entsprechend, die Zwangsvollstreckung für unzulässig zu erklären.", PS),
    # --- I Eilrechtsschutz: § 769, § 775, § 776, § 770 -------------------------------------------------------------------------------
    ("[eil]Die Klage allein hält die Vollstreckung aber nicht auf. [p769]Deshalb beantragt Rechtsanwältin Kellermann "
     "zugleich die einstweilige Einstellung nach Paragraf siebenhundertneunundsechzig. Das Prozessgericht kann anordnen, dass "
     "die Zwangsvollstreckung bis zum Urteil gegen oder ohne Sicherheitsleistung eingestellt wird. [glaub]Die Tatsachen, "
     "die den Antrag begründen, sind glaubhaft zu machen, [glaub2]hier mit dem Überweisungsbeleg und einer eidesstattlichen "
     "Versicherung. [nr2]Den Beschluss legt Herr Neubauer der Gerichtsvollzieherin vor, dann stellt sie ein, Paragraf "
     "siebenhundertfünfundsiebzig Nummer zwei.", PS),
    ("[p775]Schon vorher hilft ihm sein Beleg. [wl775]Nach Paragraf siebenhundertfünfundsiebzig Nummer fünf ist die "
     "Zwangsvollstreckung einzustellen, wenn der Überweisungsnachweis einer Bank vorgelegt wird, aus dem sich ergibt, dass "
     "der nötige Betrag auf das Konto des Gläubigers überwiesen worden ist. [nr4]Eine Quittung von Herrn Rademacher wäre "
     "ein Fall der Nummer vier. [p776]Aber Achtung: Bereits getroffene Vollstreckungsmaßregeln bleiben dann einstweilen "
     "bestehen, Paragraf siebenhundertsechsundsiebzig. [titel]Und das Urteil bleibt ein Titel. Seine Vollstreckbarkeit "
     "beseitigt erst die Vollstreckungsabwehrklage. [p770]Im Urteil kann das Gericht die einstweilige Anordnung dann "
     "bestätigen, ändern oder aufheben, Paragraf siebenhundertsiebzig.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei der Präklusion das richtige Datum. Es zählt der Schluss der mündlichen Verhandlung, "
     "nicht der Tag der Verkündung. [tipp2]Wer zwischen Verhandlung und Urteil zahlt, ist also nicht ausgeschlossen. "
     "[tipp3]Und in der Anwaltsklausur gehören Klage und Eilantrag zusammen.", PS),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sA]A: Zulässigkeit. [s1]Erstens Statthaftigkeit: eine materielle Einwendung gegen den "
     "titulierten Anspruch. [s2]Zweitens Zuständigkeit: das Prozessgericht des ersten Rechtszuges, ausschließlich. "
     "[s3]Drittens Rechtsschutzbedürfnis, solange der Gläubiger den Titel hat. [sB]B: Begründetheit. [sb1]Erstens eine "
     "Einwendung gegen den Anspruch, hier die Erfüllung. [sb2]Zweitens keine Präklusion nach Absatz zwei "
     "[sb3]und drei. [sC]Daneben der Antrag auf einstweilige Einstellung.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nach der letzten mündlichen Verhandlung zahlt, wehrt sich mit der Vollstreckungsabwehrklage. "
     "[m2]Und bis zum Urteil schützt ihn die einstweilige Einstellung.", 1.4),
]
