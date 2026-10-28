"""Folge 164 · Richtlinie unmittelbare Wirkung: Nicht umgesetzt – und jetzt? (Mi · Examenswissen · Öffentliches Recht/
Europarecht, Format Schema). Fall nach dem Plan-Hook, deutlich als Annahme gekennzeichnet (Deutschland hat die
Arbeitszeitrichtlinie in Wirklichkeit umgesetzt): Herr Ruppert, Feuerwehrmann der Berufsfeuerwehr einer Stadt; eine
Landesverordnung erlaubt für die Feuerwehr im Schnitt 54 Wochenstunden; er verlangt die 48 Stunden aus Art. 6 Buchst. b
RL 2003/88/EG. Herr Goldbach (Personalamt der Stadt) hält dagegen.
Aufbau: Fall → Sachverhalt → Normen (Art. 288 Abs. 3 AEUV als Wortlautkarte, Merkmale gesprochen; Art. 4 Abs. 3 UAbs. 2
EUV als Wortlautkarte, vorgelesen; Verweis Folge 138 in einem Satz) → Prüfschema vertikale unmittelbare Wirkung:
1. Umsetzungsfrist abgelaufen (Ratti Rn. 2, 3, 7, 22–24, 41–43, Tenor 1 und 5; Fuß I Rn. 3),
2. nicht oder nicht ordnungsgemäß umgesetzt (Fuß I Rn. 56; Marshall Rn. 46),
3. inhaltlich unbedingt und hinreichend genau (Ratti Rn. 23; Art. 6 Buchst. b als Wortlautkarte, vorgelesen; Fuß I Rn. 57–59),
4. gegenüber dem Staat, auch als Arbeitgeber (Marshall Rn. 49; Foster Rn. 17; Fuß I Rn. 56)
→ funktionaler Staatsbegriff (Foster Rn. 3, 8, 20; Farrell Rn. 26, 29; Gebietskörperschaften: Foster Rn. 19, Farrell Rn. 33,
Fuß I Rn. 61) → keine Wirkung zwischen Privaten, richtlinienkonforme Auslegung (je ein Satz, Verweis 138) → Lösung und
Rechtsfolge (Fuß I Rn. 60, 61, 63; Fuß II Rn. 38–40; Anwendungsvorrang, Verweis 127) → Klausurtipp (Lexi) → Klausurschema
→ Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Ruppert, Goldbach
(nie im Genitiv). Stimmen: Herr Ruppert niklas (Mann, jung), Herr Goldbach helmut (Mann, älter). Lexi = Erzählerin Carla.
Reale Personen (Ratti, Foster, Farrell, Fuß, Faccini Dori) nur als Fallnamen, keine Figuren.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Normen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ruppert": "niklas", "Goldbach": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Feuerwache ------------------------------------------------------------------------------------------
    ("[fall]Herr Ruppert ist Feuerwehrmann bei der Berufsfeuerwehr seiner Stadt. [plan]Eine Landesverordnung erlaubt für "
     "die Feuerwehr im Schnitt vierundfünfzig Wochenstunden, [plan2]und so plant ihn die Stadt ein. "
     "[rl]Herr Ruppert kennt aber die EU-Arbeitszeitrichtlinie.", P),
    ("[r1]Im Schnitt achtundvierzig Stunden, mehr erlaubt die Richtlinie nicht. Daran muss sich die Stadt halten.", P, "Ruppert"),
    ("[gold]Herr Goldbach leitet das Personalamt der Stadt.", P),
    ("[g1]Die Richtlinie richtet sich an Deutschland, nicht an uns. Bei uns gilt die Verordnung.", P, "Goldbach"),
    ("[ann]Nehmen wir für diesen Fall an: Deutschland hätte die Richtlinie nicht rechtzeitig umgesetzt. "
     "[echt]In Wirklichkeit ist sie umgesetzt, etwa im Arbeitszeitgesetz. [frage]Kann sich Herr Ruppert trotzdem direkt auf die Richtlinie berufen?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Normen ------------------------------------------------------------------------------------------------------
    ("[norm]Zuerst die Normen. [a288]Nach Artikel zweihundertachtundachtzig Absatz drei des Vertrags über die Arbeitsweise "
     "der Union ist die Richtlinie nur hinsichtlich des Ziels verbindlich; [form]die Wahl der Form und der Mittel bleibt den "
     "innerstaatlichen Stellen. [gold2]Insoweit hat Herr Goldbach recht: Adressat ist der Mitgliedstaat. "
     "[a4]Und Artikel vier Absatz drei des EU-Vertrags sagt: Die Mitgliedstaaten ergreifen alle geeigneten Maßnahmen "
     "allgemeiner oder besonderer Art zur Erfüllung der Verpflichtungen, die sich aus den Verträgen oder den Handlungen der "
     "Organe der Union ergeben. [pfl]Eine Richtlinie umzusetzen ist also Pflicht. [v138]Den Überblick gibt das Video zu den "
     "EU-Rechtsakten. [vert]Verletzt der Staat diese Pflicht, prüfst du die vertikale unmittelbare Wirkung in vier "
     "Schritten.", PS),
    # --- D 1. Umsetzungsfrist abgelaufen (Ratti) ------------------------------------------------------------------------
    ("[s1]Erstens: Die Umsetzungsfrist ist abgelaufen. [ratti]Das zeigt der Fall Ratti. Herr Ratti leitete in Italien ein "
     "Unternehmen für Lösemittel und Lacke. [kennz]Er kennzeichnete seine Produkte nach zwei europäischen Richtlinien, nicht nach dem "
     "italienischen Gesetz, das mehr Angaben verlangte. [loes]Für die Lösemittel war die Frist abgelaufen: Italien durfte sein "
     "altes Recht nicht gegen ihn anwenden, auch nicht als Strafrecht. [lack]Für die Lacke lief die Frist noch. [ende]Der "
     "Gerichtshof: Die unmittelbare Wirkung entsteht erst am Ende des festgesetzten Zeitraums. [frist]Im Fall ist die Frist längst "
     "abgelaufen: Schon die Vorgängerrichtlinie war bis November neunzehnhundertsechsundneunzig umzusetzen.", PS),
    # --- E 2. nicht oder nicht ordnungsgemäß umgesetzt ------------------------------------------------------------------
    ("[s2]Zweitens: Der Staat hat die Richtlinie nicht oder nicht ordnungsgemäß umgesetzt. [s2f]Im Fall fehlt die "
     "Umsetzung nach unserer Annahme ganz, und die Verordnung erlaubt mehr als achtundvierzig Stunden.", PS),
    # --- F 3. unbedingt und hinreichend genau ---------------------------------------------------------------------------
    ("[s3]Drittens: Die Bestimmung ist inhaltlich unbedingt und hinreichend genau. [a6]Artikel sechs Buchstabe b der "
     "Arbeitszeitrichtlinie verlangt Maßnahmen, damit die durchschnittliche Arbeitszeit pro Siebentageszeitraum "
     "achtundvierzig Stunden einschließlich der Überstunden nicht überschreitet. [klar]Das ist ein festes Ergebnis, an keine "
     "Bedingung geknüpft. [abw]Zwar erlaubt die Richtlinie Abweichungen, aber nur unter engen Voraussetzungen. [gen]Der "
     "Gerichtshof: Das nimmt der Regel nichts von ihrer Genauigkeit und Unbedingtheit.", PS),
    # --- G 4. gegenüber dem Staat ---------------------------------------------------------------------------------------
    ("[s4]Viertens: Der Einzelne beruft sich gegenüber dem Staat. Das ist die vertikale Richtung. [arb]Dabei ist egal, ob der "
     "Staat als Hoheitsträger handelt oder als Arbeitgeber. [nutz]Er soll aus seinem eigenen Versäumnis keinen Nutzen "
     "ziehen.", PS),
    # --- H Funktionaler Staatsbegriff (Foster, Farrell) -----------------------------------------------------------------
    ("[staat]Doch wer ist der Staat? Das Unionsrecht versteht ihn funktional. [foster]Im Fall Foster hatte die British Gas "
     "Corporation Frauen mit sechzig in den Ruhestand geschickt, Männer erst mit fünfundsechzig. [bgc]British Gas war "
     "durch Gesetz errichtet und betrieb als Monopol die Gasversorgung. [formel]Der Gerichtshof: Unabhängig von ihrer "
     "Rechtsform gehört jedenfalls eine Einrichtung dazu, die kraft staatlichen Rechtsakts unter staatlicher Aufsicht eine "
     "Dienstleistung im öffentlichen Interesse zu erbringen hat und hierzu mit besonderen Rechten ausgestattet ist, die "
     "über das hinausgehen, was für die Beziehungen zwischen Privatpersonen gilt. [farrell]Im Fall Farrell stellte er "
     "später klar: Eine Einrichtung muss nicht alle diese Merkmale erfüllen. [stadt]Für die Stadt braucht es die Formel "
     "nicht einmal: Gebietskörperschaften wie Städte und Gemeinden gehören selbst zum Staat.", PS),
    # --- I Keine horizontale Wirkung, richtlinienkonforme Auslegung -----------------------------------------------------
    ("[priv]Bei einem privaten Arbeitgeber käme Herr Ruppert so nicht weiter: Zwischen Privaten wirkt eine Richtlinie "
     "nicht unmittelbar, siehe Faccini Dori im Video zu den EU-Rechtsakten. [rka]Dann bliebe, das deutsche Recht "
     "richtlinienkonform auszulegen.", PS),
    # --- J Lösung und Rechtsfolge ---------------------------------------------------------------------------------------
    ("[loes1]Zurück zu Herrn Ruppert. [l1]Die Frist ist abgelaufen, [l2]die Richtlinie nach der Annahme nicht umgesetzt, "
     "[l3]Artikel sechs Buchstabe b ist unbedingt und hinreichend genau, [l4]und die Stadt gehört zum Staat, auch als "
     "Arbeitgeberin. [l5]Herr Ruppert kann sich ihr gegenüber unmittelbar auf die achtundvierzig Stunden berufen. [folge]Die "
     "feste Zahl der Verordnung lässt sich nicht richtlinienkonform auslegen. [unang]Also muss die Stadt sie insoweit "
     "unangewendet lassen, ebenso jedes Gericht. [vorr]Das ist der Anwendungsvorrang aus dem Video zu Costa gegen Enel. "
     "[fuss]So entschied der Gerichtshof zweitausendzehn im echten Fall Fuß: Ein Feuerwehrmann der Stadt Halle durfte sich "
     "gegenüber seiner Stadt unmittelbar auf die Regel berufen.", 0.3),
    ("[g2]Dann müssen wir den Dienstplan ändern.", PS, "Goldbach"),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die unmittelbare Wirkung dort, wo deutsches Recht dem Anspruch entgegensteht. [tf]Typischer "
     "Fehler: die Stadt als Arbeitgeberin wie einen Privaten behandeln. [tf2]Und vorher: Lässt sich das deutsche Recht "
     "richtlinienkonform auslegen, brauchst du die unmittelbare Wirkung nicht.", PS),
    # --- L Klausurschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema in vier Schritten. [z1]Römisch eins: Umsetzungsfrist abgelaufen. [z2]Römisch zwei: nicht oder nicht "
     "ordnungsgemäß umgesetzt. [z3]Römisch drei: inhaltlich unbedingt und hinreichend genau. [z4]Römisch vier: gegenüber dem "
     "Staat, [z4a]funktional verstanden, [z4b]auch als Arbeitgeber, [z4c]nicht gegenüber Privaten. [z5]Dann gilt die "
     "Bestimmung unmittelbar, und entgegenstehendes deutsches Recht bleibt unangewendet.", PS),
    # --- M Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Nach Fristablauf wirkt eine unbedingte und hinreichend genaue Richtlinie unmittelbar gegenüber dem "
     "Staat. [m2]Und Staat ist auch die Stadt als Arbeitgeberin.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
