# -*- coding: utf-8 -*-
# 북미 NG/NGL 전략 (Upstream·Midstream) 과제 진척 데이터 (전략본부 Weekly '25.12/8 ~ '26.10/30 기준)
# k: done(완료/확정) prog(진행) plan(계획/예정) risk(이슈/리스크) mile(마일스톤) info(정보/시사점)

CAT = dict(
  id='na', icon='🌎', name='북미 NG/NGL 전략 (Upstream·Midstream)',
  sub='R-PJT(E&S 공동·맥킨지) · NG/NGL 사업모델·BCG PJT·Wet Gas BM · Midstream 인수 검토·EPD · Upstream 협력·11월 미국 출장',
  what="미국에서 <b>천연가스(NG)와 NGL(Natural Gas Liquids, 천연가스에서 분리되는 에탄·프로판 등 액체 성분)</b>을 직접 확보하는 사업모델을 만드는 일입니다. 지금은 미국산 LPG·에탄·LNG를 선적항 가격(FOB)에 사오는 구조라 가격 변동에 그대로 노출되는데, <b>가스전 지분(Upstream)</b>이나 <b>파이프라인·분리시설·수출터미널 처리용량(Midstream, Tolling)</b>을 갖추면 ① 구조적 원가경쟁력, ② Natural Hedge(미국 가스가격 HH가 오르면 가스전 수익이 늘어 LNG 구매 부담을 상쇄), ③ 미국 내수-수출 간 가격차를 활용하는 Optionality(선택권)를 얻을 수 있다는 것이 출발 가설입니다. SWAN 3.0(중장기 성장전략)의 핵심 과제로 '26년 4/23 CEO 보고 후 착수했고, 크게 네 갈래로 진행됩니다. ① SK E&S와 공동으로 맥킨지와 수행한 <b>R-PJT</b>(그룹 LNG 전략·Team SK 협업), ② BCG와 함께 사업모델을 검증하는 <b>NGL PJT</b>(현재는 NGL 함량이 높은 <b>Wet Gas</b> 가스전 중심의 BM으로 수렴), ③ 미국 Midstream 업체 <b>Twin Eagle</b> 인수 검토와 미국 최대 NGL Midstream 사업자 <b>EPD</b>(Enterprise Products Partners)와의 협력, ④ <b>EOG·Devon·ConocoPhillips</b> 등 Upstream 업체와의 협력 및 11월 미국 출장 준비입니다. Non-op(운영권 없는 지분 참여), Y-grade(분리 전 혼합 NGL), Dry Gas(메탄 위주 가스) 같은 용어가 자주 나옵니다.",
  tracks=[('na1','R-PJT (E&S 공동·맥킨지)·LNG 전략'),('na2','NG/NGL 사업모델·BCG PJT·Wet Gas BM'),('na3','Midstream 인수 검토(Twin Eagle)·EPD 협력'),('na4','Upstream 투자 Rationale·업체 협력·11월 출장')],
  status=[
   ("prog","<b>Wet Gas BM 구체화 중</b>(10/26~30 기준): 투자 대상은 NGL 함량이 높고 Oil 생산 비중이 낮은 Wet Gas 자산(<b>Eagle Ford·Appalachia 우선</b>), <b>Non-op 지분 참여 + 핵심 계약상 권리 확보</b>로 투자·운영 리스크 최소화. 초과 C1(메탄)은 한화 등 C1 Offtaker와 공동투자로 해결, NGL은 Y-grade 판매 후 C2/C3 FOB 구매, NG는 Physical 연계 우선(Virtual 연계 등 옵션 개방). 별도 논의 예정."),
   ("plan","<b>11월 미국 출장</b>: 11/16 미국 에너지부 장관 미팅(미국산 LPG 수출 확대 협력, 방글라데시·하와이 LPG 사업 지원 기반)과 Upstream 업체 <b>EOG·Devon·ConocoPhillips</b> 미팅 예정. Wet Gas BM과 연계한 Upstream 투자·NG/NGL 공급 협력 가능 영역을 업체별로 검토 중 (출장 결과는 10/30까지 Weekly 미보고)."),
   ("done","<b>EPD 경영진 미팅 8/20 완료</b>: EPD는 Upstream 진출 방식으로 E&P사 Non-op 지분 참여가 적합, Wet Gas 확보는 <b>Eagle Ford가 가장 유망</b>, EOG·Devon을 유력 파트너로 추천. 이후 NGL 사업은 EPD 협업을 전제로 Y-grade 판매 → 수출터미널 FOB 에탄 구매 구조의 경제성·가격·물량 연계·역할 분담을 검증 중."),
   ("info","사업 진출 목표는 ① 구조적 원가경쟁력, ② Natural Hedge, ③ 내수-수출 Optionality(8/10~14 정리). NG는 원가경쟁력 확보에 <b>E&P 투자 필요</b>, NGL은 Rich Gas E&P 투자 시 <b>에탄 Off-take 역량을 협상 Lever</b>로 인수 조건·Fractionation Tolling Fee 개선이 핵심, <b>프로판 내수-수출 Switching Optionality는 실행 가능 기회가 제한적</b>이라고 판단. 초기 진입은 운영경험 부재를 고려해 Non-operator 모델이 적절(9/14~18)."),
   ("done","<b>Twin Eagle(미국 NG Midstream) 인수 검토 종료</b>: 6월 지분인수 검토 요청 → Non-binding IOI를 Lazard에 제출(6/29~7/3) → 7/17 Data Room Access 확보했으나, T사가 기존 잠재 인수자와 거래 완료를 통보해 7/20~24 실사·인수 검토 종료. 확보한 미국 내수 트레이딩 Insight는 전략 수립에 활용."),
   ("prog","<b>R-PJT(E&S 공동, 맥킨지)</b>: 6/4 Kick-off → 7/10 경영진 Progress Update(선제적 Long 확보 선순환 구조 공감) → 7/30 중간보고 목표로 Team SK 협업 영역 5개(Wet Gas 경제성, AIDC 발전향 NG/에탄, Switching+에탄, 선박 공동활용, Multi-Fuel 발전) 도출. 8/10~14 시너지 정량화 초안 공유 후 E&S가 미국·호주 Upstream 소싱 가격을 제공하기로 함 (<b>8/10~14 이후 R-PJT 관련 Weekly 미보고</b>)."),
  ],
)

