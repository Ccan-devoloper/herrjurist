"""Folge 047 · Vermögensdelikte Überblick: Diebstahl, Betrug, Raub, Erpressung (Mi · Examenswissen, Format Schema).
Überblicksfolge als Landkarte: Dagmars kleiner Laden für gebrauchte Kameras; Klaus will die Kamera im Schaufenster, ohne
zu bezahlen. Sieben kurze, gewaltarme Varianten (Drohung nur verbal). Eigentumsdelikte (§ 242 Wortlaut, BGH 4 StR 338/20
Rn. 5; § 246, BGH 6 StR 191/23 Rn. 5, 12 und 4 StR 442/23 Rn. 11; § 249 Wortlaut, BGH 5 StR 606/17 Rn. 10, 13) und
Vermögensdelikte (§ 263 Wortlaut; Sachbetrug/Trickdiebstahl BGH 1 StR 402/16 Rn. 10–14; §§ 253, 255; § 266 kurz,
BGH 4 StR 456/22 Rn. 28). Streit Raub/räuberische Erpressung: Rspr. äußeres Erscheinungsbild (BGH 6 StR 44/23 Rn. 5;
BGHSt 41, 123 Rn. 12, 14), Lehre Vermögensverfügung/Schlüsselstellung; Auffangfall fehlende Zueignungsabsicht
(BGH 1 StR 75/24 Rn. 9). Klausurtipp, Entscheidungsbaum, Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.6

STIMMEN = {"Klaus": "stephan", "Dagmar": "sabrina"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Kameraladen ---------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag in der Altstadt. [dagmar]Dagmar verkauft in ihrem kleinen Laden gebrauchte Kameras. "
     "[kamera]Ihr schönstes Stück ist eine alte Spiegelreflexkamera für dreihundert Euro. [klaus]Klaus gefällt sie, "
     "aber bezahlen will er nicht.", 0.3),
    ("[k1]Die Kamera kriege ich schon, so oder so.", 0.4, "Klaus"),
    ("[frage]Genau darauf kommt es an. [frage2]Ob Diebstahl, Betrug, Raub oder Erpressung, entscheidet vor "
     "allem, wie Klaus an die Kamera kommt.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier sind alle sieben Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Landkarte -----------------------------------------------------------------------------------------------------
    ("[karte]Die Landkarte hat zwei Säulen. [eigen]Links die Eigentumsdelikte: Diebstahl, Unterschlagung und Raub. "
     "[eig2]Sie schützen das Eigentum an einer fremden beweglichen Sache; ein Vermögensschaden ist nicht nötig. "
     "[verm]Rechts die Vermögensdelikte: Betrug, Erpressung, räuberische Erpressung und Untreue. [verm2]Hier muss das "
     "Vermögen einen Schaden erleiden. [bruecke]Raub und räuberische Erpressung verlangen zusätzlich Gewalt gegen eine "
     "Person oder eine Drohung mit gegenwärtiger Gefahr für Leib oder Leben.", PS),
    # --- D Diebstahl -------------------------------------------------------------------------------------------------------
    ("[p242]Erstes Feld: Diebstahl, Paragraf zweihundertzweiundvierzig. [p242w]Wer eine fremde bewegliche Sache einem "
     "anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe "
     "bis zu fünf Jahren oder mit Geldstrafe bestraft. [wegn]Wegnahme heißt nach dem Bundesgerichtshof: fremden Gewahrsam "
     "brechen und neuen begründen. [bruch]Gebrochen wird er ohne oder gegen den Willen des Inhabers. "
     "[v1]In Variante eins steckt Klaus die Kamera unbemerkt ein und geht. [v1ok]Diebstahl.", PS),
    # --- E Unterschlagung ------------------------------------------------------------------------------------------------
    ("[p246]Und wenn Klaus die Kamera schon in der Hand hat? [v2]In Variante zwei leiht Dagmar sie ihm. Erst später "
     "beschließt er, sie zu verkaufen, und tut das. [keinew]Eine Wegnahme fehlt, denn Dagmar hat ihm die Kamera selbst überlassen. "
     "[p246b]Hier greift die Unterschlagung, Paragraf zweihundertsechsundvierzig: Zueignung ohne Wegnahme. [zueig]Wie "
     "viel dafür nötig ist, sehen die Strafsenate unterschiedlich; ein Verkauf genügt jedenfalls. "
     "[anv]Weil ihm die Kamera anvertraut war, droht nach Absatz zwei eine höhere Strafe.", PS),
    # --- F Raub ----------------------------------------------------------------------------------------------------------
    ("[p249]Unten links steht der Raub, Paragraf zweihundertneunundvierzig. [p249w]Er ist ein Diebstahl mit Gewalt gegen "
     "eine Person oder unter Drohungen mit gegenwärtiger Gefahr für Leib oder Leben. [final]Das Nötigungsmittel muss "
     "die Wegnahme ermöglichen sollen. [v5]In Variante drei droht Klaus Dagmar Schläge an.", 0.3),
    ("[k3]Keine Bewegung, sonst gibt es Schläge!", 0.3, "Klaus"),
    ("[v5b]Dann nimmt er die Kamera selbst aus dem Regal. [v5ok]Raub, mit Freiheitsstrafe nicht unter einem Jahr.", PS),
    # --- G Betrug --------------------------------------------------------------------------------------------------------
    ("[p263]Rechte Säule: Betrug, Paragraf zweihundertdreiundsechzig. [p263w]Er verlangt Täuschung, Irrtum, "
     "Vermögensverfügung und Schaden, dazu Vorsatz und Bereicherungsabsicht. [v3]In Variante vier behauptet Klaus, "
     "Dagmars Bruder habe die Kamera schon bezahlt und ihn zum Abholen geschickt.", 0.3),
    ("[d1]Ach so, dann nehmen Sie sie mit.", 0.3, "Dagmar"),
    ("[verf]Dagmar glaubt ihm und will ihm den Gewahrsam übertragen: eine Vermögensverfügung. [v3ok]Das ist Sachbetrug.", PS),
    # --- H Trickdiebstahl ------------------------------------------------------------------------------------------------
    ("[trick]Ganz anders Variante fünf.", 0.3),
    ("[k2]Darf ich mal kurz durchschauen?", 0.3, "Klaus"),
    ("[v4]Dagmar reicht ihm die Kamera, er rennt damit hinaus. [locker]Auch hier täuscht Klaus, doch Dagmar will die "
     "Kamera sofort zurück. [mitgew]Nach dem Bundesgerichtshof lockert sie den Gewahrsam nur. [v4ok]Erst beim "
     "Weglaufen bricht Klaus ihn: Trickdiebstahl. [wille]Entscheidend ist die Willensrichtung der Getäuschten: Gibt sie "
     "die Sache weg, ist es Betrug; nimmt der Täter, ist es Diebstahl.", PS),
    # --- I Erpressung ----------------------------------------------------------------------------------------------------
    ("[p253]Bei Erpressung, Paragraf zweihundertdreiundfünfzig, nötigt der Täter jemanden mit Gewalt oder durch Drohung "
     "mit einem empfindlichen Übel zu einer Handlung, Duldung oder Unterlassung. [nacht]Dadurch entsteht ein "
     "Vermögensnachteil, und der Täter will sich zu Unrecht bereichern. [v7]In Variante sechs droht Klaus, den Laden "
     "von Dagmar im Internet mit erfundenen Vorwürfen schlechtzumachen. [v7b]Dagmar verkauft ihm die Kamera deshalb für zehn "
     "Euro. [v7ok]Der drohende Rufschaden ist ein empfindliches Übel, das Mittel verwerflich: "
     "Erpressung. [p255]Setzt der Täter dagegen Gewalt gegen eine Person ein oder droht er mit Gefahr für Leib oder Leben, wird er nach Paragraf "
     "zweihundertfünfundfünfzig gleich einem Räuber bestraft: räuberische Erpressung.", PS),
    # --- J Streit Raub / räuberische Erpressung --------------------------------------------------------------------------
    ("[streit]Und Variante sieben? Wieder droht Klaus Schläge an, [v6]doch diesmal reicht Dagmar ihm die Kamera. "
     "[rspr]Der Bundesgerichtshof grenzt nach dem äußeren Erscheinungsbild ab: Nimmt der Täter, ist es Raub; gibt das "
     "Opfer, ist es räuberische Erpressung. [rspr2]Eine Vermögensverfügung verlangt er nicht, der Raub ist für ihn ein "
     "Sonderfall der Erpressung. [v6ok]Variante sieben ist danach räuberische Erpressung. [lehre]Die wohl überwiegende Lehre "
     "verlangt dagegen eine Vermögensverfügung. [lehre2]Wer jedes willentliche Geben genügen lässt, kommt hier ebenfalls zur räuberischen Erpressung. [schl]Ein Teil fragt nach der Schlüsselstellung: Glaubt Dagmar, Klaus "
     "bekomme die Kamera ohnehin, gilt ihr Geben als Wegnahme, [schl2]und es bleibt beim Raub.", PS),
    # --- K Untreue -------------------------------------------------------------------------------------------------------
    ("[p266]Zuletzt die Untreue, Paragraf zweihundertsechsundsechzig. [p266b]Sie trifft nur, wem eine "
     "Vermögensbetreuungspflicht obliegt, [p266c]etwa einen Vermögensverwalter, der das Geld seiner Kundin für sich "
     "ausgibt. [p266d]Klaus betreut Dagmars Vermögen nicht.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Entscheide den Streit nur, wo er sich auswirkt. [tipp2]Nimmt der Täter mit Zueignungsabsicht, "
     "kommen alle Ansichten zum Raub. [tipp3]Nimmt Klaus die Kamera unter Drohung, will sie aber nur ein Wochenende benutzen, fehlt die "
     "Zueignungsabsicht. [tipp4]Dann hilft der Bundesgerichtshof mit der räuberischen Erpressung, wenn Klaus sich durch "
     "den Gebrauch bereichern will; nach der Lehre fehlt die Verfügung.", PS),
    # --- M Entscheidungsbaum ---------------------------------------------------------------------------------------------
    ("[sch]Dein Entscheidungsbaum. [e1]Erste Frage: Nimmt der Täter die Sache? [e1a]Dann Diebstahl, [e1b]mit Gewalt "
     "oder Drohung für Leib oder Leben Raub. [e2]Zweite Frage: Hat er sie schon und eignet sie sich zu? Dann Unterschlagung. [e3]Dritte "
     "Frage: Gibt das Opfer? [e3a]Getäuscht ist es Betrug, [e3b]genötigt Erpressung, [e3c]mit Gewalt oder Drohung für "
     "Leib oder Leben räuberische Erpressung. [e4]Vierte Frage: Betreut der Täter fremdes Vermögen? Dann Untreue.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Nehmen ist Diebstahl, mit Gewalt oder Drohung für Leib oder Leben Raub. [m2]Geben nach Täuschung ist Betrug, Geben "
     "unter Zwang Erpressung. [m3]Und wer die Sache schon hat und sie sich zueignet, begeht Unterschlagung.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
