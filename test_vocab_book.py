"""
단어장 프로그램 테스트 가이드
이 파일을 실행하면 자동으로 테스트가 진행됩니다.
"""

import subprocess
import sys
import os

def run_test():
    """자동 테스트 스크립트"""
    print("="*60)
    print("단어장 프로그램 테스트 가이드")
    print("="*60)
    print("\n[테스트 1] 프로그램을 직접 실행해서 테스트하기")
    print("-"*60)
    print("터미널에서 다음 명령어를 실행하세요:")
    print("  python vocab_book.py")
    print("\n그 다음 다음 순서로 테스트하세요:")
    print()
    print("1. 단어 추가하기")
    print("   - 메뉴에서 '1' 선택")
    print("   - 예시: 영어 단어 'apple', 한글 뜻 '사과'")
    print("   - 예시: 영어 단어 'book', 한글 뜻 '책'")
    print("   - 예시: 영어 단어 'cat', 한글 뜻 '고양이'")
    print()
    print("2. 단어 목록 보기")
    print("   - 메뉴에서 '2' 선택")
    print("   - 추가한 단어들이 보이는지 확인")
    print()
    print("3. 단어 검색하기")
    print("   - 메뉴에서 '3' 선택")
    print("   - 'apple' 검색해서 정상적으로 나오는지 확인")
    print()
    print("4. 퀴즈 해보기 (영어 → 한글)")
    print("   - 메뉴에서 '5' 선택")
    print("   - 영어 단어가 나오면 한글 뜻 입력")
    print("   - 정답/오답 여부 확인")
    print()
    print("5. 퀴즈 해보기 (한글 → 영어)")
    print("   - 메뉴에서 '6' 선택")
    print("   - 한글 뜻이 나오면 영어 단어 입력")
    print("   - 정답/오답 여부 확인")
    print()
    print("6. 퀴즈 통계 보기")
    print("   - 메뉴에서 '7' 선택")
    print("   - 각 단어별 정답률 확인")
    print()
    print("7. 파일 저장하기")
    print("   - 메뉴에서 '8' 선택")
    print("   - 'vocabulary.json' 파일이 생성되는지 확인")
    print()
    print("8. 프로그램 종료 후 다시 실행")
    print("   - 메뉴에서 '0' 선택, 저장 확인")
    print("   - 다시 실행하면 파일에서 자동으로 불러오는지 확인")
    print()
    print("="*60)
    print("\n준비되셨으면 터미널에서 'python vocab_book.py' 실행하세요!")
    print("="*60)

if __name__ == "__main__":
    run_test()

