# 웹 앱 연결 문제 해결 가이드

## 문제: "사이트에 연결할 수 없음" 오류

### 해결 방법

#### 1. Flask 앱이 실행 중인지 확인
- 터미널/PowerShell에서 Flask 앱을 실행했는지 확인
- 다음 메시지가 보여야 합니다:
  ```
  * Running on http://127.0.0.1:5000
  ```

#### 2. 올바른 주소로 접속
브라우저 주소창에 **정확히** 입력:
```
http://127.0.0.1:5000
```
또는
```
http://localhost:5000
```

**주의:**
- `https://` 가 아닌 `http://` 사용
- 마지막에 슬래시(`/`) 포함 여부는 상관없음
- `127.0.0.1` 또는 `localhost` 둘 다 사용 가능

#### 3. Flask 앱 실행 방법

**방법 1: PowerShell에서 직접 실행**
```powershell
cd C:\Users\Admin\projects\game_english
python web_vocab_app.py
```

**방법 2: 배치 파일 사용 (더 쉬움)**
- `run_web_app.bat` 파일을 더블클릭
- 또는 PowerShell에서:
  ```powershell
  .\run_web_app.bat
  ```

**방법 3: VS Code에서 실행**
- `web_vocab_app.py` 파일을 열기
- F5 키를 누르거나 "Run" 버튼 클릭

#### 4. 포트가 이미 사용 중일 때

에러 메시지: `Address already in use` 또는 `포트가 이미 사용 중입니다`

**해결 방법:**
1. 기존 Flask 앱 프로세스 종료:
   - 실행 중인 PowerShell 창을 확인
   - Ctrl+C를 눌러 종료

2. 다른 포트 사용:
   - `web_vocab_app.py` 파일의 마지막 줄 수정:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # 5001로 변경
   ```
   - 브라우저에서 `http://127.0.0.1:5001`로 접속

#### 5. 방화벽 문제

Windows 방화벽이 Flask 앱을 차단할 수 있습니다.

**해결 방법:**
1. Windows 보안 설정 열기
2. 방화벽 및 네트워크 보호
3. 앱이 방화벽을 통과할 수 있도록 허용

또는 Flask 앱 실행 시 Windows가 허용 여부를 물어보면 "허용" 클릭

#### 6. 브라우저 캐시 문제

**해결 방법:**
1. 브라우저 하드 리프레시: `Ctrl + Shift + R` 또는 `Ctrl + F5`
2. 브라우저 캐시 지우기
3. 시크릿/프라이빗 모드로 접속 시도

#### 7. 정확한 실행 순서

1. **먼저 Flask 앱 실행:**
   ```powershell
   cd C:\Users\Admin\projects\game_english
   python web_vocab_app.py
   ```

2. **터미널에 다음 메시지가 보이면 성공:**
   ```
   * Running on http://127.0.0.1:5000
   ```

3. **브라우저를 열고 다음 주소로 접속:**
   ```
   http://127.0.0.1:5000
   ```

4. **웹사이트가 로드되면 성공!**

#### 8. 문제가 계속되면

1. **Flask 설치 확인:**
   ```powershell
   python -c "import flask; print('Flask 설치됨')"
   ```

2. **파일 구조 확인:**
   ```
   game_english/
   ├── web_vocab_app.py
   ├── templates/
   │   └── index.html
   └── static/
       ├── style.css
       └── script.js
   ```

3. **터미널 오류 메시지 확인:**
   - Flask 앱 실행 시 나오는 오류 메시지 확인
   - 빨간색 오류 메시지가 있으면 내용을 기록

4. **다른 브라우저로 시도:**
   - Chrome, Edge, Firefox 등

---

## 추가 팁

- Flask 앱을 실행한 터미널 창을 닫으면 웹사이트에 접속할 수 없습니다
- Flask 앱이 실행 중일 때는 터미널 창을 열어둬야 합니다
- 여러 개의 Flask 앱을 동시에 실행하면 포트 충돌이 발생할 수 있습니다

