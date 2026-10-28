"""Folge 152 · Kündigungsschutzgesetz: Wann gilt das KSchG – und die 3-Wochen-Frist (Mi · Examenswissen · Arbeitsrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Nach acht Jahren im Betrieb bekommst du ohne jede Begründung die
Kündigung“): Kornelia arbeitet seit acht Jahren als Gärtnerin in der Gärtnerei von Herrn Steinmetz (25 Beschäftigte, kein
Betriebsrat). Am Montag, 5.10.2026, übergibt er ihr persönlich eine eigenhändig unterschriebene, ordentliche und
fristgerechte Kündigung ohne Begründung (Schriftform und Zugang gewahrt, Verweis auf Folge 050). Kornelia will es sich
„erst mal in Ruhe überlegen“.
Prüfung: Aufbau → I. Anwendbarkeit: persönlich § 1 Abs. 1 KSchG (Wortlautkarte, vorgelesen; Wartezeit), betrieblich
§ 23 Abs. 1 S. 3 KSchG (Wortlautkarte mit Auslassung; „in der Regel“ nach BAG 2 AZR 140/12 Rn. 11; Teilzeit S. 4 in einem
Satz; §§ 4–7 auch im Kleinbetrieb) → II. Sozialwidrigkeit § 1 Abs. 2 S. 1 (Wortlautkarte; personen-, verhaltens-,
betriebsbedingt je ein Satz; Abmahnung nach BAG 2 AZR 541/09 Rn. 36 f.), keine Begründungspflicht im Schreiben, Beweislast
§ 1 Abs. 2 S. 4 (Wortlaut vorgelesen), Betriebsgröße AN (BAG 2 AZR 140/12 Rn. 27), Verweis Folge 141 → III. Klagefrist:
§ 4 S. 1 (Wortlautkarte), § 7 (Wortlautkarte), § 5 ein Satz, Fristberechnung §§ 187 Abs. 1, 188 Abs. 2 BGB
(Mo 5.10.2026 → Mo 26.10.2026) → Lösung → Klausurtipp (Reihenfolge, § 102 BetrVG) → Schema → Merksatz.
Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Kornelia, Steinmetz
(nie im Genitiv). Stimmen: Kornelia laura_ruhig, Herr Steinmetz william. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; KSchG und BetrVG ausgeschrieben (synth_el kennt die Abkürzungen nicht)."""

P, PS = 0.3, 0.5

