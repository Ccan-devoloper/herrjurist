"""Folge 115 · Garantenstellung § 13 StGB: Wann muss ich einen Erfolg verhindern? (Mo · Der Fall · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook („Nach einer Kneipentour lässt ein Mann seinen volltrunkenen Freund bei Frost auf einer
Parkbank zurück“): Karsten und Wolfgang sitzen in einer Winternacht in ihrer letzten Kneipe; Wolfgang ist volltrunken.
Die Wirtin will ein Taxi rufen; Karsten sagt zu, Wolfgang nach Hause zu bringen, und führt ihn hinaus. Bei minus acht Grad
setzt er ihn auf eine Parkbank und geht; er hält eine Unterkühlung für möglich und nimmt sie in Kauf (mit dem Tod rechnet
er nicht). Eine Stunde später findet eine Passantin Wolfgang und ruft den Rettungsdienst; Unterkühlung, Wolfgang erholt sich.
Gewählt: Körperverletzung durch Unterlassen, §§ 223 Abs. 1, 13 Abs. 1 StGB (Erfolg eingetreten; § 221 Abs. 1 Nr. 2 ist nach
BGH ein echtes Unterlassungsdelikt ohne § 13, 2 StR 491/20 Rn. 35 – nur im Klausurtipp). Unterlassungsschema nur in zwei
Sätzen mit Verweis auf Folge 071. Kern: Wortlautkarte § 13 Abs. 1 (Auszug) → Funktionenlehre (Tabelle) → im Fall: Familie
nein, Zechgemeinschaft nein (BGH 2 StR 563/18 Rn. 12, 14), tatsächliche Übernahme ja (Zusage, Vertrauen der Wirtin,
Herausführen; 2 StR 563/18 Rn. 12, 17, 18; 5 StR 394/08 Rn. 23, 25; 4 StR 289/01 Rn. 20, 27; 5 StR 324/07 Rn. 23 f.),
Ingerenz offen; Selbstgefährdung ein Satz (1 StR 328/15 Rn. 18; Verweis 058) → Entsprechung, Vorsatz, RW/Schuld → Ergebnis
→ Gegenfall und Abgrenzung § 323c (Wortlautkarte Auszug; 2 StR 563/18 Rn. 17) → Klausurtipp → Schema → Merksatz.
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Karsten, Wolfgang
(nie im Genitiv mit -s). Wirtin und Passantin bleiben ohne Namen (Funktionsrollen).
Stimmen: Karsten stephan; Wirtin hilde; Passantin lucy; Wolfgang spricht nicht (stephan/christian klingen ähnlich).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Karsten": "stephan", "Wirtin": "hilde", "Passantin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der letzten Kneipe ----------------------------------------------------------------------------------
    ("[fall]Eine kalte Winternacht. [kneipe]Karsten und sein Freund Wolfgang ziehen seit Stunden durch die Kneipen und "
     "sitzen jetzt in der letzten. [voll]Wolfgang ist volltrunken und kann kaum noch stehen.", 0.3),
    ("[w1]Soll ich ihm ein Taxi rufen?", 0.3, "Wirtin"),
    ("[k1]Nicht nötig. Ich bring ihn nach Hause.", 0.3, "Karsten"),
    ("[raus]Die Wirtin ruft kein Taxi. Karsten führt Wolfgang hinaus.", 0.3),
    # --- A2 Fall: die Parkbank ----------------------------------------------------------------------------------------------
    ("[frost]Draußen sind es minus acht Grad. [bank]Nach ein paar Metern setzt Karsten ihn auf eine Parkbank.", 0.3),
    ("[k2]Ich muss jetzt los. Du schaffst das schon.", 0.3, "Karsten"),
    ("[weg]Karsten geht. [vors]Er hält es für möglich, dass Wolfgang sich eine Unterkühlung holt, und nimmt das in Kauf. "
     "[tod]Mit seinem Tod rechnet er nicht.", 0.3),
    # --- A3 Fall: eine Stunde später ---------------------------------------------------------------------------------------
    ("[stunde]Eine Stunde später findet eine Passantin Wolfgang.", 0.3),
    ("[p1]Hallo, hören Sie mich? Ich rufe den Rettungsdienst.", 0.3, "Passantin"),
    ("[klinik]Im Krankenhaus stellen die Ärzte eine Unterkühlung fest. Wolfgang erholt sich.", 0.4),
    ("[frage]Karsten hat Wolfgang nicht verletzt, er ist nur gegangen. Musste er die Unterkühlung verhindern? "
     "[frage2]Das hängt an einer Frage: War er Garant?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Einordnung ------------------------------------------------------------------------------------------------------
    ("[vorab]Vorgeworfen wird Karsten nicht, dass er Wolfgang auf die Bank gesetzt hat, sondern dass er ihn dort "
     "zurückgelassen hat. Der Schwerpunkt liegt im Unterlassen. [delikt]Wir prüfen Körperverletzung durch Unterlassen, "
     "Paragrafen zweihundertdreiundzwanzig und dreizehn. [s071]Das Schema des unechten Unterlassens kennst du aus dem Video "
     "zum unechten Unterlassen. [kurz]Hier liegen die meisten Merkmale auf der Hand: Die Unterkühlung ist eine "
     "Gesundheitsschädigung, und hätte Karsten Wolfgang heimgebracht, wäre sie mit an Sicherheit grenzender "
     "Wahrscheinlichkeit ausgeblieben. [heute]Offen ist die Garantenstellung.", PS),
    # --- D Wortlautkarte § 13 Abs. 1 (Auszug) ---------------------------------------------------------------------------------
    ("[p13]Paragraf dreizehn Absatz eins: Wer es unterlässt, einen Erfolg abzuwenden, der zum Tatbestand eines "
     "Strafgesetzes gehört, ist nach diesem Gesetz nur dann strafbar, [einst]wenn er rechtlich dafür einzustehen hat, dass "
     "der Erfolg nicht eintritt. [moral]Eine bloß moralische Pflicht genügt also nicht. [woher]Woraus die rechtliche Pflicht "
     "folgt, sagt das Gesetz nicht.", PS),
    # --- E Funktionenlehre -------------------------------------------------------------------------------------------------
    ("[funk]Die Lehre ordnet die Garantenstellungen nach ihrer Funktion. [besch]Beschützergaranten müssen ein bestimmtes "
     "Rechtsgut schützen: [fam]aus familiärer Verbundenheit, [gem]aus enger Lebens- oder Gefahrengemeinschaft [ueb]oder weil "
     "sie den Schutz tatsächlich übernommen haben. [ueberw]Überwachergaranten müssen eine Gefahr im Zaum halten: [ing]nach "
     "pflichtwidrigem Vorverhalten, der Ingerenz, [quelle]als Verantwortliche für eine Gefahrenquelle [aufs]oder bei der "
     "Aufsicht über andere Personen.", PS),
    # --- F Im Fall: Familie, Gemeinschaft ------------------------------------------------------------------------------------
    ("[fam2]Zur Familie gehört Wolfgang nicht. [zech]Und eine Gefahrengemeinschaft? Bloßes gemeinsames Zechen reicht nicht. "
     "Der Bundesgerichtshof grenzt lose Zusammenschlüsse wie Zechkumpane ausdrücklich ab. [zech2]Ihnen fehlt regelmäßig die "
     "Übernahme einer Beistandspflicht.", PS),
    # --- G Im Fall: tatsächliche Übernahme -----------------------------------------------------------------------------------
    ("[ueb2]Entscheidend ist also die tatsächliche Übernahme. [zusage]Karsten hat der Wirtin zugesagt, Wolfgang nach Hause zu "
     "bringen. [vertr]Im Vertrauen darauf ruft sie kein Taxi. [hinaus]Und Karsten führt Wolfgang aus der warmen Kneipe in die "
     "Kälte. [mehr]Das ist mehr als eine kurze Hilfe, die noch niemanden zum Garanten macht: Karsten hat die Lage von Wolfgang "
     "wesentlich verändert. [garant]Er ist Beschützergarant kraft tatsächlicher Übernahme. [ing2]Ob daneben Ingerenz vorliegt, "
     "kann offenbleiben.", PS),
    ("[selbst]Dass Wolfgang sich selbst betrunken hat, ändert nichts: Wird daraus eine konkrete Gefahr, muss der Garant "
     "handeln. Mehr dazu im Video zur eigenverantwortlichen Selbstgefährdung.", PS),
    # --- H Rest der Prüfung und Ergebnis ------------------------------------------------------------------------------------
    ("[entspr]Die Entsprechungsklausel ist bei der Körperverletzung als reinem Erfolgsdelikt regelmäßig unproblematisch. "
     "[vors2]Karsten kennt seine Zusage, hält die Unterkühlung für möglich und nimmt sie in Kauf. Das ist bedingter Vorsatz. "
     "[rw]Rechtfertigungs- und Entschuldigungsgründe fehlen; Wolfgang heimzubringen war ihm zumutbar.", P),
    ("[erg]Ergebnis: Karsten ist jedenfalls strafbar wegen Körperverletzung durch Unterlassen. [milder]Die Strafe kann nach Paragraf "
     "dreizehn Absatz zwei gemildert werden.", PS),
    # --- I Gegenfall und Abgrenzung § 323c -----------------------------------------------------------------------------------
    ("[gegen]Gegenfall: Karsten hat nur mit Wolfgang getrunken, nichts zugesagt und sieht ihn später auf der Bank sitzen. "
     "[kein]Dann ist er kein Garant. [p323]Ihn trifft nur die Jedermannspflicht aus Paragraf dreihundertdreiundzwanzig c: "
     "Strafbar ist, wer bei Unglücksfällen nicht hilft, obwohl das erforderlich und zumutbar ist. [echt]Das ist ein echtes "
     "Unterlassungsdelikt: Es bestraft das Nichthelfen selbst, nicht die Unterkühlung.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Nenne die Garantenstellung nicht nur, sondern begründe sie mit den Tatsachen aus dem Sachverhalt. "
     "[tipp2]Hier sind das die Zusage, das Vertrauen der Wirtin und das Herausführen in die Kälte. [tipp3]Und denk an die "
     "Aussetzung nach Paragraf zweihunderteinundzwanzig: Dort fragst du, ob der Täter dem Opfer beizustehen verpflichtet "
     "ist.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Körperverletzung durch Unterlassen. [s1]Römisch eins, Tatbestand. [s1a]Objektiv zuerst "
     "Erfolg, Nichtvornahme trotz Möglichkeit und Quasikausalität. [s1d]Dann die Garantenstellung: [s1d1]Prüfe zuerst "
     "Beschützergaranten, also Familie, Gemeinschaft und tatsächliche Übernahme. [s1d2]Dann Überwachergaranten, also "
     "Ingerenz, Gefahrenquelle und Aufsicht. [s1e]Danach die Entsprechung [s1f]und subjektiv der Vorsatz. [s2]Römisch zwei "
     "und drei: Rechtswidrigkeit und Schuld. [s4]Römisch vier: die Strafmilderung nach Paragraf dreizehn Absatz zwei.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gemeinsames Trinken allein macht niemanden zum Garanten. [m2]Wer aber den Schutz eines Hilflosen "
     "tatsächlich übernimmt, muss ihn auch zu Ende bringen. [m3]Sonst bleibt nur die Jedermannspflicht aus Paragraf "
     "dreihundertdreiundzwanzig c.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
