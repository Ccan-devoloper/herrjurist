"""Folge 051 · Diebstahl § 242 Schema: Wegnahme & Zueignungsabsicht (Fr · Klausurpraxis, Format Schema).
Fall im Lesesaal der Unibibliothek (Hook des Themenplans): Matthias nimmt das Ladekabel von Antje vom Nachbartisch mit
nach Hause, während Antje kurz in der Cafeteria ist. Vertieft gegenüber Folge 047 (dort § 242 nur als Feld der
Landkarte): Wortlaut § 242 I und Aufbau; fremde bewegliche Sache (§ 90 BGB; Fremdheit nach BGB, BGH 4 StR 591/17
Rn. 6); Wegnahme und Gewahrsam (BGH 4 StR 338/20 Rn. 5, 8); gelockerter Gewahrsam (BGH 5 StR 10/20 Rn. 5, 7, dort
auch der Gegenfall Handy auf der Straße); Gewahrsamsenklave (BGH 5 StR 593/18 Rn. 4 f.; 2 StR 145/13 Rn. 3); Vorsatz,
Tatbestandsirrtum § 16 (Variante 1); Zueignungsabsicht: Aneignung zielgerichtet, Enteignung bedingter Vorsatz
(BGH 3 StR 148/18 Rn. 7; 3 StR 536/18 Rn. 16); Gebrauchsanmaßung mit Rückgabewillen (BGH 4 StR 308/25 Rn. 6;
Variante 2); Rechtswidrigkeit der erstrebten Zueignung, fälliger und durchsetzbarer Anspruch auf gerade diese Sache
(BGH 3 StR 458/25 Rn. 5 f.; Variante 3); § 248a (geringwertig; BGH 2 StR 176/04 Rn. 3); § 243 als Strafzumessungsregel
(BGH 1 StR 470/00 Rn. 11); Klausurtipp (Zueignung nicht im objektiven Tatbestand, BGH 4 StR 591/17 Rn. 17), Schema,
Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Namen nie im Genitiv mit -s (Erfahrung 015/047: „Gerdas“, „Dagmars“ wurden verschluckt)."""

P, PS = 0.4, 0.6

