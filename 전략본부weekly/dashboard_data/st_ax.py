# -*- coding: utf-8 -*-
# AX 추진 (Trading AX·전사 AX) 업무 진척 데이터 (전략본부 Weekly '25.12/8 ~ '26.10/30 기준)
# k: done(완료/확정) prog(진행) plan(계획/예정) risk(이슈/리스크) mile(마일스톤) info(정보/시사점)

CAT = dict(
  id='ax', icon='🤖', name='AX 추진 (Trading AX·전사 AX)',
  sub='Trading AX·MI(개발·운영 적용) · 전사 AX 변화관리·AI Friday · CEO Agent·그룹 플랫폼 · AX 전략·과제 발굴(BCG AI Vision·본부별 과제)',
  what="회사 전체에 <b>AI를 어떻게 심을 것인가</b>를 설계하고 실제로 구현하는 일입니다. '25년 12월 신설된 AX추진실이 주관하며, 크게 네 갈래입니다. ① <b>Trading AX</b>: 트레이더가 쓰는 시황 분석 도구(MI, Market Intelligence)를 엑셀에서 AI 시스템으로 바꾸고(이벤트 해석·시나리오·Signpost 모니터링), 가격지표(Index) 조합의 반복 패턴에서 새로운 매매 기회(TAM, Trading Action Menu / Position Play)를 AI가 찾아내게 하는 것. 7/1 Beta Open 후 현업 검증 루프를 돌리며 품질을 높이는 중. ② <b>전사 AX 변화관리</b>: 임원·팀장·구성원 교육, AI 레터, AI Readiness 진단, 56개 팀 60명의 <b>AI Champion</b>, 매주 금요일 <b>AI Friday</b>, 팀별 조직 Agent 과제 등 '일하는 방식'을 바꾸는 활동. ③ <b>CEO Agent</b>: DY(SK디스커버리) 그룹 공통 플랫폼 위에 CEO 전용 비서 Agent(일정·회의록·경영분석·Trading AX 연계)를 만드는 것. ④ <b>AX 전략·과제 발굴</b>: BCG와 함께 'AI Vision 2030'을 수립(12/15~2/3)하고, 본부별 AX Needs를 들어 '26년 18대 AI 과제·KPI를 확정하고, '27년 추진계획을 세우는 일. 개발 파트너는 SK AX(구 SK C&C), 컨설팅은 BCG, 패턴 분석 방법론은 7월 이후 BSC로 인수인계됐습니다.",
  tracks=[('ax1','Trading AX·MI (개발·운영 적용)'),('ax2','전사 AX 변화관리·AI Friday'),('ax3','CEO Agent·그룹 플랫폼'),('ax4','AX 전략·과제 발굴 (BCG AI Vision·본부별 과제)')],
  status=[
   ("mile","<b>Trading AX(MI·Position Play) 주요 기능 운영환경 배포 완료</b>(10/23 PP 1차 배포 → 10/26주 1차 동작 확인). 개발조직 워크숍에서 신규 기능 확대보다 <b>분석 품질·사용성</b>에 집중하기로 결정. MI는 <b>12월까지 현업 주니어 분석가 수준</b>의 분석 품질 확보가 목표, PP는 과거 유사 시황 탐색에 날씨·기온 예측 데이터를 추가. 이후 현업의 수용·수정·기각 근거와 Back-testing, 대표 TAM 모의손익·RM 기준 충족 여부로 실거래 활용 가능성을 판단."),
   ("prog","MI·PP 데이터를 Claude와 연계한 <b>Self-Analysis 환경을 운영계로 확대</b>(10/19주). 트레이더가 정해진 화면 없이 과거·실시간 패턴과 시장 환경을 직접 조회·분석. 실물연계(TAM→실물 계약)는 대규모 신규 구축 대신 기존 PP·Self-Analysis 환경을 최대한 활용해 필수 기능만 선별 개발하는 방향. Trading RM은 파생평가손익 리포트 운영 배포·현업 테스트 중(10/12주)."),
   ("plan","<b>'27년 AX 추진계획</b>(행복경영 캔미팅 전 CEO 별도 보고): ① Trading AX 실사용 Value 창출 ② 조직 E2E 프로세스 재설계 ③ AI 활용을 위한 업무지식 자산화·E2E 재설계 방법론 정립·확산. 교훈은 'AI 기능 구현만으로는 사업 Value 창출에 한계, 개별 Agent 개선을 조직 단위 생산성 혁신으로 연결해야 함'. 본부별 E2E 후보과제를 현업과 사전 협의 중."),
   ("prog","<b>전사 AX</b>: AI Champion 56개 팀 60명(8월), AI Readiness 진단 432명(약 70%) 완료. 조직 Agent 과제정의서 52개 팀 73건 접수(9/16) → 10/2 상세설계 → 10월 구현 → 11월 과제 심사 → 12월 효과평가·우수사례 확산 일정. (9/14주 이후 전사 AX 세부 진척은 '27년 계획 중심으로만 보고)"),
   ("prog","<b>CEO Agent</b>: DY 공통 플랫폼 위에 구축. 9/23 CEO Letter 가 오픈, 10/16 유관자 대상 공통 Agent(일정·회의록·인사)+당사 특화 경영분석 1차 오픈 후 실무 테스트 중, 10월 마지막 주 CEO 보고 예정이었음. 특화기능 5개(Trading AX·경영분석·리더스 노트·CEO Letter·SHE). (10/12주 이후 Weekly 미보고)"),
   ("info","전략 골격: BCG AI Vision 2030(12/15~2/3)으로 North Star·로드맵 수립 → 3/30 전사 워크샵에서 '26년 <b>18대 AI 과제</b> 확정·KPI 세팅(4월) → Trading AI Phase 1(~6월 MI·PP 연계, 재무 성과 검증)/Phase 2(~10월 E2E 구축). 신규 TAM은 36만 개 Index 조합 분석으로 기존 Trading Menu 144개를 100% 재현하고 신규 후보 2,698개 중 <b>2개를 신규 Trading Menu로 확정</b>(5월), 추가 7개 모니터링(6월)."),
  ],
)

ITEMS = []
def add(c,t,d,w,k,title,body,tags):
    ITEMS.append(dict(c=c,t=t,d=d,w=w,k=k,title=title,body=body,tags=tags))

# ───────── 12월 ('25) ─────────
add('ax','ax4','2025-12-08','12/8~12','mile','BCG AI Vision 2030 착수 점검 (12/15~2/3, 6주): No Regret PoC 추가',
 "프로젝트 Scope·Level·Depth의 가시성을 위해 주차별 산출물과 종료 즉시 실행 가능한 결과물을 정의(As-Is/To-Be 워크플로우, AI 활용기회, <b>AI North Star</b> 구체화, 단계별 과제 로드맵·Quick-Win, 과제 정의서, SKG 특화 AX 운영 모델 등). 빠른 실행력 관점에서 <b>No Regret 과제의 PoC Task를 추가</b>해 범위 조정, 수행체계 검토 중. 'AI기반 TAM Upgrade 및 신규 TAM 도출' 과제는 Data 보유 현황·의사결정 engine 파악, 그룹 전문가 vs 외부 자문사 활용을 검토하며 조기 착수 준비.",
 ['BCG','AI Vision 2030','North Star','PoC','TAM','No Regret'])
add('ax','ax4','2025-12-08','12/8~12','prog','각 본부 주요 이해관계자 AX Needs 청취 착수 (EE·Trading·G&P 임원 미팅)',
 "Eco Energy·Trading·G&P본부 임원 미팅으로 본부/실별 주요 AX 과제 Needs 청취. 차주 기술인프라센터, 재무지원본부 임원 미팅 예정. (12/8 Weekly 서두: 최적화실/AX추진실 등 신설 조직은 각 본부 현황·니즈 파악과 과제 도출 중심으로 운영)",
 ['AX Needs','본부 인터뷰','Eco Energy','Trading','G&P'])
add('ax','ax4','2025-12-14','12/8~12','info','AX추진실 현안: UGPS IT시스템 정기 PM 12/14(일) — 15개 시스템',
 "UGPS IT시스템 정기 PM(Preventive Maintenance) 12/14(일) 진행. 대상은 그룹웨어·네트워크·인증관리 등 <b>15개 시스템</b>, Windows 보안 업데이트·S/W 취약성 Patch 후 서비스 재기동 및 정상작동 점검.",
 ['UGPS','IT PM','정기 점검','AX추진실'])
add('ax','ax4','2025-12-15','12/15~19','prog','AI Vision 2030: No Regret PoC 병행 확정 — LNG MI 고도화·LNG TAM 2과제',
 "AI Vision 2030은 'AI North Star 정의 → 단계별 로드맵 → 즉시 실행 과제 도출'을 목표로 6주간 추진, 단기 실행 검증(No Regret PoC)을 전제로 중장기 전략을 병행. 단순 BCG 산출물에 그치지 않고 Core 업무의 AI 적용 Feasibility를 빠르게 검증하는 PoC를 SK AX와 병행. PoC 과제는 ① <b>AI기반 LNG MI 고도화</b>(As-Is MI 엔진 분석·현업 인터뷰, 속도 개선·Event/Sentimental 변수 추가·AI 기반 Market Insight), ② <b>LNG TAM Upgrade·신규 TAM 도출</b>(예측·자동매매가 아닌 의사결정 지원 도구로 AI 역할 정의, 단계적 PoC로 신뢰 확보 후 확장). 수행체계: TAM Insight는 G&P 가스솔루션실, TAM 구조 분석은 BCG, Data 분석·Modeling은 그룹 전문가.",
 ['AI Vision 2030','PoC','LNG MI','TAM','SK AX','BCG','가스솔루션실'])
add('ax','ax4','2025-12-22','12/22~26','done','전 본부 AI 활용 기회 발굴 인터뷰 완료 — AI는 의사결정 구조 Re-design 방향으로',
 "Eco Energy·Trading·G&P·전략·재무·기술인프라·UGPS 전 본부 대상 핵심 가치창출 원천 정의 및 AI 활용 기회 발굴 인터뷰 완료. AI를 단순 업무 보조 도구를 넘어 <b>의사결정·판단 구조 자체를 재설계(Re-design)</b>하는 방향으로 적용하는 것이 근원적 경쟁력 제고의 핵심임을 재확인. 향후 Biz Impact 기준으로 과제 구체화·선택과 집중. '26년 단기 실행 핵심인 '트레이딩 중심 VCO(Value Chain Optimizer)'와 'TAM(Trading Action Menu) AI' 로드맵 구체화 중.",
 ['인터뷰','Re-design','VCO','TAM AI','Biz Impact'])
