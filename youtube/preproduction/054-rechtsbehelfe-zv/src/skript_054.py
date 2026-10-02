"""Folge 054 · Rechtsbehelfe Zwangsvollstreckung: §§ 766, 767, 771, 805 ZPO (Fr · 2. Examen · ZV, Format Schema).
Beispielfall (Plan-Hook): Frau Hollmann (Autowerkstatt) hat gegen Herrn Steinbach ein rechtskräftiges Urteil des
Amtsgerichts über 2.400 Euro Reparaturkosten. Einen Monat nach dem Urteil überweist Herr Steinbach den vollen Betrag.
Trotzdem lässt Frau Hollmann vollstrecken; der Gerichtsvollzieher pfändet in Steinbachs Wohnung einen Fernseher, den
ihm seine Schwester, Frau Weidner, geliehen hat. Leitfrage „Wer wehrt sich wogegen?“: § 766 (Art und Weise; GV prüft
nur Gewahrsam, BGH III ZR 143/06 Rn. 9; materielle Einwendungen nicht, BGH I ZB 91/08 Rn. 9, 13; Beispiel § 811)
→ § 793 (sofortige Beschwerde gegen die Entscheidung, § 569 I) → § 767 (Erfüllung § 362 BGB, Präklusion § 767 II)
→ § 768 kurz → § 771 (Eigentum der Schwester, BGH III ZR 143/06 Rn. 12) → § 805 kurz (Vermieterpfandrecht, § 562 BGB,
BGH I ZB 91/08 Rn. 15) → Klausurtipp (§ 769, § 771 III) → Schema (Zulässigkeit: Statthaftigkeit, ausschließliche
Zuständigkeit § 802; Begründetheit) → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Hollmann, Steinbach, Weidner;
Gerichtsvollzieher ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Hollmann": "hilde", "Steinbach": "stephan", "Weidner": "lucy", "Gerichtsvollzieher": "christian"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: die Werkstatt, das Urteil, die Zahlung ------------------------------------------------------------------
    ("[fall]Frau Hollmann betreibt eine Autowerkstatt. [rep]Sie repariert das Auto von Herrn Steinbach, für "
     "zweitausendvierhundert Euro. [zahlt]Er zahlt nicht. [urteil]Das Amtsgericht verurteilt ihn, das Urteil wird "
     "rechtskräftig. [ueberw]Einen Monat danach überweist Herr Steinbach den vollen Betrag. [auftr]Trotzdem beauftragt "
     "Frau Hollmann den Gerichtsvollzieher.", 0.3),
    ("[h1]Bitte pfänden Sie bei Herrn Steinbach.", 0.5, "Hollmann"),
    # --- B Fall: in der Wohnung ------------------------------------------------------------------------------------------
    ("[wohn]In seiner Wohnung steht neben seinem alten Gerät ein zweiter, großer Fernseher. [schw]Den hat ihm seine Schwester geliehen, Frau Weidner.", 0.3),
    ("[g1]Diesen Fernseher pfände ich. Hier ist das Siegel.", 0.4, "Gerichtsvollzieher"),
    ("[st1]Aber ich habe doch längst bezahlt!", 0.4, "Steinbach"),
    ("[w1]Und der Fernseher gehört mir!", 0.4, "Weidner"),
    ("[g2]Er steht in Ihrer Wohnung. Das genügt für die Pfändung.", 0.5, "Gerichtsvollzieher"),
    ("[frage]Wer kann sich jetzt wogegen wehren? [frage2]Und mit welchem Rechtsbehelf?", 0.6),
    # --- C Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Leitfrage -----------------------------------------------------------------------------------------------------
    ("[ueber]Die Leitfrage lautet: Wer wehrt sich wogegen? [l766]Wer die Art und Weise der Vollstreckung rügt, also einen "
     "Verfahrensfehler, erhebt Erinnerung, Paragraf siebenhundertsechsundsechzig. [l767]Wendet sich der Schuldner gegen "
     "den titulierten Anspruch selbst, erhebt er Vollstreckungsabwehrklage, Paragraf siebenhundertsiebenundsechzig. "
     "[l771]Beruft sich ein Dritter auf ein Recht am Gegenstand, erhebt er Drittwiderspruchsklage, Paragraf "
     "siebenhunderteinundsiebzig, [l805]oder Vorzugsklage, Paragraf achthundertfünf.", PS),
    # --- E § 766 Erinnerung ----------------------------------------------------------------------------------------------
    ("[e766]Zuerst die Erinnerung. Sie erfasst Einwendungen, welche die Art und Weise der Zwangsvollstreckung oder das "
     "vom Gerichtsvollzieher zu beobachtende Verfahren betreffen. [vg]Darüber entscheidet das Vollstreckungsgericht, "
     "das Amtsgericht, in dessen Bezirk vollstreckt wird. [p811]Typisch: Der Gerichtsvollzieher pfändet eine unpfändbare Sache, "
     "Paragraf achthundertelf. [gew]Hier liegt kein solcher Fehler vor. Der Gerichtsvollzieher prüft nach dem "
     "Bundesgerichtshof grundsätzlich nur, ob die Sache im Gewahrsam des Schuldners ist, nicht, ob sie ihm gehört. [mat]Zahlung und "
     "Eigentum sind materielle Einwendungen. Sie gehören nicht in die Erinnerung. [beschw]Und auf das Recht seiner "
     "Schwester kann sich Herr Steinbach dort ohnehin nicht berufen.", PS),
    # --- F § 793 sofortige Beschwerde ------------------------------------------------------------------------------------
    ("[p793]Entscheidet das Vollstreckungsgericht über eine Erinnerung, ist dagegen die sofortige Beschwerde statthaft, "
     "Paragraf siebenhundertdreiundneunzig. [frist]Die Notfrist beträgt zwei Wochen ab Zustellung.", PS),
    # --- G § 767 Vollstreckungsabwehrklage -------------------------------------------------------------------------------
    ("[e767]Herr Steinbach hat bezahlt. Das betrifft den titulierten Anspruch selbst. [wl767]Solche Einwendungen macht "
     "der Schuldner im Wege der Klage beim Prozessgericht des ersten Rechtszuges geltend, [ag767]hier beim Amtsgericht, "
     "das ihn verurteilt hat. [erf]Mit der Zahlung ist die Schuld erloschen, Paragraf dreihundertzweiundsechzig BGB. "
     "[prae]Aber Absatz zwei: Ihr Grund muss nach dem Schluss der mündlichen Verhandlung entstanden sein. "
     "[prae2]Hätte er schon vorher gezahlt, wäre er damit ausgeschlossen. [ok767]Er zahlte erst nach dem Urteil. "
     "[tenor]Seine Klage ist begründet: Das Gericht erklärt die Zwangsvollstreckung aus dem Urteil für unzulässig.", PS),
    # --- H § 768 kurz ----------------------------------------------------------------------------------------------------
    ("[p768]Kurz zur Klauselgegenklage, Paragraf siebenhundertachtundsechzig. Mit ihr bestreitet der Schuldner, dass "
     "die Voraussetzungen vorliegen, unter denen eine Klausel erteilt wurde, etwa eine Rechtsnachfolge.", PS),
    # --- I § 771 Drittwiderspruchsklage ----------------------------------------------------------------------------------
    ("[e771]Jetzt Frau Weidner. Sie ist nicht Partei des Urteils, sondern Dritte. [wl771]Paragraf "
     "siebenhunderteinundsiebzig: Behauptet ein Dritter, dass ihm an dem Gegenstand der Zwangsvollstreckung ein die "
     "Veräußerung hinderndes Recht zustehe, macht er den Widerspruch im Wege der Klage geltend. [eig]Ein solches Recht "
     "ist ihr Eigentum am Fernseher. [ger771]Sie klagt gegen Frau Hollmann, bei dem Gericht, in dessen Bezirk vollstreckt "
     "wird. [ok771]Steht ihr Eigentum fest, erklärt das Gericht die Zwangsvollstreckung in den Fernseher für unzulässig.", PS),
    # --- J § 805 kurz ----------------------------------------------------------------------------------------------------
    ("[p805]Anders ist es bei einem Dritten, der die Sache nicht besitzt und nur ein Pfandrecht hat, etwa ein Vermieter "
     "an den eingebrachten Sachen des Mieters. [p805b]Er kann der Pfändung nicht widersprechen. Er klagt nur auf "
     "vorzugsweise Befriedigung aus dem Erlös, Paragraf achthundertfünf.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Mehrere Beteiligte können zugleich verschiedene Rechtsbehelfe haben. Hier klagt Herr Steinbach "
     "nach Paragraf siebenhundertsiebenundsechzig, Frau Weidner nach Paragraf siebenhunderteinundsiebzig. [tipp2]Und die Klage allein hält die "
     "Vollstreckung nicht auf. Beantrage deshalb zugleich die einstweilige Einstellung, Paragraf "
     "siebenhundertneunundsechzig, bei der Drittwiderspruchsklage über Paragraf siebenhunderteinundsiebzig Absatz drei.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sA]A: Zulässigkeit. [s1]Erstens Statthaftigkeit nach der Leitfrage. [s2]Zweitens die "
     "Zuständigkeit. Sie ist ausschließlich, Paragraf achthundertzwei. [s3]Drittens das Rechtsschutzbedürfnis. "
     "[sB]B: Begründetheit. [sb1]Bei der Erinnerung ein Verstoß gegen Vollstreckungsrecht, [sb2]bei der "
     "Vollstreckungsabwehrklage eine materielle Einwendung, die nicht nach Absatz zwei ausgeschlossen ist, [sb3]bei der "
     "Drittwiderspruchsklage ein die Veräußerung hinderndes Recht des Dritten.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Gegen das Wie der Vollstreckung hilft die Erinnerung, gegen den Anspruch die Vollstreckungsabwehrklage. "
     "[m2]Und wem die Sache gehört, klärt die Drittwiderspruchsklage.", 1.4),
]
