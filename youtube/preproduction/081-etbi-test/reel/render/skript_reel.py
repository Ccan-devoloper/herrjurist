"""Reel 081 (9:16, ca. 45 s): Erlaubnistatbestandsirrtum. Jede Einheit = ein Untertitelblock."""

K, S = 0.18, 0.45  # Pause im Satzfluss / vor Szenenwechsel

SEGMENTE = [
    ("[hook]Notwehr gegen einen Angriff, den es nie gab?", S),
    ("[fall]Nachts am Bahnhof [b]rennt B auf A zu und [tasche]greift in die Tasche.", K),
    ("A denkt: [messer]Messer! Und [faust]schlägt zu.", K),
    ("[handy]Dabei wollte B ihm nur das Handy zurückgeben.", S),
    ("[nw]Notwehr? Nein, [kein]es gab keinen Angriff.", K),
    ("[vorst]A hat sich den Angriff nur vorgestellt.", K),
    ("[etbi]Ein Erlaubnistatbestandsirrtum.", S),
    ("[streit]Das Gesetz regelt ihn nicht.", K),
    ("[sst]Die strenge Schuldtheorie wendet nur Paragraf siebzehn an.", K),
    ("[hm]Die herrschende Meinung wendet Paragraf sechzehn analog an. [vs]Die Vorsatzschuld entfällt.", S),
    ("[erg]Also keine vorsätzliche Körperverletzung.", K),
    ("Aber: [fahr]War der Irrtum vermeidbar, kommt fahrlässige Körperverletzung in Betracht.", S),
    ("[merke]Merke: Irrtum über [hl1]Tatsachen, Paragraf sechzehn analog. [m2]Irrtum über [hl2]Recht, Paragraf siebzehn.", 1.3),
]
