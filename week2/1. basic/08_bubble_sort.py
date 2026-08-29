"""
[버블 정렬 구현]

문제 설명:
- 버블 정렬(Bubble Sort) 알고리즘을 구현합니다.
- 인접한 두 원소를 비교하여 정렬하는 방식입니다.
- 가장 큰 원소가 배열의 끝으로 "버블"처럼 이동합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [64, 34, 25, 12, 22, 11, 90]
출력: [11, 12, 22, 25, 34, 64, 90]

힌트:
- 외부 반복문: n-1번 실행
- 내부 반복문: 인접한 원소 비교 및 교환
- 최적화: 교환이 없으면 이미 정렬된 것이므로 조기 종료
"""

"""
사전지식
1. 버블 정렬
# 서로 이웃한 두 값을 비교해서 '순서'가 잘못되어 있으면 교환하는 작업을 반복하는 정렬 방법

ex) nums = [5, 3, 4, 1]
#1 왼쪽 두개부터 비교
[5, 3, 4, 1]
 ↑  ↑
5 > 3 이므로 교환
↓
[3, 5, 4, 1]

#2 다음 두 값 비교
[3, 5, 4, 1]
    ↑  ↑
5 > 4 → 교환
↓
[3, 4, 5, 1]

#3 다시 다음 두 값 비교
[3, 4, 5, 1]
       ↑  ↑
5 > 1 → 교환
↓
[3, 4, 1, 5]
"""

"""
버블 정렬 구현

Args:
    arr: 정렬할 배열

Returns:
    정렬된 배열
"""

# TODO: 외부 반복문 - n-1번 반복
# 각 패스마다 가장 큰 원소가 끝으로 이동
## TODO: 내부 반복문 - 인접한 원소 비교
## 0부터 n-i-1까지 반복 (이미 정렬된 뒷부분 제외)
## TODO: 인접한 두 원소 비교 및 교환
## arr[j] > arr[j+1]이면 교환
## 외부 반복문: n-1번 실행

def bubble_sort(arr):
    n = len(arr)        
    for i in range(n-1):  # 외부 반복문: 내부 반복문을 반복 시행
        for j in range(n-i-1): # 내부 반복문 현재 원소가 다음것보다 크면 교환
            if arr[j]>arr[j+1]: 
                tempArr = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tempArr    
    return arr

"""
최적화된 버블 정렬 (조기 종료 포함)

Args:
    arr: 정렬할 배열

Returns:
    정렬된 배열
"""
# TODO: 내부 반복문과 교환 로직 구현
# 교환이 발생하면 swapped = True 설정        
pass

# TODO: 교환이 없으면 이미 정렬된 것이므로 break
pass

# 한번 더 체크
def bubble_sort_optimized(arr):
    n = len(arr)    
    for i in range(n):
        swapped = False  
        for j in range(n-i):
            if arr[j]>arr[j+1]: # 교환 발생하면 swapped = True
                swapped = True
                tempArr = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tempArr
            if swapped == False: # 교환 없으면 해당 시행에서는 정렬이 완료된 것이므로 내부 반복 종료
                break               
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = bubble_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2: 이미 정렬된 배열
    arr2 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 2: 이미 정렬됨 ===")
    print(f"정렬 전: {arr2}")
    result2 = bubble_sort_optimized(arr2.copy())
    print(f"정렬 후: {result2}")
    print("최적화 버전은 1번의 패스만 수행")
    print()
    
    # 테스트 케이스 3: 역순 배열
    arr3 = [5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = bubble_sort(arr3.copy())
    print(f"정렬 후: {result3}")


