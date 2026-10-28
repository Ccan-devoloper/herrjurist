"""Folge 023 · Anfechtung Schema §§ 119 ff. BGB: Die Prüfung in 5 Schritten (Examenswissen, Format Schema).
Beispielfall (frei erfunden, Plan-Hook „vertippt, 100 statt 10“): Buchhändlerin Ilse bestellt per E-Mail beim Großhändler
Winkler hundert statt zehn Kartons Kalender (Erklärungsirrtum, § 119 I Alt. 2), Winkler nimmt an und bucht eine Spedition;
Ilse ficht sofort telefonisch an. Fünf Schritte (Klausurkonvention): 1. Anfechtungsgegenstand (nach Auslegung),
2. Anfechtungsgrund mit Kausalität (§§ 119 I, II, 120, 123), 3. Anfechtungserklärung gegenüber dem Gegner (§ 143),
4. Frist (§§ 121, 124), 5. kein Ausschluss (§ 144). Rechtsfolge § 142 I, Vertrauensschaden § 122.
Gegenfälle: Motivirrtum (Stadtfest abgesagt), Kalkulationsirrtum (BGH X ZR 32/14), arglistige Täuschung beim Kauf eines
Lieferwagens (Jörg, „unfallfrei“). Wortlautkarten: § 142 I, § 119 I, § 119 II BGB.
Fiktive Figuren: Ilse (Buchhändlerin), Herr Winkler (Großhändler), Jörg (Verkäufer des Lieferwagens).
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Ilse": "lisa", "Winkler": "christian", "Joerg": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Bestellung im Buchladen -----------------------------------------------------------------------
    ("[fall]Ilse führt einen kleinen Buchladen. [bestell]Am Montagabend bestellt sie per E-Mail beim Großhändler "
     "Winkler Kalender. [null]Sie will zehn Kartons, tippt aber eine Null zu viel: hundert Kartons, zu je zwanzig Euro.", 0.3),
    # --- B Fall: Annahme, Anruf, Streit --------------------------------------------------------------------------
    ("[annahme]Herr Winkler nimmt die Bestellung am Dienstagmorgen per E-Mail an und bucht gleich eine Spedition. "
     "[merkt]Ilse liest seine Antwort um neun Uhr, erschrickt und ruft sofort an.", 0.3),
    ("[i1]Herr Winkler, ich habe mich vertippt! Ich wollte zehn Kartons, nicht hundert. Diese Bestellung lasse ich so "
     "nicht gelten.", 0.4, "Ilse"),
    ("[w1]Bestellt ist bestellt. Sie schulden mir zweitausend Euro!", 0.4, "Winkler"),
    ("[frage]Muss Ilse zahlen? Ihre Rettung heißt Anfechtung. Wir prüfen sie in fünf Schritten.", 0.6),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Anspruch und Rechtsfolge § 142 I ------------------------------------------------------------------------
    ("[ansp]Herr Winkler verlangt den Kaufpreis nach Paragraf vierhundertdreiunddreißig Absatz zwei. [vertrag]Ein "
     "Kaufvertrag über hundert Kartons ist zunächst geschlossen. [nichtig]Er fällt aber weg, wenn die Anfechtung durch Ilse wirksam ist. "
     "[p142]Paragraf hundertzweiundvierzig Absatz eins: Wird ein anfechtbares Rechtsgeschäft angefochten, so ist es als "
     "von Anfang an nichtig anzusehen.", PS),
    # --- E 1. Anfechtungsgegenstand ----------------------------------------------------------------------------------
    ("[s1]Schritt eins: der Anfechtungsgegenstand. Das ist eine Willenserklärung, hier die Bestellung. [ausleg]Zuerst legst du aus, "
     "Paragrafen hundertdreiunddreißig und hundertsiebenundfünfzig. Maßgeblich ist, wie Herr Winkler die Mail verstehen "
     "musste. [hundert]Von einem Tippfehler wusste er nichts. Also gilt objektiv: hundert Kartons. [s1ok]Genau diese "
     "Erklärung will Ilse anfechten.", PS),
    # --- F 2. Anfechtungsgrund: § 119 I, Kausalität ------------------------------------------------------------------
    ("[s2]Schritt zwei: der Anfechtungsgrund. [p119]Paragraf hundertneunzehn Absatz eins nennt zwei Irrtümer. "
     "[inhalt]Beim Inhaltsirrtum sagt man, was man sagen will, irrt aber über die Bedeutung. [erkl]Beim "
     "Erklärungsirrtum wollte man eine Erklärung dieses Inhalts überhaupt nicht abgeben: Man verspricht oder vertippt "
     "sich. [ilse]Genau das ist Ilse passiert.", P),
    ("[kaus]Dazu kommt die Kausalität: Bei Kenntnis der Sachlage und bei verständiger Würdigung hätte Ilse so nicht "
     "bestellt. [kaus2]Hundert Kartons für einen kleinen Laden: Weder sie noch ein vernünftiger Dritter hätte das gewollt.", PS),
    # --- G weitere Gründe: § 119 II, § 120, § 123 -------------------------------------------------------------------
    ("[weitere]Weitere Gründe: [p119b]Nach Absatz zwei zählt auch der Irrtum über Eigenschaften einer Person oder "
     "Sache, die im Verkehr als wesentlich angesehen werden. [p120]Paragraf hundertzwanzig erfasst die falsche "
     "Übermittlung, etwa durch einen Boten. [p123]Und Paragraf hundertdreiundzwanzig erfasst arglistige Täuschung und "
     "widerrechtliche Drohung.", PS),
    # --- H Gegenfall Motivirrtum, Kalkulationsirrtum -----------------------------------------------------------------
    ("[motiv]Gegenfall: Ilse bestellt bewusst hundert Kartons, weil sie auf das Stadtfest hofft. Dann wird das Fest "
     "abgesagt. [motiv2]Jetzt irrt sie nur im Beweggrund, nicht über ihre Erklärung. Dieser Motivirrtum berechtigt "
     "nicht zur Anfechtung. [kalk]Ähnlich beim internen Rechenfehler: Nach dem Bundesgerichtshof bleibt man "
     "grundsätzlich gebunden. [treu]Treuwidrig kann es aber sein, auf dem Vertrag zu bestehen, obwohl man den erheblichen "
     "Kalkulationsirrtum erkannt hat.", PS),
    # --- I 3. Anfechtungserklärung § 143 -----------------------------------------------------------------------------
    ("[s3]Schritt drei: die Anfechtungserklärung gegenüber dem Anfechtungsgegner, Paragraf hundertdreiundvierzig. "
     "[gegner]Bei einem Vertrag ist das der andere Teil, hier Herr Winkler. [wort]Das Wort anfechten muss nicht fallen. "
     "Nach dem Bundesgerichtshof genügt, wenn Ilse unzweideutig zeigt, dass sie den Vertrag wegen ihres Irrtums nicht gelten lassen will. "
     "[s3ok]Ich habe mich vertippt, ich lasse das so nicht gelten: Das reicht.", PS),
    # --- J 4. Anfechtungsfrist §§ 121, 124 --------------------------------------------------------------------------
    ("[s4]Schritt vier: die Anfechtungsfrist. [p121]Beim Irrtum muss Ilse nach Paragraf hunderteinundzwanzig "
     "unverzüglich anfechten, also ohne schuldhaftes Zögern, sobald sie den Fehler kennt. [s4ok]Sie rief sofort an: "
     "rechtzeitig. [p124]Bei Täuschung oder Drohung gilt dagegen ein Jahr, Paragraf hundertvierundzwanzig. [zehn]Und "
     "zehn Jahre nach Abgabe der Erklärung ist die Anfechtung in beiden Fällen ausgeschlossen.", PS),
    # --- K 5. kein Ausschluss § 144 -----------------------------------------------------------------------------------
    ("[s5]Schritt fünf: kein Ausschluss. [p144]Nach Paragraf hundertvierundvierzig ist die Anfechtung ausgeschlossen, "
     "wenn Ilse das Geschäft bestätigt. [bsp]Hätte sie in Kenntnis ihres Anfechtungsrechts geschrieben: Schicken Sie ruhig die "
     "hundert, wäre das eine Bestätigung. [s5ok]Das hat sie nicht getan.", PS),
    # --- L Rechtsfolge, § 122 -----------------------------------------------------------------------------------------
    ("[folge]Damit ist der Kaufvertrag von Anfang an nichtig. Herr Winkler bekommt keine zweitausend Euro. "
     "[p122]Weil er den Tippfehler nicht erkennen konnte, muss Ilse ihm aber nach Paragraf hundertzweiundzwanzig den "
     "Vertrauensschaden ersetzen. [spedi]Das sind die achtzig Euro für die Spedition, die er nicht mehr stornieren kann. "
     "[gewinn]Seinen Gewinn aus dem Geschäft bekommt er nicht. Das wäre das Erfüllungsinteresse, und das ist nur die "
     "Obergrenze.", PS),
    # --- M Gegenfall § 123: der Lieferwagen ----------------------------------------------------------------------------
    ("[jg]Zum Schluss die Täuschung: Ilse kauft von Jörg einen gebrauchten Lieferwagen.", 0.3),
    ("[j1]Der ist unfallfrei, versprochen!", 0.4, "Joerg"),
    ("[unfall]Jörg weiß aber von einem schweren Unfall. Ilse erfährt es ein halbes Jahr später in der Werkstatt. "
     "[t123]Das ist arglistige Täuschung: Jörg spiegelt bewusst eine falsche Tatsache vor, damit Ilse kauft. "
     "[t124]Ilse hat ab der Entdeckung ein Jahr Zeit, Paragraf hundertvierundzwanzig. [t122]Schadensersatz nach "
     "Paragraf hundertzweiundzwanzig schuldet sie nicht. Die Norm erfasst nur die Anfechtung nach den Paragrafen "
     "hundertneunzehn und hundertzwanzig.", PS),
    # --- N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Erst auslegen, dann anfechten. [tipp2]Verstehen beide dasselbe, gilt das übereinstimmend "
     "Gewollte, auch wenn sich jemand verschrieben hat. Wussten beide, dass zehn Kartons gemeint sind, gibt es nichts "
     "anzufechten. [tipp3]Und die fünf Schritte sind Klausurkonvention, kein Gesetzestext.", PS),
    # --- O Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Winkler gegen Ilse aus Paragraf vierhundertdreiunddreißig Absatz zwei. [k1]Römisch eins: "
     "Kaufvertrag geschlossen. [k2]Römisch zwei: nichtig nach Paragraf hundertzweiundvierzig Absatz eins? [k21]Eins: "
     "Anfechtungsgegenstand. [k22]Zwei: Anfechtungsgrund mit Kausalität. [k23]Drei: Anfechtungserklärung gegenüber dem "
     "Gegner. [k24]Vier: Anfechtungsfrist. [k25]Fünf: kein Ausschluss. [k3]Römisch drei: Ergebnis. Kein Kaufpreis, "
     "aber Vertrauensschaden nach Paragraf hundertzweiundzwanzig.", PS),
    # --- P Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer wirksam anficht, vernichtet das Geschäft von Anfang an. [m2]Wer wegen eines Irrtums anficht, "
     "ersetzt den Vertrauensschaden, es sei denn, der andere kannte den Fehler oder musste ihn kennen.", 1.4),
]
