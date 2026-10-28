"""Folge 030 · Schlüssigkeitsprüfung: Der Test, den jede Klage bestehen muss (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall: Frau Schubert leiht ihrem Nachbarn Herrn Franke 6.000 Euro und überweist sie; mündlich ist Rückzahlung bis
Ende Juni vereinbart. Franke zahlt nicht. In der Klageschrift steht nur: Darlehen, Überweisung, „Das Darlehen ist fällig.“
Rückzahlungstermin und Kündigung fehlen im Vortrag → unschlüssig (§ 488 I 2, III BGB); Hinweis nach § 139 ZPO, Ergänzung →
schlüssig. Dazu: BGH-Schlüssigkeitsformel (BGH, Beschl. v. 1.7.2025 – VI ZR 357/24, Rn. 10 f.), Substantiierung,
Abgrenzung zur Beweisstation, zur Zulässigkeit (§ 253 II Nr. 2 ZPO; BGH, Beschl. v. 4.7.2018 – VII ZR 21/16, Rn. 11),
Folge der Unschlüssigkeit (Abweisung als unbegründet), Versäumnisurteil § 331 I, II ZPO. Stationen = Ausbildungskonvention.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Schubert, Franke; Richterin ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Schubert": "lea", "Franke": "william", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Darlehen am Gartenzaun ------------------------------------------------------------------------------
    ("[fall]Frau Schubert leiht ihrem Nachbarn, Herrn Franke, sechstausend Euro. [ueberw]Im Januar überweist sie ihm "
     "das Geld.", 0.3),
    ("[f1]Danke! Ende Juni haben Sie alles zurück.", 0.5, "Franke"),
    # --- B Fall: die Klageschrift ----------------------------------------------------------------------------------------
    ("[juli]Doch der Juli kommt, und Herr Franke zahlt nicht. [klage]Frau Schubert klagt vor dem Amtsgericht auf "
     "sechstausend Euro. [schrift]In ihrer Klageschrift steht nur:", 0.3),
    ("[s1]Ich habe mit dem Beklagten vereinbart, ihm sechstausend Euro zu leihen, und sie überwiesen. Das Darlehen ist fällig.", 0.5, "Schubert"),
    ("[frage]Besteht diese Klage den Test, den jede Klage bestehen muss? [frage2]Ist sie schlüssig?", 0.6),
    # --- C Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Die Formel ----------------------------------------------------------------------------------------------------
    ("[stat]Die Schlüssigkeit prüfst du in der Klägerstation. Die Stationen sind Ausbildungs- und Klausurkonvention. "
     "[test]Der Test lautet: Trägt der Vortrag der Klägerin, als wahr unterstellt, ihren Antrag? [formel]Der "
     "Bundesgerichtshof sagt es genauer: Schlüssig ist der Vortrag, wenn die Partei Tatsachen vorträgt, die in Verbindung mit einem Rechtssatz "
     "geeignet und erforderlich sind, das geltend gemachte Recht als in der Person der Partei entstanden erscheinen zu "
     "lassen.", PS),
    # --- E Schritt 1: Rechtssatz -------------------------------------------------------------------------------------------
    ("[rs]Erster Schritt: die Anspruchsgrundlage, also der Rechtssatz. Hier: Paragraf vierhundertachtundachtzig Absatz eins Satz zwei "
     "BGB. [rs2]Der Darlehensnehmer muss das Darlehen bei Fälligkeit zurückzahlen. [drei]Du brauchst also drei Merkmale: "
     "Darlehensvertrag, Auszahlung und Fälligkeit.", PS),
    # --- F Schritt 2: Tatsachen zuordnen -----------------------------------------------------------------------------------
    ("[tats]Zweiter Schritt: der Tatsachenvortrag. Ordne jedem Merkmal eine vorgetragene Tatsache zu. [m1]Vereinbart, ihm das Geld zu leihen: Das trägt "
     "den Darlehensvertrag. [m2]Überwiesen: Das trägt die Auszahlung. [m3]Und fällig? Das ist keine Tatsache, sondern eine "
     "rechtliche Bewertung. Als wahr unterstellt werden nur Tatsachen. [p488]Ist für die Rückzahlung keine Zeit bestimmt, "
     "wird das Darlehen erst durch Kündigung fällig, mit drei Monaten Frist, Absatz drei. [fehlt]Zu einem "
     "Rückzahlungstermin oder einer Kündigung schreibt Frau Schubert nichts. Die Klage ist unschlüssig.", PS),
    # --- G Hinweis § 139 ZPO -----------------------------------------------------------------------------------------------
    ("[hinw]Wird sie deshalb sofort abgewiesen? Nein. [hw]Dritter Schritt: der Hinweis. Nach Paragraf hundertneununddreißig Absatz eins ZPO wirkt das Gericht darauf "
     "hin, dass die Parteien ungenügende Angaben zu den geltend gemachten Tatsachen ergänzen. [frueh]Der Hinweis kommt "
     "so früh wie möglich und wird aktenkundig gemacht.", 0.3),
    ("[r1]Zur Fälligkeit fehlt Vortrag. Wann sollte das Geld zurückgezahlt werden?", 0.5, "Richterin"),
    ("[ergz]Frau Schubert ergänzt: Rückzahlung war bis Ende Juni vereinbart. [schl]Vierter Schritt, "
     "das Ergebnis: Jetzt trägt ihr Vortrag den Antrag. Die Klage ist schlüssig.", PS),
    # --- H Substantiierung -------------------------------------------------------------------------------------------------
    ("[subst]Muss sie auch sagen, an welchem Tag und wo die Abrede fiel? Nein. [einz]Nähere Einzelheiten sind nach dem "
     "Bundesgerichtshof nicht erforderlich, soweit sie für die Rechtsfolgen nicht von Bedeutung sind. [unter]Schlüssigkeit "
     "fragt, ob jedes Merkmal mit Tatsachen belegt ist. Substantiierung fragt, wie genau. Diese Anforderungen darf das "
     "Gericht nicht überspannen.", 0.3),
    # --- I Abgrenzung Beweisstation ----------------------------------------------------------------------------------------
    ("[f2]Von Juni war nie die Rede!", 0.5, "Franke"),
    ("[best]Das ist Bestreiten, ein Thema der Beklagtenstation. [bew]Ob die Abrede wahr ist, klärt erst die Beweisstation. "
     "Dort ist es nach dem Bundesgerichtshof Sache des Gerichts, benannte Zeugen nach weiteren Einzelheiten zu "
     "befragen.", PS),
    # --- J Abgrenzung Zulässigkeit ------------------------------------------------------------------------------------------
    ("[zul]Und die Zulässigkeit? Paragraf zweihundertdreiundfünfzig Absatz zwei Nummer zwei verlangt die bestimmte Angabe "
     "des Gegenstandes und des Grundes des erhobenen Anspruchs, sowie einen bestimmten Antrag. [ident]Dafür genügt, dass "
     "der Anspruch individualisierbar ist. Schlüssig muss er dafür nicht dargelegt sein, so der Bundesgerichtshof. "
     "[hier]Frau Schubert verlangt sechstausend Euro aus einem bestimmten Darlehen. Der Anspruch ist individualisiert. "
     "Es fehlte nicht an der Zulässigkeit, sondern an der Schlüssigkeit.", PS),
    # --- K Folge der Unschlüssigkeit, Versäumnisurteil -------------------------------------------------------------------
    ("[folge]Hätte sie nichts ergänzt, wäre die Klage abgewiesen worden, als unbegründet, nicht als unzulässig. [vu]Besonders "
     "deutlich wird das beim Versäumnisurteil. Erscheint Herr Franke nicht zum Termin und beantragt die Klägerin "
     "das Versäumnisurteil, ist ihr tatsächliches Vorbringen als zugestanden anzunehmen, Paragraf dreihunderteinunddreißig Absatz eins. "
     "[tatz]Zugestanden ist nur Tatsächliches, nicht das Wort fällig. [vu2]Nach Absatz zwei ergeht das "
     "Urteil nach dem Antrag nur, soweit das Vorbringen den Antrag rechtfertigt. Sonst ist die Klage abzuweisen, trotz "
     "Säumnis. [vu3]Ohne Ergänzung hätte Frau Schubert also selbst gegen den abwesenden Beklagten verloren.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Merkmal für Merkmal und nenne zu jedem die vorgetragene Tatsache. Wörter wie fällig oder "
     "grob pflichtwidrig ersetzen keine Tatsachen. [tipp2]Und trenne die Stationen: Ob der Vortrag stimmt, gehört erst in "
     "die Beweisstation.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Schlüssigkeit. [sI]Römisch eins: Anspruchsgrundlage und ihre Merkmale. [sII]Römisch zwei: "
     "Tatsachenvortrag zu jedem Merkmal, als wahr unterstellt. [sIII]Römisch drei: Fehlt etwas, Hinweis nach Paragraf "
     "hundertneununddreißig. [sIV]Römisch vier: Ergebnis. [sIVa]Schlüssig: weiter zur Beklagtenstation. [sIVb]Unschlüssig: "
     "Abweisung als unbegründet.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Schlüssig ist die Klage, wenn ihre Tatsachen, als wahr unterstellt, den Antrag tragen. [mz]Einzelheiten "
     "braucht es nur, soweit sie für die Rechtsfolge zählen.", 1.4),
]
