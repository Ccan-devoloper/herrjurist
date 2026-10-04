"""Folge 169 · Drei-Stufen-Theorie: Das Apotheken-Urteil zur Berufsfreiheit (Mo · Der Fall · Klassiker-Fall; Art. 12 I GG).
Echter Fall sachlich nacherzählt: BVerfG, Urt. v. 11.6.1958 – 1 BvR 596/56, BVerfGE 7, 377 (Apotheken-Urteil), Volltext DFR
(servat.unibe.ch/dfr/bv007377.html), Seiten der amtlichen Sammlung <…>. Klausurtipp zusätzlich BVerfGE 77, 84 <106>.
Heutige Rechtslage: § 2 Abs. 1 ApoG (gesetze-im-internet.de, Abruf 04.10.2026).
Der reale Beschwerdeführer („Karl-Heinz R.“) wird nicht benannt und nicht dargestellt.
Moderner Einstieg mit fiktiven Figuren: Grete (Apothekerin, Stimme ela_froh) und Herr Dannemann (Sachbearbeiter der
Erlaubnisbehörde, Stimme helmut; Name nur auf dem Namensschild).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Grete": "ela_froh", "Dannemann": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Einstieg (fiktiv) ---------------------------------------------------------------------------------------------
    ("[fall]Grete ist Apothekerin, mit Approbation und Berufserfahrung. [laden]In ihrem Stadtteil will sie eine eigene "
     "Apotheke eröffnen und beantragt die Erlaubnis.", P),
    ("[h1]Die Erlaubnis bekommen Sie nicht. In Ihrem Stadtteil gibt es schon genug Apotheken.", P, "Dannemann"),
    ("[o1]Aber ich bin voll ausgebildet! Darf der Staat mich deshalb aussperren?", P, "Grete"),
    ("[frage0]Darf der Staat die Zahl der Apotheken nach dem Bedarf begrenzen? [klassiker]Darüber entschied das "
     "Bundesverfassungsgericht neunzehnhundertachtundfünfzig im Apotheken-Urteil.", PS),
    # --- B Der echte Fall (BVerfGE 7, 377 <379–382>) -------------------------------------------------------------------------
    ("[bf]Ein angestellter Apotheker beantragte neunzehnhundertsechsundfünfzig die Erlaubnis, in Traunreut in Oberbayern "
     "eine eigene Apotheke zu eröffnen. [norm]Nach dem bayerischen Apothekengesetz durfte eine neue Apotheke nur "
     "zugelassen werden, wenn sie im öffentlichen Interesse lag [wirt]und wenn ihre wirtschaftliche Grundlage gesichert "
     "war, ohne die der Nachbarapotheken zu stark zu beeinträchtigen.", P),
    ("[abl]Die Behörde lehnte ab: Für rund sechstausend Menschen genüge die eine vorhandene Apotheke völlig, "
     "[umsatz]und deren Umsatz würde um vierzig Prozent sinken. [vb]Der Apotheker erhob Verfassungsbeschwerde.", P),
    ("[frage]Verletzt die Regelung seine Berufsfreiheit?", PS),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Art. 12 Abs. 1 GG (<397–403>) -----------------------------------------------------------------------------------
    ("[a12]Artikel zwölf Absatz eins: Alle Deutschen haben das Recht, Beruf, Arbeitsplatz und Ausbildungsstätte frei zu "
     "wählen. Die Berufsausübung kann durch Gesetz oder auf Grund eines Gesetzes geregelt werden. [beruf]Beruf ist nach "
     "dem Gericht jede erlaubte Tätigkeit, die man zur Grundlage seiner Lebensführung macht, auch eine untypische. [selbst]Und "
     "der Schritt vom angestellten zum selbständigen Apotheker ist selbst eine Berufswahl.", P),
    ("[wahl]Der Wortlaut deutet an, der Gesetzgeber dürfe nur die Ausübung regeln. [trenn]Doch Wahl und Ausübung lassen sich "
     "nicht scharf trennen: Wer einen Beruf aufnimmt, übt ihn aus und wählt ihn zugleich. [einheit]Artikel zwölf ist "
     "deshalb ein einheitliches Grundrecht der Berufsfreiheit; der Regelungsvorbehalt in Satz zwei gilt für Ausübung und "
     "Wahl. [intens]Aber nicht gleich stark: Je mehr eine Regelung die Berufswahl berührt, desto enger sind ihre Grenzen.", PS),
    # --- E Die drei Stufen (<405–408>) -------------------------------------------------------------------------------------
    ("[stufen]Daraus entwickelt das Gericht mehrere Stufen; die Lehre nennt das die Drei-Stufen-Theorie.", P),
    ("[s1]Stufe eins: Regelungen der Berufsausübung, also wie jemand seinen Beruf ausübt, etwa Pflichten zur "
     "Vorratshaltung in der Apotheke. [s1r]Sie sind zulässig, soweit vernünftige Erwägungen des Gemeinwohls sie "
     "zweckmäßig erscheinen lassen.", P),
    ("[s2]Stufe zwei: subjektive Zulassungsvoraussetzungen, die in der Person liegen, vor allem die Ausbildung, beim "
     "Apotheker die Approbation. [s2r]Sie sind zulässig zum Schutz besonders wichtiger Gemeinschaftsgüter und dürfen zum "
     "Zweck, den Beruf ordnungsgemäß auszuüben, nicht außer Verhältnis stehen.", P),
    ("[s3]Stufe drei: objektive Zulassungsvoraussetzungen. Sie haben mit der Person nichts zu tun, der Bewerber kann sie "
     "nicht beeinflussen. [s3r]Rechtfertigen kann sie im Allgemeinen nur die Abwehr nachweisbarer oder "
     "höchstwahrscheinlicher schwerer Gefahren für ein überragend wichtiges Gemeinschaftsgut. [konk]Bloßer "
     "Konkurrenzschutz reicht nie.", P),
    ("[gr]Dabei gilt: Der Gesetzgeber muss die Stufe wählen, die am wenigsten in die Berufswahl eingreift. "
     "[naechst]Die nächste Stufe darf er erst betreten, wenn sich die Gefahren mit Mitteln der vorigen Stufe nicht "
     "wirksam bekämpfen lassen. [vh]Die Lehre versteht die Stufen deshalb als konkretisierte Verhältnismäßigkeit; "
     "wie man diese prüft, zeigt eine eigene Folge.", PS),
    # --- F Anwendung und Ergebnis (<393 f., 414–444>, Entscheidungsformel <379>) -------------------------------------------
    ("[einord]Und das bayerische Gesetz? Ob am Ort noch eine Apotheke gebraucht wird und ob sie sich trägt, liegt nicht "
     "in der Hand des Bewerbers. [obj]Diese Prüfung von Bedarf und Tragfähigkeit ist eine objektive Zulassungsvoraussetzung, die schärfste "
     "Stufe.", P),
    ("[volk]Das Ziel des Gesetzes, die Volksgesundheit, ist unbestritten ein wichtiges Gemeinschaftsgut. [gefahr]Doch das Gericht "
     "konnte sich nicht davon überzeugen, dass ohne die Beschränkung eine Gefahr droht. [schweiz]In vergleichbaren "
     "Staaten wie der Schweiz gab es volle Niederlassungsfreiheit, ohne dass die Volksgesundheit ernstlich gefährdet "
     "war. [milder]Und mögliche Gefahren ließen sich auf den milderen Stufen bekämpfen, etwa durch eine "
     "Berufsgerichtsbarkeit.", P),
    ("[erg]Ergebnis am elften Juni neunzehnhundertachtundfünfzig: Die Bescheide verletzen das Grundrecht aus Artikel "
     "zwölf Absatz eins und werden aufgehoben. [nichtig]Artikel drei Absatz eins des Apothekengesetzes ist nichtig. "
     "[nl]Im Apothekenrecht entsprach der Verfassung damit allein die Niederlassungsfreiheit, verstanden als das Fehlen "
     "objektiver Zulassungsschranken.", PS),
    # --- G Zurück zum Einstieg (§ 2 Abs. 1 ApoG) --------------------------------------------------------------------------
    ("[o2]Und was heißt das für meine Apotheke?", P, "Grete"),
    ("[heute]Heute ist die Erlaubnis nach Paragraf zwei des Apothekengesetzes des Bundes auf Antrag zu erteilen, wenn die "
     "Voraussetzungen vorliegen, etwa die Approbation. [kein]Ob es im Stadtteil schon genug Apotheken gibt, gehört nicht "
     "dazu. [gr2]Eine solche Bedürfnisprüfung wäre eine objektive Zulassungsschranke. Erfüllt Grete die gesetzlichen "
     "Voraussetzungen, bekommt sie ihre Erlaubnis.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst die Stufe, dann den Maßstab der Rechtfertigung. [tipp2]Achtung: Auch eine "
     "Berufsausübungsregelung kann in ihren Auswirkungen einem Eingriff in die Berufswahl nahekommen. Dann genügt nicht "
     "jede vernünftige Erwägung des Gemeinwohls.", PS),
    # --- I Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Schutzbereich, also ein Beruf, auch der Schritt in die Selbständigkeit. "
     "[k2]Römisch zwei: Eingriff, und auf welcher Stufe: Ausübung, subjektive oder objektive Zulassung. [k3]Römisch drei: Rechtfertigung, mit "
     "gesetzlicher Grundlage nach Satz zwei, [k4]dem Maßstab der jeweiligen Stufe [k5]und der niedrigsten Stufe, die "
     "zum Ziel führt.", PS),
    # --- J Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Je näher eine Regelung an die freie Berufswahl rückt, desto gewichtiger muss ihr Grund sein. "
     "[m2]Objektive Zulassungsschranken rechtfertigt in aller Regel nur die Abwehr schwerer Gefahren für ein überragend wichtiges "
     "Gemeinschaftsgut.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
