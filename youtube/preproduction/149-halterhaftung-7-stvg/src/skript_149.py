"""Folge 149 · Halterhaftung § 7 StVG: Wer zahlt beim Parkplatzrempler? (Mi · Examenswissen · Deliktsrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Beim Ausparken touchieren sich zwei Autos – keiner will schuld sein“): Auf dem
Parkplatz eines Supermarkts setzen Heidrun und Volkmar gleichzeitig rückwärts aus gegenüberliegenden Parklücken; die Hecks
berühren sich, leichter Blechschaden (Heidrun: Reparatur 1.600 €), niemand verletzt. Unstreitig rollten beide noch, als
sich die Autos berührten; mehr lässt sich nicht aufklären. Beide fahren ihr eigenes Auto (Halter und Fahrer zugleich);
Volkmars Auto ist haftpflichtversichert. Heidrun verlangt Ersatz von Volkmar.
Prüfung: Aufbau (§ 7 → § 18 → § 17) → I. § 7 Abs. 1 StVG (Wortlautkarte, wörtlich), Gefährdungshaftung (BGH VI ZR 150/12
Rn. 17; VI ZR 265/14 Rn. 5 „Preis“), Halter, Betrieb (VI ZR 265/14 Rn. 5: weit, Gefahren ausgewirkt), Rechtsgutverletzung,
haftungsbegründende Kausalität; § 7 Abs. 2 höhere Gewalt (Wortlautkarte, ein Satz; VI ZR 6/15 Rn. 9) → II. § 18 Abs. 1
(Wortlautkarte), vermutetes Verschulden, Entlastung nach S. 2 (VI ZR 150/12 Rn. 13, 18), Verweis Folge 147 (ein Satz) →
III. § 17 Abs. 1, 2 (Wortlautkarte Abs. 1), Betriebsgefahr als Sockel, nur bewiesene Umstände (VI ZR 66/16 Rn. 7, 12),
§ 17 Abs. 3 Idealfahrer kurz (VI ZR 18/24 Rn. 15), § 9 StVG / § 254 BGB ein Satz → Parkplatz: StVO anwendbar, kein
„rechts vor links“ ohne Straßencharakter (VI ZR 344/21 Rn. 12, 15, 17 f.), § 1 Abs. 2 StVO, sofort anhalten können
(VI ZR 179/15 Rn. 11), Anscheinsbeweis nur gegen den, der im Kollisionszeitpunkt noch rollte (VI ZR 6/15 Rn. 15;
VI ZR 66/16 Rn. 9 f.), Betriebsgefahr zählt trotzdem (VI ZR 66/16 Rn. 12) → Lösung: Anschein gegen beide, gleiche
Beiträge, im Fall Teilung je zur Hälfte (Ergebnis der Abwägung im Fall, keine Pauschalquote) → Gegenfall (Volkmar stand) →
Klausurtipp (Reihenfolge; § 115 Abs. 1 VVG Direktanspruch; § 823 BGB verwiesen auf Folge 067) → Schema → Merksatz.
Abweichung vom Auftrag: „VI ZR 177/16 (2017)“ ist kein Parkplatzurteil; gemeint ist BGH, Urt. v. 11.10.2016 – VI ZR 66/16.
Die Plan-Lösung „beide bewegten sich, kein Anschein“ ist nach VI ZR 66/16 Rn. 9 korrigiert: Rollten beide noch, spricht der
Anschein gegen beide. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Heidrun, Volkmar
(nie im Genitiv). Stimmen: Heidrun sabrina, Volkmar marc. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; StVG, StVO und VVG ausgeschrieben (synth_el kennt die Abkürzungen nicht)."""

P, PS = 0.3, 0.5

