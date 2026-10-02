"""Folge 034 · Schwarzarbeit: Kein Werklohn, keine Mängelrechte, kein Geld zurück? (Mo · Der Fall · Zivilrecht/Bereicherungsrecht).
Übungsfall nach dem Muster von BGH, Urt. v. 1.8.2013 – VII ZR 6/13 = BGHZ 198, 141 (gepflasterte Auffahrt, bar ohne Rechnung):
Frau Ziegler (Bestellerin, um 65) lässt die Einfahrt vom selbständigen Pflasterer Herrn Fuchs (um 45) „ohne Rechnung“ pflastern.
Kern: Nichtigkeit nach § 134 BGB i. V. m. § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG (Vorsatz des Unternehmers, Kenntnis und bewusstes
Ausnutzen durch die Bestellerin; Gegenfall einseitiger Verstoß), kein Werklohn, keine GoA, kein Wertersatz wegen § 817 S. 2 BGB
(BGHZ 201, 1), keine Mängelrechte (BGHZ 198, 141), keine Rückzahlung (BGHZ 206, 69), nachträgliche Abrede (BGHZ 214, 228).
Wortlautkarten: § 134 BGB, § 1 Abs. 2 Satz 1 Nr. 2 SchwarzArbG, § 817 Satz 2 BGB. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Fuchs": "stephan", "Ziegler": "lisa"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Einfahrt -----------------------------------------------------------------------------------------------
    ("[fall]Frau Ziegler will die Einfahrt vor ihrem Haus neu pflastern lassen. "
     "[fuchs]Der Pflasterer Herr Fuchs macht ihr ein Angebot.", 0.3),
    ("[f1]Mit Rechnung wird es teurer. Ohne Rechnung, bar auf die Hand: fünftausend Euro.", 0.3, "Fuchs"),
    ("[z1]Gut, dann machen wir es ohne Rechnung.", 0.3, "Ziegler"),
    ("[anz]Sie zahlt zweitausend Euro bar an. [pfl]Herr Fuchs pflastert die Einfahrt. "
     "[senkt]Wenige Wochen später sacken mehrere Steine ab, die Einfahrt ist uneben.", 0.3),
    ("[z2]Erst bessern Sie nach, vorher zahle ich nichts mehr!", 0.3, "Ziegler"),
    ("[f2]Ich will meine restlichen dreitausend Euro!", 0.4, "Fuchs"),
    ("[frage]Bekommt Herr Fuchs sein Geld? [frage2]Muss er nachbessern? "
     "[frage3]Und bekommt Frau Ziegler wenigstens ihre Anzahlung zurück?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Vorfrage: Ist der Werkvertrag wirksam? (Wortlaut § 134 BGB, § 1 Abs. 2 SchwarzArbG) --------------------------------
    ("[vor]Alles hängt an einer Vorfrage: Ist der Werkvertrag wirksam? [p134]Paragraf hundertvierunddreißig: "
     "Ein Rechtsgeschäft, das gegen ein gesetzliches Verbot verstößt, ist nichtig, wenn sich nicht aus dem Gesetz "
     "ein anderes ergibt.", P),
    ("[sag]Das Verbot steckt im Schwarzarbeitsbekämpfungsgesetz. [nr2]Nach Paragraf eins Absatz zwei Satz eins Nummer zwei "
     "leistet Schwarzarbeit, wer Werkleistungen erbringt oder ausführen lässt "
     "[nr2b]und dabei als Steuerpflichtiger seine steuerlichen Pflichten nicht erfüllt. "
     "[verbot]Der Bundesgerichtshof liest darin ein Verbot, solche Verträge zu schließen.", PS),
    # --- D Der Verstoß im Fall, Gegenfall ------------------------------------------------------------------------------------
    ("[fu]Herr Fuchs will weder eine Rechnung stellen noch Umsatzsteuer abführen. Er verstößt vorsätzlich. "
     "[zi]Ob auch Frau Ziegler selbst Schwarzarbeit leistet, kann offenbleiben. "
     "[kennt]Nichtig ist der Vertrag jedenfalls, wenn der Besteller den Verstoß kennt und bewusst zum eigenen Vorteil "
     "ausnutzt. [spart]Genau das tut sie: Sie spart die Umsatzsteuer. [nichtig]Der Werkvertrag ist nichtig, und zwar insgesamt.", P),
    ("[gegen]Anders, wenn Frau Ziegler von alldem nichts weiß und Herr Fuchs ohne ihr Wissen keine Steuern zahlt. "
     "[gegen2]Bei diesem einseitigen Verstoß bleibt der Vertrag nach der Rechtsprechung wirksam, "
     "[gegen3]und sie behält ihre Mängelrechte.", PS),
    # --- E Ansprüche von Herrn Fuchs -------------------------------------------------------------------------------------------
    ("[a]Zuerst Herr Fuchs. [a1]Werklohn aus Paragraf sechshunderteinunddreißig? Ohne wirksamen Vertrag gibt es keinen. "
     "[a2]Auch Aufwendungsersatz aus Geschäftsführung ohne Auftrag scheidet aus: "
     "Verbotene Arbeit durfte er nicht für erforderlich halten.", P),
    ("[b]Bleibt das Bereicherungsrecht. [b1]Frau Ziegler hat die Pflasterarbeiten durch seine Leistung ohne Rechtsgrund "
     "erlangt. [b2]Herausgeben kann sie die Arbeit nicht, also schuldet sie Wertersatz nach Paragraf "
     "achthundertachtzehn Absatz zwei.", P),
    ("[p817]Doch dann greift Paragraf achthundertsiebzehn Satz zwei: [p817b]Die Rückforderung ist ausgeschlossen, "
     "wenn dem Leistenden gleichfalls ein solcher Verstoß zur Last fällt. "
     "[p817c]Herr Fuchs hat gerade mit seiner Arbeit gegen das Verbot verstoßen. "
     "[p817d]Der Bundesgerichtshof wendet die Sperre auch auf den Anspruch aus Paragraf achthundertzwölf an. "
     "[werg]Ergebnis: kein Wertersatz.", PS),
    # --- F Mängelrechte von Frau Ziegler ----------------------------------------------------------------------------------------
    ("[m]Nun Frau Ziegler. [m1]Nacherfüllung, Minderung, Schadensersatz: Diese Mängelrechte aus Paragraf "
     "sechshundertvierunddreißig setzen einen wirksamen Werkvertrag voraus. [m2]Den gibt es nicht. "
     "[m3]Auch Treu und Glauben hilft nicht: Eine Nichtigkeit nach Paragraf hundertvierunddreißig lässt sich "
     "allenfalls in ganz engen Grenzen überwinden.", P),
    # --- G Rückzahlung der Anzahlung ----------------------------------------------------------------------------------------------
    ("[r]Und die Anzahlung? [r1]Herr Fuchs hat die zweitausend Euro zwar ohne Rechtsgrund erlangt. "
     "[r2]Aber auch ihre Zahlung ohne Rechnung diente dem verbotenen Geschäft. "
     "[r3]Paragraf achthundertsiebzehn Satz zwei sperrt deshalb auch ihre Rückforderung.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------------------
    ("[erg]Das Ergebnis: [e1]Herr Fuchs bekommt weder Werklohn noch Wertersatz. "
     "[e2]Frau Ziegler hat keine Mängelrechte und bekommt ihre Anzahlung nicht zurück. "
     "[e3]Einen Ausgleich gibt es nicht. [e4]Wer bewusst gegen das Verbot verstößt, soll schutzlos bleiben.", PS),
    # --- I Rechtsprechungslinie und nachträgliche Abrede --------------------------------------------------------------------------
    ("[linie]Diese Linie hat der Bundesgerichtshof Schritt für Schritt gezogen. "
     "[l90]Neunzehnhundertneunzig gab er dem Schwarzarbeiter nach Treu und Glauben noch Wertersatz. "
     "[l13]Zweitausenddreizehn: keine Mängelrechte für den Besteller. "
     "[l14]Zweitausendvierzehn: kein Wertersatz mehr, weil die erhoffte Abschreckung ausgeblieben war. "
     "[l15]Zweitausendfünfzehn: keine Rückzahlung für den Besteller. "
     "[l17]Zweitausendsiebzehn: Der Vertrag ist auch nichtig, wenn die Ohne-Rechnung-Abrede erst nachträglich "
     "getroffen wird.", P),
    ("[st]Ein Teil der Literatur hielt dann nur die Änderung für nichtig; der ursprüngliche Vertrag sollte weitergelten. "
     "[st2]Der Bundesgerichtshof lehnt das ab: Erst die Verbindung mit der Werkleistung macht die Abrede zur "
     "Schwarzarbeit, also ist der ganze Vertrag nichtig.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Nichtigkeit genau. Wer verstößt, und weiß die andere Seite davon? "
     "[tipp2]Und Vorsicht bei Teilbeträgen: Fließt nur ein Teil des Lohns ohne Rechnung, ist trotzdem der ganze Vertrag "
     "nichtig, [tipp3]wenn die Parteien dem Teil mit Rechnung keine bestimmten Einzelleistungen zugeordnet haben.", PS),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Teil A: Ansprüche des Unternehmers. [s2]Römisch eins: Werklohn aus Paragraf "
     "sechshunderteinunddreißig. [s3]Ist der Vertrag nichtig? Ja, wenn erstens das Verbot greift, "
     "[s4]zweitens der Unternehmer vorsätzlich verstößt [s5]und drittens der Besteller das kennt und bewusst ausnutzt.", P),
    ("[s6]Römisch zwei: Geschäftsführung ohne Auftrag, Aufwendungen nicht erforderlich. "
     "[s7]Römisch drei: Wertersatz aus Paragrafen achthundertzwölf, achthundertachtzehn Absatz zwei, "
     "gesperrt durch Paragraf achthundertsiebzehn Satz zwei.", P),
    ("[s8]Teil B: Ansprüche des Bestellers. [s9]Römisch eins: Mängelrechte aus Paragraf sechshundertvierunddreißig, "
     "kein wirksamer Vertrag. [s10]Römisch zwei: Rückzahlung aus Paragraf achthundertzwölf, ebenfalls gesperrt.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei bewusster Schwarzarbeit ist der Werkvertrag nichtig. "
     "[mk2]Und Paragraf achthundertsiebzehn Satz zwei sperrt das Bereicherungsrecht für beide Seiten.", 1.4),
]
