# Railway PORT 에러 최종 해결

## 🔍 문제 재발

`Error: '$PORT' is not a valid port number.` 에러가 다시 발생했습니다.

이는 `loveallprince/loveall` 저장소의 Dockerfile이 아직 업데이트되지 않았기 때문입니다.

---

## ✅ 해결 방법: GitHub에서 Dockerfile 수정

### 방법 1: GitHub 웹에서 직접 수정 (가장 확실함)

#### 1단계: GitHub 저장소 접속
1. 브라우저에서 https://github.com/loveallprince/loveall 접속
2. `loveallprince` 계정으로 로그인

#### 2단계: Dockerfile 파일 열기
1. 저장소 루트에서 `Dockerfile` 클릭
2. 파일 내용 확인

#### 3단계: 편집
1. 오른쪽 상단의 **연필 아이콘 (✏️)** 클릭
2. **마지막 줄 (28번째 줄)** 찾기

**현재 (에러 발생):**
```dockerfile
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120 web_vocab_app:app
```

**수정 후:**
```dockerfile
CMD sh -c "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --threads 2 --timeout 120 web_vocab_app:app"
```

#### 4단계: 커밋
1. 페이지 하단의 **"Commit changes"** 섹션으로 이동
2. 커밋 메시지 입력: `fix: Dockerfile PORT 환경 변수 처리 수정`
3. **"Commit directly to the main branch"** 선택
4. **"Commit changes"** 버튼 클릭

#### 5단계: Railway 자동 재배포 확인
1. Railway 대시보드 접속: https://railway.app
2. **Deployments** 탭 확인
   - GitHub에 푸시되면 자동으로 재배포 시작
   - 새로운 배포가 "Building" 상태로 시작됨
3. **빌드 로그 확인**
   - `Error: '$PORT' is not a valid port number.` 에러가 사라져야 함
   - Gunicorn이 정상적으로 시작되어야 함

---

## 📋 전체 Dockerfile 내용 (복사용)

GitHub에서 Dockerfile을 완전히 교체하려면 다음 내용을 사용하세요:

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

## 🔍 변경 사항 설명

### 수정 전 (에러 발생):
```dockerfile
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120 web_vocab_app:app
```

**문제점:**
- `exec`는 환경 변수를 확장하지 않음
- `$PORT`가 그대로 문자열로 전달됨
- Gunicorn이 `'$PORT'`를 포트 번호로 인식하려고 해서 에러 발생

### 수정 후 (정상 작동):
```dockerfile
CMD sh -c "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --threads 2 --timeout 120 web_vocab_app:app"
```

**해결책:**
- `sh -c`를 사용하여 쉘에서 환경 변수 확장
- `${PORT:-5000}`는 PORT가 있으면 사용, 없으면 기본값 5000 사용
- 환경 변수가 올바르게 확장됨

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

## 🚀 빠른 해결 (단계별)

1. **GitHub 저장소 접속**
   - https://github.com/loveallprince/loveall

2. **Dockerfile 편집**
   - 연필 아이콘 클릭
   - 마지막 줄 수정

3. **커밋**
   - 커밋 메시지 입력
   - "Commit changes" 클릭

4. **Railway 확인**
   - Deployments 탭에서 자동 재배포 확인
   - 에러가 사라졌는지 확인

---

## 💡 중요 사항

- Railway는 연결된 GitHub 저장소 (`loveallprince/loveall`)의 Dockerfile을 사용합니다
- 로컬에 수정한 Dockerfile은 `kwiss22/loveall`에만 푸시되었습니다
- `loveallprince/loveall` 저장소의 Dockerfile도 수정해야 합니다

---

**GitHub 웹에서 Dockerfile을 수정하면 Railway가 자동으로 재배포합니다!** 🚀

