"""Folge 009 · Strafrechtsklausur Aufbau: Tatkomplexe, Beteiligte, Reihenfolge (Methodik).
Beispielfall (frei erfunden): Bruno stiftet Kim und Tara an, zwei E-Bike-Akkus aus Ohms Fahrradladen zu stehlen (Tatkomplex 1);
auf der Flucht nimmt Ohm den Rucksack zurück, Kim stößt ihn weg, Tara wirft eine Flasche und verfehlt ihn (Tatkomplex 2).
Aufbauregeln (Klausurkonvention/Lehre) am Fall; Gesetz belegt: §§ 22, 23, 25 II, 26, 52, 53, 223, 224, 240, 242, 252 StGB,
§ 127 I StPO. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Bruno": "helmut", "Kim": "lucy", "Tara": "ela_froh", "Ohm": "johann"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Werkstatt ---------------------------------------------------------------------------------------------
    ("[werk]Eine Werkstatt im Hinterhof. [bruno]Bruno repariert E-Bikes und braucht Akkus. [zwei]Er spricht Kim und Tara an.", 0.3),
    ("[b1]Holt mir zwei Akkus aus Ohms Laden. Ich zahle euch zweihundert Euro.", 0.3, "Bruno"),
    ("[k1]Abgemacht. Tara lenkt ihn ab, ich packe ein.", 0.5, "Kim"),
    # --- B Fall: Laden -------------------------------------------------------------------------------------------------
    ("[laden]Am Nachmittag im Fahrradladen von Herrn Ohm. [ablenk]Tara verwickelt Ohm in ein Gespräch über Helme. "
     "[einpack]Kim steckt zwei Akkus in ihren Rucksack. [raus]Dann verlassen beide den Laden.", 0.5),
    # --- C Fall: Flucht an der Ecke ------------------------------------------------------------------------------------
    ("[ecke]Ohm bemerkt die Lücke im Regal und rennt hinterher.", 0.2),
    ("[o1]Halt! Das sind meine Akkus!", 0.3, "Ohm"),
    ("[reisst]An der Ecke reißt er Kim den Rucksack vom Rücken [arm]und hält sie am Arm fest. Kim will nur noch weg. "
     "[stoss]Sie stößt Ohm weg. Er stürzt und prellt sich den Ellenbogen. "
     "[flasche]Tara wirft im Weglaufen wütend eine Glasflasche nach seinem Kopf. [vorbei]Sie fliegt knapp vorbei.", 0.6),
    # --- D Frage ---------------------------------------------------------------------------------------------------------
    ("[frage]Wie haben sich Kim, Tara und Bruno strafbar gemacht? [orte]Drei Beteiligte, drei Orte. Wen prüfst du zuerst?", 0.6),
    # --- E Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Tatkomplexe -----------------------------------------------------------------------------------------------------
    ("[tk]Zuerst teilst du den Fall in Tatkomplexe, und zwar nach der Zeit. [tk1]Tatkomplex eins: der Diebstahl im Laden. "
     "[tk2]Tatkomplex zwei: die Flucht an der Ecke.", P),
    ("[auftrag]Und Brunos Auftrag in der Werkstatt? Der bekommt keinen eigenen Tatkomplex. "
     "[beitat]Die Anstiftung prüfst du bei der Tat, zu der angestiftet wurde. "
     "[konv]Diese Aufteilung steht in keinem Gesetz. Es sind Klausurregeln, die dein Gutachten lesbar machen.", PS),
    # --- G Tatkomplex 1 ------------------------------------------------------------------------------------------------------
    ("[naechst]Im Tatkomplex beginnst du mit der Person, die der Tat am nächsten steht. "
     "[kim]Das ist Kim: Sie hat die Akkus selbst weggenommen. [p242]Diebstahl, Paragraf zweihundertzweiundvierzig. "
     "[dritter]Dass die Akkus für Bruno sind, schadet nicht: Die Absicht, sie einem Dritten zuzueignen, genügt.", P),
    ("[tara]Dann Tara. Sie hat nichts eingepackt, aber nach dem gemeinsamen Plan Ohm abgelenkt und soll die Hälfte bekommen. "
     "[p25]Über Paragraf fünfundzwanzig Absatz zwei wird ihr Kims Wegnahme zugerechnet: Mittäterin.", P),
    ("[getrennt]Weil beide Unterschiedliches getan haben, prüfst du sie getrennt, Kim zuerst. "
     "[gemeinsam]Hätten beide dasselbe getan, dürftest du sie zusammen prüfen.", P),
    ("[bruno2]Bruno kommt zuletzt. Er war gar nicht im Laden. "
     "[p26]Anstifter ist nach Paragraf sechsundzwanzig, wer vorsätzlich einen anderen zu dessen vorsätzlich begangener rechtswidriger Tat bestimmt. "
     "[haupt]Ohne geprüfte Haupttat also keine Anstiftung. [tvt]Darum gilt: Täter vor Teilnehmer.", PS),
    # --- H Tatkomplex 2 ------------------------------------------------------------------------------------------------------
    ("[flucht]Tatkomplex zwei, die Flucht. Wieder zuerst Kim. "
     "[schwer]Du beginnst mit dem schwersten Delikt, das in Betracht kommt: räuberischer Diebstahl, Paragraf zweihundertzweiundfünfzig. "
     "[p252]Er verlangt Gewalt oder Drohung, um sich im Besitz der Beute zu erhalten. "
     "[beute]Die Akkus hatte Ohm aber schon zurück. Kim wollte nur fliehen.", P),
    ("[leicht]Danach die leichteren Delikte. [p223]Der Stoß ist eine Körperverletzung, Paragraf zweihundertdreiundzwanzig, "
     "[p240]und zugleich eine Nötigung, Paragraf zweihundertvierzig: Ohm sollte loslassen. "
     "[p127]Notwehr scheidet aus. Ohm durfte Kim nach Paragraf hundertsiebenundzwanzig der Strafprozessordnung festhalten.", P),
    ("[tara3]Dann Tara. [vollendet]Vollendetes prüfst du vor Versuchtem. Bei Tara ist nichts vollendet, die Flasche hat Ohm verfehlt. "
     "[versuch]Also versuchte gefährliche Körperverletzung: [p224]die Flasche als gefährliches Werkzeug. "
     "[quali]Qualifikation und Grunddelikt prüfst du zusammen. [p224b]Strafbar ist der Versuch nach Paragraf zweihundertvierundzwanzig Absatz zwei.", P),
    ("[zurech]Kims Stoß wird Tara nicht zugerechnet, und umgekehrt: Für die Flucht gab es keinen gemeinsamen Plan. "
     "[bruno3]Und Bruno? Gewalt war nicht Teil seines Auftrags.", PS),
    # --- I Konkurrenzen ------------------------------------------------------------------------------------------------------
    ("[konk]Bleiben die Konkurrenzen. [p52]Im Tatkomplex: Kims Stoß verletzt mit einer Handlung zwei Gesetze, Tateinheit, Paragraf zweiundfünfzig. "
     "[p53]Über die Tatkomplexe hinweg: Diebstahl und Stoß sind zwei Handlungen, Tatmehrheit, Paragraf dreiundfünfzig. "
     "[ebenso]Ebenso bei Tara: Diebstahl und Flaschenwurf.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Erkläre deinen Aufbau nicht, zeig ihn. [t1]Jede Überschrift nennt Tatkomplex, Person und Delikt mit Paragraf. "
     "[t2]Und bei Bruno verweist du nach oben: Die Haupttat steht schon fest.", P),
    # --- K Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Erster Tatkomplex, der Diebstahl im Laden. [s2]A: Kim, Diebstahl. "
     "[s3]B: Tara, Diebstahl in Mittäterschaft. [s4]C: Bruno, Anstiftung zum Diebstahl.", P),
    ("[s5]Zweiter Tatkomplex, die Flucht. [s6]A: Kim, räuberischer Diebstahl abgelehnt, dann Körperverletzung und Nötigung in Tateinheit. "
     "[s7]B: Tara, versuchte gefährliche Körperverletzung. [s8]Zum Schluss das Gesamtergebnis: Tatmehrheit.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ordne erst nach der Zeit, dann nach der Nähe zur Tat. "
     "[m2]Täter vor Teilnehmer, Vollendung vor Versuch, Schweres vor Leichtem. [m3]Und die Konkurrenzen zum Schluss.", 1.4),
]
