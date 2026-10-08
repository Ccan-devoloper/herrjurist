"""Folge 273 · Freischuss Jura: Freiversuch und Verbesserungsversuch erklärt (Fr · Methodik · Examen, Format Methodik).
Rahmen nach dem Plan-Hook („Du schreibst das Examen früh – was passiert, wenn es schiefgeht?“): Die Jurastudentin
Leonore (Anfang 20, studiert ununterbrochen in Nordrhein-Westfalen, siebtes Fachsemester, ein Auslandssemester) steht im
Fakultätsflur vor dem Aushang mit den Meldefristen. Ihr Freund Rasmus (Mitte 20) hat das Examen im letzten Jahr früh
geschrieben und danach seine Note verbessert.
Aufbau nach Auftrag: Hook → Sachverhalt → Was ist der Freiversuch (Wortlautkarte § 5d Abs. 5 S. 1–3 DRiG; Folge für
Leonore) → Voraussetzungen (Tafel mit drei am Wortlaut geprüften Ländern: § 25 JAG NRW, § 18 NJAG mit § 17 NJAVO,
§ 29 SächsJAPO; anrechnungsfreie Semester) → Verbesserungsversuch (§ 5d Abs. 5 S. 4 DRiG; § 26, § 65 Abs. 2 Nr. 1 JAG NRW;
§ 19 NJAG mit Anlage 2 NJG Nr. 7.3; § 31 SächsJAPO; zweites Examen § 56a JAG NRW, § 19 NJAG, § 56 SächsJAPO) →
Strategie (Chancen, Risiken, ohne Statistik) → Ergebnis (Flur) → Klausurtipp (Lexi) → Freischuss in 5 Schritten →
Merksatz (Lexi). Kein Rechtsrat für den Einzelfall: Hinweis „frag dein Prüfungsamt“. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche unter youtube/preproduction und themenplanung:
0 Treffer; Reservierung „273: Leonore, Rasmus“): Leonore, Rasmus; nie im Genitiv.
Stimmen (Pool niklas, helmut, ela_froh, julia): Leonore julia (Frau, jung, ruhig), Rasmus niklas (Mann, jung); helmut (älter)
und ela_froh (nicht für ernste Rollen) nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Leonore": "julia", "Rasmus": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Flur der Fakultät, Aushang mit den Meldefristen --------------------------------------------------------
    ("[fall]Ein Flur der juristischen Fakultät. [leo]Leonore steht vor dem Aushang mit den Meldefristen fürs Examen. "
     "[ras]Ihr Freund Rasmus bleibt neben ihr stehen.", P),
    ("[l1]Ich bin im siebten Semester. Soll ich mich jetzt schon melden? Und wenn ich durchfalle?", P, "Leonore"),
    ("[r1]Im Freischuss zählt ein Fehlversuch nicht. Ich habe auch früh geschrieben.", P, "Rasmus"),
    ("[hook]Du schreibst das Examen früh. Was passiert, wenn es schiefgeht? [hook2]Genau dafür gibt es den Freiversuch, "
     "im Studium meist Freischuss genannt. [wie]Hier siehst du, wie er funktioniert, welche Fristen gelten und was der "
     "Verbesserungsversuch bringt.", P),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist die Ausgangslage von Leonore. Halte das Video ruhig kurz an.", 5.0),
    # --- C Was ist der Freiversuch? (§ 5d Abs. 5 DRiG, Wortlaut) -------------------------------------------------------
    ("[was]Was ist der Freiversuch? [drig]Die Grundlage steht im Deutschen Richtergesetz, Paragraf fünf d Absatz fünf. "
     "[wl1]Die Pflichtfachprüfung kannst du einmal wiederholen. [wl2]Fällst du durch, obwohl du dich frühzeitig "
     "gemeldet [wl3]und alle vorgesehenen Prüfungsleistungen vollständig erbracht hast, [wl4]gilt die Prüfung als nicht "
     "unternommen. [wl5]Was frühzeitig heißt, regelt das Landesrecht.", P),
    ("[folge]Für Leonore heißt das: [fa]Fällt sie im Freiversuch durch, bleiben ihr trotzdem der reguläre Versuch [fb]und "
     "eine Wiederholung. [nur1]Den Freiversuch kennt das Richtergesetz nur für die Pflichtfachprüfung, also für das erste "
     "Examen.", P),
    # --- D Voraussetzungen: drei Länder ----------------------------------------------------------------------------------
    ("[vor]Welche Voraussetzungen gelten? [land]Das regelt dein Land, hier drei Beispiele. [nrw]In "
     "Nordrhein-Westfalen meldest du dich spätestens bis zum Ende des achten Fachsemesters. [nds]In Niedersachsen "
     "beantragst du die Zulassung zum Prüfungsdurchgang nach dem achten Fachsemester. [sn]In Sachsen legst du die Prüfung "
     "spätestens im Termin nach dem neunten Semester ab, wenn du ab Oktober zweitausendzwanzig angefangen hast. "
     "[unun]Und in allen drei Ländern muss das Studium ununterbrochen sein.", P),
    ("[frei]Manche Semester zählen dabei nicht mit, etwa wegen einer schweren Krankheit oder eines Studiums im "
     "Ausland. [aus]Für das Ausland sind es in Nordrhein-Westfalen und Niedersachsen bis zu drei Semester, in Sachsen bis "
     "zu zwei, jeweils mit Nachweisen. [deckel]Nordrhein-Westfalen lässt insgesamt höchstens vier Semester "
     "unberücksichtigt. [krank]Eine Krankheit weist du dort und in Niedersachsen mit einem amtsärztlichen Zeugnis "
     "nach.", P),
    ("[leo2]Leonore hat ein Semester im Ausland Recht studiert. [leo3]Erfüllt es die Voraussetzungen in "
     "Nordrhein-Westfalen, zählen bei ihr erst sechs Semester. [leo4]Ob das bei dir so ist, klärst du mit deinem "
     "Prüfungsamt.", P),
    ("[l2]Dann hätte ich sogar noch ein Semester mehr Zeit.", P, "Leonore"),
    # --- E Verbesserungsversuch ------------------------------------------------------------------------------------------
    ("[verb]Und wenn Leonore besteht, aber die Note ihr nicht reicht? [vb2]Dann bleibt der Verbesserungsversuch. "
     "[vb3]Das Richtergesetz überlässt ihn dem Landesrecht. [vnrw]In Nordrhein-Westfalen darfst du nach bestandenem "
     "Freiversuch einmal zur Notenverbesserung antreten. [vnrw2]Den Antrag stellst du innerhalb eines Jahres. [vnrw3]Eine "
     "Gebühr fällt dort nur an, wenn du im regulären Versuch bestanden hast. [vnds]Niedersachsen verlangt den Antrag ebenfalls innerhalb eines Jahres. "
     "[vnds2]Die Gebühr von hundertsechzig Euro entfällt nach einem bestandenen Freiversuch. [vsn]In Sachsen nutzt du den "
     "nächsten oder übernächsten Termin, und zwar bevor du im Referendariat bist. [vsn2]Auch dort entfallen die "
     "fünfhundert Euro nach dem Freiversuch.", P),
    ("[besser]In allen drei Ländern verdrängt eine schlechtere Note die alte nicht. [zwei]Nach dem zweiten Examen "
     "erlauben sie ebenfalls eine Notenverbesserung.", P),
    ("[r2]Mein Freischuss brachte sieben Punkte, der Verbesserungsversuch neun.", P, "Rasmus"),
    # --- F Strategie -----------------------------------------------------------------------------------------------------
    ("[strat]Lohnt sich der Freischuss für Leonore? [ch1]Die Chance: Sie bekommt einen zusätzlichen Versuch, ohne einen "
     "regulären zu verbrauchen. [ch2]Und besteht sie, kann sie ihre Note in diesen Ländern ohne Gebühr verbessern. "
     "[ri1]Das Risiko: Ihr bleibt weniger Zeit zum Lernen. [ri2]Ein Fehlversuch kostet trotzdem einen "
     "Prüfungsdurchgang und viel Kraft, [ri3]und auch der Verbesserungsversuch kostet noch einmal Monate. "
     "[stand]Entscheidend ist darum nicht das Semester, sondern dein Stand: Schreibst du deine Probeklausuren schon "
     "unter Examensbedingungen?", P),
    # --- G Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Leonore nimmt sich das Formular vom Aushang.", 0.2),
    ("[l3]Ich frage beim Prüfungsamt, ob mein Auslandssemester zählt. Dann melde ich mich.", P, "Leonore"),
    ("[r3]Und schreib bis dahin jede Woche eine Probeklausur.", PS, "Rasmus"),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Behandle den Freiversuch wie einen echten Versuch. [tipp2]Schreib jede Klausur zu Ende, auch "
     "wenn sie schlecht läuft. [tipp3]Der Schutz gilt nur, wenn du alle Prüfungsleistungen vollständig erbringst.", PS),
    # --- I Freischuss in fünf Schritten (Schema) -------------------------------------------------------------------------
    ("[sch]Dein Freischuss in fünf Schritten. [k1]Römisch eins: Meldefrist deines Landes prüfen. [k2]Römisch zwei: "
     "Semester klären, die nicht mitzählen. [k3]Römisch drei: alle Prüfungsleistungen vollständig erbringen. "
     "[k4]Römisch vier: durchgefallen, dann gilt die Prüfung als nicht unternommen. [k5]Römisch fünf: bestanden, dann "
     "Frist und Gebühr für den Verbesserungsversuch prüfen.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Freiversuch zählt ein Fehlversuch nicht, [m2]wenn du dich rechtzeitig meldest und alle "
     "Leistungen vollständig erbringst. [m3]Fristen, Semester und Verbesserung regelt dein Land, also frag dein Prüfungsamt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
