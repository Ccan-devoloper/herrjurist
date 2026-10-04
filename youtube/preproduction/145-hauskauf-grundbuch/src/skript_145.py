"""Folge 145 · Hauskauf in drei Schritten: Kaufvertrag, Auflassung, Grundbuch (Mo · Der Fall · Zivilrecht/Sachenrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Ihr unterschreibt beim Notar – ab wann gehört euch das Haus eigentlich?“):
Ute und Joachim kaufen von Herrn Ackermann (als Eigentümer im Grundbuch eingetragen) ein Haus. Bei einer Notarin wird der
Kaufvertrag beurkundet; im selben Termin erklären alle die Auflassung. Herr Ackermann will das Eigentum zunächst erst nach
Zahlung übergehen lassen; die Notarin weist auf die Bedingungsfeindlichkeit hin und sagt zu, die Eintragung erst nach Zahlung zu
beantragen; er erklärt die Auflassung ohne Bedingung. Wochen später Fälligkeitsmitteilung, Zahlung, Antrag, Eintragung.
Kern als Schema: 1. Kaufvertrag – § 311b Abs. 1 S. 1 (Wortlaut), Zweck (BGH V ZR 213/17 Rn. 12), § 125 S. 1, Heilung § 311b
Abs. 1 S. 2 (Wortlaut), Trennungsprinzip nur verwiesen (Folge 005); 2. Auflassung – § 925 Abs. 1 S. 1 (Wortlaut), S. 2,
Vertretung (BGH XII ZR 107/17 Rn. 19), Regelfall im selben Termin (V ZR 213/17 Rn. 13), § 925 Abs. 2 (Wortlaut),
Rechtsklarheit (vgl. V ZB 126/14 Rn. 10), Kontrast Eigentumsvorbehalt (Folge 139), Vorlagesperre (V ZR 213/17 Rn. 20 f.);
3. Eintragung – § 873 Abs. 1 (Wortlaut mit Auslassung), Dauer vorsichtig, Auflassungsvormerkung § 883 nur verwiesen,
Fälligkeitsmitteilung nur als Praxis; Ergebnis; Klausurtipp (Reihenfolge, Einigsein, § 873 Abs. 2); Schema; Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Ute (sabrina), Joachim (marc), Herr Ackermann (william), Notarin (laura_ruhig);
Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter. Kein Genitiv eines Namens."""

P, PS = 0.3, 0.5

