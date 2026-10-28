"""Folge 151 · Durchsuchung StPO: Wann darf die Polizei in meine Wohnung? (Mo · Der Fall · Strafrecht/StPO, Format Schema).
Fall nach dem Plan-Hook („Nachts klingelt die Polizei ohne Beschluss und will wegen ‚Gefahr im Verzug‘ die Wohnung
durchsuchen“): Dienstag, 23 Uhr. Polizeikommissar Steiger klingelt bei Helene und will wegen Gefahr im Verzug ohne Beschluss
durchsuchen (Verdacht der Hehlerei mit gestohlenen Fahrrädern). Schon um 14 Uhr war angezeigt worden, dass ein gestohlenes
E-Bike online angeboten wird, Abholadresse: Helenes Wohnung; unter demselben Konto wurden in drei Wochen sieben teure Räder
angeboten. Einen Richter hat Steiger nicht zu erreichen versucht, obwohl der Bereitschaftsdienst bis 21 Uhr erreichbar war;
nichts deutet darauf hin, dass Helene von den Ermittlungen weiß. Helene widerspricht, tritt aber zur Seite (keine Gewalt,
keine Waffen); im Flur steht das E-Bike.
Prüfung: Art. 13 Abs. 1, 2 GG (Wortlautkarte; Verweis Folge 020) → § 102 StPO (Wortlautkarte; Anfangsverdacht nach BGH StB 40/23
Rn. 11), Kontrast § 103 Abs. 1 S. 1 (StB 40/23 Rn. 14) → § 105 Abs. 1 S. 1 StPO (Wortlautkarte; § 152 GVG) → Gefahr im Verzug
nach BVerfGE 103, 142 (Rn. 32, 34, 38, 39, 40, 44, 54) und BVerfGE 151, 67 (2 BvR 675/14, Rn. 58) → Nachtzeit § 104 StPO
(Wortlautkarte Abs. 1 und 3; 2 BvR 675/14 Rn. 62) → Lösung → Verwertungsverbot (BGHSt 51, 285 = 5 StR 546/06, Leitsatz,
Rn. 17, 24, 26, 28 f.; BGHSt 61, 266 = 2 StR 46/15 Rn. 24, 26; Verweis Folge 132) → Klausurtipp → Schema → Merksatz.
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Helene, Steiger
(nie im Genitiv). Stimmen nur aus dem Pool: Helene lucy (Frau, jung), Steiger stephan (Mann, mittel); christian nicht
verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Helene": "lucy", "Steiger": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: an der Wohnungstür, 23 Uhr -------------------------------------------------------------------------------
    ("[fall]Dienstag, dreiundzwanzig Uhr, ein Mietshaus. [klingel]Bei Helene klingelt es. [tuer]Vor der Tür steht "
     "Polizeikommissar Steiger.", 0.3),
    ("[st1]Wir haben den Verdacht, dass Sie gestohlene Fahrräder verkaufen. Wegen Gefahr im Verzug durchsuche ich "
     "jetzt Ihre Wohnung.", 0.3, "Steiger"),
    ("[h1]Jetzt, mitten in der Nacht? Wo ist denn Ihr Beschluss?", 0.3, "Helene"),
    ("[st2]Den brauche ich nicht. Bis morgen könnten die Räder weg sein.", 0.4, "Steiger"),
    # --- A2 Fall: Rückblick, 14 Uhr auf der Wache ---------------------------------------------------------------------------
    ("[weiss]Was Helene nicht weiß: [mittag]Schon um vierzehn Uhr hatte ein Mann angezeigt, dass sein gestohlenes E-Bike im "
     "Internet angeboten wird. [abhol]Als Abholadresse ist die Wohnung von Helene angegeben. [sieben]Über dasselbe Konto "
     "wurden in drei Wochen sieben teure Räder angeboten. [keinr]Um einen Beschluss hat sich Steiger nicht bemüht, obwohl der "
     "Bereitschaftsdienst bis einundzwanzig Uhr erreichbar war. [ahnt]Und nichts deutet darauf hin, dass Helene von den "
     "Ermittlungen weiß.", 0.3),
    # --- A3 Fall: zurück an der Tür ---------------------------------------------------------------------------------------
    ("[wider]Helene widerspricht, tritt aber zur Seite. [flur]Im Flur steht das E-Bike.", 0.3),
    ("[frage]Durfte Steiger die Wohnung durchsuchen? [frage2]Und darf das Gericht das E-Bike als Beweis verwerten?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Art. 13 GG (Wortlautkarte) -----------------------------------------------------------------------------------
    ("[art13]Ausgangspunkt ist Artikel dreizehn Grundgesetz: Die Wohnung ist unverletzlich. [abs2]Durchsuchungen dürfen nur "
     "durch den Richter angeordnet werden, [giv]bei Gefahr im Verzuge auch durch die in den Gesetzen vorgesehenen anderen "
     "Organe. [regel]Die richterliche "
     "Anordnung ist die Regel, die nichtrichterliche die Ausnahme. [gr020]Das Grundrechtsschema zeigt "
     "unsere Folge zur Grundrechtsprüfung.", PS),
    # --- D 2. Ermächtigungsgrundlage: § 102, Kontrast § 103 -----------------------------------------------------------------
    ("[p102]Die Ermächtigungsgrundlage: [verd]Paragraf hundertzwei erlaubt die Durchsuchung "
     "bei dem, der als Täter oder Teilnehmer einer Straftat oder etwa der Hehlerei verdächtig ist, [vermut]wenn zu vermuten ist, "
     "dass sie zur Auffindung von Beweismitteln führen werde. [anf]Es genügt ein Anfangsverdacht: ein konkreter Verdacht, "
     "gestützt auf bestimmte tatsächliche Anhaltspunkte. [hier102]Hier sind das die Anzeige, das Inserat und die "
     "Abholadresse. [auff]Dass das E-Bike in der Wohnung steht, liegt nahe.", P),
    ("[p103]Strenger ist Paragraf hundertdrei bei anderen Personen: [p103b]Dort braucht es Tatsachen, aus denen zu schließen "
     "ist, dass sich die gesuchte Sache in den Räumen befindet.", PS),
    # --- E 3. Anordnungskompetenz: § 105 (Wortlautkarte) ---------------------------------------------------------------------
    ("[p105]Wer darf anordnen? Paragraf hundertfünf Absatz eins Satz eins: Durchsuchungen dürfen nur durch den Richter, "
     "[p105b]bei Gefahr im Verzug auch durch die Staatsanwaltschaft und ihre Ermittlungspersonen angeordnet werden. "
     "[kompet]Steiger ist Ermittlungsperson; ohne Beschluss durfte er also nur bei Gefahr im Verzug durchsuchen.", PS),
    # --- F 4. Gefahr im Verzug: BVerfGE 103, 142 ---------------------------------------------------------------------------
    ("[bverfg]Die Leitentscheidung: Bundesverfassungsgericht, zweitausendeins. "
     "[eng]Gefahr im Verzug ist eng auszulegen. [def]Sie liegt nur vor, wenn schon die vorherige Einholung der richterlichen "
     "Anordnung den Erfolg der Durchsuchung gefährden würde. [tats]Das muss mit Tatsachen des Einzelfalls begründet werden. "
     "Reine Spekulationen oder fallunabhängige Vermutungen aus kriminalistischer Alltagserfahrung reichen nicht. "
     "[versuch]Regelmäßig müssen die Ermittler zuerst versuchen, einen Richter zu erreichen. [doku]Ihre Gründe müssen sie in den "
     "Akten dokumentieren, [kontr]und die Gerichte kontrollieren die Annahme von Gefahr im Verzug in vollem Umfang.", P),
    ("[selbst]Und Gefahr im Verzug entsteht nicht dadurch, dass die Behörden sie selbst "
     "herbeiführen: [zuw]Sie dürfen mit dem Antrag nicht warten, bis ein Beweismittelverlust tatsächlich droht.", P),
    ("[bereit]Dafür müssen die Gerichte einen Ermittlungsrichter erreichbar halten, auch durch einen "
     "Bereitschaftsdienst. [tag]Zweitausendneunzehn präzisierte das Gericht: Tagsüber, ganzjährig von "
     "sechs bis einundzwanzig Uhr, muss ein Ermittlungsrichter uneingeschränkt erreichbar sein. [nacht]Nachts ist ein "
     "Bereitschaftsdienst jedenfalls dann einzurichten, wenn der Bedarf über den Ausnahmefall hinausgeht.", PS),
    # --- G 5. Nachtzeit: § 104 (Wortlautkarte) ------------------------------------------------------------------------------
    ("[p104]Dazu kommt die Nachtzeit, Paragraf hundertvier. [nachtz]Sie umfasst den Zeitraum von einundzwanzig bis sechs Uhr. "
     "[p104b]Nachts dürfen Wohnungen nur in Ausnahmefällen durchsucht werden, etwa bei Verfolgung auf frischer Tat, bei Gefahr "
     "im Verzug [p104c]oder zur Wiederergreifung eines entwichenen Gefangenen. [ngiv]Gefahr im Verzug heißt hier: Schon das "
     "Warten bis zum Morgen würde den Erfolg wahrscheinlich gefährden.", PS),
    # --- H 6. Lösung -----------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Helene. [l102]Ein Anfangsverdacht nach Paragraf hundertzwei liegt vor, und bei sieben Rädern wäre eine "
     "Durchsuchung wohl auch verhältnismäßig. [lgiv]Aber Gefahr im Verzug? [lspek]Dass die Räder bis morgen weg sein könnten, ist "
     "eine bloße Vermutung. [lselbst]Und die Eile hat Steiger "
     "selbst herbeigeführt: Seit vierzehn Uhr hätte er über die Staatsanwaltschaft einen Richter erreichen können. "
     "[lneg]Gefahr im Verzug liegt nicht vor. [lnacht]Damit fehlt auch die Ausnahme für die Nachtzeit. [lerg]Die "
     "Durchsuchung war rechtswidrig.", PS),
    # --- I 7. Verwertungsverbot ------------------------------------------------------------------------------------------
    ("[bvv]Ist das E-Bike deshalb als Beweis verloren? [nichtj]Nicht jeder Fehler führt zu einem Verwertungsverbot; "
     "abzuwägen ist im Einzelfall. [bewusst]Der Bundesgerichtshof nimmt es aber an, wenn der Richtervorbehalt bewusst "
     "missachtet oder gleichgewichtig grob verkannt wurde. [stunden]So entschied er zweitausendsieben, als über Stunden "
     "niemand an einen Richter gedacht hatte. [hier]Bei Steiger spricht deshalb viel für ein "
     "Verwertungsverbot. [hypo]Dann hilft auch der Einwand nicht, ein Richter hätte den Beschluss ohnehin erlassen. "
     "[f132]Mehr dazu in unserer Folge zur Widerspruchslösung.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne sauber. [tipp1]Die Ermächtigungsgrundlage sagt, ob durchsucht werden darf, [tipp2]Paragraf "
     "hundertfünf, wer anordnen darf. [tipp3]Und prüfe Gefahr im Verzug zu dem Zeitpunkt, zu dem die Polizei die Durchsuchung "
     "für erforderlich hielt, nicht erst an der Haustür.", PS),
    # --- K Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Durchsuchung. [s1]Erstens: Ermächtigungsgrundlage, Paragraf hundertzwei beim Verdächtigen "
     "oder hundertdrei bei Dritten, [s1b]mit Anfangsverdacht und Auffindevermutung. [s2]Zweitens: Anordnungskompetenz, "
     "grundsätzlich der Richter. [s3]Drittens, ohne Beschluss: Gefahr im Verzug, auf Tatsachen gestützt, nicht selbst "
     "herbeigeführt und dokumentiert. [s4]Viertens: die Nachtzeit nach Paragraf hundertvier. [s5]Fünftens: "
     "Verhältnismäßigkeit. [s6]Und bei einem Verstoß: Verwertungsverbot nur bei bewusster oder grober Missachtung.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Durchsuchung ordnet der Richter an. [m2]Gefahr im Verzug ist die Ausnahme, und wer die Eile selbst "
     "herbeiführt, kann sich nicht auf sie berufen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
