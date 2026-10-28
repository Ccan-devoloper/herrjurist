"""Folge 236 · Schadensersatz Kaufrecht § 437 Nr. 3 BGB: Welche Anspruchsgrundlage? (Mi · Examenswissen · Kaufrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Das gekaufte Heizgerät ist defekt und setzt nach einer Woche den Keller in Brand.“):
Katharina (privat) kauft für ihren Hobbykeller im Elektrogeschäft von Raimund ein Heizgerät für 600 €; Raimund hat es original
verpackt vom Hersteller bezogen. Eine Woche später schmort ein Bauteil durch: Rauch, ein Regal brennt an, die Wand verrußt;
niemand verletzt; Kellerschaden 4.000 €. Das Bauteil war ab Werk fehlerhaft (Fehler des Herstellers), für Raimund nicht
erkennbar. Katharina verlangt ein neues Gerät und 4.000 €; Raimund bietet ein neues Gerät an, lehnt die 4.000 € ab.
Schema: § 437 Nr. 3 (Wortlautkarte) als Rechtsgrundverweisung, Mangel (§ 434 Abs. 3 Satz 1 Nr. 1) → Kontrollfrage (Lehre;
BGH VIII ZR 169/12 Rn. 26 f., VII ZR 63/18 Rn. 17, 19; Formulierungen wie Folge 177) → vier Wege: behebbar §§ 280 I, III, 281
(Frist, Ausnahmen §§ 281 II, 440, 475d; Verweis 209), nachträglich unbehebbar §§ 280 I, III, 283 (Wortlautkarte), anfänglich
unbehebbar § 311a II (Wortlautkarte), Mangelfolgeschaden § 280 I ohne Frist (BT-Drucks. 14/6040 S. 224 f.); Verzögerung der
Nacherfüllung §§ 280 II, 286 (ein Satz) → Vertretenmüssen des Händlers (V ZR 93/08 Rn. 19; VIII ZR 211/07 Rn. 29) →
Hersteller: ProdHaftG / § 823 I (ein Satz, Verweis 070) → Ergebnis → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Katharina (lucy), Raimund (stephan); Lexi/Erzählerin Carla. Namen nie im Genitiv.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Katharina": "lucy", "Raimund": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Kauf im Elektrogeschäft -----------------------------------------------------------------------------
    ("[fall]Das gekaufte Heizgerät ist defekt und setzt nach einer Woche den Keller in Brand. [kath]So ergeht es Katharina. "
     "[kauf]Für ihren Hobbykeller kauft sie im Elektrogeschäft von Raimund ein Heizgerät für sechshundert Euro. "
     "[verpackt]Raimund hat es original verpackt vom Hersteller bezogen.", P),
    ("[ra1]Bitte schön, Ihr neues Heizgerät. Viel Freude damit!", P, "Raimund"),
    # --- A2 Fall: eine Woche später im Keller ------------------------------------------------------------------------------
    ("[woche]Eine Woche später schmort im Gerät ein Bauteil durch. [rauch]Es qualmt, ein Regal brennt an, die Wand ist "
     "verrußt. [niemand]Verletzt wird niemand, doch der Schaden im Keller beträgt viertausend Euro. [werk]Später zeigt "
     "sich: Das Bauteil war schon ab Werk fehlerhaft, ein Fehler des Herstellers. [erkenn]Für Raimund war das nicht "
     "erkennbar.", P),
    # --- A3 Fall: Forderung und Antwort, Frage -----------------------------------------------------------------------------
    ("[ka1]Ihr Heizgerät hat meinen Keller verrußt! Ich will ein neues Gerät und viertausend Euro für den Schaden.", P,
     "Katharina"),
    ("[ra2]Ein neues Gerät bekommen Sie. Aber für den Fehler des Herstellers kann ich nichts.", P, "Raimund"),
    ("[frage]Was kann Katharina verlangen, und aus welcher Anspruchsgrundlage? [frage2]Muss Raimund für den Keller "
     "zahlen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 437 Nr. 3 (Wortlaut): Rechtsgrundverweisung, Mangel ------------------------------------------------------------
    ("[agl]Beim Kauf beginnt alles mit Paragraf vierhundertsiebenunddreißig. [w437]Ist die Sache mangelhaft, kann der "
     "Käufer, wenn die Voraussetzungen der folgenden Vorschriften vorliegen, [w437b]nach Nummer drei Schadensersatz "
     "verlangen, nach den dort genannten Paragrafen. [rgv]Das ist eine Rechtsgrundverweisung: Die Voraussetzungen stehen im allgemeinen Schuldrecht, "
     "und sie müssen alle vorliegen. [mangel]Gemeinsamer Ausgangspunkt ist der Mangel. Ein Heizgerät, das durchschmort, "
     "eignet sich nicht für die gewöhnliche Verwendung. [mangel2]Der Fehler steckte schon bei der Übergabe darin. "
     "[sys]Das System dahinter erklärt das Video zum Schadensersatzschema.", PS),
    # --- D Die Kontrollfrage ------------------------------------------------------------------------------------------------
    ("[kf]Welche Vorschrift passt, hängt vom Schaden ab. [kf1]Die Lehre gibt eine Kontrollfrage: Würde eine "
     "ordnungsgemäße Nacherfüllung im letztmöglichen Zeitpunkt den Schaden noch beseitigen? [kf2]Wenn ja, geht es um "
     "Schadensersatz statt der Leistung. [kf3]Wenn nein, um Schadensersatz neben der Leistung, hier aus Paragraf "
     "zweihundertachtzig Absatz eins. [kf4]Der Bundesgerichtshof fragt genauso, ob eine Nacherfüllung den Schaden "
     "beseitigen würde. [kf5]Im Fall: Das kaputte Gerät ersetzt ein neues Gerät. [kf6]Den verrußten Keller repariert es "
     "nicht.", PS),
    # --- E1 Weg 1: behebbarer Mangel, § 281 -----------------------------------------------------------------------------
    ("[wege]Daraus ergeben sich vier Wege. [t1]Erstens: Der Mangel ist behebbar, durch Reparatur oder ein neues Gerät. "
     "[t1a]Dann gelten die Paragrafen zweihundertachtzig Absätze eins und drei und zweihunderteinundachtzig, also "
     "grundsätzlich erst nach einer erfolglosen Frist zur Nacherfüllung. [t1b]Ausnahmen stehen in Paragraf "
     "zweihunderteinundachtzig Absatz zwei und Paragraf vierhundertvierzig, beim Verbrauchsgüterkauf stattdessen in "
     "Paragraf vierhundertfünfundsiebzig d. [t1v]Mehr zur Frist im Video zum Schadensersatz statt der Leistung.", PS),
    # --- E2 Weg 2: nachträglich unbehebbar, § 283 (Wortlaut) ----------------------------------------------------------------
    ("[t2]Zweitens: Der Mangel ist unbehebbar, und das Hindernis entsteht erst nach Vertragsschluss. [w283]Dann "
     "Paragraf zweihundertdreiundachtzig: Braucht der Schuldner nach Paragraf zweihundertfünfundsiebzig nicht zu leisten, "
     "kann der Gläubiger unter den Voraussetzungen des Paragrafen zweihundertachtzig Absatz eins Schadensersatz statt der "
     "Leistung verlangen. [t2b]Eine Frist wäre sinnlos, das Gesetz verlangt keine.", PS),
    # --- E3 Weg 3: anfänglich unbehebbar, § 311a Abs. 2 (Wortlaut) ----------------------------------------------------------
    ("[t3]Drittens: Der Mangel war schon bei Vertragsschluss unbehebbar. [w311]Dann gilt Paragraf dreihundertelf a "
     "Absatz zwei. [w311b]Der Verkäufer haftet nicht, wenn er das Leistungshindernis bei Vertragsschluss nicht kannte und "
     "seine Unkenntnis auch nicht zu vertreten hat.", PS),
    # --- E4 Weg 4: Mangelfolgeschaden, § 280 Abs. 1; Verzögerung --------------------------------------------------------------
    ("[t4]Viertens: der Mangelfolgeschaden, etwa ein Schaden an anderen Rechtsgütern, wie hier am Keller. [t4a]Dafür "
     "genügt Paragraf zweihundertachtzig Absatz eins, ohne Frist. [t4b]So sieht es schon die Gesetzesbegründung: Schäden an "
     "anderen Rechtsgütern als der Kaufsache selbst. [t5]Schäden aus einer verzögerten Nacherfüllung sind dagegen "
     "Verzögerungsschaden. [t5b]Dafür braucht es Verzug, Paragraf zweihundertachtzig Absatz zwei mit "
     "zweihundertsechsundachtzig.", PS),
    # --- F Vertretenmüssen des Händlers --------------------------------------------------------------------------------------
    ("[vm]Bleibt der Keller. Auch hier muss Raimund die Pflichtverletzung zu vertreten haben. [vm2]Das wird vermutet, aber Raimund kann sich entlasten. [vm3]Nach dem Bundesgerichtshof muss ein "
     "Verkäufer die Ware regelmäßig nicht untersuchen. [vm4]Und ein Verschulden des Herstellers wird ihm nicht "
     "zugerechnet, denn der Hersteller ist nicht sein Erfüllungsgehilfe. [vm5]Anders ist es etwa, wenn der Verkäufer eine "
     "Garantie übernommen hat oder Anhaltspunkte für einen Mangel hatte. [vm6]Raimund hat das Gerät original verpackt "
     "verkauft, ohne jeden Anlass zum Verdacht. [vm7]Er hat die mangelhafte Lieferung nicht zu vertreten.", PS),
    # --- G Hersteller (ein Satz, Verweis) ------------------------------------------------------------------------------------
    ("[ph]Für den Keller kommt deshalb der Hersteller in Frage, nach dem Produkthaftungsgesetz oder aus Paragraf "
     "achthundertdreiundzwanzig Absatz eins. [ph2]Mehr dazu im Video zur Produzentenhaftung.", PS),
    # --- H Ergebnis ----------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Das Gerät selbst fällt unter den Schadensersatz statt der Leistung. [erg2]Vorrang hat die "
     "Nacherfüllung, und das neue Gerät bietet Raimund schon an. [erg3]Für den Keller passt Paragraf "
     "zweihundertachtzig Absatz eins, ohne Frist. [erg4]Doch Raimund hat nichts zu vertreten. Die viertausend Euro muss "
     "Katharina beim Hersteller geltend machen.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe jeden Schadensposten einzeln mit der Kontrollfrage. [tipp2]Beim Händler kann der Folgeschaden am "
     "Vertretenmüssen scheitern. [tipp3]Dann prüfe einen Anspruch gegen den Hersteller.", PS),
    # --- J Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k0]Anspruch aus Paragraf vierhundertsiebenunddreißig Nummer drei mit den Paragrafen "
     "zweihundertachtzig folgende. [k1]Eins: Kaufvertrag und Sachmangel bei Gefahrübergang. [k2]Zwei: die Kontrollfrage, "
     "statt oder neben der Leistung. [k3]Drei: die passende Norm, Paragraf zweihunderteinundachtzig, zweihundertdreiundachtzig, "
     "dreihundertelf a oder zweihundertachtzig Absatz eins allein. "
     "[k4]Vier: Vertretenmüssen, vermutet. [k5]Fünf: Schaden.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf vierhundertsiebenunddreißig Nummer drei verweist ins allgemeine Schuldrecht. [mk2]Was "
     "eine Nacherfüllung noch beseitigen könnte, gibt es statt der Leistung, [mk3]den Folgeschaden neben der Leistung, "
     "[mk4]beides nur, wenn der Verkäufer etwas zu vertreten hat.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Katharinas|Raimunds)\b", text), "Genitiv eines Namens"
    assert not re.search(r"\d", text), "Ziffer im Sprechtext"
