# -*- coding: utf-8 -*-
# 전략본부 최적화실 과제 진척 데이터 (전략본부 Weekly '25.12/8 ~ '26.10/30 기준)
#  A) SKA/UPP 최적화 (id='ska')   B) 전사 포지션 & 미-이란 전쟁 대응 (id='pos')
# k: done(완료/확정) prog(진행) plan(계획/예정) risk(이슈/리스크) mile(마일스톤) info(정보/시사점)

CAT_A = dict(
  id='ska', icon='⚙️', name='SKA/UPP 최적화',
  sub='가동 경제성·의사결정 · 합병·구조개편(SKA/UPP) · Relocation·중동 Greenfield · 시장 전망(CMA·BCG)·손익 모델 · 프로필렌 판매 확대·H사 협력',
  what="SK가스의 자회사 <b>SKA</b>(SK어드밴스드, 울산 PDH 공장: 프로판을 원료로 프로필렌을 만드는 설비)와 그 아래 PP(폴리프로필렌) 공장 <b>UPP</b>를 전사 관점에서 어떻게 할 것인가를 정하는 일입니다. 크게 네 갈래로, ① 프로필렌–프로판 스프레드(제품가와 원료가의 차이)가 나쁠 때 <b>공장을 돌릴지 세울지</b>를 SK가스의 프로판 공급이익까지 합쳐 판단하는 가동 경제성, ② <b>SKG–SKA 합병</b>과 UPP 매각(PMC·LYB 등 이해관계자) 같은 구조개편, ③ 공장을 <b>중동으로 옮기는 Relocation</b>(AGIC·APC와 협상) 또는 Greenfield 검토, ④ 외부 전문기관(CMA·BCG)의 PDH/PP 시장 전망을 바탕으로 한 손익 모델입니다. 최적화실은 재무본부·SKA·Trading본부와 함께 분석하고 CEO·의장·이사회(특별위원회) 보고를 지원합니다.",
  tracks=[('ska1','가동 경제성·의사결정·공급 Index'),('ska2','합병·구조개편(SKA/UPP)'),('ska3','Relocation·중동 Greenfield'),('ska4','시장 전망(CMA·BCG)·손익 모델'),('ska5','프로필렌 판매 확대·H사 협력')],
  status=[
   ("risk","<b>'27년 SKA 사업은 경영계획상 약 △700억 손실 전망</b>(10/19~23). 프로필렌 가격 하락에 따른 PDH 공헌 손실과 FEI/CP 스프레드 확대에 따른 프로판 공급 손실이 겹쳐, <b>PDH 가동 유연성 확보</b>가 전사 손실 방어의 핵심 과제. '27년 가동 최적화 의사결정 기준(전사 통합 경제성·프로필렌 Term 대응·설비 안정성)과 S/D Timeline·운영 Process를 정리해 11월 초 행복경영캔미팅에서 논의 예정."),
   ("prog","SKA向 프로판 <b>공급 Index를 CP에서 FEI로 변경</b>(이체가 최적안)하는 방안을 SKA·Trading본부와 논의 중: 적정 FEI 마진·반영 시기, 법무실(H사 공급구조 일치·Compliance), 세무팀(이월결손금 공제 조건) 병행 검토. FEI/MOPJ 상대가 기반 구조는 과거 10개년으로 분석 기간을 넓혀 검증 후 보고 예정(9월)."),
   ("mile","<b>SKA 합병</b>: 8/11 3차 특별위원회에서 전략·경제적 타당성, 법률·재무 리스크, 거래 공정성을 사외이사와 논의, <b>8/20 4차 특별위원회에서 합병 시점·방식(소규모 vs 일반합병) 의결 예정</b>이었음 (의결 결과 자체는 Weekly 미보고). 9월부터는 '합병 후 PDH 유연 가동'을 전제로 Pricing·Sourcing·운영 과제를 추진 중."),
   ("prog","<b>UPP End Image</b> = PP 사업에서 Exit하되 매각을 통해 제3자가 UPP를 존속 운영, Reputation Risk 최소화. PMC·LYB·채권단·산업부 등 이해관계자별 대응 원칙을 8/23 경영진 논의 예정이었고, PMC 주도 구조개편을 촉구하면서 Plan B도 준비 (8월 이후 UPP 진척은 Weekly 미보고). 6월에는 UPP 연체채권·운영자금 부족으로 하반기 파산 가능성이 거론됐음."),
   ("info","<b>중동 Relocation</b>: 3월 Risk Exposure 관점 최적안으로 결론 → 4월 AGIC와 Term Sheet 협상(4월 내 지분매입 목표) → 4/29 4개 옵션 보고 이후 PMC/UPP 구조개편 중심으로 무게가 옮겨가며, Relocation은 'UPP 운영 유지 시' Plan B 시나리오의 하나로 남음 (6월 이후 미보고)."),
   ("info","<b>시장 전망</b>(CMA, 7/24 경영층 보고): 프로필렌은 '28년 전후 저점 후 점진 회복, PP는 중국 증설로 '35년 이후에야 개선. 신규 과제로 <b>H사 PDH '27년 가동 중단–SKA 프로필렌 공급 연계</b> Win-Win 모델(프로판 처분이익 Profit Sharing)을 10월부터 검토 중."),
  ])

CAT_B = dict(
  id='pos', icon='🛡️', name='전사 포지션 & 미-이란 전쟁 대응',
  sub='통합 포지션 Dashboard·Index · 미-이란 전쟁 시나리오·Action Plan · Hedge 구조(Proxy Hedge·JKM Position) · 전사 최적화 협의체·기타 요청과제',
  what="SK가스는 LPG·LNG를 사고파는 여러 본부(Eco Energy, Trading, G&P)가 각자 <b>가격 지수(Index)에 노출된 물량(포지션)</b>을 갖고 있습니다. 한 본부는 JKM(LNG 현물지수)을 팔고 다른 본부는 사는 식으로 서로 반대인 경우도 있어, 회사 전체로 모아 보면 위험을 줄이거나(Natural Hedge) 기회를 키울 수 있습니다. 이 과제는 ① 전사 <b>LPG·LNG 통합 포지션 Map/Dashboard</b>(Digital Cockpit)를 만들어 경영진이 한눈에 보게 하고, ② '26.2월 말 발발한 <b>미국–이란 전쟁</b>으로 유가·LPG(FEI·CP·MB)·LNG(JKM) 가격이 급변하자 종전 시점별 시나리오와 본부별 Action Plan을 세워 대응하며, ③ 프로판 가격 위험을 납사(MOPJ) 선물로 막는 <b>Proxy Hedge</b> 등 Hedge 구조를 설계하고, ④ 12월 신설 당시 각 본부가 요청한 '5개 최적화 필요 업무'와 전사 최적화 협의체를 운영하는 일입니다.",
  tracks=[('pos1','통합 포지션 Dashboard·Index'),('pos2','미-이란 전쟁 시나리오·Action Plan'),('pos3','Hedge 구조(Proxy Hedge·JKM Position)'),('pos4','전사 최적화 협의체·기타 요청과제')],
  status=[
   ("done","<b>통합 포지션 Dashboard</b>: '26~'28년 3개년 EE·G&P LPG·LNG Physical·Paper 포지션을 한 판으로 정리하고 ODIN 시스템·MI 레터와 연계한 <b>Claude AI 기반 대시보드</b>를 구축, CEO 피드백 반영 업데이트(10/5~9). CEO/전사/EE/G&P에 더해 SKA/GPS 대시보드 추가 구축 중이며, AX실(MI 데이터 연계 자동화)·재무실(재무여력 분석 반영)과 협의해 Digital Cockpit으로 고도화."),
   ("prog","<b>미–이란 전쟁 대응</b>: 2/21~22 발발 → 전사 Daily 시황 점검 → 종전 시점(4월/7월/12월)별 Action 메뉴판(4월) → 5월 변동성 안정화로 모니터링 전환 → 6월 재격화 후 주 2회 시황 대응 협의체 운영. 10월에는 <b>전쟁 전후 의사결정 Look-back</b>(즉시 대응 성과 vs 장기화에 따른 손익 악화)과 종결 이후 시나리오를 행캔 Index 전망·'27년 경영계획과 맞춰 정리 중 (10/19 이후 미보고)."),
   ("done","<b>프로필렌 Proxy Hedge(MOPJ–MB)</b>: 9/2 유가 급등으로 Target Spread(역사적 상위 5%) 도달 → SKA 12월 생산계획의 <b>25%(약 7천톤) 포지션 진입 완료</b>. 10월 말 원가(10월 MB)가 Price-out되면 판가(11월 MOPJ)만 남는 '절대가 Hedge' 구조가 되고, 최근 프로필렌 가격은 FEI가 주도해 MOPJ의 안정화 효과가 제한적이라는 판단으로 <b>포지션 정리 방침</b>(10/19~23)."),
   ("info","<b>JKM Position Natural Hedge</b>(1월): EE(JKM Sell)·G&P(JKM Buy)의 월별 Matching 물량 차이(6월 EE 0.6만톤 vs G&P 6.7만톤)로 효과는 작으나 EE–G&P 간 Swap 원칙·내부 Process 수립, 이후 JKM/HH 상승 시황에서 본부별 개별 헤지. 하반기 JKM 급등 가능성에 대비해 EE JKM Sell Position과 G&P Optionality 실행을 전사 관점 모니터링(7월)."),
   ("info","<b>12월 '5개 최적화 요청 업무'</b>(북미 MB 가격 Dynamics, EE 고속도로 충전소 입찰 수익배분, 평택 부두 준설, MU Loss-cut, 한화 연료 전환) + UGPS 연료 최적화 중 평택 준설은 '26.4월 단독 준설 착공 방향 합의(12/22). 그 외 개별 과제 결과는 Weekly 미보고. 9월에는 울산 프로판 공급량 확대에 따른 인프라·선복·Optionality 종합 검토 필요성이 새로 제기됨."),
  ])

ITEMS_A = []
ITEMS_B = []
def add(c,t,d,w,k,title,body,tags):
    (ITEMS_A if c=='ska' else ITEMS_B).append(dict(c=c,t=t,d=d,w=w,k=k,title=title,body=body,tags=tags))

# ═══════════════════════════ A. SKA/UPP 최적화 ═══════════════════════════

add('ska','ska1','2025-12-29','12/29~1/2','plan',"최적화팀 최우선 과제로 SKA 의사결정 선정: 지속 가동·UPP 공급 여부 1월 내 결정 필요",
 "전략본부 워크샵(12/26) 후속으로 최적화팀 업무·우선순위를 정리, <b>SKA 관련 주요 의사결정</b>을 최우선 과제로 선정. 구체적으로 <b>SKA 지속 가동 여부와 UPP(PP 공장) 공급 여부</b>를 재무본부와 함께 1월 내 의사결정해야 하는 상황.",
 ['SKA','UPP','지속 가동','재무본부','우선순위'])

add('ska','ska1','2026-01-05','1/5~9','prog',"SKA S/D(가동 중단) 검토: 4월 S/D 시 EE·Trading 공급·처분 손익 변화 분석",
 "SKA S/D 의사결정 요소는 SKA 공헌이익, UPP/효성 계약관계, 재무적 Impact, SKG 전사 손익이며 최적화팀은 <b>SKG 전사 손익</b>을 담당. '26년 4월 SKA S/D 시 EE/Trading 본부의 프로판 공급 손익 변화와 Trading 물량 처분 손익 변화를 검토, 차주 수요일 재무본부·SKA와 통합 손익 검토 결과 논의 예정.",
 ['SKA','S/D','Shutdown','전사 손익','프로판 처분'])

add('ska','ska1','2026-01-12','1/12~16','prog',"SKA 가동 여부 전사 통합 경제성 검토 → 프로필렌–FEI 스프레드 기반 판단 로직 정교화",
 "SKA 가동 여부에 대해 전사 통합 관점 경제성 검토를 수행하고, <b>프로필렌–FEI 스프레드</b>(제품가 – LPG 원료가) 기반 판단 로직을 정교화해 차주 CEO 보고 예정.",
 ['SKA','프로필렌','FEI','스프레드','판단 로직','CEO 보고'])

