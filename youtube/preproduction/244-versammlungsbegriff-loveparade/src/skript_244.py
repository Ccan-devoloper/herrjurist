"""Folge 244 · Versammlungsbegriff: Ist die Love Parade eine Demo? (Art. 8 GG) (Mo · Der Fall · Grundrechte · Klassiker-Fall).
Übungsfall nach dem Hook des Themenplans („Ein Techno-Umzug mit politischem Motto will als Versammlung gelten, damit die Stadt
die Reinigungskosten trägt“), Beispielland Nordrhein-Westfalen (wie Folgen 233/234), fiktiver „Sound-Umzug“ ohne echte
Marken oder Veranstalter: Herr Brendel plant zwanzig Musikwagen mit Techno, Motto „Mehr Raum für Kultur“, ohne Reden,
Flugblätter oder Transparente. Herr Zander von der Stadt: keine Versammlung, Erlaubnis nötig, Reinigung rund 38.000 €.
Aufbau: Frage → Sachverhalt → 1. Wortlaut Art. 8 I GG (Wortlautkarte) → 2. Versammlungsbegriff (weit, erweitert, eng;
BVerfGE 104, 92 Rn. 39; Love-Parade-Beschluss 1 BvQ 28/01 Rn. 16, 18, 20; § 2 Abs. 3 VersG NRW) → 3. gemischte
Veranstaltungen (Rn. 22, 25 wörtlich; BVerwG 6 C 23.06 Rn. 16–18, drei Schritte; Love Parade Rn. 19, 26; Gegenveranstaltung
6 C 23.06 Rn. 20–25) → 4. Fall (keine Versammlung) und Folgen (Sondernutzung, §§ 18, 21 StrWG NRW; Rn. 9; § 11 VersG NRW)
→ 5. Gegenfall (Frau Lechner, Musik als Mittel) → Klausurtipp, Schema, Merksatz mit Lexi.
Stimmen (Pool niklas, helmut, ela_froh, julia): Herr Brendel niklas (Mann, jung), Herr Zander helmut (Mann, älter),
Frau Lechner ela_froh (Frau, jung; heitere Rolle, ein Satz); julia nicht gebraucht. Erzählerin und Lexi: Carla ohne Rolle.
Namen nie im Genitiv mit -s. Belege je Cue: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Brendel": "niklas", "Zander": "helmut", "Lechner": "ela_froh"}

SEGMENTE = [
    # --- A Fall: der Sound-Umzug ----------------------------------------------------------------------------------------
    ("[fall]Frühjahr in einer Stadt in Nordrhein-Westfalen. [brendel]Herr Brendel plant für den Sommer einen Sound-Umzug "
     "durch die Innenstadt: [wagen]zwanzig Musikwagen, Techno, tausende Tanzende. [motto]Er will ihn als Versammlung "
     "durchführen, Motto: Mehr Raum für Kultur. Reden, Flugblätter oder Transparente sind nicht geplant. [zander]Herr "
     "Zander von der Stadt antwortet:", 0.2),
    ("[za1]Das ist keine Versammlung, sondern eine Party. Sie brauchen eine Erlaubnis und zahlen die Reinigung: rund "
     "achtunddreißigtausend Euro.", P, "Zander"),
    ("[br1]Wir haben doch ein Motto! Als Demo zahlt die Stadt.", P, "Brendel"),
    ("[frage]Ist der Sound-Umzug eine Versammlung im Sinne von Artikel acht Grundgesetz? [frage2]Genau darum stritten die "
     "Berliner Polizei und die Veranstalterin der Love Parade. Das Bundesverfassungsgericht äußerte sich im Juli zweitausendeins, im Eilverfahren.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Wortlaut ------------------------------------------------------------------------------------------------------
    ("[art8]Erstens, der Wortlaut. Artikel acht Absatz eins Grundgesetz: [wl8]Alle Deutschen haben das Recht, sich ohne "
     "Anmeldung oder Erlaubnis friedlich und ohne Waffen zu versammeln. [nichtdef]Was eine Versammlung ist, sagt der Artikel "
     "nicht.", P),
    # --- D 2. Versammlungsbegriff ---------------------------------------------------------------------------------------------
    ("[begriff]Zweitens, der Versammlungsbegriff. Drei Ansichten werden vertreten. [weit]Nach dem weiten Begriff genügt "
     "jeder gemeinsame Zweck, auch gemeinsames Tanzen. In diese Richtung argumentierte die Veranstalterin der "
     "Love Parade. [erweit]Der erweiterte Begriff "
     "verlangt gemeinsame Meinungsbildung oder Meinungsäußerung, gleich zu welchem Thema. [eng]Das Bundesverfassungsgericht "
     "vertritt den engen Begriff: [def]Versammlungen sind örtliche Zusammenkünfte mehrerer Personen zur gemeinschaftlichen, "
     "auf die Teilhabe an der öffentlichen Meinungsbildung gerichteten Erörterung oder Kundgebung.", P),
    ("[grund]Der Grund: Artikel acht schützt besonders stark, weil die Versammlungsfreiheit der öffentlichen "
     "Meinungsbildung dient. Ein beliebiger gemeinsamer Zweck reicht dafür nicht. [nrw]In Nordrhein-Westfalen steht der "
     "Begriff sogar im Gesetz, mit mindestens drei Personen und dem Wort: überwiegend. [party]Volksfeste und Massenpartys "
     "fallen nicht darunter, auch nicht die bloße Zurschaustellung eines Lebensgefühls. [mittel]Aber Musik und Tanz können "
     "das Mittel sein: Wer damit auf die öffentliche Meinung einwirken will, ist geschützt.", P),
    # --- E 3. Gemischte Veranstaltungen -------------------------------------------------------------------------------------
    ("[gemischt]Drittens, gemischte Veranstaltungen. Eine Party wird nicht schon dadurch zur Versammlung, dass bei ihrer "
     "Gelegenheit auch Meinungen kundgetan werden. [gepraege]Entscheidend ist das Gesamtgepräge: Steht die Meinungsbildung "
     "im Vordergrund oder der Spaß? [zweifel]Und das Bundesverfassungsgericht sagt wörtlich: Bleiben Zweifel, so bewirkt "
     "der hohe Rang der Versammlungsfreiheit, dass die Veranstaltung wie eine Versammlung behandelt wird.", P),
    ("[schritte]Das Bundesverwaltungsgericht prüft das in drei Schritten. [sa]Erstens: Welche Elemente zielen auf die "
     "Meinungsbildung? Nur vorgeschobene Anliegen bleiben außen vor, und dabei ist Zurückhaltung geboten. [sb]Zweitens: "
     "Welches Gewicht haben Musik, Tanz und Unterhaltung? [sc]Drittens: Was überwiegt aus Sicht eines durchschnittlichen "
     "Betrachters? Lässt sich das nicht zweifelsfrei feststellen, ist die Veranstaltung wie eine Versammlung zu behandeln.",
     P),
    ("[lp]Bei der Love Parade hielt das Bundesverfassungsgericht es für tragfähig, sie nicht als Versammlung einzuordnen. "
     "[gv]Eine Gegenveranstaltung desselben Sommers, ebenfalls ein Techno-Umzug, hatte dagegen Spruchbänder, Flugblätter "
     "und eine Podiumsdiskussion. [gv2]Sie war nach dem Bundesverwaltungsgericht wie eine Versammlung zu behandeln.", P),
    # --- F 4. Der Fall: Sound-Umzug ----------------------------------------------------------------------------------------
    ("[subs]Viertens, zurück zu Herrn Brendel. [sub1]Viele Menschen kommen an einem Ort zusammen, das passt. [sub2]Aber "
     "was prägt den Umzug? Zwanzig Musikwagen, Techno, Tanzen. Für die Meinungsbildung steht nur das Motto auf dem Papier: "
     "keine Reden, keine Flugblätter, keine Transparente. [sub3]Und Herr Brendel sagt selbst, worum es geht: Die Stadt soll "
     "zahlen. Das Motto ist vorgeschoben, der Spaß steht klar im Vordergrund. [erg]Ergebnis: Der Sound-Umzug ist keine "
     "Versammlung.", P),
    ("[folge]Was heißt das für die Kosten? [sonder]Der Umzug ist eine Sondernutzung der Straße, und die braucht eine "
     "Erlaubnis. So kam es auch bei der Love Parade. [kost]Die Stadt kann die Erlaubnis mit Auflagen verbinden und sich "
     "zusätzliche Kosten ersetzen lassen, also auch die Reinigung. [versfrei]Eine Versammlung bräuchte dagegen keine "
     "Erlaubnis für die Straße. [land]Die Normen sind Landesrecht, hier Nordrhein-Westfalen. In deinem Land können sie "
     "anders heißen.", PS),
    # --- G 5. Gegenfall -----------------------------------------------------------------------------------------------------
    ("[gegen]Fünftens, der Gegenfall. [lechner]Frau Lechner organisiert einen Umzug gegen die Schließung des "
     "Jugendzentrums. Auch hier fahren Musikwagen. [reden]Aber es gibt Reden, Transparente und Flugblätter mit konkreten "
     "Forderungen.", 0.2),
    ("[le1]Mit Musik hören uns viel mehr Leute zu!", P, "Lechner"),
    ("[gegen2]Die Musik ist hier das Mittel, um den Forderungen Gehör zu verschaffen. Das Gesamtgepräge ist die "
     "Meinungskundgabe. [gegen3]Der Umzug ist eine Versammlung, geschützt durch Artikel acht.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Versammlungsbegriff im Schutzbereich, und zwar ausführlich, wenn Musik im Spiel ist. "
     "[tipp2]Erfasse die Elemente einzeln, gewichte sie und vergleiche. [tipp3]Und schreibe nicht einfach, das Motto sei "
     "vorgeschoben. Dafür brauchst du Anhaltspunkte im Sachverhalt.", PS),
    # --- I Schema (Lexi) ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [k1]Erstens, der Schutzbereich: eine Versammlung. Örtliche Zusammenkunft mehrerer Personen, "
     "[k1b]mit dem Zweck der Teilhabe an der öffentlichen Meinungsbildung. [k1c]Bei gemischten Veranstaltungen zählt das "
     "Gesamtgepräge, im Zweifel Versammlung. [k2]Dann friedlich und ohne Waffen. [k3]Zweitens, der Eingriff. [k4]Drittens, "
     "die Rechtfertigung.", PS),
    # --- J Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Musik darf das Mittel sein, aber nicht der ganze Zweck. [m2]Es zählt das Gesamtgepräge, und im Zweifel "
     "gilt die Veranstaltung als Versammlung.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), "Marke doppelt"
