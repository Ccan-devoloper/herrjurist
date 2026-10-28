"""Folge 159 · Auslegungsmethoden Jura: Wortlaut, Systematik, Historie, Telos (Fr · Methodik · Auslegung, Format Methodik).
Beispielfall nach dem Plan-Hook („Ist ein E-Scooter ein ‚Fahrzeug‘? Vier Wege, ein Gesetz zu lesen.“): Die Jurastudentin
Thekla fährt jeden Morgen ruhig mit ihrem E-Scooter zur Uni (kein Unfall, kein Alkohol). Im Methodenseminar fragt Professor
Lindhorst: Ist Ihr E-Scooter ein Kraftfahrzeug? Leitbeispiel durchgehend: Kraftfahrzeug i. S. v. § 1 Abs. 2 StVG
(Wortlautkarte) und Elektrokleinstfahrzeug nach § 1 Abs. 1 eKFV (Wortlautkarte, gekürzt) – davon hängt ab, ob für
E-Scooter-Fahrer bei § 316 StGB der Grenzwert 1,1 ‰ für Kraftfahrer gilt.
KORREKTUR zum Plan-Text (offengelegt in ../RECHTSSTAND.md): § 316 StGB verlangt nur ein „Fahrzeug“, nicht ein
„Kraftfahrzeug“ (Wortlaut). Der Kraftfahrzeugbegriff (§ 1 Abs. 2 StVG) entscheidet über den Grenzwert der absoluten
Fahruntüchtigkeit (BayObLG 205 StRR 216/20; OLG Hamm 1 ORs 70/24 Rn. 20–31); der BGH hat die Grenzwertfrage für
Elektrokleinstfahrzeuge offengelassen (4 StR 366/20 Rn. 8; 4 StR 439/22 Rn. 4 f.).
Aufbau: Fall → Hook → Sachverhalt → vier Methoden mit gleicher Tafelstruktur Frage – Werkzeug – Ergebnis (BVerfG 2 BvR
2628/10 Rn. 66) → Wortlaut (§ 1 Abs. 2 StVG; Grenze im Strafrecht: Art. 103 Abs. 2 GG, BVerfG 2 BvR 2273/06 Rn. 11) →
Systematik (§ 1 Abs. 1 eKFV, § 1 Abs. 3 StVG im Umkehrschluss) → Historie (BR-Drs. 158/19, S. 1) → Telos (OLG Hamm Rn. 32)
→ Ergebnis der Rechtsprechung → Analogie (BGH I ZR 42/19 Rn. 32; § 1004 BGB analog, BGH VI ZR 403/19 Rn. 9) und
teleologische Reduktion (§ 181 BGB, BGH IX ZR 224/16 Rn. 17), Analogieverbot (Verweis Folge 148) → Klausurtipp (Lexi)
→ Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in keiner Textdatei unter youtube/ und nicht in der Liste vergebener Namen:
Thekla, Lindhorst (nie im Genitiv im Sprechtext). Stimmen: Thekla ela_froh, Professor Lindhorst helmut.
Lexi = Erzählerin Carla. Keine Marken von E-Scooter-Anbietern.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; StVG und eKFV ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Thekla": "ela_froh", "Lindhorst": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: mit dem E-Scooter zur Uni, Methodenseminar --------------------------------------------------------------
    ("[fall]Thekla fährt jeden Morgen mit ihrem E-Scooter zur Uni, ruhig auf dem Radweg. [ab]Vor dem Hörsaal stellt sie "
     "ihn ab. [sem]Im Methodenseminar hat Professor Lindhorst eine Frage an sie.", P),
    ("[l1]Ist Ihr E-Scooter eigentlich ein Kraftfahrzeug?", P, "Lindhorst"),
    ("[t1]Ein Kraftfahrzeug? Der hat doch nicht mal einen Sitz!", P, "Thekla"),
    ("[hook]Ist ein E-Scooter ein Fahrzeug, sogar ein Kraftfahrzeug? [hook2]Vier Wege, ein Gesetz zu lesen: Wortlaut, "
     "Systematik, Historie und Telos. [folge]Die Antwort hat Folgen. Bei der Trunkenheit im Verkehr gilt für Kraftfahrer "
     "ab eins Komma eins Promille absolute Fahruntüchtigkeit, für Radfahrer erst ab einem höheren Wert. [nur]Paragraf "
     "dreihundertsechzehn selbst verlangt nur ein Fahrzeug, und das ist der E-Scooter sicher. Spannend ist das "
     "Kraftfahrzeug.", P),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall. Halte das Video ruhig kurz an.", 5.0),
    # --- C Überblick: vier Methoden, gleiche Struktur ---------------------------------------------------------------------
    ("[vier]Jede Methode prüfst du mit denselben drei Schritten: [fr]Welche Frage stellt sie? [wz]Welches Werkzeug "
     "nutzt du? [eb]Und was ergibt sich am Beispiel? [bv]Das Bundesverfassungsgericht sagt: Die Methoden ergänzen sich, "
     "keine hat einen unbedingten Vorrang. Ausgangspunkt ist der Wortlaut.", P),
    # --- D Wortlaut ---------------------------------------------------------------------------------------------------------
    ("[w1]Erstens: der Wortlaut. Die Frage: Was sagen die Worte? [w2]Das Werkzeug: der Wortsinn und, wenn es eine gibt, die "
     "Legaldefinition. [p12]Paragraf eins Absatz zwei Straßenverkehrsgesetz: [p12w]Als Kraftfahrzeuge im Sinne dieses "
     "Gesetzes gelten Landfahrzeuge, die durch Maschinenkraft bewegt werden, ohne an Bahngleise gebunden zu sein.", P),
    ("[wl1]Der E-Scooter fährt an Land, [wl2]sein Elektromotor ist Maschinenkraft, [wl3]und Schienen braucht er nicht. "
     "[werg]Nach dem Wortlaut also: ein Kraftfahrzeug.", P),
    ("[gr1]Im Strafrecht ist der Wortlaut zugleich die Grenze. [a103]Artikel hundertdrei Absatz zwei Grundgesetz: "
     "[a103w]Eine Tat kann nur bestraft werden, wenn die Strafbarkeit gesetzlich bestimmt war, bevor die Tat begangen "
     "wurde. [gr2]Daraus folgt nach dem Bundesverfassungsgericht: Der mögliche Wortsinn ist die äußerste Grenze der "
     "Auslegung.", P),
    # --- E Systematik ------------------------------------------------------------------------------------------------------
    ("[s1]Zweitens: die Systematik. Die Frage: Wie passt die Norm zu den anderen? [s2]Das Werkzeug: die Stellung im Gesetz "
     "und das Verhältnis zu Nachbarnormen. [ek]Die Elektrokleinstfahrzeuge-Verordnung beginnt so: [ekw]Elektrokleinstfahrzeuge "
     "im Sinne dieser Verordnung sind Kraftfahrzeuge mit elektrischem Antrieb. [ekv]Gemeint sind etwa Fahrzeuge ohne Sitz bis "
     "zwanzig Kilometer pro Stunde, also der typische E-Scooter.", P),
    ("[s3]Und Paragraf eins Absatz drei Straßenverkehrsgesetz nimmt Räder, die man selbst treten muss und deren Motor nur "
     "hilft, ausdrücklich aus. [s4]Für E-Scooter gibt es keine solche Ausnahme. [serg]Systematisch also: ein "
     "Kraftfahrzeug.", P),
    # --- F Historie --------------------------------------------------------------------------------------------------------
    ("[h1]Drittens: die Historie. Die Frage: Was wollte der Normgeber? [h2]Das Werkzeug: die Materialien, also Entwürfe "
     "und ihre Begründungen. [h3]In der Begründung zur Verordnung, der Bundesratsdrucksache hundertachtundfünfzig aus dem "
     "Jahr zweitausendneunzehn, steht: [h3w]Da Elektrokleinstfahrzeuge über einen elektrischen Antriebsmotor verfügen, sind "
     "sie Kraftfahrzeuge. [herg]Der Verordnungsgeber wollte sie also bewusst als Kraftfahrzeuge.", P),
    # --- G Telos -----------------------------------------------------------------------------------------------------------
    ("[te1]Viertens: das Telos, also Sinn und Zweck. Die Frage: Wozu gibt es die Regel? [te2]Das Werkzeug: Du fragst, "
     "welche Gefahr sie abwehren soll. [te3]Der Grenzwert soll den Verkehr vor Fahrern schützen, die ihr Kraftfahrzeug "
     "nicht mehr sicher führen können. [te4]Ein E-Scooter fährt mit Motor bis zu zwanzig Kilometer pro Stunde, auf "
     "kleinen Rädern, der Fahrer steht. [te5]Das Oberlandesgericht Hamm sieht darin ein deutliches Risiko auch für "
     "andere. [teerg]Auch nach dem Zweck also: ein Kraftfahrzeug.", P),
    # --- H Ergebnis: Rechtsprechung ----------------------------------------------------------------------------------------
    ("[rs1]So sieht es auch die Rechtsprechung. [rs2]Das Bayerische Oberste Landesgericht hat zweitausendzwanzig "
     "entschieden: E-Scooter sind Kraftfahrzeuge, für ihre Fahrer gilt die Grenze von eins Komma eins Promille. "
     "[rs3]Andere Oberlandesgerichte folgen dem, etwa Hamm im Jahr zweitausendfünfundzwanzig. [rs4]Der Bundesgerichtshof hat die Frage für "
     "Elektrokleinstfahrzeuge bisher offengelassen. [rs5]Mehr zu den Promillegrenzen in Folge hundertdreißig.", P),
    ("[l2]Vier Methoden, ein Ergebnis: Ihr Scooter ist ein Kraftfahrzeug.", P, "Lindhorst"),
    ("[t2]Dann lasse ich ihn nach der Party lieber stehen.", 0.4, "Thekla"),
    # --- I Abgrenzung: Analogie und teleologische Reduktion -----------------------------------------------------------------
    ("[ab1]Wo die Auslegung endet, beginnt die Rechtsfortbildung. [an1]Die Analogie überträgt eine Norm auf einen Fall, "
     "den ihr Wortlaut nicht erfasst. [an2]Sie verlangt eine planwidrige Regelungslücke und eine vergleichbare "
     "Interessenlage. [an3]Beispiel: Paragraf tausendvier BGB schützt dem Wortlaut nach nur das Eigentum; die "
     "Rechtsprechung wendet ihn entsprechend auch auf das Persönlichkeitsrecht an.", P),
    ("[tr1]Die teleologische Reduktion ist das Gegenstück: Der Wortlaut erfasst einen Fall, den der Zweck nicht erfassen "
     "soll. [tr2]Beispiel: Paragraf hunderteinundachtzig BGB verbietet grundsätzlich Insichgeschäfte; bringen sie dem Vertretenen "
     "lediglich einen rechtlichen Vorteil, greift das Verbot nach dem Bundesgerichtshof nicht. [av]Im Strafrecht ist eine "
     "Analogie zulasten des Täters verboten, Artikel hundertdrei Absatz zwei Grundgesetz, mehr dazu in Folge "
     "hundertachtundvierzig.", P),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Beginne beim Wortlaut, dann Systematik, Historie und Telos. [tipp2]Bring zu jeder Methode ein "
     "Argument und ein Zwischenergebnis. [tipp3]Als Merkhilfe: Wortlaut zuerst, Telos entscheidet oft. Eine feste "
     "Rangfolge ist das nicht. [tipp4]Und Materialien zitierst du nur, wenn du sie wirklich kennst.", PS),
    # --- K Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Auslegung im Gutachten. [k1]Erstens, Wortlaut, mit Legaldefinition. [k2]Zweitens, "
     "Systematik. [k3]Drittens, Historie. [k4]Viertens, Telos. [k5]Dann das Ergebnis der Auslegung. [k6]Und erst danach: "
     "Lücke oder zu weiter Wortlaut? Analogie oder teleologische Reduktion, im Strafrecht nie zulasten des Täters.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Auslegen heißt, ein Gesetz auf vier Wegen zu lesen: Wortlaut, Systematik, Historie, Telos. [mm2]Der "
     "Wortlaut ist der Anfang, im Strafrecht auch die Grenze.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
