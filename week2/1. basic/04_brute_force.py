"""
[완전 탐색 - 배열에서 두 수의 합 찾기]

문제 설명:
- 정수 배열과 목표 값이 주어졌을 때, 배열에서 두 수를 선택하여 
  그 합이 목표 값과 같아지는 모든 쌍을 찾습니다.
- 완전 탐색(Brute Force) 방식으로 모든 경우를 확인합니다.

입력:
- nums: 정수 배열
- target: 목표 합

출력:
- 합이 target이 되는 (i, j) 인덱스 쌍의 리스트 (i < j)

예제:
입력: nums = [2, 7, 11, 15, 3], target = 9
출력: [(0, 1), (0, 4)]
설명: nums[0] + nums[1] = 2 + 7 = 9
      nums[0] + nums[4] = 2 + 7 = 9 (중복이지만 인덱스가 다름)

실제로는: nums[0] + nums[1] = 2 + 7 = 9만 해당

힌트:
- 이중 반복문을 사용하여 모든 쌍을 확인하세요
- i < j 조건을 유지하여 중복을 방지하세요
"""

"""
    배열에서 합이 target이 되는 모든 인덱스 쌍 찾기
    
    Args:
        nums: 정수 배열
        target: 목표 합
    
    Returns:
        list: (i, j) 인덱스 쌍의 리스트
"""
# TODO: 이중 반복문으로 모든 쌍을 확인하세요
## 외부 반복문: i는 0부터 n-1까지
## 내부 반복문: j는 i+1부터 n까지 (중복 방지)
## nums[i] + nums[j]가 target과 같으면 (i, j)를 결과에 추가
pass  

"""
사전지식 
1. 이중 반복문
반복문 안에 또다른 반복문이 들어있는 구조
보통 for문을 중첩해서 사용
for i in range(3):
    for j in range(2):
        print(i, j)
반복 구조는 아래와 같이 외부 반복문이 1번 실행되고, 내부 반복문이 모두 실행되는 구조
i = 0
    j = 0
    j = 1

i = 1
    j = 0
    j = 1

i = 2
    j = 0
    j = 1

2차원 배열(리스트) 다룰 때 많이 사용

array = [
    [1, 2, 3],
    [4, 5, 6]
]

for i in range(2):
    for j in range(3):
        print(array[i][j])

i → 행
j → 열
array[i][j] → i번째 행의 j번째 값        

array[0][0]  # 1
array[0][2]  # 3
array[1][1]  # 5

2. 조건문 논리 연산자
and: 둘 다 참일때 참
or: 둘 중 하나라도 참이면 참
not: 참/거짓을 반대로

3. 완전 탐색 
가능한 모든 경우의 수를 하나씩 전부 확인하는 방법
대표적으로,
-단순 반복문
-이중/삼중 반복문
-재귀
-순열/조합
-DFS/BFS를 이용한 모든 경우 탐색

장점 : 모든 경우를 확인하기 때문에 놓치는게 없음
단점 : 경우의 수가 많을 수록 느려짐
"""
def find_two_sum_pairs(nums, target):    
    pairs = []
    n = len(nums)

    for i in range(n-1):
        j = i+1
        for j in range(n):
            if (nums[i]+nums[j] == target and i < j):
                pair = (i,j)
                pairs.append(pair)            
    return pairs

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_two_sum_pairs(nums1, target1)
    print(f"배열: {nums1}")
    print(f"목표 합: {target1}")
    print(f"결과 쌍: {result1}")
    print()
    
    # 테스트 케이스 2
    nums2 = [1, 3, 4, 2, 5, 6]
    target2 = 7
    result2 = find_two_sum_pairs(nums2, target2)
    print(f"배열: {nums2}")
    print(f"목표 합: {target2}")
    print(f"결과 쌍: {result2}")
    print()
    
    # 테스트 케이스 3
    nums3 = [1, 1, 1, 1]
    target3 = 2
    result3 = find_two_sum_pairs(nums3, target3)
    print(f"배열: {nums3}")
    print(f"목표 합: {target3}")
    print(f"결과 쌍: {result3}")


