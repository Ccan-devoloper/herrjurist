"""Folge 192 · Abgrenzungstheorien: Öffentliches oder privates Recht? (§ 40 VwGO) (Fr · Klausurpraxis · Verwaltungsrecht AT,
Format Schema). Beispielfall nach dem Plan-Hook („Die Stadt kündigt dir die Parzelle in der städtischen Kleingartenanlage –
Zivilgericht oder Verwaltungsgericht?“): Frau Kirschner (um 70) pachtet seit zwanzig Jahren unmittelbar von der Stadt eine
Parzelle in der städtischen Kleingartenanlage. Anfang Februar kündigt die Stadt den Kleingartenpachtvertrag zum 30. November,
weil auf der Parzelle ein Spielplatz für die Anlage entstehen soll (§ 9 Abs. 1 Nr. 2, Abs. 2 BKleingG). Frau Kirschner will vor
das Verwaltungsgericht; ihre Nachbarin Elsa (Jurastudentin, Anfang 20) bremst.
Aufbau (Schema): Fall → Sachverhalt → Wortlaut § 40 Abs. 1 S. 1 VwGO und § 13 GVG → drei Merkmale → streitentscheidende Norm
(§ 4 Abs. 1, § 9 BKleingG) → Interessen-, Subordinations-, modifizierte Subjektstheorie (Tabelle, h. M.) → Sonderfälle
(Zwei-Stufen-Theorie, Hausverbot, Fiskalverwaltung) → Lösung (Zivilrechtsweg, § 13 GVG) → § 17a Abs. 2 S. 1 GVG (Wortlaut),
§ 17b GVG → Handlungsform und Verfahrensrecht → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Kirschner, Elsa (nie im Genitiv).
Stimmen (Pool stephan, hilde, christian, lucy): Frau Kirschner hilde (Frau, älter), Elsa lucy (Frau, jung); stephan und
christian nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter (keine Abkürzungen wie VwGO/GVG/BGB)."""

P, PS = 0.3, 0.5

