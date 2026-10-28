"""Folge 125 · Verbrauchsgüterkauf §§ 474 ff. BGB: Was beim Händler anders ist (Mi · Examenswissen · Zivilrecht/Kaufrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Du kaufst beim Händler einen gebrauchten Fernseher – was gilt anders als
beim Kauf von privat?“): Dirk (privat, Verbraucher) kauft im Laden von Frau Tillmann (Händlerin für gebrauchte
Elektrogeräte, Unternehmerin) einen gebrauchten Fernseher für 250 € und nimmt ihn gleich mit (Ladengeschäft, kein
Fernabsatz, kein Widerruf). Im vorgedruckten Kaufformular steht „Gekauft wie gesehen, keine Gewährleistung“. Vier Monate
später fällt das Bild aus; Dirk hat den Fernseher normal benutzt. Frau Tillmann: „… kaputtgegangen ist er erst bei Ihnen.“
Kern als Zweispalter „von privat“ / „vom Händler“: 1. Anwendungsbereich § 474 Abs. 1 S. 1 (Wortlautkarte); 2. Abweichungs-
verbot § 476 Abs. 1 S. 1 (Wortlautkarte), Abs. 3 (Schadensersatz), privat § 444; 3. negative Beschaffenheitsvereinbarung
§ 476 Abs. 1 S. 2 (Wortlautkarte; BT-Drs. 19/27424 S. 42); 4. Beweislastumkehr § 477 Abs. 1 (Wortlautkarte; BGH VIII ZR
257/23 Rn. 25, 27; VIII ZR 103/15 Rn. 59), privat § 363; 5. Verjährung § 438, § 476 Abs. 2 (Wortlautkarte); 6. Versand
§ 475 Abs. 2 (ein Satz, Abgrenzung). Ergebnis (§ 437, Verweis 063), Klausurtipp, Schema, Merksatz.
Reihenfolge 4/5 gegenüber dem Auftrag getauscht (Beweislast gehört zum Mangel bei Gefahrübergang, Verjährung zur
Durchsetzbarkeit; so folgt der Zweispalter dem Klausuraufbau). Belege: ../RECHTSSTAND.md.
Figuren: Dirk (marc), Frau Tillmann (laura_ruhig); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Dirk": "marc", "Tillmann": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Kauf im Laden ------------------------------------------------------------------------------------------
    ("[fall]Dirk kauft im Laden von Frau Tillmann, die gebrauchte Elektrogeräte verkauft, einen gebrauchten Fernseher für "
     "zweihundertfünfzig Euro. [form]Im vorgedruckten Kaufformular steht: Gekauft wie gesehen, keine Gewährleistung. "
     "[unter]Dirk unterschreibt und nimmt den Fernseher gleich mit.", 0.3),
    # --- A2 Fall: Bild fällt aus -----------------------------------------------------------------------------------------
    ("[ausfall]Vier Monate später fällt das Bild aus. [normal]Dirk hat den Fernseher ganz normal benutzt.", 0.3),
    ("[di1]Das Bild ist weg. Bitte reparieren Sie den Fernseher.", 0.3, "Dirk"),
    ("[ti1]Gekauft wie gesehen, keine Gewährleistung. Und kaputtgegangen ist er erst bei Ihnen.", 0.4, "Tillmann"),
    ("[frage]Muss Frau Tillmann trotzdem für den Defekt einstehen? [frage2]Und was wäre anders, wenn Dirk von privat "
     "gekauft hätte?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau --------------------------------------------------------------------------------------------------------
    ("[plan]Die Antwort steht in den Paragrafen vierhundertvierundsiebzig folgende, den Regeln über den "
     "Verbrauchsgüterkauf. [plan2]Sie sind keine eigene Anspruchsgrundlage, sondern ändern die Käuferrechte aus "
     "Paragraf vierhundertsiebenunddreißig. [plan3]Wir vergleichen Punkt für Punkt: [links]links der Kauf von privat, "
     "[rechts]rechts der Kauf vom Händler.", PS),
    # --- D 1. Anwendungsbereich, § 474 Abs. 1 (Wortlaut) -----------------------------------------------------------------
    ("[a1]Erstens: der Anwendungsbereich, Paragraf vierhundertvierundsiebzig Absatz eins. [a2]Verbrauchsgüterkäufe sind "
     "Verträge, durch die ein Verbraucher von einem Unternehmer eine Ware kauft. [a3]Dirk kauft privat, [a4]Frau Tillmann "
     "verkauft gewerblich, [a5]und ein Fernseher ist eine bewegliche Sache, also eine Ware. [a106]Mehr dazu im Video zum "
     "Verbraucherbegriff. [apr]Von privat gelten die Sonderregeln nicht, es bleibt "
     "beim allgemeinen Kaufrecht.", P),
    # --- E 2. Abweichungsverbot, § 476 Abs. 1 S. 1 (Wortlaut) ------------------------------------------------------------
    ("[b1]Zweitens: das Abweichungsverbot, Paragraf vierhundertsechsundsiebzig Absatz eins Satz eins. [b2]Weicht eine "
     "Vereinbarung vor Mitteilung eines Mangels zum Nachteil des Verbrauchers von den Mängelrechten ab, [b3]kann sich der "
     "Unternehmer nicht darauf berufen. [b4]Keine Gewährleistung nimmt Dirk alle Mängelrechte. Darauf kann sich Frau "
     "Tillmann nicht berufen. [b5]Nur den Schadensersatz darf ein Händler beschränken, Absatz drei, im Formular aber nur "
     "in den Grenzen der Paragrafen dreihundertsieben bis dreihundertneun. [bpr]Von privat wäre der Ausschluss "
     "grundsätzlich möglich. [b444]Grenze ist dann Paragraf vierhundertvierundvierzig: Arglist oder Garantie.", PS),
    # --- F 3. Negative Beschaffenheitsvereinbarung, § 476 Abs. 1 S. 2 (Wortlaut) ------------------------------------------
    ("[c1]Drittens: Darf der Händler wenigstens vereinbaren, dass der Fernseher schlechter ist als üblich? "
     "[c2]Paragraf vierhundertsechsundsiebzig Absatz eins Satz zwei erlaubt das nur, wenn der Verbraucher vor seiner "
     "Vertragserklärung eigens darauf hingewiesen wurde, dass ein bestimmtes Merkmal abweicht, [c3]und wenn die Abweichung "
     "im Vertrag ausdrücklich und gesondert vereinbart wurde. [c4]Nach der Gesetzesbegründung genügt es nicht, das "
     "neben vielen anderen Klauseln in ein Formular zu schreiben. [c5]Gekauft wie gesehen nennt kein bestimmtes Merkmal "
     "und steht vorgedruckt im Formular. [c6]Der Fernseher muss sich also für die gewöhnliche Verwendung eignen, auch "
     "gebraucht, [c7]und ein Fernseher ohne Bild tut das nicht. [c059]Mehr dazu im Video zum "
     "Sachmangel. [cpr]Von privat ginge eine solche Vereinbarung auch ohne diese Form.", PS),
    # --- G 4. Beweislastumkehr, § 477 Abs. 1 (Wortlaut) ------------------------------------------------------------------
    ("[d1]Viertens: die Beweislastumkehr, Paragraf vierhundertsiebenundsiebzig Absatz eins. [d2]Zeigt sich innerhalb eines Jahres seit Gefahrübergang ein "
     "abweichender Zustand der Ware, wird vermutet, dass sie schon bei Gefahrübergang mangelhaft war, [d3]es sei denn, "
     "das ist mit der Art der Ware oder des Zustands unvereinbar. [d4]Nach dem Bundesgerichtshof muss der Käufer nicht "
     "beweisen, worauf der Defekt beruht. Es genügt, dass sich der mangelhafte Zustand in der Frist zeigt. "
     "[d5]Frau Tillmann müsste das Gegenteil beweisen, etwa einen Bedienungsfehler. [d6]Das Bild fiel nach vier Monaten "
     "aus, also innerhalb eines Jahres. [d7]Der Bundesgerichtshof wendet sie auch auf gebrauchte "
     "Ware an, etwa auf einen Motorroller vom Händler. [dpr]Von privat müsste Dirk selbst beweisen, dass der Mangel "
     "schon bei der Übergabe da war.", PS),
    # --- H 5. Verjährung, § 476 Abs. 2 (Wortlaut) ------------------------------------------------------------------------
    ("[e1]Fünftens: die Verjährung. Mängelansprüche verjähren in der Regel zwei Jahre nach der Ablieferung, Paragraf "
     "vierhundertachtunddreißig. [e2]Beim Händler darf die Frist bei gebrauchten Waren nicht unter ein Jahr verkürzt "
     "werden, Paragraf vierhundertsechsundsiebzig Absatz zwei, [e3]und auch das nur mit eigenem Hinweis und ausdrücklicher, "
     "gesonderter Vereinbarung. [e4]Das Formular erfüllt das nicht. Es bleibt bei zwei Jahren. [epr]Von privat ließe "
     "sich die Frist grundsätzlich auch stärker verkürzen.", PS),
    # --- I 6. Versand, § 475 Abs. 2 (Abgrenzung) -------------------------------------------------------------------------
    ("[f1]Sechstens, nur zur Abgrenzung: Verschickt der Händler die Ware, geht die Gefahr in der Regel erst mit der "
     "Übergabe an den Verbraucher über, Paragraf vierhundertfünfundsiebzig Absatz zwei. [fpr]Von privat geht sie beim "
     "Versendungskauf schon mit der Übergabe an das Transportunternehmen über, Paragraf vierhundertsiebenundvierzig.", PS),
    # --- J Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Ein Verbrauchsgüterkauf liegt vor. [erg2]Auf den Ausschluss kann sich Frau Tillmann nicht berufen, "
     "[erg3]eine wirksame Abweichung fehlt, [erg4]und vermutet wird, dass der Fernseher schon bei der Übergabe mangelhaft "
     "war. [erg5]Dirk kann nach Paragraf vierhundertsiebenunddreißig zuerst Nacherfüllung verlangen, hier die Reparatur. "
     "[v063]Wie es danach weitergeht, zeigt das Video zu den Käuferrechten.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Stelle früh fest, dass ein Verbrauchsgüterkauf vorliegt, [tipp2]und baue die Sonderregeln dort "
     "ein, wo sie wirken: [tipp3]beim Mangel, beim Ausschluss und bei der Verjährung.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Anspruch auf Nacherfüllung: [k1]Römisch eins: Kaufvertrag, [k11]hier ein "
     "Verbrauchsgüterkauf. [k2]Römisch zwei: Sachmangel bei Gefahrübergang, [k21]Abweichung nur nach Paragraf "
     "vierhundertsechsundsiebzig Absatz eins Satz zwei, [k22]Vermutung nach Paragraf vierhundertsiebenundsiebzig. "
     "[k3]Römisch drei: kein wirksamer Ausschluss, Paragraf vierhundertsechsundsiebzig Absatz eins Satz eins. "
     "[k4]Römisch vier: keine Verjährung, Paragraf vierhundertachtunddreißig mit Paragraf vierhundertsechsundsiebzig "
     "Absatz zwei.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim Händler hilft gekauft wie gesehen nicht. [mk2]Abweichen geht nur eigens und gesondert, [mk3]und "
     "im ersten Jahr wird vermutet, dass der Mangel schon bei der Übergabe da war.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
