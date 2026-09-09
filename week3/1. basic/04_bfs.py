"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque
"""
너비 우선 탐색

Args:
    graph: 그래프 딕셔너리
    start: 시작 정점

Returns:
    방문 순서 리스트
"""

def bfs(graph, start):
    # 방문 리스트
    visited = []

    # 방문 체크용
    queue = deque()     
    visited_set = set()

    # 방문한 정점 리스트와 큐, 해시집합에 넣기
    visited.append(start)
    queue.append(start)
    visited_set.add(start)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 정점 꺼내기
        checked = queue.popleft()

        # 꺼낸 정점의 인접 정점 확인
        for vertex in graph[checked]:
            if vertex not in visited_set:
                visited_set.add(vertex)
                visited.append(vertex)
                queue.append(vertex)                
                           
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