STIMMEN = {"Ute": "sabrina", "Joachim": "marc", "Ackermann": "william", "Notarin": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: bei der Notarin ----------------------------------------------------------------------------------------
    ("[fall]Ute und Joachim kaufen ein Haus. [verk]Es gehört Herrn Ackermann, er steht als Eigentümer im Grundbuch. "
     "[notar]Zu dritt sind sie bei einer Notarin. [vorl]Sie liest den Kaufvertrag vor und fragt dann:", 0.25),
    ("[n1]Sind Sie sich einig, dass das Eigentum am Grundstück auf die Käufer übergeht?", 0.25, "Notarin"),
    ("[ak1]Ja. Aber erst, wenn der Kaufpreis bezahlt ist.", 0.25, "Ackermann"),
    ("[n2]Unter einer Bedingung geht das nicht. Ich beantrage die Eintragung erst, wenn Ihr Geld da ist.", 0.25, "Notarin"),
    ("[ak2]Gut, dann ohne Bedingung: Ja.", 0.2, "Ackermann"),
    ("[ut1]Ja, wir sind uns einig.", 0.25, "Ute"),
    ("[unter]Dann unterschreiben alle.", 0.2),
    ("[jo1]Ab heute gehört uns das Haus!", 0.3, "Joachim"),
    # --- A2 Fall: Wochen später, Frage -------------------------------------------------------------------------------------
    ("[spaet]Wochen später teilt die Notarin mit, dass der Kaufpreis fällig ist. [zahl]Ute und Joachim zahlen. "
     "[gb]Danach beantragt die Notarin die Eintragung, und das Grundbuchamt trägt die beiden als Eigentümer ein.", 0.3),
    ("[frage]Ab wann gehört ihnen das Haus? [o1]Mit der Unterschrift, [o2]mit der Zahlung [o3]oder erst mit der "
     "Eintragung?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.8),
    # --- C Aufbau -----------------------------------------------------------------------------------------------------------
    ("[plan]Ein Hauskauf läuft in drei Schritten: [s1]der Kaufvertrag, [s2]die Auflassung [s3]und die Eintragung ins "
     "Grundbuch.", PS),
    # --- D 1. Kaufvertrag ---------------------------------------------------------------------------------------------------
    ("[k1]Erstens: der Kaufvertrag. Paragraf dreihundertelf b Absatz eins Satz eins: [w311]Ein Vertrag, durch den sich der "
     "eine Teil verpflichtet, das Eigentum an einem Grundstück zu übertragen oder zu erwerben, bedarf der notariellen "
     "Beurkundung. [zweck]Das soll die Beteiligten vor übereilten Verträgen bewahren, und der Notar kann sie belehren. "
     "[nichtig]Fehlt die Beurkundung, ist der Vertrag nach Paragraf hundertfünfundzwanzig Satz eins nichtig.", P),
    ("[heil]Satz zwei kennt aber eine Heilung: [w311b]Ein ohne Beachtung dieser Form geschlossener Vertrag wird seinem "
     "ganzen Inhalt nach gültig, wenn die Auflassung und die Eintragung in das Grundbuch erfolgen.", P),
    ("[trenn]Und wichtig: Der Kaufvertrag verpflichtet Herrn Ackermann nur, das Eigentum zu verschaffen. [nochn]Übertragen "
     "ist damit noch nichts. [verw]Das ist das Trennungsprinzip, mehr dazu im Video zum Abstraktionsprinzip.", PS),
    # --- E 2. Auflassung, § 925 Abs. 1 ----------------------------------------------------------------------------------------
    ("[a1]Zweitens: die Auflassung, also die Einigung über den Eigentumsübergang. Paragraf neunhundertfünfundzwanzig "
     "Absatz eins Satz eins: [w925]Die zur Übertragung des Eigentums an einem Grundstück nach Paragraf "
     "achthundertdreiundsiebzig erforderliche Einigung des Veräußerers und des Erwerbers muss bei gleichzeitiger "
     "Anwesenheit beider Teile vor einer zuständigen Stelle erklärt werden. [zust]Zuständig ist nach Satz zwei jeder "
     "Notar.", P),
    ("[vertr]Gleichzeitig anwesend heißt nicht persönlich anwesend: Man kann sich vertreten lassen, etwa mit einer "
     "Auflassungsvollmacht. [regel]Im Fall haben alle die Auflassung im selben Termin wie den Kaufvertrag erklärt, wie es "
     "heute regelmäßig geschieht.", PS),
    # --- F § 925 Abs. 2 -------------------------------------------------------------------------------------------------------
    ("[w9252]Und Absatz zwei: Eine Auflassung, die unter einer Bedingung oder einer Zeitbestimmung erfolgt, ist "
     "unwirksam. [akb]Mit der Bedingung von Herrn Ackermann wäre die Auflassung also unwirksam gewesen. [klar]Warum so streng? "
     "Das Grundbuch soll zeigen, wem ein Grundstück gehört, und die sachenrechtliche Zuordnung braucht nach dem "
     "Bundesgerichtshof in erhöhtem Maße Rechtssicherheit und Rechtsklarheit.", P),
    ("[sofa]Anders bei beweglichen Sachen: Ein Sofa kann unter Eigentumsvorbehalt aufschiebend bedingt übereignet werden. "
     "Mehr dazu im Video zum Eigentumsvorbehalt. [sperre]Den Verkäufer eines Grundstücks schützt etwas anderes: Meist wird "
     "vereinbart, dass der Notar die Eintragung erst beantragt, wenn die Zahlung nachgewiesen ist.", PS),
    # --- G 3. Eintragung, § 873 Abs. 1 ---------------------------------------------------------------------------------------
    ("[e1]Drittens: die Eintragung. Paragraf achthundertdreiundsiebzig Absatz eins verlangt zur Übertragung des Eigentums "
     "an einem Grundstück [w873]die Einigung des Berechtigten und des anderen Teils über den Eintritt der Rechtsänderung "
     "und die Eintragung der Rechtsänderung in das Grundbuch. [erst]Eigentum gibt es also erst mit der Eintragung. "
     "[dauer]Bis dahin können Wochen oder Monate vergehen.", P),
    ("[vorm]Schutz für die Zwischenzeit bietet eine Auflassungsvormerkung nach Paragraf achthundertdreiundachtzig: "
     "Verfügungen nach ihrer Eintragung sind unwirksam, soweit sie den Anspruch der Käufer vereiteln oder beeinträchtigen würden. Dazu gibt es "
     "eine eigene Folge. [faellig]Und in der Praxis sehen Kaufverträge häufig vor, dass der Kaufpreis erst nach einer "
     "Mitteilung des Notars fällig wird.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Zurück zum Fall: [r1]Nach der Unterschrift hatten Ute und Joachim einen wirksamen Kaufvertrag und eine "
     "wirksame Auflassung, aber noch kein Eigentum. [r2]Auch die Zahlung allein ändert daran nichts. [r3]Herr Ackermann "
     "war Berechtigter, [r4]und mit der Eintragung im Grundbuch gehört das Haus den beiden.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Erwerb in dieser Reihenfolge: [t1]Einigung, [t2]Eintragung, [t3]Einigsein bei der "
     "Eintragung [t4]und Berechtigung. [t5]Vergiss das Einigsein nicht: Die Einigung muss bei der Eintragung noch "
     "bestehen. Bindend ist sie vorher nur unter den Voraussetzungen von Paragraf achthundertdreiundsiebzig Absatz zwei, etwa bei notarieller Beurkundung.", PS),
    # --- J Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Eigentumserwerb am Grundstück: [kI]Römisch eins: Einigung, also Auflassung. [kI1]Sie wird "
     "bei gleichzeitiger Anwesenheit vor einer zuständigen Stelle erklärt, [kI2]ohne Bedingung und ohne Zeitbestimmung. "
     "[kII]Römisch zwei: Eintragung im Grundbuch. [kIII]Römisch drei: Einigsein bei der Eintragung. [kIV]Römisch vier: "
     "Berechtigung des Veräußerers. [kV]Daneben steht der Kaufvertrag als Rechtsgrund, in notarieller Form.", PS),
    # --- K Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Kaufvertrag verpflichtet nur. [mk2]Eigentum am Haus bringen erst Auflassung und Eintragung. "
     "[mk3]Und die Auflassung verträgt keine Bedingung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
