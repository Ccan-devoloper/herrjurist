"""Folge 218 · Nichtanzeige geplanter Straftaten § 138: Freund verraten? (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Mann liest in einem privaten Chat, dass sein Freund am Wochenende einen Überfall auf
einen Juwelier plant“), vollständig fiktiv: kein Ort, keine echten Personen, kein echter Messenger, keine Logos.
Donnerstagabend liest Sören im privaten Chat, dass sein Freund Mirko am Samstag den Juwelier am Markt überfallen will
(„Ich bedrohe die Verkäuferin, dann gibt sie mir den Schmuck.“). Auf Nachfrage bestätigt Mirko: kein Witz, Samstag 18 Uhr.
Sören schweigt („Mirko ist mein Freund. Den verrate ich nicht.“). Am Samstag versucht Mirko den Überfall, die Verkäuferin
löst den Alarm aus, niemand wird verletzt, die Polizei fasst Mirko noch am Abend.
DARSTELLUNG: keine Waffen, kein Überfall im Bild (nur Chat-Blasen und Juweliersymbol), Mirko ohne Gangster-Klischee.
Aufbau: Fall → Frage → Sachverhalt → Wortlautkarte § 138 Abs. 1 (Nr. 7, aktuelle Fassung) → echtes Unterlassungsdelikt →
1. Katalogtat geplant (Vorhaben) → 2. glaubhafte Kenntnis → 3. rechtzeitig → 4. Unterlassen der Anzeige (Behörde oder
Bedrohter) → 5. Vorsatz, Abs. 3 Leichtfertigkeit (ein Satz) → § 139 (Wortlautkarten Abs. 3 und 4; § 11 Abs. 1 Nr. 1 kurz;
Gegenfall Bruder; Gegenfall Ausreden; Abs. 2 ein Satz; Abs. 1) → Abgrenzung Beteiligung (BGH), § 323c (ein Satz, Verweis
185) → Lösung → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi).
Belege (BGH 5 StR 464/09 Rn. 7, 13 f., 15, 17; 2 StR 493/15 Rn. 42; StB 33/16 Rn. 22; AK 33/17 Rn. 28; 1 StR 497/95
(BGHSt 42, 86) Rn. 6 f.): ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Sören, Mirko (nie im Genitiv).
Stimmen (nur aus dem Pool): Sören niklas (Mann, jung). Mirko spricht nicht (nur Chat-Text, von der Erzählerin gelesen).
Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter.
Nachvertonung v2 (nur Segment 18): „Hätte Sören Mirko seine Hilfe zugesagt“ hörten whisper small und medium als
„Nirkow“ (Satz und isoliert); umformuliert zu „Hätte Sören zugesagt, Mirko zu helfen, …“."""

P, PS = 0.3, 0.5

