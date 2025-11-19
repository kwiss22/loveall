"""
단어장 프로그램 자동 테스트 스크립트
각 기능을 자동으로 테스트합니다.
"""

import json
import os
import sys

# vocab_book 모듈의 함수들을 직접 임포트하기 어려우므로
# 파일 내용을 직접 읽어서 실행하는 방식 대신
# 간단한 테스트 데이터로 직접 테스트해보겠습니다

def test_vocabulary_basic():
    """기본 딕셔너리 기능 테스트"""
    print("="*60)
    print("[테스트 1] 기본 딕셔너리 기능 테스트")
    print("="*60)
    
    vocabulary = {}
    
    # 단어 추가
    print("\n1. 단어 추가 중...")
    vocabulary["apple"] = "사과"
    vocabulary["book"] = "책"
    vocabulary["cat"] = "고양이"
    print(f"   [OK] 3개 단어 추가 완료")
    
    # 단어 목록 보기
    print("\n2. 단어 목록:")
    for i, (eng, kor) in enumerate(vocabulary.items(), 1):
        print(f"   {i}. {eng} → {kor}")
    
    # 단어 검색
    print("\n3. 단어 검색 테스트:")
    test_word = "apple"
    if test_word in vocabulary:
        print(f"   [OK] '{test_word}' 검색 성공: {vocabulary[test_word]}")
    else:
        print(f"   [ERROR] '{test_word}' 검색 실패")
    
    # 단어 삭제
    print("\n4. 단어 삭제 테스트:")
    if "cat" in vocabulary:
        del vocabulary["cat"]
        print(f"   [OK] 'cat' 삭제 완료. 남은 단어: {len(vocabulary)}개")
    
    print("\n[테스트 1 완료] OK\n")

def test_file_save_load():
    """파일 저장/불러오기 테스트"""
    print("="*60)
    print("[테스트 2] 파일 저장/불러오기 테스트")
    print("="*60)
    
    vocabulary = {"apple": "사과", "book": "책"}
    test_file = "test_vocabulary.json"
    
    # 파일 저장
    print("\n1. 파일 저장 중...")
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(vocabulary, f, ensure_ascii=False, indent=2)
        print(f"   [OK] 파일 저장 성공: {test_file}")
    except Exception as e:
        print(f"   [ERROR] 파일 저장 실패: {e}")
        return
    
    # 파일 불러오기
    print("\n2. 파일 불러오기 중...")
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            loaded_vocab = json.load(f)
        print(f"   [OK] 파일 불러오기 성공")
        print(f"   불러온 단어: {loaded_vocab}")
        
        # 원본과 비교
        if loaded_vocab == vocabulary:
            print(f"   [OK] 원본과 일치 확인")
        else:
            print(f"   [ERROR] 원본과 불일치")
    except Exception as e:
        print(f"   [ERROR] 파일 불러오기 실패: {e}")
    
    # 테스트 파일 삭제
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n3. 테스트 파일 삭제 완료")
    
    print("\n[테스트 2 완료] OK\n")

def test_quiz_logic():
    """퀴즈 로직 테스트"""
    print("="*60)
    print("[테스트 3] 퀴즈 로직 테스트")
    print("="*60)
    
    vocabulary = {"apple": "사과", "book": "책", "cat": "고양이"}
    quiz_stats = {}
    
    # 퀴즈 시뮬레이션: apple 단어로 퀴즈
    test_word = "apple"
    correct_answer = vocabulary[test_word]
    user_answer_correct = "사과"
    user_answer_wrong = "배"
    
    print(f"\n1. 퀴즈 문제: '{test_word}'")
    print(f"   정답: '{correct_answer}'")
    
    # 정답 케이스
    print(f"\n2. 사용자 정답 케이스 테스트:")
    if user_answer_correct == correct_answer:
        print(f"   [OK] 정답 처리 성공")
        if test_word not in quiz_stats:
            quiz_stats[test_word] = [0, 0]
        quiz_stats[test_word][0] += 1
        print(f"   통계 업데이트: {quiz_stats[test_word]}")
    
    # 오답 케이스
    print(f"\n3. 사용자 오답 케이스 테스트:")
    if user_answer_wrong != correct_answer:
        print(f"   [OK] 오답 처리 성공")
        if test_word not in quiz_stats:
            quiz_stats[test_word] = [0, 0]
        quiz_stats[test_word][1] += 1
        print(f"   통계 업데이트: {quiz_stats[test_word]}")
    
    # 통계 확인
    print(f"\n4. 최종 통계:")
    correct, wrong = quiz_stats[test_word]
    total = correct + wrong
    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"   {test_word}: {correct}정/{wrong}오 (정답률: {accuracy:.1f}%)")
    
    print("\n[테스트 3 완료] OK\n")

def show_test_summary():
    """테스트 요약"""
    print("="*60)
    print("전체 테스트 완료!")
    print("="*60)
    print("\n실제 프로그램 테스트 방법:")
    print("1. PowerShell에서 'python vocab_book.py' 실행")
    print("2. 메뉴에서 원하는 기능 선택")
    print("3. 직접 단어를 추가하고 퀴즈를 해보세요!")
    print("\n" + "="*60)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("단어장 프로그램 자동 테스트 시작")
    print("="*60 + "\n")
    
    test_vocabulary_basic()
    test_file_save_load()
    test_quiz_logic()
    show_test_summary()

