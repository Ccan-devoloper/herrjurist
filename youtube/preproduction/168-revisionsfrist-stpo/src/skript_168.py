"""Folge 168 · Revisionsfrist StPO: Einlegung, Begründung, Wiedereinsetzung (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall nach dem Plan-Hook („Das Urteil wurde an einem Montag verkündet, zugestellt wird es erst sieben Wochen später“):
Die Strafkammer des Landgerichts verurteilt Herrn Tiedemann am Montag, 18.5.2026, in seiner Anwesenheit wegen Betrugs. Seine
Verteidigerin, Rechtsanwältin Sternberg, legt am Dienstag, 26.5.2026 (Pfingstmontag 25.5. → § 43 Abs. 2), elektronisch Revision
ein. Das Urteil wird ihr am Montag, 6.7.2026, zugestellt (sieben Wochen nach der Verkündung); die Kanzlei notiert die
Begründungsfrist falsch (6.9. statt 6.8.2026). Am Montag, 10.8.2026, bemerkt sie den Fehler und unterrichtet Herrn Tiedemann;
am Mittwoch, 12.8.2026, beantragt sie Wiedereinsetzung und holt die Begründung nach.
Prüfung: Aufbau (Statthaftigkeit § 333 nur ein Satz, Verweis Folge 066) → Einlegung § 341 Abs. 1 (Wortlautkarte, vorgelesen),
Abs. 2 ein Satz → Form § 32d S. 2 (Wortlautkarte; seit 1.1.2022, Neufassung seit 1.1.2026; BGH 6 StR 268/22 Rn. 3) →
Fristberechnung § 43 Abs. 1, 2 (Wortlautkarten, Kalender Mai 2026) → Begründung § 345 Abs. 1 (Wortlautkarte; S. 2 nur als
Halbsatz) → Zustellung, Monatsfrist im Kalender (Juli/August 2026) → Form § 345 Abs. 2 (Wortlautkarte), Inhalt § 344 (ein Satz,
Verweis 066), Sprungrevision § 335 (ein Satz) → Kanzlei (Figurenrede) → Wiedereinsetzung §§ 44, 45 (Wortlautkarten) →
Verteidigerverschulden (BGH 6 StR 268/22 Rn. 4; 4 StR 134/26 Rn. 1; 6 StR 331/25 Rn. 5) → Grenze Verfahrensrügen
(BGH 5 StR 442/23 Rn. 6; 3 StR 368/25 Rn. 2) → Merktabelle → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Tiedemann, Sternberg
(nie im Genitiv). Stimmen: Herr Tiedemann william, Rechtsanwältin Sternberg laura_ruhig. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Tiedemann": "william", "Sternberg": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: im Sitzungssaal --------------------------------------------------------------------------------------------
    ("[fall]Ein Montag im Mai, Sitzungssaal des Landgerichts. [urteil]Die Strafkammer verurteilt Herrn Tiedemann wegen Betrugs "
     "zu einer Freiheitsstrafe. [anw]Er ist bei der Verkündung anwesend, neben ihm seine Verteidigerin, Rechtsanwältin "
     "Sternberg.", P),
    ("[ti1]Das Urteil ist falsch. Das nehme ich nicht hin.", P, "Tiedemann"),
    ("[st1]Dann legen wir Revision ein. Die Begründung folgt mit dem schriftlichen Urteil.", P, "Sternberg"),
    # --- A2 Fall: in der Kanzlei ---------------------------------------------------------------------------------------------
    ("[zust]Das schriftliche Urteil wird ihr erst sieben Wochen später zugestellt. [notiz]In der Kanzlei wird die Frist für "
     "die Begründung falsch eingetragen: [falsch]einen Monat zu spät.", P),
    ("[frage]Bis wann musste die Revision eingelegt und begründet werden? [frage2]Und was hilft Herrn Tiedemann, wenn die "
     "Frist versäumt ist?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau ------------------------------------------------------------------------------------------------------------
    ("[aufbau]Gegen das Urteil der Strafkammer ist die Revision nach Paragraf dreihundertdreiunddreißig statthaft; was sie "
     "prüft, zeigt das Video zu Sach- und Verfahrensrüge. [a1]Hier geht es um die Fristen: [a2]die Einlegung, [a3]die "
     "Begründung [a4]und die Wiedereinsetzung.", PS),
    # --- D Einlegung, § 341 StPO ---------------------------------------------------------------------------------------------
    ("[p341]Zuerst die Einlegung, Paragraf dreihunderteinundvierzig Absatz eins: Die Revision muss bei dem Gericht, dessen "
     "Urteil angefochten wird, binnen einer Woche nach Verkündung des Urteils zu Protokoll der Geschäftsstelle oder "
     "schriftlich eingelegt werden. [lg]Also beim Landgericht, nicht beim Bundesgerichtshof. [abw]War der Angeklagte bei der "
     "Verkündung nicht anwesend, beginnt die Frist nach Absatz zwei grundsätzlich erst mit der Zustellung.", P),
    # --- E Form: § 32d S. 2 StPO ---------------------------------------------------------------------------------------------
    ("[p32d]Schriftlich heißt für die Verteidigerin: elektronisch. [p32d2]Paragraf zweiunddreißig d Satz zwei: Die folgenden "
     "Dokumente müssen sie elektronisch übermitteln, unter Nummer zwei die Revision und ihre Begründung. [seit]Das gilt seit "
     "dem ersten Januar zweitausendzweiundzwanzig. [fax]Ein Fax der Verteidigerin ist nach dem Bundesgerichtshof unwirksam.", P),
    # --- F Fristberechnung, § 43 StPO ----------------------------------------------------------------------------------------
    ("[frist1]Wann endet die Woche? [p43]Nach Paragraf dreiundvierzig Absatz eins endet eine Wochenfrist am Tag mit derselben "
     "Benennung, eine Monatsfrist am Tag mit derselben Zahl. [mo]Verkündet am Montag, dem achtzehnten Mai, endet sie also am "
     "Montag, dem fünfundzwanzigsten Mai. [pfi]Das ist aber Pfingstmontag. [p432]Nach Absatz zwei endet die Frist dann mit "
     "Ablauf des nächsten Werktages, ebenso bei Sonnabend und Sonntag: [di]am Dienstag, dem sechsundzwanzigsten Mai. "
     "[rz]An diesem Dienstag legt Rechtsanwältin Sternberg elektronisch ein. Rechtzeitig.", PS),
    # --- G Begründungsfrist, § 345 Abs. 1 StPO -------------------------------------------------------------------------------
    ("[p345]Jetzt die Begründung, Paragraf dreihundertfünfundvierzig Absatz eins. [p345a]Die Revisionsanträge und ihre "
     "Begründung sind spätestens binnen eines Monats nach Ablauf der Frist zur Einlegung anzubringen. [p345c]Aber: War bei Ablauf der Einlegungsfrist das Urteil noch nicht zugestellt, so beginnt die Frist "
     "mit der Zustellung des Urteils. [lang]Verlängert wird sie nach Satz zwei nur, wenn das Urteil erst nach einundzwanzig "
     "Wochen zu den Akten kommt.", P),
    ("[zust2]Hier wird das Urteil erst am Montag, dem sechsten Juli, zugestellt. "
     "[mon]Die Monatsfrist endet am Tag mit derselben Zahl: [aug]am Donnerstag, dem sechsten August. [sept]Notiert war der "
     "sechste September. Die Frist ist versäumt.", P),
    # --- H Form § 345 Abs. 2, Inhalt § 344, Sprungrevision § 335 -------------------------------------------------------------
    ("[p3452]Zur Form, Absatz zwei: Seitens des Angeklagten kann dies nur in einer von dem Verteidiger oder einem Rechtsanwalt "
     "unterzeichneten Schrift oder zu Protokoll der Geschäftsstelle geschehen. [brief]Anders als bei der Einlegung "
     "reicht ein eigener Brief von Herrn Tiedemann hier nicht. [p344]Zum Inhalt, Paragraf dreihundertvierundvierzig: Die "
     "Verfahrensrüge braucht alle Tatsachen, für die Sachrüge genügt die allgemeine Rüge. [spr]Gegen ein Urteil, gegen das "
     "Berufung zulässig ist, gibt es nach Paragraf dreihundertfünfunddreißig die Sprungrevision, mit denselben Fristen.", PS),
    # --- I Kanzlei: der Fehler fällt auf -------------------------------------------------------------------------------------
    ("[entd]Am Montag, dem zehnten August, bemerkt Rechtsanwältin Sternberg den Fehler und ruft Herrn Tiedemann an.", P),
    ("[ti2]Ist meine Revision jetzt verloren?", P, "Tiedemann"),
    ("[st2]Nein. Der Fehler liegt bei uns. Wir beantragen Wiedereinsetzung.", P, "Sternberg"),
    # --- J Wiedereinsetzung, §§ 44, 45 StPO ----------------------------------------------------------------------------------
    ("[p44]Paragraf vierundvierzig: War jemand ohne Verschulden verhindert, eine Frist einzuhalten, so ist ihm auf Antrag "
     "Wiedereinsetzung in den vorigen Stand zu gewähren. [p45]Paragraf fünfundvierzig: Der Antrag ist binnen einer Woche nach Wegfall "
     "des Hindernisses zu stellen. [glaub]Die Tatsachen sind glaubhaft zu machen, [nach]und innerhalb der Antragsfrist ist "
     "die versäumte Handlung nachzuholen.", P),
    # --- K Verteidigerverschulden und Lösung ---------------------------------------------------------------------------------
    ("[zur]Und das Verschulden der Kanzlei? [zur2]Anders als im Zivilprozess wird es dem Angeklagten grundsätzlich nicht "
     "zugerechnet; so der Bundesgerichtshof. [auftr]Herr Tiedemann hatte seine Verteidigerin "
     "rechtzeitig beauftragt; ihn selbst trifft kein Verschulden. [kennt]Die Woche läuft ab dem zehnten August: "
     "Maßgeblich ist, wann er selbst davon erfährt. [antr]Am Mittwoch, dem zwölften August, beantragt "
     "Rechtsanwältin Sternberg Wiedereinsetzung, macht den Fehler mit anwaltlicher Versicherung glaubhaft und reicht die "
     "Begründung elektronisch nach. [gew]Die Wiedereinsetzung ist zu gewähren.", PS),
    # --- L Die Grenze: Verfahrensrügen ---------------------------------------------------------------------------------------
    ("[grenze]Aber Vorsicht, es gibt eine Grenze. [gr1]Ist die Revision fristgerecht begründet, etwa nur mit der Sachrüge, "
     "hilft die Wiedereinsetzung grundsätzlich nicht, um Verfahrensrügen nachzuschieben. [gr2]Sie darf die strengen Regeln "
     "der Begründung nicht unterlaufen. [gr3]Ausnahmen gibt es nur, wenn das rechtliche Gehör es verlangt, etwa weil das "
     "Sitzungsprotokoll trotz Bemühens nicht rechtzeitig vorlag.", PS),
    # --- M Merktabelle -------------------------------------------------------------------------------------------------------
    ("[tab]Die Fristen auf einen Blick: [tb1]Einlegung: eine Woche ab Verkündung. [tb2]Begründung: ein Monat nach der Einlegungsfrist, "
     "bei späterer Zustellung ab Zustellung. [tb3]Wiedereinsetzung: eine Woche ab Wegfall des Hindernisses.", PS),
    # --- N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: der Fristen-Check. [k1]Leg dir einen Zeitstrahl an: Verkündung, Einlegung, Zustellung, Begründung. "
     "[k2]Rechne jedes Fristende mit Wochentag aus und prüfe Wochenende und Feiertag. [k3]Ist eine Frist versäumt, prüfst du "
     "die Wiedereinsetzung genau an dieser Stelle.", PS),
    # --- O Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zur Zulässigkeit. [s1]Römisch eins: Statthaftigkeit. [s2]Römisch zwei: Berechtigung und Beschwer. [s3]Römisch drei: Einlegung, Gericht, Frist und "
     "Form. [s4]Römisch vier: Begründung, Frist, Form und Inhalt. [s5]Römisch fünf: bei Versäumung die Wiedereinsetzung.", PS),
    # --- P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Einlegen binnen einer Woche ab Verkündung, begründen binnen eines Monats danach, oder ab Zustellung, wenn "
     "das Urteil später kommt. [m2]Und versäumt die Verteidigung die Frist, hilft dem Angeklagten die Wiedereinsetzung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
