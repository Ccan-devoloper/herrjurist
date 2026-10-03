"""Folge 121 · Verkehrszeichen als Verwaltungsakt: Kannst du ein Schild anfechten? (Mo · Der Fall · Alltagsfall ·
Verwaltungsrecht AT). Fiktiver Fall nach dem Plan-Hook („Über Nacht steht vor deiner Haustür ein Halteverbotsschild“),
Beispielland Nordrhein-Westfalen (kein Vorverfahren, § 110 Abs. 1 Satz 1 JustG NRW), offen gelegt:
Frau Wittmann parkt seit zwanzig Jahren vor ihrem Haus. Über Nacht steht dort ein dauerhaftes absolutes Haltverbot
(Zeichen 283). Herr Buchholz von der Straßenverkehrsbehörde der Stadt nennt nur einen pauschalen Grund („Sicherheit und
Ordnung des Verkehrs“). Fallprüfung: 1. Rechtsnatur: Allgemeinverfügung § 35 S. 2 VwVfG (Wortlautkarte; BVerwG 3 C 10.15
Rn. 16; dritte Variante nach VG Münster 1 K 605/10 Rn. 18), Dauerverwaltungsakt (BVerwG 3 C 37.09 Rn. 21); Verweis 044/064.
2. Bekanntgabe und Wirksamkeit: § 43 Abs. 1 VwVfG, Aufstellen als besondere Form der öffentlichen Bekanntgabe nach StVO
(3 C 10.15 Rn. 16), Sichtbarkeitsgrundsatz ein Satz mit Verweis 064. 3. Zulässigkeit: § 40 I, § 42 I, II VwGO (Adressat,
Art. 2 I GG; BVerwG 3 C 15.03, Volltext ohne Rn. → im Video ohne Az.), Vorverfahren (NRW nein), Frist § 58 II VwGO ab erster
Konfrontation (3 C 37.09 Leitsatz, Rn. 14, 16, 18), Klagegegner § 78 I Nr. 1, keine aufschiebende Wirkung analog § 80 II 1 Nr. 2
(3 C 25.16 Rn. 14), Eilantrag § 80 V nur genannt. 4. Begründetheit § 113 I 1: § 45 I 1 StVO (3 C 7.17 Rn. 11), formell
(§ 28 II Nr. 4 VwVfG), § 45 IX StVO (Wortlautkarte S. 1 und S. 3): S. 3 nur fließender Verkehr (3 C 37.09 Rn. 23–25;
3 C 5.23 Rn. 36), für das Haltverbot S. 1 restriktiv (3 C 5.23 Rn. 35), Ermessen (3 C 7.17 Rn. 13; 3 C 37.09 Rn. 35),
Darlegung durch die Behörde (3 C 37.09 Rn. 37), maßgeblicher Zeitpunkt (Rn. 21, 28) → Klage begründet, Aufhebung.
Klausurtipp (Bußgeld § 49 III Nr. 4 StVO, Abschleppen, Verweis 064), Schema, Merksatz mit Lexi. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Wittmann, Buchholz, Wolter.
Stimmen: Frau Wittmann hilde, Herr Buchholz stephan, Frau Wolter lucy (christian nicht besetzt: klingt wie stephan).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter, Abkürzungen ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Wittmann": "hilde", "Buchholz": "stephan", "Wolter": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das neue Schild vor dem Haus -----------------------------------------------------------------------------
    ("[fall]Ein Morgen in einer Stadt in Nordrhein-Westfalen. [haus]Frau Wittmann wohnt hier seit zwanzig Jahren. Ihr Auto "
     "parkt sie immer direkt vor dem Haus. [schild]Heute steht dort ein neues Schild: absolutes Haltverbot.", 0.2),
    ("[wi1]Seit wann steht das denn hier?", 0.3, "Wittmann"),
    ("[wolter]Ihre Nachbarin Frau Wolter kommt vorbei.", 0.2),
    ("[wo1]Seit gestern Abend. Jetzt darf hier keiner mehr halten, nicht mal zum Ausladen.", 0.3, "Wolter"),
    # --- B Fall: der Anruf bei der Stadt ----------------------------------------------------------------------------------
    ("[amt]Frau Wittmann ruft bei der Stadt an. [buchholz]Herr Buchholz von der Straßenverkehrsbehörde antwortet knapp.", 0.2),
    ("[bu1]Das Haltverbot dient der Sicherheit und Ordnung des Verkehrs.", 0.3, "Buchholz"),
    ("[wi2]Welche Gefahr denn? Hier ist noch nie etwas passiert!", 0.3, "Wittmann"),
    ("[bu2]Mehr kann ich Ihnen dazu nicht sagen.", 0.3, "Buchholz"),
    # --- C Frage --------------------------------------------------------------------------------------------------------
    ("[frage]Frau Wittmann will gegen das Schild vorgehen. Kann man ein Verkehrsschild anfechten? [frage2]Und hat sie "
     "Erfolg?", 0.6),
    # --- D Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E 1. Rechtsnatur: Allgemeinverfügung, Dauerverwaltungsakt ---------------------------------------------------------
    ("[natur]Erste Frage: Ist das Schild überhaupt ein Verwaltungsakt? [strspr]Ja. Nach ständiger Rechtsprechung des "
     "Bundesverwaltungsgerichts ist ein Haltverbot ein Verwaltungsakt in Form einer Allgemeinverfügung. [wl35]Paragraf "
     "fünfunddreißig Satz zwei Verwaltungsverfahrensgesetz kennt drei Varianten. [var3]Hier passt die dritte: Das Schild "
     "regelt die Benutzung einer Sache durch die Allgemeinheit, nämlich der Straße. [verweis]Die Merkmale des Verwaltungsakts findest du in Folge vierundvierzig. [dauer]Wichtig für die Klage: "
     "Das Schild regelt die Stelle auf Dauer, es ist ein Dauerverwaltungsakt.", P),
    # --- F 2. Bekanntgabe und Wirksamkeit -----------------------------------------------------------------------------------
    ("[bekannt]Zweitens: Wirksam wird ein Verwaltungsakt mit seiner Bekanntgabe, Paragraf dreiundvierzig Absatz eins. "
     "[aufstellen]Beim Schild gibt es keinen Brief und keine ortsübliche Bekanntmachung nach Paragraf einundvierzig "
     "Absatz vier. Bekannt gegeben wird es nach den Spezialregeln der Straßenverkehrs-Ordnung durch das Aufstellen, eine "
     "besondere Form der öffentlichen Bekanntgabe. [sicht]Wann es gegenüber jedem wirkt, regelt der "
     "Sichtbarkeitsgrundsatz, erklärt im Abschleppfall, Folge vierundsechzig. [wirksam]Das Schild vor dem Haus ist gut zu "
     "sehen, es ist wirksam.", P),
    # --- G 3. Zulässigkeit: Rechtsweg, Klageart, Klagebefugnis ------------------------------------------------------------
    ("[zul]Zur Klage: [weg]Der Verwaltungsrechtsweg ist offen. "
     "[statt]Statthaft ist die Anfechtungsklage, Frau Wittmann will die Aufhebung des Schildes. [befugt]Klagebefugt ist sie als "
     "Verkehrsteilnehmerin, die auf das Schild getroffen ist. Als Adressatin eines belastenden Verwaltungsakts kann sie eine "
     "Verletzung ihrer allgemeinen Handlungsfreiheit geltend machen, Artikel zwei Absatz eins Grundgesetz.", P),
    # --- H Vorverfahren, Frist, Klagegegner, keine aufschiebende Wirkung -------------------------------------------------------
    ("[vorv]Ein Vorverfahren braucht sie in Nordrhein-Westfalen nicht, nach dem Justizgesetz des Landes entfällt es in der "
     "Regel. In anderen Ländern kann zuerst ein Widerspruch nötig sein. [frist]Und die Frist? Ein Schild hat keine "
     "Rechtsbehelfsbelehrung. Deshalb gilt die Jahresfrist aus Paragraf achtundfünfzig Absatz zwei "
     "Verwaltungsgerichtsordnung. [erstmals]Sie beginnt nicht mit dem Aufstellen, sondern erst, wenn Frau Wittmann zum "
     "ersten Mal auf das Schild trifft, also an diesem Morgen. [nichtneu]Kommt sie später wieder vorbei, beginnt die Frist "
     "nicht neu. [gegner]Verklagt wird die Stadt.", P),
    ("[aufsch]Aber Achtung: Die Klage hat keine aufschiebende Wirkung. Das Haltverbot ist sofort vollziehbar, entsprechend "
     "Paragraf achtzig Absatz zwei Satz eins Nummer zwei Verwaltungsgerichtsordnung. [eil]Wer schnell Schutz "
     "braucht, stellt einen Eilantrag nach Paragraf achtzig Absatz fünf.", P),
    # --- I 4. Begründetheit: Rechtsgrundlage, formell --------------------------------------------------------------------
    ("[begr]Begründet ist die Klage, soweit das Haltverbot rechtswidrig ist und Frau Wittmann dadurch in ihren Rechten "
     "verletzt, Paragraf hundertdreizehn Absatz eins. [egl]Rechtsgrundlage ist Paragraf fünfundvierzig Absatz eins Satz eins "
     "der Straßenverkehrs-Ordnung: Die Straßenverkehrsbehörde kann die Benutzung bestimmter Straßen aus Gründen der "
     "Sicherheit oder Ordnung des Verkehrs beschränken. [formell]Formell ist die Stadt zuständig, und vor einer "
     "Allgemeinverfügung darf sie von der Anhörung absehen.", P),
    # --- J § 45 Abs. 9 StVO: Satz 1 und Satz 3 ---------------------------------------------------------------------------
    ("[wl45]Entscheidend ist Absatz neun. [s1]Satz eins: Verkehrszeichen sind nur dort anzuordnen, wo dies auf Grund der "
     "besonderen Umstände zwingend erforderlich ist. [s3]Satz drei verlangt mehr: eine Gefahrenlage aus den besonderen "
     "örtlichen Verhältnissen, die das allgemeine Risiko erheblich übersteigt. [fliess]Das gilt aber nur für Beschränkungen "
     "des fließenden Verkehrs, etwa ein Überholverbot. [ruhend]Ein Haltverbot betrifft den ruhenden Verkehr. Darauf ist Satz "
     "drei nach dem Bundesverwaltungsgericht nicht anzuwenden. Es bleibt bei Satz eins.", P),
    ("[zwingend]Die Behörde muss dabei zurückhaltend sein: Ein Schild braucht es nur, wenn die allgemeinen "
     "Verkehrsregeln für einen sicheren und geordneten Verkehr nicht ausreichen. [ermessen]Erst dann hat die Stadt Ermessen, "
     "und bei der Wahl des Mittels gilt die Verhältnismäßigkeit.", P),
    # --- K Subsumtion und Ergebnis ---------------------------------------------------------------------------------------
    ("[hier]Und hier? Die Stadt nennt nur Sicherheit und Ordnung des Verkehrs, also die Worte des Gesetzes. Besondere "
     "Umstände an dieser Stelle nennt sie nicht. [last]Diese Voraussetzungen für den Eingriff muss aber die Behörde darlegen. "
     "[zeit]Weil das Schild ein Dauerverwaltungsakt ist, zählt die Lage bei der letzten mündlichen Verhandlung. Bis dahin "
     "kann die Stadt noch neue Tatsachen vortragen, etwa eine nötige Feuerwehrzufahrt. [erg]Bleibt es beim pauschalen "
     "Grund, ist das Haltverbot rechtswidrig und verletzt Frau Wittmann in ihrer Handlungsfreiheit. [aufheb]Die Klage ist "
     "begründet, das Gericht hebt das Haltverbot auf. [keinbesch]Ein Bescheidungsurteil gibt es hier nicht, das kennt nur "
     "die Verpflichtungsklage.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bis zur Aufhebung gilt das Schild. Wer es einfach ignoriert, riskiert ein Bußgeld und das "
     "Abschleppen, wie im Abschleppfall. [tipp2]Und prüfe beim Haltverbot nicht die besondere Gefahrenlage aus Satz drei. "
     "Die gilt nur für den fließenden Verkehr.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q1]Eins, Zulässigkeit: [q1a]Rechtsweg und Anfechtungsklage gegen die Allgemeinverfügung, "
     "[q1b]Klagebefugnis, [q1c]Vorverfahren je nach Land [q1d]und Jahresfrist ab der ersten Begegnung. [q2]Zwei, "
     "Begründetheit: [q2a]Rechtsgrundlage Paragraf fünfundvierzig Absatz eins, [q2b]zwingend erforderlich nach Absatz neun, "
     "beim fließenden Verkehr zusätzlich Satz drei, [q2c]Ermessen [q2d]und Rechtsverletzung.", PS),
    # --- N Merksatz (Lexi) ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Verkehrsschild ist eine Allgemeinverfügung. Du kannst es anfechten, binnen eines Jahres ab der "
     "ersten Begegnung. [m2]Ein Haltverbot ist nur rechtmäßig, wenn es auf Grund besonderer Umstände zwingend erforderlich "
     "ist.", 1.4),
]
