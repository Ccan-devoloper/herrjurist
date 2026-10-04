"""Folge 162 · Analogie Jura: Regelungslücke und vergleichbare Interessenlage (Fr · Methodik · Auslegung, Format Methodik).
Beispielfall nach dem Plan-Hook („Das Gesetz regelt den Fall nicht – darf der Richter trotzdem entscheiden?“): Ilona wird
von ihrem Nachbarn Bertold seit Wochen immer wieder vor anderen Nachbarn im Hof beleidigt und klagt auf Unterlassung.
Vor Gericht hält Bertold dagegen, § 1004 BGB schütze nur das Eigentum (Wortlautkarte § 1004 Abs. 1). Ruhige Darstellung:
Beleidigungsworte werden NIE ausgeschrieben, nur die Text-Pille „beleidigende Äußerungen“.
Aufbau: Fall → Frage → Sachverhalt → Problem (§ 1004 Abs. 1 S. 2 nur Eigentum; § 823 Abs. 1 nur Schadensersatz) → Begriff
der Analogie, erst nach der Auslegung (Verweis Folge 159) → BGH-Formel (BGH IX ZR 91/24 Rn. 14, Zitatkarte) → drei
Schritte mit je eigener Farbe: 1. Regelungslücke (Gelb), 2. planwidrig (Lila; IX ZR 91/24 Rn. 15; Gegenbeispiel
Kilometerleasing VIII ZR 36/20 Rn. 43 f.), 3. vergleichbare Interessenlage (Grün; VIII ZR 36/20 Rn. 41; I ZR 12/23 Rn. 16)
→ Leitbeispiel quasinegatorischer Unterlassungsanspruch (V ZR 110/14 Rn. 20; VI ZR 230/23 Rn. 14, 19; Verweis Folge 142)
→ Einzel- und Gesamtanalogie (V ZR 56/12 Rn. 17: §§ 604 Abs. 3, 671 Abs. 1 BGB) → Umkehrschluss und teleologische
Reduktion je ein Satz (BVerwG 6 C 17/09 Rn. 30; Verweis Folge 159) → Grenzen: Art. 103 Abs. 2 GG (Wortlautkarte; BVerfG
2 BvR 2500/09 Rn. 164 f.; Verweis Folge 148), Vorbehalt des Gesetzes im Öffentlichen Recht (ein Satz, allgemein) →
Lösung im Gerichtssaal (Wiederholungsgefahr VI ZR 128/18 Rn. 9) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Namen mit eindeutig deutscher Aussprache, in keiner Textdatei unter youtube/ und nicht in der Liste vergebener Namen:
Ilona, Bertold (nie im Genitiv im Sprechtext). Die Richterin bleibt ohne Namen.
Stimmen nur aus dem Pool: Ilona lucy, Bertold christian, Richterin hilde (stephan nicht besetzt).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Ilona": "lucy", "Bertold": "christian", "Richterin": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Hof des Mehrfamilienhauses, dann vor Gericht ----------------------------------------------------------
    ("[fall]Ilona wohnt in einem Mehrfamilienhaus. [beleid]Ihr Nachbar Bertold beleidigt sie seit Wochen, immer wieder "
     "und vor anderen Nachbarn im Hof.", P),
    ("[il1]Bertold, ich will, dass das aufhört.", P, "Ilona"),
    ("[klage]Ilona klagt auf Unterlassung. [gericht]Vor Gericht hält Bertold dagegen.", P),
    ("[be1]Paragraf tausendvier schützt doch nur das Eigentum!", P, "Bertold"),
    ("[frage]Das Gesetz regelt diesen Fall nicht ausdrücklich. [frage2]Darf die Richterin trotzdem "
     "entscheiden?", P),
    ("[ri1]Dann prüfen wir eine Analogie.", PS, "Richterin"),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem: § 1004 Abs. 1 S. 2 (Wortlaut), § 823 Abs. 1 ------------------------------------------------------
    ("[w1004]Paragraf tausendvier Absatz eins Satz zwei: Sind weitere Beeinträchtigungen zu besorgen, so kann der "
     "Eigentümer auf Unterlassung klagen. [nureig]Der Wortlaut nennt nur das Eigentum, und die Ehre ist kein Eigentum.", P),
    ("[p823]Paragraf achthundertdreiundzwanzig Absatz eins schützt zwar auch das allgemeine Persönlichkeitsrecht und damit "
     "die Ehre. [nurse]Er gibt aber nur Schadensersatz für eine Verletzung, die schon geschehen ist. [kunft]Wie Ilona "
     "künftige Beleidigungen verhindert, regelt er nicht.", P),
    ("[ana]Hier setzt die Analogie an: Eine Norm wird auf einen Fall übertragen, den ihr Wortlaut nicht erfasst. "
     "[erst]Das kommt erst in Betracht, wenn die Auslegung ausgeschöpft ist.", PS),
    # --- D Die BGH-Formel (BGH IX ZR 91/24 Rn. 14) und drei Schritte ------------------------------------------------------
    ("[bgh]Der Bundesgerichtshof sagt: Die analoge Anwendung einer Vorschrift ist nur dann zulässig, wenn das Gesetz eine "
     "planwidrige Regelungslücke enthält [vgl]und der Sachverhalt mit dem geregelten Tatbestand vergleichbar ist. "
     "[abw]Man muss annehmen können, der Gesetzgeber wäre zum gleichen Abwägungsergebnis gekommen.", P),
    ("[drei]Daraus folgen drei Schritte. [s1]Erstens: eine Regelungslücke. [s2]Zweitens: Die Lücke ist planwidrig. "
     "[s3]Drittens: eine vergleichbare Interessenlage.", PS),
    # --- E1 1. Regelungslücke (Gelb) --------------------------------------------------------------------------------------
    ("[l1]Eine Lücke besteht, wenn keine Norm den Fall erfasst, auch nicht nach Auslegung. [l2]So ist es bei Ilona: "
     "Paragraf tausendvier erfasst nur das Eigentum, Paragraf achthundertdreiundzwanzig gibt nur Schadensersatz. "
     "[l3]Eine Lücke liegt vor.", P),
    # --- E2 2. planwidrig (Lila) ------------------------------------------------------------------------------------------
    ("[pw1]Planwidrig ist sie, wenn der Gesetzgeber unbeabsichtigt von seinem Regelungsplan abgewichen ist, den Fall also "
     "übersehen hat. [pw2]Hat er ihn bewusst ausgespart, scheidet die Analogie aus. [pw3]Das zeigen vor allem "
     "Entstehungsgeschichte und Zweck des Gesetzes. [pw4]So verneinte der Bundesgerichtshof eine Analogie beim "
     "Kilometerleasing: Der Gesetzgeber hatte die Fälle bewusst beschränkt.", P),
    ("[pwf]Bei Ilona spricht die Systematik für eine planwidrige Lücke. [sys]Das Gesetz gibt Unterlassungsansprüche für den "
     "Namen, den Besitz und das Eigentum, in den Paragrafen zwölf, achthundertzweiundsechzig und tausendvier. [ehre]Dass "
     "die Ehre gegen künftige Verletzungen schutzlos bleiben soll, ist nicht erkennbar.", P),
    # --- E3 3. vergleichbare Interessenlage (Grün) ------------------------------------------------------------------------
    ("[vi1]Drittens muss die Interessenlage vergleichbar sein: Die Wertung der Norm muss auch auf den neuen Fall passen. "
     "[vi2]Nach dem Bundesgerichtshof ist es dem Inhaber eines deliktsrechtlich geschützten Rechtsguts nicht "
     "zuzumuten, eine Verletzung tatenlos hinzunehmen. [vi3]Für die Ehre gilt das wie für das Eigentum.", PS),
    # --- F Leitbeispiel: quasinegatorischer Unterlassungsanspruch ---------------------------------------------------------
    ("[rspr]So sieht es auch die Rechtsprechung. [qn]Der Bundesgerichtshof wendet Paragraf tausendvier entsprechend auf alle "
     "Rechtsgüter an, die Paragraf achthundertdreiundzwanzig schützt; [qn2]man spricht vom quasinegatorischen Unterlassungsanspruch. "
     "[agl]Bei Ehrverletzungen lautet die Anspruchsgrundlage: Paragraf tausendvier Absatz eins Satz zwei analog, in "
     "Verbindung mit Paragraf achthundertdreiundzwanzig Absatz eins und dem allgemeinen Persönlichkeitsrecht. "
     "[f142]Wie der Anspruch beim Eigentum funktioniert, zeigt die Folge zu Paragraf tausendvier.", PS),
    # --- G Einzelanalogie und Gesamtanalogie ------------------------------------------------------------------------------
    ("[einzel]Das ist eine Einzelanalogie: Eine einzelne Norm wird übertragen. [gesamt]Bei der Gesamtanalogie, auch "
     "Rechtsanalogie genannt, gewinnt man aus mehreren Normen einen gemeinsamen Grundgedanken. [gbsp]So leitete der "
     "Bundesgerichtshof aus den Regeln zur Leihe und zum Auftrag ab: Eine unentgeltliche Versorgungsvereinbarung ist "
     "jederzeit kündbar.", PS),
    # --- H Gegenstücke: Umkehrschluss, teleologische Reduktion (Verweis 159) ---------------------------------------------
    ("[gegen]Zwei Gegenstücke kennst du schon aus der Folge zu den Auslegungsmethoden. [uk]Beim Umkehrschluss folgert man: "
     "Regelt das Gesetz einen Fall abschließend, gilt die Rechtsfolge für andere Fälle gerade nicht. [tr]Bei der teleologischen "
     "Reduktion ist es umgekehrt wie bei der Analogie: Der Wortlaut erfasst einen Fall, den der Zweck der Norm nicht "
     "erfassen soll.", PS),
    # --- I Grenzen: Art. 103 Abs. 2 GG (Wortlaut), Vorbehalt des Gesetzes --------------------------------------------------
    ("[grenz]Die Analogie hat Grenzen. [a103]Artikel hundertdrei Absatz zwei Grundgesetz: Eine Tat kann nur bestraft "
     "werden, wenn die Strafbarkeit gesetzlich bestimmt war, bevor die Tat begangen wurde. [av]Daraus folgt ein Verbot "
     "strafbegründender Analogie: Zulasten des Täters ist sie im Strafrecht ausgeschlossen; mehr dazu in der Folge zur "
     "Unfallflucht.", P),
    ("[oer]Im Öffentlichen Recht braucht ein belastender Eingriff eine gesetzliche Grundlage, das ist der Vorbehalt des "
     "Gesetzes. [oer2]Eine Analogie darf diese Grundlage nicht einfach ersetzen.", PS),
    # --- J Lösung im Gerichtssaal -----------------------------------------------------------------------------------------
    ("[loes]Zurück vor Gericht. [loes1]Lücke, Planwidrigkeit und vergleichbare Interessenlage liegen vor, die Richterin darf die Lücke also "
     "schließen. [abwg]Die "
     "Beleidigungen verletzen Ilona in ihrer Ehre, und die Meinungsfreiheit deckt sie hier nicht. [wg]Weil Bertold schon "
     "mehrfach beleidigt hat, wird die Wiederholungsgefahr vermutet.", P),
    ("[ri2]Der Beklagte muss die beleidigenden Äußerungen künftig unterlassen.", P, "Richterin"),
    ("[erg]Ilona hat einen Unterlassungsanspruch analog Paragraf tausendvier.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe eine Analogie erst, wenn die Auslegung gescheitert ist. [tipp2]Und schreib nie nur "
     "„analog“. [tipp3]Begründe die drei Schritte: Lücke, planwidrig, vergleichbar.", PS),
    # --- L Prüfschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Analogie. [k1]Römisch eins: keine direkte Anwendung, auch nicht nach Auslegung. "
     "[k2]Römisch zwei: die Analogie, [k2a]erstens mit einer Regelungslücke, [k2b]zweitens mit Planwidrigkeit, "
     "[k2c]drittens mit vergleichbarer Interessenlage. [k3]Römisch drei: Keine Grenze steht entgegen, etwa das "
     "Analogieverbot. "
     "[k4]Römisch vier: Die Rechtsfolge gilt entsprechend.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Analogie überträgt eine Norm auf einen ungeregelten Fall. [m2]Sie trägt nur, wenn die Lücke "
     "planwidrig und die Interessenlage vergleichbar ist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
