"""Folge 089 · Abtretung § 398 BGB: Voraussetzungen und Schuldnerschutz (Mi · Examenswissen · Zivilrecht/Schuldrecht AT,
Format Schema). Beispielfall nach dem Plan-Hook („Dein Handwerker verkauft seine offene Rechnung an ein Inkassobüro“):
Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen (Werklohn 2.400 €, abgenommen). Er verkauft die Forderung an ein
Inkassobüro (Sachbearbeiter Sven) und tritt sie ab. Tanja weiß davon nichts und überweist die 2.400 € an Ewald; danach
verlangt das Inkassobüro Zahlung. Wortlautkarten § 398 BGB und § 407 Abs. 1 BGB. Voraussetzungen: Abtretungsvertrag,
Bestehen der Forderung (§ 405 ein Satz), Bestimmbarkeit (BGH VIII ZR 130/19 Rn. 81), kein Ausschluss (§ 399, § 354a HGB,
§ 400), Abstraktion (Forderungskauf § 453). Rechtsfolge § 398 S. 2, § 401. Schuldnerschutz §§ 404, 406, 407 I
(BGH VII ZR 13/20 Rn. 35), 409, 410. Ergebnis: Tanja frei, Inkassobüro gegen Ewald aus § 816 II. Klausurtipp und Merksatz
mit Lexi. Figuren: Ewald (helmut), Sven (niklas), Tanja (julia); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ewald": "helmut", "Sven": "niklas", "Tanja": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Auftrag -----------------------------------------------------------------------------------------
    ("[fall]Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen. [rech]Die Arbeit ist abgenommen, seine Rechnung "
     "lautet auf zweitausendvierhundert Euro.", 0.3),
    # --- A2 Fall: der Verkauf der Rechnung ----------------------------------------------------------------------------
    ("[verk]Ewald braucht schnell Geld. Er verkauft die offene Rechnung an ein Inkassobüro. [sven]Sven schließt den "
     "Vertrag für das Büro.", 0.25),
    ("[hu1]Die Forderung gegen Tanja über zweitausendvierhundert Euro trete ich Ihnen ab.", 0.25, "Ewald"),
    ("[sn1]Einverstanden. Ab jetzt zahlt sie an uns.", 0.3, "Sven"),
    # --- A3 Fall: die Zahlung, das Inkassobüro meldet sich ------------------------------------------------------------
    ("[nichts]Tanja erfährt davon nichts. [zahlt]Eine Woche später überweist sie die zweitausendvierhundert Euro an "
     "Ewald. [meldet]Dann meldet sich das Inkassobüro bei ihr.", 0.25),
    ("[sn2]Bitte zahlen Sie die zweitausendvierhundert Euro jetzt an uns.", 0.25, "Sven"),
    ("[ta1]Aber ich habe doch schon an den Maler gezahlt!", 0.3, "Tanja"),
    ("[frage]Muss Tanja noch einmal zahlen? [frage2]Dafür klären wir zwei Fragen: Ist die Forderung übergegangen? "
     "Und wie schützt das Gesetz Tanja?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C § 398 BGB (Wortlaut) -------------------------------------------------------------------------------------------
    ("[w398]Die Abtretung regelt Paragraf dreihundertachtundneunzig: Eine Forderung kann von dem Gläubiger durch Vertrag "
     "mit einem anderen auf diesen übertragen werden. [w398b]Mit dem Abschluss des Vertrags tritt der neue Gläubiger an "
     "die Stelle des bisherigen Gläubigers. [rollen]Ewald ist der Altgläubiger, auch Zedent genannt, das Inkassobüro der "
     "Neugläubiger, der Zessionar. Tanja bleibt Schuldnerin.", PS),
    # --- D I. Voraussetzungen ---------------------------------------------------------------------------------------------
    ("[vor]Die Abtretung hat vier Voraussetzungen. [v1]Erstens: ein Abtretungsvertrag, also die Einigung zwischen Alt- und "
     "Neugläubiger. [v1b]Er ist grundsätzlich formfrei, und der Schuldner muss nicht mitwirken. [v1c]Ewald und das "
     "Inkassobüro haben sich geeinigt. Dass Tanja nichts weiß, schadet nicht.", P),
    ("[v2]Zweitens: Die Forderung muss bestehen. [v2b]Einen gutgläubigen Erwerb von Forderungen gibt es grundsätzlich nicht. "
     "[v405]Nur Paragraf vierhundertfünf hilft in engen Fällen, wenn die Forderung unter Vorlage einer Schuldurkunde "
     "abgetreten wird. [v2c]Hier besteht der Werklohnanspruch aus Paragraf sechshunderteinunddreißig.", P),
    ("[v3]Drittens: Die Forderung muss bestimmt oder wenigstens bestimmbar sein. [v3k]Bei künftigen Forderungen genügt es, "
     "wenn sie spätestens bei ihrer Entstehung bestimmbar sind. [v3b]Die Rechnung über zweitausendvierhundert Euro gegen "
     "Tanja ist eindeutig.", P),
    ("[v4]Viertens: Die Abtretung darf nicht ausgeschlossen sein. [v399]Nach Paragraf dreihundertneunundneunzig scheitert sie "
     "etwa, wenn Gläubiger und Schuldner sie vertraglich ausgeschlossen haben. [v354]Ist das Geschäft für beide Seiten ein "
     "Handelsgeschäft, ist die Abtretung einer Geldforderung nach Paragraf dreihundertvierundfünfzig a des "
     "Handelsgesetzbuchs trotzdem wirksam. [v400]Und unpfändbare Forderungen sind nach Paragraf vierhundert nicht "
     "abtretbar. [v4b]Ewald und Tanja haben nichts ausgeschlossen.", P),
    ("[abstr]Und denk an das Abstraktionsprinzip: Grund der Abtretung ist hier ein Forderungskauf, Paragraf "
     "vierhundertdreiundfünfzig. [abstr2]Die Abtretung selbst ist die Verfügung. Ihre Wirksamkeit hängt grundsätzlich nicht "
     "davon ab, ob der Kauf wirksam ist.", PS),
    # --- E II. Rechtsfolge ------------------------------------------------------------------------------------------------
    ("[rf]Die Rechtsfolge: Mit dem Vertrag ist das Inkassobüro Gläubiger. [p401]Akzessorische Sicherheiten wie Bürgschaft, "
     "Pfandrecht und Hypothek gehen nach Paragraf vierhunderteins automatisch mit. [rf2]Tanja schuldet die "
     "zweitausendvierhundert Euro jetzt also dem Inkassobüro.", PS),
    # --- F III. Schuldnerschutz: §§ 404, 406 ------------------------------------------------------------------------------
    ("[schutz]Aber Tanja hat nicht mitgewirkt und soll durch die Abtretung nicht schlechter stehen. Dafür gibt es den "
     "Schuldnerschutz. [p404]Nach Paragraf vierhundertvier behält sie die Einwendungen, die zur Zeit der Abtretung gegen "
     "Ewald begründet waren. [p404b]Wäre die Wand fleckig, könnte sie den Mangel auch dem Inkassobüro entgegenhalten. "
     "[p406]Und mit einer eigenen Forderung gegen Ewald kann sie nach Paragraf vierhundertsechs grundsätzlich auch "
     "gegenüber dem Inkassobüro aufrechnen.", PS),
    # --- G § 407 Abs. 1 BGB (Wortlaut) -------------------------------------------------------------------------------------
    ("[w407]Der Hauptfall steht in Paragraf vierhundertsieben Absatz eins: Der neue Gläubiger muss eine Leistung, die der "
     "Schuldner nach der Abtretung an den bisherigen Gläubiger bewirkt, gegen sich gelten lassen, [w407b]es sei denn, dass "
     "der Schuldner die Abtretung bei der Leistung kennt. [kenn]Es kommt also auf die Kenntnis bei der Zahlung an. "
     "Kennenmüssen reicht nach dem Wortlaut nicht.", P),
    ("[sub407]Tanja wusste nichts und hat nach der Abtretung an Ewald gezahlt. [frei]Diese Zahlung muss das Inkassobüro "
     "gegen sich gelten lassen. Tanja wird frei, so sieht es auch der Bundesgerichtshof.", PS),
    ("[p409]Zwei Ergänzungen: Zeigt der Altgläubiger die Abtretung an, muss er sie nach Paragraf vierhundertneun gegen "
     "sich gelten lassen, auch wenn sie unwirksam ist. [p410]Und nach Paragraf vierhundertzehn zahlt der Schuldner an den "
     "Neugläubiger nur gegen eine Abtretungsurkunde, außer der Altgläubiger hat die Abtretung schriftlich angezeigt.", PS),
    # --- H Ergebnis -----------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Tanja muss nicht noch einmal zahlen. Ihre Zahlung an Ewald wirkt nach Paragraf vierhundertsieben "
     "Absatz eins auch gegenüber dem Inkassobüro. [p816]Das Inkassobüro muss sich an Ewald halten. [p816b]Er hat als "
     "Nichtberechtigter eine wirksame Leistung erhalten und muss die zweitausendvierhundert Euro nach Paragraf "
     "achthundertsechzehn Absatz zwei herausgeben.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der Neugläubiger verlangt Zahlung aus dem ursprünglichen Anspruch in Verbindung mit Paragraf "
     "dreihundertachtundneunzig. [tipp2]Prüfe zuerst, ob der Anspruch entstanden und übergegangen ist. [tipp3]Paragraf "
     "vierhundertsieben gehört dann zum Erlöschen, zusammen mit Paragraf dreihundertzweiundsechzig.", PS),
    # --- J Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Anspruch des Neugläubigers: [k1]Römisch eins: Anspruch entstanden. [k2]Römisch "
     "zwei: Übergang durch Abtretung, [k2a]mit Vertrag, Bestehen der Forderung, Bestimmbarkeit und keinem Ausschluss. "
     "[k3]Römisch drei: Anspruch nicht erloschen und durchsetzbar, [k3a]Paragrafen vierhundertvier, vierhundertsechs und "
     "vierhundertsieben. [k4]Römisch vier: Ergebnis. [k5]Ist der Schuldner frei, Ausgleich über Paragraf "
     "achthundertsechzehn Absatz zwei.", PS),
    # --- K Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Abtretung wechselt den Gläubiger, ohne den Schuldner zu fragen. [m2]Deshalb darf sie ihn nicht "
     "schlechter stellen: Wer nichts von ihr weiß, zahlt beim Altgläubiger mit befreiender Wirkung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
