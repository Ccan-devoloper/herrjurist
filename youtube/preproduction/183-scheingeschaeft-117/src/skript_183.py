"""Folge 183 · Scheingeschäft § 117 BGB: Schwarzgeld beim Hauskauf – welcher Preis? (Fr · Klausurpraxis · Klassiker-Fall,
BGB AT). Fall nach dem Plan-Hook („Im Notarvertrag stehen 300.000 Euro, vereinbart sind 350.000 – 50.000 fließen bar unter
der Hand“): Markus kauft von Frau Meinhardt ein Haus. Vereinbart sind 350.000 €; auf ihren Vorschlag werden nur 300.000 €
beurkundet, 50.000 € bekommt sie vorher bar im Umschlag. Im selben Termin wird die Auflassung erklärt; Wochen später wird
Markus eingetragen.
Prüfung in vier Schritten: 1. beurkundeter Vertrag – § 117 Abs. 1 (Wortlaut), nichtig (BGH V ZR 221/10 Rn. 6);
2. verdeckter Vertrag – § 117 Abs. 2 (Wortlaut); 3. Form – § 311b Abs. 1 S. 1 (Wortlaut), Umfang (V ZR 122/10 Rn. 6),
§ 125 S. 1 (Wortlaut), formnichtig (V ZR 115/22 Rn. 8), Verweis 050; 4. Heilung – § 311b Abs. 1 S. 2 (Wortlaut),
V ZR 115/22 Rn. 8, ex nunc (V ZR 122/10 Rn. 6), Willensübereinstimmung bei Auflassung (V ZR 265/14 Rn. 29), nur Formmangel
(V ZR 115/22 Rn. 10), Verweis 145; Folgen vor/nach der Eintragung (§ 812, V ZR 122/10 Rn. 15); Hinweis Steuer (V ZR 115/22
Rn. 13, 18) und Barzahlungsverbot § 16a GwG (V ZR 115/22 Rn. 12 offengelassen); Abgrenzung §§ 118, 116 (Wortlaut);
Klausurtipp, Schema, Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Markus (stephan), Frau Meinhardt (hilde); Notar ohne Namen und ohne Rede;
Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter. Kein Genitiv eines Namens."""

P, PS = 0.3, 0.5

