@echo off
echo ========================================
echo 영어 단어장 웹 애플리케이션 실행 중...
echo ========================================
echo.
echo 브라우저에서 다음 주소로 접속하세요:
echo http://127.0.0.1:5000
echo.
echo 종료하려면 Ctrl+C를 누르세요.
echo ========================================
echo.
cd /d "%~dp0"
python web_vocab_app.py
pause

