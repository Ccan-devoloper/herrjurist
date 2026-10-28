"""Folge 234 · Fortsetzungsfeststellungsklage: Tenor und Feststellungsinteresse (Fr · 2. Examen · VwGO-Praxis · Schema).
Übungsfall nach dem Hook des Themenplans („Die Polizei hat eine Versammlung aufgelöst, die längst vorbei ist, doch der
Veranstalter plant schon die nächste“), Beispielland Nordrhein-Westfalen (wie Folge 233):
Samstag, 7. März 2026, Mahnwache vor der Stadtbücherei, die schließen soll. Herr Strauch leitet sie; die rund zwanzig
Teilnehmenden stehen vor dem Eingang. Polizeihauptkommissar Nagel löst die Versammlung auf. Herr Strauch plant schon die
nächste Mahnwache vor der Bücherei, die Polizei würde wieder so handeln. Er klagt; in der mündlichen Verhandlung hält die
Richterin Frau Bollmann die Auflösung für unverhältnismäßig (eine Beschränkung zum Ort hätte genügt).
Aufbau (Perspektive Urteil/Anwaltsschriftsatz): 1. Antrag (erledigt → Feststellung; analog; Prüfungsschema nur verwiesen auf
Folge 233); Umstellung bei Erledigung im Prozess keine Klageänderung (§ 173 S. 1 VwGO i. V. m. § 264 Nr. 2 ZPO, BVerwG
4 C 33.13 Rn. 11; teils Nr. 3, VG Düsseldorf 29 K 78/22 Rn. 18) mit Wortlautkarte § 264 ZPO; 2. Feststellungsinteresse im
Urteil (8 C 14.12 Rn. 20, 21, 25; BVerfGE 110, 77 Rn. 37, 41–43; 6 C 2.22 Rn. 21 f.); 3. Tenor (§ 113 I 4 „rechtswidrig
gewesen ist“; vgl. VG Gelsenkirchen 14 K 4207/19, Tenor und Rn. 108 f.; Verpflichtungssituation 4 C 33.13 Rn. 19, 21),
Kosten § 154 I VwGO, vorläufige Vollstreckbarkeit § 167 VwGO i. V. m. §§ 708 Nr. 11, 711 ZPO; 4. typische Fehler,
Hilfsantrag ein Satz → Klausurtipp, Schema, Merksatz mit Lexi. Tenorstil wie Folgen 102/108 (nur verwiesen).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Strauch william (Mann, älter), Polizeihauptkommissar Nagel marc
(Mann, mittel), Richterin Bollmann sabrina (Frau, mittel); laura_ruhig nicht gebraucht. Erzählerin und Lexi: Carla ohne Rolle.
Namen nie im Genitiv mit -s. Belege je Cue: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Strauch": "william", "Nagel": "marc", "Bollmann": "sabrina"}

SEGMENTE = [
    # --- A Fall: Mahnwache vor der Stadtbücherei ------------------------------------------------------------------------
    ("[fall]Samstagvormittag vor der Stadtbücherei. [strauch]Herr Strauch leitet eine Mahnwache, denn die Bücherei soll "
     "schließen. [eingang]Die rund zwanzig Teilnehmer stehen direkt vor dem Eingang. [nagel]Polizeihauptkommissar Nagel "
     "kommt dazu.", 0.2),
    ("[na1]Sie versperren den Eingang. Die Versammlung ist aufgelöst.", P, "Nagel"),
    ("[st1]Wir können doch ein paar Meter zur Seite gehen!", P, "Strauch"),
    ("[vorbei]Alle gehen nach Hause, die Mahnwache ist vorbei. [naechst]Doch Herr Strauch plant schon die nächste, wieder vor "
     "der Bücherei. Und die Polizei bleibt dabei: Sie würde wieder so handeln. [klage]Herr Strauch klagt beim "
     "Verwaltungsgericht. [gericht]In der mündlichen Verhandlung sagt die Richterin:", 0.2),
    ("[ri1]Ein paar Meter zur Seite hätten genügt. Die Auflösung war unverhältnismäßig.", P, "Bollmann"),
    ("[frage]Die Versammlung ist längst vorbei. Was beantragt Herr Strauch, und wie begründet das Urteil sein "
     "Feststellungsinteresse? [frage2]Und wie lautet der Tenor? [frage3]Die Perspektive des zweiten Examens, am Beispiel "
     "Nordrhein-Westfalen.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Der Antrag --------------------------------------------------------------------------------------------------
    ("[antrag]Erstens, der Antrag. Die Auflösung hat sich mit dem Ende der Mahnwache erledigt. Aufheben kann das Gericht sie "
     "nicht mehr. [antrag2]Herr Strauch beantragt deshalb, festzustellen, dass die Auflösung seiner Versammlung vom siebten "
     "März zweitausendsechsundzwanzig rechtswidrig gewesen ist. [analog]Die Auflösung war schon vor der Klage erledigt, "
     "also gilt Paragraf hundertdreizehn Absatz eins Satz vier entsprechend. Das Prüfungsschema zeigt unser Video zur "
     "Fortsetzungsfeststellungsklage.", P),
    ("[umst]Erledigt sich ein Bescheid dagegen erst während des Prozesses, etwa ein Verbot, gegen das Herr Strauch schon "
     "klagt, stellt er von der Anfechtung auf die Feststellung um. [wl264]Das ist keine Klageänderung. Nach dem "
     "Bundesverwaltungsgericht beschränkt er nur seinen Antrag, Paragraf zweihundertvierundsechzig Nummer zwei ZPO, über "
     "Paragraf hundertdreiundsiebzig Verwaltungsgerichtsordnung. [nr3]Manche Gerichte nennen Nummer drei. [tb]Im "
     "Tatbestand heißt es dann: Nachdem der Kläger zunächst die Aufhebung beantragt hatte, hat er seinen Antrag auf die "
     "Feststellung umgestellt.", P),
    # --- D 2. Feststellungsinteresse im Urteil ------------------------------------------------------------------------------
    ("[ffi]Zweitens, das Feststellungsinteresse. Im Urteil prüfst du es in der Zulässigkeit, für den Zeitpunkt der "
     "Entscheidung. [ffi2]Das Urteil muss die Lage des Klägers rechtlich, wirtschaftlich oder ideell verbessern können. "
     "Eine tragende Fallgruppe genügt.", P),
    ("[wh]Zuerst die Wiederholungsgefahr: Es droht konkret ein vergleichbarer Verwaltungsakt, unter im Wesentlichen "
     "unveränderten Umständen. [wh2]Im Versammlungsrecht reicht der erkennbare Wille, ähnliche Versammlungen abzuhalten. "
     "Dasselbe Motto und derselbe Ort sind nicht nötig. [wh3]Dazu kommen Anhaltspunkte, dass die Behörde bei ihren Gründen "
     "bleibt. [wh4]Herr Strauch plant die nächste Mahnwache, und die Polizei würde wieder so handeln. Die "
     "Wiederholungsgefahr besteht.", P),
    ("[reha]Dann die Rehabilitation: Die Maßnahme müsste ihn nach außen sichtbar abstempeln, und das bis heute. "
     "[reha2]Einen ehrenrührigen Vorwurf hat die Polizei nicht erhoben.", P),
    ("[tief]Schließlich der tiefgreifende Grundrechtseingriff. Nach dem Bundesverwaltungsgericht braucht es beides: eine "
     "Maßnahme, die sich typischerweise schnell erledigt, und einen gewichtigen Eingriff. [tief2]Die Auflösung ist nach dem "
     "Bundesverfassungsgericht die schwerste mögliche Beeinträchtigung der Versammlungsfreiheit. [tief3]Im Urteil schreibst "
     "du also: Der Kläger hat ein berechtigtes Interesse an der Feststellung. Es folgt aus der Wiederholungsgefahr und aus "
     "dem schweren Eingriff in seine Versammlungsfreiheit.", P),
    # --- E 3. Der Tenor --------------------------------------------------------------------------------------------------
    ("[tenor]Drittens, der Tenor. Er folgt dem Wortlaut des Gesetzes: Es wird festgestellt, dass der Bescheid rechtswidrig "
     "gewesen ist. [tenor2]Bei Herrn Strauch: Es wird festgestellt, dass die Auflösung der Versammlung des Klägers vom "
     "siebten März zweitausendsechsundzwanzig rechtswidrig gewesen ist. [verpfl]In der Verpflichtungssituation stellt das "
     "Gericht etwa fest, dass der Beklagte verpflichtet war, die beantragte Erlaubnis zu erteilen.", P),
    ("[kosten]Herr Strauch gewinnt ganz. Nach Paragraf hundertvierundfünfzig Absatz eins trägt der unterliegende Teil die "
     "Kosten: Der Beklagte trägt die Kosten des Verfahrens. [vollstr]Vollstreckbar ist nur die Kostenentscheidung, hier im "
     "Wert von höchstens tausendfünfhundert Euro. Also Paragraf hundertsiebenundsechzig Verwaltungsgerichtsordnung mit den "
     "Paragrafen siebenhundertacht Nummer elf und siebenhundertelf ZPO. [vollstr2]Der Tenor: Das Urteil ist wegen der Kosten "
     "vorläufig vollstreckbar. [vollstr3]Der Beklagte darf die Vollstreckung durch Sicherheitsleistung in Höhe von "
     "hundertzehn Prozent des vollstreckbaren Betrages abwenden, wenn nicht der Kläger vor der Vollstreckung Sicherheit in "
     "Höhe von hundertzehn Prozent des jeweils zu vollstreckenden Betrages leistet.", P),
    # --- F 4. Typische Fehler, Hilfsantrag -----------------------------------------------------------------------------------
    ("[fehler]Viertens, typische Fehler. [f1]Fehler eins: ist rechtswidrig. Richtig ist: rechtswidrig gewesen ist, denn der "
     "Verwaltungsakt hat sich erledigt. [f2]Fehler zwei: ein Aufhebungstenor. Einen erledigten Verwaltungsakt hebt das "
     "Gericht nicht mehr auf. [hilfs]Und ist unsicher, ob er sich schon erledigt hat, stellst du den Feststellungsantrag "
     "hilfsweise.", PS),
    # --- G Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Das Feststellungsinteresse muss noch am Tag der Entscheidung bestehen. [tipp2]Hat Herr Strauch die "
     "nächste Mahnwache inzwischen abgesagt, entfällt die Wiederholungsgefahr. [tipp3]Dann trägt allein der schwere Eingriff "
     "in die Versammlungsfreiheit.", PS),
    # --- H Schema (Lexi) ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für das Urteil. [s1]Erstens, der Antrag: Feststellung statt Aufhebung. [s2]Zweitens, in der "
     "Zulässigkeit das Feststellungsinteresse mit einer tragenden Fallgruppe. [s3]Drittens, der Tenor: rechtswidrig gewesen. "
     "[s4]Viertens, die Kosten nach Paragraf hundertvierundfünfzig Absatz eins. [s5]Fünftens, die vorläufige "
     "Vollstreckbarkeit wegen der Kosten.", PS),
    # --- I Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein erledigter Verwaltungsakt wird nicht aufgehoben. [m2]Das Gericht stellt fest, dass er rechtswidrig "
     "gewesen ist.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), "Marke doppelt"