add('ska','ska1','2026-01-19','1/19~23','done',"SKA 가동 판단 로직 정교화 완료 + Value Driver(전력비·H사/UPP·그룹 3사) 구체화",
 "[SKA Value-up] 전사 통합 경제성과 프로필렌-FEI 스프레드 시황을 종합한 <b>SKA 가동 여부 판단 로직 정교화 완료</b>(1/29 전사 최적화 회의 공유 예정). 경제성 개선 Value Driver로 전력비/고정비 절감, H사/UPP 협력, 그룹 화학 3사 협력을 구체화하고 SKG/SKA 통합 손익개선 기회 발굴 중. <b>2/5 그룹 화학 3사(SKG/SKGC/SKC) 통합 Operation 협업</b> 논의 예정.",
 ['SKA Value-up','판단 로직','전력비','H사','그룹 화학 3사','SKGC','SKC'])

add('ska','ska1','2026-01-26','1/26~30','info',"H사 통합 결렬 시 시나리오 비교: 운영 최적화 '미추진'이 전사 기대이익 더 큼",
 "H사와의 통합 결렬 시 운영 최적화 추진/미추진 시나리오별 전사 통합 기대이익을 비교한 결과 <b>운영 최적화 미추진 시 이익이 더 큰 것</b>으로 도출 (H사 #2 PDH향 프로판 공급 기회 손실 vs 프로판 공급비 정상화 효과). 효성向 프로필렌 판가 적정성, 효성 S/D 시 울산권역 프로필렌 판가 상승, MB·FEI Mix 공급 마진 반영 시 결과 변동 여부는 추가 검토. SKA 지속가동 의사결정 지원을 1Q 주요 과제로 설정, SKA(동북아 프로필렌 Spread 개선 기회)·재무본부(Relocation Risk 방어)와 검토 지속.",
 ['H사','효성','프로판 공급비','MB·FEI Mix','Relocation','1Q 과제'])

add('ska','ska2','2026-02-02','2/2~6','plan',"SKA 구조개편 의사결정 지원을 '26년 최우선 과제로: 가동·판가·스프레드 통합 마스터플랜",
 "SKA Value-up 관련 구조개편, 가동 여부, 판가 구조 등 전사적 의사결정 이슈가 확대 → <b>'26년 전략적 중요성이 가장 큰 사안</b>으로 3월까지 SKA 의사결정 지원을 최우선 과제로 설정. 가동 경제성·판가 구조·중장기 스프레드 전망을 통합한 마스터플랜 기반으로 (1) 프로필렌/FEI 가동 경제성 로직으로 시황별 가동 여부 점검, (2) SKA·H사向 프로판 최적 판가 구조(공급비 정상화, MB·CP·FEI Mix) 전사 손익·이해관계자 분석, (3) 국내 가동 vs Relocation 비교를 위해 <b>BCG 프로필렌 스프레드 분석 Tool</b>로 중장기 PDH 스프레드 전망 재검토. 그룹 화학 3사(SKG·GC·PG) 운영 협력(2/5)도 Follow-up.",
 ['구조개편','마스터플랜','판가 구조','BCG','스프레드 Tool','Relocation','그룹 화학 3사'])

add('ska','ska1','2026-02-09','2/9~13','done',"PDH 프로판 판가 정상화 결정: 4월부터 공급비 $2/t→$20/t, MB/CP Mix 단계 협상",
 "전사 최적화 협의체 및 전략 Weekly를 통해 PDH용 프로판 판가 정상화 방안으로 <b>4월부터 공급비 $2/t→$20/t 인상</b>을 추진하고, MB/CP Mix는 고객 수용 가능 범위를 감안해 단계적으로 협상하기로 결정.",
 ['프로판 판가','공급비','$20/t','MB/CP Mix','PDH'])

add('ska','ska3','2026-02-09','2/9~13','plan',"Relocation vs 지속운영 비교 Framework 착수, 매각 Boundary Condition 설정",
 "SKA 구조개편의 핵심인 <b>Relocation과 지속운영안</b>을 비교 평가할 Framework를 만들고, 재무본부와 매각 Boundary Condition 설정 및 SKA 중장기 Spread Cold Eye Review 진행 예정.",
 ['Relocation','지속운영','Framework','Boundary Condition','Cold Eye Review'])

add('ska','ska2','2026-02-16','2/16~20','prog',"SKA 의사결정 Framework 초안 수립(2/21 CEO 피드백), 옵션별 경제성 정교화",
 "SKA Relocation vs 국내 지속운영 의사결정 Framework 초안 수립, 2/21 CEO 논의 피드백 반영해 보완 예정. 재무본부/SKA와 <b>Relocation 비용, SKA-R 지분 기대수익, SKG-SKA 합병 시 경제성, 동북아 프로필렌 수급·Spread 전망</b>을 반영한 옵션별 경제성 정교화와 함께 이사회/주주 설득·Compliance 등 실행 쟁점을 사전 점검, 3월 중 의사결정 목표. 그룹 화학 3사 통합 Operation Synergy는 Inc. 요청 대응·울산 Site O/I 협업 과제로 정량화 추진.",
 ['Framework','SKA-R','SKG-SKA 합병','이사회','Compliance','Synergy','Inc.'])

add('ska','ska2','2026-02-23','2/23~27','done',"합병·중동 Relocation·지속운영·H사 합병 통합 의사결정 Framework 최고경영층 보고",
 "SKG-SKA 합병, 중동 Relocation, 지속운영, H사 합병을 포함한 <b>통합 의사결정 Framework 수립 → 최고경영층 보고 완료</b>. 옵션별 Net cash 관점 경제성·실행 가능성·Upside potential·Downside risk, 재무·세무 영향을 종합 분석 중이며 차주 1차 경제성 분석 결과 보고 후 3월 중 전사 최적화 관점 의사결정 예정.",
 ['통합 Framework','SKG-SKA 합병','중동 Relocation','H사 합병','Net cash'])

add('ska','ska2','2026-03-06','3/2~6','done',"3/6 CEO 1차 보고: Relocation·지속운영·H사 통합 옵션 Framework, 차주 의장 보고",
 "중동 Relocation, 국내 지속운영, H사 통합 옵션을 포함한 의사결정 Framework과 핵심 고려요소를 <b>3/6 사장 1차 보고</b>. 옵션별 재무적 영향과 주요 리스크를 보완해 차주 <b>의장 보고</b>를 통해 SKA 구조개편 경영층 의사결정 지원 예정.",
 ['CEO 보고','의장 보고','Relocation','H사 통합','구조개편'])

add('ska','ska1','2026-03-02','3/2~6','info',"4~6월 SKA 가동손익 vs MB 처분손익 비교 → 4월 MB 처분이 유리, 4월 SKA S/D 검토",
 "미국–이란 전쟁에 따른 시황 급변 속에서 4~6월 SKA 가동손익과 MB(북미 프로판) 처분손익을 비교 분석한 결과 <b>4월 MB 물량을 처분하는 편이 손익 개선 효과가 크다</b>는 시사점 도출 → 4월 SKA S/D 여부 검토 중. 급변 시황을 반영한 전사 의사결정 Framework를 TRM과 협업해 정리, 차주 경영층 논의 예정.",
 ['가동손익','MB 처분손익','S/D','TRM','미국-이란 전쟁'])

add('ska','ska3','2026-03-09','3/9~13','mile',"3개 옵션 통합 손익·CF 분석: Risk Exposure 관점 '중동 Relocation' 최적안 결론",
 "Relocation, 국내 지속운영, H사 통합 3개 옵션에 대해 재무본부와 통합 손익 및 Cash Flow 기반 경제성 분석을 공동 수행, <b>Risk Exposure 관점에서 중동 Relocation이 최적안</b>이라는 결론 도출. 향후 SKG–SKA 합병 및 Relocation 관련 주주·이사회 Communication 전략과 경영층 의사결정을 Follow-up. 다만 <b>미국-이란 전쟁으로 Relocation이 지연될 수 있어</b> SKA/재무본부와 지속 운영 시 Value-up 방안도 병행 검토.",
 ['중동 Relocation','최적안','Risk Exposure','Cash Flow','SKG-SKA 합병','전쟁 지연'])

add('ska','ska1','2026-03-09','3/9~13','done',"SKA 4월 지속 가동 결정: 가동손익·MB 처분손익·LNG 재고 부족 대응 종합 판단",
 "SKA 가동손익과 MB 처분손익 비교, LNG 재고 부족 대응 방안을 각 본부와 종합 논의하여 <b>SKA 4월 지속 가동 의사결정</b> 도출 (3/2~6 주에는 4월 S/D도 검토됐었음). 5월 이후 가동 여부도 각 본부와 협의해 전사 관점 최적 방향 수립 예정.",
 ['4월 가동','S/D','LNG 재고','MB 처분','의사결정'])

add('ska','ska2','2026-03-09','3/9~13','info',"DY 이사회 전략세션(3/19)·SK가스 이사회 전략세션(3/30)에 SKA 사업구조 개편 안건 포함",
 "기획팀이 준비 중인 DY 이사회 전략세션(3/19)에서 '26년 경영계획·주요 전략과제와 함께 <b>SKA 사업구조 개편</b>을 공유하고, 가스 이사회 전략세션(3/30)에서는 미국-이란 전쟁 시나리오별 대응방안, GPS 과제, LNG 수요확장 전략, SKA 사업구조 개편을 발표 예정.",
 ['이사회 전략세션','DY','SKA 구조개편','3/19','3/30'])

add('ska','ska3','2026-03-16','3/16~20','prog',"Relocation 협상 변수 정리: 자산 이전액·풋/콜 옵션 지분가치 기준 협상 수용 범위",
 "지속운영과 중동 Relocation 옵션을 Risk Exposure 관점에서 비교 중이며, 지속운영 시 스프레드·프로필렌 판매 포트폴리오·Terminal Value를 반영한 경제성 심화 검토. Relocation 협상의 핵심 변수인 <b>자산 이전액 및 풋/콜 옵션 지분가치</b>를 기준으로 협상 수용 범위를 정리, 차주 경영층 보고 예정.",
 ['Relocation','자산 이전액','풋/콜 옵션','Terminal Value','협상 범위'])

add('ska','ska3','2026-03-23','3/23~27','plan',"Relocation Term Sheet 협상: 4월 내 지분매입 목표, AGIC 수용 범위 설정 중",
 "중동 Relocation Term Sheet 협상 전략과 관련해 <b>4월 내 지분매입 완료를 최우선 목표</b>로 설정하고, 파트너 <b>AGIC</b>와의 입장 차이를 반영한 수용 가능 협상 범위 설정 중. 4/10 경영진 보고로 협상 가이드라인을 확정하고 이사회 커뮤니케이션을 단계적으로 추진 (w/재무본부).",
 ['AGIC','Term Sheet','지분매입','협상 가이드라인','이사회'])

add('ska','ska1','2026-03-30','3/30~4/3','done',"SKA 5월 가동 경제성 분석: 가동손익과 SKMU 기회이익 종합 시 계획대로 5월 S/D가 합리적",
 "SKA 5월 가동 경제성 분석 결과, 가동손익 수준과 <b>SKMU 기회이익</b>(SKA에 공급하지 않을 경우 SK멀티유틸리티 측 이익)을 종합 고려 시 <b>기존 계획대로 5월에 S/D하는 것이 합리적</b>이라는 결론. 전사 수익 극대화 관점의 프로판 물량 Allocation 최적화 검토도 지속.",
 ['5월 S/D','SKMU','기회이익','가동 경제성','프로판 Allocation'])

add('ska','ska3','2026-03-30','3/30~4/3','prog',"AGIC 협상안 구체화 중, 차주 TIC 업데이트 반영해 경영층 논의",
 "중동 Relocation 협상 관련 AGIC와 당사 간 수용 가능한 협상 범위를 설정하고 양측 입장을 반영한 협상안 구체화 중. 차주 <b>TIC(총투자비) 업데이트</b> 결과를 반영해 경영층 논의 및 협상 전략·구조개편 의사결정 지원 (w/재무본부).",
 ['AGIC','TIC','협상안','Relocation'])

