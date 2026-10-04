"""Folge 172 · Folgenbeseitigungsanspruch: Die Stadt pflastert deinen Vorgarten (Mo · Der Fall · Öffentliches Recht/
Staatshaftungsrecht, Format Klassiker-Fall als Fall mit Schema). Übungsfall nach dem Plan-Hook („Beim Ausbau des Gehwegs hat
die Gemeinde versehentlich einen Streifen deines Vorgartens mitgepflastert“): Ottilie (Eigentümerin, fiktiv) hat einen
Vorgarten an der Straße; beim Ausbau des Gehwegs pflastern Bauarbeiter der (namenlosen, fiktiven) Gemeinde versehentlich
einen 30 cm breiten Streifen ihres Vorgartens mit. Herr Wernicke vom Bauamt bietet Geld an, Ottilie will den Vorgarten zurück.
Aufbau: Einordnung (Kontrast § 1004 BGB, Verweis 142; Staatshaftung, Amtshaftung nur ein Satz) → I. Rechtsgrundlage
(ungeschrieben, ständige Rechtsprechung; Wortlautkarten Art. 20 Abs. 3 GG, Art. 14 Abs. 1 GG, § 113 Abs. 1 Satz 2 VwGO;
Herleitungsstreit kurz, BVerwG 6 B 33.15 Rn. 14; Verweis 069) → II. Voraussetzungen mit eigener Farbe je Punkt
(1. hoheitlicher Eingriff: Realakt, BVerwG 7 B 14.15 Rn. 8; 2. subjektives Recht: Eigentum; 3. rechtswidriger Zustand dauert
an, Legalisierung BVerwG 9 C 5.19 Rn. 13 f.; 4. Wiederherstellung möglich und zumutbar) → III. Rechtsfolge (Status quo ante,
kein Schadensersatz; Wortlautkarte Art. 34 Satz 1 GG, § 839 BGB ein Satz) → Mitverschulden (BVerwG 3 C 17.09 Rn. 28) →
Prozessuales (§ 40 Abs. 1 VwGO, allgemeine Leistungsklage, ein Satz) → Lösung → Klausurtipp, Schema, Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md. Figuren: Ottilie (sabrina), Herr Wernicke (marc); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ottilie": "sabrina", "Wernicke": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Gehweg wird ausgebaut ----------------------------------------------------------------------------
    ("[fall]Ottilie hat vor ihrem Haus einen kleinen Vorgarten mit Rosen. [bau]Die Gemeinde baut den Gehweg davor aus. "
     "[streifen]Dabei pflastern die Bauarbeiter versehentlich einen dreißig Zentimeter breiten Streifen ihres Vorgartens "
     "mit. [rosen]Wo vorher Rosen standen, liegen jetzt Pflastersteine.", 0.3),
    # --- A2 Fall: Gespräch am Gartenrand -------------------------------------------------------------------------------
    ("[ot1]Herr Wernicke, das ist mein Vorgarten! Die Steine müssen wieder weg.", 0.3, "Ottilie"),
    ("[we1]Das war ein Versehen. Ich kann Ihnen dafür Geld anbieten.", 0.3, "Wernicke"),
    ("[ot2]Ich will kein Geld. Ich will meinen Vorgarten zurück.", 0.3, "Ottilie"),
    ("[frage]Kann Otti-lie verlangen, dass die Gemeinde das Pflaster entfernt [frage2]und den Vorgarten wiederherstellt?",
     0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Einordnung ----------------------------------------------------------------------------------------------------
    ("[einord]Unter Privaten gäbe es den Beseitigungsanspruch aus Paragraf tausendvier BGB, dazu das Video zum "
     "Beseitigungsanspruch. [hoheit]Hier aber baut die Gemeinde hoheitlich. [fba]Ottilies Anspruch heißt deshalb "
     "Folgenbeseitigungsanspruch, [stsh]ein Teil des Staatshaftungsrechts.", PS),
    # --- D I. Rechtsgrundlage: ungeschrieben; Art. 20 Abs. 3 GG ----------------------------------------------------------
    ("[rg]Römisch eins: die Rechtsgrundlage. Der Folgenbeseitigungsanspruch steht in keinem Gesetz. [stRspr]Er ist aber "
     "in ständiger Rechtsprechung anerkannt, oft spricht man von Gewohnheitsrecht. [herl]Das Bundesverwaltungsgericht "
     "verankert ihn in den Grundrechten und im Rechtsstaatsprinzip. [w20]Artikel zwanzig Absatz drei GG: Die "
     "Gesetzgebung ist an die verfassungsmäßige Ordnung, die vollziehende Gewalt und die Rechtsprechung sind an Gesetz "
     "und Recht gebunden. [w20b]Handelt die Verwaltung rechtswidrig, muss sie die Folgen also wieder beseitigen.", P),
    # --- E I. Rechtsgrundlage: Art. 14 Abs. 1 GG, § 113 Abs. 1 Satz 2 VwGO ----------------------------------------------
    ("[w14]Dazu das betroffene Grundrecht, hier Artikel vierzehn Absatz eins Satz eins: Das Eigentum und das Erbrecht "
     "werden gewährleistet. [abwehr]Als Abwehrrecht schützt es den Eigentümer auch gegenüber dem Staat. "
     "[w113]Und Paragraf hundertdreizehn Absatz eins Satz zwei VwGO: Ist der Verwaltungsakt schon vollzogen, so kann das "
     "Gericht auf Antrag auch aussprechen, dass und wie die Verwaltungsbehörde die Vollziehung rückgängig zu machen hat. "
     "[streit]Ob der Anspruch daraus folgt, ist umstritten. [prozess]Das Bundesverwaltungsgericht sieht darin ein "
     "prozessuales Mittel für den Anspruch, dazu das Video zur Anfechtungsklage. [keinva]Otti-lie hilft "
     "die Vorschrift aber nicht: Es gibt keinen Verwaltungsakt.", PS),
    # --- F II. Voraussetzungen im Überblick ------------------------------------------------------------------------------
    ("[vor]Römisch zwei: die Voraussetzungen, vier Punkte. [v1]Erstens ein hoheitlicher Eingriff, [v2]zweitens in ein "
     "subjektives Recht. [v3]Drittens ist dadurch ein rechtswidriger Zustand entstanden, der noch andauert. [v4]Viertens "
     "muss die Wiederherstellung möglich und zumutbar sein.", P),
    # --- G II. 1. Hoheitlicher Eingriff in ein subjektives Recht ---------------------------------------------------------
    ("[a1]Zum ersten Punkt. Die Gemeinde hat keinen Bescheid erlassen, sie hat einfach gebaut. [a2]Das ist ein "
     "Realakt, schlicht-hoheitliches Handeln. [a3]Auch das kann ein Eingriff sein. [a4]Hoheitlich ist ein Realakt, "
     "wenn er in einem öffentlich-rechtlichen Planungs- und Funktionszusammenhang steht. [a5]Der Ausbau des Gehwegs ist Straßenbau, "
     "eine öffentliche Aufgabe der Gemeinde. [b1]Zum zweiten Punkt: Betroffen ist Ottilies Eigentum am Vorgarten, ein "
     "subjektives Recht, geschützt durch Artikel vierzehn.", P),
    # --- H II. 2. Rechtswidriger Zustand, der andauert -------------------------------------------------------------------
    ("[c1]Zum dritten Punkt. [c2]Ein Recht, Ottilies Boden zu nutzen, hat die Gemeinde nicht: keine Einwilligung, keine "
     "Widmung, keine Enteignung. [c3]Ottilie muss das Pflaster also nicht dulden. [c4]Und es liegt noch da, der Zustand "
     "dauert an. [c5]Anders wäre es, wenn er inzwischen legalisiert wäre. [c6]Beim Bundesverwaltungsgericht ging es um einen "
     "Radweg, den eine Gemeinde auf ein Privatgrundstück gebaut hatte. [c7]Als ein Bebauungsplan die Fläche später als "
     "Radweg auswies, sprach für das Gericht vieles gegen die Beseitigung.", PS),
    # --- I II. 3. Möglichkeit und Zumutbarkeit ---------------------------------------------------------------------------
    ("[d1]Zum vierten Punkt: Die Wiederherstellung muss tatsächlich möglich sein. [d2]Im Radweg-Fall war sie es am Ende "
     "nicht mehr: Der Eigentümer hatte den Weg selbst beseitigt. [d3]Rechtlich ist sie ausgeschlossen, wenn der "
     "angestrebte Zustand seinerseits der Rechtsordnung widerspräche. [d4]Und sie muss der Gemeinde zumutbar sein. "
     "[d5]Hier reicht es, die Steine auf dem Streifen herauszunehmen und Erde aufzufüllen: möglich und zumutbar.", PS),
    # --- J III. Rechtsfolge: Status quo ante, kein Schadensersatz; Art. 34 Satz 1 GG ------------------------------------
    ("[rf]Römisch drei: die Rechtsfolge. [rf1]Der Anspruch richtet sich auf die Wiederherstellung des Zustands vor dem "
     "Eingriff, des Status quo ante. [rf2]Er ist kein Schadensersatzanspruch. [rf3]Otti-lie muss sich also nicht mit Geld "
     "abfinden lassen. [w34]Schadensersatz ist etwa Sache der Amtshaftung: Nach Artikel vierunddreißig Satz eins "
     "GG trifft die Verantwortlichkeit grundsätzlich den Staat, [w839]und Paragraf achthundertneununddreißig BGB verlangt "
     "Vorsatz oder Fahrlässigkeit.", PS),
    # --- K Mitverschulden ------------------------------------------------------------------------------------------------
    ("[mv]Eine Grenze noch: das Mitverschulden. [mv1]Hat die Betroffene den Zustand mitverursacht, berücksichtigt das "
     "Bundesverwaltungsgericht das, nach dem Rechtsgedanken von Paragraf zweihundertvierundfünfzig BGB. [mv2]Hätte Ottilie "
     "etwa die Grenzsteine selbst entfernt, sodass niemand die Grenze sehen konnte, käme es darauf an. [mv3]Hier hat sie "
     "nichts dazu beigetragen.", P),
    # --- L Prozessuales --------------------------------------------------------------------------------------------------
    ("[proz]Prozessual ist nach Paragraf vierzig Absatz eins VwGO der Verwaltungsrechtsweg eröffnet, [lk]statthaft ist "
     "die allgemeine Leistungsklage.", PS),
    # --- M Lösung --------------------------------------------------------------------------------------------------------
    ("[loes]Die Lösung: [l1]Die Gemeinde hat hoheitlich in Ottilies Eigentum eingegriffen, [l2]der rechtswidrige Zustand "
     "dauert an, [l3]die Wiederherstellung ist möglich und zumutbar. [l4]Die Gemeinde muss das Pflaster auf dem Streifen "
     "entfernen und den Vorgarten wiederherstellen.", P),
    ("[we2]Gut. Wir nehmen die Steine wieder heraus und bringen Ihren Vorgarten in Ordnung.", PS, "Wernicke"),
    # --- N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Folgenbeseitigungsanspruch nicht wie einen Schadensersatz. [t1]Er verlangt kein "
     "Verschulden und zielt auf Wiederherstellung, nicht auf Geld. [t2]Die Herleitung genügt in einem Satz, weil der Anspruch anerkannt ist.",
     PS),
    # --- O Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Rechtsgrundlage, der Folgenbeseitigungsanspruch. [k2]Römisch zwei: "
     "Voraussetzungen. [k21]Eins: hoheitlicher Eingriff, [k22]zwei: in ein subjektives Recht, [k23]drei: "
     "rechtswidriger Zustand, der andauert, [k24]vier: Wiederherstellung möglich und zumutbar. [k3]Römisch drei: Rechtsfolge, Wiederherstellung des "
     "früheren Zustands, [k31]Mitverschulden nach dem Rechtsgedanken von Paragraf zweihundertvierundfünfzig.", PS),
    # --- P Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Folgenbeseitigungsanspruch stellt den früheren Zustand wieder her. [mk2]Für Schadensersatz "
     "brauchst du eine andere Grundlage, etwa die Amtshaftung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
