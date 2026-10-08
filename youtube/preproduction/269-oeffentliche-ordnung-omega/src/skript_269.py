"""Folge 269 · Öffentliche Ordnung: Zwergenweitwurf und Laserdrome (Omega) (Mi · Examenswissen · Polizei- und
Ordnungsrecht · Klassiker-Fall). Beispielfall nach dem Plan-Hook, respektvoll erzählt: Freitagnachmittag, eine Diskothek in
Nordrhein-Westfalen. Für Samstag wirbt Frau Bredemeier mit einem „Zwergenweitwurf“; der kleinwüchsige Artist Herr Mehring
macht freiwillig und gegen Bezahlung mit. Frau Leuschner (Ordnungsamt) untersagt die Veranstaltung wegen einer Gefahr für die
öffentliche Ordnung. Kein Wurf im Bild (nur Plakat), Herr Mehring als selbstbewusster Erwachsener mit eigener Stimme.
Aufbau: Begriff (BVerfGE 69, 315 [352], DFR-Rn. 77; § 4 Nr. 2 SächsPVDG), Bestimmtheitsbedenken (ebd.), Länder (Schleswig-
Holstein strich das Schutzgut 1992, LT-Drs. 16/2115; NRW, NI, SN, BB nennen es) → Zwergenweitwurf (VG Neustadt, Beschl. v.
21.5.1992 – 7 L 1271/92, NVwZ 1993, 98: Gewerberecht, gute Sitten, Menschenwürde; Volltext nicht online, nach Sekundär-
quellen; Wortlautkarte Art. 1 Abs. 1 GG; Gegenseite: Selbstbestimmung, Art. 12 GG) → Laserdrome/Omega (EuGH, Urt. v.
14.10.2004 – C-36/02, Rn. 3–12, 25, 28, 30, 34–39, 41; Wortlautkarte Art. 56 Abs. 1 AEUV, Art. 52 Abs. 1 AEUV) → Gegenfall
feste Ziele → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, nicht vergeben, eingetragen als „269: Leuschner, Bredemeier, Mehring“): Frau Leuschner (julia),
Frau Bredemeier (ela_froh), Herr Mehring (niklas); helmut nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Leuschner": "julia", "Bredemeier": "ela_froh", "Mehring": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Diskothek, Freitagnachmittag ---------------------------------------------------------------------------
    ("[fall]Freitagnachmittag, eine Diskothek in Nordrhein-Westfalen. [plakat]Am Eingang hängt ein Plakat: Samstag, "
     "Zwergenweitwurf. [wurf]Gäste sollen einen kleinwüchsigen Artisten möglichst weit auf eine Matte werfen. "
     "[amt]Frau Leuschner vom Ordnungsamt bringt eine Verfügung.", P),
    ("[le1]Frau Bredemeier, wir untersagen die Veranstaltung. Sie verletzt die Menschenwürde.", P, "Leuschner"),
    ("[br1]Aber Herr Mehring macht freiwillig mit, und er wird gut bezahlt.", P, "Bredemeier"),
    ("[meh]Der Artist Herr Mehring ist selbst gekommen.", P),
    ("[me1]Das ist mein Beruf. Über meine Würde entscheide ich selbst.", 0.4, "Mehring"),
    ("[frage]Darf die Behörde verbieten, obwohl alle einverstanden sind? [frage2]Sie stützt sich auf die "
     "Generalklausel: eine Gefahr für die öffentliche Ordnung.", PS),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Begriff, Bestimmtheit, Länder ------------------------------------------------------------------------------------
    ("[begriff]Erster Schritt: der Begriff. [def]Öffentliche Ordnung meint nach dem Bundesverfassungsgericht die "
     "ungeschriebenen Regeln, deren Befolgung nach den herrschenden sozialen und ethischen Anschauungen als unerlässlich "
     "für ein geordnetes Zusammenleben gilt. [abgr]Die öffentliche Sicherheit dagegen schützt die Rechtsordnung und "
     "zentrale Rechtsgüter; dazu Folge zweihundertdreizehn. [sachsen]Sachsen hat die Definition der öffentlichen Ordnung "
     "sogar ins Gesetz geschrieben.", P),
    ("[unbest]Kritiker halten den Begriff für zu unbestimmt. [bvg]Das Bundesverfassungsgericht hielt dagegen: Er habe "
     "durch das Polizeirecht einen hinreichend klaren Inhalt. [land]Doch nicht jedes Land kennt dieses Schutzgut. "
     "[sh]Schleswig-Holstein hat es neunzehnhundertzweiundneunzig aus seinem Landesverwaltungsgesetz gestrichen. [shgrund]Die "
     "Landesregierung meinte später, bei so unterschiedlichem Freizeitverhalten tauge eine ungeschriebene Sozialnorm "
     "nicht mehr als Ermächtigungsgrundlage. [vier]Nordrhein-Westfalen, Niedersachsen, Sachsen und Brandenburg nennen "
     "die öffentliche Ordnung. [dein]Prüfe also dein Landesgesetz.", PS),
    # --- D Zwergenweitwurf: Menschenwürde trotz Einwilligung? ---------------------------------------------------------------
    ("[zw]Nun der erste Klassiker. [vorbild]Neunzehnhundertzweiundneunzig untersagte eine Behörde in Rheinland-Pfalz "
     "eine solche Veranstaltung. [vgn]Das Verwaltungsgericht Neustadt billigte das im Eilverfahren, gestützt auf das Gewerberecht: "
     "Schaustellungen dürfen nicht gegen die guten Sitten verstoßen. [wert]Maßstab war, wie bei der öffentlichen "
     "Ordnung, die Wertordnung des Grundgesetzes. [art1]Und dort heißt es in Artikel eins: Die Würde des Menschen ist "
     "unantastbar. Sie zu achten und zu schützen ist Verpflichtung aller staatlichen Gewalt.", PS),
    ("[pro]Für Herrn Mehring spricht: Er entscheidet frei, und es ist sein Beruf, geschützt durch Artikel zwölf. "
     "[subj]Und Würde, so das Argument, heißt gerade, selbst zu bestimmen. [contra]Das Gericht sah es anders: Wer wie ein Sportgerät "
     "geworfen wird, wird zum bloßen Objekt der Belustigung. [name]Herabsetzend sei zudem schon die Bezeichnung als "
     "Zwerg. [verz]Auf seine Würde könne der Einzelne nicht wirksam verzichten; der Staat müsse sie schützen. "
     "[beruf]Und die Berufsfreiheit reiche nur so weit, wie die Berufsausübung nicht gegen die guten Sitten verstößt.", P),
    ("[erg1]Überträgt man das auf unseren Fall, ist die öffentliche Ordnung gefährdet, trotz der Einwilligung. "
     "[un]Ein Verbot in Frankreich sah auch der UN-Menschenrechtsausschuss nicht als Diskriminierung an.", PS),
    # --- E Laserdrome: EuGH Omega --------------------------------------------------------------------------------------------
    ("[ld]Zweiter Klassiker: das Laserdrome. [bonn]Neunzehnhundertvierundneunzig eröffnete in Bonn eine Anlage, in der "
     "Spieler mit Laserzielgeräten auf Sensoren an den Westen anderer Spieler zielten. [verf]Die Stadt untersagte das "
     "sogenannte spielerische Töten von Menschen, gestützt auf die Generalklausel des Ordnungsbehördengesetzes: Gefahr "
     "für die öffentliche Ordnung. [bverwg]Das Bundesverwaltungsgericht sah die Menschenwürde verletzt; sie lasse sich "
     "auch in einem Unterhaltungsspiel nicht abbedingen.", P),
    ("[eu]Doch Ausrüstung und Spielvariante kamen von einer britischen Firma. [art56]Damit war die "
     "Dienstleistungsfreiheit betroffen, heute Artikel sechsundfünfzig des Vertrags über die Arbeitsweise der "
     "Europäischen Union: Beschränkungen des freien Dienstleistungsverkehrs sind verboten. [art52]Gerechtfertigt sein "
     "können sie aus Gründen der öffentlichen Ordnung.", P),
    ("[eng]Diesen Begriff legt der Europäische Gerichtshof eng aus: Nötig ist eine tatsächliche und hinreichend schwere "
     "Gefährdung, die ein Grundinteresse der Gesellschaft berührt. [wuerde]Die Menschenwürde schützt aber auch die "
     "Unionsrechtsordnung, als allgemeinen Rechtsgrundsatz; ihr Schutz ist ein berechtigtes Interesse. [gemein]Und nicht "
     "alle Mitgliedstaaten müssen dieselbe Auffassung teilen, wie ein Grundrecht zu schützen ist. [vh]Verhältnismäßig "
     "war das Verbot, weil es nur die Spielvariante mit menschlichen Zielen untersagte. [tenor]Ergebnis: Das "
     "Unionsrecht steht dem Verbot nicht entgegen.", P),
    ("[gegen]Gegenfall: Zielten die Spieler nur auf feste Sensoren in der Anlage, erfasste die Verfügung das gar "
     "nicht.", PS),
    # --- F Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe vor der Generalklausel die Spezialgesetze, bei Schaustellungen von Personen etwa "
     "Paragraf dreiunddreißig a der Gewerbeordnung. [tipp1]Bei der öffentlichen Ordnung benenne die ungeschriebene Regel "
     "konkret und verankere sie im Grundgesetz, hier in der Menschenwürde. [tipp2]Und bei grenzüberschreitenden "
     "Dienstleistungen denk an Artikel sechsundfünfzig.", PS),
    # --- G Schema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Erstens, Ermächtigungsgrundlage: Spezialgesetz vor Generalklausel; und kennt dein Land die "
     "öffentliche Ordnung? [s2]Zweitens, Gefahr für die öffentliche Ordnung: ungeschriebene Regel, gemessen am "
     "Grundgesetz; bei der Menschenwürde hilft die Einwilligung nach der Rechtsprechung nicht. [s3]Drittens, bei "
     "grenzüberschreitenden Dienstleistungen: Artikel sechsundfünfzig, Rechtfertigung aus Gründen der öffentlichen "
     "Ordnung. [s4]Viertens, Ermessen und Verhältnismäßigkeit.", PS),
    # --- H Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Öffentliche Ordnung sind ungeschriebene Regeln, gemessen am Grundgesetz. [m2]Die Menschenwürde "
     "schützt sie nach der Rechtsprechung auch gegen die Einwilligung, und das Unionsrecht lässt dieses Schutzniveau "
     "zu.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
