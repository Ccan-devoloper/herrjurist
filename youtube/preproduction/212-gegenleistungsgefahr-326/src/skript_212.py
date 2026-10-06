"""Folge 212 · § 326 BGB: Konzert fällt aus – wer trägt die Gegenleistungsgefahr? (Mi · Examenswissen · Zivilrecht/
Schuldrecht AT, Format Schema). Beispielfall nach dem Plan-Hook („Der Pianist wird krank, das gebuchte Privatkonzert fällt
aus – musst du trotzdem zahlen?“): Friedhelm feiert am Samstagabend zu Hause seinen 70. Geburtstag und bucht dafür den
Pianisten Theodor (Privatkonzert, Honorar 2.000 €, 500 € angezahlt, Rest nach dem Konzert). Am Samstagmittag sagt Theodor
ab: hohes Fieber. Ein anderer Termin kommt nicht in Frage (Gäste nur an diesem Abend) → absolutes Fixgeschäft (Fallannahme).
Gegenfall: Theodor ist gesund, Friedhelm sagt am Samstagmittag ab, weil er spontan verreist; Theodor spart 100 € Taxi und
findet keinen anderen Auftritt.
Kern als Schema (Anspruch auf die Gegenleistung): Synallagma; I. entstanden; II. untergegangen nach § 326 Abs. 1 Satz 1
(Wortlautkarte; § 275 Abs. 1 nur verwiesen, Folge 170; absolutes Fixgeschäft, BGH VII ZR 144/22 als Abgrenzung „bloß
verlegt“); III. Ausnahme § 326 Abs. 2 Satz 1 (Wortlautkarte), im Grundfall nein; Gegenfall Satz 1 Alt. 1 ja, Anrechnung
Satz 2 (Wortlautkarte) 2.000 € − 100 € = 1.900 €, offen 1.400 €; Hinweis § 648 BGB (BGH VII ZR 144/22 Rn. 33–39);
IV. Anzahlung § 326 Abs. 4 (Wortlautkarte) mit §§ 346–348, Abs. 5 ein Satz, Abs. 3 ein Satz; Klausurtipp; Schema; Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Theodor (niklas), Friedhelm (helmut); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Theodor": "niklas", "Friedhelm": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Buchung ----------------------------------------------------------------------------------------------
    ("[fall]Friedhelm wird siebzig und feiert am Samstagabend zu Hause. [bucht]Für die Feier bucht er den Pianisten "
     "Theodor: ein Privatkonzert für zweitausend Euro. [anz]Fünfhundert Euro zahlt er gleich an.", P),
    ("[th1]Am Samstagabend spiele ich für Ihre Gäste.", P, "Theodor"),
    ("[fr1]Wunderbar. Den Rest zahle ich nach dem Konzert.", P, "Friedhelm"),
    # --- A2 Fall: das Fieber -----------------------------------------------------------------------------------------------
    ("[krank]Am Samstagmittag ruft Theodor an.", P),
    ("[th2]Ich habe hohes Fieber. Ich kann heute Abend nicht spielen.", P, "Theodor"),
    ("[fr2]Und an einem anderen Tag? Meine Gäste kommen nur heute!", P, "Friedhelm"),
    ("[aus]Das Konzert fällt aus, die Feier lässt sich nicht verschieben. [frage]Muss Friedhelm trotzdem zahlen? "
     "[frage2]Und bekommt er seine Anzahlung zurück?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Synallagma ------------------------------------------------------------------------------------------------------
    ("[syn]Konzert gegen Honorar: Das ist ein gegenseitiger Vertrag. [syn2]Jeder verspricht seine Leistung, weil der "
     "andere seine verspricht. [syn3]Entfällt eine Leistung nach Paragraf zweihundertfünfundsiebzig, dazu das Video zur "
     "Unmöglichkeit, [syn4]fragt sich: Was wird aus der Gegenleistung? [syn5]Das ist die Frage der Gegenleistungsgefahr, "
     "auch Preisgefahr genannt.", PS),
    # --- D Aufbau ----------------------------------------------------------------------------------------------------------
    ("[plan]Wir prüfen den Anspruch von Theodor auf das Honorar. [p1]Römisch eins: entstanden? [p2]Römisch zwei: "
     "untergegangen nach Paragraf dreihundertsechsundzwanzig Absatz eins? [p3]Römisch drei: ausnahmsweise erhalten nach "
     "Absatz zwei? [p4]Römisch vier: Was wird aus der Anzahlung?", PS),
    # --- E I. entstanden ---------------------------------------------------------------------------------------------------
    ("[e1]Römisch eins: Mit dem Vertrag ist der Anspruch auf zweitausend Euro entstanden.", P),
    # --- F II. § 326 Abs. 1 Satz 1 (Wortlaut) ------------------------------------------------------------------------------
    ("[w326]Römisch zwei. Paragraf dreihundertsechsundzwanzig Absatz eins Satz eins: Braucht der Schuldner nach Paragraf "
     "zweihundertfünfundsiebzig Absatz eins bis drei nicht zu leisten, entfällt der Anspruch auf die Gegenleistung.", P),
    # --- G II. im Fall: persönlich, absolutes Fixgeschäft, unmöglich -------------------------------------------------------
    ("[u1]Schuldner des Konzerts ist Theodor. [u2]Er muss persönlich spielen und kann es mit Fieber nicht. [u3]Unmöglich "
     "ist das Konzert aber nur, wenn es sich nicht nachholen lässt. [u4]Der Bundesgerichtshof hat entschieden: Wird eine "
     "Hochzeit wegen Corona-Auflagen verlegt, wird die Leistung der Fotografin dadurch nicht unmöglich. [u5]Hier aber gibt "
     "es die Feier nur an diesem Abend. Ein späteres Konzert wäre für Friedhelm wertlos: ein absolutes Fixgeschäft. "
     "[u6]Mit dem Abend ist die Leistung unmöglich, Paragraf zweihundertfünfundsiebzig Absatz eins. [u7]Also entfällt der "
     "Anspruch auf das Honorar. Die Gegenleistungsgefahr trägt Theodor.", PS),
    # --- H III. § 326 Abs. 2 Satz 1 (Wortlaut), Grundfall ------------------------------------------------------------------
    ("[w2]Römisch drei: die Ausnahme in Absatz zwei Satz eins. [w2a]Der Schuldner behält den Anspruch, wenn der Gläubiger "
     "für den Umstand allein oder weit überwiegend verantwortlich ist, [w2b]oder wenn ein Umstand, den der Schuldner nicht "
     "zu vertreten hat, im Annahmeverzug des Gläubigers eintritt.", P),
    ("[g1]Für das Fieber ist Friedhelm nicht verantwortlich. [g2]Im Annahmeverzug war er auch nicht, denn Theodor hat ihm "
     "kein Konzert angeboten. [g3]Friedhelm muss also nichts mehr zahlen.", PS),
    # --- I Gegenfall: Friedhelm sagt ab ------------------------------------------------------------------------------------
    ("[gf]Jetzt der Gegenfall: Theodor ist gesund. [gf2]Doch am Samstagmittag ruft Friedhelm an, er will spontan "
     "verreisen.", P),
    ("[fr3]Die Feier fällt aus. Ich brauche Sie heute nicht.", P, "Friedhelm"),
    ("[gf3]Mit dem Abend ist das Konzert wieder unmöglich. [gf4]Diesmal ist aber Friedhelm allein verantwortlich. "
     "[gf5]Theodor behält den Anspruch auf die zweitausend Euro.", P),
    # --- J III. § 326 Abs. 2 Satz 2 (Wortlaut), Anrechnung, Hinweis § 648 --------------------------------------------------
    ("[w22]Er muss sich nach Satz zwei aber anrechnen lassen, was er infolge der Befreiung von der Leistung erspart oder "
     "durch anderweitige Verwendung seiner Arbeitskraft erwirbt oder zu erwerben böswillig unterlässt. [an1]Theodor spart "
     "die Taxifahrt, hundert Euro. [an2]Einen anderen Auftritt findet er so kurzfristig nicht. [an3]Es bleiben "
     "neunzehnhundert Euro, [an4]abzüglich der Anzahlung sind noch vierzehnhundert offen.", P),
    ("[k648]Achtung: Beim Werkvertrag kann eine solche Absage auch eine Kündigung nach Paragraf sechshundertachtundvierzig "
     "sein. [k648b]Auch dort wird die Ersparnis abgezogen; so billigte es der Bundesgerichtshof bei der "
     "Hochzeitsfotografin.", PS),
    # --- K IV. § 326 Abs. 4 (Wortlaut), Abs. 5, Abs. 3 ---------------------------------------------------------------------
    ("[w4]Römisch vier, zurück zum Grundfall. Paragraf dreihundertsechsundzwanzig Absatz vier: Soweit die nach dieser "
     "Vorschrift nicht geschuldete Gegenleistung bewirkt ist, kann das Geleistete nach den Paragrafen "
     "dreihundertsechsundvierzig bis dreihundertachtundvierzig zurückgefordert werden. [r1]Friedhelm bekommt seine "
     "fünfhundert Euro zurück. [r2]Zurücktreten muss er dafür nicht. [r3]Er kann es aber nach Absatz fünf, ohne Frist. "
     "[r4]Und Absatz drei: Verlangt der Gläubiger nach Paragraf zweihundertfünfundachtzig einen Ersatz, bleibt er zur "
     "Gegenleistung verpflichtet.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Reihenfolge ein. [t1]Erst der Primäranspruch: Ist er nach Paragraf "
     "zweihundertfünfundsiebzig ausgeschlossen? [t2]Dann die Gegenleistung nach Paragraf dreihundertsechsundzwanzig Absatz "
     "eins, [t3]zuletzt die Ausnahmen in Absatz zwei.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Anspruch auf die Gegenleistung: [k1]Römisch eins: Anspruch entstanden. [k2]Römisch zwei: "
     "Anspruch untergegangen nach Paragraf dreihundertsechsundzwanzig Absatz eins, [k21]weil der Schuldner nach Paragraf "
     "zweihundertfünfundsiebzig nicht leisten muss. [k3]Römisch drei: ausnahmsweise erhalten nach Absatz zwei, [k31]wenn der "
     "Gläubiger allein oder weit überwiegend verantwortlich oder im Annahmeverzug ist, [k32]abzüglich der Ersparnis. [k4]Römisch vier: Rückforderung "
     "des Gezahlten nach Absatz vier.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Muss der Schuldner nach Paragraf zweihundertfünfundsiebzig nicht leisten, entfällt grundsätzlich die "
     "Gegenleistung. [mk2]Ist der Gläubiger dafür verantwortlich oder im Annahmeverzug, [mk3]behält der Schuldner sie, "
     "abzüglich der Ersparnis.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
