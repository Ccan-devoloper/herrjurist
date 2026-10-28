"""Folge 071 · Unterlassungsdelikt Schema: Unechtes Unterlassen § 13 StGB (Mi · Examenswissen · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook, sehr zurückhaltend dargestellt (kein Kind im Wasser, kein Ertrinken, kein Leid; nur Teich,
Liegestuhl, Ball, Wellen-Symbol, Rettungswagen): Lutz liegt im Liegestuhl, sein zweijähriger Sohn fällt beim Ball-Holen in
den flachen Gartenteich. Lutz sieht es, könnte ihn mit wenigen Schritten sicher herausholen, bleibt aber sitzen und nimmt
den Tod billigend in Kauf (Tötungsvorsatz nur als Sachverhaltsangabe, keine Motive). Die Nachbarin Gesa zieht den Jungen
nach etwa einer Minute heraus; er bleibt unverletzt.
Lösung (durchgehend): versuchter Totschlag durch Unterlassen, §§ 212, 13, 22, 23 I StGB. Vorab Tun/Unterlassen (Schwerpunkt
der Vorwerfbarkeit, BGH 2 StR 157/21 Rn. 13) → Vorprüfung (keine Vollendung, Verbrechen, § 23 I, § 12 I) → Wortlautkarte
§ 13 I → Tatentschluss bzgl. aller objektiven Merkmale (BGH 4 StR 200/21 Rn. 10; 2 StR 109/20 Rn. 12): 1. Erfolg (bedingter
Vorsatz), 2. Nichtvornahme trotz physisch-realer Möglichkeit, 3. Quasikausalität (BGH 1 StR 272/09 Rn. 65 f.; 4 StR 200/21
Rn. 16 f.), objektive Zurechnung (Lehre), 4. Garantenstellung (BGH 3 StR 11/25 Rn. 17 f.: §§ 1626 I, 1631 I BGB;
Beschützer-/Überwachergarant, Ingerenz nur Überblick), 5. Entsprechungsklausel (Lehre) → unmittelbares Ansetzen →
Rechtswidrigkeit → Schuld/Zumutbarkeit (Standort str.) → kein Rücktritt (§ 24 I 2) → Ergebnis → § 13 II, § 49 I, § 23 II →
Abwandlung §§ 222, 13 (ein Satz) → Abgrenzung § 323c (ein Satz) → Klausurtipp → Schema (vollendetes Delikt) → Merksatz.
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Lutz, Gesa.
Namen nie im Genitiv mit -s. „In-gerenz“ = lautliche Schreibweise für „Ingerenz“ (Nachvertonung Segment 14: beide
Erkennungsmodelle hörten in v1 „Inherenz/Innerenz“). Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Lutz": "niklas", "Gesa": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Sommernachmittag im Garten ------------------------------------------------------------------------------------
    ("[fall]Ein heißer Sommernachmittag in einem Garten. [lutz]Lutz liegt im Liegestuhl. [sohn]Sein zweijähriger Sohn spielt "
     "mit einem Ball, ein paar Meter weiter liegt ein Gartenteich.", 0.3),
    ("[l1]Spiel schön, ich ruh mich kurz aus.", 0.3, "Lutz"),
    ("[ball]Der Ball rollt ins Wasser. [faellt]Der Junge läuft hinterher und fällt in den Teich. [sieht]Lutz sieht das genau. "
     "Der Teich ist flach, mit wenigen Schritten könnte er seinen Sohn sicher herausholen. [sitzt]Aber er bleibt sitzen. "
     "[vors]Er hält es für möglich, dass sein Sohn ertrinkt, und nimmt das billigend in Kauf.", 0.3),
    ("[gesa]Nach etwa einer Minute bemerkt die Nachbarin Gesa den Jungen. [zaun]Sie springt über den Zaun und zieht ihn "
     "heraus.", 0.3),
    ("[g1]Ich hab dich! Alles gut.", 0.3, "Gesa"),
    ("[rtw]Ein Rettungswagen bringt den Jungen zur Kontrolle ins Krankenhaus. Ihm fehlt nichts.", 0.4),
    ("[frage]Lutz hat nichts getan. Kann er sich trotzdem strafbar gemacht haben? [frage2]Und wenn ja: wegen eines "
     "Tötungsdelikts?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tun oder Unterlassen, Vorprüfung --------------------------------------------------------------------------------------
    ("[tun]Zuerst: Tun oder Unterlassen? Entscheidend ist der Schwerpunkt der Vorwerfbarkeit. [unterl]Lutz wird nicht "
     "vorgeworfen, was er getan hat, sondern dass er nicht geholfen hat. Also Unterlassen. [vollend]Sein Sohn lebt, ein "
     "vollendeter Totschlag scheidet aus. [verbr]Totschlag ist aber ein Verbrechen, der Versuch ist deshalb stets strafbar. "
     "[versuch]Wir prüfen versuchten Totschlag durch Unterlassen, Paragrafen zweihundertzwölf, dreizehn, zweiundzwanzig "
     "und dreiundzwanzig.", PS),
    # --- D Wortlautkarte § 13 Abs. 1 ---------------------------------------------------------------------------------------------
    ("[p13]Die zentrale Norm ist Paragraf dreizehn Absatz eins: Wer es unterlässt, einen Erfolg abzuwenden, der zum Tatbestand "
     "eines Strafgesetzes gehört, ist nach diesem Gesetz nur dann strafbar, [einst]wenn er rechtlich dafür einzustehen hat, "
     "dass der Erfolg nicht eintritt, [entspr]und wenn das Unterlassen der Verwirklichung des gesetzlichen Tatbestandes durch "
     "ein Tun entspricht.", PS),
    # --- E Tatentschluss: 1. Erfolg ----------------------------------------------------------------------------------------------
    ("[tat]Beim Versuch prüfst du die Merkmale des objektiven Tatbestands in der Vorstellung des Täters, im Tatentschluss. "
     "[erfolg]Erstens der Erfolg: der Tod seines Sohnes. [erfolg2]Lutz sieht die Lebensgefahr und nimmt den Tod billigend in "
     "Kauf. Das ist bedingter Vorsatz.", P),
    # --- F 2. Nichtvornahme trotz Möglichkeit ------------------------------------------------------------------------------------
    ("[moegl]Zweitens: Er unterlässt die gebotene Rettung, obwohl sie ihm physisch-real möglich ist. [moegl2]Der Teich ist nah "
     "und flach, Lutz kann hingehen und seinen Sohn herausziehen. Das weiß er.", P),
    # --- G 3. Quasikausalität ----------------------------------------------------------------------------------------------------
    ("[quasi]Drittens die Quasikausalität. Ein Unterlassen ist ursächlich, wenn die gebotene Handlung den Erfolg verhindert "
     "hätte, nach dem Bundesgerichtshof mit an Sicherheit grenzender Wahrscheinlichkeit. [quasi2]Lutz weiß: Zieht er seinen "
     "Sohn sofort heraus, überlebt der Junge sicher. [zurech]Die objektive Zurechnung, die die Lehre zusätzlich verlangt, ist "
     "hier unproblematisch.", PS),
    # --- H 4. Garantenstellung ---------------------------------------------------------------------------------------------------
    ("[garant]Viertens die Garantenstellung: Lutz muss rechtlich dafür einstehen, dass der Erfolg nicht eintritt. [eltern]Als "
     "sorgeberechtigter Vater ist er Beschützergarant. [bgb]Eltern müssen nach dem Bürgerlichen Gesetzbuch für ihr Kind sorgen "
     "und es beaufsichtigen. [ueberw]Daneben gibt es Überwachergaranten, etwa wer eine Gefahrenquelle beherrscht. [ing]Oder wer "
     "durch pflichtwidriges Vorverhalten eine Gefahr geschaffen hat, die In-gerenz. Dazu kommen eigene Folgen.", PS),
    # --- I 5. Entsprechungsklausel -----------------------------------------------------------------------------------------------
    ("[entspr2]Fünftens die Entsprechungsklausel. Bei reinen Erfolgsdelikten wie dem Totschlag ist sie regelmäßig "
     "unproblematisch. [verh]Bedeutung hat sie bei Delikten, die eine bestimmte Begehungsweise verlangen.", PS),
    # --- J Ansetzen, Rechtswidrigkeit, Schuld, Rücktritt -------------------------------------------------------------------------
    ("[ansetz]Unmittelbar angesetzt hat Lutz spätestens, als sein Sohn im Wasser liegt und er sitzen bleibt. Das Leben ist da "
     "schon unmittelbar gefährdet. [rw]Rechtfertigungsgründe gibt es nicht. [zumut]In der Schuld fragst du nach der "
     "Zumutbarkeit. Die Rettung war ohne Gefahr für Lutz möglich, also zumutbar. [standort]Wo die Zumutbarkeit zu prüfen ist, "
     "ist allerdings umstritten. [rueck]Ein Rücktritt scheidet aus. Gerettet hat Gesa, Lutz hat sich nicht bemüht.", PS),
    # --- K Ergebnis, Strafmilderung ----------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Lutz ist strafbar wegen versuchten Totschlags durch Unterlassen. [milder]Die Strafe kann nach Paragraf "
     "dreizehn Absatz zwei gemildert werden, nach Paragraf neunundvierzig Absatz eins, wegen des Versuchs auch nach Paragraf "
     "dreiundzwanzig Absatz zwei.", PS),
    # --- L Abwandlung § 222, Abgrenzung § 323c -----------------------------------------------------------------------------------
    ("[ab]Abwandlung: Bemerkt Lutz den Sturz nur deshalb nicht, weil er pflichtwidrig nicht aufpasst, und kommt jede Hilfe zu "
     "spät, kommt fahrlässige Tötung durch Unterlassen in Betracht, Paragrafen zweihundertzweiundzwanzig und dreizehn.", PS),
    ("[p323]Davon unterscheide die unterlassene Hilfeleistung nach Paragraf dreihundertdreiundzwanzig c. [echt]Sie ist ein "
     "echtes Unterlassungsdelikt: Das Gesetz bestraft das Nichthelfen selbst, und es trifft jeden, auch ohne "
     "Garantenstellung.", PS),
    # --- M Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Klär Tun oder Unterlassen nur kurz vorab, außer der Fall ist wirklich zweifelhaft. [tipp2]Beim "
     "Versuch gehören Erfolg, Handlungsmöglichkeit, Quasikausalität und Garantenstellung in den Tatentschluss. [tipp3]Im "
     "vollendeten Delikt prüfst du sie im objektiven Tatbestand, den Vorsatz danach.", PS),
    # --- N Prüfschema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für das vollendete unechte Unterlassungsdelikt. [s0]Vorab: Tun oder Unterlassen? [s1]Römisch eins, "
     "Tatbestand, zuerst objektiv: [s1a]der Erfolg, [s1b]die Nichtvornahme der gebotenen Handlung trotz physisch-realer "
     "Möglichkeit, [s1c]die Quasikausalität und objektive Zurechnung, [s1d]die Garantenstellung [s1e]und die Entsprechung. "
     "[s1f]Dann subjektiv der Vorsatz. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, Schuld, mit der Zumutbarkeit. "
     "[s4]Danach die Strafmilderung nach Paragraf dreizehn Absatz zwei. [s5]Beim Versuch wandern die objektiven Merkmale in den "
     "Tatentschluss.", PS),
    # --- O Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Für einen Erfolg haftet durch Unterlassen nur, wer als Garant rechtlich dafür einstehen muss. [m2]Und die "
     "mögliche Rettung hätte den Erfolg mit an Sicherheit grenzender Wahrscheinlichkeit verhindern müssen. [m3]Tritt der "
     "Erfolg nicht ein, prüfst du den Versuch.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
