"""Folge 001 · Raser-Fall (nach BGH, Urt. v. 18.6.2020 – 4 StR 482/19, vereinfacht, Namen geändert).
Bedingter Tötungsvorsatz trotz Eigengefahr, gemeingefährliches Mittel, Mittäterschaft des zweiten Rasers.
Segmente: (text, pause) = Erzählerin Carla, (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad.
ENTWURF zur Freigabe – noch nicht vertont."""

P, PS = 0.4, 0.9

STIMMEN = {"Jonas": "timo", "Max": "niklas"}  # Lexi spricht mit der Erzählerstimme (Carla), wie im Katzenkönig

SEGMENTE = [
    # --- A Fall: das Rennen (Nacht) -------------------------------------------------------------------------
    ("[nacht]Kurz vor ein Uhr nachts, mitten in der Innenstadt. [ampel]Jonas und Max stehen mit ihren schnellen Autos "
     "nebeneinander an einer roten Ampel. Sie kennen sich flüchtig.", 0.3),
    ("[j1]Bis zum Ende vom Boulevard. Wer zuerst da ist?", 0.3, "Jonas"),
    ("[m1]Abgemacht!", 0.4, "Max"),
    ("[gruen]Die Ampel springt auf Grün. Beide geben Vollgas. [rennen]Sie rasen über mehrere Kreuzungen, "
     "teils bei Rot, immer schneller.", P),
    # --- B Fall: die Kreuzung ---------------------------------------------------------------------------------
    ("[kreuzung]An der letzten Kreuzung zeigt die Ampel längst Rot. Jonas fährt mit etwa hundertsechzig "
     "Stundenkilometern hinein. [suv]Von rechts kommt ein Geländewagen. Er hat Grün. "
     "[crash]Jonas rammt ihn mit voller Wucht. [tod]Der neunundsechzigjährige Fahrer stirbt noch an der Unfallstelle.", 0.7),
    ("[j2]Ich wollte doch niemanden töten!", 0.5, "Jonas"),
    ("[frage]Ist Jonas trotzdem ein Mörder? Und was ist mit Max, der niemanden gerammt hat?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Jonas: Vorsatz --------------------------------------------------------------------------------------
    ("[a]Wir beginnen mit Jonas, denn er hat den Unfall verursacht. In Betracht kommt Mord nach Paragraf "
     "zweihundertelf, aufbauend auf dem Totschlag nach Paragraf zweihundertzwölf.", P),
    ("[obj]Der objektive Tatbestand ist schnell erfüllt: Jonas hat durch den Zusammenstoß den Tod des Fahrers verursacht.", PS),
    ("[vors]Das eigentliche Problem ist der Vorsatz. [formen]Absicht und sicheres Wissen scheiden aus. "
     "Es bleibt nur der bedingte Vorsatz.", P),
    ("[def]Bedingt vorsätzlich handelt, wer den Tod als möglich und nicht ganz fernliegend erkennt "
     "[def2]und ihn billigend in Kauf nimmt oder sich zumindest damit abfindet.", P),
    ("[fahrl]Bewusst fahrlässig handelt dagegen, wer ernsthaft und nicht nur vage darauf vertraut, "
     "dass schon alles gut gehen wird.", PS),
    ("[eigen]Hier setzt das stärkste Argument gegen den Vorsatz an. Wer mit hundertsechzig bei Rot über eine Kreuzung "
     "fährt, bringt auch sich selbst in Lebensgefahr. Und den eigenen Tod nimmt niemand gern in Kauf.", P),
    ("[bgh18]Deshalb hob der Bundesgerichtshof das erste Mordurteil auf. [zeit]Der Vorsatz muss schon vorliegen, "
     "solange Jonas den Unfall noch verhindern kann. Ein Entschluss, der erst fällt, wenn nichts mehr zu machen ist, "
     "zählt nicht. [eigen2]Und die Eigengefahr muss das Gericht ausdrücklich würdigen.", P),
    ("[bgh20]Im zweiten Durchgang bestätigte der Bundesgerichtshof das neue Mordurteil gegen den Unfallfahrer. "
     "[panzer]Jonas fühlte sich in seinem schweren, gut gesicherten Wagen sicher. Das Risiko für sich selbst hielt er "
     "für gering. [egal]Was mit anderen geschah, war ihm gleichgültig. Ihm ging es nur darum, das Rennen zu gewinnen.", P),
    ("[vors_erg]Damit hat Jonas den Tod eines anderen billigend in Kauf genommen. Bedingter Tötungsvorsatz liegt vor.", PS),
    # --- E Jonas: Mordmerkmal, Ergebnis ---------------------------------------------------------------------
    ("[mm]Jetzt das Mordmerkmal. Naheliegend ist das gemeingefährliche Mittel.", P),
    ("[mm_def]Gemeingefährlich ist ein Mittel, wenn es in der konkreten Situation eine Mehrzahl von Menschen an Leib "
     "oder Leben gefährden kann, weil der Täter die Ausdehnung der Gefahr nicht in seiner Gewalt hat.", P),
    ("[mm_sub]Ein Auto mit hundertsechzig Stundenkilometern auf einer Kreuzung in der Innenstadt ist nicht mehr "
     "beherrschbar. [menschen]Es kann jeden treffen, der dort gerade unterwegs ist. [mm_vors]Und auch das war Jonas bewusst.", PS),
    ("[rws]Rechtswidrigkeit und Schuld sind unproblematisch. [a_erg]Jonas ist wegen Mordes strafbar, in Tateinheit mit "
     "einem verbotenen Kraftfahrzeugrennen mit Todesfolge nach Paragraf dreihundertfünfzehn d.", PS),
    # --- F Gegenfall: Max ---------------------------------------------------------------------------------
    ("[max]Und Max? Er hat den Geländewagen nicht berührt. [mt]In Betracht kommt Mord in Mittäterschaft. "
     "Dafür braucht es einen gemeinsamen Tatentschluss, der auch die Tötung umfasst.", P),
    ("[abrede]Die Abrede zum Rennen allein genügt dafür nicht. Dass Max auch einen tödlichen Unfall durch Jonas "
     "billigte, muss eigens festgestellt werden. [max_bgh]Genau daran fehlte es nach Ansicht des Bundesgerichtshofs. "
     "Er hob die Mordverurteilung von Max auf.", P),
    # TODO nach Rechtsprüfung: Ausgang des neuen Verfahrens gegen den zweiten Fahrer (LG Berlin 2021) knapp benennen
    ("[max_erg]<<AUSGANG NACH RECHTSPRÜFUNG>>", PS),
    # --- G Klausurtipp (Lexi) --------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schließe nie allein aus der Gefährlichkeit der Fahrt auf Vorsatz. [tipp1]Belege Wissen und "
     "Wollen mit Tatsachen aus dem Sachverhalt: Fahrweise, Motiv, Eigengefahr und den Zeitpunkt, an dem der Täter "
     "noch hätte bremsen können.", P),
    ("[tipp2]Und vergiss Paragraf dreihundertfünfzehn d Absatz fünf nicht. Für die Todesfolge genügt dort Fahrlässigkeit.", PS),
    # --- H Klausurschema -------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand. Erstens objektiv: Tod und Kausalität. "
     "[k1b]Zweitens der bedingte Tötungsvorsatz, mit Wissen, Wollen und Gesamtschau. "
     "[k1c]Drittens das Mordmerkmal gemeingefährliches Mittel, objektiv und subjektiv.", P),
    ("[k2]Römisch zwei, Rechtswidrigkeit. Römisch drei, Schuld. [k3]Dann die Konkurrenz mit dem verbotenen Kraftfahrzeugrennen. "
     "[k4]Und beim zweiten Raser gesondert: der gemeinsame Tatentschluss.", PS),
    # --- I Merksatz (Lexi) ------------------------------------------------------------------------------------
    ("[merke]Merke: Raser sind nicht automatisch Mörder. [m2]Entscheidend ist, ob der Täter den Tod anderer billigend "
     "in Kauf nahm, solange er ihn noch verhindern konnte.", 1.4),
]
