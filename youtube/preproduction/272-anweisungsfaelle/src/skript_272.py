"""Folge 272 · Anweisungsfälle im Bereicherungsrecht: Wer muss zurückzahlen? (Mi · Examenswissen · Bereicherungsrecht ·
Streitstand; § 812 Abs. 1 Satz 1 Alt. 1 BGB). Beispielfall nach dem Plan-Hook („Du lässt deine Bank die Handwerkerrechnung
zahlen – später stellt sich der Werkvertrag als nichtig heraus“): Tomke lässt ihre Bank die Anzahlung von 3.500 € an den
Fliesenleger Herrn Stemmler überweisen; Herr Stemmler hatte behauptet, sein Betrieb sei voll versichert; Tomke ficht den Werkvertrag wegen
arglistiger Täuschung an (§ 123 Abs. 1, § 142 Abs. 1 BGB). Gearbeitet hat Herr Stemmler noch nicht (keine Gegenkondiktion).
Die Bank ist namenlos (keine echte Bankmarke); Bankberater Herr Feldhaus.
Kernaussagen (Volltext, Rn.): BGH XI ZR 243/13 Rn. 17 f., 19 f., 22–24 (Grundsatz, fehlende Anweisung, Widerruf, § 675u);
XI ZR 158/24 Rn. 10 f.; IX ZR 52/13 Rn. 16 (Leistung der Bank an den Kontoinhaber, keine Leistungsbeziehung Bank–Empfänger);
IX ZR 226/08 Rn. 15 (Fehler im Valutaverhältnis dort abwickeln); XI ZR 343/22 Rn. 15 f., 20 (Aufwendungsersatz, keine
Einwendungen aus dem Valutaverhältnis); IX ZR 212/19 Rn. 21 (Vorrang); VIII ZR 39/17 Rn. 17 f., 34; V ZR 269/13 Rn. 22 f.
(Risikoverteilung, Insolvenzrisiko). Belege je Cue in ../RECHTSSTAND.md.
Stimmen (Pool stephan, hilde, christian, lucy): Tomke (lucy, Frau, jung), Herr Stemmler (stephan, Mann, mittel),
Herr Feldhaus (christian, Mann, mittel) – Stemmler und Feldhaus nie in derselben Szene im Gespräch; hilde nicht besetzt.
Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Tomke": "lucy", "Stemmler": "stephan", "Feldhaus": "christian"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: das alte Bad, der Fliesenleger und die Anzahlung -------------------------------------------------------
    ("[fall]Tomke will ihr altes Bad erneuern lassen. [stemmler]Der Fliesenleger Herr Stemmler [rechnung]schickt ihr eine "
     "Rechnung über die vereinbarte Anzahlung: dreitausendfünfhundert Euro.", P),
    ("[st1]Keine Sorge, mein Betrieb ist voll versichert. Sobald die Anzahlung da ist, fange ich an.", P, "Stemmler"),
    # --- A2 Überweisung --------------------------------------------------------------------------------------------------
    ("[ueberw]Tomke beauftragt ihre Bank, das Geld zu überweisen. [gutschr]Am nächsten Tag ist der Betrag auf dem Konto von "
     "Herrn Stemmler.", P),
    # --- A3 Eine Woche später: kein Meister, Anfechtung ------------------------------------------------------------------
    ("[woche]Eine Woche später erfährt Tomke: Versichert ist der Betrieb gar nicht. [anf]Sie ficht den Werkvertrag wegen "
     "arglistiger Täuschung an. [bank]Dann geht sie zu ihrer Bank.", P),
    # --- A4 Bei der Bank -------------------------------------------------------------------------------------------------
    ("[t1]Holen Sie meine dreitausendfünfhundert Euro bitte direkt bei Herrn Stemmler zurück!", P, "Tomke"),
    ("[f1]Das geht nicht. Wir haben Ihren Auftrag richtig ausgeführt. An Herrn Stemmler müssen Sie sich selbst halten.", P,
     "Feldhaus"),
    ("[frage]Hat der Bankberater recht? Wer muss hier an wen zurückzahlen? [frage2]Und warum kann die Bank nicht einfach "
     "direkt bei Herrn Stemmler kondizieren?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Anweisungsdreieck (XI ZR 243/13 Rn. 17; XI ZR 343/22 Rn. 14) ------------------------------------------------
    ("[dreieck]Das ist ein Anweisungsfall mit drei Beteiligten. [anw]Tomke ist die Anweisende, [angew]ihre Bank die "
     "Angewiesene [empf]und Herr Stemmler der Empfänger. [deck]Zwischen Tomke und ihrer Bank besteht das Deckungsverhältnis, "
     "hier der Zahlungsdiensterahmenvertrag über ihr Girokonto. [valuta]Zwischen Tomke und Herrn Stemmler besteht das "
     "Valutaverhältnis, hier der Werkvertrag. [zuw]Das Geld aber fließt von der Bank zu Herrn Stemmler.", P),
    # --- D Leistungsbegriff aus Empfängersicht (VIII ZR 39/17 Rn. 17; XI ZR 243/13 Rn. 17; IX ZR 52/13 Rn. 16) ---------------
    ("[leist]Wer hat an wen geleistet? Leistung ist die bewusste und zweckgerichtete Mehrung fremden Vermögens; "
     "[sicht]gehen die Vorstellungen auseinander, entscheidet die Sicht des Empfängers. [zwei]Nach dem Bundesgerichtshof "
     "bewirkt die eine Zahlung zwei Leistungen: [lbank]Die Bank leistet an Tomke, denn sie erfüllt deren Zahlungsauftrag. "
     "[ltomke]Und Tomke leistet an Herrn Stemmler, denn sie will die vereinbarte Anzahlung zahlen. [keine]Zwischen der Bank "
     "und Herrn Stemmler gibt es dagegen keine Leistungsbeziehung.", P),
    ("[eck]Deshalb wird über Eck rückabgewickelt: jeweils in dem Verhältnis, das fehlerhaft ist.", PS),
    # --- E Der Fall: Valutaverhältnis nichtig (XI ZR 343/22 Rn. 15 f.; IX ZR 226/08 Rn. 15) ---------------------------------
    ("[fehler]Welches Verhältnis ist hier fehlerhaft? [dok]Das Deckungsverhältnis ist in Ordnung: Tomke hat die Überweisung "
     "autorisiert, [aufw]also darf die Bank ihr Konto belasten und ihre Aufwendungen ersetzt verlangen. [vfehl]Fehlerhaft ist "
     "das Valutaverhältnis: Nach der Anfechtung ist der Werkvertrag gemäß Paragraf hundertzweiundvierzig Absatz eins als von "
     "Anfang an nichtig anzusehen.", P),
    # --- F Anspruch Tomke gegen Stemmler (Wortlautkarte § 812 Abs. 1 Satz 1; IX ZR 164/14 Rn. 8) ----------------------------
    ("[w812]Also prüfst du den Anspruch von Tomke gegen Herrn Stemmler aus Paragraf achthundertzwölf Absatz eins Satz eins, "
     "erste Alternative: Wer durch die Leistung eines anderen etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe "
     "verpflichtet. [erl]Erlangt hat Herr Stemmler die Gutschrift, also einen Anspruch gegen seine Bank, [durch]und zwar "
     "durch Leistung von Tomke, [org]ohne rechtlichen Grund, weil der Werkvertrag nichtig ist. [erg1]Tomke kann die "
     "dreitausendfünfhundert Euro also von Herrn Stemmler zurückverlangen.", P),
    # --- G Keine Durchgriffskondiktion (IX ZR 52/13 Rn. 16; IX ZR 212/19 Rn. 21; XI ZR 343/22 Rn. 20; V ZR 269/13 Rn. 22 f.) ---
    ("[durchg]Und die Bank? Auf den ersten Blick liegt ein Durchgriff nahe, denn das Geld kam ja von ihr. [nein]Eine solche "
     "Durchgriffskondiktion gibt es aber grundsätzlich nicht. [nleist]Die Bank hat nicht an Herrn Stemmler geleistet, sondern "
     "an Tomke, [vorrang]und eine Nichtleistungskondiktion scheitert an der Subsidiarität, also am Vorrang der Leistungskondiktion.", P),
    ("[gruende]Dahinter steht eine Risikoverteilung. [einw]Jeder behält seine Einwendungen gegenüber dem eigenen "
     "Vertragspartner. [insolv]Und jeder trägt nur das Insolvenzrisiko des Partners, den er sich selbst ausgesucht hat. "
     "[pleite]Ist Herr Stemmler pleite, trifft das Tomke, die ihn beauftragt hat, und nicht die Bank.", PS),
    # --- H Ausnahmen (XI ZR 243/13 Rn. 18–24; XI ZR 158/24 Rn. 11; VIII ZR 39/17 Rn. 34; § 675u BGB) ------------------------
    ("[ausn]Anders liegt es, wenn schon die Anweisung fehlerhaft ist. [fehlt]Fehlt eine wirksame Anweisung, etwa bei einem "
     "gefälschten Überweisungsauftrag, kondiziert die Bank direkt beim Empfänger, nach Satz eins, zweite Alternative, auch "
     "wenn der Empfänger davon nichts wusste. [widerr]Hat der Kunde seine Anweisung widerrufen und die Bank trotzdem gezahlt, "
     "musste sie sich nach der früheren Rechtsprechung an ihren Kunden halten, [kennt]es sei denn, der Empfänger kannte den "
     "Widerruf. [w675u]Für Zahlungsdienste gilt heute Paragraf sechshundertfünfundsiebzig u: Fehlt die Autorisierung, etwa "
     "nach einem Widerruf, hat die Bank gegen den Zahler keinen Anspruch auf Erstattung ihrer Aufwendungen, und deshalb "
     "kondiziert sie nach dem Bundesgerichtshof direkt beim Empfänger, auch wenn dieser nichts wusste.", PS),
    # --- I Ergebnis (zurück bei der Bank) --------------------------------------------------------------------------------
    ("[erg]Ergebnis: Der Bankberater hat recht. Die Anweisung war wirksam, die Bank bleibt außen vor. [erg2]Tomke muss sich "
     "an Herrn Stemmler halten und kann von ihm dreitausendfünfhundert Euro zurückverlangen.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Zeichne bei drei Beteiligten zuerst das Dreieck und trage Deckungs- und Valutaverhältnis ein. "
     "[tipp2]Dann fragst du: Gibt es eine wirksame Anweisung? Wenn ja, wird im fehlerhaften Verhältnis rückabgewickelt. "
     "Wenn nein, prüfst du die Direktkondiktion gegen den Empfänger.", PS),
    # --- K Prüfungsschema ----------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema für Anweisungsfälle. [s1]Eins: Beteiligte und Verhältnisse bestimmen, also Deckung und "
     "Valuta. [s2]Zwei: Leistungen aus der Sicht des Empfängers zuordnen. [s3]Drei: Liegt eine wirksame, autorisierte "
     "Anweisung vor? [s4]Vier: Wenn ja, Leistungskondiktion im fehlerhaften Verhältnis, kein Durchgriff. [s5]Fünf: Wenn "
     "nein, Nichtleistungskondiktion der Bank gegen den Empfänger.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei wirksamer Anweisung wird über Eck rückabgewickelt, jeder mit seinem eigenen Vertragspartner. "
     "[merk2]Fehlt eine wirksame Anweisung, holt sich die Bank das Geld in aller Regel direkt beim Empfänger.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
