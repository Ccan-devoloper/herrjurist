"""Folge 011 · Deliktsaufbau Strafrecht: Tatbestand, Rechtswidrigkeit, Schuld (Examenswissen, Format Schema).
Beispielfall (frei erfunden): Am Uferweg rast der Radfahrer Holger knapp an der Joggerin Nele vorbei; dreißig Meter weiter steht
er abgestiegen und trinkt. Nele läuft hin und stößt ihn um, er schürft sich den Ellenbogen auf. Prüfung § 223 StGB im
dreistufigen Aufbau des vorsätzlichen vollendeten Begehungsdelikts: I. Tatbestand (objektiv: Handlung, Erfolg, Kausalität,
objektive Zurechnung; subjektiv: Vorsatz §§ 15, 16), II. Rechtswidrigkeit (§ 32 scheitert an der Gegenwärtigkeit),
III. Schuld (§§ 19, 20, 35, 17). Gegenfall (Themenplan-Hook): Holger will sie gerade anfahren -> Notwehr, Prüfung endet bei II.
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Nele": "lisa", "Holger": "marc", "Albrecht": "william"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: am Uferweg ------------------------------------------------------------------------------------------
    ("[fall]Sonntagmorgen am Uferweg. [nele]Nele, Mitte fünfzig, joggt ihre Runde am Fluss. "
     "[holger]Da rast Holger auf seinem Rad heran, viel zu schnell und zu knapp.", 0.2),
    ("[t1]Platz da!", 0.3, "Holger"),
    ("[sprung]Nele springt zur Seite. [halt]Dreißig Meter weiter hält Holger an, steigt ab und trinkt in Ruhe.", 0.4),
    # --- B Fall: der Stoß ----------------------------------------------------------------------------------------------
    ("[hin]Nele läuft zu ihm und stößt ihn mit beiden Händen um. [sturz]Holger stürzt über sein Rad und schürft sich den "
     "Ellenbogen auf.", 0.3),
    ("[n1]Das war für eben!", 0.4, "Nele"),
    ("[a1]Der stand doch längst!", 0.4, "Albrecht"),
    ("[frage]Hat Nele sich strafbar gemacht? [lernst]An diesem Fall lernst du den dreistufigen Deliktsaufbau beim "
     "vorsätzlichen vollendeten Begehungsdelikt: Tatbestand, Rechtswidrigkeit, Schuld.", 0.6),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Warum drei Stufen? ------------------------------------------------------------------------------------------
    ("[drei]Warum drei Stufen? [stb]Der Tatbestand beschreibt, was das Gesetz verbietet. [srw]Die Rechtswidrigkeit "
     "fragt, ob die Tat ausnahmsweise erlaubt ist. [ssch]Und die Schuld, ob man sie dem Täter persönlich vorwerfen kann.", P),
    ("[gesetz]Das Gesetz trennt selbst: Wer in Notwehr handelt, handelt nicht rechtswidrig, Paragraf zweiunddreißig. "
     "[g20]Wer schuldunfähig ist, handelt ohne Schuld, Paragraf zwanzig. [g29]Und jeder Beteiligte wird nach seiner "
     "eigenen Schuld bestraft, Paragraf neunundzwanzig.", PS),
    # --- E I. Tatbestand, objektiv -------------------------------------------------------------------------------------
    ("[tb]Wir prüfen Körperverletzung, Paragraf zweihundertdreiundzwanzig. Römisch eins: der Tatbestand, zuerst "
     "objektiv. [handlung]Die Tathandlung: Nele stößt Holger. [erfolg]Der Erfolg: Eine körperliche Misshandlung ist jede "
     "üble, unangemessene Behandlung, die das körperliche Wohlbefinden nicht nur unerheblich beeinträchtigt. "
     "[wunde]Der Sturz mit Schürfwunde ist das, und die Wunde zugleich eine Gesundheitsschädigung.", P),
    ("[kausal]Kausal ist jede Bedingung, die nicht hinweggedacht werden kann, ohne dass der Erfolg entfiele. Ohne "
     "Stoß kein Sturz. [zurech]Die Lehre verlangt zusätzlich die objektive Zurechnung: Im Sturz verwirklicht sich genau "
     "die Gefahr, die Nele geschaffen hat.", P),
    # --- F I. Tatbestand, subjektiv ------------------------------------------------------------------------------------
    ("[subj]Dann der subjektive Tatbestand. Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz "
     "fahrlässiges Handeln ausdrücklich mit Strafe bedroht, Paragraf fünfzehn. [vorsatz]Vorsatz heißt vereinfacht: Wissen und Wollen. Nele wollte "
     "Holger umstoßen und nahm in Kauf, dass er sich verletzt.", P),
    ("[p16]Anders wäre es, wenn sie beim Dehnen den Arm nach hinten schwingt und nicht weiß, dass dort jemand steht. "
     "[p16b]Wer einen Tatumstand nicht kennt, handelt nicht vorsätzlich, Paragraf sechzehn. [p229]Dann käme nur "
     "fahrlässige Körperverletzung in Betracht, Paragraf zweihundertneunundzwanzig. [tb_erg]Bei Nele ist der Tatbestand erfüllt.", PS),
    # --- G II. Rechtswidrigkeit ----------------------------------------------------------------------------------------
    ("[rw]Römisch zwei: die Rechtswidrigkeit. [indiz]Nach der Lehre deutet der erfüllte Tatbestand auf die "
     "Rechtswidrigkeit hin. [rfg]Sie entfällt nur, wenn ein Rechtfertigungsgrund greift. [nw]In Betracht kommt Notwehr, "
     "Paragraf zweiunddreißig. Sie verlangt einen gegenwärtigen rechtswidrigen Angriff.", P),
    ("[vorbei]Holgers Fahrweise war gefährlich. Aber als Nele zustößt, steht er längst und trinkt. Ein Angriff läuft nicht "
     "mehr. [rw_erg]Notwehr scheidet aus, Nele handelte rechtswidrig.", PS),
    # --- H III. Schuld -------------------------------------------------------------------------------------------------
    ("[schuld]Römisch drei: die Schuld. [faehig]Schuldunfähig ist, wer noch nicht vierzehn ist, Paragraf neunzehn, "
     "[p20]oder wer etwa wegen einer krankhaften seelischen Störung unfähig ist, das Unrecht einzusehen oder danach zu "
     "handeln, Paragraf zwanzig. [klar]Nele ist erwachsen und bei klarem Verstand.", P),
    ("[entsch]Ein Entschuldigungsgrund wie der Notstand nach Paragraf fünfunddreißig liegt nicht vor. "
     "[p17]Und für einen Verbotsirrtum nach Paragraf siebzehn spricht nichts. [schuld_erg]Nele handelte schuldhaft.", PS),
    # --- I Ergebnis und Gegenfall --------------------------------------------------------------------------------------
    ("[ergebnis]Ergebnis: Nele hat sich wegen Körperverletzung strafbar gemacht. [antrag]Verfolgt wird die Tat "
     "grundsätzlich nur auf Antrag, Paragraf zweihundertdreißig.", P),
    ("[gegen]Gegenfall: Holger lenkt sein Rad absichtlich auf Nele zu, um sie anzufahren. Sie stößt ihn vom Rad. "
     "[gegen2]Jetzt ist der Angriff gegenwärtig und rechtswidrig. Der Stoß wehrt ihn sofort ab, ein milderes, ebenso "
     "sicheres Mittel hat sie nicht. Ausweichen muss sie nicht, und sie will sich schützen.", P),
    ("[gegen3]Der Tatbestand bleibt erfüllt, aber Nele ist durch Notwehr gerechtfertigt. [ende]Die Prüfung endet dann schon bei der "
     "Rechtswidrigkeit.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib ausführlich nur dort, wo der Fall ein Problem hat, hier also bei der Gegenwärtigkeit. "
     "[tipp2]Gibt der Sachverhalt zur Schuld nichts her, genügt ein Satz: Nele handelte schuldhaft.", PS),
    # --- K Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand. [k1a]Erstens objektiv: Tathandlung, Erfolg, Kausalität "
     "und objektive Zurechnung. [k1b]Zweitens subjektiv: der Vorsatz.", P),
    ("[k2]Römisch zwei, Rechtswidrigkeit: Rechtfertigungsgründe wie Notwehr. [k3]Römisch drei, Schuld: "
     "Schuldfähigkeit, Entschuldigungsgründe und Unrechtsbewusstsein. [k4]Danach, falls nötig, der Strafantrag.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Tatbestand fragt, ob die Tat unter das Gesetz passt. [m2]Die Rechtswidrigkeit, ob sie "
     "ausnahmsweise erlaubt war. [m3]Die Schuld, ob man sie dem Täter vorwerfen kann. [m4]Scheitert eine Stufe, endet "
     "die Prüfung.", 1.4),
]
