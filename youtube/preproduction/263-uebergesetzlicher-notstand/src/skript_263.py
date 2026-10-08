"""Folge 263 · Leben gegen Leben: Übergesetzlicher entschuldigender Notstand (Mi · Examenswissen · StGB AT, Format Streitstand).
Übungsfall nach dem Plan-Hook („Eine Stellwerksmitarbeiterin lenkt einen führerlosen Güterzug auf ein Nebengleis, wo ein
einzelner Arbeiter steht“): Montag, 6:40 Uhr. Frau Seefeld (Ende 20) hat Dienst im Stellwerk. Herr Nordmann aus dem
Nachbarstellwerk meldet einen führerlosen Güterzug, die Bremsen greifen nicht. Auf Gleis 1 arbeitet ein Bautrupp (5 Arbeiter),
über Funk nicht erreichbar. Anhalten unmöglich; einzige Möglichkeit: Weiche 7 auf das Nebengleis, wo ein einzelner Arbeiter
steht (ebenfalls nicht erreichbar). Sie stellt um; die 5 bleiben unverletzt, der Arbeiter auf dem Nebengleis kommt ums Leben.
Darstellung: kein Zusammenstoß, kein Opfer im Bild – Zug und Weiche als Symbole im Schienenplan, Arbeiter als Silhouetten mit
Abstand.
Aufbau (Streitstand, laut Auftrag): 1. Hook → Sachverhalt → Tatbestand § 212 kurz → 2. § 34 (Wortlautkarte): „wesentlich
überwiegt“ – Leben nicht abwägbar (BVerfGE 115, 118 Rn. 85, 124; Art. 1 Abs. 1 GG) → rechtswidrig (Verweis 013, 189)
→ 3. § 35 (Wortlautkarte): Personenkreis (−) → 4. übergesetzlicher entschuldigender Notstand: Herkunft (Ärzteverfahren der
Nachkriegszeit, OGHSt 1, 321; Verweis BVerfGE 115, 118 Rn. 130), Voraussetzungen, Ansichten (Entschuldigung / persönlicher
Strafausschließungsgrund / Ablehnung beim Umlenken), Gefahrengemeinschaft vs. Weichensteller → 5. Ergebnis je Ansicht
→ 6. Klausurtipp (Lexi), Schema, Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung „263: Seefeld, Nordmann“; Volltextsuche unter youtube/
ohne Treffer). Die Arbeiter bleiben namenlos.
Stimmen (Pool niklas, helmut, ela_froh, julia): Frau Seefeld julia (Frau, jung), Herr Nordmann helmut (Mann, älter); niklas und
ela_froh nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Artikel im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Seefeld": "julia", "Nordmann": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Stellwerk, Anruf, Weiche -----------------------------------------------------------------------------------
    ("[fall]Montag, sechs Uhr vierzig. [seefeld]Frau Seefeld, Ende zwanzig, hat Dienst im Stellwerk. [anruf]Da ruft "
     "Herr Nordmann aus dem Nachbarstellwerk an.", P),
    ("[no1]Ein Güterzug rollt führerlos auf deinen Bereich zu! Die Bremsen greifen nicht.", P, "Nordmann"),
    ("[gleis1]Auf Gleis eins arbeitet ein Bautrupp, fünf Arbeiter. [funk]Frau Seefeld funkt sie an.", 0.2),
    ("[se1]Gleis eins, sofort räumen! Bitte melden! Keine Antwort.", P, "Seefeld"),
    ("[halt]Anhalten kann sie den Zug nicht. [weiche]Sie kann nur die Weiche sieben umstellen, auf das Nebengleis. "
     "[einer]Dort steht ein einzelner Arbeiter, auch er ist nicht zu erreichen. [stellt]Frau Seefeld stellt die Weiche um. "
     "[neben]Der Zug fährt auf das Nebengleis. [fuenf]Die fünf bleiben unverletzt. [tot]Der Arbeiter auf dem Nebengleis "
     "kommt ums Leben.", P),
    ("[se2]Ich hatte nur die Wahl: einer oder fünf.", P, "Seefeld"),
    ("[frage]Hat sich Frau Seefeld wegen Totschlags strafbar gemacht? [frage2]Darf man ein Leben opfern, um fünf zu "
     "retten?", PS),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand -------------------------------------------------------------------------------------------------------
    ("[tb]Zuerst der Tatbestand: [tb212]Frau Seefeld hat einen Menschen getötet, Paragraf zweihundertzwölf. [vors]Sie sah "
     "den Arbeiter und wusste, dass der Zug ihn erfassen würde. Vorsatz liegt vor. [rw]Ist die Tat gerechtfertigt?", PS),
    # --- D § 34 (Wortlautkarte) ---------------------------------------------------------------------------------------------
    ("[p34]In Betracht kommt der rechtfertigende Notstand, Paragraf vierunddreißig. [lage]Für die fünf Arbeiter bestand "
     "eine gegenwärtige Gefahr für ihr Leben, [mittel]und die Weiche war das einzige Mittel. [abw]Aber das geschützte "
     "Interesse muss das beeinträchtigte wesentlich überwiegen. [v189]Das ganze Schema zeigt das Video zum "
     "Berghütten-Fall.", PS),
    # --- E Leben gegen Leben ------------------------------------------------------------------------------------------------
    ("[zahl]Fünf Leben gegen eines: Überwiegt das nicht? [nein34]Nach herrschender Meinung nicht. [nicht]Leben ist "
     "nicht abwägbar, auch nicht nach der Zahl. [bverfg]Das Bundesverfassungsgericht sagt im Urteil zum "
     "Luftsicherheitsgesetz: [gleich]Jedes menschliche Leben ist als solches gleich wertvoll. [objekt]Tötet der Staat "
     "Unbeteiligte, um andere zu retten, benutzt er sie als bloßes Mittel [wuerde]und missachtet ihre Würde, Artikel eins "
     "Absatz eins Grundgesetz.", P),
    ("[staat]Das Gericht sprach über den Staat. [lehre]Die Strafrechtslehre überträgt den Gedanken auf Paragraf "
     "vierunddreißig. [rw_erg]Frau Seefeld handelt also rechtswidrig. [v013]Mehr zum Urteil im Video zum "
     "Luftsicherheitsgesetz.", PS),
    # --- F § 35 (Wortlautkarte) ---------------------------------------------------------------------------------------------
    ("[p35]Bleibt die Schuld. Paragraf fünfunddreißig entschuldigt, wer in einer gegenwärtigen, nicht anders abwendbaren "
     "Gefahr für Leben, Leib oder Freiheit handelt, [kreis]um die Gefahr von sich, einem Angehörigen oder einer anderen "
     "ihm nahestehenden Person abzuwenden. [fremd]Die fünf Arbeiter kennt Frau Seefeld nicht. [nein35]Paragraf "
     "fünfunddreißig greift nicht.", PS),
    # --- G Übergesetzlicher entschuldigender Notstand: Herkunft und Voraussetzungen -----------------------------------------
    ("[ueber]Hier setzt der übergesetzliche entschuldigende Notstand an. [kein_g]Er steht in keinem Gesetz. [hist]Bedeutsam "
     "wurde er nach dem Krieg, in Strafverfahren gegen Ärzte, die an den nationalsozialistischen Krankenmorden mitgewirkt "
     "hatten. [listen]Einzelne Patienten hatten sie von den Listen gestrichen, um sie zu retten. [offen]Auf diese "
     "Rechtsprechung verweist auch das Bundesverfassungsgericht. Die strafrechtliche Bewertung lässt es ausdrücklich "
     "offen.", PS),
    ("[vor]Seine Befürworter verlangen: [v1]eine ausweglose Lage mit Gefahr für Leben, [v2]die Tat als einziges Mittel, "
     "um ein größeres Unheil abzuwenden, [v3]und einen Täter, der nach gewissenhafter Prüfung handelt, um zu retten.", PS),
    # --- H Ansichten ----------------------------------------------------------------------------------------------------------
    ("[ans]Wie wirkt er? [a1]Die wohl herrschende Lehre sieht einen ungeschriebenen Entschuldigungsgrund: Die Tat bleibt "
     "rechtswidrig, die Schuld entfällt. [a2]Der Oberste Gerichtshof für die Britische Zone hielt in einem Ärzteverfahren "
     "einen persönlichen Strafausschließungsgrund für möglich: [a2b]Unrecht und Schuld bleiben, nur die Strafe entfällt.", PS),
    # --- I Gefahrengemeinschaft und Weichensteller --------------------------------------------------------------------------
    ("[gg]Anerkannt wird die Figur vor allem bei der Gefahrengemeinschaft: [gg2]Alle Betroffenen stehen schon in derselben "
     "Gefahr, und der Täter rettet wenigstens einige, so in den Ärztefällen. [weichen]Unser Fall ist anders, der "
     "Weichenstellerfall: [unbet]Der Arbeiter auf dem Nebengleis war gar nicht in Gefahr. Frau Seefeld lenkt sie erst auf "
     "ihn um. [a3]Deshalb lehnt eine Gegenansicht die Entschuldigung hier ab: Wer einen bisher Unbeteiligten opfert, "
     "bleibt strafbar. [a4]Andere entschuldigen auch dann, wenn die Lage ausweglos war.", PS),
    # --- J Ergebnis je Ansicht ----------------------------------------------------------------------------------------------
    ("[lsg]Und das Ergebnis im Fall? [l1]Wer den übergesetzlichen Notstand auch beim Umlenken anwendet, kommt zur "
     "Straflosigkeit, als Entschuldigung oder als Strafausschließungsgrund. [l2]Wer ihn auf Gefahrengemeinschaften "
     "beschränkt, bejaht Totschlag, Paragraf zweihundertzwölf. [l3]Die Notlage zählt dann bei der Strafe; in Betracht kommt "
     "ein minder schwerer Fall nach Paragraf zweihundertdreizehn. [l4]Vertretbar ist beides, entscheidend ist die "
     "Begründung.", P),
    ("[se3]Dann hängt alles an diesem Streit.", PS, "Seefeld"),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Reihenfolge ein. [k1]Paragraf vierunddreißig lehnst du in der Rechtswidrigkeit ab: Leben "
     "gegen Leben. [k2]Paragraf fünfunddreißig scheitert in der Schuld am Personenkreis. [k3]Erst dann prüfst du den "
     "übergesetzlichen Notstand, ebenfalls in der Schuld. [k4]Und denk an die Folge: Die Tat bleibt rechtswidrig. "
     "[k5]Gegen sie ist Notwehr möglich, und wer hilft, kann sich als Teilnehmer strafbar machen.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Eins, Tatbestand, Paragraf zweihundertzwölf. [s2]Zwei, Rechtswidrigkeit: Paragraf "
     "vierunddreißig scheitert, Leben ist nicht abwägbar. [s3]Drei, Schuld: Paragraf fünfunddreißig, Personenkreis. "
     "[s4]Dann der übergesetzliche entschuldigende Notstand mit Voraussetzungen [s5]und dem Streit beim Umlenken auf "
     "Unbeteiligte. [s6]Vier, das Ergebnis je nach Ansicht.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Leben gegen Leben rechtfertigt nicht, auch nicht eins gegen fünf. [m2]Paragraf fünfunddreißig hilft "
     "nur bei Gefahr für dich und dir nahestehende Menschen. [m3]Der übergesetzliche Notstand kann allenfalls "
     "entschuldigen, und beim Umlenken auf Unbeteiligte ist genau das umstritten.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