STIMMEN = {"Kornelia": "laura_ruhig", "Steinmetz": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Gärtnerei ----------------------------------------------------------------------------------------------
    ("[fall]Eine Gärtnerei am Stadtrand mit fünfundzwanzig Beschäftigten. [korn]Kornelia arbeitet hier seit acht Jahren als "
     "Gärtnerin. [stein]An einem Montagmorgen kommt der Inhaber, Herr Steinmetz, ins Gewächshaus [brief]und übergibt ihr "
     "einen Brief. [kuend]Darin steht die ordentliche Kündigung, fristgerecht und eigenhändig unterschrieben. "
     "[grund]Ein Grund steht nicht darin.", P),
    ("[k1]Nach acht Jahren? Ohne jeden Grund?", P, "Kornelia"),
    ("[st1]Einen Grund muss ich Ihnen nicht nennen.", P, "Steinmetz"),
    ("[k2]Dann überlege ich mir erst mal in Ruhe, was ich mache.", P, "Kornelia"),
    ("[frage]Ist die Kündigung wirksam? [frage2]Und wie viel Zeit hat Kornelia, sich zu wehren?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau ------------------------------------------------------------------------------------------------------------
    ("[aufbau]Die Kündigung ist schriftlich erklärt und zugegangen. Worauf es dabei ankommt, zeigt das Video zur Kündigung "
     "per WhatsApp. [a1]Wir prüfen drei Schritte: [a2]Gilt das Kündigungsschutzgesetz? [a3]Ist die Kündigung sozial "
     "gerechtfertigt? [a4]Und die Falle: die Klagefrist.", PS),
    # --- D § 1 Abs. 1 KSchG: persönlicher Anwendungsbereich -----------------------------------------------------------------
    ("[p1]Zuerst der persönliche Anwendungsbereich. Paragraf eins Absatz eins: Die Kündigung des Arbeitsverhältnisses "
     "gegenüber einem Arbeitnehmer, dessen Arbeitsverhältnis in demselben Betrieb oder Unternehmen ohne Unterbrechung "
     "länger als sechs Monate bestanden hat, ist rechtsunwirksam, wenn sie sozial ungerechtfertigt ist. [warte]Man nennt "
     "das die Wartezeit. [p1fall]Kornelia ist Arbeitnehmerin und seit acht Jahren ohne Unterbrechung im Betrieb. "
     "Die Wartezeit ist erfüllt.", P),
    # --- E § 23 Abs. 1 KSchG: betrieblicher Anwendungsbereich ---------------------------------------------------------------
    ("[p23]Dann der betriebliche Anwendungsbereich, Paragraf dreiundzwanzig Absatz eins Satz drei. [p23a]Für "
     "Arbeitsverhältnisse, die nach zweitausenddrei begonnen haben, gilt der allgemeine Kündigungsschutz nicht in Betrieben, "
     "die in der Regel zehn oder weniger Arbeitnehmer beschäftigen; Auszubildende zählen nicht mit. [regel]In der Regel "
     "heißt: Maßgeblich ist die Beschäftigungslage, die den Betrieb im Allgemeinen kennzeichnet. [teil]Teilzeitkräfte zählen "
     "nach Satz vier anteilig, mit null Komma fünf oder null Komma fünfundsiebzig. [p23fall]Kornelia ist seit "
     "zweitausendachtzehn dabei, und mit fünfundzwanzig Beschäftigten liegt die Gärtnerei deutlich über der Grenze. "
     "[klein]Aber Achtung: Die Paragrafen vier bis sieben, also die Klagefrist, gelten auch im Kleinbetrieb.", PS),
    # --- F § 1 Abs. 2 S. 1 KSchG: Sozialwidrigkeit --------------------------------------------------------------------------
    ("[p12]Das Gesetz gilt also. Ist die Kündigung sozial gerechtfertigt? [p12a]Nach Paragraf eins Absatz zwei Satz eins ist "
     "sie sozial ungerechtfertigt, wenn sie nicht durch Gründe in der Person oder im Verhalten des Arbeitnehmers oder durch "
     "dringende betriebliche Erfordernisse bedingt ist. [pers]Personenbedingt heißt: Der Grund liegt in ihrer Person, etwa "
     "wenn sie die Arbeit auf Dauer nicht mehr leisten kann. [verh]Verhaltensbedingt heißt: Sie verletzt ihre Pflichten; "
     "dann ist nach dem Bundesarbeitsgericht in der Regel vorher eine Abmahnung nötig. [betr]Betriebsbedingt heißt: Ihr "
     "Arbeitsplatz fällt weg, etwa weil eine Abteilung schließt.", P),
    # --- G Begründung und Beweislast -----------------------------------------------------------------------------------------
    ("[begr]Und die fehlende Begründung? [begr2]Ins Kündigungsschreiben muss Herr Steinmetz grundsätzlich keinen Grund "
     "schreiben; Paragraf sechshundertdreiundzwanzig BGB verlangt nur die Schriftform. [obj]Entscheidend ist, dass ein "
     "solcher Grund tatsächlich vorliegt. [p124]Satz vier sagt: Der Arbeitgeber hat die Tatsachen zu beweisen, die die "
     "Kündigung bedingen. [bwl]Die Betriebsgröße dagegen muss grundsätzlich die Arbeitnehmerin beweisen. [v141]Wie das im "
     "Prozess wirkt, zeigt das Video zur Beweislast.", PS),
    # --- H Die Falle: §§ 4, 7, 5 KSchG ---------------------------------------------------------------------------------------
    ("[falle]Jetzt die Falle. [p4]Paragraf vier Satz eins: Will ein Arbeitnehmer geltend machen, dass eine Kündigung sozial "
     "ungerechtfertigt oder aus anderen Gründen rechtsunwirksam ist, so muss er innerhalb von drei Wochen nach Zugang der "
     "schriftlichen Kündigung Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis durch die "
     "Kündigung nicht aufgelöst ist. [p7]Und Paragraf sieben: Wird die Rechtsunwirksamkeit "
     "einer Kündigung nicht rechtzeitig geltend gemacht, so gilt die Kündigung als von Anfang an rechtswirksam. [p7b]Dann kommt es nicht "
     "mehr darauf an, ob es einen Grund gab. [p5]Wer trotz aller zumutbaren Sorgfalt verhindert war, kann nach "
     "Paragraf fünf die nachträgliche Zulassung der Klage beantragen.", P),
    # --- I Fristberechnung ---------------------------------------------------------------------------------------------------
    ("[frist]Wann endet die Frist? [zug]Kornelia hat den Brief am Montag, dem fünften Oktober zweitausendsechsundzwanzig, "
     "erhalten. [p187]Nach Paragraf hundertsiebenundachtzig Absatz eins BGB zählt dieser Tag nicht mit. [p188]Nach "
     "Paragraf hundertachtundachtzig Absatz zwei endet die Frist mit Ablauf des Tages, der durch seine Benennung dem "
     "Zugangstag entspricht: [ende]drei Wochen später, mit Ablauf des Montags, des sechsundzwanzigsten Oktober.", PS),
    # --- J Lösung ------------------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [l1]Das Kündigungsschutzgesetz ist anwendbar. [l2]Ob die Kündigung sozial gerechtfertigt ist, "
     "entscheidet das Arbeitsgericht; [l3]Herr Steinmetz muss dort einen Kündigungsgrund beweisen. [l4]Entscheidend ist "
     "aber: Kornelia muss bis zum sechsundzwanzigsten Oktober klagen. [l5]Überlegt sie zu lange, gilt die Kündigung als "
     "wirksam, auch ganz ohne Grund.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe in dieser Reihenfolge. [t1]Eine wirksame Kündigungserklärung, [t2]die Klagefrist, "
     "[t3]die Anwendbarkeit des Gesetzes, [t4]die Sozialwidrigkeit [t5]und sonstige Unwirksamkeitsgründe, etwa die fehlende "
     "Anhörung des Betriebsrats nach Paragraf hundertzwei Betriebsverfassungsgesetz. [t6]Die Frist gehört an den Anfang: Ist "
     "sie versäumt, gilt die Kündigung nach Paragraf sieben als wirksam, und auf die übrigen Gründe kommt es grundsätzlich "
     "nicht mehr an.", PS),
    # --- L Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins: wirksame Kündigungserklärung, schriftlich und zugegangen. [s2]Römisch zwei: "
     "Klagefrist, drei Wochen nach Zugang. [s3]Römisch drei: Anwendbarkeit, [s3a]persönlich nach Paragraf eins Absatz eins, "
     "[s3b]betrieblich nach Paragraf dreiundzwanzig. [s4]Römisch vier: soziale Rechtfertigung, [s4a]personen-, verhaltens- "
     "oder betriebsbedingt. [s5]Römisch fünf: sonstige Unwirksamkeitsgründe.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nach mehr als sechs Monaten schützt das Kündigungsschutzgesetz in Betrieben mit in der Regel mehr als zehn "
     "Arbeitnehmern. [m2]Doch nur wer innerhalb von drei Wochen klagt, kann sich darauf berufen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