STIMMEN = {"Matthias": "christian", "Antje": "lucy"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Lesesaal der Unibibliothek ------------------------------------------------------------------------------
    ("[fall]Donnerstagnachmittag im Lesesaal der Unibibliothek. [antje]Antje lernt für ihre Klausur. [kabel]Ihr Handy "
     "lädt an einem weißen Ladekabel für fünfzehn Euro, das in der Steckdose am Tisch steckt. [kaffee]Dann geht sie kurz "
     "in die Cafeteria. Das Handy nimmt sie mit, Kabel, Jacke und Bücher bleiben am Platz. [matthias]Am Nachbartisch sitzt "
     "Matthias. Sein Akku ist fast leer, sein eigenes Kabel liegt zu Hause.", 0.3),
    ("[m1]Das nehme ich mir einfach mit.", 0.3, "Matthias"),
    ("[steckt]Er zieht das Kabel aus der Steckdose und steckt es in seinen Rucksack. [heim]Zu Hause will er es behalten. "
     "[zurueck]Zehn Minuten später kommt Antje zurück.", 0.3),
    ("[a1]Wo ist denn mein Ladekabel?", 0.4, "Antje"),
    ("[frage]Hat Matthias einen Diebstahl begangen? [frage2]Wir prüfen Paragraf zweihundertzweiundvierzig Schritt für "
     "Schritt, mit drei Varianten.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier sind der Fall und die Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut und Aufbau -------------------------------------------------------------------------------------------
    ("[p242]Paragraf zweihundertzweiundvierzig, Absatz eins: [p242w]Wer eine fremde bewegliche Sache einem anderen in der "
     "Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf "
     "Jahren oder mit Geldstrafe bestraft. [obj]Daraus folgt der Aufbau: Im objektiven Tatbestand stehen die fremde "
     "bewegliche Sache und die Wegnahme. [subj]Im subjektiven Tatbestand stehen der Vorsatz und die Absicht "
     "rechtswidriger Zueignung.", PS),
    # --- D Fremde bewegliche Sache ---------------------------------------------------------------------------------------
    ("[sache]Erstes Merkmal: die fremde bewegliche Sache. [sache2]Das Kabel ist ein körperlicher Gegenstand, also eine "
     "Sache, [bewegl]und Matthias kann es wegtragen. [fremd]Fremd ist es, weil es nach bürgerlichem Recht Antje gehört "
     "und nicht ihm.", PS),
    # --- E Wegnahme und Gewahrsam ----------------------------------------------------------------------------------------
    ("[wegn]Zweites Merkmal: die Wegnahme. [wegn2]Nach dem Bundesgerichtshof ist das der Bruch fremden und die Begründung "
     "neuen Gewahrsams. [gew]Gewahrsam ist die von einem Herrschaftswillen getragene tatsächliche Sachherrschaft, "
     "[verkehr]beurteilt nach den Anschauungen des täglichen Lebens. [weg]Aber Antje ist doch gar nicht da? "
     "[locker]Gewahrsam kann in gelockerter Form fortbestehen, so der Bundesgerichtshof, etwa beim Landwirt, der seine "
     "Geräte auf dem Feld zurücklässt. [antjeok]Antje ist nur kurz im Haus unterwegs, ihr Platz ist sichtbar besetzt: "
     "Sie hat weiter Gewahrsam. [strasse]Anders bei einem Handy, das sein Besitzer nachts auf der Straße verloren hatte. "
     "Er war fort und konnte nicht darauf einwirken. [fund]Kein Gewahrsam mehr, also nur Unterschlagung.", PS),
    # --- F Bruch und neuer Gewahrsam: Gewahrsamsenklave ------------------------------------------------------------------
    ("[bruch]Matthias hebt den Gewahrsam von Antje ohne ihren Willen auf: ein Bruch. [neu]Neuen Gewahrsam begründet er, "
     "sobald er das kleine Kabel in seinen Rucksack steckt, [lesesaal]schon im Lesesaal. [enklave]Kleine, leicht "
     "bewegliche Sachen in der eigenen Tasche weist die Verkehrsauffassung nach dem Bundesgerichtshof dem Täter zu, auch im fremden Herrschaftsbereich. "
     "Man spricht von einer Gewahrsamsenklave. [wegok]Die Wegnahme ist vollendet, der objektive Tatbestand erfüllt.", PS),
    # --- G Vorsatz -------------------------------------------------------------------------------------------------------
    ("[vors]Im subjektiven Tatbestand zuerst der Vorsatz. [vors2]Matthias weiß, dass das Kabel Antje gehört, und will es "
     "nehmen. [v1]Variante eins: Matthias besitzt ein gleiches weißes Kabel und glaubt, er habe es am Morgen dort vergessen. "
     "Er hält das Kabel von Antje für seines. [v1b]Dann kennt er die Fremdheit nicht. [v1ok]Nach Paragraf sechzehn handelt er ohne "
     "Vorsatz.", PS),
    # --- H Zueignungsabsicht ---------------------------------------------------------------------------------------------
    ("[zueig]Das Herzstück ist die Zueignungsabsicht. Sie hat zwei Teile. [aneig]Die Aneignung muss Matthias "
     "beabsichtigen, also zielgerichtet wollen, direkter Vorsatz ersten Grades: [aneig2]Er will das Kabel seinem Vermögen "
     "einverleiben und wie ein Eigentümer darüber verfügen. [enteig]Für die Enteignung genügt bedingter Vorsatz: Er nimmt "
     "zumindest in Kauf, dass Antje ihr Kabel auf Dauer verliert. [zueigok]Im Grundfall will er es behalten. Beides "
     "liegt vor.", PS),
    # --- I Gebrauchsanmaßung (Variante 2) --------------------------------------------------------------------------------
    ("[v2]Variante zwei: Matthias will das Kabel nur über Nacht benutzen.", 0.3),
    ("[m2]Morgen früh lege ich es zurück.", 0.3, "Matthias"),
    ("[v2b]Wer schon bei der Wegnahme fest vorhat, die Sache unverändert zurückzugeben, maßt sich nur ihren Gebrauch an. "
     "[v2c]Ihm fehlt der Enteignungsvorsatz und damit die Zueignungsabsicht. [v2ok]Eine solche Gebrauchsanmaßung ist kein "
     "Diebstahl.", PS),
    # --- J Rechtswidrigkeit der erstrebten Zueignung (Variante 3) --------------------------------------------------------
    ("[rwz]Die erstrebte Zueignung muss außerdem rechtswidrig sein, [rwz2]und darauf muss sich der Vorsatz erstrecken. "
     "[rwz3]Rechtswidrig ist sie, wenn der Täter keinen fälligen und durchsetzbaren Anspruch gerade auf diese Sache hat. "
     "[v3]Variante drei: Antje hat Matthias genau dieses Kabel gestern verkauft. Er hat bezahlt, und sie hat zugesagt, "
     "es ihm heute zu übergeben. [v3b]Dann hat er aus dem Kaufvertrag einen fälligen, einredefreien Anspruch auf Übereignung "
     "dieses Kabels. [v3ok]Die Zueignung ist nicht rechtswidrig, ein Diebstahl scheidet aus.", PS),
    # --- K Ergebnis, § 248a, § 243 ---------------------------------------------------------------------------------------
    ("[erg]Zurück zum Grundfall: Matthias hat keinen Anspruch auf das Kabel. [rs]Rechtswidrigkeit und Schuld liegen vor. "
     "[erg2]Matthias hat sich wegen Diebstahls strafbar gemacht. [p248a]Weil ein Ladekabel für fünfzehn Euro geringwertig "
     "ist, wird die Tat nach Paragraf zweihundertachtundvierzig a nur auf Antrag verfolgt, [oeff]außer die "
     "Strafverfolgungsbehörde bejaht ein besonderes öffentliches Interesse. [p243]Ein Ausblick auf Paragraf "
     "zweihundertdreiundvierzig: [p243b]Seine Regelbeispiele, etwa das Einbrechen in ein Gebäude oder gewerbsmäßiges "
     "Stehlen, sind keine Tatbestandsmerkmale, sondern Strafzumessungsregeln. [p243c]Bei geringwertigen Sachen ist ein "
     "besonders schwerer Fall nach den Nummern eins bis sechs ausgeschlossen.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Zueignung nie im objektiven Tatbestand. [tipp2]Sie muss nicht gelingen, Matthias "
     "muss sie nur beabsichtigen. [tipp3]Trenne dann sauber: Aneignung als Absicht, Enteignung als Vorsatz. "
     "[tipp4]Und bei jeder Gebrauchsanmaßung frage: Wollte er die Sache unverändert zurückgeben?", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s_i]Römisch eins: Tatbestand. [s1a]Objektiv: fremde bewegliche Sache [s1b]und Wegnahme, "
     "also Bruch fremden und Begründung neuen Gewahrsams. [s1c]Subjektiv: Vorsatz [s1d]und Absicht rechtswidriger "
     "Zueignung, mit Aneignungsabsicht, Enteignungsvorsatz und Rechtswidrigkeit der Zueignung. [s_ii]Römisch zwei: "
     "Rechtswidrigkeit. [s_iii]Römisch drei: Schuld. [s_iv]Römisch vier: Strafzumessung, besonders schwerer Fall nach "
     "Paragraf zweihundertdreiundvierzig. [s_v]Römisch fünf: Strafantrag bei geringwertigen Sachen.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wegnahme heißt fremden Gewahrsam brechen und neuen begründen; wer nur kurz weggeht und in der Nähe "
     "bleibt, behält ihn gelockert. "
     "[m_2]Zueignungsabsicht heißt: Aneignung gewollt, Enteignung zumindest in Kauf genommen. [m_3]Wer schon beim Nehmen fest "
     "vorhat, die Sache unverändert zurückzubringen, stiehlt nicht.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