I = []
def add(c,t,d,w,k,title,body,tags):
    I.append(dict(c=c,t=t,d=d,w=w,k=k,title=title,body=body,tags=tags))

# ───────── H1: SWAN 3.0 내 Upstream 가설 → 북미 NG/NGL Play 착수 ─────────
add('na','na2','2026-01-12','1/12~16','info',"SWAN 3.0 준비: 3대 추진 관점 중 하나로 'LNG Upstream 등 V/C 확장' 설정",
 "SWAN 3.0은 (1) 저JKM 시황에서도 수익창출 가능하도록 기존 사업모델 고도화, (2) <b>LNG Upstream 등 Value Chain 확장</b>, (3) Power to Information의 Mega 전력 트렌드 하 신규 사업기회 발굴 관점에서 추진 예정. '30년 기준 전사 Price position 분석 병행 (이후 북미 NG/NGL 과제로 구체화되는 Upstream 확장 검토의 첫 언급).",
 ['SWAN 3.0','Upstream','Value Chain 확장','저JKM'])
add('na','na2','2026-01-26','1/26~30','plan',"LNG Upstream 확장 Feasibility 검토 착수 — 준비되는 대로 CEO 보고 예정",
 "CEC 물적분할·배출권 거래제 Impact와 함께 <b>LNG Upstream 확장 Feasibility</b>를 검토 중이며, 준비되는 대로 사장님께 보고 예정.",
 ['Upstream','Feasibility','LNG'])
add('na','na2','2026-02-16','2/16~20','prog',"SWAN 3.0 Framework 및 Upstream Key Question·초기 가설 수립 착수",
 "SWAN 3.0 검토 필요영역을 SWAN 2.0의 발전적 확장 외 <b>(1) Upstream 진출</b>, (2) 도시가스 및 산업가스 영역, (3) Power to Information 하 신규 기회로 초기 정의. Upstream 진출에 대한 Key Question과 초기 가설 수립 진행 중.",
 ['SWAN 3.0','Upstream','Key Question','가설'])
add('na','na2','2026-02-23','2/23~27','prog',"LNG V/C 확장 옵션 초기 검토: 미국·중동·호주 × Dry/Wet Gas, E&S 협업 포함 3개 관점",
 "지역(<b>미국, 중동, 호주</b>)과 유형(<b>Dry gas, Wet gas</b>)별로 (1) 투자 기회가 존재하는지, (2) 투자 매력도는 어떠한지(전략적 정합성, Risk Hedge 가능성, Financial Gain), (3) E&S 협업 포함 추진 용이성 관점에서 초기 검토 중.",
 ['미국','중동','호주','Dry Gas','Wet Gas','E&S','Risk Hedge'])
add('na','na2','2026-03-16','3/16~20','info',"SWAN 3.0 핵심과제(초기)에 Upstream 진출 기반 Gas to Power to AIDC 포함",
 "SWAN 3.0 지향점(초기)을 Global Net Zero Solution Provider for & by AI로, 핵심과제(초기)로 <b>Upstream 진출 기반 Gas to Power to AIDC 연결</b>, AIDC Utility Solution 확대, Net Zero Solution 사업 확장, 에탄사업 진출, AI Transformation을 정의 중.",
 ['SWAN 3.0','Upstream','Gas to Power','AIDC'])
add('na','na2','2026-03-23','3/23~27','info',"SWAN 3.0 추진과제로 '미국 NG/NGL 확보' 첫 명시 — Fuel flexibility 방향",
 "SWAN 3.0 지향점을 고객에게 경제적이고 친환경적인 에너지 솔루션을 안정적으로 공급하는 것으로, 방향성을 Electrification·글로벌 확장·Fuel flexibility 확보로 정리. 추진과제로 <b>미국 NG/NGL 확보</b>, 글로벌 발전 수요 개발, 에탄사업 개발, LNG 벙커링 사업 확대, 글로벌 Net-zero 사업 확대 등을 제시.",
 ['SWAN 3.0','미국 NG/NGL','Fuel flexibility','글로벌 확장'])
add('na','na2','2026-03-30','3/30~4/3','prog',"북미 NG/NGL Play를 SWAN 3.0 우선순위 과제로 설정 — 핵심질문·초기 가설 구체화 중",
 "SWAN 3.0 지향점·추진방향성 구체화와 함께 <b>북미 NG/NGL Play</b>와 하와이 LPG 발전 사업을 우선순위로 검토. 북미 NG/NGL Play는 핵심 질문 및 초기 가설을 구체화 중.",
 ['북미 NG/NGL Play','SWAN 3.0','우선순위','가설'])
add('na','na2','2026-04-06','4/6~10','prog',"미국 NG/NGL 확보 가설 Why/What/How 구체화 — FOB 물량 전환 Optionality",
 "Why(미국 NG/NGL 확보의 전략적 의미), What(Molecule별 사업모델), How(필요 자산/계약 및 추진옵션) 관점에서 가설과 프로젝트 추진계획 구체화 중. 미국 NG/NGL 확보 시 추가로 확보 가능한 <b>Optionality</b> 기회도 구체화 중 (예: 미국 내수가격 또는 유럽 Spot 가격 Spike 시 국내 FOB 물량 전환을 통한 기회 Capture).",
 ['Why/What/How','Molecule','Optionality','FOB','Spot Spike'])
