"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""

# 아이디어 : 문제를 어떻게 해결할 것인가?
# 1. 받은 입력을 변수에 저장한다.
# 2. 변수에서 알파벳, 숫자를 제외한 문자를 제거한다. isalnum() 메서드
# 3. 변수를 모두 소문자로 변환한다. lower() 메서드
# 4-1. 문자열을 뒤집는 방식을 이용해서 비교한다. [::-1] 사용
# 4-2. 양 끝 인덱스를 이용한 투 포인터 방식을 이용한다.

# 핵심 문제점 : isalnum()을 사용하면 공백이나 특수문자가 있으면 False를 반환한다
# 주어진 문제는 특수문자나 공백이 있다면 무시해야 한다.
# 따라서 text.isalnum()을 바로 사용하지 않고 가공해야한다.
## 아이디어 1 
# 문자열의 길이와 같은 배열 생성
# 생성된 배열에 인덱스마다 문자열의 문자를 하나씩 삽입한다.
# 각 문자에 대해 isalnum()을 사용한다. 
# True인 배열만 모아서 문자열을 생성한다.
# 생성된 문자열이 회문인지 검사한다.

# 사전 지식
## 1. isalnum() ##
# python의 문자열 메서드.
# 문자열이 오직 문자(알파벳, 한글 등)와 숫자로만 이루어져 있는지 검사.
# 문자열.isalnum()
# 조건 1. 문자열이 비어있지 않아야 함.
# 조건 2. 모든 문자가 문자 또는 숫자여야 함.
# - case - 
# print("hello123".isalnum())   # True
# print("hello".isalnum())      # True
# print("12345".isalnum())      # True
# print("안녕123".isalnum())     # True

# print("hello 123".isalnum())  # False → 공백
# print("hello!".isalnum())     # False → !
# print("abc_123".isalnum())    # False → _
# print("".isalnum())           # False → 빈 문자열

# isalnum() 코드 내부 구조 예시
# def isalnum_example(text):
#     if len(text) == 0:
#         return False

#     for char in text:
#         if not (char.isalpha() or char.isdigit()):
#             return False

#     return True

## 2. lower() ##
문자열 안의 영문 대문자를 소문자로 바꿔서 새로운 문자열을 반환

def is_palindrome(s):        
    if not (s.isalnum())        
        if len(s) == 0: # 문자열 길이가 0이면 바로 False 반환
            return False
        

    """
    문자열이 회문인지 판별하는 함수
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용
    pass
    
    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투 포인터 방식
    pass
    
    #return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


