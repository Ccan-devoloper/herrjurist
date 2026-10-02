"""Folge 055 · Ladendiebstahl: Wann ist die Ware weg? Gewahrsamsenklave erklärt (Mo · Der Fall · Strafrecht/StGB BT).
Fall nach dem Hook des Themenplans: Monika steckt im Supermarkt einen Lippenstift in ihre Jackentasche, Ladendetektiv
Rainer beobachtet alles über einen Deckenspiegel und spricht sie noch vor der Kasse ruhig an (keine Rangelei).
Vertieft gegenüber Folge 051 (dort Gewahrsamsenklave nur ein Satz): Vollendung der Wegnahme mit dem Einstecken kleiner,
leicht beweglicher Sachen in die Kleidung (BGH 5 StR 593/18 Rn. 3–5; 3 StR 556/09 Rn. 11 f.; beide unter Berufung auf
BGHSt 16, 271, 273 f., dessen Volltext nicht frei verfügbar ist), Beobachtung unerheblich, der Diebstahl ist keine
heimliche Tat (3 StR 556/09 Rn. 12; 3 StR 182/08 Rn. 8), kein gesicherter Gewahrsam nötig; Variante 1 Zurücklegen nach
Vollendung (§ 24 nur beim Versuch, § 46 II); Variante 2 schwere Kiste offen im Einkaufswagen (5 StR 593/18 Rn. 4;
2 StR 145/13 Rn. 3: keine Gewahrsamsenklave, versuchter Diebstahl; Rücktritt § 24); Variante 3 Versteck unter der Zeitung
im Wagen (BGHSt 41, 198 = 4 StR 234/95 Rn. 9–13, 18: Diebstahl statt Betrug, Vollendung Tatfrage); Folgen: Rücktritt,
§ 252 nur nach vollendetem Diebstahl (4 StR 234/95 Rn. 15, Ausblick); § 248a; § 127 Abs. 1 Satz 1 StPO (ein Satz).
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Namen nie im Genitiv mit -s (Erfahrung 015/047/051)."""

P, PS = 0.4, 0.45

