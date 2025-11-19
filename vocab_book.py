"""
영어 단어장 프로그램
기본 기능: 단어 추가, 목록 보기, 파일 저장/불러오기, 퀴즈
"""

import json
import random
import os

# 단어장을 저장할 딕셔너리 (영어 단어: 한국어 뜻)
vocabulary = {}
# 퀴즈 통계를 저장할 딕셔너리 (영어 단어: [맞춘 횟수, 틀린 횟수])
quiz_stats = {}

# 파일 이름
VOCAB_FILE = "vocabulary.json"
STATS_FILE = "quiz_stats.json"

def add_word():
    """단어 추가 함수"""
    english = input("영어 단어를 입력하세요: ").strip().lower()
    korean = input("한국어 뜻을 입력하세요: ").strip()
    
    if english and korean:
        vocabulary[english] = korean
        print(f"[OK] '{english}' 단어가 추가되었습니다!")
    else:
        print("[ERROR] 단어와 뜻을 모두 입력해주세요.")

def show_words():
    """단어 목록 보기 함수"""
    if not vocabulary:
        print("[INFO] 저장된 단어가 없습니다.")
        return
    
    print("\n" + "="*40)
    print("단어장 목록")
    print("="*40)
    
    for i, (english, korean) in enumerate(vocabulary.items(), 1):
        print(f"{i}. {english} → {korean}")
    
    print(f"\n총 {len(vocabulary)}개의 단어가 저장되어 있습니다.")
    print("="*40 + "\n")

def search_word():
    """단어 검색 함수"""
    word = input("검색할 단어를 입력하세요: ").strip().lower()
    
    if word in vocabulary:
        print(f"[OK] {word} → {vocabulary[word]}")
    else:
        print(f"[ERROR] '{word}' 단어를 찾을 수 없습니다.")

def delete_word():
    """단어 삭제 함수"""
    word = input("삭제할 단어를 입력하세요: ").strip().lower()
    
    if word in vocabulary:
        del vocabulary[word]
        if word in quiz_stats:
            del quiz_stats[word]
        print(f"[OK] '{word}' 단어가 삭제되었습니다.")
    else:
        print(f"[ERROR] '{word}' 단어를 찾을 수 없습니다.")

def save_to_file():
    """단어장을 파일에 저장하는 함수"""
    try:
        with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
            json.dump(vocabulary, f, ensure_ascii=False, indent=2)
        
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(quiz_stats, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] 파일 저장 완료! (단어: {len(vocabulary)}개)")
        return True
    except Exception as e:
        print(f"[ERROR] 파일 저장 실패: {e}")
        return False

def load_from_file():
    """파일에서 단어장을 불러오는 함수"""
    global vocabulary, quiz_stats
    
    try:
        if os.path.exists(VOCAB_FILE):
            with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
                vocabulary = json.load(f)
            print(f"[OK] 단어장 불러오기 완료! (단어: {len(vocabulary)}개)")
        
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, 'r', encoding='utf-8') as f:
                quiz_stats = json.load(f)
            print(f"[OK] 퀴즈 통계 불러오기 완료!")
        
        return True
    except Exception as e:
        print(f"[ERROR] 파일 불러오기 실패: {e}")
        return False

def quiz_english_to_korean():
    """영어 → 한글 퀴즈"""
    if not vocabulary:
        print("[INFO] 퀴즈를 하려면 먼저 단어를 추가해주세요.")
        return
    
    # 랜덤으로 단어 선택
    words = list(vocabulary.keys())
    word = random.choice(words)
    correct_answer = vocabulary[word]
    
    print("\n" + "="*40)
    print("퀴즈: 영어 → 한글")
    print("="*40)
    print(f"영어 단어: {word}")
    
    user_answer = input("한국어 뜻을 입력하세요: ").strip()
    
    if user_answer == correct_answer:
        print(f"[OK] 정답입니다! '{word}' → '{correct_answer}'")
        # 통계 업데이트
        if word not in quiz_stats:
            quiz_stats[word] = [0, 0]
        quiz_stats[word][0] += 1  # 맞춘 횟수 증가
    else:
        print(f"[WRONG] 틀렸습니다. 정답은 '{correct_answer}' 입니다.")
        # 통계 업데이트
        if word not in quiz_stats:
            quiz_stats[word] = [0, 0]
        quiz_stats[word][1] += 1  # 틀린 횟수 증가
    
    print("="*40 + "\n")

