"""Folge 261 · Beurteilungsspielraum: Kann man eine Examensnote einklagen? (Fr · Klausurpraxis · Verwaltungsrecht AT,
Format Klassiker-Fall). Übungsfall nach dem Plan-Hook („Deine Examensklausur bekommt 5 Punkte – obwohl deine Lösung
fachlich vertretbar war.“): Jorinde folgt in einer Examensklausur im Öffentlichen Recht bei einer Streitfrage der
Gegenansicht und begründet sie folgerichtig mit gewichtigen Argumenten. Ihr Prüfer, Herr Ellerbrock, schreibt „falsch“
und „insgesamt oberflächlich“ und vergibt 5 Punkte. Jorinde will 9 Punkte einklagen.
Aufbau laut Auftrag: 1. Hook → Sachverhalt → 2. Grundsatz: volle gerichtliche Kontrolle (Art. 19 Abs. 4 S. 1 GG als
Wortlautkarte, BVerfGE 84, 34 <49 f.>), unbestimmte Rechtsbegriffe, Abgrenzung zum Ermessen in einem Satz (Verweis 074),
Notenstufe „ausreichend“ (§ 1 JurPrNotSkV), Art. 12 Abs. 1 GG → 3. Ausnahme: Beurteilungsspielraum nur bei
prüfungsspezifischen Wertungen (BVerfGE 84, 34 <51 ff.>; BVerwG 6 B 71.17 Rn. 9 f.), Fachfragen voll kontrollierbar,
Antwortspielraum (BVerfGE 84, 34 <55>; BVerwG 6 B 16.20 Rn. 10) → 4. Kontrolldichte (BVerfGE 84, 34 <53 f.>; 6 B 71.17
Rn. 10), Kausalität (<55>) → 5. Überdenkungsverfahren (BVerfGE 84, 34 <48 f.>; BVerwG 6 C 19.18 Rn. 25, 26, 28;
Beispiel § 27 Abs. 1, § 27a JAG NRW) → 6. Fall: Überdenken, Klage, Neubewertung (BVerfGE 84, 34 <55 f.>; 6 B 16.20 Rn. 3;
§ 113 Abs. 5 S. 2 VwGO) → 7. Klausurtipp (Lexi), Schema, Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung
„261: Jorinde, Ellerbrock“); nie im Genitiv. Die Richterin bleibt namenlos.
Stimmen (Pool stephan, hilde, christian, lucy): Jorinde lucy (Frau, jung), Herr Ellerbrock christian (Mann, mittel),
die Richterin hilde (Frau, älter); stephan nicht verwendet (also nie stephan und christian in einer Szene).
Lexi = Erzählerin Carla. „JAG“ steht nicht in der Abkürzungsliste von synth_el.py; gesprochen wird „Juristenausbildungsgesetz“.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Jorinde": "lucy", "Ellerbrock": "christian", "Richterin": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Klausur und Korrektur ----------------------------------------------------------------------------------
    # Nachvertonung 08.10.2026 (Segmente 1 und 19): Erstfassung „Jorinde schreibt ihre Examensklausuren.“ – whisper small und
    # medium hörten übereinstimmend „Jorinda“ (im Satz und isoliert); Erstfassung Segment 19 „Neun Punkte kann Jorinde nicht
    # einklagen.“ – beide Modelle im Satz „Jurinde“. Name jeweils an eine andere Satzstelle gestellt.
    ("[fall]Examenszeit für Jorinde. Sie schreibt ihre Klausuren. [klausur]Im Öffentlichen Recht stößt sie auf eine Streitfrage. "
     "[gegen]Sie folgt der Gegenansicht und begründet sie Schritt für Schritt. [ellerbrock]Herr Ellerbrock korrigiert "
     "die Arbeit.", P),
    ("[el1]Diese Ansicht ist falsch. Insgesamt oberflächlich: fünf Punkte.", P, "Ellerbrock"),
    ("[bescheid]Wochen später bekommt Jorinde den Bescheid des Prüfungsamts und sieht die Korrektur.", 0.2),
    ("[jo1]Falsch? Meine Lösung ist vertretbar! Ich klage mir neun Punkte ein.", P, "Jorinde"),
    ("[hook]Deine Examensklausur bekommt fünf Punkte, obwohl deine Lösung fachlich vertretbar war. [frage]Kann man eine "
     "Examensnote einklagen? [frage2]Und was darf das Gericht überhaupt prüfen?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Grundsatz: volle Kontrolle -----------------------------------------------------------------------------------
    ("[grund]Zuerst der Grundsatz. [wl19]Artikel neunzehn Absatz vier Grundgesetz: Wird jemand durch die öffentliche "
     "Gewalt in seinen Rechten verletzt, so steht ihm der Rechtsweg offen. [wirksam]Das Bundesverfassungsgericht verlangt "
     "eine wirksame Kontrolle: Das Gericht prüft grundsätzlich rechtlich und tatsächlich vollständig. [ubr]Das gilt auch für "
     "unbestimmte Rechtsbegriffe. Sie zu konkretisieren, ist Sache der Gerichte. [erm]Anders beim Ermessen auf der "
     "Rechtsfolgenseite, mehr dazu in Folge vierundsiebzig.", P),
    ("[note]Auch die Notenstufen sind nur unbestimmt umschrieben. [ausr]Ausreichend heißt: eine Leistung, die trotz "
     "ihrer Mängel durchschnittlichen Anforderungen noch entspricht. [art12]Und weil Examensnoten über den Zugang zum "
     "Beruf entscheiden, schützt Artikel zwölf Absatz eins die Prüflinge, die Berufsfreiheit.", PS),
    # --- D Ausnahme: Beurteilungsspielraum -------------------------------------------------------------------------------
    ("[aber]Trotzdem setzt das Gericht keine eigene Note fest. [bezug]Prüfer bewerten im Vergleich mit vielen anderen "
     "Arbeiten und aus ihrer Erfahrung. [chance]Bekäme eine einzelne Kandidatin vor Gericht eine Bewertung unabhängig "
     "von diesem Vergleich, wäre die Chancengleichheit verletzt. [bsr]Deshalb haben Prüfer einen Beurteilungsspielraum, "
     "aber nur bei prüfungsspezifischen Wertungen.", P),
    ("[spez]Prüfungsspezifisch sind etwa der Schwierigkeitsgrad der Aufgabe, [gew]die Gewichtung von Stärken und "
     "Schwächen [eindr]und der Gesamteindruck. [eing]Hier prüft das Gericht nur eingeschränkt.", P),
    ("[fach]Anders bei fachlichen Fragen: Ist eine Ansicht richtig oder vertretbar? Das prüft das Gericht voll, notfalls "
     "mit Sachverständigen. [anspr]Hier hat der Prüfling einen Antwortspielraum. [wlbv]Das Bundesverfassungsgericht: Eine "
     "vertretbare und mit gewichtigen Argumenten folgerichtig begründete Lösung darf nicht als falsch gewertet werden. "
     "[beide]Vertretbar allein genügt also nicht. Die Lösung muss auch gut begründet sein.", PS),
    # --- E Kontrolldichte ------------------------------------------------------------------------------------------------
    ("[kontr]Und bei den prüfungsspezifischen Wertungen? Ganz frei ist der Prüfer auch dort nicht. [k1]Das Gericht "
     "prüft, ob Verfahrensfehler vorliegen, [k2]ob der Prüfer von einem falschen Sachverhalt ausging, etwa einen Teil der "
     "Arbeit übersehen hat, [k3]ob er allgemeingültige Bewertungsmaßstäbe verletzt [k4]oder sich von sachfremden "
     "Erwägungen hat leiten lassen. [kaus]Korrigiert wird aber nur, wenn sich der Fehler auf die Note ausgewirkt haben "
     "kann.", PS),
    # --- F Überdenkungsverfahren -----------------------------------------------------------------------------------------
    ("[ued]Weil das Gericht hier so wenig prüft, gibt es einen Ausgleich: das Überdenkungsverfahren. [ued2]Nach dem "
     "Bundesverfassungsgericht muss der Prüfling seine Einwände wirksam vorbringen und so ein Überdenken der Bewertung "
     "erreichen können. [subst]Die Einwände müssen konkret sein. Pauschal „zu streng“ genügt nicht. [mass]Die Prüfer "
     "bewerten dann nicht völlig neu. Sie setzen sich mit den beanstandeten Punkten auseinander, ihr Maßstab bleibt "
     "derselbe.", P),
    ("[land]Wie das abläuft und welche Fristen gelten, regelt dein Land. [nrw]In Nordrhein-Westfalen etwa holt das "
     "Prüfungsamt im Widerspruchsverfahren Stellungnahmen der Prüfer ein, Paragraf siebenundzwanzig "
     "Juristenausbildungsgesetz. [frist]Einwände gegen Klausuren sind binnen sechs Monaten im Einzelnen zu begründen.", PS),
    # --- G Der Fall: Überdenken, Klage, Urteil ---------------------------------------------------------------------------
    ("[zurueck]Zurück zu Jorinde. [einw]Sie erhebt Einwände und belegt, dass ihre Ansicht vertreten wird. [ueb]Herr "
     "Ellerbrock überdenkt seine Bewertung und bleibt dabei.", 0.2),
    ("[el2]Die Ansicht bleibt falsch. Es bleibt bei fünf Punkten.", P, "Ellerbrock"),
    ("[klage]Jorinde klagt. [fehler]Ihre Lösung ist vertretbar und mit gewichtigen Argumenten folgerichtig begründet. "
     "Sie als falsch zu werten, ist ein Bewertungsfehler. [obfl]„Oberflächlich“ ist dagegen eine prüfungsspezifische "
     "Wertung, ein Fehler ist hier nicht erkennbar. [ausw]Der Bewertungsfehler kann sich aber auf die Note ausgewirkt "
     "haben. [urteil]Die Richterin verkündet:", 0.2),
    ("[ri1]Das beklagte Land wird verpflichtet, die Klausur neu bewerten zu lassen und die Klägerin neu zu bescheiden. "
     "Im Übrigen wird die Klage abgewiesen.", 0.4, "Richterin"),
    ("[ergeb]Das Ergebnis ist in der Regel eine Neubewertung, keine Note vom Gericht. [neun]Jorinde kann also keine neun "
     "Punkte einklagen. [prue]Die Note setzen wieder die Prüfer fest, diesmal ohne den Fehler. [offen]Ob es mehr Punkte werden, ist offen. [bu]Prozessual ist das ein "
     "Bescheidungsurteil, Paragraf hundertdreizehn Absatz fünf Satz zwei Verwaltungsgerichtsordnung.", PS),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne sauber zwischen Fachfrage und prüfungsspezifischer Wertung. [tipp2]Bei der Fachfrage "
     "prüfst du voll, mit dem Antwortspielraum. Bei der Wertung prüfst du nur die Grenzen. [tipp3]Und das Klageziel ist in "
     "der Regel die Neubewertung, nicht eine bestimmte Note.", PS),
    # --- I Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Begründetheit. [s1]Eins: Verfahrensfehler, auch beim Überdenken. [s2]Zwei: Fehler bei "
     "Fachfragen, also der Antwortspielraum. [s3]Drei: die Grenzen des Beurteilungsspielraums, [s3a]Sachverhalt, "
     "Maßstäbe, sachfremde Erwägungen. [s4]Vier: Auswirkung auf die Note. [s5]Fünf: die Folge, Neubewertung durch die "
     "Prüfer.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei prüfungsspezifischen Wertungen haben die Prüfer Spielraum. [m2]Bei Fachfragen nicht. Was "
     "vertretbar und gut begründet ist, darf nicht falsch sein.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
