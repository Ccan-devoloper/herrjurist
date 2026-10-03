"""Folge 096 · Drittwiderspruchsklage § 771 ZPO: Wenn fremde Sachen gepfändet werden (Fr · 2. Examen · ZV, Format Schema).
Übungsfall nach dem Hook des Themenplans: Frau Wendland lässt ihre Wohnung renovieren und gibt ihr Ölgemälde so lange
ihrem Enkel Herrn Vollmer (Student) zur Aufbewahrung; beide halten auf einem Zettel fest, dass das Bild ihr gehört.
Herr Vollmer schuldet dem Fahrradhändler Herrn Gebhardt 1.800 Euro; aus dem rechtskräftigen Urteil des Amtsgerichts
pfändet die Gerichtsvollzieherin das Gemälde in seiner Wohnung (§ 808 I ZPO, BGH III ZR 143/06 Rn. 9: nur Gewahrsam).
Die Versteigerung ist in drei Wochen angesetzt. Frau Wendland wehrt sich.
A. Zulässigkeit: Statthaftigkeit (Wortlautkarte § 771 I; Abgrenzung § 766 und § 805 je ein Satz, Verweis auf Folge 054),
Zuständigkeit (§ 771 I, § 802; sachlich nach dem Streitwert, § 6 ZPO, BGH IX ZR 69/05 Rn. 2; § 23 Nr. 1 GVG), Parteien
(§ 771 II), Rechtsschutzbedürfnis (solange die Vollstreckung andauert; Beleg ohne Randnummer, ohne Aktenzeichen gesprochen).
B. Begründetheit: Eigentum als die Veräußerung hinderndes Recht (BGH V ZR 267/17 Rn. 6), Verwahrung (§§ 688, 868 BGB),
Beweislast und Eigentumsvermutung § 1006 I, III BGB (Beleg ohne Randnummer, ohne Aktenzeichen gesprochen), keine
Einwendungen des Beklagten. Tenor als Klausurkonvention (§ 775 Nr. 1 ZPO; BGH IX ZR 181/05 Rn. 2).
Klausurtipp (Lexi): einstweilige Anordnung über § 771 III mit §§ 769, 770 (Wortlautkarte § 769 I auszugsweise),
Glaubhaftmachung, § 775 Nr. 2 → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Fiktive Figuren: Frau Wendland (hilde), Herr Vollmer (stephan), die Gerichtsvollzieherin (lucy); Herr Gebhardt spricht nicht.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Wendland": "hilde", "Vollmer": "stephan", "Gerichtsvollzieherin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Gemälde der Großmutter ------------------------------------------------------------------------------
    ("[fall]Frau Wendland lässt ihre Wohnung renovieren. [bild]Ihr Ölgemälde gibt sie so lange ihrem Enkel, Herrn "
     "Vollmer. Er studiert und soll es nur aufbewahren. [zettel]Auf einem Zettel halten beide fest: Das Bild gehört ihr.", 0.2),
    ("[w1]Pass gut darauf auf. Nach der Renovierung hole ich es wieder ab.", 0.4, "Wendland"),
    # --- B Fall: die Pfändung -----------------------------------------------------------------------------------------------
    ("[schuld]Herr Vollmer hat allerdings Schulden: Dem Fahrradhändler Herrn Gebhardt schuldet er tausendachthundert Euro. "
     "[titel]Herr Gebhardt hat ein rechtskräftiges Urteil des Amtsgerichts [gv]und beauftragt die Gerichtsvollzieherin. "
     "[klingel]Sie klingelt bei Herrn Vollmer.", 0.3),
    ("[g1]Das Gemälde an der Wand pfände ich.", 0.3, "Gerichtsvollzieherin"),
    ("[v1]Das gehört meiner Oma! Ich bewahre es nur für sie auf.", 0.3, "Vollmer"),
    ("[g2]Es ist in Ihrer Wohnung. Wem es gehört, prüfe ich nicht.", 0.4, "Gerichtsvollzieherin"),
    ("[versteig]Die Versteigerung soll in drei Wochen stattfinden. [oma]Am nächsten Tag kommt Frau Wendland vorbei.", 0.2),
    ("[w2]Das Bild gehört mir. Das lasse ich nicht versteigern!", 0.4, "Wendland"),
    ("[frage]Wie wehrt sich Frau Wendland? [frage2]Und wie stoppt sie die Versteigerung rechtzeitig?", 0.6),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D A. Zulässigkeit: Statthaftigkeit, Wortlaut § 771 I --------------------------------------------------------------
    ("[zul]A: Zulässigkeit. [statt]Erstens die Statthaftigkeit. [wl771]Paragraf siebenhunderteinundsiebzig Absatz eins: "
     "Behauptet ein Dritter, dass ihm an dem Gegenstand der Zwangsvollstreckung ein die Veräußerung hinderndes Recht "
     "zustehe, so ist der Widerspruch gegen die Zwangsvollstreckung im Wege der Klage bei dem Gericht geltend zu machen, "
     "in dessen Bezirk die Zwangsvollstreckung erfolgt. [dritt]Frau Wendland ist nicht Schuldnerin, sondern Dritte. Sie "
     "behauptet ihr Eigentum am Gemälde. Die Drittwiderspruchsklage ist statthaft.", P),
    # --- E Abgrenzung § 766, § 805 ---------------------------------------------------------------------------------------------
    ("[a766]Abgrenzung: Die Erinnerung nach Paragraf siebenhundertsechsundsechzig rügt nur die Art und Weise der "
     "Vollstreckung. [gew]Hier hat die Gerichtsvollzieherin richtig gehandelt: Sie prüft grundsätzlich nur den Gewahrsam "
     "des Schuldners, nicht das Eigentum. [a805]Und wer ohne Besitz nur ein Pfand- oder Vorzugsrecht hat, klagt nach "
     "Paragraf achthundertfünf auf vorzugsweise Befriedigung aus dem Erlös. [verw]Mehr dazu in unserem Video zu den "
     "Rechtsbehelfen in der Zwangsvollstreckung.", P),
    # --- F Zuständigkeit, Parteien --------------------------------------------------------------------------------------------
    ("[zust]Zweitens die Zuständigkeit. Örtlich zuständig ist das Gericht, in dessen Bezirk vollstreckt wird, [p802]und "
     "zwar ausschließlich, Paragraf achthundertzwei. [sachl]Sachlich entscheidet der Streitwert. Nach Paragraf sechs ist "
     "das der Betrag der Forderung, hier tausendachthundert Euro. Ist die Sache weniger wert, zählt ihr Wert. [ag]Also ist "
     "das Amtsgericht am Wohnort von Herrn Vollmer zuständig. [bekl]Verklagt wird der Gläubiger, Herr Gebhardt. Klagt sie "
     "auch gegen den Schuldner, sind beide Streitgenossen, Absatz zwei.", P),
    # --- G Rechtsschutzbedürfnis ------------------------------------------------------------------------------------------------
    ("[rsb]Drittens das Rechtsschutzbedürfnis. Es besteht, sobald die Vollstreckung begonnen hat, und solange sie andauert. "
     "[rsb2]Ist sie durch die Verwertung des Gemäldes beendet, entfällt es. [rsb3]Hier ist das Bild gepfändet, aber noch nicht "
     "versteigert. Die Klage ist zulässig.", PS),
    # --- H B. Begründetheit: die Veräußerung hinderndes Recht ------------------------------------------------------------------
    ("[begr]B: Begründetheit. [recht]Erstens braucht Frau Wendland ein die Veräußerung hinderndes Recht. Der Standardfall "
     "ist das Eigentum. [eig]Dann greift die Vollstreckung auf das Vermögen einer Dritten über, das nicht für die Forderung "
     "haftet. [verwahr]Die Verwahrung ändert daran nichts: Herr Vollmer besitzt das Bild nur, Eigentümerin bleibt seine "
     "Großmutter.", P),
    # --- I Beweislast, § 1006 BGB ------------------------------------------------------------------------------------------------
    ("[beweis]Aber Achtung bei der Beweislast: Die Klägerin muss ihr Recht beweisen. [bw2]Und Herr Gebhardt kann sich auf "
     "Paragraf tausendsechs BGB berufen: Zugunsten des Besitzers einer beweglichen Sache wird vermutet, dass er Eigentümer "
     "ist. Besitzer ist hier der Enkel. [bw3]Frau Wendland muss deshalb zeigen, dass er das Bild nur für sie verwahrt. "
     "[p1006]Dann ist sie mittelbare Besitzerin, und nach Absatz drei gilt die Vermutung für sie. [zettel2]Ihr Zettel "
     "belegt die Verwahrung. Ihr Eigentum steht fest.", P),
    # --- J Einwendungen, Ergebnis, Tenor ----------------------------------------------------------------------------------------
    ("[einw]Zweitens dürfen keine Einwendungen von Herrn Gebhardt greifen. Er könnte etwa einwenden, das Vermögen der "
     "Dritten hafte selbst für die Forderung. [keine]Frau Wendland schuldet ihm aber nichts. Die Klage ist begründet. "
     "[tenor]Der Tenor lautet nach Klausurkonvention: Die Zwangsvollstreckung aus dem Urteil des Amtsgerichts in das "
     "Ölgemälde wird für unzulässig erklärt.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Klage allein hält die Versteigerung nicht auf. [tipp2]Beantrage zugleich die einstweilige "
     "Einstellung. Absatz drei verweist dafür auf die Paragrafen siebenhundertneunundsechzig und siebenhundertsiebzig.", PS),
    # --- L Eilantrag, Wortlaut § 769 I ---------------------------------------------------------------------------------------------
    ("[wl769]Nach Paragraf siebenhundertneunundsechzig Absatz eins kann das Prozessgericht auf Antrag anordnen, dass die "
     "Zwangsvollstreckung bis zum Urteil gegen oder ohne Sicherheitsleistung eingestellt wird. [glaub]Die Tatsachen sind "
     "glaubhaft zu machen, hier mit dem Zettel und einer eidesstattlichen Versicherung. [vorlage]Den Beschluss legt Frau "
     "Wendland der Gerichtsvollzieherin vor, dann stellt sie ein, Paragraf siebenhundertfünfundsiebzig Nummer zwei. "
     "[p770]Im Urteil kann das Gericht die Anordnung bestätigen, ändern oder aufheben, Paragraf siebenhundertsiebzig.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sA]A: Zulässigkeit. [s1]Erstens Statthaftigkeit: Ein Dritter behauptet ein die "
     "Veräußerung hinderndes Recht. [s2]Zweitens Zuständigkeit: das Gericht am Ort der Vollstreckung, ausschließlich, "
     "sachlich nach dem Streitwert. [s3]Drittens Rechtsschutzbedürfnis, solange die Vollstreckung andauert. "
     "[sB]B: Begründetheit. [sb1]Erstens ein die Veräußerung hinderndes Recht, meist das Eigentum. [sb2]Zweitens keine "
     "Einwendungen des Beklagten. [sC]Daneben der Antrag auf einstweilige Einstellung.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gepfändet wird, was der Schuldner im Gewahrsam hat. [m2]Gehört es einem Dritten, wehrt er sich mit der "
     "Drittwiderspruchsklage.", 1.4),
]
