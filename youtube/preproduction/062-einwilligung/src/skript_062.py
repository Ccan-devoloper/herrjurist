"""Folge 062 · Rechtfertigende Einwilligung: Wann ist Körperverletzung erlaubt? (Mi · Examenswissen · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook: Im Tattoostudio sticht Tätowierer Herr Riedel der siebzehnjährigen Marie ein großes Motiv
(Zweig mit Blüten) auf den Unterarm, mit ihrer Unterschrift, ohne die Eltern zu fragen; er hat ihr Dauer, Schmerz und schwere
Entfernbarkeit erklärt und sticht fachgerecht nach der gebilligten Skizze.
Prüfung: § 223 I (Wortlautkarte; Misshandlung BGH 3 StR 354/16 Rn. 4; Tätowierung OLG Hamm 12 U 151/13 Rn. 4) → § 228
(Wortlautkarte; Einwilligung als Rechtfertigungsgrund, Einverständnis kurz) → 1. Dispositionsbefugnis (§ 216) →
2. Einwilligungsfähigkeit (BGH 1 StR 368/19 Rn. 52, 57 f.; 5 StR 541/17 Rn. 7; Streit Minderjährige) → 3. Erklärung vor der
Tat → 4. keine Willensmängel (BGH 1 StR 585/12 Rn. 7; Umfang OLG Hamm Rn. 4) → 5. subjektives Rechtfertigungselement →
6. § 228 (BGH 2 StR 505/03 Rn. 19, 22, 24, 29; 1 StR 585/12 Rn. 9) → Ergebnis → Abwandlung 14 Jahre → Abwandlung Täuschung
(BGH 1 StR 300/03 Rn. 9) → Ausblick mutmaßliche Einwilligung → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Marie, Riedel.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

# Nur eine Männerstimme im Video (stephan); christian wird nicht verwendet.
STIMMEN = {"Marie": "lucy", "Riedel": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Tattoostudio ---------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag in einem Tattoostudio. [marie]Marie ist siebzehn und wünscht sich seit Monaten ein großes Motiv "
     "auf dem Unterarm: einen Zweig mit Blüten. [skizze]Tätowierer Herr Riedel zeigt ihr die Skizze. [erkl]Er erklärt: "
     "Das Motiv bleibt für immer, das Stechen tut weh, und entfernen lässt es sich nur schwer.", 0.3),
    ("[r1]Wissen deine Eltern Bescheid?", 0.3, "Riedel"),
    ("[m1]Nein. Aber ich bin siebzehn, und es ist mein Arm.", 0.4, "Marie"),
    ("[unter]Marie unterschreibt das Formular. [sticht]Dann sticht Herr Riedel das Motiv fachgerecht nach der Skizze.", 0.3),
    ("[frage]Hat Herr Riedel sich wegen Körperverletzung strafbar gemacht? [frage2]Wann erlaubt eine Einwilligung die "
     "Körperverletzung?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand § 223 ------------------------------------------------------------------------------------------------------
    ("[p223]Zuerst der Tatbestand. Paragraf zweihundertdreiundzwanzig Absatz eins erfasst, wer eine andere Person körperlich "
     "misshandelt oder an der Gesundheit schädigt. "
     "[mh]Körperliche Misshandlung ist eine üble, unangemessene Behandlung, die das körperliche Wohlbefinden oder die "
     "Unversehrtheit nicht nur unerheblich beeinträchtigt. [haut]Die Nadel verletzt die Haut, die Farbe bleibt dauerhaft darin. "
     "[hamm]Auch das Oberlandesgericht Hamm sieht im Stechen einer Tätowierung tatbestandlich eine Körperverletzung. [vors]Herr "
     "Riedel handelt vorsätzlich. Der Tatbestand ist erfüllt.", PS),
    # --- D Rechtswidrigkeit: § 228, Einwilligung und Einverständnis --------------------------------------------------------------
    ("[rw]Fraglich ist die Rechtswidrigkeit. [p228]Paragraf zweihundertachtundzwanzig: Wer eine Körperverletzung mit "
     "Einwilligung der verletzten Person vornimmt, handelt nur dann rechtswidrig, wenn die Tat trotz der Einwilligung gegen "
     "die guten Sitten verstößt. [rf]Die Einwilligung ist hier also ein Rechtfertigungsgrund: Der Tatbestand bleibt, die "
     "Rechtswidrigkeit entfällt. [einv]Anders das Einverständnis: Es schließt schon den Tatbestand aus, wo das Delikt ein "
     "Handeln gegen den Willen voraussetzt, etwa die Wegnahme beim Diebstahl.", PS),
    # --- E 1. Dispositionsbefugnis -----------------------------------------------------------------------------------------------
    ("[disp]Die Voraussetzungen im Einzelnen. Erstens: Marie muss über "
     "das Rechtsgut verfügen dürfen. Ihre körperliche Unversehrtheit ist ein Individualrechtsgut. [leben]Über ihr Leben "
     "dagegen nicht, das zeigt Paragraf zweihundertsechzehn.", P),
    # --- F 2. Einwilligungsfähigkeit ---------------------------------------------------------------------------------------------
    ("[faehig]Zweitens die Einwilligungsfähigkeit. [formel]Nach dem Bundesgerichtshof ist "
     "einwilligungsfähig, wer nach seiner geistigen und sittlichen Reife Bedeutung und Tragweite des Eingriffs erkennen und "
     "sachgerecht beurteilen kann. [streng]Je gewichtiger der Eingriff und je schwerer seine Folgen abzusehen sind, desto "
     "strenger der Maßstab. [alter]Eine feste Altersgrenze gibt es nicht, und auf die Geschäftsfähigkeit kommt es nicht an. "
     "[f15]Bei einem verabredeten Zweikampf hat der Bundesgerichtshof Fünfzehnjährige in der Regel für "
     "einwilligungsfähig gehalten. [mf]Marie ist fast volljährig, hat monatelang überlegt und kennt die Folgen. Sie ist "
     "einwilligungsfähig.", P),
    # --- G Streit: Minderjährige und Eltern --------------------------------------------------------------------------------------
    ("[streit]Umstritten ist, ob bei Minderjährigen zusätzlich die Eltern zustimmen müssen. [colit]Teile der Literatur "
     "verlangen das jedenfalls bei aufschiebbaren, nicht notwendigen Eingriffen mit größeren Risiken. [bgh]Beim "
     "Zweikampf ließ der Bundesgerichtshof die eigene Einwilligung genügen, weil keine ernsthaften Dauerfolgen zu erwarten "
     "waren. [dauer]Ein Tattoo aber bleibt. Ob das auch hier gilt, hat er damit nicht entschieden. "
     "[vertr]Gut vertretbar ist: Bei einer einsichtsfähigen Siebzehnjährigen genügt ihre eigene Einwilligung, denn es geht "
     "um ihren eigenen Körper. [zivil]Ob der Vertrag mit dem Studio ohne die Eltern wirksam ist, ist eine Frage des "
     "Zivilrechts, Paragrafen hundertsieben folgende BGB.", PS),
    # --- H 3. bis 5.: Erklärung, Willensmängel, Kenntnis -------------------------------------------------------------------------
    ("[vorher]Drittens muss die Einwilligung vor der Tat erklärt sein und bis dahin fortbestehen. Marie unterschreibt vor dem "
     "ersten Stich. [wm]Viertens: keine Willensmängel. Marie muss wissen, worauf sie sich einlässt, "
     "und darf nicht getäuscht sein. [aufkl]Herr Riedel hat ihr die Folgen erklärt. [umfang]Die Einwilligung deckt aber nur "
     "ein fachgerechtes Motiv nach der gebilligten Skizze, [genau]und genau das sticht er. [subj]Fünftens das subjektive "
     "Rechtfertigungselement: Herr Riedel handelt in Kenntnis der Einwilligung.", P),
    # --- I 6. Grenze des § 228 ---------------------------------------------------------------------------------------------------
    ("[sitten]Sechstens die Grenze des Paragrafen zweihundertachtundzwanzig. [kern]Der Begriff der guten Sitten ist nach dem "
     "Bundesgerichtshof auf seinen rechtlichen Kern beschränkt. Was einzelne gesellschaftliche Gruppen missbilligen, genügt "
     "nicht. [mass]Maßgeblich sind Art und Gewicht der Verletzung und der Grad der Gefahr für Leib und Leben. [tod]Sittenwidrig "
     "ist die Tat jedenfalls, wenn sie den Einwilligenden in konkrete Todesgefahr bringt. [tat]Ein fachgerecht gestochenes "
     "Tattoo ist kein Eingriff dieses Gewichts. Ob es ihren Eltern gefällt, spielt keine Rolle.", P),
    ("[erg]Ergebnis: Die Einwilligung ist wirksam. Herr Riedel ist nicht strafbar.", PS),
    # --- J Abwandlungen ----------------------------------------------------------------------------------------------------------
    ("[ab1]Abwandlung eins: Marie ist erst vierzehn. [ab1b]Ein großes Motiv begleitet sie ein Leben lang, und diese Folgen kann "
     "sie in diesem Alter kaum absehen. [ab1c]Hier liegt es nahe, die "
     "Einwilligungsfähigkeit zu verneinen. Dann ist die Körperverletzung rechtswidrig.", PS),
    ("[ab2]Abwandlung zwei: Marie zögert, und Herr Riedel lügt.", 0.2),
    ("[r2]Keine Sorge, diese Farbe verblasst nach einem Jahr von selbst.", 0.3, "Riedel"),
    ("[ab2b]Nur deshalb willigt Marie ein. [ab2c]Eine durch Täuschung herbeigeführte Einwilligung ist nach dem "
     "Bundesgerichtshof unwirksam. [ab2d]Herr Riedel macht sich wegen Körperverletzung strafbar.", PS),
    ("[mutm]Ausblick: Kann jemand gar nicht gefragt werden, etwa weil er bewusstlos ist, kommt die mutmaßliche "
     "Einwilligung in Betracht.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Einwilligung prüfst du bei der Körperverletzung in der Rechtswidrigkeit. "
     "[tipp2]Bei Minderjährigen liegt der Schwerpunkt meist bei der Einwilligungsfähigkeit: Alter, Reife und Tragweite des "
     "Eingriffs. [tipp3]Und verwechsle sie nicht mit der Geschäftsfähigkeit.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand. [k2]Römisch zwei: Rechtswidrigkeit, die "
     "Einwilligung. [k2a]Erstens Dispositionsbefugnis, [k2b]zweitens Einwilligungsfähigkeit, [k2c]drittens Erklärung vor der "
     "Tat, [k2d]viertens keine Willensmängel, [k2e]fünftens Handeln in Kenntnis der Einwilligung, [k2f]sechstens kein Verstoß gegen die guten "
     "Sitten. [k3]Römisch drei: Schuld.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Einwilligung rechtfertigt eine Körperverletzung, wenn eine einsichtsfähige Person vor der Tat frei von "
     "Willensmängeln zustimmt. [m2]Auf das Alter allein kommt es nicht an. [m3]Die Grenze ziehen die guten Sitten, gemessen an "
     "der Schwere der Verletzung und ihrer Gefahr.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
