"""Folge 132 · Widerspruchslösung: Fehlende Belehrung und Verwertungsverbot (Fr · 2. Examen · StPO-Praxis, Format Sonderlage).
Fall nach dem Plan-Hook („Die Polizei befragte den späteren Beschuldigten am Tatort ‚informatorisch‘, obwohl sie ihn schon
für den Täter hielt“): Herr Mangold sprüht einen Schriftzug an die Wand einer Turnhalle (Sachbeschädigung, § 303 II StGB).
Eine Anwohnerin zeigt auf ihn; Polizeikommissarin Kirchhoff sieht Farbe an seinen Fingern und die Spraydose und fragt ihn ohne
Belehrung „nur mal informatorisch“, ob er gesprüht habe. Er gesteht. In der Hauptverhandlung vor dem Amtsgericht schweigt er;
Kirchhoff sagt als Zeugin über das Geständnis aus; Rechtsanwalt Hufnagel widerspricht direkt danach der Verwertung
(Variante: er schweigt und rügt erst im Plädoyer).
Kern als Schema: 1. Belehrungspflicht § 163a IV 2 i. V. m. § 136 I 2 StPO (Wortlautkarte § 136 I 2 auszugsweise) →
2. Beschuldigtenstellung (Verfolgungswille/Willensakt, informatorische Befragung, Stärke des Tatverdachts, Beurteilungsspielraum,
Willkürgrenze: BGHSt 38, 214, 227 f.; BGH 1 StR 3/07 Rn. 17–19; StB 14/19 Rn. 30–32; 5 StR 547/25 Rn. 6) → 3. Verwertungsverbot
(BGHSt 38, 214, Leitsatz und S. 220–222; Ausnahme bekanntes Schweigerecht S. 224 f.) → 4. Widerspruchslösung (Wortlautkarte
§ 257 I, II auszugsweise; BGHSt 38, 214, 225 f.; BGH 2 StR 46/15 Rn. 14; unverteidigt: BGHSt 38, 214, 226; Kritik: 2 StR 46/15
Rn. 16) → Ergebnis Grundfall/Variante → 5. Abgrenzung § 136a III StPO (Wortlautkarte) → 6. Revision (2 StR 46/15 Rn. 14;
5 StR 17/18 Rn. 6, 8; 5 StR 547/25 Rn. 7; Verweis Folge 072) → Klausurtipp → Schema → Merksatz.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben:
Mangold, Kirchhoff, Hufnagel; Anwohnerin und Strafrichterin bleiben Funktionsrollen ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Anwohnerin": "ela_froh", "Kirchhoff": "julia", "Mangold": "niklas", "Hufnagel": "helmut"}  # Lexi = Erzählerin (Carla)

SEGMENTE = [
    # --- A Fall: an der Turnhalle ------------------------------------------------------------------------------------------
    ("[fall]Samstagabend an der Turnhalle der Gesamtschule. [spray]Ein Mann im grünen Pullover sprüht einen großen "
     "Schriftzug an die frisch gestrichene Wand. [anw]Eine Anwohnerin sieht ihn und ruft die Polizei.", 0.3),
    ("[pol]Wenige Minuten später ist Polizeikommissarin Kirchhoff da.", 0.2),
    ("[a1]Der Mann im grünen Pullover war es. Ich habe ihn genau gesehen!", 0.35, "Anwohnerin"),
    ("[mangold]Kirchhoff geht zu Herrn Mangold. [farbe]An seinen Fingern klebt grüne Farbe, in der Hand hält er eine "
     "Spraydose. [klar]Für sie ist klar: Er war es. [keinbel]Über seine Rechte belehrt sie ihn nicht.", 0.3),
    ("[k1]Ich frage Sie nur mal informatorisch: Haben Sie an die Wand gesprüht?", 0.35, "Kirchhoff"),
    ("[m1]Ja, das war ich. Tut mir leid.", 0.35, "Mangold"),
    ("[notiz]Kirchhoff schreibt das Geständnis in ihren Vermerk.", 0.3),
    # --- B Fall: Hauptverhandlung beim Amtsgericht ------------------------------------------------------------------------
    ("[hv]Monate später, Amtsgericht, Hauptverhandlung wegen Sachbeschädigung. [schweigt]Herr Mangold schweigt. "
     "[zeugin]Kirchhoff sagt als Zeugin aus, was er ihr am Tatort gestanden hat. [steht]Direkt danach "
     "erklärt sich sein Verteidiger, Rechtsanwalt Hufnagel.", 0.2),
    ("[h1]Ich widerspreche der Verwertung. Mein Mandant wurde am Tatort nicht belehrt.", 0.35, "Hufnagel"),
    ("[frage]Darf die Strafrichterin das Geständnis verwerten? [frage2]Und was, wenn Hufnagel geschwiegen hätte?", 0.6),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D 1. Belehrungspflicht -------------------------------------------------------------------------------------------
    ("[p163]Für die Vernehmung durch die Polizei verweist Paragraf hundertdreiundsechzig a Absatz vier Satz zwei "
     "[verweis]auf Paragraf hundertsechsunddreißig Absatz eins Satz zwei. [p136]Danach ist der Beschuldigte "
     "darauf hinzuweisen, dass es ihm freisteht, sich zur Beschuldigung zu äußern oder nicht zur Sache auszusagen, "
     "[vert]und dass er jederzeit einen Verteidiger befragen kann. [nichts]Kirchhoff hat nichts davon gesagt. [nurwenn]Aber "
     "musste sie das? Nur, wenn Herr Mangold schon Beschuldigter war.", PS),
    # --- E 2. Beschuldigtenstellung ---------------------------------------------------------------------------------------
    ("[besch]Der Bundesgerichtshof verbindet dafür zwei Elemente. [wille]Subjektiv braucht es den Verfolgungswillen der "
     "Polizei, [akt]objektiv einen Willensakt, in dem er nach außen sichtbar wird. [info]Wer am Tatort nur fragt, ob jemand "
     "etwas beobachtet hat, vernimmt noch keinen Beschuldigten. Das ist die informatorische Befragung. [staerke]Bedeutsam "
     "ist die Stärke des Tatverdachts. [spiel]Die Polizei hat dabei einen Beurteilungsspielraum. [willk]Ist der Verdacht "
     "aber so stark, dass alles andere willkürlich wäre, muss sie zur Beschuldigtenvernehmung übergehen.", P),
    ("[sub]Hier zeigt die Anwohnerin auf Herrn Mangold, dazu Farbe und Spraydose. "
     "[gezielt]Kirchhoff hält ihn für den Täter und fragt gezielt nach der Tat. [etik]Entscheidend sind Ziel und Umstände "
     "der Befragung, nicht ihr Etikett. [jabesch]Herr Mangold war Beschuldigter, und die Belehrung fehlte.", PS),
    # --- F 3. Verwertungsverbot ---------------------------------------------------------------------------------------------
    ("[vv]Was folgt daraus? [bghst]Der Bundesgerichtshof hat neunzehnhundertzweiundneunzig entschieden: [vv2]Äußerungen aus "
     "einer Vernehmung ohne den Hinweis auf das Schweigerecht dürfen nicht verwertet werden. [grund]Das Schweigerecht gehört zum fairen "
     "Verfahren, und die erste Befragung durch die Polizei trifft einen meist unvorbereitet. [zeug]Das Verbot gilt auch, "
     "wenn die Polizistin das Geständnis als Zeugin wiedergibt. [ausn]Eine Ausnahme: Es steht fest, dass der Beschuldigte "
     "sein Schweigerecht auch ohne Belehrung kannte. [ausn2]Dafür gibt es bei Herrn Mangold keinen Anhaltspunkt.", PS),
    # --- G 4. Widerspruchslösung --------------------------------------------------------------------------------------------
    ("[wl]Aber dieses Verwertungsverbot kommt nicht von selbst. [wl2]Nach der Widerspruchslösung muss der verteidigte "
     "Angeklagte der Verwertung widersprechen, [wl3]und zwar bis zu dem Zeitpunkt aus Paragraf zweihundertsiebenundfünfzig. "
     "[p257]Nach jeder einzelnen Beweiserhebung soll der Angeklagte befragt werden, ob er dazu etwas zu erklären habe. "
     "[p257b]Auch der Verteidiger kann sich auf Verlangen erklären. [direkt]Der Widerspruch muss "
     "also spätestens in der Erklärung nach der Beweiserhebung stecken, hier: nach der Aussage der Polizistin. "
     "[spaet]Danach kann er nicht mehr nachgeholt werden.", P),
    ("[unv]Hat der Angeklagte keinen Verteidiger, gilt das nur, wenn ihn der Vorsitzende auf die Möglichkeit des "
     "Widerspruchs hingewiesen hat. [kritik]Unumstritten ist die Frist nicht: Sogar ein Senat des Bundesgerichtshofs hat "
     "sie bezweifelt, allerdings für Funde aus Durchsuchungen.", PS),
    # --- H Ergebnis: Grundfall und Variante --------------------------------------------------------------------------------
    ("[erg]Im Grundfall hat Hufnagel rechtzeitig widersprochen. "
     "[erg2]Das Geständnis ist unverwertbar. [erg3]Verurteilen kann die Strafrichterin Herrn Mangold nur, wenn andere "
     "Beweise tragen, etwa die Aussage der Anwohnerin.", P),
    ("[var]In der Variante schweigt Hufnagel nach der Aussage. Erst im Plädoyer rügt er die fehlende Belehrung. "
     "[var2]Das ist zu spät. [var3]Ohne rechtzeitigen Widerspruch entsteht kein Verwertungsverbot, und das Geständnis darf "
     "verwertet werden.", PS),
    # --- I 5. Abgrenzung § 136a -----------------------------------------------------------------------------------------------
    ("[p136a]Anders bei verbotenen Vernehmungsmethoden nach Paragraf hundertsechsunddreißig a, etwa Drohung oder "
     "Täuschung. [p136a2]Solche Aussagen dürfen auch dann nicht verwertet werden, wenn der Beschuldigte der Verwertung "
     "zustimmt. [keinw]Auf einen Widerspruch kommt es dort nicht an.", PS),
    # --- J 6. Revision ------------------------------------------------------------------------------------------------------
    ("[rev]Verwertet das Gericht ein Geständnis trotz Widerspruch, kann der Angeklagte das mit der Revision rügen. "
     "[rev2]Die Verfahrensrüge muss nach Paragraf dreihundertvierundvierzig Absatz zwei Satz zwei auch vortragen, dass und "
     "wann widersprochen wurde. [rev3]Dazu alle Tatsachen zur Beschuldigtenstellung, also was die Polizei bis zur Befragung "
     "wusste. [rev4]Wie man eine Verfahrensrüge baut, zeigt unsere Folge dazu.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lass dich vom Wort informatorisch im Vermerk nicht täuschen. [tipp2]Prüf selbst, wie stark der "
     "Verdacht war und wie die Polizei aufgetreten ist. [tipp3]Und prüf getrennt, ob und wann widersprochen wurde. Ohne "
     "Widerspruch ist die Rüge beim verteidigten Angeklagten verloren.", PS),
    # --- L Schema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Erstens: Belehrungspflicht bei der Vernehmung. [s2]Zweitens: Beschuldigtenstellung, also Verfolgungswille und Stärke des Tatverdachts. "
     "[s3]Drittens: Verwertungsverbot, außer der Beschuldigte kannte sein Schweigerecht. [s4]Viertens: rechtzeitiger "
     "Widerspruch bis zum Zeitpunkt des Paragrafen zweihundertsiebenundfünfzig. [s5]Fünftens: Bei Paragraf "
     "hundertsechsunddreißig a kein Widerspruch nötig. [s6]Und sechstens, in der Revision: den Widerspruch in der Rüge "
     "vortragen.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ohne Belehrung kein verwertbares Geständnis. [mz]Aber nur, wenn rechtzeitig widersprochen wird.", 1.4),
]
