"""Folge 157 · Verabredete Schlägerei: Einwilligung? Sittenwidrigkeit § 228 StGB (Mo · Der Fall · Klassiker-Fall;
§§ 223, 224, 228, 231 StGB). Fiktiver Einstieg nach dem Plan-Hook (zwei Hooligan-Gruppen verabreden per Chat ein „Match“
auf einer abgelegenen Wiese, ohne Waffen, mit Schiedsrichtern), danach der echte Fall sachlich:
BGH, Beschl. v. 20.2.2013 – 1 StR 585/12, BGHSt 58, 140 (Volltext HRRS 2013 Nr. 342, Randnummern nach HRRS).
Fortführung zu Kämpfen mit Regeln und „Schiedsrichtern“: BGH, Urt. v. 22.1.2015 – 3 StR 233/14, BGHSt 60, 166
(HRRS 2015 Nr. 285). Maßstab: BGH, Urt. v. 26.5.2004 – 2 StR 505/03, BGHSt 49, 166 (HRRS 2004 Nr. 624).
Voraussetzungen der Einwilligung nur als Verweis auf Folge 062 (ein Satz).
DARSTELLUNG: keine Prügelszene, keine Schläge, kein Blut, keine Verletzten im Bild; keine Vereinsfarben, Schals, Logos.
Gruppen nur als neutrale farbige Gruppen-Icons/Pillen „Gruppe A“/„Gruppe B“, Verabredung über Chat-Icons, Wiese als
Landschafts-Icon; Sönke und Inken als ruhig stehende Erwachsene in Alltagskleidung. Im echten Fall keine Figuren.
Figuren fiktiv: Sönke (Gruppe A, Stimme stephan), Inken (Gruppe B, Stimme lucy).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Sönke": "stephan", "Inken": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fiktiver Einstieg: Verabredung per Chat ------------------------------------------------------------------------
    ("[fall]Zwei Hooligan-Gruppen verabreden sich per Chat zu einem Match. [soenke]Sönke schreibt für Gruppe A:", P),
    ("[s1]Samstag, zehn gegen zehn, auf der Wiese am Waldrand. Keine Waffen, sonst ist alles erlaubt.", P, "Sönke"),
    ("[inken]Inken antwortet für Gruppe B:", P),
    ("[i1]Einverstanden. Wer am Boden liegt, ist raus. Und wir bringen zwei Schiedsrichter mit.", P, "Inken"),
    ("[match]Am Samstag treffen sich beide Gruppen auf der abgelegenen Wiese. Alle wissen, dass es Verletzte geben wird, "
     "und alle sind einverstanden. [verl]Einige werden leicht verletzt. [frage0]Sind die Schläge durch die Einwilligung "
     "gerechtfertigt? [klassiker]Die Antwort steckt in einem Klassiker des Bundesgerichtshofs.", PS),
    # --- B Der echte Fall (BGHSt 58, 140, Rn. 2–5) ------------------------------------------------------------------------
    ("[echt]Zwei Gruppen junger Leute geraten aneinander. [anruf]Ein "
     "Angeklagter ruft per Telefon weitere Mitglieder seiner Gruppe herbei. [gegen]Dann stehen sich beide Gruppen gegenüber. "
     "[faktisch]Faktisch einigen sich alle, die Sache mit Faustschlägen und Fußtritten "
     "auszutragen; auch erhebliche Verletzungen nehmen sie hin. [minuten]In vier bis fünf Minuten werden mehrere "
     "Beteiligte erheblich verletzt.", P),
    ("[lg]Das Landgericht Stuttgart verurteilt die Angeklagten wegen gefährlicher Körperverletzung. [bgh]Der "
     "Bundesgerichtshof verwirft ihre Revisionen, Beschluss vom zwanzigsten Februar zweitausenddreizehn. [frage]Warum "
     "hilft die Einwilligung nicht?", PS),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Einwilligung (Verweis Folge 062) und § 228 (Wortlautkarte) ----------------------------------------------------
    ("[einw]Wann eine Einwilligung wirksam ist, haben wir in einer eigenen Folge geprüft. [hier]Zwei der Verletzten hatten "
     "durch die Übereinkunft in Faustschläge und Fußtritte eingewilligt, und damit auch in die typischen Folgen. "
     "[p228]Die Grenze zieht Paragraf zweihundertachtundzwanzig: Wer eine Körperverletzung mit Einwilligung der verletzten "
     "Person vornimmt, handelt nur dann rechtswidrig, wenn die Tat trotz der Einwilligung gegen die guten Sitten verstößt. "
     "[ort]Die Frage gehört also in die Rechtswidrigkeit.", P),
    # --- E Maßstab der Rechtsprechung (BGHSt 58, 140 Rn. 9, 12; BGHSt 49, 166 Rn. 22–24, 26, 29) -------------------------
    ("[mass]Wann verstößt eine Tat gegen die guten Sitten? Vorrangig zählen Art und Gewicht der Verletzung und der Grad "
     "der Gefahr für Leib und Leben. [exante]Beurteilt wird aus der Sicht vor der Tat. [tod]Sittenwidrig ist die Tat "
     "jedenfalls, wenn sie den Einwilligenden in konkrete Todesgefahr bringt. [zweck]Ein verwerflicher Zweck allein macht "
     "sie nicht sittenwidrig. [heil]Ein guter Zweck kann eine schwere Verletzung nur ausnahmsweise decken, etwa beim "
     "ärztlichen Eingriff.", P),
    # --- F Kern BGHSt 58, 140 (Rn. 11, 17, 18, 20, 22) ---------------------------------------------------------------------
    ("[gesamt]Im echten Fall zählen vor allem die Gesamtumstände, nicht der einzelne Schlag. "
     "[eskal]Bei Schlägereien zwischen rivalisierenden Gruppen droht typischerweise eine Eskalation. "
     "[dynamik]Die Gruppen beeinflussen sich gegenseitig, die Lage wird unkontrollierbar. [abspr]Hier gab es keine "
     "Absprachen, die etwa Schläge gegen Wehrlose oder eine Überzahl ausschließen, [sicher]und keine effektiven "
     "Sicherungen für ihre Einhaltung. [sitten]Deshalb verstoßen die Taten gegen die guten Sitten, selbst wenn die "
     "einzelnen Verletzungen keine konkrete Todesgefahr begründen.", P),
    # --- G § 231 StGB (Wortlautkarte; BGHSt 58, 140 Rn. 17) ---------------------------------------------------------------
    ("[p231]Dafür spricht auch Paragraf zweihunderteinunddreißig, die Beteiligung an einer Schlägerei. [p231b]Bestraft "
     "wird schon die Beteiligung, wenn durch die Schlägerei der Tod eines Menschen oder eine schwere Körperverletzung verursacht wird. [vorfeld]So "
     "schützt der Gesetzgeber Leben und Gesundheit schon im Vorfeld.", P),
    # --- H Abgrenzung Sport (BGHSt 58, 140 Rn. 13, 15) --------------------------------------------------------------------
    ("[sport]Anders beim Boxkampf. [regeln]Dort begrenzen Wettkampfregeln, die Verbände aufstellen und überwachen, die "
     "Gefahr. [gedeckt]Verletzungen nach diesen Regeln verstoßen deshalb nicht gegen die guten Sitten. [grob]Wer aber "
     "grob fahrlässig oder vorsätzlich gegen die Regeln verstößt, ist von der Einwilligung nicht mehr gedeckt.", P),
    # --- I Absprachen und Schiedsrichter (BGHSt 58, 140 Rn. 23; BGHSt 60, 166 Rn. 7, 45, 47, 50, 52, 54) -------------------
    ("[offen]Und wenn es Absprachen gibt? Das musste der Bundesgerichtshof hier nicht entscheiden. [neigt]Er neigt aber "
     "zur Sittenwidrigkeit, wenn die Einhaltung des Verabredeten nicht ausreichend sicher gewährleistet ist. [hool]Knapp "
     "zwei Jahre später ging es um Hooligan-Kämpfe mit Regeln: Waffen waren verboten, teils schauten sogenannte "
     "Schiedsrichter zu. [wertung]Auch hier waren die Körperverletzungen sittenwidrig, wegen der Wertung des Paragrafen "
     "zweihunderteinunddreißig, unabhängig von Vorkehrungen gegen eine Eskalation. [kopf]Jedenfalls drohten schwere "
     "Gesundheitsschäden: Schläge und Tritte gegen den Kopf waren erlaubt. [box2]Und der Unterschied zum Boxen? Für Schlägereien "
     "mehrerer gibt es diese gesetzliche Wertung, für Einzelkämpfe nicht.", PS),
    # --- J Zurück zum Einstieg -----------------------------------------------------------------------------------------------
    ("[s2]Aber wir hatten doch Regeln und Schiedsrichter!", P, "Sönke"),
    ("[l1]Prüfen wir. Schläge sind körperliche Misshandlungen, Paragraf zweihundertdreiundzwanzig. [l2]Begangen mit "
     "einem anderen Beteiligten gemeinschaftlich: Paragraf zweihundertvierundzwanzig Absatz eins Nummer vier. [l3]In der "
     "Rechtswidrigkeit: Alle haben eingewilligt. [l4]Aber zehn gegen zehn ist eine Schlägerei, und Schläge gegen den Kopf "
     "sind nicht ausgeschlossen. [l5]Zwei Schiedsrichter können eine Eskalation unter zwanzig Kämpfern nicht sicher "
     "verhindern. [l6]Nach dem Bundesgerichtshof ist die Tat deshalb sittenwidrig.", PS),
    ("[erg]Ergebnis: Die Einwilligung ist unwirksam, die Körperverletzungen sind rechtswidrig. [erg2]Wer zugeschlagen "
     "hat, handelt auch schuldhaft und ist wegen gefährlicher Körperverletzung strafbar. [p231c]Nach Paragraf "
     "zweihunderteinunddreißig selbst wird nur bestraft, wenn ein Mensch stirbt oder eine schwere Körperverletzung eintritt.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Sittenwidrigkeit prüfst du in der Rechtswidrigkeit, als Grenze der Einwilligung. [tipp2]Und "
     "bei Gruppen bewertest du nicht nur den einzelnen Schlag, sondern die Eskalationsgefahr.", PS),
    # --- L Prüfschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand, Paragrafen zweihundertdreiundzwanzig und zweihundertvierundzwanzig "
     "Absatz eins Nummer vier. [k2]Römisch zwei: Rechtswidrigkeit. [k2a]Erstens die Voraussetzungen der Einwilligung. "
     "[k2b]Zweitens keine Sittenwidrigkeit nach Paragraf zweihundertachtundzwanzig: Gewicht der Verletzung und Gefahr, aus "
     "der Sicht vor der Tat. [k2c]Bei Gruppen: Eskalationsgefahr, Absprachen und Sicherungen, Wertung des Paragrafen "
     "zweihunderteinunddreißig. [k3]Römisch drei: Schuld.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf zweihundertachtundzwanzig ist die Grenze der Einwilligung. [m2]Bei verabredeten Schlägereien "
     "zwischen Gruppen ist die Tat sittenwidrig, wenn wirksame Absprachen und effektive Sicherungen gegen die Eskalation "
     "fehlen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