add('ax','ax4','2025-12-29','12/29~1/2','plan',"'26년 10월 VCO·TAM AI 실질 성과 창출 목표 — 결과/실행 중심 AX 추진계획 1/8 보고 예정",
 "'26년 10월 중 '트레이딩 중심 VCO'와 'TAM AI'의 <b>실질적 성과 창출</b>을 목표로, 결과/실행 중심의 AX 추진 방향과 실행계획을 정리해 1/8(목) 전략본부 Weekly에서 보고 예정. (12/26 전략본부 워크샵 Follow-up)",
 ['VCO','TAM AI','10월 목표','실행계획'])

# ───────── 1월 ─────────
add('ax','ax1','2026-01-05','1/5~9','plan','Trading AI 목표 Image·\'26 마일스톤 수립: 상반기 v1.0 적용 목표',
 "AI Vision 2030 핵심 과제 'Trading AI'의 목표 Image 설계 및 '26년 실행 마일스톤 수립. <b>'26년 상반기 중 Trading AI v1.0 적용</b>을 목표로 차주 Trading 핵심 Process 분석 착수. 별도 Track으로 LNG 영역 추가 수익 기회(TAM) 발굴을 통한 조기 성과 창출 추진.",
 ['Trading AI','v1.0','마일스톤','TAM'])
add('ax','ax1','2026-01-12','1/12~16','mile','Trading AI v1.0·LNG MI 시스템화 개발 착수 (1/19, w/ SK AX)',
 "AI Vision 2030과 Align해 상반기 내 Trading AI v1.0 완료 목표로 개발·구현 착수(금주 Week 0: 작업계획·상세 일정). 트레이더의 사고 흐름·업무 프로세스·의사결정 참조 데이터·판단 기준을 <b>Ontology 형태로 구조화</b>하고 AI 적용 영역 상세화, SK AX가 1/19부터 단계적 참여해 Agent 설계 진입. 기존 <b>Excel 기반 LNG MI 수급모델의 System화(Phase 1)</b>도 1/19 착수: 약 5만 개 데이터셋 수기 관리, 수급모델 1회 분석에 3~4일 소요되던 구조를 개선해 3월 중 시스템 구축 목표.",
 ['Trading AI','LNG MI','Ontology','SK AX','수급모델','5만 데이터셋'])
add('ax','ax4','2026-01-12','1/12~16','plan','1/19(월) AI Vision 워크숍 예정 — North Star 합의·본부별 담당 명확화',
 "AI North Star 합의, '26년 추진 AI 과제의 본부별 담당 명확화, 각 본부 대상 AI 구축·검증·적용 공감대 형성을 목표로 1/19(월) AI Vision 워크숍 진행 예정.",
 ['AI Vision','워크숍','North Star'])
add('ax','ax1','2026-01-19','1/19~23','prog','SKAX 7명 투입 LNG MI·Trading AI 개발 착수: 6월 모의 트레이딩 Pilot 목표',
 "SKAX와 협업해 LNG MI 및 Trading AI 개발·구현 착수(<b>SKAX 총 7명 Full-time</b>). [Trading AI] 2월 1주까지 AI 활용 영역(Forward Curve 시뮬레이션 등) 컨셉 UI/UX로 가시성 확보 및 LNG 트레이더 현업 검증, 3월 Coding 착수, <b>6월 모의 트레이딩 Pilot 오픈</b> 목표. [LNG MI] 3월까지 엑셀 모델 시스템화(분석 시간 5시간→수분), 6월까지 AI 예측모델 구축. 단순 예측값이 아닌 설명 가능한 'Why(인과관계)'·'요인별 기여도(Impact)' 수치화, 시나리오별(On/Off) 시뮬레이션을 필수 기능으로 시스템화. 1/19 AI Vision 워크샵 결과 바탕으로 최근 의사결정 사례를 Use case화해 '26년 AI 과제 구체화 중.",
 ['SKAX','Trading AI','LNG MI','모의 트레이딩','Forward Curve','Use case'])
add('ax','ax2','2026-01-19','1/19~23','plan','AI Literacy 강화 및 변화관리 방안 수립(案) 착수 (w/ 기업문화실)',
 "AI 및 A.Biz 활용 확산을 목표로, 실행력을 높이는 관리 장치와 명확한 인센티브를 결합한 변화관리 전략 추진 중(w/ 기업문화실).",
 ['AI Literacy','변화관리','기업문화실','A.Biz'])
add('ax','ax1','2026-01-26','1/26~30','prog','Trading AI To-Be Image·Quick-Win 2과제: LNG spec. 자동화·신규 TAM',
 "Quick-Win ① <b>실시간 LNG spec. 기회 포착 및 손익 범위 제안 의사결정 프로세스 자동화</b>: 트레이더가 수백 개 spread 변화를 수기 분석하는 Pain point를 AI로 자동화해 추가 spec. 수익 기회 발굴 지원. ② <b>타 Commodity TAM 활용 신규 TAM 발굴 AI</b>: Oil·LPG Commodity TAM과 당사 BM을 결합. 시스템 구현 관점에서 실시간 LNG Spec. 기회 포착용 데이터 분석을 착수, 차주 초기 index 데이터 분석 결과를 내부 리뷰 후 사업본부와 논의 계획. (1/19부터 SK AX와 협업 개발 중)",
 ['Trading AI','Quick-Win','LNG spec','TAM','Oil','LPG'])
add('ax','ax2','2026-01-26','1/26~30','plan','전사 AI Literacy 3단계: Playground → 인증제(6월/9월) → 해커톤(6월~)',
 "전사 AI 역량 내재화를 위해 ① <b>Playground 확대</b>: A.Biz(사내 Legacy 연계) + Gemini/GPT 등 SOTA 서비스 Dual 운영, ② <b>AI 인증제</b>(6월 Level1 / 9월 Level2): 당사 데이터·업무 기반 실습 교육과 인증으로 역량 객관성 확보(mySUNI 컨텐츠, SK AX AI Talent Lab 등 그룹 Asset 활용), ③ <b>AI Impact 2026</b>(사내 해커톤, 6월~): 인증자 대상 해커톤 → 현업 적용 → 성과 보상의 '자기주도 AX 실행과 문화 확산'. 차주 Weekly 보고 예정.",
 ['AI Literacy','Playground','인증제','해커톤','mySUNI','Gemini'])

# ───────── 2월 ─────────
add('ax','ax1','2026-02-02','2/2~6','prog','신규 TAM 발굴: 과거 유사 시황 Event·결과 Data 규명 (SK AX 6명+BCG)',
 "Trading AI 기반 TAM 기회 발굴을 위해 '과거 수백 번의 유사 시장 상황에서 실제 어떤 이벤트가 있었고 어떤 결과가 발생했는지'를 Data로 규명하는 분석 진행. 트레이더마다 동일 시그널(예: JKM–TTF 스프레드)의 해석과 진입 시점이 달라 <b>표준 알고리즘화에 한계</b>가 있음을 인식, 과거 데이터로 검증할 가설 후보를 선별해 반복 작동한 시장 상태(State)와 의사결정 규칙(Rule)을 도출 중. SK AX 분석가 6명이 BCG 에너지 전문가와 과거 Index 데이터 심층 분석. 별도로 Trading AI의 Input/Output 정의·E2E Workflow 'How-to 구체화'에 집중.",
 ['TAM','State','Rule','SK AX','BCG','JKM-TTF'])
add('ax','ax1','2026-02-02','2/2~6','prog','LNG MI 플랫폼 엑셀 → Python 엔진 전환 (3월 말 검증 목표)',
 "엑셀 모델의 성능 한계를 극복하기 위해 Python 엔진 기반 처리 구조로 전환 추진. 개발자 단위 테스트 → MI팀 AS-IS 산출 결과와 New 시스템 결과 대조 → 실무 시나리오 기반 검증의 단계적 검증 체계를 합의해 결과 정합성 확보 중.",
 ['LNG MI','Python','엔진 검증','정합성'])
add('ax','ax1','2026-02-09','2/9~13','prog','MI 플랫폼 How 상세화·Position Play 가설 분석 (2/23 CEO 보고 준비)',
 "[MI] 시장 이벤트 수집으로 MI 모델에 업데이트할 핵심 Parameter를 자동 제안·반영하는 구조, 수급 모델–시장 가격 간 괴리(<b>CME Gap</b>) 원인을 글로벌 이벤트·자사 정보와 연결해 분석, 데이터 수집→파싱→Impact 도출→신호/소음 구분 전 과정을 트레이더 피드백 기반 증강 체계로 설계. [Position Play] '가설 검증 기반 분석'과 'LPG/LNG/Brent Index 간 상관관계·패턴 분석'으로 TAM 발굴 Data 분석 중(JKM '26 1·5월 Spread, JKM–TTF 12월물 Spread, JKM–FEI 10월물 등 현업이 검증 요청한 가설). 2/23 보고 예정.",
 ['MI','CME Gap','자가 학습','Position Play','JKM-TTF','JKM-FEI'])
add('ax','ax4','2026-02-09','2/9~13','mile','WEGO 2.0 개발 프로젝트 착수 (\'26.3~10월, 9.2억, SK AX) — EE본부 중점 AI 과제',
 "프로젝트 기간 '26.3~10월, 총 비용 <b>9.2억</b>, 개발 파트너 SK AX. 프로판 Hub(거점) 충전소 중심 공동 수송 운영·정산을 시스템화하고, 수요처 Small Bulk의 잔량·패턴 기반 주문 자동화로 프로판 판매 물량 확대 기여 목표. EE본부의 금년도 중점 AI 과제로 현업 Needs에 부합하는 사업 성과 창출 과제로 집중.",
 ['WEGO 2.0','EE본부','SK AX','9.2억','Small Bulk','공동 수송'])
