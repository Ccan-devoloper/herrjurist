"""Folge 012 · Zivilprozess Ablauf: Von der Klage bis zur Vollstreckung (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall (frei erfunden): Frau Seidel verkauft Herrn Krüger ihr Klavier für 8.000 Euro; er holt es ab, zahlt aber nicht und
behauptet, die Tasten klemmten. Stationen: I. zuständiges Gericht (§ 23 Nr. 1 GVG n. F. bis 10.000 €, § 71 GVG, §§ 12, 13 ZPO,
§ 78 ZPO) → II. Klageerhebung (§§ 253, 261 ZPO, § 204 I Nr. 1 BGB, Online-Verfahren §§ 1122 ff. ZPO) → III. Verfahrenseinleitung
(§§ 272, 276 ZPO) mit Abzweig Versäumnisurteil (§§ 331 III, 338, 339, 342, 330 ZPO) → IV. mündliche Verhandlung (§§ 278, 128a,
284, 402, 286 ZPO) → V. Urteil (§§ 300, 313 ZPO) → VI. Berufung (§§ 511, 517 ZPO, § 72 GVG) → VII. Rechtskraft und
Zwangsvollstreckung (§§ 705, 704, 724, 750, 753, 754a, 808 ZPO). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache (Vorgabe des Kanalinhabers): Seidel, Krüger; Richterin und Gerichtsvollzieher ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Seidel": "hilde", "Krueger": "niklas", "Richterin": "sabrina", "Gerichtsvollzieher": "christian"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: das Klavier ----------------------------------------------------------------------------------------
    ("[fall]Frau Seidel verkauft ihr altes Klavier. [krueger]Herr Krüger kauft es für achttausend Euro "
     "[abholen]und holt es gleich ab. [zahlt]Doch er zahlt nicht.", 0.3),
    ("[k1]Die Tasten klemmen. Dafür zahle ich keine achttausend Euro!", 0.4, "Krueger"),
    ("[s1]Das Klavier ist in Ordnung. Dann sehen wir uns vor Gericht!", 0.5, "Seidel"),
    ("[frage]Wie kommt Frau Seidel an ihr Geld? Ihr Weg führt durch den ganzen Zivilprozess.", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Zuständiges Gericht -----------------------------------------------------------------------------------
    ("[gericht]Erste Station: Welches Gericht ist zuständig? [sachl]Sachlich kommt es hier auf den Streitwert an. Die "
     "Amtsgerichte sind für Ansprüche bis zehntausend Euro zuständig, Paragraf dreiundzwanzig Nummer eins "
     "Gerichtsverfassungsgesetz. [lg]Alles andere gehört vor das Landgericht, Paragraf einundsiebzig. "
     "[neu]Diese Grenze gilt seit Januar zweitausendsechsundzwanzig, vorher waren es fünftausend Euro.", P),
    ("[oertl]Örtlich kann Frau Seidel am Wohnsitz von Herrn Krüger klagen, Paragrafen zwölf und dreizehn der Zivilprozessordnung. "
     "[anwalt]Einen Anwalt braucht sie vor dem Amtsgericht nicht.", PS),
    # --- D II. Klageerhebung ----------------------------------------------------------------------------------------
    ("[klage]Zweite Station: die Klage. Die Klageschrift nennt Parteien und Gericht, einen bestimmten Antrag und den "
     "Grund des Anspruchs, Paragraf zweihundertdreiundfünfzig. [antrag]Hier: Krüger soll achttausend Euro zahlen, aus "
     "dem Kaufvertrag.", P),
    ("[zust]Das Gericht stellt die Klage von Amts wegen zu. [rh]Damit ist sie erhoben und die Sache rechtshängig, "
     "Paragraf zweihunderteinundsechzig. [verj]Die Verjährung ist jetzt gehemmt. [online]Neu: Amtsgerichte, die dafür "
     "bestimmt sind, erproben für solche Geldklagen ein Online-Verfahren.", PS),
    # --- E III. Verfahrenseinleitung -------------------------------------------------------------------------------
    ("[weg]Dritte Station: Die Richterin wählt zwischen frühem ersten Termin und schriftlichem Vorverfahren, Paragraf "
     "zweihundertzweiundsiebzig. [vv]Sie entscheidet sich für das Vorverfahren. [frist1]Will Krüger sich verteidigen, muss er "
     "das binnen zwei Wochen anzeigen. [frist2]Für die Klageerwiderung bekommt er mindestens zwei weitere Wochen, "
     "Paragraf zweihundertsechsundsiebzig.", PS),
    # --- F Abzweig: Versäumnisurteil --------------------------------------------------------------------------------
    ("[vu]Ein Abzweig: Hätte Krüger geschwiegen, ergeht auf Antrag ein Versäumnisurteil ohne mündliche Verhandlung, "
     "Paragraf dreihunderteinunddreißig Absatz drei, [schl]soweit die Klage schlüssig ist. [eins]Dagegen hilft der "
     "Einspruch binnen zwei Wochen, Paragraf dreihundertneununddreißig. [zurueck]Ist er zulässig, geht der Prozess dort "
     "weiter, wo er vor der Säumnis stand.", PS),
    # --- G IV. Mündliche Verhandlung: Gerichtssaal -----------------------------------------------------------------
    ("[mv]Krüger verteidigt sich aber: Das Klavier sei mangelhaft. Vierte Station: der Termin. "
     "[guete]Zuerst kommt die Güteverhandlung, Paragraf zweihundertachtundsiebzig.", 0.3),
    ("[r1]Können Sie sich nicht einigen?", 0.4, "Richterin"),
    ("[k2]Nein. Die Tasten klemmen!", 0.5, "Krueger"),
    # --- H IV. Streitige Verhandlung und Beweisaufnahme -----------------------------------------------------------
    ("[streit]Es folgt die streitige Verhandlung. "
     "[beweis]Streitig ist, ob die Tasten klemmen. Darüber erhebt das Gericht Beweis, hier "
     "durch einen Sachverständigen, Paragrafen zweihundertvierundachtzig folgende. [gutachten]Sein Gutachten: Das "
     "Klavier ist in Ordnung.", PS),
    # --- I V. Urteil ------------------------------------------------------------------------------------------------
    ("[urteil]Fünfte Station: das Urteil. Ist der Rechtsstreit entscheidungsreif, ergeht ein Endurteil, Paragraf "
     "dreihundert. [aufbau]Es besteht aus Rubrum, Tenor, Tatbestand und Entscheidungsgründen, Paragraf "
     "dreihundertdreizehn.", 0.3),
    ("[r2]Der Beklagte wird verurteilt, an die Klägerin achttausend Euro zu zahlen.", PS, "Richterin"),
    # --- J VI. Berufung ---------------------------------------------------------------------------------------------
    ("[beruf]Sechste Station: die Berufung, Paragraf fünfhundertelf. [wert]Der Wert des Beschwerdegegenstands muss "
     "tausend Euro übersteigen, früher waren es sechshundert. Sonst braucht es eine Zulassung. [beschwer]Krüger könnte die vollen achttausend "
     "Euro angreifen. [frist]Die Frist: ein Monat ab Zustellung des vollständigen Urteils, Paragraf fünfhundertsiebzehn.", PS),
    # --- K VII. Rechtskraft und Zwangsvollstreckung -----------------------------------------------------------------
    ("[rk]Krüger lässt die Frist verstreichen. Das Urteil wird rechtskräftig, Paragraf siebenhundertfünf. "
     "[nichts]Gezahlt hat er trotzdem nicht. [zv]Letzte Station: die Zwangsvollstreckung. "
     "[titel]Die Klägerin braucht einen Titel: das Urteil, rechtskräftig oder vorläufig vollstreckbar, Paragraf siebenhundertvier. "
     "[klausel]Die Klausel: Die Geschäftsstelle erteilt eine vollstreckbare Ausfertigung, Paragraf "
     "siebenhundertvierundzwanzig. [zustellung]Und die Zustellung des Urteils an Krüger, spätestens bei Beginn der "
     "Vollstreckung, Paragraf siebenhundertfünfzig.", P),
    ("[gv]Dann beauftragt sie den Gerichtsvollzieher. [digital]Seit Oktober zweitausendsechsundzwanzig "
     "genügen dafür Titel und Klausel als elektronische Dokumente, Paragraf siebenhundertvierundfünfzig a.", 0.3),
    # --- L Bei Krüger -----------------------------------------------------------------------------------------------
    ("[g1]Guten Tag, Herr Krüger. Ich komme wegen des Urteils.", 0.4, "Gerichtsvollzieher"),
    ("[pfand]Er kann etwa das Klavier pfänden. [siegel]Es bleibt in der Regel bei Krüger, ein Siegel zeigt die Pfändung, "
     "Paragraf achthundertacht.", PS),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp für die Anwaltsklausur: Notiere zuerst die Fristen. Zwei Wochen für die Verteidigungsanzeige und "
     "den Einspruch, ein Monat für die Berufung. [tipp2]In der Urteilsklausur hilft die Relation: Ist die Klage "
     "schlüssig, die Verteidigung erheblich? Erst dann geht es um Beweis.", PS),
    # --- N Klausurschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [sI]Römisch eins: zuständiges Gericht. [sII]Römisch zwei: Klageerhebung durch Zustellung. "
     "[sIII]Römisch drei: Vorverfahren oder früher erster Termin, Abzweig Versäumnisurteil. [sIV]Römisch vier: "
     "Verhandlung und Beweisaufnahme. [sV]Römisch fünf: Urteil. [sVI]Römisch sechs: Berufung. [sVII]Römisch sieben: "
     "Rechtskraft und Zwangsvollstreckung.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Urteil klärt, wer recht hat. [m2]Durchsetzen lässt es sich erst mit Titel, Klausel und "
     "Zustellung.", 1.4),
]
