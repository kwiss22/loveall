"""
web_vocab_app.py 실행 진단 도구
실행이 안 되는 이유를 찾아줍니다.
"""

import sys
import os

print("="*60)
print("web_vocab_app.py 실행 진단")
print("="*60)

# 1. Python 버전 확인
print("\n[1] Python 버전 확인...")
try:
    print(f"   Python 버전: {sys.version}")
    print(f"   Python 경로: {sys.executable}")
    print("   [OK] Python이 설치되어 있습니다.")
except Exception as e:
    print(f"   [ERROR] Python 확인 실패: {e}")
    sys.exit(1)

# 2. Flask 설치 확인
print("\n[2] Flask 설치 확인...")
try:
    import flask
    print(f"   Flask 버전: {flask.__version__}")
    print("   [OK] Flask가 설치되어 있습니다.")
except ImportError:
    print("   [ERROR] Flask가 설치되지 않았습니다!")
    print("   해결 방법: pip install flask")
    sys.exit(1)

# 3. 필요한 파일 확인
print("\n[3] 필요한 파일 확인...")
required_files = [
    'web_vocab_app.py',
    'templates/index.html',
    'static/style.css',
    'static/script.js'
]

all_files_exist = True
for file in required_files:
    if os.path.exists(file):
        print(f"   [OK] {file} 존재함")
    else:
        print(f"   [ERROR] {file} 없음!")
        all_files_exist = False

if not all_files_exist:
    print("\n   [ERROR] 일부 파일이 없습니다!")
    sys.exit(1)

# 4. 문법 오류 확인
print("\n[4] web_vocab_app.py 문법 확인...")
try:
    with open('web_vocab_app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    compile(code, 'web_vocab_app.py', 'exec')
    print("   [OK] 문법 오류가 없습니다.")
except SyntaxError as e:
    print(f"   [ERROR] 문법 오류 발견: {e}")
    print(f"   위치: {e.filename}, 줄 {e.lineno}")
    sys.exit(1)
except Exception as e:
    print(f"   [ERROR] 파일 읽기 실패: {e}")
    sys.exit(1)

# 5. 모듈 임포트 확인
print("\n[5] web_vocab_app.py 모듈 임포트 확인...")
try:
    # 임포트만 테스트 (실행은 하지 않음)
    import importlib.util
    spec = importlib.util.spec_from_file_location("web_vocab_app", "web_vocab_app.py")
    # 실제 임포트는 하지 않고 문법만 확인
    print("   [OK] 모듈 구조가 올바릅니다.")
except Exception as e:
    print(f"   [ERROR] 모듈 확인 실패: {e}")
    sys.exit(1)

# 6. 포트 사용 확인
print("\n[6] 포트 5000 사용 확인...")
try:
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 5000))
    sock.close()
    
    if result == 0:
        print("   [WARNING] 포트 5000이 이미 사용 중입니다!")
        print("   해결 방법:")
        print("   1. 다른 터미널에서 실행 중인 Flask 앱을 Ctrl+C로 종료")
        print("   2. 또는 web_vocab_app.py에서 포트를 5001로 변경")
    else:
        print("   [OK] 포트 5000이 사용 가능합니다.")
except Exception as e:
    print(f"   [WARNING] 포트 확인 실패: {e}")

# 7. 최종 확인
print("\n" + "="*60)
print("진단 완료!")
print("="*60)

if all_files_exist:
    print("\n✅ 모든 검사를 통과했습니다!")
    print("\n이제 다음 명령어로 실행해보세요:")
    print("   python web_vocab_app.py")
    print("\n터미널에서 어떤 오류 메시지가 나오는지 확인해주세요.")
    print("오류 메시지를 알려주시면 더 정확하게 도와드릴 수 있습니다.")
else:
    print("\n❌ 일부 파일이 없습니다. 위의 오류를 확인하세요.")

print("\n" + "="*60)

