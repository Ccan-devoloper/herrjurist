"""Folge 111 · Räuberischer Diebstahl § 252 StGB: Gewalt auf der Flucht (Fr · Klausurpraxis · StGB BT, Format Schema).
Fall nach dem Plan-Hook: Gottfried steckt im Elektromarkt Kopfhörer (129 €) ein, geht ohne zu bezahlen hinaus; vor dem
Eingang stellt ihn Mitarbeiterin Edda, greift nach seiner Jacke; er stößt sie weg, damit sie ihm die Kopfhörer nicht
abnimmt, ruft „Die Kopfhörer behalte ich!“ und rennt mit ihnen davon. Edda bleibt unverletzt (keine Körperverletzung).
Aufbau: Wortlaut § 252 → 1. Vortat: vollendeter, nicht beendeter Diebstahl (Einstecken, Verweis auf Folge 055; BGH 3 StR
556/09 Rn. 11 f.; 5 StR 395/14 Rn. 6), Abgrenzung § 249 (BGH 3 StR 52/02 Rn. 16; BGHSt 26, 95) → 2. auf frischer Tat
betroffen (BGH 4 StR 451/22 Rn. 7; 5 StR 395/14 Rn. 7; 3 StR 112/15 Rn. 5; Zuvorkommen: BGHSt 26, 95, 96) → 3. Gewalt
gegen eine Person (BGH 1 StR 47/02 Rn. 6; 3 StR 392/22 Rn. 8) → 4. Vorsatz (3 StR 112/15 Rn. 7), Besitzerhaltungsabsicht
(BGH 1 StR 389/14 Rn. 11; 3 StR 392/22 Rn. 8) → Ergebnis, Rechtsfolge „gleich einem Räuber“ (§§ 250, 251: 3 StR 392/22
Rn. 8; 3 StR 52/02 Rn. 16), Konkurrenz (1 StR 378/12 Rn. 9) → Gegenvariante (Beute weggeworfen) → Klausurtipp
(1 StR 389/14 Rn. 12, 15) → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Gottfried, Edda. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.5

STIMMEN = {"Gottfried": "william", "Edda": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ------------------------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag im Elektromarkt. [gott]Gottfried nimmt Kopfhörer für hundertneunundzwanzig Euro aus dem Regal "
     "[steckt]und steckt sie in die Innentasche seiner Jacke. [edda]Mitarbeiterin Edda hat das gesehen. [kasse]Gottfried "
     "geht an der Kasse vorbei, ohne zu bezahlen, und verlässt den Markt. [drauss]Direkt vor dem Eingang holt Edda ihn ein.",
     0.3),
    ("[e1]Halt! Die Kopfhörer in Ihrer Jacke gehören uns!", 0.3, "Edda"),
    ("[greift]Sie greift nach seiner Jacke. [stoss]Gottfried stößt sie weg, damit sie ihm die Kopfhörer nicht abnimmt.", 0.2),
    ("[g1]Die Kopfhörer behalte ich!", 0.3, "Gottfried"),
    ("[rennt]Dann rennt er mit ihnen davon. [taumelt]Edda taumelt zurück, verletzt ist sie nicht. [frage]Ist Gottfried "
     "jetzt ein Räuber? [frage2]Wir prüfen den räuberischen Diebstahl, Paragraf zweihundertzweiundfünfzig, mit einer "
     "Gegenvariante.", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 252 und Aufbau -----------------------------------------------------------------------------------------
    ("[p252]Paragraf zweihundertzweiundfünfzig: [p252w]Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine "
     "Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des "
     "gestohlenen Gutes zu erhalten, ist gleich einem Räuber zu bestrafen. [aufbau]Du prüfst also vier Punkte: [auf1]die "
     "Vortat, einen Diebstahl, [auf2]das Betreffen auf frischer Tat, [auf3]das Nötigungsmittel [auf4]und subjektiv "
     "Vorsatz und Besitzerhaltungsabsicht.", PS),
    # --- D Vortat und Abgrenzung zum Raub ------------------------------------------------------------------------------------
    ("[vt]Erstens: die Vortat. Der Diebstahl muss vollendet sein. [vt2]Gottfried hat die Kopfhörer eingesteckt und damit "
     "schon im Laden eigenen Gewahrsam begründet, wie in unserer Folge zur Gewahrsamsenklave. [vt3]Dass Edda zusieht, ändert "
     "daran nichts. Der Diebstahl ist vollendet. [vt4]Beendet ist er aber noch nicht: Edda ist ihm direkt auf den Fersen, "
     "die Beute ist noch nicht gesichert. [p249]Und warum kein Raub? [p249b]Beim Raub setzt der Täter die Gewalt ein, um "
     "wegzunehmen. Gottfried stößt erst nach der vollendeten Wegnahme. [p249c]Diese Phase zwischen Vollendung und "
     "Beendigung erfasst Paragraf zweihundertzweiundfünfzig.", PS),
    # --- E Auf frischer Tat betroffen ----------------------------------------------------------------------------------------
    ("[ft]Zweitens: bei dem Diebstahl auf frischer Tat betroffen. [ft2]Frisch ist die Tat, solange ein enger räumlicher und "
     "zeitlicher Zusammenhang besteht: Der Täter wird noch in unmittelbarer Nähe zum Tatort und alsbald nach der Tat "
     "wahrgenommen. [ft3]Edda stellt Gottfried direkt vor dem Eingang, gleich nach der Tat. Er ist auf frischer Tat "
     "betroffen. [ft4]Dass sie ihn schon im Laden beobachtet hat, schadet nicht. [zuvor]Umstritten ist, ob auch "
     "betroffen ist, wer der Entdeckung durch schnelles Zuschlagen zuvorkommt. Der Bundesgerichtshof bejaht das.", PS),
    # --- F Nötigungsmittel ---------------------------------------------------------------------------------------------------
    ("[nm]Drittens: das Nötigungsmittel. Wie beim Raub verlangt das Gesetz Gewalt gegen eine Person oder eine Drohung mit "
     "gegenwärtiger Gefahr für Leib oder Leben. [nm2]Dafür genügt eine Einwirkung auf den Körper des anderen, die geeignet "
     "ist und nach dem Willen des Täters dazu dient, Widerstand zu verhindern. [nm3]Gottfried stößt Edda weg, als sie nach seiner Jacke greift. "
     "[nm4]Der Bundesgerichtshof hat schon das Wegschubsen eines Ladendetektivs als Gewalt gewertet. [nm5]Das "
     "Nötigungsmittel liegt vor.", PS),
    # --- G Subjektiver Tatbestand --------------------------------------------------------------------------------------------
    ("[subj]Viertens, subjektiv: [vors]Gottfried braucht Vorsatz, auch dafür, dass er betroffen ist. [bea]Dazu kommt die "
     "Besitzerhaltungsabsicht: Er muss die Gewalt einsetzen, um sich im Besitz der Beute zu erhalten. [bea2]Das muss nicht "
     "sein einziges Motiv sein. Dass er auch fliehen will, schadet also nicht. [bea3]Bloße Fluchtabsicht genügt aber nicht. "
     "[bea4]Gottfried stößt Edda weg, damit sie ihm die Kopfhörer nicht abnimmt, und ruft, dass er sie behält. "
     "[bea5]Die Besitzerhaltungsabsicht liegt vor.", PS),
    # --- H Ergebnis, Rechtsfolge, Konkurrenzen -------------------------------------------------------------------------------
    ("[rs]Rechtswidrigkeit und Schuld liegen vor. [erg]Gottfried hat einen räuberischen Diebstahl begangen. [folge]Er wird "
     "gleich einem Räuber bestraft: mit dem Strafrahmen des Raubes, [qual]und auch die Qualifikationen der Paragrafen "
     "zweihundertfünfzig und zweihunderteinundfünfzig sind anwendbar. [konk]Der Diebstahl tritt dahinter zurück.", PS),
    # --- I Gegenvariante -----------------------------------------------------------------------------------------------------
    ("[gv]Gegenvariante: Gottfried wirft die Kopfhörer weg und stößt Edda nur, um zu entkommen. [gv2]Dann fehlt die "
     "Besitzerhaltungsabsicht, also kein räuberischer Diebstahl. [gv3]Es bleibt beim Diebstahl, den Stoß prüfst du "
     "gesondert.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Besitzerhaltungsabsicht ist oft der Knackpunkt. [tipp2]Dass der Täter mit der Beute flieht, "
     "beweist sie allein nicht. [tipp3]Suche im Sachverhalt, ob es ihm gerade auf die Beute ankam, [tipp4]etwa weil er sie "
     "gegen einen Zugriff verteidigt oder ausdrücklich behalten will.", PS),
    # --- K Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s_i]Römisch eins: Tatbestand. [s1]Eins: die Vortat, ein vollendeter, nicht beendeter "
     "Diebstahl. [s2]Zwei: bei dem Diebstahl auf frischer Tat betroffen. [s3]Drei: Gewalt gegen eine Person oder Drohung "
     "mit gegenwärtiger Gefahr für Leib oder Leben. [s4]Vier, subjektiv: Vorsatz [s5]und Besitzerhaltungsabsicht. "
     "[s_ii]Römisch zwei: Rechtswidrigkeit. [s_iii]Römisch drei: Schuld. [s_iv]Danach die Rechtsfolge: gleich einem Räuber, "
     "wenn nötig mit den Paragrafen zweihundertfünfzig und zweihunderteinundfünfzig.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nach vollendetem Diebstahl auf frischer Tat betroffen wird und Gewalt einsetzt, um die Beute zu "
     "behalten, wird gleich einem Räuber bestraft. [m_2]Wer nur fliehen will, begeht keinen räuberischen Diebstahl.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
