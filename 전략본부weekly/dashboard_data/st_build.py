# -*- coding: utf-8 -*-
"""Build the 전략본부 dashboard panel (8 projects, bunkering nested) into index.html. Idempotent."""
import json, sys, os, importlib.util, re
SP='/tmp/claude-0/-home-user-skgas-knowledge/20f8b4d3-db3a-53b8-a1b4-038985727701/scratchpad/'
sys.path.insert(0,SP)
from bk_data import CATS as BK_CATS, I as BK_ITEMS, GLOSSARY as BK_GLOSS

def load(name):
    p=SP+name
    if not os.path.exists(p): print('MISSING',name); return None
    spec=importlib.util.spec_from_file_location(name[:-3],p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

WEEKS=['12/8~12','12/15~19','12/22~26','12/29~1/2','1/5~9','1/12~16','1/19~23','1/26~30','2/2~6','2/9~13','2/16~20','2/23~27','3/2~6','3/9~13','3/16~20','3/23~27','3/30~4/3','4/6~10','4/13~17','4/20~24','4/27~5/1','5/4~8','5/11~15','5/18~22','5/25~29','6/1~5','6/15~19','6/22~26','6/29~7/3','7/6~7/10','7/13~7/17','7/20~7/24','7/27~7/31','8/3~8/7','8/10~8/14','8/17~8/21','8/31~9/4','9/7~9/11','9/14~9/18','10/5~10/9','10/12~10/16','10/19~10/23','10/26~10/30']
KINDS={'done','prog','plan','risk','mile','info'}
def validate(cat,items):
    tr={t[0] for t in cat['tracks']}
    for it in items:
        assert it['t'] in tr, (cat['id'],it['t'],it['title'])
        assert it['w'] in WEEKS, (cat['id'],it['w'],it['title'])
        assert it['k'] in KINDS, (cat['id'],it['k'])
        assert re.match(r'^\d{4}-\d{2}-\d{2}$',it['d']), it['d']
        it['c']=cat['id']

projects=[]
# 1) bunkering nested
projects.append(dict(id='bk',icon='⚓',name='LNG 벙커링 (에코마린)',sub='판매·고객 / 소싱·Hedge / 항만공사 협력 / 선박·운영 / 시장·전략 / Bio-LNG',nested=True,
  what="", tracks=[], status=[]))
order=[('st_eth.py',['CAT','ITEMS']),('st_na.py',['CAT','ITEMS']),('st_hw.py',['CAT','ITEMS']),('st_ska_pos.py',['CAT_A','ITEMS_A','CAT_B','ITEMS_B']),('st_ax.py',['CAT','ITEMS']),('st_pl.py',['CAT','ITEMS'])]
all_items=[]
for fn,names in order:
    m=load(fn)
    if not m: continue
    for ci in range(0,len(names),2):
        cat=dict(getattr(m,names[ci])); items=[dict(x) for x in getattr(m,names[ci+1])]
        validate(cat,items)
        cat['nested']=False; cat['n']=len(items); projects.append(cat); all_items+=items
# bunkering flat items get p='bk'
bk_items=[dict(x,p='bk') for x in BK_ITEMS]
for it in all_items: it['p']=it['c']
data={'projects':[{k:v for k,v in p.items() if k!='n'} for p in projects],'items':all_items,'bk':{'cats':[{k:c[k] for k in ('id','icon','name','sub','what','tracks','status')} for c in BK_CATS],'items':bk_items},'glossary':BK_GLOSS}
summary=load('st_summary.py')
INTRO = summary.INTRO if summary else "<div style='font-weight:800;font-size:13.5px;margin-bottom:4px;'>🧭 처음 보는 분을 위한 30초 요약</div>전략본부는 신사업 개발(LNG 벙커링·에탄·북미·하와이), 기존 자산 최적화(SKA), 전사 리스크·포지션 관리, AX(AI 전환), 전사 전략기획·경영분석을 맡습니다. 아래 과제 카드를 누르면 각 과제의 현재 상태와 진행 과정이 펼쳐집니다."
OVERVIEW = summary.OVERVIEW if summary else ""
GLOSS_EXTRA = summary.GLOSSARY if summary else []
data['glossary']=BK_GLOSS+GLOSS_EXTRA
js_data=json.dumps(data,ensure_ascii=False).replace('</','<\\/')

hero=open(SP+'st_hero.html').read(); old_ov=open(SP+'st_old_overview.html').read()

CSS = r"""
/* ═══ 전략본부 과제 대시보드 (st-) ═══ */
.st-cards { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-bottom:14px; }
@media (max-width:1100px){ .st-cards { grid-template-columns:repeat(2,minmax(0,1fr)); } }
@media (max-width:600px){ .st-cards { grid-template-columns:minmax(0,1fr); } }
.st-cards .bk-card .bk-letter { border-radius:6px; }
.st-cards .bk-card .bk-name { font-size:13px; }
.st-nested { background:#F6F8FB; border:1px dashed #A9C8E8; border-radius:10px; padding:14px 14px 4px; margin-top:4px; }
.st-arch summary { background:#EEF3F8; border-color:#D4D6D9; color:#385269; }
.st-arch .section-label { margin-top:12px; }
.bk-card .bk-sub { min-height:30px; }
"""

PANEL = "  " + hero + """   <!-- ST-DASH START -->
   <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:#DBE6F1;border:1px solid #A9C8E8;border-radius:8px;padding:8px 14px;margin:-4px 0 14px;font-size:12px;color:#142446;">
    <span style="background:#172A55;color:white;border-radius:4px;padding:2px 8px;font-size:11px;font-weight:700;">최종 업데이트: '26.11</span>
    <span>Source: 전략본부 Weekly 보고('25.12~'26.11월) · 과제 카드를 누르면 <strong>이 과제는? → 현재 핵심 상태 → 일자별 진행(최신순)</strong>이 펼쳐집니다</span>
   </div>
   <div class="bk-intro" id="st-intro">__INTRO__</div>
   __OVERVIEW__
   <div class="bk-search">
    <span style="font-size:13px;font-weight:800;color:#142446;white-space:nowrap;">🔍 키워드 검색</span>
    <input type="search" id="st-q" placeholder="예: INEOS, H-Line, SKA 가동, AI Friday, SWAN 3.0, Hedge, EPD, 하와이 …" oninput="stSearch(this.value)" autocomplete="off">
    <span style="font-size:10.5px;color:#385269;">전 과제 통합 검색 · 여러 단어는 띄어쓰기 (모두 포함된 항목만)</span>
    <div style="width:100%;display:flex;gap:5px;flex-wrap:wrap;" id="st-chips"></div>
   </div>
   <div class="bk-results" id="st-results"></div>
   <div class="st-cards" id="st-cards"></div>
   <div class="bk-detail" id="st-detail"></div>
   <details class="bk-gloss" id="st-gloss">
    <summary>📖 용어 풀이 — LBV, 1st Trench, JKM, Hedge, FID, PDH, R-PJT, AX … (클릭해서 펼치기)</summary>
    <table id="st-gloss-table"></table>
   </details>
   <details class="bk-gloss st-arch" style="margin-top:10px;">
    <summary>🗂 아카이브 — '26.5 기준 전략본부 개요 (과제 타임라인 1~5월 · 주요 이슈)</summary>
""" + old_ov + """   </details>
   <!-- ST-DASH END -->
  </div>

"""
PANEL = PANEL.replace('__INTRO__', INTRO).replace('__OVERVIEW__', OVERVIEW)

JS = r"""
/* ═══ 전략본부 과제 대시보드 (st-) + LNG 벙커링 nested ═══ */
var ST = __DATA__;
var BK_KIND = {done:'완료·확정',prog:'진행 중',plan:'계획·예정',risk:'이슈·리스크',mile:'마일스톤',info:'정보·시사점'};
var stOpen = null, bkOpen = null, stTrack = {}, bkTrack = {};
function bkFmt(d){ var p=d.split('-'); return "'"+p[0].slice(2)+'.'+p[1]+'.'+p[2]; }
function stProj(id){ for (var i=0;i<ST.projects.length;i++) if (ST.projects[i].id===id) return ST.projects[i]; return null; }
function bkCat(id){ for (var i=0;i<ST.bk.cats.length;i++) if (ST.bk.cats[i].id===id) return ST.bk.cats[i]; return null; }
function trName(obj,t){ for (var i=0;i<obj.tracks.length;i++) if (obj.tracks[i][0]===t) return obj.tracks[i][1]; return ''; }
function byDate(a,b){ return a.d<b.d?1:a.d>b.d?-1:0; }
function stItems(pid){ return ST.items.filter(function(x){return x.p===pid;}).sort(byDate); }
function bkItems(cid){ return ST.bk.items.filter(function(x){return x.c===cid;}).sort(byDate); }
function stAllItems(){ return ST.items.concat(ST.bk.items); }
function stInit(){
  var cards=document.getElementById('st-cards'); if(!cards||cards.children.length) return;
  ST.projects.forEach(function(p,idx){
    var its = p.nested ? ST.bk.items.slice().sort(byDate) : stItems(p.id); var last=its[0];
    var b=document.createElement('button'); b.type='button'; b.className='bk-card'; b.id='st-card-'+p.id; b.setAttribute('onclick',"stToggle('"+p.id+"')");
    b.innerHTML='<div><span class="bk-letter">'+(idx+1)+'</span><span class="bk-name">'+p.icon+' '+p.name+'</span></div><div class="bk-sub">'+p.sub+'</div>'
      +'<div class="bk-meta"><span class="bk-last">최근: '+(last?bkFmt(last.d)+' '+last.title.slice(0,22)+(last.title.length>22?'…':''):'-')+'</span><span class="bk-cnt">'+its.length+'건</span></div>';
    cards.appendChild(b);
  });
  var chips=['H-Line','Maersk','JKM','Hedge','UPA','INEOS','FID','CEC','R-PJT','EPD','BCG','맥킨지','하와이','SKA','Relocation','미-이란','포지션','Trading AX','AI Friday','CEO Agent','SWAN 3.0','행캔','이사회','ZBB'];
  document.getElementById('st-chips').innerHTML=chips.map(function(k){return '<button type="button" class="bk-chip" onclick="stChip(\''+k+'\')">'+k+'</button>';}).join('');
  document.getElementById('st-gloss-table').innerHTML=ST.glossary.map(function(g){return '<tr><th>'+g[0]+'</th><td>'+g[1]+'</td></tr>';}).join('');
}
function stChip(k){ var q=document.getElementById('st-q'); q.value=k; stSearch(k); q.focus(); }
function stToggle(pid, keep){
  var d=document.getElementById('st-detail');
  document.querySelectorAll('#st-cards .bk-card').forEach(function(x){x.classList.remove('active');});
  if (stOpen===pid && !keep){ stOpen=null; d.classList.remove('open'); d.innerHTML=''; return; }
  stOpen=pid; document.getElementById('st-card-'+pid).classList.add('active');
  var p=stProj(pid);
  if (p.nested) stRenderBk(); else stRenderFlat(pid);
  d.classList.add('open');
  var top=d.getBoundingClientRect().top; if (top<0||top>window.innerHeight*0.6){ d.scrollIntoView({behavior:'smooth',block:'start'}); }
}
function stSetTrack(pid,t){ stTrack[pid]=t; stRenderFlat(pid); }
function stHead(icon,name,closeFn){ return '<div class="bk-dhead"><h3>'+icon+' '+name+'</h3><button type="button" class="bk-close" onclick="'+closeFn+'">접기 ▲</button></div>'; }
function stStatusHtml(obj){ return '<div class="bk-status"><h4>📌 현재 핵심 상태 <span style="font-size:10.5px;font-weight:600;color:#8E9398;">(최신 Weekly 기준, '+"'26.10월"+')</span></h4><ul>'+obj.status.map(function(s){return '<li class="bk-k-'+s[0]+'">'+s[1]+'</li>';}).join('')+'</ul></div>'; }
function stTracksHtml(obj,its,sel,fn){
  var h='<div class="bk-tracks"><span style="font-weight:800;">세부 트랙:</span><button type="button" class="bk-tb'+(sel==='all'?' on':'')+'" onclick="'+fn+'(\''+obj.id+'\',\'all\')">전체 ('+its.length+')</button>';
  obj.tracks.forEach(function(t){ var n=its.filter(function(x){return x.t===t[0];}).length; h+='<button type="button" class="bk-tb'+(sel===t[0]?' on':'')+'" onclick="'+fn+'(\''+obj.id+'\',\''+t[0]+'\')">'+t[1]+' ('+n+')</button>'; });
  h+='<div class="bk-legend"><span class="l-mile">마일스톤</span><span class="l-done">완료·확정</span><span class="l-prog">진행</span><span class="l-plan">계획</span><span class="l-risk">이슈</span><span class="l-info">정보</span></div></div>';
  h+='<div style="font-size:11px;color:#8E9398;margin:0 0 8px;">▼ 일자별 진행 과정 — <strong>최신이 위</strong> · 날짜는 Weekly에 명시된 날짜, 없으면 해당 Weekly 시작일(주차 표기)</div>';
  return h;
}
function stRenderFlat(pid){
  var p=stProj(pid), d=document.getElementById('st-detail'); var its=stItems(pid); var sel=stTrack[pid]||'all';
  var h=stHead(p.icon,p.name,"stToggle('"+pid+"')");
  h+='<div class="bk-what"><span class="bk-tag">이 과제는?</span>'+p.what+'</div>';
  h+=stStatusHtml(p);
  h+=stTracksHtml(p,its,sel,'stSetTrack');
  var list=its.filter(function(x){return sel==='all'||x.t===sel;});
  h+='<ul class="bk-tl">'+list.map(function(x,i){ return itemHtml(p,x,i===0?'<span class="bk-new">최신</span>':'',null); }).join('')+'</ul>';
  d.innerHTML=h;
}
function stRenderBk(){
  var d=document.getElementById('st-detail');
  var h=stHead('⚓','LNG 벙커링 (에코마린) — 6개 업무별 진척',"stToggle('bk')");
  h+='<div class="bk-intro" style="margin-bottom:12px;">'+__BK_INTRO__+'</div>';
  h+='<div class="bk-overview">'+__BK_OVERVIEW__+'</div>';
  h+='<div style="font-size:12px;color:#385269;margin:0 0 8px;font-weight:700;">▼ 업무 카드를 누르면 아래에 상세가 펼쳐집니다</div><div class="bk-cards" id="bk-cards"></div><div class="bk-detail" id="bk-detail"></div>';
  d.innerHTML=h;
  var cards=document.getElementById('bk-cards');
  ST.bk.cats.forEach(function(c){
    var its=bkItems(c.id); var last=its[0];
    var b=document.createElement('button'); b.type='button'; b.className='bk-card'; b.id='bk-card-'+c.id; b.setAttribute('onclick',"bkToggle('"+c.id+"')");
    b.innerHTML='<div><span class="bk-letter">'+c.id+'</span><span class="bk-name">'+c.icon+' '+c.name+'</span></div><div class="bk-sub">'+c.sub+'</div>'
      +'<div class="bk-meta"><span class="bk-last">최근: '+bkFmt(last.d)+' '+last.title.slice(0,26)+(last.title.length>26?'…':'')+'</span><span class="bk-cnt">'+its.length+'건</span></div>';
    cards.appendChild(b);
  });
  if (bkOpen){ var o=bkOpen; bkOpen=null; bkToggle(o); }
}
function bkToggle(id){
  var d=document.getElementById('bk-detail'); if(!d) return;
  document.querySelectorAll('#bk-cards .bk-card').forEach(function(x){x.classList.remove('active');});
  if (bkOpen===id){ bkOpen=null; d.classList.remove('open'); d.innerHTML=''; return; }
  bkOpen=id; document.getElementById('bk-card-'+id).classList.add('active');
  bkRender(id); d.classList.add('open');
  var top=d.getBoundingClientRect().top; if (top<0||top>window.innerHeight*0.6){ d.scrollIntoView({behavior:'smooth',block:'start'}); }
}
function bkSetTrack(cid,t){ bkTrack[cid]=t; bkRender(cid); }
function bkRender(cid){
  var c=bkCat(cid), d=document.getElementById('bk-detail'); var its=bkItems(cid); var sel=bkTrack[cid]||'all';
  var h='<div class="bk-dhead"><h3><span class="bk-letter" style="background:#C62828;">'+cid+'</span>'+c.icon+' '+c.name+'</h3><button type="button" class="bk-close" onclick="bkToggle(\''+cid+'\')">접기 ▲</button></div>';
  h+='<div class="bk-what"><span class="bk-tag">이 업무는?</span>'+c.what+'</div>';
  h+=stStatusHtml(c).replace("'26.10월","Weekly 10/19~23");
  h+=stTracksHtml(c,its,sel,'bkSetTrack');
  var list=its.filter(function(x){return sel==='all'||x.t===sel;});
  h+='<ul class="bk-tl">'+list.map(function(x,i){ return itemHtml(c,x,i===0?'<span class="bk-new">최신</span>':'',null); }).join('')+'</ul>';
  d.innerHTML=h;
}
function stHl(s,toks){ if(!toks||!toks.length) return s; var out=s; toks.forEach(function(t){ var re=new RegExp('('+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')(?![^<]*>)','gi'); out=out.replace(re,'<mark class="bk-hl">$1</mark>'); }); return out; }
function itemHtml(obj,x,badge,toks){
  return '<li class="bk-k-'+x.k+'"><div class="bk-date">'+bkFmt(x.d)+'<small>Weekly '+x.w+'</small><small>'+BK_KIND[x.k]+'</small></div>'
    +'<div class="bk-title"><span class="bk-trk">'+trName(obj,x.t)+'</span>'+stHl(x.title,toks)+badge+'</div>'
    +'<div class="bk-body">'+stHl(x.body,toks)+'</div>'
    +'<div class="bk-tags">'+x.tags.map(function(t){return '<span>#'+t+'</span>';}).join('')+'</div></li>';
}
function stOpenFromSearch(pid,cid){ stToggle(pid,true); if(cid){ bkOpen=null; bkToggle(cid); } }
function stSearch(q){
  var r=document.getElementById('st-results'); q=(q||'').trim();
  if(!q){ r.classList.remove('open'); r.innerHTML=''; return; }
  var toks=q.toLowerCase().split(/\s+/).filter(Boolean);
  var strip=function(s){return s.replace(/<[^>]+>/g,'').toLowerCase();};
  var hits=stAllItems().filter(function(x){ var p=stProj(x.p); var obj=x.p==='bk'?bkCat(x.c):p; var hay=strip(x.title+' '+x.body+' '+x.tags.join(' ')+' '+p.name+' '+obj.name+' '+trName(obj,x.t)); return toks.every(function(t){return hay.indexOf(t)>=0;}); }).sort(byDate);
  var byP={}; hits.forEach(function(x){ byP[x.p]=(byP[x.p]||0)+1; });
  var h='<h4>🔎 "'+q.replace(/</g,'&lt;')+'" 검색 결과 <span style="color:#C62828;">'+hits.length+'건</span> (전 과제 · 최신순)';
  ST.projects.forEach(function(p){ if(byP[p.id]) h+='<span class="bk-cat" onclick="stOpenFromSearch(\''+p.id+'\')" title="과제 상세 열기">'+p.icon+' '+p.name+' '+byP[p.id]+'</span>'; });
  h+='<button type="button" class="bk-close" style="margin-left:auto;" onclick="document.getElementById(\'st-q\').value=\'\';stSearch(\'\')">지우기 ✕</button></h4>';
  if(!hits.length){ h+='<div style="font-size:12px;color:#8E9398;">일치하는 항목이 없습니다. 다른 표기(예: 머스크 → Maersk, 헷지 → Hedge)로 검색해 보세요.</div>'; }
  else { h+='<ul class="bk-tl">'+hits.map(function(x){ var p=stProj(x.p); var obj=x.p==='bk'?bkCat(x.c):p; var lab=x.p==='bk'?'⚓ 벙커링 › '+x.c+'. '+obj.name:p.icon+' '+p.name; var oc=x.p==='bk'?"stOpenFromSearch('bk','"+x.c+"')":"stOpenFromSearch('"+x.p+"')"; return itemHtml(obj,x,'<span class="bk-trk" style="background:#172A55;color:#fff;margin-left:6px;cursor:pointer;" onclick="'+oc+'">'+lab+'</span>',toks); }).join('')+'</ul>'; }
  r.innerHTML=h; r.classList.add('open');
}
document.addEventListener('DOMContentLoaded', stInit);
"""
BK_INTRO = json.dumps("""<div style="font-weight:800;font-size:13.5px;margin-bottom:4px;">🧭 처음 보는 분을 위한 30초 요약</div><b>에코마린</b>(구 EMFS)은 SK가스가 울산 KET 터미널의 LNG를 급유선에 실어 <b>선박 연료로 파는</b> 자회사입니다. 1호 급유선 <b>Eco Frontier</b>가 '27년 4분기에 인도되고 '28년부터 상업 공급이 시작되므로, '26년은 ① 1호선에 실을 고객을 계약으로 묶고(<b>H-Line 연 5만톤</b> + 글로비스 선계약 + 컨테이너·일본 선사), ② 2호선을 띄울 수 있을 만큼 수요(약 12만톤/년)를 모으며, ③ 가격 위험을 막고(Brent-JKM Hedge), ④ 항만공사(UPA·KH)와 JV를 만들고, ⑤ 배·부두·제도를 준비하는 해입니다. 가장 큰 변수는 <b>10/20 H-Line이 주주사 반대로 5만톤 Commit이 어렵다고 통보</b>한 것이며, 일본계 대체 Term·Spot/GUCD 확대·Hedge로 대응 중입니다. 사업 기본 정보(JV 구조·1호선 제원)는 사업현황 › 벙커링(EMFS) 탭 참조.""",ensure_ascii=False)
BK_OVERVIEW = json.dumps('<div class="bk-ov"><div class="t">1호선 Eco Frontier</div><div class="v">Steel Cutting 6/19 → <b>\'27.4Q 인도</b></div>Keel Laying \'26.12 · 진수 \'27.4 · 9/18 이사회 Novation+PCG</div>'
   + '<div class="bk-ov"><div class="t">판매 (1호선 물량 확보)</div><div class="v">H-Line 5만톤 <b>10/20 Commit 곤란 통보</b></div>CMA-CGM JKM 1년 1만톤 · Maersk \'28 2.8만톤 · K-Line/MOL/Hapag 협의</div>'
   + '<div class="bk-ov"><div class="t">Brent-JKM Hedge</div><div class="v">\'28년 1만톤(50%) <b>평균 JKM-$1.69</b></div>약 12억 원가경쟁력 · Spread $4+ → 1만톤 추가 검토</div>'
   + '<div class="bk-ov"><div class="t">JV·제도</div><div class="v">3사 MOU <b>7/3 체결</b> → 12월 계약 목표</div>7/15 공급사 공동 해수부 건의 과제 도출</div>',ensure_ascii=False)
JS = JS.replace('__DATA__',js_data).replace('__BK_INTRO__',BK_INTRO).replace('__BK_OVERVIEW__',BK_OVERVIEW)

p='/home/user/skgas-knowledge/index.html'; s=open(p,encoding='utf-8').read()
# panel
mi=re.search(r'\n *<div class="div-panel" id="div-strategy">',s); mj=re.search(r'\n *<div class="div-panel" id="div-finance">',s); assert mi and mj and mj.start()>mi.start()
s=s[:mi.start()+1]+PANEL+'  '+s[mj.start()+1:].lstrip(' ')
# CSS: replace old st-tabs css + any previous st- css block
s=re.sub(r'\n\.st-tabs \{.*?\.st-page\.active \{ display:block; \}\n','\n',s,flags=re.S)
s=re.sub(r'\n/\* ═══ 전략본부 과제 대시보드 \(st-\) ═══ \*/.*?(?=\n/\* ═══ LNG 벙커링 업무 대시보드 \(bk-\) ═══ \*/)','',s,flags=re.S)
k=s.find('/* ═══ LNG 벙커링 업무 대시보드 (bk-) ═══ */'); s=s[:k]+CSS.lstrip('\n')+'\n'+s[k:]
# JS: remove old switchSt + old bk block, insert new before last </script>
s=re.sub(r'function switchSt\(id, btn\) \{.*?\n\}\n','',s,flags=re.S)
a=s.find('/* ═══ LNG 벙커링 업무 대시보드 ═══ */'); 
if a<0: a=s.find('/* ═══ 전략본부 과제 대시보드 (st-) + LNG 벙커링 nested ═══ */')
b=s.rfind('</script>'); assert a>0 and b>a
s=s[:a]+JS.lstrip('\n')+'\n'+s[b:]
open(p,'w',encoding='utf-8').write(s)
print('built: projects',[ (q['id'],q.get('n','bk')) for q in projects],'items',len(all_items))