STIMMEN = {"Monika": "laura_klar", "Rainer": "marc"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Supermarkt ----------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag im Supermarkt. [monika]Monika steht am Kosmetikregal. [lippen]Sie nimmt einen Lippenstift "
     "für neun Euro, [umsehen]schaut sich kurz um [tasche]und steckt ihn in ihre Jackentasche. Bezahlen will sie ihn nicht.", 0.3),
    ("[mo1]Den behalte ich einfach.", 0.3, "Monika"),
    ("[rainer]Was sie nicht weiß: [spiegel]Ladendetektiv Rainer beobachtet alles über einen Spiegel an der Decke. "
     "[kasse]Monika geht in Richtung Kasse. [anspr]Noch vor der Kasse spricht Rainer sie ruhig an.", 0.3),
    ("[ra1]Entschuldigung, ich bin der Ladendetektiv. Kommen Sie bitte kurz mit.", 0.4, "Rainer"),
    ("[frage]Hat Monika schon einen vollendeten Diebstahl begangen? [frage2]Sie ist noch im Laden, und der Detektiv hat "
     "alles gesehen. [frage3]Wir prüfen den Grundfall und drei Varianten.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt mit allen Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut ------------------------------------------------------------------------------------------------------
    ("[p242]Paragraf zweihundertzweiundvierzig, Absatz eins: [p242w]Wer eine fremde bewegliche Sache einem anderen in der "
     "Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf "
     "Jahren oder mit Geldstrafe bestraft. [abs2]Und Absatz zwei: Der Versuch ist strafbar. [kern]Ob vollendet oder "
     "versucht, entscheidet sich an der Wegnahme.", PS),
    # --- D Sache, Wegnahme, Gewahrsam des Supermarkts --------------------------------------------------------------------
    ("[sache]Der Lippenstift ist eine fremde bewegliche Sache, er gehört dem Supermarkt. [wegn]Wegnahme heißt nach dem "
     "Bundesgerichtshof: Bruch fremden und Begründung neuen Gewahrsams. [gewahr]Gewahrsam am Lippenstift hat zunächst "
     "der Supermarkt, denn das Regal steht in seinem Laden.", PS),
    # --- E Gewahrsamsenklave ---------------------------------------------------------------------------------------------
    ("[enkl]Jetzt der Kern: [klein]Bei kleinen, leicht beweglichen Sachen genügt nach dem Bundesgerichtshof schon das "
     "Einstecken in die Kleidung. [tasche2]Wer eine Sache in der Tasche seiner Kleidung trägt, dem weist die "
     "Verkehrsauffassung im Regelfall die Sachherrschaft zu, [mitten]auch wenn er noch im Laden steht. [enkl2]Die Jackentasche ist "
     "eine kleine eigene Gewahrsamssphäre mitten im fremden Bereich: eine Gewahrsamsenklave. [seit]Das hat der "
     "Bundesgerichtshof schon neunzehnhunderteinundsechzig entschieden und hält bis heute daran fest. [vollendet]Mit dem Einstecken ist "
     "die Wegnahme vollendet.", PS),
    # --- F Beobachtung, Ergebnis -----------------------------------------------------------------------------------------
    ("[beob]Aber der Detektiv hat doch alles gesehen? [heiml]Das ändert nichts. Der Diebstahl ist keine heimliche Tat. "
     "[chance]Die Beobachtung gibt dem Laden nur die Möglichkeit, sich die Sache zurückzuholen. [gesich]Gesicherten "
     "Gewahrsam braucht die Vollendung nicht. [subj]Monika will den Lippenstift behalten, ohne zu zahlen: Vorsatz und "
     "Zueignungsabsicht liegen vor. [erg]Rechtswidrigkeit und Schuld auch. [erg2]Monika hat einen vollendeten Diebstahl "
     "begangen.", PS),
    # --- G Variante 1: Zurücklegen nach Vollendung -----------------------------------------------------------------------
    ("[v1]Variante eins: Bevor Rainer sie anspricht, bekommt Monika ein schlechtes Gewissen und legt den Lippenstift von "
     "sich aus zurück ins Regal. [v1b]Rücktritt nach Paragraf vierundzwanzig? [v1c]Der befreit nur von der Strafe wegen "
     "Versuchs. [v1d]Die Tat ist aber schon vollendet. [v1e]Das Zurücklegen kann sich nur noch bei der Strafe "
     "auswirken.", PS),
    # --- H Variante 2: schwere Kiste offen im Einkaufswagen ---------------------------------------------------------------
    ("[v2]Variante zwei: Monika stellt eine schwere Kiste Wein offen in den Einkaufswagen. Sie will sie ohne Bezahlung "
     "hinausschieben. [v2b]Rainer spricht sie vor der Kasse an. [v2c]Bei umfangreichen, schweren Sachen macht der "
     "Bundesgerichtshof einen entscheidenden Unterschied: [v2d]Ihr Abtransport ist schwierig, und die Kiste steht offen "
     "im Wagen des Ladens. [v2e]Eine Gewahrsamsenklave entsteht so nicht. [v2f]Der Supermarkt hat noch Gewahrsam, es "
     "bleibt beim Versuch. [v2g]Und vom Versuch kann man zurücktreten: Hätte Monika die Kiste freiwillig "
     "zurückgestellt, wäre sie nach Paragraf vierundzwanzig straflos.", PS),
    # --- I Variante 3: Versteck unter der Zeitung ------------------------------------------------------------------------
    ("[v3]Variante drei: Monika versteckt den Lippenstift im Einkaufswagen unter einer Zeitung. [v3b]An der Kasse legt "
     "sie nur die übrigen Waren aufs Band und bezahlt sie. [v3c]Betrug? Nein. [v3d]Die Kassiererin verfügt nur über die "
     "Waren, die sie sieht und abrechnet, nicht über den versteckten Lippenstift. [v3e]Es bleibt Diebstahl. [v3f]Ob er "
     "schon vollendet ist oder erst versucht, hängt nach dem Bundesgerichtshof von den Umständen des Einzelfalls ab.", PS),
    # --- J Folgen: Rücktritt, § 252 --------------------------------------------------------------------------------------
    ("[folgen]Warum ist die Grenze so wichtig? [f1]Erstens der Rücktritt: Er ist nur bis zur Vollendung möglich. "
     "[p252]Zweitens ein Ausblick auf Paragraf zweihundertzweiundfünfzig, den räuberischen Diebstahl. [p252b]Er setzt "
     "einen vollendeten Diebstahl voraus. Würde Monika nach dem Einstecken Gewalt anwenden, um den Lippenstift zu "
     "behalten, käme er in Betracht. [p252c]Beim bloßen Versuch, wie bei der Kiste im Wagen, scheidet er aus.", PS),
    # --- K Strafantrag, Festnahme ----------------------------------------------------------------------------------------
    ("[p248a]Weil ein Lippenstift für neun Euro geringwertig ist, wird der Diebstahl nach Paragraf "
     "zweihundertachtundvierzig a nur auf Antrag verfolgt, [oeff]außer die Strafverfolgungsbehörde bejaht ein besonderes "
     "öffentliches Interesse. [p127]Und ein Satz zu Rainer: Wer auf frischer Tat betroffen ist, darf nach Paragraf "
     "hundertsiebenundzwanzig der Strafprozessordnung von jedermann vorläufig festgenommen werden, [p127b]wenn er "
     "fluchtverdächtig ist oder seine Identität nicht sofort festgestellt werden kann.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreibe nie: Sie wurde beobachtet, also nur Versuch. [tipp2]Prüfe die Vollendung an der "
     "Wegnahme: Wie groß ist die Sache, und wo steckt sie? [tipp3]Kleines in Kleidung oder Tasche: Gewahrsamsenklave. "
     "[tipp4]Großes offen im Einkaufswagen: noch keine Enklave. Dann prüfe den Versuch und den Rücktritt.", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s_i]Römisch eins: Tatbestand. [s1a]Objektiv: fremde bewegliche Sache [s1b]und Wegnahme, "
     "also Bruch fremden und Begründung neuen Gewahrsams. [s1c]Bei kleinen Sachen in Kleidung oder Tasche: "
     "Gewahrsamsenklave, Beobachtung unerheblich. [s1d]Subjektiv: Vorsatz und Absicht rechtswidriger Zueignung. "
     "[s_ii]Römisch zwei: Rechtswidrigkeit. [s_iii]Römisch drei: Schuld. [s_iv]Römisch vier: Strafantrag bei "
     "geringwertigen Sachen. [s_v]Fehlt die Vollendung: Versuch nach Paragraf zweihundertzweiundvierzig Absatz zwei, "
     "mit Rücktritt nach Paragraf vierundzwanzig.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer eine kleine Sache in Kleidung oder Tasche steckt, hat sie in der Regel schon weggenommen, mitten im Laden und vor "
     "den Augen des Detektivs. [m_2]Große Ware offen im Einkaufswagen bildet keine solche Enklave. [m_3]Und zurücktreten "
     "kann nur, wer die Tat noch nicht vollendet hat.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
