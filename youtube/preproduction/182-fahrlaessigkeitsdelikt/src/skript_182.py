"""Folge 182 · Fahrlässigkeitsdelikt Schema: §§ 222, 229 StGB richtig prüfen (Mi · Examenswissen · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Vermieter lässt eine morsche Balkonbrüstung wochenlang unrepariert, bis ein Gast
hinabstürzt“): Herr Berger (Eigentümer und Vermieter) wird von seiner Mieterin Frau Specht mehrfach auf die lockere
Holzbrüstung ihres Balkons hingewiesen (zuletzt per E-Mail), sagt Reparatur zu, tut sechs Wochen nichts; er hält einen
Unfall für möglich, vertraut aber darauf, dass die Brüstung hält. Ein Gast von Frau Specht lehnt sich an, die Brüstung
bricht, der Gast stürzt in den Hof und wird schwer verletzt (Grundfall § 229; Variante Tod § 222). Ein Sachverständiger
stellt fest: Eine rechtzeitige Reparatur hätte den Bruch verhindert.
Aufbau: Fall → Sachverhalt → § 15 (Wortlautkarte) → § 229, § 222 (Wortlautkarten) → Schema (I. Tatbestand: Erfolg,
Unterlassen und Garantenstellung aus Verkehrssicherungspflicht – § 13 nur kurz, Verweis Folge 071 –, Kausalität,
objektive Sorgfaltspflichtverletzung, objektive Vorhersehbarkeit, Pflichtwidrigkeitszusammenhang und Schutzzweck;
II. Rechtswidrigkeit; III. Schuld: subjektive Sorgfaltspflichtverletzung und Vorhersehbarkeit) → Ergebnis mit Variante
§ 222 und § 230 → Abgrenzung bewusste Fahrlässigkeit / Eventualvorsatz → Klausurtipp → Prüfschema → Merksatz.
Belege (BGH 4 StR 19/20 Rn. 11, 14, 18, 21 f.; 1 StR 272/09 Rn. 60–66; 4 StR 252/08 Rn. 17 f.; 5 StR 394/08 Rn. 23;
1 StR 474/19 Rn. 14): ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Herr Berger, Frau Specht (nie im Genitiv).
Der Gast bleibt ohne Namen (Funktionsrolle) und spricht nicht.
Stimmen (nur aus dem Pool): Herr Berger william (Mann, älter); Frau Specht laura_ruhig (Frau, mittel). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Berger": "william", "Specht": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das Mietshaus ----------------------------------------------------------------------------------------------
    ("[fall]Ein Mietshaus in der Stadt. [berger]Es gehört Herrn Berger. [specht]Frau Specht wohnt im zweiten Stock und hat "
     "einen Balkon. [morsch]Dessen Holzbrüstung ist morsch und wackelt.", P),
    ("[sp1]Herr Berger, die Brüstung am Balkon ist locker. Bitte lassen Sie sie reparieren!", P, "Specht"),
    ("[b1]Ja, ja, ich kümmere mich darum.", P, "Berger"),
    ("[nichts]Doch es passiert nichts. [zweimal]Frau Specht erinnert ihn noch zweimal, zuletzt per E-Mail. [haelt]Herr Berger "
     "hält einen Unfall zwar für möglich, vertraut aber darauf, dass die Brüstung schon hält.", P),
    # --- A2 Fall: der Besuch -----------------------------------------------------------------------------------------------------
    ("[wochen]Sechs Wochen nach dem ersten Hinweis hat Frau Specht Besuch. [gast]Ihr Gast lehnt sich auf dem Balkon an die "
     "Brüstung.", P),
    # --- A3 Fall: die Brüstung bricht (nur Gebäude-Icon, Warnsymbol und Text) ------------------------------------------------
    ("[bricht]Die Brüstung bricht. [verletzt]Der Gast stürzt in den Hof und wird schwer verletzt. [gutacht]Ein Sachverständiger "
     "stellt später fest: Eine rechtzeitige Reparatur hätte den Bruch verhindert.", 0.4),
    ("[frage]Herr Berger wollte niemanden verletzen. Hat er sich trotzdem strafbar gemacht? [frage2]Und wie prüfst du ein "
     "Fahrlässigkeitsdelikt?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 15 --------------------------------------------------------------------------------------------------------------------
    ("[p15]Ausgangspunkt ist Paragraf fünfzehn: Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz fahrlässiges "
     "Handeln ausdrücklich mit Strafe bedroht. [ausdr]Fahrlässigkeit ist also nur dort strafbar, wo das Gesetz es "
     "ausdrücklich sagt.", PS),
    # --- D § 229, § 222 -----------------------------------------------------------------------------------------------------------
    ("[p229]So wie Paragraf zweihundertneunundzwanzig: Wer durch Fahrlässigkeit die Körperverletzung einer anderen Person "
     "verursacht, wird mit Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe bestraft. [p222]Und Paragraf "
     "zweihundertzweiundzwanzig: Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis "
     "zu fünf Jahren oder mit Geldstrafe bestraft. [gleich]Beide Delikte prüfst du nach demselben Schema.", PS),
    # --- E Aufbau in drei Stufen ---------------------------------------------------------------------------------------------------
    ("[stufen]Es hat drei Stufen. [tb]Römisch eins, der Tatbestand. [rw0]Römisch zwei, die Rechtswidrigkeit. [sd0]Römisch "
     "drei, die Schuld. [zwei]Die Fahrlässigkeit prüfst du dabei zweimal: im Tatbestand objektiv, in der Schuld subjektiv.", PS),
    # --- F 1. Erfolg, 2. Unterlassen und Garantenstellung ------------------------------------------------------------------------
    ("[erfolg]Erstens der Erfolg: Der Gast ist am Körper verletzt. [handl]Zweitens die Handlung. [unterl]Herrn Berger wirft man "
     "kein Tun vor, sondern ein Unterlassen: Er hat die Brüstung nicht reparieren lassen. [p13]Dann brauchst du Paragraf "
     "dreizehn, Herr Berger muss Garant sein. [vsp]Als Eigentümer beherrscht er das Haus als Gefahrenquelle und ist "
     "verkehrssicherungspflichtig. Das macht ihn zum Überwachergaranten. [moegl]Die Reparatur war ihm auch möglich. "
     "[verw]Die Einzelheiten zeigt das Video zum Unterlassungsdelikt.", PS),
    # --- G 3. Kausalität -----------------------------------------------------------------------------------------------------------
    ("[kaus]Drittens die Kausalität. Beim Unterlassen fragst du: Hätte die gebotene Handlung den Erfolg verhindert? "
     "[kaus2]Laut Sachverständigem ja. Mit Reparatur wäre die Brüstung nicht gebrochen.", PS),
    # --- H 4. objektive Sorgfaltspflichtverletzung -------------------------------------------------------------------------------
    ("[sorg]Viertens, das Herzstück: die objektive Sorgfaltspflichtverletzung. [mass]Maßstab ist ein besonnener und "
     "gewissenhafter Mensch in der konkreten Lage und sozialen Rolle des Täters. [verm]Ein gewissenhafter Vermieter hätte die "
     "Brüstung nach dem ersten Hinweis prüfen und reparieren oder den Balkon sperren lassen. [sorg2]Herr Berger tat wochenlang "
     "nichts. Damit hat er die Sorgfalt verletzt.", PS),
    # --- I 5. objektive Vorhersehbarkeit -----------------------------------------------------------------------------------------
    ("[vorh]Fünftens die objektive Vorhersehbarkeit. Der Erfolg muss in seinem Gewicht im Wesentlichen vorhersehbar sein, "
     "nicht in allen Einzelheiten. [vorh2]Hier hatte die Mieterin mehrfach gewarnt. Dass sich jemand an eine morsche Brüstung "
     "lehnt und abstürzt, liegt auf der Hand.", PS),
    # --- J 6. Pflichtwidrigkeitszusammenhang und Schutzzweck ---------------------------------------------------------------------
    ("[pwz]Sechstens der Pflichtwidrigkeitszusammenhang, das Stichwort lautet rechtmäßiges Alternativverhalten. [formel]Nach "
     "dem Bundesgerichtshof wird ein Erfolg nur zugerechnet, wenn er bei pflichtgemäßem Verhalten nicht eingetreten wäre. "
     "[zweifel]Bleibt das ernsthaft zweifelhaft, gilt: im Zweifel für den Angeklagten. Eine bloß gedankliche Möglichkeit "
     "genügt dafür aber nicht. [pwz2]Hier steht fest: Die reparierte Brüstung hätte gehalten. [schutz]Und der Erfolg liegt im "
     "Schutzzweck der Pflicht: Eine sichere Brüstung soll gerade Menschen auf dem Balkon vor einem Sturz bewahren.", PS),
    # --- K II. Rechtswidrigkeit, III. Schuld ---------------------------------------------------------------------------------------
    ("[rw]Römisch zwei: Rechtfertigungsgründe sind nicht ersichtlich. [schuld]Römisch drei, die Schuld. Hier kommt die "
     "subjektive Seite. [subj]Konnte Herr Berger nach seinen persönlichen Kenntnissen und Fähigkeiten die Pflicht erkennen und "
     "erfüllen, [subj2]und war der Erfolg für ihn vorhersehbar? [subj3]Ja: Er kannte die Warnungen und hätte einen Handwerker "
     "beauftragen können.", PS),
    # --- L Ergebnis, Variante § 222, Abgrenzung zum bedingten Vorsatz -------------------------------------------------------------
    ("[erg]Ergebnis: Herr Berger ist strafbar wegen fahrlässiger Körperverletzung durch Unterlassen, Paragrafen "
     "zweihundertneunundzwanzig und dreizehn. [antrag]Verfolgt wird sie auf Strafantrag oder bei besonderem öffentlichem "
     "Interesse. [tod]Stirbt der Gast, ist es eine fahrlässige Tötung durch Unterlassen, Paragrafen zweihundertzweiundzwanzig "
     "und dreizehn, mit demselben Schema.", PS),
    ("[vors]Und warum kein Vorsatz? Herr Berger hielt einen Unfall für möglich, vertraute aber ernsthaft darauf, dass nichts "
     "passiert. Das ist bewusste Fahrlässigkeit. [event]Hätte er sich mit einer Verletzung abgefunden, läge bedingter Vorsatz "
     "vor.", PS),
    # --- M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst das Vorsatzdelikt und lehne den Vorsatz ab. Erst dann kommt das Fahrlässigkeitsdelikt. "
     "[tipp2]Und achte auf die Unterlassungsform: Dann gehören Garantenstellung und hypothetische Kausalität in den "
     "Tatbestand.", PS),
    # --- N Prüfschema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins, Tatbestand: [s1a]Erfolg, [s1b]Handlung oder Unterlassen mit Garantenstellung, "
     "[s1c]Kausalität, [s1d]objektive Sorgfaltspflichtverletzung, [s1e]objektive Vorhersehbarkeit, [s1f]"
     "Pflichtwidrigkeitszusammenhang und Schutzzweck. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, Schuld mit "
     "subjektiver Sorgfaltspflichtverletzung und subjektiver Vorhersehbarkeit.", PS),
    # --- O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Fahrlässig handelt, wer die gebotene Sorgfalt verletzt und den Erfolg vorhersehen konnte. [m2]Zugerechnet "
     "wird ihm der Erfolg nur, wenn er bei pflichtgemäßem Verhalten ausgeblieben wäre.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
