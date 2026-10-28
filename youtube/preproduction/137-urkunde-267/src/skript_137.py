"""Folge 137 · Urkunde § 267 StGB: Was ist eine Urkunde? Die 3 Funktionen (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook: Femke (16) schwänzt am Montag die Schule, schreibt am Abend eine Entschuldigung
(„wegen Fieber“), setzt den Namen ihrer Mutter darunter und ahmt deren Unterschrift nach. Die Mutter weiß nichts davon.
Am Dienstag nimmt die Klassenlehrerin Frau Melzer den Zettel entgegen und heftet ihn ab.
Prüfung: Wortlautkarte § 267 I → Urkundenbegriff (BGH 5 StR 283/22 Rn. 36; 2 StR 192/23 Rn. 36) → 1. Perpetuierungs-,
2. Beweis- (Absichts-/Zufallsurkunde: Lehre; Fotokopie BGH 2 StR 434/14 Rn. 34), 3. Garantiefunktion (Beweiszeichen
BGH 3 StR 521/18 Rn. 33) → Tathandlungen: Herstellen einer unechten Urkunde (BGH 1 StR 328/19 Rn. 70, 75; 2 StR 192/23
Rn. 17), schriftliche Lüge (2 StR 192/23 Rn. 29, 35), Verfälschen (5 StR 38/23 Rn. 13), Gebrauchen (3 StR 521/18 Rn. 34)
→ subjektiv: Vorsatz, zur Täuschung im Rechtsverkehr (Lehrbuchdefinition, offengelegt) → Gegenvariante Erlaubnis
(1 StR 328/19 Rn. 70–72, 76) → RW, Schuld (§ 19 StGB, §§ 1, 3 JGG), Ergebnis, eine Tat (3 StR 156/08 Rn. 11)
→ Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Femke, Melzer. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.6

# Femke (16) spricht mit lucy (Frau, jung; wie Marie, 17, in Folge 062), Frau Melzer (um 58) mit hilde (Frau, älter).
# Die Mutter spricht nicht. stephan und christian werden nicht eingesetzt.
STIMMEN = {"Femke": "lucy", "Melzer": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Entschuldigung ----------------------------------------------------------------------------------------
    ("[fall]Femke ist sechzehn. [schwaenzt]Am Montag schwänzt sie die Schule. [abend]Am Abend "
     "schreibt sie auf einen Zettel: [zettel]Femke war am Montag krank. Bitte entschuldigen "
     "Sie ihr Fehlen. [unterschrift]Darunter setzt sie den Namen ihrer Mutter und ahmt deren Unterschrift nach. [mutter]Die "
     "Mutter weiß davon nichts. [dienstag]Am Dienstag gibt Femke den Zettel ihrer Klassenlehrerin, Frau Melzer.", 0.3),
    ("[f1]Hier ist meine Entschuldigung für gestern.", 0.3, "Femke"),
    ("[m1]Danke, Femke. Dann ist dein Fehlen entschuldigt.", 0.3, "Melzer"),
    ("[ablage]Frau Melzer heftet den Zettel ab. [frage]Hat sich Femke wegen Urkundenfälschung strafbar gemacht? [frage2]Zuerst "
     "klären wir: Was ist eine Urkunde?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut und Urkundenbegriff ------------------------------------------------------------------------------------
    ("[p267]Paragraf zweihundertsiebenundsechzig, Absatz eins: [p267w]Wer zur Täuschung im Rechtsverkehr eine unechte Urkunde "
     "herstellt, eine echte Urkunde verfälscht oder eine unechte oder verfälschte Urkunde gebraucht, wird mit Freiheitsstrafe "
     "bis zu fünf Jahren oder mit Geldstrafe bestraft. [nichtdef]Was eine Urkunde ist, sagt das Gesetz nicht. [def]Nach "
     "ständiger Rechtsprechung ist eine Urkunde jede verkörperte Gedankenerklärung, die zum Beweis im Rechtsverkehr geeignet "
     "und bestimmt ist und ihren Aussteller erkennen lässt. [drei]Daraus folgen drei Funktionen: [fperp]Perpetuierung, "
     "[fbew]Beweis [fgar]und Garantie.", PS),
    # --- D 1. Perpetuierungsfunktion ---------------------------------------------------------------------------------------
    ("[perp]Erstens, die Perpetuierungsfunktion: Die Erklärung muss verkörpert sein, also dauerhaft auf einer Sache "
     "festgehalten. [perp2]Ein Anruf in der Schule wäre keine Urkunde. [perp3]Der Zettel hält die Erklärung auf Papier fest.",
     PS),
    # --- E 2. Beweisfunktion -----------------------------------------------------------------------------------------------
    ("[bew]Zweitens, die Beweisfunktion: Die Erklärung muss geeignet und bestimmt sein, für ein Rechtsverhältnis Beweis zu "
     "erbringen. [bew2]Die Entschuldigung soll der Schule beweisen, dass die Mutter das Fehlen entschuldigt. Dafür ist sie "
     "geeignet und gerade dafür geschrieben. [absicht]Die Lehre nennt das eine Absichtsurkunde. [zufall]Bestimmt erst später "
     "jemand ein Schriftstück zum Beweis, etwa einen alten Brief, spricht sie von einer Zufallsurkunde. [kopie]Keine Urkunde "
     "ist dagegen eine bloße Fotokopie, die als Kopie erscheint: Ihr fehlt die Beweiseignung.", PS),
    # --- F 3. Garantiefunktion ---------------------------------------------------------------------------------------------
    ("[gar]Drittens, die Garantiefunktion: Die Urkunde muss ihren Aussteller erkennen lassen, also den, der für die Erklärung "
     "einsteht. [gar2]Hier zeigt die Unterschrift die Mutter als Ausstellerin. [bz]Übrigens kann auch ein bloßes Zeichen "
     "eine Urkunde sein, ein sogenanntes Beweiszeichen. So bildet die Fahrzeugidentifikationsnummer mit dem Auto eine "
     "Urkunde. [urk]Die Entschuldigung ist also eine Urkunde.", PS),
    # --- G Tathandlung: Herstellen einer unechten Urkunde ------------------------------------------------------------------
    ("[tat]Jetzt die Tathandlung. Das Gesetz nennt drei: [herst]Herstellen einer unechten Urkunde, [verf]Verfälschen einer "
     "echten [gebr]und Gebrauchen. [unecht]Unecht ist eine Urkunde, wenn sie über die Identität des Ausstellers täuscht. Sie "
     "stammt nicht von dem, der aus ihr als Aussteller hervorgeht. [geist]Aussteller ist nach der Geistigkeitstheorie, wer "
     "geistig hinter der Erklärung steht, wer sie sich also zurechnen lassen will. [hand]Wer den Stift führt, entscheidet "
     "nicht. [sub]Die Mutter will sich diesen Zettel nicht zurechnen lassen. Er stammt geistig von Femke. [sub2]Die Urkunde "
     "ist unecht, und Femke hat sie hergestellt.", PS),
    # --- H Abgrenzung: schriftliche Lüge -----------------------------------------------------------------------------------
    ("[luege]Achtung, zentraler Klausurpunkt: Dass der Zettel lügt, macht ihn nicht unecht. Femke war nicht krank. "
     "[luege2]Hätte die Mutter selbst die falsche Entschuldigung geschrieben, wäre die Urkunde echt, nur inhaltlich unwahr. "
     "[luege3]Diese schriftliche Lüge erfasst Paragraf zweihundertsiebenundsechzig nicht. [luege4]Es geht um die Echtheit der "
     "Urkunde, nicht um die Wahrheit ihres Inhalts.", PS),
    # --- I Verfälschen und Gebrauchen --------------------------------------------------------------------------------------
    ("[verf2]Verfälschen hieße: eine echte Urkunde nachträglich inhaltlich ändern, etwa in einer echten Entschuldigung der "
     "Mutter einen zweiten Fehltag ergänzen. [gebr2]Gebraucht ist die Urkunde, wenn der Täter sie dem zu "
     "Täuschenden so zugänglich macht, dass er sie wahrnehmen kann. [gebr3]Femke gibt Frau Melzer den Zettel in die Hand. "
     "[gebr4]Damit hat sie ihn auch gebraucht.", PS),
    # --- J Subjektiver Tatbestand ------------------------------------------------------------------------------------------
    ("[vors]Subjektiv braucht Femke Vorsatz. [vors2]Sie weiß, dass ihre Mutter nicht unterschrieben hat, und will den Zettel "
     "abgeben. [rv]Außerdem muss sie zur Täuschung im Rechtsverkehr handeln. Nach der gängigen Definition will der Täter einen "
     "Irrtum über die Echtheit erregen und den Getäuschten so zu einem rechtlich erheblichen Verhalten bringen. [rv2]Femke "
     "will, dass Frau Melzer den Zettel für echt hält und das Fehlen als entschuldigt behandelt. [rv3]Das genügt.", PS),
    # --- K Gegenvariante: Erlaubnis der Mutter -----------------------------------------------------------------------------
    ("[var]Und wenn Femke wirklich krank war und die Mutter ihr am Telefon erlaubt hätte, für sie zu unterschreiben? "
     "[var2]Dann will die Mutter sich die Erklärung zurechnen lassen. Sie steht geistig dahinter, Femke unterschreibt nur "
     "für sie. [var3]Die Urkunde ist echt, solange kein Gesetz eine eigenhändige Unterschrift verlangt, wie etwa beim "
     "Testament.", PS),
    # --- L Rechtswidrigkeit, Schuld, Ergebnis ------------------------------------------------------------------------------
    ("[rw]Zurück zum Fall: Rechtfertigungsgründe sind nicht ersichtlich. [schuld]Femke ist sechzehn und damit "
     "strafmündig; schuldunfähig ist nach Paragraf neunzehn nur, wer noch nicht vierzehn ist. [jgg]Für sie gilt das "
     "Jugendstrafrecht. [erg]Ergebnis: Femke ist strafbar wegen Urkundenfälschung. "
     "[konk]Herstellen und Gebrauchen sind hier eine Tat, weil sie den Zettel schon beim Schreiben so verwenden wollte.", PS),
    # --- M Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne Echtheit und Wahrheit. [tipp2]Frage zuerst: Wer steht geistig hinter der Erklärung? Nur wenn "
     "das ein anderer ist als der scheinbare Aussteller, ist die Urkunde unecht. [tipp3]Und prüfe eine Erlaubnis "
     "des Namensträgers schon bei der Unechtheit, nicht erst bei der Rechtswidrigkeit.", PS),
    # --- N Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand. [k1a]Objektiv erstens die Urkunde mit Perpetuierungs-, Beweis- und "
     "Garantiefunktion, [k1b]zweitens die Tathandlung: Herstellen, Verfälschen "
     "oder Gebrauchen. [k1c]Subjektiv Vorsatz [k1d]und Handeln zur Täuschung im Rechtsverkehr. "
     "[k2]Römisch zwei: Rechtswidrigkeit. [k3]Römisch drei: Schuld. [k4]Und am Ende die Konkurrenzen.", PS),
    # --- O Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Urkunde hält eine Erklärung fest, beweist etwas und zeigt, wer dafür einsteht. [m2]Unecht ist sie "
     "nur, wenn sie über den Aussteller täuscht. [m3]Wer bloß lügt, fälscht keine Urkunde.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
