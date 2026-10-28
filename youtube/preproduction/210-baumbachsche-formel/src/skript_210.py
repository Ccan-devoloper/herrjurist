"""Folge 210 · Baumbachsche Kostenformel: Schritt für Schritt mit Tabelle (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall nach dem Plan-Hook („Zwei Beklagte werden als Gesamtschuldner auf 20.000 Euro verklagt, der eine verliert voll,
der andere gewinnt komplett“): Herr Lohmann und Frau Kreutzer führen zusammen einen Fahrradladen. Frau Eschenbach leiht
ihnen nach ihrer Darstellung 20.000 €; den Darlehensvertrag unterschreibt nur Herr Lohmann, das Geld geht auf sein Konto.
Klage vor dem Landgericht gegen beide als Gesamtschuldner auf 20.000 €. Urteil: Herr Lohmann (Beklagter zu 1) verliert voll,
die Klage gegen Frau Kreutzer (Beklagte zu 2) wird abgewiesen (Mitverpflichtung nicht bewiesen).
Aufbau (Schema, Perspektive 2. Examen/Tenor): Fall → Sachverhalt → Problem: §§ 91, 92 denken in zwei Parteien;
Streitgenossen §§ 59, 61 (zwei Prozessrechtsverhältnisse) → § 100 Abs. 1 (Wortlaut, Kopfteile) und Abs. 4 (Gesamtschuldner),
beides passt nicht → Grundgedanke der Formel: Gerichtskosten und außergerichtliche Kosten getrennt, fiktiver Streitwert
2 × 20.000 € = 40.000 € → Tabelle a) Gerichtskosten ½ / ½, b) außergerichtliche Kosten der Klägerin: B1 ½, Rest Klägerin,
c) außergerichtliche Kosten B1: trägt er selbst, d) außergerichtliche Kosten B2: trägt die Klägerin → Probe →
Kostentenor wortgenau → Klausurtipp (Lexi: Tabelle zuerst auf dem Konzeptpapier) → Schema → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben und reserviert (namen_reserviert.txt): Eschenbach, Lohmann, Kreutzer;
der Richter bleibt namenlos. Stimmen (Pool stephan, hilde, christian, lucy): Frau Eschenbach hilde, Herr Lohmann stephan,
Frau Kreutzer lucy, Richter christian (spricht nur in Szene B, in der Herr Lohmann schweigt: stephan und christian nie
Dialogpartner in derselben Szene). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Eschenbach": "hilde", "Lohmann": "stephan", "Kreutzer": "lucy", "Richter": "christian"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: im Fahrradladen ------------------------------------------------------------------------------------------
    ("[fall]Herr Lohmann und Frau Kreutzer führen zusammen einen Fahrradladen. [leiht]Frau Eschenbach leiht ihnen, wie sie "
     "sagt, zwanzigtausend Euro. [vertrag]Den Darlehensvertrag unterschreibt aber nur Herr Lohmann, das Geld geht auf sein "
     "Konto. [faellig]Dann wird das Darlehen fällig, und es fließt kein Cent.", P),
    ("[es1]Sie haben sich das Geld beide geliehen, also zahlen Sie auch beide!", P, "Eschenbach"),
    ("[kr1]Ich habe nichts unterschrieben. Das Darlehen hat er allein aufgenommen.", P, "Kreutzer"),
    # --- B Fall: im Landgericht -------------------------------------------------------------------------------------------
    ("[klage]Frau Eschenbach verklagt beide vor dem Landgericht als Gesamtschuldner auf zwanzigtausend Euro. [beweis]Dass "
     "sich auch Frau Kreutzer verpflichtet hat, kann sie nicht beweisen.", P),
    ("[ri1]Der Beklagte zu eins wird verurteilt, an die Klägerin zwanzigtausend Euro zu zahlen. Im Übrigen wird die Klage "
     "abgewiesen.", P, "Richter"),
    ("[frage]Herr Lohmann verliert also voll, Frau Kreutzer gewinnt komplett. [frage2]Wer trägt jetzt welche Kosten?", PS),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Problem: zwei Prozessrechtsverhältnisse ------------------------------------------------------------------------
    ("[problem]Die Paragrafen einundneunzig und zweiundneunzig denken in zwei Parteien: Wer verliert, zahlt, und wer teils "
     "verliert, zahlt nach Quote. [drei]Hier stehen aber drei Parteien vor Gericht. [p59]Die Beklagten sind Streitgenossen, "
     "Paragraf neunundfünfzig. [p61]Nach Paragraf einundsechzig steht jeder dem Gegner als Einzelner gegenüber. [zwei]Es "
     "gibt also zwei Prozessrechtsverhältnisse: Eschenbach gegen Lohmann und Eschenbach gegen Kreutzer.", PS),
    # --- E § 100 ZPO ------------------------------------------------------------------------------------------------------
    ("[p100]Hilft Paragraf hundert? Absatz eins: Besteht der unterliegende Teil aus mehreren Personen, so haften sie für die "
     "Kostenerstattung nach Kopfteilen. [p1004]Und nach Absatz vier haften Beklagte, die als Gesamtschuldner verurteilt "
     "werden, auch für die Kostenerstattung als Gesamtschuldner. [passt]Beides setzt voraus, dass mehrere verlieren. Hier verliert "
     "aber nur Herr Lohmann. [luecke]Für Streitgenossen mit unterschiedlichem Erfolg arbeitet die Praxis deshalb mit einer "
     "Rechenmethode: der Baumbachschen Formel.", PS),
    # --- F Grundgedanke, fiktiver Streitwert ------------------------------------------------------------------------------
    ("[idee]Ihr Grundgedanke: Gerichtskosten und außergerichtliche Kosten werden getrennt verteilt. [idee2]Jede Partei trägt "
     "Kosten nur aus den Prozessrechtsverhältnissen, an denen sie beteiligt ist, und nur soweit sie dort verliert. "
     "[fiktiv]Dafür bildet man einen fiktiven Streitwert: die Summe aller Prozessrechtsverhältnisse. [summe]Zwanzigtausend "
     "gegen Lohmann plus zwanzigtausend gegen Kreutzer, macht vierzigtausend Euro. [echt]Der echte Streitwert bleibt wegen "
     "der Gesamtschuld bei zwanzigtausend. Die vierzigtausend sind nur eine Rechengröße.", PS),
    # --- G Tabelle a) Gerichtskosten --------------------------------------------------------------------------------------
    ("[tab]Jetzt die Tabelle, Schritt für Schritt. [ga]Erstens, die Gerichtskosten. Das Gericht ist an beiden "
     "Prozessrechtsverhältnissen beteiligt, also an vierzigtausend Euro. [ga2]Die Klägerin verliert zwanzigtausend gegen "
     "Frau Kreutzer. Zwanzig von vierzig ist die Hälfte. [ga3]Herr Lohmann verliert zwanzigtausend, auch die Hälfte.", P),
    # --- G Tabelle b) außergerichtliche Kosten der Klägerin ---------------------------------------------------------------
    ("[kb]Zweitens, die außergerichtlichen Kosten der Klägerin, vor allem ihr Anwalt. Auch sie ist an beiden Verhältnissen "
     "beteiligt, also wieder vierzigtausend. [kb2]Herr Lohmann trägt die Hälfte, weil er zwanzigtausend verliert. [kb3]Den "
     "Rest trägt die Klägerin selbst. Frau Kreutzer zahlt nichts, sie hat ja gewonnen.", P),
    # --- G Tabelle c) und d) ----------------------------------------------------------------------------------------------
    ("[kc]Drittens, die außergerichtlichen Kosten von Herrn Lohmann. Er ist nur am Verhältnis zur Klägerin beteiligt, also "
     "zwanzigtausend. [kc2]Dort verliert er voll. Seine Kosten trägt er selbst. [kd]Viertens, die außergerichtlichen Kosten "
     "von Frau Kreutzer. Auch hier zählen nur zwanzigtausend. [kd2]Die Klägerin verliert dort voll, also trägt sie diese "
     "Kosten ganz.", P),
    ("[es2]Obwohl ich gegen Herrn Lohmann gewonnen habe?", P, "Eschenbach"),
    ("[jede]Ja. Gegen Frau Kreutzer hat sie verloren, und dieses Verhältnis wird für sich abgerechnet. [probe]Jetzt die Probe: "
     "In jeder Zeile müssen die Anteile zusammen genau ein Ganzes ergeben. [probe2]Hälfte plus Hälfte, ganz, ganz. Das "
     "stimmt.", PS),
    # --- H Kostentenor ----------------------------------------------------------------------------------------------------
    ("[tenor]Der Kostentenor lautet dann: Die Gerichtskosten tragen die Klägerin und der Beklagte zu eins je zur Hälfte. "
     "[tenor2]Die außergerichtlichen Kosten der Klägerin trägt der Beklagte zu eins zur Hälfte. [tenor3]Die Klägerin trägt "
     "die außergerichtlichen Kosten der Beklagten zu zwei. [tenor4]Im Übrigen tragen die Parteien ihre außergerichtlichen "
     "Kosten selbst. [rest]Dieser Schlusssatz deckt den Rest: die eigene Hälfte der Klägerin und die Kosten von Herrn "
     "Lohmann.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Leg die Tabelle zuerst auf dem Konzeptpapier an. [tipp2]Eine Zeile für jede Kostenmasse, eine "
     "Spalte für jede Partei. [tipp3]Mach in jeder Zeile die Probe. Erst dann schreibst du den Tenor ins Urteil, mit dem "
     "Schlusssatz für die eigenen Kosten.", PS),
    # --- J Schema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Baumbachsche Formel. [k1]Erstens: die Prozessrechtsverhältnisse auflisten. [k2]Zweitens: den "
     "fiktiven Streitwert bilden, die Summe aller Verhältnisse. [k3]Drittens: die Gerichtskosten nach dem Unterliegen am "
     "fiktiven Streitwert. [k4]Viertens: die außergerichtlichen Kosten für jede Partei gesondert, nur aus ihren eigenen "
     "Verhältnissen. [k5]Fünftens: Probe und Tenor.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei Streitgenossen rechnest du jedes Prozessrechtsverhältnis für sich. [m2]Gerichtskosten am fiktiven "
     "Gesamtstreitwert, außergerichtliche Kosten für jede Partei getrennt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
