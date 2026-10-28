"""Folge 123 · Prüfungsschemata lernen – aber richtig: Verstehen statt pauken (Fr · Methodik · Lernen, Format Methodik).
Rahmen: Der Jurastudent Gunnar hat achtzig Schemata auf Karteikarten auswendig gelernt (Karteikarten-Turm) und scheitert im
Tutorium an einem Übungsfall, der „nicht im Schema steht“: Ein Spaziergänger findet nachts auf dem leeren Gehweg ein
verlorenes Handy, behält es und benutzt es als seines (§ 242 StGB scheitert an der Wegnahme, BGH 5 StR 10/20; Lösung
§ 246 StGB). Die Tutorin Marlene zeigt drei Werkzeuge:
  1. das Schema als Landkarte des Gesetzes (Wortlautkarte § 242 Abs. 1 StGB, jeder Prüfungspunkt aus einem Wort; Vorsatz
     aus § 15 StGB),
  2. „Warum steht der Punkt hier?“ (Zueignungsabsicht subjektiv: erfolgskupiertes Delikt, BGH 4 StR 591/17 Rn. 17;
     entstanden – untergegangen – durchsetzbar, §§ 362 Abs. 1, 214 Abs. 1 BGB, Verweis Folge 103),
  3. Transfer: § 246 StGB aus dem Wortlaut neben § 242 gebaut (Wortlautkarte § 246 Abs. 1; Zueignung wird objektiv,
     BGH 6 StR 191/23 Rn. 8; Umfang streitig, 6 StR 191/23 Rn. 5/10 und 4 StR 442/23 Rn. 11, hier nach jeder Ansicht erfüllt),
dazu Lernen mit Fällen statt Listen (Abrufen und verteiltes Wiederholen: Weinstein/Madan/Sumeracki, Cogn. Res. 2018, 3:2;
Fehlerliste als Erfahrungsregel). Kein Auswendiglern-Bashing: Die Karten bleiben, sie werden verstanden.
Belege: ../RECHTSSTAND.md. Figuren: Gunnar (niklas), Marlene (ela_froh); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Gunnar": "niklas", "Marlene": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Karteikarten-Turm und Tutorium ------------------------------------------------------------------------
    ("[fall]Gunnar lernt für die Strafrechtsklausur. [turm]Vor ihm steht ein Turm aus Karteikarten: achtzig Schemata, "
     "alle auswendig. [tut]Im Tutorium legt ihm die Tutorin Marlene einen kurzen Fall hin.", 0.3),
    ("[g1]Diebstahl passt nicht. Und für alles andere habe ich keine Karte!", 0.3, "Gunnar"),
    ("[hook]Du kannst achtzig Schemata auswendig und scheiterst trotzdem am Fall? [hook2]Dann fehlt oft nicht der Fleiß, "
     "sondern der Weg vom Schema zurück zum Gesetz.", 0.3),
    ("[m1]Wirf deine Karten nicht weg. Aber lerne, woher jeder Punkt kommt. Ich zeige dir drei Werkzeuge.", 0.4,
     "Marlene"),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall aus dem Tutorium. Halte das Video ruhig kurz an.", 5.0),
    # --- C Werkzeug 1: das Schema als Landkarte des Gesetzes -----------------------------------------------------------
    ("[w1]Werkzeug eins: Das Schema ist eine Landkarte des Gesetzes. Jeder Prüfungspunkt kommt aus einem Wort. "
     "[p242]Paragraf zweihundertzweiundvierzig Absatz eins: [p242w]Wer eine fremde bewegliche Sache einem anderen in der "
     "Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird bestraft.", P),
    ("[obj]Aus fremde bewegliche Sache und wegnimmt wird der objektive Tatbestand. [subj]Aus der Absicht, rechtswidrig "
     "zuzueignen, wird der subjektive. [vors]Und was nicht in der Norm steht, kommt aus dem Allgemeinen Teil: der Vorsatz "
     "aus Paragraf fünfzehn, [rws]dazu Rechtswidrigkeit und Schuld.", P),
    ("[fall1]Jetzt der Fall. Das Handy ist eine fremde bewegliche Sache. [wegn]Aber Wegnahme heißt: fremden Gewahrsam "
     "brechen und neuen begründen. [gew]Die Eigentümerin ist fort und kann auf das Handy auf dem Gehweg nicht mehr einwirken. "
     "Sie hat keinen Gewahrsam mehr. [kein]Keine Wegnahme, also kein Diebstahl. Bis hierhin trägt das Schema.", P),
    # --- D Werkzeug 2: Warum steht der Punkt hier? ---------------------------------------------------------------------
    ("[w2]Werkzeug zwei: Frag bei jedem Punkt, warum er dort steht. [w2a]Warum prüfst du die Zueignung beim Diebstahl "
     "im subjektiven Tatbestand? Weil das Gesetz nur die Absicht verlangt. [w2b]Der Diebstahl ist mit der Wegnahme "
     "vollendet. Ob der Täter die Sache danach wirklich behält, ist für den Tatbestand egal, sagt der "
     "Bundesgerichtshof.", P),
    ("[w2c]Im Zivilrecht genauso: entstanden, untergegangen, durchsetzbar. [w2d]Erlöschen kann nur ein Anspruch, der "
     "entstanden ist. [w2e]Und die Verjährung lässt den Anspruch bestehen. Sie gibt dem Schuldner nur das Recht, die "
     "Leistung zu verweigern, deshalb kommt sie zuletzt. Mehr dazu in Folge hundertdrei. [w2f]Wer den Grund kennt, muss die Reihenfolge nicht "
     "pauken.", P),
    # --- E Werkzeug 3: Transfer auf § 246 StGB -------------------------------------------------------------------------
    ("[w3]Werkzeug drei: Ein Schema, das du nie gelernt hast, baust du aus dem Wortlaut. [p246]Paragraf "
     "zweihundertsechsundvierzig Absatz eins: [p246w]Wer eine fremde bewegliche Sache sich oder einem Dritten rechtswidrig "
     "zueignet, wird bestraft, wenn die Tat nicht in anderen Vorschriften mit schwererer Strafe bedroht ist.", P),
    ("[neben]Leg die Norm neben den Diebstahl. [t1]Fremde bewegliche Sache: kennst du schon. [t2]Wegnimmt: fehlt. Du "
     "brauchst also keinen Gewahrsamsbruch. [t3]Und die Zueignung steht nicht mehr als Absicht da, sondern als Tat: "
     "zueignet. [t4]Damit wandert sie in den objektiven Tatbestand.", P),
    ("[t5]Wie viel dafür nötig ist, sehen selbst die Strafsenate des Bundesgerichtshofs unterschiedlich. [t6]Hier reicht "
     "es nach jeder Ansicht: Der Spaziergänger benutzt das Handy als seines und schließt die Eigentümerin aus. "
     "[t7]Rechtswidrig ist das, denn er hat keinen Anspruch darauf. [t8]Dazu Vorsatz, Rechtswidrigkeit und Schuld. "
     "[t9]Eine schwerere Vorschrift greift nicht. [erg]Ergebnis: Unterschlagung nach Paragraf "
     "zweihundertsechsundvierzig.", 0.3),
    ("[g2]Das Schema stand ja schon im Gesetz!", 0.4, "Gunnar"),
    # --- F Lernen mit Fällen statt Listen ------------------------------------------------------------------------------
    ("[m2]Und so lernst du damit: mit Fällen statt Listen.", 0.3, "Marlene"),
    ("[l1]Nimm einen kurzen Fall und schreib das Schema aus dem Kopf auf, ohne Karte. [l2]Dann vergleiche mit dem "
     "Gesetz und notiere jeden Fehler. [l3]Ein paar Tage später kommt derselbe Fall noch einmal, danach ein neuer. "
     "[l4]Die Lernforschung stützt das: Wer Wissen aus dem Gedächtnis abruft und das Wiederholen auf mehrere Tage "
     "verteilt, behält es länger als durch bloßes Wiederlesen oder Pauken an einem Abend.", 0.3),
    ("[g3]Also Karten behalten, aber mit Fällen abfragen.", 0.4, "Gunnar"),
    # --- G Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Passt kein gelerntes Schema, lies die Norm Wort für Wort. [tipp2]Mach aus jedem Merkmal einen "
     "Prüfungspunkt, [tipp3]und zitiere die Norm im Obersatz genau. So zeigst du, dass du vom Gesetz aus denkst.", PS),
    # --- H Klausurschema § 246 StGB ------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Unterschlagung, gebaut aus dem Wortlaut. [s1]Römisch eins, Tatbestand. [s1a]Objektiv: "
     "[s1a1]fremde bewegliche Sache, [s1a2]Zueignung, [s1a3]und die Zueignung ist rechtswidrig. [s1b]Subjektiv: der "
     "Vorsatz. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, Schuld. [s4]Und am Ende die Klausel: Unterschlagung "
     "nur, wenn keine schwerere Vorschrift greift.", PS),
    # --- I Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Schema ist kein Gedicht zum Aufsagen, sondern eine Landkarte des Gesetzes. [mm2]Wer weiß, woher "
     "jeder Punkt kommt, findet auch durch einen neuen Fall.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
