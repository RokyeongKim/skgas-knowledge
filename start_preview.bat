@echo off
echo SK가스 지식베이스 로컬 미리보기 시작 중...
echo.
echo 브라우저가 열리면 http://localhost:3000 에서 확인하세요.
echo 종료하려면 이 창을 닫으세요.
echo.
start "" "http://localhost:3000"
python -m http.server 3000
pause
