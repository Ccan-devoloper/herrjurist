import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const dir=path.dirname(fileURLToPath(import.meta.url));
const CH=process.env.REICHWEITE_KANAL||'examenscampus';
const CFG={
 examenscampus:{label:'Examenscampus',domain:'steuer',tags:['steuerberaterexamen','steuerberaterprüfung','steuerberater','steuerrecht','abgabenordnung','umsatzsteuer','bilanzierung','ertragsteuer','steuerfachwirt','examensvorbereitung'],keys:['steuerberater','steuerrecht','abgabenordnung','ao','estg','ustg','kstg','gewstg','bilanz','jahresabschluss','umwandlung','ertragsteuer','umsatzsteuer','klausur','examen','prüfung','lernen']},
 herrjurist:{label:'Herr Jurist',domain:'jura',tags:['jura','jurastudium','staatsexamen','jurastaatsexamen','rechtsreferendariat','zivilrecht','strafrecht','öffentlichesrecht','examensvorbereitung','jurastudent'],keys:['jura','staatsexamen','examen','klausur','bgb','stgb','vwgo','gg','zivilrecht','strafrecht','öffentliches recht','referendariat','urteil','beschluss','bgh','bverfg','bverwg','eugh','lernen']}
}[CH];
if(!CFG) throw new Error(`Unbekannter Kanal ${CH}`);

