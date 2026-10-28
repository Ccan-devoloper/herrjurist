"""Abschleppfall (Polizei- und Ordnungsrecht). [marke] = Bildelement ab diesem Wort."""

P, PS = 0.4, 0.9

SEGMENTE = [
    # --- Fall ---------------------------------------------------------------------------------------
    ("[fall]Hanna parkt ihr Auto vor einer Feuerwehrzufahrt. [schild]Dort steht ein absolutes Halteverbotsschild. "
     "[weg]Sie will nur kurz zum Bäcker.", P),
    ("[oa]Eine Mitarbeiterin des Ordnungsamts sieht den Wagen. [niemand]Hanna ist nirgends zu finden. "
     "[abschl]Die Behörde lässt das Auto abschleppen.", P),
    ("[zurueck]Als Hanna zurückkommt, ist ihr Auto weg. [bescheid]Wenige Tage später kommt ein Kostenbescheid über "
     "zweihundertfünfzig Euro. [sauer]Hanna ist empört: Niemand hat ihr etwas verfügt oder angedroht.", P),
    ("[frage]Muss Hanna zahlen?", PS),
    # --- Einstieg: Konnexität ---------------------------------------------------------------------------
    ("[schema]In der Klausur prüfst du die Rechtmäßigkeit des Kostenbescheids. "
     "[egl]Rechtsgrundlage ist die Kostenvorschrift für die Ersatzvornahme im Vollstreckungsrecht deines Landes.", P),
    ("[form]Formelle Fehler sind hier nicht ersichtlich. [mat]Materiell gilt der entscheidende Grundsatz: "
     "[konnex]Kosten kann die Behörde nur verlangen, wenn die Abschleppmaßnahme selbst rechtmäßig war.", PS),
    # --- Grundverwaltungsakt -------------------------------------------------------------------------------
    ("[gva]Das Abschleppen ist hier eine Ersatzvornahme. Die Behörde vollstreckt also einen Verwaltungsakt. [welcher]Aber welchen?", P),
    ("[vz]Die Antwort steht am Straßenrand: das Verkehrszeichen. [allg]Es ist eine Allgemeinverfügung nach Paragraf "
     "fünfunddreißig Satz zwei Verwaltungsverfahrensgesetz. [gebot]Aus dem Halteverbot folgt zugleich das Gebot, "
     "ein verbotswidrig abgestelltes Fahrzeug sofort wegzufahren.", P),
    ("[bekannt]Bekannt gegeben wird das Zeichen durch das Aufstellen. [sicht]Nach dem Sichtbarkeitsgrundsatz genügt es, "
     "dass ein durchschnittlicher Kraftfahrer es mit einem raschen und beiläufigen Blick erkennen kann. "
     "[hanna]Das war hier der Fall. Dass Hanna es übersehen hat, ändert nichts.", PS),
    # --- Vollstreckungsvoraussetzungen ------------------------------------------------------------------------
    ("[vv]Jetzt die Vollstreckungsvoraussetzungen. [sofort]Das Verkehrszeichen ist sofort vollziehbar, analog Paragraf "
     "achtzig Absatz zwei Satz eins Nummer zwei Verwaltungsgerichtsordnung. "
     "[grund]Es wirkt wie die unaufschiebbare Anordnung eines Polizeibeamten.", P),
    ("[vertretbar]Wegfahren ist eine vertretbare Handlung. Das kann auch ein anderer tun. "
     "[ev]Richtiges Zwangsmittel ist deshalb die Ersatzvornahme durch einen Abschleppunternehmer.", P),
    ("[andro]Und die fehlende Androhung? [eil]In Eilfällen erlaubt das Landesrecht, auf Androhung und Festsetzung zu verzichten. "
     "[tipp]Klausurtipp: Je nach Land prüfst du hier sofortigen Vollzug oder unmittelbare Ausführung. "
     "Die Wertungen bleiben gleich.", PS),
    # --- Verhältnismäßigkeit -------------------------------------------------------------------------------------
    ("[vhm]Schließlich muss das Abschleppen verhältnismäßig sein. [geeignet]Es ist geeignet, die Zufahrt freizumachen. "
     "[erf]Es ist erforderlich, weil Hanna nicht erreichbar war. [such]Die Behörde muss nicht lange nach ihr suchen, "
     "wenn der Erfolg ungewiss ist.", P),
    ("[angem]Und es ist angemessen. [leben]Eine versperrte Feuerwehrzufahrt kann Leib und Leben gefährden. "
     "[vs]Dagegen wiegt der Nachteil für Hanna gering.", PS),
    # --- Kosten / Ergebnis -------------------------------------------------------------------------------------------
    ("[erg]Das Abschleppen war also rechtmäßig. [kosten]Die Kosten der Ersatzvornahme trägt die Pflichtige. "
     "[zahlen]Hanna muss die zweihundertfünfzig Euro zahlen.", PS),
    # --- Schema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Erstens: Rechtsgrundlage des Kostenbescheids. [s2]Zweitens: formelle Rechtmäßigkeit.", P),
    ("[s3]Drittens: materielle Rechtmäßigkeit. Das heißt: rechtmäßige Ersatzvornahme. "
     "[s4]Grundverwaltungsakt ist das Verkehrszeichen, sofort vollziehbar. "
     "[s5]Die Ersatzvornahme ist das richtige Zwangsmittel, Androhung im Eilfall entbehrlich, verhältnismäßig.", P),
    ("[s6]Viertens: Kostenpflicht der Halterin.", PS),
    # --- Merksatz ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim Abschleppfall prüfst du erst das Abschleppen, dann die Kosten. "
     "[m2]Und das Verkehrszeichen ist der Verwaltungsakt, den die Behörde vollstreckt.", 1.4),
]