add('ska','ska3','2026-04-06','4/6~10','prog',"APC 수용 조건·중동 Greenfield/Relocation TIC 반영 협상 전략, 4개 옵션 비교",
 "SKA 구조개편 관련 <b>APC의 수용 가능 조건</b>과 중동 Greenfield/Relocation TIC 분석을 반영한 협상 전략 구체화 중. SKA-UPP 최적화 옵션으로 i) Relocation, ii) PMC-UPP 구조개편 및 SKG-SKA 합병, iii) 그룹 화학 3사 협력, iv) 독자 운영을 종합 비교 후 경영진 의사결정 지원 예정 (w/재무본부).",
 ['APC','Greenfield','TIC','PMC','UPP','4개 옵션','독자 운영'])

add('ska','ska2','2026-04-13','4/13~17','prog',"PMC 매각·AGIC Relocation 포함 통합 옵션·Timeline 의사결정 체계, 4/29 보고 준비",
 "SKA/UPP 구조개편 관련 <b>PMC 매각, AGIC Relocation 협상</b> 등을 포함한 통합 옵션과 시나리오별 Timeline 기반 의사결정 체계 구체화 완료. SKA/재무본부/BSC와 옵션별 경제성·Risk Exposure 비교 분석 중이며 <b>4/29 경영진 보고</b>로 구조개편 방향성 설정 지원.",
 ['PMC','AGIC','Timeline','BSC','4/29 보고','Risk Exposure'])

add('ska','ska2','2026-04-20','4/20~24','prog',"4개 옵션 Risk Exposure 비교 + 시나리오별 Game Plan 수립 → 4/29 의장 보고",
 "SKA/UPP 구조개편 4개 옵션에 대한 Risk Exposure 기반 비교 분석과 Timeline별 의사결정 체계를 구체화하고, 시나리오별 Game Plan을 수립해 <b>4/29 의장 보고</b>로 구조개편 방향성과 실행 전략 지원 예정.",
 ['Game Plan','4개 옵션','의장 보고','Risk Exposure'])

add('ska','ska2','2026-04-29','4/27~5/1','mile',"4/29 경영진 보고: 4개 옵션 Total Exposure와 SKA/UPP 구조개편 Roadmap",
 "SKA/UPP 구조개편 4개 옵션의 Risk Exposure 비교 분석(w/재무본부)을 수행, 옵션별 Total Exposure와 함께 <b>PMC를 활용한 UPP 구조개편, Relocation을 활용한 SKA 구조개편, Hard Exit, 지속 운영</b>의 Roadmap·고려사항을 4/29 경영진 보고. 후속으로 종합 Game Plan·Framework 정리와 <b>LYB·PMC 입장에서 본 UPP 구조개편 시각</b> 분석 후 추가 보고 예정.",
 ['4/29','Total Exposure','PMC','Hard Exit','LYB','Roadmap'])

add('ska','ska5','2026-05-04','5/4~8','plan',"일본 NCC 구조조정 → SKA 프로필렌 일본 수출 기회·BDH 사업기회 검토 착수",
 "일본 석화사 미팅 Follow-up으로 <b>SKA 프로필렌 공급 확대 기회</b> 본격 검토. BDH(부타디엔) 타당성 검토를 위해 국내·울산 부타디엔 수급 분석과 금호석유화학 미팅 추진. Mitsui Korea와 미팅해 일본 NCC 구조조정에 따른 Mizushima 지역 니폰쇼쿠바이·아사히카세이 대상 프로필렌 수출 기회 발굴, 필요 시 APIC(5/28~29, 후쿠오카) 참석. 일본 NCC 구조조정이 SKA value-up에 큰 영향이 있음을 확인.",
 ['일본 NCC','프로필렌 수출','Mitsui Korea','니폰쇼쿠바이','아사히카세이','BDH','금호석유화학','APIC'])

add('ska','ska2','2026-05-04','5/4~8','done',"여수 석화 구조개편의 PMC/UPP Impact 포함 시나리오별 구조개편 프레임 경영진 보고",
 "SKA/UPP 구조개편 시나리오별 프레임·옵션을 구체화하고 <b>여수 석유화학 구조개편에 따른 PMC/UPP Impact</b> 분석 결과를 종합해 경영진 보고. 향후 PMC 대상 UPP 매각 의사결정 고려요소, SKA 지속가동 경제성, LYB/PMC 전략적 포지션·예상 협상 방향, 그룹 화학 3사 협력 방향을 지속 검토.",
 ['여수 구조개편','PMC','UPP 매각','LYB','그룹 화학 3사'])

add('ska','ska5','2026-05-11','5/11~15','prog',"Mitsui Korea 미팅: 관서지역 일본 석화사 기회 공감, APIC 미팅 3건 확정",
 "SKA 프로필렌 일본向 수출 기회 모색을 위해 Mitsui Korea와 미팅, 일본 NCC 구조조정에 따른 관서지역 Nippon Shokubai·Mitsubishi Chemical 대상 사업기회에 공감대 형성. APIC(5/28~29) 기간 <b>Idemitsu·Mitsubishi Chemical·Mitsui Chemicals 미팅 확정</b>, Nippon Shokubai 추진 중. 5/12 발표된 Mizushima 구조개편안에서 Asahi Kasei가 2030년까지 AN 생산 중단 계획 → 차주 SKA/Asahi Kasei/동서석유화학 미팅에서 동서석유화학 증산 가능성 파악 예정.",
 ['Mitsui Korea','Nippon Shokubai','Mitsubishi Chemical','Idemitsu','Asahi Kasei','동서석유화학','Mizushima','AN'])

add('ska','ska2','2026-05-11','5/11~15','prog',"SKA·Deal TF와 옵션별 경제성 산정 기준 논의, PMC 협상 Position 포함 차주 보고",
 "SKA 및 Deal TF와 구조개편 옵션별 경제성 산정 기준 논의. 차주 옵션별 경제성 비교, <b>PMC 대상 UPP 매각 시 Relocation·그룹 화학 3사 통합 등 타 옵션으로의 확장 가능성</b>, PMC 협상 과정의 상대방 Position을 종합해 사장 보고 예정.",
 ['Deal TF','경제성 산정 기준','PMC','UPP 매각','확장 가능성'])

add('ska','ska2','2026-05-18','5/18~22','prog',"UPP→PMC 매각 'No Regret Move' 판단 Framework 경영진 보고",
 "UPP를 PMC에 매각 추진하는 것이 <b>No Regret Move</b>인지 판단하기 위한 의사결정 Framework과 주요 점검 Point·최적화실 가설을 경영진 보고. 5월 말까지 UPP 매각 협상 Boundary Condition을 고민하는 한편, 대내외 환경 변화를 반영해 지속운영·Relocation·그룹 3사 통합 관점에서 PDH 사업의 전략적 의미를 재검토하고 Risk Exposure 축소/확대 대응 중장기 방향성 구체화 계획.",
 ['No Regret','PMC','Boundary Condition','PDH 전략적 의미','Risk Exposure'])

add('ska','ska5','2026-05-28','5/25~29','info',"APIC(5/28~29) 미팅: 니폰쇼쿠바이 연 20만톤 Short, 미쓰비시·미츠이 '30년 이후",
 "APIC 기간 니폰쇼쿠바이·미쓰비시화학·미츠이화학과 미팅해 일본 NCC 구조조정에 따른 SKA 일본向 프로필렌 판매 기회 모색. <b>니폰쇼쿠바이는 연간 약 20만톤 Short 포지션</b>으로 일본 내수 조달 우선이나 SKA와의 추가 협의에 열려 있고, 미쓰비시화학·미츠이화학은 <b>2030년 미즈시마 AMEC 크래커 S/D 및 오사카 OPC 통합법인 전환 이후</b> 미즈시마 단지의 구조적 Import 가능성 확인.",
 ['APIC','니폰쇼쿠바이','20만톤','미쓰비시화학','미츠이화학','AMEC','OPC','미즈시마'])

add('ska','ska2','2026-05-25','5/25~29','prog',"PMC 협상 결렬 대비 대안 시나리오 3개 Total Risk Exposure 비교, 6/5 보고 준비",
 "PMC와의 UPP 매각 협상 결렬 가능성에 대비한 대안 시나리오 ① UPP Hard Exit 후 SKA 지속 운영, ② UPP 운영 유지 및 Relocation 추진, ③ Relocation 실패 시 UPP Exit를 <b>Total Risk Exposure 관점</b>에서 비교·분석 중. 6/5 경영층 보고로 구조개편 방향성·대응 전략 수립 지원.",
 ['Plan B','Hard Exit','Relocation','UPP Exit','Total Risk Exposure','6/5'])

add('ska','ska4','2026-05-25','5/25~29','prog',"싱가포르 전망기관 CMA·Argus 미팅: PDH/PP 중장기 지속가능성 평가 착수",
 "PDH/PP 사업의 중장기 지속가능성 평가를 위해 싱가포르 소재 에너지 시장 전망 기관 <b>CMA, Argus</b>와 미팅. 미국–이란 종전 이후 에너지 시장 재편, 동북아 NCC 설비 합리화, 중국 올레핀 증설 전망 등을 고려해 동북아 PDH/PP Spread를 종합 분석할 계획이며, 전문 기관의 전망 Logic을 내재화해 최적화팀 시장 분석 역량 강화.",
 ['CMA','Argus','PDH/PP Spread','동북아','중국 올레핀 증설','NCC 합리화'])

add('ska','ska5','2026-06-01','6/1~5','info',"일본 석화사 기회: 니폰쇼쿠바이 Spot 25만톤 대체 수요, 미쓰비시 '30년 이후 Term 15만톤",
 "5월 검토한 일본 석화사 4개사 중 니폰쇼쿠바이·미쓰비시화학 중심으로 공급 기회 전망. 니폰쇼쿠바이는 기존 수입 15만톤 + 내년 이후 내수 10만톤 대체 수요가 있으나 <b>물류 제약으로 Term은 어렵고 Spot만 가능</b>. 미쓰비시화학은 미즈시마 구조조정 완료 후 <b>약 15만톤 Term 공급 기회</b>가 예상되나 발현 시점은 2030년 이후.",
 ['니폰쇼쿠바이','미쓰비시화학','15만톤','Spot','Term','2030년'])

add('ska','ska2','2026-06-01','6/1~5','prog',"Plan B 3개 시나리오 End Image·Total Risk Exposure 구체화 → 6/10 보고",
 "PMC와의 UPP 매각 협상 결렬 대비 Plan B 시나리오(① UPP Hard Exit 후 SKA 지속 운영, ② UPP 운영 유지 및 Relocation, ③ Relocation 실패 시 UPP 청산)별 의미·고려사항·<b>End Image·Total Risk Exposure</b>를 비교 분석 중. <b>6/10 경영층 보고</b>로 방향성·대응 전략 수립 지원 (당초 6/5 예정에서 조정).",
 ['Plan B','End Image','UPP 청산','6/10 보고'])

add('ska','ska4','2026-06-01','6/1~5','plan',"동북아 PDH/PP Spread 전망 프로젝트 추진: '26~'35년 시장·가격 결정 요인·시나리오별 수익성",
 "CMA·Argus 미팅을 바탕으로 동북아 PDH/PP Spread 전망 프로젝트를 추진, <b>'26~'35년 동북아 PDH·PP 시장 전망, 가격 결정 요인, 시나리오별 수익성 변화</b>를 분석할 계획. 종전 이후 시장 재편·동북아 NCC 합리화·중국 올레핀 증설을 반영하고 전망 Logic 내재화.",
 ['CMA','PDH/PP 전망','2035','시나리오별 수익성'])

add('ska','ska2','2026-06-15','6/15~19','risk',"UPP 하반기 파산 가능성 부각 → LYB CFO Call 준비(연말까지 안정 운영 협력 제안)",
 "SKA/UPP 구조개편 관련 <b>LYB CFO Call Meeting</b> 준비. LYB 글로벌 포트폴리오 재편 속 범용 PP 중심 UPP와 Specialty PP 중심 PMC의 전략적 중요도 차이, PMC가 LYB의 Specialty PP·Technology Licensing과 연계된 전략 자산인지 경영층 시각 점검 예정. <b>UPP는 연체채권 누적·운영자금 부족으로 하반기 파산 가능성이 높아지는 상황</b>이어서, UPP 파산 시 PMC 유동성 리스크와 LYB 국내 신뢰도 저하 가능성을 공유하고 연말까지 UPP 안정 운영·구조개편 협력을 제안할 계획. 재무본부·그룹 화학 TF와 UPP 가치 극대화 시나리오 지원.",
 ['LYB','CFO','PMC','UPP 파산','연체채권','Specialty PP','그룹 화학 TF'])

