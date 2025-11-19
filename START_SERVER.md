# 웹 앱 실행 가이드 (문제 해결)

## 🔍 문제 진단

"사이트에 연결할 수 없음" 오류가 발생하는 이유:
1. Flask 앱이 실행되지 않음
2. 포트가 다른 프로그램에 사용 중
3. 방화벽 차단

## ✅ 단계별 해결 방법

### 방법 1: 직접 실행 (가장 확실한 방법)

1. **PowerShell 열기** (Windows 키 + X → PowerShell)

2. **프로젝트 폴더로 이동:**
   ```powershell
   cd C:\Users\Admin\projects\game_english
   ```

3. **Flask 앱 실행:**
   ```powershell
   python web_vocab_app.py
   ```

4. **다음 메시지가 보이면 성공:**
   ```
   * Running on http://127.0.0.1:5000
   ```

5. **이 메시지가 나오는 동안 브라우저에서 접속:**
   ```
   http://127.0.0.1:5000
   ```

### 방법 2: 간단한 테스트부터 시작

먼저 Flask가 제대로 작동하는지 테스트:

```powershell
cd C:\Users\Admin\projects\game_english
python test_flask_simple.py
```

이것이 작동하면, 메인 앱도 작동할 가능성이 높습니다.

### 방법 3: 배치 파일 사용

1. `run_web_app.bat` 파일을 더블클릭
2. 또는 PowerShell에서:
   ```powershell
   .\run_web_app.bat
   ```

## 🚨 오류별 해결 방법

### 오류 1: "Address already in use"
**원인:** 5000번 포트가 이미 사용 중

**해결:**
1. 다른 프로그램이 5000번 포트를 사용 중인지 확인
2. 다른 포트 사용:
   ```powershell
   # web_vocab_app.py 파일을 열고
   # 마지막 줄의 port=5000을 port=5001로 변경
   # 그 다음 http://127.0.0.1:5001로 접속
   ```

### 오류 2: "ModuleNotFoundError: No module named 'flask'"
**원인:** Flask가 설치되지 않음

**해결:**
```powershell
pip install flask
```

### 오류 3: "Python을 찾을 수 없습니다"
**원인:** Python이 PATH에 없음

**해결:**
```powershell
# Python 설치 확인
python --version

# 없다면 Python 설치 필요
```

### 오류 4: 템플릿 파일을 찾을 수 없음
**원인:** templates 폴더가 없음

**해결:**
- `templates` 폴더와 `static` 폴더가 있는지 확인
- 폴더 구조:
  ```
  game_english/
  ├── web_vocab_app.py
  ├── templates/
  │   └── index.html
  └── static/
      ├── style.css
      └── script.js
  ```

## 📋 체크리스트

실행 전 확인:
- [ ] Python이 설치되어 있나요? (`python --version`)
- [ ] Flask가 설치되어 있나요? (`pip list | findstr flask`)
- [ ] `templates` 폴더가 있나요?
- [ ] `static` 폴더가 있나요?
- [ ] `web_vocab_app.py` 파일이 있나요?

실행 중 확인:
- [ ] 터미널에 "Running on http://127.0.0.1:5000" 메시지가 보이나요?
- [ ] 터미널 창이 열려 있나요? (Flask 앱이 실행 중이어야 함)
- [ ] 브라우저 주소창에 `http://127.0.0.1:5000`을 정확히 입력했나요?

## 💡 중요한 팁

1. **Flask 앱은 계속 실행되어야 합니다**
   - 터미널 창을 닫으면 웹사이트에 접속할 수 없습니다
   - Flask 앱을 종료하려면 터미널에서 `Ctrl+C`를 누르세요

2. **브라우저 새로고침**
   - Flask 앱을 시작한 후 브라우저를 새로고침 (`F5` 또는 `Ctrl+R`)

3. **다른 브라우저 시도**
   - Chrome, Edge, Firefox 등 여러 브라우저로 시도

4. **방화벽 확인**
   - Windows가 Flask 앱 접근을 묻는 팝업이 나오면 "허용" 클릭

## 🆘 여전히 안 되면

1. **터미널의 전체 오류 메시지를 복사해서 알려주세요**
2. **다음 명령어 결과를 알려주세요:**
   ```powershell
   python --version
   pip list | findstr flask
   python -c "from flask import Flask; print('Flask OK')"
   ```

