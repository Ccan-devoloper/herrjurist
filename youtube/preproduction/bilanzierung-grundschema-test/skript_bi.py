"""Grundschema der Bilanzierung nach Handels- und Steuerrecht. [marke] = Bildelement ab diesem Wort."""

P, PS = 0.4, 0.9

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------------------------------
    ("[fall]Lena betreibt als eingetragene Kauffrau einen Fertigungsbetrieb mit mehreren Millionen Euro Umsatz. "
     "[kauf]Am zweiten Januar kauft sie eine neue Maschine für fünfzigtausend Euro. "
     "[neben]Für Transport und Montage zahlt sie weitere zweitausend Euro.", P),
    ("[nd]Die Maschine soll zehn Jahre lang genutzt werden. [modell]Im Herbst kommt aber ein deutlich besseres Modell auf den Markt. "
     "[wert]Am Jahresende ist Lenas Maschine dauerhaft nur noch dreißigtausend Euro wert.", P),
    ("[frage]Mit welchem Wert steht die Maschine in Lenas Handelsbilanz und in ihrer Steuerbilanz?", 0.6),
    # --- Sachverhalt zum Nachlesen ------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- Grundschema ------------------------------------------------------------------------------------------------
    ("[schema]Jede Bilanzierungsfrage prüfst du in derselben Reihenfolge. [g1]Erstens: Wer muss bilanzieren? "
     "[g2]Zweitens: der Ansatz. Kommt der Posten überhaupt in die Bilanz? [g3]Drittens: die Bewertung. Mit welchem Wert?", P),
    ("[mg]Dabei gilt die Maßgeblichkeit, Paragraf fünf Absatz eins Einkommensteuergesetz. Die Steuerbilanz folgt der Handelsbilanz, "
     "[vorb]außer ein Steuergesetz regelt es anders, oder ein steuerliches Wahlrecht wird anders ausgeübt.", PS),
    # --- I. Bilanzierungspflicht -------------------------------------------------------------------------------------
    ("[wer]Lena ist Kauffrau. Die Ausnahme für kleine Einzelkaufleute greift bei ihrem Umsatz nicht. "
     "[wer1]Also ist sie nach Paragraf zweihundertachtunddreißig Handelsgesetzbuch buchführungspflichtig. "
     "[wer2]Über Paragraf hundertvierzig Abgabenordnung gilt das auch steuerlich, und sie ermittelt ihren Gewinn nach Paragraf fünf Einkommensteuergesetz.", PS),
    # --- II. Ansatz ----------------------------------------------------------------------------------------------------
    ("[ansatz]Jetzt der Ansatz. [vg]Die Maschine ist ein Vermögensgegenstand, steuerlich ein Wirtschaftsgut: "
     "selbständig bewertbar und über den Stichtag hinaus nutzbar.", P),
    ("[zur]Sie gehört Lena, und sie dient ihrem Betrieb. Damit ist sie notwendiges Betriebsvermögen. "
     "[verbot]Ein Ansatzverbot greift nicht. [pflicht]Also muss die Maschine aktiviert werden, Paragraf zweihundertsechsundvierzig Handelsgesetzbuch.", P),
    ("[av]Weil sie dem Betrieb dauernd dienen soll, gehört sie zum Anlagevermögen, Paragraf zweihundertsiebenundvierzig Absatz zwei.", PS),
    # --- III. Bewertung -------------------------------------------------------------------------------------------------
    ("[bew]Nun die Bewertung. [zugang]Beim Zugang zählen die Anschaffungskosten, Paragraf zweihundertfünfundfünfzig Absatz eins "
     "Handelsgesetzbuch, steuerlich Paragraf sechs Absatz eins Nummer eins. "
     "[ak]Dazu gehören auch die Nebenkosten: fünfzigtausend plus zweitausend, also zweiundfünfzigtausend Euro.", P),
    ("[afa]Dann die planmäßige Abschreibung über zehn Jahre: fünftausendzweihundert Euro im Jahr. "
     "[fak]Am Jahresende bleiben sechsundvierzigtausendachthundert Euro.", PS),
    ("[apl]Bleibt der Wertverlust auf dreißigtausend Euro. [hgb]Im Handelsrecht muss Lena bei voraussichtlich dauernder Wertminderung "
     "außerplanmäßig abschreiben, Paragraf zweihundertdreiundfünfzig Absatz drei Satz fünf. [hb]Handelsbilanz: dreißigtausend Euro.", P),
    ("[estg]Im Steuerrecht heißt es dagegen: Der niedrigere Teilwert kann angesetzt werden, Paragraf sechs Absatz eins Nummer eins Satz zwei. "
     "[wahl]Das ist ein eigenes steuerliches Wahlrecht, das Lena unabhängig von der Handelsbilanz ausüben kann. "
     "[sb]Steuerbilanz: dreißigtausend oder sechsundvierzigtausendachthundert Euro.", P),
    ("[verz]Weicht sie von der Handelsbilanz ab, muss sie die Maschine in ein besonderes Verzeichnis aufnehmen, Paragraf fünf Absatz eins Satz zwei.", PS),
    # --- Klausurtipp ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Beginne immer mit der Handelsbilanz. [tipp2]Suche dann gezielt nach steuerlichen Sonderregeln "
     "und Wahlrechten, die davon abweichen.", PS),
    # --- Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Grundschema. [k1]Erstens: Bilanzierungspflicht. [k2]Zweitens: Ansatz. Wirtschaftsgut, Zurechnung, kein Ansatzverbot. "
     "[k3]Drittens: Bewertung. Zugangswert, planmäßige Abschreibung, dann außerplanmäßige Abschreibung oder Teilwert.", P),
    ("[k4]Und bei jedem Schritt: Maßgeblichkeit, aber mit steuerlichem Vorbehalt.", PS),
    # --- Merksatz --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst der Ansatz, dann die Bewertung. [m2]Die Handelsbilanz ist maßgeblich, soweit das Steuerrecht nichts anderes bestimmt.", 1.4),
]
