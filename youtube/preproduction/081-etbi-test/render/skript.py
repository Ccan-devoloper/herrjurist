"""Folge 081 (Testfassung, ohne Illustrationen): Ein Angriff, den es nie gab – Putativnotwehr.

Jeder Eintrag ist eine Sprecheinheit. Bild-Cues (Prüfpfad, Karte, Stichwort rechts) starten
exakt mit dem Audiobeginn dieser Einheit. `neu` = neue Karte (alte Karte weg, neue blendet ein);
sonst werden `zeilen` an die laufende Karte angehängt. `pause` = Stille nach der Einheit in s.
"""

S = []


def seg(text, pfad=None, titel=None, zeilen=(), neu=False, rechts=None, pause=0.35):
    S.append(dict(text=text, pfad=pfad, titel=titel, zeilen=list(zeilen), neu=neu, rechts=rechts, pause=pause))


# --- Fall -----------------------------------------------------------------------------
seg("Nachts am Bahnhof. B rennt auf A zu und greift hastig in seine Jackentasche.",
    pfad="Fall › Nachts am Bahnhof", titel="Der Fall", neu=True,
    zeilen=["B rennt auf A zu", "Griff in die Jackentasche"],
    rechts=("Vorstellung", "Messerangriff?"))
seg("A denkt: Messer! Und schlägt B mit der Faust nieder.",
    zeilen=["A schlägt B nieder"])
seg("Dabei wollte B ihm nur das Handy zurückgeben, das A auf der Bank vergessen hatte.",
    zeilen=["Wirklich: B bringt das Handy"])
seg("Hat A sich wegen Körperverletzung strafbar gemacht?",
    pfad="Fall › Rechtsfrage", titel="Rechtsfrage", neu=True,
    zeilen=["Strafbarkeit des A", "gem. § 223 I StGB?"],
    rechts=("Frage", "§ 223 StGB"), pause=0.8)

# --- I. Tatbestand --------------------------------------------------------------------
seg("Erstens: der Tatbestand. Der Faustschlag ist eine körperliche Misshandlung "
    "nach Paragraf zweihundertdreiundzwanzig Absatz eins Strafgesetzbuch.",
    pfad="I. Tatbestand › § 223 I StGB", titel="I. Tatbestand", neu=True,
    zeilen=["Körperliche Misshandlung (+)"], rechts=("Punkt I", "Tatbestand"))
seg("A will B treffen. Er handelt also vorsätzlich.",
    zeilen=["Vorsatz (+)"], pause=0.8)

# --- II. Rechtswidrigkeit -------------------------------------------------------------
seg("Zweitens: die Rechtswidrigkeit. Notwehr nach Paragraf zweiunddreißig verlangt "
    "einen gegenwärtigen, rechtswidrigen Angriff.",
    pfad="II. Rechtswidrigkeit › Notwehr § 32", titel="Notwehr, § 32 StGB", neu=True,
    zeilen=["Gegenwärtiger, rechtswidriger", "Angriff?"], rechts=("Punkt II", "Rechtswidrigkeit"))
seg("Den gibt es objektiv nicht. Die Tat ist rechtswidrig.",
    zeilen=["Objektiv kein Angriff (–)", "→ Tat rechtswidrig"], pause=0.8)

# --- III. Schuld ----------------------------------------------------------------------
seg("Drittens: die Schuld. A hat sich Tatsachen vorgestellt, "
    "die ihn durch Notwehr rechtfertigen würden, wenn sie wahr wären.",
    pfad="III. Schuld › Erlaubnistatbestandsirrtum", titel="Erlaubnistatbestandsirrtum", neu=True,
    zeilen=["Irrtum über Tatsachen,", "die bei Wahrheit rechtfertigen"],
    rechts=("Punkt III", "Schuld"))
seg("Das ist der Erlaubnistatbestandsirrtum. Prüfe dabei genau: Wäre der Faustschlag "
    "in der vorgestellten Lage erforderlich gewesen? Hier ja.",
    zeilen=["Vorgestellte Lage: Notwehr (+)"])
