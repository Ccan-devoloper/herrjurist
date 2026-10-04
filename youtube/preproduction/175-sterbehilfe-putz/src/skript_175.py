"""Folge 175 · Sterbehilfe: aktiv, passiv, indirekt – Behandlungsabbruch (Fall Putz) (Mo · Der Fall · Klassiker-Fall;
§§ 212, 216, 13 StGB; § 1827 BGB). Echter Fall sachlich nach dem Volltext: BGH, Urt. v. 25.6.2010 – 2 StR 454/09,
BGHSt 55, 191 (HRRS 2010 Nr. 704), zitiert nur mit Leitsatz/Rn. Belege je Cue: ../RECHTSSTAND.md.
HÖCHSTE SENSIBILITÄT: keine Figur für die Mutter, die Tochter, den Bruder oder den Anwalt (nur „der Anwalt“, Fallname
„Fall Putz“); die Handlung nur als Text-Pille; kein Pflegebett, keine Sonde, kein Schlauch, keine Schere im Bild;
keine Bewertung der Beteiligten. Fiktiver Rahmen: Strafrecht-Seminar mit Thilo (Student, Stimme niklas) und
Professor Wedekind (Seminarleiter, Stimme helmut). Hilfsangebot (Telefonseelsorge) am Ende.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Thilo": "niklas", "Wedekind": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Einstieg im Seminar (fiktiv), Hook ----------------------------------------------------------------------------
    ("[fall]Strafrecht-Seminar. [hook]Professor Wedekind schildert einen echten Fall: Eine Frau liegt im Wachkoma und wird "
     "künstlich ernährt. [hook2]Früher hatte sie gesagt, das wolle sie nicht. [hook3]Auf Rat eines Anwalts durchtrennt ihre "
     "Tochter den Schlauch der Ernährungssonde.", P),
    ("[wd1]Ist das strafbar?", P, "Wedekind"),
    ("[th1]Das ist doch aktive Sterbehilfe. Die ist immer strafbar.", P, "Thilo"),
    ("[klassiker]So sah es lange die herrschende Meinung. Der Bundesgerichtshof hat im Fall Putz anders entschieden.", PS),
    # --- B 1. Die frühere Einteilung (Lehrbegriffe; BGHSt 55, 191 Rn. 27, 34) ------------------------------------------------
    ("[begr]Erstens, die frühere Einteilung der Lehre. [aktiv]Aktive Sterbehilfe: Jemand führt den Tod gezielt herbei, "
     "stets verboten. [passiv]Passive Sterbehilfe: Lebenserhaltende Maßnahmen werden unterlassen oder nicht "
     "fortgesetzt, unter Voraussetzungen erlaubt. [indirekt]Indirekte Sterbehilfe: Eine ärztlich gebotene "
     "Leidenslinderung nimmt einen früheren Tod als mögliche Nebenfolge in Kauf, ebenfalls erlaubt. [grenze]Die Grenze "
     "lief also zwischen Tun und Unterlassen.", PS),
    # --- C 2. Der echte Fall (Rn. 1, 3–10) ------------------------------------------------------------------------------------
    ("[echt]Zweitens, der echte Fall nach dem Urteil. [koma]Die Mutter lag seit zweitausendzwei nach einer "
     "Hirnblutung im Wachkoma, in einem Altenheim, und wurde über eine Sonde künstlich ernährt. Eine Besserung war nicht "
     "mehr zu erwarten. [wille]Kurz vorher hatte sie ihrer Tochter gesagt: Wenn sie sich nicht mehr äußern könne, "
     "wolle sie keine künstliche Ernährung. Aufgeschrieben hatte sie das nicht. [betreuer]Später wurden die Tochter und ihr "
     "Bruder zu Betreuern bestellt, der Hausarzt unterstützte sie.", P),
    ("[heim]Nach einem Kompromiss mit der Heimleitung stellte die Tochter die Ernährung ein. [anord]Am nächsten Tag ordnete "
     "die Geschäftsleitung an, sie wieder aufzunehmen. [rat]Der Anwalt riet am Telefon, den Schlauch der Sonde zu "
     "durchtrennen. Die Tochter tat es, unterstützt von ihrem Bruder. [klinik]Das Personal bemerkte es, die Mutter wurde im "
     "Krankenhaus wieder ernährt und starb gut zwei Wochen später eines natürlichen Todes.", P),
    ("[lg]Das Landgericht Fulda verurteilte den Anwalt wegen versuchten Totschlags zu neun Monaten auf Bewährung. "
     "[tochter]Die Tochter sprach es frei, wegen eines unvermeidbaren Erlaubnisirrtums nach dem "
     "Rechtsrat. [frage]War das Durchtrennen gerechtfertigt?", PS),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E 3. Kern: Behandlungsabbruch (Leitsätze 1–3; Rn. 19–22, 27–37, 39) ----------------------------------------------
    ("[kern]Drittens, der Kern. [einw]Rechtfertigen kann hier nur der Wille der Patientin, also ihre Einwilligung. "
     "[alt]Nach der alten Einteilung war das Durchtrennen aktives Tun und damit verboten. [aufg]Daran hält der "
     "BGH nicht fest.", P),
    ("[ls1]Erster Leitsatz: Sterbehilfe durch Unterlassen, Begrenzen oder Beenden einer begonnenen medizinischen Behandlung, "
     "der Behandlungsabbruch, ist gerechtfertigt, wenn dies dem tatsächlichen oder mutmaßlichen Patientenwillen entspricht "
     "[lauf]und dazu dient, einem ohne Behandlung zum Tode führenden Krankheitsprozess seinen Lauf zu lassen. [ls2]Zweiter "
     "Leitsatz: Ein Behandlungsabbruch kann sowohl durch Unterlassen als auch durch aktives Tun vorgenommen werden. "
     "[normativ]Ob jemand die Ernährung nur einstellt oder den Schlauch durchtrennt, entscheidet also nicht. Der "
     "Behandlungsabbruch ist ein normativ-wertender Oberbegriff.", P),
    ("[vor]Voraussetzung ist, dass die Person lebensbedrohlich erkrankt ist und die Maßnahme medizinisch geeignet ist, "
     "das Leben zu erhalten oder zu verlängern. [bezug]Das Handeln muss objektiv und subjektiv unmittelbar auf diese Behandlung bezogen sein. "
     "[wer]Handeln dürfen Arzt, Betreuer oder Bevollmächtigter, und die Hilfspersonen, die sie hinzuziehen.", P),
    ("[ls3]Die Grenze zieht der dritte Leitsatz: Gezielte Eingriffe in das Leben eines Menschen, die nicht in einem "
     "Zusammenhang mit dem Abbruch einer medizinischen Behandlung stehen, sind einer Rechtfertigung durch Einwilligung nicht "
     "zugänglich. [p216]Sie bleiben strafbar, auf Verlangen nach Paragraf zweihundertsechzehn, siehe Folge hundertachtundzwanzig. "
     "[indir2]Erfasst bleibt die indirekte Sterbehilfe.", PS),
    # --- F 4. Patientenwille im Betreuungsrecht (§ 1827 BGB; damals § 1901a BGB a. F., Rn. 16, 17, 24, 38) -------------------
    ("[pv]Viertens, der Patientenwille im Betreuungsrecht. Der BGH stützte sich auf Paragraf neunzehnhunderteins a BGB, "
     "heute gilt Paragraf achtzehnhundertsiebenundzwanzig. [pv1]Absatz eins regelt die Patientenverfügung: Ein "
     "einwilligungsfähiger Volljähriger legt schriftlich fest, ob er in bestimmte ärztliche Maßnahmen einwilligt oder sie "
     "untersagt. [pv2]Fehlt sie, zählen nach Absatz zwei die Behandlungswünsche oder der mutmaßliche Wille, etwa aus "
     "früheren Äußerungen. [pv3]Nach Absatz drei gilt das unabhängig von Art und Stadium der Erkrankung. [streng]Für den "
     "Willen gelten strenge Beweismaßstäbe. [hier]Hier stand der früher mündlich geäußerte Wille der Mutter zweifelsfrei "
     "fest.", PS),
    # --- G 5. Ergebnis (Rn. 31, 41; Tenor) ------------------------------------------------------------------------------------
    ("[erg]Fünftens, das Ergebnis. Das Durchtrennen sollte verhindern, dass eine nicht mehr gewollte Behandlung wieder "
     "aufgenommen wird. [erg2]Es war ein gerechtfertigter Behandlungsabbruch. [erg3]Der Anwalt handelte als hinzugezogener "
     "Berater ebenso wenig rechtswidrig wie die Betreuer selbst. [tenor]Der BGH hob das Urteil des Landgerichts auf und "
     "sprach ihn frei.", PS),
    # --- H Zurück im Seminar -----------------------------------------------------------------------------------------------
    ("[th2]Also kommt es nicht darauf an, ob man aktiv handelt?", P, "Thilo"),
    ("[wd2]Nein. Entscheidend sind der Bezug zur Behandlung und der Wille der Patientin.", PS, "Wedekind"),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe im Tatbestand Paragraf zweihundertzwölf, hier versucht und durch aktives Tun. [tipp2]Den "
     "Behandlungsabbruch prüfst du erst in der Rechtswidrigkeit, als Rechtfertigung durch Einwilligung nach dem "
     "Patientenwillen. [tipp3]Fehlt der Bezug zur Behandlung, scheidet die Rechtfertigung aus.", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Eins, Tatbestand: Tötung eines anderen Menschen, durch Tun oder Unterlassen, und "
     "Vorsatz. [s2]Zwei, Rechtswidrigkeit: Rechtfertigung durch Behandlungsabbruch. [s2a]Erstens, lebensbedrohliche "
     "Erkrankung und lebenserhaltende Behandlung. [s2b]Zweitens, Unterlassen, Begrenzen oder Beenden dieser Behandlung, mit "
     "unmittelbarem Behandlungsbezug. [s2c]Drittens, tatsächlicher oder mutmaßlicher Patientenwille, streng festgestellt. "
     "[s2d]Viertens, Handeln durch Arzt, Betreuer, Bevollmächtigten oder ihre Hilfspersonen. [s3]Drei, Schuld.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nicht Tun oder Unterlassen entscheidet, sondern der Bezug zur Behandlung. [m2]Ein Behandlungsabbruch "
     "nach dem Patientenwillen ist gerechtfertigt, ein gezielter Eingriff ohne Behandlungsbezug nicht.", 1.0),
    # --- L Hilfsangebot ----------------------------------------------------------------------------------------------------
    ("[hilfe]Wenn dich das Thema belastet: Die Telefonseelsorge ist rund um die Uhr und kostenlos für dich da. "
     "[nummern]Die Nummern siehst du hier.", 4.5),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
