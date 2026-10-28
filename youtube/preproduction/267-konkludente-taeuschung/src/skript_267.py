"""Folge 267 · Konkludente Täuschung beim Betrug: Lügen ohne falsches Wort (Fr · Klausurpraxis · StGB BT · Abgrenzung).
Voraussetzung Folge 065 (Betrugsschema, nur verwiesen); Tankfall (Folge 022) nur als Parallele der Rechtsprechung genannt.
Plan-Hook: Gast bestellt ein Drei-Gänge-Menü, obwohl er weiß, dass er nicht zahlen kann – ein Unternehmen verschickt
Angebote, die wie Rechnungen aussehen. Fall 1: Baldur bestellt im Restaurant, Kellnerin Kaja serviert, Rechnung 48 €.
Fall 2: Ortrud (Privatperson) hat eine Geburtstagsanzeige in der Tageszeitung aufgegeben; Herr Weinert schickt ihr ein
rechnungsähnliches Angebotsschreiben (Registernummer, 89,60 €, fett „zahlbar binnen 10 Tagen“, ausgefüllter
Überweisungsträger, Angebotshinweis nur im Kleingedruckten); sie zahlt, der Interneteintrag ist für sie wertlos.
Ablauf: Fall 1 → Fall 2 → Frage → Sachverhalt → § 263 Abs. 1 (Wortlautkarte) → drei Wege der Täuschung → Maßstab
(Verkehrsanschauung) → Fall 1 (Bestellung = Zahlungsfähigkeit und -willigkeit; Abgrenzung: Entschluss erst nach dem Essen)
→ Fall 2 (BGHSt 47, 1: planmäßig erweckter Eindruck einer Zahlungspflicht, direkter Vorsatz, Kleingedrucktes) →
Abgrenzung Tun/Unterlassen (Garantenpflicht) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, nicht vergeben, in namen_reserviert.txt eingetragen): Baldur, Kaja, Ortrud, Weinert.
Stimmen nur aus dem Pool: Baldur stephan, Kaja lucy, Ortrud hilde, Weinert christian (stephan und christian nie in
derselben Szene). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Baldur": "stephan", "Kaja": "lucy", "Ortrud": "hilde", "Weinert": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall 1: im Restaurant -----------------------------------------------------------------------------------
    ("[fall]Freitagabend in einem Restaurant in der Altstadt. [baldur]Baldur setzt sich an einen Tisch am Fenster. "
     "[leer]Er hat kein Geld dabei, sein Konto ist leer, und das weiß er. [kaja]Kellnerin Kaja kommt an den Tisch.", P),
    ("[b1]Einmal das Drei-Gänge-Menü, bitte.", P, "Baldur"),
    ("[k1]Sehr gern, kommt sofort.", P, "Kaja"),
    ("[essen]Suppe, Hauptgang, Nachtisch: Baldur isst alles auf. [rech]Dann bringt Kaja die Rechnung über "
     "achtundvierzig Euro.", P),
    ("[b2]Tut mir leid, ich kann nicht bezahlen.", 0.4, "Baldur"),
    # --- B Fall 2: der Brief --------------------------------------------------------------------------------------
    ("[ortrud]Szenenwechsel. Ortrud hat in der Tageszeitung eine Anzeige zum achtzigsten Geburtstag ihrer Schwester "
     "aufgegeben. [brief]Drei Tage später liegt ein Brief im Kasten. [rmerk]Oben eine Registernummer, in der Mitte ein "
     "Betrag von neunundachtzig Euro sechzig, fett gedruckt: zahlbar binnen zehn Tagen. [ueber]Dazu ein ausgefüllter "
     "Überweisungsträger.", P),
    ("[o1]Ach, die Rechnung für meine Anzeige. Die zahle ich gleich.", 0.4, "Ortrud"),
    ("[klein]Ganz unten steht klein gedruckt: Dies ist ein Angebot für einen Eintrag in einem Internetportal. "
     "[weinert]Abgeschickt hat das Schreiben Herr Weinert. Er setzt darauf, dass kaum jemand das Kleingedruckte liest.", P),
    ("[w1]Im Kleingedruckten steht doch alles. Ich habe kein falsches Wort geschrieben.", 0.4, "Weinert"),
    ("[frage]Baldur hat nicht gelogen, Weinert auch nicht. [frage2]Haben beide trotzdem getäuscht?", 0.6),
    # --- C Sachverhalt --------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Wortlaut und drei Wege der Täuschung ---------------------------------------------------------------------
    ("[p263]Betrug, Paragraf zweihundertdreiundsechzig. [tats]Am Anfang steht die Täuschung: Der Täter spiegelt falsche "
     "Tatsachen vor oder entstellt oder unterdrückt wahre. [verw]Irrtum, Vermögensverfügung und Schaden kennst du aus "
     "dem Betrugsschema; hier geht es nur um die Täuschung.", PS),
    ("[drei]Täuschen kann man auf drei Wegen. [ausdr]Ausdrücklich, mit einer bewusst unwahren Behauptung. "
     "[konkl]Konkludent, durch ein Verhalten, das nach der Verkehrsanschauung eine stillschweigende Erklärung enthält. "
     "[unterl]Und durch Unterlassen, wenn jemand einen Irrtum nicht aufklärt, obwohl er dazu verpflichtet ist.", PS),
    ("[mass]Der Maßstab für die konkludente Täuschung: Was erklärt das Verhalten nach der Verkehrsanschauung mit? "
     "[mass2]Das ergibt sich aus der konkreten Situation, dem Geschäftstyp und den Erwartungen der Beteiligten.", PS),
    # --- E Fall 1: Bestellung im Restaurant -------------------------------------------------------------------------
    ("[f1]Fall eins: Baldur im Restaurant. [f1a]Ausdrücklich hat er nichts Falsches gesagt, er hat nur bestellt. "
     "[f1b]Wer aber im Restaurant bestellt, erklärt damit schlüssig: Ich kann und will nach dem Essen bezahlen. "
     "[f1c]Ähnlich hat der Bundesgerichtshof beim Tanken und bei Hotelgästen entschieden.", P),
    ("[f1d]Baldur weiß, dass er nicht zahlen kann. Seine Erklärung ist also falsch: [f1e]eine konkludente Täuschung. "
     "[f1f]Kaja glaubt ihm und serviert das Menü; Irrtum, Verfügung und Schaden folgen daraus. [f1g]Weil Baldur "
     "vorsätzlich und in Bereicherungsabsicht handelt, ist er wegen Betrugs strafbar.", P),
    ("[zech]Anders, wenn Baldur erst nach dem Essen beschließt, nicht zu zahlen, und sich heimlich davonschleicht. "
     "[zech2]Bei der Bestellung war seine Erklärung noch wahr, und das heimliche Weggehen erklärt niemandem etwas. "
     "[zech3]Ein Betrug scheidet dann aus.", PS),
    # --- F Fall 2: rechnungsähnliches Angebot (BGHSt 47, 1) ---------------------------------------------------------
    ("[f2]Fall zwei: das Schreiben von Weinert. [f2a]Jeder Satz darin ist wahr, sogar der Hinweis auf das Angebot. "
     "[f2b]Trotzdem kann auch ein inhaltlich wahres Schreiben täuschen. [bgh]Das hat der Bundesgerichtshof "
     "zweitausendeins entschieden, für Angebotsschreiben, die wie Rechnungen aussahen.", P),
    ("[rm]Typische Rechnungsmerkmale wie Registernummer, Betrag, fett gedruckte Zahlungsfrist und ausgefüllter "
     "Überweisungsträger prägen den Gesamteindruck. [zpfl]Das Schreiben erklärt damit schlüssig: Du musst zahlen. "
     "[hint]Der kleine Hinweis auf das Angebot tritt dahinter völlig zurück.", P),
    ("[plan]Entscheidend ist, dass der Täter diese Wirkung planmäßig einsetzt. [zweck]Der Irrtum ist nicht bloße Folge, "
     "sondern Zweck des Schreibens. [dv]Dafür verlangt der Bundesgerichtshof direkten Vorsatz; bedingter Vorsatz genügt "
     "nicht.", P),
    ("[klein2]Und das Kleingedruckte? [klein3]Dass man das Angebot bei genauem Hinsehen erkennen konnte, beseitigt die "
     "Täuschung nicht. [sorg]Zwar schützt der Betrug nicht vor jeder Sorglosigkeit. [sorg2]Wer aber gezielt darauf "
     "setzt, dass sein Hinweis überlesen wird, täuscht trotzdem.", P),
    ("[kauf]Bei geschäftserfahrenen Kaufleuten hatte ein anderer Senat das früher zurückhaltender gesehen; Ortrud ist "
     "aber Privatperson. [f2e]Sie zahlt im Irrtum, und der Eintrag ist für sie wertlos. [f2f]Weinert wollte genau das "
     "und sich bereichern: Er ist wegen Betrugs strafbar.", PS),
    # --- G Abgrenzung: Tun oder Unterlassen -------------------------------------------------------------------------
    ("[tun]Bleibt die Abgrenzung zum Unterlassen. [tun2]Baldur und Weinert haben durch ihr Verhalten aktiv etwas "
     "erklärt. [unt]Wer dagegen nichts erklärt und nur einen fremden Irrtum nicht aufklärt, täuscht allenfalls durch "
     "Unterlassen, [gar]und das nur mit einer Garantenpflicht zur Aufklärung nach Paragraf dreizehn.", PS),
    # --- H Klausurtipp (Lexi) -------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Täuschung in drei Schritten. [tipp1]Gibt es eine ausdrückliche Lüge? [tipp2]Wenn "
     "nicht: Was erklärt das Verhalten nach der Verkehrsanschauung mit, und stimmt das? [tipp3]Erst danach kommt das "
     "Unterlassen mit Garantenpflicht. [tipp4]Und achte auf den Zeitpunkt: Getäuscht wird bei der Bestellung, nicht "
     "beim Weggehen.", PS),
    # --- I Schema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Täuschung. [s1]Erstens: ausdrückliche Erklärung. [s2]Zweitens: konkludente Erklärung. "
     "[s2a]Den Erklärungswert nach der Verkehrsanschauung bestimmen, [s2b]mit der Wirklichkeit vergleichen, "
     "[s2c]bei wahren Erklärungen: planmäßig erweckter Gesamteindruck und direkter Vorsatz. [s3]Drittens: Unterlassen, "
     "nur mit Garantenpflicht.", PS),
    # --- J Merksatz (Lexi) ----------------------------------------------------------------------------------------
    ("[merke]Merke: Wer im Restaurant bestellt, erklärt, dass er zahlen kann und will. [m2]Und wer planmäßig eine Rechnung "
     "vortäuscht, täuscht auch mit lauter wahren Sätzen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
