"""
[정수론 - 최대공약수(GCD)와 최소공배수(LCM)]

문제 설명:
- 두 정수의 최대공약수(GCD)와 최소공배수(LCM)를 구합니다.
- 유클리드 호제법을 사용하여 GCD를 효율적으로 계산합니다.
- GCD를 이용하여 LCM을 계산합니다.

입력:
- a, b: 두 개의 양의 정수

출력:
- GCD: 최대공약수
- LCM: 최소공배수

예제:
입력: a = 48, b = 18
출력: 
  GCD = 6
  LCM = 144

힌트:
- 유클리드 호제법: gcd(a, b) = gcd(b, a % b)
- LCM 공식: lcm(a, b) = (a × b) / gcd(a, b)
"""

"""
유클리드 호제법을 사용한 최대공약수 계산

Args:
    a, b: 두 양의 정수

Returns:
    최대공약수
"""

import math

# TODO: 유클리드 호제법 구현
# base case: b가 0이면 a 반환
# recursive를 이용 
pass

def gcd(a, b):
    if (b==0): return a # 나머지가 0인 경우
    return gcd(b, a%b)

# gcd(4,16)
# 1) return gcd(16, 0)
# 2) b = 0 이므로 a인 4 반환

"""
반복문을 사용한 최대공약수 계산

Args:
    a, b: 두 양의 정수

Returns:
    최대공약수
"""
# TODO: 반복문으로 구현
# b가 0이 될 때까지 반복
pass

# 문제점 : 나눠주는 수(제수)를 어떤 규칙으로 정할것인가?
# 자연수 : 소수 + 소수가 아닌 자연수
# 1. 소수 인 경우 : 1과 자기 자신으로만 나눠짐(17,31 등)
# 2. 소수가 아닌 경우 : 소수들 간의 곱으로 이루어짐(38=2*19 등)
# 1,2 모두 소수로 나눌 수 있음 

# case 1) 둘 다 소수
    # 최대 공약수는 1

# case 2) 둘 다 소수가 아닌 자연수
#   둘 중 작은 수를 구한다. N>n이면 
#   1) N%n==0이면 최대공약수는 n
#   2) 2로 나눈 후 나머지가 0이 아니면 종료한다.

# case 3) 한쪽은 소수(P), 한쪽은 소수가 아닌 자연수(N)
# - P>N: 최대 공약수는 1
# - P<N: 
#   N%P==0일 때, P가 최대 공약수. 
#   N%P!=0일 때, 최대공약수는 1

def gcd_iterative(a, b):    
    #최대공약수 선언
    qcd = 1
    primeCheck_a = primeCheck_b = False
    if is_prime(a):
        primeCheck_a = True
    if is_prime(b):
        primeCheck_b = True
    #case 1) 한쪽은 소수(P), 한쪽은 소수가 아닌 자연수(N)
    if (primeCheck_a and primeCheck_b): 
        return 1
    #case 2) 둘 다 소수가 아닌 자연수
    if (primeCheck_a == False and primeCheck_b == False):
        if (a >= b):
            if (a%b==0): 
                return b
            for i in range(b):
                if i>=2 and a%i==0:
                    qcd = qcd*i


        

    

def lcm(a, b):
    """
    최소공배수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최소공배수
    """
    # TODO: LCM 계산
    pass

def extended_gcd(a, b):
    """
    확장 유클리드 호제법
    ax + by = gcd(a, b)를 만족하는 x, y를 찾음
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        (gcd, x, y) 튜플
    """
    # TODO: 확장 유클리드 호제법 구현
    # base case: b가 0이면 (a, 1, 0) 반환    
    # recursive case
    # 역추적하며 x, y 계산
    pass

"""
소수 판별

Args:
    n: 판별할 양의 정수

Returns:
    소수이면 True, 아니면 False
"""
# TODO: 소수 판별 구현
# n이 2보다 작으면 False
# 2부터 sqrt(n)까지 나누어 떨어지는지 확인    
# 3부터 sqrt(n)까지 홀수만 확인
pass 

def is_prime(n):    
    if n < 2: return False
    if n == 2: return True    

    # 2 ~ sqrt(n)까지 나누어 떨어지는지 확인
    num = int(math.sqrt(n))
    for i in range(num):
        if i>=2 and n%i == 0: return False

    # 3 ~ sqrt(n)까지 나누어 떨어지는지 확인(홀수)
    if not (n%2 == 0):
        for j in range(num):
            if j>=3 and n%j == 0: return False

    return True

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")


