"""Folge 225 · Staatshaftungsrecht Überblick: Welche Ansprüche hast du? (Fr · Klausurpraxis · Öffentliches Recht/
Staatshaftungsrecht, Format Schema). Übersicht mit drei Mini-Fällen nach dem Plan-Hook („Die Stadt beschädigt deinen Zaun,
schleppt dein Auto zu Unrecht ab und blockiert monatelang deinen Laden – welche Ansprüche hast du?“), Beispielland
Nordrhein-Westfalen (StrWG NRW, OBG NRW), Figuren fiktiv:
Herr Bergner wohnt über seinem kleinen Fahrradladen. Die Stadt baut die Straße davor um. (1) Ein Baggerfahrer des
städtischen Bauhofs fährt beim Rangieren gegen seinen Gartenzaun (Amtshaftung). (2) Sein Auto wird abgeschleppt, obwohl es
außerhalb des Haltverbots stand; er zahlt 250 € laut Kostenbescheid, dazu 30 € Taxi (Primärebene: Anfechtung, Rückzahlung
als Folgenbeseitigung; Sekundärebene: Entschädigung für rechtswidrige Maßnahmen nach Landesrecht, Overlay NRW/BB/SN).
(3) Die Baustelle versperrt fünf Monate lang den Zugang zum Laden, ohne Behelfsweg; der Laden steht vor dem Aus (keine
Enteignung, Art. 14 Abs. 3 GG; enteignungsgleicher/enteignender Eingriff, Aufopferungsgedanke; Anliegerentschädigung
§ 20 Abs. 6 StrWG NRW). Danach Übersicht „Welcher Anspruch wann?“, Rechtsweg, Klausurtipp und Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben und reserviert (namen_reserviert.txt): Bergner, Wilmsen.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Bergner william, Frau Wilmsen laura_ruhig. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal (per Assertion geprüft). Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Bergner": "william", "Wilmsen": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Baustelle vor dem Fahrradladen ------------------------------------------------------------------------
    ("[fall]Herr Bergner wohnt über seinem kleinen Fahrradladen. [umbau]Die Stadt baut die Straße davor um. [zaun]Dabei fährt "
     "ein Bagger des städtischen Bauhofs gegen seinen Gartenzaun. [auto]Ein paar Tage später ist sein Auto weg, abgeschleppt, "
     "obwohl es außerhalb des Haltverbots stand. [laden]Und die Baustelle versperrt fünf Monate lang den Weg in seinen Laden.",
     P),
    ("[be1]Mein Zaun ist kaputt, mein Auto war weg, und in meinen Laden kommt kein Kunde mehr!", P, "Bergner"),
    ("[wi1]Die Straße muss gemacht werden, Herr Bergner. Das trifft alle hier.", P, "Wilmsen"),
    ("[frage]Welche Ansprüche hat Herr Bergner gegen die Stadt?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Zwei Ebenen --------------------------------------------------------------------------------------------------------
    ("[ebenen]Sortiere in zwei Ebenen. [primaer]Auf der Primärebene wehrst du dich gegen die Maßnahme selbst. "
     "[sekundaer]Auf der Sekundärebene geht es um Geld: Schadensersatz oder Entschädigung.", PS),
    # --- D Amtshaftung: Wortlaut § 839 Abs. 1 Satz 1 BGB, Art. 34 Satz 1 GG ---------------------------------------------------
    ("[ah]Zuerst der Zaun: die Amtshaftung. [w839]Paragraf achthundertneununddreißig BGB: Verletzt ein "
     "Beamter vorsätzlich oder fahrlässig die ihm einem Dritten gegenüber obliegende Amtspflicht, so hat er dem Dritten den "
     "daraus entstehenden Schaden zu ersetzen. [w34]Artikel vierunddreißig GG leitet die Haftung um: Die Verantwortlichkeit "
     "trifft grundsätzlich den Staat oder die Körperschaft, in deren Dienst er steht.", PS),
    # --- E Amtshaftung: Prüfschema am Fall Zaun -------------------------------------------------------------------------------
    ("[s1]Erstens: Jemand handelt in Ausübung eines öffentlichen Amtes, ein Beamter im haftungsrechtlichen Sinn. [s1b]Das kann "
     "auch ein Angestellter sein, sogar ein privater Abschleppunternehmer. [s1c]Der Baggerfahrer ist beim Bauhof "
     "angestellt, und Straßenbau ist in Nordrhein-Westfalen hoheitliche Aufgabe. [s2]Zweitens: eine "
     "Amtspflichtverletzung. Amtsträger dürfen fremdes Eigentum nicht rechtswidrig beschädigen. [s3]Drittens: "
     "Drittbezogenheit. Die Pflicht schützt gerade den Eigentümer. [s4]Viertens: Verschulden. Der "
     "Fahrer hat nicht aufgepasst: fahrlässig. [s5]Fünftens: der Schaden, zwölfhundert Euro "
     "Reparatur. [s6]Sechstens: kein Ausschluss. Bei Fahrlässigkeit haftet der Staat nur, wenn es keinen anderen Ersatz "
     "gibt, [s6b]und nicht, wenn der Verletzte schuldhaft kein Rechtsmittel eingelegt hat. [s6c]Beides greift hier nicht. [s7]Die Stadt muss Herrn Bergner den Zaun ersetzen.", PS),
    # --- F Abschleppen: Primärebene (Anfechtung, Rückzahlung) --------------------------------------------------------------------
    ("[ab]Jetzt das Auto. Es stand außerhalb des Haltverbots, das Abschleppen war rechtswidrig. [konnex]Kosten darf die "
     "Stadt aber nur für ein rechtmäßiges Abschleppen verlangen. [anf]Auf der Primärebene ficht Herr Bergner den "
     "Kostenbescheid an. [rueck]Gezahlt hat er schon. Das Verwaltungsgericht kann zugleich aussprechen, dass die Stadt das Geld "
     "zurückzahlt. [fba]Dahinter steht die Folgenbeseitigung, dazu das Video "
     "zum Folgenbeseitigungsanspruch.", P),
    # --- G Abschleppen: Sekundärebene, Wortlaut § 39 Abs. 1 OBG NRW ------------------------------------------------------------
    ("[taxi]Und die dreißig Euro fürs Taxi? Das ist die Sekundärebene. [w39]In Nordrhein-Westfalen ersetzt Paragraf "
     "neununddreißig Ordnungsbehördengesetz Schäden durch rechtswidrige Maßnahmen der Ordnungsbehörden, gleichgültig, ob sie "
     "ein Verschulden trifft. [vermoegen]Ersetzt werden Vermögensschäden wie das Taxi.", P),
    # --- H Länder-Overlay ----------------------------------------------------------------------------------------------------
    ("[tab]Ein Blick in die Länder. [tnrw]In Nordrhein-Westfalen gilt das über Paragraf siebenundsechzig Polizeigesetz auch "
     "für die Polizei. [tbb]Brandenburg hat die Regel in Paragraf achtunddreißig Ordnungsbehördengesetz, [tsn]Sachsen in "
     "Paragraf einundvierzig Polizeibehördengesetz. [teigen]Für dein Land: Polizei- oder Ordnungsgesetz.", PS),
    # --- I Laden: keine Enteignung, Wortlaut Art. 14 Abs. 3 Satz 1, 2 GG -------------------------------------------------------
    ("[la]Bleibt der Laden. Ist das eine Enteignung? [w14]Artikel vierzehn Absatz drei: Eine Enteignung ist nur zum Wohle der "
     "Allgemeinheit zulässig. Sie darf nur durch Gesetz oder auf Grund eines Gesetzes erfolgen, das Art und Ausmaß der "
     "Entschädigung regelt. [entzug]Enteignung heißt nach dem Bundesverfassungsgericht: Der Staat entzieht konkretes Eigentum. "
     "[nichts]Herrn Bergner wird nichts entzogen.", PS),
    # --- J Laden: enteignungsgleicher und enteignender Eingriff ----------------------------------------------------------------
    ("[auf]Die Rechtsprechung hat aber zwei Entschädigungsansprüche entwickelt. Dahinter steht der Aufopferungsgedanke: Wer "
     "für das Gemeinwohl ein Sonderopfer bringt, wird entschädigt. [alr]Das ist gewohnheitsrechtlich anerkannt und geht auf das "
     "preußische Allgemeine Landrecht zurück. [egl]Erstens der enteignungsgleiche Eingriff: Der Staat greift "
     "rechtswidrig und unmittelbar in Eigentum ein, ein Verschulden braucht es nicht. [ee]Zweitens der enteignende Eingriff: "
     "Eine rechtmäßige Maßnahme hat untypische Nebenfolgen, die über das Zumutbare hinausgehen. [bau]Der Straßenumbau ist "
     "rechtmäßig: Hier geht es um den enteignenden Eingriff.", PS),
    # --- K Laden: Anliegerentschädigung, Wortlaut § 20 Abs. 6 StrWG NRW --------------------------------------------------------
    ("[anl]Normale Baustellen muss ein Anlieger hinnehmen. Für längere Straßenarbeiten gibt es aber eine eigene Regel, [w20]in Nordrhein-Westfalen Paragraf zwanzig Absatz sechs Straßen- und Wegegesetz. [m1]Zufahrten oder "
     "Zugänge sind für längere Zeit unterbrochen oder erheblich erschwert, [m2]Behelfsmaßnahmen helfen nicht wesentlich, [m3]und "
     "die wirtschaftliche Existenz eines anliegenden Betriebes ist gefährdet. [hoehe]Dann gibt es den Betrag, der das "
     "Fortbestehen des Betriebes sichert, nicht den ganzen entgangenen Gewinn. [lerg]Fünf Monate ohne Behelfsweg, der Laden "
     "vor dem Aus: Herr Bergner bekommt diese Entschädigung.", PS),
    # --- L Übersicht: Welcher Anspruch wann? --------------------------------------------------------------------------------
    ("[ueb]Welcher Anspruch passt wann? [u1]Dauert ein rechtswidriger Zustand an, hilft die Folgenbeseitigung. "
     "[u2]Rechtswidrig und schuldhaft: Amtshaftung auf Schadensersatz. [u3]Rechtswidrig, auch ohne Verschulden: "
     "enteignungsgleicher Eingriff oder eine Entschädigung nach Landesrecht. [u4]Rechtmäßig, aber ein Sonderopfer: enteignender "
     "Eingriff oder eine Sonderregel wie im Straßenrecht. [u5]Bei Opfern an Leben oder Gesundheit: der "
     "Aufopferungsanspruch.", PS),
    # --- M Rechtsweg ---------------------------------------------------------------------------------------------------------
    ("[rw]Und der Rechtsweg? [rw34]Artikel vierunddreißig Satz drei GG: Für den Anspruch auf Schadensersatz und für den "
     "Rückgriff darf der ordentliche Rechtsweg nicht ausgeschlossen werden. [rw40]Auch vermögensrechtliche Ansprüche aus Aufopferung "
     "für das gemeine Wohl gehören dorthin, Paragraf vierzig Absatz zwei VwGO. [rwvg]Kostenbescheid und Folgenbeseitigung klärt das "
     "Verwaltungsgericht.", PS),
    # --- N Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die Primärebene. [t1]Wer sich nicht wehrt, riskiert das Geld: Paragraf "
     "achthundertneununddreißig Absatz drei BGB. [t2]Bei einer rechtswidrigen Enteignung gibt es nach dem Bundesverfassungsgericht "
     "kein Wahlrecht: erst anfechten. [t3]Prüfe außerdem Amtshaftung und Entschädigung nebeneinander.", PS),
    # --- O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst abwehren, dann Geld. [mk2]Mit Verschulden zahlt der Staat Schadensersatz, ohne Verschulden "
     "Entschädigung, wenn ein Gesetz oder ein Sonderopfer sie trägt.", 1.2),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), f"Marke doppelt: {[m for m in _alle if _alle.count(m) > 1]}"
assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)

if __name__ == "__main__":
    txt = [_re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE]
    print(len(SEGMENTE), "Segmente,", len(_alle), "Marken,", sum(len(t) for t in txt), "Zeichen")
