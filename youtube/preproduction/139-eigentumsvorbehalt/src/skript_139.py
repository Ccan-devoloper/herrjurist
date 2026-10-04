"""Folge 139 · Eigentumsvorbehalt: Das Sofa ist da, gehört aber dem Möbelhaus (Mo · Der Fall · Zivilrecht/Sachenrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Das auf Raten gekaufte Sofa steht in deinem Wohnzimmer – der Kaufvertrag
sagt: Eigentum bleibt beim Händler.“): Sonja kauft in einem Möbelhaus (Verkäufer Herr Schuster) ein Sofa für 2.400 €, zahlbar
in 12 Monatsraten zu je 200 €, mit Eigentumsvorbehalt bis zur vollständigen Zahlung. Das Sofa wird geliefert. Nach fünf Raten
(1.000 €) zahlt Sonja nicht mehr. Herr Schuster ruft an: Das Sofa gehöre noch dem Möbelhaus, man hole es am Montag ab. Eine
Frist hat das Möbelhaus nicht gesetzt.
Kern als Schema: 1. Trennungsprinzip – Kaufvertrag § 433 unbedingt, Übereignung § 929 S. 1 aufschiebend bedingt (Wortlautkarten
§ 449 Abs. 1, § 158 Abs. 1); 2. Anwartschaftsrecht (BGH V ZR 143/24 Rn. 16); 3. Herausgabe: § 985 (Wortlaut), Recht zum
Besitz aus dem Kaufvertrag § 986 Abs. 1 (BGH IX ZR 128/12 Rn. 11), § 449 Abs. 2 (Wortlautkarte), Rücktritt § 323 mit Frist
(Verweis 116), Teilzahlungsgeschäft §§ 506, 508 nur offen, Rückgewähr §§ 346 ff.; Ergebnis; Klausurtipp (Bedingungseintritt
mit der letzten Rate, § 158 Abs. 1; verlängerter/erweiterter EV nur genannt); Schema; Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Sonja (ela_froh), Herr Schuster (helmut); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Sonja": "ela_froh", "Schuster": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: im Möbelhaus ---------------------------------------------------------------------------------------------
    ("[fall]Sonja kauft in einem Möbelhaus ein Sofa für zweitausendvierhundert Euro. [raten]Sie zahlt in zwölf Monatsraten "
     "zu je zweihundert Euro. [klausel]Verkäufer Herr Schuster zeigt ihr einen Satz im Kaufvertrag.", 0.25),
    ("[sc1]Bis zur letzten Rate bleibt das Sofa Eigentum des Möbelhauses.", 0.3, "Schuster"),
    # --- A2 Fall: das Sofa im Wohnzimmer ----------------------------------------------------------------------------------
    ("[liefer]Das Sofa wird geliefert und steht nun in ihrem Wohnzimmer.", 0.25),
    ("[so1]Endlich ein eigenes Sofa!", 0.3, "Sonja"),
    # --- A3 Fall: die Raten bleiben aus, der Anruf -------------------------------------------------------------------------
    ("[fuenf]Fünf Raten zahlt Sonja pünktlich, zusammen tausend Euro. [stopp]Dann zahlt sie nicht mehr. "
     "[anruf]Herr Schuster ruft an.", 0.25),
    ("[sc2]Das Sofa gehört noch uns. Wir holen es am Montag ab.", 0.25, "Schuster"),
    ("[so2]Aber ich habe das Sofa doch gekauft!", 0.3, "Sonja"),
    ("[frage]Wer ist Eigentümer des Sofas? [frage2]Und darf das Möbelhaus es einfach abholen?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.8),
    # --- C Aufbau -----------------------------------------------------------------------------------------------------------
    ("[plan]Wir gehen in drei Schritten vor: [s1]Erstens, wie der Eigentumsvorbehalt konstruiert ist. [s2]Zweitens, welche "
     "Rechtsposition Sonja schon hat. [s3]Drittens, ob das Möbelhaus das Sofa herausverlangen kann.", PS),
    # --- D 1. Trennungsprinzip ------------------------------------------------------------------------------------------------
    ("[tr1]Erstens: das Trennungsprinzip. Kaufvertrag und Übereignung sind zwei verschiedene Geschäfte. [kv]Der Kaufvertrag "
     "nach Paragraf vierhundertdreiunddreißig ist unbedingt: Das Möbelhaus muss liefern und übereignen, Sonja muss zahlen. "
     "[ueb]Die Übereignung nach Paragraf neunhundertneunundzwanzig Satz eins steht dagegen unter einer aufschiebenden "
     "Bedingung. [ueb2]Einigung und Übergabe liegen mit der Lieferung vor, nur die Wirkung tritt noch nicht ein.", P),
    # --- E Wortlaut § 449 Abs. 1 und § 158 Abs. 1 ---------------------------------------------------------------------------
    ("[w449]So sieht es Paragraf vierhundertneunundvierzig Absatz eins vor: Hat sich der Verkäufer einer beweglichen Sache "
     "das Eigentum bis zur Zahlung des Kaufpreises vorbehalten, so ist im Zweifel anzunehmen, dass das Eigentum unter der "
     "aufschiebenden Bedingung vollständiger Zahlung des Kaufpreises übertragen wird.", P),
    ("[w158]Und Paragraf hundertachtundfünfzig Absatz eins: Wird ein Rechtsgeschäft unter einer aufschiebenden Bedingung "
     "vorgenommen, so tritt die von der Bedingung abhängig gemachte Wirkung mit dem Eintritt der Bedingung ein. "
     "[bed]Die Bedingung ist hier die vollständige Zahlung: zweitausendvierhundert Euro. [bisher]Gezahlt sind erst tausend. "
     "[eig1]Also ist das Möbelhaus noch Eigentümer des Sofas.", PS),
    # --- F 2. Anwartschaftsrecht ---------------------------------------------------------------------------------------------
    ("[anw]Zweitens: Sonja steht trotzdem nicht mit leeren Händen da. Sie hat ein Anwartschaftsrecht. [anw2]Nach dem "
     "Bundesgerichtshof entsteht es, wenn schon so viele Erfordernisse erfüllt sind, dass der andere Teil den Erwerb nicht "
     "mehr durch einseitige Erklärung zerstören kann. [anw3]Es ist ein dem Volleigentum wesensähnliches Recht. "
     "[anw4]Zahlt Sonja die restlichen Raten, wird sie Eigentümerin, ob das Möbelhaus will oder nicht.", PS),
    # --- G 3. Herausgabe: § 985, § 986 Abs. 1 --------------------------------------------------------------------------------
    ("[her]Drittens: die Herausgabe. Anspruchsgrundlage ist Paragraf neunhundertfünfundachtzig: [w985]Der Eigentümer kann "
     "von dem Besitzer die Herausgabe der Sache verlangen. [h1]Das Möbelhaus ist Eigentümer. [h2]Sonja ist Besitzerin, "
     "das Sofa steht in ihrer Wohnung. [h3]Aber nach Paragraf neunhundertsechsundachtzig Absatz eins kann sie die "
     "Herausgabe verweigern, wenn sie dem Eigentümer gegenüber zum Besitz berechtigt ist. [h4]Ihr Recht zum Besitz folgt "
     "aus dem Kaufvertrag. Es besteht, bis das Möbelhaus wirksam vom Vertrag zurücktritt.", P),
    # --- H § 449 Abs. 2 (Wortlaut) -------------------------------------------------------------------------------------------
    ("[w4492]Deshalb sagt Paragraf vierhundertneunundvierzig Absatz zwei: Auf Grund des Eigentumsvorbehalts kann der "
     "Verkäufer die Sache nur herausverlangen, wenn er vom Vertrag zurückgetreten ist. [nurev]Der Vorbehalt allein "
     "genügt also nicht.", PS),
    # --- I Rücktritt, Teilzahlungsgeschäft, Rückgewähr -----------------------------------------------------------------------
    ("[rt1]Für den Rücktritt braucht das Möbelhaus ein Rücktrittsrecht, hier aus Paragraf dreihundertdreiundzwanzig: Es muss "
     "Sonja erfolglos eine angemessene Frist zur Zahlung setzen. Mehr dazu im Video zum Rücktritt. [tz]Ob zusätzlich die "
     "Verbraucherregeln zum entgeltlichen Teilzahlungsgeschäft gelten, lassen wir offen; dann dürfte das Möbelhaus wegen "
     "Zahlungsverzugs nur unter den strengeren Voraussetzungen von Paragraf fünfhundertacht zurücktreten. "
     "[rg]Nach einem wirksamen Rücktritt wird rückabgewickelt, Paragrafen dreihundertsechsundvierzig und folgende: Sonja gibt das "
     "Sofa zurück und leistet Wertersatz für die Nutzung, das Möbelhaus zahlt die tausend Euro zurück.", PS),
    # --- J Ergebnis -----------------------------------------------------------------------------------------------------------
    ("[erg]Im Fall heißt das: [erg1]Eigentümer des Sofas ist noch das Möbelhaus. [erg2]Eine Frist hat es Sonja nicht "
     "gesetzt, wirksam zurückgetreten ist es also nicht. [erg3]Sonja darf das Sofa vorerst behalten, das Möbelhaus darf es nicht gegen ihren Willen abholen. "
     "[erg4]Es kann aber die fälligen Raten verlangen. [erg5]Erst nach einem wirksamen Rücktritt kann es das Sofa herausverlangen, "
     "nach Paragraf neunhundertfünfundachtzig und nach Paragraf dreihundertsechsundvierzig Absatz eins.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Mit der letzten Rate geht das Eigentum automatisch über. [tipp2]Eine neue Einigung oder Erklärung "
     "braucht es nicht, denn die Bedingung tritt ein, Paragraf hundertachtundfünfzig Absatz eins. [tipp3]Und merke dir zwei "
     "Begriffe für später: den verlängerten und den erweiterten Eigentumsvorbehalt.", PS),
    # --- L Klausurschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Herausgabeanspruch des Vorbehaltsverkäufers: [k1]Römisch eins: Eigentum des Verkäufers. "
     "[k11]Die Übereignung ist aufschiebend bedingt, [k12]die Bedingung ist noch nicht eingetreten, der Käufer hat nur das "
     "Anwartschaftsrecht. [k2]Römisch zwei: Besitz des Käufers. [k3]Römisch drei: kein Recht zum Besitz. [k31]Das Recht "
     "aus dem Kaufvertrag [k32]endet erst mit dem wirksamen Rücktritt. [k4]Daneben: Rückgewähr nach Paragraf "
     "dreihundertsechsundvierzig.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim Eigentumsvorbehalt ist der Kauf unbedingt, nur die Übereignung ist bedingt. [mk2]Das Eigentum "
     "geht erst mit der letzten Rate über. [mk3]Und zurückholen darf der Verkäufer die Sache erst nach dem Rücktritt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
