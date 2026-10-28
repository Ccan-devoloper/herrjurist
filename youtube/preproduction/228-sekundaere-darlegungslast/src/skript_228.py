"""Folge 228 · Sekundäre Darlegungslast § 138 ZPO: Wenn nur der Gegner es weiß (Fr · 2. Examen · ZPO, Format Sonderlage).
Beispielfall nach dem Plan-Hook („Ein Rechteinhaber verklagt den Anschlussinhaber wegen Filesharings, obwohl vier Personen
im Haushalt denselben Router nutzen.“), Figuren fiktiv: Herr Mehnert ist Inhaber des Internetanschlusses der Familie;
Frau Mehnert, der 24-jährige Sohn und die 21-jährige Tochter nutzen ihn über eigene Geräte (WLAN mit Passwort, das alle
kennen). Eine Filmfirma ermittelt, dass am 12.5.2026 um 21:47 Uhr ein Spielfilm über den Anschluss in einer Tauschbörse
angeboten wurde, und verklagt Herrn Mehnert auf 1.000 € Schadensersatz (§ 97 Abs. 2 UrhG). Herr Mehnert bestreitet;
er hat alle gefragt, niemand hat etwas eingeräumt.
Aufbau (2.-Examens-Perspektive, Relation): 1. Grundsatz – Kläger trägt Darlegungs- und Beweislast für die Täterschaft
(BGH I ZR 169/12 BearShare Rn. 14; Verweis Folge 141); 2. § 138 Abs. 1, 2 ZPO (Wortlautkarte), § 138 Abs. 3 ZPO
(Wortlautkarte); 3. tatsächliche Vermutung (BearShare Rn. 15, I ZR 154/15 Afterlife Rn. 14), Voraussetzungen der
sekundären Darlegungslast (BearShare Rn. 17), Inhalt und Nachforschungspflicht (BearShare Rn. 18, Afterlife Rn. 15, 26),
keine Beweislastumkehr (BearShare Rn. 18); 4. Fall (BearShare Rn. 19 f.) und Gegenfall pauschales Bestreiten
(Afterlife Rn. 15, I ZR 19/16 Loud Rn. 15, 27, 29; Name des geständigen Kindes: Loud Leitsatz); 5. Klausurtipp Relation
(Beklagtenstation), Schema, Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben und reserviert (namen_reserviert.txt): Mehnert. Sohn, Tochter und
Anwältin bleiben ohne Namen.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Mehnert marc, Frau Mehnert sabrina, Anwältin laura_ruhig.
Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal (per Assertion geprüft). Zahlen und Paragrafen im Sprechtext als Wörter; „Urheberrechtsgesetz“ ausgeschrieben."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Herr Mehnert": "marc", "Frau Mehnert": "sabrina", "Anwältin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das Wohnzimmer der Familie Mehnert ------------------------------------------------------------------------
    ("[fall]Vier Menschen, ein Router. [haus]Bei Familie Mehnert surfen Herr und Frau Mehnert, ihr Sohn und ihre Tochter über "
     "denselben Internetanschluss. [brief]Dann kommt Post von einer Filmfirma. [vorwurf]Über diesen Anschluss sei ein Spielfilm "
     "in einer Tauschbörse zum Herunterladen angeboten worden, am zwölften Mai um einundzwanzig Uhr siebenundvierzig.", P),
    ("[me1]Ich war das nicht! Ich habe noch nie einen Film getauscht.", P, "Herr Mehnert"),
    ("[fm1]Aber bei uns hängen vier Leute am selben Router.", P, "Frau Mehnert"),
    # --- A2 Fall: die Klage ---------------------------------------------------------------------------------------------------
    ("[klage]Die Filmfirma verklagt Herrn Mehnert als Anschlussinhaber auf tausend Euro Schadensersatz. [anw]Ihre Anwältin "
     "hat ein einfaches Argument.", P),
    ("[aw1]Die IP-Adresse gehört zu Ihrem Anschluss. Also waren Sie es.", P, "Anwältin"),
    ("[frage]Aber wer bei den Mehnerts wann im Internet war, weiß nur die Familie. [frage2]Was muss Herr Mehnert dazu "
     "vortragen, und wer muss am Ende was beweisen?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau -------------------------------------------------------------------------------------------------------------
    ("[plan]Wir gehen in fünf Schritten vor: [p1]der Grundsatz, [p2]Paragraf hundertachtunddreißig ZPO, [p3]die sekundäre "
     "Darlegungslast, [p4]der Fall mit Gegenfall [p5]und die Relation.", PS),
    # --- D 1. Grundsatz -------------------------------------------------------------------------------------------------------
    ("[g1]Erstens: der Grundsatz. Die Filmfirma verlangt Schadensersatz nach Paragraf siebenundneunzig Absatz zwei "
     "Urheberrechtsgesetz. [g2]Als Anspruchstellerin trägt sie die Darlegungs- und Beweislast dafür, dass Herr Mehnert als "
     "Täter verantwortlich ist. So der Bundesgerichtshof. [g3]Die Täterschaft gehört zu den anspruchsbegründenden "
     "Tatsachen. Mehr dazu im Video zur Beweislast.", PS),
    # --- E 2. § 138 Abs. 1, 2 ZPO (Wortlaut) ------------------------------------------------------------------------------------
    ("[e1]Zweitens: Paragraf hundertachtunddreißig ZPO. [w1]Absatz eins: Die Parteien haben ihre Erklärungen über "
     "tatsächliche Umstände vollständig und der Wahrheit gemäß abzugeben. [w2]Absatz zwei: Jede Partei hat sich über die "
     "von dem Gegner behaupteten Tatsachen zu erklären.", P),
    # --- F 2. § 138 Abs. 3 ZPO (Wortlaut) --------------------------------------------------------------------------------------
    ("[w3]Absatz drei nennt die Folge: Tatsachen, die nicht ausdrücklich bestritten werden, sind als zugestanden anzusehen, "
     "wenn nicht die Absicht, sie bestreiten zu wollen, aus den übrigen Erklärungen der Partei hervorgeht. [w4]Herr Mehnert "
     "bestreitet ausdrücklich: Er war es nicht. [w5]Reicht das?", PS),
    # --- G 3. Vermutung und sekundäre Darlegungslast ------------------------------------------------------------------------
    ("[v1]Drittens: die sekundäre Darlegungslast. [v2]Konnte niemand sonst den Anschluss nutzen, spricht eine tatsächliche "
     "Vermutung dafür, dass der Anschlussinhaber der Täter ist. [v3]Ob andere ihn nutzen konnten, wissen aber nur die "
     "Mehnerts. Die Filmfirma sieht nur die IP-Adresse. [v4]Für solche Lagen gilt: Die darlegungsbelastete Partei hat keine "
     "nähere Kenntnis und kann nichts aufklären, dem Gegner sind nähere Angaben ohne weiteres möglich und zumutbar. [v5]Dann "
     "trifft den Gegner in der Regel eine sekundäre Darlegungslast.", PS),
    # --- H 3. Inhalt: Vortrag und Nachforschung ------------------------------------------------------------------------------
    ("[i1]Was muss Herr Mehnert vortragen? [i2]Ob andere Personen und gegebenenfalls welche selbständigen Zugang zu seinem "
     "Anschluss hatten und als Täter in Betracht kommen. [i3]Im Rahmen des Zumutbaren muss er dazu nachforschen und "
     "mitteilen, was er dabei erfahren hat. [i4]Den Computer seiner Frau muss er in der Regel aber nicht untersuchen, und "
     "ihre Internetnutzung muss er nicht dokumentieren.", P),
    # --- I 3. Keine Umkehr der Beweislast --------------------------------------------------------------------------------------
    ("[u1]Ganz wichtig: Die sekundäre Darlegungslast kehrt die Beweislast nicht um. [u2]Und über die Wahrheits- und "
     "Erklärungspflicht aus Paragraf hundertachtunddreißig Absatz eins und zwei hinaus muss Herr Mehnert der Filmfirma "
     "nicht alles liefern, was sie für ihren Prozesserfolg braucht.", PS),
    # --- J 4. Der Fall -----------------------------------------------------------------------------------------------------------
    ("[f1]Viertens: der Fall. Herr Mehnert hat alle gefragt und trägt vor:", 0.25),
    ("[me2]Meine Frau, mein Sohn und meine Tochter haben eigene Geräte und kennen das WLAN-Passwort. An dem Abend waren alle "
     "zu Hause.", P, "Herr Mehnert"),
    ("[f2]Zugegeben hat es niemand. [f3]Damit hat er seiner sekundären Darlegungslast genügt. Eine Vermutung gegen ihn greift "
     "nicht. [f4]Jetzt ist wieder die Filmfirma dran: Sie muss darlegen und beweisen, dass gerade Herr Mehnert den Film "
     "angeboten hat. [f5]Gelingt ihr das nicht, wird die Klage abgewiesen.", PS),
    # --- K 4. Der Gegenfall --------------------------------------------------------------------------------------------------
    ("[gf]Und der Gegenfall? Herr Mehnert sagt nur:", 0.25),
    ("[me3]Theoretisch könnte es jeder bei uns gewesen sein.", P, "Herr Mehnert"),
    ("[gf2]Das genügt nicht. Die pauschale Behauptung der bloß theoretischen Möglichkeit des Zugriffs reicht nach dem "
     "Bundesgerichtshof nicht. [gf3]Er muss nachvollziehbar sagen, wer nach Nutzerverhalten, Kenntnissen und Fähigkeiten und "
     "zur Tatzeit Gelegenheit hatte. [gf4]Sonst ist sein einfaches Bestreiten unwirksam: Nach Paragraf hundertachtunddreißig "
     "Absatz drei gilt die Behauptung der Filmfirma als zugestanden. [gf5]Die Vermutung greift, und Herr Mehnert haftet als "
     "Täter. [loud]Weiß er sogar, wer es war, etwa weil es ihm ein volljähriges Kind gestanden hat, muss er den Namen nennen, "
     "wenn er nicht selbst haften will.", PS),
    # --- L Klausurtipp (Lexi): Relation --------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp für die Relation: Die sekundäre Darlegungslast prüfst du in der Darlegungsstation, und zwar in der "
     "Beklagtenstation. [t1]Dort fragst du: Ist das Bestreiten erheblich? [t2]Pauschales Bestreiten ist unbeachtlich. Die "
     "Täterschaft gilt als zugestanden, eine Beweisstation brauchst du dafür nicht. [t3]Erst wenn der Beklagte genug "
     "vorgetragen hat, ist die Täterschaft streitig. Dann trägt in der Beweisstation der Kläger die Beweislast.", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Wer trägt die Darlegungslast? Grundsätzlich der Anspruchsteller. [k2]Römisch zwei: "
     "Fehlt ihm der Einblick, und kann der Gegner zumutbar mehr sagen? Dann trifft den Gegner die sekundäre Darlegungslast. "
     "[k3]Römisch drei: Hat der Gegner konkret vorgetragen, auch nach zumutbarer Nachforschung? [k4]Römisch vier: Wenn ja, "
     "beweist der Anspruchsteller. Wenn nein, gilt seine Behauptung als zugestanden.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer mehr weiß, muss mehr sagen. [mk2]Die sekundäre Darlegungslast verlangt Vortrag, keinen Beweis. Die "
     "Beweislast bleibt, wo sie war.", 1.2),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), f"Marke doppelt: {[m for m in _alle if _alle.count(m) > 1]}"
assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)

if __name__ == "__main__":
    txt = [_re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE]
    print(len(SEGMENTE), "Segmente,", len(_alle), "Marken,", sum(len(t) for t in txt), "Zeichen")
