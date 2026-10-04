"""Folge 167 · Kopie als Urkunde? Scan, PDF & § 269 StGB (Mi · Examenswissen · StGB BT, Format Streitstand).
Fall nach dem Plan-Hook: Janosch (19) bewirbt sich um einen Ausbildungsplatz, scannt sein Abiturzeugnis (Note 2,8), ändert
am Rechner die Note in 1,8, speichert als PDF und schickt es per E-Mail an Frau Hagemann (Personalabteilung). Variante:
Ausdruck der bearbeiteten Datei, per Post „als Kopie“.
Prüfung: Urkundenbegriff (nur Verweis auf Folge 137) → einfache Fotokopie keine Urkunde (BGHSt 24, 140, 141 f., wiedergegeben
in BGH 2 StR 428/10 Rn. 11, 5 StR 488/09 Rn. 9, 10) → Streit (Gegenansicht in der Literatur, nach Nestler ZJS 2010, 608;
OLG Celle 1 ORs 2/23) → Ausnahmen: Anschein des Originals (5 StR 488/09 Rn. 8), Kopie eines gefälschten Originals auch
beglaubigt = Gebrauchen (2 StR 149/01 Rn. 7, 8; BGHSt 24, 140, 142 nach 5 StR 488/09 Rn. 12), Grenze Collage (2 StR 411/02
Rn. 6) → Datei: § 269 statt § 267 (4 StR 141/17 Rn. 9), Wortlautkarte § 269 Abs. 1, hypothetischer Urkundenvergleich
(2 StR 192/23 Rn. 17), Scan vs. digitales Original (2 StR 192/23 Rn. 27, 28), PDF-Zeugnis (OLG Celle), Gegenansicht,
§ 270 → Lösung beider Varianten (2 StR 428/10 Rn. 12) → Betrug als Ausblick (3 StR 221/18 Rn. 30) → Merktabelle →
Klausurtipp → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Janosch, Hagemann. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.6

# Janosch (19) spricht mit marc (Mann, mittel), Frau Hagemann (um 45) mit sabrina (Frau, mittel).
# william und laura_ruhig werden nicht eingesetzt.
STIMMEN = {"Janosch": "marc", "Hagemann": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ------------------------------------------------------------------------------------------------------------
    ("[fall]Janosch ist neunzehn und bewirbt sich um einen Ausbildungsplatz. [note]In seinem Abiturzeugnis steht die "
     "Note zwei Komma acht. [scan]Er scannt das Zeugnis ein [aendern]und ändert am Rechner die Note in eins Komma acht.", 0.3),
    ("[j1]Eine Eins vorne sieht einfach besser aus.", 0.3, "Janosch"),
    ("[pdf]Er speichert die Datei als PDF [mail]und schickt sie per E-Mail an Frau Hagemann aus der Personalabteilung.", 0.3),
    ("[h1]Eins Komma acht, sehr gut. Sie sind in der nächsten Runde.", 0.3, "Hagemann"),
    ("[variante]Variante: Janosch druckt die bearbeitete Datei aus und schickt den Ausdruck per Post, als Kopie seines "
     "Zeugnisses. [frage]Hat er eine Urkunde gefälscht? [frage2]Oder greift Paragraf zweihundertneunundsechzig?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Fotokopie: Grundsatz --------------------------------------------------------------------------------------------
    ("[begriff]Was eine Urkunde ist, kennst du aus der Folge zur gefälschten Entschuldigung: eine verkörperte "
     "Gedankenerklärung, die zum Beweis geeignet und bestimmt ist und ihren Aussteller erkennen lässt. [kopie]Und die "
     "einfache Fotokopie? Seit einem Urteil des Bundesgerichtshofs von neunzehnhunderteinundsiebzig gilt: Sie ist keine "
     "Urkunde, sofern sie nach außen als Reproduktion erscheint. [grund]Ihr fehlen die Beweiseignung und ein erkennbarer "
     "Aussteller. [grund2]Sie gibt die Erklärung des Originals nur bildlich wieder und verkörpert keine eigene.", PS),
    # --- D Streitstand Fotokopie -------------------------------------------------------------------------------------------
    ("[streit]Ganz unbestritten ist das nicht. [mm]Eine Gegenansicht in der Literatur hält Kopien für beweisgeeignet und "
     "damit grundsätzlich für Urkunden. [hm]Die herrschende Meinung folgt der Rechtsprechung: Für eine bloße Kopie steht "
     "kein erkennbarer Aussteller mit seiner Garantie ein.", PS),
    # --- E Ausnahmen und Grenze --------------------------------------------------------------------------------------------
    ("[aus]Zwei Ausnahmen und eine Grenze musst du kennen. [aus1]Erstens: Die Kopie erscheint selbst als Original. Ist "
     "sie einer Originalurkunde so ähnlich, dass eine Verwechslung möglich ist, ist sie eine Urkunde, nach einer "
     "Manipulation eine unechte. [aus2]Zweitens: Es gibt ein gefälschtes Original. Wer davon eine Kopie vorlegt, auch "
     "eine beglaubigte, gebraucht nach der Rechtsprechung das gefälschte Original. [examen]So entschied der "
     "Bundesgerichtshof bei einem gefälschten Examenszeugnis. [beglaub]Denn der Beglaubigungsvermerk bestätigt nur, dass "
     "die Kopie mit der Vorlage übereinstimmt. [collage]Die Grenze ist die Collage: Legt jemand Teile echter Urkunden nur "
     "lose zusammen und kopiert sie, entsteht kein gefälschtes Original, von dem die Kopie Gebrauch machen könnte.", PS),
    # --- F Datei: § 269 ----------------------------------------------------------------------------------------------------
    ("[datei]Jetzt zum Scan. Eine PDF-Datei ist nicht auf einer Sache verkörpert. Für Dateien und E-Mails gilt deshalb "
     "nicht Paragraf zweihundertsiebenundsechzig, [p269]sondern Paragraf zweihundertneunundsechzig: [w269]Strafbar ist, "
     "wer zur Täuschung im Rechtsverkehr beweiserhebliche Daten so speichert oder verändert, dass bei ihrer Wahrnehmung "
     "eine unechte oder verfälschte Urkunde vorliegen würde, oder solche Daten gebraucht. [hyp]Du prüfst also "
     "hypothetisch: Stell dir die Daten als verkörperte Erklärung vor. Läge dann eine unechte oder verfälschte Urkunde "
     "vor?", PS),
    # --- G Scan oder digitales Original: der Streit beim PDF ---------------------------------------------------------------
    ("[bgh]Der Bundesgerichtshof unterscheidet: [scanfall]Wird ein echtes Papierdokument eingescannt und verändert, "
     "verliert es schon durch den Scan seine Urkundenqualität. Das Bild ist zwar ein Datum, aber keine Datenurkunde des "
     "Ausstellers. [digorig]Anders, wenn ein Dokument von Haus aus digital ist, etwa eine Online-Überweisungsbestätigung, "
     "und verändert oder komplett am Rechner gefälscht wird. Dann kommt Paragraf zweihundertneunundsechzig in Betracht. "
     "[olg]Für Zeugnisse als E-Mail-Anhang hat das Oberlandesgericht Celle entschieden: Zeugnisse werden üblicherweise "
     "auf Papier ausgegeben, ein PDF erscheint deshalb erkennbar nur als Reproduktion. [gegen]Wer Kopien grundsätzlich "
     "für Urkunden hält, kommt dagegen auch hier zu Paragraf zweihundertneunundsechzig. [p270]Liest zuerst nur ein "
     "Bewerbungsprogramm die Datei, hilft Paragraf zweihundertsiebzig: Der Täuschung im Rechtsverkehr steht die "
     "fälschliche Beeinflussung einer Datenverarbeitung im Rechtsverkehr gleich.", PS),
    # --- H Lösung ----------------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [l1]Das PDF ist keine verkörperte Erklärung, Paragraf zweihundertsiebenundsechzig scheidet aus. "
     "[l2]Nach Paragraf zweihundertneunundsechzig zeigt es erkennbar nur den Scan eines Papierzeugnisses, also eine "
     "Kopie. Mit der herrschenden Meinung ist auch dieser Tatbestand nicht erfüllt. [l3]Anders wäre es, wenn das "
     "Zeugnis als digitales Original ausgegeben würde. [l4]In der Variante kommt es auf den Ausdruck an. Als Kopie "
     "verschickt, erscheint er als Reproduktion. Eine Urkunde wäre er nur, wenn er wie ein Original aussähe, mit den "
     "typischen Echtheitsmerkmalen. [l5]Und in beiden Varianten fehlt ein gefälschtes Papierzeugnis, das Janosch über "
     "die Kopie gebrauchen könnte. [betrug]Bleibt der Betrug: Wird Janosch eingestellt, kommt Anstellungsbetrug in "
     "Betracht. Ein Schaden liegt aber nur vor, wenn seine Arbeitsleistung weniger wert ist als das Gehalt.", PS),
    # --- I Merktabelle -----------------------------------------------------------------------------------------------------
    ("[tab]Deine Merktabelle. [t1]Das Original auf Papier ist eine Urkunde, Paragraf zweihundertsiebenundsechzig. [t2]Die "
     "Kopie ist keine, außer sie erscheint als Original. [t2b]Wer ein gefälschtes Original kopiert, gebraucht das "
     "Original. [t3]Der Scan ist eine Datei: Paragraf zweihundertneunundsechzig nur, wenn sie als Original auftritt, nicht "
     "als bloße Wiedergabe.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag nicht nur, was gefälscht wurde, sondern was beim Empfänger ankommt. [tipp2]Ein Original "
     "oder erkennbar eine Wiedergabe? [tipp3]Und prüfe bei jeder Kopie, ob dahinter ein gefälschtes Original steht.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Kopie ist keine Urkunde, solange sie wie eine Kopie aussieht. [m2]Und Paragraf "
     "zweihundertneunundsechzig schützt digitale Originale, nicht ihre Abbilder.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