add('ax','ax2','2026-02-16','2/16~20','plan','AI Literacy 일정 확정: 2/27 강의 시작, 임원 교육 4회, Gemini Testbed 4월',
 "AX추진실·기업문화실 대상 AI 이론 강의를 2/27 시작, 보완 후 3월 전 구성원 대상 open 계획(w/기업문화실). <b>임원 AI 교육 3~6월 총 4회</b>(3/28·4/11·5/30·6/13 토요일, mySUNI 리소스). 경영진 AI 활용: 그룹 보안가이드 참고해 <b>Google Gemini Enterprise</b> 도입 'Quick-win Testbed' 4월 내 선제 오픈. TDS(인사평가) AI는 당사 고유 리더스노트 기반 자체 구축(4월 Pilot 목표). 별도로 Excel 기반 LNG MI 모델 시스템화는 3월 말 Open 목표(5시간→5분 이내).",
 ['AI Literacy','임원 교육','Gemini Enterprise','TDS','리더스노트','mySUNI'])
add('ax','ax1','2026-02-23','2/23~27','done','MI·Position Play 상세 설계 CEO 보고 완료: PP 발굴 최우선, 5개 Block',
 "MI와 Position Play 영역 상세 설계 진행 및 사장님 보고 완료. 신규 TAM 발굴 및 '26년 Position Play 기회 포착을 최우선으로 진행하고, 실물 연계 신규 TAM·RM 등 <b>5개 Block</b>의 상세 설계와 개발 병행. '재무적 성과' 조기 창출 기여를 목적으로 LNG 'Position Play' 발굴을 최우선 과제로 추진.",
 ['Position Play','MI','5개 Block','RM','CEO 보고'])
add('ax','ax4','2026-02-23','2/23~27','prog','정보보호: 보안 수준 향상 계획 — 그룹 진단 Framework 125개 R&R 정리',
 "그룹 보안진단 Framework 125개 중 정보보호담당과 AX추진실의 R&R을 명확화하고, IT 생애주기 전반에 보안 내재화 관점의 실행계획 점검 완료. AX추진실–정보보호담당 실무 협의체를 정례화해 보안 수준 상시 점검 예정.",
 ['정보보호','보안진단','125개','AX추진실'])

# ───────── 3월 ─────────
add('ax','ax1','2026-03-02','3/2~6','mile','MI 수급모델 시스템화 단위개발 완료, 사용자 검증 진입: 5시간 → 15분',
 "Trading AI의 핵심 기반인 LNG MI 수급모델 시스템화 단위개발 완료, 사용자 검증 단계 진입(3월 내 완료 목표). 테스트 실행시간이 <b>5시간에서 15분</b>으로 단축됐고 로직 최적화 후 Cloud 서버 이관 시 5분 내 실행 예상. AI를 활용한 <b>MB/FEI Spread Position Play</b> 방법론 구체화 중(w/ G&P 본부), 사람(데이터분석가) 중심 분석을 AI Model로 빠르게 전환 계획.",
 ['MI','수급모델','15분','MB/FEI','Position Play','G&P'])
add('ax','ax2','2026-03-02','3/2~6','prog','AI 인증제 파일럿 검토·임원 교육 준비, Gemini Enterprise Playground 구축',
 "전사 AI 활용 기준 수립을 위한 AI Literacy 인증제 파일럿 검토와 임원 교육 준비 중(SK가스 사업·직무를 반영한 맞춤형 인증 문항 개발). 임원 대상 AI 교육은 3~4월 일정 확정, 이를 위한 Gemini Enterprise Playground 환경 구축 진행 중.",
 ['인증제','임원 교육','Gemini Enterprise','Playground'])
add('ax','ax1','2026-03-09','3/9~13','plan',"'26 Trading AI 목표: Phase 1(~6월) MI·PP 검증, Phase 2(~10월) E2E",
 "'26년 Trading AI 목표를 <b>Phase 1(~'26.6) LNG MI·Position Play 연계/구축 및 재무적 성과 창출 가능성 검증</b>, <b>Phase 2(~'26.10) LNG Trading AI E2E 구축</b>으로 설정하고 AX추진실/BCG/SK AX 역할 분담 및 비용 구체화 중(BCG·SK AX 선투입 개발 진행). 구축비용은 성과 극대화를 위해 구축사업자와 Value Based Pricing 합의 예정. 6월과 10월 경영진 시연 목표. 월별 마일스톤: 3월 엑셀MI 속도개선·Spread 패턴 알고리즘/Agent, 4월 Input Data 자동 수집·Event 임팩·신호/소음 구분·Spike 포착, 5월 Parameter 시나리오 제안·MI-PP 연계 검증, 6월 수급모델 vs CME 커브 Gap 해석·북미 LPG 재고 예측·LNG TAM Spread Estimator. Milestone별 품질기준·평가방식 사전협의, Agile 개발, 그룹 기개발 MI 플랫폼 레버리지. MI 수급모델은 4개 모듈 중 Demand/Supply 2개 모듈 테스트 완료, 차주 Trading/Output 테스트.",
 ['Phase 1','Phase 2','E2E','Value Based Pricing','BCG','SK AX','마일스톤'])
add('ax','ax1','2026-03-16','3/16~20','prog','MI 상세설계 4개 축 + Position Play 14개 Index 조합 Clustering 패턴 탐지',
 "[MI] 3월 상세설계 완료 목표로 ① 데이터 정합성 ② 가격 전망 고도화 ③ 의사결정 지원 ④ 단기 성과 창출 4개 축 진행. 트레이더 Use-case 기반 기능 검증 확대(예: 당사 포지션에 영향 주는 시장 이벤트 발생 시 24x365 실시간 Alert 가능 여부), 'MI–당사 포지션–RM'이 연결된 실행형 의사결정 process로 develop. [TAM-Position Play] <b>총 14개 Index</b>를 조합해 Clustering 기반 패턴 탐지 수행(JKM·MB(C3) 이종 월물, JKM-FEI, HH-MB(C3), Brent-JKM, Brent-MB C3, TTF-HH, CP(C3)-MB(C3) 분석 완료, 유의미성 검증 중). 3월 내 전체 조합 통계 패턴 도출, 4월 내 검증 방법을 알고리즘화해 전수 패턴검사·유의미성 분석 완료 목표.",
 ['MI','14개 Index','Clustering','Position Play','24x365 Alert','RM'])
add('ax','ax4','2026-03-23','3/23~27','mile','본부별 AI 과제 사전 Workshop (3/23~25, 5개 본부+UGPS): 대표 과제 정리',
 "3/23~3/25 5개 본부·UGPS와 사전 Workshop으로 본부별 AI 과제·추진방향 의견 청취 및 Vision 수립 반영 완료. 3/30 전사 워크샵에서 대표 과제의 목적·기대효과·주요 내용 논의 및 전사 AX 공감대 형성 목표. 본부별 과제: ① <b>Eco Energy</b> Wego 2.0 기반 공급망 최적화·무인화 ② <b>Trading</b> LNG 중심 Trading AI 검증 후 LPG 확장, Shipping 과제는 후순위 ③ <b>G&P</b> 시나리오 기반 Trading 활용 MI로 진화, TAM 과제 명확화 필요 ④ <b>재무</b> 유동성 시나리오 기반 자금운용 AI·전사 손익 통합 관점 ⑤ <b>기술인프라</b> 데이터 가용성 기반 우선순위 재정립·투자 타당성 검토 ⑥ <b>UGPS</b> 전력가 자동화 중심 1단계, 센서 기반 Process 관리 검토.",
 ['AI Vision 2030','본부별 과제','Wego 2.0','UGPS','재무 AI','전사 워크샵'])
add('ax','ax1','2026-03-23','3/23~27','prog','Position Play: Index 14→17개(JCC·Conway·MOPJ)·월물 M+4~M+24 확장',
 "목요일 보고 이후 차주부터 분석할 TAM 후보군 도출 기준을 정립하고 Index·월물을 확장해 TAM 후보 발굴 중. <b>Index는 14개에서 17개로 확장(JCC, Conway, MOPJ 추가)</b>, <b>월물은 기존 Y+1에서 M+4~M+24까지 확장</b>. 4월 내 패턴 발굴·시황 해석을 AI化하는 Agent 구현 목표.",
 ['Position Play','17개 Index','JCC','Conway','MOPJ','월물 확장'])
add('ax','ax2','2026-03-28','3/23~27','done',"임원 AI 교육 1차 진행(3/28): 'AI로 일하는 조직을 만드는 리더' 4주 과정",
 "임원 대상 1차 교육 3/28 진행(w/기업문화실). 단순히 AI를 활용하는 리더를 넘어 <b>'AI로 일하는 조직을 만드는 리더'</b>로의 전환을 목표로 '개인 활용 → 업무 위임 → Agent 고도화 → 조직 안착'의 단계적 여정으로 설계. 1주차 AI로 달라지는 리더의 업무 방식, 2주차 업무를 AI에 위임하는 방법, 3주차 Agent 고도화 및 조직 도입 판단, 4주차 조직 적용 판단.",
 ['임원 교육','AI Literacy','Agent','기업문화실'])
add('ax','ax4','2026-03-30','3/30~4/3','mile',"3/30 AI Vision 2차 워크숍: '26년 18대 AI 과제 확정, Master Plan·KPI 착수",
 "3/30 Vision AI 2차 워크숍을 통해 <b>'26년 18대 AI 과제 확정</b>, 그룹 가이드라인에 부합하는 AX Master Plan 및 KPI 수립 중. Staff 생산성 제고를 위해 회계 AI 개념설계 착수(e-Card/SAP 연계 회계 AI Assistant: 챗봇 회계 문의 대응, 전표 계정·증빙 검토 자동화, 분기별 전표 검토·결산 검증, 역분개 누락 점검·가수금 매칭 제안). 보안상 안전한 AI Playground(Gemini Enterprise)는 차주 임원 안내 후 전 구성원으로 확대.",
 ['18대 AI 과제','AX Master Plan','KPI','회계 AI','Gemini Enterprise','SAP'])
add('ax','ax1','2026-03-30','3/30~4/3','done','LNG 수급모델 시나리오 테스트 47개 전량 Pass: 4/6부터 MI팀 실무 적용',
 "LNG 수급모델 시나리오 테스트(47개) 전량 Pass 완료, 시스템화·Runtime 개선 완료. 차주 C-team Weekly(4/6)부터 MI팀이 개선된 수급모델로 기초자료 직접 산출. 사용자 편의성 개선 병행, 펀더멘탈 데이터(Bloomberg 등) 수집 자동화용 데이터 리스트 정의·소스 확보 방안 확정 중. [Position Play] MI 플랫폼 연동 체계하에 인덱스(+3개)·월물(Y+0~Y+2) 조합 확대 분석 및 구조적 기회 포착 알고리즘 구현 중, 차주 AX 구현 결과물 품질·성능 테스트. 6월 Phase 1 목표 변동 없음.",
 ['수급모델','47개 시나리오','MI팀','Bloomberg','Position Play'])

