"""Folge 015 · Strafrecht AT Überblick: Welches Prüfungsschema wann? (Fr · Klausurpraxis, Format Schema).
Beispielfall (frei erfunden, „Gartenfest-Fall“): Sommerfest in der Kleingartenanlage. Konrad zerschlägt mit Inas Hammer
Ottos Blumentopf (vorsätzliches vollendetes Begehungsdelikt, § 303 I; Ina: Beihilfe, § 27 I). Rudolf will Ottos
Rasenmäher mitnehmen, zieht schon, der Mäher ist angekettet (Versuch, §§ 242 I, II, 22, 23 I). Bernd gießt Spiritus in
die Grillglut, Stichflamme, Brandblase bei Otto (Fahrlässigkeit, § 229). Gerda ruft ihren Hund nicht zurück, er beißt
Otto (Unterlassen, §§ 223 I, 13 I). Vier Weichen in derselben Reihenfolge wie im Schema: allein oder mit anderen?
vollendet oder versucht? Vorsatz oder Fahrlässigkeit? Tun oder Unterlassen? Aufbauregeln als Klausurkonvention
gekennzeichnet. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für
Bild/Tafel/Prüfpfad; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Konrad": "stephan", "Otto": "helmut", "Gerda": "elinor"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Gartenfest, Blumentopf -------------------------------------------------------------------------------
    ("[fall]Sommerfest in der Kleingartenanlage. [otto]Otto liegt mit Konrad im Streit, wegen der Hecke.", 0.2),
    ("[k1]Ina, gib mir mal deinen Hammer. Ottos Blumentopf ist fällig.", 0.3, "Konrad"),
    ("[reicht]Ina reicht ihm den Hammer. [schlag]Konrad zerschlägt den Topf.", 0.4),
    # --- B Fall: Rasenmäher, Grill, Hund -----------------------------------------------------------------------------
    ("[rudolf]Am Zaun will Rudolf Ottos Rasenmäher mitnehmen und behalten. [zieht]Er packt den Griff und zieht los. "
     "[kette]Doch der Mäher ist angekettet. Das hat Rudolf übersehen, Werkzeug hat er keins.", 0.4),
    ("[grill]Am Grill gießt Bernd Brennspiritus in die Glut, damit es schneller geht. [flamme]Eine Stichflamme schießt "
     "hoch, [blase]Otto bekommt eine Brandblase an der Hand.", 0.4),
    ("[hund]Dann knurrt Gerdas Hund Otto an.", 0.1),
    ("[o1]Gerda, ruf deinen Hund zurück!", 0.2, "Otto"),
    ("[g1]Geschieht dir recht.", 0.3, "Gerda"),
    ("[biss]Gerda bleibt sitzen. Der Hund beißt Otto in die Wade.", 0.5),
    ("[frage]Wer hat sich wie strafbar gemacht? [fuenf]Fünf Personen, und jede braucht ein anderes Prüfungsschema.", 0.6),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Grundfall und Weichen ---------------------------------------------------------------------------------------
    ("[weichen]Ausgangspunkt ist der Grundfall: Einer handelt allein und vorsätzlich durch aktives Tun, und die Tat ist vollendet. "
     "[vier]Jede Abweichung stellt eine Weiche: [w1]allein oder mit anderen? [w2]Vollendet oder versucht? "
     "[w3]Vorsatz oder Fahrlässigkeit? [w4]Tun oder Unterlassen? "
     "[konv]Die Schemata selbst stehen nicht im Gesetz. Sie ordnen, was die Paragrafen verlangen.", PS),
    # --- E Konrad: Grundschema -----------------------------------------------------------------------------------------
    ("[konrad]Konrad ist der Grundfall. [p303]Sachbeschädigung, Paragraf dreihundertdrei. [tb]Römisch eins, Tatbestand: "
     "objektiv zerstört er eine fremde Sache, subjektiv mit Wissen und Wollen. "
     "[rw]Römisch zwei, Rechtswidrigkeit, [schuld]Römisch drei, Schuld: Beides liegt vor.", PS),
    # --- F Ina: Beteiligung --------------------------------------------------------------------------------------------
    ("[ina]Erste Weiche: Ina hat nicht selbst zugeschlagen. [tvt]Wirken mehrere zusammen, prüfst du erst den Täter, dann "
     "den Teilnehmer. [p27]Gehilfe ist nach Paragraf siebenundzwanzig, wer vorsätzlich einem anderen zu dessen "
     "vorsätzlich begangener rechtswidriger Tat Hilfe geleistet hat. [haupt]Konrads Tat steht fest, [hammer]der Hammer hat "
     "geholfen, [vorsatz]und Inas Vorsatz umfasst Konrads Tat und ihre Hilfe. [mitt]Mittäterin ist sie nicht, die Tat "
     "war allein Konrads Sache. Beihilfe zur Sachbeschädigung.", PS),
    # --- G Rudolf: Versuch ---------------------------------------------------------------------------------------------
    ("[rudolf2]Zweite Weiche: Bei Rudolf steht der Mäher noch da. [vorpr]Das Versuchsschema beginnt mit der "
     "Vorprüfung: Die Tat ist nicht vollendet, [p242]und der Versuch ist strafbar, Paragraf zweihundertzweiundvierzig "
     "Absatz zwei.", P),
    ("[entschl]Im Tatbestand erstens der Tatentschluss: Rudolf wollte den Mäher wegnehmen und behalten. "
     "[ansetz]Zweitens das unmittelbare Ansetzen, Paragraf zweiundzwanzig: Er hat schon gezogen. "
     "[ruecktr]Nach Rechtswidrigkeit und Schuld kommt der Rücktritt. Er scheidet aus, der Versuch ist fehlgeschlagen.", PS),
    # --- H Bernd: Fahrlässigkeit ---------------------------------------------------------------------------------------
    ("[bernd]Dritte Weiche: Bernd wollte niemanden verletzen. [p15]Ohne Vorsatz ist er nach Paragraf fünfzehn nur "
     "strafbar, wenn das Gesetz fahrlässiges Handeln ausdrücklich mit Strafe bedroht. "
     "[p229]Hier tut es das: fahrlässige Körperverletzung, Paragraf zweihundertneunundzwanzig.", P),
    ("[erfolg]Im Tatbestand prüfst du Erfolg, Handlung und Kausalität. [sorg]Der Kern ist die objektive "
     "Sorgfaltspflichtverletzung bei objektiver Vorhersehbarkeit: [spiritus]Spiritus in Glut zu gießen, ist bekannt "
     "gefährlich. [zurech]Genau diese Gefahr hat sich in der Brandblase verwirklicht. [subj]Nach dem üblichen Aufbau "
     "gibt es keinen subjektiven Tatbestand: Ob Bernd die Gefahr persönlich erkennen konnte, prüfst du in der Schuld.", PS),
    # --- I Gerda: Unterlassen ------------------------------------------------------------------------------------------
    ("[gerda]Vierte Weiche: Gerda hat nichts getan, sie hat ihren Hund nicht zurückgerufen. [p13]Nach Paragraf "
     "dreizehn ist sie nur strafbar, wenn sie rechtlich dafür einzustehen hat, dass der Erfolg nicht eintritt.", P),
    ("[biss2]Im Tatbestand: Der Biss ist eine Körperverletzung. [rufen]Gerda hätte rufen können, [quasi]und der Hund "
     "hätte gehorcht. [garant]Als Halterin muss sie ihren Hund überwachen: Garantenstellung. "
     "[entspr]Bei der Körperverletzung entspricht das Unterlassen ohne Weiteres einem Tun, [gvors]und Gerda wollte den Biss. "
     "Körperverletzung durch Unterlassen.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Weichen lassen sich kombinieren. [tipp2]Hätte Gerda den Hund nur übersehen, obwohl sie "
     "aufpassen musste, prüfst du fahrlässige Körperverletzung durch Unterlassen.", PS),
    # --- K Klausurschema (Entscheidungsbaum) ---------------------------------------------------------------------------
    ("[sch]Dein Entscheidungsbaum. [e1]Erstens: Mehrere beteiligt? Dann Täter vor Teilnehmer. "
     "[e2]Zweitens: Nur versucht? Dann Vorprüfung, Tatentschluss, unmittelbares Ansetzen. "
     "[e3]Drittens: Fahrlässig? Dann nur bei ausdrücklicher Strafdrohung, mit Sorgfaltspflichtverletzung. "
     "[e4]Viertens: Unterlassen? Dann Paragraf dreizehn mit Garantenstellung. "
     "[e5]Keine Weiche? Dann bleibt es beim Grundschema.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Gerüst bleibt immer gleich, Tatbestand, Rechtswidrigkeit, Schuld. "
     "[m2]Die Weichen verändern vor allem den Tatbestand.", 1.4),
]
