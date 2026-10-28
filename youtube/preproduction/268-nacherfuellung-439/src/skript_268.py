"""Folge 268 · Reparatur oder neues Gerät? Nacherfüllung § 439 BGB erklärt (Mo · Der Fall · Kaufrecht · Alltagsfall;
§§ 439, 440 BGB; zusätzlich §§ 269, 437, 474, 475, 475d, 477 BGB).
Fall nach dem Plan-Hook („Der Händler will dein Handy zum dritten Mal reparieren – du willst endlich ein neues“): Undine
kauft im August 2026 im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. 3 Wochen später schaltet es sich immer
wieder von selbst aus. Auf ihren Wunsch repariert Herr Stelzer zweimal (Akku getauscht, Software neu aufgespielt), beide
Male ohne Erfolg. Er bietet eine dritte Reparatur an; Undine will jetzt ein neues Handy. Ein neues kostet ihn 450 €, eine
Reparatur 60 €.
Aufbau (Plan): Hook → Ausgangslage (Verbrauchsgüterkauf, Mangel, § 477; Verweis Folge 063) → § 439 Abs. 1 (Wortlautkarte):
Wahlrecht, Wechsel zur Lieferung (BGH VIII ZR 66/17 LS 3a, Rn. 42 f., 47 f.) → Ort der Nacherfüllung (§ 269; BGH VIII ZR
220/10 Rn. 29, 33) → § 439 Abs. 4 (Wortlautkarte): relative/absolute Unverhältnismäßigkeit (BGH V ZR 275/12 Rn. 39; VIII ZR
66/17 Rn. 59, 76), Verweis Folge 219 in einem Satz → § 440 (Wortlautkarte S. 2) → beim Verbraucher § 475d Abs. 1 Nr. 2
(BT-Drs. 19/27424, S. 37), § 475 Abs. 4 in einem Satz → Ergebnis → Klausurtipp (Lexi) → Schema → Merksatz.
Belege je Cue: ../RECHTSSTAND.md (Normwortlaut gesetze-im-internet.de, Abruf 08.10.2026; BGH-Volltexte mit Rn.).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Undine (sabrina, Frau, mittel), Herr Stelzer (marc, Mann, mittel).
william und laura_ruhig nicht besetzt. Erzählerin/Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen. Kein Genitiv eines Namens."""

P, PS = 0.3, 0.5

