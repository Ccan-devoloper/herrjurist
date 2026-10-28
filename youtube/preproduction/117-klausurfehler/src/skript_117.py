"""Folge 117 · Jura Klausur Fehler: Die 10 häufigsten und wie du sie vermeidest (Fr · Methodik · Klausurtechnik, Format
Methodik).
Rahmen: Rückgabe einer Übungsklausur im Zivilrecht. Die Studentin Ronja bekommt ihre Arbeit von der Korrektorin Frau
Brinkmann zurück; die Randbemerkungen (rote Pillen am Blatt) führen durch zehn typische Fehler, geordnet nach dem
Arbeitsablauf der Klausur (lesen → gliedern → schreiben → abschließen). Die Korrektorin spricht nicht (Stimme julia war in
109, 112, 114 besetzt); die Erzählerin liest ihre Randbemerkungen vor.
Übungsfall der Klausur: Frau Kröger kauft am 1. März online eine Jacke für 80 €, erhält sie am 6. März, widerruft am
18. März per E-Mail ohne Grund; der Händler verweigert die Rückzahlung (Frist abgelaufen, kein Grund). Lösung:
Widerrufsrecht § 312g Abs. 1 BGB, Fristbeginn mit Erhalt der Ware (§ 356 Abs. 2 Nr. 1 Buchst. a BGB), Fristende
20. März (§§ 187 Abs. 1, 188 Abs. 1 BGB), Absendung genügt (§ 355 Abs. 1 Satz 5), keine Begründung nötig (§ 355 Abs. 1
Satz 4), Rückzahlung nach § 355 Abs. 3 Satz 1 BGB.
Fehler (Reihenfolge nach Arbeitsablauf, Begründung in ../SZENENPLAN.md): 1 Sachverhalt/Bearbeitervermerk, 2 Fallfrage,
3 Aufbau (Zivil: § 546 vor § 985 BGB; Straf: objektiver Tatbestand vor Vorsatz, § 16 Abs. 1 StGB), 4 Normzitat,
5 Definition/Subsumtion, 6 Gutachtenstil am falschen Ort, 7 Schwerpunkt, 8 Meinungsstreit, 9 Zeit, 10 Ergebnis.
„Häufig“ nur als Erfahrungswert aus gelesenen Hinweisen (LJPA Sachsen-Anhalt, Nds. Merkblätter, Uni Bielefeld,
ZJS-Beiträge), keine Zahlen. Belege: ../RECHTSSTAND.md.
Figuren: Ronja (ela_froh), Frau Brinkmann (stumm); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ronja": "ela_froh"}  # Lexi = Erzählerstimme (Carla); Frau Brinkmann spricht nicht

SEGMENTE = [
    # --- A Fall: Rückgabe der Übungsklausur --------------------------------------------------------------------------
    ("[fall]Rückgabe der Übungsklausur im Zivilrecht. [korr]Frau Brinkmann hat korrigiert und gibt Ronja ihre Arbeit "
     "zurück. [rand]Am Rand stehen viele rote Bemerkungen.", 0.3),
    ("[r1]Fünf Punkte? Dabei kannte ich das Widerrufsrecht genau!", 0.3, "Ronja"),
    ("[hook]Viele Punkte gehen nicht durch Nichtwissen verloren, sondern durch Fehler in Aufbau, Stil und Schwerpunkt. "
     "[warn]Vor diesen Fehlern warnen Prüfungsämter und Universitäten in ihren Hinweisen immer wieder. "
     "[zehn]Zehn davon stecken in der Klausur von Ronja.", 0.3),
    ("[r2]Welche sind das, und wie vermeide ich sie?", 0.4, "Ronja"),
    # --- B Sachverhalt der Übungsklausur -------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt der Übungsklausur. Halte das Video ruhig kurz an.", 5.0),
    # --- C Fehler 1: Sachverhalt und Bearbeitervermerk -----------------------------------------------------------------
    ("[f1]Fehler eins: Sachverhalt und Bearbeitervermerk nicht ausgewertet. [f1a]Im Sachverhalt stehen zwei Daten, der "
     "Kauf am ersten März und die Lieferung am sechsten. Ronja rechnet nur mit dem Kauf. [f1b]Und obwohl der Vermerk sagt, "
     "dass richtig belehrt wurde, prüft sie eine Seite lang die Belehrung. [f1c]Am Rand steht: Bearbeitervermerk? "
     "[f1d]Besser: Lies den Vermerk zuerst. Und frag bei jeder Angabe, wofür du sie brauchst. [f1e]Zwei Daten deuten "
     "oft auf eine Frist.", P),
    # --- D Fehler 2: die Fallfrage ---------------------------------------------------------------------------------------
    ("[f2]Fehler zwei: die falsche Frage. Ronja prüft, ob der Kaufvertrag wirksam ist. [f2a]Gefragt ist aber, ob "
     "Frau Kröger ihr Geld zurückbekommt. Am Rand: Frage? [f2b]Besser: Wer will was von wem woraus? "
     "[f2c]Frau Kröger könnte gegen den Händler einen Anspruch auf Rückzahlung von achtzig Euro haben, aus Paragraf "
     "dreihundertfünfundfünfzig Absatz drei Satz eins BGB.", P),
    # --- E Fehler 3: der Aufbau ------------------------------------------------------------------------------------------
    ("[f3]Fehler drei: der Aufbau. Hier hat Ronja alles richtig gemacht, typisch sind zwei Beispiele aus anderen "
     "Klausuren. [f3a]Verlangt ein Vermieter seine Wohnung zurück, prüfst du zuerst den Vertrag, Paragraf "
     "fünfhundertsechsundvierzig, und erst dann das Eigentum. [f3b]Denn der Mietvertrag kann ein Recht zum Besitz geben. "
     "[f3c]Im Strafrecht kommt der objektive Tatbestand vor dem Vorsatz. [f3d]Der Vorsatz bezieht sich auf die "
     "Tatumstände, also stellst du sie zuerst fest.", P),
    # --- F Fehler 4: die Norm ---------------------------------------------------------------------------------------------
    ("[f4]Fehler vier: die Norm ungenau zitiert. Ronja schreibt nur: Paragraf dreihundertsechsundfünfzig. Am Rand: Norm? "
     "[f4a]Die Vorschrift hat sechs Absätze. Den Fristbeginn regelt Absatz zwei Nummer eins Buchstabe a. "
     "[f4b]Nenn also immer Absatz, Satz und Nummer, so genau es geht.", P),
    # --- G Fehler 5: Definition und Subsumtion ----------------------------------------------------------------------------
    ("[f5]Fehler fünf: Definition und Subsumtion fehlen. Ronja schreibt nur: Es liegt ein Fernabsatzvertrag vor. "
     "Das ist eine Behauptung. Am Rand: Definition? [f5a]Besser: Ein Fernabsatzvertrag verlangt, dass beide Seiten für "
     "Verhandlung und Vertragsschluss ausschließlich Fernkommunikationsmittel verwenden, Paragraf dreihundertzwölf c Absatz eins. "
     "[f5b]Frau Kröger hat allein über den Onlineshop bestellt. [f5c]Erst danach folgt: also ein "
     "Fernabsatzvertrag.", P),
    # --- H Fehler 6: Gutachtenstil am falschen Ort ------------------------------------------------------------------------
    ("[f6]Fehler sechs: der Gutachtenstil am falschen Ort. [f6a]Den Kaufvertrag prüft Ronja Schritt für Schritt, Angebot "
     "und Annahme, alles im Konjunktiv, obwohl er klar ist. [f6b]Am Problem schreibt sie dagegen nur: Die Frist ist "
     "abgelaufen, denn sie beginnt mit dem Kauf. Am Rand: Ergebnis vorweg? [f6c]Richtig ist es umgekehrt: Klares "
     "stellst du in einem Satz fest. [f6d]Am Problem prüfst du im Gutachtenstil, und das Ergebnis kommt zum Schluss.", P),
    # --- I Fehler 7: der Schwerpunkt --------------------------------------------------------------------------------------
    ("[f7]Fehler sieben: der Schwerpunkt verfehlt. Eine Seite zum Kaufvertrag, zwei Zeilen zur Frist. Am Rand: "
     "Schwerpunkt? [f7a]Dabei liegt genau hier das Problem. Die Frist beträgt vierzehn Tage und beginnt erst, als "
     "Frau Kröger die Jacke erhält, am sechsten März. [f7b]Sie endet am zwanzigsten März. Der Widerruf ging am "
     "achtzehnten ab, also rechtzeitig. [f7c]Und einen Grund muss er nicht enthalten.", P),
    # --- J Fehler 8: der Meinungsstreit -----------------------------------------------------------------------------------
    ("[f8]Fehler acht: der Meinungsstreit. Bei einer Nebenfrage stellt Ronja zwei Ansichten dar und schreibt dann nur: "
     "Das ist umstritten. Am Rand: Ihre Lösung? [f8a]Frag zuerst: Ändert der Streit das Ergebnis? [f8b]Führen beide "
     "Ansichten zum selben Ergebnis, kann der Streit dahinstehen. [f8c]Führen sie zu verschiedenen, entscheidest du, "
     "mit einem Argument, nicht nur mit dem Hinweis auf die herrschende Meinung.", P),
    # --- K Fehler 9: die Zeit ---------------------------------------------------------------------------------------------
    ("[f9]Fehler neun: die Zeit. Für die Rückzahlung selbst bleibt Ronja keine Minute, der Punkt fehlt ganz. Am Rand: "
     "Rückzahlung? [f9a]Besser: ein Zeitplan mit Uhrzeiten an der Skizze, wie in Folge fünfundvierzig. "
     "[f9b]Wird es knapp, schreibst du die Gliederung trotzdem zu Ende und den Rest kurz im Urteilsstil.", P),
    # --- L Fehler 10: das Ergebnis ----------------------------------------------------------------------------------------
    ("[f10]Fehler zehn: Das Ergebnis widerspricht der Prüfung. Oben steht: Frist abgelaufen. Unten schreibt Ronja "
     "schnell: Frau Kröger kann die achtzig Euro zurückverlangen. Am Rand: Widerspruch? [f10a]Besser: Das Ergebnis folgt "
     "aus der Prüfung darüber. Richtig gerechnet war der Widerruf rechtzeitig, also: [f10b]Frau Kröger kann vom Händler die Rückzahlung "
     "der achtzig Euro verlangen.", 0.3),
    ("[r3]Das nehme ich mir für die nächste Klausur vor.", 0.4, "Ronja"),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lies vor der Abgabe die Fallfrage und dein Ergebnis direkt hintereinander. [tipp2]Passt die "
     "Antwort zur Frage? [tipp3]Und trägt die Prüfung darüber genau dieses Ergebnis?", PS),
    # --- N Checkliste als Klausurschema -----------------------------------------------------------------------------------
    ("[sch]Deine Checkliste vor der Abgabe. [k1]Römisch eins, vor dem Schreiben: Bearbeitervermerk, Sachverhalt, "
     "Fallfrage. [k2]Römisch zwei, die Gliederung: der richtige Aufbau. [k3]Römisch drei, beim Schreiben: "
     "[k31]genaue Normen, [k32]Definition mit Subsumtion, [k33]Gutachtenstil nur am Problem, [k34]dort der Schwerpunkt, "
     "[k35]und ein Streit nur, wenn er das Ergebnis ändert. [k4]Römisch vier, am Ende: die Zeit im Blick, [k41]und ein "
     "Ergebnis, das die Frage beantwortet.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Punkte holst du am Problem. [m2]Lies genau, zitiere genau, und schreib ausführlich nur dort, wo "
     "der Fall es verlangt. [m3]Am Ende beantwortest du die Frage.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
