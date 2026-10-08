"""Folge 255 · „Sofort kaufen“ geklickt: Ist der Verkäufer an den Preis gebunden? (Fr · Klausurpraxis · BGB AT · Alltagsfall;
§§ 145, 119 Abs. 1, 133, 157 BGB; zusätzlich § 119 Abs. 2, §§ 122, 143, 433 Abs. 1 Satz 1 BGB).
Beispielfall nach dem Plan-Hook („Du stellst deine Kamera für 900 Euro auf einer Plattform ein – und merkst danach, dass sie
2.500 wert ist“) und der Gesamtwissen-Fundstelle (Teil A – 4., UNCERTIFIED): Herr Eichler (privat) stellt am Montagmorgen
seine seltene Kamera mit festem Preis 900 € und der Schaltfläche „Sofort kaufen“ auf einer Plattform ein (fiktive Plattform,
keine Marke; Plattformregel im Sachverhalt: Kauf kommt mit dem Klick zustande). Frau Hegemann klickt mittags und zahlt.
Abends sieht Herr Eichler, dass vergleichbare Kameras rund 2.500 € kosten; Modell und Zustand kannte er genau. Am nächsten
Tag ficht er an der Haustür an. Gegenfall: Tippfehler 90 statt 900 € (Erklärungsirrtum, Verweis Folge 251, § 122).
Belege je Cue in ../RECHTSSTAND.md: BGH VIII ZR 59/16 Rn. 12, 23 (Sofort-Kaufen = Angebot zum Festpreis, Auslegung mit
Plattform-AGB, Annahme durch Betätigen des Buttons); VIII ZR 305/10 Rn. 15–17 (§§ 145 ff., §§ 133, 157 mit AGB, Bindung
ausschließbar/einschränkbar); VIII ZR 42/14 Rn. 12 (Risiko eines niedrigen Startpreises); VIII ZR 79/04 S. 7–9 (Vertippen =
Erklärungsirrtum; Kalkulationsirrtum = Motivirrtum); OLG Düsseldorf 6 U 168/98 Rn. 34, 3 W 63/25 Rn. 25 (Wert selbst keine
verkehrswesentliche Eigenschaft, nur die wertbildenden Faktoren).
Stimmen (Pool stephan, hilde, christian, lucy): Herr Eichler (stephan, Mann, mittel), Frau Hegemann (lucy, Frau, jung);
hilde und christian nicht besetzt. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Eichler": "stephan", "Hegemann": "lucy"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: Herr Eichler stellt die Kamera ein (Wohnzimmer) ----------------------------------------------------------
    ("[fall]Stell dir vor, du stellst deine Kamera für neunhundert Euro auf einer Plattform ein. Und danach merkst du: "
     "Sie ist zweitausendfünfhundert wert. [eichler]Genau das passiert Herrn Eichler. [anzeige]Er stellt am Montagmorgen "
     "seine seltene Kamera ein, zu einem festen Preis von neunhundert Euro und mit der Schaltfläche Sofort kaufen. "
     "[regel]Nach den Regeln der Plattform kommt der Kauf zustande, sobald jemand darauf klickt.", P),
    # --- A2 Frau Hegemann klickt (Parkbank) --------------------------------------------------------------------------
    ("[park]Am Mittag sieht Frau Hegemann die Anzeige. [klick]Sie klickt auf Sofort kaufen [zahlt]und bezahlt die "
     "neunhundert Euro gleich.", P),
    # --- A3 Abends: Vergleichspreise ----------------------------------------------------------------------------------
    ("[abend]Am Abend schaut sich Herr Eichler andere Angebote an. [vergleich]Vergleichbare Kameras kosten dort rund "
     "zweitausendfünfhundert Euro. [modell]Welches Modell er verkauft und in welchem Zustand es ist, wusste er genau. Nur den "
     "Marktpreis hat er unterschätzt.", P),
    # --- A4 Haustür: Dialog ------------------------------------------------------------------------------------------
    ("[tuer]Am nächsten Tag will Frau Hegemann die Kamera abholen.", P),
    ("[e1]Ich habe den Wert völlig unterschätzt. Ich fechte den Kauf an.", P, "Eichler"),
    ("[h1]Ich habe auf Sofort kaufen geklickt und bezahlt. Ich will die Kamera.", P, "Hegemann"),
    ("[frage]Ist Herr Eichler an seinen Preis gebunden? [frage2]War sein Angebot schon verbindlich? [frage3]Und darf er "
     "anfechten, weil er den Wert falsch eingeschätzt hat?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch und Aufbau ---------------------------------------------------------------------------------------
    ("[ansp]Frau Hegemann verlangt von Herrn Eichler Übergabe und Übereignung der Kamera, nach Paragraf "
     "vierhundertdreiunddreißig Absatz eins. [aufbau]Du prüfst zwei Stufen: Ist ein Kaufvertrag zu neunhundert Euro "
     "zustande gekommen? [aufbau2]Und hat Herr Eichler ihn wirksam angefochten?", P),
    # --- D1 I. Angebot durch Einstellen mit Sofort kaufen (VIII ZR 59/16 Rn. 12; VIII ZR 305/10 Rn. 15 f.) --------------
    ("[ang]Römisch eins: der Vertragsschluss, zuerst das Angebot. [v251]In unserer Folge zum Preisfehler im Onlineshop war "
     "die Shopseite nur eine Einladung, selbst ein Angebot abzugeben. [sofort]Bei Sofort kaufen ist das anders: Nach dem "
     "Bundesgerichtshof bietet der Verkäufer die Sache damit selbst zu einem festen Preis an. [ausl]Das ergibt die "
     "Auslegung nach den Paragrafen hundertdreiunddreißig und hundertsiebenundfünfzig, und dabei zählen auch die Regeln der "
     "Plattform. [jeder]Hier soll der Kauf mit dem Klick zustande kommen, ohne dass Herr Eichler noch einmal entscheidet. "
     "Sein Angebot richtet sich also an jeden, der zuerst klickt. Juristen sagen: ein Angebot ad incertas personas.", P),
    # --- D2 § 145 BGB (Wortlautkarte), Bindung (VIII ZR 305/10 Rn. 17) -------------------------------------------------
    ("[w145]Paragraf hundertfünfundvierzig sagt: Wer einem anderen die Schließung eines Vertrags anträgt, ist an den Antrag "
     "gebunden, es sei denn, dass er die Gebundenheit ausgeschlossen hat. [ausschl]Ausschließen oder einschränken darf der "
     "Verkäufer die Bindung also; das hat der Bundesgerichtshof für Auktionen ausdrücklich gesagt. [nicht]Herr Eichler hat "
     "aber nichts dergleichen erklärt. Sein Angebot war verbindlich.", P),
    # --- D3 Annahme durch den Klick (VIII ZR 59/16 Rn. 23) --------------------------------------------------------------
    ("[klick2]Mit ihrem Klick hat Frau Hegemann das Angebot ohne Vorbehalt angenommen; so sieht es auch der "
     "Bundesgerichtshof. [vertrag]Der Kaufvertrag ist geschlossen, zu neunhundert Euro. [v014]Wie Angebot und Annahme "
     "allgemein funktionieren, zeigt unsere Folge zu genau diesem Thema.", PS),
    # --- E II. Anfechtung: § 119 Abs. 1 BGB (Wortlautkarte) ------------------------------------------------------------
    ("[anf]Römisch zwei: die Anfechtung. Erklärt hat Herr Eichler sie gegenüber Frau Hegemann. Es fehlt nur ein "
     "Anfechtungsgrund. [w119]Nach Paragraf hundertneunzehn Absatz eins kann anfechten, wer über den Inhalt seiner Erklärung "
     "im Irrtum war oder eine Erklärung dieses Inhalts überhaupt nicht abgeben wollte. [wollte]Herr Eichler wollte "
     "neunhundert Euro erklären, und genau das hat er erklärt. [kein1]Wille und Erklärung stimmen überein: kein "
     "Inhaltsirrtum und kein Erklärungsirrtum.", P),
    # --- F § 119 Abs. 2 BGB (Wortlautkarte): Wert keine Eigenschaft (OLG Düsseldorf) -----------------------------------
    ("[w1192]Bleibt Absatz zwei: Als Irrtum über den Inhalt gilt auch der Irrtum über solche Eigenschaften der Person oder "
     "der Sache, die im Verkehr als wesentlich angesehen werden. [wert]Der Wert selbst ist aber keine solche Eigenschaft; so "
     "sehen es die Gerichte. [faktor]In Betracht kommen nur die Umstände, die den Wert bilden, etwa Modell und Zustand der "
     "Kamera. [hier2]Darüber hat sich Herr Eichler nicht geirrt. Er hat nur den Marktpreis falsch eingeschätzt.", P),
    # --- G Motivirrtum, Kalkulationsirrtum (VIII ZR 79/04 S. 8 f.); Risiko (VIII ZR 42/14 Rn. 12) -----------------------
    ("[motiv]Das ist ein Irrtum im Beweggrund, also ein Motivirrtum. [kalk]Wie ein Kalkulationsirrtum berechtigt er "
     "grundsätzlich nicht zur Anfechtung. [risiko]Für Auktionen sagt der Bundesgerichtshof: Wer einen Startpreis unter dem "
     "Marktwert ohne Mindestpreis wählt, geht dieses Risiko selbst ein. Bei einem festen Preis liegt es genauso beim Verkäufer.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Herr Eichler ist an seinen Preis gebunden. [erg2]Er muss Frau Hegemann die Kamera für neunhundert Euro "
     "übergeben und übereignen.", PS),
    # --- I Gegenfall: Tippfehler 90 statt 900 (VIII ZR 79/04 S. 7; § 122) ---------------------------------------------
    ("[gegen]Anders im Gegenfall: Herr Eichler will neunhundert Euro eintippen, vertippt sich aber, und in der Anzeige stehen "
     "neunzig. [tipp90]Dann fallen Wille und Erklärung auseinander: ein Erklärungsirrtum nach Paragraf hundertneunzehn Absatz "
     "eins, zweite Alternative, wie in unserer Folge zum Preisfehler im Onlineshop. [p122]Ficht er unverzüglich an, ist der "
     "Vertrag nichtig. Frau Hegemann bekommt dann nach Paragraf hundertzweiundzwanzig grundsätzlich nur ihren "
     "Vertrauensschaden ersetzt.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lege Wille und Erklärung nebeneinander. [tipp2]Stimmen sie überein, bleibt nur ein Irrtum im "
     "Beweggrund, und der ist grundsätzlich unbeachtlich. [tipp3]Bei Absatz zwei trennst du sauber: Der Wert selbst ist "
     "keine Eigenschaft, die Umstände, die ihn bilden, schon.", PS),
    # --- L Prüfungsschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Frau Hegemann gegen Herrn Eichler auf Übergabe und Übereignung. [s1]Römisch eins: "
     "Kaufvertrag, [s1a]Angebot durch Einstellen mit Sofort kaufen, bindend nach Paragraf hundertfünfundvierzig, "
     "[s1b]Annahme durch den Klick. [s2]Römisch zwei: Nichtigkeit durch Anfechtung, [s2a]kein Inhalts- oder "
     "Erklärungsirrtum, [s2b]kein Eigenschaftsirrtum, nur ein unbeachtlicher Motivirrtum. [s3]Römisch drei: Ergebnis, der "
     "Anspruch besteht.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer mit Sofort kaufen einstellt, macht in der Regel ein verbindliches Angebot. [merk2]Und wer nur den Wert falsch "
     "einschätzt, kann nicht nach Paragraf hundertneunzehn anfechten. Das Risiko des zu niedrigen Preises trägt er selbst.",
     1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