add('ska','ska2','2026-06-22','6/22~26','prog',"핵심 검토 과제 3개: UPP 개편의 SKG 손익 영향·SKA 중장기 수익성·적정 합병 시기",
 "CEO 관점에서 사업 가치·중장기 지속가능성·이해관계자 입장을 종합 점검하는 방향으로 추진. 핵심 과제는 ① UPP 구조개편이 SK가스 포트폴리오 손익·기업가치에 미치는 영향, ② 동북아 PDH Spread 전망 기반 SKA 중장기 수익성·지속가능성, ③ 이해관계자·구조개편 일정과 연계한 <b>SKA 적정 합병 시기 및 Communication 전략</b>.",
 ['핵심 과제','합병 시기','기업가치','PDH Spread','Communication'])

add('ska','ska1','2026-06-29','6/29~7/3','done',"하반기 SKA 가동 경제성 보고: V/C 통합 기준 8월 이후 가동 유리, 의사결정 프로세스 구축",
 "하반기 SKA 가동 경제성 분석 결과를 전략본부 Weekly에서 보고. <b>SKA Standalone 경제성, 공장 Shutdown 시 발생 비용, SKG 관점 프로판 공급이익 및 Shutdown 시 프로판 처분 손익</b>을 종합한 Value Chain 통합 경제성 기준으로, 현재 시황에서는 <b>8월 이후 SKA 가동이 경제적으로 유리</b>하다는 결론. 향후 프로필렌 가격 급락에 대비해 SKA와 가동·비가동 여부를 신속히 판단할 의사결정 프로세스를 공동 구축 예정.",
 ['가동 경제성','Standalone','Shutdown 비용','프로판 공급이익','Value Chain 통합','8월 가동'])

add('ska','ska2','2026-06-29','6/29~7/3','prog',"SKA 합병 필요성·리스크·중장기 방향 경영진·이사회 보고 준비, 손익 모델·프로판 공급 구조별 손익 재점검",
 "SKA 합병 필요성, 합병 시 예상 리스크, SKA 중장기 사업 방향을 종합해 <b>경영진·이사회 보고 준비</b> 중. PDH 스프레드 시나리오와 프로필렌 판매계획을 업데이트해 SKA 손익 모델을 재점검하고, 프로판 공급 구조별 SKG 프로판 공급 손익도 추정 → <b>'30년까지 통합 C3 Value Chain 관점의 실질 Cash 창출 가능성</b> 분석.",
 ['SKA 합병','이사회','손익 모델','프로판 공급 구조','C3 Value Chain','2030'])

add('ska','ska4','2026-06-29','6/29~7/3','prog',"CMA 동북아 PDH/PP 중장기 전망 리서치 진행, 싱가포르 Intensive Workshop 예정",
 "시장전문기관 CMA와 동북아 PDH/PP 시장 중장기 전망 리서치 과제 진행 중. 차주 PDH/PP 시장 분석 초안을 검토하고 차차주 <b>싱가포르 Intensive Workshop</b>으로 중장기 PDH/PP 스프레드 전망 확보. CMA 시장 Knowledge 기반 <b>스프레드 전망 모델</b>을 구축하고 지속 Revisit해 SKA 중장기 전략에 활용.",
 ['CMA','싱가포르 워크샵','스프레드 전망 모델','PDH/PP'])

add('ska','ska4','2026-07-13','7/6~7/10','plan',"CMA 싱가포르 워크숍(7/13~16): '26~'35 수급·신증설·가격 Methodology·원가 경쟁력",
 "CMA와 PDH/PP 중장기 전망 싱가포르 워크숍을 7/13~7/16 진행 예정. 동북아 프로필렌·PP 수급 전망, '26~'35년 생산능력·가동률·신증설, 가격 산정 Methodology, <b>PDH·NCC·Integrated 사업 간 원가 경쟁력</b>을 확보해 SKA/UPP 중장기 지속 가능성과 구조개편 전략 점검. 구조개편 측면에서는 UPP End Image 시나리오와 Path별 의사결정·영향도 정리, SKA 합병 필요성·정당성 보완 및 이사회 자료·이해관계자 커뮤니케이션 지원.",
 ['CMA','싱가포르','Methodology','원가 경쟁력','UPP End Image','이사회 자료'])

add('ska','ska2','2026-07-13','7/13~7/17','info',"UPP 가동 여부별 SKA 경제성 보고: UPP 운영자금 투입 대비 지속운영 효익 제한적",
 "UPP 가동 여부에 따른 SKA 경제성을 비교 분석해 사장 보고, <b>UPP 운영자금 투입 대비 UPP 지속운영의 경제적 효익은 제한적</b>이라는 결론. 후속으로 Disruption 시나리오 하 동북아 프로필렌 CFR 가격 변동성 분석과 SKA 프로필렌 마케팅 플랜 작성 지원 예정. UPP End Image 시나리오도 Path별 핵심 의사결정·당사 Impact를 정리해 경영층 논의 계획.",
 ['UPP 운영자금','SKA 경제성','프로필렌 CFR','마케팅 플랜','End Image'])

add('ska','ska4','2026-07-13','7/13~7/17','info',"CMA 분석: 프로필렌 '28년 이후·PP '35년 이후 개선, Cash Cost 가격 추정 모델 착수",
 "CMA와 동북아 C3 시황 분석 결과 <b>프로필렌은 '28년 이후 시황 개선, PP는 '35년 이후 개선 본격화</b> 등 제품별 회복 속도 차이 확인 → SKA/UPP 구조개편·지속가능성 판단의 핵심 전제로 활용. CMA 가격 산정 Methodology를 기반으로 Cash Cost를 반영한 프로필렌 가격 추정 초기 모델 구축 중, 향후 Spread 추정 모델 완성 → SKA 손익 Simulation 고도화.",
 ['CMA','프로필렌 2028','PP 2035','Cash Cost','가격 추정 모델','손익 Simulation'])

add('ska','ska4','2026-07-24','7/20~7/24','done',"7/24 경영층 보고: 프로필렌 '28년 전후 저점 후 회복, PP는 '35년 이후 개선 전망",
 "동북아 프로필렌·PP 중장기 View를 7/24 경영층 보고. <b>프로필렌은 '28년 전후 저점 형성 후 수급 개선에 따른 점진적 회복</b>, <b>PP는 구조적 공급과잉과 중국 증설 지속으로 '35년 이후에야 본격 개선</b> 전망. 이에 따라 SKA는 통합 Value Chain 관점 경쟁력 강화에 집중하고, UPP는 End Image별 재무·사업 Impact를 구체화해 재무본부와 공동 시나리오 플래닝 준비.",
 ['7/24 보고','프로필렌 저점','PP 공급과잉','중국 증설','시나리오 플래닝'])

add('ska','ska2','2026-07-27','7/27~7/31','prog',"8/11 3차 특별위원회 준비: 합병 운영 효익 정량화, PwC와 SKA+SKG 통합 중장기 사업가치 산정",
 "SKA/UPP 구조개편 관련 <b>8/11 3차 특별위원회</b> 준비 (w/재무본부). SKA 합병 시 운영 관점 효익을 정량화하고, CMA 스프레드 전망을 전제로 <b>PwC와 SKA+SKG 통합 기준 중장기 사업가치</b> 산정. UPP 구조개편 시나리오별 대응 전략을 정리해 사외이사와 합병 판단 근거를 충분히 논의하고 합병 일정에 차질 없도록 준비. UPP End Image의 지향점은 <b>안정적 지속 운영을 전제로 Reputation 리스크 없이 PP 사업 Exit</b>이며, PMC·채권단·산업부·잠재 매수자별 협상 전략을 경영층 보고 예정.",
 ['특별위원회','PwC','사업가치','사외이사','UPP End Image','PP Exit','채권단','산업부'])

add('ska','ska2','2026-08-03','8/3~8/7','prog',"특별위원회 자료: 합병 운영 유연성 효과·C3 통합 사업가치·UPP 시나리오별 Cost/Risk",
 "3차 특별위원회(8/11) 대비 SKA 합병 시 <b>운영 유연성 확보에 따른 손실 최소화 효과</b> 분석, CMA 중장기 Spread 기반 PwC와 SKA+SKG C3 통합 중장기 사업가치 산정 완료, UPP 구조개편 시나리오별 Cost·Risk 및 대응 방안 정리. UPP End Image는 <b>PP 사업 Exit하되 UPP는 매각을 통해 제3자에 의한 지속 운영 체계로 전환, Reputation Risk 최소화</b>로 정의하고 이해관계자(PMC·채권단·산업부·잠재 매수자)별 Action 전략 구체화.",
 ['운영 유연성','C3 통합','사업가치','UPP 매각','제3자 운영','Reputation Risk'])

add('ska','ska2','2026-08-11','8/10~8/14','mile',"8/11 3차 특별위원회: 합병 타당성·리스크 논의, 8/20 4차 위원회 시점·방식 의결 예정",
 "<b>8/11 3차 특별위원회</b>에서 SKA 합병의 전략적·경제적 타당성, 법률·재무 리스크, 거래 공정성 및 실행 방식을 사외이사와 논의. 전략본부는 합병 시 운영 유연성 확보에 따른 손실 최소화 효과, CMA 기반 SKA+SKG C3 통합 중장기 사업가치, UPP 시나리오별 Cost·Risk에 집중. <b>8/20 4차 특별위원회에서 합병 시점과 방식(소규모합병 vs 일반합병) 추가 논의 및 의결 예정</b>. UPP End Image 대외 소통 방안·Action Plan은 8/22 경영진 보고 예정.",
 ['3차 특별위원회','4차 특별위원회','소규모합병','일반합병','의결','8/20'])

add('ska','ska2','2026-08-17','8/17~8/21','prog',"UPP End Image(PP Exit + 제3자 존속)와 이해관계자별 대응 원칙 8/23 경영진 논의 예정",
 "UPP End Image·대응 원칙, PMC·LYB·채권단·산업부 등 주요 이해관계자별 입장·대응 방안을 종합해 8/23 경영진 논의 예정. End Image는 <b>PP 사업 Exit과 제3자를 통한 UPP 존속</b>으로 설정, 재무 Exposure·프로필렌 공급·이해관계자별 대응원칙 준수. <b>PMC 주도 구조개편 추진을 지속 촉구</b>하고 Plan B 돌입 시에도 Reputation Risk 최소화 사전 대응방안 준비.",
 ['UPP End Image','PMC 주도','Plan B','LYB','채권단','8/23'])

add('ska','ska1','2026-08-31','8/31~9/4','plan',"합병 후 PDH 유연 가동 과제 도출: 판가 Index(MB+CP vs MOPJ 상대가)·물량 확정 Rule",
 "SKA 합병 후 <b>PDH 유연 가동</b>의 전제조건/Pricing/Sourcing·Trading/OI 영역별 검토 과제 초기 도출. 우선 Pricing 영역에서 MOPJ 상대가 공급 시 현재 MB/CP Mix 대비 전사 수익성 개선 가능성 검증 계획. 세부 과제: PDH 유연 가동 대체 공급 구조, 판가 Index 설계(MB+CP vs MB+MOPJ 상대가), SKA 물량 사전 확정 Rule, 울산기지·SKA 자산 연계 고순도 C3 공급 수익성, 프로판 소싱/트레이딩–프로필렌 생산 통합 의사결정 모델. SKA 가동경제성은 통합손익 분석 체계를 유관부서 합의로 확정하고 <b>Daily Monitoring·AI Agent 자동화</b>도 검토.",
 ['PDH 유연 가동','판가 Index','MOPJ 상대가','물량 확정 Rule','고순도 C3','Daily Monitoring','AI Agent'])

