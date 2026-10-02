"""Folge 085 · Außenbereich § 35 BauGB: Warum dein Ferienhaus im Wald verboten ist (Mo · Der Fall · Öffentliches Recht/
Baurecht). Übungsfall nach dem Hook des Themenplans: Frau Wiesner kauft ein Waldgrundstück weit draußen vor dem Dorf und
beantragt die Genehmigung für ein kleines Wochenendhaus. Kein Bebauungsplan, Flächennutzungsplan stellt Wald dar.
Herr Dreher von der Bauaufsichtsbehörde lehnt ab.
Kern: zwei Ebenen (Bauplanungsrecht BauGB / Bauordnungsrecht der Länder, ein Satz), I. Vorhaben § 29 I, II. Bereich
(§ 30 – § 34 – § 35; BVerwG 4 C 10.11 Rn. 11), III. privilegiert § 35 I (Nr. 1, Nr. 5 nur genannt, Nr. 4 verneint,
§ 10 BauNVO; BVerwG 4 C 10.11 Rn. 20), IV. sonstiges Vorhaben § 35 II (Wortlautkarte): 1. öffentliche Belange § 35 III 1
(Wortlautkarte, Nr. 1, 5, 7; Splittersiedlung BVerwG 4 C 10.11 Rn. 19, 21, 22), 2. § 35 IV (ein Satz), 3. Erschließung;
Ergebnis; Waldrecht (§ 9 I 1 BWaldG, ein Satz); Rechtsschutz (Verpflichtungsklage, Verweis Klagearten, ein Satz);
Klausurtipp, Schema, Merksatz (Lexi). Fiktive Figuren: Frau Wiesner (laura_ruhig), Herr Dreher (william).
Belege je Aussage: RECHTSSTAND.md. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Wiesner": "laura_ruhig", "Dreher": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Waldgrundstück ----------------------------------------------------------------------------------------
    ("[fall]Frau Wiesner hat ein Waldgrundstück gekauft, weit draußen vor dem Dorf, mitten im Fichtenwald. [plan]Dort will "
     "sie ein kleines Wochenendhaus bauen, für ruhige Tage im Grünen.", 0.2),
    ("[wi1]Hier baue ich mir mein Wochenendhaus. Nur ich, die Bäume und die Ruhe.", 0.3, "Wiesner"),
    # --- B Fall: Bauantrag und Ablehnung -----------------------------------------------------------------------------------
    ("[antrag]Sie stellt einen Bauantrag. [dreher]Herr Dreher von der Bauaufsichtsbehörde prüft ihn. [lage]Einen "
     "Bebauungsplan gibt es dort nicht, und der Flächennutzungsplan der Gemeinde stellt die Fläche als Wald dar.", 0.2),
    ("[dr1]Frau Wiesner, ein Wochenendhaus mitten im Wald darf ich nicht genehmigen. Ich lehne Ihren Antrag ab.", 0.3, "Dreher"),
    ("[wi2]Aber es ist doch mein Grundstück! Und das Haus ist ganz klein.", 0.3, "Wiesner"),
    ("[frage]War die Ablehnung rechtmäßig?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Zwei Ebenen, I. Vorhaben ------------------------------------------------------------------------------------------
    ("[ebenen]Zuerst die zwei Ebenen des Baurechts. Das Bauplanungsrecht im Baugesetzbuch regelt, ob ein Vorhaben an diesem "
     "Ort zulässig ist; [ordnung]das Bauordnungsrecht deines Landes regelt das Genehmigungsverfahren und die Sicherheit des "
     "Baus. [vorh]Erstens, das Vorhaben: Das Wochenendhaus ist die Errichtung einer baulichen Anlage nach Paragraf "
     "neunundzwanzig. [gelten]Damit gelten die Paragrafen dreißig bis siebenunddreißig.", P),
    # --- E II. Bereich -------------------------------------------------------------------------------------------------------
    ("[reihe]Zweitens, der Bereich, immer in dieser Reihenfolge. [p30]Gilt ein Bebauungsplan nach Paragraf dreißig? Hier "
     "nicht. [p34]Liegt das Grundstück in einem im Zusammenhang bebauten Ortsteil, also im Innenbereich nach Paragraf "
     "vierunddreißig? Auch nicht, rundherum steht nur Wald. [p35]Also liegt es im Außenbereich: Paragraf fünfunddreißig.", P),
    # --- F III. Privilegiert? ------------------------------------------------------------------------------------------------
    ("[abs1]Drittens: Ist das Vorhaben privilegiert? Absatz eins zählt privilegierte Vorhaben auf, [nr1]etwa Gebäude, die "
     "einem land- oder forstwirtschaftlichen Betrieb dienen, Nummer eins, [nr5]oder Vorhaben der Windenergie, Nummer fünf. "
     "[entg]Sie sind zulässig, wenn öffentliche Belange nicht entgegenstehen und die Erschließung gesichert ist. Das Gesetz "
     "bevorrechtigt sie im Außenbereich.", P),
    ("[kein1]Das Wochenendhaus dient keinem Betrieb: Frau Wiesner betreibt keine Forstwirtschaft, sie will sich erholen. "
     "[nr4]Auch Nummer vier passt nicht. Ein Wochenendhaus muss nicht im Außenbereich stehen; dafür kann die Gemeinde eigene "
     "Wochenendhausgebiete planen. [sonst]Es ist also ein sonstiges Vorhaben.", P),
    # --- G IV. Sonstiges Vorhaben, § 35 II -------------------------------------------------------------------------------------
    ("[wl352]Viertens, Absatz zwei: Sonstige Vorhaben können im Einzelfall zugelassen werden, wenn ihre Ausführung oder "
     "Benutzung öffentliche Belange nicht beeinträchtigt und die Erschließung gesichert ist. [streng]Das ist strenger als "
     "bei Absatz eins: Die Zulassung scheitert schon, wenn ein Belang beeinträchtigt ist.", P),
    # --- H 1. Öffentliche Belange, § 35 III 1 --------------------------------------------------------------------------------
    ("[wl353]Welche Belange gemeint sind, zeigt Absatz drei mit Beispielen. [fnp]Nummer eins: Das Vorhaben widerspricht den "
     "Darstellungen des Flächennutzungsplans. Der Plan stellt hier Wald dar, kein Bauland für Wochenendhäuser. [land]Nummer "
     "fünf: Es beeinträchtigt die natürliche Eigenart der Landschaft. Im Fichtenwald, der forstlich genutzt wird, ist ein "
     "Wochenendhaus ein Fremdkörper.", P),
    ("[split]Und Nummer sieben: Es lässt die Entstehung einer Splittersiedlung befürchten, also einer bloßen Anhäufung von "
     "Gebäuden, die kein Ortsteil ist. [vorbild]Das Waldstück ist in viele Parzellen geteilt. Wer nebenan kauft, könnte sich "
     "auf ihr Haus berufen; so beginnt die Zersiedlung. [beein]Öffentliche Belange sind beeinträchtigt.", P),
    # --- I 2. § 35 IV, 3. Erschließung, Ergebnis ------------------------------------------------------------------------------
    ("[abs4]Hilft Absatz vier? Er begünstigt nur bestimmte Vorhaben, etwa die Umnutzung alter Hofgebäude oder den "
     "Wiederaufbau eines abgebrannten Gebäudes. Ein neues Wochenendhaus gehört nicht dazu. [erschl]Auf die Erschließung kommt "
     "es nicht mehr an. [erg]Das Wochenendhaus ist unzulässig, die Ablehnung war rechtmäßig.", PS),
    # --- J Zurück im Wald: Waldrecht, Rechtsschutz ------------------------------------------------------------------------------
    ("[wald]Dazu kommt das Waldrecht: Wald darf nur mit Genehmigung gerodet und anders genutzt werden. [klage]Gegen die "
     "Ablehnung könnte Frau Wiesner Verpflichtungsklage erheben, mehr dazu im Video zu den Klagearten. Erfolg hätte sie "
     "nicht.", 0.3),
    ("[wi3]Dann bleibt mein Wald eben ein Wald.", PS, "Wiesner"),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Diese Prüfung steht in der Begründetheit, bei der Frage, ob die Baugenehmigung erteilt werden muss. "
     "[tipp1]Bestimme dort zuerst den Bereich, dann die Gruppe. [tipp2]Und der Katalog in Absatz drei ist nicht abschließend, "
     "das Gesetz sagt: insbesondere.", PS),
    # --- L Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Erstens, Vorhaben nach Paragraf neunundzwanzig. [s2]Zweitens, Außenbereich: kein "
     "Bebauungsplan, kein Innenbereich. [s3]Drittens, privilegiert nach Absatz eins? [s4]Wenn nicht, viertens, sonstiges "
     "Vorhaben nach Absatz zwei: [s5]öffentliche Belange nach Absatz drei, [s6]Begünstigung nach Absatz vier, "
     "[s7]Erschließung.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei privilegierten Vorhaben fragst du, ob öffentliche Belange entgegenstehen. [m2]Ein Wochenendhaus "
     "ist ein sonstiges Vorhaben: Es scheitert schon, wenn es einen einzigen öffentlichen Belang beeinträchtigt.", 1.4),
]
