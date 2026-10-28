"""Folge 128 · Tötung auf Verlangen § 216 oder Suizidhilfe? Der Gisela-Fall (Mi · Examenswissen · StGB BT, Format Abgrenzung).
Beispielfall nach dem Plan-Hook, ohne Methodendetail: Hedwig (um 70) ist schwer krank und bittet ihren Mann Wilfried seit
Monaten ausdrücklich, ihr beim Sterben zu helfen; sie hat es lange und klar überlegt. Wilfried führt den tödlichen Schritt
selbst aus; Hedwig kann danach nichts mehr ändern. Gegenvariante: Er bereitet nur vor, sie behält den letzten Schritt.
Kern als Abgrenzung: 1. Ausgangspunkt (Suizid und Teilnahme straflos, Verweis 094; § 216 Abs. 1 als Privilegierung des
§ 212, Wortlautkarte) → 2. Kriterium: Wer beherrscht das zum Tod führende Geschehen zuletzt (BGHSt 63, 161 Rn. 18;
6 StR 68/21 Rn. 14; Tatherrschaft, Verweis 119) → Gisela-Fall BGHSt 19, 135, 139 f. (Wiedergabe über 6 StR 68/21 Rn. 18 f.)
→ 3. BGH 6 StR 68/21 (normative Betrachtung, Gesamtplan, Rn. 15–17; Verfassungsfrage offen, Rn. 21, 23), BVerfG 2020 ein
Satz → 4. Merkmale (ausdrücklich, ernstlich, bestimmt) → Zweispalter Täter § 216 / strafloser Gehilfe → Ergebnis und
Gegenvariante → Klausurtipp → Schema → Merksatz → Hilfsangebot.
ZURÜCKHALTUNG (Thema Suizid, wie 094): keine Methode, kein Mittel, keine Gegenstände dazu in Sprechtext, Bild oder Tafeln;
auch der Gisela-Fall nur als „gemeinsamer Plan, zusammen aus dem Leben zu scheiden“, „den letzten Schritt in der Hand“.
Belege: ../RECHTSSTAND.md. Namen (deutsch, nicht vergeben): Hedwig, Wilfried; Figurenstimmen hilde, stephan.
Nachvertonung (einmal je Segment): Segment 3 („Wilfried“ von beiden Erkennern als „Wilfrig“ gehört; „ihr“ eingefügt),
Segmente 8 und 16 („ernstliche“ von beiden Erkennern als „ärztliche“ gehört; lautliche Schreibung „ernst-liche“ nur im
Sprechtext, Tafeln und Untertitel normal).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hedwig": "hilde", "Wilfried": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: zu Hause ------------------------------------------------------------------------------------------------
    ("[fall]Hedwig ist schwer krank, und ihre Schmerzen werden immer stärker. [bitte]Seit Monaten bittet sie ihren Mann "
     "Wilfried ausdrücklich, ihr beim Sterben zu helfen. [klar]Sie hat es sich lange und klar überlegt.", P),
    ("[h1]Ich habe es mir gut überlegt. Bitte hilf mir.", P, "Hedwig"),
    ("[tat]Eines Abends gibt Wilfried ihr nach. Er führt den tödlichen Schritt selbst aus, [danach]und Hedwig kann danach "
     "nichts mehr ändern. [stirbt]Sie stirbt in derselben Nacht.", P),
    # --- A2 Fall: Anklage -------------------------------------------------------------------------------------------------
    ("[anklage]Die Staatsanwaltschaft klagt Wilfried an.", P),
    ("[w1]Ich habe nur getan, worum sie mich gebeten hat.", P, "Wilfried"),
    ("[frage]Ist Wilfried wegen Tötung auf Verlangen strafbar? [frage2]Und wäre er straflos geblieben, wenn er alles "
     "vorbereitet und den letzten Schritt Hedwig überlassen hätte?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Ausgangspunkt, § 216 Abs. 1 (Wortlaut) ----------------------------------------------------------------------
    ("[aus]Erstens, der Ausgangspunkt. Wer sich selbst tötet, erfüllt keinen Tötungstatbestand. [teiln]Deshalb ist auch "
     "die Hilfe dazu straflos, wie du aus Folge vierundneunzig kennst. [p212]Wer dagegen einen anderen tötet, ist nach "
     "Paragraf zweihundertzwölf strafbar, auch wenn das Opfer es will. [p216]Paragraf zweihundertsechzehn Absatz eins mildert "
     "nur die Strafe: Ist jemand durch das ausdrückliche und ernst-liche Verlangen des Getöteten zur Tötung bestimmt worden, "
     "[strafe]drohen sechs Monate bis fünf Jahre Freiheitsstrafe, statt mindestens fünf Jahren. [priv]Paragraf "
     "zweihundertsechzehn privilegiert also den Totschlag. [grenze]Die Grenze zur straflosen Suizidhilfe ist "
     "deshalb entscheidend.", PS),
    # --- D 2. Abgrenzungskriterium ----------------------------------------------------------------------------------------
    ("[krit]Zweitens, das Abgrenzungskriterium. Entscheidend ist, wer das zum Tod führende Geschehen zuletzt beherrscht, "
     "[letzt]also wer den letzten, unwiderruflichen Akt in der Hand hat. [f119]Das ist die Tatherrschaft, die du aus Folge "
     "hundertneunzehn kennst. [hand]Gibt sich der Sterbewillige in die Hand des anderen, um den Tod duldend von ihm "
     "entgegenzunehmen, hat der andere die Tatherrschaft. [selbst]Behält er dagegen bis zuletzt die freie Entscheidung über "
     "sein Schicksal, tötet er sich selbst, wenn auch mit fremder Hilfe.", PS),
    # --- E Gisela-Fall ----------------------------------------------------------------------------------------------------
    ("[gis]So hat es der Bundesgerichtshof neunzehnhundertdreiundsechzig im Gisela-Fall entschieden. [gis2]Ein junges Paar "
     "hatte den gemeinsamen Plan, zusammen aus dem Leben zu scheiden. Nach diesem Plan hatte er den letzten Schritt bis "
     "zuletzt in der Hand. [gis3]Sie starb, er überlebte. [gis4]Er wurde zunächst freigesprochen. Der BGH hob den Freispruch "
     "auf: Er hatte die Tatherrschaft. [gis5]Dass sie sich anfangs noch hätte retten können, änderte daran nichts, denn sein "
     "Beitrag lief bis zuletzt weiter. [rg]Zugleich verwarf der BGH die Sicht des Reichsgerichts, nach der es nur darauf "
     "ankam, ob jemand die Tat als eigene wollte.", PS),
    # --- F 3. Neuere Rechtsprechung ---------------------------------------------------------------------------------------
    ("[neu]Drittens, die neuere Rechtsprechung. Zweitausendzweiundzwanzig hatte der BGH diesen Fall: [neu2]Eine Ehefrau half "
     "ihrem schwerkranken Mann auf seinen Wunsch beim Sterben. Den Hauptteil führte er selbst aus, ihr aktiver Beitrag sollte "
     "vor allem den Tod absichern. [norm]Der BGH verlangt eine normative Betrachtung: Ob jemand aktiv handelt, entscheidet nicht "
     "allein. [plan]Nach dem Gesamtplan war alles ein einheitlicher Akt, über den allein der Mann bestimmte. [nach]Auch nach "
     "ihrem Beitrag hätte er noch Hilfe holen lassen können. [frei]Also nur straflose Suizidhilfe, der BGH sprach sie frei. "
     "[bverfg]Dahinter steht das Recht auf selbstbestimmtes Sterben: Deshalb erklärte das Bundesverfassungsgericht "
     "zweitausendzwanzig das Verbot der geschäftsmäßigen Suizidhilfe für nichtig, mehr dazu in Folge vierundneunzig. [offen]Ob Paragraf zweihundertsechzehn eingeschränkt werden muss, wenn "
     "jemand den Schritt faktisch nicht selbst gehen kann, ließ der BGH offen. Er hält es für naheliegend.", PS),
    # --- G 4. Merkmale des § 216 ------------------------------------------------------------------------------------------
    ("[merk]Viertens, die Merkmale. Hat der andere die Tatherrschaft, prüfst du Paragraf zweihundertsechzehn. "
     "[ausdr]Ausdrücklich verlangt ist der Tod, wenn das Opfer ihn eindeutig fordert. Eine bloße Zustimmung genügt nicht. "
     "[ernst]Ernstlich ist das Verlangen nur bei freier, fehlerfreier Willensbildung: Das Opfer überblickt Bedeutung und "
     "Tragweite und entscheidet mit innerer Festigkeit. Eine depressive Augenblicksstimmung allein genügt nicht. [best]Und das Verlangen muss den Täter bestimmt haben, "
     "es muss für ihn handlungsleitend sein.", PS),
    # --- H Zweispalter und Ergebnis -----------------------------------------------------------------------------------------
    ("[zw]Stell beides nebeneinander. [zl]Links der Täter nach Paragraf zweihundertsechzehn: Er führt den letzten Akt selbst "
     "aus, das Opfer kann danach nichts mehr ändern. [zr]Rechts der straflose Gehilfe: Er bereitet vor, das Opfer behält den "
     "letzten Schritt und die freie Entscheidung bis zuletzt.", P),
    ("[erg]Zurück zu Wilfried. Er hat den letzten Schritt selbst ausgeführt, Hedwig konnte danach nichts mehr ändern. Er "
     "hatte die Tatherrschaft. [erg2]Hedwig hat ausdrücklich und ernstlich verlangt, und ihre Bitte hat ihn bestimmt. "
     "[erg3]Wilfried ist wegen Tötung auf Verlangen strafbar. [gegen]In der Gegenvariante bereitet er nur vor, und Hedwig "
     "geht den letzten Schritt selbst. [gegen2]Dann tötet sie sich selbst, und Wilfried bleibt als Gehilfe straflos.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Zieh die Grenze zuerst über die Tatherrschaft am letzten Akt, normativ nach dem Gesamtplan. "
     "[tipp2]Erst wenn der andere herrscht, prüfst du die Merkmale. [tipp3]Und bei strafloser Suizidhilfe denk ans "
     "Unterlassen: Bei einem frei gefassten Sterbewillen muss nach dem BGH auch der Ehepartner den anderen nicht retten.", PS),
    # --- J Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Tötung auf Verlangen. [s1]Eins, objektiver Tatbestand: Tötung eines anderen Menschen, "
     "[s1a]mit Tatherrschaft über den letzten Akt, sonst straflose Suizidhilfe. [s1b]Dann das ausdrückliche und ernst-liche "
     "Verlangen [s1c]und das Bestimmtwerden. [s2]Zwei, subjektiver Tatbestand: Vorsatz, auch zum Verlangen. "
     "[s3]Drei, Rechtswidrigkeit, [s4]vier, Schuld.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer den letzten Akt selbst ausführt, tötet, auf Verlangen nach Paragraf zweihundertsechzehn. [m2]Wer "
     "ihn dem frei entscheidenden Sterbewilligen überlässt, leistet nur straflose Hilfe.", 1.0),
    # --- L Hilfsangebot ---------------------------------------------------------------------------------------------------
    ("[hilfe]Wenn dich das Thema selbst betrifft: Die Telefonseelsorge ist rund um die Uhr und kostenlos für dich da. "
     "[nummern]Die Nummern siehst du hier.", 4.5),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
