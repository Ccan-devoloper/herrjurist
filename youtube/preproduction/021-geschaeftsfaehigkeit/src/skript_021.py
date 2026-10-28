"""Folge 021 · Geschäftsfähigkeit Schema §§ 104 ff. BGB: Minderjährige im Vertrag (Klausurpraxis, Format Schema).
Beispielfall frei erfunden (nach dem Plan-Hook): Die fünfzehnjährige Frieda kauft im Handyladen von Herrn Ritter ein
Smartphone für 600 Euro, 100 Euro Anzahlung aus gespartem Taschengeld, Rest in fünf Monatsraten; Ritter weiß, dass sie
fünfzehn ist, die Eltern wissen nichts. Die Mutter verweigert die Genehmigung nur gegenüber Frieda; Ritter fordert die
Eltern zur Erklärung auf, sie schweigen zwei Wochen. Prüfung Ritter gegen Frieda aus § 433 II: I. Einigung, II. Wirksamkeit
(1. §§ 104, 105, 2. § 106, 3. § 107, 4. Einwilligung § 183, 5. § 110 mit Gegenfall Kopfhörer, 6. Genehmigung §§ 108, 184,
Aufforderung § 108 II, Widerruf § 109 mit § 131 II), III. Ergebnis; Ausblick §§ 112, 113. Belege je Aussage:
../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Frieda": "ela_froh", "Ritter": "helmut", "Mutter": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A/B Fall: Handyladen, am Abend zu Hause, Ritters Brief -------------------------------------------------------
    ("[fall]Frieda ist fünfzehn. [laden]Im Handyladen von Herrn Ritter entdeckt sie ein Smartphone für sechshundert "
     "Euro. Sonst kostet es achthundert.", 0.3),
    ("[f1]Sechshundert statt achthundert? Das nehme ich!", 0.4, "Frieda"),
    ("[anz]Hundert Euro zahlt sie sofort aus ihrem gesparten Taschengeld. [raten]Den Rest soll sie in fünf Monatsraten "
     "zahlen. [weiss]Ritter weiß, dass Frieda fünfzehn ist. Ihre Eltern wissen nichts von dem Kauf.", 0.3),
    ("[r1]Abgemacht. Viel Spaß mit dem Handy!", 0.4, "Ritter"),
    ("[abend]Am Abend sieht Friedas Mutter das neue Handy.", 0.3),
    ("[mu1]Sechshundert Euro? Das genehmigen wir nicht!", 0.4, "Mutter"),
    ("[brief]Davon erfährt Ritter nichts. Er schreibt den Eltern und fordert sie auf, zu erklären, ob sie den Kauf "
     "genehmigen. [schweigen]Die Eltern antworten nicht. [frage]Muss Frieda die restlichen fünfhundert Euro zahlen?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Anspruch, I. Einigung -------------------------------------------------------------------------------------
    ("[ansp]Ritter verlangt den restlichen Kaufpreis nach Paragraf vierhundertdreiunddreißig Absatz zwei. "
     "[einig]Römisch eins: die Einigung. Angebot und Annahme liegen vor. [wirk]Römisch zwei: Ist der Vertrag wirksam? "
     "Das hängt an der Geschäftsfähigkeit von Frieda.", PS),
    # --- E II.1/2 Geschäftsunfähigkeit, beschränkte Geschäftsfähigkeit -------------------------------------------------
    ("[p104]Erstens: Geschäftsunfähig ist nach Paragraf hundertvier, wer noch nicht sieben Jahre alt ist [krank]oder "
     "wegen einer krankhaften Störung der Geistestätigkeit dauerhaft nicht frei entscheiden kann. [p105]Seine "
     "Willenserklärung ist nichtig, Paragraf hundertfünf. [p106]Zweitens: Frieda ist fünfzehn, also minderjährig, und hat "
     "das siebte Lebensjahr vollendet. Nach Paragraf hundertsechs ist sie beschränkt geschäftsfähig.", PS),
    # --- F II.3 lediglich rechtlicher Vorteil, § 107 ---------------------------------------------------------------------
    ("[p107]Drittens: Paragraf hundertsieben. [p107w]Der Minderjährige bedarf zu einer Willenserklärung, durch die er "
     "nicht lediglich einen rechtlichen Vorteil erlangt, der Einwilligung seines gesetzlichen Vertreters. [eltern]Das "
     "sind hier Friedas Eltern. [pflicht]Der Kaufvertrag verpflichtet Frieda, sechshundert Euro zu zahlen. Das ist ein "
     "rechtlicher Nachteil. [schnapp]Dass das Handy ein Schnäppchen ist, spielt keine Rolle. Es zählt die rechtliche "
     "Folge, nicht die wirtschaftliche.", PS),
    # --- G II.4 Einwilligung -------------------------------------------------------------------------------------------
    ("[einw]Viertens: die Einwilligung, also die vorherige Zustimmung, Paragraf hundertdreiundachtzig. [keine]Die "
     "Eltern wussten vom Kauf nichts. Eine Einwilligung fehlt.", PS),
    # --- H II.5 Taschengeld, § 110 --------------------------------------------------------------------------------------
    ("[p110]Fünftens: der Taschengeldparagraf, Paragraf hundertzehn. [p110w]Der Vertrag gilt als von Anfang an "
     "wirksam, wenn Frieda die vertragsmäßige Leistung mit Mitteln bewirkt, die ihr zu diesem Zweck oder zu freier "
     "Verfügung überlassen worden sind. [nur]Frieda hat aber nur die Anzahlung von ihrem Taschengeld bezahlt. "
     "Fünfhundert Euro sind offen. [rate]Beim Ratenkauf ist die Leistung erst mit der letzten Rate bewirkt. Bis dahin "
     "hilft Paragraf hundertzehn nicht.", P),
    ("[kopf]Anders bei Kopfhörern für vierzig Euro, die Frieda sofort von ihrem Taschengeld bezahlt. [kopf_ok]Dieser "
     "Vertrag ist von Anfang an wirksam.", PS),
    # --- I II.6 Genehmigung, § 108 I, § 184 ----------------------------------------------------------------------------
    ("[p108]Sechstens: die Genehmigung. [schwebe]Ohne Einwilligung hängt die Wirksamkeit des Vertrags nach Paragraf "
     "hundertacht Absatz eins von der Genehmigung der Eltern ab. Der Vertrag ist schwebend unwirksam. [rueck]Eine "
     "Genehmigung würde nach Paragraf hundertvierundachtzig auf den Vertragsschluss zurückwirken.", P),
    # --- J § 108 II: Aufforderung ---------------------------------------------------------------------------------------
    ("[verw]Die Mutter hat die Genehmigung zwar verweigert, aber nur gegenüber Frieda. [auff]Mit Ritters "
     "Aufforderung wird diese Verweigerung nach Paragraf hundertacht Absatz zwei unwirksam. [nurihm]Die Eltern können "
     "sich jetzt nur noch ihm gegenüber erklären. [zwei]Genehmigen können sie nur bis zwei Wochen nach Empfang der "
     "Aufforderung. [fikt]Sie schweigen. Damit gilt die Genehmigung als verweigert.", PS),
    # --- K Widerruf § 109, Zugang § 131 II ------------------------------------------------------------------------------
    ("[p109]Und Ritter? Bis zur Genehmigung darf der andere Teil widerrufen, Paragraf hundertneun, [p109s]sogar "
     "gegenüber Frieda selbst. [p131]Sonst würde ein solcher Widerruf gegenüber einer beschränkt Geschäftsfähigen "
     "grundsätzlich erst wirksam, wenn er den Eltern zugeht, Paragraf hunderteinunddreißig Absatz zwei. "
     "[kannte]Aber Ritter wusste, dass Frieda minderjährig ist. Dann darf er nur widerrufen, wenn sie der Wahrheit "
     "zuwider behauptet hätte, ihre Eltern seien einverstanden. [nicht]Das hat sie nicht.", PS),
    # --- L III. Ergebnis, Ausblick §§ 112, 113 ---------------------------------------------------------------------------
    ("[erg]Römisch drei: Ergebnis. Der Kaufvertrag ist endgültig unwirksam. Ritter kann die fünfhundert Euro nicht "
     "verlangen. [rabw]Wie Handy und Anzahlung zurückkommen, ist eine eigene Frage der Rückabwicklung.", P),
    ("[aus]Nur am Rande: Ermächtigen die Eltern ihr Kind, ein Erwerbsgeschäft selbständig zu betreiben, mit "
     "Genehmigung des Familiengerichts, [p113]oder in Dienst oder Arbeit zu treten, ist es für die dazugehörigen "
     "Geschäfte unbeschränkt geschäftsfähig, Paragrafen hundertzwölf und hundertdreizehn.", PS),
    # --- M Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne Verpflichtung und Verfügung. [tipp2]Der Kaufvertrag ist für Frieda rechtlich "
     "nachteilig. [tipp3]Die Übereignung des Handys an sie bringt ihr dagegen nur Eigentum und keine Pflicht. "
     "[tipp4]Sie ist lediglich rechtlich vorteilhaft und braucht keine Einwilligung.", PS),
    # --- N Klausurschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Ritter gegen Frieda aus Paragraf vierhundertdreiunddreißig Absatz zwei. [k1]Römisch "
     "eins: Einigung. [k2]Römisch zwei: Wirksamkeit. [k2a]Erstens: geschäftsunfähig? [k2b]Zweitens: beschränkt "
     "geschäftsfähig. [k2c]Drittens: lediglich rechtlicher Vorteil? [k2d]Viertens: Einwilligung? [k2e]Fünftens: "
     "Taschengeld? [k2f]Sechstens: Genehmigung, samt Aufforderung und Widerruf. [k3]Römisch drei: Ergebnis.", PS),
    # --- O Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Was eine Minderjährige verpflichtet, braucht die Zustimmung ihrer Eltern, [m2]vorher als Einwilligung oder nachher "
     "als Genehmigung. [m3]Der Taschengeldparagraf hilft nur, wenn sie mit überlassenem Geld schon alles bezahlt hat.", 1.4),
]