STIMMEN = {"Heidrun": "sabrina", "Volkmar": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Parkplatz --------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag auf dem Parkplatz eines Supermarkts. [heid]Heidrun hat ihren Einkauf eingeladen und setzt "
     "rückwärts aus der Parklücke. [volk]Genau gegenüber setzt auch Volkmar zurück. [roll]Langsam rollen beide aufeinander "
     "zu, [kontakt]bis sich die Hecks berühren. [schaden]Verletzt ist niemand, aber beide Stoßstangen haben Kratzer.", P),
    ("[h1]Sie sind mir hinten reingefahren!", P, "Heidrun"),
    ("[v1]Ich? Sie haben doch auch nicht nach hinten geschaut!", P, "Volkmar"),
    # --- A2 Fall: die Frage -------------------------------------------------------------------------------------------------
    ("[keiner]Keiner will schuld sein. [beide]Unstreitig ist nur: Beide rollten noch, als sich die Autos berührten. "
     "[rep]Heidrun verlangt von Volkmar die Reparaturkosten, tausendsechshundert Euro. [frage]Haftet Volkmar, ohne dass Heidrun ihm "
     "ein Verschulden beweisen muss? [frage2]Und wie teilt man, wenn beide beteiligt sind?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau ------------------------------------------------------------------------------------------------------------
    ("[aufbau]Wir prüfen das Straßenverkehrsgesetz in drei Schritten: [w7]Paragraf sieben, die Haftung des Halters, "
     "[w18]Paragraf achtzehn, die Haftung des Fahrers, [w17]und Paragraf siebzehn, die Verteilung, wenn zwei Autos beteiligt sind.", PS),
    # --- D § 7 Abs. 1 und Abs. 2 ----------------------------------------------------------------------------------------------
    ("[p7]Paragraf sieben Absatz eins: Wird bei dem Betrieb eines Kraftfahrzeugs ein Mensch getötet, der Körper oder die "
     "Gesundheit eines Menschen verletzt oder eine Sache beschädigt, so ist der Halter verpflichtet, dem Verletzten den daraus "
     "entstehenden Schaden zu ersetzen. [gef]Von Verschulden steht da nichts. Das ist Gefährdungshaftung. [preis]Nach dem "
     "Bundesgerichtshof ist sie der Preis dafür, dass der Halter erlaubterweise eine Gefahrenquelle eröffnet.", P),
    ("[halter]Erstens: Volkmar fährt sein eigenes Auto, er ist Halter. [betr]Zweitens: bei dem Betrieb. Der "
     "Bundesgerichtshof legt das weit aus: Es genügt, dass sich die Gefahren des Autos im Schaden ausgewirkt haben. "
     "[betr2]Ein Auto, das rückwärts ausparkt, ist ohne Zweifel in Betrieb. [rg]Drittens: Das Auto von Heidrun ist beschädigt, "
     "eine Sache. [kaus]Viertens: Die Beschädigung beruht auf diesem Betrieb, "
     "die haftungsbegründende Kausalität liegt vor.", P),
    ("[p72]Ausgeschlossen ist die Haftung nach Absatz zwei nur, wenn der Unfall durch höhere Gewalt verursacht wird. "
     "[hg]Ein Rempler beim Ausparken ist das nicht. [p7erg]Volkmar haftet also als Halter, ganz ohne Verschulden.", PS),
    # --- E § 18 Abs. 1 --------------------------------------------------------------------------------------------------------
    ("[p18]Volkmar saß aber auch selbst am Steuer. [p18a]Nach Paragraf achtzehn Absatz eins haftet in den Fällen des "
     "Paragrafen sieben auch der Fahrer. [p18b]Satz zwei: Die Ersatzpflicht ist ausgeschlossen, wenn der Schaden nicht durch "
     "ein Verschulden des Führers verursacht ist. [verm]Man spricht von vermutetem Verschulden: Der Fahrer muss beweisen, "
     "dass ihn kein Verschulden trifft. Die Abgrenzung zum Anscheinsbeweis zeigt das Video dazu. "
     "[p18c]Ob Volkmar das kann, klärt der Parkplatz.", PS),
    # --- F § 17 ----------------------------------------------------------------------------------------------------------------
    ("[p17]Jetzt der Kern: Zwei Autos haben den Schaden verursacht. [p17a]Nach Paragraf siebzehn Absatz eins hängt die "
     "Ersatzpflicht im Verhältnis der Halter zueinander von den Umständen ab, vor allem davon, wer den Schaden vorwiegend "
     "verursacht hat. [p17b]Absatz zwei gilt, wenn einer der Halter selbst den Schaden hat, wie Heidrun.", P),
    ("[sockel]Den Sockel bildet die Betriebsgefahr: Jedes Auto bringt sie mit, auch ohne jeden Fehler. "
     "[versch]Dazu kommt das Verschulden der Beteiligten, [bew]aber nur, was unstreitig oder bewiesen ist. "
     "[p173]Ganz frei wird nach Absatz drei nur, für wen der Unfall ein unabwendbares Ereignis war: Er muss sich wie ein "
     "Idealfahrer verhalten haben. [p254]Ein Mitverschulden des Verletzten rechnet Paragraf neun über Paragraf "
     "zweihundertvierundfünfzig BGB an; unter Haltern gilt derselbe Maßstab in Paragraf siebzehn.", PS),
    # --- G Parkplatz ---------------------------------------------------------------------------------------------------------
    ("[park]Was gilt auf dem Parkplatz? [stvo]Die Straßenverkehrsordnung gilt auch auf einem öffentlich zugänglichen "
     "Parkplatz. [rvl]Aber die Fahrgassen haben meist keinen eindeutigen Straßencharakter. Dann gilt rechts vor links nicht, "
     "auch nicht mittelbar. [p12]Es bleibt Paragraf eins Absatz zwei: Jeder muss sich so verhalten, dass kein anderer "
     "geschädigt wird. [anh]Wer rückwärts fährt, muss sein Auto notfalls sofort anhalten können.", P),
    ("[ansch]Und der Beweis? [ans1]Steht fest, dass der Rückwärtsfahrende im Moment der Kollision noch rollte, spricht "
     "der erste Anschein dafür, dass er seine Sorgfaltspflicht verletzt hat. [ans2]Stand er dagegen schon, oder lässt sich "
     "das nicht ausschließen, spricht gegen ihn kein Anschein. [ans3]So der Bundesgerichtshof zweitausendfünfzehn "
     "und zweitausendsechzehn. [ans4]Seine Betriebsgefahr zählt aber trotzdem.", PS),
    # --- H Lösung ------------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Heidrun und Volkmar. [l1]Beide rollten noch, also spricht der Anschein gegen beide. [l2]Volkmar kann "
     "sich deshalb nach Paragraf achtzehn nicht entlasten, und unabwendbar war der Unfall für keinen. [l3]In der Abwägung "
     "stehen sich gleiche Betriebsgefahren und gleich schwere Verstöße gegenüber. [l4]Hier ist eine Teilung je zur Hälfte "
     "angemessen: [l5]Volkmar und sein Versicherer zahlen Heidrun achthundert Euro. [l6]Hätte Volkmar schon gestanden, "
     "spräche gegen ihn kein Anschein. Dann trüge Heidrun den größeren Teil; seine Betriebsgefahr "
     "zählte aber mit.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Reihenfolge ein. [tp1]Paragraf sieben gegen den Halter, [tp2]Paragraf achtzehn gegen "
     "den Fahrer, [tp3]dann die Verteilung nach Paragraf siebzehn. [tp4]Und vergiss den Versicherer nicht: Nach Paragraf "
     "hundertfünfzehn Versicherungsvertragsgesetz kann der Geschädigte seinen Anspruch auch gegen den Versicherer geltend "
     "machen. [tp5]Daneben kommt Paragraf achthundertdreiundzwanzig BGB in Betracht, siehe das Video zum "
     "Deliktsrecht.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins: Paragraf sieben Absatz eins. [s1a]Halter, Betrieb eines Kraftfahrzeugs, "
     "Rechtsgutverletzung und Kausalität, [s1b]kein Ausschluss durch höhere Gewalt. [s2]Römisch zwei: Paragraf achtzehn, "
     "der Fahrer haftet, wenn er sich nicht entlastet. [s3]Römisch drei: Paragraf siebzehn, die Abwägung der "
     "Verursachungsbeiträge, [s3a]Betriebsgefahr und bewiesenes Verschulden, [s3b]frei nur bei einem unabwendbaren Ereignis. "
     "[s4]Römisch vier: der Direktanspruch gegen den Versicherer.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Halter haftet für die Betriebsgefahr seines Autos, auch ohne Verschulden. [m2]Verursachen zwei "
     "Autos den Schaden, entscheidet die Abwägung, wer welchen Anteil trägt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
