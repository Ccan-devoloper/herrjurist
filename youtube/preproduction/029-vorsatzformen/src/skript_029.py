"""Folge 029 · Vorsatzformen: Absicht, direkter Vorsatz, Eventualvorsatz erklärt (Examenswissen, Format Schema).
Fiktiver Fall: Volker (Anfang 60) reißt die alte Mauer am Ende seines Gartens ab; sie kippt auf den neuen Holzzaun seiner
Nachbarin Heike. Sachbeschädigung (§ 303 I StGB), § 15 StGB (keine fahrlässige Sachbeschädigung). Varianten: Absicht
(dolus directus 1. Grades), direkter Vorsatz (2. Grades) mit dem Thomas-Fall (Bremerhaven 1875) als Lehrbuchbeispiel,
Eventualvorsatz (BGHSt 63, 88 Rn. 18; BGHSt 57, 183 Rn. 30), bewusste Fahrlässigkeit, Gesamtschau (BGHSt 63, 88 Rn. 20),
Tatumstandsirrtum § 16 I; Klausurtipp mit Hemmschwelle (BGHSt 57, 183 Rn. 42, 45) und § 226 II (BGH 2 StR 150/15 Rn. 18).
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Volker": "helmut", "Heike": "sabrina"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die alte Mauer ----------------------------------------------------------------------------------------
    ("[fall]Samstagmorgen in einer Reihenhaussiedlung. [volker]Volker, Anfang sechzig, will die alte Mauer am Ende seines "
     "Gartens abreißen. [heike]Gleich dahinter steht der neue Holzzaun seiner Nachbarin Heike.", 0.3),
    ("[h1]Pass bitte auf meinen Zaun auf!", 0.3, "Heike"),
    ("[v1]Die Mauer muss heute weg.", 0.4, "Volker"),
    ("[hammer]Volker schlägt mit dem Vorschlaghammer die unteren Steine heraus. [kippt]Die Mauer kippt, genau auf Heikes "
     "Zaun. [bruch]Drei Latten brechen.", 0.3),
    ("[h2]Mein neuer Zaun!", 0.4, "Heike"),
    ("[frage]Hat Volker den Zaun vorsätzlich beschädigt? [frage2]Das hängt davon ab, was er wusste und was er wollte.", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt mit allen Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Sachbeschädigung und § 15 -----------------------------------------------------------------------------------
    ("[p303]Geprüft wird Sachbeschädigung, Paragraf dreihundertdrei. [objektiv]Objektiv ist alles klar: Der Zaun ist für "
     "Volker eine fremde Sache, und er hat ihn beschädigt. [p15]Entscheidend ist der Vorsatz. Denn Paragraf fünfzehn sagt: "
     "Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz fahrlässiges Handeln ausdrücklich mit Strafe bedroht. "
     "[keinef]Eine fahrlässige Sachbeschädigung kennt das Gesetz nicht.", PS),
    # --- D Wissen und Wollen -------------------------------------------------------------------------------------------
    ("[ww]Vorsatz heißt Wissen und Wollen der Tatbestandsverwirklichung. [formen]Je nachdem, wie stark Wissen und Wollen "
     "ausgeprägt sind, unterscheidet man drei Vorsatzformen. Spielen wir sie an Volker durch.", P),
    # --- E Variante 1: Absicht -----------------------------------------------------------------------------------------
    ("[var1]Variante eins: Der Zaun ärgert Volker schon lange.", 0.2),
    ("[v2]Genau dorthin soll die Mauer fallen.", 0.4, "Volker"),
    ("[abs]Volker kommt es gerade darauf an, den Zaun zu beschädigen. Das ist Absicht, dolus directus ersten Grades. "
     "[abs2]Beim Wissen genügt hier sogar, dass er den Erfolg nur für möglich hält. Entscheidend ist das Wollen.", PS),
    # --- F Variante 2: direkter Vorsatz --------------------------------------------------------------------------------
    ("[var2]Variante zwei: Volker hat nichts gegen den Zaun. Aber die Mauer steht so schief, dass sie nur zum Zaun hin "
     "fallen kann. [sicher]Das weiß er sicher.", 0.2),
    ("[v3]Schade um den Zaun. Aber die Mauer muss weg.", 0.4, "Volker"),
    ("[dir]Er sieht die Beschädigung als sicher voraus. Das ist direkter Vorsatz, dolus directus zweiten Grades. "
     "[dir2]Dass ihm der Erfolg unerwünscht ist, ändert nichts.", P),
    # --- G Lehrbuchbeispiel: Thomas-Fall -------------------------------------------------------------------------------
    ("[thomas]Das klassische Lehrbuchbeispiel ist der Thomas-Fall aus Bremerhaven, achtzehnhundertfünfundsiebzig. "
     "[fass]Ein Betrüger ließ ein hoch versichertes Fass mit Sprengstoff und Uhrwerk auf ein Auswandererschiff bringen. "
     "[plan]Es sollte auf dem Ozean explodieren, und er wollte die Versicherungssumme kassieren. [th_ziel]Nach der Lehrbuchdeutung kam es ihm "
     "auf den Tod der Menschen an Bord nicht an. [th_wiss]Doch wäre sein Plan aufgegangen, wären sie sicher gestorben, und das "
     "wusste er. Das ist direkter Vorsatz.", PS),
    # --- H Variante 3: Eventualvorsatz ---------------------------------------------------------------------------------
    ("[var3]Variante drei: Volker hält es für möglich, dass die Mauer zum Zaun kippt. Abstützen ist ihm zu mühsam.", 0.2),
    ("[v4]Wenn es den Zaun erwischt, dann eben.", 0.4, "Volker"),
    ("[ev]Das ist Eventualvorsatz. [ev2]Nach dem Bundesgerichtshof erkennt der Täter den Erfolg als möglich und nicht ganz "
     "fernliegend [ev3]und billigt ihn oder findet sich mit ihm ab, mag er ihm auch unerwünscht sein. [raser]So formuliert "
     "es das Gericht in ständiger Rechtsprechung, etwa im Berliner Raser-Fall.", P),
    # --- I Variante 4: bewusste Fahrlässigkeit -------------------------------------------------------------------------
    ("[var4]Variante vier: Volker sieht dieselbe Gefahr. Deshalb bindet er die Mauer mit einem Seil an seinen Baum, "
     "damit sie zu ihm fällt.", 0.2),
    ("[v5]Mit dem Seil kann nichts passieren.", 0.4, "Volker"),
    ("[reisst]Doch das Seil reißt. [fahrl]Volker hat ernsthaft und nicht nur vage darauf vertraut, dass nichts passiert. "
     "Das ist bewusste Fahrlässigkeit, kein Vorsatz. [straflos]Wegen Sachbeschädigung strafbar ist er deshalb nicht. "
     "Schadensersatz schuldet er trotzdem, das regelt das Zivilrecht.", PS),
    # --- J Abgrenzung: Gesamtschau -------------------------------------------------------------------------------------
    ("[gesamt]Wie unterscheidet man Billigen und Vertrauen? Durch eine Gesamtschau aller objektiven und subjektiven "
     "Umstände. [indiz]Ein wesentliches Indiz ist die Gefährlichkeit der Handlung, dazu das Motiv und die konkreten "
     "Umstände. [seil]Volkers Seil spricht für echtes Vertrauen, sein Satz in Variante drei dagegen.", PS),
    # --- K Gegenstück: Tatumstandsirrtum -------------------------------------------------------------------------------
    ("[irrtum]Zum Schluss das Gegenstück: Volker hält den Zaun nach einem alten Grenzplan für seinen eigenen. "
     "[p16]Paragraf sechzehn: Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, "
     "handelt nicht vorsätzlich. [fremd]Volker kennt nicht, dass die Sache fremd ist. [p16b]Strafbar bliebe nur "
     "fahrlässige Begehung, und die gibt es hier nicht.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme die Vorsatzform nur, wenn es darauf ankommt. Meist genügt Eventualvorsatz. "
     "[tipp2]Verlangt das Gesetz aber Absicht oder Wissentlichkeit, wie Paragraf zweihundertsechsundzwanzig Absatz zwei, "
     "reicht Eventualvorsatz dafür nicht. [tipp3]Und bei Tötungsdelikten ersetzt das Schlagwort Hemmschwelle keine Begründung. "
     "Für den Bundesgerichtshof ist es nur ein Hinweis auf eine sorgfältige Gesamtwürdigung.", PS),
    # --- M Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zum Vorsatz. [k1]Römisch eins, Tatbestand. Erstens der objektive Tatbestand. [k2]Zweitens "
     "der subjektive Tatbestand: Vorsatz bei Begehung der Tat, bezogen auf alle objektiven Merkmale. [k2a]Prüfe Wissen "
     "und Wollen [k2b]und bestimme, wo nötig, die Vorsatzform: Absicht, direkter Vorsatz oder Eventualvorsatz. "
     "[k2c]Grenze zur bewussten Fahrlässigkeit ab [k2d]und denke an den Tatumstandsirrtum nach Paragraf sechzehn. "
     "[k3]Danach Rechtswidrigkeit und Schuld.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Absicht heißt, es kommt dem Täter darauf an. [m2]Direkter Vorsatz heißt, er weiß es sicher. "
     "[m3]Eventualvorsatz heißt, er hält es für möglich und findet sich damit ab. [m4]Wer ernsthaft auf das Ausbleiben "
     "vertraut, handelt höchstens fahrlässig.", 1.4),
]
