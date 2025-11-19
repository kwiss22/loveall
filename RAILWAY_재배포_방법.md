# Railway 재배포 방법 가이드

## 🔄 Railway에서 재배포하는 방법

### 방법 1: GitHub 푸시로 자동 재배포 (가장 간단)

1. **로컬에서 빈 커밋 생성**
   ```bash
   git commit --allow-empty -m "Trigger redeploy"
   git push
   ```

2. **또는 파일을 약간 수정 후 푸시**
   - 아무 파일이나 약간 수정 (예: README.md에 공백 추가)
   - 커밋하고 푸시

---

### 방법 2: Railway 대시보드에서 재배포

#### 옵션 A: Deployments 탭에서

1. **Deployments 탭 클릭**
   - 왼쪽 사이드바에서 "Deployments" 클릭
   - 또는 상단 메뉴에서 "Deployments" 선택

2. **최신 배포 찾기**
   - 배포 목록에서 가장 최근 배포 확인
   - 상태가 "Failed" 또는 "Stopped"인 경우

3. **재배포 옵션 찾기**
   - 배포 카드 우측 상단의 **"..." (3점 메뉴)** 클릭
   - 또는 배포 카드를 클릭하여 상세 보기
   - **"Redeploy"** 또는 **"Deploy"** 옵션 선택

#### 옵션 B: Settings에서 재배포

1. **Settings → Build & Deploy**
   - 설정을 약간 변경 (예: Root Directory를 `.`로 설정)
   - **"Save"** 클릭
   - 자동으로 재배포 시작

#### 옵션 C: Service 메뉴에서

1. **서비스 카드에서**
   - 메인 대시보드의 서비스 카드에서
   - **"..." (3점 메뉴)** 클릭
   - **"Redeploy"** 또는 **"Restart"** 선택

---

### 방법 3: Settings 변경으로 트리거

1. **Settings → Build & Deploy**
   - 아무 설정이나 약간 변경 (예: Root Directory)
   - 다시 원래대로 변경
   - **"Save"** 클릭
   - 자동으로 재배포 시작

---

### 방법 4: 환경 변수 추가/수정

1. **Settings → Variables**
   - 임시 환경 변수 추가 (예: `REDEPLOY=1`)
   - **"Save"** 클릭
   - 재배포 시작됨
   - 필요 없으면 나중에 삭제

---

### 방법 5: 서비스 재시작

1. **서비스 카드에서**
   - 서비스 카드 클릭
   - **"Restart"** 버튼 클릭
   - 또는 Settings → Advanced → "Restart Service"

---

## 🔍 Railway UI 확인

### 최신 Railway UI에서:

1. **Deployments 탭**
   - 왼쪽 사이드바 → "Deployments"
   - 배포 목록 확인
   - 각 배포 카드에서:
     - 우측 상단 **"..."** 메뉴 클릭
     - 또는 배포 카드 클릭 → 상세 페이지에서 옵션 확인

2. **Service 메뉴**
   - 서비스 카드 → **"..."** 메뉴
   - "Redeploy", "Restart", "Settings" 옵션 확인

3. **Settings에서**
   - Settings → Build & Deploy
   - 설정 저장 시 자동 재배포

---

## 💡 가장 확실한 방법

### GitHub 푸시로 재배포 (추천)

로컬에서 다음 명령어 실행:

```bash
# 빈 커밋 생성하여 재배포 트리거
git commit --allow-empty -m "Trigger Railway redeploy"
git push
```

이 방법이 가장 확실하고 Railway가 자동으로 재배포를 시작합니다.

---

## 📝 체크리스트

재배포 전 확인:
- [ ] GitHub에 Dockerfile이 있는가?
- [ ] Railway가 올바른 저장소를 보고 있는가?
- [ ] Settings → Build & Deploy에서 Builder가 Dockerfile인가?
- [ ] Root Directory가 `.`인가?

---

**GitHub 푸시 방법이 가장 확실합니다!** 🚀