const clean=s=>String(s||'').replace(/https?:\/\/\S+/gi,'').replace(/(^|\s)#[\p{L}\p{N}_]+/gu,' ').replace(/\s+/g,' ').trim();
const cut=(s,n=420)=>{s=clean(s);return s.length<=n?s:s.slice(0,n-1).replace(/\s+\S*$/,'')+'…'};
const norm=s=>CFG.domain==='steuer'
 ?(s.match(/§{1,2}\s*\d+[a-z]?(?:\s*(?:Abs\.?|S\.?|Satz|Nr\.?)\s*\d+[a-z]?)?\s*(?:AO|EStG|UStG|KStG|GewStG|ErbStG|HGB|UmwStG|BewG)/i)?.[0]||'')
 :(s.match(/(?:§{1,2}\s*\d+[a-z]?(?:\s*(?:Abs\.?|S\.?|Satz|Nr\.?)\s*\d+[a-z]?)?\s*(?:BGB|StGB|StPO|ZPO|VwGO|VwVfG|GG|HGB)|Art\.?\s*\d+[a-z]?(?:\s*Abs\.?\s*\d+)?\s*(?:GG|AEUV|EUV)?)/i)?.[0]||'');
const labels={ao:'der Abgabenordnung',estg:'dem EStG',ustg:'dem UStG',kstg:'dem KStG',gewstg:'dem GewStG',bgb:'dem BGB',stgb:'dem StGB',vwgo:'der VwGO',gg:'den Grundrechten',zivilrecht:'dem Zivilrecht',strafrecht:'dem Strafrecht','öffentliches recht':'dem Öffentlichen Recht',umsatzsteuer:'der Umsatzsteuer',bilanz:'der Bilanzierung',steuerrecht:'dem Steuerrecht',staatsexamen:'dem Staatsexamen',jurastudium:'dem Jurastudium',referendariat:'dem Referendariat'};
function topic(s){const l=s.toLowerCase(),k=CFG.keys.find(x=>l.includes(x));if(k)return labels[k]||k;const t=clean(s).split(/(?<=[.!?])\s+/)[0].split(/\s+/).slice(0,10).join(' ');return t?`„${t.slice(0,80)}${t.length>80?'…':''}“`:'dem Thema'}
const REL=CFG.domain==='steuer'
 ?{strong:['steuerberaterprüfung','steuerberaterexamen','steuerrecht','abgabenordnung','estg','ustg','kstg','gewstg','erbstg','bewg','umwstg','bilanzsteuerrecht','einkommensteuer','umsatzsteuer','körperschaftsteuer','gewerbesteuer','erbschaftsteuer','jahresabschluss','steuerfachwirt'],weak:['steuerberater','klausur','prüfung','examen','bilanz','buchführung','lernen'],negative:['stellenangebot','wir suchen','bewerbung','karriere','gewinnspiel','rabatt','kanzleialltag','team-event']}
 :{strong:['staatsexamen','jurastudium','referendariat','zivilrecht','strafrecht','öffentliches recht','bgb','stgb','zpo','stpo','vwgo','vwvfg','grundgesetz','bverfg','bgh','eugh','examensklausur'],weak:['jura','jurist','klausur','prüfung','examen','urteil','beschluss','lernen','jurastudent'],negative:['stellenangebot','wir suchen','bewerbung','karriere','gewinnspiel','rabatt','kanzleialltag','law firm','team-event']};
function relevance(s,trusted=false){const t=clean(s).toLowerCase(),strong=REL.strong.filter(k=>t.includes(k)),weak=REL.weak.filter(k=>t.includes(k)),negative=REL.negative.filter(k=>t.includes(k)),statute=Boolean(norm(s));return{strong,weak,negative,statute,relevant:statute||strong.length>0||weak.length>=2||(trusted&&weak.length>=1&&negative.length===0)}}

function comments(m){const s=clean(m.caption),t=topic(s),n=norm(s),court=/\b(bgh|bverfg|bverwg|bfh|eugh|olg|fg)\b/i.test(s),exam=/\b(examen|staatsexamen|steuerberaterprüfung|steuerberaterexamen|klausur|prüfung)\b/i.test(s);let a;
 if(CFG.domain==='steuer') a=n?[`Guter Punkt zu ${t}. Gerade für die StB-Prüfung lohnt es sich, ${n} nicht isoliert zu lernen, sondern den Prüfungsschritt sauber einzuordnen.`,`Sehr anschaulich. Bei ${t} ist für die Klausur gerade die Verknüpfung mit ${n} spannend.`]:exam?[`Treffend auf den Punkt gebracht. Bei ${t} ist in der StB-Prüfung oft die saubere Reihenfolge wichtiger als noch mehr Einzelwissen.`,`Guter Examenshinweis. ${t} wird deutlich sicherer, wenn man es einmal klausurmäßig durchprüft.`]:[`Spannender Beitrag zu ${t}. Genau solche Praxisbezüge helfen, den Stoff fürs Steuerberaterexamen wirklich einzuordnen.`,`Guter Impuls zu ${t}. Für die Examensvorbereitung würde ich daraus direkt einen Mini-Fall machen.`];
 else a=n?[`Starker Punkt zu ${t}. Für die Klausur ist bei ${n} die Einordnung im richtigen Prüfungsschritt entscheidend.`,`Sehr anschaulich erklärt. ${n} wird examensfest, wenn man ${t} direkt mit der passenden Prüfungsstelle verknüpft.`]:court?[`Spannende Entscheidung. Für Examenskandidaten ist bei ${t} vor allem interessant, an welcher Stelle im Gutachten die Aussage des Gerichts wirklich etwas verändert.`,`Danke fürs Aufbereiten. Bei ${t} würde ich mir fürs Examen direkt Problemtrigger, Prüfungsstelle und Rechtsfolge notieren.`]:exam?[`Treffend formuliert. Bei ${t} bringt fürs Examen eine klare Prüfungsreihenfolge meistens mehr als noch mehr Detailwissen.`,`Guter Examenshinweis. ${t} wird deutlich sicherer, wenn man es einmal in einer kurzen Lösungsskizze übt.`]:[`Spannender Beitrag zu ${t}. Gerade fürs Examen hilft es, daraus direkt einen Problemtrigger und die passende Prüfungsstelle abzuleiten.`,`Sehr verständlich dargestellt. ${t} bleibt besser hängen, wenn man es mit einem kurzen Fall statt nur abstrakt lernt.`];
 const i=parseInt(crypto.createHash('sha256').update(String(m.id||m.permalink)).digest('hex').slice(0,8),16)%a.length;return [a[i],a[(i+1)%a.length]]}
async function get(base,ep,p,token){const u=new URL(`${base}/${ep.replace(/^\//,'')}`);for(const[k,v]of Object.entries(p||{}))if(v!==''&&v!=null)u.searchParams.set(k,v);u.searchParams.set('access_token',token);const r=await fetch(u,{headers:{'user-agent':'reichweite-dashboard/1.0'}}),j=await r.json().catch(()=>({}));if(!r.ok||j.error){const e=new Error(j.error?.message||`HTTP ${r.status}`);e.code=j.error?.code;throw e}return j}
async function collect(base,id,token){const out=[],errors=[];let own=new Set;try{const x=await get(base,`${id}/media`,{fields:'id',limit:100},token);own=new Set((x.data||[]).map(x=>x.id))}catch{}
 for(const tag of CFG.tags){try{let h;try{h=await get(base,`${id}/hashtag_search`,{q:tag},token)}catch{h=await get(base,'ig_hashtag_search',{user_id:id,q:tag},token)}const hid=h.data?.[0]?.id;if(!hid)continue;const x=await get(base,`${hid}/recent_media`,{user_id:id,fields:'id,caption,media_type,permalink,timestamp,like_count,comments_count',limit:30},token);for(const m of x.data||[])if(m.permalink&&!own.has(m.id))out.push({...m,foundVia:tag})}catch(e){errors.push({tag,message:e.message,code:e.code||null});if([10,100,190,200].includes(+e.code))break}}
 return {out,errors}}

const WEB_QUERIES = CFG.domain==='steuer'
 ? ['steuerberaterprüfung steuerrecht examen','steuerberaterexamen klausur AO EStG','steuerberaterprüfung 2026 lernen']
 : ['jura staatsexamen klausur','jurastudium examen BGB','jura examensvorbereitung rechtsprechung'];
const decodeHtml=s=>String(s||'').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#39;|&apos;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&#(\d+);/g,(_,n)=>String.fromCodePoint(+n));
const stripHtml=s=>decodeHtml(String(s||'').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,' ').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim());
function webCandidates(html,via){
 const src=String(html||'').replace(/\\\//g,'/'), hits=[];
 const push=(url,idx)=>{try{url=decodeURIComponent(url)}catch{};url=decodeHtml(url);const m=url.match(/https?:\/\/(?:www\.)?instagram\.com\/(p|reel)\/([A-Za-z0-9_-]+)/i);if(!m)return;const permalink=`https://www.instagram.com/${m[1]}/${m[2]}/`;const context=stripHtml(src.slice(Math.max(0,idx-900),Math.min(src.length,idx+1600)));hits.push({id:`web-${m[2]}`,permalink,media_type:m[1].toLowerCase()==='reel'?'REELS':'IMAGE',caption:cut(context,650),timestamp:null,like_count:0,comments_count:0,foundVia:via})};
 for(const m of src.matchAll(/https?:\/\/(?:www\.)?instagram\.com\/(?:p|reel)\/[A-Za-z0-9_-]+/gi))push(m[0],m.index||0);
 for(const m of src.matchAll(/https?%3A%2F%2F(?:www\.)?instagram\.com%2F(?:p|reel)%2F[A-Za-z0-9_-]+/gi))push(m[0],m.index||0);
 for(const m of src.matchAll(/(?:uddg|url)=([^"'&\s>]+)/gi))push(m[1],m.index||0);
 for(const m of src.matchAll(/href=["'](?:https?:\/\/imginn\.com)?\/p\/([A-Za-z0-9_-]+)\/?["']/gi))push(`https://www.instagram.com/p/${m[1]}/`,m.index||0);
 return hits;
}

const PROFILE_HANDLES = CFG.domain==='steuer'
 ? ['knollsteuer','steuerfachschuleendriss','studienwerkdersteuerberater','nwbverlag','zweisteuerberater']
 : [];
function igItem(item,handle){
 const code=item?.code||item?.shortcode||item?.node?.shortcode;
 if(!code)return null;
 const product=item?.product_type||item?.node?.product_type||'';
 const mediaType=item?.media_type||item?.node?.media_type;
 const reel=product==='clips'||product==='reels'||mediaType===2;
 const carousel=mediaType===8||Array.isArray(item?.carousel_media)||item?.node?.__typename==='GraphSidecar';
 const caption=item?.caption?.text||item?.node?.edge_media_to_caption?.edges?.[0]?.node?.text||item?.node?.caption||'';
 const ts=item?.taken_at||item?.node?.taken_at_timestamp;
 return {
   id:String(item?.pk||item?.id||item?.node?.id||('profile-'+code)),
   permalink:`https://www.instagram.com/${reel?'reel':'p'}/${code}/`,
   media_type:reel?'REELS':carousel?'CAROUSEL_ALBUM':'IMAGE',
   caption, timestamp:ts?new Date(Number(ts)*1000).toISOString():null,
   like_count:Number(item?.like_count||item?.node?.edge_liked_by?.count||item?.node?.edge_media_preview_like?.count||0),
   comments_count:Number(item?.comment_count||item?.node?.edge_media_to_comment?.count||0),
   foundVia:`@${handle}`
 };
}
async function collectProfiles(){
 const out=[],errors=[];
 if(!PROFILE_HANDLES.length)return {out,errors};
 const headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36',
   'x-ig-app-id':'936619743392459',
   'accept':'*/*',
   'accept-language':'de-DE,de;q=0.9,en;q=0.7'
 };
 for(const handle of PROFILE_HANDLES){
  try{
   const u=`https://i.instagram.com/api/v1/users/web_profile_info/?username=${encodeURIComponent(handle)}`;
   const r=await fetch(u,{headers:{...headers,referer:`https://www.instagram.com/${handle}/`},redirect:'follow'});
   if(!r.ok)throw new Error(`web_profile_info HTTP ${r.status}`);
   const j=await r.json();
   const user=j?.data?.user||j?.user;
   const edges=user?.edge_owner_to_timeline_media?.edges||user?.edge_felix_video_timeline?.edges||[];
   for(const e of edges){const x=igItem(e,handle);if(x)out.push(x)}
   const uid=user?.id||user?.pk;
   if(!edges.length&&uid){
    try{
     const fr=await fetch(`https://www.instagram.com/api/v1/feed/user/${uid}/?count=12`,{headers:{...headers,referer:`https://www.instagram.com/${handle}/`},redirect:'follow'});
     if(fr.ok){const fj=await fr.json();for(const it of fj?.items||[]){const x=igItem(it,handle);if(x)out.push(x)}}
     else errors.push({source:'InstagramWebFeed',query:handle,message:`HTTP ${fr.status}`});
    }catch(e){errors.push({source:'InstagramWebFeed',query:handle,message:e.message})}
   }
  }catch(e){errors.push({source:'InstagramWebProfile',query:handle,message:e.message})}
 }
 return {out,errors};
}
async function collectWeb(){
 const out=[],errors=[];
 const ua={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36','accept-language':'de-DE,de;q=0.9,en;q=0.7'};
 for(const q0 of WEB_QUERIES){
  const q=`site:instagram.com/reel/ OR site:instagram.com/p/ ${q0}`;
  const urls=[
   ['DuckDuckGo',`https://html.duckduckgo.com/html/?q=${encodeURIComponent(q)}`],
   ['Bing',`https://www.bing.com/search?q=${encodeURIComponent(q)}&count=30&setlang=de-DE`]
  ];
  for(const [name,url] of urls)try{const r=await fetch(url,{headers:ua,redirect:'follow'});if(!r.ok)throw new Error(`HTTP ${r.status}`);const h=await r.text();out.push(...webCandidates(h,`${name}: ${q0}`))}catch(e){errors.push({source:name,query:q0,message:e.message})}
 }
 for(const tag of CFG.tags.slice(0,6))try{const r=await fetch(`https://imginn.com/tags/${encodeURIComponent(tag)}/`,{headers:ua,redirect:'follow'});if(!r.ok)throw new Error(`HTTP ${r.status}`);out.push(...webCandidates(await r.text(),`Imginn #${tag}`))}catch(e){errors.push({source:'Imginn',query:tag,message:e.message})}
 return {out,errors};
}

function rank(items){
 const map=new Map;for(const m of items)map.set(m.id||m.permalink,m);
 const now=Date.now();
 const scored=[...map.values()].map(m=>{
  const caption=clean(m.caption),trusted=String(m.foundVia||'').startsWith('@'),rel=relevance(caption,trusted),age=m.timestamp?Math.max(0,(now-Date.parse(m.timestamp))/36e5):96;
  if(!rel.relevant||age>24*90)return null;
  const freshness=Math.max(0,36-age/3),engagement=Math.log10((+m.like_count||0)+1)*5+Math.log10((+m.comments_count||0)+1)*9;
  const formatBonus=m.media_type==='CAROUSEL_ALBUM'?6:m.media_type==='IMAGE'?3:0;
  const score=Math.round((rel.strong.length*18+rel.weak.length*6+(rel.statute?20:0)-rel.negative.length*15+freshness+engagement+formatBonus)*10)/10;
  const [c,a]=comments(m);
  return{id:m.id,permalink:m.permalink,mediaType:m.media_type||'',timestamp:m.timestamp||null,likeCount:+m.like_count||0,commentCount:+m.comments_count||0,caption:cut(m.caption),foundVia:m.foundVia,score,matchedTerms:[...rel.strong,...rel.weak].slice(0,5),comment:c,alternativeComment:a};
 }).filter(Boolean).filter(x=>x.score>=20).sort((a,b)=>b.score-a.score);
 const selected=[],sources=new Map;let reels=0;
 for(const x of scored){
  const isReel=/REEL/i.test(x.mediaType),source=String(x.foundVia||'');
  if(isReel&&reels>=6)continue;
  if(source.startsWith('@')&&(sources.get(source)||0)>=3)continue;
  selected.push(x);
  if(isReel)reels++;
  sources.set(source,(sources.get(source)||0)+1);
  if(selected.length>=18)break;
 }
 return selected;
}
function encrypt(payload,pem){const k=crypto.randomBytes(32),iv=crypto.randomBytes(12),c=crypto.createCipheriv('aes-256-gcm',k,iv);c.setAAD(Buffer.from('reichweite-data-v1'));const data=Buffer.concat([c.update(Buffer.from(JSON.stringify(payload))),c.final()]);const tag=c.getAuthTag(),wk=crypto.publicEncrypt({key:pem,oaepHash:'sha256',padding:crypto.constants.RSA_PKCS1_OAEP_PADDING},k);return{version:1,alg:'RSA-OAEP-256+A256GCM',aad:'reichweite-data-v1',createdAt:new Date().toISOString(),iv:iv.toString('base64'),tag:tag.toString('base64'),key:wk.toString('base64'),data:data.toString('base64')}}

const token=process.env.IG_ACCESS_TOKEN||'',fbToken=process.env.FB_PAGE_TOKEN||'',id=process.env.IG_ACCOUNT_ID||'',ver=process.env.IG_GRAPH_VERSION||'v23.0',host=process.env.IG_GRAPH_HOST||'instagram',out=process.env.REICHWEITE_OUT||path.resolve('out/reichweite.enc.json'),pem=await fs.readFile(path.join(dir,'public-key.pem'),'utf8');
let found=[],errs=[],used=null,source=null;
if(id){
 const fb=`https://graph.facebook.com/${ver}`,ig=`https://graph.instagram.com/${ver}`;
 const attempts=[];
 if(token) attempts.push({base:host==='facebook'?fb:ig,token,label:'instagram-konfig'});
 if(fbToken) attempts.push({base:fb,token:fbToken,label:'facebook-seite'});
 if(token && host!=='instagram') attempts.push({base:ig,token,label:'instagram-login'});
 if(token && host!=='facebook') attempts.push({base:fb,token,label:'facebook-mit-ig-token'});
 const seen=new Set();
 for(const a of attempts){
  const k=a.base+'|'+a.token;
  if(seen.has(k)) continue;
  seen.add(k);
  const r=await collect(a.base,id,a.token);
  errs.push(...r.errors.map(e=>({...e,base:a.base,auth:a.label})));
  if(r.out.length){found=r.out;used=a.base;source='meta-hashtags';break}
 }
}
if(!found.length){
 const p=await collectProfiles();
 found=p.out;
 errs.push(...p.errors);
 if(found.length) source='public-instagram-profile';
}
if(!found.length){
 const w=await collectWeb();
 found=w.out;
 errs.push(...w.errors);
 if(found.length) source='public-web-search';
}
const posts=rank(found);
const payload={
 channel:CH,label:CFG.label,generatedAt:new Date().toISOString(),
 status:posts.length?'ok':'keine-treffer',source,apiBase:used,posts,
 message:posts.length?`${posts.length} öffentliche Instagram-Posts ausgewählt.`:'Keine geeigneten öffentlichen Instagram-Posts gefunden. Meta-Public-Content ist nicht freigeschaltet und die kostenfreie Websuche lieferte keine verwertbaren Direktlinks.',
 errors:errs.slice(0,12)
};
await fs.mkdir(path.dirname(out),{recursive:true});await fs.writeFile(out,JSON.stringify(encrypt(payload,pem),null,2)+'\n');console.log(`[reichweite] ${CFG.label}: ${payload.posts?.length||0} Vorschläge · ${payload.status}`);
