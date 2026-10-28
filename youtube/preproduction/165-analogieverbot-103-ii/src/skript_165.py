"""Folge 165 · Analogieverbot Strafrecht: Art. 103 II GG einfach erklärt (Fr · Methodik · Auslegung, Format Methodik).
Beispielfall nach dem Plan-Hook („Die Tat ist verwerflich, aber kein Paragraf passt genau – Pech für den Staat?“): Wieland
bindet am öffentlichen Steg das Tretboot von Hartwin los, fährt eine Stunde über den See und bringt es unbeschädigt zurück
(ruhige, gewaltfreie Darstellung). Diebstahl scheitert an der Zueignungsabsicht (bloße Gebrauchsanmaßung, BGH 3 StR 484/14
Rn. 6), § 248b StGB erfasst nur Kraftfahrzeuge und Fahrräder (Wortlautkarte).
Schwerpunkt (Auftrag): Bestimmtheitsgebot und die vier Gewährleistungen des Art. 103 Abs. 2 GG. Analogieverbot,
Wortlautgrenze und BVerfG 2 BvR 2273/06, 2 BvR 2500/09, 2 BvR 2628/10 sind in 148, 159 und 162 behandelt und werden hier
NICHT wiederholt (nur ein Verweissatz bei lex stricta).
Aufbau: Fall → Sachverhalt → § 242 / § 248b (Wortlautkarte) → Art. 103 Abs. 2 GG und § 1 StGB (Wortlautkarten), nullum
crimen, nulla poena sine lege, zwei Zwecke (BVerfGE 126, 170 Rn. 69 f.) → vier Gewährleistungen mit je eigener Farbe und
gleicher Tafelstruktur (lex scripta Blau, lex certa Gelb, lex stricta Lila, lex praevia Grün; § 2 Abs. 1 StGB Wortlaut) →
Schwerpunkt Bestimmtheit: Untreue-Beschluss BVerfGE 126, 170 (Rn. 73, 78, 80, 84, 152, 154, 158), Sitzblockaden-Beschluss
BVerfGE 92, 1 (S. 1, 14, 15, 17, 18; DFR) → nur zulasten: Analogie zugunsten erlaubt (BGH 1 StR 118/20 Rn. 9, 19–21,
§ 306e analog) → § 3 OWiG (Wortlautkarte) → Lösung am See (BVerfGE 126, 170 Rn. 77) → Klausurtipp (Lexi; Formulierung als
„üblich“ gekennzeichnet) → Prüfraster → Merksatz (Lexi).
Namen mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Textdatei unter youtube/:
Wieland, Hartwin (nie im Genitiv im Sprechtext).
Stimmen nur aus dem Pool: Wieland niklas (Mann, jung), Hartwin helmut (Mann, älter); ela_froh und julia nicht besetzt.
Lateinische Begriffe: Aussprachehilfen nur für die Vertonung in vertonen_165.py (synth_el.py bleibt unverändert).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Wieland": "niklas", "Hartwin": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Sommerabend am See, öffentlicher Steg ---------------------------------------------------------------------
    ("[fall]Ein Sommerabend am See. [boot]Am öffentlichen Steg liegt das Tretboot von Hartwin, nur mit einem Seil "
     "festgebunden. [nimmt]Wieland bindet es los und fährt eine Stunde über den See, ohne zu fragen. [zurueck]Danach "
     "bringt er es zurück und bindet es wieder fest. Kaputt ist nichts.", P),
    ("[ha1]Das ist doch Diebstahl! Dafür gehört er bestraft!", P, "Hartwin"),
    ("[wi1]Ich habe es doch zurückgebracht.", P, "Wieland"),
    ("[frage]Verwerflich ist das. Aber passt ein Paragraf genau? [frage2]Und wenn nicht: Pech für den Staat?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Welcher Paragraf? § 242, § 248b (Wortlautkarte) ---------------------------------------------------------------
    ("[dieb]Diebstahl verlangt die Absicht, sich die Sache zuzueignen. [rueck]Wer sie nur benutzen und zurückbringen will, "
     "maßt sich bloß den Gebrauch an. Das ist kein Diebstahl.", P),
    ("[p248]Für das bloße Benutzen gibt es Paragraf zweihundertachtundvierzig b: unbefugter Gebrauch eines Kraftfahrzeugs "
     "oder eines Fahrrads. [kein]Ein Tretboot hat keinen Motor. Und ein Fahrrad ist es nicht, auch wenn man tritt.", PS),
    # --- D Art. 103 Abs. 2 GG und § 1 StGB (Wortlautkarten) ----------------------------------------------------------------
    ("[a103]Warum hilft das Gericht nicht einfach nach? Artikel hundertdrei Absatz zwei Grundgesetz: Eine Tat kann nur "
     "bestraft werden, wenn die Strafbarkeit gesetzlich bestimmt war, bevor die Tat begangen wurde. [p1]Paragraf eins "
     "Strafgesetzbuch sagt wortgleich dasselbe. [latein]Kurz: nullum crimen, nulla poena sine lege. Kein Verbrechen, keine "
     "Strafe ohne Gesetz.", P),
    ("[zweck]Das Bundesverfassungsgericht nennt zwei Zwecke. [z1]Über Strafbarkeit entscheidet der Gesetzgeber selbst. "
     "[z2]Und jeder soll vorhersehen können, was verboten ist.", PS),
    # --- E Vier Gewährleistungen, je eigene Farbe, gleiche Tafelstruktur --------------------------------------------------
    ("[vier]Daraus folgen vier Gewährleistungen. [va]Das Strafgesetz muss geschrieben sein, [vb]bestimmt, [vc]streng "
     "angewendet [vd]und schon vor der Tat gelten.", PS),
    ("[sa]Erstens: lex scripta. Strafe braucht ein geschriebenes Gesetz. [sb]Gewohnheitsrecht darf keine Strafbarkeit "
     "begründen. [sc]Dass man fremde Boote nicht nimmt, ist eine Regel des Anstands, kein Straftatbestand.", P),
    ("[ca]Zweitens: lex certa, das Bestimmtheitsgebot. Es richtet sich an den Gesetzgeber. [cb]Er muss die Strafbarkeit "
     "so genau beschreiben, dass man sie im Regelfall schon am Wortlaut erkennt. [cc]Ein Gesetz nach dem Muster: Wer Unrecht "
     "tut, wird bestraft, genügte dem nicht.", P),
    ("[sta]Drittens: lex stricta, das Analogieverbot. Es richtet sich an die Gerichte. [stb]Paragraf zweihundertachtundvierzig "
     "b darf nicht auf Tretboote erweitert werden. [stc]Die Einzelheiten zeigen die Folgen zur Analogie und zur "
     "Unfallflucht.", P),
    ("[pa]Viertens: lex praevia, das Rückwirkungsverbot. [pb]Paragraf zwei Absatz eins Strafgesetzbuch: Die Strafe und ihre "
     "Nebenfolgen bestimmen sich nach dem Gesetz, das zur Zeit der Tat gilt. [pc]Ein neues Gesetz gegen fremde Bootsfahrten "
     "käme für Wieland zu spät.", PS),
    # --- F Schwerpunkt Bestimmtheit: BVerfGE 126, 170 (Untreue) ----------------------------------------------------------
    ("[best]Wie bestimmt muss ein Strafgesetz sein? [unt]Das zeigt der Untreue-Beschluss des Bundesverfassungsgerichts "
     "von zweitausendzehn. [weit]Der Untreuetatbestand ist sehr weit gefasst. [gk]Trotzdem ist er mit dem Bestimmtheitsgebot noch vereinbar. "
     "Denn wertungsbedürftige Begriffe, bis hin zu Generalklauseln, schließt das Bestimmtheitsgebot nicht von vornherein "
     "aus.", P),
    ("[pflicht]Dafür nimmt das Gericht die Rechtsprechung in die Pflicht. [pg]Sie muss Unklarheiten durch Präzisierung "
     "ausräumen, das ist das Präzisierungsgebot. [versch]Und sie darf ein Merkmal nicht so weit auslegen, dass es in "
     "einem anderen aufgeht. [vs2]Das nennt das Gericht Verschleifung.", P),
    ("[nachteil]Genau daran scheiterte eine der Verurteilungen. [nt2]Das Landgericht hatte den Vermögensnachteil nicht "
     "eigenständig ermittelt, sondern aus der Pflichtwidrigkeit gefolgert. [aufh]Das Bundesverfassungsgericht hob das "
     "Urteil auf.", PS),
    # --- F2 Sitzblockaden-Beschluss, BVerfGE 92, 1 ------------------------------------------------------------------------
    ("[sitz]Ein zweites Beispiel ist der Sitzblockaden-Beschluss von neunzehnhundertfünfundneunzig. [verg]Die Rechtsprechung "
     "hatte den Gewaltbegriff der Nötigung so vergeistigt, dass schon die bloße Anwesenheit auf der Straße als Gewalt "
     "galt, wenn sie andere psychisch hemmte. [unvor]Dann lässt sich nicht mehr sicher vorhersehen, was verboten ist. "
     "[vst]Nicht das Gesetz, aber diese Auslegung verstieß gegen Artikel hundertdrei Absatz zwei.", PS),
    # --- G Nur zulasten; § 3 OWiG -----------------------------------------------------------------------------------------
    ("[zug]Wichtig: All das schützt vor Strafe. [zug2]Eine Analogie zugunsten des Täters verbietet Artikel hundertdrei nicht. [zbsp]So wandte "
     "der Bundesgerichtshof die tätige Reue bei der Brandstiftung entsprechend an, als ein Täter die Lebensgefahr nicht "
     "durch Löschen, sondern auf andere Weise freiwillig beseitigte.", P),
    ("[owi]Dasselbe Prinzip gilt für Ordnungswidrigkeiten: [owi2]Paragraf drei des Ordnungswidrigkeitengesetzes verlangt, "
     "dass die Ahndung gesetzlich bestimmt war, bevor die Handlung begangen wurde.", PS),
    # --- H Lösung am See --------------------------------------------------------------------------------------------------
    ("[loes]Zurück am See. [l1]Ein Diebstahl scheidet aus, und Paragraf zweihundertachtundvierzig b erfasst kein "
     "Tretboot. [l2]Wieland bleibt straflos.", P),
    ("[ha2]Das ist also einfach erlaubt?", P, "Hartwin"),
    ("[pech]Strafbar ist es jedenfalls nicht. Pech für den Staat. [lg]Strafbarkeitslücken schließt nur der Gesetzgeber, und "
     "zwar nur für künftige Taten.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lege den Tatbestand aus, bis zur Grenze des Wortlauts. [tipp2]Passt der Fall dann nicht, ist "
     "Schluss: keine Analogie zulasten des Täters. [tipp3]Üblich ist etwa der Satz: Eine Anwendung auf das Tretboot wäre "
     "eine nach Artikel hundertdrei Absatz zwei verbotene Analogie.", PS),
    # --- J Prüfraster -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfraster für Artikel hundertdrei Absatz zwei. [k1]Erstens: Gibt es ein geschriebenes Gesetz? "
     "[k2]Zweitens: Galt es schon zur Tatzeit? [k3]Drittens: Ist es bestimmt genug? [k4]Viertens: Erfasst sein Wortlaut "
     "den Fall? [k5]Nur wenn alles zutrifft, darf bestraft werden.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Keine Strafe ohne geschriebenes, bestimmtes und vorher geltendes Gesetz. [m2]Was der Wortlaut nicht "
     "erfasst, bleibt straflos. Lücken schließt nur der Gesetzgeber.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
