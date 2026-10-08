"""Folge 282 · Sofortiges Anerkenntnis § 93 ZPO: Verlieren ohne Kosten (Fr · 2. Examen · ZPO · Format Zweckmäßigkeit).
Beispielfall nach dem Plan-Hook: Herr Fink (Gartenbau Fink GmbH, erfunden) hat bei Frau Mehlhorn die Hecke geschnitten und ein
Beet angelegt; Rechnung 1.280 €. Zwei Wochen später, ohne Mahnung und ohne Anruf, reicht die Firma Klage beim Amtsgericht ein.
Frau Mehlhorn will einfach zahlen und geht zu Rechtsanwalt Rosenbaum (Beklagtenvertreter).
Aufbau (Zweckmäßigkeit/Beklagtenklausur laut Auftrag): 1. Hook → 2. Problem: zahlen oder anerkennen? (Zahlung nach
Rechtshängigkeit → Erledigung, § 91a ZPO, ein Satz) → 3. § 307 ZPO (Wortlautkarte): Anerkenntnisurteil → 4. § 93 ZPO
(Wortlautkarte): (a) keine Veranlassung – Verhalten vor dem Prozess (BGH VI ZB 64/05 Rn. 10 f.; V ZB 93/13 Rn. 19), kein
Verzug (§ 286 BGB); (b) „sofort“ – schriftliches Vorverfahren, Klageerwiderungsfrist, Verteidigungsanzeige ohne
Abweisungsantrag schadet nicht (BGH VI ZB 64/05 Rn. 22; IX ZB 54/18 Rn. 7 f.) → 5. Muster: Tenor Anerkenntnisurteil (§ 313b
Abs. 1 S. 2, § 93, § 708 Nr. 1 ZPO), Teilanerkenntnis (Teil-Anerkenntnisurteil, Kosten im Schlussurteil) → 6. zwei typische
Fehler → 7. Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung „282: Mehlhorn, Rosenbaum, Fink“); nie im Genitiv.
Stimmen (Pool niklas, helmut, ela_froh, julia): Frau Mehlhorn julia (Frau, jung), Herr Rosenbaum niklas (Mann, jung),
Herr Fink helmut (Mann, älter); ela_froh nicht gebraucht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Mehlhorn": "julia", "Rosenbaum": "niklas", "Fink": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Gartenbau Fink und Frau Mehlhorn ------------------------------------------------------------------------
    ("[fall]Ein Gartenbaubetrieb. [fink]Herr Fink hat bei Frau Mehlhorn die Hecke geschnitten und ein Beet angelegt. "
     "[rechnung]Seine Rechnung: tausendzweihundertachtzig Euro. [frist]Zwei Wochen später ist das Geld noch nicht da.", P),
    ("[fi1]Keine Zahlung? Dann gleich zum Amtsgericht.", P, "Fink"),
    ("[post]Ohne Mahnung, ohne Anruf: [klage]Frau Mehlhorn bekommt die Klage zugestellt.", P),
    ("[me1]Eine Klage? Mich hat niemand gemahnt. Ich zahle die Rechnung doch einfach.", P, "Mehlhorn"),
    ("[kanzlei]Sie geht zu Rechtsanwalt Rosenbaum.", P),
    ("[ro1]Langsam. Erst klären wir, wer die Kosten trägt.", PS, "Rosenbaum"),
    ("[hook]Den Prozess verlieren und trotzdem keine Kosten tragen? [frage]Wann ist ein Anerkenntnis sofort, "
     "[frage2]wann gab die Beklagte keine Veranlassung zur Klage, [frage3]und wie sieht der Tenor aus?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Problem: zahlen oder anerkennen? ------------------------------------------------------------------------------
    ("[zahl]Erste Idee: einfach zahlen. [zahl2]Nach der Zustellung erklären die Parteien den Rechtsstreit dann "
     "typischerweise für erledigt, [zahl3]und das Gericht entscheidet über die Kosten nach Paragraf einundneunzig a, nach "
     "billigem Ermessen. [direkt]Direkter ist das Anerkenntnis.", P),
    # --- D § 307 ZPO -----------------------------------------------------------------------------------------------------
    ("[w307]Paragraf dreihundertsieben ZPO: [w307b]Erkennt eine Partei den gegen sie geltend gemachten Anspruch ganz oder "
     "zum Teil an, so ist sie dem Anerkenntnis gemäß zu verurteilen. [ohne]Einer mündlichen Verhandlung bedarf es insoweit "
     "nicht. [verl]Frau Mehlhorn verliert also den Prozess, durch Anerkenntnisurteil. [k91]Nach Paragraf einundneunzig "
     "trägt die unterliegende Partei die Kosten. [ausn]Doch dafür gibt es eine Ausnahme.", P),
    # --- E § 93 ZPO ------------------------------------------------------------------------------------------------------
    ("[w93]Paragraf dreiundneunzig ZPO: [w93b]Hat der Beklagte nicht durch sein Verhalten zur Erhebung der Klage "
     "Veranlassung gegeben, so fallen dem Kläger die Prozesskosten zur Last, wenn der Beklagte den Anspruch sofort "
     "anerkennt. [zwei]Zwei Voraussetzungen also: keine Veranlassung, und sofort anerkannt.", P),
    ("[ver]Erstens, die Veranlassung. [ver1]Veranlassung gibt, wessen Verhalten vor dem Prozess dem Kläger vernünftigerweise "
     "Grund zur Annahme bietet, er komme ohne Gericht nicht zu seinem Recht. [ver2]Typisch ist eine fällige Leistung, die trotz "
     "Aufforderung ausbleibt. [ver3]Hier gab es eine Rechnung, aber keine Mahnung und keinen Anruf. [verzug]Verzug lag "
     "auch nicht vor: keine Mahnung, und dreißig Tage nach der Rechnung waren noch nicht um. [keine]Also keine "
     "Veranlassung.", P),
    ("[me2]Ich hätte sofort gezahlt.", PS, "Mehlhorn"),
    ("[sof]Zweitens, sofort. [sof2]Das Gericht hat das schriftliche Vorverfahren angeordnet: [fr1]zwei Wochen, um die "
     "Verteidigung anzuzeigen, [fr2]dann mindestens zwei weitere Wochen für die Klageerwiderung. [sof3]Sofort heißt hier: "
     "innerhalb der Klageerwiderungsfrist. [vert]Eine Verteidigungsanzeige schadet nicht, solange sie keinen Antrag auf "
     "Klageabweisung ankündigt und den Anspruch nicht bestreitet. [bgh]So der Bundesgerichtshof seit "
     "zweitausendsechs.", P),
    ("[ro2]Wir zeigen nur die Verteidigung an und erkennen in der Klageerwiderung an.", P, "Rosenbaum"),
    ("[erg]Ergebnis: Frau Mehlhorn wird verurteilt, [erg2]aber die Kosten trägt die Gartenbaufirma.", PS),
    # --- F Muster: Tenor, Teilanerkenntnis ------------------------------------------------------------------------------
    ("[ten]So sieht der Tenor aus. [ten0]Überschrift: Anerkenntnisurteil. [ten1]Erstens: Die Beklagte wird verurteilt, an "
     "die Klägerin tausendzweihundertachtzig Euro zu zahlen. [ten2]Zweitens: Die Klägerin trägt die Kosten des "
     "Rechtsstreits. [ten3]Drittens: Das Urteil ist vorläufig vollstreckbar, [ten4]ohne Sicherheitsleistung, nach "
     "Paragraf siebenhundertacht Nummer eins ZPO.", P),
    ("[teil]Abwandlung: Dreihundert Euro der Rechnung sind für Rasenmähen, und gemäht wurde nie. [teil2]Dann erkennt Frau "
     "Mehlhorn nur neunhundertachtzig Euro an. [teil3]Darüber ergeht ein Teil-Anerkenntnisurteil, [teil4]über den Rest "
     "wird gestritten. [teil5]Die Kostenentscheidung bleibt in der Regel dem Schlussurteil vorbehalten. [teil6]Dort entscheidet das "
     "Gericht einheitlich: [teil7]Paragraf dreiundneunzig für den anerkannten Teil, [teil8]für den Rest das Ergebnis "
     "des Streits.", PS),
    # --- G Zwei typische Fehler -----------------------------------------------------------------------------------------
    ("[fehl]Zwei typische Fehler. [f1]Erstens: in der Verteidigungsanzeige Klageabweisung ankündigen und erst später "
     "anerkennen. [f1b]Dann ist das Anerkenntnis regelmäßig nicht mehr sofort, und die Kosten trägt die Beklagte. "
     "[f2]Zweitens im Tenor: beim Anerkenntnisurteil eine Sicherheitsleistung oder Abwendungsbefugnis aussprechen. [f2b]Paragraf "
     "siebenhundertelf gilt nur für die Nummern vier bis elf von Paragraf siebenhundertacht.", PS),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp für die Anwaltsklausur: [tipp2]Ist die Forderung berechtigt, prüfe vor jeder Verteidigung "
     "Paragraf dreiundneunzig. [tipp3]Im Schriftsatz steht dann: Die Beklagte erkennt den Klageanspruch an. [tipp4]Dazu "
     "der Antrag, die Kosten der Klägerin aufzuerlegen, [tipp5]und warum es keine Veranlassung zur Klage gab.", PS),
    # --- I Prüfschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Anerkenntnis, ganz oder zum Teil, Paragraf dreihundertsieben. [k2]Römisch "
     "zwei: keine Veranlassung zur Klage, [k2a]also das Verhalten vor dem Prozess. [k3]Römisch drei: sofort, [k3a]im "
     "schriftlichen Vorverfahren innerhalb der Klageerwiderungsfrist, ohne Abweisungsantrag. [k4]Römisch vier: der Tenor, "
     "[k4a]Kosten beim Kläger, vorläufig vollstreckbar nach Paragraf siebenhundertacht Nummer eins.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer ohne Anlass verklagt wird und sofort anerkennt, verliert den Prozess, [m2]aber die Kosten trägt "
     "der Kläger.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
