"""Gekreuzte Mordmerkmale (§§ 211, 212, 26, 28 StGB). [marke] = Bildelement ab diesem Wort."""

P, PS = 0.4, 0.9

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------------------------
    ("[fall]Tante Tilde ist reich. [b]Ihr Neffe Ben hofft auf das Erbe. [gier]Er will endlich an ihr Geld.", P),
    ("[a]Bens Freund Alex hat ein ganz anderes Problem. [betrug]Er hat Tilde um viel Geld betrogen, "
     "[entdeckt]und sie ist ihm auf die Schliche gekommen.", P),
    ("[ueberredet]Alex redet auf Ben ein, Tilde zu töten. [ben]Ben denkt an das Erbe. "
     "[alex]Alex denkt daran, dass sein Betrug nie herauskommen darf.", P),
    ("[tat]Ben tötet Tilde.", P),
    ("[frage]Wie haben sich Ben und Alex strafbar gemacht?", 0.6),
    # --- Sachverhalt zum Nachlesen ---------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- Ben ----------------------------------------------------------------------------------------------
    ("[schema]Beginne mit dem Tatnächsten, also mit Ben. [ben212]Er tötet Tilde vorsätzlich, Totschlag nach Paragraf "
     "zweihundertzwölf ist erfüllt.", P),
    ("[habgier]Dazu kommt ein Mordmerkmal: Habgier. Ben tötet, um an das Erbe zu kommen. "
     "[benerg]Ben ist wegen Mordes strafbar, Paragraf zweihundertelf.", PS),
    # --- Alex: Einstieg ------------------------------------------------------------------------------------------
    ("[alexsch]Nun zu Alex. Er hat Ben zur Tat bestimmt. [anst]In Betracht kommt Anstiftung zum Mord.", P),
    ("[haupt]Die vorsätzliche, rechtswidrige Haupttat ist Bens Mord aus Habgier. [kennt]Und Alex weiß, dass Ben aus Habgier handelt.", P),
    ("[problem]Aber Alex selbst ist nicht habgierig. [verd]Er handelt, um seinen Betrug zu verdecken. "
     "Das ist ebenfalls ein Mordmerkmal: Verdeckungsabsicht.", PS),
    # --- Begriff -----------------------------------------------------------------------------------------------------
    ("[begriff]Genau das nennt man gekreuzte Mordmerkmale. [kreuz]Täter und Teilnehmer haben jeweils ein täterbezogenes "
     "Mordmerkmal, aber verschiedene.", P),
    ("[gruppen]Täterbezogen sind die Merkmale der ersten und der dritten Gruppe, etwa Habgier und Verdeckungsabsicht. "
     "[28]Sie sind besondere persönliche Merkmale im Sinne von Paragraf achtundzwanzig.", PS),
    # --- Streit ------------------------------------------------------------------------------------------------------
    ("[streit]Welcher Absatz von Paragraf achtundzwanzig gilt, hängt vom Verhältnis zwischen Mord und Totschlag ab.", P),
    ("[rspr]Die Rechtsprechung sieht im Mord einen eigenständigen Tatbestand. [rspr28]Täterbezogene Mordmerkmale "
     "begründen danach die Strafe. Es gilt Paragraf achtundzwanzig Absatz eins.", P),
    ("[rspr1]Alex ist wegen Anstiftung zum Mord strafbar, denn er kennt Bens Habgier. "
     "[rspr2]Eine Strafmilderung scheidet aus, weil er selbst ein gleichartiges täterbezogenes Mordmerkmal verwirklicht.", PS),
    ("[lit]Die Literatur sieht im Mord eine Qualifikation des Totschlags. [lit28]Täterbezogene Mordmerkmale schärfen die Strafe. "
     "Es gilt Paragraf achtundzwanzig Absatz zwei.", P),
    ("[lit1]Jeder Beteiligte wird nach seinen eigenen Merkmalen bestraft. [lit2]Alex hat mit der Verdeckungsabsicht ein "
     "eigenes Mordmerkmal. Auch danach: Anstiftung zum Mord.", PS),
    # --- Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Beide Ansichten kommen also zum selben Ergebnis. [offen]Der Streit kann offenbleiben.", P),
    ("[tipp]Klausurtipp: Entscheiden musst du ihn erst, wenn dem Teilnehmer ein eigenes Mordmerkmal fehlt. "
     "[tipp2]Dann bekommt er nach der Rechtsprechung Anstiftung zum Mord mit Milderung, "
     "[tipp3]nach der Literatur nur Anstiftung zum Totschlag.", PS),
    # --- Schema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Erstens: Strafbarkeit des Täters, Mord aus Habgier.", P),
    ("[s2]Zweitens: Anstiftung zum Mord. Haupttat und Vorsatz des Anstifters. "
     "[s3]Dann Paragraf achtundzwanzig: Streit um Absatz eins oder zwei, [s4]gekreuzte Mordmerkmale, Ergebnis gleich.", PS),
    # --- Merksatz ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei gekreuzten Mordmerkmalen ist der Teilnehmer nach beiden Ansichten wegen Anstiftung zum Mord strafbar, "
     "[m2]ohne Milderung. Den Streit kannst du offenlassen.", 1.4),
]
