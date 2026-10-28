"""Folge 044 · Verwaltungsakt § 35 VwVfG: Alle Merkmale in sechs Minuten (Mi · Examenswissen · Verwaltungsrecht AT).
Beispielfall (Übungsfall, Hook laut Themenplan „Ein Brief vom Amt, eine Durchsage der Polizei, ein Verkehrsschild“):
Frau Wiegand verkauft Kaffee aus einem Wagen auf dem Marktplatz. Herr Lorenz (Ordnungsamt) übergibt ihr die Ablehnung
ihres Antrags auf einen festen Standplatz; Polizist Göbel warnt per Megafon vor einem Unwetter und ordnet danach die
Räumung des Marktplatzes an; am Montag steht vor ihrer Ladezone ein neues Haltverbotsschild; Amtsleiterin Kessler setzt
Herrn Lorenz ins Bürgerbüro um. Merkmale des § 35 Satz 1 VwVfG mit Mini-Fällen und Abgrenzungen (öffentlich-rechtlicher
Vertrag § 54 VwVfG, Gericht, Kündigung der Garage nach BGB, Hinweis, Auskunft, Realakt, Rechtsnorm, innerdienstliche
Weisung, Organisationsakt), Allgemeinverfügung § 35 Satz 2 in drei Formen, Verkehrszeichen (BVerwG 3 C 37.09),
Bedeutung: Anfechtungs-/Verpflichtungsklage § 42 I VwGO, Frist, Vollstreckung.
Wortlautkarten: § 35 Satz 1 VwVfG (vorgelesen), § 35 Satz 2 VwVfG (Merkmale).
Fiktive Figuren: Frau Wiegand (hilde), Herr Lorenz (christian), Polizist Göbel (niklas), Amtsleiterin Kessler (julia).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Wiegand": "hilde", "Lorenz": "christian", "Goebel": "niklas", "Kessler": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Samstag auf dem Marktplatz, der Bescheid -------------------------------------------------------------
    ("[fall]Samstag auf dem Marktplatz. Frau Wiegand verkauft dort Kaffee aus ihrem kleinen Wagen. "
     "[lorenz]Da kommt Herr Lorenz vom Ordnungsamt mit einem Brief.", 0.2),
    ("[lo1]Frau Wiegand, Ihr Antrag auf einen festen Standplatz ist abgelehnt. Hier ist der Bescheid.", 0.3, "Lorenz"),
    ("[wi1]Abgelehnt? Ich stehe hier seit zwanzig Jahren!", 0.3, "Wiegand"),
    # --- B Fall: Mittags, die Durchsagen ------------------------------------------------------------------------------
    ("[mittag]Mittags frischt der Wind auf. [goebel]Polizist Göbel spricht durchs Megafon.", 0.2),
    ("[go1]Achtung! Heute Nachmittag zieht ein Unwetter auf.", 0.4, "Goebel"),
    ("[donner]Kurz darauf donnert es.", 0.2),
    ("[go2]Das Unwetter ist da. Alle verlassen sofort den Marktplatz!", 0.4, "Goebel"),
    # --- C Fall: Montag, das Schild -------------------------------------------------------------------------------------
    ("[montag]Am Montag steht vor ihrer Ladezone ein neues Schild: Haltverbot.", 0.2),
    ("[wi2]Und wo soll ich jetzt ausladen?", 0.3, "Wiegand"),
    # --- D Die Frage --------------------------------------------------------------------------------------------------
    ("[frage]Ein Brief vom Amt, zwei Durchsagen der Polizei, ein Verkehrsschild. Was davon ist ein Verwaltungsakt? "
     "[frage2]Die Antwort steckt in sechs Merkmalen. Und sie entscheidet, wie sich Frau Wiegand wehren kann.", 0.6),
    # --- E Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Wortlaut § 35 Satz 1 -----------------------------------------------------------------------------------------
    ("[wl35]Paragraf fünfunddreißig Satz eins Verwaltungsverfahrensgesetz: Verwaltungsakt ist jede Verfügung, "
     "Entscheidung oder andere hoheitliche Maßnahme, die eine Behörde zur Regelung eines Einzelfalls auf dem Gebiet des "
     "öffentlichen Rechts trifft und die auf unmittelbare Rechtswirkung nach außen gerichtet ist. [sechs]Daraus folgen "
     "sechs Merkmale. [land]Die Länder haben eigene Verfahrensgesetze, meist mit gleichem Wortlaut.", P),
    # --- G 1. hoheitliche Maßnahme ------------------------------------------------------------------------------------
    ("[m1]Erstens: eine Verfügung, Entscheidung oder andere hoheitliche Maßnahme. [einseitig]Hoheitlich heißt: Die Behörde "
     "entscheidet einseitig, der Bürger muss nicht zustimmen. [vertrag]Schließt die Stadt mit Frau Wiegand einen Vertrag, "
     "Paragraf vierundfünfzig, fehlt die Einseitigkeit.", P),
    # --- H 2. Behörde ---------------------------------------------------------------------------------------------------
    ("[beh0]Zweitens: eine Behörde. Nach Paragraf eins Absatz vier ist das jede Stelle, die Aufgaben der öffentlichen "
     "Verwaltung wahrnimmt. [beh]Das Ordnungsamt und die Polizei tun das. [gericht]Ein Gericht dagegen spricht Recht. Sein "
     "Urteil ist kein Verwaltungsakt.", P),
    # --- I 3. öffentliches Recht ----------------------------------------------------------------------------------------
    ("[m3]Drittens: auf dem Gebiet des öffentlichen Rechts. Die Behörde nutzt eine Befugnis, die Privatleuten nicht "
     "zusteht, hier die Erlaubnis für den Standplatz. [garage]Kündigt die Stadt ihr dagegen die gemietete Garage, handelt sie "
     "wie jeder Vermieter, nach dem Bürgerlichen Gesetzbuch. Das ist Privatrecht.", P),
    # --- J 4. Regelung ----------------------------------------------------------------------------------------------------
    ("[m4]Viertens: eine Regelung. Die Behörde will eine verbindliche Rechtsfolge setzen, also Rechte begründen, ändern, "
     "aufheben, verbindlich feststellen oder verneinen. [abl]Die Ablehnung verneint den Standplatz verbindlich. Das ist "
     "eine Regelung.", P),
    ("[hinw]Die erste Durchsage nicht: Sie warnt nur und setzt keine Rechtsfolge. [ausk]Ebenso eine Auskunft am "
     "Telefon: Ihr Antrag hat wohl wenig Chancen. [real]Räumt der Bauhof umgewehte Schirme weg, ist das ein Realakt, "
     "tatsächliches Handeln ohne Rechtsfolge. [gebot]Die zweite Durchsage aber gebietet: Alle verlassen den Platz. Regelung.", P),
    # --- K 5. Einzelfall ------------------------------------------------------------------------------------------------
    ("[m5]Fünftens: ein Einzelfall. Klassisch: eine bestimmte Person, ein konkreter Fall, wie der Antrag von Frau Wiegand. "
     "[norm]Regelt die Stadt dagegen unbestimmt viele gleichartige Fälle, etwa per Satzung für alle künftigen Märkte, ist "
     "das eine Rechtsnorm.", P),
    ("[wl352]Dazwischen steht die Allgemeinverfügung, Satz zwei. [av1]Sie richtet sich an einen nach allgemeinen Merkmalen "
     "bestimmbaren Personenkreis, [av1b]wie die zweite Durchsage: ein Anlass, ein Ort, alle, die gerade dort sind. "
     "[av2]Oder sie betrifft die öffentlich-rechtliche Eigenschaft einer Sache, etwa die Widmung einer Straße. [av3]Oder die "
     "Benutzung einer Sache durch die Allgemeinheit, etwa ein Verbot auf einem bestimmten Gelände, das für jeden gilt.", P),
    ("[vz]Und Verkehrszeichen? Das Bundesverwaltungsgericht behandelt Verkehrsverbote und Verkehrsgebote in ständiger "
     "Rechtsprechung als Allgemeinverfügungen. [halt]Also auch das Haltverbot vor der Ladezone.", PS),
    # --- L 6. Außenwirkung ------------------------------------------------------------------------------------------------
    ("[m6]Sechstens: unmittelbare Rechtswirkung nach außen. Die Regelung muss jemanden außerhalb der Verwaltung treffen. "
     "[rathaus]Im Rathaus sagt Amtsleiterin Kessler zu Herrn Lorenz:", 0.2),
    ("[ke1]Herr Lorenz, ab Montag arbeiten Sie im Bürgerbüro.", 0.3, "Kessler"),
    ("[umsetz]Das ist eine Umsetzung, eine innerdienstliche Weisung. Sie berührt seine persönliche Rechtsstellung "
     "grundsätzlich nicht, also kein Verwaltungsakt. [org]Ebenso ein Organisationsakt, etwa wenn die Stadt zwei Ämter "
     "zusammenlegt. [aussen]Der Bescheid an Frau Wiegand dagegen wirkt "
     "nach außen.", P),
    # --- M Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Der Bescheid ist ein Verwaltungsakt. [erg2]Die zweite Durchsage und das Schild sind "
     "Allgemeinverfügungen, also auch Verwaltungsakte. [erg3]Nur die Warnung ist keiner.", PS),
    # --- N Bedeutung: Klageart, Frist, Vollstreckung ---------------------------------------------------------------------
    ("[warum]Warum das zählt: [anf]Gegen einen belastenden Verwaltungsakt wie das Haltverbot ist die Anfechtungsklage statthaft. "
     "[verpfl]Will Frau Wiegand den abgelehnten Standplatz, ist es die Verpflichtungsklage, Paragraf zweiundvierzig Absatz "
     "eins Verwaltungsgerichtsordnung. [unst]Gegen die bloße Warnung wäre sie unstatthaft.", P),
    ("[frist]Außerdem laufen Fristen, meist ein Monat. Beim Schild ohne Belehrung gilt ein Jahr, erst ab "
     "dem Moment, in dem Frau Wiegand ihm zum ersten Mal gegenübersteht. [vollstr]Und gebietet ein Verwaltungsakt etwas, kann "
     "die Behörde ihn selbst mit Verwaltungszwang durchsetzen, ohne erst zu klagen.", PS),
    # --- O Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Den Verwaltungsakt prüfst du meist bei der statthaften Klageart. [tipp1]Unproblematisches "
     "stellst du kurz fest. Argumentiere, wo es hakt, meist bei Regelung oder Außenwirkung. [tipp2]Und lies ein Schreiben "
     "wie ein objektiver Empfänger. Unklarheiten gehen zulasten der Behörde.", PS),
    # --- P Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q0]Verwaltungsakt, Paragraf fünfunddreißig Satz eins: [q1]Eins, hoheitliche Maßnahme. "
     "[q2]Zwei, Behörde. [q3]Drei, auf dem Gebiet des öffentlichen Rechts. [q4]Vier, Regelung. [q5]Fünf, Einzelfall, auch "
     "als Allgemeinverfügung nach Satz zwei. [q6]Sechs, unmittelbare Außenwirkung. [q7]Folge: Anfechtungs- oder "
     "Verpflichtungsklage.", PS),
    # --- Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Verwaltungsakt regelt verbindlich einen Einzelfall mit Wirkung nach außen. [m2]Wer nur warnt, "
     "informiert oder intern anweist, erlässt keinen.", 1.4),
]
