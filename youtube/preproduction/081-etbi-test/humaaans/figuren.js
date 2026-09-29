global.window = global;
const React = require('react');
const { renderToStaticMarkup } = require('react-dom/server');
const H = require('react-humaaans');
const fs = require('fs');
console.error = () => {};
// Besetzung: feste Farben je Person, damit A/B/Täter über alle Folien wiedererkennbar bleiben
const A = { skinColor: '#8D5B3E', hairColor: '#1F1D5B', coatColor: '#FF9A1F', shirtColor: '#FFFFFF', pantColor: '#86C5CB', shoeColor: '#1F1D5B' };
const B = { skinColor: '#E7A97F', hairColor: '#3A2415', coatColor: '#2F3CF4', shirtColor: '#FFFFFF', pantColor: '#262B6E', shoeColor: '#F4F4F4' };
const T = { skinColor: '#C98B63', hairColor: '#1F1D5B', coatColor: '#1F1D5B', shirtColor: '#E9E9F5', pantColor: '#3C3F8F', shoeColor: '#FFFFFF' };
const HM = { skinColor: '#6E4630', hairColor: '#1F1D5B', coatColor: '#FF4B33', shirtColor: '#FFFFFF', pantColor: '#1F1D5B', shoeColor: '#FFFFFF' };
const P1 = { skinColor: '#A8694A', hairColor: '#1F1D5B', coatColor: '#4FB3A9', shirtColor: '#FFFFFF', pantColor: '#1F1D5B', shoeColor: '#FFFFFF' };
const P2 = { skinColor: '#F0B892', hairColor: '#C85A2E', coatColor: '#E9A9CB', shirtColor: '#FFFFFF', pantColor: '#262B6E', shoeColor: '#FFFFFF', objectColor: '#CACDF8' };
const liste = {
  A_steht: ['Standing11', A], A_schlaegt: ['Standing19', A],
  B_rennt: ['Standing16', B], B_gibt: ['Standing23', B],
  T_links: ['Standing2', T], T_rechts: ['Standing2', T],
  Hintermann: ['Standing4', HM],
  Erklaerer: ['Standing1', P1], Grueblerin: ['Sitting6', P2], Denker: ['Sitting2', P1],
};
for (const [name, [comp, farben]] of Object.entries(liste)) {
  let svg = renderToStaticMarkup(React.createElement(H[comp], { height: 1200, ...farben }));
  svg = svg.match(/<svg[\s\S]*<\/svg>/)[0];
  if (!svg.includes('xmlns=')) svg = svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
  if (!svg.includes('xmlns:xlink')) svg = svg.replace('<svg ', '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ');
  fs.writeFileSync(`${process.argv[2]}/${name}.svg`, svg);
}