add('na','na2','2026-04-13','4/13~17','prog',"북미 Upstream 투자 사례·INEOS/EPD 계약구조 분석 — 차주 CEO 보고 준비",
 "북미 NG/NGL Value Chain 확장 검토를 Why/What/How 측면에서 가설 정리 중. 사업모델 가설 수립을 위해 <b>북미 주요 Upstream 투자 사례</b>와 <b>INEOS·EPD 등 주요 NGL Player의 계약구조 및 소유권 이전 단계</b> 분석 진행. 사업모델 가설과 프로젝트 추진방안을 정리해 차주 본부 위클리에서 사장님 보고 예정.",
 ['Upstream 투자 사례','INEOS','EPD','계약구조','NGL Player'])
add('na','na2','2026-04-23','4/20~24','mile',"북미 NG/NGL 확보 필요성·사업모델 가설 CEO 보고 완료 (4/23) → 프로젝트 본격 추진 결정",
 "SWAN 3.0의 핵심과제인 북미 NG/NGL 확보 필요성 및 사업모델 가설(Why/What/How)과 추진방안에 대한 사장님 보고를 완료하고 <b>프로젝트를 본격 추진하기로 결정</b>, 과제 착수.",
 ['CEO 보고','4/23','프로젝트 착수','북미 Upstream'])

# ───────── R-PJT(E&S 공동) 출범 · NGL PJT(BCG) 준비 ─────────
add('na','na1','2026-05-11','5/11~15','mile',"R-TF 출범: 차주부터 E&S와 공동으로 그룹 LNG 프로젝트 진행 — 자체/공동 트랙 분리 설계",
 "그동안 자체 검토해 온 북미 Upstream 전략을, 차주부터 <b>R-TF를 통해 SK E&S와 공동으로 그룹 LNG 프로젝트</b>로 진행. (1) 당사 자체 추진 영역과 (2) E&S 공동 추진 영역을 설계해 양 트랙 간 중복을 최소화하고 시너지가 발현되도록 운영 방침. R-TF는 차주 컨설팅사 선정을 위한 프로젝트 과업 범위 설정 및 Key Question 구체화 작업 진행 계획.",
 ['R-TF','SK E&S','그룹 LNG 프로젝트','컨설팅사 선정','Key Question'])
add('na','na1','2026-05-25','5/25~29','prog',"R-PJT 2개 모듈(Market Dynamics·BM/실행체계) 운영, 일본 Utility 전략 검토",
 "E&S와 공동 추진 중인 R-PJT는 <b>Market Dynamics 분석</b>과 <b>BM/실행체계 구축</b>의 2개 모듈로 운영 중. 차주에는 일본 주요 Utility 및 상사의 전략 방향성과 시사점을 우선 검토 예정.",
 ['R-PJT','Market Dynamics','BM','일본 Utility','상사'])
add('na','na2','2026-05-25','5/25~29','plan',"북미 NGL PJT: BCG와 논의 마무리 후 6/8 주 착수 예정",
 "북미 NGL PJT는 차주 BCG와 논의를 마무리하여 <b>6월 8일 주 프로젝트 착수</b> 예정.",
 ['NGL PJT','BCG','착수'])
add('na','na1','2026-06-04','6/1~5','mile',"R-PJT Kick-off 완료 (6/4): 핵심 질문 공감대, Why/What 중심 Work Plan",
 "E&S와 공동 추진하는 R-PJT <b>6/4 Kick-off 완료</b>. 프로젝트 핵심 질문에 대한 공감대를 형성했고, Tight한 일정을 고려해 Why/What 중심의 Priority 기반 Work Plan 수립 예정. 차주 맥킨지의 당사 Trading BM 이해도 제고를 위한 경영진 인터뷰 Session을 추진하고, SK가스가 생각하는 E&S와의 협력 기회를 정리해 공유 예정.",
 ['R-PJT','Kick-off','6/4','맥킨지','경영진 인터뷰','E&S'])
add('na','na2','2026-06-01','6/1~5','plan',"NGL PJT 공식 착수는 3~4주 후로 — BCG와 논의 지속하며 북미 NG/NGL Play 입장 구체화",
 "NGL PJT는 3~4주 후 공식 착수 예정이나, 그 전까지 BCG와 논의를 지속하면서 R-PJT 추진 과정에서 필요한 당사 <b>북미 NG/NGL Play에 대한 입장</b>을 구체화.",
 ['NGL PJT','BCG','R-PJT 연계'])
add('na','na1','2026-06-15','6/15~19','info',"맥킨지 LNG Market View: 유동성 확대, 선도사는 Upstream·물량·트레이딩 병행",
 "맥킨지로부터 LNG Market View 및 선도사 벤치마킹 결과 공유. LNG 시장이 장기계약 중심에서 점차 <b>유동성이 높은 시장</b>으로 변화하고 있어 트레이딩 역량과 포트폴리오 운영 능력의 중요성 확대. 글로벌 주요 Player들은 단순 다운스트림을 넘어 <b>Upstream 투자, 물량 확보, 트레이딩 사업 확대를 병행</b> 추진 중. 월요일 오전 사장님 보고 예정.",
 ['맥킨지','LNG Market View','벤치마킹','유동성','Upstream 투자'])
add('na','na2','2026-06-15','6/15~19','plan',"북미 전략 과제 10주 일정 확정 — 범위·핵심질문·산출물 Kick-off 보고 예정",
 "북미 전략 과제는 <b>10주 일정</b>으로 추진 예정이며, 월요일 오후 사장님께 프로젝트 범위, 핵심질문 및 주요 산출물에 대한 Kick-off 보고 진행 계획.",
 ['북미 전략','10주','Kick-off 보고'])
