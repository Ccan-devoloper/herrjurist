"""Folge 170 · Unmöglichkeit § 275 BGB: Wenn die Leistung nicht mehr geht (Mi · Examenswissen · Zivilrecht/Schuldrecht AT,
Format Schema). Beispielfall nach dem Plan-Hook („Der verkaufte Oldtimer brennt eine Nacht vor der Übergabe aus.“):
Waldemar verkauft Adelheid privat seinen Oldtimer (Stückschuld) für 20.000 €; Übergabe und Zahlung am Samstag. In der
Nacht davor brennt es in der Garage von Waldemar, der Wagen brennt aus. Variante A: Blitzschlag (kein Verschulden).
Variante B: Waldemar hat am Abend in der Garage mit offener Flamme hantiert (fahrlässig). Marktwert des Wagens 25.000 €;
die Versicherung von Waldemar zahlt ihm für den Wagen 25.000 €.
Kern als Schema: I. Primäranspruch § 433 Abs. 1 ausgeschlossen nach § 275 Abs. 1 (Wortlautkarte; Stückschuld, objektiv/
subjektiv, nachträglich; § 311a Abs. 1 ein Satz; kraft Gesetzes; § 275 Abs. 2, 3 als Einrede; BT-Drucks. 14/6040 S. 129);
II. Gegenleistung § 326 Abs. 1 Satz 1 (Wortlautkarte), Ausnahmen § 326 Abs. 2, Gefahrübergang § 446, Rücktritt § 326 Abs. 5
nur verwiesen (116); III. Sekundäransprüche: §§ 280 Abs. 1, 3, 283 (Wortlautkarte § 283 Satz 1; Verweis 046),
Vertretenmüssen vermutet § 280 Abs. 1 Satz 2 (Verweis 141/147), Variante B 5.000 € Wertdifferenz, Variante A kein
Schadensersatz (§ 287 Satz 2 nur verwiesen, 112); § 285 Abs. 1 (Wortlautkarte; Versicherung, BT-Drucks. 14/6040 S. 144),
§ 326 Abs. 3 Satz 1, § 285 Abs. 2; Lösungstabelle; Klausurtipp (Prüfungsreihenfolge); Schema; Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Waldemar (stephan), Adelheid (hilde); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Waldemar": "stephan", "Adelheid": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Verkauf ------------------------------------------------------------------------------------------
    ("[fall]Waldemar verkauft Adelheid privat seinen Oldtimer, genau diesen einen Wagen, für zwanzigtausend Euro. "
     "[termin]Übergabe und Zahlung sollen am Samstag sein.", 0.3),
    ("[wa1]Am Samstag gehört er Ihnen. Bis dahin steht er sicher in meiner Garage.", 0.3, "Waldemar"),
    ("[ad1]Gut. Dann bringe ich die zwanzigtausend Euro mit.", 0.3, "Adelheid"),
    # --- A2 Fall: die Nacht vor der Übergabe ----------------------------------------------------------------------------
    ("[nacht]Doch in der Nacht vor der Übergabe brennt es in der Garage. [aus]Der Oldtimer brennt vollständig aus. "
     "[varA]Variante A: Ein Blitz hat eingeschlagen. [varB]Variante B: Waldemar hat am Abend in der Garage mit offener "
     "Flamme hantiert.", 0.3),
    # --- A3 Fall: am Morgen ---------------------------------------------------------------------------------------------
    ("[wa2]Der Wagen ist ausgebrannt. Ich kann ihn Ihnen nicht mehr geben.", 0.3, "Waldemar"),
    ("[ad2]Dann zahle ich auch nichts. Aber er war fünfundzwanzigtausend Euro wert!", 0.3, "Adelheid"),
    ("[vers]Außerdem: Die Versicherung zahlt Waldemar für den Wagen fünfundzwanzigtausend Euro. [frage]Muss Waldemar "
     "noch liefern, muss Adelheid noch zahlen, [frage2]und was kann sie verlangen?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau --------------------------------------------------------------------------------------------------------
    ("[plan]Wir prüfen in drei Schritten: [p1]Römisch eins, den Anspruch auf den Wagen. [p2]Römisch zwei, den Kaufpreis. "
     "[p3]Römisch drei, die Ansprüche von Adelheid auf Ersatz.", PS),
    # --- D I. § 275 Abs. 1 (Wortlaut) ------------------------------------------------------------------------------------
    ("[w275]Paragraf zweihundertfünfundsiebzig Absatz eins: Der Anspruch auf Leistung ist ausgeschlossen, soweit diese "
     "für den Schuldner oder für jedermann unmöglich ist.", P),
    # --- E I. Unmöglichkeit im Fall --------------------------------------------------------------------------------------
    ("[u1]Adelheid hat einen Anspruch auf Übergabe und Übereignung aus Paragraf vierhundertdreiunddreißig "
     "Absatz eins. [u2]Verkauft ist genau dieser Wagen, eine Stückschuld. Einen anderen muss "
     "Waldemar nicht beschaffen. [u3]Der Wagen ist zerstört, niemand kann ihn mehr liefern: Die Leistung ist "
     "objektiv unmöglich. [u4]Kann nur der Schuldner nicht leisten, ist sie subjektiv unmöglich. [u5]Der Brand kam nach dem Vertragsschluss, die Unmöglichkeit ist also nachträglich. [u6]Wäre der "
     "Wagen schon vorher ausgebrannt, bliebe der Vertrag nach Paragraf dreihundertelf a trotzdem wirksam.", P),
    # --- F I. Rechtsfolge, § 275 Abs. 2, 3 -------------------------------------------------------------------------------
    ("[rf1]Rechtsfolge: Der Anspruch ist ausgeschlossen, kraft Gesetzes. Waldemar muss sich nicht darauf berufen. "
     "[rf2]Anders die Absätze zwei und drei: [rf3]Steht der Aufwand in einem groben Missverhältnis zum "
     "Leistungsinteresse des Gläubigers [rf4]oder ist eine persönlich zu erbringende Leistung unzumutbar, [rf5]kann der "
     "Schuldner die Leistung nur verweigern. Das ist eine Einrede.", PS),
    # --- G II. Gegenleistung, § 326 Abs. 1 Satz 1 (Wortlaut) -------------------------------------------------------------
    ("[g1]Römisch zwei: Was wird aus dem Kaufpreis? [w326]Paragraf dreihundertsechsundzwanzig Absatz eins Satz eins: "
     "Braucht der Schuldner nach Paragraf zweihundertfünfundsiebzig Absatz eins bis drei nicht zu leisten, entfällt der "
     "Anspruch auf die Gegenleistung. [g2]Adelheid muss die zwanzigtausend Euro also nicht zahlen, in beiden Varianten.", P),
    # --- H II. Ausnahmen, § 326 Abs. 2, § 446, Verweis Rücktritt ---------------------------------------------------------
    ("[g3]Ausnahme nach Absatz zwei: Der Schuldner behält den Kaufpreis, wenn der Gläubiger für den Umstand allein oder weit "
     "überwiegend verantwortlich ist [g3b]oder wenn ein Umstand, den der Schuldner nicht zu vertreten hat, im "
     "Annahmeverzug des Gläubigers eintritt. [g3f]Beides "
     "liegt hier nicht vor. [g4]Und nach Paragraf vierhundertsechsundvierzig geht die Gefahr erst mit der Übergabe auf "
     "den Käufer über. [g4f]Der Wagen war aber noch nicht übergeben. [g5]Zurücktreten kann sie nach Absatz fünf ohne Frist, "
     "dazu das Video zum Rücktritt.", PS),
    # --- I III. 1. Schadensersatz, § 283 Satz 1 (Wortlaut) ---------------------------------------------------------------
    ("[s1]Römisch drei: Schadensersatz statt der Leistung. [w283]Paragraf zweihundertdreiundachtzig Satz eins: Braucht der "
     "Schuldner nach Paragraf zweihundertfünfundsiebzig Absatz eins bis drei nicht zu leisten, kann der Gläubiger unter "
     "den Voraussetzungen des Paragrafen zweihundertachtzig Absatz eins Schadensersatz statt der Leistung verlangen. "
     "[s046]Das System zeigt das Video zum Schadensersatz.", P),
    # --- J III. 1. Subsumtion: Pflichtverletzung, Vertretenmüssen, Varianten ---------------------------------------------
    ("[s2]Die Pflichtverletzung: Waldemar leistet nicht, auch wenn er nach Paragraf zweihundertfünfundsiebzig nicht mehr "
     "leisten muss. [s3]Das Vertretenmüssen wird nach Paragraf zweihundertachtzig Absatz eins Satz zwei vermutet; Waldemar "
     "muss sich entlasten. [s141]Dazu die Videos zur Beweislast und zum Anscheinsbeweis. [vb]In Variante B "
     "gelingt ihm das nicht: Wer neben einem Oldtimer mit offener Flamme hantiert, handelt fahrlässig. [vb2]Adelheid "
     "bekommt die Wertdifferenz: fünfundzwanzigtausend minus zwanzigtausend, also fünftausend Euro. [va]In Variante A hat "
     "Waldemar den Blitzschlag nicht zu vertreten, also kein Schadensersatz.", PS),
    # --- K III. 2. § 285 Abs. 1 (Wortlaut), Klausurclou ------------------------------------------------------------------
    ("[c1]Der Klausurclou: das stellvertretende Commodum. [w285]Paragraf zweihundertfünfundachtzig Absatz eins: "
     "Erlangt der Schuldner wegen des Umstands, der ihn befreit, für den geschuldeten Gegenstand einen Ersatz oder "
     "einen Ersatzanspruch, kann der Gläubiger Herausgabe oder Abtretung verlangen. [c2]Die Zahlung der Versicherung ist "
     "ein solcher Ersatz, so schon die Gesetzesbegründung. "
     "[c3]Vertretenmüssen verlangt die Norm nicht, sie greift also auch in Variante A. [c4]Adelheid kann die "
     "fünfundzwanzigtausend Euro verlangen. [c5]Dann bleibt sie aber nach Paragraf dreihundertsechsundzwanzig Absatz drei "
     "zur Gegenleistung verpflichtet und muss die zwanzigtausend Euro zahlen. [c6]Unterm Strich bleiben ihr fünftausend "
     "Euro. [c7]In Variante B mindert sich ihr Schadensersatz nach Paragraf zweihundertfünfundachtzig Absatz zwei um den "
     "Wert des Ersatzes.", PS),
    # --- L Lösung beider Varianten (Tabelle) -----------------------------------------------------------------------------
    ("[loes]Die Lösung: [l1]Den Wagen schuldet Waldemar in beiden Varianten nicht mehr, [l2]den Kaufpreis Adelheid "
     "auch nicht. [l3]Fünftausend Euro Schadensersatz gibt es nur in Variante B. [l4]Die Versicherungszahlung kann sie in "
     "beiden verlangen, muss dann aber den Kaufpreis zahlen.", PS),
    # --- M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Reihenfolge ein. [t1]Erst der Primäranspruch, [t2]dann die Gegenleistung, "
     "[t3]zuletzt Schadensersatz und Commodum.", PS),
    # --- N Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Anspruch auf Übergabe und Übereignung, [k11]ausgeschlossen nach Paragraf "
     "zweihundertfünfundsiebzig Absatz eins. [k2]Römisch zwei: Anspruch auf den Kaufpreis, entfallen nach Paragraf "
     "dreihundertsechsundzwanzig Absatz eins, [k21]Ausnahmen in Absatz zwei. [k3]Römisch drei: Sekundäransprüche. "
     "[k31]Eins: Schadensersatz statt der Leistung, mit Vertretenmüssen. [k32]Zwei: Herausgabe des Ersatzes, mit Pflicht "
     "zur Gegenleistung.", PS),
    # --- O Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Ist die Leistung unmöglich, fällt der Anspruch weg [mk2]und mit ihm grundsätzlich der Kaufpreis. "
     "[mk3]Schadensersatz gibt es nur bei Vertretenmüssen, [mk4]den Ersatz nach Paragraf zweihundertfünfundachtzig auch "
     "ohne.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
