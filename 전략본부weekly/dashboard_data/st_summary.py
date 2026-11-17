# -*- coding: utf-8 -*-
INTRO = """<div style="font-weight:800;font-size:13.5px;margin-bottom:4px;">🧭 처음 보는 분을 위한 30초 요약 — 전략본부는 무슨 일을 하나</div>
전략본부는 SK가스의 <b>다음 먹거리를 만들고, 지금 가진 자산을 최적화하고, 회사 전체의 방향과 성적표를 챙기는</b> 조직입니다. '25.12월부터 '26.10월까지 Weekly 보고를 기준으로 보면 일은 8개 과제로 묶입니다.
<b>신사업 4개</b> — ① LNG 벙커링(선박용 LNG 급유, 자회사 에코마린), ② 에탄 사업(울산에 에탄 저장·공급, '27.1Q FID 목표), ③ 북미 NG/NGL(미국 가스전·미드스트림 직접 확보), ④ 하와이 LPG 발전 제안.
<b>최적화·리스크 2개</b> — ⑤ SKA/UPP(PDH 공장 가동·합병·UPP 매각), ⑥ 전사 포지션 & 미-이란 전쟁 대응(통합 포지션 대시보드·시나리오·Hedge).
<b>전사 기능 2개</b> — ⑦ AX 추진(Trading AI·전사 AI 변화관리·CEO Agent), ⑧ 전략기획·경영분석(SWAN 3.0·행캔·이사회·KPI·손익 추정·ZBB).
카드를 누르면 "이 과제는?" 설명, 현재 핵심 상태, 일자별 진행(최신순)이 펼쳐지고, LNG 벙커링은 다시 6개 업무로 나뉩니다."""

OVERVIEW = """<div class="bk-overview">
<div class="bk-ov"><div class="t">⚓ LNG 벙커링</div><div class="v">H-Line 5만톤 <b>10/20 Commit 곤란 통보</b></div>Eco Frontier '27.4Q 인도 · Hedge 1만톤 JKM-$1.69 · 3사 MOU 7/3</div>
<div class="bk-ov"><div class="t">🧪 에탄 사업</div><div class="v">FID 목표 <b>'27년 1분기</b></div>INEOS–SKGC 딜(전환율 55~60% 요구) · 제도개선 LCA 29.3% 감축 · STL MOU 4/14</div>
<div class="bk-ov"><div class="t">🌎 북미 · 🌺 하와이</div><div class="v">11월 미국 출장: <b>EOG·Devon·Conoco</b></div>Wet Gas Non-op BM(Eagle Ford) · Twin Eagle 인수 종료 · HECO RFP 트랙 전환</div>
<div class="bk-ov"><div class="t">⚙️ SKA · 🛡️ 전사 포지션</div><div class="v">'27 SKA <b>약 △700억</b> 전망</div>PDH 가동 유연성·FEI Index 전환 · 합병 특별위 8/20 · Proxy Hedge 7천톤 진입</div>
<div class="bk-ov"><div class="t">🤖 AX</div><div class="v">MI·PP <b>운영 배포 완료</b>(10/23)</div>AI Champion 60명 · 조직 Agent 과제 73건 · CEO Agent 1차 오픈 10/16</div>
<div class="bk-ov"><div class="t">🧭 기획·경영분석</div><div class="v">'26 세전이익 전망 <b>5,974억</b>(8월)</div>SWAN 3.0 → 행캔 10/30 · ZBB 70억 절감 · MSCI AAA</div>
</div>"""

GLOSSARY = [
 ('FID', 'Final Investment Decision, 최종 투자 결정. 에탄 사업은 수요·제도·파트너가 갖춰져야 FID 가능.'),
 ('에탄 / NEP / INEOS / SKGC', '에탄=천연가스에서 뽑는 석화 원료. NEP=SKGC(SK지오센트릭)의 나프타 분해 설비. INEOS=영국 화학사로 SKGC 분할 사업부 공동투자 협상 상대.'),
 ('CEC 물적분할', 'CEC(코리아에너지터미널 관련 법인)의 일부 사업을 별도 법인으로 떼어내는 것. 에탄 탱크 투자 구조와 연결.'),
 ('NG / NGL / Wet Gas / Non-op', 'NG=천연가스, NGL=천연가스에서 분리되는 에탄·프로판 등 액체. Wet Gas=NGL 함량이 높은 가스. Non-op=운영권 없이 지분만 참여하는 투자.'),
 ('R-PJT / E&S / EPD', "R-PJT=SK E&S와 공동으로 맥킨지와 수행한 북미·LNG 전략 프로젝트. EPD=Enterprise Products Partners, 미국 최대 미드스트림 기업(8/20 경영진 미팅)."),
 ('HSEO / HECO / JERA', 'HSEO=하와이 주 에너지청, HECO=하와이 전력회사(All-Fuels RFP 발주 예정), JERA=일본 발전사(하와이 500MW LNG 발전 추진 중).'),
 ('PDH / 프로필렌 스프레드 / UPP', 'PDH=프로판을 프로필렌으로 바꾸는 공정(SKA 울산 공장). 스프레드=프로필렌가−프로판가, 가동 경제성의 핵심. UPP=SKA 아래 PP(폴리프로필렌) 공장.'),
 ('CP / FEI / MB / MOPJ', '모두 가격 지수. CP=사우디 아람코 LPG 계약가, FEI=극동 LPG 현물지수, MB=미국 Mont Belvieu LPG가, MOPJ=일본 나프타 현물가. SKA 공급 Index를 CP→FEI로 바꾸는 논의 중.'),
 ('Proxy Hedge', '직접 Hedge할 상품이 없을 때 상관관계 높은 다른 지수(예: 프로필렌 대신 MOPJ 나프타)로 대신 위험을 막는 것.'),
 ('Relocation / AGIC', 'SKA 설비를 중동 등으로 옮기는 안. AGIC=사우디 파트너(Advanced Petrochemical 계열), 지분 매입 Term Sheet 협상 이력.'),
 ('SWAN 3.0 / 행캔', "SWAN=SK가스 중장기 성장전략 시리즈의 3번째. 행캔=행복경영캔미팅, 연말 그룹 차원 경영전략 회의(10/30)."),
 ('ZBB / OSS / AAR', 'ZBB=Zero-Based Budgeting(영기준 예산, EY와 70억 절감). OSS=One Stop Service 계약 사전검토 체계. AAR=After Action Review(SKA-SKMU 사후 점검).'),
 ('MI / PP / TAM', 'Trading AX 구성요소. MI=Market Intelligence(시황 분석), PP=Position Play(포지션 전략), TAM=Trading Action Menu(매매 기회 메뉴).'),
 ('AI Friday / AI Champion / CEO Agent', '전사 AX 변화관리 프로그램(개인·조직·과제검증 Track), 팀별 AI 선도 인력, DY(SK디스커버리) 공통 플랫폼 위에 만드는 CEO 전용 AI 비서.'),
 ('BCG AI Vision 2030', "'25.12~'26.2 BCG와 수행한 AX 전략 프로젝트. 18대 AI 과제·로드맵 도출."),
]
