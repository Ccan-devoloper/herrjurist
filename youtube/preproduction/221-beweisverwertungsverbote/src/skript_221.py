"""Folge 221 · Beweisverwertungsverbote StPO: Das System (Mi · Examenswissen · StPO · Format Schema).
Hook nach dem Themenplan: drei Ermittlungsfehler, drei Ergebnisse – warum nicht jeder Fehler zum Freispruch führt.
(1) Der Kommissar droht Herrn Kleinert in der Vernehmung mit Schmerzen; Geständnis. (2) Eine Polizistin sieht Herrn
Haferkamp einen Wagen zerkratzen und fragt ihn ohne Belehrung; Geständnis; die Verteidigerin widerspricht rechtzeitig.
(3) Ein Polizist durchsucht die Wohnung von Frau Ruhnke ohne Beschluss, weil er Gefahr im Verzug annimmt (Richter nicht
sofort erreicht, keine konkreten Anhaltspunkte); er findet gestohlene Laptops.
System: Erhebungs- vs. Verwertungsverbot (BGHSt 51, 285 Rn. 20; BVerfG 2 BvR 2225/08 Rn. 16) → gesetzliche Verbote,
unselbständig/selbständig (BGH 1 StR 54/24 Rn. 18, 24; BGH 2 StR 509/10 Rn. 21): § 136a Abs. 3 S. 2, § 252 (BGH GSSt 1/16
Rn. 32), § 100d Abs. 2 S. 1, § 479 Abs. 2 S. 1 i. V. m. § 161 Abs. 3 S. 1 StPO → ungeschriebene Verbote: Abwägungslehre
(1 StR 54/24 Rn. 24), Rechtskreistheorie (4 StR 61/22 Rn. 12), Widerspruchslösung (BGHSt 38, 214, 225 f.; Verweis 132/171)
→ Reichweite: Fernwirkung grundsätzlich nein (1 StR 316/05 Rn. 22 f.; Verweis 211), Fortwirkung/qualifizierte Belehrung
(3 StR 390/17 Rn. 28) → Lösung der drei Fälle (Fall 3: BGHSt 51, 285 Rn. 22, 24; BVerfGE 103, 142 Rn. 38; Verweis 151)
→ Klausurtipp mit Prüfungsschema I.–V. (Lexi) → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, in keiner früheren Folge, reserviert): Kleinert, Haferkamp, Ruhnke; Kommissar, Polizistin,
Polizist und Verteidigerin bleiben Funktionsrollen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Kommissar": "christian", "Polizistin": "lucy", "Haferkamp": "stephan", "Ruhnke": "hilde"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall 1: Vernehmungsraum --------------------------------------------------------------------------------------
    ("[fall]Drei Ermittlungsfehler. [f1]Erster Fall: Im Vernehmungsraum sitzt Herr Kleinert. [verd]Er soll in einen "
     "Kiosk eingebrochen sein. [ungeduld]Der Kommissar wird ungeduldig.", 0.2),
    ("[k1]Reden Sie endlich. Sonst wird es für Sie schmerzhaft.", 0.35, "Kommissar"),
    ("[ges1]Herr Kleinert bekommt Angst und gesteht.", 0.5),
    # --- B Fall 2: Straße und Hauptverhandlung --------------------------------------------------------------------------
    ("[f2]Zweiter Fall: Eine Polizistin sieht, wie Herr Haferkamp mit einem Schlüssel den Lack eines fremden Autos "
     "zerkratzt. [ohne]Sie fragt ihn sofort, ohne ihn zu belehren.", 0.2),
    ("[p2]Warum haben Sie das gemacht?", 0.3, "Polizistin"),
    ("[h2]Weil der ständig vor meiner Einfahrt parkt!", 0.35, "Haferkamp"),
    ("[hv2]In der Hauptverhandlung widerspricht seine Verteidigerin rechtzeitig der Verwertung dieser Aussage.", 0.5),
    # --- C Fall 3: Wohnungstür ------------------------------------------------------------------------------------------
    ("[f3]Dritter Fall: Über das Verkaufskonto [konto]von Frau Ruhnke werden gestohlene Laptops angeboten. [anruf]Ein "
     "Polizist ruft den Bereitschaftsrichter an, erreicht ihn aber nicht sofort. [giv]Aus Sorge, die Geräte könnten "
     "verschwinden, ordnet er die Durchsuchung selbst an: Gefahr im Verzug, meint er. [konkret]Konkrete Anhaltspunkte "
     "dafür gibt es nicht.", 0.2),
    ("[r3]Haben Sie überhaupt einen Durchsuchungsbeschluss?", 0.35, "Ruhnke"),
    ("[fund]Im Schrank liegen die Laptops.", 0.5),
    # --- D Drei Kacheln --------------------------------------------------------------------------------------------------
    ("[drei]Drei Fehler: [d1]eine Drohung, [d2]eine fehlende Belehrung, [d3]eine Durchsuchung ohne Beschluss. "
     "[frage]Welche Beweise darf das Gericht verwerten, und warum führt nicht jeder Fehler zum Freispruch?", 0.6),
    # --- E Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier sind die drei Fälle zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Erhebung und Verwertung -------------------------------------------------------------------------------------
    ("[ebv]Ein Beweiserhebungsverbot regelt, ob und wie Beweise gewonnen werden dürfen. [bvv]Ein Beweisverwertungsverbot sagt, "
     "ob das Gericht einen Beweis im Urteil verwenden darf. [nicht]Nicht jeder Erhebungsfehler führt zu einem "
     "Verwertungsverbot, [ausn]denn das Gericht soll die Wahrheit erforschen.", P),
    # --- G Gesetzliche Verbote: Überblick ------------------------------------------------------------------------------
    ("[gesetz]Erste Gruppe: Verwertungsverbote, die das Gesetz ausdrücklich regelt. [unselb]Knüpft ein "
     "Verbot an einen Fehler bei der Erhebung an, nennt man es unselbständig. [selb]Folgt es unabhängig davon unmittelbar "
     "aus der Verfassung, heißt es selbständig.", P),
    # --- H § 136a Abs. 3 S. 2 ---------------------------------------------------------------------------------------------
    ("[a136]Unselbständig ist etwa Paragraf hundertsechsunddreißig a. [a136b]Er verbietet "
     "etwa Misshandlung, Täuschung und die Drohung mit einer unzulässigen Maßnahme. [a136c]Absatz drei Satz zwei: "
     "Aussagen, die unter Verletzung dieses Verbots zustande gekommen sind, dürfen auch dann nicht verwertet werden, "
     "wenn der Beschuldigte der Verwertung zustimmt. [abs]Abgewogen wird hier nicht.", P),
    # --- I § 252 ----------------------------------------------------------------------------------------------------------
    ("[a252]Paragraf zweihundertzweiundfünfzig schützt etwa Angehörige, die das Zeugnis verweigern: [a252b]Verweigert "
     "ein Zeuge erst in der Hauptverhandlung das Zeugnis, darf seine frühere Aussage nicht verlesen werden. "
     "[a252d]Die Rechtsprechung macht daraus ein Verwertungsverbot: Auch der Polizist, der ihn vernommen hat, darf "
     "darüber grundsätzlich nicht aussagen. [a252e]Ausnahme: eine Aussage vor dem Richter nach Belehrung.", P),
    # --- J § 100d Abs. 2 und § 479 Abs. 2 ------------------------------------------------------------------------------------
    ("[a100]Paragraf hundert d Absatz zwei schützt den Kernbereich privater Lebensgestaltung, "
     "das klassische Feld selbständiger Verbote aus der Verfassung. [a100b]Erkenntnisse aus diesem Kernbereich, etwa aus einer "
     "Telefonüberwachung, dürfen nicht verwertet werden.", P),
    ("[a479]Paragraf vierhundertneunundsiebzig Absatz zwei regelt mit Paragraf hunderteinundsechzig Absatz drei andere "
     "Strafverfahren: [a479b]Daten aus Maßnahmen, die nur bei bestimmten Straftaten erlaubt sind, [a479c]dürfen dort als "
     "Beweis nur für Taten verwendet werden, für die die Maßnahme zulässig gewesen wäre.", PS),
    # --- K Ungeschriebene Verbote: Abwägungslehre ------------------------------------------------------------------------
    ("[unge]Zweite Gruppe: Verbote, die nicht im Gesetz stehen. [abwl]Hier wägt die Rechtsprechung ab. [auf]Auf der einen "
     "Seite steht das Aufklärungsinteresse, etwa die Schwere der Tat. [gew]Auf der anderen das Gewicht des "
     "Verstoßes: [k_vors]Wurde bewusst oder nur fahrlässig gehandelt? [k_zweck]Welchen Schutzzweck hat die verletzte "
     "Vorschrift? [k_hypo]Hätte man den Beweis auch rechtmäßig erlangen können? [grob]Ein Verwertungsverbot nimmt der "
     "Bundesgerichtshof vor allem bei bewusster Missachtung oder grober Verkennung der Rechtslage an.", P),
    # --- L Rechtskreis und Widerspruch ------------------------------------------------------------------------------------
    ("[rkt]Dazu kommt die Rechtskreistheorie: [rkt2]Dient die verletzte Vorschrift nicht dem Schutz des Beschuldigten, "
     "kann er sich nicht auf ein Verwertungsverbot berufen.", P),
    ("[wl]Beim Belehrungsfehler verlangt der Bundesgerichtshof zudem: [wl2]Der verteidigte "
     "Angeklagte muss der Verwertung in der Hauptverhandlung widersprechen, spätestens in seiner Erklärung nach der "
     "Beweiserhebung. [wl3]Sonst bleibt die Aussage verwertbar. [verw]Mehr dazu in unseren Folgen zur "
     "Widerspruchslösung und zum Belehrungsverstoß.", PS),
    # --- M Reichweite: Fernwirkung und Fortwirkung ------------------------------------------------------------------------
    ("[fern]Und wie weit reicht ein Verbot? [fern2]Erfasst es auch Beweise, die die Polizei erst durch eine "
     "unverwertbare Aussage findet? Diese Fernwirkung lehnt der Bundesgerichtshof grundsätzlich ab. [fern3]Mehr dazu in "
     "unserer Folge zum Fall Gäfgen. [fort]Anders die Fortwirkung: Nach einem Belehrungsfehler muss der Beschuldigte "
     "vor einer neuen Vernehmung erfahren, dass seine frühere Aussage unverwertbar ist: [qual]die qualifizierte "
     "Belehrung.", PS),
    # --- N Lösung der drei Fälle ------------------------------------------------------------------------------------------
    ("[l1]Zurück zu den Fällen. [l1a]Der Kommissar hat Herrn Kleinert mit Schmerzen gedroht, einer unzulässigen "
     "Maßnahme. [l1b]Sein Geständnis ist nach Paragraf hundertsechsunddreißig a unverwertbar, selbst wenn er zustimmt.", P),
    ("[l2]Herrn Haferkamp hätte die Polizistin über sein Schweigerecht belehren müssen. [l2a]Seine Verteidigerin hat "
     "rechtzeitig widersprochen, also ist seine Aussage unverwertbar. [l2b]Freigesprochen ist er damit aber nicht automatisch: "
     "[l2c]Die Polizistin hat die Tat selbst gesehen und kann als Zeugin aussagen.", P),
    ("[l3]Bei Frau Ruhnke genügte die bloße Befürchtung nicht für Gefahr im Verzug. [l3a]Die Durchsuchung verletzte "
     "den Richtervorbehalt. [l3b]Aber der Polizist hatte versucht, den Richter zu erreichen, [l3c]und wegen des "
     "Verkaufskontos hätte er den Beschluss sehr wahrscheinlich bekommen. [l3d]Bewusst oder grob war der Verstoß nicht. "
     "[l3e]Die Abwägung spricht deshalb für die Verwertung: Die Laptops sind verwertbar. [l3f]Mehr dazu in unserer "
     "Folge zur Durchsuchung.", PS),
    # --- O Klausurtipp mit Prüfungsschema (Lexi) ---------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüf in dieser Reihenfolge. [s1]Erstens: Wurde ein Beweiserhebungsverbot "
     "verletzt? [s2]Zweitens: Ordnet das Gesetz ein Verwertungsverbot an? [s3]Drittens: Wenn nicht, wäge ab und denk an "
     "den Rechtskreis. [s4]Viertens: Ist ein Widerspruch nötig, und kam er rechtzeitig? [s5]Fünftens: die Reichweite, "
     "also Fortwirkung und Fernwirkung.", PS),
    # --- P Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Fehler bei der Erhebung macht einen Beweis nicht automatisch unverwertbar. [mz]Entscheidend ist, "
     "ob das Gesetz ein Verbot anordnet oder die Abwägung es verlangt.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = "".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