add('ska','ska1','2026-09-07','9/7~9/11','prog',"SKA 공급 조건 CP→FEI/MOPJ 상대가 전환 초기 분석: '23~'25 기준 수익 Pool 확대 가능",
 "SKA 공급 조건을 기존 <b>CP 연동에서 FEI/MOPJ 상대가 기반 소싱·공급 구조</b>로 전환하는 가능성을 초기 분석. 과거 3개년('23~'25) 기준 FEI/MOPJ Optionality 활용 기회를 포함하면 현 구조 대비 전사 수익 Pool 확대 가능성이 있다고 판단, 연도별 시황 변동성·실제 거래 여건을 반영해 추가 검증 후 Trading본부·SKA와 실행 가능성 구체화. 한편 <b>미국–이란 전쟁 격화로 FEI가 상승하며 11~12월 SKA 미공급 및 SKG 처분손익이 확대</b> → 전사 통합 손익 관점 SKA 최적 가동 여부 의사결정 관리.",
 ['CP 연동','FEI/MOPJ 상대가','수익 Pool','SKA 미공급','처분손익','FEI 상승'])

add('ska','ska1','2026-09-14','9/14~9/18','prog',"가동 중단 의사결정 Rule·손익 배분 원칙 검토, FEI 상승으로 12월 가동 여부 SKA와 논의",
 "FEI/MOPJ 상대가 구조는 원월물 선제 확보에 따른 원가 절감·Optionality로 수익 Pool 확대 가능성이 있다고 초기 판단 → <b>분석 기간을 과거 10개년으로 확대</b>해 빈도·규모와 Downside Risk 검증 후 종합 보고 예정. 가동 경제성 측면에서는 프로판 3자 판매·시황 급변 대응력을 고려한 <b>프로판 공급 확정과 SKA 가동 중단 의사결정 기본 Rule</b>, 가동 계획 변경 시 SKA·Trading 본부 간 손익/비용 배분 원칙 검토. FEI 상승으로 12월 SKA 미공급·SKG 처분손익이 확대되어 SKA와 12월 가동 여부 논의, 별도 보고 예정.",
 ['10개년','의사결정 Rule','손익 배분','12월 가동','FEI','프로판 3자 판매'])

add('ska','ska1','2026-10-05','10/5~10/9','prog',"합병 Value Creation 핵심 = PDH 가동 유연성, '27.9월 열교환기 보수 연계 운영 방안",
 "SKA와 합병 Value Creation의 핵심 사항으로 시황·계약·운영을 종합 고려한 <b>PDH 가동 유연성 확보</b> 논의 중 — 단순 가동 여부 판단을 넘어 전사 통합 손익 극대화 운영 체계의 근간. PDH 가동 제약요인 해소, SKA 물량 확정 프로세스, 가동 계획 변경 시 SKA·Trading 본부 간 손익·비용 배분 원칙을 수립하고, <b>'27년 9월 예정 PDH 핵심 설비(열교환기) 보수 일정</b>과 공정 안정성을 고려한 최적 운영 시점·방안을 별도 보고 예정.",
 ['가동 유연성','Value Creation','열교환기','2027년 9월','물량 확정 프로세스'])

add('ska','ska1','2026-10-12','10/12~10/16','risk',"'27년 PDH 공헌 손실·프로판 공급 손실 동시 우려 → SKA向 공급 Index CP→FEI 변경 검토",
 "'27년 프로필렌 가격 하락에 따른 PDH 공헌 손실과 FEI/CP 스프레드 확대에 따른 프로판 공급 손실이 동시에 우려 → <b>PDH 가동 유연성 확보와 공급 Index 최적화</b>가 전사 손실 방어 핵심. SKA와 '27년 설비 보수일정을 고려한 적정 가동 중단 시점·기간, Term 고객 Obligation·대체 공급 확보, 운영 최적화 협의 프로토콜을 종합 보고 예정. 아울러 <b>SKA向 프로판 공급 인덱스를 CP에서 FEI로 변경</b>하는 방안을 SKA·Trading 본부와 논의 중 — 적정 FEI 마진·반영 시기, 법무실(H사 공급구조 일치·Compliance Issue), 세무팀(이월결손금 공제 조건) 검토를 거쳐 SKA 이체가 최적안 도출.",
 ['2027','PDH 공헌 손실','CP→FEI','이체가','Compliance','이월결손금','Term Obligation'])

add('ska','ska1','2026-10-19','10/19~10/23','risk',"'27년 SKA 경영계획상 약 △700억 손실 전망 → 가동 최적화 의사결정 기준(경제성·고객·설비) 정리",
 "'27년 SKA 사업은 경영계획상 <b>약 △700억원 손실</b>이 전망되어 PDH 가동 유연성 확보가 전사 손실 방어의 핵심 과제. SKA와 '27년 가동 최적화 의사결정 기준(경제성·고객 대응·설비 안정성)과 운영 최적화 Process를 종합 정리 중이며, 이를 통해 전사 관점 SKA 운영 최적화 체계 확립.",
 ['△700억','2027','가동 최적화','의사결정 기준','설비 안정성'])

add('ska','ska5','2026-10-19','10/19~10/23','plan',"H사 협력 검토 착수: '27년 H사 PDH 가동 중단–SKA 프로필렌 공급 연계 모델",
 "'27년 <b>H사 PDH 공장의 일정 기간 가동 중단과 SK어드밴스드의 프로필렌 공급을 연계</b>하는 방안 검토 착수 예정. SK가스의 프로판 처분이익 Profit Sharing을 통해 H사 입장에서 가동 중단을 상회하는 경제성 구조를 확보하는 것이 관건이며, 울산 프로필렌 생산량 감축에 따른 롱 심화 해소와 SKA 고객 확보 효과 기대. 경제성·계약·인프라·리스크를 종합해 Win-Win 솔루션 도출.",
 ['H사','PDH 가동 중단','Profit Sharing','프로판 처분이익','울산 프로필렌 롱'])

add('ska','ska1','2026-10-26','10/26~10/30','prog',"'27년 PDH 가동 최적화 의사결정 기준 3축·S/D Timeline 정리 → 행복경영캔미팅 논의 예정",
 "'27년 PDH 가동 최적화 의사결정 기준 및 운영 최적화 Process 정리 중. 의사결정 기준은 <b>전사 통합 경제성 비교, 프로필렌 판매 Term 대응 가능성, 설비 안정성</b>의 3축으로 구성하고, 전사 관점 통합 경제성 기준과 S/D 의사결정 Timeline 수립 계획. SKA 가동 최적화 의사결정 체계를 구체화해 차주 행복경영캔미팅에서 논의.",
 ['의사결정 기준 3축','S/D Timeline','행복경영캔미팅','2027'])

add('ska','ska5','2026-10-26','10/26~10/30','prog',"H사 협력 모델: 내년 상반기 높은 프로판 시황 활용 시 양사 Win-Win 구조 설계 가능 판단",
 "'27년 H사 PDH 일정 기간 가동 중단과 SKA 프로필렌 공급 연계 방안 검토 중. <b>내년 상반기 높은 프로판 시황을 활용하면 현재 대비 H사·당사 모두 Win-Win 구조 설계가 가능</b>할 것으로 판단. 기존 H사向 프로판 처분 마진, SKA 프로필렌 Discount 변화를 고려한 양사 수익 규모와 제안 가능 가격·물량·기간을 종합해 별도 논의 예정.",
 ['H사','Win-Win','프로판 시황','프로필렌 Discount','처분 마진'])

# ═══════════════════ B. 전사 포지션 & 미-이란 전쟁 대응 ═══════════════════

add('pos','pos4','2025-12-08','12/8~12','info',"최적화실 신설 첫 주: 각 본부로부터 '5개 최적화 필요 업무' 요청 수령",
 "C Team Weekly 및 각 본부 논의를 거쳐 <b>5개 최적화 필요 업무</b> 요청 수령: ① LPG MI — 북미 MB 가격의 높은 상대가·절대가 유지 이유와 지속 여부 의견 정리(Key Question·Framework 합의, 12/23 CEO 보고 예정), ② EE 고속도로 충전소 입찰 — 입찰가 수준에 따른 Trading–EE 수익 배분 Guideline, ③ 평택 부두 준설 — 단독/공동 준설 최적화 및 Trading VLGC 양하에 영향 없는 일정, ④ MU Loss-cut — 차년도 Open Cargo 2개 Hedging 통한 손실 확정 여부·물량, ⑤ 한화 연료 공급 전환 — LPG vs LNG 투입 비교. 전사 수익성/지속가능성 극대화 관점에서 EE/Trading/G&P와 협업 방안 논의 중.",
 ['5개 최적화 업무','북미 MB','고속도로 충전소','평택 준설','MU Loss-cut','한화','LPG MI'])

add('pos','pos4','2025-12-15','12/15~19','plan',"최적화실 역할 정의(Cross-BU 최적화·시황 급변 대응·전사 RM 가이드라인), 과제 6개로 확대",
 "인사 발령으로 <b>1 PL + 4 Manager 체계</b> 확정. 최적화실 역할을 (1) Cross-BU 최적화 및 전사 통합 수익 극대화 관점 의사결정, (2) 시황 급변 시 Opportunity/Risk 분석 및 전사 대응 준비, (3) 전사 RM 가이드라인 정리·모니터링으로 정의. 과제는 기존 5개에 <b>UGPS 수익 방어 연료 최적화(Spot 연료비 CP-base vs FEI-base 절감)</b>를 더해 6개 정의 중 (LPG MI 건은 12/24 CEO 보고 예정). 12/23 전략본부 워크샵에서 우선순위 확정 계획.",
 ['최적화실 역할','Cross-BU','RM 가이드라인','UGPS','CP vs FEI','워크샵'])

add('pos','pos4','2025-12-22','12/22~26','done',"평택기지 부두 준설 방안 합의: '26.4월까지 단독 준설 착공, '27년 통합 준설은 상반기 착공 유도",
 "평택기지·Trading본부와 부두 수심 추이 및 대응 방안 논의. <b>'26년 5월 이후 Full Cargo 접안이 어려울 것</b>으로 예상되어 단독 준설 필요성 재확인 → '26년 4월까지 준설공사 착공(2주 소요), '27년 통합 준설은 퇴적에 따른 접안 어려움 발생 전인 '27년 상반기 착공 유도로 합의. 연초 CEO 보고에서 수심 추이·대응 방안·Contingency Plan(통합 준설 지연·퇴적 가속 시) 논의 예정.",
 ['평택기지','부두 준설','Full Cargo','단독 준설','Contingency Plan'])

add('pos','pos1','2025-12-29','12/29~1/2','plan',"전사 Position 관리·시황 급변 대응 컨트롤타워 구축을 최적화팀 최우선 과제로 선정",
 "전략본부 워크샵 논의를 바탕으로 최적화팀 업무·우선순위를 정리, SKA 의사결정과 함께 <b>전사 Position 관리 및 시황 급변 시 대응 컨트롤타워 구축</b>을 최우선 과제로 선정.",
 ['컨트롤타워','전사 Position','우선순위','워크샵'])

add('pos','pos3','2026-01-05','1/5~9','info',"JKM Position 최적화: EE–G&P Natural Hedge 효과는 Matching 차이로 작음",
 "EE본부(JKM Sell)와 G&P본부(JKM Buy) 간 반대 Position 상쇄를 통한 <b>Natural Hedge</b> 추진 적합성 검토. 본부 간 월별 Matching 물량 차이(예: 6월 EE 0.6만톤 vs G&P 6.7만톤)로 효과는 작으나, EE본부 Position 진입 시 G&P본부와 내부거래 논의 필요. 차주 전략본부 Weekly에서 검토 결과 논의 예정.",
 ['JKM','Natural Hedge','EE본부','G&P본부','내부거래','0.6만톤','6.7만톤'])

add('pos','pos1','2026-01-05','1/5~9','plan',"3월 Target으로 LPG/LNG Index별 전사 Position Map 작성 착수",
 "최적화팀이 <b>3월 완성을 목표로 LPG/LNG Index별 전사 Position Map</b> 작성 중. 본부별로 흩어진 가격 지수 노출 물량을 한 장으로 모으는 첫 단계.",
 ['Position Map','LPG/LNG Index','3월 Target'])

