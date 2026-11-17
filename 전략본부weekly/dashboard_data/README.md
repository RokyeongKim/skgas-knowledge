# 전략본부 과제 대시보드 데이터 (본부현황 › 전략본부 탭)

- `bk_data.py` : LNG 벙커링 6개 업무(a~f) 항목 103건 + 용어
- `st_eth.py` 에탄·CEC / `st_na.py` 북미 NG/NGL / `st_hw.py` 하와이 / `st_ska_pos.py` SKA 최적화 + 전사 포지션 / `st_ax.py` AX / `st_pl.py` 기획·경영분석
- `st_summary.py` : 전략본부 30초 요약, 상단 핵심 박스, 추가 용어
- `st_build.py` : 위 데이터를 `index.html`의 `<!-- ST-DASH START/END -->` 구간과 `<script>`의 ST 데이터로 주입 (스크래치패드 경로 기준으로 작성됨 → 다른 환경에서 실행 시 SP 경로 수정)
- `AGENT_BRIEF.md` : 항목 작성 규칙(스키마·날짜·주차 라벨·kind)

새 Weekly 반영 절차: 해당 과제 파일의 ITEMS에 항목 추가 → CAT.status 갱신 → st_build.py 실행 → 렌더 확인 → 커밋.
