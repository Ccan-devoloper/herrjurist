const React = require('react');
const { renderToStaticMarkup } = require('react-dom/server');
const Peep = require('react-peeps').default;
const fs = require('fs');
// Figur = Pose + Gesicht + Haar; eine Füllfarbe je Person für Wiedererkennung
const figuren = {
  A_ruhig:   { body: 'ShirtPantsWB', face: 'Calm',          hair: 'ShortVolumed', bg: '#FFFFFF' },
  A_angst:   { body: 'ShirtPantsWB', face: 'ConcernedFear', hair: 'ShortVolumed', bg: '#FFFFFF' },
  A_wut:     { body: 'ShirtPantsWB', face: 'Rage',          hair: 'ShortVolumed', bg: '#FFFFFF' },
  A_schreck: { body: 'ShirtPantsWB', face: 'Awe',           hair: 'ShortVolumed', bg: '#FFFFFF' },
  B_laeuft:  { body: 'WalkingWB',    face: 'SmileBig',      hair: 'ShortMessy',       bg: '#FFFFFF' },
  B_zeigt:   { body: 'PointingFingerWB', face: 'Smile',     hair: 'ShortMessy',       bg: '#FFFFFF' },
  B_verletzt:{ body: 'WalkingWB',    face: 'Tired',         hair: 'ShortMessy',       bg: '#FFFFFF' },
  T_denkt:   { body: 'CrossedArmsWB', face: 'Suspicious',   hair: 'Short', facialHair: 'Goatee', bg: '#FFFFFF' },
  T_verwirrt:{ body: 'CrossedArmsWB', face: 'Concerned',    hair: 'Short', facialHair: 'Goatee', bg: '#FFFFFF' },
};
for (const [name, f] of Object.entries(figuren)) {
  const el = React.createElement(Peep, {
    body: f.body, face: f.face, hair: f.hair, facialHair: f.facialHair || 'None', accessory: 'None',
    strokeColor: '#1e1e1e', backgroundColor: f.bg, style: { width: 1000, height: 1000 }, viewBox: { x: '-600', y: '-100', width: '3000', height: '4500' },
  });
  let svg = renderToStaticMarkup(el);
  if (!svg.includes('xmlns=')) svg = svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
  fs.writeFileSync(`svg/${name}.svg`, svg);
  console.log(name, svg.length, (svg.match(/viewBox="[^"]+"/) || [''])[0]);
}
