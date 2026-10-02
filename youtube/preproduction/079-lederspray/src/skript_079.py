"""Folge 079 · Lederspray-Fall: Garantenstellung & Kausalität im Vorstand (Mo · Der Fall · StGB AT, Klassiker-Fall).
Erfundener Ausgangsfall nach dem Plan-Hook (keine echte Firma, keine Marke; zurückhaltend: keine erkrankten Menschen im
Bild, Atemnot nur als Symbol): Die drei Geschäftsführer Eberhard, Almut und Hauke einer Schuhpflege-Firma erfahren in einer
Sondersitzung, dass Kunden nach dem Gebrauch ihres Imprägniersprays Atemnot bekommen; die Laborleiterin findet keinen
Giftstoff, schließt aber andere Ursachen aus. Sie beschließen einstimmig, das Spray im Handel zu lassen und nicht
zurückzurufen; weitere Kunden erkranken. Danach der echte Fall: BGH, Urt. v. 6.7.1990 – 2 StR 549/89, BGHSt 37, 106
(Volltext mit Seitenzahlen, Belege in ../RECHTSSTAND.md).
Lösung: Vorab Tun (Verkauf nach der Sitzung) / Unterlassen (Rückruf) → § 13 I (Wortlaut) → 1. Erfolg § 223, Kausalität
trotz unbekannten Wirkmechanismus (S. 111 f.) → 2. Garantenstellung aus Ingerenz (S. 115–119), Rückrufpflicht (S. 119–122),
Generalverantwortung (S. 123 f.), Handlungspflicht des Einzelnen (S. 125 f.) → 3. Quasikausalität (S. 126 f.), Einwand
„meine Stimme“ → Mittäterschaft § 25 II (Wortlaut, S. 128 f.), Fahrlässigkeit: Teilbeitrag ursächlich (S. 130–132) →
4. Vorsatz ab Sitzung, davor § 229 (S. 110, 132) → § 224 I Nr. 5 (Wortlaut; BGH: § 223a a. F.), Nr. 1 nur nach Wortlaut →
Ergebnis → Klausurtipp → Schema → Merksatz.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Eberhard, Almut, Hauke; Laborleiterin ohne
Namen. Namen nie im Genitiv mit -s. „In-gerenz“ = lautliche Schreibweise für „Ingerenz“ (in Folge 071 hörten beide
Erkennungsmodelle ohne Bindestrich „Inherenz“). Segmente: (text, pause) = Erzählerin Carla (auch Lexi),
(text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Laborleiterin": "ela_froh", "Eberhard": "helmut", "Almut": "julia", "Hauke": "niklas"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: Sondersitzung der Geschäftsführung -----------------------------------------------------------------------------
    ("[fall]Eine Firma stellt Pflegemittel für Schuhe her, [spray]ihr Imprägnierspray verkauft sich gut. [meld]Doch seit "
     "dem Herbst gehen Meldungen ein: Nach dem Sprühen bekommen Kunden Atemnot, einige kommen ins Krankenhaus, "
     "manche auf die Intensivstation. [sitz]In einer Sondersitzung berichtet die Laborleiterin den drei Geschäftsführern Eberhard, "
     "Almut und Hauke.", 0.3),
    ("[l1]Einen Giftstoff finden wir nicht. Aber andere Ursachen scheiden aus.", 0.3, "Laborleiterin"),
    ("[e1]Ein Rückruf kostet uns ein Vermögen.", 0.2, "Eberhard"),
    ("[a1]Dann bleibt das Spray im Handel. Wir drucken einen Warnhinweis auf.", 0.3, "Almut"),
    ("[abst]Alle drei stimmen dafür, ein Rückruf unterbleibt. [vors]Weitere Erkrankungen halten sie für möglich und nehmen "
     "sie in Kauf. [weiter]In den folgenden Monaten bekommen weitere Kunden Atemnot, mit Dosen, die schon vor der Sitzung "
     "in den Läden standen.", 0.3),
    ("[h1]Meine Stimme hätte nichts geändert. Die anderen hätten mich überstimmt.", 0.3, "Hauke"),
    ("[frage]Haben sich die drei strafbar gemacht, obwohl sie nichts getan haben? [frage2]Und haftet auch Hauke?", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall ----------------------------------------------------------------------------------------------------------
    ("[bgh]Das ist dem Lederspray-Fall nachgebildet, Bundesgerichtshof, Urteil vom sechsten Juli neunzehnhundertneunzig. "
     "[bgh2]Nach Meldungen über Atembeschwerden beschloss die Geschäftsführung eines Herstellers "
     "im Mai neunzehnhunderteinundachtzig einstimmig, nicht zurückzurufen. [bgh3]Zurückgerufen wurde erst über zwei Jahre später. [bgh4]Der BGH bestätigte im Kern die Verurteilungen der "
     "Geschäftsführer wegen fahrlässiger und gefährlicher Körperverletzung.", PS),
    # --- D Tun oder Unterlassen ----------------------------------------------------------------------------------------------------
    ("[tun]Vorab: Tun oder Unterlassen? [tun2]Dosen, die die Firma nach der Sitzung noch verkauft: Das ist "
     "Tun. [unterl]Bei den Dosen, die schon in den Läden stehen, geht es um den unterlassenen Rückruf. "
     "[unterl2]Diesen Teil prüfen wir.", PS),
    # --- E Wortlautkarte § 13 Abs. 1 -----------------------------------------------------------------------------------------------
    ("[p13]Paragraf dreizehn Absatz eins: Wer es unterlässt, einen Erfolg abzuwenden, ist nur dann strafbar, [einst]wenn er "
     "rechtlich dafür einzustehen hat, dass der Erfolg nicht eintritt, [entspr]und wenn das Unterlassen einem Tun "
     "entspricht. [entspr2]Bei der Körperverletzung ist die Entsprechung regelmäßig unproblematisch.", PS),
    # --- F 1. Erfolg und Kausalität des Produkts -----------------------------------------------------------------------------------
    ("[erfolg]Erstens der Erfolg: Atemnot ist eine Gesundheitsschädigung, Paragraf "
     "zweihundertdreiundzwanzig. [kaus]Aber ist das Spray die Ursache, wenn niemand weiß, welcher Stoff wirkt? [kaus2]Der BGH "
     "sagt: Ja. Den Wirkmechanismus muss man nicht kennen. [kaus3]Es genügt, dass alle anderen in Betracht kommenden "
     "Ursachen ausgeschlossen sind.", PS),
    # --- G 2. Garantenstellung aus Ingerenz ----------------------------------------------------------------------------------------
    ("[garant]Zweitens die Garantenstellung. Der BGH stützt sie auf In-gerenz, also pflichtwidriges Vorverhalten: [ing]Wer "
     "gesundheitsgefährdende Produkte in den Verkehr bringt, muss den drohenden Schaden abwenden. [objektiv]Objektive "
     "Pflichtwidrigkeit genügt, Verschulden ist nicht nötig. [zivil]Ob schon die zivilrechtliche Produktbeobachtungspflicht "
     "reicht, ließ der Senat offen.", PS),
    # --- H Rückrufpflicht, Generalverantwortung ------------------------------------------------------------------------------------
    ("[rueck]Aus der Garantenstellung folgt die Pflicht zum Rückruf. [warn]Ein Warnhinweis reicht nicht, er erreicht die "
     "Dosen in den Läden nicht mehr. [kosten]Und Kosten, Ruf und Gewinn müssen hier hinter der Gesundheit zurücktreten. "
     "[gesamt]In der Krise ist jeder Geschäftsführer zuständig, egal wie die Ressorts "
     "verteilt sind.", PS),
    # --- I Handlungspflicht des Einzelnen ------------------------------------------------------------------------------------------
    ("[einzel]Was schuldet der Einzelne? Allein darf er den Rückruf nicht anordnen, die Geschäftsführer entscheiden "
     "gemeinsam. [moegl]Jeder muss deshalb alles ihm Mögliche und Zumutbare tun, damit ein Rückrufbeschluss zustande kommt. "
     "[keiner]Das hat keiner der drei getan.", PS),
    # --- J 3. Quasikausalität und der Einwand ---------------------------------------------------------------------------------------
    ("[quasi]Drittens die Kausalität. Ein Unterlassen ist ursächlich, wenn die gebotene Handlung den Erfolg mit an "
     "Sicherheit grenzender Wahrscheinlichkeit verhindert hätte. [quasi2]Ein sofortiger Rückruf hätte die Läden rechtzeitig "
     "erreicht. [einwand]Und der Einwand von Hauke? Allein hätte er nichts "
     "geändert. [mitt]Der BGH löst das über die Mittäterschaft.", PS),
    # --- K Wortlautkarte § 25 Abs. 2 -----------------------------------------------------------------------------------------------
    ("[p25]Paragraf fünfundzwanzig Absatz zwei: Begehen mehrere die Straftat gemeinschaftlich, so wird jeder als Täter "
     "bestraft. [gemein]Das geht auch beim Unterlassen: Mehrere Garanten können ihre Pflicht nur gemeinsam erfüllen und "
     "beschließen gemeinsam, es nicht zu tun. [zurech]Dann wird jedem das Unterlassen aller zugerechnet, und der gemeinsame "
     "Rückruf hätte die Schäden verhindert.", PS),
    # --- L Fahrlässigkeit: Teilbeitrag ---------------------------------------------------------------------------------------------
    ("[fahr]Bei Fahrlässigkeit stellt der BGH auf den Teilbeitrag ab: Im Zusammenwirken mit den "
     "anderen ist jeder ursächlich. [frei]Entlastet ist nur, wer alles ihm Mögliche und Zumutbare getan hat.", PS),
    # --- M 4. Vorsatz und Fahrlässigkeit ---------------------------------------------------------------------------------------------
    ("[vorsatz]Viertens der Vorsatz. Ab der Sondersitzung kennen die drei die Gefahr und nehmen weitere Erkrankungen in Kauf: "
     "bedingter Vorsatz. [vorher]Für Kunden, die schon vor der Sitzung erkrankten, kommt nur fahrlässige Körperverletzung "
     "durch Unterlassen in Betracht, Paragraf zweihundertneunundzwanzig. So trennte auch der BGH.", PS),
    # --- N § 224 Abs. 1 ------------------------------------------------------------------------------------------------------------
    ("[p224]Gefährlich ist die Körperverletzung nach Paragraf zweihundertvierundzwanzig Absatz eins Nummer fünf, wenn sie "
     "mittels einer das Leben gefährdenden Behandlung begangen wird. [leben]Der BGH bejahte diese Variante. [nr1]Nach dem Wortlaut kommt auch Nummer eins in Betracht, die "
     "Beibringung gesundheitsschädlicher Stoffe. [rw]Rechtfertigungsgründe fehlen, der Rückruf war zumutbar.", PS),
    # --- O Ergebnis ----------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Eberhard, Almut und Hauke sind strafbar wegen gefährlicher Körperverletzung durch Unterlassen in "
     "Mittäterschaft. [erg2]Für den Verkauf nach der Sitzung haften sie wegen Tuns.", PS),
    # --- P Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne zuerst Tun und Unterlassen nach den Dosen. "
     "[tipp2]Und prüfe die Kausalität im Gremium nicht Stimme für Stimme. [tipp3]Bei Vorsatz hilft die Mittäterschaft, bei "
     "Fahrlässigkeit das Zusammenwirken der Teilbeiträge.", PS),
    # --- Q Prüfschema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den unterlassenen Rückruf. [s0]Vorab: Tun oder Unterlassen? [s1]Römisch eins, Tatbestand, "
     "zuerst objektiv: [s1a]der Erfolg und die Ursächlichkeit des Produkts, [s1b]die Garantenstellung aus In-gerenz, "
     "[s1c]die Nichtvornahme des Einsatzes für den Rückruf, [s1d]die Quasikausalität, im "
     "Gremium über die Mittäterschaft, [s1e]die Entsprechung [s1f]und die Qualifikation nach Paragraf "
     "zweihundertvierundzwanzig. [s1g]Dann subjektiv der Vorsatz, sonst Paragraf zweihundertneunundzwanzig. [s2]Römisch zwei, "
     "Rechtswidrigkeit. [s3]Römisch drei, Schuld.", PS),
    # --- R Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer gesundheitsgefährdende Produkte in den Verkehr bringt, muss den Schaden abwenden, notfalls durch "
     "Rückruf. [m2]Im Gremium muss jeder alles ihm Mögliche und Zumutbare dafür tun. [m3]Der Hinweis, die anderen hätten "
     "ohnehin dagegen gestimmt, entlastet nicht.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
