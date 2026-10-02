"""Folge 066 · Revision Strafrecht: Sachrüge vs. Verfahrensrüge (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall nach dem Plan-Hook („Der Richter hat meinen Zeugen nicht gehört – und das Urteil ist sowieso falsch.“):
Das Landgericht verurteilt Herrn Brockmann wegen Diebstahls von 40 Laptops aus dem Lager seines Arbeitgebers (Transponder
öffnete die Lagertür am Tatabend um 22:10 Uhr). In der Hauptverhandlung beantragt Rechtsanwältin Lenz, den Alibizeugen
Herrn Stoll zu vernehmen; das Gericht bescheidet den Beweisantrag nicht und verkündet das Urteil. Strafschärfend wertet es,
dass er sich über fremdes Eigentum hinweggesetzt habe.
Prüfung: Revision als Rechtsprüfung (§ 337 I, II StPO) → Zulässigkeit kurz (§§ 333, 341 I, 345 I, II StPO; § 135 I GVG) →
zwei Rügen (§ 344 II 1 StPO, Faustregel) → Sachrüge (allgemeine Sachrüge genügt; Urteil aus sich heraus; Beweiswürdigung nur
auf Rechtsfehler; § 46 III StGB) → Verfahrensrüge (§ 244 III 1, VI 1 StPO; § 344 II 2 StPO, Vollständigkeit; § 274 StPO)
→ Beruhen (BGH 3 StR 518/19 Rn. 94) vs. § 338 StPO (Beispiel Nr. 6) → Ergebnis (§§ 353, 354 II StPO) → Revisionsbegründung
als Klausurkonvention → Klausurtipp → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Brockmann, Lenz, Stoll; Richter ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Brockmann": "marc", "Lenz": "sabrina", "Richter": "william"}  # Lexi = Erzählerstimme (Carla); Herr Stoll spricht nicht

SEGMENTE = [
    # --- A Fall: in der Kanzlei ----------------------------------------------------------------------------------------------
    ("[fall]Eine Anwaltskanzlei, drei Tage nach dem Urteil. [mandant]Herr Brockmann ist bei seiner Verteidigerin, "
     "Rechtsanwältin Lenz.", 0.2),
    ("[b1]Der Richter hat meinen Zeugen nicht gehört. Und das Urteil ist sowieso falsch.", 0.4, "Brockmann"),
    ("[lg]Das Landgericht hat ihn wegen Diebstahls verurteilt. [lager]Aus dem Lager seines Arbeitgebers fehlten vierzig "
     "Laptops. [chip]Sein Transponder öffnete am Tatabend um zweiundzwanzig Uhr zehn die Lagertür.", 0.3),
    # --- B Fall: Rückblick in die Hauptverhandlung ---------------------------------------------------------------------------
    ("[saal]Ein Blick zurück in die Hauptverhandlung. [antrag]Rechtsanwältin Lenz stellt einen Beweisantrag.", 0.2),
    ("[l1]Ich beantrage, Herrn Stoll als Zeugen dafür zu vernehmen, dass Herr Brockmann am Tatabend von einundzwanzig "
     "bis dreiundzwanzig Uhr mit ihm beim Fußballtraining war.", 0.4, "Lenz"),
    ("[stoll]Herr Stoll wartet vor dem Saal. [nichts]Doch das Gericht entscheidet über den Antrag nicht. "
     "[schluss]Es schließt die Beweisaufnahme und verkündet das Urteil.", 0.2),
    ("[r1]Der Angeklagte wird wegen Diebstahls zu einer Freiheitsstrafe von einem Jahr und sechs Monaten verurteilt.", 0.4, "Richter"),
    ("[gruende]In den Urteilsgründen steht: [schaerf]Strafschärfend wirke, dass er sich über fremdes Eigentum "
     "hinweggesetzt habe.", 0.3),
    # --- C Fall: zurück in der Kanzlei ----------------------------------------------------------------------------------------
    ("[l2]Dagegen legen wir Revision ein.", 0.4, "Lenz"),
    ("[frage]Was davon kann Herr Brockmann rügen? [frage2]Und braucht er dafür die Sachrüge oder die Verfahrensrüge?", 0.6),
    # --- D Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Revision als Rechtsprüfung: § 337 StPO ----------------------------------------------------------------------------
    ("[recht]Die Revision ist keine zweite Tatsacheninstanz. [p337]Paragraf dreihundertsiebenunddreißig Absatz eins: Die "
     "Revision kann nur darauf gestützt werden, dass das Urteil auf einer Verletzung des Gesetzes beruhe. [p337b]Absatz zwei: "
     "Das Gesetz ist verletzt, wenn eine Rechtsnorm nicht oder nicht richtig angewendet worden ist. [keinez]Das "
     "Revisionsgericht vernimmt deshalb keine Zeugen zur Tat und würdigt die Beweise nicht neu.", PS),
    # --- F Zulässigkeit, kurz ------------------------------------------------------------------------------------------------
    ("[statt]Statthaft ist sie gegen Urteile des Landgerichts und erstinstanzliche Urteile des Oberlandesgerichts, "
     "Paragraf dreihundertdreiunddreißig. [bgh]Hier entscheidet der Bundesgerichtshof. [frist1]Einlegen muss Herr Brockmann sie binnen "
     "einer Woche nach der Verkündung beim Landgericht, Paragraf dreihunderteinundvierzig. [frist2]Die Begründung folgt "
     "binnen eines Monats nach Ablauf dieser Woche, meist ab Zustellung des Urteils, Paragraf dreihundertfünfundvierzig. "
     "[form]Unterschreiben muss ein Verteidiger oder Rechtsanwalt, sonst geht es nur zu Protokoll der Geschäftsstelle.", PS),
    # --- G Zwei Rügen: § 344 II 1 StPO ---------------------------------------------------------------------------------------
    ("[p344]Paragraf dreihundertvierundvierzig Absatz zwei verlangt: Die Begründung muss zeigen, ob eine Rechtsnorm über "
     "das Verfahren oder eine andere Rechtsnorm verletzt sein soll. [zwei]Das sind die zwei Rügen: Verfahrensrüge und Sachrüge. [test]Als Faustregel: Steht der Fehler im Urteil selbst, "
     "ist es die Sachrüge. [test2]Geschah er auf dem Weg zum Urteil, in der Hauptverhandlung, ist es die Verfahrensrüge.", PS),
    # --- H Sachrüge ----------------------------------------------------------------------------------------------------------
    ("[sach]Zuerst die Sachrüge. [allg]Dafür genügt ein Satz: Ich rüge die Verletzung materiellen Rechts. [aussich]Dann "
     "prüft das Revisionsgericht das Urteil aus sich heraus, allein anhand der Urteilsgründe: [felder]Trägt die Subsumtion "
     "den Schuldspruch, und ist die Strafzumessung rechtsfehlerfrei?", P),
    ("[bw]Die Beweiswürdigung bleibt Sache des Landgerichts. [bw2]Angreifbar ist sie nur, wenn sie lückenhaft, "
     "widersprüchlich oder unklar ist oder gegen Denkgesetze verstößt. [chip2]Hier stützt sich die Kammer schlüssig auf den "
     "Transponder. [falsch]Dass Herr Brockmann das Urteil für falsch hält, reicht also nicht.", P),
    ("[strafz]Anders beim Strafmaß. [p46]Paragraf sechsundvierzig Absatz drei StGB: Umstände, die schon Merkmale des "
     "gesetzlichen Tatbestandes sind, dürfen nicht berücksichtigt werden. [doppel]Fremdes Eigentum zu verletzen, gehört aber "
     "zu jedem Diebstahl. [doppel2]Die Kammer hat das doppelt verwertet. Insoweit greift die Sachrüge.", PS),
    # --- I Verfahrensrüge ----------------------------------------------------------------------------------------------------
    ("[verf]Der übergangene Zeuge ist ein Fehler auf dem Weg zum Urteil: Verfahrensrüge. [ba]Der Antrag war ein "
     "Beweisantrag: eine bestimmte Tatsache, ein bestimmter Zeuge, der dabei war, Paragraf zweihundertvierundvierzig Absatz drei. [p244]Absatz sechs: Die Ablehnung eines Beweisantrages bedarf eines "
     "Gerichtsbeschlusses. [ohne]Das Gericht hat den Antrag aber gar nicht beschieden. Das ist ein Verfahrensfehler.", P),
    ("[vortrag]Nun kommt die Hürde. [p344b]Paragraf dreihundertvierundvierzig Absatz zwei Satz zwei: Die den Mangel "
     "enthaltenden Tatsachen müssen angegeben werden. [voll]Und zwar so vollständig, dass das Revisionsgericht allein anhand "
     "der Begründung entscheiden kann. [inhalt]Also: der Antrag im Wortlaut, wann er gestellt wurde, und dass bis zum Urteil "
     "kein Beschluss erging. [prot]Bewiesen wird das durch das Protokoll, Paragraf zweihundertvierundsiebzig.", PS),
    # --- J Beruhen und § 338 -------------------------------------------------------------------------------------------------
    ("[beruh]Bleibt das Beruhen. [beruh2]Nach dem Bundesgerichtshof beruht ein Urteil auf einem Fehler, wenn es ohne ihn "
     "möglicherweise anders ausgefallen wäre. [moegl]Hätte Herr Stoll das Alibi bestätigt, wäre ein Freispruch möglich. Das "
     "genügt. [p338]Bei den absoluten Revisionsgründen des Paragrafen dreihundertachtunddreißig wird das Beruhen sogar "
     "unwiderleglich vermutet, [oeff]etwa wenn die Vorschriften über die Öffentlichkeit verletzt sind.", PS),
    # --- K Ergebnis ----------------------------------------------------------------------------------------------------------
    ("[erg]Die Verfahrensrüge hat also Erfolg. [aufh]Das Urteil wird mit den Feststellungen aufgehoben, Paragraf "
     "dreihundertdreiundfünfzig, [zur]und die Sache an eine andere Strafkammer zurückverwiesen, Paragraf "
     "dreihundertvierundfünfzig Absatz zwei.", PS),
    # --- L Revisionsbegründung (Klausurkonvention) ---------------------------------------------------------------------------
    ("[schrift]In der Klausur schreibst du oft die Revisionsbegründung. [rb1]Oben steht der Antrag auf Aufhebung und "
     "Zurückverweisung. [rb2]Dann die Verfahrensrügen, jede mit vollständigem "
     "Tatsachenvortrag. [rb3]Am Ende die Sachrüge, erst allgemein erhoben, dann ausgeführt. [rb4]Dieser Aufbau ist "
     "Klausurkonvention.", PS),
    # --- M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag bei jedem Fehler, wo er steht. [tipp2]Steht er in den Urteilsgründen: Sachrüge. "
     "[tipp3]Ergibt er sich nur aus dem Ablauf der Hauptverhandlung: Verfahrensrüge mit allen Tatsachen, auch denen, die "
     "gegen dich sprechen. [tipp4]Und erhebe immer zusätzlich die allgemeine Sachrüge.", PS),
    # --- N Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Revision. [s1]Erstens die Zulässigkeit: statthaft, Frist und Form. [s2]Zweitens die "
     "Verfahrensrügen: Fehler, vollständiger Vortrag, Beruhen oder absoluter Revisionsgrund. [s3]Drittens die Sachrüge: "
     "Schuldspruch und Strafzumessung, allein am Urteil. [s4]Viertens der Antrag: aufheben und zurückverweisen.", PS),
    # --- O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Was im Urteil steht, prüft die Sachrüge. [mz]Was in der Hauptverhandlung geschah, braucht die "
     "Verfahrensrüge, mit allen Tatsachen.", 1.4),
]
