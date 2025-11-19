"""
빠른 테스트 - 프로그램이 정상 작동하는지 확인
이 스크립트는 자동으로 테스트를 진행합니다.
"""

import os
import sys

def check_files():
    """필요한 파일들이 있는지 확인"""
    print("="*60)
    print("파일 확인 중...")
    print("="*60)
    
    required_file = "vocab_book.py"
    if os.path.exists(required_file):
        print(f"[OK] {required_file} 파일이 있습니다.")
    else:
        print(f"[ERROR] {required_file} 파일을 찾을 수 없습니다.")
        return False
    
    return True

def check_imports():
    """필요한 모듈들이 정상적으로 임포트되는지 확인"""
    print("\n" + "="*60)
    print("모듈 임포트 확인 중...")
    print("="*60)
    
    modules = ['json', 'random', 'os']
    all_ok = True
    
    for module in modules:
        try:
            __import__(module)
            print(f"[OK] {module} 모듈 임포트 성공")
        except ImportError:
            print(f"[ERROR] {module} 모듈을 임포트할 수 없습니다.")
            all_ok = False
    
    return all_ok

def check_syntax():
    """Python 문법 오류 확인"""
    print("\n" + "="*60)
    print("문법 오류 확인 중...")
    print("="*60)
    
    try:
        with open("vocab_book.py", 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, "vocab_book.py", "exec")
        print("[OK] 문법 오류가 없습니다.")
        return True
    except SyntaxError as e:
        print(f"[ERROR] 문법 오류 발견: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] 파일을 읽을 수 없습니다: {e}")
        return False

def show_manual_test_instructions():
    """수동 테스트 안내"""
    print("\n" + "="*60)
    print("수동 테스트 시작 방법")
    print("="*60)
    print("\n다음 명령어를 입력하세요:")
    print("  python vocab_book.py")
    print("\n그 다음:")
    print("1. 메뉴에서 '1'을 선택하고 단어를 추가하세요")
    print("   예: apple → 사과")
    print("\n2. 메뉴에서 '2'를 선택하고 목록을 확인하세요")
    print("\n3. 메뉴에서 '5'를 선택하고 퀴즈를 해보세요")
    print("\n4. 메뉴에서 '7'을 선택하고 통계를 확인하세요")
    print("\n5. 메뉴에서 '8'을 선택하고 파일을 저장하세요")
    print("\n6. 메뉴에서 '0'을 선택하고 종료하세요")
    print("\n자세한 가이드는 TEST_GUIDE.md 파일을 참고하세요!")
    print("="*60 + "\n")

def main():
    print("\n" + "="*60)
    print("단어장 프로그램 사전 검사")
    print("="*60 + "\n")
    
    # 파일 확인
    if not check_files():
        print("\n[중단] 필수 파일이 없습니다.")
        return
    
    # 모듈 확인
    if not check_imports():
        print("\n[경고] 일부 모듈을 찾을 수 없지만 계속 진행합니다.")
    
    # 문법 확인
    if not check_syntax():
        print("\n[중단] 문법 오류가 있습니다. 수정 후 다시 시도하세요.")
        return
    
    print("\n" + "="*60)
    print("모든 사전 검사 통과!")
    print("="*60)
    
    # 수동 테스트 안내
    show_manual_test_instructions()

if __name__ == "__main__":
    main()