# ───────── 4월 ─────────
add('ax','ax1','2026-04-06','4/6~10','prog','MI: S&P·WoodMac 연계, Platts 라이선스 확보 / PP 기회 탐지 기능 개발 완료',
 "[MI] S&P Global, WoodMac 등 핵심 데이터 연계 진행 및 <b>Platts LNG Daily 라이선스 확보</b> 완료, 차주 시나리오 연계 파라미터 등 고난이도 요구사항 검토. [Position Play] Spread 패턴 기반 구조적 포지션 기회 탐지 기능 개발 완료·테스트 환경 전환. 발굴된 TAM의 펀더멘털/MI 해석력 보완 요구에 대응해 Index별 드라이버(재고·날씨·수요공급)와 Spread 패턴 간 상관성을 정량 분석하고 LLM 활용 정보지·시황 분석을 병행해 현업 수용도 확보. RM 고도화는 재무/트레이딩 현업 인터뷰 착수.",
 ['S&P Global','WoodMac','Platts','Position Play','LLM','RM'])
add('ax','ax4','2026-04-06','4/6~10','prog','18개 AI 과제 KPI 초안 수립, 재무 이상거래 탐지·EE SR AI Assistant 착수',
 "전사 18개 AI 과제에 대한 KPI 및 Formula 초안 수립 완료, 차주 각 본부와 논의 착수. 재무본부 내부통제(이상거래 탐지) 및 Eco Energy <b>SR AI Assistant('26.10 오픈 목표)</b> 등 주요 function 과제 착수. 생성형 AI(Gemini, M365 Copilot 등) 전사 확산에 맞춰 운영 정책 수립, 안전성·실효성을 동시에 확보한 AI 도입 환경 구축 중. (4/13주) 18개 본부별 과제 KPI 세팅 완료, HR/재무 AI 고도화 및 전사 변화관리 추진 중.",
 ['18개 과제','KPI','이상거래 탐지','SR AI Assistant','M365 Copilot','Gemini'])
add('ax','ax1','2026-04-13','4/13~17','prog','MI Event 해석 Agent(51%) 설계, 2017년 이후 RAG 확정 / PP 패턴 발굴 100%',
 "[MI] AI 기반 시장 이벤트 해석 Agent(진척 51%)·시나리오화 Agent(23%) 핵심 모듈 설계. Event Source·RAG 연계 확정: 뉴스(Reuters), 리포트(Platts·Woodmac 등), 내부 이메일을 Source로 <b>2017년 이후 데이터</b> 축적해 AI 학습용 RAG 활용. 핵심 로직(Driver Tree) 설계 완료. [Position Play] Index 조합 기반 통계적 패턴 발굴 100% 완료, 통계 기반 TAM 전략 추천(48%)·Spike 모델 구축 중. 수익 확대를 위해 <b>TAM 발굴 기준을 $0.5/mmbtu로 확대</b>, Spike 탐지 기준 수립('60일 이동평균 표준편차 3시그마를 1일 이상 이탈 후 60일 내 회귀'). 4월 내 전사 RM 기능 As-Is 분석 완료 목표. (최적화실의 PDH 프로판–프로필렌 Hedge 전략도 새로운 TAM으로 AI 활용하도록 AX실과 협업)",
 ['Event 해석 Agent','RAG','Reuters','Platts','Spike','$0.5/mmbtu','Driver Tree'])
add('ax','ax1','2026-04-20','4/20~24','prog','MI Event 구조화 Agent 1차 구현 / PP 전용 Agent 별도 구축 확정',
 "[MI] Event 구조화 Agent의 Platts Report 1차 구현 완료, Event 기반 시나리오 생성·Signpost 설계·구현 진행(시나리오화 Template·Lifecycle 설계 완료), UX/UI 상세화·API 개발 병행. [Position Play] Fundamental 정량 해석과 MI 정성 해석을 하나의 모듈로 통합(예시: MB C3/C4, DEC/DEC). PP는 정량 데이터 기반 구조적 해석, MI AI는 이벤트 강도·영향도 평가로 쓰임새가 달라 <b>PP 전용 Agent 별도 구축</b> 확정(Fundamental 해석·MI 이벤트 해석·챗봇). 신규 발굴 TAM(MB C4-C3, FEI Dec-Dec 우상향, FEI-MB, FEI-MOPJ, TTF-HH, JKM-JKM Time Spread, NWE-Naphtha) 해석을 트레이더로부터 검증받아 AI 기반 TAM 해석 체계 확보.",
 ['Signpost','시나리오 Lifecycle','PP Agent','FEI Dec-Dec','TTF-HH','NWE-Naphtha'])
add('ax','ax2','2026-04-20','4/20~24','plan','구성원 3트랙·팀장 AI 교육 기획, 위클리 AI 레터 4/29 첫 발송',
 "구성원 교육은 <b>정보 탐색·보고서/기획안 작성·반복 업무 효율화 3개 트랙</b>으로 구체화, 5월 마지막 주부터 주 1회 3주간 운영. 팀장 교육은 6월 말 P&C팀 팀장 워크숍의 일부로 mySUNI 팀장 과정·성과관리 주제 중심 약 3시간 구성. 전사 AI 활용 확산을 위한 <b>위클리 AI 레터</b>는 단순 트렌드가 아닌 구성원이 업무에서 바로 따라 할 수 있는 실무형 콘텐츠로 기획, 4/29 1회차 발송 목표.",
 ['구성원 교육','팀장 교육','AI 레터','P&C','mySUNI'])
add('ax','ax1','2026-04-27','4/27~5/1','mile',"MI 시나리오 Agent 시연(Ras Laffan 폭격·엘니뇨) / PP 2,700개 중 250개 선별",
 "MI는 Event 수집/해석, 시나리오 플래닝·Signpost 설계를 완료하고 Agent로 구현 중. 실제 발생했던 <b>'카타르 Ras Laffan 폭격'(전쟁 리스크)·'엘니뇨'(기후 리스크)</b>에 대한 AI 시나리오 플래닝을 Agent로 시연, 보완점은 있으나 MI팀 Needs에 부합함을 확인. Position Play는 FEI Dec-Dec, FEI-MB C3 등은 AI가 패턴 발생 요인을 충분히 해석했으나 JKM-JKM, TTF-HH 등 일부 조합은 해석력 부족 의견. 통계적으로 발굴된 약 <b>2,700개 패턴 중 반복성·일관성 높은 250개</b>를 우선 선별해 AI 펀더멘털 해석, 미흡 패턴은 유형별 분류·개선 영역 도출.",
 ['Ras Laffan','엘니뇨','시나리오 플래닝','2,700개 패턴','250개','해석력'])

# ───────── 5월 ─────────
add('ax','ax1','2026-05-04','5/4~8','prog','MI–PP–RM 통합 아키텍처·Multi-LLM(Claude·GPT·Gemini) 적용',
 "MI는 시황 변화 기반 시나리오 플래닝 기능을 플랫폼에 구현 중(차주 1차 완료). 단순 효율화를 넘어 <b>'MI–PP(Position Play)–RM'</b>으로 연결되는 시나리오 기반 의사결정 모듈로서 통합 아키텍처 기반 개발, Biz Ontology·Data Flow 시각화 병행. 기술적으로 Claude·GPT·Gemini 등 상황별 최적 LLM을 선택 활용하는 <b>Multi-LLM 체계</b> 적용 중. PP는 약 2,700개 신규 TAM 조합 AI 구조적 패턴 분석 차주 완료 목표. 차주 보고에서 TAM의 Fundamental/MI 해석 성능, 전쟁으로 붕괴된 패턴 중 회복 가능성 높은 케이스, 연내 진입 가능한 Trading 기회·진입/청산 전략 등 신규 TAM 발굴부터 Trading 옵션 도출까지 End-to-End Output 설명 계획.",
 ['MI-PP-RM','Biz Ontology','Multi-LLM','Claude','E2E'])
add('ax','ax1','2026-05-11','5/11~15','mile','PP 36만 개 조합 분석: 기존 TAM 144개 100% 재현, 신규 Trading Menu 2개 확정',
 "Position Play는 <b>36만 개 Index 조합 분석</b>을 통해 기존 당사 Trading Menu 144개를 100% 재현하며 방법론 신뢰성 확인, 기존 범위 외 <b>2,698개 신규 Trading Menu 후보</b> 발굴. 통계적 반복성·펀더멘털 설명력·Signpost 관측 가능성·트레이더 검토를 모두 충족한 <b>2개 조합을 신규 Trading Menu로 확정</b>(실제 전환 가능한 후보만 엄격 선별). 나머지 2,696개도 AI로 TAM 가능 여부 분석 중. [MI] 중요 이벤트 자동 선별, 이벤트별 3~7개 What-if 시나리오 생성, 시나리오별 핵심 가정·초기 확률·추적 Signpost를 AI 추천으로 도출하는 구조 구축. 기사·리포트·시장 데이터 모니터링으로 Signpost 관측·시나리오 가능성 업데이트 기능 개발 중, 수급모델 연동 시나리오별 가격 전망은 6월 3주 완료 목표.",
 ['36만 조합','144개','2,698개','신규 Trading Menu','What-if','Signpost'])
add('ax','ax1','2026-05-18','5/18~22','prog','MI 담당자 Ontology 화면으로 Prompt 직접 보정 / PP 해석력 병목 데이터 확보',
 "[MI] UX 방향성을 MI팀과 합의, MI-Record Pipeline 자동화·이벤트 구조화·시나리오 Agent 개발 병행, 6월 말 현업 사용 화면안 확정. <b>MI 담당자가 Ontology 관리 화면을 통해 MI Prompt를 직접 점검·보완</b>하는 구조로 협업(Biz Know-How를 현업이 검증·보정해 Prompt·Ontology에 재반영). [PP] 추가 TAM 확대의 핵심 병목은 2,700개 후보의 펀더멘털 해석력 확보 → ① 부족했던 Naphtha 펀더멘털 데이터 확보(완료) ② 과거 Platts Report·MI 이벤트 데이터 2017~2022년 추가 확보(완료) ③ 트레이더 검토 의견을 축적·재활용하는 Chatbot 기반 피드백 Loop 도입 검토.",
 ['Ontology','Prompt','Naphtha','Platts','피드백 Loop','해석력'])
