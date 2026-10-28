"""Folge 046 · Schadensersatz Schema: Das System der §§ 280 ff. BGB (Mo · Der Fall · Zivilrecht/Schuldrecht AT, Format Schema).
Beispielfall nach dem Plan-Hook („Die Waschmaschine kommt zu spät, ist kaputt und flutet dann noch das Bad“):
Gisela (Verbraucherin) kauft beim Elektrohändler Kranz eine Waschmaschine für 600 Euro, Lieferung und Anschluss am
2. März. Kranz vergisst den Termin und kommt eine Woche später (Waschsalon 30 Euro). Beim Ausladen stößt er die Maschine
unachtsam an, innen reißt ein Schlauch; beim ersten Waschgang flutet Wasser das Bad und den Parkettboden im Flur
(1.500 Euro). Frist zur Reparatur (zwei Wochen) läuft ungenutzt ab; Werkstatt repariert für 200 Euro.
Kern: § 280 I (Wortlaut), II, III (Wortlaut), Kontrollfrage nach BGH VIII ZR 169/12 Rn. 26 f. und VII ZR 63/18 Rn. 17–19;
Schadensersatz neben der Leistung (§§ 437 Nr. 3, 280 I), Verzögerungsschaden (§§ 280 I, II, 286 II Nr. 1, IV),
statt der Leistung (§§ 437 Nr. 3, 280 I, III, 281 I 1 Wortlaut; V ZR 33/19 Rn. 8;
§ 475d II nur im RECHTSSTAND/Beschreibung), §§ 282, 283, 311a II.
Figuren: Gisela (hilde), Herr Kranz (timo); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.7

STIMMEN = {"Gisela": "hilde", "Kranz": "timo"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Kauf, Verspätung, Wasserschaden, Reparatur ----------------------------------------------------------------
    ("[fall]Gisela kauft beim Elektrohändler Kranz eine Waschmaschine. [termin]Vereinbart sind "
     "Lieferung und Anschluss am zweiten März. [warten]Doch Herr Kranz vergisst den Termin und kommt erst eine Woche "
     "später. [salon]Bis dahin wäscht Gisela im Waschsalon, das kostet sie dreißig Euro.", 0.3),
    ("[k1]Entschuldigung, ich hatte den Termin vergessen!", 0.3, "Kranz"),
    ("[stoss]Beim Ausladen stößt er die Maschine unachtsam gegen die Treppe, innen reißt ein Schlauch. [flut]Beim ersten "
     "Waschgang läuft Wasser aus und flutet das Bad. [parkett]Der Parkettboden im Flur quillt auf: Schaden "
     "tausendfünfhundert Euro.", 0.3),
    ("[g1]Mein Bad steht unter Wasser!", 0.3, "Gisela"),
    ("[frist]Gisela verlangt die Reparatur und setzt Herrn Kranz eine Frist von zwei Wochen. "
     "[still]Er meldet sich nicht. [werk]Also lässt sie die Maschine in einer Werkstatt reparieren: zweihundert Euro.", 0.3),
    ("[frage]Drei Schäden, ein Händler. [frage2]Welcher Schaden gehört zu welcher Anspruchsgrundlage?", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 280 ----------------------------------------------------------------------------------------------------
    ("[agl]Zentrale Norm ist Paragraf zweihundertachtzig. [w1]Absatz eins: Verletzt der Schuldner eine Pflicht aus dem "
     "Schuldverhältnis, so kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen. [w1b]Dies gilt nicht, "
     "wenn der Schuldner die Pflichtverletzung nicht zu vertreten hat.", P),
    ("[grund]Der Grundtatbestand hat vier Merkmale: [m1]Schuldverhältnis, [m2]Pflichtverletzung, "
     "[m3]Vertretenmüssen [m4]und Schaden. [verm]Das Vertretenmüssen wird vermutet: Der Schuldner muss sich entlasten.", PS),
    ("[w2]Absatz zwei: Schadensersatz wegen Verzögerung der Leistung nur unter der zusätzlichen "
     "Voraussetzung des Paragrafen zweihundertsechsundachtzig. [w3]Absatz drei: Schadensersatz statt der "
     "Leistung nur unter den zusätzlichen Voraussetzungen der Paragrafen zweihunderteinundachtzig, "
     "zweihundertzweiundachtzig oder zweihundertdreiundachtzig.", PS),
    ("[drei]Also drei Arten: [a1]Schadensersatz neben der Leistung, [a2]Verzögerungsschaden, [a3]Schadensersatz "
     "statt der Leistung.", PS),
    # --- D Kontrollfrage -----------------------------------------------------------------------------------------------------
    ("[test]Der Bundesgerichtshof stellt darauf ab, ob eine Nacherfüllung den "
     "Schaden beseitigen würde. [test2]Wenn ja, ist es Schadensersatz statt der Leistung, denn der Schuldner soll zuerst "
     "eine letzte Gelegenheit bekommen. [test3]Bleibt der Schaden trotzdem, ist es Schadensersatz neben der Leistung.", PS),
    # --- E Wasserschaden: neben der Leistung ---------------------------------------------------------------------------------
    ("[wass]Beginnen wir mit dem Wasserschaden. [wass1]Würde eine Reparatur der Maschine den Parkettboden retten? Nein. "
     "[wass2]Also Schadensersatz neben der Leistung. [brueck]Bei einem Mangel führt Paragraf "
     "vierhundertsiebenunddreißig Nummer drei zu Paragraf zweihundertachtzig Absatz eins.", P),
    ("[wp1]Schuldverhältnis: der Kaufvertrag. [wp2]Pflichtverletzung: Herr Kranz hat eine mangelhafte Maschine "
     "geliefert, Paragraf vierhundertdreiunddreißig Absatz eins Satz zwei. [wp3]Vertretenmüssen: vermutet, und er war "
     "unachtsam. [wp4]Schaden: tausendfünfhundert Euro. [wp5]Eine Frist braucht Gisela nicht.", PS),
    # --- F Verzögerungsschaden ------------------------------------------------------------------------------------------------
    ("[verz]Nun die dreißig Euro für den Waschsalon. [verz1]Auch sie würde eine spätere Leistung nicht beseitigen, "
     "denn sie beruhen auf der Verspätung. [verz2]Das ist ein Verzögerungsschaden: Paragrafen zweihundertachtzig "
     "Absatz eins und zwei, zweihundertsechsundachtzig. [verz3]Voraussetzung ist Verzug.", P),
    ("[v1]Die Lieferung war fällig. [v2]Gemahnt hat Gisela nicht, [v3]aber das war entbehrlich: Für die Leistung war eine "
     "Zeit nach dem Kalender bestimmt, Paragraf zweihundertsechsundachtzig Absatz zwei Nummer eins. [v4]Den vergessenen "
     "Termin hat Herr Kranz zu vertreten. [v5]Er schuldet die dreißig Euro.", PS),
    # --- G Schadensersatz statt der Leistung, § 281 ---------------------------------------------------------------------------
    ("[statt]Bleiben die zweihundert Euro für die Reparatur. [statt1]Hätte Herr Kranz nachgebessert, wären sie nie "
     "angefallen. [statt2]Das ist Schadensersatz statt der Leistung, wieder über Paragraf "
     "vierhundertsiebenunddreißig Nummer drei: Paragrafen zweihundertachtzig Absatz eins und drei, zweihunderteinundachtzig.", P),
    ("[w281]Paragraf zweihunderteinundachtzig Absatz eins Satz eins verlangt zweierlei: [w281a]Der Schuldner "
     "erbringt die fällige Leistung nicht oder nicht wie geschuldet. [w281b]Und der Gläubiger hat ihm erfolglos eine "
     "angemessene Frist zur Leistung oder Nacherfüllung bestimmt.", P),
    ("[f1]Die Maschine war mangelhaft, also nicht wie geschuldet. [f2]Die Frist von zwei Wochen "
     "lief ungenutzt ab. [f3]Vertretenmüssen: wieder vermutet. [f4]Ergebnis: zweihundert Euro.", PS),
    # --- H Weitere Wege statt der Leistung: §§ 282, 283, 311a II ---------------------------------------------------------------
    ("[weg]Statt der Leistung gibt es drei weitere Wege. [p282]Paragraf zweihundertzweiundachtzig: Der Schuldner verletzt "
     "eine Rücksichtspflicht, und die Leistung durch ihn ist dem Gläubiger nicht mehr zuzumuten. [p282b]Beispiel der "
     "Gesetzesbegründung: Ein Maler beschädigt bei der Arbeit immer wieder Möbel.", P),
    ("[p283]Paragraf zweihundertdreiundachtzig: Der Schuldner braucht nach Paragraf "
     "zweihundertfünfundsiebzig nicht mehr zu leisten, etwa weil ein verkauftes Einzelstück nach Vertragsschluss "
     "verbrennt. Eine Frist braucht es dann nicht. [p311]Und Paragraf dreihundertelf a Absatz "
     "zwei: Das Hindernis bestand schon bei Vertragsschluss. [p311b]Dann haftet der Schuldner, wenn er es kannte oder "
     "seine Unkenntnis zu vertreten hat.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ordne jeden Schaden einzeln mit der Kontrollfrage zu. [tipp1]Ein typischer "
     "Fehler: den Wasserschaden über Paragraf zweihunderteinundachtzig prüfen [tipp2]und eine Frist verlangen, die es "
     "für Folgeschäden nicht braucht.", PS),
    # --- J Klausurschema als Entscheidungsbaum ----------------------------------------------------------------------------------
    ("[sch]Dein Schema als Entscheidungsbaum. [sb1]Erstens: Welcher Schaden? [sb2]Zweitens: Würde eine Nacherfüllung "
     "ihn beseitigen? [sb3]Wenn nein: Schadensersatz neben der Leistung. [sb4]Beruht er auf der Verspätung: zusätzlich "
     "Verzug, Paragraf zweihundertsechsundachtzig. [sb5]Sonst genügt Paragraf zweihundertachtzig "
     "Absatz eins.", P),
    ("[sb6]Wenn ja: Schadensersatz statt der Leistung. [sb7]Besteht die Leistungspflicht noch: Paragraf "
     "zweihunderteinundachtzig mit Frist, bei Rücksichtspflichten zweihundertzweiundachtzig. [sb8]Entfällt sie nach "
     "Vertragsschluss: zweihundertdreiundachtzig. [sb9]Bestand das Hindernis schon bei Vertragsschluss: dreihundertelf a "
     "Absatz zwei. [sb10]Dann "
     "jeweils: Schuldverhältnis, Pflichtverletzung, Vertretenmüssen, Schaden.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst den Schaden zuordnen, dann die Norm wählen. [merke2]Was eine Nacherfüllung beseitigen würde, gibt "
     "es nur statt der Leistung und grundsätzlich erst nach einer Frist.", 1.4),
]
