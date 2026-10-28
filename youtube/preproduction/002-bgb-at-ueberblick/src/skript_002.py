"""Folge 002 · BGB AT Überblick: Vom Vertragsschluss bis zur Anfechtung (Examenswissen, Format Schema).
Beispielfall (frei erfunden): Opa Karl bevollmächtigt seine 17-jährige Enkelin Emma, ein gebrauchtes E-Bike zu kaufen; Verkäufer
Jens verspricht sich beim Preis (570 statt 750 Euro) und ficht an. Prüfungsweg: Anspruch entstanden (Einigung, Stellvertretung mit
§ 165, Wirksamkeitshindernisse) → untergegangen (Anfechtung) → durchsetzbar. Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Karl": "johann", "Emma": "lucy", "Jens": "stephan"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Wohnzimmer ----------------------------------------------------------------------------------------
    ("[fall]Opa Karl ist zweiundsiebzig und wünscht sich ein E-Bike. [anzeige]Im Internet findet er eine Anzeige: "
     "gebrauchtes E-Bike, gut erhalten, Preis auf Anfrage. [auftrag]Er bittet seine siebzehnjährige Enkelin Emma, sich darum zu kümmern.", 0.3),
    ("[k1]Schau es dir an, Emma. Wenn es gut ist, kauf es in meinem Namen. Bis achthundert Euro.", 0.5, "Karl"),
    # --- B Fall: in der Garage des Verkäufers -----------------------------------------------------------------------
    ("[garage]Emma fährt zum Verkäufer Jens. Sie sagt gleich, dass sie im Namen ihres Großvaters kauft, "
     "[probe]und macht eine Probefahrt. [preis]Dann nennt Jens den Preis.", 0.3),
    ("[j1]Für fünfhundertsiebzig Euro gehört es Ihrem Opa.", 0.4, "Jens"),
    ("[dreher]Gemeint hatte er siebenhundertfünfzig. Er hat sich versprochen, ohne es zu merken.", 0.3),
    ("[e1]Abgemacht! Ich kaufe es im Namen von Opa Karl.", 0.6, "Emma"),
    # --- C Fall: der Anruf am Abend ---------------------------------------------------------------------------------
    ("[abend]Am Abend fällt Jens der Zahlendreher auf. Er ruft sofort bei Karl an.", 0.3),
    ("[j2]Ich habe mich versprochen. Gemeint waren siebenhundertfünfzig Euro. Ich fechte den Kauf an.", 0.4, "Jens"),
    ("[k2]Gekauft ist gekauft! Ich will das Rad für fünfhundertsiebzig Euro.", 0.6, "Karl"),
    ("[frage]Hat Karl recht? An diesem Fall gehen wir den ganzen Prüfungsweg des Allgemeinen Teils ab.", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Anspruchsgrundlage und Aufbau ----------------------------------------------------------------------------
    ("[agl]Karl verlangt Übergabe und Übereignung des Rads, Anspruchsgrundlage ist Paragraf "
     "vierhundertdreiunddreißig Absatz eins. [drei]Geprüft wird in drei Schritten: Ist der Anspruch entstanden? "
     "[drei2]Ist er untergegangen? [drei3]Und ist er durchsetzbar?", PS),
    # --- F I. Entstanden: Einigung -----------------------------------------------------------------------------------
    ("[vs]Entstanden ist der Anspruch, wenn ein Kaufvertrag geschlossen wurde, also durch Angebot und Annahme. "
     "[inv]Die Anzeige im Internet ist noch kein Angebot. Ihr fehlt der Rechtsbindungswille. Sie lädt nur dazu ein, "
     "selbst Angebote abzugeben.", P),
    ("[ang]Das Angebot macht Jens: fünfhundertsiebzig Euro, gerichtet an Karl, entgegengenommen von Emma. "
     "[ausl]Maßgeblich ist, wie Emma die Erklärung verstehen durfte, Paragrafen hundertdreiunddreißig und hundertsiebenundfünfzig. "
     "Was Jens im Kopf hatte, zählt hier noch nicht. [ann]Emma nimmt sofort an. Einigung über fünfhundertsiebzig Euro.", PS),
    # --- G Stellvertretung ------------------------------------------------------------------------------------------
    ("[st]Aber Emma ist nicht Karl. Für ihn wirkt ihre Erklärung nur über Stellvertretung, Paragraf hundertvierundsechzig. "
     "[st1]Erstens gibt Emma eine eigene Willenserklärung ab. Sie entscheidet selbst, ob sie kauft, ist also keine bloße Botin. "
     "[st2]Zweitens handelt sie im Namen von Karl, und das sagt sie offen. "
     "[st3]Drittens hat sie Vertretungsmacht: Karl hat ihr Vollmacht erteilt, bis achthundert Euro.", P),
    ("[gf]Und dass Emma erst siebzehn ist? Sie ist beschränkt geschäftsfähig, Paragraf hundertsechs. "
     "[gf2]Das schadet nach Paragraf hundertfünfundsechzig nicht. Die Folgen des Kaufs treffen ja nicht sie, sondern Karl.", P),
    ("[gegen]Anders bei neunhundert Euro: Dann fehlte die Vertretungsmacht, und der Vertrag hinge von Karls Genehmigung ab, "
     "Paragraf hundertsiebenundsiebzig. [gegen2]Emma selbst haftete als Minderjährige nicht, außer ihre Eltern hätten zugestimmt, "
     "Paragraf hundertneunundsiebzig Absatz drei.", PS),
    # --- H Wirksamkeitshindernisse ---------------------------------------------------------------------------------
    ("[wh]Bleiben die Wirksamkeitshindernisse. Karl und Jens sind voll geschäftsfähig. [form]Eine Form schreibt das Gesetz "
     "für den Kauf eines Rads nicht vor. [wh_erg]Der Kaufvertrag ist wirksam, der Anspruch entstanden.", PS),
    # --- I II. Untergegangen: Anfechtung ---------------------------------------------------------------------------
    ("[unter]Zweiter Schritt: Ist der Anspruch untergegangen? Jens hat angefochten. Dann ist der Vertrag als "
     "von Anfang an nichtig anzusehen, Paragraf hundertzweiundvierzig Absatz eins. "
     "[ae]Die Anfechtungserklärung hat Jens gegenüber Karl abgegeben, seinem Vertragspartner, Paragraf hundertdreiundvierzig.", P),
    ("[grund]Der Anfechtungsgrund ist ein Erklärungsirrtum, Paragraf hundertneunzehn Absatz eins, zweite Alternative. "
     "Jens wollte siebenhundertfünfzig sagen und hat sich versprochen. [kaus]Hätte er das gewusst, hätte er so nicht erklärt.", P),
    ("[frist]Die Frist wahrt er: Er rief noch am selben Abend an, also unverzüglich, Paragraf hunderteinundzwanzig.", P),
    ("[ue_erg]Der Kaufvertrag ist damit nichtig, der Anspruch untergegangen. [vt]Karl kann allenfalls seinen "
     "Vertrauensschaden ersetzt verlangen, Paragraf hundertzweiundzwanzig.", PS),
    # --- J III. Durchsetzbar, Ergebnis -----------------------------------------------------------------------------
    ("[durch]Im dritten Schritt ginge es um Einreden wie die Verjährung, Paragraf zweihundertvierzehn. "
     "Darauf kommt es nicht mehr an. [erg]Ergebnis: Karl kann das Rad nicht für fünfhundertsiebzig Euro verlangen.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Anfechtung erst beim Untergang des Anspruchs. Bis zur Anfechtung ist der Vertrag wirksam. "
     "[tipp2]Und beim Irrtum kommt es auf den an, der die Erklärung abgegeben hat. Hätte sich Emma versprochen, "
     "zählte ihr Irrtum, Paragraf hundertsechsundsechzig Absatz eins.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1a]Römisch eins: Anspruch entstanden. Erstens die Einigung durch Angebot und Annahme. "
     "[s1b]Zweitens, wenn ein Vertreter handelt: eigene Erklärung, im fremden Namen, mit Vertretungsmacht. "
     "[s1c]Drittens keine Wirksamkeitshindernisse, etwa bei Geschäftsfähigkeit oder Form.", P),
    ("[s2]Römisch zwei: Anspruch untergegangen, etwa durch Anfechtung: Erklärung, Grund, Frist. "
     "[s3]Römisch drei: Anspruch durchsetzbar, also keine Einrede wie die Verjährung.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Auch ein wirksam geschlossener Vertrag kann durch Anfechtung rückwirkend entfallen. "
     "[m2]Darum prüfst du immer in drei Schritten: entstanden, untergegangen, durchsetzbar.", 1.4),
]