add('ax','ax1','2026-05-25','5/25~29','prog','MI Event·Impact Pipeline 실서비스 전환(6/2~), PP Fundamental Agent',
 "[MI] Event 생성·정성적 Impact 분석 Pipeline을 실서비스용으로 전환해 6/2 개발 반영, Reuters·Platts(6/9) → Woodmac(6/12) → Email·시나리오화·모니터링 Agent 6/19 반영 목표. MI 이벤트 해석·수급모델·시나리오 생성·모니터링 Agent를 상호 연결해 Trading 의사결정 속도·품질 기반 마련, 차주 실서비스 Pipeline 반영과 6월 말 사용자 활용을 위한 서버 보안점검. [PP] 인덱스별 Fundamental Driver·Data Source 현황 업데이트, <b>Fundamental Agent 개발</b>, 반복적·실시간 패턴 및 Spike Logic 업데이트 완료. 모니터링/실시간/반복적 Spread 분석 기능 개발 완료, 기대수익 수식 정교화·Z-score/Spread Toggle·단위당 기대수익 등 UX 피드백 반영 중.",
 ['Pipeline','Reuters','Woodmac','Fundamental Agent','Spike','Z-score'])

# ───────── 6월 ─────────
add('ax','ax1','2026-06-01','6/1~5','prog','Trading AI 진척률 79%: 추가 TAM 후보 7개, 7월 실행 전환 준비(RM Policy 등)',
 "[MI] Event 생성·Impact 분석 파이프라인 개발 완료, 실서비스 전환 준비 완료. 데이터 연계 자동화 파이프라인 배포, 현업 피드백 기반 UI 개선. <b>전체 진척률 79%</b>, 7월 사용자 활용 위해 운영 준비·보안·네트워크 점검. [PP] 모니터링·실시간·반복적 Spread 분석 기능 테스트 환경 배포·안정화. 신규 TAM 확정 2개 외 <b>추가 7개를 금년 모니터링 대상</b>으로 검토(TTF-HH Y+1 1월, JKM-FEI Y+1 9월, HH-MB(C3) Y+1 1월, MB Y+1 1월–Brent Y+1 9월, MB Y+0 12월–NWE Y+1 1월, FEI Y+0 11월–Y+1 12월, FEI–Conway Y+0 12월). 7월 실행 전환을 위해 ① RM Policy·권한·책임 구조 셋업 ② 본부별 Ontology·판단로직 담당자 지정 ③ Trading 원장 DB화 및 Trading-재고-연동물량 데이터 통합 활용을 유관부서와 협의. 6/12 Gas Solution실 전 구성원 대상 패턴분석·해석력 로직 Download, AX디자인팀도 시스템을 line-by-line 내재화.",
 ['79%','TAM 7개','RM Policy','Trading 원장','Gas Solution실','TTF-HH'])
add('ax','ax2','2026-06-11','6/1~5','plan','이천포럼 CEO타운홀(6/11) 준비: AI Vision 2030·AX 방향 구성원 직접 전달',
 "사장님 보고 후 피드백을 반영해 6/11 CEO타운홀 구성원 공유자료 보완. 기술 도입을 넘어 구성원의 <b>일하는 방식 변화와 역할 전환</b>을 공식 메시지로 공유하고 실제 행동 변화로 연결되도록 후속 변화관리 추진. 6/4 P&C팀이 전 구성원 대상 일정 공지, 진행·현장 지원 체계 확정. 타운홀 이후 구성원 반응·질문 기반으로 후속 커뮤니케이션·교육 콘텐츠 보완 계획.",
 ['CEO타운홀','이천포럼','AI Vision 2030','변화관리','P&C'])
add('ax','ax1','2026-06-15','6/15~19','plan','Trading AX 7월 운영 적용 변화관리: 일괄 런칭 아닌 현업 검증 루프 착수',
 "7월 Trading AX 현업 적용은 완성형 시스템 일괄 런칭이 아니라 <b>운영 버전 적용 후 현업 검증 루프를 착수하는 단계</b>로 관리. 핵심은 AI 추천 → 현업 검토·판단 → 피드백 축적 → Agent 로직·Ontology 보완의 운영 사이클 정착. 테스트는 기능 구현 여부가 아니라 AI 결과물이 실제 Trading 판단에 활용 가능한 수준인지 점검. 현업 피드백은 ① Agent 결과물 품질·로직 ② UI·사용성 ③ 증강·기능 고도화로 분류해 Ontology 보완으로 연결, Trading Menu 발굴 역량 내재화를 위해 <b>Learning by Doing</b> 변화관리 병행(AI가 TAM 후보 도출 → 펀더멘털 해석·Signpost 정의 → Trading Menu 전환 방법론을 트레이딩 조직과 공유). 시급한 4개 Action Item: ① 시스템 기능·로직 교육 ② 피드백 수집·반영 체계 ③ AI와 사람의 역할 구분 ④ TAM 발굴·승격, 진입·청산, 자금·포지션 운영, RM Policy 등 AI 기반 의사결정 기준.",
 ['변화관리','현업 검증 루프','Learning by Doing','Ontology','RM Policy','Action Item'])
add('ax','ax2','2026-06-15','6/15~19','prog',"구성원 교육 만족도 4.5, 의장님 지시 '격주 금요일 AX 몰입' 검토, Confluence 검토",
 "구성원 대상 '반복 업무 자동화' 교육 완료, 만족도 약 <b>4.5점</b>. 수요 지속으로 2차수 준비, 6/26 팀장 AI 교육은 SK가스 맞춤 실습 시나리오·Gemini Enterprise 활용 중심 기획. AI Letter 6/18 'Deep Research' 발송, 6/25 'Agent Builder' 예정. 향후 교육은 Tool 사용법이 아닌 보고서 작성·리서치·반복업무 자동화·Agent 활용 등 생산성 중심 운영. 지난 금요일 <b>의장님 지시로 올해 말까지 격주 금요일 전 구성원 AX 몰입 시간</b> 방안 검토 후 별도 보고 예정. AI Readable Data 확보·문서 체계 표준화를 위해 <b>Confluence 도입 검토</b> 착수: AX추진실에 우선 전면 적용(회의록·의사결정·요구사항·산출물·변경 이력 구조화), 전략기획실 3개 팀 진단 후 전략본부 확대. SharePoint·Teams·메일과 역할 중복 시 추가 입력 부담으로 인식될 수 있어 'Confluence에 남길 정보'와 '기존 Tool 유지 정보' 구분 원칙 정리.",
 ['만족도 4.5','팀장 교육','AI Letter','AX 몰입','Confluence','의장님'])
add('ax','ax1','2026-06-22','6/22~26','mile','Trading AX 7/1 Beta Open 확정: Working Operation 전환, 7/20 기능확대',
 "Trading AX는 <b>7/1 Beta Open</b>을 기점으로 Working Operation 단계로 전환. 마일스톤: 7/1 1차 Beta Open → 7/20 기능확대 Beta Open → 7월 말 운영 검증. [MI] 6/22 1차 통합테스트·6/24 현업 테스트로 기능·데이터 정합성 검증, 결함 우선순위 조치. 7/1은 Event 해석·단일 이벤트 기반 시나리오 생성/수정·Signpost 기반 모니터링 중심, 7/20에는 시나리오 분기값 정량 변환·수급모델 Input Parameter 연계·가격 전망 Range 도출/해석까지 확장. 사용자 Feedback Card를 산출물로 관리. [PP] 개발기→운영기 이관 테스트, Spike·반복·실시간 패턴 QA, 6/26 통합테스트·7/1 유저 테스트 안정화. 7/1은 반복적 패턴 발굴·실시간 유효 TAM 추천 중심, AI 결과가 현업 의사결정에 실제 활용 가능한 수준인지·추천 근거가 설명 가능한지 검증하는 단계로 운영.",
 ['7/1 Beta Open','Working Operation','7/20','Feedback Card','통합테스트'])
add('ax','ax2','2026-06-22','6/22~26','prog','Confluence(AI Readable 협업 Tool) 도입 검토: AX추진실 실사용 후 확산',
 "AI Readable 기반 협업 Tool로 Confluence 도입 검토 중. AX추진실 실사용 검증 후 전략본부 및 전사 확산 계획 수립, Confluence 환경 구성·문서 작성 방식·Template·운영 기준을 실사용 관점에서 검증. 기존 SharePoint·Teams·메일과의 역할 중복에 따른 추가 입력 부담을 막기 위한 운영 원칙과 도입에 따른 변화 Point, 구성원 일하는 방법 변화관리 체계 수립·적용 예정.",
 ['Confluence','AI Readable','AX추진실','변화관리'])

# ───────── 7월 ─────────
add('ax','ax1','2026-07-01','6/29~7/3','mile','7/1 Trading AX Beta Open: 데일리 스크럼, 7/8 AI Trading Kick-off',
 "MI·Position Play를 현장 베타 테스트 단계로 전환, 현업 피드백 기반으로 기능·품질·운영 방식을 보완하는 Working Operation 시작. 7/1부터 <b>매일 오전 10시 MI·PP 통합 데일리 스크럼</b> 운영. 수용성 정량 추적: MI는 접속·주요 활용 흐름, PP는 챗봇 피드백·사용성 로그. 7/6 MI팀, 7/7 PP 사용자그룹 피드백 세션, 7/10부터 매주 금요일 오후 AX Friday. [MI] 이벤트 해석·단일 이벤트 시나리오·Signpost 모니터링 착수, 7/20 확대용 시나리오 가격 전망·해석 Agent 개발 병행. [PP] 7/1 현업 설명회에서 반복 패턴 탐색·실시간 패턴 탐지·Spike 탐지·챗봇 피드백 채널 시연. <b>AI Trading 전용 Book 필요성, Book Leader, 거래 한도, 진입 물량, AI 추천 수용·수정·기각 시 KPI·보상 반영 기준</b> 등 운영정책을 7/8 AI Trading Kick-off 보고 시 논의.",
 ['Beta Open','데일리 스크럼','AI Trading Book','손실한도','KPI','7/8 Kick-off'])
