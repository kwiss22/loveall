"""
빠른 시작 스크립트 - Flask 앱을 안전하게 실행
"""

import sys
import os

def check_dependencies():
    """필요한 파일과 모듈 확인"""
    print("="*60)
    print("시작 전 확인 중...")
    print("="*60)
    
    # Flask 확인
    try:
        import flask
        print(f"[OK] Flask 설치됨 (버전: {flask.__version__})")
    except ImportError:
        print("[ERROR] Flask가 설치되지 않았습니다.")
        print("다음 명령어로 설치하세요: pip install flask")
        return False
    
    # 필요한 파일 확인
    files_to_check = [
        'web_vocab_app.py',
        'templates/index.html',
        'static/style.css',
        'static/script.js'
    ]
    
    all_ok = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"[OK] {file} 존재함")
        else:
            print(f"[ERROR] {file} 없음")
            all_ok = False
    
    print("="*60)
    return all_ok

def main():
    """메인 함수"""
    if not check_dependencies():
        print("\n[ERROR] 필요한 파일이나 모듈이 없습니다.")
        print("위의 오류를 해결한 후 다시 시도하세요.")
        input("\n계속하려면 Enter 키를 누르세요...")
        return
    
    print("\n" + "="*60)
    print("Flask 웹 앱을 시작합니다...")
    print("="*60)
    print("\n중요:")
    print("1. 이 창을 닫지 마세요!")
    print("2. 브라우저에서 http://127.0.0.1:5000 으로 접속하세요")
    print("3. 종료하려면 Ctrl+C를 누르세요")
    print("="*60 + "\n")
    
    try:
        # web_vocab_app 모듈 실행
        import web_vocab_app
        print("\n[OK] 웹 앱이 시작되었습니다!")
        print("[OK] 브라우저에서 http://127.0.0.1:5000 으로 접속하세요\n")
    except Exception as e:
        print(f"\n[ERROR] 웹 앱 시작 실패: {e}")
        import traceback
        traceback.print_exc()
        input("\n계속하려면 Enter 키를 누르세요...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 종료되었습니다.")
    except Exception as e:
        print(f"\n[ERROR] 예상치 못한 오류: {e}")
        input("\n계속하려면 Enter 키를 누르세요...")

