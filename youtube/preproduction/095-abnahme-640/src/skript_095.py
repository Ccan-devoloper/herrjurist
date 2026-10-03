"""Folge 095 · Abnahme Werkvertrag § 640 BGB: Wirkungen und fiktive Abnahme (Mi · Examenswissen · Zivilrecht/
Werkvertragsrecht, Format Schema). Beispielfall nach dem Plan-Hook („Der Fliesenleger ist fertig und will sein Geld – du
hast Zweifel an den Fugen“): Susanne (Verbraucherin) lässt ihr Bad vom Fliesenleger Herrn Fiedler sanieren, Rechnung
3.800 €. Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig (optischer Mangel, Nachbessern 150 €; Bad dicht und
voll nutzbar). Herr Fiedler setzt per E-Mail 2 Wochen Frist zur Abnahme, mit Hinweis auf die Folgen (Textform).
Kern: Begriff (BGH VII ZR 276/13 Rn. 21; VII ZR 64/09 Rn. 21 f.), Wortlautkarten § 640 Abs. 1 und Abs. 2 Satz 1, Pflicht
und Verweigerung nur wegen wesentlicher Mängel, fiktive Abnahme mit Verbraucherhinweis § 640 Abs. 2 Satz 2, ein Mangel
genügt (BT-Drs. 18/8486 S. 48 f., 18/11437 S. 40), endgültige unberechtigte Verweigerung (BGH VII ZR 158/09 Rn. 5),
Vorbehalt § 640 Abs. 3; Wirkungen: Fälligkeit § 641 Abs. 1 (Bauvertrag: § 650g Abs. 4), Gefahr § 644, Verjährungsbeginn
§ 634a Abs. 2, Beweislast und Mängelstadium (BGH VII ZR 301/13 Rn. 31, 35 f.); Ergebnis mit § 641 Abs. 3.
Figuren: Susanne (laura_ruhig), Herr Fiedler (marc); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Susanne": "laura_ruhig", "Fiedler": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das neue Bad ---------------------------------------------------------------------------------------
    ("[fall]Susanne lässt ihr Bad sanieren, vom Fliesenleger Herrn Fiedler. [neu]Neue Fliesen an Wand und Boden, dazu "
     "eine neue Wanne.", 0.3),
    ("[fi1]Fertig! Hier ist meine Rechnung: dreitausendachthundert Euro.", 0.3, "Fiedler"),
    ("[pruef]Susanne schaut genau hin. [fuge]Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig. [schoen]Ein "
     "reiner Schönheitsfehler. Nachbessern kostet hundertfünfzig Euro.", 0.3),
    ("[su1]Die Fuge hinter der Tür ist nicht sauber. Muss ich da gleich alles zahlen?", 0.3, "Susanne"),
    # --- A2 Fall: die E-Mail -----------------------------------------------------------------------------------------
    ("[mail]Am nächsten Tag schreibt Herr Fiedler ihr eine E-Mail: [frist]Bitte nehmen Sie das Bad innerhalb von zwei "
     "Wochen ab. [hinw]Dazu der Hinweis: Wer schweigt oder die Abnahme ohne Angabe eines Mangels verweigert, bei dem gilt "
     "das Bad als abgenommen.", 0.3),
    ("[frage]Muss Susanne das Bad abnehmen und zahlen? [frage2]Und was passiert, wenn sie einfach schweigt?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Begriff ---------------------------------------------------------------------------------------------------
    ("[begr]Erst der Begriff. [b1]Abnahme heißt: Der Besteller nimmt das Werk körperlich entgegen [b2]und billigt es als "
     "im Wesentlichen vertragsgemäß. [b3]Das geht ausdrücklich, [b4]aber auch stillschweigend durch schlüssiges Verhalten, "
     "meist erst nach einer angemessenen Prüfzeit.", P),
    # --- D § 640 Abs. 1 (Wortlaut) -----------------------------------------------------------------------------------
    ("[p640]Paragraf sechshundertvierzig Absatz eins: Der Besteller ist verpflichtet, das vertragsmäßig hergestellte Werk "
     "abzunehmen, sofern nicht nach der Beschaffenheit des Werkes die Abnahme ausgeschlossen ist. [p640b]Wegen "
     "unwesentlicher Mängel kann die Abnahme nicht verweigert werden.", P),
    ("[pfl]Die Abnahme ist also eine Pflicht. Verweigern darf Susanne sie nur wegen eines wesentlichen Mangels. "
     "[fsub]Die breitere Fuge ist ein Mangel, aber nur ein optischer: Das Bad ist dicht und voll nutzbar. "
     "[unw]Das ist unwesentlich. Susanne muss abnehmen.", PS),
    # --- E § 640 Abs. 2 fiktive Abnahme (Wortlaut) -------------------------------------------------------------------
    ("[fikt]Und wenn Susanne einfach schweigt? Dann hilft dem Unternehmer Absatz zwei, die fiktive Abnahme. [w640]Als "
     "abgenommen gilt ein Werk auch, wenn der Unternehmer dem Besteller nach Fertigstellung des Werks eine angemessene "
     "Frist zur Abnahme gesetzt hat und der Besteller die Abnahme nicht innerhalb dieser Frist unter Angabe mindestens "
     "eines Mangels verweigert hat.", P),
    ("[verb]Ist der Besteller Verbraucher, verlangt Satz zwei mehr: Der Unternehmer muss zusammen mit der Aufforderung "
     "auf die Folgen hinweisen, und zwar in Textform. [vsub]Susanne ist Verbraucherin. Die E-Mail kommt nach der "
     "Fertigstellung, setzt zwei Wochen Frist und enthält den Hinweis. Eine E-Mail wahrt grundsätzlich die Textform. [schw]Schweigt "
     "Susanne bis zum Fristende, gilt das Bad als abgenommen.", PS),
    ("[mang]Nennt sie dagegen die Fuge, tritt die Fiktion nicht ein. [ein]Ein einziger Mangel genügt, auch ein "
     "unwesentlicher. Missbräuchlich kann es nach der Gesetzesbegründung nur sein, offensichtlich nicht bestehende oder "
     "eindeutig unwesentliche Mängel zu nennen. "
     "[endg]Aber Susanne bleibt zur Abnahme verpflichtet. Verweigert sie die Abnahme zu Unrecht endgültig, wird der "
     "Werklohn nach dem Bundesgerichtshof trotzdem fällig.", PS),
    # --- F § 640 Abs. 3 Vorbehalt ------------------------------------------------------------------------------------
    ("[vorb]Was soll Susanne also tun? Abnehmen, aber unter Vorbehalt. [p640c]Denn nach Absatz drei gilt: Nimmt sie ab, "
     "obwohl sie den Mangel kennt, und behält sie sich ihre Rechte bei der Abnahme nicht vor, verliert sie wegen dieses Mangels "
     "Nacherfüllung, Selbstvornahme, Rücktritt und Minderung. [se]Der Schadensersatz nach Nummer vier bleibt.", PS),
    # --- G Wirkungen der Abnahme -------------------------------------------------------------------------------------
    ("[wirk]Jetzt der Kern: Was bewirkt die Abnahme? [w1]Erstens wird die Vergütung fällig, Paragraf "
     "sechshunderteinundvierzig Absatz eins. [bau]Ist die Sanierung ein Bauvertrag, kommt nach Paragraf sechshundertfünfzig "
     "g eine prüffähige Schlussrechnung hinzu. Die Rechnung von Herrn Fiedler listet alle Posten auf.", P),
    ("[w2]Zweitens geht die Gefahr über, Paragraf sechshundertvierundvierzig. [w2b]Bis zur Abnahme trägt sie der "
     "Unternehmer: Zerstört vorher ein Rohrbruch die Fliesen, ohne dass jemand etwas dafür kann, ist das sein Risiko. "
     "[w3]Drittens beginnt die Verjährung der Mängelansprüche, Paragraf sechshundertvierunddreißig a Absatz zwei: "
     "[w3b]zwei Jahre bei Arbeiten an einer Sache, fünf Jahre bei einem Bauwerk.", P),
    ("[w4]Viertens kehrt sich nach dem Bundesgerichtshof die Beweislast um. Vor der Abnahme muss der Unternehmer beweisen, dass sein Werk "
     "mangelfrei ist. [w4b]Danach muss der Besteller den Mangel beweisen, außer bei Mängeln, die er sich vorbehalten hat. "
     "[w5]Und fünftens endet das Erfüllungsstadium: Statt der Herstellung hat der Besteller grundsätzlich die "
     "Mängelrechte aus Paragraf sechshundertvierunddreißig.", PS),
    # --- H Ergebnis --------------------------------------------------------------------------------------------------
    ("[erg]Für Susanne heißt das: Sie nimmt das Bad ab und behält sich die Fuge vor. [erg2]Damit ist der Werklohn fällig, "
     "und sie kann verlangen, dass Herr Fiedler den Mangel beseitigt. [zbr]Bis dahin darf sie nach Paragraf "
     "sechshunderteinundvierzig Absatz drei einen angemessenen Teil zurückhalten, in der Regel das Doppelte der Kosten. "
     "[zbr2]Zweimal hundertfünfzig, also dreihundert Euro. Jetzt zahlt sie dreitausendfünfhundert, den Rest nach der Nachbesserung.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Abnahme prüfst du beim Werklohn unter der Fälligkeit, [tipp2]und zwar in dieser "
     "Reihenfolge: erklärt oder stillschweigend, dann fiktiv, dann zu Unrecht endgültig verweigert. [tipp3]Und bei "
     "Mängelrechten fragst du zuerst: Ist schon abgenommen?", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Werklohn: [k1]Römisch eins: Anspruch entstanden, also ein wirksamer Werkvertrag. "
     "[k2]Römisch zwei: Fälligkeit nach Paragraf sechshunderteinundvierzig. [k2a]Dafür die Abnahme: erklärt oder "
     "stillschweigend, [k2b]fiktiv nach Paragraf sechshundertvierzig Absatz zwei, [k2c]oder zu Unrecht endgültig "
     "verweigert. [k3]Römisch drei: Durchsetzbarkeit, etwa das Leistungsverweigerungsrecht aus Paragraf "
     "sechshunderteinundvierzig Absatz drei.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Abnahme ist die Zäsur im Werkvertrag. [mk2]Mit ihr wird der Lohn fällig, die Gefahr geht über, "
     "die Verjährung beginnt, und die Beweislast für Mängel wechselt. [mk3]Und wer auf eine Frist zur Abnahme "
     "schweigt, riskiert die fiktive Abnahme.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
