"""Folge 077 · Polizeirecht Schema: Standardmaßnahme vor Generalklausel (Mi · Examenswissen · Öffentliches Recht/Polizei- und
Ordnungsrecht). Beispielfall nach dem Hook des Themenplans, Beispielland Nordrhein-Westfalen (PolG NRW ab 13.12.2025,
OBG NRW ab 01.07.2026, LImschG NRW, VersG NRW, VwVfG NRW):
Herr Schröder feiert nachts mit zwei Freunden im Stadtpark Geburtstag; eine Musikbox läuft laut. Anwohnerin Frau Krämer ruft
die Polizei. Frau Götz (Polizei) bittet die Gruppe, leiser zu sein; eine Stunde später ist die Box wieder voll aufgedreht.
Das Ordnungsamt ist nachts nicht erreichbar. Frau Götz verweist alle drei bis 6 Uhr morgens aus dem Park.
Prüfung: Ermächtigungsgrundlage (Vorrang Spezialgesetz – hier keine Versammlung, § 2 III VersG NRW; Standardmaßnahme vor
Generalklausel, Wortlautkarten § 8 I und § 34 I 1 PolG NRW); formell (§ 1 I 3 PolG NRW, § 24o OBG NRW, § 28 I, II Nr. 1 und
§ 37 II VwVfG NRW); materiell: konkrete Gefahr für die öffentliche Sicherheit (OVG NRW 15 A 2100/18 Rn. 72; 5 A 2807/19
Rn. 67), § 117 I OWiG und § 9 I LImschG NRW (Wortlaut), Verhaltensstörer § 4 I PolG NRW, Ermessen § 3 I, Verhältnismäßigkeit
§ 2, zeitlich (OVG NRW 5 B 14/23 Rn. 20) und räumlich begrenzt (OVG NRW 5 A 2807/19 Rn. 70 f., 77), Abgrenzung § 34 II;
Rechtsschutz: Fortsetzungsfeststellungsklage (OVG NRW 5 A 2807/19 Rn. 30, 56; Verweis auf das Video zu den Klagearten).
Fiktive Figuren: Herr Schröder (stephan), Frau Götz (lucy), Frau Krämer (hilde); zwei Freunde sprechen nicht.
Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Schröder": "stephan", "Götz": "lucy", "Krämer": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Geburtstag im Park -------------------------------------------------------------------------------------
    ("[fall]Samstagnacht in einer Stadt in Nordrhein-Westfalen. [gruppe]Herr Schröder feiert mit zwei Freunden im Stadtpark "
     "seinen Geburtstag. [box]Eine Musikbox läuft laut, die drei singen mit. [kraemer]Gegen Mitternacht ruft Frau Krämer die "
     "Polizei. Sie wohnt direkt am Park.", 0.2),
    ("[kr1]Ich kann nicht schlafen. Die Musik dröhnt bis in mein Schlafzimmer.", 0.3, "Krämer"),
    # --- B Fall: die Polizei kommt --------------------------------------------------------------------------------------
    ("[goetz]Frau Götz von der Polizei kommt in den Park.", 0.2),
    ("[go1]Bitte machen Sie die Musik leiser. Die Nachbarn wollen schlafen.", 0.3, "Götz"),
    ("[sch1]Klar, machen wir.", 0.3, "Schröder"),
    ("[wieder]Eine Stunde später ruft Frau Krämer wieder an. [laut]Die Box ist wieder voll aufgedreht.", 0.2),
    # --- C Fall: der Platzverweis ----------------------------------------------------------------------------------------
    ("[zurueck]Frau Götz kommt zurück.", 0.15),
    ("[go2]Sie verlassen jetzt bitte alle den Park, bis morgen früh um sechs.", 0.3, "Götz"),
    ("[sch2]Wir sitzen doch nur auf der Wiese. Auf welcher Grundlage eigentlich?", 0.4, "Schröder"),
    # --- D Frage -----------------------------------------------------------------------------------------------------------
    ("[frage]War der Platzverweis rechtmäßig?", 0.6),
    # --- E Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Aufbau, Landesrecht -----------------------------------------------------------------------------------------------
    ("[aufbau]Du prüfst wie bei jeder polizeilichen Maßnahme: [a1]Ermächtigungsgrundlage, [a2]formelle [a3]und materielle "
     "Rechtmäßigkeit. [land]Polizeirecht ist Landesrecht. Wir nehmen Nordrhein-Westfalen als Beispiel. Die anderen Länder "
     "haben ähnliche Regeln, oft unter anderer Nummer.", P),
    # --- G Ermächtigungsgrundlage: Reihenfolge, Versammlungsrecht ---------------------------------------------------------------
    ("[egl]Der Platzverweis greift in die Rechte von Herrn Schröder ein. Dafür braucht die Polizei eine gesetzliche Grundlage. "
     "[reihe]Gesucht wird sie in fester Reihenfolge: [r1]zuerst Spezialgesetze, [r2]dann Standardmaßnahmen, [r3]zuletzt die "
     "Generalklausel. [vers]Ein Spezialgesetz wäre hier das Versammlungsrecht. Eine Versammlung verlangt aber ein Treffen zur "
     "Teilhabe an der öffentlichen Meinungsbildung. Eine Geburtstagsfeier ist das nicht.", P),
    # --- H Generalklausel, Wortlaut § 8 I PolG NRW --------------------------------------------------------------------------------
    ("[wl8]Die Generalklausel in Paragraf acht des Polizeigesetzes regelt den Vorrang selbst: Die Polizei kann die notwendigen "
     "Maßnahmen treffen, um eine konkrete Gefahr abzuwehren, [soweit]soweit nicht die Paragrafen neun bis sechsundvierzig die "
     "Befugnisse besonders regeln. [warum]Der Grund: Standardmaßnahmen regeln typische Eingriffe in Grundrechte genauer, mit "
     "eigenen Voraussetzungen und Grenzen. So ist klar bestimmt, was die Polizei darf und wo Schluss ist. [offen]Die Generalklausel bleibt für Lagen, "
     "die das Gesetz nicht eigens regelt. [leiser]Auf sie stützt sich deshalb die Aufforderung, die Musik leiser zu machen. "
     "[sicher]Würde die Polizei die Box mitnehmen, wäre das wieder eine Standardmaßnahme: die Sicherstellung.", P),
    # --- I Standardmaßnahme, Wortlaut § 34 I 1 PolG NRW ----------------------------------------------------------------------------
    ("[wl34]Für den Platzverweis gibt es eine Standardmaßnahme, Paragraf vierunddreißig Absatz eins: Die Polizei kann zur "
     "Abwehr einer Gefahr eine Person vorübergehend von einem Ort verweisen. [egl34]Das ist unsere Ermächtigungsgrundlage.", P),
    # --- J Formelle Rechtmäßigkeit ----------------------------------------------------------------------------------------------
    ("[formell]Formell: [zust]Für die Gefahrenabwehr ist auch das Ordnungsamt zuständig. Es hat seit Juli "
     "zweitausendsechsundzwanzig eine eigene Vorschrift für den Platzverweis. [eil]Nachts ist es aber nicht erreichbar. Dann handelt "
     "die Polizei in eigener Zuständigkeit. [anh]Eine Anhörung kann entfallen, wenn wegen Gefahr im Verzug sofort "
     "entschieden werden muss, so wie hier. [form]Und der Platzverweis darf mündlich ergehen.", P),
    # --- K Materiell: Tatbestand ------------------------------------------------------------------------------------------------
    ("[mat]Materiell zuerst der Tatbestand: [gefahr]eine konkrete Gefahr für die öffentliche Sicherheit. [def]Dazu gehören "
     "die Gesundheit des Einzelnen und die Unversehrtheit der Rechtsordnung. [konkret]Konkret ist die Gefahr, wenn ohne "
     "Eingreifen in überschaubarer Zukunft ein Schaden hinreichend wahrscheinlich ist. [owi]Nach Paragraf hundertsiebzehn des "
     "Ordnungswidrigkeitengesetzes handelt ordnungswidrig, wer in unzulässigem oder vermeidbarem Ausmaß Lärm erregt, der "
     "geeignet ist, die Nachbarschaft erheblich zu belästigen. [nacht]In Nordrhein-Westfalen sind außerdem von zweiundzwanzig "
     "bis sechs Uhr Betätigungen verboten, welche die Nachtruhe zu stören geeignet sind. [subs]Die Musik dröhnt bis ins "
     "Schlafzimmer, und trotz der Bitte wurde sie wieder laut. Weitere Verstöße sind also hinreichend wahrscheinlich. "
     "[gja]Eine konkrete Gefahr liegt vor.", P),
    # --- L Adressat ----------------------------------------------------------------------------------------------------------------
    ("[adr]Richtiger Adressat ist, wer die Gefahr verursacht, Paragraf vier: der Verhaltensstörer. [alle]Alle drei feiern "
     "laut mit. Jeder trägt zum Lärm bei, also darf sich der Platzverweis an alle richten.", P),
    # --- M Rechtsfolge: Ermessen, Verhältnismäßigkeit, Grenzen ---------------------------------------------------------------------
    ("[rf]Auf der Rechtsfolgenseite hat die Polizei Ermessen und muss verhältnismäßig handeln. [geeig]Der Platzverweis "
     "beendet den Lärm, er ist geeignet. [erf]Er ist erforderlich, denn das mildere Mittel war schon versucht: Die Bitte, "
     "leiser zu sein, hat nicht gehalten. [angem]Und angemessen: Ein paar Stunden außerhalb des Parks wiegen weniger als die "
     "Nachtruhe der Nachbarn. [grenze]Dabei muss er zeitlich und räumlich begrenzt sein. [zeit]Vorübergehend heißt: Die Dauer richtet sich nach der konkreten Gefahr. Hier endet die Nachtruhe um sechs Uhr. "
     "[raum]Und der Ort muss überschaubar sein. Für ein ganzes Stadtgebiet reicht Absatz eins nach dem "
     "Oberverwaltungsgericht Nordrhein-Westfalen nicht. Der Park ist ein bestimmter Ort. [abgr]Für längere Verbote gibt es "
     "das Aufenthaltsverbot in Absatz zwei. Es verlangt aber Tatsachen, die eine Straftat erwarten lassen, und gilt höchstens "
     "drei Monate.", PS),
    # --- N Ergebnis, Rechtsschutz ---------------------------------------------------------------------------------------------------
    ("[erg]Der Platzverweis war rechtmäßig. [rs]Will Herr Schröder sich trotzdem wehren, hat sich die Maßnahme am Morgen "
     "schon erledigt. Dann kommt die Fortsetzungsfeststellungsklage in Betracht. Mehr dazu im Video zu den Klagearten.", PS),
    # --- O Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Fang nie mit der Generalklausel an. [tipp2]Prüfe erst, ob ein Spezialgesetz oder eine "
     "Standardmaßnahme passt. Die Generalklausel nennst du nur, wenn keine passt. [tipp3]Und die Grenzen einer "
     "Standardmaßnahme darfst du nicht über die Generalklausel umgehen.", PS),
    # --- P Klausurschema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q1]Eins, Ermächtigungsgrundlage: Spezialgesetz, dann Standardmaßnahme, zuletzt "
     "Generalklausel. Hier Paragraf vierunddreißig Absatz eins. [q2]Zwei, formell: Zuständigkeit, Verfahren und Form. "
     "[q3]Drei, materiell: [q3a]der Tatbestand mit konkreter Gefahr, [q3b]der richtige Adressat [q3c]und die Rechtsfolge: "
     "Ermessen und Verhältnismäßigkeit, zeitlich und räumlich begrenzt.", PS),
    # --- Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst das Spezialgesetz, dann die Standardmaßnahme, zuletzt die Generalklausel. [m2]Und ein Platzverweis "
     "wehrt eine konkrete Gefahr ab, nur vorübergehend und nur für einen bestimmten Ort.", 1.4),
]
