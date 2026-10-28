"""Folge 126 · Absolute Revisionsgründe § 338 StPO: Der Katalog und die Nr. 8 (Fr · 2. Examen · StPO-Praxis, Format Schema).
Fall nach dem Plan-Hook („Während der Aussage des Opfers war der Sitzungssaal ohne jeden Beschluss für Zuschauer
abgeschlossen“): Vor der Strafkammer des Landgerichts läuft das Verfahren gegen Herrn Lemke (Sexualdelikt, nur als neutrale
Aktenbezeichnung, keine Tatschilderung). Vor der Aussage der betroffenen Zeugin lässt der Vorsitzende die Saaltür abschließen,
ohne Beschluss der Kammer nach §§ 171b, 174 GVG. Draußen steht die Jurastudentin Lene vor verschlossener Tür. Herr Lemke wird
verurteilt; sein Verteidiger, Rechtsanwalt Strobel, legt Revision ein.
Kern als Schema: 1. Einordnung (§ 337 – § 338 Einleitungssatz als Wortlautkarte; Rügevortrag § 344 II 2, Verweis Folge 072)
→ 2. Katalog Nr. 1 (§§ 222a, 222b StPO, Vorabentscheidung seit 13.12.2019), Nr. 5, 6, 7, 8 als Tabelle → 3. Nr. 8 nur
eingeschränkt absolut (Wortlautkarten § 338 Nr. 8, BGH 5 StR 52/26 Rn. 8) → 4. Fall: § 338 Nr. 6 (Wortlautkarten § 338 Nr. 6,
§ 169 I 1 GVG; Beschluss nötig, BGH 5 StR 413/23 Rn. 7; Zurechnung, 5 StR 73/23 Rn. 6; ein Zuschauer genügt, 5 StR 388/25
Rn. 9; Ausnahmen eng, 5 StR 413/23 Rn. 10 f.) → Ergebnis §§ 353, 354 II → Klausurtipp → Schema → Merksatz.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Lemke,
Strobel, Lene; der Vorsitzende und der Wachtmeister bleiben Funktionsrollen ohne Namen, die Zeugin wird nicht gezeigt.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Vorsitzender": "helmut", "Lene": "ela_froh", "Strobel": "niklas"}  # Lexi = Erzählerin (Carla)

SEGMENTE = [
    # --- A Fall: im Sitzungssaal ----------------------------------------------------------------------------------------------
    ("[fall]Landgericht, Saal zwei. Die Strafkammer verhandelt gegen Herrn Lemke. [anklage]Die Anklage legt ihm ein "
     "Sexualdelikt zur Last. [zeugin]Gleich sagt die betroffene Frau als Zeugin aus.", 0.3),
    ("[v1]Herr Wachtmeister, schließen Sie bitte die Saaltür ab. Die Zeugin soll in Ruhe aussagen können.", 0.35,
     "Vorsitzender"),
    ("[ab]Der Wachtmeister schließt ab. [keinb]Einen Beschluss der Kammer über den Ausschluss der Öffentlichkeit gibt es "
     "nicht.", 0.3),
    # --- B Fall: auf dem Flur ---------------------------------------------------------------------------------------------------
    ("[flur]Draußen auf dem Flur steht Lene, eine Jurastudentin. Sie will die Verhandlung verfolgen.", 0.2),
    ("[l1]Abgeschlossen? Die Verhandlung ist doch öffentlich!", 0.35, "Lene"),
    ("[auf]Erst nach der Aussage wird die Tür wieder geöffnet. [urteil]Die Kammer verurteilt Herrn Lemke. [rev]Sein "
     "Verteidiger, Rechtsanwalt Strobel, legt Revision ein.", 0.3),
    ("[st1]Während der wichtigsten Aussage war die Tür zu, ohne jeden Beschluss. Das rüge ich.", 0.35, "Strobel"),
    ("[frage]Hat die Revision Erfolg? [frage2]Und muss Herr Lemke zeigen, dass das Urteil ohne den Fehler anders "
     "ausgefallen wäre?", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D 1. Einordnung: § 337 und § 338 -----------------------------------------------------------------------------------------
    ("[p337]Normalerweise muss das Urteil auf dem Rechtsfehler beruhen, Paragraf dreihundertsiebenunddreißig. [p338]Paragraf "
     "dreihundertachtunddreißig macht für bestimmte Fehler eine Ausnahme: Ein Urteil ist stets als auf einer Verletzung "
     "des Gesetzes beruhend anzusehen, [katal]wenn einer der aufgezählten Fälle vorliegt. [vermut]Das Beruhen wird also "
     "unwiderleglich vermutet. [ruege]Den Fehler selbst musst du trotzdem mit einer vollständigen Verfahrensrüge vortragen, "
     "Paragraf dreihundertvierundvierzig Absatz zwei Satz zwei. Wie das geht, zeigt unsere Folge zur Verfahrensrüge.", PS),
    # --- E 2. Der Katalog: Nummer 1 ----------------------------------------------------------------------------------------------
    ("[kat]Examensrelevant sind vor allem fünf Nummern. [n1]Nummer eins: Das Gericht war nicht vorschriftsmäßig besetzt. "
     "[n1b]Im ersten Rechtszug vor Landgericht und Oberlandesgericht wird die Besetzung mitgeteilt, Paragraf "
     "zweihundertzweiundzwanzig a. [n1c]Seit Dezember zweitausendneunzehn muss der Einwand binnen einer Woche erhoben "
     "werden, Paragraf zweihundertzweiundzwanzig b. [n1d]Hält das Gericht ihn für unbegründet, legt es ihn dem "
     "Rechtsmittelgericht vor, und das entscheidet vorab. [n1e]In der Revision bleibt die Besetzungsrüge nur in den Fällen "
     "von Nummer eins Buchstabe a und b, etwa wenn ein rechtzeitiger Einwand übergangen wurde und das "
     "Rechtsmittelgericht nicht entschieden hat. [alt]Ältere Darstellungen "
     "ohne dieses Vorabverfahren sind überholt.", PS),
    # --- F 2. Der Katalog: Nummern 5 bis 8 ----------------------------------------------------------------------------------------
    ("[n5]Nummer fünf: Die Hauptverhandlung findet ohne eine Person statt, deren Anwesenheit das Gesetz vorschreibt. "
     "[n5b]Etwa ohne Staatsanwalt, Paragraf zweihundertsechsundzwanzig, [n5c]ohne den Angeklagten, Paragraf "
     "zweihundertdreißig, [n5d]oder ohne Verteidiger, obwohl die Verteidigung notwendig ist, Paragraf hundertvierzig. "
     "[n5e]Erfasst ist aber nur ein wesentlicher Teil der Verhandlung.", P),
    ("[n6]Nummer sechs: Die Vorschriften über die Öffentlichkeit sind verletzt. [n6b]Ausschließen kann sie nur ein "
     "Beschluss des Gerichts, Paragraf hundertvierundsiebzig GVG.", P),
    ("[n7]Nummer sieben: Das Urteil hat keine Gründe, oder sie kommen zu spät zu den Akten, Paragraf "
     "zweihundertfünfundsiebzig.", P),
    ("[n8]Und Nummer acht: Die Verteidigung wurde durch einen Beschluss des Gerichts unzulässig beschränkt.", PS),
    # --- G 3. Warum Nummer 8 nur eingeschränkt absolut ist ----------------------------------------------------------------------
    ("[w8]Bei Nummer acht lohnt der genaue Wortlaut: [w8b]in einem für die Entscheidung wesentlichen Punkt. [bgh8]Der "
     "Bundesgerichtshof sagt deshalb: Es genügt nicht, dass die Beschränkung nur abstrakt geeignet ist, das Urteil zu "
     "beeinflussen. [konkr]Die Möglichkeit eines kausalen Zusammenhangs zwischen Verstoß und Urteil muss konkret bestehen. "
     "[bsp8]Lehnt das Gericht etwa die Beiziehung von Akten ab, muss die Rüge darlegen, welche Tatsachen sich aus welchen "
     "Aktenstellen ergeben hätten und was daraus für die Verteidigung folgte. [halb]Nummer acht ist also nur eingeschränkt absolut. [beschl8]Und "
     "die Rüge muss den Gerichtsbeschluss mitteilen.", PS),
    # --- H 4. Der Fall: Nummer 6 ------------------------------------------------------------------------------------------------
    ("[fall2]Zurück in Saal zwei. Hier geht es um Nummer sechs. [p169]Paragraf hundertneunundsechzig GVG: Die Verhandlung "
     "vor dem erkennenden Gericht einschließlich der Verkündung der Urteile und Beschlüsse ist öffentlich. [p171]Für die "
     "Aussage der Zeugin kam ein Ausschluss nach Paragraf hunderteinundsiebzig b GVG in Betracht. [nurb]Dafür braucht es "
     "aber stets einen Beschluss des Gerichts. Eine Anordnung des Vorsitzenden ersetzt ihn nicht.", P),
    ("[zurech]Der Fehler ist dem Gericht auch zuzurechnen: Der Vorsitzende hat das Abschließen selbst angeordnet. "
     "[versehen]Anders wäre es, wenn die Tür ohne Wissen des Gerichts verschlossen wird und es das auch bei "
     "ordnungsgemäßer Sorgfalt nicht erkennen kann. [einer]Und dass draußen vielleicht nur Lene stand, ändert nichts: Schon ein "
     "ausgesperrter Zuschauer genügt.", P),
    ("[ausn]Ausnahmen lässt der Bundesgerichtshof nur in engen Fallgruppen zu, etwa wenn ein Beschluss vorliegt, nur seine "
     "Begründung fehlt und der Grund für alle offensichtlich war. [hier]Hier fehlt der Beschluss ganz. [nr6]Nummer sechs liegt vor. [kein337]Ob das Urteil ohne "
     "den Fehler anders ausgefallen wäre, prüft der Senat nicht.", PS),
    # --- I Ergebnis -------------------------------------------------------------------------------------------------------------
    ("[erg]Die Revision hat Erfolg. [aufh]Das Urteil wird mit den Feststellungen aufgehoben, Paragraf "
     "dreihundertdreiundfünfzig, [zur]und die Sache an eine andere Strafkammer zurückverwiesen, Paragraf "
     "dreihundertvierundfünfzig Absatz zwei.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag bei Nummer sechs zuerst, ob es überhaupt einen Beschluss gab. [tipp2]Ob die Voraussetzungen "
     "von Paragraf hunderteinundsiebzig b im Einzelfall vorlagen, prüft das Revisionsgericht dagegen nicht. [tipp3]Und "
     "Nummer sechs gilt nur für zu wenig Öffentlichkeit. Bei zu viel Öffentlichkeit brauchst du das Beruhen.", PS),
    # --- K Schema ---------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für absolute Revisionsgründe. [s1]Erstens: Welche Nummer ist betroffen? [s2]Zweitens: Liegt der "
     "Verstoß vor? Bei Nummer eins mit Einwand und Vorabverfahren, bei Nummer sechs dem Gericht zurechenbar. [s3]Drittens, "
     "bei Nummer acht: Beschluss, wesentlicher Punkt und konkreter Zusammenhang zum Urteil. [s4]Viertens: vollständiger "
     "Rügevortrag. [s5]Dann wird das Beruhen vermutet, und das Urteil wird aufgehoben.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei Paragraf dreihundertachtunddreißig trägst du den Fehler vor, nicht das Beruhen. [mz]Nur Nummer acht "
     "verlangt einen konkreten Bezug zum Urteil.", 1.4),
]
