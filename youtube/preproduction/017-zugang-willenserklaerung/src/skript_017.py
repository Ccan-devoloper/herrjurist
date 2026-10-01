"""Folge 017 · Zugang Willenserklärung § 130 BGB: Wann ist der Brief angekommen? (Examenswissen, Format Schema).
Beispielfall frei erfunden (Silvester-Fall nach dem Plan-Hook): Café-Inhaberin Helga kündigt den Wartungsvertrag mit
Werners Firma; die Kündigung muss bis 31. Dezember zugehen. Sie wirft den Brief an Silvester um 23 Uhr in den
Briefkasten von Werners Büro, Werner leert ihn am 2. Januar. Prüfung: Abgabe, Zugang (Machtbereich, Kenntnisnahme
unter gewöhnlichen Umständen, BGH XII ZR 148/05), kein Widerruf (§ 130 I 2). Gegenfälle: E-Mail im Geschäftsverkehr
(BGH VII ZR 895/21), Empfangsbotin Paula und Erklärungsbote, Annahmeverweigerung (§ 242), Beweis beim
Einwurf-Einschreiben. Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi),
(text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Helga": "laura_klar", "Werner": "marc", "Paula": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A/B Fall: Silvesterabend, zweiter Januar ----------------------------------------------------------------------
    ("[fall]Helga betreibt ein kleines Café. [vertrag]Werners Firma wartet ihre Kaffeemaschine. Der Vertrag "
     "verlängert sich um ein Jahr, wenn Helgas Kündigung nicht bis zum einunddreißigsten Dezember bei Werner ist. "
     "[silv]Erst an Silvester schreibt Helga die Kündigung. [einwurf]Um dreiundzwanzig Uhr wirft sie den Brief in den "
     "Briefkasten von Werners Büro.", 0.3),
    ("[h1]Geschafft, noch vor Mitternacht!", 0.4, "Helga"),
    ("[jan]Werners Büro ist über Neujahr geschlossen. Am zweiten Januar leert er den Briefkasten.", 0.3),
    ("[w1]Zu spät! Der Vertrag läuft noch ein Jahr.", 0.4, "Werner"),
    ("[frage]Ist Helgas Kündigung rechtzeitig wirksam geworden?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Norm und Gliederung ---------------------------------------------------------------------------------------
    ("[norm]Die Kündigung ist eine empfangsbedürftige Willenserklärung, abgegeben in Werners Abwesenheit. [p130]Nach "
     "Paragraf hundertdreißig Absatz eins wird sie erst wirksam, wenn sie ihm zugeht. [glied]Wir prüfen: Abgabe, "
     "Zugang und kein Widerruf.", PS),
    # --- E I. Abgabe -------------------------------------------------------------------------------------------------
    ("[abg]Römisch eins: die Abgabe. Helga muss die Erklärung willentlich so auf den Weg bringen, dass sie Werner "
     "erreichen kann. [abg_ok]Mit dem Einwurf ist das geschehen.", PS),
    # --- F II. Zugang ------------------------------------------------------------------------------------------------
    ("[zug]Römisch zwei: der Zugang. [macht]Erstens muss der Brief in Werners Machtbereich gelangen. Sein Briefkasten "
     "gehört dazu. [kennt]Zweitens muss Werner unter gewöhnlichen Umständen die Möglichkeit haben, ihn zur Kenntnis "
     "zu nehmen. [leer]Beim Briefkasten zählt, wann nach der Verkehrsanschauung mit der nächsten Leerung zu rechnen "
     "ist, nicht, wann Werner tatsächlich nachsieht. [feste]Eine feste Uhrzeit dafür gibt es nicht.", P),
    ("[bgh]Der Bundesgerichtshof sagt aber: Wer einen Brief erst nach Geschäftsschluss in den Briefkasten eines Büros "
     "wirft, bewirkt keinen Zugang mehr am selben Tag. [silv2]Das gilt auch für Silvester nachmittags, wenn dort "
     "üblicherweise niemand mehr arbeitet. [zug_erg]Helgas Brief ging also erst am zweiten Januar zu.", PS),
    # --- G III. Widerruf und Ergebnis --------------------------------------------------------------------------------
    ("[wid]Römisch drei: kein Widerruf. Hätte Helga es sich anders überlegt, hätte ihr Widerruf nach Paragraf "
     "hundertdreißig Absatz eins Satz zwei vorher oder gleichzeitig zugehen müssen. [wid2]Ein Anruf am zweiten Januar "
     "mittags wäre zu spät, auch wenn Werner den Brief noch nicht gelesen hätte.", P),
    ("[erg]Ergebnis: Die Kündigung ging erst am zweiten Januar zu, also zu spät. [erg2]Der Vertrag verlängert sich um "
     "ein Jahr.", PS),
    # --- H Gegenfall E-Mail ------------------------------------------------------------------------------------------
    ("[mail]Und wenn Helga am dreißigsten Dezember um zehn Uhr eine E-Mail geschickt hätte? [mail2]Im Geschäftsverkehr "
     "geht eine E-Mail nach dem Bundesgerichtshof grundsätzlich zu, sobald sie während der üblichen Geschäftszeiten abrufbereit auf "
     "dem Mailserver des Empfängers liegt. [mail3]Ob Werner sie liest, ist egal. [mail4]Was für Mails außerhalb der "
     "Geschäftszeiten gilt, hat das Gericht offengelassen.", PS),
    # --- I Boten -----------------------------------------------------------------------------------------------------
    ("[bote]Jetzt mit Boten. [paula]Gibt Helga den Brief am Silvestermorgen Werners Büroangestellter Paula, ist Paula "
     "Empfangsbotin.", 0.3),
    ("[p1]Ich lege ihn Werner gleich auf den Schreibtisch.", 0.4, "Paula"),
    ("[weiter]Zugegangen ist der Brief, sobald unter normalen Umständen mit der Weitergabe an Werner zu rechnen ist. "
     "[erkl]Schickt Helga dagegen einen eigenen Boten, ist er ihr Erklärungsbote. Bis er den Brief bei Werner "
     "abliefert, trägt Helga das Risiko.", PS),
    # --- J Annahmeverweigerung ---------------------------------------------------------------------------------------
    ("[verw]Und wenn Werner dem Boten den Brief gar nicht abnimmt?", 0.3),
    ("[w2]Den nehme ich nicht an!", 0.4, "Werner"),
    ("[treu]Wer grundlos die Annahme verweigert, obwohl er mit rechtserheblichen Erklärungen rechnen muss, wird nach Treu und "
     "Glauben so behandelt, als sei der Brief beim Übergabeversuch zugegangen, Paragraf zweihundertzweiundvierzig. "
     "[zumut]Helga muss dafür alles Zumutbare getan haben.", PS),
    # --- K Beweis ----------------------------------------------------------------------------------------------------
    ("[bew]Bleibt der Beweis: Den Zugang muss Helga beweisen. [einw]Beim Einwurf-Einschreiben begründen "
     "Einlieferungsbeleg und Sendungsstatus nach dem Bundesarbeitsgericht keinen Anscheinsbeweis. [ausl]Der "
     "Bundesgerichtshof lässt ihn mit der Kopie des Auslieferungsbelegs zu, wenn der Zusteller das vorgeschriebene "
     "Verfahren eingehalten hat. [scan]Für das Scan-Verfahren hat das Bundesarbeitsgericht auch das abgelehnt.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne beim Zugang zwei Fragen. [tipp2]Erstens: Ist die Erklärung im Machtbereich? Zweitens: "
     "Wann war mit der Kenntnisnahme zu rechnen? [tipp3]Ob der Empfänger sie wirklich gelesen hat, prüfst du nicht.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für das Wirksamwerden nach Paragraf hundertdreißig Absatz eins: [k1]Römisch eins: Abgabe. "
     "[k2]Römisch zwei: Zugang, [k2a]mit Machtbereich [k2b]und Kenntnisnahme unter gewöhnlichen Umständen, [k2c]samt "
     "Boten, E-Mail und Vereitelung. [k3]Römisch drei: kein vorheriger oder gleichzeitiger Widerruf. [k4]Römisch vier: "
     "Ergebnis mit genauem Zeitpunkt.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Zugegangen ist, was im Machtbereich des Empfängers liegt [m2]und was er unter gewöhnlichen "
     "Umständen zur Kenntnis nehmen kann. Ob er es wirklich liest, zählt nicht.", 1.4),
]
