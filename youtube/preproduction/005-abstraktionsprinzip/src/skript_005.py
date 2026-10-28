"""Folge 005 · Abstraktionsprinzip & Trennungsprinzip: Ein Kauf, drei Verträge (Examenswissen, Zivilrecht).
Hook: Brötchenkauf (drei Verträge). Beispielfall frei erfunden: Der 17-jährige Ben kauft Nachbar Walter einen
Plattenspieler ab und zahlt bar; die Eltern verweigern die Genehmigung. Kaufvertrag unwirksam (§§ 107, 108 I BGB),
Übereignung des Plattenspielers wirksam (lediglich rechtlich vorteilhaft, Abstraktionsprinzip), Übereignung des Geldes
unwirksam (Fehleridentität); Rückabwicklung über § 985 (Geld) und § 812 I 1 Alt. 1 BGB (Plattenspieler).
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) =
Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Sandra": "sabrina", "Hanne": "elinor", "Ben": "niklas", "Walter": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Hook: Brötchenkauf ----------------------------------------------------------------------------------------
    ("[baeck]Samstagmorgen in der Bäckerei von Hanne. [sandra]Sandra zeigt auf die Auslage.", 0.3),
    ("[s1]Ein Roggenbrötchen, bitte.", 0.3, "Sandra"),
    ("[h1]Sechzig Cent.", 0.4, "Hanne"),
    ("[muenzen]Sandra legt die Münzen hin und nimmt die Tüte. "
     "[drei]Juristisch hat sie damit gerade drei Verträge geschlossen.", 0.6),
    # --- B Drei Verträge: Trennungs- und Abstraktionsprinzip ---------------------------------------------------------
    ("[kv]Erstens den Kaufvertrag nach Paragraf vierhundertdreiunddreißig. [kv2]Er verpflichtet nur: Hanne, "
     "das Brötchen zu übergeben und Sandra das Eigentum daran zu verschaffen. Und Sandra, den Preis zu zahlen. "
     "[verpfl]Das ist das Verpflichtungsgeschäft.", P),
    ("[ue1]Zweitens die Übereignung des Brötchens nach Paragraf neunhundertneunundzwanzig Satz eins: Einigung und Übergabe. "
     "[ue2]Drittens die Übereignung der Münzen an Hanne. "
     "[verf]Erst diese beiden Verfügungen lassen das Eigentum übergehen.", P),
    ("[trenn]Das ist das Trennungsprinzip: Verpflichtung und Verfügung sind getrennte Rechtsgeschäfte. "
     "[abstr]Und nach dem Abstraktionsprinzip hängt die Wirksamkeit der Übereignung grundsätzlich nicht davon ab, "
     "ob der Kaufvertrag wirksam ist. [spannend]Beim Brötchen fällt das niemandem auf. Spannend wird es, wenn der Kaufvertrag scheitert.", PS),
    # --- C Fall: Plattenspieler -----------------------------------------------------------------------------------------
    ("[ben]Am Nachmittag ist Sandras Sohn Ben, siebzehn, bei Nachbar Walter. "
     "[kauf]Er kauft Walters alten Plattenspieler für hundertzwanzig Euro.", 0.3),
    ("[b1]Hier sind hundertzwanzig Euro, bar.", 0.3, "Ben"),
    ("[w0]Bitte schön, der Plattenspieler. Viel Spaß damit!", 0.4, "Walter"),
    ("[fuehrer]Das Geld hatten Ben seine Eltern für den Führerschein gegeben. "
     "[mutter]Als Sandra davon hört, geht sie sofort zu Walter.", 0.3),
    ("[s2]Den Kauf genehmigen wir nicht! Wir wollen das Geld zurück.", 0.3, "Sandra"),
    ("[w1]Dann will ich aber meinen Plattenspieler wiederhaben.", 0.4, "Walter"),
    ("[frage]Wem gehören jetzt Plattenspieler und Geld? Und wie kommt beides zurück?", 0.6),
    # --- D Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Vertrag 1: Kaufvertrag ----------------------------------------------------------------------------------------------
    ("[v1]Wir prüfen die drei Verträge getrennt. Erstens der Kaufvertrag. "
     "[mj]Ben ist minderjährig, also beschränkt geschäftsfähig. "
     "[nachteil]Der Kaufvertrag verpflichtet ihn zur Zahlung, ist also rechtlich nachteilig. "
     "[p107]Dafür braucht er die Einwilligung seiner Eltern, Paragraf hundertsieben.", P),
    ("[p110]Der Taschengeldparagraf hilft nicht: Das Geld war für den Führerschein bestimmt, nicht zur freien Verfügung. "
     "[schwebend]Der Vertrag ist deshalb schwebend unwirksam [verweigert]und mit der Verweigerung der Genehmigung "
     "endgültig unwirksam, Paragraf hundertacht.", PS),
    # --- F Vertrag 2: Übereignung des Plattenspielers ---------------------------------------------------------------------
    ("[v2]Zweitens die Übereignung des Plattenspielers. [eu]Walter und Ben haben sich geeinigt, und Walter hat ihn übergeben. "
     "[vorteil]Ben erlangt dadurch nur Eigentum, also lediglich einen rechtlichen Vorteil. Das darf er allein.", P),
    ("[abstr2]Und der unwirksame Kaufvertrag? Er spielt hier keine Rolle. Das ist das Abstraktionsprinzip. "
     "[bgh]Der Bundesgerichtshof sagt: Verfügungen sind unabhängig von ihrem Grundgeschäft zu beurteilen. "
     "[eig]Ben ist also Eigentümer des Plattenspielers geworden.", PS),
    # --- G Vertrag 3: Übereignung des Geldes, Fehleridentität -----------------------------------------------------------
    ("[v3]Drittens die Übereignung des Geldes. [geld]Hier verliert Ben sein Eigentum an den Scheinen. "
     "Das ist rechtlich nachteilig, und die Eltern haben nicht zugestimmt. [geld_unw]Also ist auch diese Übereignung unwirksam.", P),
    ("[fi]Aber Achtung: nicht, weil der Kaufvertrag scheitert, sondern weil derselbe Fehler auch die Übereignung selbst trifft. "
     "[fi2]Das nennt man Fehleridentität. Sie durchbricht das Abstraktionsprinzip nicht. "
     "Jedes Geschäft wird für sich geprüft und hat hier denselben Mangel. "
     "[fi3]Typisch ist das bei Geschäftsunfähigkeit: Dann sind Kauf und beide Übereignungen nichtig, Paragraf hundertfünf.", PS),
    # --- H Rückabwicklung ------------------------------------------------------------------------------------------------------
    ("[rueck]Jetzt die Rückabwicklung. [geld_zur]Ben ist Eigentümer der Scheine geblieben. "
     "Solange Walter sie noch hat, kann Ben sie nach Paragraf neunhundertfünfundachtzig herausverlangen.", P),
    ("[w985]Und Walter? Paragraf neunhundertfünfundachtzig scheidet aus, er ist nicht mehr Eigentümer. "
     "[w812]Ihm hilft Paragraf achthundertzwölf Absatz eins Satz eins, erste Alternative. "
     "[erlangt]Ben hat Eigentum und Besitz am Plattenspieler erlangt, [leistung]durch Walters Leistung, "
     "[ohne]und zwar ohne rechtlichen Grund, weil der Kaufvertrag unwirksam ist. "
     "[rf]Ben muss ihn deshalb zurückübereignen und herausgeben.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Verlangt jemand eine Sache heraus, prüfst du zuerst Paragraf neunhundertfünfundachtzig. "
     "[tipp2]Beim Eigentum prüfst du jede Übereignung für sich. "
     "[tipp3]Schreib nie: Der Kaufvertrag ist unwirksam, also ist das Eigentum nicht übergegangen.", PS),
    # --- J Klausurschema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Walter gegen Ben auf Herausgabe des Plattenspielers. "
     "[k1]Teil A: Paragraf neunhundertfünfundachtzig. Römisch eins: Ben ist Besitzer. "
     "[k2]Römisch zwei: Ist Walter noch Eigentümer? [k3]Verloren durch Übereignung: Einigung und Übergabe. "
     "[k4]Die Einigung ist wirksam, weil lediglich rechtlich vorteilhaft. [k5]Ergebnis: kein Anspruch.", P),
    ("[k6]Teil B: Paragraf achthundertzwölf Absatz eins Satz eins, erste Alternative. "
     "[k7]Römisch eins: etwas erlangt, Eigentum und Besitz. [k8]Römisch zwei: durch Leistung. "
     "[k9]Römisch drei: ohne rechtlichen Grund, der Kaufvertrag ist unwirksam. "
     "[k10]Römisch vier: Rückübereignung und Herausgabe.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Kaufvertrag verpflichtet, die Übereignung verfügt. "
     "[m2]Fällt nur der Kaufvertrag weg, bleibt die Übereignung wirksam. Zurück geht es über Paragraf achthundertzwölf.", 1.4),
]
