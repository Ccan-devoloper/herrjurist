"""Folge 202 · Tippgemeinschaft ohne Tippschein: Gefälligkeitsverhältnis und Haftung (Mo · Der Fall · BGB AT, Klassiker-Fall).
Leitentscheidung: BGH, Urt. v. 16.5.1974 – II ZR 12/73, NJW 1974, 1705 (Lottospielgemeinschaft). Volltext nur in nicht
amtlicher Wiedergabe gelesen (juramagazin.de), Az./Datum/Fundstelle über dejure.org bestätigt; keine Randnummern (1974),
Fundstelle mit Seite. Inhalt: § 762 nicht anwendbar (Nebengeschäft, staatlich genehmigt, § 763); Rechtsbeziehungen der
Spielgemeinschaft (Gewinnverteilung, Einsätze) anerkannt, GbR ausdrücklich offengelassen; Ausfüllen und Einreichen:
in der Regel keine rechtsgeschäftliche Verpflichtung (Leitsatz), Interessenabwägung nach Treu und Glauben (Fehler leicht,
Schaden selten, aber existenzvernichtend; Spielgewinn kein normaler Gewinn; Gedanke des gemeinsamen Spiels; anders bei
Entgelt/geschäftlichen Zwecken; sonst besondere Vereinbarung). Kriterien des Rechtsbindungswillens heute: BGH III ZR 346/14
Rn. 8. Delikt: III ZR 211/17 Rn. 19 (Vermögen als solches nicht geschützt). Haftungsmaßstab bei Gefälligkeit (Abgrenzung):
VI ZR 467/15 Rn. 8, 10. § 705 vom BGH nicht tragend → keine Wortlautkarte, nur „offengelassen“.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des Auftrags, Volltextsuche 06.10.2026):
Hilmar (vergisst den Schein, Stimme william), Erna (Kollegin, sabrina), Ulf (Kollege, marc) – nie im Genitiv. Lexi = Carla.
Revision v1.1 (06.10.2026): Segment 16 umgestellt („Also gehen Erna und Ulf leer aus.“), weil small und medium „Erna“ am
Segmentanfang als „Gerner“ hörten; einmal nachvertont.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Hilmar": "william", "Erna": "sabrina", "Ulf": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Tipprunde im Büro ------------------------------------------------------------------------------------
    ("[fall]Deine Tipprunde hätte gewonnen – aber der Kollege hat vergessen, den Schein abzugeben. [runde]So geht es Erna "
     "und Ulf. [hilmar]Seit Jahren spielen sie mit ihrem Kollegen Hilmar Lotto. [geld]Jede Woche zahlt jeder fünf Euro an "
     "Hilmar. [schein]Hilmar füllt den Lottoschein mit ihren festen Zahlen aus und gibt ihn in der Annahmestelle ab. "
     "[gratis]Dafür bekommt er nichts.", P),
    # --- A2 Fall: der vergessene Samstag -----------------------------------------------------------------------------------
    ("[samstag]An einem Samstag muss Hilmar lange arbeiten [vergisst]und vergisst den Schein. [ziehung]Am Abend wird gezogen: "
     "Mit ihren Zahlen hätte die Runde zwölftausend Euro gewonnen.", P),
    # --- A3 Fall: Montag in der Teeküche -----------------------------------------------------------------------------------
    ("[montag]Am Montag in der Teeküche.", P),
    ("[e1]Hilmar, mit unseren Zahlen hätten wir zwölftausend Euro gewonnen!", P, "Erna"),
    ("[h1]Ich weiß. Ich habe den Schein diesmal nicht abgegeben. Es tut mir leid.", P, "Hilmar"),
    ("[u1]Dann schuldest du Erna und mir je viertausend Euro.", P, "Ulf"),
    ("[frage]Muss Hilmar den entgangenen Gewinn ersetzen? [frage2]Oder war das Einreichen nur eine Gefälligkeit? "
     "[bgh]Diesen Fall hat der Bundesgerichtshof schon neunzehnhundertvierundsiebzig entschieden.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch: Schuldverhältnis? -------------------------------------------------------------------------------------
    ("[ansp]Erna und Ulf könnten Schadensersatz aus Paragraf zweihundertachtzig Absatz eins BGB verlangen. [pfl]Dafür muss "
     "Hilmar eine Pflicht aus einem Schuldverhältnis verletzt haben. [p241]Paragraf zweihunderteinundvierzig Absatz eins: "
     "Kraft des Schuldverhältnisses ist der Gläubiger berechtigt, von dem Schuldner eine Leistung zu fordern. "
     "[frage3]Schuldete Hilmar also das Einreichen des Scheins?", PS),
    # --- D Rechtsbindungswille oder Gefälligkeit ---------------------------------------------------------------------------
    ("[rbw]Das hängt vom Rechtsbindungswillen ab, den du schon vom Angebot nach Paragraf hundertfünfundvierzig kennst. [gef]Wer einem anderen nur einen Gefallen tut, geht keine Rechtspflicht "
     "ein. [obj]Maßgeblich ist, wie ein objektiver Beobachter das Verhalten nach Treu und Glauben und der Verkehrssitte "
     "versteht. [wirt]Für eine Bindung spricht, wenn für den anderen erkennbar wesentliche wirtschaftliche Interessen auf "
     "dem Spiel stehen und er sich auf die Zusage verlässt, [eigen]oder wenn der Helfer selbst ein rechtliches oder "
     "wirtschaftliches Interesse hat. [alltag]Bei Gefälligkeiten des täglichen Lebens fehlt der Bindungswille dagegen in "
     "der Regel.", PS),
    # --- E Der Fall des BGH ------------------------------------------------------------------------------------------------
    ("[urteil]Im Fall des BGH hatte ein Mitspieler die Scheine vor einer Ziehung nicht wie verabredet ausgefüllt. [dm]Der "
     "Runde entgingen zehntausendfünfhundertfünfzig Mark. [olg]Das Oberlandesgericht hatte noch auf Paragraf "
     "siebenhundertzweiundsechzig abgestellt: Durch Spiel wird keine Verbindlichkeit begründet. [neben]Der BGH widersprach: "
     "Das Einreichen ist selbst kein Spiel, sondern ein Nebengeschäft, [p763]und eine staatlich genehmigte Lotterie ist "
     "verbindlich, Paragraf siebenhundertdreiundsechzig.", PS),
    ("[bind]Rechtlich gebunden sind die Mitspieler durchaus: [verteil]Ein Gewinn muss wie verabredet verteilt werden, "
     "[einsatz]und auch die versprochenen Einsätze können geschuldet sein. [gbr]Ob die Runde eine Gesellschaft bürgerlichen Rechts ist, "
     "ließ der BGH offen. [kern]Entscheidend war etwas anderes: [lsatz]Wer die Scheine ausfüllt und einreicht, übernimmt "
     "insoweit in der Regel keine rechtsgeschäftliche Verpflichtung.", PS),
    # --- F Die Gründe ------------------------------------------------------------------------------------------------------
    ("[warum]Warum? Der BGH wägt die Interessen beider Seiten ab. [fehler]Ein Fehler passiert leicht: Der Mitspieler "
     "vergisst den Schein, hat anderes zu tun oder kreuzt falsche Zahlen an. [hoch]Ein Schaden ist zwar selten, kann aber "
     "außergewöhnlich hoch sein, [exist]bis zur Vernichtung der wirtschaftlichen Existenz des Helfers. [unentg]Und das für "
     "eine Aufgabe, die er ohne Entgelt übernommen hat. [glueck]Ein Lottogewinn ist auch kein normaler Gewinn wie ein "
     "Arbeitslohn, sondern ein Glücksfall, mit dem niemand ernsthaft rechnen kann. [gemein]Wer gemeinsam spielt, will "
     "Spannung und Chance teilen, nicht ein Haftungsrisiko. [niemand]Niemand würde ein solches Risiko übernehmen oder einem "
     "Mitspieler zumuten.", PS),
    ("[anders]Anders kann es liegen, wenn der Beauftragte ein Entgelt bekommt, wie eine Annahmestelle, oder wenn "
     "geschäftliche Zwecke im Vordergrund stehen. [verein]Sonst braucht es für eine Pflicht eine besondere Vereinbarung. "
     "[erg]Für Hilmar heißt das: Eine Pflicht zum Einreichen gab es nicht, also auch keine Pflichtverletzung.", PS),
    # --- G Delikt und Haftungsmaßstab --------------------------------------------------------------------------------------
    ("[delikt]Bleibt das Deliktsrecht. [w823]Paragraf achthundertdreiundzwanzig Absatz eins schützt Leben, Körper, "
     "Gesundheit, Freiheit, Eigentum und sonstige Rechte. [verm]Eine entgangene Gewinnchance gehört nicht dazu, denn das "
     "Vermögen als solches ist dort nicht geschützt. [garten]Anders, wenn bei einer Gefälligkeit ein Rechtsgut verletzt "
     "wird, etwa beim Gießen des Nachbargartens ein Wasserschaden entsteht. [fahrl]Dann haftet der Helfer aus Delikt schon "
     "für einfache Fahrlässigkeit, Paragraf zweihundertsechsundsiebzig Absatz zwei. [still]Eine stillschweigende "
     "Haftungsbeschränkung nimmt der BGH nur ausnahmsweise an.", PS),
    # --- H Fall: zurück in der Teeküche ------------------------------------------------------------------------------------
    ("[leer]Also gehen Erna und Ulf leer aus.", P),  # v1.1: „Erna“ am Segmentanfang hörten small und medium als „Gerner“
    ("[e2]Dann spielen wir eben weiter. Aber den Schein gebe ab jetzt ich ab.", P, "Erna"),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Rechtsbindungswillen nicht pauschal für die ganze Tipprunde, [tp1]sondern für die "
     "einzelne Pflicht. [tp2]Den Gewinn verteilen: rechtlich bindend. [tp3]Schein ausfüllen und einreichen: "
     "in der Regel nur Gefälligkeit. [tp4]Und begründe das mit den Kriterien: wirtschaftliche Bedeutung, Interessenlage "
     "und Haftungsrisiko des Helfers.", PS),
    # --- J Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [c1]Römisch eins: Anspruch aus Paragraf zweihundertachtzig Absatz eins. [c2]Erstens: "
     "Schuldverhältnis mit einer Pflicht zum Einreichen? [c3]Rechtsbindungswille aus Sicht eines objektiven Beobachters: "
     "wirtschaftliche Bedeutung, Interessenlage, Haftungsrisiko. [c4]Hier verneint: bloße Gefälligkeit. [c5]Zweitens: "
     "kein Anspruch. [c6]Römisch zwei: Paragraf achthundertdreiundzwanzig Absatz eins. [c7]Kein geschütztes Rechtsgut, "
     "das Vermögen als solches fehlt.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer für die Tipprunde ohne Entgelt den Schein abgibt, tut in der Regel nur einen Gefallen. [mk2]Für den "
     "entgangenen Gewinn haftet er deshalb grundsätzlich nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
