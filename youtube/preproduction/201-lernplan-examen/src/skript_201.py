"""Folge 201 · Lernplan Examen: So teilst du 12 Monate Vorbereitung ein (Fr · Methodik · Lernen, Format Schritte).
Rahmen nach dem Plan-Hook („Examen in einem Jahr – womit fängst du an?“): Die Jurastudentin Fenna (Mitte 20, studiert in
Nordrhein-Westfalen) steht ein Jahr vor den Klausuren der staatlichen Pflichtfachprüfung vor einem leeren Wandkalender.
Nils (um 28, Referendar, hat das Examen im letzten Jahr geschrieben) hilft ihr, rückwärts zu planen.
Aufbau in sechs Schritten mit 12 Monatsbalken als Tafel: 1. Bestandsaufnahme (Pflichtfächer, § 5a Abs. 2 S. 3 DRiG als
Wortlautkarte; Landesrecht, § 5a Abs. 4, § 5d Abs. 6 S. 1 DRiG; Beispiel NRW: § 10 Abs. 2, § 11 Abs. 2, § 13 Abs. 1 JAG NRW;
Ampel) → 2. Rückwärtsplanung vom Examenstermin (Freiversuch § 5d Abs. 5 S. 2, 3 DRiG; Endspurt, Puffermonat, neun Monate
Stoff) → 3. Stoffphase (Gewichtung als Empfehlung) → 4. Wiederholung (Faustregel Intervalle; Verweis 123) → 5. Klausuren
von Anfang an (Verweise 045, 117) → 6. Puffer, Pausen, Endspurt → Beispielwoche (Wochenplan als Tafel) → Ergebnis →
Klausurtipp (Lexi) → Lernplan als Schema I.–VI. → Merksatz (Lexi).
Alle Zeitanteile, Monatszahlen und Intervalle sind Empfehlungen (im Sprechtext so gekennzeichnet); keine Studien, keine
Anbieter. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche unter youtube/: 0 Treffer): Fenna, Nils; nie im
Genitiv.
Stimmen (Pool hilde, christian, lucy, stephan): Fenna lucy (Frau, jung), Nils christian (Mann, mittel); stephan (Vorfolge 200)
und hilde nicht verwendet, keine Stephan/Christian-Paarung. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Fenna": "lucy", "Nils": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: ein Jahr vor dem Examen, der leere Wandkalender ------------------------------------------------------
    ("[fall]Noch ein Jahr bis zum Examen. [fenna]Fenna steht vor einem leeren Wandkalender, [stapel]auf dem Tisch ein "
     "Stapel Bücher.", P),
    ("[f1]Zwölf Monate, drei Rechtsgebiete. Womit fange ich bloß an?", P, "Fenna"),
    ("[nils]Nils hat das Examen im letzten Jahr geschrieben. [tassen]Er stellt zwei Tassen auf den Tisch.", P),
    ("[n1]Mit dem Ende. Wir planen rückwärts, vom Examen aus.", P, "Nils"),
    ("[hook]Examen in einem Jahr: Womit fängst du an? [hook2]Nicht mit dem ersten Kapitel, sondern mit einem Plan. "
     "[sechs]Den baust du in sechs Schritten, Monat für Monat.", P),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist die Ausgangslage von Fenna. Halte das Video ruhig kurz an.", 5.0),
    # --- C Schritt 1: Bestandsaufnahme – was wird geprüft? ---------------------------------------------------------------
    ("[s1]Schritt eins: die Bestandsaufnahme. Was wird geprüft? [drig]Den Rahmen setzt das Deutsche Richtergesetz. "
     "[p5a]Paragraf fünf a Absatz zwei: [p5aw]Pflichtfächer sind die Kernbereiche des Bürgerlichen Rechts, des "
     "Strafrechts, des Öffentlichen Rechts und des Verfahrensrechts, [p5ae]dazu europarechtliche Bezüge, Methoden und "
     "Grundlagen.", P),
    ("[land]Das Nähere regelt das Landesrecht. [nrw]Fenna studiert in Nordrhein-Westfalen. Dort schreibt sie sechs "
     "Klausuren: [nrw3]drei im Zivilrecht, [nrw2]zwei im Öffentlichen Recht [nrw1]und eine im Strafrecht, [fuenf]jede "
     "fünf Stunden lang. [katalog]Welche Gebiete genau dazugehören, listet Paragraf elf des Juristenausbildungsgesetzes. "
     "[eigen]In deinem Land prüfst du das in deinem Ausbildungsgesetz oder deiner Prüfungsordnung.", P),
    ("[ampel]Dann geh den Katalog durch und gib jedem Gebiet eine Ampelfarbe. [agruen]Bei Fenna ist das Strafrecht grün, "
     "[agelb]das Zivilrecht gelb [arot]und das Öffentliche Recht rot.", P),
    # --- D Schritt 2: rückwärts planen ----------------------------------------------------------------------------------
    ("[s2]Schritt zwei: Plane rückwärts. [monate]Zwölf Monate liegen vor Fenna, [ex]am Ende von Monat zwölf steht das "
     "Examen. [fv]Prüfe dabei den Freiversuch: Wer sich frühzeitig meldet und alle Prüfungsleistungen erbringt, für den "
     "gilt eine nicht bestandene Pflichtfachprüfung als nicht unternommen. [frist]Die Meldefrist regelt dein Land.", P),
    ("[end]Jetzt rechnest du vom Termin zurück, als Empfehlung: [acht]Die letzten acht Wochen gehören nur noch der Wiederholung und den "
     "Klausuren. [puf]Davor liegt ein Puffermonat. [neun]Für den Stoff bleiben neun Monate.", P),
    # --- E Schritt 3: die Stoffphase ------------------------------------------------------------------------------------
    ("[s3]Schritt drei: die Stoffphase. [gew]Wie du die neun Monate verteilst, ist eine Empfehlung, keine Regel. "
     "[gew2]Richte dich nach dem Gewicht in der Prüfung und nach deiner Ampel. [zr]Fenna gibt dem Zivilrecht vier "
     "Monate, denn es stellt die Hälfte ihrer Klausuren. [oer]Das Öffentliche Recht bekommt drei Monate, weil es bei ihr "
     "rot ist. [sr]Für das Strafrecht reichen zwei. [proz]Das Prozessrecht lernt sie im jeweiligen Block mit.", P),
    # --- F Schritt 4: Wiederholung ----------------------------------------------------------------------------------------
    ("[s4]Schritt vier: das Wiederholungssystem. [abruf]Gelernt ist erst, was du später noch abrufen kannst. "
     "[faust]Eine Faustregel: Wiederhole in wachsenden Abständen, [i1]nach einem Tag, [i2]nach einer Woche, [i3]nach "
     "einem Monat. [karte]Fenna nutzt dafür Karteikarten und Schemata. [kopf]Sie schreibt ein Schema zuerst aus dem Kopf "
     "auf und vergleicht es dann mit dem Gesetz, wie in Folge hundertdreiundzwanzig. [stunde]Jeden Tag gehört die erste "
     "Stunde der Wiederholung, [alt]auch für die Gebiete, die schon fertig sind.", P),
    # --- G Schritt 5: Klausuren von Anfang an ---------------------------------------------------------------------------
    ("[s5]Schritt fünf: Klausuren von Anfang an. [woche]Fenna schreibt ab der ersten Woche jede Woche eine Klausur, "
     "[bed]unter Examensbedingungen: fünf Stunden am Stück. [frueh]Auch wenn noch Stoff fehlt. Denn das Schreiben unter "
     "Zeitdruck ist eine eigene Übung. [korr]Lass jede Klausur korrigieren, zum Beispiel in einem Klausurenkurs an der Uni.", P),
    ("[n2]Meine ersten Klausuren waren schwach. Aber aus jeder Korrektur habe ich mir die Fehler notiert.", P, "Nils"),
    ("[v045]Wie du die fünf Stunden einteilst, zeigt Folge fünfundvierzig, [v117]die typischen Fehler Folge "
     "hundertsiebzehn.", P),
    # --- H Schritt 6: Puffer, Pausen, Endspurt ----------------------------------------------------------------------------
    ("[s6]Schritt sechs: Puffer und Pausen. [frei]Ein Tag pro Woche bleibt frei. [urlaub]Den Urlaub trägst du fest ein, "
     "bei Fenna zwei Wochen. [pmonat]Der Puffermonat fängt auf, was liegen bleibt, etwa eine Krankheit oder ein Thema, das "
     "länger dauert.", P),
    ("[f2]Und wenn ich trotzdem hinter dem Plan liege?", P, "Fenna"),
    ("[n3]Dann nimmst du den Puffer. Dafür ist er da.", P, "Nils"),
    ("[spurt]In den letzten sechs bis acht Wochen lernst du keinen neuen Stoff mehr. [spurt2]Fenna nimmt sich acht: "
     "nur noch wiederholen und Klausuren schreiben, jetzt zwei pro Woche.", PS),
    # --- I Beispielwoche ------------------------------------------------------------------------------------------------
    ("[wp]So sieht eine Woche von Fenna in der Stoffphase aus. [wp1]Von Montag bis Freitag beginnt sie mit einer Stunde "
     "Karteikarten. [wp2]Vormittags lernt sie den Stoff ihres Blocks, [wp3]nachmittags löst sie Fälle dazu. "
     "[wp4]Am Montagnachmittag wertet sie die Klausur vom Samstag aus. [wp5]Am Freitagnachmittag wiederholt sie die "
     "anderen Gebiete und prüft ihren Plan. [wp6]Samstag ist Klausurtag, fünf Stunden. [wp7]Und der Sonntag ist frei.", P),
    # --- J Ergebnis: der Plan hängt -------------------------------------------------------------------------------------
    ("[erg]Am Ende hängt der Plan von Fenna an der Wand.", 0.2),
    ("[f3]Jetzt weiß ich, womit ich anfange: mit Monat eins, Zivilrecht. Und am Samstag mit der ersten Klausur.", PS,
     "Fenna"),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib deine Übungsklausuren so, wie das Examen läuft. [tipp2]Fünf Stunden am Stück, nur mit "
     "den Hilfsmitteln, die in deinem Land erlaubt sind, [tipp3]und in der Form, in der du schreibst: von Hand oder am "
     "Computer. [tipp4]Deine Fehlerliste aus den Korrekturen zeigt dir dann, was du als Nächstes wiederholst.", PS),
    # --- L Lernplan als Schema --------------------------------------------------------------------------------------------
    ("[sch]Dein Lernplan in sechs Schritten. [k1]Römisch eins: Bestandsaufnahme, also Stoffkatalog und Ampel. "
     "[k2]Römisch zwei: rückwärts planen vom Examenstermin. [k3]Römisch drei: die Stoffphase, gewichtet nach Prüfung "
     "und Ampel. [k4]Römisch vier: Wiederholung in wachsenden Abständen. [k5]Römisch fünf: jede Woche eine Klausur, von "
     "Anfang an. [k6]Römisch sechs: Puffer, freie Tage und acht Wochen Endspurt.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Lernplan beginnt beim Examenstermin und rechnet rückwärts. [m2]Stoff, Wiederholung und Klausuren "
     "laufen jede Woche nebeneinander, [m3]und der Puffer gehört von Anfang an dazu.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