STIMMEN = {"Kirschner": "hilde", "Elsa": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Parzelle in der städtischen Kleingartenanlage -------------------------------------------------------
    ("[fall]Frau Kirschner pachtet seit zwanzig Jahren eine Parzelle in der städtischen Kleingartenanlage. [vertrag]Ihren "
     "Pachtvertrag hat sie direkt mit der Stadt geschlossen. [brief]Anfang Februar kommt ein Brief: [kuend]Die Stadt kündigt "
     "den Vertrag zum dreißigsten November. [grund]Auf der Parzelle soll ein Spielplatz für die Anlage entstehen.", P),
    ("[ki1]Die Stadt ist doch eine Behörde. Dann klage ich vor dem Verwaltungsgericht!", P, "Kirschner"),
    ("[el1]Nicht so schnell. Dass die Stadt kündigt, sagt noch nicht, welches Gericht zuständig ist.", P, "Elsa"),
    ("[frage]Zivilgericht oder Verwaltungsgericht? [frage2]Die Antwort liefern die Abgrenzungstheorien.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 40 Abs. 1 S. 1 VwGO, § 13 GVG; drei Merkmale ----------------------------------------------------------
    ("[wl40]Ausgangspunkt ist Paragraf vierzig Absatz eins Satz eins Verwaltungsgerichtsordnung: Der Verwaltungsrechtsweg ist "
     "in allen öffentlich-rechtlichen Streitigkeiten nichtverfassungsrechtlicher Art gegeben, soweit die Streitigkeiten nicht "
     "durch Bundesgesetz einem anderen Gericht ausdrücklich zugewiesen sind. [wl13]Das Gegenstück steht in Paragraf dreizehn "
     "Gerichtsverfassungsgesetz: Vor die ordentlichen Gerichte gehören die bürgerlichen Rechtsstreitigkeiten.", P),
    ("[mm]Daraus folgen drei Merkmale. [m1]Erstens, eine öffentlich-rechtliche Streitigkeit, das Thema dieses Videos. "
     "[m2]Zweitens, nichtverfassungsrechtlicher Art: Es streiten nicht Verfassungsorgane über Verfassungsrecht. [m3]Drittens, "
     "keine abdrängende Sonderzuweisung, etwa Paragraf vierzig Absatz zwei für bestimmte "
     "Schadensersatzansprüche.", PS),
    # --- D Streitentscheidende Norm -----------------------------------------------------------------------------------------
    ("[norm]Öffentlich-rechtlich ist ein Streit, wenn die streitentscheidende Norm zum öffentlichen Recht gehört. "
     "[norm2]Frag also zuerst: Nach welcher Norm wird entschieden? [norm3]Hier geht es um die Kündigung eines "
     "Kleingartenpachtvertrags. [norm4]Für ihn gelten nach Paragraf vier Bundeskleingartengesetz die Vorschriften des "
     "Bürgerlichen Gesetzbuchs über die Pacht. [norm5]Die Kündigung durch den Verpächter regelt Paragraf neun. "
     "[norm6]Ob diese Norm öffentlich oder privat ist, klären drei Theorien.", PS),
    # --- E Die drei Theorien (Tabelle) ---------------------------------------------------------------------------------------
    ("[th1]Erstens, die Interessentheorie. [i1]Sie fragt: Dient die Norm dem öffentlichen Interesse? [i2]Dann spräche hier viel "
     "für öffentliches Recht, denn die Stadt will einen Spielplatz für alle bauen. [i3]Die Kritik: Fast jedes Handeln der "
     "Verwaltung dient dem Gemeinwohl. Maßgeblich ist nicht das Ziel, sondern die Rechtsform.", P),
    ("[th2]Zweitens, die Subordinationstheorie. [s1]Sie fragt: Stehen sich die Beteiligten in Über- und Unterordnung "
     "gegenüber? [s2]Das passt zum Bescheid, mit dem eine Behörde einseitig etwas anordnet. Frau Kirschner und die Stadt haben "
     "dagegen einen Vertrag geschlossen. [s3]Die Kritik: Auch der öffentlich-rechtliche Vertrag beruht auf Gleichordnung und "
     "ist trotzdem öffentliches Recht.", P),
    ("[th3]Drittens, die modifizierte Subjektstheorie, auch Sonderrechtstheorie genannt. [hm]Sie ist herrschend. [t1]Sie "
     "fragt: Berechtigt oder verpflichtet die Norm gerade einen Träger hoheitlicher Gewalt als solchen? [t2]Dann ist sie "
     "Sonderrecht des Staates, also öffentliches Recht. Gilt sie für jedermann, ist sie Privatrecht. [t3]Beispiel: Ein Gewerbe "
     "untersagen darf nur die Behörde. [bverwg]So sieht es auch das Bundesverwaltungsgericht. "
     "[t4]Die Kritik: Lässt eine Norm offen, ob gerade der Hoheitsträger handelt, "
     "hilft erst der Zusammenhang.", PS),
    # --- F Sonderfälle ---------------------------------------------------------------------------------------------------------
    ("[sf]Drei Sonderfälle in Kürze. [zs]Die Zwei-Stufen-Theorie: Beim Zugang zu einer öffentlichen Einrichtung, etwa der "
     "Stadthalle, ist das Ob öffentlich-rechtlich, das Wie, zum Beispiel der Mietvertrag, kann privatrechtlich sein. "
     "[hv]Das Hausverbot im Rathaus: Es kommt auf den Zweck an. Schützt es den Dienstbetrieb, ist es öffentlich-rechtlich. "
     "[fisk]Die Fiskalverwaltung: Kauft die Stadt Büromaterial ein, handelt sie wie jeder Marktteilnehmer, "
     "also privatrechtlich.", PS),
    # --- G Lösung des Falls ---------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Frau Kirschner. [l1]Streitentscheidend ist Paragraf neun Bundeskleingartengesetz mit dem Pachtrecht des "
     "Bürgerlichen Gesetzbuchs. [l2]Die Norm berechtigt den Verpächter, und das kann jeder sein: ein Verein, eine Privatperson "
     "oder eben die Stadt. [l3]Die Stadt handelt hier nicht als Hoheitsträgerin, sondern als Verpächterin. [l4]Also "
     "Privatrecht: eine bürgerliche Rechtsstreitigkeit, für die nach Paragraf dreizehn der Zivilrechtsweg offensteht.", P),
    ("[el2]Über die Kündigung entscheidet also das Zivilgericht, nicht das Verwaltungsgericht.", P, "Elsa"),
    ("[ki2]Und wenn ich schon beim Verwaltungsgericht geklagt habe?", P, "Kirschner"),
    ("[wl17]Dann gilt Paragraf siebzehn a Absatz zwei Gerichtsverfassungsgesetz, über Paragraf hundertdreiundsiebzig auch im "
     "Verwaltungsprozess: Ist der Rechtsweg unzulässig, spricht das Gericht das von Amts wegen aus [wl17b]und verweist den "
     "Rechtsstreit an das zuständige Gericht. "
     "[verw]Die Klage wird also nicht als unzulässig abgewiesen, sondern verwiesen. [verw2]Die Rechtshängigkeit "
     "bleibt bestehen.", PS),
    # --- H Bedeutung: Handlungsform und Verfahrensrecht ----------------------------------------------------------------------
    ("[bed]Die Einordnung entscheidet nicht nur über den Rechtsweg. [hf]Zur Handlungsform: Einen Verwaltungsakt kann die "
     "Stadt nur auf dem Gebiet des öffentlichen Rechts erlassen. Im Kleingarten bleibt ihr die Kündigung des Vertrags. "
     "[vv]Zum Verfahrensrecht: Die Verwaltungsverfahrensgesetze gelten nur für öffentlich-rechtliche Verwaltungstätigkeit. "
     "Eine Anhörung nach Paragraf achtundzwanzig gibt es hier nicht.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Rechtsweg nur ausführlich, wenn er problematisch ist. [k1]Dann nenne zuerst die "
     "streitentscheidende Norm und ordne sie mit der modifizierten Subjektstheorie ein. [k2]Und lass dich nicht vom Absender "
     "täuschen: Dass die Stadt beteiligt ist, macht den Streit noch nicht öffentlich-rechtlich.", PS),
    # --- J Schema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den Verwaltungsrechtsweg. [q1]Römisch eins: Gibt es eine aufdrängende Sonderzuweisung, etwa "
     "für Beamte? [q2]Römisch zwei: Paragraf vierzig Absatz eins. "
     "[q2a]Erstens, öffentlich-rechtliche Streitigkeit: streitentscheidende Norm bestimmen, [q2b]mit der modifizierten "
     "Subjektstheorie einordnen, [q2c]Sonderfälle beachten. [q2d]Zweitens, nichtverfassungsrechtlicher Art. "
     "[q2e]Drittens, keine abdrängende Sonderzuweisung. [q3]Römisch drei: Ergebnis, sonst Verweisung.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nicht wer streitet, entscheidet, sondern nach welcher Norm gestritten wird. [mk2]Gilt sie für jedermann, "
     "ist es Privatrecht. [mk3]Berechtigt sie gerade den Staat, ist es öffentliches Recht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
