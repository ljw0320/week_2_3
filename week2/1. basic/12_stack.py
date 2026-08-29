"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""
"""
LIFO : 후입선출
FIFO : 선입선출

"""
"""
괄호 짝이 맞는지 확인

Args:
    s: 괄호 문자열

Returns:
    올바른 괄호면 True, 아니면 False
"""
"""
사전지식
# 1) 스택(stack)
# 데이터를 쌓아두는 자료구조
# 특징: 나중에 들어온 데이터가 먼저 나온다(LIFO).
접시 C  ← 가장 나중에 올림, 가장 먼저 꺼냄
접시 B
접시 A
파이썬에서는 리스트로 구현
| 연산     | 의미         | Python            |
| -------- | ----------- | ----------------- |
| push     | 데이터 넣기      | `stack.append(x)` |
| pop      | 마지막 데이터 꺼내기 | `stack.pop()`     |
| peek/top | 마지막 데이터 확인  | `stack[-1]`       |
| empty    | 비어있는지 확인    | `if not stack:`   |

# 2) 삼항연산자
참일 때 값 if 조건 else 거짓일 때 값
조건이 참이면 값1, 조건이 거짓이면 값2
"""
    
# TODO: 문자열의 각 문자를 순회
## : 여는 괄호 '('면 스택에 추가
## : 닫는 괄호 ')'면
## 스택이 비어있으면 False 반환
## 아니면 스택에서 pop
pass

# TODO: 반복이 끝나면 스택이 비어있는지 확인
pass

def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        if char == ')':
            if not stack:  
                return False
            else : stack.pop()                
    return True if not stack else False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


