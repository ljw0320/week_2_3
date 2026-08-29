"""
[복잡도 분석 - Big O, 시간 복잡도, 공간 복잡도]

문제 설명:
- 여러 알고리즘의 시간 복잡도와 공간 복잡도를 이해하고 비교합니다.
- 동일한 문제를 다른 복잡도로 해결하는 방법을 학습합니다.
- 배열에서 중복 원소를 찾는 문제를 여러 방법으로 구현합니다.

입력:
- nums: 정수 배열

출력:
- 중복된 원소들의 리스트

예제:
입력: [4, 3, 2, 7, 8, 2, 3, 1]
출력: [2, 3]

힌트:
- 방법1: 이중 반복문 (O(n²) 시간, O(1) 공간)
- 방법2: 정렬 후 탐색 (O(n log n) 시간, O(1) 공간)
- 방법3: 해시 집합 사용 (O(n) 시간, O(n) 공간)
"""
"""
사전지식
1. for i in range(n)
# 반복횟수를 지정할 경우 range(n)과 같이 표현한다.

2. 정렬[sort()]
# 리스트 안의 원소들을 '서로 비교해서' 정렬된 순서로 재배치한다.
# 기본적으로 오름차순이다.
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)
결과 : [1, 2, 3, 5, 8]

# 1) 원본 리스트를 직접 바꾼다.
# 새로운 리스트를 만드는 게 아닌 기존 리스트의 내부 순서를 변경한다.
# => 정렬 결과를 반환하지 않고 원본만 수정한다.

# 2) 정렬을 하나씩 하는게 아닌 Timsort라는 정렬 알고리즘을 사용한다.

# 3) 문자열도 정렬할 수 있다.
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)
['Alice', 'Bob', 'Charlie']

# 4) 내림차순 정렬도 가능하다.
numbers = [5,2,8,1]
numbers.sort(reverse=True)
print(numbers)
결과 : [8,5,2,1]

# 5) key를 이용해 "무엇을 기준으로 정렬할지" 정할 수 있다.(중요)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
students.sort(key=lambda student: student["score"])
또는 
def get_score(student):
    return student["score"]
students.sort(key=get_score)

의미: 각 students에서 student["score"]를 꺼내서 그 값을 기준으로 정렬해라.
결과:
[
    {"name": "Charlie", "score": 78},
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92}
]

## lambda : 파이썬에서 이름 없이 짧게 만드는 함수
## 'lambda 매개변수: 반환값' 구조
lambda x:x*2 = def double(x): return x*2

3. set()
# 중복을 허용하지 않고, 원소를 빠르게 찾기 위한 자료구조이다.
numbers = set([1,2,2,3,3,3])
print(numbers) 결과 = {1,2,3}
# 핵심 원리는 해시이다.
numbers = {10, 20, 30}에서
10 20 30 순서대로 저장해두고 찾는것이 아닌, 각 값을 hash()라는 함수를 통해 특정
위치와 연결한다.
개념적으로,
10 → hash(10) → 어떤 저장 위치
20 → hash(20) → 어떤 저장 위치
30 → hash(30) → 어떤 저장 위치
따라서 
20 in numbers를 하면 리스트처럼 처음부터 하나씩 찾는것이 아니라
20
 ↓
hash(20)
 ↓
20이 있을 것으로 예상되는 위치로 바로 이동
 ↓
확인
하는 방식이다.
그래서 평균 시간 복잡도가
list에서 in → O(n)
set에서 in  → O(1)
# 중복이 제거되는 이유도 해시 구조 때문이다.
numbers = set()

numbers.add(10)
numbers.add(10)
numbers.add(10)

print(numbers) 결과 = {10}

hash(10)
 ↓
해당 위치 확인
 ↓
이미 10이 있음
 ↓
추가하지 않음

# 인덱싱은 불가능하다(리스트와 구분되는 특징).
numbers = {10, 20, 30}
print(numbers[0])   # 오류

4. 리스트 순회 방법
1) 값만 필요할 때
nums = [10, 20, 30]
for num in nums:
    print(num)
에서 num은 인덱스가 아니라 실제 값.
즉, for i in nums: 라고 쓰면 
i는 0,1,2가 아닌 10,20,30이 된다.

따라서 
for i in nums:
    print(nums[i])
에서 i가 10,20,30이기 때문에 nums[10]같은 접근을 하게된다.

2) 인덱스가 필요할 때
for i in range(len(nums)):
    print(nums[i])

3) 인덱스와 값 둘 다 필요
for i, num in enumerate(nums):

"""
"""
방법1: 이중 반복문 사용
시간 복잡도: O(n²)
공간 복잡도: O(k) - k는 중복 원소 개수
"""
# TODO: 이중 반복문으로 중복 찾기
## i번째 원소와 i+1 이후의 모든 원소를 비교
## 같은 원소를 찾으면 duplicates에 추가 (중복 추가 방지 필요)
pass

