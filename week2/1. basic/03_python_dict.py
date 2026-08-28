"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""

# 학생 정보를 리스트로 입력받음
# 학생들의 평균 점수 계산
# 평균 점수 이상인 학생 찾기
# 리스트에 저장
# 평균점수와 리스트 출력(tuple)

# 사전지식
# 1. dictionary
# 1) 키(key)와 값(value)을 한 쌍으로 저장하는 자료구조이다 #
# 인덱스 기반인 리스트와 달리, key를 이용해서 데이터를 찾음
# fruit = {
#     "red":"apple",
#     "yellow":"banana"
# }
# print(fruit["red"])
# dictionary[key]를 하면 key에 연결되어 있는 value를 가져온다

# 2) 내부적으로는 Hash라는 것을 사용한다 #
# dictionary가 빠른 이유는 내부적으로 해시 테이블이라는 구조를 사용하기 때문
# ex)
# scores = {
#     "E": 3,
#     "I": 1,
#     "S": 2
# }
# scores["E"]를 호출하면 E를 처음부터 하나씩 비교하는 것이 아니라 아래와 같은 과정을 거침
# "E"
#  ↓
# hash("E")
#  ↓
# 특정 저장 위치 계산
#  ↓
# 그 위치에서 value 발견
#  ↓
# 3
# '평균적으로'
# 조회 추가 삭제가 O(1)
# 반면 리스트에서 특정 값을 직접 찾으려면
# if "apple" in array: 
# 앞에서부터 확인할 수도 있기 때문에 일반적으로 O(n)

# 3) dictionary에서는 key가 고유해야 한다. #
# scores = {
#     "E": 1,
#     "E": 5
# }
# print(scores) : {'E', 5} 와 같이 뒤에 들어온 값으로 덮어씌워진다.

# 4) value는 중복되어도 된다. #

# 5) dictionary에 값을 추가하는 원리 #
# scores = {} 빈 딕셔너리 만들고
# scores["E"] = 1 하면
# {
#     "E": 1
# }
# 가 된다.

# 다시 scores["I"] = 2하면
# {
#     "E": 1,
#     "I": 2
# }
# 가 된다.

# 6) 기존값을 수정할 수도 있다. #
# scores = {
#     "E": 1
# }
# scores["E"] = 5
# 하면 
# {
#     "E": 5
# }
# 가 된다. 아래와 같이
# scores["E"] += 1 하면
# scores["E"] = scores["E"] + 1
# scores = {
#     "E": 0,
#     "I": 0
# }

# scores["E"] += 1
# scores["E"] += 1

# print(scores)
# 결과 : {'E': 2, 'I': 0}

# 7) Key가 존재하지 않으면? #
# scores = {
#     "E" : 3
# }

# print(scores["I"])
# "I"라는 key가 없기 때문에: KeyError가 발생

# 그래서 안전하게 가져오려면 get()을 많이 사용
# print(scores.get("I"))
# 결과 : None

# 기본값 지정도 가능.
# print(scores.get("I", 0))
# 결과 : 0

# 8) dictionary 반복문 #
# dictionary를 for문으로 돌리면 기본적으로 key가 나온다.
# scores = {
#     "E": 3,
#     "I": 1,
#     "S": 2
# }
# for key in scores:
#     print(key)
# 결과 E I S
# 값 까지 가져오려면
# for key in scores:
#     print(key, scores[key])
# 또는 보통 아래와 같이 사용
# for key,value in scores.items():
#     print(key, value)
# 결과는 
# E 3
# I 1
# S 2
# 이와 같이 딕셔너리는 순서를 기억할 필요 없이 이름 자체를 key로 사용한다는 장점이 있다.

## 2. list 사용법
# # 값을 뒤에 추가 : .append(value)
# ex)
# numbers = [10, 20, 30, 40]
# numbers.append(50)
# 결과: [10, 99, 30, 40, 50]
# # 특정 위치에 추가 : .insert(index, value)
# numbers.insert(1,15)
# # 값을 삭제 : .remove(value) or del list[index]
# numbers.remove(30), del numbers[0]
# # 마지막 값을 꺼내면서 리스트에서 지운다면 : value = list.pop()
# # 리스트의 길이는 : len()
# # 빈 리스트는 array = [] 또는 array = list()

# students0 = [
#         {"name": "Alice", "score": 85},
#         {"name": "Bob", "score": 92},
#         {"name": "Charlie", "score": 78},
#         {"name": "David", "score": 95}
#     ]

# # students0 는 리스트 안에 딕셔너리들이 들어있는 구조
# scores = []

# for student in students0:
#     scores.append(student["score"])

# print(scores)

# 풀이 방법 1: 기본 풀이
# def find_above_average_students(students):
#     """
#     평균 점수 이상인 학생들을 찾는 함수
    
#     Args:
#         students: 학생 정보 딕셔너리 리스트
    
#     Returns:
#         tuple: (평균 점수, 평균 이상 학생 이름 리스트)
#     """
#     # TODO: 모든 학생의 점수를 리스트로 추출하세요
#     pass
    
#     # TODO: 평균 점수를 계산하세요
#     pass
    
#     # TODO: 평균 이상인 학생들의 이름을 리스트로 추출하세요
#     pass

#     scores = list() # 학생들 점수 리스트 생성
#     for student in students:        
#         scores.append(student["score"]) # 점수 추출

#     average = sum(scores)/len(scores)

#     above_average_students = [] # 평균 이상 학생 리스트 생성
#     for student in students:
#         if (student["score"] > average):
#             above_average_students.append(student["name"])
                
#     return average, above_average_students

# 풀이 방법 2 : 리스트 컴프리헨션 사용
def find_above_average_students(students):
    # 점수 리스트 생성
    scores = [student["score"] for student in students] #[저장할 값 for 변수 in 반복할대상]
    # 평균 계산
    average = sum(scores)/len(scores)
    # 학생 리스트 생성
    above_average_students = [student["name"] for student in students if student["score"] > average]

    return average, above_average_students


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")

