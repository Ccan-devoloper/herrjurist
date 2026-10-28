"""Folge 067 · § 823 I BGB Schema: Radfahrer rammt dich – was musst du beweisen? (Mo · Der Fall · Zivilrecht/Deliktsrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Ein Radfahrer rammt dich auf dem Gehweg – was musst du beweisen, um
Schadensersatz zu bekommen?“): Martina geht auf dem Gehweg an der Bäckerei von Erwin vorbei; Stefan fährt mit dem Fahrrad
zügig über den Gehweg und stößt sie um. Ihr Handgelenk ist verstaucht, ihre Brille zerbrochen (keine Wunden). Stefan
behauptet, sie sei ihm vor das Rad gelaufen; Erwin hat gesehen, dass Stefan viel zu schnell war. Martina verlangt 300 € für
die Brille, die Behandlungskosten und Schmerzensgeld.
Kern: Wortlautkarte § 823 I (vorgelesen), Beweislast als roter Faden (Anspruchsteller: anspruchsbegründende Tatsachen
einschließlich Verschulden; Schädiger: Einwendungen §§ 827, 828), I. Tatbestand (Rechtsgutsverletzung, Verletzungshandlung,
haftungsbegründende Kausalität: Äquivalenz, Adäquanz, Schutzzweck; § 286 ZPO), II. Rechtswidrigkeit (indiziert),
III. Verschulden (§§ 827, 828; § 276 II; § 2 I, V StVO; keine Vermutung wie § 280 I 2), Abwandlung 9-jähriger Radfahrer
(Wortlautkarte § 828 II 1, III; § 829 ein Satz), IV. Schaden und haftungsausfüllende Kausalität (§ 287 ZPO), V. Rechtsfolge
§§ 249 II 1, 253 II, § 254 ein Satz; Klausurtipp, Schema, Merksatz.
Figuren: Martina (julia), Stefan (niklas), Erwin (helmut); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.6

STIMMEN = {"Martina": "julia", "Stefan": "niklas", "Erwin": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Gehweg vor der Bäckerei ---------------------------------------------------------------------------------
    ("[fall]Martina geht auf dem Gehweg an der Bäckerei von Erwin vorbei. [rad]Da kommt Stefan mit dem Fahrrad, zügig "
     "und mitten auf dem Gehweg. [stoss]Er streift sie am Arm, und Martina stürzt. [folge]Ihr Handgelenk ist verstaucht, "
     "ihre Brille zerbrochen.", 0.3),
    ("[mt1]Mein Handgelenk! Und meine Brille ist kaputt!", 0.3, "Martina"),
    ("[st1]Sie sind mir doch vor das Rad gelaufen!", 0.3, "Stefan"),
    ("[er1]Nein, ich habe alles gesehen. Sie waren viel zu schnell!", 0.4, "Erwin"),
    ("[ford]Martina verlangt dreihundert Euro für eine neue Brille, die Behandlungskosten und ein Schmerzensgeld. "
     "[frage]Woraus kann sie das verlangen, [frage2]und was muss sie dafür beweisen?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 823 I (Wortlaut) und Beweislast ----------------------------------------------------------------------------------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertdreiundzwanzig Absatz eins: [w823]Wer vorsätzlich oder fahrlässig "
     "das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht eines anderen "
     "widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden Schadens verpflichtet.", P),
    ("[bew]Und das ist der rote Faden: Grundsätzlich beweist der Anspruchsteller alle Tatsachen, die seinen Anspruch "
     "begründen. [bew2]Einwendungen dagegen muss der Schädiger beweisen.", PS),
    # --- D I. Tatbestand -------------------------------------------------------------------------------------------------------
    ("[tb]Römisch eins: der Tatbestand. [rg]Erstens die Rechtsgutsverletzung. Das verstauchte Handgelenk verletzt Körper "
     "und Gesundheit, [rg2]die zerbrochene Brille das Eigentum. [hd]Zweitens die Verletzungshandlung: Stefan fährt Martina "
     "an, ein aktives Tun.", P),
    ("[ks]Drittens die haftungsbegründende Kausalität zwischen Handlung und Verletzung. [aeq]Äquivalent ist jede Bedingung, "
     "die man nicht hinwegdenken kann, ohne dass die Verletzung entfiele. [adq]Adäquat ist sie, wenn sie nicht nur unter "
     "ganz unwahrscheinlichen Umständen zu einem solchen Erfolg führt. [szw]Und die Verletzung muss aus dem Bereich der "
     "Gefahren stammen, vor denen die Norm schützen soll. [ksub]Ohne den Zusammenstoß kein Sturz, und ein Sturz ist die "
     "typische Folge.", P),
    ("[kbew]Das alles muss Martina voll beweisen: Nach Paragraf zweihundertsechsundachtzig der Zivilprozessordnung braucht "
     "das Gericht die volle Überzeugung. [kzeu]Den Zusammenstoß hat Erwin gesehen.", PS),
    # --- E II. Rechtswidrigkeit ------------------------------------------------------------------------------------------------
    ("[rw]Römisch zwei: die Rechtswidrigkeit. Bei einer unmittelbaren Verletzung ist sie nach herrschender Meinung "
     "indiziert. [rw2]Einen Rechtfertigungsgrund wie Notwehr hat Stefan nicht.", PS),
    # --- F III. Verschulden ----------------------------------------------------------------------------------------------------
    ("[vs]Römisch drei: das Verschulden. [df]Zuerst die Deliktsfähigkeit nach den Paragrafen achthundertsiebenundzwanzig "
     "und achthundertachtundzwanzig. Stefan ist erwachsen und bei klarem Verstand. [dfbew]Diese Ausschlussgründe sind "
     "Einwendungen: Ihre Voraussetzungen muss der Schädiger beweisen.", P),
    ("[fl]Dann Vorsatz oder Fahrlässigkeit. Fahrlässig handelt, wer die im Verkehr erforderliche Sorgfalt außer Acht "
     "lässt, Paragraf zweihundertsechsundsiebzig Absatz zwei. [stvo]Fahrzeuge müssen die Fahrbahn benutzen, Paragraf zwei "
     "Absatz eins der Straßenverkehrsordnung. Den Gehweg erlaubt Absatz fünf grundsätzlich nur Kindern. [fsub]Stefan fuhr "
     "trotzdem dort, und viel zu schnell: fahrlässig.", P),
    ("[vbew]Wichtig: Anders als im Vertrag nach Paragraf zweihundertachtzig Absatz eins Satz zwei wird das Verschulden "
     "hier nicht vermutet. Martina muss es beweisen, [zeuge]und dafür hat sie Erwin als Zeugen.", PS),
    # --- G Abwandlung: neunjähriger Radfahrer, § 828 ------------------------------------------------------------------------------
    ("[abw]Abwandlung: Der Radfahrer ist neun Jahre alt. [abw2]Auf dem Gehweg darf er fahren, muss aber auf Fußgänger "
     "besondere Rücksicht nehmen. [w828]Paragraf achthundertachtundzwanzig Absatz zwei befreit Kinder, die sieben, aber noch "
     "nicht zehn Jahre alt sind, nur bei einem Unfall mit einem Kraftfahrzeug, einer Schienenbahn oder einer Schwebebahn. [kfz]Ein "
     "Fahrrad ist kein Kraftfahrzeug, also greift das Privileg nicht.", P),
    ("[abs3]Bleibt Absatz drei: Nicht verantwortlich ist er nur, wenn ihm die zur Erkenntnis der Verantwortlichkeit "
     "erforderliche Einsicht fehlt. [abs3b]Diese Einsicht wird vermutet; ihr Fehlen muss das Kind beweisen. [alt]Die "
     "Fahrlässigkeit misst man dann an Kindern seines Alters. [p829]Fehlt die Verantwortlichkeit, kann Paragraf "
     "achthundertneunundzwanzig ausnahmsweise eine Haftung aus Billigkeit begründen.", PS),
    # --- H IV. Schaden, haftungsausfüllende Kausalität ---------------------------------------------------------------------------
    ("[sd]Römisch vier: der Schaden und die haftungsausfüllende Kausalität. [sd2]Behandlungskosten und die neue Brille "
     "beruhen auf den Verletzungen. [sdbew]Hier hilft Martina Paragraf zweihundertsiebenundachtzig der "
     "Zivilprozessordnung: Für den Schaden kann eine überwiegende Wahrscheinlichkeit "
     "genügen.", PS),
    # --- I V. Rechtsfolge ----------------------------------------------------------------------------------------------------------
    ("[rf]Römisch fünf: die Rechtsfolge nach den Paragrafen zweihundertneunundvierzig folgende. [rf1]Ist eine Person "
     "verletzt oder eine Sache beschädigt, kann Martina statt der Herstellung den erforderlichen Geldbetrag verlangen: "
     "[rf1b]die Heilbehandlungskosten und dreihundert Euro für die Brille. [rf2]Wegen der Verletzung des Körpers bekommt "
     "sie nach Paragraf zweihundertdreiundfünfzig Absatz zwei auch eine billige Entschädigung in Geld, das Schmerzensgeld.", P),
    ("[mv]Ein Mitverschulden, etwa wenn sie ihm wirklich vor das Rad gelaufen wäre, kann den Anspruch nach Paragraf "
     "zweihundertvierundfünfzig kürzen; beweisen müsste es Stefan. [erg]Ergebnis: Glaubt das Gericht Erwin, zahlt Stefan die Brille, die Behandlungskosten "
     "und ein Schmerzensgeld.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne die beiden Kausalitäten. [tipp1]Die haftungsbegründende verbindet Handlung und "
     "Rechtsgutsverletzung; auf sie muss sich das Verschulden beziehen. [tipp2]Die haftungsausfüllende verbindet die "
     "Verletzung mit dem Schaden; dafür braucht es kein Verschulden.", PS),
    # --- K Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins, Tatbestand: Rechtsgutsverletzung, Verletzungshandlung, haftungsbegründende "
     "Kausalität. [k2]Römisch zwei: Rechtswidrigkeit. [k3]Römisch drei: Verschulden, mit der Deliktsfähigkeit nach den "
     "Paragrafen achthundertsiebenundzwanzig und achthundertachtundzwanzig.", P),
    ("[k4]Römisch vier: Schaden und haftungsausfüllende Kausalität. [k5]Römisch fünf: Rechtsfolge nach den Paragrafen "
     "zweihundertneunundvierzig folgende.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer aus Paragraf achthundertdreiundzwanzig Absatz eins Schadensersatz will, beweist grundsätzlich alle "
     "anspruchsbegründenden Tatsachen, auch das Verschulden. [m2]Die Ausschlussgründe der Paragrafen achthundertsiebenundzwanzig und "
     "achthundertachtundzwanzig muss der Schädiger beweisen.", 1.4),
]