seg("Abgrenzen musst du den Erlaubnisirrtum. Wer über Bestehen oder Grenzen einer "
    "Rechtfertigung irrt, irrt über Recht. Das ist ein Verbotsirrtum nach Paragraf siebzehn.",
    pfad="III. Schuld › Abgrenzung", titel="Abgrenzung", neu=True,
    zeilen=["Irrtum über Tatsachen → ETBI", "Irrtum über Recht → § 17 StGB"],
    rechts=("Punkt III", "Tatsache oder Recht?"), pause=0.8)
seg("Das Gesetz regelt den Erlaubnistatbestandsirrtum nicht. Die strenge Schuldtheorie "
    "wendet nur Paragraf siebzehn an. A bliebe dann bei vermeidbarem Irrtum wegen vorsätzlicher Tat strafbar.",
    pfad="III. Schuld › Streitstand", titel="Streitstand", neu=True,
    zeilen=["Strenge Schuldtheorie: nur § 17"], rechts=("Punkt III", "Streitstand"))
seg("Die herrschende Meinung wendet Paragraf sechzehn Absatz eins zumindest in der "
    "Rechtsfolge analog an: Die Vorsatzschuld entfällt.",
    zeilen=["h. M.: § 16 I 1 analog", "  Rechtsfolge: Vorsatzschuld entfällt"])
seg("Tatbestand und Rechtswidrigkeit bleiben bestehen. Für Teilnehmer bleibt so eine Haupttat.",
    zeilen=["  Teilnahmefähige Haupttat bleibt"], pause=0.8)

# --- Ergebnis -------------------------------------------------------------------------
seg("Ergebnis: A ist nicht wegen vorsätzlicher Körperverletzung strafbar.",
    pfad="Ergebnis › § 223 I StGB", titel="Ergebnis", neu=True,
    zeilen=["§ 223 I StGB: Vorsatzschuld (–)"], rechts=("Ergebnis", "Vorsatz: nein"))
seg("Paragraf sechzehn Absatz eins Satz zwei lässt die Fahrlässigkeit aber unberührt. "
    "Prüfe also Paragraf zweihundertneunundzwanzig: War der Irrtum bei Sorgfalt vermeidbar?",
    pfad="Ergebnis › § 229 StGB prüfen",
    zeilen=["§ 16 I 2 analog", "→ § 229 StGB: Irrtum vermeidbar?"], pause=0.8)

# --- Klausurschema (progressiv) -------------------------------------------------------
seg("Dein Schema. Eins: Tatbestand.",
    pfad="Klausurschema › § 223 I StGB", titel="Klausurschema § 223 I", neu=True,
    zeilen=["I. Tatbestand (+)"], rechts=("Schema", "Schritt für Schritt"))
seg("Zwei: Rechtswidrigkeit, kein Rechtfertigungsgrund.",
    zeilen=["II. Rechtswidrigkeit (+)", "  kein Rechtfertigungsgrund"])
seg("Drei: Schuld. Erlaubnistatbestandsirrtum, Streit entscheiden, Vorsatzschuld entfällt.",
    zeilen=["III. Schuld", "  ETBI – Streitentscheid", "  Vorsatzschuld (–)"])
seg("Danach die fahrlässige Körperverletzung.",
    zeilen=["Danach: § 229 StGB"], pause=0.8)

# --- Merksatz -------------------------------------------------------------------------
seg("Merke: Irrt der Täter über Tatsachen, hilft Paragraf sechzehn analog. "
    "Irrt er über Recht, bleibt nur Paragraf siebzehn.",
    pfad="Merksatz", titel="Merksatz", neu=True,
    zeilen=["Irrtum über Tatsachen", "  → § 16 I 1 analog", "Irrtum über Recht", "  → § 17 StGB"],
    rechts=("Merke", "Tatsache ≠ Recht"), pause=1.2)
