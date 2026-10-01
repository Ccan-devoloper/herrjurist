"""Folge 001 · Raser-Fall (nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, vereinfacht, Namen geändert).
Bedingter Tötungsvorsatz trotz Eigengefahr, Mordmerkmale je objektiv und subjektiv, zweiter Raser ohne Mittäterschaft.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad. ENTWURF v2 zur Freigabe – noch nicht vertont."""

P, PS = 0.4, 0.9

STIMMEN = {"Jonas": "timo", "Max": "niklas"}  # Lexi spricht mit der Erzählerstimme (Carla), wie im Katzenkönig

SEGMENTE = [
    # --- A Fall: das Rennen (Nacht) -------------------------------------------------------------------------
    ("[nacht]Gegen halb eins in der Nacht, mitten in der Innenstadt. [ampel]Jonas und Max stehen "
     "mit starken Autos nebeneinander an einer roten Ampel.", 0.3),
    ("[j1]Bis zum Ende vom Boulevard. Wer zuerst da ist?", 0.3, "Jonas"),
    ("[m1]Abgemacht!", 0.4, "Max"),
    ("[gruen]Die Ampel springt auf Grün. Beide geben Vollgas. [rennen]Über mehrere Kreuzungen rasen sie, teils bei Rot.", P),
    # --- B Fall: die Kreuzung ---------------------------------------------------------------------------------
    ("[kreuzung]An der letzten Kreuzung zeigt die Ampel längst Rot. Beide fahren ungebremst hinein, "
     "Jonas mit mehr als hundertsechzig Stundenkilometern. [suv]Von rechts kommt ein Geländewagen. Er hat Grün. "
     "[crash]Jonas rammt ihn mit voller Wucht. [tod]Der neunundsechzigjährige Fahrer stirbt noch an der Unfallstelle.", 0.7),
    ("[j2]Ich wollte doch niemanden töten!", 0.5, "Jonas"),
    ("[frage]Ist Jonas trotzdem ein Mörder? Und was ist mit Max, der niemanden gerammt hat?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Jonas: Vorsatz --------------------------------------------------------------------------------------
    ("[a]Wir beginnen mit Jonas: Mord nach Paragraf zweihundertelf, "
     "aufbauend auf Totschlag nach Paragraf zweihundertzwölf.", P),
    ("[obj]Objektiv hat Jonas den Tod des Fahrers verursacht.", PS),
    ("[vors]Das Problem ist der Vorsatz. [formen]Absicht und sicheres Wissen scheiden aus, "
     "es bleibt der bedingte Vorsatz.", P),
    ("[def]Bedingt vorsätzlich handelt, wer den Tod als möglich und nicht ganz fernliegend erkennt "
     "[def2]und ihn billigt oder sich mit ihm abfindet, mag er ihm auch gleichgültig oder an sich unerwünscht sein.", P),
    ("[fahrl]Bewusst fahrlässig handelt dagegen, wer ernsthaft und nicht nur vage darauf vertraut, "
     "dass alles gut gehen wird.", PS),
    ("[eigen]Das stärkste Gegenargument: Wer so fährt, gefährdet auch sich selbst.", P),
    ("[bgh18]Der Bundesgerichtshof hob das erste Mordurteil auf. [zeit]Zum einen muss der Vorsatz schon vorliegen, "
     "solange der Täter den Unfall noch verhindern kann. Ein Entschluss erst in der Kreuzung kommt zu spät. "
     "[panzer]Zum anderen fehlte eine Würdigung der Eigengefahr. Dass sich Raser im Auto sicher fühlen wie im Panzer, ist kein Erfahrungssatz.", P),
    ("[bgh20]Im zweiten Durchgang hielt das neue Mordurteil gegen Jonas. [abgestuft]Die Eigengefahr kann "
     "nämlich abgestuft sein. Jonas rechnete damit, bei einem Aufprall auf die Seite eines querenden Autos selbst nur "
     "leicht verletzt zu werden. [vertraut]Er vertraute nur darauf, nicht mit Max zusammenzustoßen.", P),
    ("[egal]Den Unfall, der dann geschah, nahm er für den Sieg hin. "
     "[bremsen]Und er fuhr weiter, als er noch hätte bremsen können.", P),
    ("[vors_erg]Damit liegt bedingter Tötungsvorsatz vor.", PS),
    # --- E Jonas: Mordmerkmale, Ergebnis ---------------------------------------------------------------------
    ("[mm]Jetzt die Mordmerkmale. Naheliegend wirkt das gemeingefährliche Mittel: [mm_def]eines, das in der "
     "konkreten Lage mehrere Menschen gefährden kann, weil der Täter die Gefahr nicht beherrscht.", P),
    ("[mm_sub]Objektiv liegt das nahe. [mm_subj]Aber dass Jonas eine Gefahr für weitere Menschen über den Aufprall "
     "hinaus erkannte und billigte, war nicht belegt. Der Bundesgerichtshof verneinte dieses Merkmal.", PS),
    ("[heim]Der Mord hält trotzdem. Erstens Heimtücke: Der Fahrer des Geländewagens verließ sich auf sein "
     "Grün und war arg- und wehrlos. [heim2]Jonas erfasste das und nahm es hin.", P),
    ("[nb]Zweitens niedrige Beweggründe. Den Tod eines Zufallsopfers für den Sieg in einem illegalen Rennen hinzunehmen, "
     "steht in krassem Missverhältnis zum Anlass.", PS),
    ("[rws]Rechtswidrigkeit und Schuld liegen vor. [a_erg]Jonas ist wegen Mordes strafbar, in Tateinheit mit "
     "vorsätzlicher Gefährdung des Straßenverkehrs.", PS),
    # --- F Gegenfall: Max ---------------------------------------------------------------------------------
    ("[max]Und Max? Er hat den Geländewagen nicht berührt. [mt]In Betracht kommt Mord in Mittäterschaft. "
     "Dafür braucht es einen gemeinsamen Tatentschluss, der auch die Tötung umfasst.", P),
    ("[abrede]Die Abrede zum Rennen genügt dafür nicht. Der Bundesgerichtshof hob die Mordverurteilung von Max deshalb auf.", P),
    ("[max_erg]Straflos ist Max trotzdem nicht. Auch er fuhr mit bedingtem Tötungsvorsatz bei Rot in die Kreuzung. "
     "[zufall]Dass Jonas den Geländewagen traf und nicht er, war Zufall. [versuch]Max ist deshalb wegen versuchten "
     "Mordes strafbar.", PS),
    # --- G Klausurtipp (Lexi) --------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schließe nie allein aus der Gefährlichkeit der Fahrt auf Vorsatz. [tipp1]Belege Wissen und "
     "Wollen mit Tatsachen: Motiv, Eigengefahr, Zeitpunkt. [tipp1b]Und prüfe jedes Mordmerkmal auch subjektiv.", P),
    ("[tipp2]Heute gibt es zudem das verbotene Kraftfahrzeugrennen, Paragraf dreihundertfünfzehn d, "
     "seit Oktober zweitausendsiebzehn. [tipp3]Gefährdet das Rennen andere und stirbt dadurch ein Mensch, drohen bis zu zehn Jahre. Für den Tod genügt Fahrlässigkeit.", PS),
    # --- H Klausurschema -------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand. Erstens objektiv: Tod und Kausalität. "
     "[k1b]Zweitens bedingter Tötungsvorsatz: Wissen, Wollen, Eigengefahr, Zeitpunkt. "
     "[k1c]Drittens die Mordmerkmale, jeweils objektiv und subjektiv.", P),
    ("[k2]Römisch zwei, Rechtswidrigkeit. Römisch drei, Schuld. [k3]Dann die Konkurrenzen. "
     "[k4]Beim zweiten Raser zuerst die Mittäterschaft, sonst seine eigene Tat, notfalls als Versuch.", PS),
    # --- I Merksatz (Lexi) ------------------------------------------------------------------------------------
    ("[merke]Merke: Raser sind nicht automatisch Mörder. [m2]Entscheidend ist, ob der Täter den Tod anderer billigend "
     "in Kauf nahm, solange er ihn noch verhindern konnte.", 1.4),
]
