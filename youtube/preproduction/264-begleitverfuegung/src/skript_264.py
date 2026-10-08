"""Folge 264 · Begleitverfügung StA: Haft, Pflichtverteidiger, Mitteilungen (Fr · 2. Examen · StPO-Praxis · Formulierung).
Voraussetzung Folge 252 (Anklageschrift § 200 StPO): gleiche erfundene Staatsanwaltschaft Ahornstadt, neuer Fall, nichts
aus 252 wiederholt. Plan-Hook: „Der Beschuldigte sitzt seit drei Monaten in Untersuchungshaft, als deine Anklage fertig ist.“
Fall: Referendarin Ortlieb hat die Anklage gegen Herrn Wittig fertig (Einbruch in das Lager eines Baumarkts in der Nacht zum
21.6.2026, Werkzeug für 7.800 €; Kamera, Werkzeug im Transporter sichergestellt, Aufnahme auf USB-Stick). Haftbefehl wegen
Fluchtgefahr (Wohnung gekündigt, Flug gebucht), Festnahme und Vorführung am 9.7.2026, seitdem Untersuchungshaft und
Pflichtverteidigerin. Zweite Anzeige von Herrn Dengler (E-Bike im Mai aus dem Hof verschwunden), Wittig dazu als Beschuldigter
vernommen, bestreitet; kein hinreichender Tatverdacht. Oberstaatsanwältin Pfaff fragt nach der Begleitverfügung.
Ablauf: Fall → Frage → Sachverhalt → Wozu (Abgrenzung zur Anklage, kein Widerspruch, Form je Land) → Muster I.–VI.:
I. Vermerk „Haft“ (Nr. 52 RiStBV) und Abschlussvermerk § 169a StPO (Wortlaut), § 147 Abs. 2 StPO; II. Teileinstellung
§ 170 Abs. 2 StPO (Wortlautkarte), § 154 StPO, Bescheid § 171 S. 1 (Wortlautkarte), Belehrung S. 2, § 172 Abs. 1;
III. Haft: § 120, Nr. 54 RiStBV; Fortdauerantrag in der Anklage (Nr. 110 Abs. 4 RiStBV, § 207 Abs. 4 StPO); § 121 Abs. 1
(Wortlautkarte), Frist notieren, § 122 Abs. 1, Nr. 56 RiStBV; IV. § 140 Abs. 1 Nr. 4, 5 (Wortlautkarte), § 141 Abs. 2 S. 1
Nr. 1, § 143 Abs. 1, § 142 Abs. 2; V. Mitteilungen (Nr. 108 RiStBV, § 145a StPO; MiStra allgemein), Asservate (§ 111n
Abs. 1, 2, Nr. 75 RiStBV); VI. Anklage mit den Akten an das Gericht (§ 199 Abs. 2 S. 2) → zwei typische Fehler (§§ 154,
154a, 264; § 121 Abs. 2, 3) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, nicht vergeben, in namen_reserviert.txt eingetragen): Ortlieb, Pfaff, Wittig, Dengler.
Stimmen nur aus dem Pool: Ortlieb lucy (Frau, jung), Pfaff hilde (Frau, älter), Dengler stephan (Mann, mittel);
christian nicht gebraucht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ortlieb": "lucy", "Pfaff": "hilde", "Dengler": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Büro der Referendarin ------------------------------------------------------------------------------
    ("[fall]Donnerstagmorgen bei der Staatsanwaltschaft Ahornstadt. [ortlieb]Referendarin Ortlieb hat die Anklage gegen "
     "Herrn Wittig fertig. [haft]Auf dem Aktendeckel steht in Rot: Haft. [pfaff]Da schaut Oberstaatsanwältin Pfaff herein.", 0.3),
    ("[p1]Die Anklage ist gut. Aber Herr Wittig sitzt seit drei Monaten in Untersuchungshaft. Wo ist Ihre "
     "Begleitverfügung?", 0.3, "Pfaff"),
    ("[o1]Die fehlt noch. Was gehört denn da hinein?", 0.4, "Ortlieb"),
    # --- B Fall: was in der Akte steht ------------------------------------------------------------------------------
    ("[akte]In der Akte: [lager]In der Nacht zum einundzwanzigsten Juni bricht jemand in das Lager eines Baumarkts ein und "
     "nimmt Werkzeug für siebentausendachthundert Euro mit. [kamera]Eine Kamera zeigt Herrn Wittig; [transp]das Werkzeug "
     "findet die Polizei in seinem Transporter. [hb]Weil er seine Wohnung gekündigt und einen Flug gebucht hat, erlässt das "
     "Amtsgericht Haftbefehl wegen Fluchtgefahr. [fest]Am neunten Juli wird er festgenommen und dem Richter vorgeführt; "
     "seitdem hat er eine Pflichtverteidigerin. [dengler]Außerdem zeigt Herr Dengler ihn an: Im Mai sei aus seinem Hof ein "
     "E-Bike verschwunden.", 0.3),
    ("[d1]Der war damals doch auch bei uns in der Straße!", 0.3, "Dengler"),
    ("[d2]Wittig bestreitet; mehr gibt die Akte nicht her. [nur]Angeklagt ist deshalb nur der Einbruch.", 0.3),
    ("[frage]Was gehört neben der Anklage in die Begleitverfügung, und wie vermeidest du Widersprüche?", 0.5),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Wozu die Begleitverfügung --------------------------------------------------------------------------------
    ("[wozu]Wozu die Begleitverfügung? [anklage]Die Anklageschrift geht an das Gericht und beschreibt die angeklagte Tat. "
     "[bv]Die Begleitverfügung ordnet an, was die Staatsanwaltschaft daneben veranlasst. [kein]Sie darf der Anklage nie "
     "widersprechen. [land]Ihre Form unterscheidet sich von Land zu Land; maßgeblich sind die Hinweise deines Prüfungsamts.", PS),
    # --- E Kopf und Punkt I: Vermerk ----------------------------------------------------------------------------------
    ("[kopf]Ganz oben steht der Vermerk Haft, [kopf2]denn in Haftsachen tragen ihn alle "
     "Verfügungen. [v1]Punkt eins: der Vermerk nach Paragraf hundertneunundsechzig a. [v1w]Erwägt die Staatsanwaltschaft, die "
     "öffentliche Klage zu erheben, so vermerkt sie den Abschluss der Ermittlungen in den Akten. [v1f]Ab jetzt darf der "
     "Verteidigerin die Akteneinsicht nicht mehr mit Rücksicht auf den Untersuchungszweck versagt werden.", PS),
    # --- F Punkt II: Teileinstellung, Mitteilung, Bescheid ----------------------------------------------------------
    ("[e]Punkt zwei: die Teileinstellung. [e1]Das E-Bike ist eine andere Tat, und der Verdacht reicht nicht für eine "
     "Anklage. [e2]Also gilt Paragraf hundertsiebzig Absatz zwei: Andernfalls stellt die Staatsanwaltschaft das Verfahren "
     "ein. [e3]Davon erfährt Wittig, denn er wurde dazu als Beschuldigter vernommen. [e154]Bei einer nachweisbaren Tat, deren "
     "Strafe daneben nicht beträchtlich ins Gewicht fällt, kann sie nach Paragraf hundertvierundfünfzig absehen.", P),
    ("[e4]Herr Dengler bekommt nach Paragraf hunderteinundsiebzig einen Bescheid mit Gründen, keine Floskel. [e5]Als "
     "Verletzter wird er über die Beschwerde und ihre Frist von zwei Wochen belehrt.", PS),
    # --- G Punkt III: Haft ------------------------------------------------------------------------------------------
    ("[h]Punkt drei: die Haft. [h1]Liegen dringender Tatverdacht und Fluchtgefahr noch vor, und ist die Haft noch "
     "verhältnismäßig? [h2]Dann gehört ein bestimmter Antrag zur Fortdauer schon in die Anklageschrift, mit Ort und Dauer "
     "der Haft; so verlangen es die Richtlinien für das Strafverfahren. [h3]Die Verfügung muss "
     "dazu passen.", P),
    ("[h121]Dann die Sechsmonatsfrist aus Paragraf hunderteinundzwanzig Absatz eins. [h4]Über sechs Monate hinaus darf die "
     "Untersuchungshaft wegen derselben Tat nur dauern, wenn besondere Schwierigkeit, besonderer Umfang der Ermittlungen "
     "oder ein anderer wichtiger Grund das Urteil noch nicht zulassen und die Fortdauer rechtfertigen. [h5]Wittig sitzt seit dem neunten Juli; die Frist "
     "läuft also Anfang Januar ab. [h6]Die Verfügung notiert sie, damit die Akten rechtzeitig zum Oberlandesgericht "
     "gelangen, wenn die Haft länger dauern muss.", PS),
    # --- H Punkt IV: Pflichtverteidigung ----------------------------------------------------------------------------
    ("[pv]Punkt vier: die Pflichtverteidigung. [pv1]Nach Paragraf hundertvierzig Absatz eins Nummer vier ist die "
     "Verteidigung notwendig, wenn der Beschuldigte einem Gericht zur Entscheidung über Haft vorzuführen ist. [pv2]Solange "
     "er auf richterliche Anordnung in der Anstalt sitzt, greift Nummer fünf. [pv3]Wittig hat seit der Vorführung eine "
     "Pflichtverteidigerin; ihre Bestellung gilt grundsätzlich bis zum Abschluss des Verfahrens. [pv4]Fehlt sie in deiner Akte, "
     "beantragt die Staatsanwaltschaft unverzüglich die Bestellung.", PS),
    # --- I Punkt V: Mitteilungen und Asservate ----------------------------------------------------------------------
    ("[mi]Punkt fünf: Mitteilungen und Asservate. [mi1]Jede Entscheidung, die Wittig mitgeteilt wird, erfährt seine Verteidigerin zugleich. "
     "[mi2]Dazu kommen Mitteilungen an andere Stellen, wenn die Anordnung über Mitteilungen in Strafsachen sie vorsieht. "
     "[as1]Das Werkzeug braucht das Verfahren nicht mehr im Original; es geht an den Baumarkt zurück, dem es entzogen wurde. "
     "[as2]Der USB-Stick mit der Aufnahme bleibt verwahrt, denn er ist Beweismittel.", PS),
    # --- J Punkt VI: Anklage mit den Akten an das Gericht -----------------------------------------------------------
    ("[vi]Punkt sechs: Die Anklageschrift geht an das Amtsgericht Ahornstadt, Schöffengericht. [vi1]Mit ihr werden die "
     "Akten dem Gericht vorgelegt, so steht es in Paragraf hundertneunundneunzig.", 0.3),
    ("[p2]Gut. Jetzt passt die Verfügung zur Anklage, Punkt für Punkt.", 0.4, "Pfaff"),
    # --- K Typische Fehler -------------------------------------------------------------------------------------------
    ("[fehler]Zwei Fehler sieht man in Klausuren immer wieder. [f1]Erstens: Die Verfügung stellt einen Teil der angeklagten "
     "Tat nach Paragraf hundertsiebzig Absatz zwei ein. [f1b]Das widerspricht der Anklage. [f1c]Eingestellt wird nur eine "
     "andere Tat; innerhalb derselben Tat hilft allenfalls eine Beschränkung nach Paragraf hundertvierundfünfzig a. "
     "[f2]Zweitens: Die Sechsmonatsfrist wird übersehen. [f2b]Dann ist der Haftbefehl nach Ablauf aufzuheben, wenn nicht das "
     "Oberlandesgericht die Fortdauer anordnet oder der Vollzug ausgesetzt wird. [f2c]Werden die Akten dem "
     "Oberlandesgericht vor Ablauf vorgelegt, ruht die Frist bis zur Entscheidung.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lege Gutachten, Anklage und Begleitverfügung nebeneinander. [tipp1]Jede Tat ist entweder "
     "angeklagt oder eingestellt, keine doppelt und keine vergessen. [tipp2]Und ordne nur an, was Akte oder Bearbeitervermerk verlangen.", PS),
    # --- M Schema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Muster auf einen Blick. [s1]Erstens: Vermerk über den Abschluss der Ermittlungen. [s2]Zweitens: "
     "Teileinstellung mit Mitteilung und Bescheid. [s3]Drittens: Haft, mit Fortdauer und Sechsmonatsfrist. [s4]Viertens: "
     "Pflichtverteidigung. [s5]Fünftens: Mitteilungen und Asservate. [s6]Sechstens: Anklage mit den Akten ans "
     "Gericht.", PS),
    # --- N Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Anklage sagt dem Gericht, was angeklagt ist. [m2]Die Begleitverfügung erledigt alles daneben und "
     "widerspricht der Anklage nie.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
