"""Folge 245 · Leistungskondiktion § 812 I 1 Alt. 1 BGB – Prüfungsschema (Mi · Examenswissen · Bereicherungsrecht · Schema;
§ 812 Abs. 1 Satz 1 Alt. 1 BGB). Beispielfall nach dem Plan-Hook („Der Kaufvertrag über das Klavier war nichtig – du hattest
aber schon bezahlt“): Frau Heidkamp vertippt sich in ihrem schriftlichen Angebot (2.400 € statt 4.200 €), Mila nimmt an,
zahlt bar, das Klavier steht bei ihr; Frau Heidkamp ficht wegen Erklärungsirrtums (§ 119 Abs. 1 Alt. 2 BGB) an.
Nichtigkeitsgrund bewusst Anfechtung (§ 142 Abs. 1 BGB) und nicht Geschäftsunfähigkeit: Die Übereignung des Geldes bleibt
wirksam (etwas erlangt = Eigentum und Besitz an den Scheinen), kein Schutz nicht voll Geschäftsfähiger und keine Arglist,
die die Saldotheorie begrenzen würden (BGH V ZR 266/11 Rn. 23; XI ZR 234/14 Rn. 25). Belege je Cue in ../RECHTSSTAND.md.
Leitentscheidungen (Volltext, Rn.): BGH VIII ZR 39/17 Rn. 16 f. (Vorrang, Leistungsbegriff), III ZR 291/11 Rn. 24, V ZR 52/12
Rn. 28 (Saldotheorie), V ZR 55/13 Rn. 19 und VIII ZR 37/24 Rn. 41 f. (Rückabwicklung nach Anfechtung über Alt. 1).
Stimmen (Pool stephan, hilde, christian, lucy): Mila (lucy, Frau, jung), Frau Heidkamp (hilde, Frau, älter); stephan und
christian nicht besetzt. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Mila": "lucy", "Heidkamp": "hilde"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: Mila im Wohnzimmer mit dem Klavier, Frau Heidkamp klingelt ------------------------------------------------
    ("[fall]Mila hat sich einen Traum erfüllt: [klavier]Seit einer Woche steht ein gebrauchtes Klavier in ihrem Wohnzimmer. "
     "[klingel]Da klingelt die Verkäuferin, Frau Heidkamp.", P),
    ("[h1]Ich habe mich in meinem Angebot vertippt: Das Klavier sollte viertausendzweihundert Euro kosten, nicht "
     "zweitausendvierhundert. Ich fechte den Kauf an.", P, "Heidkamp"),
    ("[m1]Aber ich habe doch schon bezahlt!", P, "Mila"),
    # --- A2 Rückblick: bei Frau Heidkamp ----------------------------------------------------------------------------------
    ("[rueck]Zwei Wochen vorher. [angebot]Frau Heidkamp hatte Mila geschrieben: Sie können das Klavier für "
     "zweitausendvierhundert Euro haben. [zusage]Mila sagte sofort zu. [bar]Beim Abholen zahlte sie bar, [konto]und Frau "
     "Heidkamp zahlte die Scheine noch am selben Tag auf ihr Konto ein.", P),
    # --- A3 Zurück im Wohnzimmer: Rückforderung und Gegenforderung --------------------------------------------------------
    ("[mi2]Dann will ich meine zweitausendvierhundert Euro zurück.", P, "Mila"),
    ("[h2]Die bekommen Sie. Aber nur, wenn ich mein Klavier wiederbekomme.", P, "Heidkamp"),
    ("[frage]Der Kaufvertrag ist nichtig, aber Mila hat schon bezahlt. Kann sie ihr Geld zurückverlangen? [frage2]Und muss "
     "sie dafür das Klavier hergeben?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruchsgrundlage (Wortlautkarte § 812 Abs. 1 Satz 1 BGB) ------------------------------------------------------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertzwölf Absatz eins Satz eins, erste Alternative: die "
     "Leistungskondiktion, genauer die condictio indebiti. [w812]Wer durch die Leistung eines anderen etwas ohne rechtlichen "
     "Grund erlangt, ist ihm zur Herausgabe verpflichtet. [schema]Daraus folgt dein Schema: etwas erlangt, durch Leistung, "
     "ohne rechtlichen Grund, und kein Ausschluss.", P),
    # --- D 1. Etwas erlangt (V ZR 119/11 Rn. 17; IX ZR 164/14 Rn. 8) -------------------------------------------------------
    ("[erl]Erstens: Frau Heidkamp muss etwas erlangt haben. [vorteil]Etwas ist jeder vermögenswerte Vorteil. [scheine]Bei "
     "Bargeld sind das Eigentum und Besitz an den Scheinen. [ueber]Denn angefochten hat Frau Heidkamp nur den Kaufvertrag, "
     "nicht die Übereignung des Geldes. [gutschr]Hätte Mila überwiesen, wäre es die Gutschrift auf dem Konto, also ein "
     "Anspruch gegen die Bank.", P),
    # --- E 2. Durch Leistung (III ZR 291/11 Rn. 24; VIII ZR 39/17 Rn. 17) --------------------------------------------------
    ("[leist]Zweitens: durch Leistung. [def]Leistung ist nach dem Bundesgerichtshof die bewusste und zweckgerichtete Mehrung "
     "fremden Vermögens. [bewusst]Mila hat das Geld bewusst übergeben, [zweck]und zwar, um ihre Kaufpreisschuld aus "
     "Paragraf vierhundertdreiunddreißig Absatz zwei zu erfüllen. [horiz]Gehen die Vorstellungen auseinander, entscheidet die "
     "Sicht eines vernünftigen Empfängers. Hier ist der Zweck eindeutig.", P),
    # --- F 3. Ohne rechtlichen Grund (§§ 119, 121, 142, 143; V ZR 55/13 Rn. 19; VIII ZR 37/24 Rn. 41 f.) --------------------
    ("[org]Drittens: ohne rechtlichen Grund. [kv]Rechtsgrund wäre der Kaufvertrag. [irrt]Doch Frau Heidkamp wollte eine "
     "Erklärung dieses Inhalts gar nicht abgeben: Sie hat sich vertippt, ein Erklärungsirrtum nach Paragraf hundertneunzehn "
     "Absatz eins. [anf]Sie hat unverzüglich angefochten. [p142]Damit ist der Kaufvertrag nach Paragraf "
     "hundertzweiundvierzig Absatz eins als von Anfang an nichtig anzusehen. [alt1]Wegen dieser Rückwirkung prüfst du Satz eins, "
     "erste Alternative; so geht auch der Bundesgerichtshof vor.", PS),
    # --- G 4. Kein Ausschluss (Wortlautkarten § 814, § 817 Satz 2; XI ZR 170/13 Rn. 109) ----------------------------------
    ("[aus]Viertens: kein Ausschluss. [w814]Nach Paragraf achthundertvierzehn kann das zum Zwecke der Erfüllung einer "
     "Verbindlichkeit Geleistete nicht zurückgefordert werden, wenn der Leistende gewusst hat, dass er zur Leistung nicht "
     "verpflichtet war. [k814]Das verlangt positive Kenntnis der Rechtslage. Mila wusste beim Zahlen nichts von einem "
     "Irrtum; sie ging davon aus, den Kaufpreis zu schulden.", P),
    ("[w817]Und Paragraf achthundertsiebzehn Satz zwei sperrt die Rückforderung, wenn auch dem Leistenden ein Verstoß gegen "
     "ein gesetzliches Verbot oder die guten Sitten zur Last fällt. [k817]Ein Klavierkauf ist weder verboten noch "
     "sittenwidrig. [tbm]Alle Voraussetzungen liegen also vor.", PS),
    # --- H Rechtsfolge § 818 Abs. 1, 2 (Wortlautkarte), Abs. 3 (XI ZR 158/24 Rn. 18) ----------------------------------------
    ("[rf]Und die Rechtsfolge? [hg]Herauszugeben ist das Erlangte, [w818a]nach Paragraf achthundertachtzehn Absatz eins auch "
     "die gezogenen Nutzungen. [weg]Die Scheine selbst hat Frau Heidkamp aber nicht mehr; sie hat sie bei der Bank "
     "eingezahlt. [w818b]Ist der Empfänger zur Herausgabe außerstande, hat er nach Absatz zwei den Wert zu ersetzen: "
     "[wert]zweitausendvierhundert Euro. [entr]Entreichert nach Absatz drei ist sie nicht, denn der Betrag steckt noch in "
     "ihrem Vermögen.", P),
    # --- I Saldotheorie (V ZR 52/12 Rn. 28; VIII ZR 37/24 Rn. 41) ----------------------------------------------------------
    ("[gegen]Aber auch Mila hat etwas erlangt: das Klavier, durch Leistung von Frau Heidkamp und ohne rechtlichen Grund. "
     "[saldo]Nach der Saldotheorie werden die beiden Ansprüche nicht isoliert betrachtet: Bei Geld gegen Klavier bekommt "
     "Mila ihr Geld nur Zug um Zug gegen Rückgabe und Rückübereignung des Klaviers.", P),
    # --- J Abgrenzung condictio ob rem (XII ZR 190/08 Rn. 31 f.) ------------------------------------------------------------
    ("[orem]Und die condictio ob rem nach Satz zwei, zweite Alternative? Sie setzt eine Einigung über einen bezweckten "
     "Erfolg voraus, den man nicht einfordern kann; [orem2]Mila zahlte dagegen auf eine Kaufpreisschuld.", PS),
    # --- K Ergebnis (zurück im Wohnzimmer) --------------------------------------------------------------------------------
    ("[erg]Ergebnis: Mila kann von Frau Heidkamp zweitausendvierhundert Euro verlangen, [erg2]Zug um Zug gegen Rückgabe und "
     "Rückübereignung des Klaviers.", PS),
    # --- L Klausurtipp (Lexi; VIII ZR 39/17 Rn. 16 f.) ---------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei der Rückabwicklung einer Leistung immer zuerst die Leistungskondiktion; sie hat Vorrang "
     "vor der Nichtleistungskondiktion. [tipp2]Und bestimme Leistenden und Empfänger über den Zweck der Zuwendung, bei "
     "abweichenden Vorstellungen aus der Sicht des Empfängers.", PS),
    # --- M Prüfungsschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema für die Leistungskondiktion. [s1]Eins: etwas erlangt, hier Eigentum und Besitz an den "
     "Scheinen. [s2]Zwei: durch Leistung, also bewusst und zweckgerichtet. [s3]Drei: ohne rechtlichen Grund, hier wegen der "
     "Anfechtung. [s4]Vier: kein Ausschluss nach Paragraf achthundertvierzehn oder achthundertsiebzehn Satz zwei. "
     "[s5]Fünf: Rechtsfolge nach Paragraf achthundertachtzehn: Herausgabe oder Wertersatz, bei beiderseitigen Leistungen nach "
     "der Saldotheorie.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer durch Leistung etwas ohne rechtlichen Grund erlangt, muss es herausgeben. [merk2]Ist ein Kauf "
     "gescheitert, gibt jede Seite zurück, was sie bekommen hat, grundsätzlich Zug um Zug.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
