"""
[그래프 기본 - 인접 리스트 표현]

문제 설명:
- 그래프를 인접 리스트로 표현합니다.
- 간선(edge)을 추가하고 출력합니다.
- 방향 그래프와 무방향 그래프를 구분합니다.

입력:
- vertices: 정점(vertex) 개수
- edges: 간선 리스트

출력:
- 각 정점에 연결된 정점들

예제:
정점: 4개 (0, 1, 2, 3)
간선: [(0,1), (0,2), (1,2), (2,3)]

무방향 그래프:
0 → [1, 2]
1 → [0, 2]
2 → [0, 1, 3]
3 → [2]

힌트:
- 딕셔너리 사용: {정점: [연결된 정점들]}
- 무방향 그래프는 양방향 추가
"""

def create_graph(vertices, edges, directed=False):
    """
    그래프 생성 (인접 리스트)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
        directed: 방향 그래프 여부
    
    Returns:
        그래프 딕셔너리
    """
    # TODO: 빈 그래프 초기화
    graph = dict()    
    
    # TODO: 간선 추가
    ## 간선 추가 (u에서 v로)
    # u : 출발, v : 도착
    # u = key, v = value list
    # edges : 튜플 리스트            

    # 방향 그래프
    if directed == True:
        for i in range(vertices):            
            value = []            
            graph[i] = value

            for u, v in edges:
                if i != u:  
                    continue                
                value.append(v)  
        return graph

    # 무방향 그래프
    else :
        edges_inv = [edge[::-1] for edge in edges]
        totals = edges + edges_inv   
        totals.sort()

        for i in range(vertices):            
            value = []            
            graph[i] = value

            for u, v in totals:
                if i != u:  
                    continue                
                value.append(v)              

        return graph

"""    # 방향 그래프 

    # 외부 순회: 모든 정점
    # 내부 순회: 간선
    for i in range(vertices):
        # 빈 리스트 생성
        value = []
        # 키-값 매칭
        graph[i] = value

        for u, v in edges:
            if i != u:  continue
            # 도착점 리스트 생성
            value.append(v)                    
                
    # if directed :
    #     for u,v in edges:
    #         # 도착점 리스트로 생성
    #         value = [v]        
    #         # 시작점과 도착점 연결
    #         if graph.get(u) is None:             
    #             graph[u] = value
    #         else :
    #             end = graph.get(u)
    #             end.append(v)
    if directed : 
        return graph
    
    ## 무방향 그래프면 반대 방향도 추가    
    # 간선 리스트 내부 튜플 뒤집기    
    for i in range(vertices):
        for v, u in edges:
            if i != u: continue
            graph.get(i).append(v)
    
    return graph"""

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 무방향 그래프
    vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    
    print("=== 무방향 그래프 ===")
    graph = create_graph(vertices, edges, directed=False)
    for vertex, neighbors in graph.items():
        print(f"{vertex} → {neighbors}")
    print()
    
    # 테스트 케이스 2: 방향 그래프
    print("=== 방향 그래프 ===")
    graph_directed = create_graph(vertices, edges, directed=True)
    for vertex, neighbors in graph_directed.items():
        print(f"{vertex} → {neighbors}")


