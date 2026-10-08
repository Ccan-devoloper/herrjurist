"""Folge 274 · Gebietserhaltungsanspruch: Flüchtlingsunterkunft im Gewerbegebiet? (Mo · Der Fall · Baurecht · Klassiker-Fall).
Übungsfall nach dem Plan-Hook („Im Gewerbegebiet soll eine Unterkunft für 300 Geflüchtete entstehen – ein Handwerksbetrieb
fürchtet Einschränkungen“), angelehnt an die Konstellation von BVerwG, Beschl. v. 27.02.2018 – 4 B 39.17 (Bürogebäude im
Gewerbegebiet wird Gemeinschaftsunterkunft; Klage eines Eigentümers im Gewerbegebiet erfolglos):
Ein qualifizierter Bebauungsplan setzt ein Gewerbegebiet fest (§ 8 BauNVO, Ausnahmen nach Abs. 3 nicht ausgeschlossen).
Frau Hollenberg führt dort eine Schreinerei (Sägen ab 6 Uhr, Lieferverkehr). Der Eigentümer des leeren Bürogebäudes nebenan
will es zur Gemeinschaftsunterkunft für 300 Geflüchtete umbauen und an die Stadt vermieten. Die Bauaufsichtsbehörde (Herr
Kerkhoff) genehmigt die Nutzungsänderung mit einer Befreiung nach § 246 Abs. 10 BauGB; die Stadt hat dargelegt, dass sie die
Plätze dringend braucht und kein anderes Gebäude rechtzeitig frei ist (§ 246 Abs. 13a). Lärmgutachten: Mit
Schallschutzfenstern ist der Betriebslärm an der Unterkunft zumutbar; die Schreinerei muss nichts ändern. Frau Hollenberg klagt.
Aufbau: 1. Klagebefugnis über den Gebietserhaltungsanspruch (BVerwGE 94, 151; 4 C 6.20 Rn. 8) → 2. § 8 BauNVO
(Wortlautkarte Abs. 1, Abs. 3 Nr. 2), Gebietsverträglichkeit, Wohnähnlichkeit (4 C 14.10 Rn. 16 f.; 4 B 86.01; 4 B 39.17
Rn. 11) → 3. § 246 Abs. 10 BauGB (Wortlautkarte), Abs. 13a, 17, 12 → 4. Rücksichtnahme, § 15 Abs. 1 S. 2 BauNVO → Ergebnis
→ Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Darstellung: sachlich und respektvoll; Geflüchtete nie als Bedrohung, keine Figuren oder Gesichter in Gruppen, die Unterkunft
nur als Gebäude; Frau Hollenberg argumentiert mit Lärm- und Betriebsschutz.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Liste, namen_reserviert.txt, Volltextsuche 08.10.2026):
Hollenberg, Kerkhoff (nie im Genitiv mit -s). Stimmen aus dem Pool (william, sabrina, marc, laura_ruhig): Frau Hollenberg
laura_ruhig (Frau, mittel), Herr Kerkhoff william (Mann, älter); sabrina und marc nicht verwendet (in 268 zuletzt).
Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hollenberg": "laura_ruhig", "Kerkhoff": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Gewerbegebiet, Schreinerei, Bürogebäude, Genehmigung ------------------------------------------------------
    ("[fall]Am Stadtrand liegt ein Gewerbegebiet mit Bebauungsplan. [werk]Dort führt Frau Hollenberg eine Schreinerei. "
     "[saege]Ab sechs Uhr morgens laufen die Sägen, Lieferwagen fahren an und ab. [buero]Nebenan steht ein leeres "
     "Bürogebäude. [heim]Der Eigentümer will es zu einer Gemeinschaftsunterkunft für dreihundert Geflüchtete umbauen und an "
     "die Stadt vermieten. [genehm]Die Bauaufsichtsbehörde genehmigt die neue Nutzung. Herr Kerkhoff leitet dort die "
     "Bauaufsicht.", P),
    ("[ke1]Die Stadt braucht die Plätze dringend, und kein anderes Gebäude wird rechtzeitig frei. Deshalb erteilen wir eine "
     "Befreiung.", P, "Kerkhoff"),
    ("[ho1]Gegen die Menschen habe ich nichts. Aber wenn nebenan Schlafräume sind, bekomme ich bald Auflagen für meine "
     "Maschinen.", P, "Hollenberg"),
    ("[klage]Frau Hollenberg klagt gegen die Genehmigung. [frage]Kann ein Betrieb die Unterkunft im Gewerbegebiet "
     "verhindern, [frage2]auch wenn er gar nicht nachweisen kann, dass er gestört wird?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Klagebefugnis: Gebietserhaltungsanspruch ------------------------------------------------------------------------
    ("[kb]Erstens, die Klagebefugnis. Frau Hollenberg braucht eine Norm, die auch sie schützt. [v113]Wie du das prüfst, "
     "zeigt unser Video zur Nachbarklage. [gea]Hier hilft ihr der Gebietserhaltungsanspruch. [tausch]Wer im Plangebiet ein Grundstück hat, muss die festgesetzte Art der Nutzung "
     "hinnehmen. Dafür müssen es alle anderen auch. [schick]Das Bundesverwaltungsgericht spricht von einer rechtlichen "
     "Schicksalsgemeinschaft. [urt93]Grundlegend ist sein Urteil von neunzehnhundertdreiundneunzig.", P),
    ("[abwehr]Deshalb kann jeder Eigentümer im Baugebiet eine gebietsfremde Nutzung abwehren, [unabh]und zwar unabhängig "
     "davon, ob sie ihn tatsächlich beeinträchtigt. [beweis]Frau Hollenberg muss also nicht beweisen, dass ihre Schreinerei "
     "eingeschränkt wird. [grenze]Der Anspruch gilt aber nur innerhalb desselben Baugebiets.", PS),
    # --- D 2. § 8 BauNVO: Ausnahme, Gebietsverträglichkeit, Wohnähnlichkeit ---------------------------------------------------
    ("[p8]Zweitens: Ist die Unterkunft hier gebietsfremd? [p8a]Paragraf acht Absatz eins der Baunutzungsverordnung: "
     "Gewerbegebiete dienen vorwiegend der Unterbringung von nicht erheblich belästigenden Gewerbebetrieben. [p8b]Nach "
     "Absatz drei Nummer zwei können Anlagen für soziale Zwecke ausnahmsweise zugelassen werden. [sozial]Eine "
     "Gemeinschaftsunterkunft kommt als solche Anlage in Betracht.", P),
    ("[gv]Aber auch eine Ausnahme muss mit dem Zweck des Gebiets verträglich sein. [nwohn]Im Gewerbegebiet soll nicht "
     "gewohnt werden. [pflege]Wohnähnliche Nutzungen, etwa ein Pflegeheim, sind dort typischerweise unzulässig. "
     "[monate]Eine Unterkunft, in der Menschen über Monate schlafen, essen und leben, ist wohnähnlich. [rspr]Viele Gerichte "
     "hielten solche Unterkünfte deshalb im Gewerbegebiet für unzulässig, auch als Ausnahme. [b31]Und eine normale "
     "Befreiung verlangt, dass die Grundzüge der Planung nicht berührt werden. "
     "[gut]Nach diesen Regeln hätte Frau Hollenberg gute Chancen.", PS),
    # --- E 3. § 246 Abs. 10 BauGB (Wortlautkarte), Abs. 13a, 17, 12 ------------------------------------------------------------
    ("[p246]Drittens: Für Flüchtlingsunterkünfte enthält Paragraf zweihundertsechsundvierzig des Baugesetzbuchs befristete "
     "Sonderregeln. [w10]Nach Absatz zehn kann bis Ende zweitausendsiebenundzwanzig in Gewerbegebieten für Unterkünfte für "
     "Flüchtlinge befreit werden, [w10b]wenn an dem Standort Anlagen für soziale Zwecke als Ausnahme zugelassen werden "
     "können [w10c]und die Abweichung auch unter Würdigung nachbarlicher Interessen mit öffentlichen Belangen vereinbar "
     "ist.", P),
    ("[stand]Hier schließt der Bebauungsplan soziale Anlagen als Ausnahme nicht aus. Das genügt. [zweck]Die Unterkunft "
     "muss nicht zum Zweck des Gewerbegebiets passen. [bv18]So sah es das Bundesverwaltungsgericht zweitausendachtzehn in "
     "einem ähnlichen Fall: Das Gesetz schränkt hier den Gebietserhaltungsanspruch ein. [gzp]Und anders als bei der "
     "normalen Befreiung kommt es auf die Grundzüge der Planung nicht an.", P),
    ("[dring]Zwei Grenzen hat die Regel. Nach Absatz dreizehn a gilt sie nur, soweit dringend benötigte Unterkünfte in "
     "der Gemeinde sonst nicht oder nicht rechtzeitig bereitgestellt werden können. Das hat die Stadt dargelegt. [frist]Und die Frist betrifft nach "
     "Absatz siebzehn nur das Zulassungsverfahren. Die Genehmigung selbst muss nicht befristet werden.", PS),
    # --- F 4. Rücksichtnahme, § 15 Abs. 1 S. 2 BauNVO ----------------------------------------------------------------------------
    ("[rueck]Viertens, die Rücksichtnahme. Hinter der Würdigung nachbarlicher Interessen steht dasselbe Gebot wie in "
     "Paragraf fünfzehn Absatz eins der Baunutzungsverordnung. [p15]Danach ist eine Anlage auch unzulässig, wenn sie "
     "unzumutbaren Belästigungen oder Störungen ausgesetzt wird. [heran]Das ist der Einwand von Frau Hollenberg: Wer an einen "
     "Betrieb heranrückt, muss dessen zulässigen Lärm aushalten können. [gutacht]Ein Lärmgutachten zeigt: An der Unterkunft "
     "hält die Schreinerei die Werte für ein Gewerbegebiet ein. Sie muss nichts ändern.", PS),
    # --- G Ergebnis ------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Befreiung ist rechtmäßig, die Klage ist unbegründet. [erg2]Der Gebietserhaltungsanspruch hilft "
     "Frau Hollenberg hier nicht, weil Absatz zehn die Unterkunft in diesem Gewerbegebiet möglich macht.", P),
    ("[ho2]Dann bleibt meine Werkstatt, wie sie ist. Das war mir das Wichtigste.", PS, "Hollenberg"),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe in zwei Stufen. [k1]Erst Paragraf acht mit Ausnahme und Gebietsverträglichkeit, [k2]dann "
     "Paragraf zweihundertsechsundvierzig Absatz zehn als Befreiung. [k3]Achte auf das Datum: Nach Ende "
     "zweitausendsiebenundzwanzig darf die Behörde Absatz zehn nach heutigem Stand nicht mehr anwenden. "
     "[k4]Und argumentiere mit städtebaulichen Belangen wie Lärm und Verkehr. Gefahren, die man aus persönlichen "
     "Eigenschaften der Bewohner ableitet, sind in der Regel kein städtebaulicher Gesichtspunkt.", PS),
    # --- I Schema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zur Nachbarklage gegen die Unterkunft. [s1]Eins, die Klagebefugnis über den "
     "Gebietserhaltungsanspruch. [s2]Zwei, die Begründetheit. [s2a]Nach Paragraf acht ist die wohnähnliche Unterkunft "
     "weder allgemein noch als Ausnahme zulässig. [s2b]Aber Absatz zehn erlaubt die Befreiung: Standort und Rücksichtnahme. "
     "[s2c]Dazu die Grenzen: Dringlichkeit und Frist. [s3]Drei, das Ergebnis: keine Rechtsverletzung, die Klage ist "
     "unbegründet.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Baugebiet bilden die Eigentümer eine Schicksalsgemeinschaft. [m2]Jeder kann eine gebietsfremde "
     "Nutzung abwehren, auch ohne gestört zu sein. [m3]Für Flüchtlingsunterkünfte öffnet Paragraf zweihundertsechsundvierzig "
     "Absatz zehn das Gewerbegebiet aber, befristet bis Ende zweitausendsiebenundzwanzig.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