# 1) 4와 같은 원소 리스트에 없음 -> 점프
# 2) 3과 같은 원소 있음 -> 3을 리스트에 추가
# 3) 2와 같은 원소 있음 -> 2를 리스트에 추가
# .
# .
# .
# 순회 완료 되면 결과 반환

def find_duplicates_brute_force(nums):
    duplicates = [] # 빈 리스트 생성
    n = len(nums)   # 입력 리스트 길이 저장
    for i in range(n):        
        for j in range(n):                       
            if j > i and nums[i] == nums[j]: # 현재 원소와 다른 원소 비교
                if(nums[i] not in duplicates): duplicates.append(nums[i])               
    return duplicates

"""
방법2: 정렬 후 인접 원소 비교
시간 복잡도: O(n log n) - 정렬
공간 복잡도: O(1) - 정렬을 in-place로 수행
"""
# TODO: 배열을 정렬하세요 (nums.sort() 사용)
pass
# TODO: 인접한 원소를 비교하여 중복 찾기
# i와 i+1 원소가 같고, duplicates에 없으면 추가
pass

def find_duplicates_sorting(nums):
    if not nums: # nums가 비어있으면 빈 리스트 반환
        return []    
    nums.sort() # 정렬    
    duplicates = []        
    for i in range(len(nums)):        
            if i == len(nums)-1: break
            if nums[i]==nums[i+1] and nums[i] not in duplicates:            
                duplicates.append(nums[i])
        
    return duplicates

"""
방법3: 해시 집합 사용
시간 복잡도: O(n)
공간 복잡도: O(n)
"""
# TODO: 각 원소를 순회하면서
## 이미 seen에 있으면 duplicates에 추가
## 없으면 seen에 추가
pass

# hash 집합은 중복을 허용하지 않음
# seen에 없다면 seen에 넣음
# 다음 시행에서 확인한 원소가 seen에 있다면 중복된 원소이므로
# 해당 원소를 duplicate에 삽입

def find_duplicates_hash(nums):
    seen = set()
    duplicates = set()    
    
    for i in range(len(nums)):
        if nums[i] in seen:
            duplicates.add(nums[i])
        else : 
            seen.add(nums[i])
    return list(duplicates)

"""실행 시간 측정 헬퍼 함수"""
def measure_time(func, nums, method_name):    
    result = func(nums[:])  # 복사본 전달
    print(f"{method_name}: {sorted(result)}")
    print()

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 작은 배열
    print("=== 테스트 케이스 1: 작은 배열 ===")
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"입력: {nums1}\n")
    
    result1 = find_duplicates_brute_force(nums1)
    print(f"방법1 (Brute Force): {sorted(result1)}")
    
    result2 = find_duplicates_sorting(nums1)
    print(f"방법2 (Sorting): {sorted(result2)}")
    
    result3 = find_duplicates_hash(nums1)
    print(f"방법3 (Hash): {sorted(result3)}")
    print()
    
    # 테스트 케이스 2: 큰 배열로 성능 비교
    print("=== 테스트 케이스 2: 성능 비교 (n=1000) ===")
    import random
    random.seed(42)  # 동일한 결과를 위한 시드 설정
    nums2 = [random.randint(1, 500) for _ in range(1000)]
    
    measure_time(find_duplicates_brute_force, nums2, "방법1 (O(n²))")
    measure_time(find_duplicates_sorting, nums2, "방법2 (O(n log n))")
    measure_time(find_duplicates_hash, nums2, "방법3 (O(n))")
    
    print("=== 복잡도 분석 요약 ===")
    print("방법1 - Brute Force:")
    print("  시간: O(n²), 공간: O(k)")
    print("  특징: 간단하지만 느림")
    print()
    print("방법2 - Sorting:")
    print("  시간: O(n log n), 공간: O(1)")
    print("  특징: 추가 메모리 없이 효율적")
    print()
    print("방법3 - Hash:")
    print("  시간: O(n), 공간: O(n)")
    print("  특징: 가장 빠르지만 메모리 사용")


