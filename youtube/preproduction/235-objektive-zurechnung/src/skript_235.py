"""Folge 235 · Objektive Zurechnung: Der Neffe, das Gewitter und der Blitz (Mo · Der Fall · StGB AT · Klassiker-Fall).
Lehrbuchfall (Gewitterfall, schon 1865 bei Böhlau), keine BGH-Entscheidung zum Fall. Fiktiver Fall nach dem Plan-Hook:
Schwüler Sommernachmittag am Waldrand. Hildegard (wohlhabende Witwe, Mitte 70) trinkt Kaffee auf ihrer Terrasse; ihr Neffe
Rupert (um 40, einziger Erbe) ist zu Besuch. Auf seinem Handy erscheint eine Unwetterwarnung. Er rät ihr zu einem Spaziergang
im Wald und hofft insgeheim, dass ein Blitz sie trifft. Genau das passiert.
Prüfung: § 212 Abs. 1 (Wortlautkarte), Mord (§ 211, Habgier) nur ein Satz; Erfolg, Kausalität (csqn, Verweis 026; BGH 3 StR 394/20
Rn. 5: Mitwirkung des Opfers/anderer Ereignisse unschädlich); Problem; objektive Zurechnung als Lehre (rechtlich missbilligte
Gefahr + Realisierung; LMU, Freiburg); Subsumtion: allgemeines Lebensrisiko, nicht beherrschbar → nicht zurechenbar;
Rechtsprechung filtert über den Vorsatz (BGH 3 StR 394/20 Rn. 8; Freiburg KK 201), Wunsch ≠ Vorsatz (Böhlau nach Schroeder);
Abwandlung (Täter wartet im Wald → Gefahrschaffung durch Sonderwissen); § 222 (Wortlautkarte, BGH 4 StR 19/20 Rn. 21);
Fallgruppen (Schutzzweck, Selbstgefährdung – Verweis 058/203, atypischer Kausalverlauf, rechtmäßiges Alternativverhalten);
Klausurtipp, Schema und Merksatz mit Lexi. Belege je Cue: ../RECHTSSTAND.md.
DARSTELLUNG: Tod nur angedeutet (Blitz-Symbol, Unwetterwarnung, keine Leiche, keine Verletzung); Hildegard sympathisch,
Rupert nicht als Karikatur.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Rupert marc (Mann, mittel), Hildegard laura_ruhig (Frau, ruhig).
Erzählerin und Lexi: Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Rupert": "marc", "Hildegard": "laura_ruhig"}

SEGMENTE = [
    # --- A Fall: Terrasse am Waldrand, Gewitter ----------------------------------------------------------------------------
    ("[fall]Ein schwüler Sommernachmittag am Waldrand. [hildegard]Hildegard, eine wohlhabende Witwe Mitte siebzig, trinkt "
     "Kaffee auf ihrer Terrasse. [rupert]Ihr Neffe Rupert ist zu Besuch. Er ist ihr einziger Erbe. [warn]Auf seinem Handy "
     "erscheint eine Unwetterwarnung: Ein Gewitter zieht auf.", 0.2),
    ("[ru1]Tante Hildegard, geh doch noch ein Stück in den Wald. Die Luft ist so schön!", P, "Rupert"),
    ("[hi1]Gute Idee. Bis später, Rupert!", P, "Hildegard"),
    ("[hofft]Rupert hofft insgeheim, dass ein Blitz sie trifft. [wald]Hildegard spaziert in den Wald. [gewitter]Dann bricht "
     "das Gewitter los. [blitz]Ein Blitz schlägt ein und trifft Hildegard tödlich.", 0.4),
    ("[frage]Rupert hat sich ihren Tod gewünscht, und ohne seinen Rat wäre sie nicht im Wald gewesen. Hat er sie getötet? "
     "[frage2]Oder reicht es nicht, den Tod verursacht zu haben?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 212 Abs. 1 (Wortlautkarte), Mord kurz ----------------------------------------------------------------------------
    ("[p212]Paragraf zweihundertzwölf, Absatz eins: Wer einen Menschen tötet, ohne Mörder zu sein, wird als Totschläger "
     "bestraft. [mord]Weil Rupert erben will, käme sogar Mord aus Habgier in Betracht. [mord2]Doch auch der Mord setzt "
     "voraus, dass er einen Menschen tötet.", P),
    # --- D Erfolg und Kausalität -------------------------------------------------------------------------------------------
    ("[erfolg]Der Erfolg ist eingetreten: Hildegard ist tot. [kaus]Für die Kausalität gilt die Formel aus Folge "
     "sechsundzwanzig: Denk den Rat weg, dann geht Hildegard nicht in den Wald, und der Blitz trifft sie nicht. Kausal. "
     "[opfer]Dass sie selbst losgeht und die Natur den Rest besorgt, ändert daran nichts. Nach dem Bundesgerichtshof bleibt "
     "eine Bedingung ursächlich, auch wenn das Opfer oder andere Ereignisse mitwirken.", P),
    # --- E Problem: Reicht Kausalität? Objektive Zurechnung (Lehre) ---------------------------------------------------------
    ("[reicht]Reicht das schon? Nach der Formel wäre schon der bloße Rat zum Spaziergang eine Tötung. "
     "[lehre]Die Lehre begrenzt die weite Formel deshalb mit der objektiven Zurechnung. [def]Zurechenbar ist ein Erfolg nur, "
     "wenn der Täter eine rechtlich missbilligte Gefahr geschaffen hat [real]und sich gerade diese Gefahr im Erfolg "
     "verwirklicht hat. [werk]Kurz gefragt: Ist der Tod das Werk von Rupert oder ein Zufall?", P),
    # --- F Gewitterfall: allgemeines Lebensrisiko, nicht beherrschbar ------------------------------------------------------
    ("[gef]Hat Rupert also eine rechtlich missbilligte Gefahr geschaffen? [leben]Ein Spaziergang im Wald, auch bei "
     "Gewitter, gehört zum allgemeinen Lebensrisiko. Vom Blitz getroffen zu werden, ist so unwahrscheinlich, dass die "
     "Rechtsordnung einen solchen Rat nicht verbietet. [herr]Und den Blitz kann Rupert nicht lenken. Ob und wen er trifft, "
     "liegt außerhalb jeder menschlichen Beherrschung. [zuneg]Es fehlt schon an einer rechtlich missbilligten Gefahr. Der "
     "Tod ist Rupert nicht objektiv zuzurechnen. [tsneg]Totschlag scheidet aus, und mit ihm der Mord.", P),
    # --- G Vorsatzlösung der Rechtsprechung --------------------------------------------------------------------------------
    ("[rspr]Die Rechtsprechung prüft die objektive Zurechnung bei Vorsatztaten nicht als eigene Stufe. Sie löst solche "
     "Fälle beim Vorsatz. [vors]Er muss den Geschehensablauf umfassen. Unwesentlich sind Abweichungen in den Grenzen "
     "allgemeiner Lebenserfahrung. [wunsch]Nach dieser Lösung kann Rupert einen Tod durch Blitz nur erhoffen, nicht "
     "herbeiführen. Ein bloßer Wunsch ist kein Vorsatz. [gleich]Beide Wege führen hier zum selben Ergebnis.", PS),
    # --- H Abwandlung ------------------------------------------------------------------------------------------------------
    ("[abw]Anders in einer Abwandlung: Weiß Rupert, dass im Wald ein Täter auf Hildegard wartet, schafft er mit diesem "
     "Sonderwissen eine rechtlich missbilligte Gefahr.", PS),
    # --- I § 222 (Wortlautkarte) ------------------------------------------------------------------------------------------
    ("[p222]Bleibt die fahrlässige Tötung nach Paragraf zweihundertzweiundzwanzig: Wer durch Fahrlässigkeit den Tod eines "
     "Menschen verursacht. [p222b]Auch hier rechnet der Bundesgerichtshof einen Erfolg nur zu, wenn sich gerade die vom "
     "Täter gesetzte Gefahr im Erfolg verwirklicht hat. [p222c]Der Rat zum Spaziergang verletzt keine Sorgfaltspflicht und "
     "schafft keine solche Gefahr. [straflos]Rupert ist weder wegen Totschlags noch wegen fahrlässiger Tötung strafbar.", PS),
    # --- J Weitere Fallgruppen (Lehre) -------------------------------------------------------------------------------------
    ("[gruppen]Neben dem allgemeinen Lebensrisiko kennt die Lehre weitere Fallgruppen, in denen die Zurechnung fehlen kann. "
     "[g1]Erstens der Schutzzweck der Norm: Der Erfolg muss in den Bereich fallen, den die verletzte Pflicht schützen soll. "
     "[g2]Zweitens die eigenverantwortliche Selbstgefährdung des Opfers, dazu die Folgen achtundfünfzig und zweihundertdrei. "
     "[g3]Drittens der atypische Kausalverlauf, der völlig außerhalb der Lebenserfahrung liegt. [g4]Viertens das "
     "rechtmäßige Alternativverhalten: Zugerechnet wird ein Erfolg nur, wenn er bei pflichtgemäßem Verhalten ausgeblieben "
     "wäre.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die objektive Zurechnung prüfst du im objektiven Tatbestand, direkt nach der Kausalität. "
     "[k1]Ausführlich wird es nur, wenn der Fall Anlass gibt: bei Zufall und Natur, beim Opfer selbst oder bei Dritten. "
     "Sonst genügt ein Satz. [k2]Den Weg der Rechtsprechung über den Vorsatz erwähnst du kurz. Führt er zum selben "
     "Ergebnis, musst du den Streit nicht entscheiden.", P),
    # --- L Klausurschema (Lexi), progressiv --------------------------------------------------------------------------------
    ("[sch]So sieht die Prüfung aus: [s1]Paragraf zweihundertzwölf, objektiver Tatbestand. Erstens der Erfolg: Hildegard "
     "ist tot. [s2]Zweitens die Kausalität: gegeben. [s3]Drittens die objektive Zurechnung: keine rechtlich missbilligte "
     "Gefahr. [s4]Damit entfällt der Tatbestand. [s5]Paragraf zweihundertzweiundzwanzig scheitert aus demselben Grund.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Kausalität allein macht noch keinen Täter. [m2]Zurechenbar ist der Erfolg nur, wenn der Täter eine "
     "rechtlich missbilligte Gefahr geschaffen hat, die sich im Erfolg verwirklicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
