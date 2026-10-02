"""Folge 061 · Polizeilicher Notstand: Muss ein Vermieter Obdachlose aufnehmen? (Mo · Der Fall · Polizei- und
Ordnungsrecht). Übungsfall nach dem Hook des Themenplans, Beispielland Nordrhein-Westfalen (OBG NRW, PolG NRW):
Dezember. Frau Brandt wohnt mit zwei Kindern zur Miete bei Herrn Bauer; nach einem Jobverlust Mietrückstände, Kündigung,
Räumungsurteil, Räumungstermin am 15. Januar. Sie findet keine Wohnung. Herr Schmitz vom Ordnungsamt prüft nur die
städtischen Notunterkünfte (belegt), fragt nicht bei Hotels und Pensionen. Die Stadt beschlagnahmt die Wohnung und weist
die Familie für drei Monate wieder ein. Herr Bauer wehrt sich.
Prüfung: § 14 I OBG NRW (Generalklausel), Zuständigkeit §§ 3 I, 4 I, 5 I OBG NRW; Gefahr durch unfreiwillige
Obdachlosigkeit; Verantwortliche § 17 OBG NRW; Nichtstörer § 19 I Nr. 1–4 OBG NRW (Wortlautkarte; Parallele § 6 PolG
NRW); Kernproblem Nr. 3 (eigene Unterkünfte, Hotels, Pensionen, Anmietung; Kosten unerheblich); § 19 II OBG NRW
(nur vorübergehend; VG Köln 22 L 1688/20 Rn. 18: höchstens sechs Monate); Verhältnismäßigkeit § 15 OBG NRW;
Ergebnis rechtswidrig; Variante rechtmäßig; Entschädigung § 39 I a/b OBG NRW (Wortlautkarte), § 40 I, § 42 II,
OLG Köln 7 U 83/93; Folgenbeseitigung nach Fristablauf (VG Köln 22 L 1688/20 Rn. 16; a. A. OLG Köln 7 U 83/93 Rn. 43);
Klausurtipp (Beschlagnahme/Einweisung, Streit Ermächtigungsgrundlage, § 43 I OBG NRW), Schema, Merksatz.
Fiktive Figuren: Frau Brandt (julia), Herr Bauer (helmut), Herr Schmitz (niklas). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Brandt": "julia", "Bauer": "helmut", "Schmitz": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Winter, die Wohnung ------------------------------------------------------------------------------------
    ("[fall]Dezember, draußen fällt Schnee. [fam]Frau Brandt wohnt mit ihren zwei Kindern zur Miete bei Herrn Bauer. "
     "[job]Nach einem Jobverlust konnte sie die Miete monatelang nicht zahlen. [urteil]Herr Bauer hat gekündigt und ein "
     "Räumungsurteil erstritten. [termin]Am fünfzehnten Januar kommt der Gerichtsvollzieher.", 0.2),
    ("[br1]Ich finde keine Wohnung. Wo sollen wir mit den Kindern hin?", 0.3, "Brandt"),
    # --- B Fall: Ordnungsamt --------------------------------------------------------------------------------------------
    ("[amt]Frau Brandt geht zum Ordnungsamt. [voll]Herr Schmitz prüft die Notunterkünfte der Stadt: alle belegt. "
     "[hotel]Bei Hotels und Pensionen fragt er nicht nach.", 0.2),
    ("[sc1]Dann bleibt nur eins: Wir weisen Sie wieder in Ihre Wohnung ein.", 0.3, "Schmitz"),
    # --- C Fall: Die Verfügung ------------------------------------------------------------------------------------------
    ("[verf]Die Stadt beschlagnahmt die Wohnung und weist die Familie für drei Monate wieder ein. [post]Herr Bauer "
     "bekommt die Verfügung.", 0.2),
    ("[ba1]Ich habe ein Urteil! Warum muss ausgerechnet ich die Familie aufnehmen?", 0.3, "Bauer"),
    # --- D Die Frage ----------------------------------------------------------------------------------------------------
    ("[frage]Darf die Stadt Herrn Bauer dazu zwingen? [frage2]Und bekommt er dafür Geld?", 0.6),
    # --- E Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Landesrecht, Ermächtigungsgrundlage, Gefahr --------------------------------------------------------------------
    ("[land]Gefahrenabwehr ist Landesrecht. Wir nehmen Nordrhein-Westfalen als Beispiel. Die anderen Länder haben "
     "ähnliche Regeln, oft unter anderer Nummer. [zust]Zuständig ist die Stadt als örtliche Ordnungsbehörde.", P),
    ("[egl]Grundlage ist die Generalklausel des Ordnungsbehördengesetzes, Paragraf vierzehn. [gefahr]Sie verlangt eine "
     "Gefahr für die öffentliche Sicherheit oder Ordnung. [obdach]Unfreiwillige Obdachlosigkeit ist eine solche Gefahr: "
     "Bedroht sind Leben und Gesundheit. [unfrei]Unfreiwillig ist sie, wenn sich die Betroffenen nicht aus eigener Kraft "
     "eine Unterkunft beschaffen können. [winter]Im Winter, mit zwei Kindern, liegt das auf der Hand.", P),
    # --- G Verantwortliche und Nichtstörer -------------------------------------------------------------------------------
    ("[stoerer]Gegen wen darf die Stadt vorgehen? Verantwortlich ist nach Paragraf siebzehn Frau Brandt selbst. "
     "[nicht]Herr Bauer hat die Gefahr nicht verursacht. Er ist Nichtstörer. [notstand]Ihn darf die Stadt nur im "
     "polizeilichen Notstand heranziehen, Paragraf neunzehn. [pol6]Für die Polizei steht dieselbe Regel in Paragraf "
     "sechs Polizeigesetz.", P),
    # --- H Wortlaut § 19 Abs. 1 OBG NRW ------------------------------------------------------------------------------------
    ("[wl19]Vier Voraussetzungen müssen zusammenkommen: [n1]Eine gegenwärtige erhebliche Gefahr. [n2]Maßnahmen gegen die "
     "Verantwortlichen sind nicht oder nicht rechtzeitig möglich oder versprechen keinen Erfolg. [n3]Die Behörde kann die "
     "Gefahr nicht selbst oder durch Beauftragte abwehren. [n4]Und der Nichtstörer wird ohne erhebliche eigene Gefährdung "
     "und ohne Verletzung höherwertiger Pflichten in Anspruch genommen.", P),
    # --- I Subsumtion Nr. 1 und 2 ---------------------------------------------------------------------------------------
    ("[s1]Erstens: Der Räumungstermin steht fest, der Schaden steht unmittelbar bevor. Die Gefahr ist gegenwärtig. "
     "[s1b]Und weil Leben und Gesundheit auf dem Spiel stehen, ist sie erheblich. [s2]Zweitens: Frau Brandt kann sich "
     "selbst nicht helfen. Eine Verfügung gegen sie liefe ins Leere.", P),
    # --- J Nr. 3: das Kernproblem ----------------------------------------------------------------------------------------
    ("[s3]Drittens, der Kern des Falls: Vorrang hat die eigene Abwehr durch die Stadt. [unterk]Geschuldet ist keine "
     "Wohnung, sondern eine menschenwürdige Unterkunft, die vor der Witterung schützt. [anmiet]Sind die eigenen Plätze "
     "voll, muss die Stadt Hotels, Pensionen oder Wohnungen anmieten. [kosten]Was das kostet, spielt keine Rolle. "
     "[s3neg]Herr Schmitz hat nur die eigenen Notunterkünfte geprüft. Dass nirgends etwas frei war, steht also nicht fest. "
     "Nummer drei ist nicht erfüllt.", P),
    # --- K Nr. 4, Dauer, Verhältnismäßigkeit, Ergebnis -------------------------------------------------------------------
    ("[s4]Nummer vier wäre dagegen kein Problem: Herr Bauer gerät selbst nicht in Gefahr. [frist]Wichtig ist noch die "
     "Dauer. Nach Absatz zwei darf die Maßnahme nur so lange bleiben, wie es keinen anderen Weg gibt. [sechsm]Das "
     "Verwaltungsgericht Köln spricht von höchstens sechs Monaten. [verh]Und verhältnismäßig ist die Inanspruchnahme nur "
     "als letztes Mittel, erst recht, wenn der Vermieter ein Räumungsurteil hat.", P),
    ("[erg]Ergebnis: Die Beschlagnahme ist rechtswidrig. Herr Bauer muss die Familie nicht aufnehmen, [erg2]die Stadt muss "
     "sie anders unterbringen. [anders]Anders wäre es, wenn die Stadt nachweislich alles versucht hätte und nichts frei "
     "wäre. [dulden]Dann müsste Herr Bauer die Familie für kurze Zeit dulden.", PS),
    # --- L Entschädigung, Wortlaut § 39 Abs. 1 OBG NRW --------------------------------------------------------------------
    ("[entsch]Und das Geld? [wl39]Nach Paragraf neununddreißig wird ein Schaden ersetzt, wenn er infolge einer "
     "Inanspruchnahme als Nichtstörer oder durch eine rechtswidrige Maßnahme entsteht. [beide]Herr Bauer bekommt also in "
     "beiden Fällen Geld, [miete]vor allem für die entgangene Miete. [danach]Nach dem Oberlandesgericht Köln auch für die "
     "Zeit danach, wenn ohne die Einweisung früher geräumt worden wäre. [regress]War die Inanspruchnahme rechtmäßig, kann "
     "sich die Stadt das Geld von der Familie zurückholen, Paragraf zweiundvierzig.", P),
    # --- M Nach Fristablauf: Folgenbeseitigung ----------------------------------------------------------------------------
    ("[ende]Und wenn die Frist abläuft? [fba]Dann hat der Vermieter einen Folgenbeseitigungsanspruch: Die Stadt muss die "
     "Nutzung beenden, notfalls mit einer Räumungsverfügung gegen die Familie. [streit]Ob das auch gilt, wenn die Familie "
     "vorher schon dort wohnte, ist umstritten. Das Oberlandesgericht Köln hat es verneint.", PS),
    # --- N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne die Verfügungen. [tipp1]Herr Bauer greift die Beschlagnahme an. Die Einweisung regelt nur "
     "das Verhältnis zwischen Stadt und Familie. [tipp2]Bei der Ermächtigungsgrundlage ist umstritten, ob die "
     "Generalklausel oder die Sicherstellung passt. Den Ausschlag gibt so oder so Paragraf neunzehn. [tipp3]Und über die "
     "Entschädigung entscheiden die ordentlichen Gerichte, Paragraf dreiundvierzig.", PS),
    # --- O Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q1]Eins, Ermächtigungsgrundlage: Paragraf vierzehn Ordnungsbehördengesetz. [q2]Zwei, "
     "formell: Zuständigkeit der Ordnungsbehörde. [q3]Drei, materiell: Gefahr durch unfreiwillige Obdachlosigkeit. "
     "[q4]Dann der Adressat: Nichtstörer nur unter den vier Voraussetzungen von Paragraf neunzehn. [q5]Vier, Ermessen, "
     "Verhältnismäßigkeit und Befristung. [q6]Danach Entschädigung und Folgenbeseitigung.", PS),
    # --- P Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Vermieter ist das letzte Mittel. [m2]Erst eigene Plätze, Hotels und Pensionen. Dann nur "
     "vorübergehend seine Wohnung, und nur gegen Entschädigung.", 1.4),
]