add('pos','pos4','2026-01-15','1/12~16','mile',"1차 전사 최적화 협의체 개최 (1/15): 최적화실 업무 영역·과제 의견 수렴, JKM Swap 안건 논의",
 "<b>1차 전사 최적화 협의체(1/15)</b> 진행. 최적화실 업무 영역과 추진 과제에 대한 의견을 수렴해 과제 List update 예정. EE본부(JKM Sell)–G&P본부(JKM Buy) 간 반대 Position Swap 내부 Process를 마련해 협의체 안건으로 논의 완료.",
 ['전사 최적화 협의체','1/15','JKM Swap','내부 Process'])

add('pos','pos1','2026-01-12','1/12~16','prog',"전사 LNG/LPG Index 통합 Position 체계 정리, Framework 초안 후 CEO 의견 반영",
 "전사 LNG/LPG Index 통합 Position 체계 정리 작업 중. 최적화실 차원의 Position Framework 초안을 작성한 뒤 차주 CEO/본부장 의견을 반영할 계획.",
 ['Position Framework','통합 Position','CEO 의견'])

add('pos','pos1','2026-01-19','1/19~23','prog',"본부별 포지션 Map 설계: EE 산업체/석화사·G&P GPS/MU 공급용 초안 작성",
 "[전사 Position 통합 관리 체계 구축] 소싱/판매 전 주기 밸류체인에 걸친 본부별 포지션 Map 설계 중, <b>EE 산업체/석화사 공급용 및 G&P GPS/MU 공급용 초안</b> 작성. EE–G&P 간 JKM 반대 포지션 Swap 원칙 수립 이후 최근 시황(JKM/HH 상승)에 따라 본부별 개별 헤지가 진행 중이며 최적화실이 원가 절감·전사 관리 차원에서 모니터링.",
 ['포지션 Map','EE 산업체','GPS/MU','JKM Swap','개별 헤지','HH'])

add('pos','pos1','2026-01-26','1/26~30','done',"전사 소싱·판매 전 주기 포지션 Map 초안 완성, Trading 본부 포지션 관리 방식 추가 논의",
 "전사 소싱·판매 전 주기 <b>포지션 Map 초안 완성</b>. Trading 본부의 포지션 관리 방식을 어떻게 반영할지 추가 논의 진행 중.",
 ['포지션 Map','초안 완성','Trading 본부'])

add('pos','pos3','2026-02-02','2/2~6','plan',"SKA 마스터플랜의 일부로 '프로판 절대가 Hedge 전략' 검토 예정",
 "국내 가동과 Relocation 비교를 위한 BCG 프로필렌 스프레드 Tool 활용 중장기 PDH 스프레드 전망 재검토와 함께 <b>프로판 절대가 Hedge 전략</b> 검토 예정 — 이후 '프로필렌 Proxy Hedge' 과제로 발전하는 출발점.",
 ['프로판 절대가 Hedge','BCG','PDH 스프레드'])

add('pos','pos3','2026-02-09','2/9~13','prog',"프로판 절대가 Hedge 위한 프로필렌 Proxy Hedge 방안·Trading 운임 원가 분석 착수",
 "리스크 관리 및 구조 고도화를 위해 <b>프로판 절대가 Hedge를 위한 프로필렌 Proxy Hedge 방안</b>(프로필렌 선물시장이 없어 상관관계 높은 다른 지수로 대신 헤지)과 Trading 운임 원가·시장 Dynamics 분석 진행 중.",
 ['Proxy Hedge','프로판 절대가','운임 원가'])

add('pos','pos1','2026-02-09','2/9~13','plan',"전사 LPG·LNG 통합 포지션 Dashboard 1Q 내 구축 목표 설정",
 "포지션 Map을 발전시켜 <b>전사 LPG·LNG 통합 포지션 Dashboard를 1Q 내 구축</b>할 예정.",
 ['통합 포지션 Dashboard','1Q'])

add('pos','pos1','2026-02-16','2/16~20','prog',"통합 포지션 Dashboard Framework 수립, 3/16 SKGI 출장 시 협의 예정",
 "1Q 내 전사 LPG·LNG 통합 포지션 Dashboard 구축을 목표로 Framework을 수립, <b>3/16 SKGI(SK가스인터내셔널) 출장</b> 시 관련 협의 예정. Dashboard의 목적은 전사 포지션 가시화와 Hedge·Trading 의사결정의 일관성 확보를 위한 관리 체계 고도화.",
 ['Dashboard Framework','SKGI','3/16','의사결정 일관성'])

add('pos','pos2','2026-02-23','2/23~27','mile',"미국–이란 전쟁 발발(주말): Daily 영향 점검 착수, 포지션 맵 기반 리스크 노출·대응 통합 관리",
 "주말에 발생한 <b>미국–이란 전쟁</b>과 사우디 아람코 사고 등 지정학적 이벤트에 따른 인덱스 변동성이 사업부 손익에 미치는 영향을 점검. 구축 중인 전사 포지션 맵을 기반으로 리스크 노출과 대응 방향을 통합 관리하고, 전쟁이 전사에 미치는 영향을 <b>Daily로 점검</b>하며 각 본부와 전사 관점 대응 방안 준비 → 전사 컨트롤타워 기능 강화.",
 ['미국-이란 전쟁','아람코','Daily 점검','포지션 맵','컨트롤타워'])

add('pos','pos1','2026-02-23','2/23~27','prog',"전사 최적화 협의체에서 EE/G&P 포지션 맵 공유·경영층 활용도 피드백 수렴",
 "전사 최적화 협의체에서 EE/G&P 포지션 맵 현황을 공유하고 경영층 활용도 제고를 위한 피드백 수렴 완료. 이를 반영해 보완 작업 진행 중이며 전사 포지션 통합 관리 체계 고도화 계획.",
 ['포지션 맵','협의체','피드백','EE/G&P'])

add('pos','pos2','2026-03-02','3/2~6','prog',"전사 Daily 시황 점검 실시, 급변 시황 반영 전사 의사결정 Framework TRM과 정리",
 "미국–이란 전쟁 등에 따른 시황 변동성 확대에 대응해 <b>전사 Daily 시황 점검</b>을 실시하고 사업본부별 영향·대응 방안 논의. 급변 시황을 반영한 전사 의사결정 Framework를 TRM과 협업해 정리 중이며 차주 경영층 논의로 시황 대응·전사 운영 전략 방향 구체화 (SKA 4월 S/D 검토 포함).",
 ['Daily 시황 점검','TRM','의사결정 Framework','미국-이란 전쟁'])

add('pos','pos2','2026-03-09','3/9~13','prog',"전사 대응 방안·Daily 단기 대응 병행, 포지션 종합·대응 체계 Framework 차주 CEO 보고",
 "전쟁으로 인한 시황 변동성 확대에 대한 전사적 대응 방안 마련과 Daily 시황 점검을 통한 단기 대응 실행을 병행. SKA 4월 지속 가동 결정(가동손익 vs MB 처분손익, LNG 재고 부족 대응 종합)을 도출했고, 급변 시황을 반영한 <b>전사 포지션 종합·대응 체계·의사결정 Framework</b>를 구축해 차주 사장 보고 예정.",
 ['전사 대응','Daily','포지션 종합','CEO 보고','LNG 재고'])

add('pos','pos2','2026-03-16','3/16~20','done',"전쟁 시나리오별 전사 손익 영향 통합 분석, JKM Sell·Optionality 반영 Tool 구축",
 "전사 Daily 점검 체계를 운영하며 시황 전개에 따라 단기 대응 과제 실행 여부 관리. <b>전쟁 시나리오별 전사 손익 영향을 통합 분석</b>하고, 특히 EE JKM Sell Position, G&P Optionality, MU Bridge를 반영한 분석 Tool을 구축해 시황 대응 의사결정에 활용 예정.",
 ['전쟁 시나리오','손익 영향','분석 Tool','JKM Sell','Optionality','MU Bridge'])

add('pos','pos2','2026-03-23','3/23~27','prog',"호르무즈 봉쇄 가능성 포함 시나리오 점검, 상반기 프로판 물량 Allocation 최적화 과제 도출",
 "전사 Daily 점검 체계를 지속 운영하며 <b>호르무즈 해협 봉쇄 가능성</b> 등을 포함한 전쟁 시나리오별 손익 영향과 본부별 대응 과제 점검 중. 특히 <b>상반기 프로판 물량 Allocation 최적화</b>가 주요 과제로 도출되어 전사 통합 수익 극대화 관점에서 검토.",
 ['호르무즈','봉쇄','프로판 Allocation','시나리오'])

add('pos','pos2','2026-03-30','3/30~4/3','prog',"종전 시나리오별 전사 손익·대응 전략 정리, MI Index 전망 기반 사업부별 Action 구체화",
 "미국–이란 <b>종전 시나리오별 전사 손익 영향 및 대응 전략</b> 정리 중. LNG/LPG MI Index 전망을 기반으로 사업부별 Action·기회요인을 구체화하고 차주 C-team 논의로 방향 확정 후 경영진 의사결정 지원. 프로판 물량 Allocation 최적화 검토 지속.",
 ['종전 시나리오','MI Index','C-team','사업부별 Action'])

add('pos','pos3','2026-03-30','3/30~4/3','prog',"프로판·납사 Index 상관관계 기반 프로필렌 Proxy Hedge 적용 가능성 검토",
 "프로판 및 납사 Index 간 상관관계 분석을 기반으로 <b>프로필렌 Proxy Hedge</b> 적용 가능성을 검토 중이며, 이를 포함한 SKA 수익성 개선 방안 검토.",
 ['Proxy Hedge','납사','프로판','상관관계'])

add('pos','pos2','2026-04-06','4/6~10','done',"종전 시점(4월/7월/12월)별 시나리오 기반 전사 대응 전략 1차 안 수립, 월별 실행 계획 구체화",
 "미국–이란 <b>종전 시점(4월/7월/12월)별 시나리오</b> 기반 전사 대응 전략 1차 안 수립. 시나리오별 주요 의사결정 과제를 도출하고 월별 실행 계획으로 구체화해 시황 변화에 선제 대응하는 실행 체계 구축 중.",
 ['종전 시점','4월/7월/12월','대응 전략','월별 실행 계획'])

add('pos','pos3','2026-04-06','4/6~10','prog',"PDH 원가/판가 Hedge 전략: 프로판·프로필렌–MOPJ 상관관계 기반 Proxy Hedge·RM 기준",
 "에너지 가격 변동성을 활용한 수익 극대화와 리스크 관리 강화를 위해 PDH 원가/판가 Hedge 전략 검토 중. 프로판·프로필렌 Index와 <b>납사(MOPJ)</b> 간 상관관계를 기반으로 Proxy Hedge 적용 가능성과 전사 RM 기준을 정립할 계획.",
 ['PDH Hedge','MOPJ','Proxy Hedge','RM 기준'])

add('pos','pos2','2026-04-13','4/13~17','done',"종전 시나리오별 전사 'Action 메뉴판' 구축, CEO 관점 사업부별 핵심 실행 과제 도출 완료",
 "미국–이란 종전 시나리오(4월/7월/12월)별 <b>전사 Action 메뉴판</b>을 구축하고 CEO 관점에서 사업부별 핵심 실행 과제 도출 완료. 시나리오별 월 단위 의사결정 사항을 구체화해 선제 대응 가능한 전사 의사결정 체계 고도화, 차주 초 보고 예정.",
 ['Action 메뉴판','종전 시나리오','핵심 실행 과제','월 단위 의사결정'])

add('pos','pos3','2026-04-13','4/13~17','prog',"프로판–프로필렌 Hedge: 상승 구간 적용 설계, MOPJ Decoupling Risk 분석",
 "PDH 사업 수익성 제고를 위해 프로판–프로필렌 가격 Hedge 전략 검토 중. 시황 상승 구간에서의 Hedge 적용 방안을 설계하고 <b>프로필렌–MOPJ 상관관계 및 Decoupling Risk 분석, Index Back-testing</b>으로 안정적 수익 구조 확보 방안 마련 계획. 이를 새로운 TAM으로 AI 활용할 수 있도록 AX실과 협업.",
 ['Decoupling Risk','Back-testing','MOPJ','AX실','TAM'])