add('na','na3','2026-06-15','6/15~19','info',"Twin Eagle 지분인수 검토 요청 — 가스전 없이 연 EBITDA 2억달러 Midstream 모델",
 "Twin Eagle社 지분인수 검토 요청이 있어 초기 미팅 진행. 2010년 휴스턴 설립 NG Midstream 전문기업으로, <b>가스전 투자 없이 Offtake 계약·Pipeline 계약·수요계약 기반으로 연간 EBITDA 2억 달러</b> 창출. 주요 수익모델은 ① 수요처 Back-to-back 공급 고정 마진, ② 보유 배관계약 활용 지역 간 Hub 가격 Spread 마진, ③ Storage 활용 Time Spread 마진. 당사 북미 NG Play 사업모델 수립에 미국 내수 트레이딩 사업모델 이해가 필수적인 만큼 실사 추진 검토 (별도 보고 예정).",
 ['Twin Eagle','Midstream','EBITDA 2억달러','Hub Spread','Time Spread','실사'])
add('na','na2','2026-06-22','6/22~26','prog',"CEO 피드백: 수익모델·핵심고객·핵심역량 중심 Framework 보완, 12주 재정비",
 "사장님 피드백에 따라 북미 NG/NGL 사업모델을 단순 Value Chain 관점이 아닌 <b>수익모델, 핵심 고객, 핵심 역량 등을 포함한 사업모델 중심</b>으로 Framework 보완 중. 이를 위해 <b>Antero, Shell, Expand Energy, ONEOK</b> 등 주요 사업자의 Midstream 계약 구조, Physical Trading 수익모델, Value Chain별 핵심 경쟁력 분석. 프로젝트 추진계획도 차주부터 12주 일정으로 재정비 중이며, 차주 보완 내용 기반으로 Kick-off 재보고 예정.",
 ['사업모델 Framework','Antero','Shell','Expand Energy','ONEOK','12주'])
add('na','na3','2026-06-22','6/22~26','risk',"T사 실사: 기존 Bidder 인수제안 예정 → 대주주 Five Point Infra 협의 따라 결정",
 "실사 진행 예정이던 미국 Midstream 업체 T사는 기존 Bidder가 차주 인수제안(Offer)을 제출할 예정이라, 해당 결과와 대주주(<b>Five Point Infra</b>)와의 협의 상황에 따라 당사의 실사 참여 가능 여부가 결정될 전망. 진행상황 모니터링하며 대응 방향 조율.",
 ['Twin Eagle','T사','Bidder','Five Point Infra','실사'])

# ───────── H2: 사업모델 분석 본격화 · Twin Eagle IOI/실사 · R-PJT 중간보고 ─────────
add('na','na2','2026-06-29','6/29~7/3','prog',"프로젝트 구체화: 선도사 가치창출 메커니즘 분석 + GE 1GW 에탄 혼소 Optionality",
 "사장님 보고 결과, 북미 시장 선도 사업자의 가치 창출 메커니즘과 사업모델을 분석해 당사에 적합한 사업모델 옵션을 도출하고 사업 타당성과 최적 진입 시점을 검토하는 방향으로 프로젝트 구체화. 차주부터 NG 사업의 주요 사업모델·가치창출 메커니즘 분석과 NGL 사업의 핵심 사업모델·경쟁력 검토 본격화. 사장님 피드백을 반영해 당사만의 Unique한 사업모델 개발을 위해 <b>GE의 1GW급 에탄 혼소 발전 사례</b> 등 NG와 에탄을 연계한 Optionality 확보 방안도 종합 검토.",
 ['가치창출 메커니즘','사업모델 옵션','진입 시점','GE','에탄 혼소','NG-에탄 Optionality'])
add('na','na3','2026-06-29','6/29~7/3','done',"Midstream 인수 Non-binding IOI Lazard 제출 — 차주 Data Room 실사 예정",
 "미국 Midstream 업체 인수를 위한 <b>Non-binding IOI(Indication of Interest, 비구속적 인수의향서)를 Sell-side Advisory인 Lazard에 제출</b>. 차주부터 Data Room 접근 권한을 확보해 실사 진행 예상. 사업모델의 지속가능성, 핵심 성공요인 및 당사와의 전략적 시너지 등 정성적 요소를 중심으로 우선 검증 계획.",
 ['IOI','Lazard','Data Room','Twin Eagle','실사'])
add('na','na2','2026-07-06','7/6~7/10','info',"NG Marketer 모델: Term+Spot 결합, Regional Spread 수익화가 핵심",
 "NG Marketer 사업모델 분석 결과, <b>안정적인 Term 고객 기반에 Spot 고객을 결합해 Scale과 Optionality를 동시에 확보</b>하고, 지역별 수급 특성에 맞는 소싱·판매 전략으로 <b>Regional Spread를 수익화</b>하는 것이 핵심 사업모델임을 확인. NGL 사업모델 초기 분석 결과, NG와 달리 Midstream 사업자의 역할이 크고 Value Chain별 사업모델이 비교적 단순한 구조. 차주 당사 휴스턴 오피스 전문가 네트워크를 활용해 미국 주요 권역별 NGL Value Chain과 실제 Trading 수익 창출 메커니즘 인터뷰 진행, NG·NGL 사업모델의 공통점·차이점과 구조적 차이의 배경을 종합 분석해 보고 예정.",
 ['NG Marketer','Term','Spot','Regional Spread','NGL Midstream','휴스턴 오피스'])
add('na','na3','2026-07-06','7/6~7/10','prog',"T사, 당사 실사 참여 최종 승인 — NDA 체결 진행, 차주 Data Room 접속해 본격 실사",
 "미국 NG Midstream 업체 T사 측에서 당사의 실사 참여를 최종 승인함에 따라 NDA 체결 진행 중. 차주부터 Data Room에 접속해 사업모델의 지속가능성과 핵심 경쟁력을 중심으로 본격 실사 추진 계획.",
 ['Twin Eagle','T사','NDA','Data Room','실사 승인'])
