"""Folge 019 · Sitzblockade Nötigung: Klimakleber & die Zweite-Reihe-Rechtsprechung.
Fiktiver Fall (Personen erfunden, keine reale Gruppe): Sitzblockade mit Festkleben auf einer Hauptstraße im Berufsverkehr.
Linie: BVerfGE 92, 1 (Art. 103 II GG) → BGHSt 41, 182 (Zweite Reihe) → BVerfG (K) 1 BvR 388/05 (Billigung, mittelbare
Täterschaft) → BVerfGE 104, 92 (Anketten = Gewalt; Verwerflichkeit mit Art. 8 GG) → Obergerichte zu Klimablockaden
(OLG Karlsruhe 2024/2025, KG 2024, BayObLG 2024/2025). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad.
Politisch neutral: das Anliegen der Gruppe wird nicht bewertet."""

P, PS = 0.4, 0.9

STIMMEN = {"Hanna": "lucy", "Lukas": "timo", "Dieter": "stephan", "Sabine": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Blockade ------------------------------------------------------------------------------------------
    ("[fall]Montag, acht Uhr, Berufsverkehr auf der Ringstraße. [sitzen]Vier Menschen setzen sich nach gemeinsamem Plan quer über alle "
     "Spuren auf die Fahrbahn. [kleben]Hanna drückt ihre Hand mit Sekundenkleber auf den Asphalt. [lukas]Lukas sitzt nur daneben.", 0.3),
    ("[h1]Wir bleiben hier sitzen. Für mehr Klimaschutz!", 0.4, "Hanna"),
    # --- B Fall: die erste Reihe ------------------------------------------------------------------------------------------
    ("[dieter]Dieter kommt als Erster und bremst.", 0.2),
    ("[d1]Ich kann doch nicht über Menschen fahren!", 0.4, "Dieter"),
    # --- C Fall: die zweite Reihe --------------------------------------------------------------------------------------
    ("[sabine]Hinter ihm hält Sabine, dahinter staut es sich über einen Kilometer. [eng]Links ist eine Mittelinsel, "
     "rechts der Gehweg.", 0.2),
    ("[s1]Vor mir ein Auto, hinter mir ein Auto. Ich komme hier nicht weg.", 0.4, "Sabine"),
    ("[polizei]Angekündigt war die Aktion nicht. Erst nach fünfzig Minuten hat die Polizei die Hand von Hanna gelöst "
     "und die Straße geräumt. [frage]Haben sich die vier wegen Nötigung strafbar gemacht?", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Gewalt: erste Reihe ------------------------------------------------------------------------------------------
    ("[pruef]Wir prüfen Nötigung, Paragraf zweihundertvierzig. [gewalt]Das erste Problem ist die Gewalt. [def]Gewalt ist körperlich wirkender Zwang. "
     "[alt]Früher genügte der Rechtsprechung schon die bloße Anwesenheit auf der Fahrbahn, wenn sie andere psychisch hemmte: "
     "der sogenannte vergeistigte Gewaltbegriff.", P),
    ("[bv95]Das Bundesverfassungsgericht hat das neunzehnhundertfünfundneunzig verworfen. [anwesend]Wer nur körperlich anwesend "
     "ist und bloß psychischen Zwang ausübt, wendet keine Gewalt an. [art103]Sonst verletzt die Auslegung Artikel "
     "hundertdrei Absatz zwei Grundgesetz.", P),
    ("[dieter2]Dieter hält, weil er niemanden verletzen will. Das bloße Sitzen ist ihm gegenüber also keine Gewalt.", PS),
    # --- F Gewalt: zweite Reihe -----------------------------------------------------------------------------------------
    ("[zweite]Anders bei Sabine. Der Bundesgerichtshof hat neunzehnhundertfünfundneunzig die Zweite-Reihe-Rechtsprechung "
     "entwickelt. [hindernis]Für Sabine ist das Auto von Dieter ein echtes, körperliches Hindernis. [werkzeug]Die Blockierer "
     "benutzen das erste Auto als Werkzeug.", P),
    ("[bv11]Das Bundesverfassungsgericht hat das zweitausendelf gebilligt, als Gewalt in mittelbarer Täterschaft.", PS),
    # --- G Festkleben -----------------------------------------------------------------------------------------------
    ("[kleber]Und das Festkleben? [kette]Schon zweitausendeins hielt es das Bundesverfassungsgericht für zulässig, im "
     "Anketten Gewalt zu sehen, weil eine echte Barriere entsteht. [olg]Das Oberlandesgericht Karlsruhe hat zweitausendfünfundzwanzig auch das Festkleben "
     "als Gewalt eingeordnet. [erste]Folgt man dem, käme es auf die zweite Reihe gar nicht mehr an.", P),
    ("[offen]Das Bayerische Oberste Landesgericht hat diese Frage offengelassen. Höchstrichterlich ist sie, soweit "
     "ersichtlich, nicht geklärt.", PS),
    # --- H Mittäterschaft, Erfolg, Vorsatz --------------------------------------------------------------------------
    ("[lukas2]Lukas klebt nicht. Er handelt aber nach einem gemeinsamen Plan und ist Mittäter, Paragraf fünfundzwanzig "
     "Absatz zwei. [erfolg]Der Nötigungserfolg liegt vor: Sabine muss warten. [vorsatz]Vorsatz haben alle vier.", PS),
    # --- I Rechtswidrigkeit ----------------------------------------------------------------------------------------
    ("[rw]Zur Rechtswidrigkeit. [not]Einen Notstand nach Paragraf vierunddreißig lehnen die Oberlandesgerichte ab. "
     "[art8]Die Sitzblockade ist zwar eine Versammlung nach Artikel acht Grundgesetz. "
     "[friedlich]Sie bleibt friedlich, auch wenn sie andere behindert. [kein]Das rechtfertigt die Tat aber "
     "nicht, sondern wirkt bei der Verwerflichkeit, Paragraf zweihundertvierzig Absatz zwei.", P),
    ("[abw]Abzuwägen sind nach dem Bundesverfassungsgericht vor allem Dauer und Intensität, die vorherige Bekanntgabe, "
     "Ausweichmöglichkeiten, die Dringlichkeit der Fahrten und der Sachbezug zum Protestthema. [inhalt]Das politische "
     "Anliegen selbst darf das Gericht nicht bewerten.", P),
    # --- J Abwägung im Fall, Ergebnis ------------------------------------------------------------------------------
    ("[subs]Hier: fünfzig Minuten im Berufsverkehr, unangekündigt, kein Ausweichen. [sach]Einen Sachbezug zum Autoverkehr "
     "gibt es nur teilweise. [verw]Mit den Oberlandesgerichten bejahen wir die Verwerflichkeit.", P),
    ("[schuld]Schuld liegt vor. [erg]Alle vier sind wegen Nötigung strafbar, jedenfalls gegenüber Sabine und den Fahrern "
     "hinter ihr.", P),
    ("[gegen]Gegenfall: Eine kurze, vorher bekannt gegebene Blockade mit Umleitung wiegt viel leichter. "
     "[gegen2]Dort kann die Verwerflichkeit fehlen.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Gewalt getrennt für jede Reihe. [tipp1]In der ersten Reihe wirkt nur psychischer Zwang, "
     "es sei denn, du siehst schon im Festkleben Gewalt. [tipp2]Ab der zweiten Reihe hilft die Zweite-Reihe-Rechtsprechung. "
     "[tipp3]Und Artikel acht gehört in die Verwerflichkeit, nicht in einen eigenen Rechtfertigungsgrund.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand: [k1a]erstens Gewalt, getrennt nach erster und zweiter Reihe, "
     "[k1b]zweitens der Nötigungserfolg, [k1c]drittens der Vorsatz.", P),
    ("[k2]Römisch zwei, Rechtswidrigkeit: [k2a]keine Rechtfertigung, [k2b]dann die Verwerflichkeit nach Absatz zwei, mit "
     "Artikel acht in der Abwägung. [k3]Römisch drei, Schuld.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Sitzen allein ist keine Gewalt. [m2]Wer aber das erste Auto zur Barriere macht, nötigt die Fahrer "
     "dahinter. [m3]Ob das rechtswidrig ist, entscheidet die Verwerflichkeit.", 1.4),
]