add('pos','pos2','2026-04-20','4/20~24','prog',"Action Plan 고도화: CEO 의사결정 과제 3건(도시가스 Hedge·MU Bridge·GPS 연료)",
 "종전 시나리오별 전사 Action Plan을 고도화하고 <b>CEO 의사결정이 필요한 핵심 과제로 도시가스 판가 Hedge, MU Bridge 운영, GPS 연료 최적화</b> 도출. 최적화 협의체 및 본부 간 추가 논의를 통해 선제적 대응 체계 강화.",
 ['도시가스 판가 Hedge','MU Bridge','GPS 연료 최적화','Action Plan'])

add('pos','pos3','2026-04-20','4/20~24','prog',"프로필렌/MOPJ/FEI 상관관계·Back-testing으로 Hedge 실행 가능성 검증 중",
 "프로판–프로필렌 가격 Hedge 전략 구체화 중. <b>프로필렌/MOPJ/FEI 간 상관관계 분석 및 Index Back-testing</b>을 기반으로 Hedge 실행 가능성을 검증하고, 최근 프로필렌 강세 시황을 활용한 추가 수익 창출 가능성도 병행 점검.",
 ['MOPJ','FEI','Back-testing','프로필렌 강세'])

add('pos','pos3','2026-04-27','4/27~5/1','prog',"Proxy Hedge 실행 가능성·수익성 검증 위해 외부기관(맥쿼리)과 협의 병행",
 "PDH 수익성 제고를 위한 프로판–프로필렌 Hedge 전략 구체화, 스프레드 상관관계 기반 Proxy Hedge 적용 가능성 검토. <b>외부기관(맥쿼리)과 협의</b>를 병행해 실행 가능성·수익성 검증 후 구체적 실행 방안을 별도 보고 예정.",
 ['맥쿼리','Macquarie','Proxy Hedge','수익성 검증'])

add('pos','pos2','2026-04-27','4/27~5/1','prog',"Action Plan 과제(MU Bridge·GPS Spot 연료 운영) 사업본부 협의, 종합 보고 예정",
 "종전 시나리오별 전사 Action Plan 관련 <b>MU Bridge, GPS Spot 연료 운영</b> 등 주요 과제에 대해 사업본부와 협의 진행. 전사 포지션 분석 및 대응 전략을 종합해 전략본부 Weekly에서 보고 예정.",
 ['MU Bridge','GPS Spot 연료','전사 포지션','Action Plan'])

add('pos','pos2','2026-05-04','5/4~8','done',"6MB 조기 출하 기반 MU Bridge 최적화 방안 경영진 보고·실행 의사결정 완료",
 "미국–이란 전쟁 대응 관련 <b>6월 MB 조기 출하 기반 MU Bridge 최적화 방안</b>을 G&P 본부와 공동 검토해 경영진 보고 및 실행 의사결정 완료. 차주 Weekly에서 전사 Position 분석·전쟁 대응 현황과 함께 <b>SKA 미공급 MB Allocation 방향성, 전사 Optionality 실행 기준</b> 논의 예정.",
 ['MU Bridge','6MB','조기 출하','MB Allocation','Optionality 실행 기준'])

add('pos','pos3','2026-05-04','5/4~8','prog',"맥쿼리와 프로필렌–MB Direct Hedge 검토, 내부 MOPJ Proxy Hedge 병행",
 "프로필렌 강세 시황을 활용한 Hedge 전략 구체화 중. <b>맥쿼리와 협업해 프로필렌–MB Direct Hedge</b>를 검토하는 한편 내부적으로 MOPJ 기반 Proxy Hedge 방안 병행 검토, 예상 수익성과 VaR 등을 종합 분석해 차주 Weekly 보고 예정.",
 ['맥쿼리','Direct Hedge','프로필렌-MB','MOPJ','VaR'])

add('pos','pos2','2026-05-11','5/11~15','done',"전사 MB 물량 최적화 방안 CEO 보고(MU Bridge·GPS Spot 연료·EE MB 활용)",
 "G&P 본부의 MU Bridge 전략, GPS Spot 연료 도입 계획, Eco Energy 본부의 MB 활용 계획을 포함한 <b>전사 MB 물량 최적화 방안</b>을 사장 보고. 후속으로 Term 기반 Optionality 및 GPS Spot 기반 Optionality에 대한 전사 차원 실행 기준을 구체화해 시황 변화 대응 전사 수익 극대화 체계 정립 계획.",
 ['MB 물량 최적화','MU Bridge','GPS Spot','Optionality','실행 기준'])

add('pos','pos3','2026-05-11','5/11~15','risk',"프로필렌–MOPJ Basis Risk로 현 시황 Hedge 실행 제한적 → 사전 기준·Framework 구축",
 "PDH Spread Hedge 관련, 현재 시황에서는 <b>프로필렌–MOPJ 간 변동성 확대에 따른 Basis Risk</b>로 실질적인 Hedge 실행이 제한적. 향후 적정 시황 도래 시 즉시 실행 가능한 수준의 PDH Hedge 기준 및 의사결정 Framework를 사전 구축할 예정.",
 ['Basis Risk','MOPJ','Hedge 기준','Framework'])

add('pos','pos2','2026-05-18','5/18~22','info',"전쟁 변동성 안정화 → Monitoring 체계 전환, 하반기 대응 전략은 2Q CEO Progress 준비",
 "미국–이란 전쟁에 따른 시장 변동성이 안정화되어 <b>당분간 Monitoring 체계로 전환</b>. LPG/LNG MI의 하반기 주요 Index 전망을 기반으로 사업부별 대응 전략을 수립해 2분기 CEO Progress 미팅에서 경영층과 논의 준비.",
 ['Monitoring 전환','안정화','2Q CEO Progress','Index 전망'])

add('pos','pos3','2026-05-18','5/18~22','prog',"과거 Hedge 진입 유효 시황 구간 Index·Sign-post 분석, 현 시점 진입 필요성 재점검",
 "PDH Hedge 전략 관련 <b>과거 Hedge 포지션 진입이 유효했던 시황 구간에 대한 Index 및 Sign-post 분석</b> 진행 중. 이를 기반으로 현재 시점의 진입 필요성을 재점검하고 시황 변화에 따른 실행 기준·의사결정 체계 구체화 예정.",
 ['Sign-post','진입 구간','Index 분석','실행 기준'])

add('pos','pos2','2026-05-25','5/25~29','done',"6월·연말 종전 시나리오별 유가·LPG·LNG 전망 수립, Action Plan 6/5 보고",
 "LPG/LNG MI와 협업해 <b>6월 종전 및 연말 종전 시나리오별 유가·LPG·LNG 가격 전망</b> 수립. 이를 토대로 전사 최적화 협의체에서 사업본부별 기회·위협 요인과 대응 전략을 구체화하고 시나리오별 전사 Action Plan을 마련, <b>6/5 2분기 CEO Progress</b>에서 경영층과 논의 예정.",
 ['6월 종전','연말 종전','가격 전망','기회·위협','Action Plan','6/5 CEO Progress'])

add('pos','pos3','2026-05-25','5/25~29','prog',"진입 구간 Signpost 분석 완료, 재무RM과 Paper 한도·부채비율 고려 Target 물량 검토",
 "기존 검토 대상 포지션의 진입 가능 구간 시황·Signpost 분석 완료. <b>재무RM팀과 전사 Paper 한도 및 부채비율 제약</b>을 고려한 Hedge 진입 가능 구간과 적정 Target 물량 검토 중이며, 현 시점 진입 필요성 Revisit 결과와 실행 기준을 경영층 보고 예정.",
 ['재무RM','Paper 한도','부채비율','Target 물량','Signpost'])

add('pos','pos3','2026-06-01','6/1~5','done',"종전 시나리오별 Hedge 기대수익·Risk 산정 → 두 시나리오 모두 '미실행'이 합리적",
 "과거 포지션 진입 가능 구간 분석을 완료하고, 미–이란 전쟁의 6월 종전 및 연말 종전 시나리오별 Index 전망을 기반으로 Hedge 진입 시 기대수익과 Risk를 산정. <b>현재 시점에서는 두 시나리오 모두 기대수익 대비 Risk가 높아 실행하지 않는 것이 합리적</b>이라는 결론. 향후 시황 변화 시 적시 실행할 수 있도록 PDH Hedge 기준과 의사결정 Framework 지속 고도화.",
 ['미실행','기대수익','Risk','종전 시나리오','PDH Hedge'])

add('pos','pos2','2026-06-15','6/15~19','prog',"전사 시황 대응 협의체 주 2회 운영 개시: 유가·FEI·JKM 동향과 본부별 포지션 논의",
 "미국–이란 전쟁에 따른 주요 에너지 Index 변동성 확대에 대응하기 위해 <b>전사 시황 대응 협의체를 주 2회 운영</b>. 유가·FEI·JKM 등 주요 Index 동향과 지정학적 이벤트, MI 시장 전망을 공유하고 각 본부의 포지션 현황·대응 전략 논의 → 본부 간 커뮤니케이션 강화, 전사 포지션 관리를 통한 하반기 수익 극대화 지원.",
 ['시황 대응 협의체','주 2회','FEI','JKM','유가'])

add('pos','pos3','2026-06-22','6/22~26','done',"납사 기반 Proxy Hedge 가이드라인 CEO 보고, SKA·재무실과 실행 프로토콜 정립 예정",
 "SKA 수익성 제고를 위한 PDH Hedge 전략으로 <b>납사 기반 Proxy Hedge 가이드라인을 수립해 사장 보고</b>. 지정학적 이벤트 발생 시 적시 실행할 수 있도록 SKA 및 재무실과 실행 프로토콜을 정립하고, AX실과 협력해 시황 모니터링 적시성과 Hedge Back-testing 정합성을 높이는 분석 체계 구축 예정.",
 ['Proxy Hedge 가이드라인','CEO 보고','실행 프로토콜','AX실','Back-testing'])

add('pos','pos2','2026-06-22','6/22~26','prog',"종전 기대·호르무즈 통항 정상화 Index 점검, 하반기 상대가·Optionality Spread 모니터링",
 "주 2회 전사 시황 대응 협의체에서 미국–이란 전쟁 <b>종전 기대감과 호르무즈 해협 통항 정상화</b>에 따른 주요 에너지 Index 변화를 점검하고 본부별 포지션 대응 방안 논의. 하반기 유럽 LNG 재고 비축과 동북아 수요 증가에 대비해 상대가, Optionality Spread 등 핵심 지표를 집중 모니터링.",
 ['호르무즈 통항','종전 기대','유럽 LNG 비축','상대가','Optionality Spread'])

add('pos','pos2','2026-06-29','6/29~7/3','prog',"종전 시나리오 대비 하반기~'27년 본부별 핵심 Action Item 수립 착수",
 "미국–이란 종전 시나리오에 대비해 본부별 Action 과제 수립 중. LPG/LNG MI의 View와 전사 포지션을 종합해 <b>금년 하반기부터 '27년까지의 본부별 핵심 Action Item</b>을 정리하고 전사 시황 대응 협의체에서 실행 전략 논의.",
 ['Action Item','2027','종전 시나리오','MI View'])

add('pos','pos4','2026-07-09','7/6~7/10','prog',"7/9 전사 최적화 협의체: 중동 전쟁·시황 전망, 본부별 포지션 현황, GPS 운영 최적화 포인트 논의",
 "전사 포지션 관리는 전사 최적화 협의체를 통해 지속 고도화 중. <b>7/9 협의체</b>에서 중동 전쟁 및 시황 전망, 본부별 포지션 진행 현황, GPS 실제 운영 과정의 최적화 포인트 논의. 전사 포지션 맵을 주기적으로 업데이트하고, 미국-이란 전쟁 재격화 가능성을 감안해 주요 Index 변동 모니터링·추가 Potential 확보·리스크 관리에 집중. PDH Hedge는 7월 내 AI 기반 Back-testing 재검증 및 실시간 모니터링 체계 구축, 차주 SKA와 실행 프로토콜 정립 예정.",
 ['7/9 협의체','포지션 맵','GPS 운영 최적화','전쟁 재격화','AI Back-testing'])

add('pos','pos2','2026-07-13','7/13~7/17','prog',"C-team Weekly에서 미–이란 충돌 재점화에 따른 본부별 필요 Action 논의",
 "금주 C-team Weekly에서 <b>미국–이란 충돌 재점화</b>에 따른 본부별 필요 Action 논의. 이란 사태로 주요 Index 변동성이 확대되는 만큼 각 본부가 선제 대응할 수 있도록 지원.",
 ['충돌 재점화','C-team Weekly','본부별 Action'])