add('ax','ax2','2026-07-03','6/29~7/3','plan','AI Friday 7/10부터 매주 금요일 오후 정례화: 개인 AX·조직 AX 두 축',
 "전사 AX 확산 실행 프로그램으로 7/10부터 매주 금요일 오후 <b>AI Friday</b> 정례화. 구성원이 실제 업무 기반으로 Agent를 만들고 적용하며 피드백을 축적하는 실행 루틴. <b>개인 AX</b>는 개인별 업무 Agent 개발·반복업무 개선, <b>조직 AX</b>는 실 단위 Agent 후보 발굴·업무 프로세스 Redesign·적용 사례 축적. Trading AX의 MI·PP 활용 실습을 병행해 현업 피드백 축적, 축적된 방법론을 전사 AX 확산 업무 지식으로 연결.",
 ['AI Friday','개인 AX','조직 AX','Agent','Redesign'])
add('ax','ax3','2026-07-03','6/29~7/3','plan','CEO Agent 설계 방향: 조직·Trading Agent를 조합하는 Hyper Agent 구조',
 "CEO Agent는 권한 기반으로 전사에서 구현되는 조직별 Agent와 Trading Agent 등을 호출·조합해 경영 의사결정을 지원하는 <b>Hyper Agent 구조</b>로 설계 방향 정리. 그룹 공통 기능(일정 관리, Daily Briefing, 회의 전후 준비, Follow-up)에 더해 Trading AX·MI·Position Play·보고서 구조화·시장 분석·리더스 노트 연계 등 당사 특화 기능 검토. 사장님 업무 방식에 맞는 실효성 중심 설계 추진.",
 ['CEO Agent','Hyper Agent','Daily Briefing','리더스 노트','그룹 공통기능'])
add('ax','ax1','2026-07-09','7/6~7/10','risk','CEO 주관 품질검증 세션(7/9): 보완 과제 3개 확인, TAM→실물 계약 연결 목표',
 "베타테스트 Kick-off 미팅에서 운영 방침과 리스크 기준(Loss Limit) 확정. 사장님 주관 품질검증·피드백 세션(7/9)에서 MI·PP 결과물을 Claude로 심화 분석하는 워크플로를 직접 시연, 보완 과제 확인: ① Driver 변화가 정상인지 이상인지 판단할 <b>수치 기준 부재</b>(fundamental 해석) ② <b>하루 한 번 분석</b>에 그쳐 실시간 대응 어려움(MI 이벤트 수집) ③ 시나리오 분기값이 <b>템플릿으로 고정</b>(MI). 후속 과제로 LLM(Claude) 프롬프트 엔지니어링 교육, Driver·Signpost 정량 기준 보완, 사용자 피드백 재학습 자동화 확정. <b>최종 목표는 발굴된 TAM을 실물 계약구조로 연결</b>. [MI] 08:00 수집·09:30~10:00 분석 완료의 Daily 구조 확인, 가독성·번역체·숫자 오역·분기 템플릿 유연화 보완. [PP] 8개 빌딩블록 중 4개 현업 적용, 7/20까지 2개 추가(펀더멘탈 Q&A 챗봇, 일배치 1회→3회). 소스코드 보안점검은 정보보호담당과 차주 완료 목표.",
 ['품질검증','Claude','Loss Limit','Driver','빌딩블록','프롬프트 엔지니어링'])
add('ax','ax2','2026-07-10','7/6~7/10','done','AI Friday 1회차(7/10): Agentic AI 강연, 트레이더 Claude 분석 판단 기준 DB화',
 "AI Friday 1회차: 시행 배경·운영 방식·연말 목표 안내, 외부 전문가 초청 Agentic AI 이해 및 멤버사 사례 공유, mySUNI 자율 수강과 Track별 세션 운영. 전 구성원이 AI에 몰입하는 시간으로 AI Literacy를 높이고 일하는 방식을 바꾸는 시간으로 운영. Trading Track에서는 트레이더가 PP 결과물을 직접 Claude로 분석하며 사용법 습득·품질검증, <b>Claude 분석 종료 시 판단 기준을 자동으로 DB화해 축적</b>하는 구조로 현업 경험·노하우를 자산화하는 검증 체계 시작. 프롬프트 용어·표현, 인덱스 해석, 유가-드라이버 매핑 오류, 데이터 최신성 등 피드백 접수, 매주 금요일 품질 점검·재검증 정례 운영.",
 ['AI Friday','Agentic AI','Claude','DB화','mySUNI'])
add('ax','ax1','2026-07-13','7/13~7/17','info','CEO 세션: 신규 Trading 기회 발굴 가능성 확인, 신뢰성 제고 필요 (G&P One team)',
 "사장님 주관 세션을 통해 Trading AX의 새로운 Trading 기회 발굴 가능성을 확인하는 한편, 실제 의사결정 활용을 위해서는 <b>분석 근거와 판단의 신뢰성</b>을 더 높여야 함을 확인. AI 판단 근거·현업 활용 가능성 집중 검증 방식으로 운영 강화(기준 데이터·펀더멘털 검증, Claude 교차검증, 현업 토론 후 최종 판단, 검증 사항 시스템 반영). G&P 본부와 One team으로 실제 업무 적용 노력 지속, 초기 단계이나 Claude 활용 Optionality spread 분석 사례에서 일정 부분 <b>생산성 개선 효과</b> 확인.",
 ['CEO 세션','신뢰성','G&P','One team','Optionality spread','Claude'])
add('ax','ax2','2026-07-13','7/13~7/17','done','AI Friday 3개 Track 확정 (C-Team 보고): 개인·조직·과제 검증(Trading AX)',
 "AI Friday 실행계획을 C-Team Weekly에 보고하고 Track별 방향 확정. <b>개인 Track</b>은 AI Readiness 진단 기반 AI Literacy 육성, <b>조직 Track</b>은 AI Champion 중심 업무 프로세스 재설계·과제 발굴, <b>과제 검증 Track</b>은 Trading AX 대상 현업 주도 품질검증·피드백. 차주부터 Track별 프로그램·교육과정 구체화, 전 팀 업무 프로세스 현황을 템플릿으로 수집해 8월 중순까지 하반기 조직 AX 과제 확정. 교육 참여보다 실제 업무 적용·성과 창출에 중점.",
 ['AI Friday','3개 Track','AI Readiness','AI Champion','C-Team'])
add('ax','ax1','2026-07-20','7/20~7/24','risk','2차 확대 오픈 후 CEO 품질검증: 복합 이벤트 미반영 → 복합 시나리오 최우선, BSC 인수인계',
 "MI 수급모델 파라미터 제안·가격 전망 해석 기능과 PP 챗봇을 운영에 정식 배포해 <b>2차 확대 오픈 완료</b>. 사장님 품질검증 세션에서 폭염과 지정학 리스크가 결합된 <b>복합 이벤트를 충분히 반영하지 못하거나 일부 산출물의 현실 정합성이 떨어지는 사례</b> 확인 → 복합 이벤트 시나리오 개발을 최우선 과제로 추진, 사실관계·시장 정합성을 점검하는 평가 Agent 적용, 현업 피드백·대화 기록을 자산으로 축적해 수집–정제–승인–반영으로 개선을 입증하는 집단학습 체계 구축, 한 달 내 동일 기준으로 품질 재점검. 발굴된 TAM은 Driver 간 위계 미정립으로 상관·인과관계가 혼재될 수 있어 PP–MI 연계 과정에서 <b>Driver Tree 기반 분석체계</b>로 전환. BCG에서 BSC로 패턴 분석 방법론·검증 역량 인수인계 완료, 약 <b>4,400개 인덱스 조합</b> 검증 본격화(AI로 설명 가능성에 따라 유형화, 계절성 분리 후 핵심 Driver 인과관계 검토).",
 ['복합 이벤트','평가 Agent','집단학습','Driver Tree','BSC','4,400개 조합'])
add('ax','ax2','2026-07-20','7/20~7/24','prog','전 구성원 AI Readiness 진단 시작 (AI Champion 선정 기초), 가드레일·용어사전 배포',
 "Trading AX Track에서 공통 업무지침·가드레일·용어사전을 배포하고, 트레이더가 직접 AI로 특정 Spread의 월별 Rollover 손실 리스크를 분석. 현업의 <b>On-demand 분석 요구</b>와 기존 PP의 반복 패턴 중심 접근 간 차이를 확인, 원하는 인덱스·월물 조합을 직접 선택해 자연어로 분석 요청할 수 있도록 기능개발 우선순위 조정. 전 구성원 대상 <b>AI Readiness 진단</b> 시작: 평가 목적이 아니라 개인별 역량 수준에 맞는 교육·실습 제공, 조직별 AI Champion 선정 기초자료. AI Champion은 진단 결과와 활용 의지를 종합해 선정, 업무현황 분석은 직무 중심 Top-down과 현업·Champion 중심 Bottom-up 결합.",
 ['AI Readiness','AI Champion','가드레일','용어사전','Rollover','On-demand'])
add('ax','ax1','2026-07-27','7/27~7/31','plan','MI 복합 이벤트 시나리오·Trading AX 챗봇 10월 완료 목표, G&P Claude Code 사례',
 "현장 활용을 위한 MI 최우선 과제인 복합 이벤트 시나리오는 <b>10월 완료 목표</b>. LLM 기반 자유로운 재계산·교차검증·시나리오 분석과 자연어 양방향 피드백을 지원하는 챗봇 서비스 설계 착수: 일반 LLM과 달리 MI·PP와 직접 연계해 환각(Hallucination) 리스크를 줄이고 검증 가능한 근거 제공, 사용자 간 동일한 시장 해석 기준을 공유하는 분석 엔진 목표(10월 완료). G&P본부가 <b>2027년 롤오버(만기 이월) 리스크 분석</b>을 AI Tool(Claude Code)로 수행 — Trading AX 화면은 쓰지 않았지만 Trading AX 검증 데이터를 Claude가 활용해 보고서를 작성한 사례로, 다양한 Trading 업무로의 확산 가능성 확인. EE본부 수급전략팀과 LPG 소싱·옵셔널리티 업무도 Trading AX·Claude로 분석 가능하도록 교육·실습 진행 예정.",
 ['복합 이벤트','챗봇','Hallucination','Claude Code','롤오버','EE본부'])

