"""Folge 198 · Heimtücke § 211: Arglosigkeit, Wehrlosigkeit & Schlafende (Fr · Klausurpraxis · StGB BT, Format Schema).
Fall nach dem Plan-Hook („Ein Mann lockt seinen Geschäftspartner zu einem vermeintlichen Versöhnungsessen und greift ihn
beim Hinsetzen an.“): Heribert (um 60) und Siegmund (um 40) führen zusammen eine kleine Firma und streiten seit Wochen
ums Geld. Heribert beschließt, Siegmund zu töten, und lädt ihn zum Versöhnungsessen ein (Donnerstag, 12.3., 19 Uhr).
Siegmund glaubt an die Versöhnung; als er sich an den Tisch setzt, greift Heribert ihn mit Tötungsvorsatz an; Siegmund
stirbt. Darstellung: kein Angriff, keine Waffe, kein Blut, keine Leiche im Bild – nur Tisch/Essen-Icons und Text.
Aufbau (Schema): Fall → Sachverhalt → Wortlaut § 211 Abs. 1 und Abs. 2 (Auszug) → Definition (BGH) und Prüfschema
a) Arglosigkeit, b) Wehrlosigkeit, c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung → Sonderfälle (Schlafende,
Kleinkinder/schutzbereite Dritte, Besinnungslose) → Lösung → Restriktion (Rechtsfolgenlösung, Verweis 007; Lehre:
verwerflicher Vertrauensbruch) → Klausurtipp (Lexi) → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Auftragsliste und Volltextsuche 04.10.2026): Heribert, Siegmund.
Nie im Genitiv mit -s. Stimmen (Pool niklas, helmut, ela_froh, julia): Heribert helmut (Mann, älter), Siegmund niklas
(Mann, jung); ela_froh und julia nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gerichtsnamen im Sprechtext als Wörter (keine Abkürzungen wie StGB/BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Heribert": "helmut", "Siegmund": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Firma, der Streit, die Einladung ------------------------------------------------------------------
    ("[fall]Heribert und Siegmund führen zusammen eine kleine Firma. [streit]Seit Wochen streiten sie heftig ums Geld. "
     "[plan]Heribert hat genug: Er beschließt, Siegmund zu töten. [lock]Dafür lädt er ihn zu einem Versöhnungsessen ein.", P),
    ("[he1]Lass uns den Streit begraben. Komm am Donnerstag um neunzehn Uhr zu mir zum Essen.", P, "Heribert"),
    ("[le1]Gern. Ich bin froh, dass wir uns wieder vertragen.", P, "Siegmund"),
    # --- A2 Fall: das Versöhnungsessen ----------------------------------------------------------------------------------
    ("[abend]Donnerstag, zwölfter März, neunzehn Uhr. [kommt]Siegmund kommt pünktlich. Er glaubt an die Versöhnung und "
     "rechnet mit einem friedlichen Abend. [setzt]Als er sich an den Tisch setzt, [angriff]greift Heribert ihn mit "
     "Tötungsvorsatz an. [stirbt]Siegmund stirbt. [frage]Ist das Mord? [frage2]Siegmund wusste doch vom Streit. "
     "War er trotzdem arglos?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 211 -------------------------------------------------------------------------------------------------
    ("[p211]Die Antwort steht in Paragraf zweihundertelf. [abs1]Absatz eins: Der Mörder wird mit lebenslanger "
     "Freiheitsstrafe bestraft. [abs2]Nach Absatz zwei ist Mörder unter anderem, wer heimtückisch einen Menschen tötet. "
     "[gruppe]Die Heimtücke gehört zur zweiten Gruppe der Mordmerkmale, zur Art der Tatausführung. [v075]Den Überblick "
     "über alle Gruppen gibt unsere Folge zu den Mordmerkmalen.", PS),
    # --- D Definition und Prüfschema --------------------------------------------------------------------------------------
    ("[def]Was heißt heimtückisch? [def2]Nach ständiger Rechtsprechung des Bundesgerichtshofs handelt heimtückisch, wer in "
     "feindlicher Willensrichtung die Arg- und Wehrlosigkeit des Opfers bewusst zur Tötung ausnutzt. [schema]Daraus folgt "
     "das Prüfschema. [sa]a: die Arglosigkeit. [sb]b: die Wehrlosigkeit, und zwar infolge der Arglosigkeit. [sc]c: das "
     "Ausnutzungsbewusstsein. [sd]Und d: die feindliche Willensrichtung.", PS),
    # --- E a) Arglosigkeit ------------------------------------------------------------------------------------------------
    ("[arg]Zu a. Arglos ist, wer bei Beginn des ersten mit Tötungsvorsatz geführten Angriffs nicht mit einem erheblichen "
     "Angriff gegen seine körperliche Unversehrtheit rechnet. [zeit]Es kommt also genau auf diesen Moment an. [offen]Heimlich "
     "muss der Täter nicht vorgehen: Arglos kann das Opfer auch sein, wenn der Täter ihm offen feindselig entgegentritt, "
     "aber so schnell angreift, dass keine Möglichkeit bleibt, dem Angriff zu begegnen. [angst]Und eine latente Angst aus "
     "früheren Streitigkeiten hebt die Arglosigkeit erst auf, wenn das Opfer deshalb im Tatzeitpunkt mit Feindseligkeiten "
     "rechnet.", PS),
    # --- F b) Wehrlosigkeit -----------------------------------------------------------------------------------------------
    ("[wehr]Zu b. Wehrlos ist, wessen Verteidigungsfähigkeit aufgehoben oder erheblich eingeschränkt ist, [wehr2]etwa weil "
     "das Opfer sich nicht mehr verteidigen, fliehen oder Hilfe holen kann. [folge]Die Wehrlosigkeit muss gerade die Folge "
     "der Arglosigkeit sein.", PS),
    # --- G c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung -----------------------------------------------------
    ("[aus]Zu c. Der Täter muss die Arg- und Wehrlosigkeit erkennen und bewusst ausnutzen: Ihm muss klar sein, dass er "
     "einen ahnungslosen, schutzlosen Menschen überrascht. [blick]Das kann schon mit einem Blick geschehen. [feind]Zu d. "
     "Die feindliche Willensrichtung fehlt nur ganz ausnahmsweise, etwa wenn die Tötung dem ausdrücklichen Willen des "
     "Opfers entspricht.", PS),
    # --- H Sonderfälle ----------------------------------------------------------------------------------------------------
    ("[sf]Jetzt drei Sonderfälle. [schlaf]Erstens: Schlafende. Wer sich zum Schlafen niederlegt, nimmt seine Arglosigkeit "
     "mit in den Schlaf. [schlaf2]Der Schlafende ist deshalb regelmäßig arglos, außer etwa, er wurde gegen seinen "
     "Willen vom Schlaf übermannt.", P),
    ("[kind]Zweitens: Kleinkinder. Ein wenige Monate altes Kind ist noch zu keinerlei Argwohn fähig. Auf seine "
     "Arglosigkeit kommt es deshalb nicht an. [kind2]Heimtückisch kann die Tat aber sein, wenn der Täter die Arg- und "
     "Wehrlosigkeit eines schutzbereiten Dritten ausnutzt, [kind3]etwa der Eltern, die das Kind beschützen oder es nur "
     "deshalb nicht tun, weil sie dem Täter vertrauen. Dafür müssen sie räumlich nah genug sein.", P),
    ("[koma]Drittens: Besinnungslose, etwa im Koma. Anders als Schlafende sind sie zu keinerlei Argwohn fähig. "
     "[koma2]Auch hier kann Heimtücke über schutzbereite Dritte vorliegen, zum Beispiel über das Pflegepersonal.", PS),
    # --- I Lösung ---------------------------------------------------------------------------------------------------------
    ("[loes]Jetzt der Fall. [la]a: War Siegmund arglos? Er wusste vom Streit ums Geld. [la2]Doch ein Streit allein hebt "
     "die Arglosigkeit nicht auf. Entscheidend ist, ob er beim Hinsetzen mit einem erheblichen Angriff rechnete. [la3]Das "
     "tat er nicht, er glaubte an die Versöhnung. Siegmund war arglos. [falle]Hinzu kommt: Heribert hat ihn planmäßig in "
     "diese Lage gelockt. Solche Vorkehrungen können die Heimtücke tragen, wenn sie bis zur Tat fortwirken.", P),
    ("[lb]b: Beim Hinsetzen konnte Siegmund sich weder verteidigen noch fliehen, [lb2]und zwar gerade, weil er keinen "
     "Angriff erwartete. Wehrlos infolge der Arglosigkeit: ja. [lc]c: Heribert hat genau diesen Moment geplant. Er wusste, "
     "dass er einen ahnungslosen Menschen überrascht. [lc2]Ausnutzungsbewusstsein: ja. [ld]d: Siegmund wollte nicht "
     "sterben. Die feindliche Willensrichtung liegt vor.", P),
    ("[erg]Ergebnis: Heribert hat heimtückisch getötet. [erg2]Rechtfertigungs- und Entschuldigungsgründe gibt es nicht. "
     "Er ist strafbar wegen Mordes nach Paragraf zweihundertelf.", PS),
    # --- J Restriktion ----------------------------------------------------------------------------------------------------
    ("[restr]Weil Mord mit lebenslanger Freiheitsstrafe bestraft wird, sucht man nach Wegen, das Merkmal Heimtücke zu begrenzen. "
     "[rfl]Der Bundesgerichtshof hilft bei ganz besonderen schuldmindernden Umständen ausnahmsweise auf der Strafseite, mit "
     "der sogenannten Rechtsfolgenlösung. Mehr dazu in unserer Folge zum Haustyrannen-Fall. [lehre]Ein Teil der Lehre "
     "will schon den Tatbestand einschränken und verlangt einen besonders verwerflichen Vertrauensbruch. [bghn]Der "
     "Bundesgerichtshof verlangt das nicht. [hier]Wer der Lehre folgt, kann hier gut vertreten: Heribert hat das Vertrauen "
     "in die Versöhnung gezielt geweckt und dann missbraucht.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe immer, ob das Opfer arglos war, und zwar bei Beginn des ersten mit Tötungsvorsatz "
     "geführten Angriffs. "
     "[tipp2]Ein Streit davor schließt sie nicht automatisch aus. Frag: Rechnete das Opfer genau in diesem Moment mit "
     "einem erheblichen Angriff? [tipp3]Und diskutiere Einschränkungen der Heimtücke erst, wenn du die Merkmale sauber "
     "festgestellt hast.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Heimtückisch handelt, wer die Arg- und Wehrlosigkeit des Opfers bewusst zur Tötung ausnutzt. [mk2]Maßgeblich ist "
     "der Beginn des Angriffs: [mk3]Der Schlafende bleibt arglos. Wer mit einem Angriff rechnet, ist es nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
