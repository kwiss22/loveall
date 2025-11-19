# Git 설정 및 GitHub 업로드 가이드

## ✅ 완료된 작업
- ✅ Git 저장소 초기화
- ✅ .gitignore 설정 확인
- ✅ 파일 추가 완료

---

## 🔧 Git 사용자 정보 설정 (필수)

커밋을 하기 전에 Git 사용자 정보를 설정해야 합니다.

### 전역 설정 (모든 프로젝트에 적용)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 현재 프로젝트만 설정
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

**예시:**
```bash
git config --global user.name "홍길동"
git config --global user.email "hong@example.com"
```

---

## 📝 초기 커밋 생성

사용자 정보 설정 후:

```bash
git commit -m "Initial commit: 영어 단어장 웹 애플리케이션"
```

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
   - **"Initialize this repository with a README" 체크 해제**
   - "Create repository" 클릭

### 2단계: 로컬 저장소와 GitHub 연결

```bash
# 원격 저장소 추가 (YOUR_USERNAME을 GitHub 사용자명으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/game_english.git

# 브랜치 이름을 main으로 변경
git branch -M main

# GitHub에 업로드
git push -u origin main
```

---

## 📋 전체 명령어 순서

```bash
# 1. Git 사용자 정보 설정 (처음 한 번만)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. 초기 커밋 생성
git commit -m "Initial commit: 영어 단어장 웹 애플리케이션"

# 3. GitHub 저장소 생성 (웹사이트에서)

# 4. 원격 저장소 연결 (YOUR_USERNAME 변경 필요)
git remote add origin https://github.com/YOUR_USERNAME/game_english.git

# 5. 브랜치 이름 변경
git branch -M main

# 6. GitHub에 업로드
git push -u origin main
```

---

## 🔄 이후 업데이트 방법

코드를 수정한 후:

```bash
# 변경사항 확인
git status

# 변경된 파일 추가
git add .

# 커밋 생성
git commit -m "커밋 메시지 (예: 기능 추가, 버그 수정)"

# GitHub에 업로드
git push
```

---

## 💡 커밋 메시지 예시

좋은 커밋 메시지:
- ✅ "다중 선택형 퀴즈 기능 추가"
- ✅ "다크 모드 버그 수정"
- ✅ "통계 시각화 기능 추가"
- ✅ "코드 개선 및 에러 처리 강화"

나쁜 커밋 메시지:
- ❌ "수정"
- ❌ "업데이트"
- ❌ "변경"

---

## ❓ 문제 해결

### 인증 오류
- GitHub Personal Access Token 사용
- Settings → Developer settings → Personal access tokens

### 업로드 실패
```bash
# 원격 저장소 확인
git remote -v

# 원격 저장소 다시 설정
git remote set-url origin https://github.com/YOUR_USERNAME/game_english.git
```

---

**Git 설정 후 커밋하고 GitHub에 업로드하세요!** 🚀