# ───────── 8월 ─────────
add('ax','ax1','2026-08-03','8/3~8/7','plan','7월 피드백 190건 유형화 → 8~10월 최우선 3과제, ODIN+AI Self 분석 환경 확대',
 "7월 운영 적용 이후 축적된 <b>약 190건의 피드백</b>을 현업 활용성·의사결정 가치 관점에서 유형화·우선순위화해 8~10월 고도화 최우선 과제를 ① 복합 이벤트 시나리오 ② PP 반복패턴·Spike 로직 고도화 ③ ODIN·포지션·재고·MI 등 내부 데이터를 조회·계산·교차검증하는 Trading AX 챗봇으로 정리, 10월까지 개발·현업 검증 완료 목표. ODIN Data와 AI를 연계한 <b>Self 분석 환경</b>을 Trading·EE·최적화로 확대: Trading본부에 ODIN 자동 연동 기반 Self 분석 환경(Claude Code)·분석 프롬프트 제공, EE본부는 LPG 소싱·옵셔널리티 분석 지원, 최적화실과는 Daily Optionality Spread를 우선 Case로 협의. 향후 포지션·재고·MI 내부 데이터를 단계적으로 연계해 현업이 직접 조회·재계산·분석하는 공통 환경으로 발전.",
 ['190건 피드백','3과제','ODIN','Self 분석','Claude Code','Trading AX 챗봇'])
add('ax','ax2','2026-08-03','8/3~8/7','mile','AI Champion 56개 팀 60명 선정 완료: 8월부터 조직 단위 AX 전환',
 "전사 AX 확산의 실행주체로 <b>56개 팀 60명의 AI Champion</b> 선정 완료. 7월까지가 구성원 개인의 AI 활용 경험·역량을 높이는 단계였다면, 8월부터는 AI Champion이 각 조직의 실제 업무를 발굴하고 AI 적용·업무 재설계를 주도하는 <b>조직 단위 AX</b>로 전환. 기업문화실과 협업해 Champion 활동이 일회성이 아니라 조직 내 기여로 인정되도록 Recognition 방안 마련, 각 조직의 실제 업무 적용 사례가 만들어지도록 밀착 지원.",
 ['AI Champion','56개 팀','60명','조직 AX','Recognition','기업문화실'])
add('ax','ax1','2026-08-10','8/10~8/14','prog','4,400개 Index 조합 재검증(계절성 구분), Trading AX–LLM 연동 10월 우선 구현',
 "[신뢰성 검증] 약 4,400개 인덱스 조합을 유형화하며 실제 Trading 기회인지 통계적 왜곡인지 재검증 중, 패턴 반복성을 신뢰성 있게 판단하기 위해 <b>계절적으로 반복되는 패턴과 시기와 무관한 패턴을 구분</b>해 분석. [Self 분석 환경 확대] EE본부 수급전략지원팀의 Claude 기반 자체 Agent 활용 지원 등 ODIN·가공 데이터와 Agent 구조 지원, 현업 직접 조회·재계산·분석 Case 확대. Trading AX 챗봇의 선결과제인 Trading AX–LLM 연동은 10월까지 MI 이벤트·PP 분석결과 조회, 사용자 피드백 저장 등 핵심 기능 우선 구현 — 단순 결과 조회를 넘어 내부 데이터를 직접 조회·검증하며 현업과 상호작용하는 분석 환경으로 발전 목표.",
 ['4,400개','계절성','EE 수급전략지원팀','Agent','LLM 연동'])
add('ax','ax2','2026-08-10','8/10~8/14','prog','AI Readiness 진단 432명(70%) 마감, AI Champion Re-Design 교육 착수',
 "AI Champion 대상 역할·추진방식을 안내해 실제 조직 업무를 AI로 재설계하는 실행 단계로 전환. <b>감사팀 비용감사 자동화, 연구소 SHE 법규관리 Agent</b> 등 구성원이 직접 만든 사내 사례를 확인한 결과, 자발적 AX 확산에는 단순 교육보다 직접 Agent를 만들어보는 경험과 직속 리더의 스폰서십이 중요함을 확인. 차주부터 AI Champion이 기존 업무를 AI 관점에서 다시 설계하는 프로세스 Re-Design 교육 시작, Best Practice 공유로 조직별 Agent 과제 발굴 연결. <b>AI Readiness 진단은 432명(약 70%) 참여로 마감</b>, 전 구성원 수준별 Learning Path 안내 완료. 이제 진단·교육 자체보다 학습 → Agent 직접 구현 → 현업 적용의 실행 구조에 중점, AI Friday와 임원·구성원 실습교육도 실제 업무 변화와 연결.",
 ['AI Readiness','432명','Learning Path','Re-Design','감사팀','SHE Agent'])
add('ax','ax1','2026-08-17','8/17~8/21','prog','Trading AX 개선 3축(Pattern·해석 신뢰성·복합 Event), Red Team Agent',
 "실제 활용을 위해 ① 유효한 Spread Pattern 선별 ② Fundamental 해석의 신뢰성 ③ 복합 Event를 고려한 MI Scenario 분석 기능 보완 중심으로 개선. PP는 <b>계절성이 명확한 신규 Pattern</b> 중심으로 후보를 발굴하고 Fundamental 타당성·Trading 실행 가능성을 검증해 실제 활용 가능한 TAM으로 선별·승격. MI는 복수 Event와 시장조건을 함께 반영하는 복합 Event Scenario 구조설계, 생성된 Scenario의 사실관계·시장 정합성을 사전 점검하는 <b>Red Team Agent</b> 적용방식 설계. MI·PP와 상용 LLM 연계로 Trader가 원천 Data 재계산 → 반대가설 검증 → 근거 원문 확인 → Feedback 축적을 직접 수행하는 Self-analysis 환경 확대, Daily Workflow로 확산해 판단·Feedback을 조직의 Trading Know-how로 자산화.",
 ['Red Team Agent','계절성 Pattern','복합 Event','Self-analysis','Know-how 자산화'])
add('ax','ax1','2026-09-02','8/31~9/4','done','MI Multi-Event Scenario 구현 완료, 9/2 배포·현업 검증 (근거 제공 강화)',
 "MI Multi-Event Scenario 구현을 완료하고 <b>9/2 배포</b>, 현업 검증 진행. 복수 Event 기반 Scenario 생성과 함께 Event–MI Record 연결 근거와 수급모델 Parameter 제안 근거를 함께 제공해 현업이 AI 산출물의 근거를 직접 확인하도록 개선. 자연어 질의로 현업이 직접 신규 Event를 생성하는 Custom Event 등 후속과제 구체화, AI Friday를 활용한 현업 직접 생성·검증 실습형 검증 지속.",
 ['Multi-Event Scenario','9/2 배포','MI Record','Custom Event','AI Friday'])
add('ax','ax3','2026-08-31','8/31~9/4','prog','CEO Agent: DY 공통 플랫폼 Infra 구성 시작, CEO Letter 77편 Persona',
 "DY 공통 플랫폼에서 당사 Infra 환경 구성 시작. 사장님 <b>월간 CEO Letter 77편</b>과 본부별 Weekly를 분석해 CEO Persona 초안 구성, 반복 업무·주요 관심사 기반으로 그룹·DY 공통기능 위에 구현할 당사 특화기능 후보를 ① Trading AX ② 경영분석 ③ 리더스 노트 ④ CEO Letter ⑤ SHE 5개 영역으로 도출. 차주 전략본부 Weekly에서 특화기능별 활용 시나리오·우선순위 논의, 그룹 공통기능과 당사 Needs가 중복 없이 구현되도록 상세설계 후 <b>10월 Beta Test</b> 추진.",
 ['CEO Agent','DY 공통 플랫폼','CEO Persona','CEO Letter 77편','특화기능 5개','10월 Beta'])

# ───────── 9월 ─────────
add('ax','ax1','2026-09-07','9/7~9/11','plan','MI 9/22 정기배포 / PP 계절성 Pattern 10/16·10/23 적용 → 모의 Trading 연결',
 "[MI] 9/2 복합 Event Scenario 1차 배포로 여러 Event가 동시에 시장에 미치는 영향을 Scenario로 분석하도록 범위 확대, 현업 Feedback 반영해 중요 Event 선별·분석방식 보완 후 9/22 정기배포. 10월 말까지 상용 LLM 연계와 Feedback·활용 Log 등 개선기능 구현, 이후 실제 시황 판단에서의 반복 사용·현업 채택 여부로 Value 검증. [PP] 신뢰도 높은 계절성 Pattern을 실제 Trading 기회 탐색에 활용하도록 구현 중, <b>10/16 1차 적용·10/23 전체 적용</b> 목표. Pattern 반복 여부뿐 아니라 현재 시장상황·주요 Event를 함께 고려해 판단하는 방식으로 보완, 9월 기준 확정 → 10월 시스템 적용·검증 → 대표 Trading Menu의 모의 Trading 연결. 실물 연계 TAM과 RM Agent 설계 동시 진행.",
 ['9/22 배포','상용 LLM','계절성 Pattern','10/23','모의 Trading','RM Agent'])
add('ax','ax2','2026-09-11','9/7~9/11','prog','조직 Agent 과제정의서 57개 팀 중 40개(70%) 제출: 10월 구현·11월 적용·12월 평가',
 "전사 Agent는 개인·조직 Agent 두 Track으로 추진, 과제 발굴과 함께 구축 목표·실행계획 구체화. 조직 Agent는 9/11 기준 <b>57개 팀 중 40개 팀(70%)이 과제정의서 제출</b>, 9월 중 전 조직 과제·상세 구축계획 확정 → 10월 구현 → 11월 실 업무 적용·Demo → 12월 효과평가·우수사례 확산. 개인 Agent도 Readiness 수준별 교육과 Agent Builder 과정으로 10월 중 적용과제 확정·구현. 성과는 Agent 수보다 실제 업무 Process 변화와 조직 생산성 개선효과 중심으로 관리.",
 ['조직 Agent','과제정의서','70%','개인 Agent','Agent Builder'])
add('ax','ax3','2026-09-09','9/7~9/11','prog','CEO Agent 9/9 CEO 보고: 경영현황 조회·Trading AX 연계부터 우선 적용',
 "9/9 사장님 보고 시 피드백을 반영해 Persona 학습범위와 기능별 역할 구체화. 10월 Beta 적용 목표로, 초기에는 <b>경영현황 조회와 Trading AX 연계</b> 등 경영 판단에 활용 가능한 기능부터 우선 적용하고 Feedback 반영해 단계적 확대.",
 ['CEO Agent','Persona','Trading AX 연계','10월 Beta'])
