from collections import deque

def bfs(graph, start, visited):     # Queue 사용
    # 시작 노드 큐에 삽입 후 방문처리
    queue = deque([start])
    visited[start] = True

    # 큐가 빌때까지 반복
    while queue:
        # ★큐에서 꺼내서 출력
        v = queue.popleft()
        print(v, end=' ')

        # 현재 노드와 연결된 다른 노드 중 아직 방문하지 않은 원소 큐에 삽입 후 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드 정보 2차원 리스트
graph = [
    [],
    [2, 3],
    [4, 5],
    [6, 7],
    [2],
    [2],
    [3],
    [3]
]

visited = [False] * 8   # 방문처리 리스트
bfs(graph, 1, visited)  # 1번 노드에서 시작
