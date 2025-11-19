# loveall 저장소 연결 가이드

## 🎯 목표
`kwiss22/loveall` 저장소에 현재 프로젝트를 업로드하기

---

## 📋 단계별 명령어

### 1단계: Git 사용자 정보 설정 (필수)

터미널에서 다음 명령어를 실행하세요:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**예시:**
```bash
git config --global user.name "kwiss22"
git config --global user.email "your-email@example.com"
```

### 2단계: 초기 커밋 생성

```bash
git commit -m "Initial commit: 영어 단어장 웹 애플리케이션"
```

### 3단계: loveall 저장소 연결

```bash
# 원격 저장소 추가
git remote add origin https://github.com/kwiss22/loveall.git

# 연결 확인
git remote -v
```

### 4단계: 브랜치 이름 확인 및 변경

```bash
# 현재 브랜치 확인
git branch

# main으로 변경 (필요시)
git branch -M main
```

### 5단계: GitHub에 업로드

#### 저장소가 비어있는 경우:
```bash
git push -u origin main
```

#### 저장소에 이미 파일이 있는 경우:
```bash
# 기존 파일 가져오기
git pull origin main --allow-unrelated-histories

# 충돌 해결 후
git push -u origin main
```

---

## ⚠️ 주의사항

### 저장소에 이미 파일이 있는 경우
- `--allow-unrelated-histories` 옵션 사용
- 충돌 발생 시 수동으로 해결 필요
- 기존 파일을 덮어쓰지 않도록 주의

### 이미 원격 저장소가 연결된 경우
```bash
# 기존 원격 저장소 확인
git remote -v

# 기존 원격 저장소 제거
git remote remove origin

# 새 원격 저장소 추가
git remote add origin https://github.com/kwiss22/loveall.git
```

---

## 🔄 전체 명령어 (한 번에 실행)

```bash
# 1. Git 사용자 정보 설정 (한 번만)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. 초기 커밋 생성
git commit -m "Initial commit: 영어 단어장 웹 애플리케이션"

# 3. 원격 저장소 연결
git remote add origin https://github.com/kwiss22/loveall.git

# 4. 브랜치 이름 변경
git branch -M main

# 5. GitHub에 업로드
git push -u origin main
```

---

## ✅ 확인 방법

업로드 후 GitHub에서 확인:
1. https://github.com/kwiss22/loveall 접속
2. 파일 목록 확인
3. README.md가 표시되는지 확인

---

**loveall 저장소에 연결하고 업로드하세요!** 🚀

