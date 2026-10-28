"""Folge 195 · Kostenentscheidung ZPO: Kostenquote nach §§ 91, 92 (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall nach dem Plan-Hook („Der Kläger verlangt 10.000 Euro und bekommt 7.300 Euro zugesprochen“), Werklohnklage:
Malermeister Herr Dressler streicht die Fassade am Haus von Frau Lindau und berechnet 10.000 € (7.300 € Fassade, 2.700 €
Garage). Frau Lindau zahlt nichts. Das Amtsgericht verurteilt sie zu 7.300 € und weist die Klage im Übrigen ab (Auftrag für die
Garage nicht bewiesen). Aufbau (Schema): Fall → Sachverhalt → Grundsatz § 91 Abs. 1 S. 1 (Wortlaut, Unterliegensprinzip)
→ Teilunterliegen § 92 Abs. 1 S. 1 (Wortlaut) → Quote auf der Tafel: 2.700 / 10.000 = 27 % (Kläger 27 %, Beklagte 73 %),
Prozent oder Bruch → Kostentenor → Kostenaufhebung (§ 92 Abs. 1 S. 1 Alt. 1, S. 2) → § 92 Abs. 2 Nr. 1 (Wortlaut,
Faustregel 10 % als Literaturangabe gekennzeichnet; hier nicht anwendbar), Nr. 2 in einem Satz → Sonderregeln §§ 93, 91a,
269 Abs. 3 S. 2, 344 (Wortlautkarten kurz) → Klausurtipp (Lexi: Kostentenor nie vergessen, § 308 Abs. 2; vorläufige
Vollstreckbarkeit nur Verweis) → Schema → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Dressler, Lindau (Segment 4 nach
Anweisung des Koordinators umgestellt: „Vor dem Amtsgericht klagt Malermeister Dressler …“ statt „Herr Dressler klagt …“,
weil beide Erkenner dort zweimal „Bressler“ hörten); die Richterin bleibt
namenlos. Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Dressler marc, Frau Lindau sabrina, Richterin laura_ruhig;
william nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Dressler": "marc", "Lindau": "sabrina", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Fassade und Garage -----------------------------------------------------------------------------------------
    ("[fall]Herr Dressler ist Malermeister. [haus]Er streicht die Fassade am Haus von Frau Lindau, [garage]und, wie er "
     "sagt, auch ihre Garage. [rechnung]Seine Rechnung: zehntausend Euro. [zahlt]Frau Lindau zahlt nichts.", P),
    ("[li1]Die Fassade ist fleckig, und die Garage habe ich nie bestellt!", P, "Lindau"),
    ("[dr1]Dann sehen wir uns vor Gericht.", P, "Dressler"),
    # --- B Fall: im Amtsgericht ---------------------------------------------------------------------------------------------
    ("[klage]Vor dem Amtsgericht klagt Malermeister Dressler zehntausend Euro Werklohn ein. [beweis]Nach der Beweisaufnahme steht fest: Die Fassade "
     "ist in Ordnung. [beweis2]Einen Auftrag für die Garage kann er aber nicht beweisen.", P),
    ("[ri1]Die Beklagte wird verurteilt, an den Kläger siebentausenddreihundert Euro zu zahlen. Im Übrigen wird die Klage "
     "abgewiesen.", P, "Richterin"),
    ("[frage]Zehntausend Euro verlangt, siebentausenddreihundert bekommen. [frage2]Wer trägt jetzt die Kosten des "
     "Rechtsstreits?", PS),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Grundsatz: § 91 Abs. 1 S. 1 ------------------------------------------------------------------------------------
    ("[p91]Der Ausgangspunkt steht in Paragraf einundneunzig Absatz eins Satz eins: Die unterliegende Partei hat die Kosten "
     "des Rechtsstreits zu tragen. [unterl]Das ist das Unterliegensprinzip: Wer verliert, zahlt. [umf]Dazu gehören die "
     "Gerichtskosten und die notwendigen Kosten des Gegners, etwa für seinen Anwalt. [hier91]Hier hat aber keiner ganz "
     "verloren.", PS),
    # --- E Teilunterliegen: § 92 Abs. 1 S. 1 -------------------------------------------------------------------------------
    ("[p92]Für diesen Fall gilt Paragraf zweiundneunzig Absatz eins Satz eins: Wenn jede Partei teils obsiegt, teils "
     "unterliegt, so sind die Kosten gegeneinander aufzuheben oder verhältnismäßig zu teilen. [teilen]Der Normalfall ist "
     "das Teilen nach einer Quote.", PS),
    # --- F Quote rechnen ----------------------------------------------------------------------------------------------------
    ("[rech]Also rechnen wir. [r1]Herr Dressler hat zehntausend Euro verlangt [r2]und zweitausendsiebenhundert Euro davon "
     "verloren. [r3]Zweitausendsiebenhundert geteilt durch zehntausend sind siebenundzwanzig Prozent. [r4]So viel von den "
     "Kosten trägt der Kläger.", P),
    ("[dr2]Ich zahle mit, obwohl ich gewonnen habe?", P, "Dressler"),
    ("[r5]Zum Teil, ja. Frau Lindau hat siebentausenddreihundert Euro verloren, also dreiundsiebzig Prozent. [basis]Die "
     "Quote misst also das Unterliegen am Streitwert, hier zehntausend Euro. [bruch]Statt Prozent geht auch ein Bruch. Bei "
     "glatten Anteilen ist das üblich, etwa ein Viertel zu drei Vierteln. [bruch2]Siebenundzwanzig Hundertstel liest sich "
     "dagegen schwer, hier bleibt es bei Prozent.", PS),
    # --- G Kostentenor, Kostenaufhebung -------------------------------------------------------------------------------------
    ("[tenor]Der Kostentenor lautet dann: Von den Kosten des Rechtsstreits tragen der Kläger siebenundzwanzig Prozent und "
     "die Beklagte dreiundsiebzig Prozent. [aufh]Statt zu teilen, kann das Gericht die Kosten auch gegeneinander "
     "aufheben. [aufh2]Dann fallen die Gerichtskosten jeder Partei zur Hälfte zur Last, Absatz eins Satz zwei. Ihre eigenen "
     "Anwaltskosten trägt jede selbst. [aufh3]Das passt vor allem, wenn beide etwa zur Hälfte gewinnen.", PS),
    # --- H Ausnahme: § 92 Abs. 2 --------------------------------------------------------------------------------------------
    ("[p922]Kann Herr Dressler die Kosten trotzdem ganz loswerden? [nr1]Paragraf zweiundneunzig Absatz zwei Nummer eins: "
     "Das Gericht kann der einen Partei die gesamten Prozesskosten auferlegen, wenn die Zuvielforderung der anderen Partei "
     "verhältnismäßig geringfügig war und keine oder nur geringfügig höhere Kosten veranlasst hat. [beide]Beides muss "
     "vorliegen. [faust]Als Faustregel nennt die Literatur: geringfügig bis etwa zehn Prozent. Das ist kein Gesetz, nur eine "
     "Orientierung. [nicht]Siebenundzwanzig Prozent liegen weit darüber. Absatz zwei hilft Herrn Dressler nicht. "
     "[nr2]Nummer zwei greift, wenn die Höhe der Forderung vom richterlichen Ermessen, von Sachverständigen oder von einer "
     "gegenseitigen Berechnung abhing.", PS),
    # --- I Sonderregeln -----------------------------------------------------------------------------------------------------
    ("[sonder]Daneben gibt es Sonderregeln. Merk dir vier. [p93]Paragraf dreiundneunzig: Erkennt der Beklagte den Anspruch "
     "sofort an und hat er keinen Anlass zur Klage gegeben, trägt der Kläger die Kosten. [p91a]Paragraf einundneunzig a: "
     "Erklären die Parteien den Rechtsstreit in der Hauptsache für erledigt, entscheidet das Gericht über die Kosten nach "
     "billigem Ermessen. [p269]Paragraf zweihundertneunundsechzig Absatz drei Satz zwei: Nimmt der Kläger die Klage zurück, "
     "trägt er grundsätzlich die Kosten. [p344]Und Paragraf dreihundertvierundvierzig: Ist ein Versäumnisurteil in "
     "gesetzlicher Weise ergangen, trägt die säumige Partei die Kosten der Säumnis, auch wenn sie nach dem Einspruch "
     "gewinnt. [vu]Mehr dazu im Video zum Versäumnisurteil.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Vergiss den Kostentenor nie. [tipp2]Über die Kosten entscheidet das Gericht auch ohne Antrag, "
     "Paragraf dreihundertacht Absatz zwei. [tipp3]Danach folgt die vorläufige Vollstreckbarkeit nach den Paragrafen "
     "siebenhundertacht folgende, ein eigenes Thema.", PS),
    # --- K Schema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Kostenentscheidung. [k1]Erstens, der Grundsatz: Wer verliert, trägt die Kosten, Paragraf "
     "einundneunzig. [k2]Zweitens, das Teilunterliegen: Quote aus Unterliegen und Streitwert, Paragraf zweiundneunzig "
     "Absatz eins. [k3]Drittens, die Ausnahme nach Absatz zwei. [k4]Viertens, die Sonderregeln. [k5]Fünftens, der "
     "Kostentenor.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Kosten folgen dem Unterliegen. [m2]Wer teils gewinnt und teils verliert, zahlt nach Quote: "
     "verlorener Betrag durch Streitwert.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
