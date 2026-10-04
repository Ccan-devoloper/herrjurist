"""Folge 171 · Belehrungsverstoß: Ist das Geständnis verwertbar? (Fr · Klausurpraxis · Strafrecht/StPO, Format Streitstand).
Fall nach dem angepassten Hook: Am Bahnhof fährt Herr Pieper auf einem fremden blauen Rad los; die Besitzerin ruft, das Schloss
liegt aufgebrochen im Korb. Polizeihauptmeister Lohmeyer fragt ihn ohne Belehrung „nur informatorisch“, wem das Rad gehört; er
gesteht. Auf der Wache wird er ordnungsgemäß belehrt, aber nicht darauf hingewiesen, dass das erste Geständnis unverwertbar ist
(keine qualifizierte Belehrung); er wiederholt das Geständnis. Seine Verteidigerin widerspricht in der Hauptverhandlung rechtzeitig.
Schwerpunkt anders als Folge 132 (dort Belehrungspflicht, BGHSt 38, 214, Widerspruchslösung, § 136a, Revision – hier nur ein
Verweissatz): I. Beschuldigtenstellung (Willensakt/Inkulpationsakt; Verdachtsstärke, Beurteilungsspielraum: BGH 1 StR 3/07 Rn. 17 f.;
BGHSt 53, 112 Rn. 8 f., 16) → II. Streitstand Verwertungsverbot (Abwägungslehre: BGHSt 54, 69 Rn. 47, BGHSt 38, 214, 219 f.;
Rechtskreistheorie: BGHSt 11, 213, 215, BGH 4 StR 61/22 Rn. 12; Schutzzwecklehre: Schrifttum) → III. Widerspruch (Verweis 132)
→ IV. Fortwirkung: qualifizierte Belehrung und Abwägung (BGHSt 53, 112 Rn. 10, 12–15; BGH 3 StR 390/17 Rn. 28 f.); Fernwirkung
grundsätzlich abgelehnt (BGH 1 StR 316/05 Rn. 22 f.) → Ergebnis → Klausurtipp mit Prüfungsaufbau (Lexi) → Merksatz.
Belege je Aussage: ../RECHTSSTAND.md. Namen (eindeutig deutsch, in keiner früheren Folge): Pieper, Lohmeyer; Besitzerin und
Verteidigerin bleiben Funktionsrollen ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Besitzerin": "ela_froh", "Lohmeyer": "helmut", "Pieper": "niklas"}  # Lexi = Erzählerin (Carla)

SEGMENTE = [
    # --- A Fall: am Bahnhof ---------------------------------------------------------------------------------------------
    ("[fall]Montagmorgen am Bahnhof. [rad]Herr Pieper fährt auf einem blauen Damenrad vom Fahrradständer los. "
     "[frau]Da läuft eine Frau auf ihn zu.", 0.2),
    ("[b1]Halt! Das ist mein Rad! Mein Schloss liegt aufgebrochen im Korb!", 0.35, "Besitzerin"),
    ("[pol]Polizeihauptmeister Lohmeyer steht gleich daneben und hält Herrn Pieper an. [schloss]Im Korb liegt tatsächlich "
     "das aufgebrochene Schloss, [schl]einen Schlüssel hat Herr Pieper nicht. [keinbel]Belehrt wird er nicht.", 0.3),
    ("[l1]Nur informatorisch gefragt: Wem gehört das Rad?", 0.35, "Lohmeyer"),
    ("[p1]Nicht mir. Ich hab es mir genommen, ich war spät dran.", 0.35, "Pieper"),
    # --- B Fall: auf der Wache ------------------------------------------------------------------------------------------
    ("[wache]Eine Stunde später auf der Wache. [belehrt]Jetzt belehrt Lohmeyer ihn ordnungsgemäß: Er darf schweigen "
     "und jederzeit einen Verteidiger befragen. [nichtges]Dass das erste Geständnis nicht verwertet werden darf, sagt er "
     "nicht.", 0.2),
    ("[p2]Hab ich doch schon gesagt. Ich habe das Rad genommen.", 0.35, "Pieper"),
    ("[hv]In der Hauptverhandlung widerspricht seine Verteidigerin rechtzeitig der Verwertung beider Geständnisse. "
     "[frage]Darf das Gericht das erste Geständnis verwerten? [frage2]Und das zweite?", 0.6),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D I. Beweiserhebungsverbot: Beschuldigtenstellung --------------------------------------------------------------
    ("[besch]Erster Schritt: Belehren muss die Polizei bei der Vernehmung nur den Beschuldigten. [akt]Beschuldigter wird "
     "man durch einen Willensakt der Strafverfolgung, den sogenannten Inkulpationsakt, [akt2]etwa ein förmliches "
     "Ermittlungsverfahren oder eine Durchsuchung gegen den Verdächtigen. [staerke]Auch ohne einen solchen Akt kann man "
     "Beschuldigter sein, wenn der Verdacht stark genug ist. [spiel]Ob jemand ernstlich als Täter in Betracht kommt, "
     "beurteilt die Polizei pflichtgemäß, mit einem Spielraum. [grenze]Wäre alles andere aber willkürlich, muss sie ihn "
     "als Beschuldigten vernehmen.", P),
    ("[sub]Hier zeigt die Besitzerin auf ihr Rad, das Schloss liegt aufgebrochen im Korb, und einen Schlüssel hat Herr "
     "Pieper nicht. [jabesch]Herr Pieper war Beschuldigter, [etik]da ändert das Wort informatorisch nichts. "
     "[gegen]Anders bei jemandem, gegen den nur ein vager Verdacht spricht: Er darf als Zeuge befragt werden. "
     "[fehlt]Die Belehrung über Schweigerecht und Verteidiger fehlte also.", PS),
    # --- E II. Verwertungsverbot: Streitstand ---------------------------------------------------------------------------
    ("[vv]Zweiter Schritt: Folgt aus dem Fehler ein Verwertungsverbot? Ausdrücklich regelt das Gesetz das hier nicht. "
     "[lehren]Drei Lehren stehen sich gegenüber.", P),
    ("[abw]Die Rechtsprechung wägt ab: [abw2]die Art des Verbots und das Gewicht des Verstoßes [abw3]gegen das Interesse "
     "an der Aufklärung der Tat. [abw4]Ein Verwertungsverbot liegt nahe, wenn die verletzte Vorschrift die Grundlagen "
     "der Stellung des Beschuldigten sichert. [abw5]Genau das tut die Belehrung über das Schweigerecht.", P),
    ("[rk]Die Rechtskreistheorie fragt: Berührt der Fehler den Rechtskreis dessen, der sich darauf beruft? "
     "[rk2]Dient die verletzte Vorschrift nicht seinem Schutz, folgt für ihn kein Verwertungsverbot. "
     "[rk3]Die Belehrung schützt aber gerade Herrn Pieper.", P),
    ("[sz]Die Schutzzwecklehre aus dem Schrifttum fragt nach dem Zweck der verletzten Norm: [sz2]Würde die Verwertung "
     "ihn unterlaufen? [sz3]Die Belehrung soll verhindern, dass sich jemand unwissentlich selbst belastet. [sz4]Genau "
     "diese Selbstbelastung würde verwertet.", P),
    ("[gleich]Alle drei Lehren kommen hier zum selben Ergebnis: Das erste Geständnis ist unverwertbar. [streit]Den "
     "Streit muss man deshalb nicht entscheiden. [wid]Beim verteidigten Angeklagten gilt das aber nur bei rechtzeitigem "
     "Widerspruch, und den hat die Verteidigerin erhoben. [verw]Wie das genau läuft, zeigt unsere Folge zur "
     "Widerspruchslösung.", PS),
    # --- F IV. Fortwirkung: das zweite Geständnis -----------------------------------------------------------------------
    ("[fort]Dritter Schritt: Und das zweite Geständnis? [heil]Die spätere Belehrung macht das erste nicht nachträglich "
     "verwertbar. [qual]Der Bundesgerichtshof verlangt deshalb eine qualifizierte Belehrung: [qual2]den Hinweis, dass "
     "die frühere Aussage unverwertbar ist. [grund]Sonst verzichtet der Beschuldigte womöglich nur deshalb auf sein "
     "Schweigerecht, weil er glaubt, seine erste Selbstbelastung nicht mehr aus der Welt schaffen zu können.", P),
    ("[folge]Fehlt dieser Hinweis, ist die zweite Aussage aber nicht automatisch unverwertbar. [abwg]Es kommt auf eine "
     "Abwägung im Einzelfall an: [k1]das Gewicht des Verstoßes, [k2]das Interesse an der Aufklärung [k3]und vor allem, "
     "ob der Beschuldigte glaubte, von seinen früheren Angaben nicht mehr abrücken zu können. [wdh]Das liegt besonders "
     "nahe, wenn er sie nur wiederholt.", P),
    ("[bgh]Im Fall des Bundesgerichtshofs war es anders: [bgh2]Der Angeklagte hatte nach der Belehrung erstmals neue, "
     "sich selbst schwer belastende Angaben gemacht. [bgh3]Die Abwägung sprach dort gegen ein Verwertungsverbot.", P),
    ("[sub2]Herr Pieper dagegen wiederholt nur, was er schon gesagt hat. [sub3]Er glaubte, nicht mehr zurückzukönnen. "
     "[sub4]Und ein Fahrraddiebstahl ist kein schweres Delikt. [sub5]Hier spricht die Abwägung gegen die Verwertung: "
     "Auch das zweite Geständnis ist unverwertbar.", P),
    ("[fern]Davon zu trennen ist die Fernwirkung, also Beweise, die die Polizei erst durch ein unverwertbares Geständnis "
     "findet. [fern2]Sie lehnt der Bundesgerichtshof grundsätzlich ab.", P),
    ("[erg]Ergebnis: Beide Geständnisse sind unverwertbar. [erg2]Gegen Herrn Pieper bleiben die Besitzerin als Zeugin "
     "und das aufgebrochene Schloss.", PS),
    # --- G Klausurtipp mit Prüfungsaufbau (Lexi) -------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüf das Verwertungsverbot in vier Schritten. [t1]Erstens: Beweiserhebungsverbot. War er "
     "Beschuldigter, und fehlte die Belehrung? [t2]Zweitens: Verwertungsverbot nach Abwägung. [t2b]Den Streit der Lehren "
     "entscheidest du nur, wenn sie zu verschiedenen Ergebnissen kommen. [t3]Drittens: rechtzeitiger Widerspruch. "
     "[t4]Viertens: Fortwirkung auf spätere Aussagen, also qualifizierte Belehrung und erneute Abwägung.", PS),
    # --- H Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine spätere Belehrung heilt den ersten Fehler nicht. [mz]Fehlt die qualifizierte Belehrung, "
     "entscheidet die Abwägung über das zweite Geständnis.", 1.4),
]