def quiz_korean_to_english():
    """한글 → 영어 퀴즈"""
    if not vocabulary:
        print("[INFO] 퀴즈를 하려면 먼저 단어를 추가해주세요.")
        return
    
    # 랜덤으로 단어 선택
    words = list(vocabulary.keys())
    word = random.choice(words)
    correct_answer = word
    korean_meaning = vocabulary[word]
    
    print("\n" + "="*40)
    print("퀴즈: 한글 → 영어")
    print("="*40)
    print(f"한국어 뜻: {korean_meaning}")
    
    user_answer = input("영어 단어를 입력하세요: ").strip().lower()
    
    if user_answer == correct_answer:
        print(f"[OK] 정답입니다! '{korean_meaning}' → '{correct_answer}'")
        # 통계 업데이트
        if word not in quiz_stats:
            quiz_stats[word] = [0, 0]
        quiz_stats[word][0] += 1  # 맞춘 횟수 증가
    else:
        print(f"[WRONG] 틀렸습니다. 정답은 '{correct_answer}' 입니다.")
        # 통계 업데이트
        if word not in quiz_stats:
            quiz_stats[word] = [0, 0]
        quiz_stats[word][1] += 1  # 틀린 횟수 증가
    
    print("="*40 + "\n")

def show_quiz_stats():
    """퀴즈 통계 보기"""
    if not quiz_stats:
        print("[INFO] 퀴즈 통계가 없습니다. 먼저 퀴즈를 해보세요!")
        return
    
    print("\n" + "="*40)
    print("퀴즈 통계")
    print("="*40)
    
    for word, stats in sorted(quiz_stats.items()):
        correct, wrong = stats
        total = correct + wrong
        if total > 0:
            accuracy = (correct / total) * 100
            print(f"{word} ({vocabulary.get(word, '?')}): {correct}정/{wrong}오 (정답률: {accuracy:.1f}%)")
        else:
            print(f"{word} ({vocabulary.get(word, '?')}): 통계 없음")
    
    print("="*40 + "\n")

# 메인 메뉴
def main_menu():
    """메인 메뉴 함수"""
    while True:
        print("\n" + "="*40)
        print("영어 단어장 프로그램")
        print("="*40)
        print("1. 단어 추가")
        print("2. 단어 목록 보기")
        print("3. 단어 검색")
        print("4. 단어 삭제")
        print("5. 퀴즈 (영어 → 한글)")
        print("6. 퀴즈 (한글 → 영어)")
        print("7. 퀴즈 통계 보기")
        print("8. 파일 저장")
        print("9. 파일 불러오기")
        print("0. 종료")
        print("="*40)
        
        choice = input("선택하세요 (0-9): ").strip()
        
        if choice == "1":
            add_word()
        elif choice == "2":
            show_words()
        elif choice == "3":
            search_word()
        elif choice == "4":
            delete_word()
        elif choice == "5":
            quiz_english_to_korean()
        elif choice == "6":
            quiz_korean_to_english()
        elif choice == "7":
            show_quiz_stats()
        elif choice == "8":
            save_to_file()
        elif choice == "9":
            load_from_file()
        elif choice == "0":
            # 종료 전에 파일 저장 확인
            if vocabulary:
                save_choice = input("종료 전에 파일에 저장하시겠습니까? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_to_file()
            print("[BYE] 프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("[ERROR] 잘못된 선택입니다. 0-9 중에서 선택해주세요.")

# 프로그램 시작
if __name__ == "__main__":
    print("[WELCOME] 영어 단어장 프로그램에 오신 것을 환영합니다!")
    
    # 프로그램 시작 시 자동으로 파일 불러오기
    if os.path.exists(VOCAB_FILE):
        load_from_file()
    
    main_menu()