STIMMEN = {"Markus": "stephan", "Meinhardt": "hilde"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: die Absprache --------------------------------------------------------------------------------------------
    ("[fall]Markus kauft ein Haus. [verk]Es gehört Frau Meinhardt. [preis]Die beiden einigen sich auf "
     "dreihundertfünfzigtausend Euro. [vorher]Vor dem Notartermin sagt Frau Meinhardt:", 0.25),
    ("[mh1]In den Vertrag schreiben wir nur dreihunderttausend. Den Rest geben Sie mir bar.", 0.25, "Meinhardt"),
    ("[ma1]Gut. Die fünfzigtausend bekommen Sie vorher im Umschlag.", 0.3, "Markus"),
    # --- A2 Fall: beim Notar -------------------------------------------------------------------------------------------------
    ("[umschl]So geschieht es. [notar]Beim Notar steht im Vertrag: Kaufpreis dreihunderttausend Euro. [unter]Beide "
     "unterschreiben [aufl]und erklären im selben Termin die Auflassung. [eintr]Wochen später wird Markus als Eigentümer "
     "ins Grundbuch eingetragen.", 0.3),
    ("[frage]Welcher Vertrag gilt hier, [f2]und zu welchem Preis?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.8),
    # --- C Aufbau -----------------------------------------------------------------------------------------------------------
    ("[plan]Wir prüfen in vier Schritten: [s1]den beurkundeten Vertrag, [s2]den verdeckten Vertrag, [s3]die Form "
     "[s4]und die Heilung.", PS),
    # --- D 1. Beurkundeter Vertrag: § 117 Abs. 1 ----------------------------------------------------------------------------
    ("[k1]Erstens: der beurkundete Vertrag über dreihunderttausend Euro. Paragraf hundertsiebzehn Absatz eins: "
     "[w117]Wird eine Willenserklärung, die einem anderen gegenüber abzugeben ist, mit dessen Einverständnis nur zum Schein "
     "abgegeben, so ist sie nichtig.", P),
    ("[schein]Ein Scheingeschäft liegt vor, wenn das Erklärte nach dem übereinstimmenden Willen beider keine Geltung haben "
     "soll. [fall1]So ist es hier: Keiner der beiden will die dreihunderttausend als Preis. [nicht1]Der beurkundete "
     "Vertrag ist nichtig.", PS),
    # --- E 2. Verdeckter Vertrag: § 117 Abs. 2 ------------------------------------------------------------------------------
    ("[k2]Zweitens: der verdeckte Vertrag über dreihundertfünfzigtausend Euro. Absatz zwei: [w1172]Wird durch ein "
     "Scheingeschäft ein anderes Rechtsgeschäft verdeckt, so finden die für das verdeckte Rechtsgeschäft geltenden "
     "Vorschriften Anwendung. [gewollt]Den Kauf zu dreihundertfünfzigtausend wollen beide wirklich. [regeln]Wirksam ist "
     "er damit aber noch nicht: Er muss nach seinen eigenen Regeln bestehen.", PS),
    # --- F 3. Form: § 311b Abs. 1 S. 1, § 125 S. 1 -------------------------------------------------------------------------
    ("[k3]Drittens: die Form. Paragraf dreihundertelf b Absatz eins Satz eins: [w311]Ein Vertrag, durch den sich der eine "
     "Teil verpflichtet, das Eigentum an einem Grundstück zu übertragen oder zu erwerben, bedarf der notariellen "
     "Beurkundung. [alle]Beurkundet werden müssen alle Vereinbarungen, aus denen sich der Kauf zusammensetzt, also auch der "
     "wahre Preis. [nurs]Beurkundet ist aber nur der Scheinpreis.", P),
    ("[w125]Und Paragraf hundertfünfundzwanzig Satz eins: Ein Rechtsgeschäft, welches der durch Gesetz vorgeschriebenen "
     "Form ermangelt, ist nichtig. [fn]Der wahre Kauf ist also zunächst formnichtig. [verw050]Wie Paragraf "
     "hundertfünfundzwanzig bei der Schriftform wirkt, zeigt das Video zur Kündigung per WhatsApp.", PS),
    # --- G 4. Heilung: § 311b Abs. 1 S. 2 ----------------------------------------------------------------------------------
    ("[k4]Viertens: die Heilung. Nach Satz zwei wird der Vertrag [w311b]seinem ganzen Inhalt nach gültig, wenn die "
     "Auflassung und die Eintragung in das Grundbuch erfolgen. [verw145]Wie beides abläuft, zeigt das Video zum "
     "Hauskauf in drei Schritten.", P),
    ("[ganz]Seinem ganzen Inhalt nach heißt: mit dem wahren Preis. [bgh]So hat der Bundesgerichtshof zweitausendvierundzwanzig "
     "bei einer Schwarzgeldabrede entschieden: Der Formmangel des gewollten Vertrags wurde durch Auflassung und Eintragung "
     "geheilt. [exn]Die Heilung wirkt nur für die Zukunft, [fort]und die Einigung muss bei der Auflassung noch bestehen. "
     "[nurf]Andere Nichtigkeitsgründe heilt sie nicht.", PS),
    # --- H Folgen: vor und nach der Eintragung -----------------------------------------------------------------------------
    ("[vor]Was heißt das für die beiden? Angenommen, der Kauf platzt vor der Eintragung. [vorm]Dann sagt Markus:", 0.2),
    ("[ma2]Dann will ich meine fünfzigtausend zurück.", 0.25, "Markus"),
    ("[unw]Bis zur Eintragung ist der Vertrag unwirksam: Frau Meinhardt muss das Haus nicht übereignen. [r812]Und Markus "
     "kann das Geld grundsätzlich nach Paragraf achthundertzwölf zurückverlangen, denn es floss ohne Rechtsgrund. "
     "[nach]Nach der Eintragung ist es anders. [nachm]Jetzt sagt Frau Meinhardt:", 0.2),
    ("[mh2]Der Vertrag war doch nichtig. Ich will mein Haus zurück!", 0.25, "Meinhardt"),
    ("[geb]Ohne Erfolg: Der Vertrag ist geheilt und gilt mit dreihundertfünfzigtausend Euro. Beide sind daran gebunden, "
     "und Markus ist Eigentümer.", PS),
    # --- I Hinweise: Steuer, Barzahlungsverbot -----------------------------------------------------------------------------
    ("[steuer]Nebenbei: Wer so Grunderwerbsteuer verkürzt, kann sich wegen Steuerhinterziehung strafbar machen; den "
     "Kaufvertrag macht das nach dem Bundesgerichtshof aber in der Regel nicht nichtig. [gwg]Und seit April "
     "zweitausenddreiundzwanzig kann der Kaufpreis einer Immobilie nach Paragraf sechzehn a Geldwäschegesetz nicht mehr "
     "mit Bargeld bezahlt werden. [gwg2]Bar Übergebenes tilgt den Preis nicht, der Käufer kann es nach Bereicherungsrecht "
     "herausverlangen. [offen]Ob das den Vertrag selbst berührt, hat der Bundesgerichtshof offengelassen.", PS),
    # --- J Abgrenzung: §§ 118, 116 ------------------------------------------------------------------------------------------
    ("[abgr]Zur Abgrenzung: [w118]Beim Scherzgeschäft nach Paragraf hundertachtzehn erwartet der Erklärende, dass man den "
     "fehlenden Ernst erkennt; die Erklärung ist nichtig. [w116]Beim geheimen Vorbehalt nach Paragraf hundertsechzehn will "
     "nur einer insgeheim nicht. Die Erklärung bleibt wirksam, außer der andere kennt den Vorbehalt. [beide]Beim "
     "Scheingeschäft sind sich dagegen beide einig, dass das Erklärte nicht gelten soll.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe getrennt und in dieser Reihenfolge: [t1]das Scheingeschäft, [t2]das verdeckte Geschäft, "
     "[t3]die Form [t4]und die Heilung. [t5]Und denk daran: Geheilt wird nur der verdeckte Vertrag. Der Scheinvertrag "
     "bleibt nichtig.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [kI]Römisch eins: Scheingeschäft nach Paragraf hundertsiebzehn Absatz eins, der beurkundete Vertrag "
     "ist nichtig. [kII]Römisch zwei: das verdeckte Geschäft nach Absatz zwei. [kII1]Eins: Form nach Paragraf "
     "dreihundertelf b Absatz eins Satz eins, [kII2]zwei: Formnichtigkeit nach Paragraf hundertfünfundzwanzig, "
     "[kII3]drei: Heilung durch Auflassung und Eintragung. [kIII]Römisch drei: Ergebnis, es gilt der wahre Preis.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Scheinvertrag ist nichtig. [mk2]Der wahre Vertrag ist formnichtig, [mk3]bis Auflassung und "
     "Eintragung ihn heilen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
