"""
[그리디 - 회의실 배정]

문제 설명:
- 하나의 회의실에 여러 회의를 배정합니다.
- 각 회의는 시작 시간과 종료 시간이 있습니다.
- 최대한 많은 회의를 배정하려고 합니다.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- 배정된 회의 개수

예제:
입력: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
출력: 4개
선택: [(1, 4), (5, 7), (8, 11), (12, 14)]

힌트:
- 종료 시간이 빠른 회의부터 선택!
- 이전 회의가 끝난 후에 시작하는 회의만 선택
"""

from collections import deque

# 방법 1 시간 복잡도 고려 안하고 작성 - deque 사용하려 했으나, 중간 값 반환하면서 제거가 힘들어서 사용안함
# def select_meetings(meetings):
#     """
#     회의실 배정 (그리디)
    
#     Args:
#         meetings: [(시작, 종료)] 리스트
    
#     Returns:
#         (배정된 회의 개수, 선택된 회의 리스트)
#     """
#     # TODO: 회의가 없으면 0 반환
#     if not meetings: return 0
    
#     # TODO: 종료 시간 기준으로 정렬
#     # 현재 회의 :(시작 시간, 종료 시간)    
#     new_meetings = deque()

#     for meeting in meetings:
#         start, finished = meeting
#         meeting = finished, start
#         new_meetings.append(meeting)

#     selected = []
    
#     # TODO: 첫 번째 회의 선택
#     selected.append(new_meetings.popleft()) 
    
#     # TODO: 나머지 회의들 확인
#     ## 이전 회의가 끝난 후 시작하는 회의만 선택
#     # 이전 회의 끝난 시각 =< 새로 시작하는 회의 시각
#     meeting_count = 0

#     for i in range(len(new_meetings)):
#         if new_meetings[i][1] >= selected[meeting_count][0]:
#             meeting_count += 1
#             selected.append(new_meetings.pop(i))

#방법 1 시간 복잡도 고려 안하고 작성 => 문제점: 종료 시간과 시작 시간이 뒤집힘
def select_meetings_1(meetings):
    # TODO: 회의가 없으면 0 반환
    if not meetings: 
        return 0
    
    # TODO: 종료 시간 기준으로 정렬
    # 현재 회의 :(시작 시간, 종료 시간)    
    new_meetings = []

    for meeting in meetings:
        start, finished = meeting
        meeting = finished, start
        new_meetings.append(meeting)

    selected = []
    
    # TODO: 첫 번째 회의 선택
    # selected.append(new_meetings.pop(0)) 
    selected.append(new_meetings[0]) 
    
    # TODO: 나머지 회의들 확인
    ## 이전 회의가 끝난 후 시작하는 회의만 선택
    # 이전 회의 끝난 시각 =< 새로 시작하는 회의 시각
    meeting_count = 0

    for i in range(len(new_meetings)):
        if new_meetings[i][1] >= selected[meeting_count][0]:
            meeting_count += 1
            selected.append(new_meetings[i])

    return len(selected), selected

#방법 2 람다 활용한 정렬
def select_meetings_2(meetings):
    if not meetings: 
        return 0

    selected = []

    # arr.sort(key=특정 함수)
    # lambda : 따로 함수를 정의하지 않고 사용할 때 쓰임
    # lambda 매겨변수: 반환할 값
    # 아래 식에서 time에는 meetings의 원소가 하나씩 들어옴
    # time[1]은 하나의 원소(튜플)의 두번째 값을 반환함
    # 따라서 아래는 종료시간 기준 정렬이 되는 것
    # 만약 시작 시간 기준이라면 meetings.sort(key=lambda time: time[0])

    meetings.sort(key=lambda time: time[1])

    # 종료시간이 가장 빠른 회의 빼서 선택된 회의 리스트에 넣기    
    # selected.append(meetings.pop(0))
    # 출력에서 전체 회의 리스트도 보기 때문에 pop이 아닌 인덱스 접근을 통한 삽입 
    selected.append(meetings[0])

    # 다음 회의 넣기: 이전 회의가 끝나는 시간보다 시작시간이 클 경우 뽑기
    # 넣은 순서를 기억해야 하므로 변수 생성
    meeting_cnt = 0

    for meeting in meetings:
        if meeting[0] > selected[meeting_cnt][1]:
            meeting_cnt += 1
            selected.append(meeting)

    return len(selected), selected


# 방법 3 : 재귀 호출 이용
def select_meetings(meetings):
    # 종료 시간 기준으로 정렬 
    # 원소가 튜플이고 종료시간이 각 튜플의 두번째 원소 이므로 인덱스를 1로 설정
    meetings.sort(key=lambda meeting: meeting[1])

    # 나중에 변환된 meetings를 초기화 하기 위한 변수
    sorted_meetings = meetings

    # 정렬은 완료했고, 종료조건(base case) 필요
    # meetings가 비어있으면 종료
    if meetings==[]: return 0, []        

    # 선택된 회의 빈 배열 생성
    selected = []

    # 첫번째 회의 선택
    selected.append(meetings[0])

    # 다음 회의 시작 시간 > 이전 회의 종료 시간 이면 배열에 넣기
    # 아니면 빼주기
    # 한번에 하나 씩 넣기(하나 넣으면 재귀 호출)

    next_candidate = meetings.pop(0)

    if meetings[0][0] > selected[0][1]:
        selected.append(next_candidate)    

    select_meetings(meetings)

    # for i in range(len(meetings)):
    #     if meetings[i][0] > selected[0][1]:
    #         selected.append(meetings.pop(i))
    #         select_meetings(meetings)
    #         break 
    #     else: 
    #         meetings.pop(i)

    return len(selected), selected


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()
    
    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")