add('pos','pos2','2026-07-20','7/20~7/24','prog',"전쟁 재격화 국면 Action Plan 점검: JKM 급등 대비 EE·G&P 포지션 모니터링",
 "미–이란 전쟁 재격화 국면에서 하반기 전사 수익력 극대화를 목표로 본부별 핵심 Action Plan 점검 중. 특히 <b>하반기 JKM 급등 가능성</b>에 대비해 Eco Energy 본부의 JKM Sell Position과 G&P 본부의 Optionality 실행 계획을 전사 최적화 관점에서 모니터링하고 신속 대응 체계 구축. PDH Hedge는 유가 상승에 따른 납사 가격 상승을 반영해 근월물·원월물 기준 MOPJ Hedge 진입 여부 검토, 진입 기준·리스크 포함 실행 방안 차주 논의.",
 ['JKM 급등','JKM Sell','Optionality','MOPJ Hedge','근월물·원월물'])

add('pos','pos3','2026-07-27','7/27~7/31','mile',"Proxy Hedge 전략 CEO 보고: MOPJ–MB 고스프레드 활용 11·12월물 60% 진입 예정",
 "PDH 수익성 안정화를 위한 Proxy Hedge 전략을 사장 보고. 미국–이란 전쟁 격화로 형성된 <b>MOPJ–MB Spread 고시황 구간을 활용해 올해 11월물 및 12월물 각각 3만톤 중 60% 물량 진입 예정</b>. SKA/재무본부와 Hedge Scheme·실행 방향 논의, EE본부·Trading 본부와 실행 협의 예정이며 본부별 실행 프로토콜을 빠르게 확정해 기회를 적시 포착.",
 ['MOPJ-MB Spread','11월물','12월물','3만톤','60%','실행 프로토콜'])

add('pos','pos2','2026-07-27','7/27~7/31','prog',"시황 대응 협의체: 전쟁 양상·JKM·FEI·유가 모니터링, EE 소싱·G&P Optionality 검토",
 "시황 대응 협의체를 통해 전사 포지션 Action Plan 지속 논의. 미국–이란 전쟁 양상과 JKM·FEI·유가 등 주요 Index를 상시 모니터링하며 <b>EE본부의 소싱 Action과 G&P 본부의 Optionality 실행</b>을 전사 최적화 관점에서 검토 → 하반기 및 내년 수익 극대화 지원.",
 ['협의체','소싱 Action','Optionality','JKM','FEI'])

add('pos','pos3','2026-08-03','8/3~8/7','prog',"MOPJ–MB 상위 5% 구간 진입 시 즉시 실행토록 Trading본부에 Hedge 거래 요청서 발송",
 "11월물·12월물을 대상으로 <b>MOPJ–MB Spread가 역사적 상위 5% 구간에 진입할 경우 즉시 대응할 수 있도록 Trading 본부에 Hedge 거래 요청서 발송</b>. 금주에는 호르무즈 협상 재개에 따른 유가 급락으로 해당 구간을 벗어났으나 유가 급등 가능성도 상존해, Trading 본부와 시황 모니터링·진입 커뮤니케이션을 지속하며 Target 구간 도래 시 즉시 실행.",
 ['상위 5%','Hedge 거래 요청서','Trading본부','호르무즈 협상','유가 급락'])

add('pos','pos1','2026-08-03','8/3~8/7','prog',"전사 포지션 관리: 올해 본부별 잔여 포지션과 내년 신규 진입 물량 함께 검토",
 "미국–이란 전쟁 양상에 따른 시황 변화를 모니터링하며 전사 포지션 관리 및 Action Plan 수립 과제 추진 중. <b>올해 본부별 잔여 포지션 물량과 내년 신규 진입 물량을 함께 검토</b>해 하반기 및 내년 이후 전사 수익력 확대로 연결.",
 ['잔여 포지션','신규 진입 물량','내년','전사 수익력'])

add('pos','pos1','2026-08-10','8/10~8/14','plan',"하반기 경영층 관점 전사 포지션 Framework 수립 → Digital Cockpit화 방향 설정",
 "전사 포지션 정리 과제는 <b>하반기 경영층 관점의 전사 포지션 Framework를 수립하고 이를 Digital Cockpit화</b>하는 방향으로 준비. 상반기에는 전쟁에 따른 시황 변동성 대응에 주력했다면, 하반기에는 전사 포지션의 최적화 요소·리스크 요소·대응방안을 체계화해 경영층 의사결정 기준으로 활용. PDH Hedge는 간헐적 충돌이 반복되는 대치 국면이나 MOPJ–MB Target Spread(역사적 상위 5%)에 미도달, 유가 급등 시 적기 진입 준비.",
 ['Digital Cockpit','포지션 Framework','경영층 의사결정','Target Spread 미도달'])

add('pos','pos2','2026-08-17','8/17~8/21','plan',"9월·연말 종전 시나리오별 본부 대응방안 → 3Q CEO Progress 예정, Hedge는 12월물만",
 "경영층 관점 실물·포지션 Framework 수립 및 Digital Cockpit화를 준비하면서, 미국–이란 전쟁 대응은 LPG/LNG MI와 협력해 <b>9월 종전 및 연말 종전 시나리오별 본부별 대응방안</b>을 정리해 3Q CEO Progress에서 논의 예정. PDH Hedge는 미–이란 MOU 종료에 따른 유가 상승으로 진입 구간에 근접했으나 상위 5% 미도달, <b>11월물은 진입 후 대응 기간 확보가 어려워 제외하고 12월물만 대상</b>으로 조정.",
 ['9월 종전','연말 종전','3Q CEO Progress','12월물','MOU 종료'])

add('pos','pos3','2026-09-02','8/31~9/4','done',"9/2 Target Spread 도달 → SKA 12월 생산계획 25%(약 7천톤) Hedge 진입 완료",
 "<b>9/2 유가 급등에 따라 MOPJ–MB Spread가 Target Spread에 도달, SKA 12월 생산 계획의 25%(약 7천톤)에 대한 포지션 진입 완료</b>. 향후 진입 포지션 MtM 관리, '27년 1월물 신규 포지션 진입 검토, 기진입 포지션 Unwind Target 설정, SKA 합병 이후 페이퍼 손익 이관 방안을 준비해 Hedge 성과를 안정적으로 관리.",
 ['9/2','7천톤','25%','포지션 진입','MtM','Unwind Target','1월물'])

add('pos','pos1','2026-09-07','9/7~9/11','prog',"'26~'28 LPG·LNG Physical·Paper 포지션 판 정리 → Claude AI 대시보드 초안",
 "<b>'26~'28년 3개년 Eco Energy·G&P 본부의 LPG·LNG Physical·Paper 포지션을 종합한 판</b> 정리. 이를 ODIN 시스템, LPG/LNG MI 레터 등과 연계하고 AI(Claude Code)를 활용한 대시보드 초안 구축 중. 차주 사장에게 구축 방향을 논의하고 의견을 반영해 Digital Cockpit으로 고도화 → 경영층 의사결정 기준으로 활용.",
 ['3개년 포지션','Physical·Paper','ODIN','Claude Code','대시보드','Digital Cockpit'])

add('pos','pos1','2026-09-14','9/14~9/18','prog',"ODIN 연계 Claude AI 전사 포지션 대시보드 초안 구축 중, 별도 CEO 보고 예정",
 "'26~'28년 3개년 전사 LPG·LNG Physical·Paper 포지션 판을 바탕으로 <b>ODIN 시스템과 연계한 Claude AI 기반 전사 포지션 대시보드 초안</b> 구축 중. 별도로 사장 보고 후 의견을 반영해 전사 경영층 의사결정 기준으로 활용.",
 ['대시보드','ODIN','Claude AI','CEO 보고'])

add('pos','pos4','2026-09-14','9/14~9/18','plan',"울산 프로판 공급량 확대 → 인프라·선복·Optionality 고려 공급 우선순위 종합 검토 제기",
 "울산 프로판 공급량 확대에 따라 <b>공급 인프라 제약, 선복 운영, Optionality를 고려한 공급 우선순위</b> 등에 대한 종합 검토 필요성 제기. 전사 관점에서 인프라 안정성·자원 배분·수익 극대화가 동시에 가능한 최적 솔루션 도출을 위한 검토 추진.",
 ['울산 프로판','공급 우선순위','인프라 제약','선복','Optionality'])

add('pos','pos1','2026-10-05','10/5~10/9','done',"Claude AI 포지션 대시보드 CEO 피드백 반영 업데이트, SKA/GPS 대시보드 추가 구축",
 "'26~'28년 전사 LPG·LNG Physical·Paper 포지션 종합 <b>Claude AI 기반 대시보드를 CEO 보고 피드백 반영해 업데이트</b>. 기존 CEO/전사/EE/G&P 대시보드에 더해 <b>SKA/GPS 대시보드 추가 구축 중</b>. 향후 AX실과 MI 데이터 연계 자동화, 재무실과 전사 재무여력 분석 반영 방안을 논의해 CEO가 전사 경영 의사결정에 직접 활용 가능한 Digital Cockpit 구현.",
 ['대시보드 업데이트','SKA/GPS 대시보드','MI 연계 자동화','재무여력','Digital Cockpit'])

add('pos','pos2','2026-10-12','10/12~10/16','prog',"전쟁 전후 의사결정 Look-back 착수: 즉시 대응 성과 vs 장기화 손익 악화 점검",
 "미-이란 전쟁 대응 과정에서 <b>LNG/LPG 포트폴리오의 경쟁력과 Lessons-learned를 활용한 즉시 대응이 성과로 이어진 부분과, 역설적으로 전쟁 장기화에 따라 손익이 악화된 부분</b>을 함께 점검 중. 종전 이후 시나리오는 행캔(행복경영캔미팅) 반영 Index 전망을 바탕으로 검토하고 '27년 경영계획과 방향을 맞춰 정리 예정.",
 ['Look-back','Lessons-learned','전쟁 장기화','종전 이후 시나리오','행캔','2027 경영계획'])

add('pos','pos3','2026-10-19','10/19~10/23','done',"PDH Hedge 10월 말 '절대가 Hedge' 구조 전환, MOPJ 효과 제한 판단으로 포지션 정리",
 "PDH Hedge는 10월 말 원가(10월 MB)가 모두 Price-out되면 판가(11월 MOPJ)만 남는 <b>'절대가 Hedge' 구조로 전환</b>. 최근 동북아 프로필렌 가격은 FEI가 가격 결정을 주도하고 있어 <b>MOPJ가 프로필렌 가격 안정화에 효과적이지 않다는 판단 하에 포지션을 정리</b>하기로 하고, 전사 차원의 추가 수익 확보 방안 지속 검토.",
 ['절대가 Hedge','Price-out','FEI 주도','MOPJ','포지션 정리'])

# ───── 검증용 ─────
WEEKS = ['12/8~12','12/15~19','12/22~26','12/29~1/2','1/5~9','1/12~16','1/19~23','1/26~30','2/2~6','2/9~13','2/16~20','2/23~27',
 '3/2~6','3/9~13','3/16~20','3/23~27','3/30~4/3','4/6~10','4/13~17','4/20~24','4/27~5/1','5/4~8','5/11~15','5/18~22','5/25~29',
 '6/1~5','6/15~19','6/22~26','6/29~7/3','7/6~7/10','7/13~7/17','7/20~7/24','7/27~7/31','8/3~8/7','8/10~8/14','8/17~8/21',
 '8/31~9/4','9/7~9/11','9/14~9/18','10/5~10/9','10/12~10/16','10/19~10/23','10/26~10/30']

COVERAGE = ("[SKA/UPP 최적화] 40 / 43주 언급 — 언급 없는 주차: 12/8~12, 12/15~19, 12/22~26 (최적화실 신설 초기, SKA 과제는 12/29~1/2부터 등장). "
            "[전사 포지션 & 미-이란 전쟁 대응] 42 / 43주 언급 — 언급 없는 주차: 10/26~10/30 (10/19~23 PDH Hedge 포지션 정리 방침이 마지막 언급).")
