# Railway PORT 환경 변수 에러 해결

## 🔍 문제

```
Error: '$PORT' is not a valid port number.
```

Railway가 `$PORT` 환경 변수를 제대로 읽지 못해서 발생하는 오류입니다.

---

## ✅ 해결 방법

### Dockerfile 수정

Dockerfile의 CMD를 다음과 같이 수정했습니다:

**수정 전:**
```dockerfile
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120 web_vocab_app:app
```

**수정 후:**
```dockerfile
CMD sh -c "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --threads 2 --timeout 120 web_vocab_app:app"
```

**변경 사항:**
- `exec` 제거 (환경 변수를 읽기 위해 쉘 사용)
- `sh -c` 사용하여 쉘에서 환경 변수 확장
- `${PORT:-5000}` 사용하여 PORT가 없으면 기본값 5000 사용

---

## 🚀 적용 방법

### 방법 1: GitHub 웹에서 직접 수정 (추천)

1. **GitHub 저장소 접속**
   - https://github.com/loveallprince/loveall

2. **Dockerfile 파일 열기**
   - 저장소 루트에서 `Dockerfile` 클릭

3. **편집 버튼 클릭**
   - 오른쪽 상단의 연필 아이콘 (✏️) 클릭

4. **CMD 라인 수정**
   - 마지막 줄을 다음과 같이 변경:
   ```dockerfile
   CMD sh -c "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --threads 2 --timeout 120 web_vocab_app:app"
   ```

5. **커밋**
   - 커밋 메시지: `fix: Dockerfile PORT 환경 변수 처리 수정`
   - "Commit changes" 클릭

6. **Railway 자동 재배포**
   - GitHub에 푸시되면 Railway가 자동으로 재배포 시작
   - Deployments 탭에서 확인

---

### 방법 2: 로컬에서 수정 후 푸시 (권한이 있다면)

```bash
# Dockerfile 수정 (이미 수정됨)
git add Dockerfile
git commit -m "fix: Dockerfile PORT 환경 변수 처리 수정"
git push loveallprince main
```

---

## 📋 전체 Dockerfile 내용

수정된 전체 Dockerfile:

```dockerfile
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY web_vocab_app.py .
COPY templates/ templates/
COPY static/ static/
COPY vocabulary.json .
COPY quiz_stats.json .

# 포트 환경 변수 (Railway가 자동으로 설정)
ENV PORT=5000
EXPOSE $PORT

# Gunicorn으로 Flask 앱 실행 (환경 변수를 제대로 읽도록 쉘 사용)
CMD sh -c "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --threads 2 --timeout 120 web_vocab_app:app"
```

---

## ✅ 확인 사항

수정 후 Railway에서:

1. **Deployments 탭 확인**
   - 새로운 배포가 시작됨
   - 빌드 로그 확인

2. **에러 메시지 확인**
   - `Error: '$PORT' is not a valid port number.` 에러가 사라져야 함
   - Gunicorn이 정상적으로 시작되어야 함

3. **배포 성공 확인**
   - 배포 상태가 "Active"가 되어야 함
   - 서비스 URL로 접속 가능해야 함

---

## 🔍 추가 문제 해결

### 여전히 에러가 발생하면:

1. **Railway 환경 변수 확인**
   - Settings → Variables
   - `PORT` 환경 변수가 있는지 확인
   - 없으면 Railway가 자동으로 설정하므로 문제없음

2. **빌드 로그 확인**
   - Deployments → 최신 배포 → Logs
   - 에러 메시지 확인

3. **Dockerfile 문법 확인**
   - CMD 라인이 올바른지 확인
   - 따옴표가 올바르게 사용되었는지 확인

---

## 💡 참고 사항

- Railway는 자동으로 `PORT` 환경 변수를 설정합니다
- `${PORT:-5000}`는 PORT가 없으면 기본값 5000을 사용합니다
- `sh -c`를 사용하여 쉘에서 환경 변수를 확장합니다

---

**GitHub 웹에서 Dockerfile을 수정하면 Railway가 자동으로 재배포합니다!** 🚀

