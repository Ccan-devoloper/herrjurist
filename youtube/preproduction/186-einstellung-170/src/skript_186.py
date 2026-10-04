"""Folge 186 · Einstellung § 170 II StPO: Beschwerde und Klageerzwingung (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall nach dem Plan-Hook („Die Staatsanwaltschaft stellt das Verfahren gegen einen Arzt ein, den eine Patientin wegen
Körperverletzung angezeigt hat“): Am Dienstag, 13.1.2026, wird Frau Rautenberg (um 66) von Augenarzt Doktor Wallner am rechten
Auge operiert; danach sieht sie auf diesem Auge nichts mehr. Sie zeigt ihn an und verlangt seine Bestrafung (Antragstellerin).
Doktor Wallner wird als Beschuldigter vernommen; ein Gutachten findet keinen Behandlungsfehler, der unterschriebene
Aufklärungsbogen nennt das Risiko. Im Juni entwirft Referendarin Hölscher die Einstellungsverfügung und will die Akte
weglegen (fehlende Mitteilungen). Bescheid zugestellt Do, 2.7.2026; Beschwerde Mo, 13.7.2026 (Frist bis Do, 16.7.); Bescheid der
Generalstaatsanwaltschaft zugestellt Mi, 5.8.2026; Monatsfrist endet nicht Sa, 5.9., sondern Mo, 7.9.2026 (§ 43 Abs. 2 StPO).
Aufbau (Schema): Fall → Sachverhalt → § 170 Abs. 1/Abs. 2 S. 1 (Wortlautkarte; Gründe; Verweis 060/180) → Einstellungsverfügung
Ziff. 1/Ziff. 2 → § 170 Abs. 2 S. 2 (Wortlautkarte, Nr. 88 RiStBV) → § 171 S. 1, 2 (Wortlautkarte), § 373b, Nr. 91 Abs. 2 RiStBV →
§ 172 Abs. 1 (Wortlautkarte) → § 172 Abs. 2 S. 1, Abs. 4, Abs. 3 S. 1, 2 (Wortlautkarten; BVerfG 2 BvR 1550/17 Rn. 18, 19) →
Ausschluss § 172 Abs. 2 S. 3 (Fall: § 226 im Raum) → §§ 174, 175 → Lösung mit Kalender Juli/September 2026 → Schema → Klausurtipp
(Lexi) → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Rautenberg, Wallner, Hölscher (nie im
Genitiv). Stimmen (Pool stephan, hilde, christian, lucy): Frau Rautenberg hilde (Frau, älter), Doktor Wallner stephan (Mann,
mittel; ein Satz), Referendarin Hölscher lucy (Frau, jung). christian nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Rautenberg": "hilde", "Wallner": "stephan", "Hoelscher": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der Augenarztpraxis -------------------------------------------------------------------------------------
    ("[fall]Dienstag, der dreizehnte Januar, eine Augenarztpraxis. [op]Doktor Wallner operiert Frau Rautenberg am rechten "
     "Auge. [danach]Nach der Operation sieht sie auf diesem Auge nichts mehr.", P),
    ("[ra1]Über dieses Risiko hat mich niemand aufgeklärt. Ich zeige den Arzt an.", P, "Rautenberg"),
    ("[anz]Sie erstattet Strafanzeige wegen Körperverletzung und verlangt, dass er bestraft wird.", P),
    # --- A2 Fall: Vernehmung, Gutachten ------------------------------------------------------------------------------------
    ("[verm]Die Staatsanwaltschaft ermittelt. Doktor Wallner wird als Beschuldigter vernommen.", P),
    ("[wa1]Ich habe sie vor der Operation über die Risiken aufgeklärt.", P, "Wallner"),
    ("[gut]Ein Gutachten findet keinen Behandlungsfehler, [bogen]und der unterschriebene Aufklärungsbogen nennt das Risiko.", P),
    # --- A3 Fall: bei der Staatsanwaltschaft -------------------------------------------------------------------------------
    ("[akte]Im Juni liegt die Akte bei Referendarin Hölscher.", P),
    ("[ho1]Kein hinreichender Tatverdacht. Ich stelle ein und lege die Akte weg.", P, "Hoelscher"),
    ("[frage]Reicht das? [frage2]Was gehört in die Einstellungsverfügung, und was kann Frau Rautenberg dagegen tun?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wann: § 170 Abs. 1, Abs. 2 S. 1 StPO ----------------------------------------------------------------------------
    ("[p170]Paragraf hundertsiebzig Absatz eins Strafprozessordnung: Bieten die Ermittlungen genügenden Anlass zur Erhebung "
     "der öffentlichen Klage, erhebt die Staatsanwaltschaft sie. [p170b]Absatz zwei Satz eins: Andernfalls stellt die "
     "Staatsanwaltschaft das Verfahren ein. [tats]Es fehlt der hinreichende Tatverdacht: aus tatsächlichen Gründen, weil "
     "die Tat nicht beweisbar ist, [recht]oder aus rechtlichen Gründen, etwa weil kein Straftatbestand erfüllt ist. "
     "[hind]Auch ein Verfahrenshindernis führt hierher. [verw]Details zeigen die Videos zum Tatverdacht und zu "
     "den Verfahrenshindernissen. [fall2]Hier: kein Behandlungsfehler, die Aufklärung belegt. Einstellung.", PS),
    # --- D Aufbau der Einstellungsverfügung --------------------------------------------------------------------------------
    ("[verfg]Die Verfügung hat zwei Teile. [z1]Ziffer eins: Das Verfahren wird nach Paragraf hundertsiebzig "
     "Absatz zwei eingestellt. [z2]Ziffer zwei: die Mitteilungen. [fehlt]Genau die fehlen im Entwurf.", PS),
    # --- E Mitteilung an den Beschuldigten: § 170 Abs. 2 S. 2 StPO ---------------------------------------------------------
    ("[p170s2]Paragraf hundertsiebzig Absatz zwei Satz zwei: Hiervon setzt sie den Beschuldigten in Kenntnis, wenn er als "
     "solcher vernommen worden ist oder ein Haftbefehl gegen ihn erlassen war. "
     "[wall]Doktor Wallner wurde als Beschuldigter "
     "vernommen: Er erhält die Mitteilung. [nr88]Besteht kein begründeter Verdacht mehr, sagt sie das nach den Richtlinien "
     "für das Strafverfahren ausdrücklich.", P),
    # --- F Bescheid an die Antragstellerin: § 171 StPO ---------------------------------------------------------------------
    ("[p171]Paragraf hunderteinundsiebzig Satz eins: Verfügt die Staatsanwaltschaft die Einstellung, hat sie den "
     "Antragsteller unter Angabe der Gründe zu bescheiden. [antr]Frau Rautenberg hat die Bestrafung verlangt: Sie ist "
     "Antragstellerin. [p171s2]Satz zwei: Ist der Antragsteller zugleich der Verletzte, ist er über die Möglichkeit der "
     "Anfechtung und die Frist zu belehren. [verl]Verletzte ist sie nach Paragraf dreihundertdreiundsiebzig b: "
     "durch die Tat, ihre Begehung unterstellt, unmittelbar in ihren Rechtsgütern beeinträchtigt. [zust]Da eine "
     "Beschwerde zu erwarten ist, wird der Bescheid zugestellt.", P),
    ("[ho2]Also: Bescheid mit Gründen und Belehrung, und eine Mitteilung an den Arzt.", PS, "Hoelscher"),
    # --- G Vorschaltbeschwerde: § 172 Abs. 1 StPO --------------------------------------------------------------------------
    ("[p172]Paragraf hundertzweiundsiebzig Absatz eins: Ist der Antragsteller zugleich der Verletzte, so steht ihm gegen "
     "den Bescheid binnen zwei Wochen nach der Bekanntmachung die Beschwerde an den vorgesetzten Beamten der "
     "Staatsanwaltschaft zu. [gsta]Das ist die Generalstaatsanwaltschaft. [nurv]Wer nur anzeigt, ohne verletzt zu sein, hat "
     "diese Beschwerde nicht. [wahr]Einlegen bei der Staatsanwaltschaft wahrt die Frist; [nobel]ohne Belehrung läuft sie "
     "gar nicht.", PS),
    # --- H Klageerzwingungsantrag: § 172 Abs. 2 S. 1, Abs. 4, Abs. 3 S. 1, 2 StPO -------------------------------------------
    ("[p172b]Bleibt die Beschwerde erfolglos, gilt Absatz zwei Satz eins: Gegen den ablehnenden "
     "Bescheid kann der Antragsteller binnen einem Monat nach der Bekanntmachung gerichtliche Entscheidung beantragen. "
     "[olg]Zuständig ist das Oberlandesgericht, Absatz vier.", P),
    ("[p172c]Absatz drei Satz eins: Der Antrag muss die Tatsachen, welche die Erhebung der öffentlichen Klage begründen "
     "sollen, und die Beweismittel angeben. [bverfg]Nach dem Bundesverfassungsgericht darf man eine aus sich selbst "
     "heraus verständliche Schilderung des Sachverhalts verlangen; [nueb]überspannen dürfen die Gerichte diese Anforderungen aber nicht. "
     "[anw]Satz zwei: Er muss von einem Rechtsanwalt unterzeichnet sein.", P),
    ("[ausschl]Ausgeschlossen ist der Antrag, wenn das Verfahren nur ein Privatklagedelikt betrifft, etwa eine einfache "
     "Körperverletzung, [opp]oder nach bestimmten Einstellungen aus Opportunitätsgründen. [p226]Hier steht aber der Verlust des "
     "Sehvermögens im Raum, eine schwere Körperverletzung nach Paragraf zweihundertsechsundzwanzig: [offen]Der Weg ist offen.", PS),
    # --- I Entscheidung des Oberlandesgerichts: §§ 174, 175 StPO -----------------------------------------------------------
    ("[p174]Fehlt genügender Anlass zur Anklage, verwirft das Oberlandesgericht den Antrag, Paragraf hundertvierundsiebzig. "
     "[p175]Hält es den Antrag für begründet, beschließt es die Erhebung der öffentlichen Klage, Paragraf "
     "hundertfünfundsiebzig; [durchf]durchführen muss sie die Staatsanwaltschaft.", PS),
    # --- J Lösung mit Kalender ---------------------------------------------------------------------------------------------
    ("[lsg]Zurück zu Frau Rautenberg. [zwei]Der Bescheid wird ihr am Donnerstag, "
     "dem zweiten Juli, zugestellt: [ende1]Die zwei Wochen enden mit Ablauf des sechzehnten Juli. [mo13]Ihre Beschwerde vom "
     "dreizehnten Juli ist rechtzeitig.", P),
    ("[ablehn]Die Generalstaatsanwaltschaft weist sie zurück; ihr Bescheid wird am Mittwoch, dem fünften August, zugestellt. "
     "[sa5]Ein Monat später ist der fünfte September, ein Samstag. [mo7]Dann endet die Frist mit Ablauf des "
     "nächsten Werktags, Montag, des siebten September, Paragraf dreiundvierzig Absatz zwei.", P),
    ("[ra2]Dann gehe ich mit meiner Anwältin zum Oberlandesgericht.", PS, "Rautenberg"),
    # --- K Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Klageerzwingungsantrag. [s1]Römisch eins, Zulässigkeit: [s1a]Antragsteller und Verletzter, "
     "[s1b]erfolglose Beschwerde binnen zwei Wochen, [s1c]Antrag binnen eines Monats beim Oberlandesgericht, [s1d]mit "
     "Tatsachen, Beweismitteln und Anwalt, [s1e]kein Ausschluss nach Absatz zwei Satz drei. [s2]Römisch zwei, "
     "Begründetheit: genügender Anlass zur Erhebung der öffentlichen Klage. [s3]Römisch drei: Verwerfung oder "
     "Anklagebeschluss.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Vergiss in der Einstellungsverfügung die Mitteilungen nicht. [k1]Der Antragsteller bekommt einen "
     "Bescheid mit Gründen, [k2]als Verletzter mit Belehrung über Beschwerde und Frist, sonst läuft die Frist nicht. "
     "[k3]Und den Beschuldigten informierst du, etwa wenn er vernommen wurde.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer einstellt, muss den Antragsteller bescheiden. [m2]Der Verletzte hat zwei Wochen für die Beschwerde und dann einen "
     "Monat für den Klageerzwingungsantrag, mit Anwalt beim Oberlandesgericht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
