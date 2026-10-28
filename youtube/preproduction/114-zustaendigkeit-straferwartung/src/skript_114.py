"""Folge 114 · Straferwartung Zuständigkeit: Strafrichter, Schöffengericht, LG (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall nach dem Plan-Hook („Einem vorbestraften Beschuldigten werden zwölf Betrugstaten mit 40.000 Euro Gesamtschaden
vorgeworfen“), erzählt aus Sicht der Staatsanwältin, die die Abschlussverfügung schreibt: Herr Hartung (34, zweimal wegen
Betrugs vorbestraft) nimmt von Februar bis Juli 2026 in Erlenstadt (erfundener Ort) als angeblicher Terrassenbauer zwölf
Anzahlungen (2.000 bis 5.000 €, zusammen 40.000 €), ohne je bauen zu wollen, und lebt davon; Herr Grote (3.500 €) ist einer
der Kunden. Alle Taten und der Wohnsitz liegen in Erlenstadt. Im September liegt die Akte bei Staatsanwältin Eggert.
Kern als Schema: I. sachlich – Stufenleiter Strafrichter § 25 Nr. 2 GVG (Wortlaut), Schöffengericht § 28 i. V. m. § 24 GVG
(Strafbann § 24 Abs. 2), Landgericht § 24 Abs. 1 Satz 1 Nr. 2 (Wortlaut) / § 74 Abs. 1 GVG, Nr. 3 ein Satz, Schwurgericht
und OLG § 120 GVG ein Satz; Straferwartung: Vergehen (§ 12 Abs. 2, 3 StGB), § 263 Abs. 1/3 StGB, gewerbsmäßig (BGH
3 StR 556/25 Rn. 5), großes Ausmaß je Tat (BGH 1 StR 247/25 Rn. 14), Vorleben § 46 Abs. 2, Gesamtstrafe §§ 53, 54 StGB,
Prognose der Staatsanwältin als Einschätzung gekennzeichnet; II. örtlich §§ 7, 8, 3, 13 StPO; III. Anklage (§ 200 Abs. 1
Satz 2 StPO, Nr. 110 Abs. 3 RiStBV, Formel als Klausurkonvention). Klausurtipp (bewegliche Zuständigkeit, Nr. 113 RiStBV,
§ 209 StPO, BGH 2 StR 330/16 Rn. 11), Schema als Treppe, Merksatz.
Figuren: Herr Grote (helmut), Herr Hartung (niklas), Staatsanwältin Eggert (julia); Lexi/Erzählerin Carla.
Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Grote": "helmut", "Hartung": "niklas", "Eggert": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: im Garten von Herrn Grote, März 2026 ----------------------------------------------------------------
    ("[fall]Erlenstadt, im März. [grote]Herr Grote möchte eine neue Terrasse. [hart]Herr Hartung bietet sie ihm an, als "
     "selbstständiger Handwerker. [anz]Herr Grote zahlt dreitausendfünfhundert Euro an.", 0.3),
    ("[h1]Nächste Woche fangen wir an. Das Material ist schon bestellt.", 0.3, "Hartung"),
    # --- A2 Fall: derselbe Garten, Monate später ----------------------------------------------------------------------
    ("[nie]Gebaut wird nie.", 0.2),
    ("[g1]Seit April warte ich. Niemand kommt, und sein Telefon ist abgeschaltet.", 0.3, "Grote"),
    ("[elf]So geht es elf weiteren Kunden in Erlenstadt, von Februar bis Juli.", 0.3),
    # --- A3 Fall: bei der Staatsanwaltschaft, September -----------------------------------------------------------------
    ("[akte]Im September liegt die Akte bei Staatsanwältin Eggert. [zwoelf]Zwölf Anzahlungen, zusammen vierzigtausend Euro. "
     "[lebte]Material hat Herr Hartung nie bestellt, er lebte von dem Geld. [vor]Und er ist zweimal wegen Betrugs "
     "vorbestraft.", 0.3),
    ("[e_1]Zwölf Betrugstaten. Zu welchem Gericht klage ich an?", 0.3, "Eggert"),
    ("[frage]Strafrichter, Schöffengericht oder Landgericht? [frage2]Und welches Gericht ist örtlich zuständig?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Zwei Fragen --------------------------------------------------------------------------------------------------
    ("[plan]Die Staatsanwältin prüft zwei Fragen. [plan1]Erstens die sachliche Zuständigkeit: Sie folgt aus dem "
     "Gerichtsverfassungsgesetz, Paragraf eins StPO. [plan2]Zweitens die örtliche Zuständigkeit nach den Paragrafen sieben "
     "und folgende StPO. [plan3]Sachlich entscheidet vor allem eine Prognose: die Straferwartung.", PS),
    # --- D Die Treppe: Strafrichter, § 25 Nr. 2 GVG (Wortlaut) -----------------------------------------------------------
    ("[st1]Stell dir die sachliche Zuständigkeit als Treppe vor. [st1a]Unterste Stufe: der Strafrichter, Paragraf "
     "fünfundzwanzig Nummer zwei Gerichtsverfassungsgesetz. Er entscheidet bei Vergehen, wenn eine höhere Strafe als "
     "Freiheitsstrafe von zwei Jahren nicht zu erwarten ist.", P),
    # --- E Schöffengericht, § 28 i. V. m. § 24 GVG ---------------------------------------------------------------------
    ("[st2]Zweite Stufe: das Schöffengericht, Paragraf achtundzwanzig. Es entscheidet die übrigen Sachen des Amtsgerichts. "
     "[st2a]Mehr als vier Jahre Freiheitsstrafe darf das Amtsgericht aber nicht verhängen, Paragraf vierundzwanzig Absatz "
     "zwei.", P),
    # --- F Landgericht, § 24 Abs. 1 Satz 1 Nr. 2 GVG (Wortlaut), § 74 Abs. 1, Nr. 3, OLG ----------------------------------
    ("[st3]Dritte Stufe: das Landgericht. [st3a]Nach Paragraf vierundzwanzig Absatz eins Satz eins Nummer zwei ist das "
     "Amtsgericht nicht zuständig, wenn im Einzelfall eine höhere Strafe als vier Jahre Freiheitsstrafe zu erwarten ist, "
     "[st3b]oder die Unterbringung in einem psychiatrischen Krankenhaus oder in der Sicherungsverwahrung. [st3c]Dann ist die "
     "Strafkammer zuständig, Paragraf vierundsiebzig Absatz eins. [st3d]Nach Nummer drei kann die Staatsanwaltschaft "
     "außerdem wegen besonderer Schutzbedürftigkeit von Verletzten, besonderen Umfangs oder besonderer Bedeutung beim "
     "Landgericht anklagen.", P),
    ("[st4]Vorrang haben Sonderzuweisungen: [st4a]für Tötungsdelikte wie Mord das Schwurgericht, [st4b]und ganz oben das "
     "Oberlandesgericht, Paragraf hundertzwanzig, für Staatsschutzsachen wie Hochverrat.", PS),
    # --- G Straferwartung: Vergehen, Strafrahmen, Regelbeispiel ------------------------------------------------------------
    ("[e1]Jetzt bildet die Staatsanwältin die Straferwartung. [e2]Betrug ist ein Vergehen, Paragraf zwölf StGB, "
     "[e2a]auch im besonders schweren Fall: Solche Schärfungen bleiben nach Absatz drei außer Betracht.", P),
    ("[e3]Paragraf zweihundertdreiundsechzig Absatz eins droht Freiheitsstrafe bis zu fünf Jahren oder Geldstrafe an. [e4]In besonders schweren Fällen "
     "sind es nach Absatz drei sechs Monate bis zehn Jahre. [e5]Ein Regelbeispiel ist gewerbsmäßiges Handeln. "
     "[e6]Gewerbsmäßig handelt nach dem Bundesgerichtshof, wer sich durch wiederholte Taten eine nicht nur vorübergehende "
     "Einnahmequelle von einigem Umfang und einiger Dauer verschaffen will. [e7]Herr Hartung lebte von den Anzahlungen: "
     "Das Regelbeispiel ist erfüllt. [e8]Ein Vermögensverlust großen Ausmaßes scheidet dagegen aus: Er wird für jede Tat "
     "einzeln bestimmt, die Grenze liegt grundsätzlich bei fünfzigtausend Euro.", P),
    # --- H Vorstrafen und Gesamtstrafe ---------------------------------------------------------------------------------
    ("[e9]Die Vorstrafen wirken strafschärfend: Paragraf sechsundvierzig nennt das Vorleben des Täters. [e10]Zwölf Taten "
     "heißt zwölf Einzelstrafen, und daraus wird eine Gesamtstrafe, Paragraf dreiundfünfzig. [e11]Nach Paragraf "
     "vierundfünfzig wird die höchste Einzelstrafe erhöht, die Summe darf aber nicht erreicht werden. "
     "[e11a]Das ist das Asperationsprinzip.", P),
    ("[e12]Die Prognose der Staatsanwältin: Einzelstrafen um ein Jahr, eine Gesamtstrafe von etwa zweieinhalb bis "
     "dreieinhalb Jahren. [e13]Das ist ihre Einschätzung im Einzelfall, keine feste Regel.", PS),
    # --- I Ergebnis: sachlich zuständig ----------------------------------------------------------------------------------
    ("[f1]Damit steht die Stufe fest: [f2]Über zwei Jahre, also nicht der Strafrichter. [f3]Nicht über vier Jahre, also "
     "kein Landgericht nach Nummer zwei. [f4]Für besonderen Umfang oder besondere Bedeutung ist nichts ersichtlich. "
     "[f5]Sachlich zuständig ist das Amtsgericht, Schöffengericht.", PS),
    # --- J II. Örtliche Zuständigkeit, §§ 7, 8, 3, 13 StPO ---------------------------------------------------------------
    ("[o1]Nun die örtliche Zuständigkeit. [o2]Gerichtsstand ist der Tatort, Paragraf sieben: Alle zwölf Taten geschahen in "
     "Erlenstadt. [o3]Dazu kommt der Wohnsitz bei Erhebung der Klage, Paragraf acht: Auch Herr Hartung wohnt dort. "
     "[o4]Lägen die Tatorte in verschiedenen Bezirken, hilft der Zusammenhang: Wird eine Person mehrerer Taten beschuldigt, "
     "ist jedes Gericht zuständig, das für eine der Taten zuständig wäre, Paragrafen drei und dreizehn.", PS),
    # --- K III. Die Anklage ----------------------------------------------------------------------------------------------
    ("[an1]In der Anklageschrift nennt die Staatsanwältin das Gericht, Paragraf zweihundert Absatz eins, [an2]nach den "
     "Richtlinien für das Strafverfahren samt Spruchkörper.", 0.3),
    ("[e_2]Anklage zum Amtsgericht, Schöffengericht, Erlenstadt.", 0.3, "Eggert"),
    ("[an3]Die genaue Formel ist Klausurkonvention.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Begründe die Straferwartung konkret, mit Strafrahmen, Vorstrafen und Gesamtstrafe. [tipp2]Eine "
     "Zahl ohne Begründung überzeugt nicht. [tipp3]Und die besondere Bedeutung nach Nummer drei ist die bewegliche "
     "Zuständigkeit: Die Staatsanwaltschaft hält die Gründe in den Akten fest, [tipp4]und das Gericht prüft sie bei der "
     "Eröffnung.", PS),
    # --- M Klausurschema (Treppe) --------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Zuständigkeit. [k1]Römisch eins: sachlich. [k11]Eins: Sonderzuweisungen. [k12]Zwei: die "
     "Straferwartung, aus Strafrahmen, Vorstrafen und Gesamtstrafe. [k13]Drei: die Stufe, Strafrichter bis zwei Jahre, "
     "Schöffengericht bis vier, darüber das Landgericht. [k14]Vier: besondere Bedeutung, Umfang oder Schutzbedürftigkeit. "
     "[k2]Römisch zwei: örtlich, mit Tatort, Wohnsitz und Zusammenhang. [k3]Römisch drei: das Gericht in der Anklage.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Straferwartung bestimmt die Stufe. [mk2]Bei Vergehen bis zwei Jahre der Strafrichter, bis vier "
     "Jahre das Schöffengericht, darüber das Landgericht. [mk3]Und jede Prognose braucht eine Begründung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
