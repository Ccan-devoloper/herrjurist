import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { vorproduktionLaden, planAusVorproduktion, inhalteUebernehmen, feedAssets, storyAsset, feedWartezeitMs } from "../src/vorproduktion-live.mjs";

function fixture() {
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),"vp-live-"));
  const stateDir=path.join(dir,"state");
  fs.mkdirSync(stateDir,{recursive:true});
  const hosting={
    dir,stateDir,basisUrl:"https://example.invalid/instagram-assets",
    jsonSchreiben(name,data){ const p=path.join(stateDir,name); fs.mkdirSync(path.dirname(p),{recursive:true}); fs.writeFileSync(p,JSON.stringify(data)); }
  };
  return {dir,stateDir,hosting};
}

function tagAnlegen(dir, datum="2026-09-24") {
  const fertig=path.join(dir,"vorproduktion",datum,"fertig");
  fs.mkdirSync(path.join(fertig,"b1"),{recursive:true});
  fs.mkdirSync(path.join(fertig,"b3"),{recursive:true});
  fs.mkdirSync(path.join(fertig,"stories"),{recursive:true});
  fs.writeFileSync(path.join(fertig,"b1",`${datum}-b1-01.jpg`),"x");
  fs.writeFileSync(path.join(fertig,"b3",`${datum}-b3-cover.jpg`),"x");
  fs.writeFileSync(path.join(fertig,"b3",`${datum}-b3.mp4`),"x");
  fs.writeFileSync(path.join(fertig,"stories","s1-teaser.jpg"),"x");
  const tag={
    datum,
    renderVorschau:{pfad:`vorproduktion/${datum}/fertig`},
    plan:{
      beitraege:[
        {slot:"b1",zeit:"07:30",format:"spickzettel",themaId:"t1"},
        {slot:"b3",zeit:"21:30",format:"reel",themaId:"t3"}
      ],
      stories:[{slot:"s1",zeit:"07:30",art:"teaser",beitragSlot:"b1"}]
    },
    inhalte:{
      b1:{slug:`${datum}-b1`,caption:"c1",hashtags:[],manuellGeprueft:true},
      b3:{slug:`${datum}-b3`,caption:"c3",hashtags:[],szenen:[{titel:"r"}],manuellGeprueft:true}
    }
  };
  fs.mkdirSync(path.join(dir,"vorproduktion"),{recursive:true});
  fs.writeFileSync(path.join(dir,"vorproduktion",`${datum}.json`),JSON.stringify(tag));
  return tag;
}

test("ohne Tagespaket bleibt der autonome Fallback aktiv",()=>{
  const {hosting}=fixture();
  assert.equal(vorproduktionLaden(hosting,"2026-09-24"),null);
});

test("Vorproduktion wird vollstaendig geladen und fertige Assets werden direkt adressiert",()=>{
  const {dir,hosting}=fixture();
  tagAnlegen(dir);
  const vp=vorproduktionLaden(hosting,"2026-09-24");
  assert.equal(vp.tag.plan.beitraege[0].zeit,"07:30");
  assert.equal(feedAssets(vp,vp.tag.plan.beitraege[0]).bildUrls.length,1);
  assert.match(feedAssets(vp,vp.tag.plan.beitraege[1]).videoUrl,/b3\.mp4$/);
  assert.match(storyAsset(vp,"s1").bildUrl,/s1-teaser\.jpg$/);
});

test("bestehende echte Veroeffentlichungen werden beim Ueberlagern bewahrt",()=>{
  const {dir,hosting}=fixture();
  tagAnlegen(dir);
  const vp=vorproduktionLaden(hosting,"2026-09-24");
  const plan=planAusVorproduktion(vp,{beitraege:[{slot:"b1",status:"veroeffentlicht",medienId:"123",veroeffentlicht:"2026-09-24T05:30:00Z"}],stories:[]});
  assert.equal(plan.beitraege[0].status,"veroeffentlicht");
  assert.equal(plan.beitraege[0].medienId,"123");
  assert.equal(plan.beitraege[1].status,"geplant");
});

test("Inhalte werden als live-verknuepfte Vorproduktion abgelegt",()=>{
  const {dir,stateDir,hosting}=fixture();
  tagAnlegen(dir);
  const vp=vorproduktionLaden(hosting,"2026-09-24");
  const plan=planAusVorproduktion(vp);
  assert.equal(inhalteUebernehmen(hosting,vp,plan),2);
  const b1=JSON.parse(fs.readFileSync(path.join(stateDir,"inhalte","2026-09-24-b1.json"),"utf8"));
  assert.equal(b1.liveVerknuepft,true);
  assert.equal(b1.freigabeBetreiber,true);
});

test("belegter aber unvollstaendiger Tag faellt hart aus statt kostenpflichtig zu regenerieren",()=>{
  const {dir,hosting}=fixture();
  tagAnlegen(dir);
  fs.unlinkSync(path.join(dir,"vorproduktion","2026-09-24","fertig","b3","2026-09-24-b3.mp4"));
  assert.throws(()=>vorproduktionLaden(hosting,"2026-09-24"),/kein kostenpflichtiger Fallback/);
});

test("Feed-Wartezeit zielt auf die echte Veröffentlichungsminute",()=>{
  const plan={beitraege:[
    {slot:"b1",zeit:"07:30",status:"geplant"},
    {slot:"b2",zeit:"17:30",status:"geplant"}
  ]};
  assert.equal(feedWartezeitMs(plan,7*3600+5*60),25*60*1000);
  assert.equal(feedWartezeitMs(plan,6*3600),90*60*1000);
});

test("Frühe Story bestimmt die Wartezeit vor einem späteren Feed-Slot",()=>{
  const plan={
    beitraege:[{slot:"b1",zeit:"08:30",status:"geplant"}],
    stories:[
      {slot:"s4",zeit:"07:15",status:"geplant"},
      {slot:"s5",zeit:"07:15",status:"veroeffentlicht"}
    ]
  };
  assert.equal(feedWartezeitMs(plan,7*3600+5*60),10*60*1000);
});

test("Kein Warten wenn ein Feed-Slot bereits fällig ist oder zu weit entfernt liegt",()=>{
  assert.equal(feedWartezeitMs({beitraege:[{zeit:"07:30",status:"geplant"}]},7*3600+31*60),0);
  assert.equal(feedWartezeitMs({beitraege:[{zeit:"12:00",status:"geplant"}]},9*3600),0);
});