add('na','na1','2026-07-10','7/6~7/10','mile',"R-PJT 경영진 Progress Update (7/10): 선제적 Long 확보 선순환 구조 공감",
 "LNG 시장은 중장기 성장이 예상되나 시장 유동성 확대와 지정학·수급 불확실성 상시화로 향후 경쟁력은 <b>Optionality 확보 여부</b>가 좌우한다고 보고. Team SK의 성장 방식도 확정 수요 기반으로 Long을 매칭하는 Point-to-Point 방식에서, <b>관리 가능한 수준의 Long을 선제 확보하고 이를 기반으로 신규 수요와 글로벌 Outlet을 확대하는 선순환 구조</b>로 전환이 필요하다는 방향성에 경영진 공감대 형성. 7월 말 중간보고 전까지 Team SK 사업모델을 실행 가능한 수준으로 구체화하고, Upstream·Midstream·Downstream별 공동 추진 과제와 양사 단독 과제를 구분해 역할 분담 명확화 예정. JERA·미쓰비시의 성장 Path(선제적 Long 확보의 전략적 배경, JV·전략적 제휴 활용 방식)를 심층 벤치마킹해 Team SK 실행 전략에 반영 계획.",
 ['R-PJT','Progress Update','Team SK','선제적 Long','Point-to-Point','JERA','미쓰비시'])
add('na','na2','2026-07-13','7/13~7/17','prog',"미국 NG/NGL 시장·사업자 In-depth Study — 차주 가설적 사업모델 CEO 보고",
 "당사 북미 NG/NGL 사업전략 수립을 위해 미국 NG/NGL 시장 Dynamics, Value Chain 및 주요 사업자별 사업모델 분석 중. 차주 금요일 사장님 보고 시 미국 시장 이해를 토대로 당사의 가설적 사업모델에 대해 의미 있는 논의가 이뤄지도록 시장 In-depth Study 가속.",
 ['시장 Dynamics','Value Chain','사업모델','In-depth Study'])
add('na','na3','2026-07-17','7/13~7/17','done',"T사 NDA 체결·Data Room Access 확보 (7/17) — Standalone 경쟁력 실사 착수",
 "미국 NG Midstream 업체 T사와 <b>NDA 체결 완료, 7/17(금) Data Room Access 확보</b>. 차주부터 본격 실사를 통해 미국 NG 마케터 사업모델의 Standalone 경쟁력과 당사와의 전략적 정합성 중점 검토 계획.",
 ['Twin Eagle','T사','NDA','Data Room','7/17'])
add('na','na1','2026-07-13','7/13~7/17','prog',"R-PJT 7/30 중간보고 준비: Wet vs Dry Gas·내수 마케팅, Trading 시너지 검증",
 "7/30 경영진 중간보고 준비 중, Team SK 협업 가능 영역을 북미 Upstream과 Trading/Optimization 중심으로 E&S와 협의. <b>북미 Upstream</b>은 당사 NGL 투자의사 결정과 연계해 Dry Gas 대비 Wet Gas 투자 필요성, Upstream 투자 이후 북미 NG 내수 마케팅 진출 타당성 검증. <b>Trading/Optimization</b>은 기존 Rigid 계약 물량과 신규 Flexible 물량을 구분해 양사 물량 통합 시 시너지와 이를 위해 해소해야 할 제약조건 도출.",
 ['R-PJT','중간보고','7/30','Wet Gas','Dry Gas','Trading/Optimization','물량 통합'])
add('na','na2','2026-07-20','7/20~7/24','info',"내수-수출 Optionality 열쇠는 수출터미널 Tolling Capacity — 신규 확보 제한적",
 "북미 NG/NGL 시장 구조와 가치창출 메커니즘, 핵심 요구역량 및 당사 시사점을 정리 중(차주 수요일 사장님 보고 예정). 북미 내수와 수출시장 간 Optionality 확보를 위해서는 <b>NG와 Propane 모두 수출터미널 Tolling Capacity 확보가 중요</b>하나, 현재 시장에서 신규로 확보 가능한 Tolling 계약이 제한적인 만큼 기존 사업자들의 Capacity 확보 방식과 계약 체결 선결요건을 확인하는 작업 병행.",
 ['Tolling Capacity','수출터미널','내수-수출 Optionality','Propane','선결요건'])
add('na','na3','2026-07-20','7/20~7/24','done',"T사, 기존 잠재 인수자와 거래 완료 통보 → 실사·인수 검토 종료",
 "실사 추진 예정이던 미국 NG Midstream 업체 T사가 기존에 인수 협의를 진행해 온 잠재 인수자 중 한 곳과 <b>거래를 완료했다고 통보</b>. 이에 T사에 대한 실사 및 인수 검토를 종료했으며, 실사 준비 과정에서 확보한 시장 Insight는 북미 NG/NGL 사업전략 수립에 활용 계획.",
 ['Twin Eagle','T사','인수 검토 종료','거래 완료'])
add('na','na2','2026-07-27','7/27~7/31','prog',"핵심 검증 항목 확정: 원가경쟁력·Natural Hedge·내수-수출 Optionality",
 "사장님 보고 및 논의를 바탕으로 <b>원가경쟁력 확보 / Natural Hedge 구축 / 내수-수출 Optionality 확보</b> 등 당사 북미 사업모델 구체화에 필요한 핵심 검증 항목에 집중. NG 사업은 SK E&S의 북미 사업모델 이해를 바탕으로 양사 협력을 통한 사업 경쟁력 확보 방안을, NGL 사업은 당사가 보유한 물량 경쟁력을 기반으로 <b>EPD 등 Midstream 업체와의 협상</b>을 통해 당사에 유리한 계약조건과 사업구조를 확보할 수 있는지 중점 검토 예정.",
 ['원가경쟁력','Natural Hedge','내수-수출 Optionality','SK E&S','EPD','Midstream'])
