# 📖 영어 단어장 웹 애플리케이션

영어 단어를 효율적으로 학습할 수 있는 웹 기반 단어장 애플리케이션입니다.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 주요 기능

### 📝 단어 관리
- ✅ 단어 추가/수정/삭제
- ✅ 실시간 검색 (영어/한글)
- ✅ 단어 목록 보기

### 🎯 퀴즈 기능
- ✅ 영어 → 한글 퀴즈
- ✅ 한글 → 영어 퀴즈
- ✅ 정답/오답 즉시 확인
- ✅ Enter 키로 빠른 정답 확인

### 📊 통계 및 시각화
- ✅ 단어별 정답률 표시
- ✅ 정답률 상위 10개 단어 막대 그래프
- ✅ 전체 통계 요약 도넛 차트
- ✅ 정답률 순 정렬

### 🎨 UI/UX
- ✅ 다크 모드 지원
- ✅ 반응형 디자인 (모바일/데스크톱)
- ✅ 부드러운 애니메이션
- ✅ 직관적인 인터페이스

## 🚀 빠른 시작

### 필수 요구사항
- Python 3.7 이상
- pip (Python 패키지 관리자)

### 설치 방법

1. **저장소 클론 또는 다운로드**
   ```bash
   git clone <repository-url>
   cd game_english
   ```

2. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **애플리케이션 실행**
   ```bash
   python web_vocab_app.py
   ```

4. **브라우저에서 접속**
   ```
   http://127.0.0.1:5000
   ```

### Windows 사용자
배치 파일을 사용하여 간편하게 실행할 수 있습니다:
```bash
run_web_app.bat
```

## 📁 프로젝트 구조

```
game_english/
├── web_vocab_app.py          # Flask 메인 애플리케이션
├── vocab_book.py             # 콘솔 버전 (참고용)
├── requirements.txt          # Python 패키지 의존성
├── vocabulary.json           # 단어장 데이터 (자동 생성)
├── quiz_stats.json           # 퀴즈 통계 데이터 (자동 생성)
├── templates/
│   └── index.html           # 메인 HTML 템플릿
└── static/
    ├── style.css            # CSS 스타일
    └── script.js            # JavaScript 로직
```

## 🎯 사용 방법

### 단어 추가
1. "단어 추가" 탭 클릭
2. 영어 단어와 한국어 뜻 입력
3. "추가하기" 버튼 클릭

### 단어 검색
1. "단어 목록" 탭에서 검색창 사용
2. 영어 또는 한글로 검색
3. 실시간으로 검색 결과 표시

### 퀴즈 풀기
1. "퀴즈" 탭 클릭
2. 퀴즈 타입 선택 (영어→한글 / 한글→영어)
3. "문제 시작" 버튼 클릭
4. 답 입력 후 "정답 확인" 또는 Enter 키

### 통계 확인
1. "통계" 탭 클릭
2. 정답률 그래프 및 통계 목록 확인
3. 정답률이 낮은 단어 집중 학습

### 다크 모드
- 헤더 우측 상단의 다크 모드 버튼 클릭
- 설정은 자동으로 저장되어 다음 접속 시에도 유지

## 🔧 문제 해결

### 포트가 이미 사용 중일 때
애플리케이션이 자동으로 5001 포트로 시도합니다. 또는 수동으로 포트를 변경할 수 있습니다:
```python
# web_vocab_app.py 마지막 부분
start_server(5001)  # 원하는 포트 번호로 변경
```

### 데이터가 보이지 않을 때
- 브라우저 새로고침 (F5)
- "새로고침" 버튼 클릭
- `vocabulary.json` 파일이 프로젝트 폴더에 있는지 확인

### CSS/JS가 로드되지 않을 때
- `static` 폴더가 올바른 위치에 있는지 확인
- 브라우저 개발자 도구(F12)에서 콘솔 에러 확인
- 브라우저 캐시 삭제 후 재시도

## 📦 배포

### 로컬 네트워크에서 접근
다른 기기에서 접근하려면:
```python
# web_vocab_app.py
app.run(debug=True, host='0.0.0.0', port=5000)
```
그 후 같은 네트워크의 다른 기기에서 `http://<서버-IP>:5000`으로 접속

### 프로덕션 배포
프로덕션 환경에서는 다음을 권장합니다:
- Gunicorn 또는 uWSGI 사용
- Nginx를 리버스 프록시로 사용
- 환경 변수로 설정 관리
- HTTPS 사용

예시 (Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_vocab_app:app
```

## 🛠️ 기술 스택

- **Backend**: Python 3.7+, Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **차트**: Chart.js 4.4.0
- **데이터 저장**: JSON 파일

## 📝 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 🤝 기여

버그 리포트, 기능 제안, Pull Request를 환영합니다!

## 📧 문의

문제가 발생하거나 질문이 있으시면 이슈를 등록해주세요.

---

**즐겁게 영어 단어를 공부하세요! 📖✨**