STIMMEN = {"Soeren": "niklas"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: der Chat am Donnerstagabend -------------------------------------------------------------------------------
    ("[fall]Donnerstagabend. [chat]Sören liest auf seinem Handy einen privaten Chat mit seinem Freund Mirko. "
     "[m1]Mirko schreibt: Am Samstag überfalle ich den Juwelier am Markt. [m2]Ich bedrohe die Verkäuferin, dann gibt sie "
     "mir den Schmuck.", P),
    ("[witz]Sören fragt zurück, ob das ein Witz ist. [m3]Die Antwort: Nein. Ich brauche das Geld. [m4]Samstag, achtzehn "
     "Uhr, kurz vor Ladenschluss.", P),
    ("[so1]Mirko ist mein Freund. Den verrate ich nicht.", P, "Soeren"),
    # --- A2 Fall: Samstag ---------------------------------------------------------------------------------------------------
    ("[schweigt]Sören sagt niemandem etwas, weder der Polizei noch dem Juwelier. [samstag]Am Samstag um achtzehn Uhr "
     "versucht Mirko den Überfall. [alarm]Die Verkäuferin löst den Alarm aus, niemand wird verletzt. [polizei]Die Polizei "
     "fasst Mirko noch am selben Abend.", 0.4),
    ("[frage]Hat sich Sören strafbar gemacht, nur weil er geschwiegen hat? [frage2]Muss man seinen Freund verraten?", PS),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 138 Abs. 1 --------------------------------------------------------------------------------------------
    ("[p138]Die Norm ist Paragraf hundertachtunddreißig Absatz eins: Wer von dem Vorhaben oder der Ausführung, [nr7]in "
     "Nummer sieben eines Raubes oder einer räuberischen Erpressung, [zeitw]zu einer Zeit, zu der die Ausführung oder der "
     "Erfolg noch abgewendet werden kann, glaubhaft erfährt und es unterlässt, der Behörde oder dem Bedrohten rechtzeitig "
     "Anzeige zu machen, [strafe]wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.", PS),
    ("[echt]Das ist ein echtes Unterlassungsdelikt: Bestraft wird das Schweigen selbst. [garant]Eine Garantenstellung "
     "braucht Sören dafür nicht. [jeder]Anzeigen muss grundsätzlich jeder, der von der Tat erfährt.", PS),
    # --- D 1. Katalogtat geplant --------------------------------------------------------------------------------------------
    ("[kat]Erstens: eine geplante Katalogtat. [abschl]Paragraf hundertachtunddreißig zählt die Taten abschließend auf. "
     "[raub]Raub und räuberische Erpressung stehen in Nummer sieben. [einbr]Ein geplanter Einbruch ohne Gewalt oder Drohung "
     "stünde dagegen nicht im Katalog. [vorh]Vorhaben heißt: Es gibt einen ernsthaften Tatplan, Ziel und Vorgehen stehen "
     "wenigstens in Grundzügen fest. [vorh2]Mirko nennt den Laden, den Tag, die Uhrzeit und die Drohung. Das ist ein "
     "Vorhaben.", PS),
    # --- E 2. glaubhafte Kenntnis -------------------------------------------------------------------------------------------
    ("[glaub]Zweitens: Sören muss glaubhaft davon erfahren. [ernst]Das heißt: so, dass er ernsthaft mit der Tat rechnet. "
     "[scherz]Ein erkennbarer Scherz genügt nicht. [glaub2]Hier fragt Sören nach, und Mirko bestätigt den Plan. Sören "
     "erfährt also glaubhaft davon.", PS),
    # --- F 3. rechtzeitig ---------------------------------------------------------------------------------------------------
    ("[rz]Drittens: rechtzeitig. [rz1]Sören erfährt am Donnerstag davon, der Überfall soll erst am Samstag stattfinden. "
     "Er kann also noch abgewendet werden. [unv]Sofort muss die Anzeige nicht kommen, aber so früh, dass sie die Tat noch "
     "verhindern kann. [risiko]Wer abwartet, trägt das Risiko, zu spät zu sein.", PS),
    # --- G 4. Unterlassen der Anzeige ---------------------------------------------------------------------------------------
    ("[anz]Viertens: Er unterlässt die Anzeige. [wem]Anzeigen kann er bei der Behörde, etwa der Polizei, [bedr]oder beim "
     "Bedrohten, hier beim Juwelier. [anz2]Sören sagt keinem von beiden etwas.", PS),
    # --- H 5. Vorsatz, Abs. 3 -----------------------------------------------------------------------------------------------
    ("[vors]Fünftens: Vorsatz. [vors1]Sören weiß, dass Mirko es ernst meint, und schweigt bewusst. [abs3]Nach Absatz drei "
     "ist sogar die leichtfertige Nichtanzeige strafbar, mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe.", PS),
    # --- I § 139 Abs. 3: Angehörige -----------------------------------------------------------------------------------------
    ("[p139]Jetzt kommt Paragraf hundertneununddreißig mit seinen Ausnahmen. [ang]Nach Absatz drei ist straffrei, wer eine "
     "Anzeige gegen einen Angehörigen unterlässt, wenn er sich ernsthaft bemüht hat, ihn von der Tat abzuhalten oder den "
     "Erfolg abzuwenden. [mord]Bei Mord und Totschlag gilt das nicht, beim Raub schon. [p11]Angehörige sind nach Paragraf "
     "elf zum Beispiel Eltern und Kinder, Ehegatten, Verlobte und Geschwister. [freund]Ein Freund gehört nicht dazu, auch "
     "nicht der beste. [bruder]Wäre Mirko sein Bruder, bliebe Sören nur straffrei, wenn er sich ernsthaft bemüht hätte, "
     "ihn abzuhalten.", PS),
    # --- J § 139 Abs. 4, Abs. 2, Abs. 1 -------------------------------------------------------------------------------------
    ("[abs4]Nach Absatz vier ist straffrei, wer die Ausführung oder den Erfolg der Tat anders als durch Anzeige abwendet. "
     "[ausr]Hätte Sören zu Mirko gesagt:", P),
    ("[so2]Lass das, Mirko. Das ist es nicht wert.", P, "Soeren"),
    ("[ausr2]und hätte Mirko den Plan deshalb aufgegeben, wäre Sören straffrei. [ausr3]Hier hat er aber nichts "
     "unternommen. [abs2]Übrigens muss ein Geistlicher nicht anzeigen, was ihm als Seelsorger anvertraut wurde. [abs1]Und "
     "wird die Tat nicht einmal versucht, kann das Gericht nach Absatz eins von Strafe absehen.", PS),
    # --- K Abgrenzung: Beteiligung, § 323c ----------------------------------------------------------------------------------
    ("[bet]Wichtig ist die Abgrenzung zur Beteiligung. Wer selbst an der Tat beteiligt ist, als Täter, Anstifter oder "
     "Gehilfe, ist nicht nach Paragraf hundertachtunddreißig strafbar. Für ihn ist die Tat keine fremde. [zusage]Hätte Sören "
     "zugesagt, Mirko zu helfen, prüfst du deshalb seine Beteiligung. [verd]Bleibt am Ende nur der Verdacht, er habe "
     "mitgemacht, kann er nach dem Bundesgerichtshof trotzdem wegen Nichtanzeige bestraft werden. [p323]Und die "
     "unterlassene Hilfeleistung verlangt einen Unglücksfall. Paragraf hundertachtunddreißig greift schon beim Vorhaben, "
     "mehr dazu im Video zur unterlassenen Hilfeleistung.", PS),
    # --- L Lösung -----------------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [l1]Mirko plant einen Raub, also eine Katalogtat. [l2]Sören erfährt glaubhaft und rechtzeitig "
     "davon und zeigt die Tat bewusst nicht an. [l3]Mirko ist kein Angehöriger, und Sören hat die Tat nicht abgewendet. "
     "[l4]Weil Mirko den Überfall versucht hat, scheidet auch ein Absehen von Strafe aus. [l5]Sören ist strafbar nach "
     "Paragraf hundertachtunddreißig Absatz eins Nummer sieben.", PS),
    # --- M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst, ob der Schweigende an der Tat selbst beteiligt ist. Erst wenn das ausscheidet, "
     "kommt Paragraf hundertachtunddreißig. [tipp2]Und bei Angehörigen reicht das Verwandtschaftsverhältnis allein nicht: "
     "Straffrei ist nur, wer sich ernsthaft bemüht hat.", PS),
    # --- N Prüfschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins, Tatbestand: [s1a]geplante Katalogtat, [s1b]glaubhafte Kenntnis, "
     "[s1c]rechtzeitig, [s1d]Unterlassen der Anzeige, [s1e]Vorsatz. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, "
     "Schuld. [s4]Römisch vier, Straflosigkeit nach Paragraf hundertneununddreißig.", PS),
    # --- O Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei einer geplanten Katalogtat schützt Freundschaft nicht. [mk2]Wer glaubhaft davon erfährt, muss "
     "rechtzeitig die Polizei oder den Bedrohten warnen oder die Tat anders abwenden.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
