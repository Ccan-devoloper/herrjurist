"""Folge 027 · Besitz und Eigentum: Der Unterschied einfach erklärt (§§ 854 ff. BGB) – Klausurpraxis, Format Abgrenzung.
Frei erfundener Fall (Plan-Hook „Dein Mitbewohner hat dein Fahrrad im Keller“): Anke leiht ihrem Mitbewohner Jürgen ihr
Fahrrad bis Ende September; er schließt es in sein Kellerabteil. Tagsüber jobbt Jürgen im Fahrradladen von Frau Kunze
(Besitzdiener, § 855). Ein Unbekannter bricht das Kellerabteil auf und schiebt das Rad davon; Jürgen verfolgt ihn und
nimmt es ihm wieder ab (§§ 858, 859 II). Gegenfall: Anke nimmt das Rad im Juli eigenmächtig zurück (§§ 858, 861, 863;
§ 985 scheitert an § 986). Ausblick §§ 929 S. 1, 930, 931. Wortlautkarten: § 854 I, § 868, § 855 BGB.
Fiktive Figuren: Anke (Eigentümerin), Jürgen (Mitbewohner, Entleiher, Ladenangestellter), Frau Kunze (Ladeninhaberin),
ein Unbekannter (Dieb, ohne Text). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Anke": "laura_klar", "Juergen": "marc", "Kunze": "lisa"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das geliehene Rad -----------------------------------------------------------------------------------
    ("[fall]Anke und Jürgen wohnen in einer WG. [leiht]Im Juni leiht Anke ihm ihr Fahrrad, bis Ende September.", 0.3),
    ("[a1]Bis September kannst du es haben. Aber pass gut darauf auf!", 0.3, "Anke"),
    ("[j1]Versprochen. Ich schließe es in mein Kellerabteil.", 0.4, "Juergen"),
    # --- B Fall: im Fahrradladen -------------------------------------------------------------------------------------
    ("[laden]Tagsüber jobbt Jürgen im Fahrradladen von Frau Kunze.", 0.3),
    ("[ku1]Jürgen, stell bitte die neuen Räder ins Schaufenster.", 0.4, "Kunze"),
    # --- C Fall: der Dieb ---------------------------------------------------------------------------------------------
    ("[dieb]An einem Abend bricht ein Unbekannter das Kellerabteil auf und schiebt das Rad davon. "
     "[hinter]Jürgen sieht ihn und rennt hinterher.", 0.3),
    ("[j2]Halt! Das Rad bleibt hier!", 0.3, "Juergen"),
    ("[zurueck]An der nächsten Ecke nimmt er dem Mann das Rad wieder ab. "
     "[frage]Wem gehört das Rad, wer besitzt es? Und durfte Jürgen es sich einfach zurückholen?", 0.6),
    # --- D Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Eigentum ---------------------------------------------------------------------------------------------------
    ("[eig]Zuerst die Begriffe. Eigentum ist die rechtliche Herrschaft über eine Sache. [p903]Nach Paragraf "
     "neunhundertdrei darf die Eigentümerin mit der Sache nach Belieben verfahren und andere von jeder Einwirkung "
     "ausschließen. [anke]Eigentümerin ist hier Anke, und zwar die ganze Zeit.", P),
    # --- F Besitz, § 854 I ----------------------------------------------------------------------------------------------
    ("[besitz]Besitz ist dagegen die tatsächliche Herrschaft. [p854]Paragraf achthundertvierundfünfzig Absatz eins: "
     "Der Besitz einer Sache wird durch die Erlangung der tatsächlichen Gewalt über die Sache erworben. "
     "[wille]Dazu kommt nach herrschender Meinung ein Besitzwille. [verkehr]Wer die Gewalt hat, bestimmt nach dem "
     "Bundesgerichtshof die Verkehrsanschauung. [jb]Jürgen hat das Rad in seinem abgeschlossenen Kellerabteil. "
     "Er ist unmittelbarer Besitzer.", PS),
    # --- G mittelbarer Besitz, § 868; Eigen- und Fremdbesitz, § 872 ------------------------------------------------------
    ("[mittel]Und Anke? Sie hat das Rad nicht in der Hand und ist trotzdem Besitzerin. [p868]Paragraf "
     "achthundertachtundsechzig: Besitzt jemand eine Sache als Mieter, Verwahrer oder in einem ähnlichen Verhältnis, "
     "[zeit]vermöge dessen er auf Zeit zum Besitz berechtigt ist, dann ist auch der andere Besitzer. "
     "[leihe]Die Leihe bis September ist so ein Besitzmittlungsverhältnis. Danach muss Jürgen das Rad zurückgeben. "
     "[mb]Anke ist also mittelbare Besitzerin.", P),
    ("[p872]Noch eine Unterscheidung: Anke besitzt das Rad als ihr gehörend. Sie ist Eigenbesitzerin, Paragraf "
     "achthundertzweiundsiebzig. [fremd]Jürgen besitzt es für Anke, er ist Fremdbesitzer.", PS),
    # --- H Besitzdiener, § 855; Erbenbesitz, § 857 ------------------------------------------------------------------------
    ("[diener]Anders im Laden. [p855]Paragraf achthundertfünfundfünfzig: Übt jemand die tatsächliche Gewalt für einen "
     "anderen in dessen Erwerbsgeschäft aus und muss er dessen Weisungen folgen, ist nur der andere Besitzer. "
     "[kunze]Jürgen schiebt die Räder für Frau Kunze und tut, was sie sagt. Er ist nur Besitzdiener, Besitzerin ist "
     "Frau Kunze. [bgh855]So sieht es auch der Bundesgerichtshof: Arbeitnehmer sind für die Sachen, die ihnen zur Arbeit "
     "überlassen werden, grundsätzlich Besitzdiener.", P),
    ("[kontrast]Zwischen Mitbewohnern gibt es kein solches Weisungsverhältnis. Das geliehene Rad besitzt Jürgen selbst. "
     "[p857]Und ein Sonderfall: Stirbt ein Besitzer, geht sein Besitz nach Paragraf achthundertsiebenundfünfzig auf die "
     "Erben über, auch ohne tatsächliche Gewalt.", PS),
    # --- I verbotene Eigenmacht, § 858; Selbsthilfe, § 859 ----------------------------------------------------------------
    ("[eigenm]Jetzt zum Dieb. [p858]Er hat Jürgen den Besitz ohne dessen Willen entzogen. Das ist verbotene "
     "Eigenmacht, Paragraf achthundertachtundfünfzig. [unm]Sie trifft Jürgen, denn verbotene Eigenmacht gibt es nur "
     "gegen den unmittelbaren Besitzer. [fehler]Der Dieb hat jetzt zwar Besitz, aber fehlerhaften Besitz. Eigentum "
     "erwirbt er nicht.", P),
    ("[p859]Durfte Jürgen das Rad zurückholen? Ja. Nach Paragraf achthundertneunundfünfzig Absatz zwei darf der "
     "Besitzer dem verfolgten Täter die weggenommene Sache wieder abnehmen. [frisch]Jürgen ist dem Mann auf frischer Tat "
     "gefolgt. [erg]Ergebnis: Anke bleibt Eigentümerin, und Jürgen durfte sich seinen Besitz zurückholen.", PS),
    # --- J Gegenfall: Anke holt sich das Rad ----------------------------------------------------------------------------
    ("[gegen]Gegenfall: Im Juli will Anke ihr Rad früher zurück. [nimmt]Als Jürgen es kurz vor dem Haus abstellt, nimmt "
     "sie es ohne zu fragen und bringt es in die Garage ihrer Eltern.", 0.3),
    ("[j3]Das Rad ist bis September geliehen! Ich will es zurück.", 0.3, "Juergen"),
    ("[a2]Es ist aber mein Rad!", 0.4, "Anke"),
    ("[p861]Trotzdem hat Anke verbotene Eigenmacht begangen: Sie hat Jürgen den Besitz ohne seinen Willen entzogen, und "
     "kein Gesetz erlaubt ihr das. [anspr]Jürgen kann nach Paragraf achthunderteinundsechzig die Wiedereinräumung des "
     "Besitzes verlangen. [p863]Und das Eigentum von Anke? Es hilft ihr hier nicht. Ein Recht zum Besitz zählt nach "
     "Paragraf achthundertdreiundsechzig nur für die Frage, ob verbotene Eigenmacht vorliegt. [posses]Dieser Anspruch "
     "ist possessorisch: Er schützt den Besitz als solchen.", P),
    ("[p985]Und könnte Anke das Rad dann gleich nach Paragraf neunhundertfünfundachtzig herausverlangen? Dieser "
     "petitorische Anspruch schützt das Eigentum. [p986]Doch Jürgen hat aus der Leihe bis September ein Recht zum Besitz, "
     "Paragraf neunhundertsechsundachtzig.", PS),
    # --- K Ausblick: Übereignung --------------------------------------------------------------------------------------
    ("[ausblick]Ein Ausblick: Der Besitz entscheidet auch bei der Übereignung. [p929]Paragraf neunhundertneunundzwanzig "
     "Satz eins verlangt die Übergabe, also einen Besitzwechsel. [p930]Behält der Veräußerer die Sache, genügt nach "
     "Paragraf neunhundertdreißig, dass der Erwerber mittelbaren Besitz bekommt. [p931]Und will Anke ihr Rad übereignen, "
     "während Jürgen es hat, tritt sie ihren Herausgabeanspruch ab, Paragraf neunhunderteinunddreißig.", PS),
    # --- L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme den Besitz für jede Person einzeln: unmittelbar oder mittelbar, Besitzdiener, Eigen- "
     "oder Fremdbesitz. [tipp2]Und prüfe bei Paragraf achthunderteinundsechzig nicht, wem die Sache gehört. Der Satz, "
     "Anke ist doch Eigentümerin, gehört dort nicht hin.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Jürgen gegen Anke aus Paragraf achthunderteinundsechzig Absatz eins. [k1]Römisch eins: "
     "Jürgen war Besitzer. [k2]Römisch zwei: Besitz durch verbotene Eigenmacht entzogen. [k3]Römisch drei: Anke besitzt "
     "ihm gegenüber fehlerhaft. [k4]Römisch vier: kein Ausschluss nach Paragraf achthunderteinundsechzig Absatz zwei und "
     "kein Erlöschen nach Paragraf achthundertvierundsechzig. [k5]Römisch fünf: Einwendungen nur nach Paragraf "
     "achthundertdreiundsechzig. [k6]Ergebnis: Anke muss Jürgen den Besitz wieder einräumen.", PS),
    # --- N Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Eigentum ist das rechtliche Haben, Besitz das tatsächliche. [m2]Der Besitz wird für sich geschützt, "
     "sogar gegen die Eigentümerin.", 1.4),
]
