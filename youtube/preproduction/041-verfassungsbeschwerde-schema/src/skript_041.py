"""Folge 041 · Verfassungsbeschwerde Schema: Zulässigkeit und Begründetheit (Mi · Examenswissen · Verfassungsprozessrecht).
Beispielfall (Übungsfall): Ein neues Bundesgesetz erlaubt den Behörden, die Bienenhaltung in Wohngebieten zu untersagen.
Die Hobbyimkerin Frau Wendt erhält vom Ordnungsamt (Herr Hübner) einen Untersagungsbescheid, klagt durch alle Instanzen
und verliert zuletzt vor dem Bundesverwaltungsgericht (Richterin Reuter). Urteilsverfassungsbeschwerde, mittelbar gegen
das Gesetz. Gegenfall: Herr Seifert will ohne Bescheid direkt gegen das Gesetz vorgehen (Rechtssatz-VB, Unmittelbarkeit).
Zulässigkeit als Klausurschema I.–VII. (Zuständigkeit Art. 94 I Nr. 4a GG n. F., § 13 Nr. 8a BVerfGG; Beschwerde-
berechtigung; Prozessfähigkeit; Beschwerdegegenstand; Beschwerdebefugnis; Rechtswegerschöpfung/Subsidiarität § 90 II;
Form und Frist §§ 23 I, 92, 93 I, III BVerfGG), Begründetheit kurz (Prüfungsmaßstab spezifisches Verfassungsrecht).
Wortlautkarten: Art. 94 I Nr. 4a GG, § 90 I und II 1 BVerfGG, § 93 I 1 und III BVerfGG.
Fiktive Figuren: Frau Wendt (julia), Herr Hübner (william), Richterin Reuter (elinor), Herr Seifert (marc).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Wendt": "julia", "Huebner": "william", "Reuter": "elinor", "Seifert": "marc"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: Bienen im Garten, der Bescheid ---------------------------------------------------------------------------
    ("[fall]Frau Wendt ist zweiunddreißig und hält in ihrem Garten am Stadtrand zwei Bienenvölker, seit acht Jahren ihr "
     "Hobby. [gesetz]Dann erlaubt ein neues Bundesgesetz den Behörden, die Bienenhaltung in Wohngebieten zu untersagen. "
     "[huebner]Herr Hübner vom Ordnungsamt bringt ihr den Bescheid.", 0.2),
    ("[hu1]Ihre Bienen müssen bis Ende Mai weg. So steht es im Bescheid.", 0.3, "Huebner"),
    ("[we1]Meine Bienen stören niemanden. Dagegen klage ich.", 0.3, "Wendt"),
    # --- B Fall: durch die Instanzen --------------------------------------------------------------------------------------
    ("[klage]Frau Wendt klagt und verliert beim Verwaltungsgericht. [ovg]Auch beim Oberverwaltungsgericht. [bverwg]Zuletzt "
     "entscheidet das Bundesverwaltungsgericht. [reuter]Richterin Reuter verkündet das Urteil.", 0.2),
    ("[re1]Die Revision der Klägerin wird zurückgewiesen.", 0.3, "Reuter"),
    ("[zustell]Dann wird Frau Wendt das vollständige Urteil zugestellt.", 0.2),
    ("[we2]Das verletzt meine Freiheit. Jetzt gehe ich nach Karlsruhe.", 0.4, "Wendt"),
    # --- C Die Frage ------------------------------------------------------------------------------------------------------
    ("[frage]Hat ihre Verfassungsbeschwerde Erfolg? [frage2]Wir prüfen Schritt für Schritt: erst die Zulässigkeit, dann die "
     "Begründetheit.", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E I. Zuständigkeit -----------------------------------------------------------------------------------------------
    ("[zust]Punkt A, Zulässigkeit. Römisch eins: Zuständigkeit. Über Verfassungsbeschwerden entscheidet das "
     "Bundesverfassungsgericht nach Artikel vierundneunzig Absatz eins Nummer vier a Grundgesetz. [art93]So steht es dort "
     "seit Ende zweitausendvierundzwanzig, vorher in Artikel dreiundneunzig. [p13]Dazu kommt Paragraf dreizehn Nummer acht a "
     "Bundesverfassungsgerichtsgesetz.", PS),
    # --- F II. Beschwerdeberechtigung, III. Prozessfähigkeit ----------------------------------------------------------------
    ("[berecht]Römisch zwei: Beschwerdeberechtigung. Nach Paragraf neunzig Absatz eins kann jedermann Verfassungsbeschwerde "
     "erheben. [traeger]Jedermann heißt: wer Träger des gerügten Grundrechts sein kann. Frau Wendt ist das als Mensch ohne "
     "Weiteres. [art193]Juristische Personen nur über Artikel neunzehn Absatz drei, soweit das Grundrecht seinem Wesen nach "
     "auf sie passt.", P),
    ("[prozess]Römisch drei: Prozessfähigkeit, also die Fähigkeit, Verfahrenshandlungen selbst vorzunehmen. Bei der "
     "volljährigen Frau Wendt kein Problem.", PS),
    # --- G IV. Beschwerdegegenstand -----------------------------------------------------------------------------------------
    ("[gegenst]Römisch vier: Beschwerdegegenstand ist ein Akt der öffentlichen Gewalt. Das kann ein Gesetz sein, ein "
     "Bescheid oder ein Urteil. [hier]Frau Wendt greift das letzte Urteil an, dazu die Urteile davor und den Bescheid. "
     "[mittelbar]Mittelbar greift sie auch das Gesetz an, auf dem alles beruht.", PS),
    # --- H V. Beschwerdebefugnis --------------------------------------------------------------------------------------------
    ("[befugt]Römisch fünf: Beschwerdebefugnis. Sie muss behaupten, in einem Grundrecht verletzt zu sein, und die "
     "Verletzung muss möglich sein. [art2]Ihr Hobby schützt die allgemeine Handlungsfreiheit, Artikel zwei Absatz eins. "
     "Geschützt ist jede Form menschlichen Handelns. [moeglich]Eine Verletzung ist also jedenfalls möglich.", P),
    ("[sgu]Außerdem muss sie selbst, gegenwärtig und unmittelbar betroffen sein. [adressat]Das Urteil richtet sich gegen "
     "sie und belastet sie jetzt. Das ist unproblematisch.", PS),
    # --- I Gegenfall Seifert: Gesetz direkt ----------------------------------------------------------------------------------
    ("[seifert]Anders bei Herrn Seifert. Er hält im Nachbarort Bienen und hat noch keinen Bescheid.", 0.2),
    ("[se1]Ich ziehe gleich gegen das Gesetz nach Karlsruhe.", 0.3, "Seifert"),
    ("[direkt]Gegen ein Gesetz direkt geht das nur ausnahmsweise. [unmitt]Unmittelbar betroffen ist er grundsätzlich nur, wenn das Gesetz "
     "ohne weiteren Vollzugsakt wirkt. [vollzug]Hier braucht es erst einen Bescheid der Behörde. Gegen den muss Herr Seifert "
     "zunächst vor die Fachgerichte.", PS),
    # --- J VI. Rechtswegerschöpfung und Subsidiarität -------------------------------------------------------------------------
    ("[rechtsweg]Römisch sechs: Rechtswegerschöpfung und Subsidiarität. Paragraf neunzig Absatz zwei: Ist der Rechtsweg "
     "zulässig, geht es erst nach seiner Erschöpfung nach Karlsruhe. [erschoepft]Frau Wendt war in allen Instanzen. "
     "[subsid]Subsidiarität verlangt mehr: Sie muss alle prozessualen Möglichkeiten genutzt haben, um die Verletzung schon "
     "vor den Fachgerichten zu verhindern. [vortrag]Etwa durch vollständigen Vortrag und geeignete Beweisanträge.", PS),
    # --- K VII. Form und Frist ----------------------------------------------------------------------------------------------
    ("[form]Römisch sieben: Form und Frist. Die Beschwerde ist schriftlich einzureichen und zu begründen, Paragraf "
     "dreiundzwanzig Absatz eins. [p92]Nach Paragraf zweiundneunzig bezeichnet sie das verletzte Recht und den "
     "angegriffenen Akt.", P),
    ("[frist]Die Frist steht in Paragraf dreiundneunzig Absatz eins: binnen eines Monats erheben und begründen. "
     "[beginn]Die Frist beginnt mit der Zustellung des vollständigen Urteils. [jahr]Gegen ein Gesetz direkt gilt dagegen ein "
     "Jahr ab Inkrafttreten, Absatz drei. [zul]Hält Frau Wendt Form und Frist ein, ist ihre Verfassungsbeschwerde zulässig.", PS),
    # --- L Begründetheit -----------------------------------------------------------------------------------------------------
    ("[begr]Punkt B, Begründetheit. Die Verfassungsbeschwerde ist begründet, wenn Frau Wendt in einem Grundrecht verletzt "
     "ist. [voll]Urteile prüft Karlsruhe aber nicht in vollem Umfang nach. [heck]Es prüft nur, ob spezifisches "
     "Verfassungsrecht verletzt ist: [heck2]etwa, ob das Gericht übersehen hat, dass Grundrechte zu beachten waren, oder ihr "
     "Gewicht falsch eingeschätzt hat.", P),
    ("[gesetzpr]Beruht das Urteil auf einem verfassungswidrigen Gesetz, verletzt schon das ihr Grundrecht. [dreischritt]Dann "
     "prüfst du das Gesetz: Schutzbereich, Eingriff, Rechtfertigung. [nichtig]Hat sie damit Erfolg, hebt Karlsruhe das "
     "Urteil auf und erklärt das Gesetz grundsätzlich für nichtig.", PS),
    # --- M Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei der Urteilsverfassungsbeschwerde nicht wie ein Fachgericht das einfache Recht nach. "
     "[tipp1]Frag nur: Wo liegt der Verstoß gegen Verfassungsrecht? [tipp2]Und unproblematische Punkte wie die "
     "Prozessfähigkeit stellst du nur kurz fest.", PS),
    # --- N Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit. [s1]Römisch eins, Zuständigkeit. [s2]Römisch zwei, "
     "Beschwerdeberechtigung. [s3]Römisch drei, Prozessfähigkeit. [s4]Römisch vier, Beschwerdegegenstand. [s5]Römisch fünf, "
     "Beschwerdebefugnis: möglicherweise verletzt, selbst, gegenwärtig, unmittelbar. [s6]Römisch sechs, "
     "Rechtswegerschöpfung und Subsidiarität. [s7]Römisch sieben, Form und Frist.", P),
    ("[sb]B, Begründetheit: [sb1]Verletzung eines Grundrechts, bei Urteilen nur spezifisches Verfassungsrecht.", PS),
    # --- O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gegen ein Urteil erst durch alle Instanzen, dann binnen eines Monats nach Karlsruhe. [m2]Und dort zählt nur das "
     "Verfassungsrecht.", 1.4),
]
