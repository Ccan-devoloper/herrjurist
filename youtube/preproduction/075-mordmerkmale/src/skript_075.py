"""Folge 075 · Mordmerkmale § 211 StGB: Mord oder Totschlag? Alle Gruppen (Fr · Klausurpraxis · StGB BT, Format Schema).
Zwei Übungsfälle nach dem Plan-Hook, sehr zurückhaltend dargestellt (kein Messer, kein Stich, kein Blut, keine Leiche; nur
Gewitterwolke für die Wut, Testament/Haus für die Erbschaft, Grablicht dezent, Gerichtssymbol; Täter und Opfer nur als
neutrale Figuren vor der Tat): (1) Norbert tötet seinen Nachbarn Horst nach monatelangem Streit um die Hofeinfahrt in spontaner
Wut; Horst rechnet im Streit mit einem Angriff. (2) Friederike tötet ihren Onkel Dietmar, um früher zu erben.
Aufbau: § 212 Ausgangspunkt → Mord = zusätzliches Mordmerkmal → Streit Rspr./Lehre (BGH 5 StR 341/05 Rn. 45 f.), § 28
(ein Satz) → Rechtsfolge lebenslang (§ 211 I) → Wortlautkarte § 211 II, drei Gruppen progressiv → 1. Gruppe: Mordlust
(5 StR 257/19 Rn. 15), Geschlechtstrieb (nur genannt), Habgier (4 StR 140/20 Rn. 4) mit Erbschaft-Fall, niedrige
Beweggründe (6 StR 365/23 Rn. 17) mit Wut-Fall → 2. Gruppe: Heimtücke (2 StR 352/24 Rn. 25, 26; 5 StR 423/25 Rn. 13;
Ausnutzungsbewusstsein 2 StR 352/24 Rn. 32; feindliche Willensrichtung BGHSt 64, 111 Rn. 28), grausam (5 StR 236/19 Rn. 12),
gemeingefährliche Mittel (4 StR 482/19 Rn. 49) → 3. Gruppe: Ermöglichung (2 StR 422/14 Rn. 10), Verdeckung
(4 StR 356/21 Rn. 8) → Ergebnis beide Fälle → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Norbert, Horst, Dietmar, Friederike.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Norbert": "marc", "Dietmar": "william", "Friederike": "sabrina"}  # Lexi = Erzählerstimme (Carla); Horst spricht nicht

SEGMENTE = [
    # --- A Fall 1: Streit an der Hofeinfahrt ---------------------------------------------------------------------------------
    ("[fall]Zwei Fälle, zwei Tote, und von außen sieht alles gleich aus. [norbert]Erster Fall: Norbert und sein Nachbar "
     "Horst streiten seit Monaten um die gemeinsame Hofeinfahrt. [abend]An einem Abend geraten sie wieder aneinander. "
     "[rechnet]Horst rechnet schon damit, dass Norbert gleich auf ihn losgeht.", 0.3),
    ("[n1]Jetzt reicht es mir endgültig!", 0.3, "Norbert"),
    ("[wut]In spontaner Wut tötet Norbert Horst, mit Tötungsvorsatz.", 0.6),
    # --- A2 Fall 2: die Erbschaft ----------------------------------------------------------------------------------------------
    ("[dietmar]Zweiter Fall: Friederike ist die einzige Erbin ihres Onkels Dietmar.", 0.3),
    ("[d1]Mein Haus und mein Geld bekommst du einmal, Friederike.", 0.3, "Dietmar"),
    ("[allein]Später, allein:", 0.2),
    ("[f1]Ich will das Erbe nicht erst in zwanzig Jahren.", 0.3, "Friederike"),
    ("[tat2]Um früher an sein Vermögen zu kommen, tötet sie ihren Onkel, auf genau die gleiche Weise wie Norbert. "
     "[frage]Zweimal dieselbe Tathandlung. [frage2]Ist beides Mord? Oder einmal nur Totschlag?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier sind beide Fälle zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Totschlag und Mord ----------------------------------------------------------------------------------------------------
    ("[p212]Ausgangspunkt ist der Totschlag, Paragraf zweihundertzwölf: Wer einen Menschen tötet, ohne Mörder zu sein. "
     "[beide]Vorsätzlich einen Menschen getötet haben Norbert und Friederike beide. [p211]Mord ist es erst, wenn zusätzlich ein "
     "Mordmerkmal vorliegt. [streit]Die Lehre sieht im Mord eine Qualifikation des Totschlags, der Bundesgerichtshof bisher "
     "einen selbständigen Tatbestand. [p28]Bedeutung hat das vor allem für Teilnehmer, über Paragraf achtundzwanzig. "
     "[lebensl]Die Strafe für Mord: lebenslange Freiheitsstrafe.", PS),
    # --- D Wortlautkarte § 211 Abs. 2, drei Gruppen ---------------------------------------------------------------------------
    ("[wl]Die Mordmerkmale stehen in Paragraf zweihundertelf Absatz zwei. [gruppen]Man ordnet sie in drei Gruppen. "
     "[g1]Die erste Gruppe betrifft das Motiv, [g2]die zweite die Art der Tatausführung, [g3]die dritte den Zweck der Tat.", PS),
    # --- E Erste Gruppe: Mordlust, Geschlechtstrieb, Habgier ------------------------------------------------------------------
    ("[mlust]Erste Gruppe. Aus Mordlust tötet nach dem Bundesgerichtshof etwa, wer aus Freude an der Vernichtung eines "
     "Menschenlebens tötet. [sex]Daneben nennt das Gesetz die Tötung zur Befriedigung des Geschlechtstriebs. [habgier]Habgier "
     "ist ein Streben nach materiellen Gütern, das in seiner Hemmungslosigkeit und Rücksichtslosigkeit das erträgliche Maß "
     "weit übersteigt. [vermehr]Durch den Tod soll sich das Vermögen des Täters vermehren, zumindest nach seiner Vorstellung. "
     "[erbe]Genau so liegt es bei Friederike: Sie tötet, um früher zu erben. [hab_ja]Habgier liegt vor.", PS),
    # --- F Erste Gruppe: sonstige niedrige Beweggründe -------------------------------------------------------------------------
    ("[niedrig]Bleiben die sonstigen niedrigen Beweggründe. Niedrig ist ein Motiv, das nach allgemeiner sittlicher Wertung auf "
     "tiefster Stufe steht und deshalb besonders verachtenswert ist. [gesamt]Das klärt eine Gesamtwürdigung aller äußeren und "
     "inneren Umstände. [wutbgh]Wut oder Zorn genügen nach dem Bundesgerichtshof nur, wenn sie nicht menschlich verständlich, "
     "sondern Ausdruck einer niedrigen Gesinnung sind. [wutfall]Bei Norbert nennt der Sachverhalt nur die spontane Wut in "
     "einem langen Streit, nichts weiter. [nb_nein]Ein niedriger Beweggrund lässt sich damit nicht begründen.", PS),
    # --- G Zweite Gruppe: Heimtücke ---------------------------------------------------------------------------------------------
    ("[heim]Zweite Gruppe. Heimtückisch handelt, wer in feindlicher Willensrichtung die Arg- und Wehrlosigkeit des Opfers "
     "bewusst zur Tötung ausnutzt. [arglos]Arglos ist, wer bei Beginn des ersten mit Tötungsvorsatz geführten Angriffs nicht "
     "mit einem erheblichen Angriff rechnet. [wehrlos]Wehrlos ist, wessen Verteidigungsfähigkeit infolge der Arglosigkeit "
     "aufgehoben oder erheblich eingeschränkt ist. [ausnutz]Und der Täter muss diese Lage bewusst ausnutzen. [feind]Die "
     "feindliche Willensrichtung fehlt nur ausnahmsweise, etwa wenn die Tötung dem ausdrücklichen Willen des Opfers entspricht. "
     "[horst]Horst rechnete im Streit mit einem Angriff. Er war nicht arglos, Heimtücke scheidet aus.", PS),
    # --- H Zweite Gruppe: grausam, gemeingefährliche Mittel --------------------------------------------------------------------
    ("[grausam]Grausam tötet, wer dem Opfer in gefühlloser, unbarmherziger Gesinnung Schmerzen oder Qualen zufügt, die nach "
     "Stärke und Dauer über das für die Tötung erforderliche Maß hinausgehen. [gemein]Gemeingefährlich ist ein Mittel, das in "
     "der konkreten Lage eine Mehrzahl von Menschen an Leib und Leben gefährden kann, weil der Täter die Ausdehnung der Gefahr "
     "nicht in seiner Gewalt hat.", PS),
    # --- I Dritte Gruppe: Ermöglichung, Verdeckung -----------------------------------------------------------------------------
    ("[g3a]Dritte Gruppe. Zur Ermöglichung einer anderen Straftat tötet, wer einen Menschen tötet, um ein weiteres kriminelles "
     "Ziel zu erreichen. [verdeck]In Verdeckungsabsicht tötet, wer dadurch eine vorangegangene Straftat verdecken will, oder "
     "Spuren, die Aufschluss über bedeutsame Tatumstände geben könnten. [keins]In unseren beiden Fällen spielt das keine Rolle.", PS),
    # --- J Ergebnis -----------------------------------------------------------------------------------------------------------------
    ("[erg]Also: gleiche Tat, verschiedene Motive. [erg1]Norbert ist wegen Totschlags strafbar, weil kein Mordmerkmal vorliegt. "
     "[erg2]Friederike ist wegen Mordes aus Habgier strafbar.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die vorsätzliche Tötung als Grunddelikt, danach die Mordmerkmale. [tipp2]Die Merkmale der "
     "zweiten Gruppe sind tatbezogen: Sie gehören in den objektiven Tatbestand, und der Vorsatz muss sie umfassen. [tipp3]Die "
     "Merkmale der ersten und dritten Gruppe sind täterbezogen und gehören in den subjektiven Tatbestand.", PS),
    # --- L Klausurschema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand. Objektiv: die Tötung eines Menschen [k1b]und die tatbezogenen "
     "Mordmerkmale der zweiten Gruppe. [k2]Subjektiv: Vorsatz, auch für diese Merkmale, [k2b]dazu die täterbezogenen Merkmale "
     "der ersten und dritten Gruppe. [k3]Römisch zwei, Rechtswidrigkeit. [k4]Römisch drei, Schuld.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Mord ist eine vorsätzliche Tötung mit Mordmerkmal. [m2]Die erste Gruppe fragt nach dem Motiv, die zweite "
     "nach der Art der Tat, die dritte nach dem Zweck. [m3]Spontane Wut allein macht noch keinen Mord.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