add('na','na2','2026-08-03','8/3~8/7','prog',"EPD 미팅 전 NGL 모델 구체화: 프로판 Arbitrage·Switching, 에탄 Upstream 착수",
 "8/20 EPD 경영진 미팅 전까지 북미 NGL 사업모델 구체화 목표. <b>프로판</b>은 과거 실적 및 장기 전망 기반으로 미국 내수-수출 간 Arbitrage 수준과 Switching Optionality 사업성 검증 중, <b>에탄</b>은 원가 경쟁력 확보 관점에서 북미 Upstream 투자 필요성·타당성 검토 착수. <b>NG</b>는 E&S의 내수-수출 Switching Operation을 분석해 내수 전환 시 주요 수익·비용 Lever 구체화(Molecule 판매 외 전력 판매 추가 수익기회, 유휴 선박·Tolling 비용 등), 에탄 연계 시 Switching Optionality 추가 확대 가능 여부도 검토 예정.",
 ['프로판','Arbitrage','Switching Optionality','에탄 Upstream','E&S Switching Operation','EPD'])
add('na','na1','2026-08-03','8/3~8/7','prog',"R-PJT Team SK 협업 영역 5개 도출: Wet Gas·AIDC·Switching+에탄·선박·발전",
 "E&S와 진행 중인 R-PJT는 북미 Upstream 투자부터 Outlet 구축까지 V/C 전반의 Optionality 창출 기회와 Team SK 차원 협업 영역 구체화. 주요 영역으로 <b>① Wet Gas 투자의 Dry Gas 대비 경제성, ② 미국 AIDC 발전향 NG/에탄 Optionality, ③ 내수-수출 Switching에 에탄을 연계한 추가 수익기회, ④ 선박 공동 활용, ⑤ 국내·동남아 Multi-Fuel 발전사업</b> 도출. 차주 각 영역의 실현 가능성과 기대 Impact를 정량 검증해 양사 협업모델과 우선 추진과제 구체화 예정.",
 ['R-PJT','Team SK','Wet Gas','AIDC','Switching','선박 공동활용','Multi-Fuel 발전'])
add('na','na2','2026-08-10','8/10~8/14','info',"3대 목표·초기 BM: NG E&P 투자, NGL 에탄 Off-take Lever, 프로판은 제한적",
 "북미 NG/NGL 사업 진출 목표를 <b>① 구조적 원가경쟁력 확보, ② Natural Hedge 구축, ③ 내수-수출 Optionality 등 Upside 확보</b>의 3가지로 정리하고 초기 BM 구체화. NG는 구조적 원가경쟁력 확보를 위해 E&P 투자가 필요하다는 판단 하에 투자 효과 정량화 및 E&S 공동 추진을 통한 초기 사업 Risk 완화 방안 검토. NGL은 <b>Rich Gas E&P 투자 시 에탄 Off-take 역량을 협상 Lever로 활용해 E&P 인수 조건 및 Fractionation Tolling Fee를 개선</b>하는 것이 핵심이라는 잠정 결론 도출, Rationale 검증 중. 프로판은 수출-내수 전환 비용과 시황 Spread 기반으로 Optionality 발생 빈도·실현 가능성을 검토한 결과 <b>실제 실행 가능한 기회는 제한적</b>으로 판단.",
 ['3대 목표','원가경쟁력','Natural Hedge','E&P 투자','Rich Gas','에탄 Off-take','Fractionation Tolling Fee','프로판'])
add('na','na3','2026-08-10','8/10~8/14','plan',"EPD 미팅(8/20) 준비: Rich Gas E&P 연계 Midstream 협력 — 8/19 CEO 보고",
 "8/20 EPD 경영진 미팅용 논의 자료 작성 중, 8/19 사장님 보고 예정. 미팅에서는 당사의 <b>Rich Gas E&P 투자와 연계한 NGL Midstream 협력 필요성</b>을 중심으로, Well 선정 단계부터 EPD와 협력해 양사 시너지를 극대화하는 방안 논의 계획. EPD의 에탄·프로판 수출터미널 증설 계획 및 물량 마케팅 현황 등 MI 관점의 사전 질의를 전달했으며, 회신 검토 후 경영진 차원 추가 논의 필요 사항은 미팅 Agenda에 반영.",
 ['EPD','경영진 미팅','8/20','Rich Gas E&P','Well 선정','수출터미널 증설','사전 질의'])
add('na','na1','2026-08-10','8/10~8/14','prog',"R-PJT 시너지 정량화 초안 공유 — E&S, 미국·호주 Upstream 소싱 가격 제공키로",
 "R-PJT에서 당사가 정량화한 E&S와의 협업 시너지 효과 초안을 공유했으며, E&S가 <b>미국·호주 Upstream 소싱 가격 및 구매조건</b> 등 추가 정보를 제공하기로 함. 차주 이를 바탕으로 시너지 정량화를 고도화하고, 검토 중인 NGL Upstream에 대한 당사 Stance를 반영해 E&S와의 협업 범위 및 우선 추진과제 구체화 예정 (이후 R-PJT 관련 Weekly 미보고).",
 ['R-PJT','시너지 정량화','E&S','Upstream 소싱 가격','호주'])

# ───────── Why Upstream 검증 · EPD 미팅 · Wet Gas BM · 11월 출장 ─────────
add('na','na4','2026-08-17','8/17~8/21','prog',"Why Upstream 검증: FOB 대비 원가경쟁력·가스전 고갈 Risk·Tolling Upside",
 "북미 프로젝트는 <b>Why Upstream 투자</b>에 대한 Rationale 검증에 집중. Upstream 투자 시 FOB 조달 대비 구조적 원가경쟁력 확보 가능 여부, 저원가 가스전 고갈에 따른 경쟁력 하락 Risk, 적정 매물 확보 가능성, 투자 이후 필요한 운영역량 점검. 에탄 사업을 전제로 Wet Gas에 투자할 경우에도 NG 관점에서 Dry Gas 대비 경쟁력 확보 가능 여부를 검증하고, Tolling 구조에서는 FOB 조달 대비 내수-수출 Switching 등으로 창출 가능한 추가 Upside를 정량화 중.",
 ['Why Upstream','FOB','가스전 고갈','운영역량','Wet Gas','Dry Gas','Tolling Upside'])
