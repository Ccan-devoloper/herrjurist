"""Folge 238 · Soldaten sind Mörder und ACAB: Wie deutet man Äußerungen? (Mo · Der Fall · Grundrechte, Klassiker-Fall).
Fiktiver Rahmen nach den echten Kammerfällen (BVerfG, Beschl. v. 17.5.2016 – 1 BvR 2150/14 [Buchstaben „A C A B !“ im
Fanblock] und 1 BvR 257/14 [Aufdruck auf einer Hose]): Fan Hannes hält mit Freunden im Fanblock an der Brüstung ein Banner mit
dem Kürzel ACAB hoch, Richtung Spielfeld; Polizistin Roth ist am Spielfeldrand im Einsatz und stellt Strafantrag.
Aufbau laut Auftrag: 1. Hook → Frage → Sachverhalt → 2. Art. 5 Abs. 1 S. 1 GG (Wortlautkarte), Meinung (BVerfGE 93, 266
<289>; 1 BvR 2150/14 Rn. 11 f.), Verweis Folge 025 → 3. Deutungsregeln (BVerfGE 93, 266 <295 f.>, DFR Rn. 118–120),
„Soldaten sind Mörder“ (<297–299>, Rn. 124–127) → 4. Kollektivbeleidigung (<299–303>, Rn. 128–137) → 5. ACAB-Kammerbeschlüsse
(1 BvR 2150/14 Rn. 16–18; 1 BvR 257/14 Rn. 16 f.) → 6. Schranken Art. 5 Abs. 2 GG (Wortlautkarte), § 185 StGB (Wortlautkarte),
Wechselwirkung (Verweis Folge 146), § 193 StGB ein Satz → 7. Ergebnis, Gegenfall (1 BvR 257/14 Rn. 17; 1 BvR 1593/16 Rn. 17)
→ 8. Klausurtipp (Lexi), Prüfschema, Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Darstellung: Das Kürzel steht nur auf dem Banner und als Fallbezeichnung auf der Tafel; die Bedeutung wird einmal sachlich
(deutsch) erklärt, nie in Großschrift ausgeschrieben. Polizisten und Fans ohne Klischees, keine Gewalt, keine Vereinsfarben.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Liste, namen_reserviert.txt, Skripte früherer Folgen; 07.10.2026):
Hannes, Roth. Stimmen: Hannes marc (Mann, mittel), Polizistin Roth laura_ruhig (Frau, mittel); william und sabrina nicht
gebraucht. Lexi = Erzählerin Carla.
Sprechtext: Das Kürzel steht als „A.C.A.B.“ (wie synth_el die Gesetzesabkürzungen buchstabiert, z. B. B.G.B.), damit es
Buchstabe für Buchstabe gesprochen wird; Untertitel führen es auf „ACAB“ zurück (meta_238.py).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Roth": "laura_ruhig", "Hannes": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Stadion ------------------------------------------------------------------------------------------------
    ("[fall]Samstagnachmittag, ein Fußballstadion. [block]Im Fanblock steht Hannes mit seinen Freunden. [banner]In der "
     "zweiten Halbzeit halten sie an der Brüstung ein Banner hoch, [kuerzel]darauf das Kürzel A.C.A.B. [bedeut]Es steht für eine englische Parole, auf Deutsch: Alle Polizisten sind Bastarde. [polizei]Am Rand des "
     "Spielfelds sind Polizisten im Einsatz, darunter Polizistin Roth.", P),
    ("[ro1]Das Banner meint doch uns hier. Ich stelle Strafantrag.", P, "Roth"),
    ("[ha1]Das ist meine Meinung über die Polizei. Gemeint ist niemand persönlich.", P, "Hannes"),
    ("[frage]Beleidigt Hannes mit dem Banner die Polizisten vor Ort? [echt]Die Antwort liefern zwei Klassiker aus "
     "Karlsruhe: „Soldaten sind Mörder“ und die Beschlüsse zum Kürzel A.C.A.B.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Art. 5 Abs. 1 S. 1 GG: Meinung ----------------------------------------------------------------------------------
    ("[a5]Ausgangspunkt ist Artikel fünf Absatz eins Satz eins Grundgesetz: [wl5]Jeder hat das Recht, seine Meinung in "
     "Wort, Schrift und Bild frei zu äußern und zu verbreiten. [mein]Meinungen enthalten ein Urteil über Sachverhalte, Ideen "
     "oder Personen. [egal]Geschützt sind sie, ob begründet oder grundlos, emotional oder rational, [form]auch wenn sie "
     "polemisch oder verletzend formuliert sind.", P),
    ("[gleich]Das Kürzel darf man wie die ausgeschriebene Parole behandeln, denn seine Bedeutung ist allgemein bekannt. "
     "[ablehn]Die Parole ist auch nicht inhaltslos: Sie drückt eine allgemeine Ablehnung der Polizei aus, "
     "[meinung]also eine Meinung. [v025]Wie man Meinungen von Tatsachenbehauptungen abgrenzt, zeigt das Video zur Auschwitzlüge. "
     "[eingr]Eine Verurteilung wäre ein Eingriff.", PS),
    # --- D Deutungsregeln (BVerfGE 93, 266 <295 f.>) ------------------------------------------------------------------------
    ("[deut]Doch was bedeutet das Banner überhaupt? [vor]Jede rechtliche Würdigung setzt voraus, dass der Sinn der "
     "Äußerung zutreffend erfasst ist. [obj]Maßgeblich ist der objektive Sinn: [nicht]nicht die Absicht des Äußernden, "
     "[publ]sondern das Verständnis eines unvoreingenommenen und verständigen Publikums. [wort]Auszugehen ist vom Wortlaut. [kont]Doch auch Kontext und erkennbare "
     "Begleitumstände bestimmen den Sinn.", P),
    ("[mehrd]Und bei mehrdeutigen Äußerungen gilt: [verurt]Das Gericht darf nicht die Deutung zugrunde legen, die zur "
     "Verurteilung führt, [ausschl]ohne die anderen möglichen Deutungen mit schlüssigen Gründen auszuschließen. "
     "[fern]Fernliegende Deutungen muss es nicht prüfen.", PS),
    # --- E Soldaten sind Mörder (BVerfGE 93, 266 <297–299>) ----------------------------------------------------------------
    ("[sold]Diese Regeln stehen im Beschluss „Soldaten sind Mörder“ von neunzehnhundertfünfundneunzig. [kriegs]Kriegsgegner "
     "waren verurteilt worden, weil sie Soldaten als Mörder bezeichnet hatten, etwa auf einem Transparent. [schlecht]Die "
     "Äußerungen konnten sich aber gegen Soldatentum und Kriegshandwerk schlechthin richten, nicht gegen einzelne Soldaten. "
     "[uebers]Diese Deutung hatten die Strafgerichte nicht ausgeschlossen.", PS),
    # --- F Kollektivbeleidigung (BVerfGE 93, 266 <299–303>) ---------------------------------------------------------------
    ("[koll]Die zweite Frage: Wen trifft die Äußerung? [samm]Auch eine Äußerung über ein Kollektiv kann die persönliche "
     "Ehre seiner Mitglieder verletzen. [groesse]Aber je größer das Kollektiv, desto schwächer kann die persönliche "
     "Betroffenheit des Einzelnen werden. [skala1]Am einen Ende der Skala steht die Kränkung einer erkennbaren "
     "Einzelperson, [skala2]am anderen die Kritik an sozialen Einrichtungen.", P),
    ("[welt]Alle Soldaten der Welt sind deshalb keine hinreichend überschaubare Gruppe. [bw]Die aktiven Soldaten der "
     "Bundeswehr können es sein. [teil]Wer aber über Soldaten allgemein spricht, meint nicht schon deshalb die Bundeswehr, "
     "weil sie ein Teil davon ist. [umst]Das Gericht muss Umstände benennen, aus denen sich gerade dieser Bezug ergibt.", PS),
    # --- G ACAB-Kammerbeschlüsse (1 BvR 2150/14, 1 BvR 257/14) -------------------------------------------------------------
    ("[acab]Genau das gilt für das Kürzel A.C.A.B. [kammer]Zweitausendsechzehn beanstandete "
     "eine Kammer zwei Verurteilungen wegen Beleidigung, [stadion]in einem Fall um Buchstaben, die Fans im Stadion "
     "hochhielten. [teilg]Dass die Polizisten im Stadion eine Teilgruppe aller Polizisten sind, reicht nicht. "
     "[pers]Nötig ist eine personalisierte Zuordnung zu bestimmten Beamten. [aufent]Und dass Polizei im Stadion ist und die "
     "Parole sehen könnte, genügt dafür nicht.", P),
    ("[kontx]Dort kam der Kontext hinzu: [krit]Kurz vorher hatten die Fans auf Bannern Polizeieinsätze kritisiert, "
     "[uebg]und das hatten die Gerichte nicht gewürdigt.", PS),
    # --- H Schranken: Art. 5 Abs. 2 GG, § 185 StGB, § 193 StGB --------------------------------------------------------------
    ("[schr]Und wo steht das in der Grundrechtsprüfung? [a52]Nach Artikel fünf Absatz zwei findet die Meinungsfreiheit "
     "ihre Schranken unter anderem in den allgemeinen Gesetzen und im Recht der persönlichen Ehre. [p185]Paragraf hundertfünfundachtzig StGB ist ein allgemeines Gesetz. [nur]Er nennt nur die Strafe, "
     "die Beleidigung definiert er nicht. [wechs]Ausgelegt wird er im Licht der Meinungsfreiheit: die Wechselwirkung "
     "aus dem Lüth-Urteil. [ort]Deutung und Personenbezug prüfst du also bei der Anwendung von Paragraf "
     "hundertfünfundachtzig. [p193]Trifft die Äußerung bestimmte Personen, ist nach Paragraf hundertdreiundneunzig, der "
     "Wahrnehmung berechtigter Interessen, im Regelfall zwischen Meinungsfreiheit und Ehre abzuwägen.", PS),
    # --- I Ergebnis im Fall --------------------------------------------------------------------------------------------------
    ("[erg]Zurück ins Stadion. [erg1]Hannes hält das Banner im Fanblock hoch, in Richtung Spielfeld. [erg2]An die "
     "Polizisten wendet er sich nicht. [erg3]Dass sie da sind und das Banner sehen, reicht nicht. [erg4]Eine Beleidigung der Polizisten vor Ort liegt nicht vor. [verl]Eine Verurteilung "
     "würde Hannes in seiner Meinungsfreiheit verletzen.", PS),
    # --- J Gegenfall ---------------------------------------------------------------------------------------------------------
    ("[gegen]Anders im Gegenfall: [gg1]Nach dem Spiel geht Hannes mit dem Banner gezielt zu einer Gruppe von Polizisten "
     "und hält es direkt vor ihnen hoch.", 0.2),
    ("[ro2]Jetzt sind wirklich wir gemeint.", P, "Roth"),
    ("[gg2]Er hat sich bewusst in ihre Nähe begeben, um gerade sie mit der Parole zu konfrontieren. [gg3]Die "
     "Äußerung ist auf diese Beamten bezogen. [gg4]Eine Beleidigung kommt dann in Betracht, nach Abwägung bei Paragraf "
     "hundertdreiundneunzig.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: [t1]Ermittle bei Äußerungsdelikten zuerst den Sinn, mit Kontext und allen nicht fernliegenden "
     "Deutungen. [t2]Bei Sammelbezeichnungen fragst du dann: Gibt es eine personalisierte Zuordnung zu bestimmten Personen? "
     "[t3]Und nimm Schmähkritik nicht vorschnell an: Auch sie setzt diese Zuordnung voraus.", PS),
    # --- L Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema gegen eine Verurteilung wegen einer Äußerung. [k1]Römisch eins: Schutzbereich, die "
     "Meinung. [k2]Römisch zwei: Eingriff durch die Verurteilung. [k3]Römisch drei: Rechtfertigung. [k3a]Erstens: Paragraf "
     "hundertfünfundachtzig als Schranke. [k3b]Zweitens: verfassungsgemäße Anwendung, [k3c]mit dem Sinn der Äußerung, "
     "[k3d]dem Bezug auf bestimmte Personen [k3e]und der Abwägung bei Paragraf hundertdreiundneunzig.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst den Sinn ermitteln, dann strafen. [m2]Und eine Parole über alle Polizisten trifft die Beamten "
     "vor Ort nur, wenn besondere Umstände sie gerade auf sie beziehen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
