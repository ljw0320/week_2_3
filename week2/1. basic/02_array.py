"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

# 사전 지식
# 1. 배열(리스트)
# array = [
#     [1,2],
#     [3,4]
# ]
# array
#  ├─ array[0] → [1, 2]
#  └─ array[1] → [3, 4]
# array[0][0] 왼쪽 위
# array[0][1] 오른쪽 위
# array[1][0] 왼쪽 아래
# array[1][1] 오른쪽 아래
# 값을 출력하거나 변경도 가능함
# print(array[0][0]) = 1
# array[0][0] = -1
# print(array[0][0]) = -1
# 크기를 변수로 하여 배열을 만드는 방법도 가능
# rows = 2
# cols = 3
# array = [[0]*cols for _ in range(rows)] (여기서 _ 는 값은 필요없고 반복만 할 때 사용)
# print(array)
# for i in range(3):  # i를 사용할 때
# for _ in range(3):  # 값은 필요 없고 3번 반복만 할 때(단 _도 실제로는 변수라 값을 가지고는 있음.)
# 2차원 배열끼리 값을 삽입하는 법
# matrix_1[a][b] = matrix_2[c][d]와 같이 각 행과 열을 입력하여 원소에 접근한 후 대입한다.

## 2. 제곱근
# import math로 sqrt라는 제곱근 메소드 사용 가능
# import math
# x = math.sqrt(16)
# print(x)
# 또는 거듭제곱 연산자로도 사용가능
# x = 16 ** 0.5
# print(x)

# 입력 배열의 행과 열의 크기가 다르면 return
# 배열의 크기는 동일함
# 배열의 크기를 우선 파악
# 신규 배열 생성
# 생성한 배열에 90도 회전한 원소 배치
# 완료 후 배열 반환 

"""
2차원 배열을 시계방향으로 90도 회전

Args:
    matrix: N x N 2차원 리스트

Returns:
    회전된 2차원 리스트
"""

# TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
pass
    
# TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
# 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동
pass

def rotate_matrix_90(matrix):    
    n = len(matrix)
    # 2차원 배열 생성
    rotated = [[0]*n for _ in range(n)]    
    # (0,0) , (0,1), (0,2) 0, 1, 2
    # (1,0) , (1,1), (1,2) 3, 4, 5
    # (2,0) , (2,1), (2,2) 6, 7, 8           
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    return rotated

"""배열을 보기 좋게 출력하는 헬퍼 함수"""
def print_matrix(matrix):    
    for row in matrix:
        print(row)



# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