add('na','na3','2026-08-20','8/17~8/21','mile',"EPD 경영진 미팅 (8/20): Non-op 적합, Eagle Ford 유망, EOG·Devon 추천",
 "8/20 EPD 경영진 미팅을 통해 당사의 북미 NG/NGL 사업전략 구체화 및 실행을 위한 협력방안 논의. EPD는 Upstream 진출 방식으로 <b>E&P사의 Non-op 지분 참여</b>가 적합하며, Wet Gas 확보 측면에서는 <b>Eagle Ford가 가장 유망</b>하다는 의견과 함께 <b>EOG, Devon</b> 등을 유력 파트너로 추천. 향후 북미 NG/NGL 전략을 실행으로 전환하는 과정에서 EPD의 Network과 Midstream Infra 적극 활용 계획 (미팅은 김용범 본부장이 Arrange).",
 ['EPD','8/20','Non-op','Eagle Ford','EOG','Devon','Midstream Infra'])
add('na','na4','2026-09-01','8/31~9/4','prog',"9/1 CEO 보고 후 BCG 심화: Why 북미·Upstream Valuation·HH Hedge 효과",
 "9/1(화) 사장님 보고 이후 북미 NG/NGL 전략을 선명하게 하기 위해 BCG와 검토 심화. <b>Why 북미</b>는 원가경쟁력뿐 아니라 리스크와 Feasibility를 함께 고려해 Rationale 보강, 북미 Upstream 투자 경제성 및 핵심 Valuation 지표와 재무모델 구체화. <b>HH 가격 변동에 따른 Upstream 수익과 당사 LNG Short Position 간 Hedge 효과</b>도 분석 중. 왜 Equity Gas가 필요하고 왜 북미 Upstream이어야 하는지 명확히 정리해 9/14일주 보고 예정. 한편 INEOS와는 Terminal Fee 문의에 더해 당사의 북미 Wet Gas 투자부터 울산 수요까지 연계한 전체 사업모델 논의 준비 중(에탄 과제 연계).",
 ['BCG','Why 북미','Valuation','재무모델','HH','Natural Hedge','Equity Gas','INEOS'])
add('na','na4','2026-09-07','9/7~9/11','prog',"Why Upstream 3축 정의·북미 vs 호주·동남아·중동 비교 — Stress Test로 분석 지연",
 "Why Upstream을 <b>수익 안정성, 도입 원가경쟁력, 유연성/Optionality</b>의 3가지 축으로 정의하고, 투자 리스크까지 포함해 북미와 호주·동남아·중동을 비교하며 Why 북미 논리 보강. 북미 내에서도 Wet/Dry Gas, 자산 Maturity, 지역·규모별로 당사의 Why를 충족하기 위한 조건을 구체화하고, Basin별 생산원가 등 핵심 조건을 충족하는 매물의 존재 여부와 투자 수익성 Stress Test 진행. 가스전 유형별 Valuation Model 적용 과정에서 당초 예상보다 분석에 시간이 소요되고 있으나, 추석 전 사장님 보고에 차질 없도록 일정 관리.",
 ['Why Upstream','수익 안정성','Optionality','호주','동남아','중동','Basin','Stress Test','Valuation Model'])
add('na','na4','2026-09-14','9/14~9/18','info',"초기 진입은 Non-operator 모델 — Wet Gas 복잡성 vs C2 Benefit 검토",
 "Why Upstream/Why US와 함께 미국 Upstream 투자 시 핵심 고려사항(사업진입 모델, Dry vs Wet Gas, Target 생산원가, 자산 Maturity) 입체 검토. 초기 진입은 운영경험 부재를 고려해 <b>Non-operator 모델이 적절</b>하다고 보고, 이 경우 Downside Risk를 어느 수준까지 낮출 수 있는지와 Operator 권한 부재로 포기해야 하는 Upside를 함께 분석. Wet Gas는 Dry Gas 대비 운영 복잡성이 높은 만큼 당사가 에탄 Short를 보유할 경우 추가 복잡성을 감수할 만큼 C2 확보의 경제적·전략적 Benefit이 충분한지 검토 중. 현실적으로 <b>Oil 함량은 낮고 C1/C2/C3가 원하는 비율로 구성된 이상적 자산은 제한적</b>이므로 Molecule Composition, 생산원가, USGC 연계성, Maturity, Oil Exposure 등 조건 간 우선순위 구체화. 차주 화요일 종합 보고 예정.",
 ['Non-operator','Wet Gas','C2','에탄 Short','Molecule Composition','USGC','Oil Exposure'])
add('na','na2','2026-10-05','10/5~10/9','plan',"10/1 CEO 피드백 4주 과제: 수출국 가격 메커니즘·Wet Gas BM·Roadmap",
 "10/1 사장님 보고 피드백을 반영해 (1) 카타르 등 주요 LNG 공급 국가의 가격 메커니즘 분석을 통해 미국 Upstream 진출 필요성 보강, (2) <b>Wet Gas 사업모델</b>을 중심으로 Non-op 투자에 따른 잠재 Risk 및 대응방안, Tolling 확보 필요성 구체화, (3) 3~5년 후 북미 NG/NGL 시장의 변화 길목 선점에 초점, (4) 성공적 시장 진출·안정적 운영에 필요한 역량·파트너십·계약구조·투자조건을 시점별 Roadmap으로 정리 예정. 향후 4주간 추진하며, <b>11월 중순 미국 Upstream 업체 미팅 전까지 북미 BM과 추진 방향 구체화</b>.",
 ['카타르','가격 메커니즘','Wet Gas BM','Non-op Risk','Tolling','Roadmap','11월 미팅'])
