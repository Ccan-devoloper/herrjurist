"""Folge 281 · Mietminderung § 536 BGB: Schimmel, Baulärm, kalte Heizung (Mi · Examenswissen · Mietrecht · Alltagsfall;
§§ 536, 536b, 536c BGB; zusätzlich § 535, § 543 Abs. 2 Satz 1 Nr. 3, § 320, § 441 Abs. 1 (Vergleich), § 906 BGB).
Beispielfall nach dem Plan-Hook („In deiner Wohnung wächst Schimmel – darfst du einfach weniger Miete überweisen?“):
Friedemann mietet von Frau Teuber eine Altbauwohnung für 850 € warm (700 € kalt + 150 € Nebenkostenvorauszahlung).
Im November Schimmel hinter dem Schrank an der Außenwand, Anzeige erst im Januar; seit Dezember Neubau auf dem
Nachbargrundstück (Bagger, Presslufthammer ab 7 Uhr); im Januar eine Woche kalte Heizung, am selben Tag gemeldet.
Frau Teuber: Schimmel vom Lüften, für die Baustelle könne sie nichts. Friedemann will ab Februar nur die Hälfte zahlen.
Aufbau laut Auftrag: Hook → § 536 Abs. 1 (Wortlautkarte S. 1–3), kraft Gesetzes (Vergleich § 441 Abs. 1 in einem Satz),
Mangel, Unerheblichkeit, Bruttomiete → drei Beispiele (Schimmel mit Beweislast, Baulärm nach Bolzplatz/Baustelle,
kalte Heizung) → § 536c (Wortlautkarte Abs. 1 S. 1, Abs. 2 S. 2 Nr. 1) → § 536b (Wortlautkarte S. 1) → Praxisrisiko
(§ 543, VIII ZR 138/11, Vorbehalt; § 320 in einem Satz, VIII ZR 19/14) → Ergebnis → Klausurtipp → Schema → Merksatz.
Belege je Cue in ../RECHTSSTAND.md. Keine Minderungsquoten (nur „Einzelfall“).
Stimmen (Pool stephan, hilde, christian, lucy): Friedemann (christian, Mann, mittel), Frau Teuber (hilde, Frau, älter);
stephan und lucy (Vorfolge 278) nicht besetzt, stephan und christian also nie gemeinsam. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Friedemann": "christian", "Teuber": "hilde"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: in der Wohnung ---------------------------------------------------------------------------------------
    ("[fall]In deiner Wohnung wächst Schimmel. Darfst du einfach weniger Miete überweisen? [fried]Das fragt sich "
     "Friedemann. Er mietet eine Altbauwohnung für achthundertfünfzig Euro warm. [schim]Im November entdeckt er "
     "hinter dem Schrank im Schlafzimmer Schimmel an der Außenwand. Seiner Vermieterin sagt er erst im Januar Bescheid. "
     "[bau]Seit Dezember baut der Nachbar ein neues Haus, tagsüber dröhnt der Presslufthammer. [kalt]Und im "
     "Januar bleibt die Heizung eine Woche lang kalt. Das meldet Friedemann noch am selben Tag.", P),
    # --- A2 Dialog -----------------------------------------------------------------------------------------------------
    ("[teub]Frau Teuber, die Vermieterin, sieht sich alles an.", P),
    ("[t1]Der Schimmel kommt vom Lüften. Und für die Baustelle nebenan kann ich nichts.", P, "Teuber"),
    ("[f1]Dann überweise ich ab Februar nur noch die halbe Miete.", P, "Friedemann"),
    ("[frage]Ist seine Miete gemindert? [frage2]Muss Friedemann etwas erklären? [frage3]Und was riskiert er, wenn er "
     "zu viel abzieht?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 536 Abs. 1 (Wortlautkarte Satz 1–3), kraft Gesetzes, Mangel, Unerheblichkeit, Bruttomiete -----------------
    ("[w536]Die Antwort gibt Paragraf fünfhundertsechsunddreißig Absatz eins: Hat die Mietsache einen Mangel, der ihre "
     "Tauglichkeit zum vertragsgemäßen Gebrauch aufhebt, ist der Mieter von der Miete befreit. [w536s2]Ist die "
     "Tauglichkeit nur gemindert, zahlt er eine angemessen herabgesetzte Miete. [w536s3]Eine unerhebliche Minderung "
     "bleibt außer Betracht.", P),
    ("[kraft]Das geschieht kraft Gesetzes. Friedemann muss nichts erklären, anders als ein Käufer, der den Kaufpreis nach "
     "Paragraf vierhunderteinundvierzig durch Erklärung mindert. [mangel]Ein Mangel liegt vor, wenn der tatsächliche "
     "Zustand zum Nachteil des Mieters vom vertraglich vorausgesetzten abweicht. [unerh]Unerheblich ist etwa ein Fehler, der leicht "
     "erkennbar ist und schnell und mit geringen Kosten behoben werden kann. [brutto]Gerechnet wird nach dem "
     "Bundesgerichtshof von der Bruttomiete, also samt Nebenkosten: bei Friedemann von achthundertfünfzig Euro.", PS),
    # --- D1 Beispiel 1: Schimmel (Ursache, Beweislast nach Verantwortungsbereichen, Baustandard) ----------------------
    ("[drei]Jetzt die drei Probleme von Friedemann. [s1]Erstens der Schimmel. Er ist ein Mangel, wenn er auf einem Baumangel "
     "beruht, etwa auf einer feuchten Wand. [s1b]Kommt er davon, dass zu wenig gelüftet und geheizt wird, ist "
     "die Wohnung nicht mangelhaft. [bew]Nach dem Bundesgerichtshof muss zuerst Frau Teuber "
     "beweisen, dass die Ursache nicht aus ihrem Verantwortungsbereich stammt. [bew2]Gelingt ihr das, muss Friedemann "
     "beweisen, dass er den Schimmel nicht zu vertreten hat. [alt]Wärmebrücken in einem Altbau sind kein Mangel, wenn "
     "sie den Bauvorschriften seiner Bauzeit entsprechen; welches Lüften zumutbar ist, entscheidet der Einzelfall.", P),
    # --- D2 Beispiel 2: Baulärm vom Nachbargrundstück (Bolzplatz, Baustelle) --------------------------------------------
    ("[s2]Zweitens der Baulärm von nebenan. Er ist grundsätzlich kein Mangel, wenn auch Frau Teuber ihn als Eigentümerin "
     "ohne eigene Abwehr- oder Entschädigungsmöglichkeit hinnehmen muss. [bolz]So hat der Bundesgerichtshof für einen "
     "Bolzplatz neben der Wohnung entschieden und später für eine Baustelle bestätigt. [s2b]Friedemann muss darlegen, dass der Lärm seine Wohnung wesentlich beeinträchtigt. "
     "[s2c]Beruft sich Frau Teuber darauf, gegen den Nachbarn "
     "keine Ansprüche zu haben, muss sie die Tatsachen aus ihrem Bereich beweisen.", P),
    # --- D3 Beispiel 3: kalte Heizung ---------------------------------------------------------------------------------
    ("[s3]Drittens die kalte Heizung. Auch die Wärme schuldet die Vermieterin. "
     "[s3b]Fällt die Heizung im Januar aus, ist die Tauglichkeit der Wohnung für diese Zeit gemindert. [s3c]Um wie viel, hängt vom "
     "Einzelfall ab, etwa von Dauer und Außentemperatur.", PS),
    # --- E § 536c (Wortlautkarte Abs. 1 S. 1, Abs. 2 S. 2 Nr. 1) -------------------------------------------------------
    ("[w536c]Paragraf fünfhundertsechsunddreißig c: Zeigt sich im Laufe der Mietzeit ein Mangel, so hat "
     "der Mieter dies dem Vermieter unverzüglich anzuzeigen. [w536c2]Soweit der Vermieter infolge der unterlassenen "
     "Anzeige nicht Abhilfe schaffen konnte, darf der Mieter die Rechte aus Paragraf fünfhundertsechsunddreißig nicht "
     "geltend machen. [anz]Beim Schimmel wusste Frau Teuber von November bis Januar nichts. Konnte sie deshalb nicht "
     "abhelfen, scheidet für diese Zeit eine Minderung aus. [anz2]Die Heizung hat Friedemann sofort gemeldet, dort greift "
     "die Sperre nicht.", PS),
    # --- F § 536b (Wortlautkarte S. 1) ---------------------------------------------------------------------------------
    ("[w536b]Paragraf fünfhundertsechsunddreißig b: Kennt der Mieter bei Vertragsschluss den Mangel der Mietsache, so "
     "stehen ihm die Rechte aus den Paragrafen fünfhundertsechsunddreißig und fünfhundertsechsunddreißig a nicht zu. "
     "[kennt]Hätte Friedemann den Schimmel schon bei der Besichtigung gesehen und trotzdem unterschrieben, könnte er "
     "nicht mindern.", PS),
    # --- G Praxisrisiko: zu hohe Minderung, Verzug, § 543; Vorbehalt; § 320 -------------------------------------------
    ("[risk]Und die halbe Miete? Das ist riskant. [verz]Mindert Friedemann zu viel, gerät er mit dem Rest in "
     "Verzug. Erreicht der Rückstand etwa zwei Monatsmieten, darf Frau Teuber nach Paragraf fünfhundertdreiundvierzig "
     "fristlos kündigen. [irrt]Ein Irrtum über die Ursache entschuldigt ihn nach dem Bundesgerichtshof nicht, "
     "wenn er ihn bei verkehrsüblicher Sorgfalt hätte erkennen können. [vorb]Sicherer ist es, die "
     "volle Miete unter Vorbehalt zu zahlen und den Mehrbetrag zurückzufordern. [p320]Daneben darf er nach "
     "Paragraf dreihundertzwanzig einen Teil der Miete zurückbehalten, um Druck für die Reparatur zu machen, aber nur "
     "zeitlich und der Höhe nach begrenzt.", PS),
    # --- H Ergebnis ----------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Für die kalte Woche ist die Miete kraft Gesetzes gemindert. [erg2]Beim Schimmel kommt es auf die "
     "Ursache an, und für die Zeit vor der Anzeige kann die Minderung ausgeschlossen sein. [erg3]Beim Baulärm nur, wenn "
     "Frau Teuber selbst gegen den Nachbarn vorgehen oder Entschädigung verlangen könnte.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Minderung ist keine eigene Anspruchsgrundlage des Mieters. [tipp2]Du prüfst sie im Anspruch "
     "der Vermieterin auf Miete aus Paragraf fünfhundertfünfunddreißig Absatz zwei: Geschuldet ist nur die geminderte "
     "Miete. [tipp3]Hat der Mieter voll gezahlt, verlangt er den Mehrbetrag nach Bereicherungsrecht zurück.", PS),
    # --- L Prüfungsschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Vermieterin gegen Mieter auf Miete. [k1]Römisch eins: Anspruch entstanden "
     "aus Paragraf fünfhundertfünfunddreißig Absatz zwei. [k2]Römisch zwei: Minderung kraft Gesetzes nach Paragraf "
     "fünfhundertsechsunddreißig. [k2a]Mangel, also nachteilige Abweichung von Ist und Soll, [k2b]nicht unerheblich, "
     "[k2c]keine Kenntnis bei Vertragsschluss, [k2d]keine Sperre wegen unterlassener Anzeige, [k2e]Umfang angemessen, von "
     "der Bruttomiete. [k3]Römisch drei: Ergebnis, geschuldet ist nur die geminderte Miete.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Miete mindert sich von selbst, sobald ein nicht unerheblicher Mangel da ist. [merk2]Zeig ihn aber "
     "sofort an, und zahle im Zweifel unter Vorbehalt, statt einfach weniger zu überweisen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"\b(Friedemanns|Teubers)\b", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
