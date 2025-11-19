# GitHub 업로드 가이드

## ✅ 완료된 작업
- ✅ Git 저장소 초기화
- ✅ .gitignore 설정 확인
- ✅ 초기 커밋 생성

---

## 🚀 GitHub에 업로드하기

### 1단계: GitHub에서 저장소 생성

1. **GitHub 웹사이트 접속**
   - https://github.com 접속
   - 로그인 (계정이 없으면 회원가입)

2. **새 저장소 생성**
   - 우측 상단의 "+" 버튼 클릭
   - "New repository" 선택

3. **저장소 설정**
   - Repository name: `game_english` (또는 원하는 이름)
   - Description: "영어 단어장 웹 애플리케이션 - Flask 기반"
   - Public 또는 Private 선택
   - **"Initialize this repository with a README" 체크 해제** (이미 README.md가 있으므로)
   - "Create repository" 클릭

4. **업로드 명령어 확인**
   - GitHub에서 표시되는 명령어를 복사하거나 아래 명령어 사용

---

### 2단계: 로컬 저장소와 GitHub 연결

#### 방법 1: HTTPS 사용 (추천)
```bash
# 원격 저장소 추가 (YOUR_USERNAME을 GitHub 사용자명으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/game_english.git

# 브랜치 이름을 main으로 변경 (GitHub 기본값)
git branch -M main

# GitHub에 업로드
git push -u origin main
```

#### 방법 2: SSH 사용
```bash
# 원격 저장소 추가 (YOUR_USERNAME을 GitHub 사용자명으로 변경)
git remote add origin git@github.com:YOUR_USERNAME/game_english.git

# 브랜치 이름을 main으로 변경
git branch -M main

# GitHub에 업로드
git push -u origin main
```

---

### 3단계: 인증

#### HTTPS 사용 시
- GitHub 사용자명과 비밀번호 입력
- 또는 Personal Access Token 사용 (비밀번호 대신)

#### Personal Access Token 생성 방법:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token" 클릭
3. 권한 선택 (repo 체크)
4. 토큰 생성 후 복사
5. 비밀번호 입력 시 토큰 사용

---

## 📝 업데이트 방법

코드를 수정한 후 GitHub에 업로드:

```bash
# 변경사항 확인
git status

# 변경된 파일 추가
git add .

# 커밋 메시지와 함께 커밋
git commit -m "커밋 메시지 (예: 기능 추가, 버그 수정 등)"

# GitHub에 업로드
git push
```

---

## 🔍 유용한 Git 명령어

### 상태 확인
```bash
git status          # 현재 상태 확인
git log             # 커밋 히스토리 확인
git branch          # 브랜치 목록 확인
```

### 변경사항 관리
```bash
git add <파일명>    # 특정 파일만 추가
git add .           # 모든 변경사항 추가
git commit -m "메시지"  # 커밋 생성
git push            # GitHub에 업로드
```

### 원격 저장소 관리
```bash
git remote -v       # 원격 저장소 확인
git remote remove origin  # 원격 저장소 제거
git pull            # GitHub에서 최신 버전 가져오기
```

---

## 🎯 다음 단계

### GitHub에 업로드 후:
1. **README.md 확인** - GitHub에서 자동으로 표시됨
2. **이슈 생성** - 개선할 사항이나 버그 기록
3. **릴리스 생성** - 버전 관리
4. **위키 작성** - 추가 문서화

### 저장소 설정:
1. **설명 추가** - 저장소 설명란에 프로젝트 설명
2. **토픽 추가** - python, flask, vocabulary 등
3. **라이선스 추가** - MIT, Apache 등
4. **웹사이트 URL** - 배포된 사이트 주소 (있는 경우)

---

## 💡 팁

### 좋은 커밋 메시지 작성법
- 간결하고 명확하게
- 무엇을 했는지 설명
- 예: "다중 선택형 퀴즈 기능 추가", "다크 모드 버그 수정"

### 커밋 규칙 예시
```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 포맷팅
refactor: 코드 리팩토링
test: 테스트 추가
chore: 빌드 설정 등
```

---

## ❓ 문제 해결

### 업로드가 안 될 때
```bash
# 원격 저장소 확인
git remote -v

# 원격 저장소 다시 설정
git remote set-url origin https://github.com/YOUR_USERNAME/game_english.git
```

### 충돌 발생 시
```bash
# 최신 버전 가져오기
git pull origin main

# 충돌 해결 후
git add .
git commit -m "충돌 해결"
git push
```

---

**GitHub에 업로드하면 프로젝트를 공유하고 포트폴리오로 활용할 수 있습니다!** 🚀