add('na','na2','2026-10-12','10/12~10/16','prog',"Wet Gas BM 집중: NG Tolling·NGL EPD 협업, Eagle Ford·Appalachia",
 "현재 <b>Wet Gas BM</b> 중심으로 집중 검토. NG는 Upstream에서 액화터미널까지의 물량 연계방식 및 Tolling 확보 필요성을, NGL은 EPD와의 협업구조 도출을 중심으로 구체화. 특히 <b>Eagle Ford와 Appalachia</b>를 대상으로 Wellhead 인근 Hub의 가격 Index 연동구조 및 변동성, 파이프라인·터미널 등 인프라 연계 가능성을 Bottom-up 방식으로 분석해 BM의 실현가능성과 경제성 검증. Wet Gas BM 초안 준비되는 대로 별도 보고 예정.",
 ['Wet Gas BM','액화터미널','Tolling','EPD','Eagle Ford','Appalachia','Hub Index'])
add('na','na4','2026-10-12','10/12~10/16','plan',"11월 출장 준비: 11/16 에너지부 장관·EOG·ConocoPhillips 미팅 (10/19 보고)",
 "<b>11/16 미국 에너지부 장관 미팅</b>과 미국 Upstream 업체 미팅 준비 중. 에너지부 장관 미팅은 미국산 LPG의 해외 신규 수요 창출을 위한 미 정부 최근 정책 동향(아프리카 주요국, 방글라데시와의 MOU 체결 등)을 분석하고 당사가 미국산 LPG 수출 확대에 기여할 수 있는 협력방안 중심으로 Agenda 구체화, 당사의 방글라데시·하와이 LPG 사업 개발에 대한 미 정부 지원 기반 마련 기회로 활용. <b>EOG와 ConocoPhillips</b> 미팅은 양사 최근 Upstream 사업전략·동향을 분석해 당사 Wet Gas BM과 연계한 Upstream 투자 및 NG/NGL 공급 협력 가능성 중심으로 Discussion Point·자료 준비. 10/19(월) 출장 준비현황 및 주요 Discussion Agenda 보고 예정.",
 ['11월 출장','에너지부 장관','11/16','EOG','ConocoPhillips','미국산 LPG','방글라데시','하와이'])
add('na','na2','2026-10-19','10/19~10/23','prog',"Wet Gas BM 검증: NG Virtual 연계 Hedge, NGL Y-grade 판매→FOB 에탄 구매",
 "NG는 수출터미널에서 원거리에 위치한 가스전도 <b>Virtual 연계</b>를 통해 HH Index 변동성 Hedge가 가능한지, 수출터미널 Tolling 확보 시 FOB 구매 대비 실질적으로 어느 정도 추가 수익기회를 창출할 수 있는지 검토. NGL은 EPD와의 협업을 전제로 <b>Y-grade 판매 후 수출터미널에서 FOB 에탄을 구매하는 방식</b>의 경제성과 가격·물량 연계구조, 양사 간 역할 분담 검증. Oil 생산을 수반하는 Wet Gas전도 Oil 가격변동 리스크를 Hedge하면서 투자 목적을 충족할 수 있는지 검토해 Upstream 투자 대상 범위 명확화 예정. 차주 목요일 Wet Gas BM 구체화 결과와 11월 출장 시 EOG·ConocoPhillips별 논의 Agenda·Talking Point 보고 예정. 한편 10/23 그룹 화학TF 보고에서 사장님 지시로 <b>북미 Wet Gas 투자에 따른 SKGC향 에탄 공급가격 인하·가격 변동성 축소 효과</b> 검증 과제 추가.",
 ['Wet Gas BM','Virtual 연계','HH Hedge','Tolling','Y-grade','FOB 에탄','EPD','Oil Hedge','SKGC 에탄'])
add('na','na2','2026-10-26','10/26~10/30','prog',"Wet Gas BM: Eagle Ford·Appalachia Non-op, 초과 C1은 공동투자로 해결",
 "투자 대상을 <b>NGL 함량이 높고 Oil 생산 비중이 낮은 Wet Gas 자산(Eagle Ford·Appalachia 우선)</b>으로 설정하고, <b>Non-op 지분 참여와 핵심 계약상 권리 확보</b>를 통해 투자·운영 리스크를 최소화하는 방향으로 구체화. 초과 C1(메탄) 물량은 한화 등 C1 Offtaker와의 공동투자로 해결하고, NGL은 Y-grade 판매 및 C2/C3 FOB 구매, NG는 Physical 연계를 우선하되 Virtual 연계 등 다양한 옵션을 열어두는 방향으로 BM 구체화. 관련 내용은 별도 논의 예정.",
 ['Wet Gas BM','Eagle Ford','Appalachia','Non-op','C1 Offtaker','한화','Y-grade','C2/C3 FOB'])
add('na','na4','2026-10-26','10/26~10/30','plan',"11월 출장 대상 EOG·Devon·ConocoPhillips별 협력 가능 영역 검토 중",
 "11월 미국 출장 시 미팅 예정인 주요 Upstream 업체(<b>EOG, Devon, ConocoPhillips</b>)별 협력 가능 영역을 Wet Gas BM과 연계해 검토 중 (출장 결과는 10/30까지 Weekly 미보고).",
 ['11월 출장','EOG','Devon','ConocoPhillips','Upstream 협력'])

ITEMS = I

COVERAGE = "30 / 언급 없는 주차: 12/8~12, 12/15~19, 12/22~26, 12/29~1/2, 1/5~9, 1/19~23, 2/2~6, 2/9~13, 3/2~6, 3/9~13, 4/27~5/1, 5/4~8, 5/18~22 (12/29~1/2는 SWAN 3.0 Optionality 예시로 '중동 수출 설비 등 Upstream 확보'만 언급, 북미 비해당)"
