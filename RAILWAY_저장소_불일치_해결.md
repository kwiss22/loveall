# Railway 저장소 불일치 해결 가이드

## ❌ 문제: Dockerfile을 찾을 수 없음

Railway가 `loveallprince/loveall` 저장소를 보고 있지만, Dockerfile은 `kwiss22/loveall`에 있습니다.

---

## ✅ 해결 방법

### 방법 1: Railway에서 올바른 저장소로 변경 (추천)

1. **Railway 대시보드 접속**
   - https://railway.app
   - 프로젝트 선택

2. **Settings → Source**
   - **Repository** 확인
   - 현재: `loveallprince/loveall`
   - 변경: `kwiss22/loveall`로 변경
   - 또는 저장소를 다시 연결

3. **저장소 재연결**
   - "Disconnect" 클릭
   - "Connect GitHub Repo" 클릭
   - `kwiss22/loveall` 선택
   - Branch: `main` 선택

4. **재배포**
   - 자동으로 재배포 시작

---

### 방법 2: loveallprince/loveall 저장소에 파일 푸시

`loveallprince/loveall` 저장소에 접근 권한이 있다면:

1. **원격 저장소 추가**
   ```bash
   git remote add loveallprince https://github.com/loveallprince/loveall.git
   ```

2. **해당 저장소에 푸시**
   ```bash
   git push loveallprince main
   ```

---

### 방법 3: Railway에서 저장소 확인

1. **Settings → Source**
   - Repository가 올바른지 확인
   - Branch가 `main`인지 확인
   - Root Directory가 `.`인지 확인

2. **Build & Deploy**
   - Builder: `Dockerfile`
   - Dockerfile Path: `Dockerfile`
   - Root Directory: `.`

---

## 🔍 확인 사항

### GitHub 저장소 확인

1. **kwiss22/loveall 저장소**
   - https://github.com/kwiss22/loveall
   - Dockerfile이 루트에 있는지 확인 ✅

2. **loveallprince/loveall 저장소**
   - https://github.com/loveallprince/loveall
   - Dockerfile이 있는지 확인
   - 없으면 추가 필요

---

## 💡 가장 빠른 해결

Railway 대시보드에서:
1. Settings → Source
2. Repository를 `kwiss22/loveall`로 변경
3. 또는 저장소를 재연결
4. 자동 재배포 시작

---

**Railway가 올바른 저장소를 보고 있는지 확인하세요!** 🎯

