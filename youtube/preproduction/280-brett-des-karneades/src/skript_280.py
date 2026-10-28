"""Folge 280 · Entschuldigender Notstand § 35: Das Brett des Karneades (Mo · Der Fall · StGB AT, Format Klassiker-Fall).
Übungsfall nach dem Plan-Hook („Nach einem Bootsunglück stößt ein Schiffbrüchiger einen anderen von einer Planke, die nur
einen tragen kann“): Herr Tamm (Mitte 40) war Fahrgast auf einem Ausflugsboot, das im Sturm sinkt. Im Wasser treibt nur eine
Planke, die einen Menschen trägt. Ein zweiter Schiffbrüchiger, ein Fremder, hält sich ebenfalls daran fest; unter beiden geht
sie unter. Herr Tamm stößt ihn weg, der andere kommt ums Leben. Stunden später rettet ein Fischkutter Herrn Tamm.
Rahmenhandlung an Land: Hafenbüro der Wasserschutzpolizei, Kommissarin Petzold nimmt die Aussage auf.
Darstellung: kein Ertrinken, kein Stoß, keine Leiche im Bild – Planke und Wellen nur als Symbol, ohne Menschen im Wasser.
Aufbau (Klassiker-Fall, laut Auftrag): 1. Hook → Sachverhalt → 2. Tatbestand § 212, Rechtswidrigkeit (§ 34 in einem Satz,
Verweis 263) → 3. § 35 Abs. 1 S. 1 (Wortlautkarte) → 4. § 35 Abs. 1 S. 2 (Wortlautkarte), Abwandlung 1 Kapitän →
5. § 35 Abs. 2 (Wortlautkarte), Abwandlung 2 Irrtum (BGHSt 48, 255 Rn. 35, Verweis 007) → 6. Ergebnis → 7. Klausurtipp
(Lexi), Schema, Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung „280: Tamm, Petzold“; git grep unter youtube/ ohne
Treffer). Der Getötete, der Fahrgast der Abwandlung und der Kapitän bleiben namenlos.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Tamm marc (Mann, mittel), Kommissarin Petzold sabrina (Frau, mittel);
william und laura_ruhig nicht verwendet (der Kapitän spricht nicht). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Artikel im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Tamm": "marc", "Petzold": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Hafenbüro, Aussage, Symbolbild Planke ----------------------------------------------------------------------
    ("[fall]Dienstagmorgen im Hafenbüro der Wasserschutzpolizei. [petzold]Kommissarin Petzold nimmt eine Aussage auf. "
     "[tamm]Vor ihr steht Herr Tamm, Mitte vierzig. Er hat ein Bootsunglück überlebt.", P),
    ("[pe1]Herr Tamm, was ist draußen auf dem Wasser passiert?", P, "Petzold"),
    ("[ta1]Unser Ausflugsboot ist im Sturm gesunken. Im Wasser trieb nur eine einzige Planke.", P, "Tamm"),
    ("[planke]Die Planke trägt nur einen Menschen. [zweiter]Ein zweiter Schiffbrüchiger, ein Fremder, hält sich ebenfalls "
     "daran fest. [sinkt]Unter beiden geht sie unter. [stoss]Herr Tamm stößt den anderen weg. [tot]Der andere kommt ums "
     "Leben. [rettung]Stunden später zieht ein Fischkutter Herrn Tamm aus dem Wasser.", P),
    ("[ta2]Sonst wären wir beide ertrunken.", P, "Tamm"),
    ("[frage]Hat sich Herr Tamm wegen Totschlags strafbar gemacht? [karneades]Der Fall ist ein Klassiker: das Brett des "
     "Karneades. [antik]Das antike Gedankenexperiment wird auf den griechischen Philosophen Karneades zurückgeführt.", PS),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand und Rechtswidrigkeit ----------------------------------------------------------------------------------
    ("[tb]Zuerst der Tatbestand: [tb212]Herr Tamm hat einen Menschen getötet, Paragraf zweihundertzwölf, [vors]und zwar "
     "vorsätzlich. [rw]Gerechtfertigt ist die Tat nicht: [p34]Paragraf vierunddreißig scheitert, weil sich Leben nicht gegen "
     "Leben abwägen lässt, [v263]mehr dazu im Video zum übergesetzlichen Notstand.", PS),
    # --- D § 35 Abs. 1 S. 1 (Wortlautkarte) ---------------------------------------------------------------------------------
    ("[p35]Bleibt die Schuld. Paragraf fünfunddreißig Absatz eins Satz eins: [w1]Wer in einer gegenwärtigen, nicht anders "
     "abwendbaren Gefahr für Leben, Leib oder Freiheit eine rechtswidrige Tat begeht, um die Gefahr von sich, einem "
     "Angehörigen oder einer anderen ihm nahestehenden Person abzuwenden, handelt ohne Schuld.", PS),
    ("[gefahr]Im Wasser droht Herrn Tamm der Tod, und zwar sofort: [gegenw]Die Gefahr ist gegenwärtig. [anders]Rettung ist "
     "nicht in Sicht, und die Planke trägt nur einen. Die Gefahr ist nicht anders abwendbar. [eigen]Es geht um sein eigenes "
     "Leben, [rettw]und er handelt, um sich zu retten. Diesen Rettungswillen verlangt das Gesetz mit den Worten: um die "
     "Gefahr abzuwenden.", PS),
    # --- E § 35 Abs. 1 S. 2 (Wortlautkarte): Hinnahmepflicht -----------------------------------------------------------------
    ("[satz2]Aber Satz zwei macht eine Ausnahme: [s2w]Die Entschuldigung entfällt, soweit dem Täter zugemutet werden "
     "konnte, die Gefahr hinzunehmen. [zwei]Das Gesetz nennt zwei Beispiele. [verurs]Erstens: Er hat die Gefahr selbst "
     "verursacht. [kaus]Bloße Ursächlichkeit genügt dafür nicht, verlangt wird ein pflichtwidriges Verhalten. [gast]Herr Tamm "
     "war nur Fahrgast. Den Untergang hat er nicht herbeigeführt.", P),
    ("[rv]Zweitens: ein besonderes Rechtsverhältnis. [beruf]Darin stehen etwa Feuerwehrleute, Polizisten und Soldaten. "
     "[pflicht]Sie haben Schutzpflichten für andere übernommen und müssen berufstypische Gefahren eher hinnehmen. "
     "[frei]Auch das trifft Herrn Tamm nicht. [entsch]Er ist entschuldigt.", PS),
    # --- F Abwandlung 1: Kapitän --------------------------------------------------------------------------------------------
    ("[abw1]Erste Abwandlung: Nicht Herr Tamm, sondern der Kapitän des Bootes stößt einen Fahrgast von der Planke. "
     "[kap1]Der Kapitän ist für die Sicherheit an Bord verantwortlich, [kap2]seine Pflicht gilt gerade dem Schutz der "
     "Fahrgäste. Er steht in einem besonderen Rechtsverhältnis. [kap3]Zwar muss nach verbreiteter Ansicht niemand den "
     "sicheren Tod hinnehmen. [kap4]Doch wer die Gefahr gerade auf den abwälzt, den er schützen muss, dem kommt Paragraf "
     "fünfunddreißig nach der Lehre nicht zugute. [kap5]Der Kapitän ist wegen Totschlags strafbar, [kap6]und die Strafmilderung aus Satz zwei steht "
     "ihm nicht offen.", PS),
    # --- G Abwandlung 2: Irrtum, § 35 Abs. 2 (Wortlautkarte) ----------------------------------------------------------------
    ("[abw2]Zweite Abwandlung: Ein Rettungsboot hätte beide noch rechtzeitig erreicht, doch Herr Tamm sah es in den Wellen nicht. "
     "[objektiv]Objektiv war die Gefahr also anders abwendbar. [abs2]Hier hilft Absatz zwei: [w2]Nimmt der Täter irrig "
     "Umstände an, die ihn entschuldigen würden, wird er nur bestraft, wenn er den Irrtum vermeiden konnte.", PS),
    ("[bgh]Für die Vermeidbarkeit fragt der Bundesgerichtshof im Haustyrannen-Fall, ob der Täter mögliche Auswege "
     "gewissenhaft geprüft hat. [streng]Geht es um ein Menschenleben, sind die Anforderungen streng. [zeit]Es zählt aber "
     "auch, wie viel Zeit für eine ruhige Überlegung blieb. [sek]Im Sturm, in Sekunden, spricht einiges für einen "
     "unvermeidbaren Irrtum: Herr Tamm bliebe straflos. [verm]War der Irrtum vermeidbar, wird er bestraft, die Strafe ist "
     "dann aber zwingend zu mildern. [v007]Den Haustyrannen-Fall erklärt ein eigenes Video.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Im Ausgangsfall gilt also: [erg1]Herr Tamm hat rechtswidrig getötet, [erg2]ist aber nach Paragraf fünfunddreißig "
     "entschuldigt und bleibt straflos. [erg3]Der Kapitän der Abwandlung bleibt strafbar.", P),
    ("[pe2]Ihre Aussage geht jetzt an die Staatsanwaltschaft.", PS, "Petzold"),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Paragraf fünfunddreißig prüfst du in der Schuld, erst nach der Rechtswidrigkeit. [t1]Die Tat bleibt "
     "rechtswidrig. Gegen sie ist deshalb Notwehr möglich. [t2]Und vergiss Satz zwei nicht: [t3]Viele prüfen nur Gefahr und "
     "Personenkreis und übersehen die Hinnahmepflicht.", PS),
    # --- J Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Eins, Tatbestand, Paragraf zweihundertzwölf. [s2]Zwei, Rechtswidrigkeit: kein Paragraf "
     "vierunddreißig. [s3]Drei, Schuld: Paragraf fünfunddreißig. [s4]Gegenwärtige Gefahr für Leben, Leib oder Freiheit von "
     "dir oder einem Nahestehenden, [s5]nicht anders abwendbar, mit Rettungswillen, [s6]keine Hinnahmepflicht nach Satz zwei, "
     "[s7]bei einem Irrtum Absatz zwei. [s8]Vier, Ergebnis.", PS),
    # --- K Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Auf dem Brett des Karneades ist die Tötung rechtswidrig, aber entschuldigt. [m2]Wer die Gefahr selbst "
     "verursacht hat oder in einem besonderen Rechtsverhältnis steht, muss sie unter Umständen hinnehmen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
