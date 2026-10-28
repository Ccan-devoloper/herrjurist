"""Folge 241 · Strauß-Karikatur: Darf man Politiker als Tiere zeichnen? (Mo · Der Fall · Grundrechte, Klassiker-Fall;
Art. 5 III 1, 5 I, 1 I GG). Echter Fall sachlich: BVerfG, Beschl. v. 3.6.1987 – 1 BvR 313/85, BVerfGE 75, 369
(Strauß-Karikatur; Volltext DFR, zitiert mit der Seite der amtlichen Sammlung <…>).
DARSTELLUNG: Die Original-Karikaturen werden NICHT nachgezeichnet, keine sexuelle Darstellung; Tiere nur als neutrales
Icon (Schwein, Fuchs) ohne Kontext. Die reale Person ist KEINE Figur; der Name steht nur als Fallbezeichnung
(„Strauß-Karikatur“). „in einer sexuell herabwürdigenden Pose“ einmal sachlich im Hook.
Fiktiver Rahmen: Karikaturist Meinrad (Stimme christian), Redakteurin Henriette (lucy), Ministerpräsidentin Achenbach
(hilde). stephan nicht besetzt (also nie stephan/christian zusammen). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Artikel im Sprechtext als Wörter; kein Genitiv eines Figurennamens. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Meinrad": "christian", "Henriette": "lucy", "Achenbach": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall (fiktiv): Redaktion, Büro der Ministerpräsidentin, Amtsgericht ----------------------------------------------
    ("[fall]Die Redaktion eines Satiremagazins. [zeich]Der Karikaturist Meinrad zeichnet die Ministerpräsidentin "
     "Achenbach als Schwein, [pose]in einer sexuell herabwürdigenden Pose. [botsch]Seine Botschaft: Sie mache Politik "
     "für Bauinvestoren.", P),
    ("[he1]Satire darf alles. Das drucken wir.", P, "Henriette"),
    ("[heft]Das Heft erscheint, und die Ministerpräsidentin sieht die Zeichnung.", P),
    ("[ac1]Das ist keine Kritik mehr, das ist entwürdigend. Ich stelle Strafantrag.", P, "Achenbach"),
    ("[urteil]Das Amtsgericht verurteilt Meinrad wegen Beleidigung.", P),
    ("[me1]Das ist Kunst. Ich kritisiere ihre Politik.", P, "Meinrad"),
    ("[frage]Darf man Politiker als Tiere zeichnen? Und verletzt die Verurteilung die Kunstfreiheit von Meinrad? "
     "[klassiker]Die Antwort gibt ein Klassiker des Bundesverfassungsgerichts: der Beschluss zur Strauß-Karikatur.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Schutzbereich (Wortlautkarte Art. 5 Abs. 3 Satz 1 GG; BVerfGE 75, 369 <377>) ---------------------------------
    ("[a53]Artikel fünf Absatz drei Satz eins: Kunst und Wissenschaft, Forschung und Lehre sind frei. [kunst]Ist eine "
     "Karikatur Kunst? [beleg]Ja. Das Gericht sah in den Zeichnungen das geformte Ergebnis einer freien schöpferischen "
     "Gestaltung, in welcher der Zeichner seine Eindrücke, Erfahrungen und Erlebnisse zu unmittelbarer Anschauung "
     "bringt. [v160]Die drei Kunstbegriffe erklärt die Folge zum Mephisto-Beschluss.", P),
    ("[niveau]Ob die Zeichnung gut oder geschmacklos ist, spielt keine Rolle: Eine Niveaukontrolle wäre eine "
     "unzulässige Inhaltskontrolle. [meinung]Meinrad äußert zugleich eine Meinung. [nausschl]Kunst und Meinungsäußerung "
     "schließen sich nicht aus. [spez]Maßgeblich bleibt aber Artikel fünf Absatz drei, als die spezielle Norm. "
     "[v238]Die Meinungsfreiheit mit den Schranken aus Absatz zwei zeigt die Folge zu „Soldaten sind Mörder“. "
     "[eingriff]Die Verurteilung wegen Beleidigung greift in die Kunstfreiheit ein.", P),
    # --- D III. Rechtfertigung: kollidierendes Verfassungsrecht (Wortlautkarte Art. 1 Abs. 1 GG) -------------------------
    ("[vorb]Einen Gesetzesvorbehalt hat die Kunstfreiheit nicht. [kolli]Grenzen setzt nur kollidierendes "
     "Verfassungsrecht, [apr]hier das allgemeine Persönlichkeitsrecht der Ministerpräsidentin, mit seinem Kern: "
     "[a11]Artikel eins Absatz eins: Die Würde des Menschen ist unantastbar. [p185]Paragraf hundertfünfundachtzig StGB "
     "schützt die Ehre und gilt auch gegenüber der Kunst. [licht]Er muss aber im Licht der Kunstfreiheit ausgelegt "
     "werden.", PS),
    # --- E Der echte Fall (BVerfGE 75, 369 <369–371, 376>) -------------------------------------------------------------
    ("[echt]Nun der echte Fall von neunzehnhundertsiebenundachtzig. [echt1]Ein Karikaturist zeichnete in einer "
     "Zeitschrift den damaligen bayerischen Ministerpräsidenten mehrfach als Schwein, in ähnlichen Posen, [robe]dazu "
     "Schweine in Richterrobe. [olg]Das Oberlandesgericht sprach ihn der Beleidigung in drei Fällen schuldig. "
     "[vb]Dagegen erhob er Verfassungsbeschwerde.", P),
    # --- F Deutung: Aussagekern und Einkleidung (<377 f.>) ------------------------------------------------------------
    ("[deut]Wie prüft man Satire? [verfr]Sie arbeitet mit Übertreibungen, Verzerrungen und Verfremdungen. "
     "[entkl]Deshalb muss man ihr zuerst das satirische Gewand ausziehen: [kern]Was ist der Aussagekern? [einkl]Und was "
     "ist nur die Einkleidung? [gesond]Beides wird gesondert darauf geprüft, ob es eine Missachtung der Person "
     "ausdrückt. [milde]Für die Einkleidung gilt dabei ein weniger strenger Maßstab, denn ihr ist die Verfremdung "
     "wesenseigen.", PS),
    # --- G Echter Fall: Kern und Einkleidung, Menschenwürde (<379–381>) --------------------------------------------------
    ("[kern1]Im echten Fall lautete der Aussagekern: Der Politiker mache sich die Justiz in anstößiger Weise zunutze. "
     "[einkl1]Die Einkleidung zeigte ihn als Schwein bei sexuellem Verhalten. [entw]Dazu das Gericht: Gerade die "
     "Darstellung sexuellen Verhaltens sollte den Betroffenen als Person entwerten, ihn seiner Würde als Mensch "
     "entkleiden. [oeff]Dass er als Politiker im öffentlichen Meinungskampf stand, ändert daran nichts: Er muss mehr "
     "Kritik hinnehmen, verliert aber nicht seine personale Würde.", P),
    ("[abw]Sonst wird abgewogen; das Persönlichkeitsrecht hat keinen generellen Vorrang vor der Kunst. [absolut]Soweit "
     "es aber unmittelbarer Ausfluss der Menschenwürde ist, wirkt diese Schranke absolut, ohne die Möglichkeit eines "
     "Güterausgleichs. [erg]Ergebnis: Die Verurteilung wegen Beleidigung war verfassungsgemäß, [zurueck]die "
     "Verfassungsbeschwerde wurde zurückgewiesen.", PS),
    # --- H Zurück zum Fall ---------------------------------------------------------------------------------------------
    ("[zur]Zurück zu Meinrad. [zk]Sein Aussagekern, Politik für Bauinvestoren, ist scharfe politische Kritik, und die "
     "muss eine Ministerpräsidentin aushalten. [ze]Die Einkleidung aber soll sie als Person entwerten. [zm]Das trifft "
     "den Kern ihrer Menschenwürde. [zv]Die Verurteilung nach Paragraf hundertfünfundachtzig verletzt seine "
     "Kunstfreiheit nicht.", PS),
    # --- I Gegenfall: Tiergestalt allein (<379>) -----------------------------------------------------------------------
    ("[gegen]Darf man Politiker also nie als Tiere zeichnen? Das folgt daraus nicht.", 0.2),
    ("[me2]Dann zeichne ich sie eben als Fuchs.", P, "Meinrad"),
    ("[fuchs]Ein Fuchs, der Investoren die Tür aufhält, überspitzt einen Charakterzug. [ueblich]Das ist die übliche "
     "Karikatur, die das Gericht ausdrücklich abgrenzt: Die Tiergestalt allein greift die Würde nicht an. [abw2]Dann ist die "
     "Menschenwürde nicht berührt, und es bleibt bei der Abwägung, mit dem milderen Maßstab für die Einkleidung.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Steckt eine Meinung in einem Kunstwerk, prüfst du Artikel fünf Absatz drei, nicht Absatz eins, "
     "[t1]und deshalb auch nicht die Schranken aus Absatz zwei. [t2]Trenne Aussagekern und Einkleidung, und prüfe beide "
     "gesondert. [t3]Und nimm einen Angriff auf die Menschenwürde nicht vorschnell an: Nur dann entfällt die Abwägung.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Schutzbereich, die Karikatur als Kunst. [k2]Römisch zwei: Eingriff durch "
     "die Verurteilung. [k3]Römisch drei: Rechtfertigung. [k3a]Erstens: kollidierendes Verfassungsrecht, Paragraf "
     "hundertfünfundachtzig zum Schutz des Persönlichkeitsrechts. [k3b]Zweitens: Deutung, also Aussagekern und "
     "Einkleidung. [k3c]Drittens: Abwägung, außer bei einem Angriff auf die Menschenwürde.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Satire darf übertreiben und verfremden, auch in Tiergestalt. [m2]Wer aber einen Menschen als Person "
     "entwertet, trifft seine Würde, und dort endet die Kunstfreiheit.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    for n in ("Meinrads", "Henriettes", "Achenbachs"):
        assert n not in text, f"Genitiv: {n}"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
