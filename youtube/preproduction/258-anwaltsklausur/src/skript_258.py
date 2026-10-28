"""Folge 258 · Anwaltsklausur Aufbau: Gutachten, Zweckmäßigkeit, Schriftsatz (Fr · 2. Examen · Klausurtechnik, Format Schema).
Beispielfall nach dem Plan-Hook („Die Mandantin will nicht wissen, wer recht hat, sondern was sie jetzt konkret tun soll“):
Frau Steinhoff (um 70) hat einem Gartenbaubetrieb 3.000 € für eine neue Terrasse angezahlt; fertig sein sollte sie Ende
April (per E-Mail vereinbart). Passiert ist nichts, der Betrieb meldet sich nicht. In der Kanzlei: Referendarin Isolde
(Anwaltsstation) und ihr Ausbilder Rechtsanwalt Hohlfeld. Eine Frist hat Frau Steinhoff noch nicht gesetzt.
Aufbau: Fall → Hook/Frage → Sachverhalt → Perspektivwechsel (parteiisch, aber gebunden: § 43a Abs. 3 BRAO mit
Wortlautkarte, § 138 Abs. 1 ZPO; § 43a Abs. 4 S. 1 mit Wortlautkarte, Abs. 5 S. 1) → Aufbau in drei Stufen mit
Mandantenbegehren vorweg (Verweis 222) → Gutachten am Fall (§ 346 Abs. 1, § 323 Abs. 1 BGB mit Wortlautkarte; § 23 Nr. 1
GVG nur als Fundstelle) → Zweckmäßigkeit vs. zweites Gutachten (sicherster, schnellster, kostengünstigster Weg) →
Tafel Zeit/Kosten (§ 91 Abs. 1 ZPO)/Beweisbarkeit/Vergleich/Eilrechtsschutz (§ 917 Abs. 1 ZPO)/sicherster Weg →
Ergebnis in der Kanzlei → praktischer Teil je nach Bearbeitervermerk → Kurzblick Zivil (§ 253 Abs. 2 ZPO), Öffentliches
Recht (§ 81 Abs. 1 S. 1 VwGO), Strafrecht (§ 137 Abs. 1 S. 1 StPO; Verweis 039) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung
„258: Isolde, Steinhoff, Hohlfeld“): Isolde, Frau Steinhoff, Herr Hohlfeld; nie im Genitiv.
Stimmen (Pool stephan, hilde, christian, lucy): Isolde lucy (Frau, jung), Frau Steinhoff hilde (Frau, älter), Herr Hohlfeld
stephan (Mann, mittel); christian nicht verwendet (also nie stephan und christian in einer Szene). Lexi = Erzählerin Carla.
„BRAO“ und „GVG“ stehen nicht in der Abkürzungsliste von synth_el.py; gesprochen wird deshalb „Bundesrechtsanwaltsordnung“,
die GVG-Norm nur auf der Tafel.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Isolde": "lucy", "Steinhoff": "hilde", "Hohlfeld": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Besprechungszimmer der Kanzlei --------------------------------------------------------------------------
    ("[fall]In einer Anwaltskanzlei. [steinhoff]Frau Steinhoff legt einen Kontoauszug auf den Tisch. "
     "[isolde]Mit ihr sprechen Referendarin Isolde [hohlfeld]und ihr Ausbilder, Rechtsanwalt Hohlfeld.", P),
    ("[st1]Ich habe dem Gartenbaubetrieb dreitausend Euro angezahlt. Ende April sollte meine Terrasse fertig sein. "
     "[st1b]Passiert ist nichts.", P, "Steinhoff"),
    ("[st2]Ich will mein Geld zurück. Was soll ich jetzt tun?", P, "Steinhoff"),
    # Nachvertonung 08.10.2026: Erstfassung „Isolde, Sie schreiben …“ – der Name am Satzanfang wurde von whisper small und
    # medium übereinstimmend als „die/wie sollte“ erkannt (im Satz und isoliert); Name deshalb ans Satzende gestellt.
    ("[ho1]Sie schreiben das Gutachten, Isolde. Und am Ende steht ein Vorschlag, was wir tun.", PS, "Hohlfeld"),
    ("[hook]Die Mandantin will nicht wissen, wer recht hat, sondern was sie jetzt konkret tun soll. [hook2]Genau das "
     "verlangt die Anwaltsklausur. [frage]Wie baust du sie auf, [frage2]und was unterscheidet echte Zweckmäßigkeit von "
     "einem zweiten Gutachten?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Perspektivwechsel: parteiisch, aber gebunden ------------------------------------------------------------------
    ("[pers]Zuerst ein Perspektivwechsel. [richter]Als Richter fragst du: Wer hat recht? [anwalt]Als Anwalt fragst du: "
     "Was nützt meiner Mandantin? [partei]Du bist parteiisch, [grenze]aber nicht grenzenlos.", P),
    ("[st3]Schreiben Sie ruhig, der Betrieb ist ein Betrüger.", P, "Steinhoff"),
    ("[is1]Wir bleiben sachlich. Und wir schreiben nur, was stimmt.", P, "Isolde"),
    ("[w43]So verlangt es Paragraf dreiundvierzig a Absatz drei der Bundesrechtsanwaltsordnung. [sach]Der Anwalt darf sich "
     "nicht unsachlich verhalten, [unw]vor allem keine Unwahrheiten bewusst verbreiten [herab]und niemanden ohne Anlass "
     "herabsetzen.", P),
    ("[abs4]Und Absatz vier: Wer in derselben Rechtssache schon einen anderen Mandanten im widerstreitenden Interesse "
     "beraten oder vertreten hat, darf nicht tätig werden. [abs5]Nach Absatz fünf gilt das auch für Referendare "
     "in der Anwaltsstation.", PS),
    # --- D Aufbau: drei Stufen, Mandantenbegehren vorweg -----------------------------------------------------------------
    ("[auf]Jetzt der Aufbau: in der Regel drei Stufen, und davor eine Frage. [begehr]Vorweg das Mandantenbegehren: Was "
     "will die Mandantin erreichen? [begehr2]Frau Steinhoff will ihr Geld zurück, keine Terrasse mehr von diesem "
     "Betrieb. [stufe1]Erstens das Gutachten: die materielle und die prozessuale Lage. [stufe2]Zweitens die "
     "Zweckmäßigkeit: Welcher Weg führt am besten zum Ziel? [stufe3]Drittens der praktische Teil, also das, was du "
     "tatsächlich entwirfst. [bv]Wie die Teile heißen und was entfällt, sagt der Bearbeitervermerk. [f222]Wie du ihn "
     "liest, zeigt Folge zweihundertzweiundzwanzig.", PS),
    # --- E Erstens: das Gutachten am Fall --------------------------------------------------------------------------------
    ("[gut]Das Gutachten bei Frau Steinhoff. [mat]Materiell kann sie die dreitausend Euro nach einem Rücktritt "
     "zurückverlangen, Paragraf dreihundertsechsundvierzig BGB. [w323]Zurücktreten kann sie nach Paragraf "
     "dreihundertdreiundzwanzig, wenn der Betrieb eine fällige Leistung nicht erbringt [fr]und sie ihm erfolglos eine "
     "angemessene Frist gesetzt hat. [noch]Eine Frist hat Frau Steinhoff noch nicht gesetzt. [proz]Prozessual wäre für "
     "eine Klage über dreitausend Euro das Amtsgericht zuständig.", P),
    ("[vorb]Das Gutachten endet also nicht mit: Anspruch besteht oder besteht nicht. Es bereitet die Maßnahme vor.", PS),
    # --- F Zweitens: Zweckmäßigkeit statt zweitem Gutachten --------------------------------------------------------------
    ("[zw]Zweitens die Zweckmäßigkeit. Hier lauert eine Falle: [zw2]das zweite Gutachten. Du prüfst noch einmal, ob der "
     "Anspruch besteht. [echt]Echte Zweckmäßigkeit fragt etwas anderes: Welcher Weg bringt Frau Steinhoff ihr Geld am "
     "sichersten, schnellsten und kostengünstigsten zurück? [vor]Widerspricht sich das, geht Sicherheit vor.", P),
    # --- G Die Zweckmäßigkeit am Fall ------------------------------------------------------------------------------------
    ("[t1]Zeit: Eine Klage sofort wäre am schnellsten. [t2]Kosten: Aber ohne Frist droht die Abweisung, und dann trägt "
     "Frau Steinhoff die Kosten, Paragraf einundneunzig ZPO. [t3]Beweisbarkeit: Die Zahlung belegt der Kontoauszug, den "
     "Termin Ende April eine E-Mail. [t4]Vergleich: Vielleicht zahlt der Betrieb schon auf ein klares Schreiben, notfalls "
     "in Raten. [t5]Eilrechtsschutz: Ein Arrest setzt voraus, dass sonst die Vollstreckung vereitelt oder wesentlich "
     "erschwert würde, Paragraf neunhundertsiebzehn ZPO. Dafür spricht hier nichts. [t6]Also der sicherste Weg: erst "
     "schriftlich und nachweisbar eine angemessene Frist setzen, dann zurücktreten, notfalls klagen.", P),
    ("[t7]Jeder Punkt hat einen Fallbezug und endet in einer Entscheidung. Das ist der Unterschied zum zweiten Gutachten.", PS),
    # --- H Ergebnis in der Kanzlei ---------------------------------------------------------------------------------------
    ("[is2]Wir setzen dem Betrieb jetzt schriftlich eine Frist. Verstreicht sie, treten wir vom Vertrag zurück und "
     "verlangen die dreitausend Euro.",
     P, "Isolde"),
    ("[st4]Endlich ein Plan.", P, "Steinhoff"),
    ("[ho2]Genau so. Das ist Zweckmäßigkeit.", PS, "Hohlfeld"),
    # --- I Drittens: der praktische Teil ---------------------------------------------------------------------------------
    ("[prak]Drittens der praktische Teil. [je]Was du entwirfst, steht im Bearbeitervermerk: [p1]ein Schriftsatz an das "
     "Gericht, [p2]ein Schreiben an die Mandantin [p3]oder ein Vertragsentwurf. [pf]Bei Frau Steinhoff sind es zwei "
     "Schreiben: [pf1]die Fristsetzung an den Betrieb [pf2]und ein Brief an sie in verständlicher Sprache. "
     "[pf3]Er sagt ihr auch, dass der Betrieb innerhalb der Frist noch bauen kann.", PS),
    # --- J Kurzblick: Zivilrecht, Öffentliches Recht, Strafrecht ---------------------------------------------------------
    ("[drei]Dieser Aufbau trägt in allen drei Rechtsgebieten. Anders ist vor allem der praktische Teil. [zr]Im Zivilrecht "
     "kann es eine Klageschrift sein. Sie bezeichnet Parteien und Gericht, Gegenstand und Grund des Anspruchs und "
     "enthält einen bestimmten Antrag, Paragraf zweihundertdreiundfünfzig Absatz zwei ZPO.", P),
    ("[oer]Im Öffentlichen Recht geht es etwa um Widerspruch, Klage oder Eilantrag gegen "
     "einen Bescheid. Die Klage ist schriftlich bei Gericht zu erheben, Paragraf einundachtzig VwGO.", P),
    ("[sr]Im Strafrecht bist du Verteidiger. Der Beschuldigte kann sich in jeder Lage des Verfahrens des Beistandes eines "
     "Verteidigers bedienen, Paragraf hundertsiebenunddreißig StPO. [rev]Auch in der Revisionsklausur "
     "kann auf das Gutachten die Zweckmäßigkeit folgen. [f39]Die Sicht der Staatsanwaltschaft zeigt Folge neununddreißig.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Plane genug Zeit für den praktischen Teil ein. Fehlt er, fehlt ein großer Teil der Leistung. "
     "[tipp2]Und der Schriftsatz darf dem Gutachten nicht widersprechen: dieselben Gründe, dieselben Beweise.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Anwaltsklausur. [k0]Vorweg: das Mandantenbegehren. [k1]Römisch eins: das Gutachten, "
     "[k1a]materielle und prozessuale Lage. [k2]Römisch zwei: die Zweckmäßigkeit, [k2a]sicher, schnell und "
     "kostengünstig, am Fall begründet. [k3]Römisch drei: der praktische Teil, [k3a]je nach Bearbeitervermerk "
     "Schriftsatz, Mandantenschreiben oder Vertragsentwurf.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Gutachten sagt, was rechtlich geht. [m2]Die Zweckmäßigkeit sagt, was die Mandantin jetzt tun "
     "soll.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
