"""Jauchegrubenfall (BGHSt 14, 193): zweiaktiges Geschehen, Irrtum über den Kausalverlauf. [marke] = Bildelement ab diesem Wort.
Segmente: (text, pause) = Erzähler, (text, pause, rolle) = Figurenrede."""

P, PS = 0.4, 0.9

STIMMEN = {"Frank": "qvgnHZ5ufqbaFzs9RP51",    # Christian – Warm and Melodic
           "Gisela": "pMrwpTuGOma7Nubxs5jo"}   # Lea – Warm and Supportive

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------------------------------
    ("[fall]Frank und Gisela sind Nachbarn. [streit]Eines Abends streiten sie am Gartenzaun.", 0.3),
    ("[g1]Dein Zaun steht auf meinem Grundstück! Morgen reiße ich ihn ab.", 0.3, "Gisela"),
    ("[f1]Das wagst du nicht!", 0.4, "Frank"),
    ("[wuergen]Frank gerät in Wut und will Gisela töten. Er würgt sie, bis sie reglos zusammensackt. "
     "[tot]Frank hält sie für tot. [lebt]Tatsächlich ist sie nur bewusstlos.", 0.3),
    ("[f2]Sie atmet nicht mehr. Ich muss sie verschwinden lassen.", 0.4, "Frank"),
    ("[grube]Um die vermeintliche Leiche zu beseitigen, wirft Frank Gisela in eine Jauchegrube. [ertrinkt]Dort ertrinkt sie.", P),
    ("[frage]Hat sich Frank wegen vollendeten Totschlags strafbar gemacht?", 0.6),
    # --- Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- Objektiver Tatbestand ---------------------------------------------------------------------------------------
    ("[schema]Wir prüfen Totschlag, Paragraf zweihundertzwölf StGB. [erfolg]Gisela ist tot, der Erfolg ist eingetreten. "
     "[kaus]Das Würgen war auch kausal: Ohne das Würgen hätte Frank sie nicht in die Grube geworfen.", P),
    ("[zurech]Der Tod ist Frank auch objektiv zurechenbar. Dass ein Täter die vermeintliche Leiche beseitigt, "
     "liegt nicht außerhalb aller Lebenserfahrung.", PS),
    # --- Subjektiver Tatbestand: das Problem ----------------------------------------------------------------------------
    ("[vorsatz]Das Problem liegt im Vorsatz. [akt1]Beim Würgen wollte Frank töten, aber daran ist Gisela nicht gestorben. "
     "[akt2]Beim Versenken hatte er keinen Tötungsvorsatz mehr, denn er hielt sie schon für tot.", P),
    ("[frage2]Wie ist dieses zweiaktige Geschehen zu bewerten?", PS),
    # --- Ansichten ---------------------------------------------------------------------------------------------------------
    ("[dg]Die frühere Lehre vom dolus generalis nahm einen Gesamtvorsatz für beide Akte an. "
     "[dg2]Das wird heute abgelehnt, denn der Vorsatz muss bei der Tathandlung vorliegen.", P),
    ("[tr]Die Trennungstheorie betrachtet beide Akte getrennt. [tr2]Dann bleibt ein versuchter Totschlag durch das Würgen "
     "und eine fahrlässige Tötung durch das Versenken.", P),
    ("[rspr]Der BGH und die herrschende Lehre sehen darin einen Irrtum über den Kausalverlauf. "
     "[rspr2]Er ist unbeachtlich, wenn sich die Abweichung im Rahmen des nach allgemeiner Lebenserfahrung Voraussehbaren hält "
     "und keine andere Bewertung der Tat rechtfertigt. [rspr3]So ist es hier: vollendeter Totschlag.", P),
    ("[roxin]Roxin stellt darauf ab, ob sich der Tatplan verwirklicht hat. [roxin2]Handelt der Täter beim ersten Akt mit Tötungsabsicht, "
     "liegt Vollendung vor. Frank wollte Gisela töten, also auch danach: vollendeter Totschlag.", PS),
    # --- Ergebnis ------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Frank hat sich wegen vollendeten Totschlags strafbar gemacht. [mord]Mordmerkmale sind nicht ersichtlich.", P),
    ("[tipp]Klausurtipp: Das Problem gehört in den subjektiven Tatbestand, zum Vorsatz bezüglich des Kausalverlaufs. "
     "[tipp2]Die Kausalität selbst ist unproblematisch.", PS),
    # --- Schema ---------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Objektiver Tatbestand: Erfolg, Kausalität, objektive Zurechnung. "
     "[k2]Subjektiver Tatbestand: Vorsatz, auch bezüglich des Kausalverlaufs. [k3]Dort den Streit darstellen. "
     "[k4]Dann Rechtswidrigkeit und Schuld.", PS),
    # --- Merksatz ---------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Jauchegrubenfall ist die Abweichung vom vorgestellten Kausalverlauf unwesentlich. "
     "[m2]Der Täter ist wegen vollendeter Tat strafbar.", 1.4),
]
