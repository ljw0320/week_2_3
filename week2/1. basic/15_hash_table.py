"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 "해시 테이블"로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)

힌트:
- 딕셔너리 사용
- 평균: sum(scores.values()) / len(scores)
- 최고점 : max(scores.values())
- 최고점 학생: max(scores, key=scores.get)
: scores에서 최고 value인 key를 얻을 수 있음
"""
"""
학생 성적 관리 시스템

Args:
    students: {이름: 점수} 딕셔너리

Returns:
    평균, 최고점 학생 이름, 최고점
"""

"""
사전지식
dictionary method
1. 값 가져오기:	dict[key]
2. 안전하게 값 가져오기(없는 key일 경우 None반환):	dict.get(key) 
3. 모든 키 확인:	dict.keys()
4. 모든 값 확인:	dict.values()
5. 키와 값 같이 순회:	dict.items()
6. 삭제:	dict.pop(key)
7. 딕셔너리에 특정 키 있는지 확인(in): if "score" in student

"""
# TODO: 평균 점수 계산
pass


# TODO: 최고 점수 학생 찾기
pass

def manage_grades(students):    
    # 입력된 dictionary에서 점수 평균, 최고점 학생, 최고점 산출
    average = sum(students.values())/len(students)
    top_student = max(students, key=students.get)    
    top_score = max(students.values())
    return average, top_student, top_score

"""
특정 학생의 점수 조회

Args:
    students: 학생 딕셔너리
    name: 찾을 학생 이름

Returns:
    점수 (없으면 None)
"""
# TODO: students에서 name 찾기
pass

def find_student_score(students, name):    
    # 루프로 순회하여 딕셔너리의 key 탐색
    # name 있으면 해당 score 반환
    if name in students:
        return students.get(name)        
    # 없으면 None 반환
    return None

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {top_name} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")