STIMMEN = {"Undine": "sabrina", "Stelzer": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Kauf im Handyladen -------------------------------------------------------------------------------------
    ("[fall]Undine kauft im Handyladen von Herrn Stelzer ein neues Smartphone, für sechshundert Euro. [kauf]Sie bezahlt "
     "an der Kasse und nimmt es gleich mit.", P),
    # --- A2 Zu Hause -------------------------------------------------------------------------------------------------------
    ("[aus1]Drei Wochen später schaltet sich das Handy immer wieder von selbst aus. [zurueck]Undine bringt es zurück in "
     "den Laden.", P),
    # --- A3 Zwei Reparaturen -----------------------------------------------------------------------------------------------
    ("[u1]Mein Handy geht ständig aus. Bitte reparieren Sie es.", P, "Undine"),
    ("[rep1]Herr Stelzer tauscht den Akku. [wieder1]Eine Woche später geht das Handy wieder aus. [rep2]Bei der zweiten "
     "Reparatur spielt er die Software neu auf. [wieder2]Und wieder schaltet es sich ab.", P),
    # --- A4 Streit an der Theke, Frage ---------------------------------------------------------------------------------------
    ("[s1]Ich repariere es gern ein drittes Mal.", P, "Stelzer"),
    ("[u2]Nein. Ich will jetzt endlich ein neues Handy.", P, "Undine"),
    ("[s2]Ein neues kostet mich vierhundertfünfzig Euro. Eine Reparatur nur sechzig.", P, "Stelzer"),
    ("[frage]Wer entscheidet: Reparatur oder neues Handy? [frage2]Und kann Undine sogar ohne weitere Frist vom Vertrag "
     "zurücktreten?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Ausgangslage ------------------------------------------------------------------------------------------------------
    ("[lage]Undine kauft privat bei einem Unternehmer: ein Verbrauchsgüterkauf. [mang]Ein Handy, das sich ständig "
     "ausschaltet, ist mangelhaft. [vermut]Zeigt sich der Fehler im ersten Jahr nach der Übergabe, wird vermutet, dass "
     "er schon damals da war. [v063]Alle Käuferrechte zeigt unsere Folge zu Paragraf vierhundertsiebenunddreißig.", PS),
    # --- D 1. Wahlrecht, § 439 Abs. 1 (Wortlautkarte) ---------------------------------------------------------------------
    ("[p439]Paragraf vierhundertneununddreißig Absatz eins: Der Käufer kann als Nacherfüllung nach seiner Wahl die "
     "Beseitigung des Mangels oder die Lieferung einer mangelfreien Sache verlangen. [wahl]Die Wahl hat also Undine, "
     "nicht Herr Stelzer. [erst]Zuerst wählte sie die Reparatur. [bind]Ist sie daran gebunden? Nach dem "
     "Bundesgerichtshof grundsätzlich nicht. [treu]Die Grenze ziehen Treu und Glauben. [fehl]Hat der Verkäufer den "
     "Mangel nicht fachgerecht beseitigt, darf der Käufer zur Lieferung wechseln. [neu]Undine darf also jetzt ein neues "
     "Handy verlangen.", PS),
    # --- E 2. Ort der Nacherfüllung ----------------------------------------------------------------------------------------
    ("[ort]Und wo muss nacherfüllt werden? [ort1]Es gilt die allgemeine Regel des Paragrafen zweihundertneunundsechzig. "
     "[ort2]Bei Geschäften des täglichen Lebens, etwa beim Kauf im Laden, liegt der Ort nach dem Bundesgerichtshof "
     "regelmäßig beim Verkäufer. [ort3]Undine bringt das Handy also in den Laden. [kost]Die Kosten der Nacherfüllung "
     "trägt Herr Stelzer, Paragraf vierhundertneununddreißig Absatz zwei.", PS),
    # --- F 3. Verweigerung, § 439 Abs. 4 (Wortlautkarte) -------------------------------------------------------------------
    ("[p4]Darf Herr Stelzer das neue Handy verweigern? [p4w]Paragraf vierhundertneununddreißig Absatz vier: Der Verkäufer "
     "kann die vom Käufer gewählte Art der Nacherfüllung verweigern, wenn sie nur mit unverhältnismäßigen Kosten möglich "
     "ist. [krit]Abzuwägen sind vor allem der Wert der Sache in mangelfreiem Zustand, die Bedeutung des Mangels und ob "
     "der Käufer ohne erhebliche Nachteile auf die andere Art zurückgreifen könnte. [rel]Relativ unverhältnismäßig ist die "
     "gewählte Art, wenn sie im Vergleich zur anderen zu teuer ist. Dann bleibt dem Käufer die andere Art. [abs]Absolut "
     "unverhältnismäßig ist sie, wenn sie schon für sich allein zu teuer ist.", PS),
    ("[rsub]Herr Stelzer vergleicht vierhundertfünfzig mit sechzig Euro, also die relative Seite. [bgh2]Doch nach dem "
     "Bundesgerichtshof darf der Verkäufer nicht auf die Reparatur verweisen, wenn er den Mangel damit nicht vollständig, "
     "nachhaltig und fachgerecht beseitigen kann. [zwei]Zwei Reparaturen sind gescheitert. Auf eine dritte muss sich "
     "Undine nicht verweisen lassen. [asub]Und absolut? Vierhundertfünfzig Euro für ein Handy, das mangelfrei "
     "sechshundert Euro wert ist, sind nicht unverhältnismäßig. [verw]Herr Stelzer kann also nicht verweigern. [v219]Bei "
     "eingebauten Sachen kommen Ausbau und Einbau hinzu, dazu gibt es eine eigene Folge.", PS),
    # --- G 4. Fehlschlagen, § 440 (Wortlautkarte) --------------------------------------------------------------------------
    ("[ruek]Kann Undine sogar gleich zurücktreten oder mindern? [frist]Dafür braucht es grundsätzlich eine "
     "erfolglose Frist zur Nacherfüllung. [p440]Paragraf vierhundertvierzig macht sie unter anderem entbehrlich, wenn die "
     "Nacherfüllung fehlgeschlagen ist. [p440s2]Und Satz zwei: Eine Nachbesserung gilt nach dem erfolglosen zweiten "
     "Versuch als fehlgeschlagen, wenn sich nicht insbesondere aus der Art der Sache oder des "
     "Mangels oder den sonstigen Umständen etwas anderes ergibt. "
     "[regel]Zwei Versuche sind also eine Regel, keine feste Grenze.", PS),
    # --- H Beim Verbraucher: § 475d Abs. 1 Nr. 2, § 475 Abs. 4 --------------------------------------------------------------
    ("[vgk]Undine ist aber Verbraucherin. Für ihren Rücktritt gilt Paragraf vierhundertfünfundsiebzig d, nicht "
     "Paragraf vierhundertvierzig. [p475d]Eine Frist braucht es danach nicht, wenn sich trotz der vom Unternehmer "
     "versuchten Nacherfüllung ein Mangel zeigt. [anz]Eine feste Zahl an Versuchen gibt es hier nicht, es kommt auf den "
     "Einzelfall an. [usub]Nach zwei gescheiterten Reparaturen muss Undine keinen dritten Versuch abwarten. [info]Bei "
     "Käufen ab dem einunddreißigsten Juli zweitausendsechsundzwanzig muss der Händler vor der Nacherfüllung über das "
     "Wahlrecht informieren und darüber, dass eine Reparatur die Verjährung einmalig um zwölf Monate verlängert.", PS),
    # --- I Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Undine kann von Herrn Stelzer ein neues Handy verlangen. [erg2]Sie kann aber auch ohne weitere Frist "
     "zurücktreten, der Mangel ist erheblich. Dann gibt sie das Handy zurück und erhält den Kaufpreis, Zug um Zug. "
     "[erg3]Oder sie mindert den Kaufpreis.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne zwei Ebenen. Erst der Anspruch auf Nacherfüllung: Wahlrecht, Ort und die Einrede aus "
     "Absatz vier, die der Verkäufer erheben muss. [tipp2]Dann Rücktritt und Minderung: Ist die Frist entbehrlich? "
     "[tipp3]Beim Verbrauchsgüterkauf steht das in Paragraf vierhundertfünfundsiebzig d.", PS),
    # --- K Prüfungsschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Undine gegen Herrn Stelzer auf Lieferung eines neuen Handys, Paragraf "
     "vierhundertsiebenunddreißig Nummer eins mit Paragraf vierhundertneununddreißig Absatz eins. [k1]Römisch eins: "
     "Kaufvertrag und Sachmangel bei Gefahrübergang. [k2]Römisch zwei: Wahl der Lieferung, der Wechsel "
     "ist erlaubt. [k3]Römisch drei: Nacherfüllungsverlangen am richtigen Ort, im Laden. [k4]Römisch vier: keine "
     "Verweigerung nach Absatz vier. [k5]Römisch fünf: Ergebnis. Undine hat Anspruch auf ein neues Handy. [k6]Alternativ: "
     "Rücktritt ohne weitere Frist nach Paragraf vierhundertfünfundsiebzig d.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei der Nacherfüllung wählt der Käufer. Der Verkäufer kann nur ausnahmsweise verweigern, vor allem bei "
     "unverhältnismäßigen Kosten. [merk2]Nach zwei gescheiterten Versuchen gilt die Nachbesserung in der Regel als "
     "fehlgeschlagen, beim Verbraucher entscheidet der Einzelfall.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\bAGB\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"Undines|Stelzers", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
