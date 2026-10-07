"""Folge 233 · Fortsetzungsfeststellungsklage § 113 I 4 VwGO – Prüfungsschema (Mi · Examenswissen ·
Verwaltungsprozessrecht · Schema). Fiktiver Übungsfall nach dem Hook des Themenplans („Die Polizei hat deine Demo aufgelöst –
sie ist vorbei, aber du willst wissen, ob das rechtens war“), Beispielland Nordrhein-Westfalen:
Samstagmittag auf dem Marktplatz. Jördis leitet eine angemeldete Demo für mehr Radwege (rund 40 Menschen, neutral, keine
Parolen). Ein einzelner Teilnehmer sprüht Farbe an eine Hauswand und hört trotz Jördis' Bitte nicht auf. Polizeihauptkommissar
Hinze löst die ganze Versammlung auf. Die Demo ist vorbei; Jördis plant die nächste, die Polizei würde wieder so handeln.
Zwei Wochen später klagt Jördis.
Aufbau: Erledigung § 43 II VwVfG (Wortlautkarte) → A. Zulässigkeit: I. Rechtsweg (kurz), II. statthafte Klageart § 113 I 4
VwGO (Wortlautkarte; direkt nach Klageerhebung, BVerwG 4 C 33.13 Rn. 13; analog vor Klageerhebung, BVerwG 6 C 2.22 Rn. 15,
OVG NRW 5 A 2000/20 Rn. 25 f.; a. A. Feststellungsklage § 43, BayVGH 10 BV 17.2405 Rn. 20; Verpflichtungssituation analog,
4 C 33.13 Rn. 13), III. Fortsetzungsfeststellungsinteresse (BVerwGE 146, 303 = 8 C 14.12 Rn. 20, 21, 25, 32, 44; 6 C 2.22
Rn. 16–22; Präjudiz nur nach Klageerhebung OVG NRW 5 A 2000/20 Rn. 68, BVerwG 2 C 27.15 Rn. 15; Versammlung: BVerfGE 110,
77 Rn. 37, 41–43), IV. Klagebefugnis analog § 42 II, V. Vorverfahren (§ 110 I 1 JustG NRW), VI. Frist (BayVGH 10 BV 17.2405
Rn. 21 f. mit BVerwG 6 C 7.98; a. A. Schmidt in Eyermann; Verwirkung Rn. 23 f.) → B. Begründetheit: § 13 II 1 VersG NRW
(Bund: § 15 III VersG), formell (§ 32, § 13 IV 2 VersG NRW), materiell (milderes Mittel § 14 III VersG NRW; Brokdorf,
BVerfGE 69, 315 Rn. 92 – nur verwiesen), Rechtsverletzung Art. 8 GG → Klausurtipp, Schema, Merksatz mit Lexi.
Keine Tenorierung (Thema der Folge 234). Belege je Cue: ../RECHTSSTAND.md.
Stimmen (Pool stephan, hilde, christian, lucy): Jördis lucy (Frau, jung), Hinze stephan (Mann, mittel).
Erzählerin und Lexi: Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Jördis": "lucy", "Hinze": "stephan"}

SEGMENTE = [
    # --- A Fall: Samstagmittag auf dem Marktplatz -------------------------------------------------------------------------
    ("[fall]Samstagmittag auf dem Marktplatz. [joerdis]Jördis leitet eine angemeldete Demo für mehr Radwege. "
     "[farbe]Plötzlich sprüht ein einzelner Teilnehmer Farbe an eine Hauswand. Er hört nicht auf, "
     "obwohl Jördis ihn darum bittet. [hinze]Polizeihauptkommissar Hinze greift ein.", 0.2),
    ("[hi1]Wegen der Farbe an der Wand: Die Versammlung ist aufgelöst. Bitte verlassen Sie den Platz.", P, "Hinze"),
    ("[jo1]Aber wir anderen sind doch friedlich!", P, "Jördis"),
    ("[vorbei]Die Menschen gehen nach Hause, die Demo ist vorbei. [naechst]Jördis plant schon die nächste Demo am selben "
     "Ort, und die Polizei bleibt dabei: Sie würde wieder so handeln. [klage]Zwei Wochen später klagt Jördis beim "
     "Verwaltungsgericht. [frage]Kann man gegen eine Auflösung klagen, die längst vorbei ist? [frage2]Das Prüfungsschema der "
     "Fortsetzungsfeststellungsklage, am Beispiel Nordrhein-Westfalen.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Ausgangslage: Erledigung, § 43 Abs. 2 VwVfG (Wortlautkarte) -----------------------------------------------------
    ("[va]Die Auflösung ist ein Verwaltungsakt: Sie beendet die Versammlung, alle müssen gehen. "
     "[wl43]Nach Paragraf dreiundvierzig Absatz zwei Verwaltungsverfahrensgesetz bleibt er nur wirksam, "
     "solange er nicht aufgehoben oder auf andere Weise erledigt ist. [erl]Die Demo ist vorbei, die Auflösung regelt nichts mehr: Sie hat sich erledigt. [leer]Eine "
     "Anfechtungsklage ginge ins Leere.", P),
    # --- D A. Zulässigkeit: Rechtsweg, statthafte Klageart, § 113 Abs. 1 Satz 4 VwGO (Wortlautkarte) -----------------------
    ("[rweg]A, Zulässigkeit. Erstens, der Verwaltungsrechtsweg: Versammlungsrecht ist öffentliches Recht. "
     "[wl113]Zweitens, die statthafte Klageart. Paragraf hundertdreizehn Absatz eins Satz vier Verwaltungsgerichtsordnung: "
     "Hat sich der Verwaltungsakt vorher durch Zurücknahme oder anders erledigt, so spricht das Gericht auf Antrag durch "
     "Urteil aus, dass der Verwaltungsakt rechtswidrig gewesen ist, wenn der Kläger ein berechtigtes Interesse an dieser "
     "Feststellung hat. [direkt]Direkt passt die Norm, wenn sich der Verwaltungsakt erst nach Klageerhebung erledigt. "
     "[analog]Bei Jördis war die Auflösung schon vor der Klage erledigt. Die Rechtsprechung wendet die Norm dann entsprechend "
     "an. [streit]Manche in der Literatur nehmen stattdessen die allgemeine Feststellungsklage. [verpfl]Und hat sich ein "
     "Verpflichtungsbegehren erledigt, gilt die Norm ebenfalls entsprechend.", P),
    # --- E III. Fortsetzungsfeststellungsinteresse: vier Fallgruppen ---------------------------------------------------------
    ("[ffi]Drittens, das berechtigte Interesse, kurz Fortsetzungsfeststellungsinteresse. Das Urteil muss die Lage der "
     "Klägerin rechtlich, wirtschaftlich oder ideell verbessern können. [fg]Dafür gibt es vier "
     "Fallgruppen.", P),
    ("[wh]Erstens, die Wiederholungsgefahr: Es droht konkret, dass unter im Wesentlichen gleichen Umständen ein gleichartiger "
     "Verwaltungsakt ergeht. [wh2]Genau das droht Jördis bei der nächsten Demo.", P),
    ("[reha]Zweitens, die Rehabilitation: Die Maßnahme stempelt jemanden ab, nach außen sichtbar und bis heute. [reha2]Die "
     "Polizei hat Jördis nichts Ehrenrühriges vorgeworfen, das trägt hier also nicht.", P),
    ("[praej]Drittens, das Präjudizinteresse: Das Urteil soll einen Prozess um Amtshaftung vorbereiten, der nicht offensichtlich "
     "aussichtslos ist. [praej2]Das gilt aber nur bei Erledigung nach Klageerhebung: Dann soll die "
     "Mühe des bisherigen Prozesses nicht umsonst sein. [praej3]Für Jördis scheidet es aus.", P),
    ("[tief]Viertens, der tiefgreifende Grundrechtseingriff bei Maßnahmen, die sich typischerweise erledigen, bevor ein "
     "Gericht in der Hauptsache entscheiden kann. [tief2]Das Bundesverwaltungsgericht hat "
     "zweitausendvierundzwanzig klargestellt: Beides muss vorliegen, die kurze Dauer und ein gewichtiger Eingriff. "
     "[tief3]Nach dem Bundesverfassungsgericht ist die Auflösung die schwerste Beeinträchtigung der Versammlungsfreiheit. "
     "Und sie endet mit der Demo. [tief4]Auch diese Fallgruppe greift.", P),
    # --- F IV.–VII. weitere Zulässigkeit -------------------------------------------------------------------------------------
    ("[kb]Viertens, die Klagebefugnis, entsprechend Paragraf zweiundvierzig Absatz zwei: Als Leiterin der aufgelösten Demo "
     "kann Jördis in ihrer Versammlungsfreiheit aus Artikel acht Grundgesetz verletzt sein. [vv]Fünftens, das Vorverfahren: In "
     "Nordrhein-Westfalen entfällt es nach Paragraf hundertzehn Justizgesetz. In deinem Land kann das anders sein.", P),
    ("[frist]Sechstens, die Frist. Erledigt sich der Verwaltungsakt vor der Klage und noch innerhalb der Monatsfrist, "
     "gilt Paragraf vierundsiebzig nach der Rechtsprechung nicht. [frist2]Manche in der Literatur sehen "
     "das anders. [frist3]Zwei Wochen "
     "sind ohnehin unproblematisch. [rest]Die übrigen Punkte prüfst du wie bei der Anfechtungsklage. [zul]Die Klage ist "
     "zulässig.", PS),
    # --- G B. Begründetheit -----------------------------------------------------------------------------------------------
    ("[begr]B, Begründetheit. Die Klage ist begründet, wenn die Auflösung rechtswidrig war und Jördis in ihren Rechten "
     "verletzt hat. [egl]Ermächtigungsgrundlage in Nordrhein-Westfalen: Paragraf dreizehn Absatz zwei "
     "Versammlungsgesetz. [egl2]Auflösen darf die Behörde, wenn die Versammlung die öffentliche Sicherheit unmittelbar "
     "gefährdet und die Gefahr nicht anders abgewehrt werden kann. [bund]Hat dein Land kein eigenes Gesetz, gilt Paragraf "
     "fünfzehn Absatz drei des Versammlungsgesetzes des Bundes. [formell]Formell: Zuständig ist die Kreispolizeibehörde, und "
     "Herr Hinze hat den Grund genannt.", P),
    ("[mat]Materiell: Die Farbe an der Wand ist eine Sachbeschädigung, die öffentliche Sicherheit ist also gefährdet. "
     "[mild]Aber sie ging von einem Einzelnen aus. Die Polizei hätte ihn aus der Versammlung ausschließen können, Paragraf "
     "vierzehn Absatz drei. [brok]Friedliche Teilnehmer bleiben geschützt, wenn Einzelne Ausschreitungen begehen. Mehr dazu "
     "in unserem Video zum Brokdorf-Beschluss. [rw]Die Auflösung war rechtswidrig [rv]und verletzte Jördis in ihrer "
     "Versammlungsfreiheit. [erg]Die Klage ist zulässig und begründet.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Stell den Zeitpunkt der Erledigung an den Anfang. [tipp1]Er entscheidet, ob du Paragraf "
     "hundertdreizehn direkt oder entsprechend anwendest, [tipp2]ob ein Präjudizinteresse möglich ist [tipp3]und ob eine "
     "Frist läuft. [tipp4]In der Begründetheit prüfst du wie bei der Anfechtungsklage, nur in der "
     "Vergangenheit.", PS),
    # --- I Klausurschema (Lexi) --------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Verwaltungsrechtsweg, [s2]statthafte Klageart, direkt oder "
     "entsprechend, [s3]Fortsetzungsfeststellungsinteresse, [s4]Klagebefugnis, [s5]Vorverfahren, [s6]Frist, [s7]übrige "
     "Voraussetzungen. [sb]B, Begründetheit: [s8]Der Verwaltungsakt war rechtswidrig [s9]und verletzte den Kläger in seinen "
     "Rechten.", PS),
    # --- J Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erledigt heißt nicht schutzlos. [m2]Bei berechtigtem Interesse stellt das Gericht fest, dass der "
     "Verwaltungsakt rechtswidrig war.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), "Marke doppelt"
