"""Folge 073 · Bereicherungsrecht Überblick: Welche Kondiktion wann? (§ 812 BGB) (Mo · Der Fall · Zivilrecht/
Bereicherungsrecht, Format Schema). Beispielfall nach dem Plan-Hook („Du überweist versehentlich 500 Euro an eine völlig
fremde Person“): Ursula will ihrem Maler 500 € überweisen, vertauscht beim Eintippen der IBAN zwei Ziffern; das Geld
landet auf dem Konto des fremden Rüdiger. Er weiß, dass es nicht für ihn ist, behält es und gibt es für ein Wochenende am
See aus. Auf Ursulas Bitte um Rückzahlung: „Das Geld ist schon weg.“
Kern: Wortlautkarte § 812 I (vorgelesen), Leistungsbegriff (BGH III ZR 291/11 Rn. 24, VIII ZR 39/17 Rn. 17), Entscheidungsbaum
(Vorrang der Leistungskondiktion, I ZR 187/10 Rn. 46), vier Leistungskondiktionen je ein Satz, Ausschlüsse §§ 814, 817 S. 2
ein Satz, Eingriffskondiktion (IX ZR 204/11 Rn. 15; Bildbeispiel I ZR 120/19 Rn. 26), § 816 ein Satz, Rückgriffs-/
Verwendungskondiktion genannt; Fall: Leistung der Überweisenden bei versehentlicher Fehlüberweisung (IX ZR 164/14 Rn. 8, 10;
§ 675r I), condictio indebiti; Ausblick Bankdreieck (XI ZR 243/13 Rn. 18, 24); Rechtsfolge § 818 I, II, III, §§ 819 I,
818 IV (XII ZR 102/09 Rn. 55), § 822 ein Satz; Klausurtipp, Schema, Merksatz.
Figuren: Ursula (hilde), Rüdiger (stephan); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. „Kondiktio“ ist die lautliche Schreibweise für „condictio“ (Nachvertonung
der Segmente 12 und 17: beide Erkennungsmodelle hörten „Konditio/Kondizio“ ohne k); Tafeln und Untertitel schreiben „condictio“."""

P, PS = 0.4, 0.6

