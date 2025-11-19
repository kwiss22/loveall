# 배포 가이드

## 📦 배포 방법

### 1. 로컬 네트워크 배포

같은 네트워크의 다른 기기에서 접근하려면:

#### 방법 1: 코드 수정
```python
# web_vocab_app.py의 start_server 함수 수정
def start_server(port: int = DEFAULT_PORT) -> None:
    # ...
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)
    # debug=False로 변경, host='0.0.0.0'으로 변경
```

#### 방법 2: 환경 변수 사용
```bash
# Windows
set FLASK_HOST=0.0.0.0
set FLASK_PORT=5000
python web_vocab_app.py

# Linux/Mac
export FLASK_HOST=0.0.0.0
export FLASK_PORT=5000
python web_vocab_app.py
```

접속 방법:
- 서버 IP 주소 확인: `ipconfig` (Windows) 또는 `ifconfig` (Linux/Mac)
- 다른 기기에서: `http://<서버-IP>:5000`

---

### 2. 프로덕션 배포 (Gunicorn 사용)

#### 설치
```bash
pip install gunicorn
```

#### 실행
```bash
# 기본 실행
gunicorn -w 4 -b 0.0.0.0:5000 web_vocab_app:app

# 더 많은 옵션
gunicorn -w 4 -b 0.0.0.0:5000 \
  --access-logfile access.log \
  --error-logfile error.log \
  --log-level info \
  web_vocab_app:app
```

#### systemd 서비스로 등록 (Linux)

`/etc/systemd/system/vocab-app.service` 파일 생성:
```ini
[Unit]
Description=English Vocabulary App
After=network.target

[Service]
User=your-username
WorkingDirectory=/path/to/game_english
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 web_vocab_app:app

[Install]
WantedBy=multi-user.target
```

서비스 시작:
```bash
sudo systemctl start vocab-app
sudo systemctl enable vocab-app
```

---

### 3. Nginx 리버스 프록시 설정

#### Nginx 설정 파일
`/etc/nginx/sites-available/vocab-app`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 정적 파일 직접 서빙 (선택적)
    location /static {
        alias /path/to/game_english/static;
        expires 30d;
    }
}
```

활성화:
```bash
sudo ln -s /etc/nginx/sites-available/vocab-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

### 4. HTTPS 설정 (Let's Encrypt)

#### Certbot 설치
```bash
sudo apt-get install certbot python3-certbot-nginx
```

#### SSL 인증서 발급
```bash
sudo certbot --nginx -d your-domain.com
```

자동 갱신 설정:
```bash
sudo certbot renew --dry-run
```

---

### 5. 클라우드 배포

#### Heroku
1. `Procfile` 생성:
   ```
   web: gunicorn -w 4 -b 0.0.0.0:$PORT web_vocab_app:app
   ```

2. 배포:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

#### PythonAnywhere
1. 파일 업로드
2. Web 앱 설정에서 WSGI 파일 설정
3. 정적 파일 경로 설정

#### AWS/Google Cloud/Azure
- 각 플랫폼의 가이드에 따라 배포
- Docker 컨테이너화 고려

---

## 🔒 보안 고려사항

### 프로덕션 환경 설정
```python
# web_vocab_app.py
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['DEBUG'] = False  # 프로덕션에서는 False
```

### 환경 변수 사용
```bash
# .env 파일 생성 (gitignore에 추가)
SECRET_KEY=your-secret-key
FLASK_ENV=production
```

---

## 📊 모니터링

### 로그 확인
```bash
# Gunicorn 로그
tail -f access.log
tail -f error.log

# systemd 로그
sudo journalctl -u vocab-app -f
```

### 성능 모니터링
- Gunicorn 워커 수 조정 (CPU 코어 수 * 2 + 1)
- Nginx 캐싱 설정
- 데이터베이스 사용 고려 (단어가 많아질 경우)

---

## 🔄 업데이트 방법

1. 코드 업데이트
2. 의존성 업데이트:
   ```bash
   pip install -r requirements.txt --upgrade
   ```
3. 서비스 재시작:
   ```bash
   sudo systemctl restart vocab-app
   ```

---

## 📝 체크리스트

배포 전 확인사항:
- [ ] `DEBUG = False` 설정
- [ ] `SECRET_KEY` 설정
- [ ] 데이터 백업
- [ ] 방화벽 설정 확인
- [ ] SSL 인증서 설정 (HTTPS)
- [ ] 로그 파일 경로 확인
- [ ] 정적 파일 경로 확인
- [ ] 환경 변수 설정

---

**배포 완료 후 정상 작동을 확인하세요!** 🚀