add('ax','ax1','2026-09-14','9/14~9/18','prog','Trading RM 1단계 개발 착수(10월 말 단위 테스트), MI 가격전망 9/22 배포',
 "[MI] 복합 Event Scenario와 연계한 가격전망 정교화 진행, 9/22 운영 배포 예정. 배포 후 실제 활용·검증에서 Scenario·가격전망 품질 보완, 10월 말까지 상용 LLM 연계·Feedback Log 구현. [RM] <b>Trading RM 1단계 구축범위·Roadmap을 구체화해 개발 착수</b>, Trading AX·RM 운영에 필요한 Data 범위 구체화. 10월 말 단위 테스트 완료 목표, 이후 Backtesting 자동화 등 후속 기능 확대.",
 ['Trading RM','1단계','Backtesting','가격전망','9/22'])
add('ax','ax2','2026-09-16','9/14~9/18','done','조직 Agent 과제정의서 52개 팀 73건 접수 완료(9/16): 10/2 상세설계·11월 심사',
 "9/16까지 <b>52개 팀에서 조직 Agent 과제정의서 73건</b> 접수, 과제정의 완성도와 구축 난이도·Data 준비도·System 연결 수준 기준으로 1·2차 검토 완료. 10/2까지 상세설계 완료 및 활용계획 구체화, 10월 중 Agent 구현·업무 적용, 팀에서 실제 사용·보완한 결과를 바탕으로 11월 과제 심사.",
 ['조직 Agent','73건','52개 팀','상세설계','과제 심사'])
add('ax','ax3','2026-09-14','9/14~9/18','prog','CEO Agent M365 연동 완료, 9/23 DY 공통기능 + CEO Letter 우선 가 오픈',
 "인프라 설정과 M365(일정 등) 연동 완료, e-HR 등 내부 Data 연계 진행. <b>9/23 DY 공통기능과 당사 특화기능 중 CEO Letter를 우선 가 오픈</b>. 나머지 특화기능은 내부 Data 연계·품질 검증을 거쳐 10월 순차 적용, 사장님 실제 사용은 Contents 학습·품질 확인 이후 시작.",
 ['CEO Agent','M365','e-HR','CEO Letter','9/23 가 오픈'])

# ───────── 10월 ─────────
add('ax','ax1','2026-10-05','10/5~10/9','info','7월 대비 품질 비교: 호르무즈 사례, 복합 변수 반영 가격 상·하단 제시로 개선',
 "7월 1차 현장 적용 이후 축적된 Knowledge가 Event 해석·Scenario 품질을 실제로 높였는지 동일 사례의 7월·현재 결과를 MI팀과 비교 리뷰. 단일 Event 분석을 <b>복합 Event 기반 Scenario(Base·Bearish·Bullish)</b>로 전환, Parameter 제안 대상 Event 유형 확대, 수급모델 고도화. 예: 호르무즈 해협 봉쇄 사례는 7월에는 봉쇄 해소 시점만 달리한 Scenario에 그쳤으나 현재는 유럽 한파 등 복합 변수를 반영해 <b>가격의 상단과 하단</b>을 제시하는 수준으로 개선. MI·PP 데이터를 Claude에서 조회·활용하는 연동의 기본 동작을 확인해 트레이더가 필요한 분석을 직접 수행하는 Self-Analysis 환경 기반 마련, 운영 데이터 연동·인증·권한 검증 후 현업 적용 확대.",
 ['호르무즈','Base·Bearish·Bullish','품질 비교','Claude 연동','Self-Analysis'])
add('ax','ax3','2026-10-05','10/5~10/9','prog','CEO Agent: Trading AX MCP 연동·운영환경 세팅 완료, 10/16 오픈 목표',
 "주요 Legacy 시스템 개발계 연동에 이어 운영환경 세팅·뉴스 설정·<b>Trading AX MCP 연동</b>을 마치고 일부 질의응답 확인. CEO Persona·CEO Letter 개발 중 예상 질문·응답 규칙·사용자 시나리오를 구체화해 응답 정확도 검증. 경영분석은 월별 손익 Key Driver 자료 기반으로 결산 메일 수치를 정확히 재현하도록 데이터 매핑·검증 기준 확정, 회의록 조회·지시사항 후속조치 기능은 '26년 7월 이후 회의록·메일 적재 기준·샘플로 개발·검증 준비. 10/16 운영환경 오픈 목표, 보안 점검·대용량 조회 보완 결과 기준으로 실제 사용 가능 기능 확정.",
 ['CEO Agent','MCP','경영분석','회의록','10/16 오픈'])
add('ax','ax1','2026-10-12','10/12~10/16','done','MI 계획 기능 구현 완료 판단 → 운영 배포 / RM 파생평가손익 리포트 배포',
 "MI 업그레이드 버전에 대한 현업 피드백을 종합한 결과 <b>이번 단계에서 계획한 MI 기능 구현은 모두 완료</b>한 것으로 판단, 차주 전 기능을 운영환경에 배포하고 이후 현업 Daily 활용·피드백을 통한 분석 품질 개선에 집중. RM은 <b>파생평가손익 리포트</b>를 운영 배포하고 현업 테스트 시작 — 기존 Excel 양식을 유지하면서 수작업 전처리를 자동화하고 중간 검증 Sheet를 제공해 현업이 계산 과정·산출 결과를 직접 확인·검증.",
 ['MI 완료','운영 배포','RM','파생평가손익','Excel'])
add('ax','ax3','2026-10-16','10/12~10/16','mile','CEO Agent 1차 오픈(10/16, 유관자): 공통 Agent(일정·회의록·인사)+경영분석',
 "10/16 프로젝트 유관자 대상으로 <b>공통 Agent(일정·회의록·인사)와 당사 특화 Agent인 경영분석 기능을 1차 오픈</b>, 실무 관점 테스트 진행. 활용 시나리오 바탕으로 영역별 대표 질문·목표 답변을 정리해 현업 검토 중, 필요한 정보를 실제 데이터에 근거해 정확히 제공하고 답변 근거를 명확히 제시하는지 중점 검증해 10월 마지막 주 사장님 보고 예정. (이후 Weekly 미보고)",
 ['CEO Agent','1차 오픈','경영분석','회의록','인사'])
add('ax','ax4','2026-10-19','10/19~10/23','plan',"'27년 AX 추진계획: Trading AX 실사용 Value·조직 E2E 재설계·업무지식 형식지화",
 "'26년 Trading AX 현장 적용과 전사 AI 활용 확산을 통해 의사결정 지원·일하는 방식 변화 가능성을 확인했으나, <b>AI 기능 구현만으로는 실질적 사업 Value 창출에 한계</b>가 있으며 개별 Agent 중심 업무 개선을 조직 단위 생산성 혁신으로 연결하고 구성원의 업무지식·경험을 조직 자산으로 축적·재사용하는 체계가 필요하다는 교훈 도출. '27년 3대 중점과제: ① Trading AX 실사용 Value 창출 ② 조직 E2E 프로세스 재설계 ③ AI 기반 업무지식 형식지화 및 E2E 재설계 방법론 정립·확산. 행캔 미팅 전 사장님 별도 보고. (10/26주) 본부별 E2E 후보과제를 현업과 사전 협의하며 해결 문제·기대효과·재설계 범위·실행체계 검토 — 기존 업무에 AI를 추가하는 방식이 아니라 AI 활용을 전제로 불필요한 업무단계를 제거하고 조직 간 업무를 통합·재설계.",
 ["'27년 계획",'3대 중점과제','E2E 재설계','형식지화','행캔'])
add('ax','ax1','2026-10-23','10/19~10/23','mile','PP 10/23 운영 1차 배포, Claude 연계 Self-Analysis 운영계 확대',
 "운영 배포 계획에 따라 MI의 Event 알림·중복 Scenario 관리·독립 수급모델 등 주요 기능과 PP 전체 화면을 운영환경에 순차 배포하며 10월 계획 기능 적용 마무리. <b>PP는 10/23 운영환경 1차 배포</b>로 현업 접근 가능, 잔여 오류 보완. MI·PP 데이터를 Claude와 연계한 <b>Self-Analysis 환경을 운영계로 확대</b>해 현업이 정해진 화면에 의존하지 않고 과거·실시간 Pattern과 시장 환경을 직접 조회·분석. 11~12월은 신규 기능보다 분석 품질·사용성 개선에 집중. 실물연계는 대규모 시스템 별도 구축보다 기존 PP·Self-Analysis 환경을 최대한 활용해 중복 개발 최소화, 충족되지 않는 필수 기능만 선별해 추가 개발 범위 구체화.",
 ['PP 운영 배포','10/23','Self-Analysis','실물연계','Event 알림'])
add('ax','ax1','2026-10-26','10/26~10/30','prog','MI·PP 운영 배포 동작 확인 완료: 품질·사용성 집중, MI 12월 주니어 분석가 수준 목표',
 "지난 주 MI·PP 주요 기능 운영환경 배포와 1차 동작 확인 마무리. MI·PP 개발조직 구성원 워크숍에서 향후 <b>신규 기능 확대보다 현업 Daily 활용을 위한 분석 품질·사용성 제고에 집중</b>하기로 결정. MI는 <b>12월까지 현업 주니어 분석가 수준의 분석 품질</b>을 확보해 Daily 업무에 활용하는 것을 목표로 MI팀 피드백 세션 집중 운영, 복합 Event Scenario의 논리적 정합성·판단 근거 신뢰성 보완. PP는 과거 유사 시황 탐색 로직에 기존 Fundamental 데이터 외 <b>날씨·기온 예측 데이터</b> 추가 반영, 현업 검증으로 개선 효과 확인. 주요 기능 개발이 마무리됨에 따라 실제 Trading 의사결정에 활용 가능한 수준인지 검증에 집중: 현업의 분석 결과 수용·수정·기각 근거와 Back-testing 결과를 축적하고, 대표 TAM의 모의손익·RM 기준 충족 여부로 실거래 활용 가능성 판단.",
 ['동작 확인','주니어 분석가','날씨·기온','Back-testing','모의손익','RM 기준'])

COVERAGE = "43 / 43주차 (언급 없는 주차: 없음 — AX 추진은 '25.12/8부터 '26.10/30까지 매주 보고됨)"