STIMMEN = {"Ursula": "hilde", "Rüdiger": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Fehlüberweisung ------------------------------------------------------------------------------------
    ("[fall]Ursula will ihrem Maler fünfhundert Euro für seine Rechnung überweisen. [ziff]Beim Eintippen der IBAN "
     "vertauscht sie zwei Ziffern. [weg]Das Geld landet auf dem Konto von Rüdiger, einem völlig Fremden.", 0.3),
    ("[rd1]Fünfhundert Euro? Die sind gar nicht für mich. Egal, die behalte ich!", 0.3, "Rüdiger"),
    ("[see]Noch am selben Tag gibt er das Geld für ein Wochenende am See aus. [anruf]Zwei Tage später bemerkt Ursula "
     "den Fehler und ruft ihn an.", 0.3),
    ("[ur1]Ich habe mich bei der IBAN vertippt! Bitte überweisen Sie mir die fünfhundert Euro zurück.", 0.3, "Ursula"),
    ("[rd2]Tut mir leid, das Geld ist schon weg.", 0.4, "Rüdiger"),
    ("[frage]Kann Ursula das Geld trotzdem zurückverlangen? [frage2]Und welche Kondiktion passt?", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 812 I (Wortlaut) -----------------------------------------------------------------------------------------------
    ("[norm]Die Antwort beginnt bei Paragraf achthundertzwölf Absatz eins: [w812]Wer durch die Leistung eines anderen "
     "oder in sonstiger Weise auf dessen Kosten etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe verpflichtet. "
     "[w812b]Diese Verpflichtung besteht auch dann, wenn der rechtliche Grund später wegfällt oder der mit einer Leistung "
     "nach dem Inhalt des Rechtsgeschäfts bezweckte Erfolg nicht eintritt.", P),
    ("[typen]Darin stecken zwei Grundtypen: [lk]die Leistungskondiktion [nlk]und die Nichtleistungskondiktion, also die "
     "Bereicherung in sonstiger Weise.", PS),
    # --- D Leistungsbegriff und Entscheidungsbaum ----------------------------------------------------------------------------
    ("[lb]Die Weiche ist der Leistungsbegriff. [lb2]Leistung ist nach dem Bundesgerichtshof die bewusste und "
     "zweckgerichtete Mehrung fremden Vermögens. [ehz]Sehen die Beteiligten den Zweck verschieden, entscheidet die Sicht "
     "eines vernünftigen Empfängers.", P),
    ("[baum]Daraus folgt der Entscheidungsbaum. [b1]Erste Frage: Hat der Empfänger das Erlangte durch eine Leistung "
     "bekommen? [bja]Wenn ja, prüfst du die Leistungskondiktion. [bnein]Wenn nein, die Nichtleistungskondiktion. "
     "[vorrang]Denn sie kommt nur in Betracht, wenn der Gegenstand dem Empfänger nicht geleistet worden ist: Die "
     "Leistungskondiktion hat Vorrang.", PS),
    # --- E Leistungskondiktionen --------------------------------------------------------------------------------------------
    ("[lks]Auf dem Leistungsast gibt es vier Kondiktionen. [ci]Fehlt der Rechtsgrund von Anfang an, greift Paragraf "
     "achthundertzwölf Absatz eins Satz eins, erste Alternative, die Kondiktio indebiti. [ocf]Fällt er später weg, etwa "
     "durch eine auflösende Bedingung, die Kondiktio ob causam finitam aus Satz zwei, erste Alternative. [orem]Bleibt ein "
     "vereinbarter Zweck der Leistung aus, die Kondiktio ob rem aus Satz zwei, zweite Alternative. [p817]Und verstößt der "
     "Empfänger gerade durch die Annahme gegen ein gesetzliches Verbot oder die guten Sitten, greift Paragraf "
     "achthundertsiebzehn Satz eins.", P),
    ("[aus]Ausgeschlossen ist die Rückforderung nach Paragraf achthundertvierzehn, wenn der Leistende wusste, dass er "
     "nicht verpflichtet war, [aus2]und nach Paragraf achthundertsiebzehn Satz zwei, wenn ihm selbst ein solcher Verstoß "
     "zur Last fällt.", PS),
    # --- F Nichtleistungskondiktionen ---------------------------------------------------------------------------------------
    ("[nls]Auf dem anderen Ast ist der Hauptfall die Eingriffskondiktion, Paragraf achthundertzwölf Absatz eins Satz eins, "
     "zweite Alternative. [zw]Jemand greift in ein Recht ein, das einem anderen zur ausschließlichen Verwertung "
     "zugewiesen ist. [foto]Beispiel: Ein Unternehmen wirbt ohne Erlaubnis mit deinem Bild. Es schuldet grundsätzlich die "
     "übliche Lizenzgebühr.", P),
    ("[p816]Ein Sonderfall ist Paragraf achthundertsechzehn: Verfügt ein Nichtberechtigter wirksam über einen fremden "
     "Gegenstand, muss er dem Berechtigten herausgeben, was er durch die Verfügung erlangt hat. [rv]Daneben gibt es noch "
     "die Rückgriffskondiktion und die Verwendungskondiktion.", PS),
    # --- G Lösung des Falls ------------------------------------------------------------------------------------------------
    ("[fl]Zurück zu Ursula. [erl]Rüdiger hat etwas erlangt: die Gutschrift über fünfhundert Euro, also einen Anspruch "
     "gegen seine Bank. [auftr]Ursula hat die Überweisung selbst in Auftrag gegeben, und die Banken durften sich nach "
     "Paragraf sechshundertfünfundsiebzig r an die IBAN halten. [bgh]Eine solche versehentliche Überweisung an den falschen "
     "Empfänger hat der Bundesgerichtshof als Leistung des Überweisenden behandelt.", P),
    ("[org]Einen Rechtsgrund gibt es nicht, denn Ursula schuldet Rüdiger nichts. [k814]Und sie wusste das nicht: Sie "
     "wollte ja ihren Maler bezahlen. [ci2]Also greift die Kondiktio indebiti.", PS),
    # --- G2 Ausblick Bankdreieck ---------------------------------------------------------------------------------------------
    ("[dreieck]Ein Ausblick auf das Bankdreieck: [ohne]Zahlt die Bank ohne wirksamen Auftrag, etwa auf eine gefälschte "
     "Überweisung, hat der Kontoinhaber nichts geleistet. [direkt]Dann kann die Bank den Betrag direkt beim Empfänger "
     "herausverlangen, mit der Nichtleistungskondiktion.", PS),
    # --- H Rechtsfolge §§ 818 ff. ------------------------------------------------------------------------------------------
    ("[rf]Bleibt die Rechtsfolge. [rf1]Herauszugeben ist das Erlangte, nach Paragraf achthundertachtzehn Absatz eins auch "
     "gezogene Nutzungen. [rf2]Ist die Herausgabe nicht möglich, schuldet der Empfänger nach Absatz zwei den Wert, so wie "
     "die Lizenzgebühr für das Bild.", P),
    ("[rf3]Rüdiger beruft sich auf Absatz drei: Wer nicht mehr bereichert ist, muss nichts herausgeben und keinen Wert "
     "ersetzen. [rf4]Doch er wusste von Anfang an, dass ihm das Geld nicht zusteht. [rf5]Wer den fehlenden Rechtsgrund "
     "kennt, haftet nach Paragraf achthundertneunzehn Absatz eins so, als wäre der Anspruch rechtshängig, [rf6]und nach "
     "Paragraf achthundertachtzehn Absatz vier kann er sich dann nicht mehr auf den Wegfall der Bereicherung berufen.", P),
    ("[p822]Übrigens: Wendet ein Empfänger das Erlangte unentgeltlich einem Dritten zu und wird er dadurch frei, muss nach "
     "Paragraf achthundertzweiundzwanzig der Dritte herausgeben. [erg]Ergebnis: Rüdiger muss Ursula die fünfhundert Euro "
     "zurückzahlen, das Wochenende am See hilft ihm nicht.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe immer zuerst die Leistungskondiktion. [tipp1]Frage dafür ausdrücklich: Wer hat aus Sicht "
     "des Empfängers an wen geleistet? [tipp2]Erst wenn keine Leistung vorliegt, gehst du zur Nichtleistungskondiktion.", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins, Leistungskondiktion: etwas erlangt, durch Leistung, ohne rechtlichen "
     "Grund, kein Ausschluss nach den Paragrafen achthundertvierzehn und achthundertsiebzehn Satz zwei. [k2]Römisch zwei, "
     "nur ohne Leistung: Nichtleistungskondiktion, etwas in sonstiger Weise auf Kosten des Anspruchstellers erlangt, ohne "
     "rechtlichen Grund.", P),
    ("[k3]Römisch drei: Rechtsfolge nach den Paragrafen achthundertachtzehn folgende: Herausgabe oder Wertersatz, "
     "Entreicherung und verschärfte Haftung.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst fragen, ob geleistet wurde, dann die passende Kondiktion wählen. [m2]Und wer den fehlenden "
     "Rechtsgrund kennt, kann sich nicht auf Entreicherung berufen.", 1.4),
]
