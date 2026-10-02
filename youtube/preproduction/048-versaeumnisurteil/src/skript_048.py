"""Folge 048 · Versäumnisurteil Voraussetzungen: § 331 ZPO und unechtes VU (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall (Plan-Hook): Herr Baumann verkauft Frau Ehlers seine Wiese am Dorfrand (ein Grundstück) für 8.500 Euro, nur
mündlich per Handschlag, ohne Notar. Sie zahlt nicht; Klage zum Amtsgericht, früher erster Termin, Frau Ehlers erscheint
trotz ordnungsgemäßer Ladung nicht, Herr Baumann beantragt ein Versäumnisurteil. Prüfung: wer säumig ist (§ 330 / § 331 ZPO)
→ I. Antrag → II. Säumnis, § 333, kein Hindernis nach § 335 I Nr. 2, 3 → III. Zulässigkeit (von Amts wegen; BGH III ZR 344/20;
§ 331 I 2) → IV. Schlüssigkeit: Geständnisfiktion § 331 I 1, § 331 II; Formnichtigkeit §§ 311b I, 125 S. 1 BGB, keine Heilung
→ Hinweis § 139 ZPO → unechtes Versäumnisurteil (streitiges Endurteil, BGH I ZR 186/25 Rn. 11), Prozessurteil bei
Unzulässigkeit (BGH III ZR 344/20 Rn. 19), Berufung statt Einspruch (BGH IX ZB 59/20 Rn. 6) → Gegenfall echtes VU: Einspruch
§§ 338, 339, Wirkung § 342, zweites VU § 345 → VU im schriftlichen Vorverfahren § 331 III → Klausurtipp → Schema → Merksatz.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben:
Baumann, Ehlers; Richterin ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Baumann": "marc", "Ehlers": "ela_froh", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: auf der Wiese ------------------------------------------------------------------------------------------
    ("[fall]Herr Baumann will seine Wiese am Dorfrand verkaufen. [ehlers]Frau Ehlers ist interessiert. [preis]Am Zaun "
     "werden sich die beiden einig: achttausendfünfhundert Euro, [hand]besiegelt per Handschlag.", 0.3),
    ("[e1]Abgemacht! Ich nehme die Wiese.", 0.5, "Ehlers"),
    ("[notar]Einen Notar beauftragen die beiden nicht. [zahlt]Und Frau Ehlers zahlt nicht.", 0.4),
    # --- B Fall: im Sitzungssaal ----------------------------------------------------------------------------------------
    ("[klage]Herr Baumann klagt vor dem Amtsgericht auf den Kaufpreis. [schrift]In der Klageschrift schildert er offen "
     "die mündliche Einigung. [termin]Das Gericht bestimmt einen frühen ersten Termin.", 0.3),
    ("[r1]Ich rufe auf: Baumann gegen Ehlers.", 0.5, "Richterin"),
    ("[leer]Der Stuhl der Beklagten bleibt leer. Frau Ehlers ist ordnungsgemäß geladen, erscheint aber nicht.", 0.3),
    ("[b1]Dann beantrage ich ein Versäumnisurteil!", 0.5, "Baumann"),
    ("[frage]Bekommt er es? [frage2]Was prüft das Gericht, wenn eine Partei säumig ist?", 0.6),
    # --- C Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Wer ist säumig? -----------------------------------------------------------------------------------------------
    ("[wer]Zuerst: Wer ist säumig? [p330]Fehlt der Kläger, wird die Klage auf Antrag durch Versäumnisurteil abgewiesen, "
     "Paragraf dreihundertdreißig. Eine Schlüssigkeitsprüfung sieht die Norm nicht vor. [p331]Fehlt der Beklagte, gilt "
     "Paragraf dreihunderteinunddreißig. So hier.", PS),
    # --- E I. Antrag, II. Säumnis ----------------------------------------------------------------------------------------
    ("[antrag]Erste Voraussetzung: der Antrag des Klägers. Herr Baumann hat ihn gestellt. [saeum]Zweite: die Säumnis der "
     "Beklagten im Termin. Säumig ist auch, wer erscheint, aber nicht verhandelt. [p335]Und es darf kein Hindernis aus "
     "Paragraf dreihundertfünfunddreißig bestehen. [nr2]Nummer zwei: Die Beklagte muss ordnungsgemäß, insbesondere "
     "rechtzeitig, geladen sein. [nr3]Nummer drei: Was der Kläger vorträgt und beantragt, muss ihr rechtzeitig per "
     "Schriftsatz mitgeteilt worden sein. [zur]Sonst wird der Antrag zurückgewiesen. [hier2]Hier ist Frau Ehlers geladen, "
     "und die Klageschrift wurde ihr zugestellt. Sie ist säumig.", PS),
    # --- F III. Zulässigkeit ---------------------------------------------------------------------------------------------
    ("[zul]Dritte Voraussetzung: Die Klage muss zulässig sein. [amt]Das prüft das Gericht von Amts wegen, auch bei "
     "Säumnis. Fehlt etwa die Prozessfähigkeit, darf nach dem Bundesgerichtshof kein Versäumnisurteil ergehen. "
     "[s2]Und Vorbringen zur Zuständigkeit aus einer Vereinbarung über Gerichtsstand oder Erfüllungsort gilt nicht als "
     "zugestanden, Paragraf dreihunderteinunddreißig Absatz eins Satz zwei. [hier3]Hier klagt Herr Baumann am Wohnsitz von "
     "Frau Ehlers, und der Streitwert liegt unter zehntausend Euro. Die Klage ist zulässig.", PS),
    # --- G IV. Schlüssigkeit: Geständnisfiktion --------------------------------------------------------------------------
    ("[schl]Vierte Voraussetzung: die Schlüssigkeit. [gest]Nach Absatz eins ist das tatsächliche mündliche Vorbringen des "
     "Klägers als zugestanden anzunehmen. Das ist die Geständnisfiktion. [zug]Als zugestanden gilt also: Beide haben sich "
     "mündlich auf den Kauf der Wiese geeinigt, für achttausendfünfhundert Euro. [abs2]Absatz zwei: Soweit das den "
     "Klageantrag rechtfertigt, ergeht das Versäumnisurteil. Soweit nicht, ist die Klage abzuweisen.", PS),
    # --- H IV. Schlüssigkeit: Form ---------------------------------------------------------------------------------------
    ("[form]Und hier liegt das Problem. Ein Vertrag, durch den sich der eine Teil verpflichtet, das Eigentum an einem "
     "Grundstück zu übertragen oder zu erwerben, bedarf der notariellen Beurkundung, Paragraf dreihundertelf b BGB. "
     "[nichtig]Ohne diese Form ist er nichtig, Paragraf hundertfünfundzwanzig. [heil]Gültig würde er erst mit Auflassung "
     "und Eintragung ins Grundbuch. Beides fehlt. [unschl]Selbst als wahr unterstellt trägt der Vortrag also keinen "
     "Kaufpreisanspruch. Die Klage ist unschlüssig. [hinw]Darauf muss die Richterin hinweisen, Paragraf "
     "hundertneununddreißig.", 0.3),
    ("[r2]Ihr Kaufvertrag ist mangels notarieller Form nichtig.", 0.4, "Richterin"),
    ("[b2]Aber wir haben uns doch die Hand gegeben!", 0.5, "Baumann"),
    # --- I Das unechte Versäumnisurteil ----------------------------------------------------------------------------------
    ("[unecht]Der Handschlag genügt eben nicht. Das Gericht weist die Klage ab, obwohl die Beklagte fehlt. [streit]Das ist "
     "kein Versäumnisurteil, sondern ein streitiges Endurteil gegen den erschienenen Kläger. Man nennt es unechtes "
     "Versäumnisurteil. [unzul]Ebenso bei einer unzulässigen Klage: Sie wird durch Prozessurteil abgewiesen. [rm]Die "
     "Folge: Gegen das unechte Versäumnisurteil hilft kein Einspruch, sondern die Berufung. [inhalt]Ob ein Versäumnisurteil "
     "vorliegt, richtet sich nach dem Bundesgerichtshof nicht maßgeblich nach der Überschrift, sondern nach dem Inhalt.", PS),
    # --- J Gegenfall: das echte Versäumnisurteil -------------------------------------------------------------------------
    ("[gegen]Anders, wenn der Vertrag notariell beurkundet ist. Dann ist die Klage schlüssig, [echt]und gegen Frau Ehlers "
     "ergeht ein echtes Versäumnisurteil. Ob sie wirklich gekauft hat, prüft das Gericht nicht.", 0.3),
    ("[e2]Dagegen lege ich Einspruch ein.", 0.4, "Ehlers"),
    ("[einspr]Das kann sie, binnen zwei Wochen ab Zustellung, Paragrafen dreihundertachtunddreißig und "
     "dreihundertneununddreißig. Die Frist ist eine Notfrist. [p342]Ist der Einspruch zulässig, kehrt der Prozess in die "
     "Lage vor der Säumnis zurück, Paragraf dreihundertzweiundvierzig. [p345]Bleibt sie danach wieder aus, verwirft ein "
     "zweites Versäumnisurteil den Einspruch, ohne weiteren Einspruch, Paragraf dreihundertfünfundvierzig.", PS),
    # --- K Versäumnisurteil im schriftlichen Vorverfahren ----------------------------------------------------------------
    ("[vv]Es geht sogar ohne Termin. Im schriftlichen Vorverfahren muss die Beklagte binnen zwei Wochen anzeigen, dass sie "
     "sich verteidigen will. [vv2]Tut sie das nicht, entscheidet das Gericht auf Antrag des Klägers ohne mündliche "
     "Verhandlung, Paragraf dreihunderteinunddreißig Absatz drei. [vv3]Den Antrag kann er schon in der Klageschrift "
     "stellen.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bleibt der Beklagte aus, prüfst du nicht nur die Säumnis, sondern auch Zulässigkeit und "
     "Schlüssigkeit. [tipp2]Und unterliegt der erschienene Kläger, entwirfst du kein Versäumnisurteil, sondern ein "
     "streitiges Urteil mit Tatbestand und Entscheidungsgründen.", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für das Versäumnisurteil gegen den Beklagten. [s0]Vorab: Wer fehlt? Der Kläger, Paragraf "
     "dreihundertdreißig, oder der Beklagte, Paragraf dreihunderteinunddreißig. [sI]Römisch eins: Antrag des Klägers. "
     "[sII]Römisch zwei: Säumnis des Beklagten, ordnungsgemäß geladen, Vorbringen rechtzeitig mitgeteilt. [sIII]Römisch "
     "drei: Zulässigkeit der Klage. [sIV]Römisch vier: Schlüssigkeit, mit Geständnisfiktion. [serg]Liegt alles vor: echtes "
     "Versäumnisurteil, dagegen Einspruch. [serg2]Scheitert die Klage an Zulässigkeit oder Schlüssigkeit: unechtes "
     "Versäumnisurteil, dagegen Berufung.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Säumnis ersetzt das Geständnis, nicht die Schlüssigkeit. [mz]Trägt der Vortrag den Antrag nicht, "
     "verliert der Kläger auch vor einem leeren Stuhl.", 1.4),
]
