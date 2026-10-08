"""Folge 266 · Polizeiliche Generalklausel: Meldeauflage für Hooligans erlaubt? (Mi · Examenswissen · Polizei- und
Ordnungsrecht · Schema). Beispielfall nach dem Plan-Hook, entschärft und ohne Klischee (keine echten Vereine, kein
Gewaltbild): Samstag, 15 Uhr, eine Polizeiwache in Nordrhein-Westfalen. Herr Schütte muss sich an den Samstagen der
nächsten drei Auswärtsspiele seines Vereins jeweils um 15 Uhr melden; Anpfiff ist um halb vier, 200 km entfernt.
Polizistin Feddersen nimmt die Meldung auf, Wachleiter Rabe nennt den Anlass (zwei Verurteilungen wegen Körperverletzung
bei Auswärtsspielen, Verabredung seiner Gruppe zu einer Schlägerei; Gefährderansprache im Sommer ohne Wirkung).
Aufbau (Schema): Ermächtigungsgrundlage – Sperrwirkung, Landesvergleich (§ 16a NPOG, § 20 SächsPVDG, § 15a BbgPolG;
NRW ohne eigene Norm, VG Düsseldorf 18 L 1554/24 Rn. 15) → Wortlautkarte § 8 Abs. 1 PolG NRW → Tragfähigkeit:
Art. 2 Abs. 1, Art. 11 GG, Zitiergebot § 7 PolG NRW, BVerwG 6 C 39.06 Rn. 33–36 (Zitatkarte Rn. 33), Grenze Vorfeld
(Rn. 34) → Abgrenzung § 10 PassG (Wortlautkarte), Zweck (BVerwG Rn. 29; VG Gelsenkirchen 17 L 615/23 Rn. 5, 7), Gegenfall
Auslandsspiel → Tatbestand: konkrete Gefahr (Verweis 257, Schutzgüter 213), Tatsachen, Verhaltensstörer → Ermessen und
Verhältnismäßigkeit (Gefährderansprache als milderes Mittel: OVG NRW 5 A 2532/14 Rn. 26; VG Minden 11 K 730/17 Rn. 41)
→ Ergebnis → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, nicht vergeben, eingetragen als „266: Schütte, Feddersen, Rabe“): Herr Schütte (niklas, Mann,
jung), Polizistin Feddersen (julia, Frau, jung), Wachleiter Rabe (helmut, Mann, älter); ela_froh nicht verwendet.
Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Schütte": "niklas", "Feddersen": "julia", "Rabe": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Polizeiwache, Samstag 15 Uhr ---------------------------------------------------------------------------
    ("[fall]Samstag, fünfzehn Uhr, eine Polizeiwache in Nordrhein-Westfalen. [schuette]Herr Schütte kommt herein, in der "
     "Hand ein Schreiben der Polizei. [auflage]An den Samstagen der nächsten drei Auswärtsspiele seines Vereins muss er sich "
     "jeweils um fünfzehn Uhr hier melden. [anstoss]Angepfiffen wird um halb vier, zweihundert Kilometer entfernt.", P),
    ("[fe1]Guten Tag, Herr Schütte. Ihre Meldung ist notiert.", P, "Feddersen"),
    ("[sc1]Ich will doch nur Fußball sehen. Darf die Polizei mich einfach hierher bestellen?", P, "Schütte"),
    ("[rabe]Wachleiter Rabe kennt den Vorgang.", P),
    ("[ra1]Sie wurden zweimal wegen Körperverletzung bei Auswärtsspielen verurteilt. Und Ihre Gruppe hat sich für heute "
     "zu einer Schlägerei verabredet.", 0.4, "Rabe"),
    ("[gespraech]Schon im Sommer hatte die Polizei ihn gewarnt, in einer Gefährderansprache. "
     "[frage]Darf die Polizei Herrn Schütte zur Meldung verpflichten? [frage2]Und worauf stützt sie die Meldeauflage, wenn "
     "das Polizeigesetz sie gar nicht nennt?", PS),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Ermächtigungsgrundlage: Sperrwirkung, Landesvergleich ---------------------------------------------------------
    ("[egl]Erster Schritt: die Ermächtigungsgrundlage. Spezielle Befugnisse und Standardmaßnahmen gehen der Generalklausel "
     "vor; sie entfalten eine Sperrwirkung. [v077]Den Aufbau zeigt Folge siebenundsiebzig. [spez]Gibt es also eine eigene "
     "Befugnis für Meldeauflagen? Das hängt vom Land ab.", P),
    ("[tni]Niedersachsen regelt die Meldeauflage in Paragraf sechzehn a, [tsn]Sachsen in Paragraf zwanzig, [tbb]Brandenburg "
     "in Paragraf fünfzehn a. [tsperr]Dort ist die Generalklausel insoweit gesperrt. "
     "[tvor]Diese Normen reichen teils über die konkrete Gefahr hinaus: Es genügen Tatsachen, die eine ihrer Art nach "
     "konkretisierte Straftat erwarten lassen. [tdauer]Dafür befristen sie die Auflage, in Sachsen und Brandenburg auf "
     "einen Monat, in Niedersachsen auf drei Monate. [tnrw]Nordrhein-Westfalen hat keine solche Norm; "
     "das hat das Verwaltungsgericht Düsseldorf ausdrücklich festgestellt. [tdein]In deinem Land kann das anders sein.", P),
    ("[wl8]Also bleibt hier die Generalklausel, Paragraf acht Absatz eins: Die Polizei kann die notwendigen Maßnahmen "
     "treffen, um eine im einzelnen Falle bestehende, konkrete Gefahr für die öffentliche Sicherheit oder Ordnung "
     "abzuwehren, [soweit]soweit nicht die Paragrafen neun bis sechsundvierzig die Befugnisse der Polizei besonders "
     "regeln.", PS),
    # --- D Trägt die Generalklausel? Grundrechte und Wesentlichkeit -------------------------------------------------------
    ("[trag]Aber trägt die Generalklausel einen so spürbaren Eingriff? [grund]Die Meldeauflage greift in die allgemeine "
     "Handlungsfreiheit ein, Artikel zwei Absatz eins Grundgesetz, und ist regelmäßig mit einer Beschränkung der "
     "Freizügigkeit verbunden, Artikel elf. [art11]Artikel elf schützt, überall im Bundesgebiet Aufenthalt zu nehmen. "
     "Absatz zwei erlaubt Einschränkungen auf gesetzlicher Grundlage, um strafbaren Handlungen vorzubeugen, wenn das "
     "erforderlich ist. [zitier]Das Polizeigesetz nennt die Freizügigkeit "
     "im Zitiergebot, Paragraf sieben.", P),
    ("[wes]Kritiker meinen: Was die Polizei häufig einsetzt, braucht eine eigene Befugnis. [bvg]Das "
     "Bundesverwaltungsgericht folgt dem nicht. [bvg2]Die Generalklausel ist durch jahrzehntelange Rechtsprechung "
     "hinreichend bestimmt und nicht auf untypische Fälle beschränkt. [bvg3]Und die Meldeauflage ist an Intensität nicht "
     "mit einer Freiheitsentziehung vergleichbar. [vorfeld]Die Grenze: Eingriffe schon im Vorfeld einer Gefahr brauchen "
     "eine spezielle Grundlage. Die Generalklausel verlangt eine konkrete Gefahr.", PS),
    # --- E Abgrenzung: § 10 Passgesetz -------------------------------------------------------------------------------------
    ("[pass]Abzugrenzen ist das Passgesetz. [wl10]Nach Paragraf zehn können die Grenzbehörden "
     "einem Deutschen die Ausreise untersagen, wenn Tatsachen die Annahme rechtfertigen, dass Gründe für eine "
     "Passversagung vorliegen, [p7]etwa eine Gefährdung erheblicher Belange der Bundesrepublik. [ansehen]Dazu kann das "
     "internationale Ansehen Deutschlands zählen, wenn gewalttätige Fans im Ausland auftreten. [ausreise]Die Ausreise "
     "schützt Artikel zwei Absatz eins. [neben]Generalklausel und Passgesetz verfolgen verschiedene Ziele und sind "
     "nebeneinander anwendbar. [zweck]Soll eine Meldeauflage aber nur die Ausreise verhindern, um das Ansehen zu "
     "schützen, haben die Passvorschriften Vorrang. Auf die Generalklausel gestützt, muss sie Straftaten verhindern.", P),
    ("[ausl]Spielte der Verein im Ausland, könnte die Bundespolizei Herrn Schütte die Ausreise untersagen, [ausl2]und die "
     "Meldeauflage bliebe daneben möglich. [inl]Hier wird im Inland gespielt; das Passgesetz greift nicht.", PS),
    # --- F Tatbestand: konkrete Gefahr, Störer -------------------------------------------------------------------------------
    ("[tb]Nun der Tatbestand: eine konkrete Gefahr; die Definition zeigt Folge zweihundertsiebenundfünfzig. [prog]Hier "
     "drohen Körperverletzungen bei der verabredeten Schlägerei; zu den Schutzgütern siehe Folge zweihundertdreizehn. [tats]Die Prognose stützt sich auf Tatsachen: zwei einschlägige Verurteilungen und die Verabredung vor "
     "diesem Spiel. [indiz]Die Zugehörigkeit zur Fanszene kann mitzählen; frühere Ermittlungsverfahren muss die Polizei "
     "aber aktuell und einzeln auswerten. [stoer]Herr Schütte würde die Taten selbst begehen; er ist "
     "Verhaltensstörer. [gefja]Eine konkrete Gefahr liegt vor.", PS),
    # --- G Ermessen und Verhältnismäßigkeit ---------------------------------------------------------------------------------
    ("[vh]Rechtsfolge: Ermessen, begrenzt durch die Verhältnismäßigkeit. [geeig]Geeignet: Wer um fünfzehn Uhr auf der "
     "Wache steht, ist um halb vier nicht im Stadion, zweihundert Kilometer entfernt. [mild]Erforderlich: Milder wäre eine "
     "erneute Gefährderansprache, die je nach Inhalt nicht einmal ein Grundrechtseingriff ist; im Sommer blieb sie aber "
     "ohne Wirkung. [angem]Angemessen: Geschützt werden Leib und Gesundheit vieler Menschen, und die Auflage gilt nur an "
     "drei Spieltagen. [ort]Bei Verhinderung darf er sich laut Verfügung nach Absprache "
     "woanders melden. [erg]Ergebnis: Die Meldeauflage ist rechtmäßig.", PS),
    # --- H Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst, ob dein Landesgesetz eine eigene Meldeauflage kennt. [tipp1]Nur wenn nicht, gehst du "
     "zur Generalklausel und begründest kurz, warum sie den Eingriff trägt. [tipp2]Und benenne den Zweck: Straftaten "
     "verhindern, nicht bloß die Ausreise.", PS),
    # --- I Schema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Erstens, Ermächtigungsgrundlage: eigene Meldeauflage im Landesrecht? Sonst "
     "die Generalklausel. [s2]Zweitens, Abgrenzung zum Passgesetz nach dem Zweck. "
     "[s3]Drittens, formell: Zuständigkeit und Anhörung. [s4]Viertens, Tatbestand: konkrete Gefahr, auf Tatsachen gestützt, "
     "und der richtige Adressat. [s5]Fünftens, Ermessen und Verhältnismäßigkeit, mit der Gefährderansprache als milderem "
     "Mittel.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst die Spezialbefugnis, dann die Generalklausel. [m2]Sie trägt eine Meldeauflage, wenn konkret "
     "Straftaten drohen und die Auflage verhältnismäßig bleibt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
