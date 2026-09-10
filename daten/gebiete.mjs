/* ==========================================================================
   Die drei Rechtsgebiete tragen die Marke – so wie bei einem Steuerkanal die
   Klausurtage. Jeder Beitrag gehört zu genau einem Gebiet und trägt dessen
   Farbe: Zivilrecht blau, Strafrecht orange, Öffentliches Recht grün.

   Die Zuordnung entspricht dem, was der Kanal ohnehin schon als Eckenlabel
   führt – Wiedererkennung im Raster, ohne dass etwas gelesen werden muss.
   ========================================================================== */

export const GEBIETE = {
  1: { label: "Zivilrecht", kurz: "Zivilrecht" },
  2: { label: "Strafrecht", kurz: "Strafrecht" },
  3: { label: "Öffentliches Recht", kurz: "Öffentliches Recht" },
};

/* Fächer innerhalb der Gebiete. „kurz“ steht als Etikett auf der Kachel. */
export const FAECHER = {
  bgbat:   { label: "BGB Allgemeiner Teil",   kurz: "BGB AT",    gebiet: 1 },
  schuld:  { label: "Schuldrecht AT",         kurz: "SchuldR AT",gebiet: 1 },
  schuldbt:{ label: "Schuldrecht BT",         kurz: "SchuldR BT",gebiet: 1 },
  sachen:  { label: "Sachenrecht",            kurz: "SachenR",   gebiet: 1 },
  delikt:  { label: "Deliktsrecht",           kurz: "DeliktsR",  gebiet: 1 },
  bereich: { label: "Bereicherungsrecht",     kurz: "BereichR",  gebiet: 1 },
  gesetzs: { label: "Gesetzliche Schuldverhältnisse", kurz: "GoA/EBV", gebiet: 1 },
  arbeit:  { label: "Arbeitsrecht",           kurz: "ArbR",      gebiet: 1 },
  famerb:  { label: "Familien- und Erbrecht", kurz: "FamR/ErbR", gebiet: 1 },
  handelsg:{ label: "Handels- und Gesellschaftsrecht", kurz: "HGB/GesR", gebiet: 1 },
  zpo:     { label: "Zivilprozessrecht",      kurz: "ZPO",       gebiet: 1 },
  strafat: { label: "Strafrecht AT",          kurz: "StrafR AT", gebiet: 2 },
  strafbt: { label: "Strafrecht BT",          kurz: "StrafR BT", gebiet: 2 },
  stpo:    { label: "Strafprozessrecht",      kurz: "StPO",      gebiet: 2 },
  staat:   { label: "Staatsrecht",            kurz: "StaatsR",   gebiet: 3 },
  grundr:  { label: "Grundrechte",            kurz: "GrundR",    gebiet: 3 },
  verwalt: { label: "Verwaltungsrecht AT",    kurz: "VerwR AT",  gebiet: 3 },
  verwbt:  { label: "Besonderes Verwaltungsrecht", kurz: "Bes. VerwR", gebiet: 3 },
  vwgo:    { label: "Verwaltungsprozessrecht",kurz: "VwGO",      gebiet: 3 },
  europa:  { label: "Europarecht",            kurz: "EuR",       gebiet: 3 },
};
