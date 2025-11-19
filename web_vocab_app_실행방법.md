# web_vocab_app.py 실행 방법

## 🚀 가장 간단한 방법 (3단계)

### 1단계: 터미널 열기
- **VS Code**: 하단의 "터미널" 탭 클릭
- **또는 PowerShell**: Windows 키 + X → "Windows PowerShell" 선택

### 2단계: 명령어 실행
터미널에서 다음 명령어 입력하고 **Enter** 키 누르기:
```powershell
python web_vocab_app.py
```

**중요:**
- ✅ `python web_vocab_app.py` (O) - 올바른 명령어
- ❌ `web_vocab_app.py` (X) - 이것만 입력하면 오류!

### 3단계: 성공 확인 및 브라우저 접속

#### 3-1. 성공 메시지 확인
터미널에 다음과 같은 메시지가 보이면 성공:
```
============================================================
영어 단어장 웹 애플리케이션 시작!
============================================================
단어 개수: 6개
통계 기록: 2개
접속 주소: http://127.0.0.1:5000
============================================================

* Running on http://127.0.0.1:5000
* Debug mode: on
Press CTRL+C to quit
```

#### 3-2. 브라우저 접속
1. **브라우저 열기** (Chrome, Edge, Firefox 등)
2. **주소창에 입력:**
   ```
   http://127.0.0.1:5000
   ```
3. **Enter 키 누르기**

#### 3-3. 웹 앱 확인
다음과 같은 화면이 보이면 성공:
- "영어 단어장" 제목
- "단어 목록", "단어 추가", "퀴즈", "통계" 탭
- 보라색 그라데이션 배경
- 저장된 단어 목록

---

## 📝 상세한 설명

### VS Code에서 실행하기

1. **VS Code에서 터미널 열기:**
   - 하단의 "터미널" 탭 클릭
   - 또는 **Ctrl + `** (백틱) 키

2. **프로젝트 폴더로 이동 (필요한 경우):**
   ```powershell
   cd C:\Users\Admin\projects\game_english
   ```

3. **Flask 앱 실행:**
   ```powershell
   python web_vocab_app.py
   ```

4. **터미널 메시지 확인:**
   - "Running on http://127.0.0.1:5000" 메시지 확인

5. **브라우저 접속:**
   - 주소: `http://127.0.0.1:5000`

### PowerShell에서 실행하기

1. **PowerShell 열기:**
   - Windows 키 + X → "Windows PowerShell"

2. **프로젝트 폴더로 이동:**
   ```powershell
   cd C:\Users\Admin\projects\game_english
   ```

3. **Flask 앱 실행:**
   ```powershell
   python web_vocab_app.py
   ```

4. **브라우저 접속:**
   - 주소: `http://127.0.0.1:5000`

---

## ⚠️ 주의사항

### 1. 터미널 창을 닫지 마세요!
- Flask 앱이 실행 중일 때는 **터미널 창을 열어둬야** 합니다
- 창을 닫으면 웹사이트에 접속할 수 없습니다
- 종료하려면 터미널에서 **Ctrl + C**를 누르세요

### 2. 올바른 파일을 실행하세요!
- ✅ `python web_vocab_app.py` (O) - 실제 단어장 앱
- ❌ `python test_flask_simple.py` (X) - 이것은 테스트용

### 3. 올바른 주소로 접속하세요!
- ✅ `http://127.0.0.1:5000` (O)
- ❌ `http://127.0.0.1:5000/main` (X) - 이 경로는 없습니다

---

## 🔧 문제 해결

### 문제 1: "Python을 찾을 수 없습니다"

**원인:** Python이 설치되지 않았거나 PATH에 없음

**해결:**
```powershell
python --version
```
버전이 나오면 OK, 안 나오면 Python 설치 필요

### 문제 2: "ModuleNotFoundError: No module named 'flask'"

**원인:** Flask가 설치되지 않음

**해결:**
```powershell
pip install flask
```

### 문제 3: "Address already in use"

**원인:** 5000번 포트가 이미 사용 중

**해결:**
1. 다른 터미널에서 Flask 앱이 실행 중인지 확인
2. 실행 중이면 Ctrl + C로 종료
3. 다시 실행

### 문제 4: 명령어가 인식되지 않음

**원인:** `python` 없이 파일 이름만 입력

**해결:**
- ❌ `web_vocab_app.py` (X)
- ✅ `python web_vocab_app.py` (O)

---

## 💡 사용 팁

### 웹 앱 종료하기
터미널에서 **Ctrl + C** 키를 누르세요

### 다시 실행하기
1. 터미널에서 Ctrl + C로 종료
2. 다시 `python web_vocab_app.py` 실행
3. 브라우저 새로고침 (F5)

### 여러 번 실행하기
- 같은 터미널에서 Ctrl + C로 종료 후 다시 실행 가능
- 다른 터미널 창을 새로 열 수도 있음

---

## 📋 체크리스트

실행 전 확인:
- [ ] Python이 설치되어 있나요? (`python --version`)
- [ ] Flask가 설치되어 있나요? (`pip list | findstr flask`)
- [ ] `web_vocab_app.py` 파일이 있나요?
- [ ] `templates/index.html` 파일이 있나요?
- [ ] `static/style.css` 파일이 있나요?

실행 후 확인:
- [ ] 터미널에 "Running on http://127.0.0.1:5000" 메시지가 보이나요?
- [ ] 브라우저에서 `http://127.0.0.1:5000`로 접속했나요?
- [ ] 웹 페이지가 제대로 보이나요?
- [ ] CSS 스타일이 적용되어 있나요?

---

## 🎯 요약

1. **터미널 열기** (VS Code 또는 PowerShell)
2. **명령어 입력:** `python web_vocab_app.py`
3. **Enter 키 누르기**
4. **성공 메시지 확인** ("Running on http://127.0.0.1:5000")
5. **브라우저에서 접속:** `http://127.0.0.1:5000`
6. **터미널 창은 열어두기!** (종료하려면 Ctrl + C)

---

**지금 바로 실행해보세요!** 🚀

