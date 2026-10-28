"""Folge 060 · Hinreichender Tatverdacht: Wann die Staatsanwaltschaft anklagt (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall (Plan-Hook: nur eine Zeugin belastet den Beschuldigten, er bestreitet alles): Aus dem Vorgarten von Frau Wessel
verschwindet an einem Dienstagvormittag ihr Fahrrad (900 Euro). Die Nachbarin von gegenüber, Frau Hesse, sieht beim
Blumengießen, wie Herr Mertens, ein Nachbar, das Rad durch das Gartentor davonschiebt. Herr Mertens bestreitet alles und
behauptet, er sei gar nicht zu Hause gewesen; das bestätigt niemand. Das Rad bleibt verschwunden, eine Kamera gibt es nicht.
Prüfung: § 170 I/II StPO (Anklage oder Einstellung) → Verdachtsstufen (§ 152 II, hinreichender Tatverdacht, § 112 I 1 nur
zur Abgrenzung) → Prognose (BGH StB 58/25 Rn. 5; OLG Düsseldorf 4 Ws 73/23 Rn. 18; verwertbare Beweise, OLG Köln
2 Ws 264/13 Rn. 13) → Beweistabelle (Klausurkonvention), § 160 II → Aussage gegen Aussage (BGH StB 58/25 Rn. 6) → in dubio
pro reo nur mittelbar (OLG Düsseldorf Rn. 18) → Beurteilungsspielraum (OLG Hamm 11 U 51/19 Rn. 42; BGH III ZR 63/24 Rn. 26)
→ Ergebnis Anklage; Gegenfall Einstellung, Klageerzwingung §§ 172 ff. → § 203 → Ausblick §§ 153, 153a → Abschluss-
verfügung (§ 169a; Klausurkonvention) → Klausurtipp → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Wessel, Hesse, Mertens; Staatsanwalt ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

# stephan und christian klingen ähnlich: Mertens (christian) spricht nur in Szene B, der Staatsanwalt (stephan) nur in Szene C.
STIMMEN = {"Wessel": "lucy", "Hesse": "hilde", "Mertens": "christian", "Staatsanwalt": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: in der Wohnstraße -------------------------------------------------------------------------------------------
    ("[fall]Ein Dienstagvormittag in einer ruhigen Wohnstraße. [rad]Im Vorgarten von Frau Wessel steht ihr neues Fahrrad, "
     "Wert neunhundert Euro. [hesse]Gegenüber gießt Frau Hesse ihre Blumen. [mertens]Da kommt Herr Mertens, ein Nachbar. "
     "[schiebt]Er schiebt das Fahrrad durch das Gartentor davon.", 0.3),
    ("[mittag]Am Mittag kommt Frau Wessel nach Hause.", 0.2),
    ("[w1]Mein Fahrrad ist weg!", 0.3, "Wessel"),
    ("[h1]Ich habe es gesehen. Herr Mertens hat es weggeschoben.", 0.4, "Hesse"),
    # --- B Fall: bei der Polizei -----------------------------------------------------------------------------------------------
    ("[anzeige]Frau Wessel zeigt ihn an. [vern]Bei der Polizei bestreitet Herr Mertens alles.", 0.2),
    ("[m1]Ich war das nicht. Ich war den ganzen Vormittag gar nicht zu Hause.", 0.4, "Mertens"),
    ("[spur]Das Fahrrad bleibt verschwunden. Eine Kamera gibt es nicht, und niemand bestätigt, wo er war.", 0.3),
    # --- C Fall: beim Staatsanwalt ---------------------------------------------------------------------------------------------
    ("[akte]Die Akte landet beim Staatsanwalt.", 0.2),
    ("[sa1]Eine einzige Zeugin, und er bestreitet alles. Klage ich an?", 0.4, "Staatsanwalt"),
    ("[frage]Reicht eine Zeugin für die Anklage? [frage2]Wann ist der Tatverdacht hinreichend?", 0.6),
    # --- D Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Abschluss der Ermittlungen: § 170 StPO ------------------------------------------------------------------------------
    ("[abschl]Am Ende der Ermittlungen hat die Staatsanwaltschaft zwei Wege. [p170]Paragraf hundertsiebzig Absatz eins: Bieten "
     "die Ermittlungen genügenden Anlass zur Erhebung der öffentlichen Klage, erhebt die Staatsanwaltschaft sie durch "
     "Einreichung einer Anklageschrift. [p170b]Absatz zwei: Andernfalls stellt die Staatsanwaltschaft das Verfahren ein. "
     "[hinr]Genügender Anlass heißt hinreichender Tatverdacht. Das ist derselbe Maßstab wie bei der Eröffnung durch das Gericht.", PS),
    # --- F Verdachtsstufen -----------------------------------------------------------------------------------------------------
    ("[stufen]Er ist eine von drei Verdachtsstufen. [anf]Für den Beginn der Ermittlungen genügt der Anfangsverdacht: zureichende "
     "tatsächliche Anhaltspunkte, Paragraf hundertzweiundfünfzig Absatz zwei. [mitte]Für die Anklage braucht es mehr, den "
     "hinreichenden Tatverdacht. [dring]Noch höher liegt der dringende Tatverdacht, den etwa die Untersuchungshaft verlangt, "
     "Paragraf hundertzwölf.", PS),
    # --- G Prognose ------------------------------------------------------------------------------------------------------------
    ("[prog]Nach dem Bundesgerichtshof ist der Verdacht hinreichend, wenn bei vorläufiger Tatbewertung die Verurteilung in einer "
     "Hauptverhandlung mit vollgültigen Beweismitteln wahrscheinlich ist. [prog2]Das ist weniger als beim dringenden "
     "Tatverdacht und erst recht nicht die volle Überzeugung des Gerichts. [formel]Das Oberlandesgericht Düsseldorf sagt: Es "
     "muss mehr für eine Verurteilung als für einen Freispruch sprechen. [verw]Und es zählen nur Beweise, die verwertbar sind.", PS),
    # --- H Beweistabelle -------------------------------------------------------------------------------------------------------
    ("[tab]In der Klausur hilft dir eine Beweistabelle. [tab1]Links steht das Merkmal, hier: Hat Herr Mertens das Rad "
     "weggenommen? [tab2]Belastend ist Frau Hesse. Sie kennt ihn seit Jahren, es war hell, und bei der Polizei sagt sie dasselbe "
     "wie am Mittag. [tab3]Entlastend ist sein Bestreiten. Sein Alibi bestätigt aber niemand. [tab4]Auch entlastende Umstände "
     "muss die Staatsanwaltschaft ermitteln, Paragraf hundertsechzig Absatz zwei.", P),
    # --- I Aussage gegen Aussage -----------------------------------------------------------------------------------------------
    ("[aga]Das ist die klassische Lage: Aussage gegen Aussage. [bgh6]Der Bundesgerichtshof sagt zur Eröffnung: In Zweifelsfällen dürfen schwierige "
     "Fragen der Beweiswürdigung nicht vorab nach Aktenlage endgültig entschieden werden, ohne den unmittelbaren Eindruck "
     "der Zeugen. [hv]Ob Frau Hesse sich irrt, klärt also das Gericht in der Hauptverhandlung.", P),
    ("[idpr]Und Vorsicht mit dem Satz: Im Zweifel für den Angeklagten. [idpr2]Bei der Prüfung des hinreichenden Tatverdachts "
     "gilt er grundsätzlich noch nicht. [idpr3]Er wirkt nur mittelbar: Wird das Gericht nach Aktenlage am Ende wahrscheinlich "
     "nach diesem Grundsatz freisprechen, fehlt der hinreichende Tatverdacht.", PS),
    # --- J Beurteilungsspielraum und Ergebnis -----------------------------------------------------------------------------------
    ("[spiel]Bei dieser Prognose hat die Staatsanwaltschaft einen Beurteilungsspielraum. Es kann mehr als eine vertretbare "
     "Entscheidung geben. [erg]Hier spricht mehr für eine Verurteilung: Die Zeugin kennt Herrn Mertens, sah ihn aus der Nähe "
     "und bleibt bei ihrer Aussage. [ankl]Also hinreichender Tatverdacht. Der Staatsanwalt erhebt Anklage.", P),
    ("[gegen]Anders, wenn Frau Hesse nur eine Gestalt von hinten gesehen hätte und ihre Angaben sich geändert hätten. "
     "[gegen2]Dann wäre ein Freispruch wahrscheinlicher, und der Staatsanwalt stellt nach Absatz zwei ein. [kez]Dagegen bleibt "
     "der Verletzten das Klageerzwingungsverfahren, Paragrafen hundertzweiundsiebzig folgende.", PS),
    # --- K § 203 und Ausblick --------------------------------------------------------------------------------------------------
    ("[p203]Nach der Anklage prüft das Gericht denselben Maßstab noch einmal. Es beschließt die Eröffnung des Hauptverfahrens, "
     "wenn der Angeschuldigte einer Straftat hinreichend verdächtig erscheint, Paragraf zweihundertdrei. [opp]Bei Vergehen kann "
     "die Staatsanwaltschaft außerdem nach Paragraf hundertdreiundfünfzig wegen geringer Schuld ohne öffentliches Interesse oder "
     "nach hundertdreiundfünfzig a vorläufig gegen Auflagen von der Anklage absehen. Das ist ein eigenes Thema.", PS),
    # --- L Abschlussverfügung --------------------------------------------------------------------------------------------------
    ("[verf]In der Klausur fasst du das Ergebnis in eine Abschlussverfügung. [verf1]Erst der Vermerk, dass die Ermittlungen "
     "abgeschlossen sind, Paragraf hundertneunundsechzig a. [verf2]Dann die Anklageschrift. [verf3]Wie die Verfügung genau "
     "aussieht, ist Klausurkonvention und unterscheidet sich von Land zu Land.", PS),
    # --- M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Entscheide nicht endgültig, ob die Zeugin die Wahrheit sagt. [tipp2]Schreib, was für und gegen ihre "
     "Aussage spricht und wie das Gericht nach der Hauptverhandlung voraussichtlich entscheiden wird. [tipp3]Und begründe eine "
     "Einstellung nie allein mit: Im Zweifel für den Angeklagten.", PS),
    # --- N Klausurschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den hinreichenden Tatverdacht. [s1]Erstens: Ist die Tat nach der Akte strafbar und verfolgbar? "
     "[s2]Zweitens die Beweistabelle: belastende und entlastende Beweise, nur verwertbare. [s3]Drittens die Prognose, ohne die "
     "Hauptverhandlung vorwegzunehmen. [s4]Viertens das Ergebnis: Ist eine Verurteilung wahrscheinlich, folgt die Anklage nach "
     "Paragraf hundertsiebzig Absatz eins, sonst die Einstellung nach Absatz zwei.", PS),
    # --- O Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Angeklagt wird, wenn eine Verurteilung wahrscheinlich ist. [mz]Ob die einzige Zeugin recht hat, entscheidet "
     "am Ende das Gericht in der Hauptverhandlung.", 1.4),
]
